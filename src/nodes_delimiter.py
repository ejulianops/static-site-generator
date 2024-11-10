from textnode import TextNode
from texttypes import TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            
            # Check if we have an even number of splits
            if len(parts) % 2 == 0:
                raise ValueError("Delimiter not properly matched in text segment.")
            
            for i, part in enumerate(parts):
                # Here's where we correctly alternate types based on even/odd index
                current_type = text_type if i % 2 else TextType.TEXT
                new_nodes.append(TextNode(part, current_type))
        else:
            new_nodes.append(node)

    return new_nodes
    