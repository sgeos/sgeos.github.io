# Handoff Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the resume prompt for an agent picking up after a compaction or a new session. It is a
snapshot, deliberately not kept current, and it self-reports as stale rather than misleading a
resuming agent. Read it first, validate it, then read the live channels.

---

## Validity

- **Branch**: `master`
- **Parent commit** (the repository state this handoff describes): `bd8265c`
- **Written**: 2026-09-07
- **Tree at write**: clean, and **everything was pushed at the parent**. **One commit is unpushed when
  you read this and it is this handoff's own**, which is what `git log origin/master..HEAD` will show.
  The protocol asks for a commit and not a push, so it was left for the pilot.
- **Context**: the X-Planes series is IN PROGRESS. **Fifty-five of seventy-two articles drafted. None
  published, and none authorised.**
- **A351, Gulfstream X-54, is complete on all four passes and is PUSHED**, including its rendered
  audit. **No article is mid-rhythm.** The tree is at a clean article boundary.
- **The next prompt will be "Please draft A352, 'X-Planes: Lockheed Martin X-55.'"** Editorial date
  2025-11-30, series index 56.

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

## Resume prompt, and the next prompt will be "Please draft A352."

**No article is mid-rhythm. Wait for the pilot's prompt and do not start A352 unprompted.**

**THE PILOT MAY HAND YOU AN EXTERNAL DRAFT INSTEAD, AS HAPPENED WITH A372 AND A373.** The prompt is
"copy `<path>` into the drafts, and use it as the basis for an article Axxx with a `<date>` editorial
publication date". Those arrive already stamped with their article number, series and index, and the
work is conformance and retargeting rather than writing. **They still take all four passes afterwards.**

**A352 IS THE X-55 AND ITS SUBJECT IS NOT AERODYNAMICS.** The registry entry, allocated 19 October 2009
to Lockheed Martin with two Pratt and Whitney PW306B engines and the Air Force as sponsor, reads:

> Highly modified, experimental transport to validate extreme time and cost compression in airframe
> manufacture using large, unitized composite structures fabricated using low-temperature,
> out-of autoclave curing techniques.

**That is a MANUFACTURING demonstrator wearing an X number.** The aeroplane is the Advanced Composite
Cargo Aircraft, a Dornier 328J with a new composite aft fuselage and tail. **The literature is
out-of-autoclave curing, unitised composite structure, cure kinetics, tooling, and the cost and
schedule of manufacture** — not lift, drag or stability. **Build the gate for that and do not carry
A351's forward**, whose anchors were nonlinear acoustics, atmospheric propagation and community noise.

**THE MEASURED-QUANTITY SPECTRUM HAS A NEW END AND A352 SITS ON IT.** A331's binding quantity was
COST, which has no units and no instrument. **The X-55's registry entry names time and cost compression
as the thing to be validated**, so this is the second article whose central quantity is an estimate
rather than a reading. Read A331's treatment before writing.

**`gate.ATMOSPHERE` IS A PER-ARTICLE DECISION.** A349 left it out because an administrative refusal
computes nothing at altitude, A350 and A351 named it. **A manufacturing demonstrator probably does not
need it**, and that judgement should be made and recorded rather than inherited.

**THE SWEEP STORE IS AERONAUTICAL AND THAT IS ONLY SAFE WHILE THE SUBJECT IS.** A351 predicted in
writing that an aeronautical subject would need no tag and **needed thirteen**, because its subject was
a noise and every community-noise pattern in the store had been earned by aeroplane sweeps. **A
composites subject is exposed the other way**, since the store carries composite-laminate and
fatigue-crack patterns earned as contaminants that here would be the subject. **Measure what the store
deletes before trusting it, and read a sample of the drops.**

