## Last Updated

**Date**: 2026-08-13
**Task**: **A339, "X-Planes: Orbital Sciences X-42", equation-density review complete.** Committed and
**not pushed**, per the rule that only the publication review pushes. **Not published**, and
publication of this series has never been authorised.

---

## 23 Equations to 57, and the Worst Gap Was the Most Basic One

**The draft gave a velocity increment family across plausible inert and payload masses and never
displayed the rocket equation.** That is the single clearest instance of the rule this pass enforces,
which is that if the prose names a result, relies on a relation, or quotes a value some relation
produced, the relation is shown.

**It now has its own subsection in Sizing From First Principles**, carrying the rocket equation, the
effective exhaust velocity of **2,697 metres per second**, the definitions of ignition and burnout
mass, and the family as a table. **The family spans roughly 2,340 to 3,580 metres per second** against
a pop-up requirement in the region of two to three, so the vehicle is the right size for the job it was
described as doing. That is a weak statement and the strongest the record supports.

**Thirty-four relations were added in total.** The propellant split and the tank volumes, which the
draft quoted as bare numbers. The throat and exit geometry. The ideal vacuum thrust coefficient and the
area ratio relation that fixes it. The cavitating venturi mass flow, which the whole erosion argument
leans on and which the draft described only in words. The peroxide decomposition energy balance. The
pressurant mass. The cold gas limit. Netting analysis and the isotensoid winding angle.

---

## Two Cross-Checks Came Out of the Pass Rather Than Going Into It

**The catalyst bed sizes itself from the published table.** The bed passes only oxidiser, so the flow
is 29.7 pounds per second, and at the published bed mass flux of 0.4 pounds per second per square inch
the frontal area is 74.2 square inches and the diameter **9.72 inches**. **The published chamber inner
diameter is 10 inches.** Those numbers appear in different sections of the paper for different reasons
and they agree to three percent.

**The contraction ratio is a statement about gas speed, not about geometry.** The isentropic area
relation puts the chamber at **Mach 0.083**, within a tenth of a percent of stagnation temperature.
**So the paper's requirement of a contraction ratio of at least seven for autoignition is a
residence-time and temperature requirement written as a shape**, and saying so is more useful than
repeating the number.

**The article now makes exactly three consistency checks on the published table and names them as
such.** The catalyst bed against the chamber, the exit diameter against the engine envelope, and the
measured thrust coefficient of 1.808 against the ideal 1.835. **The third is the only one that could
have embarrassed the paper**, because a measured thrust coefficient above the ideal would mean the
stated thrust and chamber pressure could not both be true.

---

## The Decomposition Temperature Is Now Derived, and It Overshoots Honestly

**The draft asserted about 740 degrees Celsius and showed nothing.** The article now carries the
reaction, its enthalpy of 98.0 kilojoules per mole, the 2.88 megajoules per kilogram of pure peroxide
that follows, the product split, the heat spent boiling and vaporising the water, and the mixture heat
capacity.

**The balance gives about 780 degrees, six percent high.** It overshoots in the direction the
assumption predicts, because the heat capacity of steam rises steeply with temperature and the
calculation holds it constant. **It is reported as an upper bound rather than as a confirmation**, and
the Epistemic State says so.

**The point is not the last forty degrees.** It is that the dilution water sets the temperature,
absorbing heat while releasing none, which is why concentration is the most important number in
peroxide propulsion.

---

## The Pass Introduced Two Defects of Its Own and Caught Both

**Two inserted displays absorbed the following prose onto their own source line.** That is the
self-inflicted equation defect this series has shipped before, twice in A373 alone. A scan for display
lines that open with `$$` and do not close with it found both.

**The new ordinals contradicted each other.** I wrote that the catalyst bed check was **a third**
independent consistency check and, sixty lines later, that the exit diameter check was **the first**.
**The first appeared after the third.** That is the count-in-own-prose defect again, in a pass whose
whole purpose is arithmetic. All three are now numbered in the order they occur and the order was
checked against line numbers rather than against memory.

---

## Counts and State

**20,931 lines, 57 display equations, 9,816 reference definitions, 115,229 words**, of which
**22,250 are author prose**, a dilution factor of 5.2.

**All 39 figures introduced by this pass were verified against the script that computed them**, as were
the 27 from the draft pass. The area ratio relation printed in the article was checked by solving it
independently and reproducing 1.884 and 1.835.

**`_verify.py` reports 0 errors and 0 warnings across 301 posts.** The 114 display delimiters balance,
no display line fails to close on its own line, and prose style scans clean at 0 em or en dashes, 0
contractions, 0 prose colons, 0 prose semicolons and 0 parentheticals in body prose.

**Forty-three of seventy-two drafted, none published, publication never authorised.**

---

## What I Did Not Do

**I did not push.** Only the publication review pushes.

**I did not publish**, and I will not without an explicit instruction.

**I did not add equations to the survey section.** The contemporary literature section maps a field and
cites it, and it names no results of its own, so it relies on no relations.

---

## Next

**The primary-reference review of A339**, on your prompt. Nothing else is outstanding.
