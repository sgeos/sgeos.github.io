# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-05
**Task**: Task 2 complete. Documentation and process files reviewed for pathological instructions,
and every finding rectified. Both queued tasks are now done.

---

## Your Hypothesis Was Half Right, and I Can Say Which Half

You suggested the surviving `specific` overuse came either from faulty instructions or from a
pathological reference article. I tested both. **Both are false.**

**Not an exemplar.** The writing documentation names two exemplar ranges, `A152` through `A160`
in `ARTICLE_GENRES.md` and `A153` through `A160` in `SUBSYSTEM_DEEPDIVE_STRUCTURE.md`. I measured
every one, before and after the remediation pass. They run **0.0 to 1.6 uses per thousand**
against a natural rate near 1.7. The documented models were never contaminated.

**Not a faulty instruction.** No writing or process document encourages the word, and none tells
an agent to match sibling prose style.

**It was a missing check.** `STYLE_GUIDE.md` constrained punctuation, links, references, and
slugs, and said nothing whatever about word choice. `PUBLICATION_REVIEW.md` scoped "Prose Style"
to contractions, dashes, colons, semicolons, parentheticals, and line structure. The verification
script counted em-dashes, contractions, math, and anchors. **Nothing in the pipeline could see a
repeated word.**

That is why it survived resets. Each new session inherited a review process structurally blind to
the defect, so the worst article in the corpus, at 46.2 uses per thousand, passed publication
review with prose style reported clean. The rules were fine. The instruments were missing.

---

## What I Changed to Close It

- **`STYLE_GUIDE.md`** gains a Diction and Repetition section: do not calibrate density against
  recent siblings, delete the empty intensifier, vary formulaic phrasing across a rotation, and
  preserve the word where it carries meaning.
- **`PUBLICATION_REVIEW.md`** gains a Diction and Repetition check, framed as a flag needing
  judgment rather than a verdict, with three outcomes: legitimate, filler, formulaic.
- **`STYLE_VERIFICATION.md`** gains a word-frequency script restricted to content-independent
  words. **Verified end to end**: it flags the worst pre-pass article at 39.2 per thousand and
  passes that same article after remediation.
- **`COMMON_ERRORS.md`** records the whole episode, including both falsified hypotheses.

---

## The Serious Find, Which Was Not About Word Usage

**`FORWARD_DATED_POSTS.md` contained build-breaking advice.** It asserted `future: true` in five
places, quoted a `_config.yml` excerpt that does not exist, called the setting foundational, and
stated that a post may cross-reference a forward-dated post in either direction.

The live setting is `future: false`. Rather than reason about the consequence, I built a minimal
two-post site to find out:

```
Liquid Exception: Could not find post "2027-01-01-futurepost" in tag 'post_url'.
ERROR: YOUR SITE COULD NOT BE BUILT
```

An agent following that document would have taken **the entire site** down, not one page. The
error had propagated to five further locations, all corrected.

`CROSS_LINKED_SERIES.md` carried a related defect: it claimed that staging a batch together makes
all internal tags resolve. That holds **only when every article in the batch is back-dated**. The
three safe date configurations are now enumerated.

---

## Also Fixed

- **`_publish.sh` works again.** Its bracket expression `[+-:0-9 ]` reads as the range `+` to `:`,
  which BSD sed rejects. On macOS it reported every file as undated, moved nothing, and **exited
  zero**. Moving the hyphen to the front is portable across BSD and GNU sed. Confirmed to extract
  a date where it previously extracted none.
- **`CROSS_LINKED_SERIES.md` no longer tells you to publish unverified.** It had named the deploy
  build the authoritative verification because the local bundle is broken, which means letting the
  live site find the errors. It now carries the Gemfile-free scratch-copy procedure.
- **`STYLE_VERIFICATION.md`** wrote scratch to `/tmp` against your project-local convention, and
  said "expect 200 across the board" without recording that a 200 does not verify a citation, the
  failure mode behind the thirteen fabricated citations.
- **`CLAUDE.md`** now records that `_preview.sh` passes `--future` while the live site does not,
  so a clean preview is **not** evidence that a forward-dated cross-reference is safe.
- A relative-link example in `DOCUMENTATION_STRATEGY.md` corrected.

---

## Items Requiring Your Attention

1. **I changed `_publish.sh`.** It is your tooling and I had left it alone twice before. You told
   me to rectify what I found, and it was broken in a way that fails silently. Revert if you
   disagree with touching it.
2. **`future: false` is now documented as the intended policy**, because that is what the
   configuration says and what the site does. If you actually want `future: true`, that is a
   configuration change with real consequences, and it would invalidate the back-reference-only
   convention. I did not touch `_config.yml`.
3. **`_preview.sh` could drop `--future`** to make previews match the live site. I did not change
   it, since seeing forward-dated work is probably why the flag is there. Documented instead.

---

## State

Branch `master`. Full site build verified in a Gemfile-free scratch copy after the edits. Zero
broken relative links across all documentation. No background jobs running.
