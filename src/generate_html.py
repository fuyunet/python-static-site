import os
from block_markdown import markdown_to_html_node, markdown_to_blocks


def generate_page(from_path: str, template_path: str, dest_path: str):
    print(
        f"Generating page from {from_path}"
        + f" to {dest_path} using {template_path}"
    )

    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()

    title = extract_title(markdown)
    content = markdown_to_html_node(markdown).to_html()

    html = template.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", content)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(html)


def extract_title(markdown: str):
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        if block.startswith("# "):
            return block.split("# ")[1]

    raise Exception("Needs a title")
