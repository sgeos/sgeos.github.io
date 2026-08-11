# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-10
**Task**: A329 primary-reference review, the third of four passes. Committed, **not pushed**,
**not published**.

**State: 13,353 lines, 28 display equations, 4,096 reference definitions, 71,302 words**, from 7,303
lines and 2,108 definitions. Equations were held and measured before and after, and all 4,037 master
records are cited. All thirty-three articles remain in `_drafts/`.

---

## This Article Has Two Primary Bases and They Sit in Different Decades

**A primary source is one contemporary with the work, and here the work is two things that happened
thirty years apart.**

**The decision is a 1996 to 2002 subject.** Source selection, competitive prototyping, cost
estimation and requirements commonality are primary in that window and nowhere else, and it holds
621 records.

**The physics is not.** The vertical-landing research the competition rested on was done in the
1970s and 1980s, largely by NASA, and **a 1985 report on hot gas ingestion is a primary source for
this article's central failure mechanism in a way that a 2019 review is not**. That base holds
**1,324 records across 1970 to 1995** and is the healthier of the two.

**Treating everything before 2003 as one undifferentiated band would hide that**, so the Source Base
separates them.

---

## What the Pass Measured and Moved

**The measurement came first.** The set held 2,985 records and only **265, or 8.9 percent, fell in
the programme window**. The clusters carrying claims were among the thinnest: hot gas ingestion at 7
in-window against the article's central mechanism, jet-induced ground effects at 6, hover control at
1, momentum theory at 1 against an identity the equation pass had just promoted, and the winning
aircraft's own cluster at 3.

**A harvest of roughly a hundred and forty narrow queries took the window from 265 to 621 records
and the whole set from 2,985 to 4,037.** Momentum theory went from 22 to 91, nozzle design from 64
to 130.

**The cause of the shortfall was the same mechanical one that caught the previous article.** The
reports server caps a search at ten results and rewards specificity, and the pool stood at 186
records for a subject NASA researched for thirty years.

---

## A Homonym Nobody Predicted, and the Dangerous Kind

**Hot gas ingestion is also a turbomachinery subject, and it uses the identical phrase.** Sealing
flows between a turbine rotor disc and its stator are an active field whose papers are titled
"hot-gas ingestion" exactly as the inlet problem is.

**The pool holds 82 titles containing "hot gas" and only 44 belong to this article.** The remainder
are rim cavities, purge flows and sealing effectiveness, joined by dust, particle and salt
ingestion.

**That is the most dangerous class, because it is internal to the discipline**, and it was found by
reading the discarded records rather than by anticipating it. **Bird ingestion remains deliberately
admitted**, because an inlet swallowing a bird and an inlet swallowing its own exhaust are the same
fluid mechanics.

---

## One Subject Reported as Thin Rather Than Padded

**Thirteen narrow queries aimed directly at hot gas ingestion moved the cluster from 43 records to
44.** That is not a failed harvest. The open literature on inlet reingestion is genuinely small,
because the measurements that matter are full-scale, expensive, and made by manufacturers rather
than by research agencies.

**The article's central failure mechanism rests on a thin public base and now says so.**

---

## Three Additions Changed What the Article Says

**THE FIRST IS AN IDENTITY THE ARTICLE HAD ALREADY ASSEMBLED WITHOUT STATING.** Momentum theory
gives the disc loading as twice the density times the induced velocity squared, and the far field
runs at twice the induced velocity, so **the dynamic pressure in the fully developed jet is the disc
loading, exactly**.

**That means the table of disc loadings the article was already printing is also a table of the
pressure each architecture imposes on whatever it is hovering over.** The lift fan puts 1,467 pounds
per square foot onto the surface and two nozzles two and a half feet across put 2,852, a factor of
1.94 that deck coatings and ground crew feel directly. It cost nothing extra to derive because it is
the same quantity the propulsion argument already needed.

