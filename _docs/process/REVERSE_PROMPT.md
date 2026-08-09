# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: Series errata pass, on your instruction to correct A315 and resolve any other known
errors. **Nine of twenty-one articles changed. Nothing published. All still in `_drafts/`.**

---

## A315 Was Worse Than Reported, in Two Directions

The handoff recorded four wrong citations. **There were five, and then a sixth of a different
kind.**

| Anchor | What it actually is |
|---|---|
| `research_boswell_1961` | David Taylor Model Basin, US Dept of the Navy. Spindle torque on a controllable-pitch SHIP propeller |
| `research_hampton_1980` | David W Taylor Naval Ship R&D Center, Ship Performance Dept. Propeller for LSD-41, a dock landing ship |
| `research_hong_2026_2` | Marine propeller cavitation under a hull wake |
| `research_reen_2025` | **Ocean Engineering.** Wing sails for wind-assisted ship propulsion |
| `research_meng_2026` | Maritime autonomous SURFACE SHIPS propulsion reliability |
| `research_wu_2025` | Path tracking of a road car, found later in the series-wide sweep |

`research_meng_2026` was not in the handoff's list. The first two were harvested on
**controllable-pitch propeller**, which is marine terminology for what aircraft call variable
pitch.

### The Correction Was Not a Deletion

**The two Model Basin reports were load-bearing.** Spindle torque is precisely the pitch-change
mechanism load, so they were the only references supporting the claim that the pitch control
system was as complex as it was. That claim is what the article leans on when it says **the pitch
control system is what failed**. Deleting them would have left the causal claim unsupported.

Five genuine aircraft references replace them. Two on dual-rotation propeller aerodynamics from
the period, being Gray and Biermann 1941 and Reynolds, Samonds and Walker 1957, and three on the
pitch-change mechanism itself, being Oppenheimer and Jacques 1951 on turbine-propeller coupling
and Steinetz et al 1986 and Schwartz et al 1986 on actuator and control design. The last two are
labelled in the prose as propfan-era rather than contemporary with the X-18.

**A315 is 418 references to 420.** Three contemporary aerospace papers replaced the three
contemporary marine ones, one of which, May et al 2026 on the impact of failure on a tilt-wing
eVTOL backward transition, is the X-18's own deficiency stated in a modern paper.

---

## The Series-Wide Sweep

**All 3,598 cited DOIs across the twenty-one articles were resolved against Crossref for title and
venue.** Zero failed to resolve. The venue is the discriminator a title cannot supply, and the
title is the discriminator a venue cannot supply when the venue is generalist. Both were needed,
and so was reading, because several survived every pattern.

**Eleven further citations belonged to other fields.**

### Ablation Is the Richest Homonym Family Yet Found

A314 is about an ablative heat shield. **One sentence had collected three ablations from three
other disciplines.**

- Ablation of the **pituitary gland** by implantation of radioactive material
- **Laser ablation** for single-wall **carbon nanotube** production
- Thermal ablation of **malignant cells** by magnetic nanofluid

None was caught by any rule. All three are correct uses of the word. The same article also cited a
study of aviator's clothing thermal protection and one of splashes in underwater blast
experiments. **A314 is 446 references to 441.**

### A317 Was Citing a Retracted Paper

`research_du_2025` is titled **RETRACTED: Thermal radiation image detection and optical motion
capture in athlete physical health monitoring**. It was cited in the reuse and inspection survey.
The retraction notice is in the title itself, which no check looked at.

### The Rest

- **A311** an autonomous **underwater** vehicle cited for effector degradation, and a road-car
  driver take-over study cited for authority allocation
- **A310** an unmanned **surface** vehicle, which is a boat, cited for station-keeping
- **A308** a rectangular **bridge girder** under coupled wind and **wave** action, described in the
  prose as vortex-induced vibration of slender structures
- **A307** a flight-style AUV with bow-wings cited as generic computational lift and drag validation

A308 and A307 were **replaced rather than deleted**, since each was the sole support for its
clause. A308 now cites a circular cylinder in the supercritical regime, which is what a vehicle
standing on a pad in wind actually is.

---

## What Was Deliberately Kept

**A cross-domain citation that the prose flags as cross-domain is honest, not wrong.** Three cases
stay untouched.

- A311 writes **the same mathematics appears well outside aviation** before citing a road vehicle
- A303 writes **the same argument is being had at sea** before citing ocean shipping
- A307 writes **the underwater case is** before citing an AUV

