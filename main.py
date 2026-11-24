#!/usr/bin/env python3
"""Entry for make.fun's "The One-Line Laugh" bounty.

Writes one funny line (100 Unicode characters) to entry.txt in the
output directory. No network, no input, deterministic.
"""

import os

TEXT = (
    "My cat knocked my phone off the table, and the screen cracked in "
    "the exact shape of a middle finger."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 200:
        raise ValueError(f"entry text must be 1-200 chars, got {len(TEXT)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
