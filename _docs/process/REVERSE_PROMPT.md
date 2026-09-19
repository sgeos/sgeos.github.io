# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

## Last Updated

**Date**: 2026-09-18
**Task**: **A360, X-Planes: ABL Space Systems X-63, primary-reference review. The third of
four.** Committed and **NOT pushed**. **Not published**, and publication of the series has never been
authorised. **Sixty-four of seventy-two drafted, eight remain.**

**A CONCURRENT SESSION IS WORKING IN THIS TREE AND HAS COMMITTED THREE TIMES.** Its A374 commits
sit on `master` unpushed, below this article's. **Its draft is modified again and is left
unstaged.** Only this article's own paths were staged. Its report is preserved below this one
rather than overwritten, because the file has two writers whatever its design says.

---

## A360, Primary-Reference Review

**REPORT PRIMARIES 984 TO 3,748, FROM 10.4 PERCENT TO 30.6.** Research records 9,467 to
12,231, reference definitions 9,609 to 12,395, lines 20,167 to 25,796, words 117,925 to
159,118. **Every one of the fourteen clusters rose**, the range moving from 3.7 to 23.3
percent up to 14.8 to 49.0.

### The Reports Server Was Being Read One Page Deep, by Every Article in This Corpus

**THIS IS THE FINDING OF THE PASS AND IT IS NOT ABOUT THIS ARTICLE.** `fetch.ntrs_search`
passed its page specification as a single encoded object. **That server clamps such a
request to ten records AND SILENTLY IGNORES THE OFFSET INSIDE IT**, so six requests at six
different offsets return the identical ten records, which is what the probe found.
Passing the size and the offset as separate bracketed parameters is honoured.

**The question `plug nozzle` matches 242 records. The old call returned 10. The corrected
one returns all 242 with no duplicates.** The fourth sweep's reports-server return is
**10,160 records against 606 from the first three sweeps combined**, a factor of sixteen
and a half, and it is the direct cause of the primary fraction tripling.

**EVERY PRIMARY-REFERENCE PASS IN THIS SERIES HAS COMPLAINED THAT THE REPORTS FRACTION IS
THIN.** A359 said so, and this article's own drafting pass wrote that the imbalance was
`the third pass's problem arriving early`. **Part of that complaint was an instrument
reading its first page.** The fix is a parameter spelling, it is held by a test that runs
offline against a fake transport, and it is in the shared library where every later
article inherits it.

**AND THE SERVER REPORTS ITS OWN TOTAL, WHICH NOTHING WAS READING.** `fetch.ntrs_total` is
added, and with it the coverage of a sweep stops being an assumption. Across 89 questions
the server reported **32,488 matching records and returned 14,929**, which is 46.0 percent.
**That average hides a clean split.** Sixty-eight questions were taken to the bottom,
holding 7,798 between them and returning all 7,798. **Twenty-one hit this article's own
walk limit of 400 rather than the server's**, and **every one of the 17,559 records not
taken belongs to those twenty-one**, which are the broad organisational questions such as
`Marshall Space Flight Center engine`, holding 5,402 on its own. **The focused half of the
sweep is complete and the truncation is entirely of this article's choosing.**

**THE SAME MEASUREMENT CANNOT BE MADE OF THE BIBLIOGRAPHIC INDEX AND THE ARTICLE SAYS SO.**
That index performs a ranked retrieval rather than a boolean match, and asking it how many
records match `rocket nozzle performance` returns 2,406,511, which is not a count of
anything. **A coverage figure is worth quoting only where the denominator is a match
count.**

### A Read Primary Withdrew This Article's Sharpest Claim

**THE DRAFTING PASS SAID THE TRAJECTORY-OPTIMAL NOZZLE CANNOT BE BUILT.** That rested on a
separation threshold of four tenths taken from secondary accounts, and the pass said
plainly that it had not read the correlations.

**NASA Technical Paper 1207 has now been read in full and it changes three things.**

**It gives the attribution the drafting pass struck.** The four tenths belongs to
Summerfield, Foster and Swan in the Journal of Jet Propulsion for 1954, and the paper adds
that the value `is still quoted today ... although more recent studies have shown it to be
inadequate`. **The drafting pass went looking for exactly that attribution, found a 1953
paper by Scheller and Bierlein in the index instead, and removed the name rather than
assert it.** Removing it was right on the evidence then. **The paper that corrects it also
explains the confusion**, because Scheller and Bierlein are the early study that conflicted
with the others.

**It says the four tenths is for the wrong kind of nozzle.** Contoured nozzles, `the case
of most interest for modern nozzle design`, follow a different correlation, and the paper
fits a second-order curve to them between separation Mach 2.4 and 4.5.

**And applying that curve to this article's own nozzles takes the claim back.** The
criterion is local, so the nozzle is walked from throat to exit. **The trajectory optimum
separates only below about 3.3 to 3.7 megapascal of chamber pressure**, and above that it
runs attached with between 6.6 and 12.7 percent of margin in area ratio. **The chamber
pressure recovered from this engine's own instability frequency, 2.6 to 8.7 megapascal,
straddles that crossover.** So the honest claim is that the optimum sits pressed against
the limit rather than beyond it, which is weaker, better supported and more interesting.

**THE DRAFTING PASS'S ERROR HAS A NAME.** It used the more conservative of two criteria and
the conservative one is the one the primary calls inadequate. **A band taken on report is
not a band**, because a range quoted without its provenance hides which end belongs to
which kind of nozzle. The opening, the section, the reflection and the conclusion were all
corrected.

### Two Further Corrections the Checks Forced Out of My Own New Prose

**THE CRITERION AT MACH 3 IS 0.340 AND I WROTE 0.342**, which was arithmetic done in my
head and caught by a check that evaluated the polynomial.

**AND I SAID THE CONTOURED CORRELATION TOLERATES ROUGHLY TWICE THE OVER-EXPANSION, WHICH IS
TRUE NOWHERE.** It crosses the flat four tenths at separation Mach 2.59 and is **stricter
below that**, reaching 0.433 at the bottom of its fitted range. The old rule is 1.74 times
as restrictive at the top of the range and slightly less restrictive at the bottom. **A
nozzle of the area ratios this article discusses separates well above Mach 3, so the
permissive end applies here, but stating it without the crossing would have repeated the
error the section is about.**

### Twenty-Two Curated Primaries, Three Read in Full

**NASA SP-8120, the design-criteria monograph for liquid rocket engine nozzles**, which
supplies the J-2 case history the article was describing in the abstract. That engine was
given a deliberately nonoptimum contour to raise its exit pressure, suffered unsteady
asymmetric separation from a wall-pressure minimum, lost thrust chambers to the loads, and
ended up with a bolt-on diffuser and restraining arms from the test stand to the nozzle
skirt. **It also states, in the design community's own voice, that separation predictions
`are used only as a guide`**, which is the qualification this article makes independently.

