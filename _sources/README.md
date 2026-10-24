# Source Database

> **Navigation**: [Citation Style](../_docs/writing/CITATION_STYLE.md) | [Documentation Root](../_docs/README.md)

One record per cited source. Every converted article's References section is generated from these
records by `_lib/sources.py`, so a correction made here reaches every article that cites the source.
The rules the records follow are in [Citation Style](../_docs/writing/CITATION_STYLE.md).

**Status.** Prototype. It holds the 99 sources of A384, *Mercury as a Colony and a Launch Site*, the
only converted article. Records were imported on 2026-10-24.

## Layout

| Path | Contents |
|------|----------|
| `records/<c>.jsonl` | Source records, one JSON object per line, sorted by anchor. `<c>` is the first character of the anchor after any legacy prefix such as `research_` or `ref_` |
| `venues.jsonl` | Whether each journal or proceedings referees full papers, with the basis for the judgement |

Jekyll copies no directory whose name begins with an underscore, so nothing here becomes a page. The
repository is public, so the data is public.

## Commands

```sh
python3 _lib/sources.py validate            # every record and venue against the schema and the rules
python3 _lib/sources.py render POST         # print the section the database would generate
python3 _lib/sources.py write POST          # replace the section in place
python3 _lib/sources.py check POST...       # report drift, also run by _verify.py
python3 _lib/test_sources.py                # regression tests
```

## Editing

**Edit records, not articles.** A hand edit to a generated References section fails `_verify.py` as
`sources-drift`. Change the record, run `validate`, then `write` each article that cites it.

**Records are written by `sources.save_records`**, which sorts and shards them. Editing a shard by hand
is safe if the line stays valid JSON and the file stays sorted, and `validate` reports any mistake.

**Human decisions live on the record.** `synthesis` marks a review rather than a report of the
authors' own work. `stake` marks a publisher with an interest in the subject. Corrections to registry
data carry a `note` saying what was wrong and where the correct value came from. A record's `rule` and
`section` must be what the classification rules give, so a reclassification is made by changing the
decision that drives it, never the section alone.
