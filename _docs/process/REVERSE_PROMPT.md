# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A311 publication review, the fourth and final pass. Committed and **pushed**. **Not
published.** All fifteen articles in the series remain in `_drafts/`.

---

## Running the Article's Relations on a Vehicle With No Bleed Produced the Strongest Result in It

This is worth putting first because it was not the expected answer and it is not a survey finding.

Deriving control power for a multirotor from first principles, where attitude moments come from
differential rotor thrust rather than from compressor bleed, gives

**CP = c_g · min(r−1, 1) · g / (2 κ² b)**

which is **inversely proportional to span. The same law, and the same exponent, that this article
derived for bleed-fed reaction nozzles, by a mechanism that shares no hardware with it.**

The inverse-span dependence is therefore not a property of reaction controls at all. **It is a
property of making moments with forces at the extremities of a vehicle whose thrust scales with its
weight**, and it survives complete replacement of the propulsion system.

---

## The Cost Changed Character, Not Merely Magnitude

The X-14A's bleed was a standing tax of 7.41 percent, supplied whether or not the pilot was commanding
anything. A multirotor's differential is zero-sum, since one rotor rises exactly as much as another
falls, so **the mean cost of attitude control is zero**. What the vehicle pays instead is thrust
headroom it needs anyway for climb and gusts, so the attitude requirement is frequently not the
binding one.

**The design constraint that dominated the X-14 has been dissolved rather than solved**, which is the
same verdict the previous article reached about the X-13 by a different route on an aircraft that
solved vertical take-off the opposite way.

**But the constraint moved rather than vanishing.** Setting the multirotor relation equal to the
X-14A's maximum gives **17.3 metres of span at an air-taxi thrust margin**, against the 28 metres at
which this article found jet lift exhausting its bleed budget. Large hovering aircraft are still hard,
and for a reason the X-14A measured.

Representative figures: a small quadrotor at 173 rad/s², a cargo multirotor at 54.2, an air taxi at
4.33, against the X-14A's 2.0.

---

## The Loop-Order Result Gained a Retrospective Sting

The equation pass established that the X-14A presented a fourth-order plant from stick to position,
third order only below the damping break. The break sat at 0.45 and 0.59 per second, or periods of
fourteen and eleven seconds.

**A modern attitude loop closes near ten to thirty radians per second**, more than an order of
magnitude above anything the X-14A could synthesise. **The aircraft therefore sat in its fourth-order
regime across the whole of the band its pilots actually worked in**, which is the sharpest available
explanation of why it was hard to fly, and it could only be stated once the modern comparison was
computed.

---

## Two Defects Found and Fixed

**The URL-stability guard fired on the master rebuild and caught two cited anchors that had drifted to
different documents.** A biplane tail-sitter paper and a shared-control paper both acquired new
disambiguation suffixes when the 687 new records were merged. Both were repointed to the documents the
prose meant. **That is the third consecutive article in which this guard has caught real drift**, and
it would have been silent corruption without it.

**Measuring citation density by section caught a structural misplacement.** The Designation section
stood at 56.6 citations per thousand words, the densest in the article and denser than the
contemporary survey, because the primary pass had attached two paragraphs about the criteria's later
application to a section whose subject is the designation. They were moved into What the Data Changed,
with the citation count asserted unchanged across the move. **Found by measuring, not by reading.**

---

## Verification

**386 reference definitions, 372 external URLs, zero duplicates, zero orphans.** All 372 URLs swept:
185 plain 200s, 121 publisher 403s from bot detection, 51 DTIC DOI redirects to a `.mil` host that
403s by policy, 13 202s, one openlibrary rate limit, and **one genuine 404**, the Lunar Landing
Research Vehicle reference, which pointed at a Wikipedia title that does not exist and was repointed
to the one that does. **An HTTP 200 does not verify a citation** and this sweep does not claim to.

All worked values re-derived independently and reproducing, including every publication-review
addition. `_verify.py` at the 0-error 21-warning corpus baseline from the repository root. Zero
contractions, em-dashes, en-dashes, prose colons, prose semicolons, prose parentheticals, doubled
words, duplicate headings, unbalanced emphasis markers, lone dollar-delimited lines, or adjacent
display-math seams. Genre section order correct with The Source Base immediately before the Epistemic
State. Isolated build succeeding with **109 rendered display blocks matching the source count
exactly**, Part 15 navigation, no unresolved reference links and no surviving Liquid tags.

**Equation count was measured before and after the section replacement**, per the A310 lesson, and rose
from 103 to 109 rather than silently dropping.

The Epistemic State was extended to flag that the three modern reference vehicles are representative
rather than actual, that the 7.41 percent bleed figure assumes a standing rather than demand-only
supply and that the comparison would be overstated if it were demand-only, and that the modern
bandwidth figure is a quoted range rather than a measurement made here.

---

## Final State

**1515 lines, 109 display equations, 386 references, 19,934 body words.**

Lines and equations inside band. **References finish 6 above the 380 ceiling, reported rather than
trimmed** under the standing no-reference-limit directive, as A309 did. **Nothing was trimmed at any
point in any of the four passes**, which makes A311 the sixth consecutive article to finish that way.

Contemporary references **129, or 35.5 percent of dated**, inside the 101 to 189 absolute range held
since A301. Primary sources 234, or 64.5 percent of dated, above A310's 52.4 percent.

---

## State

**Pushed.** Nothing in this series is published, and the deploy workflow builds without `--drafts`, so
the push is safe. **The publication-order dependency is fifteen deep**, A311 back to A297.

Fifteen articles complete of seventy-two. **Categories remain undecided** at `aerospace history
engineering`, fifteen articles deep and raised nineteen times.

A312 is the North American X-15, and the risk is the reverse of the usual one. **The record is large
enough that the article could become a summary rather than an analysis.** The keystone will have to be
chosen and defended rather than discovered, and the A311 harvest will not help.
