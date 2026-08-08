# Handoff Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

The self-contained, imperative resume prompt, written **before a planned compaction** and validated
on resume. Unlike the two resume channels it is **not** kept always-current. It is a snapshot stamped
with the commit it describes, so a stale handoff self-reports as stale rather than misleading a
resuming agent.

Adapted from the protocol in the `keleusma` repository at `docs/process/HANDOFF.md`.

## Validity

- **Branch**: `master`
- **Parent commit** (the repository state this handoff describes): `4e41216`
- **Written**: 2026-08-07
- **Tree at write**: clean; everything through `4e41216` is PUSHED and its CI run completed with
  `success`. This handoff commit will be the only unpushed commit.
- **Context**: the X-Planes series is IN PROGRESS. **Fourteen of seventy-two articles drafted, all
  four passes complete on each. None published.**

**Validity check — run on resume, before trusting this handoff.** On the branch above, compare the
**Parent commit** to `git rev-parse HEAD~1`. Because this handoff file is itself committed, its commit
advances the tip by one, so the state it describes is the parent of the handoff commit. The two match
**only** when this handoff commit is still the branch tip and nothing has landed after it.

- **Match → VALID.** Proceed per the resume prompt below.
- **Mismatch → INVALID and STALE.** A later commit moved the tip. Do **not** proceed and do **not**
  trust this handoff. Report the mismatch to the human pilot (recorded parent versus actual `HEAD~1`),
  familiarize from the live channels — `REVERSE_PROMPT.md`, `TASKLOG.md`, `_drafts/draft_summary.md`,
  and the git log, always authoritative — and wait for instruction.

## Resume prompt — the next prompt will be "Please draft A311, 'X-Planes: Bell X-14.'"

**Nothing is outstanding.** A310 finished all four passes, is committed and pushed, its CI run
succeeded, and the article returns 404 while the site root returns 200, which is correct because
nothing in the series is published. There is no half-finished pass to pick up.

**Wait for the pilot's prompt.** Do not begin A311 unprompted.

**A311 is set up better by its predecessor than any article in this series so far.** The X-14 is the
variable-stability aircraft that **established the control-power criteria A310 borrowed
anachronistically and said so**. A310 uses half a radian per second squared in pitch and one in roll
throughout, flags them in its own Epistemic State as figures the field settled on after the X-13
flew, and cites the X-14 experiments as their source. **The obvious opening for A311 is that the
previous article had to use numbers this one produced**, and the obvious keystone is the criteria
themselves rather than any property of the airframe.

**Reuse the A310 harvest.** It is at `tmp/a310/` with 1,899 entries and already holds the Drinkwater
and Rolls variable-stability work, the Garren visual-flight investigation, the jet-lift powerplant
experience report written specifically about the X-14A, and the whole handling-qualities criteria
series. Copy the toolchain, repoint the paths, add only what A311 needs.

**The trap is a different one this time.** A310 is about a vehicle that could not do its job and
A311 is about a vehicle whose job was to measure. **A research aircraft built as an instrument has no
mission to fail at**, so the What the Data Changed section carries more weight than usual and the
flight-record section carries less. Do not write it as a performance story.

## Where the Series Stands

| Article | Date | Vehicle | Lines | Eq | Refs | Words | Passes | Pushed |
|---------|------|---------|-------|----|----- |-------|--------|--------|
| A297 | 2025-10-06 | Series framing | 1765 | 147 | 421 | 21,933 | all four | yes |
| A298 | 2025-10-07 | Bell X-1 | 1387 | 108 | 337 | 17,565 | all four | yes |
| A299 | 2025-10-08 | Bell X-2 | 1497 | 126 | 370 | 17,743 | all four | yes |
| A300 | 2025-10-09 | Douglas X-3 | 1415 | 114 | 365 | 15,583 | all four | yes |
| A301 | 2025-10-10 | Northrop X-4 | 1391 | 98 | 372 | 18,358 | all four | yes |
| A302 | 2025-10-11 | Bell X-5 | 1657 | 112 | 466 | 22,299 | all four | yes |
| A303 | 2025-10-12 | Convair X-6 | 1487 | 92 | 404 | 18,375 | all four | yes |
| A304 | 2025-10-13 | Lockheed X-7 | 1395 | 94 | 358 | 17,330 | all four | yes |
| A305 | 2025-10-14 | Aerojet X-8 | 2226 | 200 | 474 | 20,352 | all four | yes |
| A306 | 2025-10-15 | Bell X-9 | 1556 | 115 | 342 | 13,654 | all four | yes |
| A307 | 2025-10-16 | North American X-10 | 1329 | 122 | 367 | 18,323 | all four | yes |
| A308 | 2025-10-17 | Convair X-11 | 1302 | 97 | 364 | 18,837 | all four | yes |
| A309 | 2025-10-18 | Convair X-12 | 1505 | 137 | 399 | 18,179 | all four | yes |
| A310 | 2025-10-19 | Ryan X-13 Vertijet | 1346 | 91 | 336 | 17,380 | all four | yes |

