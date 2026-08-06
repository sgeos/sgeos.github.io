# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-05
**Task**: A303 publication review, the fourth and final pass. Committed and **pushed**. **Not
published.** All seven articles in the series remain in `_drafts/`.

---

## Contemporary Coverage Was the Job

A 38-query Crossref sweep returned 453 candidates, of which 365 passed a topical screen and **46 were
selected and verified individually on author and title, zero flagged**. Contemporary references went
from 59 to **105**, and from 23.5 to **35.4 percent of dated references**, comparable to A301 at 35.8.

Several land on the article's own coefficients rather than beside them, which is the test I applied.

**The shield derivation assumes a buildup factor of ten and a single-valued neutron removal
cross-section.** Both are still research subjects. [Sun et al 2025] carry Monte Carlo buildup
evaluation to a hundred mean free paths, [Kang and Zu 2026] and [Yang et al 2026] replace the
tabulations with learned models, [Hashim et al 2026] treat the multilayer case the divided shield
requires, and [Soliman 2025] addresses the energy dependence the single value hides. **The article now
says its two assumed coefficients are live subjects rather than settled constants**, which it should
have said before.

Three threads that the draft asserted are now traced. The radiation-hardening practice the programme
invented runs into the modern semiconductor literature. The coated particle is where the fuel-element
problem went, through TRISO performance modelling. And **the mission itself was answered without
nuclear propulsion at all**, by solar-powered high-altitude unmanned aircraft that achieve persistence
by having almost no energy demand rather than by carrying an enormous supply. A programme that spent
a billion dollars removing the fuel constraint was eventually answered by removing the crew and most
of the aircraft.

---

## Four Acronym Defects

The acronym check earned its place this time.

**TSFC appeared inside an equation before it was ever spelled out.** **ASTR was used in the Comparison
section although the abbreviation had never been established**, since the Flight Test Record spelled
out Aircraft Shield Test Reactor without attaching the initials. **ORNL appeared unexpanded in prose.**
And once I fixed the first, the expansion of thrust-specific fuel consumption occurred twice in
consecutive sentences, so that needed cleaning too.

---

## Diction

`programme` measured 5.37 uses per thousand body words and `than` 5.46, both above threshold and both
more generic than the article's subject vocabulary of reactor, shield, and aircraft. Thirteen passages
rotated across effort, project, work, instead of, and restructuring, bringing them to **4.82 and
5.01**.

`rather than` came to 37 uses. Before acting I measured the siblings, and it runs at **4.5 per
thousand in A301 and 3.7 in A302 against 2.9 here**, so the construction is a house norm across the
series and not an A303 defect. I trimmed five anyway and am reporting the measurement rather than
implying I fixed something.

---

## Numerical Sanity

**All 46 worked values re-derived independently from the stated inputs, none disagreeing beyond four
percent.** That includes the full shield chain from fission rate through source strength, unshielded
dose rate, required attenuation, lead and lithium hydride thicknesses, and both mass ratios, plus the
ASTR validation case, the decay heat and melt time, the heat exchanger relations, and the molten salt
pressure ratio.

---

## Verification

404 references with zero undefined, zero orphaned, and zero duplicate URLs. All **248 meaningful-404
URLs at 200 across three archives**. All 101 DOIs Crossref-resolved on author and title. `_verify.py`
at the 0-error 21-warning corpus baseline. Zero contractions, em-dashes, en-dashes, prose colons,
prose semicolons, or prose parentheticals. Zero doubled words, zero display-math seam defects.
Reference bullets and link definitions both sorted. Genre section order conforming. Isolated build
succeeding with 92 rendered display blocks matching 92 source equations and Part 7 navigation.

---

## One Density Outside the Band

**References at 404 exceed the genre ceiling of 380 by 24.** Deliberate, under the standing directive
stating no reference limit and asking for a comprehensive survey of the contemporary literature.
Reported rather than trimmed. Lines at 1487 and equations at 92 are both inside band.

Final shape: 156 primary technical documents at 38.6 percent, **53.9 percent of dated references at
1965 or earlier**, and 105 contemporary at 35.4 percent. That is what a programme whose entire
technical life fit inside fifteen years looks like when it is surveyed honestly.

---

## State

**Pushed.** Nothing in this series is published, and the deploy workflow builds without `--drafts`, so
the push is safe. **The publication-order dependency is seven deep.**

**Categories remain undecided.** `aerospace history engineering`, still my assumption, seven articles
deep. A304 is the Lockheed X-7, a ramjet test vehicle that was launched rather than flown, and the
question there is what changes when the aircraft is expendable.
