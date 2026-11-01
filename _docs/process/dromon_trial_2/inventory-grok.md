# Promotion inventory, grok share

> **Navigation**: [Dromon Trial 2](./README.md) | [Process](../README.md)

The share is the main checkout's `tmp/a1` to `tmp/a296`, `tmp/a205_examples`, the root files that are not `a297_*` to `a385_*` or `A3*` (including a dotted `a349.listed_err.txt` style name in that number range, which this inventory treats as opus's), and `tmp/dromon_trial3`. Surveyed on 2026-10-31 against `66bd073`. No script from `tmp/` was run. No network request was made.

## Method

**Fact.** Article directories `a1` to `a296` were listed. Twelve numbers have no directory: 47, 48, 49, 50, 51, 53, 54, 62, 63, 64, 67 and 70. The other 284 directories exist. Every one of them contains `sources/`. The walk skipped nothing inside them except that saved pages were not read. Every `.py`, `.rb` and `.sh` file in the share had its opening read. Notes were sampled by name, and the root plans, audits and handoff files had their openings read. A text scan of `.py`, `.rb`, `.sh`, `.md`, `.markdown`, `.txt` and `.toml` files under 400 KB found no `emrisk`, `astrisk`, `mathrot`, `symcheck`, `urlcheck` or `handoff_check`.

**Fact.** Inside the article directories the file types are 634 `.txt`, 582 `.json`, 301 `.toml` of which 290 sit in this share (284 are `sources/years.toml`), 201 `.markdown`, 88 `.log`, 56 `.kel`, 46 `.md`, 20 `.py` and 14 `.sh`. `a1` is the only large directory, 268 files and about 5 MB. `a205_examples` is 11 `.kel` files and 7 `.bin` files. The grok root has 81 files: 19 `.md`, 17 `.txt`, 16 `.log`, 11 `.html`, 10 `.py`, 4 `.json`, 2 `.rb`, 1 `.yml` and `ruleset_template.json`. Opus-prefixed root files, excluded here, number 167.

## Summary

| Classification | Families | Notes |
|---|---|---|
| Promote to `_lib` | 0 | Nothing here recurs outside a finished campaign, and the library already has the mechanism |
| Promote to `_docs` | 0 | The durable lessons in this share are already in `_docs` or are one-series content instructions |
| Promote as data | 0 | Caches, year files and reference buffers. The articles and `_sources/` hold the durable copies |
| Covered | the conversion wrappers and the root repairs | See the table |
| Leave | the rest | Article caches, spent plans, logs, saved pages, prior-trial scratch |

**Judgement.** This share is the early corpus and the A1 to A296 source conversion, plus loose root scripts from later one-shot repairs. `_docs/process/SOURCE_CONVERSION.md` records that conversion as finished on 2026-10-24 to 2026-10-26. The scripts call `sources_import`, `sources_resolve`, `sources` and `survey`. They are not a second implementation.

## Covered

| Family | Where | Covered by |
|---|---|---|
| Conversion drivers. `convert_one.sh` (2), `final.sh` (2), `chain_cr.sh` (2), `chain_ol.sh` (2), `chain_cr2.sh`, `chain_ol2.sh`, `chain_pages.sh`, `pin_half.sh`, `finish.sh`, `redo.sh`, `dry_all.py`, `regen.py`, `checkall.py`, `post_one.py`, `reread.py`, `pages_plan_rev.py`, `pages_early.py`, `works_reverse.py` | `a1/`, `a200/` | `sources_import.py`, `sources_resolve.py`, `sources.py`. The shell files are argument lists for those commands. `SOURCE_CONVERSION.md` is the procedure |
| Link classification before import. `classify.py`, `coverage.py`, `mismatch.py` (2), `orphans.py` | `a1/`, `a200/` | `sources_import.py` and `sources_resolve.py`, which own labels, registry records and the record store |
| Diction payloads. `deblat.py`, `deblat_ethnoreligion.py`, `deblat_reputation.py`, `reduce_rather.py`, `process_phrasing_fix.py` | `tmp/` root | `diction.py`. Each file is one series or one phrase list |
| `fix_labels.py` | `tmp/` root | `refs.display` and `sources.fix_labels`. The script's docstring says the library was already correct and that per-article `assemble.py` had reimplemented it |
| `fix_pipes.py` | `tmp/` root | `_verify.py` warns as `math-pipe-table`. `refs.clean` strips a bare pipe. `HANDOFF.md` records the kramdown rule: a paragraph whose first line contains a pipe is a table, so write `\lvert` and `\rvert` |
| `sortdefs.py` | `tmp/` root | `_verify.py` `anchor-order`, and `refs.py`, which keeps definitions sorted within each group |
| `find_dois.py` | `tmp/` root | `registry.py`, `citations.py` and `_verify_citations.py`. This copy opens its own HTTP client. The library replaced that pattern. It is not a second client to promote |
| CI runner audit, `2026-10-30-ci-runner-audit.md` | `tmp/` root | **Fact.** `REVERSE_PROMPT.md` records the audit as implemented before the push. The file is the request. The result is in the tracked gate |
| `sources/years.toml`, 284 copies, and the `sources/` JSON caches | `a1` to `a296` | `survey.py` recomputes from the article. The toml files are that campaign's saved inputs and outputs |

