## Last Updated

**Date**: 2026-08-13
**Task**: **A373 PUBLISHED and PUSHED.** It is live at the editorial date 2026-08-10 as Part 5 of the
Keleusma Research Spikes series.

---

## It Is Live, and Four Other Pages Changed With It

**A373 is published** at
`/engineering/compilers/verification/security/2026/08/10/when_error_correction_meets_a_signature.html`.

**Publishing renumbered four live pages**, exactly as flagged across three passes. A369 through A372 now
read **Part 1, 2, 3 and 4 of 5** where they read **of 4** before, and A373 reads **Part 5 of 5**. All five
were checked on the built site rather than assumed.

**It was verified against the real deploy condition**, which is a build **without** `--drafts`, because
that is what the workflow runs. A clean `--drafts` build proves nothing about the deploy.

**The interlock was checked before the move**, not after. The date slot was free, all four `post_url`
targets were already published, and nothing forward-referenced the article.

**`_verify.py` 0 errors and 0 warnings across 301 posts. `./_check.sh` clean at 465 pages.** The article
appears on the home page, in `feed.xml` and in `sitemap.xml`.

**Its section was removed from `_drafts/draft_summary.md`**, which tracks `_drafts/` only, leaving 52
files.

---

## The Word You Named Was Not the Problem

**`specific` is 2 uses at 0.23 per thousand**, far under any limit. I checked it first because you named
it.

**The measurement had to strip link pairs or it could not have fired at all.** This article carries
459,066 raw body words against **8,522 words of author prose**, a **dilution factor of 52.7**, the highest
in the series. Measuring the raw body would have divided every rate by fifty and guaranteed silence.

---

## The Finding Was a Template, Not a Word

**Thirteen survey subsections opened with an identical frame and closed with an identical hedge**,
differing only in a cluster name and two numbers. That is the A371 lesson repeating, and no single-word
instrument can see it.

**The hedge is now stated once, structurally, with the reason** that a hedge repeated on every heading
stops being read, which is exactly the fix A337 applied to `typically`.

**The thirteen frames are replaced by one table** of cluster sizes. That is better than deleting them,
because thirteen scattered counts cannot be compared and a table can.

**The table's shape turned out to be a finding.** Check-then-use is the smallest cluster by an order of
magnitude, which says that **the composition question this article asks has been answered in one field
and barely posed in the other**. That sentence is now in the article.

---

## An Impossible Count, Found on the Way

**The Source Base claimed 13,788 harvested works against an anchor gate that passed 13,741.** You cannot
finish with more than the gate let through.

The reference list holds **13,722**. Every figure now comes from a count of the list rather than from the
pipeline log, and **the 19-record discrepancy against the gate is stated rather than smoothed**. The
hand-selected total fell 66 to 65, since the primary pass removed the MacWilliams entry, and the whole
accounting reconciles at **13,722 plus 65 equals 13,787**.

---

## Twelve Words Above the Peer Maximum, and All Twelve Are Legitimate

Measured against 256 published peers: **scrub, fault, faults, signature, syndrome, parity, word, wrong,
artefact, repair, authentication and integrity**. No peer article writes about this subject, so of course
they are elevated. **This is the `specific impulse` case**, and each was classified rather than assumed.

**`rather` was checked and left alone.** Its thirty-seven uses carry thirty-seven distinct constructions,
so it is varied rather than formulaic, and A369's rule is that a mechanical substitution moves a tic
rather than removing it.

**Repeated four-gram counts fell from 13 to 4**, and nothing that remains is boilerplate.

---

## One Thing Needs Your Decision

**Publishing this would change four live pages.** A369 through A372 are published and their navigation
reads **Part 1 to 4 of 4**. A373 sits at index 5, so publishing renumbers all four to **of 5**.

**That is a change to live pages and I have not made it.** The article is committed, pushed and not
published, which is what you asked for.

---

## The Publication Pass

**The survey audit found no thin subjects**, which is the first of three consecutive publication reviews
where none appeared. A337 had relative density at zero and A338 had the entry corridor at nine; this
article's lowest are time-of-check-to-time-of-use and syndrome decoding, both comfortably covered.
**Contemporary coverage is 56.6 percent of dated entries from 2015 or later and 34.7 percent from 2020 or
later**, against a median year of 2016.

**Six acronym and style defects were fixed.** The worst was **`ECC` unexpanded in a section heading**,
now error-correction. `API`, the Trusted Computing Group and the File and Storage Technologies conference
are spelled out. **The cyclic redundancy check is glossed in the prose beside the quotation that names
it**, rather than by altering the quotation, since a quotation must not be edited to suit a style rule.

**All-caps emphasis was used once** and is corrected to bold, which is the style guide's rule.

**Structural conformance matches the published sibling A372 heading for heading.**

---

## What This Article Cost Across Four Passes, Worth Knowing

