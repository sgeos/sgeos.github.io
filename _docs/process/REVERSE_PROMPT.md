## Last Updated

**Date**: 2026-09-04
**Task**: **A349, X-Planes: X-52, the Designation Refused, primary-reference review. The third of four.**
Committed, **not pushed**, since only the publication review pushes. **Not published**, and publication
of the series still not authorised. **Fifty-three of seventy-two drafted.**

---

## The Article's Central Claim Was Resting on Its Own Survey

**The article said that a drug regulator makes the same judgement the Air Force made, against published
criteria, and cited nothing for it.** That is the claim the whole measurement section builds toward, and
it was an assertion drawn from the shape of the harvested literature rather than from a document.

**The Food and Drug Administration publishes every object the 2006 decision lacks.** The measure, being
a named program it also makes publicly available. The comparison set, being the drug reference
databases a proposed name is queried against. And the thresholds, published as three bands.

**Seventy percent or more is a highly similar name pair. Fifty-five to sixty-nine is moderately similar.
Fifty-four or less is low similarity.** The guidance further records that **the 55 percent screening
threshold is set on the validation work done on the algorithms**, so even the threshold has evidence
behind it.

**The guidance was read in full rather than described, and that mattered.** A web summary reported the
moderate band as beginning at 50 percent. **The document says 55.** This article has now met the
read-the-document lesson twice inside itself, once on the designation instruction and once here.

**The article's own figures fall in different bands and it says so.** The bigram coefficient of about
66.7 percent is moderately similar; the normalised edit similarity of 75 percent is highly similar.
**Both are stated as an illustration and explicitly not as a result of that program**, since neither is
the combined orthographic and phonetic score it computes.

---

## The Aviation Side Gained a Primary Study With a Count

**The United Kingdom's civil aviation authority ran a dedicated call sign confusion study and published
it**, and it rests on **482 reports of call sign similarity filed by pilots and controllers**. The
European briefing note that followed names the formats most likely to be confused and recommends
avoiding phonetically similar call signs on one frequency at one time.

**Neither appears anywhere in any of the three issues of the designation instruction.** That absence was
verified by searching all three for call sign, radiotelephony and the civil aviation body's name, and
all three returned nothing. **It is an absence claim and it was checked rather than asserted.**

---

## The Report Registries Were Aimed At Directly and Do Not Hold This Subject

**A supplementary sweep was run against the report registries specifically to raise the primary
fraction, and it returned almost nothing.** 1,196 records were retrieved that the main
harvest did not already hold, 1,148 survived the sweep store, and
**7 passed the subject gate**. The defence registry supplied 1,158 of
those records and **2 of the survivors**.

**The gate and the store were the main harvest's, unrelaxed.** A supplementary sweep that loosens either
raises the fraction by admitting records the first sweep had correctly refused, which is improving the
number rather than the article.

**So this is a measurement about the subject.** The armed services' report literature holds aeronautical
engineering. The confusability of spoken identifiers is studied in medicine, in civil aviation safety
and in linguistics, and the registries that index reports do not index it.

---

## The Count Is Now Reported Alongside the Fraction

**Report primaries 42 of 1,974, being 2.1 percent**, up from 36
of 1,968 at 1.8 percent, and **still the second-lowest in the series** behind A336's zero.

**And 9 curated sources are primary documents rather than descriptions of one**,
being three issues of the joint instruction, three of the drug regulator's naming publications, the
civil aviation call sign study, the air-ground communications briefing note and the flight research
centre's own fact sheet. **None of the nine carries an identifier the corpus-wide measure can see**, and
the measure was not changed to make them visible.

---

## Verification State

- `python3 _verify.py` reports **0 errors, 0 warnings**.
- `python3 _lib/test_lib.py` reports **104 of 104**.
- `tmp/a349/verify_numbers.py` reports **ALL CHECKS PASS**, now including the published bands, the study's
  report count, the supplementary sweep figures and the primary-document count.
- Reference integrity: **2,057 defined, 2,057 used, 0 undefined, 0 orphaned,
  0 duplicate URLs**.
- Prose: no contractions, no dashes, no prose colons, no prose semicolons, no inline span carrying a
  relation or a pipe.
- **4,820 lines, 30,499 words, 34 display equations, 2,057 reference definitions.**
- Survey **1,974 research records across 10 clusters**.
- **The build succeeded in 21 seconds**, against a checksum taken before it and re-verified after.
  **The rendered audit reports no findings across 88 pages.** Zero raw dollar pairs, zero unresolved
  reference brackets, page 454,533 bytes.
- **Source 34 display equations against 34 real rendered display blocks.** The page carries 37
  backslash-brackets and the three extra were identified as `[4pt]` and two `[2pt]` line-spacing
  directives rather than assumed away.

---

## One Process Note Worth Carrying

**The rendered audit raced the build twice and reported the previous run's numbers.** `after_build.sh`
waits on `pgrep -f "jekyll build"`, and when it is launched immediately after the build it can miss the
process before it appears and then audit the previous `_site`. **The log looked plausible and was
stale**, which is the same shape as a presence check passing on a coincidence. Read the equation count
in the audit against the article before trusting it.

---

## Next

**A349 has one pass remaining, the publication review.**

**Expect it to read the opening against the conclusion first**, which has now found a defect in five
consecutive articles. The specific risk here is that the article gained a whole new subsection during
this pass, on what the other naming authority publishes, and the conclusion was written before it
existed.
