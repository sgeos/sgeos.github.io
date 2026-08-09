# Handoff Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the resume prompt for an agent picking up after a compaction or a new session. It is a
snapshot, deliberately not kept current, and it self-reports as stale rather than misleading a
resuming agent. Read it first, validate it, then read the live channels.

---

## Validity

- **Branch**: `master`
- **Parent commit** (the repository state this handoff describes): `5a076cf`
- **Written**: 2026-08-08
- **Tree at write**: clean, nothing unpushed
- **Context**: the X-Planes series is IN PROGRESS. **Twenty-one of seventy-two articles drafted, all four
  passes complete on each. None published.**

**Validate before trusting.** Compare the recorded **Parent commit** to `git rev-parse HEAD~1`. Because
this handoff file is itself committed, its commit becomes the branch tip and its parent is the state
described.

- **Match → VALID.** Proceed per the resume prompt below.
- **Mismatch → INVALID and STALE.** A later commit moved the tip, so this file describes a state that
  is no longer current. Do **not** proceed and do **not** guess what changed. Report it as
  invalid-and-stale, familiarize from the live channels, namely `REVERSE_PROMPT.md`, `TASKLOG.md`,
  `_drafts/draft_summary.md`, and the git log, which are always authoritative, and wait for
  instruction.

---

## Resume prompt — the next prompt will be "Please draft A318, 'X-Planes: Northrop X-21.'"

**Nothing is outstanding.** A317 finished all four passes, is committed and pushed, its deploy
succeeded, and the article returns 404 while the site root returns 200, which is correct because
nothing in the series is published. There is no half-finished pass to pick up.

**Wait for the pilot's prompt. Do not begin A318 unprompted.**

**A318 is the Northrop X-21A**, editorial date 2025-10-27, Part 22 of 72. It is a WB-66D converted to
test **laminar flow control by suction through slotted wings**, and it is a different genre of subject
from the last two. A316 and A317 were both about vehicles that failed or were cancelled. The X-21
flew, worked in the sense that suction did laminarise the flow, and failed operationally because the
slots clogged with insects and ice.

**Expect the keystone to be the maintenance economics rather than the aerodynamics.** Laminar flow
control demonstrably works, which is not in dispute and was not in dispute then. Whether the drag saved
exceeds the suction power plus the cost of keeping several hundred thousand slots clean is the question
the programme actually answered, and it answered it in the negative for the technology of 1963. Compute
the suction power against the drag saving before deciding what the article is about, because the two are
the same order of magnitude and the sign of the difference is the whole story.

**Do not import the A317 pool.** Laminar flow control shares almost nothing with reentry heating. The
one-directory rule has now been followed for four consecutive articles and should be recorded in the
harvest docstring again.

---

## Where the Series Stands

Seventy-two articles, A297 through A368, back-dated one per day from 2025-10-06 to 2025-12-16, covering
every X-designation from X-1 through X-76.

**Twenty-one complete**, A297 through A317, all four passes each, all in `_drafts/`, **none published**.

| Article | Aircraft | Final state |
|---|---|---|
| A313 | Bell X-16 | 1,233 lines, 72 eq, 468 refs |
| A314 | Lockheed X-17 | 1,066 lines, 47 eq, 446 refs |
| A315 | Hiller X-18 | 935 lines, 29 eq, 418 refs |
| A316 | Curtiss-Wright X-19 | 1,200 lines, 78 eq, 431 refs |
| A317 | Boeing X-20 Dyna-Soar | 945 lines, 49 eq, 388 refs |

Read `_drafts/draft_summary.md` for per-article detail rather than re-deriving it.

---

## The Established Rhythm, Which Is the Most Important Thing Here

Four passes, each a separate prompt from the pilot. **Do not run ahead.**

1. **"Please draft Axxx, '<title>.'"** Research, write, verify, commit. **Do not push.**
2. **"Please review for equation density, and add all candidate equations."**
3. **"Please review for reference density, specifically primary references, and add all identified
   references."**
4. **"Please review for publication, and make suitable changes..."** This prompt also asks for a push.

After every pass, update `REVERSE_PROMPT.md`, `TASKLOG.md` and `_drafts/draft_summary.md`, and commit
them with the article in one commit.

---

## Standing Directive, Quoted Because It Governs Every Pass

The pilot quotes this verbatim on every publication-review prompt:

