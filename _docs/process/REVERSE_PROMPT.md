# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-07
**Task**: A308, the Convair X-11, drafted, verified, and committed. **Not pushed**, per the rhythm.
Three review passes remain.

---

## First, the Outstanding A307 Item Is Closed

The publication review reported that GitHub had created no CI run for the A307 push. Two runs for
`02127ae` have since appeared and **both completed successfully**. The delay was on GitHub's side, as
suspected. The site is deployed, the root returns 200, and A307 returns 404 because it is not
published, which is correct.

---

## What the X-11 Is

**The Atlas A.** It is the first flying article of the programme whose ballistic timeline the previous
article computed as the reason the Navaho was cancelled. The X-10 and the X-11 are separated by one
designation and four weeks. The X-11 first flew on 11 June 1957 and the Navaho cancellation message is
dated 12 July 1957.

**The keystone is structural mass fraction, and the vehicle cannot stand up without internal pressure.**
The skin is 301 extra-full-hard stainless at 0.014 to 0.037 inches, a radius-to-thickness ratio of 1622
to 4286, which is **five to thirteen times thinner in proportion than an aluminium drink can**. It needs
about five pounds per square inch of nitrogen when unfuelled or it folds.

---

## The Central Result, Which Closes With A307

A structural mass fraction of 4.58 percent gives a mass ratio of 21.85 and an ideal velocity of 8530
metres per second. Subtracting the 7193 metres per second that the previous article derived for a ten
thousand kilometre ballistic trajectory gives gravity and drag losses of 1337, adopted as a calibration.
Scaling the structure and carrying it back through both relations gives

| Structure | Range |
|---|---|
| as built | 9,999 km |
| 1.5 times | 5,676 km |
| 2 times | 3,941 km |
| 3 times | 2,346 km |

**Making the structure half as efficient costs sixty-one percent of the range**, which turns an
intercontinental weapon into an intermediate-range one. That is the whole argument for the balloon tank.

---

## The Series Contribution, Which Neither Article Could Make Alone

The X-10's keystone was a drift rate. It accumulates, and twenty-eight minutes of flight could not
measure it. The X-11's keystone is a structural load. It is applied in full within the first two
minutes, so a flight reaching only 120 kilometres of apogee and a fifth of the intercontinental burnout
speed still applies every load the mission will ever apply.

**A keystone that is exercised early can be validated cheaply. A keystone that accumulates cannot.**
The X-11 tested more of its keystone in seven percent of its mission than the X-10 did in sixteen
percent of its, and the difference is a property of the quantity rather than of either company.

---

## Other Results the Sources Do Not State

The critical bending moment of a pressure-stabilised cylinder is $M = \pi p r^{3} / 2$ and is
**independent of skin thickness**, which is the mathematical form of the claim that the pressure is
doing the work. The tensile allowable exceeds the knocked-down compressive allowable by a factor of 67.
The light gauge cannot exist at full pressure, which demonstrates the thickness taper rather than
contradicting it. The common bulkhead saves about four percent of the empty vehicle. A
constant-acceleration vertical ascent reaches maximum dynamic pressure at exactly one scale height,
independent of the acceleration. And the range sensitivity to burnout velocity is 4.34, so an
eight-hundred-metre accuracy requires cutting the engines to **0.13 metres per second out of 7193**,
which is why this weapon needs a clock where the previous one needed a navigator.

---

## Source Base, a Controlled Contrast

The same Crossref route into the defence archive that returns nothing whatever for the Navaho project
number MX-770 returns, for the Atlas, Flight Test Working Group reports for individual missiles, five
volumes of a Difficulties Review of the booster and its ground support, propellant-loading system
design, and engine system-test data. **Same archive, same route, same query form, and the difference is
that one programme was cancelled in 1957 and the other flew for sixty years.**

---

## An Error I Made and Corrected

The range-to-velocity sensitivity was first written as approximately 2.4, with a derivation that was
malformed as displayed. **The correct value is 4.34**, confirmed by closed form and by numerical
differentiation, and the dependent figures changed from 24 to 43 kilometres and from 0.24 to 0.13
metres per second.

The cause is worth recording plainly. That expansion was written without computing the values first,
which is exactly what the compute-before-writing rule forbids, and the defect appeared the moment the
rule was skipped. The rule has held for three articles when followed and failed immediately when not.

---

## Verification

All 78 worked values re-derived independently, with no corrections beyond the one above. 160 references
with zero undefined, zero orphaned, and zero duplicate URLs. `_verify.py` at the 0-error 21-warning
corpus baseline. Zero contractions, em-dashes, en-dashes, prose colons, prose semicolons, prose
parentheticals, doubled words, duplicate headings, display-math seam defects, or lone dollar-delimited
lines. Isolated build succeeding with 54 rendered display blocks against 54 in source, Part 12
navigation, both tables, no unresolved reference links and no surviving Liquid tags.

---

## State

**678 lines, 54 display equations, 160 references, 9,301 words.**

All three densities are under band, which is the intended approach direction, but **this is further
below than A307's draft was** at 943, 84, and 213. The three passes have more to close here than they
did there, and I am flagging it rather than padding.

The harvest is retained for A309, since the X-12 is the Atlas B and shares most of the record.

**Committed, not pushed.** The publication-order dependency is twelve deep. **Categories remain
undecided** at `aerospace history engineering`, twelve articles deep and raised thirteen times.
