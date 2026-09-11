# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

## Last Updated

**Date**: 2026-09-10
**Task**: **A356, X-Planes: Lockheed Martin X-59 Quesst, publication review. The fourth and
last of four.** Committed and **PUSHED**. **Not published**, and publication of the series
still not authorised. **Sixty of seventy-two drafted, twelve remain.**

---

## Five Claims Were Wrong and the Article Names Them Rather Than Deleting Them

**THE DRAFT SAID A CORPUS CHECK HAD NEVER ONCE FIRED ON THIS SERIES. IT HAS.** `_verify.py`
gates a survey cluster row against its own citation count by matching a line that begins with
the record count in bold and carries the citations on the same line. **Thirteen articles of
this series, A339 through A351, used exactly that format.** It was then lost for four
articles and this one restores it. **Losing a check makes it silent rather than failing,
which is why nobody noticed**, and it is why the draft's version of the paragraph was wrong
in the confident direction.

**AND THE ARTICLE CARRIED THE FALSE CLAIM AND ITS CORRECTION AT THE SAME TIME.** A patch
script asserted partway through and discarded its own earlier edit, the emitter was never
re-run, and the source base kept the false paragraph while the epistemic state carried the
repair. **Reassembly did not catch it, because the article was a faithful assembly of a stale
block.** The verifier now re-runs the emitter and compares its output before comparing the
article to its sources.

**The equation pass said slenderness is bought at a discount.** Wave drag falls as the fourth
power of length and wetted area rises as the first, which establishes a direction and not a
balance. **Whether the net drag falls depends on how the total divides at the design point
and no source publishes that division.**

**The draft called the difference between the two register entries the difference between
measuring a phenomenon and manufacturing one.** Both entries describe an aeroplane that would
make signatures. **The difference is the adjective and nothing else.**

**The draft said everything the register says is in the future tense.** The entry says the
aircraft **is** a research aircraft and **will create** a shaped signature. Half of it had
been true since rollout.

---

## A Numeric Verifier Cannot Check a Claim That Contains No Number

**The injection suite proved it by reverting two of the corrections above without a single
check going red.** Both were prose.

**The answer is a list of withdrawn formulations that must not reappear**, which is a
regression guard and not a test of truth, and the article says so. **Writing that list found
two more live overreaches that three passes of reading had missed**, being a claim that one
relation was the most useful single fact in the subject, which is a ranking with nothing
behind it, and a claim that length was the only variable the design has, which the article's
own later sections contradict.

**The guard has to exclude the section that names the corrections**, because this series'
convention is to name a retracted claim rather than delete it, so the withdrawn wording
appears there legitimately.

---

## Two Superlatives Checked, Two Failed

**Thirteen store families are open, which is as many as any article in this series has opened
and not more.** The other is the [X-54], **which is the other sonic boom article.** That
coincidence is worth more than the superlative was.

**Nothing remaining thin after the harvest is true of the four preceding articles and is not
claimed of the other fifty-five**, because they were not checked.

---

## The Cluster Order Was Wrong, Which Is A353's Lesson in Miniature

**A boom is heard indoors as a building moving**, so what a boom does to a building is a
special case of what it does to a person, and the human-response cluster was placed above it.
**Of 57 kept records about structures, windows and rattle, 14 were being taken by the general
cluster.** The specific cluster now precedes it, as the rule has said since A353.

---

## Fourteen Conclusions Probed, Fourteen Covered

**Four of them had never been probed at all**, because the probe was written in the first
pass and the equation and reference passes added conclusions without going back to it. **That
is A349's defect met from the other direction**, a conclusion written before half the findings
exist becoming a probe written before half the conclusions exist.

**Eight of fourteen measure thin under the article's own words and fourteen of fourteen are
covered under the field's**, and nothing remains thin.

---

## What the Article Now Says, and What It Refuses to Say

