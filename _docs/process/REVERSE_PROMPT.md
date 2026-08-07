# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-07
**Task**: A309 draft pass, the first of four. Committed and **not pushed**, per the rhythm. **Not
published.** All thirteen articles in the series remain in `_drafts/`.

---

## The Keystone, and Why It Is Not a Repeat of A308

The handoff warned that the trap for this article was repetition, because the X-12 is the same
airframe as the X-11 and A308 spent its length on the structure. The structural material is
referenced and deliberately not re-derived.

**The keystone is terminal velocity control.** A ballistic missile falls for 34.3 minutes and cannot
be steered during any of them, so everything the weapon will ever do is decided at cutoff. Range
responds to burnout speed with a dimensionless sensitivity of 4.34, which is 6.04 kilometres per
metre per second, so a two nautical mile circular error probable allows **0.613 metres per second out
of 7193, or one part in eleven thousand seven hundred.**

A308 derived that same sensitivity and spent one sentence on it. Building an article on it turns out
to explain every distinctive feature of the Atlas B, which is the test of whether a keystone was
correctly identified.

---

## The Result the Article Is Built Around

**Grazing circular speed is 7904 metres per second against 7193 for a ten-thousand-kilometre
ballistic arc.** The deficit is 711 metres per second, or 9.9 percent. Closing it costs a mass ratio
of 1.2645, which is 20.9 percent of the burnout mass, or 1129 kilogrammes.

**The predicted orbital allowance of 4266 kilogrammes reproduces the reported Project SCORE on-orbit
mass of 3980 to within 7.2 percent.** That calculation uses nothing but the range law, a published
specific impulse, and a burnout mass taken from a different Atlas variant. The weapon mission and the
satellite mission are the same mission with the payload changed, and the X-12 demonstrated both
within twenty days in December 1958.

The apogee sensitivity of the orbital case is 4.24 kilometres per metre per second against 6.04 for
ballistic range, so **the two problems have the same sensitivity to within a factor of one and a
half.** The guidance built to hit a target is neither more nor less than what places a satellite.

---

## Findings the Sources Do Not State

**The minimum-energy trajectory is stationary in flight path angle.** A maximum has a vanishing first
derivative, so angle errors enter the range at second order while speed errors enter at first. A
tenth of a degree costs 77 metres, which is the miss a speed error of 0.0128 metres per second would
produce. **Pointing is roughly fifty times more forgiving than speed at the tolerances that matter,
and the ratio grows without limit as the errors shrink.** This is why the vehicle is a
speed-measuring instrument with an attitude system attached rather than the reverse.

**The verniers are a velocity-trim device before they are a roll-control device.** Sustainer tail-off
impulse uncertainty is 1.07 metres per second, which is 1.8 times the entire error budget, so a
vehicle that simply commands its sustainer to stop cannot meet the requirement however good its
guidance. The verniers cut the required timing precision by a factor of 43.4.

**Radio guidance was the right architecture, not merely the available one.** An inertial platform
produces speed by integration, so an accelerometer bias of only 220 micro-g exhausts the whole budget
over a 280 second powered flight. Ground-based Doppler measures speed directly and removes the
integration.

**Halving the circular error probable is worth a factor of eight in yield**, because lethal radius
scales as the cube root of yield. Chaining through the range sensitivity, a cutoff error of one metre
per second instead of 0.613 must be paid for with a weapon 4.34 times larger. That is the economic
argument for the entire guidance programme.

**The flattening of the Earth is 21.4 kilometres, which is 5.8 times the entire miss budget.** An
intercontinental weapon cannot be aimed on a sphere, so the ballistic missile created a geodetic
requirement it could not itself satisfy, and the resolution came from the orbital capability this
same vehicle demonstrated.

**The autopilot bandwidth must live in a window of 31**, between a 1.14 second aerodynamic divergence
and a 4.32 hertz first bending mode. Because the shell is pressure-stabilised, that bending mode
moves during the ascent. A308 raised the same physics for pogo. This is the one place the two
articles touch and it adds rather than repeats.

