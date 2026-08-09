# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A321 equation-density review, the second of four passes.
**Committed, not pushed.** Not published.

**18 display equations to 52**, across sixteen edits, each asserted to match its anchor exactly once.
**1,205 to 1,353 lines, 8,004 to 8,822 words.**

---

## The Two Worst Omissions Were Structural

**The article integrated the flare, said so, described what was being stepped, and never showed the
system.** The central result of the whole piece could not be checked from the article, because the
equations it came out of were not in it. The three-equation system and its polar are now displayed.

**The drag polar itself was absent.** Every lift-to-drag ratio in the article comes out of it, and the
entire approach section turns on the fact that flying faster than best glide makes the glide **steeper**,
which is a property of the polar that the article asserted without ever writing it down.

---

## Two Quantities the Article Never Mentioned At All

**The sink rate at touchdown**, which is the first thing a landing-gear engineer would ask for and which
appeared nowhere. Integrating and stopping short of level:

| Residual path angle | Speed | Sink rate |
|---|---|---|
| 2.0 degrees | 211 mph | 10.8 ft/s |
| 1.0 degrees | 205 mph | 5.3 ft/s |
| 0.5 degrees | 202 mph | 2.6 ft/s |

**A transport touches down at about 2 feet per second and the X-15's gear was designed for 9.** So the
X-24B had to arrive within **half a degree of level** to land as gently as an airliner, and within two
degrees to stay inside a research aircraft's design case. **That is a tighter statement of the precision
problem than the touchdown speed alone**, and it is the version a designer would recognise.

**The Reynolds number**, which is the *reason* model-scale base drag is wrong, in a section built
entirely on that discrepancy and never naming its cause. Flight sits at $9.8\times 10^7$ against
$2.4\times 10^6$ for a twentieth-scale model, a factor of 41. **A correlation calibrated at the bottom of
that range should not be expected to hold at the top of it.**

---

## One Number Corrected

The energy spent in the flare was obtained by multiplying a constant approach drag along the whole arc.
**That overstates it, because the drag falls with the speed.** Taking the difference of energy heights
instead needs no such assumption and gives **74 percent where the article said 83**.

---

## A Second-Order Finding

The X-24B was the X-24A's structure under a new shape, so the pair is a controlled comparison. The gain
is 1.15 in lift-to-drag ratio, and the square root of the wetted-aspect-ratio gain is 1.11.

**Almost all of it came from span, not from a cleaner base.** The base-to-wetted ratio barely moved, at
0.93 of its former value. **The long pointed nose was buying span-loading rather than base cleanliness**,
which is the opposite of what the shape suggests at a glance.

---

## Also Now Shown Rather Than Asserted

The base-drag coefficient written out. The equivalent-skin-friction and forebody-referenced definitions,
both used from the start and never defined. The closed form locating the optimum. Both aspect-ratio
definitions. The load factor definition. The lift balance and dynamic pressure. The best-glide conditions
in closed form. The inverse-square fall of lift coefficient with speed, and the consequence that **seven
eighths of the approach drag is parasite**. The transport comparison worked rather than asserted. The
corridor arithmetic, the stall margin, and the glide footprint radius.

---

## Checks

**The independent verifier extended from 109 to 163 checks, all passing**, with the horizontal ground
track and the residual-angle sink rates integrated separately rather than carried across.

**The display-math-with-trailing-prose guard fired twice and was right both times.**

**Three more records read and dropped, two of them solar-flare physics that the filter missed**, because
solar papers name the flare without the adjective. The filter now excludes flare emission, flare onset,
slow-rise and fast-rise phases, chromosphere and active region. Rejection list 474 to 477.

**`_verify.py` at the 21-warning baseline.** `check_any.py` clean. **A 25-article isolated build with all
52 equations rendering as display math across 25 subsections, zero unbalanced braces.**

---

## On the Band

**Fifty-two equations against a full-aircraft band of 90 to 130.** Below band and reported that way
rather than padded. Every relation the prose names, relies on, or evaluates is now displayed, which is
the rule that produces the number.

**This is the eleventh consecutive article to finish outside all four named genre classes.**

---

## State

**A321 equation pass complete. Committed, not pushed, not published.**

**Awaiting the primary-reference review prompt.** Expect the usual inter-pass dependency. This pass
promoted Reynolds number and scale effects, landing gear and touchdown loads, the drag polar and Oswald
efficiency for low-aspect-ratio shapes, and glide footprint geometry, none of which the draft harvest was
designed around.

**One tooling note carried forward for the publication pass.** A320's survey was written by placeholder
substitution which froze its citations so they stopped tracking the clusters. Cluster citations must go
into the body as live calls.

**Still open and unchanged.** The fourth genre class, now eleven consecutive articles. The A305 length
offer.
