# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-05
**Task**: A305 equation-density review, the second pass. Committed. Not pushed, per the convention
for passes that do not ask for it. Not published. All nine articles remain in `_drafts/`.

---

## The Pass Paid for Itself Immediately

Baseline was 136 display equations. Auditing for relations the prose names, relies on, or whose
product it quotes found **25 such relations absent**, and writing the first of them down found that
three numbers the draft had quoted were wrong.

The article stated thrust coefficients of 1.55 in vacuum and 1.36 at sea level, and a theoretical
characteristic velocity of 1,570 metres per second. Computed from the area relation and the flow
factor they are **1.624, 1.409, and 1,505**. I had taken all three from secondary compilations rather
than deriving them, which is the same class of error as taking an author's name from a title.

The corrected chain is better than merely correct. Because the sea-level thrust coefficient cannot be
stated independently of the chamber pressure, the two must be solved together, and doing so recovers a
chamber pressure of 2.16 megapascals. Carrying that back to vacuum gives 4,727 pounds of thrust
against a **separately reported 4,728**, which is an independent check the original arithmetic did not
have and could not have had. Three downstream figures were corrected, including in the Epistemic
State.

---

## The Stability Analysis Now Predicts What the Flight Record Blames on It

The draft explained the 24 November 1947 failure, in which the tail yawed for 35 seconds before the
flight was terminated, as "the failure mode the stability analysis above predicts". **The analysis did
not predict it**, because I had computed a natural frequency without ever writing the equation of
motion it solves.

Writing it down gives two results the article needed. The damping ratio at tower exit is 0.0033, which
is 33 cycles to halve an oscillation, or about three minutes against a 42 second burn, so **an
unguided finned rocket does not damp its pitch motion aerodynamically in any useful sense**. What
suppresses the motion is rising dynamic pressure and roll averaging, not damping, and the damping
ratio gets worse with altitude as the square root of density. And a statically unstable vehicle of
this size has a divergence time constant of 0.86 seconds, so a flight that yawed for 35 seconds ran
for forty time constants and was not marginally unstable.

---

## Three Further Results Worth Having

**Wind weighting, derived rather than named.** Integrating the weathercock tilt over the burn gives a
lateral velocity of the wind times the logarithm of the velocity ratio. A ten metre per second wind
therefore moves the impact point **seven kilometres**. That single number justifies the adjustable
tower, the three-degree cant, and the choice of deserts, none of which the draft had quantified.

**Containment, corrected.** The draft quoted a three-sigma radius as though the error were
one-dimensional. In two dimensions the Rayleigh containment gives 0.989 at three sigma, not 0.997, and
reaching 0.997 needs 3.41 sigma. The required impact radius is 6.8 kilometres rather than 6.

**Coning, which settles the pointing argument.** A slender body has a transverse-to-roll inertia ratio
near 300, so a residual transverse rate of a tenth of a radian per second at burnout swings the
instrument axis through a **64 degree cone** for the whole observing window. That is a consequence of
slenderness rather than of workmanship, and it is much the strongest support for the article's claim
that the era's science was limited by pointing rather than by altitude.

Six measurement methods the article named and relied on had no relations at all, and now have them,
namely two-frequency differential Doppler for electron density, the eddy-against-molecular diffusivity
criterion that locates the turbopause near 107 kilometres, Poisson counting statistics giving a 150
second exposure for a five-sigma X-ray detection, the Snell invariant for acoustic sound ranging, the
Rayleigh cross-section for searchlight densitometry, and the slant-path secant that makes observing
geometry part of the altitude requirement.

---

## Verification

All 64 new worked values re-derived independently, with one correction, being an exposure time for a
ten-times-fainter source stated as 15,000 seconds against 12,750. Every previously verified value
re-checked and still reproducing. Zero lone dollar-delimited lines that would render inline, zero
blank-line seam defects, and **200 rendered display blocks confirmed in the built HTML against 200 in
the source**.

The seam scan caught one duplicated clause in text I had just inserted, where the aspect-cone addition
said the sign ambiguity is resolved by continuity immediately before an existing sentence saying the
same thing. **That is the fourth occurrence of this defect class in the series and it was again found
by reading rather than by any check aimed at it.**

