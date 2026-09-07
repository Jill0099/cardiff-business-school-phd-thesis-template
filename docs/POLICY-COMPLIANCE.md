# Clause-by-clause compliance

Every clause of Cardiff University's [Policy on the Submission and Presentation
of Research Degree Theses][policy], checked against this template.

**Policy version audited:** 8.0 — approved by ASQC 08.05.2025, in effect from
01.08.2025, owned by Education Governance (PGR Quality and Operations).

**Audited:** at the template's last commit. The policy is revised periodically.
If the version banner on the PDF no longer says 8.0, treat this table as stale
and re-check.

[policy]: https://www.cardiff.ac.uk/__data/assets/pdf_file/0010/1467235/Submission-and-Presentation-of-Research-Degree-Theses.pdf

## Key

| | Meaning |
|---|---|
| **DONE** | The template implements this. Nothing for you to do. |
| **NOTED** | Can't be enforced by LaTeX; the requirement is written into the relevant file's comments so you meet it while writing. |
| **YOURS** | Your action, outside anything a template can do. Listed so nothing is silently dropped. |
| **N/A** | Administrative or process clause with no bearing on the document. Listed for completeness. |

---

## 1. General Statements

| Clause | Requirement | Status | Where |
|---|---|---|---|
| 1.1 | Applies to PhD, MD, EngD, professional doctorates, MPhil | **DONE** | Limits in `tools/wordcount.sh`; PhD is the default |
| 1.2 | Does *not* apply to PhD by Published Works, higher doctorates, MRes | **NOTED** | Scope warning in `tools/wordcount.sh` and the README |
| 1.3 | "Thesis" includes other approved forms of submission | N/A | — |
| 1.4 | "Candidate" replaces "student" from submission | N/A | — |
| 1.5 | Not following the policy may mean your School **rejects the thesis** | **YOURS** | The reason this table exists |
| 1.6 | Read alongside the Final Deposit policy | **YOURS** | Separate document, not covered here |

## 2. Presenting Your Thesis for Examination

| Clause | Requirement | Status | Where |
|---|---|---|---|
| 2.1 | You prepare and present the thesis | N/A | — |
| 2.2 | Submit a **single electronic PDF** | **DONE** | `latexmk main.tex` produces one PDF at `build/main.pdf` |
| 2.3 | Turnitin upload mandatory in some Schools | **YOURS** | Ask your School |
| 2.4 | Email submission from your University account | **YOURS** | — |
| 2.5 | Accompanying material in stable electronic formats; datasets and analysis scripts submitted so they can be examined and reproduced | **YOURS** | Keep code and data in a separate repository |
| 2.6 | Oversized or AV material as supplementary files | **YOURS** | — |
| 2.7 | Submit with a **Notice of Submission Form** and a **Statements and Declarations Form** by the deadline | **NOTED** | `frontmatter/README.md` |
| 2.8 | No changes after the thesis is accepted for examination | **YOURS** | — |
| 2.9 | Examiners' hard copies are printed **double-sided by your School**, exactly as submitted, unchecked | **DONE** | Explains why no binding margin is mandated; the wide left margin here is convention, not requirement |
| 2.10 | A personal hard copy is optional | N/A | — |

## 3. Accepting the Thesis for Examination

| Clause | Requirement | Status | Where |
|---|---|---|---|
| 3.1 | The Convenor **reviews format and presentation** against these requirements | **YOURS** | The clause that makes sections 5 and 6 worth getting right |
| 3.2 | Submission fee in defined cases | N/A | — |
| 3.3 | Acceptance does not prejudice the examiners | N/A | — |
| 3.4 | You may appeal a refusal | N/A | — |

## 4. Format and Word Length

| Clause | Requirement | Status | Where |
|---|---|---|---|
| 4.1 | English or Welsh, apart from quotations and technical terms | **DONE** | `babel` english; Welsh option noted in `main.tex` |
| 4.2 | PhD 80,000 · EngD 80,000 · MD 60,000 · MPhil 50,000 · professional doctorates 50,000 | **DONE** | `tools/wordcount.sh`, default 80,000 |
| 4.3 | Count **excludes** summary, acknowledgements, declarations, contents, appendices, tables, diagrams and figures, references, bibliography, footnotes and endnotes | **DONE** | `%TC:ignore` blocks and `%TC:macro \footnote [ignore]` in `main.tex`; TeXcount weights exclude captions, floats and maths |
| 4.4 | Schools may allow up to **10% over**, where the topic justifies it | **DONE** | Reported by `tools/wordcount.sh` |
| 4.5 | Beyond that, needs College Postgraduate Dean approval | **NOTED** | Flagged by `tools/wordcount.sh` |
| 4.6 | PhD → MPhil re-presentation need not be shortened unless examiners direct | N/A | — |
| 4.7 | Appendices where the material usefully adds to or explains the work | **NOTED** | `chapters/appendix.tex` |
| 4.8–4.12 | Practice-led, Creative and Critical Writing, Music Composition, Music Performance, Creative Practice in Architecture have **their own limits** | **NOTED** | Scope warning in `tools/wordcount.sh`. This template is not designed for these |
| 4.13 | Non-text artefact may be a major component, with a written commentary of at least 50% | **NOTED** | Out of scope |
| 4.14 | Professional doctorates may submit a research portfolio | **NOTED** | Out of scope |

