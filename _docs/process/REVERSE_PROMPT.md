# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-07
**Task**: A310 draft pass, the first of four. Committed and **not pushed**, per the rhythm. **Not
published.** All fourteen articles in the series remain in `_drafts/`.

---

## The X-13 Ends the Run of Five

The X-8 through the X-12 were sounding rockets, missiles, and ballistic weapon articles. **The X-13
is a manufacturer's prototype built in two examples under a research contract, flown by company test
pilots, with no operational intent and no production plan**, which is exactly the pattern the X-1
established.

That is worth more than a note, because it constrains the closing article. **The run of five was an
interruption and not a redefinition.** A synthesis that describes the series as having drifted from
research aircraft to weapons would be contradicted by its own next entry, and the article says so.

---

## The Keystone

**Control authority through the transition.** An aeroplane is controlled by moving air over surfaces,
and at zero airspeed there is none, so the aerodynamic moment scales with the square of speed while
vectored thrust does not depend on speed at all. **The two cross exactly once** and the aircraft must
be controllable on both sides and at the crossing.

Neither of the previous two articles could have posed this question, because neither vehicle was ever
at zero airspeed while airborne.

---

## The Central Result, and Why It Is Not Luck

The elevons meet the control-power criterion at **48.2 metres per second against a stall speed of
52.5**, so the control surfaces become adequate at **91.8 percent of the speed at which the wing
starts flying**. Vectored thrust supplies 3.86 times the criterion everywhere below it.

Writing the ratio out shows why that is not a coincidence. The wing area cancels and the air density
cancels, leaving a function of the pitch inertia over the weight divided by the mean chord. **The
ratio is a property of proportions and not of scale**, which is also why a one-fifth-scale model
could demonstrate the same handover, and why the layout has outlived the aeroplane.

---

## Findings the Sources Do Not State

**The three axes hand over in sequence rather than together**, at 0.62 of the stall speed for yaw,
0.72 for roll, and 0.92 for pitch. A pilot accelerating through the transition feels the aircraft
become conventional one axis at a time, and for a band of about sixteen metres per second he is
flying a machine that is aerodynamic in two axes and reactive in the third.

**The entire fuel load is about eleven minutes of hovering.** Hover endurance is fuel fraction
divided by specific consumption and therefore depends **not at all on the size of the aircraft**.
There is no scale at which the problem improves, which is unlike most aircraft design constraints.

**The transition costs 12.6 pounds of fuel and 4.9 seconds.** The manoeuvre the entire programme
existed to demonstrate is about one percent of the fuel and the hovering that brackets it is
everything else. **A cautious profile spends 54.6 percent of the fuel without leaving the airfield.**

**Hovering is a third-order position loop with no restoring moment anywhere in it**, and holding
position to a metre over five seconds requires holding the mean tilt below **half a degree**. That is
the actual task and the control-power criteria do not capture it.

**The wind is a position problem, not an attitude problem.** A ten metre per second crosswind is 7.0
percent of the pitch requirement as a moment and 72 metres of drift in thirty seconds as a position
error.

**The ground observer was part of the control loop.** The man who talked the pilot down is better
understood as a delayed sensor inside an undamped third-order loop, and 0.3 seconds of delay consumes
the entire hook tolerance at one metre per second of closure.

**Deleting the undercarriage bought roughly a quarter more fuel**, so the trailer is a performance
decision rather than an eccentricity.

**A turboprop tail-sitter hovers with roughly stall-level dynamic pressure already on its control
surfaces and a turbojet tail-sitter hovers with none.** That single ratio is the whole design
difference between the X-13 and the XFY-1, and it is why one needed reaction controls and the other
did not.

---

## An Error, and a Defect

**The first writing said a one-fifth-scale model imposes a twenty-fifth of the ground pressure.** For
geometric scaling at fixed thrust to weight the thrust goes as the cube of length and the nozzle area
as the square, so disc loading goes as the **first** power. It is one fifth. That is the sixth
article running in which writing a relation down caught arithmetic the draft carried as an assertion.

**A section ordering defect was found and fixed.** The three-axis summary table cited a roll
crossover derived two sections later. The Roll section was moved ahead of Yaw so the figure is
established before it is used.

---

## Two Method Notes

**The master table is built from the A310 harvest alone.** The generator inherited from A309 read
both the current and the previous article's directories, which was right when the X-12 shared an
airframe with the X-11 and would here have imported six hundred documents about ballistic missiles
into an article about a tail-sitting jet.

**The archive lesson repeats in a new form.** Querying NASA's technical archive for `X-13 Vertijet`
or `vertijet` returns **nothing at all**, and `Ryan X-13` returns the spin-tunnel series and the
one-fifth-scale hovering and transition tests. The vehicle is indexed under the name its engineers
used and not the name the public learned, which is the X-10 project-number lesson wearing different
clothes.

---

## Verification

All 176 worked values re-derived independently with zero corrections beyond the one described. **45
of 45 fixed identifiers at 200, 82 of 82 DOIs Crossref-resolved on title at the 0.85 threshold with
zero flagged**, 130 URLs with zero duplicates, no hand-entered identifier anywhere. `_verify.py` at
the 0-error 21-warning corpus baseline. Zero contractions, em-dashes, en-dashes, prose colons, prose
semicolons, prose parentheticals, doubled words, duplicate headings, unbalanced emphasis markers,
lone dollar-delimited lines, or adjacent display-math seams. All twenty insertion seams read by eye.
Isolated build succeeding with **56 rendered display blocks matching the source count exactly**, Part
14 navigation, eleven tables, no unresolved reference links and no surviving Liquid tags.

---

## Draft State

**810 lines, 56 display equations, 143 reference definitions, 11,369 body words.**

All three densities approach their bands from below, which is the rule. `aircraft` at 8.83 and
`control` at 5.52 per thousand body words are the subject and keystone nouns and are reported rather
than remediated.

---

## A Warning for the Primary Pass

**The master pool holds only 665 entries against A309's 3,597**, of which 525 are unused. That is
very unlikely to support the 250 reference floor. **The primary pass should begin with a
supplementary harvest rather than with a citation-coverage audit**, which reverses the usual order,
and the productive queries are likely to be the XFY-1 and XFV-1 literature, the handling-qualities
series, and jet lift generally rather than anything naming this aircraft.

Primary sources are already 77 of 126, or 61.1 percent of dated, and contemporary references are
already 47, so the contemporary gap that dominated A309 does not exist here.

---

## State

**Committed, not pushed.** Fourteen articles drafted of seventy-two, none published. **The
publication-order dependency is fourteen deep**, A310 back to A297.

**Categories remain undecided** at `aerospace history engineering`, fourteen articles deep and now
raised eighteen times.
