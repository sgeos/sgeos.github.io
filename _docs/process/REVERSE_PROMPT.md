# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A319 equation-density review, the second of four passes. **Committed, not pushed. Not
published.**

**13 display equations to 25**, across nine edits. 1,003 lines to 1,101, 6,630 words to 7,835.

---

## The Pass Corrected the Draft, Then Corrected Itself

The draft evaluated the duct normal force along an **assumed** linear ramp from ninety degrees at rest
to zero at the conversion speed, and reported a peak of 1.08 times duct thrust.

**The draft also said the real corridor could not be computed because the wing areas were not to hand.
That was giving up too early.** At the end of a conversion the ducts are horizontal and the wings carry
the whole weight, so the conversion speed implies the area,

$$S = \frac{2W}{\rho V_{\text{conv}}^{2} C_{L,\max}} = 213\ \text{ft}^{2}$$

and the implied mean chords of 3.62 and 3.10 feet on the two spans are what the photographs show. **That
is a check, not an assumption.**

Solving the force balance on that area puts the ducts at much larger angles much later than a linear ramp
does, and the momentum estimate climbs to **2.26 times the whole aircraft weight**.

---

## That Number Is Not Credible, and That Is the Finding

More than twice the weight, applied sideways in mid-conversion, would be unflyable and unmissable. So the
model is wrong there, and the useful question is where it stops being right.

The momentum argument assumes the duct captures its own streamtube and turns all of it, which holds while
the crossflow component is small compared with the velocity the duct induces,

$$\mu = \frac{V_{\infty} \sin i}{v_{i}}$$

**That parameter passes 0.5 at 100 feet per second and comes back below it at 195.** The momentum model is
valid at both ends of the conversion and invalid in the middle, **and the middle is exactly where a tilt
aircraft is hard to fly.**

What caps the force in that band is not momentum. It is that the lip cannot hold the flow round it at
that incidence and separates. **Lip stall was a mention in the draft and now has a computed boundary.**

The article now states the normal force reaches about the duct's own thrust where the model can be
trusted, and that beyond it the binding limit is lip separation. **It does not quote the number the model
produces where the model does not hold.**

---

## A Second Cross-Check, on the Drag

Installed power and the quoted 278 knot maximum speed give an equivalent flat-plate area,

$$f = \frac{D}{q} = \frac{4{,}689}{193.3} = 24.3\ \text{ft}^{2}$$

and four seven-foot ducts give the same number at a duct drag coefficient of 0.158, which is ordinary for
a short annular body with a propeller in it. **A clean aeroplane of this weight would have five to eight
square feet.** The lift-to-drag ratio at maximum speed is 3.26.

**That is the same trade seen a third time.** The shroud buys twenty-six percent of thrust in the hover,
charges an annular wing's normal force in the conversion, and charges again in cruise by holding 154
square feet of frontal area in the airstream for the rest of the flight.

---

## Also Now Computed

- **The duct pitching couple**, 31,500 foot-pounds nose-up over four ducts, which the tandem layout does
  not cancel because both pairs tilt the same way
- **The elevon authority against it**, 24,600 foot-pounds from four surfaces in the jets, the same order
  as the couple they exist to oppose, which is why they are that size and in that place
- **The cross-shaft**, 3,440 foot-pounds per propeller and 312 horsepower crossing the airframe with one
  engine out. The cost is not the shaft, it is that every gearbox takes power from either direction and
  the train becomes a single failure path
- **Power loading against disc loading**, 3.9 pounds per horsepower at 94.8 against 12.1 at 10, so a
  helicopter of the period lifted about three times as much per horsepower
- **The payload fraction**, 8.2 percent, which is the number that decides whether a configuration becomes
  a transport

---

## Verification

- **134 independent re-derivations across two verifiers, zero disagreements.** The corridor is solved by
  bisecting the vertical force balance rather than by evaluating an arctangent, the drag check is
  inverted to recover the maximum speed from the flat-plate area, and the crossflow parameter is
  recomputed from the bisected angle rather than carried over
- All 23 articles pass `check_any.py`, `_verify.py` at the 0-error 21-warning baseline, and the
  23-article isolated build succeeds with **25 of 25 equations rendering as display math**

---

## State

**A319 has had two of four passes.** The reference-density review and the publication review are yours to
prompt.

At 750 references it is already reference-heavy for a draft, and the primary pass should expect the same
inter-pass dependency this series keeps finding, since the equation pass has just promoted the corridor,
the crossflow parameter, lip separation, duct drag, transmission torque and disc-loading scaling, and
none of those was a topic when the harvest was designed.

Nothing in the series is published. The publication-order dependency is twenty-three deep.

**Still open and unchanged.** The fourth genre class. The A305 length offer.
