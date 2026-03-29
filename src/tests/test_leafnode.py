import unittest

from nodes.leafnode import LeafNode

# LeafNode(tag=None, value=None, props=None)


class TestLeafNode(unittest.TestCase):
    def test_basic_eq(self):
        node = LeafNode("a", "this is a leaf node", {
                        "href": "https://ryanroyals.cloud"})
        node2 = LeafNode("a", "this is a leaf node", {
                         "href": "https://ryanroyals.cloud"})
        self.assertEqual(node, node2)

    def test_basic_neq(self):
        node = LeafNode("a", "this is a leaf node", {
                        "href": "https://ryanroyals.cloud"})
        node2 = LeafNode("a", "this is a different leaf node", {
                         "href": "https://clairewebber.design"})
        self.assertNotEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leat_to_raw_string(self):
        node = LeafNode(None, "this is raw string", None)
        self.assertEqual(node.to_html(), "this is raw string")

    def test_no_value_error(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    # def no_tag_raw_text(self):
    #     node = LeafNode(None, "this should be raw text", None, {
    #                     "href": "https://ryanroyals.cloud"})
    #     Assert that the output is just raw text

    # def no_value_has_children(self):
    #     node = LeafNode(None, None, None, HtmlNode(), None)
    #     Assert that this has no value

    # def no_children_has_value(self):
    #     node = LeafNode(None, None, "this is a html node", None, None)
    #     Assert that this has no Children

    # def no_props_no_attributes(self):
    #     node = LeafNode(None, None, "this is a html node", None, None)
    #     Assert that the value has no Attributes


if __name__ == "__main__":
    unittest.main()
