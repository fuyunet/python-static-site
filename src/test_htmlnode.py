import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq_props_to_html(self):
        props_node = HTMLNode(
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        actual = props_node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
