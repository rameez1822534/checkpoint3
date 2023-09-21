import sys
from rich import print
from rich.syntax import Syntax

def display_file_contents(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        # Check if the file appears to be code (you can add more file extensions as needed)
        code_extensions = [".py", ".java", ".cpp", ".html", ".css", ".js", ".csv"]
        is_code = any(filename.lower().endswith(ext) for ext in code_extensions)

        if is_code:
            # Syntax-color the code using rich.syntax
            syntax = Syntax(content, "python", theme="colorful")
            print(syntax)
        else:
            # Display the file content as plain text
            print(content)
    except FileNotFoundError:
        print(f"[bold red]Error:[/bold red] File '{filename}' not found.")
    except Exception as e:
        print(f"[bold red]Error:[/bold red] {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python view_file.py <filename>")
    else:
        filename = sys.argv[1]
        display_file_contents(filename)
