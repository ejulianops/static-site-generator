import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode
from texttypes import TextType

class TestTextToTextNodes(unittest.TestCase):

    def test_simple_text(self):
        text = "This is plain text."
        nodes = text_to_textnodes(text)
        expected_nodes = [TextNode("This is plain text.", TextType.TEXT)]
        self.assertEqual(nodes, expected_nodes)

    def test_bold_text(self):
        text = "This is **bold** text."
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_italic_text(self):
        text = "This is *italic* text."
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_code_text(self):
        text = "This is `code` text."
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_image(self):
        text = "This is an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_link(self):
        text = "This is a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_combined_text(self):
        text = "This is **bold** text with an *italic* word, a `code block`, an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg), and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word, a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(", an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(", and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(nodes, expected_nodes)

if __name__ == "__main__":
    unittest.main()
