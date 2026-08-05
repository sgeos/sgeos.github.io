# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-05
**Task**: A302, the Bell X-5, drafted. Committed and **not pushed**, per the four-pass rhythm.
A297 through A301 are unchanged and pushed. **No article in this series is published.**

---

## The Article Derives Its Central Numbers Instead of Quoting Them

The X-5's published dimensions are enough to recover its geometry, and that turned out to be the way
into the whole aircraft.

The projected span of a pivoting wing is $b(\Lambda) = 2(y_p + L \cos \Lambda)$. Two published spans
at two known sweep angles determine both unknowns. Inverting it gives a **pivot station of 0.953
metres, which is 18.7 percent of the semi-span**, and a movable panel of 4.42 metres. Nothing was
quoted for either figure and any reader with the same two spans can refute them.

From there the aerodynamic centre travel follows as **0.93 metres, or 58 percent of the mean chord**.
Aircraft are designed with static margins of five to fifteen percent. The X-5's sweep lever commanded
a change four to eleven times the entire stability budget of a conventional aeroplane. That single
number explains the jackscrew, the rails, the translating wing, and the mass, and it explains why
Langley's later answer of moving the pivot outboard behind a fixed glove was not an improvement to
Bell's mechanism but a dissolution of the problem it solved.

---

## The Accident Falls Out of the Same Geometry

This is the finding I would least want lost.

The NACA correlated spin recovery against the inertia grouping $(I_x - I_y)/(m b^2)$. **The span
enters squared, and sweeping the X-5's wing shortens the span from 10.21 metres to 6.32.** The
parameter therefore degrades by a factor of

$$\left( 10.21 / 6.32 \right)^2 = 2.61$$

with no change in mass distribution whatever. The mass had not moved. The lever had. The second
aircraft was lost in an unrecoverable spin at 60 degrees of sweep, which is exactly the setting where
that factor is worst, and the aerodynamic side degraded in the same direction at the same time
because the fin sits deeper in the horizontal tail's wake at spin attitudes.

**The factor of 2.61 is arithmetic. The attribution of the accident to it is inference**, and the
Epistemic State section says so in those terms. The sources consulted attribute the spin to tail
placement and to the layout generally. What this article adds is the observation that the NACA's own
correlating parameter degrades sharply with sweep and that the loss occurred where it is worst.

---

## One Inequality Made the Aircraft Possible

Sweep took thirty seconds. The short period took two. The configuration change was therefore fifteen
times slower than the mode it perturbed, so the pilot met a slow drift he trimmed out continuously
rather than a step he had to catch. That is why a 1951 aircraft could carry variable geometry with no
augmentation at all, and it is the assumption a great deal of the contemporary morphing literature
has to abandon, which is why so much of that literature is about the transient rather than the
endpoints.

---

## A Method Change, and Two Defects It Did Not Catch

**A302's reference section is generated from the anchors the body actually uses.** Orphaned
definitions are now impossible by construction and dangling anchors fail an assertion rather than an
audit. That is the direct answer to the defect A300 and A301 both shipped, and it worked.

Two defects still got through to the build, and both are worth recording.

**I truncated every Liquid tag in the corpus I inherited.** Extracting A301's apparatus with a regex
whose capture group ended at whitespace turned all fifteen `{% post_url ... %}` tags into `{%`. The
isolated build caught it as a syntax error. Worse, **I had seen the string `{%` in an earlier
duplicate-URL check and dismissed it as an artifact of the checker rather than the extractor.** It
was the extractor.

**Three Euler equations written on consecutive lines with no blank line between them** were converted
by kramdown into inline delimiters rather than display blocks, so they would have rendered running
together horizontally. Only comparing the source equation count against the rendered block count
found it. A corpus-wide scan found no other instance.

Independent re-derivation also found one arithmetic display defect, a pivot fraction shown as
0.95 over 5.106 equalling 0.187 when it computes to 0.186. The numerator now carries 0.953.

---

## State

1143 lines, 66 display equations, 318 references, 13,884 words. **Lines and references are inside
band on the draft pass alone**, which A301 was not.

All 318 cited with zero undefined, zero orphaned, zero duplicate URLs. All 182 meaningful-404 URLs at
200. All 44 DOIs Crossref-resolved on author and title. All 86 selected NTRS identifiers verified
individually. `_verify.py` at the 0-error 21-warning corpus baseline. Zero style violations. Isolated
build succeeding with Part 6 navigation.

**Two things are deliberately left for the passes that follow, and neither is padded.** Equations are
24 short of the 90 floor at 66. Contemporary references are 22.1 percent of dated, below the target
range. Word frequency shows `sweep` at 11.44 per thousand, which is the article's subject and
unavoidable, and `aircraft` at 9.57, which is the same outlier A301 had and which I have not
pre-empted.

**Publication order dependency is now six deep.** A302 back-references A301, A300, A299, A298, and
A297 through `post_url`.

---

## Categories

I proceeded on `aerospace history engineering` for A302 rather than blocking. It has now been raised
five times across six articles. The reason I did not stop is that it is one line of front matter,
reversible with a single edit across six drafts at any point up to publication, which is the only
moment it becomes permanent. If you want something else, saying so before the batch publishes costs
nothing.
