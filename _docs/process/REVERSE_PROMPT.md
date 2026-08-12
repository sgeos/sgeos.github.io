# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-12
**Task**: A335, the Scaled Composites X-38. **Draft pass complete.**
**Committed. NOT pushed**, per the rhythm in which only the publication review pushes.

---

## The Vehicle That Abandoned the Runway on Purpose

**Six vehicles in this series were built around a horizontal landing and this one was built to give it
up.** The X-23 proved a lifting entry could be steered to a point, the X-24 spent its life on the
unpowered approach, the X-33 and X-34 were sized around runway operations, and the X-37 made autonomous
runway landing routine. **The X-38 flies the same family of shape through entry and then comes down
under 696.8 square metres of ram-air canopy onto whatever flat ground is available.**

**The research question is therefore what a runway costs**, and both sides are computable from published
numbers.

---

## The Answer Is One Ratio and the Mass Cancels Out of It

A lifting body meets a runway at ninety metres per second carrying **45.93 megajoules**. The same mass
under the canopy descends at 17.58 metres per second carrying **1.752**.

**The ratio is 26.2 to one, and it is exactly the square of the speed ratio**, so no property of the
vehicle enters it at all. Everything the runway demands follows from that energy: the speed, the strip,
the gear, and the crossrange needed to reach one of the few places where all three exist.

---

## The Crossrange Argument of Six Articles Is a Consequence of Insisting on a Runway

The parafoil footprint is about **18 kilometres** against the **1,397.8 kilometres** of entry crossrange
the [X-37 article](../../_drafts/x_planes_boeing_x37.markdown) computed. **The ratio of 77.7 to one looks
devastating until the question is asked the other way round.**

**Crossrange exists to reach a runway, and runways are rare.**

| Landing sites available | Reachable per day |
|---|---|
| Runways certified for a lifting body | **0.1** |
| Airfields of adequate length | 4.0 |
| Flat unobstructed areas | **396.1** |

A vehicle needing a certified runway gets an opportunity every ten days. One needing a flat field gets
four hundred a day. **For a lifeboat, availability is the entire requirement**, so a factor of several
thousand in availability is worth a factor of seventy-eight in crossrange.

**These are order-of-magnitude figures and the article says so.** What survives the crudeness is the
direction and the scale.

---

## A Calculation That Failed Produced the Third Result

**The obvious explanation for the five-stage reefing is that a single-step inflation would injure the
crew, and it does not survive being written down.** The steady inflation load admits the whole canopy in
one step at **2.10 g**, and the admissible area at three g is **996.2 square metres** against a canopy of
696.8. Even an opening-shock factor of 2.5 reaches only **5.25 g**, which a restrained crew survives.

**What the failure locates is that the constraint is not the crew.** A canopy of that size cannot
inflate uniformly, the centre cells fill first, the load concentrates on a fraction of the suspension
lines, and the limiting structure is the canopy itself. **Reefing exists to make the inflation orderly
rather than to make it gentle**, and no vehicle-level load model can predict the stage count because the
stage count is not a vehicle-level quantity.

---

## Two Identities Worth More Than the Numbers They Support

**The flare is never limited by energy.** In steady glide the horizontal speed is the vertical times the
glide ratio, so the two kinetic energies stand in the ratio of its **square**, exactly, with no mass, no
area and no density appearing. At a glide ratio of three the forward motion carries nine times what the
descent must lose. **The flare is limited by how fast the canopy converts that energy before it stalls**,
which is a question about the canopy and not about the arithmetic.

**The entry peak deceleration carries no ballistic coefficient.** The Allen and Eggers result gives
**3.87 g** for this entry regardless of the vehicle, and lift relief takes it to 3.02 at a lift-to-drag
ratio of 0.8. **The entry load is a medical constraint rather than a structural one**, which is a
sentence that could not be written about any other vehicle in this series.

---

## The Scaling Exponent Has the Opposite Sign From the Previous Article

Mass scales as length to the **4.207** from the X-24A to the X-38, against 3 for geometric similarity.
The X-37 scaled at **1.924** from the Shuttle orbiter.

**The X-37 shrank and kept its fixed overhead. The X-38 grew because the mission grew faster than the
machine.** Neither pair is geometrically similar and the reasons differ, **which is a warning against
reading a scaling exponent as a property of the technology.** I would not have noticed had the previous
article not measured the same quantity.

---

## The Programme Proved Half the Problem, Precisely

The heaviest drop test came within a factor of **1.021** of the orbital vehicle's sink rate, because sink
rate varies as the square root of mass and the mass shortfall was 4.2 percent. **The landing system was
tested at very nearly its design condition.**

**The entry was never tested at all.** No X-38 went to orbit, none met the atmosphere at orbital speed,
and no thermal protection system was ever exposed to entry heating in flight. V-201 was **90 percent
complete** when the programme was cancelled on 29 April 2002.

**The lifeboat was cancelled because the station shrank to fit the lifeboat it already had.** The
seven-seat requirement disappeared with the station's reduction to a crew of three, which the Soyuz
already served. **That is a sixth distinct reason for a thin record**, different again from cancellation
for failure, from winning, from producing a technique, and from classification.

---

## Verification

- `python3 _verify.py` **0 errors, 0 warnings**.
- `python3 tmp/a335/verify.py` **28 of 28**. The glide speeds come back from a component resolution
  against the resultant form, the energy ratio from the square of the speed ratio with the mass
  cancelled, the area inversion from a scan against a bisection, and the deorbit increment from specific
  energy against vis-viva.
- `./_check.sh --drafts` **passes end to end**, 505 pages, no findings.
- **2,720 reference entries scanned** for stray punctuation, all clean.

**The text check caught a transcription error and that is what it is for.** The draft stated 1,376.6 g
after I first wrote 1,376.7 for a value of 1,376.617.

**Four new homonym families were recorded** in `_research/homonyms.py`, each with its incident: **crack
opening load** in fracture mechanics against parachute opening load, **impact tolerance** meaning
material toughness against human acceleration tolerance, the **parachute flare** as an illumination
munition, and **recovery system** without a parachute context.

---

## Outstanding

**Nothing blocking.** The tree is clean and the article is committed.

**The article is NOT pushed**, which is correct for a draft pass. **Publication of the thirty-nine
X-Planes drafts remains unauthorised.**

**For the equation-density pass, which is your next prompt if you want it:** `_lib/audit.py` reports
**11 sections naming numbers with no displayed relation** and **7 equations with no citation within
reach**. The draft stands at **14 display equations**, which is low and reflects a subject whose argument
runs through a few relations applied repeatedly.

**Two clusters are thin and both are the cluster ordering rather than the literature.**
`vehicle_sizing` is empty and `entry_aerothermo` holds four, because records naming those subjects match
an earlier cluster first. **That is a reporting artefact and the reference pass should fix the ordering
rather than harvest for it.**
