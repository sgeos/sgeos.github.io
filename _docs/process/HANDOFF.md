# Handoff Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the resume prompt for an agent picking up after a compaction or a new session. It is a
snapshot, deliberately not kept current, and it self-reports as stale rather than misleading a
resuming agent. Read it first, validate it, then read the live channels.

---

## Validity

- **Branch**: `master`
- **Parent commit** (the repository state this handoff describes): `01e39c7`
- **Written**: 2026-08-09
- **Tree at write**: clean, nothing unpushed
- **Context**: the X-Planes series is IN PROGRESS. **Twenty-three of seventy-two articles drafted, all
  four passes complete on each. None published.**

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

## Resume prompt — the next prompt will be "Please draft A320, 'X-Planes: Martin Marietta X-23 PRIME.'"

**Nothing is outstanding.** A319 finished all four passes, is committed and pushed, its deploy
succeeded, and the article returns 404 while the site root returns 200, which is correct because
nothing in the series is published. There is no half-finished pass to pick up.

**Wait for the pilot's prompt. Do not begin A320 unprompted.**

**A320 IS THE FIRST OF THE NINE ANOMALY CASES AND MUST BE HANDLED AS ONE.** Editorial date 2025-10-29,
Part 24 of 72. The designation is attributed to the Martin Marietta SV-5D PRIME, but United States Air
Force nomenclature records reportedly show that X-23A was never formally assigned. **State the conflict,
do not resolve it.** The anomaly cases are the evidence for the closing article's argument that the
designation system is not a counter, and an article that tidies the conflict away destroys the evidence.

**The vehicle is a lifting body flown on a ballistic reentry from an Atlas**, which puts it back with the
[X-17][a314] and [X-20][a317] rather than with the V/STOL family. **Do not import the A319 pool.** Ducted
propellers share nothing with lifting-body reentry. The one-directory rule has now held for seven
consecutive articles.

[a314]: https://en.wikipedia.org/wiki/Lockheed_X-17
[a317]: https://en.wikipedia.org/wiki/Boeing_X-20_Dyna-Soar

**Expect the keystone to be crossrange at low lift-to-drag ratio.** PRIME was flown to demonstrate
precision recovery from orbital reentry, and a lifting body of L/D near 1 buys a few hundred miles of
crossrange rather than the seventeen hundred the [X-20][a317] wanted. Compute what L/D near unity
actually gives before deciding what the article is about, because the whole point of the vehicle was that
a small amount of lift is worth a great deal compared with none.

---

## Where the Series Stands

Seventy-two articles, A297 through A368, back-dated one per day from 2025-10-06 to 2025-12-16, covering
every X-designation from X-1 through X-76.

**Twenty-three complete**, A297 through A319, all four passes each, all in `_drafts/`, **none published**.

| Article | Aircraft | Final state |
|---|---|---|
| A315 | Hiller X-18 | 937 lines, 29 eq, 420 refs |
| A316 | Curtiss-Wright X-19 | 1,200 lines, 78 eq, 431 refs |
| A317 | Boeing X-20 Dyna-Soar | 944 lines, 49 eq, 387 refs |
| A318 | Northrop X-21 | 1,692 lines, 45 eq, 1,192 refs |
| A319 | Bell X-22 | 1,891 lines, 25 eq, 1,472 refs |

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
band. Seven consecutive articles have finished short of the equation band and were reported that way.

---

## Method Rules Earned the Hard Way

### On the analysis

**Write the relation down.** This has now caught a wrong claim in fourteen articles. In A318 the draft
assumed a whole-aircraft zero-lift drag coefficient that implies a form factor and then credited the
laminarised area a flat-plate saving without one, so the aeroplane was **charged one way and credited
another**, understating the benefit by a quarter. Building the coefficient from its parts reproduced the
assumed value to three figures, which is the check that the decomposition is right.

**A NUMBER THAT IS NOT CREDIBLE IS A FINDING, NOT A NUISANCE.** A319's derived corridor produced a duct
normal force of 2.26 times the aircraft weight. That is unflyable and unmissable, so the model is wrong
there, and asking where it stops being right produced the validity parameter and the conclusion that
**the momentum model is valid at both ends of the conversion and invalid in the middle, which is exactly
where the aircraft is hard to fly**. The bad number was worth more than a plausible one.

