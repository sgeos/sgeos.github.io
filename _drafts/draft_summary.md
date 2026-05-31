---
layout: post
mathjax: false
comments: true
title: "Draft Summary"
date: 2000-01-01 00:00:00 +0000
categories: meta
---

<!-- Axxx -->

This post reviews the status of draft posts in this blog's `_drafts/` directory.
Each draft is assessed for topic, completion status, remaining work, and publication sensibility.
Assessments assume that contemporary tooling will be used if salvaged
and that appropriate ecosystem standard choices will replace any tooling that has fallen out of favor.
Missing sections and prose will need to be drafted.
Stubs and largely incomplete drafts are assessed for topicality and publication merit.

## Draft Status

### Communications and the Command-and-Control Data Link for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-09-communications_and_the_command_and_control_data_link_for_fixed_wing_uavs.markdown`
**Topic**: The command-and-control data link of a fixed-wing UAV, framed on the link budget (received power versus noise) with latency as the companion constraint; the first extension beyond the core arc.
**Article Number**: A126
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-09 (34 references)

Standalone aerospace article and the first extension beyond the core fixed-wing-UAV arc (which closed with the A125 capstone).
The master variable is the link budget, P_rx = P_tx + gains - free-space path loss, with the signal-to-noise margin setting range and the Shannon limit bounding data rate, and latency as the companion constraint that decides what can be controlled over the link.
Sections covered include
the link budget (Friis, free-space path loss, SNR, Shannon, Fresnel, ISM bands, the frequency range-versus-rate trade, near-ground multipath and the two-ray ground reflection, the regulatory cap on effective radiated power);
the radio horizon;
the moving aircraft (airframe shadowing, radiation-pattern nulls and polarization, antenna diversity, a tracking ground antenna);
the three streams (command uplink, telemetry downlink, payload downlink with codec compression latency);
radio control with a handheld transmitter (2.4 GHz FHSS, ExpressLRS, CRSF/SBUS handoff, the control-link packet rate, FPV, failsafe, the manual path);
computer-controlled transmission (MAVLink, SiK/RFD900 telemetry radios, the ground control station, companion computer over cellular, intent versus stick inputs, coexisting with the handheld link);
beyond line of sight (relay, cellular, SATCOM via Iridium);
latency and why the fast loops are aboard (tying A123 and A125);
security and jamming (J/S ratio, spread spectrum, AES encryption, spoofing, directional antenna);
lost link (the preset failsafe, geofence, tying A116 and A125);
scale and the UAV case (the radios as part of the A121 hotel load);
a worked example (a 100 mW 2.4 GHz link closing 10 km with a 12 dB margin, a ~48 km radio horizon, kbps command versus Mbps video, LOS versus SATCOM latency);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
The pilot's explicit requirement, RC control via both a consumer handheld controller and a computer-controlled transmitter, is covered in its own two sections framed as the coexisting manual and autonomous paths.
References A116, A121, and A125 via post_url.
34 references across Reference (28), Related Post (3), and Research (3) categories.

### Guidance, Navigation, and Automatic Landing for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-08-guidance_navigation_and_automatic_landing_for_fixed_wing_uavs.markdown`
**Topic**: The outer-loop autonomy of a fixed-wing UAV, framed on the feedback loop that drives the error between the navigation estimate and the guidance command to zero; the capstone of the set.
**Article Number**: A125
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-08 (29 references; 333 lines)

Standalone aerospace article and the tenth and capstone entry in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion, A121 electric energy systems, A122 stability and control, A123 dynamic stability and control, A124 landing gear and touchdown, A125 guidance, navigation, and automatic landing).
Takes up the outer loop A123 set up.
The master variable is the feedback loop that drives the error between the commanded state (guidance) and the estimated state (navigation) to zero, nested by bandwidth, with the automatic landing as the tightest loop.
Sections covered include
the nested loops (inner attitude, outer guidance, mission, bandwidth separation, digital sample rates and latency);
navigation (GNSS, INS/IMU, dead reckoning, Kalman fusion, air data, RTK, initialization, GNSS-denied vision);
guidance (waypoints, cross-track error, the look-ahead path-following law);
wind and the ground track (crab, the wind triangle, the small-UAV case);
closing the loop with energy (the total energy control system as the real-time version of the series' energy budget);
the approach and automatic landing (glideslope, flare, RTK/radar-altimeter/vision, touchdown dispersion tied to the runway width) with the automatic-takeoff bookend;
when the loop breaks (GNSS loss, lost link, geofence, return-to-launch, redundancy, flight termination);
scale and the UAV case (Pixhawk-class boards, ArduPilot/PX4, the autonomy spectrum);
a worked example (loop bandwidth separation, the cross-track law, the navigation error budget, the glideslope dispersion);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
References A114, A116, A123, and A124 via post_url, and the conclusion ties the whole ten-article set together.
29 references across Reference, Related Post, and Research categories.
333 lines.

### Landing Gear and the Physics of Touchdown for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-07-landing_gear_and_the_physics_of_touchdown_for_fixed_wing_uavs.markdown`
**Topic**: Landing gear and the surface interfaces of a fixed-wing UAV, framed on the touchdown energy absorbed over a stroke, complementing the runway and recovery articles.
**Article Number**: A124
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-07 (23 references; 320 lines)

Standalone aerospace article and the ninth in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion, A121 electric energy systems, A122 stability and control, A123 dynamic stability and control, A124 landing gear and touchdown).
The master variable is the touchdown energy absorbed over a stroke, n = v^2/(2 g0 d), the energy-and-stroke idea of the recovery article applied to the final surface interface.
Sections covered include
the touchdown energy and the stroke;
wheels and landing gear (retractable versus fixed, tricycle and conventional layout, the oleo strut as gas spring and oil damper, recoil damping and bounce, frangible and sacrificial gear, spin-up and side gear loads, the gear-up fallback);
skids (sacrificial skids, friction stroke, skis and tundra tires by surface);
water landings (floatplane, flying boat, planing and the step, ditching, porpoising);
drogue and main parachutes (the drogue-before-main staging, with the residual touchdown energy taken by an airbag or crush);
deliberate impact (intentional lithospheric and hydrospheric intersection, crushable crashworthy structure for expendable vehicles);
energy bleeding before touchdown (spoilers, forward slip, S-turns, flare, with the honest distinction that true aerobraking is an orbital maneuver while a boost-glide or ramjet or scramjet vehicle does thermally limited atmospheric deceleration);
scale and the UAV case;
a worked example (sink-rate, parachute, and deliberate-impact loads set by the stroke);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
Complements rather than duplicates the launch-and-recovery article.
References A114, A116, A120, and A122 via post_url.
23 references across Reference, Related Post, and Research categories.
320 lines.

