# Handoff Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

The self-contained, imperative resume prompt, written **before a planned compaction** and validated
on resume. Unlike the two resume channels it is **not** kept always-current. It is a snapshot stamped
with the commit it describes, so a stale handoff self-reports as stale rather than misleading a
resuming agent.

Adapted from the protocol in the `keleusma` repository at `docs/process/HANDOFF.md`.

## Validity

- **Branch**: `master`
- **Parent commit** (the repository state this handoff describes): `24cbd59`
- **Written**: 2026-08-05
- **Tree at write**: clean; commits `01e474a` and `24cbd59` plus this handoff commit are UNPUSHED
- **Context**: the X-Planes series is IN PROGRESS. Five of seventy-two articles drafted. None published.

**Validity check — run on resume, before trusting this handoff.** On the branch above, compare the
**Parent commit** to `git rev-parse HEAD~1`. Because this handoff file is itself committed, its commit
advances the tip by one, so the state it describes is the parent of the handoff commit. The two match
**only** when this handoff commit is still the branch tip and nothing has landed after it.

- **Match → VALID.** Proceed per the resume prompt below.
- **Mismatch → INVALID and STALE.** A later commit moved the tip. Do **not** proceed and do **not**
  trust this handoff. Report the mismatch to the human pilot (recorded parent versus actual `HEAD~1`),
  familiarize from the live channels — `REVERSE_PROMPT.md`, `TASKLOG.md`, `_drafts/draft_summary.md`,
  and the git log, always authoritative — and wait for instruction.

## Resume prompt — CONTINUE DRAFTING the X-Planes series at A302.

Five articles are drafted. Sixty-seven remain. Nothing else is outstanding.

**Do not start A302 until you have asked about categories.** See Open Decisions below. Everything
else can proceed on the established pattern without further instruction.

## Where the Series Stands

| Article | Date | Aircraft | Lines | Eq | Refs | Passes done | Pushed |
|---------|------|----------|-------|----|----- |-------------|--------|
| A297 | 2025-10-06 | Series framing | 1765 | 147 | 421 | all four | yes |
| A298 | 2025-10-07 | Bell X-1 | 1387 | 108 | 337 | all four | yes |
| A299 | 2025-10-08 | Bell X-2 | 1497 | 126 | 370 | all four | yes |
| A300 | 2025-10-09 | Douglas X-3 | 1415 | 114 | 365 | all four | yes |
| A301 | 2025-10-10 | Northrop X-4 | 1149 | 98 | 269 | draft + equations | **no** |

**A301 still needs its primary-reference and publication reviews.** Its primary share is 43.3
percent, the lowest of the five, and its line count is 151 short of band. Two commits are unpushed.

## The Established Rhythm, Which Is the Most Important Thing Here

The pilot drives each article through **four passes**, each a separate prompt. Do not try to do them
all at once, and do not skip ahead.

1. **"Please draft Axxx"** — research, write, verify, commit. Do not push.
2. **"Please review for equation density, and add all candidate equations."**
3. **"Please review for reference density, specifically primary references, and add all identified references."**
4. **"Please review for publication, and make suitable changes..."** — this prompt also asks for a push.

Push only when the prompt says to. Publishing is never implied by any of them.

Each review pass follows the same discipline. **Measure first, report the baseline, then act.** The
pilot has responded well to being told what the number was before it changed, and several of the
better findings came from measuring rather than from writing.

## Standing Directive, Quoted Because It Governs Every Pass

> "all articles in this series have no length limit, no reference limit, and that they should serve
> as a comprehensive survey and review of the contemporary literature in addition to any other stated
> goals"

Contemporary means recent scholarship, not recent history. Every article carries a
`## The Contemporary Literature` section. Target roughly 28 to 33 percent of dated references at 2010
or later, which is where A297 through A300 landed after their publication reviews.

## Method Rules Earned the Hard Way

These are the reason this handoff is worth writing. Each cost a real defect.

- **Title-token overlap is not proof of identity.** An NTRS query about the X-1 returned an X-2
  document and vice versa, both scoring 1.00. Two others returned "Lunar and Planetary Science
  XXXIV". **Label every entry with the title the API returned, not the title you searched for**, and
  drop anything whose returned title does not describe a usable source.
- **A generator is a source of truth only while it still generates the file.** A300 and A301 both
  shipped dangling anchors because their reference data was built by importing the previous article's
  generator, which had drifted after later additions were made directly to that article's markdown.
  **Build each article's reference data from its own harvest.** The integrity check caught it both
  times, which is luck rather than method.
- **Bulk reference additions introduce formulaic repetition wholesale.** A300 reached 70 percent of
  citations introduced by the preposition `in` because 40 primaries went in during one pass with one
  construction. Vary the construction while writing, not afterward.
