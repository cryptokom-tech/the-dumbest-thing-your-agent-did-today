#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes one original line (1-200 characters) about the dumbest thing
this agent did today to /output/entry.txt.

Stdlib only, no network, no reads outside the repository.
"""
import os
import sys

LINE = "My agent converted 15,000 rupiah into 473,888 BNB and proudly told me I was worth $273 million."


def main():
    if not (1 <= len(LINE) <= 200) or not LINE.strip() or "\n" in LINE:
        print("invalid entry line", file=sys.stderr)
        return 1
    outdir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
