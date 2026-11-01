# Promotion inventory, opus share

> **Navigation**: [Dromon Trial 2](./README.md) | [Process](../README.md)

The share is the main checkout's `tmp/a297` to `tmp/a385`, the root files `a297_*` to `a304_*`, `a369_*`, `a371_*` and
`A369_*` to `A371_*`, and `tmp/jev`. It was surveyed on 2026-10-31 against master `66bd073`.

## Method

**Fact.** I walked the share once and indexed every `.py`, `.rb`, `.sh`, `.md` and `.toml` file with its line count
and MD5 hash. I skipped `__pycache__`, `cache`, `sources`, `stub` and `build`. Families were formed by normalising
the file name, which strips the article prefix and a trailing digit. Each family's docstring was read from its
latest copy. Every candidate was checked against `_lib/`, `_verify.py` and `_docs/` before it was classified. The
index and the survey scripts are `tmp/promotion/index.json`, `survey.py` and `q.py` in my worktree. **No script
from `tmp/` was run.**

**Fact.** The share holds 478,356 files. Most are JSON, 429,026 of them, mainly registry caches and harvest pools.
Excluding the skipped directories, it holds 2,039 Python files, 642 notes, 76 shell scripts and 21 Ruby files.
The directories `a341` to `a359` each carry `stub/` and `build/`, which are whole-repository snapshots of 86 to 185 MB.

## Summary

| Classification | Families | Notes |
|---|---|---|
| Promote to `_lib` | 3 | P1, P2 and P3 below, with P4 as a weaker candidate |
| Promote to `_docs` | 2 | D1 and D2, each paired with a `_lib` item |
| Promote as data | 0 | Nothing in the share qualifies, see `jev` |
| Covered | about 40 | Every large family, see the table |
| Leave | the rest | Article payloads, snapshots, caches, spent notes |

**Judgement.** The share confirms what `_lib/README.md` predicts. The large families are already replaced, and the
residue worth promoting is a small number of checks that the A353 to A368 run of the X-Planes series wrote, copied
forward article to article, and never promoted.

## Promote to `_lib`

### P1. Emphasis tags inside inline mathematics

| | |
|---|---|
| Files | `emrisk.py`, 7 copies in A362 to A368, 1 distinct body. `astrisk.py`, 6 copies in A363 to A368, 1 distinct. `mathrot.py`, 7 copies in A362 to A368, 7 distinct. Evidence in `a362/kram_probe.rb` and `kram_verify.rb` |
| What it guards | Kramdown pairs an underscore or asterisk in one inline `$...$` span with another in the same paragraph, emits `<em>` across the two spans, and the mathematics renders with a stray tag in it |
| Why not covered | **Fact.** `grep` finds no `<em>` check in `_lib/render.py`, `_lib/lint.py` or `_verify.py`. `mathrot.py`'s docstring says the rendered audit does not see this, and `render.py`'s `audit_html` checks delimiters, raw `$$`, markers and Liquid only |
| Measured rule | From `emrisk.py`, calibrated by `kram_probe.rb`. An underscore opens when the character before it is not a word character. It closes when the character after it is not a word character. An escaped `\_` is inert. Two earlier models in the same file were wrong, and one nearly shipped a wrong number |
| Proposed destination | `render.py` gains a check for an emphasis tag inside an inline or display maths span, which sees what a reader sees. `lint.py` gains a source-side predictor for the same defect, with the measured rule, at CONVENTION severity until it is measured on the corpus. Tests in `test_lib.py` cover the five probe cases from `kram_probe.rb`. A Ruby probe beside `test_pandoc_input.rb` could pin kramdown's actual behaviour |
| Gate impact | **Measured, and the defect is live.** See the measurement below. The check would fail CI today, so it lands reporting only, and gates once the operator approves and the repairs land. `_verify.py` is not touched |

**Measurement on a production build of 66bd073**, `tmp/promotion/site`, 552 pages, 258 loading MathJax.

- **Fact.** Kramdown leaves single-dollar maths as raw `$...$` in the HTML, and MathJax typesets it in the browser. My first scan looked only for `\(...\)` spans and reported 0, which was blind and is discarded.
- **Fact.** `em_notation.py` walks each block of a MathJax page, toggles an in-maths state on each single dollar and on `\(` and `\)`, and counts emphasis tags met inside maths, in blocks whose dollar count is even. **18 blocks on 13 published pages** carry the defect.
- **Fact.** 10 of the 18 blocks, on 8 pages, are entries in the generated Notation list. `equations.py` `render` writes each one as `- ${tex}$, {meaning}` from `_sources/equations`, and a meaning naming a second symbol, such as `with $\dot{m}_{e}$`, pairs an underscore across the two spans. The pages are X-24, X-34, X-35, X-43, X-64, X-66, distressed acquisitions and native lowering coverage. **The tracked generator emits this defect, and `equations.py check` passes it.**
- **Fact.** 8 blocks, on 7 pages, are in body prose. The pages are framing, X-21, X-34, X-37, X-49, X-64 and mass drivers.
- **Fact.** The odd-count restriction drops 37 blocks where a single literal dollar in a reference title, such as `$18.5 Bn`, sits before an `<em>` journal name.
- **Inference.** MathJax 3 matches delimiters only within one text string, and an `<em>` element breaks the string, so those single dollars stay literal. A reader therefore sees `$\dot{m}` followed by italic text in the 18 defect blocks, and nothing wrong in the 37 single-dollar blocks. I have not confirmed either in a browser.
- **Inference.** The source predictor `em_measure.py` flagged 104 pairs against 18 rendered blocks, so a source-side `lint.py` predictor would over-flag heavily. The `lint.py` part of P1 is dropped, and the render check carries P1 alone.

