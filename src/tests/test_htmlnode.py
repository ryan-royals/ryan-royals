import unittest

from nodes.htmlnode import HTMLNode

# HTMLNode(tag=None, value=None, children=None, props=None)


class TestHTMLNode(unittest.TestCase):
    def test_basic_eq(self):
        node = HTMLNode("a", "this is a html node", None, {
                        "href": "https://ryanroyals.cloud"})
        node2 = HTMLNode("a", "this is a html node", None, {
                         "href": "https://ryanroyals.cloud"})
        self.assertEqual(node, node2)

    def test_basic_neq(self):
        node = HTMLNode("a", "this is a html node", None, {
                        "href": "https://ryanroyals.cloud"})
        node2 = HTMLNode("a", "this is a different html node", None, {
                         "href": "https://clairewebber.design"})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(None, None, None, props)
        self.assertEqual(node.props_to_html(),
                         ' href="https://www.google.com" target="_blank"')

    # def no_tag_raw_text(self):
    #     node = HTMLNode(None, "this should be raw text", None, {
    #                     "href": "https://ryanroyals.cloud"})
    #     Assert that the output is just raw text

    # def no_value_has_children(self):
    #     node = HTMLNode(None, None, None, HtmlNode(), None)
    #     Assert that this has no value

    # def no_children_has_value(self):
    #     node = HTMLNode(None, None, "this is a html node", None, None)
    #     Assert that this has no Children

    # def no_props_no_attributes(self):
    #     node = HTMLNode(None, None, "this is a html node", None, None)
    #     Assert that the value has no Attributes


if __name__ == "__main__":
    unittest.main()
