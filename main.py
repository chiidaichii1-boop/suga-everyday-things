"""Everyday Things, Two Lines, Longer Run — make.fun entry.

Writes a two-line explanation of a toaster to /output/entry.txt.
Line 1: one vivid sentence with a concrete, surprising analogy.
Line 2: one sentence on what the analogy maps and what it leaves out.
"""

import os

ENTRY = (
    "A toaster is a little elevator that carries bread down into a glowing "
    "orange cave, where it gets a golden suntan it can never wash off.\n"
    "The elevator maps how bread sinks down and pops back up, but the "
    "glow is hot wires, not the cave itself."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
