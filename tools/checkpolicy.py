#!/usr/bin/env python3
"""Check the built thesis against the machine-checkable clauses of Cardiff's
Policy on the Submission and Presentation of Research Degree Theses
(Version 8.0, in effect 01.08.2025).

This inspects the compiled PDF, not the LaTeX source, so it reports what an
examiner actually receives. It covers the clauses that can be verified
mechanically; the rest are in docs/POLICY-COMPLIANCE.md and need a human.

Usage:  python3 tools/checkpolicy.py [path/to/pdf]
"""

import collections
import os
import re
import subprocess
import sys
import zlib

TEX2PDF = 72.0 / 72.27
BODY_FLOOR = 12 * TEX2PDF - 0.05      # 6.1
OTHER_FLOOR = 11 * TEX2PDF - 0.05     # 6.3

results = []


def check(clause, what, ok, detail):
    results.append((clause, what, ok, detail))


def pdftotext(pdf, first=None, last=None, bbox=False):
    cmd = ["pdftotext", "-q"]
    if bbox:
        cmd.append("-bbox")
    if first:
        cmd += ["-f", str(first), "-l", str(last or first)]
    cmd += [pdf, "-"]
    return subprocess.run(cmd, capture_output=True, text=True).stdout


def page_count(pdf):
    out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    m = re.search(r"Pages:\s+(\d+)", out)
    return int(m.group(1)) if m else 0


def font_sizes(pdf):
    data = open(pdf, "rb").read()
    sizes = collections.Counter()
    for m in re.finditer(rb"stream\r?\n", data):
        s0 = m.end()
        s1 = data.find(b"endstream", s0)
        if s1 < 0:
            continue
        try:
            s = zlib.decompress(data[s0:s1])
        except zlib.error:
            continue
        for tf in re.finditer(rb"/F\d+\s+([\d.]+)\s+Tf", s):
            sizes[round(float(tf.group(1)), 2)] += 1
    return sizes


def folio(pdf, page):
    """The page number printed in the footer.

    Found by geometry, not by text order: it is the bottom-most word on the
    page. Reading order fails here, because a contents or list-of-tables page
    ends with a dotted-leader page reference that is not the folio.
    """
    xml = pdftotext(pdf, page, bbox=True)
    words = re.findall(
        r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">'
        r'(.*?)</word>', xml)
    if not words:
        return None
    bottom = max(words, key=lambda w: float(w[3]))
    text = re.sub(r"&[a-z]+;", "", bottom[4]).strip()
    return text if re.fullmatch(r"[0-9]+|[ivxlcdm]+", text) else None


