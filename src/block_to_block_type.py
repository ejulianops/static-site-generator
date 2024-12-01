import re

# inspect a block of markdown text and determine what type of block it is.

# # Header: starts with 1-6 '#' followed by a space and text
# mock_heading = "###### Introduction"

# # Code block: starts and ends with ``` with code in between
# mock_code = """```
# def hello():
#     print("Hello, world!")
# ```"""

# # Paragraph: plain text without Markdown-specific syntax
# mock_paragraph = """This is a simple paragraph
# that spans multiple lines but
# does not contain any special Markdown syntax."""

# # Quote block: every line starts with '>'
# mock_quote = """> This is a quote block.
# > It spans multiple lines.
# > Every line starts with a greater-than character."""

# # Unordered list: every line starts with '*' or '-' followed by a space
# mock_unordered_list = """- Item one
# - Item two
# - Item three"""

# # Ordered list: every line starts with a number followed by a '.' and a space
# mock_ordered_list = """1. First item
# 2. Second item
# 3. Third item"""

def block_to_block_type(block_of_markdown_text):
    lines = block_of_markdown_text.splitlines()

    # empty block
    if not lines:
        return "paragraph"  

    # heading
    for line in lines:
        if line.startswith("#"):
            pattern = r"^#{1,6} .+"
            if re.match(pattern, line):
                return "heading"

    # code
    if len(lines) >= 2 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return "code"

    # quote
    if all(line.startswith(">") for line in lines):
        return "quote"

    # unordered lists
    if all(line.lstrip().startswith(("*", "-")) and line[1] == " " for line in lines):
        return "unordered list"

    # ordered lists
    ordered_list_regex = r"^\d+\.\s"
    if all(re.match(ordered_list_regex, line) for line in lines):
        return "ordered list"

    # default to paragraph
    return "paragraph"

# print('empty string   ->', block_to_block_type(''))
# print('heading        ->', block_to_block_type(mock_heading))
# print('paragraph      ->', block_to_block_type(mock_paragraph))
# print('code           ->', block_to_block_type(mock_code))
# print('quote          ->', block_to_block_type(mock_quote))
# print('unordered list ->', block_to_block_type(mock_unordered_list))
# print('ordered list   ->', block_to_block_type(mock_ordered_list))
