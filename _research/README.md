# Research Sweep Store

> **Navigation**: [Process](../_docs/process/README.md) | [Documentation Root](../_docs/README.md)

Durable, repo-level state for literature sweeps. Everything here is tracked, unlike the per-article
scratch directories under `tmp/`, which are gitignored and disappear.

## Why This Exists

Sweep knowledge used to travel by copying `read_and_dropped.json` from one article's working directory
into the next. The chain grew A317 with 35 records, A318 with 247, A319 with 388, A320 with 469, A321
with 481, A322 with 605, A323 with 721, **and then broke at A369**, which rebuilt its filters from
nothing and re-derived a lesson the corpus had already paid for.

**A copied file is not a store.** The break was invisible because nothing referenced the previous copy,
so there was no way for the omission to fail.

## Contents

| File | What it holds |
|------|---------------|
| `rejected.json` | 721 per-record judgements, each with the reason and the article that made it |
| `homonyms.py` | Loader, curated noise patterns, and the filtering helpers |

## The Two Kinds of Knowledge, Which Are Not Interchangeable

**Per-record rejections are exact and need no judgement to reuse.** A paper judged off-topic once should
not be read again. These are keyed by digital object identifier where one is known and by anchor
otherwise, and they carry the reason and the originating article so any reuse is auditable. This is the
reliable half, and it is the half that saves reading time.

**Pattern lessons are generalisations and therefore risky.** A regular expression that removes a real
contaminant in one subject may remove the subject itself in another. Only patterns actually observed to
contaminate a sweep are listed, each with the incident that produced it. **The incident is not
decoration.** It is the evidence that the pattern describes something real, and it is what lets a later
reader decide whether the pattern still applies.

The 721 rejection reasons are the raw material for extending the pattern list. **Extending it is a
reading task rather than a counting one**, and a frequent word in the reasons is not by itself a
justification for a regular expression.

## The Standing Rules

**A filter earned in one article is not automatically valid in the next, in both directions.** Read the
venue histogram of every new sweep. Every contaminant recorded here was found by reading samples of the
results, and none by anticipating it.

**A weak anchor is worse than no anchor.** A relevance test built from `empirical`, `optimization`,
`performance` and `benchmark` admitted a study of industrial chiller faults into a compiler survey,
because those words are common to every empirical field. Anchor on subject nouns.

**Report what was dropped.** `filter_records` returns the dropped set with reasons rather than silently
truncating, because a silent filter reads as complete coverage when it is not.

## Usage

```python
import sys; sys.path.insert(0, "_research")
import homonyms

kept, dropped = homonyms.filter_records(harvested)   # harvested: {key: {title, venue, ...}}
print(f"{len(kept)} kept, {len(dropped)} dropped")
for key, why in dropped.items():
    print(f"  {key}: {why}")

homonyms.record("10.1234/x", "Some Title", "wrong field, marine hydrodynamics", "A370")
```

Inspect the store directly with `python3 _research/homonyms.py`.

## Maintenance

Judgements are additive and tooling never removes them. **If one turns out to be wrong, delete it by
hand and say so in the article that found the error**, so the correction is attributable in the same way
the original judgement is.

Nothing here is imported by `_verify.py` or by the build. This directory is off the deploy path and
carries no runtime dependency.

## Related

- [Research Agent](../_docs/process/RESEARCH_AGENT.md) for how sweeps are run
- [URL Verification](../_docs/process/URL_VERIFICATION.md) for checking what survives a sweep
- [Publication Review](../_docs/process/PUBLICATION_REVIEW.md) for the pass that consumes the results
