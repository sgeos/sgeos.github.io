# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-05
**Task**: A303 primary-reference review. Committed and **not pushed**. **No article in this series is
published.**

**287 to 358 references, 85 to 156 primary technical documents, 1235 to 1385 lines.** All three
densities are now inside band, and the line shortfall closed by citation rather than by padding.

---

## Every Coefficient the Article Uses Now Has Its Source

The equation pass left the article quoting physical constants it could not attribute. A buildup
factor of ten, a neutron removal cross-section of 0.095 per centimetre, a flux-to-dose conversion, a
core pressure drop. Those are the numbers the whole shield derivation turns on, and they were
standing on my assertion.

They are all in the programme's own record.

- **Chapman 1955** tabulates the effective neutron removal cross-sections for shielding.
- **Auslender 1957** computes the gamma buildup factors by Monte Carlo, for layered configurations.
- **Eggen 1961** gives the fast-neutron spectra and the dose-rate calculation.
- **Segaser 1948** measures pressure drop through fuel element channels, and it is among the earliest
  documents in the entire archive.
- **Waldrop 1958** treats lithium hydride specifically as a *mobile* neutron shield, which is the
  aircraft requirement written as a material specification.

**The article no longer quotes a constant it cannot attribute.**

---

## The Lexington Project Recovered in Full

The draft treated the 1948 feasibility study as a one-line verdict, fifteen years and a great deal of
money. It was a numbered report series, and OSTI holds it.

There are reports on aircraft, on aircraft configuration, on a meeting with Boeing, and on something
as specific as the tolerance of aerial reconnaissance film to nuclear radiation, plus an index
complete enough to be a document in its own right.

**Most importantly it contains its own comparison baseline.** [Shoults 1948] examined whether
chemically propelled aircraft could complete the same missions. That is the question that eventually
ended the programme, it was asked at the very beginning, and it was answered wrongly.

---

## The Molten Salt Pivot, Documented As It Happened

The draft asserted that the Aircraft Reactor Experiment became the ancestor of the modern molten salt
reactor. The record shows the handover in progress.

**McPherson 1957 is titled *Molten Salts for Civilian Power* and appeared while the aircraft programme
was still running.** Briant 1957 argues molten fluorides as power reactor fuels, Grimes 1958 sets out
the chemistry, and by MacPherson 1960 the concept is being evaluated against a ten-year plan that has
nothing to do with aeroplanes.

The people who built a reactor for an aircraft spent the late 1950s explaining that it would be more
useful somewhere else, and they were right.

---

## Two Things With No Counterpart Elsewhere in the Series

**Menegus 1958** computes the accidental dispersion of reactor materials in a crash and the distance
that must be controlled around the site. No other aircraft in this series could contaminate the ground
it fell on, and no other article has needed a citation of that kind.

**A NEPA medical advisory panel subcommittee report evaluates the psychological aspects** of asking
aircrew to fly a reactor. That is an unusual document to find in an aeronautical record and it says
something about how the problem was understood at the time. Alongside it, Leverett 1960 investigates
lens opacity in personnel operating a portable reactor, cataract being the effect that shows up first.

---

## Verification

358 references with zero undefined, zero orphaned, and zero duplicate URLs. All **248 meaningful-404
URLs at 200 across three archives**. Every added OSTI record verified individually against the API.
`_verify.py` at the 0-error 21-warning corpus baseline. Zero style violations, zero doubled words,
zero display-math seam defects. Isolated build succeeding with 92 rendered display blocks and Part 7
navigation.

A formulaic drift was caught and corrected. The construction `, and [Author]` reached 50 percent of
body citations after the pass, because seventy references went in during one sitting. Nine passages
were rotated, bringing it to 41.7 percent, with the remainder being genuine list conjunctions rather
than a repeated citation verb.

---

## What Remains

**Contemporary references are 59 absolute and 23.5 percent of dated, down from 32.8 percent purely by
dilution**, and that is now below the 28 to 33 percent target. Nothing was removed and nothing was
padded. It is the publication review's business.

For scale, this article now holds 156 primary technical documents at **43.6 percent of all
references, the highest in the series**, and 63.7 percent of its dated references fall in 1965 or
earlier. That shape is what a programme whose entire technical life fit inside fifteen years looks
like.

**Publication order dependency is seven deep.** Three commits unpushed. Categories remain
`aerospace history engineering`, seven articles deep.
