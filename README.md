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

## 4) Launch marimo

```bash
cd ~/Github/marimoSetup
uv run marimo edit lessons/lesson_01.py
```

Open the localhost URL printed in the terminal.

## 5) Optional export for students

```bash
uv run marimo export html lessons/lesson_01.py --output exports/lesson_01.html
```

## Done when

- `uv --version` works
- marimo launches from `uv run marimo edit lessons/lesson_01.py`
