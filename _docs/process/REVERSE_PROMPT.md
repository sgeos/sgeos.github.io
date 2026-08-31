## Last Updated

**Date**: 2026-08-31
**Task**: **A341 primary-reference review, the third of four passes.** Committed, **not pushed**.
**This commit also carries the equation-density pass**, which was verified but not separately
committed because you prompted for the third pass while its build was still running and the tree
cannot hold a state it has already moved past. **Both passes are described below.** Nothing published
and publication still not authorised.

---

## The Number the Pass Existed to Move

**Report primaries went from 612 to 2,141, or from 6.0 percent of the corpus to 18.3.** Primary sources
on the broader definition, counting NASA and Defense Technical Information Center reports together with
AIAA, SAE and Department of Energy identifiers, went from **5,026 of 10,187 at 49.3 percent to 6,555 of
11,716 at 55.9**.

**The period statistics moved the other way and I am reporting both numbers because only one of them
looks like a change.** Records from 2015 or later rose in count from 3,779 to 3,807 while their share
fell from 38.9 percent to 33.9, and records predating 1970 doubled from 454 to 901. The median
publication year moved back from 2009 to 2006. **The corpus did not become less current, it became
deeper in the era the relations come from**, and reporting only the fraction would have made a
deliberate improvement read as a regression.

---

## The Subject Audit Was Wrong About Nine Subjects Out of Twelve and I Ran It Twice

**This is the finding of the pass and it is about my instrument rather than about the literature.**

Written in the article's own vocabulary, asking for `tail volume` and `vertical tail sizing`, the audit
reported the article's own comparison baseline at **eleven records with one report primary.** Rewritten
in the field's vocabulary, asking for directional stability and control, for the vertical tail in any
construction, for the empennage and for lateral-directional characteristics, **the same pool returns
204 records with 32 report primaries, and nothing was harvested between the two measurements.**

The same correction moved the slender-body subject from 9 to 262, the drag polar from 12 to 77 and the
loop bandwidth subject from 2 to 38. **Nine of the twelve promoted subjects were never thin.**

**A narrow instrument reports a thin literature rather than a bug**, which is why this is invisible in
every summary statistic, and it is the third time the series has recorded it. I had the lesson in front
of me from the handoff and wrote the patterns in the article's words anyway.

---

## Three Subjects Are Genuinely Thin and Each for a Different Reason

**Naming which kind each one is matters more than the counts, because none of the three is a gap that
harvesting could close.**

**The standard atmosphere returns three records because it is settled.** It stopped generating papers
and became a standards document, and the document itself is now cited at the relation that integrates
it. **A harvest aimed at it would have returned meteorology**, which the sweep store already excludes.

**Wing internal volume returns twenty records and almost all are the wrong sense**, being fuel tank
fire, inerting, sealants and static electricity rather than how much volume a wing encloses. **That
relation lives in design textbooks and not in the report literature**, and it is cited to books.

**Quasi-tailless technique returns twenty-four records with fifteen report primaries, and it is small
because the field is small.** One aeroplane flew the experiment, inside a variable-stability tradition
that is itself narrow. **Fifteen report primaries out of twenty-four is a strong showing for a small
field and not a thin one.**

---

## Eleven Foundational Primaries Were Fetched by Identifier Rather Than Searched

**Each is a specific document a relation in this article rests on, and a search returning something
adjacent would have been worse than useless.** Munk on the aerodynamic forces on airship hulls, which
is where the slender-body moment the article displays comes from and is dated 1924. Multhopp on the
aerodynamics of the fuselage. Allen and Perkins on viscous flow over slender inclined bodies. Oswald,
whose name is on the efficiency factor in the drag polar. The U.S. Standard Atmosphere. Gilruth on
requirements for satisfactory flying qualities. Campbell and McKinney, Toll and Queijo, and Jones and
Alksne on lateral derivative estimation. And two in-flight evaluations of pure control system time
delays, which bound the loop budget with flight data rather than with a phase argument.

**Every one is cited in the prose beside the relation it establishes and not only in the reference
list.**

---

## The Gate Rejected Two of Those Eleven, Which Is the A333 Failure Exactly

**Allen and Perkins was refused because its title uses the vocabulary of the underlying fluid mechanics
rather than of aircraft, and the U.S. Standard Atmosphere was refused because `atmosphere` was not an
anchor.** Both were readmitted by name, both anchors were then added so records like them are not
silently lost, and **the readmission is recorded in the article** because a source admitted by exception
rather than by rule is one a later reader should be able to question.

