## Last Updated

**Date**: 2026-09-02
**Task**: **A345 equation-density review, the second of four passes.** Committed and **not pushed**.
**Not published**, and publication of the series still not authorised.

---

## Seven Display Equations to Thirty-Five, and Three of Them Are New Results

**The pass was not a formalisation exercise.** Writing the scaling argument out properly produced
three findings the draft did not contain, and forced one correction on the draft's own statement of
its limits.

---

## The Atmosphere Makes the Reynolds Penalty Worse, and This Is the First Article to Use That Cluster

**Three articles in this series displayed relations that use the standard atmosphere and harvested
nothing about it.** A345 harvested 51 records and, until this pass, would have cited them without
needing them.

**Kinematic viscosity rises with altitude.** The X-48B flew to a ceiling of 10,000 feet while the
full-scale aeroplane's low-speed regime is near the ground, so the honest penalty is

**40.35 times 1.281, which is 51.7**, where 1.281 is the ratio of kinematic viscosity at 10,000 feet
to its sea-level value on the standard atmosphere. **The mismatch the whole article turns on is a
quarter worse than the draft said**, for any manoeuvre flown high.

---

## The Relative Density Factor Was Assumed Away and Is Now Priced

**The weight ratio is $n^3/\sigma$ and the draft set $\sigma$ to one without saying what it cost.**
Restoring it moves the implied full-scale weight from **854,875 pounds at unity** to **914,885 at the
field elevation of Rogers Dry Lake** and **1,157,634 at the ceiling**.

**So the draft's headline figure is a lower bound rather than an estimate**, and the comparison
against Liebeck's design moves from 1.160 to at least that and 1.241 on the field reading. The
article now says so in both places.

---

## The X-48C Is Doubly Penalised on Its Weakest Axis and One Half Is Exact

**The programme's own hypothesis was that yaw control is poor throughout the envelope.** The noise
modification then acted on that axis twice.

**The engine-count half is exact and rests only on published thrusts and weights.** The asymmetric
thrust carried as a fraction of weight is $(T/W)/N_e$, giving **0.10286 for the B model, 0.17800 for
the C and 0.07485 for the full-scale trijet**, so the C model's engine-out upset is **2.378 times the
full-scale case and 1.731 times the B model's**.

**The moment-arm half is a sensitivity and the article says so.** The sweep of the outer trailing
edge is not published, so the forward shift is tabulated at 30, 35 and 40 degrees. **What does not
move is the sign**, because no reading of the geometry lets a surface moved inboard on an aft-swept
planform gain arm. **The two-foot aft-deck extension acts in the recovering direction, which is itself
evidence that arm was lost and known to be lost.**

**NASA's record that the C model needed new limiters because its handling qualities differed from the
B model's is the corroboration**, and the arithmetic is one reading of why.

---

## A Correction the Pass Forced on the Draft

**The draft asserted that no claim depended on the wing area.** The new absolute Reynolds figures do,
through the reference chord $c = S/b$, and the area comes from a secondary compilation.

**That limit now names the two numbers a reader distrusting the area should discard**, and states that
**the ratio of 40.35 does not depend on it at all, because the chord cancels.** The ratio and not the
absolute value carries the argument, which was true before and was not said.

---

## The Verifier Caught Two Rounding Errors I Introduced This Pass

**The reference chord was written 4.927 where 4.9265 rounds to 4.926**, and the full-scale asymmetry
**0.0749 where 0.074848 rounds to 0.0748**. Both were mine, both were introduced by this pass, and
both were caught because the tolerance is derived from how precisely each value is written rather than
from habit.

**The asymmetry fractions are now shown to five decimals so that a reader dividing them reproduces the
stated ratios.** At four decimals they did not, which is a defect a checker comparing against exact
values would never have reported.

**`math-display-inlined` fired three times**, every one an equation I inserted that ran into the prose
following it on the same source line. **That renders as inline math with two sentences run together
while the delimiters stay balanced and the markup resolves**, so a rendered audit reports a clean
page. **Source `$$` pairs and `lint.stats` now agree at 35**, which is the count comparison A341 had
to invent for exactly this.

---

## State

**A345 is committed and NOT pushed. Two of four passes complete.** **12,936 lines, 35 display
equations, 6,183 reference definitions, 71,294 words**, of which 7,725 are author prose. Editorial
date 2025-11-23, series index 49, **full-aircraft class**.

`_verify.py` zero errors and zero warnings, `lint.py` **zero defects and zero conventions**, reference
integrity **6,183 used, 6,183 defined, zero undefined, zero orphaned, zero duplicate URLs**, every
stated value re-derived by a verifier that does not import the computation and **writes the standard
atmosphere out rather than looking it up**, all 17 survey rows agreeing across stated, cited and
data-derived counts, 48 back-references with zero forward references, and zero contractions, colons,
semicolons, dashes, parentheticals or caps-emphasis spans in authored prose. **`_lib` tests are 95 of
95.**

**Forty-nine of seventy-two drafted, none published, publication never authorised.**

---

## Next

**A345's primary-reference review**, the third of four passes. **Report primaries stand at 796 of
6,114, being 13.0 percent**, which is the lowest fraction of the recent run and has an explicable
cause. **The article's most important sources are AIAA conference papers**, which the metric's
definition excludes, so the primary pass should either raise the NASA and DTIC yield or argue the
definition. **The atmosphere cluster is now load-bearing at 51 records** and should be checked before
anything else, since this pass is what made it so.
