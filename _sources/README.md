# Source Database

> **Navigation**: [Citation Style](../_docs/writing/CITATION_STYLE.md) | [Documentation Root](../_docs/README.md)

One record per cited source. Every converted article's References section is generated from these
records by `_lib/sources.py`, so a correction made here reaches every article that cites the source.
The rules the records follow are in [Citation Style](../_docs/writing/CITATION_STYLE.md).

**Status.** Prototype in use. It holds 342 sources and 101 venues for the five converted articles, A380 to
A384, *Who Keeps the Value When a Company Splits* through *Mercury as a Colony and a Launch Site*, imported
on 2026-10-24. Sources the articles share are one record each. The procedure is
[Source Conversion](../_docs/process/SOURCE_CONVERSION.md).

## Layout

| Path | Contents |
|------|----------|
| `records/<c>.jsonl` | Source records, one JSON object per line, sorted by anchor. `<c>` is the first character of the anchor after any legacy prefix such as `research_` or `ref_` |
| `venues.jsonl` | Whether each journal or proceedings referees full papers, with the basis and the evidence read |
| `decisions/<article>.toml` | The human decisions made when an article was imported, read by `sources_import.py import` |

Jekyll copies no directory whose name begins with an underscore, so nothing here becomes a page. The
repository is public, so the data is public.

## Commands

```sh
python3 _lib/sources.py validate            # every record and venue against the schema and the rules
python3 _lib/sources.py render POST         # print the section the database would generate
python3 _lib/sources.py write POST          # replace the section in place
python3 _lib/sources.py check POST...       # report drift, also run by _verify.py
python3 _lib/test_sources.py                # regression tests

python3 _lib/sources_import.py fetch-crossref POST CACHE_DIR
python3 _lib/sources_import.py pin-wiki POST PINS.json --saved DIR
python3 _lib/sources_import.py review POST DRAFTS.json --flagged --second-opinion --saved DIR
python3 _lib/sources_import.py import POST _sources/decisions/AXXX.toml [--write] [--replace]
python3 _lib/sources.py fix-labels POST     # set in-text labels to the database's
```

**One source, one record, across articles.** A record's identity is its DOI, its Wikipedia page and revision,
or its post. An import that meets an identity already stored keeps the stored record and its corrections. It
adds any new section locators for a related post, and applies this article's own decisions about the record.
The same anchor with a different identity is a conflict. All fourteen Wikipedia pages that A380 to A384 share
were read at the same revision. A page read at two revisions would need two records and per-article anchor
mapping, which is not built.

**Importing an article.** Cache its Crossref records, pin its Wikipedia links against the copies that were
read, then run `import` without `--write`. It prints each new record with the registry title beside the
proposed headline-case title, and every record that differs from the store as a conflict. Put each decision
in the article's decision file and rerun until the output is right, then add `--write`. A conflict is never
written without `--replace`, so an import cannot silently overwrite a corrected record.

## Editing

**Edit records, not articles.** A hand edit to a generated References section fails `_verify.py` as
`sources-drift`. Change the record, run `validate`, then `write` each article that cites it.

**Records are written by `sources.save_records`**, which sorts and shards them. Editing a shard by hand
is safe if the line stays valid JSON and the file stays sorted, and `validate` reports any mistake.

**A venue is credited with peer review only when it can be said by whom.** Set `peer_reviewed` true only
after reading a source the venue speaks through that answers the question, record the answer as
`reviewers`, and list each source in `evidence` with its `url`, a verbatim `quote`, the `read` date and
`method` `fetched`. `validate` refuses anything less. A venue that an import meets for the first time is added as not
established. See [Citation Style](../_docs/writing/CITATION_STYLE.md) under Default deny.

**Human decisions live on the record.** `synthesis` marks a review rather than a report of the
authors' own work. `stake` marks a publisher with an interest in the subject. Corrections to registry
data carry a `note` saying what was wrong and where the correct value came from. A record's `rule` and
`section` must be what the classification rules give, so a reclassification is made by changing the
decision that drives it, never the section alone.
