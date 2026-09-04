## Last Updated

**Date**: 2026-09-04
**Task**: **The book-identifier repair for A342 through A346.** Twelve anchors and sixteen citations
replaced. Committed and **pushed**. **Not an article pass**, and no article's argument, prose, counts
or reference totals changed. **Fifty-two of seventy-two drafted, none published**, and publication of
the series still not authorised.

---

## The Instrument Was Broken and Would Have Rewritten Correct Citations

**The first measurement of this repair was garbage and was discarded.** `_lib/booklinks.py` resolved a
work key by reading `openlibrary.org/works/<key>.json`. That endpoint returns **HTTP 500 for records
that plainly exist**. `OL17855977W` is Raymer's `Aircraft design, a conceptual approach` and
`OL5220705W` is Wooldridge's `Winged Wonders`, and both returned `Internal Error` six times out of six
while other keys returned 200 every time.

**A nonexistent key returns 500 as well.** That endpoint therefore cannot separate `this key is wrong`
from `this record will not serve`, and the module collapsed both into `None`, which `check` reported as
a mismatch. **Had the repair run against that measurement it would have replaced correct identifiers
with different ones.**

**That is the third time this corpus has paid for the same lesson.** A347's local SSL certificate error
nearly condemned 1,051 citations. A348 saw one book identifier fail on one run and resolve on the two
after it. **A broken check reports the data as broken, and that is the dangerous direction.**

---

## The Search Index Is the Oracle, and It Answers a Question the Work Record Does Not

`search.json?q=key:"/works/OLnnnW"` returns **numFound 1 with a title and an author** for a real key
and **numFound 0** for a bogus one, which is exactly the discrimination this needed. It also accepts
twenty keys in one query, which mattered because openlibrary.org was resetting roughly one connection
in three while this ran.

**It carries the author, which the work record does not give without a second request.** Every
replacement was therefore held to **both halves** of an `Author, Title` claim rather than to the title
alone, which is a higher standard than the gate it has to pass. A repair checked on title only is free
to land on a different author's book of the same name.

`resolve` now reports `found`, `absent` or `unknown`, and `check` reports `ok`, `wrong`, `missing` or
`undetermined`, **so that `could not be determined` can never be read as `wrong`**. `_lib/tests` are
102 of 102, up from 101.

---

## What Was Actually Wrong

**Sixteen citations across twelve anchors, in all five drafts.** Seven of A346's eight checkable book
citations, five of A345's nine, two of A343's seven, one of A344's six and one of A342's eleven.

They pointed at a market outlook for dark rum in Japan, a guide to buying apartment buildings, a book
about log homes, a Spanish travel guide to the Greek islands, a text on green chemistry, a volume of
`History of Universities`, a book on liturgy, an immigration handbook, a work on semiotic
phenomenology, a study of rural modernisation in Java, a survey of adult-education thinkers, and **a
strategy guide for the video game `Vigilante 8`**.

**Eight replacements were already living in the corpus**, seven of them in A347, which is the article
that found this class of defect and repaired its own. Four were resolved by fresh search, namely
Sheridan at `OL4274944W`, Hoerner at `OL5289631W`, Misra and Enge at `OL24594478W` and Stepniewski at
`OL5602816W`.

**The repair script confirmed the old key wrong before touching it**, so that a key which was correct
all along could not be replaced, and **refused rather than guessed** on any disagreement. It refused
nothing. Corpus measurement moved from **283 of 300 to 299 of 300**.

---

## Two Things Left for You

**A324 carries a malformed label over a correct key.** `book_jenkins` reads `Administration, National
Aeronautics and Space, Jenkins, Dennis R...`, which is the repository's author field copied verbatim
with its ellipsis, so the label swallowed the title. The identifier is right and the rendered citation
is not. **It is outside A342 through A346 and belongs to an article that has completed all four
passes**, so it was reported rather than edited. It is the one remaining item in the 299 of 300.

**A substantial fraction of OpenLibrary work pages currently return Internal Error to a reader.** Four
of the 22 book URLs in the five repaired drafts failed on two consecutive serial requests, and the
condition also hits keys A347 shipped and you already approved, namely Schlichting at `OL11833044W` and
Bramwell at `OL16987916W`. **No key was changed to chase this.** Selecting an identifier against a
transient server fault is the error this entire task was spent avoiding. **If it persists it is a
reader-facing problem for the whole series and not for these five drafts**, and it wants its own
decision.

---

## Verification State

- `python3 _verify.py` reports **0 errors, 0 warnings** across 301 posts.
- `python3 _lib/test_lib.py` reports **102 of 102**, with a new test naming the 2026-09-04 failure.
- Corpus book measurement: **300 checkable citations, 299 correct, 0 absent, 0 undetermined**.
- The diff is **16 changed lines in five drafts**, every one a reference definition. **No prose, no
  equation, no count and no reference total moved.**
- **No production build was run.** The change is confined to reference-definition URLs in drafts,
  which the production build excludes, and it cannot reach Liquid, kramdown or MathJax. `_verify.py`
  covers reference integrity and reports clean.

---

## Next

**A349**, `X-Planes: X-52, the Designation Refused`, editorial date 2025-11-27, series index 53.
**Twenty articles remain.** No article is mid-rhythm.

**Carry forward.** Use `booklinks.resolve` and never the work JSON endpoint. Hold a book key to title
and author both. The three tagged sweep-store families are switched off only for the articles whose
subject they are. `survey.loose` splits on hyphens. Finish the entire prose read, generated fragments
included, before starting a build.
