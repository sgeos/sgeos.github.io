# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-05-31
**Task**: A126-P3 Publish "Communications and the Command-and-Control Data Link for Fixed-Wing UAVs" (first extension)

---

## Verification

### A126 Published

A126 "Communications and the Command-and-Control Data Link for Fixed-Wing UAVs" published at `_posts/2026-06-09-communications_and_the_command_and_control_data_link_for_fixed_wing_uavs.markdown` with front-matter date `2026-06-09 09:00:00 +0000`. 34 references across Reference (28), Related Post (3), and Research (3) categories. Standalone aerospace article and the first extension beyond the core fixed-wing-UAV arc. References A116, A121, and A125 via `post_url`.

### Framing

The article is framed around the link budget, the accounting of how much signal power leaves the transmitter, how much is lost on the way, and how much reaches the receiver above the noise, because the margin that accounting leaves is what sets the range, the data rate, and the reliability of every link the aircraft carries. Latency rides alongside as the companion constraint that decides what can be controlled over the link at all.

### Scope Covered

The link budget (Friis, free-space path loss, SNR, Shannon, Fresnel, ISM bands, the frequency range-versus-rate trade, near-ground multipath and the two-ray ground reflection, the regulatory cap on effective radiated power); the radio horizon; the moving aircraft (airframe shadowing, radiation-pattern nulls and polarization, antenna diversity, a tracking ground antenna); the three streams; radio control with a handheld transmitter; computer-controlled transmission; beyond line of sight; latency and why the fast loops are aboard; security and jamming; lost link; scale and the UAV case; a worked example; and Out of Scope.

### The Pilot's Explicit Requirement

The required coverage of RC control via both a consumer handheld controller and a computer-controlled transmitter is met in two dedicated sections. "Radio Control with a Handheld Transmitter" covers the consumer handset, 2.4 GHz FHSS, ExpressLRS, the CRSF/SBUS handoff, the control-link packet rate, FPV, and the failsafe, the manual path. "Computer-Controlled Transmission" covers MAVLink, SiK/RFD900 telemetry radios, the ground control station, and a companion computer over cellular, sending waypoints and missions rather than stick inputs, the autonomous path. The two are framed as coexisting, the data link for the mission and the handheld as the human's fallback.

### Series Position

A126 is the first extension beyond the core ten-article fixed-wing-UAV arc, which closed with the A125 capstone. Remaining unflagged extensions, if desired later, are structures and the flight envelope, payload and mission systems, and the regulatory and operations layer.

### Reference and Style Verification

Reference integrity confirmed at 34 of 34 anchors defined and used, zero missing and zero unused, alphabetized within each category. The completeness pass added six Reference anchors (Advanced Video Coding, Antenna Diversity, Equivalent Isotropically Radiated Power, Multipath Propagation, Radiation Pattern, and the Two-Ray Ground-Reflection Model), all verified HTTP 200 on 2026-05-31. The MDPI secure-drone-communication survey returns 403 to curl under the documented anti-bot pattern and is retained as a valid peer-reviewed source. Prose style confirmed: no contractions, no em-dashes or en-dashes in the body, and no prose colons or semicolons, the only semicolon being the console.log debug tag.

### Build Verification

Verified with system Jekyll: the post renders at /aerospace/engineering/uav/2026/06/09/, MathJax is included, the A116 and A121 and A125 `post_url` links resolve, all six new reference links resolve to real hrefs, no unresolved `[ref_...]` markup remains, and the post appears on the index. The full local bundle build remains broken in this environment; the deploy build runs via the GitHub Actions pipeline after the push.

---

## Release Announcement

New Blog Post: Communications and the Command-and-Control Data Link for Fixed-Wing UAVs

The guidance and automatic-landing capstone put the autopilot aboard the aircraft, able to fly a mission on its own. This first extension takes up the link that connects that aircraft to the people on the ground, the command-and-control data link that carries the operator's intent up and the aircraft's state and its sensors down. One quantity organizes the subject, the link budget, and a second rides alongside, the latency that decides what can be controlled over the link at all.

Key takeaways:
- The link budget sets whether a message arrives, the frequency trades range against data rate, the horizon bounds the line-of-sight reach, and near the ground multipath and the regulated power cap make the clean budget optimistic.
- A handheld transmitter flies the aircraft manually within sight while a computer link carries waypoints and missions to the autopilot, the manual and the autonomous paths coexisting on a serious aircraft.
- The fast loops stay aboard because no link is quick enough to hold them, which is why a satellite relay reaches beyond the horizon only at the cost of speed.
- A lost link falls into a safe, preset behavior rather than a runaway, so the reliability the link cannot guarantee is supplied by the autonomy instead.

You can read the full article here:
https://sgeos.github.io/aerospace/engineering/uav/2026/06/09/communications_and_the_command_and_control_data_link_for_fixed_wing_uavs.html

#UAV #FixedWing #Aerospace #DataLink #C2 #MAVLink #ExpressLRS #LinkBudget

---

## Action Items for the Human Pilot

- Confirm the 2026-06-09 publication date is as intended. A126 is the first extension beyond the core arc, one day after the A125 capstone.
- Optionally request schematic diagrams (the link-budget waterfall, the three-stream architecture, the handheld-versus-computer link topology, and the line-of-sight-versus-satellite latency comparison), which are the one improvement that cannot be added in text and would require image assets.
- Possible further unflagged extensions, if desired later, are structures and the flight envelope, payload and mission systems, and the regulatory and operations layer.

---

## Notes

- Next available article number: A127.
- 0 release candidates.
- 0 new drafts. A108 through A126 published.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification.
- Published: A79 through A126.
- The core fixed-wing-UAV arc is complete (A112, A114, A116, A118, A120, A121, A122, A123, A124, A125); A126 is the first extension beyond it. No internal research cited; public encyclopedic and authoritative sources only.
- All scratch is confined to project-local `tmp/` per recorded preference. A126 process-file deltas were staged in `tmp/a126/` while drafting and have now been applied directly, so those notes are superseded.
- Blog deploys through GitHub Actions with a lean Jekyll stack; 0 open Dependabot alerts; Keleusma highlighting is live.
