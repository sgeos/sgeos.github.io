# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A317 publication review, the fourth and final pass. Committed and **pushed**. **Not
published.** All twenty-one articles in the series remain in `_drafts/`.

---

## The Survey's Organising Claim

**Contemporary coverage from zero to 118 of 353 research citations, or 33.4 percent.**

The X-20 asked three questions at once. Whether a vehicle can return from orbit by flying rather than
falling. Whether it can do so behind a structure that radiates instead of burning away. And whether it
can then be used again.

**Its descendants split those questions up and answered them separately, decades apart.**

The glide went to the Space Shuttle in 1981 and to hypersonic glide weapons after 2010. **The hot
structure was rejected in 1972 and is an active research field again**, under the names metallic and
integrated thermal protection, arguing the X-20's arguments. Reuse went to the Shuttle and turned out to
cost more in inspection than anyone had costed in mass.

**No single vehicle held all three together again until the X-37B**, which flies the X-20's specification
unmanned, forty years late.

---

## The Uncomfortable Finding

The largest contemporary literature touching this article is not about spaceplanes at all. **Hypersonic
glide weapons are the X-20's trajectory with the crew, the wings and the reuse removed.** Same
equilibrium glide, same centrifugal relief, same crossrange for the same reason, same hot leading edges.

The X-20 was cancelled for having no mission. **The mission its trajectory suited best turned out to be
the one nobody was willing to state in 1963**, and the vehicle that flies it now is unmanned and
expendable. The article says so plainly rather than leaving it implied.

---

## A Fourth Homonym Family, Caught in the Last Check

Three were caught during the primary pass. A fourth got through to the end.

**Passive daytime radiative cooling** is a large modern field about emitting to the sky to cool buildings
and wearables. It uses this article's exact vocabulary for the opposite purpose, and seven of sixteen
records in the first hot-structure bucket were building physics.

**And one survived every scan.** A paper titled "Thermal Stress on Cellular Structure and Function" is
cell biology, heat shock on cells. In aerospace a cellular structure is honeycomb core. **It was caught
by the final Crossref registry check, which prints titles**, not by any pattern I wrote. That is now the
second time in this series that the registry check has caught a wrong citation as a side effect of
verifying a link.

The persisted rejection list stands at **35 decisions across four passes**, and nothing on it is cited.

---

## Verification

**77 independent re-derivations, zero disagreements**, still reproducing after every edit. All 81 quoted
values present. 388 references, 368 external URLs, zero duplicates or orphans. 224 plain 200s, 90
publisher 403s, 12 202s, and **43 DOIs verified through the Crossref registry with matching titles**.

A red-flag scan over all cited titles and venues across eleven false-positive families returned zero
hits, and a separate check confirms no read-and-dropped record is cited. Acronym check clean, with a note
that NACA and NASA appear only inside generated citation labels and never in prose, which is the
link-text-counted-as-prose artifact this series has documented before. `_verify.py` at the 0-error
21-warning baseline from the repository root. Zero style violations. Section order matches the genre.
Build passing with 49 of 49 display blocks rendering as display, 2 of 2 tables, Part 21 navigation.
Equation count measured before and after, holding at 49.

---

## Final State

**945 lines, 49 display equations, 388 references, 8,194 words.** Contemporary 118 of 353, or 33.4
percent. Era spread 33 pre-1960, 107 across the 1960s and 1970s, 58 in the 1980s and 1990s, 38 from 2000
to 2018, 118 from 2019 onward.

**References at 388 are just above the 250 to 380 band.** Lines sit 355 below the 1,300 floor and
equations 41 below the 90 floor. **That is the fifth consecutive article to finish outside the named
classes on two of three measures, in the same direction.**

---

## Still Waiting on You

**A315's four marine citations.** Its reverse prompt still describes a David Taylor Model Basin study of
spindle torque on a controllable-pitch **ship** propeller as "directly about the system that failed on
the final flight." Four anchors and one sentence.

**The fourth genre class.** Five consecutive articles now, across twenty passes. I have not amended
`RESEARCH_AIRCRAFT_STRUCTURE.md` because it defines the series' own standards.

