# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

## Last Updated

**Date**: 2026-09-09
**Task**: **A355, X-Planes: X-58, the Slot Taken by XQ-58, equation-density review. The
second of four passes.** Committed and **NOT pushed**. **Not published**, and publication of
the series has never been authorised. **Fifty-nine of seventy-two drafted.**

---

## Twenty-Two Display Equations to Forty, and Four of Them Found Something

**Display equations 22 to 40, declared symbols 73 to 101**, lines 5,802 to 6,052, words
36,339 to 39,919, **references unchanged at 2,557** because an equation pass adds no sources.

### The Two Published Speeds Do Not Refer to the Same Altitude

**The specification carries 566 knots and Mach 0.85 side by side, and those agree only at
sea level.** At sea level 566 knots is Mach 0.856, which matches the published figure to
within half a percent. **At the quoted 45,000 foot ceiling the same speed is Mach 0.987**,
which is very nearly sonic and is not a speed this planform holds.

**Nothing in any source says the maximum is a sea level figure.** The article infers it from
consistency and says so. **A reader who assumes both apply at the ceiling is wrong by fifteen
percent**, and the dynamic pressure differs by a factor of 7.3 between the two conditions.

### The Two Published Unit Costs Imply a Progress Ratio of 0.5

**Read as a learning curve, four million dollars at fifty a year and two million at a hundred
is a halving for one doubling.** Airframe curves are conventionally quoted at 80 to 85
percent, and **an 85 percent curve needs 4.27 doublings to halve a cost**, not one. The same
doubling would take an 85 percent curve to 3.4 million dollars.

**The charitable reading is that these are rates and not cumulative units**, which makes the
claim about economies of scale rather than learning. **The article states both readings and
settles neither**, because no source specifies the basis.

### The Argument for Attritable Aircraft Needs No Prices

**Once the design life stops binding, the cost per sortie is the unit cost multiplied by the
probability of loss.** The derivative with respect to survivability is therefore the unit
cost itself, at every value of the probability. **A percentage point of survival is worth one
percent of the airframe price per sortie**, which is 20,000 dollars at the lower unit cost.

**And the break-even against an aeroplane that is not meant to be lost depends only on the
ratio of the two costs.** Against an aeroplane twenty times its price surviving 99 sorties in
100, this one wins above 0.8. **The relation also says when the case fails**, since a ratio of
ten against a nearly invulnerable opponent demands 99 percent survival. **The argument needs a
hostile sky as much as it needs a low price**, and the draft did not say so.

### The Canopy That Lands It Cannot Be Opened at the Speed It Arrives

**The canopy sized for an eight metre per second touchdown, opened at sixty metres per
second, imposes 56.2 times gravity on the empty mass.** **The arithmetic is right and the
premise is impossible, which is the finding rather than an error.** The recovery must be
staged. A first stage of 0.1778 of the full area holds ten times gravity, and the full canopy
is tolerable only below 25.3 metres per second.

**How the staging is actually done is not documented anywhere consulted.** The article derives
that there must be some and does not report what it is.

---

## Three Defects in the Pass's Own New Work, All Caught Before Assembly

**A break-even relation was written inverted and returned negative probabilities**, which is
the arithmetic telling the author the expression was backwards.

**An opening load was computed on a truncated design life**, so an exquisite aircraft's cost
per sortie was wrong by a third until the asymptote was allowed to hold.

**And the symbol table refused the first draft of the equation set.** Three collisions were
caught before assembly, the worst of them a bare `q` for dynamic pressure against a `q` already
meaning a survival probability, which is now `p_x`.

---

## Two Instruments Measured One Thing and Disagreed

**Equation citation coverage came out 36 of 40 on the body and 32 of 40 on the finished
article**, because a one-line slot becomes a three-line block and the line windows then cover
different amounts of prose. **Shipping the larger figure because it appeared first would have
been the defect.** The measurement is now defined once, on the body, and the verifier
recomputes it there and asserts the article states what was computed.

**The remaining four are arithmetic on a relation cited immediately above**, which is the same
result the [X-46][related_post_a343_boeing_x46] measured at 27 of 37 and recorded rather than
closed.

---

## And the Verifier Learned Not to Restate a Rule It Could Import

**A check expecting `20.0` failed on an article correctly saying `20`**, because the verifier
carried its own copy of the assembler's number-formatting rule. **A duplicated rule is a
second place to be wrong.** The verifier now imports the assembler's formatter, so the two
agree by construction.

---

## Verification

**Verifier clean at 0 errors and 0 warnings. Tests 110 of 110. Lint 0 findings.** The symbol
scanner reports all 101 declared symbols used and every symbol used declared.

**The article verifier runs 252 checks and 32 injected defects were all caught with the total
reassembly check disarmed**, so each defect is caught by the instrument aimed at it rather
than by the comparison that catches everything.

**FINAL STATE. 6,052 lines, 40 display equations, 101 declared symbols, 2,557 reference
definitions, 39,919 words**, research 2,452, report primaries 226 at 9.2 percent.

**The stub-isolated production build succeeded against the exact bytes committed**, the
checksum matching draft, stub copy and frozen record. **The rendered audit reports no findings
across 94 pages.** Source and rendered display-equation counts agree at **40**, with zero raw
dollar pairs leaking and zero unexpanded slots. The page is 561,617 bytes.

---

## What Remains

**A355 has completed two of four passes.** The next prompt is the primary-reference review.

**The fuel component of the operating cost is now bounded and is under one percent of the
airframe amortisation at any plausible price**, which narrows the boundary the draft left
standing without closing it. **Maintenance, ground equipment, boosters, parachutes and people
remain unquantified**, and the fact sheet's claim of low maintenance is the one no public
figure supports.

**Three things the record does not settle were added by this pass**, being whether the maximum
speed is a sea level figure, whether the two unit costs are cumulative or rate figures, and on
what basis the payload fraction is quoted. **The engine-class disagreement from the draft pass
stands**, and the arithmetic still favours the turbofan without deciding it.