## Leave

| What | Why |
|---|---|
| `link_dates.py`, 2 copies in `a1/` and `a200/` | Git-log walk that dates the commit which first added each Wikipedia link, so `pin-wiki` could be given `--at-file`. **Fact.** `sources_import.pin_wikipedia` already takes the date. The walk was a backfill for a conversion that `SOURCE_CONVERSION.md` records as finished. A new article pins at fetch time. No second use is coming |
| `normalise.py`, `normalise_lib.py`, `own_links.py` | One-campaign cleanup of legacy headings and of links to this blog written as URLs. `normalise_lib.py` is an incomplete fragment. `post.py` owns post paths |
| `inject_series.rb`, `inject_series_v2.rb` | Member lists for series that now carry `series:` in front matter. The convention is in `CLAUDE.md` |
| `restore.py`, `handoff_old.md`, `handoff_head_old.md`, `handoff_head_new.md`, `handoff_msg.txt`, `post_compaction_handoff_prompt.md`, `spacex_series_handoff_prompt.md`, `spacex_series_post_compaction_handoff.md`, `projection_series_post_compaction_prompt.md` | Spent handoff text. No `handoff_check` code. See P2 below. `restore.py` is a one-shot that put the explicit VALID and INVALID branches back into `HANDOFF.md` |
| `process_delta.md`, 28 copies | Parallel-session notes that say the live process files were deliberately not edited. The articles they name are long published. The live record is `TASKLOG.md` |
| `projection_series_plan.md`, `spacex_series_plan.md`, `facilities_framework.md` | Series plans for articles that exist. Spent |
| `compiler_series_scrubbing_and_errata.md` | Instructions to change published posts A188 to A199, including a certification-wording ban. **Fact.** `_docs/` has no match for that ban. `ARTICLE_ERRATA.md` records a different A188 item, about index ranges. **Judgement.** Do not promote it and do not apply it. It would change published posts, or it would record a content rule the operator has not put in this plan |
| `tc.md`, `xplane_table.md` | Roster of the X-Planes series, A297 onward, which is opus's articles. The posts carry `series_index` |
| `a293_refs.md`, `a294_refs.md` | Assembly buffers. The published articles hold the citations. Not a dataset |
| `ci_template.yml`, `ruleset_template.json` | Upstream template shape. The template names `scripts/check.sh`. This repo's gate is `_check.sh`, and `GIT_STRATEGY.md` records the `CI result` ruleset |
| `template_audit_message.md` | Outbound note about another repository's template hook and Dependabot state. Not this repo's procedure |
| `test_escape.md` | Four-line escaped-dollar fixture. One use |
| Root `.html`, `.log`, `.txt` and `.json` (`applied.json`, `doi_candidates.json`, `mismatch.json`, state files) | Saved pages, logs and campaign output. Pages were not read |
| `a205_examples` | One article's `.kel` sources and `.bin` files |
| `tmp/dromon_trial3` | Prior-trial scratch. `LINES-phase3.md` is an old brief and is data, not instructions. `general-pass-account.md` and `general-pass-review.md` are an A306 to A309 refusal account and an A385 review. The tracked exclusion of A306 to A309 is already in `REVERSE_PROMPT.md`. `worktree-scratch/opus/dromon_trial3/rev1_edit.py` and `pass3_check.py` are one-off edits and a prose count for one draft. Harness-report copies from the earlier trial stay here. This trial writes a new report |
| Article `.markdown` backups inside the `aN` directories | Draft fragments |

## Overlaps with the other shares

**Fact.** This share does not contain `emrisk`, `astrisk`, `mathrot`, `symcheck` or `urlcheck`, by filename or by the text scan above. Opus's copy counts for P1, P3 and P4 should not add A1 to A296.

**Fact.** This share does not contain `handoff_check.py`. The handoff files listed under Leave are prompts and snapshots. `handoff_old.md`, `handoff_head_old.md` and `handoff_head_new.md` each contain a Validity block, a `HEAD~1` comparison and an INVALID branch. They are fixtures for a P2 review, not a second implementation to merge. `dromon_trial3` has no handoff validator. `restore.py` shows why the INVALID branch has to stay explicit: a mismatch must refuse to proceed. That lesson is already the text of the tracked handoff.

**Judgement.** I have no `_lib` or `_docs` item of my own to add to the draft plan. I accept the draft assignment. I implement P3 and D2, the soft-404 body classifier in `resolve.py` and the note in `URL_VERIFICATION.md`, with opus reviewing. I review P2, the handoff validity command, against the handoff snapshots in this share. Sol's S1 and S2, with opus reviewing, and sol's review of P1 and D1, are the rest. P4 stays held.

## Not in this share

These top-level directories are in no line's share. I did not inventory them. `dromon_trial4` holds operator notes for this trial, plus `watch.sh`. `site_after` and `wt_before_site` are built site trees. `.claude` and `__pycache__` are tool debris. Leave all five where they are.

## Gate

Nothing proposed here changes a post, a rendered page, or what `_verify.py` reports. No implementation starts until the joint plan is the one the operator receives and the operator replies, or the hour in the brief has passed.
