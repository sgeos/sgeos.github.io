# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-12
**Task**: A334, the Boeing X-37. **Equation-density review complete.**
**Committed. NOT pushed**, per the rhythm in which only the publication review pushes.

---

## Twenty-Four to Forty-Two, and Nine of Twenty Gaps Closed

`_lib/audit.py` reported **twenty sections naming numbers with no displayed relation**. Nine are now
closed. **The eleven that remain are reference lists, date lists, dollar figures and restatements**,
and not one of them relies on a relation, so they are reported rather than padded.

The article moved from 14,457 lines and 78,320 words to **14,632 lines and 79,704 words**. **The
reference base did not move**, holding at 4,440 definitions with all 4,223 research records still
cited, because this pass adds relations and not literature.

---

## The Three Best Additions Were Not in the Audit's List

**The audit finds sections carrying numbers without equations. It cannot find a relation the article
never mentioned at all**, and all three of these came from asking what each argument silently assumes.

**Nodal precession, which turns an assumption into a measurement.** The draft averaged the eclipse
fraction over the node and the season without establishing that the node actually turns. Under $J_{2}$
it regresses at **-6.169 degrees per day** at 400 kilometres and 40 degrees, so the node completes a
turn in **58.35 days** and the beta angle cycles at the beat with the Sun's motion in **50.32 days**.
**The sixth mission therefore swept the node 15.58 times and the beta angle 18.06 times.** The average
is not a modelling convenience. It is what the mission experienced, and an article quoting a single
beta angle for a flight of this length would be quoting a transient.

**The scaling exponent, which quantifies a penalty the draft only gestured at.** Measuring the exponent
that relates two vehicles rather than comparing ratios, mass scales as length to the **1.924** against
3 for geometric similarity while the payload bay scales as **3.226**. A geometrically similar orbiter
scaled down to 8.92 metres would mass **1,072 kilograms**. The X-37B masses 4,990, **a factor of
4.655**. **The small vehicle keeps the airframe and loses the room**, which is the square-cube penalty
in its clearest available form and explains a 4.55 percent payload fraction without apology.

**The duty cycle, which is the operational claim the durations add up to.** First launch to seventh
landing is 5,433 days and the seven missions total 4,208.57, so **an X-37B has been in orbit for 77.46
percent of fifteen years**, on two airframes. **That is a statement about turnaround rather than about
endurance**, and the single-mission record conceals it.

---

## Reading the Forty-Two Equations Found Eight Symbol Collisions and Nothing Else Did

No checker reports a symbol used for two quantities. Reading the equations as a set does.

| Symbol | Wanted by | And also by |
|---|---|---|
| $\varepsilon$ | specific orbital energy | emissivity |
| $a$ | semi-major axis | albedo |
| $D$ | depth of discharge | drag, in $L/D$ |
| $e$ | cell specific energy | eccentricity |
| $h$ | height | specific angular momentum |
| $\eta$ | duty cycle | the charge and discharge efficiencies |
| $n$ | mean motion | the scaling exponent |
| $A$ | solar array area | the drag reference area |

**Each is resolved by marking one rather than by reusing it silently**, and a **Notation** table near
the head of the sizing section states which and why. **One case is deliberate and is now explicit.**
The orbit count and the battery cycle count are written as $N_{\text{orb}}$ and $N_{\text{cyc}}$ and
then shown to coincide, **because their coincidence is the article's central claim** and assuming it by
sharing a letter would have been assuming the conclusion.

---

## The Equation Pass Created a Citation Debt and Paid It in the Same Pass

`citation_gaps` went from **14 to 0**. Every new relation initially stood more than nine hundred
characters from any literature, because the cluster markers sat at the ends of sections. Splitting them
so each displayed relation carries citations within reach cost nothing, since every record was already
cited and the trailing all-remaining markers simply absorb whatever is left.

Thin sections fell from five to one, and **the survivor is the Conclusion**, which restates and cites
nothing by design.

---

## My Own Text Check Was Broken and Passed Twelve Values That Were Not in the Article

**This is the worst thing in this pass and it was mine.** `Checker.require_in_text` takes a single
formatter, which is too rigid for an article printing 7.6686 kilometres per second, 232.8 kelvin and
14,140 orbits. I replaced it with one that tries several roundings, **and the replacement allowed zero
decimal places.** In a document of 79,000 words and 4,440 reference entries, a bare `58` stands for
58.3519 and a bare `2` stands for 1.9236 by accident every time.

**It reported 47 of 47 passing while twelve verified values were absent from the draft.**

The fix is a floor of **three significant digits** plus digit-boundary matching, so `58.4` cannot match
inside `1958.42`. **And a self-test now runs first**, asserting that the check finds a value known to be
present and refuses one known to be absent. **A clean report from an unvalidated checker is not
evidence**, which the traps document already said and which I had to learn again.

---

## Verification

- `python3 _verify.py` **0 errors, 0 warnings**.
- `python3 tmp/a334/verify.py` **52 of 52**, up from 34, with the new relations re-derived by
  independent routes. The nodal precession comes back from the secular rate written longhand, the beta
  cycle from accumulating phase rather than dividing rates, the scaling exponent from solving the power
  law forward, and the duty cycle span from the calendar.
- `python3 _lib/test_lib.py` **75 of 75**.
- `./_check.sh --drafts` **passes end to end**, 504 pages, no findings.
- Every one of the 42 equations was read for brace balance, delimiter closure, bare pipes and doubled
  backslashes, and all 42 are clean.

---

## Outstanding

**Nothing blocking.** The tree is clean and the article is committed.

**The article is NOT pushed**, which is correct. **Publication of the thirty-eight X-Planes drafts
remains unauthorised.**

**For the primary-reference pass, which is your next prompt if you want it:** `_lib/audit.py` reports
**primary sources at 2,125 of 4,319, or 49.2 percent**, at the article's own 2011 cutoff. The period
count is 2,015 and the contemporary count 2,160, and both are reported in the article rather than only
the fraction.

**The corpus citation run is still an open decision.** It stands at 46 hard and 184 weak findings
across 87 articles with 61 clean, and A334's own coverage was 34.5 percent when last measured. **A
report that lists only articles with findings cannot distinguish a clean article from an unexamined
one**, so coverage must be measured rather than inferred from an absent row.
