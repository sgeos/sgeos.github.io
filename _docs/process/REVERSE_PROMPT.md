# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-11
**Task**: A332 equation-density review, the second of four passes. **Committed, not pushed.** **Not
published.**

**30 display equations to 71.** The article moved from 18,396 to 18,723 lines and from 98,627 to
101,571 words, with references unchanged at 5,814 definitions and all 5,678 master records still
cited.

---

## Four Pieces of Physics the Draft Did Not Reach, and Every One Serves the Thesis

The draft argued that the conversion between modes was the hard event and that the three celebrated
manoeuvres were not. **It argued that from a chronology. The equation pass gives it forces.**

### The force that appears the moment the fan engages

**A lift fan in forward flight ingests air at flight speed and throws it downward, so all of that
horizontal momentum has to be destroyed.** The reaction is a drag, $D = \dot{m} V$, and it is large.

| Speed | Momentum drag | Share of the rear nozzle's thrust |
|---|---|---|
| 80 kt | 2,431 lbf | 13.5 percent |
| 180 kt | **5,469 lbf** | **30.4 percent** |

**The X-35B made its first in-flight conversion at 180 knots**, and at that speed engaging the fan
costs 5,469 pounds force and decelerates the aircraft at 0.1609 g on its own. **Nothing about hovering,
going supersonic or landing vertically produces a step change of that size.**

### The same relation read upwards gives the conversion speed

Setting wing lift equal to the whole weight rather than to part of it gives **146.8 knots**, above
which the wing carries the aeroplane unaided. **The conversion was flown at 180 knots**, comfortably
clear, which is the safest place to engage a fan and also the point at which the momentum drag is
largest. **Lift was free and drag was most expensive, which is the right trade and not an obvious
one.**

### The hover balance fixes the centre of gravity

In a hover there is no airflow to trim against, so the only vertical forces are the fan ahead of the
centre of gravity and the rear nozzle behind it. Both thrusts are set by hardware, so **the moment
balance does not determine the trim. It determines where the centre of gravity has to be**, at 47.37
percent of the distance from one to the other. **A five percent thrust split buys 14.72 inches of
travel.** That is tight for an aeroplane whose fuel and stores move the centre of gravity by more, and
**it is the one cost in this article that does not get easier as the aircraft gets lighter.**

### What hot gas ingestion costs, in kelvin

**The fan is shaft-driven, so every pound of vertical thrust is ultimately core thrust.** Inverting for
the inlet temperature rise that consumes the hover margin gives **66.95 kelvin**. That single number is
what the cold fan buys, **and it converts the comparison with the rival from a matter of adjectives
into a matter of kelvin.**

---

## The Geometry Result, Which Was Not Anticipated

The three-bearing swivel module was a sentence in the draft. **The kinematics say why there are three
bearings rather than one.**

A joint whose mating plane is canted at $\beta$ deflects the duct by $\cos\delta = \cos^{2}\beta +
\sin^{2}\beta\cos\phi$, confirmed against a rotation-matrix composition over five thousand randomised
inputs. At half a turn that is $2\beta$, **so one joint would need a cant of 47.5 degrees to reach
ninety-five, which is not a practical pressure-tight seal on a duct carrying an augmented turbofan's
full exhaust.**

**Then the part I did not expect.** Putting joints in series helps **only if their cants alternate**. A
search over the roll angles found that two joints canted the same way reach $2\beta$ and no more,
because the second can only undo the first. **Mirrored, two reach $4\beta$ and three reach $6\beta$**,
so three alternating joints at an ordinary 15.83 degree cant reach ninety-five. **The bearing count
follows from the cant a seal can tolerate divided into the deflection the aircraft needs.**

The article claims the requirement and not the mechanism, since the actual cant angles and the gearing
are not published.

---

## The Counter-Rotation Finding, Now in Handling-Qualities Units

The draft said a single-rotation fan would have consumed most of the roll authority. **Dividing the
couple by an estimated roll inertia turns that into an angular acceleration.**

