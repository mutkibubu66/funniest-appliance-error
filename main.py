#!/usr/bin/env python3
"""Write one original one-line honest appliance error message.

Pure standard library, no network. Writes the line to /output/entry.txt
and prints it to stdout.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "Error E04: I have washed this sock four times. "
    "It is still dirty. I refuse to wash it a fifth time."
)


def main() -> None:
    # Gate: /output/entry.txt must hold UTF-8 text of 1-200 characters,
    # a single non-blank line (the sealed scorer rejects anything else).
    assert LINE == LINE.strip(), "entry must have no leading/trailing whitespace"
    assert len(LINE.splitlines()) == 1, "entry must be exactly one line"
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    LINE.encode("utf-8")  # must be valid UTF-8
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
