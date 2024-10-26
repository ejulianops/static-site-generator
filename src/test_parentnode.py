import unittest

from parentnode import ParentNode

class TestParentNode(unittest.TestCase):

    # no Children
    def test_no_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(tag="div", children=[]).to_html()
        self.assertEqual(str(context.exception), "Children value is needed")

    # No Tag
    def test_no_tag(self):
        from leafnode import LeafNode
        children = [LeafNode("b", "Bold text")]
        with self.assertRaises(ValueError) as context:
            ParentNode(tag=None, children=children).to_html()
        self.assertEqual(str(context.exception), "Tag value is needed")

    # ParentNode with Single LeafNode
    def test_single_leafnode(self):
        from leafnode import LeafNode
        children = [LeafNode("b", "Bold text")]
        node = ParentNode(tag="div", children=children)
        self.assertEqual(node.to_html(), "<div><b>Bold text</b></div>")

    # Multiple LeafNode Children
    def test_multiple_leafnode_children(self):
        from leafnode import LeafNode
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "Italic text"),
        ]
        node = ParentNode(tag="div", children=children)
        self.assertEqual(
            node.to_html(), "<div><b>Bold text</b>Normal text<i>Italic text</i></div>"
        )

    # Nesting ParentNode
    def test_nesting_parentnode(self):
        from leafnode import LeafNode
        inner_children = [LeafNode(None, "Inner text")]
        inner_node = ParentNode(tag="span", children=inner_children)
        outer_children = [inner_node, LeafNode(None, "Outer text")]
        outer_node = ParentNode(tag="div", children=outer_children)
        self.assertEqual(
            outer_node.to_html(), "<div><span>Inner text</span>Outer text</div>"
        )

    # Mixed Validity
    def test_mixed_validity(self):
        from leafnode import LeafNode
        child_node = LeafNode("b", "Bold")
        container_node = ParentNode(tag="div", children=[child_node])
        mixed_node = ParentNode(tag="section", children=[container_node, LeafNode(None, "Text")])
        self.assertEqual(
            mixed_node.to_html(), "<section><div><b>Bold</b></div>Text</section>"
        )



if __name__ == "__main__":
    unittest.main()
