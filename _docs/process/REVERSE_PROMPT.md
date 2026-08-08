# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A314 publication review, the fourth and final pass. Committed and **pushed**. **Not
published.** All eighteen articles in the series remain in `_drafts/`.

---

## The Survey Found Two Things That Act on the Article

The contemporary section grew from 38 references to **208 across twelve fields**. Two of its
observations are not extensions.

**The chemistry the X-17 surrendered is now the most expensive requirement, not the cheapest.** The
vehicle gave up velocity, and therefore the gas chemistry, because it was the cheapest of three
requirements to abandon and because nobody could compute it anyway. In a modern prediction everything
else is comparatively well posed and **the chemistry is where the model form uncertainty lives**. The
1956 reasoning has inverted.

**The relations are now run in reverse.** Design for demise computes ballistic coefficient, ablation
rate and heat load in order to guarantee that a structure **comes apart and burns** rather than that it
survives. That application did not exist in 1956, and it is the sharpest available demonstration of how
general the underlying physics turned out to be. **The X-17 measured how to survive; its instruments now
serve an industry that sometimes needs the opposite.**

---

## Further Findings

**Prediction replaced measurement and then needed validating**, so the X-17's kind of data was relocated
rather than removed. It now serves to check a code rather than to characterise an environment, which is
a different epistemic role for the same measurement.

**The facility shortfall is unresolved seventy years on.** What changed is that it is measured and
quoted rather than argued about — the same improvement this article credits the X-17's own partition
with.

**Ultra-high temperature ceramics are designed against exactly the Stefan-Boltzmann calculation this
article performs**, and the hafnium carbide that appears as the single survivor in the article's own
table is precisely the family that literature pursues.

**Entry, descent and landing is where the problem actually went.** A Mars entry vehicle is the
Allen-Eggers argument with somebody else's atmosphere, carrying a density uncertainty no terrestrial
calculation has to bear.

**Nobody now builds an X-17, and the reason is not that the problem was solved.**

---

## Thirty Rejected by Reading, and One Caught by Accident

New examples from this pass:

| Search term | What it returned |
|---|---|
| nonequilibrium | a two-temperature **Ising model** |
| ionisation | electron impact on **krypton** |
| Bayesian calibration | resource depletion in **Peruvian mining districts** |
| demise | dataveillance and the **demise of interpretive flexibility** |
| thermal protection system | a passive TPS for **divers**, which is a wetsuit |

**The wetsuit was caught only because the DOI verification step printed its title.** It had passed the
exclusion list, the bucket pattern, and a relevance scan. That is an argument for reading output that is
nominally about something else.

**A counter-observation belongs alongside it.** An automated relevance scan run after insertion flagged
ten further citations and **every one was a false positive of the scan's own keyword list** — a
ceramic-heated tunnel, high-emissivity coatings, expansion-tube flow characterisation. The reading step
finds real defects. The automated step generates noise in both directions and is useful only as a prompt
to look.

---

## Verification

**56 draft-pass and 44 equation-pass re-derivations, zero disagreements**, still reproducing after every
edit. 446 reference definitions, 429 external URLs, zero duplicates or orphans.

URL sweep: **245 plain 200s, 134 publisher 403s, 7 202s, 1 302, and 43 DTIC DOIs verified through the
Crossref registry** with titles matching the prose.

The section was extended in place rather than replaced, per the A310 defect, and the equation count was
measured before and after regardless, holding at 47. `_verify.py` at the 0-error 21-warning corpus
baseline. Zero style violations. Genre section order correct. Isolated build passing with 47 of 47
display blocks, 7 of 7 tables, Part 18 navigation.

---

## Final State

**1,066 lines, 47 display equations, 446 references, 10,417 body words.**

References are above the full-aircraft band. **Lines sit 234 below its 1,300 floor and equations 43
below the 90 floor**, so A314 finishes outside the named classes on two of three measures, exactly as
A313 did. I did not pad it.

Contemporary is 208 of 421 research citations, or **49.4 percent**, matching A313's proportion and for
the same structural reason: a subject with no literature of its own can only be surveyed through its
question.

**That is now two consecutive articles finishing outside the named classes in the same way, across
eight passes.** The fourth-class question in `RESEARCH_AIRCRAFT_STRUCTURE.md` is no longer a one-off
observation and I have still not made the decision, because it is a change to the genre document and
that is yours.

---

## State

**Pushed.** Nothing in this series is published, and the deploy workflow builds without `--drafts`, so
the push is safe. **The publication-order dependency is eighteen deep**, A314 back to A297, and every
cross-reference points backward.

Eighteen articles complete of seventy-two. **Categories remain undecided** at `aerospace history
engineering`, raised twenty-three times.

**A315 is the Hiller X-18**, editorial date 2025-10-24, a tilt-wing transport testbed. That returns the
series to jet-lift and tilt-wing, so the A310 and A311 pools are genuinely relevant for the first time
in three articles and the stated exception to the one-directory rule may apply. Check
`RESEARCH_AIRCRAFT_STRUCTURE.md` and the A311 harvest before building a new one.