## 5. Preliminary Pages

| Clause | Requirement | Status | Where |
|---|---|---|---|
| 5.1.1 | Title page per Appendix 3 | **DONE** | `frontmatter/titlepage.tex` |
| 5.1.2 | Summary of **no more than 300 words** | **DONE** (page) / **YOURS** (count) | `frontmatter/summary.tex` |
| 5.1.3 | Contents list with a page number for every chapter and sub-division | **DONE** | `tocdepth`/`secnumdepth` set to 3 in `main.tex` |
| 5.1.4 | Acknowledgements where your sponsor expects them | **DONE** | `frontmatter/acknowledgements.tex` |
| 5.2 | Contents itemises all chapters and sub-divisions; other lists come **immediately after** it | **DONE** | Lists of tables and figures follow the contents in `main.tex` |
| 5.3 | Title page carries these details **only**: full title incl. sub-title · degree award title · University name · month and year · full name as on the student record | **DONE** | `frontmatter/titlepage.tex`. No department, school, supervisor or student number |
| 5.3.4 fn 3 | After **corrections**, the title page keeps the **original submission date**. For **re-examination**, use the re-submission date | **NOTED** | Comment on `\thesisdate` in `main.tex` |
| 5.4 | Plain background. **No images — including the University logo** | **DONE** | No logo in the repository at all |
| 5.5 | The final word count goes on the Statements and Declarations Form | **NOTED** | `frontmatter/README.md`; `tools/wordcount.sh` gives you the figure |
| 5.6 | A dedication and/or acknowledgements may follow the required pages | **DONE** | Ordered accordingly in `main.tex` |
| 5.7 | A preface may relate papers you authored or co-authored to the **chapters** of the thesis | **DONE** | `frontmatter/preface.tex` — but see §8 |

## 6. Document Formatting

| Clause | Requirement | Status | Where |
|---|---|---|---|
| 6.1 | Clear readable font, sans serif recommended (Arial, Tahoma, Verdana), **no less than 12 pt** | **DONE** | Arial → TeX Gyre Heros → DejaVu Sans fallback chain; 12pt base |
| 6.2 | **Left-aligned, not justified**; spacing wide enough to be accessible, e.g. 1.5 | **DONE** | `\RaggedRight` and `\onehalfspacing` |
| 6.3 | All other text — footnotes, figure captions — **not less than 11 pt** | **DONE**, verified | `\footnotesize`, `\scriptsize` and `\tiny` all redefined to 11 pt; captions at 12 pt. Confirmed by reading the font-size operators out of the built PDF — see the note below |
| 6.4 | Roman numerals for preliminary pages, then a **single Arabic sequence** throughout; page numbers on **every page except the title page**; the sequence includes preliminary pages, figures, tables, appendices and references | **DONE** | Title page opens the roman sequence as page i and shows no number; no `\thispagestyle{empty}` on chapter openings; appendices and references stay in the Arabic sequence |
| 6.5 | Figures may be colour or black and white but must be clear and legible; characters **inside tables and figures** must be legible and large enough for accessibility; **avoid placing text over images** | **DONE** (type size) / **NOTED** (the rest) | The 11 pt floor covers table and figure text. Mathematical script levels raised from LaTeX's defaults — significance stars in the worked table went from 7.7 pt to 9.5 pt. Text-over-images noted in `main.tex`, with the compliant fixes for a table that will not fit |

### Note on the 11 pt floor, and how it was verified

This was checked by reading the font-size operators out of the built PDF, not by
trusting the source. Run it yourself:

```
python3 tools/checkfonts.py
```

Two things that reading turns up, both worth understanding before you assume a
breach:

**LaTeX's 12 pt is written into the PDF as 11.96.** A TeX point is 1/72.27 inch
and a PDF point is 1/72 inch. Every LaTeX document does this and it is
universally accepted as 12 pt; the checker accounts for it rather than flagging
it.

**Mathematical superscripts and subscripts are necessarily below 11 pt.** No
thesis in any discipline sets a subscript index at 11 pt — it is not what §6.3
is about, which is why this template does not pretend otherwise. But §6.5 *does*
reach the significance stars in a regression table, so the script levels are
raised above LaTeX's defaults: stars went from 7.7 pt to 9.5 pt, and equation
indices from 8.4 pt to 10 pt. In the current build nothing outside mathematics
falls below 10.91 pt (= 11 TeX pt), and `tools/checkfonts.py` will tell you if a
`\scriptsize` creeps into your own chapters and breaks that.