**The draft pass** removed 44 prose colons and semicolons, converted four cross-references from hardcoded
absolute URLs to `post_url` tags so they carry the build-time interlock, and renamed the two composition
orders from **(A)** and **(B)** to **verify-then-scrub** and **scrub-then-verify**, which was the whole of
the general-audience retarget and removed every prose parenthesis at the same time.

**The equation pass** went 24 to 32 and found that the six hand-chosen triple faults which mis-corrected
at 100 percent were **every way of choosing three positions from eight**, so the biased sample was biased
**toward the physically likely case**, which the memory field studies say is clustering. It also fixed a
**pre-existing build break** that was not mine, four stale `post_url` dates across three unrelated
pre-release drafts.

**The primary pass** found **three foundational citations pointing at the wrong works**, including Shannon
1948 resolving to a 2009 encyclopaedia entry about the paper. All 57 inline citations were then checked
against the registry and every one now agrees.

---


## Three Foundational Citations Pointed at the Wrong Works

**The primary base was already strong, so this became a verification pass.** The engineering session had
already cited **57 primary works inline**, covering Shannon, Hamming, Hsiao, Bellare and Namprempre,
Krawczyk, Kim on Rowhammer, the memory field studies, and Bishop and Dilger on
time-of-check-to-time-of-use. That is a far better base than A337 or A338 arrived with.

**So I checked the citations instead of hunting for more, and three of the most foundational were wrong.**

- **Shannon 1948** resolved to a **2009 SAGE encyclopaedia entry** about the paper, not the paper.
- **Gallager 1962** resolved to a Cambridge book chapter, not the IEEE paper.
- **MacWilliams and Sloane 1977** resolved to a 2004 chapter called `Group theory and error-correcting
  codes` in an entirely different book.

**All three are the exact defect the article's own Source Base describes**, a real registered work with a
plausible title. The article boasts of catching eleven of these; three survived into the load-bearing
citations.

**Shannon and Gallager were corrected to identifiers verified by author, title, container and year.**
MacWilliams and Sloane has **no registered identifier at all**, so it is now **named without a link**,
which is the article's own stated policy that a plain mention is honest where an identifier resolving to
something else is not.

**I then checked all 57 inline citations against the registry. Every one agrees.**

---

## Four Named Primaries Had Nothing Behind Them

Flip Feng Shui, the TCG integrity measurement paper, the ZFS end-to-end integrity study, and **Bishop and
Dilger** were all named in prose with **no link**, because USENIX and FAST register no identifiers. Bishop
and Dilger matters most, since their naming of the time-of-check-to-time-of-use flaw is the closest prior
statement of this article's central point.

**Lacking an identifier is not the same as lacking a citation.** All four now carry stable publisher URLs,
verified at 200. The curated set went from 8 to 12.

---

## Read This, Because I Nearly Committed the Defect I Was Fixing

Looking for a stable identifier for the MacWilliams and Sloane book, I tried a candidate Open Library key.
**It returned HTTP 200 and resolved to `Motor Racing (Inside Story)`.**

**That is the same failure mode, arrived at while correcting it.** The memory note that an Open Library
search endpoint cannot return a not-found is the only reason I checked rather than pasting it in. **A
status code is not a citation check.**

---

## Read This First, Because the Build Was Broken and It Was Not This Article

**`./_check.sh --drafts` started failing partway through this pass**, on a `post_url` in
`_drafts/claude_code_getting_started_on_openbsd.markdown` pointing at
`2026-02-24-claude_code_getting_started_on_freebsd`, which does not exist.

**I proved it was pre-existing before touching anything**, by reproducing the failure at HEAD with the
A373 draft removed from the tree entirely. It is not caused by this work.

**The cause is stale dates.** Four `post_url` targets across three pre-release-candidate drafts reference
**2026-02-2x** while those drafts now carry dates of **2026-08-1x**. They were re-dated at some point and
the tags were not moved with them. **The two targets that point at published posts were correct and I left
them alone.**

**It is date-sensitive, which is why it surfaced today rather than earlier.** A `post_url` to a
future-dated draft is not exercised until that date arrives.

**All 961 `post_url` targets across every draft now resolve**, and the page count rose from **512 to 514**,
which confirms two drafts had not been building at all.

---

## The Equation Pass

**The strongest addition connects the code's worst case to the field literature the article already
cites.** The six hand-chosen triple faults that mis-corrected at 100 percent were all confined to one
byte, and **every way of choosing three positions from eight is 56**, so that sub-sweep is exhaustive too.
**All 56 mis-correct, against 56.08 percent unconditionally, a factor of 1.783.**

**The memory field studies report that faults cluster.** So the accidental bias in the hand-chosen sample
was **toward the physically likely case**, which is the one direction a biased sample is not harmless in.
The article previously treated the biased sample only as an error to confess; it is now also evidence.