### Dynamic Stability and Control for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-06-dynamic_stability_and_control_for_fixed_wing_uavs.markdown`
**Topic**: Dynamic stability and control of a fixed-wing UAV, framed on the damping and frequency of the aircraft's natural modes, the dynamic sequel that completes the stability-and-control arc begun by the static-stability article.
**Article Number**: A123
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-06 (22 references; 316 lines)

Standalone aerospace article and the eighth in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion, A121 electric energy systems, A122 stability and control, A123 dynamic stability and control).
Takes up the dynamic question A122 deferred.
The master variable is the damping and frequency of the natural modes, with the aircraft modeled as a damped harmonic oscillator where static stability is the spring, inertia the mass, and aerodynamic rate forces the damping.
Sections covered include
the spring, the mass, and the damping (with a small-disturbance about-trim caveat);
the longitudinal modes (short-period, phugoid);
the lateral-directional modes (roll subsidence, spiral, Dutch roll, with the spiral-versus-Dutch-roll trade tied to A122's dihedral-versus-weathercock balance);
damping, frequency, and handling qualities (settling time, Cooper-Harper, flying-qualities levels);
gusts and ride quality (turbulence excitation and the small-UAV gust sensitivity);
stability augmentation (yaw damper, pitch damper, rate feedback from an IMU, the SAS inner loop, augmentation limits and pilot-induced oscillation, and the SAS-versus-CAS distinction);
fly-by-wire and relaxed static stability;
scale and the UAV case (faster modes, autopilot and actuator bandwidth);
a worked example (Dutch-roll damping from 0.05 to 0.4 with a yaw damper, and a phugoid period);
and an Out of Scope section that defers derivative estimation and the equations of motion, control-law synthesis, sensors and state estimation, structural and aeroelastic dynamics, departure and spin, and the outer-loop guidance, navigation, and automatic landing.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
References A112, A114, and A122 via post_url.
22 references across Reference, Related Post, and Research categories.
316 lines.

### Stability, Control, and Configuration for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-05-stability_control_and_configuration_for_fixed_wing_uavs.markdown`
**Topic**: Stability, control, and configuration of a fixed-wing UAV, framed on the balance of moments about the center of gravity with the static margin as the master proxy for the stability-versus-maneuverability trade.
**Article Number**: A122
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-05 (46 references; 409 lines)

Standalone aerospace article and the seventh in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion, A121 electric energy systems, A122 stability and control).
Takes up the full stability-and-control treatment A112 deferred.
The master variable is the moment balance about the center of gravity, with the static margin K_n = (x_np - x_cg)/MAC as the proxy for the stability-versus-maneuverability trade.
Sections covered include
the moment balance and the static margin (with the center-of-gravity range across the loading envelope);
lateral and directional static stability (fin weathercock stability and dihedral);
airfoils, camber, and invertibility;
configuration archetypes (conventional empennage, canard, tandem, tailless flying wing with sweep, washout, and reflex);
control surfaces by placement and name (elevator, aileron, rudder, elevon, ruddervator, stabilator, flaperon) with adverse yaw;
high-lift and spoiler devices;
control authority and dynamic pressure, running from aerodynamic surfaces through differential thrust and thrust vectoring to a reaction control system (spaceplane RCS and cold-gas thrusters, tied to A120's boost-glide arc, with an honest low-altitude caveat);
the wing tradeoff (aspect ratio versus wing loading, speed versus glide, planform);
the trim-drag energy cost;
a worked example (static margin and tail volume coefficient, with a flying-wing reflex contrast);
and an Out of Scope section that defers the dynamic-stability modes, control-law design, RCS detailed design, and the translational orbital problem (orbital mechanics, the orbital maneuver, and stationkeeping, affirmed as legitimate for spacecraft that reach orbit).
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
References A112, A114, and A118 via post_url.
46 references across Reference, Related Post, and Research categories.
409 lines.

### Electric Energy Systems and the Endurance Budget for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-04-electric_energy_systems_and_endurance_budget_for_fixed_wing_uavs.markdown`
**Topic**: The electric energy economy of a fixed-wing UAV, framed as a state-of-charge energy-flow budget (supply minus demand, buffered by storage), the flow counterpart to A120's stock budget.
**Article Number**: A121
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-04 (29 references; 381 lines)

Standalone aerospace article and the sixth in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion, A121 electric energy systems).
Fills the solar, fuel-cell, hybrid, and battery-management items A118 deferred.
The master variable is the energy-flow budget, the power balance dE/dt = P_in - P_out and its integral over the harvest cycle, contrasted explicitly with A120's one-time energy stock (stock versus flow).
Sections covered include
the energy-flow budget;
the demand side and the hotel load (flight power versus a fixed non-propulsive floor);
storage as the buffer (specific energy, depth of discharge, round-trip efficiency, cold derating, the specific-energy-versus-specific-power tradeoff, the battery wall, supercapacitor for peaks);
harvesting from the sun (output = efficiency times area times irradiance, the daily account, MPPT named);
the scale gate for solar perpetual flight (square-cube, Pathfinder/Helios/Zephyr/Solar Impulse);
harvesting from hydrogen (PEM fuel cell, Ion Tiger, Phantom Eye);
hybrid systems (series and parallel);
harvesting from the air (thermal and dynamic soaring);
the perpetual-flight closure (daily harvest at least daily demand, night energy within usable storage, cycle-life bounding the campaign);
a worked example on the 25 kg series aircraft;
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
The thesis is that sustained flight is a balance of powers rather than a quantity of energy, and indefinite flight is the cycle closing on itself, which the large light high-flying solar aircraft achieves and the small one does not.
References A112, A118, and A120 via post_url.
29 references across Reference, Related Post, and Research categories.
381 lines.

### Staged and Boosted Propulsion for Small Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-03-staged_and_boosted_propulsion_for_fixed_wing_uavs.markdown`
**Topic**: Staged and boosted propulsion for a ~2m fixed-wing UAV, framed around the post-boost mission energy budget (potential plus kinetic plus stored propulsive energy).
**Article Number**: A120
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-03 (40 references; 472 lines)

