# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-11
**Task**: A333 equation-density review, the second of four passes. **Committed, not pushed.** **Not
published.**

**13 display equations to 28.** The article moved from 11,068 to 11,229 lines and from 59,364 to
60,869 words, with references unchanged at 3,467 definitions and all 3,352 master records still cited.

---

## The Pass Turned an Assertion Into a Budget

**The draft asserted that a fixed delay is amplified by 1.8898. Control theory turns that into
milliseconds, and the milliseconds force a conclusion about the architecture.**

A loop stabilising an unstable pole must cross over above it, and a pure delay costs phase in
proportion to frequency, so the entire delay budget of the loop is a phase margin divided by a
crossover frequency.

| Condition | Growth rate | Crossover | Budget, model | Budget, full scale |
|---|---|---|---|---|
| 110 kt | 0.802 /s | 2.41 rad/s | **326.3 ms** | 616.6 ms |
| 243 kt | 1.773 /s | 5.32 rad/s | **147.7 ms** | 279.1 ms |
| 243 kt, derived derivative | 2.518 /s | 7.55 rad/s | **104.0 ms** | 196.5 ms |

**The entire budget at maximum speed is between 104 and 148 milliseconds**, against a human visual
reaction time of roughly 250 on its own, before a camera, an encoder, a radio path or a display.

**So the ground pilot cannot have been inside the stabilisation loop, and the architecture follows from
arithmetic rather than from preference.** The inner loop had to be onboard with no radio in the path,
while the pilot flew the outer loop. **That is how the aircraft was built and the article did not have
to be told.** The full-scale aeroplane would have had 196 to 279 milliseconds, roughly a human reaction
time, **so a full-scale tailless aircraft could conceivably be hand-flown and the 28 percent model
could not.** That difference is entirely an artefact of scale.

---

## A Derived Derivative Replaced an Assumed One, and the Draft Was the Optimistic Case

The draft assumed a tailless directional derivative. **Slender-body theory gives it from the fuselage
volume alone**, through the apparent-mass difference.

| Fuselage volume | Per radian | Per degree |
|---|---|---|
| 0.60 m³ | 0.1041 | 0.001816 |
| 0.80 m³ | 0.1388 | **0.002422** |
| 1.00 m³ | 0.1734 | 0.003027 |

**The derived value is 2.018 times the assumed one**, so the aircraft was more unstable than the draft
implied, doubling times fall from 0.391 to 0.275 seconds at maximum speed, **and every conclusion that
survived the optimistic case survives the derived one more comfortably.** Both are carried through the
tables rather than one replacing the other.

---

## A Claim I Had to Withdraw

**The draft said the split ailerons were margin rather than necessity. The arithmetic does not support
that and I have corrected it.**

The drag increment of a split surface is not published, and across the plausible range the answer
flips.

| Drag increment | Share of the nozzle at 243 kt | Speed at which it equals the nozzle |
|---|---|---|
| 0.10 | 22.1 percent | 517.4 kt |
| 0.30 | 66.2 percent | 298.7 kt |
| 0.60 | **132.4 percent** | **211.2 kt** |

**The bracket spans a factor of six and the conclusion flips inside it**, so the honest statement is
that public information does not determine it. **What survives is the structural claim**, which needs
no increment at all: the nozzle's authority is flat with speed and the drag rudder's rises as the
square of it, so **the nozzle owns the low-speed end and the split ailerons own the high-speed end
wherever the crossover happens to fall.**

---

## A Third Witness for the Time Compression

**Turn performance was computable from the published load factor and I had not done it.**

| Speed | Turn rate | Radius | Rate at full scale |
|---|---|---|---|
| 110 kt | 48.64 deg/s | 67 m | 25.74 deg/s |
| 243 kt | 22.02 deg/s | 325 m | 11.65 deg/s |

Turn rate goes as one over speed and speed scales as the square root of the scale factor, **so turn
rate scales as 1.8898 again**. **Three different quantities, one factor, and none of them assumed it.**
The corner speed of 210.8 knots sits below the 243 knot maximum, so the aircraft could reach the most
demanding point of its own manoeuvre envelope.

---

## One Weak Check That Passes and Is Reported as Weak

The fuel load and the mean sortie imply a fuel flow of 356.9 pounds per hour and **a thrust specific
fuel consumption of 0.510**, which is right for a small turbofan and would not be if either published
figure were badly wrong. **The article says it is a weak check rather than dressing it up.**

---

## Two Defects the Pass Produced and the Tooling Caught

**An all-remaining marker placed before a fixed-count marker for the same cluster drained it**, and the
assembler refused to emit an empty list, which is exactly the guard the handoff documents. **The
distinction between a count-zero marker finding nothing and a fixed-count marker finding nothing is
what saved this**, and the guard earned its place.

**A display equation was glued onto the following prose** by one of my replacements, which the lint
caught as `math-multiline`. It would have rendered as an equation with a paragraph inside it.

---

## The Promotion Rule, Sixteenth Article Running, for the Next Pass

**Six of the seven subjects the new equations name are thin and two stand at literally zero.**

| Newly promoted subject | Records | Period | Modern |
|---|---|---|---|
| **Phase margin and delay margin** | **0** | 0 | 0 |
| **Specific fuel consumption** | **0** | 0 | 0 |
| Munk moment and slender-body theory | 1 | 1 | 0 |
| Sutherland viscosity | 1 | 1 | 0 |
| Unstable pole stabilisation limits | 4 | 2 | 2 |
| Turn performance and corner speed | 4 | 2 | 2 |

**Phase margin at zero is the worst of these, because it now carries the article's headline result.**
`citation_gaps` reports 11 displayed equations with no citation within nine hundred characters. **Both
lists are the primary pass's work and are recorded rather than acted on.**

---

## Verification

- `python3 tmp/a333/verify.py` **99 of 99**, up from 59. New routes include bisecting for the fuselage
  volume that produces the derived derivative, **scanning the delay upward until the phase at crossover
  breaches the margin**, which is how a designer reads a Bode plot rather than how the article states
  it, bisecting for the drag-rudder crossover across the bracket, and a randomised property for the
  budget's scaling.
- `python3 _verify.py` **0 errors, 21 warnings**, taken from the repository root.
- `python3 tmp/errata/check_any.py` **0 failures, 0 warnings**.
- **Isolated 37-article build exit 0**, page 840 KB, **28 open and 28 close display-math delimiters
  matching the equation count exactly**, zero unexpanded markers, zero nested empty lists, zero
  blockquotes.
- **The comma-spacing trap fired again**, on a wing loading present only inside a display. Stated in
  prose as well.

---

## Next

**A333 pass three**, the primary-reference review, on your prompt. The two subjects at zero are the
priority, and phase margin is the one the article most needs.
