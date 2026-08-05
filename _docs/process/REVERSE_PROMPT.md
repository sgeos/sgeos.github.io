# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-05
**Task**: A298 drafted, then taken through an equation-density review. A297 is unchanged and already
pushed. Neither article is published. Both remain in `_drafts/`.

---

## A298, Bell X-1

`_drafts/x_planes_bell_x1.markdown`, editorial date 2025-10-07, series index 2 of 72.

**1209 lines, 108 display equations, 259 reference definitions, 14,960 words.** Drafted at 1095
lines and 80 equations, then taken through the equation-density review you asked for, which added 28
equations across 17 edits and closed the line gap by about half as a side effect.

**The review found one arithmetic error in the drafted text.** The axial acceleration available with
two chambers burning was stated as 1.6 metres per second squared and computes to 1.25. Writing the
relation down rather than asserting the number is what exposed it, which is the argument for this
kind of pass in one line.

The additions close places where the prose named a result or relied on a relation without showing
it. The elevator effectiveness parameter was described as a function of chord ratio without the
function, which turns out to be worth stating because thin-airfoil theory returns 0.66 while the
representative value used is 0.5, and the gap between them is viscous. Stick force was said to be
proportional to hinge moment with no constant. The position-error sensitivity was written as an
abstract $f$. The drag rise itself, the article's subject, had no functional form anywhere. Skin
friction, base drag, and the neutral point were all used and never derived, and the unpowered lake-bed
landing that every flight ended with had no glide relation at all.

One result is worth your attention. Assembling the drag build-up from four independent contributions,
being friction at 0.0138, fuselage wave drag at 0.0310, base drag at 0.0079, and induced drag at
0.0052, gives 0.058 against a measured transonic peak near 0.05. An estimate from four separate
mechanisms landing within fifteen percent of flight measurement is a good result, and it also shows
which term is weakest, since wave drag is both the largest and the least certain.

The keystone is the magnitude of the transonic drag rise and whether an aircraft could retain the
control authority to fly through it. Two results carry the article.

The engine was sized against an unknown. Inverting the drag relation gives the largest drag
coefficient the aircraft could overcome at the test condition, which is 0.173. The measured
transonic peak was near 0.05. The X-1 was built to push through a drag rise three times worse than
the one it found, which is what designing against an unknown looks like in arithmetic.

The more interesting result is that the aircraft was never thrust-limited, it was control-limited.
As the aerodynamic centre migrates aft through Mach one the trim increment demands 1.8 degrees of
all-moving stabilizer, which was trivially available, against 18 degrees of elevator once
shock-induced separation degrades the effectiveness parameter, which was not available and would not
have worked anyway. That is Mach tuck as an arithmetic shortfall rather than a mysterious barrier.

A third finding is a measurement one. At Mach 1.06 the isentropic and Rayleigh supersonic pitot
relations differ by 0.02 percent, so the pitot ratio carries almost no information about which side
of Mach one the aircraft is on. The determination could not have rested on a cockpit Machmeter, and
did not. At Mach 1.45 the same two relations differ by 5.5 percent.

**One publication-order dependency.** A298 cites A297 through `post_url`. Publishing A298 while A297
is still a draft fails the entire site build. They publish together or A297 first.

**A genre-document change you should look at.** The full-aircraft equation band was 60 to 80, taken
from the History of SpaceX medians before this series existed. Both A297 and A298 have now been
through an explicit equation-density review at your request and landed at 147 and 108. Treating that
as a standing expectation rather than an exception, I raised the full-aircraft band to 90 to 130 and
recorded the rule that actually produces the number, which is that any relation the prose names or
relies on must be shown. Revert it if you would rather the band stay where it was and these two
articles be the exceptions.

---

## Verification of A298

All 75 worked numerical examples re-derived independently, being the original 54 plus 21 introduced
by the equation pass. Two disagreed across the two rounds and were corrected, a learning-curve figure
stated as 25 percent that computes to 23 and the axial acceleration figure above. Four further
figures were tightened for precision. Zero duplicated clauses at edit seams, checked explicitly
because the A297 equation pass introduced two.

All 259 references cited, zero undefined, zero orphaned. **All 142 URLs whose status code carries
information were swept and all returned 200**, being the Wikipedia entries and the fixed NTRS
document identifiers. Every DOI was either already author-checked through Crossref for A297 or
harvested directly from Crossref for this article.

`_verify.py` clean, zero prose style violations, both agency acronyms spelled out before first use,
word frequency clean with only subject terms above five per thousand. Isolated production build
succeeds with both drafts present, the series navigation renders Part 2, and the A297 cross-link
resolves.

---

## Previous State of A297

