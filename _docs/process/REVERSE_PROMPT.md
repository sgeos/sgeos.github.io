# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A320, the Martin Marietta X-23 PRIME, drafted. The first of the four passes.
**Committed, not pushed.** Not published.

**Draft state 1,291 lines, 31 display equations, 871 references, 10,177 words.**

---

## A Judgement Call You May Want to Overrule

**I treated this as a full-aircraft article rather than the designation-anomaly stub the genre document
classes it as.** That class runs to 40 to 150 lines with no keystone, because the subject is a number
rather than an aircraft.

That did not fit. **The SV-5D was a real vehicle, three flew, one was recovered, and it returned a
measurement that can be checked against a derivation.** The genre document's own Handling a Thin Record
section names this exact case and says the conflict belongs in the article rather than behind it, which
is not the same as saying the article should be nothing but the conflict. The anomaly has its own
section and is treated at length.

**If you would rather have the stub, say so and I will cut it.**

---

## The Article's Central Result

**A lift-to-drag ratio near unity is not a round number. It is the threshold at which a returning
spacecraft can reach a chosen landing site on the next orbit instead of waiting a day.**

The chain is four steps and each is derived rather than asserted. Equilibrium glide with a constant bank
gives a closed-form crossrange of $y/R = (\pi^2/48)(L/D)^2$. The bank optimum is exactly 45 degrees and
depends on nothing at all. The crossrange a vehicle needs is half the ground-track spacing, or 1,254
kilometres at the equator. Inverting gives **0.978**.

**The heading-change relation drops the atmosphere, the mass and the reference area entirely**, which is
why this result could be obtained for a vehicle whose reference area is not published anywhere.

---

## The Verifier Contradicted the Article and the Verifier Was Right

**This is the most useful thing that happened and it is worth reading in full.**

The independent check marches a trajectory rather than evaluating the closed form, and it disagreed by
nine to twelve percent. The cause is that the classical derivation replaces $\sin\psi$ by $\psi$, and at
a lift-to-drag ratio near unity **the accumulated heading passes 180 degrees, where those two quantities
have opposite signs.** The approximation does not degrade. It inverts.

**Correcting it moved the requirement from 0.978 to 1.018, which is closer to unity.** The headline
survived and got better, which is luck rather than vindication, and the article reports both numbers.

**It also destroyed a false confirmation, and that is the part with teeth.** The closed form matched the
demonstrated crossrange to within one percent at a lift-to-drag ratio of 1.0, which looked like the
flight data settling a live source disagreement. It was two errors cancelling. The exact solve puts the
flown ratio at **1.05 to 1.18, between the two published figures rather than equal to either**.

**A second circular check was caught the same way.** An early attempt recovered a bank angle of 45.13
degrees against an assumed optimum of 45, which looked like confirmation and was the assumed
lift-to-drag ratio of 1.2 being fed straight back in. **A suspiciously clean agreement is the signal.**

---

## An Unfitted Coincidence, Checked Twice

**The Space Shuttle's 1,100 nautical mile crossrange requirement is 2,037 kilometres. The Earth turns
2,061 kilometres under a once-around polar orbit at Vandenberg's latitude. The two agree to 1.2
percent and nothing was fitted to anything.**

The requirement that shaped the Shuttle's wing is the distance its launch site travels while a
spacecraft goes round once. PRIME demonstrated 56 percent of it with a vehicle weighing 894 pounds.

---

## The Designation, Reported and Not Resolved

Per the standing instruction, the conflict is stated and left standing. The record is stranger than a
simple omission.

- **16 November 1965.** X-23A requested, for the **SV-5P**, the piloted vehicle. The accompanying
  description says so explicitly.
- **15 December 1965.** Refused, **on the ground that the aircraft was unmanned.**
- **Late 1966.** A proposal for a new designation category for gliding re-entry vehicles is raised and
  dropped. The decision is to seek X-23A for the SV-5D and X-24A for the SV-5P.
- **X-24A was requested and approved. No request for X-23A was ever sent.**

**The manned vehicle was refused a number for being unmanned, and a year later got a different number
for being manned.** The article says the record shows the designation was never assigned, says the world
calls it the X-23A anyway, and collapses neither.

**The dropped proposal for a new category is the piece most useful to the closing article**, because it
shows the system considering a new limb and instead absorbing the problem informally.

---

## Checks

**115 independent numerical checks passing**, with the crossrange re-derived by marching a trajectory,
the integral by Gauss-Legendre rather than Simpson, the great circle by the spherical law of cosines
rather than the haversine, and the simultaneous solve by bisection rather than algebra.

**`_verify.py` at the 21-warning baseline.** `check_any.py` clean across all 24 articles.

**653 of 653 DOIs confirmed registered in the Crossref registry, zero unregistered.**

**A 24-article isolated build succeeds with all 31 equations rendering as display math**, zero
unrendered Liquid, and 26 in-series links resolving.

**One tooling change.** `check_any.py` now exempts a doubled capitalised word, because a Spanish or
Catalan double surname repeats legitimately in citation display text. Miro Miro and Pinna 2018 and 2020
are real papers on hypersonic boundary-layer transition.

---

## Five New Homonym Families, All Found by Reading

**Query design prevented most of the contamination instead of filtering it.** No query in this harvest
contains PRIME or START, because those words belong to number theory and to arms control. The filters
that would have caught the mess found only forty-seven records to reject, which is the prevention
working.

**What got through was not anticipated by any amount of thinking about heat shields.**

- **Lateral motion of a vehicle** is railway hunting oscillation and road-vehicle lane keeping. Two such
  records had settled among the foundational crossrange papers, **which is the least visible place in
  the whole selection for them to be**
- **Maneuvering range** names an instrumented air combat facility, so the pool held its construction
  quality assurance plan
- **Lateral range** is a term of art in search and detection theory
- **Supercavitating** vehicles are underwater, which the underwater filter missed
- **Wind turbine** wake papers arrived through the broad contemporary catch-all

Six records read and dropped. The rejection list is now 394 entries.

---

## State

**A320 draft pass complete. Committed, not pushed, not published.**

Twenty-four of seventy-two. The publication-order dependency is twenty-four deep.

**Awaiting the equation-density review prompt.** The likely candidates are the skip-entry and
bank-reversal relations, the ballistic-coefficient and altitude history the glide implies, the Allen and
Eggers ballistic comparison in fuller form, the ablator recession rate, and the footprint area rather
than only its half-width.

**Still open and unchanged.** The fourth genre class, now **eight** consecutive articles finishing
outside all four named classes. The A305 length offer.
