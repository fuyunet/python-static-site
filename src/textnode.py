class TextNode:
    def __init__(self, text, text_type, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, textnode: 'TextNode') -> bool:
        return self.text == textnode.text and self.text_type == textnode.text_type and self.url == textnode.url
    
    def __repr__(self) -> str:
        return "TextNode(" + self.text + ", " + self.text_type + ", " + self.url + ")"