`_drafts/x_planes_framing.markdown`, editorial date 2025-10-06, series `x_planes`, index 1 of 72.

**1765 lines, 147 display equations, 421 reference definitions, 21,933 words.** The History of
SpaceX medians for comparison are 1345 lines, 72 equations, and 306 references.

It grew across four passes and each step is traceable. Drafted at 1245 lines, 76 equations, and 327
references, which was parity. The equation review took it to 147 equations by closing 19 places where
the prose named a result without showing it. The primary-reference review took it to 372 references
and raised primary sources from 13.5 to 24.5 percent. The publication review added the contemporary
literature and brought it here.

---

## What the Publication Review Found

Two classes of defect, one procedural and one substantive.

**Three acronym violations, all now fixed.** NACA was first used at character 14,960 but spelled out
only at 86,636. **NASA was never spelled out anywhere in the article.** DARPA's expansion trailed its
first use. Both agency names are now introduced in the opening paragraph and DARPA is expanded at its
genuine first occurrence. These are exactly the defects the acronym check exists to catch, and none
of the other verification would have found them.

**The contemporary literature was largely absent, and that was the real finding.** Measuring the
reference index by decade showed only 10.2 percent of dated references were 2010 or later and exactly
one was from the 2020s. The distribution peaked in the 2000s and fell off a cliff. Against your
standing directive that these articles serve as a comprehensive survey and review of the contemporary
literature, that was a straightforward failure rather than a matter of taste.

I added a `## The Contemporary Literature` section with eight subsections, covering hypersonics and
airbreathing propulsion, boundary-layer transition, thermal protection, aeroelasticity and active
control, configuration and propulsion integration, sonic boom, experiment design and system
identification, and reusable launch. It closes by naming where the contemporary literature is thin,
which is on the designation system as an administrative object, on cancelled programmes, and on
experiment rather than computation.

**Contemporary coverage is now 28.8 percent, up from 10.2. Primary sources are 33.7 percent, up from
24.5.** 49 contemporary references were added, being 41 journal articles with digital object
identifiers harvested from Crossref under a 2015 date filter and 8 NASA reports from the NTRS API.

The section is a review rather than a citation dump. It argues, for instance, that transition
prediction is the clearest case of a question the X-series opened and did not close, that
contemporary aeroelastic tailoring generalizes the X-29 solution rather than repeating it through
tow-steered laminates and active suppression, and that the X-59 is the purest contemporary instance
of this article's own information-economics argument, being an aircraft built to produce a number
that a rulemaking body has already agreed to accept.

---

## Verification

All 34 worked numerical examples re-derived independently and agreeing.

All 421 references cited in the body, zero undefined, zero orphaned.

All 65 NTRS fixed identifiers swept at 200. All 22 original digital object identifiers resolved
through Crossref and compared on author and title, of which two were defective and were repaired. The
41 contemporary identifiers came out of Crossref itself and are cited with the titles and authors it
returned.

`_verify.py` clean at zero errors with the same 21 pre-existing warnings the corpus already carried.
Zero prose style violations. Word frequency clean, with `flight`, `aircraft`, and `series` above five
per thousand but all three being the article's literal subject, which the style guide treats as
legitimate. Isolated production build succeeding with every `post_url` resolved.

---

## Pushed, Not Published

Six commits are now on `origin/master`. The article is in `_drafts/`, and the deploy workflow runs
`bundle exec jekyll build` without `--drafts`, so nothing about A297 is live. Publishing still
requires the two-commit sequence and your instruction to run it.

---

## One Roster Correction Found Earlier

Wikipedia titles the X-62 as the **General Dynamics** X-62 VISTA, because the airframe is a modified
F-16D. The roster in `HANDOFF.md` calls it the Lockheed Martin X-62 VISTA. Both are defensible, since
Lockheed Martin and Calspan performed the modification, but A359 should name the disagreement rather
than pick silently. No change has been made to the roster.

---

## Still Waiting On You

1. **Categories.** `aerospace history engineering` remains my assumption, rendering the URL as
   `/aerospace/history/engineering/2025/10/06/x_planes_framing.html`. Free to change now, fixed
   permanently at publication across all seventy-two articles.

2. **109 Open Library book citations still point at search endpoints**, which cannot return a
   not-found. Open Library exposes a search API and the same upgrade that fixed the NASA citations
   would resolve these to edition pages. The NASA side is done and this is what remains.

3. **Wikipedia is still the largest single class.** For the aircraft entries that is defensible,
   since for many designations no better public overview exists. For the concept entries it is
   weaker, and many now sit alongside a primary source that could carry the citation alone.

4. **A298, the Bell X-1**, is next whenever you are ready. Your stated preference was to review A297
   before the pattern is set across seventy-two articles.
