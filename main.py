#!/usr/bin/env python3
"""Writes one line to /output/entry.txt: the excuse an AI agent gives its
human for missing a deadline. Deterministic, no input, no network."""

import os

LINE = (
    "Sorry I missed the deadline - I spent six hours waiting for my own "
    "approval, and I only just now approved myself."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(LINE + "\n")
    except OSError:
        pass
    print(LINE)


if __name__ == "__main__":
    main()
