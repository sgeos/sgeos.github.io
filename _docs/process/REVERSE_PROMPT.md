# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A316 primary-reference review, the third of four passes. Committed, **not pushed**, per the
rhythm. **Not published.** All twenty articles in the series remain in `_drafts/`.

---

## Something You Need to Decide On, in A315 Rather Than A316

This pass found a false-positive family I had not met before, and **A315 has four of them in its
committed draft.**

A propeller in oblique inflow is a live research subject in **naval architecture**, where it means a ship
screw meeting the wake of a hull at an angle. It uses this article's exact vocabulary. The first
selection run returned eight candidates for the keystone topic and **all eight were marine.**

Filtering on the journal name rather than the title removed them. Two still got through and were caught
by reading. One is David Taylor Model Basin work on the spindle torque of a controllable-pitch **ship**
propeller. The other is the open-water characteristics of propeller 4739 designed for **LSD-41, a dock
landing ship**, which reached a section on vertical-flight handling qualities because my selection
pattern for controllability matched the phrase controllable pitch.

**A315 cites both, in the same sentence, plus two more.** Wing sails for wind-assisted ship propulsion,
and cavitation of a propeller under a non-uniform wake. Worse, A315's reverse prompt singles the spindle
torque paper out as **"directly about the system that failed on the final flight."** It is about ship
propellers.

**I have not touched A315, because it is outside what you asked for.** Say the word and I will remove the
four citations and correct that claim. It is four anchors and one sentence.

---

## My Own Scan Was Wrong in the Other Direction, Twice

Worth recording because it is the third article running.

**My first venue filter rejected the entire AIAA Guidance, Navigation and Control conference series**,
because I listed the bare token `navigation` for the marine navigation journals. Among the records it
silently discarded were optimal tiltrotor operations with one engine inoperative and an energy-optimal
speed profile for a **tandem tilt-wing** aircraft, which is this article's exact configuration. Fifteen
relevant records were recovered by narrowing the rule.

**Then my A315 scan over-flagged in the same way**, calling a NASA ducted-fan propulsor study, an
aircraft rudder paper and a ring-wing tail-sitter marine. Three false alarms in seven.

**A filter is only as trustworthy as the last time somebody read what it threw away**, and I only found
either problem by reading the rejected list rather than the accepted one.

---

## The Audit Found Both Kinds of Gap at Once

That has not happened before in this series and the two have opposite fixes.

**Five topics were genuinely thin because the draft harvest was never aimed at them, and all five carry
relations the EQUATION pass added.** High advance ratio propellers at seven records, blade loading at
five, ejection systems at two, inertias at two, drag at twelve with none cited. A targeted harvest took
them to 29, 31, 25 and five. **That is the A315 inter-pass dependency arriving on schedule rather than as
a surprise.**

**The rest were deep and barely used, which no search would have fixed.** Transition held 268 records
against 18 cited, the slipstream 96 against eight, the tandem wing 69 against six. Spreading the
selection was the whole of the work.

**One topic stays thin and is reported rather than padded.** Aircraft moments of inertia returned five
records, because mass-properties reports are working documents archives rarely index. All three inertias
therefore rest on assumed radii of gyration, and the Epistemic State says so.

---

## What the New Material Actually Adds

**The keystone's own literature turns out to be a standing NACA programme.** Wind-tunnel measurement of
how a running propeller moves an aeroplane's neutral point ran through the 1940s and 1950s. Every one of
those reports treats the propeller force as a correction to design around. **Curtiss-Wright proposed to
change its sign in the accounting rather than its magnitude in the physics.**

**A 1947 wind-tunnel investigation of the effect of HIGH SOLIDITY on propeller characteristics at high
forward speed** asks exactly the question the X-19's blade answers, sixteen years before it flew.

**Three references are about this machine's near relatives**, being four-duct tandem vertical take-off
configurations, tandem tilting ducted-propeller control augmentation, and downwash tests of dual tandem
ducted-propeller aircraft. The ducts differ and the longitudinal arrangement does not.

---

## Verification

**119 independent re-derivations, zero disagreements**, still reproducing after every edit. 274
references, 255 external URLs, zero duplicates or orphans. 162 plain 200s, 45 publisher 403s, and **17
DTIC DOIs verified through the Crossref registry with matching titles.**

