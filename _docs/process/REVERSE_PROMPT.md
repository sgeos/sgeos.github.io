# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A312 equation-density review, the second of four passes. **Committed, not pushed.** All
sixteen articles in the series remain in `_drafts/`.

---

## The Pass Answered the Question the Keystone Posed and the Draft Left Open

The article states its keystone as **how much of the shed energy ends up inside the structure rather
than in the air behind it**, and then never answered it. A keystone that poses a question the article
leaves open is a slogan rather than a keystone, so this pass answered it.

The route is the Reynolds analogy. The heat entering the wall divided by the friction work done at it
collapses to

**q̇ / τV = c_p (T_aw − T_w) / V²**

in which **the velocity cancels out of the numerator entirely**. The fraction depends only on how far
the wall sits below the adiabatic wall temperature, measured against the vehicle's kinetic energy.

At the record condition that gives **43.0 percent for a cold wall, 27.7 at the design limit, and 7.2
at the temperature Knight's leading edges actually reached.**

**A hot wall absorbs a smaller fraction than a cold one.** That is the part the framing did not
anticipate: running hot is not merely something a hot structure tolerates, it is part of the mechanism
by which it protects itself, because the driving temperature difference is what pushes heat in and a
hot wall has less of one.

---

## A Wrong Claim Caught by Computing Further Inside the Same Pass

I first wrote the energy fraction on an **assumed** friction fraction of 35 percent of total drag,
which gave ten percent to the structure and a heat load **exceeding** the structure's absorptive
capacity, at a ratio of 1.19.

Estimating the friction drag directly — turbulent flat-plate coefficient at the record Reynolds number
of 3.2 × 10⁷ over a plausible wetted area — gives **8 to 26 percent, centring near 15.** Not 35.

**The corrected figure is four percent to the structure and a ratio of 0.51, so the conclusion
inverts.** The total heat load is comfortably within capacity, with roughly a factor of two in hand,
and the binding constraint is the local rate.

**The corrected version is the one that agrees with the rest of the article.** A rate-limited hot
structure should have load margin in hand; the erroneous version contradicted the article's own
earlier finding. The two halves now agree, and they did not have to.

That is the **ninth consecutive article** in which computing before writing caught a wrong claim, and
the **second in this article** after the crossover order-of-magnitude error in the draft pass.

---

## The Relation That Closes the Keystone

Deceleration by drag at constant altitude integrates to a time to shed the energy. Evaluated at the
record speed down to a landing speed:

| Altitude | Time to shed the energy |
|----------|--------------------------|
| 31 km, the record altitude | 102 minutes |
| 20 km | 18 minutes |
| 15 km | 8 minutes |

**An X-15 flight lasts eight to twelve minutes in total.**

**So the aircraft cannot dispose of its energy where it acquires it. It must descend into denser air
to do so, and descending is precisely what raises the heating.** That is the keystone stated as a
single trap, and every other result in the sizing section is a term in it.

---

## Six Further Results

**The stagnation temperature is 2,271 K**, so the air is 2.46 times hotter than the metal is permitted
to become, and **89.9 percent of the oncoming stream's total enthalpy is kinetic**. The heat is the
aircraft's own energy arriving back at it.

**Newtonian impact theory gives Cp = 2 sin²θ, independent of Mach number**, which is exactly the
property a designer wants where everything else is falling away. A ten-degree wedge beats a
three-degree surface by a factor of 11.

**The same relation puts the trim angle of attack at the record near 13.8 degrees.** A hypersonic
aeroplane does not fly nose-first.

**The blunt-body trade eliminates to D_nose ∝ q̇⁻⁴**, so halving the heating costs sixteen times the
nose drag. That fourth-power exchange is why a capsule is blunt and an aeroplane that must glide home
is not.

**The B-52 supplies under seven percent of the energy budget.** The aircraft makes the other 93 percent
itself.

**A 1.5 mm skin is through-soaked in half a second and has no interior**, which is why the design can
be reasoned about as a surface in radiative balance with no thermal-lag margin to hide behind.

---

## Verification

**90 display equations, up from 48 across 22 edits, landing exactly on the floor.** All 43 newly
introduced numbers re-derived independently and reproducing, on top of the 40 from the draft pass.
`_verify.py` at the 0-error 21-warning corpus baseline from the repository root.

Three style violations were introduced by my own edits and caught: a prose semicolon, a doubled "and"
created by the fix for that semicolon, and an em dash. **The corpus verifier and the article's own
checker agreed on the em dash**, which is the cross-check working as intended.

Isolated build succeeding with **90 rendered display blocks matching the source count exactly**, Part
16 navigation, no unresolved reference links and no surviving Liquid tags. The Epistemic State was
extended to record the corrected result explicitly, including the superseded figure, and to state the
new assumptions carried by the energy-partition analysis.

---

## State

**929 lines, 90 display equations, 77 references, 10,729 body words.**

**Equations are exactly on the floor of the 90 to 130 band.** Lines at 929 against 1300 and references
at 77 against 250 both still approach from below, which the remaining two passes close. Nothing was
trimmed.

**Committed, not pushed.** Nothing in this series is published. The publication-order dependency is
sixteen deep. **Categories remain undecided** at `aerospace history engineering`, sixteen articles deep
and raised twenty times.
