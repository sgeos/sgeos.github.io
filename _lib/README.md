# Article Tooling Library

> **Navigation**: [Process](../_docs/process/README.md) | [Documentation Root](../_docs/README.md)

Shared mechanism for the per-article scripts that draft, cite and check posts. Tracked, unlike the
per-article scratch under `tmp/`, which is gitignored.

## Why This Exists

A survey of 457 scratch scripts totalling 78,564 lines found the mechanism copied everywhere and the
lessons copied nowhere.

| | files |
|---|---|
| re-implement the assertion-guarded edit loop | 148 |
| define their own `User-Agent` | 121 |
| hand-roll an HTTP retry loop | 90 |
| re-implement the equation-count guard | 34 |
| carry the title-and-year deduplication fix | 5 |
| carry word-boundary truncation | 2 |
| carry the bold-atomic reflow | 2 |
| **check for doubled backslashes** | **0** |

That last row is the argument. **Five scripts warn about the doubled-backslash trap in their
docstrings and none ever checked for it**, and the bug shipped in three consecutive articles, once
into a file whose own docstring warned against it. A lesson written as a comment is not a guard.

The payloads were never the problem. A representative edit script is 99 to 189 lines of which only 10
to 22 are mechanism, so extracting it touches about an eighth of each script and leaves the
article-specific content alone.

## Modules

| Module | Responsibility | Replaces |
|--------|----------------|----------|
| `fetch.py` | One HTTP client with backoff and per-host throttling, plus Crossref, NTRS, DTIC, OSTI and Open Library adapters | 90 retry loops, 121 user agents |
| `edits.py` | Whitespace-tolerant, all-or-nothing edit application with equation and invariant guards | 148 edit loops |
| `refs.py` | Anchor generation and parsing, link text, deduplication, and the categorised reference block | 19 `gen_refs`, 17 `gen_master` |
| `reflow.py` | Paragraph rewrapping that keeps bold spans and link pairs atomic | 2 partial copies |
| `lint.py` | Mid-edit invariant scan, separating defects from house conventions | 7 `check.py` |
| `diction.py` | Word and phrase overuse, measured against peer articles rather than a fixed threshold | 4 `diction.py` |
| `audit.py` | Equation gaps, citation gaps, thin sections, primary count and fraction | 13 `ref_audit`, 8 `eqn_scan` |
| `numcheck.py` | Harness for re-deriving stated values independently, with property and bisection checks | 18 `verify_numbers` |
| `citations.py` | Registry verification of recalled identifiers, sampling for retrieved ones | 13 `url_check`, 6 `verify_urls` |
| `post.py` | What a post is made of. Document structure, defined once | 7 splits, 9 anchor patterns |
| `test_lib.py` | Regression tests, one per shipped defect, plus anti-duplication guards | |

**The library reproduced its own defect within a day.** An audit found `fold` byte-identical in two
modules, seven independent splits on `## References` across four, and nine hard-codings of the anchor
character class across six. Extracting shared mechanism does not, by itself, stop shared mechanism
reappearing, because re-deriving two lines is always locally cheaper than adding an import.
`post.py` now owns document structure, and three tests fail if a byte-identical function body appears
in two modules, if any module other than `post.py` splits on `## References` or hard-codes the anchor
class, or if `post.py` acquires a library import and makes the graph cyclic.

**`diction.py` is the cautionary case.** A version of it existed in A320 and was copied into A321,
A322 and A323. A369 never received a copy, and the same analysis was redone by hand, rediscovering the
same prose-stripping rules and the same phrase list while missing the acronym check the original had.
Four copies and then silence is the pattern this library exists to end.

**Do not name a module after a standard library module.** `numcheck.py` was first written as
`numbers.py`, which shadowed the standard library and broke `statistics` for every caller through the
`fractions` import chain, because article scripts put `_lib` first on `sys.path`. A test now guards
the whole package against it.

## Usage

```python
import sys; sys.path.insert(0, "_lib")
import edits, lint, refs, reflow, fetch

items = fetch.crossref_search("instruction selection compiler", rows=50)
kept, dropped = refs.dedupe(records)
edits.apply("_drafts/x.markdown", EDITS, reflow_after=True)
print(lint.summary(open("_drafts/x.markdown").read()))
```

Run the tests with `python3 _lib/test_lib.py`. There is no test framework and no third-party
dependency, matching the discipline of `_verify.py`, which must run on a bare runner.

## What Belongs Here and What Does Not

**Mechanism belongs here.** Retry policy, match-exactly-once semantics, anchor uniqueness, truncation
rules, block emission.

**Article content does not.** Harvest queries, cluster definitions and edit payloads are the article's
own argument, and abstracting them would make the work harder rather than easier. They stay in
`tmp/<article>/`.

**Accumulated sweep judgements do not.** Those live in [`_research/`](../_research/README.md), which
holds the per-record rejections and homonym patterns.

## Two Hazards Worth Knowing Before Use

**`reflow` is opt-in per article and is not a corpus normaliser.** Two wrapping conventions coexist.
A369 wraps at 108 columns. The X-Planes drafts are effectively unwrapped at one paragraph per line,
with single lines up to 3,006 characters. Running reflow over an unwrapped draft rewrites thousands of
lines and buries any real change. It is a fixed point after one pass on every file in the corpus, so
it is safe to run repeatedly on an article that already uses it.

**`fetch` returns `None` on failure**, which is the convention the existing scripts use and is
preserved so migration is a rename. It is a genuine hazard, because a caller that forgets to test the
result harvests nothing and reports success. Use `get_json_strict` where a silent empty result would
be worse than a crash.

## Relationship to `_verify.py`

`_verify.py` is the gate. It runs in CI and on pre-push, covers the whole corpus, and every check in it
is an error the corpus is already clean of.

`lint.py` is the workbench. It runs on one file mid-edit and reports house conventions as well as
defects. **Three conventions are deliberately not gates**, because they were measured against the
corpus and tested against kramdown, which renders all three correctly.

| convention | corpus violation rate | kramdown |
|---|---|---|
| bold spanning a line break | 7.7% of posts | renders as `<strong>` |
| display math on two lines | 24.2% of posts | renders as `\[…\]` |
| duplicate reference URL | 19.5% of posts | often legitimate |

Promoting any of those to an error would flag the corpus for defects that do not exist.

## Related

- [Research Sweep Store](../_research/README.md) for rejection records and homonym patterns
- [Publication Review](../_docs/process/PUBLICATION_REVIEW.md) for the pass that uses most of this
- [Style Verification](../_docs/process/STYLE_VERIFICATION.md) for the prose rules `lint` reflects
