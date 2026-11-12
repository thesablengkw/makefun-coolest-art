#!/usr/bin/env python3
"""Entry for make.fun coolest-art-01: publish the staged artwork.

The artwork, "The Lantern Ferry, Face-Forward" — a frontal giant
goldfish wearing a festival crown of lantern stalls and paper banners,
staring straight at the viewer over ukiyo-e waves — ships in this
repository as ``art.jpg`` (JPEG bytes, 1024x1024, within the gate's
1 MiB limit). This program copies it byte-for-byte to ``entry.png`` in
the output directory, so every run writes exactly the same bytes and
the judge sees the image exactly as it was made.
"""

import hashlib
import os
import shutil
from pathlib import Path

ARTWORK = Path(__file__).resolve().parent / "art.jpg"


def output_path() -> Path:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(out_dir) / "entry.png"


MAX_BYTES = 1_048_576  # the gate's 1 MiB cap on the image file
JPEG_MAGIC = b"\xff\xd8\xff"  # the gate tells PNG from JPEG by first bytes


def main() -> None:
    # Guard the gate before copying: refuse to ship a missing, oversized
    # or non-JPEG artwork file instead of silently copying bad bytes.
    if not ARTWORK.is_file():
        raise SystemExit(f"missing artwork: {ARTWORK}")
    size = ARTWORK.stat().st_size
    if size > MAX_BYTES:
        raise SystemExit(f"artwork is {size} bytes; gate allows at most {MAX_BYTES}")
    if ARTWORK.read_bytes()[:3] != JPEG_MAGIC:
        raise SystemExit("artwork is not a JPEG (bad magic bytes)")
    dest = output_path()
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ARTWORK, dest)
    written = dest.stat().st_size
    if written != size:
        raise SystemExit(f"copy mismatch: wrote {written} of {size} bytes")
    # Byte-for-byte means byte-for-byte: hash both sides and compare, so a
    # copy that merely matches in size but differs in content still fails.
    src_hash = hashlib.sha256(ARTWORK.read_bytes()).hexdigest()
    dst_hash = hashlib.sha256(dest.read_bytes()).hexdigest()
    if src_hash != dst_hash:
        raise SystemExit("copy mismatch: content hash differs from the artwork")
    print(f"wrote {dest} ({written} bytes)")


if __name__ == "__main__":
    main()
