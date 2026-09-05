---
layout: post
mathjax: true
comments: true
title:  "X-Planes: Boeing X-53 Active Aeroelastic Wing"
date:   2025-11-28 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 54
---
<!-- A350 -->
<script>console.log("A350");</script>

**Every aeroplane's wing bends, and for a century the engineering answer has been to make it bend less.** The X-53 was built to ask whether it could be made to bend usefully instead, by twisting a deliberately flexible wing with its leading-edge flaps and rolling the aeroplane on the twist [[Active Aeroelastic Wing Flight Research, NASA Facts FS-2005-03-061 DFRC][ref_aaw_factsheet]].

This is the fifty-fourth article in the [X-Planes series][related_post_a297_framing], following the [X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], the [X-4][related_post_a301_northrop_x4], the [X-5][related_post_a302_bell_x5], the [X-6][related_post_a303_convair_x6], the [X-7][related_post_a304_lockheed_x7], the [X-8][related_post_a305_aerojet_x8], the [X-9][related_post_a306_bell_x9], the [X-10][related_post_a307_north_american_x10], the [X-11][related_post_a308_convair_x11], the [X-12][related_post_a309_convair_x12], the [X-13][related_post_a310_ryan_x13], the [X-14][related_post_a311_bell_x14], the [X-15][related_post_a312_north_american_x15], the [X-16][related_post_a313_bell_x16], the [X-17][related_post_a314_lockheed_x17], the [X-18][related_post_a315_hiller_x18], the [X-19][related_post_a316_curtiss_wright_x19], the [X-20][related_post_a317_boeing_x20], the [X-21][related_post_a318_northrop_x21], the [X-22][related_post_a319_bell_x22], the [X-23][related_post_a320_martin_marietta_x23], the [X-24][related_post_a321_martin_marietta_x24], the [X-25][related_post_a322_bensen_x25], the [X-26][related_post_a323_schweizer_x26], the [X-27][related_post_a324_lockheed_x27], the [X-28][related_post_a325_osprey_x28], the [X-29][related_post_a326_grumman_x29], the [X-30][related_post_a327_rockwell_x30], the [X-31][related_post_a328_rockwell_mbb_x31], the [X-32][related_post_a329_boeing_x32], the [X-33][related_post_a330_lockheed_martin_x33], the [X-34][related_post_a331_orbital_sciences_x34], the [X-35][related_post_a332_lockheed_martin_x35], the [X-36][related_post_a333_mcdonnell_douglas_x36], the [X-37][related_post_a334_boeing_x37], the [X-38][related_post_a335_scaled_composites_x38], the [X-39][related_post_a336_x39_reserved_never_assigned], the [X-40][related_post_a337_boeing_x40], the [X-41][related_post_a338_x41_common_aero_vehicle], the [X-42][related_post_a339_orbital_sciences_x42], the [X-43][related_post_a340_micro_craft_x43], the [X-44][related_post_a341_x44_two_aircraft], the [X-45][related_post_a342_boeing_x45], the [X-46][related_post_a343_boeing_x46], the [X-47][related_post_a344_northrop_grumman_x47], the [X-48][related_post_a345_boeing_x48], the [X-49][related_post_a346_piasecki_x49], the [X-50][related_post_a347_boeing_x50], the [X-51][related_post_a348_boeing_x51], and the [X-52][related_post_a349_x52_designation_refused].

**It worked, and it did not reach the condition it was named for.**

**The aeroplane got its designation on 16 August 2006, more than a year after it had stopped flying**, and it got the number 53 because the number 52 had been refused a few months earlier by the office that allocates them [[Boeing X-53 Active Aeroelastic Wing][ref_x53_wikipedia]] [[Missing USAF and DOD Aircraft Designations][ref_missing_mds]] [[Allocation of Official Aerospace Vehicle MDS Designations][ref_mds_allocation]]. **The previous article in this series is about that refusal** [[X-Planes: X-52, the Designation Refused][related_post_a349_x52_designation_refused]]. This one is about the aeroplane that took the number, and it is the first vehicle in three articles.

## The Research Question

**A trailing-edge control surface fights the wing it is mounted on.**

Deflect an aileron down and it does two things. It increases the camber of the section, which is the effect the pilot wants, and it produces a nose-down pitching moment about the wing's elastic axis, which twists the wing leading-edge down. **That twist reduces the local angle of attack across the whole outer wing**, while the camber change acts only over the surface's own span, so the two effects are not competing over the same piece of wing.

**Both effects grow with dynamic pressure and they grow at different rates.** The camber effect is roughly linear in dynamic pressure. The twist effect is linear in dynamic pressure as well but divided by a structural stiffness that does not change, so as speed rises the twist wins. **At some dynamic pressure the two cancel exactly and the aileron produces no rolling moment at all. Above it the aeroplane rolls the wrong way** [[Bisplinghoff, Aeroelasticity][book_bisplinghoff]] [[Fung, An introduction to the theory of aeroelasticity][book_fung]].

**That condition is aileron reversal and it has been understood since the 1930s.** The classical answer is torsional stiffness, and the design charts for choosing it were published by the national advisory committee before the war ended [[Charts for the determination of wing torsional stiffness required for specified rolling characteristics][research_charts_torsional_stiffness]] [[Calculation of the lateral control of swept and unswept flexible wings of arbitrary stiffness][research_lateral_control_flexible]] [[Determination of the effect of wing flexibility on lateral manoeuvrability][research_wing_flexibility_lateral]] [[The development of a lateral-control system for use with large-span flaps][research_lateral_control_large_flaps]].

**That literature is older than the jet engine and it was not superseded.** It sized wings by asking how much torsional stiffness a specified rolling performance required, and the answer it gave has been built into every fast aeroplane since [[Rolling effectiveness and aileron reversal of rectangular wings at supersonic speeds][research_supersonic_aileron_reversal]].

**Torsional stiffness is weight.** That is the whole of the problem. A wing stiff enough to keep its ailerons working at the corner of the envelope is heavier than the aerodynamics require everywhere else in it.

**That sentence is a relation and it is worth writing down.** For a thin-walled torsion box of enclosed
area $A$, skin thickness $t$ and perimeter $\oint \mathrm{d}s$, the Bredt-Batho result gives a torsional
rigidity [[Megson, Aircraft structures for engineering students][book_megson]] [[Hodges and Pierce, Introduction to structural dynamics and aeroelasticity][book_hodges_pierce]]

$$GJ \;=\; \frac{4 A^{2} G\, t}{\oint \mathrm{d}s},$$

while the mass of that skin per unit span is

$$m' \;=\; \rho_{s}\, t \oint \mathrm{d}s .$$

**Both are linear in the same thickness**, so eliminating it,

$$GJ \;=\; \frac{4 A^{2} G}{\bigl( \oint \mathrm{d}s \bigr)^{2}} \cdot \frac{m'}{\rho_{s}}
\qquad\Longrightarrow\qquad GJ \;\propto\; m' .$$

**And the reversal dynamic pressure is proportional to torsional stiffness.** So to first order

$$q_{R} \;\propto\; K_\theta \;\propto\; GJ \;\propto\; m',$$

which is the whole problem in one line. **Reversal margin is bought linearly in structural mass**, and
it is bought at the corner of the envelope and carried everywhere else in it.

**The X-53 asks a question about the sign of the twist rather than its magnitude.** A leading-edge flap deflected down also twists the wing, and it twists it the other way, because its hinge is ahead of the elastic axis rather than behind it. **A leading-edge surface twists the wing into the airflow instead of out of it.** So the same flexibility that destroys a trailing-edge surface's authority amplifies a leading-edge surface's.

**The keystone is therefore this.** Can a flight control system be given a deliberately flexible wing and a set of leading- and trailing-edge surfaces, and told to produce roll by choosing how to twist the wing, rather than by fighting the twist?

**If it can, the stiffness comes out and the weight comes out with it.** The programme's own estimate is that a wing designed this way could be **10 to 20 percent lighter** [[Active Aeroelastic Wing Flight Research, NASA Facts FS-2005-03-061 DFRC][ref_aaw_factsheet]].

## Programme Origin

**The flight research centre subtitled its own account of this programme `Back to the Future`, and it opens on the Wright brothers.**

**Orville Wright had no ailerons.** The Wright Flyer rolled by warping its wingtips, through cables running to a saddle the pilot lay in, so that moving his hips twisted the wings [[Wing Warping][ref_wing_warping]] [[Wright Flyer][ref_wright_flyer]] [[Active Aeroelastic Wing Flight Research, NASA Facts FS-2005-03-061 DFRC][ref_aaw_factsheet]]. **The structure was the control surface.**

**Wing warping did not survive the speeds that followed it**, because a structure light enough to twist deliberately is a structure that twists when it is not asked to, and the discrete hinged surface won on stiffness. **The claim in the programme's title is that computing power changes that trade**, since a control law can now decide how to twist a wing many times a second and a pilot's hips could not [[Aeroelasticity][ref_aeroelasticity]] [[Aileron Reversal][ref_aileron_reversal]].

**The idea flew in a wind tunnel for nine years before it flew in the air.** Design and wind-tunnel studies ran from 1984 to 1993 under the name Active Flexible Wing, and that programme was more ambitious than the one that eventually flew. **The sponsor was not the laboratory that sponsored the flight programme**, because it did not exist yet. The early work came out of the Flight Dynamics Laboratory of the Air Force Wright Aeronautical Laboratories, which was folded into the Air Force Research Laboratory only in 1997, a year after the flight programme began [[Air Force Research Laboratory][ref_afrl]]. It included active flutter suppression, manoeuvre load alleviation, and roll control from multiple leading- and trailing-edge surfaces, all on a dynamically scaled model in a tunnel [[An overview of the active flexible wing program][research_afw_overview]] [[A summary of the active flexible wing program][research_afw_summary]] [[The active flexible wing aeroservoelastic wind-tunnel test program][research_afw_wind_tunnel]] [[Flutter suppression control law synthesis for the active flexible wing model][research_afw_flutter_suppression]] [[Roll plus maneuver load alleviation control system designs for the active flexible wing][research_afw_roll_mla]] [[Aeroservoelastic wind-tunnel investigations using the active flexible wing model, status and recent accomplishments][research_afw_tm101570]] [[Summary of an active flexible wing program][research_afw_technology_summary]] [[Simulation and model reduction for the active flexible wing program][research_afw_simulation_reduction]] [[A flutter suppression system using strain gages applied to active flexible wing technology][research_afw_flutter_strain_gauge]].

**It had candidate aeroplanes long before it had a testbed.** The concept was worked against an F-16 derivative wing and against the Agile Falcon, and neither of them flew it [[An application of the active flexible wing concept to an F-16 derivative wing][research_afw_f16_derivative]] [[Application of active flexible wing technology to the Agile Falcon][research_agile_falcon]].

**The flight programme began in 1996 at the flight research centre at Edwards, and dropped the hardest of those objectives at the outset** [[NASA Armstrong Flight Research Center][ref_armstrong]] [[F/A-18 Active Aeroelastic Wing, NASA][ref_nasa_x53]]. Its central objective was reduced to developing flight control laws that integrate aerodynamic and structural flexibility on a full-scale aeroplane, **while removing the requirement for active flutter suppression** [[Flight test of the F/A-18 active aeroelastic wing airplane][research_aaw_flight_test]] [[A flight research program for active aeroelastic wing technology][research_aaw_flight_research_plan]] [[Active aeroelastic wing flight research program, technical program and model analytical development][research_aaw_technical_program]].

**That deletion is the reason a manned aeroplane could fly this at all.** An aeroplane whose flutter margin depends on a working control law is an aeroplane that a control law failure destroys.

### Four Requirements, Two of Which Did Not Survive

The programme set four requirements for whatever aeroplane would host it [[Flight test of the F/A-18 active aeroelastic wing airplane][research_aaw_flight_test]].

1. **Subsonic and supersonic capability.**
2. **At least two trailing-edge and two leading-edge control surfaces on the wing.**
3. **Wing geometry and elastic characteristics that exhibit trailing-edge roll control reversal.**
4. **Provision to study external stores carriage and launch.**

**The fourth was deleted.** **The third was effectively deleted as well, after early flight tests showed it could not be met.** The programme kept its first two requirements and abandoned the one that named it.

### The Aeroplane Was Assembled From Two Aeroplanes and Then Deliberately Weakened

**The testbed is an F/A-18A, and it is two aircraft.** The Navy supplied the airframe, tail number 853. The space agency supplied wings from an early prototype, tail number 840, which had previously flown on the high angle of attack research vehicle [[Flight test of the F/A-18 active aeroelastic wing airplane][research_aaw_flight_test]] [[High Alpha Research Vehicle][ref_harv]] [[The F-18 high alpha research vehicle, a high-angle-of-attack testbed aircraft][research_harv_testbed]].

**The F/A-18 was chosen because it already had the defect.** Derived from the Northrop YF-17, it used a thin and flexible wing, and full-scale development flight tests showed degraded roll performance transonically and supersonically, though no flutter [[McDonnell Douglas F/A-18 Hornet][ref_fa18]] [[Northrop YF-17][ref_yf17]]. The contractor fixed it with two roll modifications that stiffened the wing box and rewrote how the control laws used the trailing-edge flaps, the ailerons and the leading-edge flaps. **Production F/A-18 control laws also lean heavily on the differential stabilator for roll at those conditions**, which is to say the fleet solved the problem by rolling with the tail.

**Boeing's Phantom Works then undid the fix.** Specially built wing covers returned the wing to essentially its preproduction torsional stiffness [[Wing torsional stiffness tests of the active aeroelastic wing F/A-18 airplane][research_aaw_torsional_stiffness]] [[Phantom Works][ref_phantom_works]].

**The X-53 is a production fighter with its stiffening removed on purpose**, which is the most direct statement of the programme's thesis that anything in the record makes.

## Sizing From First Principles

**Everything in this article is a claim about dynamic pressure**, because that is the variable the reversal condition is defined on. For air density $\rho$ and true airspeed $V$,

$$q \;=\; \tfrac{1}{2} \rho V^{2},$$

and since $V = M a$ with $a$ the local speed of sound, a Mach number and an altitude together fix it [[Dynamic Pressure][ref_dynamic_pressure]] [[U.S. Standard Atmosphere][ref_us_standard_atmosphere_ref]].

### The Reversal Condition

**Take a typical section with torsional stiffness $K_\theta$ about its elastic axis, reference area $S$ and chord $c$.** Deflecting a trailing-edge surface by $\delta$ produces a pitching moment about the aerodynamic centre with derivative $C_{m,\delta}$, which is negative for a trailing-edge surface deflected down. That moment twists the section by $\theta$, and the twist itself generates lift with slope $C_{L,\alpha}$ acting at a distance $e$ ahead of the elastic axis, which feeds back.

Equilibrium of moments about the elastic axis gives

$$K_\theta \,\theta \;=\; q S c \, C_{m,\delta}\, \delta \;+\; q S e \, C_{L,\alpha}\, \theta ,$$

so that

$$\theta \;=\; \frac{q S c \, C_{m,\delta}\, \delta}{K_\theta \;-\; q S e \, C_{L,\alpha}} .$$

**The denominator vanishing is divergence**, which is the other classical aeroelastic limit and which the programme stayed well clear of,

$$q_{D} \;=\; \frac{K_\theta}{S e \, C_{L,\alpha}} .$$

**The lift the surface actually delivers is the camber term plus the twist term,**

$$\Delta L \;=\; q S \bigl( C_{L,\delta}\, \delta \;+\; C_{L,\alpha}\, \theta \bigr),$$

and setting that to zero and substituting the twist gives the reversal dynamic pressure,

$$q_{R} \;=\; \frac{C_{L,\delta}\, K_\theta}{S \, C_{L,\alpha} \bigl( e\, C_{L,\delta} \;-\; c\, C_{m,\delta} \bigr)} ,$$

which is positive because $C_{m,\delta}$ is negative and the bracket is therefore positive.

**The bracket is usually reduced.** The flap's own lift acting at the offset $e$ is small beside its pitching moment acting on the chord, so $e\,C_{L,\delta} \ll -c\,C_{m,\delta}$ and the textbook form drops it,

$$q_{R} \;\approx\; \frac{-\,C_{L,\delta}\, K_\theta}{S c \, C_{L,\alpha} C_{m,\delta}} .$$

**The article uses the reduced form and says that it is reduced**, because the dropped term is the one that makes the expression exact rather than the one that makes it useful.

**The rolling effectiveness of a trailing-edge surface then falls linearly toward it,**

$$\frac{C_{l,\delta}(q)}{C_{l,\delta}(0)} \;=\; 1 \;-\; \frac{q}{q_{R}},$$

reaching zero at $q_R$ and going negative above it [[Bisplinghoff, Aeroelasticity][book_bisplinghoff]] [[Hodges and Pierce, Introduction to structural dynamics and aeroelasticity][book_hodges_pierce]] [[Wright and Cooper, Introduction to aircraft aeroelasticity and loads][book_wright_cooper]] [[Etkin and Reid, Dynamics of flight][book_etkin_reid]].

**Two things in that expression are worth reading carefully.** $q_R$ is proportional to $K_\theta$, so buying reversal margin means buying stiffness. And $q_R$ does not depend on the surface's own lift effectiveness alone but on the ratio of its lift to its pitching moment, **so a surface that produces its lift with less pitching moment reverses later**.

**A third is worth more than either, and it appears only when the two limits are divided.** Taking the
reduced reversal expression against the divergence expression, the stiffness cancels,

$$\frac{q_{R}}{q_{D}} \;=\;
\frac{-\,C_{L,\delta}\, K_\theta}{S c \, C_{L,\alpha} C_{m,\delta}}
\cdot \frac{S e \, C_{L,\alpha}}{K_\theta}
\;=\; \frac{-\,C_{L,\delta}\, e}{c \, C_{m,\delta}} .$$

**$K_\theta$ is gone.** Whether a wing reverses before it diverges is fixed by its aerodynamics and by
where its elastic axis sits, and **stiffening the wing moves both limits together and changes neither's
order**. A designer can push reversal further out in absolute terms and cannot push it past divergence
by that means.

**For a conventional wing that ratio comes out below one**, with a flap lift slope of order two to
three per radian, a flap pitching moment of order half that, and an elastic axis a tenth of a chord or
so behind the aerodynamic centre. **That is why reversal is the limit that gets designed against and
divergence is the one that gets checked**, and it is why this article is about the first and mentions
the second once. The programme stayed clear of both.

### The Leading-Edge Surface Has the Opposite Sign

**A leading-edge flap deflected down hinges ahead of the elastic axis**, so its pitching-moment derivative about that axis takes the opposite sign. The camber contribution is small and the twist contribution dominates, and the twist is now nose-up rather than nose-down.

**The consequence is stated most cleanly as a pair of limits.** As torsional stiffness falls, a trailing-edge surface loses authority and a leading-edge surface gains it,

$$\frac{\partial\, C_{l,\delta}^{\mathrm{TE}}}{\partial K_\theta} \;>\; 0
\qquad\text{against}\qquad
\frac{\partial\, C_{l,\delta}^{\mathrm{LE}}}{\partial K_\theta} \;<\; 0 ,$$

with the trailing-edge surface recovering its authority as the wing is stiffened and the leading-edge surface losing it.

**A stiff wing wants trailing-edge surfaces and a flexible wing wants leading-edge ones**, and the flight test report says exactly this in words, recording that leading-edge surfaces exhibit no reversal tendency and that their roll effectiveness rises proportionally as torsional stiffness falls [[Flight test of the F/A-18 active aeroelastic wing airplane][research_aaw_flight_test]].

### The Four Regions

**The programme's own framing divides the dynamic-pressure axis into four regions**, and the whole flight test can be read off them [[Flight test of the F/A-18 active aeroelastic wing airplane][research_aaw_flight_test]].

| Region | Trailing edge | Leading edge |
|---|---|---|
| I | paramount | ineffective |
| II | effective | equally effective |
| III | effectiveness has gone to zero | generates all rolling moment |
| IV | **reversed** | generates even larger rolling moment |

**Region IV is the condition the aeroplane is named for.** It is where a flexible wing stops being a liability and becomes an advantage, because the trailing-edge surface can be used backwards while the leading-edge surface does the work.

**The boundaries are conditions on dynamic pressure and can be written as such.** Writing
$\eta_{\mathrm{TE}}(q)$ and $\eta_{\mathrm{LE}}(q)$ for the two rolling effectivenesses,

$$\text{region} \;=\;
\begin{cases}
\mathrm{I}, & \eta_{\mathrm{LE}} \approx 0, \\[2pt]
\mathrm{II}, & \eta_{\mathrm{LE}} \approx \eta_{\mathrm{TE}} > 0, \\[2pt]
\mathrm{III}, & \eta_{\mathrm{TE}} = 0 \ \text{ and } \ \eta_{\mathrm{LE}} > 0, \\[2pt]
\mathrm{IV}, & \eta_{\mathrm{TE}} < 0 ,
\end{cases}$$

so that the boundary between III and IV is $q = q_{R}$ exactly. **Region III is a point in the simple
model and a band in a real wing**, because a wing has a spanwise distribution of stiffness and its
sections do not all reverse at once.

## Dependent Systems

### The Leading-Edge Flap Had to Be Cut in Half

**A production F/A-18 leading-edge flap is one surface per wing driven by one rotary actuator.** The X-53 splits it, retaining the existing hydraulic drive unit for the inboard section and adding a second power drive unit in each wing leading edge for the outboard section [[Flight test of the F/A-18 active aeroelastic wing airplane][research_aaw_flight_test]].

**The outboard flap also had to move three times faster.** The inboard surface retains a rate limit of 15 degrees per second and the outboard surface gets 45, against the aileron's 100. **Every figure in the table below is the report's** [[Flight test of the F/A-18 active aeroelastic wing airplane][research_aaw_flight_test]].

| Surface | Position limits, degrees | Rate limit, degrees per second |
|---|---|---|
| Aileron | 45 down, 25 up | 100 |
| Trailing-edge flap | 45 down, 8 up | 18 |
| Inboard leading-edge flap | 34 down, 5 up | 15 |
| Outboard leading-edge flap | 34 down, 10 up | 45 |

**A leading-edge flap failure on an F/A-18 has cost aircraft**, and the report gives fleet experience of leading-edge flap failures resulting in loss of control as the reason, so each drive system received an asymmetry control unit that locks its flap on a position mismatch or an overspeed, with a deliberate slip feature so that locking the brake could not fail the shaft catastrophically [[Flight test of the F/A-18 active aeroelastic wing airplane][research_aaw_flight_test]].

### The Aileron Became the Limiting Component and Stayed That Way

**Its structural limit is about 50,000 inch-pounds of hinge moment in one direction and 52,000 in the other**, and the flight test report records that **the aileron hinge moment was a design driver for the flight control system** and that it dominated concerns throughout the second phase of flight test, even after everything the design effort had given it.

**That is worth pausing on.** The aeroplane exists to demonstrate that the trailing edge need not carry the roll, and the trailing edge's hinge moment is nonetheless what constrained the whole test programme.

**A hinge moment is a dynamic pressure times a geometry times a coefficient,**

$$H \;=\; q\, S_{f}\, \bar{c}_{f} \bigl( C_{h,\alpha}\, \alpha \;+\; C_{h,\delta}\, \delta \bigr),$$

for a surface of area $S_{f}$ and mean chord $\bar{c}_{f}$ aft of its hinge. **It grows with dynamic
pressure exactly as the twist that drives reversal does**, so the corner of the envelope where the
technology becomes interesting is the same corner where the surface becomes hardest to hold.

**The actuator's side of that contest is a force on a lever,**

$$M_{\mathrm{act}} \;=\; F \, r ,$$

and the report's own table gives the force, the arm and the structural limit in adjacent columns,
without ever multiplying the first two together.

**Multiplying them is alarming.** The aileron actuator delivers

$$M_{\mathrm{act}} \;=\; 13{,}100\ \text{lb} \times 4.0\ \text{in}
\;=\; 52{,}400\ \text{in-lb}
\qquad\text{against a structural limit of}\qquad 50{,}000\ \text{in-lb},$$

which exceeds it by 4.8 percent. **The trailing-edge flap exceeds its own limit by
4.4 percent on the same arithmetic, and the inboard leading-edge flap's rotary actuator
exceeds its negative limit by 38.7 percent.**

**Three of the four wing surfaces carry actuators strong enough to break their own structural limits**,
and only the outboard leading-edge flap cannot. **That is why the flight test was run the way it was**,
with a build-up in lateral stick through 25, 50, 75 and 100 percent, a real-time envelope display, an
aural disengage tone and a test conductor authorised to call a manoeuvre off before the pilot reached a
boundary. **The structure was not protected by the actuator. It was protected by procedure.**

### Two Design Teams Solved Two Different Optimisation Problems

**The space agency and the manufacturer each wrote a full set of control laws**, deliberately, so that the project would have design options and so the test team would understand the problem [[Development and testing of control laws for the active aeroelastic wing program][research_aaw_control_laws]].

**They optimised dual problems.** The agency's tool maximised roll rate subject to every other requirement as an explicit constraint. The manufacturer's process minimised structural loads subject to a roll performance constraint, which then required a post-design check of everything else. **One asked how fast it could roll without breaking. The other asked how little it could break while rolling fast enough.**

**Neither designed a control law for the whole envelope.** To keep costs down the programme treated each of its **18 test points as a separate design point**, with its own gains, its own arming envelope in static and impact pressure, and its own disengage envelope.

### The Aeroplane Had to Measure Itself Before It Could Be Designed For

**About 200 strain-gauge bridges** were installed and calibrated across both wings, covering wing-root and wing-fold shear, torsion and bending, plus every wing control surface actuator hinge moment. **Redundant load equations were calibrated deliberately**, so that a gauge failing after flight test began would not cost the measurement [[Strain gage loads calibration testing of the active aeroelastic wing F/A-18 aircraft][research_strain_gage_calibration]] [[Deflection-based structural loads estimation from the active aeroelastic wing F/A-18 aircraft][research_aaw_deflection_loads]] [[Loads model development and analysis for the F/A-18 active aeroelastic wing airplane][research_aaw_loads_model]] [[Deflection-based aircraft structural loads estimation with comparison to flight][research_deflection_loads_flight]].

**A flight deflection measurement system returned a 16-point wing shape at 12.5 samples per second**, calibrated on the ground against string potentiometers [[Twist model development and results from the active aeroelastic wing F/A-18 aircraft][research_aaw_twist_model]] [[In-flight deflection measurement of the HiMAT aeroelastically tailored wing][research_himat_deflection]].

**A research noseboom was fitted because the production air data was not good enough to model with.** The basic flight control system uses uncalibrated static and impact pressures for gain scheduling, and those carry large altitude and Mach errors at low supersonic conditions.

## The Flight Test Record

**Phase I ran from November 2002 to June 2003 and comprised 51 flights.** Its three objectives were to prove the modified aeroplane was flutter free, to demonstrate the low-speed characteristics of the worst-case outboard leading-edge flap failure, and to gather data for flight-derived aerodynamic and loads models using an onboard excitation system [[Flight test of the F/A-18 active aeroelastic wing airplane][research_aaw_flight_test]] [[Active aeroelastic wing aerodynamic model development and validation for a modified F/A-18A][research_aaw_aero_model]].

**Phase II ran from December 2004 to March 2005 and comprised 35 flights.** It flew the new control laws at the 18 test points, with a build-up through 25, 50, 75 and 100 percent lateral stick in bank-to-bank and 360 degree rolls and in rolling pull-outs.

**Between them lay about a year of analysis and control law redesign.** From programme kickoff to last flight was nearly ten years.

### Two Test Points Were Never Flown, and Their Dynamic Pressures Say Why

**The aeroplane could not reach the two highest-dynamic-pressure test points.** Mach 1.3 at 15,000 feet and Mach 1.2 at 10,000 feet both proved to be outside its performance envelope. The report suggests why, and the reason is the research equipment itself, naming the external deflection-measurement targets, the external wiring, the wing surface pressure instrumentation and the camera pods as likely contributors to additional drag.

**Computing the dynamic pressure at each of them shows what was lost.** Taking the standard atmosphere and $q = \tfrac{1}{2}\rho V^2$,

$$q(1.2,\ 15{,}000\ \text{ft}) \;\approx\; 1{,}204\ \text{psf}
\qquad\text{against}\qquad
q(1.3,\ 15{,}000\ \text{ft}) \;\approx\; 1{,}413\ \text{psf},$$

$$q(1.2,\ 10{,}000\ \text{ft}) \;\approx\; 1{,}467\ \text{psf}.$$

**The report's illustration of the four regions plots its dynamic-pressure axis from 600 to 1,400 pounds per square foot and puts the reversal crossing near the right-hand end of it.** **That figure is captioned as a typical fighter and not as the X-53**, so it fixes no reversal value for this aeroplane and the article claims none.

**What it does fix is the scale of the thing**, and on that scale the two test points the aeroplane could not reach are the only two that lie beyond the axis entirely. **The aeroplane could not get to the corner of the envelope where the phenomenon it is named for is drawn**, and the instrumentation that made it a research aeroplane is part of why.

**The shortfall is better stated as a ratio than as a gap.** Against the highest point actually flown,

$$\frac{q(1.3,\ 15{,}000)}{q(1.2,\ 15{,}000)} \;\approx\; 1.174
\qquad\text{and}\qquad
\frac{q(1.2,\ 10{,}000)}{q(1.2,\ 15{,}000)} \;\approx\; 1.219,$$

so the aeroplane was short of its two unflown conditions by 17.4 and
21.9 percent of dynamic pressure. **That is not a near miss and it is not a wide
one**, and on a body whose drag rises steeply through this part of the envelope it is the difference
between a level-flight test point and a shallow dive that was never cleared.

### The Aileron Never Reversed

**Phase I showed no tendency for the aileron to fully reverse.** The report states that the aileron roll control moments approached zero and stayed there, without changing sign.

**The report offers a mechanism and does not claim it.** Control position transducers on the surfaces indicated that **substantial control surface flexibility** might have provided elastic relief of the hinge moment the surfaces were applying to the wing. **The aileron, acting as a tab on a flexible wing, was itself bending**, which would reduce the very twisting moment that drives reversal.

**So the aeroplane reached region III and stopped there.** It reached the condition where the trailing edge does nothing, and never reached the one where the trailing edge works backwards.

### Roll Performance Met Its Goal Twice and Missed Its Requirement Once

**Roll rate and roll-mode time constant are the two numbers the criteria are written on, and both come
from one equation.** For roll inertia $I_{x}$, span $b$, control derivative $C_{l,\delta}$ and damping
derivative $C_{l,p}$, which is negative,

$$I_{x}\, \dot{p} \;=\; q S b \left( C_{l,\delta}\, \delta \;+\; C_{l,p}\, \frac{p b}{2V} \right).$$

**Steady state gives the helix angle**, which is the classical measure of rolling power and which is
independent of dynamic pressure for a rigid wing,

$$\frac{p_{\mathrm{ss}} b}{2V} \;=\; -\,\frac{C_{l,\delta}}{C_{l,p}}\, \delta .$$

**On a flexible wing $C_{l,\delta}$ is the quantity that decays toward reversal**, so the helix angle
decays with it, which is the same statement as the effectiveness ratio above wearing different clothes.

**The transient gives the time constant,**

$$\tau_{R} \;=\; -\,\frac{2 I_{x} V}{q S b^{2} C_{l,p}}
\;=\; -\,\frac{4 I_{x}}{\rho V S b^{2} C_{l,p}} ,$$

**so the roll mode gets faster as speed rises**, falling like $1/V$ at fixed density. That is why the
measured constants are short and why a fast roll mode was a concern rather than a prize.

**Bank angle follows from integrating the first-order response,**

$$\phi(t) \;=\; p_{\mathrm{ss}} \Bigl[\, t \;-\; \tau_{R} \bigl( 1 - e^{-t/\tau_{R}} \bigr) \Bigr],$$

and a time-to-bank criterion is that expression inverted at a stated angle. **With time constants of
order a tenth of a second and criteria written at 50, 90 and 180 degrees, the exponential term is
negligible and time to bank is very nearly $\phi / p_{\mathrm{ss}}$**, which means the criteria were
testing roll rate and not roll damping.

**Time-to-bank criteria were drawn from the military handbook on flying qualities, with level 1 goals and level 2 requirements at bank angles of 50, 90 and 180 degrees.**

**At the subsonic region I test point and the supersonic region II test point, the control designs met the level 1 goal.** **At the subsonic region III test point, roll performance was inadequate to meet the level 2 requirement.**

**Region III is the region the whole programme was built for.** It is where the trailing edge has gone to zero and the leading edge is generating all of the rolling moment, which is precisely the regime in which a deliberately flexible wing is supposed to pay for itself. **It is also the one region where the aeroplane failed to meet even the lower of its two standards.**

**Roll-mode time constants were short everywhere**, at 0.18 seconds subsonic region I, 0.10 seconds subsonic region III and 0.60 seconds supersonic region II, against a level 1 limit of 1.0 seconds and a level 2 limit of 1.4.

**None of the three was near its upper limit.** The slowest, supersonic at 0.60 seconds, sits at

$$\frac{\tau_{\mathrm{level\,1}}}{\tau_{R}}
\;=\; \frac{1.0}{0.60} \;\approx\; 1.67,$$

**so even the slowest measured roll mode beat its level 1 goal by two thirds again.**

**The concern ran the other way.** Two of the three fell below the 0.3 second guideline that the programme wrote for itself out of concern about roll-ratchet pilot-induced oscillation, and its own requirements document allowed constants that quick provided they were no worse than the production control laws, which these were not. **A criterion written to catch an aeroplane that rolls too slowly had to be given a second end**, because this one rolled too readily.

### Overall Roll Rates Came Within Fifteen to Twenty Percent, Without the Tail

**Across the second phase, roll rates adequate for lateral control were obtained by active control of wing flexibility alone**, within 15 to 20 percent of a production F/A-18, **and without the differential rolling horizontal tail that a standard F/A-18 relies on at these conditions** [[Active Aeroelastic Wing Flight Research, NASA Facts FS-2005-03-061 DFRC][ref_aaw_factsheet]].

**Stated as a ratio,**

$$\frac{p_{\mathrm{AAW}}}{p_{\mathrm{prod}}}
\;\in\; \bigl[\, 0.80,\ 0.85 \,\bigr],$$

**and the aeroplane in the denominator is using a control effector the one in the numerator was not.**

**Roll rates at 15,000 feet were highest at Mach 0.85 and Mach 1.2 and lowest at Mach 0.95**, which is the same transonic dip a conventional F/A-18 shows, and which belongs to the shock rather than to the structure [[Shock location dominated transonic flight loads on the active aeroelastic wing][research_aaw_shock_loads]].

## What the Data Changed

**The concept was demonstrated at full scale and the demonstration is the result.** A fighter with its wing stiffening deliberately removed rolled acceptably using its wing surfaces alone, at transonic and supersonic conditions, on control laws designed from flight-derived models.

**The research flight control system worked in both phases**, and the programme records it as the first use of such a system on an F/A-18 in a safety-of-flight critical envelope. **The computer it ran on was not built for this programme**, being the production support flight control computer the flight research centre had already developed as a research capability for its F/A-18 fleet [[Production support flight control computers, research capability for F/A-18 aircraft at Dryden Flight Research Center][research_psfcc]].

**Prediction quality split by regime.** Comparison of Phase II flight data with predicted response showed excellent agreement supersonically and only fair agreement subsonically, with larger differences.

**One designed benefit did not appear.** The new control laws **failed to show load reduction at a subsonic region II test point at elevated normal acceleration** when compared against the production system, and examination showed the trailing-edge surfaces being driven in a manner inconsistent with manoeuvre load control strategies.

**And the models the control laws were designed on had been extrapolated.** The report records in hindsight that some of the Phase I excitation manoeuvres were too small, that significant extrapolation of the leading-edge flap control power was required, and that Phase II research control laws used **as much as five times larger outboard leading-edge flap motion** than the manoeuvres that had measured it.

## Where the Framing Breaks Down

**Calling this an aeroelasticity experiment understates how much of it was a control law experiment.** The programme dropped flutter suppression, dropped external stores, and could not reach reversal, and what remained was the design and flight clearance of eighteen point designs on an aeroplane whose aerodynamic model came from its own earlier flights.

**Calling the result a success without qualification overstates it.** Roll performance within 15 to 20 percent of production, achieved without the stabilator, is a real demonstration. Missing the level 2 requirement in region III is a real shortfall, and region III is the interesting region.

**And the weight saving was never weighed.** The 10 to 20 percent figure is a design estimate for a wing conceived this way from the start [[Active Aeroelastic Wing Flight Research, NASA Facts FS-2005-03-061 DFRC][ref_aaw_factsheet]] [[Raymer, Aircraft design, a conceptual approach][book_raymer]]. **The X-53 did not have such a wing.** It had a production wing with its stiffening removed and a research instrumentation fit added on top, which is the opposite transaction. **The record does not give the mass of that fit** and this article does not estimate one.

## The Contemporary Literature

## The Contemporary Literature

| Cluster | Records |
|---|---|
| Other aeronautical and structural literature | 526 |
| Flutter, and the instability this programme chose not to fly | 432 |
| Measuring a wing in the air | 400 |
| Shaping a wing so that it bends usefully | 383 |
| The flow over the wing at these speeds | 358 |
| Control laws for an aircraft that will not hold its shape | 354 |
| Static aeroelasticity, twist and divergence | 257 |
| Roll performance and how an aeroplane is judged to have enough | 220 |
| Load alleviation, which is the other thing a flexible wing can be asked to do | 198 |
| Wind tunnels, and the models that stood in for the aeroplane | 110 |
| The atmosphere and the flight condition | 47 |
| Control reversal, and the dynamic pressure at which a surface stops working | 22 |
| **Total** | **3,307** |

### Other aeronautical and structural literature

**The residual, reported and not hidden.** On-subject work belonging to no cluster above.

**526 records.** [[2-D Prototypical Aeroelastic Wing 2013][research_2_d_prototypical_2013]] [[2-D Prototypical Aeroelastic Wing 2018][research_2_d_prototypical_2018]] [[3-D Prototypical Aeroelastic Wing 2013][research_3_d_prototypical_2013]] [[3-D Prototypical Aeroelastic Wing 2018][research_3_d_prototypical_2018]] [[A summary of the active flexible wing program][research_afw_summary]] [[Abdallah 2018][research_abdallah_2018]] [[Abdallah et al 2013][research_abdallah_newman_2013]] [[Abdallah et al 2014][research_abdallah_newman_2014]] [[Achache and Whalley 1996][research_achache_whalley_1996]] [[Active aeroelastic wing aerodynamic model development and validation for a modified F/A-18A][research_aaw_aero_model]] [[Aeroelastic Control 2005][research_aeroelastic_control_2005]] [[Ahmad et al 2018][research_ahmad_baig_2018]] [[Akmese et al 2009][research_akmese_comert_2009]] [[Al-Shehabi and Newman 2000][research_alshehabi_newman_2000]] [[Al-Shehabi and Newman 2000][research_alshehabi_newman_2000_b]] [[Alighanbari and Lee 2003][research_alighanbari_lee_2003]] [[Allaire et al 2014][research_allaire_lecerf_2014]] [[Allen et al 2005][research_allen_lizotte_2005]] [[Alstrom et al 2010][research_alstrom_marzocca_2010]] [[An application of the active flexible wing concept to an F-16 derivative wing][research_afw_f16_derivative]] [[An et al 2023][research_an_zhu_2023]] [[An overview of the active flexible wing program][research_afw_overview]] [[Andersen et al 1996][research_andersen_forster_1996]] [[Anderson et al 2005][research_anderson_white_2005]] [[Application of active flexible wing technology to the Agile Falcon][research_agile_falcon]] [[Aravinth et al 2018][research_aravinth_shinde_2018]] [[Armanious and Lind 2018][research_armanious_lind_2018]] [[Babcock and Lind 2012][research_babcock_lind_2012]] [[Babcock and Lind 2012][research_babcock_lind_2012_b]] [[Badcock et al 2003][research_badcock_rampurawala_2003]] [[Bae and Lee 2002][research_bae_lee_2002]] [[Bae et al 2002][research_bae_yang_2002]] [[Bai et al 2022][research_bai_cao_2022]] [[Bajaj 2019][research_bajaj_2019]] [[Balakrishnan 2012][research_balakrishnan_2012]] [[Balas et al 2011][research_balas_seiler_2011]] [[Baranyi 2006][research_baranyi_2006]] [[Baranyi 2006][research_baranyi_2006_b]] [[Baranyi and Patton 2003][research_baranyi_patton_2003]] [[Baz et al 1987][research_baz_iman_1987]] [[Behal et al 2004][research_behal_marzocca_2004]] [[Behal et al 2006][research_behal_marzocca_2006]] [[Bhat 2018][research_bhat_2018_c]] [[Bhat 2018][research_bhat_2018_d]] [[Bichiou et al 2016][research_bichiou_hajj_2016]] [[Bielawa 2006][research_bielawa_2006]] [[Blair 1994][research_blair_1994]] [[Block and Strganac 1998][research_block_strganac_1998]] [[Block et al 1997][research_block_gilliatt_1997]] [[Bontoft et al 2026][research_bontoft_bhuwal_2026]] [[Bontoft et al 2026][research_bontoft_bhuwal_2026_b]] [[Bottasso and Montinari 2013][research_bottasso_montinari_2013]] [[Bove 2026][research_bove_2026]] [[Bramsiepe et al 2020][research_bramsiepe_voss_2020]] [[Bras et al 2022][research_bras_warwick_2022]] [[Braun et al 2003][research_braun_boucke_2003]] [[Brooks and Meyer 1995][research_brooks_meyer_1995]] [[Brown and Caverly 2021][research_brown_caverly_2021]] [[Brown and Singh 2015][research_brown_singh_2015]] [[Brown and Singh 2016][research_brown_singh_2016]] [[Bunge et al 2016][research_bunge_alkurdi_2016]] [[Burken et al 1986][research_burken_alag_1986]] [[Butler et al 1995][research_butler_lillico_1995]] [[Byun and Guruswamy 1994][research_byun_guruswamy_1994]] [[Byun and Guruswamy 1996][research_byun_guruswamy_1996_b]] [[Byun and Guruswamy 1996][research_byun_guruswamy_1996_c]] [[Calculation of Elastic Deformations 2004][research_calculation_of_2004]] [[Canfield 2014][research_canfield_2014]] [[Carlson and Cassarino 1973][research_carlson_cassarino_1973]] [[Cavagna et al 2009][research_cavagna_ricci_2009]] [[Cea and Palacios 2023][research_cea_palacios_2023]] [[Cea and Palacios 2024][research_cea_palacios_2024]] [[Celi 1994][research_celi_1994]] [[Cesnik et al 1999][research_cesnik_shin_1999]] [[Chajec et al 2019][research_chajec_krzymien_2019]] [[Chandre Vila][research_chandrevila]] [[Chapter 15. Aeroelastic Systems 1994][research_chapter_15_1994]] [[Chapter 2. Exploring the 2005][research_chapter_2_2005]] [[Chapter III Elastic Deformations 1982][research_chapter_iii_1982]] [[Chen et al 1998][research_chen_chang_1998]] [[Chen et al 2008][research_chen_baldelli_2008]] [[Cheng et al 2023][research_cheng_cea_2023]] [[Cizmas and Strganac 2010][research_cizmas_strganac_2010]] [[Cocco and Meroli 2026][research_cocco_meroli_2026]] [[Cole 1990][research_cole_1990]] [[Cole and Weiland 2009][research_cole_weiland_2009]] [[Conti et al 2021][research_conti_saltari_2021]] [[Cook and Smith 2014][research_cook_smith_2014]] [[Cord 1989][research_cord_1989]] [[Crane, H. L. and Reeder, J. P. 1945][research_cranehl_reederjp_1945]] [[Cumming and Diebler 2005][research_cumming_diebler_2005]] [[D'Vari and Baker 1999][research_dvari_baker_1999]] [[Dancila and Botez 2014][research_dancila_botez_2014]] [[Danowsky et al 2008][research_danowsky_thompson_2008]] [[Das et al 2021][research_das_venkatraman_2021]] [[Davis 1974][research_davis_1974]] [[de Visser 1999][research_devisser_1999]] [[de Visser et al 2009][research_devisser_mulder_2009]] [[Deflection-based aircraft structural loads estimation with comparison to flight][research_deflection_loads_flight]] [[Deflection-based structural loads estimation from the active aeroelastic wing F/A-18 aircraft][research_aaw_deflection_loads]] [[Dehaan 1990][research_dehaan_1990]] [[Demasi 2024][research_demasi_2024]] [[Demasi and Livne 2005][research_demasi_livne_2005]] [[Demenkov 2009][research_demenkov_2009]] [[Determination of the effect of wing flexibility on lateral manoeuvrability][research_wing_flexibility_lateral]] [[Dhital and Chouvion 2024][research_dhital_chouvion_2024]] [[Dias et al 2015][research_dias_demarqui_2015]] [[Dimitriadis 2008][research_dimitriadis_2008]] [[Dimitriadis 2011][research_dimitriadis_2011]] [[Dinyavari and Friedmann 1986][research_dinyavari_friedmann_1986]] [[Djojodihardjo 2023][research_djojodihardjo_2023]] [[Djojodihardjo 2023][research_djojodihardjo_2023_c]] [[Done 1996][research_done_1996]] [[Dowell 1983][research_dowell_1983]] [[Dowell et al 2006][research_dowell_attar_2006]] [[Dracopoulos and Oz 1992][research_dracopoulos_oz_1992]] [[Dracopoulos and Öz 1988][research_dracopoulos_oz_1988]] [[Dreier 1987][research_dreier_1987]] [[Durmaz and Kaya 2013][research_durmaz_kaya_2013]] [[Eckstrom and Spain 1982][research_eckstrom_spain_1982]] [[Efremov 1992][research_efremov_1992]] [[Epureanu 2001][research_epureanu_2001]] [[Exploring the Flight Envelope 2015][research_exploring_the_2015]] [[Fan and Hall 2014][research_fan_hall_2014]] [[Fan and Lutze 1996][research_fan_lutze_1996]] [[Farbridge et al 1956][research_farbridge_woodward_1956]] [[Farhat 2001][research_farhat_2001]] [[Farhat and Amsallem 2011][research_farhat_amsallem_2011]] [[Farhat and Lin 1990][research_farhat_lin_1990]] [[Fernandez Escudero][research_fernandezescudero]] [[Filippou et al 2024][research_filippou_kilimtzidis_2024]] [[Flight Envelope 2005][research_flight_envelope_2005]] [[Flight Envelope 2021][research_flight_envelope_2021]] [[Flight Envelope Awareness/Protection][research_flight_envelope]] [[Forster et al 1996][research_forster_kolonay_1996]] [[Fournier][research_fournier]] [[Frampton and Clark 1998][research_frampton_clark_1998]] [[Franklin 2018][research_franklin_2018]] [[Freidmann 2001][research_freidmann_2001]] [[Friedmann 1977][research_friedmann_1977]] [[Friedmann 1987][research_friedmann_1987]] [[Friedmann 1990][research_friedmann_1990]] [[Friedmann 2000][research_friedmann_2000]] [[Friedmann 2001][research_friedmann_2001]] [[Friedmann 2004][research_friedmann_2004]] [[Friedmann 2010][research_friedmann_2010]] [[Friedmann and Hodges 2003][research_friedmann_hodges_2003]] [[Friedmann and Hodges 2003][research_friedmann_hodges_2003_b]] [[Friedmann and Straub 1980][research_friedmann_straub_1980]] [[Gai and Seffen 2025][research_gai_seffen_2025]] [[Gandhi and Hathaway 1998][research_gandhi_hathaway_1998]] [[Ganguli and Chopra 1995][research_ganguli_chopra_1995]] [[Garcia 2005][research_garcia_2005]] [[Gasparetto][research_gasparetto]] [[Geisbauer 2011][research_geisbauer_2011]] [[Gennaretti 2024][research_gennaretti_2024]] [[Gern and Librescu 1998][research_gern_librescu_1998]] [[Ghosh and Raisinghani 1993][research_ghosh_raisinghani_1993]] [[Ghosh and Raisinghani 1994][research_ghosh_raisinghani_1994]] [[Giansante et al 2022][research_giansante_bernardini_2022]] [[Gilbert et al 1982][research_gilbert_schmidt_1982]] [[Gilbert et al 1984][research_gilbert_schmidt_1984]] [[Gimmestad 1979][research_gimmestad_1979]] [[Giunta 1999][research_giunta_1999]] [[Gobal and Grandhi 2015][research_gobal_grandhi_2015]] [[Gordnier and Attar 2012][research_gordnier_attar_2012]] [[Gratton 2014][research_gratton_2014]] [[Gratton 2018][research_gratton_2018]] [[Grauer 2016][research_grauer_2016]] [[Grauer and Morelli 2014][research_grauer_morelli_2014]] [[Graves et al 2002][research_graves_burner_2002]] [[Gray and Martins 2024][research_gray_martins_2024]] [[Greenwell 2004][research_greenwell_2004]] [[Griffin 2006][research_griffin_2006]] [[Gu et al 2024][research_gu_healy_2024]] [[Gu et al 2024][research_gu_healy_2024_b]] [[Gujjula and Singh 2005][research_gujjula_singh_2005]] [[Guo et al 2018][research_guo_cao_2018]] [[Gupta 1996][research_gupta_1996]] [[Guruswamy 1992][research_guruswamy_1992]] [[Gwin 1974][research_gwin_1974]] [[Gwin 1976][research_gwin_1976]] [[Haas and Chopra 1987][research_haas_chopra_1987]] [[Hablowetz 2000][research_hablowetz_2000]] [[Haddadpour et al 2005][research_haddadpour_shams_2005]] [[Hajj 2004][research_hajj_2004]] [[Halder and Benedict 2018][research_halder_benedict_2018]] [[Hanel 1998][research_hanel_1998]] [[Hartman 2019][research_hartman_2019]] [[Hess and Flick 2004][research_hess_flick_2004]] [[Hess and Hess 1997][research_hess_hess_1997]] [[Hilger and Ritter 2021][research_hilger_ritter_2021]] [[Hilton and Nguyen 2014][research_hilton_nguyen_2014]] [[Hjartarson et al 2014][research_hjartarson_seiler_2014]] [[Horn et al 1998][research_horn_calise_1998]] [[Hui et al 2000][research_hui_collins_2000]] [[Hui et al 2005][research_hui_auriti_2005]] [[Hussein et al 2025][research_hussein_rashid_2025]] [[Huttsell and Eastep 1989][research_huttsell_eastep_1989]] [[Iannacci and Mayo 1999][research_iannacci_mayo_1999]] [[Ifju et al 2001][research_ifju_waszak_2001]] [[Introduction to Aeroelastic Rotor 2018][research_introduction_to_2018]] [[Ippolito et al 2014][research_ippolito_ting_2014]] [[Ishihara and Nguyen 2014][research_ishihara_nguyen_2014]] [[Ishihara et al 2013][research_ishihara_nguyen_2013]] [[Jafari et al 2019][research_jafari_feizarefi_2019]] [[Jebakumar et al 2019][research_jebakumar_kumar_2019]] [[Jian and Jinwu 2009][research_jian_jinwu_2009]] [[Jiang and Li 2018][research_jiang_li_2018]] [[Jiang and Li 2018][research_jiang_li_2018_b]] [[Johnston and Cassarino 1976][research_johnston_cassarino_1976]] [[Jorge and Lind 2013][research_jorge_lind_2013]] [[Juliana et al 2004][research_juliana_chu_2004]] [[Kafkas et al 2021][research_kafkas_kilimtzidis_2021]] [[Karpouzian and Librescu 1994][research_karpouzian_librescu_1994]] [[Ke et al 2008][research_ke_zhigang_2008]] [[Kennedy and Martins 2013][research_kennedy_martins_2013]] [[Kholodar 2014][research_kholodar_2014]] [[Koo and Lee 1994][research_koo_lee_1994]] [[Kreshock et al 2016][research_kreshock_kang_2016]] [[Kroeger, R. A. 1977][research_kroegerra_1977]] [[Kurita et al 2019][research_kurita_koike_2019]] [[Kuttenkeuler and Ringertz 1998][research_kuttenkeuler_ringertz_1998]] [[Küssner 1959][research_kussner_1959]] [[Lazarus et al 1991][research_lazarus_crawley_1991]] [[Lazarus et al 1995][research_lazarus_crawley_1995]] [[Lee 1994][research_lee_1994]] [[Lee and Kim 1995][research_lee_kim_1995]] [[Lee and Singh 2006][research_lee_singh_2006]] [[Lee and Singh 2009][research_lee_singh_2009]] [[Lee and Singh 2018][research_lee_singh_2018]] [[Leijonhufvud and Karlsson 2011][research_leijonhufvud_karlsson_2011]] [[Lesoinne 2007][research_lesoinne_2007]] [[Lesoinne and Farhat 1993][research_lesoinne_farhat_1993]] [[Lesoinne and Farhat 1995][research_lesoinne_farhat_1995]] [[Lesoinne and Kaila 2005][research_lesoinne_kaila_2005]] [[Lesoinne et al 2001][research_lesoinne_balas_2001]] [[Li 2018][research_li_2018]] [[Li et al 2010][research_li_guo_2010]] [[Li et al 2010][research_li_guo_2010_b]] [[Li et al 2021][research_li_wan_2021]] [[Li et al 2025][research_li_zheng_2025]] [[Librescu and Beiner 1983][research_librescu_beiner_1983]] [[Limitations and Flight Envelope 2017][research_limitations_and_2017]] [[Lin and Crawley 1994][research_lin_crawley_1994]] [[Lin et al 1995][research_lin_crawley_1995]] [[Lin et al 1996][research_lin_crawley_1996]] [[Lind 1999][research_lind_1999]] [[Lind et al 1998][research_lind_freudinger_1998]] [[Lindsley 2009][research_lindsley_2009]] [[Liu 2019][research_liu_2019]] [[Liu et al 2024][research_liu_yang_2024]] [[Liu et al 2025][research_liu_fan_2025]] [[Livne 2001][research_livne_2001]] [[Livne 2010][research_livne_2010]] [[Lizotte, Andrew and Allen, Michael J. 2005][research_lizotteandrew_allenmichaelj_2005]] [[Loads model development and analysis for the F/A-18 active aeroelastic wing airplane][research_aaw_loads_model]] [[Loewy 1969][research_loewy_1969]] [[Loewy 2000][research_loewy_2000]] [[Lombaerts 2012][research_lombaerts_2012]] [[Loth et al 2000][research_loth_geubelle_2000]] [[Lowe and Zingg 2021][research_lowe_zingg_2021]] [[Lu and Murthy 1990][research_lu_murthy_1990]] [[Lukichev et al 2017][research_lukichev_demidova_2017]] [[Ma et al 2022][research_ma_wang_2022]] [[Maalawi 2012][research_maalawi_2012]] [[Mahmood 2025][research_mahmood_2025]] [[Mannarino and Mantegazza 2014][research_mannarino_mantegazza_2014]] [[Mardanpour and Rastkar 2017][research_mardanpour_rastkar_2017]] [[Mardanpour et al 2013][research_mardanpour_richards_2013]] [[Mardanpour et al 2014][research_mardanpour_richards_2014]] [[Mas Colomer][research_mascolomer]] [[Masarati et al 2016][research_masarati_tod_2016]] [[McGurk et al 2024][research_mcgurk_stodieck_2024]] [[McTavish][research_mctavish]] [[Mehrotra, S. C. 1980][research_mehrotrasc_1980]] [[Melville 2000][research_melville_2000]] [[Melville and Gordnier 1998][research_melville_gordnier_1998]] [[Methods of calculating the 2015][research_methods_of_calculating_2015]] [[Milanese et al 2008][research_milanese_marzocca_2008]] [[Missoum 2012][research_missoum_2012]] [[Mkhoyan et al 2022][research_mkhoyan_wang_2022]] [[Mocsányi et al 2019][research_mocsanyi_takarics_2019]] [[Mocsányi et al 2020][research_mocsanyi_takarics_2020]] [[Mohammadi 1999][research_mohammadi_1999]] [[Mohd et al 2025][research_mohd_amoozgar_2025]] [[Molusis and Kleinman 1982][research_molusis_kleinman_1982]] [[Mooij 2020][research_mooij_2020]] [[Mooij and Wang 2021][research_mooij_wang_2021]] [[Moravej Barzani et al 2022][research_moravejbarzani_shahverdi_2022]] [[Morino and Obayashi 2015][research_morino_obayashi_2015]] [[Moshier 2006][research_moshier_2006]] [[Moshtaghzadeh et al 2023][research_moshtaghzadeh_rangel_2023]] [[Moszczynski et al 2026][research_moszczynski_grant_2026]] [[Mukhopadhyay 2003][research_mukhopadhyay_2003]] [[Murphy and Mermagen 2004][research_murphy_mermagen_2004]] [[Murphy et al 2004][research_murphy_klein_2004]] [[Murthy and Lu 1992][research_murthy_lu_1992]] [[Muscarello et al 2017][research_muscarello_masarati_2017]] [[Naftaly and Raveh 2025][research_naftaly_raveh_2025]] [[Neumann et al 2020][research_neumann_dealmeida_2020]] [[Newman and Buttrill 1995][research_newman_buttrill_1995]] [[Newman and Kassem 1997][research_newman_kassem_1997_b]] [[Newman et al 1997][research_newman_kassem_1997]] [[Newman et al 1997][research_newman_kassem_1997_c]] [[Ng et al 2020][research_ng_ong_2020]] [[Nguyen and Tal 2015][research_nguyen_tal_2015]] [[Nguyen and Tuzcu 2009][research_nguyen_tuzcu_2009]] [[Nguyen et al 2011][research_nguyen_tuzcu_2011]] [[Nguyen et al 2013][research_nguyen_ting_2013_b]] [[Nguyen et al 2015][research_nguyen_ting_2015_b]] [[Nguyen et al 2016][research_nguyen_ting_2016]] [[Nguyen et al 2018][research_nguyen_reynolds_2018]] [[Niel][research_niel]] [[Nikolaos et al 2024][research_nikolaos_spyridon_2024]] [[Nixon 2020][research_nixon_2020]] [[Numerical calculation method and 2015][research_numerical_calculation_2015]] [[Numerical Method and Program 2013][research_numerical_method_2013]] [[Onkar et al 2024][research_onkar_kumar_2024]] [[Ormiston 2001][research_ormiston_2001]] [[Oyibo 1984][research_oyibo_1984]] [[Ozbay and Turi][research_ozbay_turi]] [[Ozger 2007][research_ozger_2007]] [[Paladini et al 2024][research_paladini_drewiacki_2024]] [[Pandita et al 2009][research_pandita_chakraborty_2009]] [[Papadopoulos 1958][research_papadopoulos_1958]] [[Parsons][research_parsons]] [[Patil 2003][research_patil_2003]] [[Patil and Hodges 2000][research_patil_hodges_2000_b]] [[Pavlov and Pavlov 2024][research_pavlov_pavlov_2024]] [[Peng 2011][research_peng_2011]] [[Peters 1988][research_peters_1988]] [[Phan 2020][research_phan_2020]] [[Pomin et al 2001][research_pomin_altmikus_2001]] [[Poole et al 2020][research_poole_allen_2020_b]] [[Prazenica 2014][research_prazenica_2014]] [[Prazenica et al 2004][research_prazenica_reisenthel_2004]] [[Proulx-Cabana][research_proulxcabana]] [[Prudhomme 1995][research_prudhomme_1995]] [[Prudhomme and Prudhomme 1997][research_prudhomme_prudhomme_1997]] [[Pusch 2018][research_pusch_2018]] [[Qin and Librescu 2003][research_qin_librescu_2003]] [[Qiu et al 2018][research_qiu_xu_2018]] [[Rahman and Li 2013][research_rahman_li_2013]] [[Rao and Padmanabhan 2019][research_rao_padmanabhan_2019]] [[Rao et al 1978][research_rao_kronenberger_1978]] [[Raveh 2026][research_raveh_2026]] [[Raveh and Levy 2004][research_raveh_levy_2004]] [[Reich et al 2002][research_reich_raveh_2002]] [[Reich et al 2004][research_reich_raveh_2004]] [[Ricci et al 2022][research_ricci_marchetti_2022]] [[Richard et al 2000][research_richard_rule_2000]] [[Richard et al 2001][research_richard_rule_2001]] [[Righi 2017][research_righi_2017]] [[Rimer et al 1984][research_rimer_chipman_1984]] [[Rimer et al 1986][research_rimer_chipman_1986]] [[Robinson][research_robinson]] [[Rocha et al 2007][research_rocha_moniz_2007]] [[Rodden 1956][research_rodden_1956]] [[Rogers 1998][research_rogers_1998]] [[Roknizadeh et al 2012][research_roknizadeh_nobari_2012]] [[Roskam, J. and Lan, C. 1973][research_roskamj_lanc_1973]] [[Rowan and Burns 1975][research_rowan_burns_1975]] [[Rowley 2008][research_rowley_2008]] [[Rowley 2010][research_rowley_2010]] [[Rubillo et al 2005][research_rubillo_bollt_2005]] [[Rufino et al 2026][research_rufino_faria_2026]] [[Saltari et al 2022][research_saltari_pizzoli_2022]] [[Sang Bum Choi et al][research_sangbumchoi_haojianxu]] [[Sazesh and Shams 2017][research_sazesh_shams_2017]] [[Schmidt 1986][research_schmidt_1986]] [[Schmidt and Newman 1988][research_schmidt_newman_1988]] [[Schneider][research_schneider]] [[Schoneman 2019][research_schoneman_2019]] [[Schuster 1995][research_schuster_1995]] [[Schuster, David M. and Edwards, John W. 2004][research_schusterdavidm_edwardsjohnw_2004]] [[Schwanz and Wells 1980][research_schwanz_wells_1980]] [[Schweikhard 1966][research_schweikhard_1966]] [[Schweikhard 1967][research_schweikhard_1967]] [[Sebastiano and Ricci 2013][research_sebastiano_ricci_2013]] [[Segel 1952][research_segel_1952]] [[Seiler et al 2012][research_seiler_balas_2012]] [[Selvam et al 2001][research_selvam_qu_2001]] [[Sendner et al 2018][research_sendner_stahl_2018]] [[Sharqi et al 2021][research_sharqi_cesnik_2021]] [[Shaw et al][research_shaw_hidalgo]] [[Shevare and Arya 2012][research_shevare_arya_2012]] [[Shklovskii and Kurt 1961][research_shklovskii_kurt_1961]] [[Shmelоv et al 2019][research_shmelv_vladov_2019]] [[Shukla and Patil 2015][research_shukla_patil_2015]] [[Silva][research_silva]] [[Simmons et al 2025][research_simmons_riso_2025]] [[Simulation and model reduction for the active flexible wing program][research_afw_simulation_reduction]] [[Singer 1956][research_singer_1956]] [[Singh and Brenner 2003][research_singh_brenner_2003]] [[Singh and Wang 2002][research_singh_wang_2002]] [[Singh et al 2010][research_singh_mcdonough_2010]] [[Singh et al 2015][research_singh_brown_2015]] [[Singh et al 2016][research_singh_brown_2016]] [[Sivanandi et al 2022][research_sivanandi_gupta_2022]] [[Sivanandi et al 2024][research_sivanandi_gupta_2024]] [[Smith et al 2001][research_smith_patil_2001]] [[Sotoudeh and Ferman 2019][research_sotoudeh_ferman_2019]] [[Sotoudeh et al 2010][research_sotoudeh_hodges_2010]] [[Spada et al 2017][research_spada_afonso_2017]] [[Squires 2004][research_squires_2004]] [[Srinivas and Chopra 1998][research_srinivas_chopra_1998]] [[Stalford 1981][research_stalford_1981]] [[Stamatellou and Kalfas 2021][research_stamatellou_kalfas_2021]] [[Stanford 2018][research_stanford_2018]] [[Stanford 2021][research_stanford_2021]] [[Stanford and Dunning 2015][research_stanford_dunning_2015]] [[Stettner 2000][research_stettner_2000]] [[Stiharu-Alexe 1991][research_stiharualexe_1991]] [[Stiharu-Alexe et al][research_stiharualexe_oshea]] [[Stougie et al 2024][research_stougie_pollack_2024]] [[Strganac 2007][research_strganac_2007]] [[Striz et al 1991][research_striz_eastep_1991]] [[Su 2015][research_su_2015]] [[Su and Cesnik 2009][research_su_cesnik_2009]] [[Su and Cesnik 2010][research_su_cesnik_2010]] [[Su et al 2017][research_su_huang_2017]] [[Su et al 2018][research_su_wang_2018]] [[Suleman 2007][research_suleman_2007]] [[Suleman and Costa 2004][research_suleman_costa_2004]] [[Suleman and Moniz][research_suleman_moniz]] [[Suleman et al 2016][research_suleman_afonso_2016]] [[Summary of an active flexible wing program][research_afw_technology_summary]] [[Sungpil Yang et al 2016][research_sungpilyang_hashemi_2016]] [[Svoboda et al 2021][research_svoboda_hromcik_2021]] [[Swaim][research_swaim]] [[Swaim 1983][research_swaim_1983]] [[Szollosi and Baranyi 2016][research_szollosi_baranyi_2016]] [[Takarics et al 2018][research_takarics_vanek_2018]] [[Tamayama 2017][research_tamayama_2017]] [[Tamura and Yumitori 2024][research_tamura_yumitori_2024]] [[Tang and Dowell 1998][research_tang_dowell_1998]] [[Tang and Dowell 2001][research_tang_dowell_2001]] [[Tang et al 2000][research_tang_kholodar_2000]] [[Taylor 1959][research_taylor_1959]] [[Taylor et al 2007][research_taylor_gaitonde_2007]] [[Teng and Chen 2006][research_teng_chen_2006]] [[Terilli et al 2025][research_terilli_bueno_2025]] [[Tewari 2001][research_tewari_2001]] [[Tewari 2015][research_tewari_2015]] [[Tharayil and Alleyne 2001][research_tharayil_alleyne_2001]] [[Tharayil and Alleyne 2004][research_tharayil_alleyne_2004]] [[The development of a lateral-control system for use with large-span flaps][research_lateral_control_large_flaps]] [[The effect of elastic 1969][research_the_effect_1969]] [[The F-18 high alpha research vehicle, a high-angle-of-attack testbed aircraft][research_harv_testbed]] [[Tiomkin and Raveh 2021][research_tiomkin_raveh_2021]] [[Toffol 2023][research_toffol_2023]] [[Toffol and Ricci 2023][research_toffol_ricci_2023]] [[Torok 1996][research_torok_1996]] [[Traas et al 2026][research_traas_atmaca_2026]] [[Trame et al 1985][research_trame_williams_1985]] [[Trenka 1971][research_trenka_1971]] [[Tucker Harvey et al 2020][research_tuckerharvey_khovanov_2020]] [[Tung et al 1996][research_tung_yu_1996]] [[Turi and Rankin 1988][research_turi_rankin_1988]] [[Turns and Kraige][research_turns_kraige]] [[Twist model development and results from the active aeroelastic wing F/A-18 aircraft][research_aaw_twist_model]] [[Upper Atmosphere Re-Entry Study 1961][research_upper_atmosphere_1961]] [[Urnes et al 2008][research_urnes_reichenbach_2008]] [[van Schoor and von Flotow 1990][research_vanschoor_vonflotow_1990]] [[Vandierendonck 1973][research_vandierendonck_1973]] [[Variation of natural radioactivity 1956][research_variation_of_1956]] [[Verhaegen 1987][research_verhaegen_1987]] [[Verstraete et al 2019][research_verstraete_roccia_2019]] [[Vindigni 2023][research_vindigni_2023]] [[Vos et al 2007][research_vos_hodigeresiddaramaiah_2007]] [[Wall et al 2024][research_wall_amoozgar_2024]] [[Wan Kim and Cho 2008][research_wankim_cho_2008]] [[Wang et al 2012][research_wang_xargay_2012]] [[Wang et al 2018][research_wang_wynn_2018]] [[Wang et al 2019][research_wang_yang_2019]] [[Wang et al 2025][research_wang_hu_2025]] [[Wang et al 2026][research_wang_hu_2026]] [[Warwick et al 2019][research_warwick_bras_2019]] [[Waszak and Schmidt 1988][research_waszak_schmidt_1988]] [[Waszak et al 2002][research_waszak_davidson_2002]] [[Wei et al 2018][research_wei_zhao_2018]] [[Weiss and Thielecke 2000][research_weiss_thielecke_2000]] [[Weisshaar 1985][research_weisshaar_1985]] [[Weisshaar 2010][research_weisshaar_2010]] [[Winther et al 1993][research_winther_hagemeyer_1993]] [[Wood and Buffano 1964][research_wood_buffano_1964]] [[Wood et al 1999][research_wood_loth_1999]] [[Woodward 1962][research_woodward_1962]] [[Wu et al 2021][research_wu_zhang_2021]] [[Wu et al 2024][research_wu_zhou_2024]] [[Wu et al 2025][research_wu_li_2025]] [[Wyrick 1965][research_wyrick_1965]] [[Xie et al 2012][research_xie_yang_2012]] [[Xing and Singh 1999][research_xing_singh_1999]] [[Xu et al 2015][research_xu_gao_2015]] [[Xu et al 2015][research_xu_gao_2015_b]] [[Xue and Li 2016][research_xue_li_2016]] [[Xue et al 2019][research_xue_ye_2019]] [[Yang and Guo 2009][research_yang_guo_2009]] [[Yang and Li 2022][research_yang_li_2022]] [[Yang et al 2007][research_yang_zheng_2007]] [[Yang et al 2018][research_yang_dudley_2018]] [[Yeh 1995][research_yeh_1995]] [[Yu 2026][research_yu_2026]] [[Yucelen et al 2011][research_yucelen_kim_2011]] [[Yusuf et al 2019][research_yusuf_hayes_2019]] [[Zafirov 2010][research_zafirov_2010]] [[Zaichik et al 2013][research_zaichik_yashin_2013]] [[Zeiler, Thomas A. 1998][research_zeilerthomasa_1998]] [[Zeng and Singh 1998][research_zeng_singh_1998]] [[Zhang and Behal 2014][research_zhang_behal_2014]] [[Zhang and Singh 2000][research_zhang_singh_2000]] [[Zhang and Söffker 2010][research_zhang_soffker_2010]] [[Zhang et al 2017][research_zhang_devisser_2017]] [[Zhang et al 2025][research_zhang_jiao_2025]] [[Zhao 2011][research_zhao_2011]] [[Zheng et al 2018][research_zheng_zhang_2018]] [[Zhu et al 2017][research_zhu_chen_2017]] [[Zhuang et al 2017][research_zhuang_wu_2017]] [[Zientek 2001][research_zientek_2001]] [[Zink et al 1998][research_zink_mavris_1998]] [[Zink et al 2000][research_zink_mavris_2000]] [[Zink et al 2000][research_zink_raveh_2000]] [[Zink et al 2001][research_zink_raveh_2001]] [[Zink et al 2003][research_zink_raveh_2003]]

### Flutter, and the instability this programme chose not to fly

**Large, old and deliberately out of scope.** Flutter, limit cycle oscillation, buffet and aeroelastic stability. **The predecessor wind-tunnel programme suppressed flutter actively and the flight programme removed that requirement**, which is the single largest scope decision in the story and the reason a manned aeroplane could fly it at all.

**432 records.** [[A flutter suppression system using strain gages applied to active flexible wing technology][research_afw_flutter_strain_gauge]] [[A parametric sensitivity and 1991][research_a_parametric_1991]] [[A synthesis of reduced-order 1994][research_a_synthesis_1994]] [[Abel and Newsom 1981][research_abel_newsom_1981]] [[Abel et al 1977][research_abel_perryiii_1977]] [[Abel et al 1978][research_abel_iii_1978]] [[Abel et al 1979][research_abel_newsom_1979]] [[Abramova et al 2016][research_abramova_petrov_2016]] [[Active control of a 1994][research_active_control_1994]] [[Active Flutter Suppression 2016][research_active_flutter_2016]] [[Active flutter suppression via 1999][research_active_flutter_1999]] [[Afkhami and Alighanbari 2007][research_afkhami_alighanbari_2007]] [[Akinwale and Datta 2025][research_akinwale_datta_2025]] [[Alag and Burken 1987][research_alag_burken_1987]] [[Alag et al 1986][research_alag_burken_1986]] [[Alhajjar et al 2018][research_alhajjar_aljiboory_2018]] [[Allen et al 2003][research_allen_fenwick_2003]] [[Amoozgar and Shahverdi 2019][research_amoozgar_shahverdi_2019]] [[Amoozgar et al 2013][research_amoozgar_irani_2013]] [[Amoozgar et al 2020][research_amoozgar_fazelzadeh_2020]] [[Amoozgar et al 2021][research_amoozgar_friswell_2021]] [[Amoozgar et al 2024][research_amoozgar_hall_2024]] [[Anderson et al 2004][research_anderson_white_2004]] [[Anderson et al 2026][research_anderson_caverly_2026]] [[Andrighettoni and Mantegazza 1998][research_andrighettoni_mantegazza_1998]] [[Appendix C Flutter Analysis 2016][research_appendix_c_2016]] [[Asadi and Farsadi 2020][research_asadi_farsadi_2020]] [[Asadi et al 2021][research_asadi_farsadi_2021]] [[Bachelder et al 2004][research_bachelder_klyde_2004]] [[Bahia Monteiro et al 2023][research_bahiamonteiro_gray_2023]] [[Baldelli et al 2009][research_baldelli_zeng_2009]] [[Balleur et al 2002][research_balleur_girodrouxlavigne_2002]] [[Banerjee et al 2014][research_banerjee_liu_2014]] [[Barker and Balas 2000][research_barker_balas_2000]] [[Barker et al 1999][research_barker_balas_1999]] [[Ben Asher and Raveh 2023][research_benasher_raveh_2023]] [[Bendiksen 1992][research_bendiksen_1992]] [[Bendiksen 2001][research_bendiksen_2001]] [[Bendiksen et al 1997][research_bendiksen_hwang_1997]] [[Bennett et al 2001][research_bennett_brown_2001]] [[Bergman et al 2011][research_bergman_vakakis_2011]] [[Bernelli-Zazzera et al 2000][research_bernellizazzera_mantegazza_2000]] [[Bhat 2018][research_bhat_2018_b]] [[Bi et al 2017][research_bi_xie_2017]] [[Bismarck-Nasr 1992][research_bismarcknasr_1992]] [[Bismarck-Nasr 1994][research_bismarcknasr_1994]] [[Blue et al 1997][research_blue_balas_1997]] [[Borglund 2003][research_borglund_2003]] [[Borglund and Kuttenkeuler 2002][research_borglund_kuttenkeuler_2002]] [[Borglund and Nilsson 2004][research_borglund_nilsson_2004]] [[Botez et al 2002][research_botez_doin_2002]] [[Bradshaw et al 1988][research_bradshaw_rahulan_1988]] [[Breitsamter 2005][research_breitsamter_2005]] [[Breitsamter and Laschka 2000][research_breitsamter_laschka_2000]] [[Breitsamter and Schmid 2008][research_breitsamter_schmid_2008]] [[Browne et al 2024][research_browne_maldonado_2024]] [[Buddhamatya et al 2026][research_buddhamatya_miranda_2026]] [[Bunton and Denegri 2000][research_bunton_denegri_2000]] [[Byreddy et al 2003][research_byreddy_grandhi_2003]] [[Candida et al 2019][research_candida_souzadepaula_2019]] [[Cazier, Jr. and Kehoe 1986][research_cazierjr_kehoe_1986]] [[Chakravarty and Moore 1986][research_chakravarty_moore_1986]] [[Chang et al 2002][research_chang_trivailo_2002]] [[Chang et al 2010][research_chang_yang_2010]] [[Chen et al 2006][research_chen_wickramasinghe_2006]] [[Chen et al 2009][research_chen_ulker_2009]] [[Chen et al 2023][research_chen_shi_2023]] [[Chen et al 2023][research_chen_shi_2023_b]] [[Chopra 1983][research_chopra_1983]] [[Chopra 1988][research_chopra_1988]] [[Chung et al 2002][research_chung_lee_2002]] [[Crittenden et al 1977][research_crittenden_weisshaar_1977]] [[Crittenden et al 1978][research_crittenden_weishaar_1978]] [[Damveld 2004][research_damveld_2004]] [[Darabseh et al 2022][research_darabseh_tarabulsi_2022]] [[Darabseh et al 2022][research_darabseh_tarabulsi_2022_b]] [[Delgado et al 2026][research_delgado_datta_2026]] [[Denegri and Dubben 2003][research_denegri_dubben_2003]] [[Denegri et al 2005][research_denegri_dubben_2005]] [[Desmarais and Reed, Iii 1980][research_desmarais_reediii_1980]] [[Dessi and Mastroddi 2002][research_dessi_mastroddi_2002]] [[Di Pasquale 2024][research_dipasquale_2024]] [[Di Pasquale and Prince 2023][research_dipasquale_prince_2023]] [[Diwekar and Yedavalli 1995][research_diwekar_yedavalli_1995]] [[Dixit et al 2016][research_dixit_kodhanda_2016]] [[Djayapertapa and Allen 2002][research_djayapertapa_allen_2002]] [[Dowell 1990][research_dowell_1990]] [[Dowell 1996][research_dowell_1996]] [[Dowell 1999][research_dowell_1999]] [[Dowell 2001][research_dowell_2001]] [[Downs and Prazenica 2022][research_downs_prazenica_2022]] [[Downs and Prazenica 2023][research_downs_prazenica_2023]] [[Drake and Balakrishnan 2004][research_drake_balakrishnan_2004]] [[Duan and Zhang 2018][research_duan_zhang_2018]] [[Eichelsdörfer 2026][research_eichelsdorfer_2026]] [[Eichelsdörfer 2026][research_eichelsdorfer_2026_b]] [[Elastic and Aeroelastic Instabilities 2008][research_elastic_and_2008]] [[Elhami and Narab 2012][research_elhami_narab_2012]] [[Ericsson and Reding 1981][research_ericsson_reding_1981]] [[Eversman and Danda Roy 1996][research_eversman_dandaroy_1996]] [[Eversman and Roy 1997][research_eversman_roy_1997]] [[Farhangnia et al 1996][research_farhangnia_guruswamy_1996]] [[Faroughi et al 2012][research_faroughi_malekzadeh_2012]] [[Faïsse][research_faisse]] [[Faïsse et al 2021][research_faisse_vernay_2021]] [[Floros and Kang 2017][research_floros_kang_2017]] [[Flutter suppression control law synthesis for the active flexible wing model][research_afw_flutter_suppression]] [[Forte and Nguyen 2026][research_forte_nguyen_2026_d]] [[Friedmann 1973][research_friedmann_1973]] [[Fujimori et al 1995][research_fujimori_nikiforuk_1995]] [[Fukumoto et al 2023][research_fukumoto_kouchi_2023]] [[Gabel et al 1961][research_gabel_ricks_1961]] [[Gade and Inman 1996][research_gade_inman_1996]] [[Gade and Inman 1997][research_gade_inman_1997]] [[Gangsaas et al 1981][research_gangsaas_ly_1981]] [[Garrard and Liebst 1983][research_garrard_liebst_1983]] [[Garrard and Liebst 1985][research_garrard_liebst_1985]] [[Garrick, I E and Rubinow, S I 1946][research_garrickie_rubinowsi_1946]] [[Garrick, I E and Rubinow, S I 1946][research_garrickie_rubinowsi_1946_b]] [[Generalized predictive control for 1997][research_generalized_predictive_1997]] [[Gern 2001][research_gern_2001]] [[Ghiringhelli et al 1990][research_ghiringhelli_lanz_1990]] [[Ghiringhelli et al 1992][research_ghiringhelli_lanz_1992]] [[Ghosh and Patil 2022][research_ghosh_patil_2022]] [[Goizueta et al 2021][research_goizueta_drachinsky_2021]] [[Goizueta et al 2022][research_goizueta_wynn_2022]] [[Gonzales et al 2022][research_gonzales_sakaue_2022]] [[Grauer and Waite 1986][research_grauer_waite_1986]] [[Grauer and Waite 2024][research_grauer_waite_2024]] [[Green and Fernandez 1994][research_green_fernandez_1994]] [[Gupta et al 2005][research_gupta_doyle_2005]] [[Haas and Chopra 1989][research_haas_chopra_1989]] [[Haas and Chopra 1990][research_haas_chopra_1990]] [[Haley and Soloway 2001][research_haley_soloway_2001]] [[Haley and Soloway 2022][research_haley_soloway_2022]] [[Ham et al 1994][research_ham_kim_1994]] [[Harvey 1983][research_harvey_1983]] [[He et al 2024][research_he_shi_2024]] [[Hitch 1978][research_hitch_1978]] [[Hodges 1973][research_hodges_1973]] [[Hodson et al 1993][research_hodson_dobbs_1993]] [[Hoseini and Hodges 2019][research_hoseini_hodges_2019]] [[Huang et al 2015][research_huang_qian_2015]] [[Huang et al 2024][research_huang_zhang_2024]] [[Hwang and Pi 1982][research_hwang_pi_1982]] [[Ishii 1965][research_ishii_1965]] [[Izadpanahi][research_izadpanahi]] [[Jeong et al 2013][research_jeong_lee_2013]] [[Jiang et al 2019][research_jiang_tian_2019]] [[Johnson 1980][research_johnson_1980]] [[Jones 1976][research_jones_1976]] [[Karpel 1982][research_karpel_1982]] [[Karpel 1989][research_karpel_1989]] [[Kayran 2004][research_kayran_2004]] [[Kayran 2007][research_kayran_2007]] [[Kehoe 1988][research_kehoe_1988]] [[Kheiri and Riazat 2025][research_kheiri_riazat_2025]] [[Kholodar 2016][research_kholodar_2016]] [[Kim and Crassidis 2003][research_kim_crassidis_2003]] [[Klepl 1995][research_klepl_1995]] [[Kojima et al 2019][research_kojima_kameda_2019]] [[Kosmatka and Panza 2002][research_kosmatka_panza_2002]] [[Kotikalpudi et al 2016][research_kotikalpudi_pfifer_2016]] [[Kotikalpudi et al 2018][research_kotikalpudi_danowsky_2018]] [[Kratochvíl and Valenta 2024][research_kratochvil_valenta_2024]] [[Kreshock et al 2018][research_kreshock_yeo_2018]] [[Kwon et al 2026][research_kwon_chang_2026]] [[Lai et al 2014][research_lai_zhang_2014]] [[Lai et al 2016][research_lai_lu_2016]] [[Lam et al 2024][research_lam_paranjape_2024]] [[Lambert and Gursul 2001][research_lambert_gursul_2001]] [[Lanjun Li et al 2006][research_lanjunli_shouyiyu_2006]] [[Lee-Rausch and Batina 1993][research_leerausch_batina_1993]] [[Levinski 2004][research_levinski_2004]] [[Lewis et al 1979][research_lewis_platt_1979]] [[Lhachemi et al 2017][research_lhachemi_chu_2017]] [[Lhachemi et al 2017][research_lhachemi_saussie_2017]] [[Li and Fleeter 1996][research_li_fleeter_1996]] [[Li and Xia 2017][research_li_xia_2017]] [[Li et al 2009][research_li_dong_2009]] [[Li et al 2014][research_li_zhang_2014]] [[Li et al 2024][research_li_dai_2024]] [[Li et al 2025][research_li_dai_2025]] [[Lichtenwalner et al 1996][research_lichtenwalner_little_1996]] [[Liebst 1987][research_liebst_1987]] [[Liebst et al 1986][research_liebst_garrard_1986]] [[Liebst et al 1986][research_liebst_garrard_1986_b]] [[Liebst et al 1988][research_liebst_garrard_1988]] [[Lind and Brenner 1997][research_lind_brenner_1997_b]] [[Lind et al 1997][research_lind_brenner_1997]] [[Lorber and Carta 1991][research_lorber_carta_1991]] [[Lottati 1987][research_lottati_1987]] [[Lottati 1988][research_lottati_1988]] [[Lu and Huang 1993][research_lu_huang_1993]] [[Lu and Yeh 1993][research_lu_yeh_1993]] [[Lu et al 2016][research_lu_cui_2016]] [[Luce and Moore 1963][research_luce_moore_1963]] [[Lum et al 2016][research_lum_xu_2016]] [[Luton and Mook 1992][research_luton_mook_1992]] [[Luton and Mook 1993][research_luton_mook_1993]] [[Lyons et al 1973][research_lyons_vepa_1973]] [[Mahesh et al 1980][research_mahesh_stone_1980]] [[Mamedov et al 2018][research_mamedov_paryshev_2018]] [[Mangalam et al 2008][research_mangalam_mangalam_2008]] [[Mangalam et al 2010][research_mangalam_jutte_2010]] [[Marchetti 2023][research_marchetti_2023]] [[Mardanpour et al 2019][research_mardanpour_izadpanahi_2019]] [[Marques and Azevedo 2007][research_marques_azevedo_2007]] [[Marques and Azevedo 2008][research_marques_azevedo_2008]] [[Marques et al 2010][research_marques_badcock_2010]] [[Marques et al 2012][research_marques_badcock_2012]] [[Marretta and Marino 2007][research_marretta_marino_2007]] [[Marzocca et al 2002][research_marzocca_librescu_2002]] [[Masini et al 2019][research_masini_timme_2019]] [[Masini et al 2020][research_masini_timme_2020]] [[Mason and Berg 1994][research_mason_berg_1994]] [[Mataich et al 2025][research_mataich_elkhadiri_2025]] [[Mattaboni et al 2009][research_mattaboni_quaranta_2009]] [[Mayer et al 2019][research_mayer_lutz_2019]] [[Mayya et al 2022][research_mayya_karnick_2022]] [[Melville 2002][research_melville_2002]] [[Meng 2021][research_meng_2021]] [[Micheli 2024][research_micheli_2024]] [[Model Rotor Testing for 2006][research_model_rotor_2006]] [[Molton et al 2010][research_molton_bur_2010]] [[Molton et al 2013][research_molton_dandois_2013]] [[Moni et al 2026][research_moni_wales_2026]] [[Moosavi and Elasha 2022][research_moosavi_elasha_2022]] [[Moulin 2004][research_moulin_2004]] [[Mu et al 2022][research_mu_huang_2022]] [[Muchamad Bayu Sakti Pratama et al 2022][research_muchamadbayusaktipratama_erwinsulaeman_2022]] [[Mukhopadhyay 1995][research_mukhopadhyay_1995]] [[Murugan and Ganguli 2005][research_murugan_ganguli_2005]] [[Muscarello et al 2026][research_muscarello_marzocca_2026]] [[Muñoz and García-Fogeda 2022][research_munoz_garciafogeda_2022]] [[Muñoz and García-Fogeda 2023][research_munoz_garciafogeda_2023]] [[Muñoz and García-Fogeda 2024][research_munoz_garciafogeda_2024]] [[Na Zhao et al 2010][research_nazhao_dengqingcao_2010]] [[Nae et al 2019][research_nae_stroe_2019]] [[Nailu et al 2025][research_nailu_wentao_2025]] [[Nam et al 1996][research_nam_kim_1996]] [[Nam et al 1997][research_nam_kim_1997]] [[Nash et al 2025][research_nash_timme_2025]] [[Nasu, Ken-Ichi 1986][research_nasukenichi_1986]] [[Newsom 1978][research_newsom_1978]] [[Newsom 1979][research_newsom_1979]] [[Nguyen and Swei 2015][research_nguyen_swei_2015]] [[Nguyen et al 2019][research_nguyen_fugate_2019]] [[Nguyen et al 2026][research_nguyen_xiong_2026]] [[Nissim 1975][research_nissim_1975]] [[Nissim 1976][research_nissim_1976]] [[Nissim and Lottati 1979][research_nissim_lottati_1979]] [[Nissim and Lottati 1979][research_nissim_lottati_1979_b]] [[Nissim and Lottati 1980][research_nissim_lottati_1980]] [[Nissim, E. et al 1976][research_nissime_caspia_1976]] [[Nitzsche 1994][research_nitzsche_1994]] [[Noll and Huttsell 1978][research_noll_huttsell_1978]] [[Noll and Huttsell 1979][research_noll_huttsell_1979]] [[Noll and Merino 1976][research_noll_merino_1976]] [[Noll et al 1980][research_noll_huttsell_1980]] [[Noll et al 1983][research_noll_eastep_1983]] [[Noll et al 1983][research_noll_calico_1983]] [[Noll et al 1984][research_noll_eastep_1984]] [[O'Brien and Datta 2026][research_obrien_datta_2026]] [[Ohta et al 1984][research_ohta_nikiforuk_1984]] [[Ohta et al 1989][research_ohta_fujimori_1989]] [[Oremland et al 2017][research_oremland_suryakumar_2017]] [[Ouellette 2017][research_ouellette_2017]] [[Ouyang et al 2021][research_ouyang_gu_2021]] [[Ouyang et al 2026][research_ouyang_jia_2026]] [[Oyibo 1983][research_oyibo_1983]] [[Ozbay 1993][research_ozbay_1993]] [[Panel flutter in a 1991][research_panel_flutter_1991]] [[Passive wing/store flutter suppression 1982][research_passive_wing_store_1982]] [[Patartics et al 2017][research_patartics_luspay_2017]] [[Pecora et al 2018][research_pecora_amoroso_2018]] [[Peloubet, Jr. et al 1983][research_peloubetjr_haller_1983]] [[Perkins and Brice 1966][research_perkins_brice_1966]] [[Perry, Iii et al 1990][research_perryiii_mukhopadhyay_1990]] [[Pines et al 1955][research_pines_dugundji_1955]] [[Pitt et al 2016][research_pitt_sexton_2016]] [[Plath][research_plath]] [[Poplingher et al 2022][research_poplingher_mallik_2022]] [[Porter and Gu 1991][research_porter_gu_1991]] [[Porter et al 1992][research_porter_merzougui_1992]] [[Porter et al 1992][research_porter_merzougui_1992_b]] [[Pushtaev 1989][research_pushtaev_1989]] [[Qian 2018][research_qian_2018]] [[Qian et al 2014][research_qian_huang_2014]] [[Qian et al 2014][research_qian_huang_2014_b]] [[Quero 2025][research_quero_2025]] [[Raja and Upadhya 2007][research_raja_upadhya_2007]] [[Rea et al 2017][research_rea_pecora_2017]] [[Rea et al 2018][research_rea_pecora_2018]] [[Reding and Ericsson 1977][research_reding_ericsson_1977]] [[Reich, hoor, Mart et al 1995][research_reichhoormart_lin_1995]] [[Rendina and Mazzoni 1999][research_rendina_mazzoni_1999]] [[Rigatos et al 2026][research_rigatos_dala_2026]] [[Rock et al 1993][research_rock_ashley_1993]] [[Roger et al 1974][research_roger_hodges_1974]] [[Roy and Eversman 1996][research_roy_eversman_1996]] [[Ruhlin and Pratt-Barlow 1981][research_ruhlin_prattbarlow_1981]] [[Rule et al 2000][research_rule_richard_2000]] [[Rule et al 2001][research_rule_richard_2001]] [[Rutkowski 1979][research_rutkowski_1979]] [[Sabatini et al 2026][research_sabatini_livne_2026]] [[Sabatini et al 2026][research_sabatini_coppotelli_2026]] [[Sahyoun et al 2026][research_sahyoun_boose_2026]] [[Saitoh et al 1995][research_saitoh_hashidate_1995]] [[Santos et al 2026][research_santos_marques_2026]] [[Schauerte et al 2026][research_schauerte_kwong_2026]] [[Schewe and Mai 2019][research_schewe_mai_2019]] [[Schildkamp et al 2023][research_schildkamp_chang_2023]] [[Schmidt 2016][research_schmidt_2016]] [[sekhar et al 2024][research_sekhar_suresh_2024]] [[Sharma et al 2022][research_sharma_agrawal_2022]] [[Sharpe et al 2023][research_sharpe_ulker_2023]] [[Sheta 2000][research_sheta_2000]] [[Silva et al 2006][research_silva_mello_2006]] [[Simmons et al 2026][research_simmons_chang_2026]] [[Singh and Friedmann 2020][research_singh_friedmann_2020]] [[Singh and Friedmann 2021][research_singh_friedmann_2021]] [[Singh and Venkatraman 2023][research_singh_venkatraman_2023]] [[Slaby and Smith 2011][research_slaby_smith_2011]] [[Slater 1985][research_slater_1985]] [[Smith 2025][research_smith_2025]] [[Song et al 2010][research_song_wu_2010]] [[Sotoudeh 2014][research_sotoudeh_2014]] [[Sotoudeh 2015][research_sotoudeh_2015]] [[Spangler, Jr. and Jacques 1999][research_spanglerjr_jacques_1999]] [[Srinathkumar and Adams, Jr. 1989][research_srinathkumar_adamsjr_1989]] [[Stanewsky and Basler 1989][research_stanewsky_basler_1989]] [[Stanford and Beran 2011][research_stanford_beran_2011]] [[Stanford and Jacobson 2023][research_stanford_jacobson_2023]] [[Starodub 2026][research_starodub_2026]] [[Steimle et al 2008][research_steimle_schroder_2008]] [[Su et al 2023][research_su_sun_2023]] [[Sun and Bai 2014][research_sun_bai_2014]] [[Suzuki 1990][research_suzuki_1990]] [[Suzuki and Matsuda 1991][research_suzuki_matsuda_1991]] [[Svoboda and Hromcik 2019][research_svoboda_hromcik_2019]] [[Svoboda et al 2018][research_svoboda_hromcik_2018]] [[Syed et al 2022][research_syed_moshtaghzadeh_2022]] [[Szymanski et al 2025][research_szymanski_alstrom_2025]] [[Tadi 2003][research_tadi_2003]] [[Tang and Dowell 1996][research_tang_dowell_1996]] [[Tang and Dowell 2013][research_tang_dowell_2013]] [[Tang et al 2017][research_tang_chen_2017]] [[Tani 1992][research_tani_1992]] [[Teixeira and Cesnik 2020][research_teixeira_cesnik_2020]] [[Teng 2007][research_teng_2007]] [[Tewari 1998][research_tewari_1998]] [[Tewari 1999][research_tewari_1999]] [[Tewari 2009][research_tewari_2009]] [[Theis et al 2016][research_theis_pfifer_2016]] [[Theis et al 2020][research_theis_pfifer_2020]] [[Tian et al 2026][research_tian_wang_2026]] [[Ting et al 2026][research_ting_berg_2026]] [[Toker and Ozbay][research_toker_ozbay]] [[Torrigiani and Berci 2021][research_torrigiani_berci_2021]] [[Tracy and Chopra 1998][research_tracy_chopra_1998]] [[Triplett 1972][research_triplett_1972]] [[Triplett et al 1973][research_triplett_kappus_1973]] [[U. P. V. et al 2025][research_upv_deodhare_2025]] [[Unsteady Aerodynamics and Flutter 2006][research_unsteady_aerodynamics_2006]] [[Uppoor and Chopra 2026][research_uppoor_chopra_2026]] [[Vepa 2007][research_vepa_2007]] [[Vepa 2007][research_vepa_2007_b]] [[Vernon 1993][research_vernon_1993]] [[Vindigni 2024][research_vindigni_2024]] [[Vindigni et al 2024][research_vindigni_mantegna_2024]] [[Vindigni et al 2024][research_vindigni_mantegna_2024_b]] [[Vindigni et al 2026][research_vindigni_mantegna_2026]] [[Von Flotow 1989][research_vonflotow_1989]] [[Voracek and Clarke 1991][research_voracek_clarke_1991]] [[Waite et al 2019][research_waite_stanford_2019_b]] [[Waitman and Marcos 2020][research_waitman_marcos_2020]] [[Wasmi et al 2015][research_wasmi_hasan_2015]] [[Waszak 1996][research_waszak_1996]] [[Waszak 2001][research_waszak_2001]] [[Waszak and Buttrill 1991][research_waszak_buttrill_1991]] [[Waszak and Srinathkumar 1991][research_waszak_srinathkumar_1991]] [[Waszak and Srinathkumar 1992][research_waszak_srinathkumar_1992]] [[Waszak and Srinathkumar 1995][research_waszak_srinathkumar_1995]] [[weibing and Kuisheng 2006][research_weibing_kuisheng_2006]] [[Weisshaar 1978][research_weisshaar_1978]] [[Weisshaar and Ryan 1984][research_weisshaar_ryan_1984]] [[Weisshaar, T. A. 1983][research_weisshaarta_1983]] [[Wilcox and Brenner 2011][research_wilcox_brenner_2011]] [[Wilde et al 2001][research_wilde_omenzetter_2001]] [[Wing Buffeting Control at 2018][research_wing_buffeting_2018]] [[Woods et al 1989][research_woods_gilbert_1989]] [[Woods et al 1990][research_woods_gilbert_1990]] [[Wright and Silva 2026][research_wright_silva_2026]] [[Wu and Cooper 2016][research_wu_cooper_2016]] [[Wu et al 2022][research_wu_dai_2022]] [[Wuestenhagen 2022][research_wuestenhagen_2022]] [[Wuestenhagen et al 2018][research_wuestenhagen_kier_2018]] [[Wuestenhagen et al 2018][research_wuestenhagen_kier_2018_b]] [[Xiang and Wang 2023][research_xiang_wang_2023]] [[Xiao et al 2022][research_xiao_wang_2022]] [[Xie and Yang 2011][research_xie_yang_2011]] [[Xie et al 2007][research_xie_leng_2007]] [[Xie et al 2016][research_xie_liu_2016]] [[Xiong and Liu 2013][research_xiong_liu_2013]] [[Xiong and Nguyen 2024][research_xiong_nguyen_2024_b]] [[Xiong and Yang 2001][research_xiong_yang_2001]] [[Yang and Wan 1978][research_yang_wan_1978]] [[Yang and Xia 2011][research_yang_xia_2011]] [[Yang et al 2014][research_yang_li_2014]] [[Yang et al 2017][research_yang_huang_2017]] [[Yang et al 2019][research_yang_huang_2019]] [[Yang et al 2025][research_yang_kou_2025]] [[Yates 1963][research_yates_1963]] [[Ye and Ye 2021][research_ye_ye_2021]] [[Yeo et al 2010][research_yeo_potsdam_2010]] [[Yeo et al 2023][research_yeo_kang_2023]] [[Yu et al 2004][research_yu_yuan_2004]] [[Yu et al 2026][research_yu_bose_2026]] [[Yurkovich 1986][research_yurkovich_1986]] [[Zeng et al 2012][research_zeng_kukreja_2012]] [[Zhan 2016][research_zhan_2016]] [[Zhang and Soffker][research_zhang_soffker]] [[Zhang et al 2008][research_zhang_xu_2008]] [[Zhang et al 2026][research_zhang_deng_2026]] [[Zhao 2009][research_zhao_2009]] [[Zhong et al 2025][research_zhong_xia_2025]] [[Zhou et al 2018][research_zhou_yu_2018]] [[Zhu and Qiao 2009][research_zhu_qiao_2009]] [[Zou et al 2021][research_zou_mu_2021]] [[Zou et al 2022][research_zou_huang_2022]] [[Čečrdle 2018][research_cecrdle_2018]]

### Measuring a wing in the air

**The largest cluster, and half of what this programme actually was.** Flight test technique, parameter identification, strain-gauge load calibration and in-flight deflection measurement. **The X-53 spent its whole first phase measuring itself** before anybody wrote a control law, and the models that came out of that phase are what the second phase flew.

**400 records.** [[A comparative study of 2026][research_a_comparative_2026]] [[A flight research program for active aeroelastic wing technology][research_aaw_flight_research_plan]] [[Active aeroelastic wing flight research program, technical program and model analytical development][research_aaw_technical_program]] [[Advisory Group for Aerospace Research and Development 1984][research_advisorygroupforaerospaceresearchanddevelopment_1984]] [[Air Force Flight Test Center Edwards Afb Ca 1970][research_airforceflighttestcenteredwardsafbca_1970]] [[Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974]] [[Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974_b]] [[Air Force Flight Test Center Edwards Afb Ca 2002][research_airforceflighttestcenteredwardsafbca_2002]] [[Air Force Test Pilot School Edwards Afb Ca 1962][research_airforcetestpilotschooledwardsafbca_1962]] [[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990]] [[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_b]] [[Ajaj and Djidjeli 2022][research_ajaj_djidjeli_2022]] [[Alaverdi and Paris 2001][research_alaverdi_paris_2001]] [[Albisser][research_albisser]] [[Alvarez 2014][research_alvarez_2014]] [[Anderson et al 1983][research_anderson_vincent_1983]] [[Andrews and Gordon 1981][research_andrews_gordon_1981]] [[Andrienko et al 2010][research_andrienko_tropova_2010]] [[Aref'ev 1968][research_arefev_1968]] [[Armstrong 1977][research_armstrong_1977]] [[Arnold 1981][research_arnold_1981]] [[Bach and McNally 1988][research_bach_mcnally_1988]] [[Bachelder et al 2011][research_bachelder_thompson_2011]] [[Baer-Riedhart 1981][research_baerriedhart_1981]] [[Bateman et al 2023][research_bateman_dewekker_2023]] [[Baumann et al 2008][research_baumann_pahle_2008]] [[Bednarz et al 2013][research_bednarz_zhu_2013]] [[Belisle et al 2010][research_belisle_neale_2010]] [[Benjamin M Simmons][research_benjaminmsimmons]] [[Benyamen and Keshmiri 2022][research_benyamen_keshmiri_2022]] [[Beug et al 2012][research_beug_moser_2012]] [[Bever 1992][research_bever_1992]] [[Biederman et al 1994][research_biederman_meincke_1994]] [[Bigler 1986][research_bigler_1986]] [[Birks and Ludlow 1969][research_birks_ludlow_1969]] [[Blair et al 2008][research_blair_robinson_2008]] [[Bleimeyer 1981][research_bleimeyer_1981]] [[Bohacek et al][research_bohacek_nakamura]] [[Bouchalkha et al 2015][research_bouchalkha_alhammadi_2015]] [[Brandon and Morelli 2014][research_brandon_morelli_2014]] [[Brenner and Prazenica 2005][research_brenner_prazenica_2005]] [[Bronz and Hattenberger 2016][research_bronz_hattenberger_2016]] [[Brown et al 2004][research_brown_dillon_2004]] [[Bunge et al 2015][research_bunge_munerasavino_2015]] [[Burch 1966][research_burch_1966]] [[Burch 1967][research_burch_1967]] [[Burcham, Jr. et al 1981][research_burchamjr_myers_1981]] [[Burchett 2011][research_burchett_2011]] [[Burchett 2012][research_burchett_2012]] [[Canniff 1969][research_canniff_1969]] [[Carico 1998][research_carico_1998]] [[Carpenter et al 2018][research_carpenter_solomon_2018]] [[Carter][research_carter]] [[Castellani et al 2016][research_castellani_cooper_2016_b]] [[Castillo Zuñiga et al 2019][research_castillozuniga_giacobinisouza_2019]] [[Chahmi 2022][research_chahmi_2022]] [[Chapman and Yates 1992][research_chapman_yates_1992]] [[Chase][research_chase]] [[Chase and McDonald 2014][research_chase_mcdonald_2014]] [[Chen et al 2026][research_chen_ding_2026]] [[Cheney 1988][research_cheney_1988]] [[Chestnutt 1966][research_chestnutt_1966]] [[Clarke and Roskam 1982][research_clarke_roskam_1982]] [[Clarke et al 2005][research_clarke_allen_2005]] [[Cliett 1952][research_cliett_1952]] [[Cockrell and Doherr 1981][research_cockrell_doherr_1981]] [[Corminboeuf 2015][research_corminboeuf_2015]] [[Cornell Aeronautical Lab Inc Buffalo Ny 1947][research_cornellaeronauticallabincbuffalony_1947]] [[Couch et al 2001][research_couch_duren_2001]] [[Cowan et al 1998][research_cowan_arenajr_1998]] [[Crites et al 1992][research_crites_rueger_1992]] [[Cui et al 2021][research_cui_jianlong_2021]] [[Cunningham et al 2008][research_cunningham_foster_2008]] [[Cusimano and Johnson 1994][research_cusimano_johnson_1994]] [[Danowsky et al 2012][research_danowsky_schulze_2012]] [[de Visser and Pool 2023][research_devisser_pool_2023]] [[Deangelis 1981][research_deangelis_1981]] [[DeAngelis 1982][research_deangelis_1982]] [[Deiler 2016][research_deiler_2016]] [[Demo 1986][research_demo_1986]] [[Development of a Continuous 2012][research_development_of_2012]] [[Dias 2023][research_dias_2023]] [[Dicarlo et al 1992][research_dicarlo_brown_1992]] [[Dobronski 1988][research_dobronski_1988]] [[Dooley and Yeary 1979][research_dooley_yeary_1979]] [[Dorin and Smolin 1977][research_dorin_smolin_1977]] [[Drouet and Champoux 2014][research_drouet_champoux_2014]] [[Dwyer 1994][research_dwyer_1994]] [[Dynamic force calibration of][research_dynamic_force]] [[Ellis et al 2001][research_ellis_hui_2001]] [[Energy Approach To Performance 2003][research_energy_approach_2003]] [[Engelien 1994][research_engelien_1994]] [[Erdman 2005][research_erdman_2005]] [[Eulrich and Rynaski 1980][research_eulrich_rynaski_1980]] [[F.M. Strain Gauge System 1975][research_f_m_strain_1975]] [[Fechter and Mills 1988][research_fechter_mills_1988]] [[Finnestead et al 1970][research_finnestead_connor_1970]] [[Fischenberg 1995][research_fischenberg_1995]] [[Fisher et al 1956][research_fisher_gertsen_1956]] [[Flight test of a 1979][research_flight_test_1979]] [[Flight test of the F/A-18 active aeroelastic wing airplane][research_aaw_flight_test]] [[Flight Testing 1992][research_flight_testing_1992]] [[Flight-Loads Prediction and Structural-Life 1981][research_flight_loads_prediction_1981]] [[Force measurement. Strain gauge][research_force_measurement]] [[Fosdick 1970][research_fosdick_1970]] [[Foster 1966][research_foster_1966]] [[Francisco Peña and Benjamin Park 2024][research_franciscopena_benjaminpark_2024]] [[French 1988][research_french_1988]] [[French and Eastep 1996][research_french_eastep_1996]] [[Frierson and Van Meter 1977][research_frierson_vanmeter_1977]] [[Frierson et al 1978][research_frierson_moore_1978]] [[Frost, Susan A. et al 2015][research_frostsusana_wrightcameronhg_2015]] [[Further development and flight 1994][research_further_development_1994]] [[Gallagher and Wei 2008][research_gallagher_wei_2008]] [[Galway 1980][research_galway_1980]] [[Garcia-Velo and Walker 1995][research_garciavelo_walker_1995]] [[Gera et al 1981][research_gera_wilson_1981]] [[Gibson 1981][research_gibson_1981]] [[Gibson and Ung 1995][research_gibson_ung_1995]] [[Goodman and Conigliaro 1986][research_goodman_conigliaro_1986]] [[Gorbushin et al 2024][research_gorbushin_kozik_2024]] [[Goupil][research_goupil]] [[Grauer and Boucher 2017][research_grauer_boucher_2017]] [[Grauer and Morelli 2023][research_grauer_morelli_2023]] [[Gregory and McCrink 2016][research_gregory_mccrink_2016]] [[Gupta 2011][research_gupta_2011]] [[Gupta 2019][research_gupta_2019]] [[Hale and Chapman 2012][research_hale_chapman_2012]] [[Hanafee and Radcliffe 1967][research_hanafee_radcliffe_1967]] [[Harris et al 2016][research_harris_arthurs_2016]] [[Hatamleh et al 2009][research_hatamleh_ma_2009]] [[Hayashi and Ueda 2017][research_hayashi_ueda_2017]] [[Helicopter Flight Parameter Identification 1987][research_helicopter_flight_1987]] [[Helmken et al 1996][research_helmken_emmons_1996]] [[Hess 1986][research_hess_1986]] [[Hicks and Jenkins 1990][research_hicks_jenkins_1990]] [[High-Load Strain Gauge Balance 2018][research_high_load_strain_2018]] [[Hiti 2017][research_hiti_2017]] [[Hodges and Mckenzie 1975][research_hodges_mckenzie_1975]] [[Hofmann et al 2025][research_hofmann_hosseini_2025]] [[Holberg and Grabowsky 1981][research_holberg_grabowsky_1981]] [[Hollis et al 1999][research_hollis_brandon_1999]] [[Holman and Tuozzolo 2009][research_holman_tuozzolo_2009]] [[Hosseini et al 2025][research_hosseini_hofmann_2025]] [[Howell 1988][research_howell_1988]] [[Hu et al 2009][research_hu_qu_2009]] [[Hu et al 2024][research_hu_yu_2024]] [[Hu et al 2026][research_hu_traisnel_2026]] [[Hughes and Wernicke 1974][research_hughes_wernicke_1974]] [[Hur and Valasek 2003][research_hur_valasek_2003]] [[Iaconis and D'Emilia 1994][research_iaconis_demilia_1994]] [[Idsardi 1983][research_idsardi_1983]] [[Iliff and Maine 1983][research_iliff_maine_1983]] [[In-flight deflection measurement of the HiMAT aeroelastically tailored wing][research_himat_deflection]] [[Incorporating agility flight test 1994][research_incorporating_agility_1994]] [[Introduction to Stability and 2003][research_introduction_to_2003]] [[Iriarte et al 2021][research_iriarte_aginaga_2021]] [[Ishii et al 2005][research_ishii_gomi_2005]] [[Jain et al 2025][research_jain_singla_2025]] [[Jategaonkar et al 2004][research_jategaonkar_fischenberg_2004]] [[Jenkins et al 1977][research_jenkins_kuhl_1977]] [[Jenkins, Jerald M. and Kuhl, Albert E. 1977][research_jenkinsjeraldm_kuhlalberte_1977]] [[Kaletka and Fu 1993][research_kaletka_fu_1993]] [[Kannemans 1995][research_kannemans_1995]] [[Kelly 1974][research_kelly_1974]] [[Kelly 1988][research_kelly_1988]] [[Kim 2004][research_kim_2004]] [[Kim et al 2013][research_kim_ahn_2013]] [[King 1944][research_king_1944]] [[Klabes et al 2018][research_klabes_callsen_2018]] [[Klimek 2024][research_klimek_2024]] [[Knighton 1992][research_knighton_1992]] [[Kobow et al 2026][research_kobow_wennemann_2026]] [[Kobusch and Eichstädt 2017][research_kobusch_eichstadt_2017]] [[Koeniguer and Spear 2018][research_koeniguer_spear_2018]] [[Kokolios 1994][research_kokolios_1994]] [[Krasuski and Bakuła 2021][research_krasuski_bakua_2021]] [[Krings et al 2013][research_krings_henning_2013]] [[Kukreja 2009][research_kukreja_2009]] [[Kukreja and Brenner][research_kukreja_brenner]] [[Kulhánek 2019][research_kulhanek_2019]] [[Kumar and Ghosh 2017][research_kumar_ghosh_2017]] [[Kumar and Ghosh 2023][research_kumar_ghosh_2023]] [[Kumar et al 2008][research_kumar_ganguli_2008]] [[Kuppuswamy and Kiran 1981][research_kuppuswamy_kiran_1981]] [[Kutluay et al 2009][research_kutluay_mahmutyazicioglu_2009]] [[Laban and Masui 1993][research_laban_masui_1993]] [[Lamour 2014][research_lamour_2014]] [[Lamy 1983][research_lamy_1983]] [[Lang 1981][research_lang_1981]] [[Large et al 1981][research_large_may_1981]] [[Larsson 2019][research_larsson_2019]] [[Layton 1986][research_layton_1986]] [[Lekou and Mouzakis 2009][research_lekou_mouzakis_2009]] [[Levchenko 1987][research_levchenko_1987]] [[Level Flight Performance Flight 2003][research_level_flight_2003]] [[Lieberman 1963][research_lieberman_1963]] [[Lim et al 2000][research_lim_sreenatha_2000]] [[Lin 1983][research_lin_1983]] [[Lind and Brenner 1998][research_lind_brenner_1998]] [[Lind and Brenner 1999][research_lind_brenner_1999]] [[Lind and Brenner 1999][research_lind_brenner_1999_b]] [[Liu et al 2023][research_liu_pang_2023]] [[Liu et al 2023][research_liu_wang_2023]] [[Lo and Chan][research_lo_chan]] [[Lokos et al 2002][research_lokos_olney_2002_b]] [[Lokos et al 2005][research_lokos_lizotte_2005]] [[Lokos, William A. and Stauf, Rick 2004][research_lokoswilliama_staufrick_2004]] [[Lokos, William A. et al 2015][research_lokoswilliama_millerericj_2015]] [[Londono and Leonhardt 2012][research_londono_leonhardt_2012]] [[Long 1968][research_long_1968]] [[Longitudinal Control And Trim 2003][research_longitudinal_control_2003]] [[Lykins and Keshmiri 2010][research_lykins_keshmiri_2010]] [[Macmillan 1981][research_macmillan_1981]] [[Mandal and Gu 2016][research_mandal_gu_2016]] [[Mansfield 1953][research_mansfield_1953]] [[Martin 1978][research_martin_1978]] [[Martin Co Denver Co 1966][research_martincodenverco_1966]] [[Maslan et al 2018][research_maslan_sira_2018]] [[Matheny and Panageas 1981][research_matheny_panageas_1981]] [[Maunder 1979][research_maunder_1979]] [[McClintock 1959][research_mcclintock_1959]] [[Mckenzie 1973][research_mckenzie_1973]] [[Mcnally and Bach, Jr. 1988][research_mcnally_bachjr_1988]] [[McQuinn and Valasek 2025][research_mcquinn_valasek_2025]] [[Mehra, R. K. and Eupta, N. K. 1975][research_mehrark_euptank_1975]] [[Mehra, R. K. and Tyler, J. S. 1973][research_mehrark_tylerjs_1973]] [[Mehta et al 2017][research_mehta_marland_2017]] [[Mertaugh 1998][research_mertaugh_1998]] [[Meyer, Jr. and Schneider 1983][research_meyerjr_schneider_1983]] [[Miller et al 2011][research_miller_decallafon_2011]] [[Miller et al 2019][research_miller_pena_2019]] [[Miller, Jr. 1973][research_millerjr_1973]] [[Miodushevsky and Ruggiero 2000][research_miodushevsky_ruggiero_2000]] [[Mohamed and Dongare 2021][research_mohamed_dongare_2021]] [[Montel and Thielecke 2015][research_montel_thielecke_2015]] [[Mordfin and Bloss 1962][research_mordfin_bloss_1962]] [[Morelli 2011][research_morelli_2011]] [[Morelli 2012][research_morelli_2012]] [[Morelli and Klein 1995][research_morelli_klein_1995]] [[Morger 1988][research_morger_1988]] [[Nakadate 2005][research_nakadate_2005]] [[Nicolaides 1976][research_nicolaides_1976]] [[Nicolas et al 2016][research_nicolas_sullivan_2016]] [[Niculescu et al 2021][research_niculescu_corcau_2021]] [[Nieminen et al 2023][research_nieminen_tuohineva_2023]] [[Nisbet et al 1958][research_nisbet_brennan_1958]] [[Nisbet et al 1960][research_nisbet_brennan_1960]] [[Niven and Tait 2000][research_niven_tait_2000]] [[Norton 1990][research_norton_1990]] [[Ockier et al 2017][research_ockier_kolb_2017]] [[Oelker and Friehmelt 1998][research_oelker_friehmelt_1998]] [[Ogren et al 1974][research_ogren_sotanski_1974]] [[Overload Detection System Using 2023][research_overload_detection_2023]] [[Padua and Preisighe Viana 2025][research_padua_preisigheviana_2025]] [[Pang et al 2025][research_pang_yin_2025]] [[Paris and Alaverdi 2005][research_paris_alaverdi_2005]] [[Pawlak 1994][research_pawlak_1994]] [[Peele, E. L. and Eckstrom, C. V. 1975][research_peeleel_eckstromcv_1975]] [[Pendleton et al 1998][research_pendleton_bessette_1998]] [[Pendleton et al 2007][research_pendleton_flick_2007]] [[Peng et al 2024][research_peng_wang_2024]] [[Peschel and Röske 2000][research_peschel_roske_2000]] [[Petersen 1981][research_petersen_1981]] [[Petronevich et al 2021][research_petronevich_lyutov_2021]] [[Philipsen and Zhai 2007][research_philipsen_zhai_2007]] [[Picard 2002][research_picard_2002]] [[Plaetschke et al 1982][research_plaetschke_mulder_1982]] [[Porterfield and Alexander 1970][research_porterfield_alexander_1970]] [[Prato et al 2026][research_prato_facello_2026]] [[Production support flight control computers, research capability for F/A-18 aircraft at Dryden Flight Research Center][research_psfcc]] [[Qiu and Wang 2021][research_qiu_wang_2021]] [[Qu et al 2025][research_qu_xu_2025]] [[Raab 2014][research_raab_2014]] [[Raab 2026][research_raab_2026]] [[Raisinghani and Adak 1983][research_raisinghani_adak_1983]] [[Raisinghani and Kumar 1995][research_raisinghani_kumar_1995]] [[Rakin 1981][research_rakin_1981]] [[Raol and Singh 2023][research_raol_singh_2023_b]] [[Ratcliff et al 2016][research_ratcliff_bodkin_2016]] [[Reasor et al 2016][research_reasor_bhamidipati_2016]] [[Rediess and Melton 1994][research_rediess_melton_1994]] [[Reschke 2005][research_reschke_2005]] [[Rester and A. C. 1984][research_rester_ac_1984]] [[Rester and Alfred C. 1988][research_rester_alfredc_1988]] [[Rhoads 1952][research_rhoads_1952]] [[Richter et al 2023][research_richter_khalifa_2023]] [[Riemersma and Lammertink 1988][research_riemersma_lammertink_1988]] [[Rising 1982][research_rising_1982]] [[Roberts et al 1966][research_roberts_smith_1966]] [[Roeser and Mönnich 2024][research_roeser_monnich_2024]] [[Ruiz Garcia et al 2022][research_ruizgarcia_brown_2022]] [[Ruler 1967][research_ruler_1967]] [[Rustenburg 1973][research_rustenburg_1973]] [[S.A. Gee et al][research_sagee_akylas]] [[Saric 2010][research_saric_2010]] [[Sarnico 1993][research_sarnico_1993]] [[Schajer 2021][research_schajer_2021]] [[Schwanz and Grimes 1980][research_schwanz_grimes_1980]] [[Schäck 2020][research_schack_2020]] [[Shi et al 2023][research_shi_wang_2023]] [[Shi et al 2023][research_shi_zuo_2023]] [[Shock location dominated transonic flight loads on the active aeroelastic wing][research_aaw_shock_loads]] [[Simpson 1972][research_simpson_1972]] [[Simulation in support of 1988][research_simulation_in_1988]] [[Sinske et al 2018][research_sinske_govers_2018]] [[Smith et al 2003][research_smith_moes_2003]] [[Sneshko et al 2005][research_sneshko_chetvergov_2005]] [[Socha and Izydorczyk 2024][research_socha_izydorczyk_2024]] [[Staley 1976][research_staley_1976]] [[Stalford 1980][research_stalford_1980]] [[Stange 1959][research_stange_1959]] [[Starr et al 2011][research_starr_olds_2011]] [[Static Longitudinal Stability Flight 2003][research_static_longitudinal_2003]] [[Stengel 1983][research_stengel_1983]] [[Stepanova 2025][research_stepanova_2025]] [[Stevenson 1991][research_stevenson_1991]] [[Stewart and Bauer 1983][research_stewart_bauer_1983]] [[Strain gage loads calibration testing of the active aeroelastic wing F/A-18 aircraft][research_strain_gage_calibration]] [[Strain Gauge Bonding Service 1975][research_strain_gauge_1975]] [[Strain Gauge Specifications 1967][research_strain_gauge_1967]] [[Strain Gauge Symposium and 1965][research_strain_gauge_1965]] [[Strang 1943][research_strang_1943]] [[Subramanya and Prasad 2013][research_subramanya_prasad_2013]] [[Sun et al 2018][research_sun_schilder_2018]] [[Svec 1981][research_svec_1981]] [[Svendsen 1994][research_svendsen_1994]] [[Sykes][research_sykes]] [[Szymanski et al 2025][research_szymanski_ghazi_2025]] [[Sóbester 2021][research_sobester_2021]] [[Taha et al 2011][research_taha_tang_2011]] [[Tai et al 2023][research_tai_wang_2023]] [[Tantrairatn and Veres 2015][research_tantrairatn_veres_2015]] [[Taranto and Abdulrahim 2023][research_taranto_abdulrahim_2023]] [[Tartabini et al 2016][research_tartabini_gilbert_2016]] [[Taylor 2012][research_taylor_2012]] [[Taylor et al 1992][research_taylor_bennett_1992]] [[Tegelaar 1984][research_tegelaar_1984]] [[Teng and Fan 2025][research_teng_fan_2025]] [[The Saunders-Roe Technograph Foil 1952][research_the_saunders_roe_1952]] [[Thienel et al 1998][research_thienel_lewis_1998]] [[Tischler 2018][research_tischler_2018]] [[Tischler and Zivan 2007][research_tischler_zivan_2007]] [[Tomaine, R. L. et al 1978][research_tomainerl_bryantwh_1978]] [[Tracy 1981][research_tracy_1981]] [[Travassos and Kaufman 1979][research_travassos_kaufman_1979]] [[Tsonev and Kuzmanov 2022][research_tsonev_kuzmanov_2022]] [[Ulbrich 2011][research_ulbrich_2011]] [[Ulbrich 2024][research_ulbrich_2024]] [[Van Gaasbeek 1980][research_vangaasbeek_1980]] [[Van Graas et al 1994][research_vangraas_diggle_1994]] [[Van Pelt 1981][research_vanpelt_1981]] [[Van Wyckhouse 1966][research_vanwyckhouse_1966]] [[Vanwalleghem et al 2015][research_vanwalleghem_debaere_2015]] [[Verstynen, Jr. 1974][research_verstynenjr_1974]] [[Vincent and Franklin 1981][research_vincent_franklin_1981]] [[Volobuyev et al 2017][research_volobuyev_gorbushin_2017]] [[Voracek et al 2002][research_voracek_reaves_2002]] [[Walendziuk 2018][research_walendziuk_2018]] [[Wallace 1978][research_wallace_1978]] [[Wallace 2000][research_wallace_2000]] [[Wang and Iliff 2004][research_wang_iliff_2004]] [[Wang et al 1986][research_wang_demiroz_1986]] [[Wang et al 2022][research_wang_tai_2022]] [[Wang et al 2023][research_wang_xing_2023]] [[Wang et al 2024][research_wang_li_2024]] [[Ward 1988][research_ward_1988]] [[Wei and Zhang 2024][research_wei_zhang_2024]] [[Weinstein et al 2018][research_weinstein_hubbard_2018]] [[Wells and Keskar 1979][research_wells_keskar_1979]] [[Wells et al 1981][research_wells_banda_1981]] [[Wells et al 1982][research_wells_banda_1982]] [[Whitbeck et al 1982][research_whitbeck_smith_1982]] [[White 1973][research_white_1973]] [[Wieland 2025][research_wieland_2025]] [[Wildschek et al 2009][research_wildschek_maier_2009]] [[Wilson][research_wilson]] [[Wilson et al 2016][research_wilson_ryan_2016]] [[Wingrove, R. C. 1978][research_wingroverc_1978]] [[Winters et al 1991][research_winters_hassan_1991]] [[Wolf and Bossert 2001][research_wolf_bossert_2001]] [[Woodrow et al 2013][research_woodrow_tischler_2013]] [[Woodruff 2009][research_woodruff_2009]] [[Woolf 2012][research_woolf_2012]] [[Xiao et al 2011][research_xiao_li_2011]] [[Xu and West 1990][research_xu_west_1990]] [[Yavuztürk et al 2017][research_yavuzturk_topbas_2017]] [[Yee 1992][research_yee_1992]] [[Yu et al 2013][research_yu_zhao_2013]] [[Yuan 2026][research_yuan_2026]] [[Zhang and Cheng 2025][research_zhang_cheng_2025]] [[Zhang and Cheng 2026][research_zhang_cheng_2026]] [[Zhang et al 2013][research_zhang_yang_2013]] [[Zhao et al 2025][research_zhao_zhang_2025]] [[Zhavyrkin and Sladkova 2023][research_zhavyrkin_sladkova_2023]] [[Zhou et al 2013][research_zhou_xu_2013]] [[Zhuang and Lei 2020][research_zhuang_lei_2020]] [[Zubin 1998][research_zubin_1998]] [[Çelik and Metin 2026][research_celik_metin_2026]] [[Ştefănescu 2020][research_stefanescu_2020]]

### Shaping a wing so that it bends usefully

**Aeroelastic tailoring, composite covers, wing boxes and the morphing literature that grew out of them.** **The classical answer to a flexible wing is to stiffen it and stiffness is weight**, and this shelf is the eighty-year argument about whether there is another answer.

**383 records.** [[Abdelkader et al 2011][research_abdelkader_harmin_2011]] [[Abdi, F. et al 1988][research_abdif_ideh_1988]] [[Abdullah and Sulaeman 2013][research_abdullah_sulaeman_2013]] [[Abdulrahim et al 2004][research_abdulrahim_garcia_2004]] [[Abraham-Doman and Merrett 2014][research_abrahamdoman_merrett_2014]] [[Aero structural optimization for 2018][research_aero_structural_2018]] [[Ahmadi and Farsadi 2024][research_ahmadi_farsadi_2024]] [[Alsaidi et al 2018][research_alsaidi_akbar_2018]] [[Alsaidi et al 2018][research_alsaidi_akbar_2018_b]] [[Alsaidi et al 2019][research_alsaidi_joe_2019]] [[Alsaidi et al 2019][research_alsaidi_joe_2019_b]] [[Alulema et al 2020][research_alulema_valencia_2020]] [[Alvarez and Wissa 2021][research_alvarez_wissa_2021]] [[Alyanak and Pendleton 2014][research_alyanak_pendleton_2014]] [[Alyanak and Pendleton 2017][research_alyanak_pendleton_2017]] [[Amendola et al 2018][research_amendola_dimino_2018]] [[Ameri et al 2007][research_ameri_lowenberg_2007]] [[American Institute of Aeronautics and Astronautics 1993][research_americaninstituteofaeronauticsandastronautics_1993]] [[Andakhshideh and Tahani 2013][research_andakhshideh_tahani_2013]] [[Arizono and Isogai 2005][research_arizono_isogai_2005]] [[Austin et al 1976][research_austin_hadcock_1976]] [[Ayaz et al 2024][research_ayaz_rasoolmemon_2024]] [[Azzi et al 2024][research_azzi_tahiliani_2024]] [[Balon et al 2021][research_balon_benes_2021]] [[Bang et al 2022][research_bang_rana_2022]] [[Bartels et al 2019][research_bartels_stanford_2019]] [[Bartels et al 2019][research_bartels_stanford_2019_b]] [[Beatty et al 1977][research_beatty_brooks_1977]] [[Beaverstock et al 2015][research_beaverstock_woods_2015]] [[Bilgen et al 2011][research_bilgen_saavedraflores_2011]] [[Blair and Canfield 2002][research_blair_canfield_2002]] [[Bohlmann et al 1988][research_bohlmann_weisshaar_1988]] [[Bohlmann et al 1992][research_bohlmann_love_1992]] [[Bohlmann, Jonathan D. and Scott, Robert C. 1991][research_bohlmannjonathand_scottrobertc_1991]] [[Bonnema and Smith 1988][research_bonnema_smith_1988]] [[Bonnema, Kenneth L. and Lokos, William A. 1989][research_bonnemakennethl_lokoswilliama_1989]] [[Bordogna et al 2016][research_bordogna_macquart_2016]] [[Bordogna et al 2020][research_bordogna_lancelot_2020]] [[Botez et al 2018][research_botez_koreanschi_2018]] [[Cao and Lyu 2024][research_cao_lyu_2024]] [[Cao et al 2024][research_cao_zhao_2024]] [[Cao et al 2025][research_cao_lin_2025]] [[Carrillo et al 2024][research_carrillo_debreuker_2024]] [[Cavagna et al 2011][research_cavagna_ricci_2011]] [[Cen et al 2025][research_cen_xu_2025]] [[Cen et al 2026][research_cen_xu_2026]] [[Cesnik 2002][research_cesnik_2002]] [[Cesnik 2005][research_cesnik_2005]] [[Cesnik et al 2000][research_cesnik_ortegamorales_2000]] [[Chae et al 2017][research_chae_moosavian_2017]] [[Chen and Han 2017][research_chen_han_2017]] [[Chen et al 2015][research_chen_zhou_2015]] [[Cheng et al 2025][research_cheng_song_2025]] [[Choi et al 2020][research_choi_lim_2020]] [[Clark 2001][research_clark_2001]] [[Dale et al 2013][research_dale_cooper_2013]] [[Dale et al 2014][research_dale_cooper_2014]] [[De Breuker et al 2018][research_debreuker_binder_2018]] [[De Gaspari et al 2015][research_degaspari_ricci_2015]] [[Decamp and Hardy 1984][research_decamp_hardy_1984]] [[Delgado Regis et al 2004][research_delgadoregis_mattos_2004]] [[Dillenius and Mcintosh, Jr. 1988][research_dillenius_mcintoshjr_1988]] [[Dimino et al 2021][research_dimino_andreutti_2021]] [[Dubnický et al 2023][research_dubnicky_splichal_2023]] [[Dunning et al 2014][research_dunning_stanford_2014]] [[Eastep et al 1999][research_eastep_tischler_1999]] [[Eguea][research_eguea]] [[Eldwaib et al 2018][research_eldwaib_grbovic_2018]] [[Elham and Bahamonde Jacome 2016][research_elham_bahamondejacome_2016]] [[Elham and Timmer 2016][research_elham_timmer_2016]] [[Elshazly et al 2025][research_elshazly_kassem_2025]] [[Eraslan and Oktay 2023][research_eraslan_oktay_2023]] [[Eraslan and Oktay 2024][research_eraslan_oktay_2024]] [[España and Gilyard 1995][research_espana_gilyard_1995]] [[Espńa and Gilyard 1994][research_espna_gilyard_1994]] [[Fasel 2020][research_fasel_2020]] [[Feng et al 2015][research_feng_liu_2015]] [[Feng et al 2015][research_feng_liu_2015_b]] [[Fichera et al 2019][research_fichera_isnardi_2019]] [[Flexible manufacturing cell for 2003][research_flexible_manufacturing_2003]] [[Flight test results from a supercritical mission adaptive wing with smooth variable camber][research_mission_adaptive_flight]] [[Fonte et al 2018][research_fonte_iannaccone_2018]] [[Friedmann et al 1992][research_friedmann_venkatesan_1992]] [[Gamboa and Santos 2016][research_gamboa_santos_2016]] [[Gandhi et al 2009][research_gandhi_cooper_2009]] [[Ganguli and Chopra 1997][research_ganguli_chopra_1997]] [[Garcia et al 2003][research_garcia_abdulrahim_2003]] [[Gasbarri et al 2009][research_gasbarri_chiwiacowsky_2009]] [[Gautham Vigneswar et al 2025][research_gauthamvigneswar_ali_2025]] [[Gautham Vigneswar et al 2025][research_gauthamvigneswar_ali_2025_b]] [[Georgiou et al 2012][research_georgiou_manan_2012]] [[Gern and Librescu 2000][research_gern_librescu_2000]] [[Giese et al 1996][research_giese_reich_1996]] [[Gimmestad 1981][research_gimmestad_1981]] [[Giraud et al 2021][research_giraud_raibaudo_2021]] [[Green 1986][research_green_1986]] [[Green 1987][research_green_1987]] [[Griffin][research_griffin]] [[Grigorie and Botez 2014][research_grigorie_botez_2014]] [[Grigorie and Botez 2018][research_grigorie_botez_2018]] [[Grigorie et al 2009][research_grigorie_botez_2009]] [[Grigorie et al 2011][research_grigorie_popov_2011]] [[Gupta 2012][research_gupta_2012]] [[Haider et al 2022][research_haider_ajaj_2022]] [[Haider et al 2023][research_haider_ajaj_2023]] [[He et al 2023][research_he_wang_2023]] [[Heaney and Quindlen 2024][research_heaney_quindlen_2024]] [[Henry et al 2017][research_henry_molinari_2017]] [[Herencia et al 2007][research_herencia_weaver_2007]] [[Hu][research_hu]] [[Hu et al 2025][research_hu_dai_2025]] [[Hua et al 2025][research_hua_wang_2025]] [[Huang et al 2024][research_huang_wang_2024]] [[Huang et al 2025][research_huang_fraihat_2025]] [[Iannuzzo et al 2018][research_iannuzzo_russo_2018]] [[Ibren et al 2020][research_ibren_sulaeman_2020]] [[Islam et al 2025][research_islam_rahman_2025]] [[Islam et al 2025][research_islam_rahman_2025_b]] [[Islam et al 2026][research_islam_rahman_2026]] [[Isogai 1988][research_isogai_1988]] [[Isogai 1989][research_isogai_1989]] [[Jha and Chattopadhyay 1999][research_jha_chattopadhyay_1999]] [[Jia et al 2022][research_jia_zhang_2022]] [[Jia et al 2023][research_jia_zhang_2023]] [[Jiang and Yang 2026][research_jiang_yang_2026]] [[Jin et al 2013][research_jin_song_2013]] [[Jing and Zhang 2017][research_jing_zhang_2017]] [[Jini Raj et al 2023][research_jiniraj_bruceralphinrose_2023]] [[Jo and Majid 2023][research_jo_majid_2023]] [[Jodin et al 2017][research_jodin_scheller_2017]] [[John F Quindlen et al][research_johnfquindlen_danielmortega]] [[Joo et al 2015][research_joo_marks_2015]] [[Jun et al 2014][research_jun_harmin_2014]] [[Jutte, Christine and Stanford, Bret K. 2014][research_juttechristine_stanfordbretk_2014]] [[Kalaji 2023][research_kalaji_2023]] [[Kapania and Chun 2003][research_kapania_chun_2003]] [[Kapase et al 2026][research_kapase_joshi_2026]] [[Karpel and Sheena 1989][research_karpel_sheena_1989]] [[Karpel et al 2000][research_karpel_moulin_2000]] [[Karpouzian and Librescu 1991][research_karpouzian_librescu_1991]] [[Katagiri et al 2024][research_katagiri_park_2024]] [[Katam et al 2005][research_katam_lebeau_2005]] [[Kaufman et al 1996][research_kaufman_balabanov_1996]] [[Kaygan and Ulusoy 2018][research_kaygan_ulusoy_2018]] [[Keidel et al 2019][research_keidel_molinari_2019]] [[Keidel et al 2020][research_keidel_lienhard_2020]] [[Khot et al 2002][research_khot_zweber_2002]] [[Kim et al 2007][research_kim_kim_2007]] [[Kimaru and Bouferrouk 2017][research_kimaru_bouferrouk_2017]] [[Kirsch et al 2020][research_kirsch_montagnier_2020]] [[Koo 2001][research_koo_2001]] [[Koohi et al 2014][research_koohi_shahverdi_2014]] [[Kopsaftopoulos et al 2015][research_kopsaftopoulos_nardari_2015]] [[Koreanschi et al 2014][research_koreanschi_oliviu_2014]] [[Koreanschi et al 2016][research_koreanschi_oliviu_2016]] [[Krüger et al 2022][research_kruger_meddaikar_2022]] [[Kuder et al 2014][research_kuder_arrieta_2014]] [[Larson 1986][research_larson_1986]] [[Leal et al 2017][research_leal_petterson_2017]] [[Leal et al 2018][research_leal_stroud_2018]] [[Leal et al 2018][research_leal_white_2018]] [[Lebofsky et al 2015][research_lebofsky_ting_2015]] [[Lebofsky et al 2015][research_lebofsky_ting_2015_b]] [[Leitch et al 2024][research_leitch_stodieck_2024]] [[Leitch et al 2025][research_leitch_stodieck_2025]] [[Li and Ang 2016][research_li_ang_2016]] [[Li and Li 2016][research_li_li_2016]] [[Li et al 2019][research_li_zhang_2019]] [[Li et al 2022][research_li_ge_2022]] [[Li et al 2025][research_li_wang_2025]] [[Liang and Qin 2012][research_liang_qin_2012]] [[Liu et al 2013][research_liu_zhu_2013]] [[Liu et al 2015][research_liu_zhou_2015]] [[Liu et al 2020][research_liu_gao_2020]] [[Liu et al 2023][research_liu_zhang_2023]] [[Liu et al 2026][research_liu_qian_2026]] [[Lobo do Vale et al 2021][research_lobodovale_raffaelli_2021]] [[Love and Bohlmann 1991][research_love_bohlmann_1991]] [[Lynch and Rogers 1976][research_lynch_rogers_1976]] [[M. V. Sunil and Menghal 2022][research_mvsunil_menghal_2022]] [[Ma et al 2023][research_ma_liu_2023]] [[Macquart et al 2016][research_macquart_werter_2016]] [[Magar et al 2018][research_magar_fuchi_2018]] [[Maki 2016][research_maki_2016]] [[Manan and Cooper 2008][research_manan_cooper_2008]] [[Marano et al 2022][research_marano_belardo_2022]] [[Marciniuk et al 2024][research_marciniuk_piskur_2024]] [[Marks et al 2015][research_marks_zientarski_2015]] [[Marks et al 2016][research_marks_zientarski_2016]] [[Mason and Iglesias 2001][research_mason_iglesias_2001]] [[Meirovitch 1995][research_meirovitch_1995]] [[Melville 2021][research_melville_2021]] [[Menshchikov and Somov 2019][research_menshchikov_somov_2019]] [[Mihaila-Andres et al 2017][research_mihailaandres_larco_2017]] [[Mihaila-Andres et al 2017][research_mihailaandres_rosu_2017]] [[Miskin and Takahashi 2018][research_miskin_takahashi_2018]] [[Mission adaptive wing test program][research_mission_adaptive_wing]] [[Mkhoyan et al 2020][research_mkhoyan_thakrar_2020]] [[Mkhoyan et al 2021][research_mkhoyan_thakrar_2021]] [[Mkhoyan et al 2024][research_mkhoyan_wang_2024]] [[Montgomery and Hunsaker 2022][research_montgomery_hunsaker_2022]] [[Moon 1996][research_moon_1996]] [[Moosavian 2021][research_moosavian_2021]] [[Morphing WING REAL TIME 2010][research_morphing_wing_2010]] [[Morphing Wing Technologies 2018][research_morphing_wing_2018]] [[Najmi et al 2023][research_najmi_siddiqui_2023]] [[Namdeo et al 2023][research_namdeo_bhattacharyya_2023]] [[Navardi et al 2023][research_navardi_shahverdi_2023]] [[Navardi et al 2026][research_navardi_shahverdi_2026]] [[Navrátil et al 2024][research_navratil_hostinsky_2024]] [[Nguyen et al 2013][research_nguyen_ting_2013]] [[Nguyen et al 2015][research_nguyen_ting_2015]] [[Nguyen et al 2015][research_nguyen_precup_2015]] [[Nguyen et al 2019][research_nguyen_cramer_2019]] [[Nguyen et al 2020][research_nguyen_cramer_2020]] [[Nguyen, Nhan et al 2015][research_nguyennhan_kaulupender_2015]] [[Nixon et al 2000][research_nixon_piatak_2000]] [[Nixon, Mark W. et al 1999][research_nixonmarkw_piatakdavidj_1999]] [[Noevere and Wilhite 2016][research_noevere_wilhite_2016]] [[Norton 1989][research_norton_1989]] [[Null and Shkarayev 2004][research_null_shkarayev_2004]] [[Null and Shkarayev 2005][research_null_shkarayev_2005]] [[Obradovic and Subbarao 2010][research_obradovic_subbarao_2010]] [[Olivett et al 2020][research_olivett_corrao_2020]] [[Opgenoord and Willcox 2018][research_opgenoord_willcox_2018]] [[Othman et al 2019][research_othman_silva_2019]] [[Ouyang et al 2013][research_ouyang_chen_2013]] [[Oz et al 2025][research_oz_ekici_2025]] [[Ozbek et al 2023][research_ozbek_ekici_2023]] [[Ozbek et al 2024][research_ozbek_ekici_2024]] [[Palacios et al 2009][research_palacios_glaz_2009]] [[Palaia et al 2025][research_palaia_salem_2025]] [[Papila and Haftka 1999][research_papila_haftka_1999]] [[Patil and Patil 1997][research_patil_patil_1997]] [[Pecora 2018][research_pecora_2018]] [[Pecora and Pecora 2018][research_pecora_pecora_2018]] [[Pecora et al 2021][research_pecora_amoroso_2021]] [[Perera and Guo 2008][research_perera_guo_2008]] [[Peter and Stumpf 2018][research_peter_stumpf_2018]] [[Petermeier et al 2010][research_petermeier_radtke_2010]] [[Pines and Newman 1974][research_pines_newman_1974]] [[Pitt 2004][research_pitt_2004]] [[Poomadath and Ajaj 2025][research_poomadath_ajaj_2025]] [[Popelka et al 1997][research_popelka_lindsay_1997]] [[Powers et al 1992][research_powers_webb_1992]] [[Prabhakar 2025][research_prabhakar_2025]] [[Prabhakar and Murugan 2022][research_prabhakar_murugan_2022]] [[Prabhakar and Murugan 2026][research_prabhakar_murugan_2026]] [[Precup et al 2018][research_precup_mor_2018]] [[Psarros and Savaidis 2025][research_psarros_savaidis_2025]] [[Punzi et al 2024][research_punzi_crooks_2024]] [[Qian and Alonso 2021][research_qian_alonso_2021]] [[Rade and de Souza 2016][research_rade_desouza_2016]] [[Radestock et al 2018][research_radestock_falken_2018]] [[Rahn, D. and Reinertson, L. 1986][research_rahnd_reinertsonl_1986]] [[Rajpal et al 2021][research_rajpal_mitrotta_2021]] [[Reduction of structural loads using maneuver load control on the advanced fighter technology integration F-111 mission adaptive wing][research_afti_mlc]] [[Rehfield et al 1991][research_rehfield_chang_1991]] [[Reist et al 2022][research_reist_koo_2022]] [[Renken 1985][research_renken_1985]] [[Ricci et al 2016][research_ricci_degaspari_2016]] [[Ritter et al 2017][research_ritter_dillinger_2017]] [[Rocha et al 2005][research_rocha_moniz_2005]] [[S et al 2025][research_s_a_2025]] [[Samuels 1982][research_samuels_1982]] [[Sanders et al 2003][research_sanders_eastep_2003]] [[Sanmugadas et al 2021][research_sanmugadas_gupta_2021]] [[Sarojini et al 2022][research_sarojini_solano_2022]] [[Scarth et al 2015][research_scarth_sartor_2015]] [[Schreyer et al 2026][research_schreyer_selm_2026]] [[Schröder and Meijering 2005][research_schroder_meijering_2005]] [[Schweikert et al 2022][research_schweikert_patel_2022]] [[Seber and Sakarya 2010][research_seber_sakarya_2010]] [[Seber and Sakarya 2011][research_seber_sakarya_2011]] [[Segui et al 2017][research_segui_gabor_2017]] [[Setoodeh et al 2005][research_setoodeh_abdallah_2005]] [[Sharifi et al 2025][research_sharifi_vincenti_2025]] [[Shi and Song 2012][research_shi_song_2012]] [[Shirk et al 1984][research_shirk_hertz_1984]] [[Shirk, M. H. et al 1986][research_shirkmh_hertztj_1986]] [[Siler et al 1997][research_siler_volk_1997]] [[Singha 2025][research_singha_2025]] [[Singha and Murugan 2023][research_singha_murugan_2023]] [[Skillen and Crossley 2005][research_skillen_crossley_2005]] [[Smith, Benjamin et al 2020][research_smithbenjamin_brookstimothy_2020]] [[Smith, John W. et al 1992][research_smithjohnw_lockwiltonp_1992]] [[Solano et al 2020][research_solano_sarojini_2020]] [[Soneda et al 2020][research_soneda_yokozeki_2020]] [[Soneda et al 2026][research_soneda_tsushima_2026]] [[Sotoudeh and Hosking 2018][research_sotoudeh_hosking_2018]] [[Soykasap and Hodges 1999][research_soykasap_hodges_1999]] [[Soykasap and Hodges 2000][research_soykasap_hodges_2000]] [[Stacey and Thomas 2019][research_stacey_thomas_2019]] [[Stanford 2014][research_stanford_2014]] [[Stanford 2016][research_stanford_2016]] [[Stanford, Bret K. and Jutte, Christine V. 2014][research_stanfordbretk_juttechristinev_2014]] [[Stodieck et al 2013][research_stodieck_cooper_2013]] [[Stodieck et al 2014][research_stodieck_cooper_2014]] [[Stodieck et al 2015][research_stodieck_cooper_2015]] [[Stodieck et al 2017][research_stodieck_cooper_2017]] [[Structural weight comparison of 1981][research_structural_weight_1981]] [[Sulaeman et al 2017][research_sulaeman_abdullah_2017]] [[Svoboda et al 2023][research_svoboda_hengstermovric_2023]] [[Taflan et al 2023][research_taflan_smith_2023]] [[Taflan et al 2023][research_taflan_smith_2023_b]] [[Takahashi et al 2016][research_takahashi_yokozeki_2016]] [[Tal and Nguyen 2015][research_tal_nguyen_2015]] [[Tao and Bin 2026][research_tao_bin_2026]] [[Thuwis et al][research_thuwis_debreuker]] [[Thuwis et al 2009][research_thuwis_debreuker_2009]] [[Tian et al 2016][research_tian_yang_2016]] [[Tischler and Venkayya 1998][research_tischler_venkayya_1998]] [[Tischler et al 2000][research_tischler_venkayya_2000]] [[Torenbeek 1972][research_torenbeek_1972]] [[Triplett 1979][research_triplett_1979]] [[Triplett 1980][research_triplett_1980]] [[Triplett 1980][research_triplett_1980_b]] [[Tsushima et al 2018][research_tsushima_yokozeki_2018]] [[Tsushima et al 2018][research_tsushima_arizono_2018]] [[Urnes, James, Sr. et al 2013][research_urnesjamessr_nguyennhan_2013]] [[Vale et al 2011][research_vale_leite_2011]] [[Vincent and Botez 2015][research_vincent_botez_2015]] [[Volk et al 1998][research_volk_siler_1998]] [[Vu][research_vu]] [[Vu et al 2005][research_vu_kelkar_2005]] [[Waite et al 2020][research_waite_bartels_2020]] [[Waite et al 2021][research_waite_grauer_2021]] [[Wales et al 2015][research_wales_cheung_2015]] [[Wan et al 2003][research_wan_yang_2003]] [[Wang et al 2019][research_wang_wan_2019]] [[Wang et al 2019][research_wang_wan_2019_b]] [[Wang et al 2021][research_wang_wan_2021]] [[Wang et al 2021][research_wang_hou_2021]] [[Wang et al 2021][research_wang_mkhoyan_2021]] [[Wang et al 2023][research_wang_lei_2023]] [[Wang et al 2023][research_wang_chen_2023]] [[Wang et al 2024][research_wang_zhao_2024]] [[Wang et al 2025][research_wang_xu_2025]] [[Wang et al 2026][research_wang_chen_2026]] [[Wansasueb et al 2023][research_wansasueb_panagant_2023]] [[Weisshaar 1980][research_weisshaar_1980]] [[Weisshaar 1981][research_weisshaar_1981]] [[Weisshaar 1987][research_weisshaar_1987]] [[Weisshaar and Duke 2006][research_weisshaar_duke_2006]] [[Weisshaar and Lee 2002][research_weisshaar_lee_2002]] [[Werner 2018][research_werner_2018]] [[Werter and De Breuker 2016][research_werter_debreuker_2016]] [[Wu et al 2024][research_wu_li_2024]] [[Wunderlich and Dähne 2017][research_wunderlich_dahne_2017]] [[Wunderlich et al 2017][research_wunderlich_dahne_2017_b]] [[Xin and Li 2025][research_xin_li_2025]] [[Yamane 1992][research_yamane_1992]] [[Yamane and Friedmann 1990][research_yamane_friedmann_1990]] [[Yamane and Friedmann 1993][research_yamane_friedmann_1993]] [[Yan et al 2019][research_yan_li_2019]] [[Yang et al 2015][research_yang_sartor_2015]] [[Yang et al 2024][research_yang_xu_2024]] [[Yao et al 2023][research_yao_kan_2023]] [[Yokozeki et al 2014][research_yokozeki_sugiura_2014]] [[You et al 2020][research_you_kim_2020]] [[Yu and He 2016][research_yu_he_2016]] [[Yu et al 2017][research_yu_wang_2017]] [[Yue et al 2017][research_yue_zhang_2017]] [[Yue et al 2017][research_yue_wang_2017]] [[Yurkovich 2009][research_yurkovich_2009]] [[Zaw and Baranovski 2026][research_zaw_baranovski_2026]] [[Zeng et al 2017][research_zeng_qian_2017]] [[Zhang and Wang 2019][research_zhang_wang_2019]] [[Zhang et al 2019][research_zhang_ge_2019]] [[Zhang et al 2020][research_zhang_chen_2020]] [[Zhang et al 2021][research_zhang_shaw_2021]] [[Zhang et al 2025][research_zhang_hou_2025]] [[Zhang et al 2025][research_zhang_kang_2025]] [[Zhang et al 2026][research_zhang_dai_2026]] [[Zhang et al 2026][research_zhang_dai_2026_b]] [[Zhao et al 2024][research_zhao_li_2024]] [[Zhu 2018][research_zhu_2018]] [[Zink et al 1999][research_zink_mavris_1999]] [[Özbek et al 2023][research_ozbek_ekici_2023_b]] [[Świtała and Lipski 2026][research_switala_lipski_2026]] [[Święch 2020][research_swiech_2020]] [[Şahin et al 2018][research_sahin_cakir_2018]] [[Şahin et al 2018][research_sahin_cakir_2018_b]]

### The flow over the wing at these speeds

**Transonic and supersonic aerodynamics, which is where the wing stops behaving.** Shocks, pressure distributions, spanwise loading and aerodynamic derivatives. **The roll rate dipped at Mach 0.95 and the reason is in this cluster**, since a shock moving across the wing moves the centre of pressure that the twist is levering against.

**358 records.** [[A-7 Transonic Wing Designs 1982][research_a_7_transonic_1982]] [[Aerodynamic Phenomena in Supersonic 2020][research_aerodynamic_phenomena_2020]] [[Aeroelasticity Problems in Compressible 2010][research_aeroelasticity_problems_2010]] [[Agarwal and Deese 1983][research_agarwal_deese_1983]] [[Agarwal and Deese 1984][research_agarwal_deese_1984]] [[Agrawal et al 1991][research_agrawal_kinard_1991]] [[Alden and Schindel 1952][research_alden_schindel_1952]] [[An experimental and computational 1978][research_an_experimental_1978]] [[Appendix B Solution to 2016][research_appendix_b_2016]] [[Application of a Shock-Turbulent 1982][research_application_of_1982_b]] [[Application of Computational Methods 1982][research_application_of_1982]] [[Apte and Athani 1979][research_apte_athani_1979]] [[Archambaud et al 2004][research_archambaud_louis_2004]] [[Armstrong and Miller 1968][research_armstrong_miller_1968]] [[Askari and Soltani 2019][research_askari_soltani_2019]] [[Auls'chenko et al 2006][research_aulschenko_zamuraev_2006]] [[Azevedo 1987][research_azevedo_1987]] [[Babinsky and Délery 2011][research_babinsky_delery_2011]] [[Babister 1980][research_babister_1980]] [[Bae et al 2004][research_bae_inman_2004]] [[Baker and Forsey 1981][research_baker_forsey_1981]] [[Barnwell 1974][research_barnwell_1974]] [[Batina 1986][research_batina_1986]] [[Belesiotis-Kataras and Timme 2021][research_belesiotiskataras_timme_2021]] [[Bennett et al 1985][research_bennett_seidel_1985]] [[Bennett et al 1991][research_bennett_dansberry_1991]] [[Bennett et al 1993][research_bennett_dansberry_1993]] [[Beresh et al 2020][research_beresh_barone_2020]] [[Berton 2022][research_berton_2022]] [[Biswas and Jimbo 2015][research_biswas_jimbo_2015]] [[Blank 1995][research_blank_1995]] [[Bodin and Fuchs 2008][research_bodin_fuchs_2008]] [[Boppe 1977][research_boppe_1977]] [[Brown 1989][research_brown_1989]] [[Bryson, Jr. and Desai 1968][research_brysonjr_desai_1968]] [[Burrows et al 2021][research_burrows_vukasinovic_2021]] [[Cahill 1986][research_cahill_1986]] [[Calder and Gupta 1977][research_calder_gupta_1977]] [[Campbell and Smith 1987][research_campbell_smith_1987]] [[Carafoli 1969][research_carafoli_1969]] [[Carlson 1981][research_carlson_1981]] [[Carlson and Weed 1985][research_carlson_weed_1985]] [[Cassel et al 1969][research_cassel_durando_1969]] [[Caughey 1982][research_caughey_1982]] [[Caughey and Jameson 1977][research_caughey_jameson_1977]] [[Chakrabartty and Dhanalakshmi 1995][research_chakrabartty_dhanalakshmi_1995]] [[Chan et al 2017][research_chan_hooker_2017]] [[Chaparro et al 2017][research_chaparro_fujiwara_2017]] [[Chapter 3. Aerodynamics of 1960][research_chapter_3_1960]] [[Chapter 5. Wing-Body Interference 1957][research_chapter_5_1957]] [[Chen 1982][research_chen_1982]] [[Chen et al 1984][research_chen_vassberg_1984]] [[Chen et al 2026][research_chen_zhang_2026]] [[Cheng 1982][research_cheng_1982]] [[Chung 2002][research_chung_2002]] [[Chung et al 2021][research_chung_su_2021]] [[Chyu and Kuwahara 1982][research_chyu_kuwahara_1982]] [[Clark and Valarezo 1990][research_clark_valarezo_1990]] [[Clyde et al 1984][research_clyde_bonner_1984]] [[Cook 1964][research_cook_1964]] [[Cook 1965][research_cook_1965]] [[Cosentino and Holst 1985][research_cosentino_holst_1985]] [[Cox and Roskam 1990][research_cox_roskam_1990]] [[Crasta and Khan 2014][research_crasta_khan_2014]] [[Cunningham 1972][research_cunningham_1972]] [[Currao and Yeh 2026][research_currao_yeh_2026]] [[Dai and Zhang 2023][research_dai_zhang_2023]] [[Dallaire et al 2007][research_dallaire_tribes_2007]] [[Das 2026][research_das_2026]] [[Deconinck and Hirsch 1981][research_deconinck_hirsch_1981]] [[Durston and Stonum 1987][research_durston_stonum_1987]] [[Eastep et al 1998][research_eastep_andersen_1998]] [[Edwards et al 1985][research_edwards_carter_1985]] [[Edwards et al 1986][research_edwards_whitfield_1986]] [[Epstein 1954][research_epstein_1954]] [[Eskandary et al 2012][research_eskandary_dardel_2012]] [[Fagbade and Heinz 2024][research_fagbade_heinz_2024]] [[Farbridge and Smith 1977][research_farbridge_smith_1977]] [[Fitzgerald et al 1994][research_fitzgerald_ralston_1994]] [[Flores and Van Dalsem 1985][research_flores_vandalsem_1985]] [[Foley and Woodrey 1980][research_foley_woodrey_1980]] [[Fornasier and Heiss 1987][research_fornasier_heiss_1987]] [[Forsey 1983][research_forsey_1983]] [[Franciscus 1983][research_franciscus_1983]] [[Fruchtman 1974][research_fruchtman_1974]] [[Fuchs 1981][research_fuchs_1981]] [[Fujii and Obayashi 1986][research_fujii_obayashi_1986]] [[Galloway et al 1992][research_galloway_gelhausen_1992]] [[Gally and Carlson 1987][research_gally_carlson_1987]] [[Gloss and Washburn 1977][research_gloss_washburn_1977]] [[Gloss and Washburn 1978][research_gloss_washburn_1978]] [[Gomillion 1976][research_gomillion_1976]] [[Grasmeyer 1999][research_grasmeyer_1999]] [[Gregg and Misegades 1987][research_gregg_misegades_1987]] [[Guderley 1987][research_guderley_1987]] [[Guderley 1988][research_guderley_1988]] [[Guillot and Friedmann 1994][research_guillot_friedmann_1994_b]] [[Gupta et al 2021][research_gupta_datta_2021]] [[Guruswamy 2019][research_guruswamy_2019]] [[Guruswamy and Tu 1989][research_guruswamy_tu_1989]] [[Guruswamy and Tu 1994][research_guruswamy_tu_1994]] [[Halwas and Aggarwal 2019][research_halwas_aggarwal_2019]] [[Halwas and Aggarwal 2019][research_halwas_aggarwal_2019_b]] [[Hammer and Garmann 2023][research_hammer_garmann_2023]] [[Hartmann 2012][research_hartmann_2012]] [[Hartmann 2013][research_hartmann_2013]] [[Hayabe and Kwak 2025][research_hayabe_kwak_2025]] [[Held and Fuchs 1999][research_held_fuchs_1999]] [[Heltsley and Cline 1979][research_heltsley_cline_1979]] [[Heltsley et al 1981][research_heltsley_crosswy_1981]] [[Hendrickson et al 1978][research_hendrickson_grossman_1978]] [[Henne 1980][research_henne_1980]] [[Henne and Hicks 1978][research_henne_hicks_1978]] [[Hiley and Bowers 1981][research_hiley_bowers_1981]] [[Hinz and Miller 1979][research_hinz_miller_1979]] [[History of Supersonic Transport 2020][research_history_of_2020]] [[Holst and Thomas 1982][research_holst_thomas_1982]] [[Hope and Kunz 2019][research_hope_kunz_2019]] [[Hu 1995][research_hu_1995]] [[Huffman and Fox, Jr. 1985][research_huffman_foxjr_1985]] [[Hybrid Approach to Transonic 1982][research_hybrid_approach_1982]] [[Ide and Shankar 1987][research_ide_shankar_1987]] [[Ide et al 2019][research_ide_ishida_2019]] [[Ilie and Havenar 2023][research_ilie_havenar_2023]] [[Ionela Raluca Maxim 1970][research_ionelaralucamaxim_1970]] [[Israq et al 2025][research_israq_ahmaad_2025]] [[Iyer et al 2017][research_iyer_park_2017]] [[Jameson 1973][research_jameson_1973]] [[Jameson 1977][research_jameson_1977]] [[Jameson 1982][research_jameson_1982]] [[Jameson 2003][research_jameson_2003]] [[Jameson and Caughey 1977][research_jameson_caughey_1977]] [[Jamshidi et al 2016][research_jamshidi_dardel_2016]] [[Janardhan and Grandhi 2003][research_janardhan_grandhi_2003]] [[Jepps 1981][research_jepps_1981]] [[Johnson, C. B. and Kaufman, L. G., III 1979][research_johnsoncb_kaufmanlgiii_1979]] [[Johnston 1998][research_johnston_1998]] [[Jones 1950][research_jones_1950]] [[Jones 1980][research_jones_1980]] [[Jones and Jarrett 2018][research_jones_jarrett_2018]] [[Kady and Takahashi 2014][research_kady_takahashi_2014]] [[Kandil and Menzies 1996][research_kandil_menzies_1996]] [[Kandil et al 1993][research_kandil_kandil_1993]] [[Kandil et al 1994][research_kandil_kalisch_1994]] [[Karania et al 2021][research_karania_mohan_2021]] [[Keener 1984][research_keener_1984]] [[Kehrer 1971][research_kehrer_1971]] [[Kim and Sung 1993][research_kim_sung_1993]] [[Kim and Winchenbach 1986][research_kim_winchenbach_1986]] [[Kim et al 2001][research_kim_obayashi_2001]] [[Kim et al 2006][research_kim_jeon_2006]] [[Kishi et al 2016][research_kishi_kanazaki_2016]] [[Kisslinger and Vetsch 1965][research_kisslinger_vetsch_1965]] [[Klausmeyer 2018][research_klausmeyer_2018]] [[Klopfer and Nielsen 1980][research_klopfer_nielsen_1980]] [[Klug et al 2020][research_klug_radespiel_2020]] [[Klug et al 2023][research_klug_ullah_2023]] [[Ko et al 2003][research_ko_mason_2003]] [[Kolonay and Yang 1998][research_kolonay_yang_1998]] [[Krenz 1979][research_krenz_1979]] [[Kuhlman et al 1988][research_kuhlman_cerney_1988]] [[Kulfan and Vachal 1978][research_kulfan_vachal_1978]] [[Kurade et al 2021][research_kurade_venkatakrishnan_2021]] [[Lan et al 2006][research_lan_bianchi_2006]] [[Larson 1958][research_larson_1958]] [[Laughrey 1969][research_laughrey_1969]] [[Lee and Boedicker 1985][research_lee_boedicker_1985]] [[Leventhal et al 1977][research_leventhal_keel_1977]] [[Li and Geiselhart 2026][research_li_geiselhart_2026]] [[Li and Livne 1995][research_li_livne_1995]] [[Li and Livne 1997][research_li_livne_1997]] [[Li and Qin 2020][research_li_qin_2020_b]] [[Librescu et al 2003][research_librescu_na_2003]] [[Lin 1982][research_lin_1982]] [[Liu 2022][research_liu_2022]] [[Liu 2022][research_liu_2022_b]] [[Liu et al 2023][research_liu_lei_2023]] [[Lombardi et al 1997][research_lombardi_salvetti_1997]] [[Luce and Jr 1949][research_luce_jr_1949]] [[Ly et al 2006][research_ly_gear_2006]] [[M 2026][research_m_2026]] [[Mabey and Gaudet 1975][research_mabey_gaudet_1975]] [[Mack 1979][research_mack_1979]] [[Madson and Ericksont 1985][research_madson_ericksont_1985]] [[Marion and Sharma 2025][research_marion_sharma_2025]] [[Martin and Gerber 1953][research_martin_gerber_1953]] [[Mason 1982][research_mason_1982]] [[Mason 1983][research_mason_1983]] [[Masson et al 1999][research_masson_veilleux_1999]] [[Maute et al 2008][research_maute_farhat_2008]] [[McDonald et al 1982][research_mcdonald_shamroth_1982]] [[McLean 1994][research_mclean_1994]] [[McParlin and Adamczak 2003][research_mcparlin_adamczak_2003]] [[Menzies and Kandil 1996][research_menzies_kandil_1996]] [[Meyer and Fields 1978][research_meyer_fields_1978]] [[Miller and Schemensky 1979][research_miller_schemensky_1979]] [[Miller and Wood 1983][research_miller_wood_1983]] [[Miller et al 1979][research_miller_protopapas_1979]] [[Miskin and Takahashi 2019][research_miskin_takahashi_2019]] [[Morton et al 2012][research_morton_cox_2012]] [[Muhamad Jayadi 2025][research_muhamadjayadi_2025]] [[NACA Conference on Aerodynamic 1949][research_naca_conference_1949]] [[Nadim Melhem et al 2024][research_nadimmelhem_richardmunroe_2024]] [[Nangia and Palmer 2007][research_nangia_palmer_2007]] [[Narain 1983][research_narain_1983]] [[Naylor 1957][research_naylor_1957]] [[Newman, Iii and Baysal 1992][research_newmaniii_baysal_1992]] [[Nguyen and Xiong 2021][research_nguyen_xiong_2021]] [[Nguyen and Xiong 2022][research_nguyen_xiong_2022]] [[Nguyen and Xiong 2023][research_nguyen_xiong_2023_b]] [[Nguyen and Xiong 2023][research_nguyen_xiong_2023_c]] [[Nguyen and Xiong 2024][research_nguyen_xiong_2024]] [[Nguyen and Xiong 2024][research_nguyen_xiong_2024_b]] [[Nilsson et al 2023][research_nilsson_yao_2023]] [[Nomura 2003][research_nomura_2003]] [[Obayashi et al 2000][research_obayashi_sasaki_2000]] [[Oberkampf 1974][research_oberkampf_1974]] [[Ojiaku and Prakash 2026][research_ojiaku_prakash_2026]] [[Owens et al 2003][research_owens_capone_2003]] [[Owens et al 2004][research_owens_capone_2004]] [[Owens et al 2006][research_owens_mcconnell_2006]] [[Padova and Falk 1980][research_padova_falk_1980]] [[Palacios and Cesnik 2005][research_palacios_cesnik_2005]] [[Paniagua 2013][research_paniagua_2013]] [[Patil et al 2000][research_patil_hodges_2000]] [[Paul and Rein 2016][research_paul_rein_2016]] [[Paul and Rein 2017][research_paul_rein_2017]] [[Pfaff 1965][research_pfaff_1965]] [[Plaban and Takahashi 2021][research_plaban_takahashi_2021]] [[Polonsky 2026][research_polonsky_2026]] [[Poole et al 2020][research_poole_allen_2020]] [[Prasannakumar et al 2022][research_prasannakumar_sudhi_2022]] [[Properties and Design of 2012][research_properties_and_2012]] [[Puentes and Takahashi 2024][research_puentes_takahashi_2024]] [[Qin 2012][research_qin_2012]] [[Raghunathan and Coll 1981][research_raghunathan_coll_1981]] [[Raghunathan et al 1998][research_raghunathan_mitchell_1998]] [[Raj 1983][research_raj_1983]] [[Raluca MAXIM 2020][research_ralucamaxim_2020]] [[Rambacher and Bons 2023][research_rambacher_bons_2023]] [[Rao et al 2005][research_rao_behal_2005]] [[Recine et al 2025][research_recine_schuh_2025]] [[Reddy 1987][research_reddy_1987]] [[Regan 1964][research_regan_1964]] [[Requirements of a commercial 1967][research_requirements_of_1967]] [[Reuther and Jameson 1995][research_reuther_jameson_1995]] [[Riou et al 2010][research_riou_garnier_2010]] [[Rizk 1980][research_rizk_1980]] [[Rizzetta 1977][research_rizzetta_1977]] [[Rizzetta 1995][research_rizzetta_1995]] [[Rizzi 1981][research_rizzi_1981]] [[Rizzi 1981][research_rizzi_1981_b]] [[Rizzi 1984][research_rizzi_1984]] [[Rizzi 1995][research_rizzi_1995]] [[Rizzi et al 1986][research_rizzi_purcell_1986]] [[Robins and Carlson 1979][research_robins_carlson_1979]] [[Robins and Carlson 1980][research_robins_carlson_1980]] [[Roohani and Skews 2009][research_roohani_skews_2009]] [[Roos et al 1975][research_roos_bennekers_1975]] [[Rosemann and Birkemeyer 2002][research_rosemann_birkemeyer_2002]] [[Roskam, J. et al 1972][research_roskamj_lanc_1972]] [[Roughen et al 2010][research_roughen_bendiksen_2010]] [[Rumpfkeil et al 2021][research_rumpfkeil_lickenbrock_2021]] [[Russo et al 2020][research_russo_tognaccini_2020]] [[Russo et al 2020][research_russo_tognaccini_2020_b]] [[Sakamura and Komaki 2011][research_sakamura_komaki_2011]] [[Sandford et al 1980][research_sandford_ricketts_1980]] [[Sapkal and Attar 2011][research_sapkal_attar_2011]] [[Sapkal and Attar 2012][research_sapkal_attar_2012]] [[Sartor][research_sartor]] [[Sartor et al 2012][research_sartor_losfeld_2012]] [[Sartor et al 2013][research_sartor_clement_2013]] [[Schmidt 1995][research_schmidt_1995]] [[Schmitt et al 1983][research_schmitt_destarac_1983]] [[Schuelein 2008][research_schuelein_2008]] [[Schuster, David M. and Byrd, James E. 2003][research_schusterdavidm_byrdjamese_2003]] [[Seebass 1982][research_seebass_1982]] [[Seginer and Rose 1976][research_seginer_rose_1976]] [[Seidel et al 1985][research_seidel_sandford_1985]] [[Semionov and Kosinov 2007][research_semionov_kosinov_2007]] [[Sezgin and Krstic 2013][research_sezgin_krstic_2013]] [[Sha et al 2022][research_sha_sun_2022]] [[Shankar and Goebel 1985][research_shankar_goebel_1985]] [[Shankar and Malmuth 1982][research_shankar_malmuth_1982]] [[Shieh 1988][research_shieh_1988]] [[Silva and Bennett 1995][research_silva_bennett_1995]] [[Silva et al 2008][research_silva_mello_2008]] [[Slender Aircraft for Flight 2012][research_slender_aircraft_2012]] [[Smith and Dahlem 1981][research_smith_dahlem_1981]] [[Smith and Shyy 1995][research_smith_shyy_1995]] [[Sorensen and Bencze 1974][research_sorensen_bencze_1974]] [[Sorensen and Smeltzer 1972][research_sorensen_smeltzer_1972]] [[Spaid 1984][research_spaid_1984]] [[Spearman 1979][research_spearman_1979]] [[Spearman et al 1992][research_spearman_tice_1992]] [[Spinner and Rudnik 2023][research_spinner_rudnik_2023]] [[Stengel 1969][research_stengel_1969]] [[Streett 1981][research_streett_1981]] [[Sudhi et al 2021][research_sudhi_radespiel_2021]] [[Sundaram and Wu 1983][research_sundaram_wu_1983]] [[Supersonic Aircraft High-Speed Civil 1997][research_supersonic_aircraft_1997]] [[Supersonic Three-dimensional Wing Theory 1960][research_supersonic_three_dimensional_1960]] [[Supersonic transport wing minimum 1992][research_supersonic_transport_1992]] [[Szema and Shankar 1984][research_szema_shankar_1984]] [[Technical applications for an 1976][research_technical_applications_1976]] [[Tekawade et al 2024][research_tekawade_chandwadkar_2024]] [[Thomas and Holst 1983][research_thomas_holst_1983]] [[Three-dimensional boundary-layer transition on 1994][research_three_dimensional_boundary_layer_1994]] [[Tian et al 2026][research_tian_li_2026]] [[Trankle and Bachner 1993][research_trankle_bachner_1993]] [[Transonic Aircraft Configurations 2012][research_transonic_aircraft_2012]] [[Transonic and supersonic flight 1992][research_transonic_and_1992]] [[Transonic Maneuver/Cruise Airfoil Design 1980][research_transonic_maneuver_cruise_1980]] [[Transonic Wing Shape Design 2015][research_transonic_wing_2015]] [[Transonic, Shock, and Multidimensional 1982][research_transonic_shock_1982]] [[Tucker, Warren A and Nelson, Robert L 1950][research_tuckerwarrena_nelsonrobertl_1950]] [[Turner et al 2025][research_turner_seo_2025]] [[Tursi 2003][research_tursi_2003]] [[Uzun and Malik 2018][research_uzun_malik_2018]] [[Uzun and Malik 2019][research_uzun_malik_2019]] [[Vadyak et al 1987][research_vadyak_smith_1987]] [[Vaughn, Jr. 1982][research_vaughnjr_1982]] [[Velkova 2017][research_velkova_2017]] [[Vukasinovic et al 2013][research_vukasinovic_gissen_2013]] [[Waggoner 1980][research_waggoner_1980]] [[Waggoner 1982][research_waggoner_1982]] [[Wagner 1983][research_wagner_1983]] [[Ward 1949][research_ward_1949]] [[Wasson and Mehus 1967][research_wasson_mehus_1967]] [[Watts 1976][research_watts_1976]] [[Weed et al 1983][research_weed_carlson_1983]] [[Wells 2017][research_wells_2017]] [[Whitford 1991][research_whitford_1991]] [[Wieseman et al 2005][research_wieseman_silva_2005]] [[Williams 1965][research_williams_1965]] [[Williams and Hunt 1980][research_williams_hunt_1980]] [[Wimpress and Swihart 1964][research_wimpress_swihart_1964]] [[Wing Theory in Supersonic 1969][research_wing_theory_1969]] [[Winograd and Miles 1956][research_winograd_miles_1956]] [[Wood and Miller 1985][research_wood_miller_1985]] [[Xiong and Nguyen 2024][research_xiong_nguyen_2024]] [[Xiong et al 2019][research_xiong_fugate_2019]] [[Xiong et al 2021][research_xiong_nguyen_2021]] [[Xiong et al 2023][research_xiong_nguyen_2023]] [[Yamazaki and Kusunose 2016][research_yamazaki_kusunose_2016]] [[Yang et al 2025][research_yang_wu_2025]] [[Yoneyama and Hatamura 1989][research_yoneyama_hatamura_1989]] [[Yonezawa and Obayashi 2010][research_yonezawa_obayashi_2010]] [[Yoshikawa 1982][research_yoshikawa_1982]] [[Yu 1979][research_yu_1979]] [[Yu 1980][research_yu_1980]] [[Yu and Campbell 1992][research_yu_campbell_1992]] [[Yue 2026][research_yue_2026]] [[Zhang et al 2024][research_zhang_tian_2024]] [[Zheng 2010][research_zheng_2010]] [[Zhou et al 2017][research_zhou_chen_2017]] [[Zhu et al 2019][research_zhu_li_2019]] [[Zubin et al 2019][research_zubin_maksimov_2019]]

### Control laws for an aircraft that will not hold its shape

**Where the programme ended up.** Flight control law design for flexible aircraft, control allocation among many surfaces, and aeroservoelastic interaction. **The Active Aeroelastic Wing reduced its own objective to this**, having dropped active flutter suppression from the wind-tunnel programme that preceded it.

**354 records.** [[Abdulrahim et al 2018][research_abdulrahim_weibley_2018]] [[Adamson et al 2019][research_adamson_fichera_2019]] [[Adaptive Transonic Aeroservoelasticity 2016][research_adaptive_transonic_2016]] [[Aeroservoelastic tailoring for lateral control enhancement][research_aeroservoelastic_tailoring]] [[Aeroservoelastic wind-tunnel investigations using the active flexible wing model, status and recent accomplishments][research_afw_tm101570]] [[Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988]] [[Allen and Pollock 1983][research_allen_pollock_1983]] [[Allen et al 1986][research_allen_reardon_1986]] [[Alwi and Edwards 2007][research_alwi_edwards_2007]] [[Alwi and Edwards 2009][research_alwi_edwards_2009]] [[Andersen et al 1997][research_andersen_forster_1997]] [[Andersen et al 1998][research_andersen_kolonay_1998]] [[Antonakis and Biannic 2024][research_antonakis_biannic_2024]] [[Babcock and Lind 2013][research_babcock_lind_2013]] [[Babcock and Lind 2013][research_babcock_lind_2013_b]] [[Baggi et al 2020][research_baggi_franco_2020]] [[Baggi et al 2022][research_baggi_serrani_2022]] [[Bailey et al 1988][research_bailey_powers_1988]] [[Balas et al 2004][research_balas_hindman_2004]] [[Balas et al 2012][research_balas_moreno_2012]] [[Banavara and Newsom 2010][research_banavara_newsom_2010]] [[Barb and Mulder 2003][research_barb_mulder_2003]] [[Beh et al 2018][research_beh_hofinger_2018]] [[Benosman et al 2007][research_benosman_liao_2007]] [[Bian et al 2018][research_bian_nener_2018]] [[Bian et al 2019][research_bian_nener_2019]] [[Binder et al 2021][research_binder_wildschek_2021]] [[Binwen Lu et al 2016][research_binwenlu_jianjunma_2016]] [[Blight et al 2018][research_blight_lanedailey_2018]] [[Bocola et al 2015][research_bocola_muscarello_2015]] [[Bodson 2000][research_bodson_2000]] [[Boskovic and Mehra][research_boskovic_mehra]] [[Boskovic et al][research_boskovic_ling]] [[Botez et al 2008][research_botez_grigorie_2008]] [[Bouadi][research_bouadi]] [[Brenner 2002][research_brenner_2002]] [[Brenner and Lind 1998][research_brenner_lind_1998]] [[Brenner et al 1997][research_brenner_feron_1997]] [[Brenner, Martin J. 1996][research_brennermartinj_1996]] [[Brenner, Martin J. 2001][research_brennermartinj_2001]] [[Brinker and Wise 2000][research_brinker_wise_2000]] [[Brown et al 2017][research_brown_singh_2017]] [[Bucharles and Vacher 2002][research_bucharles_vacher_2002]] [[Buffington 1997][research_buffington_1997]] [[Buffington 1999][research_buffington_1999]] [[Burcham, Jr. and Burken 1994][research_burchamjr_burken_1994]] [[Burton and Kneeland, Jr. 1981][research_burton_kneelandjr_1981]] [[Cabaleiro de la Hoz and Fioriti 2021][research_cabaleirodelahoz_fioriti_2021]] [[Chen 2015][research_chen_2015]] [[Chen et al 2018][research_chen_zhou_2018]] [[Chin][research_chin]] [[Chin et al 1987][research_chin_chacon_1987]] [[Chin et al 2011][research_chin_brenner_2011]] [[ChunSheng Liu et al 2012][research_chunshengliu_xinzhongzhu_2012]] [[Colombo et al 2018][research_colombo_muscarello_2018]] [[Comer et al 2024][research_comer_bhandari_2024]] [[Cong et al 2023][research_cong_hu_2023]] [[Control Allocation and Flight 2016][research_control_allocation_2016]] [[Cotoi and Botez 2002][research_cotoi_botez_2002]] [[Cotton 1974][research_cotton_1974]] [[Cramer and Nguyen 2020][research_cramer_nguyen_2020]] [[Cristofaro 2024][research_cristofaro_2024]] [[Cruz and Kienitz 2007][research_cruz_kienitz_2007]] [[Dai et al 2012][research_dai_wu_2012]] [[Danowsky et al 2009][research_danowsky_thompson_2009]] [[Danowsky et al 2010][research_danowsky_brenner_2010]] [[Danowsky et al 2013][research_danowsky_thompson_2013]] [[Danowsky et al 2016][research_danowsky_lieu_2016]] [[de Vries and Van Kampen 2019][research_devries_vankampen_2019]] [[Demourant and Ferreres 2013][research_demourant_ferreres_2013]] [[Development and testing of control laws for the active aeroelastic wing program][research_aaw_control_laws]] [[Dibley et al 2005][research_dibley_allen_2005]] [[Dillinger et al 2020][research_dillinger_meddaikar_2020]] [[Dilmi 2022][research_dilmi_2022]] [[Doman and Oppenheimer 2002][research_doman_oppenheimer_2002]] [[Doman et al 2007][research_doman_gamble_2007]] [[Doman et al 2009][research_doman_gamble_2009]] [[Dong et al 2016][research_dong_lu_2016]] [[Dong et al 2024][research_dong_zhou_2024]] [[Durham et al 2016][research_durham_bordignon_2016]] [[Edwards et al 1997][research_edwards_fittante_1997]] [[Epple and Altenbach 1982][research_epple_altenbach_1982]] [[Favale et al 2021][research_favale_haidar_2021]] [[Faïsse et al 2022][research_faisse_vernay_2022]] [[Felt et al 1978][research_felt_huttsell_1978]] [[Ferreres and Puyou 2006][research_ferreres_puyou_2006]] [[Fonzi et al 2024][research_fonzi_ricci_2024]] [[Fonzi et al 2025][research_fonzi_ricci_2025]] [[Forte et al 2026][research_forte_nguyen_2026_b]] [[Frame-wise Control Allocation 2016][research_frame_wise_control_2016]] [[Franze et al 2013][research_franze_mattei_2013]] [[Friedmann 1992][research_friedmann_1992]] [[Friedmann 1998][research_friedmann_1998]] [[Frost et al 2012][research_frost_taylor_2012]] [[Gai and Wang 2013][research_gai_wang_2013]] [[Gai et al 2019][research_gai_sun_2019]] [[Gao et al 2021][research_gao_an_2021]] [[Gao et al 2021][research_gao_an_2021_b]] [[Ghorawat et al 2016][research_ghorawat_lee_2016]] [[Gilbert, Michael G. 1989][research_gilbertmichaelg_1989]] [[Graham et al 2007][research_graham_deoliveira_2007]] [[Gregory et al 2007][research_gregory_cao_2007]] [[Gregory et al 2011][research_gregory_xargay_2011]] [[Ground and flight testing 2000][research_ground_and_2000]] [[Guan et al 2025][research_guan_xing_2025]] [[Guillot and Friedmann 1994][research_guillot_friedmann_1994]] [[Gupta, K. K. et al 1987][research_guptakk_brennermj_1987]] [[Gupta, K. K. et al 1991][research_guptakk_brennermj_1991]] [[Haddadpour 2006][research_haddadpour_2006]] [[Haghighat et al 2010][research_haghighat_liu_2010]] [[Haghighat et al 2012][research_haghighat_martins_2012]] [[Han and Kim 2011][research_han_kim_2011]] [[Hansen et al 2020][research_hansen_duan_2020]] [[Hansen et al 2020][research_hansen_duan_2020_b]] [[Hansen et al 2022][research_hansen_duan_2022]] [[Hanson et al 2002][research_hanson_ryan_2002]] [[Harkegard][research_harkegard]] [[Hartwell and Nguyen 2021][research_hartwell_nguyen_2021]] [[Henderson and Lavretsky 1999][research_henderson_lavretsky_1999]] [[Hjartarson et al 2013][research_hjartarson_seiler_2013]] [[Hofmann and Kezer 1962][research_hofmann_kezer_1962]] [[Hoh and Mitchell 2018][research_hoh_mitchell_2018]] [[Hongchao Li et al][research_hongchaoli_zhongkeshi]] [[Hopwood et al 2019][research_hopwood_ruskin_2019]] [[Hu et al 2023][research_hu_shao_2023]] [[Huber 1995][research_huber_1995]] [[Hutto 1975][research_hutto_1975]] [[Idan et al 1999][research_idan_karpel_1999]] [[Ide and Ominsky 1990][research_ide_ominsky_1990]] [[Ingle and Kothmann 1998][research_ingle_kothmann_1998]] [[Isnardi et al 2018][research_isnardi_paoletti_2018]] [[Jackson and Livne 2005][research_jackson_livne_2005]] [[Jackson and Livne 2014][research_jackson_livne_2014]] [[Jenney et al 1982][research_jenney_schreadley_1982]] [[Jianjun Ma et al 2008][research_jianjunma_wenqiangli_2008]] [[Jianjun Ma et al 2008][research_jianjunma_pengli_2008]] [[Jing and Ma 2025][research_jing_ma_2025]] [[Jingping et al 2011][research_jingping_weiguo_2011]] [[Jurisson et al 2022][research_jurisson_debreuker_2022]] [[Karpel 1990][research_karpel_1990]] [[Karpel et al 1998][research_karpel_idan_1998]] [[Keas and MacMynowski 2009][research_keas_macmynowski_2009]] [[Kefayat and Kamali 2024][research_kefayat_kamali_2024]] [[Khrabrov and Sidoryuk 2010][research_khrabrov_sidoryuk_2010]] [[Khrabrov and Sidoryuk 2013][research_khrabrov_sidoryuk_2013]] [[Klepl 1990][research_klepl_1990]] [[Kubica and Livet 1994][research_kubica_livet_1994]] [[Kubica and Livet 1994][research_kubica_livet_1994_b]] [[Kubica et al 1995][research_kubica_livet_1995]] [[Kukreja, Sunil L. 2007][research_kukrejasunill_2007]] [[Layton 1995][research_layton_1995]] [[Layton 1996][research_layton_1996]] [[Li et al 2011][research_li_yu_2011]] [[Li et al 2012][research_li_yu_2012]] [[Li et al 2025][research_li_xiong_2025]] [[Lin et al 2019][research_lin_zhang_2019]] [[Lind and Brenner 1999][research_lind_brenner_1999_c]] [[Lind and Brenner 1999][research_lind_brenner_1999_d]] [[Lind and Brenner 1999][research_lind_brenner_1999_e]] [[Lind and Brenner 1999][research_lind_brenner_1999_f]] [[Lingyu et al 2006][research_lingyu_youwu_2006]] [[Little 1996][research_little_1996]] [[Liu and Zhang 2020][research_liu_zhang_2020]] [[Liu et al 2009][research_liu_sun_2009]] [[Liu et al 2018][research_liu_zhang_2018]] [[Liu et al 2025][research_liu_he_2025]] [[Liu et al 2026][research_liu_li_2026]] [[Livet et al 1994][research_livet_kubica_1994]] [[Livet et al 1995][research_livet_kubica_1995]] [[Livne 1993][research_livne_1993]] [[Livne and Li 1994][research_livne_li_1994]] [[Lou et al 2024][research_lou_duan_2024]] [[Love and Lind 2010][research_love_lind_2010]] [[Lu et al 2019][research_lu_ma_2019]] [[Lu et al 2026][research_lu_lan_2026]] [[Ma and Wang 2009][research_ma_wang_2009]] [[Maharaj 1997][research_maharaj_1997]] [[Mangalam et al 2007][research_mangalam_flick_2007]] [[Masarati et al 2010][research_masarati_quaranta_2010]] [[Masarati et al 2011][research_masarati_muscarello_2011]] [[Matamoros and de Visser 2018][research_matamoros_devisser_2018]] [[Mccuish and Caldwell 2018][research_mccuish_caldwell_2018]] [[Meirovitch and Tuzcu 2002][research_meirovitch_tuzcu_2002]] [[Miyazawa 2000][research_miyazawa_2000]] [[Model Reference Adaptation of 2016][research_model_reference_2016]] [[Mohamed and G 2020][research_mohamed_g_2020]] [[Mor and Livne 2004][research_mor_livne_2004]] [[Mor and Livne 2005][research_mor_livne_2005]] [[Moreno et al 2012][research_moreno_seiler_2012]] [[Moreno et al 2015][research_moreno_pfifer_2015]] [[Moulin et al 2001][research_moulin_idan_2001]] [[Moulin et al 2002][research_moulin_idan_2002]] [[Moulin et al 2010][research_moulin_ritz_2010]] [[Moulin et al 2011][research_moulin_zeng_2011]] [[Mouyon et al 2003][research_mouyon_cumer_2003]] [[Mu et al 2026][research_mu_huang_2026]] [[Mukhopadhyay 1988][research_mukhopadhyay_1988]] [[Murch 2008][research_murch_2008]] [[Muñoz Medina][research_munozmedina]] [[Napolitano et al 2001][research_napolitano_song_2001]] [[Newman and Schmidt 1994][research_newman_schmidt_1994]] [[Nguyen and Xiong 2026][research_nguyen_xiong_2026_b]] [[Nguyen et al 2018][research_nguyen_saussie_2018]] [[Nguyen et al 2018][research_nguyen_ting_2018]] [[Nguyen et al 2022][research_nguyen_webb_2022]] [[Nguyen et al 2023][research_nguyen_xiong_2023]] [[Nhan Nguyen et al][research_nhannguyen_benjaminwebb]] [[Noll et al 1989][research_noll_perryiii_1989]] [[Oliver and Singh 2020][research_oliver_singh_2020]] [[Ouellette 2026][research_ouellette_2026]] [[Ouellette et al 2010][research_ouellette_patil_2010]] [[Ouellette et al 2012][research_ouellette_patil_2012]] [[Ouellette et al 2014][research_ouellette_patil_2014]] [[Ouellette et al 2023][research_ouellette_miller_2023]] [[Pachikara and Lind 2012][research_pachikara_lind_2012]] [[Pankonien et al 2018][research_pankonien_durscher_2018]] [[Patil and Clark 2002][research_patil_clark_2002]] [[Pellegrino et al 2022][research_pellegrino_quaranta_2022]] [[Penning et al 2009][research_penning_zink_2009]] [[Pfeifle and Fichter 2021][research_pfeifle_fichter_2021]] [[Pfeifle and Fichter 2021][research_pfeifle_fichter_2021_b]] [[Pfeifle and Fichter 2023][research_pfeifle_fichter_2023]] [[Phillips][research_phillips]] [[Pototzky 2010][research_pototzky_2010]] [[Prasanth and Mehra 1999][research_prasanth_mehra_1999]] [[Prochazka et al 2018][research_prochazka_eduardo_2018]] [[Pursel 1977][research_pursel_1977]] [[Pusch et al 2022][research_pusch_kier_2022]] [[Puyou and Berard 2007][research_puyou_berard_2007]] [[Qin et al 2023][research_qin_wei_2023]] [[Qin et al 2023][research_qin_liu_2023]] [[Quach 2026][research_quach_2026]] [[Quach 2026][research_quach_2026_b]] [[Quackenbush et al 2009][research_quackenbush_keller_2009]] [[Quaranta et al 2013][research_quaranta_masarati_2013]] [[Rains et al 2024][research_rains_huang_2024]] [[Rao et al][research_rao_behal]] [[Raol and Singh 2023][research_raol_singh_2023]] [[Re 2014][research_re_2014]] [[Reichenbach 2008][research_reichenbach_2008]] [[Reichenbach et al 2009][research_reichenbach_urnes_2009]] [[Reichenbach et al 2011][research_reichenbach_castelluccio_2011]] [[Richardson and Kesler 1988][research_richardson_kesler_1988]] [[Ro et al 1992][research_ro_barlow_1992]] [[Robinson][research_robinson_b]] [[Rogers 2007][research_rogers_2007]] [[Sackett and Kirchwey 1982][research_sackett_kirchwey_1982]] [[Sadien et al 2019][research_sadien_carton_2019]] [[Sadien et al 2020][research_sadien_roos_2020]] [[Sahasrabudhe et al 1997][research_sahasrabudhe_celi_1997]] [[Scalera and Durham 1999][research_scalera_durham_1999]] [[Schmidt 1986][research_schmidt_1986_b]] [[Schmidt and Newman 1990][research_schmidt_newman_1990]] [[Schulze et al 2016][research_schulze_danowsky_2016]] [[Scordamaglia et al 2025][research_scordamaglia_mattei_2025]] [[Scott et al 2008][research_scott_vetter_2008]] [[Scott et al 2011][research_scott_coulson_2011]] [[Scott et al 2015][research_scott_allen_2015]] [[Shearwood et al 2020][research_shearwood_nabawy_2020]] [[Shearwood et al 2020][research_shearwood_nabawy_2020_b]] [[Sheldon and Rasmussen][research_sheldon_rasmussen]] [[Shimin et al 2025][research_shimin_letian_2025]] [[Shweyk and Weltz 2005][research_shweyk_weltz_2005]] [[Silvestre 2013][research_silvestre_2013]] [[Simbuerger et al 2022][research_simbuerger_raveh_2022]] [[Simoes et al 2009][research_simoes_alazard_2009]] [[Simões et al 2011][research_simoes_apkarian_2011]] [[Singh et al 2014][research_singh_mcdonough_2014]] [[Soares 2007][research_soares_2007]] [[Soares 2007][research_soares_2007_b]] [[Song et al 2014][research_song_liu_2014]] [[Song et al 2018][research_song_whidborne_2018]] [[Stalla et al 2024][research_stalla_kier_2024]] [[Stam and de Visser 2025][research_stam_devisser_2025]] [[Stanford 2015][research_stanford_2015]] [[Stanford 2016][research_stanford_2016_b]] [[Stanford 2019][research_stanford_2019]] [[Steer 2004][research_steer_2004]] [[Stephan 2025][research_stephan_2025]] [[Stettner and Schrage 1992][research_stettner_schrage_1992]] [[Suh, Peter M. et al 2015][research_suhpeterm_conyershowardjason_2015]] [[Sun et al 2020][research_sun_shi_2020]] [[Suryakumar et al 2016][research_suryakumar_mangalam_2016]] [[Szabolcsi and Gáspár 1997][research_szabolcsi_gaspar_1997]] [[Tabassum and Bai 2022][research_tabassum_bai_2022]] [[Tang et al 2015][research_tang_wu_2015]] [[Tang et al 2025][research_tang_yang_2025]] [[Tantaroudas and Da Ronch 2017][research_tantaroudas_daronch_2017]] [[Tariq and Nahon 2020][research_tariq_nahon_2020]] [[Taylor and Yoo 2011][research_taylor_yoo_2011]] [[Taylor et al 1995][research_taylor_pratt_1995]] [[Teng 2006][research_teng_2006]] [[Tewari 2015][research_tewari_2015_c]] [[Tewari 2016][research_tewari_2016]] [[The active flexible wing aeroservoelastic wind-tunnel test program][research_afw_wind_tunnel]] [[The Geometry of Control 2016][research_the_geometry_2016]] [[Theis et al 2015][research_theis_pfifer_2015]] [[Theis et al 2015][research_theis_takarics_2015]] [[Thompson et al 2007][research_thompson_klyde_2007]] [[Thompson et al 2011][research_thompson_danowsky_2011]] [[Ting et al 2017][research_ting_chaparro_2017]] [[Ting et al 2023][research_ting_mesbahi_2023]] [[Tingting and Aijun 2014][research_tingting_aijun_2014]] [[Tohidi et al 2018][research_tohidi_yildiz_2018]] [[Tol et al 2014][research_tol_devisser_2014]] [[Torralba et al 2009][research_torralba_puyou_2009]] [[Tırman et al 2024][research_tirman_ture_2024]] [[Vartio et al 2008][research_vartio_shaw_2008]] [[Veiberman and Karpel 2022][research_veiberman_karpel_2022]] [[Veiberman et al 2016][research_veiberman_weiss_2016]] [[Vile et al 2019][research_vile_alwi_2019]] [[Vile et al 2019][research_vile_alwi_2019_b]] [[Vile et al 2020][research_vile_alwi_2020]] [[Wahler et al 2023][research_wahler_varriale_2023]] [[Waite et al 2019][research_waite_stanford_2019]] [[Walker and Postlthewaite][research_walker_postlthewaite]] [[Wang and Guo 2012][research_wang_guo_2012]] [[Wang et al 2018][research_wang_zhang_2018]] [[Wang et al 2025][research_wang_yu_2025]] [[Wang et al 2025][research_wang_li_2025]] [[Weisshaar 1994][research_weisshaar_1994_b]] [[Weisshaar and Nam 1990][research_weisshaar_nam_1990]] [[Weisshaar, Terrence A. and Changho, Nam 1989][research_weisshaarterrencea_changhonam_1989]] [[Whitbeck and Hofmann 1978][research_whitbeck_hofmann_1978]] [[Williams 2004][research_williams_2004]] [[Williams-Hayes 2005][research_williamshayes_2005]] [[Wu and Livne 2015][research_wu_livne_2015]] [[Wu and Livne 2016][research_wu_livne_2016]] [[Wustenhagen et al 2021][research_wustenhagen_suelozgen_2021]] [[Xiaoguang et al 2023][research_xiaoguang_du_2023]] [[Xu et al 2016][research_xu_tang_2016]] [[Xu et al 2020][research_xu_zhang_2020]] [[Xu et al 2024][research_xu_sevart_2024]] [[Yamashiro and Stirling 2007][research_yamashiro_stirling_2007]] [[Yang and Gao 2020][research_yang_gao_2020]] [[Yang and Shen 2007][research_yang_shen_2007]] [[Yang et al 2009][research_yang_zhong_2009]] [[Yang et al 2011][research_yang_kim_2011]] [[Yiming et al 2019][research_yiming_mei_2019]] [[Yomchinda et al 2009][research_yomchinda_horn_2009]] [[Youssef 1985][research_youssef_1985]] [[Yurtsever et al 2026][research_yurtsever_sahin_2026]] [[Zaki et al 2017][research_zaki_unel_2017]] [[Zeng et al 2007][research_zeng_baldelli_2007]] [[Zeng et al 2008][research_zeng_baldelli_2008]] [[Zeng et al 2011][research_zeng_wang_2011]] [[Zhang and Zhao 2023][research_zhang_zhao_2023]] [[Zhang et al 2007][research_zhang_suresh_2007]] [[Zhang et al 2008][research_zhang_rabbath_2008]] [[Zhang et al 2025][research_zhang_xiang_2025]] [[Zhao et al 2026][research_zhao_zheng_2026]] [[Zhen and Cui 2023][research_zhen_cui_2023]] [[Zhong et al 2009][research_zhong_yang_2009]] [[Zou et al 2012][research_zou_yang_2012]]

### Static aeroelasticity, twist and divergence

**The physics the aeroplane was named for.** Elastic axis, torsional stiffness, wing twist and divergence. **A trailing-edge surface twists the wing against itself and a leading-edge surface twists it with itself**, and everything the X-53 did follows from that one asymmetry.

**257 records.** [[Abel 1972][research_abel_1972]] [[Adali 1981][research_adali_1981]] [[Agostinelli and Allen 2012][research_agostinelli_allen_2012]] [[Ahmad and Gazetas 1992][research_ahmad_gazetas_1992]] [[Akasaka et al 1989][research_akasaka_katoh_1989]] [[Amoozgar and Irani 2012][research_amoozgar_irani_2012]] [[Arai and Tanaka 2020][research_arai_tanaka_2020]] [[Arizono and Cesnik 2013][research_arizono_cesnik_2013]] [[Arnold 1942][research_arnold_1942]] [[Azizov et al 2019][research_azizov_derkowski_2019]] [[Balakrishnan 2006][research_balakrishnan_2006]] [[Balakrishnan 2007][research_balakrishnan_2007]] [[Balakrishnan and Iliff 2007][research_balakrishnan_iliff_2007]] [[Banerjee and Williams 1992][research_banerjee_williams_1992]] [[Baz and Chen 1993][research_baz_chen_1993]] [[Bdeiwi et al 2019][research_bdeiwi_ciarella_2019]] [[Belote and Menezes 2019][research_belote_menezes_2019]] [[Berci 2017][research_berci_2017]] [[Bernhard and Chopra 1996][research_bernhard_chopra_1996]] [[Bernhard and Chopra 1997][research_bernhard_chopra_1997]] [[Bhat 2018][research_bhat_2018]] [[Blair and Weisshaar 1982][research_blair_weisshaar_1982]] [[Boehm et al 2001][research_boehm_flick_2001]] [[Bohlmann et al 1990][research_bohlmann_eckstrom_1990]] [[Brincklow et al 2021][research_brincklow_montgomery_2021]] [[Brown, Stuart C. 1959][research_brownstuartc_1959]] [[Bugała 2025][research_bugala_2025]] [[Bugała et al 2023][research_bugala_sznajder_2023]] [[Bureerat 2026][research_bureerat_2026]] [[Burner and Martinson 1996][research_burner_martinson_1996]] [[Burner et al 2000][research_burner_liu_2000]] [[Burner, Alpheus W. et al 2005][research_burneralpheusw_lokoswilliama_2005]] [[Byun and Guruswamy 1996][research_byun_guruswamy_1996]] [[Castellani et al 2016][research_castellani_cooper_2016]] [[Castellani et al 2017][research_castellani_cooper_2017]] [[Cavin and Holyoak 1978][research_cavin_holyoak_1978]] [[Cestino and Iannuzzo 2026][research_cestino_iannuzzo_2026]] [[Chang 2005][research_chang_2005]] [[Chapman 1969][research_chapman_1969]] [[Charts for the determination of wing torsional stiffness required for specified rolling characteristics][research_charts_torsional_stiffness]] [[Cheng 1961][research_cheng_1961]] [[Cheng et al 2023][research_cheng_shi_2023]] [[Cheung et al 2023][research_cheung_palles_2023]] [[Chipman et al 1982][research_chipman_zislin_1982]] [[Chipman et al 1983][research_chipman_zislin_1983]] [[Costa and Vilela 2014][research_costa_vilela_2014]] [[Crawley et al 1995][research_crawley_curtiss_1995]] [[Cunningham 2017][research_cunningham_2017]] [[Daneshmehr et al 2013][research_daneshmehr_inman_2013]] [[Daynes et al 2015][research_daynes_lachenal_2015]] [[de Melo et al 2024][research_demelo_bussamra_2024]] [[Dixon 1963][research_dixon_1963]] [[Djojodihardjo 2023][research_djojodihardjo_2023_b]] [[Dooley 1965][research_dooley_1965]] [[Dowell 2021][research_dowell_2021]] [[Dowell et al 1989][research_dowell_curtiss_1989]] [[Du Peloux De Saint Romain][research_dupelouxdesaintromain]] [[Dubigeon 1992][research_dubigeon_1992]] [[Dumpleton 1987][research_dumpleton_1987]] [[Ecsedi 2000][research_ecsedi_2000]] [[Edwards 1992][research_edwards_1992]] [[Effective Torsional Stiffness of 1976][research_effective_torsional_1976]] [[Ehlers and Weisshaar 1992][research_ehlers_weisshaar_1992]] [[Ehlers and Weisshaar 1993][research_ehlers_weisshaar_1993]] [[Elastic Torsional Stiffness of 1965][research_elastic_torsional_1965]] [[Ellers and Boggs 2003][research_ellers_boggs_2003]] [[Engel and Miller][research_engel_miller]] [[Eslimy-Isfahany and Banerjee 1995][research_eslimyisfahany_banerjee_1995]] [[Eslimy-Isfahany et al 1996][research_eslimyisfahany_banerjee_1996]] [[Etnier 2001][research_etnier_2001]] [[Ezawa et al 2024][research_ezawa_nakatsugawa_2024]] [[Fang and Yang 2025][research_fang_yang_2025]] [[Fang et al 2025][research_fang_wang_2025]] [[Felker 1992][research_felker_1992]] [[Felker 1993][research_felker_1993]] [[Forster et al 2002][research_forster_sanders_2002]] [[Galloping and Torsional Divergence 2019][research_galloping_and_2019]] [[Garcia and Guruswamy 1999][research_garcia_guruswamy_1999]] [[Garud and Ajluni 2024][research_garud_ajluni_2024]] [[Gilbert and Silva 1987][research_gilbert_silva_1987]] [[Gimmestad 1981][research_gimmestad_1981_b]] [[Gowtham et al 2023][research_gowtham_baashkaran_2023]] [[Griffin and Eastep 1981][research_griffin_eastep_1981]] [[Gross 2002][research_gross_2002]] [[Guangming and Zhengfeng 2009][research_guangming_zhengfeng_2009]] [[Gunasekaran and Mukherjee 2016][research_gunasekaran_mukherjee_2016]] [[Guo et al 2018][research_guo_shen_2018]] [[Guo et al 2022][research_guo_yan_2022]] [[Haas and Chopra 1988][research_haas_chopra_1988]] [[Hahn and Haupt 2022][research_hahn_haupt_2022]] [[Hancock 1961][research_hancock_1961]] [[Hancock 1963][research_hancock_1963]] [[Hancock 1965][research_hancock_1965]] [[Harash et al 2012][research_harash_yadykin_2012]] [[Hatami-Marbini 2018][research_hatamimarbini_2018]] [[Herrmann][research_herrmann]] [[Herrmann and Nemat-Nasser 1966][research_herrmann_nematnasser_1966]] [[Hodges 2007][research_hodges_2007]] [[Hou and Satyanarayana 2000][research_hou_satyanarayana_2000]] [[Hoult and Beyer 2020][research_hoult_beyer_2020]] [[How to Model Post-Cracking 2020][research_how_to_2020]] [[Humbad 1978][research_humbad_1978]] [[Huo et al 2013][research_huo_yuan_2013]] [[Huo et al 2013][research_huo_wang_2013]] [[Hwu and Tsai 2002][research_hwu_tsai_2002]] [[Ibrahim and Castravete 2005][research_ibrahim_castravete_2005]] [[Investigations of Static Aeroelasticity 2016][research_investigations_of_static_2016]] [[J and J 2015][research_j_j_2015]] [[Jain 2014][research_jain_2014]] [[Johns 1964][research_johns_1964]] [[Jovanov and De Breuker 2015][research_jovanov_debreuker_2015]] [[K. Badri and Torabpour 2025][research_kbadri_torabpour_2025]] [[K. Badri and Torabpour 2026][research_kbadri_torabpour_2026]] [[Kadrnka and Hawley 1993][research_kadrnka_hawley_1993]] [[Kafkas and Lampeas 2020][research_kafkas_lampeas_2020]] [[Karathanasopoulos 2015][research_karathanasopoulos_2015]] [[Karpouzian 1991][research_karpouzian_1991]] [[Kawakami et al 2007][research_kawakami_takatoya_2007]] [[Kawakami et al 2008][research_kawakami_takatoya_2008]] [[Kaza and Kielb 1982][research_kaza_kielb_1982]] [[Khot et al 1997][research_khot_eastep_1997]] [[Kilimtzidis and Kostopoulos 2023][research_kilimtzidis_kostopoulos_2023]] [[Kim et al 2023][research_kim_sung_2023]] [[Kimler and Canfield 2006][research_kimler_canfield_2006]] [[Klaue and Seidel 2009][research_klaue_seidel_2009]] [[Lee et al 1994][research_lee_kim_1994]] [[Lei et al 2020][research_lei_wang_2020]] [[Li et al 2020][research_li_yang_2020]] [[Li et al 2021][research_li_wang_2021]] [[Li et al 2023][research_li_luo_2023]] [[Li et al 2024][research_li_zhang_2024]] [[Li et al 2024][research_li_zhiqiang_2024]] [[Li et al 2024][research_li_qian_2024]] [[Li et al 2024][research_li_kou_2024]] [[Li et al 2025][research_li_li_2025]] [[Li et al 2026][research_li_zhang_2026]] [[Liang et al 2025][research_liang_chen_2025]] [[Liang et al 2026][research_liang_chen_2026]] [[Librescu and Simovich 1988][research_librescu_simovich_1988]] [[Librescu and Song 1992][research_librescu_song_1992]] [[Librescu and Thangjitham 1989][research_librescu_thangjitham_1989]] [[Librescu and Thangjitham 1991][research_librescu_thangjitham_1991]] [[Liu et al 2011][research_liu_yin_2011]] [[Liu et al 2013][research_liu_bai_2013]] [[Lokos et al 2002][research_lokos_olney_2002]] [[Lottati 1985][research_lottati_1985]] [[Low et al 2016][research_low_pheh_2016]] [[Macek et al 2021][research_macek_branco_2021]] [[Macek et al 2021][research_macek_marciniak_2021]] [[Machado-e-Costa et al 2016][research_machadoecosta_valarinho_2016]] [[Mao et al 2023][research_mao_guo_2023]] [[Matter et al 2018][research_matter_darabseh_2018]] [[Meng et al 2020][research_meng_kaihua_2020]] [[Meresman and Ribak 2017][research_meresman_ribak_2017]] [[Merrett and Hilton 2011][research_merrett_hilton_2011]] [[Merrett et al 2011][research_merrett_hilton_2011_b]] [[Micks 1950][research_micks_1950]] [[Miniature slide units offer 2002][research_miniature_slide_2002]] [[Muscati and Grootenhuis 1975][research_muscati_grootenhuis_1975]] [[Nair and Goza 2022][research_nair_goza_2022]] [[Newsome et al 1998][research_newsome_berkooz_1998]] [[Niblett 1986][research_niblett_1986]] [[Noh et al 2025][research_noh_andreu_2025]] [[On selection of the 1972][research_on_selection_1972]] [[Pavanasam et al 2024][research_pavanasam_anil_2024]] [[Pecora et al 2012][research_pecora_amoroso_2012]] [[Phillips et al 2022][research_phillips_white_2022]] [[Price et al 2002][research_price_koffi_2002]] [[Qiao et al 2018][research_qiao_zhou_2018]] [[Qiao et al 2019][research_qiao_zhou_2019]] [[Qiao et al 2025][research_qiao_wang_2025]] [[Qin and Zhang 2013][research_qin_zhang_2013]] [[Ramlal et al 2025][research_ramlal_desai_2025]] [[Raoof and Kraincanic 1998][research_raoof_kraincanic_1998]] [[Reinbold et al 2026][research_reinbold_breitsamter_2026]] [[Revivo and Raveh 2025][research_revivo_raveh_2025]] [[Rimer et al 1984][research_rimer_chipman_1984_b]] [[Rodden 1981][research_rodden_1981]] [[Rodden 1984][research_rodden_1984]] [[Rodden 1989][research_rodden_1989]] [[Rodden and Bellinger 1982][research_rodden_bellinger_1982]] [[Rodden and Love 1984][research_rodden_love_1984]] [[Rodden and Love 1985][research_rodden_love_1985]] [[Rosenberg 1944][research_rosenberg_1944]] [[Sacchi et al 2025][research_sacchi_healy_2025]] [[Sampo' et al 2010][research_sampo_sorniotti_2010]] [[Schmidt 1991][research_schmidt_1991]] [[Scholes and Slater 1970][research_scholes_slater_1970]] [[Schuster et al 1990][research_schuster_vadyak_1990]] [[Selvadurai 1984][research_selvadurai_1984]] [[Shavezipur 2021][research_shavezipur_2021]] [[Shen et al 2019][research_shen_branscomb_2019]] [[Shen et al 2024][research_shen_li_2024]] [[Shipley and Gopalarathnam 2006][research_shipley_gopalarathnam_2006]] [[Shu-yi et al 2010][research_shuyi_xin_2010]] [[Shubin 1995][research_shubin_1995]] [[Song et al 1992][research_song_librescu_1992]] [[Static Aeroelastic Considerations 1996][research_static_aeroelastic_1996]] [[Static Aeroelasticity 2002][research_static_aeroelasticity_2002]] [[Static Aeroelasticity 2005][research_static_aeroelasticity_2005]] [[Static Aeroelasticity 2011][research_static_aeroelasticity_2011]] [[Static Aeroelasticity and Flutter 2014][research_static_aeroelasticity_2014_c]] [[Static Aeroelasticity Effect 2014][research_static_aeroelasticity_2014]] [[Static Aeroelasticity Effect 2014][research_static_aeroelasticity_2014_b]] [[Sun 2024][research_sun_2024]] [[Swaim 1961][research_swaim_1961]] [[Tacca et al 2024][research_tacca_colvin_2024]] [[The influence of the aerodynamic span effect on the magnitude of the torsional-divergence velocity][research_span_effect_divergence]] [[Thel et al 2022][research_thel_hahn_2022]] [[Thielicke and Stamhuis 2018][research_thielicke_stamhuis_2018]] [[Ting et al 2014][research_ting_lebofsky_2014]] [[Torsional Divergence 2014][research_torsional_divergence_2014]] [[Torsional stiffness and fatigue 1994][research_torsional_stiffness_1994]] [[Torsional stiffness of plastic 1972][research_torsional_stiffness_1972]] [[Truong et al 2022][research_truong_gosselin_2022]] [[Tsushima et al 2019][research_tsushima_yokozeki_2019]] [[Uhm 2021][research_uhm_2021]] [[Van Zyl 2001][research_vanzyl_2001]] [[Vance et al 1974][research_vance_brown_1974]] [[Varello et al 2013][research_varello_lamberti_2013]] [[Verri et al 2024][research_verri_luizbussamra_2024]] [[Verri et al 2025][research_verri_desilvabussamra_2025]] [[Wang 2019][research_wang_2019]] [[Wang et al 2021][research_wang_chang_2021]] [[Wang et al 2024][research_wang_wang_2024]] [[Wang et al 2026][research_wang_pei_2026]] [[Wang et al 2026][research_wang_pei_2026_b]] [[Webb and Takahashi 2022][research_webb_takahashi_2022]] [[Weisshaar 1973][research_weisshaar_1973]] [[Weisshaar 1974][research_weisshaar_1974]] [[Weisshaar 1974][research_weisshaar_1974_b]] [[Weisshaar 1979][research_weisshaar_1979]] [[Weisshaar 1990][research_weisshaar_1990_b]] [[Weisshaar and Ashley 1974][research_weisshaar_ashley_1974]] [[White and Hartl 2024][research_white_hartl_2024]] [[Wing torsional stiffness tests of the active aeroelastic wing F/A-18 airplane][research_aaw_torsional_stiffness]] [[Wunderlich 2015][research_wunderlich_2015]] [[Xie 2010][research_xie_2010]] [[xu et al 2023][research_xu_song_2023]] [[Yang et al 2009][research_yang_chen_2009]] [[Yang et al 2019][research_yang_xie_2019]] [[Yasue and Sawada 2009][research_yasue_sawada_2009]] [[Yin et al 2026][research_yin_xiao_2026]] [[Yu et al 2014][research_yu_lv_2014]] [[Zahn 1984][research_zahn_1984]] [[Zeiler 1998][research_zeiler_1998]] [[Zeiler 1999][research_zeiler_1999]] [[Zhang and Zhu 2021][research_zhang_zhu_2021]] [[Zhang et al 2018][research_zhang_zhou_2018]] [[Zhang et al 2018][research_zhang_zhou_2018_b]] [[Zhang et al 2021][research_zhang_guo_2021]] [[Zhao 2012][research_zhao_2012]] [[zhao 2019][research_zhao_2019]] [[Zhao 2020][research_zhao_2020]] [[Zheng et al 2013][research_zheng_hedrick_2013]] [[Zhi et al 2020][research_zhi_zhou_2020]] [[Zyablikov and Shirshov 2021][research_zyablikov_shirshov_2021]]

### Roll performance and how an aeroplane is judged to have enough

**The requirement side, which is where the programme's clearest failure lives.** Roll rate, roll mode time constant, time to bank, ailerons, flaps, stabilators and hinge moments. **Hinge moment dominated the flight test**, and the aeroplane met its level 1 goal at two test points and missed the level 2 requirement at a third.

**220 records.** [[ACM produces 737 aileron 2005][research_acm_produces_2005]] [[Adnyana 2017][research_adnyana_2017]] [[Aileron 2005][research_aileron_2005]] [[Air Force Test Pilot School Edwards Afb Ca 1989][research_airforcetestpilotschooledwardsafbca_1989]] [[Alam and Sohn 2023][research_alam_sohn_2023]] [[Albertani et al 2005][research_albertani_stanford_2005]] [[Alighanbari 2002][research_alighanbari_2002]] [[Altman 1952][research_altman_1952]] [[Anderson 1984][research_anderson_1984]] [[Anderson 1985][research_anderson_1985]] [[Ansell et al 2010][research_ansell_bragg_2010]] [[Ansell et al 2011][research_ansell_bragg_2011]] [[Ansell et al 2011][research_ansell_bragg_2011_b]] [[Ansell et al 2013][research_ansell_kerho_2013]] [[Ansell et al 2014][research_ansell_kerho_2014]] [[Ashkenas 1965][research_ashkenas_1965]] [[Atkinson 2016][research_atkinson_2016]] [[Avci et al 2026][research_avci_tegin_2026]] [[Ball 1978][research_ball_1978]] [[Ball 1979][research_ball_1979]] [[Bamber, Millard J 1934][research_bambermillardj_1934]] [[Bendiksen 1993][research_bendiksen_1993]] [[Bogatyrev 2017][research_bogatyrev_2017]] [[Boothe et al 1974][research_boothe_chen_1974]] [[Braun et al][research_braun_boucke]] [[Breul 1963][research_breul_1963]] [[Brewer, Gerald W. 1946][research_brewergeraldw_1946]] [[Brincklow and Hunsaker 2021][research_brincklow_hunsaker_2021]] [[Brown, Jr. 1970][research_brownjr_1970]] [[Bruno Santos et al 2020][research_brunosantos_oliveira_2020]] [[Burt Jr 1976][research_burtjr_1976]] [[Carlsson and Cronander 2005][research_carlsson_cronander_2005]] [[Carruthers et al 2007][research_carruthers_taylor_2007]] [[Cartwright 2010][research_cartwright_2010]] [[Celi 1991][research_celi_1991]] [[Cesnik and Brown 2002][research_cesnik_brown_2002]] [[Chand and Hansen][research_chand_hansen]] [[Chandrasekharan et al 2015][research_chandrasekharan_iarocci_2015]] [[Chen and Liu 2014][research_chen_liu_2014]] [[Chen et al 2026][research_chen_cai_2026]] [[Chen et al 2026][research_chen_gray_2026]] [[Cheng et al 1987][research_cheng_edwards_1987]] [[Covell et al 1986][research_covell_miller_1986]] [[Dai et al 2022][research_dai_qiu_2022]] [[Davis][research_davis]] [[Deere et al 2011][research_deere_pao_2011]] [[Dieterich et al 2006][research_dieterich_enenkl_2006]] [[Dixon 1972][research_dixon_1972]] [[Duffy 1989][research_duffy_1989]] [[Duncan 1950][research_duncan_1950]] [[Dynamic Lateral-Directional Stability Theory 2003][research_dynamic_lateral_directional_2003]] [[Ferrara 2025][research_ferrara_2025]] [[Ghalandari et al 2022][research_ghalandari_mahariq_2022]] [[Gomec et al 2020][research_gomec_unver_2020]] [[Gomec et al 2020][research_gomec_unver_2020_b]] [[Gordnier 1993][research_gordnier_1993]] [[Grant et al 1989][research_grant_nelson_1989]] [[Grantz 1985][research_grantz_1985]] [[Grantz and Marchman 1983][research_grantz_marchman_1983]] [[Greer et al 2021][research_greer_sardahi_2021]] [[Grismer et al 2000][research_grismer_kinsey_2000]] [[Gross et al 1986][research_gross_chandler_1986]] [[Grove 2006][research_grove_2006]] [[Guerreiro and Hubbard 2008][research_guerreiro_hubbard_2008]] [[Gurbacki and Bragg 1999][research_gurbacki_bragg_1999]] [[Gurbacki and Bragg 2001][research_gurbacki_bragg_2001]] [[Hall and Mason 2012][research_hall_mason_2012]] [[Harper and Robert P. 1955][research_harper_robertp_1955]] [[Haucke et al 2016][research_haucke_bauer_2016]] [[He et al 2020][research_he_song_2020]] [[He et al 2020][research_he_deparday_2020]] [[He et al 2021][research_he_wang_2021]] [[Hodapp, Jr. and Beckmann 1972][research_hodappjr_beckmann_1972]] [[Hopkins, E. J. and Lovette, G. H. 1977][research_hopkinsej_lovettegh_1977]] [[Hwang et al 1991][research_hwang_chen_1991]] [[Initial flight test of 1989][research_initial_flight_1989]] [[Innocenti 1985][research_innocenti_1985]] [[Irfan et al 2026][research_irfan_nanangburhan_2026]] [[Izadi et al 2007][research_izadi_pakmehr_2007]] [[Ize and Arena 1998][research_ize_arena_1998]] [[Ize and Arena, Jr. 1999][research_ize_arenajr_1999]] [[Ize et al 1997][research_ize_arenajr_1997]] [[Jabbar et al 2026][research_jabbar_setiawan_2026]] [[Jacobs, P. F. 1983][research_jacobspf_1983]] [[Jaworski 2012][research_jaworski_2012]] [[Jiang 1999][research_jiang_1999]] [[Jiang et al 2000][research_jiang_an_2000]] [[Karpouzian and Librescu 1992][research_karpouzian_librescu_1992]] [[Kassapakis and Warwick 1994][research_kassapakis_warwick_1994]] [[Keçecioğlu and Salih Yiğit 2026][research_kececioglu_salihyigit_2026]] [[Khot 1999][research_khot_1999]] [[Khot et al 1998][research_khot_appa_1998]] [[Khot et al 1998][research_khot_appa_1998_b]] [[Khot et al 2000][research_khot_zweber_2000]] [[Khot et al 2000][research_khot_appa_2000]] [[Klim et al 2013][research_klim_zeppetelli_2013]] [[Klyde et al 2007][research_klyde_bachelder_2007]] [[Kowalska and Goetzendorf-Grabowski 2022][research_kowalska_goetzendorfgrabowski_2022]] [[Kumar et al 2021][research_kumar_sunil_2021]] [[Kuo and Hsu 1997][research_kuo_hsu_1997]] [[Kwak et al 2004][research_kwak_shirotake_2004]] [[Kwong et al 2024][research_kwong_severson_2024]] [[Landers and Landrum 1998][research_landers_landrum_1998]] [[Landers et al 1997][research_landers_landrum_1997]] [[Lateral-Directional Stability Theory and 2003][research_lateral_directional_stability_2003]] [[Lauchle 1974][research_lauchle_1974]] [[Laurie and Farokhi 1993][research_laurie_farokhi_1993]] [[Lei and Kwak 2005][research_lei_kwak_2005]] [[Levy 1992][research_levy_1992]] [[Li et al 1999][research_li_zhu_1999]] [[Liu and Gong 2021][research_liu_gong_2021]] [[Liu et al 2025][research_liu_li_2025]] [[Luoma, Avro A 1944][research_luomaavroa_1944]] [[Marchman, Iii and Grantz 1982][research_marchmaniii_grantz_1982]] [[Masunaga and Bueno 2019][research_masunaga_bueno_2019]] [[Mayya et al 2023][research_mayya_srivastava_2023]] [[Melton et al 2005][research_melton_schaeffler_2005]] [[Meng et al 2024][research_meng_hu_2024]] [[Mertins et al 2005][research_mertins_elsholz_2005]] [[Miller et al 2014][research_miller_holguin_2014]] [[Mitchell and Hoh 1984][research_mitchell_hoh_1984]] [[Mohamed et al 2021][research_mohamed_abdelhady_2021]] [[Montgomery 1971][research_montgomery_1971]] [[Mulder et al 2009][research_mulder_lubbers_2009]] [[Nadimi 1999][research_nadimi_1999]] [[Nurohman et al 2018][research_nurohman_arifianto_2018]] [[O'Donnell and Mohseni 2019][research_odonnell_mohseni_2019]] [[Pan and Huang 2019][research_pan_huang_2019]] [[Park and Abla 1982][research_park_abla_1982]] [[Park and Abla 1983][research_park_abla_1983]] [[Park and Chung 2012][research_park_chung_2012]] [[Park et al 2001][research_park_lee_2001]] [[Parker et al 1991][research_parker_spain_1991]] [[Patidar et al 2025][research_patidar_sarwar_2025]] [[Pavlenko and Reslan 2022][research_pavlenko_reslan_2022]] [[Pedreiro et al 1998][research_pedreiro_takahara_1998]] [[Pedreiro et al 1999][research_pedreiro_takahara_1999]] [[Perez-Becker et al 2021][research_perezbecker_marten_2021]] [[Pettit and Grandhi 2003][research_pettit_grandhi_2003]] [[Pitt Ford et al 2012][research_pittford_stevens_2012]] [[Poojari 2022][research_poojari_2022]] [[Potvin and Grant 2026][research_potvin_grant_2026]] [[Psolla-Bress et al][research_psollabress_haselmeyer]] [[Purser, P. E. and Tucker, W. A. 1949][research_purserpe_tuckerwa_1949]] [[Purwadi et al 2023][research_purwadi_hidayat_2023]] [[Qiu and Ang 2019][research_qiu_ang_2019]] [[Ratliff and Pagilla 2008][research_ratliff_pagilla_2008]] [[Rennie and Jumper 1995][research_rennie_jumper_1995]] [[Rennie and Jumper 1997][research_rennie_jumper_1997]] [[Ricci and Scotti 2009][research_ricci_scotti_2009]] [[Roysdon and Khalid 2010][research_roysdon_khalid_2010]] [[Roysdon and Khalid 2011][research_roysdon_khalid_2011]] [[Sahoo and Cesnik 2002][research_sahoo_cesnik_2002]] [[Sainio and Krandel 1993][research_sainio_krandel_1993]] [[Sanghi et al 2020][research_sanghi_riso_2020]] [[Sanghi et al 2024][research_sanghi_cesnik_2024]] [[Sardahi and Kolonay 2021][research_sardahi_kolonay_2021]] [[Sarvankar et al 2023][research_sarvankar_sarkar_2023]] [[Sarvankar et al 2024][research_sarvankar_sarkar_2024]] [[Sattar et al 2020][research_sattar_wang_2020]] [[Sebastia and Hornung 2023][research_sebastia_hornung_2023]] [[Sebastia et al 2024][research_sebastia_wurz_2024]] [[Segawa and Gopalarathnam 2008][research_segawa_gopalarathnam_2008]] [[Shao et al 2024][research_shao_guo_2024]] [[Shearwood et al 2023][research_shearwood_nabawy_2023]] [[Shmilovich et al 2023][research_shmilovich_yadlin_2023]] [[Shmilovich et al 2026][research_shmilovich_yadlin_2026]] [[Sieradzki 2016][research_sieradzki_2016]] [[Sigrest et al 2022][research_sigrest_wu_2022]] [[Simsek and Tekinalp 2015][research_simsek_tekinalp_2015]] [[Singh et al 2024][research_singh_kumari_2024]] [[Sinha and Ananthkrishnan 2002][research_sinha_ananthkrishnan_2002]] [[Sohn et al 2006][research_sohn_chung_2006]] [[Sohn et al 2007][research_sohn_chung_2007]] [[Soinne 1999][research_soinne_1999]] [[Solarte-Pineda et al 2026][research_solartepineda_bravomosquera_2026]] [[Song et al 2014][research_song_yang_2014]] [[Song et al 2025][research_song_zhang_2025]] [[Soovere 1981][research_soovere_1981]] [[Sreenivasulu et al 2025][research_sreenivasulu_neelapu_2025]] [[Steer 2003][research_steer_2003]] [[Steger and Bailey 1979][research_steger_bailey_1979]] [[Steger and Bailey 1980][research_steger_bailey_1980]] [[Strand and Ennis 2012][research_strand_ennis_2012]] [[Strelkov and Kharlamov 1967][research_strelkov_kharlamov_1967]] [[Suleman et al 2000][research_suleman_crawford_2000]] [[Suleman et al 2002][research_suleman_crawford_2002]] [[Sun and Hu 2005][research_sun_hu_2005]] [[Sun et al 2021][research_sun_zhou_2021]] [[Tai et al 2023][research_tai_wang_2023_b]] [[Tamayama et al 2003][research_tamayama_kheirandish_2003]] [[Taraborrelli 2023][research_taraborrelli_2023]] [[The Effects of Leading 2007][research_the_effects_2007]] [[Tischler and Hoh 1982][research_tischler_hoh_1982]] [[Triplett and Ising 1971][research_triplett_ising_1971]] [[Veley et al 2008][research_veley_khot_2008]] [[Walker and Aglietti 2007][research_walker_aglietti_2007]] [[Wang et al 2021][research_wang_wu_2021]] [[Wang et al 2022][research_wang_zhao_2022]] [[Wei et al 2022][research_wei_lin_2022]] [[Weiss 1983][research_weiss_1983]] [[Weisshaar 1977][research_weisshaar_1977]] [[Weisshaar 1990][research_weisshaar_1990]] [[Weisshaar 1994][research_weisshaar_1994]] [[Wilson et al 1993][research_wilson_riley_1993]] [[Wolfson 2009][research_wolfson_2009]] [[Xie et al 2019][research_xie_zhao_2019]] [[Xu and Qiu 2011][research_xu_qiu_2011]] [[Xu et al 2020][research_xu_han_2020]] [[Yanagihara et al 1991][research_yanagihara_suzuki_1991]] [[Yang et al 2023][research_yang_liu_2023]] [[Yerly et al 2016][research_yerly_deluca_2016]] [[Yuan et al 2023][research_yuan_ma_2023]] [[Zanette and Almeida 2015][research_zanette_almeida_2015]] [[Zhang and Zhang 2013][research_zhang_zhang_2013]] [[Zhang et al 2013][research_zhang_yu_2013]] [[Zhang et al 2017][research_zhang_wang_2017]] [[Zhang et al 2022][research_zhang_liu_2022]] [[Zhang et al 2024][research_zhang_zhao_2024]] [[Zhao et al 2020][research_zhao_he_2020]]

### Load alleviation, which is the other thing a flexible wing can be asked to do

**The same hardware pointed at a different objective.** Manoeuvre and gust load alleviation, and active load control. **The two design teams on this programme optimised opposite problems**, one maximising roll rate under load constraints and the other minimising loads under a roll constraint, and this cluster is the second of those.

**198 records.** [[Ahmadi Tehrani et al 2025][research_ahmaditehrani_ellis_2025]] [[Alam and Hromcik 2019][research_alam_hromcik_2019]] [[Alam et al 2015][research_alam_hromcik_2015]] [[Ali 2024][research_ali_2024]] [[Allyn and Takahashi 2016][research_allyn_takahashi_2016]] [[An et al 2018][research_an_xie_2018]] [[Anderson et al 1972][research_anderson_berger_1972]] [[Aouf et al 2000][research_aouf_boulet_2000]] [[Asaro et al 2023][research_asaro_cavaliere_2023]] [[Aslam-Mir and McLean][research_aslammir_mclean]] [[Bai et al 2014][research_bai_zhang_2014]] [[Balatti et al 2023][research_balatti_ellis_2023]] [[Balatti et al 2023][research_balatti_khodaparast_2023]] [[Barzgaran et al 2021][research_barzgaran_quenzer_2021]] [[Bendixen et al 1981][research_bendixen_oconnell_1981]] [[Beyer et al 2024][research_beyer_ullah_2024]] [[Beyer et al 2024][research_beyer_steen_2024]] [[Bi et al 2017][research_bi_xie_2017_b]] [[Breitenstein et al 2023][research_breitenstein_muller_2023]] [[Breitenstein et al 2024][research_breitenstein_muller_2024]] [[Bruni et al 2014][research_bruni_cestino_2014]] [[Bruni et al 2015][research_bruni_frulla_2015]] [[Burgstaller and Galffy 2024][research_burgstaller_galffy_2024]] [[Burris and Bender 1969][research_burris_bender_1969]] [[Burris and Bender 1969][research_burris_bender_1969_b]] [[Carrillo et al 2022][research_carrillo_mertens_2022]] [[Cavaliere and Fezans 2024][research_cavaliere_fezans_2024]] [[Caverly et al 2017][research_caverly_forbes_2017]] [[Cheung et al 2019][research_cheung_rezgui_2019]] [[Cheung et al 2019][research_cheung_rezgui_2019_b]] [[Cheung et al 2020][research_cheung_rezgui_2020]] [[Ciniglio et al 2003][research_ciniglio_manimala_2003]] [[Curpanaru et al 2025][research_curpanaru_pastor_2025]] [[Darden 1984][research_darden_1984]] [[Darden 1985][research_darden_1985]] [[Dillsaver et al 2011][research_dillsaver_cesnik_2011]] [[Disney 1975][research_disney_1975]] [[Disney 1977][research_disney_1977]] [[Drew et al 2020][research_drew_hashemi_2020]] [[Duan et al 2021][research_duan_kolmanovsky_2021]] [[Duessler et al 2023][research_duessler_mylvaganam_2023]] [[Duessler et al 2024][research_duessler_mylvaganam_2024]] [[Fan et al 2017][research_fan_liu_2017]] [[Farsadi et al 2026][research_farsadi_ahmadi_2026]] [[Ferrier et al 2018][research_ferrier_nguyen_2018]] [[Fezans 2017][research_fezans_2017]] [[Fezans and Joos 2017][research_fezans_joos_2017]] [[Fezans et al 2019][research_fezans_joos_2019]] [[Filippou et al 2026][research_filippou_sodja_2026]] [[Fonte and Mantegazza 2017][research_fonte_mantegazza_2017]] [[Fonte et al 2015][research_fonte_ricci_2015]] [[Fonte et al 2018][research_fonte_toffol_2018]] [[Forte and Nguyen 2026][research_forte_nguyen_2026]] [[Forte and Nguyen 2026][research_forte_nguyen_2026_c]] [[Forte et al 2022][research_forte_nguyen_2022]] [[Forte et al 2023][research_forte_nguyen_2023]] [[Forte et al 2026][research_forte_nguyen_2026_e]] [[Fournier et al 2022][research_fournier_massioni_2022]] [[Fujimori et al 1989][research_fujimori_ohta_1989]] [[Fujimori et al 1990][research_fujimori_ohta_1990]] [[Gao et al 2024][research_gao_liu_2024]] [[Gennaretti and Ponzi 1999][research_gennaretti_ponzi_1999]] [[Gern et al 2000][research_gern_ko_2000]] [[Ghorawat et al 2015][research_ghorawat_lee_2015]] [[Giesseler et al 2012][research_giesseler_kopf_2012]] [[Haghighat et al 2012][research_haghighat_liu_2012]] [[Hammerton et al 2018][research_hammerton_su_2018]] [[Handojo et al 2018][research_handojo_lancelot_2018]] [[Hashemi and Nguyen 2018][research_hashemi_nguyen_2018_b]] [[Hashemi et al 2018][research_hashemi_nguyen_2018]] [[He et al 2022][research_he_wang_2022]] [[Hillebrand and Lutz 2026][research_hillebrand_lutz_2026]] [[Hillebrand et al 2024][research_hillebrand_breitenstein_2024]] [[Hillebrand et al 2026][research_hillebrand_breitenstein_2026]] [[Hoffmann et al 2011][research_hoffmann_loftfield_2011]] [[Huebner and Reimer 2019][research_huebner_reimer_2019]] [[Islam et al 2018][research_islam_martin_2018]] [[Johnston, J. F. 1979][research_johnstonjf_1979]] [[Khalil and Bauknecht 2024][research_khalil_bauknecht_2024]] [[Khalil and Fezans 2019][research_khalil_fezans_2019]] [[Khalil and Fezans 2019][research_khalil_fezans_2019_b]] [[Khalil and Fezans 2020][research_khalil_fezans_2020]] [[Khalil et al 2020][research_khalil_asaro_2020]] [[Khalil et al 2022][research_khalil_asaro_2022]] [[Kopf et al 2015][research_kopf_giesseler_2015]] [[Kopf et al 2018][research_kopf_bullinger_2018]] [[Kordt et al 2002][research_kordt_ballauf_2002]] [[Krengel 2024][research_krengel_2024]] [[Krengel and Hepperle 2022][research_krengel_hepperle_2022]] [[Krengel and Hepperle 2023][research_krengel_hepperle_2023]] [[Leble and Barakos 2016][research_leble_barakos_2016]] [[Lee and Singh 2014][research_lee_singh_2014]] [[Lee et al 2018][research_lee_hashemi_2018]] [[Li and Qin 2020][research_li_qin_2020]] [[Li and Qin 2021][research_li_qin_2021]] [[Li and Qin 2021][research_li_qin_2021_b]] [[Li and Qin 2022][research_li_qin_2022]] [[Li et al 2017][research_li_zhao_2017]] [[Li et al 2018][research_li_huang_2018]] [[Li et al 2025][research_li_gong_2025]] [[Liao et al 2026][research_liao_zhang_2026]] [[Lin 2016][research_lin_2016]] [[Liu and Sun 2016][research_liu_sun_2016]] [[Liu and Sun 2017][research_liu_sun_2017]] [[Liu et al 2017][research_liu_sun_2017_b]] [[Liu et al 2018][research_liu_dong_2018]] [[Lucas et al 2009][research_lucas_valasek_2009]] [[Mancini and Vos 2019][research_mancini_vos_2019]] [[Manimala et al 2004][research_manimala_padfield_2004]] [[Matsuzaki et al 1987][research_matsuzaki_ueda_1987]] [[Matsuzaki et al 1989][research_matsuzaki_ueda_1989]] [[Mballo and Prasad 2022][research_mballo_prasad_2022]] [[Michel et al 2025][research_michel_stalla_2025]] [[Molz and Breitsamter 2026][research_molz_breitsamter_2026]] [[Moore 1992][research_moore_1992]] [[Moore 1995][research_moore_1995]] [[Muradas Odriozola][research_muradasodriozola]] [[Müller et al 2026][research_muller_woidt_2026]] [[Narayanaswamy et al 2008][research_narayanaswamy_narayanan_2008]] [[Narimani et al 2025][research_narimani_haddadpour_2025]] [[Nguyen 2021][research_nguyen_2021]] [[Nguyen et al 2017][research_nguyen_ting_2017]] [[Nguyen et al 2018][research_nguyen_hashemi_2018]] [[Nie et al 2009][research_nie_zhang_2009]] [[Nixon and Tzuoo 1987][research_nixon_tzuoo_1987]] [[Odriozola et al 2026][research_odriozola_marquier_2026]] [[Ohta and Fujimori 1988][research_ohta_fujimori_1988]] [[Ossmann and Poussot-Vassal 2018][research_ossmann_poussotvassal_2018]] [[Paletta et al 2010][research_paletta_belardo_2010]] [[Pasley et al 1973][research_pasley_rohling_1973]] [[Pourtakdoust and Khodabakhsh 2026][research_pourtakdoust_khodabakhsh_2026]] [[Poussot-Vassal et al 2022][research_poussotvassal_vuillemin_2022]] [[Pusch 2017][research_pusch_2017]] [[Pusch et al 2019][research_pusch_knoblach_2019]] [[Qi et al 2015][research_qi_ting_2015]] [[Qu and Li 2022][research_qu_li_2022]] [[Rieck et al 2026][research_rieck_herrmann_2026]] [[Roll plus maneuver load alleviation control system designs for the active flexible wing][research_afw_roll_mla]] [[Rolling maneuver load alleviation using active controls][research_rolling_mla_active]] [[Sanghi et al 2022][research_sanghi_riso_2022]] [[Scaramal and Horn 2022][research_scaramal_horn_2022]] [[Scaramal and Horn 2023][research_scaramal_horn_2023]] [[Scaramal et al 2021][research_scaramal_saetti_2021]] [[Schlemmer et al 2020][research_schlemmer_dehmlow_2020]] [[Schumann et al 2025][research_schumann_wustenhagen_2025]] [[Seki et al 2019][research_seki_tani_2019]] [[Siebert et al 2026][research_siebert_strothteicher_2026]] [[Skinner and Zare-Behtash 2018][research_skinner_zarebehtash_2018]] [[Sodja et al 2018][research_sodja_werter_2018]] [[Sodja et al 2021][research_sodja_werter_2021]] [[Stanford 2020][research_stanford_2020]] [[Streitenberger and Feldwisch 2025][research_streitenberger_feldwisch_2025]] [[Strothteicher and Fezans 2026][research_strothteicher_fezans_2026]] [[Suresh et al 2010][research_suresh_radhakrishnan_2010]] [[Suzuki and Yonezawa 1993][research_suzuki_yonezawa_1993]] [[Tang et al 2016][research_tang_wu_2016]] [[Tani et al 2018][research_tani_seki_2018]] [[Tantaroudas and Karachalios 2026][research_tantaroudas_karachalios_2026]] [[Thapa Magar et al 2018][research_thapamagar_pankonien_2018]] [[Thomas and Shkarayev 2026][research_thomas_shkarayev_2026]] [[Ting et al 2022][research_ting_mesbahi_2022]] [[Toffol 2024][research_toffol_2024]] [[Ullah et al 2021][research_ullah_lutz_2021]] [[Ullah et al 2022][research_ullah_kamoun_2022]] [[Ullah et al 2023][research_ullah_lutz_2023]] [[Vartio et al 2005][research_vartio_shimko_2005]] [[Virgilio Pereira et al 2019][research_virgiliopereira_kolmanovsky_2019]] [[Virgilio Pereira et al 2019][research_virgiliopereira_kolmanovsky_2019_b]] [[Voskuijl et al 2008][research_voskuijl_walker_2008]] [[Wada et al 2020][research_wada_tamayama_2020]] [[Wang et al 2018][research_wang_vankampen_2018]] [[Wang et al 2019][research_wang_vankampen_2019]] [[Wang et al 2019][research_wang_tang_2019]] [[Wang et al 2021][research_wang_mkhoyan_2021_b]] [[Wheatcroft et al 2025][research_wheatcroft_groh_2025]] [[White 1970][research_white_1970]] [[White 1971][research_white_1971]] [[Wildschek et al 2006][research_wildschek_maier_2006]] [[Wildschek et al 2013][research_wildschek_hanis_2013]] [[Woods-Vedeler and Pototzky 1992][research_woodsvedeler_pototzky_1992]] [[Woods-Vedeler et al 1995][research_woodsvedeler_pototzky_1995]] [[Woods-Vedeler, Jessica A. et al 1994][research_woodsvedelerjessicaa_pototzkyanthonys_1994]] [[Wuestenhagen 2023][research_wuestenhagen_2023]] [[Wynn et al 2022][research_wynn_artola_2022]] [[Xu and Kroo 2011][research_xu_kroo_2011]] [[Xu and Kroo 2011][research_xu_kroo_2011_b]] [[Xu and Kroo 2014][research_xu_kroo_2014]] [[Xu et al 2011][research_xu_zhu_2011]] [[Xue Lei et al 2016][research_xuelei_zhangzheyu_2016]] [[Yang et al 2010][research_yang_xiao_2010]] [[Yang et al 2025][research_yang_liu_2025]] [[Yin et al 2015][research_yin_wu_2015]] [[Zeng et al 2010][research_zeng_moulin_2010]] [[Zhang et al 2024][research_zhang_qiu_2024]] [[Zhao et al 2016][research_zhao_yue_2016]] [[Zhao et al 2023][research_zhao_yang_2023]] [[Zink et al 2002][research_zink_raveh_2002]] [[Zink et al 2004][research_zink_raveh_2004]]

### Wind tunnels, and the models that stood in for the aeroplane

**Where this technology lived for nine years before it flew.** Aeroelastic wind-tunnel models, the transonic dynamics tunnel and ground vibration testing. **The Active Flexible Wing programme ran from 1984 to 1993 entirely in a tunnel**, and the flight programme existed to find out what a full-scale aeroplane would do instead.

**110 records.** [[Aeroelastic modeling of the active flexible wing wind-tunnel model][research_afw_modeling]] [[Aeroelastic Modelling 2016][research_aeroelastic_modelling_2016]] [[Anderson 1993][research_anderson_1993]] [[Bagherzadeh 2020][research_bagherzadeh_2020]] [[Bass et al 1993][research_bass_thompson_1993]] [[Bass et al 1995][research_bass_thompson_1995]] [[Begnini et al 2018][research_begnini_bones_2018]] [[Bennett, R. M. et al 1977][research_bennettrm_farmermg_1977]] [[Bergmann and Sevart 1973][research_bergmann_sevart_1973]] [[Bergmann and Sevart 1975][research_bergmann_sevart_1975]] [[Black et al 2007][research_black_schwaab_2007]] [[Bosch et al 2014][research_bosch_schmehl_2014]] [[Briardy and Head 1968][research_briardy_head_1968]] [[Buttrill and Houck 1990][research_buttrill_houck_1990]] [[Carlsson 2003][research_carlsson_2003]] [[Carlsson 2004][research_carlsson_2004]] [[Carlsson 2005][research_carlsson_2005]] [[Cavanaugh et al 2007][research_cavanaugh_robertson_2007]] [[Cella and Biancolini 2012][research_cella_biancolini_2012]] [[Cesnik et al 2023][research_cesnik_ritter_2023]] [[Chawla et al 1988][research_chawla_edwards_1988]] [[Chung et al 2019][research_chung_cho_2019]] [[Coder 2023][research_coder_2023]] [[Coder 2025][research_coder_2025]] [[Coe, Jr. and Perkins 1990][research_coejr_perkins_1990]] [[Coetzee et al 2023][research_coetzee_lowenberg_2023]] [[Cole et al 2003][research_cole_noll_2003]] [[Correction of model deformation 2017][research_correction_of_2017]] [[Darida and Smrcek 1998][research_darida_smrcek_1998]] [[De Gaspari et al 2007][research_degaspari_ricci_2007]] [[Deitering and Hilliard 1965][research_deitering_hilliard_1965]] [[Dias and Girardi 2016][research_dias_girardi_2016]] [[Diedrich 1971][research_diedrich_1971]] [[Dobbs et al 1985][research_dobbs_miller_1985]] [[Experimental results from the active aeroelastic wing wind tunnel test program][research_aaw_wind_tunnel]] [[Fay and Johnstone 1960][research_fay_johnstone_1960]] [[Fejtek 1994][research_fejtek_1994]] [[Forte and Nguyen 2024][research_forte_nguyen_2024]] [[Friedmann 1989][research_friedmann_1989]] [[Gaspari et al 2009][research_gaspari_ricci_2009]] [[Ghee and Taylor 2000][research_ghee_taylor_2000]] [[Ghee and Taylor 2004][research_ghee_taylor_2004]] [[Grauer et al 2012][research_grauer_heeg_2012]] [[Gutierrez et al 1994][research_gutierrez_tate_1994]] [[Haney et al 1978][research_haney_waggoner_1978]] [[Haney et al 1979][research_haney_johnson_1979]] [[Harry and Trobaugh 1966][research_harry_trobaugh_1966]] [[Heeg 2006][research_heeg_2006]] [[Heeg et al 2005][research_heeg_spain_2005]] [[Hildebrand et al 2003][research_hildebrand_eidson_2003]] [[Hoadley and McGraw 1995][research_hoadley_mcgraw_1995]] [[Kai et al 2020][research_kai_sugiura_2020]] [[Karpel 1990][research_karpel_1990_b]] [[Khaddage][research_khaddage]] [[Kolesar 1971][research_kolesar_1971]] [[Kolesar et al 1970][research_kolesar_kassianides_1970]] [[Kolesar et al 1970][research_kolesar_kassianides_1970_b]] [[Koreanschi et al 2015][research_koreanschi_oliviu_2015]] [[Koven, William and Kayten, Gerald G. 1946][research_kovenwilliam_kaytengeraldg_1946]] [[Lee et al 1993][research_lee_valerio_1993]] [[Levinsky and Palko 1978][research_levinsky_palko_1978]] [[Li and Xia 2018][research_li_xia_2018]] [[Lindsley 2007][research_lindsley_2007]] [[Lucas 1978][research_lucas_1978]] [[Matula et al 2026][research_matula_yalla_2026]] [[Mayo et al 2016][research_mayo_carroll_2016]] [[Mcclain and Pountney 1982][research_mcclain_pountney_1982]] [[Meng and Yu 2023][research_meng_yu_2023]] [[Meng et al 2021][research_meng_wan_2021]] [[Morgenstern 2004][research_morgenstern_2004]] [[Nguyen and Urnes 2012][research_nguyen_urnes_2012]] [[Nicolosi et al 2020][research_nicolosi_cusati_2020]] [[Orr 2010][research_orr_2010]] [[Pankonien et al 2019][research_pankonien_durscher_2019]] [[Paul][research_paul]] [[Persoon et al 1980][research_persoon_roos_1980]] [[Piatak, David J. and Cleckner, Craig S. 2002][research_piatakdavidj_clecknercraigs_2002]] [[Raveh et al 2023][research_raveh_sodja_2023]] [[Ricci and Scotti 2008][research_ricci_scotti_2008]] [[Ricci et al 2008][research_ricci_scotti_2008_b]] [[Rill and Ganzer 1988][research_rill_ganzer_1988]] [[Rocha Da Costa][research_rochadacosta]] [[Schmidt and Chavez 2001][research_schmidt_chavez_2001]] [[Sclafani et al 2012][research_sclafani_slotnick_2012]] [[Serpieri and Kotsonis 2015][research_serpieri_kotsonis_2015]] [[Simmons and Murphy 2021][research_simmons_murphy_2021]] [[Sims and Carter 1981][research_sims_carter_1981]] [[Sinclair and Flowers 2010][research_sinclair_flowers_2010]] [[Srivathsan and Rauleder 2023][research_srivathsan_rauleder_2023]] [[Stalla et al 2026][research_stalla_looye_2026]] [[Strand and Levinsky 1969][research_strand_levinsky_1969]] [[Tewari 2015][research_tewari_2015_b]] [[Tijdeman et al 1979][research_tijdeman_vannunen_1979]] [[Tijdeman et al 1979][research_tijdeman_vannunen_1979_b]] [[Tillotson and Fuhs 1982][research_tillotson_fuhs_1982]] [[Tsushima et al 2025][research_tsushima_soneda_2025]] [[Tuzcu and Nguyen 2010][research_tuzcu_nguyen_2010]] [[Ulker et al 2012][research_ulker_nitzsche_2012]] [[Wallace 1952][research_wallace_1952]] [[Wang et al 2025][research_wang_chen_2025]] [[White 1963][research_white_1963]] [[Wieseman et al 1995][research_wieseman_hoadley_1995]] [[Xiong and Nguyen 2024][research_xiong_nguyen_2024_c]] [[Xu et al 2023][research_xu_chen_2023]] [[Yamamoto 1992][research_yamamoto_1992]] [[Zeising and Gerhardt 1993][research_zeising_gerhardt_1993]] [[Zhang et al 2019][research_zhang_kang_2019]] [[Zhang et al 2025][research_zhang_li_2025]] [[Çiçek and Kayran 2019][research_cicek_kayran_2019]] [[Čečrdle et al 2022][research_cecrdle_malinek_2022]]

### The atmosphere and the flight condition

**The medium, named rather than assumed.** Standard atmosphere, density altitude and dynamic pressure. **Every claim in this article is a claim about dynamic pressure**, because that is the variable the reversal condition is defined on, and it is set by altitude and speed together.

**47 records.** [[A Properties of Standard 2006][research_a_properties_2006]] [[Appendix A Standard Atmosphere 2021][research_appendix_a_2021]] [[Appendix A. The Standard 2011][research_appendix_a_2011]] [[Appendix B Properties of 2003][research_appendix_b_2003]] [[Atmosphere standard atmosphere 2006][research_atmosphere_standard_2006]] [[B-34. U. S. Standard 1963][research_b_34_u_1963]] [[Definition of the standard 1954][research_definition_of_1954]] [[Dennis P. Dykstra 1980][research_dennispdykstra_1980]] [[Essenhigh 2006][research_essenhigh_2006]] [[Everett et al 1972][research_everett_cashwell_1972]] [[Gooch 2011][research_gooch_2011]] [[Gooch 2011][research_gooch_2011_b]] [[Herbert][research_herbert]] [[International Standard Atmosphere 2010][research_international_standard_2010]] [[Kang et al 2023][research_kang_zhao_2023]] [[Kang et al 2023][research_kang_meng_2023]] [[Kaushik 2018][research_kaushik_2018]] [[Kurzke and Halliwell 2018][research_kurzke_halliwell_2018]] [[Kurzke et al 2025][research_kurzke_halliwell_2025]] [[Lee and Aldredge 2015][research_lee_aldredge_2015]] [[Minimum Performance Standard for][research_minimum_performance]] [[Minimum Performance Standard for][research_minimum_performance_b]] [[Paper, board and pulps][research_paper_board]] [[Pressures and Temperatures for 2000][research_pressures_and_2000]] [[Properties of the U.S 2014][research_properties_of_2014]] [[Properties of the U.S 2024][research_properties_of_2024]] [[Report No. 538, altitude-pressure 1935][research_report_no_1935]] [[Ross et al 1993][research_ross_law_1993]] [[Space environment natural and][research_space_environment]] [[Standard Atmosphere][research_standard_atmosphere]] [[Standard Atmosphere 2005][research_standard_atmosphere_2005]] [[Standard atmosphere 2007][research_standard_atmosphere_2007]] [[Standard Atmosphere 2023][research_standard_atmosphere_2023]] [[Standard Atmosphere 2024][research_standard_atmosphere_2024]] [[Standard atmosphere chart 1927][research_standard_atmosphere_1927]] [[Standard atmosphere chart supersedes 1927][research_standard_atmosphere_1927_b]] [[Standard Atmosphere Data 1992][research_standard_atmosphere_1992]] [[standard atmosphere for preconditioning 2021][research_standard_atmosphere_2021]] [[standard atmosphere for testing 2021][research_standard_atmosphere_2021_b]] [[Standard Atmospheric Profilesa aSource 2002][research_standard_atmospheric_2002]] [[The Flight Environment Standard 2021][research_the_flight_2021]] [[The International Standard Atmosphere 2017][research_the_international_2017]] [[The international standard atmosphere 2026][research_the_international_2026]] [[The Standard Atmosphere 1964][research_the_standard_1964]] [[The Standard Atmosphere 1976][research_the_standard_1976]] [[US Standard Atmosphere Model 2014][research_us_standard_2014]] [[Vaughan 2003][research_vaughan_2003]]

### Control reversal, and the dynamic pressure at which a surface stops working

**The smallest cluster in the survey, and its size is the finding.** Aileron reversal, rolling effectiveness and the loss of control power with dynamic pressure. **The problem was solved in the 1940s by adding torsional stiffness and the answer held**, so the literature closed. This article is about an attempt to reopen it, and the attempt did not reach the condition.

**22 records.** [[Beldica and Hilton 1999][research_beldica_hilton_1999]] [[Bihrle and Barnhart 1982][research_bihrle_barnhart_1982]] [[Bihrle et al 1980][research_bihrle_jr_1980]] [[Calculation of the lateral control of swept and unswept flexible wings of arbitrary stiffness][research_lateral_control_flexible]] [[Clark 2026][research_clark_2026]] [[DeLaurier 2024][research_delaurier_2024]] [[Goland 1952][research_goland_1952]] [[Grosser 1965][research_grosser_1965]] [[Horton 1943][research_horton_1943]] [[Hunn 1953][research_hunn_1953]] [[hussain and Khan 2019][research_hussain_khan_2019]] [[Kim and Song 2013][research_kim_song_2013]] [[Mukherjee and Shaw 2004][research_mukherjee_shaw_2004]] [[Mukherjee and Shaw 2007][research_mukherjee_shaw_2007]] [[Pearson, Henry A and Aiken, William S, Jr 1944][research_pearsonhenrya_aikenwilliamsjr_1944]] [[Rolling effectiveness and aileron reversal of rectangular wings at supersonic speeds][research_supersonic_aileron_reversal]] [[Rose and Jinu 2014][research_rose_jinu_2014]] [[Sandahl, Carl A 1948][research_sandahlcarla_1948]] [[Silva][research_silva_b]] [[Song and Kim 2009][research_song_kim_2009]] [[Thomson 1946][research_thomson_1946]] [[Yoon et al 2012][research_yoon_chung_2012]]


## The Source Base

**The seventeen curated sources and seven books that carry the argument, and the 3,307 that map the field, are different things.**

**The evidentiary base is unusually strong for this series because the programme documented itself.** Beyond the curated references sit thirty-nine named technical reports, being the programme's own and those of the wind-tunnel programme that preceded it and the wartime work that settled the classical answer, **every one verified against the report server before assembly**. **The flight test report was read in full**, and most of what this article says about what happened comes from it rather than from any description of it.

**The survey base was harvested and none of it was read.** 8,612 records were retrieved across two sweeps, 3,410 passed the subject gate, and 3,307 reach the reference list after duplicate registrations were removed.

### The Pool

**The main harvest retrieved 5,108 records from the scholarly registry, 896 from the defence report registry and 123 from the space agency's, for 6,127.** A second sweep aimed at the keystone added 2,485 the first did not hold, for 8,612 in total.

**3,410 passed the subject gate and 3,307 survived deduplication into the reference list, across 12 clusters.**

### The Primary Fraction and What the Corpus-Wide Measure Cannot See

**Primaries are 261 of 3,307, or 7.9 percent**, against 2.0 percent one article ago. **The measure works again because the subject is an aeroplane again**, and the report registries hold this literature in a way they did not hold the last one.

**The count splits into two kinds and the article reports both.** 254 carry an identifier from the space agency's report server or the defence technical information centre, which is what the corpus-wide measure can see. **Seven are journal and conference papers named by hand**, being the programme's own publications and those of the wind-tunnel programme before it, and the measure cannot see them because an aeronautical society's identifier looks like any other.

**Thirty-nine sources are named foundational references rather than harvested ones.** They are the programme's technical reports, the wind-tunnel programme's, the wartime work that settled the classical answer, and the papers on the instrumentation and the flight control computer. **Every one was verified against its repository before assembly**, which is the discipline that caught a fabricated identifier in A347 and another in A349.

### The Keystone Literature Is the Smallest Cluster and That Is the Finding

**Twenty-two records of 3,307, or 0.67 percent, are about control reversal itself.** That is the smallest cluster in the survey and it is about the thing the aeroplane is named for.

**The first sweep found fewer still, and the gap was in the asking rather than in the field.** A probe of the pool found the keystone standing at 32 records, so a second sweep was run in every vocabulary the field has used for it across eighty years, being aeroelastic control effectiveness, aeroelastic efficiency, rolling power and elastic correction to the stability derivatives. 2,930 records were retrieved, 2,485 were not already held, 565 passed the gate, and the keystone probe moved to 43.

**It is still the smallest cluster and that is the finding rather than a defect in the sweep.** Reversal was solved in the 1940s by adding torsional stiffness, the design charts were published before the war ended, and the answer held. **A literature closes when a problem stops being open**, and this article is about an attempt to reopen one that did not reach the condition.

### The Sweep Store Needed No Tag, Which Is the Opposite of the Previous Article

**The shared sweep store holds 129 patterns observed to contaminate earlier sweeps, and this article switched none of them off.** Applied with nothing disabled it removed 419 records of 6,127, and reading a sample of them found the drops correct.

**That is worth stating because the previous article had to switch seven patterns off across three tagged families.** A349's subject was confusable names and the store is aeronautical, so the store was wrong for it in a way that had to be measured and corrected. **This article's subject is a wing**, and the store was built by articles about wings.

**Two families were checked closely because they are adjacent rather than contaminating.** The wind turbine blade is an aeroelastic structure and the family is armed, and reading the drops found wind speed forecasting and wind farm output smoothing rather than blade aeroelasticity. Fatigue cracking is armed and the drops included two records on flight control and crack growth in a flexible aircraft, which is a small and named loss. **Rotorcraft aeroelasticity is not filtered at all** and about 99 records in the pool carry it, many of them tiltrotor wing work that belongs here on the merits.

### Two Primary Sources Disagree About How Many Flights and How Many Gauges

**The programme's flight test report and the flight research centre's own fact sheet do not match.** The report gives Phase I as November 2002 to June 2003 and 51 flights, and the fact sheet gives it as late 2002 to April 2003 and 50 research flights. The report gives Phase II as 35 total flights and the fact sheet gives about 25 research missions.

**Both can be true and the article does not assume they are.** A research mission and a flight are not the same unit, and the difference plausibly lies in ferry, check and abort sorties. **This article uses the report's numbers**, because the report is the engineering account and states its counts as totals.

**They disagree on instrumentation as well.** The report gives approximately 200 strain-gauge bridges across the aeroplane and the fact sheet gives more than 350 strain gauges on each wing. **A bridge is made of several gauges**, so these are probably the same installation counted in two units, and the article says so rather than choosing.

## Epistemic State

### Historical Fact

The Active Aeroelastic Wing flight programme began in 1996 and concluded flight research in March 2005 [[Flight test of the F/A-18 active aeroelastic wing airplane][research_aaw_flight_test]].

The testbed was assembled from a Navy F/A-18A airframe, tail number 853, and wings from an early prototype, tail number 840 [[Flight test of the F/A-18 active aeroelastic wing airplane][research_aaw_flight_test]].

Boeing's Phantom Works returned the wing to essentially preproduction torsional stiffness and split the leading-edge flap drive into independently controlled inboard and outboard sections [[Flight test of the F/A-18 active aeroelastic wing airplane][research_aaw_flight_test]] [[Wing torsional stiffness tests of the active aeroelastic wing F/A-18 airplane][research_aaw_torsional_stiffness]].

Phase I comprised 51 flights from November 2002 to June 2003 and Phase II comprised 35 flights from December 2004 to March 2005, at 18 test points of which two were never flown.

The programme deleted the external stores requirement and effectively deleted the requirement to fly beyond trailing-edge control reversal after early flight tests showed it could not be met.

No full aileron reversal was observed. The aileron rolling moment approached zero and did not change sign.

At the subsonic region I and supersonic region II test points the control designs met the level 1 time-to-bank goal. At the subsonic region III test point roll performance was inadequate to meet the level 2 requirement.

The aircraft was designated X-53 on 16 August 2006 [[Boeing X-53 Active Aeroelastic Wing][ref_x53_wikipedia]].

### Verified by Independent Derivation

**The dynamic pressures quoted for the test points were computed here from the 1976 standard atmosphere and $q = \tfrac{1}{2}\rho V^2$, not read from any source.** Mach 1.2 at 15,000 feet gives about 1,204 pounds per square foot, Mach 1.3 at 15,000 feet about 1,413, and Mach 1.2 at 10,000 feet about 1,467.

**That the two unflown test points are the only two above 1,400 pounds per square foot is a consequence of that computation** and is not stated in the source.

### Analysis

The reversal and divergence relations in the sizing section are the standard typical-section results and are derived here rather than quoted.

That a leading-edge surface twists the wing in the opposite sense to a trailing-edge surface follows from the position of its hinge relative to the elastic axis, and the flight test report states the consequence in words.

### Inference

**That the research instrumentation is why the aeroplane could not reach the highest test points is the report's own suggestion and it is offered as a possibility rather than a finding.** The report says the external targets, wiring, pressure instrumentation and camera pods **may have** contributed.

**That control surface flexibility explains the absence of reversal is likewise the report's hypothesis**, supported by control position transducer readings and not established.

**That region III performance mattered more than region I and II performance is this article's judgement**, on the ground that region III is where the technology is supposed to pay.

### What the Record Does Not Settle

**Whether a wing designed for this from the start would save 10 to 20 percent is not settled by this programme**, which did not have one.

**Whether the aeroplane would have reversed at a higher dynamic pressure is unknown**, because it could not get there.

**Why the load reduction failed at the subsonic region II point is described and not explained.** The report identifies the trailing-edge surfaces being driven inconsistently with load control strategies and does not say why the design produced that.

**How much of the roll performance shortfall in region III is the technology and how much is an eighteen-point design process is not separable from the public record.**

## Out of Scope

**The X-52 designation refusal**, which is the previous article's subject and is treated there [[X-Planes: X-52, the Designation Refused][related_post_a349_x52_designation_refused]].

**Flutter and its active suppression**, which the wind-tunnel predecessor demonstrated and the flight programme deliberately removed from scope.

**The detailed control law synthesis**, which has its own reports and which this article treats at the level of what each team was optimising [[Development and testing of control laws for the active aeroelastic wing program][research_aaw_control_laws]].

**Morphing and shape-changing structures generally**, which share this article's motivation and not its mechanism.

**The surveyed literature itself.** None of the harvested records was read and none is cited for any claim.

## Conclusion

**The X-53 removed the stiffening from a fighter's wing on purpose and then rolled it with the wing.**

**It did that within 15 to 20 percent of a production aeroplane's roll rate, without using the tail that the production aeroplane uses for the job**, which is the demonstration the programme existed to make and which it made.

**It also failed to meet the lower of its two roll requirements in region III**, the regime where the trailing edge has stopped working and the leading edge carries the roll, and that is the regime the entire concept is aimed at.

**And it never saw reversal.** The requirement to fly beyond it was abandoned when early tests showed it could not be met, the aileron rolling moment approached zero and stopped rather than changing sign, and **the two test points at the highest dynamic pressures were never flown because the aeroplane could not get to them**, the report naming the external targets, wiring, pressure instrumentation and camera pods as likely sources of the extra drag.

**So this is a demonstration that stopped one region short of its own name.** The Active Aeroelastic Wing showed that a flexible wing can be flown as a control effector and did not show what happens past the point where the classical answer runs out. **The classical answer is stiffness, the classical answer is heavy, and the aeroplane built to find an alternative could not reach the condition that makes the alternative necessary.**

## References

### Books

- [Bisplinghoff, Aeroelasticity][book_bisplinghoff]
- [Etkin and Reid, Dynamics of flight][book_etkin_reid]
- [Fung, An introduction to the theory of aeroelasticity][book_fung]
- [Hodges and Pierce, Introduction to structural dynamics and aeroelasticity][book_hodges_pierce]
- [Megson, Aircraft structures for engineering students][book_megson]
- [Raymer, Aircraft design, a conceptual approach][book_raymer]
- [Wright and Cooper, Introduction to aircraft aeroelasticity and loads][book_wright_cooper]

[book_bisplinghoff]: https://openlibrary.org/works/OL3240762W
[book_etkin_reid]: https://openlibrary.org/works/OL19844466W
[book_fung]: https://openlibrary.org/works/OL2655267W
[book_hodges_pierce]: https://openlibrary.org/works/OL15891219W
[book_megson]: https://openlibrary.org/works/OL4809615W
[book_raymer]: https://openlibrary.org/works/OL17855977W
[book_wright_cooper]: https://openlibrary.org/works/OL12439109W

### Reference

- [Active Aeroelastic Wing Flight Research, NASA Facts FS-2005-03-061 DFRC][ref_aaw_factsheet]
- [Aeroelasticity][ref_aeroelasticity]
- [Aileron Reversal][ref_aileron_reversal]
- [Air Force Research Laboratory][ref_afrl]
- [Allocation of Official Aerospace Vehicle MDS Designations][ref_mds_allocation]
- [Boeing X-53 Active Aeroelastic Wing][ref_x53_wikipedia]
- [Dynamic Pressure][ref_dynamic_pressure]
- [F/A-18 Active Aeroelastic Wing, NASA][ref_nasa_x53]
- [High Alpha Research Vehicle][ref_harv]
- [McDonnell Douglas F/A-18 Hornet][ref_fa18]
- [Missing USAF and DOD Aircraft Designations][ref_missing_mds]
- [NASA Armstrong Flight Research Center][ref_armstrong]
- [Northrop YF-17][ref_yf17]
- [Phantom Works][ref_phantom_works]
- [U.S. Standard Atmosphere][ref_us_standard_atmosphere_ref]
- [Wing Warping][ref_wing_warping]
- [Wright Flyer][ref_wright_flyer]

[ref_aaw_factsheet]: https://www.nasa.gov/wp-content/uploads/2021/09/120314main_fs-061-dfrc.pdf
[ref_aeroelasticity]: https://en.wikipedia.org/wiki/Aeroelasticity
[ref_afrl]: https://en.wikipedia.org/wiki/Air_Force_Research_Laboratory
[ref_aileron_reversal]: https://en.wikipedia.org/wiki/Aileron#Aileron_reversal
[ref_armstrong]: https://en.wikipedia.org/wiki/Armstrong_Flight_Research_Center
[ref_dynamic_pressure]: https://en.wikipedia.org/wiki/Dynamic_pressure
[ref_fa18]: https://en.wikipedia.org/wiki/McDonnell_Douglas_F/A-18_Hornet
[ref_harv]: https://en.wikipedia.org/wiki/High_Alpha_Research_Vehicle
[ref_mds_allocation]: https://www.designation-systems.net/usmilav/mdsallocation.html
[ref_missing_mds]: https://www.designation-systems.net/usmilav/missing-mds.html
[ref_nasa_x53]: https://www.nasa.gov/aeronautics/x-53/
[ref_phantom_works]: https://en.wikipedia.org/wiki/Phantom_Works
[ref_us_standard_atmosphere_ref]: https://en.wikipedia.org/wiki/U.S._Standard_Atmosphere
[ref_wing_warping]: https://en.wikipedia.org/wiki/Wing_warping
[ref_wright_flyer]: https://en.wikipedia.org/wiki/Wright_Flyer
[ref_x53_wikipedia]: https://en.wikipedia.org/wiki/Boeing_X-53_Active_Aeroelastic_Wing
[ref_yf17]: https://en.wikipedia.org/wiki/Northrop_YF-17

### Related Post

- [X-Planes: Aerojet X-8 Aerobee][related_post_a305_aerojet_x8]
- [X-Planes: Bell X-1][related_post_a298_bell_x1]
- [X-Planes: Bell X-14][related_post_a311_bell_x14]
- [X-Planes: Bell X-16][related_post_a313_bell_x16]
- [X-Planes: Bell X-2][related_post_a299_bell_x2]
- [X-Planes: Bell X-22][related_post_a319_bell_x22]
- [X-Planes: Bell X-5][related_post_a302_bell_x5]
- [X-Planes: Bell X-9 Shrike][related_post_a306_bell_x9]
- [X-Planes: Bensen X-25][related_post_a322_bensen_x25]
- [X-Planes: Boeing X-20 Dyna-Soar][related_post_a317_boeing_x20]
- [X-Planes: Boeing X-32][related_post_a329_boeing_x32]
- [X-Planes: Boeing X-37][related_post_a334_boeing_x37]
- [X-Planes: Boeing X-40][related_post_a337_boeing_x40]
- [X-Planes: Boeing X-45][related_post_a342_boeing_x45]
- [X-Planes: Boeing X-46][related_post_a343_boeing_x46]
- [X-Planes: Boeing X-48][related_post_a345_boeing_x48]
- [X-Planes: Boeing X-50 Dragonfly][related_post_a347_boeing_x50]
- [X-Planes: Boeing X-51 Waverider][related_post_a348_boeing_x51]
- [X-Planes: Convair X-11][related_post_a308_convair_x11]
- [X-Planes: Convair X-12][related_post_a309_convair_x12]
- [X-Planes: Convair X-6][related_post_a303_convair_x6]
- [X-Planes: Curtiss-Wright X-19][related_post_a316_curtiss_wright_x19]
- [X-Planes: Douglas X-3 Stiletto][related_post_a300_douglas_x3]
- [X-Planes: Framing and the Research Aircraft Model][related_post_a297_framing]
- [X-Planes: Grumman X-29][related_post_a326_grumman_x29]
- [X-Planes: Hiller X-18][related_post_a315_hiller_x18]
- [X-Planes: Lockheed Martin X-33][related_post_a330_lockheed_martin_x33]
- [X-Planes: Lockheed Martin X-35][related_post_a332_lockheed_martin_x35]
- [X-Planes: Lockheed X-17][related_post_a314_lockheed_x17]
- [X-Planes: Lockheed X-27][related_post_a324_lockheed_x27]
- [X-Planes: Lockheed X-7][related_post_a304_lockheed_x7]
- [X-Planes: Martin Marietta X-23 PRIME and a Contested Assignment][related_post_a320_martin_marietta_x23]
- [X-Planes: Martin Marietta X-24][related_post_a321_martin_marietta_x24]
- [X-Planes: McDonnell Douglas X-36][related_post_a333_mcdonnell_douglas_x36]
- [X-Planes: Micro-Craft X-43 Hyper-X][related_post_a340_micro_craft_x43]
- [X-Planes: North American X-10][related_post_a307_north_american_x10]
- [X-Planes: North American X-15][related_post_a312_north_american_x15]
- [X-Planes: Northrop Grumman X-47][related_post_a344_northrop_grumman_x47]
- [X-Planes: Northrop X-21][related_post_a318_northrop_x21]
- [X-Planes: Northrop X-4 Bantam][related_post_a301_northrop_x4]
- [X-Planes: Orbital Sciences X-34][related_post_a331_orbital_sciences_x34]
- [X-Planes: Orbital Sciences X-42][related_post_a339_orbital_sciences_x42]
- [X-Planes: Osprey X-28 Sea Skimmer][related_post_a325_osprey_x28]
- [X-Planes: Piasecki X-49 SpeedHawk][related_post_a346_piasecki_x49]
- [X-Planes: Rockwell X-30 and the National Aero-Space Plane][related_post_a327_rockwell_x30]
- [X-Planes: Rockwell-MBB X-31][related_post_a328_rockwell_mbb_x31]
- [X-Planes: Ryan X-13 Vertijet][related_post_a310_ryan_x13]
- [X-Planes: Scaled Composites X-38][related_post_a335_scaled_composites_x38]
- [X-Planes: Schweizer X-26 Frigate][related_post_a323_schweizer_x26]
- [X-Planes: X-39, Reserved but Never Assigned][related_post_a336_x39_reserved_never_assigned]
- [X-Planes: X-41 Common Aero Vehicle][related_post_a338_x41_common_aero_vehicle]
- [X-Planes: X-44, One Designation and Two Aircraft][related_post_a341_x44_two_aircraft]
- [X-Planes: X-52, the Designation Refused][related_post_a349_x52_designation_refused]

[related_post_a297_framing]: {% post_url 2025-10-06-x_planes_framing %}
[related_post_a298_bell_x1]: {% post_url 2025-10-07-x_planes_bell_x1 %}
[related_post_a299_bell_x2]: {% post_url 2025-10-08-x_planes_bell_x2 %}
[related_post_a300_douglas_x3]: {% post_url 2025-10-09-x_planes_douglas_x3 %}
[related_post_a301_northrop_x4]: {% post_url 2025-10-10-x_planes_northrop_x4 %}
[related_post_a302_bell_x5]: {% post_url 2025-10-11-x_planes_bell_x5 %}
[related_post_a303_convair_x6]: {% post_url 2025-10-12-x_planes_convair_x6 %}
[related_post_a304_lockheed_x7]: {% post_url 2025-10-13-x_planes_lockheed_x7 %}
[related_post_a305_aerojet_x8]: {% post_url 2025-10-14-x_planes_aerojet_x8 %}
[related_post_a306_bell_x9]: {% post_url 2025-10-15-x_planes_bell_x9 %}
[related_post_a307_north_american_x10]: {% post_url 2025-10-16-x_planes_north_american_x10 %}
[related_post_a308_convair_x11]: {% post_url 2025-10-17-x_planes_convair_x11 %}
[related_post_a309_convair_x12]: {% post_url 2025-10-18-x_planes_convair_x12 %}
[related_post_a310_ryan_x13]: {% post_url 2025-10-19-x_planes_ryan_x13 %}
[related_post_a311_bell_x14]: {% post_url 2025-10-20-x_planes_bell_x14 %}
[related_post_a312_north_american_x15]: {% post_url 2025-10-21-x_planes_north_american_x15 %}
[related_post_a313_bell_x16]: {% post_url 2025-10-22-x_planes_bell_x16 %}
[related_post_a314_lockheed_x17]: {% post_url 2025-10-23-x_planes_lockheed_x17 %}
[related_post_a315_hiller_x18]: {% post_url 2025-10-24-x_planes_hiller_x18 %}
[related_post_a316_curtiss_wright_x19]: {% post_url 2025-10-25-x_planes_curtiss_wright_x19 %}
[related_post_a317_boeing_x20]: {% post_url 2025-10-26-x_planes_boeing_x20 %}
[related_post_a318_northrop_x21]: {% post_url 2025-10-27-x_planes_northrop_x21 %}
[related_post_a319_bell_x22]: {% post_url 2025-10-28-x_planes_bell_x22 %}
[related_post_a320_martin_marietta_x23]: {% post_url 2025-10-29-x_planes_martin_marietta_x23 %}
[related_post_a321_martin_marietta_x24]: {% post_url 2025-10-30-x_planes_martin_marietta_x24 %}
[related_post_a322_bensen_x25]: {% post_url 2025-10-31-x_planes_bensen_x25 %}
[related_post_a323_schweizer_x26]: {% post_url 2025-11-01-x_planes_schweizer_x26 %}
[related_post_a324_lockheed_x27]: {% post_url 2025-11-02-x_planes_lockheed_x27 %}
[related_post_a325_osprey_x28]: {% post_url 2025-11-03-x_planes_osprey_x28 %}
[related_post_a326_grumman_x29]: {% post_url 2025-11-04-x_planes_grumman_x29 %}
[related_post_a327_rockwell_x30]: {% post_url 2025-11-05-x_planes_rockwell_x30 %}
[related_post_a328_rockwell_mbb_x31]: {% post_url 2025-11-06-x_planes_rockwell_mbb_x31 %}
[related_post_a329_boeing_x32]: {% post_url 2025-11-07-x_planes_boeing_x32 %}
[related_post_a330_lockheed_martin_x33]: {% post_url 2025-11-08-x_planes_lockheed_martin_x33 %}
[related_post_a331_orbital_sciences_x34]: {% post_url 2025-11-09-x_planes_orbital_sciences_x34 %}
[related_post_a332_lockheed_martin_x35]: {% post_url 2025-11-10-x_planes_lockheed_martin_x35 %}
[related_post_a333_mcdonnell_douglas_x36]: {% post_url 2025-11-11-x_planes_mcdonnell_douglas_x36 %}
[related_post_a334_boeing_x37]: {% post_url 2025-11-12-x_planes_boeing_x37 %}
[related_post_a335_scaled_composites_x38]: {% post_url 2025-11-13-x_planes_scaled_composites_x38 %}
[related_post_a336_x39_reserved_never_assigned]: {% post_url 2025-11-14-x_planes_x39_reserved_never_assigned %}
[related_post_a337_boeing_x40]: {% post_url 2025-11-15-x_planes_boeing_x40 %}
[related_post_a338_x41_common_aero_vehicle]: {% post_url 2025-11-16-x_planes_x41_common_aero_vehicle %}
[related_post_a339_orbital_sciences_x42]: {% post_url 2025-11-17-x_planes_orbital_sciences_x42 %}
[related_post_a340_micro_craft_x43]: {% post_url 2025-11-18-x_planes_micro_craft_x43_hyper_x %}
[related_post_a341_x44_two_aircraft]: {% post_url 2025-11-19-x_planes_x44_one_designation_two_aircraft %}
[related_post_a342_boeing_x45]: {% post_url 2025-11-20-x_planes_boeing_x45 %}
[related_post_a343_boeing_x46]: {% post_url 2025-11-21-x_planes_boeing_x46 %}
[related_post_a344_northrop_grumman_x47]: {% post_url 2025-11-22-x_planes_northrop_grumman_x47 %}
[related_post_a345_boeing_x48]: {% post_url 2025-11-23-x_planes_boeing_x48 %}
[related_post_a346_piasecki_x49]: {% post_url 2025-11-24-x_planes_piasecki_x49 %}
[related_post_a347_boeing_x50]: {% post_url 2025-11-25-x_planes_boeing_x50 %}
[related_post_a348_boeing_x51]: {% post_url 2025-11-26-x_planes_boeing_x51 %}
[related_post_a349_x52_designation_refused]: {% post_url 2025-11-27-x_planes_x52_designation_refused %}

### Research

- [2-D Prototypical Aeroelastic Wing 2013][research_2_d_prototypical_2013]
- [2-D Prototypical Aeroelastic Wing 2018][research_2_d_prototypical_2018]
- [3-D Prototypical Aeroelastic Wing 2013][research_3_d_prototypical_2013]
- [3-D Prototypical Aeroelastic Wing 2018][research_3_d_prototypical_2018]
- [A comparative study of 2026][research_a_comparative_2026]
- [A flight research program for active aeroelastic wing technology][research_aaw_flight_research_plan]
- [A flutter suppression system using strain gages applied to active flexible wing technology][research_afw_flutter_strain_gauge]
- [A parametric sensitivity and 1991][research_a_parametric_1991]
- [A Properties of Standard 2006][research_a_properties_2006]
- [A summary of the active flexible wing program][research_afw_summary]
- [A synthesis of reduced-order 1994][research_a_synthesis_1994]
- [A-7 Transonic Wing Designs 1982][research_a_7_transonic_1982]
- [Abdallah 2018][research_abdallah_2018]
- [Abdallah et al 2013][research_abdallah_newman_2013]
- [Abdallah et al 2014][research_abdallah_newman_2014]
- [Abdelkader et al 2011][research_abdelkader_harmin_2011]
- [Abdi, F. et al 1988][research_abdif_ideh_1988]
- [Abdullah and Sulaeman 2013][research_abdullah_sulaeman_2013]
- [Abdulrahim et al 2004][research_abdulrahim_garcia_2004]
- [Abdulrahim et al 2018][research_abdulrahim_weibley_2018]
- [Abel 1972][research_abel_1972]
- [Abel and Newsom 1981][research_abel_newsom_1981]
- [Abel et al 1977][research_abel_perryiii_1977]
- [Abel et al 1978][research_abel_iii_1978]
- [Abel et al 1979][research_abel_newsom_1979]
- [Abraham-Doman and Merrett 2014][research_abrahamdoman_merrett_2014]
- [Abramova et al 2016][research_abramova_petrov_2016]
- [Achache and Whalley 1996][research_achache_whalley_1996]
- [ACM produces 737 aileron 2005][research_acm_produces_2005]
- [Active aeroelastic wing aerodynamic model development and validation for a modified F/A-18A][research_aaw_aero_model]
- [Active aeroelastic wing flight research program, technical program and model analytical development][research_aaw_technical_program]
- [Active control of a 1994][research_active_control_1994]
- [Active Flutter Suppression 2016][research_active_flutter_2016]
- [Active flutter suppression via 1999][research_active_flutter_1999]
- [Adali 1981][research_adali_1981]
- [Adamson et al 2019][research_adamson_fichera_2019]
- [Adaptive Transonic Aeroservoelasticity 2016][research_adaptive_transonic_2016]
- [Adnyana 2017][research_adnyana_2017]
- [Advisory Group for Aerospace Research and Development 1984][research_advisorygroupforaerospaceresearchanddevelopment_1984]
- [Aero structural optimization for 2018][research_aero_structural_2018]
- [Aerodynamic Phenomena in Supersonic 2020][research_aerodynamic_phenomena_2020]
- [Aeroelastic Control 2005][research_aeroelastic_control_2005]
- [Aeroelastic modeling of the active flexible wing wind-tunnel model][research_afw_modeling]
- [Aeroelastic Modelling 2016][research_aeroelastic_modelling_2016]
- [Aeroelasticity Problems in Compressible 2010][research_aeroelasticity_problems_2010]
- [Aeroservoelastic tailoring for lateral control enhancement][research_aeroservoelastic_tailoring]
- [Aeroservoelastic wind-tunnel investigations using the active flexible wing model, status and recent accomplishments][research_afw_tm101570]
- [Afkhami and Alighanbari 2007][research_afkhami_alighanbari_2007]
- [Agarwal and Deese 1983][research_agarwal_deese_1983]
- [Agarwal and Deese 1984][research_agarwal_deese_1984]
- [Agostinelli and Allen 2012][research_agostinelli_allen_2012]
- [Agrawal et al 1991][research_agrawal_kinard_1991]
- [Ahmad and Gazetas 1992][research_ahmad_gazetas_1992]
- [Ahmad et al 2018][research_ahmad_baig_2018]
- [Ahmadi and Farsadi 2024][research_ahmadi_farsadi_2024]
- [Ahmadi Tehrani et al 2025][research_ahmaditehrani_ellis_2025]
- [Aileron 2005][research_aileron_2005]
- [Air Force Flight Test Center Edwards Afb Ca 1970][research_airforceflighttestcenteredwardsafbca_1970]
- [Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974]
- [Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974_b]
- [Air Force Flight Test Center Edwards Afb Ca 2002][research_airforceflighttestcenteredwardsafbca_2002]
- [Air Force Test Pilot School Edwards Afb Ca 1962][research_airforcetestpilotschooledwardsafbca_1962]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988]
- [Air Force Test Pilot School Edwards Afb Ca 1989][research_airforcetestpilotschooledwardsafbca_1989]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_b]
- [Ajaj and Djidjeli 2022][research_ajaj_djidjeli_2022]
- [Akasaka et al 1989][research_akasaka_katoh_1989]
- [Akinwale and Datta 2025][research_akinwale_datta_2025]
- [Akmese et al 2009][research_akmese_comert_2009]
- [Al-Shehabi and Newman 2000][research_alshehabi_newman_2000]
- [Al-Shehabi and Newman 2000][research_alshehabi_newman_2000_b]
- [Alag and Burken 1987][research_alag_burken_1987]
- [Alag et al 1986][research_alag_burken_1986]
- [Alam and Hromcik 2019][research_alam_hromcik_2019]
- [Alam and Sohn 2023][research_alam_sohn_2023]
- [Alam et al 2015][research_alam_hromcik_2015]
- [Alaverdi and Paris 2001][research_alaverdi_paris_2001]
- [Albertani et al 2005][research_albertani_stanford_2005]
- [Albisser][research_albisser]
- [Alden and Schindel 1952][research_alden_schindel_1952]
- [Alhajjar et al 2018][research_alhajjar_aljiboory_2018]
- [Ali 2024][research_ali_2024]
- [Alighanbari 2002][research_alighanbari_2002]
- [Alighanbari and Lee 2003][research_alighanbari_lee_2003]
- [Allaire et al 2014][research_allaire_lecerf_2014]
- [Allen and Pollock 1983][research_allen_pollock_1983]
- [Allen et al 1986][research_allen_reardon_1986]
- [Allen et al 2003][research_allen_fenwick_2003]
- [Allen et al 2005][research_allen_lizotte_2005]
- [Allyn and Takahashi 2016][research_allyn_takahashi_2016]
- [Alsaidi et al 2018][research_alsaidi_akbar_2018]
- [Alsaidi et al 2018][research_alsaidi_akbar_2018_b]
- [Alsaidi et al 2019][research_alsaidi_joe_2019]
- [Alsaidi et al 2019][research_alsaidi_joe_2019_b]
- [Alstrom et al 2010][research_alstrom_marzocca_2010]
- [Altman 1952][research_altman_1952]
- [Alulema et al 2020][research_alulema_valencia_2020]
- [Alvarez 2014][research_alvarez_2014]
- [Alvarez and Wissa 2021][research_alvarez_wissa_2021]
- [Alwi and Edwards 2007][research_alwi_edwards_2007]
- [Alwi and Edwards 2009][research_alwi_edwards_2009]
- [Alyanak and Pendleton 2014][research_alyanak_pendleton_2014]
- [Alyanak and Pendleton 2017][research_alyanak_pendleton_2017]
- [Amendola et al 2018][research_amendola_dimino_2018]
- [Ameri et al 2007][research_ameri_lowenberg_2007]
- [American Institute of Aeronautics and Astronautics 1993][research_americaninstituteofaeronauticsandastronautics_1993]
- [Amoozgar and Irani 2012][research_amoozgar_irani_2012]
- [Amoozgar and Shahverdi 2019][research_amoozgar_shahverdi_2019]
- [Amoozgar et al 2013][research_amoozgar_irani_2013]
- [Amoozgar et al 2020][research_amoozgar_fazelzadeh_2020]
- [Amoozgar et al 2021][research_amoozgar_friswell_2021]
- [Amoozgar et al 2024][research_amoozgar_hall_2024]
- [An application of the active flexible wing concept to an F-16 derivative wing][research_afw_f16_derivative]
- [An et al 2018][research_an_xie_2018]
- [An et al 2023][research_an_zhu_2023]
- [An experimental and computational 1978][research_an_experimental_1978]
- [An overview of the active flexible wing program][research_afw_overview]
- [Andakhshideh and Tahani 2013][research_andakhshideh_tahani_2013]
- [Andersen et al 1996][research_andersen_forster_1996]
- [Andersen et al 1997][research_andersen_forster_1997]
- [Andersen et al 1998][research_andersen_kolonay_1998]
- [Anderson 1984][research_anderson_1984]
- [Anderson 1985][research_anderson_1985]
- [Anderson 1993][research_anderson_1993]
- [Anderson et al 1972][research_anderson_berger_1972]
- [Anderson et al 1983][research_anderson_vincent_1983]
- [Anderson et al 2004][research_anderson_white_2004]
- [Anderson et al 2005][research_anderson_white_2005]
- [Anderson et al 2026][research_anderson_caverly_2026]
- [Andrews and Gordon 1981][research_andrews_gordon_1981]
- [Andrienko et al 2010][research_andrienko_tropova_2010]
- [Andrighettoni and Mantegazza 1998][research_andrighettoni_mantegazza_1998]
- [Ansell et al 2010][research_ansell_bragg_2010]
- [Ansell et al 2011][research_ansell_bragg_2011]
- [Ansell et al 2011][research_ansell_bragg_2011_b]
- [Ansell et al 2013][research_ansell_kerho_2013]
- [Ansell et al 2014][research_ansell_kerho_2014]
- [Antonakis and Biannic 2024][research_antonakis_biannic_2024]
- [Aouf et al 2000][research_aouf_boulet_2000]
- [Appendix A Standard Atmosphere 2021][research_appendix_a_2021]
- [Appendix A. The Standard 2011][research_appendix_a_2011]
- [Appendix B Properties of 2003][research_appendix_b_2003]
- [Appendix B Solution to 2016][research_appendix_b_2016]
- [Appendix C Flutter Analysis 2016][research_appendix_c_2016]
- [Application of a Shock-Turbulent 1982][research_application_of_1982_b]
- [Application of active flexible wing technology to the Agile Falcon][research_agile_falcon]
- [Application of Computational Methods 1982][research_application_of_1982]
- [Apte and Athani 1979][research_apte_athani_1979]
- [Arai and Tanaka 2020][research_arai_tanaka_2020]
- [Aravinth et al 2018][research_aravinth_shinde_2018]
- [Archambaud et al 2004][research_archambaud_louis_2004]
- [Aref'ev 1968][research_arefev_1968]
- [Arizono and Cesnik 2013][research_arizono_cesnik_2013]
- [Arizono and Isogai 2005][research_arizono_isogai_2005]
- [Armanious and Lind 2018][research_armanious_lind_2018]
- [Armstrong 1977][research_armstrong_1977]
- [Armstrong and Miller 1968][research_armstrong_miller_1968]
- [Arnold 1942][research_arnold_1942]
- [Arnold 1981][research_arnold_1981]
- [Asadi and Farsadi 2020][research_asadi_farsadi_2020]
- [Asadi et al 2021][research_asadi_farsadi_2021]
- [Asaro et al 2023][research_asaro_cavaliere_2023]
- [Ashkenas 1965][research_ashkenas_1965]
- [Askari and Soltani 2019][research_askari_soltani_2019]
- [Aslam-Mir and McLean][research_aslammir_mclean]
- [Atkinson 2016][research_atkinson_2016]
- [Atmosphere standard atmosphere 2006][research_atmosphere_standard_2006]
- [Auls'chenko et al 2006][research_aulschenko_zamuraev_2006]
- [Austin et al 1976][research_austin_hadcock_1976]
- [Avci et al 2026][research_avci_tegin_2026]
- [Ayaz et al 2024][research_ayaz_rasoolmemon_2024]
- [Azevedo 1987][research_azevedo_1987]
- [Azizov et al 2019][research_azizov_derkowski_2019]
- [Azzi et al 2024][research_azzi_tahiliani_2024]
- [B-34. U. S. Standard 1963][research_b_34_u_1963]
- [Babcock and Lind 2012][research_babcock_lind_2012]
- [Babcock and Lind 2012][research_babcock_lind_2012_b]
- [Babcock and Lind 2013][research_babcock_lind_2013]
- [Babcock and Lind 2013][research_babcock_lind_2013_b]
- [Babinsky and Délery 2011][research_babinsky_delery_2011]
- [Babister 1980][research_babister_1980]
- [Bach and McNally 1988][research_bach_mcnally_1988]
- [Bachelder et al 2004][research_bachelder_klyde_2004]
- [Bachelder et al 2011][research_bachelder_thompson_2011]
- [Badcock et al 2003][research_badcock_rampurawala_2003]
- [Bae and Lee 2002][research_bae_lee_2002]
- [Bae et al 2002][research_bae_yang_2002]
- [Bae et al 2004][research_bae_inman_2004]
- [Baer-Riedhart 1981][research_baerriedhart_1981]
- [Baggi et al 2020][research_baggi_franco_2020]
- [Baggi et al 2022][research_baggi_serrani_2022]
- [Bagherzadeh 2020][research_bagherzadeh_2020]
- [Bahia Monteiro et al 2023][research_bahiamonteiro_gray_2023]
- [Bai et al 2014][research_bai_zhang_2014]
- [Bai et al 2022][research_bai_cao_2022]
- [Bailey et al 1988][research_bailey_powers_1988]
- [Bajaj 2019][research_bajaj_2019]
- [Baker and Forsey 1981][research_baker_forsey_1981]
- [Balakrishnan 2006][research_balakrishnan_2006]
- [Balakrishnan 2007][research_balakrishnan_2007]
- [Balakrishnan 2012][research_balakrishnan_2012]
- [Balakrishnan and Iliff 2007][research_balakrishnan_iliff_2007]
- [Balas et al 2004][research_balas_hindman_2004]
- [Balas et al 2011][research_balas_seiler_2011]
- [Balas et al 2012][research_balas_moreno_2012]
- [Balatti et al 2023][research_balatti_ellis_2023]
- [Balatti et al 2023][research_balatti_khodaparast_2023]
- [Baldelli et al 2009][research_baldelli_zeng_2009]
- [Ball 1978][research_ball_1978]
- [Ball 1979][research_ball_1979]
- [Balleur et al 2002][research_balleur_girodrouxlavigne_2002]
- [Balon et al 2021][research_balon_benes_2021]
- [Bamber, Millard J 1934][research_bambermillardj_1934]
- [Banavara and Newsom 2010][research_banavara_newsom_2010]
- [Banerjee and Williams 1992][research_banerjee_williams_1992]
- [Banerjee et al 2014][research_banerjee_liu_2014]
- [Bang et al 2022][research_bang_rana_2022]
- [Baranyi 2006][research_baranyi_2006]
- [Baranyi 2006][research_baranyi_2006_b]
- [Baranyi and Patton 2003][research_baranyi_patton_2003]
- [Barb and Mulder 2003][research_barb_mulder_2003]
- [Barker and Balas 2000][research_barker_balas_2000]
- [Barker et al 1999][research_barker_balas_1999]
- [Barnwell 1974][research_barnwell_1974]
- [Bartels et al 2019][research_bartels_stanford_2019]
- [Bartels et al 2019][research_bartels_stanford_2019_b]
- [Barzgaran et al 2021][research_barzgaran_quenzer_2021]
- [Bass et al 1993][research_bass_thompson_1993]
- [Bass et al 1995][research_bass_thompson_1995]
- [Bateman et al 2023][research_bateman_dewekker_2023]
- [Batina 1986][research_batina_1986]
- [Baumann et al 2008][research_baumann_pahle_2008]
- [Baz and Chen 1993][research_baz_chen_1993]
- [Baz et al 1987][research_baz_iman_1987]
- [Bdeiwi et al 2019][research_bdeiwi_ciarella_2019]
- [Beatty et al 1977][research_beatty_brooks_1977]
- [Beaverstock et al 2015][research_beaverstock_woods_2015]
- [Bednarz et al 2013][research_bednarz_zhu_2013]
- [Begnini et al 2018][research_begnini_bones_2018]
- [Beh et al 2018][research_beh_hofinger_2018]
- [Behal et al 2004][research_behal_marzocca_2004]
- [Behal et al 2006][research_behal_marzocca_2006]
- [Beldica and Hilton 1999][research_beldica_hilton_1999]
- [Belesiotis-Kataras and Timme 2021][research_belesiotiskataras_timme_2021]
- [Belisle et al 2010][research_belisle_neale_2010]
- [Belote and Menezes 2019][research_belote_menezes_2019]
- [Ben Asher and Raveh 2023][research_benasher_raveh_2023]
- [Bendiksen 1992][research_bendiksen_1992]
- [Bendiksen 1993][research_bendiksen_1993]
- [Bendiksen 2001][research_bendiksen_2001]
- [Bendiksen et al 1997][research_bendiksen_hwang_1997]
- [Bendixen et al 1981][research_bendixen_oconnell_1981]
- [Benjamin M Simmons][research_benjaminmsimmons]
- [Bennett et al 1985][research_bennett_seidel_1985]
- [Bennett et al 1991][research_bennett_dansberry_1991]
- [Bennett et al 1993][research_bennett_dansberry_1993]
- [Bennett et al 2001][research_bennett_brown_2001]
- [Bennett, R. M. et al 1977][research_bennettrm_farmermg_1977]
- [Benosman et al 2007][research_benosman_liao_2007]
- [Benyamen and Keshmiri 2022][research_benyamen_keshmiri_2022]
- [Berci 2017][research_berci_2017]
- [Beresh et al 2020][research_beresh_barone_2020]
- [Bergman et al 2011][research_bergman_vakakis_2011]
- [Bergmann and Sevart 1973][research_bergmann_sevart_1973]
- [Bergmann and Sevart 1975][research_bergmann_sevart_1975]
- [Bernelli-Zazzera et al 2000][research_bernellizazzera_mantegazza_2000]
- [Bernhard and Chopra 1996][research_bernhard_chopra_1996]
- [Bernhard and Chopra 1997][research_bernhard_chopra_1997]
- [Berton 2022][research_berton_2022]
- [Beug et al 2012][research_beug_moser_2012]
- [Bever 1992][research_bever_1992]
- [Beyer et al 2024][research_beyer_steen_2024]
- [Beyer et al 2024][research_beyer_ullah_2024]
- [Bhat 2018][research_bhat_2018]
- [Bhat 2018][research_bhat_2018_b]
- [Bhat 2018][research_bhat_2018_c]
- [Bhat 2018][research_bhat_2018_d]
- [Bi et al 2017][research_bi_xie_2017]
- [Bi et al 2017][research_bi_xie_2017_b]
- [Bian et al 2018][research_bian_nener_2018]
- [Bian et al 2019][research_bian_nener_2019]
- [Bichiou et al 2016][research_bichiou_hajj_2016]
- [Biederman et al 1994][research_biederman_meincke_1994]
- [Bielawa 2006][research_bielawa_2006]
- [Bigler 1986][research_bigler_1986]
- [Bihrle and Barnhart 1982][research_bihrle_barnhart_1982]
- [Bihrle et al 1980][research_bihrle_jr_1980]
- [Bilgen et al 2011][research_bilgen_saavedraflores_2011]
- [Binder et al 2021][research_binder_wildschek_2021]
- [Binwen Lu et al 2016][research_binwenlu_jianjunma_2016]
- [Birks and Ludlow 1969][research_birks_ludlow_1969]
- [Bismarck-Nasr 1992][research_bismarcknasr_1992]
- [Bismarck-Nasr 1994][research_bismarcknasr_1994]
- [Biswas and Jimbo 2015][research_biswas_jimbo_2015]
- [Black et al 2007][research_black_schwaab_2007]
- [Blair 1994][research_blair_1994]
- [Blair and Canfield 2002][research_blair_canfield_2002]
- [Blair and Weisshaar 1982][research_blair_weisshaar_1982]
- [Blair et al 2008][research_blair_robinson_2008]
- [Blank 1995][research_blank_1995]
- [Bleimeyer 1981][research_bleimeyer_1981]
- [Blight et al 2018][research_blight_lanedailey_2018]
- [Block and Strganac 1998][research_block_strganac_1998]
- [Block et al 1997][research_block_gilliatt_1997]
- [Blue et al 1997][research_blue_balas_1997]
- [Bocola et al 2015][research_bocola_muscarello_2015]
- [Bodin and Fuchs 2008][research_bodin_fuchs_2008]
- [Bodson 2000][research_bodson_2000]
- [Boehm et al 2001][research_boehm_flick_2001]
- [Bogatyrev 2017][research_bogatyrev_2017]
- [Bohacek et al][research_bohacek_nakamura]
- [Bohlmann et al 1988][research_bohlmann_weisshaar_1988]
- [Bohlmann et al 1990][research_bohlmann_eckstrom_1990]
- [Bohlmann et al 1992][research_bohlmann_love_1992]
- [Bohlmann, Jonathan D. and Scott, Robert C. 1991][research_bohlmannjonathand_scottrobertc_1991]
- [Bonnema and Smith 1988][research_bonnema_smith_1988]
- [Bonnema, Kenneth L. and Lokos, William A. 1989][research_bonnemakennethl_lokoswilliama_1989]
- [Bontoft et al 2026][research_bontoft_bhuwal_2026]
- [Bontoft et al 2026][research_bontoft_bhuwal_2026_b]
- [Boothe et al 1974][research_boothe_chen_1974]
- [Boppe 1977][research_boppe_1977]
- [Bordogna et al 2016][research_bordogna_macquart_2016]
- [Bordogna et al 2020][research_bordogna_lancelot_2020]
- [Borglund 2003][research_borglund_2003]
- [Borglund and Kuttenkeuler 2002][research_borglund_kuttenkeuler_2002]
- [Borglund and Nilsson 2004][research_borglund_nilsson_2004]
- [Bosch et al 2014][research_bosch_schmehl_2014]
- [Boskovic and Mehra][research_boskovic_mehra]
- [Boskovic et al][research_boskovic_ling]
- [Botez et al 2002][research_botez_doin_2002]
- [Botez et al 2008][research_botez_grigorie_2008]
- [Botez et al 2018][research_botez_koreanschi_2018]
- [Bottasso and Montinari 2013][research_bottasso_montinari_2013]
- [Bouadi][research_bouadi]
- [Bouchalkha et al 2015][research_bouchalkha_alhammadi_2015]
- [Bove 2026][research_bove_2026]
- [Bradshaw et al 1988][research_bradshaw_rahulan_1988]
- [Bramsiepe et al 2020][research_bramsiepe_voss_2020]
- [Brandon and Morelli 2014][research_brandon_morelli_2014]
- [Bras et al 2022][research_bras_warwick_2022]
- [Braun et al][research_braun_boucke]
- [Braun et al 2003][research_braun_boucke_2003]
- [Breitenstein et al 2023][research_breitenstein_muller_2023]
- [Breitenstein et al 2024][research_breitenstein_muller_2024]
- [Breitsamter 2005][research_breitsamter_2005]
- [Breitsamter and Laschka 2000][research_breitsamter_laschka_2000]
- [Breitsamter and Schmid 2008][research_breitsamter_schmid_2008]
- [Brenner 2002][research_brenner_2002]
- [Brenner and Lind 1998][research_brenner_lind_1998]
- [Brenner and Prazenica 2005][research_brenner_prazenica_2005]
- [Brenner et al 1997][research_brenner_feron_1997]
- [Brenner, Martin J. 1996][research_brennermartinj_1996]
- [Brenner, Martin J. 2001][research_brennermartinj_2001]
- [Breul 1963][research_breul_1963]
- [Brewer, Gerald W. 1946][research_brewergeraldw_1946]
- [Briardy and Head 1968][research_briardy_head_1968]
- [Brincklow and Hunsaker 2021][research_brincklow_hunsaker_2021]
- [Brincklow et al 2021][research_brincklow_montgomery_2021]
- [Brinker and Wise 2000][research_brinker_wise_2000]
- [Bronz and Hattenberger 2016][research_bronz_hattenberger_2016]
- [Brooks and Meyer 1995][research_brooks_meyer_1995]
- [Brown 1989][research_brown_1989]
- [Brown and Caverly 2021][research_brown_caverly_2021]
- [Brown and Singh 2015][research_brown_singh_2015]
- [Brown and Singh 2016][research_brown_singh_2016]
- [Brown et al 2004][research_brown_dillon_2004]
- [Brown et al 2017][research_brown_singh_2017]
- [Brown, Jr. 1970][research_brownjr_1970]
- [Brown, Stuart C. 1959][research_brownstuartc_1959]
- [Browne et al 2024][research_browne_maldonado_2024]
- [Bruni et al 2014][research_bruni_cestino_2014]
- [Bruni et al 2015][research_bruni_frulla_2015]
- [Bruno Santos et al 2020][research_brunosantos_oliveira_2020]
- [Bryson, Jr. and Desai 1968][research_brysonjr_desai_1968]
- [Bucharles and Vacher 2002][research_bucharles_vacher_2002]
- [Buddhamatya et al 2026][research_buddhamatya_miranda_2026]
- [Buffington 1997][research_buffington_1997]
- [Buffington 1999][research_buffington_1999]
- [Bugała 2025][research_bugala_2025]
- [Bugała et al 2023][research_bugala_sznajder_2023]
- [Bunge et al 2015][research_bunge_munerasavino_2015]
- [Bunge et al 2016][research_bunge_alkurdi_2016]
- [Bunton and Denegri 2000][research_bunton_denegri_2000]
- [Burch 1966][research_burch_1966]
- [Burch 1967][research_burch_1967]
- [Burcham, Jr. and Burken 1994][research_burchamjr_burken_1994]
- [Burcham, Jr. et al 1981][research_burchamjr_myers_1981]
- [Burchett 2011][research_burchett_2011]
- [Burchett 2012][research_burchett_2012]
- [Bureerat 2026][research_bureerat_2026]
- [Burgstaller and Galffy 2024][research_burgstaller_galffy_2024]
- [Burken et al 1986][research_burken_alag_1986]
- [Burner and Martinson 1996][research_burner_martinson_1996]
- [Burner et al 2000][research_burner_liu_2000]
- [Burner, Alpheus W. et al 2005][research_burneralpheusw_lokoswilliama_2005]
- [Burris and Bender 1969][research_burris_bender_1969]
- [Burris and Bender 1969][research_burris_bender_1969_b]
- [Burrows et al 2021][research_burrows_vukasinovic_2021]
- [Burt Jr 1976][research_burtjr_1976]
- [Burton and Kneeland, Jr. 1981][research_burton_kneelandjr_1981]
- [Butler et al 1995][research_butler_lillico_1995]
- [Buttrill and Houck 1990][research_buttrill_houck_1990]
- [Byreddy et al 2003][research_byreddy_grandhi_2003]
- [Byun and Guruswamy 1994][research_byun_guruswamy_1994]
- [Byun and Guruswamy 1996][research_byun_guruswamy_1996]
- [Byun and Guruswamy 1996][research_byun_guruswamy_1996_b]
- [Byun and Guruswamy 1996][research_byun_guruswamy_1996_c]
- [Cabaleiro de la Hoz and Fioriti 2021][research_cabaleirodelahoz_fioriti_2021]
- [Cahill 1986][research_cahill_1986]
- [Calculation of Elastic Deformations 2004][research_calculation_of_2004]
- [Calculation of the lateral control of swept and unswept flexible wings of arbitrary stiffness][research_lateral_control_flexible]
- [Calder and Gupta 1977][research_calder_gupta_1977]
- [Campbell and Smith 1987][research_campbell_smith_1987]
- [Candida et al 2019][research_candida_souzadepaula_2019]
- [Canfield 2014][research_canfield_2014]
- [Canniff 1969][research_canniff_1969]
- [Cao and Lyu 2024][research_cao_lyu_2024]
- [Cao et al 2024][research_cao_zhao_2024]
- [Cao et al 2025][research_cao_lin_2025]
- [Carafoli 1969][research_carafoli_1969]
- [Carico 1998][research_carico_1998]
- [Carlson 1981][research_carlson_1981]
- [Carlson and Cassarino 1973][research_carlson_cassarino_1973]
- [Carlson and Weed 1985][research_carlson_weed_1985]
- [Carlsson 2003][research_carlsson_2003]
- [Carlsson 2004][research_carlsson_2004]
- [Carlsson 2005][research_carlsson_2005]
- [Carlsson and Cronander 2005][research_carlsson_cronander_2005]
- [Carpenter et al 2018][research_carpenter_solomon_2018]
- [Carrillo et al 2022][research_carrillo_mertens_2022]
- [Carrillo et al 2024][research_carrillo_debreuker_2024]
- [Carruthers et al 2007][research_carruthers_taylor_2007]
- [Carter][research_carter]
- [Cartwright 2010][research_cartwright_2010]
- [Cassel et al 1969][research_cassel_durando_1969]
- [Castellani et al 2016][research_castellani_cooper_2016]
- [Castellani et al 2016][research_castellani_cooper_2016_b]
- [Castellani et al 2017][research_castellani_cooper_2017]
- [Castillo Zuñiga et al 2019][research_castillozuniga_giacobinisouza_2019]
- [Caughey 1982][research_caughey_1982]
- [Caughey and Jameson 1977][research_caughey_jameson_1977]
- [Cavagna et al 2009][research_cavagna_ricci_2009]
- [Cavagna et al 2011][research_cavagna_ricci_2011]
- [Cavaliere and Fezans 2024][research_cavaliere_fezans_2024]
- [Cavanaugh et al 2007][research_cavanaugh_robertson_2007]
- [Caverly et al 2017][research_caverly_forbes_2017]
- [Cavin and Holyoak 1978][research_cavin_holyoak_1978]
- [Cazier, Jr. and Kehoe 1986][research_cazierjr_kehoe_1986]
- [Cea and Palacios 2023][research_cea_palacios_2023]
- [Cea and Palacios 2024][research_cea_palacios_2024]
- [Celi 1991][research_celi_1991]
- [Celi 1994][research_celi_1994]
- [Cella and Biancolini 2012][research_cella_biancolini_2012]
- [Cen et al 2025][research_cen_xu_2025]
- [Cen et al 2026][research_cen_xu_2026]
- [Cesnik 2002][research_cesnik_2002]
- [Cesnik 2005][research_cesnik_2005]
- [Cesnik and Brown 2002][research_cesnik_brown_2002]
- [Cesnik et al 1999][research_cesnik_shin_1999]
- [Cesnik et al 2000][research_cesnik_ortegamorales_2000]
- [Cesnik et al 2023][research_cesnik_ritter_2023]
- [Cestino and Iannuzzo 2026][research_cestino_iannuzzo_2026]
- [Chae et al 2017][research_chae_moosavian_2017]
- [Chahmi 2022][research_chahmi_2022]
- [Chajec et al 2019][research_chajec_krzymien_2019]
- [Chakrabartty and Dhanalakshmi 1995][research_chakrabartty_dhanalakshmi_1995]
- [Chakravarty and Moore 1986][research_chakravarty_moore_1986]
- [Chan et al 2017][research_chan_hooker_2017]
- [Chand and Hansen][research_chand_hansen]
- [Chandrasekharan et al 2015][research_chandrasekharan_iarocci_2015]
- [Chandre Vila][research_chandrevila]
- [Chang 2005][research_chang_2005]
- [Chang et al 2002][research_chang_trivailo_2002]
- [Chang et al 2010][research_chang_yang_2010]
- [Chaparro et al 2017][research_chaparro_fujiwara_2017]
- [Chapman 1969][research_chapman_1969]
- [Chapman and Yates 1992][research_chapman_yates_1992]
- [Chapter 15. Aeroelastic Systems 1994][research_chapter_15_1994]
- [Chapter 2. Exploring the 2005][research_chapter_2_2005]
- [Chapter 3. Aerodynamics of 1960][research_chapter_3_1960]
- [Chapter 5. Wing-Body Interference 1957][research_chapter_5_1957]
- [Chapter III Elastic Deformations 1982][research_chapter_iii_1982]
- [Charts for the determination of wing torsional stiffness required for specified rolling characteristics][research_charts_torsional_stiffness]
- [Chase][research_chase]
- [Chase and McDonald 2014][research_chase_mcdonald_2014]
- [Chawla et al 1988][research_chawla_edwards_1988]
- [Chen 1982][research_chen_1982]
- [Chen 2015][research_chen_2015]
- [Chen and Han 2017][research_chen_han_2017]
- [Chen and Liu 2014][research_chen_liu_2014]
- [Chen et al 1984][research_chen_vassberg_1984]
- [Chen et al 1998][research_chen_chang_1998]
- [Chen et al 2006][research_chen_wickramasinghe_2006]
- [Chen et al 2008][research_chen_baldelli_2008]
- [Chen et al 2009][research_chen_ulker_2009]
- [Chen et al 2015][research_chen_zhou_2015]
- [Chen et al 2018][research_chen_zhou_2018]
- [Chen et al 2023][research_chen_shi_2023]
- [Chen et al 2023][research_chen_shi_2023_b]
- [Chen et al 2026][research_chen_cai_2026]
- [Chen et al 2026][research_chen_ding_2026]
- [Chen et al 2026][research_chen_gray_2026]
- [Chen et al 2026][research_chen_zhang_2026]
- [Cheney 1988][research_cheney_1988]
- [Cheng 1961][research_cheng_1961]
- [Cheng 1982][research_cheng_1982]
- [Cheng et al 1987][research_cheng_edwards_1987]
- [Cheng et al 2023][research_cheng_cea_2023]
- [Cheng et al 2023][research_cheng_shi_2023]
- [Cheng et al 2025][research_cheng_song_2025]
- [Chestnutt 1966][research_chestnutt_1966]
- [Cheung et al 2019][research_cheung_rezgui_2019]
- [Cheung et al 2019][research_cheung_rezgui_2019_b]
- [Cheung et al 2020][research_cheung_rezgui_2020]
- [Cheung et al 2023][research_cheung_palles_2023]
- [Chin][research_chin]
- [Chin et al 1987][research_chin_chacon_1987]
- [Chin et al 2011][research_chin_brenner_2011]
- [Chipman et al 1982][research_chipman_zislin_1982]
- [Chipman et al 1983][research_chipman_zislin_1983]
- [Choi et al 2020][research_choi_lim_2020]
- [Chopra 1983][research_chopra_1983]
- [Chopra 1988][research_chopra_1988]
- [Chung 2002][research_chung_2002]
- [Chung et al 2002][research_chung_lee_2002]
- [Chung et al 2019][research_chung_cho_2019]
- [Chung et al 2021][research_chung_su_2021]
- [ChunSheng Liu et al 2012][research_chunshengliu_xinzhongzhu_2012]
- [Chyu and Kuwahara 1982][research_chyu_kuwahara_1982]
- [Ciniglio et al 2003][research_ciniglio_manimala_2003]
- [Cizmas and Strganac 2010][research_cizmas_strganac_2010]
- [Clark 2001][research_clark_2001]
- [Clark 2026][research_clark_2026]
- [Clark and Valarezo 1990][research_clark_valarezo_1990]
- [Clarke and Roskam 1982][research_clarke_roskam_1982]
- [Clarke et al 2005][research_clarke_allen_2005]
- [Cliett 1952][research_cliett_1952]
- [Clyde et al 1984][research_clyde_bonner_1984]
- [Cocco and Meroli 2026][research_cocco_meroli_2026]
- [Cockrell and Doherr 1981][research_cockrell_doherr_1981]
- [Coder 2023][research_coder_2023]
- [Coder 2025][research_coder_2025]
- [Coe, Jr. and Perkins 1990][research_coejr_perkins_1990]
- [Coetzee et al 2023][research_coetzee_lowenberg_2023]
- [Cole 1990][research_cole_1990]
- [Cole and Weiland 2009][research_cole_weiland_2009]
- [Cole et al 2003][research_cole_noll_2003]
- [Colombo et al 2018][research_colombo_muscarello_2018]
- [Comer et al 2024][research_comer_bhandari_2024]
- [Cong et al 2023][research_cong_hu_2023]
- [Conti et al 2021][research_conti_saltari_2021]
- [Control Allocation and Flight 2016][research_control_allocation_2016]
- [Cook 1964][research_cook_1964]
- [Cook 1965][research_cook_1965]
- [Cook and Smith 2014][research_cook_smith_2014]
- [Cord 1989][research_cord_1989]
- [Corminboeuf 2015][research_corminboeuf_2015]
- [Cornell Aeronautical Lab Inc Buffalo Ny 1947][research_cornellaeronauticallabincbuffalony_1947]
- [Correction of model deformation 2017][research_correction_of_2017]
- [Cosentino and Holst 1985][research_cosentino_holst_1985]
- [Costa and Vilela 2014][research_costa_vilela_2014]
- [Cotoi and Botez 2002][research_cotoi_botez_2002]
- [Cotton 1974][research_cotton_1974]
- [Couch et al 2001][research_couch_duren_2001]
- [Covell et al 1986][research_covell_miller_1986]
- [Cowan et al 1998][research_cowan_arenajr_1998]
- [Cox and Roskam 1990][research_cox_roskam_1990]
- [Cramer and Nguyen 2020][research_cramer_nguyen_2020]
- [Crane, H. L. and Reeder, J. P. 1945][research_cranehl_reederjp_1945]
- [Crasta and Khan 2014][research_crasta_khan_2014]
- [Crawley et al 1995][research_crawley_curtiss_1995]
- [Cristofaro 2024][research_cristofaro_2024]
- [Crites et al 1992][research_crites_rueger_1992]
- [Crittenden et al 1977][research_crittenden_weisshaar_1977]
- [Crittenden et al 1978][research_crittenden_weishaar_1978]
- [Cruz and Kienitz 2007][research_cruz_kienitz_2007]
- [Cui et al 2021][research_cui_jianlong_2021]
- [Cumming and Diebler 2005][research_cumming_diebler_2005]
- [Cunningham 1972][research_cunningham_1972]
- [Cunningham 2017][research_cunningham_2017]
- [Cunningham et al 2008][research_cunningham_foster_2008]
- [Curpanaru et al 2025][research_curpanaru_pastor_2025]
- [Currao and Yeh 2026][research_currao_yeh_2026]
- [Cusimano and Johnson 1994][research_cusimano_johnson_1994]
- [D'Vari and Baker 1999][research_dvari_baker_1999]
- [Dai and Zhang 2023][research_dai_zhang_2023]
- [Dai et al 2012][research_dai_wu_2012]
- [Dai et al 2022][research_dai_qiu_2022]
- [Dale et al 2013][research_dale_cooper_2013]
- [Dale et al 2014][research_dale_cooper_2014]
- [Dallaire et al 2007][research_dallaire_tribes_2007]
- [Damveld 2004][research_damveld_2004]
- [Dancila and Botez 2014][research_dancila_botez_2014]
- [Daneshmehr et al 2013][research_daneshmehr_inman_2013]
- [Danowsky et al 2008][research_danowsky_thompson_2008]
- [Danowsky et al 2009][research_danowsky_thompson_2009]
- [Danowsky et al 2010][research_danowsky_brenner_2010]
- [Danowsky et al 2012][research_danowsky_schulze_2012]
- [Danowsky et al 2013][research_danowsky_thompson_2013]
- [Danowsky et al 2016][research_danowsky_lieu_2016]
- [Darabseh et al 2022][research_darabseh_tarabulsi_2022]
- [Darabseh et al 2022][research_darabseh_tarabulsi_2022_b]
- [Darden 1984][research_darden_1984]
- [Darden 1985][research_darden_1985]
- [Darida and Smrcek 1998][research_darida_smrcek_1998]
- [Das 2026][research_das_2026]
- [Das et al 2021][research_das_venkatraman_2021]
- [Davis][research_davis]
- [Davis 1974][research_davis_1974]
- [Daynes et al 2015][research_daynes_lachenal_2015]
- [De Breuker et al 2018][research_debreuker_binder_2018]
- [De Gaspari et al 2007][research_degaspari_ricci_2007]
- [De Gaspari et al 2015][research_degaspari_ricci_2015]
- [de Melo et al 2024][research_demelo_bussamra_2024]
- [de Visser 1999][research_devisser_1999]
- [de Visser and Pool 2023][research_devisser_pool_2023]
- [de Visser et al 2009][research_devisser_mulder_2009]
- [de Vries and Van Kampen 2019][research_devries_vankampen_2019]
- [Deangelis 1981][research_deangelis_1981]
- [DeAngelis 1982][research_deangelis_1982]
- [Decamp and Hardy 1984][research_decamp_hardy_1984]
- [Deconinck and Hirsch 1981][research_deconinck_hirsch_1981]
- [Deere et al 2011][research_deere_pao_2011]
- [Definition of the standard 1954][research_definition_of_1954]
- [Deflection-based aircraft structural loads estimation with comparison to flight][research_deflection_loads_flight]
- [Deflection-based structural loads estimation from the active aeroelastic wing F/A-18 aircraft][research_aaw_deflection_loads]
- [Dehaan 1990][research_dehaan_1990]
- [Deiler 2016][research_deiler_2016]
- [Deitering and Hilliard 1965][research_deitering_hilliard_1965]
- [DeLaurier 2024][research_delaurier_2024]
- [Delgado et al 2026][research_delgado_datta_2026]
- [Delgado Regis et al 2004][research_delgadoregis_mattos_2004]
- [Demasi 2024][research_demasi_2024]
- [Demasi and Livne 2005][research_demasi_livne_2005]
- [Demenkov 2009][research_demenkov_2009]
- [Demo 1986][research_demo_1986]
- [Demourant and Ferreres 2013][research_demourant_ferreres_2013]
- [Denegri and Dubben 2003][research_denegri_dubben_2003]
- [Denegri et al 2005][research_denegri_dubben_2005]
- [Dennis P. Dykstra 1980][research_dennispdykstra_1980]
- [Desmarais and Reed, Iii 1980][research_desmarais_reediii_1980]
- [Dessi and Mastroddi 2002][research_dessi_mastroddi_2002]
- [Determination of the effect of wing flexibility on lateral manoeuvrability][research_wing_flexibility_lateral]
- [Development and testing of control laws for the active aeroelastic wing program][research_aaw_control_laws]
- [Development of a Continuous 2012][research_development_of_2012]
- [Dhital and Chouvion 2024][research_dhital_chouvion_2024]
- [Di Pasquale 2024][research_dipasquale_2024]
- [Di Pasquale and Prince 2023][research_dipasquale_prince_2023]
- [Dias 2023][research_dias_2023]
- [Dias and Girardi 2016][research_dias_girardi_2016]
- [Dias et al 2015][research_dias_demarqui_2015]
- [Dibley et al 2005][research_dibley_allen_2005]
- [Dicarlo et al 1992][research_dicarlo_brown_1992]
- [Diedrich 1971][research_diedrich_1971]
- [Dieterich et al 2006][research_dieterich_enenkl_2006]
- [Dillenius and Mcintosh, Jr. 1988][research_dillenius_mcintoshjr_1988]
- [Dillinger et al 2020][research_dillinger_meddaikar_2020]
- [Dillsaver et al 2011][research_dillsaver_cesnik_2011]
- [Dilmi 2022][research_dilmi_2022]
- [Dimino et al 2021][research_dimino_andreutti_2021]
- [Dimitriadis 2008][research_dimitriadis_2008]
- [Dimitriadis 2011][research_dimitriadis_2011]
- [Dinyavari and Friedmann 1986][research_dinyavari_friedmann_1986]
- [Disney 1975][research_disney_1975]
- [Disney 1977][research_disney_1977]
- [Diwekar and Yedavalli 1995][research_diwekar_yedavalli_1995]
- [Dixit et al 2016][research_dixit_kodhanda_2016]
- [Dixon 1963][research_dixon_1963]
- [Dixon 1972][research_dixon_1972]
- [Djayapertapa and Allen 2002][research_djayapertapa_allen_2002]
- [Djojodihardjo 2023][research_djojodihardjo_2023]
- [Djojodihardjo 2023][research_djojodihardjo_2023_b]
- [Djojodihardjo 2023][research_djojodihardjo_2023_c]
- [Dobbs et al 1985][research_dobbs_miller_1985]
- [Dobronski 1988][research_dobronski_1988]
- [Doman and Oppenheimer 2002][research_doman_oppenheimer_2002]
- [Doman et al 2007][research_doman_gamble_2007]
- [Doman et al 2009][research_doman_gamble_2009]
- [Done 1996][research_done_1996]
- [Dong et al 2016][research_dong_lu_2016]
- [Dong et al 2024][research_dong_zhou_2024]
- [Dooley 1965][research_dooley_1965]
- [Dooley and Yeary 1979][research_dooley_yeary_1979]
- [Dorin and Smolin 1977][research_dorin_smolin_1977]
- [Dowell 1983][research_dowell_1983]
- [Dowell 1990][research_dowell_1990]
- [Dowell 1996][research_dowell_1996]
- [Dowell 1999][research_dowell_1999]
- [Dowell 2001][research_dowell_2001]
- [Dowell 2021][research_dowell_2021]
- [Dowell et al 1989][research_dowell_curtiss_1989]
- [Dowell et al 2006][research_dowell_attar_2006]
- [Downs and Prazenica 2022][research_downs_prazenica_2022]
- [Downs and Prazenica 2023][research_downs_prazenica_2023]
- [Dracopoulos and Oz 1992][research_dracopoulos_oz_1992]
- [Dracopoulos and Öz 1988][research_dracopoulos_oz_1988]
- [Drake and Balakrishnan 2004][research_drake_balakrishnan_2004]
- [Dreier 1987][research_dreier_1987]
- [Drew et al 2020][research_drew_hashemi_2020]
- [Drouet and Champoux 2014][research_drouet_champoux_2014]
- [Du Peloux De Saint Romain][research_dupelouxdesaintromain]
- [Duan and Zhang 2018][research_duan_zhang_2018]
- [Duan et al 2021][research_duan_kolmanovsky_2021]
- [Dubigeon 1992][research_dubigeon_1992]
- [Dubnický et al 2023][research_dubnicky_splichal_2023]
- [Duessler et al 2023][research_duessler_mylvaganam_2023]
- [Duessler et al 2024][research_duessler_mylvaganam_2024]
- [Duffy 1989][research_duffy_1989]
- [Dumpleton 1987][research_dumpleton_1987]
- [Duncan 1950][research_duncan_1950]
- [Dunning et al 2014][research_dunning_stanford_2014]
- [Durham et al 2016][research_durham_bordignon_2016]
- [Durmaz and Kaya 2013][research_durmaz_kaya_2013]
- [Durston and Stonum 1987][research_durston_stonum_1987]
- [Dwyer 1994][research_dwyer_1994]
- [Dynamic force calibration of][research_dynamic_force]
- [Dynamic Lateral-Directional Stability Theory 2003][research_dynamic_lateral_directional_2003]
- [Eastep et al 1998][research_eastep_andersen_1998]
- [Eastep et al 1999][research_eastep_tischler_1999]
- [Eckstrom and Spain 1982][research_eckstrom_spain_1982]
- [Ecsedi 2000][research_ecsedi_2000]
- [Edwards 1992][research_edwards_1992]
- [Edwards et al 1985][research_edwards_carter_1985]
- [Edwards et al 1986][research_edwards_whitfield_1986]
- [Edwards et al 1997][research_edwards_fittante_1997]
- [Effective Torsional Stiffness of 1976][research_effective_torsional_1976]
- [Efremov 1992][research_efremov_1992]
- [Eguea][research_eguea]
- [Ehlers and Weisshaar 1992][research_ehlers_weisshaar_1992]
- [Ehlers and Weisshaar 1993][research_ehlers_weisshaar_1993]
- [Eichelsdörfer 2026][research_eichelsdorfer_2026]
- [Eichelsdörfer 2026][research_eichelsdorfer_2026_b]
- [Elastic and Aeroelastic Instabilities 2008][research_elastic_and_2008]
- [Elastic Torsional Stiffness of 1965][research_elastic_torsional_1965]
- [Eldwaib et al 2018][research_eldwaib_grbovic_2018]
- [Elham and Bahamonde Jacome 2016][research_elham_bahamondejacome_2016]
- [Elham and Timmer 2016][research_elham_timmer_2016]
- [Elhami and Narab 2012][research_elhami_narab_2012]
- [Ellers and Boggs 2003][research_ellers_boggs_2003]
- [Ellis et al 2001][research_ellis_hui_2001]
- [Elshazly et al 2025][research_elshazly_kassem_2025]
- [Energy Approach To Performance 2003][research_energy_approach_2003]
- [Engel and Miller][research_engel_miller]
- [Engelien 1994][research_engelien_1994]
- [Epple and Altenbach 1982][research_epple_altenbach_1982]
- [Epstein 1954][research_epstein_1954]
- [Epureanu 2001][research_epureanu_2001]
- [Eraslan and Oktay 2023][research_eraslan_oktay_2023]
- [Eraslan and Oktay 2024][research_eraslan_oktay_2024]
- [Erdman 2005][research_erdman_2005]
- [Ericsson and Reding 1981][research_ericsson_reding_1981]
- [Eskandary et al 2012][research_eskandary_dardel_2012]
- [Eslimy-Isfahany and Banerjee 1995][research_eslimyisfahany_banerjee_1995]
- [Eslimy-Isfahany et al 1996][research_eslimyisfahany_banerjee_1996]
- [España and Gilyard 1995][research_espana_gilyard_1995]
- [Espńa and Gilyard 1994][research_espna_gilyard_1994]
- [Essenhigh 2006][research_essenhigh_2006]
- [Etnier 2001][research_etnier_2001]
- [Eulrich and Rynaski 1980][research_eulrich_rynaski_1980]
- [Everett et al 1972][research_everett_cashwell_1972]
- [Eversman and Danda Roy 1996][research_eversman_dandaroy_1996]
- [Eversman and Roy 1997][research_eversman_roy_1997]
- [Experimental results from the active aeroelastic wing wind tunnel test program][research_aaw_wind_tunnel]
- [Exploring the Flight Envelope 2015][research_exploring_the_2015]
- [Ezawa et al 2024][research_ezawa_nakatsugawa_2024]
- [F.M. Strain Gauge System 1975][research_f_m_strain_1975]
- [Fagbade and Heinz 2024][research_fagbade_heinz_2024]
- [Fan and Hall 2014][research_fan_hall_2014]
- [Fan and Lutze 1996][research_fan_lutze_1996]
- [Fan et al 2017][research_fan_liu_2017]
- [Fang and Yang 2025][research_fang_yang_2025]
- [Fang et al 2025][research_fang_wang_2025]
- [Farbridge and Smith 1977][research_farbridge_smith_1977]
- [Farbridge et al 1956][research_farbridge_woodward_1956]
- [Farhangnia et al 1996][research_farhangnia_guruswamy_1996]
- [Farhat 2001][research_farhat_2001]
- [Farhat and Amsallem 2011][research_farhat_amsallem_2011]
- [Farhat and Lin 1990][research_farhat_lin_1990]
- [Faroughi et al 2012][research_faroughi_malekzadeh_2012]
- [Farsadi et al 2026][research_farsadi_ahmadi_2026]
- [Fasel 2020][research_fasel_2020]
- [Favale et al 2021][research_favale_haidar_2021]
- [Fay and Johnstone 1960][research_fay_johnstone_1960]
- [Faïsse][research_faisse]
- [Faïsse et al 2021][research_faisse_vernay_2021]
- [Faïsse et al 2022][research_faisse_vernay_2022]
- [Fechter and Mills 1988][research_fechter_mills_1988]
- [Fejtek 1994][research_fejtek_1994]
- [Felker 1992][research_felker_1992]
- [Felker 1993][research_felker_1993]
- [Felt et al 1978][research_felt_huttsell_1978]
- [Feng et al 2015][research_feng_liu_2015]
- [Feng et al 2015][research_feng_liu_2015_b]
- [Fernandez Escudero][research_fernandezescudero]
- [Ferrara 2025][research_ferrara_2025]
- [Ferreres and Puyou 2006][research_ferreres_puyou_2006]
- [Ferrier et al 2018][research_ferrier_nguyen_2018]
- [Fezans 2017][research_fezans_2017]
- [Fezans and Joos 2017][research_fezans_joos_2017]
- [Fezans et al 2019][research_fezans_joos_2019]
- [Fichera et al 2019][research_fichera_isnardi_2019]
- [Filippou et al 2024][research_filippou_kilimtzidis_2024]
- [Filippou et al 2026][research_filippou_sodja_2026]
- [Finnestead et al 1970][research_finnestead_connor_1970]
- [Fischenberg 1995][research_fischenberg_1995]
- [Fisher et al 1956][research_fisher_gertsen_1956]
- [Fitzgerald et al 1994][research_fitzgerald_ralston_1994]
- [Flexible manufacturing cell for 2003][research_flexible_manufacturing_2003]
- [Flight Envelope 2005][research_flight_envelope_2005]
- [Flight Envelope 2021][research_flight_envelope_2021]
- [Flight Envelope Awareness/Protection][research_flight_envelope]
- [Flight test of a 1979][research_flight_test_1979]
- [Flight test of the F/A-18 active aeroelastic wing airplane][research_aaw_flight_test]
- [Flight test results from a supercritical mission adaptive wing with smooth variable camber][research_mission_adaptive_flight]
- [Flight Testing 1992][research_flight_testing_1992]
- [Flight-Loads Prediction and Structural-Life 1981][research_flight_loads_prediction_1981]
- [Flores and Van Dalsem 1985][research_flores_vandalsem_1985]
- [Floros and Kang 2017][research_floros_kang_2017]
- [Flutter suppression control law synthesis for the active flexible wing model][research_afw_flutter_suppression]
- [Foley and Woodrey 1980][research_foley_woodrey_1980]
- [Fonte and Mantegazza 2017][research_fonte_mantegazza_2017]
- [Fonte et al 2015][research_fonte_ricci_2015]
- [Fonte et al 2018][research_fonte_iannaccone_2018]
- [Fonte et al 2018][research_fonte_toffol_2018]
- [Fonzi et al 2024][research_fonzi_ricci_2024]
- [Fonzi et al 2025][research_fonzi_ricci_2025]
- [Force measurement. Strain gauge][research_force_measurement]
- [Fornasier and Heiss 1987][research_fornasier_heiss_1987]
- [Forsey 1983][research_forsey_1983]
- [Forster et al 1996][research_forster_kolonay_1996]
- [Forster et al 2002][research_forster_sanders_2002]
- [Forte and Nguyen 2024][research_forte_nguyen_2024]
- [Forte and Nguyen 2026][research_forte_nguyen_2026]
- [Forte and Nguyen 2026][research_forte_nguyen_2026_c]
- [Forte and Nguyen 2026][research_forte_nguyen_2026_d]
- [Forte et al 2022][research_forte_nguyen_2022]
- [Forte et al 2023][research_forte_nguyen_2023]
- [Forte et al 2026][research_forte_nguyen_2026_b]
- [Forte et al 2026][research_forte_nguyen_2026_e]
- [Fosdick 1970][research_fosdick_1970]
- [Foster 1966][research_foster_1966]
- [Fournier][research_fournier]
- [Fournier et al 2022][research_fournier_massioni_2022]
- [Frame-wise Control Allocation 2016][research_frame_wise_control_2016]
- [Frampton and Clark 1998][research_frampton_clark_1998]
- [Francisco Peña and Benjamin Park 2024][research_franciscopena_benjaminpark_2024]
- [Franciscus 1983][research_franciscus_1983]
- [Franklin 2018][research_franklin_2018]
- [Franze et al 2013][research_franze_mattei_2013]
- [Freidmann 2001][research_freidmann_2001]
- [French 1988][research_french_1988]
- [French and Eastep 1996][research_french_eastep_1996]
- [Friedmann 1973][research_friedmann_1973]
- [Friedmann 1977][research_friedmann_1977]
- [Friedmann 1987][research_friedmann_1987]
- [Friedmann 1989][research_friedmann_1989]
- [Friedmann 1990][research_friedmann_1990]
- [Friedmann 1992][research_friedmann_1992]
- [Friedmann 1998][research_friedmann_1998]
- [Friedmann 2000][research_friedmann_2000]
- [Friedmann 2001][research_friedmann_2001]
- [Friedmann 2004][research_friedmann_2004]
- [Friedmann 2010][research_friedmann_2010]
- [Friedmann and Hodges 2003][research_friedmann_hodges_2003]
- [Friedmann and Hodges 2003][research_friedmann_hodges_2003_b]
- [Friedmann and Straub 1980][research_friedmann_straub_1980]
- [Friedmann et al 1992][research_friedmann_venkatesan_1992]
- [Frierson and Van Meter 1977][research_frierson_vanmeter_1977]
- [Frierson et al 1978][research_frierson_moore_1978]
- [Frost et al 2012][research_frost_taylor_2012]
- [Frost, Susan A. et al 2015][research_frostsusana_wrightcameronhg_2015]
- [Fruchtman 1974][research_fruchtman_1974]
- [Fuchs 1981][research_fuchs_1981]
- [Fujii and Obayashi 1986][research_fujii_obayashi_1986]
- [Fujimori et al 1989][research_fujimori_ohta_1989]
- [Fujimori et al 1990][research_fujimori_ohta_1990]
- [Fujimori et al 1995][research_fujimori_nikiforuk_1995]
- [Fukumoto et al 2023][research_fukumoto_kouchi_2023]
- [Further development and flight 1994][research_further_development_1994]
- [Gabel et al 1961][research_gabel_ricks_1961]
- [Gade and Inman 1996][research_gade_inman_1996]
- [Gade and Inman 1997][research_gade_inman_1997]
- [Gai and Seffen 2025][research_gai_seffen_2025]
- [Gai and Wang 2013][research_gai_wang_2013]
- [Gai et al 2019][research_gai_sun_2019]
- [Gallagher and Wei 2008][research_gallagher_wei_2008]
- [Galloping and Torsional Divergence 2019][research_galloping_and_2019]
- [Galloway et al 1992][research_galloway_gelhausen_1992]
- [Gally and Carlson 1987][research_gally_carlson_1987]
- [Galway 1980][research_galway_1980]
- [Gamboa and Santos 2016][research_gamboa_santos_2016]
- [Gandhi and Hathaway 1998][research_gandhi_hathaway_1998]
- [Gandhi et al 2009][research_gandhi_cooper_2009]
- [Gangsaas et al 1981][research_gangsaas_ly_1981]
- [Ganguli and Chopra 1995][research_ganguli_chopra_1995]
- [Ganguli and Chopra 1997][research_ganguli_chopra_1997]
- [Gao et al 2021][research_gao_an_2021]
- [Gao et al 2021][research_gao_an_2021_b]
- [Gao et al 2024][research_gao_liu_2024]
- [Garcia 2005][research_garcia_2005]
- [Garcia and Guruswamy 1999][research_garcia_guruswamy_1999]
- [Garcia et al 2003][research_garcia_abdulrahim_2003]
- [Garcia-Velo and Walker 1995][research_garciavelo_walker_1995]
- [Garrard and Liebst 1983][research_garrard_liebst_1983]
- [Garrard and Liebst 1985][research_garrard_liebst_1985]
- [Garrick, I E and Rubinow, S I 1946][research_garrickie_rubinowsi_1946]
- [Garrick, I E and Rubinow, S I 1946][research_garrickie_rubinowsi_1946_b]
- [Garud and Ajluni 2024][research_garud_ajluni_2024]
- [Gasbarri et al 2009][research_gasbarri_chiwiacowsky_2009]
- [Gasparetto][research_gasparetto]
- [Gaspari et al 2009][research_gaspari_ricci_2009]
- [Gautham Vigneswar et al 2025][research_gauthamvigneswar_ali_2025]
- [Gautham Vigneswar et al 2025][research_gauthamvigneswar_ali_2025_b]
- [Geisbauer 2011][research_geisbauer_2011]
- [Generalized predictive control for 1997][research_generalized_predictive_1997]
- [Gennaretti 2024][research_gennaretti_2024]
- [Gennaretti and Ponzi 1999][research_gennaretti_ponzi_1999]
- [Georgiou et al 2012][research_georgiou_manan_2012]
- [Gera et al 1981][research_gera_wilson_1981]
- [Gern 2001][research_gern_2001]
- [Gern and Librescu 1998][research_gern_librescu_1998]
- [Gern and Librescu 2000][research_gern_librescu_2000]
- [Gern et al 2000][research_gern_ko_2000]
- [Ghalandari et al 2022][research_ghalandari_mahariq_2022]
- [Ghee and Taylor 2000][research_ghee_taylor_2000]
- [Ghee and Taylor 2004][research_ghee_taylor_2004]
- [Ghiringhelli et al 1990][research_ghiringhelli_lanz_1990]
- [Ghiringhelli et al 1992][research_ghiringhelli_lanz_1992]
- [Ghorawat et al 2015][research_ghorawat_lee_2015]
- [Ghorawat et al 2016][research_ghorawat_lee_2016]
- [Ghosh and Patil 2022][research_ghosh_patil_2022]
- [Ghosh and Raisinghani 1993][research_ghosh_raisinghani_1993]
- [Ghosh and Raisinghani 1994][research_ghosh_raisinghani_1994]
- [Giansante et al 2022][research_giansante_bernardini_2022]
- [Gibson 1981][research_gibson_1981]
- [Gibson and Ung 1995][research_gibson_ung_1995]
- [Giese et al 1996][research_giese_reich_1996]
- [Giesseler et al 2012][research_giesseler_kopf_2012]
- [Gilbert and Silva 1987][research_gilbert_silva_1987]
- [Gilbert et al 1982][research_gilbert_schmidt_1982]
- [Gilbert et al 1984][research_gilbert_schmidt_1984]
- [Gilbert, Michael G. 1989][research_gilbertmichaelg_1989]
- [Gimmestad 1979][research_gimmestad_1979]
- [Gimmestad 1981][research_gimmestad_1981]
- [Gimmestad 1981][research_gimmestad_1981_b]
- [Giraud et al 2021][research_giraud_raibaudo_2021]
- [Giunta 1999][research_giunta_1999]
- [Gloss and Washburn 1977][research_gloss_washburn_1977]
- [Gloss and Washburn 1978][research_gloss_washburn_1978]
- [Gobal and Grandhi 2015][research_gobal_grandhi_2015]
- [Goizueta et al 2021][research_goizueta_drachinsky_2021]
- [Goizueta et al 2022][research_goizueta_wynn_2022]
- [Goland 1952][research_goland_1952]
- [Gomec et al 2020][research_gomec_unver_2020]
- [Gomec et al 2020][research_gomec_unver_2020_b]
- [Gomillion 1976][research_gomillion_1976]
- [Gonzales et al 2022][research_gonzales_sakaue_2022]
- [Gooch 2011][research_gooch_2011]
- [Gooch 2011][research_gooch_2011_b]
- [Goodman and Conigliaro 1986][research_goodman_conigliaro_1986]
- [Gorbushin et al 2024][research_gorbushin_kozik_2024]
- [Gordnier 1993][research_gordnier_1993]
- [Gordnier and Attar 2012][research_gordnier_attar_2012]
- [Goupil][research_goupil]
- [Gowtham et al 2023][research_gowtham_baashkaran_2023]
- [Graham et al 2007][research_graham_deoliveira_2007]
- [Grant et al 1989][research_grant_nelson_1989]
- [Grantz 1985][research_grantz_1985]
- [Grantz and Marchman 1983][research_grantz_marchman_1983]
- [Grasmeyer 1999][research_grasmeyer_1999]
- [Gratton 2014][research_gratton_2014]
- [Gratton 2018][research_gratton_2018]
- [Grauer 2016][research_grauer_2016]
- [Grauer and Boucher 2017][research_grauer_boucher_2017]
- [Grauer and Morelli 2014][research_grauer_morelli_2014]
- [Grauer and Morelli 2023][research_grauer_morelli_2023]
- [Grauer and Waite 1986][research_grauer_waite_1986]
- [Grauer and Waite 2024][research_grauer_waite_2024]
- [Grauer et al 2012][research_grauer_heeg_2012]
- [Graves et al 2002][research_graves_burner_2002]
- [Gray and Martins 2024][research_gray_martins_2024]
- [Green 1986][research_green_1986]
- [Green 1987][research_green_1987]
- [Green and Fernandez 1994][research_green_fernandez_1994]
- [Greenwell 2004][research_greenwell_2004]
- [Greer et al 2021][research_greer_sardahi_2021]
- [Gregg and Misegades 1987][research_gregg_misegades_1987]
- [Gregory and McCrink 2016][research_gregory_mccrink_2016]
- [Gregory et al 2007][research_gregory_cao_2007]
- [Gregory et al 2011][research_gregory_xargay_2011]
- [Griffin][research_griffin]
- [Griffin 2006][research_griffin_2006]
- [Griffin and Eastep 1981][research_griffin_eastep_1981]
- [Grigorie and Botez 2014][research_grigorie_botez_2014]
- [Grigorie and Botez 2018][research_grigorie_botez_2018]
- [Grigorie et al 2009][research_grigorie_botez_2009]
- [Grigorie et al 2011][research_grigorie_popov_2011]
- [Grismer et al 2000][research_grismer_kinsey_2000]
- [Gross 2002][research_gross_2002]
- [Gross et al 1986][research_gross_chandler_1986]
- [Grosser 1965][research_grosser_1965]
- [Ground and flight testing 2000][research_ground_and_2000]
- [Grove 2006][research_grove_2006]
- [Gu et al 2024][research_gu_healy_2024]
- [Gu et al 2024][research_gu_healy_2024_b]
- [Guan et al 2025][research_guan_xing_2025]
- [Guangming and Zhengfeng 2009][research_guangming_zhengfeng_2009]
- [Guderley 1987][research_guderley_1987]
- [Guderley 1988][research_guderley_1988]
- [Guerreiro and Hubbard 2008][research_guerreiro_hubbard_2008]
- [Guillot and Friedmann 1994][research_guillot_friedmann_1994]
- [Guillot and Friedmann 1994][research_guillot_friedmann_1994_b]
- [Gujjula and Singh 2005][research_gujjula_singh_2005]
- [Gunasekaran and Mukherjee 2016][research_gunasekaran_mukherjee_2016]
- [Guo et al 2018][research_guo_cao_2018]
- [Guo et al 2018][research_guo_shen_2018]
- [Guo et al 2022][research_guo_yan_2022]
- [Gupta 1996][research_gupta_1996]
- [Gupta 2011][research_gupta_2011]
- [Gupta 2012][research_gupta_2012]
- [Gupta 2019][research_gupta_2019]
- [Gupta et al 2005][research_gupta_doyle_2005]
- [Gupta et al 2021][research_gupta_datta_2021]
- [Gupta, K. K. et al 1987][research_guptakk_brennermj_1987]
- [Gupta, K. K. et al 1991][research_guptakk_brennermj_1991]
- [Gurbacki and Bragg 1999][research_gurbacki_bragg_1999]
- [Gurbacki and Bragg 2001][research_gurbacki_bragg_2001]
- [Guruswamy 1992][research_guruswamy_1992]
- [Guruswamy 2019][research_guruswamy_2019]
- [Guruswamy and Tu 1989][research_guruswamy_tu_1989]
- [Guruswamy and Tu 1994][research_guruswamy_tu_1994]
- [Gutierrez et al 1994][research_gutierrez_tate_1994]
- [Gwin 1974][research_gwin_1974]
- [Gwin 1976][research_gwin_1976]
- [Haas and Chopra 1987][research_haas_chopra_1987]
- [Haas and Chopra 1988][research_haas_chopra_1988]
- [Haas and Chopra 1989][research_haas_chopra_1989]
- [Haas and Chopra 1990][research_haas_chopra_1990]
- [Hablowetz 2000][research_hablowetz_2000]
- [Haddadpour 2006][research_haddadpour_2006]
- [Haddadpour et al 2005][research_haddadpour_shams_2005]
- [Haghighat et al 2010][research_haghighat_liu_2010]
- [Haghighat et al 2012][research_haghighat_liu_2012]
- [Haghighat et al 2012][research_haghighat_martins_2012]
- [Hahn and Haupt 2022][research_hahn_haupt_2022]
- [Haider et al 2022][research_haider_ajaj_2022]
- [Haider et al 2023][research_haider_ajaj_2023]
- [Hajj 2004][research_hajj_2004]
- [Halder and Benedict 2018][research_halder_benedict_2018]
- [Hale and Chapman 2012][research_hale_chapman_2012]
- [Haley and Soloway 2001][research_haley_soloway_2001]
- [Haley and Soloway 2022][research_haley_soloway_2022]
- [Hall and Mason 2012][research_hall_mason_2012]
- [Halwas and Aggarwal 2019][research_halwas_aggarwal_2019]
- [Halwas and Aggarwal 2019][research_halwas_aggarwal_2019_b]
- [Ham et al 1994][research_ham_kim_1994]
- [Hammer and Garmann 2023][research_hammer_garmann_2023]
- [Hammerton et al 2018][research_hammerton_su_2018]
- [Han and Kim 2011][research_han_kim_2011]
- [Hanafee and Radcliffe 1967][research_hanafee_radcliffe_1967]
- [Hancock 1961][research_hancock_1961]
- [Hancock 1963][research_hancock_1963]
- [Hancock 1965][research_hancock_1965]
- [Handojo et al 2018][research_handojo_lancelot_2018]
- [Hanel 1998][research_hanel_1998]
- [Haney et al 1978][research_haney_waggoner_1978]
- [Haney et al 1979][research_haney_johnson_1979]
- [Hansen et al 2020][research_hansen_duan_2020]
- [Hansen et al 2020][research_hansen_duan_2020_b]
- [Hansen et al 2022][research_hansen_duan_2022]
- [Hanson et al 2002][research_hanson_ryan_2002]
- [Harash et al 2012][research_harash_yadykin_2012]
- [Harkegard][research_harkegard]
- [Harper and Robert P. 1955][research_harper_robertp_1955]
- [Harris et al 2016][research_harris_arthurs_2016]
- [Harry and Trobaugh 1966][research_harry_trobaugh_1966]
- [Hartman 2019][research_hartman_2019]
- [Hartmann 2012][research_hartmann_2012]
- [Hartmann 2013][research_hartmann_2013]
- [Hartwell and Nguyen 2021][research_hartwell_nguyen_2021]
- [Harvey 1983][research_harvey_1983]
- [Hashemi and Nguyen 2018][research_hashemi_nguyen_2018_b]
- [Hashemi et al 2018][research_hashemi_nguyen_2018]
- [Hatami-Marbini 2018][research_hatamimarbini_2018]
- [Hatamleh et al 2009][research_hatamleh_ma_2009]
- [Haucke et al 2016][research_haucke_bauer_2016]
- [Hayabe and Kwak 2025][research_hayabe_kwak_2025]
- [Hayashi and Ueda 2017][research_hayashi_ueda_2017]
- [He et al 2020][research_he_deparday_2020]
- [He et al 2020][research_he_song_2020]
- [He et al 2021][research_he_wang_2021]
- [He et al 2022][research_he_wang_2022]
- [He et al 2023][research_he_wang_2023]
- [He et al 2024][research_he_shi_2024]
- [Heaney and Quindlen 2024][research_heaney_quindlen_2024]
- [Heeg 2006][research_heeg_2006]
- [Heeg et al 2005][research_heeg_spain_2005]
- [Held and Fuchs 1999][research_held_fuchs_1999]
- [Helicopter Flight Parameter Identification 1987][research_helicopter_flight_1987]
- [Helmken et al 1996][research_helmken_emmons_1996]
- [Heltsley and Cline 1979][research_heltsley_cline_1979]
- [Heltsley et al 1981][research_heltsley_crosswy_1981]
- [Henderson and Lavretsky 1999][research_henderson_lavretsky_1999]
- [Hendrickson et al 1978][research_hendrickson_grossman_1978]
- [Henne 1980][research_henne_1980]
- [Henne and Hicks 1978][research_henne_hicks_1978]
- [Henry et al 2017][research_henry_molinari_2017]
- [Herbert][research_herbert]
- [Herencia et al 2007][research_herencia_weaver_2007]
- [Herrmann][research_herrmann]
- [Herrmann and Nemat-Nasser 1966][research_herrmann_nematnasser_1966]
- [Hess 1986][research_hess_1986]
- [Hess and Flick 2004][research_hess_flick_2004]
- [Hess and Hess 1997][research_hess_hess_1997]
- [Hicks and Jenkins 1990][research_hicks_jenkins_1990]
- [High-Load Strain Gauge Balance 2018][research_high_load_strain_2018]
- [Hildebrand et al 2003][research_hildebrand_eidson_2003]
- [Hiley and Bowers 1981][research_hiley_bowers_1981]
- [Hilger and Ritter 2021][research_hilger_ritter_2021]
- [Hillebrand and Lutz 2026][research_hillebrand_lutz_2026]
- [Hillebrand et al 2024][research_hillebrand_breitenstein_2024]
- [Hillebrand et al 2026][research_hillebrand_breitenstein_2026]
- [Hilton and Nguyen 2014][research_hilton_nguyen_2014]
- [Hinz and Miller 1979][research_hinz_miller_1979]
- [History of Supersonic Transport 2020][research_history_of_2020]
- [Hitch 1978][research_hitch_1978]
- [Hiti 2017][research_hiti_2017]
- [Hjartarson et al 2013][research_hjartarson_seiler_2013]
- [Hjartarson et al 2014][research_hjartarson_seiler_2014]
- [Hoadley and McGraw 1995][research_hoadley_mcgraw_1995]
- [Hodapp, Jr. and Beckmann 1972][research_hodappjr_beckmann_1972]
- [Hodges 1973][research_hodges_1973]
- [Hodges 2007][research_hodges_2007]
- [Hodges and Mckenzie 1975][research_hodges_mckenzie_1975]
- [Hodson et al 1993][research_hodson_dobbs_1993]
- [Hoffmann et al 2011][research_hoffmann_loftfield_2011]
- [Hofmann and Kezer 1962][research_hofmann_kezer_1962]
- [Hofmann et al 2025][research_hofmann_hosseini_2025]
- [Hoh and Mitchell 2018][research_hoh_mitchell_2018]
- [Holberg and Grabowsky 1981][research_holberg_grabowsky_1981]
- [Hollis et al 1999][research_hollis_brandon_1999]
- [Holman and Tuozzolo 2009][research_holman_tuozzolo_2009]
- [Holst and Thomas 1982][research_holst_thomas_1982]
- [Hongchao Li et al][research_hongchaoli_zhongkeshi]
- [Hope and Kunz 2019][research_hope_kunz_2019]
- [Hopkins, E. J. and Lovette, G. H. 1977][research_hopkinsej_lovettegh_1977]
- [Hopwood et al 2019][research_hopwood_ruskin_2019]
- [Horn et al 1998][research_horn_calise_1998]
- [Horton 1943][research_horton_1943]
- [Hoseini and Hodges 2019][research_hoseini_hodges_2019]
- [Hosseini et al 2025][research_hosseini_hofmann_2025]
- [Hou and Satyanarayana 2000][research_hou_satyanarayana_2000]
- [Hoult and Beyer 2020][research_hoult_beyer_2020]
- [How to Model Post-Cracking 2020][research_how_to_2020]
- [Howell 1988][research_howell_1988]
- [Hu][research_hu]
- [Hu 1995][research_hu_1995]
- [Hu et al 2009][research_hu_qu_2009]
- [Hu et al 2023][research_hu_shao_2023]
- [Hu et al 2024][research_hu_yu_2024]
- [Hu et al 2025][research_hu_dai_2025]
- [Hu et al 2026][research_hu_traisnel_2026]
- [Hua et al 2025][research_hua_wang_2025]
- [Huang et al 2015][research_huang_qian_2015]
- [Huang et al 2024][research_huang_wang_2024]
- [Huang et al 2024][research_huang_zhang_2024]
- [Huang et al 2025][research_huang_fraihat_2025]
- [Huber 1995][research_huber_1995]
- [Huebner and Reimer 2019][research_huebner_reimer_2019]
- [Huffman and Fox, Jr. 1985][research_huffman_foxjr_1985]
- [Hughes and Wernicke 1974][research_hughes_wernicke_1974]
- [Hui et al 2000][research_hui_collins_2000]
- [Hui et al 2005][research_hui_auriti_2005]
- [Humbad 1978][research_humbad_1978]
- [Hunn 1953][research_hunn_1953]
- [Huo et al 2013][research_huo_wang_2013]
- [Huo et al 2013][research_huo_yuan_2013]
- [Hur and Valasek 2003][research_hur_valasek_2003]
- [hussain and Khan 2019][research_hussain_khan_2019]
- [Hussein et al 2025][research_hussein_rashid_2025]
- [Hutto 1975][research_hutto_1975]
- [Huttsell and Eastep 1989][research_huttsell_eastep_1989]
- [Hwang and Pi 1982][research_hwang_pi_1982]
- [Hwang et al 1991][research_hwang_chen_1991]
- [Hwu and Tsai 2002][research_hwu_tsai_2002]
- [Hybrid Approach to Transonic 1982][research_hybrid_approach_1982]
- [Iaconis and D'Emilia 1994][research_iaconis_demilia_1994]
- [Iannacci and Mayo 1999][research_iannacci_mayo_1999]
- [Iannuzzo et al 2018][research_iannuzzo_russo_2018]
- [Ibrahim and Castravete 2005][research_ibrahim_castravete_2005]
- [Ibren et al 2020][research_ibren_sulaeman_2020]
- [Idan et al 1999][research_idan_karpel_1999]
- [Ide and Ominsky 1990][research_ide_ominsky_1990]
- [Ide and Shankar 1987][research_ide_shankar_1987]
- [Ide et al 2019][research_ide_ishida_2019]
- [Idsardi 1983][research_idsardi_1983]
- [Ifju et al 2001][research_ifju_waszak_2001]
- [Ilie and Havenar 2023][research_ilie_havenar_2023]
- [Iliff and Maine 1983][research_iliff_maine_1983]
- [In-flight deflection measurement of the HiMAT aeroelastically tailored wing][research_himat_deflection]
- [Incorporating agility flight test 1994][research_incorporating_agility_1994]
- [Ingle and Kothmann 1998][research_ingle_kothmann_1998]
- [Initial flight test of 1989][research_initial_flight_1989]
- [Innocenti 1985][research_innocenti_1985]
- [International Standard Atmosphere 2010][research_international_standard_2010]
- [Introduction to Aeroelastic Rotor 2018][research_introduction_to_2018]
- [Introduction to Stability and 2003][research_introduction_to_2003]
- [Investigations of Static Aeroelasticity 2016][research_investigations_of_static_2016]
- [Ionela Raluca Maxim 1970][research_ionelaralucamaxim_1970]
- [Ippolito et al 2014][research_ippolito_ting_2014]
- [Irfan et al 2026][research_irfan_nanangburhan_2026]
- [Iriarte et al 2021][research_iriarte_aginaga_2021]
- [Ishihara and Nguyen 2014][research_ishihara_nguyen_2014]
- [Ishihara et al 2013][research_ishihara_nguyen_2013]
- [Ishii 1965][research_ishii_1965]
- [Ishii et al 2005][research_ishii_gomi_2005]
- [Islam et al 2018][research_islam_martin_2018]
- [Islam et al 2025][research_islam_rahman_2025]
- [Islam et al 2025][research_islam_rahman_2025_b]
- [Islam et al 2026][research_islam_rahman_2026]
- [Isnardi et al 2018][research_isnardi_paoletti_2018]
- [Isogai 1988][research_isogai_1988]
- [Isogai 1989][research_isogai_1989]
- [Israq et al 2025][research_israq_ahmaad_2025]
- [Iyer et al 2017][research_iyer_park_2017]
- [Izadi et al 2007][research_izadi_pakmehr_2007]
- [Izadpanahi][research_izadpanahi]
- [Ize and Arena 1998][research_ize_arena_1998]
- [Ize and Arena, Jr. 1999][research_ize_arenajr_1999]
- [Ize et al 1997][research_ize_arenajr_1997]
- [J and J 2015][research_j_j_2015]
- [Jabbar et al 2026][research_jabbar_setiawan_2026]
- [Jackson and Livne 2005][research_jackson_livne_2005]
- [Jackson and Livne 2014][research_jackson_livne_2014]
- [Jacobs, P. F. 1983][research_jacobspf_1983]
- [Jafari et al 2019][research_jafari_feizarefi_2019]
- [Jain 2014][research_jain_2014]
- [Jain et al 2025][research_jain_singla_2025]
- [Jameson 1973][research_jameson_1973]
- [Jameson 1977][research_jameson_1977]
- [Jameson 1982][research_jameson_1982]
- [Jameson 2003][research_jameson_2003]
- [Jameson and Caughey 1977][research_jameson_caughey_1977]
- [Jamshidi et al 2016][research_jamshidi_dardel_2016]
- [Janardhan and Grandhi 2003][research_janardhan_grandhi_2003]
- [Jategaonkar et al 2004][research_jategaonkar_fischenberg_2004]
- [Jaworski 2012][research_jaworski_2012]
- [Jebakumar et al 2019][research_jebakumar_kumar_2019]
- [Jenkins et al 1977][research_jenkins_kuhl_1977]
- [Jenkins, Jerald M. and Kuhl, Albert E. 1977][research_jenkinsjeraldm_kuhlalberte_1977]
- [Jenney et al 1982][research_jenney_schreadley_1982]
- [Jeong et al 2013][research_jeong_lee_2013]
- [Jepps 1981][research_jepps_1981]
- [Jha and Chattopadhyay 1999][research_jha_chattopadhyay_1999]
- [Jia et al 2022][research_jia_zhang_2022]
- [Jia et al 2023][research_jia_zhang_2023]
- [Jian and Jinwu 2009][research_jian_jinwu_2009]
- [Jiang 1999][research_jiang_1999]
- [Jiang and Li 2018][research_jiang_li_2018]
- [Jiang and Li 2018][research_jiang_li_2018_b]
- [Jiang and Yang 2026][research_jiang_yang_2026]
- [Jiang et al 2000][research_jiang_an_2000]
- [Jiang et al 2019][research_jiang_tian_2019]
- [Jianjun Ma et al 2008][research_jianjunma_pengli_2008]
- [Jianjun Ma et al 2008][research_jianjunma_wenqiangli_2008]
- [Jin et al 2013][research_jin_song_2013]
- [Jing and Ma 2025][research_jing_ma_2025]
- [Jing and Zhang 2017][research_jing_zhang_2017]
- [Jingping et al 2011][research_jingping_weiguo_2011]
- [Jini Raj et al 2023][research_jiniraj_bruceralphinrose_2023]
- [Jo and Majid 2023][research_jo_majid_2023]
- [Jodin et al 2017][research_jodin_scheller_2017]
- [John F Quindlen et al][research_johnfquindlen_danielmortega]
- [Johns 1964][research_johns_1964]
- [Johnson 1980][research_johnson_1980]
- [Johnson, C. B. and Kaufman, L. G., III 1979][research_johnsoncb_kaufmanlgiii_1979]
- [Johnston 1998][research_johnston_1998]
- [Johnston and Cassarino 1976][research_johnston_cassarino_1976]
- [Johnston, J. F. 1979][research_johnstonjf_1979]
- [Jones 1950][research_jones_1950]
- [Jones 1976][research_jones_1976]
- [Jones 1980][research_jones_1980]
- [Jones and Jarrett 2018][research_jones_jarrett_2018]
- [Joo et al 2015][research_joo_marks_2015]
- [Jorge and Lind 2013][research_jorge_lind_2013]
- [Jovanov and De Breuker 2015][research_jovanov_debreuker_2015]
- [Juliana et al 2004][research_juliana_chu_2004]
- [Jun et al 2014][research_jun_harmin_2014]
- [Jurisson et al 2022][research_jurisson_debreuker_2022]
- [Jutte, Christine and Stanford, Bret K. 2014][research_juttechristine_stanfordbretk_2014]
- [K. Badri and Torabpour 2025][research_kbadri_torabpour_2025]
- [K. Badri and Torabpour 2026][research_kbadri_torabpour_2026]
- [Kadrnka and Hawley 1993][research_kadrnka_hawley_1993]
- [Kady and Takahashi 2014][research_kady_takahashi_2014]
- [Kafkas and Lampeas 2020][research_kafkas_lampeas_2020]
- [Kafkas et al 2021][research_kafkas_kilimtzidis_2021]
- [Kai et al 2020][research_kai_sugiura_2020]
- [Kalaji 2023][research_kalaji_2023]
- [Kaletka and Fu 1993][research_kaletka_fu_1993]
- [Kandil and Menzies 1996][research_kandil_menzies_1996]
- [Kandil et al 1993][research_kandil_kandil_1993]
- [Kandil et al 1994][research_kandil_kalisch_1994]
- [Kang et al 2023][research_kang_meng_2023]
- [Kang et al 2023][research_kang_zhao_2023]
- [Kannemans 1995][research_kannemans_1995]
- [Kapania and Chun 2003][research_kapania_chun_2003]
- [Kapase et al 2026][research_kapase_joshi_2026]
- [Karania et al 2021][research_karania_mohan_2021]
- [Karathanasopoulos 2015][research_karathanasopoulos_2015]
- [Karpel 1982][research_karpel_1982]
- [Karpel 1989][research_karpel_1989]
- [Karpel 1990][research_karpel_1990]
- [Karpel 1990][research_karpel_1990_b]
- [Karpel and Sheena 1989][research_karpel_sheena_1989]
- [Karpel et al 1998][research_karpel_idan_1998]
- [Karpel et al 2000][research_karpel_moulin_2000]
- [Karpouzian 1991][research_karpouzian_1991]
- [Karpouzian and Librescu 1991][research_karpouzian_librescu_1991]
- [Karpouzian and Librescu 1992][research_karpouzian_librescu_1992]
- [Karpouzian and Librescu 1994][research_karpouzian_librescu_1994]
- [Kassapakis and Warwick 1994][research_kassapakis_warwick_1994]
- [Katagiri et al 2024][research_katagiri_park_2024]
- [Katam et al 2005][research_katam_lebeau_2005]
- [Kaufman et al 1996][research_kaufman_balabanov_1996]
- [Kaushik 2018][research_kaushik_2018]
- [Kawakami et al 2007][research_kawakami_takatoya_2007]
- [Kawakami et al 2008][research_kawakami_takatoya_2008]
- [Kaygan and Ulusoy 2018][research_kaygan_ulusoy_2018]
- [Kayran 2004][research_kayran_2004]
- [Kayran 2007][research_kayran_2007]
- [Kaza and Kielb 1982][research_kaza_kielb_1982]
- [Ke et al 2008][research_ke_zhigang_2008]
- [Keas and MacMynowski 2009][research_keas_macmynowski_2009]
- [Keener 1984][research_keener_1984]
- [Kefayat and Kamali 2024][research_kefayat_kamali_2024]
- [Kehoe 1988][research_kehoe_1988]
- [Kehrer 1971][research_kehrer_1971]
- [Keidel et al 2019][research_keidel_molinari_2019]
- [Keidel et al 2020][research_keidel_lienhard_2020]
- [Kelly 1974][research_kelly_1974]
- [Kelly 1988][research_kelly_1988]
- [Kennedy and Martins 2013][research_kennedy_martins_2013]
- [Keçecioğlu and Salih Yiğit 2026][research_kececioglu_salihyigit_2026]
- [Khaddage][research_khaddage]
- [Khalil and Bauknecht 2024][research_khalil_bauknecht_2024]
- [Khalil and Fezans 2019][research_khalil_fezans_2019]
- [Khalil and Fezans 2019][research_khalil_fezans_2019_b]
- [Khalil and Fezans 2020][research_khalil_fezans_2020]
- [Khalil et al 2020][research_khalil_asaro_2020]
- [Khalil et al 2022][research_khalil_asaro_2022]
- [Kheiri and Riazat 2025][research_kheiri_riazat_2025]
- [Kholodar 2014][research_kholodar_2014]
- [Kholodar 2016][research_kholodar_2016]
- [Khot 1999][research_khot_1999]
- [Khot et al 1997][research_khot_eastep_1997]
- [Khot et al 1998][research_khot_appa_1998]
- [Khot et al 1998][research_khot_appa_1998_b]
- [Khot et al 2000][research_khot_appa_2000]
- [Khot et al 2000][research_khot_zweber_2000]
- [Khot et al 2002][research_khot_zweber_2002]
- [Khrabrov and Sidoryuk 2010][research_khrabrov_sidoryuk_2010]
- [Khrabrov and Sidoryuk 2013][research_khrabrov_sidoryuk_2013]
- [Kilimtzidis and Kostopoulos 2023][research_kilimtzidis_kostopoulos_2023]
- [Kim 2004][research_kim_2004]
- [Kim and Crassidis 2003][research_kim_crassidis_2003]
- [Kim and Song 2013][research_kim_song_2013]
- [Kim and Sung 1993][research_kim_sung_1993]
- [Kim and Winchenbach 1986][research_kim_winchenbach_1986]
- [Kim et al 2001][research_kim_obayashi_2001]
- [Kim et al 2006][research_kim_jeon_2006]
- [Kim et al 2007][research_kim_kim_2007]
- [Kim et al 2013][research_kim_ahn_2013]
- [Kim et al 2023][research_kim_sung_2023]
- [Kimaru and Bouferrouk 2017][research_kimaru_bouferrouk_2017]
- [Kimler and Canfield 2006][research_kimler_canfield_2006]
- [King 1944][research_king_1944]
- [Kirsch et al 2020][research_kirsch_montagnier_2020]
- [Kishi et al 2016][research_kishi_kanazaki_2016]
- [Kisslinger and Vetsch 1965][research_kisslinger_vetsch_1965]
- [Klabes et al 2018][research_klabes_callsen_2018]
- [Klaue and Seidel 2009][research_klaue_seidel_2009]
- [Klausmeyer 2018][research_klausmeyer_2018]
- [Klepl 1990][research_klepl_1990]
- [Klepl 1995][research_klepl_1995]
- [Klim et al 2013][research_klim_zeppetelli_2013]
- [Klimek 2024][research_klimek_2024]
- [Klopfer and Nielsen 1980][research_klopfer_nielsen_1980]
- [Klug et al 2020][research_klug_radespiel_2020]
- [Klug et al 2023][research_klug_ullah_2023]
- [Klyde et al 2007][research_klyde_bachelder_2007]
- [Knighton 1992][research_knighton_1992]
- [Ko et al 2003][research_ko_mason_2003]
- [Kobow et al 2026][research_kobow_wennemann_2026]
- [Kobusch and Eichstädt 2017][research_kobusch_eichstadt_2017]
- [Koeniguer and Spear 2018][research_koeniguer_spear_2018]
- [Kojima et al 2019][research_kojima_kameda_2019]
- [Kokolios 1994][research_kokolios_1994]
- [Kolesar 1971][research_kolesar_1971]
- [Kolesar et al 1970][research_kolesar_kassianides_1970]
- [Kolesar et al 1970][research_kolesar_kassianides_1970_b]
- [Kolonay and Yang 1998][research_kolonay_yang_1998]
- [Koo 2001][research_koo_2001]
- [Koo and Lee 1994][research_koo_lee_1994]
- [Koohi et al 2014][research_koohi_shahverdi_2014]
- [Kopf et al 2015][research_kopf_giesseler_2015]
- [Kopf et al 2018][research_kopf_bullinger_2018]
- [Kopsaftopoulos et al 2015][research_kopsaftopoulos_nardari_2015]
- [Kordt et al 2002][research_kordt_ballauf_2002]
- [Koreanschi et al 2014][research_koreanschi_oliviu_2014]
- [Koreanschi et al 2015][research_koreanschi_oliviu_2015]
- [Koreanschi et al 2016][research_koreanschi_oliviu_2016]
- [Kosmatka and Panza 2002][research_kosmatka_panza_2002]
- [Kotikalpudi et al 2016][research_kotikalpudi_pfifer_2016]
- [Kotikalpudi et al 2018][research_kotikalpudi_danowsky_2018]
- [Koven, William and Kayten, Gerald G. 1946][research_kovenwilliam_kaytengeraldg_1946]
- [Kowalska and Goetzendorf-Grabowski 2022][research_kowalska_goetzendorfgrabowski_2022]
- [Krasuski and Bakuła 2021][research_krasuski_bakua_2021]
- [Kratochvíl and Valenta 2024][research_kratochvil_valenta_2024]
- [Krengel 2024][research_krengel_2024]
- [Krengel and Hepperle 2022][research_krengel_hepperle_2022]
- [Krengel and Hepperle 2023][research_krengel_hepperle_2023]
- [Krenz 1979][research_krenz_1979]
- [Kreshock et al 2016][research_kreshock_kang_2016]
- [Kreshock et al 2018][research_kreshock_yeo_2018]
- [Krings et al 2013][research_krings_henning_2013]
- [Kroeger, R. A. 1977][research_kroegerra_1977]
- [Krüger et al 2022][research_kruger_meddaikar_2022]
- [Kubica and Livet 1994][research_kubica_livet_1994]
- [Kubica and Livet 1994][research_kubica_livet_1994_b]
- [Kubica et al 1995][research_kubica_livet_1995]
- [Kuder et al 2014][research_kuder_arrieta_2014]
- [Kuhlman et al 1988][research_kuhlman_cerney_1988]
- [Kukreja 2009][research_kukreja_2009]
- [Kukreja and Brenner][research_kukreja_brenner]
- [Kukreja, Sunil L. 2007][research_kukrejasunill_2007]
- [Kulfan and Vachal 1978][research_kulfan_vachal_1978]
- [Kulhánek 2019][research_kulhanek_2019]
- [Kumar and Ghosh 2017][research_kumar_ghosh_2017]
- [Kumar and Ghosh 2023][research_kumar_ghosh_2023]
- [Kumar et al 2008][research_kumar_ganguli_2008]
- [Kumar et al 2021][research_kumar_sunil_2021]
- [Kuo and Hsu 1997][research_kuo_hsu_1997]
- [Kuppuswamy and Kiran 1981][research_kuppuswamy_kiran_1981]
- [Kurade et al 2021][research_kurade_venkatakrishnan_2021]
- [Kurita et al 2019][research_kurita_koike_2019]
- [Kurzke and Halliwell 2018][research_kurzke_halliwell_2018]
- [Kurzke et al 2025][research_kurzke_halliwell_2025]
- [Kutluay et al 2009][research_kutluay_mahmutyazicioglu_2009]
- [Kuttenkeuler and Ringertz 1998][research_kuttenkeuler_ringertz_1998]
- [Kwak et al 2004][research_kwak_shirotake_2004]
- [Kwon et al 2026][research_kwon_chang_2026]
- [Kwong et al 2024][research_kwong_severson_2024]
- [Küssner 1959][research_kussner_1959]
- [Laban and Masui 1993][research_laban_masui_1993]
- [Lai et al 2014][research_lai_zhang_2014]
- [Lai et al 2016][research_lai_lu_2016]
- [Lam et al 2024][research_lam_paranjape_2024]
- [Lambert and Gursul 2001][research_lambert_gursul_2001]
- [Lamour 2014][research_lamour_2014]
- [Lamy 1983][research_lamy_1983]
- [Lan et al 2006][research_lan_bianchi_2006]
- [Landers and Landrum 1998][research_landers_landrum_1998]
- [Landers et al 1997][research_landers_landrum_1997]
- [Lang 1981][research_lang_1981]
- [Lanjun Li et al 2006][research_lanjunli_shouyiyu_2006]
- [Large et al 1981][research_large_may_1981]
- [Larson 1958][research_larson_1958]
- [Larson 1986][research_larson_1986]
- [Larsson 2019][research_larsson_2019]
- [Lateral-Directional Stability Theory and 2003][research_lateral_directional_stability_2003]
- [Lauchle 1974][research_lauchle_1974]
- [Laughrey 1969][research_laughrey_1969]
- [Laurie and Farokhi 1993][research_laurie_farokhi_1993]
- [Layton 1986][research_layton_1986]
- [Layton 1995][research_layton_1995]
- [Layton 1996][research_layton_1996]
- [Lazarus et al 1991][research_lazarus_crawley_1991]
- [Lazarus et al 1995][research_lazarus_crawley_1995]
- [Leal et al 2017][research_leal_petterson_2017]
- [Leal et al 2018][research_leal_stroud_2018]
- [Leal et al 2018][research_leal_white_2018]
- [Leble and Barakos 2016][research_leble_barakos_2016]
- [Lebofsky et al 2015][research_lebofsky_ting_2015]
- [Lebofsky et al 2015][research_lebofsky_ting_2015_b]
- [Lee 1994][research_lee_1994]
- [Lee and Aldredge 2015][research_lee_aldredge_2015]
- [Lee and Boedicker 1985][research_lee_boedicker_1985]
- [Lee and Kim 1995][research_lee_kim_1995]
- [Lee and Singh 2006][research_lee_singh_2006]
- [Lee and Singh 2009][research_lee_singh_2009]
- [Lee and Singh 2014][research_lee_singh_2014]
- [Lee and Singh 2018][research_lee_singh_2018]
- [Lee et al 1993][research_lee_valerio_1993]
- [Lee et al 1994][research_lee_kim_1994]
- [Lee et al 2018][research_lee_hashemi_2018]
- [Lee-Rausch and Batina 1993][research_leerausch_batina_1993]
- [Lei and Kwak 2005][research_lei_kwak_2005]
- [Lei et al 2020][research_lei_wang_2020]
- [Leijonhufvud and Karlsson 2011][research_leijonhufvud_karlsson_2011]
- [Leitch et al 2024][research_leitch_stodieck_2024]
- [Leitch et al 2025][research_leitch_stodieck_2025]
- [Lekou and Mouzakis 2009][research_lekou_mouzakis_2009]
- [Lesoinne 2007][research_lesoinne_2007]
- [Lesoinne and Farhat 1993][research_lesoinne_farhat_1993]
- [Lesoinne and Farhat 1995][research_lesoinne_farhat_1995]
- [Lesoinne and Kaila 2005][research_lesoinne_kaila_2005]
- [Lesoinne et al 2001][research_lesoinne_balas_2001]
- [Levchenko 1987][research_levchenko_1987]
- [Level Flight Performance Flight 2003][research_level_flight_2003]
- [Leventhal et al 1977][research_leventhal_keel_1977]
- [Levinski 2004][research_levinski_2004]
- [Levinsky and Palko 1978][research_levinsky_palko_1978]
- [Levy 1992][research_levy_1992]
- [Lewis et al 1979][research_lewis_platt_1979]
- [Lhachemi et al 2017][research_lhachemi_chu_2017]
- [Lhachemi et al 2017][research_lhachemi_saussie_2017]
- [Li 2018][research_li_2018]
- [Li and Ang 2016][research_li_ang_2016]
- [Li and Fleeter 1996][research_li_fleeter_1996]
- [Li and Geiselhart 2026][research_li_geiselhart_2026]
- [Li and Li 2016][research_li_li_2016]
- [Li and Livne 1995][research_li_livne_1995]
- [Li and Livne 1997][research_li_livne_1997]
- [Li and Qin 2020][research_li_qin_2020]
- [Li and Qin 2020][research_li_qin_2020_b]
- [Li and Qin 2021][research_li_qin_2021]
- [Li and Qin 2021][research_li_qin_2021_b]
- [Li and Qin 2022][research_li_qin_2022]
- [Li and Xia 2017][research_li_xia_2017]
- [Li and Xia 2018][research_li_xia_2018]
- [Li et al 1999][research_li_zhu_1999]
- [Li et al 2009][research_li_dong_2009]
- [Li et al 2010][research_li_guo_2010]
- [Li et al 2010][research_li_guo_2010_b]
- [Li et al 2011][research_li_yu_2011]
- [Li et al 2012][research_li_yu_2012]
- [Li et al 2014][research_li_zhang_2014]
- [Li et al 2017][research_li_zhao_2017]
- [Li et al 2018][research_li_huang_2018]
- [Li et al 2019][research_li_zhang_2019]
- [Li et al 2020][research_li_yang_2020]
- [Li et al 2021][research_li_wan_2021]
- [Li et al 2021][research_li_wang_2021]
- [Li et al 2022][research_li_ge_2022]
- [Li et al 2023][research_li_luo_2023]
- [Li et al 2024][research_li_dai_2024]
- [Li et al 2024][research_li_kou_2024]
- [Li et al 2024][research_li_qian_2024]
- [Li et al 2024][research_li_zhang_2024]
- [Li et al 2024][research_li_zhiqiang_2024]
- [Li et al 2025][research_li_dai_2025]
- [Li et al 2025][research_li_gong_2025]
- [Li et al 2025][research_li_li_2025]
- [Li et al 2025][research_li_wang_2025]
- [Li et al 2025][research_li_xiong_2025]
- [Li et al 2025][research_li_zheng_2025]
- [Li et al 2026][research_li_zhang_2026]
- [Liang and Qin 2012][research_liang_qin_2012]
- [Liang et al 2025][research_liang_chen_2025]
- [Liang et al 2026][research_liang_chen_2026]
- [Liao et al 2026][research_liao_zhang_2026]
- [Librescu and Beiner 1983][research_librescu_beiner_1983]
- [Librescu and Simovich 1988][research_librescu_simovich_1988]
- [Librescu and Song 1992][research_librescu_song_1992]
- [Librescu and Thangjitham 1989][research_librescu_thangjitham_1989]
- [Librescu and Thangjitham 1991][research_librescu_thangjitham_1991]
- [Librescu et al 2003][research_librescu_na_2003]
- [Lichtenwalner et al 1996][research_lichtenwalner_little_1996]
- [Lieberman 1963][research_lieberman_1963]
- [Liebst 1987][research_liebst_1987]
- [Liebst et al 1986][research_liebst_garrard_1986]
- [Liebst et al 1986][research_liebst_garrard_1986_b]
- [Liebst et al 1988][research_liebst_garrard_1988]
- [Lim et al 2000][research_lim_sreenatha_2000]
- [Limitations and Flight Envelope 2017][research_limitations_and_2017]
- [Lin 1982][research_lin_1982]
- [Lin 1983][research_lin_1983]
- [Lin 2016][research_lin_2016]
- [Lin and Crawley 1994][research_lin_crawley_1994]
- [Lin et al 1995][research_lin_crawley_1995]
- [Lin et al 1996][research_lin_crawley_1996]
- [Lin et al 2019][research_lin_zhang_2019]
- [Lind 1999][research_lind_1999]
- [Lind and Brenner 1997][research_lind_brenner_1997_b]
- [Lind and Brenner 1998][research_lind_brenner_1998]
- [Lind and Brenner 1999][research_lind_brenner_1999]
- [Lind and Brenner 1999][research_lind_brenner_1999_b]
- [Lind and Brenner 1999][research_lind_brenner_1999_c]
- [Lind and Brenner 1999][research_lind_brenner_1999_d]
- [Lind and Brenner 1999][research_lind_brenner_1999_e]
- [Lind and Brenner 1999][research_lind_brenner_1999_f]
- [Lind et al 1997][research_lind_brenner_1997]
- [Lind et al 1998][research_lind_freudinger_1998]
- [Lindsley 2007][research_lindsley_2007]
- [Lindsley 2009][research_lindsley_2009]
- [Lingyu et al 2006][research_lingyu_youwu_2006]
- [Little 1996][research_little_1996]
- [Liu 2019][research_liu_2019]
- [Liu 2022][research_liu_2022]
- [Liu 2022][research_liu_2022_b]
- [Liu and Gong 2021][research_liu_gong_2021]
- [Liu and Sun 2016][research_liu_sun_2016]
- [Liu and Sun 2017][research_liu_sun_2017]
- [Liu and Zhang 2020][research_liu_zhang_2020]
- [Liu et al 2009][research_liu_sun_2009]
- [Liu et al 2011][research_liu_yin_2011]
- [Liu et al 2013][research_liu_bai_2013]
- [Liu et al 2013][research_liu_zhu_2013]
- [Liu et al 2015][research_liu_zhou_2015]
- [Liu et al 2017][research_liu_sun_2017_b]
- [Liu et al 2018][research_liu_dong_2018]
- [Liu et al 2018][research_liu_zhang_2018]
- [Liu et al 2020][research_liu_gao_2020]
- [Liu et al 2023][research_liu_lei_2023]
- [Liu et al 2023][research_liu_pang_2023]
- [Liu et al 2023][research_liu_wang_2023]
- [Liu et al 2023][research_liu_zhang_2023]
- [Liu et al 2024][research_liu_yang_2024]
- [Liu et al 2025][research_liu_fan_2025]
- [Liu et al 2025][research_liu_he_2025]
- [Liu et al 2025][research_liu_li_2025]
- [Liu et al 2026][research_liu_li_2026]
- [Liu et al 2026][research_liu_qian_2026]
- [Livet et al 1994][research_livet_kubica_1994]
- [Livet et al 1995][research_livet_kubica_1995]
- [Livne 1993][research_livne_1993]
- [Livne 2001][research_livne_2001]
- [Livne 2010][research_livne_2010]
- [Livne and Li 1994][research_livne_li_1994]
- [Lizotte, Andrew and Allen, Michael J. 2005][research_lizotteandrew_allenmichaelj_2005]
- [Lo and Chan][research_lo_chan]
- [Loads model development and analysis for the F/A-18 active aeroelastic wing airplane][research_aaw_loads_model]
- [Lobo do Vale et al 2021][research_lobodovale_raffaelli_2021]
- [Loewy 1969][research_loewy_1969]
- [Loewy 2000][research_loewy_2000]
- [Lokos et al 2002][research_lokos_olney_2002]
- [Lokos et al 2002][research_lokos_olney_2002_b]
- [Lokos et al 2005][research_lokos_lizotte_2005]
- [Lokos, William A. and Stauf, Rick 2004][research_lokoswilliama_staufrick_2004]
- [Lokos, William A. et al 2015][research_lokoswilliama_millerericj_2015]
- [Lombaerts 2012][research_lombaerts_2012]
- [Lombardi et al 1997][research_lombardi_salvetti_1997]
- [Londono and Leonhardt 2012][research_londono_leonhardt_2012]
- [Long 1968][research_long_1968]
- [Longitudinal Control And Trim 2003][research_longitudinal_control_2003]
- [Lorber and Carta 1991][research_lorber_carta_1991]
- [Loth et al 2000][research_loth_geubelle_2000]
- [Lottati 1985][research_lottati_1985]
- [Lottati 1987][research_lottati_1987]
- [Lottati 1988][research_lottati_1988]
- [Lou et al 2024][research_lou_duan_2024]
- [Love and Bohlmann 1991][research_love_bohlmann_1991]
- [Love and Lind 2010][research_love_lind_2010]
- [Low et al 2016][research_low_pheh_2016]
- [Lowe and Zingg 2021][research_lowe_zingg_2021]
- [Lu and Huang 1993][research_lu_huang_1993]
- [Lu and Murthy 1990][research_lu_murthy_1990]
- [Lu and Yeh 1993][research_lu_yeh_1993]
- [Lu et al 2016][research_lu_cui_2016]
- [Lu et al 2019][research_lu_ma_2019]
- [Lu et al 2026][research_lu_lan_2026]
- [Lucas 1978][research_lucas_1978]
- [Lucas et al 2009][research_lucas_valasek_2009]
- [Luce and Jr 1949][research_luce_jr_1949]
- [Luce and Moore 1963][research_luce_moore_1963]
- [Lukichev et al 2017][research_lukichev_demidova_2017]
- [Lum et al 2016][research_lum_xu_2016]
- [Luoma, Avro A 1944][research_luomaavroa_1944]
- [Luton and Mook 1992][research_luton_mook_1992]
- [Luton and Mook 1993][research_luton_mook_1993]
- [Ly et al 2006][research_ly_gear_2006]
- [Lykins and Keshmiri 2010][research_lykins_keshmiri_2010]
- [Lynch and Rogers 1976][research_lynch_rogers_1976]
- [Lyons et al 1973][research_lyons_vepa_1973]
- [M 2026][research_m_2026]
- [M. V. Sunil and Menghal 2022][research_mvsunil_menghal_2022]
- [Ma and Wang 2009][research_ma_wang_2009]
- [Ma et al 2022][research_ma_wang_2022]
- [Ma et al 2023][research_ma_liu_2023]
- [Maalawi 2012][research_maalawi_2012]
- [Mabey and Gaudet 1975][research_mabey_gaudet_1975]
- [Macek et al 2021][research_macek_branco_2021]
- [Macek et al 2021][research_macek_marciniak_2021]
- [Machado-e-Costa et al 2016][research_machadoecosta_valarinho_2016]
- [Mack 1979][research_mack_1979]
- [Macmillan 1981][research_macmillan_1981]
- [Macquart et al 2016][research_macquart_werter_2016]
- [Madson and Ericksont 1985][research_madson_ericksont_1985]
- [Magar et al 2018][research_magar_fuchi_2018]
- [Maharaj 1997][research_maharaj_1997]
- [Mahesh et al 1980][research_mahesh_stone_1980]
- [Mahmood 2025][research_mahmood_2025]
- [Maki 2016][research_maki_2016]
- [Mamedov et al 2018][research_mamedov_paryshev_2018]
- [Manan and Cooper 2008][research_manan_cooper_2008]
- [Mancini and Vos 2019][research_mancini_vos_2019]
- [Mandal and Gu 2016][research_mandal_gu_2016]
- [Mangalam et al 2007][research_mangalam_flick_2007]
- [Mangalam et al 2008][research_mangalam_mangalam_2008]
- [Mangalam et al 2010][research_mangalam_jutte_2010]
- [Manimala et al 2004][research_manimala_padfield_2004]
- [Mannarino and Mantegazza 2014][research_mannarino_mantegazza_2014]
- [Mansfield 1953][research_mansfield_1953]
- [Mao et al 2023][research_mao_guo_2023]
- [Marano et al 2022][research_marano_belardo_2022]
- [Marchetti 2023][research_marchetti_2023]
- [Marchman, Iii and Grantz 1982][research_marchmaniii_grantz_1982]
- [Marciniuk et al 2024][research_marciniuk_piskur_2024]
- [Mardanpour and Rastkar 2017][research_mardanpour_rastkar_2017]
- [Mardanpour et al 2013][research_mardanpour_richards_2013]
- [Mardanpour et al 2014][research_mardanpour_richards_2014]
- [Mardanpour et al 2019][research_mardanpour_izadpanahi_2019]
- [Marion and Sharma 2025][research_marion_sharma_2025]
- [Marks et al 2015][research_marks_zientarski_2015]
- [Marks et al 2016][research_marks_zientarski_2016]
- [Marques and Azevedo 2007][research_marques_azevedo_2007]
- [Marques and Azevedo 2008][research_marques_azevedo_2008]
- [Marques et al 2010][research_marques_badcock_2010]
- [Marques et al 2012][research_marques_badcock_2012]
- [Marretta and Marino 2007][research_marretta_marino_2007]
- [Martin 1978][research_martin_1978]
- [Martin and Gerber 1953][research_martin_gerber_1953]
- [Martin Co Denver Co 1966][research_martincodenverco_1966]
- [Marzocca et al 2002][research_marzocca_librescu_2002]
- [Mas Colomer][research_mascolomer]
- [Masarati et al 2010][research_masarati_quaranta_2010]
- [Masarati et al 2011][research_masarati_muscarello_2011]
- [Masarati et al 2016][research_masarati_tod_2016]
- [Masini et al 2019][research_masini_timme_2019]
- [Masini et al 2020][research_masini_timme_2020]
- [Maslan et al 2018][research_maslan_sira_2018]
- [Mason 1982][research_mason_1982]
- [Mason 1983][research_mason_1983]
- [Mason and Berg 1994][research_mason_berg_1994]
- [Mason and Iglesias 2001][research_mason_iglesias_2001]
- [Masson et al 1999][research_masson_veilleux_1999]
- [Masunaga and Bueno 2019][research_masunaga_bueno_2019]
- [Mataich et al 2025][research_mataich_elkhadiri_2025]
- [Matamoros and de Visser 2018][research_matamoros_devisser_2018]
- [Matheny and Panageas 1981][research_matheny_panageas_1981]
- [Matsuzaki et al 1987][research_matsuzaki_ueda_1987]
- [Matsuzaki et al 1989][research_matsuzaki_ueda_1989]
- [Mattaboni et al 2009][research_mattaboni_quaranta_2009]
- [Matter et al 2018][research_matter_darabseh_2018]
- [Matula et al 2026][research_matula_yalla_2026]
- [Maunder 1979][research_maunder_1979]
- [Maute et al 2008][research_maute_farhat_2008]
- [Mayer et al 2019][research_mayer_lutz_2019]
- [Mayo et al 2016][research_mayo_carroll_2016]
- [Mayya et al 2022][research_mayya_karnick_2022]
- [Mayya et al 2023][research_mayya_srivastava_2023]
- [Mballo and Prasad 2022][research_mballo_prasad_2022]
- [Mcclain and Pountney 1982][research_mcclain_pountney_1982]
- [McClintock 1959][research_mcclintock_1959]
- [Mccuish and Caldwell 2018][research_mccuish_caldwell_2018]
- [McDonald et al 1982][research_mcdonald_shamroth_1982]
- [McGurk et al 2024][research_mcgurk_stodieck_2024]
- [Mckenzie 1973][research_mckenzie_1973]
- [McLean 1994][research_mclean_1994]
- [Mcnally and Bach, Jr. 1988][research_mcnally_bachjr_1988]
- [McParlin and Adamczak 2003][research_mcparlin_adamczak_2003]
- [McQuinn and Valasek 2025][research_mcquinn_valasek_2025]
- [McTavish][research_mctavish]
- [Mehra, R. K. and Eupta, N. K. 1975][research_mehrark_euptank_1975]
- [Mehra, R. K. and Tyler, J. S. 1973][research_mehrark_tylerjs_1973]
- [Mehrotra, S. C. 1980][research_mehrotrasc_1980]
- [Mehta et al 2017][research_mehta_marland_2017]
- [Meirovitch 1995][research_meirovitch_1995]
- [Meirovitch and Tuzcu 2002][research_meirovitch_tuzcu_2002]
- [Melton et al 2005][research_melton_schaeffler_2005]
- [Melville 2000][research_melville_2000]
- [Melville 2002][research_melville_2002]
- [Melville 2021][research_melville_2021]
- [Melville and Gordnier 1998][research_melville_gordnier_1998]
- [Meng 2021][research_meng_2021]
- [Meng and Yu 2023][research_meng_yu_2023]
- [Meng et al 2020][research_meng_kaihua_2020]
- [Meng et al 2021][research_meng_wan_2021]
- [Meng et al 2024][research_meng_hu_2024]
- [Menshchikov and Somov 2019][research_menshchikov_somov_2019]
- [Menzies and Kandil 1996][research_menzies_kandil_1996]
- [Meresman and Ribak 2017][research_meresman_ribak_2017]
- [Merrett and Hilton 2011][research_merrett_hilton_2011]
- [Merrett et al 2011][research_merrett_hilton_2011_b]
- [Mertaugh 1998][research_mertaugh_1998]
- [Mertins et al 2005][research_mertins_elsholz_2005]
- [Methods of calculating the 2015][research_methods_of_calculating_2015]
- [Meyer and Fields 1978][research_meyer_fields_1978]
- [Meyer, Jr. and Schneider 1983][research_meyerjr_schneider_1983]
- [Michel et al 2025][research_michel_stalla_2025]
- [Micheli 2024][research_micheli_2024]
- [Micks 1950][research_micks_1950]
- [Mihaila-Andres et al 2017][research_mihailaandres_larco_2017]
- [Mihaila-Andres et al 2017][research_mihailaandres_rosu_2017]
- [Milanese et al 2008][research_milanese_marzocca_2008]
- [Miller and Schemensky 1979][research_miller_schemensky_1979]
- [Miller and Wood 1983][research_miller_wood_1983]
- [Miller et al 1979][research_miller_protopapas_1979]
- [Miller et al 2011][research_miller_decallafon_2011]
- [Miller et al 2014][research_miller_holguin_2014]
- [Miller et al 2019][research_miller_pena_2019]
- [Miller, Jr. 1973][research_millerjr_1973]
- [Miniature slide units offer 2002][research_miniature_slide_2002]
- [Minimum Performance Standard for][research_minimum_performance]
- [Minimum Performance Standard for][research_minimum_performance_b]
- [Miodushevsky and Ruggiero 2000][research_miodushevsky_ruggiero_2000]
- [Miskin and Takahashi 2018][research_miskin_takahashi_2018]
- [Miskin and Takahashi 2019][research_miskin_takahashi_2019]
- [Mission adaptive wing test program][research_mission_adaptive_wing]
- [Missoum 2012][research_missoum_2012]
- [Mitchell and Hoh 1984][research_mitchell_hoh_1984]
- [Miyazawa 2000][research_miyazawa_2000]
- [Mkhoyan et al 2020][research_mkhoyan_thakrar_2020]
- [Mkhoyan et al 2021][research_mkhoyan_thakrar_2021]
- [Mkhoyan et al 2022][research_mkhoyan_wang_2022]
- [Mkhoyan et al 2024][research_mkhoyan_wang_2024]
- [Mocsányi et al 2019][research_mocsanyi_takarics_2019]
- [Mocsányi et al 2020][research_mocsanyi_takarics_2020]
- [Model Reference Adaptation of 2016][research_model_reference_2016]
- [Model Rotor Testing for 2006][research_model_rotor_2006]
- [Mohamed and Dongare 2021][research_mohamed_dongare_2021]
- [Mohamed and G 2020][research_mohamed_g_2020]
- [Mohamed et al 2021][research_mohamed_abdelhady_2021]
- [Mohammadi 1999][research_mohammadi_1999]
- [Mohd et al 2025][research_mohd_amoozgar_2025]
- [Molton et al 2010][research_molton_bur_2010]
- [Molton et al 2013][research_molton_dandois_2013]
- [Molusis and Kleinman 1982][research_molusis_kleinman_1982]
- [Molz and Breitsamter 2026][research_molz_breitsamter_2026]
- [Moni et al 2026][research_moni_wales_2026]
- [Montel and Thielecke 2015][research_montel_thielecke_2015]
- [Montgomery 1971][research_montgomery_1971]
- [Montgomery and Hunsaker 2022][research_montgomery_hunsaker_2022]
- [Mooij 2020][research_mooij_2020]
- [Mooij and Wang 2021][research_mooij_wang_2021]
- [Moon 1996][research_moon_1996]
- [Moore 1992][research_moore_1992]
- [Moore 1995][research_moore_1995]
- [Moosavi and Elasha 2022][research_moosavi_elasha_2022]
- [Moosavian 2021][research_moosavian_2021]
- [Mor and Livne 2004][research_mor_livne_2004]
- [Mor and Livne 2005][research_mor_livne_2005]
- [Moravej Barzani et al 2022][research_moravejbarzani_shahverdi_2022]
- [Mordfin and Bloss 1962][research_mordfin_bloss_1962]
- [Morelli 2011][research_morelli_2011]
- [Morelli 2012][research_morelli_2012]
- [Morelli and Klein 1995][research_morelli_klein_1995]
- [Moreno et al 2012][research_moreno_seiler_2012]
- [Moreno et al 2015][research_moreno_pfifer_2015]
- [Morgenstern 2004][research_morgenstern_2004]
- [Morger 1988][research_morger_1988]
- [Morino and Obayashi 2015][research_morino_obayashi_2015]
- [Morphing WING REAL TIME 2010][research_morphing_wing_2010]
- [Morphing Wing Technologies 2018][research_morphing_wing_2018]
- [Morton et al 2012][research_morton_cox_2012]
- [Moshier 2006][research_moshier_2006]
- [Moshtaghzadeh et al 2023][research_moshtaghzadeh_rangel_2023]
- [Moszczynski et al 2026][research_moszczynski_grant_2026]
- [Moulin 2004][research_moulin_2004]
- [Moulin et al 2001][research_moulin_idan_2001]
- [Moulin et al 2002][research_moulin_idan_2002]
- [Moulin et al 2010][research_moulin_ritz_2010]
- [Moulin et al 2011][research_moulin_zeng_2011]
- [Mouyon et al 2003][research_mouyon_cumer_2003]
- [Mu et al 2022][research_mu_huang_2022]
- [Mu et al 2026][research_mu_huang_2026]
- [Muchamad Bayu Sakti Pratama et al 2022][research_muchamadbayusaktipratama_erwinsulaeman_2022]
- [Muhamad Jayadi 2025][research_muhamadjayadi_2025]
- [Mukherjee and Shaw 2004][research_mukherjee_shaw_2004]
- [Mukherjee and Shaw 2007][research_mukherjee_shaw_2007]
- [Mukhopadhyay 1988][research_mukhopadhyay_1988]
- [Mukhopadhyay 1995][research_mukhopadhyay_1995]
- [Mukhopadhyay 2003][research_mukhopadhyay_2003]
- [Mulder et al 2009][research_mulder_lubbers_2009]
- [Muradas Odriozola][research_muradasodriozola]
- [Murch 2008][research_murch_2008]
- [Murphy and Mermagen 2004][research_murphy_mermagen_2004]
- [Murphy et al 2004][research_murphy_klein_2004]
- [Murthy and Lu 1992][research_murthy_lu_1992]
- [Murugan and Ganguli 2005][research_murugan_ganguli_2005]
- [Muscarello et al 2017][research_muscarello_masarati_2017]
- [Muscarello et al 2026][research_muscarello_marzocca_2026]
- [Muscati and Grootenhuis 1975][research_muscati_grootenhuis_1975]
- [Muñoz and García-Fogeda 2022][research_munoz_garciafogeda_2022]
- [Muñoz and García-Fogeda 2023][research_munoz_garciafogeda_2023]
- [Muñoz and García-Fogeda 2024][research_munoz_garciafogeda_2024]
- [Muñoz Medina][research_munozmedina]
- [Müller et al 2026][research_muller_woidt_2026]
- [Na Zhao et al 2010][research_nazhao_dengqingcao_2010]
- [NACA Conference on Aerodynamic 1949][research_naca_conference_1949]
- [Nadim Melhem et al 2024][research_nadimmelhem_richardmunroe_2024]
- [Nadimi 1999][research_nadimi_1999]
- [Nae et al 2019][research_nae_stroe_2019]
- [Naftaly and Raveh 2025][research_naftaly_raveh_2025]
- [Nailu et al 2025][research_nailu_wentao_2025]
- [Nair and Goza 2022][research_nair_goza_2022]
- [Najmi et al 2023][research_najmi_siddiqui_2023]
- [Nakadate 2005][research_nakadate_2005]
- [Nam et al 1996][research_nam_kim_1996]
- [Nam et al 1997][research_nam_kim_1997]
- [Namdeo et al 2023][research_namdeo_bhattacharyya_2023]
- [Nangia and Palmer 2007][research_nangia_palmer_2007]
- [Napolitano et al 2001][research_napolitano_song_2001]
- [Narain 1983][research_narain_1983]
- [Narayanaswamy et al 2008][research_narayanaswamy_narayanan_2008]
- [Narimani et al 2025][research_narimani_haddadpour_2025]
- [Nash et al 2025][research_nash_timme_2025]
- [Nasu, Ken-Ichi 1986][research_nasukenichi_1986]
- [Navardi et al 2023][research_navardi_shahverdi_2023]
- [Navardi et al 2026][research_navardi_shahverdi_2026]
- [Navrátil et al 2024][research_navratil_hostinsky_2024]
- [Naylor 1957][research_naylor_1957]
- [Neumann et al 2020][research_neumann_dealmeida_2020]
- [Newman and Buttrill 1995][research_newman_buttrill_1995]
- [Newman and Kassem 1997][research_newman_kassem_1997_b]
- [Newman and Schmidt 1994][research_newman_schmidt_1994]
- [Newman et al 1997][research_newman_kassem_1997]
- [Newman et al 1997][research_newman_kassem_1997_c]
- [Newman, Iii and Baysal 1992][research_newmaniii_baysal_1992]
- [Newsom 1978][research_newsom_1978]
- [Newsom 1979][research_newsom_1979]
- [Newsome et al 1998][research_newsome_berkooz_1998]
- [Ng et al 2020][research_ng_ong_2020]
- [Nguyen 2021][research_nguyen_2021]
- [Nguyen and Swei 2015][research_nguyen_swei_2015]
- [Nguyen and Tal 2015][research_nguyen_tal_2015]
- [Nguyen and Tuzcu 2009][research_nguyen_tuzcu_2009]
- [Nguyen and Urnes 2012][research_nguyen_urnes_2012]
- [Nguyen and Xiong 2021][research_nguyen_xiong_2021]
- [Nguyen and Xiong 2022][research_nguyen_xiong_2022]
- [Nguyen and Xiong 2023][research_nguyen_xiong_2023_b]
- [Nguyen and Xiong 2023][research_nguyen_xiong_2023_c]
- [Nguyen and Xiong 2024][research_nguyen_xiong_2024]
- [Nguyen and Xiong 2024][research_nguyen_xiong_2024_b]
- [Nguyen and Xiong 2026][research_nguyen_xiong_2026_b]
- [Nguyen et al 2011][research_nguyen_tuzcu_2011]
- [Nguyen et al 2013][research_nguyen_ting_2013]
- [Nguyen et al 2013][research_nguyen_ting_2013_b]
- [Nguyen et al 2015][research_nguyen_precup_2015]
- [Nguyen et al 2015][research_nguyen_ting_2015]
- [Nguyen et al 2015][research_nguyen_ting_2015_b]
- [Nguyen et al 2016][research_nguyen_ting_2016]
- [Nguyen et al 2017][research_nguyen_ting_2017]
- [Nguyen et al 2018][research_nguyen_hashemi_2018]
- [Nguyen et al 2018][research_nguyen_reynolds_2018]
- [Nguyen et al 2018][research_nguyen_saussie_2018]
- [Nguyen et al 2018][research_nguyen_ting_2018]
- [Nguyen et al 2019][research_nguyen_cramer_2019]
- [Nguyen et al 2019][research_nguyen_fugate_2019]
- [Nguyen et al 2020][research_nguyen_cramer_2020]
- [Nguyen et al 2022][research_nguyen_webb_2022]
- [Nguyen et al 2023][research_nguyen_xiong_2023]
- [Nguyen et al 2026][research_nguyen_xiong_2026]
- [Nguyen, Nhan et al 2015][research_nguyennhan_kaulupender_2015]
- [Nhan Nguyen et al][research_nhannguyen_benjaminwebb]
- [Niblett 1986][research_niblett_1986]
- [Nicolaides 1976][research_nicolaides_1976]
- [Nicolas et al 2016][research_nicolas_sullivan_2016]
- [Nicolosi et al 2020][research_nicolosi_cusati_2020]
- [Niculescu et al 2021][research_niculescu_corcau_2021]
- [Nie et al 2009][research_nie_zhang_2009]
- [Niel][research_niel]
- [Nieminen et al 2023][research_nieminen_tuohineva_2023]
- [Nikolaos et al 2024][research_nikolaos_spyridon_2024]
- [Nilsson et al 2023][research_nilsson_yao_2023]
- [Nisbet et al 1958][research_nisbet_brennan_1958]
- [Nisbet et al 1960][research_nisbet_brennan_1960]
- [Nissim 1975][research_nissim_1975]
- [Nissim 1976][research_nissim_1976]
- [Nissim and Lottati 1979][research_nissim_lottati_1979]
- [Nissim and Lottati 1979][research_nissim_lottati_1979_b]
- [Nissim and Lottati 1980][research_nissim_lottati_1980]
- [Nissim, E. et al 1976][research_nissime_caspia_1976]
- [Nitzsche 1994][research_nitzsche_1994]
- [Niven and Tait 2000][research_niven_tait_2000]
- [Nixon 2020][research_nixon_2020]
- [Nixon and Tzuoo 1987][research_nixon_tzuoo_1987]
- [Nixon et al 2000][research_nixon_piatak_2000]
- [Nixon, Mark W. et al 1999][research_nixonmarkw_piatakdavidj_1999]
- [Noevere and Wilhite 2016][research_noevere_wilhite_2016]
- [Noh et al 2025][research_noh_andreu_2025]
- [Noll and Huttsell 1978][research_noll_huttsell_1978]
- [Noll and Huttsell 1979][research_noll_huttsell_1979]
- [Noll and Merino 1976][research_noll_merino_1976]
- [Noll et al 1980][research_noll_huttsell_1980]
- [Noll et al 1983][research_noll_calico_1983]
- [Noll et al 1983][research_noll_eastep_1983]
- [Noll et al 1984][research_noll_eastep_1984]
- [Noll et al 1989][research_noll_perryiii_1989]
- [Nomura 2003][research_nomura_2003]
- [Norton 1989][research_norton_1989]
- [Norton 1990][research_norton_1990]
- [Null and Shkarayev 2004][research_null_shkarayev_2004]
- [Null and Shkarayev 2005][research_null_shkarayev_2005]
- [Numerical calculation method and 2015][research_numerical_calculation_2015]
- [Numerical Method and Program 2013][research_numerical_method_2013]
- [Nurohman et al 2018][research_nurohman_arifianto_2018]
- [O'Brien and Datta 2026][research_obrien_datta_2026]
- [O'Donnell and Mohseni 2019][research_odonnell_mohseni_2019]
- [Obayashi et al 2000][research_obayashi_sasaki_2000]
- [Oberkampf 1974][research_oberkampf_1974]
- [Obradovic and Subbarao 2010][research_obradovic_subbarao_2010]
- [Ockier et al 2017][research_ockier_kolb_2017]
- [Odriozola et al 2026][research_odriozola_marquier_2026]
- [Oelker and Friehmelt 1998][research_oelker_friehmelt_1998]
- [Ogren et al 1974][research_ogren_sotanski_1974]
- [Ohta and Fujimori 1988][research_ohta_fujimori_1988]
- [Ohta et al 1984][research_ohta_nikiforuk_1984]
- [Ohta et al 1989][research_ohta_fujimori_1989]
- [Ojiaku and Prakash 2026][research_ojiaku_prakash_2026]
- [Oliver and Singh 2020][research_oliver_singh_2020]
- [Olivett et al 2020][research_olivett_corrao_2020]
- [On selection of the 1972][research_on_selection_1972]
- [Onkar et al 2024][research_onkar_kumar_2024]
- [Opgenoord and Willcox 2018][research_opgenoord_willcox_2018]
- [Oremland et al 2017][research_oremland_suryakumar_2017]
- [Ormiston 2001][research_ormiston_2001]
- [Orr 2010][research_orr_2010]
- [Ossmann and Poussot-Vassal 2018][research_ossmann_poussotvassal_2018]
- [Othman et al 2019][research_othman_silva_2019]
- [Ouellette 2017][research_ouellette_2017]
- [Ouellette 2026][research_ouellette_2026]
- [Ouellette et al 2010][research_ouellette_patil_2010]
- [Ouellette et al 2012][research_ouellette_patil_2012]
- [Ouellette et al 2014][research_ouellette_patil_2014]
- [Ouellette et al 2023][research_ouellette_miller_2023]
- [Ouyang et al 2013][research_ouyang_chen_2013]
- [Ouyang et al 2021][research_ouyang_gu_2021]
- [Ouyang et al 2026][research_ouyang_jia_2026]
- [Overload Detection System Using 2023][research_overload_detection_2023]
- [Owens et al 2003][research_owens_capone_2003]
- [Owens et al 2004][research_owens_capone_2004]
- [Owens et al 2006][research_owens_mcconnell_2006]
- [Oyibo 1983][research_oyibo_1983]
- [Oyibo 1984][research_oyibo_1984]
- [Oz et al 2025][research_oz_ekici_2025]
- [Ozbay 1993][research_ozbay_1993]
- [Ozbay and Turi][research_ozbay_turi]
- [Ozbek et al 2023][research_ozbek_ekici_2023]
- [Ozbek et al 2024][research_ozbek_ekici_2024]
- [Ozger 2007][research_ozger_2007]
- [Pachikara and Lind 2012][research_pachikara_lind_2012]
- [Padova and Falk 1980][research_padova_falk_1980]
- [Padua and Preisighe Viana 2025][research_padua_preisigheviana_2025]
- [Palacios and Cesnik 2005][research_palacios_cesnik_2005]
- [Palacios et al 2009][research_palacios_glaz_2009]
- [Paladini et al 2024][research_paladini_drewiacki_2024]
- [Palaia et al 2025][research_palaia_salem_2025]
- [Paletta et al 2010][research_paletta_belardo_2010]
- [Pan and Huang 2019][research_pan_huang_2019]
- [Pandita et al 2009][research_pandita_chakraborty_2009]
- [Panel flutter in a 1991][research_panel_flutter_1991]
- [Pang et al 2025][research_pang_yin_2025]
- [Paniagua 2013][research_paniagua_2013]
- [Pankonien et al 2018][research_pankonien_durscher_2018]
- [Pankonien et al 2019][research_pankonien_durscher_2019]
- [Papadopoulos 1958][research_papadopoulos_1958]
- [Paper, board and pulps][research_paper_board]
- [Papila and Haftka 1999][research_papila_haftka_1999]
- [Paris and Alaverdi 2005][research_paris_alaverdi_2005]
- [Park and Abla 1982][research_park_abla_1982]
- [Park and Abla 1983][research_park_abla_1983]
- [Park and Chung 2012][research_park_chung_2012]
- [Park et al 2001][research_park_lee_2001]
- [Parker et al 1991][research_parker_spain_1991]
- [Parsons][research_parsons]
- [Pasley et al 1973][research_pasley_rohling_1973]
- [Passive wing/store flutter suppression 1982][research_passive_wing_store_1982]
- [Patartics et al 2017][research_patartics_luspay_2017]
- [Patidar et al 2025][research_patidar_sarwar_2025]
- [Patil 2003][research_patil_2003]
- [Patil and Clark 2002][research_patil_clark_2002]
- [Patil and Hodges 2000][research_patil_hodges_2000_b]
- [Patil and Patil 1997][research_patil_patil_1997]
- [Patil et al 2000][research_patil_hodges_2000]
- [Paul][research_paul]
- [Paul and Rein 2016][research_paul_rein_2016]
- [Paul and Rein 2017][research_paul_rein_2017]
- [Pavanasam et al 2024][research_pavanasam_anil_2024]
- [Pavlenko and Reslan 2022][research_pavlenko_reslan_2022]
- [Pavlov and Pavlov 2024][research_pavlov_pavlov_2024]
- [Pawlak 1994][research_pawlak_1994]
- [Pearson, Henry A and Aiken, William S, Jr 1944][research_pearsonhenrya_aikenwilliamsjr_1944]
- [Pecora 2018][research_pecora_2018]
- [Pecora and Pecora 2018][research_pecora_pecora_2018]
- [Pecora et al 2012][research_pecora_amoroso_2012]
- [Pecora et al 2018][research_pecora_amoroso_2018]
- [Pecora et al 2021][research_pecora_amoroso_2021]
- [Pedreiro et al 1998][research_pedreiro_takahara_1998]
- [Pedreiro et al 1999][research_pedreiro_takahara_1999]
- [Peele, E. L. and Eckstrom, C. V. 1975][research_peeleel_eckstromcv_1975]
- [Pellegrino et al 2022][research_pellegrino_quaranta_2022]
- [Peloubet, Jr. et al 1983][research_peloubetjr_haller_1983]
- [Pendleton et al 1998][research_pendleton_bessette_1998]
- [Pendleton et al 2007][research_pendleton_flick_2007]
- [Peng 2011][research_peng_2011]
- [Peng et al 2024][research_peng_wang_2024]
- [Penning et al 2009][research_penning_zink_2009]
- [Perera and Guo 2008][research_perera_guo_2008]
- [Perez-Becker et al 2021][research_perezbecker_marten_2021]
- [Perkins and Brice 1966][research_perkins_brice_1966]
- [Perry, Iii et al 1990][research_perryiii_mukhopadhyay_1990]
- [Persoon et al 1980][research_persoon_roos_1980]
- [Peschel and Röske 2000][research_peschel_roske_2000]
- [Peter and Stumpf 2018][research_peter_stumpf_2018]
- [Petermeier et al 2010][research_petermeier_radtke_2010]
- [Peters 1988][research_peters_1988]
- [Petersen 1981][research_petersen_1981]
- [Petronevich et al 2021][research_petronevich_lyutov_2021]
- [Pettit and Grandhi 2003][research_pettit_grandhi_2003]
- [Pfaff 1965][research_pfaff_1965]
- [Pfeifle and Fichter 2021][research_pfeifle_fichter_2021]
- [Pfeifle and Fichter 2021][research_pfeifle_fichter_2021_b]
- [Pfeifle and Fichter 2023][research_pfeifle_fichter_2023]
- [Phan 2020][research_phan_2020]
- [Philipsen and Zhai 2007][research_philipsen_zhai_2007]
- [Phillips][research_phillips]
- [Phillips et al 2022][research_phillips_white_2022]
- [Piatak, David J. and Cleckner, Craig S. 2002][research_piatakdavidj_clecknercraigs_2002]
- [Picard 2002][research_picard_2002]
- [Pines and Newman 1974][research_pines_newman_1974]
- [Pines et al 1955][research_pines_dugundji_1955]
- [Pitt 2004][research_pitt_2004]
- [Pitt et al 2016][research_pitt_sexton_2016]
- [Pitt Ford et al 2012][research_pittford_stevens_2012]
- [Plaban and Takahashi 2021][research_plaban_takahashi_2021]
- [Plaetschke et al 1982][research_plaetschke_mulder_1982]
- [Plath][research_plath]
- [Polonsky 2026][research_polonsky_2026]
- [Pomin et al 2001][research_pomin_altmikus_2001]
- [Poojari 2022][research_poojari_2022]
- [Poole et al 2020][research_poole_allen_2020]
- [Poole et al 2020][research_poole_allen_2020_b]
- [Poomadath and Ajaj 2025][research_poomadath_ajaj_2025]
- [Popelka et al 1997][research_popelka_lindsay_1997]
- [Poplingher et al 2022][research_poplingher_mallik_2022]
- [Porter and Gu 1991][research_porter_gu_1991]
- [Porter et al 1992][research_porter_merzougui_1992]
- [Porter et al 1992][research_porter_merzougui_1992_b]
- [Porterfield and Alexander 1970][research_porterfield_alexander_1970]
- [Pototzky 2010][research_pototzky_2010]
- [Potvin and Grant 2026][research_potvin_grant_2026]
- [Pourtakdoust and Khodabakhsh 2026][research_pourtakdoust_khodabakhsh_2026]
- [Poussot-Vassal et al 2022][research_poussotvassal_vuillemin_2022]
- [Powers et al 1992][research_powers_webb_1992]
- [Prabhakar 2025][research_prabhakar_2025]
- [Prabhakar and Murugan 2022][research_prabhakar_murugan_2022]
- [Prabhakar and Murugan 2026][research_prabhakar_murugan_2026]
- [Prasannakumar et al 2022][research_prasannakumar_sudhi_2022]
- [Prasanth and Mehra 1999][research_prasanth_mehra_1999]
- [Prato et al 2026][research_prato_facello_2026]
- [Prazenica 2014][research_prazenica_2014]
- [Prazenica et al 2004][research_prazenica_reisenthel_2004]
- [Precup et al 2018][research_precup_mor_2018]
- [Pressures and Temperatures for 2000][research_pressures_and_2000]
- [Price et al 2002][research_price_koffi_2002]
- [Prochazka et al 2018][research_prochazka_eduardo_2018]
- [Production support flight control computers, research capability for F/A-18 aircraft at Dryden Flight Research Center][research_psfcc]
- [Properties and Design of 2012][research_properties_and_2012]
- [Properties of the U.S 2014][research_properties_of_2014]
- [Properties of the U.S 2024][research_properties_of_2024]
- [Proulx-Cabana][research_proulxcabana]
- [Prudhomme 1995][research_prudhomme_1995]
- [Prudhomme and Prudhomme 1997][research_prudhomme_prudhomme_1997]
- [Psarros and Savaidis 2025][research_psarros_savaidis_2025]
- [Psolla-Bress et al][research_psollabress_haselmeyer]
- [Puentes and Takahashi 2024][research_puentes_takahashi_2024]
- [Punzi et al 2024][research_punzi_crooks_2024]
- [Pursel 1977][research_pursel_1977]
- [Purser, P. E. and Tucker, W. A. 1949][research_purserpe_tuckerwa_1949]
- [Purwadi et al 2023][research_purwadi_hidayat_2023]
- [Pusch 2017][research_pusch_2017]
- [Pusch 2018][research_pusch_2018]
- [Pusch et al 2019][research_pusch_knoblach_2019]
- [Pusch et al 2022][research_pusch_kier_2022]
- [Pushtaev 1989][research_pushtaev_1989]
- [Puyou and Berard 2007][research_puyou_berard_2007]
- [Qi et al 2015][research_qi_ting_2015]
- [Qian 2018][research_qian_2018]
- [Qian and Alonso 2021][research_qian_alonso_2021]
- [Qian et al 2014][research_qian_huang_2014]
- [Qian et al 2014][research_qian_huang_2014_b]
- [Qiao et al 2018][research_qiao_zhou_2018]
- [Qiao et al 2019][research_qiao_zhou_2019]
- [Qiao et al 2025][research_qiao_wang_2025]
- [Qin 2012][research_qin_2012]
- [Qin and Librescu 2003][research_qin_librescu_2003]
- [Qin and Zhang 2013][research_qin_zhang_2013]
- [Qin et al 2023][research_qin_liu_2023]
- [Qin et al 2023][research_qin_wei_2023]
- [Qiu and Ang 2019][research_qiu_ang_2019]
- [Qiu and Wang 2021][research_qiu_wang_2021]
- [Qiu et al 2018][research_qiu_xu_2018]
- [Qu and Li 2022][research_qu_li_2022]
- [Qu et al 2025][research_qu_xu_2025]
- [Quach 2026][research_quach_2026]
- [Quach 2026][research_quach_2026_b]
- [Quackenbush et al 2009][research_quackenbush_keller_2009]
- [Quaranta et al 2013][research_quaranta_masarati_2013]
- [Quero 2025][research_quero_2025]
- [Raab 2014][research_raab_2014]
- [Raab 2026][research_raab_2026]
- [Rade and de Souza 2016][research_rade_desouza_2016]
- [Radestock et al 2018][research_radestock_falken_2018]
- [Raghunathan and Coll 1981][research_raghunathan_coll_1981]
- [Raghunathan et al 1998][research_raghunathan_mitchell_1998]
- [Rahman and Li 2013][research_rahman_li_2013]
- [Rahn, D. and Reinertson, L. 1986][research_rahnd_reinertsonl_1986]
- [Rains et al 2024][research_rains_huang_2024]
- [Raisinghani and Adak 1983][research_raisinghani_adak_1983]
- [Raisinghani and Kumar 1995][research_raisinghani_kumar_1995]
- [Raj 1983][research_raj_1983]
- [Raja and Upadhya 2007][research_raja_upadhya_2007]
- [Rajpal et al 2021][research_rajpal_mitrotta_2021]
- [Rakin 1981][research_rakin_1981]
- [Raluca MAXIM 2020][research_ralucamaxim_2020]
- [Rambacher and Bons 2023][research_rambacher_bons_2023]
- [Ramlal et al 2025][research_ramlal_desai_2025]
- [Rao and Padmanabhan 2019][research_rao_padmanabhan_2019]
- [Rao et al][research_rao_behal]
- [Rao et al 1978][research_rao_kronenberger_1978]
- [Rao et al 2005][research_rao_behal_2005]
- [Raol and Singh 2023][research_raol_singh_2023]
- [Raol and Singh 2023][research_raol_singh_2023_b]
- [Raoof and Kraincanic 1998][research_raoof_kraincanic_1998]
- [Ratcliff et al 2016][research_ratcliff_bodkin_2016]
- [Ratliff and Pagilla 2008][research_ratliff_pagilla_2008]
- [Raveh 2026][research_raveh_2026]
- [Raveh and Levy 2004][research_raveh_levy_2004]
- [Raveh et al 2023][research_raveh_sodja_2023]
- [Re 2014][research_re_2014]
- [Rea et al 2017][research_rea_pecora_2017]
- [Rea et al 2018][research_rea_pecora_2018]
- [Reasor et al 2016][research_reasor_bhamidipati_2016]
- [Recine et al 2025][research_recine_schuh_2025]
- [Reddy 1987][research_reddy_1987]
- [Rediess and Melton 1994][research_rediess_melton_1994]
- [Reding and Ericsson 1977][research_reding_ericsson_1977]
- [Reduction of structural loads using maneuver load control on the advanced fighter technology integration F-111 mission adaptive wing][research_afti_mlc]
- [Regan 1964][research_regan_1964]
- [Rehfield et al 1991][research_rehfield_chang_1991]
- [Reich et al 2002][research_reich_raveh_2002]
- [Reich et al 2004][research_reich_raveh_2004]
- [Reich, hoor, Mart et al 1995][research_reichhoormart_lin_1995]
- [Reichenbach 2008][research_reichenbach_2008]
- [Reichenbach et al 2009][research_reichenbach_urnes_2009]
- [Reichenbach et al 2011][research_reichenbach_castelluccio_2011]
- [Reinbold et al 2026][research_reinbold_breitsamter_2026]
- [Reist et al 2022][research_reist_koo_2022]
- [Rendina and Mazzoni 1999][research_rendina_mazzoni_1999]
- [Renken 1985][research_renken_1985]
- [Rennie and Jumper 1995][research_rennie_jumper_1995]
- [Rennie and Jumper 1997][research_rennie_jumper_1997]
- [Report No. 538, altitude-pressure 1935][research_report_no_1935]
- [Requirements of a commercial 1967][research_requirements_of_1967]
- [Reschke 2005][research_reschke_2005]
- [Rester and A. C. 1984][research_rester_ac_1984]
- [Rester and Alfred C. 1988][research_rester_alfredc_1988]
- [Reuther and Jameson 1995][research_reuther_jameson_1995]
- [Revivo and Raveh 2025][research_revivo_raveh_2025]
- [Rhoads 1952][research_rhoads_1952]
- [Ricci and Scotti 2008][research_ricci_scotti_2008]
- [Ricci and Scotti 2009][research_ricci_scotti_2009]
- [Ricci et al 2008][research_ricci_scotti_2008_b]
- [Ricci et al 2016][research_ricci_degaspari_2016]
- [Ricci et al 2022][research_ricci_marchetti_2022]
- [Richard et al 2000][research_richard_rule_2000]
- [Richard et al 2001][research_richard_rule_2001]
- [Richardson and Kesler 1988][research_richardson_kesler_1988]
- [Richter et al 2023][research_richter_khalifa_2023]
- [Rieck et al 2026][research_rieck_herrmann_2026]
- [Riemersma and Lammertink 1988][research_riemersma_lammertink_1988]
- [Rigatos et al 2026][research_rigatos_dala_2026]
- [Righi 2017][research_righi_2017]
- [Rill and Ganzer 1988][research_rill_ganzer_1988]
- [Rimer et al 1984][research_rimer_chipman_1984]
- [Rimer et al 1984][research_rimer_chipman_1984_b]
- [Rimer et al 1986][research_rimer_chipman_1986]
- [Riou et al 2010][research_riou_garnier_2010]
- [Rising 1982][research_rising_1982]
- [Ritter et al 2017][research_ritter_dillinger_2017]
- [Rizk 1980][research_rizk_1980]
- [Rizzetta 1977][research_rizzetta_1977]
- [Rizzetta 1995][research_rizzetta_1995]
- [Rizzi 1981][research_rizzi_1981]
- [Rizzi 1981][research_rizzi_1981_b]
- [Rizzi 1984][research_rizzi_1984]
- [Rizzi 1995][research_rizzi_1995]
- [Rizzi et al 1986][research_rizzi_purcell_1986]
- [Ro et al 1992][research_ro_barlow_1992]
- [Roberts et al 1966][research_roberts_smith_1966]
- [Robins and Carlson 1979][research_robins_carlson_1979]
- [Robins and Carlson 1980][research_robins_carlson_1980]
- [Robinson][research_robinson]
- [Robinson][research_robinson_b]
- [Rocha Da Costa][research_rochadacosta]
- [Rocha et al 2005][research_rocha_moniz_2005]
- [Rocha et al 2007][research_rocha_moniz_2007]
- [Rock et al 1993][research_rock_ashley_1993]
- [Rodden 1956][research_rodden_1956]
- [Rodden 1981][research_rodden_1981]
- [Rodden 1984][research_rodden_1984]
- [Rodden 1989][research_rodden_1989]
- [Rodden and Bellinger 1982][research_rodden_bellinger_1982]
- [Rodden and Love 1984][research_rodden_love_1984]
- [Rodden and Love 1985][research_rodden_love_1985]
- [Roeser and Mönnich 2024][research_roeser_monnich_2024]
- [Roger et al 1974][research_roger_hodges_1974]
- [Rogers 1998][research_rogers_1998]
- [Rogers 2007][research_rogers_2007]
- [Roknizadeh et al 2012][research_roknizadeh_nobari_2012]
- [Roll plus maneuver load alleviation control system designs for the active flexible wing][research_afw_roll_mla]
- [Rolling effectiveness and aileron reversal of rectangular wings at supersonic speeds][research_supersonic_aileron_reversal]
- [Rolling maneuver load alleviation using active controls][research_rolling_mla_active]
- [Roohani and Skews 2009][research_roohani_skews_2009]
- [Roos et al 1975][research_roos_bennekers_1975]
- [Rose and Jinu 2014][research_rose_jinu_2014]
- [Rosemann and Birkemeyer 2002][research_rosemann_birkemeyer_2002]
- [Rosenberg 1944][research_rosenberg_1944]
- [Roskam, J. and Lan, C. 1973][research_roskamj_lanc_1973]
- [Roskam, J. et al 1972][research_roskamj_lanc_1972]
- [Ross et al 1993][research_ross_law_1993]
- [Roughen et al 2010][research_roughen_bendiksen_2010]
- [Rowan and Burns 1975][research_rowan_burns_1975]
- [Rowley 2008][research_rowley_2008]
- [Rowley 2010][research_rowley_2010]
- [Roy and Eversman 1996][research_roy_eversman_1996]
- [Roysdon and Khalid 2010][research_roysdon_khalid_2010]
- [Roysdon and Khalid 2011][research_roysdon_khalid_2011]
- [Rubillo et al 2005][research_rubillo_bollt_2005]
- [Rufino et al 2026][research_rufino_faria_2026]
- [Ruhlin and Pratt-Barlow 1981][research_ruhlin_prattbarlow_1981]
- [Ruiz Garcia et al 2022][research_ruizgarcia_brown_2022]
- [Rule et al 2000][research_rule_richard_2000]
- [Rule et al 2001][research_rule_richard_2001]
- [Ruler 1967][research_ruler_1967]
- [Rumpfkeil et al 2021][research_rumpfkeil_lickenbrock_2021]
- [Russo et al 2020][research_russo_tognaccini_2020]
- [Russo et al 2020][research_russo_tognaccini_2020_b]
- [Rustenburg 1973][research_rustenburg_1973]
- [Rutkowski 1979][research_rutkowski_1979]
- [S et al 2025][research_s_a_2025]
- [S.A. Gee et al][research_sagee_akylas]
- [Sabatini et al 2026][research_sabatini_coppotelli_2026]
- [Sabatini et al 2026][research_sabatini_livne_2026]
- [Sacchi et al 2025][research_sacchi_healy_2025]
- [Sackett and Kirchwey 1982][research_sackett_kirchwey_1982]
- [Sadien et al 2019][research_sadien_carton_2019]
- [Sadien et al 2020][research_sadien_roos_2020]
- [Sahasrabudhe et al 1997][research_sahasrabudhe_celi_1997]
- [Sahoo and Cesnik 2002][research_sahoo_cesnik_2002]
- [Sahyoun et al 2026][research_sahyoun_boose_2026]
- [Sainio and Krandel 1993][research_sainio_krandel_1993]
- [Saitoh et al 1995][research_saitoh_hashidate_1995]
- [Sakamura and Komaki 2011][research_sakamura_komaki_2011]
- [Saltari et al 2022][research_saltari_pizzoli_2022]
- [Sampo' et al 2010][research_sampo_sorniotti_2010]
- [Samuels 1982][research_samuels_1982]
- [Sandahl, Carl A 1948][research_sandahlcarla_1948]
- [Sanders et al 2003][research_sanders_eastep_2003]
- [Sandford et al 1980][research_sandford_ricketts_1980]
- [Sang Bum Choi et al][research_sangbumchoi_haojianxu]
- [Sanghi et al 2020][research_sanghi_riso_2020]
- [Sanghi et al 2022][research_sanghi_riso_2022]
- [Sanghi et al 2024][research_sanghi_cesnik_2024]
- [Sanmugadas et al 2021][research_sanmugadas_gupta_2021]
- [Santos et al 2026][research_santos_marques_2026]
- [Sapkal and Attar 2011][research_sapkal_attar_2011]
- [Sapkal and Attar 2012][research_sapkal_attar_2012]
- [Sardahi and Kolonay 2021][research_sardahi_kolonay_2021]
- [Saric 2010][research_saric_2010]
- [Sarnico 1993][research_sarnico_1993]
- [Sarojini et al 2022][research_sarojini_solano_2022]
- [Sartor][research_sartor]
- [Sartor et al 2012][research_sartor_losfeld_2012]
- [Sartor et al 2013][research_sartor_clement_2013]
- [Sarvankar et al 2023][research_sarvankar_sarkar_2023]
- [Sarvankar et al 2024][research_sarvankar_sarkar_2024]
- [Sattar et al 2020][research_sattar_wang_2020]
- [Sazesh and Shams 2017][research_sazesh_shams_2017]
- [Scalera and Durham 1999][research_scalera_durham_1999]
- [Scaramal and Horn 2022][research_scaramal_horn_2022]
- [Scaramal and Horn 2023][research_scaramal_horn_2023]
- [Scaramal et al 2021][research_scaramal_saetti_2021]
- [Scarth et al 2015][research_scarth_sartor_2015]
- [Schajer 2021][research_schajer_2021]
- [Schauerte et al 2026][research_schauerte_kwong_2026]
- [Schewe and Mai 2019][research_schewe_mai_2019]
- [Schildkamp et al 2023][research_schildkamp_chang_2023]
- [Schlemmer et al 2020][research_schlemmer_dehmlow_2020]
- [Schmidt 1986][research_schmidt_1986]
- [Schmidt 1986][research_schmidt_1986_b]
- [Schmidt 1991][research_schmidt_1991]
- [Schmidt 1995][research_schmidt_1995]
- [Schmidt 2016][research_schmidt_2016]
- [Schmidt and Chavez 2001][research_schmidt_chavez_2001]
- [Schmidt and Newman 1988][research_schmidt_newman_1988]
- [Schmidt and Newman 1990][research_schmidt_newman_1990]
- [Schmitt et al 1983][research_schmitt_destarac_1983]
- [Schneider][research_schneider]
- [Scholes and Slater 1970][research_scholes_slater_1970]
- [Schoneman 2019][research_schoneman_2019]
- [Schreyer et al 2026][research_schreyer_selm_2026]
- [Schröder and Meijering 2005][research_schroder_meijering_2005]
- [Schuelein 2008][research_schuelein_2008]
- [Schulze et al 2016][research_schulze_danowsky_2016]
- [Schumann et al 2025][research_schumann_wustenhagen_2025]
- [Schuster 1995][research_schuster_1995]
- [Schuster et al 1990][research_schuster_vadyak_1990]
- [Schuster, David M. and Byrd, James E. 2003][research_schusterdavidm_byrdjamese_2003]
- [Schuster, David M. and Edwards, John W. 2004][research_schusterdavidm_edwardsjohnw_2004]
- [Schwanz and Grimes 1980][research_schwanz_grimes_1980]
- [Schwanz and Wells 1980][research_schwanz_wells_1980]
- [Schweikert et al 2022][research_schweikert_patel_2022]
- [Schweikhard 1966][research_schweikhard_1966]
- [Schweikhard 1967][research_schweikhard_1967]
- [Schäck 2020][research_schack_2020]
- [Sclafani et al 2012][research_sclafani_slotnick_2012]
- [Scordamaglia et al 2025][research_scordamaglia_mattei_2025]
- [Scott et al 2008][research_scott_vetter_2008]
- [Scott et al 2011][research_scott_coulson_2011]
- [Scott et al 2015][research_scott_allen_2015]
- [Sebastia and Hornung 2023][research_sebastia_hornung_2023]
- [Sebastia et al 2024][research_sebastia_wurz_2024]
- [Sebastiano and Ricci 2013][research_sebastiano_ricci_2013]
- [Seber and Sakarya 2010][research_seber_sakarya_2010]
- [Seber and Sakarya 2011][research_seber_sakarya_2011]
- [Seebass 1982][research_seebass_1982]
- [Segawa and Gopalarathnam 2008][research_segawa_gopalarathnam_2008]
- [Segel 1952][research_segel_1952]
- [Seginer and Rose 1976][research_seginer_rose_1976]
- [Segui et al 2017][research_segui_gabor_2017]
- [Seidel et al 1985][research_seidel_sandford_1985]
- [Seiler et al 2012][research_seiler_balas_2012]
- [sekhar et al 2024][research_sekhar_suresh_2024]
- [Seki et al 2019][research_seki_tani_2019]
- [Selvadurai 1984][research_selvadurai_1984]
- [Selvam et al 2001][research_selvam_qu_2001]
- [Semionov and Kosinov 2007][research_semionov_kosinov_2007]
- [Sendner et al 2018][research_sendner_stahl_2018]
- [Serpieri and Kotsonis 2015][research_serpieri_kotsonis_2015]
- [Setoodeh et al 2005][research_setoodeh_abdallah_2005]
- [Sezgin and Krstic 2013][research_sezgin_krstic_2013]
- [Sha et al 2022][research_sha_sun_2022]
- [Shankar and Goebel 1985][research_shankar_goebel_1985]
- [Shankar and Malmuth 1982][research_shankar_malmuth_1982]
- [Shao et al 2024][research_shao_guo_2024]
- [Sharifi et al 2025][research_sharifi_vincenti_2025]
- [Sharma et al 2022][research_sharma_agrawal_2022]
- [Sharpe et al 2023][research_sharpe_ulker_2023]
- [Sharqi et al 2021][research_sharqi_cesnik_2021]
- [Shavezipur 2021][research_shavezipur_2021]
- [Shaw et al][research_shaw_hidalgo]
- [Shearwood et al 2020][research_shearwood_nabawy_2020]
- [Shearwood et al 2020][research_shearwood_nabawy_2020_b]
- [Shearwood et al 2023][research_shearwood_nabawy_2023]
- [Sheldon and Rasmussen][research_sheldon_rasmussen]
- [Shen et al 2019][research_shen_branscomb_2019]
- [Shen et al 2024][research_shen_li_2024]
- [Sheta 2000][research_sheta_2000]
- [Shevare and Arya 2012][research_shevare_arya_2012]
- [Shi and Song 2012][research_shi_song_2012]
- [Shi et al 2023][research_shi_wang_2023]
- [Shi et al 2023][research_shi_zuo_2023]
- [Shieh 1988][research_shieh_1988]
- [Shimin et al 2025][research_shimin_letian_2025]
- [Shipley and Gopalarathnam 2006][research_shipley_gopalarathnam_2006]
- [Shirk et al 1984][research_shirk_hertz_1984]
- [Shirk, M. H. et al 1986][research_shirkmh_hertztj_1986]
- [Shklovskii and Kurt 1961][research_shklovskii_kurt_1961]
- [Shmelоv et al 2019][research_shmelv_vladov_2019]
- [Shmilovich et al 2023][research_shmilovich_yadlin_2023]
- [Shmilovich et al 2026][research_shmilovich_yadlin_2026]
- [Shock location dominated transonic flight loads on the active aeroelastic wing][research_aaw_shock_loads]
- [Shu-yi et al 2010][research_shuyi_xin_2010]
- [Shubin 1995][research_shubin_1995]
- [Shukla and Patil 2015][research_shukla_patil_2015]
- [Shweyk and Weltz 2005][research_shweyk_weltz_2005]
- [Siebert et al 2026][research_siebert_strothteicher_2026]
- [Sieradzki 2016][research_sieradzki_2016]
- [Sigrest et al 2022][research_sigrest_wu_2022]
- [Siler et al 1997][research_siler_volk_1997]
- [Silva][research_silva]
- [Silva][research_silva_b]
- [Silva and Bennett 1995][research_silva_bennett_1995]
- [Silva et al 2006][research_silva_mello_2006]
- [Silva et al 2008][research_silva_mello_2008]
- [Silvestre 2013][research_silvestre_2013]
- [Simbuerger et al 2022][research_simbuerger_raveh_2022]
- [Simmons and Murphy 2021][research_simmons_murphy_2021]
- [Simmons et al 2025][research_simmons_riso_2025]
- [Simmons et al 2026][research_simmons_chang_2026]
- [Simoes et al 2009][research_simoes_alazard_2009]
- [Simpson 1972][research_simpson_1972]
- [Sims and Carter 1981][research_sims_carter_1981]
- [Simsek and Tekinalp 2015][research_simsek_tekinalp_2015]
- [Simulation and model reduction for the active flexible wing program][research_afw_simulation_reduction]
- [Simulation in support of 1988][research_simulation_in_1988]
- [Simões et al 2011][research_simoes_apkarian_2011]
- [Sinclair and Flowers 2010][research_sinclair_flowers_2010]
- [Singer 1956][research_singer_1956]
- [Singh and Brenner 2003][research_singh_brenner_2003]
- [Singh and Friedmann 2020][research_singh_friedmann_2020]
- [Singh and Friedmann 2021][research_singh_friedmann_2021]
- [Singh and Venkatraman 2023][research_singh_venkatraman_2023]
- [Singh and Wang 2002][research_singh_wang_2002]
- [Singh et al 2010][research_singh_mcdonough_2010]
- [Singh et al 2014][research_singh_mcdonough_2014]
- [Singh et al 2015][research_singh_brown_2015]
- [Singh et al 2016][research_singh_brown_2016]
- [Singh et al 2024][research_singh_kumari_2024]
- [Singha 2025][research_singha_2025]
- [Singha and Murugan 2023][research_singha_murugan_2023]
- [Sinha and Ananthkrishnan 2002][research_sinha_ananthkrishnan_2002]
- [Sinske et al 2018][research_sinske_govers_2018]
- [Sivanandi et al 2022][research_sivanandi_gupta_2022]
- [Sivanandi et al 2024][research_sivanandi_gupta_2024]
- [Skillen and Crossley 2005][research_skillen_crossley_2005]
- [Skinner and Zare-Behtash 2018][research_skinner_zarebehtash_2018]
- [Slaby and Smith 2011][research_slaby_smith_2011]
- [Slater 1985][research_slater_1985]
- [Slender Aircraft for Flight 2012][research_slender_aircraft_2012]
- [Smith 2025][research_smith_2025]
- [Smith and Dahlem 1981][research_smith_dahlem_1981]
- [Smith and Shyy 1995][research_smith_shyy_1995]
- [Smith et al 2001][research_smith_patil_2001]
- [Smith et al 2003][research_smith_moes_2003]
- [Smith, Benjamin et al 2020][research_smithbenjamin_brookstimothy_2020]
- [Smith, John W. et al 1992][research_smithjohnw_lockwiltonp_1992]
- [Sneshko et al 2005][research_sneshko_chetvergov_2005]
- [Soares 2007][research_soares_2007]
- [Soares 2007][research_soares_2007_b]
- [Socha and Izydorczyk 2024][research_socha_izydorczyk_2024]
- [Sodja et al 2018][research_sodja_werter_2018]
- [Sodja et al 2021][research_sodja_werter_2021]
- [Sohn et al 2006][research_sohn_chung_2006]
- [Sohn et al 2007][research_sohn_chung_2007]
- [Soinne 1999][research_soinne_1999]
- [Solano et al 2020][research_solano_sarojini_2020]
- [Solarte-Pineda et al 2026][research_solartepineda_bravomosquera_2026]
- [Soneda et al 2020][research_soneda_yokozeki_2020]
- [Soneda et al 2026][research_soneda_tsushima_2026]
- [Song and Kim 2009][research_song_kim_2009]
- [Song et al 1992][research_song_librescu_1992]
- [Song et al 2010][research_song_wu_2010]
- [Song et al 2014][research_song_liu_2014]
- [Song et al 2014][research_song_yang_2014]
- [Song et al 2018][research_song_whidborne_2018]
- [Song et al 2025][research_song_zhang_2025]
- [Soovere 1981][research_soovere_1981]
- [Sorensen and Bencze 1974][research_sorensen_bencze_1974]
- [Sorensen and Smeltzer 1972][research_sorensen_smeltzer_1972]
- [Sotoudeh 2014][research_sotoudeh_2014]
- [Sotoudeh 2015][research_sotoudeh_2015]
- [Sotoudeh and Ferman 2019][research_sotoudeh_ferman_2019]
- [Sotoudeh and Hosking 2018][research_sotoudeh_hosking_2018]
- [Sotoudeh et al 2010][research_sotoudeh_hodges_2010]
- [Soykasap and Hodges 1999][research_soykasap_hodges_1999]
- [Soykasap and Hodges 2000][research_soykasap_hodges_2000]
- [Space environment natural and][research_space_environment]
- [Spada et al 2017][research_spada_afonso_2017]
- [Spaid 1984][research_spaid_1984]
- [Spangler, Jr. and Jacques 1999][research_spanglerjr_jacques_1999]
- [Spearman 1979][research_spearman_1979]
- [Spearman et al 1992][research_spearman_tice_1992]
- [Spinner and Rudnik 2023][research_spinner_rudnik_2023]
- [Squires 2004][research_squires_2004]
- [Sreenivasulu et al 2025][research_sreenivasulu_neelapu_2025]
- [Srinathkumar and Adams, Jr. 1989][research_srinathkumar_adamsjr_1989]
- [Srinivas and Chopra 1998][research_srinivas_chopra_1998]
- [Srivathsan and Rauleder 2023][research_srivathsan_rauleder_2023]
- [Stacey and Thomas 2019][research_stacey_thomas_2019]
- [Staley 1976][research_staley_1976]
- [Stalford 1980][research_stalford_1980]
- [Stalford 1981][research_stalford_1981]
- [Stalla et al 2024][research_stalla_kier_2024]
- [Stalla et al 2026][research_stalla_looye_2026]
- [Stam and de Visser 2025][research_stam_devisser_2025]
- [Stamatellou and Kalfas 2021][research_stamatellou_kalfas_2021]
- [Standard Atmosphere][research_standard_atmosphere]
- [Standard Atmosphere 2005][research_standard_atmosphere_2005]
- [Standard atmosphere 2007][research_standard_atmosphere_2007]
- [Standard Atmosphere 2023][research_standard_atmosphere_2023]
- [Standard Atmosphere 2024][research_standard_atmosphere_2024]
- [Standard atmosphere chart 1927][research_standard_atmosphere_1927]
- [Standard atmosphere chart supersedes 1927][research_standard_atmosphere_1927_b]
- [Standard Atmosphere Data 1992][research_standard_atmosphere_1992]
- [standard atmosphere for preconditioning 2021][research_standard_atmosphere_2021]
- [standard atmosphere for testing 2021][research_standard_atmosphere_2021_b]
- [Standard Atmospheric Profilesa aSource 2002][research_standard_atmospheric_2002]
- [Stanewsky and Basler 1989][research_stanewsky_basler_1989]
- [Stanford 2014][research_stanford_2014]
- [Stanford 2015][research_stanford_2015]
- [Stanford 2016][research_stanford_2016]
- [Stanford 2016][research_stanford_2016_b]
- [Stanford 2018][research_stanford_2018]
- [Stanford 2019][research_stanford_2019]
- [Stanford 2020][research_stanford_2020]
- [Stanford 2021][research_stanford_2021]
- [Stanford and Beran 2011][research_stanford_beran_2011]
- [Stanford and Dunning 2015][research_stanford_dunning_2015]
- [Stanford and Jacobson 2023][research_stanford_jacobson_2023]
- [Stanford, Bret K. and Jutte, Christine V. 2014][research_stanfordbretk_juttechristinev_2014]
- [Stange 1959][research_stange_1959]
- [Starodub 2026][research_starodub_2026]
- [Starr et al 2011][research_starr_olds_2011]
- [Static Aeroelastic Considerations 1996][research_static_aeroelastic_1996]
- [Static Aeroelasticity 2002][research_static_aeroelasticity_2002]
- [Static Aeroelasticity 2005][research_static_aeroelasticity_2005]
- [Static Aeroelasticity 2011][research_static_aeroelasticity_2011]
- [Static Aeroelasticity and Flutter 2014][research_static_aeroelasticity_2014_c]
- [Static Aeroelasticity Effect 2014][research_static_aeroelasticity_2014]
- [Static Aeroelasticity Effect 2014][research_static_aeroelasticity_2014_b]
- [Static Longitudinal Stability Flight 2003][research_static_longitudinal_2003]
- [Steer 2003][research_steer_2003]
- [Steer 2004][research_steer_2004]
- [Steger and Bailey 1979][research_steger_bailey_1979]
- [Steger and Bailey 1980][research_steger_bailey_1980]
- [Steimle et al 2008][research_steimle_schroder_2008]
- [Stengel 1969][research_stengel_1969]
- [Stengel 1983][research_stengel_1983]
- [Stepanova 2025][research_stepanova_2025]
- [Stephan 2025][research_stephan_2025]
- [Stettner 2000][research_stettner_2000]
- [Stettner and Schrage 1992][research_stettner_schrage_1992]
- [Stevenson 1991][research_stevenson_1991]
- [Stewart and Bauer 1983][research_stewart_bauer_1983]
- [Stiharu-Alexe 1991][research_stiharualexe_1991]
- [Stiharu-Alexe et al][research_stiharualexe_oshea]
- [Stodieck et al 2013][research_stodieck_cooper_2013]
- [Stodieck et al 2014][research_stodieck_cooper_2014]
- [Stodieck et al 2015][research_stodieck_cooper_2015]
- [Stodieck et al 2017][research_stodieck_cooper_2017]
- [Stougie et al 2024][research_stougie_pollack_2024]
- [Strain gage loads calibration testing of the active aeroelastic wing F/A-18 aircraft][research_strain_gage_calibration]
- [Strain Gauge Bonding Service 1975][research_strain_gauge_1975]
- [Strain Gauge Specifications 1967][research_strain_gauge_1967]
- [Strain Gauge Symposium and 1965][research_strain_gauge_1965]
- [Strand and Ennis 2012][research_strand_ennis_2012]
- [Strand and Levinsky 1969][research_strand_levinsky_1969]
- [Strang 1943][research_strang_1943]
- [Streett 1981][research_streett_1981]
- [Streitenberger and Feldwisch 2025][research_streitenberger_feldwisch_2025]
- [Strelkov and Kharlamov 1967][research_strelkov_kharlamov_1967]
- [Strganac 2007][research_strganac_2007]
- [Striz et al 1991][research_striz_eastep_1991]
- [Strothteicher and Fezans 2026][research_strothteicher_fezans_2026]
- [Structural weight comparison of 1981][research_structural_weight_1981]
- [Su 2015][research_su_2015]
- [Su and Cesnik 2009][research_su_cesnik_2009]
- [Su and Cesnik 2010][research_su_cesnik_2010]
- [Su et al 2017][research_su_huang_2017]
- [Su et al 2018][research_su_wang_2018]
- [Su et al 2023][research_su_sun_2023]
- [Subramanya and Prasad 2013][research_subramanya_prasad_2013]
- [Sudhi et al 2021][research_sudhi_radespiel_2021]
- [Suh, Peter M. et al 2015][research_suhpeterm_conyershowardjason_2015]
- [Sulaeman et al 2017][research_sulaeman_abdullah_2017]
- [Suleman 2007][research_suleman_2007]
- [Suleman and Costa 2004][research_suleman_costa_2004]
- [Suleman and Moniz][research_suleman_moniz]
- [Suleman et al 2000][research_suleman_crawford_2000]
- [Suleman et al 2002][research_suleman_crawford_2002]
- [Suleman et al 2016][research_suleman_afonso_2016]
- [Summary of an active flexible wing program][research_afw_technology_summary]
- [Sun 2024][research_sun_2024]
- [Sun and Bai 2014][research_sun_bai_2014]
- [Sun and Hu 2005][research_sun_hu_2005]
- [Sun et al 2018][research_sun_schilder_2018]
- [Sun et al 2020][research_sun_shi_2020]
- [Sun et al 2021][research_sun_zhou_2021]
- [Sundaram and Wu 1983][research_sundaram_wu_1983]
- [Sungpil Yang et al 2016][research_sungpilyang_hashemi_2016]
- [Supersonic Aircraft High-Speed Civil 1997][research_supersonic_aircraft_1997]
- [Supersonic Three-dimensional Wing Theory 1960][research_supersonic_three_dimensional_1960]
- [Supersonic transport wing minimum 1992][research_supersonic_transport_1992]
- [Suresh et al 2010][research_suresh_radhakrishnan_2010]
- [Suryakumar et al 2016][research_suryakumar_mangalam_2016]
- [Suzuki 1990][research_suzuki_1990]
- [Suzuki and Matsuda 1991][research_suzuki_matsuda_1991]
- [Suzuki and Yonezawa 1993][research_suzuki_yonezawa_1993]
- [Svec 1981][research_svec_1981]
- [Svendsen 1994][research_svendsen_1994]
- [Svoboda and Hromcik 2019][research_svoboda_hromcik_2019]
- [Svoboda et al 2018][research_svoboda_hromcik_2018]
- [Svoboda et al 2021][research_svoboda_hromcik_2021]
- [Svoboda et al 2023][research_svoboda_hengstermovric_2023]
- [Swaim][research_swaim]
- [Swaim 1961][research_swaim_1961]
- [Swaim 1983][research_swaim_1983]
- [Syed et al 2022][research_syed_moshtaghzadeh_2022]
- [Sykes][research_sykes]
- [Szabolcsi and Gáspár 1997][research_szabolcsi_gaspar_1997]
- [Szema and Shankar 1984][research_szema_shankar_1984]
- [Szollosi and Baranyi 2016][research_szollosi_baranyi_2016]
- [Szymanski et al 2025][research_szymanski_alstrom_2025]
- [Szymanski et al 2025][research_szymanski_ghazi_2025]
- [Sóbester 2021][research_sobester_2021]
- [Tabassum and Bai 2022][research_tabassum_bai_2022]
- [Tacca et al 2024][research_tacca_colvin_2024]
- [Tadi 2003][research_tadi_2003]
- [Taflan et al 2023][research_taflan_smith_2023]
- [Taflan et al 2023][research_taflan_smith_2023_b]
- [Taha et al 2011][research_taha_tang_2011]
- [Tai et al 2023][research_tai_wang_2023]
- [Tai et al 2023][research_tai_wang_2023_b]
- [Takahashi et al 2016][research_takahashi_yokozeki_2016]
- [Takarics et al 2018][research_takarics_vanek_2018]
- [Tal and Nguyen 2015][research_tal_nguyen_2015]
- [Tamayama 2017][research_tamayama_2017]
- [Tamayama et al 2003][research_tamayama_kheirandish_2003]
- [Tamura and Yumitori 2024][research_tamura_yumitori_2024]
- [Tang and Dowell 1996][research_tang_dowell_1996]
- [Tang and Dowell 1998][research_tang_dowell_1998]
- [Tang and Dowell 2001][research_tang_dowell_2001]
- [Tang and Dowell 2013][research_tang_dowell_2013]
- [Tang et al 2000][research_tang_kholodar_2000]
- [Tang et al 2015][research_tang_wu_2015]
- [Tang et al 2016][research_tang_wu_2016]
- [Tang et al 2017][research_tang_chen_2017]
- [Tang et al 2025][research_tang_yang_2025]
- [Tani 1992][research_tani_1992]
- [Tani et al 2018][research_tani_seki_2018]
- [Tantaroudas and Da Ronch 2017][research_tantaroudas_daronch_2017]
- [Tantaroudas and Karachalios 2026][research_tantaroudas_karachalios_2026]
- [Tantrairatn and Veres 2015][research_tantrairatn_veres_2015]
- [Tao and Bin 2026][research_tao_bin_2026]
- [Taraborrelli 2023][research_taraborrelli_2023]
- [Taranto and Abdulrahim 2023][research_taranto_abdulrahim_2023]
- [Tariq and Nahon 2020][research_tariq_nahon_2020]
- [Tartabini et al 2016][research_tartabini_gilbert_2016]
- [Taylor 1959][research_taylor_1959]
- [Taylor 2012][research_taylor_2012]
- [Taylor and Yoo 2011][research_taylor_yoo_2011]
- [Taylor et al 1992][research_taylor_bennett_1992]
- [Taylor et al 1995][research_taylor_pratt_1995]
- [Taylor et al 2007][research_taylor_gaitonde_2007]
- [Technical applications for an 1976][research_technical_applications_1976]
- [Tegelaar 1984][research_tegelaar_1984]
- [Teixeira and Cesnik 2020][research_teixeira_cesnik_2020]
- [Tekawade et al 2024][research_tekawade_chandwadkar_2024]
- [Teng 2006][research_teng_2006]
- [Teng 2007][research_teng_2007]
- [Teng and Chen 2006][research_teng_chen_2006]
- [Teng and Fan 2025][research_teng_fan_2025]
- [Terilli et al 2025][research_terilli_bueno_2025]
- [Tewari 1998][research_tewari_1998]
- [Tewari 1999][research_tewari_1999]
- [Tewari 2001][research_tewari_2001]
- [Tewari 2009][research_tewari_2009]
- [Tewari 2015][research_tewari_2015]
- [Tewari 2015][research_tewari_2015_b]
- [Tewari 2015][research_tewari_2015_c]
- [Tewari 2016][research_tewari_2016]
- [Thapa Magar et al 2018][research_thapamagar_pankonien_2018]
- [Tharayil and Alleyne 2001][research_tharayil_alleyne_2001]
- [Tharayil and Alleyne 2004][research_tharayil_alleyne_2004]
- [The active flexible wing aeroservoelastic wind-tunnel test program][research_afw_wind_tunnel]
- [The development of a lateral-control system for use with large-span flaps][research_lateral_control_large_flaps]
- [The effect of elastic 1969][research_the_effect_1969]
- [The Effects of Leading 2007][research_the_effects_2007]
- [The F-18 high alpha research vehicle, a high-angle-of-attack testbed aircraft][research_harv_testbed]
- [The Flight Environment Standard 2021][research_the_flight_2021]
- [The Geometry of Control 2016][research_the_geometry_2016]
- [The influence of the aerodynamic span effect on the magnitude of the torsional-divergence velocity][research_span_effect_divergence]
- [The International Standard Atmosphere 2017][research_the_international_2017]
- [The international standard atmosphere 2026][research_the_international_2026]
- [The Saunders-Roe Technograph Foil 1952][research_the_saunders_roe_1952]
- [The Standard Atmosphere 1964][research_the_standard_1964]
- [The Standard Atmosphere 1976][research_the_standard_1976]
- [Theis et al 2015][research_theis_pfifer_2015]
- [Theis et al 2015][research_theis_takarics_2015]
- [Theis et al 2016][research_theis_pfifer_2016]
- [Theis et al 2020][research_theis_pfifer_2020]
- [Thel et al 2022][research_thel_hahn_2022]
- [Thielicke and Stamhuis 2018][research_thielicke_stamhuis_2018]
- [Thienel et al 1998][research_thienel_lewis_1998]
- [Thomas and Holst 1983][research_thomas_holst_1983]
- [Thomas and Shkarayev 2026][research_thomas_shkarayev_2026]
- [Thompson et al 2007][research_thompson_klyde_2007]
- [Thompson et al 2011][research_thompson_danowsky_2011]
- [Thomson 1946][research_thomson_1946]
- [Three-dimensional boundary-layer transition on 1994][research_three_dimensional_boundary_layer_1994]
- [Thuwis et al][research_thuwis_debreuker]
- [Thuwis et al 2009][research_thuwis_debreuker_2009]
- [Tian et al 2016][research_tian_yang_2016]
- [Tian et al 2026][research_tian_li_2026]
- [Tian et al 2026][research_tian_wang_2026]
- [Tijdeman et al 1979][research_tijdeman_vannunen_1979]
- [Tijdeman et al 1979][research_tijdeman_vannunen_1979_b]
- [Tillotson and Fuhs 1982][research_tillotson_fuhs_1982]
- [Ting et al 2014][research_ting_lebofsky_2014]
- [Ting et al 2017][research_ting_chaparro_2017]
- [Ting et al 2022][research_ting_mesbahi_2022]
- [Ting et al 2023][research_ting_mesbahi_2023]
- [Ting et al 2026][research_ting_berg_2026]
- [Tingting and Aijun 2014][research_tingting_aijun_2014]
- [Tiomkin and Raveh 2021][research_tiomkin_raveh_2021]
- [Tischler 2018][research_tischler_2018]
- [Tischler and Hoh 1982][research_tischler_hoh_1982]
- [Tischler and Venkayya 1998][research_tischler_venkayya_1998]
- [Tischler and Zivan 2007][research_tischler_zivan_2007]
- [Tischler et al 2000][research_tischler_venkayya_2000]
- [Toffol 2023][research_toffol_2023]
- [Toffol 2024][research_toffol_2024]
- [Toffol and Ricci 2023][research_toffol_ricci_2023]
- [Tohidi et al 2018][research_tohidi_yildiz_2018]
- [Toker and Ozbay][research_toker_ozbay]
- [Tol et al 2014][research_tol_devisser_2014]
- [Tomaine, R. L. et al 1978][research_tomainerl_bryantwh_1978]
- [Torenbeek 1972][research_torenbeek_1972]
- [Torok 1996][research_torok_1996]
- [Torralba et al 2009][research_torralba_puyou_2009]
- [Torrigiani and Berci 2021][research_torrigiani_berci_2021]
- [Torsional Divergence 2014][research_torsional_divergence_2014]
- [Torsional stiffness and fatigue 1994][research_torsional_stiffness_1994]
- [Torsional stiffness of plastic 1972][research_torsional_stiffness_1972]
- [Traas et al 2026][research_traas_atmaca_2026]
- [Tracy 1981][research_tracy_1981]
- [Tracy and Chopra 1998][research_tracy_chopra_1998]
- [Trame et al 1985][research_trame_williams_1985]
- [Trankle and Bachner 1993][research_trankle_bachner_1993]
- [Transonic Aircraft Configurations 2012][research_transonic_aircraft_2012]
- [Transonic and supersonic flight 1992][research_transonic_and_1992]
- [Transonic Maneuver/Cruise Airfoil Design 1980][research_transonic_maneuver_cruise_1980]
- [Transonic Wing Shape Design 2015][research_transonic_wing_2015]
- [Transonic, Shock, and Multidimensional 1982][research_transonic_shock_1982]
- [Travassos and Kaufman 1979][research_travassos_kaufman_1979]
- [Trenka 1971][research_trenka_1971]
- [Triplett 1972][research_triplett_1972]
- [Triplett 1979][research_triplett_1979]
- [Triplett 1980][research_triplett_1980]
- [Triplett 1980][research_triplett_1980_b]
- [Triplett and Ising 1971][research_triplett_ising_1971]
- [Triplett et al 1973][research_triplett_kappus_1973]
- [Truong et al 2022][research_truong_gosselin_2022]
- [Tsonev and Kuzmanov 2022][research_tsonev_kuzmanov_2022]
- [Tsushima et al 2018][research_tsushima_arizono_2018]
- [Tsushima et al 2018][research_tsushima_yokozeki_2018]
- [Tsushima et al 2019][research_tsushima_yokozeki_2019]
- [Tsushima et al 2025][research_tsushima_soneda_2025]
- [Tucker Harvey et al 2020][research_tuckerharvey_khovanov_2020]
- [Tucker, Warren A and Nelson, Robert L 1950][research_tuckerwarrena_nelsonrobertl_1950]
- [Tung et al 1996][research_tung_yu_1996]
- [Turi and Rankin 1988][research_turi_rankin_1988]
- [Turner et al 2025][research_turner_seo_2025]
- [Turns and Kraige][research_turns_kraige]
- [Tursi 2003][research_tursi_2003]
- [Tuzcu and Nguyen 2010][research_tuzcu_nguyen_2010]
- [Twist model development and results from the active aeroelastic wing F/A-18 aircraft][research_aaw_twist_model]
- [Tırman et al 2024][research_tirman_ture_2024]
- [U. P. V. et al 2025][research_upv_deodhare_2025]
- [Uhm 2021][research_uhm_2021]
- [Ulbrich 2011][research_ulbrich_2011]
- [Ulbrich 2024][research_ulbrich_2024]
- [Ulker et al 2012][research_ulker_nitzsche_2012]
- [Ullah et al 2021][research_ullah_lutz_2021]
- [Ullah et al 2022][research_ullah_kamoun_2022]
- [Ullah et al 2023][research_ullah_lutz_2023]
- [Unsteady Aerodynamics and Flutter 2006][research_unsteady_aerodynamics_2006]
- [Upper Atmosphere Re-Entry Study 1961][research_upper_atmosphere_1961]
- [Uppoor and Chopra 2026][research_uppoor_chopra_2026]
- [Urnes et al 2008][research_urnes_reichenbach_2008]
- [Urnes, James, Sr. et al 2013][research_urnesjamessr_nguyennhan_2013]
- [US Standard Atmosphere Model 2014][research_us_standard_2014]
- [Uzun and Malik 2018][research_uzun_malik_2018]
- [Uzun and Malik 2019][research_uzun_malik_2019]
- [Vadyak et al 1987][research_vadyak_smith_1987]
- [Vale et al 2011][research_vale_leite_2011]
- [Van Gaasbeek 1980][research_vangaasbeek_1980]
- [Van Graas et al 1994][research_vangraas_diggle_1994]
- [Van Pelt 1981][research_vanpelt_1981]
- [van Schoor and von Flotow 1990][research_vanschoor_vonflotow_1990]
- [Van Wyckhouse 1966][research_vanwyckhouse_1966]
- [Van Zyl 2001][research_vanzyl_2001]
- [Vance et al 1974][research_vance_brown_1974]
- [Vandierendonck 1973][research_vandierendonck_1973]
- [Vanwalleghem et al 2015][research_vanwalleghem_debaere_2015]
- [Varello et al 2013][research_varello_lamberti_2013]
- [Variation of natural radioactivity 1956][research_variation_of_1956]
- [Vartio et al 2005][research_vartio_shimko_2005]
- [Vartio et al 2008][research_vartio_shaw_2008]
- [Vaughan 2003][research_vaughan_2003]
- [Vaughn, Jr. 1982][research_vaughnjr_1982]
- [Veiberman and Karpel 2022][research_veiberman_karpel_2022]
- [Veiberman et al 2016][research_veiberman_weiss_2016]
- [Veley et al 2008][research_veley_khot_2008]
- [Velkova 2017][research_velkova_2017]
- [Vepa 2007][research_vepa_2007]
- [Vepa 2007][research_vepa_2007_b]
- [Verhaegen 1987][research_verhaegen_1987]
- [Vernon 1993][research_vernon_1993]
- [Verri et al 2024][research_verri_luizbussamra_2024]
- [Verri et al 2025][research_verri_desilvabussamra_2025]
- [Verstraete et al 2019][research_verstraete_roccia_2019]
- [Verstynen, Jr. 1974][research_verstynenjr_1974]
- [Vile et al 2019][research_vile_alwi_2019]
- [Vile et al 2019][research_vile_alwi_2019_b]
- [Vile et al 2020][research_vile_alwi_2020]
- [Vincent and Botez 2015][research_vincent_botez_2015]
- [Vincent and Franklin 1981][research_vincent_franklin_1981]
- [Vindigni 2023][research_vindigni_2023]
- [Vindigni 2024][research_vindigni_2024]
- [Vindigni et al 2024][research_vindigni_mantegna_2024]
- [Vindigni et al 2024][research_vindigni_mantegna_2024_b]
- [Vindigni et al 2026][research_vindigni_mantegna_2026]
- [Virgilio Pereira et al 2019][research_virgiliopereira_kolmanovsky_2019]
- [Virgilio Pereira et al 2019][research_virgiliopereira_kolmanovsky_2019_b]
- [Volk et al 1998][research_volk_siler_1998]
- [Volobuyev et al 2017][research_volobuyev_gorbushin_2017]
- [Von Flotow 1989][research_vonflotow_1989]
- [Voracek and Clarke 1991][research_voracek_clarke_1991]
- [Voracek et al 2002][research_voracek_reaves_2002]
- [Vos et al 2007][research_vos_hodigeresiddaramaiah_2007]
- [Voskuijl et al 2008][research_voskuijl_walker_2008]
- [Vu][research_vu]
- [Vu et al 2005][research_vu_kelkar_2005]
- [Vukasinovic et al 2013][research_vukasinovic_gissen_2013]
- [Wada et al 2020][research_wada_tamayama_2020]
- [Waggoner 1980][research_waggoner_1980]
- [Waggoner 1982][research_waggoner_1982]
- [Wagner 1983][research_wagner_1983]
- [Wahler et al 2023][research_wahler_varriale_2023]
- [Waite et al 2019][research_waite_stanford_2019]
- [Waite et al 2019][research_waite_stanford_2019_b]
- [Waite et al 2020][research_waite_bartels_2020]
- [Waite et al 2021][research_waite_grauer_2021]
- [Waitman and Marcos 2020][research_waitman_marcos_2020]
- [Walendziuk 2018][research_walendziuk_2018]
- [Wales et al 2015][research_wales_cheung_2015]
- [Walker and Aglietti 2007][research_walker_aglietti_2007]
- [Walker and Postlthewaite][research_walker_postlthewaite]
- [Wall et al 2024][research_wall_amoozgar_2024]
- [Wallace 1952][research_wallace_1952]
- [Wallace 1978][research_wallace_1978]
- [Wallace 2000][research_wallace_2000]
- [Wan et al 2003][research_wan_yang_2003]
- [Wan Kim and Cho 2008][research_wankim_cho_2008]
- [Wang 2019][research_wang_2019]
- [Wang and Guo 2012][research_wang_guo_2012]
- [Wang and Iliff 2004][research_wang_iliff_2004]
- [Wang et al 1986][research_wang_demiroz_1986]
- [Wang et al 2012][research_wang_xargay_2012]
- [Wang et al 2018][research_wang_vankampen_2018]
- [Wang et al 2018][research_wang_wynn_2018]
- [Wang et al 2018][research_wang_zhang_2018]
- [Wang et al 2019][research_wang_tang_2019]
- [Wang et al 2019][research_wang_vankampen_2019]
- [Wang et al 2019][research_wang_wan_2019]
- [Wang et al 2019][research_wang_wan_2019_b]
- [Wang et al 2019][research_wang_yang_2019]
- [Wang et al 2021][research_wang_chang_2021]
- [Wang et al 2021][research_wang_hou_2021]
- [Wang et al 2021][research_wang_mkhoyan_2021]
- [Wang et al 2021][research_wang_mkhoyan_2021_b]
- [Wang et al 2021][research_wang_wan_2021]
- [Wang et al 2021][research_wang_wu_2021]
- [Wang et al 2022][research_wang_tai_2022]
- [Wang et al 2022][research_wang_zhao_2022]
- [Wang et al 2023][research_wang_chen_2023]
- [Wang et al 2023][research_wang_lei_2023]
- [Wang et al 2023][research_wang_xing_2023]
- [Wang et al 2024][research_wang_li_2024]
- [Wang et al 2024][research_wang_wang_2024]
- [Wang et al 2024][research_wang_zhao_2024]
- [Wang et al 2025][research_wang_chen_2025]
- [Wang et al 2025][research_wang_hu_2025]
- [Wang et al 2025][research_wang_li_2025]
- [Wang et al 2025][research_wang_xu_2025]
- [Wang et al 2025][research_wang_yu_2025]
- [Wang et al 2026][research_wang_chen_2026]
- [Wang et al 2026][research_wang_hu_2026]
- [Wang et al 2026][research_wang_pei_2026]
- [Wang et al 2026][research_wang_pei_2026_b]
- [Wansasueb et al 2023][research_wansasueb_panagant_2023]
- [Ward 1949][research_ward_1949]
- [Ward 1988][research_ward_1988]
- [Warwick et al 2019][research_warwick_bras_2019]
- [Wasmi et al 2015][research_wasmi_hasan_2015]
- [Wasson and Mehus 1967][research_wasson_mehus_1967]
- [Waszak 1996][research_waszak_1996]
- [Waszak 2001][research_waszak_2001]
- [Waszak and Buttrill 1991][research_waszak_buttrill_1991]
- [Waszak and Schmidt 1988][research_waszak_schmidt_1988]
- [Waszak and Srinathkumar 1991][research_waszak_srinathkumar_1991]
- [Waszak and Srinathkumar 1992][research_waszak_srinathkumar_1992]
- [Waszak and Srinathkumar 1995][research_waszak_srinathkumar_1995]
- [Waszak et al 2002][research_waszak_davidson_2002]
- [Watts 1976][research_watts_1976]
- [Webb and Takahashi 2022][research_webb_takahashi_2022]
- [Weed et al 1983][research_weed_carlson_1983]
- [Wei and Zhang 2024][research_wei_zhang_2024]
- [Wei et al 2018][research_wei_zhao_2018]
- [Wei et al 2022][research_wei_lin_2022]
- [weibing and Kuisheng 2006][research_weibing_kuisheng_2006]
- [Weinstein et al 2018][research_weinstein_hubbard_2018]
- [Weiss 1983][research_weiss_1983]
- [Weiss and Thielecke 2000][research_weiss_thielecke_2000]
- [Weisshaar 1973][research_weisshaar_1973]
- [Weisshaar 1974][research_weisshaar_1974]
- [Weisshaar 1974][research_weisshaar_1974_b]
- [Weisshaar 1977][research_weisshaar_1977]
- [Weisshaar 1978][research_weisshaar_1978]
- [Weisshaar 1979][research_weisshaar_1979]
- [Weisshaar 1980][research_weisshaar_1980]
- [Weisshaar 1981][research_weisshaar_1981]
- [Weisshaar 1985][research_weisshaar_1985]
- [Weisshaar 1987][research_weisshaar_1987]
- [Weisshaar 1990][research_weisshaar_1990]
- [Weisshaar 1990][research_weisshaar_1990_b]
- [Weisshaar 1994][research_weisshaar_1994]
- [Weisshaar 1994][research_weisshaar_1994_b]
- [Weisshaar 2010][research_weisshaar_2010]
- [Weisshaar and Ashley 1974][research_weisshaar_ashley_1974]
- [Weisshaar and Duke 2006][research_weisshaar_duke_2006]
- [Weisshaar and Lee 2002][research_weisshaar_lee_2002]
- [Weisshaar and Nam 1990][research_weisshaar_nam_1990]
- [Weisshaar and Ryan 1984][research_weisshaar_ryan_1984]
- [Weisshaar, T. A. 1983][research_weisshaarta_1983]
- [Weisshaar, Terrence A. and Changho, Nam 1989][research_weisshaarterrencea_changhonam_1989]
- [Wells 2017][research_wells_2017]
- [Wells and Keskar 1979][research_wells_keskar_1979]
- [Wells et al 1981][research_wells_banda_1981]
- [Wells et al 1982][research_wells_banda_1982]
- [Werner 2018][research_werner_2018]
- [Werter and De Breuker 2016][research_werter_debreuker_2016]
- [Wheatcroft et al 2025][research_wheatcroft_groh_2025]
- [Whitbeck and Hofmann 1978][research_whitbeck_hofmann_1978]
- [Whitbeck et al 1982][research_whitbeck_smith_1982]
- [White 1963][research_white_1963]
- [White 1970][research_white_1970]
- [White 1971][research_white_1971]
- [White 1973][research_white_1973]
- [White and Hartl 2024][research_white_hartl_2024]
- [Whitford 1991][research_whitford_1991]
- [Wieland 2025][research_wieland_2025]
- [Wieseman et al 1995][research_wieseman_hoadley_1995]
- [Wieseman et al 2005][research_wieseman_silva_2005]
- [Wilcox and Brenner 2011][research_wilcox_brenner_2011]
- [Wilde et al 2001][research_wilde_omenzetter_2001]
- [Wildschek et al 2006][research_wildschek_maier_2006]
- [Wildschek et al 2009][research_wildschek_maier_2009]
- [Wildschek et al 2013][research_wildschek_hanis_2013]
- [Williams 1965][research_williams_1965]
- [Williams 2004][research_williams_2004]
- [Williams and Hunt 1980][research_williams_hunt_1980]
- [Williams-Hayes 2005][research_williamshayes_2005]
- [Wilson][research_wilson]
- [Wilson et al 1993][research_wilson_riley_1993]
- [Wilson et al 2016][research_wilson_ryan_2016]
- [Wimpress and Swihart 1964][research_wimpress_swihart_1964]
- [Wing Buffeting Control at 2018][research_wing_buffeting_2018]
- [Wing Theory in Supersonic 1969][research_wing_theory_1969]
- [Wing torsional stiffness tests of the active aeroelastic wing F/A-18 airplane][research_aaw_torsional_stiffness]
- [Wingrove, R. C. 1978][research_wingroverc_1978]
- [Winograd and Miles 1956][research_winograd_miles_1956]
- [Winters et al 1991][research_winters_hassan_1991]
- [Winther et al 1993][research_winther_hagemeyer_1993]
- [Wolf and Bossert 2001][research_wolf_bossert_2001]
- [Wolfson 2009][research_wolfson_2009]
- [Wood and Buffano 1964][research_wood_buffano_1964]
- [Wood and Miller 1985][research_wood_miller_1985]
- [Wood et al 1999][research_wood_loth_1999]
- [Woodrow et al 2013][research_woodrow_tischler_2013]
- [Woodruff 2009][research_woodruff_2009]
- [Woods et al 1989][research_woods_gilbert_1989]
- [Woods et al 1990][research_woods_gilbert_1990]
- [Woods-Vedeler and Pototzky 1992][research_woodsvedeler_pototzky_1992]
- [Woods-Vedeler et al 1995][research_woodsvedeler_pototzky_1995]
- [Woods-Vedeler, Jessica A. et al 1994][research_woodsvedelerjessicaa_pototzkyanthonys_1994]
- [Woodward 1962][research_woodward_1962]
- [Woolf 2012][research_woolf_2012]
- [Wright and Silva 2026][research_wright_silva_2026]
- [Wu and Cooper 2016][research_wu_cooper_2016]
- [Wu and Livne 2015][research_wu_livne_2015]
- [Wu and Livne 2016][research_wu_livne_2016]
- [Wu et al 2021][research_wu_zhang_2021]
- [Wu et al 2022][research_wu_dai_2022]
- [Wu et al 2024][research_wu_li_2024]
- [Wu et al 2024][research_wu_zhou_2024]
- [Wu et al 2025][research_wu_li_2025]
- [Wuestenhagen 2022][research_wuestenhagen_2022]
- [Wuestenhagen 2023][research_wuestenhagen_2023]
- [Wuestenhagen et al 2018][research_wuestenhagen_kier_2018]
- [Wuestenhagen et al 2018][research_wuestenhagen_kier_2018_b]
- [Wunderlich 2015][research_wunderlich_2015]
- [Wunderlich and Dähne 2017][research_wunderlich_dahne_2017]
- [Wunderlich et al 2017][research_wunderlich_dahne_2017_b]
- [Wustenhagen et al 2021][research_wustenhagen_suelozgen_2021]
- [Wynn et al 2022][research_wynn_artola_2022]
- [Wyrick 1965][research_wyrick_1965]
- [Xiang and Wang 2023][research_xiang_wang_2023]
- [Xiao et al 2011][research_xiao_li_2011]
- [Xiao et al 2022][research_xiao_wang_2022]
- [Xiaoguang et al 2023][research_xiaoguang_du_2023]
- [Xie 2010][research_xie_2010]
- [Xie and Yang 2011][research_xie_yang_2011]
- [Xie et al 2007][research_xie_leng_2007]
- [Xie et al 2012][research_xie_yang_2012]
- [Xie et al 2016][research_xie_liu_2016]
- [Xie et al 2019][research_xie_zhao_2019]
- [Xin and Li 2025][research_xin_li_2025]
- [Xing and Singh 1999][research_xing_singh_1999]
- [Xiong and Liu 2013][research_xiong_liu_2013]
- [Xiong and Nguyen 2024][research_xiong_nguyen_2024]
- [Xiong and Nguyen 2024][research_xiong_nguyen_2024_b]
- [Xiong and Nguyen 2024][research_xiong_nguyen_2024_c]
- [Xiong and Yang 2001][research_xiong_yang_2001]
- [Xiong et al 2019][research_xiong_fugate_2019]
- [Xiong et al 2021][research_xiong_nguyen_2021]
- [Xiong et al 2023][research_xiong_nguyen_2023]
- [Xu and Kroo 2011][research_xu_kroo_2011]
- [Xu and Kroo 2011][research_xu_kroo_2011_b]
- [Xu and Kroo 2014][research_xu_kroo_2014]
- [Xu and Qiu 2011][research_xu_qiu_2011]
- [Xu and West 1990][research_xu_west_1990]
- [Xu et al 2011][research_xu_zhu_2011]
- [Xu et al 2015][research_xu_gao_2015]
- [Xu et al 2015][research_xu_gao_2015_b]
- [Xu et al 2016][research_xu_tang_2016]
- [Xu et al 2020][research_xu_han_2020]
- [Xu et al 2020][research_xu_zhang_2020]
- [Xu et al 2023][research_xu_chen_2023]
- [xu et al 2023][research_xu_song_2023]
- [Xu et al 2024][research_xu_sevart_2024]
- [Xue and Li 2016][research_xue_li_2016]
- [Xue et al 2019][research_xue_ye_2019]
- [Xue Lei et al 2016][research_xuelei_zhangzheyu_2016]
- [Yamamoto 1992][research_yamamoto_1992]
- [Yamane 1992][research_yamane_1992]
- [Yamane and Friedmann 1990][research_yamane_friedmann_1990]
- [Yamane and Friedmann 1993][research_yamane_friedmann_1993]
- [Yamashiro and Stirling 2007][research_yamashiro_stirling_2007]
- [Yamazaki and Kusunose 2016][research_yamazaki_kusunose_2016]
- [Yan et al 2019][research_yan_li_2019]
- [Yanagihara et al 1991][research_yanagihara_suzuki_1991]
- [Yang and Gao 2020][research_yang_gao_2020]
- [Yang and Guo 2009][research_yang_guo_2009]
- [Yang and Li 2022][research_yang_li_2022]
- [Yang and Shen 2007][research_yang_shen_2007]
- [Yang and Wan 1978][research_yang_wan_1978]
- [Yang and Xia 2011][research_yang_xia_2011]
- [Yang et al 2007][research_yang_zheng_2007]
- [Yang et al 2009][research_yang_chen_2009]
- [Yang et al 2009][research_yang_zhong_2009]
- [Yang et al 2010][research_yang_xiao_2010]
- [Yang et al 2011][research_yang_kim_2011]
- [Yang et al 2014][research_yang_li_2014]
- [Yang et al 2015][research_yang_sartor_2015]
- [Yang et al 2017][research_yang_huang_2017]
- [Yang et al 2018][research_yang_dudley_2018]
- [Yang et al 2019][research_yang_huang_2019]
- [Yang et al 2019][research_yang_xie_2019]
- [Yang et al 2023][research_yang_liu_2023]
- [Yang et al 2024][research_yang_xu_2024]
- [Yang et al 2025][research_yang_kou_2025]
- [Yang et al 2025][research_yang_liu_2025]
- [Yang et al 2025][research_yang_wu_2025]
- [Yao et al 2023][research_yao_kan_2023]
- [Yasue and Sawada 2009][research_yasue_sawada_2009]
- [Yates 1963][research_yates_1963]
- [Yavuztürk et al 2017][research_yavuzturk_topbas_2017]
- [Ye and Ye 2021][research_ye_ye_2021]
- [Yee 1992][research_yee_1992]
- [Yeh 1995][research_yeh_1995]
- [Yeo et al 2010][research_yeo_potsdam_2010]
- [Yeo et al 2023][research_yeo_kang_2023]
- [Yerly et al 2016][research_yerly_deluca_2016]
- [Yiming et al 2019][research_yiming_mei_2019]
- [Yin et al 2015][research_yin_wu_2015]
- [Yin et al 2026][research_yin_xiao_2026]
- [Yokozeki et al 2014][research_yokozeki_sugiura_2014]
- [Yomchinda et al 2009][research_yomchinda_horn_2009]
- [Yoneyama and Hatamura 1989][research_yoneyama_hatamura_1989]
- [Yonezawa and Obayashi 2010][research_yonezawa_obayashi_2010]
- [Yoon et al 2012][research_yoon_chung_2012]
- [Yoshikawa 1982][research_yoshikawa_1982]
- [You et al 2020][research_you_kim_2020]
- [Youssef 1985][research_youssef_1985]
- [Yu 1979][research_yu_1979]
- [Yu 1980][research_yu_1980]
- [Yu 2026][research_yu_2026]
- [Yu and Campbell 1992][research_yu_campbell_1992]
- [Yu and He 2016][research_yu_he_2016]
- [Yu et al 2004][research_yu_yuan_2004]
- [Yu et al 2013][research_yu_zhao_2013]
- [Yu et al 2014][research_yu_lv_2014]
- [Yu et al 2017][research_yu_wang_2017]
- [Yu et al 2026][research_yu_bose_2026]
- [Yuan 2026][research_yuan_2026]
- [Yuan et al 2023][research_yuan_ma_2023]
- [Yucelen et al 2011][research_yucelen_kim_2011]
- [Yue 2026][research_yue_2026]
- [Yue et al 2017][research_yue_wang_2017]
- [Yue et al 2017][research_yue_zhang_2017]
- [Yurkovich 1986][research_yurkovich_1986]
- [Yurkovich 2009][research_yurkovich_2009]
- [Yurtsever et al 2026][research_yurtsever_sahin_2026]
- [Yusuf et al 2019][research_yusuf_hayes_2019]
- [Zafirov 2010][research_zafirov_2010]
- [Zahn 1984][research_zahn_1984]
- [Zaichik et al 2013][research_zaichik_yashin_2013]
- [Zaki et al 2017][research_zaki_unel_2017]
- [Zanette and Almeida 2015][research_zanette_almeida_2015]
- [Zaw and Baranovski 2026][research_zaw_baranovski_2026]
- [Zeiler 1998][research_zeiler_1998]
- [Zeiler 1999][research_zeiler_1999]
- [Zeiler, Thomas A. 1998][research_zeilerthomasa_1998]
- [Zeising and Gerhardt 1993][research_zeising_gerhardt_1993]
- [Zeng and Singh 1998][research_zeng_singh_1998]
- [Zeng et al 2007][research_zeng_baldelli_2007]
- [Zeng et al 2008][research_zeng_baldelli_2008]
- [Zeng et al 2010][research_zeng_moulin_2010]
- [Zeng et al 2011][research_zeng_wang_2011]
- [Zeng et al 2012][research_zeng_kukreja_2012]
- [Zeng et al 2017][research_zeng_qian_2017]
- [Zhan 2016][research_zhan_2016]
- [Zhang and Behal 2014][research_zhang_behal_2014]
- [Zhang and Cheng 2025][research_zhang_cheng_2025]
- [Zhang and Cheng 2026][research_zhang_cheng_2026]
- [Zhang and Singh 2000][research_zhang_singh_2000]
- [Zhang and Soffker][research_zhang_soffker]
- [Zhang and Söffker 2010][research_zhang_soffker_2010]
- [Zhang and Wang 2019][research_zhang_wang_2019]
- [Zhang and Zhang 2013][research_zhang_zhang_2013]
- [Zhang and Zhao 2023][research_zhang_zhao_2023]
- [Zhang and Zhu 2021][research_zhang_zhu_2021]
- [Zhang et al 2007][research_zhang_suresh_2007]
- [Zhang et al 2008][research_zhang_rabbath_2008]
- [Zhang et al 2008][research_zhang_xu_2008]
- [Zhang et al 2013][research_zhang_yang_2013]
- [Zhang et al 2013][research_zhang_yu_2013]
- [Zhang et al 2017][research_zhang_devisser_2017]
- [Zhang et al 2017][research_zhang_wang_2017]
- [Zhang et al 2018][research_zhang_zhou_2018]
- [Zhang et al 2018][research_zhang_zhou_2018_b]
- [Zhang et al 2019][research_zhang_ge_2019]
- [Zhang et al 2019][research_zhang_kang_2019]
- [Zhang et al 2020][research_zhang_chen_2020]
- [Zhang et al 2021][research_zhang_guo_2021]
- [Zhang et al 2021][research_zhang_shaw_2021]
- [Zhang et al 2022][research_zhang_liu_2022]
- [Zhang et al 2024][research_zhang_qiu_2024]
- [Zhang et al 2024][research_zhang_tian_2024]
- [Zhang et al 2024][research_zhang_zhao_2024]
- [Zhang et al 2025][research_zhang_hou_2025]
- [Zhang et al 2025][research_zhang_jiao_2025]
- [Zhang et al 2025][research_zhang_kang_2025]
- [Zhang et al 2025][research_zhang_li_2025]
- [Zhang et al 2025][research_zhang_xiang_2025]
- [Zhang et al 2026][research_zhang_dai_2026]
- [Zhang et al 2026][research_zhang_dai_2026_b]
- [Zhang et al 2026][research_zhang_deng_2026]
- [Zhao 2009][research_zhao_2009]
- [Zhao 2011][research_zhao_2011]
- [Zhao 2012][research_zhao_2012]
- [zhao 2019][research_zhao_2019]
- [Zhao 2020][research_zhao_2020]
- [Zhao et al 2016][research_zhao_yue_2016]
- [Zhao et al 2020][research_zhao_he_2020]
- [Zhao et al 2023][research_zhao_yang_2023]
- [Zhao et al 2024][research_zhao_li_2024]
- [Zhao et al 2025][research_zhao_zhang_2025]
- [Zhao et al 2026][research_zhao_zheng_2026]
- [Zhavyrkin and Sladkova 2023][research_zhavyrkin_sladkova_2023]
- [Zhen and Cui 2023][research_zhen_cui_2023]
- [Zheng 2010][research_zheng_2010]
- [Zheng et al 2013][research_zheng_hedrick_2013]
- [Zheng et al 2018][research_zheng_zhang_2018]
- [Zhi et al 2020][research_zhi_zhou_2020]
- [Zhong et al 2009][research_zhong_yang_2009]
- [Zhong et al 2025][research_zhong_xia_2025]
- [Zhou et al 2013][research_zhou_xu_2013]
- [Zhou et al 2017][research_zhou_chen_2017]
- [Zhou et al 2018][research_zhou_yu_2018]
- [Zhu 2018][research_zhu_2018]
- [Zhu and Qiao 2009][research_zhu_qiao_2009]
- [Zhu et al 2017][research_zhu_chen_2017]
- [Zhu et al 2019][research_zhu_li_2019]
- [Zhuang and Lei 2020][research_zhuang_lei_2020]
- [Zhuang et al 2017][research_zhuang_wu_2017]
- [Zientek 2001][research_zientek_2001]
- [Zink et al 1998][research_zink_mavris_1998]
- [Zink et al 1999][research_zink_mavris_1999]
- [Zink et al 2000][research_zink_mavris_2000]
- [Zink et al 2000][research_zink_raveh_2000]
- [Zink et al 2001][research_zink_raveh_2001]
- [Zink et al 2002][research_zink_raveh_2002]
- [Zink et al 2003][research_zink_raveh_2003]
- [Zink et al 2004][research_zink_raveh_2004]
- [Zou et al 2012][research_zou_yang_2012]
- [Zou et al 2021][research_zou_mu_2021]
- [Zou et al 2022][research_zou_huang_2022]
- [Zubin 1998][research_zubin_1998]
- [Zubin et al 2019][research_zubin_maksimov_2019]
- [Zyablikov and Shirshov 2021][research_zyablikov_shirshov_2021]
- [Çelik and Metin 2026][research_celik_metin_2026]
- [Çiçek and Kayran 2019][research_cicek_kayran_2019]
- [Özbek et al 2023][research_ozbek_ekici_2023_b]
- [Čečrdle 2018][research_cecrdle_2018]
- [Čečrdle et al 2022][research_cecrdle_malinek_2022]
- [Świtała and Lipski 2026][research_switala_lipski_2026]
- [Święch 2020][research_swiech_2020]
- [Şahin et al 2018][research_sahin_cakir_2018]
- [Şahin et al 2018][research_sahin_cakir_2018_b]
- [Ştefănescu 2020][research_stefanescu_2020]

[research_2_d_prototypical_2013]: https://doi.org/10.1201/b15376-18
[research_2_d_prototypical_2018]: https://doi.org/10.1201/9781315218045-20
[research_3_d_prototypical_2013]: https://doi.org/10.1201/b15376-19
[research_3_d_prototypical_2018]: https://doi.org/10.1201/9781315218045-21
[research_a_7_transonic_1982]: https://doi.org/10.2514/5.9781600865558.0431.0450
[research_a_comparative_2026]: https://doi.org/10.17586/1023-5086-2026-93-01-12-22
[research_a_parametric_1991]: https://doi.org/10.2514/6.1991-1054
[research_a_properties_2006]: https://doi.org/10.1002/9780470117859.app1
[research_a_synthesis_1994]: https://doi.org/10.1016/0967-0661(94)90526-6
[research_aaw_aero_model]: https://ntrs.nasa.gov/citations/20050204039
[research_aaw_control_laws]: https://ntrs.nasa.gov/citations/20060003626
[research_aaw_deflection_loads]: https://ntrs.nasa.gov/citations/20050172129
[research_aaw_flight_research_plan]: https://doi.org/10.2514/6.1996-1574
[research_aaw_flight_test]: https://ntrs.nasa.gov/citations/20050204120
[research_aaw_loads_model]: https://ntrs.nasa.gov/citations/20050204113
[research_aaw_shock_loads]: https://ntrs.nasa.gov/citations/20060002813
[research_aaw_technical_program]: https://doi.org/10.2514/2.2654
[research_aaw_torsional_stiffness]: https://ntrs.nasa.gov/citations/20030004753
[research_aaw_twist_model]: https://ntrs.nasa.gov/citations/20070022496
[research_aaw_wind_tunnel]: https://ntrs.nasa.gov/citations/20050203672
[research_abdallah_2018]: https://doi.org/10.2514/6.2018-3153
[research_abdallah_newman_2013]: https://doi.org/10.2514/6.2013-4985
[research_abdallah_newman_2014]: https://doi.org/10.2514/6.2014-2193
[research_abdelkader_harmin_2011]: https://doi.org/10.2514/6.2011-1712
[research_abdif_ideh_1988]: https://ntrs.nasa.gov/citations/19890026240
[research_abdullah_sulaeman_2013]: https://doi.org/10.4028/www.scientific.net/amm.464.110
[research_abdulrahim_garcia_2004]: https://doi.org/10.2514/6.2004-1674
[research_abdulrahim_weibley_2018]: https://doi.org/10.2514/6.2018-1013
[research_abel_1972]: https://doi.org/10.2514/3.58934
[research_abel_iii_1978]: https://doi.org/10.2514/3.55790
[research_abel_newsom_1979]: https://doi.org/10.2514/6.1979-1633
[research_abel_newsom_1981]: https://doi.org/10.2514/6.1981-639
[research_abel_perryiii_1977]: https://doi.org/10.2514/6.1977-1062
[research_abrahamdoman_merrett_2014]: https://doi.org/10.2514/6.2014-0194
[research_abramova_petrov_2016]: https://doi.org/10.1063/1.4963940
[research_achache_whalley_1996]: https://doi.org/10.4050/vfs-f52-2053
[research_acm_produces_2005]: https://doi.org/10.1016/s0034-3617(05)70593-2
[research_active_control_1994]: https://doi.org/10.1016/0967-0661(94)90531-2
[research_active_flutter_1999]: https://doi.org/10.1109/acc.1999.786286
[research_active_flutter_2016]: https://doi.org/10.1002/9781118823491.ch4
[research_adali_1981]: https://doi.org/10.1080/03052158108902442
[research_adamson_fichera_2019]: https://doi.org/10.2514/6.2019-1754
[research_adaptive_transonic_2016]: https://doi.org/10.1002/9781118823491.ch11
[research_adnyana_2017]: https://doi.org/10.14203/metalurgi.v31i3.175
[research_advisorygroupforaerospaceresearchanddevelopment_1984]: https://ntrs.nasa.gov/citations/19840026325
[research_aero_structural_2018]: https://doi.org/10.20474/jater-4.1.5
[research_aerodynamic_phenomena_2020]: https://doi.org/10.1002/9781119667063.ch4
[research_aeroelastic_control_2005]: https://doi.org/10.1007/1-4020-2106-2_12
[research_aeroelastic_modelling_2016]: https://doi.org/10.1002/9781118823491.ch3
[research_aeroelasticity_problems_2010]: https://doi.org/10.2514/5.9781600867552.0335.0373
[research_aeroservoelastic_tailoring]: https://ntrs.nasa.gov/citations/19900046005
[research_afkhami_alighanbari_2007]: https://doi.org/10.1049/iet-cta:20060455
[research_afti_mlc]: https://ntrs.nasa.gov/citations/19940019822
[research_afw_f16_derivative]: https://doi.org/10.2514/6.1991-987
[research_afw_flutter_strain_gauge]: https://doi.org/10.2514/6.1992-2098
[research_afw_flutter_suppression]: https://ntrs.nasa.gov/citations/19890016639
[research_afw_modeling]: https://ntrs.nasa.gov/citations/19910013020
[research_afw_overview]: https://ntrs.nasa.gov/citations/19910013019
[research_afw_roll_mla]: https://ntrs.nasa.gov/citations/19910013022
[research_afw_simulation_reduction]: https://doi.org/10.2514/3.46679
[research_afw_summary]: https://ntrs.nasa.gov/citations/19920022020
[research_afw_technology_summary]: https://doi.org/10.2514/3.46677
[research_afw_tm101570]: https://ntrs.nasa.gov/citations/19890014942
[research_afw_wind_tunnel]: https://ntrs.nasa.gov/citations/19900000803
[research_agarwal_deese_1983]: https://doi.org/10.2514/6.1983-501
[research_agarwal_deese_1984]: https://doi.org/10.2514/6.1984-1551
[research_agile_falcon]: https://doi.org/10.2514/3.46181
[research_agostinelli_allen_2012]: https://doi.org/10.2514/6.2012-2661
[research_agrawal_kinard_1991]: https://doi.org/10.2514/6.1991-3205
[research_ahmad_baig_2018]: https://doi.org/10.1063/1.5045437
[research_ahmad_gazetas_1992]: https://doi.org/10.1061/(asce)0733-9410(1992)118:8(1168)
[research_ahmadi_farsadi_2024]: https://doi.org/10.1016/j.ast.2023.108849
[research_ahmaditehrani_ellis_2025]: https://doi.org/10.2514/6.2025-0715
[research_aileron_2005]: https://doi.org/10.1002/0471743984.vse0218
[research_airforceflighttestcenteredwardsafbca_1970]: https://doi.org/10.21236/ada529707
[research_airforceflighttestcenteredwardsafbca_1974]: https://doi.org/10.21236/ada011561
[research_airforceflighttestcenteredwardsafbca_1974_b]: https://doi.org/10.21236/ada011562
[research_airforceflighttestcenteredwardsafbca_2002]: https://doi.org/10.21236/ada402888
[research_airforcetestpilotschooledwardsafbca_1962]: https://doi.org/10.21236/ada320208
[research_airforcetestpilotschooledwardsafbca_1988]: https://doi.org/10.21236/ada319984
[research_airforcetestpilotschooledwardsafbca_1989]: https://doi.org/10.21236/ada319980
[research_airforcetestpilotschooledwardsafbca_1990]: https://doi.org/10.21236/ada320062
[research_airforcetestpilotschooledwardsafbca_1990_b]: https://doi.org/10.21236/ada320058
[research_ajaj_djidjeli_2022]: https://doi.org/10.3390/designs6050092
[research_akasaka_katoh_1989]: https://doi.org/10.2346/1.2141688
[research_akinwale_datta_2025]: https://doi.org/10.2514/1.c037994
[research_akmese_comert_2009]: https://doi.org/10.2514/6.2009-6302
[research_alag_burken_1986]: https://doi.org/10.2514/6.1986-2243
[research_alag_burken_1987]: https://doi.org/10.2514/3.20253
[research_alam_hromcik_2015]: https://doi.org/10.1016/j.ast.2014.12.020
[research_alam_hromcik_2019]: https://doi.org/10.1016/j.conengprac.2019.05.005
[research_alam_sohn_2023]: https://doi.org/10.3390/jmse12010062
[research_alaverdi_paris_2001]: https://doi.org/10.2514/6.2001-4015
[research_albertani_stanford_2005]: https://doi.org/10.2514/6.2005-6324
[research_albisser]: https://doi.org/10.70675/ab94f713z868bz4379za278z50bc17451ea3
[research_alden_schindel_1952]: https://doi.org/10.2514/8.2140
[research_alhajjar_aljiboory_2018]: https://doi.org/10.2514/6.2018-1342
[research_ali_2024]: https://doi.org/10.1016/j.rico.2024.100399
[research_alighanbari_2002]: https://doi.org/10.2514/2.2986
[research_alighanbari_lee_2003]: https://doi.org/10.2514/2.3129
[research_allaire_lecerf_2014]: https://doi.org/10.2514/6.2014-1175
[research_allen_fenwick_2003]: https://doi.org/10.2514/6.2003-3510
[research_allen_lizotte_2005]: https://doi.org/10.2514/6.2005-6313
[research_allen_pollock_1983]: https://doi.org/10.2514/6.1983-994
[research_allen_reardon_1986]: https://doi.org/10.2514/6.1986-957
[research_allyn_takahashi_2016]: https://doi.org/10.2514/6.2016-3744
[research_alsaidi_akbar_2018]: https://doi.org/10.2514/6.2018-2934
[research_alsaidi_akbar_2018_b]: https://doi.org/10.2514/6.2018-2934.c1
[research_alsaidi_joe_2019]: https://doi.org/10.3390/aerospace6080090
[research_alsaidi_joe_2019_b]: https://doi.org/10.3844/ajassp.2019.182.191
[research_alshehabi_newman_2000]: https://doi.org/10.1115/imece2000-2305
[research_alshehabi_newman_2000_b]: https://doi.org/10.2514/6.2000-4148
[research_alstrom_marzocca_2010]: https://doi.org/10.2514/6.2010-8146
[research_altman_1952]: https://doi.org/10.21236/ada075871
[research_alulema_valencia_2020]: https://doi.org/10.2514/6.2020-3958
[research_alvarez_2014]: https://doi.org/10.5162/etc2014/2.5
[research_alvarez_wissa_2021]: https://doi.org/10.1115/smasis2021-68299
[research_alwi_edwards_2007]: https://doi.org/10.1109/cca.2007.4389401
[research_alwi_edwards_2009]: https://doi.org/10.1109/acc.2009.5160331
[research_alyanak_pendleton_2014]: https://doi.org/10.2514/6.2014-3158
[research_alyanak_pendleton_2017]: https://doi.org/10.2514/1.c033040
[research_amendola_dimino_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00018-6
[research_ameri_lowenberg_2007]: https://doi.org/10.2514/6.2007-6500
[research_americaninstituteofaeronauticsandastronautics_1993]: https://ntrs.nasa.gov/citations/19930049879
[research_amoozgar_fazelzadeh_2020]: https://doi.org/10.1016/j.ast.2020.106241
[research_amoozgar_friswell_2021]: https://doi.org/10.3390/aerospace8040100
[research_amoozgar_hall_2024]: https://doi.org/10.2514/6.2024-2044
[research_amoozgar_irani_2012]: https://doi.org/10.4028/www.scientific.net/amr.463-464.1568
[research_amoozgar_irani_2013]: https://doi.org/10.1016/j.jfluidstructs.2012.10.007
[research_amoozgar_shahverdi_2019]: https://doi.org/10.1108/aeat-07-2018-0212
[research_an_experimental_1978]: https://doi.org/10.2514/6.1978-1200
[research_an_xie_2018]: https://doi.org/10.2514/6.2018-0192
[research_an_zhu_2023]: https://doi.org/10.1109/icmae59650.2023.10424458
[research_andakhshideh_tahani_2013]: https://doi.org/10.1016/j.euromechsol.2013.06.002
[research_andersen_forster_1996]: https://doi.org/10.2514/6.1996-1443
[research_andersen_forster_1997]: https://doi.org/10.2514/2.2208
[research_andersen_kolonay_1998]: https://doi.org/10.2514/6.1998-1803
[research_anderson_1984]: https://doi.org/10.2514/6.1984-2093
[research_anderson_1985]: https://doi.org/10.2514/3.45218
[research_anderson_1993]: https://doi.org/10.2514/6.1993-3795
[research_anderson_berger_1972]: https://doi.org/10.2514/6.1972-870
[research_anderson_caverly_2026]: https://doi.org/10.2514/6.2026-1746
[research_anderson_vincent_1983]: https://doi.org/10.2514/6.1983-2746
[research_anderson_white_2004]: https://doi.org/10.1115/imece2004-60458
[research_anderson_white_2005]: https://doi.org/10.1115/detc2005-85586
[research_andrews_gordon_1981]: https://doi.org/10.2514/6.1981-2452
[research_andrienko_tropova_2010]: https://doi.org/10.1134/s0005117910050139
[research_andrighettoni_mantegazza_1998]: https://doi.org/10.2514/2.2319
[research_ansell_bragg_2010]: https://doi.org/10.2514/6.2010-4225
[research_ansell_bragg_2011]: https://doi.org/10.2514/1.c031435
[research_ansell_bragg_2011_b]: https://doi.org/10.4271/2011-38-0066
[research_ansell_kerho_2013]: https://doi.org/10.2514/6.2013-2654
[research_ansell_kerho_2014]: https://doi.org/10.2514/1.c032703
[research_antonakis_biannic_2024]: https://doi.org/10.2514/1.c037707
[research_aouf_boulet_2000]: https://doi.org/10.1109/acc.2000.879526
[research_appendix_a_2011]: https://doi.org/10.1515/9781400839063-017
[research_appendix_a_2021]: https://doi.org/10.1002/9781118949818.app1
[research_appendix_b_2003]: https://doi.org/10.2514/5.9781600862069.0573.0576
[research_appendix_b_2016]: https://doi.org/10.1002/9781118823491.app2
[research_appendix_c_2016]: https://doi.org/10.1002/9781118823491.app3
[research_application_of_1982]: https://doi.org/10.2514/5.9781600865558.0405.0430
[research_application_of_1982_b]: https://doi.org/10.2514/5.9781600865558.0621.0636
[research_apte_athani_1979]: https://doi.org/10.2514/3.55842
[research_arai_tanaka_2020]: https://doi.org/10.1299/jsmemecj.2020.j19206
[research_aravinth_shinde_2018]: https://doi.org/10.2514/6.2018-1443
[research_archambaud_louis_2004]: https://doi.org/10.2514/6.2004-2245
[research_arefev_1968]: https://doi.org/10.1007/bf00979749
[research_arizono_cesnik_2013]: https://doi.org/10.2514/6.2013-1862
[research_arizono_isogai_2005]: https://doi.org/10.2514/1.392
[research_armanious_lind_2018]: https://doi.org/10.2514/6.2018-1012
[research_armstrong_1977]: https://doi.org/10.21236/adb029224
[research_armstrong_miller_1968]: https://doi.org/10.2514/3.43932
[research_arnold_1942]: https://doi.org/10.2514/8.10949
[research_arnold_1981]: https://doi.org/10.2514/6.1981-2444
[research_asadi_farsadi_2020]: https://doi.org/10.1016/j.ast.2020.105853
[research_asadi_farsadi_2021]: https://doi.org/10.2514/1.j059568
[research_asaro_cavaliere_2023]: https://doi.org/10.2514/6.2023-1946
[research_ashkenas_1965]: https://doi.org/10.21236/ad0627659
[research_askari_soltani_2019]: https://doi.org/10.2514/1.c035328
[research_aslammir_mclean]: https://doi.org/10.1109/naecon.1994.332859
[research_atkinson_2016]: https://doi.org/10.2514/6.2016-1185
[research_atmosphere_standard_2006]: https://doi.org/10.1007/978-0-387-30160-0_849
[research_aulschenko_zamuraev_2006]: https://doi.org/10.1134/s1063785006010020
[research_austin_hadcock_1976]: https://doi.org/10.2514/6.1976-1506
[research_avci_tegin_2026]: https://doi.org/10.2514/6.2026-4049
[research_ayaz_rasoolmemon_2024]: https://doi.org/10.1109/access.2024.3435961
[research_azevedo_1987]: https://doi.org/10.2514/6.1987-708
[research_azizov_derkowski_2019]: https://doi.org/10.4028/www.scientific.net/msf.968.330
[research_azzi_tahiliani_2024]: https://doi.org/10.2514/6.2024-84319
[research_b_34_u_1963]: https://doi.org/10.1016/0019-1035(63)90063-0
[research_babcock_lind_2012]: https://doi.org/10.2514/6.2012-4400
[research_babcock_lind_2012_b]: https://doi.org/10.2514/6.2012-4865
[research_babcock_lind_2013]: https://doi.org/10.2514/6.2013-4845
[research_babcock_lind_2013_b]: https://doi.org/10.2514/6.2013-4744
[research_babinsky_delery_2011]: https://doi.org/10.1017/cbo9780511842757.003
[research_babister_1980]: https://doi.org/10.1016/b978-0-08-024768-7.50011-9
[research_bach_mcnally_1988]: https://doi.org/10.1016/s1474-6670(17)54915-0
[research_bachelder_klyde_2004]: https://doi.org/10.2514/6.2004-5065
[research_bachelder_thompson_2011]: https://doi.org/10.2514/6.2011-6445
[research_badcock_rampurawala_2003]: https://doi.org/10.2514/6.2003-3512
[research_bae_inman_2004]: https://doi.org/10.1016/j.jfluidstructs.2004.04.005
[research_bae_lee_2002]: https://doi.org/10.1115/imece2002-33066
[research_bae_yang_2002]: https://doi.org/10.2514/2.2984
[research_baerriedhart_1981]: https://doi.org/10.2514/6.1981-2467
[research_baggi_franco_2020]: https://doi.org/10.2514/6.2020-0841
[research_baggi_serrani_2022]: https://doi.org/10.1109/ccta49430.2022.9966141
[research_bagherzadeh_2020]: https://doi.org/10.1108/aeat-06-2019-0129
[research_bahiamonteiro_gray_2023]: https://doi.org/10.2514/6.2023-0728
[research_bai_cao_2022]: https://doi.org/10.1016/j.tsep.2022.101297
[research_bai_zhang_2014]: https://doi.org/10.1109/chicc.2014.6896634
[research_bailey_powers_1988]: https://doi.org/10.2514/6.1988-4327
[research_bajaj_2019]: https://doi.org/10.31224/osf.io/ecxpv
[research_baker_forsey_1981]: https://doi.org/10.2514/6.1981-1015
[research_balakrishnan_2006]: https://doi.org/10.1061/(asce)0893-1321(2006)19:3(194)
[research_balakrishnan_2007]: https://doi.org/10.1201/9781420011159.ch11
[research_balakrishnan_2012]: https://doi.org/10.1007/978-1-4614-3609-6_4
[research_balakrishnan_iliff_2007]: https://doi.org/10.1061/(asce)0893-1321(2007)20:3(152)
[research_balas_hindman_2004]: https://doi.org/10.2514/6.2004-6824
[research_balas_moreno_2012]: https://doi.org/10.2514/6.2012-4897
[research_balas_seiler_2011]: https://doi.org/10.2514/6.2011-6290
[research_balatti_ellis_2023]: https://doi.org/10.2514/6.2023-2567
[research_balatti_khodaparast_2023]: https://doi.org/10.1016/j.jfluidstructs.2023.103892
[research_baldelli_zeng_2009]: https://doi.org/10.2514/1.36584
[research_ball_1978]: https://doi.org/10.2514/6.1978-1500
[research_ball_1979]: https://doi.org/10.2514/3.58559
[research_balleur_girodrouxlavigne_2002]: https://doi.org/10.1007/978-3-540-45856-2_9
[research_balon_benes_2021]: https://doi.org/10.1109/icmerr54363.2021.9680832
[research_bambermillardj_1934]: https://ntrs.nasa.gov/citations/19930081509
[research_banavara_newsom_2010]: https://doi.org/10.2514/6.2010-8114
[research_banerjee_liu_2014]: https://doi.org/10.5890/jand.2014.12.012
[research_banerjee_williams_1992]: https://doi.org/10.1016/0045-7949(92)90026-v
[research_bang_rana_2022]: https://doi.org/10.1115/1.4053089
[research_baranyi_2006]: https://doi.org/10.2514/1.14981
[research_baranyi_2006_b]: https://doi.org/10.2514/1.9462
[research_baranyi_patton_2003]: https://doi.org/10.23919/ecc.2003.7085276
[research_barb_mulder_2003]: https://doi.org/10.2514/6.2003-5556
[research_barker_balas_1999]: https://doi.org/10.2514/2.4418
[research_barker_balas_2000]: https://doi.org/10.2514/2.4637
[research_barnwell_1974]: https://doi.org/10.2514/6.1974-185
[research_bartels_stanford_2019]: https://doi.org/10.2514/6.2019-2035
[research_bartels_stanford_2019_b]: https://doi.org/10.2514/6.2019-2035.c1
[research_barzgaran_quenzer_2021]: https://doi.org/10.2514/6.2021-0500
[research_bass_thompson_1993]: https://doi.org/10.2514/6.1993-3412
[research_bass_thompson_1995]: https://doi.org/10.2514/6.1995-1887
[research_bateman_dewekker_2023]: https://doi.org/10.2514/6.2023-0787
[research_batina_1986]: https://doi.org/10.2514/6.1986-862
[research_baumann_pahle_2008]: https://doi.org/10.2514/6.2008-6570
[research_baz_chen_1993]: https://doi.org/10.1016/0961-9526(93)90069-v
[research_baz_iman_1987]: https://doi.org/10.21236/ada205948
[research_bdeiwi_ciarella_2019]: https://doi.org/10.1108/hff-07-2018-0352
[research_beatty_brooks_1977]: https://doi.org/10.21236/ada045951
[research_beaverstock_woods_2015]: https://doi.org/10.3390/aerospace2030524
[research_bednarz_zhu_2013]: https://doi.org/10.1111/str.12035
[research_begnini_bones_2018]: https://doi.org/10.2514/6.2018-3004
[research_beh_hofinger_2018]: https://doi.org/10.1201/9781315136820-15
[research_behal_marzocca_2004]: https://doi.org/10.2514/6.2004-5227
[research_behal_marzocca_2006]: https://doi.org/10.2514/1.14011
[research_beldica_hilton_1999]: https://doi.org/10.2514/6.1999-1423
[research_belesiotiskataras_timme_2021]: https://doi.org/10.2514/6.2021-0611
[research_belisle_neale_2010]: https://doi.org/10.2514/6.2010-4381
[research_belote_menezes_2019]: https://doi.org/10.26678/abcm.cobem2019.cob2019-1150
[research_benasher_raveh_2023]: https://doi.org/10.2514/6.2023-1309
[research_bendiksen_1992]: https://doi.org/10.2514/6.1992-2121
[research_bendiksen_1993]: https://doi.org/10.2514/6.1993-1479
[research_bendiksen_2001]: https://doi.org/10.2514/2.4699
[research_bendiksen_hwang_1997]: https://doi.org/10.2514/6.1997-1269
[research_bendixen_oconnell_1981]: https://doi.org/10.1017/s0001924000030244
[research_benjaminmsimmons]: https://ntrs.nasa.gov/citations/20210024304
[research_bennett_brown_2001]: https://doi.org/10.4050/vfs-f57-00071
[research_bennett_dansberry_1991]: https://doi.org/10.2514/6.1991-1107
[research_bennett_dansberry_1993]: https://doi.org/10.2514/3.46314
[research_bennett_seidel_1985]: https://doi.org/10.2514/6.1985-665
[research_bennettrm_farmermg_1977]: https://ntrs.nasa.gov/citations/19770060309
[research_benosman_liao_2007]: https://doi.org/10.1109/cca.2007.4389344
[research_benyamen_keshmiri_2022]: https://doi.org/10.1109/icuas54217.2022.9836206
[research_berci_2017]: https://doi.org/10.1063/1.4992672
[research_beresh_barone_2020]: https://doi.org/10.2514/6.2020-1308
[research_bergman_vakakis_2011]: https://doi.org/10.21236/ada565204
[research_bergmann_sevart_1973]: https://doi.org/10.2514/6.1973-323
[research_bergmann_sevart_1975]: https://doi.org/10.2514/3.59810
[research_bernellizazzera_mantegazza_2000]: https://doi.org/10.2514/2.4671
[research_bernhard_chopra_1996]: https://doi.org/10.4050/vfs-f52-310
[research_bernhard_chopra_1997]: https://doi.org/10.4050/vfs-f53-3010
[research_berton_2022]: https://doi.org/10.2514/6.2022-3078
[research_beug_moser_2012]: https://doi.org/10.1109/cpem.2012.6251056
[research_bever_1992]: https://doi.org/10.2514/6.1992-4113
[research_beyer_steen_2024]: https://doi.org/10.2514/1.g007984
[research_beyer_ullah_2024]: https://doi.org/10.1007/s13272-024-00760-8
[research_bhat_2018]: https://doi.org/10.1201/9781315370613-3
[research_bhat_2018_b]: https://doi.org/10.1201/9781315370613-9
[research_bhat_2018_c]: https://doi.org/10.1201/9781315370613-6
[research_bhat_2018_d]: https://doi.org/10.1201/9781315370613-11
[research_bi_xie_2017]: https://doi.org/10.2514/6.2017-1349
[research_bi_xie_2017_b]: https://doi.org/10.1016/j.cja.2016.12.028
[research_bian_nener_2018]: https://doi.org/10.1080/00207179.2018.1473643
[research_bian_nener_2019]: https://doi.org/10.1109/access.2019.2894961
[research_bichiou_hajj_2016]: https://doi.org/10.1007/s11071-016-2922-y
[research_biederman_meincke_1994]: https://doi.org/10.2514/6.1994-2125
[research_bielawa_2006]: https://doi.org/10.2514/4.862373
[research_bigler_1986]: https://doi.org/10.2514/6.1986-9729
[research_bihrle_barnhart_1982]: https://doi.org/10.2514/3.44789
[research_bihrle_jr_1980]: https://doi.org/10.21236/ada082335
[research_bilgen_saavedraflores_2011]: https://doi.org/10.1115/smasis2011-4971
[research_binder_wildschek_2021]: https://doi.org/10.1016/j.ast.2021.106516
[research_binwenlu_jianjunma_2016]: https://doi.org/10.1109/cgncc.2016.7828906
[research_birks_ludlow_1969]: https://doi.org/10.1111/j.1475-1305.1969.tb01623.x
[research_bismarcknasr_1992]: https://doi.org/10.2514/3.46189
[research_bismarcknasr_1994]: https://doi.org/10.2514/3.46590
[research_biswas_jimbo_2015]: https://doi.org/10.1115/gtindia2015-1225
[research_black_schwaab_2007]: https://doi.org/10.2514/6.2007-869
[research_blair_1994]: https://doi.org/10.2514/6.1994-1471
[research_blair_canfield_2002]: https://doi.org/10.2514/6.2002-1337
[research_blair_robinson_2008]: https://doi.org/10.21236/ada482613
[research_blair_weisshaar_1982]: https://doi.org/10.2514/3.44806
[research_blank_1995]: https://doi.org/10.2514/6.1995-1816
[research_bleimeyer_1981]: https://doi.org/10.2514/6.1981-2515
[research_blight_lanedailey_2018]: https://doi.org/10.1201/9781315136820-9
[research_block_gilliatt_1997]: https://doi.org/10.2514/6.1997-16
[research_block_strganac_1998]: https://doi.org/10.2514/2.4346
[research_blue_balas_1997]: https://doi.org/10.2514/6.1997-3640
[research_bocola_muscarello_2015]: https://doi.org/10.2514/6.2015-2557
[research_bodin_fuchs_2008]: https://doi.org/10.2514/6.2008-4174
[research_bodson_2000]: https://doi.org/10.21236/ada381657
[research_boehm_flick_2001]: https://doi.org/10.2514/6.2001-1372
[research_bogatyrev_2017]: https://doi.org/10.1615/tsagiscij.2017020745
[research_bohacek_nakamura]: https://doi.org/10.1109/cpem.1998.699813
[research_bohlmann_eckstrom_1990]: https://doi.org/10.2514/3.25319
[research_bohlmann_love_1992]: https://doi.org/10.2514/6.1992-2373
[research_bohlmann_weisshaar_1988]: https://doi.org/10.2514/6.1988-2263
[research_bohlmannjonathand_scottrobertc_1991]: https://ntrs.nasa.gov/citations/19910047245
[research_bonnema_smith_1988]: https://doi.org/10.2514/6.1988-2118
[research_bonnemakennethl_lokoswilliama_1989]: https://ntrs.nasa.gov/citations/19910035087
[research_bontoft_bhuwal_2026]: https://doi.org/10.2514/6.2026-4425
[research_bontoft_bhuwal_2026_b]: https://doi.org/10.2514/6.2026-4425.c1
[research_boothe_chen_1974]: https://doi.org/10.21236/ad0782218
[research_boppe_1977]: https://doi.org/10.2514/6.1977-207
[research_bordogna_lancelot_2020]: https://doi.org/10.1007/s00158-019-02446-w
[research_bordogna_macquart_2016]: https://doi.org/10.2514/6.2016-4122
[research_borglund_2003]: https://doi.org/10.2514/2.3074
[research_borglund_kuttenkeuler_2002]: https://doi.org/10.1006/jfls.2001.0426
[research_borglund_nilsson_2004]: https://doi.org/10.2514/1.9328
[research_bosch_schmehl_2014]: https://doi.org/10.2514/1.g000545
[research_boskovic_ling]: https://doi.org/10.1109/cdc.2002.1184767
[research_boskovic_mehra]: https://doi.org/10.1109/acc.2002.1024911
[research_botez_doin_2002]: https://doi.org/10.1115/imece2002-33623
[research_botez_grigorie_2008]: https://doi.org/10.2514/1.32817
[research_botez_koreanschi_2018]: https://doi.org/10.1017/aer.2018.15
[research_bottasso_montinari_2013]: https://doi.org/10.4050/vfs-f69-0282
[research_bouadi]: https://doi.org/10.70675/aa62b2a6zce9ez41fcz95cdz6ebfead4b829
[research_bouchalkha_alhammadi_2015]: https://doi.org/10.1109/aeect.2015.7360545
[research_bove_2026]: https://doi.org/10.21741/9781644904251-72
[research_bradshaw_rahulan_1988]: https://doi.org/10.1177/014233128801000105
[research_bramsiepe_voss_2020]: https://doi.org/10.1007/s13272-020-00446-x
[research_brandon_morelli_2014]: https://doi.org/10.2514/6.2014-2554
[research_bras_warwick_2022]: https://doi.org/10.1016/j.ast.2022.107400
[research_braun_boucke]: https://doi.org/10.1007/3-540-26589-9_23
[research_braun_boucke_2003]: https://doi.org/10.1007/978-3-642-55876-4_25
[research_breitenstein_muller_2023]: https://doi.org/10.2514/6.2023-3953
[research_breitenstein_muller_2024]: https://doi.org/10.2514/1.c037648
[research_breitsamter_2005]: https://doi.org/10.2514/1.8174
[research_breitsamter_laschka_2000]: https://doi.org/10.2514/6.2000-656
[research_breitsamter_schmid_2008]: https://doi.org/10.2514/1.33969
[research_brenner_2002]: https://doi.org/10.2514/2.4942
[research_brenner_feron_1997]: https://doi.org/10.2514/6.1997-1216
[research_brenner_lind_1998]: https://doi.org/10.2514/2.4331
[research_brenner_prazenica_2005]: https://doi.org/10.2514/6.2005-5917
[research_brennermartinj_1996]: https://ntrs.nasa.gov/citations/19970001360
[research_brennermartinj_2001]: https://ntrs.nasa.gov/citations/20010071675
[research_breul_1963]: https://doi.org/10.21236/ad0402774
[research_brewergeraldw_1946]: https://ntrs.nasa.gov/citations/20050031173
[research_briardy_head_1968]: https://doi.org/10.21236/ad0673964
[research_brincklow_hunsaker_2021]: https://doi.org/10.1017/aer.2020.139
[research_brincklow_montgomery_2021]: https://doi.org/10.2514/6.2021-0327
[research_brinker_wise_2000]: https://doi.org/10.2514/6.2000-3941
[research_bronz_hattenberger_2016]: https://doi.org/10.2514/6.2016-3979
[research_brooks_meyer_1995]: https://doi.org/10.2514/6.1995-1504
[research_brown_1989]: https://doi.org/10.2514/6.1989-2112
[research_brown_caverly_2021]: https://doi.org/10.2514/6.2021-1562
[research_brown_dillon_2004]: https://doi.org/10.2514/6.2004-4815
[research_brown_singh_2015]: https://doi.org/10.2514/6.2015-2241
[research_brown_singh_2016]: https://doi.org/10.2514/6.2016-0712
[research_brown_singh_2017]: https://doi.org/10.2514/6.2017-0569
[research_browne_maldonado_2024]: https://doi.org/10.2514/6.2024-0065
[research_brownjr_1970]: https://doi.org/10.2514/6.1970-947
[research_brownstuartc_1959]: https://ntrs.nasa.gov/citations/19980228294
[research_bruni_cestino_2014]: https://doi.org/10.1115/imece2014-38851
[research_bruni_frulla_2015]: https://doi.org/10.2514/6.2015-1188
[research_brunosantos_oliveira_2020]: https://doi.org/10.5151/siintec2020-analysisofelevator
[research_brysonjr_desai_1968]: https://doi.org/10.2514/6.1968-877
[research_bucharles_vacher_2002]: https://doi.org/10.1016/s1270-9638(02)01197-5
[research_buddhamatya_miranda_2026]: https://doi.org/10.2514/6.2026-2116
[research_buffington_1997]: https://doi.org/10.21236/ada327799
[research_buffington_1999]: https://doi.org/10.21236/ada374954
[research_bugala_2025]: https://doi.org/10.2478/tar-2025-0008
[research_bugala_sznajder_2023]: https://doi.org/10.2478/tar-2023-0023
[research_bunge_alkurdi_2016]: https://doi.org/10.2514/6.2016-3652
[research_bunge_munerasavino_2015]: https://doi.org/10.2514/6.2015-3225
[research_bunton_denegri_2000]: https://doi.org/10.2514/2.2690
[research_burch_1966]: https://doi.org/10.21236/ad0489065
[research_burch_1967]: https://doi.org/10.21236/ad0816631
[research_burchamjr_burken_1994]: https://doi.org/10.2514/6.1994-2123
[research_burchamjr_myers_1981]: https://doi.org/10.2514/6.1981-2438
[research_burchett_2011]: https://doi.org/10.2514/6.2011-6359
[research_burchett_2012]: https://doi.org/10.2514/6.2012-4861
[research_bureerat_2026]: https://doi.org/10.1007/978-981-95-8903-6_6
[research_burgstaller_galffy_2024]: https://doi.org/10.2514/6.2024-4490
[research_burken_alag_1986]: https://doi.org/10.23919/acc.1986.4788986
[research_burner_liu_2000]: https://doi.org/10.2514/6.2000-2386
[research_burner_martinson_1996]: https://doi.org/10.2514/6.1996-2253
[research_burneralpheusw_lokoswilliama_2005]: https://ntrs.nasa.gov/citations/20060002833
[research_burris_bender_1969]: https://doi.org/10.21236/ad0865310
[research_burris_bender_1969_b]: https://doi.org/10.21236/ad0864555
[research_burrows_vukasinovic_2021]: https://doi.org/10.1007/s00348-021-03280-x
[research_burtjr_1976]: https://doi.org/10.21236/ada037077
[research_burton_kneelandjr_1981]: https://doi.org/10.2514/6.1981-2465
[research_butler_lillico_1995]: https://doi.org/10.2514/6.1995-1223
[research_buttrill_houck_1990]: https://doi.org/10.2514/6.1990-3121
[research_byreddy_grandhi_2003]: https://doi.org/10.21236/ada417124
[research_byun_guruswamy_1994]: https://doi.org/10.2514/6.1994-1487
[research_byun_guruswamy_1996]: https://doi.org/10.2514/6.1996-4059
[research_byun_guruswamy_1996_b]: https://doi.org/10.2514/3.46954
[research_byun_guruswamy_1996_c]: https://doi.org/10.2514/6.1996-1389
[research_cabaleirodelahoz_fioriti_2021]: https://doi.org/10.1177/09544100211063110
[research_cahill_1986]: https://doi.org/10.4271/861846
[research_calculation_of_2004]: https://doi.org/10.1201/9780203021187.axa
[research_calder_gupta_1977]: https://doi.org/10.2514/6.1977-830
[research_campbell_smith_1987]: https://doi.org/10.2514/6.1987-2552
[research_candida_souzadepaula_2019]: https://doi.org/10.26678/abcm.diname2019.din2019-0103
[research_canfield_2014]: https://doi.org/10.21236/ada610546
[research_canniff_1969]: https://doi.org/10.2514/6.1969-842
[research_cao_lin_2025]: https://doi.org/10.2139/ssrn.5375639
[research_cao_lyu_2024]: https://doi.org/10.3390/act13090369
[research_cao_zhao_2024]: https://doi.org/10.23967/j.rimni.2024.03.004
[research_carafoli_1969]: https://doi.org/10.1016/b978-0-08-012330-1.50005-4
[research_carico_1998]: https://doi.org/10.21236/ada350677
[research_carlson_1981]: https://doi.org/10.1007/978-3-663-14008-5_11
[research_carlson_cassarino_1973]: https://doi.org/10.21236/ad0771963
[research_carlson_weed_1985]: https://doi.org/10.2514/6.1985-4075
[research_carlsson_2003]: https://doi.org/10.2514/6.2003-450
[research_carlsson_2004]: https://doi.org/10.2514/1.8431
[research_carlsson_2005]: https://doi.org/10.2514/1.5440
[research_carlsson_cronander_2005]: https://doi.org/10.1016/j.ast.2004.12.004
[research_carpenter_solomon_2018]: https://doi.org/10.2514/6.2018-3809
[research_carrillo_debreuker_2024]: https://doi.org/10.2514/6.2024-2590
[research_carrillo_mertens_2022]: https://doi.org/10.2514/6.2022-1559
[research_carruthers_taylor_2007]: https://doi.org/10.2514/6.2007-43
[research_carter]: https://doi.org/10.1109/dasc.1997.637229
[research_cartwright_2010]: https://doi.org/10.3833/pdr.v2010i8.1384
[research_cassel_durando_1969]: https://doi.org/10.21236/ad0862483
[research_castellani_cooper_2016]: https://doi.org/10.2514/6.2016-1573
[research_castellani_cooper_2016_b]: https://doi.org/10.1155/2016/4805817
[research_castellani_cooper_2017]: https://doi.org/10.2514/1.c033825
[research_castillozuniga_giacobinisouza_2019]: https://doi.org/10.2514/6.2019-2033
[research_caughey_1982]: https://doi.org/10.1016/b978-0-12-493280-7.50009-7
[research_caughey_jameson_1977]: https://doi.org/10.2514/6.1977-677
[research_cavagna_ricci_2009]: https://doi.org/10.1016/j.ast.2009.06.009
[research_cavagna_ricci_2011]: https://doi.org/10.2514/1.c031072
[research_cavaliere_fezans_2024]: https://doi.org/10.2514/1.g007762
[research_cavanaugh_robertson_2007]: https://doi.org/10.2514/6.2007-4175
[research_caverly_forbes_2017]: https://doi.org/10.2514/6.2017-1718
[research_cavin_holyoak_1978]: https://doi.org/10.2514/3.58355
[research_cazierjr_kehoe_1986]: https://doi.org/10.2514/6.1986-9730
[research_cea_palacios_2023]: https://doi.org/10.2514/1.c036740
[research_cea_palacios_2024]: https://doi.org/10.2139/ssrn.4970758
[research_cecrdle_2018]: https://doi.org/10.5772/intechopen.70171
[research_cecrdle_malinek_2022]: https://doi.org/10.21495/51-2-57
[research_celi_1991]: https://doi.org/10.2514/3.45991
[research_celi_1994]: https://doi.org/10.2514/6.1994-1544
[research_celik_metin_2026]: https://doi.org/10.24425/mms.2026.158365
[research_cella_biancolini_2012]: https://doi.org/10.2514/1.c031293
[research_cen_xu_2025]: https://doi.org/10.2139/ssrn.5759948
[research_cen_xu_2026]: https://doi.org/10.2139/ssrn.6797266
[research_cesnik_2002]: https://doi.org/10.21236/ada401331
[research_cesnik_2005]: https://doi.org/10.21236/ada439640
[research_cesnik_brown_2002]: https://doi.org/10.2514/6.2002-1719
[research_cesnik_ortegamorales_2000]: https://doi.org/10.2514/6.2000-1331
[research_cesnik_ritter_2023]: https://doi.org/10.52843/cassyni.70bjfs
[research_cesnik_shin_1999]: https://doi.org/10.4050/vfs-f55-00008
[research_cestino_iannuzzo_2026]: https://doi.org/10.2514/1.c038607
[research_chae_moosavian_2017]: https://doi.org/10.1115/smasis2017-3833
[research_chahmi_2022]: https://doi.org/10.1109/icaee53772.2022.9961981
[research_chajec_krzymien_2019]: https://doi.org/10.1108/aeat-12-2017-0279
[research_chakrabartty_dhanalakshmi_1995]: https://doi.org/10.2514/3.12756
[research_chakravarty_moore_1986]: https://doi.org/10.23919/acc.1986.4788989
[research_chan_hooker_2017]: https://doi.org/10.2514/6.2017-0098
[research_chand_hansen]: https://doi.org/10.1109/cdc.1989.70207
[research_chandrasekharan_iarocci_2015]: https://doi.org/10.4271/2015-01-2566
[research_chandrevila]: https://doi.org/10.70675/d83cfa8bz5f8fz4e1az8e9aze0b59b413f31
[research_chang_2005]: https://doi.org/10.4271/2005-01-2273
[research_chang_trivailo_2002]: https://doi.org/10.1142/9789812776228_0125
[research_chang_yang_2010]: https://doi.org/10.2514/6.2010-1510
[research_chaparro_fujiwara_2017]: https://doi.org/10.2514/6.2017-4221
[research_chapman_1969]: https://doi.org/10.1243/jmes_jour_1969_011_010_02
[research_chapman_yates_1992]: https://doi.org/10.2514/6.1992-4502
[research_chapter_15_1994]: https://doi.org/10.1515/9781400880034-018
[research_chapter_2_2005]: https://doi.org/10.1515/9781400866816-003
[research_chapter_3_1960]: https://doi.org/10.1515/9781400874941-004
[research_chapter_5_1957]: https://doi.org/10.1515/9781400879908-011
[research_chapter_iii_1982]: https://doi.org/10.1016/s0074-6142(08)60469-6
[research_charts_torsional_stiffness]: https://ntrs.nasa.gov/citations/19930092723
[research_chase]: https://doi.org/10.15368/theses.2014.38
[research_chase_mcdonald_2014]: https://doi.org/10.2514/6.2014-0033
[research_chawla_edwards_1988]: https://doi.org/10.2514/6.1988-2527
[research_chen_1982]: https://doi.org/10.2514/6.1982-162
[research_chen_2015]: https://doi.org/10.1142/9781783266852_0002
[research_chen_baldelli_2008]: https://doi.org/10.2514/6.2008-6376
[research_chen_cai_2026]: https://doi.org/10.1109/tie.2025.3639811
[research_chen_chang_1998]: https://doi.org/10.2514/6.1998-907
[research_chen_ding_2026]: https://doi.org/10.2139/ssrn.7319825
[research_chen_gray_2026]: https://doi.org/10.2514/6.2026-1489
[research_chen_han_2017]: https://doi.org/10.21595/mme.2017.18505
[research_chen_liu_2014]: https://doi.org/10.4028/www.scientific.net/amm.574.480
[research_chen_shi_2023]: https://doi.org/10.1063/5.0130370
[research_chen_shi_2023_b]: https://doi.org/10.1063/5.0162013
[research_chen_ulker_2009]: https://doi.org/10.2514/1.42489
[research_chen_vassberg_1984]: https://doi.org/10.2514/6.1984-2157
[research_chen_wickramasinghe_2006]: https://doi.org/10.1017/s000192400001318x
[research_chen_zhang_2026]: https://doi.org/10.2139/ssrn.7380660
[research_chen_zhou_2015]: https://doi.org/10.2514/6.2015-1176
[research_chen_zhou_2018]: https://doi.org/10.2514/1.c034621
[research_cheney_1988]: https://doi.org/10.2514/6.1988-2125
[research_cheng_1961]: https://doi.org/10.1115/1.3641678
[research_cheng_1982]: https://doi.org/10.1016/b978-0-12-493280-7.50010-3
[research_cheng_cea_2023]: https://doi.org/10.2514/6.2023-2073
[research_cheng_edwards_1987]: https://doi.org/10.1007/978-1-4612-4678-7_10
[research_cheng_shi_2023]: https://doi.org/10.3390/app13169277
[research_cheng_song_2025]: https://doi.org/10.2139/ssrn.5399002
[research_chestnutt_1966]: https://doi.org/10.21236/ad0629632
[research_cheung_palles_2023]: https://doi.org/10.2514/6.2023-1888
[research_cheung_rezgui_2019]: https://doi.org/10.2514/6.2019-1863
[research_cheung_rezgui_2019_b]: https://doi.org/10.2514/6.2019-1863.c1
[research_cheung_rezgui_2020]: https://doi.org/10.2514/1.c035732
[research_chin]: https://doi.org/10.15368/theses.2011.43
[research_chin_brenner_2011]: https://doi.org/10.2514/6.2011-6206
[research_chin_chacon_1987]: https://doi.org/10.2514/6.1987-2878
[research_chipman_zislin_1982]: https://doi.org/10.2514/6.1982-684
[research_chipman_zislin_1983]: https://doi.org/10.2514/3.48204
[research_choi_lim_2020]: https://doi.org/10.5139/jksas.2020.48.8.555
[research_chopra_1983]: https://doi.org/10.2514/6.1983-985
[research_chopra_1988]: https://doi.org/10.4050/jahs.33.60
[research_chung_2002]: https://doi.org/10.1007/s00193-002-0159-9
[research_chung_cho_2019]: https://doi.org/10.2514/6.2019-3591
[research_chung_lee_2002]: https://doi.org/10.2514/6.2002-2934
[research_chung_su_2021]: https://doi.org/10.3390/aerospace8060157
[research_chunshengliu_xinzhongzhu_2012]: https://doi.org/10.1109/acc.2012.6314694
[research_chyu_kuwahara_1982]: https://doi.org/10.2514/6.1982-350
[research_cicek_kayran_2019]: https://doi.org/10.1115/imece2019-11483
[research_ciniglio_manimala_2003]: https://doi.org/10.4050/vfs-f59-000140
[research_cizmas_strganac_2010]: https://doi.org/10.21236/ada563189
[research_clark_2001]: https://doi.org/10.21236/ada399161
[research_clark_2026]: https://doi.org/10.2514/6.2026-2112
[research_clark_valarezo_1990]: https://doi.org/10.2514/6.1990-31
[research_clarke_allen_2005]: https://doi.org/10.2514/6.2005-6316
[research_clarke_roskam_1982]: https://doi.org/10.2514/6.1982-1312
[research_cliett_1952]: https://doi.org/10.21236/ad0006050
[research_clyde_bonner_1984]: https://doi.org/10.21236/ada148355
[research_cocco_meroli_2026]: https://doi.org/10.4050/f-0082-2026-0187
[research_cockrell_doherr_1981]: https://doi.org/10.2514/6.1981-1940
[research_coder_2023]: https://doi.org/10.2514/6.2023-2452
[research_coder_2025]: https://doi.org/10.21203/rs.3.rs-6389577/v1
[research_coejr_perkins_1990]: https://doi.org/10.2514/6.1990-3074
[research_coetzee_lowenberg_2023]: https://doi.org/10.2514/6.2023-1311
[research_cole_1990]: https://doi.org/10.2514/6.1990-981
[research_cole_noll_2003]: https://doi.org/10.2514/2.6873
[research_cole_weiland_2009]: https://doi.org/10.1115/dscc2009-2679
[research_colombo_muscarello_2018]: https://doi.org/10.4050/f-0074-2018-12753
[research_comer_bhandari_2024]: https://doi.org/10.2514/6.2024-2644
[research_cong_hu_2023]: https://doi.org/10.3390/aerospace10030241
[research_conti_saltari_2021]: https://doi.org/10.2514/1.c036115
[research_control_allocation_2016]: https://doi.org/10.1002/9781118827789.ch8
[research_cook_1964]: https://doi.org/10.2514/6.1964-329
[research_cook_1965]: https://doi.org/10.2514/3.43636
[research_cook_smith_2014]: https://doi.org/10.2514/1.c032955
[research_cord_1989]: https://doi.org/10.2514/6.1989-3357
[research_corminboeuf_2015]: https://doi.org/10.1051/metrology/20150004004
[research_cornellaeronauticallabincbuffalony_1947]: https://doi.org/10.21236/ada800190
[research_correction_of_2017]: https://doi.org/10.17559/tv-20160525142932
[research_cosentino_holst_1985]: https://doi.org/10.2514/6.1985-424
[research_costa_vilela_2014]: https://doi.org/10.4271/2014-36-0234
[research_cotoi_botez_2002]: https://doi.org/10.2514/2.4975
[research_cotton_1974]: https://doi.org/10.21236/ada000894
[research_couch_duren_2001]: https://doi.org/10.4050/vfs-f57-05
[research_covell_miller_1986]: https://doi.org/10.2514/6.1986-315
[research_cowan_arenajr_1998]: https://doi.org/10.2514/6.1998-4152
[research_cox_roskam_1990]: https://doi.org/10.2514/6.1990-3231
[research_cramer_nguyen_2020]: https://doi.org/10.2514/6.2020-0211
[research_cranehl_reederjp_1945]: https://ntrs.nasa.gov/citations/20050028615
[research_crasta_khan_2014]: https://doi.org/10.9790/5728-10530108
[research_crawley_curtiss_1995]: https://doi.org/10.1007/978-94-011-0499-9_2
[research_cristofaro_2024]: https://doi.org/10.1002/oca.3222
[research_crites_rueger_1992]: https://doi.org/10.2514/6.1992-3983
[research_crittenden_weishaar_1978]: https://doi.org/10.2514/3.58383
[research_crittenden_weisshaar_1977]: https://doi.org/10.2514/6.1977-454
[research_cruz_kienitz_2007]: https://doi.org/10.4271/2007-01-2898
[research_cui_jianlong_2021]: https://doi.org/10.1515/mt-2020-0101
[research_cumming_diebler_2005]: https://doi.org/10.2514/6.2005-6312
[research_cunningham_1972]: https://doi.org/10.2514/3.59005
[research_cunningham_2017]: https://doi.org/10.2514/6.2017-1651
[research_cunningham_foster_2008]: https://doi.org/10.2514/6.2008-6200
[research_curpanaru_pastor_2025]: https://doi.org/10.2514/6.2025-3739
[research_currao_yeh_2026]: https://doi.org/10.2139/ssrn.6450319
[research_cusimano_johnson_1994]: https://doi.org/10.2514/6.1994-2120
[research_dai_qiu_2022]: https://doi.org/10.1007/s42401-022-00159-5
[research_dai_wu_2012]: https://doi.org/10.2514/6.2012-4771
[research_dai_zhang_2023]: https://doi.org/10.3390/aerospace10060553
[research_dale_cooper_2013]: https://doi.org/10.2514/6.2013-1510
[research_dale_cooper_2014]: https://doi.org/10.2514/6.2014-0763
[research_dallaire_tribes_2007]: https://doi.org/10.2514/6.2007-1866
[research_damveld_2004]: https://doi.org/10.2514/6.2004-5365
[research_dancila_botez_2014]: https://doi.org/10.2514/6.2014-2291
[research_daneshmehr_inman_2013]: https://doi.org/10.4028/www.scientific.net/amm.325-326.1318
[research_danowsky_brenner_2010]: https://doi.org/10.2514/6.2010-7500
[research_danowsky_lieu_2016]: https://doi.org/10.2514/6.2016-1749
[research_danowsky_schulze_2012]: https://doi.org/10.2514/6.2012-4950
[research_danowsky_thompson_2008]: https://doi.org/10.2514/6.2008-6370
[research_danowsky_thompson_2009]: https://doi.org/10.2514/6.2009-5708
[research_danowsky_thompson_2013]: https://doi.org/10.2514/6.2013-4743
[research_darabseh_tarabulsi_2022]: https://doi.org/10.1142/s0219455422501577
[research_darabseh_tarabulsi_2022_b]: https://doi.org/10.3390/aerospace9090475
[research_darden_1984]: https://doi.org/10.2514/6.1984-138
[research_darden_1985]: https://doi.org/10.2514/3.45082
[research_darida_smrcek_1998]: https://doi.org/10.2514/6.1998-2532
[research_das_2026]: https://doi.org/10.2514/6.2026-112783
[research_das_venkatraman_2021]: https://doi.org/10.2514/6.2021-0730
[research_davis]: https://doi.org/10.22215/etd/2006-07735
[research_davis_1974]: https://doi.org/10.21236/ad0782756
[research_daynes_lachenal_2015]: https://doi.org/10.1016/j.tws.2015.04.017
[research_deangelis_1981]: https://doi.org/10.2514/6.1981-2450
[research_deangelis_1982]: https://doi.org/10.2514/3.44816
[research_debreuker_binder_2018]: https://doi.org/10.2514/6.2018-0764
[research_decamp_hardy_1984]: https://doi.org/10.2514/6.1984-2088
[research_deconinck_hirsch_1981]: https://doi.org/10.1007/978-3-663-14008-5_7
[research_deere_pao_2011]: https://doi.org/10.2514/6.2011-172
[research_definition_of_1954]: https://doi.org/10.59161/cgpm1954res4e
[research_deflection_loads_flight]: https://ntrs.nasa.gov/citations/20050160482
[research_degaspari_ricci_2007]: https://doi.org/10.2514/6.2007-2138
[research_degaspari_ricci_2015]: https://doi.org/10.2514/6.2015-1054
[research_dehaan_1990]: https://doi.org/10.2514/6.1990-3062
[research_deiler_2016]: https://doi.org/10.2514/6.2016-3852
[research_deitering_hilliard_1965]: https://doi.org/10.21236/ad0464786
[research_delaurier_2024]: https://doi.org/10.1201/9781032709093-4
[research_delgado_datta_2026]: https://doi.org/10.2514/1.c038396
[research_delgadoregis_mattos_2004]: https://doi.org/10.2514/6.2004-5192
[research_demasi_2024]: https://doi.org/10.1007/978-3-031-50054-1_34
[research_demasi_livne_2005]: https://doi.org/10.2514/6.2005-2172
[research_demelo_bussamra_2024]: https://doi.org/10.21203/rs.3.rs-3761279/v1
[research_demenkov_2009]: https://doi.org/10.1109/cca.2009.5280946
[research_demo_1986]: https://doi.org/10.2514/6.1986-9797
[research_demourant_ferreres_2013]: https://doi.org/10.1051/eucass/201306729
[research_denegri_dubben_2003]: https://doi.org/10.2514/6.2003-1426
[research_denegri_dubben_2005]: https://doi.org/10.2514/1.1345
[research_dennispdykstra_1980]: https://doi.org/10.13031/2013.34619
[research_desmarais_reediii_1980]: https://doi.org/10.2514/6.1980-792
[research_dessi_mastroddi_2002]: https://doi.org/10.1115/imece2002-33065
[research_development_of_2012]: https://doi.org/10.2514/5.9781600868207.0645.0718
[research_devisser_1999]: https://doi.org/10.2514/6.1999-1258
[research_devisser_mulder_2009]: https://doi.org/10.2514/6.2009-5726
[research_devisser_pool_2023]: https://doi.org/10.2514/1.c037283
[research_devries_vankampen_2019]: https://doi.org/10.2514/6.2019-0144
[research_dhital_chouvion_2024]: https://doi.org/10.20944/preprints202411.1381.v1
[research_dias_2023]: https://doi.org/10.2514/1.c037252
[research_dias_demarqui_2015]: https://doi.org/10.2514/1.j053108
[research_dias_girardi_2016]: https://doi.org/10.2514/6.2016-2012
[research_dibley_allen_2005]: https://doi.org/10.2514/6.2005-6314
[research_dicarlo_brown_1992]: https://doi.org/10.2514/6.1992-4094
[research_diedrich_1971]: https://doi.org/10.2514/6.1971-742
[research_dieterich_enenkl_2006]: https://doi.org/10.4050/vfs-f62-075
[research_dillenius_mcintoshjr_1988]: https://doi.org/10.2514/6.1988-528
[research_dillinger_meddaikar_2020]: https://doi.org/10.3390/fluids5010035
[research_dillsaver_cesnik_2011]: https://doi.org/10.2514/6.2011-6368
[research_dilmi_2022]: https://doi.org/10.1061/(asce)as.1943-5525.0001401
[research_dimino_andreutti_2021]: https://doi.org/10.3390/app11052439
[research_dimitriadis_2008]: https://doi.org/10.2514/1.30472
[research_dimitriadis_2011]: https://doi.org/10.2514/1.c031139
[research_dinyavari_friedmann_1986]: https://doi.org/10.2514/3.9459
[research_dipasquale_2024]: https://doi.org/10.2514/6.2024-2723
[research_dipasquale_prince_2023]: https://doi.org/10.3390/aerospace10060569
[research_disney_1975]: https://doi.org/10.2514/6.1975-991
[research_disney_1977]: https://doi.org/10.2514/3.57164
[research_diwekar_yedavalli_1995]: https://doi.org/10.2514/6.1995-3340
[research_dixit_kodhanda_2016]: https://doi.org/10.1109/iciinfs.2016.8262981
[research_dixon_1963]: https://doi.org/10.2514/6.1963-1029
[research_dixon_1972]: https://doi.org/10.2514/6.1972-781
[research_djayapertapa_allen_2002]: https://doi.org/10.2514/6.2002-2713
[research_djojodihardjo_2023]: https://doi.org/10.1007/978-981-16-8078-6_19
[research_djojodihardjo_2023_b]: https://doi.org/10.1007/978-981-16-8078-6_5
[research_djojodihardjo_2023_c]: https://doi.org/10.1007/978-981-16-8078-6_15
[research_dobbs_miller_1985]: https://doi.org/10.2514/6.1985-739
[research_dobronski_1988]: https://doi.org/10.2514/6.1988-2119
[research_doman_gamble_2007]: https://doi.org/10.2514/6.2007-6778
[research_doman_gamble_2009]: https://doi.org/10.2514/1.37312
[research_doman_oppenheimer_2002]: https://doi.org/10.2514/6.2002-4667
[research_done_1996]: https://doi.org/10.1017/s0001924000028906
[research_dong_lu_2016]: https://doi.org/10.1155/2016/5037678
[research_dong_zhou_2024]: https://doi.org/10.2139/ssrn.4950726
[research_dooley_1965]: https://doi.org/10.1016/0020-7403(65)90017-2
[research_dooley_yeary_1979]: https://doi.org/10.21236/ada071648
[research_dorin_smolin_1977]: https://doi.org/10.1007/bf00817129
[research_dowell_1983]: https://doi.org/10.21236/ada135133
[research_dowell_1990]: https://doi.org/10.21236/ada227930
[research_dowell_1996]: https://doi.org/10.21236/ada325524
[research_dowell_1999]: https://doi.org/10.21236/ada362982
[research_dowell_2001]: https://doi.org/10.21236/ada389366
[research_dowell_2021]: https://doi.org/10.1007/978-3-030-74236-2_2
[research_dowell_attar_2006]: https://doi.org/10.21236/ada469723
[research_dowell_curtiss_1989]: https://doi.org/10.1007/978-94-015-7858-5_2
[research_downs_prazenica_2022]: https://doi.org/10.2514/6.2022-1729
[research_downs_prazenica_2023]: https://doi.org/10.2514/6.2023-0130
[research_dracopoulos_oz_1988]: https://doi.org/10.1007/978-3-642-61381-4_325
[research_dracopoulos_oz_1992]: https://doi.org/10.2514/3.46156
[research_drake_balakrishnan_2004]: https://doi.org/10.2514/6.2004-4816
[research_dreier_1987]: https://doi.org/10.2514/6.1987-2500
[research_drew_hashemi_2020]: https://doi.org/10.2514/6.2020-0213
[research_drouet_champoux_2014]: https://doi.org/10.1016/j.proeng.2014.06.016
[research_duan_kolmanovsky_2021]: https://doi.org/10.2514/6.2021-0501
[research_duan_zhang_2018]: https://doi.org/10.1142/s021945541850150x
[research_dubigeon_1992]: https://doi.org/10.2514/3.11232
[research_dubnicky_splichal_2023]: https://doi.org/10.21495/em2023-59
[research_duessler_mylvaganam_2023]: https://doi.org/10.2514/6.2023-2571
[research_duessler_mylvaganam_2024]: https://doi.org/10.2514/6.2024-0614
[research_duffy_1989]: https://doi.org/10.2514/6.1989-3383
[research_dumpleton_1987]: https://doi.org/10.1080/03052158708941082
[research_duncan_1950]: https://doi.org/10.1017/s0001925900000378
[research_dunning_stanford_2014]: https://doi.org/10.2514/6.2014-0344
[research_dupelouxdesaintromain]: https://doi.org/10.70675/0bb39fd4z79c9z4517z8183z84c411f70c12
[research_durham_bordignon_2016]: https://doi.org/10.1002/9781118827789
[research_durmaz_kaya_2013]: https://doi.org/10.1115/imece2013-64261
[research_durston_stonum_1987]: https://doi.org/10.4271/872311
[research_dvari_baker_1999]: https://doi.org/10.2514/2.2421
[research_dwyer_1994]: https://doi.org/10.2514/6.1994-2158
[research_dynamic_force]: https://doi.org/10.3403/00024595
[research_dynamic_lateral_directional_2003]: https://doi.org/10.2514/5.9781600861840.0311.0322
[research_eastep_andersen_1998]: https://doi.org/10.2514/6.1998-4932
[research_eastep_tischler_1999]: https://doi.org/10.2514/2.2546
[research_eckstrom_spain_1982]: https://doi.org/10.2514/6.1982-678
[research_ecsedi_2000]: https://doi.org/10.1016/s0093-6413(00)00110-5
[research_edwards_1992]: https://doi.org/10.2514/6.1992-4002
[research_edwards_carter_1985]: https://doi.org/10.2514/6.1985-371
[research_edwards_fittante_1997]: https://doi.org/10.21236/ada325252
[research_edwards_whitfield_1986]: https://doi.org/10.1007/978-3-642-82770-9_7
[research_effective_torsional_1976]: https://doi.org/10.14359/11098
[research_efremov_1992]: https://doi.org/10.1007/bf00847286
[research_eguea]: https://doi.org/10.11606/d.18.2019.tde-05072019-144340
[research_ehlers_weisshaar_1992]: https://doi.org/10.2514/6.1992-2526
[research_ehlers_weisshaar_1993]: https://doi.org/10.2514/3.46376
[research_eichelsdorfer_2026]: https://doi.org/10.2514/6.2026-1556
[research_eichelsdorfer_2026_b]: https://doi.org/10.2514/6.2026-1555
[research_elastic_and_2008]: https://doi.org/10.1017/cbo9780511801631.034
[research_elastic_torsional_1965]: https://doi.org/10.14359/7706
[research_eldwaib_grbovic_2018]: https://doi.org/10.1016/j.prostr.2018.12.074
[research_elham_bahamondejacome_2016]: https://doi.org/10.2514/6.2016-1660
[research_elham_timmer_2016]: https://doi.org/10.2514/6.2016-0160
[research_elhami_narab_2012]: https://doi.org/10.1109/acc.2012.6314699
[research_ellers_boggs_2003]: https://doi.org/10.1554/0014-3820(2003)057[1100:teowcm]2.0.co;2
[research_ellis_hui_2001]: https://doi.org/10.2514/6.2001-4012
[research_elshazly_kassem_2025]: https://doi.org/10.1088/1742-6596/3070/1/012001
[research_energy_approach_2003]: https://doi.org/10.2514/5.9781600861840.0143.0151
[research_engel_miller]: https://doi.org/10.1109/ectc.1992.204259
[research_engelien_1994]: https://doi.org/10.2514/6.1994-2121
[research_epple_altenbach_1982]: https://doi.org/10.2514/6.1982-1531
[research_epstein_1954]: https://doi.org/10.21236/ad0037709
[research_epureanu_2001]: https://doi.org/10.2514/6.2001-4200
[research_eraslan_oktay_2023]: https://doi.org/10.5755/j01.itc.52.4.33527
[research_eraslan_oktay_2024]: https://doi.org/10.28948/ngumuh.1501418
[research_erdman_2005]: https://doi.org/10.21236/ada435347
[research_ericsson_reding_1981]: https://doi.org/10.2514/6.1981-1672
[research_eskandary_dardel_2012]: https://doi.org/10.1016/j.actaastro.2011.07.017
[research_eslimyisfahany_banerjee_1995]: https://doi.org/10.2514/6.1995-1448
[research_eslimyisfahany_banerjee_1996]: https://doi.org/10.1006/jsvi.1996.0421
[research_espana_gilyard_1995]: https://doi.org/10.1016/b978-0-08-042238-1.50009-4
[research_espna_gilyard_1994]: https://doi.org/10.1016/s1474-6670(17)45775-2
[research_essenhigh_2006]: https://doi.org/10.1021/ef050276y
[research_etnier_2001]: https://doi.org/10.2307/1543080
[research_eulrich_rynaski_1980]: https://doi.org/10.2514/6.1980-1633
[research_everett_cashwell_1972]: https://doi.org/10.2172/4635208
[research_eversman_dandaroy_1996]: https://doi.org/10.2514/6.1996-1345
[research_eversman_roy_1997]: https://doi.org/10.2514/2.2163
[research_exploring_the_2015]: https://doi.org/10.2307/j.ctt1287kgx.5
[research_ezawa_nakatsugawa_2024]: https://doi.org/10.2139/ssrn.4780376
[research_f_m_strain_1975]: https://doi.org/10.1111/j.1475-1305.1975.tb00165.x
[research_fagbade_heinz_2024]: https://doi.org/10.3390/app14072705
[research_faisse]: https://doi.org/10.70675/c7bfd6f3z9deez44edz8b34zc551fda30c97
[research_faisse_vernay_2021]: https://doi.org/10.2514/6.2021-0892
[research_faisse_vernay_2022]: https://doi.org/10.2514/6.2022-2243
[research_fan_hall_2014]: https://doi.org/10.4050/f-0070-2014-9498
[research_fan_liu_2017]: https://doi.org/10.2514/6.2017-1721
[research_fan_lutze_1996]: https://doi.org/10.2514/6.1996-3407
[research_fang_wang_2025]: https://doi.org/10.1016/j.tws.2024.112567
[research_fang_yang_2025]: https://doi.org/10.1016/j.jobe.2025.112978
[research_farbridge_smith_1977]: https://doi.org/10.2514/6.1977-606
[research_farbridge_woodward_1956]: https://doi.org/10.1108/eb032701
[research_farhangnia_guruswamy_1996]: https://doi.org/10.2514/6.1996-286
[research_farhat_2001]: https://doi.org/10.21236/ada397705
[research_farhat_amsallem_2011]: https://doi.org/10.21236/ada566361
[research_farhat_lin_1990]: https://doi.org/10.2514/6.1990-3053
[research_faroughi_malekzadeh_2012]: https://doi.org/10.1177/1077546312455211
[research_farsadi_ahmadi_2026]: https://doi.org/10.2514/1.j066652
[research_fasel_2020]: https://doi.org/10.52843/cassyni.tbr8qg
[research_favale_haidar_2021]: https://doi.org/10.4050/f-0077-2021-16766
[research_fay_johnstone_1960]: https://doi.org/10.21236/ad0248516
[research_fechter_mills_1988]: https://doi.org/10.2514/6.1988-2174
[research_fejtek_1994]: https://doi.org/10.2514/6.1994-2604
[research_felker_1992]: https://doi.org/10.2514/6.1992-2123
[research_felker_1993]: https://doi.org/10.2514/3.11331
[research_felt_huttsell_1978]: https://doi.org/10.2514/6.1978-1289
[research_feng_liu_2015]: https://doi.org/10.1115/smasis2015-9116
[research_feng_liu_2015_b]: https://doi.org/10.1088/0964-1726/24/3/035023
[research_fernandezescudero]: https://doi.org/10.70675/b3e6d75bz90efz4ee7zb097z170728fe1dd6
[research_ferrara_2025]: https://doi.org/10.5040/9781350426351.ch-4
[research_ferreres_puyou_2006]: https://doi.org/10.2514/1.18535
[research_ferrier_nguyen_2018]: https://doi.org/10.2514/6.2018-0620
[research_fezans_2017]: https://doi.org/10.1007/978-3-319-65283-2_3
[research_fezans_joos_2017]: https://doi.org/10.2514/6.2017-3548
[research_fezans_joos_2019]: https://doi.org/10.1007/s13272-019-00362-9
[research_fichera_isnardi_2019]: https://doi.org/10.3390/aerospace6020013
[research_filippou_kilimtzidis_2024]: https://doi.org/10.20944/preprints202401.0348.v1
[research_filippou_sodja_2026]: https://doi.org/10.2139/ssrn.6828778
[research_finnestead_connor_1970]: https://doi.org/10.21236/ad0874210
[research_fischenberg_1995]: https://doi.org/10.2514/6.1995-3438
[research_fisher_gertsen_1956]: https://doi.org/10.21236/ad0092459
[research_fitzgerald_ralston_1994]: https://doi.org/10.2514/6.1994-3400
[research_flexible_manufacturing_2003]: https://doi.org/10.1108/aeat.2003.12775fab.001
[research_flight_envelope]: https://doi.org/10.4271/arp4104/1
[research_flight_envelope_2005]: https://doi.org/10.1002/0471743984.vse3286
[research_flight_envelope_2021]: https://doi.org/10.2514/5.9781624105920.0355.0410
[research_flight_loads_prediction_1981]: https://doi.org/10.17226/19736
[research_flight_test_1979]: https://doi.org/10.2514/6.1979-1703
[research_flight_testing_1992]: https://ntrs.nasa.gov/citations/19930010712
[research_flores_vandalsem_1985]: https://doi.org/10.2514/6.1985-5004
[research_floros_kang_2017]: https://doi.org/10.4050/f-0073-2017-12057
[research_foley_woodrey_1980]: https://doi.org/10.2514/6.1980-1877
[research_fonte_iannaccone_2018]: https://doi.org/10.1115/smasis2018-8167
[research_fonte_mantegazza_2017]: https://doi.org/10.2514/6.2017-1361
[research_fonte_ricci_2015]: https://doi.org/10.2514/1.c032995
[research_fonte_toffol_2018]: https://doi.org/10.2514/6.2018-1442
[research_fonzi_ricci_2024]: https://doi.org/10.2514/6.2024-1269
[research_fonzi_ricci_2025]: https://doi.org/10.1016/j.jfluidstructs.2025.104332
[research_force_measurement]: https://doi.org/10.3403/02919794u
[research_fornasier_heiss_1987]: https://doi.org/10.2514/6.1987-2619
[research_forsey_1983]: https://doi.org/10.2514/6.1983-1805
[research_forster_kolonay_1996]: https://doi.org/10.2514/6.1996-4010
[research_forster_sanders_2002]: https://doi.org/10.2514/6.2002-5404
[research_forte_nguyen_2022]: https://doi.org/10.2514/6.2022-0715
[research_forte_nguyen_2023]: https://doi.org/10.2514/6.2023-0881
[research_forte_nguyen_2024]: https://doi.org/10.2514/6.2024-1782
[research_forte_nguyen_2026]: https://doi.org/10.2514/6.2026-2109
[research_forte_nguyen_2026_b]: https://doi.org/10.2514/6.2026-1836
[research_forte_nguyen_2026_c]: https://doi.org/10.2514/6.2026-1839
[research_forte_nguyen_2026_d]: https://doi.org/10.2514/6.2026-1840
[research_forte_nguyen_2026_e]: https://doi.org/10.2514/6.2026-2895
[research_fosdick_1970]: https://doi.org/10.21236/ad0880677
[research_foster_1966]: https://doi.org/10.1088/0950-7671/43/3/421
[research_fournier]: https://doi.org/10.70675/740d6648z220fz43a1zbeaczdfda6e921f86
[research_fournier_massioni_2022]: https://doi.org/10.2514/1.g006084
[research_frame_wise_control_2016]: https://doi.org/10.1002/9781118827789.ch7
[research_frampton_clark_1998]: https://doi.org/10.2514/6.1998-1980
[research_franciscopena_benjaminpark_2024]: https://ntrs.nasa.gov/citations/20240008449
[research_franciscus_1983]: https://doi.org/10.2514/6.1983-2541
[research_franklin_2018]: https://doi.org/10.1201/9781315136820-5
[research_franze_mattei_2013]: https://doi.org/10.1109/cdc.2013.6760903
[research_freidmann_2001]: https://doi.org/10.2514/6.2001-1534
[research_french_1988]: https://doi.org/10.2514/6.1988-2139
[research_french_eastep_1996]: https://doi.org/10.2514/3.46922
[research_friedmann_1973]: https://doi.org/10.2514/3.60270
[research_friedmann_1977]: https://doi.org/10.2514/3.58887
[research_friedmann_1987]: https://doi.org/10.1016/s0889-9746(87)90194-0
[research_friedmann_1989]: https://doi.org/10.2514/6.1989-1321
[research_friedmann_1990]: https://doi.org/10.2514/6.1990-1115
[research_friedmann_1992]: https://doi.org/10.2514/6.1992-2107
[research_friedmann_1998]: https://doi.org/10.21236/ada351094
[research_friedmann_2000]: https://doi.org/10.21236/ada387479
[research_friedmann_2001]: https://doi.org/10.2514/6.2001-427
[research_friedmann_2004]: https://doi.org/10.2514/1.9022
[research_friedmann_2010]: https://doi.org/10.1002/9780470686652.eae155
[research_friedmann_hodges_2003]: https://doi.org/10.2514/6.2003-1817
[research_friedmann_hodges_2003_b]: https://doi.org/10.2514/2.7216
[research_friedmann_straub_1980]: https://doi.org/10.4050/jahs.25.1.36
[research_friedmann_venkatesan_1992]: https://doi.org/10.2514/6.1992-4779
[research_frierson_moore_1978]: https://doi.org/10.2514/3.58341
[research_frierson_vanmeter_1977]: https://doi.org/10.2514/6.1977-1067
[research_frost_taylor_2012]: https://doi.org/10.2514/6.2012-4858
[research_frostsusana_wrightcameronhg_2015]: https://ntrs.nasa.gov/citations/20190001122
[research_fruchtman_1974]: https://doi.org/10.1115/74-gt-80
[research_fuchs_1981]: https://doi.org/10.1007/978-3-663-14008-5_6
[research_fujii_obayashi_1986]: https://doi.org/10.2514/6.1986-1831
[research_fujimori_nikiforuk_1995]: https://doi.org/10.1016/b978-0-08-042238-1.50041-0
[research_fujimori_ohta_1989]: https://doi.org/10.1016/s1474-6670(17)53399-6
[research_fujimori_ohta_1990]: https://doi.org/10.1016/b978-0-08-037027-9.50024-0
[research_fukumoto_kouchi_2023]: https://doi.org/10.2514/6.2023-1180
[research_further_development_1994]: https://doi.org/10.2514/6.1994-2141
[research_gabel_ricks_1961]: https://doi.org/10.21236/ad0267342
[research_gade_inman_1996]: https://doi.org/10.1115/imece1996-0909
[research_gade_inman_1997]: https://doi.org/10.2514/2.4139
[research_gai_seffen_2025]: https://doi.org/10.2514/6.2025-1088.c1
[research_gai_sun_2019]: https://doi.org/10.1109/safeprocess45799.2019.9213444
[research_gai_wang_2013]: https://doi.org/10.1016/j.cja.2013.04.031
[research_gallagher_wei_2008]: https://doi.org/10.4050/vfs-f64-000306
[research_galloping_and_2019]: https://doi.org/10.1002/9781119375890.ch20
[research_galloway_gelhausen_1992]: https://doi.org/10.2514/6.1992-4230
[research_gally_carlson_1987]: https://doi.org/10.2514/6.1987-2551
[research_galway_1980]: https://doi.org/10.21236/ada090484
[research_gamboa_santos_2016]: https://doi.org/10.2514/6.2016-0317
[research_gandhi_cooper_2009]: https://doi.org/10.2514/6.2009-5890
[research_gandhi_hathaway_1998]: https://doi.org/10.2514/2.2341
[research_gangsaas_ly_1981]: https://doi.org/10.2514/6.1981-21
[research_ganguli_chopra_1995]: https://doi.org/10.2514/3.46882
[research_ganguli_chopra_1997]: https://doi.org/10.4050/jahs.42.218
[research_gao_an_2021]: https://doi.org/10.1016/b978-0-12-822990-3.00008-5
[research_gao_an_2021_b]: https://doi.org/10.1016/b978-0-12-822990-3.00004-8
[research_gao_liu_2024]: https://doi.org/10.1016/j.ast.2024.109671
[research_garcia_2005]: https://doi.org/10.2514/1.6544
[research_garcia_abdulrahim_2003]: https://doi.org/10.2514/6.2003-5347
[research_garcia_guruswamy_1999]: https://doi.org/10.2514/6.1999-796
[research_garciavelo_walker_1995]: https://doi.org/10.2514/6.1995-3500
[research_garrard_liebst_1983]: https://doi.org/10.2514/6.1983-2222
[research_garrard_liebst_1985]: https://doi.org/10.2514/3.19980
[research_garrickie_rubinowsi_1946]: https://ntrs.nasa.gov/citations/19930081835
[research_garrickie_rubinowsi_1946_b]: https://ntrs.nasa.gov/citations/19930090942
[research_garud_ajluni_2024]: https://doi.org/10.2514/6.2024-84867
[research_gasbarri_chiwiacowsky_2009]: https://doi.org/10.1007/s00158-009-0429-6
[research_gasparetto]: https://doi.org/10.22215/etd/2021-14645
[research_gaspari_ricci_2009]: https://doi.org/10.2514/1.34649
[research_gauthamvigneswar_ali_2025]: https://doi.org/10.1115/imece-india2025-159737
[research_gauthamvigneswar_ali_2025_b]: https://doi.org/10.1177/10996362251383075
[research_geisbauer_2011]: https://doi.org/10.2514/6.2011-3811
[research_generalized_predictive_1997]: https://doi.org/10.1109/37.608553
[research_gennaretti_2024]: https://doi.org/10.1007/978-3-031-53379-2_4
[research_gennaretti_ponzi_1999]: https://doi.org/10.1017/s0001924000064964
[research_georgiou_manan_2012]: https://doi.org/10.1016/j.ymssp.2012.05.003
[research_gera_wilson_1981]: https://doi.org/10.2514/6.1981-2505
[research_gern_2001]: https://doi.org/10.1006/rwvb.2001.0194
[research_gern_ko_2000]: https://doi.org/10.2514/6.2000-4826
[research_gern_librescu_1998]: https://doi.org/10.2514/2.499
[research_gern_librescu_2000]: https://doi.org/10.2514/2.2718
[research_ghalandari_mahariq_2022]: https://doi.org/10.32604/cmc.2022.020884
[research_ghee_taylor_2000]: https://doi.org/10.21236/ada377908
[research_ghee_taylor_2004]: https://doi.org/10.2514/6.2004-4843
[research_ghiringhelli_lanz_1990]: https://doi.org/10.2514/3.25277
[research_ghiringhelli_lanz_1992]: https://doi.org/10.1016/b978-0-12-012752-8.50007-6
[research_ghorawat_lee_2015]: https://doi.org/10.2514/6.2015-2555
[research_ghorawat_lee_2016]: https://doi.org/10.2514/6.2016-1866
[research_ghosh_patil_2022]: https://doi.org/10.2514/6.2022-1126
[research_ghosh_raisinghani_1993]: https://doi.org/10.2514/6.1993-3640
[research_ghosh_raisinghani_1994]: https://doi.org/10.2514/3.46510
[research_giansante_bernardini_2022]: https://doi.org/10.3390/app122312204
[research_gibson_1981]: https://doi.org/10.2514/6.1981-2507
[research_gibson_ung_1995]: https://doi.org/10.2514/6.1995-1201
[research_giese_reich_1996]: https://doi.org/10.21236/ada399629
[research_giesseler_kopf_2012]: https://doi.org/10.3182/20120823-5-nl-3013.00049
[research_gilbert_schmidt_1982]: https://doi.org/10.2514/6.1982-1544
[research_gilbert_schmidt_1984]: https://doi.org/10.2514/3.8566
[research_gilbert_silva_1987]: https://doi.org/10.2514/6.1987-2563
[research_gilbertmichaelg_1989]: https://ntrs.nasa.gov/citations/19890015868
[research_gimmestad_1979]: https://doi.org/10.2514/6.1979-726
[research_gimmestad_1981]: https://doi.org/10.2514/6.1981-607
[research_gimmestad_1981_b]: https://doi.org/10.2514/6.1981-1671
[research_giraud_raibaudo_2021]: https://doi.org/10.1007/978-981-33-4960-5_36
[research_giunta_1999]: https://doi.org/10.1016/s1369-8869(99)00016-6
[research_gloss_washburn_1977]: https://doi.org/10.2514/6.1977-1132
[research_gloss_washburn_1978]: https://doi.org/10.2514/3.58347
[research_gobal_grandhi_2015]: https://doi.org/10.2514/6.2015-0766
[research_goizueta_drachinsky_2021]: https://doi.org/10.2514/6.2021-1711
[research_goizueta_wynn_2022]: https://doi.org/10.2514/1.c036710
[research_goland_1952]: https://doi.org/10.21236/ad0004240
[research_gomec_unver_2020]: https://doi.org/10.2514/6.2020-0278
[research_gomec_unver_2020_b]: https://doi.org/10.2514/6.2020-0278.c1
[research_gomillion_1976]: https://doi.org/10.21236/ada029144
[research_gonzales_sakaue_2022]: https://doi.org/10.1016/j.ast.2022.107718
[research_gooch_2011]: https://doi.org/10.1007/978-1-4419-6247-8_879
[research_gooch_2011_b]: https://doi.org/10.1007/978-1-4419-6247-8_11129
[research_goodman_conigliaro_1986]: https://doi.org/10.2514/6.1986-9774
[research_gorbushin_kozik_2024]: https://doi.org/10.1016/j.measurement.2024.114176
[research_gordnier_1993]: https://doi.org/10.2514/6.1993-2975
[research_gordnier_attar_2012]: https://doi.org/10.2514/6.2012-711
[research_goupil]: https://doi.org/10.15368/theses.2020.10
[research_gowtham_baashkaran_2023]: https://doi.org/10.4271/2023-01-5060
[research_graham_deoliveira_2007]: https://doi.org/10.2514/6.2007-6300
[research_grant_nelson_1989]: https://doi.org/10.21236/ada214778
[research_grantz_1985]: https://doi.org/10.2514/6.1985-5005
[research_grantz_marchman_1983]: https://doi.org/10.2514/3.44846
[research_grasmeyer_1999]: https://doi.org/10.2514/6.1999-10
[research_gratton_2014]: https://doi.org/10.1007/978-3-319-11409-5_4
[research_gratton_2018]: https://doi.org/10.1007/978-3-319-75617-2_4
[research_grauer_2016]: https://doi.org/10.2514/6.2016-2009
[research_grauer_boucher_2017]: https://doi.org/10.2514/6.2017-0699
[research_grauer_heeg_2012]: https://doi.org/10.2514/6.2012-4641
[research_grauer_morelli_2014]: https://doi.org/10.2514/6.2014-0542
[research_grauer_morelli_2023]: https://doi.org/10.2514/1.c037583
[research_grauer_waite_1986]: https://doi.org/10.2514/6.1986-2242
[research_grauer_waite_2024]: https://doi.org/10.2514/6.2024-2201
[research_graves_burner_2002]: https://doi.org/10.2514/6.2002-3136
[research_gray_martins_2024]: https://doi.org/10.2514/6.2024-2775.c1
[research_green_1986]: https://doi.org/10.2514/6.1986-1021
[research_green_1987]: https://doi.org/10.2514/3.45525
[research_green_fernandez_1994]: https://doi.org/10.2514/6.1994-2107
[research_greenwell_2004]: https://doi.org/10.2514/6.2004-5276
[research_greer_sardahi_2021]: https://doi.org/10.23919/acc50511.2021.9483198
[research_gregg_misegades_1987]: https://doi.org/10.2514/6.1987-520
[research_gregory_cao_2007]: https://doi.org/10.2514/6.2007-6525
[research_gregory_mccrink_2016]: https://doi.org/10.2514/6.2016-0270
[research_gregory_xargay_2011]: https://doi.org/10.2514/6.2011-6608
[research_griffin]: https://doi.org/10.33915/etd.1826
[research_griffin_2006]: https://doi.org/10.2514/6.2006-2163
[research_griffin_eastep_1981]: https://doi.org/10.2514/6.1981-637
[research_grigorie_botez_2009]: https://doi.org/10.2514/6.2009-5893
[research_grigorie_botez_2014]: https://doi.org/10.2514/6.2014-2187
[research_grigorie_botez_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00012-5
[research_grigorie_popov_2011]: https://doi.org/10.2514/6.2011-6460
[research_grismer_kinsey_2000]: https://doi.org/10.2514/6.2000-4325
[research_gross_2002]: https://doi.org/10.2514/6.2002-310
[research_gross_chandler_1986]: https://doi.org/10.23919/acc.1986.4789163
[research_grosser_1965]: https://doi.org/10.2514/6.1965-789
[research_ground_and_2000]: https://doi.org/10.2514/5.9781600866555.0197.0224
[research_grove_2006]: https://doi.org/10.2514/6.2006-854
[research_gu_healy_2024]: https://doi.org/10.2514/6.2024-0618
[research_gu_healy_2024_b]: https://doi.org/10.2514/1.j063646
[research_guan_xing_2025]: https://doi.org/10.23919/ccc64809.2025.11178863
[research_guangming_zhengfeng_2009]: https://doi.org/10.1109/ifcsta.2009.345
[research_guderley_1987]: https://doi.org/10.21236/ada193773
[research_guderley_1988]: https://doi.org/10.21236/ada191408
[research_guerreiro_hubbard_2008]: https://doi.org/10.2514/6.2008-328
[research_guillot_friedmann_1994]: https://doi.org/10.2514/6.1994-1721
[research_guillot_friedmann_1994_b]: https://doi.org/10.1115/imece1994-1447
[research_gujjula_singh_2005]: https://doi.org/10.2514/6.2005-6263
[research_gunasekaran_mukherjee_2016]: https://doi.org/10.2514/6.2016-1779
[research_guo_cao_2018]: https://doi.org/10.1007/s11071-018-4398-4
[research_guo_shen_2018]: https://doi.org/10.4208/aamm.oa-2017-0342
[research_guo_yan_2022]: https://doi.org/10.3390/act11110309
[research_gupta_1996]: https://doi.org/10.2514/3.47046
[research_gupta_2011]: https://doi.org/10.1007/978-3-642-23412-5_5
[research_gupta_2012]: https://doi.org/10.2514/6.2012-2603
[research_gupta_2019]: https://doi.org/10.1007/978-3-030-12465-6_5
[research_gupta_datta_2021]: https://doi.org/10.2514/6.2021-2756
[research_gupta_doyle_2005]: https://doi.org/10.2514/6.2005-233
[research_guptakk_brennermj_1987]: https://ntrs.nasa.gov/citations/19870046442
[research_guptakk_brennermj_1991]: https://ntrs.nasa.gov/citations/19910016799
[research_gurbacki_bragg_1999]: https://doi.org/10.2514/6.1999-3149
[research_gurbacki_bragg_2001]: https://doi.org/10.2514/2.2801
[research_guruswamy_1992]: https://doi.org/10.2514/6.1992-4680
[research_guruswamy_2019]: https://doi.org/10.1016/j.ifacsc.2019.100057
[research_guruswamy_tu_1989]: https://doi.org/10.2514/3.45820
[research_guruswamy_tu_1994]: https://doi.org/10.2514/6.1994-1725
[research_gutierrez_tate_1994]: https://doi.org/10.2514/6.1994-2558
[research_gwin_1974]: https://doi.org/10.2514/6.1974-349
[research_gwin_1976]: https://doi.org/10.2514/3.58668
[research_haas_chopra_1987]: https://doi.org/10.2514/6.1987-920
[research_haas_chopra_1988]: https://doi.org/10.2514/3.45684
[research_haas_chopra_1989]: https://doi.org/10.2514/6.1989-1184
[research_haas_chopra_1990]: https://doi.org/10.2514/3.45937
[research_hablowetz_2000]: https://doi.org/10.2514/6.2000-4299
[research_haddadpour_2006]: https://doi.org/10.2514/1.13591
[research_haddadpour_shams_2005]: https://doi.org/10.2514/6.2005-838
[research_haghighat_liu_2010]: https://doi.org/10.2514/6.2010-9123
[research_haghighat_liu_2012]: https://doi.org/10.2514/1.57013
[research_haghighat_martins_2012]: https://doi.org/10.2514/1.c031344
[research_hahn_haupt_2022]: https://doi.org/10.1007/s13272-022-00586-2
[research_haider_ajaj_2022]: https://doi.org/10.3390/aerospace9090483
[research_haider_ajaj_2023]: https://doi.org/10.3390/aerospace10010057
[research_hajj_2004]: https://doi.org/10.21236/ada428596
[research_halder_benedict_2018]: https://doi.org/10.4050/f-0074-2018-12840
[research_hale_chapman_2012]: https://doi.org/10.1111/j.1747-1567.2011.00801.x
[research_haley_soloway_2001]: https://doi.org/10.2514/2.4696
[research_haley_soloway_2022]: https://doi.org/10.1109/mcs.2022.3171473
[research_hall_mason_2012]: https://doi.org/10.2514/6.2012-2482
[research_halwas_aggarwal_2019]: https://doi.org/10.2514/1.c035481
[research_halwas_aggarwal_2019_b]: https://doi.org/10.2514/1.c035093
[research_ham_kim_1994]: https://doi.org/10.2514/6.1994-1745
[research_hammer_garmann_2023]: https://doi.org/10.2514/6.2023-1979
[research_hammerton_su_2018]: https://doi.org/10.2514/6.2018-2213
[research_han_kim_2011]: https://doi.org/10.1080/0305215x.2010.502937
[research_hanafee_radcliffe_1967]: https://doi.org/10.1063/1.1720698
[research_hancock_1961]: https://doi.org/10.1017/s0001925900002110
[research_hancock_1963]: https://doi.org/10.1017/s0001925900002675
[research_hancock_1965]: https://doi.org/10.2514/6.1965-1120
[research_handojo_lancelot_2018]: https://doi.org/10.2514/6.2018-3573
[research_hanel_1998]: https://doi.org/10.2514/6.1998-4297
[research_haney_johnson_1979]: https://doi.org/10.2514/6.1979-80
[research_haney_waggoner_1978]: https://doi.org/10.2514/6.1978-102
[research_hansen_duan_2020]: https://doi.org/10.2514/6.2020-1186
[research_hansen_duan_2020_b]: https://doi.org/10.2514/6.2020-1186.c1
[research_hansen_duan_2022]: https://doi.org/10.2514/1.g006577
[research_hanson_ryan_2002]: https://doi.org/10.2514/6.2002-3431
[research_harash_yadykin_2012]: https://doi.org/10.3103/s1068799810040083
[research_harkegard]: https://doi.org/10.1109/cdc.2002.1184694
[research_harper_robertp_1955]: https://doi.org/10.21236/ad0092496
[research_harris_arthurs_2016]: https://doi.org/10.1109/icuas.2016.7502624
[research_harry_trobaugh_1966]: https://doi.org/10.21236/ad0641246
[research_hartman_2019]: https://doi.org/10.2514/6.2019-1292
[research_hartmann_2012]: https://doi.org/10.2514/6.2012-459
[research_hartmann_2013]: https://doi.org/10.1002/fld.3762
[research_hartwell_nguyen_2021]: https://doi.org/10.2514/6.2021-1117
[research_harv_testbed]: https://ntrs.nasa.gov/citations/19920024160
[research_harvey_1983]: https://doi.org/10.23919/acc.1983.4788223
[research_hashemi_nguyen_2018]: https://doi.org/10.2514/6.2018-0623
[research_hashemi_nguyen_2018_b]: https://doi.org/10.2514/6.2018-0619
[research_hatamimarbini_2018]: https://doi.org/10.1103/physreve.97.022504
[research_hatamleh_ma_2009]: https://doi.org/10.2514/6.2009-5936
[research_haucke_bauer_2016]: https://doi.org/10.1007/978-3-319-27279-5_19
[research_hayabe_kwak_2025]: https://doi.org/10.2514/6.2025-0257
[research_hayashi_ueda_2017]: https://doi.org/10.1016/j.measurement.2016.10.027
[research_he_deparday_2020]: https://doi.org/10.2514/1.j059719
[research_he_shi_2024]: https://doi.org/10.2514/1.j061902.c1
[research_he_song_2020]: https://doi.org/10.2514/6.2020-1908
[research_he_wang_2021]: https://doi.org/10.2514/6.2021-2534
[research_he_wang_2022]: https://doi.org/10.1145/3548608.3559293
[research_he_wang_2023]: https://doi.org/10.1155/2023/1711088
[research_heaney_quindlen_2024]: https://doi.org/10.2514/6.2024-2509
[research_heeg_2006]: https://doi.org/10.2514/6.2006-2185
[research_heeg_spain_2005]: https://doi.org/10.2514/6.2005-2234
[research_held_fuchs_1999]: https://doi.org/10.1615/tsfp1.2030
[research_helicopter_flight_1987]: https://doi.org/10.1108/eb036427
[research_helmken_emmons_1996]: https://doi.org/10.1063/1.49842
[research_heltsley_cline_1979]: https://doi.org/10.21236/ada068328
[research_heltsley_crosswy_1981]: https://doi.org/10.21236/ada103929
[research_henderson_lavretsky_1999]: https://doi.org/10.2514/6.1999-4080
[research_hendrickson_grossman_1978]: https://doi.org/10.2514/6.1978-1452
[research_henne_1980]: https://doi.org/10.2514/6.1980-330
[research_henne_hicks_1978]: https://doi.org/10.2514/6.1978-105
[research_henry_molinari_2017]: https://doi.org/10.2514/6.2017-0294
[research_herbert]: https://doi.org/10.1007/10339647_21
[research_herencia_weaver_2007]: https://doi.org/10.2514/6.2007-2214
[research_herrmann]: https://doi.org/10.15368/theses.2016.157
[research_herrmann_nematnasser_1966]: https://doi.org/10.2514/6.1966-475
[research_hess_1986]: https://doi.org/10.2514/6.1986-2681
[research_hess_flick_2004]: https://doi.org/10.4271/2004-01-3116
[research_hess_hess_1997]: https://doi.org/10.2514/6.1997-3498
[research_hicks_jenkins_1990]: https://doi.org/10.21236/ada224398
[research_high_load_strain_2018]: https://doi.org/10.12968/s1478-2774(23)50053-3
[research_hildebrand_eidson_2003]: https://doi.org/10.2514/6.2003-3818
[research_hiley_bowers_1981]: https://doi.org/10.2514/6.1981-1441
[research_hilger_ritter_2021]: https://doi.org/10.3390/aerospace8100308
[research_hillebrand_breitenstein_2024]: https://doi.org/10.2514/6.2024-3841
[research_hillebrand_breitenstein_2026]: https://doi.org/10.2514/1.c038610
[research_hillebrand_lutz_2026]: https://doi.org/10.2514/6.2026-4527
[research_hilton_nguyen_2014]: https://doi.org/10.2514/6.2014-0505
[research_himat_deflection]: https://ntrs.nasa.gov/citations/19820030846
[research_hinz_miller_1979]: https://doi.org/10.2514/6.1979-100
[research_history_of_2020]: https://doi.org/10.1002/9781119667063.ch1
[research_hitch_1978]: https://doi.org/10.2514/3.58464
[research_hiti_2017]: https://doi.org/10.21014/acta_imeko.v6i4.396
[research_hjartarson_seiler_2013]: https://doi.org/10.2514/6.2013-4742
[research_hjartarson_seiler_2014]: https://doi.org/10.1109/acc.2014.6859301
[research_hoadley_mcgraw_1995]: https://doi.org/10.2514/3.46680
[research_hodappjr_beckmann_1972]: https://doi.org/10.2514/6.1972-975
[research_hodges_1973]: https://doi.org/10.2514/6.1973-322
[research_hodges_2007]: https://doi.org/10.2514/1.28686
[research_hodges_mckenzie_1975]: https://doi.org/10.2514/6.1975-72
[research_hodson_dobbs_1993]: https://doi.org/10.2514/6.1993-1538
[research_hoffmann_loftfield_2011]: https://doi.org/10.1007/978-3-642-19817-5_25
[research_hofmann_hosseini_2025]: https://doi.org/10.2514/6.2025-2175
[research_hofmann_kezer_1962]: https://doi.org/10.21236/ad0403433
[research_hoh_mitchell_2018]: https://doi.org/10.1201/9781315136820-1
[research_holberg_grabowsky_1981]: https://doi.org/10.2514/6.1981-2492
[research_hollis_brandon_1999]: https://doi.org/10.21236/ada367921
[research_holman_tuozzolo_2009]: https://doi.org/10.1061/41023(337)4
[research_holst_thomas_1982]: https://doi.org/10.2514/6.1982-105
[research_hongchaoli_zhongkeshi]: https://doi.org/10.1109/isscaa.2006.1627440
[research_hope_kunz_2019]: https://doi.org/10.2514/1.j057456
[research_hopkinsej_lovettegh_1977]: https://ntrs.nasa.gov/citations/19770013088
[research_hopwood_ruskin_2019]: https://doi.org/10.2514/6.2019-0608
[research_horn_calise_1998]: https://doi.org/10.2514/6.1998-4459
[research_horton_1943]: https://doi.org/10.1108/eb031070
[research_hoseini_hodges_2019]: https://doi.org/10.2514/1.c035098
[research_hosseini_hofmann_2025]: https://doi.org/10.2514/6.2025-2173
[research_hou_satyanarayana_2000]: https://doi.org/10.2514/6.2000-4824
[research_hoult_beyer_2020]: https://doi.org/10.1061/(asce)st.1943-541x.0002733
[research_how_to_2020]: https://doi.org/10.14359/51728290
[research_howell_1988]: https://doi.org/10.2514/6.1988-2185
[research_hu]: https://doi.org/10.17760/d20449615
[research_hu_1995]: https://doi.org/10.1016/0955-7997(95)00083-6
[research_hu_dai_2025]: https://doi.org/10.1016/j.ast.2025.110174
[research_hu_qu_2009]: https://doi.org/10.2514/6.2009-5713
[research_hu_shao_2023]: https://doi.org/10.1007/978-981-99-0681-9_6
[research_hu_traisnel_2026]: https://doi.org/10.2139/ssrn.6790318
[research_hu_yu_2024]: https://doi.org/10.1109/cac63892.2024.10865419
[research_hua_wang_2025]: https://doi.org/10.3390/aerospace12040327
[research_huang_fraihat_2025]: https://doi.org/10.2514/6.2025-3471
[research_huang_qian_2015]: https://doi.org/10.1016/j.jfluidstructs.2015.03.014
[research_huang_wang_2024]: https://doi.org/10.1007/s00158-024-03809-8
[research_huang_zhang_2024]: https://doi.org/10.1007/978-981-99-8048-2_113
[research_huber_1995]: https://doi.org/10.2514/6.1995-3199
[research_huebner_reimer_2019]: https://doi.org/10.2514/6.2019-3198
[research_huffman_foxjr_1985]: https://doi.org/10.2514/6.1985-276
[research_hughes_wernicke_1974]: https://doi.org/10.21236/ad0783393
[research_hui_auriti_2005]: https://doi.org/10.2514/1.4501
[research_hui_collins_2000]: https://doi.org/10.2514/6.2000-3905
[research_humbad_1978]: https://doi.org/10.2514/3.28011
[research_hunn_1953]: https://doi.org/10.1017/s0368393100131128
[research_huo_wang_2013]: https://doi.org/10.1108/00022661311294030
[research_huo_yuan_2013]: https://doi.org/10.1007/s11771-013-1489-8
[research_hur_valasek_2003]: https://doi.org/10.2514/6.2003-5539
[research_hussain_khan_2019]: https://doi.org/10.1109/ibcast.2019.8667187
[research_hussein_rashid_2025]: https://doi.org/10.1007/s42401-025-00395-5
[research_hutto_1975]: https://doi.org/10.4050/vfs-f31-035
[research_huttsell_eastep_1989]: https://doi.org/10.2514/6.1989-3375
[research_hwang_chen_1991]: https://doi.org/10.2514/6.1991-2423
[research_hwang_pi_1982]: https://doi.org/10.2514/6.1982-724
[research_hwu_tsai_2002]: https://doi.org/10.2514/2.2945
[research_hybrid_approach_1982]: https://doi.org/10.2514/5.9781600865558.0605.0620
[research_iaconis_demilia_1994]: https://doi.org/10.1111/j.1475-1305.1994.tb00917.x
[research_iannacci_mayo_1999]: https://doi.org/10.4050/vfs-f55-00127
[research_iannuzzo_russo_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00020-4
[research_ibrahim_castravete_2005]: https://doi.org/10.1115/detc2005-84737
[research_ibren_sulaeman_2020]: https://doi.org/10.37934/cfdl.12.4.7989
[research_idan_karpel_1999]: https://doi.org/10.2514/2.4427
[research_ide_ishida_2019]: https://doi.org/10.2514/6.2019-1847
[research_ide_ominsky_1990]: https://doi.org/10.2514/6.1990-1075
[research_ide_shankar_1987]: https://doi.org/10.2514/6.1987-707
[research_idsardi_1983]: https://doi.org/10.2514/6.1983-2732
[research_ifju_waszak_2001]: https://doi.org/10.2514/6.2001-4005
[research_ilie_havenar_2023]: https://doi.org/10.2514/6.2023-4089
[research_iliff_maine_1983]: https://doi.org/10.2514/3.48210
[research_incorporating_agility_1994]: https://doi.org/10.2514/6.1994-2135
[research_ingle_kothmann_1998]: https://doi.org/10.4050/vfs-f54-00100
[research_initial_flight_1989]: https://doi.org/10.2514/6.1989-3359
[research_innocenti_1985]: https://doi.org/10.2514/6.1985-1805
[research_international_standard_2010]: https://doi.org/10.1017/cbo9780511844652.021
[research_introduction_to_2003]: https://doi.org/10.2514/5.9781600861840.0199.0208
[research_introduction_to_2018]: https://doi.org/10.2514/5.9781624105135.0321.0346
[research_investigations_of_static_2016]: https://doi.org/10.12677/jast.2016.43009
[research_ionelaralucamaxim_1970]: https://doi.org/10.33422/jarss.v2i3.222
[research_ippolito_ting_2014]: https://doi.org/10.2514/6.2014-1044
[research_irfan_nanangburhan_2026]: https://doi.org/10.35261/barometer.v11i2.13201
[research_iriarte_aginaga_2021]: https://doi.org/10.1016/j.measurement.2020.108938
[research_ishihara_nguyen_2013]: https://doi.org/10.2514/6.2013-4860
[research_ishihara_nguyen_2014]: https://doi.org/10.1109/cdc.2014.7039759
[research_ishii_1965]: https://doi.org/10.2514/6.1965-772
[research_ishii_gomi_2005]: https://doi.org/10.2514/6.2005-6119
[research_islam_martin_2018]: https://doi.org/10.2514/6.2018-2834
[research_islam_rahman_2025]: https://doi.org/10.31224/4605
[research_islam_rahman_2025_b]: https://doi.org/10.1115/imece2025-166937
[research_islam_rahman_2026]: https://doi.org/10.21203/rs.3.rs-9116370/v1
[research_isnardi_paoletti_2018]: https://doi.org/10.2514/6.2018-0603
[research_isogai_1988]: https://doi.org/10.6089/jscm.14.96
[research_isogai_1989]: https://doi.org/10.2514/3.45883
[research_israq_ahmaad_2025]: https://doi.org/10.2514/6.2025-106584
[research_iyer_park_2017]: https://doi.org/10.2514/6.2017-3953
[research_izadi_pakmehr_2007]: https://doi.org/10.1109/aero.2007.352761
[research_izadpanahi]: https://doi.org/10.25148/etd.fidc008911
[research_ize_arena_1998]: https://doi.org/10.2514/2.2394
[research_ize_arenajr_1997]: https://doi.org/10.2514/6.1997-3486
[research_ize_arenajr_1999]: https://doi.org/10.2514/6.1999-990
[research_j_j_2015]: https://doi.org/10.14445/23488360/ijme-v2i6p103
[research_jabbar_setiawan_2026]: https://doi.org/10.35261/barometer.v11i2.13206
[research_jackson_livne_2005]: https://doi.org/10.2514/6.2005-2170
[research_jackson_livne_2014]: https://doi.org/10.2514/1.j050941
[research_jacobspf_1983]: https://ntrs.nasa.gov/citations/19850007386
[research_jafari_feizarefi_2019]: https://doi.org/10.3390/aerospace6100115
[research_jain_2014]: https://doi.org/10.4271/2014-01-0355
[research_jain_singla_2025]: https://doi.org/10.2514/6.2025-0464
[research_jameson_1973]: https://doi.org/10.2514/6.1973-3002
[research_jameson_1977]: https://doi.org/10.2172/7093932
[research_jameson_1982]: https://doi.org/10.1016/b978-0-12-493280-7.50008-5
[research_jameson_2003]: https://doi.org/10.1007/978-94-010-0017-8_39
[research_jameson_caughey_1977]: https://doi.org/10.2172/7308750
[research_jamshidi_dardel_2016]: https://doi.org/10.24200/sci.2016.3845
[research_janardhan_grandhi_2003]: https://doi.org/10.21236/ada417106
[research_jategaonkar_fischenberg_2004]: https://doi.org/10.2514/1.3165
[research_jaworski_2012]: https://doi.org/10.2514/1.j051579
[research_jebakumar_kumar_2019]: https://doi.org/10.1109/icc47138.2019.9123231
[research_jenkins_kuhl_1977]: https://doi.org/10.2514/3.58914
[research_jenkinsjeraldm_kuhlalberte_1977]: https://ntrs.nasa.gov/citations/20020086520
[research_jenney_schreadley_1982]: https://doi.org/10.21236/ada117244
[research_jeong_lee_2013]: https://doi.org/10.2514/1.c032087
[research_jepps_1981]: https://doi.org/10.1007/978-3-663-14008-5_9
[research_jha_chattopadhyay_1999]: https://doi.org/10.2514/6.1999-1514
[research_jia_zhang_2022]: https://doi.org/10.3390/aerospace9110699
[research_jia_zhang_2023]: https://doi.org/10.3390/aerospace10100853
[research_jian_jinwu_2009]: https://doi.org/10.1016/s1000-9361(08)60111-9
[research_jiang_1999]: https://doi.org/10.4271/1999-01-5618
[research_jiang_an_2000]: https://doi.org/10.2514/6.2000-4324
[research_jiang_li_2018]: https://doi.org/10.2514/6.2018-3160
[research_jiang_li_2018_b]: https://doi.org/10.2514/6.2018-3160.c1
[research_jiang_tian_2019]: https://doi.org/10.1016/j.ast.2019.03.043
[research_jiang_yang_2026]: https://doi.org/10.1007/978-981-95-7840-5_15
[research_jianjunma_pengli_2008]: https://doi.org/10.1109/asc-icsc.2008.4675349
[research_jianjunma_wenqiangli_2008]: https://doi.org/10.1109/asc-icsc.2008.4675328
[research_jin_song_2013]: https://doi.org/10.4028/www.scientific.net/amm.401-403.571
[research_jing_ma_2025]: https://doi.org/10.1108/aeat-01-2024-0025
[research_jing_zhang_2017]: https://doi.org/10.1109/cyber.2017.8446465
[research_jingping_weiguo_2011]: https://doi.org/10.1016/j.proeng.2011.08.232
[research_jiniraj_bruceralphinrose_2023]: https://doi.org/10.1007/s42235-022-00326-6
[research_jo_majid_2023]: https://doi.org/10.3390/biomimetics8010034
[research_jodin_scheller_2017]: https://doi.org/10.4028/www.scientific.net/ssp.260.85
[research_johnfquindlen_danielmortega]: https://ntrs.nasa.gov/citations/20250011280
[research_johns_1964]: https://doi.org/10.2514/3.2691
[research_johnson_1980]: https://doi.org/10.2514/6.1980-765
[research_johnsoncb_kaufmanlgiii_1979]: https://ntrs.nasa.gov/citations/19790035549
[research_johnston_1998]: https://doi.org/10.2514/6.1998-2736
[research_johnston_cassarino_1976]: https://doi.org/10.21236/ada020871
[research_johnstonjf_1979]: https://ntrs.nasa.gov/citations/19820007203
[research_jones_1950]: https://doi.org/10.2514/8.1517
[research_jones_1976]: https://doi.org/10.2514/3.44558
[research_jones_1980]: https://doi.org/10.2514/6.1980-3040
[research_jones_jarrett_2018]: https://doi.org/10.2514/1.j056725
[research_joo_marks_2015]: https://doi.org/10.2514/6.2015-1050
[research_jorge_lind_2013]: https://doi.org/10.2514/6.2013-4983
[research_jovanov_debreuker_2015]: https://doi.org/10.2514/6.2015-0175
[research_juliana_chu_2004]: https://doi.org/10.2514/6.2004-5170
[research_jun_harmin_2014]: https://doi.org/10.4028/www.scientific.net/amm.629.182
[research_jurisson_debreuker_2022]: https://doi.org/10.2514/6.2022-2169
[research_juttechristine_stanfordbretk_2014]: https://ntrs.nasa.gov/citations/20140006404
[research_kadrnka_hawley_1993]: https://doi.org/10.2514/6.1993-3929
[research_kady_takahashi_2014]: https://doi.org/10.2514/6.2014-0024
[research_kafkas_kilimtzidis_2021]: https://doi.org/10.3390/aerospace8120398
[research_kafkas_lampeas_2020]: https://doi.org/10.3390/aerospace7110164
[research_kai_sugiura_2020]: https://doi.org/10.2514/6.2020-1757
[research_kalaji_2023]: https://doi.org/10.32920/ryerson.14653803
[research_kaletka_fu_1993]: https://doi.org/10.2514/6.1993-3635
[research_kandil_kalisch_1994]: https://doi.org/10.2514/6.1994-1887
[research_kandil_kandil_1993]: https://doi.org/10.2514/6.1993-2973
[research_kandil_menzies_1996]: https://doi.org/10.2514/6.1996-828
[research_kang_meng_2023]: https://doi.org/10.3390/atmos14101577
[research_kang_zhao_2023]: https://doi.org/10.3390/atmos14121784
[research_kannemans_1995]: https://doi.org/10.2514/6.1995-3434
[research_kapania_chun_2003]: https://doi.org/10.2514/6.2003-2004
[research_kapase_joshi_2026]: https://doi.org/10.22214/ijraset.2026.79150
[research_karania_mohan_2021]: https://doi.org/10.1007/978-981-15-9601-8_38
[research_karathanasopoulos_2015]: https://doi.org/10.1016/j.istruc.2015.05.004
[research_karpel_1982]: https://doi.org/10.2514/3.57379
[research_karpel_1989]: https://doi.org/10.2514/6.1989-3467
[research_karpel_1990]: https://doi.org/10.2514/3.20514
[research_karpel_1990_b]: https://doi.org/10.2514/3.25297
[research_karpel_idan_1998]: https://doi.org/10.2514/6.1998-1864
[research_karpel_moulin_2000]: https://doi.org/10.2514/6.2000-4722
[research_karpel_sheena_1989]: https://doi.org/10.2514/3.45791
[research_karpouzian_1991]: https://doi.org/10.2514/3.10655
[research_karpouzian_librescu_1991]: https://doi.org/10.2514/6.1991-934
[research_karpouzian_librescu_1992]: https://doi.org/10.2514/6.1992-2469
[research_karpouzian_librescu_1994]: https://doi.org/10.2514/3.46551
[research_kassapakis_warwick_1994]: https://doi.org/10.1002/acs.4480080405
[research_katagiri_park_2024]: https://doi.org/10.2514/6.2024-0850
[research_katam_lebeau_2005]: https://doi.org/10.2514/6.2005-4880
[research_kaufman_balabanov_1996]: https://doi.org/10.2514/6.1996-89
[research_kaushik_2018]: https://doi.org/10.1007/978-981-13-1678-4_1
[research_kawakami_takatoya_2007]: https://doi.org/10.2514/6.2007-4174
[research_kawakami_takatoya_2008]: https://doi.org/10.2514/6.2008-6419
[research_kaygan_ulusoy_2018]: https://doi.org/10.30518/jav.482507
[research_kayran_2004]: https://doi.org/10.1115/esda2004-58468
[research_kayran_2007]: https://doi.org/10.1108/00022660710732707
[research_kaza_kielb_1982]: https://doi.org/10.2514/6.1982-726
[research_kbadri_torabpour_2025]: https://doi.org/10.2139/ssrn.5248546
[research_kbadri_torabpour_2026]: https://doi.org/10.1016/j.engstruct.2025.121912
[research_ke_zhigang_2008]: https://doi.org/10.1016/s1000-9361(08)60052-7
[research_keas_macmynowski_2009]: https://doi.org/10.2514/6.2009-5709
[research_kececioglu_salihyigit_2026]: https://doi.org/10.1109/rast69551.2026.11672518
[research_keener_1984]: https://doi.org/10.2514/6.1984-2092
[research_kefayat_kamali_2024]: https://doi.org/10.1109/iccia65044.2024.10768167
[research_kehoe_1988]: https://doi.org/10.2514/6.1988-2075
[research_kehrer_1971]: https://doi.org/10.2514/6.1971-785
[research_keidel_lienhard_2020]: https://doi.org/10.1115/smasis2020-2254
[research_keidel_molinari_2019]: https://doi.org/10.1177/1045389x19828501
[research_kelly_1974]: https://doi.org/10.2514/6.1974-909
[research_kelly_1988]: https://doi.org/10.2514/6.1988-2129
[research_kennedy_martins_2013]: https://doi.org/10.2514/6.2013-1530
[research_khaddage]: https://doi.org/10.22215/etd/2017-12070
[research_khalil_asaro_2020]: https://doi.org/10.2514/6.2020-2940
[research_khalil_asaro_2022]: https://doi.org/10.2514/1.c036426
[research_khalil_bauknecht_2024]: https://doi.org/10.2514/1.c037503
[research_khalil_fezans_2019]: https://doi.org/10.2514/6.2019-0822
[research_khalil_fezans_2019_b]: https://doi.org/10.2514/6.2019-0822.c1
[research_khalil_fezans_2020]: https://doi.org/10.1017/aer.2020.85
[research_kheiri_riazat_2025]: https://doi.org/10.1017/aer.2025.10028
[research_kholodar_2014]: https://doi.org/10.2514/1.c032295
[research_kholodar_2016]: https://doi.org/10.2514/1.c033772
[research_khot_1999]: https://doi.org/10.1117/12.350112
[research_khot_appa_1998]: https://doi.org/10.2514/6.1998-4886
[research_khot_appa_1998_b]: https://doi.org/10.2514/6.1998-1802
[research_khot_appa_2000]: https://doi.org/10.2514/2.2687
[research_khot_eastep_1997]: https://doi.org/10.2514/6.1997-1268
[research_khot_zweber_2000]: https://doi.org/10.2514/6.2000-1333
[research_khot_zweber_2002]: https://doi.org/10.2514/2.2971
[research_khrabrov_sidoryuk_2010]: https://doi.org/10.2514/6.2010-284
[research_khrabrov_sidoryuk_2013]: https://doi.org/10.14355/fae.2013.0204.06
[research_kilimtzidis_kostopoulos_2023]: https://doi.org/10.3390/aerospace10030251
[research_kim_2004]: https://doi.org/10.21236/ada423149
[research_kim_ahn_2013]: https://doi.org/10.2514/6.2013-5169
[research_kim_crassidis_2003]: https://doi.org/10.2514/6.2003-5506
[research_kim_jeon_2006]: https://doi.org/10.2514/1.13864
[research_kim_kim_2007]: https://doi.org/10.4028/0-87849-427-8.481
[research_kim_obayashi_2001]: https://doi.org/10.2514/2.2823
[research_kim_song_2013]: https://doi.org/10.2514/1.c031212
[research_kim_sung_1993]: https://doi.org/10.2514/6.1993-3474
[research_kim_sung_2023]: https://doi.org/10.1109/lra.2023.3243439
[research_kim_winchenbach_1986]: https://doi.org/10.2514/3.20100
[research_kimaru_bouferrouk_2017]: https://doi.org/10.1109/icmae.2017.8038751
[research_kimler_canfield_2006]: https://doi.org/10.2514/6.2006-7134
[research_king_1944]: https://doi.org/10.1108/eb031093
[research_kirsch_montagnier_2020]: https://doi.org/10.1016/j.jfluidstructs.2020.102930
[research_kishi_kanazaki_2016]: https://doi.org/10.4236/jfcmv.2016.41004
[research_kisslinger_vetsch_1965]: https://doi.org/10.2514/6.1965-1245
[research_klabes_callsen_2018]: https://doi.org/10.1007/978-3-319-76780-2_19
[research_klaue_seidel_2009]: https://doi.org/10.1103/physrevlett.102.028302
[research_klausmeyer_2018]: https://doi.org/10.2514/6.2018-2992
[research_klepl_1990]: https://doi.org/10.23919/acc.1990.4790836
[research_klepl_1995]: https://doi.org/10.2514/3.46702
[research_klim_zeppetelli_2013]: https://doi.org/10.4271/2013-01-2232
[research_klimek_2024]: https://doi.org/10.15199/48.2024.03.24
[research_klopfer_nielsen_1980]: https://doi.org/10.2514/6.1980-126
[research_klug_radespiel_2020]: https://doi.org/10.2514/6.2020-0271
[research_klug_ullah_2023]: https://doi.org/10.1007/s13272-023-00645-2
[research_klyde_bachelder_2007]: https://doi.org/10.2514/6.2007-6385
[research_knighton_1992]: https://doi.org/10.2514/6.1992-4072
[research_ko_mason_2003]: https://doi.org/10.2514/6.2003-4062
[research_kobow_wennemann_2026]: https://doi.org/10.2514/6.2026-0302
[research_kobusch_eichstadt_2017]: https://doi.org/10.21014/acta_imeko.v6i1.433
[research_koeniguer_spear_2018]: https://doi.org/10.2514/6.2018-4169
[research_kojima_kameda_2019]: https://doi.org/10.1007/978-3-319-91017-8_134
[research_kokolios_1994]: https://doi.org/10.2514/6.1994-10
[research_kolesar_1971]: https://doi.org/10.21236/ad0734236
[research_kolesar_kassianides_1970]: https://doi.org/10.21236/ad0734233
[research_kolesar_kassianides_1970_b]: https://doi.org/10.21236/ad0734235
[research_kolonay_yang_1998]: https://doi.org/10.2514/2.2260
[research_koo_2001]: https://doi.org/10.2514/2.2767
[research_koo_lee_1994]: https://doi.org/10.1016/0045-7949(94)90293-3
[research_koohi_shahverdi_2014]: https://doi.org/10.1016/j.compstruct.2014.03.012
[research_kopf_bullinger_2018]: https://doi.org/10.23919/acc.2018.8430956
[research_kopf_giesseler_2015]: https://doi.org/10.1109/acc.2015.7171080
[research_kopsaftopoulos_nardari_2015]: https://doi.org/10.12783/shm2015/163
[research_kordt_ballauf_2002]: https://doi.org/10.1524/auto.2002.50.9.451
[research_koreanschi_oliviu_2014]: https://doi.org/10.2514/6.2014-3170
[research_koreanschi_oliviu_2015]: https://doi.org/10.2514/6.2015-3386
[research_koreanschi_oliviu_2016]: https://doi.org/10.2514/6.2016-1083
[research_kosmatka_panza_2002]: https://doi.org/10.2514/6.2002-3470
[research_kotikalpudi_danowsky_2018]: https://doi.org/10.2514/6.2018-3426
[research_kotikalpudi_pfifer_2016]: https://doi.org/10.2514/6.2016-1752
[research_kovenwilliam_kaytengeraldg_1946]: https://ntrs.nasa.gov/citations/19930092590
[research_kowalska_goetzendorfgrabowski_2022]: https://doi.org/10.1108/aeat-01-2022-0001
[research_krasuski_bakua_2021]: https://doi.org/10.20858/sjsutst.2021.111.6
[research_kratochvil_valenta_2024]: https://doi.org/10.1007/s13272-024-00745-7
[research_krengel_2024]: https://doi.org/10.23967/eccomas.2024.094
[research_krengel_hepperle_2022]: https://doi.org/10.2514/6.2022-0126
[research_krengel_hepperle_2023]: https://doi.org/10.2514/6.2023-3369
[research_krenz_1979]: https://doi.org/10.2514/6.1979-692
[research_kreshock_kang_2016]: https://doi.org/10.4050/f-0072-2016-11432
[research_kreshock_yeo_2018]: https://doi.org/10.4050/f-0074-2018-12761
[research_krings_henning_2013]: https://doi.org/10.1007/978-3-642-38253-6_17
[research_kroegerra_1977]: https://ntrs.nasa.gov/citations/19780012166
[research_kruger_meddaikar_2022]: https://doi.org/10.3390/aerospace9100535
[research_kubica_livet_1994]: https://doi.org/10.2514/6.1994-3630
[research_kubica_livet_1994_b]: https://doi.org/10.1109/cca.1994.381445
[research_kubica_livet_1995]: https://doi.org/10.1016/b978-0-08-042238-1.50010-0
[research_kuder_arrieta_2014]: https://doi.org/10.1115/smasis2014-7493
[research_kuhlman_cerney_1988]: https://doi.org/10.2514/6.1988-7
[research_kukreja_2009]: https://doi.org/10.1080/00207170903032847
[research_kukreja_brenner]: https://doi.org/10.1007/978-1-84628-899-9_5
[research_kukrejasunill_2007]: https://ntrs.nasa.gov/citations/20070028827
[research_kulfan_vachal_1978]: https://doi.org/10.21236/ada056124
[research_kulhanek_2019]: https://doi.org/10.1108/aeat-06-2018-0162
[research_kumar_ganguli_2008]: https://doi.org/10.2514/1.32024
[research_kumar_ghosh_2017]: https://doi.org/10.2514/6.2017-0936
[research_kumar_ghosh_2023]: https://doi.org/10.1108/aeat-09-2019-0179
[research_kumar_sunil_2021]: https://doi.org/10.1007/978-981-15-9601-8_13
[research_kuo_hsu_1997]: https://doi.org/10.2514/2.2222
[research_kuppuswamy_kiran_1981]: https://doi.org/10.2514/6.1981-2381
[research_kurade_venkatakrishnan_2021]: https://doi.org/10.1017/aer.2021.99
[research_kurita_koike_2019]: https://doi.org/10.2322/tjsass.62.108
[research_kurzke_halliwell_2018]: https://doi.org/10.1007/978-3-319-75979-1_14
[research_kurzke_halliwell_2025]: https://doi.org/10.1007/978-3-031-65026-0_20
[research_kussner_1959]: https://doi.org/10.1016/b978-1-4831-9833-0.50009-8
[research_kutluay_mahmutyazicioglu_2009]: https://doi.org/10.2514/6.2009-5724
[research_kuttenkeuler_ringertz_1998]: https://doi.org/10.2514/2.2330
[research_kwak_shirotake_2004]: https://doi.org/10.2514/6.2004-5082
[research_kwon_chang_2026]: https://doi.org/10.1201/9781003761891-33
[research_kwong_severson_2024]: https://doi.org/10.2514/6.2024-84746
[research_laban_masui_1993]: https://doi.org/10.2514/3.46327
[research_lai_lu_2016]: https://doi.org/10.2514/6.2016-3835
[research_lai_zhang_2014]: https://doi.org/10.2514/6.2014-1200
[research_lam_paranjape_2024]: https://doi.org/10.2514/6.2024-2820
[research_lambert_gursul_2001]: https://doi.org/10.2514/6.2001-2426
[research_lamour_2014]: https://doi.org/10.5162/etc2014/4.2
[research_lamy_1983]: https://doi.org/10.2514/6.1983-2736
[research_lan_bianchi_2006]: https://doi.org/10.2514/6.2006-6490
[research_landers_landrum_1997]: https://doi.org/10.2514/6.1997-2248
[research_landers_landrum_1998]: https://doi.org/10.2514/2.3355
[research_lang_1981]: https://doi.org/10.2514/6.1981-2416
[research_lanjunli_shouyiyu_2006]: https://doi.org/10.1109/wcica.2006.1714300
[research_large_may_1981]: https://doi.org/10.2514/6.1981-2395
[research_larson_1958]: https://doi.org/10.2172/12393299
[research_larson_1986]: https://doi.org/10.2514/6.1986-2237
[research_larsson_2019]: https://doi.org/10.3384/diss.diva-156694
[research_lateral_control_flexible]: https://ntrs.nasa.gov/citations/19930092079
[research_lateral_control_large_flaps]: https://ntrs.nasa.gov/citations/19930084594
[research_lateral_directional_stability_2003]: https://doi.org/10.2514/5.9781600861840.0297.0310
[research_lauchle_1974]: https://doi.org/10.2514/3.62987
[research_laughrey_1969]: https://doi.org/10.2514/6.1969-428
[research_laurie_farokhi_1993]: https://doi.org/10.2514/6.1993-3422
[research_layton_1986]: https://doi.org/10.2514/6.1986-9787
[research_layton_1995]: https://doi.org/10.2514/6.1995-1192
[research_layton_1996]: https://doi.org/10.2514/6.1996-1442
[research_lazarus_crawley_1991]: https://doi.org/10.2514/6.1991-985
[research_lazarus_crawley_1995]: https://doi.org/10.2514/3.56650
[research_leal_petterson_2017]: https://doi.org/10.2514/6.2017-0054
[research_leal_stroud_2018]: https://doi.org/10.2514/6.2018-0799
[research_leal_white_2018]: https://doi.org/10.2514/6.2018-0800
[research_leble_barakos_2016]: https://doi.org/10.1007/978-3-319-39095-6_7
[research_lebofsky_ting_2015]: https://doi.org/10.2514/6.2015-1408
[research_lebofsky_ting_2015_b]: https://doi.org/10.2514/6.2015-2723
[research_lee_1994]: https://doi.org/10.2514/6.1994-1695
[research_lee_aldredge_2015]: https://doi.org/10.1016/j.ast.2015.08.004
[research_lee_boedicker_1985]: https://doi.org/10.2514/6.1985-3073
[research_lee_hashemi_2018]: https://doi.org/10.23919/acc.2018.8431916
[research_lee_kim_1994]: https://doi.org/10.2514/3.46667
[research_lee_kim_1995]: https://doi.org/10.2514/3.46803
[research_lee_singh_2006]: https://doi.org/10.2514/6.2006-6315
[research_lee_singh_2009]: https://doi.org/10.2514/6.2009-6301
[research_lee_singh_2014]: https://doi.org/10.2514/6.2014-0603
[research_lee_singh_2018]: https://doi.org/10.2514/6.2018-1341
[research_lee_valerio_1993]: https://doi.org/10.2514/6.1993-3468
[research_leerausch_batina_1993]: https://doi.org/10.2514/6.1993-3476
[research_lei_kwak_2005]: https://doi.org/10.2514/6.2005-5087
[research_lei_wang_2020]: https://doi.org/10.21595/jve.2019.20968
[research_leijonhufvud_karlsson_2011]: https://doi.org/10.2514/1.c031170
[research_leitch_stodieck_2024]: https://doi.org/10.2139/ssrn.4786120
[research_leitch_stodieck_2025]: https://doi.org/10.1016/j.compstruct.2025.119706
[research_lekou_mouzakis_2009]: https://doi.org/10.1115/1.3027508
[research_lesoinne_2007]: https://doi.org/10.21236/ada481320
[research_lesoinne_balas_2001]: https://doi.org/10.2514/6.2001-4031
[research_lesoinne_farhat_1993]: https://doi.org/10.2514/6.1993-3325
[research_lesoinne_farhat_1995]: https://doi.org/10.2514/6.1995-1709
[research_lesoinne_kaila_2005]: https://doi.org/10.2514/6.2005-1089
[research_levchenko_1987]: https://doi.org/10.1007/bf00865899
[research_level_flight_2003]: https://doi.org/10.2514/5.9781600861840.0083.0096
[research_leventhal_keel_1977]: https://doi.org/10.2514/6.1977-1068
[research_levinski_2004]: https://doi.org/10.21914/anziamj.v45i0.936
[research_levinsky_palko_1978]: https://doi.org/10.2514/6.1978-786
[research_levy_1992]: https://doi.org/10.2514/6.1992-4193
[research_lewis_platt_1979]: https://doi.org/10.2514/3.58552
[research_lhachemi_chu_2017]: https://doi.org/10.2514/1.g002497
[research_lhachemi_saussie_2017]: https://doi.org/10.2514/6.2017-1735
[research_li_2018]: https://doi.org/10.3901/jme.2018.05.142
[research_li_ang_2016]: https://doi.org/10.21595/jve.2016.16705
[research_li_dai_2024]: https://doi.org/10.2514/1.j063907
[research_li_dai_2025]: https://doi.org/10.1063/5.0295770
[research_li_dong_2009]: https://doi.org/10.1109/cdc.2009.5399970
[research_li_fleeter_1996]: https://doi.org/10.2514/6.1996-3177
[research_li_ge_2022]: https://doi.org/10.1016/j.cja.2021.04.030
[research_li_geiselhart_2026]: https://doi.org/10.2514/1.c038747
[research_li_gong_2025]: https://doi.org/10.3390/app15168882
[research_li_guo_2010]: https://doi.org/10.1016/j.jsv.2010.06.006
[research_li_guo_2010_b]: https://doi.org/10.2514/6.2010-2951
[research_li_huang_2018]: https://doi.org/10.1177/1077546318810033
[research_li_kou_2024]: https://doi.org/10.1016/j.jfluidstructs.2023.104055
[research_li_li_2016]: https://doi.org/10.1177/1729881416664846
[research_li_li_2025]: https://doi.org/10.21203/rs.3.rs-7650803/v1
[research_li_livne_1995]: https://doi.org/10.2514/6.1995-1219
[research_li_livne_1997]: https://doi.org/10.2514/2.2179
[research_li_luo_2023]: https://doi.org/10.21203/rs.3.rs-2932289/v1
[research_li_qian_2024]: https://doi.org/10.3390/aerospace11121015
[research_li_qin_2020]: https://doi.org/10.1016/j.ast.2019.105622
[research_li_qin_2020_b]: https://doi.org/10.2514/1.c035696
[research_li_qin_2021]: https://doi.org/10.1016/j.jfluidstructs.2021.103407
[research_li_qin_2021_b]: https://doi.org/10.1016/j.ast.2021.106919
[research_li_qin_2022]: https://doi.org/10.3390/app122010537
[research_li_wan_2021]: https://doi.org/10.3390/app112411800
[research_li_wang_2021]: https://doi.org/10.1155/2021/3949078
[research_li_wang_2025]: https://doi.org/10.23919/ccc64809.2025.11179130
[research_li_xia_2017]: https://doi.org/10.1016/j.cja.2017.09.007
[research_li_xia_2018]: https://doi.org/10.1017/aer.2018.93
[research_li_xiong_2025]: https://doi.org/10.1088/1742-6596/3044/1/012002
[research_li_yang_2020]: https://doi.org/10.1177/1077546320949122
[research_li_yu_2011]: https://doi.org/10.4028/www.scientific.net/amm.138-139.404
[research_li_yu_2012]: https://doi.org/10.1166/asl.2012.2975
[research_li_zhang_2014]: https://doi.org/10.4028/www.scientific.net/amm.608-609.708
[research_li_zhang_2019]: https://doi.org/10.2514/6.2019-1214
[research_li_zhang_2024]: https://doi.org/10.2139/ssrn.4923624
[research_li_zhang_2026]: https://doi.org/10.1088/1361-6501/ae3b62
[research_li_zhao_2017]: https://doi.org/10.2514/1.g002178
[research_li_zheng_2025]: https://doi.org/10.1115/1.4069068
[research_li_zhiqiang_2024]: https://doi.org/10.2139/ssrn.4720148
[research_li_zhu_1999]: https://doi.org/10.1007/bf01179541
[research_liang_chen_2025]: https://doi.org/10.2139/ssrn.5198189
[research_liang_chen_2026]: https://doi.org/10.1016/j.measurement.2025.119491
[research_liang_qin_2012]: https://doi.org/10.4028/www.scientific.net/amr.466-467.282
[research_liao_zhang_2026]: https://doi.org/10.3390/aerospace13080725
[research_librescu_beiner_1983]: https://doi.org/10.1002/oca.4660040209
[research_librescu_na_2003]: https://doi.org/10.2514/6.2003-1414
[research_librescu_simovich_1988]: https://doi.org/10.2514/3.45572
[research_librescu_song_1992]: https://doi.org/10.1016/0961-9526(92)90039-9
[research_librescu_thangjitham_1989]: https://doi.org/10.4271/891056
[research_librescu_thangjitham_1991]: https://doi.org/10.2514/3.46004
[research_lichtenwalner_little_1996]: https://doi.org/10.1115/imece1996-0947
[research_lieberman_1963]: https://doi.org/10.2514/6.1963-1813
[research_liebst_1987]: https://doi.org/10.2514/3.20238
[research_liebst_garrard_1986]: https://doi.org/10.2514/6.1986-2247
[research_liebst_garrard_1986_b]: https://doi.org/10.2514/3.20068
[research_liebst_garrard_1988]: https://doi.org/10.2514/3.20297
[research_lim_sreenatha_2000]: https://doi.org/10.2514/6.2000-3904
[research_limitations_and_2017]: https://doi.org/10.1002/9781118534786.ch20
[research_lin_1982]: https://doi.org/10.2514/6.1982-1326
[research_lin_1983]: https://doi.org/10.2514/6.1983-2102
[research_lin_2016]: https://doi.org/10.2514/1.c033701
[research_lin_crawley_1994]: https://doi.org/10.2514/6.1994-1547
[research_lin_crawley_1995]: https://doi.org/10.2514/6.1995-1386
[research_lin_crawley_1996]: https://doi.org/10.2514/3.47045
[research_lin_zhang_2019]: https://doi.org/10.23919/chicc.2019.8865352
[research_lind_1999]: https://doi.org/10.2514/6.1999-4205
[research_lind_brenner_1997]: https://doi.org/10.2514/6.1997-3714
[research_lind_brenner_1997_b]: https://doi.org/10.2514/2.4082
[research_lind_brenner_1998]: https://doi.org/10.2514/2.2320
[research_lind_brenner_1999]: https://doi.org/10.1007/978-1-4471-0849-8_7
[research_lind_brenner_1999_b]: https://doi.org/10.1007/978-1-4471-0849-8_13
[research_lind_brenner_1999_c]: https://doi.org/10.1007/978-1-4471-0849-8_5
[research_lind_brenner_1999_d]: https://doi.org/10.1007/978-1-4471-0849-8_12
[research_lind_brenner_1999_e]: https://doi.org/10.1007/978-1-4471-0849-8
[research_lind_brenner_1999_f]: https://doi.org/10.1007/978-1-4471-0849-8_4
[research_lind_freudinger_1998]: https://doi.org/10.2514/2.7585
[research_lindsley_2007]: https://doi.org/10.2514/6.2007-1336
[research_lindsley_2009]: https://doi.org/10.2514/6.2009-5710
[research_lingyu_youwu_2006]: https://doi.org/10.1109/chicc.2006.4347425
[research_little_1996]: https://doi.org/10.4050/vfs-f52-2050
[research_liu_2019]: https://doi.org/10.1177/0020294019858106
[research_liu_2022]: https://doi.org/10.1007/978-981-19-4586-1_12
[research_liu_2022_b]: https://doi.org/10.1007/978-981-19-4586-1_13
[research_liu_bai_2013]: https://doi.org/10.4028/www.scientific.net/amm.302.377
[research_liu_dong_2018]: https://doi.org/10.1109/icca.2018.8444282
[research_liu_fan_2025]: https://doi.org/10.3390/app15137596
[research_liu_gao_2020]: https://doi.org/10.1016/j.jfluidstructs.2020.103098
[research_liu_gong_2021]: https://doi.org/10.1177/0020294020983377
[research_liu_he_2025]: https://doi.org/10.1007/978-981-96-1467-7_35
[research_liu_lei_2023]: https://doi.org/10.3390/aerospace10070646
[research_liu_li_2025]: https://doi.org/10.3390/fluids10060152
[research_liu_li_2026]: https://doi.org/10.3390/electronics15163532
[research_liu_pang_2023]: https://doi.org/10.1016/j.measurement.2023.113165
[research_liu_qian_2026]: https://doi.org/10.1016/j.ast.2026.112709
[research_liu_sun_2009]: https://doi.org/10.1109/ccdc.2009.5192368
[research_liu_sun_2016]: https://doi.org/10.1155/2016/1060574
[research_liu_sun_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000712
[research_liu_sun_2017_b]: https://doi.org/10.1016/j.ast.2017.10.006
[research_liu_wang_2023]: https://doi.org/10.3390/s23218846
[research_liu_yang_2024]: https://doi.org/10.20944/preprints202410.1024.v1
[research_liu_yin_2011]: https://doi.org/10.1117/12.880323
[research_liu_zhang_2018]: https://doi.org/10.1109/gncc42960.2018.9019008
[research_liu_zhang_2020]: https://doi.org/10.23919/ccc50068.2020.9188689
[research_liu_zhang_2023]: https://doi.org/10.1002/aisy.202300420
[research_liu_zhou_2015]: https://doi.org/10.2991/itms-15.2015.114
[research_liu_zhu_2013]: https://doi.org/10.1016/j.cja.2013.04.015
[research_livet_kubica_1994]: https://doi.org/10.1016/s1474-6670(17)45836-8
[research_livet_kubica_1995]: https://doi.org/10.1016/b978-0-08-042238-1.50070-7
[research_livne_1993]: https://doi.org/10.2514/3.49052
[research_livne_2001]: https://doi.org/10.2514/6.2001-1370
[research_livne_2010]: https://doi.org/10.1002/9780470686652.eae148
[research_livne_li_1994]: https://doi.org/10.1115/imece1994-1443
[research_lizotteandrew_allenmichaelj_2005]: https://ntrs.nasa.gov/citations/20050111580
[research_lo_chan]: https://doi.org/10.1109/smelec.1996.616492
[research_lobodovale_raffaelli_2021]: https://doi.org/10.3390/app112210631
[research_loewy_1969]: https://doi.org/10.2514/6.1969-202
[research_loewy_2000]: https://doi.org/10.2514/6.2000-1600
[research_lokos_lizotte_2005]: https://doi.org/10.2514/6.2005-6315
[research_lokos_olney_2002]: https://doi.org/10.2514/6.2002-1333
[research_lokos_olney_2002_b]: https://doi.org/10.2514/6.2002-2926
[research_lokoswilliama_millerericj_2015]: https://ntrs.nasa.gov/citations/20150000842
[research_lokoswilliama_staufrick_2004]: https://ntrs.nasa.gov/citations/20040075561
[research_lombaerts_2012]: https://doi.org/10.2514/6.2012-4512
[research_lombardi_salvetti_1997]: https://doi.org/10.2514/6.1997-1838
[research_londono_leonhardt_2012]: https://doi.org/10.2514/6.2012-4734
[research_long_1968]: https://doi.org/10.2514/6.1968-264
[research_longitudinal_control_2003]: https://doi.org/10.2514/5.9781600861840.0275.0283
[research_lorber_carta_1991]: https://doi.org/10.2514/6.1991-935
[research_loth_geubelle_2000]: https://doi.org/10.21236/ada378320
[research_lottati_1985]: https://doi.org/10.2514/3.45238
[research_lottati_1987]: https://doi.org/10.2514/3.45523
[research_lottati_1988]: https://doi.org/10.2514/3.45588
[research_lou_duan_2024]: https://doi.org/10.2514/6.2024-2489
[research_love_bohlmann_1991]: https://doi.org/10.2514/6.1991-1099
[research_love_lind_2010]: https://doi.org/10.2514/6.2010-7504
[research_low_pheh_2016]: https://doi.org/10.1109/aim.2016.7576787
[research_lowe_zingg_2021]: https://doi.org/10.2514/6.2021-2547
[research_lu_cui_2016]: https://doi.org/10.2514/6.2016-1226
[research_lu_huang_1993]: https://doi.org/10.2514/3.11436
[research_lu_lan_2026]: https://doi.org/10.1109/ccdc69976.2026.11560122
[research_lu_ma_2019]: https://doi.org/10.1109/access.2019.2956818
[research_lu_murthy_1990]: https://doi.org/10.2514/3.45947
[research_lu_yeh_1993]: https://doi.org/10.2514/6.1993-3285
[research_lucas_1978]: https://doi.org/10.21236/adb028240
[research_lucas_valasek_2009]: https://doi.org/10.2514/6.2009-2536
[research_luce_jr_1949]: https://doi.org/10.21236/ada278113
[research_luce_moore_1963]: https://doi.org/10.2514/6.1963-1030
[research_lukichev_demidova_2017]: https://doi.org/10.1109/ctsys.2017.8109577
[research_lum_xu_2016]: https://doi.org/10.1109/acc.2016.7525401
[research_luomaavroa_1944]: https://ntrs.nasa.gov/citations/19930092838
[research_luton_mook_1992]: https://doi.org/10.2514/6.1992-4652
[research_luton_mook_1993]: https://doi.org/10.2514/3.11930
[research_ly_gear_2006]: https://doi.org/10.21914/anziamj.v47i0.1046
[research_lykins_keshmiri_2010]: https://doi.org/10.2514/6.2010-7648
[research_lynch_rogers_1976]: https://doi.org/10.2514/6.1976-1505
[research_lyons_vepa_1973]: https://doi.org/10.2514/6.1973-832
[research_m_2026]: https://doi.org/10.36227/techrxiv.176827253.34525913/v1
[research_ma_liu_2023]: https://doi.org/10.1007/978-981-19-6613-2_101
[research_ma_wang_2009]: https://doi.org/10.2514/6.2009-55
[research_ma_wang_2022]: https://doi.org/10.3390/aerospace9110691
[research_maalawi_2012]: https://doi.org/10.5772/45878
[research_mabey_gaudet_1975]: https://doi.org/10.2514/3.44494
[research_macek_branco_2021]: https://doi.org/10.1016/j.measurement.2021.109910
[research_macek_marciniak_2021]: https://doi.org/10.1016/j.measurement.2021.109443
[research_machadoecosta_valarinho_2016]: https://doi.org/10.1016/j.engstruct.2016.09.014
[research_mack_1979]: https://doi.org/10.2514/6.1979-264
[research_macmillan_1981]: https://doi.org/10.2514/6.1981-2350
[research_macquart_werter_2016]: https://doi.org/10.2514/6.2016-1966
[research_madson_ericksont_1985]: https://doi.org/10.2514/6.1985-4093
[research_magar_fuchi_2018]: https://doi.org/10.1115/smasis2018-8040
[research_maharaj_1997]: https://doi.org/10.1049/ic:19970114
[research_mahesh_stone_1980]: https://doi.org/10.2514/6.1980-1758
[research_mahmood_2025]: https://doi.org/10.1177/10775463241312815
[research_maki_2016]: https://doi.org/10.2514/6.2016-3849
[research_mamedov_paryshev_2018]: https://doi.org/10.1615/tsagiscij.2018027114
[research_manan_cooper_2008]: https://doi.org/10.2514/6.2008-5868
[research_mancini_vos_2019]: https://doi.org/10.2514/6.2019-3272
[research_mandal_gu_2016]: https://doi.org/10.2514/6.2016-0636
[research_mangalam_flick_2007]: https://doi.org/10.2514/6.2007-6380
[research_mangalam_jutte_2010]: https://doi.org/10.2514/6.2010-8113
[research_mangalam_mangalam_2008]: https://doi.org/10.2514/6.2008-7187
[research_manimala_padfield_2004]: https://doi.org/10.1017/s0001924000000087
[research_mannarino_mantegazza_2014]: https://doi.org/10.2514/1.g000329
[research_mansfield_1953]: https://doi.org/10.1108/eb032280
[research_mao_guo_2023]: https://doi.org/10.54097/hset.v77i.14411
[research_marano_belardo_2022]: https://doi.org/10.3390/aerospace9070335
[research_marchetti_2023]: https://doi.org/10.21741/9781644902813-8
[research_marchmaniii_grantz_1982]: https://doi.org/10.2514/6.1982-128
[research_marciniuk_piskur_2024]: https://doi.org/10.3390/en17081801
[research_mardanpour_izadpanahi_2019]: https://doi.org/10.2514/1.j057183
[research_mardanpour_rastkar_2017]: https://doi.org/10.3390/aerospace4030035
[research_mardanpour_richards_2013]: https://doi.org/10.2514/6.2013-1571
[research_mardanpour_richards_2014]: https://doi.org/10.1016/j.jfluidstructs.2013.09.018
[research_marion_sharma_2025]: https://doi.org/10.2514/6.2025-97857
[research_marks_zientarski_2015]: https://doi.org/10.2514/6.2015-1051
[research_marks_zientarski_2016]: https://doi.org/10.2514/6.2016-1313
[research_marques_azevedo_2007]: https://doi.org/10.2514/1.27510
[research_marques_azevedo_2008]: https://doi.org/10.2514/1.32561
[research_marques_badcock_2010]: https://doi.org/10.2514/1.46971
[research_marques_badcock_2012]: https://doi.org/10.2514/1.c031103
[research_marretta_marino_2007]: https://doi.org/10.1243/09544100jaero98
[research_martin_1978]: https://doi.org/10.21236/ada066904
[research_martin_gerber_1953]: https://doi.org/10.21236/ad0005479
[research_martincodenverco_1966]: https://doi.org/10.21236/ad0378020
[research_marzocca_librescu_2002]: https://doi.org/10.2514/2.4970
[research_masarati_muscarello_2011]: https://doi.org/10.4050/vfs-f67-000318
[research_masarati_quaranta_2010]: https://doi.org/10.4050/vfs-f66-000353
[research_masarati_tod_2016]: https://doi.org/10.4050/f-0072-2016-11442
[research_mascolomer]: https://doi.org/10.70675/641c36e3z1c8ez400fzb0e4z97b4192e068b
[research_masini_timme_2019]: https://doi.org/10.1017/jfm.2019.906
[research_masini_timme_2020]: https://doi.org/10.2514/1.j059219
[research_maslan_sira_2018]: https://doi.org/10.1109/cpem.2018.8501038
[research_mason_1982]: https://doi.org/10.2514/6.1982-97
[research_mason_1983]: https://doi.org/10.2514/6.1983-1858
[research_mason_berg_1994]: https://doi.org/10.2514/3.21343
[research_mason_iglesias_2001]: https://doi.org/10.2514/6.2001-5234
[research_masson_veilleux_1999]: https://doi.org/10.2514/6.1999-3187
[research_masunaga_bueno_2019]: https://doi.org/10.26678/abcm.cobem2019.cob2019-1729
[research_mataich_elkhadiri_2025]: https://doi.org/10.37394/232022.2025.5.16
[research_matamoros_devisser_2018]: https://doi.org/10.2514/6.2018-1116
[research_matheny_panageas_1981]: https://doi.org/10.2514/6.1981-2433
[research_matsuzaki_ueda_1987]: https://doi.org/10.2514/6.1987-781
[research_matsuzaki_ueda_1989]: https://doi.org/10.2514/3.45763
[research_mattaboni_quaranta_2009]: https://doi.org/10.2514/1.40774
[research_matter_darabseh_2018]: https://doi.org/10.1007/s11012-018-0915-2
[research_matula_yalla_2026]: https://doi.org/10.5194/wes-2025-263
[research_maunder_1979]: https://doi.org/10.2514/6.1979-1803
[research_maute_farhat_2008]: https://doi.org/10.13052/remn.17.217-243
[research_mayer_lutz_2019]: https://doi.org/10.2514/1.c034969
[research_mayo_carroll_2016]: https://doi.org/10.1115/imece2016-65683
[research_mayya_karnick_2022]: https://doi.org/10.2514/6.2022-4173
[research_mayya_srivastava_2023]: https://doi.org/10.2514/6.2023-1565
[research_mballo_prasad_2022]: https://doi.org/10.4050/f-0078-2022-1255
[research_mcclain_pountney_1982]: https://doi.org/10.2514/6.1982-601
[research_mcclintock_1959]: https://doi.org/10.1063/1.1716731
[research_mccuish_caldwell_2018]: https://doi.org/10.1201/9781315136820-12
[research_mcdonald_shamroth_1982]: https://doi.org/10.1016/b978-0-12-493280-7.50014-0
[research_mcgurk_stodieck_2024]: https://doi.org/10.1016/j.compstruct.2023.117794
[research_mckenzie_1973]: https://doi.org/10.2514/6.1973-782
[research_mclean_1994]: https://doi.org/10.1049/cp:19940361
[research_mcnally_bachjr_1988]: https://doi.org/10.2514/6.1988-2134
[research_mcparlin_adamczak_2003]: https://doi.org/10.2514/6.2003-599
[research_mcquinn_valasek_2025]: https://doi.org/10.2514/6.2025-1249
[research_mctavish]: https://doi.org/10.22215/etd/2008-08205
[research_mehrark_euptank_1975]: https://ntrs.nasa.gov/citations/19750021936
[research_mehrark_tylerjs_1973]: https://ntrs.nasa.gov/citations/19740042090
[research_mehrotrasc_1980]: https://ntrs.nasa.gov/citations/19800015830
[research_mehta_marland_2017]: https://doi.org/10.2118/184634-ms
[research_meirovitch_1995]: https://doi.org/10.21236/ada293689
[research_meirovitch_tuzcu_2002]: https://doi.org/10.2514/6.2002-5055
[research_melton_schaeffler_2005]: https://doi.org/10.2514/1.10294
[research_melville_2000]: https://doi.org/10.2514/6.2000-2341
[research_melville_2002]: https://doi.org/10.2514/6.2002-2970
[research_melville_2021]: https://doi.org/10.32920/ryerson.14653311
[research_melville_gordnier_1998]: https://doi.org/10.2514/6.1998-2657
[research_meng_2021]: https://doi.org/10.32920/ryerson.14656272
[research_meng_hu_2024]: https://doi.org/10.20944/preprints202405.0475.v1
[research_meng_kaihua_2020]: https://doi.org/10.1109/icus50048.2020.9274846
[research_meng_wan_2021]: https://doi.org/10.1016/j.cja.2020.07.027
[research_meng_yu_2023]: https://doi.org/10.1109/ccdc58219.2023.10326492
[research_menshchikov_somov_2019]: https://doi.org/10.1063/1.5086976
[research_menzies_kandil_1996]: https://doi.org/10.2514/6.1996-3391
[research_meresman_ribak_2017]: https://doi.org/10.1098/rsos.171152
[research_merrett_hilton_2011]: https://doi.org/10.2514/6.2011-1716
[research_merrett_hilton_2011_b]: https://doi.org/10.2514/6.2011-6208
[research_mertaugh_1998]: https://doi.org/10.21236/ada350674
[research_mertins_elsholz_2005]: https://doi.org/10.1016/j.ast.2005.06.003
[research_methods_of_calculating_2015]: https://doi.org/10.20535/0203-377129201563837
[research_meyer_fields_1978]: https://doi.org/10.2514/6.1978-148
[research_meyerjr_schneider_1983]: https://doi.org/10.2514/6.1983-2747
[research_michel_stalla_2025]: https://doi.org/10.2514/6.2025-0902
[research_micheli_2024]: https://doi.org/10.2514/1.g008146
[research_micks_1950]: https://doi.org/10.2514/8.1784
[research_mihailaandres_larco_2017]: https://doi.org/10.1063/1.4992590
[research_mihailaandres_rosu_2017]: https://doi.org/10.1109/icmae.2017.8038669
[research_milanese_marzocca_2008]: https://doi.org/10.2514/6.2008-3866
[research_miller_decallafon_2011]: https://doi.org/10.2514/6.2011-6207
[research_miller_holguin_2014]: https://doi.org/10.2514/6.2014-0277
[research_miller_pena_2019]: https://doi.org/10.2514/6.2019-0227
[research_miller_protopapas_1979]: https://doi.org/10.2514/6.1979-1813
[research_miller_schemensky_1979]: https://doi.org/10.2514/6.1979-62
[research_miller_wood_1983]: https://doi.org/10.2514/6.1983-1816
[research_millerjr_1973]: https://doi.org/10.2514/6.1973-823
[research_miniature_slide_2002]: https://doi.org/10.1108/aa.2002.03322aaf.009
[research_minimum_performance]: https://doi.org/10.4271/as855
[research_minimum_performance_b]: https://doi.org/10.4271/as8003
[research_miodushevsky_ruggiero_2000]: https://doi.org/10.1142/9789812792013_0078
[research_miskin_takahashi_2018]: https://doi.org/10.2514/6.2018-4002
[research_miskin_takahashi_2019]: https://doi.org/10.2514/6.2019-3068
[research_mission_adaptive_flight]: https://ntrs.nasa.gov/citations/19930027277
[research_mission_adaptive_wing]: https://ntrs.nasa.gov/citations/19870060565
[research_missoum_2012]: https://doi.org/10.21236/ada582315
[research_mitchell_hoh_1984]: https://doi.org/10.2514/3.8551
[research_miyazawa_2000]: https://doi.org/10.2514/6.2000-4256
[research_mkhoyan_thakrar_2020]: https://doi.org/10.1115/smasis2020-2370
[research_mkhoyan_thakrar_2021]: https://doi.org/10.2514/6.2021-0477
[research_mkhoyan_wang_2022]: https://doi.org/10.2514/6.2022-1551
[research_mkhoyan_wang_2024]: https://doi.org/10.2514/6.2024-0832
[research_mocsanyi_takarics_2019]: https://doi.org/10.1109/gpmc48183.2019.9106961
[research_mocsanyi_takarics_2020]: https://doi.org/10.3390/fluids5020047
[research_model_reference_2016]: https://doi.org/10.1002/9781118823491.ch8
[research_model_rotor_2006]: https://doi.org/10.2514/5.9781600862373.0557.0578
[research_mohamed_abdelhady_2021]: https://doi.org/10.1007/s00348-021-03282-9
[research_mohamed_dongare_2021]: https://doi.org/10.1007/978-981-16-0104-0
[research_mohamed_g_2020]: https://doi.org/10.1016/j.ifacol.2020.06.013
[research_mohammadi_1999]: https://doi.org/10.2514/6.1999-182
[research_mohd_amoozgar_2025]: https://doi.org/10.1115/ssdm2025-152329
[research_molton_bur_2010]: https://doi.org/10.2514/6.2010-4595
[research_molton_dandois_2013]: https://doi.org/10.2514/1.j051000
[research_molusis_kleinman_1982]: https://doi.org/10.1109/cdc.1982.268383
[research_molz_breitsamter_2026]: https://doi.org/10.1016/j.ast.2026.113432
[research_moni_wales_2026]: https://doi.org/10.2514/6.2026-4251
[research_montel_thielecke_2015]: https://doi.org/10.2514/6.2015-2237
[research_montgomery_1971]: https://doi.org/10.2514/6.1971-955
[research_montgomery_hunsaker_2022]: https://doi.org/10.2514/6.2022-2531
[research_mooij_2020]: https://doi.org/10.2514/6.2020-1103
[research_mooij_wang_2021]: https://doi.org/10.2514/6.2021-1221
[research_moon_1996]: https://doi.org/10.21236/ada361169
[research_moore_1992]: https://doi.org/10.2514/6.1992-2100
[research_moore_1995]: https://doi.org/10.2514/3.46703
[research_moosavi_elasha_2022]: https://doi.org/10.3390/designs6020029
[research_moosavian_2021]: https://doi.org/10.32920/ryerson.14654676
[research_mor_livne_2004]: https://doi.org/10.2514/6.2004-1762
[research_mor_livne_2005]: https://doi.org/10.2514/1.10005
[research_moravejbarzani_shahverdi_2022]: https://doi.org/10.1177/10775463221074145
[research_mordfin_bloss_1962]: https://doi.org/10.1063/1.1717967
[research_morelli_2011]: https://doi.org/10.2514/6.2011-6672
[research_morelli_2012]: https://doi.org/10.2514/1.c031699
[research_morelli_klein_1995]: https://doi.org/10.2514/6.1995-3499
[research_moreno_pfifer_2015]: https://doi.org/10.1109/acc.2015.7171010
[research_moreno_seiler_2012]: https://doi.org/10.2514/6.2012-4859
[research_morgenstern_2004]: https://doi.org/10.2514/6.2004-4536
[research_morger_1988]: https://doi.org/10.2514/6.1988-2091
[research_morino_obayashi_2015]: https://doi.org/10.2514/1.c032775
[research_morphing_wing_2010]: https://doi.org/10.5220/0002885701140124
[research_morphing_wing_2018]: https://doi.org/10.1016/c2015-0-01317-x
[research_morton_cox_2012]: https://doi.org/10.2514/6.2012-1624
[research_moshier_2006]: https://doi.org/10.21236/ada448143
[research_moshtaghzadeh_rangel_2023]: https://doi.org/10.2514/6.2023-0587
[research_moszczynski_grant_2026]: https://doi.org/10.2514/6.2026-2210
[research_moulin_2004]: https://doi.org/10.2514/6.2004-5115
[research_moulin_idan_2001]: https://doi.org/10.2514/6.2001-1583
[research_moulin_idan_2002]: https://doi.org/10.2514/2.4860
[research_moulin_ritz_2010]: https://doi.org/10.2514/6.2010-7802
[research_moulin_zeng_2011]: https://doi.org/10.2514/6.2011-6370
[research_mouyon_cumer_2003]: https://doi.org/10.2514/6.2003-5417
[research_mu_huang_2022]: https://doi.org/10.1016/j.jsv.2022.116916
[research_mu_huang_2026]: https://doi.org/10.1016/j.jsv.2025.119440
[research_muchamadbayusaktipratama_erwinsulaeman_2022]: https://doi.org/10.37934/cfdl.14.1.2037
[research_muhamadjayadi_2025]: https://doi.org/10.35894/jtk.v10i1.259
[research_mukherjee_shaw_2004]: https://doi.org/10.21236/ada425857
[research_mukherjee_shaw_2007]: https://doi.org/10.21236/ada473600
[research_mukhopadhyay_1988]: https://doi.org/10.23919/acc.1988.4789734
[research_mukhopadhyay_1995]: https://doi.org/10.2514/3.46682
[research_mukhopadhyay_2003]: https://doi.org/10.2514/2.5108
[research_mulder_lubbers_2009]: https://doi.org/10.2514/6.2009-5692
[research_muller_woidt_2026]: https://doi.org/10.2514/1.c038139
[research_munoz_garciafogeda_2022]: https://doi.org/10.3390/aerospace9120804
[research_munoz_garciafogeda_2023]: https://doi.org/10.20944/preprints202311.0323.v1
[research_munoz_garciafogeda_2024]: https://doi.org/10.3390/aerospace11030198
[research_munozmedina]: https://doi.org/10.20868/upm.thesis.90592
[research_muradasodriozola]: https://doi.org/10.70675/2bd250f4zf819z440dz95c5z16c5e9b49af1
[research_murch_2008]: https://doi.org/10.2514/6.2008-6990
[research_murphy_klein_2004]: https://doi.org/10.2514/6.2004-5277
[research_murphy_mermagen_2004]: https://doi.org/10.2514/6.2004-5058
[research_murthy_lu_1992]: https://doi.org/10.1016/b978-0-12-012754-2.50012-1
[research_murugan_ganguli_2005]: https://doi.org/10.2514/1.5652
[research_muscarello_marzocca_2026]: https://doi.org/10.2514/6.2026-1648
[research_muscarello_masarati_2017]: https://doi.org/10.4050/jahs.62.022003
[research_muscati_grootenhuis_1975]: https://doi.org/10.1111/j.1475-1305.1975.tb00149.x
[research_mvsunil_menghal_2022]: https://doi.org/10.26634/jme.12.3.18591
[research_naca_conference_1949]: https://ntrs.nasa.gov/citations/19650074048
[research_nadimi_1999]: https://doi.org/10.32855/2642-2492.1455
[research_nadimmelhem_richardmunroe_2024]: https://doi.org/10.1201/9781003516903-2
[research_nae_stroe_2019]: https://doi.org/10.1063/1.5114362
[research_naftaly_raveh_2025]: https://doi.org/10.2514/6.2025-1021
[research_nailu_wentao_2025]: https://doi.org/10.1177/10775463251364763
[research_nair_goza_2022]: https://doi.org/10.2514/6.2022-1968
[research_najmi_siddiqui_2023]: https://doi.org/10.2139/ssrn.4568776
[research_nakadate_2005]: https://doi.org/10.2514/6.2005-7408
[research_nam_kim_1996]: https://doi.org/10.2514/6.1996-3984
[research_nam_kim_1997]: https://doi.org/10.2514/6.1997-1265
[research_namdeo_bhattacharyya_2023]: https://doi.org/10.2514/6.2023-4244
[research_nangia_palmer_2007]: https://doi.org/10.2514/6.2007-250
[research_napolitano_song_2001]: https://doi.org/10.1016/s1369-8869(00)00023-9
[research_narain_1983]: https://doi.org/10.2514/6.1983-186
[research_narayanaswamy_narayanan_2008]: https://doi.org/10.2514/6.2008-5971
[research_narimani_haddadpour_2025]: https://doi.org/10.1016/j.ast.2025.109992
[research_nash_timme_2025]: https://doi.org/10.2514/6.2025-3767
[research_nasukenichi_1986]: https://ntrs.nasa.gov/citations/19870009139
[research_navardi_shahverdi_2023]: https://doi.org/10.1142/s1758825122500910
[research_navardi_shahverdi_2026]: https://doi.org/10.1016/j.ast.2026.112391
[research_navratil_hostinsky_2024]: https://doi.org/10.1088/1742-6596/2716/1/012029
[research_naylor_1957]: https://doi.org/10.2514/8.3909
[research_nazhao_dengqingcao_2010]: https://doi.org/10.1109/isscaa.2010.5632395
[research_neumann_dealmeida_2020]: https://doi.org/10.1016/j.jfluidstructs.2020.102901
[research_newman_buttrill_1995]: https://doi.org/10.2514/6.1995-3250
[research_newman_kassem_1997]: https://doi.org/10.2514/6.1997-3621
[research_newman_kassem_1997_b]: https://doi.org/10.2514/2.4170
[research_newman_kassem_1997_c]: https://doi.org/10.2514/6.1997-457
[research_newman_schmidt_1994]: https://doi.org/10.2514/3.21326
[research_newmaniii_baysal_1992]: https://doi.org/10.2514/6.1992-4571
[research_newsom_1978]: https://doi.org/10.2514/6.1978-1270
[research_newsom_1979]: https://doi.org/10.2514/3.55894
[research_newsome_berkooz_1998]: https://doi.org/10.2514/2.550
[research_ng_ong_2020]: https://doi.org/10.1007/978-3-030-23792-9_7
[research_nguyen_2021]: https://doi.org/10.2514/6.2021-1129
[research_nguyen_cramer_2019]: https://doi.org/10.2514/6.2019-3156
[research_nguyen_cramer_2020]: https://doi.org/10.2514/6.2020-0214
[research_nguyen_fugate_2019]: https://doi.org/10.2514/6.2019-0217
[research_nguyen_hashemi_2018]: https://doi.org/10.2514/6.2018-0622
[research_nguyen_precup_2015]: https://doi.org/10.2514/6.2015-2417
[research_nguyen_reynolds_2018]: https://doi.org/10.2514/1.c034448
[research_nguyen_saussie_2018]: https://doi.org/10.1109/icuas.2018.8453440
[research_nguyen_swei_2015]: https://doi.org/10.2514/6.2015-0118
[research_nguyen_tal_2015]: https://doi.org/10.2514/6.2015-1843
[research_nguyen_ting_2013]: https://doi.org/10.2514/6.2013-4746
[research_nguyen_ting_2013_b]: https://doi.org/10.2514/6.2013-4859
[research_nguyen_ting_2015]: https://doi.org/10.2514/6.2015-1405
[research_nguyen_ting_2015_b]: https://doi.org/10.2514/6.2015-1840
[research_nguyen_ting_2016]: https://doi.org/10.2514/6.2016-1094
[research_nguyen_ting_2017]: https://doi.org/10.2514/6.2017-1589
[research_nguyen_ting_2018]: https://doi.org/10.2514/6.2018-2210
[research_nguyen_tuzcu_2009]: https://doi.org/10.2514/6.2009-6045
[research_nguyen_tuzcu_2011]: https://doi.org/10.2514/6.2011-6291
[research_nguyen_urnes_2012]: https://doi.org/10.2514/6.2012-4642
[research_nguyen_webb_2022]: https://doi.org/10.2514/6.2022-3594
[research_nguyen_xiong_2021]: https://doi.org/10.2514/6.2021-2574
[research_nguyen_xiong_2022]: https://doi.org/10.2514/6.2022-1325
[research_nguyen_xiong_2023]: https://doi.org/10.4050/f-0079-2023-18048
[research_nguyen_xiong_2023_b]: https://doi.org/10.2514/6.2023-0998
[research_nguyen_xiong_2023_c]: https://doi.org/10.2514/6.2023-3945
[research_nguyen_xiong_2024]: https://doi.org/10.2514/6.2024-0251
[research_nguyen_xiong_2024_b]: https://doi.org/10.2514/6.2024-4348
[research_nguyen_xiong_2026]: https://doi.org/10.2514/6.2026-1655
[research_nguyen_xiong_2026_b]: https://doi.org/10.2514/6.2026-2655
[research_nguyennhan_kaulupender_2015]: https://ntrs.nasa.gov/citations/20150023531
[research_nhannguyen_benjaminwebb]: https://ntrs.nasa.gov/citations/20220008237
[research_niblett_1986]: https://doi.org/10.2514/3.45369
[research_nicolaides_1976]: https://doi.org/10.21236/ada056569
[research_nicolas_sullivan_2016]: https://doi.org/10.3390/aerospace3030018
[research_nicolosi_cusati_2020]: https://doi.org/10.1007/978-3-030-36514-1_2
[research_niculescu_corcau_2021]: https://doi.org/10.1109/icate49685.2021.9465010
[research_nie_zhang_2009]: https://doi.org/10.1109/ical.2009.5262891
[research_niel]: https://doi.org/10.70675/0a5746acz2780z42a1z83e4zb2dace818ceb
[research_nieminen_tuohineva_2023]: https://doi.org/10.1016/j.ijfatigue.2023.107533
[research_nikolaos_spyridon_2024]: https://doi.org/10.21203/rs.3.rs-4764693/v1
[research_nilsson_yao_2023]: https://doi.org/10.31224/2981
[research_nisbet_brennan_1958]: https://doi.org/10.1121/1.1930026
[research_nisbet_brennan_1960]: https://doi.org/10.1121/1.1907878
[research_nissim_1975]: https://doi.org/10.2514/6.1975-822
[research_nissim_1976]: https://doi.org/10.2514/3.61416
[research_nissim_lottati_1979]: https://doi.org/10.2514/6.1979-792
[research_nissim_lottati_1979_b]: https://doi.org/10.2514/3.55895
[research_nissim_lottati_1980]: https://doi.org/10.2514/3.56000
[research_nissime_caspia_1976]: https://ntrs.nasa.gov/citations/19760019497
[research_nitzsche_1994]: https://doi.org/10.2514/3.46552
[research_niven_tait_2000]: https://doi.org/10.1017/s0001924000017875
[research_nixon_2020]: https://doi.org/10.2514/6.2020-2672
[research_nixon_piatak_2000]: https://doi.org/10.4050/jahs.45.270
[research_nixon_tzuoo_1987]: https://doi.org/10.2514/3.45510
[research_nixonmarkw_piatakdavidj_1999]: https://ntrs.nasa.gov/citations/19990050923
[research_noevere_wilhite_2016]: https://doi.org/10.2514/6.2016-0235
[research_noh_andreu_2025]: https://doi.org/10.1007/s11071-025-11265-2
[research_noll_calico_1983]: https://doi.org/10.2514/6.1983-2220
[research_noll_eastep_1983]: https://doi.org/10.2514/6.1983-991
[research_noll_eastep_1984]: https://doi.org/10.2514/3.48246
[research_noll_huttsell_1978]: https://doi.org/10.2514/6.1978-1459
[research_noll_huttsell_1979]: https://doi.org/10.2514/3.58553
[research_noll_huttsell_1980]: https://doi.org/10.2514/6.1980-764
[research_noll_merino_1976]: https://doi.org/10.2514/6.1976-1542
[research_noll_perryiii_1989]: https://doi.org/10.2514/6.1989-1168
[research_nomura_2003]: https://doi.org/10.2514/6.2003-4145
[research_norton_1989]: https://doi.org/10.2514/6.1989-1320
[research_norton_1990]: https://doi.org/10.21236/ada257262
[research_null_shkarayev_2004]: https://doi.org/10.2514/6.2004-2694
[research_null_shkarayev_2005]: https://doi.org/10.2514/1.12401
[research_numerical_calculation_2015]: https://doi.org/10.1002/9781118920978.ch2
[research_numerical_method_2013]: https://doi.org/10.1002/9781118451205.ch12
[research_nurohman_arifianto_2018]: https://doi.org/10.1088/1742-6596/1005/1/012020
[research_obayashi_sasaki_2000]: https://doi.org/10.1109/4235.850658
[research_oberkampf_1974]: https://doi.org/10.2514/6.1974-111
[research_obradovic_subbarao_2010]: https://doi.org/10.2514/6.2010-8236
[research_obrien_datta_2026]: https://doi.org/10.2514/1.c038655
[research_ockier_kolb_2017]: https://doi.org/10.4050/f-0073-2017-12180
[research_odonnell_mohseni_2019]: https://doi.org/10.2514/1.c034704
[research_odriozola_marquier_2026]: https://doi.org/10.2514/1.c038643
[research_oelker_friehmelt_1998]: https://doi.org/10.2514/6.1998-4263
[research_ogren_sotanski_1974]: https://doi.org/10.21236/ad0784134
[research_ohta_fujimori_1988]: https://doi.org/10.2514/6.1988-4114
[research_ohta_fujimori_1989]: https://doi.org/10.2514/3.20390
[research_ohta_nikiforuk_1984]: https://doi.org/10.2514/6.1984-1931
[research_ojiaku_prakash_2026]: https://doi.org/10.21203/rs.3.rs-9271663/v1
[research_oliver_singh_2020]: https://doi.org/10.2514/6.2020-1675
[research_olivett_corrao_2020]: https://doi.org/10.1115/smasis2020-2355
[research_on_selection_1972]: https://doi.org/10.1016/0022-4898(72)90055-9
[research_onkar_kumar_2024]: https://doi.org/10.1007/s12046-024-02629-2
[research_opgenoord_willcox_2018]: https://doi.org/10.2514/6.2018-4055
[research_oremland_suryakumar_2017]: https://doi.org/10.2514/6.2017-4354
[research_ormiston_2001]: https://doi.org/10.4050/vfs-f57-00011
[research_orr_2010]: https://doi.org/10.2514/6.2010-7642
[research_ossmann_poussotvassal_2018]: https://doi.org/10.1109/ccta.2018.8511549
[research_othman_silva_2019]: https://doi.org/10.1016/j.compstruct.2018.09.086
[research_ouellette_2017]: https://doi.org/10.2514/6.2017-0019
[research_ouellette_2026]: https://doi.org/10.2514/6.2026-1835
[research_ouellette_miller_2023]: https://doi.org/10.2514/6.2023-0377
[research_ouellette_patil_2010]: https://doi.org/10.2514/6.2010-7505
[research_ouellette_patil_2012]: https://doi.org/10.2514/6.2012-4640
[research_ouellette_patil_2014]: https://doi.org/10.2514/6.2014-0032
[research_ouyang_chen_2013]: https://doi.org/10.2514/1.c031915
[research_ouyang_gu_2021]: https://doi.org/10.1016/j.ast.2020.106457
[research_ouyang_jia_2026]: https://doi.org/10.56028/aetr.17.1.1413.2026
[research_overload_detection_2023]: https://doi.org/10.56726/irjmets41234
[research_owens_capone_2003]: https://doi.org/10.2514/6.2003-750
[research_owens_capone_2004]: https://doi.org/10.2514/1.3073
[research_owens_mcconnell_2006]: https://doi.org/10.2514/1.16972
[research_oyibo_1983]: https://doi.org/10.2514/3.8292
[research_oyibo_1984]: https://doi.org/10.2514/3.48423
[research_oz_ekici_2025]: https://doi.org/10.61112/jiens.1550755
[research_ozbay_1993]: https://doi.org/10.1016/s1474-6670(17)48848-3
[research_ozbay_turi]: https://doi.org/10.1109/cdc.1991.261840
[research_ozbek_ekici_2023]: https://doi.org/10.3390/drones7060379
[research_ozbek_ekici_2023_b]: https://doi.org/10.1007/978-3-031-37160-8_40
[research_ozbek_ekici_2024]: https://doi.org/10.1108/aeat-04-2024-0096
[research_ozger_2007]: https://doi.org/10.2514/6.2007-6718
[research_pachikara_lind_2012]: https://doi.org/10.2514/6.2012-4577
[research_padova_falk_1980]: https://doi.org/10.21236/ada088831
[research_padua_preisigheviana_2025]: https://doi.org/10.2514/6.2025-3459
[research_palacios_cesnik_2005]: https://doi.org/10.2514/6.2005-1945
[research_palacios_glaz_2009]: https://doi.org/10.4050/vfs-f65-000360
[research_paladini_drewiacki_2024]: https://doi.org/10.2139/ssrn.4815689
[research_palaia_salem_2025]: https://doi.org/10.2514/1.c038131
[research_paletta_belardo_2010]: https://doi.org/10.2514/1.c000265
[research_pan_huang_2019]: https://doi.org/10.5028/jatm.v11.1074
[research_pandita_chakraborty_2009]: https://doi.org/10.2514/6.2009-6258
[research_panel_flutter_1991]: https://doi.org/10.2514/6.1991-746
[research_pang_yin_2025]: https://doi.org/10.1109/icsi64877.2025.11009569
[research_paniagua_2013]: https://doi.org/10.21236/ada587666
[research_pankonien_durscher_2018]: https://doi.org/10.2514/6.2018-2930
[research_pankonien_durscher_2019]: https://doi.org/10.2514/6.2019-2358
[research_papadopoulos_1958]: https://doi.org/10.2514/8.7862
[research_paper_board]: https://doi.org/10.3403/30408899u
[research_papila_haftka_1999]: https://doi.org/10.2514/6.1999-1312
[research_paris_alaverdi_2005]: https://doi.org/10.2514/1.3172
[research_park_abla_1982]: https://doi.org/10.2514/6.1982-183
[research_park_abla_1983]: https://doi.org/10.2514/3.19811
[research_park_chung_2012]: https://doi.org/10.5139/jksas.2012.40.2.165
[research_park_lee_2001]: https://doi.org/10.2514/6.2001-4014
[research_parker_spain_1991]: https://doi.org/10.2514/6.1991-936
[research_parsons]: https://doi.org/10.22215/etd/2021-14794
[research_pasley_rohling_1973]: https://doi.org/10.2514/6.1973-791
[research_passive_wing_store_1982]: https://doi.org/10.1121/1.387660
[research_patartics_luspay_2017]: https://doi.org/10.1016/j.ifacol.2017.08.1263
[research_patidar_sarwar_2025]: https://doi.org/10.1134/s0015462825601494
[research_patil_2003]: https://doi.org/10.2514/6.2003-1800
[research_patil_clark_2002]: https://doi.org/10.2514/6.2002-1632
[research_patil_hodges_2000]: https://doi.org/10.2514/2.2685
[research_patil_hodges_2000_b]: https://doi.org/10.2514/6.2000-1627
[research_patil_patil_1997]: https://doi.org/10.2514/6.1997-15
[research_paul]: https://doi.org/10.15368/theses.2017.65
[research_paul_rein_2016]: https://doi.org/10.2514/6.2016-0799
[research_paul_rein_2017]: https://doi.org/10.2514/1.c034080
[research_pavanasam_anil_2024]: https://doi.org/10.4271/2024-26-0447
[research_pavlenko_reslan_2022]: https://doi.org/10.34759/vst-2022-3-17-28
[research_pavlov_pavlov_2024]: https://doi.org/10.3103/s1068799824020041
[research_pawlak_1994]: https://doi.org/10.2514/6.1994-2116
[research_pearsonhenrya_aikenwilliamsjr_1944]: https://ntrs.nasa.gov/citations/19930091876
[research_pecora_2018]: https://doi.org/10.1115/smasis2018-8108
[research_pecora_amoroso_2012]: https://doi.org/10.2514/1.c000328
[research_pecora_amoroso_2018]: https://doi.org/10.1117/12.2300173
[research_pecora_amoroso_2021]: https://doi.org/10.1117/12.2580861
[research_pecora_pecora_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00014-9
[research_pedreiro_takahara_1998]: https://doi.org/10.2514/6.1998-4518
[research_pedreiro_takahara_1999]: https://doi.org/10.2514/2.2539
[research_peeleel_eckstromcv_1975]: https://ntrs.nasa.gov/citations/19750023957
[research_pellegrino_quaranta_2022]: https://doi.org/10.4050/f-0078-2022-1163
[research_peloubetjr_haller_1983]: https://doi.org/10.2514/6.1983-995
[research_pendleton_bessette_1998]: https://doi.org/10.2514/6.1998-1972
[research_pendleton_flick_2007]: https://doi.org/10.2514/6.2007-1855
[research_peng_2011]: https://doi.org/10.4028/www.scientific.net/amr.284-286.2456
[research_peng_wang_2024]: https://doi.org/10.3390/app14199078
[research_penning_zink_2009]: https://doi.org/10.2514/6.2009-2405
[research_perera_guo_2008]: https://doi.org/10.2514/6.2008-5969
[research_perezbecker_marten_2021]: https://doi.org/10.5194/wes-2021-1
[research_perkins_brice_1966]: https://doi.org/10.21236/ad0632829
[research_perryiii_mukhopadhyay_1990]: https://doi.org/10.2514/6.1990-1074
[research_persoon_roos_1980]: https://doi.org/10.21236/ada097094
[research_peschel_roske_2000]: https://doi.org/10.1016/s0263-2241(99)00056-1
[research_peter_stumpf_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00003-4
[research_petermeier_radtke_2010]: https://doi.org/10.2514/6.2010-9075
[research_peters_1988]: https://doi.org/10.1016/0895-7177(88)90501-8
[research_petersen_1981]: https://doi.org/10.2514/6.1981-2417
[research_petronevich_lyutov_2021]: https://doi.org/10.34759/vst-2021-4-48-61
[research_pettit_grandhi_2003]: https://doi.org/10.2514/2.7208
[research_pfaff_1965]: https://doi.org/10.21236/ad0467448
[research_pfeifle_fichter_2021]: https://doi.org/10.2514/6.2021-1457
[research_pfeifle_fichter_2021_b]: https://doi.org/10.2514/6.2021-1457.c1
[research_pfeifle_fichter_2023]: https://doi.org/10.2514/1.g006929
[research_phan_2020]: https://doi.org/10.1016/j.istruc.2020.08.035
[research_philipsen_zhai_2007]: https://doi.org/10.2514/6.2007-143
[research_phillips]: https://doi.org/10.33915/etd.3049
[research_phillips_white_2022]: https://doi.org/10.2514/6.2022-2555
[research_piatakdavidj_clecknercraigs_2002]: https://ntrs.nasa.gov/citations/20030013003
[research_picard_2002]: https://doi.org/10.21236/ada409130
[research_pines_dugundji_1955]: https://doi.org/10.2514/8.3436
[research_pines_newman_1974]: https://doi.org/10.2514/3.59251
[research_pitt_2004]: https://doi.org/10.2514/6.2004-1754
[research_pitt_sexton_2016]: https://doi.org/10.2514/6.2016-1960
[research_pittford_stevens_2012]: https://doi.org/10.2514/6.2012-2840
[research_plaban_takahashi_2021]: https://doi.org/10.2514/6.2021-2423
[research_plaetschke_mulder_1982]: https://doi.org/10.1016/s1474-6670(17)63152-5
[research_plath]: https://doi.org/10.70675/9415f5c4zb15ez4e25z87c4z376e176813a2
[research_polonsky_2026]: https://doi.org/10.2514/1.c038869
[research_pomin_altmikus_2001]: https://doi.org/10.1007/978-3-642-56548-9_26
[research_poojari_2022]: https://doi.org/10.47893/gret.2022.1089
[research_poole_allen_2020]: https://doi.org/10.2514/6.2020-0042
[research_poole_allen_2020_b]: https://doi.org/10.2514/6.2020-0404
[research_poomadath_ajaj_2025]: https://doi.org/10.2514/6.2025-3472
[research_popelka_lindsay_1997]: https://doi.org/10.4050/jahs.42.126
[research_poplingher_mallik_2022]: https://doi.org/10.2514/6.2022-2314
[research_porter_gu_1991]: https://doi.org/10.2514/6.1991-2814
[research_porter_merzougui_1992]: https://doi.org/10.2514/6.1992-2105
[research_porter_merzougui_1992_b]: https://doi.org/10.2514/6.1992-2104
[research_porterfield_alexander_1970]: https://doi.org/10.4050/jahs.15.3.22
[research_pototzky_2010]: https://doi.org/10.2514/6.2010-7801
[research_potvin_grant_2026]: https://doi.org/10.2514/6.2026-1883.c1
[research_pourtakdoust_khodabakhsh_2026]: https://doi.org/10.1016/j.ast.2025.111214
[research_poussotvassal_vuillemin_2022]: https://doi.org/10.2514/6.2022-1044
[research_powers_webb_1992]: https://doi.org/10.2514/6.1992-4101
[research_prabhakar_2025]: https://doi.org/10.52843/cassyni.fjt1xn
[research_prabhakar_murugan_2022]: https://doi.org/10.1115/smasis2022-90198
[research_prabhakar_murugan_2026]: https://doi.org/10.1007/978-3-032-16528-2_26
[research_prasannakumar_sudhi_2022]: https://doi.org/10.2514/6.2022-3550
[research_prasanth_mehra_1999]: https://doi.org/10.2514/6.1999-4089
[research_prato_facello_2026]: https://doi.org/10.1016/j.measurement.2025.119568
[research_prazenica_2014]: https://doi.org/10.2514/6.2014-2188
[research_prazenica_reisenthel_2004]: https://doi.org/10.2514/6.2004-1939
[research_precup_mor_2018]: https://doi.org/10.2514/6.2018-3106
[research_pressures_and_2000]: https://doi.org/10.1016/b978-012257060-5/50023-x
[research_price_koffi_2002]: https://doi.org/10.2514/6.2002-1210
[research_prochazka_eduardo_2018]: https://doi.org/10.1109/ccta.2018.8511538
[research_properties_and_2012]: https://doi.org/10.2514/5.9781600869228.0338.0438
[research_properties_of_2014]: https://doi.org/10.2514/5.9781624102547.0625.0632
[research_properties_of_2024]: https://doi.org/10.2514/5.9781624107252.0695.0702
[research_proulxcabana]: https://doi.org/10.70675/92307e29z7167z4596zbe27z41aa8212d0c8
[research_prudhomme_1995]: https://doi.org/10.2514/6.1995-3308
[research_prudhomme_prudhomme_1997]: https://doi.org/10.2514/6.1997-3622
[research_psarros_savaidis_2025]: https://doi.org/10.3390/engproc2025090038
[research_psfcc]: https://ntrs.nasa.gov/citations/19970041277
[research_psollabress_haselmeyer]: https://doi.org/10.1109/iciasf.2001.960272
[research_puentes_takahashi_2024]: https://doi.org/10.2514/6.2024-0001
[research_punzi_crooks_2024]: https://doi.org/10.4050/f-0080-2024-1149
[research_pursel_1977]: https://doi.org/10.2514/6.1977-1514
[research_purserpe_tuckerwa_1949]: https://ntrs.nasa.gov/citations/19650074054
[research_purwadi_hidayat_2023]: https://doi.org/10.1063/5.0181422
[research_pusch_2017]: https://doi.org/10.1109/ccta.2017.8062766
[research_pusch_2018]: https://doi.org/10.2514/6.2018-0618
[research_pusch_kier_2022]: https://doi.org/10.2514/6.2022-0439
[research_pusch_knoblach_2019]: https://doi.org/10.1007/s13272-019-00367-4
[research_pushtaev_1989]: https://doi.org/10.1016/0041-5553(89)90024-4
[research_puyou_berard_2007]: https://doi.org/10.3182/20070625-5-fr-2916.00085
[research_qi_ting_2015]: https://doi.org/10.1109/chicc.2015.7259631
[research_qian_2018]: https://doi.org/10.1061/(asce)as.1943-5525.0000925
[research_qian_alonso_2021]: https://doi.org/10.2514/6.2021-1967
[research_qian_huang_2014]: https://doi.org/10.1016/j.cja.2014.03.004
[research_qian_huang_2014_b]: https://doi.org/10.1016/j.cja.2014.10.011
[research_qiao_wang_2025]: https://doi.org/10.23967/j.rimni.2024.10.56530
[research_qiao_zhou_2018]: https://doi.org/10.2514/6.2018-4148
[research_qiao_zhou_2019]: https://doi.org/10.1109/aero.2019.8742016
[research_qin_2012]: https://doi.org/10.1007/978-3-642-25688-2_7
[research_qin_librescu_2003]: https://doi.org/10.2514/2.3127
[research_qin_liu_2023]: https://doi.org/10.1049/cth2.12427
[research_qin_wei_2023]: https://doi.org/10.23919/ccc58697.2023.10240514
[research_qin_zhang_2013]: https://doi.org/10.4028/www.scientific.net/amm.459.669
[research_qiu_ang_2019]: https://doi.org/10.1155/2019/5046395
[research_qiu_wang_2021]: https://doi.org/10.1109/iscsic54682.2021.00017
[research_qiu_xu_2018]: https://doi.org/10.1177/1077546318764191
[research_qu_li_2022]: https://doi.org/10.1088/1742-6596/2258/1/012074
[research_qu_xu_2025]: https://doi.org/10.2139/ssrn.5182532
[research_quach_2026]: https://doi.org/10.2139/ssrn.6368418
[research_quach_2026_b]: https://doi.org/10.1038/s41598-026-67574-y
[research_quackenbush_keller_2009]: https://doi.org/10.2514/6.2009-6142
[research_quaranta_masarati_2013]: https://doi.org/10.4050/vfs-f69-0222
[research_quero_2025]: https://doi.org/10.1016/j.jfluidstructs.2025.104435
[research_raab_2014]: https://doi.org/10.2514/6.2014-0730
[research_raab_2026]: https://doi.org/10.21741/9781644904251-262
[research_rade_desouza_2016]: https://doi.org/10.21236/ad1009258
[research_radestock_falken_2018]: https://doi.org/10.1115/smasis2018-7976
[research_raghunathan_coll_1981]: https://doi.org/10.2514/3.7765
[research_raghunathan_mitchell_1998]: https://doi.org/10.1007/s001930050113
[research_rahman_li_2013]: https://doi.org/10.4028/www.scientific.net/amm.419.55
[research_rahnd_reinertsonl_1986]: https://ntrs.nasa.gov/citations/19860022091
[research_rains_huang_2024]: https://doi.org/10.2514/6.2024-2264
[research_raisinghani_adak_1983]: https://doi.org/10.1080/00207728308926538
[research_raisinghani_kumar_1995]: https://doi.org/10.2514/6.1995-3435
[research_raj_1983]: https://doi.org/10.2514/6.1983-262
[research_raja_upadhya_2007]: https://doi.org/10.2514/1.21660
[research_rajpal_mitrotta_2021]: https://doi.org/10.1016/j.compstruct.2021.114373
[research_rakin_1981]: https://doi.org/10.2514/6.1981-2461
[research_ralucamaxim_2020]: https://doi.org/10.33422/ejbs.v2i2.148
[research_rambacher_bons_2023]: https://doi.org/10.2514/6.2023-1239
[research_ramlal_desai_2025]: https://doi.org/10.2139/ssrn.5381976
[research_rao_behal]: https://doi.org/10.1109/cdc.2005.1582536
[research_rao_behal_2005]: https://doi.org/10.2514/6.2005-6250
[research_rao_kronenberger_1978]: https://doi.org/10.21236/ada055619
[research_rao_padmanabhan_2019]: https://doi.org/10.1504/ijndc.2019.103285
[research_raol_singh_2023]: https://doi.org/10.1201/9781003293514-12
[research_raol_singh_2023_b]: https://doi.org/10.1201/9781003293514-10
[research_raoof_kraincanic_1998]: https://doi.org/10.1016/s0045-7949(98)00128-x
[research_ratcliff_bodkin_2016]: https://doi.org/10.2514/6.2016-3854
[research_ratliff_pagilla_2008]: https://doi.org/10.1109/acc.2008.4586722
[research_raveh_2026]: https://doi.org/10.52843/cassyni.yvbqts
[research_raveh_levy_2004]: https://doi.org/10.2514/6.2004-1515
[research_raveh_sodja_2023]: https://doi.org/10.52843/cassyni.zm5mgk
[research_re_2014]: https://doi.org/10.4271/2014-01-2137
[research_rea_pecora_2017]: https://doi.org/10.18178/ijmerr.6.6.
[research_rea_pecora_2018]: https://doi.org/10.18178/ijmerr.6.6.440-450
[research_reasor_bhamidipati_2016]: https://doi.org/10.2514/6.2016-1053
[research_recine_schuh_2025]: https://doi.org/10.2514/6.2025-0457
[research_reddy_1987]: https://doi.org/10.2514/3.45421
[research_rediess_melton_1994]: https://doi.org/10.2514/6.1994-2172
[research_reding_ericsson_1977]: https://doi.org/10.2514/3.58883
[research_regan_1964]: https://doi.org/10.21236/ad0600975
[research_rehfield_chang_1991]: https://doi.org/10.2514/6.1991-1186
[research_reich_raveh_2002]: https://doi.org/10.2514/6.2002-1633
[research_reich_raveh_2004]: https://doi.org/10.2514/1.78
[research_reichenbach_2008]: https://doi.org/10.2514/6.2008-7189
[research_reichenbach_castelluccio_2011]: https://doi.org/10.2514/6.2011-1956
[research_reichenbach_urnes_2009]: https://doi.org/10.2514/6.2009-6143
[research_reichhoormart_lin_1995]: https://doi.org/10.2514/6.1995-1193
[research_reinbold_breitsamter_2026]: https://doi.org/10.2514/1.c038409
[research_reist_koo_2022]: https://doi.org/10.2514/1.c036754
[research_rendina_mazzoni_1999]: https://doi.org/10.1002/stc.4300060108
[research_renken_1985]: https://doi.org/10.2514/6.1985-5006
[research_rennie_jumper_1995]: https://doi.org/10.2514/6.1995-1904
[research_rennie_jumper_1997]: https://doi.org/10.2514/2.2236
[research_report_no_1935]: https://doi.org/10.1016/s0016-0032(35)90062-x
[research_requirements_of_1967]: https://doi.org/10.2514/6.1967-376
[research_reschke_2005]: https://doi.org/10.2514/6.2005-6026
[research_rester_ac_1984]: https://doi.org/10.21236/ada150316
[research_rester_alfredc_1988]: https://doi.org/10.21236/ada198399
[research_reuther_jameson_1995]: https://doi.org/10.1115/imece1995-0954
[research_revivo_raveh_2025]: https://doi.org/10.2514/6.2025-1018
[research_rhoads_1952]: https://doi.org/10.21236/ad0014479
[research_ricci_degaspari_2016]: https://doi.org/10.2514/6.2016-1316
[research_ricci_marchetti_2022]: https://doi.org/10.2514/6.2022-0166
[research_ricci_scotti_2008]: https://doi.org/10.2514/6.2008-1727
[research_ricci_scotti_2008_b]: https://doi.org/10.2514/1.33303
[research_ricci_scotti_2009]: https://doi.org/10.2514/6.2009-2511
[research_richard_rule_2000]: https://doi.org/10.1115/imece2000-1708
[research_richard_rule_2001]: https://doi.org/10.1115/1.1389458
[research_richardson_kesler_1988]: https://doi.org/10.2514/6.1988-4143
[research_richter_khalifa_2023]: https://doi.org/10.1016/j.procir.2023.06.032
[research_rieck_herrmann_2026]: https://doi.org/10.21203/rs.3.rs-8496708/v1
[research_riemersma_lammertink_1988]: https://doi.org/10.1016/0021-9290(88)90239-4
[research_rigatos_dala_2026]: https://doi.org/10.1007/s42417-026-02349-3
[research_righi_2017]: https://doi.org/10.1108/aeat-01-2017-0051
[research_rill_ganzer_1988]: https://doi.org/10.2514/6.1988-2039
[research_rimer_chipman_1984]: https://doi.org/10.2514/6.1984-1866
[research_rimer_chipman_1984_b]: https://doi.org/10.2514/3.45034
[research_rimer_chipman_1986]: https://doi.org/10.2514/3.20069
[research_riou_garnier_2010]: https://doi.org/10.2514/1.j050531
[research_rising_1982]: https://doi.org/10.2514/6.1982-1297
[research_ritter_dillinger_2017]: https://doi.org/10.2514/6.2017-0637
[research_rizk_1980]: https://doi.org/10.2514/6.1980-125
[research_rizzetta_1977]: https://doi.org/10.21236/ada057505
[research_rizzetta_1995]: https://doi.org/10.2514/6.1995-2282
[research_rizzi_1981]: https://doi.org/10.1007/978-3-663-14008-5_18
[research_rizzi_1981_b]: https://doi.org/10.1007/978-3-663-14008-5_16
[research_rizzi_1984]: https://doi.org/10.2514/6.1984-2142
[research_rizzi_1995]: https://doi.org/10.1007/978-3-642-79440-7_9
[research_rizzi_purcell_1986]: https://doi.org/10.1007/978-3-642-82770-9_23
[research_ro_barlow_1992]: https://doi.org/10.2514/6.1992-46
[research_roberts_smith_1966]: https://doi.org/10.21236/ad0635953
[research_robins_carlson_1979]: https://doi.org/10.2514/6.1979-1871
[research_robins_carlson_1980]: https://doi.org/10.2514/3.57919
[research_robinson]: https://doi.org/10.22215/etd/2018-13315
[research_robinson_b]: https://doi.org/10.1007/978-3-540-73719-3_11
[research_rocha_moniz_2005]: https://doi.org/10.2514/1.308
[research_rocha_moniz_2007]: https://doi.org/10.1080/15376490600864505
[research_rochadacosta]: https://doi.org/10.22215/etd/2017-11781
[research_rock_ashley_1993]: https://doi.org/10.2514/6.1993-3817
[research_rodden_1956]: https://doi.org/10.2514/8.3630
[research_rodden_1981]: https://doi.org/10.2514/3.44744
[research_rodden_1984]: https://doi.org/10.2514/3.56737
[research_rodden_1989]: https://doi.org/10.2514/3.45825
[research_rodden_bellinger_1982]: https://doi.org/10.2514/3.61559
[research_rodden_love_1984]: https://doi.org/10.2514/6.1984-986
[research_rodden_love_1985]: https://doi.org/10.2514/3.45205
[research_roeser_monnich_2024]: https://doi.org/10.1007/978-3-031-69425-7_5
[research_roger_hodges_1974]: https://doi.org/10.2514/6.1974-402
[research_rogers_1998]: https://doi.org/10.2514/6.1998-4324
[research_rogers_2007]: https://doi.org/10.2514/6.2007-6305
[research_roknizadeh_nobari_2012]: https://doi.org/10.1108/00022661211255485
[research_rolling_mla_active]: https://ntrs.nasa.gov/citations/19920022107
[research_roohani_skews_2009]: https://doi.org/10.1007/978-3-540-85181-3_98
[research_roos_bennekers_1975]: https://doi.org/10.2514/6.1975-864
[research_rose_jinu_2014]: https://doi.org/10.1177/0954410014537241
[research_rosemann_birkemeyer_2002]: https://doi.org/10.1007/978-3-540-45856-2_12
[research_rosenberg_1944]: https://doi.org/10.2514/8.11091
[research_roskamj_lanc_1972]: https://ntrs.nasa.gov/citations/19730013170
[research_roskamj_lanc_1973]: https://ntrs.nasa.gov/citations/19730013169
[research_ross_law_1993]: https://doi.org/10.2514/6.1993-4385
[research_roughen_bendiksen_2010]: https://doi.org/10.2514/6.2010-8397
[research_rowan_burns_1975]: https://doi.org/10.2514/3.59890
[research_rowley_2008]: https://doi.org/10.21236/ada476708
[research_rowley_2010]: https://doi.org/10.21236/ada547432
[research_roy_eversman_1996]: https://doi.org/10.2514/3.47014
[research_roysdon_khalid_2010]: https://doi.org/10.2514/6.2010-9167
[research_roysdon_khalid_2011]: https://doi.org/10.2514/6.2011-1563
[research_rubillo_bollt_2005]: https://doi.org/10.2514/6.2005-2076
[research_rufino_faria_2026]: https://doi.org/10.2139/ssrn.6153395
[research_ruhlin_prattbarlow_1981]: https://doi.org/10.2514/6.1981-654
[research_ruizgarcia_brown_2022]: https://doi.org/10.2514/6.2022-0713
[research_rule_richard_2000]: https://doi.org/10.2514/6.2000-1629
[research_rule_richard_2001]: https://doi.org/10.2514/2.4828
[research_ruler_1967]: https://doi.org/10.1111/j.1475-1305.1967.tb00889.x
[research_rumpfkeil_lickenbrock_2021]: https://doi.org/10.2514/6.2021-0732
[research_russo_tognaccini_2020]: https://doi.org/10.2514/6.2020-0447
[research_russo_tognaccini_2020_b]: https://doi.org/10.2514/1.j059080
[research_rustenburg_1973]: https://doi.org/10.21236/ad0761491
[research_rutkowski_1979]: https://doi.org/10.2514/3.58539
[research_s_a_2025]: https://doi.org/10.37591/jopc.v13i04.215732
[research_sabatini_coppotelli_2026]: https://doi.org/10.2514/1.g009632
[research_sabatini_livne_2026]: https://doi.org/10.2514/6.2026-1443
[research_sacchi_healy_2025]: https://doi.org/10.2514/6.2025-0713
[research_sackett_kirchwey_1982]: https://doi.org/10.2514/6.1982-1535
[research_sadien_carton_2019]: https://doi.org/10.23919/acc.2019.8814718
[research_sadien_roos_2020]: https://doi.org/10.1016/j.conengprac.2019.104228
[research_sagee_akylas]: https://doi.org/10.1109/icmts.1988.672958
[research_sahasrabudhe_celi_1997]: https://doi.org/10.2514/2.4034
[research_sahin_cakir_2018]: https://doi.org/10.1051/matecconf/201818804002
[research_sahin_cakir_2018_b]: https://doi.org/10.1051/matecconf/201823300006
[research_sahoo_cesnik_2002]: https://doi.org/10.2514/6.2002-1720
[research_sahyoun_boose_2026]: https://doi.org/10.1007/s13272-026-00954-2
[research_sainio_krandel_1993]: https://doi.org/10.2514/6.1993-1162
[research_saitoh_hashidate_1995]: https://doi.org/10.2514/6.1995-3926
[research_sakamura_komaki_2011]: https://doi.org/10.1007/s00193-011-0347-6
[research_saltari_pizzoli_2022]: https://doi.org/10.2514/6.2022-1187
[research_sampo_sorniotti_2010]: https://doi.org/10.4271/2010-01-0094
[research_samuels_1982]: https://doi.org/10.2514/3.57418
[research_sandahlcarla_1948]: https://ntrs.nasa.gov/citations/19930085384
[research_sanders_eastep_2003]: https://doi.org/10.2514/2.3062
[research_sandford_ricketts_1980]: https://doi.org/10.2514/6.1980-738
[research_sangbumchoi_haojianxu]: https://doi.org/10.1109/cdc.2003.1272404
[research_sanghi_cesnik_2024]: https://doi.org/10.2514/1.c037470
[research_sanghi_riso_2020]: https://doi.org/10.2514/6.2020-2645
[research_sanghi_riso_2022]: https://doi.org/10.2514/6.2022-4093
[research_sanmugadas_gupta_2021]: https://doi.org/10.2514/6.2021-3084
[research_santos_marques_2026]: https://doi.org/10.4050/f-0082-2026-0072
[research_sapkal_attar_2011]: https://doi.org/10.2514/6.2011-1743
[research_sapkal_attar_2012]: https://doi.org/10.2514/1.j051212
[research_sardahi_kolonay_2021]: https://doi.org/10.23919/acc50511.2021.9482767
[research_saric_2010]: https://doi.org/10.21236/ada564004
[research_sarnico_1993]: https://doi.org/10.2514/6.1993-4606
[research_sarojini_solano_2022]: https://doi.org/10.2514/6.2022-4054
[research_sartor]: https://doi.org/10.70675/0127f7c9zede5z4492z9342z76d03852c137
[research_sartor_clement_2013]: https://doi.org/10.2514/6.2013-2735
[research_sartor_losfeld_2012]: https://doi.org/10.1007/s00348-012-1330-4
[research_sarvankar_sarkar_2023]: https://doi.org/10.1115/gtindia2023-118416
[research_sarvankar_sarkar_2024]: https://doi.org/10.1115/1.4065408
[research_sattar_wang_2020]: https://doi.org/10.1109/anzcc50923.2020.9318355
[research_sazesh_shams_2017]: https://doi.org/10.1016/j.jfluidstructs.2017.05.005
[research_scalera_durham_1999]: https://doi.org/10.2514/6.1999-4281
[research_scaramal_horn_2022]: https://doi.org/10.2514/6.2022-3281
[research_scaramal_horn_2023]: https://doi.org/10.2514/1.g007192
[research_scaramal_saetti_2021]: https://doi.org/10.4050/f-0077-2021-16792
[research_scarth_sartor_2015]: https://doi.org/10.2514/6.2015-0918
[research_schack_2020]: https://doi.org/10.21014/acta_imeko.v9i5.971
[research_schajer_2021]: https://doi.org/10.1007/s11340-021-00771-0
[research_schauerte_kwong_2026]: https://doi.org/10.2514/6.2026-2314
[research_schewe_mai_2019]: https://doi.org/10.1016/j.jfluidstructs.2018.07.005
[research_schildkamp_chang_2023]: https://doi.org/10.3390/act12070280
[research_schlemmer_dehmlow_2020]: https://doi.org/10.2514/6.2020-1188
[research_schmidt_1986]: https://doi.org/10.2514/6.1986-2077
[research_schmidt_1986_b]: https://doi.org/10.2514/6.1986-2711
[research_schmidt_1991]: https://doi.org/10.2514/6.1991-3316
[research_schmidt_1995]: https://doi.org/10.2514/6.1995-3200
[research_schmidt_2016]: https://doi.org/10.2514/6.2016-2099
[research_schmidt_chavez_2001]: https://doi.org/10.2514/6.2001-4020
[research_schmidt_newman_1988]: https://doi.org/10.2514/6.1988-4079
[research_schmidt_newman_1990]: https://doi.org/10.2514/6.1990-3446
[research_schmitt_destarac_1983]: https://doi.org/10.2514/6.1983-1804
[research_schneider]: https://doi.org/10.70675/b8e9486dz5049z42bdz806cz7c4ff08ef266
[research_scholes_slater_1970]: https://doi.org/10.1243/03093247v054242
[research_schoneman_2019]: https://doi.org/10.2514/6.2019-1119
[research_schreyer_selm_2026]: https://doi.org/10.2514/6.2026-0256
[research_schroder_meijering_2005]: https://doi.org/10.1002/gamm.201490013
[research_schuelein_2008]: https://doi.org/10.2514/6.2008-4208
[research_schulze_danowsky_2016]: https://doi.org/10.2514/6.2016-2007
[research_schumann_wustenhagen_2025]: https://doi.org/10.2514/6.2025-0083
[research_schuster_1995]: https://doi.org/10.2514/3.46686
[research_schuster_vadyak_1990]: https://doi.org/10.2514/3.45942
[research_schusterdavidm_byrdjamese_2003]: https://ntrs.nasa.gov/citations/20030009796
[research_schusterdavidm_edwardsjohnw_2004]: https://ntrs.nasa.gov/citations/20040086524
[research_schwanz_grimes_1980]: https://doi.org/10.2514/6.1980-1635
[research_schwanz_wells_1980]: https://doi.org/10.2514/6.1980-1634
[research_schweikert_patel_2022]: https://doi.org/10.2514/6.2022-3355
[research_schweikhard_1966]: https://doi.org/10.2514/6.1966-468
[research_schweikhard_1967]: https://doi.org/10.2514/3.43804
[research_sclafani_slotnick_2012]: https://doi.org/10.2514/6.2012-2919
[research_scordamaglia_mattei_2025]: https://doi.org/10.1109/ojcsys.2025.3619810
[research_scott_allen_2015]: https://doi.org/10.2514/6.2015-1172
[research_scott_coulson_2011]: https://doi.org/10.2514/6.2011-1960
[research_scott_vetter_2008]: https://doi.org/10.2514/6.2008-7186
[research_sebastia_hornung_2023]: https://doi.org/10.2514/6.2023-3528
[research_sebastia_wurz_2024]: https://doi.org/10.2514/6.2024-3997
[research_sebastiano_ricci_2013]: https://doi.org/10.2514/6.2013-1704
[research_seber_sakarya_2010]: https://doi.org/10.2514/1.c000312
[research_seber_sakarya_2011]: https://doi.org/10.2514/6.2011-1715
[research_seebass_1982]: https://doi.org/10.1016/b978-0-12-493280-7.50007-3
[research_segawa_gopalarathnam_2008]: https://doi.org/10.2514/6.2008-319
[research_segel_1952]: https://doi.org/10.21236/ada076043
[research_seginer_rose_1976]: https://doi.org/10.2514/6.1976-330
[research_segui_gabor_2017]: https://doi.org/10.2316/p.2017.848-048
[research_seidel_sandford_1985]: https://doi.org/10.2514/6.1985-598
[research_seiler_balas_2012]: https://doi.org/10.1007/978-1-4614-1833-7_19
[research_sekhar_suresh_2024]: https://doi.org/10.1051/matecconf/202439201016
[research_seki_tani_2019]: https://doi.org/10.2514/6.2019-1105
[research_selvadurai_1984]: https://doi.org/10.1520/stp36812s
[research_selvam_qu_2001]: https://doi.org/10.21236/ada399278
[research_semionov_kosinov_2007]: https://doi.org/10.1134/s0869864307030031
[research_sendner_stahl_2018]: https://doi.org/10.2514/6.2018-3194
[research_serpieri_kotsonis_2015]: https://doi.org/10.2514/6.2015-2576
[research_setoodeh_abdallah_2005]: https://doi.org/10.2514/6.2005-2083
[research_sezgin_krstic_2013]: https://doi.org/10.1109/cdc.2013.6760342
[research_sha_sun_2022]: https://doi.org/10.34759/vst-2022-4-22-35
[research_shankar_goebel_1985]: https://doi.org/10.2514/6.1985-428
[research_shankar_malmuth_1982]: https://doi.org/10.21236/ada121662
[research_shao_guo_2024]: https://doi.org/10.2139/ssrn.5041226
[research_sharifi_vincenti_2025]: https://doi.org/10.1016/j.compstruct.2025.118839
[research_sharma_agrawal_2022]: https://doi.org/10.1109/icc56513.2022.10093649
[research_sharpe_ulker_2023]: https://doi.org/10.2514/6.2023-3951
[research_sharqi_cesnik_2021]: https://doi.org/10.2514/6.2021-0905
[research_shavezipur_2021]: https://doi.org/10.32920/ryerson.14651571
[research_shaw_hidalgo]: https://doi.org/10.1109/aero.2006.1656021
[research_shearwood_nabawy_2020]: https://doi.org/10.3390/aerospace7100150
[research_shearwood_nabawy_2020_b]: https://doi.org/10.2514/6.2020-2677
[research_shearwood_nabawy_2023]: https://doi.org/10.1109/access.2023.3286848
[research_sheldon_rasmussen]: https://doi.org/10.1109/naecon.1994.332847
[research_shen_branscomb_2019]: https://doi.org/10.1177/1528083719881818
[research_shen_li_2024]: https://doi.org/10.3390/app14031304
[research_sheta_2000]: https://doi.org/10.2514/6.2000-4227
[research_shevare_arya_2012]: https://doi.org/10.2514/6.2012-2596
[research_shi_song_2012]: https://doi.org/10.1109/wcica.2012.6358104
[research_shi_wang_2023]: https://doi.org/10.1088/1742-6596/2658/1/012023
[research_shi_zuo_2023]: https://doi.org/10.1016/j.asr.2023.06.009
[research_shieh_1988]: https://doi.org/10.2514/6.1988-3614
[research_shimin_letian_2025]: https://doi.org/10.1007/978-981-96-2252-8_15
[research_shipley_gopalarathnam_2006]: https://doi.org/10.2514/6.2006-451
[research_shirk_hertz_1984]: https://doi.org/10.2514/6.1984-982
[research_shirkmh_hertztj_1986]: https://ntrs.nasa.gov/citations/19860035417
[research_shklovskii_kurt_1961]: https://doi.org/10.1007/978-1-4899-5929-4_8
[research_shmelv_vladov_2019]: https://doi.org/10.30929/1995-0519.2019.1.27-32
[research_shmilovich_yadlin_2023]: https://doi.org/10.2514/6.2023-0655
[research_shmilovich_yadlin_2026]: https://doi.org/10.2514/1.c037586
[research_shubin_1995]: https://doi.org/10.1006/jcph.1995.1080
[research_shukla_patil_2015]: https://doi.org/10.2514/6.2015-2245
[research_shuyi_xin_2010]: https://doi.org/10.1109/icie.2010.237
[research_shweyk_weltz_2005]: https://doi.org/10.2514/6.2005-5812
[research_siebert_strothteicher_2026]: https://doi.org/10.2139/ssrn.6498098
[research_sieradzki_2016]: https://doi.org/10.5604/05096669.1226890
[research_sigrest_wu_2022]: https://doi.org/10.1115/smasis2022-89275
[research_siler_volk_1997]: https://doi.org/10.2514/6.1997-1165
[research_silva]: https://doi.org/10.14393/ufu.te.2022.345
[research_silva_b]: https://doi.org/10.11606/003273318
[research_silva_bennett_1995]: https://doi.org/10.2514/3.46678
[research_silva_mello_2006]: https://doi.org/10.2514/1.16886
[research_silva_mello_2008]: https://doi.org/10.2514/1.33406
[research_silvestre_2013]: https://doi.org/10.1007/978-3-642-38253-6_37
[research_simbuerger_raveh_2022]: https://doi.org/10.2514/1.c036626
[research_simmons_chang_2026]: https://doi.org/10.2514/1.c038907
[research_simmons_murphy_2021]: https://doi.org/10.2514/6.2021-1298
[research_simmons_riso_2025]: https://doi.org/10.4050/f-0081-2025-0208
[research_simoes_alazard_2009]: https://doi.org/10.1109/cdc.2009.5400576
[research_simoes_apkarian_2011]: https://doi.org/10.1016/j.ast.2010.08.004
[research_simpson_1972]: https://doi.org/10.2514/6.1972-785
[research_sims_carter_1981]: https://doi.org/10.2514/6.1981-2387
[research_simsek_tekinalp_2015]: https://doi.org/10.2514/6.2015-1480
[research_simulation_in_1988]: https://doi.org/10.2514/6.1988-2130
[research_sinclair_flowers_2010]: https://doi.org/10.2514/6.2010-7725
[research_singer_1956]: https://doi.org/10.1016/0083-6656(56)90015-0
[research_singh_brenner_2003]: https://doi.org/10.2514/6.2003-5501
[research_singh_brown_2015]: https://doi.org/10.2514/6.2015-1420
[research_singh_brown_2016]: https://doi.org/10.2514/1.c033658
[research_singh_friedmann_2020]: https://doi.org/10.4050/f-0076-2020-16434
[research_singh_friedmann_2021]: https://doi.org/10.2514/1.c036291
[research_singh_kumari_2024]: https://doi.org/10.1063/5.0185035
[research_singh_mcdonough_2010]: https://doi.org/10.1115/imece2010-38877
[research_singh_mcdonough_2014]: https://doi.org/10.2514/1.c032183
[research_singh_venkatraman_2023]: https://doi.org/10.2514/6.2023-1566
[research_singh_wang_2002]: https://doi.org/10.2514/6.2002-4442
[research_singha_2025]: https://doi.org/10.52843/cassyni.rwpkvl
[research_singha_murugan_2023]: https://doi.org/10.2514/6.2023-3753
[research_sinha_ananthkrishnan_2002]: https://doi.org/10.2514/2.3014
[research_sinske_govers_2018]: https://doi.org/10.1007/s13272-018-0294-3
[research_sivanandi_gupta_2022]: https://doi.org/10.21203/rs.3.rs-2263166/v1
[research_sivanandi_gupta_2024]: https://doi.org/10.4273/ijvss.16.6.27
[research_skillen_crossley_2005]: https://doi.org/10.2514/6.2005-1960
[research_skinner_zarebehtash_2018]: https://doi.org/10.1016/j.jfluidstructs.2017.12.018
[research_slaby_smith_2011]: https://doi.org/10.2514/6.2011-2171
[research_slater_1985]: https://doi.org/10.2514/6.1985-1965
[research_slender_aircraft_2012]: https://doi.org/10.2514/5.9781600869228.0439.0447
[research_smith_2025]: https://doi.org/10.33548/scientia1180
[research_smith_dahlem_1981]: https://doi.org/10.2514/6.1981-1659
[research_smith_moes_2003]: https://doi.org/10.2514/6.2003-5701
[research_smith_patil_2001]: https://doi.org/10.2514/6.2001-1582
[research_smith_shyy_1995]: https://doi.org/10.1115/imece1995-1328
[research_smithbenjamin_brookstimothy_2020]: https://ntrs.nasa.gov/citations/20200001139
[research_smithjohnw_lockwiltonp_1992]: https://ntrs.nasa.gov/citations/19920012951
[research_sneshko_chetvergov_2005]: https://doi.org/10.2514/1.3334
[research_soares_2007]: https://doi.org/10.2514/6.2007-2943
[research_soares_2007_b]: https://doi.org/10.2514/6.2007-2942
[research_sobester_2021]: https://doi.org/10.2514/1.c036180
[research_socha_izydorczyk_2024]: https://doi.org/10.3390/s24154845
[research_sodja_werter_2018]: https://doi.org/10.2514/6.2018-2153
[research_sodja_werter_2021]: https://doi.org/10.2514/1.c035955
[research_sohn_chung_2006]: https://doi.org/10.5139/ijass.2006.7.2.128
[research_sohn_chung_2007]: https://doi.org/10.2514/6.2007-4280
[research_soinne_1999]: https://doi.org/10.2514/6.1999-3147
[research_solano_sarojini_2020]: https://doi.org/10.2514/6.2020-0274.c1
[research_solartepineda_bravomosquera_2026]: https://doi.org/10.2514/1.c038573
[research_soneda_tsushima_2026]: https://doi.org/10.2514/1.j065576
[research_soneda_yokozeki_2020]: https://doi.org/10.2514/6.2020-0450
[research_song_kim_2009]: https://doi.org/10.5139/jksas.2009.37.12.1192
[research_song_librescu_1992]: https://doi.org/10.2514/3.11633
[research_song_liu_2014]: https://doi.org/10.1109/chicc.2014.6896454
[research_song_whidborne_2018]: https://doi.org/10.1109/control.2018.8516783
[research_song_wu_2010]: https://doi.org/10.1109/isscaa.2010.5633472
[research_song_yang_2014]: https://doi.org/10.1016/j.cja.2014.08.003
[research_song_zhang_2025]: https://doi.org/10.1142/s0219455426502111
[research_soovere_1981]: https://doi.org/10.2514/6.1981-634
[research_sorensen_bencze_1974]: https://doi.org/10.2514/3.59241
[research_sorensen_smeltzer_1972]: https://doi.org/10.2514/3.59067
[research_sotoudeh_2014]: https://doi.org/10.1115/imece2014-36967
[research_sotoudeh_2015]: https://doi.org/10.2514/6.2015-1182
[research_sotoudeh_ferman_2019]: https://doi.org/10.2514/6.2019-0762
[research_sotoudeh_hodges_2010]: https://doi.org/10.2514/1.46974
[research_sotoudeh_hosking_2018]: https://doi.org/10.2514/6.2018-1203
[research_soykasap_hodges_1999]: https://doi.org/10.2514/6.1999-1475
[research_soykasap_hodges_2000]: https://doi.org/10.2514/2.2680
[research_space_environment]: https://doi.org/10.3403/30237419
[research_spada_afonso_2017]: https://doi.org/10.1016/j.ast.2017.01.010
[research_spaid_1984]: https://doi.org/10.2514/6.1984-100
[research_span_effect_divergence]: https://ntrs.nasa.gov/citations/19930084742
[research_spanglerjr_jacques_1999]: https://doi.org/10.2514/6.1999-1316
[research_spearman_1979]: https://doi.org/10.2514/6.1979-1815
[research_spearman_tice_1992]: https://doi.org/10.2514/6.1992-4246
[research_spinner_rudnik_2023]: https://doi.org/10.2514/6.2023-0810
[research_squires_2004]: https://doi.org/10.21236/ada427305
[research_sreenivasulu_neelapu_2025]: https://doi.org/10.61653/joast.v77i3.2025.1088
[research_srinathkumar_adamsjr_1989]: https://doi.org/10.2514/6.1989-3610
[research_srinivas_chopra_1998]: https://doi.org/10.2514/2.2296
[research_srivathsan_rauleder_2023]: https://doi.org/10.2514/6.2023-1752
[research_stacey_thomas_2019]: https://doi.org/10.1115/smasis2019-5567
[research_staley_1976]: https://doi.org/10.21236/ada021176
[research_stalford_1980]: https://doi.org/10.2514/6.1980-172
[research_stalford_1981]: https://doi.org/10.2514/3.57565
[research_stalla_kier_2024]: https://doi.org/10.2514/6.2024-1442
[research_stalla_looye_2026]: https://doi.org/10.2514/6.2026-1557
[research_stam_devisser_2025]: https://doi.org/10.2514/6.2025-0082
[research_stamatellou_kalfas_2021]: https://doi.org/10.3390/mi12080962
[research_standard_atmosphere]: https://doi.org/10.1007/springerreference_29038
[research_standard_atmosphere_1927]: https://doi.org/10.6028/nbs.mp.78
[research_standard_atmosphere_1927_b]: https://doi.org/10.6028/nbs.mp.82
[research_standard_atmosphere_1992]: https://doi.org/10.1016/b978-0-12-354355-4.50022-x
[research_standard_atmosphere_2005]: https://doi.org/10.1017/cbo9780511807138.014
[research_standard_atmosphere_2007]: https://doi.org/10.1007/978-0-387-30160-0_10930
[research_standard_atmosphere_2021]: https://doi.org/10.5040/9781501365072.15547
[research_standard_atmosphere_2021_b]: https://doi.org/10.5040/9781501365072.15548
[research_standard_atmosphere_2023]: https://doi.org/10.1017/9781009043076.015
[research_standard_atmosphere_2024]: https://doi.org/10.2514/5.9781624107290.1007.1012
[research_standard_atmospheric_2002]: https://doi.org/10.1016/s0074-6142(02)80030-4
[research_stanewsky_basler_1989]: https://doi.org/10.1007/978-3-642-83584-1_38
[research_stanford_2014]: https://doi.org/10.2514/6.2014-2596
[research_stanford_2015]: https://doi.org/10.2514/6.2015-2419
[research_stanford_2016]: https://doi.org/10.2514/6.2016-1097
[research_stanford_2016_b]: https://doi.org/10.2514/1.c033613
[research_stanford_2018]: https://doi.org/10.2514/1.c034653
[research_stanford_2019]: https://doi.org/10.2514/1.g004373
[research_stanford_2020]: https://doi.org/10.2514/6.2020-0448
[research_stanford_2021]: https://doi.org/10.2514/1.c036315
[research_stanford_beran_2011]: https://doi.org/10.2514/1.c031185
[research_stanford_dunning_2015]: https://doi.org/10.2514/1.c032913
[research_stanford_jacobson_2023]: https://doi.org/10.2514/6.2023-0589
[research_stanfordbretk_juttechristinev_2014]: https://ntrs.nasa.gov/citations/20140012777
[research_stange_1959]: https://doi.org/10.21236/ada955359
[research_starodub_2026]: https://doi.org/10.32620/aktt.2026.1.02
[research_starr_olds_2011]: https://doi.org/10.2514/6.2011-6465
[research_static_aeroelastic_1996]: https://doi.org/10.2514/5.9781600862465.0223.0231
[research_static_aeroelasticity_2002]: https://doi.org/10.1017/cbo9780511809170.004
[research_static_aeroelasticity_2005]: https://doi.org/10.1007/1-4020-2106-2_2
[research_static_aeroelasticity_2011]: https://doi.org/10.1017/cbo9780511997112.006
[research_static_aeroelasticity_2014]: https://doi.org/10.1002/9781118700440.ch8
[research_static_aeroelasticity_2014_b]: https://doi.org/10.1002/9781118700440.ch7
[research_static_aeroelasticity_2014_c]: https://doi.org/10.1002/9781118700440.ch22
[research_static_longitudinal_2003]: https://doi.org/10.2514/5.9781600861840.0223.0233
[research_steer_2003]: https://doi.org/10.2514/6.2003-5308
[research_steer_2004]: https://doi.org/10.1017/s000192400000018x
[research_stefanescu_2020]: https://doi.org/10.1007/978-3-030-35322-3_7
[research_steger_bailey_1979]: https://doi.org/10.2514/6.1979-134
[research_steger_bailey_1980]: https://doi.org/10.2514/3.50756
[research_steimle_schroder_2008]: https://doi.org/10.2514/6.2008-6908
[research_stengel_1969]: https://doi.org/10.2514/6.1969-813
[research_stengel_1983]: https://doi.org/10.2514/6.1983-2099
[research_stepanova_2025]: https://doi.org/10.7868/s3034498025070017
[research_stephan_2025]: https://doi.org/10.1007/978-3-031-78487-3_4
[research_stettner_2000]: https://doi.org/10.2514/6.2000-4701
[research_stettner_schrage_1992]: https://doi.org/10.2514/6.1992-4781
[research_stevenson_1991]: https://doi.org/10.2514/6.1991-2878
[research_stewart_bauer_1983]: https://doi.org/10.2514/6.1983-2712
[research_stiharualexe_1991]: https://doi.org/10.23919/acc.1991.4791848
[research_stiharualexe_oshea]: https://doi.org/10.1109/acc.1994.751829
[research_stodieck_cooper_2013]: https://doi.org/10.1016/j.compstruct.2013.07.023
[research_stodieck_cooper_2014]: https://doi.org/10.2514/6.2014-0343
[research_stodieck_cooper_2015]: https://doi.org/10.2514/1.j053599
[research_stodieck_cooper_2017]: https://doi.org/10.2514/1.j055364
[research_stougie_pollack_2024]: https://doi.org/10.2514/6.2024-2565
[research_strain_gage_calibration]: https://ntrs.nasa.gov/citations/20020063604
[research_strain_gauge_1965]: https://doi.org/10.1111/j.1475-1305.1965.tb00040.x
[research_strain_gauge_1967]: https://doi.org/10.1111/j.1475-1305.1967.tb00905.x
[research_strain_gauge_1975]: https://doi.org/10.1111/j.1475-1305.1975.tb00152.x
[research_strand_ennis_2012]: https://doi.org/10.1109/aero.2012.6187310
[research_strand_levinsky_1969]: https://doi.org/10.21236/ad0698355
[research_strang_1943]: https://doi.org/10.1108/eb030987
[research_streett_1981]: https://doi.org/10.2514/6.1981-1266
[research_streitenberger_feldwisch_2025]: https://doi.org/10.2514/6.2025-1663
[research_strelkov_kharlamov_1967]: https://doi.org/10.1007/bf01040744
[research_strganac_2007]: https://doi.org/10.21236/ada475354
[research_striz_eastep_1991]: https://doi.org/10.2514/6.1991-1100
[research_strothteicher_fezans_2026]: https://doi.org/10.2514/1.g009267
[research_structural_weight_1981]: https://doi.org/10.2514/6.1981-366
[research_su_2015]: https://doi.org/10.2514/6.2015-2057
[research_su_cesnik_2009]: https://doi.org/10.2514/6.2009-2402
[research_su_cesnik_2010]: https://doi.org/10.2514/1.47317
[research_su_huang_2017]: https://doi.org/10.2514/6.2017-1353
[research_su_sun_2023]: https://doi.org/10.1016/j.ymssp.2023.110776
[research_su_wang_2018]: https://doi.org/10.1145/3208833.3208850
[research_subramanya_prasad_2013]: https://doi.org/10.1049/cp.2013.2516
[research_sudhi_radespiel_2021]: https://doi.org/10.2514/6.2021-2606
[research_suhpeterm_conyershowardjason_2015]: https://ntrs.nasa.gov/citations/20150020901
[research_sulaeman_abdullah_2017]: https://doi.org/10.1088/1757-899x/184/1/012010
[research_suleman_2007]: https://doi.org/10.21236/ada525877
[research_suleman_afonso_2016]: https://doi.org/10.2514/6.2016-0778
[research_suleman_costa_2004]: https://doi.org/10.1016/j.compstruc.2004.03.027
[research_suleman_crawford_2000]: https://doi.org/10.1115/imece2000-1711
[research_suleman_crawford_2002]: https://doi.org/10.1177/104538902761402477
[research_suleman_moniz]: https://doi.org/10.1007/978-1-4020-4979-8_5
[research_sun_2024]: https://doi.org/10.1088/1742-6596/2882/1/012087
[research_sun_bai_2014]: https://doi.org/10.4028/www.scientific.net/amr.898.688
[research_sun_hu_2005]: https://doi.org/10.1515/ijnsns.2005.6.1.25
[research_sun_schilder_2018]: https://doi.org/10.2514/6.2018-0523
[research_sun_shi_2020]: https://doi.org/10.1016/j.ast.2020.106126
[research_sun_zhou_2021]: https://doi.org/10.1016/j.ast.2021.106638
[research_sundaram_wu_1983]: https://doi.org/10.2514/6.1983-1852
[research_sungpilyang_hashemi_2016]: https://doi.org/10.1109/acc.2016.7525000
[research_supersonic_aileron_reversal]: https://ntrs.nasa.gov/citations/19930083701
[research_supersonic_aircraft_1997]: https://doi.org/10.2514/5.9781600866449.0173.0210
[research_supersonic_three_dimensional_1960]: https://doi.org/10.1515/9781400877706-009
[research_supersonic_transport_1992]: https://doi.org/10.2514/6.1992-2372
[research_suresh_radhakrishnan_2010]: https://doi.org/10.1504/ijde.2010.034864
[research_suryakumar_mangalam_2016]: https://doi.org/10.2514/6.2016-3101
[research_suzuki_1990]: https://doi.org/10.2514/6.1990-3325
[research_suzuki_matsuda_1991]: https://doi.org/10.2514/3.20782
[research_suzuki_yonezawa_1993]: https://doi.org/10.2514/3.48276
[research_svec_1981]: https://doi.org/10.2514/6.1981-2498
[research_svendsen_1994]: https://doi.org/10.2514/6.1994-2160
[research_svoboda_hengstermovric_2023]: https://doi.org/10.1016/j.ast.2023.108415
[research_svoboda_hromcik_2018]: https://doi.org/10.1109/med.2018.8442815
[research_svoboda_hromcik_2019]: https://doi.org/10.23919/ecc.2019.8795733
[research_svoboda_hromcik_2021]: https://doi.org/10.1109/pc52310.2021.9447451
[research_swaim]: https://doi.org/10.1109/naecon.1988.195064
[research_swaim_1961]: https://doi.org/10.2514/8.9241
[research_swaim_1983]: https://doi.org/10.2514/6.1983-2219
[research_swiech_2020]: https://doi.org/10.3390/aerospace7030027
[research_switala_lipski_2026]: https://doi.org/10.1063/5.0302401
[research_syed_moshtaghzadeh_2022]: https://doi.org/10.2514/6.2022-2557
[research_sykes]: https://doi.org/10.33915/etd.612
[research_szabolcsi_gaspar_1997]: https://doi.org/10.1016/s1474-6670(17)42641-3
[research_szema_shankar_1984]: https://doi.org/10.2514/6.1984-427
[research_szollosi_baranyi_2016]: https://doi.org/10.1002/asjc.1418
[research_szymanski_alstrom_2025]: https://doi.org/10.2514/1.c037978
[research_szymanski_ghazi_2025]: https://doi.org/10.2514/6.2025-2228
[research_tabassum_bai_2022]: https://doi.org/10.1016/j.ast.2021.107323
[research_tacca_colvin_2024]: https://doi.org/10.3389/fresc.2024.1290092
[research_tadi_2003]: https://doi.org/10.2514/2.6918
[research_taflan_smith_2023]: https://doi.org/10.2514/6.2023-1554
[research_taflan_smith_2023_b]: https://doi.org/10.2514/6.2023-1554.c1
[research_taha_tang_2011]: https://doi.org/10.1016/j.mechatronics.2010.09.008
[research_tai_wang_2023]: https://doi.org/10.2514/1.j062188
[research_tai_wang_2023_b]: https://doi.org/10.3390/aerospace10040350
[research_takahashi_yokozeki_2016]: https://doi.org/10.1177/1045389x16642298
[research_takarics_vanek_2018]: https://doi.org/10.1109/aero.2018.8396537
[research_tal_nguyen_2015]: https://doi.org/10.2514/6.2015-2722
[research_tamayama_2017]: https://doi.org/10.1063/1.4972751
[research_tamayama_kheirandish_2003]: https://doi.org/10.2322/tjsass.46.186
[research_tamura_yumitori_2024]: https://doi.org/10.2514/6.2024-2446
[research_tang_chen_2017]: https://doi.org/10.1109/med.2017.7984127
[research_tang_dowell_1996]: https://doi.org/10.2514/3.47059
[research_tang_dowell_1998]: https://doi.org/10.2514/2.2377
[research_tang_dowell_2001]: https://doi.org/10.2514/2.1484
[research_tang_dowell_2013]: https://doi.org/10.2514/1.j052495
[research_tang_kholodar_2000]: https://doi.org/10.2514/6.2000-1621
[research_tang_wu_2015]: https://doi.org/10.2514/6.2015-0664
[research_tang_wu_2016]: https://doi.org/10.1016/j.cja.2015.12.001
[research_tang_yang_2025]: https://doi.org/10.1109/cac67268.2025.11487048
[research_tani_1992]: https://doi.org/10.1117/12.2298093
[research_tani_seki_2018]: https://doi.org/10.2514/6.2018-1794
[research_tantaroudas_daronch_2017]: https://doi.org/10.1002/9781118928691.ch4
[research_tantaroudas_karachalios_2026]: https://doi.org/10.24132/acm.2026.1114
[research_tantrairatn_veres_2015]: https://doi.org/10.1016/j.ifacol.2015.09.485
[research_tao_bin_2026]: https://doi.org/10.3390/biomimetics11010036
[research_taraborrelli_2023]: https://doi.org/10.21741/9781644902813-92
[research_taranto_abdulrahim_2023]: https://doi.org/10.2514/6.2023-71776
[research_tariq_nahon_2020]: https://doi.org/10.1109/icuas48674.2020.9213869
[research_tartabini_gilbert_2016]: https://doi.org/10.2514/6.2016-0783
[research_taylor_1959]: https://doi.org/10.1017/s0001924000092502
[research_taylor_2012]: https://doi.org/10.2514/6.2012-4410
[research_taylor_bennett_1992]: https://doi.org/10.2514/6.1992-170
[research_taylor_gaitonde_2007]: https://doi.org/10.2514/1.22959
[research_taylor_pratt_1995]: https://doi.org/10.2514/6.1995-3180
[research_taylor_yoo_2011]: https://doi.org/10.2514/6.2011-6253
[research_technical_applications_1976]: https://doi.org/10.2514/6.1976-892
[research_tegelaar_1984]: https://doi.org/10.2118/12420-ms
[research_teixeira_cesnik_2020]: https://doi.org/10.1017/aer.2019.165
[research_tekawade_chandwadkar_2024]: https://doi.org/10.61653/joast.v76i3.2024.979
[research_teng_2006]: https://doi.org/10.2514/6.2006-6317
[research_teng_2007]: https://doi.org/10.4271/2007-01-3921
[research_teng_chen_2006]: https://doi.org/10.2514/6.2006-443
[research_teng_fan_2025]: https://doi.org/10.1007/978-981-96-2440-9_40
[research_terilli_bueno_2025]: https://doi.org/10.26678/abcm.cobem2025.cob2025-1817
[research_tewari_1998]: https://doi.org/10.2514/6.1998-4142
[research_tewari_1999]: https://doi.org/10.2514/6.1999-4312
[research_tewari_2001]: https://doi.org/10.2514/2.4727
[research_tewari_2009]: https://doi.org/10.2514/1.44049
[research_tewari_2015]: https://doi.org/10.1007/978-1-4939-2368-7_5
[research_tewari_2015_b]: https://doi.org/10.1007/978-1-4939-2368-7_4
[research_tewari_2015_c]: https://doi.org/10.1007/978-1-4939-2368-7_6
[research_tewari_2016]: https://doi.org/10.1002/9781118823491
[research_thapamagar_pankonien_2018]: https://doi.org/10.2514/6.2018-0850
[research_tharayil_alleyne_2001]: https://doi.org/10.1115/imece2001/ad-23740
[research_tharayil_alleyne_2004]: https://doi.org/10.1109/tmech.2004.823852
[research_the_effect_1969]: https://doi.org/10.1016/s0041-2678(69)80276-9
[research_the_effects_2007]: https://doi.org/10.5139/jksas.2007.35.10.899
[research_the_flight_2021]: https://doi.org/10.1002/9781118949818.ch2
[research_the_geometry_2016]: https://doi.org/10.1002/9781118827789.ch5
[research_the_international_2017]: https://doi.org/10.1016/b978-0-08-100194-3.00017-1
[research_the_international_2026]: https://doi.org/10.1016/b978-0-32-399544-3.00016-5
[research_the_saunders_roe_1952]: https://doi.org/10.1108/eb032229
[research_the_standard_1964]: https://doi.org/10.1016/b978-0-12-634450-9.50033-6
[research_the_standard_1976]: https://doi.org/10.1016/b978-0-08-020414-7.50016-2
[research_theis_pfifer_2015]: https://doi.org/10.1109/acc.2015.7171927
[research_theis_pfifer_2016]: https://doi.org/10.2514/6.2016-1751
[research_theis_pfifer_2020]: https://doi.org/10.2514/1.g004846
[research_theis_takarics_2015]: https://doi.org/10.2514/6.2015-1686
[research_thel_hahn_2022]: https://doi.org/10.1007/s00158-022-03248-3
[research_thielicke_stamhuis_2018]: https://doi.org/10.1088/1748-3190/aad5a3
[research_thienel_lewis_1998]: https://doi.org/10.21236/ada373637
[research_thomas_holst_1983]: https://doi.org/10.2514/6.1983-499
[research_thomas_shkarayev_2026]: https://doi.org/10.2514/6.2026-4006
[research_thompson_danowsky_2011]: https://doi.org/10.2514/6.2011-6209
[research_thompson_klyde_2007]: https://doi.org/10.2514/6.2007-6716
[research_thomson_1946]: https://doi.org/10.2514/8.11345
[research_three_dimensional_boundary_layer_1994]: https://doi.org/10.2514/6.1994-2375
[research_thuwis_debreuker]: https://doi.org/10.4203/ccp.89.112
[research_thuwis_debreuker_2009]: https://doi.org/10.1007/s00158-009-0437-6
[research_tian_li_2026]: https://doi.org/10.1016/j.jsv.2026.119977
[research_tian_wang_2026]: https://doi.org/10.1016/j.compstruct.2026.120104
[research_tian_yang_2016]: https://doi.org/10.1061/(asce)as.1943-5525.0000652
[research_tijdeman_vannunen_1979]: https://doi.org/10.21236/ada071420
[research_tijdeman_vannunen_1979_b]: https://doi.org/10.21236/ada077370
[research_tillotson_fuhs_1982]: https://doi.org/10.2514/6.1982-1361
[research_ting_berg_2026]: https://doi.org/10.2514/6.2026-1058
[research_ting_chaparro_2017]: https://doi.org/10.2514/6.2017-1815
[research_ting_lebofsky_2014]: https://doi.org/10.2514/6.2014-0838
[research_ting_mesbahi_2022]: https://doi.org/10.2514/6.2022-2489
[research_ting_mesbahi_2023]: https://doi.org/10.2514/1.g007450
[research_tingting_aijun_2014]: https://doi.org/10.1109/icarcv.2014.7064295
[research_tiomkin_raveh_2021]: https://doi.org/10.1016/j.paerosci.2021.100738
[research_tirman_ture_2024]: https://doi.org/10.4050/f-0080-2024-1231
[research_tischler_2018]: https://doi.org/10.1201/9781315136820-2
[research_tischler_hoh_1982]: https://doi.org/10.2514/6.1982-1292
[research_tischler_venkayya_1998]: https://doi.org/10.2514/6.1998-4778
[research_tischler_venkayya_2000]: https://doi.org/10.2514/6.2000-1326
[research_tischler_zivan_2007]: https://doi.org/10.4050/vfs-f63-000051
[research_toffol_2023]: https://doi.org/10.21741/9781644902813-10
[research_toffol_2024]: https://doi.org/10.3390/app14219883
[research_toffol_ricci_2023]: https://doi.org/10.3390/aerospace10080693
[research_tohidi_yildiz_2018]: https://doi.org/10.1109/ccta.2018.8511389
[research_toker_ozbay]: https://doi.org/10.1109/acc.1995.529233
[research_tol_devisser_2014]: https://doi.org/10.2514/1.g000065
[research_tomainerl_bryantwh_1978]: https://ntrs.nasa.gov/citations/19780061530
[research_torenbeek_1972]: https://doi.org/10.1108/eb034867
[research_torok_1996]: https://doi.org/10.4050/vfs-f52-1022
[research_torralba_puyou_2009]: https://doi.org/10.2514/6.2009-6303
[research_torrigiani_berci_2021]: https://doi.org/10.2514/6.2021-1911
[research_torsional_divergence_2014]: https://doi.org/10.1007/978-94-007-2739-7_100771
[research_torsional_stiffness_1972]: https://doi.org/10.1016/0010-4361(72)90404-1
[research_torsional_stiffness_1994]: https://doi.org/10.1016/0026-2714(94)90317-4
[research_traas_atmaca_2026]: https://doi.org/10.2514/6.2026-0549
[research_tracy_1981]: https://doi.org/10.2514/6.1981-2464
[research_tracy_chopra_1998]: https://doi.org/10.2514/2.2371
[research_trame_williams_1985]: https://doi.org/10.2514/6.1985-1858
[research_trankle_bachner_1993]: https://doi.org/10.2514/6.1993-3634
[research_transonic_aircraft_2012]: https://doi.org/10.2514/5.9781600869174.0171.0220
[research_transonic_and_1992]: https://doi.org/10.1017/cbo9780511607134.012
[research_transonic_maneuver_cruise_1980]: https://doi.org/10.2514/5.9781600865466.0187.0211
[research_transonic_shock_1982]: https://doi.org/10.1016/c2013-0-11177-4
[research_transonic_wing_2015]: https://doi.org/10.1142/9781783266296_0011
[research_travassos_kaufman_1979]: https://doi.org/10.2514/6.1979-1636
[research_trenka_1971]: https://doi.org/10.21236/ad0727653
[research_triplett_1972]: https://doi.org/10.2514/3.59009
[research_triplett_1979]: https://doi.org/10.2514/6.1979-725
[research_triplett_1980]: https://doi.org/10.2514/6.1980-794
[research_triplett_1980_b]: https://doi.org/10.2514/3.57932
[research_triplett_ising_1971]: https://doi.org/10.2514/3.59137
[research_triplett_kappus_1973]: https://doi.org/10.2514/6.1973-194
[research_truong_gosselin_2022]: https://doi.org/10.5703/1288284317481
[research_tsonev_kuzmanov_2022]: https://doi.org/10.1063/5.0091463
[research_tsushima_arizono_2018]: https://doi.org/10.1299/jsmetld.2018.27.1005
[research_tsushima_soneda_2025]: https://doi.org/10.1016/j.ast.2025.110665
[research_tsushima_yokozeki_2018]: https://doi.org/10.12783/asc33/26174
[research_tsushima_yokozeki_2019]: https://doi.org/10.1016/j.ast.2019.03.025
[research_tuckerharvey_khovanov_2020]: https://doi.org/10.1016/j.apenergy.2020.115014
[research_tuckerwarrena_nelsonrobertl_1950]: https://ntrs.nasa.gov/citations/19930092034
[research_tung_yu_1996]: https://doi.org/10.4050/vfs-f52-20144
[research_turi_rankin_1988]: https://doi.org/10.23919/acc.1988.4790101
[research_turner_seo_2025]: https://doi.org/10.2514/6.2025-1494
[research_turns_kraige]: https://doi.org/10.1017/cbo9780511813696.014
[research_tursi_2003]: https://doi.org/10.2514/6.2003-3787
[research_tuzcu_nguyen_2010]: https://doi.org/10.2514/6.2010-7503
[research_uhm_2021]: https://doi.org/10.4271/2021-01-0797
[research_ulbrich_2011]: https://doi.org/10.2514/6.2011-6090
[research_ulbrich_2024]: https://doi.org/10.2514/6.2024-4282
[research_ulker_nitzsche_2012]: https://doi.org/10.4050/vfs-f68-000320
[research_ullah_kamoun_2022]: https://doi.org/10.2514/6.2022-1334
[research_ullah_lutz_2021]: https://doi.org/10.2514/6.2021-1831
[research_ullah_lutz_2023]: https://doi.org/10.2514/1.c037086
[research_unsteady_aerodynamics_2006]: https://doi.org/10.2514/5.9781600862373.0447.0528
[research_upper_atmosphere_1961]: https://doi.org/10.2172/4791901
[research_uppoor_chopra_2026]: https://doi.org/10.4050/f-0082-2026-0261
[research_upv_deodhare_2025]: https://doi.org/10.1115/imece-india2025-161192
[research_urnes_reichenbach_2008]: https://doi.org/10.2514/6.2008-6983
[research_urnesjamessr_nguyennhan_2013]: https://ntrs.nasa.gov/citations/20140006948
[research_us_standard_2014]: https://doi.org/10.1016/b978-0-12-419953-8.00019-x
[research_uzun_malik_2018]: https://doi.org/10.2514/6.2018-3854
[research_uzun_malik_2019]: https://doi.org/10.2514/1.j057850
[research_vadyak_smith_1987]: https://doi.org/10.2514/6.1987-1752
[research_vale_leite_2011]: https://doi.org/10.1177/1045389x11416031
[research_vance_brown_1974]: https://doi.org/10.21236/ad0783390
[research_vandierendonck_1973]: https://doi.org/10.2514/6.1973-159
[research_vangaasbeek_1980]: https://doi.org/10.21236/ada089008
[research_vangraas_diggle_1994]: https://doi.org/10.1002/j.2161-4296.1994.tb02322.x
[research_vanpelt_1981]: https://doi.org/10.2514/6.1981-2375
[research_vanschoor_vonflotow_1990]: https://doi.org/10.2514/3.45955
[research_vanwalleghem_debaere_2015]: https://doi.org/10.1016/j.proeng.2015.07.203
[research_vanwyckhouse_1966]: https://doi.org/10.21236/ad0630927
[research_vanzyl_2001]: https://doi.org/10.2514/2.2806
[research_varello_lamberti_2013]: https://doi.org/10.5139/ijass.2013.14.4.310
[research_variation_of_1956]: https://doi.org/10.1029/tr037i002p00177
[research_vartio_shaw_2008]: https://doi.org/10.2514/6.2008-7192
[research_vartio_shimko_2005]: https://doi.org/10.2514/6.2005-1946
[research_vaughan_2003]: https://doi.org/10.1016/b0-12-227090-8/00379-1
[research_vaughnjr_1982]: https://doi.org/10.2514/6.1982-414
[research_veiberman_karpel_2022]: https://doi.org/10.2514/6.2022-0244
[research_veiberman_weiss_2016]: https://doi.org/10.2514/6.2016-1486
[research_veley_khot_2008]: https://doi.org/10.21236/ada478915
[research_velkova_2017]: https://doi.org/10.19062/1842-9238.2017.15.3.1
[research_vepa_2007]: https://doi.org/10.2514/1.26115
[research_vepa_2007_b]: https://doi.org/10.2514/1.28152
[research_verhaegen_1987]: https://doi.org/10.2514/6.1987-2620
[research_vernon_1993]: https://doi.org/10.2514/6.1993-1537
[research_verri_desilvabussamra_2025]: https://doi.org/10.2514/1.c037829
[research_verri_luizbussamra_2024]: https://doi.org/10.2514/6.2024-2447
[research_verstraete_roccia_2019]: https://doi.org/10.1007/s11071-019-05234-9
[research_verstynenjr_1974]: https://doi.org/10.2514/6.1974-953
[research_vile_alwi_2019]: https://doi.org/10.23919/acc.2019.8814298
[research_vile_alwi_2019_b]: https://doi.org/10.1109/cdc40024.2019.9030030
[research_vile_alwi_2020]: https://doi.org/10.1049/cth2.12042
[research_vincent_botez_2015]: https://doi.org/10.2514/6.2015-0904
[research_vincent_franklin_1981]: https://doi.org/10.2514/6.1981-2449
[research_vindigni_2023]: https://doi.org/10.21741/9781644902677-31
[research_vindigni_2024]: https://doi.org/10.21741/9781644903193-27
[research_vindigni_mantegna_2024]: https://doi.org/10.1016/j.jsv.2023.118151
[research_vindigni_mantegna_2024_b]: https://doi.org/10.1088/1742-6596/2746/1/012007
[research_vindigni_mantegna_2026]: https://doi.org/10.1016/j.ejcon.2026.101632
[research_virgiliopereira_kolmanovsky_2019]: https://doi.org/10.2514/6.2019-1591
[research_virgiliopereira_kolmanovsky_2019_b]: https://doi.org/10.2514/6.2019-1591.c1
[research_volk_siler_1998]: https://doi.org/10.2514/6.1998-1971
[research_volobuyev_gorbushin_2017]: https://doi.org/10.1615/tsagiscij.2017021104
[research_vonflotow_1989]: https://doi.org/10.2514/6.1989-1187
[research_voracek_clarke_1991]: https://doi.org/10.2514/6.1991-1053
[research_voracek_reaves_2002]: https://doi.org/10.2514/6.2002-1349
[research_vos_hodigeresiddaramaiah_2007]: https://doi.org/10.2514/6.2007-1706
[research_voskuijl_walker_2008]: https://doi.org/10.1017/s0001924000002633
[research_vu]: https://doi.org/10.31274/rtd-20200803-400
[research_vu_kelkar_2005]: https://doi.org/10.2514/6.2005-2039
[research_vukasinovic_gissen_2013]: https://doi.org/10.2514/6.2013-529
[research_wada_tamayama_2020]: https://doi.org/10.1088/2631-8695/abbb59
[research_waggoner_1980]: https://doi.org/10.2514/6.1980-129
[research_waggoner_1982]: https://doi.org/10.2514/6.1982-163
[research_wagner_1983]: https://doi.org/10.2514/6.1983-645
[research_wahler_varriale_2023]: https://doi.org/10.2514/6.2023-3485
[research_waite_bartels_2020]: https://doi.org/10.2514/6.2020-2717
[research_waite_grauer_2021]: https://doi.org/10.2514/6.2021-0609
[research_waite_stanford_2019]: https://doi.org/10.2514/6.2019-1022
[research_waite_stanford_2019_b]: https://doi.org/10.2514/6.2019-3025
[research_waitman_marcos_2020]: https://doi.org/10.2514/1.g004618
[research_walendziuk_2018]: https://doi.org/10.3390/s18124200
[research_wales_cheung_2015]: https://doi.org/10.2514/6.2015-1053
[research_walker_aglietti_2007]: https://doi.org/10.1061/(asce)0893-1321(2007)20:2(102)
[research_walker_postlthewaite]: https://doi.org/10.1109/cdc.1991.261254
[research_wall_amoozgar_2024]: https://doi.org/10.1016/j.ast.2024.109684
[research_wallace_1952]: https://doi.org/10.21236/ad0043099
[research_wallace_1978]: https://doi.org/10.2514/6.1978-1462
[research_wallace_2000]: https://doi.org/10.21236/ada382563
[research_wan_yang_2003]: https://doi.org/10.2514/6.2003-1491
[research_wang_2019]: https://doi.org/10.1063/1.5087963
[research_wang_chang_2021]: https://doi.org/10.1108/aeat-01-2021-0022
[research_wang_chen_2023]: https://doi.org/10.1016/j.tws.2023.111266
[research_wang_chen_2025]: https://doi.org/10.2139/ssrn.5529999
[research_wang_chen_2026]: https://doi.org/10.2139/ssrn.6750138
[research_wang_demiroz_1986]: https://doi.org/10.2514/6.1986-9772
[research_wang_guo_2012]: https://doi.org/10.1504/ijmic.2012.046692
[research_wang_hou_2021]: https://doi.org/10.1109/cac53003.2021.9727458
[research_wang_hu_2025]: https://doi.org/10.2139/ssrn.5264811
[research_wang_hu_2026]: https://doi.org/10.1016/j.ast.2025.111272
[research_wang_iliff_2004]: https://doi.org/10.2514/1.332
[research_wang_lei_2023]: https://doi.org/10.3390/vibration6040062
[research_wang_li_2024]: https://doi.org/10.1061/jaeeez.aseng-5657
[research_wang_li_2025]: https://doi.org/10.1016/j.ast.2025.110134
[research_wang_mkhoyan_2021]: https://doi.org/10.2514/1.g005870
[research_wang_mkhoyan_2021_b]: https://doi.org/10.2514/6.2021-0503
[research_wang_pei_2026]: https://doi.org/10.1016/j.measurement.2026.121991
[research_wang_pei_2026_b]: https://doi.org/10.1088/1361-6501/ae4ac2
[research_wang_tai_2022]: https://doi.org/10.3390/aerospace9110689
[research_wang_tang_2019]: https://doi.org/10.23919/chicc.2019.8865402
[research_wang_vankampen_2018]: https://doi.org/10.2514/6.2018-0774
[research_wang_vankampen_2019]: https://doi.org/10.2514/1.g003980
[research_wang_wan_2019]: https://doi.org/10.2514/6.2019-0419
[research_wang_wan_2019_b]: https://doi.org/10.2514/6.2019-0419.c1
[research_wang_wan_2021]: https://doi.org/10.1016/j.compstruct.2020.113201
[research_wang_wang_2024]: https://doi.org/10.2139/ssrn.4984796
[research_wang_wu_2021]: https://doi.org/10.1016/j.jfluidstructs.2021.103286
[research_wang_wynn_2018]: https://doi.org/10.2514/1.c034684
[research_wang_xargay_2012]: https://doi.org/10.2514/6.2012-4894
[research_wang_xing_2023]: https://doi.org/10.1109/cac59555.2023.10451081
[research_wang_xu_2025]: https://doi.org/10.3390/machines13050428
[research_wang_yang_2019]: https://doi.org/10.2514/6.2019-1021
[research_wang_yu_2025]: https://doi.org/10.1016/j.cja.2025.103603
[research_wang_zhang_2018]: https://doi.org/10.1109/icarcv.2018.8581089
[research_wang_zhao_2022]: https://doi.org/10.3390/aerospace9080433
[research_wang_zhao_2024]: https://doi.org/10.2139/ssrn.5001796
[research_wankim_cho_2008]: https://doi.org/10.1080/10402000802325533
[research_wansasueb_panagant_2023]: https://doi.org/10.1007/s00707-023-03756-3
[research_ward_1949]: https://doi.org/10.1017/s0001925900000056
[research_ward_1988]: https://doi.org/10.2514/6.1988-2116
[research_warwick_bras_2019]: https://doi.org/10.2514/6.2019-1116
[research_wasmi_hasan_2015]: https://doi.org/10.31026/j.eng.2015.12.07
[research_wasson_mehus_1967]: https://doi.org/10.2514/3.43843
[research_waszak_1996]: https://doi.org/10.2514/6.1996-3437
[research_waszak_2001]: https://doi.org/10.2514/2.4694
[research_waszak_buttrill_1991]: https://doi.org/10.2514/6.1991-3111
[research_waszak_davidson_2002]: https://doi.org/10.2514/6.2002-4875
[research_waszak_schmidt_1988]: https://doi.org/10.2514/3.45623
[research_waszak_srinathkumar_1991]: https://doi.org/10.2514/6.1991-2629
[research_waszak_srinathkumar_1992]: https://doi.org/10.2514/6.1992-2097
[research_waszak_srinathkumar_1995]: https://doi.org/10.2514/3.46684
[research_watts_1976]: https://doi.org/10.21236/ada030344
[research_webb_takahashi_2022]: https://doi.org/10.2514/6.2022-3587
[research_weed_carlson_1983]: https://doi.org/10.21236/ada129573
[research_wei_lin_2022]: https://doi.org/10.1108/aeat-12-2021-0364
[research_wei_zhang_2024]: https://doi.org/10.21203/rs.3.rs-4439024/v1
[research_wei_zhao_2018]: https://doi.org/10.1109/control.2018.8516896
[research_weibing_kuisheng_2006]: https://doi.org/10.1163/157361106776240833
[research_weinstein_hubbard_2018]: https://doi.org/10.2514/6.2018-3313
[research_weiss_1983]: https://doi.org/10.2514/6.1983-1091
[research_weiss_thielecke_2000]: https://doi.org/10.2514/6.2000-4098
[research_weisshaar_1973]: https://doi.org/10.2514/6.1973-397
[research_weisshaar_1974]: https://doi.org/10.2514/3.59792
[research_weisshaar_1974_b]: https://doi.org/10.2514/3.60415
[research_weisshaar_1977]: https://doi.org/10.2514/3.44579
[research_weisshaar_1978]: https://doi.org/10.21236/adb032318
[research_weisshaar_1979]: https://doi.org/10.21236/adb042815
[research_weisshaar_1980]: https://doi.org/10.2514/6.1980-795
[research_weisshaar_1981]: https://doi.org/10.2514/3.57542
[research_weisshaar_1985]: https://doi.org/10.2514/3.48607
[research_weisshaar_1987]: https://doi.org/10.2514/6.1987-976
[research_weisshaar_1990]: https://doi.org/10.2514/3.25276
[research_weisshaar_1990_b]: https://doi.org/10.2514/6.1990-1078
[research_weisshaar_1994]: https://doi.org/10.2514/3.46463
[research_weisshaar_1994_b]: https://doi.org/10.1115/imece1994-1444
[research_weisshaar_2010]: https://doi.org/10.1002/9780470686652.eae149
[research_weisshaar_ashley_1974]: https://doi.org/10.2514/3.44409
[research_weisshaar_duke_2006]: https://doi.org/10.2514/1.12040
[research_weisshaar_lee_2002]: https://doi.org/10.2514/6.2002-1207
[research_weisshaar_nam_1990]: https://doi.org/10.2514/3.25358
[research_weisshaar_ryan_1984]: https://doi.org/10.2514/6.1984-985
[research_weisshaarta_1983]: https://ntrs.nasa.gov/citations/19840055636
[research_weisshaarterrencea_changhonam_1989]: https://ntrs.nasa.gov/citations/19890015818
[research_wells_2017]: https://doi.org/10.2514/6.2017-1628
[research_wells_banda_1981]: https://doi.org/10.2514/6.1981-221
[research_wells_banda_1982]: https://doi.org/10.2514/3.57377
[research_wells_keskar_1979]: https://doi.org/10.1016/s1474-6670(17)65522-8
[research_werner_2018]: https://doi.org/10.2514/6.2018-0789
[research_werter_debreuker_2016]: https://doi.org/10.1016/j.compstruct.2016.09.044
[research_wheatcroft_groh_2025]: https://doi.org/10.1017/aer.2025.10113
[research_whitbeck_hofmann_1978]: https://doi.org/10.21236/ada067177
[research_whitbeck_smith_1982]: https://doi.org/10.21236/ada134175
[research_white_1963]: https://doi.org/10.21236/ad0296103
[research_white_1970]: https://doi.org/10.2514/6.1970-877
[research_white_1971]: https://doi.org/10.2514/3.59169
[research_white_1973]: https://doi.org/10.1111/j.1475-1305.1973.tb01830.x
[research_white_hartl_2024]: https://doi.org/10.2139/ssrn.5062463
[research_whitford_1991]: https://doi.org/10.2514/3.46102
[research_wieland_2025]: https://doi.org/10.2514/6.2025-3316
[research_wieseman_hoadley_1995]: https://doi.org/10.2514/3.46681
[research_wieseman_silva_2005]: https://doi.org/10.2514/6.2005-1995
[research_wilcox_brenner_2011]: https://doi.org/10.2514/6.2011-6210
[research_wilde_omenzetter_2001]: https://doi.org/10.1061/(asce)0733-9399(2001)127:1(80)
[research_wildschek_hanis_2013]: https://doi.org/10.1051/eucass/201306707
[research_wildschek_maier_2006]: https://doi.org/10.2514/6.2006-6054
[research_wildschek_maier_2009]: https://doi.org/10.2514/6.2009-6118
[research_williams_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50012-9
[research_williams_2004]: https://doi.org/10.2514/6.2004-6283
[research_williams_hunt_1980]: https://doi.org/10.2514/6.1980-1809
[research_williamshayes_2005]: https://doi.org/10.2514/6.2005-6995
[research_wilson]: https://doi.org/10.15368/theses.2020.2
[research_wilson_riley_1993]: https://doi.org/10.21236/ada273685
[research_wilson_ryan_2016]: https://doi.org/10.1109/maes.2016.150128
[research_wimpress_swihart_1964]: https://doi.org/10.2514/3.43561
[research_wing_buffeting_2018]: https://doi.org/10.15372/pmtf20180406
[research_wing_flexibility_lateral]: https://ntrs.nasa.gov/citations/19930092577
[research_wing_theory_1969]: https://doi.org/10.1016/c2013-0-02078-6
[research_wingroverc_1978]: https://ntrs.nasa.gov/citations/19790066419
[research_winograd_miles_1956]: https://doi.org/10.1017/s0001925900010167
[research_winters_hassan_1991]: https://doi.org/10.1007/978-1-4615-3746-5_32
[research_winther_hagemeyer_1993]: https://doi.org/10.2514/6.1993-3664
[research_wolf_bossert_2001]: https://doi.org/10.2514/6.2001-4313
[research_wolfson_2009]: https://doi.org/10.1016/j.chembiol.2009.09.008
[research_wood_buffano_1964]: https://doi.org/10.21236/ad0607656
[research_wood_loth_1999]: https://doi.org/10.2514/6.1999-614
[research_wood_miller_1985]: https://doi.org/10.2514/3.45141
[research_woodrow_tischler_2013]: https://doi.org/10.2514/6.2013-4739
[research_woodruff_2009]: https://doi.org/10.2514/6.2009-5722
[research_woods_gilbert_1989]: https://doi.org/10.2514/6.1989-1385
[research_woods_gilbert_1990]: https://doi.org/10.2514/3.25336
[research_woodsvedeler_pototzky_1992]: https://doi.org/10.2514/6.1992-2099
[research_woodsvedeler_pototzky_1995]: https://doi.org/10.2514/3.46685
[research_woodsvedelerjessicaa_pototzkyanthonys_1994]: https://ntrs.nasa.gov/citations/19950010982
[research_woodward_1962]: https://doi.org/10.21236/ad0282989
[research_woolf_2012]: https://doi.org/10.2514/6.2012-2723
[research_wright_silva_2026]: https://doi.org/10.4050/sm-2026-vlada-5167
[research_wu_cooper_2016]: https://doi.org/10.2514/6.2016-1227
[research_wu_dai_2022]: https://doi.org/10.2514/1.j061947
[research_wu_li_2024]: https://doi.org/10.1016/j.ast.2024.109693
[research_wu_li_2025]: https://doi.org/10.1016/j.tws.2025.113710
[research_wu_livne_2015]: https://doi.org/10.2514/6.2015-2056
[research_wu_livne_2016]: https://doi.org/10.2514/1.j054824
[research_wu_zhang_2021]: https://doi.org/10.1016/j.ijmecsci.2021.106358
[research_wu_zhou_2024]: https://doi.org/10.1017/aer.2024.43
[research_wuestenhagen_2022]: https://doi.org/10.2514/6.2022-0440
[research_wuestenhagen_2023]: https://doi.org/10.2514/6.2023-0371
[research_wuestenhagen_kier_2018]: https://doi.org/10.2514/6.2018-3150
[research_wuestenhagen_kier_2018_b]: https://doi.org/10.2514/6.2018-3150.c1
[research_wunderlich_2015]: https://doi.org/10.1007/s13272-015-0151-6
[research_wunderlich_dahne_2017]: https://doi.org/10.1007/s13272-017-0251-6
[research_wunderlich_dahne_2017_b]: https://doi.org/10.1007/s13272-017-0266-z
[research_wustenhagen_suelozgen_2021]: https://doi.org/10.1109/aero50100.2021.9438354
[research_wynn_artola_2022]: https://doi.org/10.2514/6.2022-0442
[research_wyrick_1965]: https://doi.org/10.21236/ad0627372
[research_xiang_wang_2023]: https://doi.org/10.1061/jaeeez.aseng-4658
[research_xiao_li_2011]: https://doi.org/10.1111/j.1475-1305.2009.00650.x
[research_xiao_wang_2022]: https://doi.org/10.1117/12.2645493
[research_xiaoguang_du_2023]: https://doi.org/10.1007/978-981-19-6613-2_453
[research_xie_2010]: https://doi.org/10.4236/engineering.2010.29090
[research_xie_leng_2007]: https://doi.org/10.1155/2008/957561
[research_xie_liu_2016]: https://doi.org/10.1155/2016/5090719
[research_xie_yang_2011]: https://doi.org/10.1007/s11431-010-4252-5
[research_xie_yang_2012]: https://doi.org/10.2514/6.2012-1513
[research_xie_zhao_2019]: https://doi.org/10.1109/icusai47366.2019.9124755
[research_xin_li_2025]: https://doi.org/10.1038/s41598-025-08792-8
[research_xing_singh_1999]: https://doi.org/10.2514/6.1999-4283
[research_xiong_fugate_2019]: https://doi.org/10.2514/6.2019-3026
[research_xiong_liu_2013]: https://doi.org/10.2514/6.2013-3205
[research_xiong_nguyen_2021]: https://doi.org/10.2514/6.2021-0336
[research_xiong_nguyen_2023]: https://doi.org/10.2514/6.2023-1575
[research_xiong_nguyen_2024]: https://doi.org/10.2514/6.2024-2668
[research_xiong_nguyen_2024_b]: https://doi.org/10.2514/6.2024-4056
[research_xiong_nguyen_2024_c]: https://doi.org/10.2514/6.2024-2678
[research_xiong_yang_2001]: https://doi.org/10.2514/6.2001-1463
[research_xu_chen_2023]: https://doi.org/10.1017/aer.2023.59
[research_xu_gao_2015]: https://doi.org/10.1155/2015/258315
[research_xu_gao_2015_b]: https://doi.org/10.3923/jse.2015.217.229
[research_xu_han_2020]: https://doi.org/10.1016/j.cja.2019.12.018
[research_xu_kroo_2011]: https://doi.org/10.2514/6.2011-3180
[research_xu_kroo_2011_b]: https://doi.org/10.2514/6.2011-7016
[research_xu_kroo_2014]: https://doi.org/10.2514/1.c032402
[research_xu_qiu_2011]: https://doi.org/10.4028/www.scientific.net/amm.148-149.833
[research_xu_sevart_2024]: https://doi.org/10.2514/6.2024-4231
[research_xu_song_2023]: https://doi.org/10.2139/ssrn.4549793
[research_xu_tang_2016]: https://doi.org/10.1109/chicc.2016.7554396
[research_xu_west_1990]: https://doi.org/10.2514/3.25338
[research_xu_zhang_2020]: https://doi.org/10.1109/access.2020.3041855
[research_xu_zhu_2011]: https://doi.org/10.1016/s1000-9361(11)60048-4
[research_xue_li_2016]: https://doi.org/10.1109/chicc.2016.7553873
[research_xue_ye_2019]: https://doi.org/10.1080/19942060.2019.1663264
[research_xuelei_zhangzheyu_2016]: https://doi.org/10.1109/cgncc.2016.7829133
[research_yamamoto_1992]: https://doi.org/10.2514/3.11227
[research_yamane_1992]: https://doi.org/10.1016/0045-7930(92)90023-o
[research_yamane_friedmann_1990]: https://doi.org/10.2514/6.1990-1160
[research_yamane_friedmann_1993]: https://doi.org/10.2514/3.46315
[research_yamashiro_stirling_2007]: https://doi.org/10.2514/6.2007-6381
[research_yamazaki_kusunose_2016]: https://doi.org/10.2514/1.c033417
[research_yan_li_2019]: https://doi.org/10.1051/jnwpu/20193740656
[research_yanagihara_suzuki_1991]: https://doi.org/10.4271/911979
[research_yang_chen_2009]: https://doi.org/10.2514/1.42370
[research_yang_dudley_2018]: https://doi.org/10.2514/1.j056280
[research_yang_gao_2020]: https://doi.org/10.1109/tac.2019.2918122
[research_yang_guo_2009]: https://doi.org/10.2514/6.2009-2197
[research_yang_huang_2017]: https://doi.org/10.2514/1.g002690
[research_yang_huang_2019]: https://doi.org/10.1016/j.jsv.2019.01.006
[research_yang_kim_2011]: https://doi.org/10.5302/j.icros.2011.17.11.1067
[research_yang_kou_2025]: https://doi.org/10.33737/gpps25-tc-002
[research_yang_li_2014]: https://doi.org/10.1109/cgncc.2014.7007599
[research_yang_li_2022]: https://doi.org/10.3390/aerospace9090515
[research_yang_liu_2023]: https://doi.org/10.1061/(asce)as.1943-5525.0001484
[research_yang_liu_2025]: https://doi.org/10.1007/978-981-96-2240-5_49
[research_yang_sartor_2015]: https://doi.org/10.2514/6.2015-0441
[research_yang_shen_2007]: https://doi.org/10.2514/6.2007-1052
[research_yang_wan_1978]: https://doi.org/10.21236/ada061942
[research_yang_wu_2025]: https://doi.org/10.1063/5.0280452
[research_yang_xia_2011]: https://doi.org/10.1007/s11431-011-4454-5
[research_yang_xiao_2010]: https://doi.org/10.1007/s11431-010-4103-4
[research_yang_xie_2019]: https://doi.org/10.1177/0954410019885238
[research_yang_xu_2024]: https://doi.org/10.1007/s11071-024-09764-9
[research_yang_zheng_2007]: https://doi.org/10.1007/978-3-540-75999-7_127
[research_yang_zhong_2009]: https://doi.org/10.1109/aero.2009.4839614
[research_yao_kan_2023]: https://doi.org/10.3390/aerospace10040328
[research_yasue_sawada_2009]: https://doi.org/10.2514/6.2009-604
[research_yates_1963]: https://doi.org/10.2514/6.1963-205
[research_yavuzturk_topbas_2017]: https://doi.org/10.2514/6.2017-1865
[research_ye_ye_2021]: https://doi.org/10.1016/j.ast.2020.106428
[research_yee_1992]: https://doi.org/10.6028/nist.ir.4823
[research_yeh_1995]: https://doi.org/10.2514/6.1995-2263
[research_yeo_kang_2023]: https://doi.org/10.2514/1.c036950
[research_yeo_potsdam_2010]: https://doi.org/10.4050/vfs-f66-000444
[research_yerly_deluca_2016]: https://doi.org/10.2514/6.2016-3570
[research_yiming_mei_2019]: https://doi.org/10.1109/iccais46528.2019.9074698
[research_yin_wu_2015]: https://doi.org/10.2514/6.2015-1860
[research_yin_xiao_2026]: https://doi.org/10.1007/978-981-95-7668-5_12
[research_yokozeki_sugiura_2014]: https://doi.org/10.2514/6.2014-1261
[research_yomchinda_horn_2009]: https://doi.org/10.2514/6.2009-6058
[research_yoneyama_hatamura_1989]: https://doi.org/10.1299/jsmec1988.32.113
[research_yonezawa_obayashi_2010]: https://doi.org/10.2514/1.46651
[research_yoon_chung_2012]: https://doi.org/10.1007/s12206-012-0889-2
[research_yoshikawa_1982]: https://doi.org/10.2514/6.1982-1362
[research_you_kim_2020]: https://doi.org/10.2514/1.j058002
[research_youssef_1985]: https://doi.org/10.2514/6.1985-1861
[research_yu_1979]: https://doi.org/10.2514/6.1979-75
[research_yu_1980]: https://doi.org/10.2514/3.50744
[research_yu_2026]: https://doi.org/10.21741/9781644904251-73
[research_yu_bose_2026]: https://doi.org/10.2514/6.2026-1052
[research_yu_campbell_1992]: https://doi.org/10.2514/6.1992-2651
[research_yu_he_2016]: https://doi.org/10.1109/chicc.2016.7553228
[research_yu_lv_2014]: https://doi.org/10.4028/www.scientific.net/amm.633-634.1233
[research_yu_wang_2017]: https://doi.org/10.1155/2017/1592527
[research_yu_yuan_2004]: https://doi.org/10.2514/6.2004-1752
[research_yu_zhao_2013]: https://doi.org/10.4028/www.scientific.net/amm.327.246
[research_yuan_2026]: https://doi.org/10.54254/2753-8818/2026.dl34744
[research_yuan_ma_2023]: https://doi.org/10.1016/j.ast.2023.108508
[research_yucelen_kim_2011]: https://doi.org/10.2514/6.2011-6454
[research_yue_2026]: https://doi.org/10.2514/6.2026-4344
[research_yue_wang_2017]: https://doi.org/10.2514/6.2017-3396
[research_yue_zhang_2017]: https://doi.org/10.1016/j.ast.2017.08.013
[research_yurkovich_1986]: https://doi.org/10.2514/6.1986-897
[research_yurkovich_2009]: https://doi.org/10.2514/6.2009-2514
[research_yurtsever_sahin_2026]: https://doi.org/10.3390/aerospace13070596
[research_yusuf_hayes_2019]: https://doi.org/10.2514/6.2019-1594
[research_zafirov_2010]: https://doi.org/10.2514/6.2010-7509
[research_zahn_1984]: https://doi.org/10.1061/(asce)0733-9445(1984)110:1(47)
[research_zaichik_yashin_2013]: https://doi.org/10.2514/6.2013-4507
[research_zaki_unel_2017]: https://doi.org/10.1109/icuas.2017.7991344
[research_zanette_almeida_2015]: https://doi.org/10.2514/6.2015-3227
[research_zaw_baranovski_2026]: https://doi.org/10.3390/aerospace13060563
[research_zeiler_1998]: https://doi.org/10.2514/2.2273
[research_zeiler_1999]: https://doi.org/10.2514/2.2495
[research_zeilerthomasa_1998]: https://ntrs.nasa.gov/citations/19990010052
[research_zeising_gerhardt_1993]: https://doi.org/10.2514/6.1993-4840
[research_zeng_baldelli_2007]: https://doi.org/10.2514/6.2007-6302
[research_zeng_baldelli_2008]: https://doi.org/10.2514/6.2008-6374
[research_zeng_kukreja_2012]: https://doi.org/10.2514/1.56790
[research_zeng_moulin_2010]: https://doi.org/10.2514/1.46091
[research_zeng_qian_2017]: https://doi.org/10.2514/6.2017-4146
[research_zeng_singh_1998]: https://doi.org/10.2514/6.1998-4209
[research_zeng_wang_2011]: https://doi.org/10.2514/6.2011-6459
[research_zhan_2016]: https://doi.org/10.2749/222137816819258807
[research_zhang_behal_2014]: https://doi.org/10.1177/1077546314554821
[research_zhang_chen_2020]: https://doi.org/10.1016/j.compstruct.2019.111696
[research_zhang_cheng_2025]: https://doi.org/10.2139/ssrn.5433376
[research_zhang_cheng_2026]: https://doi.org/10.1016/j.measurement.2025.119855
[research_zhang_dai_2026]: https://doi.org/10.1177/09544100261451551
[research_zhang_dai_2026_b]: https://doi.org/10.2514/1.j066148
[research_zhang_deng_2026]: https://doi.org/10.3390/aerospace13010098
[research_zhang_devisser_2017]: https://doi.org/10.2514/6.2017-1863
[research_zhang_ge_2019]: https://doi.org/10.1177/1729881419886740
[research_zhang_guo_2021]: https://doi.org/10.1155/2021/5553304
[research_zhang_hou_2025]: https://doi.org/10.3390/machines13090834
[research_zhang_jiao_2025]: https://doi.org/10.1038/s41598-025-95445-5
[research_zhang_kang_2019]: https://doi.org/10.2514/6.2019-1368
[research_zhang_kang_2025]: https://doi.org/10.1016/j.ymssp.2024.111871
[research_zhang_li_2025]: https://doi.org/10.1007/s42405-025-00955-1
[research_zhang_liu_2022]: https://doi.org/10.1109/lra.2022.3192803
[research_zhang_qiu_2024]: https://doi.org/10.3390/act13060229
[research_zhang_rabbath_2008]: https://doi.org/10.1109/acc.2008.4586631
[research_zhang_shaw_2021]: https://doi.org/10.1016/j.ast.2021.106534
[research_zhang_singh_2000]: https://doi.org/10.2514/6.2000-4255
[research_zhang_soffker]: https://doi.org/10.1007/978-1-4020-9438-5_36
[research_zhang_soffker_2010]: https://doi.org/10.2514/6.2010-8284
[research_zhang_suresh_2007]: https://doi.org/10.1109/cca.2007.4389398
[research_zhang_tian_2024]: https://doi.org/10.3390/app142210234
[research_zhang_wang_2017]: https://doi.org/10.2991/mme-16.2017.1
[research_zhang_wang_2019]: https://doi.org/10.2514/1.c035182
[research_zhang_xiang_2025]: https://doi.org/10.23919/ccc64809.2025.11178744
[research_zhang_xu_2008]: https://doi.org/10.1109/asc-icsc.2008.4675399
[research_zhang_yang_2013]: https://doi.org/10.1016/j.measurement.2013.07.017
[research_zhang_yu_2013]: https://doi.org/10.1155/2013/714168
[research_zhang_zhang_2013]: https://doi.org/10.4028/www.scientific.net/amm.397-400.218
[research_zhang_zhao_2023]: https://doi.org/10.3390/aerospace10120981
[research_zhang_zhao_2024]: https://doi.org/10.1063/5.0214653
[research_zhang_zhou_2018]: https://doi.org/10.2514/6.2018-3574
[research_zhang_zhou_2018_b]: https://doi.org/10.2514/6.2018-3574.c1
[research_zhang_zhu_2021]: https://doi.org/10.1016/j.jfluidstructs.2021.103263
[research_zhao_2009]: https://doi.org/10.1016/j.jsv.2009.02.026
[research_zhao_2011]: https://doi.org/10.1016/j.ast.2010.05.008
[research_zhao_2012]: https://doi.org/10.1007/978-3-642-33832-8_7
[research_zhao_2019]: https://doi.org/10.1109/ihmsc.2019.00027
[research_zhao_2020]: https://doi.org/10.1504/ijvnv.2020.112428
[research_zhao_he_2020]: https://doi.org/10.1016/j.ast.2019.105635
[research_zhao_li_2024]: https://doi.org/10.1016/j.taml.2024.100540
[research_zhao_yang_2023]: https://doi.org/10.1016/j.cja.2022.06.016
[research_zhao_yue_2016]: https://doi.org/10.2514/1.c033713
[research_zhao_zhang_2025]: https://doi.org/10.3390/s25051633
[research_zhao_zheng_2026]: https://doi.org/10.2139/ssrn.6926148
[research_zhavyrkin_sladkova_2023]: https://doi.org/10.21285/1814-3520-2023-2-241-249
[research_zhen_cui_2023]: https://doi.org/10.1007/978-981-19-6613-2_11
[research_zheng_2010]: https://doi.org/10.1007/s10409-009-0328-5
[research_zheng_hedrick_2013]: https://doi.org/10.1371/journal.pone.0053060
[research_zheng_zhang_2018]: https://doi.org/10.1109/access.2018.2789935
[research_zhi_zhou_2020]: https://doi.org/10.1117/12.2557758
[research_zhong_xia_2025]: https://doi.org/10.1007/978-981-95-2998-8_44
[research_zhong_yang_2009]: https://doi.org/10.2514/6.2009-58
[research_zhou_chen_2017]: https://doi.org/10.1016/j.taml.2017.11.006
[research_zhou_xu_2013]: https://doi.org/10.3724/sp.j.1187.2012.00286
[research_zhou_yu_2018]: https://doi.org/10.1016/j.jfluidstructs.2018.03.009
[research_zhu_2018]: https://doi.org/10.3901/jme.2018.14.028
[research_zhu_chen_2017]: https://doi.org/10.23919/chicc.2017.8027398
[research_zhu_li_2019]: https://doi.org/10.2514/1.j058011
[research_zhu_qiao_2009]: https://doi.org/10.1007/978-3-642-01273-0_11
[research_zhuang_lei_2020]: https://doi.org/10.1109/tocs50858.2020.9339720
[research_zhuang_wu_2017]: https://doi.org/10.2514/6.2017-1514
[research_zientek_2001]: https://doi.org/10.4050/vfs-f57-00067
[research_zink_mavris_1998]: https://doi.org/10.2514/6.1998-4781
[research_zink_mavris_1999]: https://doi.org/10.4271/1999-01-5640
[research_zink_mavris_2000]: https://doi.org/10.2514/6.2000-4827
[research_zink_raveh_2000]: https://doi.org/10.2514/6.2000-1439
[research_zink_raveh_2001]: https://doi.org/10.2514/6.2001-1427
[research_zink_raveh_2002]: https://doi.org/10.2514/6.2002-5603
[research_zink_raveh_2003]: https://doi.org/10.2514/2.3126
[research_zink_raveh_2004]: https://doi.org/10.2514/1.64
[research_zou_huang_2022]: https://doi.org/10.2514/1.g006114
[research_zou_mu_2021]: https://doi.org/10.1016/j.jfranklin.2021.01.012
[research_zou_yang_2012]: https://doi.org/10.1109/wcica.2012.6358155
[research_zubin_1998]: https://doi.org/10.1111/j.1475-1305.1998.tb01092.x
[research_zubin_maksimov_2019]: https://doi.org/10.31857/s0869-56524853290-294
[research_zyablikov_shirshov_2021]: https://doi.org/10.14489/hb.2021.11.pp.030-037
