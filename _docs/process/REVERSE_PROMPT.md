# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-05
**Task**: A301 primary-reference review. A297 through A300 are unchanged and already pushed. **No
article in this series is published.** All five remain in `_drafts/`. A301 is committed and **not
pushed**, since the push is attached to the publication review.

---

## The Recorded Baseline Was Not Reproducible, and the Real One Is Worse

The process files recorded A301 at 43.3 percent primary. I could not reproduce that figure under any
definition I could state and audit, so I defined one that is checkable and measured all five articles
the same way. Counting NTRS-hosted programme documents as a share of all references, A301 held **41
of 269, or 15.2 percent, against 32.6, 31.4, and 32.1 percent for A298, A299, and A300**. It carried
roughly a third of the primary base its siblings carry. That is a larger and more specific deficit
than the recorded number described, and it explains the line shortfall the equation pass could not
close.

After this pass A301 holds **112 NTRS documents, 32.9 percent**, which is at parity with its
siblings. References dated 1960 or earlier rose from 22.9 to **43.2 percent** of dated references,
the highest of the five.

**The article is 1149 to 1313 lines and 269 to 340 references.** Lines are now inside the 1300 to
1600 band, and they got there by citing new material rather than by padding.

---

## Three Findings That Change What the Article Says

**A criterion contemporaneous with the aircraft exists.** The equation pass closed on modern
handling-qualities criteria and had to concede that they postdate the programme by two decades and
are quoted as a restatement rather than as a standard anyone judged the X-4 against. That concession
is now much smaller. Sternfield and Gates, NACA-TN-1859 of 1949, give a method for constructing a
boundary in the plane of period against damping that separates satisfactory from unsatisfactory
oscillatory behaviour, published the year before the NACA began flying the aircraft. The X-4 result
is no longer only unsatisfactory by a rule invented afterward. It was measurable against a rule that
existed while the aircraft was flying.

**The Oswald efficiency factor now points at Oswald.** The induced-drag argument turns on a span
efficiency the equation pass corrected from 0.78 to 0.95. The harvest returned NACA-TR-408 of 1932 by
W. Bailey Oswald, which is the report that defined the quantity. The correlation the article uses is
a later fit to it, and the article now says so.

**The article was missing a second research role, and it is a positive one.** After the blunt trailing
edge experiments the X-4 flew a long series of approaches with its split flap speed brakes open,
spoiling the lift-to-drag ratio deliberately, reportedly below three to one, to generate landing data
for future rocket-powered aircraft that would arrive unpowered and steep. The thread runs from
Matranga and Menard 1959 on a delta-wing interceptor through the **same author's** analysis of the
first thirty X-15 landings in 1961 and onward into routine gliding re-entry practice. An article that
otherwise reads as a clean negative result had a positive contribution in it that no pass had found.

I could not locate a primary document for the X-4's own landing series despite repeated searching, so
that claim is attributed to the secondary account and **flagged as reported rather than verified** in
the Epistemic State section. The successor literature is primary-documented.

---

## A Defect the Previous Pass Left, and How It Survived

The equation pass glued prose onto the same line as a closing display-math delimiter, so the
induced-drag ratio ran straight into the next sentence with no break and the sentence itself became a
non sequitur. **`_verify.py`, the anchor integrity check, and the isolated Jekyll build all passed
it.** This is the third instance of the same class, after the two duplicated clauses A297 shipped
from its own equation pass. Automated checking does not see edit seams. Only reading the connective
lines does. It is repaired.

---

## What Was Rejected and Why

The harvest returned 445 distinct documents from 62 queries built from this article's own terms, of
which 129 were programme-era and uncited. I selected 75 and verified each individually against the
citations API rather than trusting the search response.

Seven did not survive. **Four were already cited under existing anchors**, and all four had been
picked out of the ad-hoc probes I ran while testing the API rather than out of the filtered harvest,
which had them flagged correctly. **One matched on title tokens alone** and proved to be a study of
cruciform interdigitated missile models. **Two were off-configuration**, being X-1 vortex-generator
work and a horizontal-attitude VTOL model, and precision was worth more than the count. A follow-up
harvest supplied three low-lift-to-drag approach documents, giving 71 net.

Per the method rule, this article's reference data was built from its own harvest. No previous
article's generator was imported, which is the defect A300 and A301 both shipped.

---

## Verification

340 references with zero undefined and zero orphaned. All 71 new NTRS URLs at 200. `_verify.py` at
the 0-error, 21-warning corpus baseline with no new warning attributable to this article. Zero
contractions, em-dashes, en-dashes, prose colons, prose semicolons, or prose parentheticals. Zero
doubled words, zero malformed links, zero display-math seam defects. Isolated build succeeding with
Part 5 navigation and zero unresolved anchors in the rendered page. Citation-introducing prepositions
peak at 34 percent, matching A300's corrected level rather than the 70 percent A300 first produced.

---

## One Thing for You to Decide, and One Standing Question

**Contemporary share fell from 38.5 to 27.6 percent** of dated references. The absolute count is
unchanged at 69, so this is dilution by 71 new primaries rather than removal of anything. It moves
the article from above the 28 to 33 percent target band to marginally below it, and into line with
A298 at 26.3 percent. The publication review can restore it if you want it inside the band. I did not
add contemporary references in a pass you asked to be about primary ones.

**Categories remain undecided.** `aerospace history engineering` has now been carried through five
articles and is still my assumption. It fixes 72 URLs permanently at publication and you have
declined redirects. This is the fifth time it has been raised.

---

## State

Committed, **not pushed**, per the four-pass rhythm. Four commits are now unpushed. A301's
publication review is the remaining pass before A302.
