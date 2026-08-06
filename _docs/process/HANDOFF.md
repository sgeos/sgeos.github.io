# Handoff Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

The self-contained, imperative resume prompt, written **before a planned compaction** and validated
on resume. Unlike the two resume channels it is **not** kept always-current. It is a snapshot stamped
with the commit it describes, so a stale handoff self-reports as stale rather than misleading a
resuming agent.

Adapted from the protocol in the `keleusma` repository at `docs/process/HANDOFF.md`.

## Validity

- **Branch**: `master`
- **Parent commit** (the repository state this handoff describes): `b8cba87`
- **Written**: 2026-08-06
- **Tree at write**: clean; everything through `b8cba87` is PUSHED and its CI run succeeded. This
  handoff commit will be the only unpushed commit.
- **Context**: the X-Planes series is IN PROGRESS. **Ten of seventy-two articles drafted, all four
  passes complete on each. None published.**

**Validity check — run on resume, before trusting this handoff.** On the branch above, compare the
**Parent commit** to `git rev-parse HEAD~1`. Because this handoff file is itself committed, its commit
advances the tip by one, so the state it describes is the parent of the handoff commit. The two match
**only** when this handoff commit is still the branch tip and nothing has landed after it.

- **Match → VALID.** Proceed per the resume prompt below.
- **Mismatch → INVALID and STALE.** A later commit moved the tip. Do **not** proceed and do **not**
  trust this handoff. Report the mismatch to the human pilot (recorded parent versus actual `HEAD~1`),
  familiarize from the live channels — `REVERSE_PROMPT.md`, `TASKLOG.md`, `_drafts/draft_summary.md`,
  and the git log, always authoritative — and wait for instruction.

## Resume prompt — the next prompt will be "Please draft A307, 'X-Planes: North American X-10.'"

**Nothing is outstanding.** A306 finished all four passes, is committed and pushed, and CI succeeded.
Every article through A306 is at the same state. There is no half-finished pass to pick up.

**Wait for the pilot's prompt.** Do not begin A307 unprompted. When it comes, follow the rhythm below.

**A307 is the third consecutive article whose subject is not an aircraft**, after the [X-8] sounding
rocket and the [X-9] missile testbed, and it is the point at which that stops being two exceptions and
starts being a pattern the series should name. The X-10 is the North American Navaho testbed. It is
also the first of the three that took off and landed on its own undercarriage, so the "not an
aircraft" framing has to be argued rather than asserted. **Keep the designation question open.** The
closing article at A368 is where it resolves, and A305 and A306 both deliberately left it unresolved.

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

The `Eq` column is display blocks as counted and reported at the time of each publication review. A
naive `grep -c '^\$\$'` halved does not reproduce it, so do not "correct" the table from that. For
articles whose equations are written as single-line `$$...$$` blocks, which is the A305 and A306
style, the count is one per line rather than one per two.

**A305 is the outlier and A306 is the model.** A305 exceeded all three ceilings, at 2226 lines against
1600, 200 equations against 130, and 474 references against 380. A306 finished inside all three with
no overage argued for, which is a first for this series. The difference was approach direction rather
than restraint, and it is written up as a method rule below.

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
settled at 101 to 155 while the percentage swung on the denominator**, giving A301 101 at 35.8
percent, A302 109 at 30.6, A303 105 at 35.4, A304 107 at 40.2, A305 155 at 37.8, and A306 110 at 36.2.
The count is the stable measure and the percentage is not, because an article carrying fewer dated
references overall reports a higher share for the same work. **Treat 28 to 33 percent as a floor
rather than a ceiling**, and say explicitly in the report when a figure exceeds it deliberately.

**Assemble the contemporary set by DOI taken from the harvest records.** See the first method rule
below for why this is stated as a rule rather than as a preference.

**Aim the contemporary sweep at the threads the equation and primary passes opened, not at the
article's original topics.** A305 and A306 both did this and it is what makes the additions attach to
the article's own derivations rather than sitting beside them. The best single result in A306 came
this way, namely that the resolution factor the article treats as a constant of order twenty is, in
the modern literature, the output of a computation.

## Method Rules Earned the Hard Way

These are the reason this handoff is worth writing. Each cost a real defect.

