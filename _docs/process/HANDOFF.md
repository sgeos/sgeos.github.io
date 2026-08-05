# Handoff Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

The self-contained, imperative resume prompt, written **before a planned compaction** and validated
on resume. Unlike the two resume channels it is **not** kept always-current. It is a snapshot stamped
with the commit it describes, so a stale handoff self-reports as stale rather than misleading a
resuming agent.

Adapted from the protocol in the `keleusma` repository at `docs/process/HANDOFF.md`.

## Validity

- **Branch**: `master`
- **Parent commit** (the repository state this handoff describes): `9c8955c`
- **Written**: 2026-08-05
- **Tree at write**: clean; commit `9c8955c` plus this handoff commit are UNPUSHED
- **Context**: the X-Planes series is PLANNED and VERIFIED but NOT DRAFTED. Drafting begins next.

**Validity check — run on resume, before trusting this handoff.** On the branch above, compare the
**Parent commit** to `git rev-parse HEAD~1`. Because this handoff file is itself committed, its commit
advances the tip by one, so the state it describes is the parent of the handoff commit. The two match
**only** when this handoff commit is still the branch tip and nothing has landed after it.

- **Match → VALID.** Proceed per the resume prompt below.
- **Mismatch → INVALID and STALE.** A later commit moved the tip. Do **not** proceed and do **not**
  trust this handoff. Report the mismatch to the human pilot (recorded parent versus actual `HEAD~1`),
  familiarize from the live channels — `REVERSE_PROMPT.md`, `TASKLOG.md`, `_drafts/draft_summary.md`,
  and the git log, always authoritative — and wait for instruction.

## Resume prompt — DRAFT the X-Planes series. Everything else is finished.

The pilot has approved drafting and asked to begin after compaction. Two items were outstanding at
write time and should be settled in the first exchange rather than assumed:

1. **Categories are still the agent's assumption, not the pilot's decision.** `aerospace history
   engineering` has been carried throughout. This fixes 72 published URLs and cannot be changed later
   without dead links, which the pilot has declined to mitigate with redirects. **Ask.**
2. **Commit `9c8955c` is unpushed**, carrying the genre document the whole series depends on.

The pilot's stated preference is to draft **A297 and A298 only, then stop** so the shape, depth, and
per-article source burden can be reviewed before the pattern is set across seventy-two articles.

## The Series

72 articles, **A297 through A368**, editorially dated **2025-10-06 through 2025-12-16**, one per day
unbroken, ending flush against the 2025-12-17 article that begins the run to 2026-08-05. Verified
zero collisions, zero date gaps, contiguous numbering.

**Back-dated, so every article publishes immediately on push.** The series does not depend on the
daily cron, which was still unproven at write time.

- `series: x_planes`, `series_title: X-Planes`
- Genre: **research aircraft**, defined in
  [`_docs/writing/RESEARCH_AIRCRAFT_STRUCTURE.md`](../writing/RESEARCH_AIRCRAFT_STRUCTURE.md).
  Read it before drafting. It gives the twelve-section order and three article classes.
- Parity target: the History of SpaceX medians of **1345 lines, 72 display equations, 306 reference
  definitions**. Depth falls where the record does not support it, and the shortfall is stated in the
  Epistemic State rather than padded.
- Written from **current knowledge**; where information postdates the editorial date, say so in the
  Epistemic State. This applies to X-76, revealed 2026-03-09, and to X-59, X-65, X-66 and X-68.
- Overlap with `History of Rocketplanes` is **accepted** for X-1, X-2, X-15, X-20, X-23, X-24, X-37
  and X-40. Take a per-aircraft engineering angle and cross-link rather than restate.

### The roster, embedded because the working copy is gitignored

The pilot accepted a gitignored roster at `tmp/xplane_table.md`. It is reproduced here so it survives
a clean checkout.

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

### The nine anomaly cases

These are the short articles, and they are the evidence for the closer. The designation system is not
a counter.

- **X-23** — attributed to the Martin Marietta SV-5D PRIME, but USAF nomenclature records reportedly
  show X-23A was never assigned. State the conflict, do not resolve it silently.