A318 is the Northrop X-21. Nothing in the series is published and publishing has never been authorised.

---

## The Cleanest Instance of the Inter-Pass Dependency So Far

**115 references to 271**, of which 236 are research citations and all 236 are primary or period, with
zero contemporary held back for the publication review.

The coverage audit found five thin topics, and **they were exactly the five the equation pass had
promoted.**

**Newtonian impact theory stood at ZERO records.** The article's independent cross-check on its own
keystone had no reference base whatever, for the plain reason that the draft harvest could not know the
cross-check would come to exist. Thermal expansion stood at eleven, emissivity at one, the ballistic
coefficient at six, energy management at four. A targeted search took them to 15, 47, 28, 12 and 17.

**Everything the draft was already about was deep and under-used**, which no search would have fixed.
Radiative cooling held 78 records against 10 cited, refractory coatings 73 against 7, launch 79 against
15. Spreading the selection was the whole of the work there.

---

## A Process Defect I Had Not Seen Before

**Four references I rejected by reading during the draft pass came back in this one.** Each pass rebuilds
its rejection list from scratch, so a record thrown out by judgement in pass one is free to be reselected
in pass three. Among the four was a study of the **thermal protection capacity of aviator's textiles**,
which is clothing.

**The rejection list is now written to a file** so later passes inherit it. Twenty-eight decisions are in
it, across three passes.

---

## A Word Boundary Caused the Miss, Which Is the Opposite of the Usual Lesson

The exclusion rule that should have caught the textiles paper was `\btextile\b`. The title says
TEXTILES. **The trailing word boundary fails against the plural.**

This series has documented substring matching three times, in `fRAMework`, `ARISING` and `controllable`,
and the fix each time was to add word boundaries. **Here the word boundary is what let the wrong record
through.** Both failures are the same underlying mistake, which is trusting a pattern instead of reading
what it returned.

---

## Three Homonym Families, All Caught by Reading

**In spectroscopy an "impact theory" is a model of collisional line broadening** and has nothing to do
with hypersonic flow. The first Newtonian bucket returned one.

**In aviation the "terminal area" is the airspace around an airport**, so a search for terminal energy
management returns air traffic control, including a paper on Orly.

**Thermal expansion is a materials-science subject** in plutonium, phthalocyanines, lithium hydride and
rare earths, none of which this article has any use for. A high-emissivity coating for **television
picture tubes** was also returned.

---

## What the New Material Adds

**The emissivity assumption is now visible as an assumption.** Temperature goes as the inverse fourth
root of emissivity, so 0.6 rather than 0.85 runs the nose about 250 degrees hotter, and the measurement
of emissivity on refractory metals at these temperatures was an active subject rather than a settled one.

**Two references are the X-20's exact problem stated in their abstracts**, being the temperature
distribution and thermal stresses in a hypersonic wing structure, and transient temperature and thermal
stresses in the skin of a hypersonic vehicle, both from the years the configuration was being chosen.

**One topic stays genuinely narrow and is reported rather than padded.** Terminal energy management for
an unpowered orbital vehicle has four usable period references, because the subject did not exist until a
vehicle was actually going to fly it.

---

## Verification

**77 independent re-derivations, zero disagreements**, still reproducing after every edit. All 81 quoted
values present. 271 references, 251 external URLs, zero duplicates or orphans. 158 plain 200s, 44
publisher 403s, 9 202s, and **44 DTIC DOIs verified through the Crossref registry with matching titles**.

A red-flag scan over all cited titles and venues across ten false-positive families returned zero hits,
and a separate check confirms no read-and-dropped record is still cited. `_verify.py` at the 0-error
21-warning baseline from the repository root. Zero style violations. Build passing with 49 of 49 display
blocks rendering as display, Part 21 navigation. Equation count measured before and after, holding at 49.

---

## State

Superseded by the state section above. Era spread is 33
pre-1960, 107 across the 1960s and 1970s, 58 in the 1980s and 1990s, 38 from 2000 to 2018, and zero
contemporary.

**References at 271 are inside the 250 to 380 band.** Lines sit 546 below the 1,300 floor and equations
41 below the 90 floor. The publication review is the remaining pass and contemporary coverage is its work.

