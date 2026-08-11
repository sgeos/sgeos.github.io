# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-11
**Task**: A370 primary-reference review. **Committed, not pushed.** **Not published.**

**References 53 to 57 definitions and research citations 31 to 35.** The article moved from 9,812 to
10,250 words, with equations unchanged at 31.

---

## The Article Contradicted Itself and I Nearly Accepted the Contradiction

**The References introduction asserted that all references are primary and that no secondary literature
survey is offered.** The article carries **31 research citations inside a section titled The Contemporary
Literature**, which is a secondary literature survey and is one of its longest sections.

**That introduction was a leftover from a draft written before the survey existed.** I flagged the risk
last pass in the opposite direction, saying a reference review would be a change of character because the
article was all-primary. **It was not all-primary and had not been for some time.** The introduction now
says what is true, which is that every source is primary in the sense of being a specification, an
interface document, reference documentation, **or the original paper that introduced a result the argument
uses**.

---

## Four Primary Sources for Results the Equation Pass Imported

The equation pass added arithmetic that came from somewhere, and **none of it was cited**.

- **Clopper and Pearson 1934** for the exact binomial confidence bound the nine-of-nine argument evaluates.
- **Hanley and Lippman-Hand 1983** for the no-observed-failures case specifically, which is the same
  arithmetic under a clinical heading, and the article says so.
- **Shannon 1948** for the channel-capacity framing, of which the bits form is the elementary case.
- **Cousot and Cousot 1977**, cited **to mark a contrast rather than a precedent**. A sound but incomplete
  rule is the normal condition of static analysis because an exact answer is often uncomputable. **This
  article's imprecision was not forced**, since the property is decidable on straight-line bytecode by
  summing two integers, **which is a worse position than the classical one and an easier one to fix.**

---

## The Citation Audit Produced a Finding the Article Did Not Have

**All 35 identifiers resolve to the work they are cited as, an error rate of zero.**

**Two instruments flagged different records and that is itself the lesson.** The article's original
title-overlap heuristic flagged four. A check comparing author surname and year flagged five. **The union
is eight distinct records and every one was vindicated on individual inspection**, giving four artefact
categories where the article documented two.

| Artefact | Records | What the registry does |
|---|---|---|
| Title split from subtitle | 3 | Stores a short title where the citation carries the full one |
| Wrong registration agency | 1 | LIPIcs deposits with DataCite, so a Crossref lookup finds nothing |
| **Surname particle dropped** | 1 | Stores de Moura as Moura |
| **Registry typo** | 1 | Stores Dyvbig for Dybvig, so the article is right and the registry is wrong |
| **Identifier resolves to a reprint** | 2 | Reynolds 1972 and Strachey and Wadsworth 1974 carry identifiers for their 1998 and 2000 reprints |

**The reprint category is the one worth carrying forward, because it is not instrument error at all.** The
identifier is correct, the work is correct, and the year genuinely differs, because a foundational paper
and its journal reprint are two publications of one text. **A checker comparing years will flag every
reprinted classic in any bibliography**, and a bibliography of foundational work is mostly reprinted
classics. That is a real limitation of the method this series uses, and it now sits in the article.

The DataCite case was confirmed by querying DataCite directly, which returns the cited title, the cited
year and both authors.

---

## Verification

- `python3 tmp/a370/verify.py` **34 of 34**, unchanged, since this pass added no arithmetic.
- `python3 _verify.py` **0 errors, 21 warnings**, the unchanged baseline, from the repository root.
- **57 definitions with zero undefined and zero orphaned**, and the Research block re-sorted by anchor.
- `lint.scan` **clean**, after a reflow verified a fixed point and content-preserving.
- **Prose scan clean** of em dashes, en dashes, contractions, prose colons, prose semicolons, prose
  parentheses and italics.
- **Isolated build exit 0**, with **31 open and 31 close display-math delimiters**.

---

## Next

Your call. **Three of the four passes have now been applied to A370**, being the standards brush-up, the
equation-density review and this one. **A publication review has not**, and for this article that would
mean a contemporary-literature sweep, a full citation sweep, and a final structural read.

The X-Planes series is unchanged at **thirty-seven of seventy-two**, none published, with **A334, the
Boeing X-37, next** whenever you want it.