**THE SECOND IS THE SQUARE-ROOT LAW SEEN FROM THE OTHER SIDE.** Two streams mix at the mass-weighted
mean of their temperatures, and because the cold stream is **slower** it carries **more mass per unit
of thrust**. A 47.7 percent share of the lift is a **60.9 percent share of the mass**, and the
mixed-mean exhaust falls from 1,200 degrees Fahrenheit with all-hot lift to **505**.

The article had asserted that the lift fan's exhaust is cooler and never written the relation that
makes the claim quantitative.

**THE THIRD PRICES A CLAIM THE ARTICLE HAD ONLY ASSERTED.** Bleeding a fraction of the mass flow for
reaction controls removes that fraction of the thrust **before any moment is produced**. A four
percent bleed costs 1,120 pounds of lift and takes the direct-lift allowance from 2,637 pounds to
1,570, which is **forty percent of everything the aircraft can bring home**, spent on a roll control
that has not yet been used. The lift-fan aircraft takes its roll control from posts that are already
producing lift, so the same function costs it nothing it was not already spending.

---

## One Defect in My Own Verifier

**Three checks compared the allowance line against the direct form, which is an agreement between
two computed routes rather than a value the article states.** Recording them with the harness's
value-tracking check made `require_in_text` demand that unrounded intermediates such as 2636.67
appear in the prose.

**That is exactly the two-kinds-of-check distinction the harness exists to keep**, and the
comparison is now made without being recorded.

---

## The First Aircraft in the Series Built to Win a Competition

**Every other X-plane so far existed to find something out. This one existed to beat another
aeroplane**, and on 26 October 2001 it did not.

**The keystone is therefore what a fly-off decides and on what evidence**, and it is a question of
**construct validity** rather than of sampling error. That distinguishes it from the previous
article. The X-31 flew hundreds of engagements and the difficulty was that a finite sample carries a
wide interval. Here the sample size is one, and the difficulty is that **the one trial was not a
trial of the proposed aircraft**.

---

## The Propulsion Half Has a Clean Answer in One Relation

Static thrust is mass flow times jet velocity and the power added is half the mass flow times the
velocity squared, so eliminating the velocity gives thrust as the square root of twice the power
times the mass flow. **At fixed power, doubling the mass flow multiplies thrust by root two.**

**That is the entire case for a lift fan over direct lift and it fits on one line.** A lift fan
spends shaft power on a large cold stream and a direct-lift system spends the same power on a
smaller hot one.

**Three published numbers that were never published together turn out to be mutually consistent.**
The lift fan's 50-inch diameter, its 20,000 pounds of cold thrust and its 29,000 shaft horsepower
imply a figure of merit of **0.697**, which is what a good ducted fan achieves. Establishing that
before building an argument on them seemed worth doing, and nobody appears to have checked it in
print.

**The nozzle the direct-lift system would have needed is inverted rather than assumed.** Matching
the fan's disc loading with 28,000 pounds of core thrust needs 19.09 square feet of nozzle, a single
opening **4.93 feet across**, on a 45-foot fighter. That is not an engineering trade.

---

## The Competition in One Number

At 24,030 pounds empty and a five percent control margin, direct lift permits a bring-back allowance
over empty weight of **2,637 pounds** and the lift system permits **15,875**, a ratio of **6.02**.

**Both aircraft can hover. One can come home with two and a half thousand pounds of fuel and weapons
and the other with nearly sixteen thousand.**

**And the small number is badly conditioned.** The allowance is a small difference between two large
numbers, so it amplifies a fractional thrust loss by **10.11** against 2.51 for the lift system, and
a fifty degree inlet temperature rise from hot gas ingestion takes **45.5 percent of it**. Below
25,232 pounds of lift the allowance is negative, meaning the aircraft could not land vertically at
its own empty weight.

**The amplification is reported as badly conditioned rather than as a precise number**, because it
blows up as the allowance approaches zero and that is the shape of the problem rather than an
artefact of the arithmetic.

---

## The Second Finding Came Out of Building the Reference Set

**In a pool of 4,412 harvested records, exactly one carries the X-32 in its title.** It was written
by the engine supplier, in 2002, after the decision. Against that, the F-35 appears in 29 titles
running continuously from 2002 to 2020.

