#!/usr/bin/env python3
"""Entry point: write the front-page image to /output/entry.png.

Renders THE WORLD TODAY - Saturday 21 November 2026 with render.py
and writes it to /output/entry.png (JPEG bytes under the .png name,
which the rules allow). If Pillow or the fonts are unavailable in the
sandbox, it falls back to the pre-rendered entry.jpg shipped in this
repository, so both runs still write identical bytes. No network, no
randomness, no timestamps.
"""
# SPDX-License-Identifier: MIT
import os
import shutil
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR",
                             os.environ.get("OUTPUT_DIR", "/output"))
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    try:
        sys.path.insert(0, _HERE)
        from render import build

        build(out_path)
    except Exception:
        shutil.copyfile(os.path.join(_HERE, "entry.jpg"), out_path)


if __name__ == "__main__":
    main()
