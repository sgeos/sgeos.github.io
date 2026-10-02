# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

## Last Updated

**Date**: 2026-10-02
**Task**: **A364 EQUATION-DENSITY REVIEW, the second of four passes. Committed, not pushed, NOT
published.** **Display equations 26 to 68**, lines 4,020 to 4,573, words 26,616 to 30,926, inline
expressions 124 to 185, the symbol table 50 entries to 85, references held at 1,164, in 9 H2 and 48 H3
sections with 18 tables.

**A SCAN DROVE THE PASS AND IT FOUND 172 CANDIDATES.** `eqscan.py` lists every prose line carrying a
figure with no display block within six lines, after excluding dates, years, designation numbers,
contract numbers, document numbers and status codes, **because none of those is a result**. The author
then decided which candidates were relations. **The excluded families are measured rather than assumed**,
and the exclusions are why the output was readable at all.

**THE PASS ADDED ONE NEW MEASUREMENT AND IT TESTS THE INSTRUCTION'S OWN DEFINITION OF A DESIGN
NUMBER.** The instruction says the 16 in F-16A is the sixteenth approved designator for a fighter, which
is a claim with a testable consequence. **The ordinal form cannot be tested against this register**,
because it opens in August 1998 and most series were already numbering, **so the claim was differenced**
and each new design number should exceed the previous new one by exactly one. **The research series gives
15 of 22 steps exactly one, or 68.2 percent, and the unmanned series 9 of 29.**

**AND THE FIRST VERSION OF THAT MEASUREMENT WAS WRONG IN TWO WAYS, BOTH NOW RECORDED IN THE ARTICLE.**
It counted the X-40B as a new design number, **which is the register's own edge misread as a government
decision**, since a series letter of B or later is evidence that the number predates the row. And it
conflated skipping with out-of-order allocation, **because an allocation below the pointer makes its own
increment negative and inflates the next one by the same amount.** A second measure was added for that,
the advance of the running maximum, with the identity that the advance is zero exactly when the
allocation is at or below the pointer.

**THE POINTER MEASURE PRODUCES THE ARTICLE'S CLEANEST TABLE.** The research series has 22 steps, **16
advances of exactly one, 5 greater than one and 1 of zero**, and the five gaps are exactly this series'
own five documented losses, being the 49 passed for a round fifty, the refused 52, the borrowed 58, this
article's 67, and the leapfrogged 69 to 75. **Eleven numbers skipped and exactly one ever filled.**

**AND THE RESEARCH SERIES IS THE BEST-BEHAVED SEQUENCE IN THE REGISTER, WHICH SHARPENS THE FINDING.**
Among the three basic missions with at least twenty steps the rates are 72.7 percent for the research
series, 51.5 for missiles and 44.8 for unmanned, against 50.4 percent register-wide. **The X-67 was lost
from the one numbering sequence that mostly does follow the rule.**

**THE PASS'S LARGEST FINDING IS THAT THE RULE CHANGED, AND WRITING DOWN THE RELATION IS WHAT FOUND
IT.** The pointer passed the 49 on 2002-02-13 and the X-49A was allocated 464 days later, filling a gap
the pointer had already crossed. **The joint instruction of 9 September 1994, in force at the time, says
the office will assign the next available consecutive design number**, and a passed number is available.
**The 2020 instruction replaced that with the last approved design number and added a refusal of requests
in reverse or skipped sequences.** So the X-49A is the instruction obeyed under one rule and would be
refused under the other. **The X-67 is the first number in the research series to be skipped under a rule
that makes skipping permanent**, and the X-58's slot was recoverable for its first two years while
nobody wanted it.

**A CLAIM WAS WRONG AND THE ARITHMETIC CORRECTED IT INTO SOMETHING STRONGER.** A draft said the three
competing definitions of the next number all coincided at 67. **The lowest-never-allocated definition
returns 1 over this register**, because the X-1 through the X-36 are outside the window, **so the
quantity the 1994 instruction named is not derivable from the only public source of the thing it
governs.** Of the two definitions that are computable, **both gave 67 on the day the X-68A was approved**,
which is sharper than the claim it replaced.

**THE KEYSTONE'S FORMAL STATEMENT WAS ADDED AND IT IS TWO DIFFERENT FAILURES RATHER THAN ONE.** For a
design number to index a purpose the purpose map must be injective, and **6 of 490 distinct descriptions
are shared across numbers**. For it to index an organisation the maker map must be well defined, and
**27 of 235 mission-and-number pairs name more than one leading firm**. So the purpose map is a function
and is not injective, while the maker map is not a function at all.

**AND THAT EXPOSED A DENOMINATOR THE ARTICLE WAS QUOTING TWO WAYS.** The same 27 numbers are 11.5
percent of all pairs and 26.2 percent of the pairs carrying more than one row. **Both were in the
article and neither named its denominator**, which is now displayed as two fractions with the same
numerator.

**THE COMMONALITY MODEL GAINED ITS DERIVATIVES AND ITS LIMITS, AND THE LIMITS BOUND THE PROGRAMME'S
CLAIM.** The sharing slope tends to minus one as the family grows, so **no family however large saves
more unit cost than the fraction it shares**, which at three fifths is 60.00 percent against the 13.63
percent three species actually reach. Inverting the cost factor for the family size needed, **a thirty
percent saving at those parameters needs about nineteen species on one chassis** and the programme named
two. The linear-penalty curvature is displayed and is negative, which is why that model has no interior
optimum, and **the quadratic threshold's limit is 300 percent**, so a large enough family tolerates a
tripling of cost before an interior optimum appears.

**AND THE REFRESH ARGUMENT GAINED THE DERIVATIVE THAT MAKES IT A CLAIM ABOUT EVERY INTERVAL.** The
shortfall's gradient is 0.08940 per year at a three-year freeze against 0.01238 at fifteen, a ratio of
7.218, **so the first year of delay costs about seven times what the fifteenth does.** The long-freeze
asymptote is also displayed and is within a tenth of a point of the exact value at fifteen years.

**THE SURVEY'S OWN BOOKKEEPING IS NOW RELATIONS RATHER THAN ASSERTIONS.** The pool identity, the
officiality partition into four exhaustive and disjoint states, the absence partition into inside and
outside the register's window, the reference-base partition into four provenances, the coverage ratio,
the report-primary share and the mean clusters per record. **Each is asserted in the verifier**, so a
record or a row falling into none of a partition's parts, or into two, fails the build rather than
quietly changing a total.

**FOUR SYMBOL COLLISIONS ARRIVED WITH THE PASS AND THREE WERE RESOLVED BY RENAMING.** The pool took a
capital pi because the part count is $P$, the cluster set took a script form because the common part
count is $C$, the discriminant took a capital theta because $\Delta$ is a difference throughout, and
**a row inside the well-definedness condition took $w$ because $r$ is the progress ratio.** Three further
pairs differ only in case and the article says so, since $D$ counts refused records while $d$ is a design
number.

**AND `symcheck.py` HAD A BLIND SPOT THAT THIS PASS WOULD HAVE WALKED STRAIGHT PAST.** It treated
`\mathcal` as structural and stripped its contents, **so every script letter was invisible and the five
new script sets this pass added would have been validated by nothing.** It now keeps the script form as
a compound token, and it immediately reported four undeclared sets. The symbol table is 85 entries and
every token resolves.

**VERIFICATION.** `verify_numbers.py` **322 checks**, passing, up from 256, **with every new gradient
re-evaluated by a central difference on the function it is the gradient of, every limit by evaluation at
ten to the fortieth, the inversion by a round trip through the forward relation, and the increment and
pointer walks redone with a different loop and sort key.** The two walks are asserted to agree on their
step count. `_verify.py` **0 errors and 0 warnings across 304 posts**, the two `progress-stale` warnings
having resolved themselves when the other line published its series. `_lib/render.py` no findings across
538 pages. `mathrot.py` **68 source display blocks against 68 rendered brackets** with zero emphasis
tags. `stylecheck.py` zero findings. `emrisk.py` and `astrisk.py` both confirm the article adds nothing
to the corpus-wide corrupted-maths count.

**THREE VERIFIER DEFECTS WERE FOUND BY IT FAILING, WHICH IS THE PATTERN THIS SERIES KEEPS MEETING.** The
emitter divided the pointer's eleven skipped numbers by the allocation rate where the prose defines the
quantity over the ten numbers actually absent, **the difference being the X-49 which the pointer skipped
and which is present in the register.** A limit check at ten to the ninth failed by three quarters of a
percent, because the sharing slope goes as a power of 0.2345 and a billion is not large at that
exponent. **And a tolerance derived from the last printed digit failed on a correctly rounded figure**,
because the computed value carried floating-point noise eight parts in a billion beyond the exact half.

**THE WORKING TREE CARRIES EIGHT DRAFTS THIS LINE DID NOT TOUCH.** `android_development_on_freebsd`,
`android_unit_testing`, three `claude_code_getting_started` drafts, `phoenix_json_api_authentication_with_guardian`
and two solana drafts have been re-dated from 2026-08-14 through 21 to **2126**, a century forward, day
and time preserved. **They are uncommitted, they are not this line's work, and they are excluded from
this commit.** The untracked `sa.html` is excluded as before.

**Date**: 2026-10-02
**Task**: **A364, X-Planes: X-67, the Slot Taken by XQ-67A, DRAFTED.** Committed, not pushed, and
**NOT PUBLISHED**, publication of the series never having been authorised. **Sixty-eight of
seventy-two drafted, four remain.** The three remaining passes on this article are equation density,
primary references and the publication review.

**STATE 4,020 lines, 26,616 words, 26 display equations, 124 inline expressions, a 50-entry symbol
table and 1,163 reference definitions**, in 9 H2 and 42 H3 sections with 16 tables, citing 1,081
research records across 15 clusters from a pool of 9,505 distinct records. **This is the shortest of
the four designation anomalies and that is deliberate**, the genre document being explicit that
padding an anomaly article is worse than leaving it short.

**THE KEYSTONE IS THAT THE REGISTER'S ENTRY FOR THIS DESIGNATION IS AN ANALOGY.** The compiler writes
that just like the X-58 the slot was skipped after the allocation of the XQ-67A, and that is the whole
of the public reasoning. **The X-58's entry carries reasoning, a confidence grading and the claim that
the slot is empty. The X-67's carries none of the three.** His treatment of the rest of the family
shows he is not being careless, since he writes `unclear` for the XRQ-72A and `probably` for the
XRQ-73A. **He is citing a precedent rather than withholding an argument**, and the X-67 is the point
at which a precedent becomes a rule.

**SO THE ARTICLE HAD TO SUPPLY THE EVIDENCE THE REGISTER ASSERTS WITHOUT, AND THERE IS A TEST.** A
borrowed number should equal its claimed source series' next number at the moment of the borrowing and
should equal no other series' next number. **Run against every out-of-sequence unmanned design number
carrying a full date, the test fires twice in six, on 58 and 67, naming the research series both times
and matching nothing on the other four.** A null model drawing uniformly from two-digit numbers above
the unmanned ceiling gives a tail probability of 0.03159, about one in 31.7, **which the article
reports as weak alone and decisive in combination with three other facts.**

**AND THE INSTRUCTION SHOWS THE QUESTION OF WHO SKIPPED IT IS MALFORMED.** Two sentences neither the
X-58 article nor any other in this series had cited. The request procedure defines the next designator
from **the last approved design number** of the same basic mission, and the eligibility criteria state
that **requests are not accepted for designators in reverse or skipped sequences**. **Nobody had to
decide to skip the X-67. Somebody had to ask for the X-68**, 763 days later, and from that approval
the number was unrequestable for ever. **The X-58 article concluded the absence was permitted and
unexplained. This one adds that it is irreversible by rule and names the moment it became so.**

**THREE READINGS OF THE X-68A AND THE RECORD CHOOSES NONE.** That the design-number pool is shared
across basic missions in practice, which the instruction's own definition denies. That the allocating
office exercised its unconditioned discretion to skip. That the pointer was read off a list sorted by
design number within a vehicle type, which places the XQ-67A among the sixty-sevens. **All three
predict an X-68A, no X-67 row and no public document**, so the article states that the slot is
unrequestable, states when, and declines to say who.

**AND THE COMPILER'S OWN NEXT-NUMBER FIGURE CANNOT SETTLE IT, BECAUSE IT PRESUPPOSES THE ANSWER.** He
publishes the next available research number as 69 while the register carries an X-76A, so his
convention is one above the highest number **he judges** to have been allocated in sequence. **He
applies it consistently across the research, unmanned and fighter series, which is the test of whether
it is a convention or an error**, and it is not the convention the instruction states. Read literally
the instruction gives 77.

**THE SECOND CASE FALLS ON THE FAR SIDE OF A LINE THE FIRST DID NOT, AND THIS IS THE DEEPEST
DIFFERENCE.** The XQ-58A's description is official Department wording and the XQ-67A's carries the
mark saying it is not. **So in 2017 the government said what the aeroplane taking the number was for
and in 2023 it did not.** What survives the mark is the date, the designation, the contractor and the
engine. **The government will officially record which engine is in the aeroplane that consumed the
X-67 and will not officially record what it is for.**

**THE AEROPLANE WAS BUILT TO DENY THE PREMISE THE NUMBER RESTS ON, AND THAT IS WHY IT IS IN THE
ARTICLE AT ALL.** A design number marks a major design change within a basic mission, presuming one
design identity. The Off-Board Sensing Station existed to prove a common chassis carrying replaceable
species, which the laboratory called a genus and species approach in those words. **By the
instruction's own criterion a species belongs on a series letter**, the only concrete test it offers
for that level being whether the change alters the logistics support of the vehicle, **and a common
chassis is built so that it does not.**

**THE REGISTER SHOWS THE SAME THING FROM BOTH SIDES AND BOTH MEASUREMENTS ARE NEW.** Six pairs of
design numbers in the whole register carry identical official descriptions, and in five of the six the
contractor is the only differing field, so the number does not index the stated purpose. **Yet 27
design numbers survive a change of leading firm, one of them across seven firms and ten series
letters, so it does not index the designer either.** What it indexes is a request, and the instruction
never defines what a request is for.

**THE ARITHMETIC IS NEW TO THIS SERIES AND SAYS THE VALUE WOULD LIE IN THE CADENCE RATHER THAN THE
PARTS.** At three species and an eighty-five percent learning curve a three-fifths shared fraction
buys 13.63 percent of unit cost. **A sharing penalty linear in the shared fraction has no interior
optimum at all, which is the model telling the reader about its own linearity**, and a penalty rising
as the square has one only above three times the square of the sharing slope, 15.47 percent at three
species. **At a thirty percent penalty the optimum shared fraction is 44.63 percent, saving 4.76
percent, while full commonality is 0.48 percent worse than sharing nothing.** By contrast shortening
a design freeze from fifteen years to three takes the capability shortfall from 80.87 to 37.82
percent. **Every input to both calculations is unpublished and the article inverts the break-even
rather than asserting a saving it cannot measure.**

**THE AWARD RECORD CONTRADICTS THE REPORTED CONTRACT VALUES IN BOTH DIRECTIONS AT ONCE.** Trade
coverage reported matching 17,700,000 dollar contracts with a 49,000,000 dollar ceiling. **The award
record shows one at 67,986,112 dollar, 38.75 percent above that ceiling, and the other at 16,003,302
dollar, 9.59 percent short of its base.** One contract grew past the maximum its own option defined
and the other stopped before its minimum. **And the laboratory's own account of deciding at the end of
2021 disagrees with contemporary reporting placing the selection in February 2023**, by about a year,
which the article names and does not resolve.

**THE INSTITUTIONAL FINDING IS LARGER THAN THE DESIGNATION.** The request procedure requires research
into the last approved design number in an official source. **The printed list was cancelled in 2018,
and the hostname its cancellation notice named as successor returns no answer from the authoritative
nameservers for its own zone**, checked on 2 October 2026 with a sibling in the same zone resolving
normally. **The article states the narrow version**, which is that the official source is not reachable
publicly at the address its own cancellation notice named, since a Department network may resolve
internally. **So every public claim about the X-67, including every claim in this article, passes
through one private compiler's reconstruction obtained under the Freedom of Information Act.**

**AN OPEN DECISION IS RESOLVED AND THE RECORDED FIGURE WAS RIGHT.** The research series' officiality
split recomputes as 21 official, 7 with an unofficial description, 2 entirely unofficial rows and 1
partly, which agrees with the recorded twenty-one, nine and one **provided wholly unofficial merges
two different claims.** A row-level mark says the allocation itself is absent from officially released
data; a cell-level mark says the allocation is official and its stated purpose is the compiler's.
**The recorded figure is correct and the category is too coarse for this article, because the XQ-67A
is in the second group and that distinction is the whole comparison.**

