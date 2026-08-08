# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A315 equation-density review, the second of four passes. Committed, **not pushed**, not
published. Display equations rose from **21 to 29**.

---

## The Draft Asserted the Mechanism and Never Wrote It Down

The draft claimed the slipstream keeps the immersed panel flying and never gave the relation that makes
it true. Because the propeller axis lies along the wing chord, the slipstream adds velocity **along the
chord** while the freestream arrives at the tilt angle, so

**α_local = arctan[ V sin(i_w) / (V cos(i_w) + v_s) ]**

**At zero forward speed that is exactly zero, at any tilt whatever.** The immersed wing is not merely
unstalled in hover — it sits at precisely zero incidence, seeing only flow down its own chord. For the
un-immersed panel v_s is zero and the expression collapses to α = i_w, which turns the draft's separate
assertion into a limiting case of one relation.

---

## The Largest Correction Is That a Corridor Exists

The draft never established that a conversion corridor exists. Solving the level-flight balance
T sin(i_w) + L = W for the required tilt, and setting it beside the tilt the immersed panel tolerates:

| Speed | Required | Allowed | Margin |
|---|---|---|---|
| 10 m/s | 51.9° | 90.0° | 38.1° |
| 30 m/s | 26.6° | 46.2° | 19.6° |
| 50 m/s | 20.5° | 33.1° | **12.6°** |
| 60 m/s | 17.0° | 30.0° | 13.1° |

**A margin exists at every speed.** The draft's emphasis on what is stalled left the impression that the
configuration was marginal. It is not. **Its closing claim — that the configuration was sound and this
aeroplane was under-equipped for it — is now established rather than asserted.**

---

## Descent Is What Closes It

Promoted out of Out of Scope, where the draft had abandoned it, because it turns out to be the thing
that matters. Descending adds arctan(w/V) to the angle of attack, and the descent rate that consumes the
whole margin is

**284 feet per minute at ten metres per second**, rising to 1,351 at sixty.

A gentle descent by any normal standard exhausts the margin. That is why tilt-wings carried restricted
descent envelopes, and **why the approach rather than the take-off was the hard half of the flight.**

---

## One Finding Runs the Other Way

Momentum theory with forward speed shows the induced velocity **falls** from 40.05 to 24.71 metres per
second across the conversion, while the freestream rises faster, so slipstream dynamic pressure over the
immersed panel **climbs from 2,210 to 5,772 pascals**.

**The handover is helped by the physics rather than fought by it**, which is a large part of why the
configuration is viable at all and which the draft did not say.

---

## Also Added

**Advance ratio**, running from zero to 1.12 across the conversion. That ties the article to the
critical-advance-ratio source it cited and never used, and it matters because **the pitch control system
that failed exists to manage exactly that range**. A helical tip Mach number of 0.844, so the blade tips
are transonic while the aircraft is not. The figure of merit as a definition rather than a bare number.
And the blowing momentum coefficient the X-18 did not have, at 0.125 for fifteen hundred newtons at
twenty metres per second.

Out of Scope was corrected, since it still said the descent problem was left for a fuller treatment
after the pass had treated it.

---

## Verification

**62 draft-pass re-derivations still reproducing plus 77 new ones, zero disagreements.** All independent
of the calculation modules, with the corridor located by a linear scan against calc2's bisection so
neither validates the other.

`_verify.py` at the 0-error 21-warning corpus baseline. Zero style violations. Isolated build passing
with 29 of 29 display blocks rendered, 8 of 8 tables, and Part 19 navigation. Equation count measured
before and after, per the A310 lesson.

The section scan flagged seven sections and all seven are legitimately narrative, **so the real gap was
not where the scan looks.** That is worth remembering: the scan finds sections without equations, and
this article's largest omission was a missing relation inside a section that already had several.

---

## State

**485 lines, 29 display equations, 66 references, 5,240 body words.**

**Committed, not pushed.** References at 66 are the measure furthest from any band and the reference
pass will move that substantially, since this subject's configuration has a genuine primary literature
unlike the previous two articles.

Nineteen articles complete of seventy-two. Categories remain undecided, and the fourth-class question
in `RESEARCH_AIRCRAFT_STRUCTURE.md` is open across two completed articles.
