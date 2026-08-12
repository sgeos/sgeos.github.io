# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-12
**Task**: A334, the Boeing X-37. **Publication review complete. All four passes done.**
**Committed and PUSHED. NOT published.**

---

## Five Findings, and Reading Is the Only Reason Any of Them Surfaced

**Three curated links returned 404, and all three were addresses I built from what the page ought to be
called.** Wikipedia has no article titled Space Maneuver Vehicle, none titled Aerojet AR2-3 and none
titled Space Shuttle landing. The subjects are all real and well covered, under Boeing X-40, Rocketdyne
AR2 and Space Shuttle orbiter. **A plausible title is not a URL.**

**Nothing else could have caught it.** The identifier sweep covers `doi.org` links and the rendered
audit covers markup. **Neither looks at a hand-written encyclopaedia link**, so a curated reference is
checked only if this review actually requests each one. It now does, and the trap is recorded.

**One of the three dead links was a symptom of a wrong belief rather than of a moved page.** The AR2-3
is a **Rocketdyne** engine, widely credited to Aerojet, which is the successor company and not the
developer. The article now says so.

**Two drafting-history leaks removed.** The Source Base narrated an equation pass and an earlier
version of an audit, both referring to revisions no reader ever saw. **The epistemic content was kept
and the revision history dropped.** The section now states the finding in general terms, that a search
built from what an article says will not find the literature the article depends on, without narrating
how this article learned it.

**The aerobraking heritage was undercounted.** The text said three Mars orbiters and one at Venus. It
is **six spacecraft**: Magellan and Venus Express at Venus, and Mars Global Surveyor, Mars Odyssey, the
Mars Reconnaissance Orbiter and the ExoMars Trace Gas Orbiter at Mars between 1997 and 2018.

**The designation count was stale in two places**, still quoting a pool of 8,905 after it reached
13,351. **Re-measured, the finding is stronger than it was.**

---

## The Central Finding, Re-measured and Sharper

**Seventeen records in a harvested pool of 13,351 carry the X-37 designation. Fourteen survive into the
cited base of 5,545. Twelve of those fourteen are dated between 2000 and 2005 and every one of the
twelve is a space agency document.** The remaining two are outside analyses by people with no access.

**The programme's own literature stops in 2005, one year after the transfer to the defence research
agency, and not one record in the base describes a flown mission.** The vehicle has operated for
fifteen years since.

---

## The Citation Run Found Four More, and One Was a Rejection That Had Already Been Made

The full run over the expanded base checked **4,838 identifiers and reported 4 findings**, a rate of
0.1 percent. All four are now recorded and removed: a Mars surface geomorphology paper admitted by the
aerobraking harvest, a second Science news item indexed as a work, and two nonexistent Korean journal
identifiers.

**The two nonexistent ones had already been rejected in the previous pass and came back anyway.** The
deposited identifiers carry a **trailing full stop**, and I recorded the clean form, so the keys never
matched. **A DOI ending in a full stop is a different string and does not resolve**, which is both why
they were nonexistent and why the store missed them.

`gen_master` now strips a trailing full stop from every harvested identifier. **It does not strip a
closing parenthesis**, because several publishers deposit identifiers that legitimately end in one and
two of them are cited here.

---

## Verification

- **Prose style clean on every check.** Zero em dashes, en dashes, prose colons, prose semicolons,
  parentheticals and contractions. The only capitals are TUFROC, which is an acronym.
- **All 32 curated URLs resolve.** The single 403 is `spaceforce.mil`, a documented bot-detected host.
- **Reference integrity clean**, 5,762 used against 5,762 defined, no undefined, no orphaned, no
  duplicate URLs, definitions sorted.
- **11,469 reference entries scanned** for delimiters, entities, doubled commas and carets, all clean.
- `python3 _verify.py` **0 errors, 0 warnings**.
- `python3 tmp/a334/verify.py` **52 of 52** independent re-derivations.
- `python3 _lib/test_lib.py` **75 of 75**.
- `./_check.sh --drafts` **passes end to end**, 504 pages, no findings.
- Identifier sweep **300 of 300 resolved**, citation coverage **96.3 percent** of 4,838 distinct
  identifiers with a 0.1 percent finding rate.
- **Section order conforms to the research-aircraft genre** without exception.

---

## Final State

**18,700 lines, 42 display equations, 5,762 reference definitions, 100,776 words**, with all **5,545
research records cited and none left over**, plus 148 reference works.

Period half **3,061**, contemporary **2,428**, technical reports **1,116**. Contemporary coverage is
**43.7 percent** of dated records and **25.2 percent** is dated 2020 or later, which satisfies the
comprehensive-survey directive comfortably.

---

## Outstanding

**Nothing blocking.** The tree is clean and everything is pushed.

**A334 IS NOT PUBLISHED and publication of the thirty-eight X-Planes drafts has never been
authorised.** The article remains in `_drafts/`, the deploy workflow builds without `--drafts`, and the
publication-order dependency is now **thirty-eight deep**, so the set publishes in order or together.

**Three new entries were added to `_docs/process/VERIFICATION_TRAPS.md`**, being that a plausible title
is not a URL, that a measuring instrument has the same blind spot as the thing it measures, and that a
summary listing only exceptions cannot distinguish clean from unexamined.

**A335 is the Scaled Composites X-38 per the roster**, editorial date 2025-11-13, Part 39 of 72, and it
starts only on your prompt.
