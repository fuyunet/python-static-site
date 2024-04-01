block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdwon: str) -> list[str]:
    block_str = markdwon.split("\n\n")
    filtered_blocks = []
    for str in block_str:
        if str == "":
            continue
        str = str.strip()
        filtered_blocks.append(str)
    return filtered_blocks


def block_to_block_type(block: str) -> str:
    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_type_heading
    if block.startswith("```") and block.endswith("```"):
        return block_type_code

    lines = block.split("\n")

    if all(line.startswith(">") for line in lines):
        return block_type_quote
    if all(line.startswith(("*", "-")) for line in lines):
        return block_type_unordered_list

    tmp_bool = True
    cur_num = 1
    for line in lines:
        if line.startswith(str(cur_num) + "."):
            cur_num += 1
            continue
        tmp_bool = False
        break
    if tmp_bool:
        return block_type_ordered_list
    return block_type_paragraph

    pass
