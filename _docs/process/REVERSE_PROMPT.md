# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A316 publication review, the fourth and final pass. Committed and **pushed**. **Not
published.** All twenty articles in the series remain in `_drafts/`.

---

## A Section Was Missing From the Article Entirely

The genre carries three sections beyond the standard twelve, and **A316 was drafted with only two of
them.** `## The Contemporary Literature` was absent from the article from the draft pass onward, and
every automated check passed it through three passes, because `check.py` counted sections rather than
identifying them.

That is the section this pass exists to write, so the omission surfaced the moment I went looking for
where to put the survey. **`check.py` now names the three required extras and fails if any is missing**,
and also verifies that The Source Base precedes the Epistemic State.

**Three acronyms were also used before expansion**, namely NACA, NASA, and the vertical take-off and
landing abbreviation, the last used some thirty thousand characters before its expansion. That is the
A298 defect recurring. All three are corrected.

---

## The Survey's Claim Is the Opposite of A315's

A315 closed on a configuration that came back because distributed electric propulsion **dissolved** its
keystone, driving the immersed fraction to unity and deleting the problem the article was built on.

**This article cannot make that claim and does not try to.** The X-19's keystone was never wrong. A
propeller in oblique flow develops a force normal to its axis, it did so in 1963, and it does so now.

**What changed is the failure mode, and it was abolished rather than improved.** The X-19 died of a
gearbox, and that gearbox existed only because two engines had to drive four propellers through an
interconnected transmission. Electric propulsion removes the requirement outright. Each rotor takes its
own motor, there is no cross-shaft, no combining box, and no propeller reduction gearbox to fail.

**The cure that killed this aircraft is absent from the modern configuration rather than better
engineered within it.** That is a genuinely different kind of progress from the one the previous article
described, and the survey is organised around the distinction.

---

## The Thinness of the Keystone's Modern Literature Is a Result

Worth flagging because it looks like a gap and is not. A search that returns hundreds of recent papers on
transition corridors returns **four** on propeller normal force.

**That is the signature of a solved problem.** A quantity that is settled stops generating publications.
The modern form of the subject is a simplified model for propeller thrust in oblique flow, or propeller
performance at large angle of attack for compound helicopters, which is a term to include in a simulation
rather than a question to argue. I report it as evidence that Curtiss-Wright's aerodynamic claim is no
longer contested, rather than padding the section to hide it.

---

## Reading the Rejections Caught Three More Families

The contemporary sweep needed three rounds of narrowing, and each round was driven by reading rather than
by any check.

**A bare `gearbox` returns the entire industrial condition-monitoring literature.** The first run of the
drivetrain bucket was fourteen records of fault diagnosis for planetary gearboxes, twin-screw extruders,
a cable-car drive and wind-turbine drivetrains, with almost nothing aeronautical. The bucket was reframed
around the electric powertrain that removed the mechanical interconnection, which is what the article
actually needs.

**A bare rotor-inflow pattern returns at least four fields.** The first keystone bucket held wind-turbine
rotors, a Kaplan water turbine, two axial-flow compressor stages and a generator in a drain pipe.

**Two more survived every rule and were caught by a final scan**, being film cooling of a turbine blade
and an H-Darrieus rotor. The token `VAWT` was in my exclusion list and the machine's own name was not.

---

## Verification

**119 independent re-derivations, zero disagreements**, still reproducing after every edit. 431 reference
definitions, 412 external URLs, zero duplicates or orphans. 234 plain 200s, 122 publisher 403s, 7 202s,
and **15 DTIC DOIs verified through the Crossref registry with matching titles**, none of them marine.

A red-flag scan over all 399 cited titles **and venues**, across eight false-positive families, returned
**zero hits**. `_verify.py` at the 0-error 21-warning corpus baseline with no new warnings. Zero style
violations. Acronym check clean. Section order matches the genre. Isolated build passing with 78 of 78
display blocks rendering as display, 2 of 2 tables, and Part 20 navigation. Equation count measured
before and after and holding at 78.

---

## Final State

**1,200 lines, 78 display equations, 431 references, 11,792 words.** Contemporary coverage is **157 of
399 research citations, or 39.3 percent**. Era spread is 67 pre-1960, 111 across the 1960s and 1970s, 56
in the 1980s and 1990s, eight from 2000 to 2018, and 157 from 2019 onward.

**References at 431 are above the 250 to 380 band.** Lines sit 100 below the 1,300 floor and equations 12
below the 90 floor. **That is the fourth consecutive article to finish outside the named classes on two
of three measures, in the same direction**, and it is the closest any of the four has come on lines.

---

## The Two Things Still Waiting on You

**The A315 marine citations.** A315 cites four naval-architecture papers as aircraft propeller
literature, and its reverse prompt describes one of them, a David Taylor Model Basin study of spindle
torque on a controllable-pitch **ship** propeller, as "directly about the system that failed on the final
flight." **I have not touched A315**, because it is outside what you asked for. It is four anchors and
one sentence whenever you want it done.

**The fourth genre class.** A313, A314, A315 and A316 have now all finished outside every named class on
two of three measures in the same direction, across sixteen passes. I have not amended
`RESEARCH_AIRCRAFT_STRUCTURE.md`, because it defines the series' own standards. Say the word and I will
propose a fourth class with bands drawn from the four.

A317 is the Boeing X-20 Dyna-Soar. Nothing in the series is published and publishing has never been
authorised.