The `Eq` column is display blocks as counted and reported at the time of each publication review. A
naive `grep -c '^\$\$'` halved does not reproduce it, so do not "correct" the table from that. For
articles whose equations are written as single-line `$$...$$` blocks, which is the style from A305
onward, the count is one per line rather than one per two.

**A306 through A310 all finished with nothing trimmed**, and **A310 is the only article so far to
finish with every band satisfied in both directions**, at 1346 lines, 91 equations, and 336
references. A309 finished seven equations and nineteen references above their ceilings, reported
rather than trimmed under the standing directive. **A305 remains the only article that wrote long and
finished over**, at 2226 lines against a 1600 ceiling, which is 39 percent over on lines and 200
percent over on the original equation band, and it is the reason the approach direction became a rule.

**The gap a draft leaves is the gap the passes must close, and it is not free.** A306 drafted at 1228
lines and needed 328 more. A307 at 943 needed 386. A308 at 678 needed 624, which took the largest
publication-review expansion the series has performed and required writing four additional analytical
sections rather than only surveying literature. A309 at 1066 needed 439. A310 at 810 needed 536.
**Draft nearer 1100 lines than 700.** The rule to approach from below is correct and was overapplied
in A308. The two drafts that came closest to the
floor, A309 at 1066 and A306 at 1228, are also the two that needed the least rework, and the pattern
across five articles is consistent enough to act on.

## The Established Rhythm, Which Is the Most Important Thing Here

The pilot drives each article through **four passes**, each a separate prompt. Do not try to do them
all at once, and do not skip ahead.

1. **"Please draft Axxx"** — research, write, verify, commit. Do not push.
2. **"Please review for equation density, and add all candidate equations."**
3. **"Please review for reference density, specifically primary references, and add all identified references."**
4. **"Please review for publication, and make suitable changes..."** — this prompt also asks for a push.

Push only when the prompt says to. Publishing is never implied by any of them.

Each review pass follows the same discipline. **Measure first, report the baseline, then act.** The
pilot has responded well to being told what the number was before it changed, and several of the
better findings came from measuring rather than from writing.

## Standing Directive, Quoted Because It Governs Every Pass

> "all articles in this series have no length limit, no reference limit, and that they should serve
> as a comprehensive survey and review of the contemporary literature in addition to any other stated
> goals"

Contemporary means recent scholarship, not recent history. Every article carries a
`## The Contemporary Literature` section. A297 through A300 landed at 28 to 33 percent of dated
references at 2010 or later, and that was the stated target. **From A301 onward the absolute count
settled at 101 to 189 while the percentage swung on the denominator**, giving A301 101 at 35.8
percent, A302 109 at 30.6, A303 105 at 35.4, A304 107 at 40.2, A305 155 at 37.8, A306 110 at 36.2,
A307 151 at 45.1, A308 189 at 55.3, A309 158 at 41.4, and A310 133 at 41.7. The count is the stable
measure and the percentage is not, because an article carrying fewer dated references overall reports
a higher share for the same work. **Treat 28 to 33 percent as a floor rather than a ceiling**, and say
explicitly in the report when a figure exceeds it deliberately.

**Assemble the contemporary set by DOI taken from the harvest records.** See the first method rule
below for why this is stated as a rule rather than as a preference.

**Aim the contemporary sweep at the threads the equation and primary passes opened, not at the
article's original topics.** Every article from A305 onward has done this and it is what makes the
additions attach to the article's own derivations rather than sitting beside them.

**The strongest contemporary sections open with analysis rather than survey.** A309 and A310 both
begin theirs by running the article's own relations forward on a modern case, and in both the
computation changed what the survey then said. A310's caught an overstatement the obvious comparison
would have produced. **Do the arithmetic before writing the literature review, not after.**

## Method Rules Earned the Hard Way

These are the reason this handoff is worth writing. Each cost a real defect.

- **An identifier that can be looked up must never be constructed.** While assembling the
  contemporary set during the A304 draft pass I hand-built nineteen plausible-looking DOIs rather
  than reading them out of the harvest records. Crossref showed most resolving to entirely unrelated
  papers, including one on dendrite deformation and one on alcohol licensing policy. All were
  discarded and the set was rebuilt from actual records. **Take every DOI, NTRS id, OSTI id, and DTIC
  id verbatim from the record that returned it.** A306 through A310 each contain no hand-entered
  identifier at all, which is the standard to hold.
- **Resolve the anchor index from harvest metadata BEFORE drafting, not after.** This supersedes the
  weaker rule that author names cannot be inferred from titles, which was known and still violated.
  A304 guessed 31 keys and had to remap 42 citations. A305 guessed twenty and **every one was wrong**.
  A306 built a greppable anchor index from metadata first and all 239 anchors landed correctly on the
  first attempt. **The remedy is ordering, not care.** A307 still invented three anchors during
  composition and A308 invented three more, all caught by the reference generator before any pass ran,
  so **the ordering rule prevents systematic error and does not prevent invention at the keyboard**.
  Verify a new anchor exists before writing the sentence that uses it.
