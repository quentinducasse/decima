# tree_filtered.py
import os

ROOT = "."
EXTENSIONS = {".py", ".json", ".html", ".ascii", ".env", ".cpp", ".hpp"}
EXCLUDE_DIRS = {".vscode", "decima_env", "__pycache__"}

def walk_filtered(root):
    for current_path, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        rel_path = os.path.relpath(current_path, root)
        indent = "  " * (rel_path.count(os.sep) if rel_path != "." else 0)
        print(f"{indent}{os.path.basename(current_path)}")
        for file in sorted(files):
            ext = os.path.splitext(file)[1]
            if ext in EXTENSIONS:
                print(f"{indent}  └── {file}")

if __name__ == "__main__":
    print(f"Arborescence filtrée de '{os.path.abspath(ROOT)}':\n")
    walk_filtered(ROOT)
