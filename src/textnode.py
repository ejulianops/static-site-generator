class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eg__(self, other):
        return self == other
    
    def __repr__(self):
        print(f'TextNode({self.text}, {self.text_type}, {self.url})')