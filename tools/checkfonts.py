#!/usr/bin/env python3
"""Report every font size used in the built thesis PDF.

Cardiff's Policy on the Submission and Presentation of Research Degree
Theses sets two floors:

  6.1  body text no less than 12 point
  6.3  all other text -- footnotes, figure captions -- no less than 11 point
  6.5  characters inside tables and figures legible and large enough
       for general accessibility

This reads the font-size operators out of the PDF's content streams, so
it reports what a reader actually gets rather than what the source asked
for. Run it before you submit.

One caveat on the numbers. A TeX point is 1/72.27 inch and a PDF point is
1/72 inch, so LaTeX's 12pt is written into the PDF as 11.96 and its 11pt
as 10.96. That is normal and universally accepted; this script accounts
for it rather than flagging it.

Mathematical superscripts and subscripts are reported separately: they
are inherently smaller than body text, and no floor sensibly applies to
them.

Usage:  python3 tools/checkfonts.py [path/to/pdf]
"""

import collections
import re
import sys
import zlib

TEX_TO_PDF = 72.0 / 72.27          # 12 TeX pt -> 11.958 PDF pt
BODY_FLOOR = 12 * TEX_TO_PDF - 0.05
OTHER_FLOOR = 11 * TEX_TO_PDF - 0.05


def font_sizes(path):
    data = open(path, "rb").read()
    sizes = collections.Counter()
    for m in re.finditer(rb"stream\r?\n", data):
        start = m.end()
        end = data.find(b"endstream", start)
        if end < 0:
            continue
        try:
            s = zlib.decompress(data[start:end])
        except zlib.error:
            continue
        for tf in re.finditer(rb"/F\d+\s+([\d.]+)\s+Tf", s):
            sizes[round(float(tf.group(1)), 2)] += 1
    return sizes


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "build/main.pdf"
    try:
        sizes = font_sizes(path)
    except FileNotFoundError:
        print(f"{path} not found. Build the thesis first: latexmk main.tex")
        return 1

    if not sizes:
        print(f"No font-size operators found in {path}.")
        return 1

    print(f"\nFont sizes in {path}\n")
    print(f"  {'size':>8}  {'runs':>6}   note")
    print(f"  {'-'*8}  {'-'*6}   {'-'*44}")

    below = []
    for sz in sorted(sizes):
        n = sizes[sz]
        if sz >= BODY_FLOOR:
            note = "body text or larger (6.1)"
        elif sz >= OTHER_FLOOR:
            note = "footnotes, captions, table notes (6.3)"
        else:
            note = "maths script level -- see below"
            below.append((sz, n))
        print(f"  {sz:8.2f}  {n:6d}   {note}")

    print()
    if below:
        total = sum(n for _, n in below)
        print(f"  {total} run(s) below the 11pt floor, at "
              f"{', '.join(f'{s:.2f}pt' for s, _ in below)}.")
        print("  Check these are only mathematical superscripts and")
        print("  subscripts. If any is body text, a footnote or a caption,")
        print("  it breaches 6.3 -- find the \\scriptsize or \\tiny that")
        print("  produced it. If it is a shrunken table, the compliant fix")
        print("  is a landscape page or fewer columns, not smaller type.")
    else:
        print("  Nothing below the 11pt floor.")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
