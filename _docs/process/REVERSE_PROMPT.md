## Last Updated

**Date**: 2026-09-02
**Task**: **A347, X-Planes: Boeing X-50 Dragonfly, primary-reference review. The third of four.**
Committed and **not pushed**, since only the publication review pushes. **Not published**, and
publication of the series still not authorised. **Fifty-one of seventy-two drafted.**

---

## The Article

**The X-50A existed to demonstrate one manoeuvre, flew nine times across two airframes, was destroyed
twice, and never attempted that manoeuvre once.** Both losses were at low speed. Neither had anything
directly to do with the conversion the programme was funded to prove.

**The article argues the two are not independent, and the argument is geometric.** A rotor can be
stopped in flight only if it is unloaded first. Unloading it means the canard and horizontal tail must
carry the entire aircraft at conversion speed. That requirement sets their size. On an aeroplane this
small it produces two lifting surfaces spanning **0.742 and 0.675 of the rotor diameter**, sitting
directly beneath a rotor whose disc loading is **12.9 pounds per square foot, being 1.34 times the
X-49A's**, because the same surface also has to be a wing at 380 knots.

**As the aircraft accelerates the wake skews aft, leaving the canard before it leaves the tail, and
the residual is a nose-up pitching moment that grows with airspeed.** The 2006 accident finding was a
nose-up pitching moment from airspeed and rotor wake exceeding control authority.

---

## The Finding That Carries the Article, and What It Is Not

**A 2001 NASA Ames inviscid computation of this exact aeroplane identified forebody upwash as a source
of positive pitching moment and stated that no change to the hub geometry could relieve it.** The same
paper concluded that **the amplitudes of the moments are well within the authority of the control
surfaces**.

**Five years later the second airframe was lost to a nose-up pitching moment the controls could not
answer.**

**The article states the limit of that coincidence at length rather than trading on it.** The
computation was at 130 knots in conversion. The accident was at low speed before conversion entry.
**These are different flight conditions and the paper was not wrong about the one it examined. It was
never asked about the one that mattered**, because the X-wing had taught the community that conversion
was the hard part. That is a finding about where analysis effort goes, and it is labelled as inference
in the Epistemic State.

---

## The Results Probe Was Run at the Draft Pass, Not the Publication Review

**A340 through A346 all discovered at their fourth pass that the survey under-covered their own
conclusions.** Both measurements were made here before the prose existed.

| Subject | Article's words | Field's words |
|---|---|---|
| the stopped rotor and its conversion | 30 | 167 |
| the conversion corridor | 5 | 95 |
| reaction drive | 28 | 258 |
| control authority | 14 | 24 |
| the elliptical section | 7 | 236 |
| rotor wake on the tail | 0 | 140 |
| pitch-up at low speed | 3 | 111 |
| the low aspect ratio wing | 140 | 219 |

**Seven of eight opened by factors between two and infinity, which is the third consecutive article to
reverse A340 through A344.** The eighth moved 14 to 24, **and it is the subject both airframes were
lost to**, so a supplementary harvest ran immediately rather than being deferred. It now stands at 160
records and its cluster at 941.

---

## Nine of Ten Book Identifiers Pointed at Unrelated Works

**This is the most serious thing found this session and it was inherited, not introduced.**

The hand-written book list carried from A346 was checked against OpenLibrary for the first time.
**`Leishman, Principles of helicopter aerodynamics` resolved to `The 2007-2012 Outlook for Dark Rum in
Japan`.** `Prouty, Helicopter performance, stability and control` resolved to a book on buying
apartment buildings. `Stepniewski and Keys, Rotary-wing aerodynamics` resolved to `Rural
modernization`.

**Every existing check passed on all nine.** The link resolves, so a status check is satisfied. The
block is well formed, so `_verify.py` is satisfied. The page renders the label the article wrote, so
`render.py` sees nothing. **A citation whose text is right and whose target is wrong is invisible to
every check that does not read the target, and this corpus had none.**

**Measured scope: 510 distinct work keys across 40 files. Of the 215 carrying a title-style label, 19
disagree, and every one is in an unpublished draft.** That is luck, not process.

**`_lib/booklinks.py` is the instrument**, with three regression tests. It deliberately skips the
generated `Author Year` citation style, which claims no title and came from a real lookup. The first
version of the measurement did not, and over-reported by a factor of four.

**A347's own list is now thirteen verified keys.** Two books were **dropped rather than guessed at**,
having no locatable repository record.

### Still outstanding, and it needs your decision

