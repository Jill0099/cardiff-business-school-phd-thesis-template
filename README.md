# Cardiff Business School PhD Thesis LaTeX Template

A LaTeX thesis template for **Cardiff University / Cardiff Business School** PhD
candidates, built for XeLaTeX and structured for a **paper-style (three-essay)
thesis** — though it works as well for a monograph.

The defaults follow Cardiff's [Policy on the Submission and Presentation of
Research Degree Theses][policy], with clause numbers cited inline in the source
so you can check each one yourself. Everything you personalise lives in one
metadata block at the top of `main.tex`.

![Build](https://github.com/Jill0099/cardiff-business-school-phd-thesis-template/actions/workflows/build.yml/badge.svg)

[policy]: https://www.cardiff.ac.uk/__data/assets/pdf_file/0010/1467235/Submission-and-Presentation-of-Research-Degree-Theses.pdf

> **Check the policy yourself before submitting.** It is revised periodically,
> and this template reflects the version current when it was written. The clause
> citations are there to make re-checking quick, not to substitute for it.

---

## Quick start

```bash
git clone https://github.com/Jill0099/cardiff-business-school-phd-thesis-template.git
cd cardiff-business-school-phd-thesis-template
latexmk main.tex            # builds build/main.pdf
./tools/wordcount.sh        # counts against the 80,000-word limit
```

Then edit the metadata block in `main.tex`:

```latex
\newcommand{\thesistitle}{Thesis Title and Any Sub-Titles, in Bold, with Each Word Capitalised}
\newcommand{\thesisauthor}{Candidate's Full Name, as Recorded on the Student Record}
\newcommand{\thesisdegree}{Doctor of Philosophy}
\newcommand{\thesisdate}{Month Year}
```

**On Overleaf:** upload the repository as a zip and set the compiler to
**XeLaTeX** in *Menu → Compiler*.

---

## What the policy actually requires

These are the points where a generic thesis template gets Cardiff wrong. Each is
already handled here.

| Policy | Requirement | How the template handles it |
|---|---|---|
| §5.3 | The title page carries **five items only**: full title, degree award title, University name, month and year, and your full name as recorded on the student record | `frontmatter/titlepage.tex` reproduces the Appendix 3 template exactly. No department, school, supervisor or student number |
| §5.4 | "The title page must have a plain background. **No images should be used: this includes the University logo**" | No logo anywhere in the repo |
| §5.1 | Required preliminary pages: title page, summary (**max 300 words**), contents list, and acknowledgements where a sponsor expects them | Assembled in that order in `main.tex` |
| §5.2 | Lists of tables and figures go **immediately after** the contents list | Ordered accordingly |
| §5.6 | Dedication and acknowledgements come **after** the required pages | Ordered accordingly |
| §5.7 | A preface may explain how any papers relate to the thesis | `frontmatter/preface.tex` — a co-authorship statement for a three-essay thesis |
| §6.1 | Font recommended for easy reading — **sans serif** such as Arial, Tahoma, Verdana — at **no less than 12 pt** | Arial by default, with a one-line switch back to Times |
| §6.2 | **Left-aligned, not justified**; line spacing wide enough for accessibility, "e.g. 1.5" | `\RaggedRight` and `\onehalfspacing` |
| §6.3 | Footnotes and captions **no smaller than 11 pt** | `\footnotesize` redefined to 11 pt |
| §6.4 | Roman numerals for preliminary pages, then a single Arabic sequence to the end; page numbers on **every page except the title page** | Handled in `main.tex`; no `\thispagestyle{empty}` on chapter openings |
| §4.2 | PhD (standard format): **80,000 words** | `tools/wordcount.sh` |
| §4.3 | The count **excludes** summary, acknowledgements, declarations, contents, appendices, tables, diagrams and figures, references, bibliography, footnotes and endnotes | Encoded as TeXcount directives in `main.tex` |

**There is no declaration page in this template, and that is deliberate.** Cardiff
collects the statements and declarations on a separate signed form (Appendix 1
of the policy), not bound into the thesis. The final word count goes on that form
too (§5.5), not in the thesis.

---

## Word count

```
$ ./tools/wordcount.sh

  Counted (policy 4.3 exclusions)         261
  Limit (policy 4.2)                    80000
  Limit + 10% (policy 4.4)              88000

  Within the limit.

  Per chapter:
    chapters/chapter1.tex               226
    ...
```

Pass a different limit for another award — `./tools/wordcount.sh 50000` for
MPhil or a professional doctorate, `60000` for MD.

The exclusions in §4.3 are encoded in the source: `%TC:ignore` brackets the front
matter, appendices and bibliography, `%TC:macro \footnote [ignore]` drops
footnotes, and the TeXcount weights count body text and headings but not
captions, floats or maths. It is an estimate — agree the final figure with your
supervisor before it goes on the form.

---

## Repository layout

```
main.tex                 preamble, metadata block, document assembly
latexmkrc                build config (XeLaTeX + bibtex + nomenclature)
references.bib           bibliography
tools/wordcount.sh       word count against the policy limits
frontmatter/
  titlepage.tex          Appendix 3 title page — do not add to it
  summary.tex            the required summary, max 300 words
  acknowledgements.tex
  dedication.tex         optional
  preface.tex            optional; co-authorship for a paper-style thesis
  abbreviations.tex      acronym list; use \ac{KEY} in the text
  nomenclature.tex       symbol list; off by default
chapters/
  chapter1.tex           full empirical chapter skeleton (see below)
  chapter2-6.tex         stubs, same shape as chapter 1
  appendix.tex           variable definitions + supplementary results
```

---

## What chapter 1 gives you

`chapters/chapter1.tex` is laid out as a complete empirical study, so it doubles
as a skeleton for any paper-style chapter:

| Section | What goes there |
|---|---|
| Introduction | background, motivation, research questions, findings, contributions, roadmap |
| Literature Review | strands of prior work, then a synthesis naming the gap |
| Theoretical Framework | core framework, mechanism, and a TikZ conceptual diagram |
| Hypothesis Development | hypotheses stated with their predicted signs |
| Data and Model | sample, variable construction, the estimating equation |
| Empirical Results | descriptives, baseline, identification, mechanism, heterogeneity, robustness |
| Conclusion | findings, implications, limitations |

It ships with two worked exhibits to copy: a **descriptive statistics table** and
a **four-column regression table** with a fixed-effects ladder, clustered
standard errors in parentheses and significance stars — both `booktabs`, with
placeholder cells (`[.]`, `[N]`) rather than numbers.

The comments in the file are prompts about what belongs in each section. Delete
them as you write.

---

## Other features

- **Graceful font fallback.** Arial if installed, otherwise TeX Gyre Heros, then
  DejaVu Sans — so it compiles anywhere, including on CI.
- **Serif switch.** Set `\usesansfontfalse` in `main.tex` for Times New Roman.
  §6.1 is a recommendation, not a prohibition, and serif faces remain common in
  Business School theses — ask your supervisor.
- **Optional CJK support** via `xeCJK`, commented out in the preamble.
- **`subfiles`.** `latexmk chapters/chapter3.tex` builds that chapter alone, with
  the right chapter number, while the full thesis still builds from `main.tex`.
- **Harvard referencing** (`agsm` via `natbib`), the usual Cardiff Business
  School choice. Confirm with your supervisor.
- **`cleveref`** for `\cref{}` cross-references.
- **CI build** on every push.

---

## Requirements

A full TeX distribution (TeX Live 2021+ or MacTeX) with `latexmk` and `texcount`.
Build with **XeLaTeX** — the template uses `fontspec` and `unicode-math`, which
pdfLaTeX does not support.

---

## Licence

[MIT](LICENSE). Use it for your thesis, no attribution required.

Not an official Cardiff University template, and not affiliated with or endorsed
by the University. The policy is the authority; this is a convenience.
