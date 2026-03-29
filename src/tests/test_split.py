import unittest

from nodes.textnode import TextNode, TextType
from split import split_nodes_image, split_nodes_link
from delimeter import split_nodes_delimeter


class SplitNodesDelimeter(unittest.TestCase):
    # --- single-character delimiter: * for italic ---

    def test_italic_only(self):
        nodes = [TextNode("*italic*", TextType.TEXT)]
        expected = [TextNode("italic", TextType.ITALIC)]
        self.assertEqual(split_nodes_delimeter(nodes, "*", TextType.ITALIC), expected)

    def test_italic_at_end(self):
        nodes = [TextNode("text *italic*", TextType.TEXT)]
        expected = [
            TextNode("text ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
        ]
        self.assertEqual(split_nodes_delimeter(nodes, "*", TextType.ITALIC), expected)

    def test_italic_at_start(self):
        nodes = [TextNode("*italic* text", TextType.TEXT)]
        expected = [
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(split_nodes_delimeter(nodes, "*", TextType.ITALIC), expected)

    def test_italic_in_middle(self):
        nodes = [TextNode("text *italic* text", TextType.TEXT)]
        expected = [
            TextNode("text ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(split_nodes_delimeter(nodes, "*", TextType.ITALIC), expected)

    def test_italic_multiple_spans(self):
        nodes = [TextNode("*a* and *b*", TextType.TEXT)]
        expected = [
            TextNode("a", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("b", TextType.ITALIC),
        ]
        self.assertEqual(split_nodes_delimeter(nodes, "*", TextType.ITALIC), expected)

    def test_italic_multi_node(self):
        nodes = [
            TextNode("This is a *test*", TextType.TEXT),
            TextNode("This is another *test*", TextType.TEXT),
        ]
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("test", TextType.ITALIC),
            TextNode("This is another ", TextType.TEXT),
            TextNode("test", TextType.ITALIC),
        ]
        self.assertEqual(split_nodes_delimeter(nodes, "*", TextType.ITALIC), expected)

    # --- multi-character delimiter: ** for bold ---

    def test_bold_only(self):
        nodes = [TextNode("**bold**", TextType.TEXT)]
        expected = [TextNode("bold", TextType.BOLD)]
        self.assertEqual(split_nodes_delimeter(nodes, "**", TextType.BOLD), expected)

    def test_bold_in_middle(self):
        nodes = [TextNode("text **bold** text", TextType.TEXT)]
        expected = [
            TextNode("text ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(split_nodes_delimeter(nodes, "**", TextType.BOLD), expected)

    def test_bold_multiple_spans(self):
        nodes = [TextNode("text **a** and **b**", TextType.TEXT)]
        expected = [
            TextNode("text ", TextType.TEXT),
            TextNode("a", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("b", TextType.BOLD),
        ]
        self.assertEqual(split_nodes_delimeter(nodes, "**", TextType.BOLD), expected)

    # --- mid-word guard ---

    def test_mid_word_underscore(self):
        nodes = [TextNode("test_case should not split", TextType.TEXT)]
        expected = [TextNode("test_case should not split", TextType.TEXT)]
        self.assertEqual(split_nodes_delimeter(nodes, "_", TextType.ITALIC), expected)

    def test_mid_word_asterisk(self):
        nodes = [TextNode("re*run should not split", TextType.TEXT)]
        expected = [TextNode("re*run should not split", TextType.TEXT)]
        self.assertEqual(split_nodes_delimeter(nodes, "*", TextType.ITALIC), expected)

    # --- adjacent delimiter guard ---

    def test_single_asterisk_ignores_double(self):
        # ** should not be split when processing * as the delimiter
        nodes = [TextNode("**bold**", TextType.TEXT)]
        expected = [TextNode("**bold**", TextType.TEXT)]
        self.assertEqual(split_nodes_delimeter(nodes, "*", TextType.ITALIC), expected)

    # --- escaped delimiter ---

    def test_escaped_delimiter_treated_as_literal(self):
        # \* on both sides: no split, backslash stripped from output
        nodes = [TextNode(r"\*literal\*", TextType.TEXT)]
        expected = [TextNode("*literal*", TextType.TEXT)]
        self.assertEqual(split_nodes_delimeter(nodes, "*", TextType.ITALIC), expected)

    def test_escaped_delimiter_mixed_with_real(self):
        # \* is literal, the second pair *italic* is a real delimiter
        nodes = [TextNode(r"\* text *italic*", TextType.TEXT)]
        expected = [
            TextNode("* text ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
        ]
        self.assertEqual(split_nodes_delimeter(nodes, "*", TextType.ITALIC), expected)

    # --- error cases ---

    def test_unmatched_delimiter_raises(self):
        nodes = [TextNode("*test", TextType.TEXT)]
        with self.assertRaises(Exception):
            split_nodes_delimeter(nodes, "*", TextType.ITALIC)

    # --- non-TEXT node passthrough ---

    def test_non_text_node_passthrough(self):
        nodes = [TextNode("already bold", TextType.BOLD)]
        expected = [TextNode("already bold", TextType.BOLD)]
        self.assertEqual(split_nodes_delimeter(nodes, "*", TextType.ITALIC), expected)


class TestSplitNodesLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [magical link](https://i.imgur.com/3elNhQu.png) with text after",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "magical link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" with text after", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_multi_node(self):
        nodes = [
            TextNode(
                "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [magical link](https://i.imgur.com/3elNhQu.png)",
                TextType.TEXT,
            ),
            TextNode(
                "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [magical link](https://i.imgur.com/3elNhQu.png)",
                TextType.TEXT,
            ),
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "magical link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "magical link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links_with_blanks(self):
        node = TextNode(
            "[link](https://i.imgur.com/zjjcJKZ.png)[magical link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(
                    "magical link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


class TestSplitNodesImages(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) with text after",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" with text after", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_multi_node(self):
        nodes = [
            TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![magical image](https://i.imgur.com/3elNhQu.png)",
                TextType.TEXT,
            ),
            TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![magical image](https://i.imgur.com/3elNhQu.png)",
                TextType.TEXT,
            ),
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "magical image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "magical image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_with_blanks(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)![magic image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(
                    "magic image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