**A342, A343, A344, A345 and A346 still carry wrong keys**, being five drafts and no published post.
Repairing them is an edit to five other articles and outside the scope of drafting A347, so it has not
been done. The affected anchors are
`book_sheridan`, `book_anderson_performance`, `book_nicolai`, `book_hoerner_lift`, `book_mccormick`,
`book_schlichting`, `book_misra_enge`, `book_bramwell`, `book_johnson_helicopter_theory`,
`book_leishman`, `book_prouty` and `book_stepniewski`.

---

## One Identifier in This Article Was Fabricated and Caught Before Assembly

**A NASA Technical Reports Server number for the 1992 report `Smoother conversion from helicopter to
airplane` was written from the title rather than looked up, and 19940020285 does not resolve.** The
correct record is 19920000710. It was found because every foundational identifier was verified against
the repository before assembly rather than after. **Same defect class as the book keys, found by the
same habit.**

---

## The Gate Was Audited Four Times and Changed Every Time

**Eleven homonym families were predicted in advance and four occurred.** The NASA Dragonfly mission to
Titan, elliptic curves, the canard as a duck, the hub as a gene, the wake as the opposite of sleep,
energy conversion and the medical bleed all measured **zero**. That ratio is why the shared store
admits only observed patterns.

**Eight families were recorded in `_research/homonyms.py`, which is now 109 patterns.** Palladium
cross-coupling chemistry against the accident report's own words, Darrieus and Savonius turbines, the
electrical machine rotor, petroleum gas lift, turbine blade cooling, turbomachinery compressors,
atmospheric chemistry against `gate.ATMOSPHERE`, and insect flight against the aeroplane's own name.

**The residual was a fact about the clusterer and not the field.** It stood at 1,355 records, a quarter
of the pool. Reading thirty-four showed it was on-subject flight-control and wake literature the
cluster patterns refused on adjacency while the gate admitted it. Widening them moved 479 records.

---

## Verification State

- `python3 _verify.py` reports **0 errors, 0 warnings**.
- `python3 _lib/test_lib.py` reports **98 of 98**, up from 95.
- `tmp/a347/verify_numbers.py` reports **ALL CHECKS PASS**, being 50 recomputed claims, all 50 present
  in the prose, 19 cluster rows matching their own citations and the cluster table matching the
  sections.
- Reference integrity: **6,121 defined, 6,121 used, 0 undefined, 0 orphaned, 0 duplicate URLs**.
- Book links: **13 title-style citations checked, 0 mismatched**.
- Prose style: no contractions, no em or en dashes, no prose colons, and the only semicolon is the
  mandatory `console.log` tag. Thirteen display equations, none inlined with prose.

**No production build has been run.** The draft pass does not build. The stub build belongs to the
publication review and costs roughly half an hour.

---

## The Number Verifier Disagreed Four Times and Every Disagreement Was a Tie

**The two reaction-drive penalties compute to exactly 1.455 and 2.425, the length ratio to exactly
1.475 and the slipstream velocity to exactly 61.75 knots.** At the precision first written each was a
coin toss and the article and the checker had called it differently. **The rule adopted is to state
such a value at a precision where it is not a tie.** Choosing a rounding convention instead would have
made the disagreement invisible rather than absent.

**One defect of the A345 class was also caught.** The note explaining that rule had been written
**inside the reaction-drive argument**, which is the article narrating its own method in its own
reasoning. It was moved to the Source Base.

---

## The Primary Pass Changed the Article's History

**The draft called the X-50A the second serious attempt at a stopped rotor, following the X-wing. It
is the third.**

**Hughes proposed a tip-jet driven rotor/wing in 1965**, developed it as a research aircraft design
through 1968, and offered it as city-centre transport in 1967. **The propulsion was flight-proved on
the XV-9A, which first flew in November 1964.** No rotor/wing aircraft was ever built.

**None of this appears in any secondary account of the X-50 consulted for this article.** It was found
by asking the Defense Technical Information Center for hot cycle rotors, not by asking anybody about
the X-50. Reading about an aeroplane produces the predecessor that aeroplane's own literature names.

**It also handed the reaction-drive argument a flight test.** The XV-9A worked, and Hughes abandoned
pressure-jet propulsion because the aircraft was **noisy and burned a great deal of fuel**. That is
the Froude efficiency the equation pass computed, being paid forty years before this aeroplane was
asked to pay it again.

**The opening history, the research question, the reaction-drive section and the conclusion were all
rewritten.** A survey that changes the argument is the pass working.

---

