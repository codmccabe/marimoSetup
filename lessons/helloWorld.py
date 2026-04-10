import marimo

__generated_with = "0.23.0"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Hello, marimo

    This lesson is authored in VS Code as a normal Python file.
    Edit the cells here, then preview the notebook with:

    `uv run marimo edit lessons/helloWorld.py`
    """)
    return


@app.cell
def _():
    message = "Hello from a VS Code-authored marimo notebook."
    return (message,)


@app.cell
def _(message):
    print(message)
    return


if __name__ == "__main__":
    app.run()