`_verify.py` at the 0-error 21-warning corpus baseline. Zero style violations. Isolated build
succeeding with Part 9 navigation and no unresolved references.

---

## The Count Is the Highest in the Series and I Did Not Trim It

2007 lines, **200 display equations**, 370 references, 18,655 words. The equation ceiling is 130 and
the opener A297 holds the previous high at 147.

Every one of the 64 additions is a relation the prose already names, relies on, or whose product it
quotes, so the rule that produces the number was followed rather than the number targeted. I have not
proposed changing the genre band, because A303 and A304 sat at 92 and 94 and one outlier is not
evidence. The subject is the reason: this article carries propulsion, flight dynamics, structures,
heating, telemetry, and six separate measurement techniques, where a typical article in the series
carries three or four of those.

**If you would rather the article were shorter, the place to cut is the measurement-method relations
in What the Data Changed**, which are the least load-bearing of the additions. Say so and I will
remove them.

---

## Prior State, Carried Forward

The draft pass is described below and remains accurate except for the metrics, which the equation pass
superseded.

---

## The Keystone, Which Is Specific to This Article

Every previous vehicle in this series was the object of its own measurement. The X-1 was instrumented
to find out what happened to the X-1. Even the expendable X-7 was flying to characterise the ramjet
bolted underneath it.

**The X-8 is the first X-vehicle whose own performance is not what is being measured.** It is
apparatus rather than subject, and the design requirement that follows is transparency, meaning that
every way in which the carrier might perturb somebody else's instrument becomes a constraint. That
gives six requirements, being altitude set by the physics of the phenomenon, observing time, pointing
knowledge, non-contamination, data return, and repeatability, and the trades between them are the
article.

The central relation is clean enough to be worth stating here. Observing time above burnout altitude
is exactly twice the burnout velocity divided by gravity, so combined with the rocket equation it is
the exhaust velocity times the log of the mass ratio, divided by half g. With the Aerobee's
propellants that is **400 seconds of observation per factor of e in mass ratio**. Doubling the
observing time squares the mass ratio. **This is the quantitative reason a sounding-rocket programme
buys precision by flying often rather than by flying high**, and it is the article's answer to why
five minutes was enough to discover Scorpius X-1.

---

## The Published Figures Do Not Close, and the Article Says So

A staged trajectory reconstruction reproduces the reported burnout velocity of 1,347 metres per second
to within 2 percent. It then leaves **26 metres per second for drag, against an independent drag-loss
estimate of 60 to 150**. One or more of the booster inert mass, the sustainer burn time, and the
specific impulse is off by a few percent in a compensating direction, and no source consulted settles
which.

I have shown both numbers rather than tuning an assumption until the residual looked right. The
reconstruction is worth trusting to the extent it is because of an independent check that fell out of
it, namely that the implied sustainer stage mass of 498 kilogrammes matches the separately reported
1,100 pounds without being fitted to it.

Six further items are recorded in the Epistemic State as unsettled, including the date the X-8
designation was applied, which one source gives as 1955 and another as 1949; the relationship between
X-8 and RM-84, where two sources cannot both be right; the flown-against-delivered counts, which
differ by seven; and whether any fragments from the 1957 shaped-charge flight reached escape velocity,
where Zwicky's contemporary claim and McDowell's later analysis disagree and the article takes no
position.

---

## Three Results the Sources Do Not State

**Roll resonance is unavoidable in general.** Roll rate from canted fins and pitch natural frequency
are both linear in velocity, so velocity cancels from their ratio, which then varies as the inverse
square root of density alone. A vehicle starting below resonance therefore crosses it at a definite
altitude regardless of how fast it is going, and no amount of thrust avoids the crossing. At half a
degree of cant this vehicle never crosses; at a tenth of a degree it crosses near 6 kilometres, inside
the sustainer burn.

**Blowing the fins off is worth a factor of sixty.** Tumbling cuts the ballistic coefficient from 8,180
to 129 kilogrammes per square metre, so the dynamic pressure at parachute deployment falls by the same
factor. That is the whole justification for a technique that looks like damage, and the sources record
the practice without giving the reason.