## 7. Acknowledging the Work of Others

| Clause | Requirement | Status | Where |
|---|---|---|---|
| 7.1 | You declare the work and ideas are your own except where referenced | **YOURS** | On the Statements and Declarations Form |
| 7.2 | Third-party material acknowledged, with the copyright owner's permission where needed | **YOURS** | See §12 |
| 7.3 | Collaborators' contributions go in your **acknowledgements** *and* are referenced in the main text | **NOTED** | `frontmatter/acknowledgements.tex`. Note this is *in addition to* the preface |

## 8. Inclusion of Papers

| Clause | Requirement | Status | Where |
|---|---|---|---|
| 8.1 | A "thesis with publication" — papers replacing traditional chapters — is permitted, and is governed by **separate guidance**: *Presentation of Research Degree Theses: Guidance on the Inclusion of Papers and Published Work* | **YOURS — GAP** | See below |
| 8.2 | The same guidance applies to a traditional thesis that adapts your published work | **YOURS — GAP** | See below |

> **This is the one thing in the policy that this template cannot check for you.**
> That guidance document is not published on the public website — it is on the
> staff and student intranet. Since this template is shaped for a paper-style
> (three-essay) thesis, and §8 is exactly the clause governing that format, get
> the guidance from your PGR office and check the chapter structure and
> `frontmatter/preface.tex` against it before relying on them. Everything else in
> this table still holds; that guidance may add requirements on top.

## 9. Acknowledgements / Dedications

| Clause | Requirement | Status | Where |
|---|---|---|---|
| 9.1 | Be mindful of tone — the page is read widely, including by employers and funders | **NOTED** | `frontmatter/acknowledgements.tex` |
| 9.2 | **No private personal details or confidential information** about yourself or others, in the acknowledgements or anywhere else | **NOTED** | `frontmatter/acknowledgements.tex` |

## 10. Proofreading

| Clause | Requirement | Status | Where |
|---|---|---|---|
| 10.1 | Minimal typing and spelling errors; **bibliographic citations and references consistent throughout** | **DONE** (consistency) / **YOURS** (proofreading) | `natbib` with a single `agsm` style gives consistent citations by construction |

## 11. Third-Party Editors

| Clause | Requirement | Status | Where |
|---|---|---|---|
| 11.1–11.9 | If anyone outside your supervisory team — including family, friends and peers — helps with drafting, the Appendix 2 procedure applies. Supervisors are not third parties. An editor may advise on spelling, punctuation, grammar, footnote formatting, sentence length, and table and figure positioning — **not** on content, argument, or shortening to fit the word limit. Non-compliance can be treated as academic misconduct | **YOURS** | Nothing a template can do. Read Appendix 2 before letting anyone edit |

## 12. Third-Party Copyright

| Clause | Requirement | Status | Where |
|---|---|---|---|
| 12.1–12.5 | Copying third-party material is generally fine **for examination**, but making the thesis available afterwards may need the copyright owner's permission. Where permission is refused, deposit a redacted version with the material replaced by a bibliographic reference. Check your own publishing agreements before reproducing your published text. Advice: copyright@cardiff.ac.uk | **YOURS** | Relevant if you reproduce figures, tables or extracts from published sources |

## 13. Deposit After Examination

| Clause | Requirement | Status | Where |
|---|---|---|---|
| 13.1–13.6 | The approved thesis is uploaded to ORCA before the award is confirmed, and made openly available subject to any approved bar on access | **YOURS** | Governed by the Final Deposit policy |
| 13.7 | Print-only theses are bound in boards, with **surname and initials, title, degree and date (month and year) on the spine** | **YOURS** | Only applies to the print-only cases in 13.5 |
| 13.8 | Sign and submit a **new** Statements and Declarations Form with the final version | **NOTED** | `frontmatter/README.md` |

## 14. Ownership

| Clause | Requirement | Status | Where |
|---|---|---|---|
| 14.1–14.2 | You own the IP by default; depositing grants the University a licence to store it; you may publish elsewhere subject to studentship or contractual terms | N/A | — |

## 15. Restrictions on Access

| Clause | Requirement | Status | Where |
|---|---|---|---|
| 15.1 | A temporary bar on access may be applied for under the Bar on Access Policy | **YOURS** | Relevant if a chapter is under review or commercially sensitive |

## Appendices

| Appendix | Content | Status | Where |
|---|---|---|---|
| 1 | Statements and Declarations, signed and **submitted loose with the thesis** — not bound in | **DONE** | No declaration page in the template; explained in `frontmatter/README.md` |
| 2 | Third-Party Editors procedure | **YOURS** | See §11 |
| 3 | Title page template | **DONE** | `frontmatter/titlepage.tex` reproduces it |

