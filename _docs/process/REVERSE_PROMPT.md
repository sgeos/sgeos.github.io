# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-07
**Task**: A310 publication review, the fourth and final pass. Committed and **pushed**. **Not
published.** All fourteen articles in the series remain in `_drafts/`.

---

## The Review Ran the Article's Relations on a Modern Vehicle, and Corrected an Overstatement

This is the most useful thing the pass did, and it is worth putting first because the obvious version
of the comparison would have been wrong.

Applying the article's own relations to three representative modern electric vehicles gives two
results. **The first is that a small electric tail-sitter's disc loading and wing loading are the
same quantity to within a factor of two**, against the X-13's ratio of 84. This article derived, from
the XFY-1 comparison, that a designer wanting stall-level dynamic pressure on the controls in a hover
should set the disc loading equal to the wing loading. A modern tail-sitter satisfies that without
anyone arranging it. **The design difference that separated the X-13 from the XFY-1 has been
dissolved rather than solved.**

**The second corrects the first.** Twenty-three minutes of hover against the X-13's eleven suggests
the energy problem has halved. It has not. The modern figures assume a battery at thirty percent of
the mass where the X-13's fuel was seventeen. Holding the energy fraction equal gives **12.9 minutes
against 11.0, an improvement of about seventeen percent in seventy years.**

Expressed as an effective specific consumption the comparison is cleanest. **A battery forty-eight
times worse than kerosene per kilogramme, driving a rotor seventeen times better at converting power
into thrust, comes out fifteen percent ahead.** The rest of the modern advantage is bought by
carrying more energy, which a vehicle with no pilot and no weapon can afford. **The hover is still
expensive and it is expensive for the same reason.**

---

## Contemporary Coverage

A 64-query sweep returned **710 new records**, taking contemporary references from **47 to 133, or
41.7 percent of dated**, which sits inside the 101 to 189 absolute range the series has held since
A301.

Twelve subsections replaced five. The ones worth naming are these.

**The tail-sitter came back as a biplane quadrotor**, which is the X-13's configuration with four
rotors in place of one jet and a computer in place of the man, and it has a large literature.
**The stability derivatives the 1953 wind-tunnel programme measured for the XFY-1 are now obtained
from the vehicle itself in flight.**

**The handover is a least-squares problem.** The blend the X-13's pilot performed by hand is now the
solution of a control allocation, evaluated many times a second.

**The position loop became somebody else's problem**, closed by a computer with better sensors than
eyes, and where a human remains in it the article's transport-delay analysis has become a research
subject. **The ground observer who talked Girard onto the hook was an early and unusually literal
instance of shared control with a transport delay.**

**The visual task was solved by deleting the viewer.** Vision-based landing on a moving platform is
harder than landing on a trailer and is the same problem.

**Handling qualities became certification**, and the most direct descendant of the X-13's pilot
problem is simplified vehicle operations, in which the aircraft is made easy enough that a
non-pilot can fly it. **The X-13 asked an experienced test pilot to do something at the edge of what
a person can do, and the field's eventual answer was to change the aircraft rather than train the
person.**

**Ground effect became a civil planning problem.** A tail-sitting jet needing a prepared surface and
a particular trailer was held against it. A modern vertical take-off aircraft needs a prepared
surface and a licensed vertiport, and that is treated as infrastructure rather than as a defect.
**The requirement did not go away. The expectation did.**

**Subscale free flight is still how it is done**, and the difference from 1958 is that the model now
carries the flight computer it is testing, so the Reynolds mismatch matters less because the quantity
of interest is a control law rather than a stall.

A closing subsection names the three findings with no modern remedy. **Hovering is expensive, ground
loading scales with disc loading, and a hovering aircraft has no aerodynamic restoring moment.** What
changed is who closes the loop, how much energy the vehicle can afford, and whether the ground is
expected to be prepared. **None of those is an aerodynamic advance, and the X-13's aerodynamics were
never the problem.**

---

## Two Defects Found and Fixed

**The section replacement silently dropped three equations**, taking the count from 91 to 88 and
below the floor. Caught by measuring rather than assuming, and the relations were restored into the
lead subsection where they belong.

**An en dash reached the prose inside a citation display string.** Publishers use them in titles, and
a disambiguation suffix cut from a title carries one into the display, which then appears in the
body and violates the house style rule. **The fix is an automatic rule in the normaliser rather than
a patch in the markdown**, since the markdown is regenerated, and it now normalises en and em dashes
to hyphens across every display in the master table. Zero remain.

---

## Verification

**336 reference definitions, 323 external URLs, zero duplicates.** All 268 worked values re-derived
independently and reproducing, including every publication-review addition. `_verify.py` at the
0-error 21-warning corpus baseline when run from the repository root. Zero contractions, em-dashes,
en-dashes, prose colons, prose semicolons, prose parentheticals, doubled words, duplicate headings,
unbalanced emphasis markers, lone dollar-delimited lines, or adjacent display-math seams. Genre
section order correct with The Source Base immediately before the Epistemic State. Isolated build
succeeding with **91 rendered display blocks matching the source count exactly**, Part 14 navigation,
twenty-two tables, no unresolved reference links and no surviving Liquid tags.

The Epistemic State was updated in the same pass and now flags that **the three modern reference
vehicles are representative rather than actual**, with masses, spans, areas, and rotor geometries
chosen as plausible for their classes. The conclusions drawn from them are ratios and orders and are
insensitive to reasonable variation. The specific endurances are not.

---

## Final State

**1346 lines, 91 display equations, 336 reference definitions, 17,380 body words.**

**All three densities are inside band and nothing was trimmed at any point.** That is the fifth
article in the series to finish that way, after A306, A307, A308, and A309, and the first to do it
without any band being exceeded in either direction.

Primary sources are 167 of 319, or 52.4 percent of dated. The absolute count is unchanged since the
primary pass and the percentage moved only because the contemporary additions grew the denominator.

Citation construction mix healthy at a top bigram of 4.5 percent. `aircraft` at 8.61 and `control` at
5.94 per thousand body words are the subject and keystone nouns and are reported rather than
remediated.

---

## State

**Pushed.** Nothing in this series is published, and the deploy workflow builds without `--drafts`,
so the push is safe. **The publication-order dependency is fourteen deep**, A310 back to A297.

Fourteen articles complete of seventy-two. **Categories remain undecided** at `aerospace history
engineering`, fourteen articles deep and raised eighteen times.

A311 is the Bell X-14, and it is unusually well set up by this article. The X-14 is the
variable-stability aircraft that **established the control-power criteria A310 borrowed
anachronistically**, so the obvious keystone is the criteria themselves and the obvious opening is
that the previous article had to use numbers this one produced. The A310 harvest already holds the
Drinkwater and Rolls work, the Garren visual-flight investigation, and the jet-lift powerplant
experience report, so it should be reused rather than rebuilt.