**A photographic frame is not telemeterable.** One 35 millimetre frame carries roughly 52 megabits
against a six-channel link delivering 4.2 kilobits per second, so transmitting it would take 3.4 hours
against an eight-minute flight. This is why the parachute failures on the first five Air Force flights
destroyed the science rather than degrading it, and it is the sharpest illustration in the article of
the difference between a vehicle that is its own experiment and one carrying somebody else's.

---

## Defects Found, and How

**Twenty author keys guessed from document titles were all wrong.** Every one. A further 23 guessed
during the citation pass were caught before that pass ran rather than after. This is the fourth
article in which inferring an author from a title has produced bad citations, and it now seems fair to
say the practice has no success rate at all rather than a poor one.

**Three mis-citations were found by reading the reference list, not by any check aimed at them.** Two
disambiguation tags were assigned to the wrong member of their pair, so both the displayed text and
the surrounding prose description pointed at the other paper. A third citation, introduced as an
injector-design review, resolved to a paper on thermosphere density prediction. All three would have
survived every automated check I ran. A link-text invariant now enforces that each prose citation's
text equals the master-table display for its anchor, and enforcing it resynchronised 53 further link
texts that an earlier case normalisation had left stale.

**The seam scan caught a duplicated passage and a repeated citation.** The Comparison With Ground
Prediction section restated the Programme Origin passage almost verbatim, and an anchor correction had
produced the same citation twice in one clause.

**One flagged value was the check being wrong rather than the article.** The roll-resonance crossing
altitude failed at 20.6 percent against an exponential atmosphere of a single scale height.
Recomputing against the US Standard Atmosphere puts it between 6.0 and 6.5 kilometres, confirming the
article.

---

## A Decision I Made Without Asking

**Contemporary coverage was raised during the draft pass rather than left for the publication review.**
The draft closed at 25 contemporary references, or 11.4 percent of dated, well below the 28 to 33
percent floor the series has settled at. Since the standing directive governs every pass and the
harvest was already in hand, deferring a known deficit through two more passes seemed worse than
closing it. 87 journal articles were added, taking contemporary references to **112 and 36.6 percent**,
an absolute count consistent with A301 at 101, A302 at 109, A303 at 105, and A304 at 107. Two new
subsections came with them, on the motor such a vehicle would use today and on what a flight costs.

If you would rather the four passes stayed strictly separated, say so and I will leave the later
articles thin at the draft stage.

---

## Verification

**All 89 worked numerical values re-derived independently from their stated inputs.** Two corrections.
A signal-to-noise ratio was inflated 10 percent by a rounding carried through the link budget, and a
lumped skin temperature was stated 14 kelvin low.

370 references with zero undefined, zero orphaned, and zero duplicate URLs. All 147 fixed identifiers
at 200. All 170 DOIs Crossref-resolved on title at the 0.85 threshold with zero flagged. The one
hand-entered DOI, Shannon 1948, was verified individually and printed in full rather than trusted,
because it did not come from a harvest record. `_verify.py` at the 0-error 21-warning corpus baseline
with no new warning. Zero contractions, em-dashes, en-dashes, prose colons, prose semicolons, or prose
parentheticals. Zero doubled words, zero display-math seam defects. Isolated production build
succeeding with 136 rendered display blocks, Part 9 navigation, no unresolved reference links, and no
surviving Liquid tags.

**Two densities are over band and it is deliberate.** 1746 lines against a ceiling of 1600, and 136
display equations against 130. References at 370 are inside. Reported rather than trimmed, under the
directive stating no length limit.

---

## State

**Committed, not pushed.** The draft pass does not push, per the established rhythm. Nothing in this
series is published.

Nine articles complete of seventy-two. **The publication-order dependency is now nine deep**, A305
back to A297, through `post_url`.

**Categories remain undecided** at `aerospace history engineering`, now nine articles deep and raised
seven times. It fixes 72 URLs permanently at publication and remains reversible with one edit until
the first article publishes. I have proceeded on the assumption rather than blocking.

A306 is the Bell X-9 Shrike, which returns the series to a vehicle that is genuinely a missile
testbed, and which will need the designation question this article opens to stay open rather than be
answered early.
