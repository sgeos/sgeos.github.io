# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-10
**Task**: A328 equation-density review, the second of four passes. Committed, **not pushed**,
**not published**.

**State: 4,978 lines, 55 display equations, 1,054 reference definitions, 25,489 words**, from
4,825 lines and 35 equations after the draft pass. References were held and measured before and
after. All thirty-two articles in the series remain in `_drafts/`.

---

## Two Additions Changed What the Article Concludes

**An equation pass usually displays what the prose already said. Two of these did not.**

**THE HEADLINE RESULT SITS ON A KNIFE EDGE.** The draft established that between 81.9 and 93.6
percent of the aircraft's simulated losses fell in the two conditions where it was behind. Solving
the same identity for the share that would drive the pooled ratio to **parity** rather than to the
published 1.83 gives

    w = (8.5 - 1) / (8.5 - 0.36) = 0.9214

and **that threshold lies inside the bracket.** The published figures are therefore consistent with
weight distributions that produce an overall advantage and with distributions that produce an
overall disadvantage, and they do not distinguish between them. **The claim of an overall advantage
is not robust to a quantity the programme never published.** The flight testing is what settles the
question, and it settles it conditionally, which is what the arithmetic predicts.

**AT SEVENTY DEGREES A ROLL ABOUT THE VELOCITY VECTOR IS 94.0 PERCENT YAW RATE.** Writing the
kinematics down explains a sentence in the programme's own conclusions that otherwise reads as a
correction of itself, where the main advantage is called an apparent directional nose-pointing rate
which is, in actuality, yaw rate. **At seventy degrees those are the same manoeuvre**, and the axis
that has to supply it is exactly the one whose aerodynamic control has been lost and whose vectored
control the paddles restore. The article asserted the equivalence and did not have the relation
that makes it true.

---

## What Else Was Added

The atmosphere ratios and the speed of sound, which every altitude-dependent result rests on and
none of which appeared. The thrust-lapse model, carried as a sentence only. The true-against-
equivalent airspeed conversion, with **both routes required to return the same 633.4 pounds per
square foot** as a check. The load factor from lift and the level-flight speed, which are the
post-stall table's own columns. The canard contribution, quoted as a bare 0.313. The decibel
definition for a table column that had none. The impact-pressure relation the iced probe corrupted,
whose ratio between 170 and 48 knots is **12.735** and independently reproduces the 12.543
loop-gain factor. The asymmetry expressed as a moment, **32,863 foot-pounds at the measured bound
and 67,780 at the worst swing**. The separability test and the split relation. The counted rates,
including **4.06 scored engagements per sortie**, which is the direct product of real-time kill
determination. The flight tempo. The Pinball campaign ratios, where the offensive condition
reproduces to **4.3 percent** while slow-speed line abreast differs by **2.999**, so the campaigns
agree far better in aggregate than anywhere in particular.

---

## One Error in My Own Edit

**The asymmetry moment was written as 1,452 foot-pounds per hundredth of coefficient against a true
4,108**, a factor of 2.8 wrong in a line introduced specifically to make a quantity concrete. It
was caught by recomputing before committing rather than by any check, which is the argument for
recomputing every number an edit introduces even when the edit exists only to display a relation
that was already correct.

---

## The Keystone Is an Experimental Design, Which Is New in This Series

**Every previous article asked what a number was. This one asks whether an advantage exists.** The
X-1 measured a drag rise, the X-15 measured heating, the X-29 measured a divergence boundary. Each
of those is a quantity with units and an instrument can be pointed at it.

**The X-31's question has no units**, so the only instrument available was a designed sequence of
adversarial engagements with an outcome recorded for each. That makes the aircraft the first in the
series whose keystone is an experimental design, and it changes what the programme had to get
right. A badly chosen starting condition gives a wrong answer about whether a class of aeroplane is
worth building.

---

## The Central Result Is Arithmetic on Published Numbers and It Contradicts the Reputation

**A pooled exchange ratio is not the average of the per-condition ratios.** It is the ratio of sums,
which makes it the mean of those ratios **weighted by the losses of the denominator side**, so a
condition in which the aircraft was shot down fourteen times counts fourteen times as heavily as
one in which it was shot down once.

**The published overall figure of 1.83 therefore sits 3.514 times below the 6.43 average of the
four conditions it summarises.** A reader who computes the average from the table and a reader who
takes the published overall come away with completely different impressions of the same experiment.

