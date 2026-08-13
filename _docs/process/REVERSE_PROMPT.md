## Last Updated

**Date**: 2026-08-13
**Task**: **A337, X-Planes, Boeing X-40. Equation-density review complete.** Committed, **not pushed**,
per the four-pass rhythm. **Not published.**

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
- **10,190 lines, 64 display equations, 4,547 reference definitions, 92,833 words**, of which 6,620 are
  author prose. Every display equation occupies exactly one source line and the rendered page carries 64
  display math blocks with balanced delimiters.
- `tmp/a337/verify.py` **55 of 55**, sharing no code with the draft.

---

## Outstanding

**It is committed and not pushed**, which is what these passes call for. The remaining two are the
primary-reference review and the publication review.

**The X-Planes set remains unpublished and unauthorised.** Forty-one of seventy-two drafted, forty of them
citing a sibling through `post_url` with no target in `_posts/`, so **the set publishes in order or
together**.

**One item is still owed from outside this repository**, being A369's factor-of-roughly-thirty claim,
which rests on the Keleusma decision register.
