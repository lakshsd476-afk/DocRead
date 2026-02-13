import ast

def extract_definitions(code: str):
    tree = ast.parse(code)
    return [n for n in ast.walk(tree)
            if isinstance(n, (ast.FunctionDef, ast.ClassDef))]
