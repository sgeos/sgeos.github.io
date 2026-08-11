# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-10
**Task**: A329, the Boeing X-32, drafted. The first of four passes. Committed, **not pushed**,
**not published**.

**State: 7,195 lines, 15 display equations, 2,108 reference definitions, 39,311 words.** All
thirty-three articles in the series remain in `_drafts/`.

---

## The First Aircraft in the Series Built to Win a Competition

**Every other X-plane so far existed to find something out. This one existed to beat another
aeroplane**, and on 26 October 2001 it did not.

**The keystone is therefore what a fly-off decides and on what evidence**, and it is a question of
**construct validity** rather than of sampling error. That distinguishes it from the previous
article. The X-31 flew hundreds of engagements and the difficulty was that a finite sample carries a
wide interval. Here the sample size is one, and the difficulty is that **the one trial was not a
trial of the proposed aircraft**.

---

## The Propulsion Half Has a Clean Answer in One Relation

Static thrust is mass flow times jet velocity and the power added is half the mass flow times the
velocity squared, so eliminating the velocity gives thrust as the square root of twice the power
times the mass flow. **At fixed power, doubling the mass flow multiplies thrust by root two.**

**That is the entire case for a lift fan over direct lift and it fits on one line.** A lift fan
spends shaft power on a large cold stream and a direct-lift system spends the same power on a
smaller hot one.

**Three published numbers that were never published together turn out to be mutually consistent.**
The lift fan's 50-inch diameter, its 20,000 pounds of cold thrust and its 29,000 shaft horsepower
imply a figure of merit of **0.697**, which is what a good ducted fan achieves. Establishing that
before building an argument on them seemed worth doing, and nobody appears to have checked it in
print.

**The nozzle the direct-lift system would have needed is inverted rather than assumed.** Matching
the fan's disc loading with 28,000 pounds of core thrust needs 19.09 square feet of nozzle, a single
opening **4.93 feet across**, on a 45-foot fighter. That is not an engineering trade.

---

## The Competition in One Number

At 24,030 pounds empty and a five percent control margin, direct lift permits a bring-back allowance
over empty weight of **2,637 pounds** and the lift system permits **15,875**, a ratio of **6.02**.

**Both aircraft can hover. One can come home with two and a half thousand pounds of fuel and weapons
and the other with nearly sixteen thousand.**

**And the small number is badly conditioned.** The allowance is a small difference between two large
numbers, so it amplifies a fractional thrust loss by **10.11** against 2.51 for the lift system, and
a fifty degree inlet temperature rise from hot gas ingestion takes **45.5 percent of it**. Below
25,232 pounds of lift the allowance is negative, meaning the aircraft could not land vertically at
its own empty weight.

**The amplification is reported as badly conditioned rather than as a precise number**, because it
blows up as the allowance approaches zero and that is the shape of the problem rather than an
artefact of the arithmetic.

---

## The Second Finding Came Out of Building the Reference Set

**In a pool of 4,412 harvested records, exactly one carries the X-32 in its title.** It was written
by the engine supplier, in 2002, after the decision. Against that, the F-35 appears in 29 titles
running continuously from 2002 to 2020.

**The winner acquired a literature and the loser did not.**

**The cluster was tested before the claim was made.** Two harvests asked for the aircraft by
designation, by manufacturer and programme together, and by the pre-competition programme names,
across the reports server, both Crossref content types and the defence registry. The answer did not
move.

**The consequence for the article is stated rather than hidden.** Its technical case rests on
published numbers for the winning system and an assumed upper bound for the losing one, because the
losing one's numbers were never published. **The evidentiary asymmetry available to a historian is a
direct inheritance of the asymmetry in the decision.**

---

## The Historical Finding

**Boeing flew a wing it had already abandoned.** The demonstrators carried a tailless delta and the
production proposal used a conventional wing with a canted twin tail, and the change was made before
the X-32 ever flew.

**A demonstrator that differs from the proposal in the feature under examination is evidence about a
different aeroplane.** The customer was shown an aircraft nobody intended to build, while the
competitor's demonstrator flew a short takeoff, a supersonic dash and a vertical landing in a single
sortie in the configuration it was offering.

**The article gives the opposite reading its own subsection**, because a company that finds a
configuration problem and fixes it before proposing has done what a risk-reduction phase is for, and
the record does not say which reading the source selection took.

---

## Two Defects Found

**An all-remaining marker can legitimately find nothing left**, when an earlier marker for the same
cluster and era already drained it. The assembler now distinguishes that from a fixed-count marker
finding nothing, which means the article is citing a subject it does not have.

**`require_in_text` failed on a value that was present in the draft.** The equation wrote
`20{,}199`, which is LaTeX comma spacing, and the flattened text therefore contained `20{}199`
rather than `20199`. **A value inside an equation is not reliably findable by a text check**, so the
figure is now stated in prose as well.

**One record was dropped** for a contraction inside a verbatim citation title, which is the second
such collision after A328 and is handled identically.

---

## Verification

**44 of 44 independent checks passing, none importing the calculation.** The square-root law is
tested as a randomised property over twenty thousand inputs, the figure of merit is reached by
numerically integrating the momentum flux through two hundred thousand annuli rather than by
evaluating the closed form, the nozzle area by bisection, the bring-back allowance by scanning
weights upward until the margin fails, and the amplification by finite difference.

`_verify.py` at the 21-warning baseline with zero errors, check_any clean, `_lib/test_lib.py` at 48
of 48, and reference integrity at 2,108 with zero undefined and zero orphaned anchors.

**A 33-article isolated build renders the page at 16 sections, 50 subsections, 12 tables and all 15
equations**, with zero broken anchors and zero empty headings.

---

## For the Equation Pass

**15 display equations is low against a corpus median of 94**, and that is the next pass's material.
Sections stating numbers without displaying the relation behind them include the wing loading and
thrust-to-weight arithmetic, the corrected-thrust definition, the hover control balance, the
reaction-control bleed penalty, and the sensitivity table's own construction.

---

## Awaiting Instruction

**A329 has completed the draft pass only.** Thirty-three of seventy-two drafted, **none published**.

The next pass is the equation-density review.
