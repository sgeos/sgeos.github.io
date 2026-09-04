## Last Updated

**Date**: 2026-09-04
**Task**: **A349, X-Planes: X-52, the Designation Refused, draft pass. The first of four.**
Committed, **not pushed**, since only the publication review pushes. **Not published**, and
publication of the series still not authorised. **Fifty-three of seventy-two drafted.**

---

## The Subject Is a Refusal and Not a Gap

**X-52A was requested in 2006, disapproved because of possible confusion with the B-52 series, and
X-53A was allocated to the programme instead.** The paperwork was done correctly and the answer was no.

**That is a different anomaly from A336's X-39**, where the allocation request was never submitted and
the number was lost to two missing documents. **Here nothing was lost.** The request was made,
considered, refused and answered on the same occasion, the programme got a designation, and the
register records why 52 is absent. **The cost of the refusal, measured in anything the designation
system exists to provide, is zero**, which is what makes it the cleanest case in the series for asking
what the rule is actually for.

---

## The Finding Came From Reading the Instruction, Not a Description of It

**The 14 April 2005 issue was read in full and it does not contain the rule that refused the number.**

- It directs that the coordinating office **assign the next available consecutive design number**.
- **It does not contain the word skip**, nor any discretion, nor any criterion for judging a number
  unsuitable.
- Its duplication check, its **trademark search** and its four levels of review apply to the
  **popular name**, which the same document calls an aid to communications and media references.
- The designation, which it calls **official**, is issued in sequence by a logistics office.
- **Its only written anti-confusion rule for a designator is that the series letters I and O are
  prohibited because they resemble the digits 1 and 0.**

**The 1994 issue says the same.** **The 3 November 2020 issue adds one sentence, at A2.1.6.1.2,
granting AF/A8PE the authority to skip a design number at discretion, with no criterion attached.**

**So the authority was absent for at least twenty-six years while the practice ran throughout them**,
and when it was finally written down it described a power rather than a test.

---

## The Same Office Had Manufactured the Same Collision Four Years Earlier

**F-35 was approved on 5 June 2002 by HQ USAF/XPPE**, which became AF/A8PE on 1 February 2006,
**against its own nomenclature office's recommendation of F-24A** made on the ground that design
numbers are assigned consecutively. The number came from a press conference, by replacing the X of
X-35 with an F.

**A cross-series numeric echo was desirable continuity in 2002 and a hazard in 2006**, under one
instruction that authorised neither. The article states the inconsistency as one of the system rather
than of any person, because the individuals need not have been the same.

---

## The Sharpest Thing in the Record Is an Asymmetry

**Q-7 and Q-8 were requested in 1953 to renumber two drones because they were ALREADY being confused
with the unmodified aircraft they were built from**, and the confusion was costing production time and
parts. **Both requests were refused in March 1954.**

**In 1954 the system declined to act although confusion was occurring. In 2006 it acted because
confusion might occur.**

---

## The Sweep Store Is Aeronautical and This Subject Is Not

**This is the first article in the series whose subject is not an aeroplane**, and the store noticed.

Applied untagged, the inherited store removed **310 records of which
188 were on subject**. Among them was an intervention study on look-alike and
sound-alike medication errors, **the single most on-subject title in the whole harvest**, and the
readback and hearback literature, both removed by a pattern reading patient or clinic.

**The store is not wrong. It is aeronautical.** Every medical pattern in it was earned because medicine
bleeds into aeroplane sweeps. **Refusing a proposed drug name because an approved name is near it is
the same administrative act as refusing X-52A because a B-52 exists.**

**3 tagged families covering 7 patterns are switched off by
name** through A348's mechanism. `homonyms.TAGS` now holds six. The store gained three new patterns and
stands at 124.

---

## The Filter Built to Protect the Survey Deleted Its Subject

**Biological nomenclature reached the kept set, as it had for A336, and component nomenclature had done
the same for A341**, so a pattern was written to remove the family for good.

**Its first version anchored on the phrase `generic name`, which is the taxonomic term and is also the
pharmacist's term for a nonproprietary drug name.** It deleted a paper on the hazards of illegible
prescriptions with look-alike and sound-alike trade and generic names. It also anchored on `taxonomy`,
deleting a controller-to-controller communication taxonomy and a cognitive error taxonomy.

**A filter built to remove naming-that-is-not-this-naming removed this-naming, and only reading its own
drops found it.**

---

## Three Further Defects Caught Before the Build

**A fabricated report identifier.** One of four foundational identifiers was written from a plausible
title rather than looked up and resolved to nothing. **That is the A347 defect exactly**, and it was
caught because every foundational identifier is verified before assembly. The correct source is better
than the invented one.

**A false superlative.** The article claimed the lowest report-primary fraction in the series. **A336
is lower, at zero of 2,454 records.** The claim is now a computed rank rather than a typed assertion,
and it reads **second-lowest of 53**.

**A heading contradicting its own section.** Correcting the superlative in the body left the heading
saying `Is the Lowest in the Series`. **That is the opening-against-conclusion defect at paragraph
scale**, and it was found by reading the assembled article rather than the source.

---

## Verification State

- `python3 _verify.py` reports **0 errors, 0 warnings**.
- `python3 _lib/test_lib.py` reports **104 of 104**, up from 102, with two new tests naming this
  article's failures. **The A348 tag test was changed from pinning the whole tag list to asserting
  presence**, because a test that fails when the store grows correctly teaches its reader to edit it
  without reading it.
- `tmp/a349/verify_numbers.py` reports **ALL CHECKS PASS**, with every survey statistic recomputed from
  the reference data, the cluster table matching its own citation runs, and claims written in words
  checked as words.
- Reference integrity: **2,046 defined, 2,046 used, 0 undefined,
  0 orphaned, 0 duplicate URLs**.
- Book links **four checked, zero mismatched**, verified on title AND author.
- Prose: no contractions, no dashes, no prose colons, no prose semicolons.
- **4,560 lines, 28,087 words, 13 display equations, 2,046 reference definitions.**
- Survey **1,968 research records across 10 clusters**, report primaries
  **36 at 1.8 percent**.
- **The stub-isolated production build succeeded in 22 seconds with no Liquid error**, against a
  checksum taken before the build and re-verified after it. **The rendered audit reports no findings
  across 88 pages.** Zero raw dollar pairs leak, zero unresolved reference brackets, page renders to
  435,333 bytes. The rendered `\[` count is 14 against 13 source equations **because one `cases`
  environment carries a `\[4pt]` line-spacing directive**, which was checked rather than assumed.

---

## One Thing to Carry Into the Next Build

**`tmp/a349/make_stub.sh` now symlinks `vendor` back into the stub.** The rsync excludes `vendor`, the
gems live in `vendor/bundle`, and A348 restored the link by hand without recording the step, so A349's
first build failed with every gem missing. **The recipe is now in the script rather than in a memory.**

---

## Next

**A349 has three passes remaining**, being the equation-density review, the primary-reference review
and the publication review, in that order and each on its own prompt.

**A350 is Boeing X-53 Active Aeroelastic Wing**, editorial date 2025-11-28, series index 54. **A349
deliberately leaves the aeroelastics alone**, names the programme and stops, so the roll-reversal
problem, the control laws and the flight-test results are all still available to it.
