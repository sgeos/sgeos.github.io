# Source Conversion

> **Navigation**: [Process](./README.md) | [Citation Style](../writing/CITATION_STYLE.md) | [Source Database](../../_sources/README.md)

How an article's legacy reference list is converted to Chicago author-date entries generated from the source
database. Five articles have been converted this way, A380 to A384, on 2026-10-24. A384 was converted first by
hand, and the procedure below is what the other four needed.

## The Procedure

Each step is a command that reads data. Scratch goes under `tmp/<article>/sources/`. Human decisions go in
`_sources/decisions/<article>.toml`, which is tracked.

1. **Cache the registry records.** `python3 _lib/sources_import.py fetch-crossref POST tmp/aNNN/sources/crossref`.
   It resumes, so rerun it until nothing is missing. Missing records were transient network failures in every
   case so far.
2. **Pin the Wikipedia links.** `python3 _lib/sources_import.py pin-wiki POST tmp/aNNN/sources/wiki_pins.json
   --saved tmp/aNNN/wiki`. A pin is verified in one of three ways.
   - `exact` means saved wikitext is byte-identical to the revision current when the copy was saved.
   - `stripped` means the same, apart from surrounding whitespace.
   - `embedded` means a saved rendered page carries the revision id in its own configuration, which is how A380's
     pages were pinned.

   A copy saved under a shorter name, such as `Sphere_of_influence.txt` for *Sphere of influence
   (astrodynamics)*, is accepted only if byte-identical. Pass a sibling article's directory as a second `--saved`
   when a copy was saved there. The first directory given wins, and the evidence names the article whose scratch
   held the copy.
3. **Dry-run the import** with a decision file that holds only `article`, `crossref_cache` and `wiki_pins`.
   `python3 _lib/sources_import.py import POST _sources/decisions/AXXX.toml --drafts tmp/aNNN/sources/drafts.json`.
   It reports which records are new, which are already stored, which it extends, and every conflict.
4. **Review.** `python3 _lib/sources_import.py review POST tmp/aNNN/sources/drafts.json --flagged
   --second-opinion --saved tmp/aNNN/wiki`. Every drafted title is compared with the article's legacy label,
   which was checked by hand when the article was drafted. A record is flagged for each of the following.
   - Its words differ from the label.
   - Its year or author list disagrees with the label.
   - It has no pages, volume, publisher or authors.
   - Its container looks concatenated.

   For author findings, review also prints OpenAlex's author list. It also prints any fuller author list found in
   the citation templates of the saved wikitext. Each finding is a question for a person, not a verdict.
5. **Record decisions** in the decision file, as `[title]`, `[note]`, `[synthesis]` and `[fix.<anchor>]` tables.
   Every correction carries a note saying what was wrong and where the right value came from. Rerun steps 3 and 4
   until review shows only the findings you mean to keep.
6. **Write.** Add `--write` to the import. Decisions about a record already stored from another article amend
   it. A different source under a stored anchor is a conflict and is never written without `--replace`.
7. **Credit the venues.** New venues arrive as not established. A venue is credited only with a recorded answer
   to the question of by whom, read from a source the venue speaks through. See [Citation
   Style](../writing/CITATION_STYLE.md) under Default deny.
8. **Generate and relabel.** `python3 _lib/sources.py write POST`, then `python3 _lib/sources.py fix-labels POST`,
   then `python3 _lib/sources.py check POST`.
   - `fix-labels` sets each in-text label to the database's author and year. This covers three-author works
     becoming "et al." and year suffixes such as McInnes 1999a and 1999b. A locator after the year is kept.
   - Check the prose for sentences that describe a label, such as "it is cited as unattributed", and correct them
     with an edit file.
9. **Diff the body against a copy taken before step 8.** Only in-text labels, and any sentence corrected on
   purpose, should differ.
10. **Gate.** `python3 _verify.py --strict`, then `./_check.sh`.

## Registry Habits Found So Far

Each of these is now handled by the importer or recorded as a decision, and each has a test.

| Habit | Example | Handling |
|---|---|---|
| Incomplete author list | Wieczorek et al. 2006 given as one author | Decision, from the pinned Moon wikitext |
| Affiliation entered as an author | Janhunen 2025 | Decision |
| No author at all | AIAA 1977-536 | Listed under its title, cited by a short title |
| Misspelt author | Mclnnes for McInnes, in both registries | Decision |
| Name in capitals | `JAMES K.` | Importer recases word by word |
| Caret for an apostrophe | `O^Neill` | Importer |
| Suffix in the family name | `Sauer Jr.` | Formatter inverts as `Sauer, C., Jr.` and cites `Sauer` |
| Section label or session code in a title | FRONTIER, Invited Article, A1 | Decision |
| Typeset footnote mark | `Spin-Offs*`, `Astrometry∗` | Importer |
| SGML entity | `/ques/` for a question mark | Importer |
| Doubly escaped markup | `&amp;lt;BR&amp;gt;` | Importer |
| Concatenated or truncated meeting names | AIAA structures conferences | Decision |
| Container in capitals | JSASS Transactions | Importer proposes a recasing |
| Wrong item type | Mori 2011 typed as a journal article | Decision |
| A conference code used as a volume | `2010.19` | Decision |
| Words run together | `Vicinityof` | Decision |
| Misspelt title with no second source | `Electomagnetic` | Kept and marked `[sic]` |

**Headline casing is a proposal.** The importer keeps registry capitals in later parts of compounds, as in
`Spin-Off`. It leaves symbols such as `α` alone, cases each side of an em dash, and lowercases the prepositions
Chicago lowercases, `aboard` among them.

## Related

- [Citation Style](../writing/CITATION_STYLE.md)
- [Source Database](../../_sources/README.md)
- [Article Tooling Library](../../_lib/README.md)
