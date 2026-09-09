# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

## Last Updated

**Date**: 2026-09-09
**Task**: **A353, X-Planes: Lockheed Martin X-56, researched and written. The first of
four passes.** Committed and **NOT PUSHED**, which is the rhythm. **Not published**, and
publication of the series still not authorised. **Fifty-seven of seventy-two drafted.**

---

## The Register Has Three Verbs and This Entry Uses a Fourth

**Of 526 allocation rows, eighteen say demonstrate, five say investigate and one says
validate.** Every one of those verbs takes a capability as its object. **Exactly one entry
uses the verb exhibit, and its object is a failure mode.**

> A remotely piloted, high aspect ratio, flying wing vehicle designed to exhibit multiple
> flutter mechanisms within its flight envelope.

Five separate counts return one and they all return the same row. It is the only entry
naming flutter, the only one using any form of exhibit, the only one naming a flying wing,
the only one naming a high aspect ratio and the only one naming a flight envelope.

**THE OPENING OVERREACHED AND THE REGISTER NARROWED IT, WHICH IS NOW THREE ARTICLES
RUNNING.** The first draft claimed the X-56A is the only entry whose purpose is to produce
an unwanted phenomenon. **It is not.** Two entries name a sonic boom, one names vortices,
two name icing and one names fatigue. **The claim that survives is sharper.** A sonic boom
does not threaten the aeroplane making it. Flutter destroys the structure exhibiting it,
and the X-56A is the only entry whose stated purpose is to produce a phenomenon capable of
destroying the vehicle built to demonstrate it.

---

## The Plural Is the One Clause the Programme Did Not Deliver

**Body freedom flutter was found between 111 and 114 knots depending on fuel state, and
the aeroplane was flown past it under active control.** A second mechanism, coupling the
first symmetric wing bending mode with the first symmetric wing torsion mode, was predicted
from flight data at 138 knots at low fuel and 144 at high fuel.

**Maximum level flight speed is 135 knots.** The second mechanism therefore sits three to
nine knots above anything the aeroplane can do in level flight and is reachable only in a
dive. **The envelope was expanded to 120 knots, eighteen knots short of it.**

**And the reason is recorded and is not aerodynamic.** The programme retrospective states
that the vehicle was capable of likely flying deeper into flutter and possibly getting
close to the second flutter mode, that with only one vehicle left the team became too risk
averse, and that the Air Force Research Laboratory kept the project going just enough to
get past flutter. **The register's plural was defeated by arithmetic about spare
airframes**, and the retrospective's own recommendation is that three vehicles would
likely have been the sweet spot.

---

## The Aeroplane Built to Flutter Was Destroyed by Rotation

**The first X-56A was lost on 19 November 2015 on its first takeoff with flexible wings,
and not to flutter.** It pitched up, stalled and crashed back onto the ground at about
sixty knots, with the flutter boundary fifty knots away and irrelevant.

Two causes, both consequences of the design. **The aeroplane is statically unstable**, so
during rotation the lift arrives well forward of the main gear and produces a positive
pitch acceleration. **And the flexible wings bend up as lift builds**, which gives the tip
a vertical velocity, which reduces the local angle of attack, which reduces tip lift, which
on an aft swept wing is a pitch up moment.

**The programme's own account of why is the sentence worth keeping.** At the time of the
mishaps, a piloted simulation with fully coupled structural dynamics was an active area of
research for the team but was not a requirement for airworthiness, and the coupled models
that existed were built for the up and away condition. **The model was excellent where the
research was and absent where the flying was.**

---

## Four Instrument Defects, and Two Share A352's Root Cause

**THE GATE AND THE REFERENCE LIST WERE READING DIFFERENT STRINGS.** Forty-five harvested
titles carry HTML markup or entities. Every reference definition passes through
`refs.clean`, which is why no published title carries a tag. **Nothing was cleaning the
title the gate reads.** A paper on fixed order robust control was matched against a pattern
for the term it is about, written in markup the pattern cannot see, and refused as off
subject. **A defect that only ever deletes evidence leaves no trace in the output**, which
is why it survived to A353. Cleaning at load recovered fifty-four records.