**NASA Technical Paper 1207**, described above.

**The 1976 United States Standard Atmosphere.** **The drafting pass implemented that
atmosphere and cited an encyclopedia for it**, which is precisely the gap a
primary-reference pass exists to close.

The remaining nineteen are the four Lewis reports of 1954 to 1959 that founded the
plug-nozzle literature, the design monographs for turbopumps and combustion chambers, the
standard design text, the four LASRE reports covering the only aerospike that ever left
the ground, and the five X-33 reports covering the largest one ever built.

### Which Clusters Rose, and Why the Keystone Rose Least

**THE KEYSTONE WENT FROM 8.7 PERCENT TO 16.8, WHICH IS A NEAR DOUBLING AND STILL BELOW THE
ARTICLE'S OWN AVERAGE OF 30.6.** The largest gains were general rocket propulsion at plus
29.8 points, manufacture at plus 27.0 and named vehicles at plus 23.0. The smallest was the
wake cluster at plus 3.3, which was already among the richest.

**AND A359'S TEST SAYS THE REMAINING THINNESS IS A FACT ABOUT THE DISCIPLINE.** The three
thinnest clusters are exactly the three in which one publisher's conference proceedings
hold the largest share, being altitude compensation at 34 percent, the wake at 49 and the
fixed-nozzle limits at 51. **Half of the wake literature and half of the limits literature
is one conference series.** The general nozzle cluster beside them is 26 percent that
publisher and 29 percent reports, and general rocket propulsion is 29 and 49. **The
specifically aerospike subject is a conference literature and the rocket propulsion around
it is a report literature.**

### A Third Instance of the Cached-Measurement Defect, Caught Before It Bit

The family-cost cache added in the drafting pass was fingerprinted on the gate's patterns.
**The fourth sweep changed the pool rather than the gate**, which would have served the old
counts against new records. The fingerprint now covers the pool size as well. **That is the
trap this article documented two passes ago, one level up, and it was caught by looking for
it rather than by anything failing.**

### Verification

`_verify.py` **0 errors and 0 warnings** across 301 posts. Library tests **120 of 120**,
one added holding both halves of the pagination repair. **Article verifier 652 checks and 0
failures**, and **the relation verifier 246 checks and 0 failures**. **The symbol check
passes in both directions** at 73 declared symbols, 46 display equations and 187 inline
expressions. Diction **0 constructions above the corpus maximum**. **Zero contractions,
parentheses, colons, semicolons or dashes outside verbatim quotations.** The stub-isolated
production build succeeded in **19.2 seconds** with no Liquid error against checksum-matched
bytes, **the rendered audit reports no findings across 543 pages**, source and rendered
display-equation counts agree at **46**, the inline count at **187 balanced pairs**, and the
page carries zero raw dollar pairs, zero unresolved reference brackets and zero unrendered
Liquid.

---

## A360, Equation-Density Review

**DISPLAY EQUATIONS 15 TO 45, INLINE EXPRESSIONS 70 TO 181, LINES 19,915 TO 20,167, WORDS
114,090 TO 117,925.** A symbol table of **71 entries** is added and checked in both
directions.

**THE ARTICLE PERFORMED A WHOLE THERMODYNAMIC CALCULATION AND SHOWED NONE OF ITS
MACHINERY.** The drafting pass used the thrust coefficient in nine places and **never
defined it**. It used the area ratio without relating it to the throat, the isentropic
relations without writing them, the Vandenkerckhove constant not at all, and it quoted a
gain in percent without saying that the quantity is a ratio of two integrals. **The
throat area did not appear anywhere in the article.** That is the density gap, and it was
found by listing the symbols the mathematics uses and asking which had been introduced.

### What Was Added, and Which Additions Changed Something

**THE DEFINITIONAL LAYER.** The thrust coefficient and area ratio, the affine law in
coefficients, the Vandenkerckhove constant, the area-Mach and pressure-ratio relations,
the vacuum coefficient, and the split of specific impulse into characteristic velocity
times thrust coefficient. **That last one earns its place**, because it is why an article
about a vehicle with no published engine can quote a performance figure at all. The
characteristic velocity carries the propellant and the chamber, the thrust coefficient
carries the nozzle and the atmosphere, and **a claim about altitude compensation is a claim
about the second factor only**.

**THE STRUCTURE THE KEYSTONE ALREADY HAD AND DID NOT STATE.** The Fenchel-Young inequality,
which says exactly that every fixed nozzle lies at or below the envelope with equality only
at its own design point. The inverse transform, which says the family of bells and the
envelope carry the same information, so **an aerospike is a different point on a structure
that was already there rather than a new capability**. The envelope theorem and the
convexity, the second of which **has a physical reason rather than a formal one**, since a
higher ambient pressure selects a shorter nozzle, so the exit area falls as the ambient
rises and its negative is non-negative. **The envelope bends upward because the optimal
nozzle shrinks as the air thickens.**

**AND THE BREGMAN LOSS AS AN INTEGRAL**, which is the form that can be read off a picture.
The loss is the area between a horizontal line at the fitted exit area and the curve of the
area the envelope would have chosen. **The order of that subtraction was settled by a check
and not by inspection.** Written the other way round the expression is the negative of the
loss, and the first version of the numerical test was written that way, which is how the
sign was fixed before the relation reached the page.

**THE ATMOSPHERE, WHICH THE DRAFTING PASS USED AND NEVER SHOWED.** Both barometric forms,
the isothermal one being the limit of the other as the lapse rate goes to zero, the scale
height, and **a closed form for the pressure-time integral that says something the numbers
do not**. For an isothermal atmosphere climbed at a constant rate the integral saturates at
sea-level pressure times scale height over climb rate. **A rocket does not pay for the
atmosphere by the second. It pays once, and the bill is set by how fast it left.**

### One New Substantive Result

**THE EQUIVALENT GIMBAL ANGLE OF DIFFERENTIAL THROTTLING IS 0.91 DEGREES.** Converting the
ring's directional-average authority into the quantity a conventional stage would quote
gives a deflection whose sine is the throttle depth over pi times the ring radius over the
moment arm. At a throttle range of two tenths and a radius a quarter of the arm, that is
**under one degree**. **Differential throttling is adequate for trim and marginal for
anything faster**, and the article now says so with a number rather than leaving the reader
to assume the technique is a substitute for a gimbal. **The drafting pass had the authority
figure and never converted it into a unit anyone thinks in.**

### Three Defects in My Own New Work

**BOTH SCALE HEIGHTS ROUND TO 8,435 AND I PRINTED THEM AS 8,435 AND 8,434.** The sea-level
value is 8,434.9 metres and the isothermal value 8,434.5, a gap of four tenths of a metre
which is the lapse rate appearing in the fourth figure. **Rounding to whole metres makes
two numbers that agree look as though they disagree**, which is the opposite of what the
sentence was for. Caught by a check that compared the two roundings rather than the two
values.

