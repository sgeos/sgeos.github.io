# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-07
**Task**: A309 equation-density pass, the second of four. Committed and **not pushed**. **Not
published.** All thirteen articles in the series remain in `_drafts/`.

---

## The Pass Found a Wrong Claim, Which Is the Point of It

This belongs first because it is the most useful thing the pass did and because it cuts against the
article's own argument.

The draft asserted that all-inertial guidance replaced radio guidance in the Atlas E and F "once
components improved by roughly two orders of magnitude." That was an assertion, not a computation.
Deriving the requirement properly gives a gyroscope drift allowance of

**0.329 degrees per hour**, from $\varepsilon \leq 2 \delta v / (g t^{2})$,

against period instruments drifting at of order one degree per hour. **The gap is a factor of about
three, not two orders of magnitude.**

The consequence is that the article's inference about architecture is now weaker rather than
stronger. All-inertial guidance was **close** in 1958 rather than out of reach, so what the ground
link bought was margin rather than capability. Both the claim and the Epistemic State entry that
depended on it have been rewritten to say so.

**That is the fifth article running in which writing a relation down caught arithmetic the draft
carried as an assertion.**

---

## Three Results That Changed What the Article Says

**The error budget saturates, and the draft understated how badly.** The draft said halving the
largest contribution improves the total by only 10.3 percent. Writing the improvement relation
$\delta v_{\text{new}} / \delta v_{\text{old}} = \sqrt{1 - s_{i} (1 - k^{-2})}$ and taking the limit
shows that **removing that contribution entirely, at infinite cost, buys only 14.0 percent.** Halving
it already captures three quarters of everything perfect elimination could achieve. That is a much
stronger statement about why accuracy programmes proceed by increments.

**The oblate gravity field displaces the impact point by tens of kilometres.** The draft said the
departure from a point-mass field "is not small" and gave no number. The leading zonal harmonic
contributes 1.62 parts in a thousand of gravity, which over a 2,058 second free-fall arc gives a
displacement of order **34 kilometres, nine times the entire miss budget.** A vague qualification
became a quantitative one.

**The angle-versus-speed claim needed its own scaling.** The draft said pointing is "roughly fifty
times more forgiving than speed at the tolerances that matter," which is true and incomplete, because
the ratio scales as the inverse square of the angle. At a twentieth of a degree it is 191 and **at
half a degree it is 1.9, so the angle stops being free.** An autopilot holding a tenth of a degree
has margin and one holding half a degree does not, which the draft did not say.

---

## Smaller Additions

**An identity worth having.** The factor by which the vehicle becomes harder to stop precisely
through the sustainer burn is 4.38, and that number is not independent. It is exactly the sustainer
mass ratio, the same quantity the rocket equation rewards through a logarithm.

**The Earth rotation credit exposes where the article's own linear sensitivity stops working.** The
first-order azimuth relation gives 2,466 kilometres due east against an exact 3,195, **a shortfall of
23 percent**, because a 408 metre per second perturbation is far outside the regime where the
linearisation that governs the whole article holds.

**A range instrument must be 3.1 times better than the missile it certifies** for a five percent
ceiling on measured-scatter inflation, which is 0.196 metres per second. The draft asserted the
requirement without sizing it.

Also added: the plasma-frequency inversion and its square-law ratio of 77.4, the variance-share
relation, the linear scaling of the speed budget across one, two, and five nautical miles of assumed
circular error probable, and the boil-off holding time of five days.

---

## Density, and Why Nothing Was Trimmed

**115 display equations before the pass, 135 after.** The band for a full aircraft is 90 to 130, so
the article now sits **five over the ceiling.**

That is deliberate and it is reported rather than repaired. The genre document states that the rule
producing the band takes precedence over the number, and the rule is that if the prose names a
result, relies on a relation, or quotes a value some relation produced, the relation must be shown.
Every one of the twenty additions answers a claim the draft was already making. **Trimming to stay
under a band is explicitly worse than reporting the overrun**, and A305 sits at 200.

The structural audit found ten sections above 150 words with no equations, and all ten are
legitimately narrative, namely the opening, the two programme-origin subsections, the flight-record
introduction, the contemporary literature survey, the assessment of what the vehicle was worth, the
designation question, the source base, the Epistemic State, and the conclusion.

---

## Verification

All 160 worked values re-derived independently, including every equation-pass addition, with **zero
disagreements**. `_verify.py` at the 0-error 21-warning corpus baseline. Zero contractions,
em-dashes, en-dashes, prose colons, prose semicolons, prose parentheticals, doubled words, duplicate
headings, lone dollar-delimited lines, or adjacent display-math seams. All eleven insertion seams
read by eye. Isolated build succeeding with **135 rendered display blocks matching the source count
exactly**, Part 13 navigation, eleven tables, no unresolved reference links and no surviving Liquid
tags.

The Epistemic State was updated in the same pass. Five new assumptions are now named, of which **the
period gyroscope drift of order one degree per hour is the least well sourced number in the
article** and the conclusion drawn from it depends on it directly. That is stated explicitly.

---

## State

**1162 lines, 135 display equations, 165 reference definitions, 13,712 body words.**

Lines are 138 below the 1300 floor and references 85 below the 250 floor. Both are reported rather
than padded, and the reference gap is the primary pass's work.

**Contemporary references remain at 23, or 15.5 percent of dated**, well below the 28 to 33 percent
floor and far below the 101 to 189 absolute count held since A301. The publication-review sweep still
carries the largest single gap.

**Committed, not pushed.** Thirteen articles drafted of seventy-two, none published. The
publication-order dependency is thirteen deep, A309 back to A297.

**Categories remain undecided** at `aerospace history engineering`, thirteen articles deep and raised
seventeen times.
