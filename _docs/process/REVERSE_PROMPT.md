# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A314 drafted, the Lockheed X-17. The first of four passes. Committed, **not pushed**, not
published. All eighteen articles in the series remain in `_drafts/`.

---

## The Vehicle Fired Rockets Downward, and the Article Had to Justify That

The X-17 went up, turned over, and fired two solid stages **downward** to drive a nose cone into thick
air at Mach 14.5. Everything in the article follows from establishing that this was necessary rather
than merely striking.

**Free fall from its own apogee reaches 1,684 metres per second against an achieved 4,023.** That is a
speed ratio of 2.389, and convective heating goes as the CUBE of speed, so the heating ratio is

**13.63.**

A vehicle that merely fell would have produced under a tenth of the thermal condition it was built to
study. **The downward stages are not an enhancement of the experiment. They are the experiment.**

That conclusion survives the source disagreement. Published apogees differ at about 100 miles, about
500,000 feet, and 250 miles, and even from the largest of those free fall still falls short by a factor
of 3.15.

---

## The Keystone Is Partial Simulation, and It Partitions Cleanly

A re-entry is several simultaneous conditions. Three must be matched. **Velocity**, which sets the
chemistry through stagnation enthalpy. **Heating rate**, which the structure must survive. And the
**degree of chemical nonequilibrium**, through the binary scaling parameter.

A test vehicle has two knobs, altitude and model scale. **Two knobs cannot satisfy three conditions.**

**What the trade buys.** Density enters the heating correlation under a square root and velocity cubed,
so holding heating fixed requires density proportional to velocity to the minus sixth. At 57 percent of
intercontinental velocity the X-17 needs **27.74 times the density**, which is 13.97 kilometres, and
both conditions then give 1,398 watts per square centimetre exactly.

**What it cannot buy.** Stagnation enthalpy is one half of velocity squared and **contains no density
at all**. The X-17 reached 8.094 megajoules per kilogramme against 24.50, or **33.0 percent of the
energy per unit mass**, and no choice of altitude changes it. At 8 megajoules oxygen is fully
dissociated and nitrogen partly. At 24.5 nitrogen dissociation is far advanced and ionisation has
begun. **These are different gases doing the heating.**

| Quantity | Reproduced |
|---|---|
| Stagnation heating rate | **Yes, exactly** |
| Full scale and real material | **Yes** |
| Boundary layer state | **Yes, arguably more severe** |
| Stagnation enthalpy and chemistry | **No, 33 percent** |
| Nonequilibrium state | **No, 9.25 times off** |
| Total heat load | **No, about a quarter** |

**The framing the article carries is that the programme surrendered the gas physics because nobody
could compute it, and kept the heat flux because everybody needed to design against it.** That was
correct for 1956 and would be wrong today, which is the most interesting thing about the vehicle.

---

## Series Threads Worth Noting

**Mach 14.5 is 2.05 times the Mach 7.06 perfect-gas validity limit** that the X-15 article computed for
its own arithmetic. The X-17 flew deep into the regime A312 identified as the edge of its own method.

**This is the second consecutive subject with no archival record of its own.** The X-16 was cancelled
and classified. The X-17 flew and was classified. Both articles are carried by the literature of the
question rather than of the vehicle, and each Source Base says so.

**The X-17 boosted the three Operation Argus high-altitude nuclear detonations in 1958.** That is the
only instance so far in this series of an X-designated vehicle delivering a nuclear device, and the
article names it plainly rather than passing over it.

---

## The A313 Lesson Was Applied Proactively

A313's coverage audit found three citations across the whole of 1960 to 2018 because the draft harvest
never asked for the middle era, and correcting that was a correction to the article's implicit history.
**The mid-era sweep is present in A314's harvest from the start.** The pool is 1,181 records and the
master 1,059 entries with the era already covered.

---

## Verification

**56 independent re-derivations, zero disagreements**, using a trapezoidal integration of the
hydrostatic equation so that the calculation module cannot validate itself. **This is the first article
in several where the number check found nothing**, which I record rather than treat as an achievement.

71 reference definitions, 54 external URLs, zero duplicates or orphans. 40 plain 200s, 4 publisher
403s, 10 DTIC DOIs verified through the Crossref registry with matching titles.

**A title scan of all 46 cited research entries found no off-topic citation.** The single flag was a
false positive of the scan's own keyword list, which did not include arc-jet. That scan exists because
A313's publication review removed sixteen citations a title search had wrongly returned.

`_verify.py` at the 0-error 21-warning corpus baseline. Zero style violations after three adjacent
display-math seams were given connective prose. Isolated build passing with 27 of 27 display blocks
rendered, 3 of 3 tables, and Part 18 navigation.

**One defect caught in my own tooling.** The isolated build script was copied from A313 and its series
navigation check still tested for Part 17 in one of two clauses after the other had been repointed to
Part 18. That is the copied-script defect A311 and A312 both shipped, caught here by reading the
repointed file rather than trusting the replacement.

---

## State

**461 lines, 27 display equations, 71 references, 5,266 body words.**

That is again **between the documentation-poor and full-aircraft classes on all three measures**,
exactly as A313's draft was. The equation and reference passes will raise the last two substantially.

**Committed, not pushed**, per the series rhythm for a draft pass. Nothing in the series is published
and the deploy workflow builds without `--drafts`.

**The publication-order dependency is eighteen deep**, A314 back to A297, and every cross-reference
points backward.

Eighteen articles complete of seventy-two. **Categories remain undecided** at `aerospace history
engineering`, and **the fourth-class question in `RESEARCH_AIRCRAFT_STRUCTURE.md` is now live for a
second consecutive article** rather than one. Both remain yours to settle.

A315 is the Hiller X-18, editorial date 2025-10-24, which returns the series to jet-lift and tilt-wing
and therefore to the A310 and A311 literature.
