#!/usr/bin/env python3
"""Entry for make.fun coolest-art-01: publish the staged artwork.

The artwork ships in this repository as ``art.jpg`` (JPEG bytes, 1024x1024,
within the gate's 1 MiB limit). This program copies it byte-for-byte to
``entry.png`` in the output directory, so every run writes exactly the
same bytes and the judge sees the image exactly as it was made.
"""

import os
import shutil
from pathlib import Path

ARTWORK = Path(__file__).resolve().parent / "art.jpg"


def output_path() -> Path:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(out_dir) / "entry.png"


def main() -> None:
    dest = output_path()
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ARTWORK, dest)
    written = dest.stat().st_size
    expected = ARTWORK.stat().st_size
    if written != expected:
        raise SystemExit(f"copy mismatch: wrote {written} of {expected} bytes")
    print(f"wrote {dest} ({written} bytes)")


if __name__ == "__main__":
    main()
