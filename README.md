# marimoSetup: Minimal Linux Mint Setup

Goal: set up `uv` + `marimo` in this folder and launch a working marimo app.

## 1) Prerequisites

Run in your terminal:

```bash
sudo apt update
sudo apt install -y curl git build-essential
```

## 2) Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
uv --version
```

If `uv` is still not found, close and reopen your terminal, then run `uv --version` again.

## 3) Set up marimo in this repo

`uv` handles the virtual environment silently — you never run `python -m venv` or `source venv/bin/activate`. When you run `uv init` + `uv add marimo`, uv creates a `.venv` inside the project and installs dependencies into it. `uv run` then uses that environment automatically, every time, no activation needed.

```bash
cd ~/Github/marimoSetup
uv init
uv add marimo
mkdir -p lessons exports assets
touch lessons/lesson_01.py
```

## 4) Build content in VS Code

With the marimo VS Code extension installed, you can open and run marimo notebooks directly inside VS Code.

Recommended workflow:

```bash
cd ~/Github/marimoSetup
code .
```

1. Open [lessons/helloWorld.py](lessons/helloWorld.py) or another marimo `.py` file.
2. If it does not open as a notebook automatically, run `marimo: Open as marimo notebook` from the Command Palette.
3. For a new notebook, run `marimo: New marimo notebook`.
4. Edit and run cells inside VS Code.

`uv` still manages the environment in the background. The extension uses your project setup; you do not need to activate a venv manually.

## 5) Browser fallback

If you want or need the standalone marimo app, run:

```bash
cd ~/Github/marimoSetup
uv run marimo edit lessons/lesson_01.py
```

That starts marimo and opens the notebook through a local URL.

## 6) Optional export for students

```bash
uv run marimo export html lessons/lesson_01.py --output exports/lesson_01.html
```

## Done when

- `uv --version` works
- marimo opens inside VS Code with the extension, or from `uv run marimo edit lessons/lesson_01.py`
