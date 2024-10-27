import unittest

from textnode import TextNode
from leafnode import LeafNode
from text_node_to_html_node import text_node_to_html_node
from texttypes import TextType

class TestTextNodeToHtmlNode(unittest.TestCase):

    # Test for TextNode with TextType.TEXT
    def test_text_conversion(self):
        # Step 1: Create a TextNode with TextType.TEXT
        text_node = TextNode("example text", TextType.TEXT)        
        # Step 2: Convert it using the function
        result = text_node_to_html_node(text_node)
        # Step 3: Assert that the result is a LeafNode with the correct properties
        self.assertIsInstance(result, LeafNode)  # Check that result is a LeafNode
        self.assertEqual(result.tag, "")  # Check that tag is an empty string
        self.assertEqual(result.value, "example text")  # Check that text is correct

    # Test for TextNode with TextType.BOLD
    def test_bold_conversion(self):
        # Step 1: Create a TextNode with TextType.BOLD
        bold_text = "Bold Example"
        text_node = TextNode(text_type=TextType.BOLD, text=bold_text)
        # Step 2: Conversion
        leaf_node = text_node_to_html_node(text_node)
        # Step 3: Assertions
        assert leaf_node.tag == "b"
        assert leaf_node.value == bold_text

    # Test for TextNode with TextType.ITALIC
    def test_italic_conversion(self):
        # Step 1: Create a TextNode with TextType.ITALIC
        italic_text = "Italic Example"
        text_node = TextNode(text_type=TextType.ITALIC, text=italic_text)
        # Step 2: Convert the TextNode to a LeafNode
        leaf_node = text_node_to_html_node(text_node)
        # Step 3: Assertions
        assert leaf_node.tag == "i"
        assert leaf_node.value == italic_text

    # Test for TextNode with TextType.CODE
    def test_code_conversion(self):
        # Step 1: Create a TextNode with TextType.CODE
        code_text = "print('Hello, World!')"
        text_node = TextNode(text_type=TextType.CODE, text=code_text)
        # Step 2: Conversion
        leaf_node = text_node_to_html_node(text_node)
        # Step 3: Assertions
        assert leaf_node.tag == "code"
        assert leaf_node.value == code_text

    # Test for TextNode with TextType.LINK
    def test_link_conversion(self):
        # Step 1: Create a TextNode with TextType.LINK and proper 'url' argument
        link_text = "Boot.dev"
        url = "https://boot.dev"
        text_node = TextNode(text=link_text, text_type=TextType.LINK, url=url)
        # Step 2: Conversion
        leaf_node = text_node_to_html_node(text_node)
        # Step 3: Assertions
        assert leaf_node.tag == "a"
        assert leaf_node.value == link_text
        # Assert that URL is part of props under 'href'
        assert "href" in leaf_node.props
        assert leaf_node.props["href"] == url

    # Test for TextNode with TextType.IMAGE
    def test_image_conversion(self):
        # Step 1: Create a TextNode for TextType.IMAGE
        alt_text = "A majestic bear"
        image_url = "https://images.example.com/bear.jpg"
        text_node = TextNode(text=alt_text, text_type=TextType.IMAGE, url=image_url)
        # Step 2: Convert to LeafNode
        leaf_node = text_node_to_html_node(text_node)
        # Step 3: Assertions to validate the conversion
        assert leaf_node.tag == "img"
        assert leaf_node.value == ""
        # Props checks for 'src' and 'alt'
        assert leaf_node.props["src"] == image_url
        assert leaf_node.props["alt"] == alt_text

    # Test for handling invalid TextType
    def test_invalid_type(self):
        # Step 1: Set up a TextNode with an invalid text type
        class InvalidTextType:
            pass
        text_node = TextNode(text="Invalid", text_type=InvalidTextType())
        # Step 2: Test if the function raises an exception for the invalid type
        with self.assertRaises(Exception):  # Or a more specific exception type, if you have one
            leaf_node = text_node_to_html_node(text_node)

if __name__ == "__main__":
    unittest.main()

