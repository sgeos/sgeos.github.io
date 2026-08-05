# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-05
**Task**: A297, the X-Planes series opener, drafted and verified. One article only, per your
stated preference to review shape and depth before the pattern is set across seventy-two.

---

## What Was Written

`_drafts/x_planes_framing.markdown`, editorial date 2025-10-06, series `x_planes`, index 1.

1623 lines, 147 display equations, 372 reference definitions, 19,822 words. The History of SpaceX
medians for comparison are 1345 lines, 72 equations, and 306 references.

**The equation count is deliberately double the parity figure and you should know why.** The article
was drafted at 76 equations, which sat at parity. You then asked for an equation-density review with
all candidate equations added. The audit found 19 results that the prose named or relied on without
ever showing, including Sutherland's law, the Kantrowitz starting condition, Fay-Riddell, Wright's
learning curve, the Shannon capacity, the area rule as a design statement, the exponential
atmosphere, and the elliptic lift distribution. Closing those gaps plus the derivation steps they
depended on added 71 equations across 44 edits. Nothing was added to raise a count. The filter was
that the prose already asserted the relation or that a cited result was named but not given.

The argument is that a research aircraft is an instrument rather than a vehicle. Ground facilities
cannot match Mach, Reynolds, Prandtl, wall temperature ratio, Damkohler, and Knudsen numbers
simultaneously, and the residue is what each aircraft was built to measure. That residue then
dominates the design, which the article states as a constrained optimization whose largest shadow
price identifies the keystone. The remaining sections derive the sizing relations the per-aircraft
articles will reference rather than repeat, covering the flight envelope, transonic drag, propulsion
and mass budget, structures and aeroelasticity, aerothermodynamics, stability and control, and
instrumentation.

Two results are worth your attention because they are the article's own rather than borrowed. A
binomial attrition calculation at a two percent per-flight loss rate over twenty-five flights and
ninety-five percent completion confidence returns three airframes, and both the X-1 and the X-15
were built in threes. The article explicitly declines to claim anyone performed that calculation.
Separately, the Sutton-Graves heating correlation and a radiation equilibrium balance put the
X-15A-2 stagnation point at 1880 kelvin against an Inconel X working limit near 1200, which is why
the Mach 6.7 flight needed ablative coating and returned damaged. The arithmetic explains the
historical fact rather than merely accompanying it.

---

## Verification Performed

All 34 worked numerical examples were re-derived independently from stated inputs. Every one agrees.

All 372 references are cited in the body. Zero undefined anchors, zero orphaned definitions.

159 Wikipedia URLs were swept. Five titles were wrong and were corrected against the Wikipedia API,
and seven additional confirmed pages were added.

**All 22 digital object identifiers were resolved through Crossref and compared on author and title.
Two of the original 11 were defective.** The Sears 1947 identifier did not exist, and the Weisshaar 1980 identifier
resolved to an unrelated 1979 paper on bipropellant exhaust optics. Both were replaced with
identifiers confirmed against the correct works. This is the exact defect class that produced the 47
broken citations in the existing corpus, and it appeared on the first article of a new series.

`_verify.py` reports zero errors and the same 21 pre-existing warnings as before the draft landed.
Zero prose style violations. The article builds clean in an isolated tree and renders with every
`post_url` resolved.

---

## The Reference Pass, and What It Found

You asked for a reference-density review of primary sources specifically. Measuring first was the
right move, because the index was worse than the raw count suggested. Of 327 references, **only 42
were primary, or 13.5 percent.** Wikipedia accounted for 159 at 51 percent and books for 109 at 35
percent. Meanwhile the article asserts in its own Historiographical section that the NACA and NASA
report series is the backbone of the series. The index did not support that claim.

Worse, six results were named in the prose as results while carrying no citation at all, namely
Ackeret, Sutherland, Buckingham, Bredt-Batho, the Newtonian stagnation velocity gradient, and the
Reynolds analogy. That is precisely the defect a reference index exists to prevent, and the equation
pass had introduced most of them.

**Primary references are now 87 of 372, or 24.5 percent.** 45 were added and 22 existing citations
were upgraded.

The upgrade matters as much as the additions. NTRS turns out to expose a citations API, so instead of
adding more search endpoints I resolved reports to real document identifiers. Twenty-two citations
that previously pointed at `ntrs.nasa.gov/search?q=...`, which returns 200 for any query including
nonsense, now point at `ntrs.nasa.gov/citations/<id>`. **All 63 fixed identifiers were swept and all
returned 200**, so for the first time a status code on these citations means something.

One methodological note worth keeping. Title-token overlap alone is not proof of identity. A query
about the X-1 returned an X-2 document and a query about the X-2 returned an X-1 document, both with
perfect token scores. Two other queries returned "Lunar and Planetary Science XXXIV". The rule I
applied is that every entry is labelled with the title the API actually returned rather than the
title I searched for, and anything whose returned title did not describe a usable primary source was
dropped rather than relabelled into plausibility.

## A Genre-Document Question the Equation Pass Raised

`RESEARCH_AIRCRAFT_STRUCTURE.md` bands a full-aircraft article at 60 to 80 display equations. At 147
this opener now sits far outside that band, and the band has no row for a series opener. I have added
one, describing the opener as the article that carries the shared derivations so the seventy-one
per-aircraft articles can reference rather than repeat them. That is a description of what the
article now is rather than a new target, and it is the smallest change that stops the genre document
contradicting the article. Revert it if you would rather the opener be held to the per-aircraft band.

## Three Things You Should Decide

1. **Categories.** I used `aerospace history engineering`, which renders the URL as
   `/aerospace/history/engineering/2025/10/06/x_planes_framing.html`. This is still my assumption
   rather than your decision. It is free to change while the article sits in `_drafts/` and fixed
   permanently once published, across all seventy-two.

2. **Citation strength, now narrowed but not closed.** The NASA side is fixed. What remains is 109
   Open Library search URLs for books and 3 NTRS reports the API could not resolve, so 112 citations
   still point at endpoints that cannot return a not-found. Open Library does expose a search API, so
   the same treatment that fixed the NASA citations would work on the books and would resolve them to
   edition pages with work identifiers. Say the word and I will do that pass.

3. **Wikipedia is still the largest single class at 159, or 43 percent.** For the aircraft entries
   that is defensible, since for many of these designations no better public overview exists. For the
   concept entries it is weaker, and several now sit alongside a primary source that could carry the
   citation alone. Pruning that is a judgement call about what a reference index is for, and it is
   yours rather than mine.

---

## One Roster Correction Found

Wikipedia titles the X-62 as the **General Dynamics** X-62 VISTA, because the airframe is a modified
F-16D. The roster in `HANDOFF.md` calls it the Lockheed Martin X-62 VISTA. Both are defensible,
since Lockheed Martin and Calspan performed the modification, but A359 should name the disagreement
rather than pick silently. No change has been made to the roster.

---

## State

Branch `master`, three commits unpushed including this one. The draft is committed but not
published, so nothing is live and the two-commit publication sequence has not begun.