**An exhaustiveness identity was added**, 23,364 mis-corrected plus 18,300 refused equal to 41,664, which
shows the enumeration is complete rather than merely large.

**Further additions** cover the binomial generator behind the opening table, the measured rates as the
divisions they are, the heuristic against the measurement at 0.17 percentage points, the small-artefact
overhead at 20.0 percent against a documented 12.5 with a 1.60 excess factor, the crossover across four
artefact sizes, and the compound exposure probability in the time-of-check window. **The article
explicitly declines to estimate the first factor of that product**, because it depends on medium,
exposure and workload, none of which is measured.

**24 to 32 display equations.** `tmp/a373/verify.py` recomputes **31 results** from the code parameters
and the raw instrument counts rather than from the quoted percentages, and shares no code with the draft.

**Two self-inflicted defects were caught during the pass**, an inserted equation that absorbed the
following prose onto its own source line, and a display duplicated between the summary and the
derivation. Both are the same class the A338 pass recorded.

---

## What Arrived and What I Did

**The source was already in good shape.** It came stamped A373 with the correct series, editorial date
and index, and already carried its harvested survey at 13,800 references. **I did not rewrite it.** The
work was standards conformance and the general-audience retarget.

**42,362 lines, 24 display equations, 13,800 reference definitions, 458,572 words**, of which 8,305 are
author prose.

---

## The Retarget Was Mostly One Change

**The two candidate orders were labelled (A) and (B) in seventeen places.** They are now
**verify-then-scrub** and **scrub-then-verify**.

**That single change did three things at once.** It puts the meaning in the name, so a reader never has
to hold a mapping in their head. It **removed every prose parenthesis in the article**, since the labels
were the only ones. And it made the result headings self-explanatory, because one of them already said
"Scrub-Then-Verify" while the body said "(B)".

**Two smaller changes finish it.** A skip signpost at the head of the algebra tells a reader who wants
the argument rather than the derivation to go straight to The Measurement, and says what the algebra is
for so skipping it is an informed choice. **The syndrome is glossed in plain words at first use**, since
it appears fourteen times and was previously defined only in symbols.

---

## Standards Work

**44 prose colons and semicolons removed**, across the author prose and the survey leads both. The source
used the colon as an introducing device throughout, which the house style does not permit.

**The cross-references were hardcoded absolute URLs and are now `post_url` tags.** That matters beyond
tidiness: a hardcoded path **bypasses the build-time interlock**, so it would rot silently if a category
or date ever changed, where a `post_url` fails the build loudly. All four targets were verified present
in `_posts/` and their built URLs confirmed against a production build **before** converting.

**Two constructions sat above the corpus maximum**, `which is` at 5.66 per thousand against 5.29, and
`worth showing`, which no peer article has ever used. Fifteen uses were varied **across a rotation rather
than by one replacement**, per A369's lesson, taking `which is` to **3.85** and the count above maximum
to zero.

---

## One Thing You Should Decide, Not Me

**Publishing this would change four live pages.** A369 through A372 are published and their navigation
reads **Part 1 to 4 of 4**. A373 sits at index 5, so publishing renumbers all four to **of 5**.

**That is a change to live pages and I have not made it.** The article is not published and the draft
pass does not push.

---

## Verification

- `python3 _verify.py` **0 errors, 0 warnings**. `./_check.sh --drafts` clean at **512 pages**, 212
  carrying display math, no rendered findings.
- Reference integrity **13,800 used against 13,800 defined**, zero undefined, zero orphaned, all
  definition groups sorted.
- **Zero em dashes, en dashes, contractions, prose colons, prose semicolons and prose parentheses.**
- **8 of 8 curated URLs at 200**, and a sample of 15 harvested identifiers resolving 15 of 15.
- The one block-form `cases` equation is confirmed permitted by `MATHJAX_CONVENTIONS.md`, which allows
  delimiters on separate lines, and it renders.
- Diction **0 constructions above the corpus maximum** against 300 peers.

---

## Outstanding

**One pass remains**, being the publication review, which commits and pushes but does not publish.

**The X-Planes mainline is untouched by this and remains at forty-two of seventy-two**, all four passes
complete on each, none published and none authorised. **A339, the Orbital Sciences X-42, starts only on
your prompt.**

---

## From A338, the X-41 Common Aero Vehicle, Which Is Complete and Pushed


## The Survey's Thinnest Subject Was the Article's Central Construct

**The entry corridor measured nine records.** The corridor is the whole sizing argument of this article,
the squeeze between flying low enough to be held up and high enough to survive, and the survey had almost
nothing on it. **Cross-range stood at fourteen** against a Dependent Systems paragraph that leans on it.

**A supplementary harvest of 3,075 records closed both**, taking the corridor from **9 to 45** and
cross-range and footprint from **14 to 59**.

