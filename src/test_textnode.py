import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    # Different text
    def test_not_equal_due_to_text(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a different text", "bold")
        self.assertNotEqual(node1, node2)

    # Different text_type
    def test_not_equal_due_to_text_type(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node1, node2)

    # url Differences
    def test_not_equal_due_to_url(self):
        node1 = TextNode("This is a text node", "bold", "http://example.com")
        node2 = TextNode("This is a text node", "bold", "http://different.com")
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
