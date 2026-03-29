# delimeter.py
#
# Responsible for splitting a flat list of TextNodes on a given inline delimiter
# (e.g. *, **, _, `) and producing a new flat list where the delimited spans
# have been assigned the appropriate TextType.
#
# --- Parsing model ---
#
# Inline parsing is done as a series of single-delimiter passes over a flat
# node list. Each pass only touches nodes that are still TextType.TEXT; nodes
# that have already been typed (BOLD, ITALIC, CODE, etc.) are passed through
# unchanged. This means the order of passes matters:
#
#   1. ** (bold)    — must come before * so that ** is consumed first and the
#                     individual * pass never sees the asterisks inside **...**
#   2. _  (italic)
#   3. *  (italic)
#   4. `  (code)    — must come last in the delimiter passes because code spans
#                     have highest inline precedence per the GFM spec (section
#                     6.3): content inside a code span is never parsed for
#                     further inline structure.
#
# --- Code-span masking ---
#
# Because * and _ are processed before `, we must ensure that asterisks or
# underscores that appear *inside* a backtick span (e.g. `*.tf`) are never seen
# by the emphasis regex. We achieve this by temporarily replacing every
# `...` span in the raw text with a null-byte-delimited placeholder before
# running the emphasis regex, then restoring the original text into each output
# node afterwards.
#
# The masking step is skipped when the delimiter being processed is ` itself,
# since in that case the backticks are exactly what we want to match.
#
# --- Delimiter matching rules ---
#
# The regex has two alternatives that together implement left- and right-
# flanking delimiter detection:
#
#   Alt 1 — opening (left-flanking):
#     (?<!\\)   not preceded by a backslash (escaped delimiter guard)
#     (?<!{d})  not preceded by the same delimiter (adjacent-delimiter guard)
#     (?<!\w)   not preceded by a word character (mid-word guard)
#     {d}       the delimiter itself
#     (?!{d})   not followed by the same delimiter (adjacent-delimiter guard)
#
#   Alt 2 — closing (right-flanking):
#     (?<!\\)   not preceded by a backslash
#     (?<!{d})  not preceded by the same delimiter
#     {d}       the delimiter itself
#     (?!{d})   not followed by the same delimiter
#     (?!\w)    not followed by a word character (mid-word guard)
#
# The adjacent-delimiter guard uses a *literal* lookaround rather than a
# character class. A character class like [\*\*] deduplicates to [\*], so it
# would incorrectly block single * when ** is the delimiter being tested.
# Literal lookarounds check the full delimiter sequence as a string.
#
# --- Escape handling ---
#
# A delimiter immediately preceded by a backslash (e.g. \*) is skipped by the
# regex. After splitting, each output node has \{delimiter} replaced with the
# bare delimiter character so that the backslash is stripped from the final HTML
# (e.g. \* → *).

import re
from nodes.textnode import TextType, TextNode


def split_nodes_delimeter(old_nodes, delimeter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            # When the delimiter is not a backtick, mask any `...` code spans
            # so that special characters inside them (e.g. * in `*.tf`) are
            # invisible to the emphasis regex.
            if delimeter != "`":
                masked, spans = _mask_code_spans(node.text)
            else:
                masked, spans = node.text, {}

            d = re.escape(delimeter)
            pattern = re.compile(
                rf"(?<!\\)(?<!{d})(?<!\w){d}(?!{d})"
                rf"|"
                rf"(?<!\\)(?<!{d}){d}(?!{d})(?!\w)"
            )
            parts = pattern.split(masked)
            if len(parts) % 2 == 0:
                raise Exception(
                    f"Invalid markdown: unmatched delimiter '{delimeter}'"
                    f" in '{node.text}'"
                )
            for i, part in enumerate(parts):
                if part == "":
                    continue
                node_type = TextType.TEXT if i % 2 == 0 else text_type
                # Restore any masked code spans and strip backslash escapes.
                text = _restore_code_spans(part, spans).replace(
                    f"\\{delimeter}", delimeter
                )
                new_nodes.append(TextNode(text, node_type))
    return new_nodes


def _mask_code_spans(text):
    """Replace every `...` span with a null-byte-keyed placeholder.

    Returns (masked_text, spans) where spans is a dict mapping each
    placeholder key back to the original backtick span text.  Null bytes
    are used as delimiters for the keys because they cannot appear in
    normal markdown source.
    """
    spans = {}

    def replace(m):
        key = f"\x00{len(spans)}\x00"
        spans[key] = m.group(0)
        return key

    masked = re.sub(r"`+.+?`+", replace, text, flags=re.DOTALL)
    return masked, spans


def _restore_code_spans(text, spans):
    """Substitute placeholder keys back to their original backtick span text."""
    for key, original in spans.items():
        text = text.replace(key, original)
    return text
