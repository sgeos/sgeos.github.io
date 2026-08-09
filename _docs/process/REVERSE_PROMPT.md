# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A318, the Northrop X-21A, drafted. The first of four passes. **Committed, not pushed. Not
published.** Twenty-two of seventy-two articles now drafted, all in `_drafts/`.

---

## The Instruction Was to Compute First, and the Computation Overturned the Instruction

The brief said to work the suction power against the drag saving before deciding what the article is
about, because the two would be the same order of magnitude and the sign of the difference would be the
whole story.

**They are not the same order of magnitude.** At the nominal cruise the suction system costs **17.2
percent** of the friction it removes, and the suction coefficient would have to rise to **5.8 times** the
design value before the system stopped paying for itself. In absolute terms it absorbs about 131
horsepower to remove drag worth 763.

So the article could not be about whether laminar flow control pays. **The aerodynamics was never the
difficulty, and finding that out is what made it possible to see what the difficulty actually was.**

---

## Two Results That Came Out of Writing the Relation Down

**The suction drag coefficient does not depend on altitude.** Density enters the mass flow and the
dynamic pressure identically and cancels. What remains is a function of the suction coefficient, the duct
recovery, the machinery efficiency and the Mach number, and nothing else. An aircraft climbing at fixed
Mach carries the same suction penalty at 20,000 feet as at 50,000.

**The penalty falls as the inverse square of Mach number.** The work to recompress a unit of captured air
is set by temperature and the kinetic energy available to pay for it goes as speed squared, so the
penalty runs from 52 percent of the saving at Mach 0.4 to 14 percent at Mach 0.85. **Laminar flow control
is a high-speed technology for a thermodynamic reason rather than an aerodynamic one**, which is why the
application was always aimed at fast subsonic transports.

Neither was in the draft plan. Both came from insisting on the algebra.

---

## The Keystone

**The X-21 is remembered for answering a question it never asked.**

The received account, which is in encyclopaedias, reference works and aviation histories alike, is that
laminar flow control failed on maintenance. The slots clogged, the aeroplane needed constant attention,
and the cost of cleaning exceeded the fuel saved.

[Braslow 1999][braslow], who was the NASA technical consultant to the programme, records something else.
The service-experience objective, one of three the programme was built around, **had not been initiated**
when the money stopped, because the effort had gone into surface tolerance and spanwise contamination.
The advisory group that met in November 1965 recommended a major wing modification before any maintenance
data could mean anything. **That modification was never made**, and the reason recorded is the resource
demands of the war in Vietnam rather than any finding about laminar flow.

The verdict was reached anyway and has outlived everyone who could have said the experiment was not run.

[braslow]: https://www.nasa.gov/wp-content/uploads/2021/04/88792main_laminar.pdf

---

## A Second Finding the Article Did Not Expect

**The testbed could not measure the quantity being argued about.**

The wing is 44 percent of the aircraft wetted area, and the programme guaranteed laminar flow over 70
percent of the wing, so 31 percent of the aeroplane. That is worth about **ten percent in range**. The
case for the technology was a doubling of range and a lift-to-drag ratio above thirty, which requires a
purpose-designed aircraft in which the wing shrinks, the fuel load shrinks and the structure lightens.

**A converted bomber cannot show that, however well its wing works.** The gap is not an error in the
case. It is the difference between laminarising an aeroplane and designing one around laminar flow.

---

## Where the Trouble Actually Was

Spanwise contamination along the attachment line, which arrives already turbulent and which no amount of
downstream suction can fix.

**The sweep that governs it is the leading-edge sweep, not the quarter-chord sweep quoted for the
planform.** At a taper ratio of 0.30 the X-21's 30 degrees becomes 33.2. The attachment-line Reynolds
number then runs from **205 at the root to 113 at the tip**.

That is everywhere inside the band between about 100, below which a disturbance decays, and about 245,
above which it is sustained and propagates. **It is the worst place to be**, because whether the wing
stays laminar depends on how large a disturbance the root, the fuselage junction or an insect happens to
present. And it is highest at the root, which is where the contamination started and where the aeroplane
carries a large fairing to tailor the pressure field.

At a leading-edge radius of 0.012 chord rather than the assumed 0.008 the root reaches 252 and crosses
outright. **Which side of the threshold the wing sat on depends on a geometric detail of about one
percent of chord.**

---

## A Correction to the Secondary Literature

**The figure of 800,000, repeated everywhere as a count of slots, is a count of drilled metering holes.**

The 1963 primary description makes clear that air passes through spanwise slots into milled plenum
chambers, and that from each plenum a large number of small holes is drilled down into the ducts. The
slots number of the order of a hundred and thirty, sixty-eight above and sixty-seven below, between
0.0025 and 0.008 inches wide.

The error does not change the physics and it badly changes the impression, since it converts a precisely
engineered surface into something that sounds like a colander. The handoff carried the same error, having
inherited it from the same source.

---

## What the Harvest Learned About Itself

**Seven percent of the pool had to be discarded for belonging to another discipline, the highest
proportion this series has recorded.**

**The phrase boundary layer belongs to meteorology as much as to aerodynamics.** One query returned most
of a journal devoted to the atmospheric boundary layer, 89 records in all. Operating-room laminar air
flow, crossflow filtration, a co-laminar-flow fuel cell, a double-pipe heat exchanger, micro-riblets on
ship hulls, a Martian entry stability analysis and a Cretaceous stick-insect fossil arrived by the same
route.

**Both directions of the word-boundary failure occurred in the same pass**, which has not happened before.
One pattern matched the letters of a transition-prediction abbreviation inside ordinary English words and
swelled a cluster to 362 records. Another matched the middle of the word **re-duct-ion** and put 73 drag
papers into the pumping cluster. The first failed for want of a boundary and so did the second.

Two further tooling notes. **The NTRS search endpoint returns no authors and no year**, so display text
fell back to title fragments and dragged title punctuation into link text, which then failed the prose
rules. The per-record detail endpoint fixes it and is now called for every record. **Crossref correction
notices are not the paper** and three were being cited in place of the articles they correct.

---

## Verification

- **64 independent re-derivations, zero disagreements.** The verifier uses a tabulated atmosphere where
  the model uses a formula, bisection where the model uses a closed form, and computes the suction
  coefficient by two independent routes that are required to agree. All 22 quoted values confirmed
  present in the text
- **539 references**, zero undefined, zero orphaned, zero duplicate URLs, `research_` block sorted
- **398 DOIs confirmed registered in the Crossref registry** with titles printed and read, and 123
  archive links at HTTP 200. **Zero failures of either kind**
- A residual red-flag scan over all 398 printed titles found six, of which three were dropped and three
  kept as canonical porous-wall transpiration analyses
- `check_any.py` clean on **all 22 articles**, `_verify.py` at the 0-error 21-warning baseline from the
  repository root, with **no new warnings from this article**
- **22-article isolated build succeeds**, with 16 of 16 equations rendering as display math, three
  tables, Part 22 navigation, and no unresolved Liquid. The build script no longer hardcodes the article
  count, which was the constant that arrived one short in A316

---

## State

**A318 has had one of four passes.** The three remaining are yours to prompt.

The article is short by series standards at 827 lines and 16 equations, and deliberately so. It is
reference-heavy already at 539. **The equation pass has a great deal to work with**, since the suction
derivation, the attachment-line criterion and the wetted-area accounting are all stated in the draft in
compressed form.

Nothing in the series is published. The publication-order dependency is now twenty-two deep.

**Still open and unchanged.** The fourth genre class, now six consecutive articles outside all four named
classes. The A305 length offer. Neither touched.
