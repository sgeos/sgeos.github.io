# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-07
**Task**: A309 primary-reference pass, the third of four. Committed and **not pushed**. **Not
published.** All thirteen articles in the series remain in `_drafts/`.

---

## Two Cited References Had Silently Become Different Papers

This belongs first because it is a defect that shipped undetected in the previous two passes and
would have shipped in the article.

Rebuilding the master table on the enlarged harvest **moved two anchors the article was already
citing onto entirely different documents.** `research_buell_1964` went from a paper on ground-wind
loads in launch vehicles to one on Doppler-inertial techniques, and `research_naca_1969` went from an
Atlas-Agena flight performance report to a study of inflatable falling spheres. Both were cited in
passages where the original document was the correct one, so the article would have carried two
citations pointing at unrelated work.

The cause is the one the handoff already records. Disambiguation suffixes are assigned in generator
iteration order, so a larger harvest reshuffles them. **What was new is that this can happen to
already-cited anchors and not merely to ones being chosen**, which the previous statement of the rule
did not cover.

**The toolchain now prevents it structurally.** The reference section already in the file records the
URL each anchor had when it was cited, so it is ground truth for what the prose meant. The generator
compares every cited anchor's new URL against that record and refuses to regenerate if any changed.
It is a guard rather than a habit, which is what this defect class needed after biting twice.

---

## The Pass Found an Entire Missing Literature

**The largest addition was not planned and came from following a relation rather than a topic.**

The equation pass established that the flattening of the Earth is 21.4 kilometres, or 5.8 times the
miss budget, and that the oblate field displaces the impact point by of order 34 kilometres. The
article named the consequence in one sentence, that the ballistic missile created a geodetic
requirement it could not itself satisfy. The harvest assembled for a missile article contained
**nothing at all** about datums, geoids, deflection of the vertical, or zonal harmonics.

A sweep aimed at them returned a complete discipline, and a new section now traces it. The classical
pre-satellite method determined the geoid from surface gravity and left continental datums internally
consistent and mutually offset, so **two continents surveyed separately are two coordinate systems
and a weapon aimed from one at the other is aiming at a number rather than a place.** Satellite
perturbations then determined the zonal harmonics directly, Doppler tracking supplied the non-zonal
terms, and a world datum tying the continents together arrives in the mid 1970s.

**Sixteen years separate the first Atlas B flight from a published world geodetic datum**, so for
much of the force's operational life the target coordinates were plausibly less well known than the
guidance system's own contribution to the error budget. That inference is flagged in the Epistemic
State as resting on publication dates rather than on when the knowledge reached a targeting
organisation, which may well have been earlier and classified.

**The source-base observation is the sharpest in the article.** The weapon literature is classified,
fragmentary, and archived under project numbers. The literature the weapon depended on is openly
published in astronomical and geodetic journals, because the shape of the Earth was not a secret and
could not usefully have been made one.

---

## The Four Sections in Debt Are Closed

The coverage audit found four sections carrying equations and too few citations, which is fewer than
A307's fourteen or A308's eleven because the draft pass repaired most of that debt already.

**The Angle Is Almost Free** gained the optimum-trajectory literature. **The Earth Is Turning**, which
had zero citations against two equations, gained the geodetic-azimuth material, which is the correct
attachment since a launch heading must be referred to the same figure of the Earth as the target.
**The Sustainer** gained a caution that matters: a specific impulse quoted to three figures for a
period engine is a trajectory reconstruction rather than a measurement, and the 309 second figure
carries most of this article's orbital arithmetic. **Where the Framing Breaks Down** gained the wind
and reentry-dispersion literature, including the Atlas programme's own flight-wind restriction
procedure and a paper that treats a reentry body's dispersion as a design variable.

---

## Other Clusters Added

**Thrust termination**, where the solid-motor literature shows the last-instant uncertainty is generic
rather than peculiar to liquid engines. **Gyroscope instruments**, which support the equation pass's
corrected reading rather than the draft's. **Radio interferometry**, where the founding astronomical
instrument paper makes the point that a missile tracker and a radio telescope are the same instrument
pointed at different things. **Cryogenic storage and boil-off**, where every document is a reason the
storable and solid-fuelled competitors won and none of them is about accuracy. **Project Courier**,
the direct successor that took SCORE's store-and-forward architecture and built a purpose-designed
satellite around it. Plus range instrumentation, orbital lifetime under oblateness, and the
covariance machinery that let programmes substitute analysis for the hundred flights they could not
fly.

---

## Verification

**251 external URLs with zero duplicates.** All 30 fixed identifiers at 200. **All 217 DOIs
Crossref-resolved on title at the 0.85 threshold with zero flagged**, and the article still contains
no hand-entered identifier anywhere. `_verify.py` at the 0-error 21-warning corpus baseline. Zero
contractions, em-dashes, en-dashes, prose colons, prose semicolons, prose parentheticals, doubled
words, duplicate headings, lone dollar-delimited lines, or adjacent display-math seams. All fifteen
insertion seams read by eye, and one meta-reference to the drafting process that had leaked into the
prose was removed. Isolated build succeeding with 135 rendered display blocks matching the source
count exactly, Part 13 navigation, eleven tables, no unresolved reference links and no surviving
Liquid tags.

Every anchor added this pass was checked against its title before the sentence using it was written,
and 75 were verified in a single batch with zero problems.

---

## State

**1286 lines, 135 display equations, 263 reference definitions, 16,482 body words.**

**References are inside band at 263 against 250 to 380.** Lines are 14 below the 1300 floor, which is
the closest any article in this series has come to the floor before its publication review. Equations
remain five above the ceiling and are reported rather than trimmed.

**Primary sources are 220 of 246, or 89.4 percent of dated**, up from 83.1. That is the highest
primary fraction in the series.

Citation density rose from 14.01 to 18.72 per thousand body words. The citation construction mix is
healthy, with the top bigram at 3.4 percent, and `atlas` at 6.03 per thousand is the subject noun and
is reported rather than remediated.

---

## What the Publication Review Has to Close

**Contemporary references are 23, or 9.3 percent of dated.** The absolute count is unchanged and the
percentage fell only because the primary pass grew the denominator, which is exactly the behaviour
the count-versus-percentage rule predicts. Against the 101 to 189 absolute count the series has held
since A301, **this is the largest contemporary gap any article has carried into a publication
review**, and closing it will also carry the article past the line floor.

---

**Committed, not pushed.** Thirteen articles drafted of seventy-two, none published. The
publication-order dependency is thirteen deep, A309 back to A297. **Categories remain undecided** at
`aerospace history engineering`, thirteen articles deep and raised seventeen times.
