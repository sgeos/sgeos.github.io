# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A312 draft pass, the first of four. **Committed, not pushed.** All sixteen articles in the
series remain in `_drafts/`.

---

## The Keystone Was Chosen Rather Than Discovered, and the Article Says So

This is the structural difference between A312 and everything before it, and it is the risk the
handoff warned about.

Every previous article found its keystone by locating the one binding unknown. **The X-15's record is
large enough that four candidate keystones are all well supported**, and an article that picks one
silently is hiding a decision. So the article names all four, chooses, and defends the choice.

The rejected candidates are aerodynamic heating, hypersonic stability and control, flight outside the
atmosphere, and structures at temperature. **The objection to all four is the same**: they are
consequences of a single quantity, and treating any one as primary makes the other three look like
separate subjects when they are the same subject.

---

## The Quantity Is Energy, and One Ratio Carries the Article

At its record speed the X-15's kinetic energy was **2.041 MJ per kilogramme**. The energy needed to
take a kilogramme of its own structure to melting and melt it is about **0.904 MJ**.

**The aircraft carried 2.26 times the energy needed to melt itself**, and 7.4 times the energy needed
to take the whole structure to the 1,200 degree Fahrenheit limit of its strength.

That is what makes hypersonic flight different in kind rather than in degree. **Deceleration stops
being a nuisance and becomes a thermal event**, and the research question becomes whether a piloted
aircraft can carry that much energy, dispose of all of it, and land.

**The central number follows.** A Sutton and Graves correlation at the record condition gives 64.8
watts per square centimetre. A structure at its design temperature can radiate 3.28. **The record
flight asked the structure to reject 19.8 times what its design temperature could handle** — which is
why the X-15A-2 was covered in ablative coating, why that flight was the fastest ever made, and why
nothing like it was attempted again. The correlation is validated against the reported 2,700 degree
leading-edge temperature, overshooting by 12.7 percent, and survives doubling the assumed nose radius.

---

## Five Results the Sources Do Not State

**The two records are one budget spent two ways**, at 2.347 and 1.964 MJ/kg. They differ by 19.5
percent, and the reason is not piloting: the speed flight was flown by the X-15A-2 with external tanks.

**Converting the speed record's kinetic energy entirely to height gives 239.3 km against an actual
altitude record of 108.0.** A little over half the available energy never reached apogee.

**The heating rate falls with thinner air and the heat load rises.** The rate goes as √ρ·V³ while the
time to shed a fixed energy goes as 1/ρ, so rate and load are optimised by opposite trajectories.
**The X-15A-2 moved from a rate-limited to a load-limited regime when it was coated**, which is a more
interesting statement than that the coating let it fly faster.

**A 300 kelvin gradient alone yields the structure**, at 830 MPa. That is why the skin is corrugated
and slotted for no load reason at all. And a 1.5 mm Inconel skin reaches equilibrium in 7.5 seconds,
which is what makes a hot structure rate-limited.

**99.8 percent of the energy the vehicle holds at its fastest must be disposed of before it lands.**

---

## The Series Thread Arrives From the Opposite Direction

The X-13 and X-14 lost their aerodynamic control authority because the vehicle was not moving. **The
X-15 loses it because there is no air.** Same relation, opposite cause, same reaction-control answer,
and the dynamic pressure ratio across a single flight exceeds 4,600.

---

## An Order-of-Magnitude Error, Caught by Verifying

I wrote the aerodynamic-to-reaction crossover as **6,280 pascals. It computes to 628.** The altitude
band moved from "between 30 and 50 kilometres" to about 55. **Eighth consecutive article in which
computing before writing caught a wrong claim**, and the first where the error was a full order of
magnitude.

The corrected value produced something I had not looked for. **Flight 91's burnout at 53.6 km sits
within 1.4 km of the crossover**, so on a high flight the engine stops at roughly the altitude where
the aerodynamic surfaces stop working, and the pilot loses thrust and aerodynamic control at nearly
the same moment.

**Two omissions were found by surveying the references rather than by reading the draft**: the MH-96
adaptive flight control system, which was fitted to the airframe that was lost, and shock interference
heating, which is what nearly destroyed the speed-record flight and which the draft described without
citing. Both added.

---

## Verification

**77 reference definitions, 62 external URLs, zero duplicates, zero orphans.** All 40 in-prose numbers
re-derived independently and reproducing. `_verify.py` at the 0-error 21-warning corpus baseline.
Zero contractions, em-dashes, en-dashes, prose colons, prose semicolons, prose parentheticals, doubled
words, duplicate headings, unbalanced emphasis markers, lone dollar-delimited lines, or adjacent
display-math seams. Two style violations were found and fixed, a prose semicolon and a prose colon.
Isolated build succeeding with **48 rendered display blocks matching source exactly** and Part 16
navigation.

**Two documents cited in the draft were absent from the harvest** and were added to the detail fetch
by identifier rather than by repointing the prose at something else, which is the A311 lesson applied.
One archive quirk is recorded in The Source Base: the lift and drag report's cover reads Saltzman and
Garringer while the archive records the authors in the opposite order, and the article uses the
archive's order because its citations are generated from archive metadata.

---

## State

**669 lines, 48 display equations, 77 references, 8,057 body words.**

All three densities approach from below, at 669 against a 1300 floor, 48 against 90, and 77 against
250. Nothing was padded. Contemporary references are 13 of 58 dated, or 22.4 percent, and primary 45,
or 77.6 percent.

The draft is shorter than A311's 854 and comparable to A308's 678. **The three remaining passes have
more to close than usual**, and the equation pass in particular has a large surface to work on because
the energy framing generates relations readily.

**Committed, not pushed.** Nothing in this series is published. The publication-order dependency is
sixteen deep. **Categories remain undecided** at `aerospace history engineering`, sixteen articles deep
and raised twenty times.
