# Handoff Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the resume prompt for an agent picking up after a compaction or a new session. It is a
snapshot, deliberately not kept current, and it self-reports as stale rather than misleading a
resuming agent. Read it first, validate it, then read the live channels.

---

## Validity

- **Branch**: `master`
- **Parent commit** (the repository state this handoff describes): `b77cfba`
- **Written**: 2026-08-09
- **Tree at write**: clean, nothing unpushed
- **Context**: the X-Planes series is IN PROGRESS. **Twenty-five of seventy-two articles drafted, all
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

## Resume prompt — the next prompt will be "Please draft A322, 'X-Planes: Bensen X-25.'"

**Nothing is outstanding.** A321 finished all four passes, is committed and pushed, its deploy
succeeded, and the article returns 404 while the site root returns 200, which is correct because
nothing in the series is published. There is no half-finished pass to pick up.

**Wait for the pilot's prompt. Do not begin A322 unprompted.**

**A322 IS THE SHARPEST SUBJECT BREAK IN THE SERIES SO FAR.** Editorial date 2025-10-31, Part 26 of 72.
The Bensen X-25 is a **one-person autogyro**, subsonic, flown in autorotation, developed for an Air
Force programme about escape from a disabled aircraft rather than about spaceflight. The four articles
before it are lifting bodies and entry vehicles. **Do not import the A321 pool.** The one-directory
rule has now held for nine consecutive articles and this is the case where breaking it would be most
obviously wrong.

**Expect the keystone to be autorotation itself**, meaning the descent rate at which a freely turning
rotor reaches equilibrium, which is computable from momentum theory and is the entire reason the
concept was proposed as an escape system. Compute what that descent rate actually is before deciding
what the article is about, and compare it against a parachute, because the comparison is the point.

**Note that the X-25 has a designation subtlety that is not one of the nine anomaly cases.** There were
several vehicles under the designation, including the X-25A gyrocopter and the X-25B gyroglider. Check
the record before assuming a single aircraft.

---

## Where the Series Stands

Seventy-two articles, A297 through A368, back-dated one per day from 2025-10-06 to 2025-12-16, covering
every X-designation from X-1 through X-76.

**Twenty-five complete**, A297 through A321, all four passes each, all in `_drafts/`, **none published**.

| Article | Aircraft | Final state |
|---|---|---|
| A317 | Boeing X-20 Dyna-Soar | 944 lines, 49 eq, 387 refs |
| A318 | Northrop X-21 | 1,692 lines, 45 eq, 1,192 refs |
| A319 | Bell X-22 | 1,891 lines, 25 eq, 1,472 refs |
| A320 | Martin Marietta X-23 PRIME | 4,088 lines, 72 eq, 3,403 refs |
| A321 | Martin Marietta X-24 | 3,684 lines, 53 eq, 3,144 refs |

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
band. Eleven consecutive articles have finished short of the equation band and were reported that way.

---

## Method Rules Earned the Hard Way

### On the analysis

**Write the relation down.** This has now caught a wrong claim in sixteen articles.

**THE VERIFIER CAN BE RIGHT AND KILL A FINDING YOU LIKE, AND THAT IS THE POINT OF HAVING ONE.** A321's
draft treated the flare as a circular arc at constant radius. The vehicle decelerates, so the arc
tightens, and the constant-radius version was too long by twelve percent in speed. **At low load factor
the error was qualitative rather than numerical**, producing a claim that a gentle flare ran out of
speed entirely and a whole finding built on it. Integrating properly, it does not. **The claim was
deleted rather than defended.**

**A CLEAN FACTOR IS A HINT THAT THE CHECKER IS AT FAULT, AND IT FIRED AGAIN.** A320's heading-angle
integration disagreed with its speed march by **exactly two**, which was a dropped factor in a
substitution rather than a physical disagreement. Corrected, two independent schemes agreed to five
significant figures.

**AN APPARENT CONFIRMATION CAN BE CIRCULAR.** A320 recovered a bank angle of 45.13 degrees against an
assumed optimum of 45, which looked like a beautiful check and was the assumed lift-to-drag ratio being
fed straight back in. **Suspiciously clean agreement is the signal to look for the loop.**

**TWO ERRORS CAN CANCEL AND PRODUCE A FALSE VINDICATION.** A320's closed form matched the demonstrated
crossrange to one percent, which appeared to settle a live source disagreement. It was a small-angle
error and a low assumed lift-to-drag ratio cancelling. **A model that agrees to one percent is not
thereby correct; improve it and see whether the agreement survives.** It did not.