- **Compute the worked numerics before writing, not while writing.** This is the rule with the
  clearest evidence for and against. A306, A307, A309, and the A308 draft's early sections all passed
  first numeric verification with zero corrections while it was followed. A308's third draft expansion
  was written without computing first and immediately produced a wrong range-to-velocity sensitivity,
  at 2.4 against a true 4.34, with a displayed derivation that was malformed. **The rule holds while followed and fails the moment it is skipped, with
  no grace period.**
- **Writing a relation down catches arithmetic the draft carried as an assertion. Six articles
  running.** A305's thrust coefficients were all wrong. A306 asserted an error decay that ignored a
  polynomial factor of 85. A307 stated a heating margin with the wrong sign. A308's equation pass
  overturned the draft's claim that the staging gain was modest, which is 1044 metres per second.
  **A309's found that "roughly two orders of magnitude" of gyroscope improvement was a factor of about
  three**, which weakened the article's own architectural inference rather than strengthening it.
  **A310's found that a one-fifth-scale model imposes one fifth of the ground pressure and not one
  twenty-fifth**, because disc loading goes as the first power of length. Two of the six changed the
  article's argument rather than a number in it.
- **Anchor suffixes are not stable, and TWO guards are needed because each covers a case the other
  does not.** Disambiguation suffixes such as `_2` and `_3` are assigned in generator iteration order
  and shift whenever the master table is rebuilt on a larger harvest. **The URL-stability guard**
  compares every cited anchor's new URL against the URL recorded in the reference section already in
  the file, which is ground truth for what the prose meant, and refuses to regenerate on any change.
  It exists because A309 found two already-cited anchors silently pointing at unrelated papers, and it
  fired again on the very next regeneration and once more in A310. A307's earlier version of the same
  defect was caught only because titles were dumped before writing, which remains the habit to keep
  even with the guards in place. **The link-text invariant**
  compares display strings and catches anchors being *added*, which the URL guard cannot see because
  they are not yet in the file. A310's contemporary pass needed both. Neither is optional.
- **Key manual reference corrections by URL, never by anchor.** A308 keyed them by anchor and the five
  Difficulties Review volumes share author, year, and leading title, so regenerating the master for
  A309 permuted them and **every one of the five manual displays landed on a different volume than it
  named**. A URL is the only stable identity a harvest record has.
- **A regenerated table is not a source of truth either.** Reference-text defects belong in the master
  table rather than in the markdown, because the markdown is regenerated. A307 then lost a manual OCR
  correction when the master table was itself regenerated. **The fix must live in whatever produces the
  last artefact in the chain**, which in this toolchain is the normaliser. A310 added a rule there for
  en and em dashes, which arrive inside citation display strings when a disambiguation suffix is cut
  from a publisher's title and then violate the absolute prose style rule in the body.
- **Build the master from the CURRENT article's harvest alone unless the vehicles genuinely share
  one.** A309 read both its own and A308's directories, which was right because the X-12 is the X-11's
  airframe. A310 inherited that generator unchanged and would have imported six hundred documents
  about ballistic missiles into an article about a tail-sitting jet. **Check this whenever the
  toolchain is copied forward.**
- **Deduplicate the master table by URL.** A DOI arrives through more than one harvest file, because
  the DTIC prefix filter and the period date filter return overlapping records and successive modern
  sweeps overlap. A307 accumulated 105 duplicate URLs before this was noticed and its cited set was
  clean only by luck. Every generator since dedupes.
- **Use absolute paths in EVERY command, not only in edit scripts, and especially after any `cd`.**
  During the A307 publication review a rotation script with a relative path edited a scratch build
  copy and the verification read the same copy and reported success. **The draft was committed with
  the defect still present and the report to the pilot was wrong.** **In A310 this recurred three
  times in one session**, once when `_verify.py` run from inside the scratch build tree reported 40
  warnings instead of 21 and looked like a regression I had caused, and once when a process-file edit
  failed outright. **A check run from the wrong directory reports something untrue and looks like a
  finding.**
- **The equation pass creates reference debt, and the primary pass must be aimed at it.** True in A305
  through A310 without exception. Run a citation-coverage audit by section, counting citations per
  thousand words the way the equation audit counts equations, which found the debt precisely at
  fourteen thin sections in A307 and eleven in A308, rather than guessing. **But when the
  pool is small, harvest first and audit second.** A310's pool held 665 entries against A309's 3,597
  and would not have supported the 250 floor, so its primary pass opened with a supplementary harvest
  that took the pool to 1,305. Reversing the order was correct and the draft pass had predicted the
  need.
- **A whole-section replacement can silently drop equations.** A310's contemporary rewrite took the
  count from 91 to 88 and below the floor. Nothing failed. **Measure the count after any replacement
  rather than assuming the new text carries at least as much as the old.**
