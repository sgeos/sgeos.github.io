# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

## Last Updated

**Date**: 2026-09-08
**Task**: **A352, X-Planes: Lockheed Martin X-55 ACCA, equation-density review. The second of four
passes.** Committed and **NOT pushed**, which is the rhythm. **Not published**, and publication of the
series still not authorised. **Fifty-six of seventy-two drafted.**

---

## Eight Display Equations to Thirty-One, and Working Them Changed Two of the Article's Explanations

**Adding the equations was not the point.** In both cases below the draft had been asserting something
its own arithmetic does not support, and in both cases the correction made the argument stronger
rather than weaker.

---

## The Draft Was Modelling the Wrong Fluid

The draft said that every term in the Darcy relation works against the clock, and named the path
length as the thing at risk. **Two entirely different fluids cross those channels.** Air leaves them
and resin closes them, and their viscosities differ by a factor of **540,541**.

**Air crosses ten millimetres of dry tow in 0.01 seconds, and four hours of vacuum would clear 12.1
metres of it.** The same path takes resin 1.47 hours to fill. **The length of the path was never the
constraint on a part this size**, and because the sweep time goes as the square of the length, a
permeability a hundred times worse would still clear more than a metre.

**What the process actually races is whether the channels are still open when the air needs them**,
which is a question about the resin's viscosity history and therefore about out-time. **The draft had
kept the void mechanism and the out-life argument as two separate arguments**, and they are one.

---

## The Cure Margin Is the Oven, Not the Laminate

The draft said the datasheet's 32.2 percent margin covers laminate thickness among other things.
**A six millimetre facesheet equilibrates in two minutes, which is 0.83 percent of a four hour
dwell.** That is not a margin, it is a rounding.

**Where the margin goes is the oven, and putting a number on it found something the article had not
been counting.** Convective heat transfer in forced turbulent flow scales as the Reynolds number to
the four fifths, and Reynolds number goes with gas density, so an autoclave's pressure buys a factor
of **4.93** in heat transfer alongside its factor of 7.35 in consolidation. **The autoclave's pressure
buys two things at once and the article had counted one.**

---

## The Strongest New Result Is Why the Post-Cure Is Not Optional

**A curing thermoset vitrifies when its own glass transition overtakes the cure temperature, and the
reaction stops there.** Inverting the DiBenedetto relation for the conversion gives the ceiling each
temperature can reach.

| Cure temperature | Conversion it can reach |
|---|---|
| 80 C | 0.667 |
| 120 C | 0.824 |
| 130 C | 0.857 |
| 180 C | 1.000 |

**The registry entry's phrase `low-temperature curing` does not describe a complete process.** It
describes the first half of a two-stage one, and the second stage runs at exactly the temperature the
first stage was chosen to avoid. **That turns the article's central tension from an observation into a
mechanism.**

**The sensitivity was computed rather than asserted.** Two of the three DiBenedetto parameters are
assumptions, and sweeping them moves the 120 degree ceiling between 0.741 and 0.899. **The conclusion
does not move at all**, because the conversion at the post-cure temperature is exactly one for every
combination, vitrification being defined by the glass transition meeting the cure temperature and
nothing else entering that definition.

---

## Surface Tension Locates the Autoclave's Real Advantage

A void's own surface sustains a pressure that grows as it shrinks, so setting that excess equal to the
available consolidation gives the radius below which pressure cannot close a void at all.

**A vacuum bag at Air Force Plant 42 stops at 0.758 micrometres and a full autoclave at 0.103.** The
advantage is not bulk squeezing. **It is reaching voids 7.35 times smaller, and the factor is the
pressure ratio exactly.** A one micrometre void sustains 10.15 pounds per square inch on its own
account, which is 76 percent of everything a bag can bring to bear.

**And the shop rule of thumb turned out to be a derivative.** Composites shops are told that roughly
one inch of mercury is lost per thousand feet of elevation, and differentiating the hydrostatic
balance at sea level gives **1.081 inches**. The rule is low by 8.1 percent and otherwise exactly
right.

---

## A Figure the Draft Pass Deleted Has Come Back With Arithmetic Behind It

The draft's conclusion said the saving only exists on the hundredth aeroplane. **That was a rhetorical
number no checker had ever seen and the draft pass removed it.**

**Dividing the programme cost by the recurring saving puts the break-even between 41 and 409
aeroplanes and at 109 on the middle assumption**, and charging it against a declining learning curve
rather than a flat one pushes the middle case to 210. **The rhetorical figure was approximately right,
which is not a reason to have kept it.**

**The article states plainly that this is not the industrial break-even**, which would weigh the saving
against a production programme's own non-recurring cost rather than against what a demonstrator cost,
and that figure is not available.

