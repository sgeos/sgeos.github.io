## Last Updated

**Date**: 2026-09-04
**Task**: **A349, X-Planes: X-52, the Designation Refused, equation-density review. The second of four.**
Committed, **not pushed**, since only the publication review pushes. **Not published**, and publication
of the series still not authorised. **Fifty-three of seventy-two drafted.**

---

## Thirteen Display Equations to Thirty-Three, and None of Them Is Physical

**This is the first article in the series whose relations are not about air.** The subject is an
administrative refusal, so what there is to display is set theory, information theory and string
metrics. That turned out to be a great deal more than the draft had shown.

**The designation space gained an honest partition.** The instruction knows two states, allocated and
available, and the master list of designations records a third, since the C-16 correspondence directs
that the number be marked **not used**. The article now writes the partition with all three, because
**the second state is where the X-52 went**, along with C-16, C-42, C-43, C-44, P-6, F-19 and every
thirteenth number in the system.

**The availability set only ever shrinks**, since a retired designation may not be reused, so a design
number is consumed rather than borrowed and a refusal spends one without allocating it.

**The unwritten thirteen rule is now measured.** Six mission series are missing their thirteenth number
by custom, and the instruction mentions the custom nowhere.

---

## The Two Decisions Are Now in the Same Unit, and It Is Bits

**A listener who hears the design number and not the mission letter carries a residual uncertainty of
$\log_2 o_k$ bits**, where $o_k$ counts the series holding that number. Zero bits when a number belongs
to one series, one bit when it belongs to two.

**The F-35 approval in 2002 raised that quantity at 35 from zero to one bit.** The X-35 had been
allocated and the F-35 was approved on top of it.

**The X-52A refusal in 2006 held the quantity at 52 at zero**, against the one bit the approval would
have added.

**One office spent the bit and then withheld the same bit, four years apart, and wrote down its reason
for neither.** That is the article's thesis reduced to a single unit, and it is the strongest thing
this pass produced.

---

## Computing a Relation Overturned the Prose That Named It

**The draft said that saying the designation aloud separates the two names further. It does the
opposite.**

Written, `X-52` against `B-52` scores 0.75 on normalised edit distance. Spoken, `ex fifty two` against
`bee fifty two` scores about **0.846**, and higher means closer. **Spelling the designation out pushes
the two names together**, because the shared numeral expands into two long words while the letter that
distinguishes them stays one short syllable at the front. At whole-word level the ordering reverses
again at about 0.667.

**So the answer depends on what a listener is taken to be matching**, which is exactly what the 2006
decision did not say. **This is the equation review doing the thing it exists for**, since the claim
looked obvious and was backwards, and only computing it found that out.

---

## The Judgement Now Has the Measures It Never Recorded

Three of them, all computed here and none quoted. **Normalised edit distance 0.75. Longest common
subsequence 0.75. Bigram Dice two thirds**, the last being the family drug regulators actually use,
because a listener who mishears is not performing an alignment.

**And then the object that turns any of them into a refusal**, being a threshold, written as the rule
that refuses a proposed designation when its greatest similarity to a designation already in use
reaches $\tau$.

**The 2006 decision supplies the proposal and the outcome. It supplies no measure, no threshold and no
comparison set. The 2020 instruction, which finally granted the authority, supplies none of them
either.**

---

## Two Defects the Pass Introduced and the Pass Caught

**A symbol collision.** The edit-distance section reused $m$ and $n$ for string lengths, and those two
letters name the basic mission symbol and the design number two sections above. They are now $\ell_a$
and $\ell_b$, and the article says so where a reader would otherwise wonder.

**An unsupported rate.** A sentence added during the pass claimed the X series consumed fifty-one
numbers in forty-four years. **Forty-four is the interval from the refusal to the B-52's planned
retirement and has nothing to do with it**, and the correct figure needs the X-1's designation date,
which this article has not established. **The rate was removed rather than repaired**, since an
equation pass is not the place to introduce a date the article does not otherwise carry.

---

## Verification State

- `python3 _verify.py` reports **0 errors, 0 warnings**.
- `python3 _lib/test_lib.py` reports **104 of 104**.
- `tmp/a349/verify_numbers.py` reports **ALL CHECKS PASS**. **Every string metric in the article is
  recomputed inside the checker from the strings themselves** rather than compared against
  `eqns.json`, so a wrong value in the generator cannot validate itself.
- Reference integrity: **2,046 defined, 2,046 used, 0 undefined, 0 orphaned, 0 duplicate URLs**.
- Prose: no contractions, no dashes, no prose colons, no prose semicolons. **No inline span carries a
  relation and none carries a pipe**, which is the kramdown table trap `_verify.py` caught in the draft
  pass.
- **4,734 lines, 29,449 words, 33 display equations, 2,046 reference definitions.**
- **The build succeeded in 21 seconds with no Liquid error**, against a checksum taken before it and
  re-verified after. **The rendered audit reports no findings across 88 pages.** Zero raw dollar pairs,
  zero unresolved reference brackets, page 445,001 bytes.
- **Source 33 display equations against 33 real rendered display blocks.** The page carries a
  thirty-fourth backslash-bracket and it was checked rather than assumed: it is the `[4pt]`
  line-spacing directive inside the edit-distance `cases` environment. **The first version of that
  check had its own escaping wrong and reported 34 real blocks**, which is a broken check reporting the
  data as broken, and it was rerun correctly.

---

## Next

**A349 has two passes remaining**, the primary-reference review and the publication review, in that
order and each on its own prompt.

**Expect the primary pass to be unusual.** Report primaries stand at 36 of 1,968, which is 1.8 percent
and the second-lowest in the series after A336's zero. **The measure counts report-server and defence
technical identifiers, and this article's primary documents are three issues of a joint instruction and
a designation registry, none of which carries one.** Raising the fraction by harvesting aeronautical
reports would make the number look better and the article worse.