A red-flag scan of all cited titles **and venues** returned zero hits after the two removals. `_verify.py`
at the 0-error 21-warning corpus baseline. Zero style violations. Isolated build passing with 78 of 78
display blocks rendering as display, 2 of 2 tables, Part 20 navigation. Equation count measured before
and after and holding at 78.

---

## State

**Committed, not pushed**, which is correct for this pass. **937 lines, 78 display equations, 274
references, 9,408 words.** Research citations are **242, all of them primary or period**, with zero
contemporary, which is deliberate. Era spread is 67 pre-1960, 112 across the 1960s and 1970s, 57 in the
1980s and 1990s, and eight after 2000.

**References are now inside the 250 to 380 band.** Lines sit 363 below the 1,300 floor and equations 12
below the 90 floor, which is the same shape A313 to A315 finished in. The publication review is the
remaining pass and contemporary coverage is its work.

---

## The Pass Caught Two Errors in the Drafted Text

**33 display equations to 78, across 22 edits**, every one asserted to match its anchor exactly once and
every section extended in place rather than replaced.

**The pitch-moment relation was wrong by a factor of two.** The draft displayed $M = fT\ell$, which
evaluates to 30,934 foot-pounds, while the prose beside it quoted 15,467. **The quoted value was right
and the displayed algebra was wrong**, so the article contradicted itself and every automated check
passed it. Shifting a fraction of thrust between stations raises one by $fT/2$ and lowers the other by
the same, so the correct form is $M = \tfrac{1}{2} f T \ell$.

**The yaw inertia was transcribed as 100,565 and computes to 100,690.** The acceleration built on it was
right, so this was a prose slip rather than a modelling error, and it is exactly what displaying
$I_{zz} = m k_z^2$ with both factors visible prevents.

**That is twelve consecutive articles in which writing the relation down caught a wrong claim.**

---

## The Review Introduced a Defect of Its Own

One of my new blocks was missing its closing delimiter. It would have rendered as broken mathematics, and
**it was invisible to every existing check**, because it is not a lone delimiter and the display-equation
regex simply fails to match it, so it was not even counted as an equation. I found it in the adjacent-math
warnings rather than by looking for it.

`check.py` now fails on any line that opens with a display delimiter and does not close with one. The
checks need the same discipline as the thing they check, which is the A315 lesson arriving in a new form.

---

## The Handoff Was Right and the Keystone Does Not Transfer

You warned me not to assume the X-18's keystone carried over, and it does not. **A tilt-wing must keep
its wing flying at absurd angles, so slipstream immersion is everything. A tilt-propeller never rotates
its wing at all.**

What is astonishing about the X-19 instead is the size of its wings. **154.6 square feet carrying 13,660
pounds, a wing loading of 88.4 pounds per square foot in an aircraft required to land vertically.** The
wing alone stalls at 136.5 knots, so it cannot carry the aircraft at any speed below that.

**The keystone is the propeller normal force**, meaning the force a propeller develops at right angles to
its own axis in oblique flow. Curtiss-Wright called it the radial lift force and sized the wing around
it. Its literature is Ribner's wartime work on propellers in yaw, which is **aerodynamic stability
literature from 1943 to 1945, eighteen years older than the aircraft**. A pool imported from A315 would
not have contained a line of it, which settled the one-directory question on its own.

---

## The Wide Blade Is Demanded Twice

The best result in the article. The X-19's propellers had famously wide blades and the usual explanation
is radial lift.

The 400-knot cruise caps the helical tip Mach number, which caps the rotational tip speed at **644.2 feet
per second, or 946 revolutions per minute**. Hovering at that tip speed then requires a solidity of 0.211
and a blade chord of **17.2 inches on a 13-foot propeller**, against about 7 inches for a conventional
one. **That calculation never mentions radial lift.** The wide blade is forced by two requirements that
were going to be imposed anyway, and the radial lift force arrives with it.

Feeding the chord back through Ribner's fin analogy fixes the one free parameter, the in-plane momentum
fraction, at **0.283 from geometry rather than by assumption.**

---

## A Result That Cuts Against the Article's Own Thesis

I want to flag this rather than bury it, because it is the finding I did not expect.

