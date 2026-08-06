# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-06
**Task**: A306 primary-reference review, the third pass. Committed. Not pushed. Not published. All ten
articles remain in `_drafts/`.

---

## The Baseline Was Already the Highest in the Series

Primary technical documents measured **125 of 229 external references, or 54.6 percent**, before this
pass, against A298 at 52.1 and A305 at 51.4 after their own reviews. So the count was not the problem.

The deficit was coverage, and it was concentrated in one place. **The equation pass created the same
reference debt it created in A305.** Every relation added last week arrived without its period source,
so the supplementary harvest was aimed at those topics rather than at the article's original ones.

39 primary documents added across 12 edits. Primary is now **164 of 268 external, or 61.2 percent**,
and references went from 239 to 278, which brings the last of the three densities inside band.

---

## What the Equation Pass Owed

Blast scaling, which turns the asserted lethal radius into a statement about yield, now has [Morton
1966] on scaling air blast against real targets. The drag buildup's flat-plate friction coefficient,
which the article had simply stated as 0.0025, now has [Dhawan 1953] measuring it directly and
[Rubesin et al 1951] supplying the compressibility correction, with the roughness dependence that
makes a real missile worse than a plate.

**The beacon argument is the article's strongest single claim and it had no source at all.** That a
one watt transmitter on the missile beats a hundred kilowatt radar on the aircraft now rests on
[Feldman et al 1962] on beacon system evaluation and improvement, including the decoder that lets the
same link carry commands.

The bomber's turn radius now has [Wrestler 1965] on aircraft agility in the turnaround manoeuvre. The
hinge-moment balance argument now traces to [Harris 1935], and the actuator that supplies what balance
does not remove is [Scott 1966]. The gyro bias that maps straight onto the error budget now has
[Vaughn 1960] on test methods and [Flowe and Bright 1963] on drift.

---

## Two Gaps the Draft Left

**The operator's display is a component of the loop and the article had treated it as furniture.** The
operator can only close a loop around what he can see, so the console engineering of [Fluhr 1963],
[Mitchell and Kinney 1966], and [Drake 1967] belongs in the argument, as does the radar-presentation
interpretation problem of [Esten 1953], since relief displacement and parallax are what a radar
picture of a ground scene actually shows an operator.

**Three X-9 flights carried a warhead and the article mentioned it without a source.** Now sourced
across warhead development and fuzing for guided missiles of the period.

---

## A Housekeeping Defect Worth Recording

Nine reference entries carried machine-generated corporate author names, such as `Army Missile Command
Redstone Arsenal Al 1963` and `Bell Aerospace Co Buffalo Ny 1953`. The harvest produces these from the
defence archive's corporate-author field, which is a place name and an organisation rather than a
person, and my author-key derivation had no way to know that.

All nine are shortened in the master table, and the link-text invariant resynchronised them into the
prose automatically. **This will recur on every article that draws on that archive**, so it is worth
handling at harvest time rather than at review time in future.

---

## Verification

278 references with zero undefined, zero orphaned, and zero duplicate URLs. All 77 fixed identifiers
at 200. **All 156 DOIs Crossref-resolved on title at the 0.85 threshold with zero flagged, and this
article contains no hand-entered identifiers at all.** All 89 worked values still reproducing.
`_verify.py` at the 0-error 21-warning corpus baseline. Zero style violations, zero duplicate
headings, zero display-string collisions, zero link texts out of sync. Isolated build succeeding with
115 rendered display blocks and Part 10 navigation.

---

## State, and the One Remaining Deficit

1414 lines, 115 display equations, 278 references, 12,731 words. **All three densities are inside
band**, which is the first article in the series to arrive there without an overage being argued for
since A304.

**Contemporary coverage is the deficit.** 46 references at 19.2 percent of dated, against absolute
counts of 101 to 155 in A301 through A305. The percentage fell from 22.9 only because the denominator
grew, but the count is what the series tracks and 46 is low. The publication review will need to add
roughly a hundred, and the harvest already holds 349 modern records of which only 46 are cited.

Committed, not pushed. Publication-order dependency ten deep. Categories still undecided at
`aerospace history engineering`, raised nine times.

---

## Prior State, Carried Forward

The draft and equation passes are described below and remain accurate except for the metrics.

---

## The Audit Found a Structural Defect Before It Found an Equation

I began by counting equations per section, which is the usual first move, and the count exposed
something else. **Four orphaned subsections sat at the end of The Contemporary Literature**, three of
them duplicating headings the draft expansion had already written properly and one an unfilled stub.

