## Last Updated

**Date**: 2026-09-01
**Task**: **A343, Boeing X-46, DRAFT PASS complete.** Committed, **not pushed**, per the rhythm.
Nothing published and publication still not authorised.

---

## The First Aeroplane in This Series With No Published Specification

**The specialist designation directory prints a specification table for the X-45A and the X-45C and
prints none for the X-46A**, stating instead that Boeing disclosed only minimal information about it.
The encyclopaedia entry carries no specification table at all and cites three trade-press articles for
four sentences. **No airframe was ever built.**

**So the article inverts the procedure of the series.** Every other article takes a vehicle and asks
what question it answered. **This one takes a question and asks what vehicle it demanded**, because
the requirement is what the record actually contains.

---

## The Documentation Finding, Which Is the Article's Sharpest

**Figures for the X-46 circulate, and they are the UCAV-N requirement numbers exactly.** A four
thousand pound payload and a six hundred and fifty nautical mile radius are what the aircraft was
asked to do, not what any aircraft was measured doing.

**The distinction between what was demanded and what was achieved collapses whenever nothing was
achieved**, and it collapses silently, because the number does not change when its meaning does. For a
vehicle never built the requirement is the only quantitative material available, so it migrates into
the specification field of every compilation that has one to fill.

**Boeing's own announcement of the aeroplane that replaced the X-46 does not contain the word X-46.**
The 29 April 2003 release names the X-45B as the design being set aside and describes the X-45C as
serving both services. **The naval programme is not cancelled in that document, it is absorbed.**

---

## Sizing a Requirement, Which Is What the Record Allows

**The one constant the aeroplane may legitimately inherit came from the previous article.** A342
measured the Boeing UCAV payload fraction at 0.12297 and 0.12289 across a tripling of payload, and the
mean of 0.12293 fixes the size before any aerodynamics are considered. **A four thousand pound payload
implies 32,539 lb, which is 11.1 percent lighter than the X-45C.**

**The mission then fixes the fuel and the requirement fixes what is left.** Breguet range for the two
cruise legs and Breguet endurance for the loiter give a fuel fraction of 0.5285, so

**the empty-weight fraction demanded is 0.3485**, and no manned carrier aeroplane examined achieves
better than 0.441. **The gap is the crew and everything the crew requires**, and the requirement is a
bet on its size.

| aircraft | fraction |
|---|---|
| Grumman A-6E, land | 0.441 |
| Grumman A-6E, maximum catapult | 0.456 |
| Boeing F/A-18E | 0.477 |
| Lockheed S-3A | 0.506 |

**The three requirement numbers cannot hold at once.** Read as a single profile they imply an
aeroplane of 77,713 lb, heavier at takeoff than an F/A-18E and not a demonstrator anybody was
proposing to land on a deck. **Read as separate capability points they are demanding and achievable**,
and at an empty-weight fraction of 0.42 the aircraft holds 11.03 hours on station at the full radius
against a requirement of twelve. **The record does not say which reading was meant and the article
says so rather than choosing.**

---

## Two Results I Am Reporting With Their Weaknesses Attached

**The carrier constraint reproduces the built span and that is weaker than it looks.** A 130-knot
approach at a maximum lift coefficient of 1.2 and an aspect ratio of 5 gives 48.7 ft against the
X-45C's 48.9. **Three free parameters were chosen to produce it** and other rows in the same table
give 34 to 45 ft, so it is reported as a consistency check and the article says exactly that.

**The comparison aircraft are all manned and all older**, entering service between 1970 and 1999, so a
modern composite airframe should do better than any row. **The comparison establishes that the
requirement is demanding and not by how much.**

---

## The Verifier Caught One Defect and Then Caught Itself

**The article stated a payload fraction of 0.052 where the computation gives 0.051472**, which rounds
to 0.051. The gross mass derived from the same quantity was right, so only the displayed fraction was
wrong. **The table also omitted the empty-weight fraction its rows depend on**, without which no row
is reproducible. Both fixed.

**Then the verifier passed the corrected article while still carrying the old value.** It had the
number hardcoded, so it was checking its own copy. **It now parses the table out of the finished
article**, which is the lesson from A342's presence-check trap applied one level up.

---

## Tooling Notes From the First Article to Use Yesterday's Changes

**`_lib/survey.py` ran on a real article for the first time and reports 0 failures across 36 claims**,
holding every cluster row against both its own citations and the reference data.

**`_verify.py` reports zero errors and zero warnings with the two promoted checks live.**

**Two defects in the inherited scripts were found and fixed.** The gate crashed comparing a string
year to an integer, because Crossref returns a number and the NTRS detail endpoint returns text. And
`assemble.py` asserted more than 5,000 relabelled survey citations, **which is a fact about A342's
pool rather than about the check**, and would have failed on any smaller survey for the wrong reason.
It now scales with the pool.

**A cluster I added split the evidence and was merged away.** A separate carrier-suitability cluster
measured 31 records against the existing carrier cluster's 197, because cluster assignment is first
match wins and the existing pattern is earlier in the list. **Two overlapping clusters for one subject
make both look thin**, so the distinctive vocabulary was folded into the existing one, which now holds
229.

---

## State

**A343 is committed and not pushed. One of four passes complete.** **9,391 lines, 11 display
equations, 4,441 reference definitions, 51,999 words**, of which 6,778 are author prose, a dilution
factor of 7.7. Editorial date 2025-11-21, series index 47, **documentation-poor class**.

**The class was decided from the record and the reasoning is worth keeping.** The genre says the
reduced order is honest where no vehicle was built, but that rule is written for designation anomalies
where the subject is the number and there is no keystone to identify. **The X-46 designation was
assigned normally to a real programme with a contractor, a contract and a documented requirement**, so
there is a keystone and there are systems to dimension. Full order, short sections, explicit statement
of what is unknown.

`_verify.py` zero errors and zero warnings, `lint.py` **zero defects and zero conventions**, reference
integrity zero undefined, zero orphaned, zero duplicate URLs, all 45 numerical checks passing, and
**zero caps-emphasis spans on the corrected instrument**.

**Forty-seven of seventy-two drafted, none published, publication never authorised.**

---

## Next

**The equation-density review of A343 on your prompt**, which is the second of four passes.

**Two content decisions remain yours and both are on published posts.**
`_posts/2026-08-06-native_lowering_coverage.markdown` carries two authored caps-emphasis spans at
lines 879 and 1306, and thirteen published posts carry 1,045 shouted citation titles that `refs.decap`
now prevents at generation but does not repair.
