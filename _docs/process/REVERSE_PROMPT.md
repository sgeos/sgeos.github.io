# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A321, the Martin Marietta X-24, drafted. The first of the four passes.
**Committed, not pushed.** Not published.

**Draft state 1,205 lines, 18 display equations, 855 references, 8,004 words.**

---

## The Keystone

**Can a pilot land a vehicle with a lift-to-drag ratio of three, without an engine, on a runway, on
purpose?** The answer was two landings on the Edwards concrete in 1975, and the quantity that makes the
question hard turns out to be base drag.

**A reentry vehicle must be cut off flat.** Hoerner's relation makes base drag fall as forebody drag
rises, so the two trade and there is an interior optimum. Differentiating that bucket gives a result
that contains none of its parameters:

$$C_{F_e} = x + 2x = 3x$$

**At the optimum, total drag is exactly three times forebody drag and the base contributes exactly
twice it.** Saltzman, Wang and Iliff quote 0.1284 and 0.3852, whose ratio is 3.000, which is the check
that the derivation is theirs rather than mine.

**The reference area cancels out of the lift-to-drag expression**, which is why the right independent
variable for a shape with no wing is span squared over wetted area.

---

## The Validation Was Not Fitted

**The Shuttle prototype Enterprise flew truncated and with a tailcone over its blunt base.** That is the
same airframe with and without the penalty, which is as close to a controlled experiment as this subject
offers.

Covering the base removes two thirds of the drag, so it should buy exactly the square root of three in
lift-to-drag ratio. The prediction is **7.05 against a measured 7.5, six percent, from geometry alone.**

---

## The Verifier Overturned the Flare, and a Headline Claim With It

**This is the third pass running where the independent check has been right and the article wrong, and
this time it killed a finding I liked.**

The draft treated the flare as a circular arc at constant radius. But the vehicle decelerates through
the manoeuvre, so **the arc tightens as it goes**. An arc evaluated at entry speed is too long, which
overstates the work done against drag, which understates the touchdown speed. The error was nine percent
in height and twelve in speed.

**At low load factor it was not numerical but qualitative.** The crude model said a 1.2 g flare ran out
of speed entirely, and I had built a claim on it that the corridor was bounded below by energy
exhaustion. **Integrating the flare properly, 1.2 g touches down at 202 miles an hour, perfectly well.**

Integrating instead, and solving for the load factor from the quoted touchdown speed rather than
assuming one:

**1.19 g. The flare begins 2,125 feet up and lasts 21.5 seconds.** A transport begins at thirty feet and
is done in three, so **the X-24B began its flare seventy times higher**, and covered 9,460 feet of
ground track doing it, more than half the runway it was aiming at.

**The corridor survives but the lower bound is stall, not exhaustion**, at about 1.07 g, and it is about
four tenths of a g wide. **The hold-off segment the draft claimed was demanded by arithmetic is gone**,
because the corrected flare reaches 200 miles an hour unaided.

---

## A Source Conflict Worth Naming

**Several accessible sources give the X-24A and the X-24B identical dimensions**, which cannot be right
for a vehicle that was rebuilt half again as long. The flight-determined table settles it, and as a side
effect it **independently confirms the X-24A figures A320 used** for its reference-area derivation,
namely 24.50 feet, 13.63 feet and 195.0 square feet.

---

## What the Data Changed

**The Space Shuttle was designed to carry air-breathing engines for its landing approach and flew
without them.** The two precision landings on concrete are cited by the programme's own account as what
removed them. The article states that as a programme retrospective rather than as an established
decision record, because two landings do not by themselves settle a choice that large.

---

## Three New Homonym Families, Two of Them Severe

**Flare is overwhelmingly the solar flare**, and secondarily the gas flare and the flare stack of
petrochemical engineering. The landing flare is a minority meaning by a wide margin.

**Energy management belongs to power grids, buildings and batteries.** A pattern for it retrieved a
manual on energy conservation in Navy family housing and a study of control systems in Texas buildings.

**Base is the air base, the database and the base station**, and survives here only because base drag
carries its own disambiguating word.

Five records read and dropped, including **a heavy-duty truck aerodynamics paper by the same author
applying the same base-drag physics**, which is legitimate work and the wrong vehicle class. Rejection
list 469 to 473.

---

## Checks

**109 independent numerical checks**, with the drag optimum found by golden-section search rather than
by calculus, the lift-to-drag ratio by scanning the polar rather than the closed form, and the flare
integrated a second time with a different step variable.

**`_verify.py` at the 21-warning baseline.** `check_any.py` clean. **A 25-article isolated build with
all 18 equations rendering as display math.**

---

## State

**A321 draft pass complete. Committed, not pushed, not published.**

Twenty-five of seventy-two. The publication-order dependency is twenty-five deep.

**Awaiting the equation-density review prompt.** Eighteen equations is low and the pass has plenty to
find. Likely candidates are the lift-curve slope relations the article names but does not show, the
stall-speed and load-factor relations, the energy-height accounting, the drag polar itself, the
approach trim balance, and the base-pressure-to-forebody-drag relation written out rather than
described.

**One tooling note for the publication pass.** A320's survey was written by placeholder substitution
which froze its citations; that approach must not be reused. Cluster citations belong in the body as
live calls.

**Still open and unchanged.** The fourth genre class, now ten consecutive articles. The A305 length
offer.
