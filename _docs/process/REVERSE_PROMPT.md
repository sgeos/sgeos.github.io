# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A322 equation-density review, the second of four passes. Committed. **Not pushed.** **Not
published.** All twenty-six articles in the series remain in `_drafts/`.

**19 display equations to 43**, across thirteen edits each asserted to match its anchor exactly once,
taking the article from 4,094 to 4,367 lines and 13,732 to 15,890 words.

---

## The Two Largest Omissions Were Explanatory Rather Than Missing Lines

**THE ARTICLE NEVER SAID WHY A ROTOR AUTOROTATES.** It asserted that the rotor turns because air comes
up through it and moved on. The blade element meets the flow at an inflow angle, its lift and drag both
have components in the plane of rotation, and the element neither drives nor retards the rotor when

    tan(phi) = C_d / C_l

**The equilibrium element is the one whose inflow angle equals its own drag-to-lift angle.** Inboard of
it the element drives, outboard it is driven, and autorotation is that balance integrated over the
disc. That is the entire physical content of the subject and it was absent.

**THE ARTICLE SAID MOMENTUM THEORY IS NOT VALID AT THE AUTOROTATION POINT AND DID NOT SHOW IT.** Written
out, the windmill-brake thrust is $T = 2\rho A V_d^2 a(1-a)$, and setting it equal to the weight gives

    (v_h / V_d)^2 = a(1 - a)

whose right side is a parabola with maximum one quarter. **So momentum theory admits no solution below
$V_d = 2 v_h$, and the measured value is 1.8.** The quadratic in the induction factor has a negative
discriminant there.

**This is stated precisely and not dressed up as the rotor beating a bound**, because the bound exists
only inside a model that does not apply at that condition. It is why the constant is empirical, which
the article had asserted without justifying. **One consequence lands on a table the article already
prints**: the limiting case is a drag coefficient of exactly 1 on disc area, so the last row of that
table is the momentum-theory bound.

---

## A Correction the Pass Produced

**Every descent rate was computed at sea level and every ejection happens at altitude.**

Descent goes as one over the square root of density, so a rotor at 20,000 feet arrives 37 percent
faster than the same rotor at sea level.

**The range survives untouched and that is worth knowing**, because it is the article's headline
number. Range is $h(L/D)$, which contains no speed and no density at all, so an ejection at twenty
thousand feet still reaches fifteen miles.

**The time aloft does not survive.** Integrating with density varying gives 9.4 minutes from ten
thousand feet rather than 10.1, and 17.4 from twenty thousand rather than 20.2. **The constant-density
figure overstates by 8 percent and 16 percent respectively, and the table has been corrected.**

---

## The Strongest New Result, and It Closes a Gap the Draft Admitted

**The draft asserted that the SAVER would have to retrieve its whole descent in the flare out of stored
rotor energy, and never checked whether it could.**

Substituting the inertia and the operating speed into the stored energy gives a small surprise:

    E = (1/2) I Omega^2 = (N/6) m_b V_tip^2

**The radius has cancelled.** At fixed blade mass and tip speed a rotor stores the same energy whatever
its size, because inertia rises as the square of the radius exactly as fast as angular speed falls.
**Shrinking a rotor costs nothing in stored energy.** The energy required, however, goes as

    E_req proportional to W^2 / R^2

| | X-25B | SAVER |
|---|---|---|
| Energy required, ft lb | 4,130 | 34,700 |
| Energy available, ft lb | 19,900 | 19,900 |
| **Margin** | **4.8** | **0.57** |

**The X-25B carries nearly five times the energy its flare needs. The SAVER carries about half.**
Inverted, the SAVER would have needed **21 pound blades against the 12 assumed**, on a vehicle whose
entire design constraint was folding into an ejection seat. **Doubling the assumed blade mass still
leaves it at 1.15, which is no margin at all for an escape system.**

It rests on an assumed blade mass and tip speed for a vehicle whose real figures are unpublished, so
the article offers it as an order-of-magnitude statement rather than a measurement.

---

## Two Symbol Collisions, Both Found by Reading the Rendered Equations

**Neither would have been caught by any check, and both are between two standard notations.**

- **`sigma` was doing rotor solidity and atmospheric density ratio.** Solidity was kept, since the
  article uses the blade loading coefficient, and the density ratio is now written out longhand.
- **`gamma` was doing glide angle and Lock number.** The glide angle was kept, since it appears first
  and more often, and the Lock number is subscripted with a sentence saying why.

**A collision between two standard notations is resolved by marking one, not by silently reusing it**,
and the article now says so in both places.

Also found by reading: **the range relation was displayed twice**, and **the terminal-velocity force
balance was displayed twice**. Both second occurrences were removed.

---

## Prose the Pass Introduced and Then Removed

**Five sentences referred to what an earlier draft of the article had said.** That is drafting history
leaking into the published text, and the reader never saw that draft. The epistemic content was kept
and the references to a prior revision were removed.

---

## The Promoted-Subjects Rule Fired, and Once in an Unexpected Direction

**Exactly one cluster in the article was uncited, and it was the one this pass made central.** Stored
rotor energy now carries the SAVER flare-margin argument and had no citation at all.

**Investigating it produced a better finding than simply fixing it.**

- **The cluster pattern contained a homonym the search created for itself.** It included `flywheel`,
  meaning the flywheel effect of a turning rotor, and retrieved **flywheel energy storage for
  spacecraft and power grids**, meaning containment rings and composite burst testing. Six of its seven
  records were that. Removed.
- **What remained was one record, and the article does not call that an archive limit**, because it is
  not one. The relevant work exists and is cited, but it sits inside the autorotation and blade-motion
  literature rather than beside it, since a paper on autorotative landing is a paper about spending
  exactly that energy. **A thin heading is not the same thing as a thin subject.**

**Rotor spin-up and prerotation is genuinely thin at three records** after a harvest aimed at it, and
that one is reported as an archive limit and as the reason the spin-up section reasons from energy
rather than from measurement.

---

## Verification

**Numerical.** Extended from 40 to **71 independent checks**, none importing the calculation. New routes
include bisecting on the in-plane force to recover the equilibrium inflow angle rather than inverting a
tangent, scanning the descent ratio to confirm the momentum-theory root appears **exactly** at 2 and
nowhere below, trapezoid rather than midpoint integration of the time aloft, and a property test that
stored energy is radius-independent across six radii. **All pass, and every value was required to
appear in the draft text.**

**Build.** Twenty-six article isolated build succeeding, all 43 equations rendering as display math,
zero mangled escapes, zero unbalanced braces, zero duplicated equations, Part 26 of 72.

**Corpus.** `_verify.py` at 0 errors and 21 warnings. Style and integrity check clean at zero failures
and zero warnings across all twenty-six articles.

**URLs.** The seven records the newly cited cluster introduced were swept individually. All resolve, one
DOI registered and six NTRS identifiers at 200, and **reading them is what exposed the flywheel
homonym**.

---

## State

**A322 has two of four passes complete. Committed, not pushed, not published.**

**Expected next is the primary-reference review.** The coverage audit already names where it will land.
Five equation-promoted subjects are thin, and **two are at or near zero with the article now leaning on
them**, being stored rotor energy and profile drag at the blade section, with bluff-body drag coefficient
at 20 cited of 41 and only 6 primary.

**Still open and unchanged.** The fourth genre class, now **thirteen** consecutive articles. The A305
length offer.
