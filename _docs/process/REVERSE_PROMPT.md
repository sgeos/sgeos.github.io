# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-05
**Task**: A304, the Lockheed X-7, drafted. Committed and **not pushed**, per the four-pass rhythm.
A297 through A303 are unchanged and pushed. **No article in this series is published.**

---

## I Made Up Nineteen DOIs and Verification Caught It

This is the most important thing in this report and it is a failure rather than a finding.

While assembling the contemporary set I wrote out nineteen references with DOIs that looked right,
constructed from the publisher prefix and a plausible article number, instead of taking them from the
harvest records I had already downloaded. **Resolving them through Crossref showed that most pointed
at entirely unrelated papers** — one to a study of dendrite deformation in alloys, one to a paper on
alcohol licensing policy, one to heat flux on a hypersonic cone with a swept fin.

All nineteen were discarded and the contemporary set was rebuilt from actual harvest records, each
verified on author and title. **The rule is that an identifier which can be looked up must never be
constructed**, and I am recording it in the task log because a reader would have had no way to detect
the difference from the page.

A second, smaller version of the same mistake followed. Thirty-one prose citations used author names I
had guessed from document titles rather than the verified NTRS metadata, producing anchors with no
master entry. The anchor integrity check caught those, and all 42 affected citations were remapped.

---

## The Keystone Is Epistemic, Which Is a First for This Series

Every previous article concerns an aircraft that had to come back. This one is about what changes when
it does not, and the interesting difference is not speed.

**A crewed programme approaches a destructive limit and stops short of it, so its estimate of where
the limit lies is an extrapolation.** An expendable programme crosses the limit and interpolates. The
cost is computable, since the prediction variance of any fitted model carries a term in the squared
distance from the data centroid, and for twenty observations, predicting one full data span beyond
the centroid costs a **factor of 3.6** in standard error against predicting at the centroid.

The X-7 was not built for that reason and nobody in the programme described it that way. The article
says so explicitly, in Epistemic State and again in Where the Framing Breaks Down, because the
framing is mine.

---

## The Engine Explains the Whole Vehicle

A ramjet's compression ratio is **1 at rest, 7.8 at Mach 2, and 152 at Mach 4**. It is worthless
standing still and unmatched at speed, so the vehicle must be thrown. The booster delivers 1.87
million newton seconds, a velocity increment near 575 metres per second, and takes a release Mach
number of 0.45 to a burnout Mach number of **2.37, which is precisely where the engine becomes worth
having**. It does so at 13 g rising to 16, which no crewed vehicle could accept, so the booster is the
first place where having no pilot is a requirement rather than a convenience.

**A single normal shock at Mach 4.31 keeps 10.7 percent of the total pressure.** A staged conical
shock system keeps roughly half. That factor of five is the difference between an engine and a duct,
and it is why the most conspicuous feature of the vehicle is a spike doing nothing visible.

Recovery temperature at Mach 4.31 and 32 kilometres is **985 kelvin, or 712 degrees**, which excludes
aluminium and specifies steel eight years before titanium. The same stagnation temperature arrives at
the combustor and leaves only **922 kelvin of useful temperature rise against 1600 at Mach 2**, which
is the real ceiling on the subsonic-combustion ramjet and the reason the scramjet exists.

---

## Verification

252 references with zero undefined, zero orphaned, and zero duplicate URLs. All 125 meaningful-404
URLs at 200. All 58 DOIs Crossref-resolved on author and title. All 70 NTRS records verified
individually. `_verify.py` at the 0-error 21-warning corpus baseline. Zero style violations after one
prose semicolon was removed. Isolated build succeeding with Part 8 navigation and zero unresolved
anchors.

**Independent re-derivation of all 28 worked values found two errors**, a residence time rounded from
8.3 to 8 milliseconds, and an extrapolation figure whose prose described a different calculation from
the one actually performed. Both corrected.

---

## What Remains

**Lines at 895 and equations at 33 are well below the full-aircraft band and have not been padded.**
References at 252 are just inside. Contemporary coverage is already 38.8 percent of dated, so A304
enters the later passes without a deficit there.

**Publication order dependency is eight deep.** One commit unpushed. Categories remain
`aerospace history engineering`, eight articles deep.
