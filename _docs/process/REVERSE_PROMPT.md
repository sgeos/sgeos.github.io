# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

## Last Updated

**Date**: 2026-09-09
**Task**: **A353, X-Planes: Lockheed Martin X-56, equation-density review. The second of
four passes.** Committed and **NOT PUSHED**, which is the rhythm. **Not published**, and
publication of the series still not authorised. **Fifty-seven of seventy-two drafted.**

---

## Display Equations 8 to 36, and Working Them Produced the Article's Best Result

**Lines 8,380 to 8,554, words 49,601 to 51,338, display equations 8 to 36, declared
symbols 20 to 51.** References unchanged at 3,971, because this pass adds relations rather
than sources.

**THE STRONGEST NEW RESULT IS AN EXCHANGE RATE, AND IT IS EXACT AND PARAMETER FREE.** The
programme's stated goal was thirty to forty percent more aspect ratio, and both halves of
that trade can be computed without knowing anything about the particular aeroplane.

**The prize is induced drag**, which falls as the reciprocal of the aspect ratio ratio.
Neither the lift coefficient nor the span efficiency survives into the ratio, so thirty
percent more aspect ratio is **23.1 percent** less induced drag and forty percent is
**28.6 percent**.

**The price is bending stiffness, and it goes as the square.** Treating the wing as a
uniform cantilever, the first bending frequency falls with the square of semispan and rises
with the square root of stiffness. The short period frequency rises with airspeed. Body
freedom flutter is where they coalesce, so the flutter speed inherits the bending
frequency's scaling exactly. At fixed area, span goes as the square root of aspect ratio,
so **holding the flutter speed requires the bending stiffness to rise by the square of the
aspect ratio ratio**, being **1.69** at thirty percent and **1.96** at forty.

**The structural price is the square of the aerodynamic prize.** A 23.1 percent drag
reduction costs 69 percent more bending stiffness, and stiffness is weight. **That single
relation is the entire commercial argument for this aeroplane**, because if the margin can
come from a feedback law instead, the exponent on the right hand side is what goes away.

**The idealisation is stated rather than buried.** A real wing is not a uniform cantilever.
**What survives is the exponent**, because the fourth power comes from the length scale and
the square comes from the definition of aspect ratio, so the numbers are approximate and
the shape of the trade is not.

---

## Three More Relations That Changed What the Article Could Say

**THE DAMPING GATE BECAME PHYSICAL.** The programme required a closed loop damping ratio
above 0.04 to proceed. Through the logarithmic decrement that is an amplitude ratio of
**0.778 per cycle**, so the gate says a disturbance must lose about **22 percent** of its
amplitude every cycle. **That is a small margin**, and the aeroplane was required to hold it
while flying above the speed at which the same structure, uncontrolled, had none.

**AND THE INSTABILITY PAST THE BOUNDARY WAS BOUNDED BY INVERSION.** The report says that
about two knots past onset the response was approaching test limits by the third open loop
oscillation, and the test limit is not published. **Sweeping the growth factor rather than
assuming it**, a threefold growth over three cycles implies a damping ratio of about
**minus 0.058** and a tenfold growth about **minus 0.121**. Both are the same order as the
positive 0.04 the closed loop had to supply. **The aeroplane was not far past its boundary
in any absolute sense.**

**AND THAT EXPLAINS THE OPEN LOOP WINDOW'S UNIT.** Cycles to double depends only on the
damping ratio, while seconds to double depends on the frequency as well. **A window measured
in cycles means the same thing at every condition and a window in seconds does not.**

**THE ACCIDENT BECAME AN ANGLE.** A wingtip rising at one metre per second at a takeoff
speed of 65 knots loses **1.71 degrees** of local angle of attack. **The deliberate
excitation used to provoke flutter at the boundary was one to one and a half degrees of
control deflection**, so a single metre per second of tip motion during rotation is the same
order of disturbance as the input the programme later used to make the aeroplane flutter on
command.

**AND THE LIMIT CYCLE GOT ITS MECHANISM.** The describing function of a deadband rises
monotonically with amplitude, from zero inside the deadband to unity for a large signal, so
a loop unstable at small amplitude gains authority as the oscillation grows and settles
where the gain restores marginal stability. **The instability is bounded by the nonlinearity
that caused it.**

