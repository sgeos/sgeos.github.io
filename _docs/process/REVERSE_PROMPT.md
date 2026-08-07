# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-07
**Task**: A309 publication review, the fourth and final pass. Committed and **pushed**. **Not
published.** All thirteen articles in the series remain in `_drafts/`.

---

## The Review Ran the Article's Own Arithmetic Forward

This is the most useful thing the pass did and it is the new lead of the contemporary section.

Nothing in the range law has changed since 1958, so the accuracy chain can be recomputed against a
modern requirement by substituting a smaller circular error probable. Doing so gives, for a
hundred-and-twenty-metre weapon, a burnout speed correct to **one part in 362,029**, which is two
centimetres per second, requiring an accelerometer bias of 7.24 micro-g and a gyroscope drift of
0.0107 degrees per hour. **Instruments about thirty-one times better than the Atlas needed, in both
terms.**

The consequence is the one that actually shaped the arsenals. Carrying the cube-root yield scaling
through the same improvement gives

**a factor of 2.94 times ten to the fourth.**

A warhead delivered to a hundred and twenty metres does the work of one nearly thirty thousand times
larger delivered to two nautical miles. **That single ratio is why the arsenals grew more accurate
rather than larger**, and it makes the unglamorous engineering the article describes, the verniers
and the propellant utilisation system and the ground station full of computers, the part of the
programme that mattered. The conclusion now says so.

---

## Contemporary Coverage

An 84-query sweep returned **923 new records**, taking contemporary references from **23 to 158, or
41.4 percent of dated**, which sits inside the 101 to 189 absolute range the series has held since
A301 and above the 28 to 33 percent floor. The article entered this pass with the largest
contemporary gap any article in the series has carried into a final review, so the expansion was
correspondingly large.

Fourteen subsections replaced the previous seven paragraphs. The strongest are these.

**Geodesy is where the article's largest uncertainty went**, and the discipline that closed it is
unrecognisably larger than the primary references suggest. Satellite gravimetry became a mission
class, global geopotential models are now evaluated rather than derived, and the datum problem the
article identifies has become a routine national adjustment. **A targeting organisation in 1958 could
not know a target's coordinates to the tolerance its own guidance system met. That is no longer the
binding term anywhere.**

**Inertial navigation has returned the article's architectural question in the same terms.** The
Atlas put the measurement on the ground because the instrument was marginal. Instruments improved,
satellite navigation moved the measurement outside the vehicle, and the current literature is about
moving it back, because a signal from outside can be denied. **The Atlas could be denied by attacking
the ground station and a modern vehicle by attacking the signal**, so the question is open rather
than settled.

**The explosive bolts the Atlas B introduced are now the component the field most wants to replace.**
A mechanism chosen in 1958 for absolute reliability delivers a shock the payload must survive, and
the low-shock and non-pyrotechnic literature is an active line.

**SCORE was the first communications satellite and also the first deliberate orbital debris**, and
the modern literature treats those as the same fact. Its thirty-four day lifetime is now a casualty
risk calculation. **SCORE reentered over an empty world with nothing below it worth insuring, and
that assumption expired.**

**The four percent duty cycle was solved by quantity rather than by design.** The modern answer to
store and forward is not a better recorder but enough satellites that another one is always overhead,
which was unavailable to a programme that could fly ten vehicles.

**What killed the Atlas as a weapon is being solved for reasons that have nothing to do with
weapons.** The boil-off constraint that made it unable to stand alert is now a substantial research
programme, because a mission to Mars faces the same physics over years rather than days.

---

## Two Further Drift Cases, and Which Guard Caught Each

The URL-stability guard added during the primary pass **fired on the very next regeneration** and
caught a third case, in which an already-cited anchor had moved from a staging and range-safety paper
to one on liquid sloshing.

Two more were caught by the older link-text invariant instead, both in citations being added rather
than already present. **The two mechanisms are complementary and both are needed.** The URL guard
protects anchors the prose already uses by comparing against the reference section already in the
file. The link-text invariant protects anchors being added by comparing display strings. Neither
covers the other's case.

---

## Checks

**Two defects found and fixed on read-through.** The Epistemic State still carried a wording the body
had already corrected, and the conclusion still asserted the accelerometer claim the equation pass had
weakened. Both were repaired. Three further internal inconsistencies were closed, namely the
full-range flight date being flagged as disputed in one place and stated flatly in two others, and an
Out of Scope entry that contradicted a section the equation pass had added.

**Two NTRS identifiers timed out and both returned 200 on retry**, per the rule that a timeout is
retried before being recorded as a failure.

---

## Verification

**399 reference definitions, 387 external URLs, zero duplicates.** All 31 fixed identifiers at 200,
two after transient read timeouts. **All 352 DOIs Crossref-resolved on title at the 0.85 threshold
with zero flagged, and this article contains no hand-entered identifier anywhere.** All 176 worked
values re-derived independently and reproducing, including the modern accuracy chain. `_verify.py` at
the 0-error 21-warning corpus baseline. Zero contractions, em-dashes, en-dashes, prose colons, prose
semicolons, prose parentheticals, doubled words, duplicate headings, lone dollar-delimited lines, or
adjacent display-math seams. Genre section order correct with The Source Base immediately before the
Epistemic State. Isolated build succeeding with **137 rendered display blocks matching the source
count exactly**, Part 13 navigation, twelve tables, no unresolved reference links and no surviving
Liquid tags.

Citation construction mix healthy at a top bigram of 3.0 percent. `atlas` at 5.89 per thousand body
words is the subject noun and is reported rather than remediated, and it is the only word above
threshold.

---

## Final State

**1505 lines, 137 display equations, 399 references, 18,179 body words.**

**Lines are inside band at 1505 against 1300 to 1600.** Equations are seven above the 130 ceiling and
references nineteen above the 380 ceiling, both **reported rather than trimmed**. The standing
directive states there is no length limit and no reference limit and asks for a comprehensive survey,
and the genre rule is explicit that trimming to stay under a band is worse than reporting the
overrun. **Nothing was trimmed at any point in any of the four passes.**

Primary sources are 220 of 382, or 57.6 percent of dated. The absolute count is unchanged since the
primary pass and the percentage moved only because the contemporary additions grew the denominator,
which is the count-versus-percentage behaviour the series has seen repeatedly.

---

## State

**Pushed.** Nothing in this series is published, and the deploy workflow builds without `--drafts`,
so the push is safe. **The publication-order dependency is thirteen deep**, A309 back to A297.

Thirteen articles complete of seventy-two. **Categories remain undecided** at `aerospace history
engineering`, thirteen articles deep and raised seventeen times.

A310 is the Ryan X-13 Vertijet, which breaks the Atlas run entirely. It is a genuine research
aircraft again, the first since the X-7, a tail-sitting vertical take-off jet, and
its keystone is almost certainly the transition between hovering and wingborne flight rather than
anything to do with mass fraction or cutoff. **The A308 and A309 harvest will not help**, and the
harvest should be rebuilt from scratch against NTRS rather than the defence archive, since this is an
aircraft programme rather than a weapon system.
