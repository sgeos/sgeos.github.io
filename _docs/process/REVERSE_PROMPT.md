# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-06-15
**Task**: Publish A149 "Operator Training and Certification for a Search and Rescue Drone Program" (fifth in the SAR drone series) and draft A150 "Sensor and Payload Selection for Search and Rescue Drones" (sixth in the SAR drone series, the sensor-investment companion to A146)

---

## Verification

### A149 Published

A149 "Operator Training and Certification for a Search and Rescue Drone Program" published at `_posts/2026-05-19-operator_training_and_certification_for_search_and_rescue_drone_programs.markdown` with front-matter date `2026-05-19 09:00:00 +0000`. 56 references across Reference (52) and Related Post (4) categories. Fifth article in the SAR drone series, the operator-investment companion to A146. Disaggregates the operator training cost A146 mentioned in passing into a five-layer training stack covering the FAA Part 107 regulatory minimum, manufacturer training, SAR operational training, NIMS and ICS integration, and specialised operations. Per-layer cost and timeline, recurrency requirements, crew roles and training pathways, operator pool construction, training budget by programme tier mapped to A146.

### A150 Drafted

A150 "Sensor and Payload Selection for Search and Rescue Drones" drafted at `_drafts/sensor_and_payload_selection_for_search_and_rescue_drones.markdown` with front-matter date `2026-05-20 09:00:00 +0000`. 49 references across Reference (44) and Related Post (5) categories. 2,989 lines. Sixth article in the SAR drone series, the sensor-investment companion to A146. Treats the sensor payload as the principal mission-capability decision the programme manager makes after the airframe and the operator training. Covers six sensor categories with per-class detection physics, performance metrics, resolution tiers, and vendor landscape. Payload integration covers mass and endurance trade, power budget, data bandwidth, gimbal mount standards, and MISB KLV motion imagery metadata. Sensor mix by mission profile scorecard table covering eight mission profiles. Sensor budget by programme tier table mapping to A146 tiers.

### Research Agent Pass

Research agent verified vendor specifications and standards references and applied factual corrections to A150. Critical corrections include the Brigade Electronics drone loudspeaker claim removed and replaced with the DJI Zenmuse V1 and Sky Speaker-I from Yangda since Brigade has no public drone loudspeaker product, the SkyShout manufacturer attribution removed since it could not be verified, the Carnegie Mellon whistle detection attribution softened with the DroneAudioset benchmark cited as the specific research anchor, the 12 volt and 28 volt drone payload power bus standards claim reframed since the drone industry has not adopted MIL-STD-704 or MIL-STD-1275 as a universal payload bus, the ASTM F38 universal payload mount standard claim reframed since F38 has not standardised a universal payload mount, and URL corrections for FLIR Boson Plus and Hadron 640R OEM pages, Workswell WIRIS Pro, Freefly MoVI XL, YellowScan compare-products, Sierra-Olympia airborne cameras, DJI Payload SDK developer portal, and Sony Starvis Framos overview.

### Reference and Style Verification

Reference integrity confirmed at 49 of 49 anchors defined and used, zero missing, zero unused, zero duplicate definitions. Prose style confirmed for both A149 and A150: no contractions, no em-dashes or en-dashes in the body, and no prose colons or semicolons outside the YAML front matter, the timestamps, and the console.log debug tag. Anchor prefixes consistent across the series (ref_, related_post_).

### Build Verification

The local bundle build remains broken in this environment; the deploy build runs via the GitHub Actions pipeline after the push. The system Jekyll-based rendering of the prior series articles (A145 through A148) confirmed under `future: true` in `_config.yml`, which permits the backdated and forward-dated SAR series to render in the deploy build.

---

## Release Announcement

New Blog Post: Operator Training and Certification for a Search and Rescue Drone Program

The five-layer training stack that a working SAR drone programme requires, from the FAA Part 107 regulatory minimum to the specialised operations training that particular missions impose. Disaggregates the operator training cost the previous article in the series mentioned in passing into the detail that a programme manager planning the multi-year investment needs.

Key takeaways:
- Operator training is the single largest cost the programme bears over its lifetime, dominant over both the platform acquisition and the maintenance programme.
- The training stack has five layers (FAA Part 107 regulatory minimum, manufacturer training, SAR operational training, NIMS and ICS integration, and specialised operations) each with distinct currency, timeline, and cost characteristics.
- The crew roles (Visual Observer, Sensor Operator, Remote Pilot in Command, Search Team Coordinator, UAS Team Leader) hold different subsets of the training stack, which permits the operator pool to be built progressively as new operators enter the lighter roles while completing the longer Remote Pilot in Command training.
- The training budget by programme size maps to the five-tier framework that the previous article in the series established, with the operator training typically equalling or exceeding the platform acquisition cost over a five-year lifecycle.

You can read the full article here:
https://sgeos.github.io/aerospace/engineering/uav/search-and-rescue/training-and-certification/2026/05/19/operator_training_and_certification_for_search_and_rescue_drone_programs.html

#SearchAndRescue #SAR #Drones #UAS #PublicSafety #Training #NIMS

---

## Action Items for the Human Pilot

- Review A149 (published) for tone, accuracy, and completeness.
- Review A150 draft (not yet published) for tone, accuracy, and completeness. Pay particular attention to the sensor budget tables, the sensor mix by mission profile table, and the six sensor category sections.
- Confirm publication date for A150 (currently 2026-05-20).
- Confirm whether the SAR drone series should continue with A151 (maintenance and lifecycle management) and A152 (data management and chain of custody) as the conclusion of A150 forecasts, or pivot to a different topic.

---

## Notes

- Next available article number: A151.
- 1 release candidate (A150).
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification.
- Published through A149.
- The SAR drone series is ACTIVE in the aerospace/engineering/uav/search-and-rescue category, with A145 (physics), A146 (buyer's framework), A147 (R&D), A148 (geographic setting), and A149 (operator training) published, and A150 (sensor and payload selection) drafted. The series forecasts A151 (maintenance and lifecycle management) and A152 (data management and chain of custody) as the remaining articles.
- All scratch is confined to project-local `tmp/` per recorded preference.
- Blog deploys through GitHub Actions with a lean Jekyll stack; `future: true` is enabled in `_config.yml` to permit backdated and forward-dated posts in the SAR series to render in the deploy build.
