# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A322 draft pass, the first of four. Committed. **Not pushed**, per the rhythm. **Not
published.** All twenty-six articles in the series remain in `_drafts/`.

**Draft state 4,284 lines, 19 display equations, 2,472 references, 14,221 words.**

---

## The Keystone, and Why the Obvious Reading Is Wrong

**An autorotating rotor is not a gentler way down than a parachute. It is a worse one.**

The Discretionary Descent Vehicle is usually described as giving a descending crewman a softer landing.
The arithmetic refuses that before any archive is consulted. Descent rate goes as the square root of
disc loading for a rotor and a canopy alike, and the Bensen rotor sweeps 314 square feet where a
28 foot canopy sweeps 616. **At equal weight the rotor descends nine percent faster, and as flown it
descends twenty-nine percent faster.**

**What autorotation buys is translation.** In forward flight the rotor is a wing rather than a brake,
glides at about four to one, and reaches seven and a half miles from ten thousand feet, where a round
canopy reaches nothing. **The programme was named discretionary descent and not slow descent, and the
name is the more accurate description of what the physics delivers.**

---

## A Bridge Between Two Literatures That Do Not Cite Each Other

**The autorotation constant every rotorcraft text quotes and the drag coefficient every parachute text
quotes are the same number.** Substituting the definition of hover induced velocity into the drag law
cancels the weight, the density and the area, leaving

    C_D = 4 / (V_d / v_h)^2

so the measured ratio of 1.8 is exactly a disc-referred drag coefficient of 1.23. A flat circular
canopy referred to its projected area sits at 1.67. **Both devices are swept-area drag devices near the
same coefficient, and neither field says so.** The relation contains no fitted quantity, and the
verification file confirms that by re-deriving it over two thousand randomised weights, densities and
radii and requiring the answer to be identical every time.

---

## A Result That Came Out Negative, and Is Reported That Way

**The first objection anybody raises against this concept does not survive being written down.** A
canopy inflates in seconds while a rotor must be spun up, and the energy has to come out of height.
Written down, the stored rotor energy is about 19,900 foot pounds, which is **fifty-seven feet** of
ideal height loss and a few hundred at any believable efficiency. That is comparable to canopy
inflation. **The energetic argument fails, and the article says so rather than quietly dropping it.**

The real constraints are elsewhere and neither is aerodynamic. **The deployment sequence contains an
irreversible step**, since the crewman must cut away a working parachute to gain range rather than
safety. And the record says the aircraft were flown to evaluate piloting technique and training
requirements, which is a programme discovering that its hard problem is the operator.

---

## A Prediction Against a Case the Model Was Not Fitted To

The X-25 published no measurement to check against. **The Kaman SAVER does.** Its rotor had to fold
into an ejection seat, so it was 14 feet rather than 20, at 710 pounds rather than 350. Since descent
rate goes as the square root of weight over radius, that is punished twice, and the model puts its
vertical autorotation at **56 feet per second, or 38 miles an hour straight down**, which is not
survivable in steady descent. **The model therefore predicts that a stowable rotor seat needs an
engine, and the SAVER had one.**

**The prediction is deliberately not overclaimed.** The record says the Williams turbofan was fitted
because it was available off the shelf and was more powerful than needed, and a thrust to weight ratio
of 0.61 is far above what a gyroplane needs. The article states the prediction as directionally right
and quantitatively unconfirmed.

---

## The Keystone-Vocabulary Rule, Applied Before Writing for the First Time

The handoff calls this the most reliable rule in the series, and it had fired on the previous three
articles as a repair after drafting. **This time the pool was audited against the article's topic list
before a word existed.** The keystone came back healthy at fifty records because the first harvest
already used the era's words for it. **Six other topics did not, and four were at zero**, including
rotor stored energy and prerotation, both of which the article's own equations need. Two further
harvests aimed at those recovered them using period vocabulary such as autorotative index and rotor
speed decay.

---

## Two Inherited Filters Had to Be Removed

**A filter earned in one article is not automatically valid in the next.** The accumulated homonym
patterns were written for entry vehicles and two of them would have silently destroyed legitimate
records here.

