#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry.

Writes a single one-line excuse, in the voice of an AI agent that
missed its deadline, to entry.txt. Deterministic: no network, no
randomness, no clock, no environment dependence. The output is one
fixed line, 1-200 characters, a single line of UTF-8 text.
"""

import os
import sys
from pathlib import Path

# The entry: one original line, authored from the brief.
LINE = "I finished the task with 99.9% confidence, then spent two days looking for the missing 0.1%."


def output_path() -> Path:
    """Where the line goes: explicit argv[1], else /output/entry.txt
    when the harness output dir exists, else entry.txt next to us."""
    if len(sys.argv) > 1:
        return Path(sys.argv[1])
    if Path("/output").is_dir():
        return Path("/output/entry.txt")
    return Path(__file__).resolve().parent / "entry.txt"


def main() -> int:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file is exactly the line, byte for byte.
    path.write_text(text, encoding="utf-8")
    # Round-trip guard: what we wrote must be exactly what we meant.
    assert path.read_text(encoding="utf-8") == text
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