- **Title-token overlap is not proof of identity.** An NTRS query about the X-1 returned an X-2
  document and vice versa, both scoring 1.00, and two others returned "Lunar and Planetary Science
  XXXIV". A308 nearly cited a SNARK electron-beam paper for the Snark missile, and A307's DTIC queries
  on the Navaho returned antiseize compound for tanks and an air-cushion vehicle test programme.
  **Label every entry with the title the API returned, not the title you searched for**, and drop
  anything whose returned title does not describe a usable source.
- **A vehicle is indexed under the name its engineers used, not the name the public learned.** A307
  found the X-10 under its project number MX-770 and under nothing else, and the DTIC route that
  reaches Bell's own papers through MX-776 returned nothing whatever for MX-770 while the same route
  on the Atlas returned Flight Test Working Group reports and five volumes of a Difficulties Review. **A310 found that
  `X-13 Vertijet` and `vertijet` return nothing at all from NTRS while `Ryan X-13` returns the spin
  tunnel series and the one-fifth-scale hovering and transition tests.** Try the manufacturer plus
  designation, the project number, and the popular name separately before concluding scarcity, and
  check all three archives.
- **Generate the reference section from the anchors the body actually uses.** This structurally
  eliminates the orphan-definition defect that shipped in A300 and A301. The pattern is
  `used = sorted(set(re.findall(r"\]\[([a-z_0-9]+)\]", text)))`, then raise if any used anchor has
  no master-table entry. **Build each article's reference data from its own harvest.**
- **Enforce a link-text invariant: every prose citation text equals the master-table display for its
  anchor.** It caught display-string collisions automatically in A305, A306, and A307, and caught two
  newly-added anchors pointing at the wrong papers in A310. **Apply it to `research_` and `book_`
  anchors only**, since reference and related-post
  links legitimately use short inline text such as `X-1`.
- **Normalise author displays after every reference addition, not once.** Publishers hand Crossref
  names in capitals, so `BOWYER et al 1964` appears beside `Bowyer et al 1964` for two different
  papers, and the defence archive supplies corporate authors as place names, giving
  `Army Missile Command Redstone Arsenal Al 1963` and `Bell Aerospace Co Buffalo Ny 1953`, which decay
  under a surname parser to a trailing US state code and produce `Ca 1963` and `DC 1987`. Mark those
  unusable rather than trying to repair them. Both classes recurred in A306 after the normaliser had
  already run once, because references added later were never normalised. **Whitelist real acronyms**,
  because the naive capitalisation rule turns NACA into Naca, which is worse than the defect it
  repairs.
- **Check edit seams after inserting before existing text.** A297, A304, and A305 each produced a
  duplicated clause. A305 produced two insertions that split an argument from its conclusion. A307
  produced the same defect twice, once splitting a finding from its resolution and once burying a
  nine-item citation cluster inside the paragraph carrying an argument. **A310's primary pass left two clauses running together across a
  paragraph break, reading "…which is" at the end of one paragraph and "which is the correct
  decision…" at the start of the next.** **Every automated check passed all of them.** Read the
  connective lines by eye. This is the defect class with the longest unbroken run in the series.
- **Count equations and citations per section as structural audits, not only as density measures.**
  The A306 equation pass found four orphaned subsections that the reference generator, the build, and
  the style scan had all passed.
- **Vary the citation construction while writing, not afterwards.** A300 reached 70 percent of
  citations introduced by one preposition. The rule was known and violated again in A307 at 48
  percent, twice in A308 at 39 and 37, and in A309 at 31.3. **A309 also showed that a careless
  rotation trades one concentration for another**, since its first pass moved the leading construction
  off `is` and concentrated `appears in` at 7.7 percent instead, needing a second dispersal. Each was repaired by rotation, which works and is avoidable. **The
  house norm is a leading construction near 20 to 27 percent and a top bigram near 3 percent**, which
  A305 and A306 held by varying while writing and which every article since has had to reach by
  rotating afterwards. Measure the construction mix after every pass that adds references, and note that the single-word
  measure overstates the problem because it counts list-joining `and` and phrase-internal `in`, so the
  bigram measure is the honest one.
- **Re-derive every worked number independently.** Errors were found in nearly every article this way,
  including A303's decay-energy integral stated as 58 gigajoules when it computes to 73, A304's shock
  recovery stated as a factor of five when two sixteen-degree turns give 0.397 against 0.107 for a
  normal shock alone, a factor of 3.7, and A305's signal-to-noise ratio inflated 10 percent by a
  rounding carried through a link budget. **The verification can also be the
  thing that is wrong**, as happened four times: once when the article was right and the check used a
  different Reynolds number, once in A305 when a roll-resonance altitude failed against an
  exponential atmosphere of a single scale height and the US Standard Atmosphere confirmed the
  article, once in A308 when the checker compared the wrong row of a sensitivity table, and **twice in A309, once on
  a zero-target tolerance and once on a missing SI-to-cgs conversion in the Sutton and Graves
  correlation**. The second of those exposed real sloppiness in the article's unit labelling. State
  the inputs so the check is reproducible.
