import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_image,
    text_type_link,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


def split_nodes_delimiter(
    old_nodes: list[TextNode | str], delimiter: str, text_type: str
) -> list[TextNode]:
    new_list = []
    for text_node in old_nodes:
        if text_node.text_type != text_type_text:
            new_list.append(text_node)
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


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_list = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_list.append(old_node)
            continue
        copy_text = old_node.text
        image_tups = extract_markdown_images(copy_text)
        if len(image_tups) == 0:
            new_list.append(old_node)
            continue
        for image_tup in image_tups:
            texts = copy_text.split(f"![{image_tup[0]}]({image_tup[1]})", 1)
            if len(texts) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if len(texts[0]) != 0:
                new_list.append(TextNode(texts[0], text_type_text))
            new_list.append(
                TextNode(image_tup[0], text_type_image, image_tup[1])
            )
            copy_text = texts[1]
        if len(copy_text) != 0:
            new_list.append(TextNode(copy_text, text_type_text))
    return new_list


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_list = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_list.append(old_node)
            continue
        copy_text = old_node.text
        link_tups = extract_markdown_links(copy_text)
        if len(link_tups) == 0:
            new_list.append(old_node)
            continue
        for link_tup in link_tups:
            texts = copy_text.split(f"[{link_tup[0]}]({link_tup[1]})", 1)
            if len(texts) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if len(texts[0]) != 0:
                new_list.append(TextNode(texts[0], text_type_text))
            new_list.append(TextNode(link_tup[0], text_type_link, link_tup[1]))
            copy_text = texts[1]
        if len(copy_text) != 0:
            new_list.append(TextNode(copy_text, text_type_text))
    return new_list


def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def extract_markdown_images(text: str) -> tuple(list[str, str]):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text: str) -> tuple(list[str, str]):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
