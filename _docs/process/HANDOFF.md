# Handoff Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the resume prompt for an agent picking up after a compaction or a new session. It is a
snapshot, deliberately not kept current, and it self-reports as stale rather than misleading a
resuming agent. Read it first, validate it, then read the live channels.

---

## Validity

- **Branch**: `master`
- **Parent commit** (the repository state this handoff describes): `9d1e733`
- **Written**: 2026-08-12
- **Tree at write**: clean, nothing unpushed
- **Context**: the X-Planes series is IN PROGRESS. **Thirty-nine of seventy-two articles drafted,
  all four passes complete on each. None published.**
- **Since the previous handoff**: **A334, the Boeing X-37, and A335, the Scaled Composites X-38, were
  each taken through all four passes and pushed.** Neither is published. The tooling gained a
  bare-pipe strip in `refs.clean`, a typographic-normalisation step in the article gates, a
  trailing-full-stop guard on harvested identifiers, and eleven new homonym families. **Three new
  entries were added to `VERIFICATION_TRAPS.md` after A334 and two more after A335.**

**Commit identifiers recorded in `_docs/` before 2026-08-09 are void.** History was rewritten that day
and 147 commits took new identifiers. Anything older than that will not resolve.

**Validate before trusting.** Compare the recorded **Parent commit** to `git rev-parse HEAD~1`. Because
this handoff file is itself committed, its commit becomes the branch tip and its parent is the state
described.

- **Match → VALID.** Proceed per the resume prompt below.
- **Mismatch → INVALID and STALE.** A later commit moved the tip, so this file describes a state that
  is no longer current. Do **not** proceed and do **not** guess what changed. Report it as
  invalid-and-stale, familiarize from the live channels, namely `REVERSE_PROMPT.md`, `TASKLOG.md`,
  `_drafts/draft_summary.md`, and the git log, which are always authoritative, and wait for
  instruction.

---

## Resume prompt, and the next prompt will be "Please draft A336, 'X-Planes: X-39, Reserved but Never Assigned.'"

**Nothing is outstanding.** A335 finished all four passes, is committed and pushed, and returns 404
while the site root returns 200, which is correct because nothing in the series is published. There is
no half-finished pass to pick up.

**Wait for the pilot's prompt. Do not begin A336 unprompted.**

**A336 IS A DESIGNATION ANOMALY AND THAT CHANGES THE JOB.** X-39 was reserved and never assigned.
There is no aircraft, no keystone to identify and no system to dimension, so
`_docs/writing/RESEARCH_AIRCRAFT_STRUCTURE.md` prescribes the **reduced six-section order** rather than
the twelve-section one. **Read that section before writing a line.**

**THE ANOMALY CLASS HAS A BOUNDARY AND A320 ESTABLISHED IT.** The X-23 is listed among the anomalies
and was written at full length, because the SV-5D actually flew three times and returned a measurement.
**The test is whether a vehicle existed and produced data, not whether the designation is disputed.**
For a number that was reserved and never assigned, **the short class is the honest default**, and the
genre document says in terms that padding a short article with sections it does not need is worse than
leaving it short.

**THE RESEARCH QUESTION IS THEREFORE ABOUT THE DESIGNATION SYSTEM AND NOT ABOUT A MACHINE.** What was
the number reserved for, by whom, and why was it never assigned. **I have not researched it and I am
not going to guess in this file.** Establish it from sources before writing, and where the record does
not settle it, say so, because on a short article the statement of what is unknown is the main
contribution.

**EXPECT THE SOURCE BASE TO BE SMALL AND DO NOT INFLATE IT.** The comprehensiveness directive is a
permission and not an instruction. An article that says the designation was reserved in a given year,
names the deciding authority and explains what the reservation reveals about the numbering system is
complete at that length. **Report the counts and do not target them.**

**WHAT THE THREE SERIES SECTIONS SHOULD DO ON AN ANOMALY ARTICLE IS AN OPEN QUESTION.** The
contemporary-literature survey and the source-base accounting exist to serve a technical argument, and
an anomaly article has none. **Decide deliberately whether they belong, and say why in the article
rather than including them out of habit.** A320 kept them because it had a vehicle. This one may not.

**THE SEQUEL IS A REAL AIRCRAFT AND IT IS ALREADY WRITTEN ABOUT HERE.** A337 is the Boeing X-40, which
A334 and A335 both discuss as the X-37's subscale predecessor. **Do not exhaust the X-40 material in
A336**, and remember the back-reference-only rule, which means A336 may cite A334 and A335 and must not
cite A337.

## Where the Series Stands

Seventy-two articles, A297 through A368, back-dated one per day from 2025-10-06 to 2025-12-16,
covering every X-designation from X-1 through X-76.

**Thirty-nine complete**, A297 through A335, all four passes each, all in `_drafts/`, **none
published**.

| Article | Aircraft | Final state |
|---|---|---|
| A329 | Boeing X-32 | 19,593 lines, 28 eq, 6,159 refs |
| A330 | Lockheed Martin X-33 | 32,379 lines, 92 eq, 10,248 refs |
| A331 | Orbital Sciences X-34 | 20,006 lines, 38 eq, 6,352 refs |
| A332 | Lockheed Martin X-35 | 27,560 lines, 71 eq, 8,710 refs |
| A333 | McDonnell Douglas X-36 | 20,991 lines, 28 eq, 6,696 refs |
| A334 | Boeing X-37 | 18,700 lines, 42 eq, 5,762 refs |
| A335 | Scaled Composites X-38 | 6,733 lines, 24 eq, 1,936 refs |

**A335 IS THE SMALLEST FULL-AIRCRAFT ARTICLE SINCE A323 AND THAT IS CORRECT.** Its pool held 6,212
records against A334's 13,351, because the decelerator literature is smaller than the orbital one and
because the vehicle ran for seven years rather than twenty-five. **Neither number was targeted and
neither should be read as a standard.**

**THE REFERENCE COUNTS JUMPED BY A FACTOR OF THREE AT A328 AND THAT IS THE DIRECTIVE WORKING, NOT A
CHANGE OF STANDARD.** From A328 onward the practice is that **every harvested master record is
cited**, with no leftovers, which is what the comprehensiveness directive means once the pool is
built properly. Do not treat the earlier, smaller counts as the target.

**THE SIZE VARIES WITH THE SUBJECT AND THAT IS CORRECT.** A330 is the largest article in the series
and A331 is half its size, because the X-33 has a physics chain worth thirty thousand lines and the
X-34 does not. **Neither number was targeted.**

**THE EQUATION COUNT VARIES MORE THAN THE LENGTH AND A333 IS THE LOWEST IN THE SERIES AT 28.** That is
correct too. The X-36 has **one relation applied repeatedly** rather than several chains, and padding
it toward the median of 94 would have been manufacturing rather than earning. **Report the count and
move on.**

Read `_drafts/draft_summary.md` for per-article detail rather than re-deriving it.

---

## The Established Rhythm, Which Is the Most Important Thing Here

Four passes, each a separate prompt from the pilot. **Do not run ahead.**

1. **"Please draft Axxx, '<title>.'"** Research, write, verify, commit. **Do not push.**
2. **"Please review for equation density, and add all candidate equations."**
3. **"Please review for reference density, specifically primary references, and add all identified
   references."**
4. **"Please review for publication, and make suitable changes..."** This prompt also asks for a push.

After every pass, update `REVERSE_PROMPT.md`, `TASKLOG.md` and `_drafts/draft_summary.md`, and commit
them with the article in one commit.

---

## Standing Directive, Quoted Because It Governs Every Pass

The pilot quotes this verbatim on every publication-review prompt:

> Note that all articles in this series have no length limit, no reference limit, and that they should
> serve as a comprehensive survey and review of the contemporary literature in addition to any other
> stated goals. Finally, make sure that the draft has been committed and pushed, but do not yet publish
> it.

**No length limit and no reference limit are permissions, not instructions.** Do not pad to reach a
band.

---

## Method Rules Earned the Hard Way

### On the analysis

**A DEMONSTRATION CAN BE EASIER OR HARDER THAN THE THING IT DEMONSTRATES, AND BOTH ARE COMPUTABLE.
TWO CONSECUTIVE ARTICLES FOUND OPPOSITE SIGNS.** A332's famous sortie was flown in the easiest
available ordering, with the heaviest event first and the most weight-sensitive last, at a weight the
production aircraft would never see. A333's model carried a handicap the full-scale aircraft would
never carry, because Froude scaling compresses time by the square root of the scale while a link delay
and a human reaction time do not compress at all. **Ask which way the demonstration was tilted and by
how much. It is usually arithmetic rather than opinion.**

**BEFORE REACHING FOR PHYSICS, CHECK WHETHER A CHRONOLOGY ANSWERS THE QUESTION.** A332 spent its
keystone on whether one sortie was evidence or theatre, and the answer came from dates. Every element
had been flown already, the first in-flight conversion was eleven days earlier on a sortie that went
faster, **and the programme's own contemporary statements listed every element as done four days
before the famous flight.** No calculation was needed and none would have been as decisive.

**A FORWARD CALCULATION THAT FAILS TO EXPLAIN A DESIGN DECISION LOCATES THE CONSTRAINT, AND A335 GOT
ITS THIRD RESULT THAT WAY.** The obvious reason a canopy reefs in five stages is crew tolerance. Run
forwards, the steady inflation load admits the WHOLE canopy in one step inside three g, and an
opening-shock factor of 2.5 still reaches only 5.25 g. **The constraint is therefore not the crew**, and
what the failure locates is the canopy's own structure, which no vehicle-level model can reach. **Do
not fit a model to a known answer. Report the failure and say what it rules out.**

**INVERT FOR THE SPEED, NOT ONLY FOR THE AREA, BECAUSE AN INVERSION IN THE RIGHT VARIABLE ATTACHES A
MARGIN.** A335's reefing conclusion was stated first as an area comparison and looked comfortable.
Inverted for the deployment speed at which the load bites, it holds by **1.20 times at three g and not
at all at two g.** **A claim without a margin invites the reader to assume the margin is large.**

**TWO ARTICLES MEASURING THE SAME QUANTITY WITH OPPOSITE SIGNS IS WORTH MORE THAN EITHER.** A334's
X-37 scales from the Shuttle orbiter at mass proportional to length to the **1.924**, below the cube,
because a small reusable vehicle keeps its fixed overhead. A335's X-38 scales from the X-24A at
**3.507**, above it, because the mission grew faster than the machine. **Neither pair is geometrically
similar and the reasons differ**, which is a warning against reading a scaling exponent as a property
of the technology. **The second measurement was only possible because the first existed.**

**COMPUTE THE SENSITIVITY RATHER THAN ASSERTING ROBUSTNESS.** A335's draft claimed its energy ratio was
robust to the assumed lift coefficient. The equation pass showed the sink rate moving fifteen percent
and the ratio moving as the FIRST power between 19.7 and 32.8. **The claim survived and the individual
sink rates turned out not to deserve three significant figures.** An assertion of robustness that has
not been computed is a guess.

**AN IDENTITY THAT REMOVES THE VEHICLE ENTIRELY IS WORTH MORE THAN THE NUMBER IT SUPPORTS, AND BOTH
RECENT ARTICLES FOUND ONE.** A334's entry heading change is the lift-to-drag ratio times the sine of
bank times the logarithm of the speed ratio, **and the altitude term cancels**. A335's flare has
available energy exceeding what it must remove by the SQUARE of the glide ratio, **exactly, with no
mass, area or density**. In both cases the identity says which vehicle properties can and cannot buy
the manoeuvre, which the number alone does not.

**TURN AN AMPLIFICATION INTO A BUDGET, BECAUSE A BUDGET FORCES CONCLUSIONS AN AMPLIFICATION CANNOT.**
A333's draft asserted that a fixed delay is worth 1.8898 times as much at model scale. The equation
pass wrote the crossover frequency an unstable pole demands and divided a phase margin by it, giving
**147.7 milliseconds for the model against 279.1 for the full-scale aircraft**. The budget is smaller
than a human reaction time, **so the ground pilot cannot have been inside the stabilisation loop, and
the architecture follows from arithmetic rather than from preference.**

**AN IDENTITY THAT DOES NOT DEPEND ON HOW A PROCESS IS MANAGED IS WORTH MORE THAN ITS MAGNITUDE.** A
clutch engaging a stationary inertia to a constant-speed source destroys **exactly half** the energy
drawn, whatever the torque profile. A332 verified it by integrating under three unrelated profiles.
**The magnitude needed an unpublished inertia and the fraction needed nothing.**

