# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

## Last Updated

**Date**: 2026-09-07
**Task**: **A351, X-Planes: Gulfstream X-54, primary-reference review. The third of four.**
Committed and **not pushed**, which is what this pass asks for. **Not published**, and publication of
the series still not authorised. **Fifty-five of seventy-two drafted.**

**Report primaries 318 to 380, being 10.4 percent to 12.1. Curated sources forty-two to eighty-four.**

---

## The Largest Gain Came From Bibliographies, Not From Sweeping

**Sixteen of the article's thirty-one display equations carried no citation at all**, which the pass
began by measuring rather than assuming. The equation review had made a dozen subjects load-bearing
that the draft pass had correctly treated as background, and **the four-pass rhythm has no step that
re-asks whether an absent subject has become load-bearing.** This audit is that step.

**Three primary documents carry bibliographies naming exactly what those equations needed.** The Quiet
Spike flight test report, the shaped-boom demonstration paper and the Mach cutoff investigation each
list the work they were built on, and this article had been using their ACCOUNTS of those documents
rather than the documents. **This is the A350 finding, one article later, and it doubled the curated
set.**

- **The Gulfstream design chain from 2003 to 2009.** The company's supersonic vehicle studies, its
  non-axisymmetric shaping method, Henne's published case for the small supersonic civil aircraft, the
  extendable-spike patent of March 2004, the prototype design and validation, the flight results, the
  aerodynamic effect of a thirty-foot boom on the host, and the propagation work it went on publishing
  after the aeroplane it wanted was not built.
- **The classical literature from 1956 to 1979.** Whitham on weak shock propagation, Jones on lower
  bounds, Hayes with the stratified-atmosphere propagation code, McLean on nonasymptotic effects,
  Carlson on transport design, Darden in real rather than isothermal atmospheres, and the wind-tunnel
  study that validated the minimisation concept before anybody flew it.
- **The human-response experiments the loudness procedure was calibrated against**, including booms of
  different shapes and rise times, booms against aircraft flyovers, and simulated booms in people's
  own homes.
- **The standard atmosphere the article computes in**, which is the A341 lesson document.

---

## And a Finding That Changed the Shape of the Story

**Mach cutoff was measured in flight and published in 1971.** The article had it as the modern
alternative, demonstrated by the space agency in 2012. **It is two years older than the prohibition it
now helps displace and fifty-four years older than the order to repeal it.**

**That came out of a bibliography and not out of a sweep.** It turns the closing argument from a new
technique overtaking an old aeroplane into an old technique outlasting one.

---

## The Equation Pass Had Shipped an Anachronism

**A regulatory limit of 0.11 pounds per square foot went into the article dated November 2025.** It is
the interim limit in a notice of proposed rulemaking published in **July 2026**, seven months after
the editorial date, and the prose promised it would `later appear` in an article that stops before it
does.

**An anachronism hides in a number as easily as in a sponsor's name**, which is the A350 lesson met
from a new direction. The passage is re-anchored on Concorde, which boomed throughout the period the
article covers, at roughly two pounds per square foot, 133.6 decibels peak and one part in 1,060 of
ambient. **No pressure target for a shaped signature is quoted, because a low-boom goal is stated in
perceived level and the two are not interconvertible.**

**`verify_numbers.py` now refuses any year in the prose after the dateline**, and it was proved
non-vacuous by injecting one.

---

## Instruments

**A doubled backslash is invisible to a macro allowlist.** `\\times` contains `\times`, so the check
added last pass passed it while MathJax would have rendered a line break followed by the word. **It
came out of an emitter whose escaping had been through a heredoc twice.** The verifier now refuses a
doubled backslash in math, proved by injection.

**A hard-coded word list in the verifier reported the article as wrong when the checker was stale.**
The store gained two tag families this pass, so the spelled-out count moved from nine to eleven and
the check still expected nine. **A spelled-out claim needs a spelled-out check computed from the same
data the prose is.**

**One anchor pointed at a paper whose title was not the label citing it**, and two anchors shared one
URL. The label checker found the first and the reference integrity check found the second, and they
were the same defect seen from two directions.

**One identifier could not be verified and was dropped rather than cited.** `Sonic Boom: Six Decades
of Research` is the standard monograph and the NTRS API returns 404 for it on four consecutive
requests while the citations page returns 200. **That 200 is the single-page-app shell.** An HTTP 200
is not verification.

---

## A New Contaminant Family, Earned by This Subject

**`community response` is an ecological term as well as an acoustic one.** `Plant Community Response
in Small Plots One Year after Treatment with Triclopyr and Endothall` reached the kept set of a survey
whose second-largest cluster is community response to noise. **The pattern is anchored on the ORGANISM
word rather than on `community`, which must survive.**

**Coupled atmosphere-ocean modelling** was recorded at the same time, and it also removed three North
Pacific Acoustic Laboratory studies of ocean SHADOW ZONE arrivals that had entered through the
atmospheric shadow-zone anchor. **Store 132 patterns, seventeen tags.**

**Every sweep is re-gated whenever the store changes.** A pattern is global, so re-gating only the
sweep that motivated it would leave the corpus as the union of two instruments. `merge_sweeps.py`
applies one gate, one store and one tag set to all three sweeps, and the store's four measured numbers
were re-taken with the current instrument rather than carried forward.

---

## Counts

| Quantity | Draft | Equations | Primaries |
|---|---|---|---|
| Lines | 6,745 | 6,891 | 7,057 |
| Words | 39,473 | 41,392 | 44,159 |
| Display equations | 11 | 31 | 31 |
| Reference definitions | 3,159 | 3,159 | 3,231 |
| Research records | 3,072 | 3,072 | 3,143 |
| Report primaries | 318 at 10.4 percent | unchanged | **380 at 12.1 percent** |
| Curated sources | 42 | 42 | **84** |
| Retrieved across sweeps | 8,289 in two | unchanged | **9,521 in three** |
| Prose citation labels checked | 41 | 48 | **105** |

**The measure misses four of the documents that decide the argument** — a designation registry, an
executive order, a part of the code of federal regulations and a patent — and the article reports the
count of named primary documents beside the fraction rather than instead of it.

---

## Open Questions for the Pilot

**A324's `book_jenkins` label remains the one live repair**, unchanged.

**The OpenLibrary work pages returning Internal Error to a reader** is also unchanged.

**Nothing is pushed.** The next prompt in the rhythm is the publication review, which is the one that
asks for a push.
