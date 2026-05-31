# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-05-31
**Task**: A128-P3 Publish "Aerobatics as Costed Trajectories for Fixed-Wing UAVs" (third extension, synthesis capstone)

---

## Verification

### A128 Published

A128 "Aerobatics as Costed Trajectories for Fixed-Wing UAVs" published at `_posts/2026-06-11-aerobatics_as_costed_trajectories_for_fixed_wing_uavs.markdown` with front-matter date `2026-06-11 09:00:00 +0000`. 42 references across Book (1), Reference (33), Related Post (6), and Research (2) categories. Standalone aerospace article and the third extension beyond the core fixed-wing-UAV arc, the synthesis capstone of the extension set. References A120, A122, A123, A124, A125, and A127 via `post_url`.

### Framing

The article is written for the UAV operator and the autonomy and explicitly not for the human pilot, because a maneuver is a different object once no one is aboard, a commanded spatiotemporal trajectory rather than a learned skill. It is organized around the energy state and the specific excess power that changes it, every maneuver a transaction in potential, kinetic, and propulsive energy carrying three costs, an energetic one, a structural one, and a thermal one, whose dominant term migrates with the speed regime until at reentry all three bind at once.

### Scope Covered

A maneuver as a trajectory; the energy state and specific excess power; the three costs and the control-authority-and-bandwidth feasibility gate; the kinematic primitives and the maneuverability diagram; a scored catalogue of ten maneuvers; the footprint in space and time; the subsonic, transonic and supersonic, and hypersonic regimes; spaceplane maneuvering during reentry and after the thermal wall; scale and the UAV case; a worked example; and Out of Scope.

### The Pilot's Framing Honored

The two rounds of pre-draft framing were all carried through. The article is for the unmanned case and discards human pedagogy and physiology. It is math-heavy on the backbone of energy-maneuverability theory and turn kinematics and honest where no closed form exists, the post-stall spin and cobra flagged rather than faked. The catalogue is a representative scored set of ten rather than an exhaustive enumeration. The thermal cost is made first-class through an explicit subsonic, supersonic, and hypersonic regime structure, inert at low speed and dominant at high. The hypothetical spaceplane case is split into maneuvering during reentry, a survival corridor of bank reversals and angle-of-attack modulation with the control authority migrating from reaction control thrusters to aerodynamic surfaces, and maneuvering after the thermal wall, the terminal-area energy management of an unpowered glider. The word aerobatics is extended to mean commanded maneuvering, with an explicit statement that figure flying does not survive the hypersonic and reentry regimes. Orbital mechanics, the deorbit, and the entry guidance derivation are out of scope, the boundary the stability-and-control article drew.

### Reference and Style Verification

Reference integrity confirmed at 42 of 42 anchors defined and used, zero missing and zero unused, alphabetized within each category. The completeness pass added four Reference anchors (Inertia Coupling, Maneuverability, Precession, and Separation in Aeronautics), all verified HTTP 200 on 2026-05-31. The Book source (Vinh, Flight Mechanics of High-Performance Aircraft, whose final chapter covers hypervelocity reentry) and the two NASA Research sources (Space Shuttle Entry Terminal Area Energy Management, TM 104744, and Shuttle Entry Guidance Revisited) were verified accessible. Prose style confirmed: no contractions, no em-dashes or en-dashes in the body, and no prose colons or semicolons, the only semicolon being the console.log debug tag.

### Build Verification

Verified with system Jekyll: the post renders at /aerospace/engineering/uav/2026/06/11/, MathJax is included, the catalogue table renders, the A120 and A122 and A123 and A124 and A125 and A127 `post_url` links resolve, all four new reference links resolve to real hrefs, no unresolved link markup remains, and the post appears on the index. The full local bundle build remains broken in this environment; the deploy build runs via the GitHub Actions pipeline after the push.

---

## Release Announcement

New Blog Post: Aerobatics as Costed Trajectories for Fixed-Wing UAVs

The structures article drew the flight envelope. This one is about the paths flown inside it, and it is written for the people who command unmanned aircraft and the autonomy that flies them, not for the human pilot, because a maneuver is a different object once no one is aboard. It is a commanded spatiotemporal trajectory, and the article prices it in energy, in structure, and in heat.

Key takeaways:
- A maneuver is a path through the energy state, and the specific excess power says which way the path can go, the difference between an instantaneous figure that spends stored energy and a sustained one that can be held only where the excess power is not negative.
- The three costs are paid together, a tighter turn raising the load factor and the induced drag at once, and at high speed the heating too, while a fourth gate, the control authority and bandwidth, decides whether the figure can be commanded at all.
- The catalogue of figures is richest in the slow and light regime, thins through the supersonic regime where wave drag makes every turn an energy decision, and collapses in the hypersonic regime to the shaping of a descent.
- At reentry the only maneuvering left is a bank reversal inside a corridor where the energetic, structural, and thermal costs all bind at once, and the unmanned aircraft inherits the whole range without the human ceiling, so the airframe and the energy and the heat, not a person, decide which trajectories may be flown.

You can read the full article here:
https://sgeos.github.io/aerospace/engineering/uav/2026/06/11/aerobatics_as_costed_trajectories_for_fixed_wing_uavs.html

#UAV #FixedWing #Aerospace #Aerobatics #EnergyManeuverability #Hypersonic #Spaceplane #Reentry

---

## Action Items for the Human Pilot

- Confirm the 2026-06-11 publication date is as intended. A128 is the third extension beyond the core arc and the synthesis capstone of the extension set, one day after A127.
- Optionally request schematic diagrams (the doghouse maneuverability plot, the energy-height-versus-airspeed diagram with maneuver paths drawn on it, the reentry corridor, and a per-regime maneuver-survival figure), which are the one improvement that cannot be added in text and would require image assets.
- Possible further unflagged extensions, if desired later, are payload and mission systems, and the regulatory and operations layer.

---

## Notes

- Next available article number: A129.
- 0 release candidates.
- 0 new drafts. A108 through A128 published.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification.
- Published: A79 through A128.
- The core fixed-wing-UAV arc is complete (A112, A114, A116, A118, A120, A121, A122, A123, A124, A125); A126 (communications), A127 (structures and the flight envelope), and A128 (aerobatics as costed trajectories) are the first three extensions beyond it, A128 being the synthesis capstone of the extension set. No internal research cited; public encyclopedic and authoritative sources only.
- All scratch is confined to project-local `tmp/` per recorded preference. A128 process-file deltas were staged in `tmp/a128/` while drafting and have now been applied directly, so those notes are superseded.
- Blog deploys through GitHub Actions with a lean Jekyll stack; 0 open Dependabot alerts; Keleusma highlighting is live.
