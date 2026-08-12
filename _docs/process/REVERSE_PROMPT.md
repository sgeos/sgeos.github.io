# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-11
**Task**: Gated the corpus's largest verbal tic and cleared it, refreshed the stale tooling indexes.
**Committed and pushed.** **The citation run has landed and its findings are acted on.**

---

## The Largest Tic In The Corpus Was Never Gated

`rather` appeared **3,739 times**, 99.7 percent of it as `rather than`, at or above the rate limit in
**21 articles** against a corpus median of 1.29 per thousand. **`WATCH_WORDS` held 45 words and
`rather` was not one of them**, so `_verify.py` had never seen any of it.

It is now watched, and all 21 articles are reduced below the limit. **262 replacements**, taking the
corpus to **3,478** uses. Eleven of the articles are published and ten are X-Planes drafts.

**`instead of` cannot be substituted mechanically and my first attempt proved it.** `of` takes a noun
phrase while `than` does not, so "helped by the physics rather than fought by it" became "instead of
fought by it", which is ungrammatical. Only `and not` and `, not` preserve the structure, because any
complement that can follow `than` can follow `not`. I reverted the trial file and restricted the
rotation before touching anything else.

**Neither replacement became a new tic.** The highest rate for either is 3.77 per thousand, against
473 and 332 corpus-wide.

---

## Three Defects I Introduced Doing It, All Caught And Fixed

- **Three double commas**, where `X, rather than Y` became `X,, not Y` because the replacement
  absorbed the preceding space but not a comma already there. Repaired, and the script now absorbs
  the comma so it cannot recur.
- **A false alarm of my own making.** A prose scan reported up to 173 double commas and 276 double
  spaces per file. Both were artefacts of `diction.prose` stripping citation link text, which leaves
  `, ,` behind. **The raw files contain zero double commas.** The checker was wrong, not the corpus,
  which is the trap the new traps document opens with.
- **One genuine registry artefact**, unrelated to this pass, found while checking. A harvested title
  in an unpublished draft read `Col, Demler of A, E, C, , Washington`. The entry is repaired and
  `refs.clean` now collapses a repeated comma, with a test.

---

## The Tooling Indexes Were Stale And I Made Them So

`_lib/README.md` documented ten modules while the library held thirteen. **I added `gate.py`,
`render.py` and `resolve.py` across three commits today and updated the index in none of them.** It is
the entry point the process index points at, so it is what someone would actually read.

It now carries all thirteen, plus the distinction that matters more than the table suggests: **every
module except `render.py` reads markdown source and therefore predicts what the renderer will do
rather than observing it**, and `resolve.py` and `_verify_citations.py` answer different questions
with neither subsuming the other.

`STYLE_VERIFICATION.md` gains sections for rendered output and identifier resolution, including that
`_preview.sh` cannot tell you whether the deploy will pass and that the math check counts by
backslash-run parity.

---

## Verification

- `python3 _verify.py` **0 errors, 0 warnings**, with `rather` now among the 46 watched words.
- `python3 _lib/test_lib.py` **74 of 74**, up from 73.
- `./_check.sh` **passes end to end**: 462 pages, no findings.
- Every one of the 262 replacements was reviewed in word context, not sampled.

---

## The Citation Run Landed, And Both Big Categories Were The Checker

It covered **77,593 citations across 61,483 distinct identifiers**, the first run ever to reach A369,
A370 and the 37-draft publication queue. It reported **195 mismatch, 3 nonexistent and 15,159 weak**.

**I fixed the checker before believing it, and that was right.** 14,979 of the 15,159 weak findings
were labels carrying no title at all, because most of the corpus renders an entry as `Surname Year` by
design. **A title-overlap test against a label with no title is not a test.** The author check also
matched by whole-string containment, so `Henriquez Huecas` cited as `Huecas` read as a wrong work
rather than a wrong name.

**I guessed diacritics were the main cause of the mismatches and I was wrong**, at 2 of 195. The three
I happened to sample made it look typical.