**This is the second consecutive article whose survey audit found a displayed subject at or near zero.**
A337's was relative density. The pattern is the same each time: the first harvest asks for the subject the
article is *about*, and misses the construct the article *reasons with*.

---

## The Supplementary Set Was Audited This Time

**A337 audited its first harvest by reading samples and did not audit the supplementary one**, and two
homonym families entered through the new anchors as a result. That gap is now closed as routine.

**The sample came back clean**, twenty-four records all on subject, and no new family was found. The
anchor-collision check also ran before merging and returned zero, and **all eight cluster blocks were
rebuilt from the harvest files rather than patched**, so every count in the survey is derived rather than
edited.

---

## The Template Leak Is Fully Swept

The primary pass found three of A337's sentences sitting in this article's Source Base, including a
finding about animal-behaviour apparatus and a reference to the wrong vehicle. **I swept the whole article
afterwards and none remain.** The only mention of another article's vehicle is a legitimate Related Post
entry.

---

## The Curated Set Had No Primary Sources At All

**Two designation references, four encyclopaedia articles, one trade report and one programme overview.**
That was the entire evidentiary base for an article whose **whole argument is a derivation**.

**Citing an encyclopaedia for the relations you are deriving is exactly backwards.** I harvested 86 NASA
reports, selected 23, and cited three canonical papers the harvest had already found and the prose had
been ignoring. **The primary share of the curated set went from 0 to 76 percent.**

---

## Three Additions Carry Relations the Article Was Already Using

- **The equilibrium glide range relation is Eggers and colleagues**, published 1955 and refined through
  1958, **before any such vehicle existed**. The article derives it, uses it for every range figure, and
  had been treating it as common knowledge.
- **The lift to drag ceiling is Küchemann 1965**, which the harvest had already surfaced and the prose had
  never cited.
- **The stagnation-point heating form** belongs to a family running from Fay and Kemp through free-flight
  measurement at Mach 14.6 to modern blunt-body procedures.

**The article had been using all three and citing none of them.**

---

## The Central Contradiction Turns Out to Have Its Own Literature

**An aerothermal performance constraint analysis of sharp nosecaps and leading edges** works the
sharp-versus-blunt trade from the materials side, and a flight experiment programme was built specifically
to attack it. **The contradiction derived here is a recognised design problem rather than a novel claim**,
which is a stronger position than deriving it alone.

**The Küchemann ceiling is now corroborated with the measurements it summarises**, being wind tunnel and
free-flight characterisations of hypersonic glider, all-body and lifting-body configurations. **None
reports a ratio near what the mission would need at Mach 20**, which is the empirical form of the same
conclusion.

**And the failure board's ground-test conclusion was stated in advance**, by a 1997 survey of hypersonic
flight experimentation subtitled status and shortfalls. **The board did not discover that ground test runs
out. It confirmed it with two vehicles.**

---

## Read This, Because a Template Leaked

**The Source Base had been adapted from A337's and carried three of its sentences unaltered.** One was a
finding about **the runway as an apparatus in animal behaviour research**, which is that article's homonym
family and has nothing to do with this one. Another referenced **the wrong vehicle**.

**A template that is edited rather than rewritten will leak**, and it did. The section is rewritten and
the leak is recorded in the article itself rather than quietly fixed.

**The anchor-collision check ran before merging this time**, per the defect A337 reproduced, and returned
zero.

---

## The Best Addition Recovers the Planned Flight Time

**The draft reproduced the intended distance from two published numbers. It now reproduces the intended
duration from the same two.**

Integrating the glide deceleration gives **29.3 minutes against a planned thirty**. So the published lift
to drag ratio of 2.6 and the stated Mach 20 now account for **both the distance and the time** of the
flight that was intended. **That is the strongest available check that the model describes this vehicle
rather than something else**, and neither figure was used to fit it.

The deceleration itself is gentle, **0.17 of a gravity at entry rising to 0.36 as the centrifugal relief
disappears**, which is why the flight takes half an hour rather than minutes.

---

## The Boost Cost Is Now Exact Rather Than Rhetorical

The draft said the vehicle "needs most of a space launcher". **That phrase can be made a number.**

Specific energy goes as the square of speed, so the mission needs **69 to 87 percent of the energy of
reaching orbit**. The rocket equation turns that into a mass ratio of **10.8** at a solid-propellant
specific impulse, meaning **near ten tonnes of stack for a 900 kilogram glider** before losses.

**The cheap alternative to an intercontinental ballistic missile needs most of one.**

---

## A Contradiction in the Published Figures, Found by Arithmetic

**The Common Aero Vehicle payload is quoted as 1,000 pounds and the Hypersonic Technology Vehicle mass as
900 kilograms.** That is a payload fraction of **50 percent**, which is not credible for a hypersonic
glider.

