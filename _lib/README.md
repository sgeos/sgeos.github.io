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
| `edits.py` | Whitespace-tolerant, all-or-nothing edit application with equation and invariant guards, applied from a TOML edit file by its command line | 148 edit loops, 16 one-shot pass scripts in A381 to A384 |
| `refs.py` | Anchor generation and parsing, link text, deduplication, and the categorised reference block | 19 `gen_refs`, 17 `gen_master` |
| `reflow.py` | Paragraph rewrapping that keeps bold spans and link pairs atomic | 2 partial copies |
| `lint.py` | Mid-edit invariant scan, separating defects from house conventions | 7 `check.py` |
| `sources.py` | The source database, Chicago entries, generated References sections and their drift check. See `_docs/writing/CITATION_STYLE.md` | per-article `refsNNN.py` generators |
| `sources_import.py` | Draft source records from Crossref, pinned Wikipedia revisions and related posts, and import a whole post from a TOML decision file | hand-typed reference labels, the A384 prototype scripts |
| `diction.py` | Word and phrase overuse, measured against peer articles rather than a fixed threshold | 4 `diction.py` |
| `audit.py` | Equation gaps, citation gaps, thin sections, primary count and fraction | 13 `ref_audit`, 8 `eqn_scan` |
| `numcheck.py` | Harness for re-deriving stated values independently, with property and bisection checks | 18 `verify_numbers` |
| `citations.py` | Registry verification of recalled identifiers, sampling for retrieved ones | 13 `url_check`, 6 `verify_urls` |
| `post.py` | What a post is made of. Document structure, defined once | 7 splits, 9 anchor patterns |
| `gate.py` | Subject-anchor gating for a harvested corpus, with the two-sided random audit that is the only thing detecting a mis-tuned gate | 2 copied `select.py` |
| `render.py` | Audit of BUILT HTML for defects a reader would see, including same-site links to a missing fragment, and page-weight reporting | 1 ad hoc `audit_html.py`, 1 `fragcheck.py` |
| `resolve.py` | Whether a cited identifier resolves at all, with registry fallback and bot-mitigation handling | 3 rewritten `sweep.py` |
| `survey.py` | Recomputation of the statistics an article states about its own reference survey, since a presence check goes green precisely when a number goes stale | scratch `verify_survey.py` |
| `progress.py` | Recomputation of the drafted count a resume channel states, against the drafts on disk | nothing, the count was maintained by hand |
| `registry.py` | Command line for Crossref and OpenAlex search, abstract lookup and grep, DOI metadata with handle status, and OpenAlex work types | 37 raw-HTTP query scripts in A375 to A384 |
| `harvest.py` | The survey pipeline, harvest, select, master and assemble, driven by one TOML file per article | per-article `harvest`, `select`, `gen_master`, `assemble` |
| `textscan.py` | Context search in saved source text and removal of references from wikitext | 4 `ctx.py`, 3 `clean.py` |
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

**One distinction matters more than the table suggests.** Every module above except `render.py` reads
**markdown source**, so every one of them predicts what kramdown and MathJax will do rather than
observing it. Run corpus-wide on 2026-08-11, `lint.py` reported 1,596 defect-severity findings and the
rendered pages carried none of them. `render.py` is the only instrument that sees what a reader sees,
and `./_check.sh` at the repository root runs it the way CI does.

**`resolve.py` and `citations.py` answer different questions and neither subsumes the other.**
`resolve.py` asks whether an identifier resolves at all, which catches a dead landing page.
`_verify_citations.py` asks whether it resolves to **the work it is cited as**, which catches a wrong
identifier. An HTTP 200 does not verify a citation.

## The Library Was Being Bypassed, and Why

A second survey on 2026-10-24 found 4,368 distinct scratch scripts outside the repository, totalling 689,243
lines. Across the whole of `tmp/` the library was adopted, with 366 scripts importing `fetch`. In the ten
articles A375 to A384 it was not.

| A375 to A384, 100 distinct scripts | files |
|---|---|
| open their own HTTP connections | 37 |
| import `fetch` | 4 |
| re-implement the exactly-once edit loop | 16 |
| import `edits` | 0 |

**A module with no command line is bypassed by one-shot work.** Every bypassing script was a few lines, a
search, an abstract lookup or a single edit pass, and for a one-shot task retyping a loop is cheaper than
writing a script that imports one. The fix is a command line that ingests data, so the article's part is a
list of queries or a file of edits and nothing else.

| Command | Data it reads |
|---|---|
| `python3 _lib/edits.py apply EDITS.toml [POST]` | `[[edit]]` tables, `old` and `new`, or `after` or `before` with `insert` |
| `python3 _lib/registry.py crossref QUERY...` and `openalex` | Queries, or `@FILE` with one per line |
| `python3 _lib/registry.py abstract DOI...`, `works` and `type` | Identifiers, or `@FILE` |
| `python3 _lib/harvest.py harvest CONFIG`, `select`, `master` and `assemble` | `tmp/<article>/survey.toml`, the queries, rounds, anchors and clusters |
| `python3 _lib/sources_import.py fetch-crossref`, `pin-wiki` and `import` | `_sources/decisions/<article>.toml`, the human decisions on titles, notes and corrections |
| `python3 _lib/textscan.py ctx FILE REGEX` and `strip-wikitext` | A saved source file |

**TOML literal strings cannot carry the doubled-backslash defect.** `'''...'''` takes no escapes, so
`\mathcal` is one backslash on disk and one in the article. Python string literals needed `\\mathcal`, and
the defect shipped in three consecutive articles through them.

**An edit file refuses to apply twice.** An insertion still finds its anchor after it is applied, so a
second run of a one-shot script inserted the text again. `edits.py` refuses an edit whose result is already
present unless `--rerun` is passed, and then skips it.

**Each promoted pipeline was checked against the copy it replaces.** On A372's saved pools, `harvest.py`
`select`, `master` and `assemble` produce output identical to A372's own scripts run against the same
rejection store, byte for byte for the assembled draft. Against A372's outputs as saved on the day, `select`
keeps 152 fewer records, all removed by rejections added to `_research/rejected.json` since. Rebuilding
A384 from `_sources/decisions/A384.toml` reproduces its 99 stored records exactly, which `test_sources.py`
checks wherever the scratch registry cache exists and reports as skipped elsewhere.

**Reviewed and deliberately not promoted.** The corpus campaigns under `tmp/cite/`, `tmp/fix5/`, `tmp/fix6/`
and the `retrofit/` directories, which include `build_drop`, `splice`, `draw_sample`, `thin`,
`gate_and_cluster`, `write_notes` and `make_chunks`, were one-time corpus operations that are complete, and
the handoff forbids rerunning the stale generators among them. `calc.py` and `verify_numbers.py` are article
content on top of `numcheck.py`. `wordcheck.py` and `phrases.py` are already `diction.py outliers` and
`diction.py formulas`.

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
own argument. They stay in `tmp/<article>/`, but as data files read by a tracked command rather than as
scripts that carry their own copy of the mechanism.

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
