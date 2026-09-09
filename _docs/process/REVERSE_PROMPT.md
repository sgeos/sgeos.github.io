# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

## Last Updated

**Date**: 2026-09-09
**Task**: **A354, X-Planes: ESAero X-57 Maxwell, researched and written. The first of four
passes.** Committed and **NOT PUSHED**, which is the rhythm. **Not published**, and
publication of the series still not authorised. **Fifty-eight of seventy-two drafted.**

---

## The Longest Entry in the Class Belongs to the Aeroplane That Flew Least

**Of the thirty X designations the register carries, the X-57A has the longest mission
statement at 343 characters**, more than double the median X row. **The aeroplane never
flew.** The programme ran from 2016 to 2023, delivered an aircraft, tested it on the
ground, and closed out without it leaving the runway.

**Five separate counts return one and all return this row**, it being the only entry
naming all electric, propulsion technology, a high lift device, a wing tip or a leading
edge. Four rows mention electricity at all. It is also one of only four rows naming two
contractors joined by the word and.

**And it reads as a specification rather than an intention.** The register's ordinary
grammar is a purpose clause. **This entry explains a mechanism, names its parts, says where
each is mounted and what each is for.** It is the only entry in the register that teaches
the reader how something works.

---

## A Tempting Opening Was Tested and Abandoned

**The engines cell for this row is empty**, which invites the reading that the register had
no category for an aeroplane without engines. **Eighty-eight of 526 rows have an empty
engines cell, and the two other X rows that do are a supersonic demonstrator and a rocket**,
both of which plainly have engines. **The blank is a gap in the compilation.** It is
recorded in the article because it is the first thing an argument would reach for, and
because two of the preceding three articles opened with a uniqueness that measurement had
to take away.

---

## The Wing Is the Argument, and the Prize Is Smaller Than It Looks

**The Mod III wing is 42 percent of the area of the wing it replaced**, 14.76 square metres
becoming 6.19. At the same mass that multiplies the wing loading by 2.38, and holding the
stall speed then requires multiplying the maximum lift coefficient by 2.38. **The twelve
leading-edge propellers exist to supply that factor and nothing else.**

**But cutting the wing to 42 percent did not cut the drag to 42 percent.** Parasite drag
scales with wetted area, and twelve nacelles put wetted area back, so **the wing area fell
58 percent and the wetted area fell 18**.

**And the induced drag went the wrong way.** Induced drag is set by span, not by aspect
ratio, and the new wing has nearly twice the aspect ratio on a shorter span, 9.94 metres
against 11.40. **Induced drag rose 32 percent while parasite drag fell 18.**

**That result was derived here and then found stated independently in the primary source**,
which says the reduction in span led to higher induced drag despite the higher aspect ratio
and increased the importance of the wingtip propellers. **Agreement between an independent
derivation and the source is recorded as a check that passed rather than as a discovery.**

---

## The Published Geometry Does Not Close

**Three quantities describe a wing and two are independent, so a published set of three can
be checked.** For the original wing they agree to better than one percent. **For the new
wing a span of 9.94 metres and an area of 6.19 square metres give an aspect ratio of 15.96
against the 15.0 the same paragraph states**, a disagreement of 6.4 percent. The report
notes the span excludes the wingtip propeller, which would widen the gap rather than close
it. **The article uses area and span, which enter every computation, and does not use the
aspect ratio, which enters none.**

---

## What Actually Stopped It Was Transistors

**Not the wing, not the battery, not the aerodynamics.** The cruise and high-lift motor
controllers used silicon carbide transistors switching at 538 volts and 200 amperes peak
per phase, and they failed three ways. **Vibration**, where the first module could not
survive 7.7 g root mean square for twenty minutes per axis and shorted across the bus.
**Heat**, where a thermal gap pad was too thin, the case wore through it, and the internals
were ejected. **Software**, where an early version commanded shoot-through and a mistuned
control law destroyed all three phases.

**The deck summarising this for a standards committee contains the sentence that describes
the whole programme**, which is that one loose washer can cause catastrophic failure.

