# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

## Last Updated

**Date**: 2026-09-09
**Task**: **A353, X-Planes: Lockheed Martin X-56, primary-reference review. The third of
four passes.** Committed and **NOT PUSHED**, which is the rhythm. **Not published**, and
publication of the series still not authorised. **Fifty-seven of seventy-two drafted.**

---

## Report Primaries 275 at 7.1 Percent to 496 at 10.3, and Both Numbers Moved

**References 3,971 to 4,905, research 3,862 to 4,796, lines 8,554 to 10,442, words 51,338
to 61,958.** Display equations unchanged at 36, because this pass adds sources rather than
relations.

---

## The Bibliography Found What the Sweep Missed, Which Is the Opposite of Last Article

**A352 transcribed its programme's reference list and found twenty-six of thirty-two
already in the pool**, and concluded that a bibliography's value is not that it finds what
a sweep missed but that it says which records the argument needs.

**A353 ran the same exercise and got the opposite answer.** The flight test report's
seventeen references, plus the ancestor's mishap reporting and the theory the article
computes with, gave twenty-three documents found by hand. **Only six were in the first
sweep.**

**AND THE DIAGNOSIS IS IN THE QUERIES.** The draft sweep named this aeroplane once, in a
query reading `X-56 multi utility technology testbed flutter`. **That query returned
exactly 200 records, which is the row cap**, and the ranking was carried by the words that
are not the aeroplane's name. It brought back a millimetre-wave seeker testbed, a
Testbed-12 tile retrieval service and four separate tiltrotor whirl-flutter testbeds.
**Six records in a 6,477-record harvest had the X-56 in their title, and sixteen of the
seventeen documents the report cites were never retrieved at all.**

**A bibliographic query mixes its terms, so a distinctive designation put beside five
generic words is diluted by them.** The more distinctive the designation, the more of the
ranking is spent on its neighbours. **This is a general lesson for the fifteen articles
remaining**, because every one of them is named after a vehicle.

**The fix was a second sweep querying the designation alone, the mechanism alone, and the
names of the people who publish under them.** It retrieved 3,919 records, doubled the
X-56 titled records from six to twelve, and took the hand-found overlap from six of
twenty-three to fifteen. **The eight still absent were curated by hand**, among them
Theodorsen's 1935 report, the Helios mishap findings by Noll and others, and the deadband
paper whose title is itself the finding.

**Every curated identifier was requested individually and its returned metadata compared
against the title this article gives it**, alongside a deliberately absent digital object
identifier and a deliberately absent report number as controls. **Both controls failed
correctly**, because a checker that says yes to everything says nothing.

---

## A Tag Count Is a Count of First Reasons, Not of Releasable Records

**The four opened families sum to 153 in the histogram and opening them returns 152.**

The difference is one record and it generalises. A study of unsteady pressure on turbine
rotor blades is caught by the wind energy family and by the turbomachinery family, and
opening the first leaves the second holding it. **The store defends some records twice.**

**The article now measures the release as a set difference rather than summing the
histogram**, and says so, because the histogram overstates what opening a family returns.
**This is the same property a test pinned in the previous commit** for the binary liquid
records, now measured in the pool rather than asserted about two titles.

---

## Two Numbers Were Emitted From the Wrong File

**THE SOURCE BASE REPORTED THE FIRST SWEEP'S RETRIEVAL AGAINST THE MERGED POOL.** The
statistics emitter read `raw.json` alone, so after the primary sweep the article stated
6,477 records retrieved when 10,396 had been, and computed the store's cost over a
denominator a third too small. **A number emitted from the wrong file is the same defect as
a number typed from a console.**

**AND THE ARTICLE CLAIMED FOUR SWEEPS WHEN IT HAD RUN ONE.** The draft pass's source base
carried the phrase `four sweeps` straight from A352, where it was true. **A phrase inherited
from a sibling article is an unmeasured claim wearing a measured one's clothes.** The number
of sweeps is now counted from the artefacts, and the verifier asserts both that the correct
count appears and that none of the wrong ones do.

**THE STORE HAS TWO DROP COUNTS AND THE ARTICLE WAS CONFLATING THEM.** Armed exactly as
written it removes 673 of 8,935 distinct records, being 7.5 percent. With the four families
opened it removes 521, being 5.8 percent. **The article was quoting one count against the
other's fraction**, and now states both with their own denominators.

---

## Verification

**Verifier clean at 0 errors and 0 warnings. Tests 107 of 107. Lint 0 findings. The symbol
scanner reports all 51 declared symbols used and every symbol used declared.**

**Seventeen defects were injected one at a time and all seventeen caught**, being a
contraction, a prose colon, a semicolon, an em dash, a parenthetical, capitals used for
emphasis, a wrong register count, a wrong stiffness factor, a wrong damping inversion, a
wrong primary count, a wrong primary fraction, a wrong retrieval total, a wrong armed store
count, a wrong released count, a wrong bibliography overlap, a wrong sweep count and a year
past the dateline.

**Every survey statistic the article states is recomputed from the reference data and the
sweep artefacts rather than matched against a remembered string.**

**FINAL STATE. 10,442 lines, 36 display equations, 51 declared symbols, 4,905 reference
definitions, 61,958 words**, research 4,796, report primaries 496 at 10.3 percent, two
sweeps retrieving 10,396 records of which 8,935 distinct, gate 4,902, store residual 5.8
percent. **All 4,905 definitions are cited, none orphaned and none undefined.**

**The stub-isolated production build succeeded in 660 seconds with no Liquid error, against
the exact bytes committed**, the checksum matched against the stub copy before the build and
against both afterwards, **which also proves the seventeen injections did not contaminate
the built bytes**. **The rendered audit reports no findings across 92 pages.** Source and
rendered display-equation counts agree at **36**, with zero raw dollar pairs leaking, zero
unresolved reference brackets, zero unexpanded slots and zero unrendered Liquid. The page is
903,112 bytes.

---

## What Is Not Done

**The publication review has not run.** It is the pass that reads the opening against the
conclusion, which has found a defect in every article since A340, and the pass that probes
each conclusion against the pool.

**Three disagreements remain recorded and unresolved**, being the register's P-240 against
the report's P400, three maximum weights across three documents of the same programme, and
the X-56B's questioned 2019 date against 2021 flight dates in secondary sources.

**The wing area and the modal frequencies are still not published.** The aspect ratio of
approximately fourteen comes from secondary sources and every quantity resting on it is
flagged as approximate.