- **Beware rounding carried into a conversion.** A308 converted 153 decibels to a pressure and got 893
  pascals from the rounded level against 861 from the unrounded one, a 3.7 percent discrepancy from one
  rounding. **Compute through the unrounded intermediate quantity where one exists.**
- **Consecutive `$...$` lines render inline, not display.** Kramdown passes them through and MathJax
  applies `inlineMath` (`_includes/mathjax.html:5`). Three A302 Euler equations shipped that way.
  Separate display math with blank lines, and confirm the rendered display-block count against the
  source count in the built HTML.
- **The word-frequency check counts citation labels as prose, in two different ways.** `research`
  measures above 20 per thousand in every article and is entirely anchor names, so strip
  `[Display][anchor]` to `Display` before counting. Even then `nasa` and `naca` measure above threshold
  in every per-aircraft article and are almost entirely `[NACA 1953]` link text, so report the split
  and do not remediate a citation index for a style violation it does not have. Subject nouns
  legitimately exceed the 5.0 threshold and should be reported rather than remediated, as `error` was
  in A306, `flight` in A307, `pressure` and `atlas` and `tank` in A308, `atlas` in A309, and `aircraft`
  and `control` in A310.
- **An HTTP 200 is worthless from a search endpoint.** Open Library and NTRS `search?q=` return 200
  for nonsense. Only fixed identifiers and Wikipedia titles give a meaningful 404. Say so when
  reporting a sweep, and report the meaningful-404 count rather than the total swept. **Retry a timeout
  before recording a failure**, since NTRS produced transient read timeouts in A307, A308, and A309 and
  every one returned 200 on the next attempt.
- **Status codes mislead on DOIs in both directions.** Publishers return 403 (AIAA, APS, ASME, Royal
  Society, Taylor and Francis) or 202 (IEEE, Wiley). **Resolve every DOI through Crossref and compare
  on title at a 0.85 similarity threshold.** Crossref rate-limits at scale and returns 429; retry
  serially with backoff rather than treating it as a failure.
- **A thin result in one archive may mean the record lives in another, or under another name.** The
  X-6's record is in OSTI, not NTRS. The X-8's is in NTRS, not OSTI, with its 1946 to 1958 material
  largely in DTIC. The X-9's is overwhelmingly in DTIC. The X-10 is indexed under MX-770. **The X-13's
  own record is almost nothing anywhere, and the article stands on documents about the XFY-1, the
  XFV-1, the flight condition, the test technique, and the pilot's task.**
- **An article about a vehicle with almost no record of its own can still be dense, provided the
  question it asked was one other people were also asking.** That was true of the X-13 and was not true
  of the X-10, whose keystone was peculiar to a cancelled programme. **The difference is a property of
  the question rather than of the archive**, and it is worth assessing early because it decides whether
  a thin-looking subject can carry a full-length article.
- **An archive comparison measures what happened to a programme afterwards.** Open literature is
  systematically thicker where a technology found civilian use, so the Atlas has sixty years of
  launch-vehicle publication behind it and the Navaho has four years of cancelled-programme reporting.
  Say so when contrasting source bases.
- **Approach the density bands from below and let the later passes fill**, but see the warning in the
  series table above. **Padding to reach a band is forbidden and trimming to stay under one is worse.**
- **When a roster looks like a sequence, verify that it is one.** Designations are not assigned
  monotonically. Seven of the nine anomaly cases surfaced only after dropping that assumption.

## Verification Toolchain

- `python3 _verify.py` — offline corpus invariants, about 4 seconds. Also runs in CI and via
  `_hooks/pre-push`. Baseline is **0 errors, 21 warnings**; any new warning is yours. **Run it from
  the repository root**, since from inside a scratch build tree it scans the build copy and reports a
  different number.
- **NTRS citations API** — `https://ntrs.nasa.gov/api/citations/search?q=<terms>` and
  `/api/citations/<id>`. Short queries work; long ones return nothing because matching is near-AND.
  Cite `ntrs.nasa.gov/citations/<id>`, never a search URL. **The publication year is in
  `publications[0].publicationDate`**, not in `distributionDate` or `created`, both of which are
  archive-processing dates and read as 2013 for period documents. **The author field arrives as a dict
  rather than a string**, so unwrap before parsing a surname.
- **DTIC through Crossref** — the Defense Technical Information Center registers its reports under the
  **`10.21236` publisher prefix**, so `works?query.bibliographic=<terms>&filter=prefix:10.21236`
  harvests it and every result resolves and verifies like a journal article. **This is where
  weapon-programme, service, and contractor material lives.** It holds very little on a pure research
  aircraft, which is itself informative.
- **OSTI API** — `https://www.osti.gov/api/v1/records?q=<terms>&publication_date_end=<date>` and
  `/records/<id>`. Cite `https://www.osti.gov/biblio/<id>`. This is where Atomic Energy Commission
  and national-laboratory material lives.