**TWO MEASURED NEGATIVE RESULTS, BOTH REPORTED RATHER THAN HIDDEN.** The reports server holds 745
records across 62 questions and the sweep retrieved all 745, **which is the first complete coverage in
this series and a statement about the server rather than the sweep.** The report-primary share is 9.5
percent, the lowest recorded, against 30.6, 45.0, 39.5 and 28.3 in the preceding four articles,
because commonality and product family design are a manufacturing and management literature. **And the
programme's own vocabulary is unsearchable**, `common chassis aircraft` returning one record about a
different vehicle, `attritable aircraft` returning none, `genus` and `species` returning forty
biological and chemical results in forty, and `OBSS` returning ten about the Space Shuttle's Orbiter
Boom Sensor System.

**FIVE DEFECTS FOUND, AND FOUR OF THE FIVE WERE THE INSTRUMENT RATHER THAN THE SUBJECT.** A remembered
digital object identifier was written into the reference file **in the belief that it was correct** and
resolves to nothing, the real one having been in the harvest throughout, which is A363's placeholder
defect in a worse form because no rule about placeholders catches it. The subject gate **refused the
article's own foundational source** because its title carries no engineering noun. A frozen occurrence
count **returned zero for a phrase plainly in the article**, the body being hard-wrapped so the phrase
carries a newline. An inherited display-equation counter saw only one-line blocks and reported zero
against twenty-six. **And an officiality parser read one of the register's three markup levels and
reported a confident wrong count twice, at a different level each time.**

**VERIFICATION.** `verify_numbers.py` **256 checks**, passing, importing neither the measurement module
nor the derivation module and **parsing the register again with a different parser**, with the null
model's tail probability checked a second time by simulation and the commonality optimum found by a
golden-section search that does not know the first-order condition. `_verify.py` 0 errors and no new
warnings. `_lib/render.py` no findings across 550 pages. `mathrot.py` matching 26 source display
blocks against 26 rendered brackets with zero emphasis tags in any expression. `symcheck.py` passing
across 50 declared symbols after four collisions were resolved. `stylecheck.py` zero findings.
`emrisk.py` and `astrisk.py` both confirm the article adds nothing to the corpus-wide corrupted-maths
count. **Fifteen hand-written addresses, eleven fetched, four confirmed against the bibliographic
index after a publisher refused the client, and one returning neither**, that one being the
Department's own cancelled list which the article records as not read.

**A NOVELTY OVERCLAIM WAS CAUGHT AFTER THE FIRST COMMIT AND CORRECTED IN PLACE.** The article had
said that neither of the two instruction sentences it quotes had been cited by any earlier article in
this series. **Grepping every draft and post refutes half of it**, the X-58 article having cited the
research step in its non-standard-aircraft branch. **The eligibility criterion refusing requests in
skipped sequences is the one that is new, and it is also the one the irreversibility argument rests
on**, so the correction narrows the claim without weakening the argument and the article records it.

**TWO ITEMS REMAIN FOR THE PILOT AND BOTH ARE OLDER THAN THIS ARTICLE.** The corrupted mathematics in
published posts, re-measured by A363 in the rendered pages as 133 spans across 37 pages. And the
publication decision on A376, which is line two of the handoff. **The A358 and A359 officiality
correction is resolved above.**

**Date**: 2026-10-02
**Task**: **A376 IS PUBLISHED and the `war_with_china` series is complete at three articles.**
Published on the pilot's instruction as
`_posts/2026-08-13-balance_of_power_after_war_with_china.markdown`, following a pathological word
usage pass in which **the enumerated tic class came back clean against 259 peers** and one
discovered formula was over the limit and is now under it. See the A376 sections below.

**THE PUBLICATION USED THE TWO-COMMIT PATTERN.** The draft commit is `3ce299f` and the move is its
successor. **A374 and A375 now read Part 1 of 3 and Part 2 of 3 and neither URL moved**, so no
`redirects/` entry is owed. **The `progress-stale` warnings are gone**, not by a tooling change but
because the two-concurrent-series condition that produced them no longer holds. `./_check.sh`
reports **0 errors and 0 warnings across 304 posts**, a clean build, and no rendered findings across
469 pages.

**ONE ITEM REMAINS OPEN ON THIS LINE AND IT IS NOT MINE TO DECIDE.** Commits `1dd90d0` and `33fd7fe`
carry this line's staged work under the other line's commit messages. The content is intact and
verified byte-identical on the remote; only the attribution is wrong, and the history was
deliberately not rewritten because those commits are pushed.

The previous report follows.

**Date**: 2026-10-01
**Task**: **A363, X-Planes: Boeing X-66, ALL FOUR PASSES COMPLETE.** Committed and **PUSHED** on the
pilot's instruction. **NOT PUBLISHED**, and publication of the series has never been authorised.
**Sixty-seven of seventy-two drafted, five remain.**

**FINAL STATE 10,795 lines, 59,564 words, 83 display equations, 188 inline expressions, an 84-entry
symbol table, 4,537 reference definitions, 21 H2 and 60 H3 sections and 24 tables**, citing 4,436
research records across 17 clusters with 1,256 report primaries at 28.3 percent, a period count of
1,790 at 42.6 percent, median year 2012 and a range from 1921 to 2026. **Four commits for four
passes**, which is the rhythm the handoff asks for.

**THE PUBLICATION REVIEW FOUND THE ARTICLE CONTRADICTING ITSELF, WHICH IS THIS SERIES' RECURRING
DEFECT.** A heading read *Three Things the FY2026 Supplement Says That Nothing Else Does* and the
first of the three was that it uses a word the agency's press item avoided. **The same paragraph
then conceded that the press item uses that word too**, for a different object. The concession was
right and the heading and lead were wrong. Both were rewritten and the honest statement now leads.

**THIRTEEN RANKINGS WERE SCOPED TO WHAT THE ARTICLE MEASURED AND ONE WAS SIMPLY FALSE.** It called
the centroid argument **the only independent confirmation** of a closed form that the same paragraph
confirms twice. It called the fold **the single largest number in this article** when the article
carries a ratio of 10,316. It ranked an input, a service to the reader, a thing an assertion can do,
and the most interesting passage of a contractor report. **Each now names its comparison set, is
marked as a judgement, or is gone.**

**AND A FACTUAL ERROR IN AN AERODROME CODE.** The article had the Boeing 747-8 at Code E. **It spans
about 68.4 metre, which is in the 65-to-80 band and is therefore Code F.** The aeroplane that reaches
Code E is the 777X with its wingtips folded, which the same sentence already named. **The corrected
passage is stronger**, because the 777X folding across a code boundary is precisely the manoeuvre
this article says the X-66A would need, and it is already certificated.

**THREE COMPUTED FIGURES WERE TYPED AS LITERALS AND ARE NOW SLOTS**, being the before-sweep primary
share and the gate's own pattern and test-case counts. **That is the A362 defect class**, where one
hard-coded pool size went stale by two thousand records and the publication review had to find it by
hand.

**FOURTEEN SMALL COUNTS ARE NOW SPELLED AT THE EMITTER RATHER THAN IN THE PROSE**, so the convention
cannot drift when a count changes, and the verifier reads them back through the shared library's
words-to-integer helper.

**DICTION WENT FROM ONE WORD ABOVE THE PEER MAXIMUM TO ZERO.** `fairly` appeared three times where no
peer in seventy-five used it once. **It was not a hedge but the report's own criterion**, so the three
uses were varied across a rotation rather than deleted, to an equal footing, like-for-like, and on
equal terms.

**FOUND CLEAN.** Prose style, with every parenthetical and both semicolons outside maths proving to be
inside block quotations except one statutory subsection citation that cannot be written otherwise.
Structure, all twelve of the genre's sections present and in order among twenty-one. The dateline,
with every post-dateline year proving to be a future date stated by a primary document. Reference
integrity, with no anchor undefined and no definition unused.

**VERIFICATION.** `verify_numbers.py` **158 checks** and `neweqns.py` **94 checks**, both passing,
the latter importing neither the calculation module nor the equation pass's own. `_verify.py` 0
errors and no new warnings. `_lib/render.py` no findings across 549 pages. `mathrot.py` matching 83
source display blocks against 83 rendered brackets with zero emphasis tags in any expression.
`symcheck.py` passing across 84 declared symbols. **Thirty-five hand-written addresses, 25 reached
and 10 refused by one publisher's bot policy, every one of those ten verified in the registry by
title, venue and year.** `emrisk.py` and `astrisk.py` both confirm A363 adds nothing to the
corpus-wide corrupted-maths count.

**TWO ITEMS REMAIN FOR THE PILOT AND BOTH ARE OLDER THAN THIS ARTICLE.** The A358 and A359
officiality correction, now surviving five articles. And the corrupted mathematics in published
posts, which this article's new instruments have **re-measured in the rendered pages as 133 spans
across 37 pages, 104 underscore-driven and 29 asterisk-driven**, where the recorded figure was 72
source-side pairs and the asterisk cause was outside the existing instrument's model entirely.

The older reports follow, newest first. **Nothing below this block was rewritten.**

---

## A376, Pathological Word Usage Pass

**Lines 4,442 to 4,440, author prose 21,118 words once quoted material is excluded.** Display
equations held at 89, references at 202. **NOT PUBLISHED.**

**THE ENUMERATED TIC CLASS IS CLEAN AND THAT IS THE MAIN RESULT.** Against **259 published peers**,
**zero of the seventy watched tic words reach the corpus maximum**. `specific`, the word that caused
the original corpus-wide problem, stands at **3 uses and 0.13 per thousand against a natural rate
near 1.7**, so the article is below ordinary usage rather than above it. The seventeen words that do
exceed every peer are all subject nouns, and each was checked by collocation rather than asserted
clean. `great` is 71 percent `great power`, `share` carries six distinct content modifiers, `median`
four. Those are the documented term-of-art signature.

**WHAT THE ENUMERATED CHECKS COULD NOT SEE WAS A SENTENCE SHAPE.** `tics` tests seventy known words
and `report` tests twenty-two known constructions, so a formula peculiar to one article is invisible
to both. Scoring every repeated sequence against the peer maximum found **`which is a` at 1.37 times
the highest rate in any article this author has written**, carried by `which is a reason to` five
times and `which is a defensible X` four times. A second family, `worth noting` and `worth stating`
and their relatives, stood at **1.02 times the maximum with its head member used by no peer ever**.
**Both are now under the maximum**, at 18 and 2 uses, across 29 edits.

**A QUOTATION IS OTHER PEOPLE'S WORDS AND THE INSTRUMENT WAS COUNTING THEM AS MINE.** `prose` strips
reference link text on exactly that ground and keeps block quotations. With 124 of them, **7.0
percent of what the instrument attributed to the author was quoted material**, and the bias runs one
way, because a larger denominator lowers every rate and a lowered rate hides a tic. Every figure
above was recomputed with quotations stripped from **both** sides, since correcting only the article
is the opposite error. **The clean verdict survived the correction**, moving `rather` from 0.86 to
0.94 of the maximum without crossing it.

**I BROKE THE ANTI-SUBSTITUTION RULE WHILE OBEYING IT.** Four of the replacements reached for `should
therefore be`, turning a construction used once into one used four times. Only diffing the introduced
phrases against the original caught it, and two were varied back. **Checking the target construction
alone reports success**, which is why the rule now says to re-measure what the edit introduced.

**TWO EDITS WERE GRAMMATICALLY WRONG AND ONE DROPPED A CLAIM.** Two replacements hung an independent
clause off a relative clause, which the originals did not do, and were repaired. One conjoined two
facts where the original asserted a causal relation between them, and the relation was restored.
**All three were found by reading the passages, not by any check**, which is the standing limit on
this kind of pass.

**TWO MEASUREMENTS WENT INTO THE LIBRARY RATHER THAN A SCRATCH DIRECTORY.** `diction.py` records that
its predecessor was lost after being copied into four article directories, so `author_prose`,
`quoted_share` and `phrase_outliers` are now in `_lib/diction.py` with a `formulas` CLI mode and
**four new tests, 124 of 124 passing**. **`prose` is deliberately unchanged**, because every rate
`_verify.py` has reported and every exemption reason recorded against one was measured with
quotations included. **`_verify.py` output and `tics` output were diffed before and after and are
byte-identical**, so the other line sees no change.

**NOT ACTED ON, WITH REASONS.** `sets out the` sits at 1.93 times the maximum on **2 uses** against a
peer maximum of 0.05 per thousand, which is small-number noise. `which is not` at 1.13 on 4 uses, all
four substantively different. `this article` at 84 uses is heavy self-reference but 0.83 of the
maximum, and `rather than` at 98 is the article's core contrast device at 0.93. **Acting on those
would be churn, and an unactioned measurement is only acceptable with a reason recorded.**

**VERIFICATION.** `_verify.py` 0 errors and the same 2 known `progress-stale` warnings. Scratch
production build with A376 staged as a post, **469 pages, `_lib/render.py` no findings**. **89 source
display blocks against 89 rendered brackets.** Inline dollar parity even at 24. No unresolved
reference pair, no unrendered Liquid, no raw delimiter. No em-dash, en-dash, semicolon, parenthesis
or contraction in any added line.

## A363, Publication Review

**Lines 10,784 to 10,795, words 59,517 to 59,564.** Display equations held at 83, references at
4,537, the symbol table at 84. Committed and **PUSHED**. **NOT PUBLISHED.**

### The Article Contradicted Itself and the Heading Was the Wrong Half

**A heading read *Three Things the FY2026 Supplement Says That Nothing Else Does*, and the first of
the three was that the supplement uses the word pause where the agency's press item avoided it.**
Three sentences later the same paragraph conceded that the press item uses the word too, applied to
the flight-demonstrator work rather than to the project. **The concession was correct and the
heading and the bold lead were not.**

The heading is now *Three Things the FY2026 Supplement Says Plainly*, and the lead states what is
actually true, which is that **the agency used both words on the same day for different objects and
the budget document is the one that says so without a headline over it.** This is the defect class
this series keeps meeting, an article refuted by something it says about itself a few lines later.

### Thirteen Rankings Scoped, and One That Was False

**One was not a scoping problem but an error.** The article called the centroid argument **the only
independent confirmation** of the root-moment closed form, in a paragraph that goes on to report a
second confirmation by quadrature at six stations. **It is one of two and now says so.**

**One was false on its face.** The fold was **the single largest number in this article**, which
carries a ratio of 10,316 to one and a factor of 18.17. The intended claim was about effect size and
it now reads **the largest aerodynamic effect this article computes**.

**The rest named no comparison set.** The induced-drag fraction was **the single most important
input** and is now one of the two quantities every condition is written in. Reading three budget
books was **the only way** to see the money and is now the route this article took. A declared
symbol table was **the only instrument this corpus has found** that catches a collision and now
simply catches them. Setting three figures side by side was **the most useful service this article
can perform** and is now what a reader needs. An assertion refuting its own docstring was **the most
useful thing an assertion can do** and the sentence survives without the ranking. The aeroelastic
passages were **the most interesting single thing** in the report and are now the ones this article
found hardest to summarise. The flutter margin was **the single largest soft spot** and is now the
only named soft spot that could change the exponent rather than the coefficient, **which is the
reason, and the reason is what was missing.**

**Two rankings were kept with their reasons attached.** The gate-box claim is now explicitly an
inference and the one the article would defend first **because a reader can check it in one line**.
The homonym measurements now carry outside the subject **because the registries do not change
between articles**, rather than being the most transferable thing in the article.

### A Factual Error in an Aerodrome Code

**The article placed the Boeing 747-8 at Code E.** It spans about 68.4 metre, the Code F band runs
from 65 to 80, and the 747-8 is therefore **Code F**. The aeroplane that reaches Code E is the
**777X with its wingtips folded**, at about 64.8 metre against 71.8 unfolded, and the same sentence
had already named it for a different purpose.

**The corrected passage is stronger than the error was.** A wide-body that folds its wingtips across
a code boundary is precisely the manoeuvre this article argues the X-66A depends on, **and it is
already certificated**, which is the best available reason to think the gate box is negotiable for
an aeroplane worth negotiating for.

### Three Literals That Should Have Been Slots

**A362 shipped a stale pool size because one figure in the article was a hard-coded literal rather
than a slot, and the publication review had to find it by hand.** This pass scanned every numeric
literal in the prose mechanically, excluding quotations, tables, maths, dates, designations and
instrument numbers.

**Three survived the exclusions as computed quantities.** The primary share before the third sweep,
and the gate's own pattern count and its two test-case counts. **All three are now emitted**, so a
change to the gate or a re-run of the sweep cannot leave the prose behind.

**One more was a citation gap rather than a staleness risk.** The demonstrator's span of 145 feet was
attributed to trade coverage with no reference, and now says in terms that it comes from secondary
aerospace coverage and **from no primary document this article has read**.