> Note that all articles in this series have no length limit, no reference limit, and that they should
> serve as a comprehensive survey and review of the contemporary literature in addition to any other
> stated goals. Finally, make sure that the draft has been committed and pushed, but do not yet publish
> it.

**No length limit and no reference limit are permissions, not instructions.** Do not pad to reach a
band. Five consecutive articles have finished short of the line and equation bands and were reported
that way.

---

## Method Rules Earned the Hard Way

### On the analysis

**Write the relation down.** This caught a wrong claim in **twelve consecutive articles**, A305 through
A316. A317 broke that run by catching an OMISSION instead, which is the other thing the pass is for. In
A316 the drafted pitch-moment relation was wrong by a factor of two while the value quoted beside it was
right, so the article contradicted itself and every automated check passed.

**An equation pass can catch omission rather than error, and the omission can be the article's own
central claim.** A317 asserted that peak heating is independent of lift-to-drag ratio and that the peak
falls at a particular speed, and displayed neither the maximisation nor the speed. The result was one
line of algebra away and materially stronger than what the draft claimed.

**Look for a cross-check between two quantities the article already has.** A317 assumed a lift
coefficient and separately derived a lift-to-drag ratio from a mission requirement. Newtonian impact
theory connects them, and they agreed to 2.3 percent from directions that share nothing. **Nothing
prompted that check except looking for one.**

**Computing further inside a pass can invert a conclusion written earlier in the same pass.** A317
expected to show that a thirty-minute heat load makes ablation impossible and found it entirely
buildable at five to twenty-four percent of vehicle weight, which moved the reason for the hot structure
from mass to reuse. Withdraw the earlier reading in the text rather than silently replacing it.

**Read calculation output for plausibility.** A315 produced a 454-knot crossover from a coefficient
sixty times too small. A316's first corridor returned 0.6 knots at every nacelle angle below 60 degrees
because the formulation was circular. A317's first ballistic comparison reported a heat-load ratio of
twelve thousand five hundred. **No automated check would have caught any of the three.**

**A named limit belongs in the article.** A316 stated where its in-plane momentum model stops deserving
belief and reported that five of ten corridor rows sit outside it.

**Do not assume the previous article's keystone transfers.** A316's was propeller normal force where
A315's was slipstream immersion, and the two share no quantity. A317's was neither of the heating
keystones the series already had.

### On harvesting and selection

**An equation pass promotes subjects, and the reference base must follow.** This is now the strongest
recurring rule in the series. A317's audit found five thin topics and they were EXACTLY the five the
equation pass had promoted, with **Newtonian impact theory at zero records** because the draft harvest
could not know that cross-check would come to exist.

**Distinguish a supply gap from a selection gap. Both can be present at once.** A316 had both in
different topics. Deep-and-unused needs spreading, not searching.

**Read the selection. A title regex is not a substitute.** Across A316 and A317, more than fifty
candidates were rejected after being read and almost none by any rule.

**HOMONYM FAMILIES ARE NOW THE DOMINANT FAILURE MODE.** Documented cases, all correct words in the wrong
field:

| Phrase | The other field |
|---|---|
| propeller in oblique inflow | naval architecture, a ship screw in a hull wake |
| impact theory | spectroscopy, collisional line broadening |
| terminal area | aviation, the airspace around an airport |
| radiative cooling | building physics, emitting to the sky to cool a house |
| cellular structure | biology, cells rather than honeycomb core |
| gearbox | industrial condition monitoring |
| open water | marine propeller testing |

**Filter on the VENUE, not only the title.** `gen_master.py` carries a `venue` field for this. It is the
only thing that separated eight marine propeller papers from aerospace ones in A316, since one of them
contained no marine word in its title at all. **Archive records carry no venue, so the title must do the
work there.**

**Word boundaries fail in BOTH directions.** `ram` matched inside `fRAMework` and `ising` inside
`ARISING`, so the rule was to add boundaries. Then `\btextile\b` failed against TEXTILES and let a paper
about clothing into A317. Both are the same mistake, which is trusting a pattern instead of reading what
it returned.

**Read the REJECTED list, not only the accepted one.** A316's first venue rule listed the bare token
`navigation` and discarded the entire AIAA Guidance, Navigation and Control series, including an
energy-optimal speed profile for a tandem tilt-wing aircraft, which was that article's exact
configuration. Fifteen records were recovered by narrowing it.

