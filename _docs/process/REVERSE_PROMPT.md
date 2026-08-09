# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A319, the Bell X-22A, drafted. The first of four passes. **Committed, not pushed. Not
published.** Twenty-three of seventy-two articles now drafted, all in `_drafts/`.

**1,003 lines, 13 display equations, 750 references, 6,630 words.**

---

## The Keystone. The Shroud Pays Twice, in Opposite Directions

Ducted momentum theory with an exit area ratio $\sigma$ gives $T \propto \sigma^{1/3}$, and an open
propeller is the case $\sigma = 1/2$ because its wake contracts to half the disc area. So a duct that
merely prevents that contraction returns

$$\frac{T_{\text{duct}}}{T_{\text{open}}} = 2^{1/3} = 1.26$$

**Twenty-six percent more static thrust for the same power, from a ring of metal that does no work.**
That is what makes a seven-foot propeller viable at ninety-five pounds per square foot of disc loading.

The same shroud held at incidence during conversion behaves as an annular wing. Its normal force peaks
at **3,941 pounds against a duct thrust of 3,650**, a ratio of 1.08, at 130 feet per second. **That is
the middle of the conversion**, where the wings are not yet working and the ducts no longer point at the
ground.

---

## The Strongest Check. The Quoted Margin Is Not a Margin

The programme is described everywhere as having 35 percent excess power so it could hover with an engine
out. **That is not a safety margin. It is the smallest number that makes three-engine hover possible**,
because

$$\tfrac{3}{4} \times 1.35 = 1.0125$$

One and a quarter percent. And the reading is checkable, because it fixes the figure of merit at 0.716,
which is an ordinary value for a ducted lift fan. Feeding that back through momentum theory predicts the
weight three engines can lift as **14,721 pounds against the 14,600 the programme quotes separately**.

**Agreement to 0.83 percent, from a press figure and a momentum calculation that share nothing.**

At maximum takeoff weight the aircraft could not hover on three engines at all, and had 1.6 percent in
hand on four.

---

## The Series Thread. Cross-Shafting Answers the X-18

Losing one of four ducts applies

$$M = 3{,}650 \times 19.62 = 71{,}600\ \text{ft}\cdot\text{lbf}$$

of rolling moment. **Cross-shafting adds no power. It converts an engine failure from a control
emergency into a performance shortfall spread over four ducts.** The X-18 had two engines with no
interconnection and died of the asymmetry rather than the shortfall. The X-22 was designed so the
asymmetry cannot happen.

---

## What the Aeroplane Became

It flew from 17 March 1966 to October 1984. **Eighteen years, longer than the X-1, X-2 and X-15 put
together.** One of the two aircraft was lost in August 1966 to a propeller-control failure, and the crew
survived, which is more than the X-18 managed with the same class of failure.

From 1968 the survivor carried a variable-stability system from the Cornell Aeronautical Laboratory. It
stopped being a prototype of a configuration and became a flying simulator of configurations that did
not exist. **What it produced was not data about four-ducted aeroplanes but data about how any
vertical-takeoff aircraft ought to handle.**

**It is the only aircraft in this series so far that was rescued by repurposing.** The X-18 was scrapped,
the X-19 crashed, the X-20 was cancelled and the X-21 became a photographic target. The X-22 is the only
one of them still whole.

---

## A Ducted Propeller Belongs to Three Fields

**Aeronautics, naval architecture and wind energy.** The Kort nozzle is a duct round a ship's propeller
with a large old literature. The diffuser-augmented wind turbine is a ducted rotor with the same
momentum theory and no relevance here.

Twenty-one marine records were read out of the pool at the first scan and **four more survived into the
fourth check**, including a ducted propeller for submarines and a ducted Archimedes screw turbine. This
homonym is more persistent than the A315 propeller case because the marine device is not merely
similarly named, it is the same device.

**Three near-misses went the other way and were kept.** The United States **Marine** Corps is not marine
engineering, **Building** Credible Flight Models is not building aerodynamics, and helicopter shipboard
landings are aircraft work.

---

## Verification

- **65 independent re-derivations, zero disagreements.** The verifier builds the ducted momentum result
  from the exit condition rather than the closed form the article displays, obtains the figure of merit
  by bisection rather than division, and inverts the weight numerically rather than with an exponent
- **One imprecision caught and corrected.** The normal-force table samples every twenty feet per second,
  and its maximum row is not the continuous maximum. The peak is at 130 feet per second, not 120, and
  the article now states both
- 750 references, zero undefined, zero orphaned, zero duplicate URLs
- **625 DOIs confirmed registered in Crossref and 105 archive links at HTTP 200, zero failures**
- All 23 articles pass `check_any.py`, `_verify.py` at the 0-error 21-warning baseline, and the
  23-article isolated build succeeds with 13 of 13 equations rendering as display math

---

## State

**A319 has had one of four passes.** The three remaining are yours to prompt.

At 13 equations it is the lightest draft in the series so far, and deliberately so. **The equation pass
has a great deal to work with**, since the conversion corridor, the tandem interference, the duct
pitching moment and the transmission torque are all named in the draft and none is computed.

Nothing in the series is published. The publication-order dependency is twenty-three deep.

**Still open and unchanged.** The fourth genre class. The A305 length offer.