**Of 526 allocation rows exactly 2 mention a sonic boom and the word create appears in 1.**
The other boom row is the X-54, never built. **The difference between the two sentences is
one adjective.**

**The weight rather than the shape sets most of the signature.** The lift term of the
equivalent area integrates to the weight over twice the dynamic pressure with every trace of
shape gone, being 4.232 square metres, **and it grows by 2.06 between forty thousand feet and
the design altitude**, so two of the things altitude does to a boom are opposed.

**Loudness is set by rise time, classical theory is short by 192, and the absorption is short
by 31.** Both are repaired by molecular relaxation, so **a predicted perceived level is a
prediction about the weather as much as about the aeroplane**.

**The claimed reduction is 47.8 percent in sones and not the ninety percent that is
published**, which is a pressure ratio of 85 percent reported as a loudness.

**Across five governing documents and 206,232 characters the programme's own metric appears
0 times**, the aeroplane is named 0 times, and in 2021 the agency wrote that the
determination made in the 1970s that no level of sonic boom is acceptable over land still
applies. **The only noise standard ever proposed for these aeroplanes governs them while
flying subsonically and was never adopted.**

**The carpet is 59.2 kilometres wide and the boom lands 19.29 kilometres behind**, from a ray
tracer checked against the literature's Mach 2 rule of thumb to within 3.9 percent.

**At the editorial date the aeroplane had flown once, subsonically, with the gear down.**

**And it refuses to say** whether the net drag falls, what the range is, whether the X-59
needs an authorisation at all, and whether the aeroplane will meet its number in flight.

---

## Verification

**Verifier clean at 0 errors and 0 warnings. Tests 111 of 111. Lint 0 defects and 3
convention findings**, two of which are one display equation whose tall bracket a
source-level scanner reads as a broken link. **The symbol scanner reports all 92 declared
symbols used and every symbol used declared.**

**The article verifier runs 144 checks and 82 injected defects were all caught with the total
reassembly check disarmed.** **Three went green at first**, two because they were prose
claims carrying no number and one on a stale anchor.

**Identifier verification passed seven hand-written addresses on content**, including the
builder's card on a figure the article quotes, **both regulation sections against the copies
they were quoted from and against the live page, 24 of 24 sampled report primaries, and a
fabricated identifier resolving to nothing.**

**Every regulatory block quote is matched verbatim against the retrieved text of the document
it came from.** All 16 cluster rows state their own recomputed count, the total equals the
research count exactly at 4,340, and all 4,455 definitions are cited with none orphaned and
none undefined.

**FINAL STATE. 10,072 lines, 51 display equations, 92 declared symbols, 4,455 reference
definitions, 63,424 words**, research 4,340, report primaries 808 at 18.6 percent, six sweeps
retrieving 22,654 records of which 18,330 distinct, gate 4,568.

**The stub-isolated production build succeeded against the exact bytes committed**, the
checksum matching draft, stub copy and frozen record. **The rendered audit reports no findings
across 95 pages.** Source and rendered display-equation counts agree at **51**, with zero raw
dollar pairs, zero unresolved reference brackets and zero unrendered Liquid. The page is
882,606 bytes.

---

## What Remains

**A356 is complete at all four passes.** The next new article is **A357, the X-60**, editorial
date 2025-12-05, series index 61. **Twelve articles remain**, ending at editorial date
2025-12-16.

**Two repairs are still awaiting a pilot decision**, both verified live on 2026-09-10.
A350 carries a duplicated `## The Contemporary Literature` heading at lines 412 and 414, and
A324 carries a malformed `book_jenkins` label over a correct key.

**And one repair this article's findings imply but did not make.** Four articles of this
series present no per-cluster record count at all and one presents it in a shape the corpus
check cannot read. **Bringing A352 through A355 into the gated format would put 
approximately fifty more rows under the corpus gate**, and that is a change to published
drafts rather than to this article, so it is recorded rather than done.

**Nothing is published and publication of the series has never been authorised.**