**THE SYMBOL SCANNER'S PASS ORDER WAS WRONG THREE TIMES BEFORE IT WAS RIGHT.** Stripping
operators first breaks every declared name containing a macro, so `C_{F,\mathrm{vac}}`
stopped matching and reported a bare undeclared `C`. Stripping declared symbols first
breaks the operators instead, because a single-letter symbol such as `c` sits inside
`\frac`. **The only order in which no pass destroys another's input** is compound names
first as placeholders, macros second, bare letters last. Environment names then had to be
removed with their braces, because `\begin{cases}` leaves `{cases}` behind as three more
undeclared letters.

**AND ONE CONSTRUCTION WENT OVER THE CORPUS MAXIMUM BECAUSE OF THIS PASS.** `the second is`
reached six uses against a peer maximum of 0.34 per thousand, three of them added here by
the habit of writing `the first is` and `the second is` when introducing a pair of
relations. Three were varied and the rate is back under the maximum.

### Two Things Deliberately Not Added

**THE BASE PRESSURE OF A TRUNCATED PLUG IS NOT COMPUTED AND NOW SAYS SO IN AN EQUATION.**
The thrust splits exactly into the force on the wetted surface plus the base pressure times
the base area, and that decomposition is worth writing because it names the term this
article cannot evaluate. **A one-dimensional isentropic model does not produce a
recirculating turbulent base pressure**, so the regimes are classified by which quantity
sets that pressure and the magnitude is left to the literature.

**AND THE ASCENT PROFILE IS A GUESS WITH AN EXPONENT, WHICH THE EQUATION NOW SHOWS.** The
family is stated as a power law with the exponent swept from 1.5 to 3.0 rather than
described in prose, so a reader can see that two published points and a zero initial rate
do not determine a trajectory and that the spread is the honest measure of what that costs.

### Verification

`_verify.py` **0 errors and 0 warnings** across 301 posts. Library tests **119 of 119**.
**Article verifier 626 checks and 0 failures.** **A separate verifier for the new relations
runs 246 checks and 0 failures**, each relation evaluated against an independent route
rather than against the code that produced it. **The symbol check passes in both
directions**, every symbol in the mathematics declared and every declaration used, with the
macro allowlist confirming that all thirty macros are base TeX. Diction **0 constructions
above the corpus maximum** after three were varied. **Zero contractions, parentheses,
colons, semicolons or dashes outside verbatim quotations.** The stub-isolated production
build succeeded in **15.4 seconds** with no Liquid error against checksum-matched bytes,
**the rendered audit reports no findings across 543 pages**, and **source and rendered
display-equation counts agree at 45** with the inline count at **181 balanced pairs**, zero
raw dollar pairs, zero unresolved reference brackets and zero unrendered Liquid.

**AND THE BUILD WAS RUN TWICE FOR THE RIGHT REASON.** The first run finished against bytes
that three diction edits had already superseded, and a build of superseded bytes verifies
nothing about what ships, which is A345's lesson and which the frozen checksum made visible
immediately.

---

## A360, ABL Space Systems X-63, Drafting Pass

**TWO X NUMBERS WERE ISSUED ON ONE DAY WITH ONE DESCRIPTION AND THE DESCRIPTION IS IDENTICAL TO
THE BYTE.** The X-63A and the X-64A carry the same allocation date, the same sponsor cell, the
same engines cell and the same 101 characters. **Eleven descriptions repeat in the 539-row
register and ten of those repeats are munitions, targets and a ground station.** This pair is
the eleventh and the only duplicate among the 31 X rows.

**THE SPACE FORCE APPEARS IN THE X-PLANE REGISTER EXACTLY TWICE AND BOTH TIMES ARE HERE.** No
other row reads `USAF/USSF`. **And `1 rocket engine` appears in exactly two of 539 rows**, also
these, against an engines column that otherwise names a model. The X-60A, which A357 established
is a rocket, has an empty engines cell.

### A Correction to This Series' Own Arithmetic, Which Is the Most Important Thing Here

**THE REGISTER'S OFFICIALITY MARKUP HAS THREE STATES AND THE LAST TWO ARTICLES EACH SUMMARISED IT
IN TWO NUMBERS.** Recomputed from the saved page and confirmed by an independent re-parse of the
markup, the split is **436 official, 86 wholly unofficial and 17 partly unofficial** across the
register, and **21, 9 and 1 across the 31 X rows**.

**A358 gave the register-wide figures exactly right** as 86 and a further 17. It then gave the
X-row figures as 21 official and 9 not, **which accounts for 30 of 31 rows** because the partly
marked one has nowhere to go.

**A359 closed that sum by raising the official count to 22**, which places the partly marked row
on the official side. **That is the one side it cannot be on**, because the marking is the
compiler's statement that part of its wording is a reconstruction. A359's sentence reads `22 carry
official wording and 9 do not`.

**NEITHER ARTICLE IS PUBLISHED AND BOTH ARE PUSHED, SO THIS IS A DECISION RATHER THAN AN EDIT.**
A360 states the correct three-way split and says plainly that the previous two articles carried a
two-number version of it. **I have not touched A358 or A359.** The pilot may prefer that A359's
sentence be corrected at its source, in which case the change is one clause, and A358's needs a
third number rather than a different one.

### The Mathematics, Which Is an Identity That Removes the Vehicle

**THE INCREMENTAL VACUUM THRUST BOUGHT BY AN INCREMENT OF EXIT AREA IS THE EXIT PRESSURE ACTING ON
THAT INCREMENT, EXACTLY.** One line from the one-dimensional momentum equation. **So ambient
pressure is the variable conjugate to exit area**, the ideal altitude-compensating nozzle's thrust
curve is the Legendre transform of the vacuum thrust, every fixed nozzle is one of its tangent
lines, and **the loss of a fixed nozzle is a Bregman divergence** rather than being analogous to
one. The matched-expansion condition every text states separately is the transform's first-order
condition.

**AND THE DESIGN RULE THAT FALLS OUT WAS NOT ANTICIPATED.** The optimal fixed nozzle expands to
**the time-averaged ambient pressure of its own flight**, with nothing about the gas, the chamber
or the vehicle in it. **It emerged as an invariant before it was derived**, the same exit-pressure
fraction coming out of nine optimisations that shared no parameters, and it was then checked over
**one hundred independent searches across four trajectory shapes, five gas ratios and five chamber
pressures**. The optimal area ratios across that grid span 4.985 to 84.093, a factor of seventeen,
and every one produces an exit pressure equal to its own trajectory's mean ambient, worst
disagreement 4.2 parts in ten million.

**THE RULE THEN PUTS THE OPTIMUM SOMEWHERE IT CANNOT BE BUILT.** On the manufacturer's own
published first-stage trajectory the burn-averaged ambient pressure is 28.06 percent of sea level,
so the optimal nozzle sits at an exit-to-ambient ratio at liftoff of 0.2806, **inside the band
where an over-expanded nozzle separates from its own wall**. The bell is constrained twice and the
second constraint binds. **An aerospike has no divergent wall to separate from.**