### Small Counts, Spelled at the Emitter

**Fourteen small counts were numerals where the convention asks for words.** The fix is applied in
`emit.py` rather than in the prose, so the convention holds when a count changes, and
`verify_numbers.py` reads them back through `_lib/survey.py`'s words-to-integer helper rather than
parsing them as integers. **A convention enforced in prose is a convention that drifts.**

### Diction, One Word and Not a Hedge

**`fairly` appeared three times and no peer in seventy-five used it once.** Inspection showed it was
not a hedge but the Phase IV report's own criterion, rendered as *done fairly*, *made fairly* and
*made fairly* again. **The word carried meaning and the phrasing repeated**, which the style guide
says to fix by varying across a rotation rather than by substituting one replacement. The three now
read **put on an equal footing**, **like-for-like** and **on equal terms**. Diction reports zero
words at or above the peer maximum, and the one construction above the corpus maximum is *in other
words*, inside a quotation.

### What Was Found Clean, With the Exceptions Named

**Prose style.** Zero em-dashes, en-dashes, contractions and prose colons. **Nine parentheticals and
two semicolons, every one of which proved to be inside a block quotation or the mandated debug tag,
except a single statutory subsection citation** which cannot be written otherwise.

**Structure.** All twelve of the research-aircraft genre's sections present and in the prescribed
order among twenty-one, with the Epistemic State, Out of Scope and Conclusion in the last three body
positions and References last.

**The dateline.** Fourteen prose years after December 2025, every one of them a future date stated
by a primary document, being the agreement's seven-year term and its milestone schedule, the budget
books' out-year projections and the Ames paper's 2035 technology level.

**Reference integrity.** No anchor used without a definition and no definition unused, checked in
`verify_numbers.py` rather than by eye.

### Verification

`verify_numbers.py` **158 checks**, `neweqns.py` **94 checks**, both passing. `_verify.py` 0 errors
and no new warnings across 303 posts. The stub build succeeds against checksum-matched bytes.
`_lib/render.py` reports no findings across 549 pages. `mathrot.py` matches 83 source display blocks
against 83 rendered brackets with zero emphasis tags. `symcheck.py` passes. `stylecheck.py` reports
only the statutory citation. **Thirty-five hand-written addresses, 25 reached and 10 refused by one
publisher's bot policy, all ten registry-verified by title, venue and year.**


## A363, Primary-Reference Review

**4,064 reference definitions to 4,537, report primaries 1,035 to 1,256, the primary share 26.1 to
28.3 percent, the period count 1,641 to 1,790, and the record base's earliest year 1930 to 1921.**
Lines 9,546 to 10,767, words 53,128 to 59,396, tables 19 to 24. Committed, **NOT PUSHED**, **NOT
PUBLISHED**.

### The Aim Was Measured Before the Sweep Was Written

`before_after.py` computed the per-cluster primary share first, which is A362's rule. **The result
named `span_constraint` as the cluster with 37 records and ZERO report primaries**, and it is the
cluster carrying this article's own keystone. The other five thinnest were `aspect_ratio` at 11.9
percent, `alt_config` at 12.1, `gust_loads` at 17.1, `mdo` at 17.9 and `thin_transonic` at 24.1.

**The eighty questions were then written in the report literature's own vocabulary rather than the
subject's.** A journal asks about airport compatibility and a report asks about *airplane
characteristics for airport planning*. A journal asks about multidisciplinary optimisation and a
report names its code, being FLOPS or ACSYNT. **That is the whole difference between a sweep that
buys primaries and one that buys more of what the pool already has.**

**It worked where there was report literature.** `aspect_ratio` went from 11.9 to **23.4 percent**
and from 64 primaries to **167**, `fuel_burn` from 28.8 to **36.2**, `thin_transonic` from 24.1 to
**30.5**, `high_lift` from 32.2 to **36.1**, `mdo` from 17.9 to **20.1**. The pool went from 14,967
to 18,863 and the gated set from 4,238 to 4,744. **And the lifting-line vocabulary reached the
foundations**, bringing in **Munk's 1921 NACA Report 121 on the minimum induced drag of aerofoils**,
a 1922 report on the effect of aspect ratio on lift-curve slope, and a **1935 analysis of a strut
with a single elastic support in the span**, which is this article's jury strut by another name.

### And It Bought Nothing Where It Mattered Most

**Fourteen questions in the airport-planning vocabulary, nine of them returning no records at all,
bought one record and zero primaries.** `span_constraint` is still at exactly zero.

**The honest reading is that this is a fact about where the knowledge lives rather than a failure of
the sweep.** Airport design is a regulator's and an airport planner's subject. It is published as
advisory circulars and aerodrome annexes, not as technical reports, and a research-report server
therefore has almost none of it. **The constraint this article argues is binding has no research
literature because it is not a research question**, and that belongs in the article for the same
reason A362's three-record air-budget result did.

### The Paper the Article Said It Had Not Read

**The Phase IV report's recommendation list asked for an equivalent conceptual-level optimisation of
cantilever and truss-braced aircraft of the same technology level, to allow a more fair and
transparent comparison. A NASA Ames team published it in January 2025 and it is on the reports
server.** The article had cited it from a publisher identifier and said in terms that it had not
read it. **It is now read in full.**

**What it holds equal is the point.** Same payload of 33,750 pound, same 3,400-nautical-mile design
range, same design Mach number, same 2035 technology, same advanced direct-drive turbofan, **same
wing-fold rule above 118 feet**, and **a tube-and-wing weight calibration applied to both** rather
than each contractor's own.

| Mission | Boeing Phase IV | Ames, fuel in wings | Ames, body tanks |
|---|---|---|---|
| 900 nautical mile | 7.2 percent | **1.65 percent** | 5.71 percent |
| About 3,400 to 3,500 | 9.0 percent | 7.51 percent | 9.39 percent |

**Boeing's economic-mission figure is 4.36 times the Ames figure for a wing that must carry its own
fuel.** At the long mission the three agree within a point. **The disagreement is about the mission
and not about the aerodynamics.**

**The two causes it names and ranks are exactly the two the drafting pass had identified and could
not price.** Fuel volume, rated Significant, because the thin high-aspect-ratio wing cannot carry
all the fuel without a significant increase in planform area. Weight calibration, rated Moderate,
because the empty weight and fuel burn both rise under the tube-and-wing calibration.

### A Fourth Independent Route to the Keystone

**Its like-for-like pair is the closest thing to a measurement of the weight elasticity that this
subject's public record contains.** Four readings give **-0.00384, -0.12956, -0.00282 and +0.09926**,
every one below the exact fixed-lift target of **0.299033**, the largest short by **66.8 percent**,
and **three of four negative**, meaning the braced aeroplane at aspect ratio 19.57 weighs less than
the cantilever at 13.

**An elasticity from a pair is not a derivative** and the article says so, because the two aeroplanes
differ in span, area, thrust and altitude too. **What it establishes is magnitude**, and the
magnitude agrees with the three readings computed from the Phase IV group weight statement, which ran
from 0.0775 to 0.2749. **Four routes, one conclusion.**

**And it prices the truss directly against a cantilever of the same technology**, which is the
comparison the Phase IV report said had not been made fairly. Wing plus strut is **24.58 percent**
heavier on the contractor's calibration and **28.10 percent** on the harsher one, while **the wing
alone is only 1.38 and 4.28 percent heavier**. **The strut is almost the whole penalty**, which is a
direct measurement of the derived claim that a geometrically similar truss buys a coefficient rather
than an exponent.

### The Limit on the Keystone's Reach

**The braced aeroplane needs 25.65 percent more sea-level static thrust and cruises 4,250 feet
higher, with a 12.92 percent better start-of-climb lift-to-drag ratio.** The paper says it spends
more time climbing, which pronounces the engine-efficiency differences.

**So the aerodynamic advantage is real and the short mission spends it.** The optimality conditions
derived in this article are cruise-fuel conditions, and **an aspect ratio chosen to minimise cruise
fuel is being chosen against the wrong objective for the mission this class flies most often.** The
article now states that as a limit and does not derive a climb-inclusive condition.

### The Circular Corrected the Article a Second Time

**The article had cited the FAA's airport design circular for a table it had read in a NASA
memorandum. This pass read the circular.** Its Table 1-2 gives every bound in **both** unit systems,
and its front matter settles the question.

> Throughout this AC, U.S. customary units are used followed with "soft" (rounded) conversion to metric units. The U.S. customary units govern.

**So 118 feet and 36 metre are one boundary written twice and the circular declares which writing
governs.** The 1.3228-inch gap is the rounding the circular warns about, not a disagreement between
two authorities. **The article's framing was recast and every downstream passage with it**, and the
reproduced table now prints both unit columns as the circular does.

### Three More Primaries Each Replaced an Assertion

**The non-optimum factor now has a source.** A 1981 Grumman methodology prepared for NASA describes
the whole class of wing weight equations as a rational bending-material model with regression
constants absorbing **non-optimum weight, minimum gages and secondary loads**, which is what the
article had asserted in its own words. **The same report names flutter and divergence as the penalty
that can change an exponent**, which is the article's own named soft spot.

**The methodological thesis now has a source too.** A 2016 NASA Langley paper deriving an
aero-structural efficiency metric states that the trade differs by objective in one sentence, and
its metric is the lift-to-drag ratio that would give the same fuel consumption with a weightless
wing, coming out eleven to twelve percent below the aerodynamic value for a 737-class aeroplane.
**This article reaches the same place by the derivative route.**

**And the stationary aspect ratio turns out not to be novel.** A 1980 study under NASA contract
NAS1-16000 developed a business jet with an **aspect ratio 25 strut-braced high wing**, reported fuel
savings above twenty percent, and noted the higher cruise altitude and lower wing loading that the
2025 comparison rediscovered as a cost. **The article records the coincidence of magnitude and
declines to claim more**, because the report does not say how the 25 was chosen and a business jet is
a different class.

### What Could Not Be Got, and One Repair

**Volumes II, III and IV of the Phase IV final report are not held by the reports server at all.**
The article now says they are unavailable through this channel rather than merely unread.

**A quotation was restructured rather than altered.** The Ames summary contains a contraction and
`_verify.py` flagged it, correctly, since its contraction check does not exclude block quotations as
`stylecheck.py` does. **The source's own phrases are kept inline and its contraction is not
reproduced**, which keeps the corpus at no new warnings without putting words into a source's mouth.

### Instruments

`before_after.py` the per-cluster measurement, run twice to produce the before-and-after table.
`harvest3.py` the aimed sweep, 80 reports-server questions plus 15 and 15. `primhunt.py` the
document hunt, eleven targets and eight full texts. `fairpair.py` the like-for-like arithmetic.
`urlcheck2.py` re-run across 35 addresses.


## A363, Equation-Density Review

**38 display equations to 82, 130 inline expressions to 188, the symbol table 61 entries to 84,
9,540 lines to 9,546 and 50,183 words to 53,128.** Committed, **NOT PUSHED**, **NOT PUBLISHED**.

### What the Scan Looked For

The governing rule is the genre document's. **If the prose names a result, relies on a relation, or
quotes a value that some relation produced, the relation is shown.** A crude scan over 454
paragraphs found 139 verbal signatures of a relation in use, 87 of them in paragraphs with no
adjacent display equation, and each was then judged by hand. **Forty-four equations were added.**

### The Largest Addition Corrected the Article's Own Keystone

**The two optimality conditions rested on linearising the Breguet exponential, and this aeroplane's
usable fuel is 29,028 pound of a 145,000 pound take-off weight.** A fuel fraction of 20.0 percent
is not small, and at that fraction the linearisation overstates fuel by **11.585 percent**.

Carrying the exponential through introduces exactly one factor and nothing else changes.
**Phi equals X e-to-the-minus-X over one minus e-to-the-minus-X**, which is **0.892462** here, and
the differential of the logarithm of fuel becomes the differential of the logarithm of weight plus
Phi times the differential of the logarithm of the exponent. **Both conditions then follow
immediately.** At fixed cruise lift coefficient **nu-star equals Phi delta**, which is **0.299033**
against the drafted 0.335065. At fixed wing area **nu-star equals Phi delta over one minus Phi plus
two Phi delta**, which is **0.423797** against the drafted one half. **Both reduce to the drafted
forms as the fuel fraction vanishes**, checked at three vanishing fractions rather than asserted.

**The curvature gains one term.** It is **Phi delta times open bracket n plus one minus delta minus
Phi delta close bracket, plus Phi-prime times X times delta squared**, which also reduces correctly
and which evaluates to **0.503772** against the linearised 0.613125. **The closed form was checked
against a second difference on the exact objective, agreeing to seven decimal places, and
Phi-prime against a central difference at three hundred random points.**

**Every figure moves in the direction that strengthens the conclusion.** The stationary aspect ratio
falls from 25.100 to **23.754**, the shortfall from 28.29 to **21.41 percent**, the penalty from
1.9024 to **0.9481 percent**, and the required exponents from 2.4376 and 3.6376 to **2.1755 and
3.0832**. **The conclusion survives every weight reading and the margin narrows**, the
deliberately over-generous reading now short by **8.07 percent** rather than by the margin the
linearised figures implied, and the article says so in those terms.

**AND IT CLOSED A GAP THE DRAFTING PASS HAD TO APOLOGISE FOR.** The linearised 1.9024 percent sat
**above** the Phase II report's independently optimised bound of under 1.4 percent and needed an
explanation. The exact 0.9481 percent sits **below** it and needs none. **A discrepancy the article
was prepared to explain away turned out to be an artefact of its own approximation.**

### The Lift Equation Found a Defect in the Primary Record

**Writing down $C_L = W/(qS)$ was enough to show that the drag buildup's three stated conditions do
not hold together.** It gives a cruise altitude of 40,000 feet, Mach 0.80 and a lift coefficient of
0.695. At maximum take-off weight the lift coefficient at 40,000 feet is **0.5594**. The stated
0.695 requires either a weight **24.2 percent above maximum take-off weight** or an altitude of
**44,515 feet**, and the report's own optimum cruise altitude at maximum take-off weight, in a
different table of the same document, is **44,437 feet**. **The two differ by 78 feet, which is
0.175 percent.**

**So the lift coefficient belongs to the optimum altitude and the altitude printed beside it does
not.** It is a bookkeeping entry rather than an error of substance, since a drag buildup is properly
a function of Mach number and lift coefficient. **It is recorded because this article uses that lift
coefficient in every subsequent calculation.**

**The inversion that found it hit its bracket edge and returned it on the first attempt**, with the
direction test inverted, so the production version asserts the root is bracketed before searching.

### Two More Independent Closures, and a Closed Form That Replaced a Scan

**The equivalent flat plate area closes on the published parasite drag.** Dividing the buildup's own
27.7722 square feet by the reference area gives **0.0188017** against the published **0.01880**, an
error of **0.0092 percent**. It also prices the truss in drag, the strut and jury being **12.422
percent of the parasite drag area** and **0.0023356** as a coefficient.

**The Korn turning point has a closed form.** Substituting the secant of sweep makes the relation a
cubic whose derivative is a quadratic, so the turning point is a positive root. It gives **53.8022
degrees** at the Mach 0.80 thickness and **52.3000** at the Phase III thickness, against **53.80**
and **52.30** from a scan of seven and a half thousand angles, **with the peak values agreeing to
six decimal places**. The drafting pass had only the scan.

**The prop influence coefficient also turned out to be elementary.** The unit-load denominator is
exactly **eta cubed over three**, confirmed against quadrature to nine decimals at six stations, so
the prop force needs no numerical self-influence at all and the beam stiffness cancels.

**And the percentage-point distinction became exact.** The ratio between a percentage-point change
in a reduction and a percentage change in fuel is **the baseline over the compared value**, which is
**2.3279**. The drafting pass said about two and a half.

### A New Instance of a Documented Corruption Class

**Kramdown pairs ASTERISKS inside inline mathematics exactly as it pairs underscores, and
`emrisk.py` is blind to it.** Writing `$\nu^{*}$` twice in one paragraph produced `\nu^{<em>}` and
`\nu^{</em>}` in the rendered page.

**The rule was probed against kramdown directly rather than modelled**, which is A362's lesson about
this exact defect. Two bare asterisks in one paragraph of inline mathematics pair. One survives
alone. `\*` is inert because kramdown eats the escape. **Display blocks pass through untouched**,
so a display equation carries a bare asterisk correctly and only inline spans need escaping.

**`astrisk.py` is new and predicts it from source. `mathcorpus.py` is new and MEASURES it in the
rendered pages**, which is the only authority. Reading all 549 built pages finds **133 corrupted
mathematical spans across 37 pages, 104 underscore-driven and 29 asterisk-driven**, consistent with
the recorded 72 source-side pairs once the unit is matched since a pair corrupts two spans.
**A363 itself carries none.**

