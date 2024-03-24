from textnode import (
    TextNode,
    text_type_text,
)


def split_nodes_delimiter(
    old_nodes: list[TextNode | str], delimiter: str, text_type: str
) -> list[TextNode]:
    new_list = []
    for text_node in old_nodes:
        if text_node.text_type != text_type_text:
            new_list.extend(text_node)
            continue

        count = text_node.text.count(delimiter)
        if count % 2 != 0:
            raise ValueError("Invalid markdown, formatted section not closed")

        list_split = text_node.text.split(delimiter)
        new_split = []
        for i, value in enumerate(list_split):
            if value == "":
                continue
            if i % 2 == 0:
                new_split.append(TextNode(value, text_node.text_type))
            else:
                new_split.append(TextNode(value, text_type))
        new_list.extend(new_split)
    return new_list
