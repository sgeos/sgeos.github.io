# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A318 primary-reference review, the third of four passes. **Committed, not pushed. Not
published.**

**References 531 to 824** across eight edits. 949 lines to 1,258, 7,831 words to 9,628. Equations
unchanged at 45, measured before and after.

---

## The Audit Named Both Defects Before Anything Was Selected

Running the coverage audit first is the rule, and it paid twice.

**The inter-pass dependency, reproduced almost exactly from A317.** The equation pass promoted ten
subjects. **Eight were thin in the pool, three had zero citations, and slot metering had zero records.**
Everything the article argued from the start was deep and fully used, with the attachment line at 22 of
22 and surface tolerance at 34 of 34. The draft harvest could not have known which derivations would come
to exist.

**The era gap, which is what you asked about.** Period sources through 1965 were **12.5 percent** of
citations against **53.8 percent** contemporary. For an aeroplane that flew in 1963, in a series that
treats the period record as the backbone, that is the wrong way round.

**It is now 27.9 percent period against 35.3 percent contemporary.**

---

## The Era Gap Was Selection, Not Supply

This is the part worth keeping.

**Four hundred and seventeen records dated 1970 or earlier were already in the pool and unused.** Among
them was [Schubauer and Skramstad 1947][ssk], whose measurement of laminar boundary-layer oscillations is
the experiment the entire stability argument rests on, and which the article had been leaning on without
citing.

[ssk]: https://ntrs.nasa.gov/citations/19930091976

The cause was **cluster ordering**. Broad topical groupings were matching first and the foundational work
was falling between them. A dedicated period cluster, placed after the specific topics so it would not
gut them and before the broad ones so it would not be pre-empted, recovered 253 records at a stroke.

**A search would not have fixed this and a bigger harvest would have hidden it**, which is the
supply-versus-selection distinction the series keeps rediscovering.

---

## The Recovery Worth Naming

**[Braslow and Knox 1958][bk], the simplified method for the critical height of distributed roughness
particles.** The equation pass derived that criterion and applied it to get an admissible roughness of
0.0123 inches, and cited nothing for it.

[bk]: https://ntrs.nasa.gov/citations/19930085292

It was written by Albert Braslow, the same engineer whose monograph is this article's main narrative
source and who served as NASA technical consultant to the X-21 programme. **The man who wrote the history
the article relies on also wrote the criterion it uses for its arithmetic**, and the draft had cited him
for one and not the other.

Also recovered, **Oswald 1932**, whose span-efficiency factor is the 0.80 the drag build-up uses and is
still called by his name.

---

## A Homonym Inside Aerodynamics Itself

Every homonym this series has documented has been a word shared with another discipline. This one is not.

**Boundary layer control means suction to hold laminar flow and cut drag. It also means suction or
blowing to delay separation and raise lift.** Same name, same mechanism, frequently the same authors and
the same laboratories, and they are different technologies answering different questions. A high-lift
blowing paper looks exactly like a laminar-flow suction paper until you read what it is for.

Several were removed on that ground, along with swept-wing flutter, a rolling-moment stability
derivative, internal pipe flow, a fuselage load distribution and an oscillatory flow reactor.

---

## Reported Rather Than Padded

**The Breguet and cruise-performance literature is thin here and stays thin.** Two usable records. The
relation is textbook material rather than journal material, and the word range in an aeronautical archive
mostly means the distance to a target or a ballistic test facility, so searching harder returns more of
those rather than more of this. The article says so.

**Slot metering and flow distribution remains at one record.** For the component that decides whether the
whole scheme installs, that is a genuine hole in the public literature and it is stated as one.

---

## Verification

- **824 references**, zero undefined, zero orphaned, zero duplicate URLs, `research_` block sorted
- **635 DOIs confirmed registered in the Crossref registry, 169 archive links at HTTP 200, zero failures
  of either kind**
- A residual red-flag scan over all 635 printed registry titles left **two deliberate keeps**, being
  Yuan's porous-wall transpiration analyses, which are canonical in this literature despite being pipe
  flow
- The 142 re-derivations from the earlier passes still pass unchanged
- All 22 articles clean, `_verify.py` at the 0-error 21-warning baseline, 22-article isolated build
  succeeding with 45 of 45 equations rendering as display math

**One hazard worth recording.** Rebuilding the master after a harvest changes display text for any record
that gains a title collision, which silently breaks link text in body prose already written. The
link-text invariant caught four; a repair pass now rewrites them from the master rather than failing.

---

## State

**A318 has had three of four passes.** The publication review is yours to prompt.

1,258 lines, 45 equations, 824 references, 9,628 words. Lines and equations remain below the series
bands and references are well above.

Nothing in the series is published. The publication-order dependency is twenty-two deep.

**Still open and unchanged.** The fourth genre class, now seven consecutive articles outside all four
named classes. The A305 length offer.
