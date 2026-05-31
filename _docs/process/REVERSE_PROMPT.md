# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-05-31
**Task**: A125-P3 Publish "Guidance, Navigation, and Automatic Landing for Fixed-Wing UAVs" (capstone)

---

## Verification

### A125 Published

A125 "Guidance, Navigation, and Automatic Landing for Fixed-Wing UAVs" published at `_posts/2026-06-08-guidance_navigation_and_automatic_landing_for_fixed_wing_uavs.markdown` with front-matter date `2026-06-08 09:00:00 +0000`. 333 lines. 29 references across Reference (21), Related Post (4), and Research (4) categories. Standalone aerospace analytical article and the capstone of the fixed-wing-UAV set. References A114, A116, A123, and A124 via `post_url`.

### Framing

The article is framed around a single idea, that every loop drives to zero the error between the state the aircraft is commanded to hold and the state it is estimated to be in, so navigation supplies the estimate, guidance supplies the command, and control nulls the difference, the loops nested by bandwidth with the automatic landing as the tightest. The total energy control system is presented as the real-time version of the energy budget the whole series has tracked.

### Scope Covered

The nested loops with their bandwidth separation and digital sample rates; navigation by GNSS and INS fused in a Kalman filter, with air data, RTK, initialization, and the GNSS-denied vision fallback; guidance by waypoints and the cross-track look-ahead law; wind and the ground track; energy management by the total energy control system; the approach and automatic landing with the automatic-takeoff bookend; the degraded modes when a sensor or link fails; the small-UAV autopilot and the autonomy spectrum; and a worked example.

### Series Completion

A125 is the capstone. The fixed-wing-UAV set is now a complete ten-article arc: A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion, A121 electric energy systems, A122 stability and control, A123 dynamic stability and control, A124 landing gear and touchdown, and A125 guidance, navigation, and automatic landing. The conclusion ties them together as one energy budget and one error driven to zero. No further sequels are flagged; any continuation (the communications and command-and-control data link, structures and the flight envelope, payload and mission systems, or the regulatory and operations layer) would be an unflagged extension.

### Reference and Style Verification

Reference integrity confirmed at 29 of 29 anchors defined and used, zero missing and zero unused, alphabetized within each category. External URLs verified, with all 21 Wikipedia URLs and all four research sources (NASA Total Energy Control System flight test, the University of Washington waypoint-guidance paper, and the ArduPilot automatic-landing and automatic-takeoff documentation) accessible. Prose style confirmed: no contractions, no em-dashes or en-dashes in the body, and no prose colons or semicolons, the only semicolon being the console.log debug tag.

### Build Verification

Verified with system Jekyll: the post renders at /aerospace/engineering/uav/2026/06/08/, MathJax is included, the A114 and A116 and A123 and A124 `post_url` links resolve, all 29 reference links render, and the post appears on the index. The full local bundle build remains broken in this environment; the deploy build runs via the GitHub Actions pipeline after the push.

---

## Release Announcement

New Blog Post: Guidance, Navigation, and Automatic Landing for Fixed-Wing UAVs

The dynamics article sized the inner loop that holds an attitude. This capstone takes up the outer loop on top of it, the guidance, navigation, and control that decides where the aircraft should go, works out where it actually is, and closes the gap, all the way to an automatic landing. One idea runs through it, that every loop drives an error to zero, the gap between where the aircraft is estimated to be and where it is commanded to be.

Key takeaways:
- Navigation builds an estimate by fusing a drifting inertial solution with a bounded satellite fix, guidance turns a route into a commanded heading and a total-energy target, and control flies it, the loops nested by speed.
- The total energy control system manages the same energy budget the whole series tracked, the throttle setting total energy and the elevator distributing it between speed and height.
- The automatic landing is the tightest loop, where the tolerated error shrinks to zero just as the ground arrives, and the lateral accuracy at the threshold is the dispersion the runway width must hold.
- The whole stack now runs on an open board no larger than a hand, which is why an autonomous fixed-wing UAV is ordinary rather than exotic, and this completes the ten-article series from foam-and-glass airframe to self-landing aircraft.

You can read the full article here:
https://sgeos.github.io/aerospace/engineering/uav/2026/06/08/guidance_navigation_and_automatic_landing_for_fixed_wing_uavs.html

#UAV #FixedWing #Aerospace #GNC #Autopilot #AutomaticLanding #Navigation #ArduPilot

---

## Action Items for the Human Pilot

- Confirm the 2026-06-08 publication date is as intended. A125 is the capstone, one day after A124, and completes the set.
- Optionally request schematic diagrams (the nested-loop block diagram, the GNSS-and-INS fusion picture, the cross-track look-ahead geometry, and the glideslope-and-flare profile), which are the one improvement that cannot be added in text and would require image assets.
- The fixed-wing-UAV series is complete. Possible unflagged extensions, if desired later, are the communications and command-and-control data link, structures and the flight envelope, payload and mission systems, and the regulatory and operations layer.

---

## Notes

- Next available article number: A126.
- 0 release candidates.
- 0 new drafts. A108 through A125 published.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification.
- Published: A79 through A125.
- The fixed-wing-UAV set is complete (A112, A114, A116, A118, A120, A121, A122, A123, A124, A125). No internal research cited; public encyclopedic and authoritative sources only.
- All scratch is confined to project-local `tmp/` per recorded preference. A125 process-file deltas were staged in `tmp/a125/` while drafting and have now been applied directly, so those notes are superseded.
- Blog deploys through GitHub Actions with a lean Jekyll stack; 0 open Dependabot alerts; Keleusma highlighting is live.
