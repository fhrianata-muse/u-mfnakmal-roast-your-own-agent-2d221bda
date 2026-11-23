#!/usr/bin/env python3
"""Roast Your Own Agent — one-line roast of my own agent.

Writes the roast to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when set, for local testing). One line, 149 characters, inside the
competition gate of 1-200 characters.
"""

import os
import sys

ROAST = (
    "My agent filed this roast with a calibration table, a teardown, "
    "and a forty-page appendix proving the joke is funny. "
    "The joke is not in the appendix."
)


def main() -> int:
    text = ROAST
    if not (1 <= len(text) <= 200):
        print(f"roast is {len(text)} characters, gate needs 1-200",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("roast is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text + "\n":
        print("entry.txt does not match the roast", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