### Three Instruments Failed And Each Failure Was Instructive

**A token count found three display blocks with prose on the same line.** Dollar pairs came to 164
against 79 counted blocks, which cannot both be true. **A display block with text after its closing
delimiter is a paragraph and not a block.** A375 lost four equations to the same class.

**`mathrot.py` reported a mismatch on a page that was correct.** A LaTeX line break with optional
row spacing, `\\[4pt]`, contains the display opener the counter looked for, so the piecewise
atmosphere definition produced two more openers than closers. **The counter now requires that a
delimiter not be preceded by another backslash.** The equation pass hit this the moment it used a
`cases` environment, which the series had never done.

**`neweqns.py` CHECKED THE ATMOSPHERE AGAINST A TABLE IT COULD NOT SOURCE, WHICH IS THE A362 DEFECT
IN A NEW UNIT.** That article put five-thousand-FOOT values against a key in metres. This one typed
tabulated values from memory, failed, and then added a geometric-to-geopotential conversion **in the
wrong direction** to explain the mismatch it had itself caused, which made the high-altitude entries
fail worse. **A check against numbers the author cannot source is not a check.** What replaced it is
the two defining temperatures, the agreement of the two pressure branches at the tropopause, the
barometric exponent against its definition, and **the hydrostatic equation by central difference at
six hundred random altitudes**, which tests the model against the physics rather than against a
printout.

**A fourth failure was smaller and worth one line.** The presence checks for the new display
relations were written as regular expressions, and `\Phi` is a bad escape, so the check crashed
rather than running. **A presence test for a literal string has no business being a pattern.**

### Seven Symbol Collisions Were Resolved Before They Shipped

The new relations introduced seven base letters that would have carried two meanings each. The
established meaning kept its letter and the newer arrival was renamed. **Cap separation yielded `h`
to geopotential altitude. The flat plate area took script F because `f(u)` is the moment shape
function. Fuel volume took script V because `V` is airspeed. The record set took script R because
`R` is range. The budget projection took script P because `P` is the prop force. Block fuel per seat
took beta because `b` is span. The milestone payment took mu because `m_f` is the fuel mass.**
`symcheck.py` then needed the trigonometric functions and the layout directives added to its
structural set, since neither had appeared in this series before.

### Instruments Added This Pass

`calc2.py` the new quantities, `exact.py` the exact Breguet derivation with its limits, `neweqns.py`
94 independent checks, `astrisk.py` the asterisk prediction, `mathcorpus.py` the rendered corpus
measurement, `count.py` the structure count. `mathrot.py` and `symcheck.py` repaired.


## A363, X-Planes: Boeing X-66, Drafting Pass

**9,160 lines, 50,183 words, 38 display equations, 130 inline expressions, a 61-entry symbol
table, 4,064 reference definitions, 21 H2 sections, 54 H3 sections and 17 tables.** Committed,
**NOT PUSHED**. **NOT PUBLISHED.**

### The Keystone, and Why It Is Infrastructural Rather Than Aerodynamic

The aspect-ratio trade is derived from the lift distribution outward. An elliptic spanload gives a
root bending moment of **L b over three pi**, checked three ways. Cap area is moment over the
product of allowable stress and box depth, and integrating it across a straight-taper wing gives
bending material proportional to **the three-halves power of aspect ratio at fixed area and
thickness ratio, and to the inverse first power of thickness ratio**. The exponent is derived and
then measured numerically as 1.5000.

**The optimality condition then splits in two, which is the analytical result worth keeping.**
Holding wing area and cruise condition makes induced drag proportional to weight squared over
aspect ratio, so the stationary point is **nu equals one half exactly**, with the induced-drag
fraction cancelling out of the condition entirely. Holding cruise lift coefficient instead gives
**nu equals delta**. Both are exact, both are parameter-free in their own terms, and they call for
different aspect ratios on the same aeroplane.

**Every reading of the weight data puts this aeroplane below both stationary points.** Counting
only the 7,488 pound of bending material the report identifies gives nu of 0.0775 against a
required 0.5. Counting the whole wing group and the whole truss group at the three-halves power
gives 0.2062. **The falsifiable form is that the wing and truss together would have to grow as
the 3.64 power under one criterion or the 2.44 power under the other.**

**And then the tone reverses, because the optimum is flat and the flatness has a closed form.**
The curvature at the fixed-lift stationary point is exactly **delta times (n + 1 - 2 delta)**,
which is 0.6131 here, so a 28.3 percent shortfall costs **1.90 percent** in fuel. **The Phase II
report, by a full multidisciplinary optimisation over span limits nine years earlier, reported
under 1.4 percent for all further span beyond 170 feet.** Two routes sharing no arithmetic agree
on magnitude and sign, and the gap is explained by the field-length and range constraints the
optimisation had active and the expansion does not see.

### The Gate Box, Which the Dead Reference Forced Into Better Shape

**The address sweep found the ICAO publications page unreachable.** Replacing it meant going to
the Airplane Design Group table reproduced in NASA/TM-20250002858, and that table is **in feet
with exclusive bounds**. Group III runs from 79 feet up to but not including 118, and Group IV
from 118 up to but not including 171.

**So the fold station is not near a boundary. It is exactly on one, to the inch, with a margin of
exactly zero.** And because the bound is exclusive, a span of exactly 118.000 feet is a Group IV
aeroplane. The memorandum's own wording is **less than 118 feet**, while the Phase IV report puts
the fold **at 118 feet**. **Whether that is a rounding, an unrecorded inch, or a genuine gap
between two NASA documents is not settled by the record and the article says so.** ICAO's bound of
36 metre is 118.1102 feet, **1.3228 inch looser**, so the same fold clears Code C and not Group III.

**The fold is worth 35.96 percent in lift-to-drag ratio**, because the Code C box permits aspect
ratio 9.427 at this area against the 19.565 the fold buys. **And 9.427 is essentially the aspect
ratio of the conventional single-aisle fleet**, whose own comparison baseline in the report carries
10.41. The inference the article draws, and labels as an inference, is that **the aspect ratio of
the fleet is an airport number rather than a structural one**.

### Three Expectations This Article Overturned By Deriving Them

**The truss buys a coefficient and not a power.** A truss whose attachment station, dihedral and
proportions scale with span leaves the exponent at exactly three halves, and since the optimum
moves as the coefficient to the power minus two fifths, halving the bending material would move
the optimum aspect ratio by about thirty-two percent and the fuel consequence by very little.
**That is the uncomfortable corollary, because it says the truss's structural achievement cannot
by itself be worth much in fuel**, and the value has to be in the fold and in the thin wing.

**The absolute weight model is wrong and the way it is wrong is the point.** The cantilever
estimate landed at 0.909 times the published **braced** bending material, which looks like a
validation and is a coincidence of two large errors in opposite directions, since a cantilever
must be heavier. With the brace included the model is low by a factor of **7.88**, which is
non-optimum material. **A constant factor does not touch a logarithmic derivative**, which is
exactly why the keystone survives being unable to predict the absolute weight.

**And an assertion refuted the docstring of the function it guarded.** The Korn relation's
inversion for sweep was written with a bracket from zero to seventy degrees and a docstring
claiming monotonicity. The relation turns over at **53.8 degrees** because the thickness and lift
terms grow as the inverse square and cube of the cosine, so both ends of the bracket fell below
the target and **the assertion refused to run rather than returning the wrong root**.

### What the Korn Relation Found That Nothing Else Did

**Both configurations sit the same distance below their own drag-divergence Mach number.** With a
single supercritical constant of 0.95 the margins are **0.0203** for the Mach 0.745 predecessor
and **0.0181** for the Mach 0.80 configuration, **differing by 0.00212**, and the difference stays
below **0.00672** across the whole plausible range of that constant. Neither margin was an input.
**So the ten degrees of sweep and the thickness reduction Phase IV added are, to within a few
thousandths in Mach number, exactly what the relation requires to buy 0.055 in cruise Mach.** The
thinning alone is worth **4.86 degrees** of sweep and cost about **28.7 percent** in bending
material, which is a prediction the volume read here cannot check.

### What the Primary Record Admits About Itself

**A flutter correction turned a forty percent margin negative.** At Mach 0.92 the raw
doublet-lattice model gave margins near forty percent and the computational-fluid-dynamics
adjusted model produced multiple mechanisms with margins as low as **minus 7.5 percent**, with the
report saying the adjustments **completely changed the character of the analysis results**. It also
says the method is incapable of capturing the nonlinear flow features and that a braced wing's
redundant load path requires prestressed modes about a large deformation state. **That is the
largest soft spot in this article's own keystone**, because flutter-driven stiffness is the term
that could push the exponent above three halves and it is unmodelled at the critical condition.

**And the report's own recommendation list undercuts the figures everybody quotes.** It asks for
**equivalent conceptual-level design, sizing and optimization studies of cantilever and
truss-braced wing aircraft of the same technology level to allow a more fair and transparent
comparison**, which is a statement by the organisation with the most to gain that the comparison
has not been made fairly. A January 2025 paper appears to answer it and is cited from its registry
record only. **Then it asks for the preliminary design of a demonstrator, which is the one
recommendation that was carried out.**

### The Programme, From the Signed Instrument

**Twenty-seven funded milestones totalling exactly 425 million dollar**, checked against the
appendix's own stated total rather than merely summed. **98.824 percent is paid before first
flight**, which is itself worth 1.5 million dollar against a largest milestone 18.17 times that.
Boeing signed 12 January 2023 and NASA the next morning, so the seven-year term expires 13 January
2030 while the last milestone falls due August 2029.

**The agreement has no pause in it.** The word appears zero times. Article 20 offers termination by
mutual consent, termination thirty days after notice of a missed milestone, and unilateral
termination on four grounds. **The pause landed between Milestone 9 in February 2025 and Milestone
10, the Wing and Strut Critical Design Review, due May 2025**, which is the gate at which the wing
would have been committed to fabrication, and the activity announced as retained is wing research.
Through February 2025 the agreement had reached **153 million dollar, 36.00 percent**.

**The award record holds one contract under the project's name, for 41,198 dollar of desk models**,
and nine truss-braced-wing research contracts totalling **21,420,664.42 dollar**, of which
**80LARC21F0101 at 615,042 dollar is a dedicated task for truss-braced wing structural weight
estimation**, the quantity the keystone turns on. **Three budget books show the Integrated Aviation
Systems Program line falling 67.8 percent for fiscal year 2029 between two successive
justifications**, and aeronautics overall falling 37.0 percent.

### The Sweep, the Gate, and What the Audit Changed

**Two sweeps, 150 reports-server questions, a pool of 14,967, a gate keeping 4,238 across 17
clusters.** The first sweep retrieved 98.2 percent of what the server reported and only one
question hit the wall. **Nine questions returned nothing and seven were rescued by rephrasing in
the vocabulary the registry's own titles use.**

**The homonym measurements are the transferable part.** `SUGAR` returns astrophysical ice
analogues, carbonaceous meteorites, Coccidioides immitis and blood sugar, one of ten aeronautical,
and **`sugar aircraft` returns ten of ten**. **`aspect ratio` is aeronautical at the reports server
and zero of ten aeronautical in the bibliographic index**, which is the second registry-dependent
homonym this series has recorded. `strut` returns zero of ten wing braces and `truss` two of ten,
while **`braced wing` returns ten of ten**.

**THE TWO-SIDED AUDIT CHANGED THE GATE IN BOTH DIRECTIONS AND THE REFUSED SIDE MATTERED MORE.**
Reading thirty admitted records found six that should not have been there, so a bare `aeroelastic`
now needs an aeronautical noun, a bare `net zero` needs aviation, a bare `open rotor` needs an
airframe, and a rotary-wing exclusion family was added. **Reading thirty refused records found an
entire missing cluster**, being a joined-wing research aircraft, a tandem-wing spacing study and a
blended-wing-body pre-design, none of which any pattern admitted. **`alt_config` now holds 448
records and is the third largest in the article. A gate audited only on what it keeps cannot find
an absence.**

**One tightening failed twice on the same title.** Narrowing `aeroelastic` left an aeroelastic
**panel** paper admitted, first because the qualifier list contained the words `model` and
`analysis`, which qualify nothing, and then because the leak was in a second pattern entirely.
**A panel, a plate and a shell are aeroelastic and are not wings.**

### The Verifier Found Three Faults In Itself

**`verify_numbers.py` passes 104 checks and the first three runs failed inside the checker.** Its
first quadrature design was eight million evaluations and timed out, when the taper integral does
not depend on aspect ratio and needed computing once. It then compared the article's rounded
display strings at full precision and reported **eleven failures that were all the article's own
rounding**, so the tolerance is now derived from the last printed digit. And a regex conversion
moved explicit tolerances into a `scale` parameter, **rescaling one slot by ten thousand**, which
the check caught as a 999,934 percent error. **A verifier that fails on its own display precision
is measuring the wrong thing.**

### Instruments

`meas.py` the physics with every loop bounded in its header. `calc.py` the driver.
`verify_numbers.py` 104 checks, importing nothing from `meas.py` by design. `gate_and_cluster.py`
139 patterns, nine exclusion families, 29 keep cases and 43 refusal cases with every refusal
re-tested hyphenated. `run_gate.py`, deliberately not named `select.py`. `homprobe.py` the homonym
measurements. `harvest.py` and `harvest2.py`. `resolve_years.py` with its success-rate floor,
resolving 785 of 965 at 0.813. `build_refs.py`, `emit.py` 233 slots, `assemble.py` which reports
unused slots as well as unfilled ones, `series_line.py` which generates the opening line from the
same mapping that emits its definitions. **`stylecheck.py` is new**, checking the project's prose
rules on prose only after stripping tables, headings, quotations, maths and reference definitions,
and checking that each acronym is expanded before its first bare use. `urlcheck2.py`, `symcheck.py`
with trigonometric operators added, `mathrot.py`, `rendercheck.py`, `emrisk.py`, `site_build.sh`.

### Verification State

`_verify.py` 0 errors and 4 warnings, all four `progress-stale` and all four resolved by this
commit's channel updates. The stub build takes about fifteen seconds. `_lib/render.py` reports no
findings across 549 pages. `mathrot.py` matches 38 source display blocks against 38 rendered
brackets with zero emphasis tags inside any expression. **`emrisk.py` confirms A363 adds nothing
to the corpus-wide count of 72 corrupted expressions in 38 files**, which remains an open pilot
decision. `symcheck.py` passes. `stylecheck.py` reports one finding, which is the statutory
citation `51 U.S.C. 20113(e)` and cannot be written otherwise.

### A Placeholder Identifier Was Caught Before It Shipped

**A reference was entered with the digital object identifier `10.2514/6.2026-0000` as a placeholder
while the real one was looked up.** The real identifier is `10.2514/6.2026-4344`. **A fabricated
identifier that resolves to nothing is worse than no citation at all**, and the record is omitted
rather than cited because the article's dateline is December 2025 and a 2026 conference paper cannot
be used in the body.


## A362, Publication Review

**Lines 8,775 to 8,777, words 67,925 to 67,992, the symbol table 100 entries to
102.** Display equations held at 46, references at 3,804.
Committed and **PUSHED** on the pilot's instruction. **NOT PUBLISHED**, and publication of the
series has never been authorised.

### A Claim This Review Refuted by Counting

**The article said `hingeless control` returned seventy-two records from the reports server of
which every one was a helicopter. It is 61 of 72.** The review counted
all 72 titles instead of trusting the sample that had been read, and
11 do not carry rotorcraft vocabulary. **Most of those are rotorcraft work under
other words**, being higher harmonic control, flap-lag stability in forward flight, ground
resonance and a vertical and short take-off conference. **Two are not rotorcraft at all.** They
are the DARPA, Air Force Research Laboratory, NASA and Northrop Grumman Smart Wing programme,
**which shares the hingeless vocabulary because it is about a wing with no discrete moving
surface**, and which this article's sweep never asked for. The corrected count and the Smart Wing
finding are both in the body.

### Seven Rankings Were Scoped to What Had Been Measured

**The superlative scan returned forty-five hits and seven were rankings this article had not
earned.** That the aircraft is the first in the series able to be compared with itself, a ranking
across sixty-six articles. That `CRANE` is the least useful query in the sweep, a ranking over
roughly two hundred probes where ten were read by hand. That a declared symbol table is the only
instrument that catches a collision. That the air architecture is the single largest uncertainty in
the analysis, where the amplification range is wider. That the differencing design is the single
most important decision in the aircraft. That this article's vocabulary is the worst the series has
met, across vocabularies never measured. And that asking the detail endpoint was the only way to
tell a catalogue gap from a literature gap. **Each is now scoped to what was checked**, and the
rankings that survive are the ones with a measurement behind them, such as the air budget being the
thinnest of fifteen clusters.

### A Stale Figure an Emitter Had Hard-Coded

