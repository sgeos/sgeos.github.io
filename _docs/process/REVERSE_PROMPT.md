# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A320 equation-density review, the second of four passes.
**Committed, not pushed.** Not published.

**31 display equations to 70**, across twenty edits, each asserted to match its anchor exactly once.
**1,291 to 1,471 lines, 10,177 to 11,245 words, 871 references unchanged.**

---

## The Most Instructive Finding Was Not a Missing Equation

**The draft said the two published lift-to-drag ratios differ by 44 percent. As ratios they differ by
20.**

The 44 is correct, but it is correct about the **crossrange** those ratios imply, because crossrange
goes as the square. The sentence was leaning on the squaring without showing it, and a reader checking
1.2 against 1.0 would have found an apparent error that was not one.

$$\frac{y(1.2)}{y(1.0)} = \left(\frac{1.2}{1.0}\right)^2 = 1.44$$

**A twenty percent disagreement about the vehicle is a forty-four percent disagreement about what it can
do.** That is a better sentence than the one it replaced, and the pass found it by asking which relation
produced a quoted number.

---

## Four Quantities Were Computed in the Draft Pass and Never Reached the Article

**This is the mirror defect and it is just as much a density failure.** The work had been done and the
article did not carry it.

- **The ballute deployment dynamic pressure**, 3,350 pascals or 70 pounds per square foot, which is a
  mild load and is the reason for deploying that high
- **The altitude at peak heating**, 71.8 kilometres, which anchors the whole thermal section to
  somewhere physical
- **The deceleration at the start of the glide**, 0.066 g, against 1.18 at the end. **The entire lifting
  entry is gentler than standing up**
- **The lift-to-drag ratio the Shuttle's own requirement implies**, 1.25

**That last one answers a question the draft raised and left hanging.** Putting 1,100 nautical miles
through the same relation that gave 0.978 for the general case gives 1.25, which is above what a pure
lifting body of the period could reach and about what a delta wing at hypersonic incidence does reach.
**The once-around requirement bought the Shuttle its wing.**

---

## Three Results Are New Rather Than Merely Displayed

**The footprint area goes as the cube of the lift-to-drag ratio.** Crossrange half-width is quadratic in
it and downrange depth is linear, so the reachable ground area is cubic. The disputed twenty percent is
therefore a factor of 1.73 in the area a vehicle can reach, which is why the disagreement in the sources
is worth the space this article gives it.

**Crossrange stops accumulating exactly where the heading passes half a turn**, since it accumulates as
the sine of the heading. At a ratio of 1.2 that happens at 189 metres per second, very near the end.
Everything after it is spent flying back toward the plane the vehicle started in.

**The SV-5D does not obey square-cube scaling against the X-24A, and the failure is informative.** The
length ratio is 0.272, so cube scaling predicts a weight ratio of 0.020. The actual ratio is 0.078,
nearly four times more. The SV-5D is very nearly solid thermal protection while the X-24A is enclosed
volume with a pilot and a rocket engine in it. **Areas scale and contents do not**, which is exactly why
the reference area derived from the X-24A is defensible and a weight derived the same way would not have
been. The article now says so where it introduces that assumption.

---

## Derivations That Were Asserted Are Now Shown

The radial balance with its centrifugal term, rather than only the rearranged result. The substitution
chain behind the crossrange integral. The geometric-series expansion that produces the Basel sum, which
is worth doing because **a constant from elementary number theory turns up in the range of a re-entry
vehicle**. The bank optimum as a stationary condition with its second derivative, rather than an
assertion. The downrange relation derived from the same two statements the crossrange came from, which
is what makes the simultaneous solve legitimate. The heat-flux proportionality and the quadratic whose
root puts peak heating at two thirds. The latitude relation as a square root of the cosine.

---

## One Guard Fired and Was Right

**The display-math-with-trailing-prose check caught an equation left sharing a line with the sentence
after it.** That renders as inline math and is not even counted, and it is the defect class found
corpus-wide during the errata pass in A300 and A313. It cost one edit to fix and would have been
invisible in review.

---

## Checks

**A new independent verifier of 104 checks**, re-deriving every added quantity by a different route
wherever one exists. The Basel sum by the **Euler product over primes** rather than by summation. The
bank optimum by **golden-section search** rather than by calculus. The parachute area by **numerical
integration of the disc** rather than from the formula. The peak-heating altitude by **forward
substitution back to the density**, which is the stronger direction than the inversion that produced it.

**The original 114-check verifier still passes**, after three stale text expectations were corrected
where the equation pass had moved values into LaTeX. Those were verifier defects, not article defects,
and the values were confirmed present in their new form before the expectations were changed.

**`_verify.py` at the 21-warning baseline.** `check_any.py` clean across all 24 articles. **A 24-article
isolated build with all 70 equations rendering as display math and zero unbalanced braces.**

---

## On the Band

**Seventy equations against a full-aircraft band of 90 to 130.** The article is below band and is
reported that way rather than padded toward it. Every relation the prose names, relies on, or evaluates
is now displayed, which is the rule that produces the number, and the number it produced is 70.

**This is the ninth consecutive article to finish outside all four named genre classes**, references far
above band and lines and equations below.

---

## State

**A320 equation pass complete. Committed, not pushed, not published.**

**Awaiting the primary-reference review prompt.** Expect the usual inter-pass dependency to bite, since
this pass promoted several subjects the draft harvest could not have anticipated. The likely thin ones
are the Basel-sum and trajectory-mechanics literature behind the closed form, atmospheric scale height
and standard-atmosphere models, supersonic decelerator loads for the ballute, weight and mass-fraction
estimation for the scaling argument that fails, and the Shuttle crossrange requirement's own
documentary record.

**Still open and unchanged.** The fourth genre class, now nine consecutive articles. The A305 length
offer.