**TWO DEFINITIONS OF ONE QUANTITY CAN DIFFER BY AN EXACT CONSTANT AND BOTH BE CORRECT, AND THE
VERIFIER WILL LOOK LIKE IT FOUND A BUG.** A333's calculation and its verifier disagreed on a doubling
time by **1.900**, which is arccosh 2 over ln 2. The modal convention measures the growing
eigen-solution; a disturbance released from rest follows a cosh because it starts with no rate.
**Neither was wrong. Report both and say which question each answers.**

**AN ASSUMPTION-FREE BOUND WHOSE ABSURDITY IS THE FINDING.** A332 bounded the clutch dissipation by
rated power times quoted engagement time and got 97.3 megajoules, which would heat the plates by 6,853
kelvin. **The bound is impossible and that is the result**, because it proves the engagement is limited
by heat rejection rather than by energy, which is why a mode change is a scheduled event.

**INVERT A CORRECTED-FLOW OR EFFICIENCY RELATION FOR A THRESHOLD IN PHYSICAL UNITS.** A332 turned hot
gas ingestion from an adjective into **66.95 kelvin**, the inlet temperature rise at which the hover
margin vanishes. **A comparison between two architectures then becomes a comparison of numbers.**

**A MOMENT BALANCE WHOSE FORCES ARE FIXED BY HARDWARE DETERMINES THE CENTRE OF GRAVITY RATHER THAN
BEING TRIMMED TO IT.** A332's hover balance fixes the station at 47.37 percent of the fan-to-nozzle
distance, and a five percent thrust-split modulation buys 14.72 inches of travel. **That is the one
cost in the article which does not ease as the aircraft gets lighter.**

**DERIVE AN ASSUMED COEFFICIENT AND THEN ASK WHICH DIRECTION THE ASSUMPTION ERRED.** A333 assumed a
tailless directional derivative and later derived it from slender-body theory, getting **2.018 times**
the assumption. **The draft was therefore the optimistic case**, and every conclusion that survived it
survives the derived one more comfortably. Carry both through the tables rather than replacing one.

**A BRACKET THAT SPANS A FACTOR OF SIX AND FLIPS THE CONCLUSION INSIDE ITSELF MEANS THE CONCLUSION IS
NOT DETERMINED. WITHDRAW IT AND KEEP THE STRUCTURAL CLAIM.** A333 said the split ailerons were margin
rather than necessity. Across the plausible drag increment they run from 22.1 to 132.4 percent of the
nozzle's moment. **What survives needs no increment at all**, being that the nozzle's authority is flat
with speed and the drag rudder's rises as its square, so each owns one end wherever the crossover
falls.

**A RATIO THAT SOUNDS FATAL MAY NOT BE, AND PUTTING BOTH NUMBERS ON THE PAGE IS HOW YOU TELL.** A333's
Reynolds penalty is 6.749, which sounds disqualifying until the model turns out to run at 8.81 million
and the full-scale aircraft at 59.46 million, **both deep in the fully turbulent regime.** The penalty
is real and confined. **Neither dismiss a ratio nor be frightened of it. Compute both ends.**

**THE SAME FACTOR ARRIVING FROM THREE UNRELATED QUANTITIES IS WORTH MORE THAN ONE DERIVATION.** A333
gets 1.8898 from the time ratio, from the delay budget and from the turn rate, and assumed it for none
of them.

**A SECOND ROUTE THAT IS ALGEBRAICALLY THE SAME STATEMENT TESTS TRANSCRIPTION AND NOT PHYSICS. SAY
WHICH.** A332 recovered a fan mass flow two ways and they agreed exactly, because the ideal disc makes
them identical. **Exact agreement between equivalent formulations is what they ought to produce and is
no evidence the physics is right.**

**A WITHDRAWN CLAIM MUST BE CHASED THROUGH THE EPISTEMIC STATE AND THE CONCLUSION.** A333's equation
pass withdrew a claim about the split ailerons and the withdrawal reached neither. **Both still
asserted it a pass later**, and only the publication read caught them.

**WHERE A PREVIOUS ARTICLE'S INVARIANCE STOPS HOLDING IS ITSELF A RESULT, AND A331 GOT THE BEST
STRUCTURAL FINDING IN THE SERIES OUT OF IT.** A330 proved the membrane tank fraction contains no
length and concluded that a subscale tank was therefore a valid test. **That cancellation holds only
while STRESS sets the thickness.** Minimum gauge does not scale, so the gauge is 1.45 times what load
needs at the X-33's radius and 4.14 at the X-34's, and once gauge binds the fraction goes as one over
the radius. **Two consecutive articles, the same relation, opposite conclusions, both correct.** When
an article inherits a relation from its predecessor, ask where the predecessor's conclusion stops.

**A FORWARD CALCULATION THAT FAILS BY AN ORDER OF MAGNITUDE IS A FINDING ABOUT THE MODEL, NOT A
REASON TO ABANDON IT.** A331's ablation balance, run forwards with the energy silica phenolic can
absorb, predicts 65.9 millimetres of recession over a burn that real chambers survive. **Inverting it
from the recession such chambers actually show recovers an effective heat of ablation four and a half
times larger**, and the gap is the transpiration blocking that the absorption model omits. **The
error located the physics.** Do not delete a calculation that fails; ask what its failure measures.

**ONLY ONE ROW OF A COMPARISON TABLE MAY COMPARE EQUALS, AND SAYING WHICH IS THE DIFFERENCE BETWEEN A
RESULT AND A MISLEADING ONE.** A330 nearly shipped a sandwich mass table whose later rows compared
walls of increasing stiffness as though they were alternatives. **Only the equal-stiffness row is
like for like**, where the saving is 1.72 times; at a thirty millimetre core it is 1.13 and beyond
40.6 millimetres the sandwich is heavier. The table now labels which row compares equals.

**INVERT FOR THE THRESHOLD RATHER THAN ESTIMATE THE INPUT.** A330 needed to know whether buckling or
pressure sized the tank wall and did not need the compressive load. Setting the two thicknesses equal
and solving gives **a threshold line load of 7.54 kilonewtons per metre**, and the only thing that
then has to be established is that the vehicle clears it, which thrust alone does by a factor of
seven. **The conclusion needs the input to clear a bar, not to be known.**

**A CONCLUSION THAT SURVIVES ITS OWN CORRECTION IS WORTH FAR MORE THAN ONE THAT NEEDED THE ERROR.**
A330's buckling section first omitted that internal pressure stabilises a shell, which was an error
in the article's favour. Including it cut the thickness ratio from 2.64 to 1.80 **and the conclusion
held**, which is a stronger statement than the original.

**A RELATION SHOWN FOR ITS STRUCTURE MUST BE FLAGGED WHEN IT IS CIRCULAR.** A331 displays the
factorisation of specific impulse into a chamber term and a nozzle term, and it returns the published
impulse exactly, **because the throat area was derived from that same impulse.** The article says so
at the point of use. **Presenting a construction as a confirmation is the easiest dishonesty in
technical writing and nothing in the toolchain catches it.**

**A BINDING QUANTITY NEED NOT BE PHYSICAL, AND WHEN IT IS NOT, SAY SO FIRST.** A331's keystone is
cost, which has no units, no conservation law and no instrument, and every number attached to it is a
forecast rather than a reading. **The article opens by admitting that** and then prices the physical
fingerprints the cost argument left, which is the only honest route into such a subject.

**AN IDENTITY THE ARTICLE HAS ALREADY ASSEMBLED WITHOUT NOTICING IS THE CHEAPEST RESULT AVAILABLE,
AND A329 FOUND ONE.** Momentum theory gives the disc loading as twice rho times the induced velocity
squared, and the far field runs at twice the induced velocity, so **the dynamic pressure in the jet
IS the disc loading, exactly**. The article was already printing a table of disc loadings and had
not noticed it was also printing the pressure each architecture puts on the ground. **Before adding
a calculation, check whether a quantity already computed answers a second question.**

**A QUANTITY THAT IS A SMALL DIFFERENCE BETWEEN TWO LARGE NUMBERS IS BADLY CONDITIONED AND SAYING SO
IS THE RESULT.** A329's bring-back allowance is lift over a margin minus empty weight, and it
amplifies a one percent thrust change into a ten percent change in what the aircraft can carry home.
**Report the conditioning rather than the amplification factor**, because the factor blows up as the
allowance approaches zero and quoting it as a precise number misrepresents a genuine singularity.

**REPORT THE QUANTITY THAT ASSUMES NOTHING, THEN TEST THE ONE THAT DOES.** A329's central number
rests on an unpublished STOVL lift, so the article gives a sensitivity table across the plausible
range and shows that no value inside it produces a comfortable answer. **A conclusion that survives
its own sensitivity table is worth more than one that needs a particular assumption.**

**A BOUND-FREE IDENTITY BEATS A RECONSTRUCTION AND A328 LEARNED IT BY BUILDING THE RECONSTRUCTION
FIRST.** The integer search for the kill counts behind published exchange ratios was under-determined
and its answers were facts about the search bound. **The weighting identity, that a pooled ratio is
the loss-weighted mean of the per-condition ratios, needs no counts at all**, and the bracket derived
from it is what the article actually rests on.

**SOLVE FOR THE THRESHOLD, NOT ONLY FOR THE VALUE.** A328 inverted its identity for the weight that
would drive the pooled ratio to PARITY rather than to the published figure, got 92.14 percent, and
found that **the threshold lies INSIDE the bracket the same identity had already established**. The
published claim of an advantage is therefore not robust to a quantity nobody published, and the
article could not have said that before asking the inverted question.

**A RELATION CAN EXPLAIN A SENTENCE IN THE SOURCE THAT READS AS A CORRECTION OF ITSELF.** A328's
programme described its advantage as an apparent directional nose-pointing rate which is "in
actuality" yaw rate. Writing down the wind-axis kinematics shows that **at seventy degrees a roll
about the velocity vector is 94.0 percent yaw rate**, so the two are the same manoeuvre and the
source was not correcting itself but describing one thing twice.


**AN IDENTITY THE QUANTITY MUST SATISFY IS WORTH MORE THAN A SECOND OPINION.** A327's Rayleigh
choking relation was missing a factor of gamma plus one on the fourth-power term, and no amount of
re-reading would have shown it. **The Rayleigh ratio must be EXACTLY unity at Mach one**, because that
is the definition of the sonic reference state, and the wrong form returned 1.108. One line of test
found what inspection could not.

**AN ARITHMETIC LINE THAT DOES NOT EVALUATE TO ITS OWN STATED ANSWER IS THE EASIEST DEFECT TO SHIP.**
A327 displayed a substitution reading 220.6 times 13.8 equals 3,086. The true static temperature is
223.7 and the product of the numbers as written is 3,044. **Both figures look reasonable in isolation
and the line is wrong on its face**, which is exactly why nobody notices.

**A GUARD CAN BE TOO STRICT AND SILENTLY REMOVE THE CASE YOU NEEDED.** A327's Rayleigh function
rejected subsonic entry as an error, which is precisely the ramjet case its comparison existed to
make. The relation holds on both branches and only the sonic point is inadmissible.

**A CONFIDENT ANSWER THAT MOVES WITH AN ASSUMPTION IS A FINDING ABOUT THE ASSUMPTION.** A327 searched
for the speed at which net thrust reaches zero, found 16,577 metres per second, and nearly reported it
as a ceiling set by chemistry. **In an ideal engine net thrust never crosses zero.** The crossing moves
to 8,880 at a nozzle efficiency of 0.90 and vanishes at 1.00. Report the quantity that assumes nothing,
which there was the loss budget.

**A BOUND THAT OWES NOTHING TO THE MODEL IS THE BEST CHECK ON THE MODEL.** A327's ascent integration
gives a propellant fraction of 45.44 percent, and thermodynamics alone puts the floor at 26.9. The
integrated answer sits 1.69 times above it. **A result below the bound would have been proof of an
error**, and nothing else available could have said so.

**A CLEAN CLOSED FORM THAT LANDS NEAR A MEASURED NUMBER IS NOT AN EXPLANATION OF IT.** A326 wrote
1/(1 - r) for the Southwell sensitivity, which is tidy and gives 1.600 against a simulated 1.389. They
are different estimators. **The closed form was deleted rather than displayed.**

**THE QUADRATIC TERM MAY BE IDENTICALLY ZERO AND FLOATING POINT WILL NOT TELL YOU.** A326's two-mode
divergence eigenvalue has an exactly vanishing quadratic coefficient, so the characteristic equation is
linear. The residue is sixteen orders below the terms that cancelled and still enormous in absolute
terms, so **an absolute tolerance cannot catch it**. The test must be relative to what cancelled.

