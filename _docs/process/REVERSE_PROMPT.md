## Last Updated

**Date**: 2026-08-14
**Task**: **Series-wide audit and back-sweep of the forty-four X-Planes drafts.** Not an article pass.
No article was written and nothing was published. **A341 was not started.**

---

## The Series Is Structurally Sound and I Checked Rather Than Assumed

**Every sequence property holds exactly.** Series index runs 1 to 44 with no gaps or duplicates,
article numbers A297 to A340 likewise, editorial dates 2025-10-06 to 2025-11-18 unbroken, and the
three agree on an exact arithmetic mapping, index `i` to `A(296+i)` to `2025-10-05` plus `i` days.
Front matter is identical across all forty-four on series, series title, categories and mathjax.

**No draft cites a sibling forward or itself**, every `post_url` target resolves to a post or a draft,
and there are **zero dangling targets**. The roster still ends flush against the published 2025-12-17
Solana article with no date collision. **43 of 44 still cite a sibling absent from `_posts/`**, so the
publish-together constraint is intact.

**`_verify.py` reports 0 errors and 0 warnings across 301 posts.** Zero em or en dashes. **Zero true
contractions**, where an initial crude count of 1,962 was possessives, which are legitimate.

---

## Two Findings, and the Larger One Was My Own Error

**Nine caps-emphasis spans were real and are fixed**, in A316, A327, A332 and A340. Two carried genuine
emphasis and became bold, the rest were capitalisation that had leaked out of a harvested source title
into author prose. `ARE`, `START` and `AN/ARW` were correctly left alone as genuine acronyms.

**The gate-escape finding was largely my instrument, not the corpus.** A probe of medical and
agricultural terms returned 78 hits across twelve articles, thirty of them in A336, which looked like
the worst escape in the series. **A336's survey is deliberate and the article says so**, declaring that
its subject is not an aircraft but what a gap in an official register means, across eight named clusters
spanning archival silence, classification infrastructure and identifier administration. My probe had
assumed every article in an aerospace series is about aerospace. **A335's long-COVID orthostatic
intolerance cluster is likewise correct**, since the X-38 returns deconditioned crew to one gravity.

**Genuine escapes do exist and are rare.** `Effectiveness of Birth Control` in A323, `Divergence
Paralysis with Increased Intracranial Pressure` in A326, `Agricultural Data Source Selection for Crop
Yield` in A329, an Indonesian COVID booster-acceptance study in A330, and `Insurance. Liability
Insurance.` under A328's general control literature. **The A330 case is the exact `booster` defect A339
diagnosed and fixed**, which went forward into A339 and A340 and was never swept backward.

---

## I Did Not Strip Them, and the Reason Is the Count-in-Own-Prose Hazard

**Every survey states its own counts in prose**, in several phrasings, including 26 per-cluster
"the harvest returned N records here" statements across four articles and pool totals elsewhere.
**Removing citations desynchronises every one of them**, which is the defect class that has already
shipped nine times in this series.

**Against that cost, the benefit is small.** The escapes are a fraction of a percent of 245,285
citations, and every survey states explicitly that the records are an unread map of the surrounding
literature rather than evidence for any claim. **The correct repair is at the gate and not in the
artefact**, meaning corrected vocabulary and a re-harvest, which is a rebuild rather than an edit.
**I recommend that as its own unit of work and did not undertake it unasked.**

---

## What I Did Change

**3,564 citation titles normalised out of all capitals**, across 26 articles, from the DTIC and NTRS
records that store titles that way. **The acronym set was derived from the data rather than listed**,
by taking tokens that appear capitalised inside normally-cased titles and keeping those whose capital
form dominates their normal use. That keeps NASA, VTOL, STOL, RCS, CFD, USAF and LOX and rejects JET,
AIR, LOW, AN and THE.

**Three defects were caught in my own instrument before it shipped.** A short-token fallback preserved
`LOW`, `AIR` and `JET` as though they were acronyms. An absolute lowercase threshold demoted `VTOL` to
`Vtol` and needed to be a ratio. A missing DOTALL flag let citation text that wraps before its year
evade the prefix strip, which is the same wrapped-form blind spot as the hyphen defects in A339 and A340.

**The result is provably presentation-only.** 3,534 lines changed, additions equal deletions, line
counts unchanged in every file, **exactly 2 lines differ by more than letter case** and those two are
the caps fixes that gained bold markers. **Anchor sets are byte-identical to HEAD in all 44 files** and
no reference dangles.

---

## A Check I Built, Measured and Rejected

**The caps-emphasis lesson was nearly turned into a `_verify.py` check and should not be.** The broad
version gave 80 hits across 20 files at roughly 15 percent precision, including `AT&T`, `ION-DTN`,
`AGENTS.md` and the `AND` and `OR` of logic gates. The narrow version, capitals inside a bold span,
gave 1 hit corpus-wide and it was real, **but it catches only one of the nine defects that motivated
it**. A check that green-lights the corpus at 11 percent recall stops the manual search that was
working. **Both numbers or neither**, and this is recorded in `VERIFICATION_TRAPS.md`.

**A hypothesis about the low recall was also wrong.** I attributed it to `prose_text` stripping only
single-line link pairs while citation text wraps, and measured **0.0 percent inflation on every article
including the 26,249-line A340**. The helper is correct.

---

## One Item Outside This Sweep, for Your Decision

**A published post carries the same defect.** `_posts/2026-08-06-native_lowering_coverage.markdown`
line 1306 reads `to ADD TO A COMPLETE MACHINE for speed`. It is a one-word prose fix with no URL
consequence, but the post is live and outward facing, so **I did not touch it**.

---

## Shells, Since You Asked

**This session had zero live background shells.** The 63 in the status line are dead registry entries,
generated by backgrounding a three-hour deploy gate once per pass.

**The seven live ones belong to the keleusma session**, not this one, and six are unproductive `until`
loops polling `gh run view`. Five poll runs that already completed, and one has run **10 hours 29
minutes on an empty run identifier**, so `gh run view ""` fails forever and the loop cannot exit.
**I did not kill another session's work.** That last one is the trap already recorded in
`VERIFICATION_TRAPS.md` as a wait loop that can never exit, in a new form: **an unbounded poll with no
guard on an empty input.**

---

## State

**Forty-four of seventy-two drafted, none published, publication never authorised.** Nothing was
published, nothing was trimmed, and no article gained or lost a reference.

**The build-time decision is still open and now more pressing**, since the gate is the long pole in
every pass and twenty-eight articles remain.

---

## Next

**A341, "X-Planes: X-44, One Designation and Two Aircraft"**, editorial date 2025-11-19, series index
45, on your prompt. **Not started.** The re-harvest of the escaped clusters is available as a separate
unit of work whenever you want it.