**The two figures cannot describe the same vehicle.** Either the payload belongs to a larger design than
the one that flew, or the mass belongs to a stripped demonstrator carrying nothing. The record does not
say which, and the article now states which figure it uses where.

---

## Also Added, and One Defect Repaired

The inversion that generates the required-ratio table, the Mach conversion behind it, the transcendental
equation whose root is the Küchemann crossover, the linearity of range in the ratio, the weight, the
exponential atmosphere converting density to the 61.2 kilometre corridor altitude, and the implied lift
coefficient.

**One equation had absorbed the following prose onto its own source line** and was repaired, so every
display equation again occupies exactly one line.

---

## The First Documentation-Poor Article in the Series

**A297 names the class and no article had used it.** No specifications for this vehicle have ever been
released, so the section order is the full one, the sections are short, and **the statement of what is
unknown carries the weight a specification table would otherwise carry.**

**The keystone is that classification hides the design and not the physics.**

---

## What the Public Numbers Force

**A published range of 9,000 nautical miles and the equilibrium glide relation fix the required lift to
drag ratio at each entry speed.** The Küchemann barrier then refuses most of that table.

- **Below Mach 22.2 the mission is unavailable to any shape.** The glider had to be boosted to at least
  **83 percent of orbital speed.**
- **At the 2.6 ratio actually estimated for the vehicle that flew, the figure is 93 percent**, which is
  very nearly a launch to orbit, and is the quantitative version of the observation that boost-glide and
  space launch are the same problem wearing different labels.

**The model was validated before it was used to argue.** Feeding the published 2.6 and Mach 20 into the
range relation recovers **6,746 km against a planned 7,700**, or **88 percent**, from two published
numbers and nothing else. That is good agreement for a two-parameter model and not good enough to size
hardware, and the article says so.

---

## The Corridor Is Where the Vehicle Breaks

**A glider at this speed must fly low enough for the air to hold it up and high enough for the air not to
destroy it.** At the corridor point a 50 millimetre leading edge reaches **2,921 K**, against a published
design surface temperature of **2,203 K**.

**Holding the design value needs an edge radius of 0.48 metres on a vehicle four metres long**, and that
much bluntness collapses the lift to drag ratio the range depends on. **Five of the nine swept
combinations exceed the design temperature**, and the two quantities swept are exactly the two the record
withholds.

**The design wants a sharp edge for range and a blunt edge for survival and cannot have both.**

---

## The Failure Report Confirms It in Its Own Terms

Both flights ended near the **ninth minute** of a thirty minute glide. The engineering review board found
**unexpected aeroshell degradation**, skin peeling beyond expectation, and roll upsets beyond the
vehicle's control authority.

**It also found that the aerodynamic design was validated and that what the flight taught concerned the
thermal material properties.** The shape was never the problem. The edge was, **and the arithmetic said so
before the vehicle flew.**

---

## The Title May Be Wrong

**The X-41A was allocated in late 1997 or early 1998, years before the Common Aero Vehicle programme
existed**, was never used again in any official announcement, and the authoritative survey explicitly
doubts that it ever applied to this vehicle. **The article uses the pairing because the public record
does, and says plainly that it may be wrong.** That connects directly to the X-39 article two before it.

---

## Three Homonym Families, and a Pattern in How They Were Found

Reading the samples caught **the underwater glider**, which shares glide, trajectory, range and vehicle
with a hypersonic glider and nothing else, and **the block-glide landslide**, which also collects "front
range".

**A third survived the samples.** A condensed-matter physics identifier in a routine URL check led to the
**nanofluid stagnation-point flow** literature, a large applied-mathematical field about flow over
stretching sheets that shares "stagnation point" and "heat transfer" with reentry aerothermodynamics and
shares no physics. **97 records, 2.2 percent of the corpus, removed.**

**That is the third consecutive article on which a publisher-prefix check has beaten the random sample.**
It is now part of the routine rather than a lucky catch.

---

## Verification

- **10,179 lines, 30 display equations, 4,654 reference definitions, 91,036 words**, of which 5,213 are
  author prose.
- **23 of 23 swept URLs resolve**, being the 8 curated and a 15-record harvested sample. No anchor appears
  twice. Structural conformance matches A335 and A337 heading for heading, and acronyms are clean.
- `python3 _verify.py` **0 errors, 0 warnings**. `./_check.sh --drafts` clean at **511 pages**.
- Reference integrity **4,375 used against 4,375 defined**, zero undefined, zero orphaned, zero duplicates.
- Every display equation on one source line. Rendered body clean on every marker check, both tables
  rendering, MathJax balanced. Navigation reads **Part 42 of 42**.
- **8 of 8 curated URLs at 200**, a sample of 15 harvested identifiers resolving 15 of 15.
- `tmp/a338/verify.py` all pass, sharing no code with the draft.
- Diction **0 constructions above the corpus maximum** against 300 peers.