**The persisted rejection list is at `tmp/aNNN/read_and_dropped.json` and MUST be carried forward.**
A317 found four references rejected by reading in the draft pass reappearing in the primary pass,
because each pass rebuilt its rejection list from scratch. Copy the file forward and load it in every
selector.

**The Crossref registry check catches wrong citations as a side effect of verifying links**, because it
prints titles. It has now done so twice, finding a diver's wetsuit in A315's sweep and a cell-biology
paper in A317's. Read what it prints.

### On tooling

**A stale script from the previous article can execute itself.** A317's working directory contained
`select.py` copied from A316. Python imported it in place of the standard library `select` module,
it ran on import, and it **overwrote the article's reference selection with output computed for a
tilt-propeller aircraft**. Rename or delete copied scripts that share a name with a standard module.

**Copied scripts keep the previous article's constants.** A316's isolated build arrived with eighteen
predecessor stubs where nineteen were needed, so the `post_url` to A315 had no target and the whole build
failed. **The stub list grows by one every article.** A317's `ref_audit.py` ran with A316's propeller
topics against a spaceplane. **Grep every copied script for the previous article's identifiers and read
what comes back.**

**Two-clause checks need both clauses changed.** `isolated_build.sh` has a navigation test of the form
`"Part N of N" in html or "Part N" in html`. A314 shipped with one clause repointed and one not.

**Know the expected number, not just pass or fail.** A317's `_verify.py` reported zero errors and **zero
warnings** against a baseline of zero and twenty-one, because it had inherited a scratch working
directory and checked nothing. **Absolute paths in every command issued after a `cd`.** This defect has
now recurred six times.

**Measure the equation count before and after any section work, and extend sections in place.**

**When a check finds a defect class, harden the checker.** `check.py` now fails on unterminated display
math, added after A316's equation pass introduced one, and on a missing series section, added after A316
shipped three passes without a Contemporary Literature section. **The second fix failed A317's draft on
its first run**, catching in minutes what had survived three passes before.

---

## Verification Toolchain

**`tmp/*` IS GITIGNORED, so none of this survives a fresh clone and all of it is rebuilt per article by
copying the previous article's directory and repointing.** That is why the endpoints below are embedded
here rather than referenced.

| Script | Purpose |
|---|---|
| `harvest.py`, `harvest2.py`, `harvest3.py` | archive sweeps; the second fills audit gaps, the third is the publication-review contemporary sweep |
| `ntrs_detail.py` | per-record NTRS metadata, since search returns only id and title |
| `gen_master.py` | build the master reference index; **carries a `venue` field, added in A316** |
| `gen_refs.py` | emit the reference section from anchors the body uses; enforces the link-text invariant |
| `ref_audit.py` | coverage audit by source, era and topic; **run it BEFORE selecting** |
| `select.py`, `select2.py` | candidate selection; **rename on copy, `select` shadows a standard module** |
| `read_and_dropped.json` | **persisted read-and-drop decisions; carry forward and load in every selector** |
| `check.py` | style and integrity; front matter, prose rules, section order, the three series sections, unterminated math |
| `calc.py`, `calc2.py` | the article's physics; calc2 carries the equation pass |
| `verify_numbers.py` | independent re-derivation of every quoted value AND a check that each appears in the text |
| `url_check.py` | external URL sweep with Crossref registry fallback |
| `isolated_build.sh` | real Jekyll build in a scratch tree with predecessors as stubs |
| `eqn_scan.py` | per-section words, equations and numeric literals |

### The Endpoints, Embedded Because the Scripts Are Not Committed

- **NTRS search** — `https://ntrs.nasa.gov/api/citations/search?q=<terms>`, and per-record detail at
  `https://ntrs.nasa.gov/api/citations/<id>`. **Cite `https://ntrs.nasa.gov/citations/<id>`, never a
  search URL.**
- **DTIC** — reached through Crossref with `filter=prefix:10.21236`. Cite `https://doi.org/<doi>`.
- **OSTI** — `https://www.osti.gov/api/v1/records?q=<terms>&publication_date_end=<date>&rows=<n>`.
  Cite `https://www.osti.gov/biblio/<id>`.
