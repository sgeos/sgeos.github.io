# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A313 publication review, the fourth and final pass. Committed and **pushed**. **Not
published.** All seventeen articles in the series remain in `_drafts/`.

---

## The Survey Found Two Things That Change the Article's Own Conclusions

The contemporary section grew from 57 references to **217 across twelve identifiable fields**. Two of
its findings are not extensions of the article. They act on it.

**The keystone is dissolved rather than solved.** This article's central result is that the X-16's
ceiling was set by how well a compressor works in thin air, and that the whole aeroplane lived on a
nineteen percent margin bought by ram recovery. **A solar-electric platform has no compressor and no
lapse exponent.** Photovoltaic output depends on irradiance rather than on air, so the term that
dominated the design by a factor of four over every aerodynamic parameter simply leaves the equation.

What replaces it is energy storage over the night. **The constraint did not get easier. It moved from
the propulsion system's altitude behaviour to the energy system's mass**, where the ceiling relation
punishes it just as hard.

**The binding constraint on a modern equivalent is certification, not performance.** A 1955 military
aeroplane needed to work. A modern high-altitude platform needs to work, be certified, be insurable,
and be integrated into shared airspace. The X-16 was cancelled by a procurement decision, which this
article argues was not an engineering verdict. Its descendants are more often delayed by an approval
process than a design problem. An article treating only the arithmetic would miss where the difficulty
now lies.

---

## Further Findings From the Survey

**The platform became the product.** What was a sortie is now a station, and the design driver is
holding position against stratospheric wind rather than range.

**The diplomatic problem returned in civil dress.** Who may authorise a persistent platform above a
country is the X-16's original difficulty, with the same absence of a settled answer.

**Buffet onset is still computed rather than known**, seventy years on. That is the most direct
available measure of how hard the corner actually is, and why this article's single assumed value
carries the sensitivity it does.

**The sensor improved and the penalty did not.** Ground sample distance is slant range times angular
resolution, which is exact and permanent. Angular resolution improved enormously, so **flying high
stopped being a compromise.**

**The modern remedy for the 23-knot instrument band is to stop trusting the pitot tube** and estimate
airspeed from fused inertial, satellite and model-based sources.

**A modern analysis of the X-16 is impossible for want of one table.** Every method in the very-flexible
-wing literature takes a stiffness distribution as its input, and none was ever published.

---

## The Largest Defect Class Was Citation Relevance, and Reading Found All of It

**Sixteen citations were removed after insertion.** The pattern is worth recording because a rule
caught none of them and several survived two successive filters.

| Search term | What it returned |
|---|---|
| resolution | wireless sensor network localisation; unexploded ordnance detection; **spectra of stars in globular clusters** |
| high aspect ratio | a high-explosive round for a **railgun bore** |
| fatigue under spectrum loading | **gun tube steel** |
| digital twin | cable-stayed bridges; rolling-element bearings |
| airborne hyperspectral imaging | the organic matter content of **winter wheat topsoil** |

**The general lesson, now stated in the Source Base, is that a keyword diagnostic within a field is not
diagnostic across the literature.** Aspect ratio, resolution, fatigue and digital twin each mean
something precise here and something entirely different one discipline away.

---

## Verification

**83 draft-pass and 74 equation-pass re-derivations, zero disagreements**, still reproducing after every
edit. 468 reference definitions, 452 external URLs, zero duplicates, zero orphans.

URL sweep: **255 plain 200s, 138 publisher 403s, 9 202s, and 50 DTIC DOIs verified through the Crossref
registry** with titles matching the prose. An HTTP 200 does not verify a citation and the sweep does not
claim to.

The contemporary section was **extended in place rather than replaced**, per the A310 defect where a
wholesale replacement silently dropped three equations. The count was measured before and after
regardless and held at 72. `_verify.py` at the 0-error 21-warning corpus baseline. Zero style
violations. Genre section order correct. Isolated build passing with 72 of 72 display blocks, 9 of 9
tables, Part 17 navigation.

---

## Final State, and the One Thing I Am Leaving to You

**1,233 lines, 72 display equations, 468 references, 13,316 body words.**

References are at or above the full-aircraft band. **Lines sit 67 below the 1,300 floor and equations 18
below the 90 floor.**

**A313 is the first article in the series to finish outside the named classes on two of three
measures.** I did not pad it to fit. The material supported what it supported, and the subject has no
technical record of its own, which is the whole reason the article exists in the shape it does.

Contemporary references are 217 of 443, or **49.0 percent**, which is a higher proportion than any
previous article in the series. That is a direct consequence of the X-16 having no literature, so the
only thing available to survey comprehensively is the question rather than the aircraft.

**Whether `RESEARCH_AIRCRAFT_STRUCTURE.md` should gain a fourth class is a decision I have deliberately
not made.** It has now come up on three consecutive passes and I would rather you settled it than have
me invent a band to justify an outcome.

---

## State

**Pushed.** Nothing in this series is published, and the deploy workflow builds without `--drafts`, so
the push is safe. **The publication-order dependency is seventeen deep**, A313 back to A297, and every
cross-reference points backward.

Seventeen articles complete of seventy-two. **Categories remain undecided** at `aerospace history
engineering`, seventeen articles deep and raised twenty-two times.

**A314 is the Lockheed X-17**, editorial date 2025-10-23, per the roster in `HANDOFF.md`. That is a
three-stage solid-fuel test vehicle for re-entry research, so it returns the series to the missile and
test-vehicle family last seen at the X-12 in A309 rather than continuing the aeroplane
run, and its literature will be re-entry heating rather than anything in the A313 pool. **Build its
harvest from scratch.** A315 is the Hiller X-18.
