# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

## Last Updated

**Date**: 2026-09-12
**Task**: **A357, X-Planes: Generation Orbit X-60, primary-reference review.** The third of
four passes. Committed. **Not pushed and not published**, and publication of the series
still not authorised. **Sixty-one of seventy-two drafted, eleven remain.**

---

## The Count and the Fraction Both Rose

**REPORT PRIMARIES 1,430 TO 1,846, A GAIN OF 416, AND THE FRACTION 31.8 PERCENT TO 34.9.**
The directive is to report the count as well as the fraction, because adding a contemporary
survey lowers the fraction while leaving the count unchanged and reporting only the fraction
reads as a regression when it is the directive working. **This time both moved the same way**,
which is the easy case and is stated with the count first regardless.

**THREE FURTHER SWEEPS WERE RUN AND THEY WERE AIMED AT THE REPORT SERVERS**, because a report
primary is an original result and a journal record usually is not. The space agency's server
is capped near ten records a question and is therefore bought with questions rather than with
patience, so the three sweeps asked 164 narrow questions and almost nothing of the
bibliographic index.

**THE YIELD PER QUESTION FELL FROM 8.8 TO 6.7 ACROSS 302 QUESTIONS.** That is what a capped
server returning overlapping answers looks like, and it is the measurement that says when to
stop asking rather than a feeling about diminishing returns.

## Five Hand-Written Primaries, and a Dead Link the Draft Carried

Each was fetched and read before it was written down. **The small-business award record**, a
separate document from the contract record. **The sounding-rocket user handbook**, which is
this vehicle's ancestry in the operator's own words. **The definitions section of the launch
regulations** and **the 2020 rule that consolidated launch licensing**, which is nine months
after the X-60A's planned first flight, so the programme spanned the change. And **the
conference paper describing the vehicle that later flew this one's engine**.

**THE SPACEPORT'S OWN ADDRESS WAS DEAD AND HAD BEEN THROUGH TWO PASSES.** It returned a 404
and survived because `verify_ids.py` checked a hand-picked list rather than every hand-written
address. **A verifier that inspects a chosen subset of its subject reports a clean subset**,
which is the same defect the equation pass found in the assembler's placement check. It now
sweeps all of them. **58 reachable, 3 refused by hosts known to refuse automated fetches, 0
dead.**

## Two Federal Records Disagree by Six Months and the Modifications Reconcile Them

**THE AWARD RECORD ENDS THE AWARD ON 31 AUGUST 2022 AND THE CONTRACT RECORD RUNS TO 28
FEBRUARY 2023.** A six-month discrepancy between two government databases usually means one is
wrong. **Neither is.** Three modifications fall after the award record's end date and the
first of them is a no-cost time extension, which is precisely the instrument that moves an end
date without moving any money. One record states the award as awarded and the other as
extended.

**The award record also carries the programme's abstract cut off in mid-word**, ending
*validate the f*, which is an artefact of the database and is recorded because a reader
following the citation will see a sentence that stops.

## The Budget Model Was Wrong by Half and the Limit Was Held Anyway

**THE DRAFT PASS DERIVED ITS CITATION BUDGET FROM A MICRO-BENCHMARK OF KRAMDOWN ALONE**, which
gave an exponent of 3.04. Extrapolating that to 6,061 definitions predicted a 317 second build.
**The build took 474.**

**THE EXPONENT IS NOT CONSTANT. IT RISES WITH THE COUNT.** Fitted between the two full
production builds actually measured, being 173 seconds at 4,628 definitions and 473.7 at 6,061,
**the local exponent is 4.83**. A micro-benchmark of one stage is a worse calibration than a
measurement of the whole thing, and the whole thing is what the deploy gate runs.

**THE LIMIT WAS STATED BEFORE THE COUNT WAS KNOWN AND IT WAS HELD RATHER THAN MOVED.** A
five-minute limit overran by half, and the repair was to correct the model and cut the budget,
not to raise the limit after seeing the result.

**AND THEN THE CAP WAS FOUND TO BE BINDING ON THE WRONG SET.** It solved a time limit for a
total and applied that total to the harvested records alone, leaving the hand-written block
outside it. **The markdown processor does not know which definitions were typed by hand**, so
the cost follows the total, and the whole of a seven percent overrun was those 133 references.
The cap now binds on every definition and the article carries exactly 5,413 of them.

