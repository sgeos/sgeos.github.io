# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

## Last Updated

**Date**: 2026-09-14
**Task**: **A359, X-Planes: Lockheed Martin X-62 VISTA, publication review. The fourth and last
of four.** Committed and **PUSHED**. **Not published**, and publication of the series has never
been authorised. **Sixty-three of seventy-two drafted, nine remain.**

**A CONCURRENT SESSION HAS UNCOMMITTED WORK IN THIS TREE**, being A374 and its
`URL_VERIFICATION.md` entries. Its TASKLOG row and its `draft_summary.md` block were interleaved
with this article's in shared files and could not be separated without destroying one, so they
ride along in this article's commits and the commit messages say so. **Its own draft and its
`URL_VERIFICATION.md` change are left unstaged for it.**

---

## The Scan Found No Drafting History and That Is the First Time

**A322 shipped five sentences of drafting history, A323 six and A358 seven**, every one of the
form `the draft said X and was wrong`. **This article shipped none.** The scan was run over 483
author sentences and returned nothing, which is worth recording because the convention that
produces those sentences, naming a withdrawn claim rather than deleting it, is unchanged. **What
changed is that the equation pass wrote its withdrawals as statements about the subject from the
start**, so there was nothing to rewrite.

## The Superlative Scan Found Four Real Defects

**Seventy-six sentences carried a strong ranking and four of them did not earn it.**

**The article said the X-62A is the fourth or fifth machine in the line of variable-stability
aeroplanes.** That is a count this article never made, and the line includes at minimum the
Cornell and Calspan machines, the NT-33A, the Total In-Flight Simulator, the Learjets and two
European aircraft. **It now says the X-62A is a late member rather than the first, and says
plainly that it does not know how many stand between**, because counting them would mean
settling what makes an aeroplane a variable-stability aeroplane and no source consulted draws
that line.

**It said NASA Technical Paper 1538's appendix gives the actuator lag and rate limit of every
surface.** It gives them for every surface but the speedbrake, which carries a deflection limit
in Table 1 and no actuator anywhere. **The article now says so**, and observes that the omission
is consistent with the speedbrake not being a flight control.

**It said the award record is the only place the older expansion of the acronym survives at
scale.** That is a claim about everywhere and this article searched part of it. **It now says it
is the largest body of text this article searched in which the older expansion still stands.**

**And it called manual control theory's crossover model the strongest single result in the
field.** That is a ranking over a discipline. **It is now described as the field's central
result**, which is what the textbooks call it.

**Three further softenings were made on the same pass**, being `every simulator of every kind`,
`will always show a lumpy record` and `the whole twelve years` against a measured span of 11.6.

## A Formatting Defect the Number Checks Could Not See

**The article printed `the weaker one for the last 4.48` with no unit.** The slot held a number
of years and the sentence supplied no noun. **Every numeric check passed**, because the value
was correct and appeared the expected number of times. **A unit is not a number and nothing in
the suite was looking for one.**

## A Decision Was Recorded in the Process Files and Never Reached the Page

**The equation pass decided not to use the phase-delay parameter of the bandwidth criterion and
wrote that decision into TASKLOG and this file.** It never reached the article. **The
publication review found it by re-reading the closing sections against the process files**,
which is the check that exists for exactly this.

**The article now carries it as a section.** The criterion is the field's own way of turning a
delay into a handling-qualities level and its phase-delay parameter is exactly what the delay
floor should be expressed in. **Deriving that parameter for a pure delay from the definition as
recalled gives half the delay, and the usual summary of the subject says it is the delay.** Those
cannot both be right, **a factor of two is not a rounding**, and the specification that settles
it has not been read. So the article uses the phase margin, which it derives in one line, and
says why the other is absent.

## What the Primary Pass Had Found

**Report primaries 842 to 1,199 and 10.2 percent to 13.9**, after a fourth sweep of 148 narrow
reports-server questions and 42 defence-registry ones. **Every cluster rose.** The keystone rose
least, from 4.0 to 5.5, and **no single venue holds more than 4.8 percent of it**, so it is a
dispersed conference and journal literature and was never a report literature.

**Every one of the 42 defence-registry questions returned exactly 200 rows.** All of them. The
reports server saturated on 60.8 percent and averaged 7.29 against a cap of 10. **The two
registries are limited in different ways and this sweep measured it rather than repeating it.**

