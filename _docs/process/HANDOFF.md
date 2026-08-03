# Handoff Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

The self-contained, imperative resume prompt, written **before a planned compaction** and validated
on resume. Unlike the two resume channels it is **not** kept always-current. It is a snapshot stamped
with the commit it describes, so a stale handoff self-reports as stale rather than misleading a
resuming agent.

Adapted from the protocol in the `keleusma` repository at `docs/process/HANDOFF.md`.

## Validity

- **Branch**: `master`
- **Parent commit** (the repository state this handoff describes): `ec25680`
- **Written**: 2026-08-04
- **Tree at write**: clean, in sync with `origin/master`, nothing unpushed
- **Context**: written before a planned compaction, with two tasks queued and neither started.

**Validity check — run on resume, before trusting this handoff.** On the branch above, compare the
**Parent commit** to `git rev-parse HEAD~1`. Because this handoff file is itself committed, its commit
advances the tip by one, so the state it describes is the parent of the handoff commit. The two match
**only** when this handoff commit is still the branch tip and nothing has landed after it.

- **Match → VALID.** Proceed per the resume prompt below.
- **Mismatch → INVALID and STALE.** A later commit moved the tip. Do **not** proceed and do **not**
  trust this handoff. Report the mismatch to the human pilot (recorded parent versus actual `HEAD~1`),
  familiarize from the live channels — `REVERSE_PROMPT.md`, `TASKLOG.md`, `_drafts/draft_summary.md`,
  and the git log, always authoritative — and wait for instruction.

## Resume prompt — two queued tasks, neither started

The History of SpaceX series A281 through A292 is complete, published, and pushed. Do not resume it.

Two tasks are queued. **Confirm with the pilot which to start**; they were given together and the order
was not specified.

---

## Task 1 — pathological word-usage pass over the whole corpus

Extend to every article the pass already completed on the twelve SpaceX articles.

**Scope**: 257 non-SpaceX posts plus 8 drafts, roughly 1.46 million words. The 12 SpaceX articles are
**already remediated** and must be excluded from the worklist and from any baseline.

**The reconnaissance is already done. Do not redo it.** Findings, measured 2026-08-04:

| Article | `specific`/1k | tic burden/1k |
|---|---|---|
| 2026-07-23 contemporary_snapshot_and_extrapolation | 46.2 | 52.6 |
| 2026-07-21 silicon_valley_from_defense_contracting | 33.0 | 38.2 |
| 2026-07-22 software_defined_aerospace_and_autonomy | 32.5 | 39.3 |
| 2026-07-20 safety_critical_software | 22.5 | 27.0 |
| 2026-02-01 rocket_propellant_chemistry_design_tradeoffs | 19.7 | 20.3 |
| 2026-07-18 arpanet_and_networking_origins | 18.8 | 22.7 |
| 2026-07-19 space_shuttle_software | 18.1 | 20.3 |

- **23 articles exceed 5 per 1k**; **48 exceed 2 per 1k**. Natural corpus rate is about 1.7.
- The worst cluster is the **aerospace and computing history run of 2026-07-15 through 2026-07-23**,
  which ramps 7.2 → 46.2. This is the same escalation that fed into the SpaceX series, and it was
  never remediated outside that series.
- Secondary clusters: **rocket propellant chemistry** (2026-02-01 to 02-05, 8.1 → 19.7), **comparative
  industrialization** (2026-03-18 to 03-21, 7.4 → 9.9), and the **ethnoreligion series**
  (2026-01-09 to 01-13), whose tic is `various` at 37.9x corpus rate and `comprehensive` at 12 to 14x.
- Corpus-wide generic-word rates per 1k: `framework` 3.01 (3132 uses), `substantial` 1.69,
  `specific` 1.68, `configuration` 1.03, `structure` 1.03, `admits` 0.74, `compact` 0.36. The last two
  are my own formulaic equation-introduction tic bleeding beyond the SpaceX series.

**Root cause, and it changes the remedy.** I grepped every writing and process document: **nothing
instructs the use of `specific`.** The tic is self-imitation drift, an agent calibrating to its own
prior output rather than following a bad rule. So fixing the prose alone will not prevent recurrence.
Propose a short preventive line for `_docs/writing/STYLE_GUIDE.md` — write at ordinary density and do
not calibrate against recent siblings — and let the pilot decide whether to adopt it.