## The Equation Pass Had Moved the Keystone and the Survey Had Not Followed

Probing the pool for what the article now argues from found the support close to absent.

| Subject | Records | Primaries |
|---|---|---|
| rotor wake skew angle | 0 | 0 |
| download pitching moment | 0 | 0 |
| empennage in the rotor wake | 4 | 0 |
| figure of merit | 0 | 0 |
| blade element theory | 86 | 0 |

**A survey holding 86 records on blade element theory and no primary among them is not a survey of
blade element theory.**

**The relation the whole article turns on was named rather than searched for.** Heyson and Katzoff's
1957 treatment of induced velocities near a lifting rotor is where the wake skew relation comes from,
and no keyword sweep in this article had returned it. Six further reports on inflow modelling, wake
geometry and rotor-fuselage interaction went in the same way, each verified against the repository
before being added.

---

## Why the Fraction Opened Low, and What Fixed It

**13.6 percent was the lowest opening of the recent articles, and that is a fact about where this
subject was published.** Stopped rotors, wake skew, empennage immersion and control power were worked
out by NASA, the Army and the Navy between roughly 1955 and 1995 and issued as reports, which Crossref
indexes poorly. **A general sweep dilutes the primary fraction even when every record it adds is on
subject**, because Crossref returns roughly six records per repository record on these queries.

**The second sweep asked the two repositories only**, so every record it could return was a primary by
this article's definition. **Final: 1,836 of 7,708, being 23.8 percent, past A346's 23.0.**

**The share by cluster is uneven and the article prints the whole table.** Weight and sizing reaches
57.7 percent because sizing is what a contractor writes a report about. **Two clusters stayed low
after being aimed at directly**, being the article's own subject at 11.5 percent and control power at
11.1, and the article says so rather than hiding it. A cluster that does not move when aimed at is
reporting something about the field.

---

## A Verification of Mine Was Broken and Nearly Condemned a Thousand Citations

**A sample of ten report identifiers was checked by requesting each address and all ten failed.** The
conclusion available at that moment was that the survey's report primaries did not resolve.

**The failure was a certificate verification error in my own checking script.** Re-checking against
the Crossref registry, which is what this corpus verifies citations against rather than an address
returning a status, found every one registered, and a fourteen-record sample returned fourteen of
fourteen.

**A broken check reports the data as broken, and that is the dangerous direction**, because a checker
that fails loudly against good data trains its reader to overrule it.

---

## The Sweep Store Gained Six More Observed Families

Now **115 patterns**. A military environmental assessment for a **wastewater lift station** reached the
kept set on the word LIFT, and one for a tactical air control **wing** on the word WING.
Thick-section **composites** reached the aerofoil cluster against a thick aerofoil section. Also
helmet-mounted display symbology, rotor blade structural repair, spacecraft formation flying, and
hypersonics.

**The hypersonics pattern carries an explicit warning not to reuse it blindly.** This series covers
the X-15, the X-30 and the X-43, and for those articles hypersonics is the subject rather than the
contaminant. It is recorded only because A347's aeroplane never exceeded Mach 0.6.

---

## Verification State

- `python3 _verify.py` reports **0 errors, 0 warnings**.
- `python3 _lib/test_lib.py` reports **98 of 98**.
- `tmp/a347/verify_numbers.py` reports **ALL CHECKS PASS**, now **102 recomputed claims**, all present
  in the prose, 19 cluster rows matching their own citations, cluster table matching sections.
- **The survey statistics are now emitted from `refs.json` at assembly rather than typed**, by
  `emit_source_base.py`, so the paragraph and the per-cluster primary table carry no hand-written
  number. That closes the A342 defect class at its source rather than checking for it afterwards.
- Reference integrity: **7,788 defined, 7,788 used, 0 undefined, 0 orphaned**.
- Book links: **13 checked, 0 mismatched**. All 16 hand-added reference URLs return 200.
- **16,364 lines, 91,414 words, 16,641 author prose words, 40 display equations, none inlined.**

**No production build has been run.** That belongs to the publication review, and costs roughly half
an hour against a stub site.

---

## Next

**The A347 publication review**, the fourth and last pass. It builds and it pushes.

**The known target has fired for seven consecutive articles**, being that the survey under-covers the
article's own conclusions. **A347 ran that probe at the draft pass instead**, so the publication
review should probe the conclusions as they now stand, which are not the ones the draft had. The
history, the reaction-drive argument and the conclusion were all rewritten this pass.

**The book-identifier repair for A342 through A346 is still outstanding and still needs your
decision.**
