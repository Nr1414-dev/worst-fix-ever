#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit message, at most 100 characters, for the bug fix
that made everything worse, to /output/entry.txt.

The entry is a fixed, deterministic string: no input is read, no time or
randomness is involved, so every run produces byte-identical output.
"""

import os

ENTRY = "fix: Feb 29 bug by deleting Feb 29 — the calendar is correct now, and one day shorter"


def main() -> None:
    # Gate: the entry must be UTF-8 text of 1 to 100 characters, not only
    # whitespace. Fail loudly here rather than shipping an invalid entry.
    if not (1 <= len(ENTRY) <= 100) or not ENTRY.strip():
        raise ValueError("entry violates the 1-100 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    # Read back what was written and confirm it is byte-identical.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise ValueError("read-back mismatch on entry.txt")


if __name__ == "__main__":
    main()