### Method: the discriminator is the whole problem

I wasted a scan today on the wrong one. Record both.

- **WRONG — ratio against the rest of the corpus.** Surfaces topic vocabulary, not tics. It ranked
  `iondtn`, `kotlin`, `openbsd`, `playdate`, `clipboard`, `raycasting` at the top. Those words are
  concentrated because the articles are about them.
- **RIGHT — restrict to a fixed list of content-independent words, then look for outliers.** Generic
  adjectives, hedges, connectives, and generic nouns. A tic is a word that carries no topic content
  and is still overused.

**Even the right discriminator produces false positives that need judgment.** `key` at 50 per 1k in
the Solana articles is cryptographic keys. `key` in the SSH article is SSH keys. `structure` in
"Structures and the Flight Envelope" is the subject. Never remove a word from an article whose topic
is that word.

### Transformation rules that worked, in the order they must run

The scripts are gone, since the session scratchpad does not survive compaction. Rebuild from this.

1. **Stash genuine technical terms FIRST**, before any other rule. `specific impulse`, `specific heat`,
   `specific thrust`, `specific power`, `specific strength`, `specific gravity`, `specific energy`,
   `specific performance`. Placing this guard later defeats it: the determiner rules turn
   `the specific impulse` into `the impulse` before a late guard ever sees it. That cost 12 of 17 terms
   on the first attempt.
2. **Stash inline math** with `\$[^$\n]+\$` so nothing inside it is touched.
3. **Skip non-prose lines**: front matter, headings, HTML, link definitions, reference bullets, table
   rows, fenced code.
4. **Track display math by cumulative `$$` count, never by "line starts with `$$`".** A block closing
   with `\end{array}$$` does not start with the delimiter, so a toggle-based tracker never flips back
   and silently skips the entire rest of the file. This bug made an early run look like it had
   plateaued.
5. Then: `the specific` → `the`; `a specific X` → `a`/`an X` with article agreement fixed against the
   following word; determiner + `specific` → determiner; possessive + `specific` → possessive,
   including the plural `s'` form; preposition or verb or comma + `specific` → drop.
6. **Preserve genuine contrast** only where it attaches to the same noun phrase, matching
   `specific (\w+[\s-]+){1,4}(rather than|as opposed to|and not|not)`. A proximity window is too loose
   and protects whole regions because one `rather than` appears somewhere nearby.
7. Handle pre-existing awkwardness the plain rules would worsen, such as `a specific such X`.
8. For formulaic phrases, **vary across a rotation rather than substituting one formula for another**,
   and apply only to line-final occurrences preceding a display equation so sentence-medial uses stay
   intact.
9. For a word that is legitimate domain vocabulary but repetitive, such as `configuration`, **vary only
   the within-sentence repeats** and leave single uses alone.

### Verification after every batch

Non-negotiable, and it caught both silent bugs above when reading did not.

- Equation counts **unchanged** per article; `$$` balanced; `\left`/`\right` matched; braces balanced.
- Anchors: zero missing, unused, or duplicate; definitions matching reference-list bullets exactly.
- Style discipline clean: no em-dashes, en-dashes, contractions, prose parentheticals, prose colons,
  or prose semicolons outside math.
- Grammar after removal: zero `a` before a vowel, zero `an` before a consonant, zero doubled words.
  Expect false positives such as `lock-in in shaping` and `Falcon Heavy Heavy-Lift`, both correct.
- **Check counts on things you did not intend to change.** That is what surfaced both bugs.

Work in batches with a commit per batch. Do not attempt 265 articles in one transformation.

---

## Task 2 — review documentation and process files for pathological instructions

Scope: 31 files under `_docs/`, plus `CLAUDE.md`. About 42,000 tokens.

**Word usage in the docs is already clean** and is not the target. `specific` sits at 0.78 per 1k,
below natural rate. Do not run Task 1's transformation over the docs.

The target is instructions that are **wrong, contradictory, or harmful to follow**. Two are already
confirmed and are the place to start.