---

## The Symbol Table Refused Three Collisions

**Rebuilt from a dict to a duplicate-refusing list by A352, it earned its keep again.** The
Zimmerman parameter already owned `\beta_1` as a decay rate and the cantilever eigenvalue is
conventionally the same letter, so the cantilever one became `\kappa_1`. The Zimmerman
parameter also owned `\omega_1` and `\omega_2` as a generic mechanism's two modes, so the
specific frequencies became `\omega_b` and `\omega_{sp}`. **Renaming in the article is the
fix and declaring both is not.**

**THE SYMBOL SCANNER'S FIRST VERSION REPRODUCED ALL FOUR OF A352's SCANNER FAILURES AT
ONCE.** It split the multi-letter symbols `AR` and `EI` into single letters, emptied
`\text{new}` out of a subscript and reported `L_{}`, stripped the digit out of `x_{n+1}` and
reported `x_{n+}`, and read the `h` inside `\dot{h}` twice.

**SO IT DOES NOT TOKENISE ANY MORE.** It removes the declared symbols from each equation,
longest first, and asks whether anything symbol-shaped is left. **That is the question,
stated directly**, and it cannot be defeated by a symbol whose name is longer than one
character. It is proved against all four failure modes by injection, and it reports that all
**51** declared symbols are used and every symbol used is declared.

---

## A Presence Check Went Green Because a Number Had Gone Stale

**THIS IS THE DEFECT `survey.py` EXISTS TO PREVENT, AND IT REAPPEARED IN A NEW COSTUME.**

Almost every derived number in this article appears twice, once inside a display equation
and once in the prose that interprets it. The verifier asserted presence by looking for the
bare substring. **An injection that changed the PROSE from `about minus 0.058` to `about
minus 0.048` sailed straight past a check looking for `0.058`, because the equation still
contained it.**

**So the expected prose is now built from the computed value and then looked for.** Each
assertion names a phrase that exists only in the prose, so the equation cannot satisfy it on
the prose's behalf. **Eight such phrases are pinned and all eight were proved to bite.**

---

## Equation Citation Coverage Was Audited and Closed

**An equation is a claim and a claim needs a source.** The first audit after placement found
**twenty of thirty-six uncited** within two paragraphs, which is worse than A352's five of
thirty-one, because dense runs of equations push the section's citations out of range.
**Sources were added adjacent to every block and the count is now zero of thirty-six.**

---

## Verification

**Verifier clean at 0 errors and 0 warnings. Tests 107 of 107. Lint 0 findings.**

**The article verifier now runs 124 passing checks across eight groups.** Eleven defects
were injected one at a time and all eleven caught, being a contraction, a prose colon, a
semicolon, an em dash, a parenthetical, capitals used for emphasis, a wrong register count,
a wrong stiffness factor, a wrong drag reduction, a wrong damping inversion and a year past
the dateline. **A further eight injections against the rebuilt prose figures were all
caught.**

**FINAL STATE. 8,554 lines, 36 display equations, 51 declared symbols, 3,971 reference
definitions, 51,338 words**, research 3,862, report primaries 275 at 7.1 percent.

**The stub-isolated production build succeeded in 168 seconds with no Liquid error, against
the exact bytes committed**, the checksum matched against the stub copy before the build and
against both afterwards. **The rendered audit reports no findings across 92 pages.** Source
and rendered display-equation counts agree at **36**, with zero raw dollar pairs leaking,
zero unresolved reference brackets, zero unexpanded slots and zero unrendered Liquid. The
page is 748,231 bytes.

---

## What Is Not Done

**The primary-reference pass and the publication review have not run.** References are
unchanged from the draft pass at 3,971, and report primaries stand at 275 or 7.1 percent,
which is where the next pass will work.

**Three disagreements remain recorded and unresolved**, being the register's P-240 against
the report's P400, three maximum weights across three documents of the same programme, and
the X-56B's questioned 2019 date against 2021 flight dates in secondary sources.

**The wing area and the modal frequencies are still not published**, which is why the
central trade is derived as a scaling law rather than evaluated numerically. The aspect
ratio of approximately fourteen comes from secondary sources and every quantity resting on
it is flagged as approximate in the article.
