import unittest

from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):

    # single block
    def test_single_block(self):
        markdown_input = "This is a single paragraph of text with **bold** and *italic* words."
        expected_output = ["This is a single paragraph of text with **bold** and *italic* words."]
        result = markdown_to_blocks(markdown_input)
        self.assertEqual(result, expected_output)

    # multiple blocks
    def test_multiple_blocks(self):
        markdown_input = """# This is a heading

This is a paragraph of text with **bold** and *italic* words.

* This is the first list item
* This is the second list item"""

        expected_output = [
            "# This is a heading",
            "This is a paragraph of text with **bold** and *italic* words.",
            "* This is the first list item\n* This is the second list item"
        ]
        result = markdown_to_blocks(markdown_input)
        self.assertEqual(result, expected_output)

    # consecutive empty lines
    def test_consecutive_empty_lines(self):
        # Define the markdown input with multiple consecutive blank lines between blocks
        markdown_input = """# Block One


This is block two.


* List item 1
* List item 2"""
        expected_output = [
            "# Block One",
            "This is block two.",
            "* List item 1\n* List item 2"
        ]
        result = markdown_to_blocks(markdown_input)
        self.assertEqual(result, expected_output)

    # leading whitespace

    # trailing whitespace

    # no blocks present

    # block without newline at end
    def test_block_without_newline_at_end(self):
        # Define markdown input with the last block having no trailing newline
        markdown_input = """# Heading 1

This is a paragraph.

* List item 1
* List item 2 without newline"""

        # Define the expected output
        expected_output = [
            "# Heading 1",
            "This is a paragraph.",
            "* List item 1\n* List item 2 without newline"
        ]

        # Call the function and check that the result matches the expected output
        result = markdown_to_blocks(markdown_input)
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
