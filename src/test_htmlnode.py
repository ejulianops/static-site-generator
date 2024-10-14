import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):

    # empty prop
    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    # single prop
    def test_props_to_html_single_prop(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    # multiple prop
    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()