**SINGULAR INTEGRALS NEED THE RIGHT INDEPENDENT VARIABLE, NOT MORE STEPS.** Entry at exactly circular
speed makes one over one minus u unbounded, so a uniform march in speed is dominated by its first steps
and a step count that looks generous is not. Integrating in **heading angle**, where the sine vanishes
at the same place, makes the integrand finite and ordinary quadrature converge.

**A NUMBER THAT IS NOT CREDIBLE IS A FINDING, NOT A NUISANCE.**

**"The article cannot compute this" is usually giving up too early.**

**Look for a cross-check between two quantities the article already has.** A321 predicted the Space
Shuttle prototype's tailcone-on lift-to-drag ratio from geometry alone and landed six percent from the
measured value, on a case the model was not fitted to. **That is worth more than any number the model
was tuned on.**

**A named limit belongs in the article**, including the boundary of the model's own validity, and
including **why a term is neglected**. A320 used a convective heating correlation and never said why
radiation was ignored, which is correct below ten kilometres per second and was unstated.

### On harvesting and selection

**THE KEYSTONE CLUSTER HAS BEEN THIN THREE ARTICLES RUNNING AND THE CAUSE IS ALWAYS THE SAME. THIS IS
NOW THE MOST RELIABLE RULE IN THE SERIES.**

- A319, ducted fans, thin until the era's vocabulary was used
- A320, **crossrange had EIGHT records**. The period says roll modulation, lift modulation, maneuvering
  range and boost-glide range. Broadening took it to 21
- A321, **unpowered landing had TWELVE records against 387 matching landing or approach**. The period
  does not say unpowered. It says approach and landing, and the fact that the vehicle has no engine
  sits in the body rather than the title. Broadening took it to 101

**THE PATTERN IS WRITTEN IN THE WRONG DECADE'S VOCABULARY. THE ARCHIVE HAS NEVER BEEN THE PROBLEM.**
Before concluding a topic is thin, probe it with the era's own words and with looser patterns.

**An equation pass promotes subjects, and the reference base must follow.** A320 had all ten promoted
subjects thin with four at zero. A321 had all nine thin with two at zero and one at thirteen in the
pool with none cited.

**The era gap is a selection problem, not a supply problem.** Place a dedicated period cluster after
the specific topics and before the broad ones. **And cap the topical clusters so the contemporary ones
are not starved**, which is the same defect running the other way.

**Read the selection, and read what the URL sweep prints.** Reading the sweep caught twenty-one
wrong-field citations in A320 that nothing else would have found.

**REPORT A TOPIC THAT IS GENUINELY THIN RATHER THAN PADDING IT.** A321's glide-range literature is seven
records in the whole pool after two harvests aimed at it. That is an archive limit and the article says
so.

**HOMONYM FAMILIES ARE THE DOMINANT FAILURE MODE. THE LIST NOW RUNS TO TWENTY-FIVE AND THE MOST
DANGEROUS ARE INTERNAL TO THE DISCIPLINE.**

| Phrase | The other field |
|---|---|
| **ballistic** | **three senses in one corpus.** Entry trajectories; the ballistic RANGE, a gun that fires models, which is LEGITIMATE and must not be filtered; and TERMINAL ballistics, meaning warheads and armour |
| **flare** | **overwhelmingly the SOLAR flare**, and solar papers omit the adjective. Also the gas flare and the flare stack |
| **energy management** | **power grids, buildings and batteries.** A query returned a manual on energy conservation in Navy family housing |
| **the electric road vehicle** | the largest body of literature this series has had to exclude. Shares vehicle, thermal management, model predictive control and trajectory |
| **reentry** | **agriculture.** The interval before workers may re-enter a treated field |
| **entry** | space physics, solar protons entering the magnetosphere; cell biology, a protein crossing a membrane |
| **easy glide** | crystal plasticity, a strain regime |
| **host range** | microbiology. It put Pseudomonas plasmids in A320's keystone cluster |
| **lateral motion of a vehicle** | railway hunting oscillation and road-vehicle lane keeping |
| **lateral range** | search and detection theory |
| **maneuvering range** | an instrumented air combat facility, so the pool holds its construction plan |
| **unpowered range** | wheelchairs. **Unpowered is not an aeronautical word** |
| **base** | the air base, the database, the base station |
| **speed of sound** | solutions and acoustics. A homonym A320 created for itself by adding that query |
| **footprint** | carbon accounting |
| **recovery** | economics, waste heat, and food microbiology where it is a term of art |
| **thermal resistance, inactivation, injury** | food microbiology |
| **dispersion** | atmospheric pollution |
| **boundary layer control** | **aeronautics itself.** Suction for drag or blowing for lift |
| **trim** | **aeronautics itself.** Balance, interior fittings, engine setting, planing attitude |
| **figure of merit** | **engineering itself.** Rotor hover efficiency, and radiation detectors |
| **electric propulsion** | **aerospace itself.** Aircraft motors and spacecraft ion thrusters |
| ablation | medicine and laser materials processing |
| laminar flow | cleanrooms, chromatography, fuel cells |
| ducted propeller | the Kort nozzle and the diffuser-augmented turbine |