- **Crossref** — `https://api.crossref.org/works?query.bibliographic=<terms>` with
  `filter=from-pub-date:...,until-pub-date:...,type:journal-article`, and
  `https://api.crossref.org/works/<doi>` to verify a single identifier. The response carries
  `container-title`, which is the venue the selector filters on.

### The Corpus Checks

`python3 _verify.py` from the **repository root**, and `--strict` to treat warnings as errors. The same
checks run in CI before every build and in the local hook at `_hooks/pre-push`, which is enabled with
`git config core.hooksPath _hooks` and bypassed with `--no-verify`. **The baseline is 0
errors and 21 warnings**, all pre-existing in other articles. Any new warning is yours, and **a reading
of 0 warnings means the check did not run against the corpus.**

**Archive behaviours that will otherwise waste time.** NTRS caps at ten results and is phrasing
sensitive, so use short period vocabulary. NTRS author metadata arrives as a dict. Publication year is
in `publications[0].publicationDate`. **DTIC DOIs redirect correctly and then land on `www.dtic.mil`,
which refuses automated connections, so verify them through the Crossref registry instead** — asking
whether the identifier is registered and what title it carries is strictly stronger than an HTTP 200.
Publisher 403s from bot detection are normal and numerous.

**An HTTP 200 does not verify a citation** and no sweep in this series claims it does.

**Independence matters.** `verify_numbers.py` must not import the calculation module. A317's uses an
exponential atmosphere where the model uses tabulated layers, Simpson where it uses trapezoid, and
closed-form maximisation where it searches numerically.

---

## Open Decisions

**Categories — SETTLED 2026-08-08, at the pilot's discretion.** The answer is
`aerospace history engineering`, which all twenty-one drafts carry. **Do not revisit it and do not raise
it again.**

**A315 CARRIES FOUR WRONG CITATIONS AND THE PILOT HAS BEEN OFFERED THE FIX TWICE.** A315 cites four
naval-architecture papers as aircraft propeller literature, being a David Taylor Model Basin study of
spindle torque on a controllable-pitch ship propeller, the open-water characteristics of a propeller for
LSD-41 which is a dock landing ship, wing sails for wind-assisted ship propulsion, and cavitation of a
propeller under a non-uniform wake. **A315's `REVERSE_PROMPT.md` also describes the first of those as
"directly about the system that failed on the final flight," which it is not.** The correction is four
anchors and one sentence. **Do not make it unprompted**, since A315 is a completed article outside the
current work, but raise it.

**A fourth genre class.** `_docs/writing/RESEARCH_AIRCRAFT_STRUCTURE.md` names four classes. **A313
through A317 have each finished outside all of them on two of three measures, in the same direction,
across twenty passes.** References land in or above band while lines and equations land well below.
**Do not amend the genre document unprompted**, since it defines the series' own standards, but offer to
propose a fourth class with bands drawn from those five.

**A305 length.** An offered cut of roughly 300 lines and 25 equations was never taken up. The offer
stands. **Do not act on it unprompted.**

---

## Governing Rules That Are Easy to Lose

**The `post_url` interlock.** A `post_url` tag whose target is absent fails the **entire** site build.
Cross-references are **back-reference only**, never forward. The publication-order dependency is
**twenty-one deep**, A317 back to A297, so these articles publish in order or together.

**Pushing drafts is safe.** The deploy workflow builds without `--drafts`, so a pushed draft does not
appear on the live site. Confirm after every push that the article returns 404 while the site root
returns 200. **A 503 on the site root immediately after a deploy is transient; retry before reporting
it.**

**The two-commit publication pattern** applies when publishing eventually happens. Nothing in this
series is published and no publication has been authorised.

**Prose style is absolute.** No contractions, em dashes, en dashes, prose colons, prose semicolons, or
prose parentheticals. **A possessive is not a contraction.** The `console.log` debug tag is the only
permitted parenthesis.

**Every article carries** an `<!-- Axxx -->` comment and a `<script>console.log("Axxx");</script>` tag
immediately after the front matter.

**The genre carries three sections beyond the standard twelve**, being Comparison With Ground
Prediction, The Contemporary Literature, and The Source Base, the last immediately before Epistemic
State. `check.py` now enforces all three.

**Density conventions are absolute counts, not ratios.**

**Irreversible or outward-facing actions need confirmation.** Pushing is authorised only by the
publication-review prompt. Publishing has never been authorised.

