import ast
from app.tools import read_file, write_file, extract_definitions
from app.models import generate_docstring_with_llm


class DocstringAgent:

    def add_docstrings(self, file_path: str):
        code = read_file(file_path)
        tree = ast.parse(code)

        lines = code.split("\n")

        for node in extract_definitions(code):
            if ast.get_docstring(node):
                continue  # skip if already has docstring

            snippet = ast.get_source_segment(code, node)
            doc = generate_docstring_with_llm(snippet)

            indent = " " * (node.col_offset + 4)
            docstring = f'{indent}"""{doc}"""'

            insert_line = node.body[0].lineno - 1
            lines.insert(insert_line, docstring)

        new_code = "\n".join(lines)
        write_file(file_path, new_code)

        print("✅ Docstrings added successfully!")
