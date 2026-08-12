# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-12
**Task**: A334, the Boeing X-37. **Draft pass complete.**
**Committed. NOT pushed**, per the rhythm in which only the publication review pushes.

---

## The Documentary Problem Is the Inverse of Every Previous Article

Thirty-seven articles have struggled with vehicles that left too little trace. **This one has left a
very large trace with a hole in the middle.** Eight missions since 2010, 4,208.57 days on orbit across
the seven completed, dimensions published, durations recorded to the minute, orbits tracked
continuously by amateur observers. **What it carried and what it did are classified.**

**Fourteen records in a harvested pool of 8,905 carry the designation.** Every one is from the 1999 to
2004 space agency phase or was written by outsiders, and **not one describes a flown mission.**

**That makes the fifth thin-cluster reason, and it is distinct from the other four.** The X-33 and X-34
were cancelled, the X-35 won, the X-36 produced a technique rather than a vehicle. **The X-37 did not
stop existing and did not stop working. It stopped being publishable.**

---

## The Route In, Which Is a Measurement Rather Than a Guess

**The orbit is public even when the payload is not.** Every quantitative claim in the article rests on
published dimensions, published durations, public orbital elements and textbook relations. **The
article does not speculate about the payload anywhere**, and says so in its own voice.

**The keystone is endurance, and endurance in orbit is not a propulsion problem.** The central result
converts an operational record into a hardware requirement using nothing but the mission duration and
the orbital period. **908.88 days is 14,140 orbits and therefore 14,140 charge and discharge cycles**,
and at the 40 degree inclination of the first four missions the largest reachable beta angle is 63.44
degrees against a full-sun threshold of 70.22, so **not one orbit is exempt and no phasing provides
relief.**

Inverting an inverse power law for cycle life gives an admissible depth of discharge of **38 to 50
percent across the whole plausible exponent range**, which is routine flight practice. **The record
endurance needs no exotic energy storage.** It needs a conservatively cycled battery of roughly fifteen
kilograms per kilowatt.

---

## Two Independent Public Geometries, Reported as a Bracket and Not as Agreement

The array must fold into a 2.52 square metre bay, which caps the continuous load near **1,164 watts**.
The heat must leave through the doors, which caps it between **540 and 1,623 watts**. **Heat rejection
is the tighter constraint**, which is the usual result for a compact spacecraft and explains why the
doors open on orbit and stay open.

**Both are upper bounds and the article says so repeatedly.** Claiming that two ceilings agree to some
precision would be claiming more than two ceilings can support, so the finding is the bracket.

---

## The Aerobraking Result, and an Estimate of Mine That Was Wrong

Circularising the seventh mission's 38,600 kilometre apogee propulsively costs **2,469.4 metres per
second** against a whole propulsive budget near **310.6**, a ratio of 7.95. **Setting the manoeuvre up
costs 19.9 metres per second**, so the leverage is **124 to one**, and the perigee passes run at about
a fifth of the heat flux of a full entry.

**MY FIRST FEASIBILITY ESTIMATE SAID THE MANOEUVRE WAS IMPOSSIBLE AND IT WAS WRONG.** Holding the
period constant gives 314 passes in the available calendar and demands 7.87 metres per second each,
which no perigee above the entry interface delivers. **The period is not constant.** Every pass lowers
the apogee, which shortens the period, which fits more passes into the same days. The proper walk-down
gives **467 passes and 81.2 days at a 100 kilometre perigee**, which fits.

**Both versions are left standing in the article deliberately**, because the difference between them is
the lesson. The crude estimate held constant the one quantity the manoeuvre exists to change.

---

## An Identity Worth More Than the Number It Supports

In equilibrium glide the vertical balance fixes the lift, so the turn rate and the deceleration carry
the same factor and dividing one by the other removes it. **The heading a vehicle can turn during entry
depends on its lift-to-drag ratio, its bank angle and the ratio of entry speed to terminal speed, and
on nothing else.** Not on mass, not on wing area, not on the atmosphere. Checked against an integration
that retains the term the identity claims cancels, and they agree to four decimal places.

---

## Three Defects Found During Assembly, All of Them Mine

