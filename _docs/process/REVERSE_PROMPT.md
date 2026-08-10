# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-10
**Task**: A327 draft pass, the first of four. Committed, **not pushed**, per the rhythm.

**State: 4,978 lines, 22 display equations, 1,375 reference definitions, 28,697 words.** Thirty-one
articles drafted, all in `_drafts/`, **none published**.

---

## This Article Inverts the One Before It

**The X-29 was built and left a flight record. The X-30 left a technology record and no aeroplane.**
The pair is useful because the X-29 could measure the thing it existed to measure, and the X-30's
central quantity could not be measured by anything on the ground at all.

---

## The Keystone

**It is the verification gap, not the scramjet.** Supersonic combustion was demonstrated in the 1960s.

**What accelerates the vehicle is gross thrust minus ram drag**, and at orbital speed those are nearly
equal. At 7,000 metres per second **net thrust is 4.78 percent of gross**, the amplification from a
gross-thrust error to a net-thrust error is **20.90**, and the fuel's chemical energy is only **12.82
percent** of the stream's kinetic energy. Read as a budget, everything the vehicle loses to spillage,
shock losses, incomplete combustion, cooling and external drag must together fit inside 4.78 percent.

**And nobody could measure it.** Mach 25 carries 34.26 megajoules per kilogram of stagnation enthalpy.
The flow needs 2.0 milliseconds to cross a five-metre combustor and about eight flow-through times to
establish. A reflected shock tunnel gives 2.5 of them and an expansion tube gives 0.1. **The facilities
that reach the enthalpy cannot hold it, and the ones that can hold it cannot reach it.**

---

## The Result That Surprised Me

**The rocket equation was never the X-30's problem.** Integrating it with the specific impulse allowed
to decay, rather than assuming a constant value and so begging the question, an all-rocket single stage
permits **12.19 percent** of its mass to be structure. **Air-breathing to six kilometres per second
permits 52.56 percent**, and it keeps closing even when drag takes sixty percent of thrust throughout.

**The concept is not forbidden by mass fraction. It is deferred by uncertainty.**

---

## Three Errors in My Own Physics, and the Verifier Caught the Worst

**The Rayleigh choking relation was missing a factor of (gamma + 1)** on the fourth-power term. A
one-line identity exposed it, because the ratio must be **exactly unity at Mach one** and the wrong
form returned 1.108. **An identity a quantity must satisfy is worth more than a second opinion.**

**The guard on that same function then rejected subsonic entry**, which is precisely the ramjet case
the comparison needed.

**And the combustion comparison used Mach 1.2 as its subsonic case, which is supersonic.** A ramjet
decelerates to about Mach 0.3.

**Corrected, the analysis reproduces something it was not fitted to.** Burner entry static temperature
crosses the dissociation threshold of about 3,000 kelvin **between Mach 6 and Mach 8** for subsonic
combustion, which is where ramjets in fact give way to scramjets. The reason for a scramjet is a
temperature argument rather than a choking one.

---

## A Confident Wrong Answer, Reported as Such

The first analysis searched for the speed at which net thrust reaches zero, found 16,577 metres per
second, and was about to call it a ceiling set by chemistry. **In an ideal engine net thrust never
crosses zero at all.** The crossing moves to 8,880 metres per second at a nozzle efficiency of 0.90 and
**disappears entirely at 1.00**, so it was a finding about the assumption. The article states the loss
budget instead, which assumes no efficiency.

---

## The Keystone Cluster Was Thin for the Seventh Article Running

**The cause was supply and it was unambiguous.** Searching the whole 2,333-record pool for "specific
impulse", "ram drag", "net thrust" and "thrust margin" returned **zero titles**. The field says force
accounting, thrust minus drag, installed performance and cycle analysis. A second harvest in that
vocabulary took the cluster from **2 to 32**.

Three further headings were thinner than their subjects, in each case because a pattern required a
phrase the titles do not use.

---

## Verification

**58 of 58 independent checks passing, none importing the calculation.** The hydrostatic profile is
checked by numerical integration, the Rayleigh relation by its Mach-one identity and two randomised
properties, the normal shock recovery by two independent formulations, the ascent mass fraction by
Simpson quadrature against a midpoint rule, the radiation equilibrium temperature by bisection rather
than a fourth root, and the corridor altitudes by scanning rather than bisecting.

`_verify.py` at the 21-warning baseline, check_any clean after removing **four prose semicolons I had
introduced**, reference integrity at 1,375 with zero undefined, orphaned or duplicate URLs, **zero
search-endpoint citations**, the full set swept with **zero hard failures**, zero constructions above
the corpus maximum, and a 31-article isolated build rendering all 22 equations across 17 sections and
13 tables.

---

## Awaiting Instruction

**A327 has completed the draft pass only.** The equation, primary-reference and publication passes
remain, each on its own prompt.

**22 display equations is low against a corpus median of 94**, and the audit already names twelve
sections that state numbers with no displayed relation behind them. The equation pass has ample
material.