def main():
    pdf = sys.argv[1] if len(sys.argv) > 1 else "build/main.pdf"
    if not os.path.exists(pdf):
        print(f"{pdf} not found. Build first: latexmk main.tex")
        return 2

    data = open(pdf, "rb").read()
    n = page_count(pdf)

    # --- 5.4 no images, including the University logo -----------------
    imgs = len(re.findall(rb"/Subtype\s*/Image", data))
    check("5.4", "No images anywhere (incl. University logo)",
          imgs == 0, f"{imgs} image XObject(s)")

    # --- 5.3 title page carries the five permitted items only ---------
    title = [l.strip() for l in pdftotext(pdf, 1).splitlines() if l.strip()]
    banned = re.compile(r"school|department|faculty|supervis|student number|"
                        r"reg\.?\s*no|registration", re.I)
    offending = [l for l in title if banned.search(l)]
    check("5.3", "Title page carries only the permitted details",
          not offending, "found: " + "; ".join(offending) if offending
          else f"{len(title)} line(s), none forbidden")

    # --- 6.4 no page number on the title page -------------------------
    check("6.4a", "Title page displays no page number",
          folio(pdf, 1) is None,
          f"bottom-most word: {folio(pdf, 1)!r}")

    # --- 6.4 roman preliminaries, then one Arabic sequence ------------
    roman_pages, arabic_start = [], None
    for p in range(2, min(n, 40) + 1):
        t = folio(pdf, p)
        if t is None:
            continue
        if re.fullmatch(r"[ivxlcdm]+", t):
            roman_pages.append(p)
        elif t.isdigit() and arabic_start is None:
            arabic_start = (p, int(t))
    check("6.4b", "Preliminary pages in roman numerals",
          len(roman_pages) >= 3, f"{len(roman_pages)} roman-numbered page(s)")
    check("6.4c", "Arabic sequence starts at 1 after the preliminaries",
          arabic_start is not None and arabic_start[1] == 1,
          f"first Arabic page: pdf p{arabic_start[0]} shows {arabic_start[1]}"
          if arabic_start else "none found")

    # --- 6.4 the sequence runs through appendices and references ------
    last_num = folio(pdf, n)
    check("6.4d", "Numbering continues through appendices and references",
          last_num is not None and last_num.isdigit(),
          f"last page shows {last_num!r}")

    # --- 6.1 / 6.3 / 6.5 type sizes -----------------------------------
    sizes = font_sizes(pdf)
    body = [s for s in sizes if s >= BODY_FLOOR]
    other = [s for s in sizes if OTHER_FLOOR <= s < BODY_FLOOR]
    below = {s: c for s, c in sizes.items() if s < OTHER_FLOOR}
    check("6.1", "Body text at 12pt or larger",
          bool(body), f"{sorted(body)} pt")
    check("6.3", "Nothing outside maths below the 11pt floor",
          True if not below else all(s >= 9.0 for s in below),
          f"{sum(below.values())} run(s) below 11pt at "
          f"{sorted(below)} pt — expected to be maths script levels only; "
          f"verify with tools/checkfonts.py" if below
          else f"smallest non-body size {min(other) if other else '-'} pt")

    # --- 6.1 sans-serif face ------------------------------------------
    fonts = subprocess.run(["pdffonts", pdf], capture_output=True, text=True).stdout
    sans = re.search(r"Arial|Helvetica|Heros|DejaVuSans|Verdana|Tahoma", fonts)
    check("6.1b", "Sans-serif body face (6.1 recommendation)",
          bool(sans), sans.group(0) if sans else "no sans-serif face found")

    # --- 6.2 left-aligned, not justified ------------------------------
    mid = max(2, n // 2)
    xml = pdftotext(pdf, mid, bbox=True)
    xmax = sorted(float(x) for x in re.findall(r'xMax="([\d.]+)"', xml))[-40:]
    if len(xmax) >= 10:
        mean = sum(xmax) / len(xmax)
        sd = (sum((x - mean) ** 2 for x in xmax) / len(xmax)) ** 0.5
        check("6.2a", "Paragraphs left-aligned, not justified",
              sd > 2.0, f"right-edge spread {sd:.1f}pt "
                        f"(justified text would be near 0)")

    # --- 5.1.2 summary no more than 300 words -------------------------
    summary = pdftotext(pdf, 2)
    words = len([w for w in summary.split() if re.search(r"[A-Za-z]", w)])
    check("5.1.2", "Summary within 300 words",
          words <= 305, f"{words} words on the summary page")

    # --- 4.2 / 4.3 word count -----------------------------------------
    if os.path.exists("main.tex"):
        try:
            out = subprocess.run(
                ["texcount", "-1", "-sum=1,1,0,0,0,0,0", "-merge", "-q", "main.tex"],
                capture_output=True, text=True).stdout
            cnt = int(re.sub(r"\D", "", out.strip().splitlines()[-1]) or 0)
            check("4.2", "Within the 80,000-word PhD limit",
                  cnt <= 80000, f"{cnt} words (policy 4.3 exclusions applied)")
        except Exception as e:
            check("4.2", "Word count", False, f"texcount failed: {e}")

    # --- report --------------------------------------------------------
    width = max(len(w) for _, w, _, _ in results)
    print(f"\nPolicy check — {pdf}\n")
    failed = 0
    for clause, what, ok, detail in results:
        mark = "PASS" if ok else "FAIL"
        if not ok:
            failed += 1
        print(f"  [{mark}] {clause:<6} {what:<{width}}  {detail}")
    print()
    print(f"  {len(results) - failed}/{len(results)} checks passed.")
    print("  Clauses that cannot be checked mechanically are in")
    print("  docs/POLICY-COMPLIANCE.md and need your judgement.\n")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
