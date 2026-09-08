# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

## Last Updated

**Date**: 2026-09-08
**Task**: **A352, X-Planes: Lockheed Martin X-55 ACCA, researched and written. The draft pass, the
first of four.** Committed and **NOT pushed**, which is the rhythm. **Not published**, and publication
of the series still not authorised. **Fifty-six of seventy-two drafted.**

---

## The Registry Entry Is a Manufacturing Statement, and It Pulls Against Itself

**The X-55A was allocated on 19 October 2009 to validate `extreme time and cost compression in
airframe manufacture using large, unitized composite structures fabricated using low-temperature,
out-of autoclave curing techniques`.** Of the 526 allocation rows in the addendum it is **the only
entry naming manufacture, the only one naming fabrication, the only one naming a unitized structure
and the only one mentioning an autoclave**. Ten others name cost and every one of them describes a
vehicle that is itself cheap. **In those entries cost is an adjective on the article. In this one it
is the dependent variable.**

**And the two halves of that sentence do not point the same way.** Low-temperature curing costs time.
The MTM45-1 datasheet offers twenty hours at eighty degrees and two hours at a hundred and thirty,
and **fitting an Arrhenius law to those two lines gives 54.5 kilojoules per mole**, which sits in the
published range for epoxy amine systems. **The fit then predicts the datasheet's third entry**, four
hours at a hundred and twenty, at 3.02 hours, a margin of 32.2 percent that is exactly what a process
specification carries for thickness and thermal lag. **A cure schedule is not a kinetics prediction.**

**Counting the mandatory post-cure, the low-temperature route costs three times the oven dwell of the
autoclave route it replaces, and the lowest-temperature option costs eleven times.** So the time
compression cannot have come from the cure. It comes from part count.

---

## The Schedule Is the Half That Failed, and the Cause Was the Technology

**Twelve months were asked for and about twenty were taken**, an overrun of roughly two thirds. The
cause is documented. **The skin on the lower fuselage did not bond satisfactorily and a second
fuselage had to be built.**

**An aeroplane designated to validate extreme time compression lost the better part of a year to a
defect in the process it existed to validate.** The cost half held, and the trade press recorded the
programme at the time as seven months late and on budget.

**And the two claims were never symmetric.** The cost claim compares against an estimate of an
aeroplane nobody built. The schedule claim compares against a date.

---

## The Fastener Arithmetic Locates the Saving Somewhere the Demonstrator Cannot Reach

Three hundred structural parts against three thousand, and four thousand fasteners against forty
thousand. **Thirty-six thousand fasteners were not installed**, and at two to ten minutes each and a
hundred to two hundred dollars an hour that is **0.24 to 2.44 percent of the 49,097,981 dollar Phase
II contract**. The range spans a factor of ten and the answer stays small.

**The saving is real and it is recurring.** A fastener eliminated is worth its installation cost every
time an aeroplane is built, and the demonstrator is a run of one. **The X-55 could not in principle
measure the quantity in its own mission statement.**

---

## A Suspicion Failed and the Failure Is in the Article

**The first version of the autoclave argument said no autoclave was large enough.** Working the
pressure vessel scaling gives **18.4 tonnes of shell** for a vessel that would take a sixty-five foot
fuselage half, which is an ordinary industrial machine. **The size argument is real at launch-vehicle
scale and false at this one**, and the real reasons had to be stated instead.

**The steel goes as the cube of the diameter**, which is why the argument is real at the other scale
and why doubling every dimension multiplies the shell by eight.

**The void arithmetic was also wrong on its first pass, in the same flattering direction.** Dividing a
void fraction by a pressure ratio ignores that the laminate shrinks with the void. Correcting it moved
the compressed value from 1.13 to 1.22 percent and the required ratio from 8.30 to 8.96, so **the
corrected numbers put the target further beyond what an autoclave can reach by squeezing.**

---

## The Atmosphere Is Load-Bearing in Exactly One Place and It Decides a Specification

**A vacuum bag cannot press harder than the air outside it.** Air Force Plant 42 stands at 2,543 feet,
where the standard atmosphere gives 92.35 kilopascals, being **27.27 inches of mercury**. The MTM45-1
datasheet asks for a minimum vacuum of **29.00 inches**. Read as a gauge vacuum that specification is
unattainable on that site by 1.73 inches, not through any deficiency of the pump but because the air
there does not contain that much pressure to remove.

**Elevation alone costs 8.85 percent of the available consolidation pressure.** `gate.ATMOSPHERE` is
named for this computation and for nothing else.

---

## The Store Was Armed Against the Whole Subject, and the Measurement Came First

**With every pattern armed the store refused 2,430 of the 11,325-record main harvest, being 21.5
percent**, across sixty-eight patterns. **A single entry accounted for 1,529 of them, which is 63
percent of every deletion**, being the alternation `epoxy`, `resin`, `laminate` recorded by A335 for a
parachute article. **Here those three words are the subject.**

**Seven new tag families and one entry SPLIT took the refusal to 432, being 3.8 percent, recovering
1,998 records.** The families are `adhesive-bonding`, `composites`, `cost-estimation`,
`cure-monitoring`, `delamination`, `fracture` and `ndt`.

