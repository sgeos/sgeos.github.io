# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-11
**Task**: New tooling, promotion of ad hoc tooling, and the verification record.
**Committed and pushed.** **The citation run is still in flight and is reported separately.**

---

## `./_check.sh` Runs The Deploy Gate Locally

`_preview.sh` shows you a page and **cannot** tell you whether the deploy will pass, because it ends
in `jekyll serve --watch` and nothing can run after it. That is now stated in its own header.

```sh
./_check.sh              # _verify.py, a production build, then the rendered audit
./_check.sh --drafts     # include drafts
./_check.sh --weights    # also report page weight
```

It builds into a throwaway directory rather than `_site`, because `_site` is what `jekyll serve`
writes and clobbering it mid-preview is confusing.

**One defect found while writing it, worth knowing.** Jekyll cleans its destination before building,
so a build log written into the destination is deleted by the build it was meant to record. The log
now lives outside.

---

## Page Weight Is Measured For The First Time

`python3 _lib/render.py <site> --weights`. **It is reported and deliberately not gated**, because a
comprehensive survey is an editorial choice rather than a defect.

| Measure | Value |
|---|---|
| Pages | 462, totalling 45.0 MB |
| Median page | 84 KB |
| A370 | **776 KB, 9.2 times the median** |
| A369 | **573 KB, 6.8 times the median** |
| Next largest | 333 KB, an ordinary SpaceX history article |

The two survey articles are in a class of their own, and nothing measured that until now.

---

## Ad Hoc Tooling Promoted

**`_lib/resolve.py`**, from `tmp/a370/sweep.py`, which had been written from scratch three times. It
answers whether a cited identifier resolves at all, which is a **different and weaker** question than
the one `_verify_citations.py` answers, and neither subsumes the other.

It carries the two facts each rewrite had to rediscover. **An HTTP failure is usually not a citation
failure**, since publishers run bot mitigation and a Defense Technical Information Center deposit
refuses the connection outright, so 202 and 403 count as resolution. **The fallback must be a
different route rather than a retry**, so it asks the issuing registry, Crossref and then DataCite,
because LIPIcs deposits with the latter and a Crossref-only check reports a valid identifier as
missing.

Sampling requires a seed and has no default, the same rule `gate.audit` follows, because an unseeded
sample is not a reproducible measurement.

---

## `_verify_citations.py` Reports Per Article

A flat problem list is unactionable when one article carries thousands of citations. **Two articles
hold 92 percent of the corpus's 4,036 DOI citations**, at 1,960 and 1,759, so a single corpus verdict
says almost nothing about the other 47 posts and buries whichever of the two is worse. It now prints a
per-article table of checked, mismatch, absent, weak and a hard-problem rate, worst first.

---

## The Verification Record

**[`_docs/process/VERIFICATION_TRAPS.md`](./VERIFICATION_TRAPS.md)** records the mistakes the working
method has actually made and the observation that caught each one. The repository already applies that
rule to `_verify.py`, where every check exists because the defect shipped. This applies it to the
method.

**The common root is asserting a property instead of measuring it.** Eight entries, each with a
concrete failure: the sticky working directory, the checker whose second wrong version masked its
first, mixing two instruments' numbers in one sentence, a rate that cannot tell a term of art from a
tic, a style substitution that changed a claim, a category rename that moved live URLs, reporting a
finding the repository had already documented, and a source check answering a rendering question.

**[`URL_VERIFICATION.md`](./URL_VERIFICATION.md)** gains a citation cadence section with a run record,
since nothing runs `_verify_citations.py` automatically and nothing will remind you.

---

## Verification

- `python3 _verify.py` **0 errors, 0 warnings**.
- `python3 _lib/test_lib.py` **73 of 73**, up from 69. Four new tests cover bot-mitigation status
  handling, identifier extraction, the required sampling seed, and the registry-only fraction.
- `./_check.sh` **passes end to end**: 462 pages, no findings.

---

## Outstanding

**`_verify_citations.py` is still running** and has been for over an hour, taking the cache from
45,752 to 50,477 entries. It is the first run covering A369 and A370. **I will report it per article
when it lands, and the run record in `URL_VERIFICATION.md` points at the TASKLOG entry rather than
claiming a result.**

**A334, the Boeing X-37**, on your prompt. **The thirty-seven X-Planes drafts remain unpublished and
unauthorised.**