**A308's four Ocean Engineering sloshing papers also stay.** Resonant sloshing in a baffled tank is
shared physics between a liquid natural gas carrier and an Atlas propellant tank, and the article
claims only that the modern literature is largely about where to put the baffles, which is true.

Also kept and worth naming, because they look wrong and are not. A309's eight geodesy papers are
correct, since aiming an intercontinental missile requires the geoid. A303's radiation shielding
is correct for a nuclear aircraft. A305's astronomy is correct, because that is what Aerobee
rockets did. A306's circular-probable-error statistics are correct for a missile.

---

## Three Silent Rendering Defects

**A display equation sharing a line with prose is parsed as inline math inside a paragraph.**
Nothing errors, the build succeeds, and the display-equation regex does not even count it, which is
why these survived every pass.

- A300 line 56, one equation, **113 to 114**
- A313 lines 267 and 520, two equations, **72 to 74**

**The rise in both counts is a correction rather than an addition.** The equations were always in
the text. All three are confirmed rendering as display math in the build output.

A311 also carried a **prose colon** introducing a citation list, which the absolute style rule
prohibits.

---

## The Checker Was the Problem Too

`check.py` carries four hardcoded constants for slug, date, series index and article number, and
A311 and A312 each inherited it by copy with the constants still pointing at the previous article.
**Retyping four constants per article is a defect class, not a task.**

`tmp/errata/check_any.py` replaces it. It derives the article number from the file's own
`<!-- Axxx -->` marker and then validates date and series index against the roster, which is
**strictly stronger** than the hardcoded form because the roster is an independent authority rather
than a value retyped from the thing being checked. It runs over all twenty-one articles at once.

**Writing it produced four false positives before it produced a true one**, and each was a lesson.

- `an AN/ARW-56` is a radio designation, not a doubled word
- Stripping inline math to nothing made the phrase `and u sub e and u sub infinity` read as a
  doubled `and`
- A display block may legitimately span several lines
- The series opener is its own genre row, with no aircraft to compare and a Series Roadmap

The back-reference rule also needed splitting. **It governs within-series links only.** The whole
series is back-dated to 2025 while much of the corpus is 2026, so links to other series are
necessarily forward-dated and that is not a defect. What matters for those is that the target
exists and is not itself dated past today, since `future: false` would exclude it and fail the
build. All seventeen such targets check out.

---

## Verification

- **All 21 articles pass `check_any.py`**, zero failures, zero warnings
- **`_verify.py` at the 0-error 21-warning baseline**, run from the repository root. Not zero
  warnings, which would have meant it checked nothing
- **A 21-article isolated build succeeds.** Every draft staged as a post at its own front-matter
  date, so every in-series `post_url` resolves against the real article rather than a stub. There
  is no stub list to arrive one short
- **All three repaired equations confirmed as display math** in the built HTML
- Ten new URLs swept. Seven plain 200s and **three publisher 403s confirmed through the Crossref
  registry** with matching first authors, titles and venues
- Reference integrity on all nine changed articles, zero undefined and zero orphaned, `research_`
  blocks still sorted

**The bundle is now installed** at `vendor/bundle`, which is gitignored. It was never broken,
merely never installed, and the isolated build needs `BUNDLE_GEMFILE` pointed back at the
repository when the source tree is elsewhere.

---

## Open, and Yours to Decide

**The fourth genre class.** Now six consecutive articles outside all four named classes on two of
three measures. Unchanged by this pass. I will not amend the genre document unprompted.

**A305 length.** The offered cut of roughly 300 lines and 25 equations still stands.

**Marginal citations I did not touch and will not without instruction.** A307 cites marine gravity
anomaly work for gravity-aided inertial navigation, which is the standard dataset and the framing
is accurate. A303 cites nuclear marine reactor shielding for a nuclear aircraft. A305 cites
suborbital biology payloads. A306 cites a marine radar antenna for low-probability-intercept
design. A313 cites a digital-twin bearing-fault paper where the lead-in names digital twins. Each
is defensible as written and each is a judgement call rather than an error.

---

## State

**Committed. Not pushed**, since pushing is authorised only by the publication-review prompt and
this was an errata instruction. Say the word and it goes.

Nothing in the series is published. The publication-order dependency remains twenty-one deep.
