import ast
from app.tools import extract_definitions
from app.models import generate_docstring_with_llm


class DocstringAgent:

    def process_code(self, code: str) -> str:
        """
        Takes Python code and inserts generated docstrings.
        """

        lines = code.split("\n")

        for node in extract_definitions(code):

            # Skip if already has docstring
            if ast.get_docstring(node):
                continue

            snippet = ast.get_source_segment(code, node)
            doc = generate_docstring_with_llm(snippet)

            indent = " " * (node.col_offset + 4)
            docstring = f'{indent}"""{doc}"""'

            insert_line = node.body[0].lineno - 1
            lines.insert(insert_line, docstring)

        return "\n".join(lines)
