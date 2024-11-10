import unittest
import re
from extract_links import extract_markdown_images, extract_markdown_links

class TestMarkdownExtraction(unittest.TestCase):

    def test_extract_markdown_images(self):
        # Test with multiple images
        text = "This has an image ![cat](https://example.com/cat.jpg) and another ![dog](https://example.com/dog.jpg)"
        expected = [("cat", "https://example.com/cat.jpg"), ("dog", "https://example.com/dog.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

        # Test with no images
        text = "This has no images."
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)

        # Test with special characters in image alt text and URL
        text = "Image with special chars ![c@t!](https://example.com/c@t!.jpg)"
        expected = [("c@t!", "https://example.com/c@t!.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links(self):
        # Test with multiple links
        text = "This has a link [to Google](https://www.google.com) and [to OpenAI](https://www.openai.com)"
        expected = [("to Google", "https://www.google.com"), ("to OpenAI", "https://www.openai.com")]
        self.assertEqual(extract_markdown_links(text), expected)

        # Test with no links
        text = "This has no links."
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)

        # Test with special characters in link text and URL
        text = "Check [GitHub!](https://github.com/openai?tab=repositories)"
        expected = [("GitHub!", "https://github.com/openai?tab=repositories")]
        self.assertEqual(extract_markdown_links(text), expected)

# Run the tests
if __name__ == "__main__":
    unittest.main()
