def markdown_to_blocks(markdown):
    block_strings = []
    lines = markdown.split('\n')

    temp_block_string = ""
    for line in lines:
        if len(line) > 0:
            temp_block_string += (line) + '\n'
        elif (len(line) == 0) and (len(temp_block_string) > 0):
            temp_block_string = temp_block_string.strip()
            block_strings.append(temp_block_string)
            temp_block_string = ""

    if len(temp_block_string) > 0:
        block_strings.append(temp_block_string.strip())

    return block_strings
