# Handoff Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the resume prompt for an agent picking up after a compaction or a new session. It is a
snapshot, deliberately not kept current, and it self-reports as stale rather than misleading a
resuming agent. Read it first, validate it, then read the live channels.

---

## Validity

- **Branch**: `master`
- **Parent commit** (the repository state this handoff describes): `574022c`
- **Written**: 2026-10-03, by the X-Planes line, which is the only line running.
- **Tree at write**: **CLEAN.** `git status --porcelain` returned nothing before this file was edited,
  and `origin/master` equalled `HEAD` at `574022c`, the A367 publication review having pushed, carrying
  with it the previous handoff `63d4b87` and A367's three earlier commits.
- **THIS HANDOFF'S OWN COMMIT IS NOT PUSHED.** The pilot asked for the handoff to be updated and
  restamped and did not ask for a push, so a resuming agent should expect **exactly one unpushed
  commit, this file's**, and nothing else. **More than one unpushed commit is a divergence worth
  reporting before acting.** Push it only on the pilot's instruction.
- **A367 IS COMPLETE, ALL FOUR PASSES, AND PUSHED.** Commits `6fa8e6c` drafted, `942e822` equation
  density, `df10328` primary references, `574022c` publication review. **Seventy-one of seventy-two
  drafted and 71 `x_planes` drafts are on disk, which agrees.** One remains. **Nothing in the series is
  published and publication has never been authorised.** The deploy of `574022c` succeeded, the site
  root returned 200 and A367's address returned 404, as a draft should. The next prompt is **A368,
  slotted in the roster as *X-Planes: Synthesis and What the Designation Became***, editorial date
  2025-12-16, series index 72, **the last article of the series.**
- **LINE TWO IS FINISHED AND PUBLISHED. THERE IS ONE LINE.** A376 was published on 2026-10-02 as
  `4d4938e`. Its section below is kept for its apparatus notes and method rules.
- **THE CORPUS BASELINE IS 0 ERRORS AND 0 WARNINGS ACROSS 304 POSTS.** **Two warnings now means
  something is wrong.** A `progress-stale` warning reading 71 against 72 drafts on disk is the expected
  transient while A368 is being drafted and before its channels are updated.
- **ONE PILOT DECISION IS OPEN**, recorded under Open Items: whether A364's and A365's Epistemic State
  sections should record that the register rows they rely on were not public at their own dates.

**Commit identifiers recorded in `_docs/` before 2026-08-09 are void.** History was rewritten that
day and 147 commits took new identifiers. Anything older than that will not resolve.

**Validate before trusting.** Compare the recorded **Parent commit** to `git rev-parse HEAD~1`.
Because this handoff file is itself committed, its commit becomes the branch tip and its parent is
the state described.

- **Match → VALID.** Proceed per the resume prompt for the line the pilot names.
- **Mismatch → INVALID and STALE.** A later commit moved the tip, so this file describes a state
  that is no longer current. Do **not** proceed and do **not** guess what changed. Report it as
  invalid-and-stale, familiarize from the live channels, namely `REVERSE_PROMPT.md`, `TASKLOG.md`,
  `_drafts/draft_summary.md`, and the git log, which are always authoritative, and wait for
  instruction. **This file has two writers and a mismatch is the expected state whenever the other
  line commits.**

**THREE HARD-WON WARNINGS WERE LOST FROM THIS FILE WHEN IT WAS REWRITTEN AND ARE RESTORED HERE.** Each
describes a failure that actually happened. **A handoff that drops its own operational warnings is the
failure it was warning about**, and the loss was found by grepping this file for them rather than by
anyone noticing.

**THE STAMP ON THIS FILE HAS BEEN WRONG ONCE AND THE ERROR IS WORTH NAMING AGAIN.** It was once written
as `HEAD~1` at the moment the Validity block was drafted. **But this file's own rule is that its commit
becomes the branch tip**, so the state it describes is whatever HEAD was BEFORE that commit. **The
quantity to record is the current HEAD at write time, not the current `HEAD~1`.** A self-check that runs
before the commit and compares against `HEAD~1` as it then stands will agree with the wrong value. **A
check that runs at the wrong moment confirms the wrong thing.** Run it twice, once before the commit
against `HEAD` and once after against `HEAD~1`.

**AND `REVERSE_PROMPT.md` IS APPEND-AT-TOP, NOT A SINGLE SLOT.** Its header describes a file overwritten
after each completed task and its practice is to accumulate, newest first, with every prior section
preserved including the other line's. **A362's drafting pass read the header, wrote 150 lines over 1,305,
and destroyed the A375 line's section along with every prior report from both lines.** It was repaired
from `git show HEAD`. **A file whose header says it is overwritten and which in practice accumulates
will be truncated by whoever believes the header.** **`_lib/progress.py` believed it too**, which is why
`_verify.py` now narrows that channel to its newest report before checking a drafted count.

**AND A SPAN EDIT BOUNDED BY A LATER SECTION'S TEXT HAS DESTROYED SECTIONS THREE TIMES NOW.** A362's
TASKLOG edit deleted three. **And an attempt at writing THIS file replaced a span and then looked for a
heading that the same span had just removed**, failing partway through, after which the file was restored
with `git checkout`. **Compute every boundary on the original string, assemble the result in one pass,
and compare the full heading list before and after.** That is cheap and it is the only thing that catches
it. **This revision was written that way and its heading comparison is in the commit message.**


## THE OTHER LINE COMMITTED THIS LINE'S STAGED WORK INTO ITS OWN COMMIT

This is new, it is the most important operational fact in this file, and it is not in any channel.

**Commit `33fd7fe`, whose message is about the X-66, contains the entire A376 publication review**,
namely the draft, `draft_summary.md`, `TASKLOG.md` and `REVERSE_PROMPT.md`. Commit `1dd90d0` did
something similar at a smaller scale. The A376 line had staged its own paths and was composing a
commit message when the other line committed, and the other line's commit swept the staged index.

**The content is intact.** The A376 draft on the remote was diffed against the verified working
tree and is byte-identical. Nothing was lost or altered. **Only the attribution is wrong**, and the
history was deliberately not rewritten, because those commits are pushed and may be visible to the
other session. That is a pilot decision, not an agent one.

**What a resuming agent must do about it.** Stage explicit paths, never `-a` and never `add -A`,
which both lines' instructions already imply. **And expect that the other line may not.** If a
commit is being composed, the window between `git add` and `git commit` is a window in which
another writer can take the index. Keep it short, and after committing, verify with
`git show --stat HEAD` that the commit contains what was intended and nothing else.

## Line two, the war-with-China series, is FINISHED AND PUBLISHED

**THIS SECTION'S HEADING AND OPENING WERE CORRECTED BY LINE ONE ON 2026-10-02 AND NOTHING ELSE IN IT WAS
ALTERED.** It previously read as a resume prompt for an article awaiting a publication decision. **That
decision was taken.** A376 published on 2026-10-02 as commit `4d4938e`, so the heading was false and a
resuming agent reading it would have been told to wait for something that had already happened.

**A376, Whether a War With China Would Change the Global Balance of Power**, editorial date
**2026-08-13**, categories `geopolitics military war-gaming`, series `war_with_china` index 3, is
**PUBLISHED** at `_posts/2026-08-13-balance_of_power_after_war_with_china.markdown`. **The series is
complete at three articles and the corpus is 304 posts.** A374 and A375 now read Part 1 of 3 and Part 2
of 3, which was the one outward-facing consequence its own author recorded in advance.

**Everything below in this section is line two's own writing and is kept because it still applies.** Its
final state was **4,442 lines, 89 display equations, 202 reference definitions at 25.0 percent primary,
about 23,100 words of author prose, 17 H2 and 82 H3 sections, 124 block quotations**.

**What the article argues, in its author's words, in case a later pass needs it.** On the standard
capability index China passed the United States in 1995 and stood at 1.89 times it in 2022. Applying the
historical median for large wars, an American victory produces approximate parity rather than restored
primacy, and a defeated China stays above where the United States is today. Belligerent concentration
predicts belligerent fortune at minus 0.225 across seventy-six wars, the prospective case sits at the
ninety-sixth percentile of concentration, and ten of the twelve wars in its band ended with the
belligerents smaller.

**THE EIGHT RE-DATED DRAFTS ARE COMMITTED AND THIS PARAGRAPH WAS CORRECTED ON 2026-10-02 DURING A366.**
It previously said they were uncommitted and that a resuming agent should ask the pilot, which
contradicted this file's own Validity and Open Items sections. A375's publication record notes that
`android_development_on_freebsd.markdown` collided with the 2026-08-12 slot and would have to be
re-dated before it published. **Eight drafts were moved from 2026-08-14 through 21 to 2126 by the second
line, and on the pilot's decision of 2026-10-02 they were committed exactly as they stood, as
`ee17f86`.** The intent behind the re-dating is still recorded rather than interpreted. **Nothing about
them is open.**

### The A376 verification apparatus lives in a gitignored path and will not survive a clean checkout

`tmp/` is gitignored. `tmp/a376` is 251 MB and holds six scripts and the primary data. **The data
are all re-downloadable and the provenance is recorded here because the scripts are not recoverable
otherwise.**

- `verify_numbers.py`, **184 checks**, recomputes from the Correlates of War files every figure the
  article states about capability shares, base rates, the index defects and the concentration
  result. Constants are re-entered by hand; nothing is imported from the article.
- `verify_cofer.py`, **19 checks**, the same for the reserve-composition figures.
- `verify_derived.py`, **60 checks**, the article's own arithmetic on figures quoted from the
  literature. **Kept separate on purpose**, because it cannot establish that a source says what the
  article reports, only that a printed division is the division of its printed operands.
- `power_shift.py`, the base rate by war outcome. `bystanders.py`, the belligerents' combined
  share. `concentration.py`, the result that replaced the refuted claim.
- **263 checks across the three harnesses, all passing at the time of writing.**

Data provenance, with the SHA-256 of each file as used:

- `https://correlatesofwar.org/wp-content/uploads/NMCv7.zip`, National Material Capabilities v7.0,
  1816 to 2022. Inner `NMC-70-abridged.csv` is
  `807a7092ea50b5957c7280d591dac5db16e572f6158fda0fa6c306bc27d8bf7a`.
- `https://correlatesofwar.org/wp-content/uploads/Inter-StateWarData_v4.0.csv`, 95 wars, 337
  participant rows, `2535e30b145141c331a07d12d91e498ad8bdd3db32ba8d3bd88c4fda54817731`. **It has
  bare carriage-return line endings and the `csv` module rejects it until they are normalised.**
- `https://api.imf.org/external/sdmx/2.1/data/COFER`, reserve composition, payload stamped
  2026-09-30.
- RAND `RRA591-1` and `RRA591-2` from `rand.org`, both read in full. The forecasting-accuracy table
  is a colour-coded image and **must be rendered and read by eye**, because colour does not survive
  text extraction.

**A clean checkout loses the scripts.** Their methods are described in the article's own Epistemic
State and in the above, which is enough to rebuild them, and the data hashes make a rebuild
checkable against the figures the article prints.

## Method rules this line earned, which generalise beyond it

**A CLAIM REASONED FROM THE EXTREME CASES IS NOT A CLAIM COMPUTED FROM THE DATASET.** A376 asserted
through three passes that a great-power war in which the belligerents hold a minority of world
capability would be without precedent. It is false, and the file the article already had open
refutes it in one query. The claim was reached by reasoning from 1914 and 1939 rather than from the
ninety-five wars available. **If an article has the data to test its own central structural claim,
test that claim before the fourth pass, and treat any sentence containing "for the first time" or
"never" as a computation that has not been run yet.** Computing it returned a better result than
the one it replaced, which is the usual outcome.

**VERIFY QUOTATIONS TAKEN FROM A SUBAGENT, BECAUSE THE FAILURE RATE IS NOT ZERO.** Four were
checked directly in the publication review. Two were verbatim. One differed by a single character,
the source spelling `tradeoffs` where the article had hyphenated it. One could not be verified at
all, its cited page being dead, and was replaced with a claim from the live page. **A one-character
difference in a quotation is still a difference**, and a subagent reporting a quotation it read is
not the same as having read it.

**AN UNPAIRED INLINE MATH DELIMITER IS INVISIBLE TO EVERY GATE.** Counting unescaped `$` outside
display blocks and checking the total for parity found one, a currency sign inside a quotation,
which would have left MathJax with an unterminated delimiter free to consume following text.
`_verify.py`, the production build and the rendered audit all passed with it present. **Escape
currency signs inside quotations**, which renders the character and hides it from MathJax.

**THE SOURCE-TO-RENDERED DISPLAY COUNT REMAINS THE ONLY CHECK THAT CATCHES A FOLDED EQUATION.** It
found eight in A376's equation pass, all closing delimiters sitting flush against following prose.
Every other gate passed with them present. This is now the fifth article to record it and it should
be treated as mandatory after any pass that touches equations.

**A PUBLISHER'S 403 IS NOT A DEAD DOI.** Of 200 reference URLs swept, 73 returned 403 from
`doi.org` landing pages. Each was confirmed registered by content negotiation with an
`Accept: application/vnd.citationstyles.csl+json` header, which the publishers do not block.
**Three returned an empty 202**, which is one publisher's way of refusing, and is likewise not a
broken link.

**INSERTING SECTIONS BY ANCHOR CREATES DUPLICATES AND MISPLACEMENTS THAT ONLY A STRUCTURE SCAN
FINDS.** A376's reference pass inserted blocks before named headings and produced four duplicated
subsections and four blocks filed under an unrelated heading. One duplicate said a quotation
appeared "earlier" when it appeared forty-six lines later. **After any pass that inserts sections,
dump the heading list and read it**, and check for repeated headings programmatically.

## Where the Series Stands

**Seventy-one of seventy-two drafted, A297 through A367, indices 1 through 71 contiguous. One remains**,
A368 at editorial date 2025-12-16. **Nothing in the series is published and publication has never
been authorised.**

**A363, Boeing X-66**, editorial date 2025-12-11, index 67. Four passes, pushed. 10,795 lines, 59,564
words, 83 display equations, 4,537 reference definitions, 28.3 percent primaries. Keystone: **the span of
a transport wing comes from an airport**, the wing folding at exactly the Federal Aviation
Administration's Airplane Design Group III bound.

**A364, X-67, the Slot Taken by XQ-67A**, editorial date 2025-12-12, index 68. **Four passes in four
commits, pushed**, `a9ecee9`, `8805696`, `fd6362e` and `91cf7c9`. **5,214 lines, 36,167 words, 68 display
equations, 185 inline expressions, an 85-entry symbol table and 1,315 reference definitions**, in 9 H2
and 54 H3 sections with 20 tables, citing 1,228 research records across 15 clusters from a pool of
14,384, with 159 report primaries at 12.1 percent, median year 2011 and a range from 1900 to 2026.

**WHAT A364 FOUND, IN ONE PARAGRAPH, BECAUSE A POINTER IS NOT A SUMMARY.** The whole public case for the
X-67 having been skipped is one sentence and four fifths of it is a comparison with another number, the
compiler writing that **just like the X-58** the slot was skipped after the allocation of the XQ-67A,
where the X-58's entry one paragraph above carries reasoning, a confidence grading and the claim that the
slot is empty. **So the article supplied the evidence the register asserts without.** A borrowed number
should equal its source series' next number at the moment of the borrowing and no other series', and
across six out-of-sequence unmanned numbers tested against twenty basic missions **the test fires twice
and names the research series both times**, against a null tail of 0.03159. **The instruction then makes
the question of who skipped it malformed**, defining the next designator from the last approved design
number and refusing requests in reverse or skipped sequences, so **nobody had to decide to skip the X-67
and somebody had to ask for the X-68**, 763 days later. **Four editions of the rule were read and the
change falls between 2005 and 2020**, being two changes, the quantity and the duty, which makes the X-67
**the first number in the research series to be skipped under a rule that makes skipping permanent**
while the X-49A of 2003 filled a gap the X-50A had passed and the X-58's slot stayed recoverable for two
years while nobody wanted it. **The founding document of 18 September 1962 was read in full as page
images** and defines the design number as **the sequence number of each new design**, gives **three
worked examples of what forces a new one**, all the airframe's shape or propulsion and none mission
equipment, defines both of this designation's letters on facing pages, shows the Q was then a modified
mission symbol so the designation could not have been written in 1962, and states that **the requester
named the mission while the agency chose the number**. **The aeroplane that consumed the number was built
to deny the premise the number rests on**, the Off-Board Sensing Station existing to prove a shared genus
carrying replaceable species, and **a genus holds the 1962 test's three examples constant and swaps
exactly what that test ignores**. The register shows the same from both sides, six pairs of design
numbers carrying identical official descriptions with the contractor the only differing field in five,
while 27 design numbers survive a change of leading firm. **And the research series is the best-behaved
sequence in the register at 72.7 percent of pointer advances equal to one against 50.4 register-wide**,
so the X-67 was lost from the one numbering sequence that mostly does follow the rule.

**A365, General Atomics X-68 LongShot**, editorial date 2025-12-13, index 69. **Four passes in four
commits plus an addendum**, `dd73308`, `bd1cc3d`, `789a500`, `c82c2ef` and `db308a4`. **2,917 lines,
22,194 words, 42 display equations, 133 inline expressions, a 78-entry symbol table and 548 reference
definitions**, two of them nominal addresses for walled documents, citing 458 distinct works across 11
clusters from a pool of 4,711, with 72 report primaries at 15.7 percent, median year 2009, range 1935
to 2026, and 20 primaries read directly.

**WHAT A365 FOUND, IN ONE PARAGRAPH.** The keystone is the store mass fraction and **the government
named it**, four budget books inside the dateline carrying the sentence that the programme will address
the stability and control challenges of launching air-to-air missiles from a relatively small unmanned
vehicle. A fighter releasing one of these missiles sheds 0.601 percent of itself and this vehicle
releasing two sheds 17.94, a factor of 30 that is **an identity in the two launcher masses alone, the
missile cancelling out of its own comparison**. The reach benefit every account leads with is arithmetic
stated as a cost, a missile's reach logarithmic in its speed ratio so doubling it takes the propellant
fraction from 0.402 to 0.746 while the carrier flies the distance on 0.013. **The best derived result
is the pit-test fidelity ratio**, the clamped ground test dividing the cartridge impulse by the store's
mass where flight divides it by the reduced mass, so the standard test underreads flight separation by
exactly 1/(1-mu), half a percent for a fighter and a tenth to a fifth here, **the test's fidelity
degrading with the very parameter the programme exists to study**. The altitude climb gradient under
density-lapsed thrust goes negative at 3,000 kilograms and **closes the mass sweep from above by
classical mechanics alone**. The budget books date the concept's one change, weapon to vehicle, to an
eleven-month window, **the award record corroborating it independently** by preserving the multi-mode
wording verbatim in a January 2021 contract description, with the single-mode cruise-missile engine as
the physical trace. The in-flight release of a missile from the vehicle, the keystone as a
demonstration, **appears in the plans of exactly one budget book**, replaced in the next by carriage
release, which is a different test. And **every official word about the aeroplane is bookkeeping**, the
register's markup putting only the name outside the unofficial span, the only research row marked at
that level.

**A366, X-69 through X-75, the Leapfrogged Block**, editorial date 2025-12-14, index 70. **Four passes in
four commits, pushed**, `b6882a6`, `2adccd6`, `083525b` and `e7a8e85`. **4,669 lines, 29,682 words, 42
display equations, 105 inline expressions, a 33-entry symbol table and 1,974 reference definitions**,
being 24 primaries, 1,881 research works of which 13 are hand-chosen primaries verified by title and 59
are report-server records at 3.14 percent, and 69 related posts, in 11 H2 and 42 H3 sections with 9
tables, from a pool of 15,522.

**WHAT A366 FOUND, IN ONE PARAGRAPH.** **The block is seven skips made at once so that one number could
be chosen.** Seven unreleased allocations would all have to fall in the 61 days between the X-68A and
the X-76A, a Poisson tail of 1.83e-10 at the series' own rate, needing a rate 23.51 times the observed
one to reach 0.05. A reserved block has no instrument in the 2020 instruction. The instruction refuses
requests in skipped sequences and gives the allocating office an unconditioned discretion to skip, and
**DARPA's statement of 9 March 2026, postdating the article, calls the 76 a deliberate nod to the
revolutionary spirit of 1776.** **The public register did not show the X-68A or the X-76A until between
15 January and 1 February 2026**, by archived copies, so the anomaly was invisible in the public record
at its own date, **and so was A364's X-67 gap at A364's date, which A364 does not record.** The
compiler wrote a sentence naming the X-77 reading and removed it after DARPA's statement under a
last-updated stamp that never changed. **The X-76A is the third founding-year design number in 329
days**, after the YMV-75A for 1775 and the F-47A for 1947, and released Air Force public affairs emails
name General Allvin as the F-47's decider, the only named chooser of a design number found. **The 2020
rule describes 6 of 23 allocation events since it took effect, or 7 with the RQ-170 row set aside.**
NASA's 2003 X-vehicle inventory gives the X-50A precedent a second primary, with the contractor's
programme manager claiming the request and a 2003 prediction that the passed X-49 would be issued,
which it was. **The article ends on a test: the next research designation is the X-69A if the X-49
precedent governs and the X-77A if the 2020 text governs.**

**A367, Bell Textron X-76 SPRINT**, editorial date 2025-12-15, index 71. **Four passes in four commits,
pushed**, `6fa8e6c`, `942e822`, `df10328` and `574022c`. **8,298 lines, 55,686 words, 40 display
equations, 95 inline expressions, a 51-entry symbol table and 3,737 reference definitions**, being 66
primaries, 3,601 research works of which 17 are hand-chosen primaries read for their abstracts and 616
of the 3,584 swept works are report-server records at 17.2 percent, and 70 related posts, in 16 H2 and
55 H3 sections with 6 tables, from a pool of 12,957 with 3,847 admitted to 11 clusters.

**WHAT A367 FOUND, IN ONE PARAGRAPH.** **The X-76 carries two kinds of engine so that no one machine has
to both lift it and push it fast**, and the certificated ratings of the register's engines bound it
without its mass. Under a lapse of density times a swept factor, **the PW308C's thrust fixes the largest
equivalent drag area at 400 knots at 0.60 to 0.84 square metres, the density cancelling so the ceiling
is the same at every altitude**. The two CT7-8s would hover about 30,800 lb at the XV-15's disk loading,
twice the solicitation's top weight, and the bare engines are 16.3 percent of 15,000 lb, so the aircraft
is, as an inference, heavy or at a high disk loading. **The hover wake's dynamic pressure equals the
rotor's thrust per unit disk area, independent of density**, so the stowable rotor's downwash cost is
exact. The programme is documented from government primaries: the solicitation HR001123S0031 with its
slides and answers, three of four Phase 1A award records with thirteen offers each and Bell's absent,
four budget books, and two engine data sheets, the PW308C's approving multiple-engine installation
only. **The concept was shown at full scale in 1972 and shelved for want of a convertible engine**,
which the 1988 literature preferred to separate engines, and **both SPRINT finalists chose separate
turbofans and turboshafts**, by Aurora's own releases, so the existing-engine rule and not the
configuration drove the choice. Textron's mirror misdates two Bell releases by a year, Phase 2 is dated
three ways, the recorded Phase 1A obligations exceed the solicitation's Phase 1A figure, and the
schedule slipped at least eight months between October 2024 and July 2025. **The literature is
silent on any stop-fold conversion in flight, which is the X-76's keystone.**

**ONE REMAINS, A368, THE CLOSING SYNTHESIS**, editorial date 2025-12-16, series index 72.

**Next available article number: A377.**

## Open Items

**ONE ITEM, AND IT IS THE PILOT'S.** **A364 and A365 state register facts that were not public at their
own editorial dates**, the X-68A and X-76A rows first appearing in archived copies of the register
between 15 January and 1 February 2026, and the X-67 gap being visible only through the X-68A row.
**Neither article's Epistemic State records this.** A366 records it for itself and states it about
A364. **The decision is whether to add a dated postdating statement to each**, which is a two-paragraph
edit per article with the archive captures already cited in A366 as
`ref_mds_addendum_wb_2025_12`, `ref_mds_addendum_wb_2026_01` and `ref_mds_addendum_wb_2026_02`.
**Do not make the edit without the decision.**

**Everything decided on 2026-10-02 stays closed**: the mathematics repair `ea593f0`, the A358/A359
officiality repair `442fc41`, the eight 2126-dated drafts `ee17f86`, `sa.html` deleted, the A376
attribution left in pushed history.

**WHAT A RESUMING AGENT SHOULD EXPECT**: a clean tree, exactly one unpushed commit being this file's,
0 errors and 0 warnings across 304 posts, and the next prompt being A368. **Anything else is a
divergence worth reporting before acting.**

## Resume prompt for the X-Planes line, and the next prompt is A368

**A367 IS COMPLETE AND THE LINE IS AT AN ARTICLE BOUNDARY. Wait for the pilot's prompt and do not
start A368 unprompted.**

**The next article is A368, slotted in the roster as *X-Planes: Synthesis and What the Designation
Became*.** Editorial date **2025-12-16**, series index **72**, the last article of the series, slug
following the series pattern, for example `x_planes_synthesis_what_designation_became`. **Check the
roster title with the pilot's prompt**, since the pilot has retitled slots before.

