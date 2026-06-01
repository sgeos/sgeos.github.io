# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-05-31
**Task**: A131-P3 Publish "The Regulatory and Operations Layer for Fixed-Wing UAVs" (sixth and final flagged extension)

---

## Verification

### A131 Published

A131 "The Regulatory and Operations Layer for Fixed-Wing UAVs" published at `_posts/2026-06-14-regulatory_and_operations_layer_for_fixed_wing_uavs.markdown` with front-matter date `2026-06-14 09:00:00 +0000`. 41 references across Reference (33), Related Post (5), and Research (3) categories. Standalone aerospace article and the sixth and final flagged extension beyond the core fixed-wing-UAV arc, with which the series and its extensions are now complete. References A112, A125, A126, A127, and A130 via `post_url`.

### Framing

The article is the layer above the engineering, organized around the principle that the authorization to operate is granted in proportion to the risk an operation poses and the control the operator can demonstrate, so the regulatory burden and the operational discipline both scale with the harm a flight could do. The impact kinetic energy is the physical proxy for that harm, tying the regulatory categories back to the mass and speed the whole series worked in.

### The Pilot's Instruction Honored

The instruction that not everyone is in the USA is honored throughout. The article is jurisdiction-neutral, framed on the International Civil Aviation Organization and the Chicago Convention, naming the United States, European, United Kingdom, Australian, Canadian, and Chinese authorities as examples while stating that every state has its own. The specific thresholds, the common quarter-kilogram and hundred-and-twenty-meter figures, are presented as patterns that differ between states and change from year to year, and the reader is repeatedly directed to the authority that governs the actual flight. The three Research sources are the international bodies rather than United States documents.

### Scope Covered

Regulation is jurisdictional; authorization proportionate to risk with the open, specific, and certified pattern; kinetic energy as the measure of harm; the axes of risk; registration, identification, and competency with the autonomy-and-responsibility tension; airworthiness and the certified end; integrating with other traffic through unmanned traffic management and detect-and-avoid; the operations layer with its safety management system and just culture and independent investigation; contingency and containment with the geofence and flight termination and command-link security; adjacent regimes of spectrum, export control, privacy, property rights, insurance, and noise; the boundary with space where the suborbital carrier hands off to space law; scale and the UAV case; and Out of Scope.

### Reference and Style Verification

Reference integrity confirmed at 41 of 41 anchors defined and used, zero missing, zero unused, zero duplicate definitions, all cited in the body prose and alphabetized within each category. The completeness pass added five Reference anchors (Air Rights, Air Safety, Flight Termination System, Geofence, and Vehicular Automation), all verified HTTP 200 on 2026-05-31. The three international Research sources (the ICAO Unmanned Aviation page, the EASA Civil Drones page, and the JARUS site for the risk assessment) were verified accessible, and the Kármán line URL is percent-encoded. Prose style confirmed: no contractions, no em-dashes or en-dashes in the body, and no prose colons or semicolons, the only semicolon being the console.log debug tag.

### Build Verification

Verified with system Jekyll: the post renders at /aerospace/engineering/uav/2026/06/14/, MathJax is included, the A112 and A125 and A126 and A127 and A130 `post_url` links resolve, all five new reference links resolve to real hrefs, no unresolved link markup remains, and the post appears on the index. The full local bundle build remains broken in this environment; the deploy build runs via the GitHub Actions pipeline after the push.

---

## Release Announcement

New Blog Post: The Regulatory and Operations Layer for Fixed-Wing UAVs

The series has now designed and equipped the aircraft from the airframe outward. This final article is about the permission to fly it and the discipline of operating it, the layer that sits above the engineering and decides whether the aircraft may leave the ground at all. One principle organizes it, that the authorization to operate is granted in proportion to demonstrated control of risk, and regulation is jurisdictional, so the article gives the shape of the layer rather than the law of any one country.

Key takeaways:
- The burden tracks the risk, the open or low-risk band flown without asking, a reasoned case made to the authority in the middle, and the full apparatus of certified aviation at the top, with the impact kinetic energy as the physical measure of harm.
- The numbers differ between states and change every year, so an operator must read the rules of the authority that governs where the aircraft will actually fly, not the rules of somewhere else.
- The heart of the safety case is what happens when things go wrong, the contingency procedures, the geofence that contains a failure, and the flight termination of last resort, and a command link secure enough that the aircraft cannot be hijacked.
- The right to fly is the engineering and the regulation seen as two views of one thing, the case that a flight is safe enough to permit, which completes the arc from a foam-and-glass airframe on a workbench to a regulated and operated system.

You can read the full article here:
https://sgeos.github.io/aerospace/engineering/uav/2026/06/14/regulatory_and_operations_layer_for_fixed_wing_uavs.html

#UAV #FixedWing #Aerospace #Regulation #ICAO #BVLOS #Operations #Airworthiness

---

## Action Items for the Human Pilot

- Confirm the 2026-06-14 publication date is as intended. A131 is the sixth and final flagged extension, one day after A130.
- The fixed-wing-UAV series and its extensions are now complete, the core ten-article arc (A112 through A125) plus six extensions (A126 communications, A127 structures and the flight envelope, A128 aerobatics as costed trajectories, A129 the aerobatic maneuver reference catalog, A130 payload and mission systems, and A131 the regulatory and operations layer). No further extensions are flagged.
- Optionally request the diagrams that recur as the one improvement text cannot supply across these articles, the various V-n, doghouse, energy-height, reentry-corridor, and risk-band figures, which would require image assets.

---

## Notes

- Next available article number: A132.
- 0 release candidates.
- 0 new drafts. A108 through A131 published.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification.
- Published: A79 through A131.
- The fixed-wing-UAV series and its extensions are complete, the core arc A112, A114, A116, A118, A120, A121, A122, A123, A124, A125 plus the extensions A126, A127, A128, A129, A130, A131. No internal research cited; public encyclopedic and authoritative sources only.
- All scratch is confined to project-local `tmp/` per recorded preference. A131 process-file deltas were staged in `tmp/a131/` while drafting and have now been applied directly, so those notes are superseded.
- Blog deploys through GitHub Actions with a lean Jekyll stack; 0 open Dependabot alerts; Keleusma highlighting is live.
