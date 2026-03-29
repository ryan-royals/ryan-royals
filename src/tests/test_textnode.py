import unittest

from nodes.textnode import TextNode, TextType

# TextNode(text, text_type, url=None)


class TestTextNode(unittest.TestCase):
    def test_basic_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a text node", TextType.BOLD,
                        "http://ryanroyals.cloud")
        node2 = TextNode("This is a text node", TextType.BOLD,
                         "http://ryanroyals.cloud")
        self.assertEqual(node, node2)

    def test_basic_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node but different", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD,
                         "http://ryanroyals.cloud")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
