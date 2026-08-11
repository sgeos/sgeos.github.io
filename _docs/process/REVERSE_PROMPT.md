# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-11
**Task**: Gated the corpus's largest verbal tic and cleared it, refreshed the stale tooling indexes.
**Committed and pushed.** **The citation run is still in flight.**

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

## Outstanding

**`_verify_citations.py` is still running.** It is now clear why it is slow, and the reason corrects
something I told you earlier. The repository holds **77,593 DOI citations, of which 73,557 are in the
37 unpublished X-Planes drafts** and only 4,036 in published posts. My earlier figure of 4,036 was
`_posts` alone and I described it as the corpus. **The run is verifying the publication queue, which
has never been checked**, across 61,483 distinct identifiers.

I will report it per article when it lands. **The run record in `URL_VERIFICATION.md` points at the
TASKLOG entry rather than claiming a result.**

**A334, the Boeing X-37**, on your prompt. **The thirty-seven X-Planes drafts remain unpublished and
unauthorised.**
