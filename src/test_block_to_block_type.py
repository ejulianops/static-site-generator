import unittest

from block_to_block_type import block_to_block_type

class TestMarkdownBlockType(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(block_to_block_type(''), "paragraph")

    def test_heading(self):
        mock_heading = "###### Introduction"
        self.assertEqual(block_to_block_type(mock_heading), "heading")

    def test_paragraph(self):
        mock_paragraph = "This is a paragraph."
        self.assertEqual(block_to_block_type(mock_paragraph), "paragraph")

    def test_code(self):
        mock_code = "```\nprint('Hello World')\n```"
        self.assertEqual(block_to_block_type(mock_code), "code")

    def test_quote(self):
        mock_quote = "> This is a quote\n> Continued quote"
        self.assertEqual(block_to_block_type(mock_quote), "quote")

    def test_unordered_list(self):
        mock_unordered_list = "* Item 1\n* Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(mock_unordered_list), "unordered list")

    def test_ordered_list(self):
        mock_ordered_list = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(mock_ordered_list), "ordered list")

    def test_paragraph_with_unordered_list(self):
        mock_mixed = "This is a paragraph\n* Unordered item"
        self.assertEqual(block_to_block_type(mock_mixed), "paragraph")

    def test_paragraph_with_code(self):
        mock_mixed_code = "This is a paragraph\n```\ncode block\n```"
        self.assertEqual(block_to_block_type(mock_mixed_code), "paragraph")

if __name__ == '__main__':
    unittest.main()