**`homonyms.TAGS` IS NOW `['civil-structures', 'ecology', 'environmental-assessment', 'geophysics',
'hypersonics', 'interpreting', 'marine', 'medicine', 'meteorology', 'missiles', 'nomenclature',
'ocean-modelling', 'ramjet', 'remote-sensing', 'surface-transport', 'teaching', 'wind-energy']** across
132 patterns, and an unknown tag raises rather than failing open.

---

## Where the Series Stands

**Fifty-five drafts, series indices 1 through 55 contiguous, all in `_drafts/`. Zero published.**
Measured, not recalled. **Seventeen articles remain.**

**Every draft has completed all four passes.** A351 is the most recent and its four commits are
`6603498`, `9c047c4`, `aaf71ff` and `bd8265c`.

### A350, Boeing X-53 Active Aeroelastic Wing

**8,036 lines, 27 display equations, 3,682 references, 47,556 words**, research 3,605, primaries 282 at
7.8 percent. Full-aircraft class.

**The aeroplane never reached the condition it was named for**, missed the lower of its two roll
requirements in the regime the concept exists to exploit, and **three of its four wing surfaces carry
actuators strong enough to break their own structural limits**, which came out of multiplying two
columns of a table the report only set out.

### A351, Gulfstream X-54

**7,077 lines, 31 display equations, 3,231 reference definitions, 44,766 words**, research 3,143,
primaries 380 at 12.1 percent, 84 curated sources. **Designation-anomaly class**, the third after the
X-39 and the X-52, but unlike both this number went to a real contractor with a real sponsor and a real
mission statement and then nothing was built.

**The registry entry is the article.** Allocated 5 May 2008 to Gulfstream Aerospace, sponsored by NASA,
mission stated as generating relevant ground sonic boom signatures `in support of NASA and a regulatory
change process`. **Of the 510 designations allocated between August 1998 and November 2025, exactly one
mission statement contains the word `regulatory`**, and `certification`, `rulemaking` and `policy`
appear in none. That is measured by `registry_scan.py` and asserted by `assemble.py`.

**The central computation is one the source set out and did not perform.** The Quiet Spike report says
a ground signature was not attempted because the aeroplane's own shocks would overtake the spike's
shocklets `within a short distance below the flight path`. **Weak-shock theory turns that into a
number**, and the equation pass then showed the answer is CONDITIONAL: with geometric spreading it
completes at strength differences of 0.02 and above and never completes at 0.01.

**And the finding that changed the shape of the story.** Mach cutoff, the technique the 2025 executive
order actually rests on, **was measured in flight and published in 1971**, two years before the
prohibition it now helps displace. **That came out of a bibliography, not a sweep.**

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

### Earned in A351, and nine of them are checkers that passed while something was wrong

**A CHECKER THAT SILENTLY VALIDATES STALE OUTPUT IS WORSE THAN NO CHECKER.**
`python3 assemble.py | tail -3 && python3 verify_numbers.py` reports the exit status of `tail`, so a
failed assembly let the verifier run against the PREVIOUS draft and print `all checks pass`. **The
verifier now refuses to run when `body.md` or any input JSON is newer than the draft**, which is
cheaper than remembering `pipefail` every time.

**A TEST THAT CANNOT FAIL IS NOT A TEST.** The test written to lock A351's store fix in place asserted
that eleven titles survive with the tags off. **Two of them were never deleted by their TITLE at all**,
having been removed through their VENUE, so those assertions would have passed with the fix reverted.
**Every title is now asserted ARMED before it is asserted disarmed**, and the venue cases go through
`filter_records` with a venue attached. This is A348's green-without-checking defect in a new costume.

**A TAG SWITCHES OFF ONE PATTERN AND A CONTAMINANT FAMILY CAN BE SPREAD ACROSS SEVERAL.** A351 tagged
`\bwind turbines?\b` and the wind-turbine community-noise literature was STILL being deleted, by a
separate A347 entry matching the same family. **That is precisely the failure `TAGS` exists to prevent,
met from a direction the mechanism does not cover.** It was found by measuring the residual, not by
reading the store. **After tagging, re-measure what is still dropped.**

**A HARD-CODED EXPECTATION IN A CHECKER GOES STALE AND THEN BLAMES THE ARTICLE.** The number verifier
listed the spelled-out words the article happened to use. The store gained two tag families, the prose
correctly regenerated from nine to eleven, and **the checker reported the article as wrong**. A
spelled-out claim needs a spelled-out check COMPUTED FROM THE SAME SOURCE THE PROSE IS.

**AN ANACHRONISM HIDES IN A NUMBER AS EASILY AS IN A SPONSOR'S NAME.** A351's equation pass put a
regulatory limit of 0.11 pounds per square foot into an article dated November 2025. **It is the
interim limit in a rulemaking published in July 2026**, and the prose promised it would `later appear`
in an article that stops before it does. **The corpus back-dates its articles and keeps their BODIES
inside their datelines**, citing later publications only in the bibliography. `verify_numbers.py` now
refuses any year in the prose after the dateline.

**AN UNKNOWN LATEX MACRO FAILS NOTHING.** MathJax 3 loads `noundefined`, which renders an unrecognised
command as red text in the page. **The build passes, `_verify.py` passes, and the rendered audit passes.**
The verifier now carries an allowlist of the packages `tex-mml-chtml` actually provides.

**AND A DOUBLED BACKSLASH IS INVISIBLE TO THAT ALLOWLIST**, because `\\times` contains `\times`. It
came out of an emitter whose escaping had been through a heredoc twice. Checked separately now.

**SYMBOLS COLLIDE AND ONLY A DECLARED TABLE CATCHES IT.** In A351, `T` was the temperature, the N-wave
duration AND the sound-exposure reference time; `L` was the atmospheric lapse rate, the coalescence
distance AND the sound pressure level; `R` was the gas constant and the ground reflection coefficient.
**A regex cannot know what a symbol means**, so the instrument is a declared table plus a refusal to
accept anything undeclared, and maintaining the table is what catches the collision because a second
meaning has nowhere to go.

**A PROSE CITATION LABEL CAN NAME A DIFFERENT PAPER FROM THE ONE ITS ANCHOR POINTS AT.** Survey labels
are emitted from the reference data and cannot drift. **Body labels are typed.** A351 shipped one
reading `Overview of Low-Boom Flight Demonstration Mission` over an anchor whose target is `An Overview
of NASA Sonic Boom Flight Research`, and later a second where two anchors shared one URL. **Nothing
else in this repository sees that**, and the new checker compared 106 labels in the final pass.

**AN INSERTION BREAKS WHAT THE NEXT PARAGRAPH POINTS AT, NOT ONLY THE SENTENCE IT LANDS IN.** A350
learned that an appended equation makes a run-on. **A351's publication review found FOUR referents that
later passes had orphaned**: `the last of these` pointing at a list a new paragraph had come between,
`the same year` twice, and `three years later` counting from a paragraph inserted before it. **After
inserting a paragraph, read the one after it.**

**A PREDICTION IS NOT A MEASUREMENT AND A REPORT WILL PRINT BOTH.** A351 stated that the Quiet Spike
cost its host up to twenty-four percent of its supersonic lateral-directional stability. **That is a
prediction from three aerodynamic models, and the same report says flight measurement contradicted
it.** This is A350's weight-for-drag misattribution on a different quantity.

**DIVIDE BY THE RIGHT DISTANCE.** A351's coalescence percentages used the vertical altitude, and a
boom does not travel straight down. **The ray leaves normal to the Mach cone**, so the path is
`h / cos(mu)`, forty-three percent longer at Mach 1.4. **The error was in the direction that flattered
the argument.**

**A PLANE-WAVE ESTIMATE CAN HIDE A CONDITIONAL.** Dividing a fixed closing rate into a fixed separation
scales identically at every strength, which made A351's coalescence result look independent of its
assumption. **Adding geometric spreading showed it is not**, and the finding holds only above a
strength difference of 0.02. **When a result looks assumption-independent, check whether the FORM of
the estimate made it so.**

**AN IDENTIFIER THAT CANNOT BE VERIFIED DOES NOT GO IN.** `Sonic Boom: Six Decades of Research` is the
standard monograph of A351's subject, named by its own primary sources. The NTRS API returns 404 for it
on four consecutive requests while the citations page returns 200. **That 200 is the single-page-app
shell.** It was dropped and the omission recorded in the Epistemic State.

**READ THE PROGRAMME'S BIBLIOGRAPHY. IT IS WORTH MORE THAN A SWEEP.** A351's primary pass ran a
dedicated 1,232-record sweep of the report registries, which yielded 66 records. **Reading three
bibliographies doubled the curated set from forty-two to eighty-four.** This is the A350 finding
confirmed, and it should now be the FIRST move of a primary pass rather than the last.

**AUDIT WHICH EQUATIONS CARRY NO CITATION. THAT IS THE MISSING STEP.** Sixteen of A351's thirty-one
display equations had none, because the equation pass had made a dozen subjects load-bearing that the
draft had correctly treated as background. **The four-pass rhythm has no step that re-asks whether an
absent subject has become load-bearing**, and this audit is it.

**A CLUSTER RANK IS A NUMBER AND IT MOVES.** A351 called its shaping cluster the fourth largest and
three reference passes made it the fifth. **Emit ordinals from the data with an ordinal table.**

**RE-GATE EVERY SWEEP WHEN THE STORE CHANGES, AND RE-TAKE THE STORE'S OWN NUMBERS.** A pattern is
global. Re-gating only the sweep that motivated it leaves the corpus as the union of two instruments,
and the four store numbers the article states must be measured with the store as it finally stands.
`merge_sweeps.py` in `tmp/a351/` is the pattern.

**A COMPREHENSIVE SURVEY IS NOT A CITATION LIST.** A351's primary pass left a paragraph reading `the
article describes X, Y and Z` with fourteen citations and no content. **Give each group of citations a
fact**, or the reference count rises while the article says nothing new.

**THE AGE PROFILE OF A LITERATURE IS ITSELF A FINDING.** A351's report primaries have a median year of
1982 against 2008 for its corpus, a gap of twenty-six years, **so its report-primary fraction reports
when the subject was funded rather than how the article was researched.** Its publication rate also
fell in exactly the decade following the cancellation and the prohibition. `_lib/survey.py`
`period_stats` gives the median and the shares; the per-decade rate is worth computing beside it, and
**the 2020s are not a full decade, so compare rates rather than counts.**

### Earned in A349 and A350, and the first five are about a check that looked right and was not

**AN ORACLE THAT CANNOT SEPARATE `ABSENT` FROM `UNREACHABLE` WILL CONDEMN GOOD DATA.**
`openlibrary.org/works/<key>.json` returns HTTP 500 for records that plainly exist and **returns 500
for keys that do not exist either**. `_lib/booklinks.py` collapsed both into `None` and reported both
as mismatches, and running the A342-to-A346 book repair against that measurement **would have rewritten
correct citations**. The module now reads the search index, which answers with a title and an author
for a real key and with nothing for a bogus one, and `resolve` returns `found`, `absent` or `unknown`
while `check` returns `ok`, `wrong`, `missing` or `undetermined`. **`Could not be determined` must
never be readable as `wrong`.** That is the third time this corpus has paid for it, after A347's SSL
error nearly condemned 1,051 citations and A348's transient book mismatch.

**A PROBE THAT NAMES A CONCEPT IN THE AUTHOR'S WORDS MEASURES THE AUTHOR.** A349 probed
`names are refused before use` and got **two records**, then 203 once the probe was allowed to say
look-alike and sound-alike. Spoken-against-written confusability went 46 to 273 the same way. **A350
checked this first** and found its three thin shelves genuinely thin. **Always restate a thin probe in
the field's vocabulary before concluding anything about the field.**

**A REWORDING AND A HARVEST ARE DIFFERENT MOVES AND MUST BE REPORTED SEPARATELY.** A350's leading-edge
shelf went 34 to 58 by rewording and 58 to 145 by sweeping. **Reporting only the endpoints would credit
the sweep with work the vocabulary did**, which is the shape of A348's fragment that credited one
supplementary sweep with four sweeps' results.

**A COMPLETION TOKEN IS ONLY EVIDENCE IF THE LOG IS KNOWN TO BE FRESH, AND A PROCESS WAIT CAN MATCH
ITSELF.** Three build-wait failures in two articles. A349's audit ran before the build finished and
reported the previous run's numbers. A350's draft pass waited on `pgrep -f "jekyll build"`, **and the
waiting shell has that string in its own command line**, so the loop matched itself and three
accumulated while the build had long since finished. A350's primary pass waited on the log for
`done in` and matched the previous build's line, then audited a `_site` that had just been deleted.
**What works: delete the log first, then wait for BOTH the completion line and the site directory.**

**MULTIPLY THE COLUMNS OF ANY TABLE A SOURCE ONLY SETS OUT.** A350's flight test report gives actuator
force, horn arm and structural limit in adjacent columns, and the draft reproduced all three without
multiplying the first two. **Force times arm is a moment in the same units as the limit**, and doing it
showed that three of four wing surfaces carry actuators strong enough to break their own structure,
which explains the entire flight-test caution regime the draft had reported as an unexplained list of
procedures. **A source that has done the measuring has not necessarily done the arithmetic.**

**A CONCLUSION WRITTEN BEFORE HALF THE FINDINGS EXIST WILL NOT MENTION THEM.** A349's conclusion
predated the subsection the primary pass added, and A350's predated three sections the two later passes
added. **Both were flagged as the specific risk before the read and both were confirmed by it.** The
opening-against-conclusion read has now found a defect in **six consecutive articles**.

**AN OPENING THAT COMPRESSES MUST NOT OUTRUN WHAT THE BODY QUALIFIES.** A349's opening asserted an
auditory mechanism the registry does not give and the article's own Epistemic State calls unknown.
A350's said `It worked` where the body spends three sections qualifying it. **Compression is allowed;
asserting more than the body supports is not.**

**RETRIEVAL ARITHMETIC MUST BE EMITTED ONCE SWEEPS ACCUMULATE.** A349's Source Base said 4,993 records
retrieved and 2,337 through the gate, and both were right and could not both stand in one sentence
after two later sweeps fed the pool. **Each pass added a sweep without revisiting the sentence that
counted them.** Emit the total.

**REPORT BOTH KINDS OF PRIMARY.** The corpus-wide measure counts report-server and defence-registry
identifiers. **A349's primary documents were three issues of a joint instruction, a designation
registry, a drug regulator's guidance and a civil aviation study, and not one carries an identifier the
measure can see.** A350 added journal papers the measure also cannot see. Report the fraction and the
count of named primary documents beside it, and **do not change the measure to flatter the number**.

**A FILTER BUILT TO REMOVE NAMING-THAT-IS-NOT-THIS-NAMING CAN REMOVE THIS-NAMING.** A349 wrote a store
pattern against biological nomenclature that anchored on `generic name`, **which is the taxonomic term
and also the pharmacist's term for a nonproprietary drug name**, and on `taxonomy`, which is the
general word for any classification. It deleted look-alike and sound-alike drug-name papers and a
controller-to-controller communication taxonomy. **Only reading its own drops found it.**

**A SUPPLEMENTARY SWEEP MUST NOT RELAX THE GATE OR THE STORE.** Loosening either raises the primary
fraction by admitting records the first sweep correctly refused, which improves the number and not the
article. A349's report-registry sweep returned **1,196 records of which seven passed**, and that is a
measurement about the subject.

**AN INSERTION APPENDED TO A COMPLETE PARAGRAPH PRODUCES A RUN-ON.** A350's equation pass did it three
times, each giving a full stop followed by a comma, and twice placing an equation before the sentence
it depends on. **A regex for that signature now runs over the assembled article.**

**`The Leading Edge` IS A GEOPHYSICS JOURNAL.** A sweep for the leading-edge flap as a roll effector
returned its digital editions, a microseismic moment-tensor inversion and an interview with a
geophysicist. **In a general bibliographic index the aeronautical sense of that phrase is the rarer
one.**

**READ THE DOCUMENT, NOT THE DESCRIPTION OF IT, AND THIS COST TWICE IN ONE ARTICLE.** A349's whole
argument rests on what an instruction does and does not contain. Separately, a web summary gave the
drug regulator's moderate similarity band as beginning at 50 percent and **the guidance says 55**.

**AN ANACHRONISM HIDES IN A SPONSOR'S NAME.** A350 had the Air Force Research Laboratory sponsoring a
programme that ran from 1984, and **that laboratory was formed in 1997**. The predecessor is named in
the source's own first reference.

---

### Earned in A347 and A348, and every one of them is about an instrument failing quietly

**A WARNING ADDRESSED TO A READER IS NOT A MECHANISM, AND THIS COST 48 PERCENT OF AN ARTICLE'S POOL.**
A346 recorded `ramjet` as a contaminant and A347 recorded `hypersonic|scramjet` and `missile`, and
**both entries carried written warnings not to reuse them where those families are the subject.** A348
was the X-51. Those three patterns would have deleted **3,408 records, being 48.1 percent of everything
harvested**, including scramjet flameholding and waverider aerodynamics. The warnings were honoured
only because the article happened to check. **`homonyms.TAGS` now exists**, a caller switches patterns
off by name, and an unknown tag raises rather than being ignored, because the quiet failure is an
article believing it disabled a filter while its own subject is still being deleted.

**A CITATION WHOSE TEXT IS RIGHT AND WHOSE TARGET IS WRONG IS INVISIBLE TO EVERY CHECK THAT DOES NOT
READ THE TARGET.** A347 checked its inherited book identifiers against OpenLibrary for the first time
and **nine of ten pointed at unrelated works**, Leishman's `Principles of Helicopter Aerodynamics`
resolving to a market outlook for dark rum in Japan. The link resolved, the block was well formed, the
rendered label read correctly, and every existing check passed. **`_lib/booklinks.py` is the
instrument**, and it caught six more wrong identifiers in A348 one article later, while the two
carried forward from A347's verified set stayed right. **A hand-typed identifier is wrong almost every
time and a verified one stays right.**

**A CHECK CAN GO GREEN WITHOUT CHECKING ANYTHING.** A348's conclusion described a range as `about a
twentieth` when it is one part in 18.5 to one in 12.3. Correcting it to `between a twelfth and an
eighteenth` left a claim written in words, so the digits `12` and `18` were added to the number
checker. **Both passed, on `18.8`, on `18,500` and on the X-12 backlink in the opening sentence.**
That is the A342 defect class in a new costume. **A spelled-out claim needs a spelled-out check**, and
`verify_numbers.py` now verifies ordinals as words.

**A SEPARATOR OR A WORD BOUNDARY WILL DEFEAT YOUR OWN DIAGNOSTIC, AND IT HAS DONE SO FOUR TIMES.**
A345's `\bX-?48\b` could not match `X-48B`. A347's `\bcompressor\b` could not match `COMPRESSORS`.
A348's contamination probe matched `urban` inside `disturbance` and reported 48 on-subject papers as
contaminants, and its Hyper-X probe reported **2 records where there were 16**, because
`flatten_separators` turns `Hyper-X` into `Hyper X`. **Every one reported the DATA as wrong when the
DIAGNOSTIC was wrong**, which is the dangerous direction, because it argues for work that is not needed
and hides work that is. **`survey.loose` now splits on hyphens as well as spaces.** Use it for any
probe naming a designation or a hyphenated programme.

**A BROKEN CHECK REPORTS THE DATA AS BROKEN, AND THE SAME LESSON ARRIVED TWICE.** A347 sampled ten
report identifiers, requested each address, and all ten failed. **The failure was a certificate error
in the checking script**, and registry checks against Crossref found every one registered. A348 then
saw one book identifier return nothing on a single run and resolve on two more. **Re-run before
concluding, and verify against a registry rather than a status code.**

**GENERATED PROSE IS PROSE.** A342's defect class was fixed by emitting survey statistics from the
reference data so they cannot go stale, and A347 and A348 extended that to the commentary and the pool
counts. **A348's publication review then read the article and did not read what the emitters
produced**, and shipped `1 record in 5,976` into a build, using a numeral where the house style spells
small numbers out, along with a sentence crediting one sweep with figures four sweeps produced.
**Read the emitted fragments before freezing.** Fix them in the emitter, never in the article, or the
next regeneration undoes it.

**FINISH THE ENTIRE PROSE READ BEFORE STARTING THE BUILD.** A347 started three builds and killed two,
each time because the article changed after the build began. A348 started two and killed one, for the
reason above. **The build is roughly a quarter of an hour and a killed one costs all of it.**

**A NUMBER THAT APPEARS ONLY IN A CONCLUSION IS A NUMBER NO CHECKER HAS EVER SEEN.** A347's conclusion
compared its disc loading to a Black Hawk's and nothing in the article computed it. **Reading the
opening against the conclusion has found a defect in four consecutive articles**, so do it first.

**A SUBJECT THAT DOES NOT MOVE WHEN IT IS AIMED AT IS REPORTING SOMETHING ABOUT THE FIELD.** A348 wrote
sweeps for endothermic fuel and for engine cycle analysis and neither moved. **Verified against what
the repositories returned rather than inferred from the pool**, eighteen of 3,660 records touch the
first and five touch the second. Fuel heat-sink measurement and cycle accounting are things a
contractor measures and does not publish. **Say so in the Source Base rather than harvesting again.**

**AND THE MEASUREMENT THIS SERIES HAS NOW PAID FOR THREE TIMES.** A342 measured span of control at
eleven records and left it. A347 measured where analysis effort goes at 65 and left it. A348 measured
whether the engine was the limiting item at 34 and left it. **A bibliographic survey is a poor
instrument for a claim about how a programme allocated its attention.** Do not buy it a fourth time.

---

### Earned in A345 and A346, and the first four are about instruments rather than subjects

**A LESSON RECORDED AS PROSE IS NOT AN INSTRUMENT.** This is the same rule as
`PROSE WARNING A READER ABOUT A DEFECT DOES NOT PREVENT THE DEFECT` below, met from the other side,
and the pair is worth reading together. A344's publication review reported that its
refused records included a substantial literature on estimating the weight of a foetus. That went into
three process files as prose and into `_research/homonyms.py` not at all. **A346 made `weight
estimation` an anchor and thirteen clinical records walked in**, including foetal weight estimation by
Johnson's formula. **When you observe a homonym, add the pattern in the same commit as the sentence.**

**A SEPARATOR DEFEATS A GATE AND CLUSTER ASSIGNMENT, NOT ONLY AN AUDIT PATTERN.** A344 fixed audit
patterns with `survey.loose` and nobody applied the rule to gates. **A345's gate refused 57 records on
a hyphen alone**, among them its own keystone subject and the subject of its second aeroplane, and the
same separator was silently misfiling 195 records into the residual. **`gate.flatten_separators` now
does this for every gate**, flattening only a hyphen between two LETTERS so that `X-48B` survives.

**A CLAIMED ABSENCE MUST BE VERIFIED AGAINST THE SEARCH ENGINE AND NOT AGAINST THE POOL.** A345
measured zero records naming the X-48 in a pool of six thousand and was about to publish that as a
fact about indexing. **The pattern was `\bX-?48\b`, and a word boundary after `48` cannot match
`X-48B`.** The records had been there all along. A346 made the same claim about the X-49, **tested the
search engines directly, and the claim held**, which is the only reason it is in that article.

**PRIMACY IS A PROPERTY OF THE DOCUMENT AND NOT OF THE SWEEP THAT FOUND IT.** A DTIC report carries a
Crossref-registered identifier under the `10.21236` prefix, so it arrives under two labels. A345 held
101 such urls twice, deduplication kept the `crossref` label for 95, and **133 report primaries were
counted as secondary.** Derive primacy from the identifier.

**ASK FOR THE AEROPLANE BY NAME.** A345's first harvest asked for its subject matter and never named
its aircraft, so the documents carrying its whole argument had to be cited by identifier, which looked
like foresight and was covering for a gap. **A346 applied that one article later rather than
rediscovering it**, which is what these rules are for.

**A THIN MEASUREMENT IS A QUESTION AND NOT AN ANSWER, AND THIS REVERSES A340 THROUGH A344.** Those
articles measured conclusions thin and broadening moved nothing, because their subjects had genuinely
small literatures. **A345 opened eight of eleven and A346 opened seven of seven by restating the
question in the field's words.** A346's keystone went 12 to 64 on rewording alone. **Measure both
columns from the start.**

**DO NOT RE-BUY A MEASUREMENT THE SERIES HAS ALREADY PAID FOR.** A346's designation subject measured
6 and was deliberately not harvested, because **A341 already ran that experiment** and eight queries
for designation systems and nomenclature returned Massachusetts tax valuations of 1771, salmonella
serotype naming and dental implant designation systems. **Cite the earlier measurement and move on.**

**AN ARTICLE MUST NOT NARRATE ITS OWN DRAFTING HISTORY INSIDE ITS ARGUMENT.** A345's primary pass left
`the draft of this article argued` and `the part the draft got wrong` in What the Data Changed. **A
reader has no access to a superseded draft.** State the corrected position directly and put the
correction in the Epistemic State, which is what that section is for.

**A NUMBER TYPED RATHER THAN MEASURED FAILS IN THE DIRECTION OF THE STORY.** A345's publication review
typed three values into its own results table and **all three were wrong**, the leading-edge row
written 194 and measuring 89. A346's conclusion said the 1965 aeroplane flew on `a third of the power
per pound` when its own equation gives three-quarters. **Emit tables from the data and have the
verifier reproduce them.**

**A VERIFIER'S PARSE BECOMES AMBIGUOUS AS THE ARTICLE GROWS, EXACTLY AS AN ARTICLE'S DOES.** A346's
results-table parse also matched the promoted-subjects table, because two of its rows share a
four-column shape. **Scope a parse to its own section, and have the verifier fail when it parses a row
it does not recognise**, which is how this one was caught.

**A BUILD OF SUPERSEDED BYTES VERIFIES NOTHING.** A345 started its production build three times
because the article kept changing after the build began. **Freeze the article, checksum the stub copy
against the draft, and only then build.** Both A345 and A346 now record a matched checksum.

### Earned in A343 and A344, and the first three are about the instruments rather than the subject

**A SUBJECT CORRECTLY ABSENT IN ONE PASS CAN BE MADE LOAD-BEARING BY THE NEXT, AND NOTHING RE-CHECKS
IT.** A344's draft pass recorded an atmosphere cluster of two records as correct, because that article
computed no altitude condition, and wrote that judgement into the process files. **The equation pass
then added a fuel table at Mach 0.75 and 40,000 feet**, which needs the standard atmosphere to become
a true airspeed, and neither the step nor the citation was there. **The four-pass rhythm has no step
that re-asks whether an absent subject has become load-bearing.** The audit at the head of the primary
pass is the only thing that catches it, and only if the subject is in its list.

**PROSE WARNING A READER ABOUT A DEFECT DOES NOT PREVENT THE DEFECT.** TASKLOG.md's Current Task
block carried a paragraph saying it had gone self-contradictory six times through incremental editing
and that a resume channel disagreeing with itself is worse than one merely out of date. **On
2026-09-02 that block stated forty-eight and forty-seven drafted on consecutive lines**, eleven lines
above its own warning, and also named A342 as the last completed article when A343 and A344 were
finished. **The warning was addressed to a reader and the defect was introduced by an editor**, and
those are not the same audience. The count is a count of files on disk, so it is now recomputed rather
than read.

**A PER-ARTICLE GATE FIX FIXES NOTHING FOR ANYBODY ELSE.** A341's gate refused `U.S. Standard
Atmosphere, 1976`, one of its own foundational sources, readmitted it by name and recorded the defect.
A342 then used the standard atmosphere for its engine model and harvested **zero** records about it,
and A343 displayed the relation and also harvested zero. **A subject nobody searched for returns no
records, and an absent cluster looks exactly like an absent literature**, so there is no signal to
notice. The vocabulary is now `gate.ATMOSPHERE` and is named rather than copied.

**AN AUDIT PATTERN IS NOT A GATE AND NORMALISES NOTHING.** `gate.py` normalises typographic dashes so
no subject gate fails on the shape of a dash. **A344's audit asked for `arresting gear` with a space
while the literature writes `ARRESTING-GEAR CABLE`**, and the subject measured 4 records where the pool
held 12, and 40 where it held 72, with nothing harvested between. **Use `survey.loose` for compound
technical nouns.**

**A CHECKER THAT FIRES ON ALMOST EVERYTHING IS THE PERMISSIVE-GATE FAILURE WEARING DIFFERENT CLOTHES.**
A diagnostic was built for the hyphen problem, flagging every literal space a hyphen could defeat. Run
over one article's twelve audit subjects **it flagged eleven**, including `span of control` and `probe
and drogue`, which nobody hyphenates. **It was measured and abandoned in favour of a builder**, and
the refusal is recorded in the docstring because it is the more useful half. **Making the right thing
easy beats warning about the wrong one.**

**A RECORD THE GATE ADMITS IS NOT A RECORD ABOUT THE SUBJECT.** The gate admits on any anchor while an
audit measures one, so a large admitted count is not evidence of coverage. A344's publication review
saw 1,139 records returned and 648 admitted for a subject that measured 10. **Volume arrives and
coverage does not**, and the reflex that a thin measurement means a narrow pattern is right often
enough to be dangerous.

**A BEFORE AND AN AFTER MEASURED WITH DIFFERENT INSTRUMENTS ARE NOT A COMPARISON.** When a pattern is
corrected mid-pass, re-measure both columns with the corrected one and print all four numbers.

**A PRESENCE CHECK GOES GREEN PRECISELY WHEN A NUMBER GOES STALE.** A342 shipped a survey paragraph
wrong in all six of its statistics past a verifier that confirmed the string was still there.
**Recompute every stated statistic from the data**, which is what `_lib/survey.py` exists for, and use
presence only for words. A spelled-out number is still a number and needs a word-to-integer parser.

**A PATTERN THAT WAS UNAMBIGUOUS WHEN WRITTEN STOPS BEING SO WHEN THE ARTICLE GROWS.** A344's verifier
matched its arrestment table by a regular expression that became ambiguous the moment the equation
pass added a hook-load table beginning with the same cells. **A verifier that parses the article is
better than one carrying its own copy of a value, and it still needs re-reading when the article
changes.**

**AN ARTICLE'S OWN ARGUMENT CAN BE OUT OF SCOPE FOR ITS OWN GATE, AND THAT IS CORRECT.** A343's claim
about a requirement standing in for a measurement belongs to information science, and A344's claims
about which constraint is active and how estimates compare to outcomes belong to design methodology.
**An aeronautical gate refuses both correctly**, and a gate that admitted them would be the wrong gate
for the rest of the article. **Say so in the Source Base and let the claim stand on the arithmetic.**

**DIMENSIONAL REASONING CAN SETTLE A READING THE RECORD LEAVES OPEN.** A344's draft printed two
readings of an arrested landing and said the record does not choose. **A stopping distance measured
aboard a ship is a deck distance and must pair with a deck-relative speed**, and the aeroplane's own
wing loading made one reading of the quoted speed implausible. **Print both, say which is better and
why, and do not pretend a document settled it.**

**REMOVING GATE ESCAPES IS SAFE ONLY INSIDE A PASS THAT REGENERATES EVERY COUNT.** A survey states its
own counts in prose, so deleting a record otherwise desynchronises the article from its data. **In
that one window it is safe**, and the anchors the argument cites must be protected by name.

**A LATER ARTICLE CAN SCORE AN EARLIER ONE AND SHOULD.** A343 sized a requirement with no aeroplane to
measure and named its weakest assumption. A344 had the aeroplane, and that assumption failed in
exactly the named direction. **A prediction recorded with its own weakest link is worth more than one
recorded without, precisely because the next article can grade it.**

### Earned in A341 and A342, and the most transferable of them is the first

**PROBE THE SURVEY WITH THE ARTICLE'S CONCLUSIONS AND NOT ONLY ITS TOPICS. THIS HAS NOW FIRED IN THREE
CONSECUTIVE PUBLICATION REVIEWS.** The first three passes harvest for what the article is about, and
nobody harvests for what it turns out to conclude. A341's strongest result was that pure thrust
vectoring fails a crosswind landing, and crosswind landing had **40 records**. Its second identity was
engine-out trim, which had **7**. A340 found the same shape. **A conclusion is a claim about a subject
and the survey has to cover that subject.**

**THERE IS A FOURTH KIND OF THIN AND IT CANNOT BE HARVESTED AWAY.** The three known kinds are work
never done, the wrong heading, and a subject so settled it stopped generating papers. **The fourth is a
subject whose vocabulary does not discriminate.** A341's framing subject was a designation collision,
and eight queries for designation systems, nomenclature, records management and classification returned
**1,510 records including Massachusetts tax valuations of 1771, salmonella serotype naming and dental
implant designation systems**. Thirteen survived an aerospace gate and every one was component
nomenclature, the wrong sense of the word. **A cluster of thirteen off-subject records is worse than no
cluster, because it looks like coverage.** It was built, read and removed.

**A RENDERED-OUTPUT AUDIT CANNOT SEE A DISPLAY EQUATION DEMOTED TO INLINE, AND THE FIX IS A COUNT
COMPARISON.** An edit put `$$...$$` and the next paragraph on one source line, kramdown rendered inline
math with two sentences run together, the delimiters balanced and the markup resolved, so `render.py`
reported a clean page. **It was found by counting display equations in the source against `\[` in the
rendered HTML and getting 59 against 58.** `lint.py` now carries `math-display-inlined` as a defect and
**it fired again on the very next article**. Run the count comparison anyway, since it is one line.

**A TOLERANCE TIGHTER THAN THE QUOTED PRECISION IS A FALSE ALARM AND NOT A CHECK.** A342's number
verifier reported the article wrong for writing 6.5 where the computation gives 6.461, which is a
correct rounding to the one decimal the table uses. **Derive the tolerance from how precisely the value
was written**, not from habit. This is the mirror of the A324 rule about tolerances that are too wide.

**TYPOGRAPHIC PUNCTUATION MUST BE NORMALISED BEFORE THE GATE MATCHES, AND IT NOW IS, IN THE LIBRARY.**
A334 recorded this and said to carry it forward. **A342 did not carry it forward and the gate refused
one of its own foundational sources because the publisher sets `Human-Robot` with an en dash.** A
per-article fix had already failed once, so `_lib/gate.py` normalises dashes and quotes for every gate,
with a regression test over six code points. **Re-running one harvest through it admitted 23 records
that were being refused on the shape of a dash alone.**

**A GATE WRITTEN IN A FIELD'S CURRENT VOCABULARY CANNOT REACH THAT FIELD'S ORIGIN.** A342's gate
refused `Remote Manipulative Control with Transmission Delay`, published in 1963, because it predates
`latency`, `teleoperation` and `supervisory control` as terms of art. **That is not a defect and no
anchor list fixes it.** The only remedy is to know the document exists and fetch it by identifier, and
the paper turned out to establish that supervisory control was invented as an answer to latency.

**WHEN THE KEYSTONE LITERATURE IS NOT THE ARTICLE'S FIELD, DECLARE THE SECOND ANCHOR FAMILY BEFORE THE
HARVEST.** A341 rejected two of its own foundational sources and readmitted them by name. A342 wrote a
supervisory-control family into the gate in advance and its keystone cluster holds a thousand records.
**The same lesson, applied in advance, costs nothing and applied afterwards costs a re-harvest.**

**THE DEFINITION OF PRIMARY MUST FIT THE SUBJECT, AND SOME SUBJECTS SPAN TWO FIELDS.** A NASA report is
primary for A342's aerodynamics and an ACM conference paper is primary for its fan-out relation.
**A definition admitting only the first would report the article's own keystone literature as entirely
secondary.** State the definition in the Source Base rather than leaving it implied.

**DIVIDE THE NUMBERS YOU HAVE ALREADY TABULATED.** A342's specification table carried both aircraft's
payloads and gross masses for two passes before anyone divided them. **The payload fractions agree to
four significant figures**, which explains a near-cubic mass scaling that the draft had called a
coincidence of mission sizing. **A scaling exponent arriving from the mission looks identical in the
arithmetic to one arriving from the shape and means something entirely different.**

**CHECK THE SUSPICION BEFORE REPORTING IT, BECAUSE MINE KEEP FAILING.** A342 expected to report the
X-45C's quoted thrust as an error against its engine family. Tested against the vehicle's own stated
ceiling it is admissible and **pins the aeroplane's lift to drag ratio at 16.3 or better**, which no
source publishes. **My first attempt at that check omitted the ram term and reached the opposite
conclusion.** Two figures that corroborate is a weaker result than an error and a truer one.

**THIS SERIES CITES BACKWARD ONLY AND A FORWARD REFERENCE FAILS THE BUILD.** A342 cited A343 and A344
in its first draft. **Reference integrity caught it before the build did**, which is the cheaper of the
two ways to find out.

**I REINTRODUCE CAPS-EMPHASIS SPANS ONCE PER PASS AND IT IS NOW THE MOST RELIABLE DEFECT I PRODUCE.**
The 2026-08-14 audit cleared nine from the corpus. I have put three back across A341 and A342, every
one in newly written Source Base prose. **Scan for three or more consecutive all-capitals words before
finishing any pass**, and expect a false positive on legitimate acronym lists such as `AIAA, SAE, ACM`.


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

**A GROUPING DEFECT MADE A GATE SIMULTANEOUSLY TOO PERMISSIVE AND TOO NARROW, AND NO COUNT SHOWED IT.**
A337 and A338 write the order-free qualifier as `(?=.*(?:{p}))` because A336 wrote it as `(?=.*{p})`.
With an alternation inside, the second form parses as `(?=.*first)` OR `second` OR `third`, so **the
alternation escapes the lookahead and the conjunction silently becomes a disjunction of bare words**. It
admitted any title containing `maintenance` while refusing `Domain Name System`. **Correcting it moved
one cluster from 7 records to 132.** Group every part.

**A SURVEY AUDIT MUST TEST THE CONSTRUCTS THE ARTICLE REASONS WITH, NOT ONLY ITS SUBJECT.** Two
consecutive publication reviews found a displayed subject at or near zero. A337 displayed **relative
density** as the canonical similarity parameter and the survey held **none**. A338's central construct
is the **entry corridor** and the survey held **nine**. **The first harvest asks for what the article is
about and misses what it reasons with**, every time so far. Audit against the article's own load-bearing
vocabulary before the publication pass ends.

**AUDIT THE SUPPLEMENTARY HARVEST TOO, NOT ONLY THE FIRST.** A337 read samples of its first gate and not
of the supplementary one, and **two homonym families entered through the new anchors**, being `relative
density` as a soil-mechanics term for the packing of granular soil and `moment of inertia` as a nuclear
physics model. **44 records, 10.6 percent of that supplementary set.** A338 audited its supplementary set
and it came back clean.

**A PUBLISHER-PREFIX CHECK HAS NOW BEATEN THE RANDOM SAMPLE THREE ARTICLES RUNNING.** Scan the reference
list for identifiers whose prefix does not belong to the field. A clinical-psychology prefix exposed
`subscale` as a psychometrics term. A condensed-matter prefix exposed the **nanofluid stagnation-point
flow** literature, which shares `stagnation point` and `heat transfer` with reentry aerothermodynamics
and shares no physics, at **97 records, 2.2 percent of A338's corpus**. **Make the prefix scan routine.**

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

### On merging and assembly, earned in A337 and A338

**AN ANCHOR DERIVED FROM AUTHOR AND YEAR IS NOT UNIQUE, AND A MERGE THAT ASSUMES IT IS WILL REPOINT A
CITATION SILENTLY.** A337 hand-assigned slugs for its primaries, two of them already existed as harvested
anchors, and the merge overwrote both **without erroring**. **Nothing showed it except an off-by-two in
the harvested count.** One collision was the same work registered twice; the other was two different
papers by the same author in the same year. **Pass every existing anchor as `taken` and raise on any
intersection**, which A338 did, returning zero.

**DO NOT PATCH A COUNT IN PROSE WITH A REGEX THAT SPANS HEADINGS.** A337's cluster-count updater used a
non-greedy pattern that reached past its intended heading, so two clusters carried their neighbours'
counts and **the stated totals disagreed with the data by as much as 173 records**. The display sizes
exposed it, two clusters showing 14 entries where the prose claimed 25. **Rebuild every cluster block
from the harvest files rather than editing it**, so each count is derived.

**A TEMPLATE THAT IS EDITED RATHER THAN REWRITTEN WILL LEAK.** A338's Source Base was adapted from
A337's and carried three of its sentences unaltered, including a finding about animal-behaviour apparatus
belonging to that article and **a reference to the wrong vehicle**. **Sweep a new article for the
previous one's vehicle names and findings before the publication pass ends.**

**TWO LIBRARY CALLS HAVE SHAPES THAT FAIL SILENTLY.** `refs.dedupe` returns `(kept, dropped)`, so binding
it to one name yields a list of two lists and the next stage emits a survey of **two** records without
raising. `refs.clean` was being applied to titles and not to author names, so an HTML entity reached the
link text undecoded and rendered correctly enough that nothing complained.

**A VERIFIER THAT SHARES AN INPUT WITH THE THING IT CHECKS DOES NOT CHECK THAT INPUT.** A337 and A338
each carry a `tmp/aNNN/verify.py` that recomputes every published result **from the source units**,
converting them itself, and shares no code with the draft. A337's runs 55 checks.

---

### On measurement and citation, earned in A373

**MEASURE AUTHOR PROSE, NEVER THE RAW BODY.** A373 carries 459,066 raw body words against **8,522 words
of author prose**, a **dilution factor of 52.7**, the highest in this corpus. Measuring the raw body
divides every word rate by fifty and **guarantees the instrument reports nothing**. `diction.prose` strips
link pairs and is the only reason a word pass on a harvested article can fire at all.

**THE TIC IS OFTEN A TEMPLATE, NOT A WORD, AND NO SINGLE-WORD INSTRUMENT CAN SEE IT.** A373's finding was
thirteen survey subsections opening with an identical frame and closing with an **identical hedge**. Run
`diction.repeated_ngrams` as well as the word check. **The fix is not deletion**, since the hedge was
load-bearing; state it **once, structurally, with the reason that a hedge repeated on every heading stops
being read**, which is what A337 did for `typically`.

**WHEN THIRTEEN SCATTERED COUNTS SAY THE SAME THING, A TABLE SAYS IT BETTER.** Replacing A373's thirteen
frames with one table removed the boilerplate **and gave the reader comparability they did not have**. The
table's shape then turned out to be a finding in its own right.

**A DERIVED FIGURE MUST BE COUNTED FROM THE ARTEFACT, NOT READ FROM THE PIPELINE LOG.** A373's source base
claimed **13,788 harvested works against an anchor gate that passed 13,741**, which is impossible, and the
reference list actually held **13,722**. **A number that cannot have happened survived four passes**
because nobody counted the list. Count the list.

**A STATUS CODE IS NOT A CITATION CHECK, AND CHECKING RESOLVABILITY IS NOT CHECKING THE WORK.** Three of
A373's most foundational citations resolved perfectly and pointed at the wrong works, **Shannon 1948
resolving to a 2009 encyclopaedia entry about the paper**. Compare every inline citation's label against
the registered title, which `citations` does and `resolve` does not.

**THE SAME TRAP CATCHES YOU WHILE YOU ARE FIXING IT.** Hunting a replacement identifier, a candidate Open
Library key returned **HTTP 200 and resolved to `Motor Racing (Inside Story)`**. **Never paste an
identifier you have not opened.**

**WHERE NO IDENTIFIER EXISTS, A STABLE PUBLISHER URL IS STILL A CITATION.** Four works were named in A373's
prose with nothing behind them because USENIX and the storage conference register no identifiers.
**Lacking an identifier is not the same as lacking a citation.** Where not even that exists, name the work
without a link and say why.

**PROVE A BUILD BREAK IS NOT YOURS BEFORE YOU FIX IT.** `./_check.sh --drafts` failed during A373 on a
`post_url` in an unrelated draft. **Reproducing the failure at HEAD with the new file removed** settled it
in one command. The cause was **four `post_url` targets carrying dates from before their drafts were
re-dated**, and the failure is **date-sensitive**, because a `post_url` to a future-dated draft is not
exercised until that date arrives. **Audit every `post_url` target after any re-dating.**

---

### On gates, earned in A339 and A340, and the most reusable thing in this file

**A CONJUNCTION WHOSE TWO HALVES CAN BE SATISFIED BY THE SAME WORD IS NOT A CONJUNCTION.** Writing
`q("booster", AERO)` where `AERO` itself contains `booster` admits anything containing the word once.
A339 found five instances of this. Three were caught by reading audit samples, one by an empirical
probe, and **the fifth only by asserting the property**.

**SO ASSERT THE PROPERTY. Do not hunt instances.** The gate now carries a test that, for every
conjunction, checks that no alternative in one half matches inside another half. **A339 wrote it after
finding four by hand. A340 inherited it and it failed on the first run**, catching `shock`, `combustor`
and `nozzle` before the gate ever touched the corpus. **That is the first time in this series a defect
of that class was caught before it reached a sample**, and it is the strongest argument in this file
for turning a lesson into a test rather than a comment.

**HYPHENS. A PATTERN WRITTEN WITH A SPACE DOES NOT MATCH THE HYPHENATED FORM.** A339 dropped
filament-wound vessel work because the pattern demanded `filament wound`. A340 dropped high-enthalpy,
wind-tunnel and flight-test work for the same reason, and **correcting it recovered 367 records and
more than doubled one cluster**. Write every multi-word term as `foo[- ]bar` from the start.

**THE AUDIT AND THE TESTS COVER DIFFERENT FAILURES AND NEITHER COVERS THE THIRD ONE.** The tests catch
malformed patterns. The two-sided sample catches a gate that is too permissive or too narrow. **Neither
can catch a gate whose QUESTIONS were too narrow**, because both only examine what the queries returned.

**A340 FOUND THAT THIRD FAILURE AND IT IS THE ONE TO WATCH FOR.** The article's most transferable
finding was about margins and uncertainty, and the survey covered that subject with 235 records out of
11,279, because every harvest query had been about hypersonic propulsion. **A survey that under-covers
the subject of its own article's conclusion is not comprehensive.** A supplementary harvest raised the
pool by thirty percent and that coverage from 235 to 908.

**THE TEST TO APPLY, AND APPLY IT AT THE DRAFT PASS RATHER THAN THE PUBLICATION REVIEW.** Write the
article's conclusion in one sentence. Ask which literature that sentence belongs to. **If the harvest
queries do not name that literature, the survey will not cover it**, however good the gate is.

**CROSS-DISCIPLINARY METHODOLOGY VOCABULARY MUST NEVER ADMIT ALONE.** A340's supplementary harvest
admitted `uncertainty quantification` and got laser powder bed fusion, `epistemic uncertainty` and got
seismic shear-wave profiles, `six degree of freedom` and got a robotic arm. **Uncertainty, validation,
sensitivity and margin belong to every field that computes.**

**AND CHECK THE ANCHORS YOU THINK ARE SAFE.** A340 admitted `waverider` bare, because a waverider is an
unambiguous hypersonic configuration. **Waverider is also the make of an oceanographic wave-measuring
buoy**, and the gate collected one deployed during a 1980 field experiment.

**A FOURTH FAILURE, FOUND BY THE 2026-08-14 SWEEP: THE PROBE THAT LOOKS FOR ESCAPES ASSUMES A DOMAIN.**
A series-wide probe flagged 78 off-domain citations, **thirty of them in A336**, which read as the worst
gate escape in the series. **It is not one.** A336's survey states in prose that its subject is not an
aircraft but what a gap in an official register means, and declares eight clusters across archival
silence, classification infrastructure and identifier administration. **The probe had assumed that every
article in an aerospace series is about aerospace.** Before calling a survey off topic, read what the
article says its topic is.

**THE FIX FOR ONE ARTICLE DOES NOT REACH THE ONES ALREADY WRITTEN.** A330 still carries an Indonesian
COVID booster-acceptance study, admitted by the bare `booster` that A339 diagnosed and corrected.
**Every gate lesson in this series was learned incrementally and nothing re-applies a later lesson to an
earlier article**, so each publication review was correct against the standard that existed when it ran.
**The repair is a re-harvest at the gate, not an edit to the artefact**, because every survey states its
own counts in prose and removing records desynchronises them.

---

### On claims about your own corpus, earned in A339 and A340

**THE COUNT-IN-OWN-PROSE DEFECT HAS NOW SHIPPED SEVEN TIMES AND SAMPLING WILL NOT STOP IT.** A339's
first survey draft called two different clusters the smallest, called the keystone cluster the smallest
when it ranked eighth of sixteen, and named as largest a cluster the residual exceeded twofold.

**SO ASSERT THE ORDERING CLAIMS AGAINST THE COMPUTED COUNTS AT BUILD TIME.** Both articles now do, and
**A340's guard caught its own author overstating a ratio as an order of magnitude when it was a factor
of 7.9**. The assembly script refuses to write the draft if any claim fails.

**A DERIVED FIGURE MUST BE COUNTED FROM THE ARTEFACT.** While writing this handoff's predecessor I put
12,547 harvested records into the reverse prompt from memory. **The counted figure was 12,504**, and it
reconciles only against the article's own table plus the curated and series anchors.

**AND IT HAPPENED AGAIN WHILE WRITING THIS FILE.** The series table above first recorded A339 at 21,067
lines, which was its length after the primary-reference pass rather than after the publication review.
**Measuring the file gave 21,099.** A count taken from a previous report is not a count. **Measure the
artefact at the moment you write the number**, including in this handoff.

**AND CHECK THAT A CLAIM ABOUT THE ARTICLE IS TRUE OF THE ARTICLE.** A339's reverse prompt stated that
two weakly sourced dates were flagged in the Epistemic State. **They were not.** The fix was to make the
article match the claim rather than to soften the claim.

---

### On citations and identifiers, earned in A339 and A340

**A STATUS CODE IS NOT A CITATION CHECK AND A 403 IS NOT A DEAD LINK.** A339 sampled 40 harvested
identifiers and 25 returned 403, of which **all 25 were registered works**, nineteen of them AIAA.
**Where a DOI is the identifier, query the registry.** The landing page answers only whether the
publisher feels like talking to curl. `URL_VERIFICATION.md` now records this and lists the publisher
hosts.

**DO NOT CONSTRUCT AN IDENTIFIER BY PATTERN.** A340's draft pass built a designation-reference URL from
the shape of the two preceding articles' URLs. **It does not resolve.** It was removed rather than
replaced with another guess, and the gap is recorded in the article. This is the A373 trap in a new
costume, and the only reason it did not ship is that curated URLs are checked individually.

**VERIFY BOOK KEYS THE SAME WAY.** Both articles resolved every Open Library key and checked the title
and authors, because A373 proved that a guessed key returns a healthy response for the wrong book.

---

### On the NASA design-criteria monographs, earned in A339 and A340

**WHEN AN ARTICLE DERIVES SOMETHING, CITE THE DOCUMENT THE ENGINEERS DERIVED IT FROM.** Both articles
displayed dozens of relations and cited nothing for any of them until the primary-reference pass.

**THE SP-8000 SERIES IS THE RIGHT ANSWER FOR AMERICAN LIQUID PROPULSION AND STRUCTURES.** A339 cites
eight, covering self-cooled chambers, pressurisation, injectors, nozzles, metal tanks, regulators,
flexible lines and slosh loads. **They are primary, contemporary with the practice, and they state the
design problem in the terms the programme's own engineers used.**

**NACA REPORT 1135 IS THE RIGHT ANSWER FOR COMPRESSIBLE FLOW.** A340 uses it for the isentropic
relations, the oblique shock relations and Rayleigh flow. **A 1953 report is the correct citation for a
2004 flight**, because the relations have not changed and it states them better than any textbook.
Kantrowitz and Donaldson 1945, Sutton and Graves 1971, Fay and Riddell 1958 and the 1976 standard
atmosphere are the other four to reach for.

**THE STANDARD ATMOSPHERE IS THE ONE PEOPLE FORGET.** Every flight-condition figure in A340 depends on
it and the draft used it silently.

---

### On markdown hazards, earned in A340

**A LITERAL PIPE INSIDE INLINE MATH AT THE START OF A LINE MAKES KRAMDOWN RENDER THE PARAGRAPH AS A
TABLE.** Absolute value bars do this. **Write `\lvert` and `\rvert`**, which render identically and
carry no pipe. `_verify.py` catches it as a warning and this was the first time it fired.

**AN INSERTED DISPLAY THAT ABSORBS THE FOLLOWING PROSE ONTO ITS OWN SOURCE LINE HAS NOW HAPPENED IN
FOUR ARTICLES.** After every equation pass, scan for lines that open with `$$` and do not close with it.

---

## Verification Toolchain

**THE SHARED MECHANISM IS COMMITTED AND MUST NOT BE REBUILT.** `_lib/` holds it, with `README.md`
describing each module: `fetch` for archive queries, `refs` for anchors and the reference block, `edits`
for guarded editing, `reflow`, `lint`, `diction` for word and phrase overuse, `audit` for equation and
citation gaps, `numcheck` for independent re-derivation, and `citations` for registry verification. Run
`python3 _lib/test_lib.py`, which should report **105 of 105** as of 2026-09-07. **`refs.clean` gained a bare-pipe strip on
2026-08-12**, because kramdown reads a paragraph whose first line contains a pipe as a table and a
publisher-mangled apostrophe entity put one into link text. **Three modules were added on
2026-08-11**, being `gate` for subject-anchor gating with a mandatory two-sided sample, `render` for
auditing BUILT HTML, and `resolve` for identifier resolution. `_research/rejected.json` holds the accumulated
sweep judgements, reused through `_research/homonyms.py`, **whose curated pattern list is now 132.**

**`_lib/booklinks.py` WAS REWRITTEN ON 2026-09-04 AND ITS PREVIOUS ORACLE WAS UNSAFE.** It reads the
OpenLibrary SEARCH INDEX rather than the work JSON endpoint, because that endpoint returns HTTP 500
both for records that exist and for keys that do not. `resolve` returns `found`, `absent` or `unknown`;
`check` returns `ok`, `wrong`, `missing` or `undetermined`. **A failure is never a verdict.** The
search index also returns the AUTHOR, so a key can be held to both halves of an `Author, Title` claim,
which is a higher standard than the gate it has to pass. `author_claim` and `author_agrees` are
reported and not enforced, because repositories list editors and initials inconsistently.

**TWENTY-SIX OF THOSE PATTERNS CARRY TAGS AND CAN BE SWITCHED OFF BY NAME**, across seventeen
families: `civil-structures`, `ecology`, `environmental-assessment`, `geophysics`, `hypersonics`,
`interpreting`, `marine`, `medicine`, `meteorology`, `missiles`, `nomenclature`, `ocean-modelling`,
`ramjet`, `remote-sensing`, `surface-transport`, `teaching` and `wind-energy`. **Eleven of those
families were added by A351 alone**, whose subject was a noise rather than an aeroplane and which
therefore met the whole community-noise literature of railways, roads and wind turbines as its own
subject where the store held it as contamination. **A351 also proved that a family can span two
patterns and that tagging one leaves the other armed**, so after tagging, re-measure what is still
being dropped. **`medicine` covers
five patterns and exists because A349's subject was confusable names**, where every medical pattern in
the store had been earned by aeroplane sweeps and between them they deleted 190 on-subject records. A tagged pattern is one whose subject is somebody else's subject. Pass
`allow=("hypersonics", "ramjet")` to `homonyms.filter_records` and to `noise_hit`, list the tags in
the article's harvest module so the gate and the merge cannot drift apart, **and say in the Source
Base which were switched off and why**. An unknown tag raises. **Only tagged patterns can be switched
off**, deliberately, so that a general contaminant cannot be disabled by accident. A334 and A335 between them added eleven families, and
A342's publication review added six more, all consequences of the word `unmanned` except the
semiconductor sense of `fan-out`, whose discriminating words are in the CONTAINER rather than the
title. Each is listed in the homonym table above with the incident that produced it.

**FIVE CHECKS WERE ADDED TO THE PER-ARTICLE VERIFIER IN A351 AND ALL FIVE FOUND SOMETHING.** They
live in `tmp/a351/verify_numbers.py`, which is gitignored, so they are described here in enough detail
to rebuild. **Every one was proved non-vacuous by injecting the defect and watching it fail**, and
that proof should be repeated when they are carried forward.

| Check | What it caught |
|---|---|
| **Staleness guard** | refuses to run when `body.md` or any input JSON is newer than the draft. A pipe had masked a failed assembly and the verifier validated the previous draft |
| **Prose citation labels** | compares every typed `[[label][anchor]]` in the body to the TITLE its anchor points at. Survey labels are emitted and cannot drift; body labels are typed. Found two |
| **Declared symbol table** | refuses any symbol in math that is not declared with one meaning. Found four collisions, `T`, `L`, `R` and `\ell` |
| **MathJax macro allowlist** | refuses any macro outside the packages `tex-mml-chtml` provides, because `noundefined` renders an unknown macro as red text and fails NOTHING. Also refuses a doubled backslash, which contains the macro it doubles |
| **Dateline horizon** | refuses any year in the prose after the article's own editorial date. Caught a July 2026 regulatory limit in an article dated November 2025 |

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
| `booklinks` | verifies that a book citation's OpenLibrary work key IS the book the article names. **Nine of ten inherited keys once pointed at unrelated works and every other check passed**, because a citation whose text is right and whose target is wrong is invisible to anything that does not read the target. Skips the generated `Author Year` style, which claims no title |
| `survey` | recomputes every statistic an article states about its own reference survey, since **a presence check goes green precisely when a number goes stale**. Carries `words_to_int`, because a spelled-out number is still a number, and `loose`, which **now splits on hyphens as well as spaces** because `flatten_separators` turns `Hyper-X` into `Hyper X` and a probe written with a literal hyphen matches nothing, silently |

**Three additions to existing modules are easy to miss.** `gate.ATMOSPHERE` is a shared vocabulary
naming the medium rather than any aeroplane, and an article's gate must NAME it rather than copy it.
`gate.normalise` folds typographic dashes and quotes so no gate fails on the shape of a dash.
`refs.decap` normalises a shouted title while preserving initialisms, deciding on the whole string
first because `IFAC` and `ON` are the same length.

**THE STUB BUILD TAKES ROUGHLY A QUARTER OF AN HOUR AND ITS COST IS KNOWN.** A345 took 1,940 seconds,
A346 1,548, A347 918 and A348 824, all against checksum-matched bytes and all reporting no findings.
**Budget fifteen minutes, and start it only after the entire prose read is finished, including the
fragments the emitters generate.**

**`_verify.py` gained two checks on 2026-09-01.** `math-display-inlined` catches a display equation
sharing a source line with prose, and `survey-row-count` holds a cluster row's stated count against
the citations on that row. **`_verify.py` runs its whole battery over DRAFTS downgraded to warnings**,
which is why promoting the first was worth doing and where both of its incidents had happened.
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

**`progress-stale` and `progress-contradiction` gate the resume channels themselves**, added
2026-09-02. `_lib/progress.py` counts the drafts of a series on disk and compares that count to what
TASKLOG.md's Current Task block and REVERSE_PROMPT.md claim, reporting a disagreement with the tree
separately from two channels' claims disagreeing with each other. **HANDOFF.md is deliberately
excluded**, because it goes stale by design between refreshes and a count check would fire on it every
time an article is drafted.

**Read `_docs/process/VERIFICATION_TRAPS.md` before trusting any checker you write.** It records the
mistakes this method has actually made and the observation that caught each. The recurring root is
**asserting a property instead of measuring it**, and the most expensive instance was a rendered-math
checker whose second wrong version masked its first.

**The bundle is installed** at `vendor/bundle`, which is gitignored. **The stub build needs it
symlinked in**, and the recipe above now says so after that omission cost A345 two failed builds.

**`_lib/gate.py` GAINED `flatten_separators` ON 2026-09-02** and every gate inherits it. A hyphen
between two letters is flattened before an anchor is tested, the unflattened title being tested first,
so no existing pattern changes meaning and an aircraft designation survives.

**`_lib/progress.py` IS NEW AND SO IS `_lib/survey.py`.** Both exist because a number that could be
recomputed was being maintained by hand. **`_lib` tests are 95 of 95** and the shared sweep store
carries **101 noise patterns**.

**PUSHING CAN EXCEED A TWO-MINUTE FOREGROUND LIMIT**, because the pre-push hook runs the whole corpus
gate over 301 posts and 59 drafts. **Run the push in the background and then confirm the remote head**,
which is what A346's publication review had to do after a timeout left the commit landed and unpushed.

**An HTTP 200 does not verify a citation.**

**Independence matters.** The article's verifier must not import its calculation module.
`_lib/numcheck.py` is the harness, with `prop` for randomised property checks, `bisect` for reaching a
value by a different route, and `require_in_text` to fail when a verified number is absent from the
draft. A323 finds its
maximum lift-to-drag ratio by **scanning the polar**, its decibel-per-doubling by **bisection**, and
tests the helix-angle cancellation as a **randomised property**.

---

## Open Decisions

**Two things need the pilot rather than the agent, and both are unchanged through the whole of
A351.** The agent raised neither again during that article because neither is inside the article in
hand, which is the standing rule.

### RESOLVED on 2026-09-04. The book identifiers in A342 through A346 were repaired

**Twelve anchors and sixteen citations replaced**, every one confirmed on title AND author before it
was written, and every old key confirmed wrong before it was touched. The corpus moved from **283 of
300 to 299 of 300 checkable book citations correct**. Eight replacements were already vetted elsewhere
in the corpus, seven in A347 and one in A324, and four were resolved by fresh search.

**The measurement that made the repair possible had to be rebuilt first**, because the previous oracle
reported correct citations as broken. See the method rule above.

### A324 carries a malformed book label over a correct key, and it is the one live repair

**`book_jenkins` reads `Administration, National Aeronautics and Space, Jenkins, Dennis R...`**, which
is the repository's author field copied verbatim with its ellipsis, so the article's own label
swallowed the title. **The identifier is right and the rendered citation is not.**

**It is the single remaining item in the 299 of 300**, and it is outside A342 through A346, in an
article that has completed all four passes. **The agent reported it rather than editing it**, because
the agent will not touch articles outside the one in hand absent instruction.

### A substantial fraction of OpenLibrary work pages return Internal Error to a reader

**Four of the 22 book URLs in the five repaired drafts failed on two consecutive serial requests**, and
the condition also hits keys A347 shipped and the pilot has already approved, namely Schlichting at
`OL11833044W` and Bramwell at `OL16987916W`.

**No key was changed to chase this.** Selecting an identifier against a transient server fault is the
error the whole book repair was spent avoiding. **If it persists it is a reader-facing problem for the
whole series rather than for any one article**, and it wants its own decision.

### The stub build, whose cost is now known and falling

**A345 took 1,940 seconds, A346 1,548, A347 918, A348 824, A349 between 21 and 39, A350 between 65
and 1,290, and A351 between 92 and 111 across four builds**, all against checksum-matched bytes and
all reporting no findings.

**BUILD TIME IS NOT LINEAR IN THE CORPUS AND THE RANGE IS NOW THREE ORDERS OF MAGNITUDE.** A350's
publication build took 1,290 seconds on 3,682 references where its equation build took 65 on 3,372.
**A351 was remarkably stable at roughly a hundred seconds across all four of its passes** on a corpus
of comparable size, which is evidence that the variance is not in the reference count. **Budget
open-endedly and wait on a condition rather than a duration.** Start it only after the entire prose
read is finished, **including the fragments the emitters generate**, which is the lesson A348 paid
for, and **delete the build log before waiting on it, then wait for BOTH the completion line and the
`_site` directory**, which is the lesson A350 paid for three times and A351 applied without incident
four times.

**The decision left** is whether to run the full corpus build at the publication review only, which is
what has happened since A341, or more often. **The agent will continue with the stub build per pass
and no full build absent instruction.**

### The deploy gate, and the stub build that mostly answers it

**The problem as recorded.** `./_check.sh --drafts` took about thirty-five minutes before A339 and over
three hours by A340's publication review, scaling superlinearly in link-definition count rather than in
article count. With twenty-six articles left at four passes each, that was hundreds of hours.

**What was done instead, and it works.** A341 and A342 were built in a **stub-isolated site**, holding
the article under work in full and every sibling as a front-matter-only stub so `post_url` resolves.
**That renders the article a reader would see in about an hour instead of three**, exercises kramdown
on the real reference block, and lets `render.py` run. The full 346-post corpus build was run once, on
A341's draft pass, and took **six and a half hours**.

**The recipe is in `tmp/a342/stub/` and the script that builds it is a dozen lines**, but that path is
gitignored, so it is written out here. Copy the repository excluding `_posts`, `_drafts`, `_site` and
`tmp`. Put the article under work into `_posts` with its date prefix. Write every sibling series draft
into `_posts` as front matter plus one line.

**ALSO EXCLUDE `vendor` FROM THE COPY AND THEN SYMLINK IT BACK IN**, since it holds the installed
bundle and is several hundred megabytes. **This step was missing from this recipe until 2026-09-02 and
cost A345 two failed builds**, which fail with `Bundler::GemNotFound` listing every gem. Setting
`BUNDLE_PATH` to the real tree does not work, because the stub carries its own `.bundle/config`
pinning `vendor/bundle` as a relative path. `ln -sfn <repo>/vendor <stub>/vendor` does. **The stub site's own `_verify.py` is not run against it,
because the stubs would fail. Run that against the real tree.**

**What the stub build cannot see** is an interaction between the article and another real post, and a
category-slug collision across the whole corpus. **Neither has ever been the defect**, and `_verify.py`
catches the second on the real tree anyway.

**The decision left.** Whether to run the full corpus build at the publication review only, which is
what happened for A341 and A342, or more often. **The agent will continue with the stub build per pass
and the full build at publication absent instruction.**

### RESOLVED on 2026-09-01, and the reason it was promoted is not the one expected

**`math-display-inlined` is now a `_verify.py` check and no longer only a `lint.py` defect.** The
deciding fact was not the incident count. It was that **`_verify.py` runs its whole battery over
DRAFTS, downgraded to warnings**, so promotion makes it a hard error on published posts and a visible
warning on drafts. **Both incidents that motivated it happened in drafts**, so a posts-only gate would
have guarded the wrong half of the workflow.

Measured at promotion at zero across the 174 posts and 47 drafts that then enabled MathJax, and it
costs 0.75 seconds of the gate's 20 seconds of processor time. **The draft figure is 49 now**, since
A343 and A344 both enable it. **It has since fired in A343 and again in A344**, which makes
four consecutive articles in which the equation pass produced this defect.

`survey-row-count` was promoted alongside it, holding a cluster row's stated count against the
citations on that row. **It guards a different failure from the one that motivated it** and the code
says so.

### The caps defect on a live page, and it is two spans rather than one

`_posts/2026-08-06-native_lowering_coverage.markdown` carries **two** authored caps-emphasis spans, at
line 879 reading `worthless FOR THE INSTRUCTION CLASS PROPOSED` and line 1306 reading `to ADD TO A
COMPLETE MACHINE for speed`. **The file was reported as carrying one for weeks**, because the scan
used to find it could not see a run containing a single-letter word.

**Thirteen published posts also carry 1,045 shouted citation titles**, 1,030 of them in the five
compiler articles of 2026-08-06 to 2026-08-10. `refs.decap` now prevents new ones at generation and
repairs none of these. **Both are content edits on published pages with no URL consequence, and the
agent has not touched them.**

### RESOLVED. The designation directory gap was specific to the X-49

**A346 was the first article in fifty with no page in the specialist designation directory.** The
X-50 has one and the X-51 has one, so the gap was a fact about that aeroplane rather than a change in
the source. **Nothing needs deciding.** The original note is kept below because the situation will
recur for some later designation and the handling is already settled.

### The X-49 had no designation-directory entry, and that will recur

**A346 is the first article in fifty with no page in the specialist designation directory**, whose
index runs straight from X-48 to X-50. **That is a fact about the source and not a defect in the
article**, and it is consistent with the designation having been skipped in 2002 and filled in 2004.

**Nothing needs deciding unless the pilot wants a substitute source named** for the articles ahead
that may share the gap. The agent will continue assembling specifications from the manufacturer, the
sponsor and the general press, and saying so in the Source Base, absent instruction.

### Still open from before, unchanged

**The gate re-harvest of the escaped clusters in A323, A326, A328, A329 and A330.** Rare off-topic
citations survive in the earlier articles. They were deliberately not stripped, because every survey
states its own record counts in prose and removing citations desynchronises them. **The repair belongs
at the gate as a rebuild and is a separate unit of work that has not been done.**

**A369's factor-of-roughly-thirty claim awaits the Keleusma decision register**, which is in another
repository.

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

**X-23, X-27, X-39, X-41, X-42, X-44 AND X-52 ARE NOW WRITTEN, and X-30 and X-54 are written although
neither is one of the nine. X-58, X-67 and the leapfrogged X-69 to X-75 block remain ahead**, at A355,
A364 and A366 respectively.

**X-54 IS A FOURTH KIND OF ANOMALY AND THE CLOSER SHOULD CARRY IT.** The X-39 marks a number reserved
and never assigned. The X-52 marks a number requested and refused. **The X-54 marks a number ALLOCATED
IN FULL** — to a named contractor, with a named sponsor, named engines and a mission statement — after
which nothing was built and no cancellation was ever recorded. **It is the emptiest kind of allocation
because it is the most complete one**, and the record contains no decision to point at.

**AND ITS MISSION STATEMENT IS UNIQUE IN THE REGISTER, WHICH IS A MEASURED CLAIM.** Of the 510
designations allocated between August 1998 and November 2025, **exactly one contains the word
`regulatory`**, and `certification`, `rulemaking` and `policy` appear in none. **An aeroplane whose
stated purpose is evidence for a rulemaking has tied itself to a clock it does not control**, and the
rulemaking arrived seventeen years later on a technique the aeroplane was not designed around and
which had been flown in 1971. That belongs in the closer beside the other reasons a designation went
to a vehicle that never flew.

**X-44 IS THE SHARPEST OF THEM AND SET A PRECEDENT WORTH REUSING.** Two aircraft, both Lockheed Martin,
both current in 1999, both recorded as X-44A, one never built and one flown and classified for
seventeen years. **The specialist registry carries no page for the number at all** and the journalism
that broke the story said plainly it could not explain it. The article took the documentation-poor
class and gave the collision its own section, as A320 and A339 did. **When two vehicles share a number,
the collision is the subject and the vehicles are the evidence.**

**THE THREE CLASSES ARE NOW ALL DEMONSTRATED ON ANOMALY CASES.** X-23 and X-27 went to full length
because each had a keystone to dimension. **X-39 took the reduced order** because no vehicle existed at
all. **X-41 took the documentation-poor class**, full section order with short sections, because a
vehicle existed and its specifications did not. **The class is decided by what the record supports, and
the article should say which class it is and why.**

- **X-23**, attributed to the Martin Marietta SV-5D PRIME, but USAF nomenclature records reportedly
  show X-23A was never assigned. State the conflict, do not resolve it. **Written at full length in
  A320, because the SV-5D flew and returned a measurement.**
- **X-27**, never built, mock-up only. **Written at full length in A324, against the previous handoff's
  prediction of the short class**, because the design record carries complete geometry, weights and
  engine ratings, and the parent F-104 flew for thirty years and anchors the derivative's claims. **The
  class test is whether there is a keystone to dimension systems against, not whether anything flew.**
- **X-39**, reserved 23 April 1997 for the AFRL Future Aircraft Technology Enhancements programme;
  no written allocation request followed. **Written in A336 in the reduced order.** The finding is that
  the gap needed **two** missing documents, the allocation request that was never submitted and the
  **cancellation that was never filed**, since reuse requires cancellation before the next number is
  allocated and X-40A was allocated the same year. **The number became unrecoverable before it became
  unnecessary.** The joint instruction permits reserving popular **names** and has no equivalent
  provision for design **numbers**.
- **X-41**, still-classified vehicle in the DARPA FALCON programme. No specifications released.
  **Written in A338 as the first documentation-poor article.** The designation was allocated in late
  1997 or early 1998, **years before the programme**, was never used again officially, and the
  authoritative survey **doubts it ever applied to this vehicle at all**. The article uses the pairing
  because the public record does and says plainly that it may be wrong.
- **X-42**, sources disagreed, one calling it an expendable upper stage and another a spaceplane test
  vehicle. **Written at full length in A339, and the disagreement was not one.** Both sources were
  right about different vehicles four years apart. X-42A was allocated in late 1997 or early 1998 to
  the Upper Stage Flight Experiment, a pressure-fed peroxide and JP-8 stage, and never used officially
  again. In 2002 the laboratory and industry applied X-42 informally to a winged reusable booster from
  the same contractor. **The authoritative survey ties the number to neither and the article follows
  it.** The full order was chosen against the roster's implication, because engine and tank hardware
  existed and produced data.
- **X-44**, two different aircraft, the Lockheed Martin MANTA and a separate unmanned programme.
  **This is A341 and it is next.** Establish which designation belongs to which aircraft before writing,
  and expect the A339 shape rather than a genuine conflict, since a number used twice is not a number
  in dispute.
- **X-52**, requested 2006, refused over possible confusion with the B-52. The programme became X-53.
  **Written in A349 in the reduced order.** The finding is that **the instruction in force required the
  next available consecutive design number, contained no authority to skip one, and did not contain the
  word skip**, while aiming its whole confusability apparatus at the POPULAR NAME. **The 2020 issue
  added bare discretion to skip with no criterion**, fourteen years later. The refusal belongs to a
  documented family across the whole system, and the family contains an asymmetry: **Q-7 and Q-8 were
  requests to renumber drones because they were ALREADY being confused, and both were refused in 1954.**
  The system acted on possibility and declined to act on evidence.
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
