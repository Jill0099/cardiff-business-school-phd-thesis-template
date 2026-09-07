# Cardiff Business School PhD Thesis LaTeX Template

A clean LaTeX thesis template for **Cardiff University / Cardiff Business School**
PhD candidates, built for XeLaTeX and structured for a **paper-style (three-essay)
thesis** — though it works just as well for a monograph, and nothing in it is
Cardiff-specific enough to stop you using it at another university.

Everything you personalise lives in one metadata block at the top of `main.tex`.
The front matter fills itself in from there.

![Build](https://github.com/Jill0099/cardiff-business-school-phd-thesis-template/actions/workflows/build.yml/badge.svg)

---

## Quick start

```bash
git clone https://github.com/Jill0099/cardiff-business-school-phd-thesis-template.git
cd cardiff-business-school-phd-thesis-template
latexmk main.tex          # builds build/main.pdf with XeLaTeX
```

Then open `main.tex` and edit the metadata block:

```latex
\newcommand{\thesistitle}{Title of Your Thesis}
\newcommand{\thesisauthor}{Author Name}
\newcommand{\thesisuniversity}{University Name}
\newcommand{\thesissupervisor}{Prof. Supervisor Name}
...
```

Drop your institution's crest into `figures/` and point `\thesislogo` at it.

**On Overleaf:** upload the repository as a zip, then set the compiler to
**XeLaTeX** in *Menu → Compiler*. `main.tex` is detected as the root file
automatically.

---

## Repository layout

```
main.tex                 preamble, metadata block, document assembly
latexmkrc                build config (XeLaTeX + bibtex + nomenclature)
references.bib           bibliography
frontmatter/
  titlepage.tex          title page, driven by the metadata macros
  certificate.tex        supervisor's certificate (omit if not required)
  declaration.tex        candidate's declaration
  acknowledgements.tex
  dedication.tex
  abstract.tex
  abbreviations.tex      acronym list; use \ac{KEY} in the text
  nomenclature.tex       symbol list
chapters/
  chapter1.tex           full empirical chapter skeleton (see below)
  chapter2-6.tex         stubs, same shape as chapter 1
  appendix.tex           variable definitions + supplementary results
figures/
  university-logo.pdf    placeholder crest — replace with your own
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

It ships with two worked exhibits you can copy: a **descriptive statistics
table** and a **four-column regression table** with a fixed-effects ladder,
clustered standard errors in parentheses, and significance stars — both in
`booktabs` style with placeholder cells (`[.]`, `[N]`) rather than numbers.

The comments in the file are prompts about what belongs in each section, not
instructions to the compiler. Delete them as you write.

---

## Features

- **XeLaTeX with graceful font fallback.** Uses Times New Roman if installed,
  otherwise TeX Gyre Termes, so the template compiles on any machine and on CI.
- **Optional CJK support.** Uncomment the `xeCJK` block in `main.tex` for
  Chinese, Japanese, or Korean text.
- **`subfiles`.** Each chapter compiles on its own — `latexmk chapters/chapter3.tex`
  builds just that chapter, with the right chapter number, while the full thesis
  still builds from `main.tex`.
- **Thesis-regulation defaults.** A4, 12pt, double-spaced body, 1.5in binding
  margin, single-spaced contents and bibliography, widow and orphan control.
- **Front matter that assembles itself** from the metadata block.
- **Nomenclature and acronym lists** wired into the build via `latexmkrc`.
- **Harvard (`agsm`) citations** through `natbib`; swap `\bibliographystyle` for
  a numeric style if your field prefers one.
- **`cleveref`** for `\cref{}` cross-references.
- **CI build** on every push, so a broken template is caught immediately.

---

## Adapting it to your university

Thesis regulations vary, and most institutions mandate exact wording on some
pages. The places to check:

1. **Margins** — `\geometry{...}` in `main.tex`. The default assumes a 1.5in
   left margin for binding.
2. **Line spacing** — `\doublespacing` in `main.tex`. Some universities specify
   1.5.
3. **Declaration wording** — `frontmatter/declaration.tex` is usually
   prescribed verbatim. Replace it with yours.
4. **Certificate page** — not universal. If yours does not require one, comment
   out its `\input` line in `main.tex`.
5. **Word limit and abstract length** — check whether the abstract counts
   towards it.

---

## Requirements

A full TeX distribution (TeX Live 2021+ or MacTeX), plus `latexmk`. All packages
used are on CTAN and ship with a full install. Build with **XeLaTeX** — the
template uses `fontspec` and `unicode-math`, which pdfLaTeX does not support.

---

## Licence

[MIT](LICENSE). Use it for your thesis, no attribution required.
