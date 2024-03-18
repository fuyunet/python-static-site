import unittest

from htmlnode import HTMLNode, LeafNode


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

    def test_eq_leaf_node_to_html_with_props(self):
        leaf_note = LeafNode(
            "a", "Click me!", {"href": "https://www.google.com"}
        )
        actual = leaf_note.to_html()
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
