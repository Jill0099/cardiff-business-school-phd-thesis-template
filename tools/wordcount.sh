#!/usr/bin/env bash
#
# Word count for a Cardiff University research degree thesis.
#
# From the Policy on the Submission and Presentation of Research Degree
# Theses:
#
#   4.2  Maximum words -- PhD (standard format): 80,000; EngD: 80,000;
#        MD: 60,000; MPhil (standard format): 50,000; professional
#        doctorates: 50,000.
#   4.3  The calculation "excludes the summary, acknowledgements,
#        declarations, contents pages, appendices, tables, diagrams and
#        figures, references, bibliography, footnotes and endnotes".
#   4.4  Schools may accept up to 10% over the limit, where the nature
#        of the topic clearly justifies it.
#   5.5  The final count goes on the Statements and Declarations Form.
#
# Scope (1.1, 1.2): the policy covers PhD, MD, EngD, professional
# doctorates and MPhil. It does NOT cover the PhD by Published Works,
# higher doctorates, or MRes -- different rules apply to those.
#
# Practice-led and Creative and Critical Writing submissions have their
# own limits under 4.8-4.9, not the ones below.
#
# Those exclusions are encoded in main.tex as TeXcount directives
# (%TC:ignore around the front matter, appendices and bibliography;
# %TC:macro \footnote [ignore]) and by the weights below, which count
# body text and headings only -- not captions, floats or maths.
#
# This is an estimate. Agree the final figure with your supervisor
# before you put it on the form.
#
# Usage:  ./tools/wordcount.sh [limit]        # limit defaults to 80000

set -euo pipefail
cd "$(dirname "$0")/.."

LIMIT="${1:-80000}"

if ! command -v texcount >/dev/null 2>&1; then
    echo "texcount not found. It ships with TeX Live -- check that your" >&2
    echo "TeX bin directory is on PATH." >&2
    exit 1
fi

# -sum=1,1,0,0,0,0,0 -> body text + headings; no captions, floats, maths.
# -merge             -> follow \subfile and \input into the chapters.
count=$(texcount -1 -sum=1,1,0,0,0,0,0 -merge -q main.tex 2>/dev/null | tail -1 | tr -dc '0-9')

if [ -z "$count" ]; then
    echo "texcount produced no number. Run it directly to see the error:" >&2
    echo "  texcount -sum=1,1,0,0,0,0,0 -merge main.tex" >&2
    exit 1
fi

discretionary=$((LIMIT * 110 / 100))

printf '\n'
printf '  %-34s %8s\n' "Counted (policy 4.3 exclusions)" "$count"
printf '  %-34s %8s\n' "Limit (policy 4.2)"              "$LIMIT"
printf '  %-34s %8s\n' "Limit + 10% (policy 4.4)"        "$discretionary"
printf '\n'

if   [ "$count" -le "$LIMIT" ]; then
    printf '  Within the limit.\n\n'
elif [ "$count" -le "$discretionary" ]; then
    printf '  Over the limit but within the 10%% School discretion (policy 4.4).\n'
    printf '  That discretion is not automatic -- your School has to agree it.\n\n'
else
    printf '  Over the limit and beyond the 10%% discretion.\n'
    printf '  Policy 4.5: acceptance needs College Postgraduate Dean approval.\n\n'
fi

# Per-chapter breakdown, to show where the words actually are.
printf '  Per chapter:\n'
for f in chapters/chapter*.tex; do
    n=$(texcount -1 -sum=1,1,0,0,0,0,0 -q "$f" 2>/dev/null | tail -1 | tr -dc '0-9')
    printf '    %-30s %8s\n' "$f" "${n:-0}"
done
printf '\n'