**THE GENRE IS NEW AND THE GENRE TEST DOES NOT APPLY.** There is no aircraft and no anomaly number. It
is the series' closer, the counterpart of A297's framing article, and its subject is the designation
system across all seventy-one articles. **Read A297 first**, `_drafts/x_planes_framing.markdown`, for the
research aircraft model and the questions the series opened with, and **answer them by name.** The
closer should not be a list of summaries. It is an argument about what an X designation has meant,
from a sequence number assigned to a crewed research aeroplane in 1946 to a number chosen to spell a
founding year in 2025.

**WHAT THE SERIES HANDS A368, ALL RECORDED IN THIS FILE AND THE DRAFTS.**

- **The nine anomaly cases and their findings**, under *The Nine Anomaly Cases* below, with A366's two
  additions, that design numbers have started to carry messages and that the register lags its
  allocations by months, and A358's finding that the register stops being an official primary source
  for descriptions after the X-60A.
- **The per-mission numbering rule and its editions**, read in A364 and A366: the 1962 founding
  document, the 1994 joint instruction, the 2005 and 2020 instructions, and the 2020 clause reserving a
  discretion to skip. The 2020 instruction is saved as `tmp/a367/prim/dafi2020.txt`.
- **The register as the measurement instrument.** `tmp/a366/meas.py`, `register.py` and `meas366.py`,
  copied to `tmp/a367/`, parse it two ways. The pointer walk, the share of advances equal to one, the
  allocation rate and the founding-year class are A364's and A366's measurements and should be
  recomputed rather than quoted.
- **The arc from crewed rocket aircraft to uncrewed demonstrators.** A365 and A367 are both uncrewed
  DARPA demonstrators and A367's description is the compiler's word unmanned. **Count it from the
  register and the series**, crewed against uncrewed by decade, rather than asserting it.
- **The contractor heritage claim A367 corrected.** Bell's research designations are eight, the X-1,
  X-2, X-5, X-9, X-14, X-16, X-22 and X-76, and the XV-3 and XV-15 are a different sequence. The closer's
  account of which firms built X-planes should count the same way.

**THE GENRE WILL TEMPT THE DRAFT TO OVERCLAIM, AND THE OPENING CHECK IS THE GUARD.** A synthesis invites
sentences about every article at once, and every such sentence is a claim about seventy-one documents.
**Run the opening check against the analysis at the end of the drafting pass**, as A366 directed and A367
showed works, and scope every generalisation to the articles it counts.

**THE SERIES LINE.** `tmp/a367/series_line.py` generates the opening line from `related.json`. For
A368 add A367's anchor, `related_post_a367_bell_textron_x76_sprint` with the post_url of
`2025-12-15-x_planes_bell_textron_x76_sprint`, set the expected count to 70 prior aircraft articles and
the ordinal to seventy-second, and keep the special-label map, which already covers the X-69 through
X-75 block.

**SAVED UNDER `tmp/a367/`, WHICH IS GITIGNORED**: the solicitation, slides and answers under `prim/`,
the award records `awards367*.json`, the engine data sheets and New Zealand reports, the XV-15 history
`prim/xv15_hist.txt`, the patents `patents367.json`, the abstracts `prim_research.json` and
`lit_abstracts367.json`, the register `addendum.html` and its archived copies under `wb/`. The DARPA
budget books are under `tmp/a365/bb/`. **Lift what A368 needs before the directories go.**

### What A367 Established That A368 Inherits as Practice

- **RUN THE OPENING CHECK AT THE END OF THE DRAFTING PASS. IT WORKED.** A367's opening failed the check
  in five places at drafting, was corrected before commit, and held at publication, the first article
  in four where the publication check found nothing in the opening.
- **THE COMPETITOR'S DOCUMENTS ARE PRIMARIES ABOUT THE WINNER'S CHOICES.** Aurora's releases turned an
  inference about Bell's engines into evidence about the rule. **When a choice is attributed to a rule,
  look for the other bidder.**
- **A MONEY IDENTITY CAN REFUTE A PREMISE.** Displaying the Phase 1A sum showed it already exceeded the
  solicitation's Phase 1A figure, which undid the premise of a bound the draft had stated. **Write the
  arithmetic out and read it.**
- **A SYMBOLIC DISPLAY HAS NOTHING TO RECOMPUTE AND WAS UNCHECKED.** A mutation test found it. Assert
  identities verbatim and test them algebraically.
- **A MUTATION THAT DOES NOT APPLY TESTS NOTHING.** A `sed` mutation silently failed and reported the
  verifier blind. Apply mutations in Python and assert the target exists first.
- **A LITERATURE SECTION THAT MAPS IS NOT A REVIEW.** The directive asks for a review, and A367's
  publication review added a synthesis from fetched abstracts. **Write the synthesis in the drafting
  pass**, scoped to what the abstracts say.
- **A DOLLAR SIGN IN PROSE IS MATHEMATICS.** "$15M" would have rendered as an equation and was caught
  only as a stray symbol. Write amounts in words.

## The Established Rhythm, Which Is the Most Important Thing Here

Four passes, each a separate prompt from the pilot. **Do not run ahead.**

1. **"Please draft Axxx, '<title>.'"** Research, write, verify, commit. **Do not push.**
2. **"Please review for equation density, and add all candidate equations."**
3. **"Please review for reference density, specifically primary references, and add all identified
   references."**
4. **"Please review for publication, and make suitable changes..."** This prompt also asks for a push.

After every pass, update `REVERSE_PROMPT.md`, `TASKLOG.md` and `_drafts/draft_summary.md`, and commit
them with the article in one commit.

**A360's THREE COMPLETED PASSES ARE ALREADY PUSHED AND THAT WAS NOT THIS SESSION'S DOING.** The
concurrent session's publication push carried them. **The rhythm still says do not push on passes one
to three**, and the fact that they are pushed anyway is an accident of a shared tree rather than a
change of practice.

**AND THE BUILD TO RUN PER PASS IS THE STUB BUILD.** `./_check.sh --drafts` scales superlinearly in
link-definition count and **A360 lost five hours and forty-one minutes to it before reading the
paragraph in this file that forbids it**. Use `tmp/a360/site_build.sh` or its equivalent, which takes
under twenty seconds, and run `_verify.py` against the real tree.

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

### Earned in A367, and the theme is that the other party's documents decide your inference

- **A RULE'S EFFECT IS BEST SHOWN BY TWO PARTIES OBEYING IT.** The existing-engine rule was an inference
  from one aircraft until the competitor's releases showed the same answer in a different configuration.
- **A SECONDARY RECORD CAN CARRY A PRIMARY'S ERROR, AND THE MIRROR IS THE PLACE TO LOOK.** Textron's
  investor-relations copies misdate two Bell releases by exactly a year while Bell's newsroom is right.
  **Read the issuer's own copy and compare.**
- **A REGULATOR'S ACCEPTANCE REPORT IS A PRIMARY INSIDE THE DATE WHEN THE CURRENT DATA SHEET IS NOT.** The
  European CT7 sheet postdates the article by four days, and the New Zealand reports of 2007 and 2020
  corroborated both engines from inside the date, the PW308C's rating agreeing to within a pound.
- **A TABLE THE TEXT EXTRACTOR CANNOT READ IS NOT A SOURCE FOR A NUMBER.** The 1985 XV-15 hover test's
  figure of merit sits in an appendix whose extraction failed, so the value stayed an assumption.
- **A REGISTER CONVENTION IS MEASURED, NOT REMEMBERED.** The first draft said combination pluses are
  always spaced, and the RIM-156B row says otherwise. **Every claim about the register's syntax is a
  query over its rows.**
- **AN ASSUMED TIP SPEED CAN BE CHECKED AGAINST A MEASURED RANGE.** The XV-15's hover tip Mach of 0.69
  falls inside the 0.60 to 0.73 the full-scale test measured, which is the only independent check of
  an input A367 found.
- **THE TURBOFAN COUNT WAS A READING STATED AS A FACT IN THREE PLACES.** Search the whole draft for a
  reading once it is identified as one, not only the sentence where it was noticed.

### Earned in A366, and the theme is that the date a fact existed is not the date it could be known

- **A REGISTER ROW HAS TWO DATES AND A DATELINE ARGUMENT NEEDS THE SECOND.** The allocation date is the
  government's and the publication date is the compiler's. **A366 found the X-68A and X-76A rows public
  only between 15 January and 1 February 2026**, three to five months after allocation, by bracketing
  archive captures. The `wb/` snapshot pattern in `tmp/a366/` is the instrument.
- **A SOURCE CAN CHANGE UNDER AN UNCHANGED STAMP.** The compiler's page added and removed a sentence
  while its last-updated date stayed 3 January 2026. **Date by capture time and say so.**
- **THE OPENING FAILED AGAINST THE ARTICLE'S OWN ANALYSIS FOR THE THIRD ARTICLE RUNNING.** The rule
  earned in A365 caught it again at publication. **Move the check earlier, to the end of the drafting
  pass**, since the defect is evidently produced there.
- **THE HANDOFF'S PREMISE CAN BE PARTLY WRONG AND THE DRAFT MUST SAY WHERE.** It said no allocation in
  the register carries any of the seven numbers. **No research row does, but three rows in other
  missions do**, and the YMV-75A turned out to be the key to the article. **Measure the premise before
  writing on it.**
- **AN ATTRIBUTION READ ONLY BY TITLE IS A FABRICATED ARGUMENT.** Three sentences in the reference pass
  said what papers argue from their titles alone. **Fetch the abstract or cite the title as a title.**
- **THE AIMED SWEEP IS MEASURED AGAINST A FROZEN BEFORE-FIGURE, AND THE BEFORE-FIGURE IS RECOMPUTED
  FROM THE PRIOR COMMIT.** `before_prim.md` is `git show HEAD:` of the draft before the pass, which
  makes the before-and-after an audit rather than a memory.
- **AN INHERITED INSTRUMENT POINTED AT THE WRONG ARTICLE REPORTS PLAUSIBLE NUMBERS.** `count.py` was
  still pointed at the X-66 and printed its counts. **Retarget every constant and check one output
  against a hand count.** `rendercheck.py` also expects script-tag mathematics the site no longer emits;
  `mathrot.py` is the authority for the display count.
- **AN ESCAPE IN A PYTHON EDIT SCRIPT IS A SECOND MARKUP LANGUAGE.** Use raw strings for every LaTeX
  fragment, since `\;` passed through only by luck and `\b` would not have.

### Earned in A365, and the theme is that the sample that cannot fail is the one that fails you

**THE AUDIT PASSED WHILE THE GATE REFUSED THE SUBJECT**, and half of what this article earned is
about where a test's cases may come from.

- **A KEEP SAMPLE DRAWN FROM THE PROBE'S OUTPUT CANNOT DETECT LOW RECALL.** The homonym probe lists
  the titles the bare-word patterns find, which are by construction the titles the gate matches, so
  an audit built from them is clean whatever the gate refuses. The refused pile held the F-15
  store-separation loads report while the audit reported no disagreements. **Draw the keep sample
  from the refused pile and read it by eye**, which failed twenty-four cases at once.
- **THE DISCRIMINATOR IS THE CARRIED OBJECT AND NEVER THE SHARED WORD.** Boundary-layer, flow and
  leading-edge separation are the word's largest aeronautical users, and they are aerodynamics, **so
  no guard that asks whether a title is aeronautical can exclude them**. The gate admits
  `separation` nowhere without a word naming a thing that is carried and released, a structural
  property rather than an exclusion list, which is why it holds for collisions nobody enumerated.
- **A HYPHEN DEFEATS A CLUSTER PATTERN SILENTLY WHERE IT DEFEATS A GUARD LOUDLY.** A defeated guard
  admits wrongly and is visible in the kept pile; a defeated cluster pattern refuses wrongly and the
  record is simply not in the output. Separator tolerance is applied once, centrally, to every core.
- **TWO INSTRUMENTS' POPULATIONS MUST NEVER MIX, SECOND OFFENCE.** This article confidently
  corrected three of the handoff's register counts and the handoff was right every time, the narrow
  dated-rows parser against the wide well-formed one. The trap was already in
  `VERIFICATION_TRAPS.md` and was walked into anyway, **which is why the rule is now stated beside
  the numbers it governs rather than only in the traps file.**
- **AN EXPONENTIAL BENEFIT CURVE IS USUALLY A CEILING WEARING THE WRONG CLOTHES.** The first pass
  reported a terminal-energy gain of six thousand from an expression whose domain the missile cannot
  reach, the decay length being 114 kilometres against the 500 assumed. **State the domain beside
  any exponential, and when a figure looks astronomical, suspect the domain before the subject.**
- **THE CLAMP CHANGES THE PHYSICS BY THE KEYSTONE PARAMETER.** The pit test divides the cartridge
  impulse by the store's mass and flight divides it by the reduced mass, so the standard ground test
  underreads flight separation by exactly 1/(1-mu). **At a fighter's mass fraction the error is the
  reason the technique is standard, and at this vehicle's it is a tenth to a fifth**, the
  instrument's fidelity degrading with the very parameter under study.
- **A REMEMBERED IDENTIFIER IS A FABRICATED IDENTIFIER, SECOND ENFORCEMENT.** The register's URL was
  written from memory as a plausible path that 404s, and the address sweep caught it exactly as it
  caught A364's invented DOI. **The sweep is not optional on any pass that adds a definition.**
- **QUOTE A PRIMARY BY ITS ORIGINAL UNITS AND CONVERT AT THE DEFINITION.** Both service fact sheets
  read for this article misconvert their own pound figures, one by 291 kilograms and one by 1.2.
  **A primary document's derived figures are not primary**, and the verifier asserts both
  discrepancies so neither can silently become the article's own.
- **AN INHERITED INSTRUMENT MODELS THE PREVIOUS ARTICLE UNTIL EVERY CONSTANT IS RETARGETED.** The
  dateline scan's heading carried A362's editorial date through two passes while its filter was
  right, which is the instrument-inheritance defect in its mildest possible form and was still worth
  a correction commit.
- **THE EMITTER RUNS AFTER THE REFERENCE REGENERATION.** The stated primary count went stale at 19
  against 20 definitions because the pipeline ran in the wrong order once. **Recompute-never-match
  only works when the recomputation is downstream of everything it counts.**
- **A TURN'S FINDINGS WRITTEN ONLY TO THE CHANNEL DO NOT SURVIVE THE TURN.** A365's first drafting
  attempt was ended by a safeguard with fourteen minutes of research on disk and every finding only
  in the conversation. The data survived and the readings did not. **The findings file is written as
  findings arrive**, and the general rule is now `_docs/process/WORK_DURABILITY.md`.
- **THE TWIN-BUILD COMPARISON IS THE ONLY PROOF AN EDIT TO PUBLISHED PAGES IS CONFINED TO ITS
  TARGET.** The mathematics repair's first fixer escaped a glob star inside a published 2016 GRANT
  statement, a shell listing whose two dollar signs read as an inline span. Two pages differed
  outside mathematics in the twin comparison and that is the only way it would have been caught.
  **Rehearse in twins, blank the target spans, and require the remainder byte-identical.**

### Earned in A364, and the theme is that the document you already quote is the one you have not read

**THE PASS THAT YIELDED MOST WAS THE ONE THAT FOLLOWED A CITATION BACKWARDS**, and three of the
instrument failures below are the previous article's formatting surviving into this one's tools.

- **READ THE DOCUMENTS A SENTENCE YOU ALREADY QUOTE HAS NAMED.** A364 quoted the instruction's sentence
  that the designator format was established on 18 September 1962 by three named regulations, and had
  read none of the three. **They are one document issued three times over, a public scan exists, and
  reading it changed four of the article's claims.** It defines the design number as **the sequence
  number of each new design**, gives three worked examples of what forces a new one where the modern
  instruction gives none, and states that the agency chose the number while the requester named only the
  mission. **A named document inside a quotation is a task, not a footnote.**
- **AND AN IMAGE-ONLY SCAN IS READ AS IMAGES OR NOT AT ALL.** Text extraction from that scan returned
  **nineteen bytes**. A pass that had trusted the extraction would have reported the document as empty or
  cited it unread. **Check the extracted length against the file size before believing an extraction.**
- **A WEB ARCHIVE IS A LEGITIMATE ROUTE TO A DOCUMENT A PORTAL REFUSES, AND THE DEFINITION SAYS SO.** The
  Department's issuance portal returns HTTP 403 for its own list to every client tried. **The document
  was read from a public archive snapshot**, and reading it showed that the 2018 change the article had
  been told cancelled the public list **cancels nothing**; it reassigns an office. **The cancellation is
  in the 2020 instruction the article was already quoting twice.**
- **AN OPENING SENTENCE CAN BE REFUTED BY THE ARTICLE'S OWN TABLE TWO SECTIONS LATER.** A364's opening
  claimed the X-67's register entry is the only one that reasons by analogy. **The compiler's notes
  reason by analogy for the XRQ-73A and the YFQ-44A and the article's own table lists both.** This is the
  series' most frequent defect and it was in the most visible position in the article. **Run the risky
  and superlative scans and read every absolute against the paragraphs that follow it, not only the one
  it sits in.**
- **AND A SECOND ABSOLUTE WAS WRONG IN THE ARTICLE'S FAVOUR.** It said a search of the register for the
  string X-67 finds the note and nothing else. **The string does not occur in the register at all.** The
  corrected sentence is stronger. **Verify a negative by enumeration even when the weaker version
  already supports the argument.**
- **A CLAIM CAN BECOME TOO STRONG BECAUSE AN EARLIER PASS STRENGTHENED THE EVIDENCE.** The
  lowest-never-allocated number was said to be uncomputable from the public record, and the primary pass
  had just added two documents reaching back before the register. **Re-read the absolutes after any pass
  that adds sources.**
- **A HAND-WRITTEN SOURCE DEFINED AND NEVER CITED IN THE BODY IS A SOURCE THE ARTICLE DOES NOT USE.**
  Four were found, including all three entries for the modularity theory the commonality section rests
  on, whose title the source base already told a story about. **`verify_numbers.py` now asserts that no
  hand-written source is body-uncited.**
- **AN ARTICLE WHOSE OWN MEASUREMENTS POSTDATE ITS DATELINE MUST SAY SO IN THE EPISTEMIC STATE.** A364
  carries three such statements and the genre provides for exactly that. **The provision has to be used,
  not merely to exist.**
- **A REMEMBERED IDENTIFIER IS WORSE THAN A PLACEHOLDER BECAUSE NO RULE ABOUT PLACEHOLDERS CATCHES IT.**
  A digital object identifier was written into the reference file in the belief that it was correct and
  **resolves to nothing**, while the real one was in the harvest throughout. **The address sweep's
  registry fallback is what caught it**, by distinguishing an identifier whose publisher refuses a robot
  from one that resolves to no record at all.
- **AN INHERITED INSTRUMENT MODELS THE PREVIOUS ARTICLE'S FORMATTING, THREE TIMES IN ONE ARTICLE.** The
  display-equation counter saw only one-line blocks and reported zero against twenty-six. The
  publication-review style scan removed the `$$` delimiter lines and left the block body, reporting
  **193 prose semicolons that were every `\;` in the article**. And the officiality parser read one of the
  register's three markup levels and reported a confident wrong count **twice, at a different level each
  time**. **Two instruments disagreeing about the same question means one of them is wrong.**
- **A CHECKER THAT CANNOT SEE SCRIPT LETTERS CANNOT CHECK THEM.** `symcheck.py` treated `\mathcal` as
  structural and stripped its contents, **so the five new script sets the equation pass added would have
  been validated by nothing.** It now keeps the script form as a compound token and immediately found
  four undeclared sets. **A blind spot is invisible precisely in the pass that would have used it.**
- **A FROZEN OCCURRENCE COUNT MUST BE MEASURED ON WHITESPACE-NORMALISED TEXT.** The body is hard-wrapped,
  so a phrase carrying a newline returned zero. **A count of zero for a phrase plainly in the article is
  the instrument reading the line wrapping rather than the prose.**
- **A TOLERANCE DERIVED FROM THE LAST PRINTED DIGIT MUST ADMIT TWO KINDS OF SLACK.** It failed on a
  correctly rounded figure because the computed value carried floating-point noise eight parts in a
  billion beyond the exact half. **A verifier that fails on its own display rounding is measuring the
  wrong thing, and so is one that fails on the representation of the number it is rounding.**
- **A LIMIT CHECK NEEDS AN ARGUMENT LARGE ENOUGH FOR ITS OWN EXPONENT.** Ten to the ninth left a sharing
  slope at minus 0.9922 against a limit of minus one, because the exponent is 0.2345. **Ten to the
  fortieth passes. Choose the argument from the exponent, not from how large the number looks.**
- **A DUPLICATE KEY IN A DICT LITERAL IS A DEFECT EVEN WHEN THE SURVIVOR IS CORRECT.** Merging a second
  sweep left `source` assigned twice in one literal. **It happened to be right and it was waiting for
  somebody to reorder the lines.**
- **AN INCREMENT AND A POINTER ADVANCE MEASURE DIFFERENT THINGS AND CONFLATING THEM DOUBLE-COUNTS.** An
  allocation below the pointer makes its own increment negative and inflates the next one by the same
  amount. **The advance of the running maximum separates skipping from out-of-order allocation**, and
  only the second measure produced a gap list that matched this series' own articles exactly.
- **AND A SERIES LETTER OF B OR LATER PROVES ITS DESIGN NUMBER PREDATES THE ROW.** Without that filter
  the walk counted a B-model as a new design number and reported a step of minus four, **which is the
  register's own edge misread as a government decision.**
- **A PARENTHESIS INSIDE A PROPER NAME IS NOT A PARENTHETICAL.** The instruction is officially named
  `AFI 16-401(I)` and cannot be cited without it. **An interruption is preceded by a space and a name
  suffix is not**, which is narrower than excluding citation link texts wholesale and is what the check
  now tests.
- **THE REPORT LITERATURE'S VOCABULARY IS NOT THE PROGRAMME'S AND THE PROBE SAYS WHICH.** `commonality`
  returns 421 records on the reports server and they are space station and habitat commonality. **The
  first sweep asked in aeronautical words and missed all of them.** Asking in the server's words bought
  49 report primaries. **And the largest cluster still went from zero primaries to one**, because
  product family design is a management literature and no rephrasing moves it.
- **COMPLETE COVERAGE CAN BE A PROPERTY OF THE PHRASING RATHER THAN OF THE REACH.** The first sweep
  retrieved 745 of 745 and the article called that complete coverage. **The third retrieved 1,795 of
  2,966 and walked out on two questions**, because those questions reach a literature large enough to
  walk out of. **Say which.**
- **AN OFF-BY-ONE THAT RUNS IN BOTH DIRECTIONS READS AS CORRECT IN EXACTLY ONE OF THEM.** The handoff's
  own validity check parsed `git status --porcelain` for lines beginning `" M "` after a helper had
  called `strip()` on the output, **so it discarded whichever path sorted first, always.** Run before
  the commit the discarded path was this file's own and the draft count came out right by two errors
  cancelling; run after, it discarded a real draft and reported one too few. **The claim under test was
  true the whole time and the instrument failed it.** Parse with `git diff --name-only`, which has no
  status columns to misalign, and count the population the claim is actually about rather than a
  superset of it. This is why the protocol runs the check twice: a single run would have passed.

### Earned in A363, and the theme is that the instrument is wrong more often than the subject

**EVERY ONE OF THESE WAS FOUND BY A CHECK FAILING, AND IN EIGHT CASES THE CHECK WAS THE THING THAT
WAS WRONG.** That is the shape of this article's method record, and it is the opposite of A362's,
where the corrections needed correcting.

- **A PLACEHOLDER IDENTIFIER WAS ENTERED INTO A REFERENCE FILE AND CAUGHT BEFORE IT SHIPPED.** A
  digital object identifier was written as `10.2514/6.2026-0000` while the real one was looked up.
  **A fabricated identifier that resolves to nothing is worse than no citation at all**, because it
  looks checkable and is not. **Never write a placeholder into a reference definition. Leave the
  entry out until the identifier is in hand.**
- **KRAMDOWN PAIRS ASTERISKS INSIDE INLINE MATHEMATICS EXACTLY AS IT PAIRS UNDERSCORES, AND
  `emrisk.py` IS BLIND TO IT.** Writing an inline `^{*}` twice in one paragraph produced an `<em>`
  and a `</em>` inside the rendered expressions. **The rule was probed against kramdown directly
  rather than modelled**, which is A362's lesson about this exact defect. Two bare asterisks in one
  paragraph pair, one alone survives, an escaped one is inert, and **display blocks pass through
  untouched so only inline spans need escaping**. `tmp/a363/astrisk.py` predicts it from source.
- **AND THE CORPUS-WIDE NUMBER IS LARGER THAN RECORDED AND HAS TWO CAUSES.** `tmp/a363/mathcorpus.py`
  reads the built pages and measures **133 corrupted mathematical spans across 37 pages, 104
  underscore-driven and 29 asterisk-driven**, where the open decision recorded 72 source-side pairs.
  **The two agree once the unit is matched, since a pair corrupts two spans**, and the asterisk cause
  was outside the existing instrument's model entirely. **A measurement in the rendered pages beats a
  prediction from the source.**
- **A LATEX LINE BREAK WITH OPTIONAL ROW SPACING CONTAINS THE DISPLAY OPENER A COUNTER LOOKS FOR.**
  A row-spacing break inside a `cases` environment passes through verbatim, so counting bare opening
  brackets found two more openers than closers and **reported a mismatch on a page that was
  correct**. A delimiter is only a delimiter when it is not preceded by another backslash. The
  equation pass hit this the moment it used a piecewise definition, which this series had never done.
