# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A317 equation-density review, the second of four passes. Committed, **not pushed**, per the
rhythm. **Not published.** All twenty-one articles in the series remain in `_drafts/`.

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

**Committed, not pushed**, which is correct for this pass. **566 lines, 49 display equations, 115
references, 4,996 words.**

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