**A COARSE SCAN QUANTISES ITS ROOT TO THE GRID STEP.** A326's determinant scan produced apparent
disagreements of up to 0.31 percent that were entirely the grid. Bracket, then bisect.

**A DISCREPANCY NEAR AN ORDER OF MAGNITUDE IS A HINT THAT THE CHECKER IS AT FAULT, exactly as a
suspiciously clean factor is.** A324's Breguet carried a spurious factor of g and produced a combat
radius of 27 nautical miles against a claimed 367. That looked like a devastating finding about the
brochure and was a defect in the checker. **Corrected, the claim survives.**

**A TOLERANCE WIDER THAN THE QUANTITY IT CHECKS IS NOT A CHECK.** A324's specific-excess-power peak was
computed on a four-point grid and reported 1.5 percent low. The verifier passed it because its tolerance
on that value was three percent. **Set the tolerance from the quantity's own sensitivity, not from
habit.**

**A CHECKER THAT CAN PRINT FREE ENERGY IS NOT CHECKING.** A324's cone search ran to its bound and
returned a total-pressure recovery of 1.227. Guard the physically impossible explicitly rather than
trusting the search to stay inside it.

**THE ARITHMETIC CAN BE RIGHT AND THE PREMISE WRONG, AND THAT IS THE COMMONER FAILURE.** A324 converted
maximum CORRECTED airflow to physical flow at Mach 2.6 and got three times the sea-level rating. A325's
climb inversion returned a zero-lift drag of 0.0050, a quarter of a clean sailplane's. **In both cases
nothing was wrong with the algebra.** Ask which input is not what the table says it is.

**WHEN TWO PUBLISHED FIGURES CAN BE CONNECTED BY GEOMETRY NEITHER WAS DERIVED FROM, DO IT.** A324's
strongest result reconciles four inches of quoted spike travel with 260 pounds per second of quoted
airflow through a cone angle nobody published, to 4.2 percent. **That is the closest an aeroplane which
never existed can come to leaving a measurement behind.**

**AN INEQUALITY CAN BE BACKWARDS AND STILL LOOK CONSERVATIVE.** A325's sweep-width function returned more
than twice the sighting range and was described in its own docstring as conservative. Sweep width is the
integral of the lateral-range curve and **can never exceed twice the definite range**. Check the
direction of every bound, not only its presence.

**A COMPARISON THAT GIVES EVERY CANDIDATE THE SAME SENSOR IS NOT A COMPARISON.** A325 first gave a P-3C
and an X-28A the same sweep width, which flattered the small aircraft enormously. **The conclusion
survived a fair comparison and the first version did not deserve to.**


**Write the relation down.** This has now caught a wrong claim in eighteen articles.

**A CLEAN FACTOR IS A HINT THAT THE CHECKER IS AT FAULT, AND IT FIRED AGAIN IN A323.** A scaling law
for observability disagreed with the worked cases by **exactly two**, which was the ratio of the two
aircraft's assumed directional stiffness, omitted from the scaling. **Corrected, the helix angle
cancels out entirely**, which is a better result than the one being checked.

**WHEN A PARAMETER IS UNKNOWN, INVERT THE RELATION RATHER THAN ASSERT A PREDICTION.** A323 claimed a
stall speed of 45.9 mph from an assumed maximum lift coefficient and was wrong by five miles an hour.
Replaced by asking what the **quoted** stall implies, which is 1.11 at light weight against 1.47 at
gross, **the inversion became a third independent piece of evidence** that the quoted figures belong to
a lighter aircraft. **The error produced a better finding than the claim would have.**

**A MODEL WITH TWO FREE PARAMETERS THAT LANDS WITHIN SEVEN PERCENT HAS DEMONSTRATED VERY LITTLE.** Say
so. A323 reports its glide-ratio agreement and then says exactly this, and points at the weight
reconciliation instead, which resolved an apparent conflict rather than confirming an expectation.

**REPRODUCING TWO INDEPENDENT QUOTED FIGURES FROM ONE MODEL IS WORTH FAR MORE THAN EITHER ALONE.**
A323's polar reproduces both the glide ratio and the minimum sink rate with no further fitting.

**IF A CURVE IS CALIBRATED BACKWARDS OUT OF ONE OBSERVATION, IT REPRODUCES THAT OBSERVATION BY
CONSTRUCTION AND NOT BY PREDICTION.** Say which. A323's acoustic detection table does exactly this and
says so, and reports the **sensitivity** as the finding instead.

**A RESULT THAT COMES OUT NEGATIVE IS STILL A RESULT.** A322's spin-up energy objection, the first
thing anybody reaches for against that concept, **does not survive being written down**. Reported as a
negative rather than dropped.

**THE VERIFIER CAN BE RIGHT AND KILL A FINDING YOU LIKE.** It has now done so in A321, A322 and A323.

**A NUMBER THAT IS NOT CREDIBLE IS A FINDING, NOT A NUISANCE.**

**A named limit belongs in the article**, including the boundary of the model's own validity and
**why a term is neglected**. A323 tabulates atmospheric absorption purely to show that neglecting it is
a statement rather than a gap.

### On harvesting and selection

**A THIN CLUSTER IS A CLAIM ABOUT THE ORDERING BEFORE IT IS A CLAIM ABOUT THE LITERATURE, AND A335 HAD
TWO.** `vehicle_sizing` measured ZERO and `entry_aerothermo` measured FOUR. Neither was a gap. Both sat
behind clusters that matched their records first, since the matcher returns the first match and an
entry-trajectory cluster takes the bare `re-entry` stem. **Correcting the order took the second from 4
to 21 with no harvesting at all.** Check the order before harvesting for an empty cluster.

**THE MEASURING INSTRUMENT HAS THE SAME BLIND SPOT AS THE SEARCH, AND THIS IS THE THIN-HEADING RULE ONE
LEVEL UP.** A334's subject audit was written in the ARTICLE's vocabulary while the harvest asked in the
LITERATURE's, so a well-supplied subject measured zero. **Three of the largest apparent gaps closed on
the instrument and not on the pool**, equilibrium glide going 3 to 18 and crossrange 4 to 11 **with no
new records found in either case.** Write the audit patterns in the field's words from the outset.

**AND THE SHARPEST CASE OF ALL IS WHEN THE THIN HEADING IS THE ARTICLE'S OWN LOAD-BEARING ASSUMPTION.**
A335's canopy lift coefficient measures ONE record. It is not thin. The papers that measure it are
titled as aerodynamic characterisations, and the parafoil cluster holds 142 including a 1964 study of
the parafoil glider and a 1971 report of parafoil wind tunnel tests. **Check what the cluster actually
contains before reporting a gap.**

**A SPELLING VARIANT IN AN ANCHOR RETURNS A SMALLER CORPUS RATHER THAN A WRONG ONE, WHICH IS WHY IT
SURVIVES PASSES. THIS IS NOW SIX INSTANCES.** A335's `ram-?air` matched `ramair` and `ram-air` and
**not `ram air`**, which is how most of the decelerator literature writes it. Correcting it took the
selection from 1,680 to 1,818. Earlier instances were `Diffusers`, `area rules`, `installation
effects`, `airship hulls` and British against American manoeuvrability.

**TYPOGRAPHIC PUNCTUATION MUST BE NORMALISED BEFORE THE GATE MATCHES, NOT ONLY BEFORE LINK TEXT IS
BUILT.** A334 refused "Thermal Characteristics of a Nickel-Hydrogen Battery" because the depositor wrote
the hyphen as U+2010, and nickel-hydrogen is one of that article's strongest anchors. `refs.clean` had
normalised for link text since A332. **The gate needed the same and did not have it.** Both A334's and
A335's selection scripts now carry a `normalise` step and it should be copied forward.

**WIDENING HAS A PRICE AND A335 PAID IT IN SIX FAMILIES AT ONCE.** Reading the kept sample after the
primary harvest found surgical reefing in orthopaedics, the parachute metaphor in clinical writing,
probabilistic risk assessment outside aerospace, the air-refuelling drogue, the parachute flare written
with its words separated, and the parachute problem as a differential-equations exercise. **All six are
in `_research/homonyms.py` with the incident that produced each.**

**THE PROMOTION RULE FIRED WITH SIX SUBJECTS AT LITERALLY ZERO IN A331, WHICH IS THE STARKEST YET AND
THE TWELFTH ARTICLE RUNNING.** Of the seventeen subjects that article's equations name, thirteen were
thin and six stood at zero, **including the convective heat transfer correlation the article displays
and the effective heat of ablation it inverts for.** Audit the equations against the pool BEFORE the
primary harvest, not after.

**A SUBJECT CAN BE THIN FOR A THIRD REASON AND IT IS INVISIBLE TO A COUNT.** Either the work was never
done, or the heading is wrong, **or the knowledge is so settled that it stopped generating papers.**
A331's search for the rocket equation and the ascent loss budget returned NOTHING in a pool of four
thousand three hundred, after a harvest aimed directly at them, because both live in every textbook
and in no journal article. **Report that rather than padding, and name which of the three kinds it
is.**

**THE COUNT-VERSUS-FRACTION TRAP CAUGHT TWO CONSECUTIVE ARTICLES AT BOTH ENDS IN CONSECUTIVE PASSES,
WHICH MAKES IT STRUCTURAL RATHER THAN ACCIDENTAL.** In both A330 and A331 the primary pass raised the
contemporary COUNT slightly while dropping its FRACTION by nine to twelve points, and the
contemporary pass then left the period COUNT completely unmoved while dropping its fraction by
seventeen or eighteen. **The report literature is the clearest case in both, holding at exactly 1,692
and exactly 884 records while its share fell.** The four-pass rhythm produces this. **Reporting both
numbers is not optional and both articles carry all three columns.**

**A CANCELLED PROGRAMME STOPS GENERATING LITERATURE UNDER ITS OWN NAME, AND TWO INSTANCES MAKE IT A
PATTERN.** The X-33 cluster holds sixty records and every one predates 2002. The X-34 cluster holds
its records and every one predates 2002. **The documentary trace of a vehicle measures how long it
survived rather than what it contributed**, and that belongs in the closing article.

**WIDENING AN ANCHOR TO REACH ONE GOOD RECORD HAS A PRICE THAT ARRIVES IMMEDIATELY.** A330 admitted
`multicell` to reach the 1965 juncture-stress reports on multicellular shells and simultaneously
admitted an eleven-volume FLUIDIZED BED BOILER programme and a nickel-hydrogen BATTERY common
pressure vessel, seventeen records in all. **Pay it at the moment of widening.**

**THE LITERATURE FOR A TERM AN ARTICLE DECLINES TO COMPUTE MAY BE DECADES OLDER THAN THE VEHICLE.**
A330's mass build-up leaves the lobe-junction bending unaccounted, and a 1965 report series on
juncture stress fields in multicellular shell structures is exactly that subject, with a
two-hundred-inch multicell tank pressure tested in 1968. **The knowledge was thirty years old when
the X-33 was designed**, which turns an omission into a choice of model.

**THE NASA REPORTS SERVER CAPS A SEARCH AT TEN AND REWARDS SPECIFICITY, SO A BROAD QUERY RETURNS TEN
RECORDS AND A NARROW ONE RETURNS TEN DIFFERENT RECORDS. THIS IS NOW THE MOST RELIABLE HARVEST RULE
IN THE SERIES AND IT FIRED TWICE IN A ROW.** A328 sat at 252 NTRS records for a programme NASA
documented extensively until roughly a hundred and seventy narrow questions took it past five
hundred. A329 sat at 186 for a subject NASA researched for thirty years, and a hundred and forty
narrow questions more than doubled it. **Ask many narrow questions from the outset.**

**A DATE FILTER OMITTED FROM A CONFERENCE HARVEST MAKES IT A MODERN HARVEST.** A328's conference
round took no date filter and was dominated by recent work, leaving the vehicle cluster at eighteen
while the two keystone papers sat in the registry unqueried. **Restricting the same publisher prefix
to the programme window reached the papers the programme's own engineers wrote.**

**AN ERA CAN BE THIN WHERE NEITHER THE HEADING NOR THE SUBJECT IS, AND THIS IS A NEW VARIANT.** A328
found thirteen cluster-and-era pairs short of what the draft cited and **twelve were the MODERN
half**, because the harvests had asked the modern pool only for obviously modern subjects. A329 hit
the mirror image, where a primary pass raised the period count and left the contemporary fraction to
fall underneath it. **Measure both halves after every reference pass.**

