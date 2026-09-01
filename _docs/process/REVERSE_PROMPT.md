## Last Updated

**Date**: 2026-09-01
**Task**: **A343 equation-density review, the second of four passes.** Committed, **not pushed**.
Nothing published and publication still not authorised.

---

## Eleven Display Equations to Thirty-Seven, and Two Prose Claims Were Wrong

**The pass found what it exists to find, which is prose asserting a result that no displayed relation
produces.** Two of those assertions turned out to be false as soon as the relation was written down.

**The draft said the implied vehicle is "two and a half times the X-45A" and it is 2.67 times.** The
ratio was never computed, only estimated from the two masses by eye.

**The draft said the requirement sits "about one point of empty-weight fraction away from being met"
and it sits 2.1 points away.** That one is the better catch, because the correction came from writing
the derivative rather than from recomputing an arithmetic slip,

$$\frac{\partial E}{\partial \zeta_{\text{empty}}} = -\frac{L/D}{c} \frac{1}{\zeta_{\text{end}}}
= -44.2 \ \text{hours per unit}$$

which is 0.442 hours per point against 0.97 hours still needed. **An estimate by eye from a table of
six rows read the gap as half what it is.**

---

## One of My Own New Equations Was Wrong and the Verifier Caught It

**I wrote the end-of-mission weight fraction as one minus payload minus empty.** It is empty plus
payload, equivalently one minus the fuel fraction. The numbers in the table were right, having come
from code that had it right, so **only the newly written relation was wrong** and it would have been a
relation contradicting the table beneath it. The verifier now asserts both forms.

**A displayed line must evaluate to its own stated answer, and one did not.** The span agreement was
written as 0.0042 where the division gives 0.0043. **This is the third article in which that class has
appeared** and it is the reason the check exists.

**One check was itself wrong.** The gap between the demanded fraction and the lightest carrier
aeroplane is 0.0925 from the displayed figures and 0.0928 from unrounded inputs, and the verifier
demanded the second of a line that computes the first. **A displayed line should be checked as it is
written**, so the verifier now checks both and says which is which.

---

## The Guard Promoted Yesterday Fired Today

**`math-display-inlined` caught two defects in this pass.** Both were mine and both had the same cause,
which is that a replacement ending in a display equation left the paragraph's remaining prose on the
same source line. **That renders as inline math with the equation and the following sentences run
together**, and `render.py` cannot see it because the delimiters balance.

**This is the third consecutive article in which the equation pass has produced this defect.** A341
shipped it into a build, A342 was caught by the workbench, and A343 by the gate. **The source `$$`
pair count and the complete-line equation count now agree at 37**, which is the check A341 had to
invent.

---

## What Was Added

**The framing inequality, which the article rested on in words and never wrote.** Carrier suitability
adds mass and removing the crew saves it, so the requirement is satisfiable only if the crew saving
exceeds the deck penalty by the gap between what carrier aircraft achieve and what the requirement
demands. **Neither delta is published for any aircraft**, which is why the article bounds their
difference rather than estimating them.

**The standard atmosphere and the Mach relation**, which the draft used to produce 430.2 knots without
showing either. **The fuel split**, which the draft quoted as fourteen and thirty-nine percent, and
which is 14.0 and 33.8 because the loiter is charged after the outbound leg has already burned fuel.
**The three readings as three distinct products of the same segment ratios.** **The wing area and span
relations** the carrier table is built from and never showed. **Thrust from thrust to weight**, which
puts the required installed thrust 40 percent above the X-45C's at the lowest plausible ratio.
**The fan-out relation and its latency form**, named in prose and left undisplayed. **The fuel-flow
equation and its integral**, which the framing section criticised the article for not using.

---

## The Promoted-Subjects Rule Fired

**Twenty-seven of thirty-seven equation paragraphs carry no citation within their window.** Most are
arithmetic on values already cited and legitimately need none. **Three were closed against sources
already in the reference block**, being the area and span definitions, the thrust relation and the
fuel-flow equation. **The standard atmosphere is the clearest remaining gap** and it is the same one
A341 had to readmit by name, so the primary-reference pass should expect to add it.

**Recorded rather than closed, which is the A342 precedent.** The reference base is the third pass's
work and harvesting for it here would do that pass badly and early.

---

## State

**A343 is committed and not pushed. Two of four passes complete.** **9,489 lines, 37 display
equations, 4,441 reference definitions, 52,819 words**, of which 7,560 are author prose. **References
held at 4,441 and measured before and after**, since an equation pass adds no sources.

`_verify.py` zero errors and zero warnings, `lint.py` **zero defects and zero conventions**, reference
integrity zero undefined, zero orphaned, zero duplicate URLs, **all numerical checks passing** across
the original 45 and the additions, zero caps-emphasis spans on the corrected instrument, and zero
contractions, colons, semicolons, dashes or parentheticals in prose.

**Forty-seven of seventy-two drafted, none published, publication never authorised.**

---

## Next

**The primary-reference review of A343 on your prompt**, which is the third of four passes.

**Two content decisions remain yours and both are on published posts.**
`_posts/2026-08-06-native_lowering_coverage.markdown` carries two authored caps-emphasis spans at
lines 879 and 1306, and thirteen published posts carry 1,045 shouted citation titles that `refs.decap`
now prevents at generation but does not repair.
