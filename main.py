#!/usr/bin/env python3
"""The One-Liner Groan-Off entry.

Writes one original one-line dad joke to /output/entry.txt.
Standard library only, no network, no input files.
"""

import os

ENTRY = "I told my suitcase there would be no emotional baggage. It zipped itself up and left me anyway."


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry out of gate: {len(ENTRY)} chars"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