**A HOMONYM INTERNAL TO AN ADJACENT ENGINEERING DISCIPLINE IS THE MOST DANGEROUS KIND, AND A329
FOUND ONE NOBODY PREDICTED.** "Hot gas ingestion" is also a turbomachinery subject describing sealing
flows between a turbine rotor disc and its stator, using the identical phrase. **The pool held 82
titles containing "hot gas" and only 44 belonged to the article.** Found by reading the discarded
records, not by anticipation.

**A CONTRACTION INSIDE A VERBATIM CITATION TITLE COLLIDES WITH THE PROSE RULES AND THE RECORD IS
DROPPED.** Link text is prose under the corpus rules and a published title cannot be rewritten.
A328 and A329 each hit exactly one, and both were dropped rather than weakening the corpus-wide
checker. **One record in several thousand is the right price.**


**AN EQUATION PASS PROMOTES SUBJECTS AND THIS IS NOW TEN ARTICLES RUNNING, WITH A NEW CAUSE NAMED IN
A327.** The mechanics beneath an equation are not the same literature as the technology above it. The
original harvest asked for forward sweep, tailoring and digital flight control, and never for
Rayleigh-Ritz, the Southwell method or lift-curve slope estimation. A327 asked for scramjets and
never for inlet starting, mass capture or the energy required to reach orbit. **Three of A327's ten
promoted subjects stood at ZERO in a pool of four thousand records.**

**THE KEYSTONE CLUSTER HAS NOW BEEN THIN SEVEN ARTICLES RUNNING AND A327 WAS THE STARKEST.** Searching
the entire 2,333-record pool for "specific impulse", "ram drag", "net thrust" and "thrust margin"
returned **zero titles**. The field says FORCE ACCOUNTING, THRUST MINUS DRAG, INSTALLED PERFORMANCE and
CYCLE ANALYSIS. A second harvest in that vocabulary took the cluster from 2 to 32.

**THE ANCHOR GATE CAN SILENTLY NARROW EVERYTHING, AND THIS IS A NEW VARIANT OF THE WORD-BOUNDARY
FAMILY.** A326 wrapped its whole alternation in a LEADING AND TRAILING boundary, which forces every
stem meant as a PREFIX to match as a whole word. `structur` failed on "structural", `buckl` on
"Buckling", `stabilit` on "stability", `flying qualit` on "flying qualities". **A false negative from
an EXTRA boundary, not a false positive from a missing one.** Separate WORDS, which keep both
boundaries, from STEMS, which keep only the leading one.

**HARVESTING A RECORD AND NEVER CITING IT IS DOING THE WORK AND THROWING IT AWAY.** A327 had 249
records sitting uncited because the article carried a marker for the period half of several clusters
and none for the modern half, and one cluster had no marker at all. **That is bookkeeping, not
research.** Check for uncited master records before every commit; it is one line.

**AN EQUATION PASS PROMOTES SUBJECTS AND THE REFERENCE BASE MUST FOLLOW. THIS IS NOW EIGHT ARTICLES
RUNNING AND IT HAS A NEW CAUSE.** In A324 and A325 the promoted subjects were not merely thin, they were
**being discarded entirely as "no cluster"**, because no cluster existed for them when the first harvest
was written. **That is the thin-heading rule arriving from the opposite direction**: a heading so thin it
does not exist, over a subject the pool partly holds.

**A CLUSTER PLACED AFTER A BROADER ONE NEVER SEES ITS OWN RECORDS**, because the matcher returns the
first match. Both A324 and A325 hit this, and A325 hit it twice, the second time created by the fix for
the first. **Put specific clusters first, and re-check the counts after any broadening.**

**WIDENING AN ANCHOR LIST HAS A PRICE AND IT ARRIVES IMMEDIATELY.** A324 admitted `propulsive` to rescue
"Propulsive efficiency from an energy utilization standpoint" and admitted "the propulsive efficiency of
single-screw supertankers" in the same run. **Pay it at the moment of widening rather than in the URL
sweep.**

**A FILTER EARNED IN ONE ARTICLE IS NOT AUTOMATICALLY VALID IN THE NEXT, AND A325 WITHDREW ONE
DELIBERATELY.** A324 filtered the ship hull as marine noise. For a flying boat the ship hull is the same
physics and is adjacent rather than noise. **Read the inherited filters before carrying them forward.**

**PROXIMITY REQUIREMENTS IN CLUSTER PATTERNS ARE A TRAP.** A325 required "flying boat" within forty
characters of "hydrodynamic" and rejected 86 NACA tank tests whose titles put the two ends ninety
characters apart. **The anchor gate has already established the record is on-subject; the cluster test
does not need to re-establish it.**

**PLURALS FAIL SILENTLY.** A324's cluster patterns missed "Diffusers" and "area rules". Same class as the
word-boundary bugs of the three articles before it.

**REPORT A GENUINELY THIN SUBJECT RATHER THAN PADDING IT, AND SAY WHERE THE WORK ACTUALLY LIVES.** A324
found thirteen records for ram drag and seven for energy height in 6,518 harvested. **The subjects are
not thin, the headings are**: ram-drag bookkeeping lives inside inlet additive-drag papers, energy height
inside trajectory optimisation.


**THE KEYSTONE CLUSTER HAS NOW BEEN THIN FIVE ARTICLES RUNNING. THIS IS THE MOST RELIABLE RULE IN THE
SERIES.** A319 ducted fans, A320 crossrange at 8 records, A321 unpowered landing at 12, A322
autorotation, A323 **adverse yaw at 7 records, which reached 48** once the queries used the 1930s
vocabulary of aileron yawing moment and lateral control research.

**AND THERE IS A SECOND VARIANT THAT IS NOT CURABLE BY REPHRASING.** A322's keystone was thin on
**primary fraction** rather than on count, at 32 percent. The cause was a vocabulary that spans **both**
eras, so the query matched happily in both directions and the larger, better-indexed modern literature
crowded the period out. **The query succeeded and the balance failed.** Two harvests naming the period
reports moved it five records and stopped. **The pool was itself 31 percent primary and every primary
in it was cited**, which is the proof that it was supply and not selection.

**AUDIT THE POOL AGAINST THE ARTICLE'S TOPIC LIST BEFORE WRITING, NOT AFTER.** A322 did this first and
found four topics at zero that its own equations needed. It costs one script and saves a rewrite.

**AN EQUATION PASS PROMOTES SUBJECTS AND THE REFERENCE BASE MUST FOLLOW. SIX ARTICLES RUNNING.** A322
had nine thin with two at zero. A323 had **eight of eleven at or near zero**, the worst being *adding
noise sources* at zero while carrying the article's sharpest acoustic claim, and the second worst *the
drag polar* at one, which is the relation both halves of that article rest on.

**A THIN HEADING IS NOT THE SAME THING AS A THIN SUBJECT.** A322's stored-rotor-energy cluster stood at
one record, and the work existed and was cited **inside the autorotation literature**, because a paper
on autorotative landing is a paper about spending exactly that energy. **Check before reporting a gap.**

**REPORT A TOPIC THAT IS GENUINELY THIN RATHER THAN PADDING IT.** A322's spin-up literature is three
records after a harvest aimed at it.

**A FILTER EARNED IN ONE ARTICLE IS NOT AUTOMATICALLY VALID IN THE NEXT, AND THIS CUTS BOTH WAYS.**
A322 had to **admit** wind turbines and samaras, because autorotation is the windmill brake state.
A323 had to **withdraw** both and then explicitly **re-exclude** wind turbines, because the turbine
noise literature shares propagation and psychoacoustics with a fixed-wing acoustics article. **Read
the inherited filters before carrying them forward.**

**ANTICIPATING HOMONYMS BEFORE WRITING BEATS REPAIRING AFTERWARDS.** A323 anticipated five families,
including the warship in the aircraft's own name, and its first cited set came back with **one**
contaminant, by far the cleanest first pass the series has had.

**BUT READING THE URL SWEEP STILL FINDS WHAT ANTICIPATION MISSES.** It found ship roll damping,
audiology, marine snow and startle, none of which were predicted.

**MY OWN SCANNING PATTERNS HAVE NOW BEEN WRONG SIX TIMES ACROSS THREE ARTICLES AND ALWAYS THE SAME
WAY.** `EVA` inside `EVALUATION`, `train` inside `training`, `crop` inside `microphone`, `tire` inside
`entire`, `IoT` inside `Elliott` and `radiotechnical`. **Word boundaries by default in every scanning
pattern.** Twice the false report was large enough to look like a real finding.

**THE PERSISTED REJECTION LIST IS AT `tmp/aNNN/read_and_dropped.json`, NOW 721 ENTRIES, AND MUST BE
CARRIED FORWARD. KEY IT BY URL AS WELL AS BY ANCHOR**, because disambiguation suffixes shift when an
earlier record is removed.

### The homonym table

**THIS IS THE DOMINANT FAILURE MODE AND THE LIST NOW RUNS PAST FORTY.** The most dangerous are internal
to the discipline or inside the article's own vocabulary.

| Phrase | The other field |
|---|---|
| **divergence** | **THE KEYSTONE WORD OF A326 AND ITS WORST HOMONYM.** The vector operator, the Kullback-Leibler divergence, beam divergence, evolutionary divergence, and economic divergence |
| **orbit** | **THE ORBIT OF A GROUP ACTION in pure mathematics**, the atomic orbital, and the orbit of the eye |
| **short period** | **geomagnetic secular variation, meteoroid streams, crustal dynamics and superlattices.** Not predicted, and it arrived from one control-theory phrase |
| **energy budget** | **oceanography and meteorology.** Internal waves in the South China Sea, stratospheric budgets, surface energy balance. Not predicted |
| **isolator** | the ELECTRICAL and VIBRATION isolator. The scramjet isolator is a duct |
| **bridge** | **THE STRAIN-GAUGE BRIDGE, and A326 carried eighteen at every load station.** Cannot be filtered bare |
| **building** | **THE BUILDING-BLOCK APPROACH to composite certification**, a term of art. Cannot be filtered bare |
| **transition** | phase, energy, democratic, demographic and nutritional transition, against the boundary-layer one |
| **hydrogen** | the hydrogen ECONOMY, storage and fuel cells. **Embrittlement is legitimate** where tanks are metal |
| **enthalpy** | chemical thermodynamics generally |
| **descent** | **THREE senses.** Gradient descent in optimisation; **descent groups in kinship anthropology**, which put four papers on ancestor worship in A322; and the aeronautical one |
| **rotor** | **turbomachinery**, where it is a compressor blade row, which was A322's largest single contaminant at 44 records. Also the electrical machine rotor and the meteorological mountain rotor |
| **frigate** | **the warship, inside an aircraft's own name.** Also the frigatebird |
| **roll damping** | **naval hydrodynamics.** Ships roll, it is a major subject, and **those papers never say frigate**, so a warship filter does not catch it |
| **height-velocity** | **paediatric growth.** Peak height velocity in children |
| **training requirements** | **a Defense Technical Information Center term of art for personnel documents of any kind.** Army battalions, peacekeeping, Ada software education |
| **startle** | **fear conditioning in psychology**, with its own anxiety literature |
| **acoustic reflex, acoustic impedance** | **audiology.** A middle-ear muscle contraction |
| **sinking speed** | **oceanography.** Marine snow, the descent of organic aggregates |
| **flare** | the solar flare, the gas flare, and **the illumination flare, a parachute-suspended munition** |
| **ballistic** | **three senses**, and the ballistic RANGE is legitimate and must not be filtered |
| **canopy** | the forest canopy |
| **parachute** | the golden parachute, corporate governance |
| **observation** | astronomical and Earth observation, and the control-theory observer |
| **surveillance** | epidemiological surveillance |
| **noise** | electronic noise. **Filter it without taking the acoustic sense with it** |
| **coupling** | mechanical, quantum and coupled oscillators |
| **escape** | escape velocity and atmospheric escape |
| **flywheel** | **energy storage for spacecraft and grids.** A homonym A322 created for itself |
| **speed of sound** | solutions and acoustics. A homonym A320 created for itself |
| **wind turbines** | **CONTEXT DEPENDENT.** Legitimate for autorotation, excluded for fixed-wing acoustics |
| **samara** | **legitimate for autorotation**, excluded elsewhere |
| **unmanned ground vehicle** | shares nearly every acronym with the aerial one |
| **energy management** | power grids and buildings |
| **reentry** | agriculture, the interval before workers re-enter a field |
| **bioacoustics** | birdsong and whale-song classification |
| the electric road vehicle | the largest body this series has had to exclude |
| boundary layer control, trim, figure of merit, electric propulsion | **aeronautics itself** |

