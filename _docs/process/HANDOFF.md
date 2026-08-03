# Handoff Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

The self-contained, imperative resume prompt, written **before a planned compaction** and validated
on resume. Unlike the two resume channels it is **not** kept always-current. It is a snapshot stamped
with the commit it describes, so a stale handoff self-reports as stale rather than misleading a
resuming agent.

Adapted from the protocol in the `keleusma` repository at `docs/process/HANDOFF.md`.

## Validity

- **Branch**: `master`
- **Parent commit** (the repository state this handoff describes): `7c2c97b`
- **Written**: 2026-08-04
- **Tree at write**: clean, in sync with `origin/master`, nothing unpushed
- **Context**: written immediately after the twelve-article History of SpaceX series A281 through A292
  was completed, corrected, published, and pushed. Deploy succeeded. There is no work in flight.

**Validity check — run on resume, before trusting this handoff.** On the branch above, compare the
**Parent commit** to `git rev-parse HEAD~1`. Because this handoff file is itself committed, its commit
advances the tip by one, so the state it describes is the parent of the handoff commit. The two match
**only** when this handoff commit is still the branch tip and nothing has landed after it.

- **Match → VALID.** Proceed per the resume prompt below.
- **Mismatch → INVALID and STALE.** A later commit moved the tip. Do **not** proceed and do **not**
  trust this handoff. Report the mismatch to the human pilot (recorded parent versus actual `HEAD~1`),
  familiarize from the live channels — `REVERSE_PROMPT.md`, `TASKLOG.md`, `_drafts/draft_summary.md`,
  and the git log, always authoritative — and wait for instruction.

## Resume prompt — no work is in flight; wait for direction

**The History of SpaceX series is complete and published.** Twelve articles, A281 through A292,
editorial dates 2026-07-24 through 2026-08-04, all at 09:00 UTC. Nothing about the series is
outstanding. Do not resume drafting it and do not re-verify it without being asked.

**Do not act on the items below without instruction.** They are carried-forward observations, not a
queue.

### Carried-forward items

- **A configuration and documentation contradiction.** `_docs/process/FORWARD_DATED_POSTS.md` states
  the site sets `future: true` and calls that foundational. The live `_config.yml` line 86 sets
  `future: false`. Commit `4cf5dd5` set it to true at some earlier point. Aligning them in either
  direction is a human-pilot decision. The observed consequence was benign, because the series
  back-reference-only convention means no published article points forward at a future-dated one.
- **`_publish.sh` does not work on macOS.** Its date-extraction `sed` expression uses `[+-:0-9 ]`,
  which BSD sed rejects as an invalid character range, so it reports that every file has no date and
  moves nothing. The publication `git mv` operations were performed directly with identical semantics.
  The script is the pilot's and was left unchanged.
- **269 Open Library search URLs across the series** point at a query rather than a specific work.
  This is a citation-quality matter, not link rot, and resolving them to work identifiers would be a
  dedicated pass.
- **A292 was withheld from the deploy on 2026-08-03** because its editorial date is 2026-08-04 and
  `future: false` excludes future-dated posts. It should be live on its own from that date. Confirm
  rather than assume.

### Method rules that were earned during this series, not assumed

1. **An HTTP 200 does not verify a citation.** A 2026-08-02 audit found thirteen citations whose
   anchor title and target document did not correspond, every one returning 200. Check DOI-bearing
   citations against the Crossref and `doi.org` registries, not against status codes. See
   `URL_VERIFICATION.md`.
2. **Never introduce a citation whose target you have not confirmed names the work you are citing.**
   When a source cannot be confirmed, drop it. A missing citation is a gap; a confident citation
   pointing at the wrong document is a fabrication.
3. **Prefer consolidating a dead anchor into one that already resolves** over guessing a replacement
   URL. Guessing at moved slugs is how fabricated citations enter.
4. **Verify a script's blast radius before running it over the corpus.** A resort script written
   during the consistency pass deleted the trailing link-definition block in all twelve articles by
   slicing a line range that ran to end of file. Prefer permuting lines in place over replacing ranges.
5. **Check counts on things you did not intend to change.** Two silent bugs during the word-usage pass
   were caught only by verification, never by reading: math-skipping logic that failed on blocks whose
   closing delimiter was not at line start, and a guard clause placed after the rules it was meant to
   guard against.
6. **Density conventions are absolute counts, not per-word ratios.** Equations cluster in the 60 to 78
   band regardless of article length. A ratio would break the convention.
7. **Rate-limited hosts make everything look dead.** `openlibrary.org` hard-blocks after an aggressive
   sweep and stays blocked. Pace verification, and retest a suspect URL in isolation before concluding
   anything is broken.

### Governing rules that are easy to lose

- **The `post_url` interlock.** A `{% post_url %}` tag whose target is absent from `_posts/` fails the
  entire site build, not just that page. Cross-linked drafts that reference one another must publish
  together or in strict order. The series convention is back-reference-only, and forward references are
  plain prose.
- **The two-commit publication pattern.** A staging commit with the draft in `_drafts/`, then a
  publication commit performing `git mv` into `_posts/` with the date prefix and syncing the process
  files. Never single-commit a publication. See `GIT_STRATEGY.md`.
- **Build verification before any push that publishes.** Local Jekyll is broken by a gem-environment
  issue. Copy the site into a scratch directory under `tmp/` without the `Gemfile`, strip
  `jekyll-archives` from the config, and build there with `--future`.
- **Style discipline.** No em-dashes, en-dashes, contractions, prose parentheticals, prose colons, or
  prose semicolons outside math. See `_docs/writing/STYLE_GUIDE.md`.
- **Commit once after every prompt**, including the `REVERSE_PROMPT.md` update. `PROMPT.md` is
  read-only for the AI agent but must be included in the commit if the pilot has modified it.
- **Confirm before irreversible or outward-facing actions.** Publishing, pushing, and force-pushing
  are the outward-facing ones here.

**Git position** (as of the Parent commit): branch `master`, tree clean, in sync with `origin/master`,
nothing unpushed. Deploy of the final batch completed successfully.

## Writing a New Handoff

Overwrite this file before a planned compaction, or when the pilot asks for a handoff. Then:

1. Set **Parent commit** to the current `HEAD`, because the handoff commit will become the new tip and
   the state described is its parent.
2. Set **Branch**, **Written**, and **Tree at write** to the observed state. Do not carry forward a
   remembered value; read it.
3. Replace the resume prompt with what a fresh agent must know that the live channels do not already
   say. Prefer pointers to on-disk sources over restating them.
4. Carry forward open concerns, earned method rules, and governing constraints. Drop anything resolved.
5. Commit it as the tip. If anything lands afterward, this handoff is stale by construction and the
   validity check will say so.

A handoff that is merely a summary of the resume channels is not worth writing. Its value is the
imperative direction and the hard-won rules that a summary would smooth away.