---

## Outstanding

**It is committed and pushed, and it is not published**, which is what you asked for.

**Publishing it alone would fail the build.** A338 cites forty-one siblings through `post_url` and none
exists in `_posts/`, so **the set publishes in order or together**. Forty-two of seventy-two are drafted
and **publication has never been authorised**.

**The X-Planes set remains unpublished and unauthorised.** Forty-two of seventy-two drafted, forty-one of
them citing a sibling through `post_url` with no target in `_posts/`, so **the set publishes in order or
together**.

**One item is still owed from outside this repository**, being A369's factor-of-roughly-thirty claim.

---

## From A337, the Boeing X-40, Which Is Complete and Pushed


## The Survey Had a Subject at Zero That the Article Displays

**I audited the survey against the article's own load-bearing subjects and two came back thin.**

**Relative density measured zero.** The article displays it as the canonical form of the similarity
condition, derives the vehicle's value from it, and uses it as the independent cross-check on the central
finding. **The survey held nothing on it**, because the first harvest never asked. That is the A335
pattern exactly.

**Runway excursion stood at six**, against a closing argument that rests on the X-37A overrunning a runway.

**A supplementary harvest of 3,184 records closed both**, taking relative density and scaling laws from
**0 to 104** and runway excursion from **6 to 176**.

---

## Read This, Because My Supplementary Anchors Were Bad

**`relative density` is a soil mechanics term.** It is the standard measure of how densely a granular soil
is packed, and it is everywhere in geotechnical engineering. **`moment of inertia` names a nuclear physics
model** of rotational bands in odd-mass nuclei, and separately a reinforced concrete section property.

**Forty-four records across those families reached the corpus and were removed**, which was 10.6 percent
of the supplementary set. **The first harvest was audited by reading samples and the supplementary one
initially was not**, and that is the whole explanation. The gap is recorded in the article rather than
smoothed over.

**I found them by checking an out-of-place publisher prefix in a routine URL sample**, a Physical Review D
identifier sitting in an aerospace reference list. That is the second time on this article that a prefix
check has beaten the random sample.

---

## A Merge Routine Corrupted Seven Cluster Counts

**The routine that updated a cluster's record count used a non-greedy pattern that reached past its
intended heading**, so two clusters were given counts belonging to their neighbours. **The stated totals
disagreed with the data by as much as 173 records.**

**The display sizes exposed it**, because two clusters were left showing 14 entries where the prose claimed
25. **All nine cluster blocks were then rebuilt from the harvest files rather than patched**, and every
count in the survey is now derived rather than edited.

---

## The Curated Set Had One Primary Source in Twelve

**Eleven reference works and a single press release is an indefensible base for an article whose keystone
is a scaling law**, and that is what the first two passes left. I harvested **127 NASA technical reports**
and selected **28**. The curated set is now 40 sources and its **primary share went from 8 percent to
70 percent**.

---

## One Primary Changed a Claim Rather Than Supporting One

**The draft said the instrumentation suite is not described anywhere in the accessible record. That was
wrong, and it was written without searching the technical reports server.**

A paper to the twentieth Digital Avionics Conference names the **Space Integrated Global Positioning
System and Inertial Navigation System**, reports its testing during the X-40A approach and landing
campaign against differential satellite navigation, and states two objectives: demonstrating performance
sufficient for the X-37 requirement, and **reducing the risk of integrating that specific unit into that
specific vehicle**.

**That is a hardware qualification and not a scaling experiment.** It is this article's thesis stated by
the people who ran the programme, and it is now the strongest single piece of support the argument has.

---

## Three Uncited Claims Now Rest on Primary Sources

- **The attainable lift to drag ratio of 3 to 4**, which the article uses to say the X-40A flew at half
  its capability, now rests on flight-determined lift and drag for seven lifting-body and wing-body
  reentry configurations rather than on my impression.
- **The touchdown sink rate** behind the landing gear calculation now rests on a statistical analysis of
  landing contact conditions across three lifting-body research vehicles.
- **The low lift-to-drag approach regime** now rests on the 1959 flight investigations that opened it and
  the later work that extended the range downward.

**The Shuttle Approach and Landing Test programme is cited as the methodological precedent** rather than
asserted, and the 22 percent F/A-18E/F drop model supplies the quantitative comparison, sitting near a
tenth of full-scale Reynolds number where the X-40A sat at 69 percent.

---

## Read This, Because I Reproduced a Defect This Corpus Has Shipped Before

**Two of my hand-assigned anchors already existed as harvested records**, because both derive from a
surname and a year, and merging them overwrote the harvested entries **without erroring**.

**Nothing showed it except an off-by-two in the harvested count.** One collision was the same work
registered twice, once by a conference publisher and once by the reports server, and it is now a single
entry. **The other was two different papers by the same author in the same year**, and the harvested
record was restored under its own anchor with the primary given a suffixed one.

