# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A312 publication review, the fourth and final pass. Committed and **pushed**. **Not
published.** All sixteen articles in the series remain in `_drafts/`.

---

## The Pass Found a Limit on the Article's Own Method

This is the most useful thing the review did, and it is a statement about the arithmetic rather than
about the aeroplane.

Every relation in this article treats air as a perfect gas at a ratio of specific heats of 1.4. That
fails when the gas gets hot enough to dissociate, and the stagnation-temperature relation says exactly
when. Setting it equal to the onset of oxygen dissociation near 2,500 kelvin and solving at the record
altitude gives **Mach 7.06**.

**The X-15 reached Mach 6.70, which is 94.8 percent of it.**

**The article's arithmetic is very nearly at the edge of its own validity at the aircraft's fastest
condition.** The ideal-gas stagnation temperature at orbital entry would be 30,500 kelvin, which is
physically meaningless because the air dissociates and ionises long before it gets there.

That is not a coincidence of my method. **It is close to what the phrase hypersonic aeroplane could
mean in 1954**, because a vehicle going meaningfully faster is not managing a thermal load but
conducting chemistry, and the materials of the period could not have been designed against a problem
nobody could yet compute.

---

## A Result That Changed Direction

The equation pass found that a hot wall absorbs a smaller fraction of the friction dissipation than a
cold one, and treated that as a mechanism by which a hot structure protects itself. That is correct at
the X-15's speed.

Extending the same relation shows the fraction tends to **the recovery factor over two, about 44.5
percent**, as speed grows, because the adiabatic wall temperature itself grows as V². Evaluated: 27.4
percent at the X-15's record, 36.7 at three kilometres per second, 41.7 at five.

**A faster vehicle gives a larger share of its friction dissipation to its own structure, not a smaller
one.** The protection the X-15 enjoyed is a low-speed luxury that fades exactly where it would be most
wanted. Both statements are in the text and neither supersedes the other.

---

## The Keystone Ratio Evaluated Elsewhere, and Why the Hot Structure Died

The X-15's 2.26 becomes 3.15 for Mach 8 cruise, 13.8 for a glide vehicle, **33.6 for orbital entry**,
and 66.9 for lunar return. Orbital entry is **14.9 times worse** by the measure the article is built on,
which is a sharper statement of why the architecture does not scale than the usual observation that
entry is hotter.

And the reason the hot metallic structure was abandoned is a fourth power:

| Surface | Temperature | Rejects | Against the X-15 record rate |
|---|---|---|---|
| Inconel at its design limit | 922 K | 3.28 W/cm² | 5.1 percent |
| Shuttle tile | 1,533 K | 26.6 W/cm² | 41.1 percent |
| Ultra-high-temperature ceramic | 2,273 K | 128.7 W/cm² | 198.5 percent |

**A ceramic leading edge rejects 39.2 times what Inconel at its limit rejects**, and can sustain twice
the heating rate that nearly destroyed the X-15A-2.

---

## Contemporary Coverage

A 65-query sweep returned **689 new records**, taking contemporary references from **13 to 111, or 33.5
percent of dated**, inside the 101 to 189 absolute range the series has held since A301. That closes
the largest contemporary gap any article had carried into a publication review.

Twelve subsections replaced eight. **The one worth naming is the nonequilibrium cluster**, because it
is the literature that begins exactly where this article's arithmetic stops. **[Lushchik et al 2026]
treats the Reynolds analogy factor in a compressible turbulent boundary layer on a cooled wall**, which
is this article's own relation at this article's own condition, published sixty years after the
aircraft flew.

Three further findings. **Transition is still being settled by flying experiments** — [Johnston et al
2026] reports BOLT-1B transition at flight conditions, which is a flight experiment for the same reason
the X-15 was one. **Shock interference became a field**, with its own separation criteria and control
techniques, built around the mechanism that destroyed the X-15A-2's pylon. And **no facility reproduces
flight**; what changed is that the resulting ignorance is now quantified rather than argued about.

---

## Two Defects Found

**A sweep of all 336 external URLs found one persistently dead DOI**, a 2026 paper on medical risks in
suborbital flight, and **the citation was removed rather than shipped**. A second 404 proved transient
and resolved at 200 on recheck with a longer timeout, which is worth recording because the first sweep
would have condemned it.

**Two link-text mismatches** were caught by the invariant, both truncated disambiguation suffixes.
**The URL-stability guard fired no drift** on a rebuild over 689 new records.

---

## Verification

**350 reference definitions, 336 external URLs, zero duplicates, zero orphans.** URL distribution: 152
plain 200s, 107 publisher 403s from bot detection, 69 DTIC DOI redirects, 4 202s, one publisher 500,
one transient 404 that resolved. **An HTTP 200 does not verify a citation** and the sweep does not claim
to.

All 20 newly introduced numbers re-derived independently and reproducing, on top of the 43 from the
equation pass and 40 from the draft. `_verify.py` at the 0-error 21-warning corpus baseline. Zero
contractions, em-dashes, en-dashes, prose colons, prose semicolons, prose parentheticals, doubled words,
duplicate headings, unbalanced emphasis markers, lone dollar-delimited lines, or adjacent display-math
seams. Two prose semicolons introduced by my own edits were caught and fixed.

**Equation count was measured before and after the section replacement**, per the A310 lesson, and rose
from 90 to 99 rather than silently dropping.

The Epistemic State was extended to record the validity limit, the direction change, and the
representative modern values.

---

## Final State

**1368 lines, 99 display equations, 350 references, 15,267 body words.**

**All three densities inside band. Nothing was trimmed at any point in any of the four passes**, which
makes A312 the seventh consecutive article to finish that way.

Contemporary 111, or 33.5 percent of dated. Primary 220, or 66.5 percent. Citation density 22.73 per
thousand, above A311's final 20.2, which reflects a survey section carrying 111 contemporary references.

---

## State

**Pushed.** Nothing in this series is published, and the deploy workflow builds without `--drafts`, so
the push is safe. **The publication-order dependency is sixteen deep**, A312 back to A297.

Sixteen articles complete of seventy-two. **Categories remain undecided** at `aerospace history
engineering`, sixteen articles deep and raised twenty times.

**A313 is the Bell X-16**, a reconnaissance aircraft cancelled before it flew. That is a
documentation-poor article immediately after the most documentation-rich one in the series, and the
genre document's short-article class exists for exactly this case. **The risk is padding a thin record
rather than stating the limit**, which is the opposite failure from the one A312 was written against.
