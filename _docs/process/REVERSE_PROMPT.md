# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-05
**Task**: A304 primary-reference review. Committed and **not pushed**. **No article in this series is
published.**

**253 to 313 references, 49 to 109 primary technical documents, 1157 to 1289 lines.**

---

## The Deficit Was the Largest in the Series

A304 came into this pass at **49 primary documents and 19.4 percent of all references**, against 30.1
percent for A301 and 39 percent for A302 and A303. That is roughly half the series norm and it is the
worst starting position any article has had.

Two things caused it. **Thirty-one records I had already verified never got cited**, because the draft
pass ran out of places to put them before it ran out of documents. And the harvest itself was barely
tapped, with 337 documents gathered and 70 verified.

Primary documents are now **109, or 34.8 percent**, and references dated 1965 or earlier are **51.1
percent** of dated references, second only to A303.

---

## Four Additions Land on the Article's Own Derivations

**[Disher et al 1953] report the free-flight performance of a rocket-boosted, air-launched sixteen-inch
ramjet.** That is the X-7's entire operating concept in miniature, flown two years into the programme,
and it is the closest thing in the open literature to a direct antecedent. The draft had no citation
for the architecture at all.

**[Evans 1951] analyses ramjet performance across Mach 3 to 7**, which is exactly the interval in which
the engine goes from excellent to impossible, and reaches the ceiling this article derives
independently at Mach 6.2. Having derived it, it is worth knowing someone had it in 1951.

**[Flaherty and Stitt 1959] test an isentropic spike inlet designed for Mach 5.** The shock section
gestures at continuous compression as the limiting case of many weak shocks; this is that limit built
as a contoured centrebody and flown.

**[Tower and Gammon 1953] give the analytical relation between equivalence ratio, inlet air
temperature, and combustion pressure** that the fuel-air calculation evaluates numerically.

---

## Two Claims Substantiated Rather Than Repeated

The Comparison With Ground Prediction section asserted that a tunnel model runs an order of magnitude
low in Reynolds number and that this matters. **[Anderson et al 1957] compare a full-scale and a
quarter-scale translating-spike inlet at the same Mach numbers**, which is precisely the experiment
that settles how far a tunnel result can be trusted, and the article now cites the measurement rather
than the reasoning.

The combustion section said boron deposits solid oxide in the nozzle, which is well known and was
standing on secondary accounts. **[Schafer et al 1953] compare theoretical and experimental oxide
coating formation.** The claim is now attributable.

---

## Diction

Citations introduced by the preposition `in` reached **34.2 percent** of body citations after the
pass, because sixty references went in during one sitting with one construction. Nine passages rotated
across `by`, `from`, `through`, and verb forms, bringing it to **22.7 percent**, with `and` at 27.7 and
`by` at 15.1. **That is the best-distributed citation mix of any article in the series so far**, and
it is the third consecutive article where this check has caught the same drift, which suggests the
drift is a property of how I add references in bulk rather than of any particular article.

---

## Verification

313 references with zero undefined, zero orphaned, and zero duplicate URLs. All 185 meaningful-404
URLs at 200. `_verify.py` at the 0-error 21-warning corpus baseline. Zero style violations, zero
doubled words, zero display-math seam defects. Isolated build succeeding with 94 rendered display
blocks and Part 8 navigation.

---

## What Remains

**Lines at 1289 are 11 short of the 1300 floor and I have not padded them.** Eleven lines is exactly
the amount that would be tempting to manufacture, and the publication review will close it with real
material or it will stay 11 short and be reported that way.

Contemporary references are 28.1 percent of dated, just inside the target range, so A304 does not
carry a second deficit into the last pass.

**Publication order dependency is eight deep.** Three commits unpushed. Categories remain
`aerospace history engineering`, eight articles deep.
