# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A311 draft pass, the first of four. **Committed, not pushed.** All fifteen articles in the
series remain in `_drafts/`.

---

## The Bleed Price Was Measured Rather Than Estimated, and It Is the Article

This is the most useful thing the draft found and it comes from inverting one sentence in a report
about something else.

Attitude control on the X-14 came from compressor bleed, and the cost of bleed is normally estimated
because separating it from every other installation effect requires flying the same engine with two
different bleed schedules. **The X-14A programme did exactly that, for an unrelated reason.** The
tip-turbine fan report states that the fans needed about half the bleed of the reaction controls for
the same thrust, and that this let the engines produce four percent more thrust. If thrust with full
bleed is $T_0(1-\beta)$ and with half bleed $T_0(1-\beta/2)$, then $(\beta/2)/(1-\beta) = 0.04$ and

**beta = 0.08/1.08 = 7.41 percent, exactly.**

Set that against the hover margin rather than against the thrust and it stops being a small number.
At the reported 3,700 pound test weight and 1.1 to 1.2 available thrust-to-weight ratio, the bleed
cost 397 pounds and the margin before it would have been 767 to 1,137. **The attitude control system
consumed between 34.9 and 51.8 percent of everything the aircraft could lift beyond its own weight.**

Not payload. Not fuel. The ability to point.

---

## Four Results the Sources Do Not State

**The roll inertia, recovered from two reports that do not mention each other.** One states the
maximum lateral control power tested at 2.0 rad/s2. The other states that the replacement wingtip
fans were designed for 150 pounds of thrust. Together they give 3,333 kg m2 and a radius of gyration
of **13.7 percent of span**, which is mid-band for an aircraft with its engines on the centreline and
borrowed light-aircraft wings. That the recovered value lands where it should is the check. **The
sharper inference is that the fans were specified at exactly the existing maximum authority and not
above it**, which says bleed rather than control power was the binding constraint.

**Control power falls inversely with span.** With tip nozzles, CP goes as $F b / (m b^2) = F/(mb)$,
and a hovering aircraft has thrust proportional to mass, so at fixed bleed fraction **CP is
proportional to 1/b**. Holding the criterion while doubling the size doubles the bleed. A jet-lift
aircraft with a twenty percent thrust margin exhausts it near **28 metres of span**, and a Do 31 sized
vehicle would need **3,542 pounds of thrust at each wingtip** to reach 2.0 rad/s2. That is a small jet
engine on each wing purely to point the aircraft. **The type stopped growing where the arithmetic says
it had to.**

**The original X-14 could not hover at the weight the X-14A hovered at.** Sources give the Viper 8 as
either 1,750 or 1,560 pounds of thrust each, and the article resolves neither because both give a
thrust-to-weight ratio below unity at 3,700 pounds, at **0.946 and 0.843**. So the J85 re-engining was
**not an upgrade to an aircraft that worked. It was the precondition for the research programme**,
because a variable-stability aircraft must be able to give control power away to the experiment and
still fly.

**Gravity was not adjustable, and the mismatch is exactly 2.46.** Attitude dynamics contain no
gravitational term so the X-14A reproduced a lunar module's attitude response exactly. Translation
goes as $g \tan\theta$, so the lunar timescale is longer by $\sqrt{9.807/1.62} = 2.46$. Holding five
degrees for five seconds moves 10.7 metres on Earth and 1.8 on the Moon. **It simulated the inner loop
exactly and the outer loop 2.46 times too fast**, which is why the Lunar Landing Research Vehicle,
a far more dangerous machine, had to be built.

---

## The Archive Has a Hole and the Article Says So

**NASA TN D-1328, Rolls and Drinkwater 1962, is the origin of the criteria and could not be
retrieved.** The NTRS record carries an abstract and no document, and the search endpoint returns it
for no phrasing of its own title. It was found only through its citation in a later report.

The article therefore takes every quantitative claim from the complete successor, TN D-2701, and The
Source Base states this plainly rather than implying the origin was read.

**One consequence is worth flagging because it nearly went the other way.** The first writing of the
threshold section assigned plausible Cooper ratings to the three sampled control powers and
interpolated a satisfactory boundary from them. **Those ratings are in no source.** The figure
carrying them did not survive text extraction. Inventing them would have manufactured the article's
headline number out of nothing, so they were removed and replaced by the argument that survives
without them, which is about resolution: three points spaced 0.6 apart locate a threshold only to
within **thirty to seventy-five percent of its own value**.

---

## Defects Found

**Two in the numerical spine, both caught by running it.** The repositioning analysis used
$a = g\theta$ and searched tilt over a bounded interval whose upper bound it then reported as the
optimum for every control power above 1.4, so the printed optimum was **the edge of the search
range rather than a minimum**. Rewritten with $a = g\tan\theta$, a realistic cap, and a hover-scale
correction distance. The corrected version yields a genuinely useful result, that control power has
**sharply diminishing returns with an exponent of minus 0.26**, so two and a half times the authority
buys only 21 percent less time.

**Three caught by reading and counting, all of which passed every automated check.** The phrase "in
its own right" ended one paragraph and opened the next, because a later insertion landed behind a
sentence that happened to end the same way. **The disturbance fraction and the radius-of-gyration
fraction were both written as kappa**, a symbol collision inside one article. And a sentence promised
four subsections where five stood.

---

## Verification

**95 reference definitions, 81 external URLs, zero duplicates, zero orphans.** All 45 in-prose numbers
re-derived independently and reproducing. `_verify.py` at the 0-error 21-warning corpus baseline from
the repository root. Zero contractions, em-dashes, en-dashes, prose colons, prose semicolons, prose
parentheticals, doubled words, duplicate headings, unbalanced emphasis markers, lone dollar-delimited
lines, or adjacent display-math seams. Genre section order correct, with The Source Base immediately
before the Epistemic State and the series extras ordered as in A310.

**The bundle was installed for the first time**, into a repo-local `vendor/bundle` that was already
gitignored. The isolated build therefore now runs the real CI toolchain including `jekyll-archives`
rather than a Gemfile-free approximation. It succeeds with **51 rendered display blocks matching the
source count exactly**, Part 15 navigation, no unresolved reference links, and no surviving Liquid
tags.

---

## Draft State

**854 lines, 51 display equations, 95 references of which 72 research, 13,322 body words.**

All three densities approach their bands from below, at 854 against a 1300 floor, 51 against 90, and
95 against 250. **Reported rather than padded.** Contemporary references are 10 of 72 dated, or 13.9
percent, which is the publication review's task.

The draft sits above A310's 810 and well above A308's 678, which is deliberate under the rule that
the gap a draft leaves is the gap the passes must close.

---

## State

**Committed, not pushed**, per the draft-pass convention. Nothing in this series is published.
**The publication-order dependency is now fifteen deep**, A311 back to A297.

**Categories remain undecided** at `aerospace history engineering`, now fifteen articles deep and
raised nineteen times.

A312 is the North American X-15, and the risk is the reverse of the usual one. **The record is large
enough that the article could become a summary rather than an analysis.** The keystone will have to
be chosen and defended rather than discovered, and the A311 harvest will not help.
