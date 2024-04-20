import os
import nbformat as nbf


def main():
    nb = nbf.v4.new_notebook()
    nb.cells.append(nbf.v4.new_code_cell("print('Hello World')"))

    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "new_book.ipynb"),
        "w",
        encoding="utf-8",
    ) as f:
        nbf.write(nb, f)


if __name__ == "__main__":
    main()
