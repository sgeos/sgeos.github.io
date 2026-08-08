# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A311 primary-reference review, the third of four passes. **Committed, not pushed.** All
fifteen articles in the series remain in `_drafts/`.

---

## Two Documents the Article Should Have Had and Did Not

**The X-14A's own variable-stability system has a paper, and the article was not citing it.**
[Hegarty et al 1965] describes a system for varying the stability and control of a deflected-jet
fixed-wing vertical take-off aircraft. That is the X-14A and no other machine, but the title names
the configuration rather than the aircraft, which is why it was missed by a search keyed to the
designation. **It is the primary description of the apparatus that produced every number in the
article**, and it is now cited where the variable-stability system is introduced.

**The MIL-F-83300 lineage now has a primary source instead of an assertion.** The What the Data
Changed section claimed the specification descends from the flight and simulator work of the
preceding decade. [Key 1971] is an account of how MIL-F-83300 was generated, published the year after
adoption. The conventional-aircraft counterpart is documented the same way in [Chalk et al 1969] for
MIL-F-8785B, and the specification's subsequent life runs through Vinje and Miller, Hutchings,
Anderson, and Goldstein. **The claim that this aircraft's output became a contractual obligation is
now sourced rather than inferred.**

---

## Corroboration for Two Things the Article Derived on Its Own

**The scaling argument has a second contemporary paper.** The article derives that control power at
fixed bleed fraction falls inversely with span, and cited Johnston and Friend 1965 as evidence the
field had noticed. [Johnston et al 1965] reports a study of size effects on vertical take-off
handling-qualities criteria in the same year. **Two papers on the size dependence within three years
of the first results is not a coincidence**, and it upgrades the corroboration from suggestive to
firm.

**The two-pilots objection was raised contemporaneously and I did not know it.** The article criticises
a criterion derived from two test pilots' opinions. [Kidd and Bull 1963] examines how handling
qualities requirements are influenced by pilot evaluation time and sample size, **published two years
before the lateral control experiments it applies to**. The field knew the objection and ran the
experiment anyway, which is a more interesting fact than the objection itself and is now recorded as
such.

**The bandwidth successor is now sourced.** The claim that the field changed the variable rather than
the number rests on the Pausder and Blanken bandwidth and time-delay experiments of 1992 to 1994,
which are the X-14A's own procedure with the independent variables replaced.

---

## Composition

**267 references, 244 of them research, up from 95 and 72 across 26 edits.**

**Primary sources are 234 of 244 dated, or 95.9 percent**, which is the highest share the series has
carried. That is not a stylistic choice. The X-14's subject is almost entirely a 1955 to 1985
technical-report literature, and the modern material belongs to the pass that follows. Composition by
archive is NTRS 105, period 84, DTIC 45, modern 10.

Citation density is 16.17 per thousand body words, at the top of the 12.82 to 16.58 range A310 held.
The densest paragraph carries nine citations in fifty-five words and is a conference-series listing,
which is the acceptable form of that shape.

---

## Verification

**267 reference definitions, 253 external URLs, zero duplicates, zero orphans.** The URL-stability
guard fired no drift when the reference section was regenerated, and the link-text invariant reported
no mismatches, so every citation text equals its master-table display exactly.

`_verify.py` at the 0-error 21-warning corpus baseline from the repository root. Zero contractions,
em-dashes, en-dashes, prose colons, prose semicolons, prose parentheticals, doubled words, duplicate
headings, unbalanced emphasis markers, lone dollar-delimited lines, or adjacent display-math seams.
Isolated build succeeding with **103 rendered display blocks matching source exactly**, Part 15
navigation, no unresolved reference links and no surviving Liquid tags.

**Three repeated-phrasing collisions introduced by the insertions were caught and varied**, two of
them by a mechanical repeated-phrase scan and one by reading the result of the fix.

---

## State

**1300 lines, 103 display equations, 267 references, 17,821 body words.**

**All three densities are inside band and nothing has been trimmed at any point.** Lines landed
exactly on the 1300 floor. That makes A311 the sixth article in the series to finish a pass with
nothing trimmed, after A306 through A310.

**Contemporary references are 10 of 244 dated, or 4.1 percent.** The absolute count is unchanged since
the draft and the percentage fell only because this pass grew the denominator by 172. Against the 101
to 189 absolute count the series has held since A301, **this is the largest contemporary gap any
article has carried into a publication review**, larger than A309's, and closing it is the next pass's
principal task.

**Committed, not pushed.** Nothing in this series is published. The publication-order dependency is
fifteen deep. **Categories remain undecided** at `aerospace history engineering`, fifteen articles deep
and raised nineteen times.
