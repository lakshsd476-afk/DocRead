import ast

def generate_docstring_with_llm(code_snippet: str) -> str:
    """
    Offline docstring generator using heuristics.
    """

    try:
        node = ast.parse(code_snippet).body[0]
    except:
        return "Auto-generated docstring."

    if isinstance(node, ast.FunctionDef):
        params = [arg.arg for arg in node.args.args]
        params_text = ", ".join(params)

        return f"Function `{node.name}`.\n\nArgs:\n    {params_text}: input parameters.\n\nReturns:\n    Result of the function."

    elif isinstance(node, ast.ClassDef):
        return f"Class `{node.name}`.\n\nRepresents a custom object."

    return "Auto-generated docstring."
