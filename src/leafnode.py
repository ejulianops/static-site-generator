from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag = tag, value = value, props = props)

    def to_html(self):
        if not self.value:
            raise ValueError('All leaf nodes must have a value')
    
        props_string = self.props_to_html()
    
        if not self.tag:
            return self.value

        return f'<{self.tag}{props_string}>{self.value}</{self.tag}>'