- **Wind turbines** were in the ground-vehicle filter. **Autorotation is the windmill brake state**, so
  a turbine rotor and a descending rotor are the same flow state in different reference frames.
  Filtering it would have deleted the closest living relative of this article's keystone.
- **Seed dispersal** was in the biology filter. **The samara is an autorotating wing** and the
  rotary-decelerator literature cites it directly.

---

## Five New Homonym Families, Four Found by Reading the Selection

**Anticipated**, and the first is the worst collision the series has met. **Descent** is gradient
descent. **Canopy** is the forest canopy. **Parachute** is the golden parachute. **Rotor** is the
electrical machine rotor and the mountain-wave rotor. **Flare**, already known as the solar flare, is
here also the **illumination flare**, a parachute-suspended munition sitting inside this article's own
search space.

**Found only by reading what was selected**, which is the rule that keeps earning its place.
**Turbomachinery was the largest at forty-four cited records**, because in an axial compressor the word
rotor means a rotating blade row and it shares blade, tip speed, solidity and stall with everything
here. Also **planetary landing**, **patents**, **forensic bloodstain analysis** reached through flight
characteristics, and **animal flight biomechanics** reached through wing disc loading. All are now zero.

**The animal filter had to be written carefully.** A bare pattern would have deleted the Black Hawk
helicopter, the Hawker Siddeley Hawk, bird-strike testing and the artificial bee colony algorithm. It
uses taxa and biological constructions only, and all six legitimate records survive.

---

## Three Defects Found by Reading Rather Than by Checking

**Every automated check passed while all three were present.**

- **Doubled backslashes in LaTeX.** In an rf-string `\\,` stays two backslashes, which MathJax reads as
  a line break followed by a comma rather than a thin space. Twenty-one such macros. The equation
  count, the brace balance and the build were all correct.
- **Link text truncated mid-word**, giving citations reading "Empirical Relation Between Induce". Link
  text is prose and no check looks for a word cut in half.
- **The same paper cited twice in a row** with character-identical display text, from records indexed
  under two identifiers. Ninety-five such duplicates removed.

Also fixed, **Crossref returns HTML inside titles** and it reached the link text complete with italic
tags, and unbalanced curly quotes survived truncation.

---

## Verification

**Numerical.** 40 independent checks, none importing the calculation. Induced velocity recovered by
bisection rather than the closed form, rotor inertia by numerical integration rather than the rod
formula, stored energy from angular momentum, and the bridge tested as a property over randomised
inputs. **All pass, and every value was required to appear in the draft text.**

**The unsettled rotor diameter was tested rather than asserted.** Twenty feet against twenty feet six
inches moves the descent rate by **2.44 percent**, which supports the article's claim of under five.

**Build.** Twenty-six article isolated build succeeding, all 19 equations rendering as display math,
zero mangled escapes, zero unbalanced braces, series navigation reporting Part 26 of 72.

**Corpus.** `_verify.py` at 0 errors and 21 warnings, the expected baseline. Style and integrity check
clean at zero failures and zero warnings.

**URL sweep** was still running at the time of writing and its result is recorded in the task log.

---

## The Source Base Is the Thinnest in the Series

**A pool of 3,526 harvested records contains exactly one matching the X-25, Bensen, the Discretionary
Descent Vehicle or the stowable rotor seat**, and that one is Hollrock and Barzda on the SAVER rather
than on the X-25. There is no flight test report, no aerodynamic data report and no programme summary
in the open literature reached here. **The specifications come from museum fact sheets, and where they
disagree the article names the disagreement rather than choosing.** Rotor diameter is given as both
20 feet and 20 feet 6 inches, and the engine as both 72 and 90 horsepower.

**The supporting physics is abundant and that asymmetry is the article's actual subject.** Everything
about the concept can be derived and almost nothing about the aircraft can be verified.

---

## State

**A322 draft pass complete. Committed, not pushed, not published.**

Twenty-six of seventy-two. The publication-order dependency is now twenty-six deep.

**Expected next is the equation-density review.** Ten subjects are already listed in the coverage audit
as what an equation pass would promote, written before the pass rather than after it.

**Still open and unchanged.** The fourth genre class, now **thirteen** consecutive articles outside all
named classes. The A305 length offer.