**Report faithfully.** If a check fails, say so with the output. If a figure is assumed, say it is
assumed. If a band is missed, report the miss rather than padding toward it.

## The Roster, Embedded Because the Working Copy Is Gitignored

The pilot accepted a gitignored roster at `tmp/xplane_table.md`, which matches `.gitignore`. It is
reproduced here so it survives a clean checkout.

| Date | Article | Title |
|------|---------|-------|
| 2025-10-06 | A297 | X-Planes: Framing and the Research Aircraft Model |
| 2025-10-07 | A298 | X-Planes: Bell X-1 |
| 2025-10-08 | A299 | X-Planes: Bell X-2 |
| 2025-10-09 | A300 | X-Planes: Douglas X-3 Stiletto |
| 2025-10-10 | A301 | X-Planes: Northrop X-4 Bantam |
| 2025-10-11 | A302 | X-Planes: Bell X-5 |
| 2025-10-12 | A303 | X-Planes: Convair X-6 |
| 2025-10-13 | A304 | X-Planes: Lockheed X-7 |
| 2025-10-14 | A305 | X-Planes: Aerojet X-8 Aerobee |
| 2025-10-15 | A306 | X-Planes: Bell X-9 Shrike |
| 2025-10-16 | A307 | X-Planes: North American X-10 |
| 2025-10-17 | A308 | X-Planes: Convair X-11 |
| 2025-10-18 | A309 | X-Planes: Convair X-12 |
| 2025-10-19 | A310 | X-Planes: Ryan X-13 Vertijet |
| 2025-10-20 | A311 | X-Planes: Bell X-14 |
| 2025-10-21 | A312 | X-Planes: North American X-15 |
| 2025-10-22 | A313 | X-Planes: Bell X-16 |
| 2025-10-23 | A314 | X-Planes: Lockheed X-17 |
| 2025-10-24 | A315 | X-Planes: Hiller X-18 |
| 2025-10-25 | A316 | X-Planes: Curtiss-Wright X-19 |
| 2025-10-26 | A317 | X-Planes: Boeing X-20 Dyna-Soar |
| 2025-10-27 | A318 | X-Planes: Northrop X-21 |
| 2025-10-28 | A319 | X-Planes: Bell X-22 |
| 2025-10-29 | A320 | X-Planes: Martin Marietta X-23 PRIME and a Contested Assignment |
| 2025-10-30 | A321 | X-Planes: Martin Marietta X-24 |
| 2025-10-31 | A322 | X-Planes: Bensen X-25 |
| 2025-11-01 | A323 | X-Planes: Schweizer X-26 Frigate |
| 2025-11-02 | A324 | X-Planes: Lockheed X-27 |
| 2025-11-03 | A325 | X-Planes: Osprey X-28 Sea Skimmer |
| 2025-11-04 | A326 | X-Planes: Grumman X-29 |
| 2025-11-05 | A327 | X-Planes: Rockwell X-30 and the National Aero-Space Plane |
| 2025-11-06 | A328 | X-Planes: Rockwell-MBB X-31 |
| 2025-11-07 | A329 | X-Planes: Boeing X-32 |
| 2025-11-08 | A330 | X-Planes: Lockheed Martin X-33 |
| 2025-11-09 | A331 | X-Planes: Orbital Sciences X-34 |
| 2025-11-10 | A332 | X-Planes: Lockheed Martin X-35 |
| 2025-11-11 | A333 | X-Planes: McDonnell Douglas X-36 |
| 2025-11-12 | A334 | X-Planes: Boeing X-37 |
| 2025-11-13 | A335 | X-Planes: Scaled Composites X-38 |
| 2025-11-14 | A336 | X-Planes: X-39, Reserved but Never Assigned |
| 2025-11-15 | A337 | X-Planes: Boeing X-40 |
| 2025-11-16 | A338 | X-Planes: X-41 Common Aero Vehicle |
| 2025-11-17 | A339 | X-Planes: Orbital Sciences X-42 |
| 2025-11-18 | A340 | X-Planes: Micro-Craft X-43 Hyper-X |
| 2025-11-19 | A341 | X-Planes: X-44, One Designation and Two Aircraft |
| 2025-11-20 | A342 | X-Planes: Boeing X-45 |
| 2025-11-21 | A343 | X-Planes: Boeing X-46 |
| 2025-11-22 | A344 | X-Planes: Northrop Grumman X-47 |
| 2025-11-23 | A345 | X-Planes: Boeing X-48 |
| 2025-11-24 | A346 | X-Planes: Piasecki X-49 SpeedHawk |
| 2025-11-25 | A347 | X-Planes: Boeing X-50 Dragonfly |
| 2025-11-26 | A348 | X-Planes: Boeing X-51 Waverider |
| 2025-11-27 | A349 | X-Planes: X-52, the Designation Refused |
| 2025-11-28 | A350 | X-Planes: Boeing X-53 Active Aeroelastic Wing |
| 2025-11-29 | A351 | X-Planes: Gulfstream X-54 |
| 2025-11-30 | A352 | X-Planes: Lockheed Martin X-55 ACCA |
| 2025-12-01 | A353 | X-Planes: Lockheed Martin X-56 |
| 2025-12-02 | A354 | X-Planes: ESAero X-57 Maxwell |
| 2025-12-03 | A355 | X-Planes: X-58, the Slot Taken by XQ-58 |
| 2025-12-04 | A356 | X-Planes: Lockheed Martin X-59 Quesst |
| 2025-12-05 | A357 | X-Planes: Generation Orbit X-60 |
| 2025-12-06 | A358 | X-Planes: Dynetics X-61 Gremlins |
| 2025-12-07 | A359 | X-Planes: Lockheed Martin X-62 VISTA |
| 2025-12-08 | A360 | X-Planes: ABL Space Systems X-63 |
| 2025-12-09 | A361 | X-Planes: Invocon X-64 |
| 2025-12-10 | A362 | X-Planes: Aurora Flight Sciences X-65 CRANE |
| 2025-12-11 | A363 | X-Planes: Boeing X-66 |
| 2025-12-12 | A364 | X-Planes: X-67, the Slot Taken by XQ-67A |
| 2025-12-13 | A365 | X-Planes: General Atomics X-68 LongShot |
| 2025-12-14 | A366 | X-Planes: X-69 through X-75, the Leapfrogged Block |
| 2025-12-15 | A367 | X-Planes: Bell Textron X-76 SPRINT |
| 2025-12-16 | A368 | X-Planes: Synthesis and What the Designation Became |

