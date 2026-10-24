# Citation Style

> **Navigation**: [Writing](./README.md) | [Documentation Root](../README.md)

This document defines how the blog cites its sources. Reference list entries follow the author-date system of
*The Chicago Manual of Style*, 18th edition. The reference list is divided into seven sections ranked by
reliability. Entries are generated from a single database of sources rather than written by hand.

**Status.** Adopted 2026-10-24 as the target format. A prototype of the database and generator exists, and one
article, A384, is converted. Unconverted articles use the legacy format described in the
[Style Guide](./STYLE_GUIDE.md#reference-style), and that section remains authoritative for them.
`_verify.py` checks only converted articles, which it recognises by the marker comment the generator writes.
[Tooling Requirements](#tooling-requirements) records what exists and what does not.

## Sources of Truth

**The canonical source** is *The Chicago Manual of Style*, 18th edition, University of Chicago Press, 2024, at
<https://www.chicagomanualofstyle.org/>. The full manual requires a subscription. Section numbers below refer to
that edition and are given so that anyone with access can check a rule against the manual.

**The rules below are distilled from free sources** written for students. Where they disagree, the publisher's
own guide wins.

1. The Chicago Manual of Style Citation Quick Guide, author-date tab, published by the University of Chicago
   Press. <https://www.chicagomanualofstyle.org/tools_citationguide/citation-guide-2.html>
2. The University of Queensland Library, Chicago 18th author-date guide.
   <https://guides.library.uq.edu.au/referencing/chicago-18th-author-date>
3. Curtin University UniSkills, Chicago 18th author-date guide.
   <https://uniskills.library.curtin.edu.au/referencing/chicago18/reports/>
4. University of Portland Library, the changes made in the 18th edition.
   <https://libguides.up.edu/chicago/whats_new>
5. California State University Channel Islands Writing and Multiliteracy Center, Chicago author-date handout,
   revised February 2026. <https://www.csuci.edu/wmc/pdf/citations/wmc-chicago-authdate-18threv2026.pdf>

**Secondary guides contain errors.** Two of the guides above print examples with typographical errors in their
punctuation. Copy patterns from this document, which was checked against the publisher's guide, rather than from
an arbitrary library page.

**The rules are paraphrased, not copied.** The manual is copyrighted. This document states the rules in its own
words and quotes only short examples.

**Confidence markers.** A rule marked **Verified** was confirmed in at least one source above. A rule marked
**House** is a decision of this blog, made by analogy where the free sources are silent. A rule marked
**Unverified** must be checked against the manual before the generator relies on it.

## Reference List Sections

Every article's `## References` section is divided into the following subsections, in this order. Each
subsection is an `###` heading. A subsection with no entries is omitted.

| Order | Heading | Contents |
|---|---|---|
| 1 | Primary Sources, Peer-Reviewed | Original work that passed full peer review before publication |
| 2 | Primary Sources, Non-Peer-Reviewed | Original work and first-hand records that were not peer-reviewed |
| 3 | Secondary Sources | Scholarly works that synthesise primary work |
| 4 | Commercial Sources | Material from organisations with a stake in the subject |
| 5 | General Sources | Material from publishers without a stake in the subject |
| 6 | Tertiary Sources | Encyclopaedias, Wikipedia included |
| 7 | Related Posts | This blog's own articles |

**Why the order is a ranking.** Sections 1 to 6 run from most to least reliable, so a reader who wants the
strongest evidence reads from the top. Wikipedia sits in the lowest tier because any revision can be vandalised
or degraded, and because it summarises other sources rather than reporting evidence.

**Why Related Posts come last.** A reader looking for external evidence does not want the blog's own articles.
Placing them last is also a matter of humility, since the blog does not rank its own work as evidence. The fixed
final position also makes them easy to find.

**The headings appear in the automatic table of contents.** The table of contents builds from every `h2` and
`h3` heading with an id, so the subsections are listed under References. This is accepted as a navigation aid.

## Classification Rules

Classify a source by taking the **first rule that applies**. The evaluation order below differs from the display
order above, because encyclopaedias and the blog's own posts must be caught before the broader rules match them.

1. **The blog's own posts** go to **Related Posts**.
2. **Encyclopaedia and dictionary entries** of any kind go to **Tertiary Sources**. This includes Wikipedia,
   edited encyclopaedias and peer-reviewed encyclopaedias such as the Stanford Encyclopedia of Philosophy.
3. **Work in a peer-reviewed venue** goes to **Primary Sources, Peer-Reviewed**. A peer-reviewed venue is a
   journal or a conference proceedings whose full papers are refereed before publication, **as verified by
   a recorded answer to the question of by whom**. A review article goes to **Secondary Sources** instead, because it synthesises
   rather than reports, and it stays there under rule 5 when its venue is not verified.
4. **Original work and records without peer review** go to **Primary Sources, Non-Peer-Reviewed**. This
   includes government and agency technical reports, statistical releases and data, standards, patents,
   archival documents, datasets, theses, preprints, conference abstracts, meeting papers whose venue reviews
   only the abstract, and the documentation of open-source projects.
5. **Scholarly books** go to **Secondary Sources**. This includes monographs, edited scholarly collections,
   handbooks and textbooks.
6. **Material from an organisation with a stake in the subject** goes to **Commercial Sources**. A stake means a
   financial or institutional interest in how the subject is perceived. This includes company product pages,
   datasheets, vendor documentation, company press releases and company blogs. **It also includes non-profit
   organisations.** Foundations, advocacy groups, trade associations and think tanks earn money, pay staff and
   promote causes, and their tax status does not remove that interest. Government and university press
   releases and outreach pages also fall here, because they promote the institution's own work. Their technical
   reports and data fall under rule 4.
7. **Everything else** goes to **General Sources**. This covers news reports, magazines, personal blogs,
   forums, social media and popular books, where the publisher reports on a subject in which it has no stake.

**Worked cases.**

- A company paper in a refereed journal is **Primary Sources, Peer-Reviewed** under rule 3, because the venue
  vetted it.
- The same company's datasheet is **Commercial Sources** under rule 6.
- A NASA technical report on the NASA Technical Reports Server is **Primary Sources, Non-Peer-Reviewed** under
  rule 4. A NASA mission news page is **Commercial Sources** under rule 6.
- A news organisation's report on a third party is **General Sources** under rule 7. The same organisation's page
  about its own subscription offer is **Commercial Sources** under rule 6.
- An EGU General Assembly abstract is **Primary Sources, Non-Peer-Reviewed** under rule 4.

**Peer review is credited only when the database can say by whom.** This is the pilot's ruling of
2026-10-24. The label tells a reader that people independent of the authors assessed the work before
publication, so the question that decides it is the reader's: reviewed by whom? If a source the venue speaks
through gives a good answer, the venue is credited and the answer is recorded as `reviewers`, for example "usually
two or more independent reviewers selected by the editors". If not, the basis for the label is lacking, even if
the work was in fact reviewed by an acceptable group, and the source drops to rule 4.

**The policy statement is a means, not the end.** Any source the venue speaks through may answer the
question: its own pages, its publisher's, its editors' published editorials, or its society's magazine. AGU's
policy pages refused automated reading, but AGU's magazine *Eos* reports more than 30,000 reviews across its
journals in 2016 and names the reviewers each journal's editors selected that year, which answers by whom.
Three things still leave a venue uncredited.

- **No answer read.** A search-engine summary may paraphrase, so it is recorded with method `snippet` as a
  lead and cannot credit the venue. Elsevier's guides for *Acta Astronautica*, *Icarus* and *Planetary and
  Space Science*, every *Astronomy & Astrophysics* page and *Science*'s peer-review page refused automated
  reading.
- **A statement that does not say by whom.** Springer says research content in *Space Science Reviews* is
  peer reviewed, single-anonymous, without saying who reviews or whether the invited reviews and mission
  descriptions that fill that journal count. The AAAS editorial policy for *Science* says only that the editor
  weighs "recommendations of reviewers and referees". The IEEE Aerospace Conference's 2021 pages say full
  drafts are reviewed and approved, and that reviews rely on "expert guidance from senior engineers and
  scientists", without saying who writes them.
- **An answer that does not reach back to the work.** Nature's editorial dates mandatory review to 1973,
  so `since` is 1973 and an earlier Nature paper is not credited. An answer that gives no date is applied to
  every year. That is a known weakness, recorded here rather than hidden.

On 2026-10-24 twelve of the eighteen journals A384 cites were credited: *American Journal of Physics*,
*Applied Optics*, the three AAS journals, *Geology*, the two AIAA journals, *Nature* and the three AGU journals.
The *American Journal of Physics* answer is the weakest, "referees, with the editors", from an editorial policy
that names referees without saying how many or how they are chosen. No proceedings is credited.

**Peer review is a property of the venue, recorded once.** Whether a journal or conference referees full papers
is recorded in a venue table in the database, so the decision is made once per venue rather than once per
paper. **The venue is the unit of judgement, and it is not always obvious.** For example, many engineering
society meeting papers are selected by abstract and published without full review. Each venue's status must
be established from a source the venue speaks through that says by whom its papers are reviewed.

**Telling a review article from a research article** cannot be done from Crossref metadata, which types both as
`journal-article`. A title heuristic may flag candidates. The decision is recorded per source in the database.

## Reference Entry Format

**Reference entries follow Chicago exactly, and the prose rules do not apply to them.** An entry is a citation,
not prose. It therefore uses the colons, parentheses, serial commas and quotation marks that Chicago requires,
and titles keep the spelling of the source. A title published in American spelling is never anglicised.

### Elements and Order

**Verified.** An author-date entry gives the author, then the year, then the title, then the source details,
then the persistent identifier or URL. The year follows the author directly, which distinguishes author-date
entries from bibliography entries.

### Authors

- **Verified.** The first author is inverted as `Family, Given`. Later authors are not inverted.
- **Verified.** Up to six authors are all listed. With more than six, list the first three followed by
  `et al.` (13.23, 13.78).
- **Verified.** Two authors are joined as `Family, Given, and Given Family`. Three to six use the serial comma,
  as in `Family, Given, Given Family, and Given Family`.
- **Verified.** Editors of a whole book take `ed.` or `eds.` after the names.
- **Verified.** A repeated author name is written out in full in each entry. The old three-em dash is not used
  (13.72).
- **Verified.** An organisation can be the author.
- **House.** An organisation known by an acronym is given as the acronym followed by the full name in
  parentheses, as in `NASA (National Aeronautics and Space Administration)`. The free sources disagree here. One
  guide prints this form, and another lists a widely known acronym alone. The expanded form is chosen because it
  matches the blog's rule of spelling out acronyms.
- **Verified.** With no author, editor or translator, the entry begins with the title (13.81).
- **House.** Given names appear as the source prints them. Initials are not expanded unless the source itself
  gives the full name.

### Dates

- **Verified.** The year follows the author. A source with no date takes `n.d.` and an access date.
- **Verified.** Continually updated web content takes a publication or revision date, introduced by
  `Last modified`. An access date, introduced by `Accessed`, is used only when no such date exists. The year
  is written in the `Last modified` date only when it differs from the entry's year.
- **Verified.** Two or more works by the same author in the same year take `a`, `b`, `c` after the year, as in
  `2026a` (13.114). Because the suffix depends on which works an article cites, it is assigned per article at
  generation time, not stored in the database.
- **Verified.** A journal article's month or season is usually omitted (13.26).
- **House.** Dates inside entries use Chicago's month, day, year order, as in `December 19, 2023`.

### Titles

- **Verified.** Titles of articles, chapters, web pages and other parts of a larger work go in quotation marks.
  Titles of books, journals, reports and other whole works go in italics.
- **Verified.** English titles use headline-style capitalisation. A subtitle follows a colon.
- **House.** Acronyms and proper nouns keep the capitalisation the source uses.
- **House.** A registry title's separator of a typed spaced hyphen becomes a colon, and a trailing period is
  dropped. Other punctuation is kept as published, including a published em dash.
- **House.** Headline case is proposed by `_lib/sources_import.py` and reviewed by a person for every title.
  The proposal never removes an existing capital, so it cannot damage an acronym, but it cannot know that a
  planet designation such as `51 Pegasi b` keeps its lower-case letter. Such titles are corrected on the
  record.

### Identifiers and URLs

- **Verified.** A DOI is given as a URL of the form `https://doi.org/10.1086/725865`. The `doi:` prefix is
  deprecated (13.7).
- **House.** When a DOI exists, the DOI URL is used instead of any publisher URL.
- **House.** The entry ends with the DOI or URL, linked through the source's anchor.

### Ordering Within a Section

- **Verified.** Entries are alphabetised by the first element, normally the first author's family name (13.112).
- **Verified.** Works by the same author are ordered by year, oldest first (13.112).
- **Verified.** When sorting by title, an initial `A`, `An` or `The` is ignored (13.100).

## Templates by Source Kind

Italics are written in Markdown with asterisks. The generator emits these patterns. Square-bracketed words are
placeholders.

**Journal article. Verified.**

```
[Family], [Given], and [Given] [Family]. [Year]. "[Article Title]." *[Journal]* [Volume] ([Issue]): [First]–[Last]. https://doi.org/[DOI].
```

Example from the publisher's guide: `Dittmar, Emily L., and Douglas W. Schemske. 2023. "Temporal Variation in
Selection Influences Microgeographic Local Adaptation." *American Naturalist* 202 (4): 471–85.
https://doi.org/10.1086/725865.`

- **Verified.** With an issue but no volume, write `no. [Issue]`. Page ranges are abbreviated as in `471–85`.
- **Verified.** An article published online ahead of print adds `ahead of print` and the posting date (14.75).

**Book. Verified.** Place of publication is no longer required (14.30).

```
[Family], [Given]. [Year]. *[Book Title: Subtitle]*. [Publisher]. [URL or DOI].
```

**Chapter in an edited book, or paper in published proceedings. Verified.** The chapter's page range is no
longer required (14.9).

```
[Family], [Given]. [Year]. "[Chapter Title]." In *[Book or Proceedings Title]*, edited by [Given] [Family]. [Publisher]. [URL or DOI].
```

**Preprint. Verified in outline, Unverified in detail.** A preprint is cited like a journal article, with the
word `Preprint` and the server name in place of the journal details (14.76). The exact element order must be
checked against the manual.

```
[Family], [Given]. [Year]. "[Title]." Preprint, [Server], [Month Day]. https://doi.org/[DOI].
```

**Paper presented at a meeting, and conference abstracts. Verified in outline for papers, House for
abstracts.** The free sources confirm that a presented paper gives the meeting's details after the title. The
exact wording and order of those details are Unverified.

```
[Family], [Given]. [Year]. "[Title]." Paper presented at [Meeting Name], [Place], [Month Day–Day]. [URL or DOI].
[Family], [Given]. [Year]. "[Title]." Abstract [Number], *[Meeting Name]*. [Publisher]. https://doi.org/[DOI].
```

**Report, including government and agency reports. Verified.**

```
[Author or Organisation]. [Year]. *[Report Title]*. [Report Number]. [Publisher]. [URL].
```

- **Verified.** Elements that cannot be found are omitted. When the author and publisher are the same
  organisation, the publisher may be abbreviated.

**Thesis. Unverified.** The free sources disagree on the label. The generator must not emit theses until the
manual's wording is confirmed.

```
[Family], [Given]. [Year]. "[Title]." [Degree Label], [Institution]. [URL].
```

**Newspaper or magazine article. Verified.** Page numbers are omitted from the entry.

```
[Family], [Given]. [Year]. "[Article Title]." *[Publication]*, [Month Day]. [URL].
```

**Web page. Verified.**

```
[Owner or Sponsor]. [Year or n.d.]. "[Page Title]." [Site Title, if different from the owner]. Last modified [Month Day, Year]. [URL].
```

Example from a guide: `NASA (National Aeronautics and Space Administration). n.d. "Juno." Last modified
September 3, 2025. http://www.nasa.gov/mission_pages/juno/main/index.html.`

**Wikipedia article. House, built on the verified web page and no-author rules.**

```
"[Article Title]." [Revision Year]. Wikipedia. Last modified [Month Day], at [HH:MM] (UTC). https://en.wikipedia.org/w/index.php?title=[Title]&oldid=[Revision].
```

- **Verified.** The year is omitted from the `Last modified` date when it equals the entry's year. The
  publisher's guide prints `Last modified December 19, at 21:54 (UTC)` after an entry year of 2023. Because the
  entry year here is the revision year, the two always match.

- **Every Wikipedia citation pins a revision.** The URL is a permanent link carrying the `oldid` of the revision
  that was checked, not the live page. The date is that revision's timestamp. Later vandalism or editing cannot
  change what the citation points to, and a reader sees exactly the text that was verified. This fits Chicago's
  rule that continually updated content carries its revision date.
- **The entry begins with the article title.** Chicago begins an entry with the title when there is no author
  (13.81). Wikipedia articles have no single author. Putting the owner first would give every entry the same
  author and force year suffixes such as `2026a` to `2026z` across a long list.
- **Verified context.** The publisher's guide cites a Wikipedia policy page as web content with a `Last modified`
  date and time. Some library guides say well-known encyclopaedias are cited in the text rather than in the
  list. This blog lists them, ranked last, because readers must be able to audit them.

**Patent, standard, dataset and software. House, Unverified.** The free sources give no examples. Until the
manual is checked, these follow the report template, with the patent, standard or dataset number in the
report-number position and the software version after the title.

**This blog's own posts. House.** The title, date and address come from the cited post's front matter and the
site configuration at generation time, so a renamed post updates every citation of it.

```
Sechter, Brendan. [Year]. "[Post Title]." *[Blog Title]*, [Month Day]. [Absolute URL].
```

- Related posts take no year suffix, although they share an author and often a year. They are cited in the
  text by title, never by author and year, and the month and day already distinguish them.
- They are ordered by date, oldest first.
- A link to a section of a related post is a **locator**, an extra anchor on the post's record that adds a
  fragment. The section is listed once however many of its sections the article links to.

**Social media and blog posts. House.** Chicago usually cites these in the text only. This blog lists every
cited source, so they take the web page template, with the post's author as the author.

## In-Text Citations

- **House.** In-text citations remain Markdown reference links without parentheses, as in
  `[Lammer et al. 2026][research_lammer_et_al_2026]`. Chicago's parenthetical form would break the prose rule
  against parentheticals. The link text carries the same author and year Chicago puts in parentheses.
- **Verified.** In the text, one or two authors are named, as in `Kopp and Lean 2011`. Three or more are given
  as the first author followed by `et al.`, as in `Kulkarni et al. 2018`. Some existing articles name three
  authors in the text and will change on conversion.
- **Verified.** The year carries the same `a`, `b` suffix as the entry when one is assigned.
- **House.** A Wikipedia article is cited in the text by its title, as in `[Mercury][ref_mercury]`.
- **House.** The link target is the source's DOI or URL, as it is today.

## Source Database

**Reference entries are generated from one database of sources**, never typed by hand. Correcting a source once
corrects every article that cites it, and two articles can never describe the same source differently.

**Scale, measured 2026-10-24 across the 333 posts that carry link definitions.** The corpus holds 415,869
reference definitions, 233,350 distinct anchors and 238,013 distinct URLs. Of the URLs, 198,288 are DOI links
and 27,047 point at the NASA Technical Reports Server. The remainder spans 1,764 domains. **Most
classification is therefore mechanical.** DOIs take their kind from Crossref, and report servers map to rule 4.
The long tail of domains is classified once per domain.

**Anchors are corpus-wide identifiers.** Each source has exactly one canonical anchor, carried in its database
record and used by every article. An anchor is an opaque identifier. Its prefix, such as `research_` or `ref_`,
says nothing about the source's section, because a source can be reclassified without being renamed. **Existing
anchors are kept as canonical anchors wherever they are unambiguous.** The measurement above found 14,194
anchors that point at more than one URL across articles, and 14,634 URLs cited under more than one anchor.
Some of these are the same source under different URL spellings. The rest are true collisions. Consolidation
must keep one anchor per source, record the others as aliases, and rename the articles that used an alias.

**Record fields.** The database stores data, not formatted strings. `_lib/sources.py` rejects any other
field.

| Field | Meaning |
|---|---|
| `anchor` | Canonical anchor, unique, lower case, immutable |
| `aliases` | Former anchors that resolve to this source |
| `locators` | Extra anchors mapped to a fragment id, for links to a section of the source |
| `kind` | `journal-article`, `proceedings-paper`, `abstract`, `book`, `chapter`, `report`, `preprint`, `web-page`, `wikipedia` or `related-post` |
| `rule`, `section` | The classification, which must equal what the rules give |
| `synthesis` | True for a review or other synthesis, a human decision |
| `stake` | True for a publisher with an interest in the subject, a human decision |
| `encyclopaedia` | True for an encyclopaedia entry that is not Wikipedia |
| `authors`, `editors` | Ordered lists of people, each with `family` and `given`, or organisations, each with `name` and `short` |
| `year` | Publication year, or `null` for no date |
| `title` | Title as displayed, in reviewed headline case |
| `title_published` | Title exactly as the registry gave it, kept for audit |
| `container` | Journal, book, proceedings, site or meeting |
| `venue` | Key into the venue table, for journals and proceedings |
| `volume`, `issue`, `pages` | Journal details. `pages` may hold an electronic article number |
| `publisher` | Publisher |
| `number` | Report, abstract, meeting-paper or series number |
| `doi` | DOI without the resolver prefix, lower case |
| `url` | URL when there is no DOI |
| `revision` | For Wikipedia, `oldid` and `timestamp`. For a web page, `modified` |
| `accessed` | Access date, used only with no revision date |
| `post` | For a related post, its filename stem |
| `evidence` | How the cited version was verified |
| `note` | What was corrected from registry data and where the correct value came from |

**Venue fields.** Each venue records `peer_reviewed`, the `basis` for that judgement, and `checked`, which is true
only once a source the venue speaks through has been read. `reviewers` is the answer to by whom. `evidence`
is a list of sources, each with the page's `url`, a verbatim `quote`, the date it was `read`, and the
`method`, either `fetched` for a page read directly or `snippet` for a search-engine summary kept as a lead.
`since` is the first year the evidence covers, when it gives one. Validation refuses `peer_reviewed` true
without `checked`, `reviewers` and at least one `fetched` source, so an unverified venue cannot be credited
by a hand edit.

**Storage.** The database lives in `_sources/`, which Jekyll does not copy. Its eventual size, roughly a quarter
of a million records, rules out one file per source and a single file. Records are JSON Lines in
`_sources/records/`, one record per line sorted by anchor, sharded by the first character of the anchor after any
legacy prefix. The Python standard library reads and writes it, and a corrected record changes one line in a
diff. No third-party parser is required. Whether thirty-six shards stay a manageable size at full scale has not
been measured.

**The database is in a public repository.** The repository behind the site is public, so the database is
visible to anyone. It is the blog's own database, not a confidential one. A private store would need a separate
repository.

**Generation, not runtime rendering.** A generator writes each article's References section into the article's
Markdown, as the per-article scratch generators do today. The site build stays unchanged and needs no plugin,
which matches the decision recorded for redirects. A check confirms that every article's References section is
exactly what the generator would write, so a hand edit cannot drift from the database.

## Tooling Requirements

**Built in the prototype, 2026-10-24.**

1. `_sources/` with the record shards and the venue table. See its README.
2. `_lib/sources.py`, which validates records and venues, classifies by the rules, formats entries, generates a
   References section, and checks a converted article for drift and for in-text labels that disagree.
3. `_lib/sources_import.py`, which drafts records from Crossref, from a pinned Wikipedia revision, and from a
   related post, and proposes headline-case titles.
4. `_lib/test_sources.py`, regression and negative tests.
5. `_verify.py` runs the drift check on every converted article, exempts generated sections from the prose
   rules, and counts any list item as a visible reference.

**Not yet built.**

1. A corpus importer that seeds records from every article's link definitions and reports every anchor
   collision for decision. `sources_import.py import` now imports one post from a decision file in
   `_sources/decisions/` and reports conflicts with the store, which is the per-post half.
2. An answer to by whom for the six journals still uncredited, *Acta Astronautica*, *Icarus*, *Planetary
   and Space Science*, *Astronomy & Astrophysics*, *Science* and *Space Science Reviews*. A person reading
   the pages that refused automated reading would settle most of them.
3. Templates for theses, patents, standards, datasets and software, and a check of the unverified rules.
4. Updates to `_lib/survey.py`, which reads the legacy label format, before any article with a reference survey
   is converted.

## Open Decisions

1. **Agency and university outreach.** This document places government and university press releases and
   outreach pages under Commercial Sources. The alternative is Primary Sources, Non-Peer-Reviewed.
2. **Future Reading.** Whether the `## Future Reading` section uses the same entry format and database.
3. **Legacy posts.** Whether A1 to A74 are converted or keep their original format.
4. **Unverified rules.** The thesis label, the preprint element order, and the patent, standard, dataset and
   software templates need a check against the manual.

## Related Sections

- [Style Guide](./STYLE_GUIDE.md) for prose rules and the legacy reference format
- [Post Structure](./POST_STRUCTURE.md) for where the References section sits in a post
- [Analytical Essay Structure](./ANALYTICAL_ESSAY_STRUCTURE.md) for the Epistemic State section, which names
  sources that were not peer-reviewed