**The empty-cluster message said the sweep retrieved 18,432 records and the pool is 20,430.** The
figure was written into `emit_clusters.py` as a literal after the second sweep and the third sweep
moved it. **The article therefore stated a number its own source base contradicted**, which is the
defect the slot discipline exists to prevent and which survived because this one number was not a
slot. It now reads the pool from the gate statistics.

### An Acronym Reached the Reader as a Subscript

**`AFC` appeared first in the authority-ratio equation as a subscript and was never expanded.**
`symcheck.py` could not see it because it strips `\mathrm{...}` before comparing symbols, so a
subscript that is itself an unexpanded acronym passed every check the article had. The prose that
introduces the equation now spells it out and both subscripted force increments are declared,
taking the symbol table to 102.

### Small Counts and Dollar Figures

**The article spelled fourteen, eighteen and twenty-five and wrote `4 move no money`,
`5 times out of 5`, `2 of the 5 quoted cases`, `8 questions` and `where 6 still did not`.** Counts
are now spelled and measured quantities keep their numerals, so eight percent of core flow and 1.5
percent stay as they were. **Eleven dollar figures carried a meaningless `.00`** against the
article's own `192,823 dollars`, and the one figure with real cents keeps them. **And a cluster
heading read `1 records.`**

### What Was Checked and Found Clean

**Prose style.** No em dashes, no en dashes, no contractions, no capitals as emphasis. Three
findings and all three are permitted, being a colon inside a code span quoting what a registry
emits, the semicolon in the mandated debug tag, and a parenthetical inside a block quotation of the
register's own description.

**Structure.** All eighteen sections in the order the research-aircraft genre prescribes, with the
Epistemic State, Out of Scope and Conclusion present and last.

**Diction.** Zero content-independent words at or above the peer maximum. Forty-six words exceed it
and every one is the subject or a proper noun, being the contractor, the programme, the agency, the
plenum, the effectors, the fiscal years and the budget books.

**Thirty URLs.** Every one verified. Nine publisher addresses refused the fetcher and all nine are
confirmed in the registry by title, venue and year. **Two were flagged thin and both were false
positives of this review's own byte threshold**, the encyclopedia's pages being plain markup with no
boilerplate and the federal award service being a JavaScript application whose markup is a shell by
construction.

**Numbers.** `verify_numbers.py` runs **160 checks with none failing**, `neweqns.py` a further 52.
`_verify.py` reports 0 errors and 0 warnings across 302 posts. The rendered audit reports no
findings across 546 pages, source and rendered display blocks both count 46, and no
inline expression in the page carries an emphasis tag.


## A362, Primary-Reference Review

**Report primaries 1,387 to 1,464, a share of 38.1 to 39.5 percent, the
period count 1,205 to 1,274 and its share 34.4 to
35.7 percent.** Research records 3,636 to 3,709, reference
definitions 3,658 to 3,804, lines 8,516 to 8,773 and words 64,114 to
67,817. Display equations held at 46 and inline at 228. Committed,
**not pushed**, which is the rhythm. **Not published.**

**BOTH THE COUNT AND THE SHARE ROSE, WHICH THE GENRE DOCUMENT WARNS IS UNUSUAL.** A reference pass
normally raises the period count while lowering the recent share, because it adds older primaries
faster than recent ones and the denominator grows with them. **This sweep was aimed at one
registry's literature rather than at the subject broadly**, so primaries arrived faster than
anything else. The median year did not move, staying at 2007, and the earliest record
moved back ten years to 1927.

### Seven Claims Were Second-Hand and the Audit Began by Saying So

**Every threshold in the article was read through one review.** The regime boundary of three to
five percent, the reduced-frequency band, the measured response at 0.08 percent, the reattachment
at 0.34 percent, the modified-coefficient thresholds, the velocity-ratio condition, the caution
against comparing momentum coefficients across configurations and the attribution of the
definition to Poisson-Quinton. **A pass that exists to prefer primaries has to start by listing
what is not one.**

**Nine originals were located and four could be read in full, and all four are agency reports.**
Every journal item the review names is paywalled. **The upgrade from second-hand to first-hand was
available only where the work was also published as a report**, which is the practical reason this
corpus prefers the report literature, and six items are now carried at registry-record strength
and quoted for nothing.

### The Report That Reversed the Equation Pass

**Seifert and Pack, AIAA 2000-2542, read in full, demonstrated oscillatory separation control at
chord Reynolds numbers as high as forty million** and state that the Reynolds number has a very
weak effect on the pressure distributions and spectra of a deliberately fully turbulent baseline.

**The equation-density pass had argued the opposite way round.** It computed this aircraft's
Reynolds number at 11.44 million, compared it with the low-Reynolds experiments whose
thresholds the article had borrowed, found a gap of one to nearly three orders of magnitude and
concluded that the thresholds were the part most likely to be wrong at flight scale. **The X-65A
flies at 0.715 times that report's sixteen million and 0.286 times the
forty million it quotes.** It is inside the demonstrated range, not beyond it. **The strong form of
the argument is withdrawn in the body rather than quietly softened**, and what remains is the
narrow and correct form, that transferring a threshold differs from transferring a phenomenon.

**And the report quotes the coefficients it used, on a definition identical to this article's.**
Oscillatory momentum coefficients of 0.03 to 0.32 percent, with its own stated
uncertainty of plus or minus twenty-five percent. **This article's wing-referenced
0.0945 percent sits inside that band**, reaching 2 of 5 quoted cases
with no concentration at all. **At that report's own Mach number of 0.25 the same bleed budget
delivers 0.5579 percent, which is 1.74 times its highest quoted value.** So the
air is sufficient where the method is proved and marginal only where this aircraft wants to fly.

### The Primary Names This Article's Keystone as the Open Problem

**Among its proposals for future work is overcoming the lack of sufficient control authority,
especially at high speeds.** That is the conclusion this article derived from the Mach dependence
of a bleed-fed momentum coefficient. **The article now says the constraint was derived here and
discovered elsewhere**, which is the second time in three passes that a primary has shown a result
to be a rediscovery.

### The Targeted Sweep Returned Little and the Little-ness Is the Finding

**Eighty-six new questions were asked of the two report registries and the per-cluster share was
computed before any of them were written.** Five clusters were thin. **The one the pass most wanted
to fix moved least.** The air budget stood at 9.1 percent of 77 records and now
stands at 12.5 percent of 80. **Thirty-five dedicated questions across both
registries bought three records.**

**The reason is measurable and it is not the sweep's.** A reports server asked for a secondary air
system returns two hundred and seven records of a seal workshop, because inside an engine secondary
air means internal cooling. Asked for an aircraft air supply system it returns electric-propulsion
impedance and direct-current power supplies. The defence registry asked what bleed air costs in
engine performance returns two hundred records of which three pass the gate and none is about bleed
air. **What a bleed costs an engine is known to the companies that build engines and is in neither
public registry**, so the article's refusal to put a number on the thrust penalty is a gap in the
record rather than in its research.

**Two clusters did move.** Conventional actuation went 25.6 to 35.1 percent, because
hinge moments and actuation power are what the agency reports of the 1960s and 1970s are full of.
**Control without a hinge did not move at all, staying at 50.0 percent**, which says that
literature is genuinely journal-held.

### The Programme's Own Ancestor Has No Report Literature

**The CRANE manager named Micro Adaptive Flow Control as the work CRANE descends from and neither
registry holds a report about it.** The reports server returns two 1995 summer faculty fellowship
programmes, a Spacelab life-sciences experiment and a paper on the importance of properties in
modelling. The defence registry returns one hundred and twenty-one records of which two pass the
gate and both concern adaptive structures. **A DARPA programme leaves no report literature in a
NASA registry because it was never a NASA programme.**

### Four Method Findings

**THE SAME WORK IS HELD TWICE AND ONLY ONE IDENTIFIER CARRIES THE FILE.** A request for the
flight-Reynolds report's full text returned nothing, and the duplicate record of the same work
carries both a portable document and a plain-text rendering. **A null answer from a registry is
usually a measurement about the literature and this one was about the catalogue.**

**SERENDIPITY IS RECORDED AS SERENDIPITY.** Three of the better allocation records came from a
question about secondary power extraction, being a 1997 report on tailless aircraft control
allocation and two of 1999 on robust nonlinear control of tailless aircraft. **A sweep that found
its best records for one cluster while asking about another has not demonstrated a method.**

**A REWRITE SILENTLY DELETED A DISPLAY EQUATION.** Replacing a span from one heading to another
swallowed a third heading between them, taking the moment relation and its table. **Every figure
still reconciled, every slot still filled, `_verify.py` passed and the rendered audit passed**,
because a missing equation is not a defect in anything that remains. The verifier now carries a
floor at the equation pass's own count, and the first version of that floor used a dotted-all flag
that made its pattern greedy across newlines and reported one equation where there were
forty-six.

**AND A DOUBLED BACKSLASH LEFT A LITERAL ONE IN THE PAGE.** An escaped citation written with two
backslashes rather than one renders the backslash, and it was found by counting brackets in the
rendered page against display blocks in the source, 47 against 46, where the extra was not an
equation at all.

### Verification

`verify_numbers.py` runs **141 checks with none failing**, up from 111, now including the pass's
before-and-after figures recomputed from a frozen baseline, the four primaries read in full, the
withdrawn Reynolds wording, the air-budget negative result, the equation floor and the doubled
escape. `_verify.py` reports **0 errors and 0 warnings**, and it caught an undefined anchor when the
new primaries were cited before being defined. The rendered audit reports **no findings across 546
pages**, source and rendered display blocks both count **46**, and no inline expression
in the page carries an emphasis tag.


## A362, Equation-Density Review

**Display equations 21 to 46, inline expressions 113 to 228, the symbol
table 48 entries to 100, lines 8,281 to 8516 and words 60,403 to
64114.** Reference definitions unchanged at 3721. Committed, **not pushed**, which
is the rhythm. **Not published.**

### What Was Missing Was the Ground the Whole Article Stands On

**Twenty-five relations were added and most of them had been in use since the drafting pass
without ever appearing.** The standard atmosphere, the speed of sound, the total conditions, the
corrected-flow invariant, the compressor temperature ratio, the two mass-flow routes, the core
flow, the aspect ratio, the wing loading and the lift coefficient were all computed and none was
shown. **The genre rule is that a relation the prose relies on gets displayed, and an article
that tabulates a standard-atmosphere pressure without showing where it comes from fails it.**

**The additions that are findings rather than bookkeeping are three.**

### The Reynolds Number Gap, Which Quantifies Why the Aeroplane Exists

**The drafting pass asserted that Reynolds number is why a flight demonstrator is needed and
never computed it.** On the mid-sweep chord at Mach 0.7 and thirty thousand feet the X-65A flies
at **11.44 million**, by Sutherland's law for the viscosity, checked against the published
sea-level value.

**The experiments this article borrows its thresholds from ran at between 19.1 and
497.6 times less.** The measured reattachment at 0.34 percent was obtained at one hundred
thousand. The modified-coefficient thresholds at twenty-three thousand. **Every number used to
decide whether the bleed budget is adequate was measured one to nearly three orders of magnitude
below the condition it is applied to**, and the article now says so and says the direction of the
error is not known in advance, since a boundary layer that separates later needs less control
while being less receptive to it.

### Sharing One Plenum Is an Advantage, and the Limit Is Pi Squared Over Two

**The drafting pass said the constraint set is a simplex rather than a box and left the
impression that sharing is a penalty.** The algebra says otherwise and the algebra is now shown.
The demanded moment is the effectiveness matrix times the demand vector, three axes need full row
rank, and the reachable set is the image of the admissible set. **A box maps to a zonotope and a
simplex maps to the convex hull of its vertices' images.**

**Held at the same total air, the shared plenum reaches 4.9360 times the moment area that
equal fixed per-effector shares would reach**, at fourteen effectors. **The ratio converges to an
exact closed form**, the hull tending to a half disc and the equal-share zonotope to the
reciprocal of pi, so the limit is pi squared over two, 4.9348. At a hundred effectors the
computed ratio sits within a part in ten thousand of it. **Both areas were also checked against a
rejection sample over an exactly computed bounding box, and the unit square and unit triangle by
hand.**

**So the cost of one supply is not a smaller reachable set. It is that the set is no longer a
box**, so the allocator cannot be a per-axis gain and has to solve a programme. The geometry is
labelled illustrative in the text, because the effector positions are not published.

### The Air's Price, Now Stated

**Bleeding 1.860 percent of total engine flow is also the floor on the thrust it costs**,
and the compressor work already spent on each kilogram is 334.1 kilojoule at a temperature
ratio of 2.3241. **The article states the inequality and declines to compute the true loss**,
which needs an engine deck. And the bleed inversion is now displayed, so the fractions are
derived rather than tabulated: 6.77 percent of core flow reaches the lowest measured
threshold and 253.95 percent would be needed for super-circulation, **which is two and a
half times the core flow the engine has.**

### Four Defects, and Two Were in the Checks

**THE FIRST EQUATION CHECK FAILED FOUR TIMES AND THREE WERE ITS OWN REFERENCE VALUES.** Its
standard-atmosphere table carried the 1976 values at five thousand FEET against a key in METRES.
**A unit confusion in a test accuses the code of the test's own mistake**, and this is the fourth
time in this series an equation pass has failed in the check rather than the article.

**THE FOURTH FAILURE WAS A MONTE CARLO WHOSE BOUNDING BOX MISSED THE EXTREME POINTS.** It
reported a hull area BELOW the closed form, which for a coarse outer approximation is impossible,
and that impossibility is how it was spotted. The bounding box is exact and needed no sampling.

**AND THE RENDERED PAGE CARRIED TWO CORRUPTED EXPRESSIONS THAT NOTHING SAW.** Kramdown does not
protect `$...$` from markdown processing, so an underscore opened emphasis in one expression and
closed it in another, putting an `<em>` tag inside the mathematics. **`_verify.py` passed,
`_lib/render.py` passed, and the equations still rendered.** It was found by reading a snippet of
the page by eye.

**THE FIRST FIX WAS BUILT ON A GUESS AND MADE IT WORSE, TWO CORRUPTED SPANS BECOMING THREE.** It
braced every subscript on a wrong model of the flanking rule. **A direct probe of kramdown
settled the rule in five lines**, and the measured behaviour is that an underscore opens when the
character before it is not a word character and closes when the character after it is not.
Escaping the openers works and costs nothing, because kramdown consumes the backslash and MathJax
receives the underscore. **Nine spans carry the escape and the rendered page now carries none of
the tags.**

**THE DEFECT IS PRE-EXISTING AND CORPUS-WIDE, AND THE FIRST COUNT OF IT WAS WRONG TOO.** A scan
built on the pre-probe flanking rule reported fifteen pairs across ten files. **Rebuilt on the
measured rule it reports seventy-two pairs across thirty-eight files**, of which **thirty-five are
published posts carrying sixty-nine pairs** and three are drafts carrying three. The heaviest is a
projection-series post with seven. **Two of the drafts are this series' own**, being the opener and
A361, and the third is A334.

**A362 is fixed and the other thirty-seven are reported and untouched**, because editing the
mathematics of published posts is the pilot's call and not a side effect of an equation-density
review. **The wrong count had already been written into these files and was corrected before the
commit**, which is the only reason it is not in the history table as a fact.

### Verification

`verify_numbers.py` now runs **111 checks with none failing**, up from sixty-three, and
`neweqns.py` runs **fifty-two** more against published table values, independent routes and
hand-checkable cases. `symcheck.py` reports 100 declared symbols with every token
used resolving to one, after **two more collisions were renamed**, the lapse rate off `L` which
`\Delta L` and `C_L` were already using, and the tropopause conditions off `T_t` and `p_t` which
are the plenum's. `_verify.py` reports **0 errors and 0 warnings**. The rendered audit reports
**no findings across 546 pages**, and **source display blocks and rendered blocks both count
46**.


## A362, X-Planes: Aurora Flight Sciences X-65 CRANE, Drafting Pass

### The Keystone, Which Cancelled Altitude Twice and Exactly

**The momentum coefficient an engine-bled flow-control effector can deliver is exactly
independent of altitude.** Corrected mass flow makes the bled flow proportional to ambient
pressure, the compressible identity makes dynamic pressure proportional to ambient pressure, and
those cancel. **Then a second cancellation nobody asked for**, because corrected flow divides by
the square root of the compressor-face total temperature while a choked jet fed from that same
air multiplies by it. **The inlet total-condition factor cancels once as well.** What survives is
the inlet's own total-pressure recovery over the square of the Mach number, verified identical to
twelve significant figures across ninety-one altitudes from sea level to forty-five thousand feet.

**The other architecture varies by 7.92 times over the same band**, so the published
phrase `a pressurized source` conceals which behaviour this aircraft has. **The article's
prediction is that two flights at one Mach number and two altitudes settle it.**

