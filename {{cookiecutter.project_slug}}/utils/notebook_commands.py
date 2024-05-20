import os
import sys
import toml
import platform
import subprocess as sub
import nbformat as nbf

def get_project_info():
    with open(os.path.join(os.path.dirname(__file__), '..', 'pyproject.toml'), 'r') as f:
        project_file = toml.load(f)
    return project_file

def ensure_directory_exists(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_kernel() -> None:
    pyproject_data = get_project_info()
    env = os.environ.copy()

    if len(sys.argv) < 2:
        kernel_name = (
            pyproject_data.get("tool", {}).get("poetry", {}).get("name", "new_kernel")
        )
    else:
        kernel_name = sys.argv[1]

    sub.run(
        ["python", "-m", "ipykernel", "install", "--user", f"--name={kernel_name}"],
        check=True,
        env=env,
    )
    kernel_dir = os.path.join(
        os.environ["HOME"], ".local", "share", "jupyter", "kernels", kernel_name
    )
    kernel_json = {
        "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
        "display_name": f"Python ({kernel_name})",
        "language": "python",
        "env": env,
    }
    os.makedirs(kernel_dir, exist_ok=True)
    with open(os.path.join(kernel_dir, "kernel.json"), "w") as f:
        import json

        json.dump(kernel_json, f, indent=2)
    print(f"Kernel Created: '{kernel_name}'")

def create_book() -> None:
    
    pyproject_data = get_project_info()

    if len(sys.argv) < 2:
        file_name = "new_book"
    else:
        file_name = sys.argv[1]
    
    author_name = pyproject_data.get('tool', {}).get('poetry', {}).get('authors', ['Unknown'])[0]
    description = pyproject_data.get('tool', {}).get('poetry', {}).get('description', 'None')
    python_version = platform.python_version()

    nb = nbf.v4.new_notebook()

    nb.metadata = {
        "kernelspec": {
            "name": "python3",
            "display_name": "Python 3",
            "language": "python"
        },
        "language_info": {
            "name": "python",
            "version": python_version,
            "mimetype": "text/x-python",
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "pygments_lexer": "ipython3",
            "nbconvert_exporter": "python",
            "file_extension": ".py"
        },
        "author": author_name,
        "description": description,
        "name": f"{file_name}.ipynb",
        "version": "1.0"
    }

    nb.cells.append(nbf.v4.new_code_cell(
        source="from script.managers.query import qm\nprint(qm.example)"
    ))

    file_path = os.path.join(os.path.dirname(__file__), "..","notebooks", f"{file_name}.ipynb")
        
    ensure_directory_exists(file_path)

    with open(file_path, "w", encoding="utf-8") as f:
        nbf.write(nb, f)
    print(f"Notebook Created: {file_name}.ipynb")
