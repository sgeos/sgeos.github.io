# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-06
**Task**: A307 equation-density review, the second of four passes. Committed. **Not pushed.**

---

## Baseline and Result

84 display equations across 13,382 body words. **38 added across 17 edits**, taking the article from
943 lines and 84 equations to **1111 and 122**, which is inside the 90 to 130 band.

The structural audit that opens this pass found **no orphaned or duplicate subsections**, which is the
first time since the audit was adopted that it found nothing. A306 had four.

---

## The Largest Omission Was the Argument That Killed the Programme

The article stated the cruise-versus-ballistic exposure comparison in words and never derived it. It
now does. A minimum-energy ballistic ellipse over the same ten thousand kilometres gives a range angle
of 1.570 radians, a burnout speed of 7193 metres per second, an eccentricity of 0.415, an apogee of
1319 kilometres, and a free-flight time of

**32.2 minutes against the cruise mission's 172, an exposure ratio of 5.35.**

That number is the whole cancellation case. The airbreathing weapon is exposed more than five times as
long, and it is exposed inside the atmosphere where an interceptor can reach it while its competitor
spends most of its flight above thirteen hundred kilometres where in 1957 nothing could.

---

## Other Relations Now Shown

The drift specification is inversely proportional to the range requirement, so growing the mission from
five hundred to five thousand five hundred nautical miles tightened the gyroscope specification
elevenfold. Two-system availability. Static margin and pitch stiffness, with the finding that **a seven
percent aerodynamic-centre shift exceeds a three percent static margin outright**, which is what makes
the autopilot mandatory rather than convenient. The drag decomposition placing base drag at half the
wave drag. The thrust-lapse relation. The skin thermal time constant of 48.6 seconds, which shows the
platform oven faces a step rather than a ramp. The linear drift-temperature model. The quadrature
variance shares, of which **two attitude terms carry 94 percent**. Glide-slope sink rate and the
exponential flare. The full-scale Reynolds number of 46.8 million against the free-flight models' 19 to
51 percent of it. Dive-angle sensitivity of 48 metres per milliradian.

**The contemporary comparison got sharper rather than more flattering.** Carrying the 2025 reported
bias instability of 0.003 degrees per hour through the article's own relation gives 957 metres over the
Navaho mission, which **still does not meet the 800 metre requirement on drift alone**, seventy years
later and before any other budget term is added. The earlier phrasing implied the requirement had
become easy. It has become approachable by a component rather than by a national programme, which is a
different and more honest claim.

---

## Verification

All 50 new worked values re-derived independently with **no corrections**, and all 102 previously
verified values still reproducing. Zero duplicate headings, zero display-math seam defects, zero lone
dollar-delimited lines, zero paragraph-repeated citations. 122 rendered display blocks confirmed in the
built HTML against 122 in the source. `_verify.py` at the 0-error 21-warning corpus baseline. Zero
contractions, em-dashes, en-dashes, prose colons, prose semicolons, or prose parentheticals.

**Two seam defects found by reading and not by any check.** The configuration insertion orphaned the
canard citation list from the material it belonged to, leaving it dangling after a base-drag
conclusion, and the ballistic insertion left three consecutive identically-introduced citations. Both
repaired. This is the fifth article in which a seam defect survived every automated check.

---

## A Process Error I Made and Have Corrected

**The citation-construction rotations I reported as complete in the draft pass never reached the
article.** An earlier step in that pass had left the shell inside the scratch build directory, the
rotation script used a relative path, and so both batches edited the build copy. The verification I ran
afterwards read that same copy and reported success. The draft was committed with the formulaic drift
still present, and my report to you on that point was wrong.

The rotations are now applied to the article and the script uses an absolute path. Construction share
is **15.1 percent for `in` and 10.1 percent for `is`**, against 21.0 and 30.1 before.

The general lesson is worth recording. An edit script with a relative path is unsafe in any session
where another step changes directory, and a verification that reads the same relative path will confirm
the wrong file rather than catch it.

---

## State

**1111 lines, 122 display equations, 218 references, 13,591 body words.**

Equations are inside band. **Lines remain 189 short of the 1300 floor and references 32 short of the
250 floor**, and the reference-density pass is expected to close both. The equation pass added five
references of its own, which is the usual pattern of it creating reference debt, and the primary harvest
should be aimed at the topics it opened, namely ballistic trajectories, automatic landing control laws,
and inlet and engine matching.

**Committed, not pushed.** The publication-order dependency is eleven deep. **Categories remain
undecided** at `aerospace history engineering`, now raised eleven times.
