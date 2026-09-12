# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

## Last Updated

**Date**: 2026-09-12
**Task**: **A357, X-Planes: Generation Orbit X-60, equation-density review.** The second of
four passes. Committed. **Not pushed and not published**, and publication of the series
still not authorised. **Sixty-one of seventy-two drafted, eleven remain.**

---

## Forty-Seven Display Relations to Eighty-Two, and Eighty-Four Symbols to a Hundred and Twenty-Six

**THE RULE IS THAT A RESULT THE PROSE NAMES MUST BE SHOWN.** The audit read every sentence
making a relational or quantitative claim and asked whether the relation behind it was
displayed. **Thirty-five were not**, and each is now placed where the prose relies on it.

## The Section Carrying the Article's Central Claim Had No Equations At All

**THE CRUISE ARGUMENT WAS ENTIRELY PROSE.** The register says the X-60A tests at cruise
flight conditions, the article's answer is that no steady state exists, and the whole of that
answer was written in words. It is now five relations. The thrust must balance drag plus the
component of weight along the path, that fixes the required flight path angle, and the
largest the weight term can be is the whole weight in a vertical climb, so the test does not
depend on the trajectory.

**The required sine is 3.19 at 500 pounds per square foot, 3.02 at a thousand, 2.79 at
the published condition and 2.66 at two thousand.** All four exceed one, which is the largest
a sine can be, so the impossibility holds at every dynamic pressure in the corridor rather
than at the one the draft happened to evaluate.

**And the injector relation is now displayed rather than named.** The draft said the injector
pressure drop falls with the square of the flow rate. **A throttle ratio therefore costs the
square of itself in stiffness**, so twenty percent thrust leaves 4 percent of the rated drop,
ten percent leaves 1, and five percent leaves 0.25. That is the quantitative reason deep
throttling is an engine programme rather than a control setting.

## The Statutory Definition Has a Second Half and the Draft Never Tested It

**51 U.S.C. 50902(24) DEFINES A SUBORBITAL ROCKET BY TWO CONDITIONS AND THE DRAFT CHECKED
ONE.** The thrust-against-lift clause was integrated. The requirement that the vehicle be
*intended for flight on a suborbital trajectory* was not, and the statute defines that term
too, at 50902(25), by the vacuum instantaneous impact point.

**That is a two-body problem with a closed-form answer.** The burnout state gives a specific
energy and a specific angular momentum, those fix the coasting ellipse, and the ellipse
either reaches the surface or it does not.

**Burnout is at 1,805.9 metres per second and 24,209 metres. The ellipse has a semi-major
axis of 0.515 Earth radii and an eccentricity of 0.9477, giving a perigee radius of 171,811
metres**, which is about 6,199 kilometres below the surface. The impact point is not merely
on the Earth. It is deep inside it. **Burnout speed is 22.9 percent of circular orbital speed
and 5.2 percent of the kinetic energy**, which is the quantitative form of the observation
that an endoatmospheric testbed and a launch vehicle are not the same kind of machine.

**Both halves of the definition are now satisfied and neither was satisfied by assertion.**

## Why the Corridor Is a Dynamic Pressure Band, Written Down

**THE DRAFT ASSERTED THAT A SCRAMJET'S THRUST FOLLOWS THE AIR IT SWALLOWS AND LEFT IT
THERE.** The captured mass flow per unit area is twice the dynamic pressure over the flight
speed, which is why the corridor is a statement about what the engine can breathe.

**And the flux falls as the Mach number rises at fixed dynamic pressure**, from 97.0
kilograms per square metre per second at Mach 5 to 59.8 at Mach 8, because the same $q$ is
delivered at a higher speed and therefore a lower density. **An engine that wants more air as
it goes faster has to be flown deeper into the atmosphere**, which is the tension the corridor
exists to manage and which the draft never stated.

## Three Draft Claims Were Approximate and Are Now Computed

**THE DRAFT SAID A CARRIER AIRCRAFT LIFTS THE ROCKET ABOVE THREE QUARTERS OF THE
ATMOSPHERE'S MASS.** The column mass above an altitude is its pressure divided by gravity, so
the figure was always computable and was not computed. **It is 80.9 percent**, leaving 1,978
kilograms per square metre overhead against 10,332 at sea level. The article records that the
estimate was easy to compute and was not.

**The draft said the Mach 8 mass budget gives a structural coefficient a real expendable
stage achieves.** Directionally right and imprecisely put. **The coefficient is 18.0 percent
against 8 to 12 for an expendable upper stage**, so the hardest case here is *more generous*
than a launcher stage has to be. **The budget closes with room, which is the opposite of the
answer the calculation was expected to give.**

**And stagnation temperature is not what a wall reaches.** A surface in a moving boundary
layer recovers only part of the rise, set by the Prandtl number, so the turbulent recovery
temperature at Mach 6 is 1,639 kelvin against a stagnation value of 1,811. **The correction is
9.5 percent and it runs the safe way.**

## The Throat the Record Does Not Publish, Traded Rather Than Invented

Neither chamber pressure nor throat area is published. Characteristic velocity ties them
through the mass flow, so **one unpublished quantity can be traded for another**. The product
of chamber pressure and throat area is 14,078 newtons, which puts the throat at 66.9
millimetres across at four megapascals, 50.6 at seven and 42.3 at ten. **An oxygen-rich staged
combustion cycle exists to run at the higher end**, so the throat is probably nearer the last
figure, and the article says it does not know which.

