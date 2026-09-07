#!/usr/bin/env bash
#
# Regenerate the README preview images from the compiled thesis.
#
# Run after any change that alters how the output looks, so the images
# on the front page keep matching what the template actually produces.
#
# Requires pdftoppm (poppler) and Python with Pillow.
#
# Usage:  ./tools/preview.sh

set -euo pipefail
cd "$(dirname "$0")/.."

command -v pdftoppm >/dev/null 2>&1 || { echo "pdftoppm not found (brew install poppler)" >&2; exit 1; }

echo "Building the thesis..."
latexmk -xelatex -interaction=nonstopmode main.tex >/dev/null

mkdir -p docs/preview

# page number -> output name. Update these if the page order changes.
render() {
    pdftoppm -png -r 100 -f "$1" -l "$1" -singlefile build/main.pdf "docs/preview/$2" -q
    echo "  page $1 -> docs/preview/$2.png"
}

echo "Rendering..."
render 1  01-title
render 3  02-contents
render 11 03-chapter
render 18 04-table

# Thin grey frame, so white pages stay visible against GitHub's
# light-mode background without disappearing in dark mode.
python3 - <<'PY'
from PIL import Image, ImageOps
import glob
for f in sorted(glob.glob("docs/preview/*.png")):
    im = Image.open(f).convert("RGB")
    ImageOps.expand(im, border=2, fill=(190, 197, 205)).save(f, optimize=True)
PY

echo "Done."
