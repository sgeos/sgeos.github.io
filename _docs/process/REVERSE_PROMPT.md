# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A322 primary-reference review, the third of four passes. Committed. **Not pushed.** **Not
published.** All twenty-six articles in the series remain in `_drafts/`.

**References 2,348 to 2,852, and PRIMARY CITATIONS FROM 54.8 TO 61.8 PERCENT**, with period sources
dated 1975 or earlier rising from 639 to 977. Article 4,367 to 5,277 lines and 15,890 to 18,990 words.
Equations held at 43 and measured before and after.

---

## The Keystone Is Thin on Primaries for the Fourth Article Running, and the Cause Has Changed

**This is the same headline as the last three articles and a different defect underneath it, which is
why it is worth reporting carefully rather than filing under the existing rule.**

Autorotation carries **65 citations and 21 primaries, or 32 percent**, against an article average of
62. In A319, A320 and A321 the keystone cluster was thin **on count**, and the cause every time was
that the pattern had been written in the wrong decade's vocabulary. Broadening fixed it.

**Autorotation is not that case.** It is a word the 1930s used and the 2020s still use. The query
matched happily in both directions, and **the larger and better-indexed modern computational literature
simply crowded the period out**. The query succeeded and the balance failed.

**Two further harvests aimed squarely at the period reports moved it from 16 primaries to 21 and then
stopped.** Those harvests named the period work rather than describing the topic, querying the steady
vertical descent in single-rotor autorotation, the transition from hovering into autorotative descent,
the power-off flare-up tests of a model rotor, and the empirical relation between induced velocity,
thrust and rate of descent. They found the classics and they found no more of them.

**The pool itself is 31 percent primary on this topic and every primary in it is cited.** The only
autorotation records left uncited are three modern wind-turbine papers, two of them Darrieus machines
the filter excludes anyway. **The cited fraction of 32 percent matches the pool's 31 percent almost
exactly, which is the proof that this is supply and not selection.**

**The article reports it rather than padding toward a band.**

---

## What the Harvest Did Fix

| Topic | Primary before | Primary after |
|---|---|---|
| Bluff-body drag coefficient | 6 of 20, 30 percent | 44 of 61, 72 percent |
| Descent states and the vortex ring | 3 of 24, 12 percent | 24 of 48, 50 percent |
| The autogiro and the gyroplane | 41 of 53, 77 percent | 65 of 77, 84 percent |
| Glide performance and reach | 7 cited | 12 of 14, 86 percent |
| Rotor kinetic energy and inertia | 0 of 1 | 5 of 6, 83 percent |

Three harvests added 185 NTRS records, 225 Defense Technical Information Center records and 381 journal
records, taking the master pool from 3,511 to 4,256.

---

## Five Assertions Had No Citation Within Four Hundred Characters

**The worst of them was the 1.8 constant, which is the number the entire article turns on.** It now
rests explicitly on the mid-century measurement literature that produced it.

The others were the canopy drag coefficient of 0.75 and its inflated geometry, the assumed glide ratio
of 4, the statement that a helicopter Lock number sits between eight and ten, and the blade loading
coefficient limit near 0.10. **All five are quantitative claims the prose relies on, and this is the
defect the genre document's equation and reference bands exist to catch.**

---

## Two Topics Are Thin and Only One of Them Is Real

**This distinction cost some effort and is worth keeping.**

**Rotor spin-up and prerotation stands at three records** after a harvest aimed at it using period
vocabulary including prerotation, rotor starting and starting torque. **That is a genuine archive
limit**, and it is the stated reason the spin-up section reasons from energy rather than from
measurement.

**Stored rotor energy appears to stand at one record and does not really.** The relevant work exists
and is cited, but it sits inside the autorotation and blade-motion literature rather than beside it,
because a paper on autorotative landing is a paper about spending exactly that energy. **A thin heading
is not the same thing as a thin subject**, and the error is easy to make in the direction of claiming a
gap that is not there.

---

## Contamination Found by Reading, and One Self-Inflicted Regex Bug

Thirteen records were read and dropped, taking the rejection list from 507 to 533 entries, keyed by URL
as well as by anchor. They are pump and fan rotors, a reactor coolant pump, a nuclear ramjet, a lunar
landing-site study, and three physiological papers including **the effect of gentling on the heart rate
and flight distance of sheep**, which reached the pool through the words flight and distance.

**One record was flagged and kept.** A 1964 study of space-cabin landing impact vectors on human
physiology is squarely the body-tolerance topic, and so is a 1962 evaluation of a light autogyro for
the aerial treatment of crops, which the agricultural filter would have taken.

**Two scanning patterns of my own reported false contamination and both were my bug, not the pool's.**
One matched `EVA` inside `EVALUATION` and reported 184 records; the real count was four. The other
matched `train` inside `training` and reported 96.

**The second bug exposed something real.** Checking why so many training papers were present found that
**twenty-five of the seventy-two records in the training cluster had no aviation word in the title at
all** — Army battalions, United Nations peacekeeping, Ada software engineering education, vocational
programmes and manual-handling ergonomics. **"Training requirements" is a Defense Technical Information
Center term of art for personnel documents of any kind**, and this article's own harvest query for pilot
training requirements pulled in the entire genre. The cluster pattern now requires the training word to
sit beside an aviation one, and the cluster is at 64 records with none lacking an aviation term.

Eighteen records were dropped by reading in total across the pass, taking the rejection list from 507 to
543 entries.

---

## Verification

**Numerical.** 71 independent checks passing unchanged, none importing the calculation, every value
required to appear in the draft text.

**Build.** Twenty-six article isolated build succeeding, all 43 equations rendering as display math,
zero mangled escapes, zero unbalanced braces, zero duplicated equations, Part 26 of 72.

**Corpus.** `_verify.py` at 0 errors and 21 warnings. Style and integrity check clean across all
twenty-six articles.

**URLs.** 2,867 external links swept against a superset of the final set, with **2,372 of 2,372 DOIs
confirmed registered in the Crossref registry and zero unregistered**, and 494 of 495 non-DOI links at
200. The single exception is the National Museum of the United States Air Force fact sheet, a `.mil`
address that refuses automated connections and was verified independently by search. **Reading the
2,372 printed titles is what found the training-genre contamination.**

---

## State

**A322 has three of four passes complete. Committed, not pushed, not published.**

**Expected next is the publication review**, which is also the pass that authorises a push.

**Still open and unchanged.** The fourth genre class, now **thirteen** consecutive articles. The A305
length offer.