The posts give **46.07 degrees per second squared**, which is healthy. A single-rotation fan's reaction
torque is **93.31 percent of the whole couple**, leaving **3.083 degrees per second squared**.

**Three degrees per second squared is not a degraded control system. It is not a control system.** A
pilot would have had about one fifteenth of the roll acceleration the aircraft actually has.

---

## Two Refinements That Made a Number Worse and the Conclusion Stronger

**The draft asserted a lumped transonic drag coefficient of 0.035.** A build-up gives 0.03773, so the
drag is 10,289 pounds force rather than 9,546 and the thrust to drag ratio falls from 2.389 to
**2.216**. **The conclusion that Mach 1.05 was not demanding survives, and now rests on a build-up
rather than on a guess.** Induced drag is 0.0027 of the total, which is itself worth knowing, because
it means the dash is a pure zero-lift and wave-drag problem.

**The thrust lapse exponent is assumed and is now shown not to matter.** Across 0.6 to 1.0 the ratio
runs from 2.589 to 1.878 and the margin survives the whole range.

---

## One Symbol Collision, Caught by Reading

The relation for thrust loss with inlet temperature needs a thrust and a temperature in the same
expression, and the article has used $T$ for thrust throughout. **The first version silently wrote both
as $T$.** Thrust is now written $F$ in that relation and only there, and the article says so at the
point of use.

I also removed a claim that the momentum drag appears in no account of this aeroplane, which I cannot
support, and corrected a statement that two derivations of the fan mass flow agreed to a part in five
hundred. **They are algebraically the same statement**, so the agreement tests transcription rather
than physics, and the article now says that instead.

---

## The Promotion Rule, Fourteenth Article Running, and This Is for the Next Pass

Auditing the ten subjects the new equations name against the pool found **seven thin and one at
literally zero.** The two carrying the sharpest new results are the worst.

| Newly promoted subject | Records | Period | Modern |
|---|---|---|---|
| **Momentum drag of a lift system** | **1** | 0 | 1 |
| **Canted joint kinematics** | **1** | 0 | 1 |
| Fan stage loading and tip Mach | 1 | 1 | 0 |
| Centre of gravity limits in hover | 2 | 0 | 2 |
| Induced drag and span efficiency | 4 | 3 | 1 |
| Barometric and standard atmosphere | 8 | 3 | 0 |
| **Fuel volume and density** | **0** | 0 | 0 |

`citation_gaps` reports 25 displayed equations with no citation within nine hundred characters.
**Both lists are the primary pass's work and are recorded here rather than acted on now.**

---

## Verification

- `python3 tmp/a332/verify.py` **115 of 115**, up from 53, by an independent verifier that does not
  import the calculation. New routes this pass include a **rotation-matrix composition tested against
  the closed form over five thousand randomised inputs**, a search over the roll space for what series
  joints can do, bisection for the critical inlet temperature rise and for the wing-borne speed, a
  scan for the centre-of-gravity band, the fan mass flow by a second route, and the ground roll in
  closed form against the time-stepped figure already checked.
- `python3 _verify.py` **0 errors, 21 warnings**, the baseline.
- `python3 tmp/errata/check_any.py` **0 failures, 0 warnings**.
- `python3 _lib/test_lib.py` **53 of 53**.
- **Isolated build exit 0**, and the rendered page carries **71 open and 71 close display-math
  delimiters**, matching the equation count exactly, with zero unexpanded markers, zero nested empty
  lists and zero blockquotes.
- **The comma-spacing trap fired again, fifth consecutive article.** Seven verified values were present
  only inside displays, where LaTeX comma spacing flattens `29{,}018` to `29{}018`. All seven are now
  stated in prose as well.

---

## Next

**A332 pass three**, the primary-reference review, on your prompt. The seven thin subjects above are
the list, and the two at one record each are the ones the article most needs, since they carry its
newest results.
