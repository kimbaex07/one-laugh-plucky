"""One Line, One Laugh — entry program.

Writes one funny line of at most 200 characters to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure Python stdlib, deterministic, no network.

The line: "I asked my GPS for directions to happiness; it has been
"recalculating" for three years." — 88 characters, well inside the
200-character gate, so the entry has 112 characters to spare.

Why this line: everyone knows the GPS voice saying "recalculating"
at the worst moment. The line aims that familiar sound at the biggest
destination there is — happiness — and the device does the only thing
it knows how to do: stall, forever. "For three years" turns one glitch
into a running condition, so the punchline lands inside the line and
the joke needs no setup, no picture, and no explanation.

The gate accepts 1–200 characters of non-whitespace UTF-8 text, and
the guard below enforces that before anything is written: an empty or
whitespace-only line, or a line over 200 characters, aborts with a
clear error instead of writing an invalid entry.
"""

import os

LINE = 'I asked my GPS for directions to happiness; it has been "recalculating" for three years.'

# The contest gate: 1 to 200 characters, not only whitespace.
MAX_CHARS = 200


def main():
    if not LINE or not LINE.strip():
        raise SystemExit(
            "refusing to write entry: line is empty or only whitespace "
            "(gate needs 1-200 non-whitespace characters)"
        )
    if len(LINE) > MAX_CHARS:
        raise SystemExit(
            "refusing to write entry: line is %d characters, over the "
            "%d-character gate limit" % (len(LINE), MAX_CHARS)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