| **exchange ratio** | **THE KEYSTONE PHRASE OF A328.** The share-swap ratio in mergers and acquisitions, ion exchange in chemistry, gas exchange in physiology. The finance literature alone is larger than everything the article cites |
| **agility** | **AGILE SOFTWARE DEVELOPMENT and ORGANISATIONAL AGILITY**, plus physical agility in sports science |
| **engagement** | employee, student, civic and customer engagement. Very large |
| **competition** | **THE KEYSTONE WORD OF A329.** ECOLOGICAL competition between species and ECONOMIC competition between firms, both dwarfing the procurement sense |
| **hot gas ingestion** | **TURBINE RIM CAVITIES, and this is the most dangerous kind because it is INTERNAL TO AN ADJACENT ENGINEERING DISCIPLINE.** Sealing flows between rotor and stator use the identical phrase. Dust, particle and salt ingestion join it. **BIRD ingestion is LEGITIMATE and must not be filtered with them** |
| **ingestion** | dietary and toxicological ingestion in medicine |
| **acquisition** | **LANGUAGE acquisition and DATA acquisition**, both very large, against the procurement sense |
| **selection** | natural selection, selection bias, feature and model selection |
| **scheduling** | **JOB-SHOP AND FLOW-SHOP SCHEDULING in operations research**, admitted by the `schedul` stem written for GAIN scheduling |
| **ISA** | **A HOMONYM CREATED BY THE AUTHOR.** The International Standard Atmosphere abbreviation matches the journal ISA Transactions, and because the cluster test runs against title AND venue, every paper in it landed in the atmosphere cluster |
| **ground effect** | the GROUND-EFFECT VEHICLE, and the electrical ground |
| **lift** | the ELEVATOR in British usage, and lifting in ergonomics |
| **stall** | **THE COMPRESSOR STALL IS LEGITIMATE and adjacent**, against the market and economic senses |
| **maneuver** | **MEDICAL MANOEUVRES**, the Valsalva, Epley and Heimlich, plus road-vehicle lane changes |
| **utility** | utility functions in economics and electric utilities |
| **vane** | the turbomachinery guide vane, adjacent, and the anemometer vane |
| **Herbst** | a common German surname, so a manoeuvre's name collides with an author name in every field |
| **duel** | **GAME-THEORY DUELS ARE LEGITIMATE and adjacent** to one-versus-one air combat |

| Phrase | The other field |
|---|---|
| **phenolic** | **PLANT POLYPHENOLS in food and agricultural chemistry, and the worst word A331 met.** Silica phenolic is a heat shield and the food literature owns the word |
| **transpiration** | **PLANT TRANSPIRATION and EVAPOTRANSPIRATION in agronomy and hydrology.** The cooling sense is a boundary-layer term and the agricultural one is enormous |
| **lobe** | **THE KEYSTONE WORD OF A330.** The brain, lung, liver and thyroid lobe, plus the ANTENNA sidelobe. Five literatures, one word |
| **core** | **THE REACTOR core, the EARTH's core, the ICE core, core-shell nanoparticles and the CORE COMPETENCY of a firm.** Probably the worst word in A330, because it is also exactly right |
| **recession** | **THE ECONOMIC RECESSION**, larger by orders of magnitude than the ablation sense, plus gum recession in dentistry |
| **erosion** | **SOIL AND COASTAL EROSION**, and dental erosion |
| **pyrolysis** | **BIOMASS AND WASTE PYROLYSIS**, which uses char, tar and volatiles exactly as the ablation literature does |
| **ablation** | CARDIAC and LASER ablation in medicine, and **GLACIER ablation**, where it is also a mass-loss rate |
| **spike** | the NEURAL spike train and, **INTERNAL TO THIS DISCIPLINE, the AERODYNAMIC SPIKE on a blunt body.** An aerospike is two different things in aerospace |
| **tank** | **THE ARMOURED FIGHTING VEHICLE**, which Defense Technical Information Center records make an active hazard |
| **honeycomb** | **THE HONEYCOMB LATTICE of graphene**, which uses the word as a structural adjective exactly as a sandwich article does |
| **microcracking** | CONCRETE, rock mechanics, asphalt and dental enamel |
| **delamination** | **LITHOSPHERIC delamination in geophysics** |
| **knockdown** | **GENE KNOCKDOWN in molecular biology**, sharing the exact word with the buckling allowable |
| **gauge** | **GAUGE THEORY in physics** and the RAILWAY gauge, against minimum gauge in structures |
| **multicell** | **AN ELEVEN-VOLUME FLUIDIZED BED BOILER PROGRAMME** and the nickel-hydrogen battery common pressure vessel. Self-inflicted by widening |
| **shell** | **A QUANTUM FIELD THEORY OBJECT.** One Casimir self-stress paper reached A330's structures cluster |
| **RP-1, MC-1** | **GENE AND RECEPTOR NAMES.** RP1 is a retinitis pigmentosa gene and MC1R the melanocortin receptor, so both engine designations collide with molecular biology |
| **blowing** | the BLOWING AGENT in polymer foams, against blowing into a boundary layer |
| **wrinkling** | **SKIN WRINKLING in dermatology and cosmetics**, against face wrinkling in sandwich panels |
| **peel** | the DERMATOLOGICAL and FRUIT peel, against climbing drum peel |
| **health monitoring** | **HUMAN health monitoring**, which dwarfs the structural sense |
| **blanket** | the FUSION BREEDING blanket and the bedding one |
| **redundancy** | **EMPLOYMENT redundancy in British usage** |
| **drop test** | PACKAGING and consumer electronics drop testing |
| **kerosene** | the KEROSENE LAMP and its public-health literature |
| **star, venture** | astronomy and venture capital, which is why VentureStar is not a usable query term |
| **vehicle** | **THE ROAD VEHICLE.** A331's catch-all admitted automotive software and electric city cars on this one word |
| **condensation, separation** | chemistry, condensed matter and building physics; psychology and chemical engineering |

| Phrase | The other field |
|---|---|
| **effector** | **THE BIOLOGICAL EFFECTOR, and the worst word A333 met.** Effector proteins in immunology and in plant-pathogen interaction are a very large and very active literature that owns the word outright. A CONTROL effector is the article's term of art and cannot be filtered bare |
| **figure of merit** | **THERMOELECTRICS AND PHOTONIC SENSING, and this is a homonym on the article's OWN term.** A contemporary search for hover efficiency returns solar cells and graphene sensors, and those records reached A332's momentum-theory cluster |
| **clutch** | **THE CLUTCH OF EGGS in ornithology and evolutionary ecology**, where clutch SIZE is a central measured quantity, plus CLUTCH PERFORMANCE in sports psychology. A332's transition argument rests on the mechanical clutch, so the word cannot be excluded |
| **fountain flow** | **POLYMER INJECTION MOULDING, which describes the advancing melt front with the identical phrase.** Internal to an adjacent engineering discipline, which is the most dangerous kind |
| **impingement** | **SHOULDER AND FEMOROACETABULAR IMPINGEMENT in orthopaedics.** Jet impingement cooling is legitimate and adjacent and must not be filtered with it |
| **augmentation** | **DATA AUGMENTATION in machine learning**, now enormous, and BREAST AUGMENTATION in surgery. Thrust augmentation is A332's own term |
| **thrust** | **THRUST FAULTS AND THRUST BELTS in structural geology** |
| **variant** | **THE GENETIC VARIANT**, which owns the word outright |
| **demonstrator** | **THE PROTESTER**, in political science and crowd dynamics |
| **fin** | **THE HEAT-TRANSFER FIN**, meaning an extended surface, a large thermal-engineering literature, plus the FISH fin. The vertical fin is the thing A333's aircraft does not have |
| **canard** | **THE HOAX.** In journalism and political science a canard is a false story. Also the duck. The canard surface is A333's pitch effector |
| **reconfigurable** | **RECONFIGURABLE COMPUTING and the FPGA.** Reconfigurable CONTROL is A333's subject |
| **RESTORE** | **ECOLOGICAL RESTORATION, which is enormous, and several CLINICAL TRIALS named RESTORE.** It is also the name of the software A333's aircraft flew in 1998 |
| **tailless** | **BIOLOGY.** Tailless amphibians, the tailless whip scorpion, and the tailless gene in developmental biology |
| **spin** | **QUANTUM SPIN AND SPINTRONICS**, plus political spin. The spin tunnel and the departure from controlled flight are aeronautical |
| **vortex** | **SUPERFLUID AND OPTICAL VORTICES.** Vortex breakdown over a slender wing is exactly the aeronautical subject |
| **joint** | **THE ANATOMICAL JOINT and the JOINT DISTRIBUTION**, plus the joint venture. A programme name carrying the word cannot be filtered bare |
| **carrier** | the DISEASE carrier, the CHARGE carrier, the CARRIER WAVE and the carrier protein. The aircraft carrier is legitimate |
| **gearbox** | **THE WIND TURBINE AND AUTOMOTIVE GEARBOX**, adjacent enough that a bare filter cuts real drivetrain work |
| **hover** | **THE HOVERFLY** and the USER INTERFACE hover state |
| **allocation** | RESOURCE ALLOCATION in economics and computing, against control allocation |
| **adaptation** | **EVOLUTIONARY AND CLIMATE adaptation**, both very large, against adaptive control |
| **Froude** | **NAVAL HYDRODYNAMICS. ADMITTED DELIBERATELY**, because a ship model's scaling argument is the same argument, and it is the older and better documented of the two |
| **found only by reading a random sample** | railway power protection, bridge aerodynamics in civil engineering, astronomical transient surveys, and point-cloud shape completion. **None of the four was anticipated** |

| Phrase | The other field |
|---|---|
| **OTV** | **ORBITAL TRANSFER VEHICLE. INTERNAL TO THE DISCIPLINE**, decades older in the transfer-stage sense than in A334's Orbital Test Vehicle sense, and much the larger of the two |
| **inflation** | **ECONOMIC INFLATION**, one of the largest bodies of literature in existence. Canopy inflation is A335's term of art and cannot be filtered bare |
| **opening load** | **CRACK OPENING LOAD in fracture mechanics.** Parachute opening load is the article's term and the phrases are identical |
| **impact tolerance** | **MATERIAL TOUGHNESS in composites**, against human acceleration tolerance in aeromedicine |
| **reefing** | **SURGICAL REEFING in orthopaedics**, a tightening of soft tissue, and the sailing sense |
| **drogue** | **THE AIR-REFUELLING DROGUE**, a basket on a hose |
| **parachute** | **THE METAPHOR IN CLINICAL WRITING**, from the famous trial parody, and **THE DIFFERENTIAL-EQUATIONS EXERCISE** in teaching, plus the golden parachute |
| **probabilistic risk assessment** | **A METHOD AND NOT A SUBJECT.** Nuclear plants, offshore drilling and dose-response toxicology all use it |
| **apparent mass** | **BIODYNAMICS**, the apparent mass of the human body under vibration, against the parafoil term. **The gate distinguished these correctly and it is recorded so the next article does not filter both** |
| **ram air** | **THE RAM AIR TURBINE**, an emergency generator |
| **recovery system** | waste recovery, air traffic recovery, and every other use of the two words |
| **classification** | **STATISTICAL AND MACHINE-LEARNING CLASSIFICATION**, which dwarfs the security sense A334 needed |
| **docking** | **MOLECULAR DOCKING** in drug discovery, which owns the word |
| **payload** | **THE MALWARE PAYLOAD** in computer security |
| **discharge** | **HOSPITAL DISCHARGE** and RIVER DISCHARGE, against depth of discharge |
| **crew, return** | crew resource management and airline crew scheduling; investment return |
| **eclipse** | **THE INTEGRATED DEVELOPMENT ENVIRONMENT** |
| **spiral, boost, module, habitat** | acquisition spiral development; boosting in machine learning; the algebraic module; the ecological habitat |
| **grid storage, off-grid solar, electrode chemistry** | **THE BATTERY LITERATURE OUTSIDE SPACECRAFT**, which owns cycle life and capacity fade |
| **contact graph, 5G handover** | **SATELLITE COMMUNICATIONS NETWORKING**, which shares low Earth orbit with everything here |
| **instrument landing system glide slope** | **A RADIO NAVIGATION AID**, against an unpowered spacecraft approach |
| **Mars surface geomorphology** | admitted by an aerobraking harvest through `planetary atmosphere`. **Aerobraking AT a planet is legitimate; the geology of the surface is not** |

