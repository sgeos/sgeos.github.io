# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-05-31
**Task**: A114-P4 Publish "Runway Sizing for Fixed-Wing UAVs"

---

## Verification

### A114 Published

A114 "Runway Sizing for Fixed-Wing UAVs" published at `_posts/2026-05-31-runway_sizing_for_fixed_wing_uavs.markdown` with front-matter date `2026-05-31 09:00:00 +0000`. 548 lines. 28 references across Reference (21), Related Post (1), and Research (6) categories. Standalone aerospace analytical article. References A112 (Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass) via `post_url`.

### Scope Covered

The squared-speed master variable and explicit square-cube size-scaling; the level ground roll; paved versus dirt; inclined and ski-jump runways; wind, crosswind, and landing-gear ground handling; orientation with an Earth-rotation dismissal; density altitude; obstacle clearance, margins, and an in-scope abort and stopping-margin note; the landing roll and ground effect; width and the lateral dimension (touchdown dispersion and guidance lateral error); full-runway versus single-phase operation anchored to real UAVs (ScanEagle, RQ-7 Shadow, MQ-9 Reaper); planform and airframe implications; a worked numeric example; and lighting, reflectors, and markings (optional versus required), with an explicit Out of Scope section.

### Reference and Style Verification

Reference integrity confirmed at 28 of 28 anchors defined and used, zero missing and zero unused. External URLs verified, with publisher anti-bot 403 cases avoided in favor of accessible sources. Prose style confirmed: no contractions, no em-dashes or en-dashes, and no prose colons or semicolons, the only semicolons being the console.log debug tag and LaTeX spacing. The worked-example arithmetic was re-checked.

### Build Verification

Verified with system Jekyll: the post renders at /aerospace/engineering/uav/2026/05/31/, MathJax is included, the A112 `post_url` resolves, and all 28 reference links render. The full local bundle build remains broken in this environment (gem environment issue documented in earlier history); the deploy build runs via the GitHub Actions pipeline after the push.

---

## Release Announcement

New Blog Post: Runway Sizing for Fixed-Wing UAVs

A fixed-wing unmanned aerial vehicle needs ground to accelerate to flying speed and ground to slow back down, and the question of how much ground has a surprisingly structured answer. One variable dominates, the speed the aircraft must reach, because the distance to reach a speed grows with the square of that speed. Slope, surface, wind, air density, planform, and even raw size all act by changing that speed or the acceleration available to reach it.

Key takeaways:
- Wing loading is the single best proxy for runway length within a configuration, because for a given airfoil and air it sets the stall speed, and the stall speed squared sets the runway.
- Size enters through the square-cube law. Scaling an airframe up while keeping its construction roughly doubles wing loading per doubling of size, so larger aircraft want longer runways as a consequence of the same proportionality.
- Many UAVs use a runway for only one phase. Catapults, nets, parachutes, and ramps let the field be sized for the phase that remains on the ground, as ScanEagle, the RQ-7 Shadow, and the MQ-9 Reaper illustrate across the spectrum.
- Width, lighting, and reflectors are sizing-stage decisions as well, and lighting is sometimes mandatory rather than optional.

You can read the full article here:
https://sgeos.github.io/aerospace/engineering/uav/2026/05/31/runway_sizing_for_fixed_wing_uavs.html

#UAV #FixedWing #Aerospace #Runway #Aerodynamics #STOL #DroneOps #FlightTest

---

## Action Items for the Human Pilot

- Confirm the 2026-05-31 publication date is as intended. A114 publishes after A113's backdated 2026-05-23 entry.
- Optionally request schematic diagrams (force balance on the roll, slope and ski-jump geometry, the crosswind triangle, width versus length). These are the one improvement that cannot be added in text and would require image assets.
- Optionally repair the local gem environment so future drafts can be previewed with a full bundle build rather than system Jekyll.

---

## Notes

- Next available article number: A115.
- 0 release candidates.
- 0 recent pre-release candidates. A108 through A114 published.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification.
- Published: A79 through A114.
- Blog deploys through GitHub Actions with a lean Jekyll stack; 0 open Dependabot alerts; Keleusma highlighting is live.
- All scratch is confined to project-local `tmp/` per recorded preference.
- A114 scratch and earlier process-file deltas were staged under `tmp/a114/` while the A113 session held the live process files. Those files are now synced directly, so the `tmp/a114/` notes are superseded.
