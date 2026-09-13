# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

## Last Updated

**Date**: 2026-09-12
**Task**: **A357, X-Planes: Generation Orbit X-60, publication review. The fourth and last of
four.** Committed and **PUSHED**. **Not published**, and publication of the series still not
authorised. **Sixty-one of seventy-two drafted, eleven remain.**

---

## The Citation Budget Was a Misdiagnosis and It Cost Three Passes

**THE ARTICLE NOW CITES EVERY ONE OF THE 11,708 RECORDS THE GATE ADMITTED.** For three passes
it cited a sample, under a budget of 4,500 references, then 5,928, then 5,413. **Every figure
behind those budgets was measured and every conclusion drawn from them was wrong.**

The draft pass timed the markdown processor against the reference count and found a cost
rising as the cube of it and then faster. **The timings were real. The variable they were
attributed to was not.** This series writes an inline citation as a link inside a pair of
square brackets, so the processor sees an opening bracket, tries to parse a link whose text is
itself a link, fails, and backtracks, once per citation on the page.

**Escaping the outer pair turned 226.02 seconds into 0.70, a factor of 323, with output
identical to the byte.** Two controls separate the explanations. Breaking the long lines so
each citation sits on its own line, brackets left alone, took 196.49 seconds, a thirteen
percent gain, which rules out line length. Removing the brackets entirely took 0.63, matching
the escaped form, which isolates the brackets as the whole of it.

**THE EVIDENCE WAS IN THE REPOSITORY THROUGHOUT.** A published post carries 13,803 reference
definitions and 27,584 citations, more than twice what this article carried under its budget,
and the whole 301-post corpus builds in 12.8 seconds. **That post writes its references one to
a list item rather than inline**, so it never pays the backtracking.

**A model fitted to one article's own numbers agreed with itself and never looked at the
corpus it lives in.** That is the defect underneath all three budgets and it is worth more
than any of them. **The earlier passes also measured the wrong build**, timing a 96-page stub
rather than the deploy, which is what made the corpus comparison invisible.

**The whole corpus with this article published now builds in 18.5 seconds against 12.8 without
it.** Publishing it costs the deploy about six seconds while carrying twice the references it
had this morning.

## Six Claims Withdrawn, and the List Is in the Article

**A NUMERIC VERIFIER CANNOT CATCH ANY OF THESE, BECAUSE NOT ONE CONTAINS A NUMBER.**

The draft said **every article in this series asks what binding unknown its aeroplane existed
to resolve**, which is false of the designation anomalies, where there is no aeroplane. It
called the dynamic pressure identity **the cleanest result in the subject**, a ranking with
nothing behind it. It said the corridor sits **above every air-breathing aeroplane**, and the
two densest cells of its own table are below the sustained altitude record of the fastest one.
It called unit Reynolds number **the quantity a ground facility most often gets wrong**, a
ranking no source read here supports. It credited the engine's maker with being **the first
American company to fire an oxygen-rich staged combustion engine**, which appears in secondary
reporting and **in none of the documents read for this article**. And it said federal law
asked **the only question about this vehicle with a numerical answer**, which every computed
figure in the preceding sections contradicts.

**The guard is a list of withdrawn formulations that must not reappear**, which is a
regression test rather than a test of truth, and it excludes the paragraph that names them,
because this series names a retracted claim rather than deleting it. **Three injections
reinstate three of them and all three are caught.**

## Four Acronyms and a Probe Gap

**AFRL appeared first inside a block quote and was spelled out sixty thousand characters
later.** MDS and DAFI were never spelled out at all. All three now precede their acronym.

**AND THE PROBE HAD NOT SEEN TWO CONCLUSIONS.** The equation pass introduced the vacuum
instantaneous impact point and the inlet capture relation, and the probe was written before
them, which is A356's defect exactly. Both are added, and the probe now carries **16
conclusions with none uncovered**.

## One Conclusion Is Not Supported by This Article's Own Survey

