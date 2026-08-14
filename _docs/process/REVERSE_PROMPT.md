## Last Updated

**Date**: 2026-08-14
**Task**: **A340, "X-Planes: Micro-Craft X-43 Hyper-X", equation-density review complete.** Committed
and **not pushed**, since only the publication review pushes. **Not published**, and publication of
this series has never been authorised.

---

## 10 Equations to 30, and the Most Important One Formalises the Article's Own Claim

**The draft asserted that no single analysis could have found the margin failure and never showed
why.** That was the article's central claim carried entirely by prose.

It now writes the true margin as the nominal margin less the modelling errors, lets each error consume
a fraction of the nominal margin, and shows the two conditions side by side. **Any single analysis
reports a healthy margin whenever that fraction is under one. The combination is unstable whenever the
number of terms times the fraction exceeds one.** Both hold together whenever there is more than one
error term and the fraction sits between one over the number of terms and one.

**The table that follows is the point.** Three terms each consuming 40 percent, four each consuming 30,
five each consuming 25. **Every row is a vehicle that every individual analysis passes and that is
unstable.** That is the mishap board's finding restated as arithmetic rather than paraphrased.

---

## The Divergence Now Has a Growth Rate and It Is Smaller Than Expected

Five cycles at 2.5 hertz over two seconds fix the growth rate, and the corresponding damping ratio is
between **−0.051 and −0.095** depending on how much amplitude growth is assumed.

**The vehicle was not wildly unstable. It was slightly unstable, for two seconds, which was enough.**
That is the gain margin statement in another form and it is worth having both.

---

## Nine Relations the Prose Had Leaned On Silently

**Momentum thrust and air capture**, which show that exit velocity exceeds flight velocity by a few
percent rather than by a factor, so a five percent excess yields 103 newtons per kilogram per second of
captured air at Mach 7. **Everything in the engine is spent on that few percent.**

**The total pressure ratio**, at 3,543 and 32,345, which is why hypersonic compression is taken through
several weak oblique shocks rather than one strong one.

**The theta-beta-M relation with worked property jumps**, showing that a single ten degree turn does
most of a factor of three in pressure and costs a Mach number and a half.

**Rayleigh flow**, which is the relation the isolator exists to answer. A combustor entering at Mach 2
may raise its stagnation temperature by only **26 percent** before it chokes.

**Combustor residence time**, at 970 and 680 microseconds, which is why the problem is mixing rather
than chemistry.

**The heating ratio decomposed**, into a velocity cube of 2.91 against a density square root of 0.702,
giving the factor of 2.04.

**Reynolds number with Sutherland viscosity**, which puts the flight article an order of magnitude
below a full-size vehicle and is the quantitative form of the scale caution.

**Why the thrust-drag margin closes with Mach number**, which the draft asserted. Heat release per unit
mass of air is fixed while the kinetic energy of the captured flow grows as the square of speed, so the
fractional velocity increment falls while drag holds constant on a constant dynamic pressure
trajectory.

---

## The Pass Introduced Two Defects and Both Were Caught

**A display absorbed the following line**, which is the self-inflicted equation defect this series has
shipped before and which a scan for displays that open with `$$` and do not close with it finds
immediately.

**The second was new to me and `_verify.py` caught it.** A literal pipe inside inline math at the start
of a line makes kramdown render the whole paragraph as a table. The absolute value bars in the margin
relation did exactly that. **Rewriting them with `\lvert` and `\rvert` removes the pipe character
entirely** and renders identically, which is the right fix rather than reflowing the paragraph.

**That check exists because the defect shipped before**, and this is the first time in my work on this
series that it has fired.

---

## Counts and State

**23,713 lines, 30 display equations, 11,344 reference definitions, 128,194 words**, of which
**20,135 are author prose**, a dilution factor of 6.4.

**All 29 figures introduced by this pass were verified against the script that computed them**, as were
the 31 from the draft pass.

**`_verify.py` reports 0 errors and 0 warnings across 301 posts.** The 60 display delimiters balance,
no display fails to close on its own line, no inline math carries a pipe, prose style scans clean on
all five rules and there are zero caps-emphasis spans. Reference integrity is exact at 11,344 used and
11,344 defined.

**One figure in the verification script was wrong and was corrected before it reached the article.**
The Rayleigh prose said 28 percent at Mach 2.5 where the computation gives 41, and the Mach 2.0 value
is 26. The article uses the computed figures.

**Forty-four of seventy-two drafted, none published, publication never authorised.**

---

## What I Did Not Do

**I did not push.** Only the publication review pushes.

**I did not publish**, and I will not without an explicit instruction.

**I did not add equations to the survey section.** It maps a field and cites it, names no results of
its own, and so relies on no relations.

---

## Next

**The primary-reference review of A340**, on your prompt. Nothing else is outstanding.