**Inverting that identity brackets the weights.** Between **81.9 and 93.6 percent** of the
aircraft's simulated losses must have fallen in the two starting conditions where it was behind.
**That bracket owes nothing to any model.** It assumes no counts, no engagement totals and nothing
about the aeroplane, and Monte Carlo over 26,971 feasible weight vectors reproduces it at 0.8198 to
0.9356.

**The aircraft loses in two of the four conditions**, at 0.36 defensive and 0.86 high-speed line
abreast. The popular account does not mention that.

---

## Two of the Four Conditions Could Not Have Settled Anything

**A ratio estimated from a finite number of engagements carries an interval, and the programme
never published one.** At twelve scored outcomes per condition the defensive result does not
separate from parity. The high-speed line-abreast ratio of 0.86 sits so close to parity that it
would need **691 scored outcomes** to separate, against a few dozen flown, while the slow-speed
line-abreast 16 needs only six.

**The programme reached the correct flight-test priority order by judgement**, putting slow-speed
line abreast first and high-speed line abreast third, from an analysis of which conditions showed
the largest difference rather than from any consideration of statistical power.

---

## Two Published Reports Were Never Compared and Their Comparison Reproduces the Departures

The programme reported that departures at 58 degrees of angle of attack were caused by yawing-moment
asymmetries that overcame the vectoring authority. A different report measured those asymmetries at
a coefficient of 0.080, reaching 0.100 with transition strips and swinging by **0.165 across three
degrees** in the worst case.

**Setting one equal to the other determines the moment arm, which is not published anywhere.** It
returns **16.22 feet**, placing the centre of gravity at **60.1 percent** of fuselage length, which
is exactly where a canard delta's belongs. The inversion could have returned an arm longer than the
aeroplane and did not, so it is a check rather than a fit.

---

## An Effect the Flight-Test Report Describes in Words Is Computable in One Line

The report notes that the traditional build-up approach fails when control power comes from the
engine, and that manoeuvres impossible at thirty thousand feet became possible at twenty.

**Aerodynamic authority is fixed at constant calibrated airspeed while vectored authority follows
thrust**, so the vectored share falls with altitude for no change of speed whatever. The ratio is
**0.6462 between thirty and twenty thousand feet, a loss of 35.4 percent.** The test team found the
answer empirically because nobody had written the ratio down.

---

## The Accident Is Now Quantified, and the Redundancy Needed Was Free

**Loop gain scales with the ratio of true to indicated dynamic pressure, which is the square of the
airspeed ratio.** With the indicated airspeed between 48 and 100 knots against a true 170, the loop
stood at **2.890 to 12.543 times design** against a conventional gain-margin factor of 1.995. Even
the least severe reading exceeded the entire margin.

**The failure was detectable from information already displayed.** Angle of attack and airspeed are
redundant through the lift equation, and the two readings the pilot called out disagreed by **11.2
degrees**. Expressed as dynamic pressure that is a factor of **2.266, which had already exceeded the
design gain margin at the moment he spoke.** A second probe would have been heavier. A comparison of
two signals the aircraft already had would have weighed nothing.

---

## The Advantage Is Not What the Summaries Say

**It is not a smaller turn radius.** Every radius computed at seventy degrees of angle of attack
exceeds the 1,171 feet available at corner speed, and below 138 knots the manoeuvre is a descending
transient rather than a turn.

**It is forty degrees of aim-off angle**, which is the difference between a thirty-degree
conventional limit and a seventy-degree demonstrated one, and which a conventional aircraft can buy
only by turning its velocity vector through the same angle, taking **1.41 to 3.13 seconds**
depending on where in the envelope the fight is.

**It costs 4,600 feet of specific energy and 44.7 seconds to repay**, integrated rather than
estimated, against a single-point estimate that would have said 507 seconds. Forty-five seconds is
the whole engagement, which is the quantitative form of the programme's own conclusion that the
technique works only when used selectively.

---

## Four Errors in My Own Work, All Caught Before Writing

**The integer reconstruction bounded both counts by the same number.** A ratio of sixteen to one
with three losses on the denominator needs forty-eight on the numerator, so a common bound of forty
silently forbade every large-denominator realisation. One published set then reported three
solutions and another reported none, and **both figures were facts about the bound rather than
about the data**. The article now rests on the weighting identity, which needs no counts at all.