### P2. Handoff validity check

| | |
|---|---|
| Files | `handoff_check.py`, 7 copies in A359 to A365, 7 distinct, 136 to 259 lines |
| What it guards | `CLAUDE.md`'s startup protocol step 1, which compares the handoff's recorded parent commit to `git rev-parse HEAD~1` by hand, at every session start and after every compaction |
| Generic part | About a quarter of each copy. It covers reading the stamp from the Validity block, choosing `HEAD` before the commit and `HEAD~1` after it, the branch, and whether each commit hash the Validity block names exists. The rest asserts article-specific claims and stays in `tmp/` |
| Lesson it carries | **A check run at the wrong moment confirms the wrong thing.** The first `--pushed` run compared the stamp to `HEAD` and reported the handoff's own commit as a disagreement |
| Proposed destination | A `handoff` command, either a new `_lib/handoff.py` or a function in `progress.py`, which already reads the resume channels. Tests on a fixture handoff in `testdata/` |
| Gate impact | None. It is a command, not a gate |

### P3. A not-found page served with status 200

| | |
|---|---|
| Files | `urlcheck.py`, 6 copies in A360 to A365, 4 distinct |
| What it guards | An address that returns 200 with a body saying the page is not found. `resolve.py` sends a HEAD request and accepts the status, so it reports such an address as resolved |
| Why not covered | **Fact.** `resolve.py`'s `check` reads only the status. No module classifies a response body |
| Proposed destination | A body classifier in `resolve.py`, run only on a 200 from a GET when an option asks for it, with offline tests on saved body strings. **Inference.** Sol's `linktest`, `dltest` and `site_check` may hold the same mechanism, so this needs a merge decision |
| Gate impact | None. `resolve.py` is not in CI |

### P4. Undeclared symbols in an article's equations, a weaker candidate

| | |
|---|---|
| Files | `symcheck.py`, 16 copies in A353 to A368, 15 distinct |
| What it guards | A symbol used in the body mathematics that the article never declares |
| Overlap | `equations.py check` already confirms that each declared notation symbol appears in an equation. This is the converse |
| Doubt | **Judgement.** The structural-token list was tuned per article over sixteen copies, and the series used `\mathcal` for quantities. A corpus-wide report may be mostly noise. I propose it only as an opt-in `equations.py symbols POST` report, and only if the team judges the noise acceptable after a trial on A305 to A310 |

## Promote to `_docs`

| ID | Lesson | Source in the share | Destination | Check done |
|---|---|---|---|---|
| D1 | The measured kramdown emphasis rule, the escape `\_` that fixes it, and why bracing a subscript made it worse | `emrisk.py`, `astrisk.py`, `kram_probe.rb` | `_docs/writing/MATHJAX_CONVENTIONS.md`, with P1 | **Fact.** It is recorded only in the logs `TASKLOG.md`, `REVERSE_PROMPT.md` and `HANDOFF.md`. `MATHJAX_CONVENTIONS.md` and `VERIFICATION_TRAPS.md` do not mention it |
| D2 | A 200 does not verify a citation and a 403 does not refute one, plus the third case of a 200 whose body is a not-found page | `urlcheck.py` | `_docs/process/URL_VERIFICATION.md`, with P3 | **Fact.** It is recorded only in `x_planes_drafting_notes/A341.md` |

## Covered

