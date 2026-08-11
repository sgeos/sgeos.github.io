# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-11
**Task**: A370 brought into the repository from the Keleusma working tree, brought to house standards, and
retargeted for a general audience. **Committed, not pushed.** **Not published.**

`_drafts/two_calling_conventions.markdown`, editorial date **2026-08-07**, series `keleusma_native` index
2, the sequel to the published A369. **8,937 words, 21 display equations, 53 reference definitions.**

---

## What I Did With the File You Pointed At

**The copy already existed and was byte-identical**, so there was nothing to fetch. An untracked
`_drafts/2026-08-11-two_calling_conventions.markdown` was sitting in the working tree carrying the wrong
date and a date-prefixed name that no other draft uses. **I confirmed it identical to your source, created
the correctly named and dated file, and removed the duplicate.** Nothing was lost, since the source in the
Keleusma tree is untouched.

---

## Standards, Which Was the Mechanical Half

- **Twenty-five prose colons and seven prose semicolons removed** by restructuring the sentences. The style
  guide permits neither outside front matter and the debug tag.
- **Ten italic emphasis spans converted to bold.** The style guide does not mention italics, so I checked
  the corpus. Fifty-nine of 297 published posts use them, **but the recent run uses none and the direct
  predecessor A369 uses none**, so bold is current practice.
- **Six acronyms given first-use spell-outs**, being POSIX, LLVM, ABI, PEP, ECMA and ELF.
- **The reference block consolidated** from three `Reference, ...` subheadings into a single sorted
  `Reference`, which is what A369 emits and what the corpus convention specifies.
- **`_lib/reflow.py` applied** to restore atomic bold spans, verified a fixed point after one pass and
  **content-preserving**, with word count, equation count, definition count and normalised text all
  identical before and after. `lint.scan` is clean afterwards.

**One thing I deliberately did not change.** Colons inside verbatim citation titles stay. **A369 carries
846 of them across 3,415 entries**, so they are established practice in this series rather than a defect,
and rewriting a published title would be worse than keeping the punctuation.

---

## Retargeting, Which Was the Real Job

**The article already claimed no compiler background was required and then opened with compiler
backends.** The changes close that gap.

- **The title now leads with plain words.** *One Construct, Two Calling Conventions* became **Two Ways of
  Doing One Thing**, keeping the memorable second half about a design wart being a semantic boundary.
- **The lede leads with the counting argument**, which anyone can follow. One case has two things to report
  and one slot to report them in, the other has one thing and one slot, and that settles it before any code
  is written. The compiler arrives afterwards as the instance rather than the subject.
- **A `How to read this` section** names the three sections a general reader can take and stop at, and
  states that the mathematics is optional because every display is preceded by the same claim in words.
- **Seven jargon terms glossed at first use**, being backend, host, chunk, stack frame, bytecode, lowering
  and register.

---

## One Error of Mine, Caught on Re-reading

The new lede first said that twenty of twenty-odd instances had the shape that invited the tidy-up.
**The figure that actually misled the author was nine of nine**, which is a different measurement in a
different table, and I had conflated it with the twenty-two of twenty-four stream figure. A leftover
sentence from the old lede had also been glued onto the end of a new paragraph. **Both were found by
reading the result rather than by any check.**

---

## Verification

- `python3 _verify.py` **0 errors, 21 warnings**, the unchanged baseline, taken from the repository root.
- **Prose scan clean.** Zero em dashes, en dashes, minus signs, contractions, prose colons, prose
  semicolons, prose parentheses, curly quotes and italics.
- `lint.scan` **clean**.
- **Isolated build exit 0**, the article rendering at its live URL with **21 open and 21 close display-math
  delimiters**, zero unresolved references, zero literal Liquid, two tables, two code blocks, and series
  navigation reporting **Part 2**.
- The `post_url` back-reference to A369 resolves, since that article is published at 2026-08-06.

**`check_any.py` was not used and should not be.** It derives an article number from the debug marker and
validates it against the X-Planes roster, so it fails A370 for not being an aircraft.

---

## What I Did Not Do

**I did not push**, since only the publication-review prompt authorises that and this was not one. **I did
not publish.** **I did not run the four-pass review** the X-Planes articles get, because this article did
not arrive that way and you asked for a brush-up rather than a rebuild.

**One judgement worth flagging.** I changed the title. That is inside "retarget for a general audience" as
I read it, but it is the most visible single change and the easiest to reverse if you disagree.

---

## Next

Your call. The X-Planes series is at **thirty-seven of seventy-two**, all four passes complete on each,
none published, and **A334, the Boeing X-37, is next** whenever you want it.
