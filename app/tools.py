import ast

def read_file(path):
    with open(path, "r") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w") as f:
        f.write(content)

def extract_definitions(code: str):
    tree = ast.parse(code)
    return [
        n for n in ast.walk(tree)
        if isinstance(n, (ast.FunctionDef, ast.ClassDef))
    ]