**AND A MONOTONICITY CHECK REFUTED A BOUND THE ARTICLE HAD ASSERTED.** The Mach factor was
claimed monotone to about Mach 1.9. It turns at exactly Mach 1.4142, independently of the
specific-heat ratio, and the minimum has the closed form gamma to the power gamma over gamma
minus one, halved. **Three routes agree to one part in ten to the fifteenth.**

### The Result That Had to Be Withdrawn, and the Review That Withdrew It

**THE DRAFTING PASS INVENTED A BAND AND A PRIMARY REFUTED IT.** The first version asserted that
separation control needs a momentum coefficient between 0.005 and 0.02, computed that engine
bleed cannot reach it, and made that the central difficulty. **An open-access review, read in
full, reports the separation-control to super-circulation threshold at three to five percent and
a measured lift response at 0.08 percent.** The wing-referenced coefficient computed here is
0.0945 percent, so it reaches the smallest value at which a response has been measured, and
needs a concentration factor of only 3.60 to reach a measured reattachment threshold.
**The conclusion reversed and the reversal favours the aircraft.**

**The same review names the article's own quantity.** What this article derived as an
amplification identity, the ratio of the lift increment to the momentum coefficient, the
literature calls the actuation efficiency and already reports as falling through the regime
transition. **No novelty is claimed and the article says so in its own text.**

**It also cautions against the use the article makes of the momentum coefficient**, because many
combinations of mass flow and jet velocity give one value, and the parameter that separates them
is the velocity ratio, which must exceed unity. **It is 2.083 here.** And because a higher
velocity ratio beats a higher mass flow at the same momentum, **the single-stage centrifugal
compressor that forces hot full-cycle bleed is favourable in exactly that dimension**, which is a
reason not to precool the air and was not looked for.

### Where Flow Control Loses to a Hinge

**The authority ratio is altitude-independent and falls as the square of the Mach number.** At an
amplification of thirty against a surface worth 0.05 in lift coefficient, the crossover is Mach
0.485, flow control delivering 5.15 times the hinge's authority at Mach 0.2 and
0.567 of it at Mach 0.7. **For a conventional aeroplane the hard case for control power
is slow flight. For this one it is fast flight**, and an envelope expanded upward walks from the
easy end to the hard one.

### The Award Record Names What the Narrative Does Not

**Twenty-five offers, three awards, and the downselect visible as an exercised option.** Aurora
Flight Sciences, Lockheed Martin and Georgia Tech Research Corporation each hold a Phase 0
contract reporting twenty-five offers received. Aurora and Lockheed each exercised an option in
mid-2021 and **Georgia Tech never exercised one at all**, leaving 45.1 percent of its ceiling
unused, so the record dates a cut no source states in words. **Georgia Tech was also cost no fee
where both companies were cost plus fixed fee.**

**The Phase 2 and Phase 3 contract carries 94,372,238 dollars against a press figure of forty-two
million**, because the two phases went onto one instrument. **Its last obligation is 16 January
2025 and the only action after it is a zero-dollar change order on 11 February 2025**, which is
the pause appearing as an absence. The period of performance expired on 2 October 2025, sixty-nine
days before the article's dateline, with the fuselage unfinished. **The restructured co-investment
appears nowhere in the record, because a contractor's cost share is not federal spending.**

### Seven Budget Books, and a Milestone That Slipped Two Fiscal Years

Every CRANE line in every DARPA justification book from the fiscal year 2020 request to the
fiscal year 2026 request was read. **The three columns of an exhibit are a prior-year actual, a
current-year estimate and a budget-year request, so one fiscal year appears in three consecutive
books wearing three hats**, and reading the disagreement as inconsistency would be wrong.

**Fiscal year 2020 came in 81.33 percent above its request and every year since has come in
below, at a mean shortfall of 16.29 percent.** The programme asked 200.507 million
dollars across seven years and expects 179.416 million. **The critical design review was
promised in four consecutive books for three different fiscal years.** The fiscal year 2026
request of 4.000 million is the only round number among seven figures carrying three decimals.

### The Vocabulary Is the Worst the Series Has Met

**`CRANE` returns a logging-crane fatality, a mobile-gantry-crane fatality and two collections of
nursery rhymes, with nothing aeronautical in ten results.** `novel effectors`, the literal phrase
in the programme's title, returns fungal and oncological effectors. `control authority` is
bibliographic authority control, ten of ten. `fluidic oscillator` is an American Water Works
Association standard for cold-water meters. **`momentum coefficient`, the article's keystone
parameter, returns microchannel accommodation, rarefied momentum exchange and an evolutionary
optimiser.**

**AND ONE HOMONYM DEPENDS ON WHICH REGISTRY YOU ASK, WHICH IS NEW TO THIS SERIES.**
`hingeless control` returned ten of ten on subject from the bibliographic index, every one about
flow-control effectors, and seventy-two records from the reports server of which every one is a
helicopter rotor hub. **The same two words name two unrelated subjects and the right anchor
differs by registry.** The gate carries a rotorcraft guard because a probe was read, not because
an audit failed.

**The keystone parameter is almost never in a title.** Twelve titles in nearly twenty thousand
name it and the gate admits eleven. **The parameter is a method rather than a subject**, which is
a third case beside a query that failed and a literature that was thin.

### What the Audit and the Checkers Caught

**The two-sided audit changed the gate twice.** A refused co-flow jet paper revealed an entire
effector family with no anchor. A refused reconfigurable-control record revealed fifty-nine
control-allocation records of which forty were being refused, **and twenty-eight effectors on
three axes is an allocation problem by construction**, so that cluster exists because refusals
were read.

**A GUARD WAS DEFEATED BY A HYPHEN AND THE SHARED LIBRARY CANNOT REPAIR IT.** The library flattens
intraword hyphens only after an unflattened pattern has failed. **A guard is a negative lookahead,
so a guard that fails to fire is a guard that admits**, and the record is admitted before
flattening is tried. Two further guards leaked when refusal cases were re-tested with hyphens,
having passed because the test used the spelling the probe returned.

**THE YEAR RESOLVER FAILED ON ALL 1,321 RECORDS AND RAISED NOTHING.** It read the raw response's
`publications` field from a library function that had already consumed and discarded it. **An
empty year is a legitimate value, so a total parser failure and a dateless registry are the same
observation**, and the only instrument that can separate them is a success-rate floor, which the
file now carries.

**A ZERO-COUNT CLUSTER IS INVISIBLE IN A COUNTER.** The statistics looked for zero values and
found none, because `collections.Counter` never creates a key it did not count. **The one empty
cluster is a finding**, being that not one record in 18,432 names this programme, this
aircraft or this contractor.

**`symcheck.py` FOUND TWO REAL SYMBOL COLLISIONS.** The letter A served as the amplification and
as the choked throat area, and f served as a dimensionless factor and as a frequency. Both were
renamed.

### Verification

**8,281 lines built from eleven body files with every number filled from a slot**, so no
figure is typed into the prose. `verify_numbers.py` runs sixty-three checks and all pass,
re-deriving the atmosphere against published table values, the altitude invariance across
ninety-one altitudes, the turning point by three routes, the amplification identity and the
survey statistics from the reference base. `_verify.py` reports **0 errors**. The stub build took
fifteen seconds and the rendered audit reports **no findings across 546 pages**. **Source display
equations and rendered display blocks both count 21**, which is the check A375 earned
when four of its equations folded into a paragraph.

---

## Next

**Await the pilot's prompt.** By the rhythm the next prompt is A362's equation-density review.


## A361, X-Planes: Invocon X-64

**FINAL STATE 8,873 lines, 67,030 words, 39 display equations, 231 inline expressions, a
90-entry symbol table, 3,934 reference definitions**, with **3,837 research records cited
across 15 clusters and 1,726 report primaries at 45.0 percent**, median year 2003, period
share 87.7 percent, from one sweep retrieving 23,960 records of which 23,824 were distinct.

### The Register Says One Thing and the Laboratory Says Another

**A360 established that the X-63A and X-64A rows are identical in every cell that describes
the machine.** This article found the government document that contradicts the impression
that leaves. The laboratory's own background paper on its rocket propulsion organisation,
cleared September 2022, says **each company has their own launch vehicle and chosen approach**
and ties each designation to its company.

**THAT DOCUMENT HAD NEVER BEEN USED BY THIS SERIES AND NO SWEEP WOULD HAVE FOUND IT.** It is
a public-affairs PDF on a laboratory web site with no report identifier, and it was reached
through the encyclopedia entry's own source list. **A source list at the foot of a secondary
is a retrieval channel**, and it is the channel that produced the sentence this article is
built on. It also quantifies the modularity half of ARISE, which A360 said the fact sheet did
not, the portfolio seeking **70 percent less development time and 50 percent less cost**.

**Two slips in that primary are recorded rather than smoothed.** It writes `into the 22nd
century` twice where it means the twenty-first, and it names nitrogen tetroxide with Aerozine
50 in one sentence and with monomethylhydrazine in the next, which are different fuels.

### A Name Is a Query and a Query Is Only as Good as Its Spelling

Invocon returns **81** award rows of wireless instrumentation, impact detection and radiation
monitors. KT Engineering returns **15**, and **every one of the seven rows the phrase
`segmented launch vehicle` returns in the whole record is this company's**. The announcement
writes `Troy7` and the award record writes `TROY 7`. **`Troy7` returns nothing in any of five
award families and `Troy 7` returns fifteen.** **And the spaced spelling imports a collision
the unspaced one avoided**, matching a router backup and a seven-inch rifle rail, so the more
findable query is the less precise one and both halves of that trade are stated.

### The Keystone, and a Timing Result That Reversed the Expected Answer

**An accelerometer is blind to gravity, which is what makes it the right instrument.** It
reads thrust minus drag over mass, so the largest term in the equation of motion is the one it
declines to see. **Recovering thrust needs a drag model and the drag term is the only one no
instrument on board can reduce.** Holding it to a tenth of A360's 5.3 percent effect needs a
drag model good to **2.65 percent** at a drag fraction of one fifth, and the drag fraction at
which the total error equals the effect is **0.209** for a quarter-accurate model.

**THE EXPECTATION WAS THAT THE CONFOUNDER PEAKS WHERE THE SIGNAL LIVES AND IT DOES NOT.**
Ambient pressure depends on position while drag depends on position and the square of speed,
and a rocket reaches altitude before it reaches speed. **Dynamic pressure peaks 2.10 to 2.48
times later than the half-signal time, and by then between 83.6 and 95.3 percent of the
pressure-time integral is collected.** The trajectory is the instrument.

### Two Power Laws Are Not a Trajectory

Taking A360's altitude exponent of 2 with a speed law linear in time returns a peak dynamic
pressure of **190 kilopascal** and a drag fraction above one, **and a drag fraction above one
describes a decelerating vehicle**. The repair removes an assumption rather than correcting
one, making the published cut-off altitude a constraint. **A model with one assumption too
many will usually tell you so somewhere, and rarely in the quantity you were computing.**

### The Shape, and the Same Polygon A360 Found in the Sky

Two published numbers give a fineness ratio of about five against the RS1's 14.67, so the
frontal area is 1.72 times as large and **one calibre of static margin costs 20 percent of
this vehicle's own length against 6.8 percent for the other**. The tip-over anisotropy is one
over the cosine of pi over N, **exactly the square root of two for four legs**, but the
footprint has N sides for every N where A360's control polygon had N or 2N, **and the
difference is a half-plane truncation rather than anything geometric**.

**Harmonic N sampled at N points has exactly the discrete mean of harmonic zero**, so a
four-legged vehicle with four taps would report its own legs' disturbance as a change in the
thrust-bearing mean, and both phases of harmonic mu need 2mu plus 1 sensors.

### The Equation Pass, 20 to 39

**The largest omission was a structural result that lived in the numerics and never reached
the page**, being the drag fraction in terms of thrust-to-weight and ballistic coefficient,
from which follows the relation that licenses the article's central comparison. Also added
were the geometry relations as scaling laws so the article says which figures are
consequences, the atmosphere's layer forms, the mass history, **the exact axial-force
decomposition that makes the zero-angle-of-attack approximation precise rather than merely
disclosed**, the slender-body slopes that explain why the legs must be fins, the support
function beside the lever arm, and the Fourier estimators with the counting bound. **One
symbol collision forced a change of notation**, A360's gamma for the ratio of specific heats
becoming kappa because gamma was already the flight-path angle.

### The Primary Pass Found a Literature the Drafting Pass Engaged None Of

**Determining thrust in flight is a settled discipline whose own review states this article's
premise in as many words.** That literature is about air-breathing engines, where an inlet
captures a momentum flux no body-mounted instrument can separate from drag, **which is why its
method is gas-path modelling and why a rocket may use an accelerometer**. The inverse was done
once in flight, the XB-70's drag measured by determining its thrust independently. **Thrust
minus drag is one observable and splitting it always costs a model of one side.**

**AND THE ESTABLISHED METHODOLOGY NAMES A TERM THIS BUDGET DOES NOT HAVE.** It separates bias
from precision and carries a model bias error, where this budget combines three terms in
quadrature as though all were random, and a drag model's error is more likely systematic than
random. **So the article now says plainly that it presents a sensitivity analysis and not an
uncertainty statement**, and that a single demonstrator flight is a single-sample experiment.

**Report primaries 45.0 percent against A360's 30.6**, from the fixed fetcher and from the
subject being a report literature rather than a conference one. **Three encyclopaedia anchors
dropped as superseded** by Barrowman, Moffat, and Shannon with Nyquist. **Barrowman 1967 read
in full confirms both halves of a displayed relation**, and the bibliographic index returns
gastrointestinal lymphatics for his name while the reports server holds the document under its
title, **so the two registries hold different literatures rather than the same literature to
different depths**. **Four sources are used from their abstracts alone and say so.**

### The Publication Review

**The superlative scan found four real defects in 158 ranking sentences.** A claim that the
1967 report is what `the whole practice rests on`, which is field-wide and now says it made the
method a convention. That `Invocon was never a launch company`, which an award record cannot
settle and now says the record gives no sign it had ever been one. That `the only image the
encyclopedia entry describes is a three-dimensional printed model`, **which is simply wrong**,
the entry crediting two images and captioning one, so the article now says no photograph of
flight hardware is identified as such in any source consulted. And a claim about `the only
claim this article makes without qualification`, now scoped to drag.

**The drafting-history scan took six instances to two.** The lever-arm inversion is now stated
as the tempting construction rather than as a previous draft, a reference to A360's own review
process became a reference to its finding, and the two kept are the defused coincidence, which
is epistemic content, and `What the Data Changed`, whose purpose is exactly that.

**ARMR first appeared inside a quotation and was never expanded before it.** A quotation cannot
be altered, so the expansion is now in the sentence introducing it.

**And the diction scan found one tic**, the laboratory's key sentence paraphrased four times
beyond its quotation, now twice.

**No unit is missing and no decision is stranded.** Forty recorded decisions were probed
against the article and all forty are present, **the one apparent miss being my probe using my
own report's phrasing rather than the article's**, which is the same class of false failure as
a check whose scope is wrong.

### Verification

| Gate | Result |
|---|---|
| `verify_numbers.py` | **1,531 checks, 0 failures** |
| `neweqns.py` | **466 checks on the new relations, 0 failures** |
| `symcheck.py` | 90 symbols, both directions, 39 display equations, 218 inline, 0 failures |
| `_verify.py` | 302 posts, **0 errors, 0 warnings** |
| `urlcheck.py` | 33 addresses, 30 fetched, **3 confirmed through the registry**, 0 unresolved |
| stub build | clean, **against checksum-matched bytes** |
| `_lib/render.py` | 545 pages, 172 carrying display math, **no findings** |
| rendered article | 912,434 bytes, 8,213 links, 18 tables, 0 unresolved brackets, 0 raw dollar pairs |

### What Comes Next

**A361 IS COMPLETE. FOUR PASSES, COMMITTED AND PUSHED, AND NOT PUBLISHED.** The next article
is **A362, the X-65**, editorial date 2025-12-10, series index 66. The register gives the
X-65A to Aurora Flight Sciences with an engines cell of `1 Williams FJ44-3A` and a DARPA
sponsor, which is the active-flow-control demonstrator.

**THE A358 AND A359 OFFICIALITY CORRECTION REMAINS THE PILOT'S DECISION AND IS UNTOUCHED.**

---

## A360, Publication Review

**THE PASS FOUND A SUBSTANTIVE PHYSICS ERROR, NOT ONLY PROSE DEFECTS**, and it found it by
refusing to let one of its own edits stand unverified.

### The Rule Is Modulo Four and the Article Said Parity

