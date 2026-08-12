# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-12
**Task**: A334, the Boeing X-37. **Primary-reference review complete.**
**Committed. NOT pushed**, per the rhythm in which only the publication review pushes.

---

## The Promotion Rule Fired Again, and Two Subjects Stood at Zero

An audit of the pool against the article's own subject list found **twenty-four of thirty-seven thin or
absent**. Two stood at **zero while the article displayed them**.

**Specific orbital energy is the foundation of every orbital result in this article and the pool held
none.** **Energy height is displayed in the landing section and the pool held none.** The first harvest
asked for spaceplanes, power systems, thermal protection and aerobraking. It never asked for the second
zonal harmonic, the solar aspect angle, the square-cube law or the energy state approximation, and the
equation pass had since made every one of those a displayed relation.

Three further harvests took the pool from **8,905 to 13,351** records and the cited base from **4,223
to 5,552**. The period half rose from 2,015 to **3,064** and the technical reports from 705 to
**1,116**.

---

## The Audit's Own Headings Were Thin in Exactly the Same Way

**This is the new lesson and it is one level up from the usual one.** I wrote the audit's subject
patterns in the ARTICLE's vocabulary and then harvested in the LITERATURE's, so a subject could be well
supplied and still measure zero.

**Three of the largest apparent gaps closed on the measuring instrument and not on the pool.**
Equilibrium glide went from 3 to 18, crossrange from 4 to 11 and vehicle scaling from 9 to 24, **with
no new records involved in any of them.** The records were already there. The audit could not see them
because it asked for `crossrange` while the field says `lateral range`.

**The thin-heading rule has always applied to harvest queries. It applies to the instrument that
measures the harvest too**, and nothing but reading the discarded matches would have shown it.

---

## Nineteen Subjects Remain Thin and the Article Names Each With Its Kind

A new Source Base table gives all nineteen. The four kinds are distinct and only one is curable.

**Settled knowledge, which must not be padded.** Vis-viva stands at **zero**, the rocket equation at
**one**, Kepler at **three** and the energy state approximation at **three**, after harvests aimed
directly at each. **These are not gaps.** They are relations in every textbook and in no journal
article, because nobody has published on them since the seventeenth and nineteenth centuries. **The
reference works carry them and that is the correct home.** A331 found exactly this for the rocket
equation and the finding reproduces.

**Thin headings whose subject is covered elsewhere.** Aerobraking corridor control at one record, while
aerobraking itself holds 191 under periapsis management and density reconstruction.

**Genuinely modern subjects.** Manoeuvre detection and debris disposal both have near-empty period
halves because the capability and the obligation are both recent.

**And the last row is the article rather than a footnote to it.** The X-37's own contemporary half
stands at **two records**. Every other thin subject here has an ordinary explanation. **The vehicle's
own is the only one whose cause is that somebody decided the work should not be published.**

---

## A Typographic Hyphen Hid a Directly Relevant Record

A record titled "Thermal Characteristics of a Nickel-Hydrogen Battery" was **refused by the gate**,
because the depositor wrote the hyphen as U+2010 rather than as ASCII. **Nickel-hydrogen is one of this
article's strongest anchors.**

`refs.clean` has normalised typographic punctuation for LINK TEXT since A332. **The gate needed the
same treatment for MATCHING and did not have it**, and nothing reported the failure because **a missed
match returns a smaller corpus rather than a wrong one**, which reads as a thin literature instead of
as a bug. That is the same shape as the plural-boundary defect that has now bitten five times.

---

## Reading the Kept Sample Found Four New Contaminant Families

All four are recorded in `_research/homonyms.py` with the incident that produced each, because a pattern
without its incident cannot be judged by the next article.

- **Terrestrial off-grid solar.** "Optimum battery depth of discharge for off-grid solar PV/battery
  system" uses this article's exact relation for a different machine.
- **Battery electrode materials chemistry**, which owns the phrases cycle life and capacity fade and is
  orders of magnitude larger than the spacecraft power literature.
- **Contact-graph satellite routing**, which is the 5G networking family arriving through a different
  door.
- **The instrument landing system glide slope**, a radio navigation aid sharing the phrase with an
  unpowered spacecraft approach.

---

## A Date Is Not a Measure of Primacy and the Article Now Reports Both

A cutoff separates period from contemporary and says nothing whatever about whether a record is an
original report or a commentary on one. **The technical report servers hold originals almost
exclusively**, so their share is the closest available proxy, and the Source Base now carries it beside
the date split rather than instead of it.

| Measure | Count | Share |
|---|---|---|
| Period, through 2011 | 3,064 | 55.7 percent of dated |
| Contemporary, 2012 onward | 2,432 | 44.3 percent of dated |
| Technical reports, all eras | 1,116 | 20.1 percent of all |
| Technical reports at or before 2011 | 915 | 16.5 percent of all |

---

## The Corpus Citation Run Reached A334 and Found Three Defects

Coverage went from 34.5 percent to **99.9 percent**, 3,629 of 3,631 identifiers. The findings were **1
mismatch and 2 absent**, a rate of 0.1 percent and the second best in the corpus.

All three are now recorded in the rejection store and gone from the base. One was a **Science news item
indexed by Crossref as a work**, which is the same family as the fellowship notices A322 cited. Two were
**nonexistent identifiers** returned by Crossref search but never registered.

---

## Verification

- `python3 _verify.py` **0 errors, 0 warnings**.
- `python3 tmp/a334/verify.py` **52 of 52**.
- `./_check.sh --drafts` **passes end to end**, 504 pages, no findings.
- **11,469 reference entries scanned** for delimiters, entities, doubled commas and carets, **all
  clean**. That scan is still the only method that has ever worked for this class.
- One lint finding fixed, a **bold span left unclosed by my own diction edit** in the previous pass,
  which the reflow then carried across a line break.
- `rather than` crossed the corpus maximum at 4.70 per thousand and was reduced to **4.20**.

---

## Outstanding

**Nothing blocking.** The tree is clean and the article is committed.

**The article is NOT pushed**, which is correct. **Publication of the thirty-eight X-Planes drafts
remains unauthorised.**

**The seeded identifier sweep returned 300 of 300 resolved**, with 41 through the issuing registry
rather than by HTTP. **That registry share rose from 5.5 percent to 13.7 percent and the rise is
expected**, because the primary harvest added 289 Defense Technical Information Center records and
those deposits refuse automated connections by design. A registry confirmation is strictly stronger
than an HTTP 200, so the higher share is a sign the base got more primary rather than less reliable.

**A further citation run was still in flight when this was written**, covering the identifiers added
during this pass. Its result belongs to the publication review, which is the next prompt if you want
it, and which is also the pass that pushes.

**Final state.** 18,691 lines, 42 display equations, 5,769 reference definitions, 100,512 words, with
**all 5,552 research records cited and none left over**, plus 148 reference works.