**Carried forward from earlier articles and still live, condensed rather than dropped.**

| Phrase | The other field |
|---|---|
| **easy glide** | crystal plasticity, a strain regime, which answered a pattern written for gliding range |
| **host range** | microbiology. It put Pseudomonas plasmids in A320's keystone cluster |
| **maneuvering range** | an instrumented air combat facility, so the pool holds its construction plan |
| **unpowered range** | wheelchairs. **Unpowered is not an aeronautical word** |
| **footprint** | carbon accounting |
| **thermal resistance, inactivation, injury; recovery** | food microbiology, where several are terms of art |
| **ducted propeller** | the Kort nozzle and the diffuser-augmented turbine |
| **laminar flow** | cleanrooms, chromatography, fuel cells |
| **ablation** | medicine and laser materials processing |
| **lateral motion, lateral range** | railway hunting oscillation, road-vehicle lane keeping, and search and detection theory |
| **base** | the air base, the database, the base station |
| **dispersion** | atmospheric pollution |

**Not a homonym but the same defect: Crossref indexes EDITORIAL MATTER AND FELLOWSHIP ADVERTISEMENTS
as works.** Guidance for Authors, Guest Editorial and conference announcements have all reached article
pools. A322 cited two Hypersonic Aerodynamics Fellowships notices.

**QUERY DESIGN PREVENTS MORE THAN FILTERING CURES.**

### On tooling

**A VERIFIER THAT SHARES AN INPUT WITH THE THING IT CHECKS DOES NOT CHECK THAT INPUT.** A335 gave its
independent verifier the same two X-24A constants the production module used, and both were wrong. The
length had been set equal to the X-38 ATMOSPHERIC TEST VEHICLE's 24.5 feet, which is a different
aircraft. **The scaling exponent moved from 4.207 to 3.507 once corrected.** The verifier now converts
from the imperial figures the sources quote. **Enter every published constant into the verifier by a
different route, and check them all again at the publication review.**

**A CHECKER THAT CANNOT FAIL IS NOT A CHECK, AND I BUILT ONE.** A334's rewrite of `require_in_text`
accepted renderings at zero decimal places, so a bare `58` stood for 58.3519 and a bare `2` for 1.9236.
In a document of 79,000 words those match by accident every time. **It reported 47 of 47 passing while
twelve verified values were absent from the draft.** The fix is a floor of **three significant digits**
plus digit-boundary matching, and **a `_self_test` that runs first and proves the check can fail.** Both
A334's and A335's verifiers carry it and it should be copied forward.

**A PLAUSIBLE TITLE IS NOT A URL.** Three curated links in A334 returned 404 and all three were
addresses built from what the page ought to be called. **The identifier sweep covers `doi.org` links and
the rendered audit covers markup, so neither looks at a hand-written encyclopaedia link.** Request every
curated URL individually at the publication review. One of A334's three was a symptom of a wrong belief
rather than a moved page, the AR2-3 being a **Rocketdyne** engine widely credited to Aerojet.

**A SUMMARY THAT LISTS ONLY EXCEPTIONS CANNOT DISTINGUISH CLEAN FROM UNEXAMINED.** A334 had no row in
the corpus citation report and was very nearly reported clean. It had been examined at **34.5 percent
coverage**, because the run was capped at 600 new lookups against 64,462 identifiers. **Measure coverage
explicitly. An absent row means nothing until the denominator is known.**

**A TRAILING FULL STOP IN A HARVESTED IDENTIFIER MAKES IT A DIFFERENT STRING.** Two of A334's records
carried one, which is why they did not resolve AND why they survived a rejection already recorded
against the clean form. `gen_master` now strips a trailing stop. **It does not strip a closing
parenthesis**, since several publishers deposit identifiers that legitimately end in one.

**`_verify.py` RESOLVES `_posts` AND `_drafts` RELATIVE TO THE WORKING DIRECTORY, SO RUNNING IT BY
ABSOLUTE PATH FROM ANYWHERE ELSE SILENTLY CHECKS A DIFFERENT CORPUS.** Invoked from an isolated build
tree it scanned the staged files there and reported **0 errors and 42 warnings** against a true
reading of 21. **An absolute path to the script is not enough when the script's own paths are
relative.** Run it from the repository root and know the expected number.

**A PLURAL BOUNDARY FAILS SILENTLY AND IT HAS NOW DONE SO FOUR TIMES.** A332's cluster matched
`installation effect` where every report writes `installation effects`, routing a whole subject to the
catch-all. A333's matched `airship hull` while Munk's keystone paper is titled airship **hulls**,
sending the article's oldest primary source to the catch-all. **Earlier instances were `Diffusers` and
`area rules`.** The failure returns a SMALLER answer rather than a wrong one, **which reads as a thin
literature instead of as a bug**, and that is why it survives passes.

**SPELLING VARIANTS ARE THE SAME DEFECT IN A DIFFERENT DRESS.** British manoeuvrability and American
maneuverability are different strings and A333's pattern matched neither reliably.

**THE ANCHOR GATE CAN REJECT THE ARTICLE'S BEST PRIMARY SOURCE OUTRIGHT.** A333's keystone is Allen and
Perkins 1951 on viscosity over slender inclined bodies of revolution, whose title contains no aircraft,
no aerodynamics and no design. **A gate built from vehicle vocabulary refuses a paper about physics.**
Admitting the vocabulary of the physics as well as the machine took selection from 4,772 kept to 5,050.

**WIDENING THE ANCHOR GATE AFTER THE REPORTS-SERVER DETAIL PASS LEAVES THE NEWLY ADMITTED RECORDS
WITHOUT METADATA, SO THEY NEVER REACH THE MASTER SET AND NOTHING REPORTS AN ERROR.** A333's 1951 paper
passed selection, showed as kept, and was still absent from the article. **Re-run `ntrs_detail` after
any change to the anchor gate or the cluster patterns.**

**AN ALL-REMAINING MARKER PLACED BEFORE A FIXED-COUNT MARKER FOR THE SAME CLUSTER DRAINS IT**, and the
fixed-count marker then finds nothing and the assembler refuses to emit an empty list. **That guard is
correct and earned its place.** Put the count-zero marker last.

**`refs.clean` MUST UNESCAPE TO A FIXED POINT.** Double-escaped markup survives one pass, so an escaped
paragraph tag plus an escaped non-breaking space decodes to real markup plus a literal entity, the tag
rule removes the tag, and the ampersand and semicolon rules turn the survivor into `andnbsp`. **A332
shipped link text reading `andnbsp andnbsp andnbsp`.**

**TYPOGRAPHIC PUNCTUATION MUST BE NORMALISED TO ASCII BEFORE ANY OTHER RULE RUNS, AND THE REASON IS A
HOLE RATHER THAN AN UNTIDINESS.** The corpus contraction check matches an ASCII apostrophe, so a title
reading "What's" written with a right single quotation mark **sailed past a check that exists to catch
exactly that word.** The soft hyphen and stray combining marks are normalised in the same place.
**Diacritics are untouched, because an author's name is not punctuation.**

**A DASH BETWEEN TWO WORD CHARACTERS IS A COMPOUND JOINER AND NOT A SEPARATOR.** Collapsing every dash
to a space turned a harvested `jet-jet/film impingement`, written with an en dash, into `jet jet`, and
**the corpus doubled-word check then reported a defect against a title that never carried one.**

**`git add -A` SWEPT IN A FILE I DID NOT CREATE.** An unrelated draft sitting untracked in the working
tree went into an article commit. **Stage explicitly.** The fix is `git rm --cached` and
`git commit --amend`, which leaves the file untouched on disk.

**AN UNDECODED HTML ENTITY IS TURNED INTO VISIBLE JUNK BY THE PUNCTUATION RULE, AND IT SHIPPED IN
THREE CONSECUTIVE DRAFTS.** Publishers emit titles wrapped in an escaped title tag rather than a
literal one, the tag-stripping rule never sees them, and the later rule that removes semicolons
mangles the escaped form into literal entity text in the link label. **`refs.clean` now decodes
entities first**, which is the only ordering in which both rules are correct, and `anchor_stem`
routes its title fallback through `clean` so markup cannot occupy the anchor's two-word window.

**A BARE ANGLE BRACKET SURVIVES THE TAG RULE, BECAUSE THAT RULE REMOVES ONLY A MATCHED PAIR.** A331
harvested a title reading `Precision >> Accuracy`, which sat mid-line by luck. **A `>` that reflow
places at the start of a line is a markdown blockquote**, the same family as the unbalanced `$$` and
the bare `\(`. `clean` now removes both brackets and the build is checked for zero blockquotes.

**AN ANCHOR STEM IS ONLY A SURNAME WHEN AN AUTHOR SURVIVED FOLDING.** Where every author is in a
non-Latin script the stem is a TITLE fallback, and `citations.verify_doi` was comparing that against
a registry author that also folds to nothing, so a correct citation reported a mismatch. **It now
declines the check rather than failing it**, reporting `author_checked` as false, and still bites on
a bogus surname. **A checker that cannot run should say so instead of reporting a defect.**

**THE LATEX COMMA-SPACING PROBLEM HAS NOW HIT FOUR ARTICLES RUNNING.** An equation writing `7{,}784.3`
flattens to `7{}784.3` and no text check finds it. **State every verified figure in prose as well as
in its display**, and expect `require_in_text` to catch three or four per pass regardless.

**RECORD VERIFIED VALUES IN THE UNITS THE ARTICLE PRINTS.** A330 recorded fractions while the article
printed percentages and newtons while it printed kilonewtons, which made `require_in_text` fail on
twenty-one values that were all present. **The check exists to confirm the article states what was
verified, so recording a different unit makes it vacuous in one direction and noisy in the other.**

**THE ASSEMBLER'S PERIOD CUTOFF MUST MATCH THE ARTICLE'S OWN STATED WINDOW.** A330 inherited a 1999
cutoff from A329, whose programme ran to 2002, while stating that its own programme ran to early
2001. **The rendered count and the sentence beside it disagreed.**

**A FRAGILE STEP IN A DOCUMENT-REWRITE SCRIPT CAN ABORT THE WRITE ENTIRELY AND LOOK LIKE SUCCESS.**
A331's reverse-prompt rewrite raised on a trailing trim after building the whole new text, so nothing
was written at all and the surrounding output looked normal. **Check the file after rewriting it, not
just the exit status of the step that was supposed to.**

**`\(` AND `\[` ARE MATHJAX DELIMITERS AND THE COMMAND RULE DOES NOT REACH THEM.** A328 harvested a
title beginning `\({\mathcal{L}_1}\)`, and after `refs.clean` stripped the commands and braces the
link text still carried **bare backslashes**, because the character after the backslash is
punctuation rather than a letter. **An unbalanced `\(` opens an inline math block exactly as an
unbalanced `$$` opens a display one**, which is the A327 defect through a different delimiter.
`clean` now removes any surviving backslash and `test_lib` has a case for it.

**A NON-LATIN AUTHOR NAME FOLDS TO NOTHING AND PRODUCED BROKEN ANCHORS.** A328 shipped anchors
reading `research___2023` because the stem was built from two names that both folded away and the
fallback did not fire, **since a lone underscore is truthy**. One record's link text was nothing but
a year. `refs` now prefers an author name that survives folding, which RECOVERS the records where
Crossref supplies both a Cyrillic and a Latin form, and falls back to the title otherwise.

**SCAN EVERY REFERENCE-LIST ENTRY FOR PUNCTUATION THAT DOES NOT BELONG.** Both delimiter defects and
both anchor defects were found that way and by no checker. A329 scanned 12,259 entries and A328
16,953. **It is one script and it is the only method that has ever worked for this class.**

**A VALUE INSIDE AN EQUATION IS NOT RELIABLY FINDABLE BY A TEXT CHECK.** A329's `require_in_text`
failed on a number that was present, because the equation wrote `20{,}199` in LaTeX comma spacing
and the flattened text held `20{}199`. **State any verified figure in prose as well as in the
display.**

**AN ALL-REMAINING MARKER MAY LEGITIMATELY FIND NOTHING LEFT**, when an earlier marker for the same
cluster and era already drained it. That is different from a fixed-count marker finding nothing,
which means the article is citing a subject it does not have. The assembler distinguishes them.

