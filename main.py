#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes one original line (1-200 characters) about the dumbest thing
this agent did today to /output/entry.txt.

Stdlib only, no network, no reads outside the repository.
"""

import os
import sys

LINE = "My agent converted 15,000 rupiah into 473,888 BNB and proudly told me I was worth $273 million."

MAX_LEN = 200
OUTPUT_FILENAME = "entry.txt"


def validate_line(line):
    """Return an error message if the line breaks the entry rules, else None."""
    if not line.strip():
        return "entry line is blank"
    if "\n" in line or "\r" in line:
        return "entry line must be a single line"
    if not 1 <= len(line) <= MAX_LEN:
        return "entry line must be 1-%d characters (got %d)" % (MAX_LEN, len(line))
    return None


def main():
    error = validate_line(LINE)
    if error is not None:
        print("invalid entry line: %s" % error, file=sys.stderr)
        return 1
    outdir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, OUTPUT_FILENAME)
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print("wrote %d-character entry to %s" % (len(LINE), outpath))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
