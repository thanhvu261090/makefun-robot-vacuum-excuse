#!/usr/bin/env python3
"""make.fun entry: The Robot Vacuum's Best Excuse.

Holds the entry line as a constant, checks it against the kit's gate
(UTF-8 text, 1-140 characters, not only whitespace, a single line),
and writes it to /output/entry.txt.
"""

import os
import sys

ENTRY = (
    "I didn't miss that spot \u2014 my lidar classified it as emotional "
    "support dust, and my bumper signed a peace treaty with it."
)

MAX_CHARS = 140


def gate_check(text: str) -> None:
    """Enforce the exact entry gate from the kit's RULES.txt."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    text.encode("utf-8")


def main() -> int:
    gate_check(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
