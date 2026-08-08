# Handoff Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the resume prompt for an agent picking up after a compaction or a new session. It is a
snapshot, deliberately not kept current, and it self-reports as stale rather than misleading a
resuming agent. Read it first, validate it, then read the live channels.

---

## Validity

- **Branch**: `master`
- **Parent commit** (the repository state this handoff describes): `9d52919`
- **Written**: 2026-08-08
- **Tree at write**: clean, nothing unpushed
- **Context**: the X-Planes series is IN PROGRESS. **Nineteen of seventy-two articles drafted, all four
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

## Resume prompt — the next prompt will be "Please draft A316, 'X-Planes: Curtiss-Wright X-19.'"

**Nothing is outstanding.** A315 finished all four passes, is committed and pushed, its CI run
succeeded, and the article returns 404 while the site root returns 200, which is correct because
nothing in the series is published. There is no half-finished pass to pick up.

**Wait for the pilot's prompt. Do not begin A316 unprompted.**

**A316 is the Curtiss-Wright X-19**, editorial date 2025-10-25, Part 20 of 72. It is a tandem-wing
tilt-propeller transport testbed using radial lift force propellers, and it crashed in 1965.

**The A315 pool is genuinely relevant and the one-directory question is live again.** The X-18 and the
X-19 share the propeller-slipstream transition problem almost exactly, far more closely than the X-18
shared anything with the X-13 or X-14. A315 handled the same question by BUILDING FRESH AND ASKING THE
SHARED QUESTIONS DIRECTLY in its own harvest, which obtains the common literature without importing a
pool built for a different aircraft, and that is the pattern to repeat. It costs a few duplicate
queries and nothing else. **Decide it explicitly in the harvest docstring either way**, because A309
imported six hundred ballistic-missile documents into an article about a tail-sitting jet by inheriting
a generator without deciding.

**Expect the tandem wing to be the keystone difference.** The X-18's problem was that two propellers
immerse only part of one wing. Four propellers on two wings is a different geometry with a different
failure mode, and the rear wing sits in the wake of the front one. Do not assume the A315 keystone
transfers. Compute the immersion and the wake interference before deciding what the article is about.

---

## Where the Series Stands

Seventy-two articles, A297 through A368, back-dated one per day from 2025-10-06 to 2025-12-16, covering
every X-designation from X-1 through X-76.

**Nineteen complete**, A297 through A315, all four passes each, all in `_drafts/`, **none published**.

| Article | Aircraft | Final state |
|---|---|---|
| A310 | Ryan X-13 Vertijet | 1,346 lines, 91 eq, 336 refs |
| A311 | Bell X-14 | 1,515 lines, 109 eq, 386 refs |
| A312 | North American X-15 | 1,368 lines, 99 eq, 350 refs |
| A313 | Bell X-16 | 1,233 lines, 72 eq, 468 refs |
| A314 | Lockheed X-17 | 1,066 lines, 47 eq, 446 refs |
| A315 | Hiller X-18 | 935 lines, 29 eq, 418 refs |

**The trend in that table is the open decision below.** A313, A314 and A315 each finished outside the
named genre classes on two of three measures, in the same direction, across twelve passes. Read
`_drafts/draft_summary.md` for per-article detail rather than re-deriving it.

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
band. A313, A314 and A315 all finished short of the line and equation bands and were reported that way.

---

## Method Rules Earned the Hard Way

### On the analysis

**Write the relation down.** Doing so has caught a wrong claim carried as an assertion in **eleven
consecutive articles**. Three times it inverted a conclusion rather than correcting a digit. If the
prose names a result, relies on a relation, or quotes a value some relation produced, show the relation.

**Computing further inside a pass can invert a conclusion written earlier in the same pass.** A312's
friction-share estimate and A313's Breguet check both reversed. When that happens, withdraw the earlier
reading in the text rather than silently replacing it.

**An article's own method can have a validity limit worth computing.** A312 found its perfect-gas
arithmetic valid to Mach 7.06 against an aircraft that flew at 6.70.

**A keystone can be conditional rather than general.** A314 assumed a reference condition, then derived
it, and found the vehicle's whole technique fails above a ballistic coefficient of about 2,500.

