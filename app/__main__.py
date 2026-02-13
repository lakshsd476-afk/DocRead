import sys
from app.agents import DocstringAgent

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m app <python_file>")
        return

    file_path = sys.argv[1]

    agent = DocstringAgent()
    agent.add_docstrings(file_path)

if __name__ == "__main__":
    main()
