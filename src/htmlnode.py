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


class ParentNode(HTMLNode):
    def __init__(
        self, tag: str, children: "HTMLNode", props: dict = None
    ) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return (
            f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        )

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