| Family, copies in the share | Covered by |
|---|---|
| `harvest`, 182 copies. `gate_and_cluster`, 50. `select`, 24. `gen_master`, 32. `assemble`, 51. `cluster`, `pick`, `thin_harvest` | `harvest.py`, `gate.py` |
| `build_refs`, 60. `gen_refs`, 19. `refs`, 21. `merge_primaries`, `emit_backlinks` | `refs.py`, `sources.py` |
| `verify_survey`, 79 and its `.pre*` backups. `regen_survey`, `survey_prose`, `survey_facts` | `survey.py` |
| `verify_numbers`, 58. `numbers`, 16. `inject`, 5. `neg_labelpass`, 6 | `numcheck.py`, including `--inject` |
| `primary_pass`, 24. `eqn_pass`, 23. `apply`, 17. `prose_edits`, 13. `hygiene_apply`, 18. `pub_pass`, 11. `fix`, `edit`, `edits` | `edits.py` |
| `ref_audit`, 17. `eqn_scan`, 9. `eqscan`, 6. `eqcand`, `neweqns` | `audit.py` |
| `url_check`, 13. `sweep`, 18. `verify_ids`, 9. `verify_refs`, 7. `verify_urls`, 6 | `citations.py`, `resolve.py`, `_verify_citations.py` |
| `ntrs_detail`, 32. `ntrs_harvest`, `crossref`, `resolve_years`, `ol` | `fetch.py`'s NTRS, Crossref and Open Library adapters, and `sources_import.py fetch-reports` |
| The A375 to A384 shell shortcuts `cr.sh`, `oa.sh`, `s.sh` and others, plus `search`, `abs`, `oa_q` | `registry.py` |
| `diction`, 10 | `diction.py` |
| `ctx`, 5 | `textscan.py` |
| `rendercheck`, 7 | `_verify.py` `math-display-inlined`, promoted from the A375 incident |
| `stylecheck`, 6. `pubrev` and `pubreview`, 14 | `_verify.py` style checks and the scripts in `_docs/process/STYLE_VERIFICATION.md`. `diction.py acronyms` covers the acronym scan |
| `make_stub.sh`, `site_build.sh`, `after_build.sh`, `isolated_build.sh`, `full_build.sh` | `_check.sh` |
| Every `retrofit/` directory, with `draw_sample`, `thin`, `splice`, `write_notes`, `make_chunks`, `record_reading`, `cands`, `prose`, `existing` and others | `campaign.py`. `_lib/README.md` records that the retrofit campaigns are complete and are not to be rerun |
| `homprobe`, `merge_sweeps`, `store_cost`, `homonyms` | `_research/homonyms.py` and the sweep store. The lessons are in `x_planes_drafting_notes` |
| `READING_RULE.md` and `PROGRESS.md` in each `retrofit/` | `x_planes_drafting_notes/`, which records the reading rules article by article |

## Leave

| What | Why |
|---|---|
| `stub/` and `build/` in A341 to A359, and `full/` in A357 to A359 | Snapshots of the repository, including copies of `_lib`, `_verify.py`, `_docs` and `_check.sh`. They explain the 28 copies of each library module in the raw count |
| `calc*.py`, 86 copies in 44 articles. `meas`, `register`, `emit`, `emit_source_base`, `expand`, `eqns`, `analysis`, `primhunt` | One article's physics, measurements or slot values. `numcheck.py` holds the mechanism |
| `series_line.py`, 6 copies | It builds the opening line of the X-Planes synthesis articles. It belongs to one series that is now complete |
| `body*.md`, `A*.md`, `source_base.md`, `contemporary.md`, `*_refs_block.md`, `draft_before_*.md`, `*.markdown` backups | Draft fragments and backups |
| Logs, JSON pools, chunk files, PDFs, saved HTML, caches | Payloads and third-party material |
| `A369_addendum_note.md`, `A370_correction_instructions.md`, `A371_draft_corrections.md`, `A371_erratum.md`, `a371_*.txt` | Spent. **Fact.** The A371 post carries `## Erratum, 2026-08-12`, and `TASKLOG.md` rows for 2026-08-12 record the A369 addendum and the A371 corrections as applied |
| `a363/handoff_*.md`, `a364/ho_*.md`, `a365/FINDINGS.md`, `a377/findings.md`, `a381` to `a384` pass notes | Spent handoff fragments and per-article findings. Their durable parts are in `x_planes_drafting_notes/` and `TASKLOG.md` |
| `tmp/jev`, 2.0 GB | Screening of X-Planes survey records through a paid third-party API, TypeSafe Jev. It holds that vendor's saved documentation, `api*.md`, `sdk_python.md` and `llms.txt`, whose licence is unclear, plus a 1.6 GB cache. The 300-row hand-judged gold sample in `data/` is registry titles judged under a pilot rule. No tracked code would read it. The outcome is already recorded in the drafting notes and `TASKLOG.md` |

## Overlaps to resolve with the other shares

- **P3 and Sol's share.** `linktest`, `dltest`, `dltest2`, `site_check` and `web` may already hold a body-reading
  link check. Sol should say whether one is more general than `urlcheck.py`.
- **P1 and Sol's share.** `mathrepair` may hold the same emphasis-in-mathematics mechanism.
- **P2 and Grok's share.** The root handoff prompts and `dromon_trial3` may carry handoff validation code.

## Proposed ownership, for discussion

I propose to implement P1 with D1 and P2, and to review an item from another line. P3 with D2 should go to
whichever line holds the more general copy, after the overlap question above. P4 is held until the team judges it.
