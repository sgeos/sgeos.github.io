# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A320 publication review, the fourth and final pass. Committed and **pushed**. **Not
published.** All twenty-four articles in the series remain in `_drafts/`.

**Final state 4,088 lines, 72 display equations, 3,403 references, 23,879 words.**

**Contemporary coverage from 550 to 1,685 of 3,372 research citations, or 50.0 percent**, across ten
subsections where the draft had none.

---

## The Survey's Organising Claim

**The capability was demonstrated, adopted, then given up by the very class of vehicle it had been built
for, and adopted again by a different class for the opposite reason.**

**Every crewed spacecraft flying today comes home the way Mercury did.** Orion, Dragon, Soyuz and
Shenzhou are blunt capsules on parachutes, and this article's own relation prices that choice exactly. A
capsule trims near a lift-to-drag ratio of 0.3, which buys 117 kilometres of crossrange against the
1,254 kilometres derived earlier as the once-per-orbit requirement.

**Nine percent.** A modern crewed spacecraft has, by deliberate choice, about one eleventh of the
crossrange that would let it come home when it wants to. **That is not a failure of engineering. It is
the requirement disappearing**, because the once-around polar mission that generated the Shuttle's
1,100 nautical miles was an Air Force requirement and nothing replaced it.

**Meanwhile crossrange became the whole point of the hypersonic glide vehicle**, where the value is not
reaching a chosen site but being impossible to extrapolate. The literature is about estimating and
tracking a manoeuvring entry body where the period literature was about designing one. **The relation is
identical and the motive is inverted, and the equation cannot tell the difference.**

---

## The Two Sharpest Things in the Survey

**The part of PRIME that failed twice is the part that has been most thoroughly vindicated.** Mid-air
retrieval, which lost two of three vehicles, has since been demonstrated on a returning orbital booster.
**The technique outlived the aerodynamics**, and the configuration it was carrying is flown by nobody.

**The footprint inverted.** PRIME wanted a large one. Modern practice wants a small and precisely
predicted one, because the same trajectory mathematics now serves debris casualty risk and controlled
disposal. **A quantity computed to show what a vehicle could reach is now computed to prove what it
cannot.**

---

## The Verifier Caught an Under-Converged Table, and Then Caught Itself

**This is the most instructive failure of the pass.**

Entry at exactly circular speed makes the factor of one over one minus u unbounded, so a uniform march
in speed is dominated by its first few steps. **The survey table was under-converged by two percent and
a step count that looked generous was not.** Two schemes differing only in whether they used the old or
the updated heading disagreed by four percent, which is what exposed it.

The fix was to integrate in **heading angle** instead, where the sine of the heading vanishes at the same
place the singularity sits, so the integrand is finite and ordinary quadrature converges.

**The first attempt at that carried an extra factor of two and disagreed with the speed march by exactly
two.** That is this series' own standing hint that the checker rather than the article is at fault, and
it was right again. Corrected, the two independent schemes agree to five significant figures at 1,213.6
kilometres, the exact required lift-to-drag ratio of 1.018 is confirmed, and four rows of the survey
table were fixed.

---

## A Design Flaw in This Pass's Own Tooling

**The survey was written by placeholder substitution, which froze its citations as literal text.** They
stopped tracking the clusters, so when fourteen records were dropped they survived in the body and
`gen_refs.py` correctly refused to emit. The citations were restored to live calls by position.

**Anchor-keyed drops were also found fragile.** Disambiguation suffixes shift when an earlier record is
removed, so dropping `research_xie_2024_3` can silently retarget a different paper. The rejection list is
now keyed by URL as well as by anchor.

---

## Three More Homonym Families, All From Reading the Sweep

**The electric road vehicle is the largest body of literature this series has had to exclude.** It shares
vehicle, thermal management, model predictive control, energy management and trajectory with entry work,
and there is far more of it. A contemporary query for model predictive control returns battery packs.

**Entry in cell biology** is a protein or a virus crossing a membrane. **Dispersion in atmospheric
science** is a pollutant plume and not a landing footprint.

Fourteen more records read and dropped. **The rejection list is now 469 entries** and this article
contributed 81 of them.

---

## Publication Checks

**Prose style.** Clean across all 24 articles.

**Diction.** `this article` reduced from 23 uses to 13 and `rather than` from 27 to 16. The two words
still above five per thousand are `vehicle` at 9.83 and `ratio` at 6.05. **Both were read in context and
both are the article's subject**, the second being the lift-to-drag ratio the whole piece turns on.

**Acronyms.** One real violation, `SI`, replaced with spelled-out metric units. `JC` and `SLV` are parts
of the JC-130B and Atlas SLV-3 model designations and are exempt.

**Reference integrity.** 3,403 references, zero undefined, zero orphaned, zero duplicate URLs.

**URL response.** 3,418 external links. **2,796 of 2,796 DOIs confirmed registered in the Crossref
registry, zero unregistered.** An HTTP 200 does not verify a citation, which is why the DOI half goes to
the registry.

**Numerical sanity.** 238 checks across two independent verifiers, both passing.

**Structural conformance.** Genre order intact, the three series sections present, The Source Base
immediately before Epistemic State.

**Build.** 24-article isolated build succeeds with all 72 equations rendering as display math across 18
sections and 28 subsections.

---

## A Note on the Era Balance

**The period count is essentially unchanged at 980 against 983 while the primary fraction falls from 68.7
to 45.6 percent.** That is the directive working as intended. This pass added roughly 1,100 contemporary
references and removed almost no period ones, so the denominator moved and the numerator did not.
**Stating the count as well as the fraction is the only way that reads correctly.**

---

## State

**A320 is complete. All four passes done, committed and pushed, not published.**

Twenty-four of seventy-two. The publication-order dependency is twenty-four deep.

**The next article is A321, the Martin Marietta X-24**, editorial date 2025-10-30, Part 25 of 72. It is
the piloted SV-5P, the same shape at larger scale, and **it is the vehicle that X-23A was refused for in
1965 and that received X-24A in 1967**. Much of the shape literature is already in this article's pool,
but the one-directory rule still holds and A321 should harvest its own, because the subject shifts from
entry mechanics to piloted low-speed handling and landing.

**Still open and unchanged.** The fourth genre class, now **ten** consecutive articles finishing outside
all four named classes, references far above band with lines and equations below. The A305 length offer.
