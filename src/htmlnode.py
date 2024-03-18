class HTMLNode:
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: "HTMLNode" = None,
        props: dict = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise (NotImplementedError)

    def props_to_html(self):
        if self.props is None:
            return ""
        result_str = ""
        for key, value in self.props.items():
            result_str += f' {key}="{value}"'
        return result_str

    def __repr__(self) -> str:
        return (
            "HTMLNode: ("
            f"tag: {self.tag}, "
            f"value: {self.value}, "
            f"children: {self.children}, "
            f"props: {self.props})"
        )


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