**Not a homonym but the same defect: Crossref indexes EDITORIAL MATTER as works.** Guidance for
Authors and Guest Editorial both reached article pools.

**QUERY DESIGN PREVENTS MORE THAN FILTERING CURES.** A320 used no query containing PRIME or START,
because those belong to number theory and arms control, and the contamination largely never entered.

**The persisted rejection list is at `tmp/aNNN/read_and_dropped.json`, now 481 entries, and MUST be
carried forward.** **KEY IT BY URL AND NOT ONLY BY ANCHOR.** Anchor disambiguation suffixes shift when
an earlier record is removed, so dropping `research_x_2024_3` can silently retarget a different paper.

### On tooling

**DO NOT WRITE ARTICLE SECTIONS BY PLACEHOLDER SUBSTITUTION.** A320's survey was generated by expanding
cluster citations into literal text, which FROZE them. They stopped tracking the clusters, and when
records were later dropped they survived in the body and `gen_refs.py` correctly refused to emit.
**Cluster citations belong in the body as live `{c('...')}` calls.**

**HEREDOC BACKSLASH COLLAPSE MANGLES LATEX AND NOTHING CATCHES IT.** A321's survey equation was patched
through a shell heredoc that collapsed `\\text` to `\text`, and `write.py`'s own f-string then read
`\t` as a **tab**. The rendered output was `V_[tab]ext{td}` with `\frac` reduced to `rac`. The equation
count was right, the build succeeded and the braces balanced. **It was found by reading the generated
body.** Inspect rendered escapes after any patch that touches math.

**`check_any.py` REPLACES the per-article `check.py`.** It lives at `tmp/errata/check_any.py`, derives
the article number from the `<!-- Axxx -->` marker, and validates date and series index against the
roster. It now exempts a doubled **capitalised** word, because a Spanish or Catalan double surname
repeats legitimately in citation display text.

**`build_check.sh` derives the article count from the roster.** No stub list to arrive one short.

**`gen_master.py` suppresses a year the title fragment already ends with**, after authorless records
produced "U.S. Standard Atmosphere, 1962 1962", a doubled word in body prose.

**The NTRS search endpoint returns no authors and no year.** Both come from the per-record detail
endpoint.

**A stale script from the previous article can execute itself.** `select.py` shadowed the standard
library once and destroyed a work product. The selector is named `pick.py`.

**Know the expected number, not just pass or fail.** `_verify.py` baseline is **0 errors and 21
warnings**. A reading of 0 warnings means it did not run against the corpus. **Absolute paths in every
command issued after a `cd`.**

**Measure the equation count before and after any section work, and extend sections in place.**
Replacing a section is permitted only where it is an explicit placeholder or where the existing
structure cannot carry the content, and the replacement must be shown to preserve every existing claim.

---

## Verification Toolchain

**`tmp/*` IS GITIGNORED, so none of this survives a fresh clone.** Per-article scripts are rebuilt by
copying the previous article's directory and repointing. The two cross-article scripts live in
`tmp/errata/` and are not article-specific.

| Script | Purpose |
|---|---|
| `tmp/errata/check_any.py` | style and integrity for any or all articles, identity derived and roster-validated |
| `tmp/errata/build_check.sh` | real Jekyll build of every draft staged as a post, count derived from the roster |
| `harvest.py`, `harvest2.py`, `harvest3.py` | archive sweeps; the second closes audit gaps, the third is the publication-review contemporary sweep |
| `ntrs_detail.py` | per-record NTRS metadata, incremental; **search returns no authors** |
| `gen_master.py` | master reference index; carries `venue`, applies the rejection list, drops corrections and repeated years |
| `gen_refs.py` | emit the reference section from anchors the body uses; enforces the link-text invariant |
| `ref_audit.py` | coverage by topic, era and source, with an explicit primary definition; **run it BEFORE selecting** |
| `pick.py` | cluster selection; **not named `select.py`** |
| `diction.py` | word frequency, formulaic phrases and acronym spell-out for the publication pass |
| `read_and_dropped.json` | persisted decisions; carry forward, now 481 entries, **keyed by URL as well as anchor** |
| `calc.py`, `calc2.py` | the article's physics; calc2 carries the equation pass |
| `verify_numbers.py`, `verify_numbers2.py` | independent re-derivation, and a check that each value appears in the text |
| `url_check.py` | external sweep; Crossref registry for DOIs, HTTP for archives, **prints titles** |

### The Endpoints, Embedded Because the Scripts Are Not Committed