- **The word-frequency check counts citation labels as prose.** `nasa` and `naca` measure above
  threshold in every per-aircraft article and are almost entirely `[NACA 1953]` link text. Report the
  split; do not remediate a citation index for a style violation it does not have.
- **An HTTP 200 is worthless from a search endpoint.** Open Library and NTRS `search?q=` return 200
  for nonsense. Only fixed identifiers and Wikipedia titles give a meaningful 404. Say so when
  reporting a sweep.
- **Status codes mislead on DOIs in both directions.** Publishers return 403 (AIAA, APS, ASME, Royal
  Society, Taylor and Francis) or 202 (IEEE, Wiley). **Resolve every DOI through Crossref and compare
  on author and title.** This caught a nonexistent identifier and one resolving to an unrelated paper
  on bipropellant exhaust optics.
- **Re-derive every worked number independently.** Errors were found in *every* article this way,
  including one where the article was right and the verification was wrong because it used a
  different Reynolds number. State the reference length so the check is reproducible.
- **Check edit seams after inserting before existing text.** The A297 equation pass produced two
  duplicated clauses that all automated checks passed straight through. Read the connective lines.
- **When a roster looks like a sequence, verify that it is one.** Designations are not assigned
  monotonically. Seven of the nine anomaly cases surfaced only after dropping that assumption.

## Verification Toolchain

- `python3 _verify.py` — offline corpus invariants, about 4 seconds. Also runs in CI and via
  `_hooks/pre-push`. Baseline is **0 errors, 21 warnings**; any new warning is yours.
- **NTRS citations API** — `https://ntrs.nasa.gov/api/citations/search?q=<terms>` returns real
  document ids. Short queries work; long ones return nothing because matching is near-AND. Cite
  `ntrs.nasa.gov/citations/<id>`, never a search URL.
- **Crossref** — `https://api.crossref.org/works/<doi>` to verify, and
  `works?query.bibliographic=...&filter=from-pub-date:YYYY-01-01,type:journal-article` to harvest
  contemporary literature.
- **Isolated build** — symlink `_posts`, `_layouts`, `_includes`, `_sass`, `css`, `assets`,
  `_plugins`, `_data`, `vendor`, `.bundle`, `_config.yml`, `Gemfile`, `Gemfile.lock` into a scratch
  directory, copy only the series drafts into its `_drafts/`, and run
  `JEKYLL_ENV=production bundle exec jekyll build --drafts --baseurl "" --destination _out`.
  A full-tree `--drafts` build fails on the pre-existing empty `post_url` in `_drafts/draft_summary.md`.
- **Genre document** — `_docs/writing/RESEARCH_AIRCRAFT_STRUCTURE.md`. Bands are 1300 to 1600 lines,
  90 to 130 equations for a full aircraft and 120 to 160 for the opener, and 250 to 380 references.
  **Padding to reach a band is forbidden.** Report a shortfall instead.

## Open Decisions

1. **Categories, and ASK BEFORE DRAFTING A302.** `aerospace history engineering` has been carried
   through all five articles and is still the agent's assumption. It fixes 72 URLs permanently at
   publication and the pilot has declined redirects. This has been raised four times without a
   decision, so raise it once more and then proceed on the assumption if no answer comes.
2. **109 Open Library search URLs remain in A297.** Open Library exposes a search API and the same
   upgrade that fixed the NASA citations would resolve them to edition pages. Offered, not yet taken up.
3. **The roster names the X-62 as Lockheed Martin.** Wikipedia titles it **General Dynamics X-62
   VISTA** because the airframe is a modified F-16D. A359 should name the disagreement rather than
   pick silently.

## Governing Rules That Are Easy to Lose

- **The `post_url` interlock.** A tag whose target is absent from the build fails the entire site
  build. Under `future: false` that includes any forward-dated article. **The publication-order
  dependency is now five deep**, since A301 cites A300, A299, A298, and A297. They publish in order
  or together.
- **Nothing in this series is published.** All five are in `_drafts/`. The deploy workflow runs
  `bundle exec jekyll build` without `--drafts`, so pushing is safe. After every push, verify by
  reading `gh run view --json conclusion` directly and then curling the article URLs to confirm 404.
- **Two-commit publication.** Staging commit with drafts in `_drafts/`, then a publication commit
  performing `git mv` into `_posts/` and syncing process files.
- **Commit once after every prompt**, including the `REVERSE_PROMPT.md` update. Sync
  `TASKLOG.md` and `_drafts/draft_summary.md` in the same commit.
- **Do not infer a CI verdict from a chained shell exit code.**
- **Confirm before irreversible or outward-facing actions.** Push when asked. Never publish
  unprompted.

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
