# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A313 drafted, the Bell X-16. The first of four passes. Committed, **not pushed**, not
published. All seventeen articles in the series remain in `_drafts/`.

---

## The Archive Holds Nothing About This Aeroplane

This is worth stating first because it decided how the article was built. NASA's technical reports
server returns **zero records for MX-2147**, zero for the aircraft as an aeroplane, zero for the Bell
model number, and ten false positives for the aircraft name, consisting of Bell Laboratories radio
surveys and a galaxy catalogued as MCG-05-23-16. The Defense Technical Information Center holds the
reconnaissance requirement and several sibling weapon-system studies and nothing on this aircraft.

**This is not the retrieval defect A311 and A312 both met**, where a report existed but no phrasing of
its own title would surface it. There is nothing to surface. Every dimension, weight, and performance
figure in the article comes from a secondary compilation, and the compilations disagree with one
another.

**The A310 rule carried the article.** A vehicle with almost no record of its own can still be dense
provided the question it asked was one other people were also asking. The X-16's question is subsonic
cruise at extreme altitude, which is the U-2's question, the RB-57D's question, and the question the
modern high-altitude long-endurance field is asking now. The harvest returned 947 records and the
master table holds 871 entries, none of them about the X-16.

---

## The Keystone Was Chosen Against the Famous Answer, and Computed

The popular limit on a seventy-thousand-foot aeroplane is the coffin corner. **It is not what bound
the X-16, and the article computes both rather than assuming the famous one.**

Minimum drag is weight over the maximum lift to drag ratio and **contains no density at all**, so it
does not vary with altitude. Turbojet thrust does. The ceiling is where they meet, which makes it

**a function of instantaneous weight rather than a property of the aeroplane.**

Thrust binds at every weight, by about fourteen thousand feet. The two limits sit at density ratios
both proportional to weight, so they move together and no amount of fuel burn brings the aeroplane
near the corner.

---

## The Method Failed Its Own Validation, and That Is the Best Result in the Article

At a linear thrust lapse the quoted service ceiling of 71,832 feet requires a weight of 22,325 pounds.
**The empty weight is 23,280.** The relation demands an aeroplane 955 pounds lighter than one with
nothing in it.

The same failure lands on the U-2A and the RB-57D in the same direction, which makes it one shared
wrong assumption rather than three data errors. The sensitivity study named the culprit. The ceiling
moves **7,786 feet** across a plausible zero-lift drag range and **32,142 feet** across a plausible
lapse-exponent range, a factor of **4.13**.

Solving for the exponent instead of assuming it:

| Aircraft | Required exponent |
|---|---|
| Bell X-16 | 0.9686 |
| Lockheed U-2A | 0.9780 |
| Martin RB-57D | 0.8669 |

**The two whose wing areas are actually published agree to within one percent.** Three aeroplanes
designed separately by three companies against one requirement are consistent with one statement about
how a turbojet behaves in thin air. That is a statement about compressors rather than wings, and it
corroborates the historical claim that the programme's lasting contribution was the high-altitude J57
that then powered the aeroplane that beat it.

At the solved exponent the X-16 first reaches its design altitude at **29,839 pounds**, after burning
**48.9 percent of its disposable load**, so the design altitude is an end-of-mission condition and the
mission is a cruise climb.

---

## Two Conclusions Inverted During the Pass

**The Breguet check.** First solved one way, it implied a specific fuel consumption of 1.157 pounds per
pound force per hour against a period band of 0.8 to 0.9, which reads as the quoted range being
optimistic. Solved the other way, the quoted range is **73.5 percent of ideal Breguet**, which is an
ordinary allowance for climb, descent, and reserves. **The reading was wrong, the range figure passes,
and the article says so in the text rather than silently correcting.**

**The widening margin.** The draft first explained the thrust-to-corner margin widening by stalling
speed going as the square root of wing loading against a linear thrust ceiling. **That was wrong.**
Both limits sit at density ratios proportional to weight and move together. The 279 feet of widening
is a scale-height effect, because the corner sits fourteen thousand feet higher where the temperature
is rising above the tropopause.

---

## A Defect My Own Tooling Introduced

A delimiter-normalisation regex whose trailing `\s*$` consumed the blank line after every display
equation collapsed **all twenty** into their following paragraphs. Kramdown then rendered them as
**inline** math rather than display math, which is silently wrong rather than visibly broken.

Every automated check passed it. **Only the isolated build caught it**, by counting rendered display
delimiters against source blocks. `check.py` now requires a blank line on both sides of every display
equation.

---

## Verification

**83 independent re-derivations, zero disagreements.** Deliberately not importing the calculation
module. The atmosphere is reimplemented by trapezoidal integration of the hydrostatic equation rather
than the analytic layer solution, and the ceiling by scanning altitude rather than inverting the
relation, so a mistake in one cannot validate itself.

**69 external URLs.** 44 plain 200s, 13 publisher 403s from bot detection, and **12 DTIC DOIs verified
through the Crossref registry** with titles matching the prose, after the `.mil` landing pages refused
automated connections. Asking the registry whether an identifier is registered and what title it
carries is **a stronger check than an HTTP 200**, because it confirms the identifier points at the
document the prose names rather than merely that a server answered.

`_verify.py` at the 0-error 21-warning corpus baseline, run from the repository root. **The
relative-path defect recurred twice this session**, once invoking a generator by bare name from the
repository root and once running `_verify.py` with an inherited scratch working directory, where it
reported a misleading 0 warnings. Isolated build passing with 20 of 20 display blocks rendered, 8 of 8
tables, and Part 17 navigation.

---

## Draft State and an Open Question for You

**534 lines, 20 display equations, 85 references, 7,450 body words.**

That sits **above the documentation-poor band** of 150 to 400 lines, 0 to 15 equations, and 20 to 60
references on all three measures, and **well below the full-aircraft band** of 1,300 to 1,600 lines, 90
to 130 equations, and 250 to 380 references on all three.

**`RESEARCH_AIRCRAFT_STRUCTURE.md` does not name an intermediate class.** The draft was neither padded
upward nor trimmed downward, and the figures are reported as they fell out of the material. The
equation and reference passes will raise the last two substantially, as they have on every previous
article. Whether the genre document should gain a fourth class is a decision for you and I have not
made it.

---

## State

**Committed, not pushed.** The draft pass does not push, per the series rhythm. Nothing in the series
is published, and the deploy workflow builds without `--drafts`.

**The publication-order dependency is seventeen deep**, A313 back to A297, and every cross-reference in
this article points backward.

Seventeen articles of seventy-two. **Categories remain undecided** at `aerospace history engineering`,
seventeen articles deep and raised twenty-one times.
