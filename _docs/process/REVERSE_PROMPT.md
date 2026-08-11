# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-11
**Task**: A370 publication review. **Committed and pushed.** **Not published.**

**References 57 to 2,002 definitions**, of which **1,980 are research citations**, being the 35 hand-selected
ones and 1,945 harvested. The article moved from 10,250 to 11,477 prose words, with equations unchanged at
31. The rendered page carries 4,206 links and 4,123 list items.

---

## The First Harvest Was Twice The Size And Was Worthless

**This is the finding of the pass and it was nearly shipped.**

The contemporary-survey gap was real. A369, this article's published predecessor, carries 1,765 reference
definitions of which 93.5 percent are from 2015 onward, against A370's 57. So the pass built a harvest.

**The first gate was inherited from A333 and rejected 2,174 compiler-science titles for containing no
aircraft.** That is the same defect A333's own primary pass found, recurring because the file was copied
rather than rewritten. It was caught and the gate was rewritten for this subject.

**The rewrite overcorrected into uselessness and the symptom looked like success.** The new gate admitted
generic stems, being analysis, implementation, generation, evaluation, system, model, performance and
interface. Every discipline that publishes uses those words. The corpus grew to 4,305 records and I was
about to treat the larger number as reassurance.

**A random sample of the kept records is what caught it.** The survey contained rabies control, seismic
depth imaging, breeding soundness examination in veterinary medicine, supercontinuum generation in
photonics, transport appraisal, fibre art and early-childhood language acquisition. The contamination was
not confined to the general cluster. It was in `static_analysis` by way of philosophical soundness, in
`calling_conventions` by way of logistics interoperability, and in `concurrency_runtime` by way of optical
fibre.

The gate now requires a term that is **computing-specific on its own**, so an ambiguous term contributes
nothing however many of them a title carries. It admits 2,021 of 7,334. **The corpus is less than half the
size of the contaminated one and that reduction is the result rather than a cost of it.**

**The lesson I would ask you to hold me to.** A larger harvest is not a better one, and the only instrument
that detects this failure is reading a random sample of what was kept. No count, no cluster distribution and
no drop-reason table shows it, because a permissive gate produces healthy-looking numbers in every one of
them.

---

## The Article Now States Which Half Of Its Bibliography It Read

A list of two thousand citations implies a reading it does not represent, so the article says so in three
places rather than leaving it to be assumed.

- **Method** reports the queries, the filter, the count it discarded and the two failed gates above.
- **The References introduction** separates the 35 hand-selected works, which the argument depends on and
  which were read, from the 1,945 harvested ones, which were not.
- **The Epistemic State** states that the harvested layer supports a claim about **coverage** and not about
  content, and that **the harvest makes the article's negative claim more exposed rather than less**, since
  a paper answering the question could sit unread in the list.

**The reconciliation with the article's own caution about citation error is that the two layers have
different failure modes.** A369's 5.5 percent error rate came from identifiers supplied from memory, which
is a generative process. A harvested identifier is transcribed from the registry that issued it and was
never a guess, so **harvesting removes that failure mode rather than reducing it**. What it does not remove
is a correct record cited for a claim it does not support, and no harvested record is cited for any claim.

---

## A Reader Clicking These References Will Meet One Failure In Eleven

A random sample of 250 harvested identifiers was resolved. **All 250 exist.**

**Twenty-two of them, being 8.8 percent, resolved only through the registry and not through the identifier
resolver.** Twenty refused the connection, of which 14 were Defense Technical Information Center deposits,
and 2 returned not-found from a publisher that no longer serves the landing page. In every case the
identifier is registered and the record is correct, so the defect is in the resolution path.

**This is in the article** because a reader spot-checking by clicking will hit it and would otherwise read
it as a bad citation.

---

## Three Smaller Corrections

- **The kept-count was read from the wrong level of a JSON file** and the article briefly stated "discarded
  7,332 of the 7,334 retrieved records". The file is `{"kept": {...}, "dropped": {...}}`, so its length is
  2. **A figure wrong by three orders of magnitude still looks like a number**, and only checking it against
  the console output caught it.
- **Registry titles carried newlines, HTML tags and `&NA;` where an author belongs.** A newline in a title
  breaks the list item it is emitted into, so whitespace is collapsed and markup stripped before use.
- **Two colon-led bold labels** in The Decision This Informs were converted to the corpus pattern of a bold
  sentence ending in a period.

---

## Verification

- `python3 _verify.py` **0 errors, 21 warnings**, the unchanged baseline, from the repository root.
- **Isolated production build with drafts, exit 0.** The rendered page carries **0 unfilled markers, 0
  unresolved references, 31 open and 31 close display-math delimiters, 0 empty list items and 0 nested empty
  lists**, the last being the doubled-marker defect that shipped in A332 and A333.
- **2,002 definitions with 0 undefined and 0 orphaned**, sorted by anchor.
- **The `--drafts` build fails on `_drafts/draft_summary.md`**, which carries a literal `post_url` example.
  That is pre-existing and is the documented reason drafts are off by default. It was moved aside inside the
  scratch copy only.
- `lint.scan` **clean**.
- **Prose scan clean** of em dashes, en dashes, contractions, prose colons, prose semicolons, prose
  parentheses and italics. The 45 apparent contractions are all possessives.
- `diction` against 297 published peers, **0 constructions above the corpus maximum**.
- `python3 tmp/a370/verify.py` **34 of 34**, unchanged, since this pass added no arithmetic.

---

## Next

**All four passes have now been applied to A370.** It is committed and pushed and **is not published**, and
publication has not been authorised for it or for anything else.

The X-Planes series is unchanged at **thirty-seven of seventy-two**, none published, with **A334, the Boeing
X-37, next** whenever you want it.
