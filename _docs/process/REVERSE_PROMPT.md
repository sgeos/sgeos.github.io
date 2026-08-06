# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-05
**Task**: A305 primary-reference review, the third pass. Committed. Not pushed. Not published. All
nine articles remain in `_drafts/`.

---

## The Baseline Was Already Above Band, So the Deficit Was Elsewhere

Primary technical documents measured **155 of 359 external references, or 43.2 percent**, before this
pass. The series has settled around 30 to 40 percent, and A298 reached 52.1 percent only after its own
primary review. So the count was not the problem.

The problem was coverage. Two specific gaps. Several claims rested on secondary compilations where a
period document exists, and **every relation the equation pass added last week had arrived without its
primary method paper**.

61 primary documents added across 21 edits. Primary sources are now **216 of 420 external, or 51.4
percent**, and references went from 370 to 431.

---

## The Finding That Changes the Article Rather Than Decorating It

The draft said the early Air Force record sat in the defence technical archive, "much of which is not
publicly indexed". **That was wrong, and I had not tested it.**

Reports held by the Defense Technical Information Center are registered with Crossref under a single
publisher prefix. They resolve by digital object identifier like any journal article and verify the
same way. A prefix-restricted search returned **125 records for this subject, 64 of them predating
1975**.

This matters beyond convenience. The article's Source Base section argued from a sweep of 569 NASA
records, which returned 41 published in the 1950s against 161 in the 1960s, that the X-8 era is poorly
documented. **On that archive alone the conclusion is reasonable and it is wrong.** The material the
aerospace archive lacks for 1946 to 1958 is largely in the defence archive; reaching it needs a
different query rather than a different expectation. The section is rewritten around that.

The single best result is **[Walker 1954], the research and development report on the Navy
Aerobee-Hi**, which is the closest thing in the accessible record to a programme document for this
family and which the draft had implied did not exist in reachable form.

---

## The Equation Pass Created Its Own Reference Debt

Every relation added last week now carries the paper that established it. **[Seddon 1953]** for the
two-frequency propagation experiment, which is the primary source for the whole electron-density
derivation rather than the Aerobee papers that applied it. **[Chapman 1931]**, both parts, for the
optical-depth treatment, the unit-optical-depth level, and the slant-path function the article uses
throughout. **[Jones et al 1951]** and **[Hedin and Nier 1965]** for diffusive separation and the
turbopause. **[Eggers and Wong 1961]** for the ballistic descent. **[Platus 1967]** and **[Wilke
1967]** for roll resonance and for nutation divergence at atmosphere exit specifically. **[Armendariz
et al 1963]** and **[Rachele and Armendariz 1967]** for the wind variability that bounds how well any
weighting scheme can work. **[Walters 1967]** for the numerical-integration question the Comparison
section raises.

**And the regenerative-cooling failure now has its own primary document.** The equation pass computed
a 9.3 megawatt per square metre throat heat flux to explain burnouts the article sourced only to
Aerojet's later corporate recollection. [Bushnell and Busse 1966] report localised overheating in
Aerobee regeneratively cooled thrust chambers directly, which is a considerably better authority than
a company history.

---

## An Invariant Earned Its Keep

Two display-string collisions arrived with the additions, being the two parts of Chapman 1931 and two
unrelated Wang et al 2021 papers. **The link-text invariant adopted during the draft pass caught both
automatically.** That is the first time an invariant rather than a read has caught this class of
defect, and it is worth noting because reading caught the previous four.

Reading still found two things no check flagged. The turbopause paragraph listed later composition
measurements ahead of the measurement it calls the first of them, and The Source Base contradicted
itself by keeping the draft's claim that the record is thin before 1959 immediately beside the new
finding that it is not. Both rewritten.

---

## Verification

431 references with zero undefined, zero orphaned, and zero duplicate URLs. All 179 fixed identifiers
at 200. **All 199 DOIs Crossref-resolved on title at the 0.85 threshold with zero flagged.** All 89
worked numerical values still reproducing. `_verify.py` at the 0-error 21-warning corpus baseline.
Zero style violations, zero doubled words. Isolated build succeeding with 200 rendered display blocks
and Part 9 navigation.

---

## State and Densities

2136 lines, 200 display equations, 431 references, 19,990 words.

**References at 431 exceed the 380 ceiling by 51**, joining lines and equations over band. All three
overages are deliberate under the directive stating no length and no reference limit, and all three
are reported rather than trimmed.

Contemporary references are unchanged in absolute count at **112**. Their share of dated references
fell from 36.6 to 30.5 percent, and the fall is entirely denominator growth from the primary
additions, which is why the count rather than the percentage is the measure the series tracks.
References dated 1965 or earlier rose to 137, or 37.3 percent of dated, which is the shape you would
expect from a pass that added period documents.

**Categories remain undecided** at `aerospace history engineering`, nine articles deep and raised
eight times.

The remaining pass is the publication review. A305 is otherwise complete.