**The article claimed that on an even ring of thruster modules the direction of least
steering authority points straight at a module.** That is true only when **four divides the
module count**. At six, ten, fourteen, eighteen and twenty-two modules the module direction
is the direction of **greatest** authority, as it is at every odd count. The reason is that a
quarter turn is a whole number of module spacings exactly when four divides the count, so
that is the only case in which a module sits on the boundary of the forward half plane when
the command points at another module.

**The closed forms were never wrong**, because they depend only on the polygon's side count,
and every one of the article's authority figures stands unchanged. **What was wrong was the
statement about where the extremes sit**, which is the part an autopilot designer would use.

**HOW IT SURVIVED TWO PASSES IS THE USEFUL PART.** The numerical check evaluated **both**
candidate direction sets and took the extremes over their union, specifically so that it
would not have to assume which set held the maximum. That made the check correct and
**blind to the false rule**. Worse, the comment above it documented the false rule as the
justification for evaluating both sets, **so the wrong belief was written into the verifier
as the reason for the code that made the verifier immune to it.**

**AND I FOUND IT BY CHECKING MY OWN EDIT.** The publication review first replaced a
drafting-history sentence with a tidier one asserting that a naive check reports swapped
extremes `at every even module count`. That was an unverified structural claim, so it was
tested before being trusted, and the test refuted both it and the article's original
sentence. `check_extremal_parity` now pins the rule by enumeration against the modulo-four
condition. The suite is **652 checks to 699**.

### A Withdrawn Phrase Standing in Two Summarising Sections

**The primary-reference pass established that `roughly twice as permissive` is, in the
article's own words, true nowhere**, the correlation crossing the flat four tenths at
separation Mach 2.59 and being stricter below it, with 1.74 times as the correct figure at
the top of the fitted range.

**It then left that exact phrase standing in `What the Data Changed` and again in the
conclusion.** The article asserted in two places the phrasing it refuted in a third.

**No check could see it.** 652 checks passed. **A retracted wording carries no number to
recompute**, so a suite built on recomputing stated quantities is blind to it by
construction. This is the inconsistency the handoff predicted the fourth pass would inherit,
and it was worse than an unsoftened claim, because it was a self-contradiction.

### A Paragraph Refuted by the Paragraph After It

**The Source Base opened by calling the reports server's share thin and `a fact about this
subject rather than about the sweep`**, and closed by saying the primary-reference pass **is
where this imbalance has to be answered**. The subsection four lines below proves the
thinness was a defect in the shared fetcher, and the pass that would answer it had already
run. **Both readings stood in the article's own voice.** The emitter had regenerated the
paragraph's numbers and left the sentences interpreting them exactly as written.

### Caps Emphasis, Cleared Again

**Twelve shouted spans**, converted to bold sentence case. The corpus-wide sweep of commit
65e807f cleared caps emphasis across the series and **this article's third pass reintroduced
it**, five spans in the separation section and seven in the Source Base.

### The Drafting-History Scan, Decided Rather Than Swept

**Twenty candidate lines, reduced to seven.** The handoff was right that this mattered more
than usual, and right that the answer was neither to keep them all nor to cut them all.

**Cut as autobiography**, being sentences that told the reader about a previous draft rather
than about the subject: that the drafting pass implemented the atmosphere and cited an
encyclopedia for it; that the first draft of a sentence rounded two scale heights to
different numbers; that a verifier reported eighteen failures. **The separation section
carried six statements about its own drafting pass and now carries one.**

**Kept and reframed**, being sentences whose content is about the subject: the numerical
lesson that a central difference at a clamped boundary halves its own denominator, restated
as a fact about evaluating the derivative rather than about a first attempt; and the warning
that the regular-ring closed form does not apply to a ring with a module missing, restated
as the tempting move rather than as this article's mistake.

**Kept unaltered**, being the seven in sections licensed to narrate method: `What the Data
Changed`, whose whole purpose is to record what the work overturned, and `The Source Base`,
whose subject is the instrument.

### The Superlative Scan, Which Had Not Been Run

**158 ranking sentences, three real defects.**

**`The largest aerospike ever built is the XRS-2200`** is a ranking over the world's
aerospike hardware made from a survey of publications that **contains no size comparison**.
The corpus holds four toroidal-aerospike records and none of the 1970s large-engine
hardware that would settle it. Now scoped to the largest the survey documents.

**`the matched-expansion condition that every text states as a separate empirical fact`** is
a claim about every text ever written, from an article that read a handful. Now `texts
commonly state`.

**`Seven decades of publication`** sat directly beneath a table whose nine decade rows a
reader would count. Now **seven decades of continuous publication**, which ties it to the
verified continuity from 1956 and is exact to this article's dateline.

Also softened: **`the cheapest error to make`** to `among the cheapest`.

### One Sentence That Was Not Grammatical

`Written the other way round the expression is the negative of the loss, and the first
version of the numerical test was, which is how the sign was fixed` is elliptical past
readability. **The surviving content is the one a reader implementing the integral needs**,
which is that the integrand is the fitted nozzle's exit area minus the envelope's and not
the reverse.

### What Did Not Need Changing

**The style scan is clean.** No contractions, no parentheticals in this article's own voice,
no em-dashes or en-dashes, no prose colons or semicolons. The three parenthetical hits are
inside quoted primary material and were left exactly as the sources write them.

**No unit is missing.** A359 shipped a number with no unit past every numeric check. Twelve
bolded numbers were examined here and each carries its unit in the adjacent clause or is
dimensionless by construction.

**No decision was stranded in the process files.** A359 recorded a decision in `TASKLOG.md`
and this file that never reached the article. Twenty substantive claims the process files say
A360 carries were probed against the article and **all twenty are present**.

**The three numbers a fourth pass usually moves were left alone**, as the handoff directed.
Report primaries stay at 3,748 of 12,231, being 30.6 percent. Display equations stay at 46
and inline expressions at 187, with the symbol table at 73 rows checked in both directions.

### Verification

| Gate | Result |
|---|---|
| `verify_numbers.py` | **699 checks, 0 failures**, up from 652 |
| `neweqns.py` | 246 checks on the new relations, 0 failures |
| `symcheck.py` | 73 symbols, 46 display equations, 187 inline, 0 failures |
| `_verify.py` | 302 posts, **0 errors, 0 warnings** |
| stub site build | 40 seconds, clean |
| `_lib/render.py` | 543 pages, 172 carrying display math, **no findings** |
| `_lib/test_lib.py` | **120 of 120 passed** |
| rendered article | 2,274,470 bytes, 25,054 links, 0 unresolved references |

**The article is 25,796 lines and 159,263 words**, up 145 words, the increase being the
corrected modulo-four passage.

### What Comes Next

**A360 IS COMPLETE. FOUR PASSES, COMMITTED AND PUSHED, AND NOT PUBLISHED.** The next article
is **A361, the X-64**, editorial date 2025-12-09, series index 65, **which shares every word
of its register description with A360**.

**A361 cannot be built the way A360 was, and that is already measured.** `Invocon` and
`Troy7` return nothing at all from the bibliographic index and `KT Engineering` is flooded by
a mechanical-engineering journal with those initials. **Three contractors and no indexed
publications between them.** What A361 has instead is the federal award record, where the
recipient name returns decades of instrumentation contracts, and the contractor's own
physical description of a recoverable vehicle about twelve metres tall landing on four legs
that double as stabilising fins.

**THE A358 AND A359 OFFICIALITY CORRECTION REMAINS THE PILOT'S DECISION AND IS UNTOUCHED.**

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

## A376, Publication Review

**All four passes are complete. The article is committed and pushed and is NOT published.**
Lines 4,443, display equations 89, references 202 at 25.0 percent primary, prose about 23,100
words.

**THE REVIEW REFUTED A CLAIM THE ARTICLE HAD CARRIED THROUGH THREE PASSES.** It said that a
great-power war in which the belligerents hold a minority of world capability would be without
precedent, and that the resulting pool of non-participants was the novel feature of this case. The
same file that produced every other number in the article refutes it. Twenty wars with at least
twenty thousand battle deaths had less concentrated belligerents, among them the Russo-Japanese
War and the Gulf War. **The claim survived three passes because it was reasoned from the two world
wars rather than computed from the ninety-five wars in the file.** The article had a dataset
capable of testing its own central structural assertion and did not point it at it until the
fourth pass.

**COMPUTING IT RETURNED A BETTER RESULT THAN THE ONE IT REPLACED.** Belligerent concentration
predicts belligerent fortune at a correlation of minus 0.225 across seventy-six wars. The
prospective case sits at the ninety-sixth percentile of concentration, and ten of the twelve wars
in its band ended with the belligerents holding less than they started with, at a median of minus
five percent. That supports the article's conclusion by a different mechanism. Nobody captures
anything; concentrated belligerents simply have more to lose. The refuted claim was removed from
the opening, the bystander section, the agreements section, the gaps section and the conclusion.

**STRUCTURAL DAMAGE FROM THE REFERENCE PASS WAS FOUND AND REPAIRED.** Four subsections had been
duplicated, including two making the same allies argument, where the first said a quotation
appeared "earlier" when it appeared forty-six lines later. Four blocks on bystanders, official
assessments, shipping and the fiscal position had been inserted under the Alliances heading with
no topical relation to it. All eight were merged or relocated, and the article now has no
duplicate headings. Two directional references were wrong, one counting "the subsection after
next" when the target is three subsections later.

**THREE QUOTATIONS TAKEN FROM SUBAGENT REPORTS WERE VERIFIED DIRECTLY AND ONE WAS WRONG.** Clauset
and Eichengreen and Flandreau were confirmed verbatim from open-access copies. Lim and Cooper was
confirmed from the author manuscript, which spells "tradeoffs" where the article had hyphenated
it. **A one-character difference in a quotation is still a difference**, and the article now
quotes the verified text and says it is the accepted manuscript.

**A FOURTH CLAIM COULD NOT BE VERIFIED AND WAS REPLACED.** The article asserted that Allison's
project concedes there are no agreed metrics of national power. The page that was supposed to
carry that is dead, and the live essay does not say it. What the live essay does say is that the
cases use rise and rule "according to their conventional definitions, generally emphasizing rapid
shifts in relative GDP and military strength", which supports the same paragraph and is checkable.

**FOR THE PILOT.** The article is ready for a publication decision and has not been published. Its
editorial date is 2026-08-13, the slot is free of other posts, and `post_url` targets resolve
because both back-references point at articles already published. **Publishing will renumber the
series navigation on two live pages** from Part 1 of 2 and Part 2 of 2 to of 3, which is the only
outward-facing change beyond the new page itself.

## A376, Primary-Reference Pass

**References 86 to 202, lines 3,201 to 4,357, display equations 80 to 88, prose about 22,400
words.** Not published. One pass remains.

**THE PRIMARY SHARE WAS THE ASK AND IT ROSE.** Government documents went from 6 to 30 and datasets
from 12 to 20, so primary sources are now **25.0 percent of the external total against 10.5
percent in A375**. The substitutions are the substance of the pass. Alliance commitments are
quoted from the Washington Declaration, the Camp David statement and the Wilmington Declaration
rather than from descriptions of them, and reading them establishes that the Quad document
contains no mutual defence commitment and no extended deterrence language at all. Legislative
figures come from the public laws rather than the aggregates in circulation, which is how the
advanced manufacturing credit turned out to have moved from 25 to 35 percent in 2025. Taiwanese
energy dependence comes from the Taiwanese ministry at 94.62 percent.

**A SCAN DROVE THE PASS RATHER THAN A READ-THROUGH.** Counting citations against word count per
section returned 27 sections carrying none, three of them among the longest in the article.

**A 163-WORD STUB BECAME A SECTION.** `What the alternative instruments say` had asserted that the
instruments disagree while citing nothing at all. It now reports five with their own published
definitions and caveats, and carries the critique literature, including Carroll and Kenkel's
finding that the capability ratio **barely outperforms random guessing** at predicting dispute
outcomes, which is the sharpest objection to this article's own instrument and belongs in it.

**FORTY-FIVE EXISTING ANCHORS WERE NAMED IN PROSE WITHOUT LINKS.** The agreements, disagreements
and epistemic roll-call named authors the article had already defined references for. That was a
correctness defect before it was a density one.

**A PRIMARY DOCUMENT SUPPLIED THE ONE HISTORICAL CASE THE BYSTANDER ARGUMENT HAD LACKED.** Two
Foreign Relations documents record American officials in 1953 worrying about Japanese dependence
on Korean War special procurement, including the fear of "a drastic decline in United States
special procurement following a Korean armistice". That is a bystander gaining materially from a
war it did not join, recorded by the belligerent that was paying for it, as it happened, and it
falls in the same case this article's base rate assigns the largest stalemate effect to. Both
quotations were confirmed against the Department's own published text rather than taken from a
subagent's report.

**WHAT WAS DELIBERATELY NOT ADDED.** Several works the sweeps surfaced were left out because no
claim in the article needed them, and a reference that supports nothing is padding. Where a
quotation comes from a publisher-deposited abstract rather than an article body, the Epistemic
State says so by name.

**VERIFICATION.** `_verify.py` 0 errors across 303 posts, 245 checks across three harnesses with
none failing, build clean, rendered audit no findings across 468 pages, source-to-rendered display
count agreeing at 88, delimiters balanced with no blank-line defects and inline delimiters paired,
zero contractions and zero dashes in prose, zero bullet-list-only anchors, and all 200 reference
URLs swept returning 124 direct resolutions, 73 publisher refusals each confirmed registered by
DOI content negotiation, and 3 empty-202 responses from a publisher that answers that way.

## A376, Equation-Density Pass

**Display equations 39 to 80, lines 2,896 to 3,201, inline expressions 9 to 12, references held at
86.** Not published. The article now carries more display mathematics than either companion at
comparable length, A374 having 63 and A375 75.

**A SCAN DROVE THE PASS AND NOT A READ-THROUGH.** Every prose line carrying a figure with no
display block within six lines was listed, which returned 160 candidates across 42 sections and
made the thin sections obvious. The additions are mostly definitions the article had been carrying
in words, including the component share, the relative change with its equal-length prewar window,
the constant-membership share, the belligerent share and its bystander complement, the exact
contribution decomposition and the scenario map.

**THE SOURCE-TO-RENDERED COUNT CAUGHT EIGHT DEFECTS AND NOTHING ELSE WOULD HAVE.** Eight of the new
blocks closed flush against the following prose, which kramdown folds into inline mathematics.
`_verify.py`, the production build and the rendered audit all passed with them present. **A
scratch build carrying the real configuration and this draft alone now reports 80 source blocks
against 80 rendered**, and the published A375 in the same build reports 75, which is the control
that shows the method measures what it claims to.

**A SECOND RENDERING DEFECT PREDATED THIS PASS AND THE EQUATION WORK SURFACED IT.** Counting
unescaped dollar signs outside display blocks returned an odd number. The odd one was a currency
sign inside a quotation added during the drafting pass, which would have left MathJax with an
unterminated inline delimiter free to consume following text as mathematics. Currency signs inside
quotations are now escaped, the reader sees the character, and the rendered page carries no
literal backslash.

**A FIGURE WAS CHASED TO ITS SOURCE RATHER THAN LEFT IN AN EQUATION UNVERIFIED.** Writing the
ratio of the Iraq cost outturn to the top of the forecast range meant putting a specific number in
a display block, and that number had reached the draft through a subagent quoting a work it had
not retrieved. The open-access Chang and others paper was fetched and the sentence confirmed
verbatim, its two-column layout interleaving exactly as A375 recorded for scanned sources. The
article now attributes the figure to Chang and others attributing it to Bilmes, and says plainly
that it is not independently checked here.

**A THIRD HARNESS WAS ADDED AND DELIBERATELY KEPT SEPARATE.** `verify_derived.py` recomputes 53
pieces of arithmetic the article performs on figures it quotes. It is distinct from the two that
recompute from primary data because it cannot establish that a source says what the article
reports, only that the division printed beside a quoted pair is the division of that pair. The
Epistemic State now says so, and the stale count of 166 constants it carried was corrected to 238.

**VERIFICATION.** `_verify.py` 0 errors across 303 posts, 238 checks across three harnesses with
none failing, build clean, rendered audit no findings across 468 pages, 160 display delimiters
balanced with no blank-line defects, braces and `\left`/`\right` balanced in every block, zero
contractions and zero dashes in prose, all 86 references cited and alphabetically ordered.

## A376, Whether a War With China Would Change the Global Balance of Power, Drafting Pass

**The draft stands at 2,896 lines, 39 display equations, 86 references and about 16,300 words
of author prose**, at the editorial date 2026-08-13, categories `geopolitics military war-gaming`,
series `war_with_china` index 3. Not published. `_verify.py` reports zero errors, `./_check.sh`
builds clean, and the rendered audit finds nothing across 468 pages.

**THE ARTICLE'S SPINE IS COMPUTED RATHER THAN QUOTED.** Two Correlates of War files were
downloaded and the base rate was computed from them, which is the thing the surveyed literature
asserts without measuring. Across 95 inter-state wars the median belligerent gained about seven
percent of relative standing over the following decade, **but 38 percent of winners declined**.
Restricted to wars above 100,000 battle deaths, **every one of eleven losers declined, median
-41.8 percent, while winners gained a median 12.6 percent and more than a third of them still
fell**. The prewar trend has no predictive power for the postwar change, `r = -0.038`, which is an
informative null against the reading that wars merely ratify a trend already underway.

**THE VERSION IN USE WAS WRONG AND THE LANDING PAGE SAID SO.** Work began on National Material
Capabilities v6.0, which ends in 2016. The landing page is titled v7.0 and runs to 2022. Every
figure was recomputed. The base rates barely moved, since the historical data did not change,
but the headline year moved six years and the present-day ratio moved from 1.73 to 1.89.

**THE NUMBER HARNESS CAUGHT TWO ERRORS AND ONE OF THEM BECAME A SECTION.** 185 constants were
re-entered by hand and recomputed. One was a rounding error. The other was a claim that the
capability ratio has exceeded one in every year since 1995; it dips to 0.9987 in 2002. Tracing
that dip found a documented definitional break, the urban component switching from cities over
100,000 to United Nations agglomerations of 300,000 or more. **The break alone removes 2.117 index
points while every other component adds 0.927, and holding urban population at its 2001 share puts
the 2002 ratio at 1.14.** The one year this index does not place China ahead is an artefact.

**A CLAIM WAS WITHDRAWN AFTER A SUBAGENT CONTRADICTED IT.** The draft called the averaging rule a
defect. The codebook documents it, in the same paragraph that says the sums "may be slightly
greater than or less than 1.0". The section was rewritten to credit the documentation and to
contribute the magnitude instead, since the deviation reaches 1.0747 and misses one by more than a
thousandth in 183 of 207 years. **A second false claim, that the 2002 break was undocumented, was
also removed.** The honest contribution is narrower and survives.

**A VALIDATION STATISTIC WAS SHOWN TO BE THE RIGHT ANSWER TO THE WRONG QUESTION.** The project
validated the urban change by a panel correlation of 0.99 on CINC. That bounds the error for a
researcher using the whole panel and bounds nothing for a bilateral comparison, which is what
almost every citation of this index makes. For China the same change is 52 percent of one
component. **A later revision cuts recorded United States urban population by 44 percent in one
year, and the codebook names the United States as the most prominent case.**

**THE STRUCTURAL FINDING IS THE ONE WORTH KEEPING.** The belligerents of 1914 held 82 percent of
measured world capability and those of 1939 held 98. Two states fighting this war would hold about
36 percent, 45 on the widest plausible coalition. **There has never been a great-power war with a
bystander pool this large**, which is why the historical test of the bystander hypothesis returns
nothing and why the mechanism everyone asserts has not previously been testable.

**THE FINANCIAL SERIES WERE PULLED DIRECTLY AND REFUTED A POPULAR CLAIM.** The reserve-composition
data were retrieved from the Fund's own interface and parsed here. The dollar share fell from
75.03 percent in 1999-Q1 to 56.70 in 2026-Q2, **and it fell more slowly after the 2022 reserve
freeze than in the twenty-three years before it**, -0.64 against -0.68 points per year. **The
renminbi's share peaked at 2.85 percent in 2021-Q4, one quarter before the freeze**, and has lost
a quarter of that since. The accelerated-de-dollarisation claim does not survive the series.

**ONE INSTITUTIONAL FACT WAS READ RATHER THAN INFERRED.** The Joint War Committee listed-areas
circular of 16 September 2026 was retrieved and read in full. Taiwan, the Taiwan Strait, the South
China Sea, mainland China and Hong Kong appear nowhere in it, while the Southern Red Sea and
fourteen Middle Eastern entries do. **The market that prices war risk for the busiest container
waterway in the world is charging nothing extra for it.**

**THE RAND TABLE WAS READ OFF AN IMAGE BECAUSE COLOUR DOES NOT SURVIVE TEXT EXTRACTION.** On the
balance-of-power column the ten wars grade one green, six yellow, three red. That count agrees
with A375's independent figure and with a subagent's pixel reconstruction, so three routes concur.
**The three cases where every combatant was wrong are the three largest wars**, which is sharper
than the ratio alone.

**SIX SUBAGENTS SWEPT THE LITERATURE AND THEIR FINDINGS WERE NOT TAKEN ON TRUST.** Load-bearing
quotations were re-verified against retrieved documents, including both RAND volumes read in full
and the RAND commentary page fetched directly. One subagent reported a quotation it had discarded
after finding a summariser had produced text absent from the raw HTML, which is the reason nothing
from a summarising fetcher was used. Several quotations come from publisher-deposited abstracts
because the publishers refuse automated clients, **and the article labels those as abstracts
rather than as the authors' prose**.

**THE CONTRARY EVIDENCE IS IN THE ARTICLE RATHER THAN OMITTED.** Trade modelling puts a
non-belligerent ally's proportional output loss at nearly three times the American one, RAND
estimates Chinese losses at about four times American ones, and the one study taking
non-belligerents as its subject argues a war would derail Indian growth rather than advance it.
Each contradicts a limb of the arithmetic and each is stated as a challenge.

## A375, Pathological Word Usage Pass

**THE ENUMERATED TIC CLASS FOUND NOTHING, BEFORE OR AFTER.** `diction.py tics` reports 0 words at
or above the peer maximum and `report` reports 0 constructions above the corpus maximum. Its own
banner says the class is enumerated and not discovered, so the pass had to find what *this* article
invented. `tmp/a375/pathology.py` compares unigram, bigram and trigram rates against all 258
published posts, with quotations and mathematics stripped.

**THE PATHOLOGY WAS ONE CLUSTER: the article kept talking about itself.** `this article's` at 1.97
times the peer maximum, **`the article above` used six times and never once by any peer**, and it
was the opening sentence of six consecutive survey subsections.