The cause is mechanical and worth recording. During the draft pass I replaced a block of five stub
headings with a written section, but my replacement matched only the first heading and the paragraph
under it, so the other four stubs survived below the new material. **Every automated check passed
this.** The reference generator was happy, the build was clean, the style scan was clean, and the
article rendered with three headings appearing twice.

The three duplicates are removed. The fourth stub, on circular-error estimation, is now written, and
writing it produced a finding rather than filler, which is that the estimators of the early 1960s are
still the estimators and the modern effort has gone into predicting trajectories well enough that a
sample is not needed.

---

## Writing a Relation Down Exposed an Error in the Draft's Reasoning

The draft said the residual miss decays as $f(t_{go}/\tau_g, N)$ and never gave $f$. Giving it showed
the draft's own conclusion to be wrong.

I had asserted that eight guidance time constants reduce an error by more than two orders of
magnitude. That is the behaviour of the bare exponential. The full expression carries a polynomial
factor, which at eight time constants is $8^{3}/3! = 85$, so the residual is **three percent rather
than three parts in a thousand**, and three time constants leave twenty-two percent rather than more
than half. Both statements are corrected.

**This is the second article running in which the equation pass caught arithmetic the draft had
carried as an assertion**, and in both cases the error was in a quantity I had reasoned about
qualitatively instead of computing.

---

## What Else Was Added

27 equations across 12 edits, taking the article from 88 to 115.

**Proportional navigation itself**, which the article had been naming for several sections without
ever writing. Giving it in its line-of-sight-rate form makes the point the prose was gesturing at,
which is that a zero line-of-sight rate is the condition for a collision, so the law drives the
geometry toward an intercept without ever computing where the intercept will be.

**Cube-root yield scaling**, which turns the article's asserted 1,500 metre lethal radius into a
statement about a weapon of roughly 600 kilotonnes and shows that every factor of eight in yield
doubles the tolerable circular error. That is the arithmetic behind accuracy and yield being
substitutes, and the founding irony needed it.

**The bomber's turn radius**, 5.1 kilometres at 1.5 g with a 68 second reversal, which makes the
launch aircraft's commitment concrete rather than rhetorical. **The first bending frequency**, 19
hertz against a 7.5 radian per second rigid-body mode, which is the number the autopilot gain limit
was referencing. **A zero-lift drag buildup** replacing an assumed coefficient, which splits half to
friction and half to compressibility. And **the beam-rider error**, which completes the
three-architecture comparison the period sources make qualitatively.

---

## Verification

All 27 new worked values re-derived independently, with the one correction above. Every previously
verified value still reproducing. Zero lone dollar-delimited lines, zero blank-line seam defects, and
**115 rendered display blocks confirmed in the built HTML against 115 in the source**. Two
paragraph-level repeated citations introduced by the bending-frequency addition were caught and
removed. Zero duplicate headings now. `_verify.py` at the 0-error 21-warning corpus baseline.

---

## State

1336 lines, 115 display equations, 239 references, 12,337 words. **Lines and equations are now inside
band. References remain 11 short of the 250 floor**, which the primary-reference pass will close
without difficulty given that 125 primary documents are already cited and the harvest holds 177
unused pre-1975 records.

Committed, not pushed. Publication-order dependency ten deep. Categories still undecided at
`aerospace history engineering`, raised nine times.

---

## Prior State, Carried Forward

The draft pass is described below and remains accurate except for the metrics.

---

## The Keystone

Every vehicle in this series so far has had a keystone that is ultimately physical. Transonic drag
rise, aeroelastic divergence, shielding mass, ramjet combustion, atmospheric optical depth. Each is a
question about the behaviour of matter.

**The X-9's binding unknown is a control loop, and its specification is a probability.** The military
characteristics of 15 July 1945 asked for a missile that would strike within 500 feet of its target 75
percent of the time. Read as a Rayleigh distribution that is an axis standard deviation of 91.5 metres
and a circular error probable of **108 metres at a hundred miles**. Every subsystem is then specified
in metres of miss distance, contributions add in quadrature, and the design activity is the allocation
of that budget rather than the pursuit of a performance figure.

The contrast with the article before it is the cleanest in the series so far. **The X-8 had to bring
data back. The X-9 had to take a command out.**

---

## The Central Technical Claim

A radar resolves an angle, so its cross-range position error is proportional to range. That single
fact cuts in opposite directions depending on which end of the engagement the radar sits at.