- **Crossref** — `https://api.crossref.org/works/<doi>` to verify, and
  `works?query.bibliographic=...&filter=from-pub-date:YYYY-01-01,type:journal-article` to harvest
  contemporary literature, or `until-pub-date:1975-12-31` to harvest period papers. **Verify at a
  0.85 title-similarity threshold**, which is what A304 adopted after the fabricated-DOI incident,
  rather than the 0.5 used earlier.
- **Isolated build** — symlink `_posts`, `_layouts`, `_includes`, `_sass`, `css`, `assets`,
  `_plugins`, `_data`, `vendor`, `.bundle`, `_config.yml`, `Gemfile`, `Gemfile.lock` into a scratch
  directory, copy only `_drafts/x_planes_*.markdown` into its `_drafts/`, and run
  `JEKYLL_ENV=production bundle exec jekyll build --drafts --baseurl "" --destination _out`.
  A full-tree `--drafts` build fails on the pre-existing empty `post_url` in `_drafts/draft_summary.md`.
  **Confirm the rendered display-block count and the series navigation part number from the built
  HTML**, since both have caught real defects. The build takes about 5 to 10 seconds once warm.
- **Genre document** — `_docs/writing/RESEARCH_AIRCRAFT_STRUCTURE.md`. Bands are 1300 to 1600 lines,
  90 to 130 equations for a full aircraft and 120 to 160 for the opener, and 250 to 380 references.
  **Padding to reach a band is forbidden.** Report a shortfall instead. Twelve genre sections plus
  three series-standard extras, namely Comparison With Ground Prediction, The Contemporary
  Literature, and The Source Base, the last placed **immediately before Epistemic State**. An
  article-specific section may be added, and A307 through A310 each carry one, but it goes before The
  Source Base and never after Epistemic State.
- **Edit scripts are assertion-guarded.** Every bulk edit counts its exact-match target, collects
  failures, and leaves the file untouched unless all edits matched exactly once. Working copies live
  in the gitignored `tmp/`. **The A310 set is the current template**, at `tmp/a310/`, comprising
  `harvest.py`, `harvest2.py`, `harvest3.py`, `ntrs_detail.py`, `gen_master.py`, `normalise.py`,
  `gen_refs.py`, `verify_numbers.py`, `verify_urls.py`, and the pass scripts. It carries the URL
  deduplication, the URL-keyed manual-correction dict, the URL-stability guard, the dash
  normalisation, and absolute paths throughout. **Check its `gen_master.py` reads only the current
  article's directory before reusing it.**

## Open Decisions

1. **Categories.** `aerospace history engineering` has been carried through all fourteen articles and
   is still the agent's assumption. It fixes 72 URLs permanently at publication and the pilot has
   declined redirects. **This has now been raised eighteen times without an answer.** It remains
   reversible with one edit until the first publication. Mention it once per publication review and
   proceed; do not block on it.
2. **109 Open Library search URLs remain in A297**, and every later article adds more, since books are
   cited through `openlibrary.org/search?q=`. Open Library exposes a search API and the same upgrade
   that fixed the NASA citations would resolve them to edition pages. Offered, not taken up.
3. **The roster names the X-62 as Lockheed Martin.** Wikipedia titles it **General Dynamics X-62
   VISTA** because the airframe is a modified F-16D. A359 should name the disagreement rather than
   pick silently.
4. **A305 is 40 percent over the line ceiling and I offered a cut the pilot did not take.** The offer
   stands, and the material named was the measurement-method relations in What the Data Changed,
   roughly 300 lines and 25 equations. Do not act on it unprompted.
5. **The designation question has at least two mechanisms, and A310 settled its shape without
   resolving it.** A307 concluded the X-8, X-9, and X-10 were RTV-A vehicles absorbed wholesale. A308
   found the X-11 was never an RTV-A vehicle, so that explanation does not extend to it, and offered
   three readings without choosing. **A310 ends the run of five**, being a manufacturer's prototype in
   two examples under a research contract with no operational intent, which is exactly the pattern the
   X-1 established. **The run of five was therefore an interruption and not a redefinition**, and a
   closing article describing the series as having drifted from research aircraft to weapons would be
   contradicted by its own fourteenth entry. **A368 has to carry at least two coexisting mechanisms and probably more**,
   and each article from here should record which one its subject fits rather than restating the
   question.

## Governing Rules That Are Easy to Lose

- **The `post_url` interlock.** A tag whose target is absent from the build fails the entire site
  build. Under `future: false` that includes any forward-dated article. **The publication-order
  dependency is now fourteen deep**, A310 back to A297. They publish in order or together.
  Cross-references are **back-reference only**, never forward. A forward reference must be an external
  URL rather than a `post_url` tag, which is how A308 refers to the X-12.
