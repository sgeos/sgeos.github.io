# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-05
**Task**: A301 publication review, the fourth and final pass. Committed and **pushed**. **Not
published.** All five articles in the series remain in `_drafts/`.

---

## Two Mathematical Defects, One of Them Two Orders of Magnitude

**The wing pitch damping expression did not produce the number the article used.** The line read

> $C_{m q, \text{wing}} \approx -\frac{\pi A}{4} \left( \frac{x_{ac} - x_{cg}}{\bar{c}} \right)^2 \sim -1$

and for the article's own inputs, an aspect ratio of 3.60 and a static margin of 0.05, that formula
returns **minus 0.007**. The same line asserted an order of minus one, and every subsequent
calculation used minus 0.8. Two orders of magnitude separated the formula from its stated magnitude,
and the draft pass, the equation pass, and the primary-reference pass all went past it.

The physics is that a wing damps in pitch two ways and the article had conflated them. The
parallel-axis term, which is the tail relation applied to the wing's own lift at its aerodynamic
centre, evaluates to minus 0.02 and vanishes entirely when the centre of gravity sits at the
aerodynamic centre. The wing's own unsteady chordwise loading does not vanish there and is of order
unity, and that is where minus 0.8 comes from. The passage now separates them, evaluates the first,
labels the second as adopted rather than derived, and notes that the conclusion is insensitive to it
because any value small against the tail's minus 13 gives the same finding. **The argument is
unchanged and better supported.**

**A split-drag yaw expression divided by unity.** `\frac{y_{\text{eff}}}{1}` is meaningless and is now
just `y_{\text{eff}}`. This is the **third instance of that malformation in the series**, after A297
and A299. It may be worth a check across the corpus rather than per-article discovery.

---

## The Diction Check Earned Its Place Again

`aircraft` measured **12.37 uses per thousand body words against a sibling range of 5.31 to 8.30**,
driven by twenty instances of `tailless aircraft` and seven of `conventional aircraft`. Twenty-five
occurrences were rotated across design, layout, configuration, case, and the designation itself,
bringing it to **9.07**. It remains the highest of the five, which the article's constantly
comparative structure justifies, since it contrasts two configurations in nearly every paragraph.
`configuration` rose to 4.22 and stays under the 5.0 threshold.

---

## Contemporary Literature, and a Deliberate Departure From the Band

A twenty-eight-query Crossref harvest under a 2019 date filter returned 296 candidates, of which 143
passed a topical screen and **32 were selected and verified individually against Crossref on author
and title**. Contemporary references rose from 69 to **101**, and from 27.6 to **35.8 percent** of
dated references.

**That is above the 28 to 33 percent range A297 through A300 settled at, and it is deliberate.** The
standing directive asks for a comprehensive survey of the contemporary literature, and the absolute
count of 101 is now the highest in the series. The primary base is diluted rather than displaced,
holding at 112 NTRS documents and 38.3 percent of dated references at 1960 or earlier. **Tell me if
you would rather I hold the percentage band and trim.**

Three of the additions land on arguments the article already makes rather than beside them. Actuator
saturation treated as a nonlinear bifurcation is the rigorous form of the amplitude-dependent
effective delay the article writes down by hand. Delay effects in longitudinal augmentation are the
formal statement of the actuator bandwidth inequality. Configuration parameter boundaries derived
from closed-loop flying qualities requirements are the method that, had it existed in 1946, would
have made the X-4 an expensive confirmation rather than a discovery, which is a sharper way of saying
what the article says about the answer being available before the aircraft flew.

A wing rock paragraph was added, since it is the lateral member of the tumbling family and afflicts
exactly this planform. The reported tendency to hunt about all three axes rather than in pitch alone
is consistent with proximity to it. **No source consulted makes that identification, and the
Epistemic State section now says so explicitly.**

---

## Verification

1391 lines, 98 display equations, 372 references, 18,358 words. All three densities inside band.

372 references cited with zero undefined and zero orphaned, zero duplicate URLs. All 182
meaningful-404 URLs at 200. All 99 DOIs resolved through Crossref and compared on author and title.
`_verify.py` at the 0-error, 21-warning corpus baseline with no new warning attributable to this
article. Zero contractions, em-dashes, en-dashes, prose colons, prose semicolons, or prose
parentheticals. Zero doubled words, zero malformed links, zero display-math seam defects. Genre
section order conforming. Isolated build succeeding with Part 5 navigation and zero unresolved
anchors in the rendered page.

The 76 Open Library URLs are search queries and return 200 for anything, so they are **not** evidence
of anything and are excluded from the meaningful-404 count. That upgrade remains offered and not
taken up.

---

## State and the One Standing Question

Pushed. **Nothing in this series is published**, and the deploy workflow builds without `--drafts`,
so the push is safe. The publication-order dependency is five deep, since A301 back-references A300,
A299, A298, and A297 through `post_url`.

**Categories remain undecided.** `aerospace history engineering` has now been carried through five
articles and is still my assumption. It fixes 72 URLs permanently at publication and you have
declined redirects. This is the fifth time it has been raised, and A302 is next.