Standalone aerospace article and the fifth in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion).
Reopens the high-speed families A118 ruled out of regime by adding a boost stage, and is framed throughout as the management of the post-boost mission energy budget.
The boost deposits potential and kinetic energy (Tsiolkovsky rocket equation, specific impulse, one versus two stage), to which stored propulsive energy is added, and the kinetic share sets the stagnation temperature and therefore the airframe material.
Sections covered include
the mission energy budget with the energy height h_e = h + V^2/2g;
the boost stage;
the thermal wall (stagnation temperature versus Mach, aerodynamic heating, altitude and duration relief);
airframe materials by regime (LW-PLA subsonic, aluminum/composite transonic, titanium/steel supersonic with the SR-71 anchor, superalloy/refractory/CMC/carbon-carbon/UHTC/active-cooling/ablative hypersonic with the X-43 and X-51 anchors);
airframe archetypes for spending the budget (vertical-fighter banking it as altitude with the Bachem Natter anchor, maneuverable descending spending it on lift with lifting-body/waverider/HGV/MaRV members, and conventional holding it level on propulsion);
boost-glide with range (L/D)(h + V^2/2g);
boost-sustainer (RATO and the cruise-missile boost-turbojet);
boost-ramjet (integral rocket-ramjet, GQM-163 Coyote, Mach 2-4 titanium airframe);
boost-scramjet (X-43, X-51, hypersonic materials, research-grade honesty);
boost-throttleable-rocket;
one stage versus two;
a worked example on a 2 m vehicle (propellant fraction and stagnation temperature to Mach 2 and Mach 5, with the Mach-5 energy height of about 147 km);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
The thesis is that the ~2m scale forbids none of these configurations, since material and budget, not size, set how far up the speed ladder a prototype can be carried.
References A112, A114, A116, and A118 via post_url.
40 references across Reference, Related Post, and Research categories.
472 lines.

### Propulsion and Power Sizing for Small Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-02-propulsion_and_power_sizing_for_fixed_wing_uavs.markdown`
**Topic**: Sizing the propulsion and power system of a small fixed-wing UAV, worked outward from the power-required master variable.
**Article Number**: A118
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-02 (36 references; 445 lines)

Standalone aerospace article and the fourth in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion).
Establishes the power-required master variable, where power is thrust times speed and thrust in level flight is drag, so the power to fly is the weight times the speed divided by the lift-to-drag ratio, and works through
the drag polar and lift-to-drag ratio;
propellers and efficiency via momentum theory, static thrust, and advance ratio, including the electric ducted fan;
the thrust-to-weight and launch and climb case that usually sizes the powertrain, tying back to A114 and A116;
electric propulsion (battery specific energy, brushless motor, the endurance equation, and the battery wall);
combustion propulsion (two-stroke and Wankel, brake-specific fuel consumption, heavy fuel, range and endurance);
altitude and available power (the density-altitude lapse of engine power and propeller thrust);
endurance and range with reserves (endurance at the minimum-power speed, range at the best lift-to-drag speed for a propeller aircraft);
a brief solar, hybrid, and fuel-cell note;
jets and regimes beyond the propeller (turbojet and turbofan in scope; ramjet, scramjet, throttleable rocket, and rocket boost-glide named and declared out of regime);
a worked example on the 25 kg series aircraft;
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
Real-UAV anchors RQ-7 Shadow (Wankel), ScanEagle (heavy-fuel piston), and RQ-20 Puma (electric).
References A112, A114, and A116 via post_url.
36 references across Reference, Related Post, and Research categories.
445 lines.

### Three Audiences for an Operating System — Published

**File**: `_posts/2026-05-22-three_audiences_for_an_operating_system.markdown`
**Topic**: Prequel to the BTRON-hypermedia trilogy. Names the operator-as-end-user category as a distinct third audience for an operating system, alongside the consumer and the developer. Sets up the question that A113, A115, and A117 then answer.
**Article Number**: A119
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-22 (61 references; 1,364 lines)

Standalone category-framing article and the prequel to the BTRON-hypermedia trilogy (A113, A115, A117).
Sections covered include
Opening on who an operating system serves;
The Three Audiences (consumer, developer, operator with role definitions and the load-bearing authority concept);
The Consumer Answer (Apple HIG, Windows UX Guidelines, GNOME HIG, KDE HIG, Material Design);
The Developer Answer (Unix philosophy, Emacs, Vim, Visual Studio Code, Git, Cargo, npm, pip);
The Operator (the unfilled category);
A Short History of Operator-Facing Computing (Sketchpad, NLS, MOCR, Alto, Macintosh, BTRON, HyperCard, OpenDoc, GNOME Bonobo, SCADA, PLCs, ARINC 661, ISA-101, NUREG-0700, IEC 62366, ISO 9241, ASM Consortium);
Why the Consumer Answer Fails the Operator (five structural failure modes);
Why the Developer Answer Also Fails (four structural failure modes);
The Operator Population Today (aerospace, medical, industrial, defense and intelligence, legal and regulatory, financial markets);
A Scorecard of Audience Requirements (10-row table across consumer, developer, operator);
The Gap That Remains;
Out of Scope (defers the substantive solution, the language substrate, and the worked vertical to the trilogy);
Conclusion.

References:
61 references across Reference (58) and Related Post (3) categories.
All inline-linked per project style.
A113, A115, and A117 cited via post_url as the deferred follow-ups.
No internal research cited.
A research agent verified the operator-specific references (ISA-101, ASM Consortium, IEC 62366, ISO 9241, NUREG-0700, ARINC 661, glass cockpit, SCADA, HITL, ergonomics, alarm fatigue) and the audience-contrast sources (Apple HIG, Windows UX, GNOME HIG, KDE HIG, Unix philosophy).

### Launch and Recovery Systems for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-01-launch_and_recovery_systems_for_fixed_wing_uavs.markdown`
**Topic**: Runway-independent launch and recovery for fixed-wing UAVs, worked outward from the energy-and-stroke master variable.
**Article Number**: A116
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-01 (26 references; 478 lines)

Standalone aerospace article and the runway-independent companion to A114.
Establishes the energy-and-stroke master variable, where launch must add and recovery must remove a kinetic energy fixed by mass and flying speed and the g-load rises as the stroke shrinks, and works through
launch by catapult (bungee, pneumatic, hydraulic, rail), winch and aerotow, booster, and zero-length launch;
recovery by net and cable (Skyhook), arrested landing, parachute and airbag, belly skid, and high-alpha braking (deep stall, cobra braking as a routine procedure, and perched landing);
wind and environment;
the acceleration limit;
failure and abort modes, with the fail-safe principle and a flight-termination or controlled-ditch option;
matching launch to recovery with real-UAV anchors (ScanEagle, RQ-7 Shadow, RQ-21 Blackjack);
airframe implications;
a worked numeric example;
and a fully declared Out of Scope.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
References A114 (Runway Sizing for Fixed-Wing UAVs) and A112 (Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass) via post_url.
26 references across Reference, Related Post, and Research categories.
478 lines.

### Human Spaceflight Ground Systems as an Illustrative Vertical for a Hypermedia Desktop — Published