**HALF OF THE ENTIRE PRESSURE-TIME INTEGRAL OF A 160 SECOND BURN IS COLLECTED IN THE FIRST 18 TO
34 SECONDS.** The altitude-compensation question is settled in the first fifth of the burn.

### The Other Half of the Programme, Where the Answer Reverses

**DIFFERENTIAL THROTTLING OF A RING OF MODULES GIVES A DIRECTIONAL AVERAGE AUTHORITY OF EXACTLY
THE THROTTLE DEPTH DIVIDED BY PI, AT EVERY MODULE COUNT FROM THREE UPWARD.** Not asymptotically.
More modules buy evenness rather than authority.

**AND THE EVENNESS DEPENDS ON PARITY.** The achievable moment set is a regular polygon with one
side per module when the count is even and **two sides per module when it is odd**, because a half
turn is a whole number of spacings only in the even case. **Nine modules steer as evenly as
eighteen and better than any even count below twenty. Eleven need twenty-four to beat them.** The
RS1 first stage carried nine engines in its first block and eleven in its second, both odd.

**AFTER A FAILURE THE RANKING REVERSES**, because a failure breaks the symmetry the parity argument
rests on. Nine modules keep 65.3 percent of guaranteed steering authority after losing one, twelve
keep 73.2, and **a four-module ring keeps none at all**, since no surviving module points toward
the gap.

### Findings From the Documents

**THE AWARD RECORD DOES NOT CONTAIN THIS PROGRAMME AND THE ANNOUNCEMENT SAYS WHY.** Twelve keywords
were put to the federal award system across five families of award type and the programme returns
nothing anywhere. **The instrument was a Space Enterprise Consortium other transaction agreement**,
which exists so that a company outside the Federal Acquisition Regulation can be paid, and which
does not appear where procurement contracts appear. **A359 found a government that spent
29,085,924.37 dollars without writing a designation down. This is the same silence produced on
purpose and explained in advance.**

**THE MANUFACTURER'S OWN TABLE DOES NOT CLOSE AND THE INCIDENT REPORT SETTLES IT.** The payload
user's guide gives nine engines at 12,100 pounds force and a total of 133,118, which is 22.24
percent more than the product. **133,118 divided by 12,100 is 11.0015**, and eleven engines give
133,100, a residual of 18 pounds force or 135 parts per million. **The company's static-fire report
describes firing all 11 first-stage engines and auto-aborting on Engine 10.** A nine-engine vehicle
has no Engine 10.

**A SUPPRESSED ENGINEERING PARAMETER WAS RECOVERED FROM A FAILURE REPORT.** No chamber pressure or
diameter is published for the E2 engine. The incident report names **a 4.5 kilohertz first
tangential mode**, and the first tangential mode of a cylindrical chamber fixes the diameter given
the speed of sound. Sweeping flame temperature, molar mass and the ratio of specific heats over 48
combinations gives **147 to 179 millimetres**, and adding a contraction ratio and a thrust
coefficient over 36 more gives **2.6 to 8.7 megapascal**. **That band sits inside the 3 to 10
megapascal band this article had assumed on general grounds several sections earlier**, which is
two routes sharing no input and agreeing.

**AND THE SAME REPORT QUANTIFIES WHAT MODULARITY COSTS.** Two of eleven engines went unstable
against a history of one occurrence in more than three hundred tests. **Two or more of eleven at
that rate has probability 6.0 parts in ten thousand, about one in 1,669**, and the observed rate is
54.5 times the historical one. **A modular engine is many small combustors sharing one manifold,
which is precisely a mechanism for correlating their start transients**, and the independence that
calculation assumes is what the incident falsified.

**THE SPONSOR SPELLS ITS OWN PROGRAMME TWO WAYS IN ONE DOCUMENT**, three times hyphenated and once
not, while its two web documents and the register are consistent and use the other form.

**AND THE `NEARLY 60 YEARS` IN THE AWARD ANNOUNCEMENT IS CHECKABLE AND CHECKS OUT.** 492 of this
article's 9,467 surveyed records name a plug, spike or altitude-compensating nozzle. The earliest
is a 1944 weather-rocket patent followed by a twelve-year silence, and **from 1956 the record is
continuous at every window length from five to ten years**, the largest later gap being four. That
is 63 years before the sentence, so the claim was modest rather than generous. **Seven decades of
publication and not one flight.**

### The Method Rules This Pass Earned

**EVERY CENTRAL NOUN OF THIS SUBJECT IS OWNED BY ANOTHER FIELD, WHICH IS A DIFFERENT SITUATION FROM
THE LAST SEVERAL ARTICLES.** There the homonyms were proper nouns and a qualifier fixed them. Here
`spike` is Spike Jonze and the spike lute, **`wake closure` is fatigue crack closure**, `open wake`
is Wake Forest University, `area ratio` is a regurgitant jet, `thrust coefficient` is a wind
turbine, **`gas generator` is nineteen-seventies coal gasification**, `annular` is a borehole and
**`altitude compensation` is a carburettor**. A bare `nozzle` returns ten results, one a diesel
injector. **So every pattern pins its noun with a second noun.**

**TWO GUARDS WRITTEN FOR UNRELATED REASONS TURNED OUT TO BE THE TWO THIS ARTICLE MOST NEEDED.**
`fracture`, earned by A335 against parachute opening loads, is the only thing standing between this
sweep and the crack-closure literature. `wind-energy`, earned by A341 against rotor aerodynamics,
is what refuses the wind-turbine thrust coefficient.

**A MEASUREMENT THAT DISAPPEARS ONCE IT IS ACTED ON CANNOT BE AUDITED.** The family-cost report
compared the current allow list against itself plus the tag, so the moment a family was opened on
that evidence the evidence reported zero. It now measures against the closed baseline and persists
the result to a file.

**A NEGATIVE LOOKAHEAD IN FRONT OF AN ALTERNATION GUARDS ONE CLAUSE, FOR THE FOURTH TIME IN THIS
SERIES.** Caught here before it ran, because the rule was written down.

**A `sys.path.insert` INSIDE A PER-RECORD FUNCTION IS A QUADRATIC COST THAT LOOKS LIKE SLOW
NETWORK.** `homonyms._anchor_stem` inserted a directory and imported once per harvested record, so
a thirty-thousand-record sweep left thirty thousand copies on the path. **Three thousand records
took 6.19 seconds and the same three thousand took 6.27 on the second pass with the path already
grown.** Hoisting the import and memoising the stem brings a repeated pass to 2.27 seconds. **Every
article in this corpus has been paying this.**

