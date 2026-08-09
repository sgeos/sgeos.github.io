# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A321 publication review, the fourth and final pass. Committed and **pushed**. **Not
published.** All twenty-five articles in the series remain in `_drafts/`.

**Final state 3,684 lines, 53 display equations, 3,144 references, 19,766 words.**

**Contemporary coverage from 611 to 1,536 of 3,115 research citations, or 49.3 percent**, across ten
subsections where the draft had five.

---

## The Survey's Organising Claim

**Everything the X-24B demonstrated is now done by software, and the corridor did not widen, because it
is set by energy rather than by skill.**

Written out, the touchdown speed is a function of load factor, wing loading, drag polar and density, **in
which there is no term describing the pilot**. An autonomous vehicle arriving too fast still floats, and
one arriving too slow still runs out of speed. Automation buys consistency in hitting the middle of a
corridor whose width is fixed by aerodynamics.

**The milestone came thirteen years after the X-24B.** On 15 November 1988 Buran flew one uncrewed
orbital mission and landed itself on the runway at Baikonur, unpowered, in a crosswind. **That is the
same demonstration Manke and Love flew, performed by a machine, at fifty times the weight.**

---

## And the Problem Was Solved a Second Time, By Refusing It

**The X-24's entire difficulty was that no energy could be added once the approach began.** A booster
that lands on its engine answers that by adding energy, which is **not a better unpowered landing but a
decision not to attempt one**.

The article states it as a trade and not a victory. The X-24B carried no landing propellant and paid with
a corridor four tenths of a g wide and no second attempt. A booster carries propellant it could have
spent on payload and buys a hover, a divert and an abort.

**Which is better depends on what is coming back.** For a stage that is mostly empty tank the propellant
is affordable. For a vehicle returning from orbit with a heat shield already sized for the entry,
carrying landing propellant through that entry is expensive, **which is why things returning from orbit
still land the X-24B's way and things returning from a few minutes of flight do not.**

---

## The Physics Migrated to Lorries

**The most active base-drag literature today is not aeronautical.** A heavy goods vehicle is a
blunt-based body whose drag is dominated by its wake, and **one of the authors of the lifting-body
base-drag analysis went on to apply the same treatment to heavy trucks**.

**The drag bucket does not care what the body is for.** Base drag falls as forebody drag rises whatever
the body, so the factor of three at the optimum is as true of a lorry as of a lifting body.

---

## A Defect Introduced and Caught in the Same Pass

**The survey's one new equation was mangled and I found it by reading the generated body, not by a
check.**

The patch was written through a heredoc that collapsed its backslashes, so `write.py` ended up
containing `\text` rather than `\\text`, and its own f-string then read `\t` as a **tab**. The rendered
LaTeX came out as `V_[tab]ext{td}` with `\frac` reduced to `rac` and `\rho` to `ho`.

**Nothing would have caught it.** The equation count was right, the build succeeded, the braces balanced.
A rendered-escape check is now part of the build inspection.

**The A320 lesson was heeded**: the survey's cluster citations are live calls, so they track the clusters
rather than freezing.

---

## Publication Checks

**Prose style.** Clean across all 25 articles.

**Diction.** Five words sit above five per thousand and **all five were read in context and all five are
the article's own subject**: `vehicle`, `drag`, `base`, `factor` and `flare`. **`factor` was checked
specifically** and is doing three distinct technical jobs, being load factor, the factor of three, and
the named efficiency and profile factors.

**Acronyms.** Clean. `HL` and `XLR` are parts of the HL-10 and XLR-11 model designations and are exempt.

**Reference integrity.** 3,144 references, zero undefined, zero orphaned, zero duplicate URLs.

**URL response.** 3,122 external links. **2,613 of 2,613 DOIs confirmed registered in the Crossref
registry, zero unregistered.** Reading the 2,116 titles it printed found **only two contaminants**, a
journal guest editorial and a construction-machinery soil-interaction simulator. **That it found only two
is the query design and the accumulated filters working.** Rejection list 479 to 481.

**Numerical sanity.** 163 checks passing unchanged.

**Structural conformance.** Genre order intact, the three series sections present, The Source Base
immediately before Epistemic State.

**Build.** 25-article isolated build with all 53 equations rendering as display math across 16 sections
and 29 subsections, zero unbalanced braces and zero mangled escapes.

---

## A Note on the Era Balance

**The period count is unchanged at 765 against 766 while the primary fraction falls from 61.1 to 43.1
percent.** That is the directive working. This pass added roughly 900 contemporary references and
removed almost no period ones, so the denominator moved and the numerator did not.

---

## State

**A321 is complete. All four passes done, committed and pushed, not published.**

Twenty-five of seventy-two. The publication-order dependency is twenty-five deep.

**The next article is A322, the Bensen X-25**, editorial date 2025-10-31, Part 26 of 72. It is a
one-person autogyro, which is a sharper break from the preceding four than any in the series so far,
being subsonic, unpowered in autorotation, and built for a Air Force programme about escape from
disabled aircraft rather than about spaceflight. **Do not import the A321 pool.** The keystone is likely
autorotation itself, meaning the descent rate a freely turning rotor settles at, which is computable
from momentum theory and is the whole reason the concept was proposed.

**Still open and unchanged.** The fourth genre class, now **twelve** consecutive articles. The A305
length offer.
