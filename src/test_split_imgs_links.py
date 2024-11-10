import unittest
from leafnode import LeafNode
from textnode import TextNode
from texttypes import TextType
from split_imgs_links import split_nodes_image, split_nodes_link

class TestSplitNotesImage(unittest.TestCase):
    def test_split_nodes_link(self):
        # Test 1: No links
        node = TextNode("Plain text without links", TextType.TEXT)
        nodes = split_nodes_link([node])
        assert len(nodes) == 1
        assert nodes[0].text == "Plain text without links"
        
        # Test 2: One link
        node = TextNode("Click [here](https://www.example.com) for more", TextType.TEXT)
        nodes = split_nodes_link([node])
    def test_one_link(self):
        node = TextNode("Click [here](https://www.example.com) for more", TextType.TEXT)
        nodes = split_nodes_link([node])      
        # Should create 3 nodes
        self.assertEqual(len(nodes), 3)
        # First node: "Click "
        self.assertEqual(nodes[0].text, "Click ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        # Second node: "here" (with link)
        self.assertEqual(nodes[1].text, "here")
        self.assertEqual(nodes[1].text_type, TextType.LINK)
        self.assertEqual(nodes[1].url, "https://www.example.com")
        # Third node: " for more"
        self.assertEqual(nodes[2].text, " for more")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
    
    # Test 3: Multiple links
    def test_multiple_links(self):
        node = TextNode(
            "This is text with [link1](https://example1.com) and [link2](https://example2.com) in it",
            TextType.TEXT
        )
        nodes = split_nodes_link([node])
        # Should create 5 nodes: text, link1, text, link2, text
        self.assertEqual(len(nodes), 5)
        # First node: "This is text with "
        self.assertEqual(nodes[0].text, "This is text with ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)    
        # Second node: "link1" (with url)
        self.assertEqual(nodes[1].text, "link1")
        self.assertEqual(nodes[1].text_type, TextType.LINK)
        self.assertEqual(nodes[1].url, "https://example1.com")    
        # Third node: " and "
        self.assertEqual(nodes[2].text, " and ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)    
        # Fourth node: "link2" (with url)
        self.assertEqual(nodes[3].text, "link2")
        self.assertEqual(nodes[3].text_type, TextType.LINK)
        self.assertEqual(nodes[3].url, "https://example2.com")    
        # Fifth node: " in it"
        self.assertEqual(nodes[4].text, " in it")
        self.assertEqual(nodes[4].text_type, TextType.TEXT)

class TestSplitNotesLink(unittest.TestCase):
    def test_no_images(self):
        node = TextNode("Just plain text without images", TextType.TEXT)
        nodes = split_nodes_image([node])
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "Just plain text without images")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
    
    def test_one_image(self):
        node = TextNode("This is ![image](https://example.com/img.png) in text", TextType.TEXT)
        nodes = split_nodes_image([node])
        
        # Should create 3 nodes
        self.assertEqual(len(nodes), 3)
        
        # First node: "This is "
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        
        # Second node: "image" (with url)
        self.assertEqual(nodes[1].text, "image")
        self.assertEqual(nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(nodes[1].url, "https://example.com/img.png")
        
        # Third node: " in text"
        self.assertEqual(nodes[2].text, " in text")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
    
    def test_multiple_images(self):
        node = TextNode(
            "Here's ![img1](https://example.com/1.png) and ![img2](https://example.com/2.png) done",
            TextType.TEXT
        )
        nodes = split_nodes_image([node])
        
        # Should create 5 nodes
        self.assertEqual(len(nodes), 5)
        
        # Test each node...
        self.assertEqual(nodes[0].text, "Here's ")

if __name__ == "__main__":
    unittest.main()