**A PAIRWISE CONTINUITY TEST IS DECIDED BY ITS SINGLE WORST GAP, WHEREVER THAT GAP FALLS.** The
first form of the `continuous from` test asked that no consecutive pair of publishing years differ
by more than three, and **one four-year gap in 1988 moved the answer from 1956 to 1992**. The
window form cannot be moved by one gap.

**A VERIFIER'S INDEPENDENT ROUTE DISAGREED WITH THE CLOSED FORM AND THE DISAGREEMENT WAS REAL
GEOMETRY.** The ring check evaluated the maximum at the module directions, which is right for an
odd ring and wrong for an even one, and reported eighteen failures with the two extremes swapped.
**For an even ring the direction of least authority points straight at a module.**

**A FORMULA'S ASSUMPTIONS MUST BE RECHECKED WHEN ITS SUBJECT CHANGES.** The engine-out section was
written twice, because the first version applied the regular-ring closed form to a ring with a
module missing. **It overstates the surviving authority by up to 2.62 and, at four modules, by all
of it.** No check was looking, and the error was found by asking whether the assumptions still held.

**A TABLE OF THRUST FIGURES IS NOT A DESCRIPTION OF ONE NOZZLE UNLESS THE TABLE SAYS SO.** The
difference of the payload guide's sea-level and vacuum thrusts divided by sea-level pressure would
give an exit area exactly, and it would mean nothing, **because two lines above the same document
says the two figures belong to two different engines.** Caught before it reached the page.

**TWO DEFECTS IN MY OWN PROSE WERE FOUND BY READING THE ASSEMBLED ARTICLE AND BY NOTHING ELSE.**
The first was date arithmetic, a three-year term from December 2019 ending in December 2022 against
an allocation of 20 April 2022, **written as four months where the answer is eight**. **Nothing in
the numeric suite was looking at dates**, because a month is not a quantity the calculation files
produce, and there is now a check that recomputes every interval the prose states between two named
dates. The second was an over-claim, that the chamber-pressure band recovered from the instability
frequency **sits inside** the band assumed independently. **It does not.** The recovered floor of
2.60 megapascal is below the assumed floor of 3, the two overlap over 93.5 percent of the recovered
band and 82.0 percent of the assumed one, and **overlap is the honest word**. The calculation had
only ever tested overlap; the prose promoted it to containment.

**AND I RAN THE WRONG BUILD FOR SIX HOURS.** `HANDOFF.md` says plainly that
`./_check.sh --drafts` scales superlinearly in link-definition count, that it took over three hours
by A340, and that **the agent runs the stub build per pass and the full corpus build at publication
absent instruction**. I started the full drafts build anyway, watched it hold one processor at a
hundred percent for five hours and forty-one minutes with an empty output directory, and only then
read the paragraph that forbids it. **The stub build it should have been took sixteen point nine
seconds.** The handoff had the answer before the work started, and the cost of not reading it was a
working day of wall clock. **A procedure written down is not a procedure followed**, which is this
pass's own theme arriving one more time.

**AND A SLOT IS THE ONLY DEFENCE AGAINST A SURVEY NUMBER GOING STALE.** Adding twenty-two
hand-written references moved the research count from 9,485 to 9,467, because a record that gains a
hand-written definition stops being auto-cited. **The prose said 9,485 and the verifier caught it.**
The repair was not to retype the number.

### Verification

`_verify.py` **0 errors and 0 warnings** across 301 posts, the two remaining warnings being the
progress counters in this file and `TASKLOG.md`, which this commit fixes. Library tests **119 of
119**. **Article verifier 608 checks, 0 failures**, including every number the prose states checked
against the file that produced it. **Identifier verification resolved 23 hand-written identifiers
through the registry against their claimed titles and years, and required a deliberately fabricated
identifier to return nothing.** Address sweep: 57 hand-written addresses, **two of which did not
exist and were replaced**, and 19 of which return 403 from `doi.org` redirecting into publisher
anti-bot pages, which is not a citation check either way. Diction **0 constructions above the
corpus maximum**. **The stub-isolated production build succeeded in 16.9 seconds with no Liquid error, against checksum-matched bytes**, and **the rendered audit reports no findings across 543 pages**, 171 of which carry display math. The article renders to 1,714,391 bytes with 19,474 links. Source and rendered display-equation counts agree at **15**, the inline count agrees at **70 balanced pairs**, and the page carries **zero raw dollar pairs, zero unresolved reference brackets, zero unexpanded slots, zero unrendered Liquid and zero double-escaped entities**. **Zero contractions, zero parentheses, zero colons and zero semicolons outside
verbatim quotations, and zero em or en dashes.** 

### What Is Open

**THE OFFICIALITY CORRECTION IS THE PILOT'S DECISION.** A360 states the right numbers; A358 and A359
still carry the two-number form and I have not edited them.

**A361 IS THE SIBLING DESIGNATION AND IT SHARES EVERY WORD OF ITS DESCRIPTION WITH THIS ONE.** This
article deliberately left it the instrumentation, the recovery gear and the question of what it
means for one programme to hold two numbers. **`Invocon` and `Troy7` return nothing at all from the
bibliographic index**, which is a measurement rather than a gap, and the award record returns
decades of instrumentation contracts under the Invocon name.

**AND `REVERSE_PROMPT.md` NOW HAS TWO WRITERS.** This report preserves the concurrent session's
below it rather than overwriting, which is a choice and not a convention.

---

## A374 IS PUBLISHED AND LIVE

**PUBLISHED 2026-09-19 at the editorial date 2026-08-11.** Moved by `git mv` to
`_posts/2026-08-11-published_wargames_of_war_with_china.markdown` and live at
`/geopolitics/military/war-gaming/2026/08/11/published_wargames_of_war_with_china.html`.
**The two-commit pattern was followed**, the draft state having been committed across five earlier
commits and this being the publication move.

**THE INTERLOCK WAS VERIFIED BEFORE THE MOVE, NOT AFTER.** The 2026-08-11 date slot was free. All
three `post_url` targets were already published, so no build-breaking forward reference exists.
Nothing in the corpus forward-references this article. The article carries no series, so **no
navigation was renumbered on any live page**, which is the failure mode that renumbered four pages
when A373 published.

**THIS IS THE FIRST POST WHOSE FIRST CATEGORY IS `geopolitics`**, so it claims a new top-level path.
**Fifty-eight sibling repositories were checked** for a name matching `geopolitics`, `military` or
`war-gaming`, and none exists. That check is the one the `keleusma` shadowing incident exists to
force, and a live-site probe alone would not have answered it, since an unclaimed path and a shadowed
path both return 404 before publication.

**Deploy gate before pushing.** `_verify.py` 0 errors and 0 warnings across **302 posts**, build ok,
and the rendered audit reporting **no findings across 466 pages**.

### Draft release announcement, for the pilot to review