- **A DISPLAY BLOCK WITH PROSE ON THE SAME LINE IS NOT A DISPLAY BLOCK**, and three shipped that way
  before a token count found them. **Dollar pairs came to 164 against 79 counted blocks, which cannot
  both be true.** A375 lost four equations to the same class through a missing blank line. **Count
  delimiter tokens against counted blocks after any pass that inserts mathematics.**
- **A VERIFIER'S REFERENCE TABLE MUST BE SOURCEABLE, AND THIS IS THE A362 DEFECT IN A NEW UNIT.** That
  article put five-thousand-FOOT standard-atmosphere values against a key in METRES. This one typed
  tabulated values from memory, failed, **and then added a geometric-to-geopotential conversion in the
  wrong direction to explain the mismatch it had itself caused**, which made the high-altitude entries
  fail worse. **A check against numbers the author cannot source is not a check.** It was replaced by
  the two defining temperatures, the agreement of the two pressure branches at the tropopause, the
  barometric exponent against its definition, and **the hydrostatic equation by central difference at
  six hundred random altitudes**, which tests the model against the physics rather than a printout.
- **A VERIFIER THAT FAILS ON ITS OWN DISPLAY ROUNDING IS MEASURING THE WRONG THING.** Comparing a
  printed value against a computed one at a tolerance tighter than the printing reported eleven
  failures, **every one of them the rounding the article itself performs**. The tolerance is now
  derived from the last printed digit. **A slot holds a rounded display string and not a
  full-precision number.**
- **A REGEX CONVERSION MOVED EXPLICIT TOLERANCES INTO A `scale` PARAMETER AND RESCALED A SLOT BY TEN
  THOUSAND.** The check caught it as a 999,934 percent error, which is the only reason it was visible.
  **A bulk rewrite of call sites must be checked against the signature it is rewriting into.**
- **A PRESENCE TEST FOR A LITERAL STRING HAS NO BUSINESS BEING A PATTERN.** Nineteen presence checks
  for new display relations were written as regular expressions, one LaTeX macro is a bad regex
  escape, and **the check crashed rather than running**. Literal substrings now.
- **A BISECTION MUST ASSERT ITS BRACKET BEFORE IT SEARCHES, AND TWO DID NOT.** One searched a bracket
  that did not contain its root, with an inverted direction test, and **returned the bracket edge**,
  which is a silent wrong answer rather than a failure. **Both production inversions now assert that
  the root is bracketed first.**
- **AND AN INVERSION MUST SAY WHICH BRANCH IT IS ON.** The Korn drag-divergence relation is not
  monotone in sweep, turning over near fifty-four degrees, and a bracket spanning the turning point
  put the target below the objective at both ends. **The assertion refused to run rather than
  returning the wrong root, and the docstring it refused had claimed the function was monotone.** An
  assertion caught a wrong sentence written by the person who wrote the assertion. **The closed form
  for the turning point then replaced the scan entirely.**
- **THE TWO-SIDED AUDIT'S REFUSED SIDE FOUND AN ENTIRE MISSING CLUSTER.** Thirty refused records
  carried a joined-wing research aircraft, a tandem-wing spacing study and a blended-wing-body
  pre-design, **and no existing pattern admitted any of them**. The new cluster holds 522 records and
  is the third largest in the article. **A gate audited only on what it keeps cannot find an absence.**
- **A GUARD QUALIFIER LIST MUST NOT CONTAIN WORDS THAT QUALIFY NOTHING.** Narrowing a bare
  `aeroelastic` to require a nearby aeronautical noun left an aeroelastic **panel** paper admitted,
  because the qualifier list contained `model` and `analysis`. **The regression test failed twice on
  the same title**, the second time because the leak was in a different pattern from the one being
  edited. A panel, a plate and a shell are aeroelastic and are not wings.
- **A LINEARISATION IS NOT FREE AND THE FUEL FRACTION DECIDES.** The whole keystone rested on
  linearising the Breguet exponential at a **twenty percent** fuel fraction, where the linearisation
  overstates fuel by 11.585 percent. **Carrying the exponential generalised both optimality conditions
  by one factor, moved every figure, and closed a gap the drafting pass had to apologise for**, taking
  the computed penalty from above the report's independently optimised bound to inside it. **Check the
  fraction before linearising anything, and take the limit to prove the general form reduces.**
- **WRITE DOWN THE GOVERNING EQUATION AND IT WILL AUDIT THE PRIMARY SOURCE FOR YOU.** Writing the lift
  equation showed that the Phase IV drag buildup's stated altitude, Mach number and lift coefficient
  **do not hold together at the aeroplane's own weight**, and that the altitude at which they do is
  the report's own optimum altitude from a different table, seventy-eight feet away. **No amount of
  reading would have found that. Only the equation did.**
- **SEVEN SYMBOL COLLISIONS IN ONE PASS, AND THE ESTABLISHED MEANING KEEPS ITS LETTER.** Cap
  separation yielded its letter to altitude, the flat plate area took a script form because the plain
  one was the moment shape function, fuel volume yielded to airspeed, the record set to range, the
  budget projection to the prop force, block fuel to span, and the milestone payment to fuel mass.
  **`symcheck.py` also needed the trigonometric functions and the layout directives added to its
  structural set**, neither having appeared in this series before.
- **SPELL SMALL COUNTS AT THE EMITTER AND NOT IN THE PROSE.** Fourteen were numerals where the
  convention asks for words. **A convention enforced in prose is a convention that drifts** when a
  count changes, so the rule now lives in the emitter and the verifier reads the words back through
  `_lib/survey.py`'s words-to-integer helper rather than parsing them as integers.
- **A SUPERLATIVE NEEDS A COMPARISON SET OR IT IS DECORATION, AND ONE WAS SIMPLY FALSE.** Thirteen
  rankings were scoped in the publication review. The centroid argument was called **the only
  independent confirmation** of a closed form the same paragraph confirms twice. The fold was **the
  single largest number in this article**, which carries a ratio of ten thousand to one. **Two
  rankings were kept by attaching their reasons, which was what had been missing rather than the
  ranking itself.**
