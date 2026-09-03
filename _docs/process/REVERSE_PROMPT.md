## Last Updated

**Date**: 2026-09-03
**Task**: **A348, X-Planes: Boeing X-51 Waverider, primary-reference review. The third of four.**
Committed and **not pushed**, since only the publication review pushes. **Not published**, and publication of the series
still not authorised. **Fifty-two of seventy-two drafted.**

---

## The First Article to Switch Sweep-Store Patterns Off, and It Nearly Was Not

**A346 recorded `ramjet` as a contaminant. A347 recorded `hypersonics` and `missiles`.** Both entries
carried a written warning that they must not be reused in the articles where those families are the
subject, and A347's named the X-15, X-30 and X-43 explicitly.

**A348 is the X-51. Those three patterns would have deleted 3,408 records, being 48.1 percent of
everything harvested**, including scramjet combustor flameholding, ramjet to scramjet mode
transition, waverider aerodynamics and inlet unstart prediction. That is not contamination. That is
the article.

**A warning addressed to a reader is not a mechanism**, which is this repository's oldest lesson and
it arrived again one article after the warning was written. `NOISE_PATTERNS` entries may now carry a
tag, `homonyms.TAGS` lists them, and `noise_hit` and `filter_records` take an `allow` list.

**An unknown tag raises rather than being ignored.** The quiet failure this prevents is an article
believing it has switched a filter off while its own subject is still being deleted, whose symptom
would be a thin survey with no explanation. Two regression tests cover both directions and the
library is **100 of 100**.

**Only tagged patterns can be switched off**, and every other pattern stayed armed, because
turbomachinery and atmospheric chemistry are contaminants here too.

---

## The Article

**The X-51A flew four times. On the flight that worked, the engine under test supplied under eight
percent of the vehicle's kinetic energy.** A 26 second rocket supplied 92.3 percent; the scramjet
supplied 7.7 across 210 seconds, taking 8.08 times as long to do a twelfth as much.

**A340 left a claim unfinished and this article tests it.** That article recorded that eleven seconds
on hydrogen has not demonstrated a propulsion system, because the thermal problem at length is a
different problem. **It was right, and the reason is arithmetic.**

**The X-51A flew 19.1 times longer than the X-43 at 6.67 times the lower heating rate, so it absorbed
2.86 times the heat load.** A short flight is a heat capacity problem. A long one is a heat transfer
problem, because the structure reaches equilibrium.

**The fuel does two jobs and they compete.** 270 pounds of JP-7 was the energy supply and the entire
heat sink aboard, and its heat sink capacity is 5.4 to 8.1 percent of the energy it releases.

**None of the three failures was combustion.** A thermal seal that had to take three quarters of an
inch of engine growth, an inlet unstart with a failed transition from ethylene to JP-7, and a fin
latch. **The discipline's exotic component works and its ordinary components did not.**

---

## The A347 Instrument Caught Six Errors in A348

**`_lib/booklinks.py` found six of eight book identifiers wrong in this article's first list.** The
two that were right are the two carried forward from A347's verified set.

**A hand-typed OpenLibrary key is wrong almost every time and a verified one stays right**, which is
an argument for the instrument rather than for care. Written one article ago, paid for immediately.

---

## Two Bugs of the Same Class, One in My Own Diagnostic

**A347's `\bcompressor\b` could not match `COMPRESSORS`.** While auditing A348 I wrote a probe for
civil-engineering contamination containing a bare `urban`, which matched inside **dist·urban·ce** and
reported 48 hypersonic flight-control papers as contaminants. **The probe was the defect.**

**Both are the A345 near-miss class**, where `\bX-?48\b` could not match `X-48B`. It has now appeared
three times, twice in patterns written to implement the lesson.

---

## The Equation Pass Supplied the Argument's Missing Half

**19 display equations to 39.**

**The draft argued from duration and never said what duration does to a solid.** Heat diffuses as the
square root of time, so at a diffusivity typical of a nickel superalloy the heat reached **6.2
millimetres into the structure on the X-43 and 27.1 on the X-51**.

**The ratio is the firm part**, being the square root of the ratio of burn times, and it depends on no
material property at all because the diffusivity cancels. The absolute depths depend on it entirely.
**Six millimetres is a skin. Twenty-seven is not carriable as dead mass**, and that is the distinction
between a heat capacity problem and a heat transfer problem made concrete.

---

## The Flight Data Bounds the Engine the Programme Never Published

**Inverting Breguet's range relation gives a product and not a value.**

    Isp x (L/D) = R / (V ln(W0/W1)) = 3,215

At a lift-to-drag ratio of 3 the engine was making about **1,072 seconds** of specific impulse; at 2 it
is 1,607 and at 4 it is 804. **The flight cannot separate the two factors** and the article says so.

**The vehicle's own acceleration over the burn gives a net specific impulse of 87 seconds**, a lower
bound because the altitude at booster separation is unpublished and any climb is energy the engine also
supplied. **Between 89 and 95 percent of what the engine made went into drag.**

That is the article's thesis seen from the propulsion side: the engine was not the marginal component.

---

## Two More Results Worth Naming

**The waverider's compromise is now a temperature.** Sutton and Graves gives 2.85 megawatts per square
metre at a five millimetre nose radius and 0.90 at fifty, and radiation equilibrium puts those at
**2,543 and 1,839 degrees Celsius**, both above any structural material. **The shape wants a sharp
edge to keep the shock attached and the thermal problem wants a blunt one.**

