# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-10
**Task**: A324, the Lockheed X-27, drafted. **Draft pass only.** Committed, not pushed, not published.

---

## The Class Question, Settled Against the Handoff's Prediction

**The handoff written before this pass said the short designation-anomaly order was the honest default,
and the record does not support that.** It was right that nothing flew and wrong about what follows.

The X-27 was the CL-1200 Lancer, a Lockheed private venture derived from the F-104 and offered for
export. **No aircraft was built.** One full-scale mock-up of wood with a metal skin was completed and up
to three fuselages were reportedly worked. **The NASA Technical Reports Server returns zero results for
the vehicle under any of its names**, which was confirmed before designing the harvest rather than
discovered during it.

**But the design record is complete enough to dimension systems against, and the parent flew for thirty
years.** Published geometry, weights, engine ratings and performance estimates all exist, and a
derivative can be checked against the thing it was derived from. **The genre document's test is whether
there is a keystone**, and the X-27's stated objective of testing advanced-technology engines at Mach
2.6 is one. It is therefore a full-order article, at 6,066 lines, 39 equations and 1,650 references.

**The harvest had to be written for the physics rather than the vehicle**, since no query naming the
aircraft returns anything. That is the methodological move this subject required.

---

## What the Article Establishes

**The binding question is whether a turbofan can be fed at Mach 2.6 through an inlet descended from a
Mach 2.0 turbojet installation, in an aluminium airframe.** Two of the three answers are negative.

**The inlet cannot meet the standard with one cone.** Taylor-Maccoll was integrated rather than assumed.
The best single cone reaches 0.7442 against a reference recovery of 0.8585, an 11.44 point shortfall.
**That is a floor rather than an estimate**, because the calculation is inviscid and charges nothing for
bleed, friction or off-design operation, while the reference standard includes all of them. The same
arrangement clears the standard at Mach 2.0, which is the control showing the method is not biased
against the design. **Two ramps recover 8.18 of the missing points, and the record says the X-27 was to
have rectangular intakes without saying why.** The article offers this as the explanation and labels it
inference.

**The structure cannot hold its strength there.** Recovery temperature at Mach 2.6 is 210.8 degrees
Celsius, where the alloy retains about 69 percent of its yield. **The dash defence does not survive**,
since the skin time constant is 26.2 seconds and the skin is nine-tenths of the way there after a minute.

**The manoeuvre answer is favourable to Lockheed.** Sustained load factor 6.34 against the F-5E's 5.33,
and specific excess power within 3.5 percent of the F-15A's. **The ordering holds across the whole range
of both free parameters**, which makes it a statement about ordering rather than about the absolute
numbers, and the article says so.

---

## The Result Worth Your Attention

**Two published figures that were never derived from one another agree through geometry connecting them.**

The cowl radius is not in the public record and the four inches of spike travel is, so shock-on-lip
geometry was inverted to ask what radius that travel implies. **A twenty-five degree cone, an entirely
ordinary half-angle, gives 5.401 square feet of capture against the 5.639 the TF30's documented 260
pounds per second needs at Mach 2.0.** Agreement to 4.2 percent.

**It does not establish that the aircraft would have worked.** It establishes that the published airframe
and engine figures are mutually consistent, which is evidence the design was worked out rather than
sketched, and nothing beyond that. The article says exactly this.

---

## Three of My Own Errors, Two of Them in the Article

**A Breguet implementation carried a spurious factor of g** and produced a combat radius of 27 nautical
miles against a claimed 367. That looked like a devastating finding about the brochure and was a defect
in the checker. **A discrepancy near an order of magnitude is a hint that the checker is at fault,
exactly as a suspiciously clean factor is.** Corrected, the claim survives.

**An inlet calculation converted maximum corrected airflow to physical flow at Mach 2.6** and obtained
three times the sea-level rating. The arithmetic was right and the premise was wrong.

**A cone-angle search ran to its bound and returned a total-pressure recovery of 1.227**, which is not
merely wrong but impossible. The function now returns nothing on shock detachment and raises on any
recovery outside the unit interval. **A checker that can print free energy is not checking.**

**And two genuine bugs were found in the verifier itself**, one admitting the strong-shock branch and one
mismatching the property-test calling convention. 59 of 59 checks now pass, none importing the
calculation.

---

## One Shared-Module Defect Fixed

**`_lib/reflow.py` held reference link pairs atomic but not inline `[text](url)` links, while
`_lib/lint.py` reported both.** The two modules disagreed, so reflow would produce a file it had just
declared a fixed point and lint would then fail it. Fixed with a regression test, and confirmed by a
controlled before-and-after diff to change nothing on A369, the one article authored with reflow.
Library tests are 45 of 45.

---

## Patterns Continuing

**The keystone cluster was thin for the sixth article running.** Energy manoeuvrability returned 28
records against 232 for materials at elevated temperature, and period vocabulary raised it to 51.
**Reported in the article rather than padded**, with the reason, which is that the foundational documents
are Air Force internal reports that were never journal articles.

**The designation finding is now three deep.** A322, A323 and A324 are three consecutive designations
that did not go to a research aeroplane. The first two were off-the-shelf aircraft bought for properties
they already had. **The third did not exist at all.** This belongs in the closing article.

---

## State

Working tree has the new draft and the process files, committed. **Not pushed**, per the draft-pass
convention. `_verify.py` at zero errors and the 21-warning baseline, check_any clean, 45 of 45 library
tests passing, reference integrity showing 1,650 definitions with zero undefined and zero orphaned, and
an isolated 28-article build succeeding with all 27 back-references resolving and the page rendering
correctly.

---

## Awaiting Instruction

**A324 has completed the first of four passes.** The expected next prompt is the equation-density review.

**One thing is worth deciding before that pass.** The article carries 39 display equations against a
series median of 94, and the reason is that its subject is narrow. Whether that is a subject producing a
low count or an equation pass waiting to happen is exactly what the next pass exists to determine, and I
have not pre-judged it.