**A315's four marine citations are still uncorrected.**

---

## The Article's Own Central Claim Was Undisplayed

**24 display equations to 49, across 17 edits.**

The draft asserts that peak heating on an equilibrium glide is independent of lift-to-drag ratio and that
the peak falls at a particular speed. **It displayed neither the maximisation that locates the peak nor
the speed it gives**, both of which I had computed and verified before writing the draft and neither of
which reached the page.

Writing $u = (V/V_c)^2$ makes the heating proportional to $u\sqrt{1-u}$, and maximising the square gives
$2u - 3u^2 = 0$, so $u = 2/3$ exactly.

**The worst heating always arrives at 81.6 percent of circular speed**, whatever the vehicle, whatever
its wing loading, whatever its lift-to-drag ratio. Only the magnitude changes. That is a much stronger
statement than the draft made and it was sitting one line of algebra away.

---

## A Cross-Check the Draft Never Made

The article assumes a hypersonic lift coefficient of 0.6 and separately derives a required lift-to-drag
ratio of 1.245 by inverting the crossrange requirement. **Those two numbers are connected and the draft
did not connect them.**

Newtonian impact theory gives $C_L = 2\sin^2\alpha\cos\alpha$, so a lift coefficient of 0.6 means an
angle of attack of **38.14 degrees**. At that angle the lift-to-drag ratio is simply the cotangent.

$$L/D = \cot 38.14^\circ = 1.273$$

**Against the 1.245 the mission requires, that is agreement to 2.3 percent**, reached from two directions
that share nothing. One is a crossrange requirement inverted through orbital mechanics. The other is
impact theory applied to a flat plate. Neither knows about the other.

---

## The Structure Section Had No Relation and Its Claim Was Quantitative

The draft said a hot panel is "a good deal longer" than its frame without saying how much. Writing
$\Delta L = \alpha L \Delta T$ out gives numbers that change how the section reads.

**The airframe grows 5.09 inches over its own length** at a 1,500 degree rise. Worse, molybdenum shingles
expand at about three eighths the rate of the René 41 beneath them, so a three-foot panel and its frame
differ by 0.27 inches. **The problem is accommodation rather than strength**, and that is now stated with
a number behind it.

I also added the eighth-root dependence, $T \propto (W/S)^{1/8}$, which is why the wing-loading
temperature table is so flat and which the draft left as an unexplained observation.

---

## Verification

**77 independent re-derivations, zero disagreements**, up from 57. All 81 quoted values present. Two
approximations I had stated loosely were tightened after checking, a kerosene-equivalent figure from
1,200 to 1,133 gallons and an energy height from 1,363 to 1,365 statute miles.

`_verify.py` at the 0-error 21-warning baseline, confirmed from the repository root. Zero style
violations. Isolated build passing with 49 of 49 display blocks rendering as display, 2 of 2 tables, Part
21 navigation. Equation count measured before and after.

**No error was found in the drafted text this time**, which breaks a run of twelve consecutive articles
in which writing the relations down caught a wrong claim. What it caught here was omission rather than
error.

---

## State

Superseded by the state section above.

Seven sections remain flagged by the density scan and I judge all seven correct as they stand, being the
opening, the historical framing, and the closing analytical sections, which quote numbers derived
elsewhere in the article.

Equations at 49 sit 41 below the 90 floor and lines 735 below the 1,300 floor, with two passes remaining.

**A315's four marine citations are still uncorrected** and still outside what you have asked for.

---

## The Keystone Turned Out Cleaner Than Expected

The X-20 asked what lift costs on the way back from orbit. Substituting the equilibrium-glide density
into the heating relation gives

  peak heat rate proportional to the square root of WING LOADING, with **no lift-to-drag ratio in it at
  all**

  total heat load proportional to LIFT-TO-DRAG RATIO

  crossrange proportional to the SQUARE of lift-to-drag ratio

**Across a twelvefold change in lift-to-drag ratio the peak rate does not move in the fourth decimal
place.** I checked that numerically over an eighty-fold range and then confirmed it analytically, since
the peak sits at a speed ratio of exactly two thirds and the expression contains no lift term.

