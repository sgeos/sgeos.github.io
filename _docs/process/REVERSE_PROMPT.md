# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-05-31
**Task**: A118-P4 Publish "Propulsion and Power Sizing for Small Fixed-Wing UAVs"

---

## Verification

### A118 Published

A118 "Propulsion and Power Sizing for Small Fixed-Wing UAVs" published at `_posts/2026-06-02-propulsion_and_power_sizing_for_fixed_wing_uavs.markdown` with front-matter date `2026-06-02 09:00:00 +0000`. 445 lines. 36 references across Reference (31), Related Post (3), and Research (2) categories. Standalone aerospace analytical article and the fourth in the fixed-wing-UAV set. References A112, A114, and A116 via `post_url`.

### Scope Covered

The power-required master variable, where power is thrust times speed and thrust in level flight is drag, so the power to fly is the weight times the speed divided by the lift-to-drag ratio; the drag polar and lift-to-drag ratio; propellers and efficiency via momentum theory, static thrust, and advance ratio, including the electric ducted fan; the thrust-to-weight and launch and climb case that usually sizes the powertrain; electric and combustion propulsion with the battery wall and the heavy-fuel logistics note; altitude and available power; endurance and range with reserves; a brief solar, hybrid, and fuel-cell note; jets and regimes beyond the propeller; a worked example on the 25 kg series aircraft; and a declared Out of Scope.

### Correctness Note

A completeness pass corrected an inverted attribution: for a propeller aircraft, maximum endurance is at the minimum-power speed and maximum range is at the best lift-to-drag speed, with the jet's mirror-image pairing noted. This was the one item that made the draft not-yet-publication-ready, and it is fixed.

### Date and Series

The article is dated 2026-06-02, one day after its A116 companion, completing the fixed-wing-UAV set in publication-date order (A112 on 2026-05-30, A114 on 2026-05-31, A116 on 2026-06-01, A118 on 2026-06-02). Article number A118 fills the gap below A119 (2026-05-22) in number while sitting later in publication date, consistent with POST_STRUCTURE.md's out-of-order-numbering policy.

### Reference and Style Verification

Reference integrity confirmed at 36 of 36 anchors defined and used, zero missing and zero unused, alphabetized within each category. External URLs verified, with the MDPI Aerospace propulsion-sizing paper retained as a documented 403-to-curl source. Prose style confirmed: no contractions, no em-dashes or en-dashes, and no prose colons or semicolons, the only semicolon being the console.log debug tag. The worked-example arithmetic was re-checked.

### Build Verification

Verified with system Jekyll: the post renders at /aerospace/engineering/uav/2026/06/02/, MathJax is included, the A112 and A114 and A116 `post_url` links resolve, all 36 reference links render, and the post appears on the index. The full local bundle build remains broken in this environment; the deploy build runs via the GitHub Actions pipeline after the push.

---

## Release Announcement

New Blog Post: Propulsion and Power Sizing for Small Fixed-Wing UAVs

The companion articles sized the runway, the launch and recovery, and the airframe while taking the propulsion as given. This one sizes the propulsion. One quantity dominates, the power required to fly, because power is thrust times speed and thrust in steady flight is drag, so the whole problem flows from the drag the aircraft must overcome and the speed it must overcome it at.

Key takeaways:
- The power required to fly is the weight times the speed divided by the lift-to-drag ratio, and a propulsion system must supply that cruise power, the surplus that climb and launch demand, and the energy that endurance needs.
- The launch and climb case, not cruise, usually sizes the powertrain, because the static thrust for a sensible thrust-to-weight ratio is several times the cruise thrust.
- Electric propulsion buys quiet simplicity at the price of a battery wall, while a combustion engine buys an order of magnitude more endurance per unit mass at the price of vibration and a minimum practical size.
- For a propeller aircraft, fly slow at the minimum-power speed for endurance and faster at the best lift-to-drag speed for range, and size everything at the worst density altitude rather than the bench condition.

You can read the full article here:
https://sgeos.github.io/aerospace/engineering/uav/2026/06/02/propulsion_and_power_sizing_for_fixed_wing_uavs.html

#UAV #FixedWing #Aerospace #Propulsion #Propeller #ElectricFlight #Endurance #DroneOps

---

## Action Items for the Human Pilot

- Confirm the 2026-06-02 publication date is as intended. A118 completes the fixed-wing-UAV set, one day after A116.
- Optionally request schematic diagrams (the power-required-versus-speed curve with the minimum-power and best-lift-to-drag speeds marked, the drag polar, the propeller efficiency-versus-advance-ratio curve, and the battery-versus-fuel endurance comparison), which are the one improvement that cannot be added in text and would require image assets.
- Optionally request the next sequel in the series, namely guidance, navigation, and automatic landing, or stability and control sizing, both flagged earlier as natural follow-ups.

---

## Notes

- Next available article number: A120.
- 0 release candidates.
- 0 new drafts. A108 through A119 published.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification.
- Published: A79 through A119.
- A118 completes the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion). No internal research cited; public encyclopedic and authoritative sources only.
- All scratch is confined to project-local `tmp/` per recorded preference. A118 process-file deltas were staged in `tmp/a118/` while drafting and have now been applied directly, so those notes are superseded.
- Blog deploys through GitHub Actions with a lean Jekyll stack; 0 open Dependabot alerts; Keleusma highlighting is live.
