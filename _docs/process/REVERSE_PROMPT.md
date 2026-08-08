# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-07
**Task**: A310 equation-density pass, the second of four. Committed and **not pushed**. **Not
published.** All fourteen articles in the series remain in `_drafts/`.

---

## The Pass Found an Imprecision in the Article's Own Framing

The opening said the two control systems "cross exactly once" and then computed a crossing at 48.2
metres per second. **Those are two different crossings and the article was using one sentence for
both.**

The speed at which the elevons produce as much moment as the deflected thrust is

**94.7 metres per second**, well above the stall speed.

The speed at which they produce enough moment to meet the control-power criterion is 48.2. The second
is the one that matters, because a vehicle needs adequate control rather than maximal control, and
the article now separates them explicitly in the section that introduces the problem.

The consequence is a more honest picture of the handover. Tabulating the aerodynamic share of the
available authority shows that **at the speed where the elevons first become adequate they still
supply only a fifth of what is there**, and the nozzle is doing the rest. The handover is gradual and
a single crossover speed overstates how sharp it is.

---

## Three Results That Changed What the Article Says

**The design spiral has a direction and it is unforgiving of size.** The required moment scales as
$mL^2$ and the available moment as $mL$, so the ratio grows linearly with length. **Doubling the
length doubles the fraction of the engine that attitude control consumes**, taking the puffer bleed
from 4.5 percent to 9.0 and then 13.5 at three times scale. That is a stronger statement than the
draft's, and it sits beside the earlier finding that the crossover ratio is scale-independent without
contradicting it. **The speed at which the controls become adequate does not care about size. The
cost of making them adequate does.**

**A tumble is stopped in half a second with the engine running and cannot be stopped at all without
it.** Writing the recovery as an angular momentum problem gives 0.52 seconds and 14.8 degrees of arc
at one radian per second. Both the nozzle and the puffers are powered by the engine, so an engine
failure removes every means of attitude control simultaneously. **That is why a spin recovery
parachute was tested**, and it is the sharpest illustration in the article of what it means to
control an aircraft with its propulsion.

**Froude scaling explains why the models worked and where they stopped.** A one-fifth free-flight
model flies at 23.5 metres per second, completes the transition in 2.19 seconds over 25.6 metres, and
weighs 24.4 kilogrammes. Everything happens **2.24 times faster** than full scale, which is the
practical difficulty. The Reynolds number is **11.2 times lower**, so the model's boundary layer is
not the aircraft's, and that is exactly the division between what the models settled, which is
inertia and thrust, and what they did not, which is the stall.

---

## The Largest Exposure Is Now Tabulated

The crossover speed varies as the inverse square root of the assumed elevon effectiveness, and the
draft stated that in words. Tabulating it shows the exposure plainly. **If the elevons were half as
effective as assumed the crossover would sit thirty percent above the stall speed and the article's
central claim would invert.** That is the single largest exposure in the analysis and it rests on a
coefficient nobody measured for this aircraft.

---

## The Contemporary Result Worth Keeping

The article's hover endurance relation has no length in it. Writing the electric analogue out gives a
different relation, because a rotor's power depends on disc loading rather than on fuel, and
evaluating it for a rotor of the X-13's own span with a battery at the same seventeen percent mass
fraction gives **8.2 to 10.9 minutes against the X-13's eleven on kerosene**.

**The battery's specific energy is roughly forty times worse than kerosene's and the rotor's hovering
efficiency roughly forty times better, and the two cancel almost exactly.** That is a coincidence
rather than a law, and it is flagged as such, but it is the reason the hover endurance problem feels
as intractable now as it did then.

---

## Smaller Additions

The nozzle's rolling moment is **identically zero as a cross-product identity**, not merely small.
Holding station in a ten metre per second crosswind requires a steady tilt of **0.94 degrees against
a drift budget of 0.47**, so the two tasks conflict by a factor of two on the same actuator. The
landing point bears **135 degrees from a tail-sitter pilot and about 45 from a horizontal jet-lift
pilot**, and no seat pivoting closes that gap because the difference is which end of the aeroplane
points at the ground. Deleting the undercarriage is worth **1.94 to 3.22 minutes of hovering**. The
modern control-allocation solution is written out, and the fraction the article tabulates is what it
converges to.

---

## Verification

All 268 worked values re-derived independently, including every equation-pass addition, with **zero
disagreements**. `_verify.py` at the 0-error 21-warning corpus baseline. Zero contractions,
em-dashes, en-dashes, prose colons, prose semicolons, prose parentheticals, doubled words, duplicate
headings, unbalanced emphasis markers, lone dollar-delimited lines, or adjacent display-math seams.
Isolated build succeeding with **91 rendered display blocks matching the source count exactly**, Part
14 navigation, twenty-one tables, no unresolved reference links and no surviving Liquid tags.

The structural audit leaves five sections above 150 words without equations and all five are
legitimately narrative, namely the opening, the programme-origin narrative, the source base, the
Epistemic State, and the conclusion.

---

## State

**1047 lines, 91 display equations, 143 reference definitions, 13,590 body words.**

**Equations are inside band at 91 against 90 to 130.** Lines are 253 below the 1300 floor and
references 107 below the 250 floor, both reported rather than padded.

---

## The Warning From the Draft Pass Still Stands

**The master pool holds only 665 entries against A309's 3,597**, of which 522 are unused. That is
very unlikely to support the 250 reference floor. **The primary pass should begin with a
supplementary harvest rather than with a citation-coverage audit**, which reverses the usual order,
and the productive queries are likely to be the XFY-1 and XFV-1 literature, the handling-qualities
series, and jet lift generally rather than anything naming this aircraft.

**Committed, not pushed.** Fourteen articles drafted of seventy-two, none published. The
publication-order dependency is fourteen deep, A310 back to A297. **Categories remain undecided** at
`aerospace history engineering`, fourteen articles deep and raised eighteen times.