- **A HEADING CAN BE REFUTED BY ITS OWN PARAGRAPH.** A heading claimed a budget document says three
  things nothing else says, and three sentences later the paragraph conceded that the agency's press
  item says one of the three too. **The concession was right and the heading was wrong**, which is
  this series' most frequent defect and is why the risky-claim scan exists. **Run `pubreview.py
  risky` and read every absolute and negative-existence claim against the paragraph it sits in.**
- **AND A FACTUAL ERROR SURVIVED THREE PASSES.** An aeroplane was placed in the wrong aerodrome code
  class by one band. **The publication review found it and the corrected passage is stronger**,
  because the aeroplane that does belong in the lower class folds its wingtips, which is precisely
  the manoeuvre the article argues its subject depends on and which is already certificated.
- **A DEAD CITATION IS A REASON TO FIND A BETTER SOURCE, NOT TO SOFTEN A CLAIM.** The address sweep
  found a standards body's publications page unreachable. Replacing it sent the argument to the
  regulator's own circular, **which is in feet with exclusive bounds and settled the unit question
  the keystone turned on.** The article got stronger because a citation died.
- **A COMPUTED FIGURE TYPED INTO PROSE IS A STALENESS BOMB, AND A MECHANICAL SCAN FINDS THEM.** A362
  shipped a stale pool size for exactly this reason. A363 scanned every numeric literal in its prose,
  excluding quotations, tables, mathematics, dates, designations and instrument numbers, and **three
  survived the exclusions as computed quantities** and became slots. **A fourth was a citation gap
  rather than a staleness risk**, a span figure attributed to nothing, now attributed to secondary
  coverage and to no primary document the article has read.
- **AND THE SHARED TREE WILL SWEEP UP THE OTHER LINE'S WORK, SO SAY SO IN THE MESSAGE.** A363's
  publication-review commit carried A376's staged draft. **Do not unstage another session's work to
  tidy an attribution**, which is the larger risk. Record it in the commit message, which is the
  convention this file already carried and which A363 followed. The mirror happened at `29af463`.

### Earned in A362, and the theme is that a correction can need correcting

**READ THIS SECTION BEFORE THE OLDER ONES.** A361's theme was that a check can be immune to the
thing it was written about. **A362's is narrower and more uncomfortable: three of its own
conclusions were overturned by a later pass of the same article**, and in two cases the fix for a
defect introduced a worse one. **A pass that corrects an earlier pass is not thereby right.**

#### The Reynolds argument, which the equation pass asserted and the primary pass withdrew

**THE EQUATION-DENSITY PASS COMPUTED A GAP AND DREW THE WRONG CONCLUSION FROM IT.** It found the
X-65A's flight Reynolds number at 11.44 million, compared it with the experiments whose thresholds
the article had borrowed at between twenty-three thousand and six hundred thousand, and concluded
that those thresholds were the part most likely to be wrong at flight scale. **The arithmetic was
right and the inference was not.**

**The primary-reference pass found the report that settles it.** Seifert and Pack, AIAA 2000-2542,
read in full from the reports server, demonstrated oscillatory separation control at chord Reynolds
numbers as high as forty million and state that the Reynolds number has a very weak effect on the
pressure distributions and spectra of a deliberately fully turbulent baseline. **The aircraft flies
BELOW the demonstrated range.** The rule is not about aerodynamics. **A gap between two numbers is
not evidence about which of them is wrong, and the pass that computes a gap is not the pass that can
interpret it.**

**AND THE SAME REPORT NAMED THE ARTICLE'S KEYSTONE AS AN OPEN PROBLEM**, proposing that the lack of
sufficient control authority especially at high speeds be overcome. **The second time in three
passes that a primary showed a result to be a rediscovery**, the first being Reddy and Woszidlo on
the altitude scaling. **An article that derives something elegant should assume the literature has
it and go looking before claiming otherwise.**

#### A guard defeated by a hyphen, which the shared library structurally cannot repair

**`_lib/gate.py` FLATTENS INTRAWORD HYPHENS ONLY AFTER AN UNFLATTENED PATTERN HAS FAILED.** That is
correct for a body anchor, which is tried again in flattened form on a miss. **It is useless for a
guard, because a guard is a negative lookahead and a guard that fails to fire is a guard that
ADMITS.** The record is admitted on the first attempt and flattening is never reached.

A362's rotorcraft guard was written `hingeless rotor` with a space and the reports server writes
`hingeless-rotor`, so **the guard admitted the rotor-hub paper it existed to refuse.** `check_guards`
caught it. **Two further guards then leaked when the same refusal cases were re-tested with their
spaces hyphenated**, having passed because the regression test used the spelling the probe happened
to return. **A test that uses one spelling is a test of the probe and not of the guard.** Every guard
phrase now goes through `sep()`.

#### Kramdown pairs underscores across inline mathematics, and a guessed fix made it worse

**THE RENDERED PAGE CARRIED TWO CORRUPTED EXPRESSIONS AND NOTHING SAW THEM.** Kramdown does not
protect `$...$` from markdown processing, so an underscore opened emphasis in one expression and
closed it in another, putting an `<em>` tag inside the mathematics. **`_verify.py` passed,
`_lib/render.py` passed, and MathJax still rendered.** It was found by reading a snippet of the page
by eye.

**THE FIRST FIX WAS BUILT ON THE COMMONMARK FLANKING RULE AND TOOK TWO CORRUPTED SPANS TO THREE.**
Kramdown's rule is not CommonMark's. **A five-line probe of kramdown settled it in one run**, and the
measured rule is that an underscore OPENS when the character before it is not a word character and
CLOSES when the character after it is not. Escaping the openers costs nothing, because kramdown
consumes the backslash and MathJax receives the underscore.

**THE RULE: PROBE THE TOOL. DO NOT MODEL IT.** The probe is five lines and it is faster than one
wrong fix. **And the defect is pre-existing and corpus-wide**, seventy-two emphasis pairs across
thirty-eight files, thirty-five of them published posts, including this series' own opener and A361.
**Those are reported and untouched, because editing the mathematics of published posts is the
pilot's call.**

#### A claim count that was wrong twice, because the model was wrong both times

**THE FIRST SCAN FOR THAT DEFECT REPORTED 1,225 PARAGRAPHS IN 202 FILES AND WAS USELESS.** The
second, on the CommonMark rule, reported fifteen pairs in ten files. **The third, on the measured
rule, reports seventy-two in thirty-eight.** The wrong middle figure had already been written into
the process files and was corrected before the commit. **A corpus-wide count is only as good as the
model behind it, and a plausible count is the most dangerous kind.**

#### A span bounded by a later section's text is not a safe edit, and that is twice

**TWICE IN ONE SESSION A REPLACEMENT DELETED CONTENT NOBODY INTENDED TO TOUCH.**

The primary pass rewrote a body file by replacing everything from one heading to another. **A third
heading sat between them**, so the moment relation and its table went with the span. **Every figure
still reconciled, every slot still filled, `_verify.py` passed and the rendered audit passed**,
because a missing equation is not a defect in anything that remains. Only a count found it.

The same pass then edited `TASKLOG.md` by replacing a span running from a paragraph in the Current
Task block to the history table's header. **Success Criteria, Notes and the History heading all sat
between them and all three were deleted.** `_verify.py` caught it by reporting four different drafted
counts in a Current Task block that then contained the whole history table. **It was repaired from
`git show HEAD` and the section list was compared before and after.**

**THE RULE: MATCH THE TEXT YOU MEAN TO CHANGE, NEVER A SPAN BOUNDED BY TEXT THAT BELONGS TO SOMETHING
ELSE.** And after any structural edit to a long shared document, **compare the heading list before
and against after.**

#### A resolver that can legitimately return nothing cannot detect its own failure

**THE YEAR RESOLVER FAILED ON ALL 1,321 RECORDS AND RAISED NOTHING.** It read the raw response's
`publications` field from `fetch.ntrs_detail`, which returns a PARSED result and had already consumed
and discarded it. **An empty year is a legitimate value for an undated record**, so a total parser
failure and a dateless registry are the same observation.

**THE ONLY INSTRUMENT THAT SEPARATES THEM IS A SUCCESS-RATE FLOOR**, and the file now refuses to
finish below one half. The real rate is 0.945. **Any resolver whose null answer is meaningful needs
this.**

#### A zero-count cluster is invisible in a Counter

**`collections.Counter` NEVER CREATES A KEY IT DID NOT COUNT**, so a check that looked for zero values
found none and the one empty cluster was invisible. **The empty cluster was a finding**, being that no
record in a pool of twenty thousand names this programme, this aircraft or its contractor. **Take the
key list from the gate, not from the counter.**

#### A figure that is not a slot goes stale, and only this one did

**THE EMPTY-CLUSTER MESSAGE CARRIED A HARD-CODED POOL SIZE AND THE THIRD SWEEP MOVED IT.** The
article stated 18,432 where its own source base said 20,430. **Every other number in the article is
filled from a slot and this one was a literal in an emitter**, which is exactly why it was the one
that went stale. **A number about the corpus is read from the corpus.**

#### An acronym can reach the reader as a mathematical subscript

**`AFC` APPEARED FIRST IN AN EQUATION AS `\Delta L_{\mathrm{AFC}}` AND WAS NEVER EXPANDED.**
`symcheck.py` could not see it because it strips `\mathrm{...}` before comparing symbols, so **a
subscript that is itself an unexpanded acronym passed every check the article had.** The acronym
trace in the publication review found it. **Declare subscripted forms, and trace acronyms through
mathematics as well as prose.**

#### A test's own reference values are the likeliest place for an equation pass to fail

**THE NEW EQUATION VERIFIER FAILED FOUR TIMES ON ITS FIRST RUN AND THREE WERE ITS OWN TABLE.** It
carried the 1976 standard-atmosphere values at five thousand FEET against a key in METRES. **A unit
confusion in a test accuses the code of the test's own mistake**, and this is the fourth time in this
series an equation pass has failed in the check rather than the article.

**The fourth failure was a Monte Carlo whose bounding box missed the extreme points**, so it reported
a hull area BELOW the closed form. **For a coarse outer approximation that is impossible, and the
impossibility is how it was caught.** A cross-check that disagrees in the impossible direction is
telling you about itself.

#### A scratch script must not take a standard library module's name

**A FILE CALLED `select.py` IN THE WORKING DIRECTORY BROKE `subprocess` IN A SCRIPT THAT NEVER
IMPORTED IT.** The directory goes on `sys.path`, so it shadowed the standard library module,
`selectors` could not find `select.select`, and the failure surfaced in an unrelated file naming a
module nobody had written.

#### A doubled escape leaves a literal backslash in the page

**AN ESCAPED CITATION WRITTEN WITH TWO BACKSLASHES RENDERS ONE.** It came out of a replacement script
whose escaping went through one level too many, which is the same shape as the doubled-spacing-macro
defect the verifier already carries for display mathematics. **It was found by counting brackets in
the rendered page against display blocks in the source, 47 against 46**, where the extra was not an
equation at all.

#### A ranking is a measurement or it is scoped

**THE PUBLICATION REVIEW FOUND SEVEN RANKINGS THIS ARTICLE HAD NOT EARNED**, among them that its
subject vocabulary is the worst the series has met, across vocabularies never measured, and that
`CRANE` is the least useful query in a sweep where ten of roughly two hundred probes were read by
hand. **And one claim was refuted by counting.** The article said seventy-two reports for `hingeless
control` were all helicopters; counting all seventy-two gives sixty-one, and two of the exceptions
are a morphing-wing programme that is genuinely adjacent prior art. **If a claim is countable, count
it rather than sampling it.**

#### A shared tree will commit your uncommitted work

**THE OTHER LINE'S COMMIT CARRIED THIS LINE'S UNCOMMITTED `REVERSE_PROMPT.md` SECTION.** The content
is intact and the attribution is wrong, so the A362 primary-reference report is committed under a
message naming A375. **Stage and commit promptly, because in a shared tree an uncommitted file is
somebody else's to sweep up.**

### Earned in A361, and the theme is that a check can be immune to the thing it was written about

**THE READING ORDER IS THE ORDER THE FAILURES WERE FOUND**, because the point is that each one was
found by an instrument that was not looking for it.

#### The gate bug, which is the largest and which nothing but the audit would have caught

**A GUARD THAT IS ANCHORED AT THE START OF THE STRING ANCHORS WHAT IT GUARDS.** A361's subject gate
combined exclusion guards with match patterns by concatenation, `_NOT_SOFTWARE + _NOT_HVAC + BODY`,
where each guard is `\A(?!.*\bbad\b)`. **The guard's `\A` fixes the match position at zero, so
`BODY` then has to begin the title.** Every guarded pattern matched only titles opening with its own
subject phrase.

**Nothing failed.** The gate ran, admitted a plausible 4,164 records and clustered them. Three
clusters came back absurdly small, being fins at 16 records, modular vehicles at 12 and the named
cluster at 1, against neighbours in the hundreds, **and a small cluster looks like a small
literature.**

**WHAT FOUND IT WAS THE MANDATORY TWO-SIDED AUDIT.** `gatelib.audit` prints thirty random REFUSED
records beside thirty kept ones, and the refused list contained `Qualitative investigation of booster
recovery in open sea` while `booster recovery` was a phrase the gate was written to keep. **A count
cannot tell you what is missing. A sample of what you threw away can.** Repairing it took fins from 16
records to 148 and recovery from 310 to 546.

**The fix is `guarded(guards, body)`, which puts the body in its own lookahead** so the whole
expression is zero-width at position zero and the body is free to match anywhere. **Copy it and copy
`check_guards` with it.** That test pins five keep cases and nine refusal cases, and **every keep case
places its subject phrase in the MIDDLE of the title on purpose**, because a silently anchoring guard
passes a test whose phrase comes first.

**THIS IS THE FIFTH APPEARANCE IN THIS SERIES OF A LOOKAHEAD THAT DOES NOT GUARD WHAT ITS AUTHOR
THOUGHT.** The earlier four were negative lookaheads placed before an alternation, which guard only
the first clause. This one anchors instead. **The family resemblance is that a lookahead's scope is
never what the eye assumes**, and the only reliable response is to test every pattern against a string
it should match and a string it should refuse, at the moment it is written.

**AND THE SAME AUDIT CAUGHT THE OTHER DIRECTION.** Among the kept records were a taxonomy of SCADA
vulnerabilities, a tiltwing electric aircraft, ice borehole thermometry and a microrolling process
monitor. `data acquisition ... system` admitted the first because **the bare word `system` is not a
subject anchor**, `vertical landing` admitted the second, and bare optimal-sensor-placement admitted
the others. **An audit that only reads the kept side is half an audit.**

#### A measurement that refuted the reason for taking it

**TWELVE HOMONYM-STORE FAMILIES WERE MEASURED AND THE DECISION NEEDED SEVEN.** The candidate list was
built around `ndt`, on the argument that a family earned against non-destructive testing could delete
this article's structural-health-monitoring cluster wholesale. **`ndt` releases one record from this
pool.** So does `delamination`. `composites` releases thirteen and `ecology` none.

**The store's tagged families were earned against other articles' contaminants, and this article's
contaminants are words the store carries no patterns for**, which is why its own homonym probe found so
much while the store released so little. **When a measurement comes back near zero everywhere, that is
a finding about the instrument rather than a boring result.**

#### Two power laws are not a trajectory

**A360 FITTED ALTITUDE ALONE AND A361 INHERITED THE FIT INTO A PLACE IT DID NOT BELONG.** A360's
`h_b (t/t_b)^n` sits inside a pressure integral where only altitude enters. Dynamic pressure needs
altitude and speed together, and pairing that altitude law with a speed law linear in time put the
vehicle at Mach 2.85 at 8.4 kilometre, returned a peak dynamic pressure of **190 kilopascal** against a
launch vehicle's usual thirty to forty, and gave a drag-to-thrust ratio above one.

**The model refuted itself on a quantity nobody asked it about**, because a drag fraction above one
describes a decelerating vehicle and this one was climbing. **Neither fit was wrong on its own.** The
defect was treating two dependent quantities as independent assumptions.

**The repair removed an assumption rather than correcting one.** A rocket's altitude is the integral of
the vertical component of its own speed, so a speed law and a pitch program determine it, and **the
published cut-off altitude then fixes the remaining parameter instead of being assumed alongside it.**

**The habit: evaluate a derived quantity the model was not built to produce.** A drag fraction, a Mach
number and a dynamic pressure all have ranges a reader of the field knows by heart. **And inheriting a
fit from another article inherits the conditions under which it was valid.**

#### A hull is not a rosette, and the closed form had the right range with the wrong orientation

The tip-over lever arm was first computed by measuring the angle to the nearest leg and dividing the
inradius by its cosine. **That produces a function with the correct range and the inverted
orientation**, placing the short lever arm at a leg and the long one in the gap, which says a
four-legged vehicle is most stable in the direction it is least stable in.

**A RANGE CHECK PASSES AN INVERTED FUNCTION.** The minimum and maximum were both right. What was wrong
was which direction attained which, and **evaluating the closed form at the two special directions and
asking which gives the smaller number settles it in one line.** Both orientations look plausible
written down, which is why the check is worth the line.

#### A test's own reference values are part of the test

**FOUR OF THE FIRST RUN'S FAILURES WERE IN THE TEST AND NOT IN THE ARTICLE.** A 1976 standard-atmosphere
reference value was entered as 255.676 kelvin at 5 kilometre where the standard says 255.650, and a
brute-force sweep written as `range(2000)` against a `/20000` denominator walked a tenth of the circle
and so found the minimum of an arc. **A reference table copied by hand is an untested input**, and a
loop bound and its denominator are a pair that must be read together.

#### The scope of a check is a claim about the article

**A PROSE-LITERAL CHECK REPORTED AN HONEST SENTENCE ABSENT.** `verify_numbers.py` defined the article's
body as everything before the Contemporary Literature heading, which silently excluded the Epistemic
State, the Out of Scope section and the Conclusion. A literal stated only in the conclusion read as
missing. **A check whose scope is wrong fails honest prose and passes nothing.**

**The same defect appeared a second time in a different instrument.** The publication review's
decision probe reported one of forty decisions stranded, and the article did carry it. **The probe had
been written with my own report's phrasing rather than the article's.** Both cost a false alarm and
neither cost a defect, which is the cheap direction, but **a check that can only fail falsely is still
a check that needs fixing**, because the next false alarm trains its author to discount it.

#### A withdrawn wording has no number to recompute

**A360's PUBLICATION REVIEW FOUND A RETRACTED PHRASE STANDING IN TWO SUMMARISING SECTIONS**, and the
same thing happened here in the drafting pass. The drag-coefficient inequality is an inference from the
ordering of drag contributions and was asserted as a computation in two later sections after being
hedged in the one that established it.

**652 numeric checks could not see it, because a retracted wording carries no number.** So
`check_withdrawn` now asserts the withdrawn wordings ABSENT and the hedges PRESENT, **and it needs both
halves**, because a check that only forbids the bad wording passes when the hedge is deleted too.

#### A publisher's refusal is not a dead link

Three of thirty-three hand-written addresses failed to fetch, all of them IEEE and ASME DOIs, and all
three are registered with matching title, author and year. **A DOI that will not fetch is now looked up
in the registry that issued it**, and that is the stronger check anyway, because it confirms the
identifier points at the document the article names where a 200 from a landing page does not. **The
sweep reports fetched, confirmed-through-the-registry, and unresolved as three outcomes**, since
collapsing the middle case into either of the others is a lie in one direction or the other.

#### The index and the reports server hold different literatures

**A361's HOMONYM PROBE FOUND `Barrowman` RETURNING GASTROINTESTINAL LYMPHATICS AND CONTEXT-AWARE RANDOM
NUMBERS**, and the reports server holds his 1967 report under its title. **A method that circulated as a
report and then as a handbook convention has no presence in an index of journal papers.** The two
registries are not the same literature to different depths.

**AND A SOURCE LIST AT THE FOOT OF A SECONDARY IS A RETRIEVAL CHANNEL.** The single most important
primary in A361, the laboratory background paper that contradicts the register, would not have been
returned by any of this article's 166 sweep questions, because it is a public-affairs document with no
report identifier. **It was found by reading the encyclopedia entry's own source list.**

#### The porcelain comparison broke a fourth time, inside the check written to stop it

**THREE EARLIER HANDOFF SELF-CHECKS BROKE ON `git status --porcelain`**, because the format carries a
two-character status field whose first character is a SPACE for an unstaged modification, so ` M file`
must be compared as a whole line with that space preserved. A360's check fixed it and said so.

**A361's CHECK BROKE ON IT AGAIN, AND THROUGH ITS OWN HELPER.** The `sh()` wrapper called
`.strip()` on every command's output, which removed the leading space from the first porcelain line,
so ` M _docs/process/HANDOFF.md` arrived as `M _docs/process/HANDOFF.md` and compared unequal. **The
comparison was written correctly and the helper undid it one level down.**

**It was caught by the check failing rather than by anyone reading the code**, which is the system
working, and the repair is a `strip` parameter defaulting to true with the porcelain call passing
false. **The transferable rule is that a general-purpose output helper must not normalise whitespace
for a caller whose format is whitespace-significant**, and the place to look for a defect you have
already fixed is the layer you added since.

**AND THE SAME RUN FOUND TWO OVER-STRICT ASSERTIONS IN THE SAME CHECK.** A multi-word figure was
reported missing because the handoff is hard-wrapped and the literal straddled a newline, and an
allocation date was reported missing because the register stores `24-Apr-23` while the house form is
prose. **Both were checks that would only ever fail falsely**, and a check that can only fail falsely
still needs fixing, because the next false alarm trains its author to discount it.

#### And the established practice may already have stated your premise

**A361's DRAFTING PASS DERIVED FROM SCRATCH A CLAIM THAT IN-FLIGHT THRUST DETERMINATION HAS STATED
SINCE THE NINETEEN EIGHTIES**, that thrust is not measured but calculated from models of direct
measurements. **The primary-reference pass found the literature and the engagement improved the
article twice over.** It converted a derivation into a confirmation, and it surfaced a real limitation,
because the established methodology separates bias from precision and carries a model bias error where
this article's budget combines three terms in quadrature as though all were random.

**The article now says plainly that it presents a sensitivity analysis and not an uncertainty
statement.** **Search the field's own vocabulary for your keystone before deriving it**, and expect the
engagement to cost you a hedge as well as buying you a citation.


### Earned in A360, and the theme is that each pass found the previous pass's most confident sentence to be its weakest

**THE READING ORDER OF THIS SECTION IS THE ORDER THE PASSES RAN**, because the point is the sequence.
The drafting pass stated a conclusion with no hedge. The equation pass found that the article had
performed a whole calculation and shown none of its machinery. The primary-reference pass read one
document and withdrew the drafting pass's conclusion. **No check failed at any stage. Each pass
found the previous one's confident sentence by doing its own job properly.**

#### The instrument findings, of which the first is the largest this series has had

**THE REPORTS SERVER WAS BEING READ TEN RECORDS DEEP BY EVERY ARTICLE IN THIS CORPUS.**
`fetch.ntrs_search` passed its page specification as a single encoded object. **That server clamps
such a request to ten records AND SILENTLY IGNORES THE OFFSET INSIDE IT**, so six requests at six
different offsets return the identical ten records. Passing `page[size]` and `page[from]` as separate
bracketed query parameters is honoured. **The question `plug nozzle` matches 242 records, of which
the old call returned 10 and the corrected one returns all 242 with no duplicates.** A360's fourth
sweep returned **10,160 reports-server records against 606 from its first three sweeps combined**,
and its report-primary fraction went from 10.4 percent to 30.6.

**EVERY PRIMARY-REFERENCE PASS IN THIS SERIES HAS COMPLAINED THAT THE REPORTS FRACTION IS THIN**, and
part of that complaint was an instrument reading its first page. **The fix is in `_lib/fetch.py` and
is held by a test that runs offline against a fake transport**, checking both the parameter spelling
and that the walk advances. **Expect every sweep after A360 to return far more than the sweeps before
it, and do not compare a post-A360 primary fraction with a pre-A360 one without saying which side of
the repair it sits on.**

**AND THE SERVER REPORTS ITS OWN TOTAL, WHICH NOTHING WAS READING.** `fetch.ntrs_total` is added.
With it a sweep's coverage becomes a measurement, and A360 reports that across 89 questions the
server held 32,488 records and returned 14,929. **The average hides a clean split and the split is
the useful figure.** Sixty-eight questions were exhausted and returned all 7,798 they held; 21 hit
the article's own walk limit; **every one of the 17,559 records not taken belongs to those 21**, which
are the broad organisational questions. **Report the split, not the average.**

**A COVERAGE FIGURE IS ONLY WORTH QUOTING WHERE THE DENOMINATOR IS A MATCH COUNT.** The reports
server performs a boolean match against a curated collection, so its total means something. **The
bibliographic index performs a ranked retrieval and answers 2,406,511 to `rocket nozzle
performance`**, which is not a count of anything an article wants. The defence registry sits between
them, being a ranked retrieval restricted to one prefix, and there a total is meaningful again.

**A `sys.path.insert` INSIDE A PER-RECORD FUNCTION IS A QUADRATIC COST THAT LOOKS LIKE SLOW NETWORK.**
`homonyms._anchor_stem` inserted a directory and imported once per harvested record. The import is
cached; **the insert is not**, so a thirty-thousand-record sweep left thirty thousand copies on the
path. **A360 measured 6.19 seconds for three thousand records and 6.27 for the same three thousand on
a second pass**, which is the signature of a cost that grows with work already done. Hoisting the
import and memoising the stem takes a repeated pass to 2.27 seconds. **Time the same input twice in
one process. A pure function that takes longer the second time is mutating something.**

#### A procedure written down is not a procedure followed, which is A359's theme arriving again

**A360 RAN `./_check.sh --drafts` FIVE TIMES AND LET THE LAST ONE HOLD A PROCESSOR AT A HUNDRED
PERCENT FOR FIVE HOURS AND FORTY-ONE MINUTES WITH AN EMPTY OUTPUT DIRECTORY.** This file already
recorded that the full-corpus drafts build scales superlinearly in link-definition count, that it
took over three hours by A340, and that **the agent runs the stub build per pass and the full build
at publication absent instruction**. **The stub build it should have run took sixteen point nine
seconds.** The answer was written down before the work began and the cost of not reading it was a
working day of wall clock.

**THE RECIPE IS IN `tmp/a360/site_build.sh` AND THAT PATH IS GITIGNORED, SO USE IT BEFORE IT IS
GONE.** Copy the repository excluding `_site`, `tmp`, `.git` and `vendor`, symlink `vendor` back in,
put the article under work into `_posts` with its date prefix, write every sibling draft into
`_posts` as front matter plus one line, empty `_drafts`, **match the checksum before the build starts**,
then build with `JEKYLL_ENV=production` and run `_lib/render.py` on the output. **Do not run
`_verify.py` against the stub**, because the stubs would fail it. Run that against the real tree.

**AND A `cd` IN A COMMAND THAT ENDS WITH `&` DOES NOT PERSIST.** The first entry in
`VERIFICATION_TRAPS.md` records a `cd` that persisted and cost eight edits. **A360 met the inverse.**
A patch addressed a scratch file by bare name, reported that it had patched it, and **patched nothing
the build would read**, and the stale wording reached the assembled article twice. **Address every
file by absolute path, and after a patch grep the file for the text the patch was supposed to
introduce.** A script that prints `patched` has reported its intention, not its effect.

#### A cached measurement does not know what it depends on, and this fired three times

**THE FAMILY-COST REPORT IS EXPENSIVE, SO A360 PERSISTED IT, AND THEN THE CACHE WAS WRONG TWICE.**
First it compared the current allow list against that list plus the candidate tag, so **the moment a
family was opened on that evidence the difference became empty and the report said zero**. The
evidence for the decision vanished at the instant the decision was made. **Measure against the
baseline the decision was made from.** Second it was keyed on a fingerprint of the gate's patterns,
and **the fourth sweep changed the pool rather than the gate**, which would have served the old
counts against new records. The fingerprint now covers the pool size.

**RECORD THE FINGERPRINT OF WHATEVER A CACHED VALUE DEPENDS ON, ALONGSIDE THE VALUE.** A cache whose
key is a filename is not a cache. **And if a report exists to justify a choice, it must still read
the same after the choice.**

#### A band taken on report is not a band

**THE DRAFTING PASS SAID THE TRAJECTORY-OPTIMAL NOZZLE CANNOT BE BUILT, ON A THRESHOLD IT DECLINED TO
ATTRIBUTE.** It quoted a separation band of about a quarter to about four tenths from secondary
accounts, said plainly that this article had not read the correlations, and drew a flat conclusion
from the conservative end.

**NASA TECHNICAL PAPER 1207, READ IN FULL BY THE THIRD PASS, TOOK THE CONCLUSION BACK.** The four
tenths belongs to Summerfield, Foster and Swan in 1954, and the paper records that it **is still
quoted today although more recent studies have shown it to be inadequate**. It is a conical-nozzle
rule. **Contoured nozzles, which is what a rocket has, follow a different correlation**, and under
that correlation the optimum separates only below about 3.3 to 3.7 megapascal of chamber pressure.

**A RANGE QUOTED WITHOUT ITS PROVENANCE HIDES WHICH END BELONGS TO WHICH CASE.** That is the rule.
**And the pass that goes looking for sources is the pass that can fix it**, which is an argument for
doing the primary-reference pass before believing anything the drafting pass concluded from a
secondary account.

**THE SAME PAPER ALSO RESTORED AN ATTRIBUTION THE DRAFTING PASS HAD STRUCK FOR GOOD REASON.** A360
went looking for the name behind the four tenths, found a 1953 paper by Scheller and Bierlein in the
bibliographic index instead, and removed the attribution rather than assert it. **Removing it was
right on the evidence then available.** The paper that corrects it also explains the confusion,
because Scheller and Bierlein are the early study that **conflicted** with the others. **A search
that returns the nearest thing is not a search that returns the right thing.**

#### An article can perform a calculation and show none of its machinery

**A360's DRAFTING PASS USED THE THRUST COEFFICIENT IN NINE PLACES AND NEVER DEFINED IT.** It used the
area ratio without relating it to the throat, used the isentropic relations without writing them, and
**never mentioned the throat area anywhere in the article**. Fifteen display equations looked like an
adequate density and the gap was structural rather than thin.

**THE CUE-PHRASE SCAN FOUND TWELVE SENTENCES AND WOULD HAVE MISSED ALL OF IT.** What found it was
**listing every symbol the mathematics uses and asking which had been introduced**. Do that. A search
for prose that describes a relation finds relations the author chose to describe; it cannot find the
ones the author assumed.

**AND THE SYMBOL TABLE IS WORTH BUILDING AT THIS DENSITY BECAUSE THE SCANNER THAT CHECKS IT FINDS
REAL THINGS.** `tmp/a360/symcheck.py` requires every symbol in the mathematics to be declared and
every declaration to be used, and it caught two undeclared symbols the third pass introduced.

**THE SCANNER'S PASS ORDER WAS WRONG THREE TIMES BEFORE IT WAS RIGHT, AND THE REASON GENERALISES.**
Stripping operators first breaks every declared name containing a macro, so `C_{F,\mathrm{vac}}`
stops matching and reports a bare `C`. Stripping declared symbols first breaks the operators, because
a single-letter symbol such as `c` sits inside `\frac`. **The only order in which no pass destroys
another's input is compound names first as placeholders, macros second, bare letters last**, and
environment names then have to go with their braces because `\begin{cases}` leaves `{cases}` behind.
**A358 and A359 both recorded that a symbol name must not contain a macro the scanner strips. A360's
addition is that the same hazard applies to the ORDER of the passes.**

#### Checks that caught the author rather than the code

**A NUMERIC VERIFIER CANNOT SEE A MISSING UNIT AND CANNOT SEE DATE ARITHMETIC.** A359 shipped a value
with no unit. **A360 wrote four months where the answer is eight**, a three-year term from December
2019 against an allocation of 20 April 2022, and nothing in the suite was looking at dates because a
month is not a quantity the calculation files produce. There is now a check that recomputes every
interval the prose states between two named dates.

**AN ENUMERATION MUST HAVE AS MANY ITEMS AS THE SENTENCE CLAIMS.** A360 wrote that ten of eleven
duplicated register descriptions are munitions and targets, and then listed nine, having merged two
of the three target entries. **Nothing counts a list for you.** The repeat structure is now recomputed
and the multiplicities the prose names are checked against it.

**BOTH SCALE HEIGHTS ROUND TO 8,435 AND A360 PRINTED THEM AS 8,435 AND 8,434.** The gap is four
tenths of a metre. **Rounding to whole metres makes two numbers that agree look as though they
disagree**, which is the opposite of what the sentence was for. Caught by a check that compared the
two roundings rather than the two values.

**OVERLAP IS NOT CONTAINMENT.** A360 said the chamber-pressure band recovered from the instability
frequency **sits inside** the band it had assumed independently. It does not; its floor falls below
the assumed floor and the two merely overlap, over 93.5 percent of one and 82.0 percent of the other.
**The calculation had only ever tested overlap and the prose promoted it to containment.**

**AND A CLAIM ABOUT A WHOLE RANGE MUST BE CHECKED AT BOTH ENDS OF IT.** A360 said the contoured
separation correlation tolerates roughly twice the over-expansion of the flat rule. **It crosses the
flat rule at separation Mach 2.59 and is stricter below that**, reaching 0.433 at the bottom of its
fitted range against the flat 0.400. The permissive end is the end that applies to this article's
nozzles, **and saying `far more permissive` without the crossing would have repeated the very error
the section is about**.

#### A formula outlives the assumptions that made it true

**A360 DERIVED THE GUARANTEED CONTROL AUTHORITY OF A REGULAR RING AND THEN USED THE SAME FORMULA FOR
A RING WITH ONE THRUSTER FAILED.** A ring with a hole in it is not regular. The formula overstates the
surviving authority by up to a factor of 2.62 and, at four modules, by all of it, since **a
four-module ring loses every bit of guaranteed authority when one fails** and the formula reports a
quarter. **No test was looking and nothing failed.** It was found by asking whether the derivation's
assumptions still held.

**AND A VERIFIER'S INDEPENDENT ROUTE MAY DISAGREE BECAUSE THE GEOMETRY IS REAL.** The ring check
evaluated the maximum at the module directions, which is right for an odd ring and wrong for an even
one, and reported eighteen failures with the two extremes swapped. **The closed forms were correct.**
For an even ring the control polygon is rotated half a side, so the direction of least authority
points straight at a module. **When two routes disagree, establish which is wrong before repairing
either**, because the disagreement is sometimes information about the subject.

#### A survey number typed into prose goes stale, and a table is prose

**ADDING TWENTY-TWO HAND-WRITTEN REFERENCES MOVED A360's RESEARCH COUNT FROM 9,485 TO 9,467**, because
a record that acquires a hand-written definition stops being auto-cited. The prose said 9,485 and the
frozen-occurrence check caught it. **The repair is not to retype the number.** Put a slot in the prose
and fill it from the file that computes it.

**A NUMBER SLOT MAY LEGITIMATELY APPEAR TWICE AND A BLOCK SLOT MAY NOT.** The assembler's once-only
rule was written for generated blocks, where a repeat means a duplicated section. A figure may be
stated in two sentences and is still safe because both come from one computed value.

**AND A SLOT THAT HOLDS A YEAR IS DESCRIBED IN PROSE BY WHAT HAPPENED THAT YEAR.** A360 calls the
earliest record in its plug-nozzle family a weather-rocket patent. **If a later sweep finds something
older, the slot updates silently and the description does not**, so there is now a check that the
record the slot came from still matches what the prose calls it.

#### A pairwise continuity test is decided by its single worst gap

**A360 NEEDED THE YEAR FROM WHICH A LITERATURE PUBLISHES CONTINUOUSLY.** The first test asked for the
first year after which no two consecutive publishing years differ by more than three. **One four-year
gap between 1988 and 1992 moved the answer from 1956 to 1992**, thirty-six years, and the number
looked plausible enough to write down. A window test, asking that every window of a fixed length
contain at least one record, cannot be moved by one gap.

**AND WHEN THE WINDOW GETS WIDE ENOUGH IT STOPS MEASURING THE LITERATURE.** After the fourth sweep
added a second record in the nineteen forties, the eight-year and ten-year windows put the start at
1944 while the five-year and six-year windows still say 1956. **At that point the window is doing the
work.** The article reports both and says which.

#### Two thrust figures in one table row are not one nozzle

**A360 ALMOST DERIVED AN EXIT AREA FROM A SUBTRACTION THAT IS ARITHMETICALLY VALID AND PHYSICALLY
EMPTY.** The manufacturer's table prints `12,100 (sea-level)` and `13,000 (vacuum)` on one row, and
the difference divided by sea-level pressure would give the exit area exactly. **Two lines above, the
same document says stage one uses nine sea-level engines and stage two uses one vacuum engine**, so
the figures describe two different nozzles. **Read what a table says about itself before doing
arithmetic across it.**

#### And two store families guarded this article for reasons that had nothing to do with it

**`fracture` WAS EARNED BY A335 AGAINST PARACHUTE OPENING LOADS AND TAGGED BY A352 FOR BONDED
JOINTS.** It is the only thing in this repository standing between an aerospike sweep and the
fatigue-crack-closure literature, **which shares both of its words with this nozzle's central flow
feature**. `wind-energy`, earned by A341 and A347 against rotor aerodynamics, is what refuses the
wind-turbine thrust coefficient. **Check what the armed families are protecting before opening any of
them, because the reason a pattern exists is not always the reason it is load-bearing.**

**AND `ramjet` WAS LEFT ARMED ON EVIDENCE RATHER THAN ON ITS NAME.** It releases 134 records of which
A360's gate admits 75, and **28 of those 75 land in a nozzle cluster and every one is the exhaust
nozzle of an air-breathing engine**, being a single expansion ramp on a hypersonic afterbody. That is
external expansion and it is not altitude compensation. **This vehicle has no inlet.** The cost is
stated in the Source Base rather than hidden.

### Earned in A359, and the theme is that a rule you write down is not a rule you follow

**`pgrep -f <PATTERN>` MATCHES THE WAITING SHELL'S OWN COMMAND LINE, AND THIS COST SIX SHELLS IN ONE
SESSION.** An `until ! pgrep -f "a359/harvest3.py"; do sleep; done` loop contains the string it is
searching for, so it matches itself and can never terminate. **Two shells sat in that loop for over
an hour**, one of them after its real work had already succeeded. **The rule was diagnosed, written
into `REVERSE_PROMPT.md` and `TASKLOG.md`, and then broken four more times in the same session.**

**THE RULE AS FIRST WRITTEN NAMED THE SYMPTOM AND NOT THE HABIT.** The correct form is used twice in
the same session and works both times, being `until grep -q "^WROTE " <log>` and `until grep -q
"FULL DONE" <log>`. **The reason for the relapse is that those two scripts printed a completion
marker and the others did not**, so the fallback was reached for whenever there was nothing to grep
for. **If a long job has no completion marker, give it one.** Do not reach for `pgrep`.

**AND A WAIT CONDITION THAT CANNOT TELL YOUR PROCESS FROM ANOTHER SESSION'S IS THE SAME DEFECT.** A
loop watching for `jekyll build` to disappear was watching the concurrent session's `_check.sh`,
while this article's own build had finished in seventeen seconds.

**A SECOND SESSION MAY BE WRITING THE SAME SHARED FILES AND `git add -A` WILL SWEEP UP ITS WORK.**
A359 met this for the whole of three passes. **`TASKLOG.md` and `draft_summary.md` are append-and-edit
files that two sessions can interleave in, and `REVERSE_PROMPT.md` is single-writer by design.**
The resolution used was to stage this article's own paths explicitly, to insert the new history row
BELOW the other session's rather than above it, and **to say in the commit message that the other
session's interleaved text rides along because separating it would destroy it.** Nothing was lost.
**Check `git status` before every commit.**

**A NUMERIC VERIFIER CANNOT SEE A MISSING UNIT.** A359 shipped `the weaker one for the last 4.48`
into three passes. **Every numeric check passed**, because the value was correct, rendered
correctly and appeared exactly as often as the frozen list expected. **A unit is not a number and
nothing in the suite was looking for one.** The superlative scan found it by accident.

**A DECISION RECORDED IN THE PROCESS FILES IS NOT A DECISION IN THE ARTICLE.** The equation pass
declined to use the phase-delay parameter of the bandwidth criterion and wrote that into
`TASKLOG.md` and `REVERSE_PROMPT.md`. **It never reached the page.** The publication review found it
by reading the closing sections against the process files, **which is the only check that would
have.** Do that comparison at every pass after the first.

**AND THE REASON FOR THE REFUSAL IS ITSELF A RULE.** Deriving the phase-delay parameter for a pure
delay from the definition as recalled gave half the delay, where the usual summary of the subject
says it is the delay. **A factor of two is not a rounding**, and the specification that settles it
had not been read. **A formula reached for from memory is not a citation.** The article derived the
phase margin it could and said why the other is absent.

**WALK A CONFERENCE'S OWN NUMBERING.** A thematic sweep found four of the programme's eight papers.
**Resolving every identifier in two contiguous ranges found all eight**, in two blocks of four, and
the four the sweep missed are the ones whose titles name the SYSTEMS rather than the aeroplane.
This is A356's lesson fired again, and that article's programme published no index where this one
published a session. **The same walk turned up a correction notice on one of the eight.**

**AND SEARCH THE DEFENCE REGISTRY FOR THE CURRICULUM, NOT ONLY FOR THE RESEARCH.** The United
States Air Force Test Pilot School publishes its own flying-qualities textbook chapter by chapter
into that registry. **Chapter 16 is a reprint of NASA Technical Note D-5153**, which is the paper
defining the Cooper-Harper scale. **It was the best citation of the primary pass and it was found by
a question about specifications rather than by looking for it.**

**CHECK WHETHER THE REGISTRY CARRIES AN ABSTRACT BEFORE REFUSING TO QUOTE A PAPER.** An abstract is
published metadata that may legitimately be read and quoted, and Crossref carries one for a great
many works. **It carries none for any of the eight session papers**, nor for the aeroplane's 1984
and 1988 founding papers, so the refusal became a measured limit rather than a scruple.

**A THIN PRIMARY FRACTION MAY BE A FACT ABOUT WHERE A DISCIPLINE PUBLISHES, AND THE TEST IS THE
NEIGHBOURING CLUSTER.** A359's keystone sat at 4.0 percent report primaries against the article's
10.2. **No single venue holds more than 4.8 percent of it**, so model following is a dispersed
conference and journal literature. **The aeronautical half of the same subject sat at 16.8 percent**,
and that contrast is what makes the claim a measurement rather than an excuse.

**THE TWO REGISTRIES ARE LIMITED IN DIFFERENT WAYS AND A SWEEP SHOULD LOG WHICH.** A359's fourth
sweep printed its per-question yield. **All 42 defence-registry questions returned exactly 200
rows**, so the binding constraint there is entirely the number of questions. **The reports server
saturated on 60.8 percent and averaged 7.29 against a cap of 10**, and the two questions in five
that came back under the cap are the only evidence that any part of the sweep reached the bottom of
anything. **The earlier three sweeps printed a running total where the fourth printed an
increment**, and parsing them alike gave three hundred records per question against a cap of ten.
**An impossible number is the clearest sign that a parser is reading the wrong column.**

**A NEGATIVE LOOKAHEAD GUARDING ONE CLAUSE LEAVES THE SIBLING CLAUSE ARMED, FOR THE THIRD TIME.**
A359's `terrain following` guard was applied to the model-following clauses and not to the
model-reference-adaptive one. **In that instance the record it admitted was genuinely on subject**,
because the title independently named model reference adaptive control, so the gate was left as it
was and the reasoning recorded. **Read what the unguarded clause admits before widening or
narrowing it.**

**AN OMNIBUS PROCEEDINGS VOLUME IS A LIST OF SUBJECTS AND NOT A SUBJECT.** One conference prints
each year as `Volume 2, Aircraft Engine, Marine, Microturbines and Small Turbomachinery, Oil and Gas
Applications`, and that container name alone deleted a paper on integrated flight and propulsion
control from an article about flight control. **This is A354's multi-modal venue defect in a
different family** and the guard has the same shape. **137 records in that pool were dropped by the
container alone with a clean title**, most of them correctly, including a paper titled `Dogfight in
the clouds` published in a volume on British archaeology in the Middle East. **The container filter
earns its place and needs guarding, which are not in tension.**

**AND A STORE ENTRY CAN SPAN TWO FAMILIES WHERE ONLY ONE IS THE ARTICLE'S SUBJECT.** A348's
biomedical entry alternated ten terms and exactly one of them, the stem `physiolog`, names the
discipline that measures a pilot. **Opening `medicine` wholesale would have readmitted
thirty-eight records on artificial intelligence in clinical trials**, so the alternative was split
into its own tagged entry on the A352 precedent. **The medical remainder the split releases carries
no aeronautical anchor and the gate refuses it downstream**, which is where the division of labour
between store and gate is supposed to fall.

**A MACRO ALLOWLIST THAT REJECTS VALID INPUT TRAINS ITS AUTHOR TO WIDEN IT WITHOUT LOOKING.**
A359's rejected `iff`, `ll`, `ne` and `simeq`, all of which are base TeX. **The list exists to
catch a macro MathJax does NOT provide**, because an unknown macro renders as red text and fails
nothing, **and a list that cries wolf is worse than a short one.**

**THE SYMBOL SCANNER'S OPERATOR LIST IS ARTICLE-DEPENDENT AND MUST BE READ AS SUCH.** A359 added
`det` and `dot`, because `\det` left a `d` after the declared `E`, `t` and `e` had eaten the rest,
and `\dot{x}` left a `do` the same way. **`dot` is only safe while no symbol NAME contains it**,
which A359's table satisfied and an article declaring `\dot{h}` would not. **`bar` stayed out**,
because `\bar{c}` was a declared name.

**AND A SYMBOL NAME MAY NOT CONTAIN A MACRO THE SCANNER STRIPS, WHICH IS A358'S RULE MET AGAIN.**
A359 first wrote an amplitude as `\mathcal{a}`. The scanner removes `\mathcal` as an operator before
it looks for declared symbols, so the declaration never matched, the braces fell away and a bare `a`
was reported undeclared. **The amplitude became a hatted delta.**

**A GUARD AGAINST A PARTIAL NUMERIC MATCH MUST NOT REJECT A FULL STOP.** A359's first occurrence
scan wrote the trailing guard as a bare `(?![\d,.])`, which refuses any occurrence at the end of a
sentence, **and a value that appears three times was reported as appearing none.** Reject a
following DIGIT, or a comma or point that is itself followed by a digit, and nothing else.

**AND THE FROZEN OCCURRENCE LIST MUST REFUSE TO DECAY.** A359 holds 104 values at their measured
counts and **asserts that every unambiguous value reaching the page is in the list**, so a value
added by a later pass cannot be silently unguarded. **Values of two digits or fewer are excluded and
the reason is written down**, because a `4` cannot be located in a hundred thousand words and a
check that counts every incidental four measures nothing.

**A RE-PARSE FINDS ITS OWN DEFECTS FIRST AND THAT IS THE POINT OF IT.** A359's verifier re-parses
the saved register HTML rather than re-reading the parsed JSON. **Written as a bare `<tr>` it
matched 512 of 539 rows and missed exactly the 27 that carry a class**, which are the wholly
unofficial and unconfirmed ones. **The omission was invisible as a parse failure and visible only
as a disagreement with the other parser.**

**AND A CONTRACT RECORD IS A THIRD KIND OF OBJECT AGAIN.** A357 found money that outlived its
publicity, A358 found the inverse, and **A359 found an operating account rather than a development
programme**, obligated in calendar-year increments to two contractors for twelve years. **It
answers what an instrument costs to own**, which neither of the other two could ask. **The
whole-record average conceals the step and is the figure a reader computes first**, so the article
reported it alongside the step rather than instead of it.

### Earned in A358, and the theme is that the thing you did not guard is the thing that bites

**WRITE THE RELATION DOWN. IT WITHDREW THIS ARTICLE'S BEST FRAMING AND THAT IS NINETEEN ARTICLES
RUNNING.** A358's draft called the towed docking device the end of a resonator and left its aerodynamic
damping as an adjective, saying a cable has a great deal of it. **An adjective is not a quantity.**
Linearising the damping about the equilibrium inclination gives a modal damping ratio of 0.324 on the
fundamental, which decays by a factor of e in 0.49 of a cycle. **It does not ring, and the word was
withdrawn.** What survived was the half the argument actually used, which is that the loop still cannot
reject motion at those frequencies whatever produces it.

**A DIFFERENCE THAT LOOKS LIKE A CONVENTION MAY BE STRUCTURAL, AND THE TEST IS AN IDENTITY.** A358
found two standard forms of a second-order position loop giving opposite answers about whether the loop
amplifies its target's motion, and called the difference a convention it had no information about.
**It is a difference of relative degree.** The minor-loop form's Bode sensitivity integral converges to
zero and the forward-path form's is finite, equal to minus half pi times the high-frequency loop gain
to four figures. **The convergence is the evidence rather than either value**, so the residual was
computed at three upper limits and required to halve as the limit doubled.

**AND THE ARCHITECTURE THAT ESCAPES A CONSTRAINT PAYS FOR IT SOMEWHERE.** The form that avoids
amplification passes 140 times more high-frequency noise. **Find the price before reporting the escape.**

**A NUMERICAL INTEGRAL OF AN IDENTITY MUST BE CHECKED BY ITS CONVERGENCE AND NOT BY ITS VALUE**, and a
uniform quadrature cannot do it. A358's verifier reported the Bode residual failing to halve, which was
the integration and not the identity, because the integrand concentrates near one frequency and decays
as the inverse square beyond it. **A logarithmic grid fixes it and is a genuinely different rule from
the calculation's**, which is what makes it an independent check.

**A PRESENCE CHECK CANNOT SEE ONE OF SEVERAL OCCURRENCES GOING STALE, AND THIS HAS NOW BITEN TWICE IN
ONE ARTICLE.** Eight of A358's first in-text checks passed while a value had been corrupted, because
the corruption hit the first occurrence and the check needed only one to survive. **The count is the
check.** The equation pass fixed that for numbers and did not notice it had a twin, so the phrase guard
went on using presence and the injection suite caught it two passes later at 135 of 136. **Hold the
expected number of occurrences, for a digit and for a sentence alike.**

**A NUMERIC VERIFIER CANNOT CATCH A CLAIM THAT CONTAINS NO NUMBER.** The suite proved it by turning
`the most favourable value` into `the least favourable value` with nothing firing. **A358 holds
twenty-one load-bearing formulations that carry no digits, by their exact wording and by their count.**
It is a regression guard and not a test of truth, and a deliberate rewording must change the list,
which is the point.

**THE HOMONYMS YOU GUARD ARE NOT THE HOMONYMS THAT BITE YOU, FOR THE SECOND ARTICLE RUNNING.** A358
measured `gremlin`, `retrieval`, `parasite`, `formation`, `capture`, `swarm` and `bullet` against the
registry before its first sweep and **not one produced a contaminant**, because none was ever queried
bare. **What got through were a grey partridge, a desert locust, the coronavirus and molecular
docking.** `Perdix` is a micro air vehicle and `Perdix perdix` is the bird, in five languages. `LOCUST`
is a tube-launched swarming programme and locust SWARMING is the insect literature's own central word,
so the one qualifier a careful author would add is the one that admits it. `Corona` reached the pool
through the word `recovery`. **Guard the foreseeable ones anyway, then read the kept sample, because
only reading finds the rest.**

**AND A HOMONYM THE TABLE HAS NAMED FOR YEARS MAY STILL HAVE NO PATTERN.** Molecular docking has been
in this handoff's homonym table since A334 and no store entry had ever been written, because no article
needed the word until one whose entire subject is docking. **Sixty-six records reached the
relative-navigation cluster**, being pancreatic adenocarcinoma, dopamine receptors, androgenetic
alopecia, kidney stones and the taste mechanism of umami peptides. **A qualifier list cannot separate
them**, because `docking and molecular dynamics` is one of computational chemistry's commonest
collocations and satisfies any qualifier an aerospace gate would reach for. **Require a companion from
the other field rather than excluding one from your own.**

**AND `git status --porcelain` PREFIXES AN UNSTAGED MODIFICATION WITH A SPACE, WHICH `.strip()`
EATS. THIS HAS NOW BROKEN THREE CONSECUTIVE HANDOFF SELF-CHECKS.** The comparison fails on whitespace
and reports a clean tree as dirty, which looks like a real finding for about a minute. **Compare
`splitlines()` against a list, or keep the leading space in the expected string.**

**A NEGATIVE LOOKAHEAD MUST BE ANCHORED OR IT DOES NOTHING.** `re.search` tries every starting
position, so an unanchored `(?!...)` succeeds somewhere past the phrase it was written to refuse and the
pattern matches as though the guard were absent. **A358's first internal-homonym guard reported no
change on nine test titles and looked correct on a clean corpus.** The `\A` is the whole of the fix.

**AND `recovery` IS AN INTERNAL HOMONYM, WHICH IS THE MOST DANGEROUS KIND.** Recovery from a spin, an
upset or a stall is aeronautics itself, so it was excluded in the article's own cluster ordering rather
than in the shared store. **A seeded sample of twenty-two keystone records found five and nothing else
would have.**

**A PLURAL BOUNDARY FAILS SILENTLY AND THAT IS FIVE TIMES NOW.** A358's first molecular-docking pattern
wrote its companions as whole words and `inhibitor` then refused `inhibitors`. **Separate WORDS, which
keep both boundaries, from STEMS, which keep only the leading one.**

**A MODULE IN THE WORKING DIRECTORY SHADOWS THE STANDARD LIBRARY, AND THE FAILURE SURFACES SOMEWHERE
ELSE.** A358 named a file `numbers.py`, which `fractions` imports and `statistics` imports in turn, and
the emitter died with `module numbers has no attribute Rational` from a file that had nothing to do with
fractions. **Do not name a payload module after a standard library module.**

**THE DUPLICATE-SYMBOL REFUSAL EARNS ITS PLACE EVERY TIME.** A358 redeclared `z` as altitude when it was
already the depth below the vortex plane. **A dictionary literal would have accepted the second
declaration in silence and the symbol table would have shown one meaning while another section used the
other.** Declare symbols as a LIST OF PAIRS and raise on a repeat.

**AND THE SYMBOL SCANNER'S OWN DOCSTRING WARNS AGAINST `\text{}` INSIDE A SYMBOL NAME**, which A358 did
anyway. Written `\sigma_{w, \text{band}}` the subscript decayed before the symbol was matched, the
declared `\sigma_w` no longer matched it, and the bare `\sigma` was eaten letter by letter by the
declared s, g, m and a, leaving an undeclared `i`. **Give the quantity its own plain symbol.**

**A TOLERANCE SET FROM HABIT FAILS ON A FIGURE THAT IS RIGHT.** A358 solved a break-even forwards
through a value rounded to two decimals and demanded agreement to one dollar. **Derive the tolerance
from the rounding**, or from the quantity's own sensitivity, and never from a round number.

**AN EQUATION PASS PROMOTES SUBJECTS AND THE REFERENCE BASE MUST FOLLOW. ELEVEN ARTICLES RUNNING.**
A358's equation pass promoted the drag polar, feedback design limitations, the phase a transport delay
costs, aerodynamic damping of a cable and attrition modelling, all measuring between 26 and 46 records
in a pool of nearly six thousand. **A third sweep in those five vocabularies took them to between 90 and
539**, and the audit was run before that sweep rather than after it.

**THE REPORTS SERVER IS QUERY-LIMITED AND THE DEFENCE REGISTRY IS CEILING-LIMITED, AND THE REMEDY
DIFFERS.** A358's first three sweeps asked 161 NASA questions and got 6.1 records each against a cap of
ten, so the limit was the number of questions. Forty defence-registry queries returned 156 records each
with the four most productive hitting the two hundred row ceiling exactly. **A fourth sweep of 146
narrow reports-server questions and 40 registry ones took report primaries from 814 to 1,155 and their
share from 12.0 percent to 16.2.**

**A THIN PRIMARY FRACTION MAY BE A FACT ABOUT WHERE THE WORK WAS PUBLISHED.** Every cluster's primary
fraction rose except A358's keystone, which moved from 11.1 to 11.2 percent. **The publisher composition
says why**, at 24.1 percent from one aeronautical society and 18.1 percent from one engineering
institute against 11.2 percent from the two agency report servers. The subject was published at
conferences. **Report the composition rather than the shortfall.**

**THE CONTRACT RECORD IS A DIFFERENT RECORD FROM THE PUBLICITY AND IT IS WORTH READING TWICE NOW.**
A357 found a programme whose money outlived its publicity by three years. A358 found the inverse, money
stopping 47 days after the last flight while the period of performance ran on another 1,463 days on
zero-dollar modifications. **A contract that is open and unfunded is a different object from one that is
quietly spending.** Both were found by summing transactions rather than by reading a press release, and
both totals reconcile to the cent against the figure the registry states separately.

**AND THE EARLIEST DOCUMENT MAY PREDATE THE PROGRAMME AND CORRECT AN ATTRIBUTION.** A358 credited
`aircraft carriers in the sky` to a 2017 release. It is from a Request for Information of November 2014,
which also named the carrier by type, capped the payload at a figure the built vehicle exceeded by 1.45
times, and asked for a full-system flight demonstration within four years. **A stated duration is rare
and can be measured**, and the outcome came at 1.74 times it.

**SEVEN SENTENCES OF DRAFTING HISTORY REACHED THE PUBLICATION REVIEW, WHICH IS MORE THAN A322 OR A323
SHIPPED.** They arose because three passes each withdrew a claim and named it, which is this series'
convention. **Naming a withdrawn claim is epistemic content and naming the draft that made it is
revision history.** The test is whether the sentence still works for a reader who has never seen a
previous version. `It is tempting to stop there and call it a resonator` passes; `The draft of this
section stopped there` does not.

**A SUPERLATIVE SCAN OVER THE AUTHOR PROSE IS CHEAP AND FOUND THREE BARE RANKINGS.** A358 called one
sentence `the only public statement` of a tolerance, which is a claim about a record it had searched
part of. It said span is `the only way` to buy an efficiency where the relation it had just displayed
offers two levers. And it asserted a historical first belonging to two interested parties. **Scan for
`the only`, `the best`, `never` and `every` and make each one earn its place.**

**THE CLOSING SECTIONS OUTRUN THE LATER PASSES AND NOTHING WARNS YOU.** A358's Epistemic State still
listed the sharp-edged gust as the crudest available model two passes after the spectrum had vindicated
it. **A withdrawn assumption still asserted in the epistemic state is A333's defect exactly.** Re-read
What Is Assumed, What the Record Does Not Settle, What the Data Changed and the Conclusion at every pass
after the first, because they are written early and never fail a check.

**AND A STATISTIC CAN GO STALE INSIDE A SINGLE PASS.** A358 typed the keystone's publisher composition
as literals and a gate change later in the same pass moved the cluster by four records. **Worse, the
body and the source base computed the same quantity on different denominators**, one from the gated set
and one from the cited set, so the article carried two percentages for one thing. **Derive both, and
hold each at its occurrence count so they cannot drift apart again.**

**A DATELINE HORIZON CHECK MUST EXCLUDE BIBLIOGRAPHIC YEARS OR IT FIRES ON THE WRONG THING.** A358's
found 2026 in citation labels and in the survey's own year range. **A publication year carried by the
registry is not a claim the article makes**, so strip citations first, and exclude the survey's range by
name with the reason written down rather than hidden.

### Earned in A357, and the theme is that a measurement can be right and mean nothing

**THE LARGEST FINDING OF A357 IS THAT THREE OF ITS OWN PASSES WERE BUILT ON A MISDIAGNOSIS.** Read
this first, because it is the one most likely to repeat.

**A COST CURVE FITTED TO ONE VARIABLE PROVES NOTHING ABOUT THAT VARIABLE.** A357 timed the markdown
processor against its reference count, found 0.43 seconds at 500 definitions, 8.8 at 2,000 and 103.36
at 4,500, and concluded the cost went as the cube of the count. It imposed a citation budget, refitted
the exponent to 4.83 when a build overran, and cut the budget again. **Every timing was real.** The
cost was in an unescaped square bracket around every inline citation, which makes the processor attempt
to parse a link inside a link and backtrack once per citation.

**THE SERIES CITATION FORM `[[text][anchor]]` COSTS 226 SECONDS WHERE `\[[text][anchor]\]` COSTS
0.70**, on the same content, with rendered output identical to the byte. **Escape the outer brackets.**
Two controls separate the explanations, and run both before believing either. Wrapping the long lines
with the brackets left alone gave 196.49 seconds, a thirteen percent gain, which rules out line length.
Removing the brackets entirely gave 0.63, matching the escaped form, which isolates the brackets.

**MEASURE THE BUILD THE DEPLOY RUNS, NOT A STUB.** Three passes timed a 96-page stub site. The deploy
builds 301 posts. **The whole corpus builds in 12.8 seconds**, and it always did, including a published
post carrying 13,803 reference definitions and 27,584 citations. That post writes its references one to
a list item and never pays the backtracking. **The counter-example was in the repository the whole
time and no model fitted to one article's own numbers was ever going to find it.** `tmp/a357/full_build.sh`
is the script that measures the real thing, and it is worth copying forward.

**A CHECK CAN BE RIGHT ABOUT THE WRONG THING.** Every budget check A357 wrote passed, on every run, for
three passes. They verified an apparatus that should not have existed.

**ONE SAMPLE IS NOT A MEASUREMENT.** The same article at the same reference count built in 275.1
seconds and then 305.0, an eleven percent spread on an identical input. Report both. Reporting only the
faster is choosing the favourable sample, which is the same failure as quoting the model that agreed
and not the one that did not.

**ADDING PROSE WITHOUT ADDING CHECKS IS THE DEFECT THIS ARTICLE COMMITTED FOUR TIMES.** The injection
suite caught it every time and nothing else ever did, at 78 of 92, 59 of 76, 92 of 96 and 98 of 100.
**Write the check when you write the sentence**, and run the suite after every pass rather than at the
end.

**A BARE PRESENCE CHECK CANNOT HOLD A SMALL NUMBER.** A355 established it and A357 violated it three
separate times. `2.18` occurs five times in A357, four of them inside digital object identifiers, so
`ok("2.18" in text)` passes while the equation says something else. **Anchor every number on
distinctive neighbouring text**, and make the anchor specific. `to`, `which is`, `asked` and `carries`
all matched everywhere and produced failures about the stem rather than about the number.

**A CHECK THAT INSPECTS A SUBSET OF ITS SUBJECT REPORTS A CLEAN SUBSET.** Three instances in one
article. The assembler's placement assertion scanned the body and not the emitted blocks. A353's
block-slot assertion checked what precedes a slot and not what follows it, so a relation glued to the
front of a sentence passed and produced an unclosed display fence. And `verify_ids.py` checked a
hand-picked list of addresses rather than all of them, which is how a dead link survived two passes.
**All three now scan everything.**

**AN ODD FENCE COUNT IS AN UNCLOSED DISPLAY AND INTEGER DIVISION HIDES IT.** Assert the parity before
believing the count.

**A CURRENCY DOLLAR SIGN IS AN INLINE MATH DELIMITER ON A MATHJAX PAGE.** A357 shipped 26 of them in
its first assembly. Write amounts as a number followed by the word dollars. The linter reports it as a
bold span crossing a line break, which is the symptom and not the cause.

**DO NOT RUN THE STUB BUILDER, `_verify.py`, OR ANY OTHER CHECK AGAINST THE ARTICLE WHILE THE INJECTION
SUITE HOLDS IT.** A357 did both, building for four and a half minutes against possibly injected bytes
and reporting a phantom em-dash from an injected defect. `make_stub.sh` now refuses while
`inject.lock` exists. **Run the suite and the build in sequence, never beside each other.**

**A `cd` THAT FAILS SILENTLY SKIPS THE EDIT BEHIND IT.** `cd tmp/a357 && python3 - <<PY` short-circuits
when the working directory is already there, the heredoc never runs, and `str.replace` on a missing
target writes nothing and says nothing. **Assert that an edit's target exists before replacing it**,
which caught five undefined citations that would otherwise have shipped.

**A HAND-TYPED COMPARISON TO AN EARLIER PASS IS A STALE NUMBER WITH A LONGER FUSE.** A357 wrote `13.3
percent of 10,754` into its emitter as a literal. `pass_history.json` now carries each pass's measured
figures and the emitter reads the last one, and the file carries the current pass under `current` for
the next to promote.

**A PROBE WRITTEN BEFORE THE CONCLUSIONS EXIST DOES NOT COVER THEM.** A356 found this and A357 repeated
it, adding two conclusions in the equation pass that the probe never saw. **Re-read the probe against
the finished Conclusion in the publication review.**

**AND SAY WHICH CONCLUSIONS YOUR OWN SURVEY DOES NOT SUPPORT.** A357's statutory suborbital test rests
on two-body orbital mechanics and its pool holds 4 records on it, because the gate excludes
astrodynamics deliberately. **A gate that excludes a subject has not measured it**, and a reader should
not have to infer from a citation count that a question is unstudied.

**THE HOMONYMS YOU GUARD ARE NOT THE HOMONYMS THAT BITE YOU.** A357 guarded Hadley, Ursa Major,
Gulfstream and orbit before its first sweep and **none of the four produced a contaminant**. The record
that got through was Sandia's PEGASUS pulsed-power machine, whose flyer plates are called booster
projectiles, so the title carried launch vocabulary in every position. **Guard the foreseeable ones
anyway and then read the kept sample**, because only reading finds the rest.

**AN ORDER-DEPENDENT DISCRIMINATOR IS NOT A DISCRIMINATOR.** The first PEGASUS pattern was a bounded
lookahead after the name and missed the very record that produced it, because the name is that title's
last word.

### Earned in A356, and the theme is that a check can be abandoned rather than absent

**A PROGRAMME HAS TWO PUBLISHERS AND THIS CORPUS HAD BEEN READING ONE OF THEM.** The draft's epistemic
state recorded the aeroplane's weight as not stated in any source consulted. **It was stated by the
company that built it**, on a product card carrying the gross weight, the empty weight, the fuel, the
payload, an overall length and the engine. **Every relation needing a weight became evaluable**, and
the range relation's three unknowns collapsed to one. Look for the prime contractor's own literature
before recording a quantity as unpublished.

**A THEMATIC SWEEP AND A NAME SWEEP ARE DIFFERENT INSTRUMENTS.** After four thematic sweeps a
ten-question probe by bare programme name returned sixty-six records of which **twenty-eight were not
in a pool of sixteen thousand**, eleven squarely on subject. **That is A353's lesson stated the other
way round.** A designation beside generic words is diluted by them, and the corollary nobody had drawn
is that the designation alone finds what the designation beside words does not.

**A METHOD RULE CAN RETURN A NEGATIVE AND THE NEGATIVE IS WORTH FIVE MINUTES.** A354 established that a
programme's own published index recovers what a thematic sweep does not. **This programme publishes
none**, its project page carrying an editor's note that the project has concluded. Establishing that
cost nothing and it is recorded so the next agent does not hunt for one either.

**A DECLARED EQUATION THAT IS NEVER PLACED IS SILENTLY DROPPED.** The module declared 28 relations, the
body placed 27, the substitution reported nothing missing because nothing in the body was unfilled, and
the symbol checker passed because it reads the DECLARATION rather than the article. **Only the
assembler's own summary line noticed, and only because a human compared it.** The assembler now refuses
an unplaced or a duplicated equation.

**A COUNT IS NOT AN IDENTITY.** The symbol table was checked for the right number of rows, so an
injection that renamed one symbol was missed. It is now checked as a set.

**A VERIFIER THAT CANNOT READ A DECIMAL POINT REPORTS TWELVE CORRECT NUMBERS AS WRONG.** The inherited
occurrence check stopped its capture at the full stop, which was harmless for A355's integers.
**And some sentences put the number first**, so a rightward-only check reports a correct figure absent;
there is now a leftward sibling.

**AN ARTICLE'S OWN CENTRAL QUANTITY IS THE MOST DANGEROUS BARE ANCHOR.** `rise time` was written bare
precisely because it is what the article is about, and it admitted a surface-acoustic-wave resonator,
partial discharge under square-wave voltage, a Kerr cell, a klystron and chlorophyll absorption.

**A PLACE NAME DELETES THE MEASUREMENT LITERATURE.** The `missiles` family was removing the White Sands
Missile Range sonic boom propagation experiment. **A missile range is where a boom is measured.**

**A PARTS-CATALOGUE FILTER REFUSES REPORT TITLES.** The inherited rule refused any all-capitals title
with three or more comma-separated fields, the shape of `SCREW, MACHINE, ROUND HEAD`. **It is also the
shape of a 1962 defence report**, because the registry typesets its older records in capitals and their
titles name a place and a year. It was removing a foundational community study while keeping a
lower-case registration of the same work. **The discriminator is terseness, not capitalisation.**

**THREE COPIES OF ONE RULE ARE THREE PLACES TO BE WRONG**, and they disagree the moment one is
repaired. That filter lived in three files and now lives in the gate module and is imported.

**THE EMITTED BLOCKS ARE A FUNCTION OF THE EMITTER AND REASSEMBLY DOES NOT SEE IT.** A patch script
asserted partway through, discarded its own earlier edit, and the emitter was never re-run. **The
article carried a false claim in its source base and the correction of that claim in its epistemic
state, at the same time, and reassembly passed because the article was a faithful assembly of a stale
block.** The verifier now re-runs the emitter and compares its output first.

**A NUMERIC VERIFIER CANNOT CHECK A CLAIM THAT CONTAINS NO NUMBER.** The injection suite proved it by
reverting two prose corrections without a single check going red. **The answer is a guarded list of
withdrawn formulations**, which is a regression guard and not a test of truth and must be labelled as
one. **It has to exclude the section that names the corrections**, because this series names a
retracted claim rather than deleting it. **Writing that list found two more live overreaches that three
passes of reading had missed.**

**THE PROBE IS WRITTEN IN PASS ONE AND LATER PASSES ADD CONCLUSIONS.** Four of A356's fourteen
conclusions had never been probed at all. **That is A349's defect from the other direction**, a
conclusion written before half the findings exist becoming a probe written before half the conclusions
exist. Go back to the probe in every pass that adds a claim.

**LOSING A CHECK MAKES IT SILENT RATHER THAN FAILING.** The corpus survey-row gate reads a line
beginning with the count in bold; thirteen articles used that format and four then stopped, and nobody
noticed because the check simply had nothing to read. **Ask of any check whether it is passing or
merely not being fed.**

**THE SIGN OF THE RELEASE DIFFERENCE HAS MEANING.** A353 and A354 found the single-family releases
summing to more than the joint release. **A356 found the opposite**, because a record held by patterns
from two different families is released only when both are open. With many families open the whole
exceeds the sum of its parts.

**A PDF IS NOT ITS OWN TEXT, AND A SITE CAN REFUSE BY SERVING A STUB.** The regulations site answers
this corpus's fetching library with ten kilobytes of navigation chrome for a section that is eighty in
a browser, and the quoted clause is not in the ten. **An HTTP 200 with a plausible body defeats both a
status check and a naive content check.** Retry with a browser user agent, save the text, quote from
the saved copy, and check the copy against the live page.

**A PREAMBLE IS A PRIMARY DOCUMENT AND A REGULATION IS NOT THE WHOLE OF IT.** The draft read the rule
and not the rulemaking, which is the difference between knowing what a rule says and knowing what its
author thinks it means. The Federal Register's API and full-text endpoint both work and are listed
below.


### Earned in A355, and the theme is that an instrument fails at the edge of its own vocabulary

**A PROPER NOUN WITH NO CONTEXT REQUIREMENT IS NOT AN ANCHOR, IT IS A TRAWL.** A bare `Valkyrie`
admitted 74 records of which one had the subject beside it. **The X-57 met the same effect through a
physicist's surname and recorded it in its STORE notes**, and A355 carried the lesson into its store
and not into its GATE. **That is the shape of a lesson learned in the wrong place**, and it survived a
whole draft pass. Guard a vehicle name with a vehicle word, in the gate, from the first run.

**A PLURAL WILL DEFEAT AN INSTRUMENT AND IT WILL DO IT TWICE.** `\bUAV\b` does not match `UAVs`, and it
refused 24 records including the loyal wingman concept in a title. **A guard later written against
`launch vehicle` did not match `launch vehicles`** and let the thing it was written for walk through.
**Write `s?` into every anchor and every guard.**

**A HOMONYM IS NOT A BROADER CASE OF THE SUBJECT.** `expendable` in aerospace overwhelmingly means a
rocket that is not reused, `attrition` in the defence registry usually means personnel turnover, and
`force` appears in so many titles that as a context term it guards nothing. **But `Personnel Attrition
Rates in Historical Land Combat Operations` IS the subject**, so cut by the vocabulary of the wrong
sense rather than by the word the two senses share.

**A METHOD THE ARTICLE USES BRINGS ITS LITERATURE WITH IT.** A paper on the microwave oven learning
curve was deliberately kept, because the article applies the learning curve. That is the X-52
precedent, and it is the opposite decision from the homonym rule above. **The test is whether the
record is about the same THING or about the same METHOD.**

**A SMALL INTEGER CANNOT BE CHECKED BY PRESENCE.** In a document full of numbers, `15`, `4` and `0.2`
appear everywhere, so a check asking whether the article contains the computed value passes on any
other occurrence. **Five figures escaped injections for this reason and were closed with
per-occurrence checks anchored on distinctive stems.** State a fraction as a percentage when you can,
because `20 percent` is checkable and `0.2` is not.

**A PRESENCE CHECK IS SATISFIED BY A SECOND COPY, AND THE ANSWER IS A TOTAL CHECK.** The article is a
pure function of its body, its computed numbers and its reference data, so **reassembling it and
comparing byte for byte catches any alteration**. That check found two live corruptions of the working
draft that nothing else saw. **But a check that cannot fail selectively is not evidence about the
instruments beside it**, so the injection suite disarms it and each defect must be caught by the
instrument aimed at it.

**RESTORE BY REASSEMBLY, NEVER BY COPYING BACK A FILE.** A killed injection run left the article
modified, and every run afterwards copied that corruption into its own backup and restored it
faithfully. **A copy can be poisoned. An assembly cannot.**

**A NUMBER A SECTION STATES ABOUT ITS OWN INSTRUMENT IS AS PERISHABLE AS ONE ABOUT THE WORLD.** Five
Source Base measurements were typed from a console and went stale when the gate was corrected twice.
**And two numbers that were correctly emitted were still wrong in their prose**, a capitalisation
helper writing `Three Sweeps` and a subtraction reporting a negative fall as a fall. **Emission is a
defence against staleness and not against being wrong.**

**TWO INSTRUMENTS MEASURING ONE THING MUST BE MADE TO AGREE BEFORE EITHER IS QUOTED.** Equation
citation coverage came out 36 of 40 on the body and 32 of 40 on the finished article, because a
one-line slot becomes a three-line block. **Shipping the larger because it appeared first would have
been the defect.**

**THE SYMBOL TABLE IS AN INSTRUMENT AND NOT DOCUMENTATION.** It refused the first draft of A355's
equation set outright, catching `N` meaning both design life and normal force, `m` meaning both mass
and weapons carried, and `n` meaning four things in four sections. **Do not write `\text{}` inside a
symbol NAME**, because the markup rule strips it before the symbol can match and the stem is then
reported undeclared.

**AN EQUATION ADDED BEFORE IT IS EVALUATED IS DECORATION.** Three of A355's own new relations were
wrong when first computed, being an inverted break-even that returned negative probabilities, a design
life truncated at 1,000 sorties, and an opening load computed on an impossible premise. **The third
was kept, because the arithmetic was right and the premise being impossible was the finding.**

**AND REPORT COVERAGE IS BOUGHT WITH THE NUMBER OF QUERIES.** A355 acted on the X-57's measurement
rather than merely recording it, asking the report server 42 questions after the draft's 12 and taking
its contribution from 16 records to 77. **The ceiling is bought off, never lifted.**


### Earned in A354, and the theme is that an index is not a search result

**A PROGRAMME'S OWN PUBLISHED INDEX MUST BE READ AND CANNOT BE SEARCHED.** NASA publishes a page
listing the X-57 programme's technical output. Sixty-three entries transcribed from it resolved to
sixty-one records, and **the first sweep, which queried the designation alone, had retrieved eleven**.
That is eighteen percent.

**AND THE REASON WAS TESTED, WHICH DISPROVED A HYPOTHESIS ABOUT OUR OWN TOOLING.** A direct query
reports seventy-four matching records and returns ten. Asking for a hundred returns ten. **Asking by
offset returns the same ten again at every offset from ten to seventy.** The suspicion was that
`fetch.ntrs_search` never paginates and was leaving records on the table, which would have been a
defect in every article of this series. **It paginates correctly and the server ignores the offset.**
Look for the programme's own index before building the sweep.

**A VENUE THAT NAMES SEVERAL FIELDS IS EVIDENCE FOR NONE OF THEM.** The store joins the title and the
venue before matching, which is right when a venue carries evidence. The IEEE conference named for
electrical systems in aircraft, railways, ship propulsion and road vehicles is a principal venue for
electric aircraft propulsion, and **its name alone removed 31 records including one titled advanced
aircraft electrical systems to enable an all-electric aircraft**, whose own title contains no marine or
rail word. The marine, rail and road families are now guarded against that construction.

**A FAMILY MUST BE TAGGED BEFORE IT CAN BE OPENED, AND SOME ARE NOT.** The pattern removing the rotor
of an electrical machine was added by A347 for a rotorcraft survey, where it was a contaminant. **For
an electric-aeroplane article it is the subject**, and it carried no tag, so there was no handle. Check
early whether the families your subject will meet are tagged at all.

**A PRESENCE CHECK CAN BE SATISFIED BY A SECOND COPY OF THE SAME SENTENCE.** A353 found that a
presence check cannot tell whether it matched the equation or the prose. **A354 found the next case, a
figure appearing twice in the PROSE**, once where it is derived and once where the article records what
a pass changed. An injection altered one and the other satisfied the check. **Count the stem and
require every occurrence to carry the computed value.**

**A NUMBER SPELLED OUT AS A WORD GOES STALE BESIDE COMPUTED FIGURES THAT DO NOT.** A353's source base
said `the difference is one record` while the two emitted figures beside it had moved to two. **A word
typed next to a number emitted from data is the stalest thing on the page.**

**AND A CONCLUSION MUST NOT RESOLVE BY ASSERTION WHAT THE BODY LEFT AS A BOUNDARY.** A354's equation
pass established that dynamic pressure alone cannot account for landing the wing on the installed
power. **The conclusion said the propellers solved it.** It now carries the boundary. The same review
found the conclusion claiming the aeroplane was not `possible` where the record says only that the
programme ran out of budget and schedule with a redesigned motor in work.

### Earned in A353, and four of them are instruments that condemned good data

**A SUBJECT GATE IS BLIND TO A PROPER NOUN.** The Helios mishap findings, a primary document A353's
argument rests on, were retrieved by the sweep and then refused for carrying no subject anchor, because
the title names a vehicle and an event and no physics at all. **Name the vehicles in the gate
explicitly.** A354's gate did so from the start.

**A BIBLIOGRAPHIC QUERY MIXES ITS TERMS, SO A DESIGNATION BESIDE GENERIC WORDS IS DILUTED BY THEM.**
`X-56 multi utility technology testbed flutter` returned exactly 200 records, which is the row cap, and
brought back a millimetre-wave seeker testbed, a Testbed-12 tile retrieval service and four tiltrotor
whirl-flutter testbeds. **Six records in 6,477 had the aeroplane in their title.** Query every proper
noun alone.

**CLUSTER ASSIGNMENT IS FIRST MATCH WINS, SO LIST ORDER IS A MEASUREMENT DECISION.** A general flutter
pattern placed above a specific flutter-suppression pattern reported the programme's own subject at 19
records where it is 325. **The specific cluster must precede the general one it is a special case of.**

**THE GATE AND THE REFERENCE LIST MUST READ THE SAME STRING.** Forty-five harvested titles carry markup
and only the reference path cleaned it, so records were refused on markup their own pattern cannot see.
**A defect that only ever deletes evidence leaves no trace in the output.**

**A TAG COUNT IS A COUNT OF FIRST REASONS, NOT OF RELEASABLE RECORDS.** Summing the opened families
overstates what opening returns, because some records are held by a second armed pattern. A353 measured
two, A354 measured thirty-one. **Measure the release as a set difference.**

**A DISPLAY EQUATION SUBSTITUTED AT THE END OF A TEXT LINE IS NOT A DISPLAY EQUATION.** Kramdown reads
`$$` that does not begin its own line as inline math. The source declared eight and the built page
carried seven, and only counting the rendered page found it. **The assembler now asserts it.**

**A CHECK MUST NOT MEASURE A POOL IT HAS ITSELF FILLED.** A353's identifier check compared the
hand-found bibliography against the final references, which by then contained the documents curated
because they were missing, and duly reported 100 percent. **Compare against the sweep's own artefact.**

**A NUMBER CORRECTED IN A PASS IS THE NUMBER MOST WORTH PINNING IN THAT PASS.** A353's publication
review changed a flight count from sixteen to eight and did not pin it, and an injection changing it to
nine sailed straight through.


### Earned in A352, and four of them are instruments that reported the data as wrong

**FOUR INSTRUMENTS IN ONE ARTICLE CONDEMNED GOOD DATA, AND THAT IS THE MOST CONSISTENT FINDING OF ITS
WHOLE RHYTHM.** A351's lesson was checkers that passed while something was wrong. **A352's is the
mirror image and it is more dangerous, because a false alarm argues for work that is not needed and
hides work that is.**

- **A MONKEYPATCH MUST PATCH WHAT THE CODE ACTUALLY READS.** The harness written to prove a store test
  non-vacuous replaced `homonyms.NOISE_PATTERNS`, and `noise_hit` iterates `_COMPILED`, which is built
  once at import. **It injected nothing and reported a good test as vacuous.**
- **A DIGITAL OBJECT IDENTIFIER CONTAINS A SLASH.** The check comparing hand-found identifiers against
  the corpus split each address at its last slash, so `10.2514/6.2000-1379` was compared as
  `6.2000-1379` and matched nothing. **It reported that none of thirty-two documents were in a corpus
  that held twenty-six of them**, and that wrong number was reported to the pilot before it was
  checked.
- **A TOLERANCE TIGHTER THAN THE QUOTED PRECISION IS A FALSE ALARM.** A property check held two sweep
  times to their viscosity ratio using the figures the PROSE quotes, and the smaller is quoted to
  three decimal places, which is a five percent rounding on a hundredth of a second. **Hold a property
  to the unrounded values and hold the rounded one to its own rounding, separately.**
- **A SCANNER THAT CANNOT READ ACROSS A LINE BREAK.** The prose-colon check stripped citation labels
  with a regex that stopped at a newline, so a label split over two lines reported as a prose colon.

**A DICT LITERAL ACCEPTS A DUPLICATE KEY SILENTLY, AND THE SYMBOL TABLE WAS A DICT LITERAL.** Ten
symbols had been declared twice and the later declaration simply won. **The whole point of a declared
table is that a second meaning has nowhere to go, and a dict was quietly giving it somewhere.**
Rebuilding it from a list of pairs that raises on a repeat found **five real collisions** in one
article, being `h` for altitude and core separation, `\lambda` for lapse rate and the DiBenedetto
parameter, `\rho` for steel density and the learning ratio, `n` for reaction order and the unit index
and the Prandtl exponent, and `A` for the Arrhenius prefactor and the skin area's stem. **Rename in
the article. Never declare a symbol twice.**

**AND THE TABLE HAS A LIMIT WORTH KNOWING.** It catches an UNDECLARED symbol. **It does not catch a
declared symbol used with a second meaning**, which is how the DiBenedetto lambda slipped past until
the duplicate check was added. The two together are the instrument.

**A METRIC CAN QUIETLY USE THE WRONG COLUMN, WHICH IS THE COUNT-IN-OWN-PROSE DEFECT ONE LEVEL DOWN.**
The sentence reporting how many thin subjects opened `on rewording alone` read the column measured
after three further sweeps, and said six where rewording alone opens four. **Emitting a number from
data is only as honest as the column it is emitted from**, and this is the eighth time the corpus has
paid for that family.

**A CONDITIONAL EXPRESSION INSIDE A DICT LITERAL BINDS THE WHOLE ENTRY, NOT THE VALUE.** A
scientific-notation formatter written as `"K": a if cond else b` would have emitted something
different from what it looked like it emitted. Write the helper and test it.

**A DIMENSIONLESS GROUP IS ONE SYMBOL AND A NESTED BRACE DEFEATS A NON-NESTING PARSE.** The symbol
scanner collapsed `\mathrm{Nu}` to `Nu` and read `N` and `u` as two undeclared symbols, and later
turned `C_{\mathrm{Nu}}` into `C_{mathrm{Nu}`. **Write the plain subscript in the article rather than
asking the scanner to cope.**

**WORKING AN EQUATION IS THE POINT, AND TWO OF THIS ARTICLE'S OWN EXPLANATIONS DID NOT SURVIVE IT.**
The draft's gas-transport argument had one fluid where there are two, air and resin crossing the same
channels with viscosities a factor of 540,541 apart, **so four hours of vacuum would clear twelve
metres of dry tow and the path length was never the constraint.** And the draft blamed a cure-schedule
margin on laminate thickness when a six millimetre facesheet equilibrates in two minutes against a
four hour dwell. **In both cases the correction made the argument stronger.**

**COMPUTE THE SENSITIVITY AND SAY WHICH HALF IS ROBUST.** Two of the three DiBenedetto parameters are
assumptions and the vitrification ceiling moves between 0.741 and 0.899 across the range they occupy.
**The conclusion does not move at all**, because vitrification is defined by the glass transition
meeting the cure temperature and nothing else enters that definition. **A number can be
assumption-dependent while the claim built on it is not, and both halves belong in the article.**

**A FIGURE DELETED FOR BEING UNSUPPORTED CAN COME BACK WITH ARITHMETIC BEHIND IT.** The draft pass
removed `the hundredth aeroplane` from the conclusion as a rhetorical number no checker had seen. **The
equation pass computed the break-even run at 41 to 409 and 109 on the middle assumption.** The
rhetorical figure was approximately right, **which is not a reason to have kept it.**

**READ THE PROGRAMME'S BIBLIOGRAPHY, AND THE REASON IS NOT THE ONE A350 AND A351 GAVE.** Chasing the
Composites Affordability Initiative's citation chain produced thirty-two documents by hand, and
**twenty-six of them were already in the corpus.** So a bibliography does not mainly find what a sweep
missed. **It says which of five and a half thousand records the argument needs**, which no gate can
decide and no count can show. Twenty-six sat in the survey as anonymous author-and-year entries
carrying the whole citation chain of the article's central claim, unread. **That is a better argument
than the one it replaces, because it does not depend on the sweep having failed.**

**PROBE THE CONCLUSIONS IN THE FIELD'S WORDS BEFORE CONCLUDING ANYTHING ABOUT COVERAGE.** Eight of
nine of A352's conclusions were probed and **six opened on rewording alone with no harvest at all**,
three of them from literally zero. **The appearance that a survey does not cover its own conclusions
is usually a fact about the probe.**

**AND ONE CONCLUSION WAS CORRECTLY OUT OF SCOPE FOR THE ARTICLE'S OWN GATE.** The claim that a
programme was built cheaper and slower belongs to defence acquisition, which an aeronautical
manufacturing gate refuses by design. **Say so in the Source Base and let the claim stand on its
dates.**

**A CONCLUSION CAN CONTRADICT ITS OWN BODY AND NOT MERELY LAG IT.** Eight previous articles found a
conclusion that predated a later pass and omitted its findings. **A352's asserted the opposite of
what its body said**, claiming the aeroplane retired a technical risk the body spends a section
showing was still open fourteen years later. **And the same stale claim was sitting in the body as
well**, which is why finding it in the conclusion must send the search back through the article.

**THE CAPS-EMPHASIS DEFECT APPEARED IN THREE OF THE FOUR PASSES, EVERY TIME IN NEWLY WRITTEN SOURCE
BASE PROSE.** It is now the most reliable defect this method produces. **Scan before every freeze.**

---

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

### Added in A367, and the pattern is that every quotation is found in a saved source

- `verify367.py`, 569 checks, importing no measurement module. It re-parses the register with an HTML
  parser, recomputes hover weights by bisection, the drag ceiling by thrust over dynamic pressure at four
  altitudes, the cruise ceiling and atmosphere by integrating the hydrostatic equation, and money from the
  award transactions. **Every double-quoted span of twelve characters or more must appear verbatim in a
  saved source**, 75 of them against 109 sources. Thirteen symbolic displays are asserted verbatim and
  withdrawn wordings asserted absent. `A367_DRAFT` points it at a mutated copy.
- `calc367.py` and `eqpass367.py`, every figure computed in one place, with the assumptions named in
  `ASSUME`.
- `harvest367.py`, `cluster367.py` with 32 keep and 42 refusal cases each also hyphenated, `refs367.py`
  with overlap and empty counts, `abstracts367.py` and `lit_abstracts367.py` for abstracts, and
  `patents367.py` for patent abstracts.
- `awards367.py`, the USAspending sweep by programme name, phrase and recipient, with transactions.
- `assemble367.py`, one sorted definition block, since `_verify.py` sorts a contiguous run as a whole.
- `handoff367.py`, this file's rewrite, boundaries on the original string and the heading list compared.

### Added in A366, and the pattern is that every figure has a second route

**Under `tmp/a366/`, gitignored.**

- `meas366.py`, the register over `meas.all_rows()` only: rows carrying 69 to 75, the pointer walk,
  the rate and Poisson tail, the officiality counts and the commemorative lags. `rule2020.py`, every new
  design number since 3 November 2020 against both next-number definitions, with same-day blocks.
- `eqpass366.py`, every equation-pass value, with `verify366.py` re-deriving each by a different route:
  Newton against bisection for the rescue multiplier, direct integration against the closed form for
  the range probability, the upper sum against the complement for the tail.
- `verify366.py`, **745 checks importing no measurement module**, the register re-parsed with an HTML
  parser, every quotation read back from its saved copy, withdrawn wordings asserted absent and
  replacements present, the display floor at 42, and **the blank-line check around display blocks**.
- `harvest366.py`, `sweep2_366.py` and `cluster366.py`, the two sweeps and the gate with 24 keep and
  33 refusal cases each hyphenated; `resolve366.py`, years for admitted reports-server records only
  with a success-rate floor; `refs366.py` with the hand-chosen primaries verified by title in
  `prim_research.json`; `assemble366.py`, slots filled and every definition required cited.
- `wb/`, the archived register and missing-designations snapshots that date the rows' publication,
  fetched as `id_` captures with `--compressed`, **because the uncompressed fetch returned a 51 KB
  page that is not the register**.
- `prim/`, the primaries read in the reference pass, including NASA SP-2003-4531 as text.
- `handoff366.py`, this file's rewrite, boundaries on the original string and the heading list compared.

### Added in A365, and the pattern is one instrument per claim class

**Under `tmp/a365/`, gitignored, with `tmp/mathrepair/` beside it for the corpus repair.**

- `meas365.py` and the lifted `meas.py` and `register.py`, the register over both populations,
  with the wide `meas.all_rows()` the only one any stated figure may use.
- `bbscan.py`, every budget book's LongShot entry, the funding matrix with its restatements, the
  description diff that dated the concept change, and the plans lists; `slips.py`, each named
  milestone tracked across the books that plan it, the rolling-slip signature being a milestone
  planned for every book's own budget year in turn.
- `awards.py` and `usaspend.py`, the federal award record with keep and refusal lists, the
  homonym company and the mine-removal contract refused by name.
- `calc365.py`, the keystone arithmetic with the derivations in the docstrings, plus the equation
  pass's `eqpass()`, the atmosphere, the two-body energetics, the roll transient, the climb
  collapse and the marginal exchange; `emit365.py`, roughly three hundred slots.
- `gate365.py`, the subject gate on the carried-object principle, audited 62 keep against 45
  refusal cases with every refusal retested hyphenated; `homprobe365.py`, the bare words measured
  before any guard was written; `cluster365.py`, both sweeps merged and clustered;
  `harvest365.py` and `sweep2.py`, the aimed second sweep measured against `before365.json`.
- `refs365.py`, the chooser on the shared library's dedupe with the `NAMED` group for addresses
  that are not readings; `mklit.py`, the citation runs generated, never typed; `assemble365.py`,
  slots filled, every defined anchor required cited; `verify365.py`, **120 checks importing none
  of the measurement or emitter modules**, the register re-parsed with a second parser, the books
  re-read with different patterns, closed forms against explicit moment-taking and bisection, and
  both fact-sheet conversion errors asserted.
- `series_line.py` for the sixty-ninth opening line, 68 anchors asserted; `pubreview.py` retuned,
  the dateline label now this article's; `symcheck.py` and `mathrot.py` as before.
- **`tmp/mathrepair/fixmath.py` and the twin-build pair**, the corpus repair rehearsed to zero
  with the collateral proof, kept because the next corpus-wide edit should start from them.
- `FINDINGS.md`, the durable findings file the flagged turn taught, written as findings arrive.

### Added in A364, and the register is the instrument rather than the subject

**IN `tmp/a364/`, WHICH IS GITIGNORED, SO LIFT WHAT YOU WANT BEFORE IT GOES.**

| File | What it does that nothing else did |
|---|---|
| `register.py` | parses the allocation register into rows with officiality at **three markup levels**, a row mark, a cell mark and a span mark, which mean three different things |
| `meas.py` | every count, share, ordering and gap the article states about the register, including the borrowing chronology and the identical-description measurement |
| `calc.py` | the code space, the information bound, the commonality and refresh closed forms, and the empirical ceiling-match test |
| `calc2.py` | the increment and pointer walks that test the instruction's own definition of a design number, plus every derivative, limit and inversion the equation pass added |
| `eqscan.py` | lists every prose line carrying a figure with no display block nearby, after excluding dates, designations, contract numbers and status codes, **because none of those is a result** |
| `getdocs.py`, `getdocs2.py`, `getdocs3.py` | the primary-document fetches, each recording whether bytes arrived, whether they are a document, and under which user agent |
| `primhunt.py` | the named-document hunt, which checks a **proof phrase** inside the bytes so that a wrong document arriving at a right address is visible |
| `harvest2.py` | the aimed third sweep, written in the report literature's vocabulary rather than the programme's |

**AND THE REPAIRS TO INHERITED INSTRUMENTS MATTER AS MUCH AS THE NEW ONES.** `mathrot.py`'s source-side
counter now counts three-line display blocks as well as one-line ones. `symcheck.py` keeps `\mathcal{X}`
as a compound token instead of stripping it, and gained the operator and label tokens the equation pass
introduced. `stylecheck.py` excludes inline code spans, narrows the parenthetical test to an actual
interruption, and carries this article's acronyms rather than A363's. `pubreview.py` removes a display
block as a block. `urlcheck.py` gained a **registry fallback**, which is what separates a publisher
refusing a robot from an identifier that resolves to no record at all, and is what caught an invented
identifier. `run_gate.py` merges two sweeps and normalises the source label once.

**`verify_numbers.py` RUNS 373 CHECKS AND IMPORTS NEITHER `meas.py` NOR `calc.py` BY DESIGN**, and
**parses the register again with a different parser**, because two parsers agreeing is evidence and one
parser is a transcription. **The shapes that transfer**: re-derive rather than read; freeze occurrence
counts on whitespace-normalised text rather than asserting presence; carry a floor on the display-equation
count; assert withdrawn wordings absent **and** their replacements present; check a closed form against a
quadrature, a central difference or a simulation rather than against itself; take a limit at an argument
chosen from the exponent; assert that every partition is exhaustive and disjoint; and **assert that every
hand-written source is cited in the body**.

**THE STUB BUILD IS STILL THE BUILD TO RUN PER PASS.** `tmp/a364/site_build.sh` takes about fifteen
seconds and matches the shipped bytes by checksum before it starts. **`./_check.sh --drafts` scales
superlinearly in link-definition count and A360 lost five hours and forty-one minutes to it.**

### Added in A363, and three of them exist because an existing instrument was blind

**IN `tmp/a363/`, WHICH IS GITIGNORED, SO LIFT WHAT YOU WANT BEFORE IT GOES.**

| File | What it does that nothing else did |
|---|---|
| `astrisk.py` | predicts kramdown's ASTERISK pairing inside inline mathematics, which `emrisk.py` does not model at all |
| `mathcorpus.py` | MEASURES corrupted mathematics in the rendered corpus and attributes each span to its cause, which is the only authority on the count |
| `stylecheck.py` | the project's prose rules checked on prose only, after stripping tables, headings, quotations, mathematics and reference definitions, plus an acronym-before-first-bare-use check |
| `exact.py` | the exact Breguet optimality conditions with their small-fuel limits taken rather than asserted |
| `fairpair.py` | the like-for-like arithmetic from the Ames comparison, including the apparent weight elasticity from a pair |
| `before_after.py` | the per-cluster primary share, run before and after the third sweep so the aim and the result are both measurements |
| `primhunt.py` | the named-document hunt, eleven targets and eight full texts, which separates a download from a reading in what it prints |
| `count.py` | the structure count, in a file because a heredoc double-escapes regexes and reported eight thousand symbols |

**`stylecheck.py` IS THE ONE MOST WORTH CARRYING FORWARD.** `_verify.py`'s contraction check does not
exclude block quotations, so it correctly flagged a contraction that belonged to a quoted source and
A363 had to restructure the quotation to keep the corpus at no new warnings. **`stylecheck.py` knows
the difference between the author's punctuation and a source's**, which is what makes its zero
meaningful, and it proved that all nine parentheticals and both semicolons in A363 were quotations
except one statutory subsection citation.

**AND THE REPAIRS TO INHERITED INSTRUMENTS MATTER AS MUCH AS THE NEW ONES.** `mathrot.py`'s display
counter now requires that a delimiter not be preceded by another backslash. `symcheck.py` gained the
trigonometric functions and the layout directives. `verify_numbers.py` derives its tolerance from the
last printed digit rather than comparing rounded strings at full precision, and reads spelled counts
back through `_lib/survey.py`.

**`verify_numbers.py` RUNS 158 CHECKS AND `neweqns.py` RUNS 94, AND THE SECOND IMPORTS NEITHER
`meas.py` NOR `calc2.py` BY DESIGN.** A verifier that calls the calculation module checks that the
module is self-consistent and nothing else. **The shape that transfers**: re-derive rather than read,
freeze occurrence counts rather than asserting presence, carry a FLOOR on the display-equation count,
assert withdrawn wordings absent AND their replacements present, check a closed form against a
quadrature or a difference rather than against itself, and **take the limit of a general form to prove
it reduces to the special case it generalises**.

**THE STUB BUILD IS STILL THE BUILD TO RUN PER PASS.** `tmp/a363/site_build.sh` takes about fifteen
seconds and matches the shipped bytes by checksum before it starts. **`./_check.sh --drafts` scales
superlinearly in link-definition count and A360 lost five hours and forty-one minutes to it.**

### Added in A362, and all four exist because something reached the rendered page unseen

**A362 ADDED FOUR INSTRUMENTS AND NONE OF THEM TOUCHED THE SHARED LIBRARY.** They live in
`tmp/a362/` and each catches something no existing check does. **Copy them forward.**

| File | What it catches that nothing else does |
|---|---|
| `emrisk.py` | where kramdown will put an emphasis tag inside inline mathematics, predicted from the source on a rule measured from kramdown itself |
| `mathrot.py` | the same defect confirmed in the rendered page, plus source display blocks against the rendered bracket count |
| `rendercheck.py` | unresolved markers, literal anchors and unrendered Liquid in the built page, with inline and display counts beside the source's |
| `symcheck.py` | every symbol used but not declared, and every base letter carrying two declared meanings |

**`tmp/a362/gate_and_cluster.py` IS THE FILE TO COPY WHOLESALE.** It carries `guarded(body)` for
combining an exclusion with a match pattern without anchoring the body, **`sep(phrase)` so that no
guard phrase can be defeated by a hyphen**, `_not(*phrases)` for building a guard from
separator-tolerant parts, and `check_guards` with fourteen keep cases and thirty-four refusal cases
**including every refusal re-tested with its spaces hyphenated**. All four are load-bearing.

**AND THE SWEEP IS NOW THREE SWEEPS.** `harvest.py` asks the subject broadly, `harvest2.py` walks
deeper wherever the first hit the retrieval wall, and `harvest3.py` is written in the report
literature's own vocabulary **after `before_after.py` has measured the per-cluster primary share**.
Measure first, aim the third sweep at the thinnest clusters, and **report what it bought even when
the answer is three records**.

**`resolve_years.py` CARRIES A SUCCESS-RATE FLOOR AND MUST KEEP IT.** `fetch.ntrs_detail` returns a
parsed result, not the raw response. **An empty year is legitimate, so only a floor separates a
parser fault from a dateless registry.**

**`verify_numbers.py` RUNS 160 CHECKS AND THE SHAPE IS WHAT TRANSFERS.** Re-derive the physics rather
than reading a results file. Freeze occurrence counts rather than asserting presence. Recompute the
survey statistics from the reference base. **Freeze a floor on the display-equation count**, because
a later pass deleted one silently. Assert that withdrawn wordings are ABSENT and their replacements
PRESENT. **And recompute every before-and-after figure from a frozen baseline, so the pass can be
audited rather than believed.**

**THE STUB BUILD IS STILL THE BUILD TO RUN PER PASS.** `tmp/a362/site_build.sh` takes fifteen
seconds and matches the shipped bytes by checksum before it starts. **`./_check.sh --drafts` scales
superlinearly in link-definition count and A360 lost five hours and forty-one minutes to it.**

### Carried forward from A361

**A361 ADDED NOTHING TO THE SHARED LIBRARY AND THAT IS WORTH SAYING.** Its two transferable findings
are about how to USE `_lib/fetch.py` rather than about changing it. **The reports-server detail call
buys only the publication year**, since the search response already carries the title and the authors,
so the correct order is to gate on titles first and resolve years for the admitted records alone.
**`tmp/a361/resolve_years.py` is the pattern** and it prints the saving it achieves, which on A361 was
10,889 avoided requests and 61.7 minutes. The second is that a sweep must write its search phase to
disk before its slow walk begins.

**AND A361'S OWN GATE CARRIES THE ONE THING A LATER ARTICLE MUST COPY.** `guarded(guards, body)` in
`tmp/a361/gate_and_cluster.py` combines an exclusion guard with a match pattern without anchoring the
body, and `check_guards` in the same file is the regression test that keeps it correct. **Both are
short and both are load-bearing**, for the reason given in the first entry under *Earned in A361*.

**IN `tmp/a361/`, WHICH IS GITIGNORED, SO LIFT WHAT YOU WANT BEFORE IT GOES.**

  `meas.py`          The 1976 standard atmosphere extended to density and sound speed, a
                     self-consistent ascent from a speed law and a pitch program with the published
                     cut-off altitude as a constraint, the thrust error budget, the footprint polygon
                     and the azimuthal sampling. **Every loop has a bound in its header** and the
                     lever-arm function documents the inversion it once had.
  `neweqns.py`       **466 checks verifying each relation the equation pass added by a route
                     different from the one that produced it.** The atmosphere is checked against the
                     standard's own published table at five altitudes, the budget by finite
                     differences through `F = m a + D`, the ballistic-coefficient form against the
                     direct ratio, the Fourier estimators by building a field from known coefficients
                     and recovering them, and the alias map by direct evaluation at every harmonic up
                     to three times the sensor count.
  `verify_numbers.py` **1,531 checks pairing every stated figure with a recomputation**, plus
                     `check_withdrawn`, which asserts the withdrawn wordings absent AND the hedges
                     present, because forbidding the bad wording alone passes when the hedge is
                     deleted too.
  `pubreview.py`     The publication-review scans as one file, taking a mode argument, being the
                     superlative scan in two strengths, the drafting-history scan, the bold-number
                     unit scan, the acronym first-use scan and the n-gram diction scan.
  `urlcheck.py`      The address sweep, **with a registry fallback for a DOI a publisher refuses**,
                     reporting fetched, confirmed-through-the-registry and unresolved separately.
  `primaudit.py`     Per-cluster primary fractions with each cluster's largest single source, which
                     is what turns a thin cluster from a shortfall into a fact about a publisher.
  `curated.py`       Resolves each curated primary to a fixed identifier and **checks the returned
                     title against a fragment the article asserts**, which caught two anchors
                     resolving to one document because one title is a substring of the other.

**THE PREVIOUS ENTRY, FOR A360, FOLLOWS AND ITS SHARED-LIBRARY REPAIRS ARE STILL THE IMPORTANT ONES.**

**A360 ADDED TWO TO THE SHARED LIBRARY AND SEVEN TO ITS OWN PIPELINE.** The shared ones are the
ones that matter, because they are inherited.

**IN `_lib/fetch.py`, WHICH EVERY LATER ARTICLE GETS FOR FREE.** `ntrs_search` now paginates with
bracketed parameters and actually returns the `rows` it is asked for, where before it returned ten
whatever it was asked. `ntrs_total` is new and reports the server's own match count. **Both are held
by `t_a360_ntrs_search_paginates_with_bracketed_parameters` in `_lib/test_lib.py`, which runs offline
against a fake transport** and checks the parameter spelling, that the walk advances, that no record
comes back twice, and that a server repeating one page terminates the walk rather than spinning.

**AND IN `_research/homonyms.py`.** `_anchor_stem` no longer inserts into `sys.path` per record, and
the stem is memoised. `t_a360_stem_cache_is_stable_and_does_not_grow_sys_path` holds both halves,
being that the path does not grow and that the cached answer equals the direct one.
`t_a360_fracture_family_guards_the_nozzle_wake` fixes the finding that the `fracture` and
`wind-energy` families are what protect a plug-nozzle sweep, with the rocket sense required to
survive both. **The suite is at 120 of 120.**

**IN `tmp/a360/`, WHICH IS GITIGNORED, SO LIFT WHAT YOU WANT BEFORE IT GOES.**

  `noz.py`        Isentropic nozzle flow and the 1976 standard atmosphere in pure Python, with
                  bounded bisection, the Vandenkerckhove constant, thrust coefficients, the ideal
                  envelope and the Bregman loss. **Every loop has a bound in its header** and the
                  scale-height function documents the factor-of-two boundary error it once had.
  `neweqns.py`    **246 checks that verify each relation the equation pass added, by a route
                  different from the one that produced it.** The conjugacy identity is checked by a
                  momentum integral rather than by differencing the closed form, Fenchel-Young by
                  evaluating the gap, the Bregman form by quadrature, and the ring identities by
                  enumerating the crossing directions.
  `symcheck.py`   The symbol table and its two-way check, with the pass-order lesson in its
                  docstring. **Run it with `--table` to regenerate `symbols.md`.**
  `sepcalc.py`    The separation criterion of NASA TP-1207 applied to this article's nozzles by
                  walking the nozzle from throat to exit. **This is the instrument that withdrew the
                  drafting pass's conclusion.**
  `primaudit.py`  Report-primary fraction per cluster, with the largest registrant of each. **This
                  is what says whether a thin fraction is a shortfall or a fact about a
                  discipline**, and it is the file to run first in any primary-reference pass.
  `primrefs.py`   Curated primaries resolved by identifier with their titles read back.
  `site_build.sh` The stub-isolated build. **Use this and not `_check.sh --drafts`.**

Also present and reusable without change: `harvest.py` through `harvest4.py`, `merge_sweeps`,
`gate_and_cluster` with its fingerprinted family-cost cache, `build_refs`, `emit`,
`emit_source_base`, `emit_years`, `emit_spellings`, `emit_tables`, `emit_series_line`, `calc`,
`calc2`, `chamber`, `engineout`, `meanid`, `regstats`, `related`, `assemble`, `verify_numbers`,
`verify_ids`, `urlcheck`, `homprobe`, `curated`, `keydois`, `ramjetprobe`, `remeasure_families`,
`usa` and `usa2`.

**THREE PRIMARY DOCUMENTS ARE SAVED AS PDF AND TEXT IN THAT DIRECTORY AND ARE WORTH KEEPING**, being
NASA SP-8120 on liquid rocket engine nozzles, NASA Technical Paper 1207 on separation criteria, and
the 1976 United States Standard Atmosphere. **A361 will want all three.**

**`primaudit.py` IS THE ONE TO RUN FIRST NEXT TIME.** A360's third pass began by measuring the
primary fraction per cluster, found the keystone at 8.7 percent against an article average of 10.4,
and aimed its sweep at the clusters that measured thin. **Every cluster then rose, and the keystone
rose to 16.8 while remaining the thinnest.** The test that says why is A359's: **the three thinnest
clusters are exactly the three in which one conference publisher holds the largest share**, at 34, 49
and 51 percent, against 26 and 29 percent for the general nozzle and propulsion clusters which carry
29 and 49 percent reports. **The aerospike subject is a conference literature and the rocket
propulsion around it is a report literature**, so the remaining thinness is a fact about publishing.

**A359 ADDED SEVEN INSTRUMENTS WORTH COPYING FORWARD, ALL IN `tmp/a359/` AND THEREFORE
GITIGNORED.** The whole A359 pipeline is there and repoints cleanly: `harvest.py` through
`harvest4.py`, `merge_sweeps`, `gate_and_cluster`, `build_refs`, `emit`, `emit_source_base`,
`emit_limits`, `emit_years`, `emit_spellings`, `calc` and `calc2`, `eqns`, `symcheck`,
`article_numbers` and `article_numbers2`, `probe`, `regstats`, `contract`, `usa`, `usa2`,
`related`, `assemble`, `verify_numbers`, `verify_ids`, `inject`, `pubscan`, `eqn_scan`,
`homprobe`, `homprobe360`, `lin` and `full_build.sh`.

**`lin.py` IS SMALL DENSE LINEAR ALGEBRA IN PURE PYTHON, BECAUSE THIS ENVIRONMENT HAS NO ARRAY
LIBRARY.** Gauss-Jordan inverse, full-column-rank pseudoinverse, the projector, power-iteration
spectral norm, closed-form two-by-two singular values and a bounded-loop rank. **Every loop has a
bound visible in its header.** A359's first draft of `calc.py` imported `numpy` and died.

**`pubscan.py` IS THE PUBLICATION REVIEW'S OWN INSTRUMENT AND IT FOUND FOUR REAL DEFECTS.** It
splits the AUTHOR PROSE into sentences, having removed citations, display equations and tables,
and reports two classes: **drafting-history candidates**, by a vocabulary of `the draft`, `an
earlier version`, `was withdrawn` and their relatives, and **superlatives**, by `the only`, `the
first`, `never`, `every`, `always`, `unique` and thirty more. A359 returned **0 drafting-history
candidates**, which is the first time in this series, and **76 superlatives of which four did not
earn their place**.

**`eqn_scan.py` IS THE EQUATION PASS'S MIRROR OF IT.** It reports sections that name a relation or
carry four or more numeric literals and display no equation. **The shared `audit.equation_gaps`
counts a one-line `$$ ... $$` fence and this corpus writes a three-line one**, so it reports zero
equations everywhere and every section as a gap, which is a check reporting a clean subset in
reverse. The fence shape is the whole of the difference.

**`emit_limits.py`, `emit_years.py` AND `emit_spellings.py` EMIT TABLES RATHER THAN LETTING THEM BE
TYPED**, each asserting its own total against a figure computed separately. A358 typed a
composition as literals and a gate change moved it within the same pass.

**`regstats.py` RECOMPUTES EVERY CLAIM THE ARTICLE MAKES ABOUT THE REGISTER**, and the verifier
then re-parses the saved HTML by a second route and compares. **That second parser found its own
defect before it found anything else.**

**AND THE CURATED-IDENTIFIER CHECK IN `verify_ids.py` IS NEW AND IS THE STRONGEST OF THEM.** Every
hand-written DOI and reports-server identifier is resolved through the registry and compared
against the year its label claims, **and a deliberately fabricated identifier is resolved alongside
them and required to return nothing.** A check that cannot distinguish a real identifier from an
invented one is measuring the network. A359 held 39 of them, plus 33 quoted phrases against saved
copies with a whitespace-collapsing fallback for scanned text, plus 14 books against both recorded
title and recorded author.

**A358 ADDED SIX INSTRUMENTS WORTH COPYING FORWARD, ALL IN `tmp/a358/` AND THEREFORE
GITIGNORED.**

**`contract.py` READS A FEDERAL AWARD AS DATA AND RECONCILES IT.** It sums the raw transactions of
each award, compares the sum with the total the registry states separately, and refuses on a
disagreement. It also applies the article's dateline horizon at the source rather than in the prose,
because one transaction on A358's contract carries an action date past the editorial date and an
article must not report it. **Three awards, three exact reconciliations.**

**`origin.py` TURNS A PAPER TRAIL INTO ARITHMETIC.** Dates of documents, obligations and milestones
go in and intervals come out, including the one that matters, which is a stated schedule against the
outcome.

**`record.py` MAKES A FLIGHT TEST RECORD REASSEMBLE.** Each test series is a row and the programme's
own stated totals are separate constants, so the parts and the whole are independent statements that
can be added up. **Three reassembly checks, three agreements.**

**THE OCCURRENCE-COUNT CHECK REPLACES EVERY PRESENCE CHECK**, for numbers and for sentences alike.
A value is required to appear exactly as often as it does, so one instance going stale in a later
pass drops the count and fails. **Eight of A358's first in-text checks passed while a value had been
corrupted, and the phrase guard repeated the same defect two passes later.**

**THE PHRASE GUARD HOLDS TWENTY-ONE FORMULATIONS THAT CARRY NO DIGITS**, by exact wording and by
count, because a numeric verifier structurally cannot catch a claim with no number in it.

**AND THE DATELINE HORIZON CHECK STRIPS CITATIONS BEFORE IT LOOKS.** A bibliographic year in a
reference label is not a claim the article makes, and A358's survey holds several thousand of them.

**A357 ADDED FOUR INSTRUMENTS WORTH COPYING FORWARD, ALL IN `tmp/a357/` AND THEREFORE GITIGNORED.**

**`full_build.sh` BUILDS WHAT THE DEPLOY BUILDS.** It rsyncs the whole repository, copies the draft
into `_posts`, writes a front-matter stub for every sibling draft so `post_url` resolves, checksums the
copy against the draft, and times a production build of all 301 posts. **The stub builder every earlier
article used measures 96 pages and is not the deploy**, which is how three passes of A357 came to model
a cost that did not exist. Use both, and believe the corpus one.

**`pass_history.json` MAKES A BEFORE-AND-AFTER COMPARISON DATA RATHER THAN PROSE.** Each pass appends
its measured research count, primary count and per-query yield, the emitter reads the last entry, and
the current pass sits under `current` for the next to promote. **A comparison typed as a literal is
A342's stale-statistic defect with a longer fuse.**

**`check_withdrawn` IS A REGRESSION GUARD AND NOT A TEST OF TRUTH.** A numeric verifier cannot catch a
claim that contains no number, so the withdrawn formulations are listed and the article is scanned for
their return, with the paragraph that names them cut before the scan.

**AND THE INJECTION SUITE HAS BECOME THE SLOWEST INSTRUMENT AND THE MOST VALUABLE ONE.** A357's runs
took up to two hours for a hundred injections, because each one re-runs a verifier that re-integrates a
53-programme trajectory grid. **Budget for that**, and do not run anything else against the article
while it holds `inject.lock`.

**THE SHARED MECHANISM IS COMMITTED AND MUST NOT BE REBUILT.** `_lib/` holds it, with `README.md`
describing each module: `fetch` for archive queries, `refs` for anchors and the reference block, `edits`
for guarded editing, `reflow`, `lint`, `diction` for word and phrase overuse, `audit` for equation and
citation gaps, `numcheck` for independent re-derivation, and `citations` for registry verification. Run
`python3 _lib/test_lib.py`, which should report **117 of 117** as of 2026-09-14. **`refs.clean` gained a bare-pipe strip on
2026-08-12**, because kramdown reads a paragraph whose first line contains a pipe as a table and a
publisher-mangled apostrophe entity put one into link text. **Three modules were added on
2026-08-11**, being `gate` for subject-anchor gating with a mandatory two-sided sample, `render` for
auditing BUILT HTML, and `resolve` for identifier resolution. `_research/rejected.json` holds the accumulated
sweep judgements, reused through `_research/homonyms.py`, **whose curated pattern list is now 141 across 31 tagged families**, the newest family being
`physiology`, earned by A359 and **created by SPLITTING AN ENTRY rather than by widening one**,
because A348's biomedical computational-fluid-dynamics entry alternated ten terms of which exactly
one, the stem `physiolog`, names the discipline that measures a pilot. The family before it was
`drug-discovery`, earned by A358 when molecular docking reached the relative-navigation cluster of
an article about docking one aeroplane with another. **A358 added four patterns**, being that one,
the remote-sensing sense of `retrieval`, the grey partridge and desert locust behind two programme
names, and the African locust bean. The family before it was `pulsed-power`, earned by A357 when
Sandia's PEGASUS capacitor bank reached a kept set about the Orbital Sciences Pegasus air-launched
booster.

**`_lib/booklinks.py` WAS REWRITTEN ON 2026-09-04 AND ITS PREVIOUS ORACLE WAS UNSAFE.** It reads the
OpenLibrary SEARCH INDEX rather than the work JSON endpoint, because that endpoint returns HTTP 500
both for records that exist and for keys that do not. `resolve` returns `found`, `absent` or `unknown`;
`check` returns `ok`, `wrong`, `missing` or `undetermined`. **A failure is never a verdict.** The
search index also returns the AUTHOR, so a key can be held to both halves of an `Author, Title` claim,
which is a higher standard than the gate it has to pass. `author_claim` and `author_agrees` are
reported and not enforced, because repositories list editors and initials inconsistently.

**THOSE PATTERNS CARRY TAGS AND CAN BE SWITCHED OFF BY NAME**, across twenty-nine
families: `adhesive-bonding`, `civil-structures`, `cockpit-displays`, `composites`, `cost-estimation`,
`cure-monitoring`, `delamination`, `dentistry`, `ecology`, `electric-machines`,
`environmental-assessment`, `fracture`, `geophysics`, `hypersonics`, `interpreting`, `marine`,
`medicine`, `meteorology`, `missiles`, `ndt`, `nomenclature`, `ocean-modelling`, `ramjet`,
`remote-sensing`, `smart-actuators`, `surface-transport`, `teaching` and `wind-energy`.

**A359 OPENED THREE AND SPLIT AN ENTRY TO CREATE THE THIRD**, being `cockpit-displays` because
its subject was a pilot in a cockpit being deceived, `teaching` because the aeroplane is operated
by a school and the family was deleting three papers about that school's own curriculum, and
`physiology` because the family that held it did not exist until A359 made it.

**A356 TAGGED ONE AND OPENED THIRTEEN.** The cockpit-display family was written by A347 against the
human-factors literature of rotorcraft displays and **carried no tag**, so it could not be reached at
all, and it was deleting 105 titles of synthetic vision, head-up display and symbology literature from
an article about an aeroplane with no forward windscreen. **The repair is a tag rather than a
weakening**, on the A352 adhesive-bonding precedent. **Thirteen families open is as many as any article
in this series has opened**, equalled by A351, and both are the sonic boom articles.

**A353 SPLIT ONE ENTRY AND A354 TAGGED ONE AND GUARDED THREE.** A353 found a tag whose NAME was
narrower than its PATTERN, the bare word `dielectric` carrying the tag `cure-monitoring` while also
catching dielectric barrier discharge plasma actuators and dielectric elastomer actuators, so it was
split and `smart-actuators` added. **A354 found a pattern with NO tag at all that was its article's
subject**, the rotor of an electrical machine, and added `electric-machines`. **A354 also guarded the
marine, rail and road families against multi-modal venue names**, by a condition that fires only when a
string names aircraft alongside another transport mode.

**A352 ADDED SEVEN AND SPLIT ONE ENTRY, AND THE SPLIT IS THE LESSON.** A351 found that a contaminant
FAMILY can span two store entries, so tagging one leaves the other armed. **A352 found that a single
ENTRY can span two families.** The A347 rotor-repair entry alternates `field-replaceable`, `rotor
blade`, `blade pocket`, `hot corrosion`, `adhesive bond`, `corrosion protection` and `depot
maintenance`, and exactly one of those named a composites article's subject. **Tagging the entry would
have readmitted rotor blade pockets and hot corrosion**, so the alternative was separated into its own
tagged entry and the remainder left armed. A test in `_lib/test_lib.py` holds the separated half armed
and was proved capable of failing by rebuilding the store the naive way.

**AND WIDENING HAS A PRICE THAT ARRIVES IMMEDIATELY.** Switching off `composites`,
`adhesive-bonding` and `fracture` readmitted thirty-nine records on restorative dentistry, which uses
bond strength, cure kinetics, resin composite and degree of conversion as its own terms of art.
`dentistry` went into the store in the same commit as the sentence recording it.

**Eleven families were added by A351 alone**, whose subject was a noise rather than an aeroplane and which
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

**THE PER-ARTICLE VERIFIER NOW RUNS SEVEN CHECKS AND EVERY ONE HAS FOUND SOMETHING.** Five came
from A351 and two from A352. They live in `tmp/a352/verify_numbers.py`, which is gitignored, so they
are described here in enough detail to rebuild. **Every one was proved non-vacuous by injecting the defect and watching it fail**, and
that proof should be repeated when they are carried forward.

| Check | What it caught |
|---|---|
| **Staleness guard** | refuses to run when `body.md` or any input JSON is newer than the draft. A pipe had masked a failed assembly and the verifier validated the previous draft |
| **Prose citation labels** | compares every typed `[[label][anchor]]` in the body to the TITLE its anchor points at. Survey labels are emitted and cannot drift; body labels are typed. Found two |
| **Declared symbol table** | refuses any symbol in math that is not declared with one meaning. Found four collisions, `T`, `L`, `R` and `\ell` |
| **MathJax macro allowlist** | refuses any macro outside the packages `tex-mml-chtml` provides, because `noundefined` renders an unknown macro as red text and fails NOTHING. Also refuses a doubled backslash, which contains the macro it doubles |
| **Dateline horizon** | refuses any year in the prose after the article's own editorial date. Caught a July 2026 regulatory limit in an article dated November 2025 |
| **Independent re-derivation** | recomputes every published number by a DIFFERENT route without importing the calculation. A352's solves the Arrhenius pair as a two-by-two system rather than a log ratio, reaches a pressure ratio by bisection, and round-trips DiBenedetto forwards from its own inversion |
| **Duplicate-symbol refusal** | the symbol table is built from a LIST OF PAIRS and raises on a repeated symbol, because a dict literal accepts a duplicate key silently. **Found five real collisions in one article.** It catches an undeclared symbol and NOT a declared one used twice, so the duplicate refusal is the half that catches the collision |

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

**THE FEDERAL REGISTER IS A PRIMARY SOURCE AND A356 WAS THE FIRST ARTICLE TO USE IT.** Its search API
is `https://www.federalregister.gov/api/v1/documents.json` with `conditions[term]`,
`conditions[agencies][]`, `conditions[type][]` and `conditions[publication_date][gte|lte]`, and it
returns a `raw_text_url` for each document. **The full text is served inside a preformatted HTML block,
so the tags must come off before it is searched.** **A direct fetch of a document page redirects an
automated agent to an unblock page**, so use the API or the full-text endpoint. The American Presidency
Project carries executive orders in plain HTML when the Federal Register refuses.

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

### RESOLVED on 2026-10-02, in-place repair on the pilot's decision. The A358 and A359 officiality correction

**THE REGISTER'S OFFICIALITY MARKUP HAS FOUR STATES AND TWO PUBLISHED ARTICLES SUMMARISE IT IN TWO
NUMBERS.** A358 gives the X-row split as 21 official and 9 not, which accounts for 30 of 31 rows because
the partly marked row has nowhere to go. **A359 closed that sum by raising the official count to 22**,
which places the partly marked row on the side its own markup denies. The split recorded here has been
**21 official, 9 wholly unofficial and 1 partly unofficial**, and A360 states it correctly.

**A364 RECOMPUTED IT FROM THE MARKUP AND THE RECORDED FIGURE IS RIGHT, WITH ONE QUALIFICATION THAT
MATTERS.** The mark sits at three levels and they mean three different things. **A row-level mark says
the allocation itself is absent from officially released data. A cell-level mark says the allocation is
official and its stated purpose is the compiler's. A span-level mark says part of the description is
official wording and part is not.** Measured that way the research series is **21 fully official, 7
cell-marked, 2 row-marked and 1 span-marked**, which sums to 31 and reproduces the recorded twenty-one,
nine and one **only if wholly unofficial merges the row-marked and the cell-marked**.

**SO THE RECORDED NUMBER WAS CORRECT AND THE CATEGORY IS TOO COARSE FOR SOME USES.** A364's central
comparison is between the XQ-58A, whose description is official Department wording, and the XQ-67A, whose
description is cell-marked, **and merging cell with row would have destroyed that comparison.** A364 uses
the four-state split throughout and says so.

**AND A364'S OWN FIRST TWO ATTEMPTS AT THIS MEASUREMENT WERE BOTH WRONG, AT A DIFFERENT LEVEL EACH TIME.**
The first regex captured a cell's inner HTML and discarded the `class` attribute, so every row read as
official. The second read the cell and missed the mark on the `<tr>`. **A confident wrong count twice
over, from a parser that could not see its own evidence.**

**RESOLVED 2026-10-02 as `442fc41`.** The pilot chose in-place repair over the errata convention.
Both drafts now state the three-way split of 21, 9 and 1, A358's chronology claim is scoped to the
rows the register dates in full because the two row-marked rows carry partial dates, and **A360's two
passages narrating the sister drafts' errors were rewritten to make the same argument impersonally**,
preserving its recomputation, its table and its conclusion. Every repaired figure was recomputed from
the register before the edit and asserted after it. **The editorial fork that kept this open for six
articles was A360's narration**, and the resolution cost was exactly the two paragraphs predicted.

### RESOLVED on 2026-10-02, applied on the pilot's decision. Corrupted mathematics in published posts

**THE RECORDED FIGURE WAS SEVENTY-TWO SOURCE-SIDE PAIRS ACROSS THIRTY-EIGHT FILES AND A363 MEASURED
IT IN THE RENDERED PAGES INSTEAD.** `tmp/a363/mathcorpus.py` reads every built page and counts what
kramdown actually emitted, which is the only authority.

**133 corrupted mathematical spans across 37 pages, of which 104 are underscore-driven and 29 are
asterisk-driven.** The two figures agree once the unit is matched, since one emphasis pair corrupts
two spans. **The heaviest pages are a reinforcement-learning article at nine spans, a reputation
article at nine and a projection article at eight.**

**THE ASTERISK CAUSE IS NEW AND THE EXISTING INSTRUMENT IS BLIND TO IT.** `tmp/a362/emrisk.py`
models kramdown's underscore pairing only. **Kramdown pairs bare asterisks inside inline mathematics
in exactly the same way**, which A363 discovered by writing an inline superscript star twice in one
paragraph and finding an emphasis tag in the rendered expression. **`tmp/a363/astrisk.py` predicts
that cause and reports 57 further paragraphs carrying a single unpaired asterisk, which are latent
rather than broken**, since one more asterisk in the same paragraph would pair with it.

**THE FIX IS MECHANICAL AND VERIFIED IN BOTH DIRECTIONS.** Escape the underscores and the asterisks
that can open emphasis, which kramdown then consumes so MathJax receives the correct LaTeX. **Only
inline spans need it, because display blocks pass through untouched**, which was measured by probing
kramdown directly rather than modelled. `tmp/a362/mathfix.py` performs the underscore half.

**RESOLVED 2026-10-02 as `ea593f0`.** 61 published posts, 313 inline spans, 133 corrupted rendered
spans to 0, the sweep also disarming every latent case. **Rehearsed first in a twin-build pair under
`tmp/mathrepair/` whose comparison caught the fixer escaping a glob star inside a published 2016
GRANT statement**, after which the fixer gates on `mathjax: true` and masks code, and the final twins
differ on 38 pages with every difference inside inline mathematics, proven by blanking the spans and
comparing the remainder byte for byte. The applied tree is byte-identical to the rehearsal and a
fresh production build from it measures zero.

### Resolved since the last handoff

**A361's TWO COMMITS FOR FOUR PASSES.** The previous handoff recorded it as a departure and asked the
next article to keep to one commit per pass. **A362 has four commits for four passes.** The question
of how to handle a long sweep did not need answering, because A362's three sweeps were each short
enough to finish inside a pass.

**WHETHER PRIMARY FRACTIONS ARE COMPARABLE ACROSS THE A360 FETCHER REPAIR.** They are not, and the
three articles since have each reported their own figure with its subject named, which is the
practice that makes the incomparability harmless. **A360 at 30.6 percent, A361 at 45.0 and A362 at
39.5 are three subjects and not a trend**, and each article says so.

### RESOLVED on 2026-09-30. The concurrent session finished and published

**A374 IS PUBLISHED** at `_posts/2026-08-11-published_wargames_of_war_with_china.markdown`, and the
corpus is 302 posts. The shared-tree arrangement held for four passes of A359 and three of A360
without losing a line of either session's work. **The convention that worked, and is worth reusing if
two sessions run again**, was to stage only one's own paths, insert a new history row without
displacing the other's, and say in the commit message that interleaved text rides along because
separating it would destroy it.

**WHAT IS STILL NOT SETTLED IS WHO OWNS `REVERSE_PROMPT.md`.** It is single-writer by design and it
had two writers. **The arrangement that emerged is a dated header describing the latest state,
followed by one section per article, newest first**, with each session rewriting the header and
leaving the other's section intact. A360 followed it and updated the other session's stale note about
verifier warnings in place rather than deleting it. **That is a convention by accident and the pilot
may want to make it one on purpose.**

### PARTLY RESOLVED on 2026-09-30. A360 and A361 are one programme

**THE DIVISION WAS MADE AND A360 EXECUTED IT.** A360 took the programme, the aerospike and the
altitude-compensation mathematics. **A361 has the contractor, the instrumentation, the recovery gear
and the question of what it means for one programme to hold two numbers**, and A360's Out of Scope
section says so explicitly so that a reader is not surprised.

**WHAT REMAINS OPEN IS WHETHER A361 CAN BE BUILT THE WAY THIS SERIES BUILDS ARTICLES.** `Invocon`
returns **nothing at all** from the bibliographic index, `Troy7` returns nothing, and `KT Engineering`
is flooded by a journal with those initials. **Three contractors and no indexed publications between
them.** A361 therefore has no literature of its own to survey under its subject's name, and will have
to be built from the instrumentation and measurement literature plus the award record, where the
recipient name does return decades of contracts. **Raise this before drafting rather than discovering
it in the first sweep.**

### NEW on 2026-09-14. The bandwidth criterion's phase-delay parameter is unresolved

**A359 wanted it and would not use it.** Deriving the phase delay of a pure delay from the
definition as recalled gives half the delay, where the usual summary of the subject says it is the
delay. **A factor of two is not a rounding.** The specification that settles it, MIL-STD-1797 or its
handbook, **has not been read and is not in the corpus.** Any later article that wants to express a
delay as a handling-qualities level must read it first.


### NEW on 2026-09-13. Two published-chain drafts show anchor slugs where titles belong

**A356 AND A357 EACH SHIP FIFTY-EIGHT REFERENCE-LIST ENTRIES WHOSE VISIBLE LINK TEXT IS A RAW ANCHOR
SLUG**, reading `related_post_a297_framing` where the article title belongs. **Verified still live on
2026-09-13**, and confined to exactly those two files.

**The cause is a scraper and it is worth understanding because the shape recurs.** Each article read
its predecessor's bullet list to recover the labels. **A355 shipped no Related Post section at all**,
so A356's scraper matched nothing and fell back to the anchor, and A357 then read A356's slugs and
round-tripped them. **A fallback that cannot fail is not a fallback.**

**A358 broke the chain** by building its labels from the roster embedded in this file and asserting
that every anchor resolves to a title, so the defect does not propagate further. **The two affected
drafts are not touched**, because that is a change to finished articles and the standing rule is that
the agent works on the article in hand.

### NEW on 2026-09-13. `check_any.py` now fails corpus-wide and is not the gate

**It reports 14,613 failures across 62 articles.** Its math rules refuse the three-line display fence
that every article in this corpus uses, and it reads LaTeX spacing such as `\;` and `\left(` as prose
punctuation. **A357 trips it 164 times and A358 113 times, entirely on those two classes.**

**Its orphan-definition check is still correct and still useful**, and it found 23 real orphans in
A358 which were then cited. **The instrument needs repair and the articles do not**, and until it is
repaired the real gate is `_verify.py`, a production build and `_lib/render.py`, in that order.

### The citation format, which is the largest of these and is repository-wide

**EVERY ARTICLE IN THIS SERIES THAT CITES IN BULK WRITES `[[text][anchor]]` AND PAYS FOR IT.** A357
measured the cost at 226.02 seconds against 0.70 for the escaped form `\[[text][anchor]\]`, on
identical content with identical rendered output. **Several sibling drafts carry thousands of these**,
one of them with 4,544 citations on a single line, and each is paying the same backtracking cost in
every build.

**A357 fixed only itself and A358 followed it**, escaping the outer brackets everywhere including
hand-written prose, and its rendered page carries zero escaped-bracket artefacts. **So two articles now
use the escaped form and the rest of the series does not.** The change is mechanical, the rendered
appearance is unchanged, and the corpus survey-row check reads `][anchor]` either way so it keeps
working. **It is a change to finished drafts rather than to the article in hand**, so it is recorded
here for the pilot rather than done.

**Three repairs need the pilot rather than the agent. All three were verified still live on
2026-09-13**, the duplicated heading at lines 412 and 414 of the X-53 draft and the malformed
`book_jenkins` label at line 4275 of the X-27 draft. `x_planes_boeing_x53_active_aeroelastic_wing.markdown` still carries its duplicated
heading at lines 412 and 414, and A324 still carries its malformed book label. **The agent has not
raised either again during A352 through A356 because neither is inside the article in hand**, which is
the standing rule and the reason they persist.

### NEW on 2026-09-10. Four articles are outside a corpus check that reads their format

**`_verify.py` gates a survey cluster row against its own citation count by matching a line that
begins with the record count in bold and carries the citations on the same line.** Thirteen articles of
this series used exactly that format, being A339 through A351, and A356 uses it again.

**A352, A353 and A354 state no per-cluster count at all, and A355 states it inside a sentence with the
citations on the line below, which the rule cannot read.** Nothing is ungated, because each article's
own verifier recomputes the same agreement from its own reference data. **But roughly fifty rows sit
outside a corpus-wide check that would read them if they were reshaped.**

**It is not repaired**, because all four are complete on their four passes and editing a finished
article during another article's work mixes two units. **That is the standing rule and it is why this
is a pilot decision rather than an agent action.**

### RESOLVED on 2026-09-04. The book identifiers in A342 through A346 were repaired

**Twelve anchors and sixteen citations replaced**, every one confirmed on title AND author before it
was written, and every old key confirmed wrong before it was touched. The corpus moved from **283 of
300 to 299 of 300 checkable book citations correct**. Eight replacements were already vetted elsewhere
in the corpus, seven in A347 and one in A324, and four were resolved by fresh search.

**The measurement that made the repair possible had to be rebuilt first**, because the previous oracle
reported correct citations as broken. See the method rule above.

### The report server serves ten records per query, and A355 showed what to do about it

**MEASURED ON 2026-09-09 AND NOT INFERRED.** A direct query for `X-57 Maxwell` reports seventy-four
matching records in its own `stats.total` and returns ten. **Asking for a hundred returns ten. Asking
by offset returns the same ten again**, at every offset tried from ten to seventy.

**A HYPOTHESIS ABOUT OUR OWN TOOLING WAS TESTED AND DISPROVED.** The suspicion was that
`fetch.ntrs_search` never paginates and was silently losing records in every article of this series.
**It sends the offset correctly and the server ignores it.**

**A355 ACTED ON THIS RATHER THAN RECORDING IT AGAIN, AND IT WORKED.** Its supplementary sweeps asked the
report server 42 questions after the draft's 12, and its contribution to the reference list went from
16 records to 77. **Report coverage is bought with the NUMBER of queries and never with the row count**,
and that is now demonstrated rather than predicted.

**THIS IS NO LONGER AN OPEN DECISION SO MUCH AS A STANDING METHOD.** What remains open is whether a
better interface exists, which this agent has not established. **The workaround is to read the
programme's own index where one exists**, which A354 did for sixty-one documents no query assembled.

### A350 ships a duplicated heading, found while writing A352 and not repaired

**`x_planes_boeing_x53_active_aeroelastic_wing.markdown` carries `## The Contemporary Literature`
twice, at lines 412 and 414.** It was found while comparing section structures for A352.

**It is not repaired**, because A350 is complete on all four passes and editing a finished article
during another article's work mixes two units. **A351's assembler asserts its own heading appears
exactly once and A352's asserts the same**, so the class cannot recur in a new article. The repair is
a two-line deletion whenever the pilot wants it.

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

**ALL NINE ANOMALY CASES ARE NOW WRITTEN**, the X-58, X-67 and leapfrogged X-69 to X-75 block having
followed at A355, A364 and A366, and X-30 and X-54 are written although neither is one of the nine.

**A366 ADDS TWO THINGS THE CLOSER SHOULD CARRY.** **Design numbers have started to carry messages**, three
founding-year numbers in 329 days, the YMV-75A, F-47A and X-76A, with none before November 2024. **And the
register itself lags the allocations by months**, so the closer's account of what was knowable when must
use first archived appearance rather than allocation date.

**A367 ADDS THREE THINGS THE CLOSER SHOULD CARRY.** **The newest research aircraft is defined by a
solicitation's envelope and a register's engine cell**, and nothing about its mass or drag was public
at its date, which is the documentation pattern of the series' last years. **Both finalists of a
competed X-plane programme carried the same propulsion answer**, so the rule shaped the aeroplane.
**And the contractor's heritage claim counts convertiplane numbers as X-planes**, which the per-mission
rule does not, a confusion of sequences the closer should state once and correctly.

**A358 ADDS THE FINDING THE CLOSER MOST NEEDS, AND IT IS ABOUT THE REGISTER RATHER THAN ABOUT ANY
AEROPLANE.** The register stops being a primary source partway through this series. Its compiler's own
note states that no complete official data on designations assigned after October 2018 is available,
that for later allocations **the official description is no longer releasable to the public**, and that
such entries are therefore shown in blue to mark them as not official Department of Defense wording.
**Of the 31 X rows, the X-60A is the last whose description is official and the X-61A is the first
whose description is not.**

**THAT SPLITS THE SERIES IN TWO AND THE CLOSER SHOULD SAY SO.** Everything from the X-1 to the X-60 can
be read against what the government said the aeroplane was for. **Everything from the X-61 onward
cannot**, and the remaining nine articles are all on the far side of that line. **A blue description is
a narrower claim than an entirely blue row**, which the same note reserves for designations missing from
officially released data altogether, so the date, designation, contractor, engine and sponsor remain
official throughout. **What is withheld is the one sentence saying what the aeroplane was for.**

**AND THE CLOSER SHOULD CARRY A PATTERN ABOUT ORDERING RATHER THAN ABOUT AIRCRAFT.** Three
consecutive articles found the number and the flying decoupled in three different ways. **The X-53 was
designated more than a year after it stopped flying. The X-54 was designated and never flew at all.
The X-55 flew and was designated 139 days later.** None of the three is an anomaly case in the sense
this section means, and together they say something the anomaly cases do not, **which is that the
register records outcomes at least as often as it authorises attempts.**

**A FIFTH ORDERING ARRIVES WITH THE X-62 AND IT IS MEASURED.** The X-62A's row is the only one in
the whole 539-row register whose description uses the word `redesignated`. Eight X rows describe a
modification of an existing aircraft and the other seven say `Highly modified`, `converted`,
`Derivative of` or `Upgrade`. **Only this one says the aeroplane was renamed**, and the aeroplane it
renames had been flying for twenty-nine years. **The X-53 was designated after it stopped flying, the
X-54 was designated and never flew, the X-55 flew and was designated 139 days later, and the X-62 was
an aeroplane with a different designation for a generation before it got this one.**

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
- **X-69 to X-75**, unassigned and leapfrogged, **written at A366**: seven skips made at once for a number chosen to spell 1776.

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

**A359 ADDS THREE TO THE CLOSER AND THE FIRST IS THE STRONGEST THING THIS SERIES HAS ON WHAT A
DESIGNATION IS FOR.** The government allocated the X-62A in June 2021 and then spent 29,085,924.37
dollars on the aeroplane across 73 transactions **without once writing the number down**. The
designation appears exactly once in the whole federal award record and that once falls 23 days past
the article's own editorial date. **A designation is a claim about a vehicle's purpose made by one
part of a government to another, and the part that buys the fuel and the spares had no use for the
claim**, because for its purposes the aeroplane had not changed and the contract line was the same
contract line. **Both records are right and they are answering different questions**, which is a
sharper statement of what the register is than anything the series has had.

**A SECOND, WHICH COMPLETES THE ORDERING TABLE.** The series has now met five distinct orderings
between a designation and its aeroplane: the number first and the aeroplane after, which is most of
the early series; the number after the aeroplane stopped flying, which is the X-53; the number
allocated and no aeroplane ever built, which is the X-54; the number following first flight by
months, which is the X-55; and **the number following first flight by twenty-nine years while the
aeroplane is still flying, which is the X-62A**. **The fifth is the only one in which the
designation records a change of purpose rather than an event in the aeroplane's life.**

**A THIRD, WHICH IS AHEAD RATHER THAN BEHIND AND WHICH THE CLOSER SHOULD NOT LOSE.** The X-63A and
the X-64A were allocated on the same day, to the same sponsor, with the same engines cell, **and
with byte-identical descriptions**, differing only in contractor. **It is the only duplicated
description among the 31 X rows.** Two numbers for one programme, distinguished by who builds them.
**The system is counting contractors there rather than aeroplanes**, which belongs beside the X-44's
two aircraft and the XQ- series drawing from the same pool.

**AND A CORROBORATION THAT CUTS THE OTHER WAY, WHICH THE CLOSER SHOULD CARRY HONESTLY.** A358
established that the register stops being a primary source at the X-61A. **A359 found one of those
unofficial sentences corroborated by a different arm of the same government**, the accounting system
naming the Skyborg programme 108 days after the redesignation. **A reconstruction is not thereby
official and it is corroborated**, which is a weaker claim and a more useful one, and the closer
should not let the register's loss of authority become a blanket refusal to believe it.

**A360 ADDS THREE TO THE CLOSER AND THE FIRST IS A SECOND INSTANCE OF A359's STRONGEST FINDING.**
A359 found a government that allocated an X number and then spent twenty-nine million dollars without
writing it down. **A360 found a government that bought a vehicle with an instrument designed to leave
no trace in the procurement record, and an announcement that says so in advance.** Twelve keywords put
to the federal award system across five families of award type return nothing for this programme
anywhere, because the awards were made through a Space Enterprise Consortium other transaction
agreement, which exists precisely so that a company outside the Federal Acquisition Regulation can be
paid. **A359's silence was an accident of accounting practice. A360's is the point of the
instrument**, and the closer should distinguish them, because together they say that a designation's
visibility in the record depends on which mechanism bought the vehicle.

**A SECOND, WHICH IS THE PAIRED DESIGNATION AND IS NOW MEASURED RATHER THAN NOTED.** The X-63A and
X-64A share an allocation date, a sponsor cell, an engines cell and 101 characters of description, and
**it is the only duplicated description among the 31 X rows**. Eleven descriptions repeat in the whole
539-row register and the other ten are munitions, targets and a ground station. **The system is
counting contractors there rather than aeroplanes.** Two further facts belong with it. **The Space
Force appears in the register's X rows exactly twice and both times are this pair**, so a service that
did not exist when most of the register was written enters its experimental series for two halves of
one rocket programme. **And `1 rocket engine` appears in exactly two of 539 rows**, also these,
against an engines column that otherwise names a model, because at allocation the engine had no model
name and arguably did not exist.

**A THIRD, WHICH IS A CORRECTION TO THIS SERIES' OWN ARITHMETIC AND IS STILL OUTSTANDING.** The
register's officiality markup has three states, not two. Recomputed from the saved page and confirmed
by an independent re-parse of the markup, the split is **436 official, 86 wholly unofficial and 17
partly unofficial across the register, and 21, 9 and 1 across the 31 X rows**. **A358 gave the
register-wide figures exactly right** and then gave the X-row figures as 21 official and 9 not, which
accounts for 30 of 31 rows because the partly marked one has nowhere to go in a two-number summary.
**A359 closed that sum by raising the official count to 22**, which places the partly marked row on
the one side its own markup denies. **A360 states the three-way split correctly and neither earlier
article has been edited.** The repair is one clause in A359 and a third number in A358, **and it is
the pilot's decision because both are pushed.**

**AND A METHODOLOGICAL FINDING FOR THE CLOSER RATHER THAN A FACTUAL ONE.** A360's keystone is an
identity that removes the vehicle entirely, being that ambient pressure is the variable conjugate to
exit area, so the ideal altitude-compensating nozzle's thrust curve is a Legendre transform and a
fixed nozzle's loss is a Bregman divergence. **That is the third consecutive article whose central
result is an exact identity rather than a measurement**, after A358's Bode sensitivity integral and
A359's control-effectiveness projector. **The series is accumulating a second spectrum alongside the
one about how answerable a question was, which is how much of an X-plane's research question can be
settled without the aeroplane.** A360's answer is almost all of it, and the article says so, which is
an uncomfortable thing for a programme that bought a flight.

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