**THE STATUTORY SUBORBITAL TEST RESTS ON TWO-BODY ORBITAL MECHANICS AND THE POOL HOLDS 4
RECORDS ON IT.** That is a decision rather than an oversight, because `orbit` is the worst
homonym in the vehicle's own name and admitting astrodynamics would have brought the whole of
spaceflight into a pool about endoatmospheric flight. **The conclusion is carried by the
textbooks and the article says so**, rather than leaving a reader to infer from a citation
count that the question is unstudied. **A gate that excludes a subject has not measured it**,
which is the same distinction as a dead link and a refused one.

## Diction, Structure and the Rest of the Checklist

**Five content words sit above five per thousand and all five are subject vocabulary**, being
vehicle, flight, Mach, pressure and number, the last of which is Mach number eighteen times
and Reynolds number eight. None is filler.

**Cluster order holds**, with the two residual clusters at positions thirteen and fourteen of
sixteen and the specific clusters before the general ones they are special cases of.
**Structural conformance holds**, with the genre's twelve sections in order and three
article-specific sections interleaved.

## The Injection Suite, and the Same Lesson a Fifth Time

**98 OF 100 ON THE FULL RUN.** Both misses were the build exponents, checked by presence
rather than anchored. **`2.18` occurs five times in this article, four of them inside
digital object identifiers**, so a presence check on it passes while the equation says
something else. That is A355's lesson met for the third time in this one article.

**Repaired and re-checked individually, those two and a third related case are all caught.**
The full hundred were not re-run after the repair, and this report says so rather than
claiming a round number it did not measure.

**THIS PASS WROTE ITS CHECKS BEFORE RUNNING THE SUITE**, which is the only change of habit the
three previous findings actually asked for, and it is why the publication review's own
fourteen figures were caught by construction rather than by the suite.

## Verification

**Verifier 0 errors and 0 warnings. Tests 112 of 112. Lint 0 defects and 1 convention
finding**, the intended multi-line equation form.

**The article verifier runs 276 checks and passes all of them.** The symbol scanner reports
all 121 declared symbols used and every symbol used declared. **Identifier verification passed
on content**, with twelve hand-written addresses checked against a phrase each must contain,
six quoted documents checked against the copies they were quoted from, the live statute
checked against the saved copy, **every hand-written address swept with 58 reachable, 3
refused by hosts known to refuse automated fetches and 0 dead**, 23 of 24 sampled report
primaries resolving, and a fabricated identifier resolving to nothing.

**The production build is now the real one.** The whole corpus with this article published
builds in 18.5 seconds against checksum-matched bytes. **The rendered audit reports no
findings across 539 pages.** Source and rendered display-equation counts agree at **82**, with
zero raw dollar pairs, zero unresolved reference brackets and zero unrendered Liquid. The page
is 2,012,081 bytes and carries 23,031 links.

**FINAL STATE. 24,065 lines, 82 display equations, 121 declared symbols, 11,379 reference
definitions, 135,012 words**, research 11,248, report primaries 1,846 at 16.4 percent, six
sweeps retrieving 45,900 records of which 34,673 distinct, **every one of the 11,708 gated
records cited**.

**The report-primary count is unchanged at 1,846 and the fraction fell from 34.9 percent to
16.4**, because the survey grew from 5,282 records to 11,248. **That is the trap the genre
note names**, and reporting only the fraction would describe a pass that doubled the
literature as a regression.

## What Remains

**A357 is complete at all four passes.** The next new article is **A358, the X-61**, editorial
date 2025-12-06, series index 62. **Eleven articles remain**, ending at editorial date
2025-12-16.

**THE CITATION FORMAT FINDING APPLIES TO THE WHOLE SERIES AND IS NOT ACTED ON HERE.** Several
sibling drafts carry thousands of inline citations in the unescaped form, one of them with
4,544 on a single line, and each is paying the same cost. **That is a change to finished
drafts rather than to this article**, so it is recorded for the pilot rather than done.

**Two repairs are still awaiting a pilot decision.** A350 carries a duplicated
`## The Contemporary Literature` heading at lines 412 and 414, and A324 carries a malformed
`book_jenkins` label over a correct key.

**And the fourth-article format decision carries forward.** A352 through A355 present no
per-cluster record count in a shape the corpus check can read.

**Nothing is published and publication of the series has never been authorised.**