**"The article cannot compute this" is usually giving up too early.** A318 said its corridor could not be
computed for want of wing areas. The conversion speed implies the wing area, because the wings carry the
whole weight at the end of a conversion, and the implied chords then check against the spans. Look for
the quantity the article already knows that fixes the one it does not.

**Look for a cross-check between two quantities the article already has.** A318's opening claim that half
a transport's fuel goes to skin friction was met by 45.6 percent computed from geometry and a flat-plate
correlation. A319's quoted 35 percent excess power fixed a figure of merit that then predicted the
separately quoted three-engine hover weight to 0.83 percent. **Nothing prompted either check except
looking for one.**

**A quoted margin may be a minimum rather than a margin.** A319's 35 percent excess power leaves three
quarters of 1.35, which is 1.25 percent, after an engine fails. The number was chosen so that three
engines would just do.

**Read calculation output for plausibility.** A319's first normal-force table contained a duct at 45
degrees at 200 feet per second, which is not a flight condition, and reported a force larger than the
aeroplane. **Evaluate along a schedule, not on a grid.**

**A named limit belongs in the article**, including the boundary of the model's own validity.

### On harvesting and selection

**An equation pass promotes subjects, and the reference base must follow.** This is the strongest
recurring rule in the series and A319 produced its clearest instance yet. Nine subjects were promoted,
**all nine were thin and four were at zero records.** The draft harvest cannot know which derivations
will come to exist.

**THE ERA GAP IS A SELECTION PROBLEM, NOT A SUPPLY PROBLEM, AND THIS IS NOW A RULE BECAUSE IT HAPPENED
TWICE.** In A318 period sources stood at 12.5 percent and 417 records dated 1970 or earlier were sitting
in the pool unused. In A319 they stood at 15.0 percent with the same cause. **A broad cluster placed
early eats the foundational literature and the coverage audit then reports a supply gap that does not
exist.** The fix both times was one move, placing a dedicated period cluster after the specific topics
and before the broad ones, which recovered 253 records in A318 and 376 in A319.

**Read the selection. A title regex is not a substitute.** Across A318 and A319 more than a hundred
candidates were rejected after being read.

**HOMONYM FAMILIES ARE THE DOMINANT FAILURE MODE AND SOME ARE INTERNAL TO THE DISCIPLINE.**

| Phrase | The other field |
|---|---|
| ablation | medicine, the pituitary gland and tumours; materials, laser ablation for nanotubes |
| boundary layer | meteorology, the atmospheric boundary layer. One query returned most of a journal |
| laminar flow | operating-room ventilation, chromatography, co-laminar fuel cells, coal-cleaning cyclones |
| ducted propeller | naval architecture, the Kort nozzle; wind energy, the diffuser-augmented turbine |
| propeller in oblique inflow | naval architecture, a ship screw in a hull wake |
| impact theory | spectroscopy, collisional line broadening |
| terminal area | aviation, the airspace around an airport |
| radiative cooling | building physics, emitting to the sky to cool a house |
| cellular structure | biology, cells rather than honeycomb core |
| open water | marine propeller testing |
| **boundary layer control** | **aeronautics itself.** Suction for laminar flow and drag, or blowing for lift |
| **trim** | **aeronautics itself.** Aircraft balance, interior fittings, engine setting, planing attitude |
| **figure of merit** | **engineering itself.** Rotor hover efficiency, and nuclear-radiation detectors |
| **electric propulsion** | **aerospace itself.** Aircraft motors, and spacecraft ion thrusters |
| inlet | coastal geomorphology, the channel between barrier islands |
| hovering | underwater vehicle station-keeping |

**The internal ones are the dangerous ones**, because the venue does not separate them and the authors
are often the same people.

**Filter on the VENUE, not only the title.** `gen_master.py` carries a `venue` field. **Archive records
carry no venue, so the title must do the work there.**

**Word boundaries fail in BOTH directions, and A318 did both in one pass.** A pattern for the
transition-prediction method matched those two letters inside ordinary English words and swelled a
cluster to 362 records. A pattern for ducting matched the middle of the word **re-duct-ion** and put 73
drag papers into the pumping cluster.

**The persisted rejection list is at `tmp/aNNN/read_and_dropped.json` and MUST be carried forward.** It
now holds 388 entries. Copy it forward and load it in every selector.