- **Nothing in this series is published.** All fourteen are in `_drafts/`. The deploy workflow runs
  `bundle exec jekyll build` without `--drafts`, so pushing is safe. After every push, verify by
  reading `gh run view --json conclusion` directly and then curling the article URLs to confirm 404.
  **GitHub can be slow to create the run**, as it was for A307 where none existed for twenty-five
  minutes and two appeared later, both successful. Confirm the remote has the commit before
  diagnosing, and do not infer failure from an absent run.
- **Two-commit publication.** Staging commit with drafts in `_drafts/`, then a publication commit
  performing `git mv` into `_posts/` and syncing process files.
- **Commit once after every prompt**, including the `REVERSE_PROMPT.md` update. Sync
  `TASKLOG.md` and `_drafts/draft_summary.md` in the same commit.
- **Density conventions are absolute counts, not ratios.**
- **Prose style is absolute.** No contractions, em-dashes, en-dashes, prose colons, prose semicolons,
  or prose parentheticals. Every article ships a `<!-- Axxx -->` comment and a
  `<script>console.log("Axxx");</script>` immediately after the front matter. The `console.log` tag is
  the one permitted location for a semicolon and for parentheses, and a style scan that does not strip
  it will report one false positive of each. Headings use commas rather than colons; the title is the
  only permitted colon. **A dash can arrive from a publisher's title through a citation display
  string**, so scan the rendered prose and not only what you typed.
- **Do not infer a CI verdict from a chained shell exit code.** Poll rather than assuming.
- **Confirm before irreversible or outward-facing actions.** Push when asked. Never publish
  unprompted.
## The Roster, Embedded Because the Working Copy Is Gitignored

The pilot accepted a gitignored roster at `tmp/xplane_table.md`, which matches `.gitignore`. It is
reproduced here so it survives a clean checkout.

| Date | Article | Title |
|------|---------|-------|
| 2025-10-06 | A297 | X-Planes: Framing and the Research Aircraft Model |
| 2025-10-07 | A298 | X-Planes: Bell X-1 |
| 2025-10-08 | A299 | X-Planes: Bell X-2 |
| 2025-10-09 | A300 | X-Planes: Douglas X-3 Stiletto |
| 2025-10-10 | A301 | X-Planes: Northrop X-4 Bantam |
| 2025-10-11 | A302 | X-Planes: Bell X-5 |
| 2025-10-12 | A303 | X-Planes: Convair X-6 |
| 2025-10-13 | A304 | X-Planes: Lockheed X-7 |
| 2025-10-14 | A305 | X-Planes: Aerojet X-8 Aerobee |
| 2025-10-15 | A306 | X-Planes: Bell X-9 Shrike |
| 2025-10-16 | A307 | X-Planes: North American X-10 |
| 2025-10-17 | A308 | X-Planes: Convair X-11 |
| 2025-10-18 | A309 | X-Planes: Convair X-12 |
| 2025-10-19 | A310 | X-Planes: Ryan X-13 Vertijet |
| 2025-10-20 | A311 | X-Planes: Bell X-14 |
| 2025-10-21 | A312 | X-Planes: North American X-15 |
| 2025-10-22 | A313 | X-Planes: Bell X-16 |
| 2025-10-23 | A314 | X-Planes: Lockheed X-17 |
| 2025-10-24 | A315 | X-Planes: Hiller X-18 |
| 2025-10-25 | A316 | X-Planes: Curtiss-Wright X-19 |
| 2025-10-26 | A317 | X-Planes: Boeing X-20 Dyna-Soar |
| 2025-10-27 | A318 | X-Planes: Northrop X-21 |
| 2025-10-28 | A319 | X-Planes: Bell X-22 |
| 2025-10-29 | A320 | X-Planes: Martin Marietta X-23 PRIME and a Contested Assignment |
| 2025-10-30 | A321 | X-Planes: Martin Marietta X-24 |
| 2025-10-31 | A322 | X-Planes: Bensen X-25 |
| 2025-11-01 | A323 | X-Planes: Schweizer X-26 Frigate |
| 2025-11-02 | A324 | X-Planes: Lockheed X-27 |
| 2025-11-03 | A325 | X-Planes: Osprey X-28 Sea Skimmer |
| 2025-11-04 | A326 | X-Planes: Grumman X-29 |
| 2025-11-05 | A327 | X-Planes: Rockwell X-30 and the National Aero-Space Plane |
| 2025-11-06 | A328 | X-Planes: Rockwell-MBB X-31 |
| 2025-11-07 | A329 | X-Planes: Boeing X-32 |
| 2025-11-08 | A330 | X-Planes: Lockheed Martin X-33 |
| 2025-11-09 | A331 | X-Planes: Orbital Sciences X-34 |
| 2025-11-10 | A332 | X-Planes: Lockheed Martin X-35 |
| 2025-11-11 | A333 | X-Planes: McDonnell Douglas X-36 |
| 2025-11-12 | A334 | X-Planes: Boeing X-37 |
| 2025-11-13 | A335 | X-Planes: Scaled Composites X-38 |
| 2025-11-14 | A336 | X-Planes: X-39, Reserved but Never Assigned |
| 2025-11-15 | A337 | X-Planes: Boeing X-40 |
| 2025-11-16 | A338 | X-Planes: X-41 Common Aero Vehicle |
| 2025-11-17 | A339 | X-Planes: Orbital Sciences X-42 |
| 2025-11-18 | A340 | X-Planes: Micro-Craft X-43 Hyper-X |
| 2025-11-19 | A341 | X-Planes: X-44, One Designation and Two Aircraft |
| 2025-11-20 | A342 | X-Planes: Boeing X-45 |
| 2025-11-21 | A343 | X-Planes: Boeing X-46 |
| 2025-11-22 | A344 | X-Planes: Northrop Grumman X-47 |
| 2025-11-23 | A345 | X-Planes: Boeing X-48 |
| 2025-11-24 | A346 | X-Planes: Piasecki X-49 SpeedHawk |
| 2025-11-25 | A347 | X-Planes: Boeing X-50 Dragonfly |
| 2025-11-26 | A348 | X-Planes: Boeing X-51 Waverider |
| 2025-11-27 | A349 | X-Planes: X-52, the Designation Refused |
| 2025-11-28 | A350 | X-Planes: Boeing X-53 Active Aeroelastic Wing |
| 2025-11-29 | A351 | X-Planes: Gulfstream X-54 |
| 2025-11-30 | A352 | X-Planes: Lockheed Martin X-55 ACCA |
| 2025-12-01 | A353 | X-Planes: Lockheed Martin X-56 |
| 2025-12-02 | A354 | X-Planes: ESAero X-57 Maxwell |
| 2025-12-03 | A355 | X-Planes: X-58, the Slot Taken by XQ-58 |
| 2025-12-04 | A356 | X-Planes: Lockheed Martin X-59 Quesst |
| 2025-12-05 | A357 | X-Planes: Generation Orbit X-60 |
| 2025-12-06 | A358 | X-Planes: Dynetics X-61 Gremlins |
| 2025-12-07 | A359 | X-Planes: Lockheed Martin X-62 VISTA |
| 2025-12-08 | A360 | X-Planes: ABL Space Systems X-63 |
| 2025-12-09 | A361 | X-Planes: Invocon X-64 |
| 2025-12-10 | A362 | X-Planes: Aurora Flight Sciences X-65 CRANE |
| 2025-12-11 | A363 | X-Planes: Boeing X-66 |
| 2025-12-12 | A364 | X-Planes: X-67, the Slot Taken by XQ-67A |
| 2025-12-13 | A365 | X-Planes: General Atomics X-68 LongShot |
| 2025-12-14 | A366 | X-Planes: X-69 through X-75, the Leapfrogged Block |
| 2025-12-15 | A367 | X-Planes: Bell Textron X-76 SPRINT |
| 2025-12-16 | A368 | X-Planes: Synthesis and What the Designation Became |