Guiding from the launch aircraft makes the error grow with the standoff distance the weapon exists to
buy. Guiding from the missile makes it shrink throughout the approach. **The two architectures have
opposite error gradients**, and setting the launcher-guided resolution equal to the whole error budget
gives a maximum useful range of about 72 kilometres against the X-9's demonstrated 80. That
correspondence is close enough to state and too loose to press, and the Epistemic State says so.

It is also why the operational weapon was named for its guidance link rather than its warhead or its
airframe. RASCAL stands for radar scanning link, and the link carried a radar picture from the missile
back to an operator in the launch aircraft. **The sensor rode the missile and the judgement stayed
behind.**

---

## The Founding Irony Is Datable

The accuracy requirement was published on **15 July 1945. Trinity was fired on 16 July.**

Inverting the damage function shows what that timing cost. A nuclear warhead with a 1,500 metre lethal
radius needs a circular error probable of 823 metres for a 90 percent kill probability, against the
108 metres the specification demanded. **The requirement was about eight times tighter than the weapon
that eventually flew actually needed**, because it was written for a conventional warhead one day
before anyone knew the other kind worked.

That does not make the X-9 pointless. It relocates its value, since the accuracy work was largely
surplus to the nuclear mission and directly applicable to everything after it, while the reliability,
the launch procedures, and the trained crews were not surplus at all.

---

## Three Results the Sources Do Not State

**The operator cannot be given the control surfaces.** The airframe's short-period frequency is 7.5
radians per second against a human operator's maximum crossover of 2.6, so the missile is three times
faster than the man flying it. An inner autopilot loop is forced by two time constants rather than
chosen by preference.

**Only terminal errors matter.** A guidance time constant of 0.83 seconds, summing the operator, the
autopilot, and the airframe, means the loop needs about eight seconds of flight remaining to null an
error, which at Mach 2 is five kilometres. Every error still present inside that radius arrives at the
target, which reorganises the whole budget.

**A one watt transmitter on the missile is worth more than a hundred kilowatts on the aircraft.**
Replacing the fourth-power skin-return law with the beacon's second-power law is worth a factor near
10 to the 5 at eighty kilometres, and it is the single most consequential decision in a
command-guidance system.

---

## A Rule That Finally Cost Nothing

**No author key was guessed from a document title in this article.** I resolved the anchor index from
harvest metadata before drafting rather than after, and every one of the 239 anchors landed correctly
on the first attempt.

That defect cost twenty corrections in A305 and appeared in three articles before it. The remedy turns
out to be ordering rather than care, which is worth recording as a method rule rather than as a
resolution to be more careful.

The link-text invariant adopted during A305 caught both display-string collisions automatically.
Reading still found two seams no check flagged, being an insertion that split an argument from its
conclusion and another that orphaned a citation from its subject.

---

## Verification

**All 62 worked numerical values re-derived independently from their stated inputs, with no
corrections required.** That is a first for this series, and I attribute it to computing the numerics
before writing rather than while writing.

239 references with zero undefined, zero orphaned, and zero duplicate URLs. All 70 fixed identifiers
at 200. All 124 DOIs Crossref-resolved on title at the 0.85 threshold with zero flagged. `_verify.py`
at the 0-error 21-warning corpus baseline. Zero style violations, zero doubled words, zero
display-math seam defects. Isolated build succeeding with 88 rendered display blocks and Part 10
navigation.

---

## Densities Are Just Under Band and I Did Not Pad

**1228 lines against a 1300 floor, 88 equations against 90, and 239 references against 250.**

All three shortfalls are small and all three are reported rather than filled. The equation-density and
reference-density passes exist to close exactly this gap, and after A305 came in at 2226 lines and 200
equations I would rather approach the band from below than overshoot it again.

Primary technical documents are already **125 of 229 external references, or 54.6 percent**, which is
the highest in the series at a draft stage. The reason is structural rather than lucky. A weapon
programme reports to a service that keeps its reports, and the defence archive holds Bell's own
project documents covering the Shrike and the RASCAL together. Contemporary coverage at 22.9 percent
of dated references is the clearest deficit for the later passes.

---

## State

**Committed, not pushed.** Nothing in this series is published.

Ten articles complete of seventy-two. **The publication-order dependency is now ten deep**, A306 back
to A297.

**Categories remain undecided** at `aerospace history engineering`, ten articles deep and raised nine
times.

A307 is the North American X-10, which is the Navaho missile testbed and therefore the third
consecutive vehicle that is not an aircraft, and the first that was large enough to take off and land
on its own undercarriage.
