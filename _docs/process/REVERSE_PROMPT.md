## Last Updated

**Date**: 2026-08-13
**Task**: **A339, "X-Planes: Orbital Sciences X-42", draft pass complete.** Committed and **not
pushed**, per the draft-pass rule. **Not published**, and publication of this series has never been
authorised.

---

## The Disagreement in the Roster Was Not a Disagreement

**You flagged that sources disagree about what the X-42 was, one calling it an expendable upper stage
and another a spaceplane test vehicle. Both are right, about different vehicles, four years apart.**

**X-42A was allocated in late 1997 or early 1998** to an expendable demonstrator for pop-up upper stage
technology, being the Upper Stage Flight Experiment, and **was never used in an official announcement
again**. **In 2002 the Air Force Research Laboratory and industry used X-42 informally** for a
candidate reusable launch vehicle demonstrator, a winged vehicle on a single RS-27 engine derived from
Orbital Sciences' Multi-Role Reusable Vehicle, able to carry a Common Aero Vehicle on its fuselage.

**They share a contractor and a sponsoring directorate and nothing else.** One is expendable and
wingless on peroxide and jet fuel. The other is a winged reusable booster on the Delta II first stage
engine. The authoritative survey declines to tie the number to either, and this article follows it.

**This is the third consecutive article to find a designation that may not belong to its vehicle**,
after X-39 reserved and never assigned and X-41A allocated years before its programme. **The closing
article will have to account for the late 1990s administration of this number space.**

**One detail cuts the other way and is worth keeping.** The USFE contract with Orbital Sciences was
initiated in **December 1997**, inside the allocation window. **Unlike X-41, the X-42 pairing is not
anachronistic.** Its weakness is that no official use ever confirmed it.

---

## The Class Test Overruled the Roster Title

**A disputed designation does not make a designation-anomaly article.** The genre note's test is
whether a vehicle existed and produced data, and a great deal of data exists. A 10,000 lbf engine ran
**more than 700 seconds on a single catalyst bed** at Stennis, and an all-composite common-bulkhead
tank was proof tested at Chandler in April 2003.

**So this is full section order with the designation given its own section**, on the A320 precedent
rather than the reduced order A336 used.

---

## The Keystone Explains Both Unusual Choices With One Relation

**Tank mass is pressure times volume divided by material specific strength, with shape entering only
through a constant.** Nothing scales away, so a pressure-fed stage pays in proportion to what it
carries. Dividing by propellant mass leaves exactly three levers, being pressure, propellant bulk
density and material specific strength.

**The vehicle pulled the second and third at once, and that is the whole design.** Ninety percent
peroxide with JP-8 at mixture ratio 4.7 gives a bulk density of **1.230 g/cm³**, and filament wound
carbon and epoxy carries **seven to eleven times** the specific strength of aluminium 2219-T87. On the
ideal membrane relation that is **0.82 percent** of propellant mass against **5.84 percent**.

**On specific impulse this propellant is the worst combination in the comparison table. On density
impulse it beats liquid hydrogen by more than a factor of two.** For a pressure-fed stage that is the
column that decides the design.

---

## Three Results I Did Not Expect to Get

**Two papers four years apart settle a number neither states.** The structures paper gives a proof
pressure of 1,100 psia at 150 percent of operating pressure, which admits two readings. The engine
paper independently fixes a floor of **636 psia** from chamber pressure plus measured catalyst bed
drop. That leaves 97 psi of margin under **MEOP = 733 psia** and 464 psi under the alternative.
**Only the first is a design anyone would build**, and neither paper was written to support it.

**The throat erosion is measured twice by independent means and the two agree.** Cavitating venturis
fix the mass flow, so chamber pressure tracks throat area inversely, and the 140 second test's pressure
history alone implies **0.00050 in/s**. Post-test metrology on a different run at a higher mixture
ratio gave **0.0009 in/s**. Neither figure was derived from the other and they order correctly.

**The same fixed mass flow makes thrust nearly immune to erosion.** A **22.5 percent** growth in throat
area over a full burn changes thrust by about **one percent**, because thrust follows the thrust
coefficient alone. **The ablative nozzle and the cavitating venturi are one decision, not two.**

---

## The Headline Paper Overstates How Easily the Throttling Was Obtained

**A companion paper at the same conference reports a low frequency catalyst bed instability at about
one third of design flow**, removed by modifying the combustion chamber. The demonstrated throttle
range reaches 20 percent in bipropellant mode and 10 percent in monopropellant mode, **below the flow
at which the untreated engine went unstable**.

**Reading the throttling claim without the instability paper gives a false impression**, and the
article treats the pair as one result.

