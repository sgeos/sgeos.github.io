# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-05
**Task**: Task 1 complete. Pathological word-usage pass over every blog post and draft. Task 2, the documentation review, remains queued and unstarted.

---

## Result

110 files changed across four commits. Corpus-wide rates per thousand prose words:

| Word | Before | After |
|---|---|---|
| `specific` | 1715 (1.68) | 501 (0.49) |
| `specifically` | 887 (0.87) | below the reporting floor |
| `substantial` | 1613 (1.58) | 522 (0.51) |
| `substantially` | 924 (0.90) | 370 (0.36) |
| `admits` | 755 corpus-wide | 321 |
| `comprehensive` | 405 (0.40) | below the reporting floor |
| `various` | 218 (0.21) | below the reporting floor |

Two kinds of remediation, because the words are not alike. **Deletion** for adjectival
`specific` and `specifically`, which were filler. **Rotation** for `comprehensive`,
`framework`, `substantial`, and `admits`, which carry meaning, so removing them would have
changed claims. Rotation is deterministic rather than random, so reruns reproduce the same
output and the diff stays reviewable.

---

## What I Found That You Should Know

**The comparative industrialization series was ungrammatical, not merely repetitive.** It used
`specifically` as an adjective: "the specifically Gulf oil states", "the specifically Saudi
ratio", "the specifically structural dependence". 571 of roughly 600 uses were preceded by
"the" and followed by a proper adjective. Against that, 2 legitimate adverbial uses in the
entire cluster. This is a grammar defect that shipped, not a style preference.

**Three formulas did most of the damage.** `the comprehensive treatments` closed a citation
**234 times** across the ethnoreligion series. `The framework provides` or `The framework has`
opened **106 of 273** sentences in one machines-that-learn article. `X admits the compact form`
preceded a display equation **130 times**.

**Two pre-existing defects, which I did not introduce and have not fixed.** An unused
`elixir-syslog` anchor in the 2016-01-17 post. More seriously, an undefined `rust_book`
reference link in the 2025-12-17 Solana post, which renders literally as
`[The Rust Programming Language][rust_book]` in the built HTML on the live site.

---

## What I Deliberately Did Not Do

**`framework` remains the highest generic word at 2.08 per thousand.** That residual is
**1379 modified phrases against 149 bare ones** -- "reinforcement learning framework",
"predictive coding framework", "the options framework" -- in a series that surveys learning
frameworks. Pushing it lower means substituting synonyms into technical terms, which risks
semantic drift for no real gain. It is topic vocabulary, in the same way `specific impulse` is.

**The rocket propellant articles are almost untouched**, at 71, 61, 44, 43, and 23 uses of
`specific`. 201 of roughly 222 uses were `specific impulse`. The earlier reconnaissance had
flagged this cluster as pathological; that was wrong, and the guard now proves it by leaving
those files at 71 uses to 71.

**Structural monotony is untouched.** Rotating the adjective in "X and Y provide the
comprehensive treatments" fixes the word frequency but leaves the sentence pattern repeating
234 times. Restructuring that many sentences is an editorial judgment, not something I should
automate silently. Say if you want it.

---

## The Method Note Worth Keeping

**Four bugs were caught by verification, and none by reading the diff.** This is the whole
argument for checking counts on things you did not intend to change.

1. A word-boundary rule spliced hyphenated compounds: `case-specific supplementary` became
   `case-supplementary`. Silent text corruption, caught by a unit test.
2. The adverbial guard omitted a trailing word boundary, so its alternation matched PREFIXES:
   `in` matched "Indian", `for` matched "forward". Roughly 90 adjectival uses were silently
   protected as though adverbial. Caught by counting what survived the pass.
3. Rotation produced "a extensive" and "the most appreciable".
4. Whitespace collapse ran unconditionally and rewrote pre-existing double spaces on 21 lines
   the word rules never touched.

**The discriminator remains the hard part.** Ratio against the rest of the corpus surfaces
topic vocabulary, not tics. Restricting to content-independent words and comparing against the
MEDIAN article rate works, because the mean is dragged upward by the articles under
investigation. Even then, a 44-entry exclusion table was needed to record why each surviving
outlier is legitimate.

---

## Items Requiring Your Attention

1. **Task 2 has not started.** The documentation review is still queued. Two defects are
   already confirmed and recorded in [`HANDOFF.md`](./HANDOFF.md): `FORWARD_DATED_POSTS.md`
   contradicts the live `future: false` setting, and 25 documentation references point at a
   `_publish.sh` that fails silently on macOS.
2. **The root cause is unaddressed.** No writing or process document instructs the use of
   `specific`. This is self-imitation drift, an agent calibrating to its own prior output. The
   prose is fixed; the mechanism that produced it is not. I can propose a preventive line for
   `_docs/writing/STYLE_GUIDE.md` if you want one.
3. **Nothing is pushed.** Four commits sit local. The build verifies clean, but these edit 110
   published articles, so the push is yours to authorize.

---

## State

Branch `master`, four commits ahead of `origin/master`, tree clean once the process-file commit
lands. Full site build verified in a Gemfile-free scratch copy: 294 posts in, 294 HTML out,
zero Liquid errors, equation counts unchanged in every changed file. No background jobs running.
