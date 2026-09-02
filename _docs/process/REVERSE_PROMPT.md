## Last Updated

**Date**: 2026-09-02
**Task**: **A346 draft pass, the first of four.** Committed and **not pushed**, per the rhythm.
**Not published**, and publication of the series still not authorised.

---

## Compounding Fixes One Half of the Rotor and Not the Other

**A rotor in forward flight is asymmetric in two independent ways and only one of them responds to
compounding.** The advancing blade sees tip speed plus flight speed, the retreating blade the
difference.

**Offloading lift to a wing relieves the retreating blade**, which is what the X-49A demonstrated. It
reached an advance ratio of **0.441** where a conventional rotor gives out near 0.40.

**The advancing tip does not care how much lift the blade is carrying.** It is a compressibility
problem set by $\Omega R + V$, and at the demonstrated 190 knots it is already at **Mach 0.938**. At
the never-exceed speed it is at **Mach 0.984**.

**Neither a drag clean-up nor a third engine moves a Mach number.** The only remaining variable is
rotor speed, and holding Mach 0.90 at Vne would need it **12.8 percent lower**, which is a different
aeroplane with different dynamics and a fresh clearance to earn.

---

## The Constraint Was the Transmission, Not the Engines

**Two T700s deliver 3,800 shaft horsepower into a main gearbox rated at 3,400.** Four hundred
horsepower, **10.5 percent of what the engines make, cannot reach the rotor**.

**That explains the shape of the unbuilt phase two**, which added a third engine to drive the ducted
propeller DIRECTLY. It was never about total power. It was about routing power to the propulsor
without passing it through a gearbox already at its limit.

---

## The 1965 Aircraft Was Faster, and That Is the Wrong Comparison

**The 16H-1A Pathfinder II reached 225 mph in 1965 on one 1,250 horsepower turbine at 10,800 pounds.
The X-49A reached 218.65 mph in 2008 with 1.342 times the power per pound.** Six and a third miles
per hour slower, forty-two years later.

**The article opens with that and then argues it is not the indictment it looks like.** The 16H-1A was
a clean-sheet compound. **The X-49A was a production naval helicopter with a duct and a wing bolted
on**, flown inside the envelope that helicopter was already cleared to, hub in the breeze and gear
down.

**Read as a retrofit study the numbers line up**, at 1,600 pounds and **11.7 percent of empty weight**
against halved vibration and hover within 3.7 percent of prediction.

---

## The Designation Was Skipped on Purpose

**DARPA asked for X-50 for the Dragonfly on the reasoning that it would be the first true fifty-fifty
marriage of helicopter and aeroplane.** The number 49 was left vacant to achieve that and was filled
in 2004 when Piasecki's programme transferred from the Navy to the Army.

**One consequence is bibliographic.** The specialist designation directory that has supplied a
specification table for every previous aeroplane in this series **runs straight from X-48 to X-50**.
This is **the first article in fifty with no entry in that source**.

---

## A Lesson Recorded as Prose Is Not an Instrument

**A344's publication review reported that its refused records included a substantial literature on
estimating the weight of a foetus.** That went into three process files as prose and into the shared
homonym store not at all.

**A346 made `weight estimation` an anchor, because what a modification costs is one of its arguments,
and thirteen clinical records walked in** — foetal weight estimation by Johnson's formula, the
accuracy of parental weight estimation for children. **The pattern is now in the store**, with the
turbomachinery sense of rotor dynamics and the polymer and surfactant sense of drag reduction.

**This is the same failure shape as the TASKLOG count trap found this morning**, where a paragraph
warning that a block goes self-contradictory sat eleven lines above the contradiction. **A warning
addressed to a reader is not a check, and an observation recorded in prose is not a filter.**

---

## Three Gate Passes, and the Third Is Larger

| Pass | Kept | Dropped | What changed |
|---|---|---|---|
| 1 | 4,027 | 1,693 | the gate as first written |
| 2 | 3,974 | 1,665 | three homonym families added |
| 3 | 4,007 | 1,611 | the duct anchor broadened |

**The third pass grew because the second anchor family was too narrow.** The gate refused
`Incompressible Potential Flow About Axially Symmetric Ducted Bodies`, which is duct aerodynamics
exactly, because the pattern demanded a specific noun after `ducted`. **Fifty dropped records carried
the bare form.** Broadening admitted them and let in two families now in the store, being the ducted
rocket and ramjet of solid-propellant propulsion, and domestic air conditioning.

---

## State

**A346 is committed and NOT pushed. One of four passes complete.** **8,035 lines, 13 display
equations, 3,815 reference definitions, 44,075 words**, of which 5,026 are author prose. Editorial
date 2025-11-24, series index 50, **full-aircraft class**. Research 3,744, report primaries **781 at
20.9 percent**, median publication year 2007.

`_verify.py` zero errors, `lint.py` **zero defects and zero conventions**, reference integrity
**3,815 used and defined, zero undefined, orphaned or duplicate**, every stated value re-derived by a
verifier that does not import the computation, **all four advance-ratio rows parsed out of the article
and checked in three columns**, **the published hover tip Mach number of 0.65 reproduced
independently from rotor geometry**, all 16 survey rows agreeing across three counts, **49
back-references with zero forward references** and the X-50 cited externally rather than by
`post_url`, and zero contractions, colons, semicolons, dashes, parentheticals or caps-emphasis spans
in authored prose. **`_lib` tests are 95 of 95.**

**No production build was run**, which the draft pass does not require.

**Fifty of seventy-two drafted, none published, publication never authorised.**

---

## Next

**A346's equation-density review**, the second of four. The article carries **13 display equations**.
**The equation pass should look hardest at the duct**, which is the one major component the article
describes without computing anything about, and at the lift-sharing between rotor and wing in forward
flight, which is currently asserted qualitatively and is the mechanism the whole argument rests on.