- **An identifier that can be looked up must never be constructed.** While assembling the
  contemporary set during the A304 draft pass I hand-built nineteen plausible-looking DOIs rather
  than reading them out of the harvest records. Crossref showed most resolving to entirely unrelated
  papers, including one on dendrite deformation and one on alcohol licensing policy. All were
  discarded and the set was rebuilt from actual records. **Take every DOI, NTRS id, OSTI id, and DTIC
  id verbatim from the record that returned it.** This is the single most serious defect in the series
  so far. A306 contains no hand-entered identifier at all, which is the standard to hold.
- **Resolve the anchor index from harvest metadata BEFORE drafting, not after.** This supersedes the
  weaker rule that author names cannot be inferred from titles, which was known and still violated.
  A304 guessed 31 keys and had to remap 42 citations. A305 guessed twenty and **every one was wrong**,
  with a further 23 caught only because I checked before running the pass. A306 built a greppable
  anchor index from the metadata first and all 239 anchors landed correctly on the first attempt.
  **The remedy is ordering, not care.**
- **Compute the worked numerics before writing, not while writing.** A306 was the first article in the
  series to pass its first numeric verification with zero corrections, and the only procedural
  difference was that every number was computed in a scratch script and then written into prose.
- **The equation pass creates reference debt, and the primary pass must be aimed at it.** In both A305
  and A306 every relation the equation pass added arrived without its period source. Plan the primary
  harvest around the equation pass's topics rather than around the article's original ones.
- **Title-token overlap is not proof of identity.** An NTRS query about the X-1 returned an X-2
  document and vice versa, both scoring 1.00. Two others returned "Lunar and Planetary Science
  XXXIV". **Label every entry with the title the API returned, not the title you searched for**, and
  drop anything whose returned title does not describe a usable source.
- **Generate the reference section from the anchors the body actually uses.** This structurally
  eliminates the orphan-definition defect that shipped in A300 and A301. The pattern is
  `used = sorted(set(re.findall(r"\]\[([a-z_0-9]+)\]", text)))`, then raise if any used anchor has
  no master-table entry. **Build each article's reference data from its own harvest**, and never
  import the previous article's generator, because **a generator is a source of truth only while it
  still generates the file** and the imported one has drifted from additions made directly to that
  article's markdown. The integrity check caught this in both A300 and A301, which is luck rather
  than method; generating from body anchors is the method.
- **Enforce a link-text invariant: every prose citation text equals the master-table display for its
  anchor.** Adopted during A305 and it earns its keep. It caught both display-string collisions in
  A305 and both in A306 automatically, which is the first time an invariant rather than a read caught
  that class. It also resynchronised 53 stale link texts in A305 that an earlier case normalisation
  had left behind.
- **Normalise author displays after every reference addition, not once.** Publishers hand Crossref
  names in capitals, so `BOWYER et al 1964` appears beside `Bowyer et al 1964` for two different
  papers. The defence archive supplies corporate authors as place names, giving
  `Army Missile Command Redstone Arsenal Al 1963` and `Bell Aerospace Co Buffalo Ny 1953`. Both
  recurred in A306 after the normaliser had already run once, because references added later were
  never normalised. **Re-run the normaliser at the end of every pass that adds references.**
- **Correct reference-text defects in the master table, not in the markdown.** En-dashes and
  parentheticals fixed in the article are silently undone by the next regeneration.
- **Check edit seams after inserting before existing text.** The A297 equation pass produced two
  duplicated clauses, the A304 equation pass produced another that said the flame must be anchored
  twice in consecutive sentences, and the A305 equation pass produced a third about an aspect
  ambiguity. **Every automated check passed all of them.** They surfaced only during unrelated reads.
  Read the connective lines by eye. In A305 a read also found two insertions that had split an
  argument from its conclusion and orphaned a citation from its subject, neither of which any check
  looks for.
- **Count equations per section as a structural audit, not only as a density measure.** The A306
  equation pass began with a per-section count and the count found four orphaned subsections at the
  end of The Contemporary Literature, three of them duplicating headings the draft expansion had
  already written. The cause was an edit that matched one heading and left the four stubs below it.
  The reference generator, the build, and the style scan were all clean while three headings appeared
  twice.
