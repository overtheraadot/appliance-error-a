#!/usr/bin/env python3
"""The Funniest Honest Appliance Error entry (account A).

Writes one line to /output/entry.txt: the funniest honest error message
an appliance could show. Deterministic, stdlib only, no network, no secrets.

The joke: a washing machine reports its drain filter blocked by the
odds and ends it actually finds in pockets — two coins, a button, a
USB stick — then, in its own flat put-upon voice, refuses the role of
lost-property office and orders the owner to clean it out. The
humour comes from the truth of the fault:
a clogged filter really is what stops the machine, and the inventory
of pocket debris is exactly what a technician pulls out of one.
"""

import os

# The error: a clogged drain filter, reported by the machine itself
# in a flat tone, with the pocket debris itemised as evidence.
ERROR = (
    "Error 12: drain filter blocked by two coins, a button and a USB "
    "stick. I am a washing machine, not a lost-property office. "
    "Clean me out."
)

MAX_CHARS = 200
OUT_PATH = "/output/entry.txt"


def verify(text: str) -> str:
    """Return the error, stripped, after enforcing the gate."""
    line = text.strip()
    if not line:
        raise ValueError("error is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"error is {len(line)} chars, must be at most {MAX_CHARS}")
    if "\n" in line:
        raise ValueError("error must be a single line")
    return line


def write_entry(text: str, path: str = OUT_PATH) -> str:
    """Verify the error and write it to the output file."""
    line = verify(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod(path, 0o644)
    return line


def main() -> None:
    line = write_entry(ERROR)
    print(f"Wrote {len(line)} chars to {OUT_PATH}")


if __name__ == "__main__":
    main()