---

## Verifying this yourself

Two of the three claim types in this table can be checked by machine. Run:

```
latexmk main.tex
python3 tools/checkpolicy.py     # clauses checkable against the PDF
python3 tools/checkfonts.py      # every type size in the output
./tools/wordcount.sh             # 4.2-4.4
```

`checkpolicy.py` reads the **compiled PDF**, not the source, so it reports what
an examiner receives. Current result:

```
  [PASS] 5.4    No images anywhere (incl. University logo)             0 image XObject(s)
  [PASS] 5.3    Title page carries only the permitted details          6 line(s), none forbidden
  [PASS] 6.4a   Title page displays no page number
  [PASS] 6.4b   Preliminary pages in roman numerals                    9 roman-numbered page(s)
  [PASS] 6.4c   Arabic sequence starts at 1 after the preliminaries    pdf p11 shows 1
  [PASS] 6.4d   Numbering continues through appendices and references  last page shows '19'
  [PASS] 6.1    Body text at 12pt or larger                            11.96pt and up
  [PASS] 6.3    Nothing outside maths below the 11pt floor
  [PASS] 6.1b   Sans-serif body face                                   Arial
  [PASS] 6.2a   Paragraphs left-aligned, not justified                 right-edge spread 17.1pt
  [PASS] 5.1.2  Summary within 300 words
  [PASS] 4.2    Within the 80,000-word PhD limit

  12/12 checks passed.
```

Run it again after you have written your own chapters — the checks that matter
most (summary length, word count, and whether a `\scriptsize` has crept into a
table) only become meaningful once there is real content.

---

## Source text

The clauses this template acts on, in the policy's own words, so you can verify
each row against the [PDF][policy] rather than taking this table on trust. Page
numbers are the printed numbers in the document.

| Clause | p. | Wording |
|---|---|---|
| 4.2.1 | 3 | "PhD (standard format): 80,000 words" |
| 4.3 | 3 | "excludes the summary, acknowledgements, declarations, contents pages, appendices, tables, diagrams and figures, references, bibliography, footnotes and endnotes" |
| 4.4 | 3 | "up to 10% more than the stated limit, but only where this is clearly justified" |
| 5.1 | 5 | "a title page…; a summary of no more than 300 words; a list of contents…; acknowledgements, where this is an expectation of your sponsor" |
| 5.2 | 5 | "Any other lists (e.g. tables, diagrams, illustrations) should be included separately, immediately after the contents list" |
| 5.3 | 5–6 | "must include the following details only" — title, degree award title, University name, month and year, candidate's full name |
| 5.3.4 fn 3 | 6 | after approved corrections "the date on the title page should be the original date of submission" |
| 5.4 | 6 | "The title page must have a plain background. No images should be used: this includes the University logo" |
| 5.6 | 6 | a dedication and/or acknowledgements "must appear after the required pages listed above" |
| 5.7 | 6 | a preface highlighting how papers "relate to the chapters of your thesis" |
| 6.1 | 6 | "sans serif fonts such as Arial, Tahoma and Verdana… no less than 12 point" |
| 6.2 | 6 | "left-aligned, rather than justified… e.g. 1.5 spacing" |
| 6.3 | 6 | "Characters used in all other texts (e.g. footnotes, figure captions) must not be less than 11 point" |
| 6.4 | 6 | "Page numbers must be displayed on all pages except the title page" |
| 6.5 | 6 | "Characters used within tables and figures must be legible… The placing of text over images should be avoided" |
| 7.3 | 7 | collaborators' contributions "should be highlighted in your acknowledgements, as well as clearly referenced within the main text" |
| 9.2 | 7 | "you should not include any private personal details or other confidential information" |
| App. 1 | 11 | "Statements and Declarations to be Signed by the Candidate and Submitted loose with the Thesis" |
| App. 3 | 13 | Title Page Template |

Quoted for verification. The [policy PDF][policy] is the authority; if these
differ from the current version, the policy wins and this table is stale.

---

## Summary

Of the clauses that bear on the document itself, all are implemented or written
into the source as prompts. The rest are process clauses listed so you can see
they were considered rather than missed.

**One genuine gap:** §8. The paper-style format has its own guidance document
that is not publicly accessible, so this template's three-essay shape is
convention plus common sense, **not** verified against the rule that governs it.
Get that document.

**Two things this template cannot check:** whether your summary is under 300
words (§5.1.2), and whether your final word count is right (§5.5) — run
`tools/wordcount.sh`, then agree the figure with your supervisor.

**Not from the policy:** Harvard (`agsm`) referencing and the three-essay
structure are Cardiff Business School convention. The policy sets no referencing
style. Confirm both with your supervisor.
