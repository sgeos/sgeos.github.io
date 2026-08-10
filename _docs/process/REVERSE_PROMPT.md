# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: Two items on human-pilot instruction. **A369 drafted** as a general-audience retarget of the
published A285, editorial date 2026-08-06. **`RESEARCH_AIRCRAFT_STRUCTURE.md` amended** to describe
what the series actually does. Committed, **not pushed**, not published.

---

## A369, Why SpaceX Built a Ladder Instead of a Moonshot

**412 lines, 7 display equations, 43 references, 3,602 words. Standalone rather than part of a
series**, since the History of SpaceX series is complete at twelve articles and no further article in
it was planned.

### What Changed, and What Did Not

**The framework scaffolding went.** A general reader does not need the mapping problem, the
methodological commitments, the four analytical traditions or the forcing-function vocabulary to
follow an argument that is strong on its own.

**The notation was replaced by arithmetic.** The source carries 69 display equations and almost none
of them compute anything. They are definitional forms that restate a sentence in symbols. **The
analytical essay genre is explicit on this**, saying essays carry equations only where a real
quantitative relationship exists and that token equations belong to a different genre. **All seven
equations here produce a number the reader can check.**

**The argument was made falsifiable.** The source describes the pattern. This version states what it
costs, where it does not apply, and what it cannot establish.

**The substance was not reduced.** The vehicle history, the negation cases and a 43-reference base are
carried forward, and the counterfactual is quantified where the source only named it.

### The Central Result

**A ladder does not need better odds than a monolith. It needs the same odds arranged differently.**

Eight stages at ninety percent each give a monolith a 0.43 chance of delivering everything and a 0.57
chance of delivering **nothing**. The same stages arranged as independently valuable rungs deliver 64
percent of the value in expectation and deliver **something** ninety percent of the time. **The gap
widens as the odds get worse**, which is where long technical programmes live.

**The shape of the risk matters more than its size.** The monolith's outcome is binary and the
ladder's is graded, and a programme with three delivered rungs is far harder to cancel than a hole in
Texas.

### The Strongest Argument Is One the Vehicle List Misses

Falcon 1 used one Merlin engine, Falcon 9 uses nine, Falcon Heavy twenty-seven. **Every vehicle pays
into the same learning curve.** On Wright's law at a 0.85 learning rate a nine-engine design reaches a
unit engine cost **40 percent below** a one-engine design on the same number of airframes.

**And the ratio does not depend on fleet size**, because nine times the units is a fixed 3.17 extra
doublings whether the fleet is ten aircraft or three hundred. **That is the ladder operating on a
component rather than on a vehicle**, and unlike the vehicle sequence it does not depend on commercial
judgement or good fortune.

### Where the Article Argues Against Itself

**The Super Collider could not have been built as a ladder.** A collider's energy is set by its
circumference and half a ring is not a small ring. **So the lesson is that some projects genuinely do
not decompose, not that its managers chose badly**, and those projects need a different kind of
political protection.

**Apollo is placed among the cautionary cases rather than the successes.** Its rungs were technical
rather than commercial, so when political demand ended there was no customer to keep paying and the
capability was dismantled. **A rung that only an internal sponsor values vanishes when the sponsor
does.**

**Three costs are named and the third is the interesting one.** A rung that pays well is a reason not
to climb. That is the mechanism that makes successful firms slow to replace their own products, and
**the ladder does not remove it. The ladder creates it.**

### Verification

**23 independent checks.** The ladder expectation is recovered by **simulation over 400,000 trials**
rather than by the closed-form sum, and the two are required to agree. The outcome distribution is
required to sum to one. The fleet-size independence of the engine ratio is tested as a **property**
across six fleet sizes.

**One check was itself corrected**, since a relative tolerance was too tight on the smallest table
entry, where the real question is whether 5.76 percent rounds to the quoted 6.

Prose style clean with zero em dashes, en dashes, prose colons, prose semicolons or parentheticals,
zero unbalanced bold, all seven equations on single lines, zero doubled backslashes, and the fourteen
apostrophes audited as possessives. Isolated build succeeding with zero Liquid errors and zero
unresolved links.

**`tmp/errata/check_any.py` does not apply to this article** and correctly reports A369 as absent from
the X-Planes roster. That is the tool working, not a defect.

---

## The Genre Document, Amended

**The previous bands were drawn from the History of SpaceX medians and no recent article matched
them.** They had drifted far enough from practice to be misleading.

Measured across all twenty-seven X-Planes articles then drafted:

| | Lines | Equations | References |
|---|---|---|---|
| Minimum | 937 | 25 | 335 |
| Median | 1,488 | 94 | 404 |
| Maximum | 7,198 | 200 | 3,990 |

**The corpus contains two regimes and the transitions are sharp.** The equation count fell at A313 and
the reference count rose by an order of magnitude at A318.

**Neither is a change of standard, and the document now says why.** The equation count follows the
**subject**, since the governing rule displays whatever relations the prose relies on. The reference
count follows the **contemporary-survey directive**, which from A318 was satisfied by citing a topic
as a body of literature rather than by a few exemplars.

**The class table is now explicitly about section order, which stays prescriptive**, while the numbers
are labelled measured descriptions and not targets. The comprehensiveness directive is recorded, so
exceeding a figure is not a defect and needs no justification, **while padding toward one remains
equally forbidden.**

**Two further sections were reconciled.** The series-opener paragraph no longer quotes a withdrawn
band. And **the designation-anomaly section now records the boundary A320 established**, that the test
is whether a vehicle existed and produced data rather than whether the designation is disputed.
**That bears directly on A324**, where no vehicle was ever built.

---

## State

**Committed, not pushed.** Neither item is a publication-review pass, so the push rule does not apply.
Nothing is published.

Twenty-seven X-Planes articles complete and pushed, plus A369 drafted. **The next X-Planes article is
A324, the Lockheed X-27**, and the amended genre document now gives it a clearer test for which class
it belongs to.