```
New Blog Post: What Published Wargames Say About a War With China

Everyone cites the same handful of Taiwan wargames and almost nobody reads them. I read them,
checked every number, and found that the most confident summaries get the headline result wrong.

Key takeaways:
- The invasion does not fail in "the vast majority" of the CSIS iterations. Nine of twenty-four
  ended in clear Chinese defeat, fourteen ended in stalemate, and the one Chinese victory came
  when the United States stayed out.
- The nuclear study finds that seven of eight nuclear uses began with a China team facing exactly
  the conventional defeat the other games treat as the happy ending.
- The economic consensus is an artefact of citation. Three original estimates exist and everything
  else re-cites them, and two estimates of the same blockade differ by nearly a factor of two
  because one prices trade disruption and the other a macroeconomic shock.
- The United States intelligence community says Chinese leaders have no current plan for 2027 and
  no fixed timeline, which contradicts the closing-window premise the whole genre assumes.

You can read the full article here:
https://sgeos.github.io/geopolitics/military/war-gaming/2026/08/11/published_wargames_of_war_with_china.html

Let me know your thoughts. I would love to hear how you handle load-bearing numbers that arrive
through a summary rather than from the source!

hashtag#Wargaming hashtag#NationalSecurity hashtag#Taiwan hashtag#Research hashtag#Verification
hashtag#DataQuality hashtag#Analysis
```

---

## A374, What Published Wargames Say About a War With China, Four Passes and a Diction Pass

**THE PATHOLOGICAL WORD-USAGE PASS FOUND AN OVER-CORRECTION I HAD INTRODUCED MYSELF.** `and not` ran
at **1.67 per thousand against a corpus median of 0.60** while `rather` had fallen to **0.28 against a
median of 4.00**. The equation pass had substituted `and not` for `rather than` and the survey pass had
raised it again, so avoiding the corpus-normal construction manufactured a replacement tic. That is the
failure `STYLE_GUIDE.md` names, and the fix was to restore `rather than` where the structure is
parallel rather than to invent a third formula. **34 constructions varied**, leaving `and not` at 0.28
and `rather` at 1.30, both below median. The `Let X be` equation opener went 16 to 5 across three
rotated forms, `were read from` 10 to 3, and `which is` 14 to 9. **Four were kept on purpose**, two
paraphrasing McGrady and one quoting TIDALWAVE, because editing a quotation to hit a rate is
falsification. The full diff was read line by line, an n-gram rescan confirmed no new formula, and the
rendered audit reports no findings across 466 pages.



**THE PUBLICATION REVIEW DOUBLED THE ARTICLE AND TRIPLED ITS REFERENCES, 32 TO 111.** On the pilot's
instruction the article now also serves as a comprehensive survey of the contemporary literature. A
new section of thirteen subsections covers the other operational wargames, the allied and European
games, invasion feasibility in the peer-reviewed journals, whether Taiwan is strategically decisive,
the nuclear escalation split, deterrence theory, blockade, the economic estimates, semiconductor
dependence, official assessments, wargaming as a method, and artificial intelligence in wargaming.
Four delegated research sweeps supplied leads and **every citation was verified here before use**,
which is why several leads did not survive into the article.

**THE OFFICIAL ASSESSMENT CONTRADICTS THIS ARTICLE'S OWN PREMISE.** The threat assessment of the
United States intelligence community, prepared with information available as of 14 March 2026, states
that **Chinese leaders do not currently plan to execute an invasion of Taiwan in 2027, nor do they have
a fixed timeline for achieving unification**, and that Chinese officials recognise an amphibious
invasion **would be extremely challenging and carry a high risk of failure**. The article was built on
a closing-window premise, so this now appears early in the premise section rather than buried in a
survey. It is the sharpest official contradiction of that premise available and it comes from the body
whose job is to assess Chinese intent.

**THE ECONOMIC LITERATURE IS SMALLER THAN IT LOOKS.** Only Bloomberg, Rhodium and the Institute for
Economics and Peace produce original numbers. The Commission, the German Marshall Fund and others
re-cite them, which manufactures a false impression of convergence. **The two blockade estimates differ
by a factor approaching two**, 2.8 percent of global output against 5 percent, because one prices trade
disruption and the other a macroeconomic shock. RAND's 2025 work prices sanctions alone and therefore
sits an order of magnitude below the war figures, so quoting it beside them would misrepresent both.

**THE SEMICONDUCTOR FIGURE NOW CARRIES ITS THRESHOLD AND ITS DATE.** The famous 92 percent is a 2019
measurement of capacity below 10 nanometres, where that capacity was about 2 percent of all capacity.
TrendForce measured 68 percent at 16 and 14 nanometres and below in 2023. The two are not in conflict,
and a claim quoted without its threshold cannot be checked.

**TWO INDEPENDENTLY DESIGNED GAMES LAND WITHIN EIGHT PERCENT OF EACH OTHER.** The Sasakawa hex-map
exercise destroyed 127 major Chinese ships where the CSIS base scenario averaged 138. **The starkest
number in the public record comes from the game members of Congress played**, where 40,000 of 50,000
landed troops became casualties in six days.

**THE METHOD CRITICS ARE NOW IN THE ARTICLE, AND THEY ARE WARGAME DESIGNERS.** Their case is that
wargames are about understanding and not knowledge, that a game often reveals more about its players
than about the war, and that combat wargames should not be repurposed to answer questions about
deterrence or war termination. One RAND study finds artificial intelligence least promising for games
**played as one-offs or a very limited number of times**, which describes most of the public Taiwan
games.



**THE PRIMARY-REFERENCE PASS CAUGHT A MISATTRIBUTION IN MY OWN DRAFTING PASS, AND THE PRIMARY SAYS
CLOSE TO THE OPPOSITE.** The drafting pass credited the Heritage Foundation's executive summary with
four TIDALWAVE figures, the culmination ratio, the five to seven and thirty-five to forty day
munitions brackets, and ninety percent of aircraft destroyed on the ground. **The archived executive
summary contains none of them.** They came from a search-engine summary and a news article.
heritage.org refuses every page to curl and to the fetcher, so **a Wayback snapshot of 14 April 2026
supplied the text the live site would not**, bylined Robert Greenway and Anna Gustafson. **The two
equations built on those figures were deleted** and the figures are now labelled press claims. **On
munitions the primary states that platform destruction, not munition exhaustion, limits combat power**
in the most intense cases, with part of the magazine never fired because the platforms are already
destroyed. That is a different failure from running out of missiles and it weakens the tidy reading
that stockpile depth is the binding constraint.

**THE SCENARIO YEARS NOW HAVE A SOURCED ORIGIN.** The drafting pass could say only that the reports
gave no rationale. The Senate Armed Services Committee stenographic transcript of 9 March 2021 carries
Admiral Davidson telling Senator Sullivan that the threat is manifest during this decade, in fact in
the next six years. **2021 plus six is 2027**, which is where CSIS at 2026, CNAS at 2027, the nuclear
game at 2028 and the Heritage exercise at 2030 cluster, and the TIDALWAVE summary independently says
many insiders point to 2027. The demographic-peak explanation the external summary offered remains
unsupported.