**CLUSTER ASSIGNMENT IS FIRST MATCH WINS, SO LIST ORDER IS A MEASUREMENT DECISION.** A
general pattern for flutter placed above a specific pattern for flutter suppression
reported the programme's own subject at **19** records. Moving the specific cluster above
the general one it is a special case of reported **325**. **The survey understated the
article's central topic by a factor of seventeen**, and the cause was the order of two
entries in a list.

**A SCANNER THAT CANNOT READ ACROSS A LINE BREAK, AGAIN.** The verifier searched the
extracted text of the flight report for two phrases that are wrapped mid-sentence by
`pdftotext`, and reported the report as not containing what it plainly contains. **This is
A352's colon-scanner defect in a new place**, and the fix is the same, which is to
normalise whitespace once at the source rather than weaken each needle.

**A PRESENCE CHECK WRITTEN AGAINST THE SOURCE RATHER THAN THE ARTICLE.** Two checks looked
for `28 ft` and `54 flights`, which are the source's forms. The prose spells them out as
`28 feet` and `Fifty-four flights`, because the house style does. **The check was
measuring the wrong document.**

**A HORIZON CHECK THAT COULD NOT SEE MOST OF ITS YEARS.** The dateline regex read
`20[2-9]\d`, so 1940, 1964, 2003, 2012, 2015, 2017 and 2019 were all invisible to it.
**Its own non-vacuity guard was the only thing that noticed**, and without that guard it
would have reported a pass while checking almost nothing.

---

## A Tag Broader Than Its Own Name, Which Is a New Case

A351 found that a family can span two patterns. A352 found the converse, that an entry can
span two families. **A353 found the third case.**

The entry was the bare word `dielectric`, tagged `cure-monitoring`. Dielectric cure
monitoring is a real subject and the tag was correct for A352. **But a dielectric barrier
discharge is a plasma actuator and a dielectric elastomer is a soft actuator**, and both
are actuation technologies a flutter suppression survey wants. Opening the tag to reach
them would also have readmitted the binary liquid mixtures the pattern exists for.
**The entry was split so each half opens alone**, and the store is now 135 patterns across
26 families with 35 tagged.

**AND THE NEW TEST ASSERTED THE WRONG THING AND THE SUITE CAUGHT IT.** The first version
claimed that opening `cure-monitoring` readmits the binary liquid records. It does not,
because a second and untagged pattern also covers them. **The store defends that incident
twice**, which is worth pinning rather than a failure, and it was found only because a new
pattern was given a test in the same change.

---

## Verification

**Verifier clean at 0 errors.** Two `progress-stale` warnings stood until the process files
were updated in this same commit, which is the expected order.

**Tests 107 of 107**, one added for the store split. **Lint 0 findings.**

**The article verifier runs seven check groups and every one was proved non-vacuous by
injection.** Nine defects were injected one at a time, being a contraction, a prose colon,
a semicolon, an em dash, a parenthetical, capitals used for emphasis, a wrong register
count, a wrong flight count and a year past the dateline. **All nine were caught, and the
restored article verifies clean.**

**Every count the article states about the register is recomputed from the register**, and
every number attributed to the flight test report is checked against the report's own text
and then checked again for presence in the prose.

**FINAL STATE. 8,378 lines, 8 display equations, 3,971 reference definitions, 49,601
words**, 3,862 curated research records, 275 report primaries at 7.1 percent, one sweep
retrieving 6,477 records, store residual 5.9 percent. **All 3,971 definitions are cited,
none orphaned and none undefined.**

---

## What Is Not Done

**The equation-density pass, the primary-reference pass and the publication review have not
run.** This is the first of four and the draft is deliberately at draft strength, with
eight equations where the series typically lands near thirty.

**The engine disagreement is recorded and not resolved.** The register says P-240 and the
flight test report says P400. **Three different maximum weights appear in three documents
of the same programme**, being 525, 550 and about 480 pounds, and the article states all
three rather than smoothing them.

**The X-56B date is not resolved.** The register says 2019 with its own question mark, and
secondary sources place the flights in 2021. The article records the discrepancy and does
not adjudicate it.
