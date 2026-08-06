# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-06
**Task**: A306, the Bell X-9 Shrike, drafted, verified, and **committed**. Not pushed, per the
draft-pass convention. Not published. All ten articles in the series remain in `_drafts/`.

---

## The Keystone

Every vehicle in this series so far has had a keystone that is ultimately physical. Transonic drag
rise, aeroelastic divergence, shielding mass, ramjet combustion, atmospheric optical depth. Each is a
question about the behaviour of matter.

**The X-9's binding unknown is a control loop, and its specification is a probability.** The military
characteristics of 15 July 1945 asked for a missile that would strike within 500 feet of its target 75
percent of the time. Read as a Rayleigh distribution that is an axis standard deviation of 91.5 metres
and a circular error probable of **108 metres at a hundred miles**. Every subsystem is then specified
in metres of miss distance, contributions add in quadrature, and the design activity is the allocation
of that budget rather than the pursuit of a performance figure.

The contrast with the article before it is the cleanest in the series so far. **The X-8 had to bring
data back. The X-9 had to take a command out.**

---

## The Central Technical Claim

A radar resolves an angle, so its cross-range position error is proportional to range. That single
fact cuts in opposite directions depending on which end of the engagement the radar sits at.

Guiding from the launch aircraft makes the error grow with the standoff distance the weapon exists to
buy. Guiding from the missile makes it shrink throughout the approach. **The two architectures have
opposite error gradients**, and setting the launcher-guided resolution equal to the whole error budget
gives a maximum useful range of about 72 kilometres against the X-9's demonstrated 80. That
correspondence is close enough to state and too loose to press, and the Epistemic State says so.

It is also why the operational weapon was named for its guidance link rather than its warhead or its
airframe. RASCAL stands for radar scanning link, and the link carried a radar picture from the missile
back to an operator in the launch aircraft. **The sensor rode the missile and the judgement stayed
behind.**

---

## The Founding Irony Is Datable

The accuracy requirement was published on **15 July 1945. Trinity was fired on 16 July.**

Inverting the damage function shows what that timing cost. A nuclear warhead with a 1,500 metre lethal
radius needs a circular error probable of 823 metres for a 90 percent kill probability, against the
108 metres the specification demanded. **The requirement was about eight times tighter than the weapon
that eventually flew actually needed**, because it was written for a conventional warhead one day
before anyone knew the other kind worked.

That does not make the X-9 pointless. It relocates its value, since the accuracy work was largely
surplus to the nuclear mission and directly applicable to everything after it, while the reliability,
the launch procedures, and the trained crews were not surplus at all.

---

## Three Results the Sources Do Not State

**The operator cannot be given the control surfaces.** The airframe's short-period frequency is 7.5
radians per second against a human operator's maximum crossover of 2.6, so the missile is three times
faster than the man flying it. An inner autopilot loop is forced by two time constants rather than
chosen by preference.

**Only terminal errors matter.** A guidance time constant of 0.83 seconds, summing the operator, the
autopilot, and the airframe, means the loop needs about eight seconds of flight remaining to null an
error, which at Mach 2 is five kilometres. Every error still present inside that radius arrives at the
target, which reorganises the whole budget.

**A one watt transmitter on the missile is worth more than a hundred kilowatts on the aircraft.**
Replacing the fourth-power skin-return law with the beacon's second-power law is worth a factor near
10 to the 5 at eighty kilometres, and it is the single most consequential decision in a
command-guidance system.

---

## A Rule That Finally Cost Nothing

**No author key was guessed from a document title in this article.** I resolved the anchor index from
harvest metadata before drafting rather than after, and every one of the 239 anchors landed correctly
on the first attempt.

That defect cost twenty corrections in A305 and appeared in three articles before it. The remedy turns
out to be ordering rather than care, which is worth recording as a method rule rather than as a
resolution to be more careful.

The link-text invariant adopted during A305 caught both display-string collisions automatically.
Reading still found two seams no check flagged, being an insertion that split an argument from its
conclusion and another that orphaned a citation from its subject.

---

## Verification

**All 62 worked numerical values re-derived independently from their stated inputs, with no
corrections required.** That is a first for this series, and I attribute it to computing the numerics
before writing rather than while writing.

239 references with zero undefined, zero orphaned, and zero duplicate URLs. All 70 fixed identifiers
at 200. All 124 DOIs Crossref-resolved on title at the 0.85 threshold with zero flagged. `_verify.py`
at the 0-error 21-warning corpus baseline. Zero style violations, zero doubled words, zero
display-math seam defects. Isolated build succeeding with 88 rendered display blocks and Part 10
navigation.

---

## Densities Are Just Under Band and I Did Not Pad

**1228 lines against a 1300 floor, 88 equations against 90, and 239 references against 250.**

All three shortfalls are small and all three are reported rather than filled. The equation-density and
reference-density passes exist to close exactly this gap, and after A305 came in at 2226 lines and 200
equations I would rather approach the band from below than overshoot it again.

Primary technical documents are already **125 of 229 external references, or 54.6 percent**, which is
the highest in the series at a draft stage. The reason is structural rather than lucky. A weapon
programme reports to a service that keeps its reports, and the defence archive holds Bell's own
project documents covering the Shrike and the RASCAL together. Contemporary coverage at 22.9 percent
of dated references is the clearest deficit for the later passes.

---

## State

**Committed, not pushed.** Nothing in this series is published.

Ten articles complete of seventy-two. **The publication-order dependency is now ten deep**, A306 back
to A297.

**Categories remain undecided** at `aerospace history engineering`, ten articles deep and raised nine
times.

A307 is the North American X-10, which is the Navaho missile testbed and therefore the third
consecutive vehicle that is not an aircraft, and the first that was large enough to take off and land
on its own undercarriage.
