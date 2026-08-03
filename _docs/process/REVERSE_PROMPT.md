# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-04
**Task**: Handoff prompt drafted ahead of your planned compaction, covering the two queued tasks. Stamped at `ec25680` and committed as the branch tip.

---

## What I Put in the Handoff

I did the reconnaissance for both tasks rather than describing them, because a handoff that only restates the goals is worth less than the tokens it costs. The next session should not have to rediscover any of this.

### Task 1 — the scope is larger than the SpaceX pass

**257 non-SpaceX posts and 8 drafts, roughly 1.46 million words.** The twelve SpaceX articles are excluded as already remediated.

**23 articles exceed 5 uses of `specific` per thousand words; 48 exceed 2.** Natural corpus rate is about 1.7.

The worst cluster is the **aerospace and computing history run of 2026-07-15 through 2026-07-23**, ramping 7.2 → **46.2**. That is the same escalation that fed into the SpaceX series — I remediated the series and left its run-up untouched. Secondary clusters: rocket propellant chemistry (8.1 → 19.7), comparative industrialization, and the ethnoreligion series, whose tic is `various` at 37.9x corpus rate rather than `specific`.

Corpus-wide, `framework` is the most overused generic word at 3.01 per thousand across 3,132 uses. My own `admits the compact` equation formula has bled beyond the SpaceX series too.

### The finding that changes the remedy

**I grepped every writing and process document. Nothing instructs the use of `specific`.**

So this is self-imitation drift — an agent calibrating to its own prior output — not a bad rule being followed. That matters: fixing 265 articles without addressing the mechanism means it comes back. The handoff directs the next session to propose a preventive line for the style guide and let you decide on it, rather than assuming.

### Task 2 — the docs are clean on words, so that is not the target

`specific` sits at 0.78 per thousand in the documentation, below natural rate. I recorded explicitly that Task 1's transformation must **not** be run over the docs.

The real target is instructions that are wrong or contradictory, and two are already confirmed:

1. **`FORWARD_DATED_POSTS.md` contradicts the live config.** It asserts `future: true` in two places and calls it foundational; `_config.yml` line 86 sets `future: false`. An agent trusting the document reasons incorrectly about publication.
2. **25 documentation references point at `_publish.sh`**, which fails silently on macOS because BSD sed rejects its `[+-:0-9 ]` character range.

Both are recorded as decisions for you, not unilateral fixes.

---

## The Method Note I Most Want Preserved

I wasted a scan today and recorded both the wrong approach and the right one.

**Wrong**: ratio against the rest of the corpus. It ranks `iondtn`, `kotlin`, `openbsd`, `playdate`, `raycasting` at the top — topic vocabulary, concentrated because the articles are about those things.

**Right**: restrict to a fixed list of content-independent words, then look for outliers. A tic carries no topic content.

**Even that needs judgment.** `key` at 50 per thousand in the Solana articles is cryptographic keys. `structure` in "Structures and the Flight Envelope" is the subject. Never strip a word from an article whose topic is that word.

The handoff also carries the transformation rules **in their required order**, because order was load-bearing: the technical-term guard must run first or the determiner rules defeat it, and display math must be tracked by cumulative delimiter count rather than by "line starts with `$$`". Both of those were silent bugs, caught only by verifying counts on things I had not intended to change.

---

## Items Requiring Your Attention

1. **Task order is unspecified.** You gave both together. The handoff tells the next session to confirm with you rather than guess. Say if you want them run in a particular order, or interleaved.
2. **Task 1 should be batched with a commit per batch.** 265 articles in one transformation is how the resort script destroyed twelve files during the consistency pass.
3. **The two confirmed doc defects are yours to direct.** Aligning the `future:` contradiction could go either way, and `_publish.sh` is your tooling.

---

## State

Tree clean, in sync with `origin/master`, nothing unpushed once this commit lands. No background jobs running. The handoff's validity check passes against the committed state.

Ready for you to compact.
