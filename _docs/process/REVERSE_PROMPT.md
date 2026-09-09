# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

## Last Updated

**Date**: 2026-09-09
**Task**: **A354, X-Planes: ESAero X-57 Maxwell, primary-reference review. The third of four
passes.** Committed and **NOT PUSHED**, which is the rhythm. **Not published**, and
publication of the series still not authorised. **Fifty-eight of seventy-two drafted.**

---

## Report Primaries 187 at 7.6 Percent to 342 at 11.2, and Both Numbers Moved

**References 2,567 to 3,176, research 2,451 to 3,060, lines 5,669 to 6,905, words 33,185 to
40,283.** Display equations unchanged at 34.

---

## A Programme's Own Index Cannot Be Searched, Only Read

**This is the pass's finding and it strengthens the previous article's rather than
repeating it.**

NASA publishes a page listing the X-57 programme's technical output. **Sixty-three entries
were transcribed from it and sixty-one resolved**, the other two carrying metadata too thin
to identify. **The first sweep had retrieved eleven of those sixty-one**, which is eighteen
percent, from a sweep built specifically to avoid the failure A353 documented and which
queried the designation alone.

**THE REASON WAS TESTED RATHER THAN ASSUMED, AND A HYPOTHESIS WAS DISPROVED.** A direct query
for the designation reports **seventy-four matching records and returns ten**. Asking for a
hundred returns ten. **Asking for the eleventh onward by offset returns the same ten again**,
at every offset tried from ten to seventy.

**The suspicion was that the fetching library never paginates and was leaving records on the
table, which would have been a defect affecting every article in this series.** It
paginates correctly and the server ignores the offset. **The library's own note already said
the endpoint caps well below what is asked for, and that note is right.**

**So A353's lesson needs strengthening.** Query a distinctive designation alone rather than
beside generic words, yes. **But this article did that and still retrieved eighteen percent,
because the constraint is not the query.** The remaining sixty-four records cannot be reached
by that interface at all. **A programme's own published index must be read.**

---

## A Presence Check Was Satisfied by a Second Copy of the Same Sentence

**A353 found that a presence check cannot tell whether it matched the equation or the prose.
A354 found the next case, which is a figure appearing twice in the PROSE.**

The implied lift to drag ratio is stated once where it is derived and once where the article
records what the equation pass changed. **An injection altered one of them and the check was
satisfied by the other.**

**The fix counts the stem and requires every occurrence to carry the computed value**, which
closes both cases at once and fails loudly if the stem disappears entirely. It was proved
against an injection in the first position, the second position, and both at once.

---

## Verification

**Verifier clean at 0 errors and 0 warnings. Tests 108 of 108. Lint 0 findings.** The symbol
scanner reports all 52 declared symbols used and every symbol used declared.

**The article verifier runs 144 passing checks.** Seventeen injected defects were caught,
and the eighteenth was missed until the every-occurrence check was written, after which it
is caught in either position and in both.

**Twenty-four of the sixty-one curated identifiers were sampled and every one matched its
own record's metadata**, alongside a deliberately absent report number as a control, which
failed correctly. **One documented exception is carried rather than a threshold quietly
lowered**, being a record whose NTRS metadata is truncated to `X-57 Maxwell Aircraft` where
NASA's own index gives the fuller title, and the check asserts the record's title is a
prefix of the label used.

**FINAL STATE. 6,905 lines, 34 display equations, 52 declared symbols, 3,176 reference
definitions, 40,283 words**, research 3,060, report primaries 342 at 11.2 percent, two
sweeps retrieving 8,079 records of which 7,031 distinct, gate 3,138, store residual 9.8
percent. **All 3,176 definitions are cited, none orphaned and none undefined.**

**The stub-isolated production build succeeded in 121 seconds against the exact bytes
committed**, checksum matched before and after. **The rendered audit reports no findings
across 93 pages.** Source and rendered display-equation counts agree at **34**, with zero
raw dollar pairs leaking, zero unresolved reference brackets, zero unexpanded slots and zero
unrendered Liquid. The page is 608,311 bytes.

---

## What Is Not Done

**The publication review has not run.** It is the pass that reads the opening against the
conclusion, which has found a defect in every article since A340, and the pass that probes
each conclusion against the pool.

**Two disagreements remain recorded and unresolved**, being the high-lift motor power at
12.6 kilowatts in the flight performance report against 10.5 in the reference literature,
and the battery at 80 watt hours per pound against a usable 55.

**And one boundary stands rather than a conclusion.** The equation pass established that
raising dynamic pressure over seventy percent of the span cannot by itself account for
landing this wing on the installed power. **The article says it does not know from these
sources how much of the remaining work the other slipstream effects do**, and the
publication review should check whether the enlarged reference pool can now answer that.