1. **A doc that contradicts the live configuration.** `_docs/process/FORWARD_DATED_POSTS.md` states in
   two places that the site sets `future: true` and calls that setting foundational, quoting a config
   excerpt asserting it. `_config.yml` line 86 sets `future: false`, with its own deliberate comment
   describing the opposite policy and the constraint it imposes. Commit `4cf5dd5` set it to true at
   some earlier point. An agent trusting the document would reason incorrectly about publication.
   **Aligning them in either direction is a pilot decision**, so present both options rather than
   choosing.
2. **25 documentation references to a script that does not work on this platform.** `_publish.sh` is
   the documented publication mechanism. Its date-extraction `sed` expression uses `[+-:0-9 ]`, which
   BSD sed rejects as an invalid character range, so on macOS it reports that every file has no date
   and silently moves nothing. The fix is to reposition the hyphen, for example `[-+:0-9 ]`, but the
   script is the pilot's and was left unchanged.

Beyond those, look for: instructions contradicting other instructions; absolute directives that force
a worse outcome in a foreseeable case; steps referring to files, flags, or paths that no longer exist;
and guidance that would have prevented a defect this project actually hit but is not written down.
Absolute-directive density is modest, the highest being `CROSS_LINKED_SERIES.md` at 14 per 1k, so
volume is not the problem. Correctness is.

**Report findings and let the pilot decide.** Do not rewrite process documents unilaterally.

---

## Governing rules that are easy to lose

- **The `post_url` interlock.** A `{% post_url %}` whose target is absent from `_posts/` fails the
  entire site build, not just that page. Cross-linked drafts publish together or in strict order. The
  convention is back-reference-only; forward references are plain prose.
- **The two-commit publication pattern.** Staging commit with the draft in `_drafts/`, then a
  publication commit performing `git mv` into `_posts/` and syncing process files. Never single-commit.
- **Build verification before any publishing push.** Local Jekyll is broken by a gem-environment issue.
  Copy the site into a scratch directory under `tmp/` without the `Gemfile`, strip `jekyll-archives`
  from the config, build with `--future`.
- **An HTTP 200 does not verify a citation.** A 2026-08-02 audit found thirteen citations whose title
  and target did not correspond, every one returning 200. Check DOIs against Crossref and `doi.org`.
  Never introduce a citation whose target you have not confirmed; drop what cannot be confirmed.
- **Density conventions are absolute counts, not per-word ratios.**
- **Verify a script's blast radius before running it over the corpus.** A resort script deleted the
  trailing link-definition block in all twelve SpaceX articles by slicing a range that ran to end of
  file. Prefer permuting lines in place over replacing ranges.
- **Rate-limited hosts make everything look dead.** `openlibrary.org` hard-blocks after an aggressive
  sweep and stays blocked for hours. Pace verification; retest a suspect URL in isolation.
- **Do not build chains of sentinel-waiting background jobs.** Four shells deadlocked for over two
  hours today waiting on sentinels whose producers had been killed. Give a producer a `trap` that
  writes its sentinel on exit, or give the waiter a bounded timeout.
- **Commit once after every prompt**, including the `REVERSE_PROMPT.md` update. `PROMPT.md` is
  read-only for the AI agent but is included in the commit if the pilot modified it.
- **Confirm before irreversible or outward-facing actions.**

## Git position (as of the Parent commit)

Branch `master`, tree clean, in sync with `origin/master`, nothing unpushed. The final publication
deploy succeeded. A292 was withheld from that deploy because its editorial date of 2026-08-04 is later
than the deploy date and `future: false` excludes future-dated posts; confirm it is live rather than
assuming.

## Writing a New Handoff

Overwrite this file before a planned compaction, or when the pilot asks for a handoff. Then:

1. Set **Parent commit** to the current `HEAD`, because the handoff commit becomes the new tip and the
   state described is its parent.
2. Set **Branch**, **Written**, and **Tree at write** from the observed state. Read it; do not carry
   forward a remembered value.
3. Replace the resume prompt with what a fresh agent must know that the live channels do not say.
   Prefer pointers to on-disk sources over restating them.
4. Carry forward open concerns, earned method rules, and governing constraints. Drop anything resolved.
5. Commit it as the tip. If anything lands afterward, the validity check will report it stale.

A handoff that is merely a summary of the resume channels is not worth writing. Its value is the
imperative direction and the hard-won rules that a summary would smooth away.
