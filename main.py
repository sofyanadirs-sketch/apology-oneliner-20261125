#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — make.fun bounty entry.

Writes the one-line apology to /output/entry.txt (1-159 chars, UTF-8).
The line is the entry: an AI agent's message to its human right after
it has accidentally done something it should not have.
"""

import os

LINE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def load_line() -> str:
    """Read the one-liner from entry.txt, the entry's single source of truth."""
    with open(LINE_FILE, encoding="utf-8") as f:
        text = f.read().strip()
    assert 1 <= len(text) <= 159, f"line is {len(text)} chars, must be 1-159"
    return text


def main() -> None:
    text = load_line()
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Outputs are collected as another user: leave the file world-readable.
    os.chmod(path, 0o644)
    print(text)


if __name__ == "__main__":
    main()