**That is the A371 lesson repeated**, that an anchor derived from author and year is not unique and a
merge assuming it is will repoint a citation silently.

**A mis-mapped identifier was also caught before it shipped.** A hand-chosen record for the X-37 dynamics
paper resolved to an unrelated X-33 navigation paper. Every selected anchor was afterwards checked against
its record's first author.

---

## The Best Addition Says What Eight Flights Actually Prove

**The draft said eight clean landings establish that the concept is sound, and never said what eight
trials bound.** The standard one-sided limit for zero failures in $n$ trials answers it.

**For eight flights the failure rate is bounded only below 31.2 percent at 95 percent confidence.** That
is a statement about sample size rather than about the vehicle, and it is the precise sense in which the
programme established **tractability and not reliability**. A vehicle returning from orbit needs a figure
orders of magnitude smaller, and no drop-test campaign of affordable length reaches it.

**The article now says both halves.** The flights did establish that the concept, the sensors and the
integration work at all, which is necessary and different.

---

## The Canonical Similarity Parameter Was Missing

**Free-flight similarity is normally written as a match of relative density**, comparing the vehicle's
mass to the mass of air in a volume set by its own dimensions, and the draft never used it. Computing it
gives **19.7 against 37.9, a ratio of 0.519**.

**Two independent formulations therefore land on the same factor of two.** The wing loading route and the
relative density route share only the published masses, so their agreement is the strongest internal
check the finding has.

---

## Three Claims That Were Asserted Are Now Derived

**The inertia claim.** The draft said the vehicle had "roughly half the inertia for a given size" in
prose. Similarity requires an inertia ratio of **0.285** against an actual **0.143**, and the angular
acceleration for a given control moment is therefore **1.99 times** the similar value. Combined with the
13 percent rate increase from geometry, the plant was appreciably harder to fly than the full-scale case.

**The energy accounting.** Of the specific energy available at release, **18.9 percent was carried as
speed and 81.1 percent was spent against drag**. A drag-free fall from the same height would have arrived
at 984 ft/s against the 428 actually reached, which is the quantitative statement that this was a
drag-dominated descent rather than an acceleration.

**The landing accuracy.** Seven feet of centreline error means little without the range it was achieved
over. Over a 28,353 foot ground track it is **0.85 arcmin, or 0.025 percent of the distance flown.**

---

## A Verifier That Shares No Code With the Draft

`tmp/a337/verify.py` recomputes **55 results** from the published imperial figures, converting them itself
rather than taking the draft's metric values. **All pass.** That is the A335 lesson, that a verifier
sharing an input with the thing it checks does not check that input.

---

## A Formulaic Tic, Found by the Instrument and Not by Reading

**Seven `worth` constructions were present and five were meta-textual**, being me announcing what the
article was about to show rather than saying anything. Varying those five across a rotation and keeping
the two substantive uses took diction from **1 construction above the corpus maximum to 0**.

**Three equation blocks spanned multiple source lines** and were collapsed, so every display equation now
occupies exactly one.

---

## The Finding, Which Contradicts How the Vehicle Is Always Described

**The X-40A is called a subscale model of the X-37 almost everywhere, and by the test that matters it was
not one.**

Its geometric ratio to the X-37 is **0.778**, the mean of the published length ratio of 0.752 and span
ratio of 0.804. **Its mass ratio is 0.618.** Froude similarity at that geometric scale demands a weight of
**5,186 lb** and the vehicle weighed about **2,600 lb**.

**It flew at 50 percent of its dynamically similar mass**, so the Froude number was never matched, and
therefore the speeds, the times and the trajectory never scaled. **No quantitative aerodynamic result from
those eight flights transfers to the vehicle it was built to inform.**

**This is not a criticism and the article says so.** The X-40A carried no propulsion, no thermal
protection, no payload and no orbital subsystems, and those absent systems are exactly the mass the full
vehicle would carry. Ballasting a one million dollar test article to preserve a similarity nobody intended
to exploit would have been a strange use of the money.

---

## The Mass Deficit Is the Programme's Best Argument

**Angular rates scale as the inverse square root of the length ratio**, so at this scale the model's rates
are **13 percent higher** than the full-scale vehicle's. The halved inertia makes the plant quicker still.

**The control system was therefore exercised against something harder to fly than the aircraft it was
written for**, and it landed the vehicle eight times out of eight, once within 7 feet of the centreline.
**The subscale test was conservative in the one dimension that mattered**, which is the opposite of the
usual situation with scale models.

---

## The Disputed Scale Figure Resolves

**Four sources give four numbers for the best documented parameter of the aircraft.** Boeing's own press
release says 90 percent, the space agency says 80, a contemporaneous report of the second free flight says
85, and a reference encyclopaedia hedges at 80 to 90.