**A GROWING REFERENCE SET CAN MOVE A VERBATIM ACRONYM AHEAD OF THE AUTHORIAL SPELL-OUT.** A329
passed the acronym check at the draft pass and failed it at the publication pass without the prose
changing, because the reference lists had grown until a citation title carrying NASA appeared at
character 9,460 while the spell-out sat at 56,304. **Re-run the acronym check after every reference
pass, not once.**

**SEPARATE THE TWO KINDS OF NUMERIC CHECK, AND A329 GOT IT WRONG BEFORE GETTING IT RIGHT.** Three
checks compared an allowance line against its direct form, which is an agreement between two
computed routes rather than a value the article states, and recording them with `chk` made
`require_in_text` demand that unrounded intermediates appear in the prose.


**A PUBLISHER TITLE CAN CARRY LATEX AND BREAK THE PAGE.** A327 hit a Springer title reading
"Al/MLG/CuO/$${\text{Bi}}_{2}{\text{O}}_{3}$$ Nanothermite". Truncated for link text it left **a
single unbalanced `$$`, which opens a MathJax display block and swallows the rest of the page**.
`refs.clean` stripped HTML, ampersands, brackets and braces and **not dollars or LaTeX commands**. It
now strips both, and `_verify.py` catches the symptom as an odd delimiter count.

**A TEST APPENDED TO THE END OF `test_lib.py` NEVER RUNS.** Discovery is a module-level loop over
`globals()`, so anything defined after it is invisible, and the suite reports a healthy count while
silently omitting the new case. **A test that is never collected is worse than no test, because it
reads as coverage.** Insert above the loop.

**`require_in_text` APPENDS TO THE FAILURE LIST AND RETURNS TRUE WHEN NOTHING IS MISSING.** Calling it
after `report()` means anything it finds is never printed, and guarding on its return inverts the
sense. A326 made both mistakes at once, **which made a silent check look like a passing one.** Call it
before `report`.

**SEPARATE TWO KINDS OF NUMERIC CHECK.** `chk` records a value the article STATES, so
`require_in_text` can later insist it appears. Agreements between two computed routes need a different
helper, because an article that deliberately withholds a number should not be forced to print it.

**THE DOUBLED-BACKSLASH DEFECT SHIPPED IN THREE CONSECUTIVE ARTICLES.** In an rf-string `\\,` stays
**two characters**, and MathJax reads it as a line break followed by a comma. The equation count is
right, the braces balance and the build succeeds. **A323 did it in a file whose own docstring warns
against it.** Use `\,`. **`_verify.py` now has a `math-doubled-backslash` error for it**, so this one is
caught, but the general lesson stands: **read the rendered output.**

**A BARE `|` IN INLINE MATH AT THE START OF A PARAGRAPH TURNS THE PROSE INTO A TABLE.** kramdown reads a
paragraph whose first line contains a pipe as a table, so `$|S| = 39$` opening a paragraph shreds the
math across table cells. **Write `\lvert S \rvert`.** `_verify.py` warns on it as `math-pipe-table`.

**MATCH STRINGS CARRY PRE-REFLOW LINE BREAKS AND WILL NOT MATCH AFTER A REFLOW.** Use
`_lib/edits.match_ws`, which exists for exactly this and which A324 forgot to use on its first attempt.

**AN EDIT APPLIED AFTER REFLOW LEAVES BOLD SPANS CROSSING LINE BREAKS.** Reflow again, and run the lint
on the text that will ship rather than on the text before wrapping. A324 reported 122 bold-span
conventions that reflow was about to fix.

**READ THE GENERATED BODY AND THE RENDERED EQUATIONS.** Every article has produced at least one defect
that only reading found: mangled LaTeX, link text truncated mid-word, duplicated equations, symbol
collisions.

**SYMBOL COLLISIONS BETWEEN TWO STANDARD NOTATIONS ARE RESOLVED BY MARKING ONE, NOT BY SILENTLY
REUSING IT.** A322 had `sigma` doing solidity and density ratio, and `gamma` doing glide angle and Lock
number. Both are standard. The article keeps one, subscripts the other, and says why.

**DO NOT LET DRAFTING HISTORY LEAK INTO THE ARTICLE.** Sentences of the form "the draft said X and was
wrong" refer to a revision the reader never saw. A322 shipped five and A323 six; both were removed.
**Keep the epistemic content, drop the revision history.**

**DO NOT WRITE ARTICLE SECTIONS BY PLACEHOLDER SUBSTITUTION.** It freezes cluster citations. They
belong in the body as live `{c('...')}` calls.

**A DISPLAY EQUATION MUST OCCUPY EXACTLY ONE SOURCE LINE, AND A BOLD SPAN MUST NOT CROSS ONE.** The
style checker validates per line. `_lib/reflow.py` enforces both and is a fixed point after one pass.

**`check_any.py` REPLACES the per-article `check.py`.** It lives at `tmp/errata/check_any.py`, derives
the article number from the `<!-- Axxx -->` marker, and validates date and series index against the
roster.

**Know the expected number, not just pass or fail.** `_verify.py` baseline is **0 errors and 21
warnings**. A reading of 0 warnings means it did not run against the corpus. **Absolute paths in every
command issued after a `cd`.**

**Measure the equation count before and after any section work, and extend sections in place.**

---

## Verification Toolchain

**THE SHARED MECHANISM IS COMMITTED AND MUST NOT BE REBUILT.** `_lib/` holds it, with `README.md`
describing each module: `fetch` for archive queries, `refs` for anchors and the reference block, `edits`
for guarded editing, `reflow`, `lint`, `diction` for word and phrase overuse, `audit` for equation and
citation gaps, `numcheck` for independent re-derivation, and `citations` for registry verification. Run
`python3 _lib/test_lib.py`, which should report **75 of 75**. **`refs.clean` gained a bare-pipe strip on
2026-08-12**, because kramdown reads a paragraph whose first line contains a pipe as a table and a
publisher-mangled apostrophe entity put one into link text. **Three modules were added on
2026-08-11**, being `gate` for subject-anchor gating with a mandatory two-sided sample, `render` for
auditing BUILT HTML, and `resolve` for identifier resolution. `_research/rejected.json` holds the accumulated
sweep judgements, reused through `_research/homonyms.py`, **whose curated pattern list is now 35 and
whose store holds 728 per-record rejections.** A334 and A335 between them added eleven families,
listed in the homonym table above with the incident that produced each.

**`tmp/*` IS GITIGNORED**, and what belongs there is the article's own payload only, meaning harvest
queries, cluster definitions and edit text. **Repoint every path** when copying a previous article's
directory, **and rewrite the topic list** used by the coverage audit, which otherwise still describes the
previous subject.

**Committed, in `_lib/`.** Use these rather than writing new ones.

| Module | Purpose |
|---|---|
| `fetch` | archive queries with backoff; Crossref, NTRS, DTIC, OSTI, Open Library. **NTRS search returns no authors**, so `ntrs_detail` supplies them |
| `refs` | anchors, link text, deduplication by title AND year, and `emit_blocks` for the reference section. **Truncates at word boundaries** |
| `edits` | whitespace-tolerant, all-or-nothing edits with equation and invariant guards |
| `reflow` | rewrapping that keeps bold spans and link pairs atomic. **Opt-in per article, not a corpus normaliser** |
| `lint` | mid-edit invariant scan, defects separated from house conventions |
| `diction` | word and phrase overuse **measured against peer articles**, since a fixed threshold cannot tell a tic from a subject noun. Strips citation link text |
| `audit` | equation gaps, citation gaps, thin sections, primary count AND fraction. **Run `citation_gaps` after every equation pass** |
| `numcheck` | independent re-derivation harness; **must not import the calculation** |
| `citations` | Crossref registry verification for recalled identifiers, sampling for retrieved ones |
| `gate` | subject-anchor gating for a harvested corpus. **`audit` samples BOTH the kept and dropped sides and requires a seed**, because a narrow gate reports a small corpus and a permissive one reports a large corpus, and no summary statistic tells them apart |
| `render` | audit of **BUILT HTML**, the only check that sees what a reader sees. Math balance by backslash-run parity |
| `resolve` | whether an identifier resolves at all, with registry fallback. **Different question from `citations` and neither subsumes the other** |

**Per article, in gitignored `tmp/`.** Harvest queries, cluster definitions, the physics in `calc.py`,
and the edit payloads. These are the article's argument and do not belong in `_lib`.

### The Endpoints, Also Documented Here Because They Are Easy to Get Wrong

- **NTRS search**, `https://ntrs.nasa.gov/api/citations/search?q=<terms>`, detail at
  `https://ntrs.nasa.gov/api/citations/<id>`. **Cite `https://ntrs.nasa.gov/citations/<id>`.** Caps at
  ten and is phrasing sensitive, so **many narrow period queries beat few broad ones**. Authors are a
  dict under `authorAffiliations`; the year is in `publications[0].publicationDate`. Full text at
  `/api/citations/<id>/downloads/<id>.pdf`, and `pdftotext` works on it.
- **DTIC**, through Crossref with `filter=prefix:10.21236`. Cite `https://doi.org/<doi>`. **DTIC DOIs
  land on `www.dtic.mil`, which refuses automated connections, so verify through the Crossref
  registry**, which is strictly stronger than an HTTP 200.
- **OSTI**, **not worth using for this subject.**
- **Crossref**, `https://api.crossref.org/works?query.bibliographic=<terms>` with
  `filter=from-pub-date:...,until-pub-date:...,type:journal-article`. `container-title` is the venue the
  selector filters on. Use a polite-pool `mailto`.

### The Corpus Checks

`python3 _verify.py` from the **repository root**. The same checks run in CI and in `_hooks/pre-push`.
**Baseline 0 errors and 0 WARNINGS as of 2026-08-11.** It was 21 warnings for most of the series'
life. **A new warning is now signal rather than noise, so do not let one accumulate.**

**`./_check.sh` runs the whole deploy gate locally**, being `_verify.py`, a production build and
`_lib/render.py` in CI's order, into a throwaway directory. `--drafts` includes drafts and `--weights`
reports page weight. **`_preview.sh` cannot tell you whether the deploy will pass**, because it ends in
`jekyll serve --watch` and nothing runs after it.

**Read `_docs/process/VERIFICATION_TRAPS.md` before trusting any checker you write.** It records the
mistakes this method has actually made and the observation that caught each. The recurring root is
**asserting a property instead of measuring it**, and the most expensive instance was a rendered-math
checker whose second wrong version masked its first.

**The bundle is installed** at `vendor/bundle`, which is gitignored.

**An HTTP 200 does not verify a citation.**

**Independence matters.** The article's verifier must not import its calculation module.
`_lib/numcheck.py` is the harness, with `prop` for randomised property checks, `bisect` for reaching a
value by a different route, and `require_in_text` to fail when a verified number is absent from the
draft. A323 finds its
maximum lift-to-drag ratio by **scanning the polar**, its decibel-per-doubling by **bisection**, and
tests the helix-angle cancellation as a **randomised property**.

---

## Open Decisions

**Categories, SETTLED and not to be revisited.** `aerospace history engineering`.

**THE CITATION RESIDUE IS LARGELY WORKED THROUGH AND THE REMAINDER STILL BELONGS TO THE PUBLICATION
REVIEWS.** A334 was taken to **99.9 percent coverage** and its four findings were resolved, being a Mars
geomorphology paper, two Science news items indexed as works and two nonexistent identifiers. **The
corpus-wide run stands near 50 hard and 184 weak findings across 87 articles with 60 clean.** Resolve
these one article at a time during its publication review, where the context to judge a label exists.

**The historical record of how the residue arose, kept because the cause will recur.** The first
ever corpus-wide `_verify_citations.py` run, on 2026-08-11, covered **77,593 citations across 61,483
distinct identifiers** and reached the X-Planes drafts for the first time. After the checker was fixed
and 632 wrongly named authors were repaired, **43 mismatch and 89 label-name findings remain, all in
X-Planes drafts**, plus 184 weak, 3 nonexistent and 5 identifiers registered with DataCite.

**Resolve these one article at a time during its publication review**, where the context to judge a
label exists. The figures are in `_docs/process/URL_VERIFICATION.md` under the run record.

**The cause is worth carrying forward because it will recur.** Each article's throwaway `assemble.py`
built its own reference link text and took the **last token** of the author string, so
`BELL AEROSPACE CO BUFFALO NY` rendered as `NY` and the prose read "described in NY 1955".
**`refs.display()` was already correct.** **Call it. Do not reimplement link text.**

