# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-11
**Task**: A332 publication review, the fourth and final pass. Committed and **pushed**. **Not
published.**

**Final state: 27,560 lines, 71 display equations, 8,710 reference definitions, 148,103 words**, with
all 8,573 master records cited and none left over. **All thirty-six articles remain in `_drafts/`.**

---

## The Contemporary Survey, Which Doubled

Coverage stood at 3,099 records and 44.0 percent with ten clusters under thirty modern records, six of
them carrying arguments. **A harvest took it to 4,466 and 52.1 percent, with 2,028 published from 2022
onward.**

**The most useful thing it found is where this article's newest physics actually lives now.**

**Momentum drag has almost no contemporary literature under that name and a large one under others.**
The modern vocabulary is boundary layer ingestion, distributed propulsion installation, and the
tiltrotor or tiltwing conversion corridor. **That last one is the closest analogue this article has**,
because a conversion corridor is exactly what it computed when it found the fully wing-borne speed at
146.8 knots and observed that the X-35B converted well above it. An electric vehicle with many rotors
faces the same trade between converting early, where the lift system must carry weight, and converting
late, where it must absorb drag.

**The canted-joint kinematics are not an aeronautical subject any more.** Spatial mechanisms and
constant-velocity couplings are studied continuously in robotics and machine design. **The
high-temperature rotating seal is the part that stayed aeronautical**, because it is the requirement
that makes the mechanism hard rather than the geometry.

**And one the draft did not expect.** The fan-bay calculation assumes a fuel density, which in 2001
would have been a table lookup and is now an active subject, because sustainable aviation fuels have
densities differing from conventional kerosene. **An aeroplane that gave up three thousand pounds of
fuel volume to carry a fan is exactly the kind that feels that.**

---

## The Count-Versus-Fraction Trap, in Its Classic Form, After Two Passes That Did Not Show It

| | Draft | Equation pass | Primary pass | Publication pass |
|---|---|---|---|---|
| Harvested pool | 7,567 | 7,567 | 10,069 | **12,974** |
| Cited records | 5,678 | 5,678 | 7,051 | **8,573** |
| Period count | 2,820 | 2,820 | 3,524 | **3,640** |
| Period fraction | 49.7 | 49.7 | 50.0 | **42.5 percent** |
| Contemporary count | 2,514 | 2,514 | 3,099 | **4,466** |
| Contemporary fraction | 44.3 | 44.3 | 44.0 | **52.1 percent** |

**The primary pass raised both counts and both fractions, which had not happened before in this
series.** Then this pass raised the period count again, by 116, **while its fraction fell 7.5 points.**
Nothing was removed. The contemporary harvest moved the denominator underneath it. **All four columns
are in the article rather than the last one**, because a single column of fractions would read as a
regression when the period base grew in every pass.

---

## A New Homonym, and It Is on the Article's Own Term of Art

**Figure of merit is a standard quantity in thermoelectrics and in plasmonic and photonic sensing.** A
contemporary search for hover efficiency returns solar cells and graphene sensors, and those records
were reaching the momentum theory cluster until they were filtered.

The same random-sample reading found railway power protection, bridge aerodynamics, astronomical
transient surveys and point-cloud shape completion. **None of the five was anticipated**, which is the
standing lesson about this class.

---

## A Third Shared-Library Defect, Found by the Corpus Checker

**Double-escaped markup survives a single unescape pass and the later rules then mangle it into visible
junk.** A publisher emitting an escaped paragraph tag followed by an escaped non-breaking space decodes
once to real markup plus a literal entity. The tag rule removes the tag, the surviving entity meets the
ampersand rule and becomes `andnbsp;`, and the semicolon rule strips the terminator. **The article
briefly carried link text reading `andnbsp andnbsp andnbsp`.**

`refs.clean` now unescapes to a **fixed point**, bounded to four iterations so a hostile title cannot be
made to expand. Regression test added and `test_lib` is **53 to 54**.

---

## A Process Defect I Should Flag, Because It Silently Checks the Wrong Corpus

**`_verify.py` resolves `_posts` and `_drafts` relative to the working directory.** Running it by
absolute path from the isolated build tree therefore checks the 333 staged files there rather than the
corpus, and it reported **0 errors and 42 warnings** while the corpus reading is 21.

**I caught this only because the number moved.** The handoff already says to know the expected number
rather than just pass or fail, and this is a second door into the same hazard: **an absolute path to
the script is not enough when the script's own paths are relative.** Every corpus reading in this
report was retaken from the repository root and confirmed twice. **The reading is 0 errors and 21
warnings.**

---

## What the Prose Pass Changed

- **Diction**: `it is worth` stood at 7 occurrences and a rate above the corpus maximum. Reduced to 2.
  **Zero constructions now exceed the corpus maximum.**
- **A stale figure**: the Epistemic State still claimed fifty-one verification checks. It is 115, and
  that section now also covers the momentum drag, the hot gas margin, the canted-joint geometry and the
  control power, none of which existed when it was written.
- **An invented number**: the Conclusion said the sortie made its point in ninety seconds. Nothing
  supports that and it is removed.
- **An imprecise one**: the Conclusion said the fan presses about half as hard as the core. The bracket
  is 1.69 to 2.00, so it is between half and three fifths, and it now says so.
- **A broken transition** left by an earlier edit, and an **opaque cross-reference** to two defects from
  other articles that a reader has no way to interpret.

---

## Verification

Every reading below was taken from the repository root.

- `python3 _verify.py` **0 errors, 21 warnings**, the baseline.
- `python3 tmp/errata/check_any.py` **0 failures, 0 warnings**. Twelve genre sections and three series
  sections in order, with the Source Base immediately before Epistemic State.
- `python3 _lib/test_lib.py` **54 of 54**.
- `python3 tmp/a332/verify.py` **115 of 115** by an independent verifier that does not import the
  calculation.
- **Prose style clean**: zero em dashes, en dashes, minus signs, contractions, prose colons, curly
  quotes and capitals used for emphasis. **The only semicolon and parentheses in the whole article are
  the debug tag**, which is the permitted exception.
- **Reference scan clean across 17,365 visible entries**, with zero punctuation defects of any kind in
  link text and **zero duplicate, undefined or orphaned definitions**, zero blockquotes.
- **Acronym check re-run after the reference growth.** The authorial spell-out sits at character 6,487
  against the first citation occurrence at 6,835.
- **Sweep clean with zero hard failures**: **800 of 800 sampled DOIs verify against the Crossref
  registry** with 25 honestly declining the author check, **453 of 453 NTRS identifiers resolve**, and
  **102 of 102 curated URLs return OK**.
- **Isolated 36-article build exit 0**, page 1.95 MB, **71 open and 71 close display-math delimiters
  matching the equation count exactly**, zero unexpanded markers, zero nested empty lists, zero
  blockquotes and zero entity junk.
- **Confirmed after pushing** that the article returns 404 while the site root returns 200, which is
  correct because nothing in the series is published.

---

## Next

**A333, the McDonnell Douglas X-36**, editorial date 2025-11-11, Part 37 of 72, on your prompt.

**Publication has still never been authorised and the `post_url` interlock is now thirty-six deep**, so
these articles publish in order or together.