- **NTRS search** — `https://ntrs.nasa.gov/api/citations/search?q=<terms>`, per-record detail at
  `https://ntrs.nasa.gov/api/citations/<id>`. **Cite `https://ntrs.nasa.gov/citations/<id>`, never a
  search URL.** Caps at ten results and is phrasing sensitive, so **use short period vocabulary**.
  Author metadata is a dict under `authorAffiliations`; the year is in
  `publications[0].publicationDate`. **Full text is available at
  `/api/citations/<id>/downloads/<id>.pdf` and `pdftotext` works on it**, which is how A321's
  flight-determined vehicle table was obtained.
- **DTIC** — through Crossref with `filter=prefix:10.21236`. Cite `https://doi.org/<doi>`. **DTIC DOIs
  land on `www.dtic.mil`, which refuses automated connections, so verify through the Crossref
  registry**, which is strictly stronger than an HTTP 200.
- **OSTI** — **not worth using for this subject.**
- **Crossref** — `https://api.crossref.org/works?query.bibliographic=<terms>` with
  `filter=from-pub-date:...,until-pub-date:...,type:journal-article`. The response carries
  `container-title`, which is the venue the selector filters on. Use a polite-pool `mailto`.

### The Corpus Checks

`python3 _verify.py` from the **repository root**, `--strict` to treat warnings as errors. The same
checks run in CI and in the local hook at `_hooks/pre-push`. **The baseline is 0 errors and 21
warnings.**

**The bundle is installed** at `vendor/bundle`, which is gitignored. An isolated build whose source
tree is elsewhere needs `BUNDLE_GEMFILE` pointed back at the repository.

**An HTTP 200 does not verify a citation** and no sweep in this series claims it does.

**Independence matters.** `verify_numbers.py` must not import the calculation module. Use a different
quadrature, a different independent variable, a search where the model differentiates, and forward
substitution to check anything obtained by inverting.

---

## Open Decisions

**Categories — SETTLED and not to be revisited.** `aerospace history engineering`, which all
twenty-five drafts carry.

**A fourth genre class.** `_docs/writing/RESEARCH_AIRCRAFT_STRUCTURE.md` names four classes. **A313
through A321 have each finished outside all of them on two of three measures, in the same direction,
across TWELVE consecutive articles.** References land far above band while lines and equations land
below. **Do not amend the genre document unprompted**, since it defines the series' own standards, but
offer to propose a fourth class with bands drawn from those twelve.

**A305 length.** An offered cut of roughly 300 lines and 25 equations was never taken up. The offer
stands. **Do not act on it unprompted.**

**A320's genre classification was a judgement call and the pilot did not object.** The genre document
lists X-23 among the designation anomalies, whose class is 40 to 150 lines with no keystone. It was
written as a full-aircraft article because the SV-5D flew three times and returned a measurement, with
the anomaly given its own section. **If a later anomaly case has a real vehicle, that precedent
applies.**

---

## Governing Rules That Are Easy to Lose

**The `post_url` interlock.** A `post_url` tag whose target is absent fails the **entire** site build.
Cross-references are **back-reference only** within the series. The publication-order dependency is
**twenty-five deep**, A321 back to A297, so these articles publish in order or together. **Links to
other series are necessarily forward-dated** and that is not a defect.

**Pushing drafts is safe.** The deploy workflow builds without `--drafts`. Confirm after every push
that the article returns 404 while the site root returns 200. **A 503 on the root immediately after a
deploy is transient; retry before reporting it.**

**The two-commit publication pattern** applies when publishing eventually happens. Nothing in this
series is published and **no publication has ever been authorised**.

**Prose style is absolute.** No contractions, em dashes, en dashes, prose colons, prose semicolons, or
prose parentheticals. **A possessive is not a contraction.** The `console.log` debug tag is the only
permitted parenthesis. **Link text is prose**, so citation display strings must carry none of it either.

**Every article carries** an `<!-- Axxx -->` comment and a `<script>console.log("Axxx");</script>` tag
immediately after the front matter.

**The genre carries three sections beyond the standard twelve**, being Comparison With Ground
Prediction, The Contemporary Literature, and The Source Base, the last immediately before Epistemic
State. `check_any.py` enforces all three and exempts the series opener.

**Density conventions are absolute counts, not ratios.**

**Report the count as well as the fraction.** Adding a contemporary survey lowers the period *fraction*
while leaving the period *count* unchanged, and saying only the fraction reads as a regression when it
is the directive working. A321's period count moved by one, from 766 to 765, while the primary fraction
fell from 61.1 to 43.1 percent.

**Irreversible or outward-facing actions need confirmation.** Pushing is authorised only by the
publication-review prompt. **Publishing has never been authorised.**

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
