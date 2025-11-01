import re

def rmcomments(json_string_with_comments):
    # Remove single-line comments (// ...)
    json_string_with_comments = re.sub(r'//.*?(\n|$)', '\n', json_string_with_comments)
    # Remove multi-line comments (/* ... */)
    json_string_with_comments = re.sub(r'/\*.*?\*/', '', json_string_with_comments, flags=re.DOTALL)
    return json_string_with_comments