**THE SIGNATURE WORD WAS ONE NO GATE WOULD FLAG.** `finding`, 45 uses, 33 of them the noun
labelling a conclusion, sitting at **2.24 against a peer maximum of 8.56**. **The case for cutting
was repetition and not frequency**, four near-identical bold openers inside one section. A reader
meets that formula four times in a few pages whatever the corpus says.

**THE PASS CAUGHT ITSELF OVER-CORRECTING TWICE.** Varying the six openers put `earlier` into five
of six replacements. Fixing that put `above` into four with two sharing a passive shape. And
redistributing attribution verbs pushed `report that` over the peer maximum. **Each was caught by
re-measuring, not by reading.** This is A374's failure mode recurring, and the lesson is that a
diction fix must be measured after it is applied, exactly like an equation pass.

**WHERE IT STOPPED IS RECORDED RATHER THAN SILENT.** `report that` stays at 1.37 times the maximum
because the peer set is not literature surveys. `own` stays because a source's own words is the
method. All six `article's own` uses stay because each marks the boundary between the article's
arithmetic and a source's.

---

## A375, What Rebuilding Would Take After a War With China, Publication Review

**ALL FOUR PASSES COMPLETE. Committed and PUSHED. NOT PUBLISHED, as instructed.**
References **97 to 222**, display equations **63 to 75**, lines **2,303 to 3,797**,
author prose about **12,800 to 21,000 words**, 16 sections and 40 subsections.

### The opening paragraph contradicted the article's own evidence

The first paragraph said **every major public wargame stops within about three weeks**.
Seventeen hundred lines later the article cites Stewart modelling the campaign
to the seizure of Taipei on **day 46**. The opening now gives the horizon precisely and says
that no public game located continues into the period the article is about, which is both true
and a stronger claim. The conclusion carried the same defect and was fixed with it.

### Three antecedent defects, two of them created by the previous pass

An inserted accountability-office paragraph displaced *the two brackets* from the build-duration
figures it referred to. An inserted note about the Archigos dataset split an attribution from the
figures it introduced, so published rates read as though they came from the current data file.
And **a forward reference was described as backward**, the workforce section citing a report
*cited above* that was first cited 106 lines **below**.
**Inserting a paragraph moves an antecedent, and no checker in this repository sees it.**

### What else the scans found

A date error, the bombing survey said to precede the econometrics by *thirty years* when 1945 to
2009 is more than half a century. A broken promise, the article undertaking to treat Taiwan's
missing reconstruction estimate *below as one of the gaps* when the gaps section did not contain
it; it is now the fifth gap and **the count is recomputed from the bullets**. Two overclaims in my
own prose, including a conclusion asserting that *every* correction made the secondary literature
look overconfident, which was false because two corrections were the article's own. Eleven ranking
claims scoped. Six acronyms expanded, four of which first appear inside quotations that cannot be
altered, so the expansion went into the introducing sentence.

### The survey section, and the finding that reorganised it

Fifteen clusters were added and **125 references**, every one confirmed in a registry with matching
authors, title, year and venue, with a finding attached only where an abstract or full text was
retrieved.

**The best single finding is that three incommensurable quantities wear the same units.** The
circulating cost estimates for a Taiwan contingency run from about two trillion dollars to about
ten, and that is not a disagreement about magnitude. The low end counts activity at risk and its
authors say in their own text that they do not estimate welfare. The middle counts modelled welfare
loss and is far smaller. The high end bundles destruction, mobilisation and panic behind a method
that could not be read. **The only properly specified input-output estimate located, a geological
survey model of a total gallium and germanium cutoff, lands at 3.4 billion dollars**, three orders
of magnitude below the headlines.

### The survey corrected this line's own headline finding

**The twenty-day liquefied natural gas figure is the commission's, carried in its footnotes, and
appears in no Taiwanese government energy series located.** The article now says so and sets
against it the one stockpile that is statutory, 60 days of petroleum held by industry plus 30 by
government. **Petroleum has a 90-day statutory reserve and the fuel the island is moving toward has
none.** Food supplies a third horizon at about six months, so the ordering is gas, coal, food, and
**the binding constraint in a long blockade is energy rather than starvation.**

### The reachability figure was nearly reported wrong

A sweep showed 89 of 219 addresses failing, 87 of them digital object identifiers, which looked
like a corpus problem. Tested individually, the registry resolves with a 302 every time and **the
publisher refuses the client**. The identifier works and the paywall does not. **Writing the
aggregate into the article would have recorded publisher bot policy as a fact about the citations.**

### Verification

`_verify.py` **0 errors and 0 warnings across 302 posts**. **111 arithmetic and structural
statements recheck by script with no failures**, up from 85, and they now include every stated
reference-composition figure recomputed from the list, the agreement and disagreement counts, and
the gap count. Diction reports **0 words at or above the peer maximum**. Build 12.7 seconds,
**rendered audit no findings across 458 pages**, and **source and rendered display counts agree at
75**, which is this line's mandatory check.

### What remains, and it is the pilot's decision

**A375 is finished and unpublished.** The only blocking item is the date.
**`_drafts/android_development_on_freebsd.markdown` still carries the same editorial date,
2026-08-12.** `_verify.py` builds its date map from `_posts` only, so two drafts sharing a date are
invisible while both are drafts and become a hard `date-collision` error the moment either
publishes. The run from 2026-08-20 onward is free of both posts and drafts. **That is a content
decision and it has not been made.**

---

## A375, What Rebuilding Would Take After a War With China, Primary-Reference Pass

**THREE OF FOUR PASSES COMPLETE. Committed, not pushed, not published. Only the publication
review remains.** References **78 to 97**, display equations **50 to 63**, lines **1,448 to
2,303**, author prose about **7,600 to 12,800 words**.

### The pass began by finding a defect the verifier structurally cannot see

**Four references were defined, listed and never cited in the argument.** `_verify.py`
reported zero unused anchors, and it was right on its own terms, because **the References
bullet list cites every anchor**, so a reference that appears only in that list satisfies the
unused-anchor check. The four were the Section 301 maritime report, the annual threat
assessment, the commission's Taiwan chapter and a War on the Rocks essay.

**All four turned out to be precisely the primary documents this pass wanted**, which is why
the defect mattered rather than being cosmetic. The check to run is a citation count against
the body text alone, excluding the bullet list. The article now carries 97 references and 97
cited in the body.

### The best single find is an energy figure that sits on the wargame horizon

The commission's Taiwan chapter reports the island holds storage for **20 days** of liquefied
natural gas and about **42 days** of coal. The published games end at about **21 days**.
**The modelled war ends at about the moment the island's gas runs out.**

That is not a finding about the games, which model an invasion rather than a blockade, and the
two quantities were measured by different people for different purposes. It is a finding about
the aftermath, and it joins to the Heim denial essay, which states that a defeated invasion is
plausibly followed by **a shift to blockade**. **Neither source makes the connection**, and
every reconstruction estimate in the article assumes electricity is available to rebuild with.

The same chapter supplies the thesis at the smallest scale anyone has tested it. Undersea
cables to the Matsu Islands were cut in 2023 and the islands were offline for weeks; cut again
in 2025, backup installed in between kept services running. **The repair time did not improve.
The redundancy did.**

### And the European bombing survey measured the thesis in 1945

In the anti-friction bearing industry, building destruction equalled about **half the preraid
floor space** while **machine tools destroyed equalled 12 percent of the original inventory**.
The survey adds that "it proved more difficult to put the plants out of operation than had been
foreseen". **The article's organising claim, that what bombing destroys is production rather
than the means of production, is a 1945 finding before it is a 2009 econometric one.**

### Six corrections came from reading the primaries behind secondary accounts

- **Japanese damage figures disagree with the survey Davis and Weinstein cite.** 2,510,000
  buildings against the paper's 2.2 million, 330,000 fatalities against three hundred
  thousand, and the important one is a difference of subject: **the survey's 40 percent is
  built-up area destroyed**, where the share who lost homes is about 30 percent. **An earlier
  draft additionally inserted the word urban into the paper's sentence**, producing a claim
  that matched neither source.
- **Quinlivan 1995 states no 20-per-thousand rule.** It is descriptive, sectioned by ratio
  band, and reaches 20 per thousand as a measured value in two cases. The norm was hardened by
  FM 3-24 of 2006, which credits nobody, and **the 2014 revision deleted the ratio entirely**.
  The number the central calculation uses is in no current doctrine.
- **Taiwan's population was stale and unsourced.** The ministry series is now cited and the
  requirement is **465,980 rather than 468,000**, with the declining trend stated.
- **The 395-ship figure is a 2023 projection and not a count**, and the 2025 edition of that
  report gives no fleet total at all.
- **The Ukrainian damage growth is the report's own 15.5 percent**, not a ratio of rounded
  inputs giving 16.
- **The Nature Food claim was too strong**, since the largest scenario assumes attacks on
  seven countries including China.

**One claim was strengthened instead.** The 2025 National Academies report, read in full,
carries **no economic recovery analysis and no recovery timescale for human systems**, and
names that as a research gap itself. **The only official study with a recuperation analysis is
the Office of Technology Assessment's of 1979**, which said that the effects which cannot be
calculated "are at least as important as those for which calculations are attempted".

### Two methodological findings worth keeping

**A failed string match is not evidence of a bad quotation.** Nineteen quotations verified on
first match; several more failed and were confirmed only after normalising for scanned
hyphenation, two-column interleaving, and a running header that fell inside a sentence.
Every quotation was confirmed against source text rather than against an agent's report of it,
and three delegated leads needed correction.

**The user agent cuts both ways.** Nine addresses answer a browser string and refuse an honest
one carrying a contact address, while `archive.dni.gov` and `documents.worldbank.org` do the
exact opposite. **A single-agent sweep therefore reports blocks that are properties of the
client**, and a two-agent sweep took reachability from 70 to 79 of 94. Separately, `osti.gov`
answered a throttled sweep with HTTP/2 stream resets rather than a status code, which is a
transport failure and must not be recorded as a 403. Both are now in `URL_VERIFICATION.md`.

### Verification

`_verify.py` **0 errors and 0 warnings across 302 posts**. **85 arithmetic statements
rechecked by script with no failures**, up from 53. Diction reports **0 words at or above the
peer maximum**, the earlier deliberate flags having fallen as the article grew. No prose
colons, semicolons, parentheses, dashes or contractions. Build 12.7 seconds, **rendered audit
no findings across 458 pages**, and **source and rendered display counts agree at 63**, which
is the mandatory check this line earned the hard way.

### What remains

**The publication review, which is the fourth pass.** Under the standing instruction it must
also make the article a comprehensive survey of the contemporary literature, with no length or
reference limit. **The 2026-08-12 date still collides with the
`android_development_on_freebsd` pre-release candidate**, invisible to the verifier while both
are drafts and a hard error the moment either publishes. That remains the pilot's content
decision and has not been made.

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
