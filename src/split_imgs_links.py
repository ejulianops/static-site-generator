from textnode import TextNode
from texttypes import TextType
from nodes_delimiter import split_nodes_delimiter
from extract_links import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []

    # Iterate over nodes
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue

        text = node.text
        for alt_text, url in images:
            image_markdown = f"![{alt_text}]({url})"
            parts = text.split(image_markdown, 1)
            
            # Add the text before the image if it exists
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            
            # Add the image node
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            
            # Update text for the next iteration (remaining part after the image)
            text = parts[1] if len(parts) > 1 else ""
        
        # If there's remaining text after the last image, add it as a new node
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    
    # Iterate over nodes
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue
        text = node.text
        for alt_text, url in links:
            link_markdown = f"[{alt_text}]({url})"
            # Split only on the first occurrence
            parts = text.split(link_markdown, 1)
            
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            
            new_nodes.append(TextNode(alt_text, TextType.LINK, url))
            
            # Update text for the next iteration (remaining part after the link)
            text = parts[1] if len(parts) > 1 else ""
        
        # If there's remaining text after the last link, add it as a new node
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes
    