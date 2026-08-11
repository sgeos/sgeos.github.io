# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-10
**Task**: A328 second publication review, run after the primary pass. Committed and **pushed**.
**Not published.**

**Final state: 30,008 lines, 55 display equations, 9,322 reference definitions, 162,918 words**,
with all 9,249 master records cited. All thirty-two articles remain in `_drafts/`.

---

## A Second Shared-Library Defect, and It Is the Same One Wearing a Different Delimiter

**A327 found that a `$$` in a citation title opens a MathJax display block and swallows the page.
This pass found the inline form.** A harvested title began with `\(` and `\mathcal`, and after the
command rule and the brace rule had run, the link text still carried **bare backslashes**, because
the character after the backslash is punctuation rather than a letter and the command rule never
reaches it.

`refs.clean` now removes any backslash that survives that far. `test_lib.py` gained a regression
test **inserted above the discovery loop** and stands at **48 of 48**.

**Both defects were found by reading rendered link text.** Neither was found by a checker, and the
rule that keeps producing results is to scan every entry in the reference list for punctuation that
does not belong there. **16,953 entries were scanned this pass** and, outside the 31 series titles
whose colon is part of the title, none remain.

---

## The Contemporary Survey Was Measured Again Rather Than Assumed

**Two harvests aimed at the programme window could easily have left the modern half behind. They
had not.** Coverage from 2015 onward stands at **6,067 records, and 2,842 of those were published
from 2022 onward**, so the survey reaches the present rather than stopping a decade short.

**Two contemporary subjects had no heading at all, and both bear on the article's own argument
rather than merely being recent.**

**Fluidic thrust vectoring is the direct successor to the paddles the article spends a section
on.** It deflects the exhaust by injecting a secondary flow, with no vane in the stream, nothing to
actuate and nothing brittle to crack, which answers the weight and reliability objection the paddle
choice was made against. **The scaling is unchanged**, because a fluidic system still produces a
moment proportional to thrust, so its authority still falls as one over dynamic pressure and still
lapses with altitude. The mechanism is different and the physics that set the X-31's departure
boundary is identical.

**Assurance of learning-enabled flight control is the certification problem created by the
autonomous air combat work the article already surveys.** An article reporting that learned
policies now fly the engagements six test pilots once flew, without reporting that nobody knows how
to clear such a policy for flight, has surveyed half its subject.

**The connection to this aircraft is closer than it looks.** The X-31 already carried the
architectural idea. Its quasi-tailless experiment had an automatic safety disengagement on system
failure or envelope exceedance, which is a run-time assurance monitor in all but name, built in
1994 because nobody was willing to fly a deliberately destabilised aeroplane without one. **And the
accident is the counter-example**, since it was not a control law behaving unexpectedly but a
correct control law fed a wrong number, which is the failure mode that no amount of verifying the
controller addresses.

---

## The Primary Base Was Thin and the Measurement Said So

**The measurement came first and it was the reason for the pass.** The reference set held 7,097
records and only **666 of them, 9.4 percent, fell inside the 1985 to 1996 programme window**. For
an article about an aircraft that flew from 1990 to 1995, that window is the primary base.

**The thinnest clusters were the ones carrying claims.** The aircraft's own literature stood at 21
records in the window. The keystone combat-utility work stood at 35. The measured asymmetries the
departure boundary rests on stood at 21, post-stall manoeuvring at 16, the gain scheduling the
accident rests on at 15, agility metrics at 12, unstable dynamics at 9, the tailless work at 8, and
control power at 7.

**Two harvests took the window from 666 records to 1,762 and its share from 9.4 percent to 20.9.**
The whole set went from 7,097 to 8,440 and every record is cited.

**The vehicle's own cluster reached 36 records and one of the new ones matters more than the
rest.** It is the flight-test companion to the tactical utility paper the keystone rests on,
alongside a frequency-domain identification of the unstable airframe from flight data and the
low-speed aerodynamic characterisation of the configuration.

---

## Why the Earlier Rounds Missed It, Which Is a Reusable Finding

**The cause was mechanical rather than editorial.** The reports server caps a search at ten results
and is sensitive to phrasing, so a broad query returns ten records and a narrow one returns ten
DIFFERENT records. Five harvests of broad questions had left that pool at 252 records for a
programme NASA documented extensively. Roughly a hundred and seventy narrow questions took it past
five hundred.

**The conference harvest also carried no date filter**, so it was dominated by modern work.
Restricting the same publisher prefix to the programme window reached the papers the programme's
own engineers wrote.

---

## Two Subjects Reported as Thin Rather Than Padded

**Agility metrics did not move at all.** A harvest aimed directly at it in every phrasing the
period used returned 14 in-window records, exactly as before. That is not a failed query. The
agility-metrics literature of the late 1980s is concentrated in a handful of papers, and the
subject then dissolved into energy manoeuvrability and trajectory optimisation rather than growing
into a field of its own.

**Control power stands at 13 and is thin as a heading rather than as a subject.** The work exists
and the article cites it, but it lives inside the high angle of attack and departure literature,
because a paper about control power at high incidence is filed as a paper about high incidence.
Checking before reporting a gap is the rule, and the check says the gap is in the filing.

---

## The Reference Base

**References 1,054 to 9,322 definitions and 981 to 9,249 cited across the reference and
publication passes. Every anchored record is cited and none is left over.**

The audit at the start of this pass found **3,908 of 4,889 master records uncited**, which is the
A327 bookkeeping lesson repeating. Two harvests, one aimed at the subjects the equation pass
promoted and one at the contemporary sweep the standing directive asks for, took the master to
7,097.