---

## The Symbol Table Was a Dict Literal, and a Dict Literal Absorbs a Second Meaning Silently

**Ten symbols had been declared twice and the later declaration simply won.** The whole point of a
declared table is that a second meaning has nowhere to go, and a dict was quietly giving it somewhere.
**This is the article's own defect class turned on the instrument built to catch it.**

Rebuilding the table from a list of pairs that raises on a repeat found **five real collisions**.

- `h` was the geopotential altitude and the sandwich core separation.
- `\lambda` was the atmospheric lapse rate and the DiBenedetto parameter.
- `\rho` was the density of steel and the learning progress ratio.
- `n` was the reaction order, the unit index in Wright's law and the Prandtl exponent.
- `A` was the Arrhenius pre-exponential and the stem of the skin area.

**Every one was renamed in the article rather than declared twice**, which is what the table is for.

---

## Four More Checkers Failed to Discriminate

- **The symbol scanner collapsed `\mathrm{Nu}` to `Nu`** and read `N` and `u` as two undeclared
  symbols. A dimensionless group is one symbol.
- **A nested brace in a subscript defeated its non-nesting parse**, turning `C_{\mathrm{Nu}}` into
  `C_{mathrm{Nu}`. The article now writes the plain subscript.
- **The sweep-time property check compared the rounded figures the prose quotes.** The air sweep is
  quoted to three decimal places, which is a five percent rounding on a hundredth of a second, so it
  **reported the data as wrong when the tolerance was wrong**. That is A342's rule met from the other
  side, and the check now holds the unrounded values to the property and the rounded one to its own
  rounding.
- **A conditional expression inside a dict literal binds the whole entry rather than the value**, so a
  scientific-notation formatter would have emitted something different from what it looked like it
  emitted for a positive exponent.

---

## Equation Citation Coverage Was Audited at the End of This Pass Rather Than the Start of the Next

**Five of thirty-one displays carried no nearby citation, against sixteen of thirty-one in A351.**
Three were genuine promoted subjects and were closed with curated identifiers taken from the harvest,
being the thermal conductivity of a porous composite, the measured effect of autoclave pressure and
vacuum timing, and a thick-laminate cure cycle. **The two that remain are one-line consequences of the
relation immediately above them.**

---

## Counts

| Quantity | Draft | Equations |
|---|---|---|
| Lines | 10,459 | 10,681 |
| Words | 59,764 | 62,552 |
| Display equations | 8 | **31** |
| Reference definitions | 4,970 | 4,976 |
| Research records | 4,874 | 4,874 |
| Report primaries | 308 at 6.3 percent | 308 at 6.3 percent |
| Curated identifiers | 25 | 28 |
| Prose citation labels checked | 61 | 73 |
| Declared symbols | 31 | **102** |

**Verifier clean at 0 errors and 0 warnings. Tests 106 of 106. Lint 0 defects.** The article's own
verifier now runs seven checks and every one was proved capable of failing by injection.

**The stub-isolated production build succeeded in 229 seconds with no Liquid error, against the
exact bytes committed**, the checksum having been matched against the stub copy before the build
started and against both stub and draft after it finished. **The rendered audit reports no findings
across 91 pages.** Source and rendered display-equation counts agree at **31**, with **zero raw dollar
pairs leaking**, **zero unresolved reference brackets**, **zero unexpanded slots** and **zero
unrendered Liquid**. The page is 955,254 bytes.

---

## Flagged for the Later Passes

**THE SURVEY COVERS THIS ARTICLE'S OWN FRAMING PROGRAMME WITH ZERO RECORDS.** Probing the corpus for
`affordability initiative` returns nothing, and the Composites Affordability Initiative is where the
article's central argument comes from. **The article cites it only through two trade-press columns**,
and an AIAA paper carrying the programme's own name exists at `10.2514/6.2000-1379` and is not in the
corpus. **The primary-reference pass should fetch that identifier by hand and harvest around it.**

**A second gap in the same direction.** Laser bond inspection is the technique that programme
developed for exactly the problem this article says unitisation creates, and the corpus holds one
record on it.

---

## Open Questions for the Pilot

**A324's `book_jenkins` label remains the one live repair**, unchanged. **The OpenLibrary work pages
returning Internal Error to a reader** is also unchanged. **And A350 ships a duplicated
`## The Contemporary Literature` heading** at lines 412 and 414, not repaired here because A350 is
complete on all four passes.

**A352 has completed two of four passes and is committed, NOT pushed. Nothing is published and
publication of the series has never been authorised.** The next prompt is the primary-reference review.