**THE PREMISE NOW CARRIES BEIJING'S OWN PRIMARY.** The 2022 white paper states that peaceful
reunification is the first choice and that force is not renounced. It announces no timetable. That is
the minimum the wargames assume and no more.

**All four passes complete. Committed and PUSHED on the pilot's instruction. NOT PUBLISHED**, and
publication was explicitly not requested.

Standalone analytical essay at editorial date **2026-08-11**, categories
`geopolitics military war-gaming`, **2,069 lines, 63 display equations, 53 inline expressions, 111
references, about 12,100 words.** Article number and date were chosen as the next free number after
the reserved X-Planes range and the only unused date between 2025-12-17 and 2026-08-19.

**THE SOURCE WAS AN EXTERNAL MODEL'S SUMMARY AND NINE OF ITS CLAIMS WERE WRONG.** The pilot supplied
an exchange with an external large language model. Every claim was checked against the primary
reports. **The largest error was that the invasion fails in the vast majority of the CSIS iterations.**
The counts give **9 decisive Chinese defeats, 14 stalemates and 1 PLA victory out of 24**, the victory
being the run where the United States stays out. **The second was that the record is uniform.** The
summary's own logistics citation was a news article about the Heritage Foundation's TIDALWAVE model,
**whose stated aim is to push the American culmination date beyond the PRC's, which implies the
United States culminates first**, and the summary did not say so. The blunter phrasing about
catastrophic defeat is a press claim and is not in the archived executive summary, as the
primary-reference pass established below. The other seven corrections are listed in the article's Epistemic State.

**THE KEYSTONE IS THAT THE TWO CSIS GAMES POINT AT THE SAME MOMENT FROM OPPOSITE SIDES.** The
conventional game treats destruction of the amphibious fleet as decisive. The nuclear game puts
**seven of its eight nuclear uses at Chinese first use while facing exactly that defeat**. The
conventional failure the external summary treated as the end of the gamble is where the nuclear games
locate the greatest danger. **This synthesis is marked as inference and is not stated in that form by
any single report.**

**EQUATION DENSITY WENT 12 TO 48 AND EVERY EQUATION IS ARITHMETIC ON A PUBLISHED FIGURE.** The opening
says so, because none of them models a war. The consistency checks close against the sources. **The
population balance leaves implied net migration at zero**, the crude rates recompute from the counts,
and **the Bloomberg dollar and percentage figures imply world output of about 98 and 110 trillion
dollars**, which are plausible for their years. **The equation pass also found something the drafting
pass had missed.** Comparing only midpoints hid that **the latest Bloomberg ratio of Chinese to
American loss, 1.7, falls below the entire RAND range of 2.5 to 7.**

**FOUR ASSUMPTIONS ARE MINE AND NOT THE SOURCES' AND ARE LISTED AS SUCH**, the one most likely to be
mistaken for a report finding being the independent forty percent loss per voyage behind the ship
survival figure.

**VERIFICATION, AND ONE LIMITATION THAT MATTERS.** `_verify.py` reports **0 errors and 0 warnings**
across 301 posts. **The deploy gate `./_check.sh` passed end to end**, 465 pages, 170 carrying display
math, **no findings**. **The `--drafts` gate could not be run.** It was killed three times for low
memory, because `_drafts/` holds **73 files, 51 MB and 648,000 lines** of X-Planes work and building
all of it exhausts memory. **A374 was therefore built in a scratch copy carrying the real `Gemfile`,
`_config.yml`, all four plugins and the whole `_posts` corpus, with only this article in `_drafts/`.**
That is not the Gemfile-free plugin-stripped build the process forbids, and it differs from the full
gate only in which other drafts are present, none of which this article references. **That build
succeeded in 37.5 seconds after the primary-reference pass and its rendered audit reports no findings
across 466 pages**, with the
draft's checksum matched before and after. The rendered page was then read directly. **No unresolved
reference brackets, no raw dollar pairs, no unexpanded Liquid, 56 display blocks for the 54 equations
plus two `\\[2ex]` line breaks, and all three `post_url` links resolving to live addresses.** **All 75
arithmetic statements across those 54 blocks were rechecked by script** with no failures. **Two defects in my own new prose
were caught by reading and not by any checker**, a survival example claiming four voyages where two
already suffice, and `An [news article]`.

**URLs.** 27 of the 29 addressed definitions return 200, the exceptions being 403 on both
`heritage.org` pages and 406 on `newsweek.com`. **`aei.org` refuses HEAD with 403 and serves GET with
200**, so a HEAD-only sweep misreports it. That, the `usnews.com` timeout that forced a different
Reuters copy, the fetcher refusals from `bloomberg.com` and `cnn.com`, and the Wayback route around
`heritage.org` are all recorded in `URL_VERIFICATION.md`.

**WHAT WAS DROPPED, AND WHAT REMAINS WEAK.** A Cyber Defense Review wargame paper refused at 403 and
was never read. A French institute after-action report would not connect. A St Louis Fed review
article would not resolve. **The Department of Defense annual report on Chinese military power refused
every retrieval route tried**, so only its existence is cited and its warhead figures are attributed to
an accessible specialist summary. A sweep also reported fleet counts attributed to that report that
could not be found in it, and they are not used. **The full TIDALWAVE report, about 400 pages according
to Newsweek, was never retrieved**, nor was TIDALWAVE II, nor is the Bloomberg model public, so those
three remain at press-account strength and are labelled as such.

**THE TWO REMAINING VERIFIER WARNINGS BELONG TO THE X-PLANES SESSION AND WERE LEFT ALONE.** They
reported a drafted count that had gone stale when that session added the X-63, and this article
carries no series field and was not the cause. **That session has since updated both counters and
the warnings are gone**, so this paragraph records what was true when it was written rather than
what is true now.

**Publication is not requested and the article is not published.**

---

## The Scan Found No Drafting History and That Is the First Time

**A322 shipped five sentences of drafting history, A323 six and A358 seven**, every one of the
form `the draft said X and was wrong`. **This article shipped none.** The scan was run over 483
author sentences and returned nothing, which is worth recording because the convention that
produces those sentences, naming a withdrawn claim rather than deleting it, is unchanged. **What
changed is that the equation pass wrote its withdrawals as statements about the subject from the
start**, so there was nothing to rewrite.

## The Superlative Scan Found Four Real Defects

**Seventy-six sentences carried a strong ranking and four of them did not earn it.**

**The article said the X-62A is the fourth or fifth machine in the line of variable-stability
aeroplanes.** That is a count this article never made, and the line includes at minimum the
Cornell and Calspan machines, the NT-33A, the Total In-Flight Simulator, the Learjets and two
European aircraft. **It now says the X-62A is a late member rather than the first, and says
plainly that it does not know how many stand between**, because counting them would mean
settling what makes an aeroplane a variable-stability aeroplane and no source consulted draws
that line.

