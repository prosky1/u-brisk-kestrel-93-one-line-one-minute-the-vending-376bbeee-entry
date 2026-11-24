#!/usr/bin/env python3
"""One-line vending-machine pickup line entry.

Writes the competition entry — a single pickup line spoken by a vending
machine to a passing human — to /output/entry.txt, the artifact the
house gate scorer checks (UTF-8 text, 1 to 200 characters).
"""

import os
import sys

LINE = "Press B7 for a date: I am fully stocked, slightly dented, and yours for exact change."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(line: str) -> None:
    """Guard the house gate before writing: 1-200 chars, one line, not blank."""
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry is {len(line)} characters, gate allows 1-200")


def main() -> int:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != LINE:
        raise ValueError("round-trip check failed: output differs from entry line")
    print(f"wrote {len(LINE)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