**The Crossref registry check catches wrong citations as a side effect of verifying links**, because it
prints titles. Read what it prints. It has now caught something in every article that used it.

**OSTI is not worth querying for this subject.** One record of 49 was usable. The Department of Energy
corpus uses these words for other things.

**Crossref correction, erratum and withdrawn notices are not the paper.** Filter them at build time.

### On tooling

**`check_any.py` REPLACES the per-article `check.py`.** It lives at `tmp/errata/check_any.py`, takes any
draft path or defaults to all of them, derives the article number from the `<!-- Axxx -->` marker, and
validates date and series index against the roster. That is **strictly stronger** than the four
hardcoded constants the old script carried, which arrived stale twice.

**`build_check.sh` derives the article count from the roster.** It lives at `tmp/errata/build_check.sh`
and stages every X-Planes draft as a post so all in-series `post_url` tags resolve against real
articles. **There is no stub list to arrive one short**, which was the A316 failure.

**Rebuilding the master after a harvest changes display text** for any record that gains a title
collision, which silently breaks link text in body prose already written. The link-text invariant catches
it; a repair pass rewrites body link text from the master rather than failing.

**The NTRS search endpoint returns no authors and no year.** Both come from the per-record detail
endpoint. Falling back to a title fragment produces link text like "Tests of the" and drags title
punctuation into prose, which then fails the style rules.

**A stale script from the previous article can execute itself.** Rename or delete copied scripts sharing
a name with a standard module. `select.py` shadowed the standard library once and destroyed a work
product.

**Know the expected number, not just pass or fail.** `_verify.py` once reported zero warnings against a
21-warning baseline because it inherited a scratch working directory. **Absolute paths in every command
issued after a `cd`.**

**THE VERIFIER CAN BE THE THING THAT IS WRONG.** A318's wedge-area integration disagreed with the article
by exactly two because the verifier integrated the half-width of a wedge that spreads at a half-angle on
each side. A319's peak-speed check expected the tabulated maximum rather than the continuous one. **A
clean factor or a small offset is a hint that the checker is at fault.**

**Measure the equation count before and after any section work, and extend sections in place.** Replacing
a section is permitted only where it is an explicit placeholder, and the count is measured regardless.

---

## Verification Toolchain

**`tmp/*` IS GITIGNORED, so none of this survives a fresh clone.** The per-article scripts are rebuilt by
copying the previous article's directory and repointing. The two cross-article scripts live in
`tmp/errata/` and are not article-specific.

| Script | Purpose |
|---|---|
| `tmp/errata/check_any.py` | style and integrity for any or all articles, identity derived and roster-validated |
| `tmp/errata/build_check.sh` | real Jekyll build of every draft staged as a post, count derived from the roster |
| `harvest.py`, `harvest2.py`, `harvest3.py` | archive sweeps; the second closes audit gaps, the third is the publication-review contemporary sweep |
| `ntrs_detail.py` | per-record NTRS metadata, incremental; **search returns no authors** |
| `gen_master.py` | master reference index; carries `venue`, applies the rejection list, drops corrections |
| `gen_refs.py` | emit the reference section from anchors the body uses; enforces the link-text invariant |
| `ref_audit.py` | coverage by topic, era and source; **run it BEFORE selecting** |
| `pick.py` | cluster selection; **not named `select.py`, which shadows a standard module** |
| `read_and_dropped.json` | persisted read-and-drop decisions; carry forward, now 388 entries |
| `calc.py`, `calc2.py` | the article's physics; calc2 carries the equation pass |
| `verify_numbers.py`, `verify_numbers2.py` | independent re-derivation, and a check that each value appears in the text |
| `url_check.py` | external sweep; Crossref registry for DOIs, HTTP for archives, **prints titles** |

### The Endpoints, Embedded Because the Scripts Are Not Committed

- **NTRS search** — `https://ntrs.nasa.gov/api/citations/search?q=<terms>`, per-record detail at
  `https://ntrs.nasa.gov/api/citations/<id>`. **Cite `https://ntrs.nasa.gov/citations/<id>`, never a
  search URL.** Caps at ten results and is phrasing sensitive, so **use short period vocabulary**. Author
  metadata is a dict under `authorAffiliations`; the year is in `publications[0].publicationDate`.
