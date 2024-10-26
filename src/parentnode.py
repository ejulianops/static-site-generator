from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag = tag, children = children, props = props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag value is needed")
        elif not self.children:
            raise ValueError("Children value is needed")
        else:
            output = ""
            for child in self.children:
                output += f"{child.to_html()}"
            return f"<{self.tag}>{output}</{self.tag}>"

