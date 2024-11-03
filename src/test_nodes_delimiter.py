import unittest
from nodes_delimiter import split_nodes_delimiter
from textnode import TextNode
from texttypes import TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_basic_properly_paired(self):
        node = TextNode("This is a `code block` word", TextType.TEXT)
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE), expected)
    
    def test_unmatched_delimiter(self):
        node = TextNode("This is an `unclosed code block", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)
    
    # Add more tests here

if __name__ == '__main__':
    unittest.main()