**It said NASA Technical Paper 1538's appendix gives the actuator lag and rate limit of every
surface.** It gives them for every surface but the speedbrake, which carries a deflection limit
in Table 1 and no actuator anywhere. **The article now says so**, and observes that the omission
is consistent with the speedbrake not being a flight control.

**It said the award record is the only place the older expansion of the acronym survives at
scale.** That is a claim about everywhere and this article searched part of it. **It now says it
is the largest body of text this article searched in which the older expansion still stands.**

**And it called manual control theory's crossover model the strongest single result in the
field.** That is a ranking over a discipline. **It is now described as the field's central
result**, which is what the textbooks call it.

**Three further softenings were made on the same pass**, being `every simulator of every kind`,
`will always show a lumpy record` and `the whole twelve years` against a measured span of 11.6.

## A Formatting Defect the Number Checks Could Not See

**The article printed `the weaker one for the last 4.48` with no unit.** The slot held a number
of years and the sentence supplied no noun. **Every numeric check passed**, because the value
was correct and appeared the expected number of times. **A unit is not a number and nothing in
the suite was looking for one.**

## A Decision Was Recorded in the Process Files and Never Reached the Page

**The equation pass decided not to use the phase-delay parameter of the bandwidth criterion and
wrote that decision into TASKLOG and this file.** It never reached the article. **The
publication review found it by re-reading the closing sections against the process files**,
which is the check that exists for exactly this.

**The article now carries it as a section.** The criterion is the field's own way of turning a
delay into a handling-qualities level and its phase-delay parameter is exactly what the delay
floor should be expressed in. **Deriving that parameter for a pure delay from the definition as
recalled gives half the delay, and the usual summary of the subject says it is the delay.** Those
cannot both be right, **a factor of two is not a rounding**, and the specification that settles
it has not been read. So the article uses the phase margin, which it derives in one line, and
says why the other is absent.

## What the Primary Pass Had Found

**Report primaries 842 to 1,199 and 10.2 percent to 13.9**, after a fourth sweep of 148 narrow
reports-server questions and 42 defence-registry ones. **Every cluster rose.** The keystone rose
least, from 4.0 to 5.5, and **no single venue holds more than 4.8 percent of it**, so it is a
dispersed conference and journal literature and was never a report literature.

**Every one of the 42 defence-registry questions returned exactly 200 rows.** All of them. The
reports server saturated on 60.8 percent and averaged 7.29 against a cap of 10. **The two
registries are limited in different ways and this sweep measured it rather than repeating it.**

**The programme publishes eight papers and a thematic sweep found four**, the four it missed
being the ones whose titles name the systems rather than the aeroplane. Walking two contiguous
identifier ranges recovered all eight and turned up a correction notice on one of them.

**And the school teaches the scale its own aeroplane is measured on.** The USAF Test Pilot School
publishes its Flying Qualities Phase textbook chapter by chapter into the defence registry, and
**Chapter 16 is a reprint of NASA Technical Note D-5153**. It was found by a question about
specifications rather than by looking for it, and it is now the Conclusion's penultimate finding.

## What the Equation Pass Had Found

**From 21 display equations to 45 and from 46 declared symbols to 88.** Its two findings were
that **the column which makes the projector vanish is the column that runs out first**, the flap
saturating at 8.17 degrees of angle of attack where the tail would not until 30.5, and that
**the leading-edge flap's scheduled lead is very nearly cancelled by its own actuator**, the
schedule's pole and the actuator's corner sitting 1.42 percent apart.

## Verification

**Verifier 0 errors and 0 warnings. Tests 117 of 117.** **The article verifier runs 492 checks
and passes all of them**, up from 269 at the drafting pass. **The injection suite catches 281 of
281.** The symbol scanner reports all 88 declared symbols used and every symbol used declared.
**Diction reports 0 constructions above the corpus maximum** across 62 peers on 17,573 words of
author prose. **Zero citation gaps at a nine-hundred-character window. Zero contractions, zero
dashes, zero prose colons, zero semicolons, and no caps emphasis outside engine designations.**

**Identifier verification passes on content**, with 33 quoted phrases held against the saved
copies they were read from, **39 curated identifiers resolved through the registry and compared
against the year their labels claim**, 14 book identifiers held against both recorded title and
recorded author, **a deliberately fabricated identifier resolving to nothing**, and 0 dead
addresses.

**The whole corpus with this article published builds against checksum-matched bytes and the
rendered audit reports no findings across 542 pages.** Source and rendered display-equation
counts agree at 45, with zero raw dollar pairs, zero unresolved reference brackets, zero
unexpanded slots and zero unrendered Liquid.

**FINAL STATE.** **18,645 lines, 45 display equations, 88 declared symbols, 8,749 reference
definitions, 113,876 words.** Four sweeps retrieved 35,837 records of which 30,647 distinct, the
store removed 1,829, the gate admitted 9,012 and refused 19,806, and **every one of the 8,596
records surviving deduplication is cited** across 15 clusters alongside 153 hand-written
definitions. Report primaries 1,199 at 13.9 percent. Median year 2006, range 1927 to 2027, with
85.0 percent at or before the year of the redesignation.

**The probe covers 19 conclusions with one uncovered**, being the claim that the contract record
and the designation register are independent documents that agree, **which has no aeronautical
literature because it is a claim about records** and rests on the two records themselves.

## What the Article Says, in Five Findings

**THE X NUMBER IS NOT IN THE ACCOUNTING SYSTEM.** 73 transactions and 29,085,924.37 dollars over
11.6 years and not one of them calls it the X-62A. The designation appears once in the whole
record and that once falls 23 days past the article's own date, **so the dateline horizon had to
be enforced in the data rather than in the sentence** or the article would have reported the
opposite.

**THE KEYSTONE IS AN IDENTITY AND IT REMOVES THE VEHICLE.** Exact model following holds if and
only if a projector built from the host's control effectiveness matrix annihilates the demanded
change of dynamics. **The rank bound turns that into a count of control surfaces at three per
axis and the aeroplane has three per axis**, the throttle among them because the speed equation
is one of the three.

**THE COLUMN THAT MAKES THE PROJECTOR VANISH IS THE COLUMN THAT RUNS OUT FIRST**, so the
envelope is set by the weakest control and not the strongest.

**THE MACHINE CAN MAKE ANY AEROPLANE SLUGGISH AND CANNOT MAKE ANY AEROPLANE CRISP**, because
every delay in the host lies between the pilot and the simulated response and delays add.

**AND THE ANSWER COMES BACK ON A SCALE WITH TEN BOXES AND NO METRIC**, whose defining paper is
Chapter 16 of the operating school's own textbook.

## What Comes Next

**A360, the X-63**, editorial date 2025-12-08, series index 64. **The register has now been
unofficial for two designations running and the X-63A is the third**, allocated 10.2 months after
this one. **Wait for the pilot's prompt.**
