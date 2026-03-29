import re

from nodes.block import BlockType


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def block_to_block_type(block):
    if re.match("^#{1,6} ", block):
        return BlockType.HEADING

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    lines = block.split("\n")
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    if all(line.startswith(f"{i + 1}. ") for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def extract_title(markdown):
    lines = markdown.split("\n")

    title = ""
    for line in lines:
        if line.startswith("# "):
            title = line.strip("# ")

    if title == "":
        title = None

    return title
