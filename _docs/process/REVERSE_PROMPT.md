# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-11
**Task**: A332 primary-reference review, the third of four passes. **Committed, not pushed.** **Not
published.**

**References 5,814 to 7,188 definitions and 5,678 to 7,051 cited**, with all 7,051 master records
cited and none left over. The article moved from 18,723 to 22,924 lines and from 101,571 to 123,341
words. **Equations unchanged at 71.**

---

## Both Halves Rose, Which Has Not Happened in This Series Before

| | After drafting | After the equation pass | After this pass |
|---|---|---|---|
| Harvested pool | 7,567 | 7,567 | **10,069** |
| Cited records | 5,678 | 5,678 | **7,051** |
| Period count, through 2001 | 2,820 | 2,820 | **3,524** |
| Period fraction | 49.7 percent | 49.7 percent | **50.0 percent** |
| Contemporary count, 2015 onward | 2,514 | 2,514 | **3,099** |
| Contemporary fraction | 44.3 percent | 44.3 percent | **44.0 percent** |

**The period count rose by 704 and its fraction rose by three tenths of a point.** In A330 and A331
this pass raised the period count while the contemporary fraction fell underneath it, and the standing
warning is that neither movement is a fact about coverage. **Here both counts rose and both fractions
barely moved, because the harvest was aimed at subjects rather than at eras.** Both columns are in the
article.

---

## The Promotion Rule, Fourteenth Article Running, and the Correction Was Vocabulary

**Seven of the ten subjects the new equations name were thin, one stood at zero, and the two carrying
the article's sharpest new results stood at one record each.**

| Newly promoted subject | Before | After |
|---|---|---|
| **Momentum drag of a lift system** | **1** | **74** |
| **Canted joint kinematics** | **1** | **89** |
| Fan stage loading and tip Mach | 1 | 129 |
| Centre of gravity limits in hover | 2 | 32 |
| Induced drag and span efficiency | 4 | 145 |
| Barometric and standard atmosphere | 8 | 35 |
| **Fuel volume and density** | **0** | **49** |

**Not one extra query was needed once the vocabulary was right.** The article says momentum drag and
the period reports say **inlet momentum drag, ram drag, lift engine installation losses and
propulsion-induced effects**. The article says canted joint and the period says **swivel duct,
deflector, skewed axis coupling and spatial mechanism**.

---

## A Defect in My Own Search Pattern, and It Fails Silently

**One of those gaps was mine rather than the literature's.** The cluster pattern matched the singular
`installation effect` where every report in the field writes `installation effects`, and a word
boundary after the singular refuses the plural. **An entire subject was routed to the catch-all without
anything reporting an error.**

**This failure mode returns a smaller answer rather than a wrong one, so it reads as a thin literature
instead of as a bug.** That is why it survived a draft pass and an equation pass. The same family has
appeared before in this series. Widening the pattern took momentum drag from 7 records to 36 in its own
cluster and from 1 to 74 across the pool.

---

## The Keystone Primary Sources, Now Cited by Name

The draft cited this architecture entirely through secondary description. **It now rests on the
inventor's own record.**

- **The patent**, Bevilaqua and Shumpert, United States Patent 5,209,428, granted 1993.
- **Bevilaqua 1996**, dual cycle operation of the shaft driven lift fan propulsion system.
- **Bevilaqua 2009**, the genesis of the F-35, which is the Wright Brothers Lecture, and its companion
  paper on inventing it. **Both were absent from the pool and were injected deliberately**, and both
  verify against the Crossref registry.
- **Palmer and Holdø 2002** and **Sayma and Vahdati 2003**, the first open-literature studies of the
  fan itself.

**And the pool contained something I did not go looking for.** Bevilaqua published on
**thrust-augmenting ejectors** in 1974, 1977, 1984 and 1987. **The ejector is the other way of adding
mass flow to a lift system**, entraining ambient air into a high-velocity primary jet rather than
driving a fan with a shaft, and it was the leading candidate for supersonic vertical landing for two
decades. **The man who displaced it had spent fifteen years on it.** That is now in the article.

---

## The Headline Source-Base Claim Survived a Larger Pool

**Zero of 10,069 harvested records carry "X-35" in the title**, after four harvests that asked for it
directly. The claim was made at 7,567 and **stayed at zero while the pool grew by a third**, which is a
stronger statement than the one the draft could make. Forty-three records name the Joint Strike Fighter
and fourteen name the F-35. **Nothing names the aeroplane.**

---

## Two of My Own Style Defects, Caught by the Checks That Exist for Them

**A prose semicolon**, in a sentence I wrote this pass, caught by `check_any`.

**The acronym check fired exactly as the handoff predicted it would.** A growing reference set moved a
verbatim NASA in a citation title ahead of any authorial spell-out, and there was no authorial
spell-out at all. The article now spells out the National Aeronautics and Space Administration in
Programme Origin, before the first citation list, at character 6,487 against the first citation
occurrence at 6,673.

---

## What Stays Thin, and It Is Now Five Headings and Two Genuine

| Subject | Records | Kind |
|---|---|---|
| Ground roll and takeoff distance | 2 | **Settled.** A closed form in every performance textbook |
| Disc loading | 3 | Wrong heading. It sits inside momentum theory, which holds 175 |
| Jet footprint and ground erosion | 4 | Wrong heading. It lives inside impingement work, which holds 680 |
| Rotor spin-up and inertia | 7 | Wrong heading. It lives inside drive-system transients |
| Thrust lapse with altitude | 12 | Wrong heading. It lives inside installed performance |
| Stagnation temperature and kinetic heating | 14 | Moved. Its modern half is hypersonics |
| Standard atmosphere | 35, three modern | **Settled, and the harvest proved it** |

**The standard atmosphere is the clearest case of settled knowledge this series has produced.** A
harvest aimed directly at it took the count from 9 to 35 and returned almost nothing published after
2015, because it is a standards document rather than a research subject. **Reporting that is more
useful than padding it.**

---

## Verification

- `python3 tmp/a332/verify.py` **115 of 115**, unchanged, since this pass added no arithmetic.
- `python3 _verify.py` **0 errors, 21 warnings**, the baseline.
- `python3 tmp/errata/check_any.py` **0 failures, 0 warnings**.
- `python3 _lib/test_lib.py` **53 of 53**.
- **Reference scan clean across 14,321 visible entries**, with zero semicolons, parentheses, dashes,
  dollars, backslashes, angle brackets, braces, entities, curly quotes or soft hyphens in link text,
  zero contractions anywhere, and **zero duplicate, undefined or orphaned definitions.**
- **75 of 75 sampled DOIs verify against the Crossref registry**, including all five keystone records,
  with two honestly declining the author check.
- **Isolated build exit 0**, page 1.62 MB, with 71 open and 71 close display-math delimiters, zero
  unexpanded markers, zero nested empty lists and zero blockquotes.

---

## Next

**A332 pass four**, the publication review, on your prompt. **It also asks for a push.** The
contemporary half stands at 3,099 records and 44.0 percent, which is healthy, so I expect that pass to
be about prose, the full URL sweep and the final structural check rather than about another harvest.