**THE COUNT-VERSUS-FRACTION TRAP FIRED IN BOTH DIRECTIONS AND THEN REVERSED.** At the publication
pass the period count rose from 1,221 to 1,393 while the period fraction fell from 44.9 percent to
19.6, because nearly four thousand contemporary records arrived underneath it. At this pass the
movement went the other way, the period count reaching **2,622 through 1996** and its share
recovering to **31.1 percent** as the primary harvest landed. **Nothing was removed at any point**,
and the Source Base carries a table by band so every movement is visible.

**Four subjects the equation pass promoted had no cluster at all** and each now has a subsection of
its own, being the standard atmosphere, engine thrust lapse, airspeed systems as a measurement
discipline, and the axis transformations behind a velocity-vector roll.

---

## Citation Gaps, and the Seven That Should Stay

**Twenty displayed equations carried no nearby citation and seven still do.** The seven are the
weighting identity, the two-point bracket, the tipping weight, the same bracket applied to the
other two comparisons, the flight-rate bookkeeping and the ratio between the two simulation
campaigns.

**Every one of those is a construction original to this article rather than a result taken from a
source, so attaching a citation would be false attribution.** The article now says that in its own
words rather than leaving the gap unexplained, and it draws the distinction against the other
relations, which are standard results and now carry their literature.

---

## Three Selection Defects, One of Them Self-Inflicted

**A pattern for the International Standard Atmosphere abbreviation matched the journal ISA
Transactions.** Because the cluster test runs against title and venue together, every paper in that
journal landed in the atmosphere cluster. **That is a homonym I created for myself in the previous
pass**, and it is the same class as the ones the article warns about.

**A pattern for engine models matched a transient heat-transfer study**, which is a phrase too
loose to carry the meaning intended.

**The `schedul` anchor stem, added for gain scheduling, admitted job-shop and flow-shop scheduling
from operations research.** The contamination was small at two records, and the filter is recorded
so it carries forward.

---

## A Shared-Library Defect, Found on the Page

**Thirteen records with Chinese, Russian and Ukrainian author names produced anchors reading
`research___2023`.** The stem was built from two folded author names, both folded to the empty
string, and the fallback did not fire **because a lone underscore is truthy**. One record's link
text rendered as nothing but a year.

`_lib/refs.py` now prefers an author name that survives folding, which **recovers** the records
where Crossref supplies both a Cyrillic and a Latin form of the same name rather than discarding
them, and falls back to the title where no such form exists. `test_lib.py` gained a regression test
**inserted above the discovery loop** and stands at **47 of 47**.

**This was found by reading the rendered link text, not by any check.** It is the same lesson as
the two word-boundary variants in the earlier passes.

---

## One Record Dropped Rather Than Weakening a Gate

**An econometrics working paper on temporal aggregation bias has a title that opens with a
contraction.** The corpus rule is that link text is prose and prose carries no contractions, and a
published title cannot be altered without misrepresenting it.

**The record was dropped rather than rewritten and rather than weakening the corpus-wide checker.**
The loss is one record in seven thousand, and it is recorded here rather than hidden.

---

## Publication Checks

Prose style clean, with **zero em dashes, zero en dashes, zero contractions, zero prose
parentheticals, zero prose colons and zero prose semicolons** in the body. Every colon traces to
the YAML front matter, and the single parenthesis and semicolon to the `console.log` debug tag.

**Diction clean, and the two flagged items are legitimate rather than filler.** The word `aircraft`
runs at 8.08 per thousand across 123 uses and `angle of attack` appears 49 times. The first is the
article's subject noun and the second is its keystone quantity, so both stay and the judgement is
recorded rather than left implicit.

**Acronym spell-out verified.** The National Aeronautics and Space Administration is expanded at
character 873 against a first acronym use at 14,186, which is itself inside verbatim link text.

**Structural conformance confirmed**, with all twelve genre sections present plus the three series
sections, and The Source Base immediately before Epistemic State.

---

## Final Verification

**107 of 107 numerical checks passing, none importing the calculation**, with all article-facing
values confirmed present in the draft.

`_verify.py` at the 21-warning baseline with zero errors, check_any clean, `_lib/test_lib.py` at 48
of 48, and reference integrity at 9,322 with zero undefined, zero orphaned and zero malformed
anchors. Citation gaps held at seven, all of them constructions original to this article.

**The final set swept with zero hard failures**, including **all 307 NTRS identifiers**, 600 of
8,382 sampled journal DOIs, 160 of 562 sampled DTIC DOIs, and all 15 books and 25 curated URLs,
with **zero search-endpoint citations**. The three reported mismatches are author-display
differences on title-derived anchors rather than bad citations.

**A 32-article isolated build renders the page at 2.16 megabytes, 16 sections, 98 subsections, 22
tables, 18,928 list items and all 55 equations**, with zero broken anchors, zero empty headings and
zero stray backslashes in link text.

---

## What the Article Concludes

**An exchange ratio is not a property of an aeroplane. It is a property of an engagement**, and the
adversary has a say in which engagement occurs. The programme measured that with more care than
anyone had before, and the measurement is usually quoted as a single number by people who did not
read the table it came from.

**The headline figure sits on a knife edge.** Between 81.9 and 93.6 percent of the aircraft's
simulated losses fell in the two starting conditions where it was behind, and the share that would
have driven the pooled ratio below parity is 92.14 percent, which lies inside that bracket.

---

## Awaiting Instruction

**A328 is complete, with all four passes done.** Thirty-two of seventy-two drafted, **none
published**.

The next article to draft is **A329, the Boeing X-32**, editorial date 2025-11-07, series index 33.
**It inverts this one.** The X-31 was a demonstrator that never competed for a production contract
and answered a research question. The X-32 was a competitor in a procurement, it lost, and the
question it answers is what a fly-off decides and on what evidence.
