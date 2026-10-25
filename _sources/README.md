# Source Database

> **Navigation**: [Citation Style](../_docs/writing/CITATION_STYLE.md) | [Documentation Root](../_docs/README.md)

One record per cited source. Every converted article's References section is generated from these
records by `_lib/sources.py`, so a correction made here reaches every article that cites the source.
The rules the records follow are in [Citation Style](../_docs/writing/CITATION_STYLE.md).

**Status.** Prototype in use, holding the converted articles A297 to A384. Counts are in the latest
[Reverse Prompt](../_docs/process/REVERSE_PROMPT.md) entry, since they change with every import. Most sources
belong to the reference surveys of A297 to A373. Sources the articles share are one record each. The procedure is
[Source Conversion](../_docs/process/SOURCE_CONVERSION.md).

## Layout

| Path | Contents |
|------|----------|
| `records/<c>.jsonl` | Source records, one JSON object per line, sorted by anchor. `<c>` is the first character of the anchor after any legacy prefix such as `research_` or `ref_` |
| `venues.jsonl` | Whether each journal or proceedings referees full papers, with the basis and the evidence read |
| `decisions/<article>.toml` | The human decisions made when an article was imported, read by `sources_import.py import` |
| `articles/<post stem>.json` | For an article that names a source differently from the store, its names mapped to canonical anchors |
| `articles/<post stem>.links.json` | Link text in an article that is not a citation label, left alone by `fix-labels` |
| `domains.toml` | Judgements about publishers of web sources, made once per host, each with its reason |
| `acronyms.txt` | Words kept in capitals when a title registered in capitals is recased, derived from registry titles by `sources_import.py acronyms` |
| `publishers.toml` | A publisher's own statement that it peer reviews, with a verbatim quote, applied to its venues by `credit-venues` |

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
python3 _lib/sources_import.py import POST DECISIONS --write --refresh   # also rebuild unannotated records
python3 _lib/sources_import.py import PRE.markdown DECISIONS --as-post POST --write   # from a pre-conversion copy
python3 _lib/sources_import.py fetch-reports ntrs|osti|openlibrary tmp/sources POST... [--ids FILE] [--shard k/n]
python3 _lib/sources_import.py fetch-openalex DOIS.txt tmp/sources      # OpenAlex, a hundred DOIs a request
python3 _lib/sources_import.py read-archive META.json... --out OUT.json # Internet Archive captures' own metadata
python3 _lib/sources_import.py acronyms tmp/sources --write             # rebuild acronyms.txt
python3 _lib/survey.py years POST... [--edits FILE.toml]                 # recompute stated year statistics
python3 _lib/sources_import.py credit-venues [--write]                   # apply publishers.toml
python3 _lib/sources.py fix-labels POST     # set in-text labels to the database's
python3 _lib/sources.py diff-labels PRE POST   # what conversion changed, labels apart
```

**A DOI cited is the DOI kept.** Crossref answers some DOIs with another, its primary, for a work registered
twice. The record keeps the DOI the article cited and stores the primary as `doi_primary`, because the link
must still lead where the article said. `diff-labels` compares every link target as well as the text, so a
changed target fails the comparison.

**`--refresh` rebuilds a record from its registry data** when the importer's rules change. A record whose `note`
records a human decision is never rebuilt, and Wikipedia and related-post records are left alone. A note the
importer itself writes about provenance, such as "Metadata from the NASA Technical Reports Server record", marks
no correction, so such a record is rebuilt; the patterns are `_PROVENANCE` in `_lib/sources_import.py`.

**An import from a pre-conversion copy needs `--as-post`.** An article's name map is filed under its post's
name, and an import given a copy once filed it under the copy's name, which no article reads.

**Where a record comes from.** In order of preference, a DOI's record is Crossref's, then OpenAlex's for a DOI
Crossref lacks, then OpenAlex's fetched in bulk for a harvested survey. A NASA Technical Reports Server, OSTI or
Open Library link takes its server's own record. A web page takes the metadata read from it, and only a page
that refused reading falls back to the article's label. Each record's note says which.

**Publisher statements.** A venue may be credited from its publisher's own statement in
`publishers.toml`. Each entry names the publisher as Crossref spells it, with aliases, says whether it covers
journals, proceedings or both, may narrow itself to a series with `venue_pattern`, and records the reviewers
the statement names and each source read, with its URL, quote, reading date and method. A quote read through
a summarising fetch may be a fragment, which the file's header says. A venue carrying
`no_publisher_credit` is never credited this way, because its own pages say otherwise.

**One source, one record, across articles.** A record's identity is its DOI, its Wikipedia page and revision,
or its post. An import that meets an identity already stored keeps the stored record and its corrections. It
adds any new section locators for a related post, and applies this article's own decisions about the record.
**An article keeps its own names.** When an article cites a stored source under another name, its map in
`articles/` points that name at the stored record. When an article's name is already taken by a different
source, such as a second `research_smith_2020` or a page read at another revision, the new source is stored under
a canonical name with a suffix derived from its identity, and the article's map points its name there. The
article's text never changes for either case, and `sources.py` resolves every name through the article's map
first.

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