- **Writing a relation down catches arithmetic the draft carried as an assertion.** Two articles
  running. A305's thrust coefficients and characteristic velocity were quoted from secondary
  compilations and all three were wrong. A306 asserted that eight guidance time constants reduce an
  error by two orders of magnitude, which describes the bare exponential and ignores a polynomial
  factor of 85. **If the prose reasons about a quantity qualitatively, compute it.**
- **Bulk reference additions introduce formulaic repetition wholesale.** A300 reached 70 percent of
  citations introduced by the preposition `in` because 40 primaries went in during one pass with one
  construction. **Vary the construction while writing, not afterward.** The drift recurred in A302,
  A303, and A304 despite the rule being known, so also measure the preposition mix after every
  reference pass. A305 and A306 both held the top construction near 20 to 27 percent by varying while
  writing, which suggests the rule works when applied at composition time and not otherwise.
- **Re-derive every worked number independently.** Errors were found in *every* article this way
  except A303's final pass and A306's draft pass, including A303's decay-energy integral stated as 58
  gigajoules when it computes to 73, A304's shock recovery stated as a factor of five when two sixteen-degree turns give 0.397 against
  0.107 for a normal shock alone, a factor of 3.7, and A305's signal-to-noise ratio inflated 10 percent by a rounding carried through a link budget.
  **The verification can also be the thing that is wrong**, as happened twice, once when the article
  was right and the check used a different Reynolds number, and once in A305 when a roll-resonance
  altitude failed against an exponential atmosphere of a single scale height and the US Standard
  Atmosphere confirmed the article. State the inputs so the check is reproducible.
- **Consecutive `$...$` lines render inline, not display.** Kramdown passes them through and MathJax
  applies `inlineMath` (`_includes/mathjax.html:5`). Three A302 Euler equations shipped that way.
  Separate display math with blank lines, and confirm the rendered display-block count against the
  source count in the built HTML.
- **The word-frequency check counts citation labels as prose.** `nasa` and `naca` measure above
  threshold in every per-aircraft article and are almost entirely `[NACA 1953]` link text. Report the
  split; do not remediate a citation index for a style violation it does not have.
- **An HTTP 200 is worthless from a search endpoint.** Open Library and NTRS `search?q=` return 200
  for nonsense. Only fixed identifiers and Wikipedia titles give a meaningful 404. Say so when
  reporting a sweep, and report the meaningful-404 count rather than the total swept.
- **Status codes mislead on DOIs in both directions.** Publishers return 403 (AIAA, APS, ASME, Royal
  Society, Taylor and Francis) or 202 (IEEE, Wiley). **Resolve every DOI through Crossref and compare
  on title at a 0.85 similarity threshold.** This caught a nonexistent identifier and one resolving to
  an unrelated paper on bipropellant exhaust optics, before it caught the nineteen above. Crossref
  rate-limits at scale and returns 429; retry serially with backoff rather than treating it as a
  failure.
- **A thin result in one archive may mean the record lives in another.** The X-6's record is in OSTI,
  not NTRS. The X-8's is in NTRS, not OSTI, and its 1946 to 1958 material is largely in DTIC. The X-9's
  is overwhelmingly in DTIC because a weapon programme reports to a service that keeps its reports.
  **Check all three before concluding scarcity**, and note that on the aerospace archive alone the X-8
  era looks poorly documented and that conclusion is wrong.
- **Approach the density bands from below and let the later passes fill.** A305 wrote long and finished
  200 percent over on lines. A306 finished the draft under band on all three, the equation pass brought
  two inside, and the primary pass brought the third, with nothing cut at any point. **Padding to reach
  a band is forbidden and trimming to stay under one is worse**, so the only safe direction of approach
  is upward.
- **When a roster looks like a sequence, verify that it is one.** Designations are not assigned
  monotonically. Seven of the nine anomaly cases surfaced only after dropping that assumption.

## Verification Toolchain

- `python3 _verify.py` — offline corpus invariants, about 4 seconds. Also runs in CI and via
  `_hooks/pre-push`. Baseline is **0 errors, 21 warnings**; any new warning is yours.
- **NTRS citations API** — `https://ntrs.nasa.gov/api/citations/search?q=<terms>` and
  `/api/citations/<id>`. Short queries work; long ones return nothing because matching is near-AND.
  Cite `ntrs.nasa.gov/citations/<id>`, never a search URL. **The publication year is in
  `publications[0].publicationDate`**, not in `distributionDate` or `created`, both of which are
  archive-processing dates and read as 2013 for period documents.