**File**: `_posts/2026-05-25-human_spaceflight_ground_systems_as_illustrative_vertical.markdown`
**Topic**: Vertical-specific follow-up to A113 and A115. Walks through human spaceflight ground systems in the Apollo lineage, lampshaded as an illustrative example vertical with explicit extrapolation guidance to modern crewed launch and on-orbit operations. Includes a Day-in-the-Launch-Operator's-Workflow walkthrough and six verified Keleusma code samples for the load-bearing claims.
**Article Number**: A117
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-25 (40 references; 1,944 lines)

Sections covered include
The Apollo Reference (MOCR, RTCC on IBM System/360 Model 75, LCC and Firing Rooms, MSFN, NASCOM, Flight and Mission Rules, simulators, recovery, the flight directors and Apollo 13);
Extrapolation to Modern Requirements (CCSDS, Commercial Crew Program, ISS Multilateral Coordination, Artemis and Human Landing System, FAA Part 450, NPR 7150.2 and NASA-STD-8719.13 and NPR 8705.2, ITAR);
The Hypermedia Object Model in Launch Operations (six commitments with Apollo-to-hypermedia mapping table);
Engineering Commitments in Launch Operations (five commitments with five Keleusma code samples and a mapping table);
The Ten-Layer Architectural Sketch in Launch Operations (full table inheriting A115 verdicts and clarifying each layer's launch role);
A Day in the Launch Operator's Workflow (eleven scenes from pre-launch shift report through post-flight review);
Trust and Provenance;
Certification and Regulatory Posture;
Why This Vertical Is a Good Illustration (and where it is hard);
Risks and Open Questions;
Out of Scope (link store schema, certification path, contractor selection deferred to future posts);
Conclusion.

Six verified Keleusma code samples in `tmp/a117/`:
01_countdown_sequencer.kel (loop main compiles to 260 bytes);
02_telemetry_alarm.kel (Proprietary -> displayable bucket, returns 1);
03_abort_decision.kel (Sensitive -> typed outcome, returns 2);
04_abort_decision_reject.kel (same without declassify, compile-time reject);
05_mission_rules.kel (const data registry, returns 300);
06_signed_flight_rules.kel (signed entry function compiles to 232 bytes).

References:
40 references across Reference (37), Related Post (2), and Research (1) categories.
All inline-linked per project style.
A113 and A115 cited via post_url.
Apollo-era and contemporary primary sources verified by a parallel research agent.
No internal Keleusma research cited.

### Keleusma as a Substrate for a Real-Time Hypermedia Desktop — Published

**File**: `_posts/2026-05-24-keleusma_as_substrate_for_real_time_hypermedia_desktop.markdown`
**Topic**: Follow-up to A113. Maps Keleusma V0.2.0 capabilities and the public V0.5+ roadmap onto A113's six structural commitments of the hypermedia object model, the five engineering commitments for real-time hypermedia composition, and the ten-layer architectural sketch. Vertical-agnostic by design; the vertical-specific treatment is deferred to a separate follow-up.
**Article Number**: A115
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-24 (45 references; 1,701 lines)

Analytical follow-up to A113. Sections covered include
What Keleusma Provides at Version 0.2.0;
The Six Structural Commitments of the Hypermedia Object Model;
The Five Engineering Commitments for Real-Time Hypermedia;
Mapping the Ten-Layer Architectural Sketch (ten verdicts: two strong fits, five partial fits, three mismatches);
What Keleusma Uniquely Provides (verified totality, verified WCET/WCMU, language-level IFC);
What Keleusma Does Not Provide (mature ecosystem, general-purpose breadth, authoring tooling);
The Asymmetry and Its Implication;
The Roadmap Path (V0.3.0 self-hosted compiler through V0.5.x interval-graph refinement);
What Would Need to Be Built;
Risks and Open Questions;
Out of Scope (vertical choice, detailed link store design, certification path all deferred to separate posts);
Conclusion.

Five illustrative Keleusma code samples verified against the installed keleusma 0.2.0 CLI:
01_typed_part.kel (Citation struct, runs and returns 42);
02_handler_loop.kel (loop main with yield, compiles to 228-byte bytecode);
03_ifc_sanitiser.kel (classify/declassify sanitiser pattern, runs and returns 200);
04_ifc_reject.kel (same without declassify, verifier rejects at compile time);
05_preallocated.kel (const data block, runs and returns 20).

All examples in `tmp/a115/`.

References:
45 references across Reference (38), Related Post (5), and Research (1) categories.
Inline citations throughout per project style.
A113, A107, A109, A110, A111 cited via post_url.
No internal Keleusma research material cited; only public Keleusma artefacts (README, crates.io, docs.rs, GitHub).

**Remaining Work**:
Human review of analytical claims and the Keleusma-to-BTRON mapping.
Confirm publication date and assign final timestamp.
Update memory once published.

### Runway Sizing for Fixed-Wing UAVs — Published

**File**: `_posts/2026-05-31-runway_sizing_for_fixed_wing_uavs.markdown`
**Topic**: Sizing runways for small and medium fixed-wing UAVs, worked outward from the master speed variable.
**Article Number**: A114
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-31 (28 references; 548 lines)

Standalone aerospace article.
Establishes the squared-speed master variable, where stall and liftoff speed are set by wing loading, air density, and the maximum lift coefficient, and works outward through explicit square-cube size-scaling;
the level ground roll;
paved versus dirt surfaces;
inclined and ski-jump runways;
wind, crosswind, and landing-gear ground handling;
orientation with an Earth-rotation dismissal;
density altitude;
obstacle clearance, margins, and an in-scope abort and stopping-margin note;
the landing roll and ground effect;
width and the lateral dimension (touchdown dispersion and guidance lateral error);
full-runway versus single-phase operation anchored to real UAVs (ScanEagle, RQ-7 Shadow, MQ-9 Reaper);
planform and airframe implications (conventional, delta, flying wing);
a worked numeric example;
and lighting, reflectors, and markings (optional versus required).
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
References A112 (Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass) via post_url.
28 references across Reference, Related Post, and Research categories.
548 lines.

### BTRON, Hypermedia, and the Real-Time Desktop — Published

**File**: `_posts/2026-05-23-btron_hypermedia_and_real_time_desktop.markdown`
**Topic**: Historical and analytical treatment of the BTRON proposition, the asymmetry between successful real-time operating systems and failed hypermedia desktops, a contemporary diagnosis of the market gap, and a concrete architectural sketch for a 2026 successor.
**Article Number**: A113
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-23 (149 references; 4,166 lines)

Standalone operating-systems history and philosophy article.
Surveys the BTRON proposition under the TRON Project (Sakamura, 1984),
why BTRON failed (Super 301 trade dispute listed in April 1989 and withdrawn the following month after USTR site visit, hardware program collapse, ecosystem shortfall, conceptual depth tax, vendor entrenchment),
the histories of relevant real-time operating systems (VRTX 1981, pSOS ~1982, VxWorks 1987, QNX 1980 in the Ottawa area of Canada, QNX Photon, Green Hills INTEGRITY, FreeRTOS, Zephyr, RTEMS, NuttX, μITRON, T-Kernel, seL4, Genode, Redox OS),
the histories of hypermedia systems (Memex, NLS in 1968 funded by ARPA/NASA/USAF, Project Xanadu, Smalltalk, NoteCards developed at Xerox PARC starting 1984 by Trigg/Halasz/Moran, HyperCard 1987-2004, OLE 2 in the 1992-1993 window, Cairo, OpenDoc framework 1994 and CyberDog 1996, Bonobo, KParts, Lotus/HCL Notes ~42M peak seats with ~140M cumulative licenses, SharePoint, World Wide Web with the Berners-Lee 1989 CERN proposal, Roam, Logseq, Obsidian, Notion, Coda, Jupyter, Observable, Solid, Beaker last released December 2020, Automerge, Yjs, ActivityPub),
the six structural commitments of the hypermedia object model,
where the model wins on merit and where it is clearly the wrong fit,
the real-time-plus-hypermedia special case,
who is served by the mass-market file-and-application model,
who would benefit from a real-time hypermedia desktop,
the web browser as substrate analysis,
a super-browser as modern realization,
why the gap persists (four-component diagnosis),
and viable entry strategies (vertical-first, internal-program, acquisition-path, sponsored-standards).
References A93 (Fast-Moving Versus Mission-Critical Engineering) and A86 (Mission Command Management Style) via post_url.
76 references across 4 categories (Book, Reference, Related Post, Research).
2,219 lines.

**Research Pass (2026-05-31)**:
Four parallel research agents verified factual claims across TRON Project history,
real-time operating systems history, hypermedia systems history,
and contemporary tools / regulated-industry incumbents / standards.
Corrections applied:
ITRON deployment softened from "several billion per year" to "cumulative billions";
Super 301 chronology refined (listed April 1989, withdrawn May 1989);
Real Object / Virtual Object pairing introduced for BTRON's hypermedia model;
TRON character code Unicode comparison added with concrete dates (Cho Kanji 1999 ~180K characters vs Unicode 4.1 in 2005);
RTOS first-generation date range corrected from "1970s-early 1980s" to "early 1980s";
QNX origin location corrected from "Ottawa" to "Ottawa area of Canada" with University of Waterloo founder attribution;
QNX Photon deprecation since 2014 disclosed;
QNX vehicle deployment updated to "more than 275 million" with BlackBerry press release citation;
FreeRTOS "most widely deployed" softened to "among the most widely deployed";
FreeRTOS AWS 2017 transaction reframed as stewardship transfer with AWS blog citation;
seL4 superlative softened to "most extensive functional-correctness proof of a general-purpose OS kernel";
Redox OS alpha status disclosed;
NLS funding expanded to ARPA/NASA/USAF;
NoteCards authorship attributed (Trigg, Halasz, Moran);
HyperCard "several million users" softened to "millions";
OLE 2 release window clarified (1992-1993);
OpenDoc shipping clarified (framework 1994, CyberDog 1996);
Lotus Notes seat counts corrected from "hundreds of millions" to ~42M active / ~140M cumulative;
SharePoint primitives clarified (files and lists);
Beaker reframed from "dormant" to "discontinued after December 2020";
ARP4754B successor noted.
URL fixes:
ref_cho_kanji (Wikipedia 404, replaced with chokanji.com);
ref_super_301 (replaced with Section 301 stable URL);
ref_vrtx (replaced with Versatile_Real-Time_Executive);
ref_qnx_neutrino (replaced with qnx.software);
ref_qnx_photon (replaced with QNX_Photon Wikipedia entry).
New references added with inline citations:
ARP4754A; TRON character encoding;
IEEE Milestone for TRON RTOS family;
USTR 25 May 1989 statement;
Mars Pathfinder priority inversion engineering note;
BlackBerry QNX 275M vehicles press release;
Amazon FreeRTOS launch blog post;
seL4 SOSP 2009 paper;
Engelbart and English 1968 AFIPS paper;
Halasz 1988 NoteCards retrospective in CACM;
Berners-Lee 1989 CERN proposal;
Kleppmann and colleagues local-first essay (Onward 2019).
URL verification:
all new URLs return HTTP 200 except ACM Digital Library and chokanji.com which return 403 to curl due to bot detection but are valid human-accessible URLs.

**Expansion Pass (2026-05-31)**:
Four additional parallel research agents covered alternative research operating systems (Plan 9, Inferno, Self, Oberon, JX),
the artificial intelligence and large language model angle (retrieval-augmented generation, Model Context Protocol, structured output, Coalition for Content Provenance and Authenticity, agent provenance research),
architectural building blocks for a 2026 hypermedia operating system (Automerge, Yjs, Loro, InterPlanetary File System, Iroh, Hypercore, seL4, Genode, Capsicum, Cap'n Proto, WebAssembly Component Model, Servo, Chromium Embedded Framework, WebKit, ProseMirror, TipTap, Lexical, JetBrains Meta Programming System, CodeMirror, Skia, Cairo Graphics, HarfBuzz, FreeType),
and regulated-industry incumbents (DOORS, Polarion, Windchill, ENOVIA, Vault, Gotham, Foundry, Relativity, iManage).
Seven new sections added:
"Other Radical Unifications" (Plan 9, Inferno, Self/Morphic, Oberon, JX as alternative unification approaches);
"Performance and Latency Engineering for Composed Documents" (bounded handler execution time, deadline propagation, preallocated resources, spatial and temporal isolation, admission control);
"The Artificial Intelligence Synergy" (RAG, MCP, structured output, C2PA, regulatory provenance requirements, PROV-AGENT, HyperAgents workshop);
"How the Incumbents Compare" (comparison table across the nine incumbents on typed parts, typed links, in-place composition, provenance, and local-first persistence);
"Coexistence with the File and Application World" (file system bridges, import handlers, lossy export, gradual adoption);
"A Concrete Architectural Sketch" (ten layers from verified microkernel through user-facing shell, naming production-quality open-source components for each);
"Out of Scope" (explicit declaration of seven topics deferred to follow-up articles).
56 new authoritative sources added with inline citations.
Reference count rose from 76 to 132 across Book (2), Reference (108), Related Post (2), and Research (20) categories.
Line count rose from 2,219 to 3,408.

**Completion Pass (2026-05-31)**:
Three additional parallel research agents covered Lifestreams (Gelernter and Freeman, Yale, mid-1990s),
Sutherland's Sketchpad (1963) and Alan Kay's Dynabook (1968-1972),
and the contemporary Tools for Thought movement (Matuschak, Nielsen, Appleton, Bret Victor, Rheingold, Future of Coding, Hyperlink Academy).
Seven new sections and inline additions added:
Sketchpad paragraph in hypermedia history;
Dynabook paragraph in hypermedia history;
Lifestreams paragraph in hypermedia history;
Tools for Thought paragraph in hypermedia history (with cultural framing);
"A Day in the Workflow, an Aerospace Requirements Example" between Architectural Sketch and Conclusion;
"Epistemic State of the Argument" between Workflow and Conclusion (distinguishing factual, structural, and strategic claims);
"Reader's Next Steps" after Out of Scope (TRON Forum, seL4 community, Genode community, local-first community, Solid working group, HyperAgents workshop, Tools for Thought community);
"Glossary" after Reader's Next Steps (defined-terms section for 12 key concepts including capability-based security, compound document, conflict-free replicated data type, content-addressable storage, handler, hypermedia object model, link store, microkernel, provenance, real-time operating system, separation kernel, transclusion, typed link, typed part).
17 new authoritative sources added with inline citations:
Mirror Worlds (Gelernter 1991 Oxford);
Tools for Thought (Rheingold 1985 MIT Press);
Lifestreams CHI 1996 paper;
Lifestreams SIGMOD 1996 paper;
Lifestreams Yale project page;
Sutherland's Sketchpad Cambridge-hosted thesis;
Sketchpad Wikipedia;
Kay and Goldberg Personal Dynamic Media 1977;
Dynabook Wikipedia;
Matuschak and Nielsen 2019 ttft essay;
Matuschak personal site;
Evergreen Notes;
Maggie Appleton personal site;
Appleton Garden History essay;
Bret Victor Magic Ink essay;
Future of Coding;
Hyperlink Academy.
Reference count rose from 132 to 149.
Line count rose from 3,408 to 4,166.
All anchors verified used and defined; style scan clean.
URL verification: all HTTP 200 except documented OUP 202 (project memory) and ACM DL 403 (bot detection, valid for human readers).

**Remaining Work**:
Human review of the four completion-pass additions (Lifestreams, Sketchpad/Dynabook, Tools for Thought, user journey walkthrough, epistemic state, next steps, glossary).
Confirm publication date and assign final timestamp.
Update Software Versions section if any is desired (currently omitted to match A98-class analytical-article convention).
Update memory once published.

### Solana sBPF Assembly Example — Pre-Release Candidate

**File**: `solana_sbpf_assembly_example.markdown`
**Topic**: Writing Solana programs using sBPF assembly with the sbpf standalone toolchain
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

Completely rewritten from a partial draft with x86 assembly and clang build.rs
to use the correct sBPF instruction set and the sbpf standalone toolchain.
Covers the sBPF virtual machine, registers and memory layout, instruction set overview,
toolchain installation, project creation, a Hello World program using `.rodata` section,
`lddw` address loading, and `.equ` named constants for all non-trivial literals.
Building and deploying with sbpf tool,
and the current state of mixed Rust and assembly projects.
Three experimental paths for mixed projects documented (nightly inline asm, sbpf-linker, build.rs).
Includes a theoretical linked Rust and assembly example
using the Solana SDK's Clang and llvm-ar in a `build.rs` script.
The Rust entrypoint passes a string to an sBPF assembly logging subroutine via C FFI.
Both assembly files use `.equ` named constants with inline comments.
Nine limitations documented.
Eleven references across two categories (Reference, Research).
No article number assigned. Not slotted for publication.

**Remaining Work**:
Human verification by building and deploying the Hello World program with the sbpf tool.
Verify the linked Rust and assembly example compiles with cargo build-sbf.
Fill in Software Versions TODO placeholders.
Verify assembly code executes correctly on a local test validator.
Assign article number and publication date when ready.

### Android Development on FreeBSD — Pre-Release Candidate

**File**: `android_development_on_freebsd.markdown`
**Topic**: Android SDK and NDK development on FreeBSD using Kotlin, Rust, and the Linuxulator
**Completion**: ~90%
**Publication Sensibility**: Medium
**Status**: Pre-Release Candidate

Completely rewritten from 2017 content (FreeBSD 11, SDK 25, NDK r13b)
to modern toolchain (FreeBSD 14, SDK 35, NDK r28).
Covers Linuxulator setup with Rocky Linux 9 base,
Android SDK and NDK installation via sdkmanager,
ADB setup with native FreeBSD port,
Kotlin SDK development with standard XML layouts,
Rust NDK development with JNI integration via cargo-ndk,
and emulator feasibility discussion.
Sample app is a native Android port of the CLMM calculator (A91)
with Kotlin UI and Rust math exposed through JNI.
No article number assigned. Not slotted for publication.
Ten references across four categories (Android, FreeBSD, Related Post, Rust).

**Remaining Work**:
Human verification on FreeBSD hardware.
Fill in Software Versions TODO placeholders.
Test build pipeline on FreeBSD 14 with Linuxulator.
Assign article number and publication date when ready.

### Android Unit Testing — Pre-Release Candidate

**File**: `android_unit_testing.markdown`
**Topic**: Android unit testing across Kotlin, Robolectric, instrumented, and NDK layers
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

Completely rewritten from 2017 content (SDK 25, Java 1.8, ApplicationTestCase)
to modern toolchain (SDK 35, JDK 17, Kotlin 2.1.0, AGP 8.9.0).
Test subject is the CLMM calculator app with both Kotlin and Rust native implementations.
Covers test dependencies (JUnit 4, AndroidX Test, Robolectric, MockK, Espresso),
local unit tests with pure logic and Robolectric Activity tests,
mocking with MockK object declarations,
instrumented tests with Espresso,
and NDK unit testing with Rust cargo test, JNI boundary testing, and GoogleTest for C++.
Running Tests section provides Gradle task table. Code Coverage section covers JaCoCo, Kover, and cargo-llvm-cov.
Seven limitations documented. MathJax enabled for CLMM reserve formulas.
References Android FreeBSD article and CLMM Mathematics (A91) via post_url.
No article number assigned. Not slotted for publication.
Twelve references across four categories (Android, Reference, Related Post, Rust).

**Remaining Work**:
Human verification of test code against actual Android project.
Fill in Software Versions TODO placeholders.
Verify floating-point test expected values against CLMM calculator.
Verify JNI function name conventions for NativeBridgeTest.
Assign article number and publication date when ready.
Android FreeBSD article and CLMM Mathematics (A91) must be published first.

### Authenticating a Phoenix JSON API with Guardian and Ueberauth — Pre-Release Candidate

**File**: `phoenix_json_api_authentication_with_guardian.markdown`
**Topic**: Phoenix/Elixir JSON API authentication with Guardian JWT and Ueberauth identity strategy
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

Completely rewritten from 2016 content (Phoenix 1.1.4, Elixir 1.2.3, Guardian ~0.10.0, Comeonin ~2.1)
to modern toolchain (Phoenix 1.7+, Guardian ~> 2.3, bcrypt_elixir ~> 3.0, Ueberauth ~> 0.10).
MemoApi example application with user registration, JWT-based login, and protected memo CRUD.
Uses context modules, Guardian implementation module pattern, plug pipeline, and error handler.
Ueberauth identity strategy integration with callback pattern example.
Testing the API section with curl commands and expected JSON responses.
Seven limitations documented.
References published article A27 "A Shell Script for Working with Phoenix JSON APIs" via post_url.
No article number assigned. Not slotted for publication.
Eleven references across four categories (Elixir, Phoenix, Reference, Related Post).

**Remaining Work**:
Human verification by building and running the MemoApi project.
Fill in Software Versions TODO placeholders.
Verify Guardian secret key generation command.
Verify Ueberauth identity strategy plug compatibility.
Assign article number and publication date when ready.

### Getting Started with Claude Code on FreeBSD — Pre-Release Candidate

**File**: `claude_code_getting_started_on_freebsd.markdown`
**Topic**: Installing and configuring Claude Code on FreeBSD
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

New article covering Claude Code installation on FreeBSD via the misc/claude-code port, binary packages, and npm.
Documents shebang fix, ripgrep configuration, and a Hello World exercise
that generates a curses-based system dashboard using only FreeBSD base system tools.
Limitations section documents unsupported platform status and known issues.
References the companion Getting Started with Claude Code post (A74) via post_url.
Twelve references across four categories (Claude, FreeBSD, GitHub, Related Post).
No article number assigned. Not slotted for publication.

**Remaining Work**:
Human verification on FreeBSD hardware.
Fill in Software Versions output.
Test the Hello World prompt on FreeBSD.
Verify shebang fix and ripgrep configuration.
Assign article number and publication date when ready.

### Getting Started with Claude Code Over SSH — Pre-Release Candidate

**File**: `claude_code_getting_started_over_ssh.markdown`
**Topic**: Using Claude Code locally to work on remote machines over SSH
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

New article covering the use of Claude Code on a local workstation
to execute commands on remote machines via SSH.
Introduces SSH fundamentals for readers unfamiliar with the protocol.
Walks through Ed25519 key generation, public key copying, SSH agent setup,
host configuration, and verification.
Documents remote execution patterns using Claude Code's Bash tool
including single commands, multi-command chains, and scp file transfer.
Covers timeout configuration for long-running remote operations.
Detailed agent forwarding section covers mechanism, configuration,
verification, Claude Code usage, security considerations,
and ProxyJump as a safer alternative for untrusted intermediate hosts.
Briefly discusses Claude Code Desktop SSH as an alternative
that requires Claude Code on the remote machine.
Hello World section demonstrates end-to-end remote workflow
with OS detection, C code generation, scp transfer, and remote compilation.
References companion Getting Started posts for macOS (A74), FreeBSD, and OpenBSD via post_url.
Eleven references across three categories (Claude, Reference, Related Post).
No article number assigned. Not slotted for publication.

**Remaining Work**:
Human verification with an actual remote SSH target.
Fill in Software Versions output.
Test the Hello World prompt against a remote machine.
Verify agent forwarding with `ssh -A myserver "ssh-add -l"`.
Verify timeout configuration format.
Assign article number and publication date when ready.

### Getting Started with Claude Code on OpenBSD — Pre-Release Candidate

**File**: `claude_code_getting_started_on_openbsd.markdown`
**Topic**: Installing and configuring Claude Code on OpenBSD
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

New article covering Claude Code installation on OpenBSD via npm,
the only viable installation path on the platform.
No port or package exists for Claude Code on OpenBSD.
Documents bash installation and `/bin/bash` symlink requirement,
ripgrep configuration via `USE_BUILTIN_RIPGREP` setting,
and a critical warning against running the native installer or `claude install`
which downloads an incompatible Linux binary and breaks npm installations.
Hello World exercise generates a curses-based system dashboard using only OpenBSD base system tools.
Limitations section is more extensive than the FreeBSD article
due to the absence of a dedicated port and the removal of the Linux compatibility layer.
References the companion Getting Started with Claude Code post (A74)
and the FreeBSD article via post_url.
Twelve references across four categories (Claude, GitHub, OpenBSD, Related Post).
No article number assigned. Not slotted for publication.

**Remaining Work**:
Human verification on OpenBSD hardware.
Fill in Software Versions output.
Test the Hello World prompt on OpenBSD.
Verify bash symlink and ripgrep configuration.
Verify that `doas pkg_add node` installs a supported Node.js version (18-24).
Assign article number and publication date when ready.

### Getting Started with Solana Using Rust and Pinocchio — Pre-Release Candidate

**File**: `solana_with_rust_and_pinocchio_getting_started.markdown`
**Topic**: Building a Solana program with Pinocchio zero-dependency library, mirroring the Anchor companion article (A65)
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

New article mirroring A65 "Getting Started with Solana Using Rust and Anchor"
but using the Pinocchio zero-dependency library instead of Anchor.
Same key pegboard toy contract that stores a public key and encrypted private key on-chain.
Covers Pinocchio project setup, manual account validation, raw byte parsing,
PDA creation via CPI to System Program, Mollusk test harness,
building with cargo build-sbf, and deployment to local test validator.
Comparison table with Anchor implementation (A65).
Nine limitations documented.
References published article A65 via post_url.
No article number assigned. Not slotted for publication.
Twelve references across three categories (Reference, Related Post, Research).

**Remaining Work**:
Human verification by building and deploying the program with cargo build-sbf.
Fill in Software Versions TODO placeholders.
Run Mollusk tests against compiled BPF binary.
Verify Pinocchio crate versions are current.
Assign article number and publication date when ready.

### Template

**File**: `template.markdown`
**Topic**: Post template for new articles
**Completion**: N/A
**Publication Sensibility**: N/A

This is a template file, not a draft. It provides the standard structure for new posts.

## Summary

Ten files exist in `_drafts/`. One is a template.
No release candidates remain.
No new drafts remain.
No stubs remain.
A79 through A126 have been published.

**Tier 1: Publishable with moderate effort.**
No drafts remain in Tier 1.
A126 (communications and the command-and-control data link) is the first extension beyond the core fixed-wing-UAV arc; remaining unflagged extensions, if desired later, are structures and the flight envelope, payload and mission systems, and the regulatory and operations layer.

The drafts fall into four tiers when assessed for salvageability with contemporary tooling.

**Pre-Release Candidates.**
Android Development on FreeBSD has been fully rewritten with modern tooling
and is awaiting verification on FreeBSD hardware before publication.
Android Unit Testing has been fully rewritten with contemporary AndroidX Test, Robolectric, MockK,
and NDK testing coverage and is awaiting verification against an actual Android project.
Getting Started with Claude Code on FreeBSD covers installation via ports, packages, and npm
and is awaiting verification on FreeBSD hardware before publication.
Getting Started with Claude Code on OpenBSD covers npm-only installation with bash and ripgrep configuration
and is awaiting verification on OpenBSD hardware before publication.
Getting Started with Claude Code Over SSH covers using Claude Code locally to work on remote machines via SSH
and is awaiting verification with a remote SSH target.
Authenticating a Phoenix JSON API with Guardian and Ueberauth has been fully rewritten
from 2016 Phoenix 1.1/Guardian 0.10 to modern Phoenix 1.7+/Guardian 2.x
and is awaiting verification by building and running the MemoApi project.
Solana sBPF Assembly Example has been fully rewritten from a partial draft with x86 assembly
to use the correct sBPF ISA and the sbpf standalone toolchain,
revised with `.rodata` section usage and a theoretical linked Rust and assembly example,
and is awaiting verification by building and deploying with the sbpf tool.
Getting Started with Solana Using Rust and Pinocchio mirrors the Anchor companion article (A65)
using the Pinocchio zero-dependency library
and is awaiting verification by building and running Mollusk tests.

**No stubs remain.**
All article-numbered drafts have been elevated to release candidate status.

## Candidate Future Post Topics

The following table lists on-brand post ideas organized by thematic cluster.
Topics are selected to align with the blog's established strengths in systems programming, applied mathematics, unconventional toolchains, and AI-assisted development.

| Topic | Categories | Rationale | Builds On |
|-------|------------|-----------|-----------|
| Formal Verification with TLA+ | math development | Formal methods for distributed protocol design. Bridges the mathematical rigor thread with systems engineering. | Writing Proofs (A79), Radioactive Half-Life Demurrage Cryptocurrency Coin (A88) |
| Lean 4 and Automated Theorem Proving | math ai development | Interactive theorem prover with growing LLM integration. Connects proofs, AI, and software verification. | Writing Proofs (A79) |
| Property-Based Testing in Rust | rust development | QuickCheck-style testing as lightweight formal methods. Practical bridge between proofs and everyday engineering. | no_std Rust series, AMM Mathematics (A67) |
| RISC-V Assembly Getting Started | asm embedded development | Emerging instruction set architecture for embedded and open hardware. Natural extension of ARM and x86 assembly posts. | ASM Playdate Development, UNIX ARM Assembler |
| Rust on RISC-V Microcontrollers | rust embedded no_std | no_std Rust on RISC-V hardware. Combines two active threads in the blog. | no_std Rust series, Radioactive Half-Life Demurrage Cryptocurrency Coin (A88) |
| WebAssembly Component Model | rust wasm development | WASI and the component model as the next step beyond basic WASM. | WASM on Jekyll (A73) |
| ~~CLMM Mathematics and Calculator~~ | ~~crypto defi math~~ | ~~Concentrated liquidity mathematics with interactive widget. Direct sequel to AMM article.~~ | ~~Covered by Concentrated Liquidity Market Maker Mathematics (A91)~~ |
| ~~Solana sBPF Assembly~~ | ~~crypto development asm~~ | ~~Writing Solana programs at the assembly level. Unique low-level blockchain content.~~ | ~~Covered by Solana sBPF Assembly Example draft~~ |
| Statistics for A/B Testing | math development | Applied statistics for software engineers. Practical extension of the statistics reference. | Probability and Statistics Reference (A80) |
| ~~Orbital Mechanics Primer~~ | ~~math science~~ | ~~Applied physics with MathJax. Evergreen STEM content.~~ | ~~Covered by Introduction to Space Studies (A90)~~ |
| Context Engineering Patterns Cookbook | ai ai-tools development | Practical patterns distilled from the survey article. Shorter, actionable format. | Context Engineering (A78), A75-A77 series |
| Evaluating AI-Generated Code | ai development | Metrics and methods for assessing agent output quality. Addresses the evaluation gap identified in A78. | A75-A78 series |
| FreeBSD Jails for Development Environments | freebsd development | Container-like isolation using FreeBSD jails. Updates the FreeBSD systems thread with modern practices. | FreeBSD series (A1-A40 era) |
| Shell Scripting with Modern CLI Tools | sh unix development | fd, ripgrep, jq, fzf as modern replacements for traditional UNIX tools. | Shell scripting series |
| Game AI with Minimax and Alpha-Beta Pruning | gamedev math ai | Classical game AI algorithms with proofs of optimality. Bridges game development and mathematical rigor. | Chess/Go game theory series |
| Playdate Game Physics | gamedev playdate math c | Physics simulation on constrained hardware. Applied mathematics on embedded game platform. | Playdate series, Trigonometry (A14) |
| Observable Signatures of Competitive Civilizations | science philosophy | Unselected A101 candidate. What observational evidence would distinguish competitive expansion from natural astrophysical processes. Connects Dyson sphere searches and SETI to the competitive framework. | A98, A99, A100, A101 |
| The Survival Bottleneck Engineering Roadmap | science philosophy | Unselected A101 candidate. Detailed engineering requirements for the Type 0 to Type I transition. Covered adequately in A100 but could be expanded with specific technology roadmaps and quantitative risk reduction strategies. | A100 |
| Self-Replicating Technology Engineering | science philosophy | Unselected A101 candidate. Detailed engineering analysis of self-replicating machines and spacecraft. Von Neumann universal constructor, error correction, gray goo risk quantification. Implementation-focused rather than strategic. | A100, A101 |
| Governance Coherence Deep Dive | science philosophy | Unselected A101 candidate. Full treatment of governance coherence half-life, myth-structure transition, and institutional degradation at cosmic scales. A92 already covers this but the competitive context from A98-A101 would add depth. | A87, A89, A92, A100 |
| Economics of Competitive Expansion | science philosophy | Unselected A101 candidate. Resource allocation, opportunity costs, and economic optimization under competitive expansion imperatives. Interesting but secondary to physical feasibility questions. | A98, A100 |
| First Contact Protocols Under Competitive Assumptions | science philosophy | Unselected A101 candidate. Decision-theoretic analysis of first contact under the competitive framework. Premature without knowing whether force projection is physically feasible, which A101 now addresses. | A98, A99, A101 |
