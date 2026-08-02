# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-02
**Task**: A284 through A287 of the History of SpaceX series published as a four-article batch at editorial dates 2026-07-27 through 2026-07-30, all at 09:00 UTC, via the two-commit publication sequence pushed to origin/master.

---

## Published Articles

| # | Editorial date | File | Words | Equations | Anchors |
|---|---|---|---|---|---|
| A284 | 2026-07-27 09:00 | `_posts/2026-07-27-spacex_history_value_capture.markdown` | ~14,954 | 65 | 234 |
| A285 | 2026-07-28 09:00 | `_posts/2026-07-28-spacex_history_decomposability.markdown` | ~16,942 | 69 | 257 |
| A286 | 2026-07-29 09:00 | `_posts/2026-07-29-spacex_history_generality_forcing.markdown` | ~29,811 | 72 | 390 |
| A287 | 2026-07-30 09:00 | `_posts/2026-07-30-spacex_history_governance.markdown` | ~23,648 | 72 | 287 |

Seven of the twelve series articles are now live. A288 through A292 remain to be drafted at editorial dates 2026-07-31 through 2026-08-04.

---

## Commit Sequence

1. **Staging commit** `ad18c06` added the four drafts to `_drafts/` with process files describing the drafting-complete state, and aligned the series publication-time convention at 09:00 UTC by correcting A284 from 00:00 UTC.
2. **Publication commit** performed `git mv` from `_drafts/` to `_posts/` with date prefixes for all four articles and synced `draft_summary.md`, `TASKLOG.md`, and `REVERSE_PROMPT.md` to the published state.

Both pushed to origin/master. Deployment proceeds via the GitHub Actions build.

---

## Verification Performed Before Push

The interlock across these four articles was the main publication risk. A286 cross-references A284 and A285 by `post_url`, and A287 cross-references A286. Publishing any of them alone would have failed the site build and blocked deployment of the whole site. Publishing them together resolves it, and I verified that rather than assuming it.

- **Pre-flight.** Editorial dates 2026-07-27 through 2026-07-30 confirmed free of collision. Front matter, series metadata, categories, debug tags, and 09:00 UTC times confirmed correct on all four. Anchor integrity confirmed at 234, 257, 390, and 287 with zero missing, unused, or duplicate in each.
- **Build.** The local bundle environment is broken by the documented gem issue, so I built a Gemfile-free scratch copy under `tmp/` with the unavailable archives plugin stripped. The build completed without error, which is what confirms every `post_url` resolves.
- **Render.** All four articles generated at their expected permalinks. The A287 page renders with correct title, MathJax include, series navigation reading Part 7 of 7, zero unresolved Liquid tags, and all seven intra-series links resolving to existing files.

The scratch build directory was removed before the publication commit.

---

## Notes You Should Have

1. **95 broken reference URLs were repaired** across A286 and A287 during their expansion passes, all inherited from the sibling reference corpus. The already-published A281, A282, and A283 still carry many of the same dead links, including three SpaceX user's-guide PDFs, both NASA Human Landing System award press releases, the NASA Space Act Agreements guide, and the FAA current-licenses database. A sweep of those three is worth scheduling and was outside the scope of this task.

2. **Open Library search URLs.** 32 of A286's and 32 of A287's book references point to Open Library search queries rather than publisher editions. This is a consequence of repairing rotted publisher links for older works, not a preference. The form is stable and matches existing repo convention, but it is a weaker citation than an edition page. A later pass could resolve them to specific work identifiers.

3. **A285 had no `draft_summary.md` entry.** I wrote one at publication so the record is complete, reconstructed from the file itself rather than from session history I did not have.

4. **A287 carries a critical case I did not soften.** The article states plainly that a configuration resisting capital capture resists every other form of external accountability by the same mechanism, and it does not resolve the tension. If you would prefer the article take a side, it currently does not.

5. **A284's summary entry was stale** before this session, recording initial-draft metrics rather than its expanded state. The entry is now marked published; the metrics in it may still understate the article.

---

## Suggested Next Steps

- Confirm the GitHub Actions build succeeded and the four new pages are live.
- Draft A288 Portfolio Patience next, at editorial date 2026-07-31 09:00 UTC. A287 forward-references it in plain prose as the article treating the internalized portfolio across which the controller allocates capital without external review.
- Schedule the broken-link sweep across A281, A282, and A283.
- Consider whether the remaining five articles publish individually as drafted or as a second batch. Nothing in A288 through A292 is written yet, so the interlock question does not bind until they cross-reference one another.
