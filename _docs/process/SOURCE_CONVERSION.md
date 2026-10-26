# Source Conversion

> **Navigation**: [Process](./README.md) | [Citation Style](../writing/CITATION_STYLE.md) | [Source Database](../../_sources/README.md)

How an article's legacy reference list is converted to Chicago author-date entries generated from the source
database. A200 to A384 have been converted this way, between 2026-10-24 and 2026-10-25. A384 was converted
first by hand, and the procedure below is what A369 to A383 needed. The X-Planes series and A200 to A296 each
needed more, described in their own sections.

## The Procedure

Each step is a command that reads data. Scratch goes under `tmp/<article>/sources/`. Human decisions go in
`_sources/decisions/<article>.toml`, which is tracked.

1. **Cache the registry records** in the shared cache. `python3 _lib/sources_import.py fetch-crossref POST
   tmp/sources/crossref`.
   - Records are requested forty DOIs at a time. A failed batch is halved until the identifier at fault is
     isolated.
   - A DOI Crossref lacks, such as a DataCite one, is fetched from OpenAlex into `tmp/sources/openalex/`.
   - It resumes, so rerun it until nothing is missing.
   - **Run one Crossref fetch at a time.** Crossref's public pool answered about five DOIs a second on 2026-10-24
     and refuses a client that asks concurrently. Its faster pool needs a contact address, which this project
     does not send.
   - `@FILE` in place of the post fetches a list of DOIs in file order, so a list ordered by article completes
     articles in turn. A batch's misses are fetched singly at once, not at the end.
   - **Report servers.** `python3 _lib/sources_import.py fetch-reports ntrs|osti|openlibrary tmp/sources POST...`
     caches each NASA Technical Reports Server, OSTI or Open Library record a post links, one file per
     identifier. `--ids FILE` takes identifiers in file order and `--shard k/n` splits them between processes.
     Only an HTTP 404 is recorded as absent; a refusal or a timeout is retried by the next run.
   - **A harvested survey too large for Crossref's pace.** `python3 _lib/sources_import.py fetch-openalex
     DOIS.txt tmp/sources` fetches OpenAlex records a hundred to a request into `tmp/sources/openalex_bulk/`.
     The import prefers a Crossref record wherever one is cached, and a record drafted from a bulk OpenAlex
     record says that Crossref was not asked. OpenAlex allowed about 140 such requests a day without an API key
     on 2026-10-24, and the fetch stops at the first refusal.
2. **Pin the Wikipedia links.** `python3 _lib/sources_import.py pin-wiki POST tmp/aNNN/sources/wiki_pins.json
   --saved tmp/aNNN/wiki`. A pin is verified in one of three ways.
   - `exact` means saved wikitext is byte-identical to the revision current when the copy was saved.
   - `stripped` means the same, apart from surrounding whitespace.
   - `embedded` means a saved rendered page carries the revision id in its own configuration, which is how A380's
     pages were pinned.

   With no saved copy at all, `--at` pins each page to the revision current when the article was drafted, and the
   decision file must say `dated_pins = true`. `--at-file` gives a timestamp per link instead, the author date of
   the commit that added it, which is what the X-Planes series used since links were added over two months of
   passes. Wikipedia is asked at most once a second, and a dated pin asks for no wikitext. The evidence then states that the text read may differ, as for
   A377. A copy saved under a shorter name, such as `Sphere_of_influence.txt` for *Sphere of influence
   (astrodynamics)*, is accepted only if byte-identical. Pass a sibling article's directory as a second `--saved`
   when a copy was saved there. The first directory given wins, and the evidence names the article whose scratch
   held the copy.
3. **Read the web sources.** A source with no DOI, Wikipedia page or post is read once from its page. The page's
   title, authors, publisher, periodical, date, number and document type are recorded in a metadata file, which
   the decision file names as `web_metadata` along with the reading date as `web_read`.
   - A page that refuses reading falls back to the article's label, and its note says so.
   - Judgements about the publisher, such as whether it has a stake, whether its site is a periodical, or whether
     its pages are first-hand records, are made once per host in `_sources/domains.toml`.
   - Press releases count as Commercial by default, testimony counts as primary, and articles in a periodical
     have the periodical's name in italics.
4. **Dry-run the import** with a decision file that holds only `article`, `crossref_cache` and `wiki_pins`.
   `python3 _lib/sources_import.py import POST _sources/decisions/AXXX.toml --drafts tmp/aNNN/sources/drafts.json`.
   It reports which records are new, which are already stored, which it extends, and every conflict.
5. **Review.** `python3 _lib/sources_import.py review POST tmp/aNNN/sources/drafts.json --flagged
   --second-opinion --saved tmp/aNNN/wiki`. Every drafted title is compared with the article's legacy label,
   which was checked by hand when the article was drafted. A record is flagged for each of the following.
   - Its words differ from the label.
   - Its year or author list disagrees with the label.
   - It has no pages, volume, publisher or authors.
   - Its container looks concatenated.

   For author findings, review also prints OpenAlex's author list. It also prints any fuller author list found in
   the citation templates of the saved wikitext. Each finding is a question for a person, not a verdict.
6. **Record decisions** in the decision file, as `[title]`, `[note]`, `[synthesis]` and `[fix.<anchor>]` tables.
   Every correction carries a note saying what was wrong and where the right value came from. Rerun steps 4 and 5
   until review shows only the findings you mean to keep.
7. **Write.** Add `--write` to the import. Decisions about a record already stored from another article amend
   it. A source stored under another name is mapped, and a name the store uses for a different source is
   renamed in the store and mapped, both in `_sources/articles/`.
8. **Credit the venues.** New venues arrive as not established. `python3 _lib/sources_import.py credit-venues
   --write` credits those a publisher's statement in `_sources/publishers.toml` covers. A venue is credited only with a recorded answer
   to the question of by whom, read from a source the venue speaks through. See [Citation
   Style](../writing/CITATION_STYLE.md) under Default deny.
9. **Generate and relabel.** `python3 _lib/sources.py write POST`, then `python3 _lib/sources.py fix-labels POST`,
   then `python3 _lib/sources.py check POST`.
   - `fix-labels` sets each in-text label to the database's author and year. This covers three-author works
     becoming "et al." and year suffixes such as McInnes 1999a and 1999b. A locator after the year is kept.
   - Check the prose for sentences that describe a label, such as "it is cited as unattributed", and correct them
     with an edit file.
10. **Diff the body against a copy taken before step 9.** `python3 _lib/sources.py diff-labels PRE POST` lists
   each label that changed in substance and every other change, including any link that now leads somewhere
   else. Only in-text labels, and any sentence corrected on purpose, should differ.
11. **Gate.** `python3 _verify.py --strict`, then `./_check.sh`.

**Survey articles.** A369 to A373 list their harvested works in the body as survey entries, one per line, as
`- [Pike and others, 2001, Title][anchor]`. A survey entry is not an in-text citation, so the label check skips
any standalone list item whose text carries a title after its year. Their counts are checked from the cluster
rows by `_lib/survey.py`, which does not read the References section, so conversion leaves those checks intact.

**When the importer changes.** Rerun step 7 with `--refresh` on every converted article, then step 9 and
step 10 against each article's last committed copy. A record with a `note` is never rebuilt. On 2026-10-24 this
pass caught two regressions in already converted articles, a footnote mark left on a title and a German title
given English capitals.

## The X-Planes Series

A297 to A368 were converted on 2026-10-24 and 2026-10-25, 72 articles holding 363,651 link definitions. The
work differs from a single article in three ways.

- **The registry fetch is the long pole.** 164,546 DOIs at Crossref's public pace is the better part of a
  day, so DOIs cited in the prose outside the survey rows were fetched first, and the survey's in article
  order, so that articles completed in turn. OpenAlex's bulk records filled part of the survey until its daily
  allowance ran out.
- **A driver converts each article as its sources complete**, one at a time, since every import writes the
  shared store. Each conversion starts from the copy taken before conversion, so a rerun cannot inherit an
  earlier run's labels.
- **The reference lists' own statistics are recomputed.** `_lib/survey.py years` reads each stated median,
  dated count and period count, recomputes it from the database years and writes an edit for any that
  disagree. A survey count that changes does so because the database dates works the harvest left undated,
  or takes a registry's first-publication year. Statistics stated per cluster other than a median, such as
  `415 were published in 2015 or later`, are not yet checked.

## Links That Are Not DOIs, A200 to A296

A200 to A296 were converted on 2026-10-25. Their links are the pages a reader opens, a publisher's book page,
a JSTOR stable URL, an arXiv abstract, a proceedings site or a search, and only 215 of about 9,500 were DOIs.
Reading every page did not scale, so `_lib/sources_resolve.py` resolves each link to a registry record and the
decision file turns it on with `resolve_links = true`.

- **An identifier in the URL.** A DOI in the path, a JSTOR number as `10.2307/N`, a Nature path, an NBER,
  SSRN or eLife number, an Elsevier PII, an arXiv number or a checked ISBN. An old Elsevier PII spells its DOI,
  `0004370289900774` being `10.1016/0004-3702(89)90077-4`. A newer one is asked of Crossref. arXiv numbers are
  read from DataCite, which registers arXiv's DOIs, since arXiv's own interface refused the first request.
- **A search by the label's title**, Open Library for books and Crossref for the rest. A label with only an
  author and a year, `Boehm 1981`, is searched by the title its anchor spells,
  `book_boehm_software_engineering_economics`, a hint used for searching and never printed.
- **The page itself**, live for proceedings sites whose pages state `citation_*` metadata, otherwise the
  Internet Archive capture nearest the article's date. A page's own DOI, as IEEE states in its document
  metadata, leads to the Crossref record.
- **A proceedings index.** A NeurIPS or PMLR link that serves no paper is matched to the one paper in that
  year's or volume's index by exactly the label's authors.
- **The label.** A label written as a bibliography entry, `Church, Alonzo, The Calculi of Lambda-Conversion,
  Princeton University Press, 1941`, gives a full entry. A label naming only authors and a year gives an entry
  whose title is marked `[Title not identified]`, never a surname printed as a title.

**A record is used only when it agrees with the label.** `agrees` states the test. A search result must agree
on the title, the first author and the year. A record the link itself names must agree on the title, or on the
first author and the year, or, for a label naming an organisation such as `OpenAI 2019`, on the exact year.
A disagreeing record is reported by `python3 _lib/sources_resolve.py explain POST` and not used.

**Five things the old lists did that the generator now honours.**

- **A work the list names and the prose does not cite stays in the list.** A207 closes with a bibliography it
  never cites in the prose, and the generator once kept only cited works. Nine X-Planes articles had lost 156
  works this way and were regenerated. The import records such works in
  `_sources/articles/<post stem>.listed.json`.
- **A Wikipedia article standing in for a work** is replaced by the work its label names. A207 linked Curry
  and Feys's *Combinatory Logic* to the Wikipedia article on combinatory logic.
- **A linked Open Library work that is not the label's book** is sought again by title, as `booklinks.py`
  found nine of ten such links wrong in A345 to A347.
- **A source cited only in the prose** is checked against the prose's own label.
- **A dead report link** is resolved like any other. Twelve NTRS identifiers in A237 to A289 named no record.
  Four were relinked to the records found by their authors and titles, two to the journal publication of the
  same work, and the rest are entries built from their labels.

**Pace.** Crossref's bibliographic search answered about one query in five seconds, Open Library's ISBN
endpoint as slowly because it imports a book it lacks before answering, and archive captures took five to
fifteen seconds each. Open Library's search index is fast but mapped one ISBN to the wrong work, so ISBNs go
through the slow endpoint. dblp and OpenReview answered with browser challenges and are not used.

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
| Spaced footnote marks | `Resolution B3 * †` | Importer |
| Title in capitals with a designation | `RESOLUTION B3` | Importer keeps `B3`, a decision restores `IAU` |
| Title in another language | `nur ein Schlagwort?` | Importer when the language is stated, else a decision |
| Alias DOI | Crossref answers with the primary DOI | Importer keeps the cited DOI, stores `doi_primary` |
| Inline TeX | `$\mathbb{Z}_p$` | Importer writes plain text |
| One chapter under two DOIs | *Death by Perfume*, A377 | Both kept, labels take `a` and `b` |
| Online-first year | Lin-Greenberg et al. | Crossref `issued` year, the house rule |
| Name split in two | DTIC `{Binion, Jr}` then `{T. W.}` | Importer rejoins |
| Initials in the family field | `M. Jaffal`, `W Taylor` | Importer moves them to the given names |
| Lone initial as the family name | `{P, Nishanth}` | Importer swaps |
| Organisation as author | NTRS centres, `AIR FORCE FLIGHT TEST CENTER EDWARDS AFB CA` | Importer: an organisation beside people is dropped, one alone is recased |
| Placeholder author or pages | `&NA;`, `n/a-n/a` | Importer drops |
| Title in capitals | Most older NTRS titles | Recased, `_sources/acronyms.txt` keeps acronyms |
| Slashes for brackets | NTRS `/TO 3700 DEG K/` | Importer writes brackets |
| Cataloguing year | NACA Report 121 of 1921 dated 1979 by NTRS | The year the article cites it by |
| Work without its edition | Open Library work records | The edition of the label's year, else the nearest |
| Incomplete author list | Open Library works list the first author | The label's authors |
| Dead Wikipedia link | `NASA_Helios_Prototype`, `Kratos_BQM-167_Skeeter` | The link corrected to the page's title |
| Given names filed as the family name | Elsevier's `{Peter R., Huttenlocher}` | Importer swaps |
| Some of the authors only | Crossref's Stulz alone for Lang and Stulz 1994 | The label's list, the registry's full names kept |
| DOI registered long after publication | ICWSM's 2013 papers dated 2021 | The year the article cites |
| Edition long after the original | *Phenomenology of Perception* 1945 in its 2002 English edition | `(1945) 2002` |
| Translation or audiobook as the label's edition | A Spanish *Why Nations Fail*, narrators as authors | Passed over for an English print edition |
| Title running into its subtitle, author listed twice | Open Library's Bushman and Genovese | Importer |
| Imprint statement as the publisher | `Published for the Institute of Early American History and Culture by the University of North Carolina Press` | The press |
| Particle omitted by the venue | PMLR's `Herke Hoof` | Kept as the venue prints it |
| Identifier naming another work | arXiv numbers in A250 to A265, `Barreto et al 2019` naming a paper on string theory | Entry from the label, linked to a search, note names the other work |
| Dead link | 29 NeurIPS hashes, 12 NTRS identifiers | Matched in the proceedings index, relinked, or built from the label |

**Headline casing is a proposal.** The importer keeps registry capitals in later parts of compounds, as in
`Spin-Off`. It leaves symbols such as `α` alone, cases each side of an em dash, and lowercases the prepositions
Chicago lowercases, `aboard` among them.

## Related

- [Citation Style](../writing/CITATION_STYLE.md)
- [Source Database](../../_sources/README.md)
- [Article Tooling Library](../../_lib/README.md)