**The split is the new lesson and it runs opposite to A351's.** That article found a contaminant
FAMILY spanning two store entries, so tagging one leaves the other armed. **This one found a single
ENTRY spanning two families.** The A347 rotor-repair entry alternates `field-replaceable`, `rotor
blade`, `blade pocket`, `hot corrosion`, `adhesive bond`, `corrosion protection` and `depot
maintenance`, and exactly one of those names this subject. **Tagging it whole would have opened the
wrong half.**

**Widening has a price and it arrived immediately.** Switching off three families readmitted
thirty-nine records on restorative dentistry, which uses bond strength, cure kinetics, resin composite
and degree of conversion as its own terms of art. `dentistry` went in with the sentence recording it.
**Store 134 patterns, 25 tag families.**

---

## Five Checkers Could Not Fail When First Written

**Every one was caught by counting what it had looked at rather than by reading it.**

- **The gate's self-satisfying-conjunction test parsed zero candidates**, because it required both
  halves to be parenthesised and the gate writes most of them as a bare stem. It passed and **missed a
  deliberately injected defect**. It now examines sixty-seven candidates and catches all three.
- **The store injection harness patched `NOISE_PATTERNS` while `noise_hit` reads a compiled cache**,
  so it injected nothing and **reported a good test as vacuous**. A broken diagnostic condemning good
  data, for the third time in this corpus.
- **The symbol table stripped every macro before scanning**, so a Greek letter was invisible to it. It
  took three further rounds to make it discriminate an undeclared subscript on a declared macro.
- **The assembler's leftover-slot regex could not match a digit**, and nine of eighty-two slots carry
  one, so an unconsumed `@P_PLANT42_KPA@` would have shipped into the article.
- **The probe's separator helper crashed on a character class**, turning `[- ]` into `[-[-\s]+]`.

---

## Two Findings About the Method Itself

**REWORDING BEAT SWEEPING IN FIVE OF SIX THIN SUBJECTS, THE EIGHTH ARTICLE RUNNING.** Out-life went
from 7 records to 150 on vocabulary alone and from 150 to 196 on a supplementary sweep. **The first
version of that table conflated the two moves**, crediting the vocabulary with the sweep's records
inside the very fragment that warns against it, and the three columns are now measured so that each
step changes exactly one thing.

**THE PERIOD STATISTICS NOW STOP AT THE DATELINE AND THE BIBLIOGRAPHY DOES NOT.** 136 records carry a
year later than 30 November 2025. They stay in the reference list under the series convention and are
excluded from every statistic, because **a rate computed over papers not yet written is a claim about
the future wearing the clothes of a measurement**. A351 states a median over a corpus holding
forty-nine such records. A further 266 carry no year and cannot be filtered either way.

---

## Counts

| Quantity | Draft |
|---|---|
| Lines | 10,459 |
| Words | 59,764 |
| Display equations | 8 |
| Reference definitions | 4,970 |
| Research records | 4,874 |
| Report primaries | 308 at 6.3 percent |
| Curated identifiers | 25 |
| Clusters | 11 plus a residual at 4.7 percent |
| Records retrieved | 15,422 across two sweeps |

**Verifier clean at 0 errors and 0 warnings. Tests 106 of 106. Lint 0 defects.** The article's own
verifier runs six checks and every one was proved capable of failing by injection.

**The stub-isolated production build succeeded in 700 seconds with no Liquid error, against the
exact bytes committed**, the checksum having been matched against the stub copy before the build
started and against both stub and draft after it finished. **The rendered audit reports no findings
across 91 pages.** Source and rendered display-equation counts agree at **8**, with **zero raw dollar
pairs leaking**, **zero unresolved reference brackets**, **zero unexpanded slots** and **zero
unrendered Liquid**. The page is 934,230 bytes.

---

## Flagged for the Later Passes, Found After the Draft Was Frozen

**THE SURVEY COVERS THIS ARTICLE'S OWN FRAMING PROGRAMME WITH ZERO RECORDS.** Probing the
5,248-record corpus for `affordability initiative` returns nothing, and the Composites
Affordability Initiative is where the article's central argument comes from. **The article cites it
only through two trade-press columns**, and an AIAA paper carrying the programme's own name exists at
`10.2514/6.2000-1379` and is not in the corpus.

**This is A340's rule arriving one pass early.** A survey that under-covers the subject of its own
conclusion is not comprehensive however good the gate is, and neither the gate tests nor the
two-sided sample can see it, because both examine only what the queries returned. **The
primary-reference pass should fetch that identifier by hand and harvest around it**, rather than
assuming the gate would have admitted it.

**A second gap in the same direction.** Laser bond inspection is the technique the programme
developed for exactly the problem this article says unitisation creates, being that a bondline cannot
be inspected by looking at it, and the corpus holds one record on it.

---

## Open Questions for the Pilot

**A324's `book_jenkins` label remains the one live repair**, unchanged. The key is correct and the
label swallowed the title.

**The OpenLibrary work pages returning Internal Error to a reader** is also unchanged.

**And a new one. A350 ships a duplicated `## The Contemporary Literature` heading**, at lines 412 and
414 of `x_planes_boeing_x53_active_aeroelastic_wing.markdown`. It was found while comparing section
structures for this article. **It is not repaired here**, because A350 is complete on all four passes
and editing a finished article during another article's draft pass mixes two units of work.

**A352 has completed its DRAFT PASS only and is committed, NOT pushed. Nothing is published and
publication of the series has never been authorised.** The next prompt is the equation-density review.