- **A possessive is not a contraction, and my filter forgot it.** A pattern matching any apostrophe-s
  dropped **81 records**, including "X-37 Flight Demonstrator: A Building Block in NASA's Future Access
  to Space", which is among the article's best primary sources. The filter now carries `_verify.py`'s
  own list so the two cannot disagree.
- **A hyphenated compound is not a doubled word.** `\w` excludes the hyphen, so a backreference read
  "Based on On-Orbit Measurement Data" as a repeat and dropped a correct title.
- **A harvested title put a bare pipe into link text**, through a publisher-mangled apostrophe entity
  deposited as `^|^apos;`. **kramdown reads a paragraph whose first line contains a pipe as a table.**
  This is the last member of the delimiter family that included the unbalanced `$$` of A327, the bare
  `\(` of A328 and the stray `>` of A331. **`refs.clean` now strips a bare pipe corpus-wide**, with a
  test, taking `test_lib.py` from 74 to 75.

**All three were found by scanning every reference entry for punctuation that does not belong**, which
remains the only method that has ever worked for this class. Nothing else reported them.

**Six reference works have no author**, and `refs.display`'s title fallback truncates to the same
two-word window an author label uses, so "Experimental Aerothermodynamic Research of Hypersonic
Aircraft" rendered as "Experimental Aerothermodynamic Research of 2018", which reads as a person and a
year. Two of the six are the standard texts for this subject, so they are labelled by title instead of
being dropped. **Where there is an author, `refs.display` is used unchanged.**

---

## The Gate Was Written for This Subject and Both Samples Were Read

**Reading the kept sample found a cardiac radiofrequency ablation trial**, admitted by a bare `ablat`
stem. **Reading the dropped sample found the Global Reference Atmospheric Model and a spacecraft
thermal design paper**, refused because `thermal control` does not match `Thermal-Control`.

Three new noise families were recorded in `_research/homonyms.py`, each with the incident that produced
it: **grid storage and economic dispatch**, which share depth of discharge and cycle life with
spacecraft batteries; **satellite communications networking**, which shares low Earth orbit with
everything this series does; and **the electric road vehicle again**, arriving this time through
battery cycle life rather than propulsion.

---

## Verification

- `python3 _verify.py` **0 errors, 0 warnings**.
- `python3 tmp/a334/verify.py` **34 of 34**, each value re-derived by a route sharing no code with the
  one that produced it. The orbital period comes back from a numerical integration of the two-body
  problem, the eclipse fraction from direct geometric counting, the altitude floor from a scan against
  a bisection, and the perigee-pass drag from a time-domain quadrature against a true-anomaly one.
- `python3 _lib/test_lib.py` **75 of 75**, up from 74.
- `./_check.sh --drafts` **passes end to end**, 504 pages, no findings.
- Identifier sweep, seeded sample of 400: **400 of 400 resolved**, 22 through the issuing registry
  rather than by HTTP, which is the expected Defense Technical Information Center pattern.

**One verifier failure was a real finding rather than a defect.** I asserted that a decaying-orbit
propagation should exceed the fixed-altitude drag budget by no more than fifteen percent. It exceeds it
by **48.4 percent**, because drag is exponential in altitude and every metre lost makes the next metre
dearer. **The band was asserted rather than measured**, the calculation was right, and the gap is now a
reported result about reboost cadence.

---

## Outstanding

**Nothing blocking.** The draft is committed and the working tree is clean.

**The article is NOT pushed**, which is correct for a draft pass. **Publication of the thirty-eight
X-Planes drafts remains unauthorised.**

**For the equation-density pass, which is your next prompt if you want it:** `_lib/audit.py` reports
**14 sections naming numbers with no displayed relation**, the largest being the scale comparison
against the Shuttle orbiter, the solar-cycle bracket and the crossrange table. The draft stands at
**24 display equations**, which is low against a series median of 94 and reflects a subject whose
argument runs through a few relations applied repeatedly. **Report the count and do not pad toward the
median.**

**A background citation verification run was started and had not returned when this was written.** Its
findings belong to the publication review, alongside the 43 mismatch and 89 label-name findings already
recorded as an open decision.