**Read calculation output for plausibility.** A315 produced a 454-knot crossover speed from an elevator
effectiveness sixty times too small. The arithmetic was correct and the coefficient was wrong, so **no
automated check would have caught it.**

**A vehicle with almost no record of its own can still carry a dense article, provided the question it
asked was one other people were also asking.** Established at A310, carried A313 and A314, both of which
had no archival record of the vehicle at all.

### On harvesting

**Ask for the middle era.** A313's audit found three citations across the whole of 1960 to 2018 because
the draft harvest never asked for it. That is a correction to an article's implicit history, not to its
arithmetic.

**Ask for the earliest era with a tight cutoff.** A314's pool held twenty pre-1960 records for a vehicle
that flew in 1956, because a 1985 cutoff let later work crowd out the contemporaneous literature. Use a
1960 cutoff as its own sweep. **These two rules are separate and neither implies the other.**

**An equation pass can promote a subject from an aside to a load-bearing claim, and the reference base
has to follow it.** A315's descent topic held three records because the draft mentioned it in Out of
Scope, and the equation pass then made it the quantity that closes the conversion corridor. **After an
equation pass, re-audit the topics the new relations rest on.**

**Distinguish a supply gap from a selection gap.** A314's audit found the pool genuinely lacked
material. A315's found the pool had everything and the draft had used only the earliest of it. The fixes
are opposite.

### On selection, which is where the defects actually are

**Read the selection. A title regex is not a substitute for looking.** Across A313 to A315, **fifty-four
candidate references were rejected after being read** and none was caught by any rule.

**A keyword diagnostic inside a field is useless outside it.** Documented cases:

| Search term | What it returned |
|---|---|
| resolution | spectra of stars in globular clusters; wireless sensor localisation |
| high aspect ratio | a high-explosive round for a railgun bore |
| fatigue under spectrum loading | gun tube steel |
| digital twin | cable-stayed bridges; rolling-element bearings |
| airborne hyperspectral | winter wheat topsoil |
| thermal protection system | a wetsuit for divers |
| high temperature air | a pneumatic air motor |
| nonequilibrium | a two-temperature Ising model |
| demise | dataveillance and interpretive flexibility |
| high angle of attack | missile bodies of revolution |
| noise | micro-mobility, meaning scooters |

**Use word boundaries.** `ram` matched inside `fRAMework`, `ising` inside `ARISING`, `bearing` inside a
legitimate paper on propeller bearing forces, and `regulat` inside `roll attitude REGULATION`.

**The checks need the same discipline as the thing they check.** Two of those substring failures were in
A315's own ad-hoc verification scan rather than in its selector.

**Reading works in both directions.** A315 kept a reference after reading its full title, because a
truncated display had hidden that its subject was Advanced Air Mobility.

### On tooling

**Copied scripts keep the previous article's constants, and one repointed clause does not mean all of
them are.** A311 and A312 both shipped a verification script pointing at the previous article. A314's
build script had `Part 18 of 18` corrected in one clause of a two-clause navigation check and `Part 18`
left in the other. **Grep the copy for the previous article's identifiers and read what comes back.**

**Absolute paths in every command issued after a `cd`.** This defect has recurred five times, including
`_verify.py` reporting a misleading zero warnings because it inherited a scratch working directory.

**Measure the equation count before and after any section work.** A310's publication review silently
dropped three equations by replacing a section. **Extend sections in place rather than replacing them.**

---

## Verification Toolchain

**`tmp/*` IS GITIGNORED, so none of this survives a fresh clone and all of it is rebuilt per
article by copying the previous article's directory and repointing.** That is why the endpoints below
are embedded here rather than referenced.

| Script | Purpose |
|---|---|
| `harvest.py`, `harvest2.py`, `harvest3.py` | archive sweeps, one mode per source; the second fills audit gaps, the third is the publication-review contemporary sweep |
| `ntrs_detail.py` | per-record NTRS metadata, since search returns only id and title |
| `gen_master.py` | build the master reference index from harvest metadata |
| `normalise.py` | display-string normalisation, including en and em dashes to hyphens |
| `gen_refs.py` | emit the reference section from anchors the body uses; enforces the link-text invariant and the URL-stability guard |
| `ref_audit.py` | coverage audit by source, era and topic; run it BEFORE selecting |
| `select.py`, `select2.py` | candidate selection by topic and era, with exclusion and read-and-drop lists |
| `check.py` | style and integrity; front matter, prose rules, section order, reference integrity |
| `calc.py`, `calc2.py` | the article's physics; calc2 carries the equation pass |
| `verify_numbers.py`, `verify_numbers2.py` | independent re-derivation of every quoted value |
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
  `https://api.crossref.org/works/<doi>` to verify a single identifier.