**The safety claim needed the same treatment.** The engine paper reports a perfect safety record in
July 2000. In **December 2000** an overpressurisation incident at the same centre during peroxide work
damaged facility infrastructure and test hardware. **Whether it involved this engine is not
established, and the article does not assert that it did.**

---

## The Programme Was Destroyed by the Component It Existed to Prove

The tank passed a hydrostatic proof at 150 percent in April 2003 and later **failed during a helium
pressurisation test, taking the engine with it**. A second article leaked. **No flight ever followed**,
and the article states that as an argument from silence and marks it as one.

**That is more informative than a launch failure would have been**, because it locates the difficulty
precisely in the composite pressure vessel rather than in the propulsion or the mass relation.

---

## The Gate Was Wrong Four Times and the Fourth Fix Was a Test

**This subject's vocabulary collides with biomedicine, dentistry and food chemistry on almost every
high-value term**, so the gate did more work than any in this series.

**Bare `booster` admitted a systematic review of child booster seats.** The same audit showed the gate
was simultaneously too narrow, dropping filament-wound work because the pattern refused a hyphen.

**Three conjunctions were satisfiable by one word**, because the qualifying vocabulary contained a word
that also appeared in the term being qualified. Those admitted piston liner tribology and silica
particle chemistry.

**The same defect sat in a fourth place that fixing the first three did not reach**, because I searched
for the word rather than for the shape of the mistake.

**So I stopped hunting instances and asserted the property.** The gate now proves that no alternative in
one half of a conjunction matches inside another half. **It failed immediately on a fifth instance no
sample had surfaced**, and passes now across all 26 conjunctions.

---

## Seven Ordering Claims Are Now Checked Rather Than Trusted

**My first draft of the survey claimed two different clusters were the smallest**, claimed the keystone
cluster was the smallest when it ranks eighth of sixteen, and named as largest a cluster the residual
exceeds by more than a factor of two. **That is the count-in-own-prose defect for the seventh time in
this series.**

**The assembly script now asserts all seven ordering claims against the computed counts** and refuses
to write the draft if any fails.

---

## One Change Landed in the Shared Library and It Affects Every Future Article

**`_lib/refs.py` gained `title_lead`**, and `display` and `anchor_stem` now call it. Abstracting
services and patent registries prefix their own accession number to the title field and Crossref
passes it through, so a record with no Latin-script author produced reader-visible link text reading
**"98/02419 Effects of launch 1998"** and **"5451015 Crashworthy composite aircraft 1996"**. **A339
harvested 33 of these in one pool.**

**It is deliberately not part of `clean`**, because a title is entitled to begin with a number and the
full reference text should keep it. Only the shortened label needs the prefix gone.

**My first version of the rule broke a legitimate title**, turning "3D printing" into "D printing".
Requiring a lowercase letter after the capital is what separates a glued word from a leading
initialism. **`_lib/test_lib.py` gained a regression test covering both directions and the suite is
79 of 79.**

**I judged this to be mechanism rather than article content**, which the library README says belongs
in `_lib` rather than in `tmp/`. **Say so if you would rather I had kept it local**, since it changes
labels and anchors for any article whose pipeline is re-run.

---

## Counts and State

**20,715 lines, 23 display equations, 9,816 reference definitions, 113,314 words**, of which
**20,961 are author prose**, a dilution factor of 5.4.

**20 curated sources carry the argument**, of which 18 are primary, and **9,754 harvested records** map
the field. **The pool was 25,076 Crossref records at a 39.4 percent admit rate**, plus 130 from the
NASA Technical Reports Server.

**`_verify.py` reports 0 errors and 0 warnings across 301 posts.** Prose style scans clean at 0 em or en
dashes, 0 contractions, 0 prose colons, 0 prose semicolons and 0 parentheticals in body prose. All 27
derived figures in the article were cross-checked against the verification script that computed them.

**Forty-three of seventy-two drafted, none published, publication never authorised.** Forty-two of the
forty-three cite a sibling through `post_url` with no target in `_posts/`, so **the set publishes in
order or together**.

---

## What I Did Not Do

**I did not push.** The draft pass commits and stops.

**I did not publish**, and I will not without an explicit instruction.

**The equation count is 23, which is low against this series.** The equation-density pass exists for
exactly that and I have left the candidates for it rather than padding the draft.

**I corrected the `TASKLOG.md` Current Task block**, which had gone self-contradictory for a sixth time,
naming A336 as both draft-pass-only-and-unpushed and four-passes-and-pushed in consecutive sentences.
I deliberately left it alone at session resume so the handoff would validate GREEN, and folded the fix
into this commit as planned.

---

## Next

**The equation-density review of A339**, on your prompt. Nothing else is outstanding.