`assess()` now folds diacritics, matches any token of a compound surname, skips the overlap test when
there is no title to overlap, and reports a wrong author name as its own `label-name` verdict, so a
naming defect is neither buried among 15,000 weak findings nor mistaken for a fabricated citation.
Re-assessed from cache with no further network use: **195 to 87 mismatch, 15,159 to 184 weak**.

## The Real Defect Was Reader-Visible And In The Publication Queue

**401 reference labels named the author wrongly.** Each article's throwaway `assemble.py` built its own
link text and took the **last token** of the author string. For `BELL AEROSPACE CO BUFFALO NY` that
gives `NY`, so the prose read **"the MX-2276 system described in NY 1955"**. For `Bardera Mora` it gives
`Mora`, naming a real person incorrectly.

**`refs.display()` was already correct.** This is precisely the duplication the shared library exists
to end, and it reached 31 drafts because the label logic was reimplemented per article rather than
called.

**632 occurrences across 28 drafts were rebuilt from the cached registry record**, leaving 43 mismatch
and 89 label-name as a residue. Anchors were left alone, since a reader never sees them.

## The Drafts Gate Caught One More, And It Was Mine

`./_check.sh --drafts` reported `andnbsp` three times in `draft_summary.html` — a document **describing
that defect** and quoting it in backticks. `render.py` counted `double-escaped` and `literal-nbsp-word`
inside code while every other markup check excluded it. Both now match the others.

## Side Work Is Closed Out

**The handoff was stale and would have failed its own validity check.** It recorded parent `d2ceb3c`
against an actual `HEAD~1` of `0cf2f29`, so the startup protocol would have reported it
invalid-and-stale and refused to proceed. It is refreshed **surgically rather than rewritten**, which is
what its own regeneration rules ask for: carry forward the earned rules, drop what is resolved.

What changed in it: the parent commit and tree state, a note that A370 was published and corrected
without touching the X-Planes rhythm, the three new `_lib` modules, **the corpus baseline moving from
21 warnings to 0**, `./_check.sh`, a pointer to `VERIFICATION_TRAPS.md` rather than a restatement of it,
and the citation residue recorded as an open decision.

**`tmp/` held 2.9 GB and is now 978 MB.** The six throwaway repository build copies, `a328build`
through `a370build` at roughly 180 to 200 MB each, were pure waste once their builds finished. **The
`aNNN` harvest directories were kept**, because `master.json` and the selection data are expensive to
regenerate. This will not recur, since `_check.sh` builds into `mktemp` with a cleanup trap.

---

## The Task Log Had Gone Stale In The Way It Exists To Prevent

The resume check on 2026-08-11 found `TASKLOG.md`'s current-task block naming A333 as **both complete
and next**, and carrying **36 drafted against a working tree holding 37**. The block already contains a
paragraph recording three previous rewrites for exactly this defect, so this is the fourth.

**The counts were re-measured rather than carried forward**: 37 series drafts, A297 through A333, 36 of
which cite a sibling through `post_url`, and 0 published. **A334, the Boeing X-37, is next.**

The handoff's parent commit was advanced to `947d6fa` in the same breath, because the correction moved
the branch tip and would otherwise have made the handoff fail its own validity check.

---

## Outstanding

**Nothing blocking.** The tree is clean, everything is pushed, `_verify.py` reports **0 errors and 0
warnings**, `_lib/test_lib.py` reports **74 of 74**, and `./_check.sh --drafts` passes at 502 pages
with no findings.

**43 mismatch and 89 label-name citation findings remain**, all in unpublished X-Planes drafts. **They
are recorded in the handoff as an open decision and belong to each article's publication review**,
where the context to judge a label exists, not to a bulk pass now.

**A334, the Boeing X-37**, editorial date 2025-11-12, Part 38 of 72, is next and starts on your prompt.
**The thirty-seven X-Planes drafts remain unpublished and unauthorised.**