**The genre bands, SETTLED on 2026-08-09 and not to be revisited.**
`_docs/writing/RESEARCH_AIRCRAFT_STRUCTURE.md` was amended on the pilot's instruction to describe what
the series actually does. The old bands, drawn from the History of SpaceX medians, matched no recent
article. **The document now carries measured figures across all twenty-seven drafts**, records that the
class table is about SECTION ORDER rather than size, and states the comprehensiveness directive
explicitly. **Exceeding any figure in it is not a defect and requires no justification. Padding toward
one is forbidden.** Report the counts, do not target them.

**A305 length, SETTLED on 2026-08-09 and not to be revisited.** The pilot has directed that **the
goal is for these articles to be as comprehensive as possible and that doing more is not a problem**,
and has instructed that A305 be left as it stands. The offered cut is **withdrawn**, not pending.

**Two things about that offer are worth recording so the mistake is not repeated.** It described the
cut as roughly 300 lines and 25 equations, and **that figure was wrong**. The section it named,
`## What the Data Changed`, is 130 lines and 19 equations, and was that size on the day the offer was
made. The overstatement was carried forward through several handoffs before anyone checked it.
**Verify a figure before putting it in this file, including a figure about the articles themselves.**

**THE COMPREHENSIVENESS DIRECTIVE IS GENERAL AND NOT SPECIFIC TO A305.** Exceeding a genre band is not
a defect and does not need an apology. **Continue to REPORT the counts**, because the record is
useful, but do not offer to trim, do not pad toward a band either, and do not treat an overrun as
something requiring justification.

**A336 IS THE NEXT ANOMALY AND THE DECISION IS ALREADY MADE.** X-39 was reserved and never assigned, so
no vehicle existed and none produced data. **The reduced six-section order is the honest default**, and
the genre document states that padding a short anomaly article with sections it does not need is worse
than leaving it short. **Whether the three series sections belong on an anomaly article is genuinely
open**, since the contemporary survey and the source-base accounting exist to serve a technical argument
that an anomaly article does not have. **Decide it deliberately and say why in the article.**

**A320's full-length treatment of a designation anomaly is a precedent with a limit.** It was written
long because the SV-5D flew and returned a measurement. **A324 is the opposite case and the short class
is the honest default there.**

**A FINDING NOW FOUR CASES DEEP AND HEADING FOR FIVE, WHICH IS THE STRONGEST EVIDENCE THE CLOSING
ARTICLE WILL HAVE.** The vehicle's own cluster has been thin in four consecutive articles **and every
reason was different.**

| Article | Vehicle | Why its cluster is thin |
|---|---|---|
| A330 | X-33 | **Cancelled.** Sixty records, every one predating 2002 |
| A331 | X-34 | **Cancelled.** Same shape, and two instances made it a pattern |
| A332 | X-35 | **It won, and never had a trace at all.** Zero of 12,974 records carry the designation, because contractor demonstrators flown for a source selection do not produce reports |
| A333 | X-36 | **It ran to completion and produced a technique rather than a vehicle**, so its contribution is filed under the names of its methods |

**THE PATTERN IS NOW SIX CASES DEEP AND EVERY REASON IS DIFFERENT.** This is the strongest evidence the
closing article will have.

| Article | Vehicle | Why its cluster is thin |
|---|---|---|
| A330 | X-33 | **Cancelled.** Sixty records, every one predating 2002 |
| A331 | X-34 | **Cancelled.** The same shape, and two instances made it a pattern |
| A332 | X-35 | **It won**, and contractor demonstrators flown for a source selection do not produce reports |
| A333 | X-36 | **It produced a technique rather than a vehicle**, so its contribution is filed under the names of its methods |
| A334 | X-37 | **It became classified.** Seventeen records in 13,351, and **the programme's own literature stops in 2005**, one year after the transfer to the defence research agency, while the vehicle went on flying for twenty years |
| A335 | X-38 | **The requirement went away.** Fifty records in the period half and three in the contemporary. **It was not cancelled for failing**, it was cancelled because the station shrank to a crew of three that the Soyuz already served |

**The conclusion is not that thin clusters mean failure.** The X-37 is the most operationally successful
vehicle in the last ten articles and has the thinnest trace of any of them. **The documentary record
measures the institution and its circumstances rather than the aircraft.** The conclusion is not that thin clusters mean failure. It is that **the
documentary trace measures the institution and its circumstances rather than the aircraft.**

**A finding accumulating across articles.** A322 and A323 were both **off-the-shelf civil aircraft
bought for properties they already had**, and neither generated any development literature, because
nothing was developed. **If A324 makes three, that is a substantive finding about what the designation
had come to mean** and belongs in the closing article.

---

## Governing Rules That Are Easy to Lose

**The `post_url` interlock.** A `post_url` tag whose target is absent fails the **entire** site build.
Cross-references are **back-reference only** within the series. The publication-order dependency is
**thirty-nine deep**, A335 back to A297, so these articles publish in order or together. **Links to
other series are necessarily forward-dated** and that is not a defect.

**Pushing drafts is safe.** The deploy workflow builds without `--drafts`. Confirm after every push
that the article returns 404 while the site root returns 200. **A 503 on the root immediately after a
deploy is transient; retry before reporting it.**

**The two-commit publication pattern** applies when publishing eventually happens. Nothing in this
series is published and **no publication has ever been authorised.**

**Prose style is absolute.** No contractions, em dashes, en dashes, prose colons, prose semicolons, or
prose parentheticals. **A possessive is not a contraction.** The `console.log` debug tag is the only
permitted parenthesis. **Link text is prose.** **Emphasis is bold, never capitals.**

**Every article carries** an `<!-- Axxx -->` comment and a `<script>console.log("Axxx");</script>` tag
immediately after the front matter.

**The genre carries three sections beyond the standard twelve**, being Comparison With Ground
Prediction, The Contemporary Literature, and The Source Base, the last immediately before Epistemic
State. `check_any.py` enforces all three and exempts the series opener.

**Density conventions are absolute counts, not ratios.**

**THE COUNT-VERSUS-FRACTION TRAP RUNS IN BOTH DIRECTIONS AND A325 WAS CAUGHT BY BOTH ENDS.** Adding a
contemporary survey holds the period COUNT and drops its fraction; adding period sources holds the
contemporary COUNT and drops its fraction. **Neither movement is a fact about coverage. Both are facts
about the denominator.** Give the count and the fraction together, every time, and say which one moved.

**REPORT THE COUNT AS WELL AS THE FRACTION.** Adding a contemporary survey lowers the period *fraction*
while leaving the period *count* unchanged, and saying only the fraction reads as a regression when it
is the directive working. A323's period count held at 920 against 922 while the primary fraction fell
from 64.0 to 43.7 percent.

**SPELL OUT NASA.** It has now been missed in two consecutive articles and caught in both publication
reviews. Model designations such as QT-2, SGS 2-32, YO-3A, KSA-100 and WRC-19 are exempt.

**Irreversible or outward-facing actions need confirmation.** Pushing is authorised only by the
publication-review prompt. **Publishing has never been authorised.**

**Report faithfully.** If a check fails, say so with the output. If a figure is assumed, say it is
assumed. If a band is missed, report the miss rather than padding toward it.

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

**X-23 and X-27 ARE NOW WRITTEN, and X-30 is written although it is not one of the nine.
The rest remain ahead.**

- **X-23**, attributed to the Martin Marietta SV-5D PRIME, but USAF nomenclature records reportedly
  show X-23A was never assigned. State the conflict, do not resolve it. **Written at full length in
  A320, because the SV-5D flew and returned a measurement.**
- **X-27**, never built, mock-up only. **Written at full length in A324, against the previous handoff's
  prediction of the short class**, because the design record carries complete geometry, weights and
  engine ratings, and the parent F-104 flew for thirty years and anchors the derivative's claims. **The
  class test is whether there is a keystone to dimension systems against, not whether anything flew.**
- **X-39**, reserved 23 April 1997 for the AFRL Future Aircraft Technology Enhancements programme;
  no written allocation request followed.
- **X-41**, still-classified vehicle in the DARPA FALCON programme. No specifications released.
- **X-42**, sources disagree, one calling it an expendable upper stage and another a spaceplane test
  vehicle. No dedicated treatment exists anywhere.
- **X-44**, two different aircraft, the Lockheed Martin MANTA and a separate unmanned programme.
- **X-52**, requested 2006, refused over possible confusion with the B-52. The programme became X-53.
- **X-58**, skipped, with the slot consumed by the Kratos XQ-58 Valkyrie.
- **X-67**, skipped, with the slot consumed by the General Atomics XQ-67A.
- **X-69 to X-75**, unassigned and leapfrogged.

**THE FIRST FINDING FOR THE CLOSER, NOW COMPLETE.** X-25, X-26, X-27 and X-28 are **four consecutive
designations that did not go to a purpose-built research aeroplane**. Three were aircraft that already
existed and were bought for properties they already had, and the fourth did not exist at all. **The
X-28A is the clearest case**, since the Navy watched a man demonstrate his own aeroplane and wrote him
a cheque. **A326 ends the run**, and that ending is itself evidence.

**THE SECOND FINDING, ADDED BY A327, IS THAT THERE ARE TWO KINDS OF NEVER BUILT AND THEY ARE
OPPOSITES.** The X-27 was not built **because nobody bought it**. The design existed, the manufacturer
was ready, and no customer appeared, which is a procurement fact. The X-30 was not built **because the
thing it was meant to demonstrate could not be shown to be achievable before building it**, after
roughly three billion dollars and a decade. **A designation can mark an absence of demand or an
absence of knowledge**, and the closer should not collapse the two.

**A THIRD OBSERVATION WORTH CARRYING.** A326 and A327 are consecutive articles whose keystones are
mirror images. The X-29 could measure the thing it existed to measure. The X-30's central quantity
could not be measured by anything on the ground at all. **The series is accumulating a spectrum of how
answerable a research question was**, which is more interesting than a list of what flew.

**A FOURTH FINDING, ADDED BY A329 AND MEASURABLE.** The designation went to a COMPETITOR for the
first time. Every earlier X-plane existed to find something out; the X-32 existed to beat another
aeroplane, and it lost. **The consequence is documentary and it is quantified in the article**: in a
pool of 4,412 harvested records, exactly ONE carries the X-32 in its title, written by its engine
supplier after the decision, against 29 for the winner running continuously from 2002 to 2020. **A
competition decides not only which aircraft is built but which one is KNOWN**, and that belongs in
the closer as a statement about what the designation buys.

**A FIFTH, WHICH IS THE SPECTRUM THE SERIES IS ACCUMULATING.** A326 could measure the thing it
existed to measure. A327's central quantity could not be measured on the ground at all. A328
answered its question with an experimental design and a measured rate. A329 answered its question
with a single comparison against a rival, where the difficulty was not sampling error but
**construct validity**, since neither demonstrator was the aircraft being bought. **The series is
accumulating a spectrum of HOW ANSWERABLE a research question was, and the closer should present it
as one.**

**A SIXTH FINDING, ADDED BY A330 AND A331, AND IT COMPLETES A SET OF FOUR.** The series has now met
four distinct reasons a designation went to a vehicle that never flew, and they are not variations of
one thing. The X-27 marks **an absence of demand**, since the design existed and no customer
appeared. The X-30 marks **an absence of knowledge**, since the thing it was meant to demonstrate
could not be shown achievable before building it. The X-33 marks **the presence of an answer nobody
wanted**, since its demonstrator worked, returned a number, and the number did not close. **The X-34
marks none of those.** It was finished, it was never asked a question it could fail, and it was
scrapped. **Of the four it is the only one that was ready.**

**A SEVENTH, AND IT IS ABOUT THE RECORD RATHER THAN THE AIRCRAFT.** A cancelled programme stops
generating literature under its own name almost immediately. Every record carrying the X-33
designation predates 2002 and so does every record carrying the X-34's, in pools of ten thousand and
six thousand respectively. **The documentary trace of a vehicle measures how long it survived rather
than what it contributed**, which sits directly against the series' habit of treating a thin record
as a thin subject.

**AN EIGHTH, WHICH IS THE SPECTRUM CONTINUING AND NOW HAS A NON-PHYSICAL END.** A326 could measure the
thing it existed to measure. A327's central quantity could not be measured on the ground at all. A328
answered with an experimental design. A329 had a construct-validity problem. A330 could answer and
did, negatively. **A331's binding quantity was COST, which has no units, no conservation law and no
instrument**, so its demonstrator returned a revised estimate rather than a reading. **One programme
was killed by a number it measured and the next by a number it recalculated**, and the closer should
present the spectrum as running from the measurable to the merely estimated.

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
