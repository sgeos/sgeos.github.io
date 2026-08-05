# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-05
**Task**: X-Planes series planned, verified, and documented. Handoff written ahead of your planned
compaction. No articles drafted.

---

## Where Things Stand

The series is ready to draft. 72 articles, A297 through A368, back-dated 2025-10-06 to 2025-12-16,
one per day unbroken, ending flush against the existing corpus. Zero collisions, zero date gaps,
contiguous numbering, all verified rather than assumed.

Because the series is back-dated, every article publishes immediately on push. It does not depend on
the daily cron, which has still not fired.

A fourth genre was needed and now exists. `_docs/writing/RESEARCH_AIRCRAFT_STRUCTURE.md` defines the
research-aircraft hybrid, since neither existing genre fits a vehicle built to answer one question.
That question behaves as an architectural keystone, so systems are dimensioned against it as in a
deep-dive, while programme origin, flight-test record, and the Epistemic State come from the essay.
It defines three article classes with explicit bands, because depth follows the surviving record
rather than effort.

---

## The Correction You Made

You challenged the assumption that X-plane designations are assigned monotonically, and you were
right. I had excluded X-76 after reading `designation-systems.net`'s "the next available design
number is X-69" as a ceiling. It is not. It describes the next unused sequential slot. The DARPA
release you supplied confirms the Bell Textron X-76 SPRINT and states the number was chosen as a
deliberate nod to 1776 for the country's 250th anniversary.

That mattered beyond one entry. **Seven of the nine anomaly cases surfaced only after I dropped the
sequential assumption** — the duplicated X-44, the leapfrogged X-69 to X-75 block, and the rest. It
also reframed the closer, which is now about a designation system that skips numbers to avoid
collisions, loses them to the parallel XQ- unmanned series, carries reservations never formalised,
holds a disputed assignment, reuses a number, and jumps for an anniversary.

I also withdrew a title I had proposed. Renaming X-42 to "an Upper Stage with an Aircraft Number"
embedded a conclusion drawn from a disagreement between two unequal sources into a title, where the
Epistemic State is the right home for that uncertainty. X-41 was renamed to "Common Aero Vehicle",
which is a genuine correction, since the previous title used a contested description rather than the
designation's name.

---

## Two Things Waiting On You

1. **Categories.** I have carried `aerospace history engineering` throughout, but that is my
   assumption and not your decision. It fixes 72 published URLs and cannot be changed later without
   dead links, which you have declined to mitigate with redirects. Worth one sentence from you.
2. **One commit is unpushed**, carrying the genre document the series depends on.

---

## A Note on Scale

At parity the series implies roughly 91,000 lines, 4,900 equations, and 20,000 reference definitions,
against a corpus that today holds 296 articles. That is not an objection, since you have been clear
that length is what it is, and the verification tooling now exists where it did not before.

But the citation volume is precisely the condition that produced 47 broken citations in the existing
corpus. Run `_verify_citations.py` per batch rather than at the end.

My recommendation stands that we draft A297 and A298, then stop, so you can judge shape and depth
before the pattern is set across seventy-two articles.

---

## State

Branch `master`, tree clean, one commit unpushed plus the handoff commit. `_verify.py` reports zero
errors. Recent deploys succeeded. The roster is embedded in `HANDOFF.md` so it survives a clean
checkout despite living in a gitignored scratch file.