That is an unusually clean decomposition. **Peak temperature, which selects the material, is set by wing
loading alone. Mission reach, which selects the programme, is set by lift-to-drag ratio alone.** The two
decisions do not interfere.

The quoted 1,700 nautical miles of crossrange needs a lift-to-drag ratio of **1.245**, which is exactly
what a flat-bottomed delta of 1957 achieved, so the programme's headline claim is consistent with its own
configuration rather than optimistic about it.

---

## I Was Wrong About Why the Structure Was Hot, and Say So

The file was written expecting to show that a thirty-minute heat load makes ablation impossibly heavy and
therefore forces a radiative structure. **The arithmetic says otherwise and the earlier reading is
withdrawn in the text.**

An ablator sized for the whole vehicle load comes out between **556 and 2,778 pounds**, or five to
twenty-four percent of glider weight, across every plausible effective heat of ablation. Heavy, and
entirely buildable. A heat sink is genuinely impossible at 333 percent.

**So the hot structure was chosen for REUSE, not compelled by mass**, which makes the X-20's most
distinctive engineering decision a consequence of wanting an aeroplane rather than a consequence of the
heat.

---

## The Comparison With a Capsule Is Not the One Usually Drawn

I integrated a proper Allen-Eggers ballistic entry rather than degenerating the glide model, after the
first attempt evaluated the glide at a lift-to-drag ratio of 0.0001 and produced a heat-load ratio of
twelve thousand five hundred, which was absurd on its face.

Done properly, a ballistic entry imposes a peak rate **26.1 times higher** and a total load **essentially
the same**, at 0.95. The glider's whole advantage is in rate, and that is precisely what permits a
structure that radiates rather than one that burns away.

---

## Two Tooling Defects, Both From the Working Directory

**A leftover selector from A316 shadowed a Python standard library module.** It was named `select.py`,
sat in the working directory, was imported in place of the standard `select`, executed on import, and
**overwrote this article's reference selection with output computed for a tilt-propeller aircraft.** I
caught it because the replacement contained propeller buckets for a spaceplane. Nothing in the checking
apparatus would have found it.

**The corpus verifier then reported zero errors and zero warnings**, where the baseline is zero and
twenty-one. It had inherited a scratch working directory and checked nothing. **It was caught only
because the expected number was known**, which is the argument for recording baselines rather than
reading checks as pass or fail. This is the relative-path defect for the sixth time.

---

## The A316 Checker Fix Paid Off Immediately

`check.py` gained a test after A316 that the three required series sections are all present. **It failed
this draft on the first run**, for the missing Contemporary Literature section, so the defect that
survived three passes in A316 was caught in minutes here. A brief survey section is now in the draft and
the publication review will expand it.

---

## Verification

**57 independent re-derivations, zero disagreements**, from a verifier that uses an exponential
atmosphere where the model uses tabulated layers, Simpson where the model uses trapezoid, and closed-form
maximisation where the model searches numerically. All 60 quoted values confirmed present.

115 references, 95 external URLs, zero duplicates or orphans, 70 plain 200s, 5 publisher 403s, and **7
DTIC DOIs verified through the Crossref registry with matching titles**. Red-flag scan over all 80 cited
titles and venues across seven families returned zero hits. `_verify.py` at the 0-error 21-warning
baseline, confirmed from the repository root. Zero style violations. Isolated build passing with 24 of 24
display blocks rendering as display, 2 of 2 tables, Part 21 navigation.

---

## State

Superseded by the state section above.

Twenty-one of seventy-two. The publication-order dependency is now **twenty-one deep** and every
cross-reference points backward.

**A source conflict was resolved rather than repeated.** A gross mass of 22,321 pounds appears widely and
is inconsistent with a wing loading of 33 on 345 square feet. The glider weight of 11,386 pounds
reproduces the quoted loading exactly, so the larger figure is the launch stack including the transtage.

**A315's four marine citations are still uncorrected** and still outside what you have asked for. Four
anchors and one sentence whenever you want it.

The three remaining passes on A317 are yours to prompt.