**THE CORRECTED MODEL ALSO EXPLAINS THE BUILD THAT NEVER FINISHED**, putting the first
assembly's 10,882 definitions at 118 minutes rather than the 25 the old model gave. **A
prediction of 25 minutes for a build that had already run past thirty when it was stopped
should have been the clue that the exponent was wrong.**

## One Sample Is Not a Measurement

**THE BUILD AT THE SHIPPED COUNT WAS RUN TWICE AND TOOK 275.1 SECONDS AND THEN 305.0**, on an
otherwise identical input. That is **10.9 percent of run-to-run variance**, and the slower
sample is 1.7 percent over the stated limit. **The budget therefore sits at the limit rather
than comfortably inside it**, and reporting only the faster sample would have been choosing
the favourable one, which is the same failure as quoting the model that agreed and not the one
that did not. Both are in the article.

## The Before-and-After Is Now Emitted From Data

**THE DRAFT PASS WROTE `13.3 PERCENT OF 10,754` INTO THE EMITTER AS A LITERAL.** It was true
when written and would have stayed in the article unchanged however the figures moved.
**A hand-typed comparison to an earlier pass is A342's stale-statistic defect with a longer
fuse.** The comparison now reads `pass_history.json`, which each pass appends to, and the
file carries this pass's figures under `current` for the next one to promote.

## The Injection Suite Found the Same Defect a Third and a Fourth Time

**78 OF 92 ON THE FIRST RUN AFTER THE PASS.** Fourteen new survey figures had been added with
no article-side checks. That is the draft pass's defect and the equation pass's defect met
again in the same article.

**AND THEN 92 OF 96**, because four of the checks written to fix that were **bare presence
checks**, which A355 established cannot hold a small number in a document full of numbers.
Anchored properly the suite is **98 of 98**.

**THE PATTERN IS NOW UNAMBIGUOUS AND IT IS WORTH CARRYING FORWARD.** Every pass of this
article added prose faster than it added checks, and nothing except the injection suite ever
noticed. **The suite should be run after every pass rather than at the end**, and the check
written for a new figure should be anchored rather than a presence test.

## Two Smaller Repairs

**A DUPLICATE BUDGET CHECK IN THE VERIFIER WENT STALE.** Two checks of one fact in two places
is two places to go stale, which is the rule this article applies to its own computations and
had not applied to its verifier.

**AND A `cd` THAT FAILED SILENTLY SKIPPED AN EDIT.** The five hand-written primaries were
written into a heredoc whose working directory was wrong, the shell short-circuited, and the
edit never landed. **The verifier caught it as five undefined citations**, which is the
failure mode that apparatus exists for.

## Verification

**Verifier 0 errors and 0 warnings. Tests 112 of 112. Lint 0 defects and 1 convention
finding**, which is the intended multi-line equation form.

**The article verifier runs 268 checks and passes all of them**, measured by counting its own
output lines. **The symbol scanner reports all 126 declared symbols used and every symbol used
declared.** **Identifier verification passed on content**, with twelve hand-written addresses
checked against a phrase each must contain, six quoted documents checked against the copies
they were quoted from, the live statute checked against the saved copy, every remaining
hand-written address swept for reachability with none dead, 23 of 24 sampled report primaries
resolving, and a fabricated identifier resolving to nothing.

**The stub-isolated production build succeeded against checksum-matched bytes**, run after the
injection suite released the article rather than beside it. The rendered audit reports no
findings. Source and rendered display-equation counts agree at **83**, with zero raw dollar pairs,
zero unresolved reference brackets and zero unrendered Liquid. The build measured 305
seconds and the page is 1,044,904 bytes.

**FINAL STATE. 12,131 lines, 83 display equations, 126 declared symbols, 5,413 reference
definitions, 75,243 words**, research 5,282, report primaries 1,846 at 34.9 percent, six
sweeps retrieving 45,900 records of which 34,673 distinct, gate 11,708 under a 5,413
definition budget solved from a 300 second build limit.

## What Remains

**A357 has completed three of four passes.** The publication review is a separate pilot prompt
and has not been run.

**Two repairs are still awaiting a pilot decision.** A350 carries a duplicated
`## The Contemporary Literature` heading at lines 412 and 414, and A324 carries a malformed
`book_jenkins` label over a correct key.

**And the fourth-article format decision carries forward.** A352 through A355 present no
per-cluster record count in a shape the corpus check can read.

**Nothing is published and publication of the series has never been authorised.**
