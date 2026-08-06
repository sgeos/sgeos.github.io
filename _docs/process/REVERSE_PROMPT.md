# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-05
**Task**: A304 equation-density review. Committed and **not pushed**. **No article in this series is
published.**

**33 to 94 display equations, 895 to 1157 lines.** Equations and references are inside band.

---

## The Pass Corrected a Claim the Draft Asserted Without Computing

The draft said a staged conical shock system recovers "something like half" the total pressure where
a normal shock recovers a tenth, "a factor of five." That was an assertion from memory and it was
wrong.

Carrying out the oblique shock arithmetic properly, two sixteen-degree turns followed by a terminal
normal shock give component recoveries of 0.739, 0.874, and 0.615, whose product is **0.397** against
**0.107** for a single normal shock. That is **a factor of 3.7, not five**. The article now shows the
three components rather than asserting the total, and the conclusion is unchanged in kind and smaller
in size.

---

## Three Results the Draft Did Not Have

**Specific impulse is the argument the draft never made.** At Mach 4.31 the ramjet returns 1850
seconds against 250 to 450 for a chemical rocket, so it delivers **four to seven times the specific
impulse of the rocket that starts it**. That is the entire reason for the architecture and the reason
the booster is thrown away four seconds in.

**The subsonic-combustion ceiling can be located rather than gestured at.** Thrust vanishes when the
stagnation temperature reaches the combustor limit, and solving that gives $M_{\lim} = 6.2$. The
draft said the ramjet "stops being useful somewhere near Mach 5 to 6" without deriving it.

**The Damköhler number makes the combustion section quantitative.** The ratio of residence time to
chemical time is 8.3 for a one millisecond chemistry, 1.7 at five, and 0.83 at ten. **A ramjet
combustor operates within a factor of a few of not working**, which is why the flame must be anchored
and why the whole flame-holder literature exists.

---

## The Keystone Got Its Machinery

The draft asserted the extrapolation argument with one variance relation. It now has the apparatus.

The **stopping rule** that separates the two kinds of programme is an expected-cost balance, in which
a test point is bought until the marginal information no longer justifies the marginal expected loss.
**When the vehicle cost term includes a human life the right side is effectively unbounded and the
stopping point moves inward without limit.** That single term is the whole difference, and it explains
why the X-7's advantage cannot be recovered by making a crewed aircraft cheaper, which is the obvious
objection and one the draft left unanswered.

Fisher information supplies the other half, since the information a sample carries about a slope grows
with its distance from the centroid, so **the optimal design places points exactly where a crewed
programme is forbidden to go**.

The economics are now quantified too. At an eighty-five percent Wright learning curve the cumulative
average over 130 articles is 0.41, so **130 vehicles cost about 53 times one vehicle rather than 130
times**. That connects to Wright 1936, which has been in the series apparatus since the opener and
has not done real work until now.

---

## Verification

**All 33 worked values re-derived independently**, with two rounding slips corrected, a drag loss of
9.4 metres per second stated as 9 and a scramjet residence time of 0.67 milliseconds stated as 0.7.

Three seam and style defects found and repaired. **Two equations had prose glued to the same line**,
both from insertions that landed mid-paragraph, and one sentence carried two prose semicolons. The
unbalanced-delimiter check caught the first two and the style scan the third.

253 references with zero undefined and zero orphaned. `_verify.py` at the 0-error 21-warning corpus
baseline. Isolated build succeeding with 94 rendered display blocks matching 94 source equations and
Part 8 navigation.

---

## What Remains

**Lines at 1157 are 143 short of the 1300 floor and have not been padded.** Contemporary references
are 38.8 percent of dated, comfortably inside the target range, so A304 enters the later passes
without a deficit there. The section with the least equation coverage remaining is the contemporary
literature, which carries four across five subsections.

**Publication order dependency is eight deep.** Two commits unpushed. Categories remain
`aerospace history engineering`, eight articles deep.