## The Nine Anomaly Cases

Short articles by design, and the evidence for the closing article. The designation system is not a
counter.

- **X-23** — attributed to the Martin Marietta SV-5D PRIME, but USAF nomenclature records reportedly
  show X-23A was never assigned. State the conflict, do not resolve it.
- **X-39** — reserved 23 April 1997 for the AFRL Future Aircraft Technology Enhancements programme;
  no written allocation request followed.
- **X-41** — still-classified vehicle in the DARPA FALCON programme. No specifications released.
- **X-42** — sources disagree, one calling it an expendable upper stage and another a spaceplane test
  vehicle. No dedicated treatment exists anywhere.
- **X-44** — two different aircraft, the Lockheed Martin MANTA and a separate unmanned programme.
- **X-52** — requested 2006, refused over possible confusion with the B-52. The programme became X-53.
- **X-58** — skipped; slot consumed by the Kratos XQ-58 Valkyrie.
- **X-67** — skipped; slot consumed by the General Atomics XQ-67A.
- **X-69 to X-75** — unassigned and leapfrogged.

X-58 and X-67 were lost to the **parallel XQ- unmanned series drawing from the same numeric pool**,
which is a genuine finding about how the system evolved and belongs in the closer.

## Writing a New Handoff

Overwrite this file before a planned compaction, or when the pilot asks for a handoff. Then:

1. Set **Parent commit** to the current `HEAD`, because the handoff commit becomes the new tip and the
   state described is its parent.
2. Set **Branch**, **Written**, and **Tree at write** from the observed state. Read it; do not carry
   forward a remembered value.
3. Replace the resume prompt with what a fresh agent must know that the live channels do not say.
   Prefer pointers to on-disk sources over restating them, but **embed anything that lives only in a
   gitignored path**.
4. Carry forward open concerns, earned method rules, and governing constraints. Drop anything resolved.
5. Commit it as the tip. If anything lands afterward, the validity check will report it stale.

A handoff that is merely a summary of the resume channels is not worth writing. Its value is the
imperative direction and the hard-won rules that a summary would smooth away.