**The programme publishes eight papers and a thematic sweep found four**, the four it missed
being the ones whose titles name the systems rather than the aeroplane. Walking two contiguous
identifier ranges recovered all eight and turned up a correction notice on one of them.

**And the school teaches the scale its own aeroplane is measured on.** The USAF Test Pilot School
publishes its Flying Qualities Phase textbook chapter by chapter into the defence registry, and
**Chapter 16 is a reprint of NASA Technical Note D-5153**. It was found by a question about
specifications rather than by looking for it, and it is now the Conclusion's penultimate finding.

## What the Equation Pass Had Found

**From 21 display equations to 45 and from 46 declared symbols to 88.** Its two findings were
that **the column which makes the projector vanish is the column that runs out first**, the flap
saturating at 8.17 degrees of angle of attack where the tail would not until 30.5, and that
**the leading-edge flap's scheduled lead is very nearly cancelled by its own actuator**, the
schedule's pole and the actuator's corner sitting 1.42 percent apart.

## Verification

**Verifier 0 errors and 0 warnings. Tests 117 of 117.** **The article verifier runs 492 checks
and passes all of them**, up from 269 at the drafting pass. **The injection suite catches 281 of
281.** The symbol scanner reports all 88 declared symbols used and every symbol used declared.
**Diction reports 0 constructions above the corpus maximum** across 62 peers on 17,573 words of
author prose. **Zero citation gaps at a nine-hundred-character window. Zero contractions, zero
dashes, zero prose colons, zero semicolons, and no caps emphasis outside engine designations.**

**Identifier verification passes on content**, with 33 quoted phrases held against the saved
copies they were read from, **39 curated identifiers resolved through the registry and compared
against the year their labels claim**, 14 book identifiers held against both recorded title and
recorded author, **a deliberately fabricated identifier resolving to nothing**, and 0 dead
addresses.

**The whole corpus with this article published builds against checksum-matched bytes and the
rendered audit reports no findings across 542 pages.** Source and rendered display-equation
counts agree at 45, with zero raw dollar pairs, zero unresolved reference brackets, zero
unexpanded slots and zero unrendered Liquid.

**FINAL STATE.** **18,645 lines, 45 display equations, 88 declared symbols, 8,749 reference
definitions, 113,876 words.** Four sweeps retrieved 35,837 records of which 30,647 distinct, the
store removed 1,829, the gate admitted 9,012 and refused 19,806, and **every one of the 8,596
records surviving deduplication is cited** across 15 clusters alongside 153 hand-written
definitions. Report primaries 1,199 at 13.9 percent. Median year 2006, range 1927 to 2027, with
85.0 percent at or before the year of the redesignation.

**The probe covers 19 conclusions with one uncovered**, being the claim that the contract record
and the designation register are independent documents that agree, **which has no aeronautical
literature because it is a claim about records** and rests on the two records themselves.

## What the Article Says, in Five Findings

**THE X NUMBER IS NOT IN THE ACCOUNTING SYSTEM.** 73 transactions and 29,085,924.37 dollars over
11.6 years and not one of them calls it the X-62A. The designation appears once in the whole
record and that once falls 23 days past the article's own date, **so the dateline horizon had to
be enforced in the data rather than in the sentence** or the article would have reported the
opposite.

**THE KEYSTONE IS AN IDENTITY AND IT REMOVES THE VEHICLE.** Exact model following holds if and
only if a projector built from the host's control effectiveness matrix annihilates the demanded
change of dynamics. **The rank bound turns that into a count of control surfaces at three per
axis and the aeroplane has three per axis**, the throttle among them because the speed equation
is one of the three.

**THE COLUMN THAT MAKES THE PROJECTOR VANISH IS THE COLUMN THAT RUNS OUT FIRST**, so the
envelope is set by the weakest control and not the strongest.

**THE MACHINE CAN MAKE ANY AEROPLANE SLUGGISH AND CANNOT MAKE ANY AEROPLANE CRISP**, because
every delay in the host lies between the pilot and the simulated response and delays add.

**AND THE ANSWER COMES BACK ON A SCALE WITH TEN BOXES AND NO METRIC**, whose defining paper is
Chapter 16 of the operating school's own textbook.

## What Comes Next

**A360, the X-63**, editorial date 2025-12-08, series index 64. **The register has now been
unofficial for two designations running and the X-63A is the third**, allocated 10.2 months after
this one. **Wait for the pilot's prompt.**
