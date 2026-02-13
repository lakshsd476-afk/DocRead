import ast

def read_file(path: str) -> str:
    with open(path, "r") as f:
        return f.read()


def write_file(path: str, content: str):
    with open(path, "w") as f:
        f.write(content)


def extract_definitions(code: str):
    tree = ast.parse(code)
    return [node for node in ast.walk(tree)
            if isinstance(node, (ast.FunctionDef, ast.ClassDef))]