**And the lessons learned report gives a root cause that is not technical.** The project was
scoped as an integration effort, so the plan assumed no time or money was needed to develop
subsystems and the team was staffed accordingly. **The readiness assessment rested on access
to overseas flight-proven hardware, and the direction was then given to use United States
industry only.** The report states that the project may have benefitted from reassessing the
readiness of American components, and that it did not. Four subsystems had to be developed
by a team staffed to integrate them.

---

## The Sweep Was Built the Way the Previous Article's Failure Taught It

**A353 named its aeroplane once, beside five generic words, and spent the whole query on the
generic words.** Every proper noun in this harvest was queried alone, and the aeroplane's
own literature came back with it. **Twenty primary documents were curated from NASA's own
published technical papers page before the primary pass**, rather than after it.

---

## The Store Met Its Largest Exposure in This Series, and Two Defects

**Armed as written the store would remove 677 of 5,477 records, being 12.4 percent.**

**ONE FAMILY HAD TO BE TAGGED BEFORE IT COULD BE OPENED.** The pattern removing the rotor of
an electrical machine was added by A347, where it contaminated a rotorcraft survey. **Here
the electrical machine is the subject**, and one of this article's primary documents is an
electromagnetic model of a permanent magnet synchronous cruise motor. The pattern carried no
tag, so there was no handle. One was added and the family opened, taking the residual to
9.9 percent.

**AND A VENUE THAT NAMES FOUR TRANSPORT MODES WAS REJECTING PAPERS ABOUT THE FIRST OF
THEM.** The store joins title and venue before matching, which is right when a venue carries
evidence. **The IEEE conference named for electrical systems in aircraft, railways, ship
propulsion and road vehicles is a principal venue for this exact subject**, and its name
alone removed 31 records, including one titled advanced aircraft electrical systems to
enable an all-electric aircraft, whose own title contains no marine or rail word. **A venue
naming several fields is evidence for none of them.** The marine, rail and road families are
now guarded by a condition that fires only when a string names aircraft alongside another
mode.

**The release is measured as a set difference and the gap is the largest yet.** The
histogram sums to 161 and opening returns 134, because the electrical machine pattern
overlaps heavily with marine and wind energy. **Twenty-seven records are held by a second
armed pattern**, against two in the previous article.

---

## And the Aeroplane Is Named After a Physicist

**Of 126 harvested titles containing the word Maxwell, 26 also mention aircraft, propulsion
or flight and 100 do not.** The store's geophysics family caught the Love numbers of a
generalized Maxwell sphere and a Maxwell-Wagner polarization theory, and its teaching family
caught a study of teaching the Maxwell distribution. **Naming an aeroplane after a physicist
has consequences for anybody who later tries to survey it.**

---

## Verification

**Verifier clean at 0 errors.** Two `progress-stale` warnings stood until the process files
were updated in this same commit, which is the expected order. **Tests 108 of 108**, one
added for the multi-modal venue guard. **Lint 0 findings.** The symbol scanner reports all
34 declared symbols used and every symbol used declared.

**The article verifier runs 110 passing checks and seventeen injected defects were all
caught.** Two of the seventeen needed their anchors corrected first, which was a fault in the
injection harness rather than in the verifier.

**FINAL STATE. 5,551 lines, 16 display equations, 34 declared symbols, 2,567 reference
definitions, 31,980 words**, research 2,451, report primaries 187 at 7.6 percent, one sweep
retrieving 5,477 records, gate 2,538, store residual 9.9 percent. **All 2,567 definitions
are cited, none orphaned and none undefined.**

**The stub-isolated production build succeeded against the exact bytes committed**, the
checksum matched against the stub copy before the build and against both afterwards.
**The rendered audit reports no findings across 93 pages.** Source and rendered
display-equation counts agree at **16**, with zero raw dollar pairs leaking, zero unresolved
reference brackets, zero unexpanded slots and zero unrendered Liquid. The page is 495,906
bytes.

---

## What Is Not Done

**The equation-density, primary-reference and publication passes have not run.** Sixteen
equations is draft strength; the series lands near thirty.

**Two disagreements are recorded and unresolved.** The high-lift motor power is 12.6
kilowatts in the flight performance report and 10.5 in the reference literature, and the
article uses the report. The battery is quoted at 80 watt hours per pound while usable
energy over pack mass gives 55, and the difference between a cell rating and a usable pack
figure is not documented in the sources consulted.
