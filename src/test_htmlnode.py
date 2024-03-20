import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq_props_to_html(self):
        props_node = HTMLNode(
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        actual = props_node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(actual, expected)

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_eq_parent_node_to_html_no_props(self):
        parent_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        actual = parent_node.to_html()
        expected = (
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )
        self.assertEqual(actual, expected)

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_eq_parent_node_to_html_parent_node_in_children(self):
        parent_node = ParentNode(
            "p",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                )
            ],
        )
        actual = parent_node.to_html()
        expected = (
            "<p><p><b>Bold text</b>Normal text"
            + "<i>italic text</i>Normal text</p></p>"
        )
        self.assertEqual(actual, expected)

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text"
            + "<i>italic text</i>Normal text</h2>",
        )

    def test_eq_leaf_node_to_html_with_props(self):
        leaf_note = LeafNode(
            "a", "Click me!", {"href": "https://www.google.com"}
        )
        actual = leaf_note.to_html()
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