**The Kantrowitz limit makes the second flight's failure a number.** A fixed-geometry inlet at Mach 5.1
cannot contract internally past **1.55**, the throat being at least **0.646** of the capture area, so
any further compression has to come from the forebody, which is the other reason the vehicle is shaped
as it is.

**The seal was inverted to give the engine length.** Three quarters of an inch of growth implies an
engine about six feet long, offered as a consistency check rather than a measurement.

---

## The A347 Lesson Was Applied One Pass Earlier

**A347's publication review found its Epistemic State and framing section stale**, both written at the
draft pass and never updated for the two passes since.

**Both were updated in this pass, immediately.** The Epistemic State now lists every derived quantity
rather than the draft-pass subset, and a fifth framing limit names the six results that rest on
material and mixture properties this vehicle never published, being a diffusivity, an expansion
coefficient, a temperature rise, a nose radius, an emissivity and a stoichiometric ratio.

**One instance of drafting narration was caught and removed** from inside that section, where a limit
had been introduced as something a named pass had added. **The argument does not narrate its own
history**, and this defect has now appeared in three consecutive articles.

---

## The Primary Fraction Opened at 14.2 Percent and the Reason Was Not the Harvest

**Supersonic combustion stood at 4.3 percent primary across 1,137 records.** The coolant argument
stood at 4.2. **The sibling programme this whole article compares against had two records.**

**That is a fact about where hypersonic propulsion was published.** NASA Langley and the Air Force
Research Laboratory worked it out between roughly 1960 and 2010 and issued reports, while the modern
journal literature on scramjet combustion is enormous and international. **A balanced sweep dilutes
the primary fraction even when every record it adds is on subject.**

**Two repository-only sweeps took it to 21.4 percent**, 1,262 of 5,891.

---

## Two Subjects Were Aimed At Directly and Did Not Move

**Endothermic fuel and engine cycle analysis were the two thinnest and a sweep was written for each.**
Neither moved much, and the reason was **verified against what the repositories returned rather than
inferred from the pool**, which is A345's lesson.

**Across the 3,660 records the two repositories returned in total, eighteen touch endothermic fuels or
fuel heat sink and five touch cycle analysis or specific impulse.** Several of the eighteen are
off-subject, being photochemical hydrazine synthesis and a methanol shelter cooling system.

**Fuel heat-sink measurement and cycle accounting are things a contractor measures and does not
publish.** Both of the article's arguments resting on them are now carried by a small named set rather
than by a keyword sweep, and the article says so.

---

## Twenty-Nine Primaries Named by Identifier, Every One Verified

Chief among them the **Mach 5 endothermic-fuel thermal management study**, which is this article's
coolant argument almost exactly; the **X-43A Mach 10 lessons-learned report** and the chief engineer's
account of that flight; the **actively cooled structural panel series of 1978 and 1979**, which is
what a long flight actually needs; the **stream thrust accounting method**, which is how an engine
with no separable inlet or nozzle is measured at all; and the **waverider heat transfer work** that
bears directly on the sharp-versus-blunt compromise.

---

## A Diagnostic of Mine Reported Two Records Where There Were Sixteen

**A probe for the Hyper-X programme was written as `hyper-?x`.** The corpus normalises an intraword
hyphen to a space before matching, so the pattern could not match `Hyper X` and reported the sibling
programme as almost absent from a pool holding sixteen records of it, eleven of them primaries.

**That is the fourth separator or boundary failure in this article's preparation**, after `X-48B`
against a hyphenated pattern in A345, `COMPRESSORS` against `\bcompressor\b` in A347, and a bare
`urban` matching inside `disturbance` earlier in A348.

**Every one reported the data as wrong when the diagnostic was wrong**, which is the dangerous
direction, because it argues for work that is not needed and hides work that is.

**`survey.loose` now splits on hyphens as well as spaces** and carries a regression test naming all
four incidents. Library 100 to 101.

---

## The Pool Counts Are Now Emitted

**The Source Base stated how many records name the X-51, the waverider and supersonic combustion, and
all of those were hand-typed.** They moved three times during this pass and would have gone stale each
time. They are emitted from `refs.json` at assembly now, which is the A342 defect class **prevented
rather than caught**.

---

## Verification State

- `python3 _verify.py` reports **0 errors, 0 warnings**.
- `python3 _lib/test_lib.py` reports **101 of 101**.
- `tmp/a348/verify_numbers.py` reports **ALL CHECKS PASS**, now **80 recomputed claims**, all present
  in the prose, 17 cluster rows matching their own citations, cluster table matching sections.
- Reference integrity: **5,966 defined, 5,966 used, 0 undefined, 0 orphaned**.
- Book links **8 checked, 0 mismatched**. All 20 foundational NTRS identifiers and all promoted DTIC
  identifiers resolve or are registered.
- **12,589 lines, 70,295 words, 12,921 author prose words, 39 display equations, none inlined.**
- Survey **5,891 research records, 1,262 report primaries at 21.4 percent**.

**No production build has been run.** That belongs to the publication review.

---

## Next

**The A348 publication review**, the fourth and last pass. It builds and it pushes.

**Finish the entire prose read before starting the build.** A347's review started the build twice and
killed it twice, because the read kept finding things. The rule earned there is that a publication
review reliably finds prose defects and any build started before the read is finished is wasted.

**Read the opening against the conclusion first.** That has found a defect in three consecutive
articles, most recently a disc loading compared to a Black Hawk that nothing in the article computed.

**The book-identifier repair for A342 through A346 remains outstanding and still needs your decision.**
