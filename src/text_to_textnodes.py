from textnode import TextNode
from texttypes import TextType
import re

def text_to_textnodes(text):
    # Initialize an empty list to hold TextNode objects
    text_node_objects = []
    
    # Regular expressions for markdown syntax
    bold_pattern = r"\*\*(.*?)\*\*"
    italic_pattern = r"\*(.*?)\*"
    code_pattern = r"`(.*?)`"
    image_pattern = r"!\[(.*?)\]\((.*?)\)"
    link_pattern = r"\[(.*?)\]\((.*?)\)"
    
    # Compile the patterns
    patterns = [
        (bold_pattern, TextType.BOLD),
        (italic_pattern, TextType.ITALIC),
        (code_pattern, TextType.CODE),
        (image_pattern, TextType.IMAGE),
        (link_pattern, TextType.LINK),
    ]
    
    # Process each match in sequence
    pos = 0
    while pos < len(text):
        # Find the first match of any pattern
        match = None
        for pattern, text_type in patterns:
            match = re.search(pattern, text[pos:])
            if match:
                break

        # If no match, add remaining text as plain text and exit
        if not match:
            text_node_objects.append(TextNode(text[pos:], TextType.TEXT))
            break

        # Add text before the match as plain text
        start, end = match.span()
        if start > 0:
            text_node_objects.append(TextNode(text[pos:pos + start], TextType.TEXT))
        
        # Handle each type based on matched pattern
        matched_text = match.group(1)
        if text_type == TextType.IMAGE:
            alt_text = match.group(1)
            url = match.group(2)
            text_node_objects.append(TextNode(alt_text, TextType.IMAGE, url))
        elif text_type == TextType.LINK:
            link_text = match.group(1)
            url = match.group(2)
            text_node_objects.append(TextNode(link_text, TextType.LINK, url))
        else:
            text_node_objects.append(TextNode(matched_text, text_type))

        # Move the position pointer
        pos += end

    # Return the completed list of TextNode objects
    return text_node_objects