**The winner acquired a literature and the loser did not.**

**The cluster was tested before the claim was made.** Two harvests asked for the aircraft by
designation, by manufacturer and programme together, and by the pre-competition programme names,
across the reports server, both Crossref content types and the defence registry. The answer did not
move.

**The consequence for the article is stated rather than hidden.** Its technical case rests on
published numbers for the winning system and an assumed upper bound for the losing one, because the
losing one's numbers were never published. **The evidentiary asymmetry available to a historian is a
direct inheritance of the asymmetry in the decision.**

---

## The Historical Finding

**Boeing flew a wing it had already abandoned.** The demonstrators carried a tailless delta and the
production proposal used a conventional wing with a canted twin tail, and the change was made before
the X-32 ever flew.

**A demonstrator that differs from the proposal in the feature under examination is evidence about a
different aeroplane.** The customer was shown an aircraft nobody intended to build, while the
competitor's demonstrator flew a short takeoff, a supersonic dash and a vertical landing in a single
sortie in the configuration it was offering.

**The article gives the opposite reading its own subsection**, because a company that finds a
configuration problem and fixes it before proposing has done what a risk-reduction phase is for, and
the record does not say which reading the source selection took.

---

## Two Defects Found

**An all-remaining marker can legitimately find nothing left**, when an earlier marker for the same
cluster and era already drained it. The assembler now distinguishes that from a fixed-count marker
finding nothing, which means the article is citing a subject it does not have.

**`require_in_text` failed on a value that was present in the draft.** The equation wrote
`20{,}199`, which is LaTeX comma spacing, and the flattened text therefore contained `20{}199`
rather than `20199`. **A value inside an equation is not reliably findable by a text check**, so the
figure is now stated in prose as well.

**One record was dropped** for a contraction inside a verbatim citation title, which is the second
such collision after A328 and is handled identically.

---

## Verification

**77 of 77 independent checks passing, none importing the calculation.** The square-root law is
tested as a randomised property over twenty thousand inputs, the figure of merit is reached by
numerically integrating the momentum flux through two hundred thousand annuli, the nozzle area by
bisection, the bring-back allowance by scanning weights upward until the margin fails, and the
amplification by finite difference.

**The disc-loading identity is checked by computing its two sides separately from their own
definitions** over twenty thousand random thrust and area pairs, the fan mass flow by dividing the
momentum flux rather than by thrust over twice the induced velocity, the mixed mean by simulating
the mixing of forty thousand parcels, and the claim that a slower stream carries a larger mass share
than thrust share as a property over random velocity pairs rather than at the one published
point.

`_verify.py` at the 21-warning baseline with zero errors, check_any clean, `_lib/test_lib.py` at 48
of 48, and reference integrity at 4,096 with zero undefined, zero orphaned and **zero link-text
defects across 8,133 reference entries**.

**The set swept with zero hard failures**, including all 161 NTRS identifiers, 600 of 3,103 sampled
journal DOIs, 160 of 774 sampled DTIC DOIs, and all 8 books and 18 curated URLs, with **zero
search-endpoint citations**.

**A 33-article isolated build renders the page at 977 kilobytes, 16 sections, 56 subsections, 16
tables, 8,440 list items and all 28 equations**, with zero broken anchors and zero empty
headings.

---

## Citation Gaps, and the Five That Should Stay

**Twelve displayed equations carried no nearby citation and five still do.** They are the three that
construct the bring-back allowance, the roll moment as differential thrust times a lateral arm, and
the ratio between the winner's and the loser's record counts.

**The first three and the last are original constructions and the roll moment is elementary
statics**, so citing any of them would be false attribution or worse. The article says so in its own
subsection. **Everything else now carries its literature**, including momentum theory, the figure of
merit, the disc loading as a dynamic pressure, the corrected engine parameters, the ingestion
correlations and the twin-jet fountain.

---

## Awaiting Instruction

**A329 has completed the draft, equation and primary-reference passes.** Thirty-three of seventy-two
drafted, **none published**.

The next pass is the publication review.
