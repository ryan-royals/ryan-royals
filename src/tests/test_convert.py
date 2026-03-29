import unittest

from nodes.textnode import TextNode, TextType
from convert import (
    text_node_to_html_node,
    text_to_textnodes,
    markdown_to_blocks,
    markdown_to_html_node,
)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_not_valid_type(self):
        node = TextNode("Not a valid Node", None)
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

    def test_text(self):
        text = TextNode("Text Node", TextType.TEXT)
        html = text_node_to_html_node(text)

        self.assertEqual(html.to_html(), "Text Node")
        self.assertEqual(html.props_to_html(), "")
        self.assertEqual(html.tag, None)
        self.assertEqual(html.value, "Text Node")

    def test_bold(self):
        text = TextNode("Bold Text Node", TextType.BOLD)
        html = text_node_to_html_node(text)

        self.assertEqual(html.to_html(), "<b>Bold Text Node</b>")
        self.assertEqual(html.props_to_html(), "")
        self.assertEqual(html.tag, "b")
        self.assertEqual(html.value, "Bold Text Node")

    def test_italic(self):
        text = TextNode("Italic Text Node", TextType.ITALIC)
        html = text_node_to_html_node(text)

        self.assertEqual(html.to_html(), "<i>Italic Text Node</i>")
        self.assertEqual(html.props_to_html(), "")
        self.assertEqual(html.tag, "i")
        self.assertEqual(html.value, "Italic Text Node")

    def test_code(self):
        text = TextNode("Code Text Node", TextType.CODE)
        html = text_node_to_html_node(text)

        self.assertEqual(html.to_html(), "<code>Code Text Node</code>")
        self.assertEqual(html.props_to_html(), "")
        self.assertEqual(html.tag, "code")
        self.assertEqual(html.value, "Code Text Node")

    def test_link(self):
        text = TextNode("Link Text Node", TextType.LINK, "https://ryanroyals.cloud")
        html = text_node_to_html_node(text)

        self.assertEqual(
            html.to_html(), '<a href="https://ryanroyals.cloud">Link Text Node</a>'
        )
        self.assertEqual(html.props_to_html(), ' href="https://ryanroyals.cloud"')
        self.assertEqual(html.tag, "a")
        self.assertEqual(html.value, "Link Text Node")

    def test_image(self):
        text = TextNode(
            "Image Text Node", TextType.IMAGE, "https://ryanroyals.cloud/cat.png"
        )
        html = text_node_to_html_node(text)

        self.assertEqual(
            html.to_html(),
            '<img src="https://ryanroyals.cloud/cat.png" alt="Image Text Node"/>',
        )
        self.assertEqual(
            html.props_to_html(),
            ' src="https://ryanroyals.cloud/cat.png" alt="Image Text Node"',
        )
        self.assertEqual(html.tag, "img")
        self.assertEqual(html.value, "")


class TestTextToTextNodes(unittest.TestCase):
    def test_combined(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            text_to_textnodes(text),
        )

    def test_bold_and_underscore_italic(self):
        # Both ** and _ correctly parsed in the same string
        text = "**bold** and _italic_"
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            text_to_textnodes(text),
        )

    def test_bold_and_asterisk_italic(self):
        # Both ** and * correctly parsed in the same string
        text = "**bold** and *italic*"
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            text_to_textnodes(text),
        )

    def test_asterisk_italic_only(self):
        text = "*italic*"
        self.assertListEqual(
            [TextNode("italic", TextType.ITALIC)],
            text_to_textnodes(text),
        )

    def test_asterisk_italic_in_middle(self):
        text = "text *italic* text"
        self.assertListEqual(
            [
                TextNode("text ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT),
            ],
            text_to_textnodes(text),
        )

    def test_bold_not_split_by_asterisk_italic_pass(self):
        # ** is processed first as BOLD; the * pass should not disturb the resulting BOLD node
        text = "**bold**"
        self.assertListEqual(
            [TextNode("bold", TextType.BOLD)],
            text_to_textnodes(text),
        )

    def test_escaped_underscore_italic_delimiter(self):
        # \_ is treated as a literal _, backslash stripped in output
        text = r"\_not italic\_"
        self.assertListEqual(
            [TextNode("_not italic_", TextType.TEXT)],
            text_to_textnodes(text),
        )

    def test_escaped_asterisk_italic_delimiter(self):
        # \* is treated as a literal *, backslash stripped in output
        text = r"\*not italic\*"
        self.assertListEqual(
            [TextNode("*not italic*", TextType.TEXT)],
            text_to_textnodes(text),
        )

    def test_escaped_delimiter_mixed_with_real(self):
        # \_ is literal, but _italic_ still correctly parses
        text = r"\_ some text _italic_"
        self.assertListEqual(
            [
                TextNode("_ some text ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            text_to_textnodes(text),
        )


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


class TestMarkdownToHtmlNodes(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_codeblock_with_language(self):
        md = """
```python
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><pre><code class="language-python">This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>',
        )


if __name__ == "__main__":
    unittest.main()