**The 90 percent figure is correct about a vehicle that was never built.** The test bed was 90 percent of
the **Space Maneuver Vehicle**, the operational concept, and the X-37 that everybody now compares it to
was a later and larger vehicle. **A ratio quoted without its denominator produced a twelve point
disagreement in the literature.**

**Nothing depends on which figure is adopted.** The article tabulates the Reynolds, time and angular-rate
ratios across the whole disputed range and no conclusion moves.

---

## Numbers Recovered From Figures No Source Combines

**No source states the flight path angle.** Release at 15,050 feet, a descent of about 75 seconds and a
speed of 428 feet per second give a mean sink of 200.7 ft/s, a path angle of **28.0 degrees**, an
effective lift to drag ratio of **1.88** and a ground range of **4.67 nautical miles**. That is a steep
energy-management descent rather than a best-glide profile, which is what a vehicle does when it is aiming
at a fixed point.

**No reference area is published anywhere**, so the article bounds it instead. The steady glide fixes the
product of area and lift coefficient at **13.42 square feet** and the split between them is stated as an
estimate rather than a measurement.

---

## What Did Not Transfer, With Evidence

**The X-37A overran the runway and was damaged on its first free glide flight on 7 April 2006.** The same
programme lineage, flying a vehicle 120 percent the size built on the X-40A's own outer mould line, failed
to stop on the runway. **That is the clearest available evidence that the X-40A results did not transfer
quantitatively.**

**The most durable output was the shape.** A one million dollar test article defined the outer mould line
of a spacecraft that has since spent years in orbit, which is a return this series has no other example of.

---

## Read This Part, About the Survey Gate

**Reading the audit samples found two homonym families that no count would have shown.** The **runway is a
piece of apparatus in animal behaviour research**, a straight alley a rat runs down for reinforcement, and
one such record had been admitted. **Disaster risk reduction** shares both words with flight risk
reduction and nothing else.

**A third family was found by checking an out-of-place publisher prefix rather than by the random sample.**
A clinical-psychology identifier in the reference list led to the discovery that **subscale is a
psychometrics term**, a subscale being a component of a test instrument, so the phrase matches
questionnaire-validation papers exactly. One had reached the corpus and was removed.

**The measured residual noise is reported as a floor and not a ceiling**, since it counts only what two
samples and one prefix check happened to surface. The article claims a clean corpus nowhere.

**The A336 lookahead defect cannot recur here.** Each qualifier part is wrapped in a non-capturing group,
so an alternation cannot escape its lookahead and turn a conjunction into a disjunction of bare words.

---

## Verification

- `python3 _verify.py` **0 errors, 0 warnings** across 300 posts.
- `./_check.sh --drafts` **clean end to end**, 510 pages, 210 carrying display math, no findings.
- Reference integrity **4,547 used against 4,547 defined**, zero undefined, zero orphaned, zero duplicates.
- **Every display equation occupies exactly one source line.** All definition groups and visible lists
  sorted.
- Rendered body carries **zero raw display-math delimiters, zero unresolved reference syntax, zero
  unrendered Liquid and zero empty list items**, with MathJax delimiters balanced. Navigation reads
  **Part 41 of 41**.
- **All 12 curated URLs resolve at 200.** A sample of 15 harvested identifiers resolves 15 of 15, the 403
  responses being AIAA, MDPI and Bentham, all documented publisher behaviour.
- Diction **0 constructions above the corpus maximum** against 300 peers.
- **10,681 lines, 64 display equations, 4,735 reference definitions, 97,714 words**, of which 7,903 are
  author prose.
- **All 12 curated URLs and all 28 NASA identifiers resolve 200 of 200**, and a sample of 15 harvested
  identifiers resolves 15 of 15. No anchor appears twice in the reference list.
- Contemporary coverage **47.3 percent from 2015 or later, 29.2 percent from 2020 or later**.
- Structural conformance matches A335 heading for heading. Acronyms clean, the only flagged tokens being
  `UH` and `CH` from model designations, which the checklist exempts. Every display equation occupies exactly one source line and the rendered page carries 64
  display math blocks with balanced delimiters.
- `tmp/a337/verify.py` **55 of 55**, sharing no code with the draft.

---

## Outstanding

**It is committed and pushed, and it is not published**, which is what you asked for.

**Publishing it alone would fail the build.** A337 cites forty siblings through `post_url` and none exists
in `_posts/`, so **the set publishes in order or together**. Forty-one of seventy-two are drafted and
**publication has never been authorised**.

**The X-Planes set remains unpublished and unauthorised.** Forty-one of seventy-two drafted, forty of them
citing a sibling through `post_url` with no target in `_posts/`, so **the set publishes in order or
together**.

**One item is still owed from outside this repository**, being A369's factor-of-roughly-thirty claim,
which rests on the Keleusma decision register.
