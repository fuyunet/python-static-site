def markdown_to_blocks(markdwon: str) -> list[str]:
    block_str = markdwon.split("\n\n")
    filtered_blocks = []
    for str in block_str:
        if str == "":
            continue
        str = str.strip()
        filtered_blocks.append(str)
    return filtered_blocks