The propellers do supply **29.8 percent of the lift slope in cruise**, and without the radial lift force
the X-19 would have needed about **225 square feet at 61 pounds per square foot**, an ordinary transport
wing loading. Two independent routes to that number, one ignoring drag entirely and one from the fully
trimmed corridor, **agree to 3.5 percent**.

**But the conversion corridor is continuous with the effect switched off.** Higher speeds, narrower
bands, still continuous. So the radial lift force is **not** what made the X-19 possible. It made the
wing smaller. The article says so plainly in a section titled for it, because the opposite claim was the
one the configuration was sold on.

---

## The Cure and the Cause of Death Were the Same Component

The X-18's fatal deficiency was two engines with no interconnection. The X-19 had the interconnection,
and losing both propellers on one side is an upset of **1.67 times full roll control**, so the
cross-shaft was not a refinement. **The cross-shaft is also the gearbox that destroyed the aircraft.**

Two further control findings. The tandem layout supplies for nothing the pitch control that the X-18
needed a turbojet to obtain, at 35.9 degrees per second squared. **Yaw is an order of magnitude short**
at 1.99 degrees per second squared, which is a candidate explanation for the recorded control system
problems rather than an answer, since differential nacelle tilt is not excluded.

---

## Two Defects Found by Reading, Not by Checking

**The corridor was circular and returned nonsense.** The first formulation solved the vertical
equilibrium equation for thrust and then tested the same equation, which is satisfied identically at any
speed. It reported **0.6 knots at every nacelle angle below 60 degrees**. Nothing flagged it. Eliminating
thrust between the two equations instead gives a residual that is well scaled everywhere.

**The isolated build script arrived one stub short.** The copy carried eighteen predecessors and A316
needs nineteen, so the `post_url` to A315 had no target and **the entire build failed**. That is the
interlock behaving exactly as designed, and it is the copied-script defect in its purest form. I also
found and fixed the two-clause navigation check, both clauses, per the A314 lesson.

**One model inconsistency fixed rather than carried.** A figure of merit of 0.70 and a propeller
efficiency of 0.80 were being used for what the momentum model treats as one quantity. The corridor is
now reported across both.

---

## What This Article Cannot Do

**There is no flight data from the regime the aircraft was built for.** Fifty flights, four hours, and
**no transition was ever attempted**. Comparison With Ground Prediction therefore reports the absence
rather than a comparison, and every cruise number in the article is a prediction with no X-19
measurement against it. The only confirmation belongs to the X-100, which transitioned once in 1960.

I also state where my own model stops deserving belief. The in-plane momentum picture is defensible to
about 60 degrees of disc incidence, and **five of the ten corridor rows sit outside that**, reaching 89.5
degrees at the hover end.

---

## Verification

**119 independent re-derivations, zero disagreements**, from a verifier that integrates the atmosphere by
trapezoidal rule where the model uses the analytic layer solution and uses closed forms where the model
bisects. All 115 quoted values confirmed present in the text, a check that flagged the stale 100,565 as absent
once the correction landed.

79 references, 60 external URLs, zero duplicates or orphans. URL sweep at 38 plain 200s, 10 publisher
403s, and **3 DTIC DOIs verified through the Crossref registry** with matching titles. `_verify.py` at
the 0-error 21-warning corpus baseline with no new warnings. Zero style violations. Isolated build
passing with 78 of 78 display blocks rendering as display rather than inline, 2 of 2 tables, and Part 20
navigation.

---

## State

Superseded by the state section above.

Twenty of seventy-two articles. The publication-order dependency is now **twenty deep** and every
cross-reference points backward.

**On the fourth genre class.** A316 now sits at **78 equations against the 90 floor and 688 lines against
the 1,300 floor**, with two passes still to run. A313 to A315 each ended below both. This one is closer on
equations at the equivalent stage than any of those three were, so I would not treat it as further
evidence for a new class yet. The reference and publication passes are yours to prompt.

**Ten sections remain flagged by the density scan and I judge all ten correct as they stand.** They are
the opening, the programme history, and the closing analytical sections, which quote numbers derived
elsewhere in the article rather than relying on relations of their own. Padding them would be the defect
the standing directive warns against.
