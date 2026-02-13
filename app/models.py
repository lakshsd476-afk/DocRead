import ast

def generate_docstring_with_llm(code_snippet: str) -> str:
    try:
        node = ast.parse(code_snippet).body[0]
    except:
        return "Auto-generated docstring."

    if isinstance(node, ast.FunctionDef):
        params = [a.arg for a in node.args.args]
        return f"Function `{node.name}`.\nArgs: {', '.join(params)}\nReturns: result."

    if isinstance(node, ast.ClassDef):
        return f"Class `{node.name}`."

    return "Auto-generated docstring."
