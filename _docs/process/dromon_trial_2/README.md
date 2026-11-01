# Dromon Trial 2

> **Navigation**: [Process](../README.md) | [Documentation Root](../../README.md)

The second three-model trial of the PyDromon harness on this blog, run on 2026-10-31 from 23:36Z into
2026-11-01. The pilot asked for a review of the main checkout's `tmp/`, 24 GB in 664 entries with about 4,800
scripts written over eight months, and for anything that ought to be generalized to be promoted to a tracked
status. Claude Opus 5.5 on Claude Code, GPT-6.1-Sol on Codex and Grok 4.7 on Grok Build did the work, on PyDromon
`main` at `f5f8da1`. GPT-6.1-Sol replaced GPT-6-Luna on the pilot's word, and Grok took a full share from the start.
[Dromon Trial 1](../dromon_trial_1/README.md) is the first trial.

| File | Description |
|------|-------------|
| [inventory-opus.md](./inventory-opus.md) | The Opus line's inventory of the article scratch from A297 to A385 and `tmp/jev` |
| [inventory-sol.md](./inventory-sol.md) | The Sol line's inventory of the campaign and tooling directories |
| [inventory-grok.md](./inventory-grok.md) | The Grok line's inventory of the article scratch from A1 to A296 and the loose root files |
| [plan.md](./plan.md) | The joint promotion plan, verbatim, and the operator's approval with its conditions |
| [harness-report-opus.md](./harness-report-opus.md) | Experience report of the Opus line |
| [harness-report-sol.md](./harness-report-sol.md) | Experience report of the Sol line |
| [harness-report-grok.md](./harness-report-grok.md) | Experience report of the Grok line |
| [operator-report.md](./operator-report.md) | Experience report of the operator session |

## Outcome

**Most of `tmp/` is covered or should be left.** The earlier survey recorded in [`_lib/README.md`](../../../_lib/README.md)
had already promoted the large families. What remains is one-article payloads, saved sources, snapshots of the
repository, caches, logs and spent handoff prompts, and the inventories say which module or document covers each
family. One file, `compiler_series_scrubbing_and_errata.md`, holds unapplied instructions to change published posts
A188 to A199, and it stays unapplied.

**Promoted to `_lib`.**

| Item | Change | Evidence | Implementer, reviewer |
|---|---|---|---|
| P1 | `render.py` gates on an emphasis tag inside inline mathematics, as `math-emphasis` | 3 detectors copied through A362 to A368 | Opus, Sol |
| P2 | `handoff.py` and `blog.py handoff`, the startup validity check | 7 copies of `handoff_check.py` | Opus, Grok |
| P3 | `resolve.py --body` reads each HTTP 200 and reports a not-found page as `NOT-FOUND-BODY` | 6 copies of `urlcheck.py` | Grok, Opus |
| S1 | `equations.py preview POST DATA`, which validates a candidate classification in memory | 3 byte-identical `validate.py` | Sol, Opus |
| S2 | `equations.py audit BEFORE AFTER`, a layout guard for a migration and not a proof of equivalence | 2 migration auditors | Sol, Opus |

**Promoted to `_docs`.** D1 records the measured kramdown underscore and asterisk rule in
[MathJax Conventions](../../writing/MATHJAX_CONVENTIONS.md). D2 records the 200 whose body says not found in
[URL Verification](../URL_VERIFICATION.md).

**A live defect fixed in 13 published posts.** A production build of `66bd073` showed 18 blocks on 13 pages where
kramdown paired an underscore across two inline mathematics spans and put an emphasis tag inside the mathematics.
Ten came from the Notation lists that `equations.py` generates, and `equations.py check` passed them. R1 corrected
the generator and regenerated eight Equations sections. R2 escaped eight body blocks on seven pages. Every changed
post is identical to `66bd073` once backslashes are removed. The rendered diff shows the 18 blocks fixed, ten
repeated in five feeds, and no other change. No URL, category, date or claim changed, so there is no erratum.

**Every review found something.** Opus found that P3 never reached the hand-written URLs it was written for, and
that R1 missed an underscore after a digit. Sol found that D1 denied a case kramdown does break. Each was fixed and
re-reviewed on a case the author had not used.

**Gates.** `test_lib` 188 of 188, `test_sources` 96 of 96, `test_equations` passing, `_verify.py` 0 errors and 0
warnings over 385 posts, and `./_check.sh` passing with the new check gating, run by the Opus line on the integrated
tree and again by the operator in the main checkout.

## Harness Findings

Reported to the PyDromon implementation line with the four reports.

- A resumed Grok session kept the rules it was created with, so Grok began this trial on the phase 2 brief. The
  operator reset it by hibernating the line and rebinding it twice.
- `@operator` did not resolve, so two lines lost their first operator message. PyDromon resolves an operator by
  its registered name, so the alias works only where the operator is named `operator`.
- The `kill_all` stop policy held the Sol line three times after one slow `ps`. A probe measured 9.5 to 15.4
  seconds under load from other projects, against a ten-second timeout with no retry.
- Grok's engine offered `todo_write`, which the line is not given, and the line was held for calling it.
- A line that ended its turn with `./_check.sh` running in the background showed idle.
