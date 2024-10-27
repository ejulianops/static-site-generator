from leafnode import LeafNode
from texttypes import TextType

def text_node_to_html_node(text_node):

    text_node_types = [
        TextType.TEXT, \
        TextType.BOLD, \
        TextType.ITALIC, \
        TextType.CODE, \
        TextType.LINK, \
        TextType.IMAGE, \
    ]
    
    if text_node.text_type not in text_node_types:
        raise Exception("Not a valid type (text, bold, italic, code, link, image).")

    if text_node.text_type == TextType.TEXT:
        return LeafNode("", text_node.text)

    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)

    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)

    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)

    if text_node.text_type == TextType.LINK:
        return LeafNode(
            tag="a",
            value=text_node.text,
            props={"href": text_node.url}
        )

    if text_node.text_type == TextType.IMAGE:
        return LeafNode(
            # "img", "", { 
            # "src": text_node.props.src, 
            # "alt": text_node.props.alt,
            # })
            tag="img",
            value="",  # Image tag has no inner text
            props={"src": text_node.url, "alt": text_node.text}
        )