- **DTIC** — through Crossref with `filter=prefix:10.21236`. Cite `https://doi.org/<doi>`. **DTIC DOIs
  redirect correctly and then land on `www.dtic.mil`, which refuses automated connections, so verify
  through the Crossref registry**, which is strictly stronger than an HTTP 200.
- **OSTI** — `https://www.osti.gov/api/v1/records?q=<terms>&publication_date_end=<date>&rows=<n>`.
  **Not worth using for this subject.**
- **Crossref** — `https://api.crossref.org/works?query.bibliographic=<terms>` with
  `filter=from-pub-date:...,until-pub-date:...,type:journal-article`, and
  `https://api.crossref.org/works/<doi>` for one identifier. The response carries `container-title`,
  which is the venue the selector filters on. Use a polite-pool `mailto` and retry on 429.

### The Corpus Checks

`python3 _verify.py` from the **repository root**, `--strict` to treat warnings as errors. The same checks
run in CI and in the local hook at `_hooks/pre-push`, enabled with `git config core.hooksPath _hooks` and
bypassed with `--no-verify`. **The baseline is 0 errors and 21 warnings**, all pre-existing in other
articles. **A reading of 0 warnings means the check did not run against the corpus.**

**The bundle is installed** at `vendor/bundle`, which is gitignored. It was never broken, merely never
installed. An isolated build whose source tree is elsewhere needs `BUNDLE_GEMFILE` pointed back at the
repository.

**An HTTP 200 does not verify a citation** and no sweep in this series claims it does.

**Independence matters.** `verify_numbers.py` must not import the calculation module. Use a tabulated
atmosphere where the model uses a formula, bisection where it uses a closed form, numerical integration
where it uses an area formula, and forward substitution to check anything obtained by inverting.

---

## Open Decisions

**Categories — SETTLED and not to be revisited.** `aerospace history engineering`, which all
twenty-three drafts carry.

**A315's wrong citations — RESOLVED 2026-08-09.** The errata pass corrected them and eleven more across
the corpus. **Do not raise this again.**

**A fourth genre class.** `_docs/writing/RESEARCH_AIRCRAFT_STRUCTURE.md` names four classes. **A313
through A319 have each finished outside all of them on two of three measures, in the same direction,
across twenty-eight passes.** References land far above band while lines and equations land below. **Do
not amend the genre document unprompted**, since it defines the series' own standards, but offer to
propose a fourth class with bands drawn from those seven.

**A305 length.** An offered cut of roughly 300 lines and 25 equations was never taken up. The offer
stands. **Do not act on it unprompted.**

---

## Governing Rules That Are Easy to Lose

**The `post_url` interlock.** A `post_url` tag whose target is absent fails the **entire** site build.
Cross-references are **back-reference only** within the series. The publication-order dependency is
**twenty-three deep**, A319 back to A297, so these articles publish in order or together. **Links to
other series are necessarily forward-dated**, because the whole run is back-dated to 2025 while much of
the corpus is 2026, and that is not a defect; what matters is that the target exists and is not itself
dated past today.

**Pushing drafts is safe.** The deploy workflow builds without `--drafts`. Confirm after every push that
the article returns 404 while the site root returns 200. **A 503 on the root immediately after a deploy
is transient; retry before reporting it.**

**The two-commit publication pattern** applies when publishing eventually happens. Nothing in this series
is published and no publication has been authorised.

**Prose style is absolute.** No contractions, em dashes, en dashes, prose colons, prose semicolons, or
prose parentheticals. **A possessive is not a contraction.** The `console.log` debug tag is the only
permitted parenthesis. **Link text is prose**, so citation display strings must carry none of it either.

**Every article carries** an `<!-- Axxx -->` comment and a `<script>console.log("Axxx");</script>` tag
immediately after the front matter.

**The genre carries three sections beyond the standard twelve**, being Comparison With Ground Prediction,
The Contemporary Literature, and The Source Base, the last immediately before Epistemic State.
`check_any.py` enforces all three and exempts the series opener, which has its own shape.

**Density conventions are absolute counts, not ratios.**

**Report the count as well as the fraction.** Adding a contemporary survey lowers the period *fraction*
while leaving the period *count* unchanged, and saying only the fraction reads as a regression when it is
the directive working.

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