- **X-39** — reserved 23 April 1997 for the AFRL FATE program; no written allocation request followed,
  so it remained officially unassigned.
- **X-41** — still-classified vehicle in the DARPA FALCON program. No specifications released.
- **X-42** — sources disagree. One calls it an expendable liquid-propellant upper stage, another a
  military spaceplane test vehicle. No dedicated article anywhere.
- **X-44** — two different aircraft, the Lockheed Martin MANTA and a separate UAV.
- **X-52** — requested 2006, refused over possible confusion with the B-52. The program became X-53.
- **X-58** — skipped; slot went to the Kratos XQ-58 Valkyrie.
- **X-67** — skipped; slot went to the General Atomics XQ-67A.
- **X-69 to X-75** — unassigned and leapfrogged.

X-58 and X-67 were lost to the **parallel XQ- unmanned series consuming numbers from the same pool**,
which is a genuine finding about how the system evolved and belongs in the closer.

### The method rule this series was built on

**Designations are NOT assigned monotonically.** The agent excluded X-76 after reading
`designation-systems.net`'s statement that "the next available design number is X-69" as an upper
bound. The pilot challenged that assumption and supplied the DARPA release, which confirms the Bell
Textron X-76 SPRINT and states the number was chosen as **a deliberate nod to 1776** for the
country's 250th anniversary. The reference describes only the next unused sequential slot.
Wikipedia's own navigation template independently labels X-76 "Non-sequential".

Seven of the nine anomaly cases were found only after abandoning the sequential assumption. When a
roster looks like a sequence, verify that it is one.

## Verification, all of it built and proven this session

- `python3 _verify.py` — offline corpus invariants, about 4 seconds. Runs in CI after checkout and
  via `_hooks/pre-push`. Enable the hook with `git config core.hooksPath _hooks`.
- `python3 _verify_citations.py` — DOI resolution against Crossref, paced, cached in `.cache/`.
  Network-dependent, deliberately outside the deploy path. **Run per batch, not at the end**, since
  20,000 references at parity is exactly the condition that produced 47 broken citations before.
- `_verify_exemptions.yml` — documented false positives. Add X-Planes entries as needed rather than
  muting checks.
- Faithful local build: `bundle install` then
  `JEKYLL_ENV=production bundle exec jekyll build --baseurl ""`. Do **not** use a Gemfile-free build
  with plugins stripped; it invents hundreds of phantom broken links and hides real ones.

## Governing rules that are easy to lose

- **An HTTP 200 does not verify a citation.** Confirm DOIs through Crossref by author and title.
  `doi.org` returns 202 for IEEE and 403 for ACM under bot detection, so status codes mislead in both
  directions. Never introduce a citation whose target has not been confirmed; drop what cannot be.
- **Do not pad math or references to hit a target.** The conventions forbid it explicitly.
- **The `post_url` interlock.** A tag whose target is absent from the build fails the entire site
  build. Under `future: false` that includes any forward-dated article. Everything dated on or before
  today is safe to link regardless of order; only future-dated targets break. The
  back-reference-only convention is about build safety, not chronology.
- **Two-commit publication.** Staging commit with drafts in `_drafts/`, then a publication commit
  performing `git mv` into `_posts/` and syncing process files.
- **Date collisions are zero corpus-wide and must stay zero.** `_verify.py` enforces this.
- **Verify a behavioural claim by running it**, not by reasoning about it.
- **When a system derives a value through a transformation, verify against the transformed value**,
  not the input. Checking front matter dates for collisions missed two that existed at URL level.
- **Do not infer a CI verdict from a chained shell exit code.** Read `gh run view --json conclusion`.
- **Commit once after every prompt**, including the `REVERSE_PROMPT.md` update.
- **Confirm before irreversible or outward-facing actions.**

## Git position (as of the Parent commit)

Branch `master`, tree clean, one commit unpushed. Recent deploys succeeded. Downloads healthy at
`pdf=295 epub=295 failed=0`. Deploy time is about two minutes with caching, down from twenty-one.

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
