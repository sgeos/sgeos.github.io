# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-12
**Task**: A335, the Scaled Composites X-38. **Equation-density review complete.**
**Committed. NOT pushed**, per the rhythm in which only the publication review pushes.

---

## Fourteen to Twenty-Four, and Three of Eleven Gaps Closed

The article moved from 4,907 lines and 26,710 words to **5,040 lines and 27,858 words**. The reference
base did not move, holding at 1,388 definitions with all 1,220 records still cited, because this pass
adds relations and not literature.

**The eight audited gaps that remain are the opening, two tables, the reference lists and two
restatements**, and not one of them relies on a relation.

---

## The Three Best Additions Sharpen a Conclusion Rather Than Confirming It

**This is the useful kind of equation pass and it is not the usual kind.** Two of the three additions
made the article's claims weaker and more precise.

**Inverting the inflation load for the SPEED at which it bites, rather than for the area.** The full
canopy reaches three g at **32.28 metres per second**, which is only **1.20 times** the assumed
deployment speed, and it reaches two g at **26.36**, which is **below** it. **The claim that the steady
load does not set the reefing stage count therefore holds by only twenty percent in speed**, and at a
two g limit it does not hold at all. The draft rested on the three g figure without saying how much room
it had. **It now says.**

**Asking where the deployment speed comes from at all**, which the draft left as a bare assumption. A
drogue bringing the vehicle to twenty-seven metres per second needs **452.8 square metres**, or **65.0
percent of the main canopy**. **The descent system is two large decelerators in sequence and not one**,
and the second cannot open until the first has done its work. That closes a real hole in the argument.

**Computing the lift-coefficient sensitivity instead of asserting robustness.** The sink rate moves
between 6.42 and 4.97 metres per second across the plausible range, which is a lot. **The energy ratio
moves only as the first power, between 19.7 and 32.8**, so the conclusion survives and **the sink rates
should not be quoted to three significant figures.** The draft claimed robustness without showing it.

---

## Reading the Equations Found a Collision the Pass Itself Introduced

The crew-count model I added used $n$ for the seat count while the scaling relation already used $n$ for
the exponent. **The crew count is now $c$.**

The notation table gained five further entries for cases that were ambiguous and uncaught, the most
useful being that **$L/D$ serves two different aerodynamics in this article**, the canopy gliding at 3
and the vehicle entering at about 0.8, and every use now says which.

---

## The Citation Debt, and What Sizing the Markers Exposed

`citation_gaps` went from 7 to **15** as the equations landed and back to **0** once cluster markers
were split so every relation carries literature within reach.

**Sizing them exposed something the draft pass had not measured.** The `parafoil` period half holds only
**22 records** and the markers requested **41**, so the assembler refused to emit an empty list. The
surplus moved to `parachute_systems`, which holds 184 in the same era. **The keystone cluster is thinner
than it looks and the reference pass should know that before it starts.**

---

## A New Corpus Warning Appeared and Was Cleared

`rather` reached **5.7 per thousand** against the 5.0 limit, taking `_verify.py` off its zero-warning
baseline for the first time in this article. **Nine uses were rewritten.**

**Two took `instead of`, and I checked the grammar rather than assuming it.** That substitution fails
where the complement is not a noun phrase, which is a lesson this corpus paid for. Both complements here
are gerunds, so both are grammatical.

---

## Verification

- `python3 _verify.py` **0 errors, 0 warnings**, back on baseline.
- `python3 tmp/a335/verify.py` **46 of 46**, up from 28. The new relations are re-derived independently,
  the speed inversion round-tripped through the forward load, the glide angle checked as a randomised
  property, and the first-order square-root approximation for the sink shortfall checked against its own
  error bound.
- `./_check.sh --drafts` **passes end to end**, 505 pages, no findings.
- **2,720 reference entries scanned**, all clean.
- All 24 equations read for brace balance, delimiter closure, bare pipes and doubled backslashes.

---

## Outstanding

**Nothing blocking.** The tree is clean and the article is committed.

**The article is NOT pushed**, which is correct. **Publication of the thirty-nine X-Planes drafts remains
unauthorised.**

**For the primary-reference pass, which is your next prompt if you want it:** primaries stand at **686 of
1,320 dated, or 52.0 percent**, at the article's own 2006 cutoff. **The `parafoil` period half at 22
records is the thinnest thing in the base and it is the keystone**, so that is where the pass should
start. `vehicle_sizing` is empty and `entry_aerothermo` holds four, both because the cluster ordering
routes their records to an earlier cluster, and **that is a reporting artefact to fix in the ordering and
not a gap to harvest for.**
