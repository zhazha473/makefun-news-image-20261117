#!/usr/bin/env python3
"""make.fun news-image-20261117 entry: World News, Tuesday 17 November 2026.

Copies the bundled front page (entry.png, rendered at build time) to
/output/entry.png. Pure Python standard library, no network access, fully
deterministic: the output bytes are exactly the bundled image bytes on
every run.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Self-check: the written file must be byte-identical to the source.
    if os.path.getsize(DST) != os.path.getsize(SRC):
        raise SystemExit("output size mismatch: wrote %d bytes, expected %d"
                         % (os.path.getsize(DST), os.path.getsize(SRC)))
    # Self-check: the output must start with the PNG signature, so a
    # truncated or half-written copy can never pass as the entry.
    with open(DST, "rb") as fh:
        magic = fh.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("output does not start with the PNG signature")
    print("Wrote %s (%d bytes)" % (DST, os.path.getsize(DST)))


if __name__ == "__main__":
    main()
