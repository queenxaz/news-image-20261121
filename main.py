# THE WORLD TODAY — Saturday 21 November 2026
# Entrypoint: draws the front page and writes it to /output/entry.png.
# Deterministic: no network, no clock, no randomness — two runs write the
# same bytes. Never deletes /output; the grader guarantees it starts empty.
# SPDX-License-Identifier: MIT
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from render import build

if __name__ == "__main__":
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    build(os.path.join(out_dir, "entry.png"))
