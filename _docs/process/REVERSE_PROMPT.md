# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-11
**Task**: Corpus word-usage triage, tooling promotion, and housekeeping.

**`_verify.py` now reports 0 errors and 0 warnings.** The baseline for this whole session was 0 errors
and 21 warnings, and it had never been zero before.

---

## Only One Article Needed Rewriting, And My Earlier Recommendation Was Wrong

**I previously recommended rewriting four live SpaceX history articles for `configuration`. That
recommendation was wrong and I withdrew it after measuring properly.**

The error was direction. For a noun the compound is formed by the word BEFORE it, and I had read the word
after. Measured correctly, the modified share is **98 percent in value_capture, 99 percent in
decomposability, 79 percent in generality_forcing and 62 percent in governance**, led by "capability
configuration" at 39 uses and "decomposability configuration" at 25. Those name distinct configurations the
series analyses. **The determiner-led residue is ordinary anaphora with a named antecedent.**

**The one genuine tic was `substantial`** in the hardware description languages article, at 29 uses and
10.6 per thousand. It is an adjective that never forms a compound, and it was imprecise in an article that
elsewhere quotes percentages. It now stands at **6 uses and 2.20 per thousand**, with 23 replacements
varied across nine different words so that one vague quantifier did not become another. No replacement
exceeds 1.10 per thousand.

**Nine warnings were term-of-art false positives** and are now recorded in `_verify_exemptions.yml` with a
measured modifier split each, per that file's rule that a reason is an auditable claim.

---

## The Tooling Now Carries The Discriminator, And It Refuses To Give A Verdict

`_lib/diction.py` gains `collocations`, `top_collocate`, `word_rates`, `word_outliers`, `TICS` and a
`collocation_report`, plus a command line.

```sh
python3 _lib/diction.py collocate substantial _posts/<file>.markdown
python3 _lib/diction.py report _drafts/<file>.markdown '_posts/*.markdown'
```

**`_verify.py` word-frequency warnings now carry their own evidence**, so a reader can triage without
rerunning anything.

```
`specific` 59x = 15.6/1k (limit 5.0, top collocate `specific impulse` 57x = 86%)
```

**The tool reports and deliberately does not classify.** An automatic verdict would need to know that
"achieved substantial" is a verb followed by an adjective while "capability configuration" is a compound
noun, which is a part-of-speech judgement with no tagger behind it. A wrong verdict would license deleting
a term of art from a published article, so the human still writes the reason.

`_lib/test_lib.py` goes from **54 to 58 tests**, covering the term-of-art discriminator, the function-word
skip, the both-directions requirement, and the silent-peer-counts-as-zero rule.

---

## I Applied Two Fixes To The Wrong Directory And Caught It Afterwards

**The Bash working directory persists between commands, and I had left it inside a throwaway build copy.**
The eight draft date changes and the category rename were written into `tmp/dbuild`, verified there, and
then deleted with it. The "0 errors, 0 warnings" I first observed was measured against that copy.

The diagnosis and the fixes were correct. They were re-applied to the real repository with absolute paths
and re-verified. **The lesson is that a `cd` into a scratch tree is sticky and a later edit will silently
land there**, and that git status is what catches it.

---

## Housekeeping, All Four Done

**The `--drafts` build was broken repository-wide and now is not.** `_drafts/draft_summary.md` carried a
bare `{% post_url %}` with no argument in prose about converting forward references. Jekyll parsed it as a
real tag, so every drafts build failed, including `DRAFTS=1 ./_preview.sh`. It is now inside a `raw` block.
**This is a separate cause from the unresolved-cross-reference policy `CLAUDE.md` describes.**

**Eight drafts were dated on days already used by published posts.** No published date in the corpus carries
two posts, so one article per day is a hard convention and these eight would have violated it at
publication. They are moved to the eight consecutive free days from **2026-08-12 to 2026-08-19**, order
preserved, all forward-dated so nothing back-dates into an occupied calendar. **The specific dates are
arbitrary and easy to change if they cut across your editorial plan.**

**The `categories/c` build conflict was a real defect that was losing a page.** `c` and `c++` both slugify
to `c`, so `jekyll-archives` wrote `/categories/c/index.html` twice and one archive silently overwrote the
other. `/categories/cpp/` returned 404 on the live site. The category is renamed to `cpp` in the two posts
that carry it. **Neither post lists it first, so under the default permalink no post URL changes.** Both
archives now generate, with 4 posts under `c` and 2 under `cpp`.

**The announcement commit is pushed**, along with everything above.

---

## Verification

- `python3 _verify.py` **0 errors, 0 warnings**, from the repository root.
- `python3 _lib/test_lib.py` **58 of 58**.
- **Isolated production build exit 0, no conflict**, and **isolated drafts build exit 0**.
- Both category archives generate and A370 still builds.

---

## Standing Work, Which I Have Not Started And Will Not Assume

**A334, the Boeing X-37**, is next in the X-Planes series at editorial date 2025-11-12, Part 38 of 72. It is
a four-pass job and starts on your prompt.

**The thirty-seven X-Planes drafts remain unpublished.** Publication has never been authorised for them, and
I did not read the A370 authorisation as extending to them. Publishing thirty-seven articles is
irreversible and outward-facing, so it needs its own instruction.
