# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-07
**Task**: A310 primary-reference pass, the third of four. Committed and **not pushed**. **Not
published.** All fourteen articles in the series remain in `_drafts/`.

---

## The Pass Opened With a Harvest, Which Reversed the Usual Order

The draft pass warned that the pool held only 665 entries against A309's 3,597 and would not support
the 250 reference floor. It would not have. **The primary pass therefore began with a supplementary
harvest rather than with a citation-coverage audit**, and that reversal was the right call.

The harvest returned 684 new records and took the pool from 665 to **1,305 entries**. It was aimed
where the draft had found the material actually lives, which is the NASA low-speed research programme
rather than the defence archive, and at the sub-problems the equation pass had opened, namely
free-flight model technique, the hover position loop, ground effect and impingement, the pilot's
visual task, and the vertical-attitude revival of the 1970s.

**References went from 143 to 250, which is exactly the floor.** Primary sources are 167 of 233, or
**71.7 percent of dated**, up from 61.1.

---

## The Article Is Held Up Almost Entirely by Documents About Other Aircraft

This is the source-base finding and it is now stated in the article.

**Almost nothing here rests on a document about the X-13.** It rests on documents about the
configuration, the flight condition, the test technique, and the pilot's task, written before and
after the aircraft flew and mostly about other machines. **An article about a vehicle with almost no
record of its own can still be dense, provided the question it asked was one other people were also
asking.**

That is true of the X-13 and it was **not** true of the [X-10], whose keystone was peculiar to a
cancelled programme, and the difference is a property of the question rather than of the archive.

---

## What the Harvest Found That Mattered Most

**The pilot's problem was eventually measured.** [Lollar and Matous 1963] observes the pilot-vehicle
loop closure for hovering aircraft directly, which is the closest thing in the literature to the
third-order position-loop analysis this article performs, and it postdates the X-13's last flight by
six years. [Howard 1976] measures what happens to pilot performance when the visual cues are removed,
and the answers the field arrived at were all forms of **giving the information back rather than
improving the view**, through peripheral vision displays, head-up displays, and shipboard control and
display combinations. **The X-13 had none of them.**

**The ground effect problem generated a multi-year programme.** The downwash impingement studies, the
erosion work for jet-lift aircraft specifically, the suckdown literature, and the fluid mechanics of
a jet meeting a surface are all present. **The jet-versus-rotor comparison the article computes was
made directly and by measurement**, in a 1971 paper comparing the outflows from a helicopter, a
tilt-wing aircraft, and a jet-lift aircraft, which is the empirical form of the hundred-to-one disc
loading ratio.

**The free-flight technique has a literature of its own**, and the 1975 vertical-attitude fighter
studies were flown in the same facility and reported in the same form as the 1958 X-13 model tests.
**Two decades changed the proposed aircraft and did not change how the question was asked.**

**Vortex lift explains the wing.** The leading-edge suction analogy postdates the X-13, so the
maximum lift coefficient the article assumes is a vortex-lift number rather than an attached-flow
one, which is worth knowing given how much rests on it.

---

## One Seam Defect, Caught by Reading

An insertion left two clauses running together across a paragraph break, producing "...which is" at
the end of one paragraph and "which is the correct decision..." at the start of the next. **Every
automated check passed it.** It was caught by reading the connective lines, which is the defect class
with the longest unbroken run in this series and the reason that step is not optional.

---

## A False Alarm Worth Recording

`_verify.py` appeared to jump from 21 warnings to 40. It had not. The command inherited a working
directory inside the scratch build tree from an earlier step, so it scanned the build copy, which
contains fourteen extra draft files. **This is the A307 relative-path defect in a new place**, and it
is the second time this session that a check run from the wrong directory reported something untrue.
The rule already says to use absolute paths in edit scripts. It should say the same about checks.

---

## Verification

**250 reference definitions, 237 external URLs, zero duplicates.** `_verify.py` at the 0-error
21-warning corpus baseline when run from the repository root. All 268 worked values reproducing.
Zero contractions, em-dashes, en-dashes, prose colons, prose semicolons, prose parentheticals,
doubled words, duplicate headings, unbalanced emphasis markers, lone dollar-delimited lines, or
adjacent display-math seams. All fourteen insertion seams read by eye. Isolated build succeeding with
**91 rendered display blocks matching the source count exactly**, Part 14 navigation, twenty-one
tables, no unresolved reference links and no surviving Liquid tags.

Every anchor added this pass was checked against its title before the sentence using it was written,
in three batches of 86, 16, and 19, all with zero problems. The URL-stability guard added during A309
fired no drift on the rebuild.

---

## State

**1184 lines, 91 display equations, 250 reference definitions, 15,521 body words.**

**References are exactly at the 250 floor and equations are inside band at 91.** Lines are 116 below
the 1300 floor, reported rather than padded. Citation density rose from 12.82 to 16.58 per thousand
body words. Top bigram 4.1 percent. `aircraft` at 8.82 and `control` at 6.11 per thousand are the
subject and keystone nouns and are reported rather than remediated.

---

## What the Publication Review Has to Close

**Contemporary references are 47, or 20.2 percent of dated.** The absolute count is unchanged since
the draft and the percentage fell because the primary pass grew the denominator, which is the
familiar behaviour. Against the 101 to 189 absolute count the series has held since A301, **the gap
is between 54 and 142 references**, which is smaller than A309 carried but still the largest single
item. Closing it will also carry the article past the line floor.

**Committed, not pushed.** Fourteen articles drafted of seventy-two, none published. The
publication-order dependency is fourteen deep, A310 back to A297. **Categories remain undecided** at
`aerospace history engineering`, fourteen articles deep and raised eighteen times.