**The Atlas B is not measurably more reliable than the Atlas A.** Six of ten against four of eight
gives a pooled z of 0.42. Three of the four failures are in the booster phase and none is in a system
the B introduced.

---

## The Article Argues Against Its Own Keystone

This is the section worth reading. Accuracy decided whether the weapon worked and **did not decide
whether it was kept.** A cryogenic missile needing roughly fifteen minutes to load consumes 44
percent of the adversary's 34.3 minute flight time, which is not a second-strike posture, and
Minuteman loads nothing. The Atlas was retired from the weapon role by 1965.

---

## A Method Improvement, Which Is a Correction to A308's Toolchain

**Manual reference-display corrections are now keyed by URL rather than by anchor.** A308 keyed them
by anchor. The five Difficulties Review volumes share author, year, and leading title, so their
disambiguation suffixes are assigned in generator iteration order, and regenerating the master table
for A309 permuted them. **Every one of the five manual displays landed on a different volume than it
named.** A URL is the only stable identity a harvest record has. Each volume is now named by the
subsystem it covers, namely propellant utilisation, the propulsion interface, pneumatics, the
autopilot, and the electrical system.

A relative path in a shell command also failed silently by running in the wrong directory, which is
the A307 defect recurring in a new place. It was caught because the command errored rather than
succeeding against the wrong file.

---

## Verification

All 130 worked values re-derived independently with **zero corrections to the article**. Two checker
disagreements were both the checker, once on a zero-target tolerance and once on a missing
SI-to-cgs conversion in the Sutton and Graves correlation. The second exposed genuine sloppiness in
the article's unit labelling, which was repaired. **That is the fourth time in this series the
verification rather than the article has been the thing that was wrong.**

22 of 22 fixed identifiers at 200, 127 of 127 DOIs Crossref-resolved on title at the 0.85 threshold
with zero flagged, zero duplicate URLs, and no hand-entered identifier anywhere. `_verify.py` at the
0-error 21-warning corpus baseline. Zero contractions, em-dashes, en-dashes, prose colons, prose
semicolons, prose parentheticals, doubled words, duplicate headings, lone dollar-delimited lines, or
adjacent display-math seams. Isolated build succeeding with 115 rendered display blocks matching the
source count exactly, Part 13 navigation, nine tables, no unresolved reference links and no surviving
Liquid tags. All eleven edit seams read by eye.

---

## Draft State

**1066 lines, 115 display equations, 165 reference definitions, 13,142 words.**

**Equations are already inside band at 115 against 90 to 130, which no draft in this series has
achieved before.** Lines sit 234 below the 1300 floor and references 85 below the 250 floor, both
reported rather than padded. The shortfall is deliberately smaller than A308's, which entered its
review passes at 678 lines.

A citation-coverage audit by section during the pass found eleven sections carrying equations and no
citations at all, including the booster staging section with nine displayed relations and none. That
debt was repaired inside the draft pass rather than deferred.

The citation construction mix was rotated twice. The first rotation moved the leading construction
off 31.3 percent and concentrated a replacement instead, which the second rotation dispersed. Top
bigram now 5.6 percent. `atlas` at 6.91 per thousand body words is the subject noun and is reported
rather than remediated.

---

## What the Review Passes Have to Close

**Contemporary references sit at 23, or 15.5 percent of dated.** That is well below the 28 to 33
percent floor and far below the 101 to 189 absolute count the series has held since A301, so the
publication-review sweep carries the largest single gap.

Primary sources are already 83.1 percent of dated, so the primary pass has less to do than usual and
should be aimed at the sections the coverage audit still shows thin.

Equation density being in band means the equation pass should look for relations the prose relies on
without displaying, rather than for count.

---

## State

**Committed, not pushed**, per the four-pass rhythm. Thirteen articles drafted of seventy-two, none
published. **The publication-order dependency is thirteen deep**, A309 back to A297.

**Categories remain undecided** at `aerospace history engineering`, thirteen articles deep and now
raised seventeen times.