## The Nine Anomaly Cases

Short articles by design, and the evidence for the closing article. The designation system is not a
counter.

- **X-23** — attributed to the Martin Marietta SV-5D PRIME, but USAF nomenclature records reportedly
  show X-23A was never assigned. State the conflict, do not resolve it.
- **X-39** — reserved 23 April 1997 for the AFRL Future Aircraft Technology Enhancements programme;
  no written allocation request followed.
- **X-41** — still-classified vehicle in the DARPA FALCON programme. No specifications released.
- **X-42** — sources disagree, one calling it an expendable upper stage and another a spaceplane test
  vehicle. No dedicated treatment exists anywhere.
- **X-44** — two different aircraft, the Lockheed Martin MANTA and a separate unmanned programme.
- **X-52** — requested 2006, refused over possible confusion with the B-52. The programme became X-53.
- **X-58** — skipped; slot consumed by the Kratos XQ-58 Valkyrie.
- **X-67** — skipped; slot consumed by the General Atomics XQ-67A.
- **X-69 to X-75** — unassigned and leapfrogged.

X-58 and X-67 were lost to the **parallel XQ- unmanned series drawing from the same numeric pool**,
which is a genuine finding about how the system evolved and belongs in the closer.

## Writing a New Handoff

Overwrite this file before a planned compaction, or when the pilot asks for a handoff. Then:

1. Set **Parent commit** to the current `HEAD`, because the handoff commit becomes the new tip and the
   state described is its parent.
2. Set **Branch**, **Written**, and **Tree at write** from the observed state. Read it; do not carry
   forward a remembered value.
3. Replace the resume prompt with what a fresh agent must know that the live channels do not say.
   Prefer pointers to on-disk sources over restating them, but **embed anything that lives only in a
   gitignored path**.
4. Carry forward open concerns, earned method rules, and governing constraints. Drop anything resolved.
5. Commit it as the tip. If anything lands afterward, the validity check will report it stale.

A handoff that is merely a summary of the resume channels is not worth writing. Its value is the
imperative direction and the hard-won rules that a summary would smooth away.