- **DTIC through Crossref** — the Defense Technical Information Center registers its reports under the
  **`10.21236` publisher prefix**, so `works?query.bibliographic=<terms>&filter=prefix:10.21236`
  harvests it and every result resolves and verifies like a journal article. Found during the A305
  primary pass and used from the start in A306. **This is where weapon-programme, service, and
  contractor material lives**, and it is the reason A306 could cite Bell's own project documents.
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
  HTML**, since both have caught real defects. The build now takes about 70 seconds rather than 5.
- **Genre document** — `_docs/writing/RESEARCH_AIRCRAFT_STRUCTURE.md`. Bands are 1300 to 1600 lines,
  90 to 130 equations for a full aircraft and 120 to 160 for the opener, and 250 to 380 references.
  **Padding to reach a band is forbidden.** Report a shortfall instead. Twelve genre sections plus
  three series-standard extras, namely Comparison With Ground Prediction, The Contemporary
  Literature, and The Source Base, the last placed before Epistemic State.
- **Edit scripts are assertion-guarded.** Every bulk edit counts its exact-match target, collects
  failures, and leaves the file untouched unless all edits matched exactly once. Working copies live
  in the gitignored `tmp/`. The A306 set is the current template and is the cleanest, being
  `tmp/a306/harvest.py`, `tmp/a306/ntrs_detail.py`, `tmp/a306/gen_refs.py`,
  `tmp/a306/verify_numbers.py`, `tmp/a306/verify_urls.py`, and the four pass scripts.

## Open Decisions

1. **Categories.** `aerospace history engineering` has been carried through all ten articles and is
   still the agent's assumption. It fixes 72 URLs permanently at publication and the pilot has
   declined redirects. **This has now been raised nine times without an answer.** It remains reversible
   with one edit until the first publication. Mention it once per publication review and proceed; do
   not block on it.
2. **109 Open Library search URLs remain in A297**, and every later article adds more, since books are
   cited through `openlibrary.org/search?q=`. Open Library exposes a search API and the same upgrade
   that fixed the NASA citations would resolve them to edition pages. Offered, not taken up.
3. **The roster names the X-62 as Lockheed Martin.** Wikipedia titles it **General Dynamics X-62
   VISTA** because the airframe is a modified F-16D. A359 should name the disagreement rather than
   pick silently.
4. **A305 is 40 percent over the line ceiling and I offered a cut the pilot did not take.** The offer
   stands, and the material named was the measurement-method relations in What the Data Changed,
   roughly 300 lines and 25 equations. Do not act on it unprompted.

## Governing Rules That Are Easy to Lose

- **The `post_url` interlock.** A tag whose target is absent from the build fails the entire site
  build. Under `future: false` that includes any forward-dated article. **The publication-order
  dependency is now ten deep**, A306 back to A297. They publish in order or together.
  Cross-references are **back-reference only**, never forward.
- **Nothing in this series is published.** All ten are in `_drafts/`. The deploy workflow runs
  `bundle exec jekyll build` without `--drafts`, so pushing is safe. After every push, verify by
  reading `gh run view --json conclusion` directly and then curling the article URLs to confirm 404.
- **Two-commit publication.** Staging commit with drafts in `_drafts/`, then a publication commit
  performing `git mv` into `_posts/` and syncing process files.
- **Commit once after every prompt**, including the `REVERSE_PROMPT.md` update. Sync
  `TASKLOG.md` and `_drafts/draft_summary.md` in the same commit.
- **Density conventions are absolute counts, not ratios.**
- **Prose style is absolute.** No contractions, em-dashes, en-dashes, prose colons, prose semicolons,
  or prose parentheticals. Every article ships a `<!-- Axxx -->` comment and a
  `<script>console.log("Axxx");</script>` immediately after the front matter. The `console.log` tag is
  the one permitted location for a semicolon and for parentheses, and a style scan that does not strip
  it will report one false positive of each.
- **Do not infer a CI verdict from a chained shell exit code.** CI now takes six to ten minutes rather
  than two, so poll rather than assuming.
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