### The Corpus Checks

`python3 _verify.py` from the **repository root**, and `--strict` to treat warnings as errors. The
same checks run in CI before every build and in the local hook at `_hooks/pre-push`, enabled with
`git config core.hooksPath _hooks` and bypassed with `--no-verify`. **The baseline is 0 errors and 21
warnings**, all pre-existing in other articles. Any new warning is yours.

**Archive behaviours that will otherwise waste time.** NTRS caps at ten results and is phrasing
sensitive, so use short period vocabulary. NTRS author metadata arrives as a dict. Publication year is
in `publications[0].publicationDate`. DTIC is reached through Crossref prefix `10.21236`. **DTIC DOIs
redirect correctly and then land on `www.dtic.mil`, which refuses automated connections, so verify them
through the Crossref registry instead** — asking whether the identifier is registered and what title it
carries is a strictly stronger check than an HTTP 200 on a landing page. Publisher 403s from bot
detection are normal and numerous.

**An HTTP 200 does not verify a citation** and no sweep in this series claims it does.

**Independence matters.** `verify_numbers.py` must not import the calculation module. Reimplement the
atmosphere by trapezoidal integration against the analytic layer solution, and locate roots by a
different method than the calculation used, so that neither can validate the other.

---

## Open Decisions

**Categories — SETTLED 2026-08-08, at the pilot's discretion.** The answer is
`aerospace history engineering`, which all nineteen drafts already carry. **Do not revisit it and do not
raise it again.** It was checked rather than merely retained: three terms matches the corpus convention
at 203 of 296 posts; `aerospace` is the second most common first category and is not one of the shadowed
paths; **both `aerospace` and `engineering` are on the curated `jekyll-feed` category list**, so the
series reaches subscribers of two topical Atom feeds, while `history` is not on that list and gets an
archive page only; and category ORDER affects nothing but the URL path, since `jekyll-archives` and
`jekyll-feed` both select by name. Live checks returned 200 for an existing `/aerospace/...` post URL,
for `/categories/aerospace/`, for `/categories/engineering/`, and for `/feed/aerospace.xml`. Volumes
after the full seventy-two land at 135 aerospace, 135 history and 109 engineering against a 296-post
corpus, which is a large share of `engineering` and an accurate one.

**A fourth genre class.** `_docs/writing/RESEARCH_AIRCRAFT_STRUCTURE.md` names four classes. **A313, A314 and A315
each finished outside all of them on two of three measures, in the same direction, across twelve
passes.** References land in or above band while lines and equations land well below. This is now a
pattern rather than a coincidence. **Do not amend the genre document unprompted**, since it defines the
series' own standards, but offer to propose a fourth class with bands drawn from those three articles.

**A305 length.** An offered cut of roughly 300 lines and 25 equations was never taken up. The offer
stands. **Do not act on it unprompted.**

---

## Governing Rules That Are Easy to Lose

**The `post_url` interlock.** A `post_url` tag whose target is absent fails the **entire** site build.
Cross-references are **back-reference only**, never forward. The publication-order dependency is
**nineteen deep**, A315 back to A297, so these articles publish in order or together.

**Pushing drafts is safe.** The deploy workflow builds without `--drafts`, so a pushed draft does not
appear on the live site. Confirm after every push that the article returns 404 while the site root
returns 200.

**The two-commit publication pattern** applies when publishing eventually happens. Nothing in this
series is published and no publication has been authorised.

**Prose style is absolute.** No contractions, em dashes, en dashes, prose colons, prose semicolons, or
prose parentheticals. **A possessive is not a contraction.** The `console.log` debug tag is the only
permitted parenthesis.

**Every article carries** an `<!-- Axxx -->` comment and a `<script>console.log("Axxx");</script>` tag
immediately after the front matter.

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
