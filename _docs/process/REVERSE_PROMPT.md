## Last Updated

**Date**: 2026-08-13
**Task**: **A337, X-Planes, Boeing X-40. Publication review complete.** Committed and **PUSHED**.
**Not published.** All four passes are done.

---

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
