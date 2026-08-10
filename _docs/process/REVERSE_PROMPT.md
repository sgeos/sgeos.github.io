# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A323 draft pass, the first of four. Committed. **Not pushed**, per the rhythm. **Not
published.** All twenty-seven articles in the series remain in `_drafts/`.

**Draft state 3,613 lines, 17 display equations, 2,016 references, 12,061 words.** Primary 64.7
percent, contemporary 25.2.

---

## One Airframe, Two Aircraft, and a Single Number

**The Schweizer SGS 2-32 is a 1962 club sailplane. The American military bought it twice, gave it the
same X-designation both times, and used it for purposes with nothing in common.**

As the **X-26A** it was flown unmodified at the Naval Test Pilot School to teach student test pilots
what adverse yaw feels like. As the **X-26B** it was the QT-2 Quiet Thruster, a silenced engine and a
slow-turning propeller on the same airframe, flown over the Mekong Delta at night in 1968 to watch the
ground without being heard.

**One programme wanted the aircraft's worst handling trait made as visible as possible. The other
wanted the aircraft made as close to absent as possible.** Both got what they wanted from the same
property.

    (L/D)_max = (1/2) sqrt( pi e A / C_D0 )

Read as a wing requirement it **demands a long slender wing**, and a long slender wing flown slowly is
what produces adverse yaw. Read through the power required it **demands very little power**, and an
engine barely working can be silenced.

**The article derives this connection and explicitly does not claim it as anyone's stated rationale.**
Nobody at Patuxent River chose the aircraft because its aspect ratio implied a low power requirement.
Each programme chose it for its own reason and the common cause is visible only in retrospect.

---

## The Teaching Argument, Made Quantitative

Adverse yaw is proportional to lift coefficient through the classical elliptic result, and a long span
rolls slowly because roll rate goes as speed over span. Taking the X-26A at 60 miles per hour against a
generic jet trainer at 300, **with every jet quantity assumed**:

| | X-26A | jet, assumed |
|---|---|---|
| Sideslip developed, deg | 6.2 | 1.4 |
| Time to 45 degrees of bank, s | 4.25 | 0.25 |

**Four and a half times as much sideslip, developing seventeen times slower**, for an observability
index of seventy-five. **Neither aircraft is worse behaved in any dimensionless sense.** The sailplane
runs the same physics slowly and at large amplitude, which is the whole pedagogical case as arithmetic.

---

## A Scaling Law That Was Wrong, and the Discrepancy That Caught It

The index written as a scaling disagreed with the worked cases by **exactly a factor of two**, which is
the standing hint that the checker is at fault. It was: the scaling omitted directional stiffness, and
two is the ratio of the two aircraft's assumed values.

**Corrected, the helix angle cancels out of the expression entirely**, so the comparison does not
depend on how powerful the ailerons are. That is not obvious and the verifier tests it as a property
over two thousand randomised helix-angle pairs.

---

## Where the Acoustics Is Exact and Where It Is Not

**Spherical spreading costs 6.02 decibels per doubling of slant range, exactly.** The Army asked for
inaudibility at 1,500 feet and the QT-2PC betrayed itself at 750, so **it missed its specification by
exactly one doubling**. That is a small miss for a first article and is why the line continued to the
Q-Star and the YO-3A.

**The detection-range table cannot be checked and the article says so.** The source level was
calibrated backwards out of the single reported detection distance, so the table reproduces that
distance **by construction rather than by prediction**. What it does yield is the sensitivity, and
that is the finding: **a five decibel change in night ambient moves the detection range by 78
percent**, so the aircraft's usable altitude was never a property of the aircraft alone.

**The tip-speed lever is far stronger than the shortfall needed**, at tens of decibels against six,
**which is why the interesting question is not how they made it quiet but what was still audible once
they had.**

---

## A Quoted Figure Reconciled Rather Than Dismissed

The best-glide relation disagreed with the quoted 55.9 miles per hour by 13 percent. The same sources
quote a wing loading of 6.0 pounds per square foot, which is about 1,080 pounds and not the 1,430 pound
gross. **At the matched weight the relation gives 54.7 against 55.9, agreement to two percent.** The
quoted performance is a one-pilot number and the discrepancy was in the reading.

**That is worth more than the glide-ratio check**, which lands within seven percent using two assumed
parameters and therefore demonstrates very little. The article says so.

---

## Method

**The keystone was thin for the fifth article running and for the usual reason.** Adverse yaw stood at
**seven** records until the queries were rewritten in the period's own vocabulary of aileron yawing
moment, lateral control research and rolling and yawing moments, at which point it reached **48**.

**Five homonym families were anticipated before writing rather than discovered afterwards**, including
**the warship in the aircraft's own name**, which is the first time the series has had a homonym inside
a designation. Also astronomical and Earth observation, epidemiological surveillance, electronic noise
which had to be filtered without taking the acoustic sense with it, and mechanical coupling.

**The cited set came back with a single contaminant**, which is by far the cleanest first pass this
series has had, and it is the direct payoff of anticipating rather than repairing.

**Reading the URL sweep still found one new family.** **Audiology**, where the acoustic reflex is a
contraction of the middle-ear muscles and acoustic impedance is a clinical measurement. Also the marine
propeller, which shares nearly every word with the aeronautical one. Thirty records dropped, rejection
list 605 to 637.

**Two inherited exemptions were withdrawn.** A322 admitted wind turbines and samaras because
autorotation is the windmill brake state. Neither is relevant to a fixed-wing acoustics article and
both are excluded again, which is the rule that a filter earned in one article is not automatically
valid in the next, applied in the other direction.

**My own scanner produced two more false-positive bugs**, matching `crop` inside **microphone** and
`tire` inside **entire**. That is four such bugs across two articles, all the same mistake, and the
lesson is now explicit: **word boundaries by default in every scanning pattern.**

---

## Verification

**Numerical.** 40 independent checks, none importing the calculation. The maximum lift-to-drag ratio is
found by **scanning the polar** rather than quoting the closed form, the decibel-per-doubling by
**bisection** rather than by evaluating a logarithm, the helix-angle cancellation as a **randomised
property**, and the acoustic calibration by inverting the round trip. **All pass, and every value was
required to appear in the draft text.**

**Build.** Twenty-seven article isolated build, all 17 equations rendering as display math, zero
mangled escapes, zero duplicates, Part 27 of 72.

**URLs.** 2,006 external links swept. **1,597 of 1,597 DOIs confirmed registered, zero unregistered,
and 409 of 409 non-DOI links at 200 with no exceptions**, which is the first sweep in the series with
nothing at all to report.

**Corpus.** `_verify.py` at 0 errors and 21 warnings. Style and integrity clean across all
twenty-seven articles.

---

## Open Questions the Article Declines to Answer

**Three of the four X-26A airframes were lost and replaced.** A docile sailplane operated by
professional test pilots should not have that record. **The article states this as an open question
rather than reaching for the plausible inference** that an aircraft used to demonstrate departures will
occasionally depart.

---

## State

**A323 has one of four passes complete. Committed, not pushed, not published.**

Twenty-seven of seventy-two. The publication-order dependency is twenty-seven deep.

**Expected next is the equation-density review.** At 17 equations this is the lowest count of any
full-aircraft article in the series so far, and the acoustics side in particular names several
relations it does not display.

**Still open and unchanged.** The fourth genre class, now **fifteen** consecutive articles. The A305
length offer.