**The rounding tolerance was keyed off magnitude rather than printed precision**, treating a figure
written "2.8" as though it had been printed to two decimals, which drove one published set to zero
solutions.

**The lift curve was extrapolated linearly to seventy degrees**, returning 3.38, roughly twice any
lift coefficient a delta of this aspect ratio has produced.

**The theory comparison used the unswept slope and explained the disagreement by appealing to the
canard, which is backwards.** A canard in trim raises the whole-aircraft slope and sweep lowers it.
**The corrected comparison is stronger than the original**, with the inferred 2.769 per radian
sitting between a swept 2.278 and an unswept 3.027.

---

## The Word-Boundary Family Returned in Two New Variants

**Twenty alternation groups closed with a boundary after a stem or a singular**, so a pattern
reading "agility followed by metric or measure" failed on the phrase "agility metrics", because the
boundary after "metric" requires a non-word character and "s" is not one.

**Titles use hyphens where the patterns used spaces.** A paper titled "High Angle-of-Attack
Aerodynamics" fell through to the no-cluster pile, as did "Flush Air-Data Sensing System".

**Both were found by reading a random sample of the discarded records rather than by inspecting the
patterns**, which is the only method that has ever worked for this class of defect.

---

## A New Variant of the Thin-Heading Rule, and a Whole Literature Missed

**Thirteen cluster-and-era pairs came up short of what the draft cites and twelve were the modern
half.** The cause was not a thin heading and not a thin subject. **The era was thin**, because the
harvests asked the modern pool only for the obviously modern subjects and asked the period pool for
everything else, so the contemporary literature on subjects that existed in 1993 and still exist
was never requested. A harvest written against that diagnosis moved the modern pool from 1,316
records to 4,947.

**Separately, two harvests filtered Crossref to journal articles and this aircraft did not publish
in journals.** It published at meetings of the American Institute of Aeronautics and Astronautics
and the Society of Experimental Test Pilots. The vehicle cluster stood at eighteen while the two
most important papers about the programme sat in the registry unqueried. Dropping the filter added
**638 conference records**.

---

## A Flight Log Was Parsed for Distributions Nobody Published

The published record gives 580 flights. **The per-flight log in the history's appendix gives the
distributions**, and parsing it recovers 578 of the published 580 with three sequence numbers
unrecovered, which accounts for the difference.

**The eighty-four-day stand-down after the accident falls out of the arithmetic rather than out of
the narrative**, dating the programme's recovery to within a day.

---

## Verification

**107 of 107 independent checks passing, none importing the calculation.** The tipping weight is
reached by bisection on the pooled value rather than in closed form and is asserted to lie inside
the bracket. The wind-axis shares are checked by rotating a vector. The impact pressure is inverted
for speed as well as evaluated forward. The aggregation identity is
tested as a randomised property over 20,000 count vectors, the weight bracket by Monte Carlo against
the analytic extremes, the binomial endpoints by evaluating the tail rather than repeating the
bisection, corner speed by scanning the load-factor curve, the moment arm by bisection, the energy
recovery by integrating forward in time against integration over speed, the eigenvalue by simulating
the divergence, and the rate limit by generating the sinusoid and differencing it.

`_verify.py` at the 21-warning baseline with zero errors, check_any clean after removing a
contraction inside a quoted radio call, `_lib/test_lib.py` at 46 of 46, and reference integrity at
1,054 with zero undefined and zero orphaned anchors.

**The reference set swept with zero hard failures** across all 50 NTRS identifiers, 240 of 811
sampled journal DOIs, 80 of 121 sampled DTIC DOIs, all 15 books and all 25 curated URLs, after
replacing two dead Wikipedia targets.

**A 32-article isolated build renders the page at 16 sections, 88 subsections, 21 tables and all 55
equations.**

---

## For the Reference Pass

**20 displayed equations have no nearby citation**, and that is the next pass's material.

**The equation pass promoted subjects again, which is now eleven articles running.** The relations
added here reach into the standard atmosphere, engine thrust lapse, airspeed-system instrumentation,
inference on rates from small samples, and flight-dynamics kinematics. None of those was a heading
the original harvest was written for.

---

## Awaiting Instruction

**A328 has completed the draft and equation passes.** Thirty-two of seventy-two drafted, **none
published**.

The next pass is the primary-reference review.
