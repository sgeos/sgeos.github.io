## Last Updated

**Date**: 2026-09-03
**Task**: **A347, X-Planes: Boeing X-50 Dragonfly, publication review. The fourth and last of four.**
Committed and **pushed**. **Not published**, and publication of the series still not authorised.
**Fifty-one of seventy-two drafted.**

---

## Reading the Opening Against the Conclusion Found Two Defects, Which Is Why It Is Done First

**The conclusion compared this aeroplane's disc loading to a Black Hawk's and nothing in the article
computed it.** The comparison appeared in the closing section and nowhere else. The value is 1.33, it
is correct, and it was asserted. **A number that appears only in a conclusion is a number no checker
has ever seen**, and this is the third consecutive article in which reading those two sections against
each other found something.

**The opening said the flight record spanned three years. It spans twenty-eight months.** Both are now
computed in `analysis.py` and verified.

---

## The Results Probe Fired for the Eighth Article Running

**Ten conclusions were probed in the article's words and the field's.** Seven were comfortable.

| Conclusion | Article's words | Field's words |
|---|---|---|
| tail surface sizing as the link | 2 | 380 |
| effort goes where the risk is believed to be | 4 | 65 |
| reaction drive costs a factor in fuel | 0 | 77 |
| the designation and how aircraft are numbered | 0 | 1 |

**Three of the four thin ones opened on rephrasing alone**, tail sizing going from 2 records to 380.
That is the fourth consecutive article in which most thin measurements turn out to be questions about
phrasing rather than answers about the pool.

**The fourth was deliberately not harvested.** How aircraft are numbered stands at one record. A341
already ran that experiment for this series and returned Massachusetts tax valuations of 1771 and
salmonella serotype naming. **The series has paid for that measurement once.**

**A depth harvest was run for the two that opened but stayed modest**, adding 761 records.

---

## The Epistemic State Was Stale and the Framing Section Was Incomplete

**Both were written at the draft pass and neither had been updated for the two passes since.** The
Epistemic State listed only the draft-pass derivations, so roughly thirty computed quantities added by
the equation pass appeared nowhere in the article's own account of what it had verified. The framing
section named three unpublished quantities where there are four.

**Both rewritten.** A fifth framing limit was added bounding the new ancestry claim to the sources
actually consulted, since **the claim that the Hughes rotor/wing appears in no secondary account is a
claim about a search and not about the world.**

**Out of Scope now names rotor icing and the human factors of rotorcraft displays**, because both were
in the harvest and both were removed from it, and a scope statement that omits what was deliberately
excluded is less useful than one that names it.

---

## A Store Pattern I Wrote This Session Had the A345 Bug

**`\bcompressor\b` cannot match `COMPRESSORS`.** Axial-flow compressor design charts reached the kept
set through a pattern added three hours earlier to exclude exactly that. `field-replaceable` likewise
missed `field-repairable`.

**This is the A345 near-miss class**, where `\bX-?48\b` could not match `X-48B`, and it recurred in a
pattern written to implement a lesson from the same article. Both fixed.

**The sweep store is now 119 patterns**, four more families having been observed in the publication
harvest. **The missile pattern carries an explicit warning not to reuse it**, because the X-7, X-8,
X-9, X-10 and X-17 are all missiles and for those articles it would delete the subject. The
hypersonics pattern from the previous pass carries the same warning for the X-15, X-30 and X-43.

---

## The Cluster Commentary Went Stale Within a Single Pass

**Three of its statistics were wrong immediately after the publication harvest moved the counts.**

**That is the A342 defect class arriving for the second time inside one article.** The first time, the
survey paragraph and the per-cluster table were converted to emitted text. The commentary sentences
about that table were left hand-written, and they went stale one pass later.

**The fix is the same fix.** A number about the reference set is emitted from the reference set,
**including the ones that sit inside a sentence**. The verifier's own expected values are now computed
on both sides rather than typed on one.

---

## The Build Was Started, Killed and Restarted on Purpose

**The article was edited after the first build began.** That is exactly A345's recorded defect, where
a build was started three times because the article kept changing underneath it.

**The build was killed and discarded rather than shipped against bytes that no longer existed.** All
remaining edits were finished first, the article was checksummed, the stub was rebuilt from the frozen
file, and the checksum was matched against the stub copy before the second build started.

---

## Reading the Whole Article End to End Found a Defect No Checker Could Have

**The download percentages are computed against the lift-coefficient 1.0 area of 25.5 square feet.
The prose called that the mid-range area of 21.3 square feet**, which is the smallest area in the
range and belongs to the lift-coefficient 1.2 case.

**Every number in that sentence verified individually.** 21.3 is a real computed area, 22.6 is the
real download percentage, and the verifier checks values rather than the claims that connect them.
**A checker that recomputes every quantity still cannot see a sentence that joins two correct
quantities wrongly**, which is an argument for reading the article and not only for checking it.

**One overclaim of mine was tempered in the same read.** The XV-9A being noisy and thirsty had been
written as the flight test agreeing with the Froude arithmetic. It does not measure it, and no source
consulted gives that aircraft's specific fuel consumption against a shaft-driven comparison. The claim
is now that the penalty was large enough to end the programme.

---

## Verification State

- `python3 _verify.py` reports **0 errors, 0 warnings**.
- `python3 _lib/test_lib.py` reports **98 of 98**.
- `tmp/a347/verify_numbers.py` reports **ALL CHECKS PASS**, **105 recomputed claims**, all present in
  the prose, 19 cluster rows matching their own citations, cluster table matching sections.
- Reference integrity: **7,952 defined, 7,952 used, 0 undefined, 0 orphaned, 0 duplicate URLs**.
- Book links **13 checked, 0 mismatched**. All 16 hand-added reference URLs return 200. All 50
  `post_url` targets resolve against the stub.
- Prose: **no contractions, no dashes, no prose colons**, one semicolon and it is the mandatory
  `console.log` tag. **Zero authored caps-emphasis runs.** NASA is spelled out at first authored use,
  which the handoff flags as missed in two consecutive articles.
- **16,706 lines, 93,835 words, 17,442 author prose words, 40 display equations, none inlined.**
- Survey **7,872 research records, 1,873 report primaries at 23.8 percent**.
- **The stub-isolated production build succeeded in 918 seconds with no Liquid error**, against bytes
  checksummed before the build and re-verified after it. **The rendered audit reports no findings
  across 86 pages.** Source and rendered display equations agree at **40**, **zero raw dollar pairs
  leak**, **zero unresolved reference brackets**, page renders to 1,384,343 bytes.
- **The build was started three times and the first two were killed and discarded**, because the
  article was edited after each began. That is A345's recorded defect and it recurred twice in one
  pass. **The rule that follows is to finish the entire prose read before building at all**, since a
  publication review reliably finds prose defects and a build started before it is wasted.

---

## Next

**A348**, editorial date 2025-11-26, series index 52. **Twenty-one articles remain.**

**Carry forward from A347**: the rotor family transfers to any rotorcraft subject and the
stopped-rotor and reaction-drive families do not. `gate.ATMOSPHERE` is named rather than copied.

**Two sweep-store patterns carry explicit warnings against blind reuse.** The hypersonics pattern
would delete the subject of the X-15, X-30 and X-43 articles. The missile pattern would delete the
subject of the X-7, X-8, X-9, X-10 and X-17. Both are recorded as subject-specific.

**The book-identifier repair for A342 through A346 is still outstanding and still needs your
decision.** Twelve anchors across five drafts, none of them in a published post.