**That takes this article's gate defects to six.** Three more noise families were added to the shared
sweep store as well, being the signal-processing time compressor against the turbomachinery compressor,
the ocean families the earlier ship pattern does not reach, and aeromedical research about the crew
rather than the aeroplane, which entered through the `fighter` anchor this article itself added.

---

## What the Equation Pass Did, Since It Is In This Commit Too

**25 display equations to 59, across 27 edits, and two of them changed what the article says.**

**The draft's sensing claim does not survive being written down.** The gearing from sideslip to nozzle
is 1.13 degrees per degree and a half-degree measurement error costs 2.9 percent of authority, so the
static requirement is mild and only the dynamic one binds. **The claim was withdrawn and chased into
the Dependent Systems section, that subsection's own closing paragraph, and the Epistemic State.**

**Relaxing the constant jet velocity assumption improved the conclusion.** It runs by 25.7 percent
across the envelope, moving the minimising Mach from 1.674 to 1.550 and cutting the demonstrated
point's penalty from 13.5 percent to 7.8.

**Three further results.** A propulsive tail volume puts vectoring in a rudder's own units, giving 44
percent of a thirty-degree rudder at the demonstration point and reproducing the 5.33 throttle factor
from the opposite direction. The loop budget gives 60 to 90 milliseconds supersonically and says an
actuator spends it before a processor does. And inverting the slender-body moment shows **the
instability bracket is conservative**, so every conclusion survives a more unstable aeroplane.

**A second displayed line was found not to evaluate to its own stated answer**, the lapse exponent
showing the logarithm of 1751 over 8450 and stating 0.960 where those numbers give 0.959. Both
instances in this article were caught by an instrument and neither by reading.

---

## A Rendering Defect the Rendered Audit Structurally Cannot See

**The build was clean, the rendered audit reported no findings, and the page was still wrong.** An
edit landed a display equation and the next paragraph's opening sentence on one source line, because
this article's prose is one paragraph per line and two consecutive edits both anchored there.
**Kramdown rendered the equation as inline math inside a paragraph and ran two unrelated sentences
together.**

**Nothing in the toolchain could have caught it.** The delimiters balance and the markup resolves, so
`render.py` sees a well-formed page, and no property of the HTML distinguishes an equation the author
wanted inline from one the author wanted displayed. **I found it by counting display equations in the
source and `\[` in the rendered HTML and getting 59 against 58.**

**The guard is in `lint.py` now rather than in a comment.** `math-display-inlined` is a DEFECT, and it
was measured across the whole corpus before being promoted, reporting **zero findings** there so it
gates without flagging anything that already ships. Code is excluded through a new
`post.strip_code_keeping_lines`, which blanks fenced, Liquid-highlight and indented code while keeping
line numbers intact so the report points at the right line. **Two regression tests cover it and the
suite is 81 of 81.** The incident is written up in `VERIFICATION_TRAPS.md`.

**I did not promote it to `_verify.py` and that is your decision rather than mine.** It qualifies on
the stated grounds, since the corpus is clean of it and the defect reaches a rendered page, but
`_verify.py` is the CI gate on the deploy path and adding to it is a change of a different kind from
adding a workbench check. **Say the word and it is about ten lines**, duplicated rather than imported
because that file must run standalone on a bare runner.

---

## State

**24,509 lines, 59 display equations, 11,799 reference definitions, 138,237 words**, of which 16,890
are author prose. **Two of the four passes were completed in this commit and the publication review
has not run.**

`_verify.py` clean on the draft apart from the `date-filename` artefact every draft reports, zero
warnings, `lint.py` zero defects, zero true contractions, colons, semicolons or dashes in authored
prose, reference integrity **zero undefined, zero orphaned, zero duplicate URLs across 11,799
definitions**. **Every count the article states about its own corpus was checked against the data it
ships with**, including all fifteen cluster rows and every cluster's inline record count.

**Forty-five of seventy-two drafted, none published, publication never authorised.**

---

## Next

**The publication review of A341 on your prompt**, which is also the pass that pushes.

**The gate re-harvest of the escaped clusters in the earlier articles remains an open unit of work.**
**The one-word caps defect on the live `_posts/2026-08-06-native_lowering_coverage.markdown` is still
yours to decide.**
