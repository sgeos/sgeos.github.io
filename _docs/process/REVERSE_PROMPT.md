## Last Updated

**Date**: 2026-09-02
**Task**: **A347, X-Planes: Boeing X-50 Dragonfly, equation-density review. The second of four.**
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

## The Equation Pass Computed the Keystone the Draft Had Only Asserted

**13 display equations to 40**, past A345's 36 and A346's 32.

**The article's central mechanism was carried entirely by a verbal argument.** The draft said the wake
skews off the canard before it leaves the tail and that the residual is a nose-up moment. That is the
claim the whole article rests on and it had no arithmetic behind it.

**It does now.** With the wake sheet descending at the induced velocity and convecting aft at the
flight speed, a surface at station $x_s$ and drop $h$ is clear once $V > v_i (R - x_s) / h$. **The
canard clears near 15 knots and the tail not until about 108.**

**The strongest part is a ratio.** The induced velocity and the surface height appear in both clearing
speeds and cancel, so

    V_tail / V_canard = (R - x_tail) / (R - x_canard) = 10.5 / 1.5 = 7.0

**The two quantities the estimate is least sure of are exactly the two that do not affect this
number.** Whatever they really are, the tail stays in the wake to roughly seven times the speed at
which the canard leaves it. The unopposed moment is equivalent to a centre of gravity shift of **3.7
to 7.3 inches**, or 5.1 to 10.2 percent of rotor radius, across exactly the band both airframes were
lost in.

**Other additions.** The reverse flow area fraction $\mu^2/4$ and its limit, where the whole disc
reverses at an advance ratio of two, reached when the tip speed has fallen to 20 percent of its
conversion-entry value and with all of that still left to lose. The retreating tip going negative at
an advance ratio of one. The advancing tip Mach number. The square law of rotor lift against rotor
speed, tabulated. Blade element loading and the local velocity that survives when the rotational term
vanishes. The four-term lift balance. Download and its weight fraction, in which the disc area
cancels. Induced power and figure of merit. Tip jet thrust reduced by the nozzle's own motion, and the
power it delivers, which fight each other. Aspect ratio with Helmbold's low aspect ratio lift slope,
showing the stopped rotor gives away 28 to 46 percent of its lift-curve slope to its own proportions.
The same surface sized twice, at cruise and maximum speed, differing by a factor of 6.42.

---

## Three Defects in the New Work, and Only One Was Caught by a Machine

**The verifier caught a real arithmetic error.** The maximum-speed Mach number was stated as 0.575
against a computed 0.574.

**Two were caught by reading, and both were in prose I had just written.** A band from 15 to 108 knots
was described as **an order of magnitude** when it is a factor of seven. And I claimed the hover-value
induced velocity biased the estimate **conservatively**, when in fact a smaller induced velocity moves
**both** clearing speeds down together and shifts the band rather than widening it.

**A third was the A345 class again.** A note about rounding was written inside the reaction-drive
argument, and a remark about an earlier draft was written inside the wake section. **The article
narrating its own drafting history in its own reasoning is a defect this method produces reliably**,
and it has now been caught twice in two passes on this article alone.

**Where the Framing Breaks Down gained a paragraph saying that quantifying an inference does not make
it evidence.** The numbers show the proposed mechanism is of the right size to matter. They do not
show that it operated.

---

## Verification State

- `python3 _verify.py` reports **0 errors, 0 warnings**.
- `python3 _lib/test_lib.py` reports **98 of 98**.
- `tmp/a347/verify_numbers.py` reports **ALL CHECKS PASS**, now **96 recomputed claims**, all 96
  present in the prose, 19 cluster rows matching their own citations, cluster table matching sections.
- Reference integrity: **6,121 defined, 6,121 used, 0 undefined, 0 orphaned**.
- **40 display equations, none inlined with prose.** No contractions, no em or en dashes, no prose
  colons, only the mandatory `console.log` semicolon.
- **12,959 lines, 71,344 words, 13,815 author prose words.**

**No production build has been run.** That belongs to the publication review.

---

## Next

**The A347 primary-reference review**, the third of four passes. **Report primaries stand at 824 of
6,042, being 13.6 percent**, which is the lowest opening figure of the recent articles, so the pass
has room. The obvious targets are the stopped-rotor and X-wing report literature of the 1970s and
1980s, which is a NASA and Navy literature that Crossref indexes poorly, and the control-power and
handling-qualities specification reports.

**The book-identifier repair for A342 through A346 is still outstanding and still needs your
decision.** It is listed above.