## The Build-Time Law Is Now Displayed With Its Exponents

The citation budget rests on a measured cost curve and the draft quoted its exponents without
showing the relation that produces them. **The exponent between 500 and 2,000 definitions is
2.18 and between 2,000 and 4,500 it is 3.04**, and extrapolating the second to the first
assembly's 10,882 definitions predicts 25.1 minutes for the markdown alone, which is
consistent with a build that had consumed over thirty minutes of processor time when it was
stopped.

## Four Repairs to the Shared Instruments

**THE A353 BLOCK-SLOT ASSERTION WAS ONE-SIDED.** It refuses a slot with text before it on the
same line and said nothing about text after it. **A relation glued to the front of a sentence
fails in exactly the same way**, and this pass produced one, giving an unclosed display fence,
163 fence lines and one display equation fewer than the article declared. **The assembler's
own summary line was again the only thing that noticed**, which is how A356's unplaced
equation surfaced. The check now looks both ways, and the verifier refuses an odd fence count
outright rather than letting integer division hide it.

**THE PLACEMENT CHECK SCANNED THE BODY AND NOT THE EMITTED BLOCKS.** Three relations belong in
the source base, where the budget they justify is explained. **A check that inspects a subset
of its subject reports a clean subset.** It now scans the body with the emitted blocks in it.

**`make_stub.sh` NOW REFUSES WHILE THE INJECTION SUITE HOLDS THE ARTICLE.** The suite rewrites
the draft in place for each injection, so a stub taken while it runs may faithfully copy a
deliberately corrupted article, and **the checksum guard cannot catch that because both copies
are the same corrupt bytes**. This pass did exactly that and built for four and a half
minutes before the post-hoc comparison of the draft against the frozen checksum caught it.
The suite already wrote a lock and the stub builder now honours it.

**AND `min` AND `max` WERE NEVER IN THE SYMBOL SCANNER'S OPERATOR LIST**, so a declared `m`
and `n` ate the letters out of them and the scanner reported a bare `i`.

## A Duplicate Computation the Collision Guard Could Not See

`calc2.py` and `calc4.py` both compute the inert mass, under two different names. **The
assembler's collision guard compares keys and these keys differ**, so it saw nothing. The
agreement is now asserted in the file that came second. The guard did fire correctly on a
genuine key collision, refusing `span_over_diameter` when it was defined twice with values
that would have differed, 3.67 against the converged 3.39.

## The Injection Suite Found the Same Defect Twice in One Article

**FIFTY-NINE OF SEVENTY-SIX ON THE FIRST RUN AFTER THE PASS.** All fifty-six original
injections were still caught and every one of the seventeen new ones was missed, because
thirty-five relations and their numbers had been added with no article-side checks at all.
**Adding content without adding checks is how an article acquires unverified prose**, and it
is the defect the suite found in the draft pass met a second time in the same article.

With the checks added the suite is **76 of 76** with the total reassembly check disarmed.

## A Number in the Previous Reverse Prompt Was Wrong

**THE DRAFT PASS REPORTED 251 ARTICLE CHECKS AND THAT WAS ARITHMETIC ON AN ESTIMATE RATHER
THAN A COUNT.** The verifier now runs **235 checks, measured** by counting its own output
lines, and it ran fewer than that before this pass added thirty. **A figure about the
verification apparatus is exactly the kind of figure this apparatus exists to stop anyone
guessing**, and it was guessed, in a commit message and in three process files. The count is
measured here and the method for measuring it is one shell command.

## Verification

**Verifier 0 errors and 0 warnings. Tests 112 of 112. Lint 0 defects and 1 convention
finding**, which is 164 display equations spanning several source lines and is the intended
form. **The tall-bracket false positive the draft carried is gone**, because the one relation
that produced it now keeps its bracket on a single line.

**The article verifier runs 235 checks and passes all of them**, measured rather than
estimated. **The symbol scanner reports all 126 declared symbols used and every symbol used
declared.** **76 of 76 injected defects caught** with the total reassembly check disarmed.

**The stub-isolated production build succeeded in 173 seconds against checksum-matched
bytes**, run after the injection suite released the article rather than beside it. The
rendered audit reports no findings across 96 pages. Source and rendered display-equation
counts agree at **82**, with zero raw dollar pairs, zero unresolved reference brackets and
zero unrendered Liquid. The page is 905,719 bytes.

**FINAL STATE. 10,524 lines, 82 display equations, 126 declared symbols, 4,628 reference
definitions, 64,907 words**, research 4,501, report primaries 1,430 at 31.8 percent, three
sweeps retrieving 38,596 records of which 31,527 distinct, gate 11,149 under a 4,500 citation
budget.

## What Remains

**A357 has completed two of four passes.** The primary-reference review and the publication
review are separate pilot prompts and have not been run.

**Two repairs are still awaiting a pilot decision.** A350 carries a duplicated
`## The Contemporary Literature` heading at lines 412 and 414, and A324 carries a malformed
`book_jenkins` label over a correct key.

**And the fourth-article format decision carries forward.** A352 through A355 present no
per-cluster record count in a shape the corpus check can read, which leaves approximately
fifty rows outside the corpus gate.

**Nothing is published and publication of the series has never been authorised.**
