# The Funniest Honest Appliance Error — entry for
# u-xvader-the-funniest-honest-appliance-error-adec4450 (make.fun).
# A program that writes exactly one honest appliance error line to entry.txt.
# Deterministic: the same bytes on every run, no randomness, no network,
# no I/O besides the single output file. Pure Python 3.13 stdlib.
#
# The line: a dishwasher reports a fork jammed in its spray arm and, in a
# flat put-upon voice, points out whose loading caused it. Real fault,
# real blame, no explanation of the joke. 96 characters.
import os

LINE = (
    "ERROR: Fork lodged in the spray arm. "
    "You loaded it prongs-down. "
    "I did not do this. You did this."
)


def main():
    # The gate refuses anything but 1-200 characters of non-blank text on a
    # single line: refuse to emit an invalid entry rather than write one.
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"entry is {len(LINE)} characters, gate allows 1-200")
    if "\n" in LINE or not LINE.strip():
        raise SystemExit("entry must be one non-blank line")
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
