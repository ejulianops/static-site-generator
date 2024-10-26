import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    # LeafNode with a tag and a value
    def test_leafnode_with_tag_and_value(self):
        leaf = LeafNode("p", "This is text.")
        self.assertEqual(leaf.to_html(), "<p>This is text.</p>")

    # LeafNode with no tag but with a value
    def test_leafnode_no_tag_with_value(self):
        leaf = LeafNode(value="This is raw text.")
        self.assertEqual(leaf.to_html(), "This is raw text.")

    # LeafNode with a tag, value, and attributes
    def test_leafnode_with_tag_value_attribute(self):
        leaf = LeafNode(tag="a", value="Click!", props={"href": "https://www.santosfc.com"})
        expected_html = '<a href="https://www.santosfc.com">Click!</a>'
        self.assertEqual(leaf.to_html(), expected_html)

    # LeafNode with no value
    def test_leafnode_no_value(self):
        leaf = LeafNode(tag="p", value=None)
        with self.assertRaises(ValueError) as context:
            leaf.to_html()
        self.assertEqual(str(context.exception), 'All leaf nodes must have a value')

    # to_html() What should happen when rendering a basic tag like <p>?
    def test_basic_tag_rendering(self):
        leaf = LeafNode(tag="p", value="This is a paragraph of text.")
        result = leaf.to_html()
        expected_html = "<p>This is a paragraph of text.</p>"
        self.assertEqual(result, expected_html)

    # to_html() What about when there are attributes?
    def test_rendering_with_attributes(self):
        attributes = {"href": "https://www.google.com"}
        leaf = LeafNode(tag="a", value="Click me!", props=attributes)
        result = leaf.to_html()
        expected_html = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(result, expected_html)

    # to_html() What if there's no tag?
    def test_no_tag(self):
        leaf = LeafNode(tag=None, value="This is plain text")
        result = leaf.to_html()
        expected_output = "This is plain text"
        self.assertEqual(result, expected_output)

    # to_html() What if there's no value?
    def test_no_value_raises_error(self):
        leaf = LeafNode(tag="p", value=None)
        with self.assertRaises(ValueError):
            leaf.to_html()

if __name__ == "__main__":
    unittest.main()
