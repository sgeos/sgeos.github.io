# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-05
**Task**: A305 publication review, the fourth and final pass. Committed and **pushed**. **Not
published.** All nine articles in the series remain in `_drafts/`.

---

## Contemporary Coverage

43 journal articles added from a 30-query Crossref sweep, taking contemporary references from 112 to
**155 and to 37.8 percent of dated references**. The absolute count now exceeds A301 at 101, A302 at
109, A303 at 105, and A304 at 107, which is appropriate given that this article is half again their
length rather than a departure from the series.

The sweep was aimed at the threads the two preceding passes opened rather than at the article's
original topics, so the additions attach to its own analysis instead of sitting beside it. Throat heat
flux estimation is set against the 1957 correlation the article uses, and the conclusion is worth
having: **the correlation is still the first thing anyone reaches for**, which says something about
how little that physics has moved. Zero boil-off work is set against the 18 percent of oxidiser per
hour the article computes for a cryogenic alternative. Pressurised-shell buckling is set against the
finding that this shell is in net tension and never buckles at all. Two-vector attitude determination
is set against the cone-intersection geometry the equation pass derived.

The most useful addition is a paragraph noting that every modern replacement for the measurements the
Aerobee pioneered, being radio occultation for electron density, lidar for the sodium layer, and limb
retrieval for ozone, **measures the region from outside it rather than within it**. That is why the
sounding rocket has not been retired, and the article could not make the point before because it had
not surveyed the replacements.

---

## Defects Found

**Two acronym failures.** OSTI was used without spell-out and NTRS appeared as a bare link display.
Both now spell out on first use.

**A third uppercase author name had slipped in.** Bondarenko arrived with a reference added after the
case normaliser last ran. Rather than patch the one case I re-ran the normaliser across the whole
master table, which corrected 69 display strings, most of them not yet cited.

**Diction.** `which is` measured 5.72 per thousand body words, above the 5.0 threshold, and `rather
than` measured 4.30. Twenty constructions rotated, bringing them to **4.62 and 3.58**. `rather than`
at 3.58 sits between A303 at 2.9 and A302 at 3.7, so it is a house norm rather than an A305 defect and
is reported as one. `vehicle` measures 5.35 per thousand and is the article's subject noun, so it is
left alone.

**Two seams no automated check flagged**, again found by reading. The OSTI spell-out had left a
redundant sentence repeating the acronym as its own link, and the propellant paragraph had acquired a
three-clause chain. Both rewritten.

---

## Verification

**All 89 worked numerical values re-derived and reproducing.** 474 references with zero undefined,
zero orphaned, and zero duplicate URLs. All 179 fixed identifiers at 200. **All 242 DOIs
Crossref-resolved on title at the 0.85 threshold with zero flagged**, and the single hand-entered
identifier verified individually and reported in full. `_verify.py` at the 0-error 21-warning corpus
baseline. Zero contractions, em-dashes, en-dashes, prose colons, prose semicolons, or prose
parentheticals. Zero doubled words, zero display-math seam defects, zero display-string collisions,
zero link texts out of sync with the master table. All thirteen genre sections present and in order
with The Source Base before Epistemic State. Isolated build succeeding with 200 rendered display
blocks, Part 9 navigation, no unresolved reference links and no surviving Liquid tags.

---

## Final State, and Three Deliberate Overages

**2226 lines, 200 display equations, 474 references, 20,352 words.**

All three densities exceed their genre ceilings, at 2226 against 1600, 200 against 130, and 474
against 380. Every one is licensed by the standing directive stating no length limit and no reference
limit, and every one is reported rather than trimmed. **This is the largest article in the series by a
wide margin and I want to flag that plainly rather than bury it in a metrics line.** The reason is the
subject. This article carries propulsion, flight dynamics, structures, heating, telemetry, recovery,
and six separate measurement techniques, where a typical article in the series carries three or four
of those, and each one earned its relations and its sources honestly.

Primary sources are 216 of 463 external, or 46.7 percent. The fall from 51.4 percent is denominator
growth from the contemporary additions rather than any removal.

**If the length is unwelcome, the cut I would make is the measurement-method material in What the Data
Changed**, which is roughly 300 lines and 25 equations and is the least load-bearing part of the
article. Say the word and I will make it.

---

## State

**Pushed.** Nothing in this series is published, and the deploy workflow builds without `--drafts`, so
the push is safe. **The publication-order dependency is nine deep**, A305 back to A297.

Nine articles complete of seventy-two. **Categories remain undecided** at
`aerospace history engineering`, nine articles deep and raised eight times. It fixes 72 URLs
permanently at publication and stays reversible with one edit until the first article publishes.

A306 is the Bell X-9 Shrike, which returns the series to a vehicle that is a missile testbed, and
which should keep the designation question this article opened open rather than answering it early.
