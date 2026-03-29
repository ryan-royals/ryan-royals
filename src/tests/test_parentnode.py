import unittest

from nodes.parentnode import ParentNode
from nodes.leafnode import LeafNode

# ParentNode(tag, children, props=None)


class TestParentNode(unittest.TestCase):
    def test_basic_eq(self):
        child_node = LeafNode("span", "child")

        node = ParentNode("p", child_node, {
            "href": "https://ryanroyals.cloud"})
        node2 = ParentNode("p", child_node, {
            "href": "https://ryanroyals.cloud"})
        self.assertEqual(node, node2)

    def test_basic_neq(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("span", "child2")

        node = ParentNode("p", child_node, {
            "href": "https://ryanroyals.cloud"})
        node2 = ParentNode("p", child_node2, {
            "href": "https://clairewebber.design"})
        self.assertNotEqual(node, node2)

    def test_to_html_with_no_children(self):
        node = ParentNode("p", None, {
            "href": "https://ryanroyals.cloud"})
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(parent_node.to_html(),
                         "<div><span>child</span><span>child2</span></div>")


if __name__ == "__main__":
    unittest.main()
