---
layout: post
mathjax: true
comments: true
title: "X-Planes: Bell X-1"
date: 2025-10-07 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 2
---

<!-- A298 -->
<script>console.log("A298");</script>

The [Bell X-1][ref_bell_x1] was built to measure the transonic drag rise and to determine whether an aircraft could retain enough control authority to fly through it. The rest of the design follows from that question. This article is the second in the [X-Planes series][related_post_a297_xplanes_framing], and it applies the research-aircraft model set out there to the aircraft that established the model. The National Advisory Committee for Aeronautics, abbreviated NACA throughout and reconstituted in 1958 as the National Aeronautics and Space Administration, abbreviated NASA, supplied the research programme and the instrumentation. The Army Air Forces supplied the requirement and the money \[[Hansen 1987][book_hansen_1987_engineer_in_charge]\]. [Bell Aircraft][ref_bell_aircraft] supplied the airframe. The rocket-powered lineage of the aircraft is treated separately in [A96 History of Rocketplanes][related_post_a96_history_rocketplanes], which asks what came next. This article asks why the wing was that thick and why the tail moved.

## The Research Question

The keystone is the magnitude and character of the drag rise through Mach one, together with the control authority required to pass through it. In 1944 neither was known. The reason deserves a precise statement, because it is the clearest historical instance of the similarity gap that justifies the series.

The theory available was linearized subsonic aerodynamics. The [Prandtl-Glauert transformation][ref_prandtl_glauert] of [Glauert 1928][research_glauert_1928] relates the compressible pressure coefficient to its incompressible value as

$$C_p = \frac{C_{p,0}}{\sqrt{1 - M_\infty^2}}$$

with $C_{p,0}$ the incompressible pressure coefficient and $M_\infty$ the free-stream [Mach number][ref_mach_number]. The expression [diverges][ref_prandtl_glauert_singularity] as $M_\infty$ approaches unity. That divergence is not a physical prediction of infinite drag. It is the linearization failing at exactly the condition of interest, and the supersonic counterpart of [Ackeret 1925][research_ackeret_1925] is equally singular approached from above. Theory was therefore silent in the band that mattered.

The popular account leaves the impression that the transonic problem arrived suddenly with the jet engine. It did not. The NACA had been working on it for more than a decade, beginning with the compressibility losses of propeller tips, which reach high local Mach numbers while the aircraft itself is slow \[[Hansen 1987][book_hansen_1987_engineer_in_charge]\]. [Stack 1935][research_stack_1935_burble] named the phenomenon the compressibility burble and described the abrupt loss of lift and rise in drag that accompanies it, with the systematic section data gathered by [Stack and Von Doenhoff 1935][research_stack_1935_16_airfoils]. [Stack et al 1939][research_burble_1939_pressures] measured the pressures and forces through the burble directly, and a sustained effort to delay its onset by section design ran through [Stack 1939][research_burble_delay_1939] and [Stack 1944][research_burble_delay_1944]. The same compressibility limit governed engine cowling design, which [Robinson and Becker 1942][research_cowling_highspeed_1942] addresses.

That decade of work established what the problem was and left open what happened past it, and the open half is what the X-1 was for. The experimental facilities had a matching failure. A closed-throat [wind tunnel][ref_wind_tunnel] chokes when the model blocks enough of the test section that the flow reaches sonic conditions at the minimum area, and the tunnel then cannot be driven past that condition regardless of available power. The choking condition does not depend on a shortage of power, and it can be written down. One-dimensional isentropic flow relates local area to Mach number through

$$\frac{A}{A^{*}} = \frac{1}{M} \left[ \frac{2}{\gamma + 1} \left( 1 + \frac{\gamma - 1}{2} M^2 \right) \right]^{\frac{\gamma + 1}{2 (\gamma - 1)}}$$

with $A^{*}$ the area at which the flow would be sonic, tabulated for every case in [NACA Report 1135][research_naca_1135]. A model of frontal area $A_m$ in a test section of area $A_t$ reduces the available flow area, so the effective condition for the tunnel to reach a free-stream Mach number $M_\infty$ is

$$\frac{A_t - A_m}{A_t} \ge \frac{A^{*}(M_\infty)}{A_t}$$

and as $M_\infty$ approaches unity the right-hand side approaches the whole test-section area. Any model of finite size therefore chokes the tunnel before the free stream reaches Mach one, and the blockage ratio

$$\varepsilon_b = \frac{A_m}{A_t}$$

sets how early. Reducing the model until it no longer chokes reduces the Reynolds number until the data no longer represent the aircraft. Here the similarity gap takes its sharpest form. Data in the band from roughly Mach 0.85 to Mach 1.15 were unusable, and the [NACA conference on transonic design problems][research_transonic_conference_1949] held in 1949 records how completely that band had resisted ground measurement. The slotted and perforated wall treatments that eventually opened it, and the wall-interference corrections that make transonic tunnel data trustworthy even now as in [Chen et al 2024][research_chen_wang_2024], all postdate the X-1.

What remained was falling bodies, rocket-propelled models, and accidents. Aircraft in high-speed dives, notably the [Lockheed P-38 Lightning][ref_p38], encountered a nose-down pitching tendency that the pilot could not counter, and some of them did not recover. The phenomenon acquired the name [Mach tuck][ref_mach_tuck]. Whether it reflected a drag barrier, a stability change, a control failure, or all three was the open question, and the popular framing of a [sound barrier][ref_sound_barrier] treated as a physical wall obscured that the difficulty was several distinct effects arriving together.

Two of those effects can be separated on paper. The first is the [critical Mach number][ref_critical_mach], the free-stream Mach number at which the flow first reaches sonic conditions somewhere on the body. It is found by equating the compressible peak suction to the pressure coefficient corresponding to sonic flow,

$$C_{p,\text{crit}} = \frac{2}{\gamma M_\infty^2} \left[ \left( \frac{1 + \frac{\gamma - 1}{2} M_\infty^2}{1 + \frac{\gamma - 1}{2}} \right)^{\frac{\gamma}{\gamma - 1}} - 1 \right]$$

with $\gamma$ the ratio of specific heats, and solving for the Mach number at which the transformed peak suction meets that value. The second is the [drag divergence Mach number][ref_drag_divergence], higher than the critical value, at which [wave drag][ref_wave_drag] from the terminating [shock][ref_shock_wave] begins to dominate, conventionally defined by

$$\left. \frac{\partial C_D}{\partial M} \right|_{M = M_{DD}} = 0.1$$

The shock itself is governed by the Rankine-Hugoniot relations, which for a [normal shock][ref_normal_shock] at upstream Mach number $M_1$ give the static pressure, density, and temperature ratios

$$\frac{p_2}{p_1} = \frac{2 \gamma M_1^2 - (\gamma - 1)}{\gamma + 1}, \qquad \frac{\rho_2}{\rho_1} = \frac{(\gamma + 1) M_1^2}{(\gamma - 1) M_1^2 + 2}$$

$$\frac{T_2}{T_1} = \frac{\left[ 2 \gamma M_1^2 - (\gamma - 1) \right] \left[ (\gamma - 1) M_1^2 + 2 \right]}{(\gamma + 1)^2 M_1^2}$$

and a downstream Mach number

$$M_2^2 = \frac{(\gamma - 1) M_1^2 + 2}{2 \gamma M_1^2 - (\gamma - 1)}$$

The loss that matters for drag is the entropy rise, expressed as a total pressure ratio,

$$\frac{p_{02}}{p_{01}} = \exp \left( -\frac{\Delta s}{R} \right)$$

which is unity for a vanishing shock and falls rapidly as shock strength grows. Wave drag is that loss integrated over the surface, which is why the drag rise begins gently and then steepens. The rise can be fitted, though not derived, in the form

$$C_D(M) = C_{D0} + \Delta C_{D_w} \left( \frac{M - M_{\text{crit}}}{M_{DD} - M_{\text{crit}}} \right)^{n}, \qquad M > M_{\text{crit}}$$

with $n$ between two and four, and the purpose of the X-1 was to supply the coefficients that such a fit requires. Between the critical and divergence Mach numbers lies the region where a shock stands on the surface and the [boundary layer][ref_boundary_layer] beneath it may or may not separate. [Prandtl 1928][research_prandtl_1928] introduced the boundary layer whose behaviour decides all of this, and separation occurs where the adverse pressure gradient imposed by the shock overcomes the near-wall momentum,

$$\left. \frac{\partial u}{\partial y} \right|_{y=0} = 0$$

which is the separation criterion in its simplest form. That [flow separation][ref_flow_separation] is the mechanism behind both the [buffeting][ref_buffeting] and the control failure, and it remains an active research subject, treated in the contemporary literature by [Chung 2017][research_chung_2017] and [Qi et al 2026][research_qi_gao_2026] for buffet onset prediction and by [Sugioka et al 2021][research_sugioka_2021] for the unsteady pressure field it produces.

The question the X-1 was built to answer was therefore not whether an aircraft could exceed Mach one, which nobody with a working knowledge of ballistics doubted, since projectiles had long been supersonic. It was how much drag the rise represented, how the pitching moment behaved through it, and whether a pilot retained the authority to do anything about either.

## Programme Origin

The programme came out of a disagreement in 1944. The NACA wanted a turbojet aircraft that would collect transonic data, the Army Air Forces wanted a rocket aircraft able to reach about Mach 1.2, and in December 1944 the Army Air Forces settled the matter by paying for the airplane and choosing the rocket \[[Hansen 1987][book_hansen_1987_engineer_in_charge]\]. The Navy pursued a parallel and partly overlapping effort that produced the Douglas D-558 series, whose transonic handling qualities [Ankenbruck 1954][research_d558_handling_1954] reports, its slat loads in [Peele 1953][research_d558_slat_1953], and the drag penalty of external stores measured by [Nugent 1957][research_d558_stores_1957]. The two programmes are best read together, because the Navy aircraft was turbojet-powered and runway-launched where the X-1 was rocket-powered and air-launched, so the pair brackets the design space rather than duplicating a point in it. The rationale for a dedicated research aircraft, as opposed to instrumenting a service type, was argued in print by the people who built it in [Drake and Williams 1958][research_williams_drake_1948], which remains the clearest contemporary statement of why the flight-only residual justified the expense. The division of labour matters for reading the record. The NACA specified the research programme and the instrumentation and wanted an aircraft that could be flown repeatedly at incrementally increasing Mach number. The Army Air Forces wanted a demonstration. Those two objectives are not the same and they produced visible friction over the flight programme, which is treated below.

Bell Aircraft received the airframe contract in March 1945 for what was then designated the XS-1, later shortened to X-1. The sources expand the S differently, Hansen as Sonic and the NASA inventory as Supersonic \[[Hansen 1987][book_hansen_1987_engineer_in_charge]\] \[[Jenkins Landis and Miller 2003][book_jenkins_landis_miller_2003]\]. Three airframes were built \[[Jenkins Landis and Miller 2003][book_jenkins_landis_miller_2003]\], and the fleet size agrees with the attrition sizing derived in the [series opener][related_post_a297_xplanes_framing]. Three is also close to the worst possible quantity from a unit-cost standpoint, because the learning effects quantified for airframe manufacture by [Wright 1936][research_wright_1936],

$$C_n = C_1 \, n^{\log_2 b}$$

with a learning rate $b$ near 0.80, have barely begun at $n = 3$. The third airframe costs about 70 percent of the first, where the hundredth would cost about 23 percent. A research aircraft is therefore expensive per unit because it is never built in quantity, not because it is complex, and that arithmetic recurs throughout this series. The design decisions that define the aircraft were all made under the constraint that the answer was unknown, which produces a characteristic conservatism.

The fuselage was shaped after a .50 calibre machine gun bullet, on the reasoning that a projectile of that form was known to be stable and to have acceptable drag through Mach one because it had been observed to do so in ballistic ranges \[[Wikipedia Article on the Bell X-1][ref_bell_x1]\] \[[National Air and Space Museum Record for the Bell X-1][ref_nasm_x1]\]. That was design by the only available data. The fineness ratio that choice implies can be checked against the wave-drag result. With a fuselage length of 9.45 metres and a maximum diameter of 1.40 metres the fineness ratio is

$$f = \frac{L_f}{d_{\max}} = \frac{9.45}{1.40} = 6.75$$

and the maximum cross-sectional area is $A_{\max} = 1.54$ square metres, so the [Sears-Haack][ref_sears_haack] minimum wave drag area is

$$\frac{D_w}{q} = \frac{9 \pi}{2} \left( \frac{A_{\max}}{L_f} \right)^2 = 14.14 \times \left( \frac{1.54}{9.45} \right)^2 = 0.375 \ \text{square metres}$$

which against a reference wing area of 12.1 square metres is a wave drag coefficient contribution of 0.031. The contribution is of the same order as the transonic peak taken below. It indicates that the fuselage, not the wing, dominated the drag rise, and it justifies in retrospect the effort spent on fuselage shape. The wing was unswept, because although [Jones 1947][research_jones_1947] had by then established the [sweep][ref_swept_wing] argument, an unswept wing keeps the aerodynamics interpretable, and the aircraft was built to produce interpretable data, not speed.

The propulsion choice followed from the thrust requirement derived below. A turbojet of 1945 could not produce the thrust-to-weight ratio needed to push through an unknown drag rise at altitude, so the aircraft used a [Reaction Motors][ref_reaction_motors] [XLR11][ref_xlr11] rocket engine burning [liquid oxygen][ref_liquid_oxygen] and diluted [ethyl alcohol][ref_ethanol_fuel]. The propellant tradeoff space that makes that combination sensible for the period is covered in [A217 Rocket Propellant Chemistry][related_post_a217_rocket_propellant_chemistry].

The aircraft was air-launched from a [Boeing B-29 Superfortress][ref_b29] rather than taking off under its own power. That decision is usually explained as a fuel-saving measure, which is true but understates it \[[Hansen 1987][book_hansen_1987_engineer_in_charge]\]. The carrier aircraft supplies both altitude and speed, and the quantity it supplies is energy. Energy is the correct accounting unit for a rocket aircraft and is developed below.

The design decision that turned out to matter most was the [all-moving horizontal tail][ref_stabilator], an incidence-adjustable stabilizer carrying a hinged [elevator][ref_elevator_aircraft], rather than a fixed surface with an elevator alone \[[Hansen 1987][book_hansen_1987_engineer_in_charge]\]. The historiography of that decision is contested. The British [Miles M.52][ref_miles_m52] programme had adopted an all-moving tail and was cancelled in 1946, and whether and how that information reached Bell is disputed in the literature, with [Wood 1975][book_wood_1975_project_cancelled] and [Brown 2006][book_brown_1988_wings_on_my_sleeve] making the strongest British claims. What is not disputed, because it is in the NACA record, is that the NACA had itself been flight-testing all-movable horizontal tails since at least 1945. [Kleckner 1945][research_allmovable_prelim_1945] reports preliminary flight research on an all-movable horizontal tail as a longitudinal control, and [Harmon 1945][research_allmovable_comparison_1945] compares fixed-stabilizer, adjustable-stabilizer, and all-movable configurations directly. [Kleckner 1946][research_allmovable_geared_1946] extends the work with geared unbalancing tabs. A domestic research basis for the decision demonstrably existed. That bounds the priority question without settling it.

## Sizing From First Principles

The keystone relationship is the thrust required to overcome an unknown drag rise at the test condition. Working it through shows what the design was protecting against.

[Dynamic pressure][ref_dynamic_pressure] at the test condition is most conveniently written in terms of measured static pressure and Mach number as

$$q = \frac{\gamma}{2} p M^2$$

with $p$ the static pressure in pascals. Take the condition of the 14 October 1947 flight, a Mach number of 1.06 at 13,115 metres \[[Wikipedia List of X-1 Flights][ref_list_of_x1_flights]\] \[[National Air and Space Museum Record for the Bell X-1][ref_nasm_x1]\]. The [standard atmosphere][ref_us_standard_atmosphere] in the isothermal layer above 11 kilometres gives a temperature of 216.65 kelvin and a pressure obtained from the hydrostatic relation

$$p(h) = p_{11} \exp \left[ -\frac{g (h - h_{11})}{R T} \right]$$

with $p_{11} = 22{,}632$ pascals, $R = 287$ joules per kilogram kelvin, and $g = 9.80665$ metres per second squared, giving $p = 16{,}212$ pascals and a density of 0.2607 kilograms per cubic metre. The [speed of sound][ref_speed_of_sound] is $a = \sqrt{\gamma R T} = 295.0$ metres per second, so the true airspeed is 312.7 metres per second. The dynamic pressure is therefore

$$q = 0.7 \times 16{,}212 \times 1.1236 = 1.275 \times 10^{4} \ \text{pascals}$$

or 12.75 kilopascals, which is 266 pounds per square foot. That is a low dynamic pressure. The X-1 met the transonic problem in thin air by deliberate choice, because the loads scale with $q$ while the Mach number does not.

Drag at that condition follows from the reference wing area $S$ and the [drag coefficient][ref_drag_coefficient] as

$$D = q S C_D$$

and the design problem in 1945 was that $C_D$ in the transonic band was the unknown the aircraft existed to measure. The engine could not be sized against a known number. It can instead be read as sized so that the available thrust would exceed the drag for any plausible value of the unknown. Inverting the relation gives the drag coefficient at which thrust and drag balance,

$$C_{D,\max} = \frac{T}{q S}$$

which is the largest drag rise the aircraft could push through. The XLR11 delivered four chambers of about 6,672 newtons each for a total of 26,689 newtons \[[Wikipedia Article on the Reaction Motors XLR11][ref_xlr11]\], and with a wing area of 12.1 square metres,

$$C_{D,\max} = \frac{26{,}689}{12{,}750 \times 12.1} = 0.173$$

The transonic peak is taken here as near 0.05, which is consistent with the roughly sixfold rise from subcritical to sonic speed in low-lift drag coefficient that \[[Carman and Carden 1951][ref_naca_rm_l51e08]\] report for the eight-percent wing. The aircraft was therefore capable of overcoming a drag rise more than three times worse than the one it found. That margin is the quantitative expression of designing against an unknown. Reported flight lift and drag for the ten-percent-thick wing appear in [Saltzman 1953][research_x1_liftdrag_1953], and the corresponding wing pressure distributions in [Knapp and Jordan 1953][research_x1_wing_pressures_1953].

The propellant budget follows from the [Tsiolkovsky relation][ref_tsiolkovsky]. With [specific impulse][ref_specific_impulse] $I_{sp}$ taken as 180 seconds, somewhat below the roughly 190 seconds that the rated thrust and the propellant flow of about 7.9 pounds per second per chamber imply \[[Carman and Carden 1951][ref_naca_rm_l51e08]\], the mass flow is

$$\dot{m} = \frac{T}{I_{sp} g_0} = \frac{26{,}689}{180 \times 9.80665} = 15.1 \ \text{kilograms per second}$$

so a propellant load of about 2,268 kilograms \[[Carman and Carden 1951][ref_naca_rm_l51e08]\] gives a full-thrust burn time of

$$t_b = \frac{m_p}{\dot{m}} = \frac{2268}{15.1} = 150 \ \text{seconds}$$

and an ideal velocity increment, with a launch mass of 5557 kilograms \[[Wikipedia Article on the Bell X-1][ref_bell_x1]\], of

$$\Delta v = I_{sp} g_0 \ln \frac{m_0}{m_0 - m_p} = 1765 \times \ln \frac{5557}{3289} = 926 \ \text{metres per second}$$

That number should not be compared directly with the speed achieved, because most of it is spent climbing. The correct comparison is in energy height,

$$h_e = h + \frac{V^2}{2g}$$

The B-29 released the aircraft at roughly 6100 metres \[[Hansen 1987][book_hansen_1987_engineer_in_charge]\], and with a true airspeed taken as 150 metres per second the release energy height is 7247 metres. The fastest flight of the first airframe reached Mach 1.45 at about 12,230 metres \[[Wikipedia List of X-1 Flights][ref_list_of_x1_flights]\] \[[National Air and Space Museum Record for the Bell X-1][ref_nasm_x1]\], which is 428 metres per second and an energy height of 21,559 metres. The gain is 14,312 metres, corresponding to a specific energy of $g \Delta h_e = 1.40 \times 10^{5}$ joules per kilogram, against an ideal budget of $\Delta v^2 / 2 = 4.29 \times 10^{5}$ joules per kilogram. Roughly a third of the ideal energy reached the vehicle state and the remainder went to drag and gravity losses,

$$\eta_{\text{traj}} = \frac{g \Delta h_e}{\Delta v^2 / 2} = 0.33$$

which is a low figure. Since nothing shows that the flight used its whole propellant load or was flown for maximum energy, the figure bounds the published masses and thrust without confirming them.

The air-launch decision can now be stated quantitatively. The carrier supplied 7247 metres of energy height out of a final 21,559, which is 34 percent of the total. Reproducing that from a runway would have required either a much larger propellant fraction or a second propulsion system, and both were rejected \[[Wikipedia Article on the Bell X-1][ref_bell_x1]\] \[[Hansen 1987][book_hansen_1987_engineer_in_charge]\].

Three further ratios complete the sizing picture. The initial thrust-to-weight ratio is

$$\frac{T}{W} = \frac{26{,}689}{5557 \times 9.80665} = 0.49$$

which is far below unity, so the aircraft could not have taken off vertically and had to be either air-launched or given a runway it did not have. The mass budget divides as

$$\frac{m_p}{m_0} = \frac{2268}{5557} = 0.41, \qquad \frac{m_s + m_i}{m_0} = 0.59$$

with a propellant fraction of 0.41 that is low for a rocket and high for an aircraft, the signature of the type. The climb angle available at the test condition follows from the excess thrust,

$$\sin \gamma = \frac{T - D}{W}$$

and the specific excess power, the rate at which energy height can be added, is

$$P_s = \frac{V (T - D)}{W}$$

With two chambers burning, a mass of 4500 kilograms, and drag near 7.7 kilonewtons at the coefficient of 0.05 taken above, the excess is 5.6 kilonewtons, giving a climb angle of 7.3 degrees and a specific excess power of 40 metres per second. The aircraft climbed while accelerating, so the energy-height accounting above is the only coherent way to read the flight profile.

## Dependent Systems

### Wing Section and the Thickness Experiment

The wing was unswept, of [aspect ratio][ref_aspect_ratio] six and area 12.1 square metres, using [NACA 65-series][ref_naca_airfoil] sections \[[Carman and Carden 1951][ref_naca_rm_l51e08]\]. The decisive parameter was thickness ratio, and the programme treated it as an experiment rather than a choice. The first airframe flew its powered programme with an eight-percent-thick wing and the second flew with a ten-percent-thick wing, so that the two could be compared directly at the same conditions \[[Hansen 1987][book_hansen_1987_engineer_in_charge]\] \[[Wikipedia Article on the Bell X-1][ref_bell_x1]\].

The reason thickness dominates is that it sets the peak suction, and the peak suction sets the critical Mach number through the relation above. The peak suction itself scales with thickness. Linearized thin-airfoil theory at low lift gives a minimum pressure coefficient proportional to the thickness ratio,

$$C_{p,\min} \approx -k_t \frac{t}{c}$$

with $k_t$ of order three to four for the NACA six-series shapes, and this relation makes the comparison below a thickness comparison and not an arbitrary one. Taking representative incompressible peak pressure coefficients of $C_{p,0} = -0.30$ for the eight-percent section and $C_{p,0} = -0.38$ for the ten-percent section, and solving

$$\frac{C_{p,0}}{\sqrt{1 - M_\infty^2}} = C_{p,\text{crit}}(M_\infty)$$

numerically gives critical Mach numbers of approximately 0.784 and 0.754 respectively. Two percentage points of thickness are worth about 0.030 in critical Mach number. That difference carries the argument for thin wings on transonic aircraft, and the X-1 was meant to check it in flight instead of assuming it.

Wave drag reinforces the same conclusion. For a slender body the minimum wave drag of [Sears 1947][research_sears_1947] scales as the square of the cross-sectional area distribution,

$$\frac{D_w}{q} = \frac{9 \pi}{2} \left( \frac{A_{\max}}{L} \right)^2$$

so thickness enters quadratically rather than linearly. The [area rule][ref_whitcomb_area_rule] that follows from the same reasoning, established by [Whitcomb 1952][research_whitcomb_1952] several years later, was not available to the X-1 designers, and the aircraft carries no waisting. The experimental route to it is visible in the intervening literature. [Cheatham and Kurbjun 1948][research_transonic_drag_wingbody_1948] measured the transonic drag of a wing-body combination, [NACA 1949][research_comparative_drag_1949] and [NACA 1950][research_comparative_drag_1950] compared rectangular against sweptback sections at the same conditions, [Kelly and Osborne 1954][research_fuselage_mods_drag_1954] examined what fuselage modification alone could achieve, and [Holdaway 1954][research_drag_rise_reduction_1954] investigated reducing the zero-lift drag rise by adding volume in the right place, an experimental statement of the area rule. Separation-controlled variants of the same idea were still being tried two decades later by [Howell and Korst 1971][research_drag_rise_notches_1971].

Lift at the test condition follows from the [lift coefficient][ref_lift_coefficient],

$$C_L = \frac{W}{q S}$$

The lift-curve slope that produces it is also compressibility-corrected,

$$C_{L\alpha} = \frac{C_{L\alpha,0}}{\sqrt{1 - M_\infty^2}}$$

below the critical Mach number, and this relation fails in the same band and for the same reason as the pressure transformation, which is one more thing the flight data had to supply. With a mass near 4500 kilograms after propellant burn the level-flight equivalent lift coefficient at the test point is 0.29, well below any stall consideration. The X-1 was never lift-limited. It was drag-limited and control-limited, so the [drag polar][ref_drag_polar] matters here mainly through its zero-lift term. Written out, the polar is

$$C_D = C_{D0} + \frac{C_L^2}{\pi A e}$$

with the efficiency factor $e$ following the charts of [Oswald 1932][research_oswald_1932]. At an aspect ratio of six, an efficiency factor of 0.85, and a lift coefficient of 0.29, the induced term is

$$\frac{C_L^2}{\pi A e} = \frac{0.0841}{\pi \times 6 \times 0.85} = 0.0052$$

against a transonic zero-lift value near 0.05, so induced drag is about ten percent of the total at the test point and the aircraft is overwhelmingly wave-drag limited. That ratio is the quantitative reason the programme could ignore span efficiency and concentrate on thickness and fuselage shape.

Assembling the full drag build-up is useful, because the result can be checked against the measurement. Skin friction on a turbulent flat plate follows

$$C_f = \frac{0.074}{Re^{1/5}}$$

which at the flight Reynolds number of $8.15 \times 10^{6}$ gives $C_f = 0.00307$, and referred to wing area through a wetted-area ratio near 4.5 this is a friction contribution of 0.0138. The base of the fuselage, where the rocket nozzles sit, contributes

$$C_{D,\text{base}} = -C_{p,b} \frac{A_b}{S}$$

with $C_{p,b}$ the base pressure coefficient, and at a representative transonic value of negative 0.15 over a base area of 0.64 square metres this is 0.0079. That term is the reason the programme measured base and rear fuselage pressures separately, reported in [Knapp and Johnson 1953][research_x1_base_pressures_1953]. Adding the fuselage wave drag of 0.031 and the induced term of 0.0052 gives

$$C_D \approx 0.0138 + 0.0310 + 0.0079 + 0.0052 = 0.058$$

against the transonic peak near 0.05 taken above. An estimate assembled from four independent contributions landing within about fifteen percent of that value is a good result for the period, and it also shows where the estimate is weakest, since the wave drag term is both the largest and the least certain.

### Reynolds Number and the Scale Problem

The tunnel data the programme was checked against were taken at a fraction of flight [Reynolds number][ref_reynolds_number], and quantifying that gap is what makes the flight data valuable rather than merely confirmatory.

The formal basis for asking which groups must match is the theorem of [Buckingham 1914][research_buckingham_1914], which fixes the number of independent dimensionless groups at the number of variables less the number of independent dimensions and therefore tells the experimenter how many knobs must be matched, so that the count is not left to judgement. For this problem the binding pair is Mach number and Reynolds number, the second being

$$Re = \frac{\rho V L}{\mu}$$

with the viscosity following from the relation of [Sutherland 1893][research_sutherland_1893],

$$\mu = \mu_{\text{ref}} \left( \frac{T}{T_{\text{ref}}} \right)^{3/2} \frac{T_{\text{ref}} + S}{T + S}$$

with $\mu_{\text{ref}} = 1.716 \times 10^{-5}$ pascal seconds at 273.15 kelvin and $S = 110.4$ kelvin. At the test condition of 216.65 kelvin this gives $\mu = 1.42 \times 10^{-5}$ pascal seconds, and with a density of 0.2607 kilograms per cubic metre and a speed of 312.7 metres per second the unit Reynolds number is

$$\frac{Re}{L} = \frac{0.2607 \times 312.7}{1.42 \times 10^{-5}} = 5.74 \times 10^{6} \ \text{per metre}$$

so across the 1.42 metre mean geometric chord the flight Reynolds number is $8.2 \times 10^{6}$. A quarter-scale model as used in [Donlan et al 1976][research_xs1_tunnel_1976] at the same Mach number and temperature would reach a quarter of that unless the tunnel were pressurized, and a sixteenth-scale model as in [Mattson 1947][research_xs1_model_1947] would reach one sixteenth, which is $5 \times 10^{5}$ and firmly in a regime where transition location and separation behaviour differ from flight. Matching both groups requires

$$p_{\text{model}} = k \, p_{\text{flight}}$$

for a geometric scale of $1/k$, which was not available. The flight article was the only place the two could be matched simultaneously, because it was the aircraft.

### Propulsion and the Four-Chamber Engine

The XLR11 produced thrust in four nominally equal chambers, and the pilot selected the number of chambers burning rather than modulating a throttle \[[Wikipedia Article on the Reaction Motors XLR11][ref_xlr11]\]. Thrust was therefore quantized,

$$T_n = n \, T_c, \quad n \in \{0, 1, 2, 3, 4\}$$

with $T_c$ about 6672 newtons. The quantization was a design constraint, because it meant that the acceleration through the drag rise was not continuously controllable. The axial acceleration available at any moment is

$$a_x = \frac{T_n - D}{m}$$

and at the test condition with two chambers burning and a mass of 4500 kilograms the available axial acceleration once the drag is subtracted is

$$a_x = \frac{T_2 - D}{m} = \frac{13{,}345 - 7700}{4500} = 1.25 \ \text{metres per second squared}$$

and the time to cross the drag rise from Mach 0.9 to Mach 1.1 follows by integrating

$$t = \int_{V_1}^{V_2} \frac{dV}{a_x(V)} \approx \frac{\Delta M \, a_\infty}{a_x} = \frac{0.2 \times 295}{1.25} = 47 \ \text{seconds}$$

so the aircraft crossed the drag rise slowly enough for the instrumentation to resolve it. That excess is not free, because in a climb it must be shared,

$$a_x = \frac{T - D}{m} - g \sin \gamma$$

and at the 7.3 degree climb angle computed in Sizing From First Principles the entire excess goes into potential energy and none into acceleration. The pilot chose between them, a choice that specific excess power expresses, and that freedom made the quantization tolerable in operation.

Thrust follows from the momentum and pressure terms,

$$F = \dot{m} v_e + (p_e - p_a) A_e$$

with $v_e$ the exhaust velocity, $p_e$ and $p_a$ the exit-plane and ambient pressures, and $A_e$ the exit area. The pressure term is why the engine performed better at altitude, and it is one reason for flying the test points high. The engine was [pressure-fed][ref_pressure_fed] rather than turbopump-fed, so the tanks themselves were pressure vessels and the nitrogen supply was part of the mass budget. The tank wall thickness follows from the [hoop stress][ref_hoop_stress] relation,

$$\sigma_h = \frac{p_t r}{t_w}, \qquad t_w = \frac{p_t r}{\sigma_{\text{allow}}}$$

with $p_t$ the tank pressure and $r$ the tank radius. At a tank pressure of 2.4 megapascals, a radius of 0.4 metres, and an allowable stress of 300 megapascals, the required wall thickness is 3.2 millimetres. The chamber performance separates into a combustion term and an expansion term through the characteristic velocity and thrust coefficient,

$$c^{*} = \frac{p_0 A_t}{\dot{m}}, \qquad C_F = \frac{F}{p_0 A_t}, \qquad I_{sp} = \frac{c^{*} C_F}{g_0}$$

with $A_t$ the throat area and $p_0$ the chamber pressure. The nozzle fixes $C_F$ through its expansion ratio, obtained by solving the area relation at the exit Mach number,

$$\varepsilon_n = \frac{A_e}{A_t} = \frac{1}{M_e} \left[ \frac{2}{\gamma + 1} \left( 1 + \frac{\gamma - 1}{2} M_e^2 \right) \right]^{\frac{\gamma + 1}{2 (\gamma - 1)}}$$

For a chamber pressure near 1.7 megapascals expanding to roughly 40 kilopascals with a combustion-gas ratio of specific heats near 1.2, the exit Mach number is 2.95 and the expansion ratio is 6.3, which is modest and appropriate for an engine that must work from sea level to the stratosphere without an altitude-compensating nozzle. The propellant combination fixes $c^{*}$. Complete combustion of ethanol in oxygen proceeds as

$$\mathrm{C_2H_5OH} + 3\,\mathrm{O_2} \longrightarrow 2\,\mathrm{CO_2} + 3\,\mathrm{H_2O}$$

which at molar masses of 46.07 and 32.00 grams per mole gives a stoichiometric oxidizer-to-fuel mass ratio of

$$\left. \frac{m_{ox}}{m_f} \right|_{\text{stoich}} = \frac{3 \times 32.00}{46.07} = 2.08$$

Engines of the period ran fuel-rich of stoichiometric to hold chamber temperature down, and the alcohol was further diluted with water for the same reason \[[Carman and Carden 1951][ref_naca_rm_l51e08]\], which costs specific impulse and buys chamber life. The tank volume required follows from the propellant densities,

$$V_{\text{tank}} = \frac{m_{ox}}{\rho_{ox}} + \frac{m_f}{\rho_f}$$

and with liquid oxygen at 1141 and diluted alcohol at about 810 kilograms per cubic metre, a 2268 kilogram load split near the operating mixture ratio needs roughly 2.4 cubic metres of tankage. Pressurizing that volume to 2.4 megapascals with nitrogen requires a pressurant mass of

$$m_{N_2} = \frac{p_t V_{\text{tank}}}{R_{N_2} T} = \frac{2.4 \times 10^{6} \times 2.4}{297 \times 290} = 67 \ \text{kilograms}$$

before accounting for the mass of the high-pressure vessels that store it. The tank pressure is not a free choice either, since it must exceed the chamber pressure by the injector drop and the line losses,

$$p_t = p_c + \Delta p_{\text{inj}} + \Delta p_{\text{line}}$$

and the injector drop is in turn set by the requirement that the feed system be stiff enough to prevent combustion instability coupling back into the propellant lines, conventionally $\Delta p_{\text{inj}} \gtrsim 0.2 \, p_c$. That inequality is the reason a pressure-fed engine cannot simply raise chamber pressure to improve performance, and it caps the architecture. Pressure feeding trades tank mass for turbomachinery development risk, and in 1945 that trade favoured tank mass decisively \[[Hansen 1987][book_hansen_1987_engineer_in_charge]\].

### Structure and the Load Factor Unknown

The airframe was designed to a load factor of eighteen, which is extreme for a crewed aircraft and reflects that nobody knew what loads the transonic band would impose \[[Hansen 1987][book_hansen_1987_engineer_in_charge]\]. The [load factor][ref_load_factor] is

$$n = \frac{L}{W}$$

and at a launch weight of 54,514 newtons the design load is 981 kilonewtons. For an elliptic spanwise distribution over a span of 8.53 metres the root bending moment is

$$M_{\text{root}} = \frac{n W b}{3 \pi} = \frac{981{,}252 \times 8.53}{9.42} = 8.88 \times 10^{5} \ \text{newton metres}$$

where the elliptic distribution assumed is the minimum-induced-drag case of [Munk 1921][research_munk_1921],

$$\ell(y) = \frac{4 L}{\pi b} \sqrt{1 - \left( \frac{2 y}{b} \right)^2}$$

The required spar cap area for an allowable stress $\sigma_{\text{allow}}$ and structural depth $h_s$ is

$$A_{\text{cap}} = \frac{M_{\text{root}}}{\sigma_{\text{allow}} h_s}$$

With [duralumin][ref_duralumin] at 400 megapascals and a root structural depth of 0.144 metres, being eight percent of a 1.8 metre root chord, the cap area is 154 square centimetres. Two caps four metres long at a density of 2780 kilograms per cubic metre come to roughly 340 kilograms, which is six percent of the launch mass in spar caps alone. That figure is the price of designing against the unknown, and the X-1 is heavy for its size because of it. The [factor of safety][ref_factor_of_safety] applied on top of it made the aircraft heavier still.

The manoeuvring boundary follows from the same load factor. The corner speed, the lowest speed at which the limit load can be reached aerodynamically, is

$$V_A = \sqrt{\frac{2 n_{\max} W}{\rho S C_{L,\max}}}$$

and at the test altitude with $n_{\max} = 8$ for the operational limit rather than the ultimate design value, this is 482 metres per second, or Mach 1.63. The aircraft could not reach its structural limit aerodynamically anywhere in the subsonic envelope, which restates the overdesign in envelope terms. Limit and ultimate loads are conventionally related by

$$n_{\text{ult}} = 1.5 \, n_{\text{limit}}$$

and the structural mass fraction that results,

$$\frac{m_s}{m_0} \approx 0.35$$

is high for an aircraft of this size and is the direct cost of the unknown.

Two further structural checks belong to the same sizing. Thin skin panels fail by buckling long before they reach material yield, at a critical stress

$$\sigma_{cr} = \frac{k \pi^2 E}{12 \left( 1 - \nu^2 \right)} \left( \frac{t_s}{b_s} \right)^2$$

with $E$ the elastic modulus, $\nu$ the Poisson ratio, $t_s$ the skin thickness, $b_s$ the stiffener pitch, and $k$ near four for a simply supported panel. For aluminium at 72 gigapascals with a 1.6 millimetre skin on a 100 millimetre pitch this gives 68 megapascals, which is a small fraction of the material allowable and explains why high-speed airframes carry closely spaced stringers. Torsion is carried as a shear flow around the closed box,

$$q_s = \frac{T_{\text{torque}}}{2 A_m}$$

by the Bredt relation, with $A_m$ the enclosed area, and the same enclosed area appears in the torsional stiffness that sets the divergence speed below. Dynamic behaviour imposed a second constraint. Flutter clearance is governed by the reduced frequency

$$k = \frac{\omega b}{V}$$

with $b$ the semichord, and by the mass ratio and flutter speed index

$$\mu_m = \frac{m_w}{\pi \rho b^2}, \qquad F_i = \frac{V_f}{b \omega_\alpha \sqrt{\mu_m}}$$

with $\omega_\alpha$ the uncoupled torsional frequency. The unsteady aerodynamic theory behind the calculation is [Theodorsen 1935][research_theodorsen_1935], its programme history is [Garrick and Reed 1981][research_garrick_reed_1981], and the field was named and bounded by [Collar 1946][research_collar_1946]. Static [divergence][ref_aeroelasticity] of the thin wing was checked against

$$q_D = \frac{K_\theta}{e S C_{L\alpha}}$$

and a thin unswept wing at low dynamic pressure is comfortably clear of it, which is one of the few places the X-1 had margin to spare. The standard treatments are [Bisplinghoff Ashley and Halfman 1955][book_bisplinghoff_ashley_halfman_1955] and [Fung 1955][book_fung_1955], with wing-aileron flutter of the later thin-wing X-1E measured by [Gibson et al 1957][research_x1e_flutter_1957].

Wing loads determined from pressure measurement on the ten-percent-thick aircraft come from [Knapp and Jordan 1953][research_x1_wing_loads_1953], and the equivalent horizontal-tail load measurements on the sibling [Bell X-5][ref_bell_x5] in [Reed 1955][research_x5_tail_loads_1955]. The loads and structures community treated these programmes together, as the [NACA 1957 conference on aircraft loads, structures, and flutter][research_loads_flutter_conf_1957] records, and flight flutter testing acquired its own literature in the [NASA 1975 symposium][research_flutter_symposium_1975]. Measured wing and tail loads from the acceptance programme come from [Beeler and Mayer 1948][research_xs1_loads_1948], and the flight-determined fuselage pressures in [Knapp et al 1953][research_x1_fuselage_pressures_1953] and [Knapp and Johnson 1953][research_x1_base_pressures_1953]. Contemporary practice for the same measurement problem is described by [Zhao et al 2024][research_zhao_li_2024], and the calibration of strain-gauge installations remains the same exercise it was then.

### The All-Moving Tail

The programme turned on this subsystem, and the case can be argued quantitatively.

The pitching moment contribution of a horizontal tail is conventionally written through the tail volume coefficient

$$V_H = \frac{S_t \, l_t}{S \, \bar{c}}$$

with $S_t$ the tail area, $l_t$ the tail arm, and $\bar{c}$ the mean aerodynamic chord. For the X-1 with a tail area of 2.42 square metres, a tail arm of 4.5 metres, and a mean chord of 1.42 metres, $V_H = 0.63$. The control power of a full-incidence stabilizer is then

$$C_{m \delta_s} = -V_H \, C_{L \alpha_t} \, \eta_t$$

with $C_{L\alpha_t}$ the tail lift-curve slope and $\eta_t$ the tail efficiency. Taking 4.0 per radian and 0.9 gives $C_{m\delta_s} = -2.28$ per radian. A hinged elevator instead produces

$$C_{m \delta_e} = -V_H \, C_{L \alpha_t} \, \eta_t \, \tau$$

where $\tau$ is the elevator effectiveness parameter, a function of the ratio of elevator chord to tail chord. Thin-airfoil theory gives it explicitly as

$$\tau = 1 - \frac{\theta_h - \sin \theta_h}{\pi}, \qquad \cos \theta_h = 2 \frac{c_e}{c_t} - 1$$

which for a thirty-percent-chord elevator returns $\theta_h = 1.982$ radians and $\tau = 0.66$. Measured values run lower than the inviscid theory because of boundary-layer thickening near the hinge and gap leakage, and a value near 0.5 is representative for a thirty-percent-chord elevator in attached flow. The elevator therefore starts with half the authority of the all-moving surface.

The decisive point is not the nominal value of $\tau$ but what happens to it. When a shock forms ahead of the hinge line and the boundary layer separates behind it, the elevator deflection no longer changes the circulation over the whole surface, and $\tau$ collapses toward zero. The all-moving surface has no hinge line inside the flow field to be blanked, so its authority is not destroyed by the same mechanism.

The trim requirement makes the consequence concrete. As the flow becomes supersonic the [aerodynamic centre][ref_aerodynamic_center] migrates aft, typically from about the quarter chord to about the half chord, and the resulting nose-down moment increment at a lift coefficient of 0.29 is

$$\Delta C_m = C_L \frac{\Delta x_{ac}}{\bar{c}} = 0.29 \times 0.25 = 0.0725$$

The stabilizer deflection required to trim that out is

$$\delta_s = \frac{\Delta C_m}{\left| C_{m \delta_s} \right|} = \frac{0.0725}{2.28} = 0.032 \ \text{radians} = 1.8 \ \text{degrees}$$

which is trivially available. The elevator deflection required in attached flow would be 3.6 degrees, also available. But with $\tau$ degraded to 0.1 by shock-induced separation the requirement becomes

$$\delta_e = \frac{0.0725}{0.63 \times 4.0 \times 0.9 \times 0.1} = 0.32 \ \text{radians} = 18 \ \text{degrees}$$

which exceeds the available deflection and would be ineffective in any case because the surface it acts on is separated. Mach tuck is thus an arithmetic shortfall in control authority, not a mysterious barrier. That shortfall is why the aircraft flew with a stabilizer that the pilot could adjust in flight rather than with an elevator alone \[[Hansen 1987][book_hansen_1987_engineer_in_charge]\] \[[Wikipedia Article on the Bell X-1][ref_bell_x1]\].

A second mechanism reinforces the first. The [hinge moment][ref_hinge_moment] on a control surface is

$$H = q \, S_e \, c_e \, C_h, \qquad C_h = C_{h_0} + C_{h\alpha} \alpha_t + C_{h\delta} \delta_e$$

with $S_e$ and $c_e$ the surface area and chord aft of the hinge, and the stick force in a manually reversible system is proportional to it through the control system gearing $G$,

$$F_s = G \, H = G \, q \, S_e \, c_e \, C_h$$

so the force the pilot feels scales with dynamic pressure and with a coefficient whose sign is not guaranteed. Through the transonic band the hinge moment derivatives change sign and magnitude unpredictably as the shock moves across the hinge line, so the stick force feedback the pilot relies on becomes an unreliable guide to what the surface is doing. An all-moving surface brings a penalty of its own, since a large surface free to rotate about a spanwise axis is a classical flutter risk, and transonic flutter clearance of all-movable tails was investigated separately by [Abbott and Land 1957][research_allmovable_flutter_1957] and [Sellers 1958][research_allmovable_flutter_1958]. The X-1 accepted that risk because the alternative was no pitch control at all. An all-moving surface driven through an irreversible actuator removes the pilot from that loop entirely. That argument comes from control-system design, not from aerodynamics, and it is at least as important. [Trim tabs][ref_trim_tab] and geared servotabs, the alternative approach of the period, are the subject of [Mungall 1948][research_geared_tab_1948].

Trim is the statement that the total pitching moment vanishes,

$$C_{m_0} + C_{m\alpha} \alpha + C_{m \delta_s} \delta_s = 0$$

and the pilot solves it by adjusting the stabilizer as Mach number changes the first two terms. The tail contribution also fixes where the [neutral point][ref_aerodynamic_center] sits,

$$\frac{x_{np}}{\bar{c}} = \frac{x_{ac,w}}{\bar{c}} + V_H \frac{C_{L\alpha_t}}{C_{L\alpha_w}} \left( 1 - \frac{d\varepsilon}{d\alpha} \right)$$

and with a wing aerodynamic centre at the quarter chord, the tail volume coefficient of 0.63 computed above, a slope ratio of 0.89, and a downwash derivative estimated from lifting-line theory as

$$\frac{d\varepsilon}{d\alpha} \approx \frac{2 C_{L\alpha_w}}{\pi A} = \frac{2 \times 4.5}{\pi \times 6} = 0.48$$

the neutral point lies at 54 percent of the mean aerodynamic chord. Longitudinal dynamics close the picture. The [static margin][ref_longitudinal_static_stability] is

$$SM = \frac{x_{np} - x_{cg}}{\bar{c}}$$

and the aft migration of the neutral point through Mach one increases it sharply, stiffening the aircraft in pitch and raising the short period frequency

$$\omega_{sp} \approx \sqrt{\frac{-M_\alpha Z_w}{V} - M_q \frac{Z_w}{V}}$$

with damping ratio

$$\zeta_{sp} \approx -\frac{M_q + M_{\dot\alpha} + Z_w / V}{2 \, \omega_{sp}}$$

so the aircraft becomes simultaneously harder to trim, quicker to respond, and relatively less damped, a demanding combination for a pilot. The related failure mode, in which the aircraft pitches up uncommandedly as the tail enters the wing wake at high angle of attack, became a preoccupation of the same period and is documented in [Fischel and Nugent 1953][research_longitudinal_accel_1953], [Anderson and Bray 1955][research_pitchup_evaluation_1955], and eventually met with automatic intervention by [Hurt and Whitten 1960][research_pitchup_control_1960]. Configuration effects on the same behaviour appear in [Peterson and Menees 1959][research_unswept_stability_1959], and an alternative control-feel approach using a spring-loaded tab in [Hunter and Reeder 1946][research_spring_tab_1946]. The tail also sits in the wing wake, so its effective incidence carries the downwash derivative

$$\alpha_t = \alpha \left( 1 - \frac{d\varepsilon}{d\alpha} \right) + i_t - \varepsilon_0$$

and the change of $d\varepsilon / d\alpha$ through the transonic band is a research quantity, which [Matthews 1948][research_xs1_downwash_1948] treats for this aircraft. Dynamic stability derived from flight is reported in [Polhamus 1950][research_x1_dynamic_stability_1950], with the lateral case in [Drake 1950][research_x1_lateral_1950]. The standard modern treatments of the modal structure are [Etkin and Reid 1996][book_etkin_reid_1996], [Nelson 1998][book_nelson_1998], [Stengel 2004][book_stengel_2004], and [McRuer Ashkenas and Graham 1973][book_mcruer_ashkenas_graham_1973], and the equivalent problem at model scale is worked in [A122 Stability, Control, and Configuration][related_post_a122_stability_configuration] and [A123 Dynamic Stability and Control][related_post_a123_dynamic_stability].

The NACA basis for the choice is in the 1945 and 1946 reports cited above, and the X-1 trim problem including the [downwash][ref_tailplane] contribution is treated in [Matthews 1948][research_xs1_downwash_1948]. Horizontal tail loads measured at transonic speeds are given by [Rogers 1953][research_x1_tail_loads_1953]. The underlying flow physics is still under study, with contemporary treatments of shock-induced separation on control surfaces in [Pickles and Narayanaswamy 2020][research_pickles_2020] and of the interaction between surface deformation and separation in [Brouwer et al 2017][research_brouwer_2017]. Modern longitudinal control law design for supersonic aircraft, as in [Lee et al 2020][research_lee_sim_2020], still contends with the same aerodynamic centre migration.

### Buffet and the Separated Wake

Shock-induced separation does not only destroy control effectiveness. It also feeds an unsteady wake into the structure, and the resulting [buffeting][ref_buffeting] was a second limiting phenomenon.

Buffet onset is conventionally reported as a boundary in the lift coefficient and Mach number plane,

$$C_{L,\text{buffet}} = f(M_\infty)$$

which falls steeply once the shock is strong enough to separate the boundary layer. The structural response is a forced random vibration, and its severity is measured as the root mean square of the normal acceleration increment,

$$\sigma_{a} = \left[ \frac{1}{T} \int_0^{T} \left( a_n(t) - \bar{a}_n \right)^2 dt \right]^{1/2}$$

with the response concentrated near the natural frequencies of the wing bending modes. The relevant transfer is between the unsteady pressure field and the structural mode, so buffet intensity depends on how nearly the separation shedding frequency approaches a structural frequency rather than on separation alone.

Buffet loads on a quarter-scale model are reported in [Rainey and Igoe 1958][research_buffet_loads_1958], and free-flight rocket model results in [Mason 1953][research_buffet_rocket_models_1953]. The same phenomenon set the practical high-speed limit for the first generation of jet transports, documented in [Butchart et al 1959][research_jet_transport_highspeed_1959]. The field is still active, with onset prediction in [Chung 2017][research_chung_2017] and [Qi et al 2026][research_qi_gao_2026], the unsteady pressure field characterized by [Sugioka et al 2021][research_sugioka_2021], and control approaches in [Di Pasquale and Prince 2023][research_dipasquale_prince_2023] and [Liu and Yang 2016][research_liu_yang_2016]. Passive [vortex generators][research_vortex_generator_1952], investigated by the NACA in 1952, are still studied for the same purpose by [Dai and Zhang 2023][research_dai_zhang_2023] and [Pickles and Narayanaswamy 2020][research_pickles_2020].

One thing the X-1 did not have to contend with is heating. The stagnation temperature at the test condition is

$$T_0 = T_\infty \left( 1 + \frac{\gamma - 1}{2} M_\infty^2 \right) = 216.65 \times 1.225 = 265 \ \text{kelvin}$$

which is below the freezing point of water and imposes no material constraint whatever. Even at the Mach 1.45 record the stagnation temperature is 308 kelvin. Only above roughly Mach 3 does the stagnation-point heating correlation of [Fay and Riddell 1958][research_fay_riddell_1958] and the blunt-body analysis of [Lees 1956][research_lees_1956] become relevant, and neither applies to anything the X-1 did. The thermal problem that dominates the [X-2][ref_bell_x2] and the [X-15][ref_na_x15] does not arise below roughly Mach 2, and the [aluminium][ref_duralumin] airframe was never at risk. The absence matters because it isolates what the X-1 tested.

### Instrumentation and the Problem of Knowing the Mach Number

The hardest measurement in the programme was the Mach number itself, and this deserves more attention than it usually receives.

Airspeed and Mach number come from a [pitot-static system][ref_position_error]. In subsonic flow the ratio of total to static pressure gives Mach number through the isentropic relation

$$\frac{p_0}{p} = \left( 1 + \frac{\gamma - 1}{2} M^2 \right)^{\frac{\gamma}{\gamma - 1}}$$

but above Mach one a bow shock stands ahead of the [pitot tube][ref_pitot_tube] and the probe senses the total pressure behind that shock. The correct relation becomes the [Rayleigh supersonic pitot formula][ref_rayleigh_pitot],

$$\frac{p_{02}}{p_1} = \left[ \frac{(\gamma + 1)^2 M_1^2}{4 \gamma M_1^2 - 2(\gamma - 1)} \right]^{\frac{\gamma}{\gamma - 1}} \cdot \frac{1 - \gamma + 2 \gamma M_1^2}{\gamma + 1}$$

Now evaluate both at the flight condition. At Mach 1.06 the isentropic relation gives a pressure ratio of 2.0330 and the Rayleigh relation gives 2.0325. The two differ by 0.02 percent. At Mach 1.45 they give 3.416 and 3.228, a difference of 5.5 percent.

Those two numbers state the central measurement difficulty of the programme. Just above Mach one the pitot pressure ratio carries almost no information about which side of Mach one the aircraft is on, because the [normal shock][ref_normal_shock] is vanishingly weak and the two formulas agree to within the instrument error. The determination of Mach 1.06 therefore did not and could not rest on reading a cockpit Machmeter, whose needle went off the scale. It rested on the NACA data reduction, which applied the calibrated error of the static source and assumed no error in total head \[[Hansen 1987][book_hansen_1987_engineer_in_charge]\], and the airspeed calibrations for the X-1 were made with ground tracking by radar and phototheodolite \[[Carman and Carden 1951][ref_naca_rm_l51e08]\]. The pressure jump observed on the instrument trace as the shock passed over the static port is evidence that a shock existed, not a calibrated measure of speed.

The reason is the position error. A static port reads a local pressure that differs from free-stream static by an amount that varies with Mach number and that changes abruptly when a shock crosses the port,

$$\Delta p_s = p_{\text{measured}} - p_\infty, \qquad \frac{\Delta M}{M} = f\left( \frac{\Delta p_s}{p_\infty}, M \right)$$

The sensitivity can also be written out explicitly. Differentiating the isentropic relation between pressure ratio and Mach number gives

$$\frac{dM}{M} = \frac{1 + \frac{\gamma - 1}{2} M^2}{\gamma M^2} \cdot \frac{d(p_0 / p)}{p_0 / p}$$

so a one percent error in the measured pressure ratio produces roughly a one percent error in Mach number at Mach one, and rather more at lower Mach number where the leading factor grows. Calibrating the static source through the transonic band, where the error itself moves as the shock crosses the port, was therefore a research task rather than a bench calibration. The NACA treated it as one. [Hasel and Coletti 1948][research_pitot_supersonic_1948] investigated the behaviour of pitot-static tubes at supersonic speeds directly, supplying the experimental counterpart of the Rayleigh relation above. [Thompson et al 1950][research_airspeed_calibration_1950] reports the flight calibration of four separate airspeed systems on one aircraft through Mach one, and flight calibration of that kind is the only honest way to establish what a static source is doing when theory cannot be trusted, and [Sinclair and Mace 1956][research_pitot_vane_1956] extends the calibration to a combined pressure and flow-angularity probe. Anyone inclined to treat the Mach 1.06 figure as a simple instrument reading should look at the length of that calibration literature. The uncertainty in derived quantities then propagates through

$$u_c^2(y) = \sum_i \left( \frac{\partial y}{\partial x_i} \right)^2 u^2(x_i)$$

as described in [Taylor 1997][book_taylor_1997_error_analysis] and [Bevington and Robinson 2002][book_bevington_robinson_2002]. Drag obtained from an [accelerometer][ref_accelerometer] and known thrust,

$$D = T - m a_x$$

amplifies relative uncertainty by approximately the thrust-to-drag ratio, which at the test condition is about 3.5, so a three percent thrust calibration error becomes a ten percent drag uncertainty. The technique and its error budget were set out by [Beeler et al 1956][research_beeler_1956]. Sampling imposed its own limit. Resolving a structural mode at frequency $f_{\max}$ requires

$$f_s > 2 f_{\max}$$

by the criterion of [Nyquist 1928][research_nyquist_1928] and [Shannon 1948][research_shannon_1948], and the resulting recorded bit rate for $N_c$ channels of $b$ bits is

$$B = N_c f_s b$$

The X-1 predates practical wideband [telemetry][ref_telemetry] and carried a five-channel telemeter, so most data were recorded on board by oscillographs, a recording manometer and a camera photographing the instrument panel, and recovered after landing. [Strain gauges][ref_strain_gauge] carried the load measurements \[[Hansen 1987][book_hansen_1987_engineer_in_charge]\]. The modern descendant of this discipline is surveyed by [Grauer and Morelli 2023][research_grauer_morelli_2023].

## The Flight Test Record

The first airframe made unpowered glide flights beginning in January 1946 to establish handling and landing characteristics before any propellant was carried. The first glide is dated 19 January by Hallion and 25 January by the NASA inventory, and the record read for this article does not settle which is right \[[Hallion 1972][book_hallion_1972_supersonic_flight]\] \[[Jenkins Landis and Miller 2003][book_jenkins_landis_miller_2003]\]. Powered flights began in December 1946 \[[Hansen 1987][book_hansen_1987_engineer_in_charge]\]. Acceptance testing by the contractor is the subject of [Williams et al 1948][research_xs1_handling_1948], and the accelerated transonic test results in [Drake et al 1948][research_xs1_accelerated_1948].

The expansion schedule can be put on the same information footing used in the [series opener][related_post_a297_xplanes_framing]. If each flight returns the drag coefficient in a narrow Mach band with relative standard deviation $\sigma_m$, and the prior is $\sigma_0$, then after $n$ flights in that band

$$\sigma_n^2 = \left( \frac{1}{\sigma_0^2} + \frac{n}{\sigma_m^2} \right)^{-1}$$

and reaching a target $\sigma_T$ requires

$$n^{*} = \left\lceil \sigma_m^2 \left( \frac{1}{\sigma_T^2} - \frac{1}{\sigma_0^2} \right) \right\rceil$$

flights per band, with the information gain measured as

$$I_n = \frac{1}{2} \ln \frac{\sigma_0^2}{\sigma_n^2}$$

The rate at which the aircraft could move through that schedule is the specific excess power already derived, since

$$\frac{dh_e}{dt} = P_s$$

so at 40 metres per second the aircraft added its entire energy-height increment of 10.9 kilometres in about four and a half minutes, which is comparable to the powered endurance and explains why every flight was a single climbing run rather than a series of test points. The fleet size follows from the same logic through the attrition condition,

$$\sum_{i=0}^{n_a - 1} \binom{n}{i} p^i (1-p)^{n-i} \ge 1 - \alpha$$

which returns three airframes for a per-flight loss probability of two percent over twenty-five flights at ninety-five percent confidence, and three were built. The decision-theoretic basis is [Lindley 1956][research_lindley_1956] and the modern survey is [Chaloner and Verdinelli 1995][research_chaloner_verdinelli_1995], with the design-of-experiments framing in [Box Hunter and Hunter 2005][book_box_hunter_hunter_2005] and [Gelman et al 2013][book_gelman_et_al_2013]. A programme covering several Mach bands to five percent from an order-unity prior needs a flight count in the tens. The X-1 flew a count of that order, and the cumulative total across three airframes is consistent with the attrition sizing that predicted three. Envelope expansion proceeded in small Mach increments, the standard method then and now, as described for a modern programme by [Deepa and Gupta 2023][research_deepa_gupta_2023]. The NACA plan was that each flight advance the maximum Mach number by a small step and that the next step wait on the ground reduction of the data, although the Air Force pilots often flew faster than the NACA engineers recommended \[[Hansen 1987][book_hansen_1987_engineer_in_charge]\]. The buffet and the loss of elevator effectiveness appeared near Mach 0.88 to 0.94, and when the elevator ran out of authority at Mach 0.94 in October 1947 the team, at first surprised, recovered pitch control by moving the stabilizer \[[Wikipedia Article on the Bell X-1][ref_bell_x1]\].

The character of that schedule matters, because the schedule is the method. A flight was flown to a target Mach number set a small increment above the previous best. The instrumentation recorded on board. The aircraft landed on the lake bed, unpowered \[[Hansen 1987][book_hansen_1987_engineer_in_charge]\], and the unpowered landing was a flight condition that the programme had to clear before anything else. An unpowered glide holds

$$\tan \gamma_g = \frac{1}{L / D}, \qquad w_s = \frac{V}{L / D}$$

with $\gamma_g$ the glide angle and $w_s$ the sink rate. With a subsonic zero-lift drag coefficient near 0.04 the best glide ratio is

$$\left( \frac{L}{D} \right)_{\max} = \frac{1}{2} \sqrt{\frac{\pi A e}{C_{D0}}} = \frac{1}{2} \sqrt{\frac{\pi \times 6 \times 0.85}{0.04}} = 10.0$$

giving a glide angle of 5.7 degrees. The landing weight after propellant exhaustion is near 3300 kilograms, so the stall speed is

$$V_{\text{stall}} = \sqrt{\frac{2W}{\rho S C_{L,\max}}} = \sqrt{\frac{2 \times 32{,}373}{1.10 \times 12.1 \times 1.2}} = 64 \ \text{metres per second}$$

and an approach flown at 1.3 times stall is 83 metres per second with a sink rate of 8.3 metres per second. That is a fast, steep, one-attempt arrival with no engine, which is why the glide programme came first and why a dry lake bed rather than a runway was the enabling piece of infrastructure \[[Hansen 1987][book_hansen_1987_engineer_in_charge]\]. The film and oscillograph records were developed and reduced on the ground between flights. The reduced data were compared against the prediction before the next increment was planned. The loop is slow, and its slowness is the price of not losing the aircraft.

The buffet boundary and the control degradation were therefore met a small step beyond the last cleared point, because each had been approached in steps. What could not be approached in steps was the region above the last data point, and incremental expansion exists to keep that region as small as possible at every moment.

On 14 October 1947 the first airframe, flown by [Chuck Yeager][ref_yeager] and named Glamorous Glennis, reached Mach 1.06 at approximately 13,115 metres. On 26 March 1948 the same airframe reached Mach 1.45 at approximately 12,230 metres in a dive. The 21,900 metres sometimes given for that flight is the altitude of a later flight of the same airframe, on 8 August 1949 \[[Wikipedia List of X-1 Flights][ref_list_of_x1_flights]\] \[[National Air and Space Museum Record for the Bell X-1][ref_nasm_x1]\].

The energy state of that flight can be checked against the propulsion budget derived above. At Mach 1.06 and 13,115 metres the energy height is

$$h_e = 13{,}115 + \frac{312.7^2}{2 \times 9.80665} = 13{,}115 + 4985 = 1.81 \times 10^{4} \ \text{metres}$$

which against a release energy height of 7247 metres is a gain of 10.9 kilometres, well inside what the propellant load allows and consistent with the aircraft having propellant remaining at the test point. The flight of 26 March 1948 reached an energy height of 21.6 kilometres at the highest Mach number the first airframe flew. The difference between the two figures is the difference between demonstrating a condition and exhausting an envelope.

The [National Air and Space Museum record][ref_nasm_x1], which holds the airframe itself, gives the first airframe 78 flights, being nineteen contractor demonstration flights and fifty-nine Air Force test flights, and the flight-by-flight record shows that this count includes the glide flights \[[Wikipedia List of X-1 Flights][ref_list_of_x1_flights]\]. The NASA inventory counts 157 flights for the three first-generation airframes together \[[Jenkins Landis and Miller 2003][book_jenkins_landis_miller_2003]\].

The third airframe was lost in a ground explosion in 1951 attributed to a gasket material reacting with the propellant, without loss of life \[[Wikipedia Article on the Bell X-1][ref_bell_x1]\] \[[Jenkins Landis and Miller 2003][book_jenkins_landis_miller_2003]\]. The [X-1A and later variants][ref_bell_x1a] extended the design to higher speeds and altitudes, and the X-1A encountered violent inertia coupling at Mach 2.44 in December 1953, a phenomenon predicted by [Phillips 1948][research_phillips_1948] and treated in the [series opener][related_post_a297_xplanes_framing]. Wind-tunnel damping measurements for those variants come from [McDearmon and Clark 1956][research_x1a_damping_1956] and [McDearmon and Clark 1956][research_x1e_damping_1956], with the interference effects that complicate such measurements examined by [McDearmon and Boatright 1956][research_x1a_interference_1956] and the lateral and longitudinal stability of the thin-wing variant in [Henderson 1957][research_x1e_lateral_1957], with the X-1E static stability in [Smith 1959][research_x1e_stability_1959] and its flutter characteristics in [Gibson et al 1957][research_x1e_flutter_1957].

## Comparison With Ground Prediction

The similarity-gap argument matters only if the flight data disagreed with the ground prediction, so the question is what the comparison showed.

Three independent ground methods were applied to the same configuration. Wind tunnel tests on a quarter-scale model are described by [Donlan et al 1976][research_xs1_tunnel_1976], and on a sixteenth-scale model in [Mattson 1947][research_xs1_model_1947] and [Mattson and Loving 1948][research_xs1_model_stability_1948]. The free-fall method, in which an instrumented body is dropped from altitude and accelerates through the transonic band under gravity, is reported for this configuration in [Matthews and Mathews 1948][research_xs1_freefall_1948] and had the considerable advantage of reaching the choked band that tunnels could not. The free-fall work was no sideline but a substantial programme. [NACA 1945][research_freefall_1945] established the technique, [Mathews and Thompson 1947][research_freefall_65009_1947] applied it to airfoil sections, [Mathews and Thompson 1947][research_freefall_wingbody_1947] and [Thompson and Mathews 1947][research_freefall_sweptfwd_1947] to wing-body combinations including a swept-forward planform, and [Kurbjun and Thompson 1953][research_freefall_interference_1953] to wing-body interference specifically. The method contributed transonic drag data before the X-1 flew, and it helps explain why the drag rise was expected rather than discovered. Rocket-propelled models provided a fourth route, used for buffet in [Mason 1953][research_buffet_rocket_models_1953].

The agreement varied with configuration. Lift and drag for the ten-percent-thick wing agreed satisfactorily with the sixteenth-scale tunnel data, as [Saltzman 1953][research_x1_liftdrag_1953] reports. Inside the band, and particularly for control surface effectiveness and for the location of separation, the ground methods were less secure, because those quantities depend on boundary layer state and therefore on Reynolds number, which the ground methods did not match. The mechanism is that transition location scales with Reynolds number, so a model at one sixteenth of flight Reynolds number carries laminar flow over a region that is turbulent in flight. Taking a transition criterion of the form

$$Re_{x,\text{tr}} = \frac{\rho V x_{\text{tr}}}{\mu} \approx \text{constant}$$

the transition point moves aft in proportion to $1 / Re$ per unit length, so at a sixteenth of flight Reynolds number the transition location moves aft by a factor of sixteen in fractional chord until it runs off the surface entirely. A fully laminar model and a mostly turbulent aircraft do not separate at the same place, and separation location was the quantity the control-effectiveness question depended on. The free-fall bodies avoided the tunnel walls but not this, since they too were subscale, and their equation of motion

$$m \frac{dV}{dt} = m g \cos \gamma_e - \frac{1}{2} \rho V^2 S C_D$$

gives drag from the measured acceleration in the same way the flight article did. The pattern generalizes. Quantities set by inviscid geometry scale well and quantities set by the boundary layer do not, and the flight-only residual is concentrated in the second class.

The ability to predict a transonic drag change from a model modification remained poor enough to warrant a separate investigation years later from [Pierpont 1957][research_transonic_predict_1957], and computing wave drag reliably took until the era of [Garabedian 1976][research_wave_drag_computation_1976]. The supercritical body work of [Usry and Wallace 1971][research_supercritical_body_1971] and the supercritical airfoil of [Whitcomb and Clark 1965][research_whitcomb_clark_1965] are downstream of the same measurement problem. The wall-interference corrections that make modern transonic tunnel data trustworthy, as in [Chen et al 2024][research_chen_wang_2024], are the eventual answer to the question the X-1 was built to bypass. [Pope and Goin 1965][book_pope_goin_1965] and [Barlow Rae and Pope 1999][book_barlow_rae_pope_1999] document the technique that resulted, and [Baals and Corliss 1981][book_baals_corliss_1981] the facilities.

## What the Data Changed

The programme produced flight-measured transonic force and pressure data on a full-scale aircraft through Mach one, and that database is the concrete deliverable. Lift and drag through the band are tabulated by [Saltzman 1953][research_x1_liftdrag_1953], wing pressure distributions in [Knapp and Jordan 1953][research_x1_wing_pressures_1953], and dynamic stability in [Polhamus 1950][research_x1_dynamic_stability_1950] and [Drake 1950][research_x1_lateral_1950]. Wind tunnel results on a quarter-scale model in [Donlan et al 1976][research_xs1_tunnel_1976] and on a sixteenth-scale model in [Mattson 1947][research_xs1_model_1947] and [Mattson and Loving 1948][research_xs1_model_stability_1948] allowed the flight data to be compared against ground prediction, and the similarity-gap argument turns on that comparison. Free-fall body results in [Matthews and Mathews 1948][research_xs1_freefall_1948] provided a third independent method.

Three consequences are traceable.

The all-moving tail became standard on transonic and supersonic aircraft \[[Wikipedia Article on the Stabilator][ref_stabilator]\]. The [North American F-86 Sabre][ref_f86] adopted an all-flying tail with the F-86E and the [F-100 Super Sabre][ref_f100] was one of the first aircraft to have one, and the configuration is now unremarkable. Whether the X-1 caused that adoption or merely confirmed a decision the NACA research of 1945 had already justified is a real question of attribution, and the honest answer is that the flight demonstration removed the remaining doubt without originating the idea.

The transonic drag database fed directly into the design of the first generation of supersonic fighters \[[Jenkins Landis and Miller 2003][book_jenkins_landis_miller_2003]\].

The successor research airplanes inherited the configuration and the method directly. The [Bell X-2][ref_bell_x2] took the same approach into a thermal and structural regime the X-1 never reached, with glide results in [Day 1953][research_x2_glide_1953] and the Mach 3.2 flight behaviour in [Day and Reisert 1959][research_x2_mach32_1959]. The [Bell X-5][ref_bell_x5] tested variable sweep against the same transonic problem, as [Finch and Walker 1953][research_x5_stability_1953] records. The [Northrop X-4 Bantam][ref_northrop_x4] tested the semitailless configuration that the transonic control problem appeared to argue for. The [Douglas X-3 Stiletto][ref_douglas_x3] pursued sustained supersonic flight and produced the inertia coupling data instead. The [North American X-15][ref_na_x15], whose programme documentation begins with [Beeler 1961][research_x15_conference_1958], carried the method to hypersonic speeds. The [Lockheed F-104 Starfighter][ref_f104] inherited the thin unswept wing directly.

Summaries show the consolidated result of the effort better than any single report does. [Bellman 1959][research_transonic_summary_1959] gathers the flight-determined transonic lift and drag characteristics of several research airplanes into one comparison, the database the programme set out to produce, and [Saltzman and Ayers 1995][research_supersonic_research_1995] reviews the supersonic flight research programme across four decades. [Dana 1993][research_x15_lessons_1993] performs the same service for the X-15, and [Gelzer and Peebles 2015][research_hsfrs_rcs_2015] traces the reaction control lineage from the High Speed Flight Research Station. Operations at extreme altitude, which the X-1 opened and the X-15 completed, are surveyed by [Drake 1957][research_high_altitude_1957].

Boundary layer behaviour in flight, which the tunnel comparison above identified as the weakest link, eventually acquired its own flight measurement programme through [Banner et al 1958][research_transition_flight_1958]. Buffet became a recurring flight-test subject on the successor fleet, documented for the [F-104][research_f104_buffet_1972], for the supercritical-wing [F-8][research_f8_buffet_1977], and in the general investigations of [Benepe et al 1974][research_buffet_response_1974] and [Benepe et al 1978][research_buffet_response_1978], and its characterization continues on modern fighters, as in [Moses and Huttsell 2000][research_f22_fin_buffet_2000]. The supercritical wing that eventually tamed the drag rise for transport aircraft emerges from [Ferris 1972][research_supercritical_17pct_1972].

The programme also had an operational counterpart. Once the research airplanes established what the transonic band did, the NACA instrumented service aircraft in ordinary squadron use to find out what pilots actually did in it, reported for the [F-86A][research_f86_squadron_1952] and the [F-84G][research_f84g_squadron_1953]. That transition from research aircraft to fleet instrumentation is the point at which a research programme has succeeded.

The programme also established the research-aircraft method, its largest consequence and the least tangible. Incremental envelope expansion, dedicated instrumentation, ground data reduction between flights, and a fleet sized for attrition are all visible in the X-1 programme and were subsequently applied to every aircraft in this series. [Vincenti 1990][book_vincenti_1990] treats this kind of knowledge generation directly, and [Hallion 1981][book_hallion_1981_on_the_frontier] and [Gorn 2001][book_gorn_2001_expanding_envelope] cover the institutional consolidation at [Muroc and Edwards][ref_muroc].

The contemporary literature shows how much of the underlying problem remains open. Transonic buffet onset is still predicted rather than computed with confidence, as in [Chung 2017][research_chung_2017] and [Qi et al 2026][research_qi_gao_2026], and its control is an active subject in [Di Pasquale and Prince 2023][research_dipasquale_prince_2023] and [Liu and Yang 2016][research_liu_yang_2016]. Shock and boundary-layer interaction is an open research problem in [Dai and Zhang 2023][research_dai_zhang_2023], [Ma et al 2024][research_ma_yu_2024], and [Natarajan 2022][research_natarajan_2022], with [vortex generators][research_vortex_generator_1952] appearing in the NACA record of 1952 and in the contemporary literature alike. Transonic wing design is posed as an optimization problem in [Poole et al 2026][research_poole_allen_2026] and [Chau and Zingg 2022][research_chau_zingg_2022], and compressibility effects in [Russo et al 2020][research_russo_tognaccini_2020]. The transonic band the X-1 opened has been characterized but not closed.

## The Contemporary Literature

| Cluster | Records |
|---|---|
| Compressibility theory and the computation of transonic flow | 903 |
| Ground test methods, the transonic tunnel and the free-fall body | 546 |
| The transonic drag rise, wave drag and the area rule | 497 |
| Control authority, the all-moving tail and longitudinal trim | 470 |
| Shock and boundary-layer interaction and shock-induced separation | 469 |
| Aeroelasticity, flutter and flight loads | 370 |
| Reynolds number, transition and the scale problem | 297 |
| Buffet onset and the separated wake | 273 |
| Flight test technique, instrumentation and flight measurement | 142 |
| The X-1, its sibling research airplanes and the later research fleet | 123 |
| Transonic and supersonic aircraft design, and the sonic boom | 109 |
| Air data, the pitot-static system and knowing the Mach number | 109 |
| Rocket propulsion and the pressure-fed engine | 61 |
| Other transonic, high-speed and flight research literature | 476 |
| **Total** | **4,845** |

The X-1 answered its question in 1947. The field it opened is not closed, and a survey that stopped at the historical record would leave the reader with the impression that transonic aerodynamics is settled. It is not.

Shock and boundary layer interaction remains the governing unsolved problem. Contemporary treatments include the flow-control study of [Ma et al 2024][research_ma_yu_2024], the vortex generator work of [Dai and Zhang 2023][research_dai_zhang_2023], a direct descendant of the NACA investigation of 1952, and the exchange on bulk viscosity in [Natarajan 2022][research_natarajan_2022]. Control surfaces specifically are treated by [Pickles and Narayanaswamy 2020][research_pickles_2020], and the coupling between surface deformation and separation, which the X-1 encountered as a rigid-surface problem and modern flexible aircraft encounter as an aeroelastic one, by [Brouwer et al 2017][research_brouwer_2017].

Buffet is the second thread. Onset prediction remains empirical enough to warrant continued work in [Chung 2017][research_chung_2017] and [Qi et al 2026][research_qi_gao_2026], the unsteady pressure field remains under experimental characterization by [Sugioka et al 2021][research_sugioka_2021], and suppression is being attempted passively in [Di Pasquale and Prince 2023][research_dipasquale_prince_2023] and numerically in [Liu and Yang 2016][research_liu_yang_2016].

Transonic design has become an optimization discipline. [Poole et al 2026][research_poole_allen_2026] treat the design point itself as a variable, and [Chau and Zingg 2022][research_chau_zingg_2022] optimize an entire strut-braced configuration in the same band the X-1 explored one point at a time. [Russo et al 2020][research_russo_tognaccini_2020] continue to refine compressibility corrections of the kind that failed the X-1 designers. Machine learning has entered the modelling of these flows, surveyed by [Brunton et al 2020][research_brunton_noack_2020].

Ground facilities and computation eventually took back much of the band. Two-dimensional transonic flow yielded to combined experiment and theory through [NASA 1973][research_transonic_2d_1973], lifting wing-body combinations in [Barnwell 1974][research_transonic_wingbody_1974], and test-section flow quality became a design subject with [NASA 1982][research_calspan_ejector_1982]. The modern continuation is visible in the shock and boundary layer interaction experiments summarized by [Sasson et al 2022][research_sbli_experiments_2022], the natural-laminar-flow slotted cruise wing of [Hiller et al 2024][research_slotted_nlf_2024], and the transonic correction method for flight dynamic stability analysis in [Nguyen and Xiong 2021][research_transonic_correction_2021]. Control derivative extraction in the same regime is treated by [Nguyen and Xiong 2023][research_control_derivative_2023].

Two threads of this article have live contemporary literatures, and both repay following.

The first is the all-moving surface. The X-1 adopted it to survive a control problem and accepted a flutter risk in exchange. That exchange has not gone away, and [Bai et al 2022][research_bai_cao_2022] analyse the coupled thermal, aerodynamic, and elastic behaviour of an all-moving control surface directly, the same trade at higher temperature. Shock movement during transonic flutter is now measured rather than inferred, as [Stubblefield et al 2025][research_stubblefield_kunz_2025] report, and actuation for thin high-speed surfaces is a design subject in [Barrett-Gonzalez and Wolf 2021][research_barrett_gonzalez_2021].

The second is air data. The difficulty of knowing the Mach number, argued above, has a modern continuation. [Jurado and McGehee 2019][research_jurado_mcgehee_2019] present a complete online algorithm for air data system calibration, an automated descendant of the flight calibration campaigns of 1950, and [Takahashi et al 2026][research_takahashi_2026_airdata] describe a flush air-data sensing system for a hypersonic flight experiment, where no probe can be exposed at all. The uncertainty framing that accompanies such measurement is treated by [Weiss et al 2022][research_weiss_staudacher_2022].

Buffet and shock control have consolidated into an engineering discipline. Unsteady simulation of buffet on a supercritical section appears in [Zhang et al 2021][research_zhang_yang_2021], shock control bumps for delaying it in [Zhang et al 2026][research_zhang_deng_2026], passive control of the underlying interaction in [da Silva Tuan et al 2024][research_tuan_malatesta_2024], separation suppression on a swept interaction in [Kim and Park 2026][research_kim_park_2026], and the inlet case, which is where the interaction is least forgiving, in [Wang et al 2023][research_wang_wang_2023]. Viscous transonic modelling is treated by [Li and Ekici 2018][research_li_ekici_2018], and the coordinated experimental and numerical programmes that validate all of it by [Lutz et al 2023][research_lutz_kleinert_2023].

Transition prediction, the quantity that made the tunnel-to-flight comparison unreliable in 1947, is still being reduced to a usable criterion, with a surrogate method in [Nie et al 2022][research_nie_song_2022] and an onset criterion in [Egorov 2025][research_egorov_2025].

Supersonic aircraft design has become a multidisciplinary optimization problem rather than a configuration choice, treated generally by [Duan et al 2026][research_duan_wan_2026] and [Takovitskii 2023][research_takovitskii_2023], and specifically against the boom constraint by [Li and Geiselhart 2021][research_li_geiselhart_2021], [Kishi et al 2023][research_kishi_yashiro_2023], and [Ding et al 2023][research_ding_han_2023]. Rocket propulsion for small fast aircraft, the X-1 architecture in miniature, reappears in [Vernacchia et al 2022][research_vernacchia_2022], and tunnel measurement technique continues to advance in [Huang et al 2026][research_huang_liang_2026]. Where speed does bring a thermal problem, which the X-1 never had, the material response is now modelled from molecular processes upward as in [Prata et al 2022][research_prata_2022].

The measurement side has advanced without changing its character. Flight load calibration is essentially unchanged as an exercise, as [Zhao et al 2024][research_zhao_li_2024] describe it, envelope expansion still proceeds by increments as in [Deepa and Gupta 2023][research_deepa_gupta_2023], and system identification from flight data is surveyed by [Grauer and Morelli 2023][research_grauer_morelli_2023]. Boundary layer transition, which the X-1 encountered only as a scaling nuisance, became the central uncertainty for later vehicles and is still verified against flight experiment in [Berry et al 2016][research_blt_shuttle_2016]. Fibre optic sensing of the kind reported in [Pena et al 2018][research_fiber_optic_loads_2018] is the modern version of the strain gauge installation the X-1 carried. Flight-determined lift and drag remains the deliverable it was, whether for a forward-swept research aircraft as in [Saltzman et al 1994][research_fsw_liftdrag_1994] or for a propulsion experiment carried on a supersonic testbed as in [Moes et al 1998][research_aerospike_sr71_1998]. Neither of those aircraft resembles the X-1, and both were flown by the same method.

Finally, the civil supersonic question that the X-1 opened by demonstration is being reopened by regulation. [Ross 2021][research_ross_2021] reports the return of supersonic civil demonstrators, and [Coen et al 2023][research_coen_loubeau_2023] address the acceptability standard that would permit overland flight. The question descends from the X-1 result, and the aircraft addressing it is the X-59, not anything of the first generation.

### Compressibility theory and the computation of transonic flow

**The theory that failed at Mach one and the computation that eventually replaced it.** Compressibility corrections, critical Mach number, small-disturbance theory, transonic potential and Navier-Stokes computation and supercritical sections. **This is the largest cluster**, because computing the transonic band became a discipline of its own once the flight data existed to check it against.

**903 records.** \[[A self-adaptive computational method 1989][research_a_self_adaptive_1989]\] \[[A-7 Transonic Wing Designs 1982][research_a_7_transonic_1982]\] \[[Abed et al 2024][research_abed_alhamadani_2024]\] \[[Ackeret 1925][research_ackeret_1925]\] \[[Adamczyk 1973][research_adamczyk_1973]\] \[[Adamson et al 1980][research_adamson_jr_1980]\] \[[Advanced technology airfoil research 1978][research_advanced_technology_1978]\] \[[Agarwal and Deese 1983][research_agarwal_deese_1983]\] \[[Agarwal and Deese 1983][research_agarwal_deese_1983_b]\] \[[Agrawal et al 1990][research_agrawal_lowrie_1990]\] \[[Agrawal et al 1991][research_agrawal_kinard_1991]\] \[[Agrell and Elmeland 1984][research_agrell_elmeland_1984]\] \[[Agrell and Elmeland 1985][research_agrell_elmeland_1985]\] \[[Ahn and Drela 1998][research_ahn_drela_1998]\] \[[Ahn et al 1999][research_ahn_yee_1999]\] \[[Ahn et al 2001][research_ahn_kim_2001]\] \[[Ahn et al 2001][research_ahn_kim_2001_b]\] \[[Airfoil Integrals 2001][research_airfoil_integrals_2001]\] \[[Albone et al 1976][research_albone_hall_1976]\] \[[Alexander et al 2005][research_alexandermichaelg_andersscottg_2005]\] \[[Alguacil et al 2023][research_alguacil_becherucci_2023]\] \[[Allan and Owens 2006][research_allan_owens_2006]\] \[[Allison and Mineck 1993][research_allisondenniso_mineckraymonde_1993]\] \[[Alshabu et al 2007][research_alshabu_hermes_2007]\] \[[Alternative Methods for Modeling 1989][research_alternative_methods_1989]\] \[[Amiet 1974][research_amiet_1974]\] \[[An Experimental Study on 2006][research_an_experimental_2006]\] \[[Anders et al 1999][research_anders_anderson_1999]\] \[[Andrew and Stenton 1967][research_andrew_stenton_1967]\] \[[Anhichem et al 2025][research_anhichem_timme_2025]\] \[[Application of Computational Methods 1982][research_application_of_1982]\] \[[Applied Computational Transonics-Capabilities and 1982][research_applied_computational_1982]\] \[[Ar 2013][research_ar_2013]\] \[[Armstrong et al 1952][research_armstrong_holt_1952]\] \[[Arnault et al 2016][research_arnault_dandois_2016]\] \[[Arnold and Thiele 1993][research_arnold_thiele_1993]\] \[[Arnold and Thiele 1994][research_arnold_thiele_1994]\] \[[Arthur 1984][research_arthur_1984]\] \[[Atta and Vadyak 1983][research_attaeh_vadyakj_1983]\] \[[Aul'chenko et al 2014][research_aulchenko_zamuraev_2014]\] \[[Avkhadiev et al 1992][research_avkhadiev_elizarov_1992]\] \[[Bachaio 1983][research_bachaio_1983]\] \[[Bailey and Ballhaus][research_bailey_ballhaus]\] \[[Bailey and Ballhaus 1973][research_baileyfr_ballhauswf_1973]\] \[[Baker and Forsey 1981][research_baker_forsey_1981]\] \[[Baker and Forsey 1983][research_baker_forsey_1983]\] \[[Baker et al 1961][research_baker_schuman_1961]\] \[[Balakrishnan 2004][research_balakrishnan_2004]\] \[[Bardina et al 1988][research_bardina_lombard_1988]\] \[[Barnwell 1975][research_barnwellrw_1975]\] \[[Barnwell 1976][research_barnwellrw_1976]\] \[[Baron 1954][research_baron_1954]\] \[[Basic Equations for Unsteady 1989][research_basic_equations_1989]\] \[[Basu and Niyogi 1987][research_basu_niyogi_1987]\] \[[Batina 1986][research_batina_1986]\] \[[Batina 1986][research_batina_1986_b]\] \[[Batina 1986][research_batina_1986_c]\] \[[Batina 1987][research_batina_1987]\] \[[Batina 1988][research_batina_1988]\] \[[Batina 1988][research_batina_1988_b]\] \[[Batina 1989][research_batina_1989]\] \[[Batina and Yang 1985][research_batina_yang_1985]\] \[[Batina et al 1989][research_batina_seidel_1989]\] \[[Bauer et al 1977][research_bauer_garabedian_1977]\] \[[Bazgir and Takovitskii 2018][research_bazgir_takovitskii_2018]\] \[[Bennett et al 1987][research_bennett_bland_1987]\] \[[Bergman 1948][research_bergman_1948]\] \[[Bergman 1949][research_bergman_1949]\] \[[Bernstein 1953][research_bernstein_1953]\] \[[Berry et al 1985][research_berry_yang_1985]\] \[[Berry 1986][research_berrysa_1986]\] \[[Bertelrud et al 1980][research_bertelrud_bergmann_1980]\] \[[Bhaduri et al 2024][research_bhaduri_sugarno_2024]\] \[[Biber and Tilmann 2003][research_biber_tilmann_2003]\] \[[Biibosunov and Karybekov 1967][research_biibosunov_karybekov_1967]\] \[[Biswas et al 2025][research_biswas_mustak_2025]\] \[[Blose 1949][research_blose_1949]\] \[[Boelens 2017][research_boelens_2017]\] \[[Boling et al 2020][research_boling_zha_2020]\] \[[Boppe 1978][research_boppe_1978]\] \[[Boppe 1980][research_boppecw_1980]\] \[[Borland 1979][research_borland_1979]\] \[[Borland and Sotomayer 1989][research_borland_sotomayer_1989]\] \[[Boundry value problems for 2002][research_boundry_value_2002]\] \[[Bourguet et al 2011][research_bourguet_braza_2011]\] \[[Boyle 2002][research_boyle_2002]\] \[[Boyle 2003][research_boyle_2003]\] \[[Branch et al 2023][research_branch_zang_2023]\] \[[Bray 1998][research_bray_1998]\] \[[Bredif 1983][research_bredif_1983]\] \[[Brosh et al 1983][research_brosh_kussoy_1983]\] \[[Brown and Harris 1984][research_brown_harris_1984]\] \[[Bueno et al 2014][research_bueno_sandovalgoes_2014]\] \[[Bur and Berthouze 2003][research_bur_berthouze_2003]\] \[[Burdges 1973][research_burdges_1973]\] \[[Burns and Danehy 2017][research_burns_danehy_2017]\] \[[Burrows et al 2019][research_burrows_vukasinovic_2019]\] \[[Buzzi and Fico 2006][research_buzzi_fico_2006]\] \[[Cahn and Garcia 1971][research_cahn_garcia_1971]\] \[[Campbell and Smith 1987][research_campbell_smith_1987]\] \[[Canic and Keyfitz 1995][research_canic_keyfitz_1995]\] \[[Carlson 1976][research_carlson_1976]\] \[[Carlson 1981][research_carlson_1981]\] \[[Carlson and Weed 1985][research_carlson_weed_1985]\] \[[Carlson et al 1985][research_carlson_pendergraftjr_1985]\] \[[Carlson 1979][research_carlsonla_1979]\] \[[Caughey 1976][research_caughey_1976]\] \[[Caughey 1982][research_caughey_1982]\] \[[Caughey and Jameson 1977][research_caughey_jameson_1977]\] \[[Caughey and Jameson 1979][research_caughey_jameson_1979]\] \[[Caughey and Jameson 1979][research_caughey_jameson_1979_b]\] \[[Cavcar 2006][research_cavcar_2006]\] \[[CFD Analysis of RAE 2015][research_cfd_analysis_of_2015]\] \[[Chakrabartty 1990][research_chakrabartty_1990]\] \[[Chan et al 1976][research_chan_chen_1976]\] \[[Chan et al 1997][research_chan_yeung_1997]\] \[[Chandrasekhara 1994][research_chandrasekhara_1994]\] \[[Chandrasekhara and Carr 1989][research_chandrasekhara_carr_1989]\] \[[Chandrasekhara and Carr 1990][research_chandrasekhara_carr_1990]\] \[[Chang 1981][research_chang_1981]\] \[[Chao and Shijun 1996][research_chao_shijun_1996]\] \[[Chaparro et al 2016][research_chaparro_fujiwara_2016]\] \[[Chaparro et al 2017][research_chaparro_fujiwara_2017]\] \[[Chaplin 2013][research_chaplin_2013]\] \[[Harris 1975][research_charlesdharris_1975]\] \[[Chassaing and Lucor 2010][research_chassaing_lucor_2010]\] \[[Chaudhuri and Balasubramanyan 1982][research_chaudhuri_balasubramanyan_1982]\] \[[Chen 1981][research_chen_1981]\] \[[Chen 1982][research_chen_1982]\] \[[Chen 1983][research_chen_1983]\] \[[Chen and Bui 1990][research_chen_bui_1990]\] \[[Chen and Chan 1976][research_chen_chan_1976]\] \[[Chen and Gat 2022][research_chen_gat_2022]\] \[[Chen and Thuerey 2024][research_chen_thuerey_2024]\] \[[Chen et al 1979][research_chen_sajben_1979]\] \[[Chen et al 1982][research_chen_verhoff_1982]\] \[[Chen et al 1984][research_chen_vassberg_1984]\] \[[Chen et al 1985][research_chen_clark_1985]\] \[[Chen et al 1985][research_chen_vassberg_1985]\] \[[Chen et al 1987][research_chen_li_1987]\] \[[Chen et al 2026][research_chen_wang_2026]\] \[[Chen et al 2026][research_chen_wang_2026_b]\] \[[Chen et al 1985][research_chencl_chowcy_1985]\] \[[Cheng and Hafez 1973][research_cheng_hafez_1973]\] \[[Cheng and Hafez 1973][research_cheng_hafez_1973_b]\] \[[Cheng and Luo 1996][research_cheng_luo_1996]\] \[[Cheng et al 1980][research_cheng_meng_1980]\] \[[Chern and Keyfitz 2016][research_chern_keyfitz_2016]\] \[[Chiara Iorio][research_chiaraiorio]\] \[[Chieng 1991][research_chieng_1991]\] \[[Chin and Rizzetta 1979][research_chin_rizzetta_1979]\] \[[Chmielewski 1986][research_chmielewski_1986]\] \[[Chow 1986][research_chowcy_1986]\] \[[Chow et al 1985][research_chowcy_holsttl_1985]\] \[[Chow et al 1987][research_chowchuenyen_vandalsemwilliamr_1987]\] \[[Chwalowski et al 2017][research_chwalowski_heeg_2017]\] \[[Chyu and Davis 1979][research_chyu_davis_1979]\] \[[Chyu and Schiff 1981][research_chyu_schiff_1981]\] \[[Chyu and Davis 1984][research_chyuwj_davisss_1984]\] \[[Chyu and Davis 1985][research_chyuwj_davisss_1985]\] \[[Cinnella and Congedo 2006][research_cinnella_congedo_2006]\] \[[Clark et al 2010][research_clark_bain_2010]\] \[[Coakley 1987][research_coakley_1987]\] \[[Cole 1988][research_cole_1988]\] \[[Cole and Malmuth 1989][research_cole_malmuth_1989]\] \[[Collazo Garcia and Ansell 2021][research_collazogarcia_ansell_2021]\] \[[Compressible, Subsonic Flows and 2021][research_compressible_subsonic_2021]\] \[[Compressible, Subsonic Flows and 2025][research_compressible_subsonic_2025]\] \[[Computational Methods for Unsteady 1989][research_computational_methods_1989]\] \[[Consigny et al 1983][research_consigny_gravelle_1983]\] \[[Cook-Ioannidis 1991][research_cookioannidis_1991]\] \[[Cosentino and Holst 1985][research_cosentino_holst_1985]\] \[[Cosentino and Holst 1984][research_cosentinogb_holsttl_1984]\] \[[Coustols et al 1997][research_coustols_seraudie_1997]\] \[[Cramer 2001][research_cramer_2001]\] \[[Cramer et al 1992][research_cramer_tarkenton_1992]\] \[[Daley and Humphreys 1947][research_daleybernardn_humphreysmiltond_1947]\] \[[Danberg et al 1985][research_danberg_heavey_1985]\] \[[Dargel and Thiede 1987][research_dargel_thiede_1987]\] \[[Davies 2020][research_davies_2020_b]\] \[[Davies 2020][research_davies_2020_c]\] \[[Davies 2025][research_davies_2025]\] \[[Davies 2025][research_davies_2025_c]\] \[[Davis and Malcolm 1979][research_davisss_malcolmgn_1979]\] \[[de Faria Mello and Sankar 1999][research_defariamello_sankar_1999]\] \[[de Mattos and Wagner 1994][research_demattos_wagner_1994]\] \[[Decker and Miller 2019][research_decker_miller_2019]\] \[[Deere et al 2016][research_deere_luckring_2016]\] \[[Deese and Agarwal 1987][research_deese_agarwal_1987]\] \[[Deese and Agarwal 1988][research_deese_agarwal_1988]\] \[[Deiwert et al 1975][research_deiwertgs_mcdevittjb_1975]\] \[[Denegri and Dubben 2005][research_denegri_dubben_2005]\] \[[Design and CFD Analysis 2024][research_design_and_2024]\] \[[DeSpirito 2008][research_despirito_2008]\] \[[DeSpirito 2009][research_despirito_2009]\] \[[Dhurandhar et al 2026][research_dhurandhar_sharma_2026]\] \[[Dietrich et al 1984][research_dietrich_kromer_1984]\] \[[Dietz et al 2004][research_dietz_schewe_2004]\] \[[Dietz et al 2005][research_dietz_schewe_2005]\] \[[Djayapertapa and Allen 2000][research_djayapertapa_allen_2000]\] \[[Djojodihardjo 2023][research_djojodihardjo_2023]\] \[[Doherty 2017][research_doherty_2017]\] \[[Donegan 1984][research_donegan_1984]\] \[[Donovan and Takahashi 2010][research_donovan_takahashi_2010]\] \[[Dragoş 2003][research_dragos_2003]\] \[[Drela 1992][research_drelamark_1992]\] \[[Drèze and di Mare 2024][research_dreze_dimare_2024]\] \[[Dutton and Addy 1980][research_dutton_addy_1980]\] \[[Dykas et al 2017][research_dykas_szymanski_2017]\] \[[Eberle 1981][research_eberle_1981]\] \[[Ecer 1985][research_ecer_1985]\] \[[Eldern et al][research_eldern_vos]\] \[[Epstein et al 1989][research_epstein_luntz_1989]\] \[[Erickson et al 1990][research_erickson_schreiner_1990]\] \[[Essawy 1985][research_essawy_1985]\] \[[Euvrard and Tournemine][research_euvrard_tournemine]\] \[[McFadden and Bons][research_evanjmcfadden_jeffreypbons]\] \[[Evans 1987][research_evans_1987]\] \[[Evers 1999][research_evers_1999]\] \[[Evers 2001][research_evers_2001]\] \[[Evers and Peake 1998][research_evers_peake_1998]\] \[[Extension of FLO Codes 1982][research_extension_of_1982]\] \[[Fanning and Mueller 1978][research_fanning_mueller_1978]\] \[[Feldhusen-Hoffmann et al 2017][research_feldhusenhoffmann_statnikov_2017]\] \[[Fernandez et al 2018][research_fernandez_hoffmann_2018]\] \[[Ferrari 1962][research_ferrari_1962]\] \[[Fink 1971][research_fink_1971]\] \[[Fishelov 1988][research_fishelov_1988]\] \[[Fix 1980][research_fix_1980]\] \[[Flores et al 1984][research_flores_holst_1984]\] \[[Forsey 1983][research_forsey_1983]\] \[[Forster and Steijl 2015][research_forster_steijl_2015]\] \[[Francés et al 2024][research_frances_solerarico_2024]\] \[[Friedewald 2020][research_friedewald_2020]\] \[[Friend and Sakamoto 1978][research_friendel_sakamotogm_1978]\] \[[Frolov 2015][research_frolov_2015]\] \[[Fuchs 1981][research_fuchs_1981]\] \[[Fuglsang and Williams 1985][research_fuglsang_williams_1985]\] \[[Fujii and Obayashi 1986][research_fujii_obayashi_1986]\] \[[Fujii and Obayashi 1987][research_fujii_obayashi_1987]\] \[[Fujiwara et al 2016][research_fujiwara_chaparro_2016]\] \[[Fung 1982][research_fung_1982]\] \[[Fung 1982][research_fung_1982_b]\] \[[Fuzaro Miotto and Wolf 2020][research_fuzaromiotto_wolf_2020]\] \[[Gally and Carlson 1987][research_gally_carlson_1987]\] \[[Gao et al 2003][research_gao_luo_2003]\] \[[Gao et al 2017][research_gao_qu_2017]\] \[[Gao et al 2018][research_gao_qu_2018]\] \[[Garabedian 1964][research_garabedian_1964]\] \[[Garabedian 1994][research_garabedian_1994]\] \[[Garabedian and McFadden 1982][research_garabedianp_mcfaddeng_1982]\] \[[Garabedian and McFadden 1982][research_garabedianp_mcfaddeng_1982_b]\] \[[Garnier et al 2009][research_garnier_adams_2009]\] \[[Gatski and Bonnet 2009][research_gatski_bonnet_2009]\] \[[Gatski and Bonnet 2013][research_gatski_bonnet_2013]\] \[[Gatski and Bonnet 2013][research_gatski_bonnet_2013_b]\] \[[Gautam and Prasad 2025][research_gautam_prasad_2025]\] \[[Gebelein 1939][research_gebeleinh_1939]\] \[[Geffen 1978][research_geffen_1978]\] \[[Ghaffari 2005][research_ghaffarifarhad_2005]\] \[[Ghayour and Baysal 1999][research_ghayour_baysal_1999]\] \[[Ghoreyshi et al 2024][research_ghoreyshi_aref_2024]\] \[[Ghoreyshi et al 2025][research_ghoreyshi_aref_2025]\] \[[Gibbings 1966][research_gibbings_1966]\] \[[Gibbons 1992][research_gibbons_1992]\] \[[Gibbons and Batina 1989][research_gibbons_batina_1989]\] \[[Gibbons and Batina 1990][research_gibbons_batina_1990]\] \[[Gilbarg and Shiffman 1954][research_gilbarg_shiffman_1954]\] \[[Gill et al 2016][research_gill_zhang_2016]\] \[[Gilliot et al 2004][research_gilliot_monnier_2004]\] \[[Glauert 1928][research_glauert_1928]\] \[[Glauert 1983][research_glauert_1983]\] \[[Goldberg et al 1985][research_goldberg_gorski_1985]\] \[[Golubev et al 2010][research_golubev_hollenshade_2010]\] \[[Gompertz et al 2012][research_gompertz_jensen_2012]\] \[[Gonzalez et al 2026][research_gonzalez_ilie_2026]\] \[[Goorjian 1984][research_goorjian_1984]\] \[[Goorjian and Buskirk 1985][research_goorjian_buskirk_1985]\] \[[Goorjian et al 1983][research_goorjian_meagher_1983]\] \[[Gopesh. M. P and Manivel. M 2016][research_gopeshmp_manivelm_2016]\] \[[Graham 1948][research_grahamdonaldj_1948]\] \[[Graham 1949][research_grahamdonaldj_1949]\] \[[Graphs of Critical Mach 2014][research_graphs_of_2014]\] \[[Green 2008][research_green_2008]\] \[[Gregg and Misegades 1987][research_gregg_misegades_1987]\] \[[Gross and Steinle 1975][research_grossar_steinlefwjr_1975]\] \[[Grossman and Volpe 1977][research_grossman_volpe_1977]\] \[[Grossman and Volpe 1977][research_grossman_volpe_1977_b]\] \[[Guderley 1956][research_guderley_1956]\] \[[Guderley 1980][research_guderley_1980]\] \[[Guderley 1982][research_guderley_1982]\] \[[Guderley 1983][research_guderley_1983]\] \[[Guderley and Clemm 1979][research_guderley_clemm_1979]\] \[[Guruswamy and Goorjian 1987][research_guruswamy_goorjian_1987]\] \[[Guruswamy and Goorjian 1988][research_guruswamy_goorjian_1988]\] \[[Gülçat 2010][research_gulcat_2010]\] \[[Gülçat 2015][research_gulcat_2015]\] \[[Gülçat 2021][research_gulcat_2021]\] \[[Hacıogˇlu and Özkol 2003][research_hacioglu_ozkol_2003]\] \[[Haderlie and Crossley 2009][research_haderlie_crossley_2009]\] \[[Hafez 1982][research_hafez_1982]\] \[[Hafez 1999][research_hafez_1999]\] \[[Hafez and Cheng 1975][research_hafez_cheng_1975]\] \[[Hafez and Cheng 1977][research_hafez_cheng_1977]\] \[[Hafez and Lovell 1984][research_hafez_lovell_1984]\] \[[Hafez and Wahba][research_hafez_wahba]\] \[[Hafez 1985][research_hafezmm_1985]\] \[[Hager et al 1992][research_hager_eyi_1992]\] \[[Hager et al 1993][research_hager_eyi_1993]\] \[[Hager et al 1994][research_hager_eyi_1994]\] \[[Haglund and Kane 1974][research_haglundgt_kaneej_1974]\] \[[Haines 1990][research_haines_1990]\] \[[Hall et al 2011][research_hall_atassi_2011]\] \[[Hammer and Olivier 2019][research_hammer_olivier_2019]\] \[[Handa et al 2003][research_handa_masuda_2003]\] \[[Hansen 1976][research_hansen_1976]\] \[[Harbeck and Jameson 2005][research_harbeck_jameson_2005]\] \[[Hartwich 1991][research_hartwich_1991]\] \[[Hassan and Sobieczky 1981][research_hassan_sobieczky_1981]\] \[[Hayabe and Kwak 2025][research_hayabe_kwak_2025]\] \[[Held and Fuchs 1998][research_held_fuchs_1998]\] \[[Heltsley et al 1981][research_heltsley_crosswy_1981]\] \[[Henne 1980][research_henne_1980]\] \[[Henne 1981][research_henne_1981]\] \[[Henne and Hicks 1978][research_henne_hicks_1978]\] \[[Henne and Hicks 1978][research_hennepa_hicksrm_1978]\] \[[Herbert 1973][research_herbert_1973]\] \[[Hermes et al 2008][research_hermes_klioutchnikov_2008]\] \[[Hermes et al 2012][research_hermes_nies_2012]\] \[[Hermes et al 2013][research_hermes_klioutchnikov_2013]\] \[[Hess and Gardner 1949][research_hessrobertv_gardnercliffords_1949]\] \[[Hewlett 1987][research_hewlett_1987]\] \[[Hicks 1981][research_hicks_1981]\] \[[Hillenherms et al 2001][research_hillenherms_schroeder_2001]\] \[[Hillenherms et al 2004][research_hillenherms_schroder_2004]\] \[[Hindman 1992][research_hindman_1992]\] \[[Hirose et al 1985][research_hirose_takanashi_1985]\] \[[Hirose et al 1987][research_hirose_takanashi_1987]\] \[[Hitzel 2015][research_hitzel_2015]\] \[[Hitzel 2017][research_hitzel_2017]\] \[[Hitzel 2017][research_hitzel_2017_b]\] \[[Holst 1981][research_holst_1981]\] \[[Holst 1987][research_holst_1987]\] \[[Holst 1988][research_holst_1988]\] \[[Holt 1982][research_holt_1982]\] \[[Hood and Anderson 1942][research_hoodmanleyj_andersonjosephl_1942]\] \[[Hooker 1931][research_hooker_1931]\] \[[Horibata 2001][research_horibata_2001]\] \[[Hou et al 1995][research_hounkateshwar_taylor_1995]\] \[[Houtman et al 2023][research_houtman_timme_2023]\] \[[Hsieh 1975][research_hsieh_1975_b]\] \[[Hsu 1987][research_hsu_1987]\] \[[Hsu 1988][research_hsu_1988]\] \[[Hsu and Liu 1990][research_hsuch_liuch_1990]\] \[[Hu 2023][research_hu_2023]\] \[[Hu and Kandil 1990][research_hu_kandil_1990]\] \[[Hu et al 2018][research_hu_qu_2018]\] \[[Hubbard et al 2011][research_hubbard_mcfarland_2011]\] \[[Huff et al 1987][research_huff_wu_1987]\] \[[Hurley 1975][research_hurley_1975]\] \[[Hurley et al 1975][research_hurleyfx_spaidfw_1975]\] \[[Hybrid Approach to Transonic 1982][research_hybrid_approach_1982]\] \[[Inger and Kayser 1983][research_inger_kayser_1983]\] \[[Integral Equation Method in 1982][research_integral_equation_1982]\] \[[Inverse Airfoil Design A 1990][research_inverse_airfoil_1990]\] \[[Ito and Takanashi 1991][research_ito_takanashi_1991]\] \[[Jacobs et al 2002][research_jacobs_kopriva_2002]\] \[[Blackwell 1969][research_jamesablackwelljr_1969]\] \[[Jameson][research_jameson]\] \[[Jameson][research_jameson_b]\] \[[Jameson 1973][research_jameson_1973]\] \[[Jameson 1977][research_jameson_1977]\] \[[Jameson 1982][research_jameson_1982]\] \[[Jameson and Caughey 1977][research_jameson_caughey_1977]\] \[[Jameson 1979][research_jamesona_1979]\] \[[Jameson and Caughey 1977][research_jamesona_caugheyda_1977]\] \[[Jansen et al 2024][research_jansen_glockner_2024]\] \[[Jansen et al 2025][research_jansen_glockner_2025]\] \[[Jegdi 'c 2019][research_jegdic_2019]\] \[[Jeon et al 2014][research_jeon_kim_2014]\] \[[Jepps 1981][research_jepps_1981]\] \[[Ji and Liu 1996][research_ji_liu_1996]\] \[[Ji et al 2025][research_ji_yang_2025]\] \[[Jiang 2024][research_jiang_2024]\] \[[Jiang et al 2023][research_jiang_wang_2023]\] \[[Jing et al 2025][research_jing_lu_2025]\] \[[Joh et al 1991][research_johcy_grossmanb_1991]\] \[[Johnson 1982][research_johnson_1982]\] \[[Johnson and Bachalo 1978][research_johnson_bachalo_1978]\] \[[Johnson and Bachalo 1980][research_johnson_bachalo_1980]\] \[[Johnson et al 1979][research_johnson_owen_1979]\] \[[Johnston 1992][research_johnston_1992]\] \[[Jokari and Kamali 2025][research_jokari_kamali_2025]\] \[[Jokari and Kamali 2026][research_jokari_kamali_2026]\] \[[Joshi and Thomas 2025][research_joshi_thomas_2025]\] \[[Jou and Metcalfe 1984][research_jou_metcalfe_1984]\] \[[Jou and Mueller 1985][research_jou_mueller_1985]\] \[[Kady and Takahashi 2014][research_kady_takahashi_2014]\] \[[Kafyeke et al 1988][research_kafyeke_piperni_1988]\] \[[Kalkhoran and Sforza 1992][research_kalkhoran_sforza_1992]\] \[[Kalkhoran and Wilson 1992][research_kalkhoran_wilson_1992]\] \[[Kalkhoran et al 1989][research_kalkhoran_wilson_1989]\] \[[Kandil and Hu 1990][research_kandil_hu_1990]\] \[[Kandil et al 1993][research_kandil_kandil_1993]\] \[[Kandil et al 1993][research_kandil_kandil_1993_b]\] \[[Kandil et al 1994][research_kandil_kalisch_1994]\] \[[Kashitani et al 2010][research_kashitani_yamaguchi_2010]\] \[[Kashitani et al 2012][research_kashitani_miura_2012]\] \[[Kashitani et al 2020][research_kashitani_taguchi_2020]\] \[[Kasim Biber and Trenton White 2019][research_kasimbiber_trentonwhite_2019]\] \[[Kaul 2021][research_kaul_2021]\] \[[Kaul 2022][research_kaul_2022]\] \[[Kaya 2025][research_kaya_2025]\] \[[Keener 1984][research_keener_1984]\] \[[Keener 1985][research_keener_1985]\] \[[Kennelly 1983][research_kennellyjr_1983]\] \[[Kerlick et al 1982][research_kerlick_nixon_1982]\] \[[Kerlick et al 1983][research_kerlick_nixon_1983]\] \[[Kerschen and Tsai 1989][research_kerschen_tsai_1989]\] \[[Kesic and Majic 2004][research_kesic_majic_2004]\] \[[Keyfitz and Canic 1998][research_keyfitz_canic_1998]\] \[[Keyfitz et al 1977][research_keyfitz_melnik_1977]\] \[[Keyfitz et al 1978][research_keyfitz_melnik_1978]\] \[[Keyfitz et al 1979][research_keyfitz_melnik_1979]\] \[[Khanal et al 2009][research_khanal_knowles_2009]\] \[[Kholodar et al 2004][research_kholodar_dowell_2004]\] \[[Kim 2006][research_kim_2006]\] \[[Kim and Chokani 1990][research_kim_chokani_1990]\] \[[Kim and Rho 1998][research_kim_rho_1998]\] \[[Kim and Sung 1993][research_kim_sung_1993]\] \[[Kim and Sung 1995][research_kim_sung_1995]\] \[[Kim et al 2012][research_kim_lee_2012]\] \[[Kirkman and Takahashi 2016][research_kirkman_takahashi_2016]\] \[[Kirkman and Takahashi 2017][research_kirkman_takahashi_2017]\] \[[Klevenhusen 1980][research_klevenhusen_1980]\] \[[Klioutchnikov and Olivier 2010][research_klioutchnikov_olivier_2010]\] \[[Klioutchnikov et al 2008][research_klioutchnikov_ballmann_2008]\] \[[Klunker and Newman 1974][research_klunker_newman_1974]\] \[[Klutchnikov and Ballmann 2004][research_klutchnikov_ballmann_2004]\] \[[Kluwick and Cox 2018][research_kluwick_cox_2018]\] \[[Knipfer and Schewe 1999][research_knipfer_schewe_1999]\] \[[Kodigaddi et al 2024][research_kodigaddi_khazi_2024]\] \[[Kojima and Hashimoto 2022][research_kojima_hashimoto_2022]\] \[[Konig et al 2018][research_konig_singh_2018]\] \[[Koziel and Leifsson 2011][research_koziel_leifsson_2011]\] \[[Kraiko 1987][research_kraiko_1987]\] \[[Kraljic and Rusak 2021][research_kraljic_rusak_2021]\] \[[Krenz 1979][research_krenz_1979]\] \[[Kallstrom][research_kristenkallstrom]\] \[[Kumar and Das 1989][research_kumar_das_1989]\] \[[Kumaravel et al 2015][research_kumaravel_jeyajothiraj_2015]\] \[[Kurbatskii and Montanari 2006][research_kurbatskii_montanari_2006]\] \[[Kurosaka et al 1981][research_kurosaka_chou_1981]\] \[[Kurus et al 2021][research_kurus_takahashi_2021]\] \[[Kutler and Lomax 1971][research_kutlerp_lomaxh_1971]\] \[[Kuz'min 2005][research_kuzmin_2005]\] \[[Kuz'min 2006][research_kuzmin_2006]\] \[[Kwon and Vepa 2022][research_kwon_vepa_2022]\] \[[Kwon and Vepa 2022][research_kwon_vepa_2022_b]\] \[[Laitone 1951][research_laitone_1951]\] \[[Lamah and Harris 1983][research_lamah_harris_1983]\] \[[Lan 1989][research_lancedward_1989]\] \[[Landahl 1959][research_landahl_1959]\] \[[Landahl and Rubbert 1966][research_landahl_rubbert_1966]\] \[[Larson 1984][research_larson_1984]\] \[[Lauer and Ansell 2022][research_lauer_ansell_2022]\] \[[Laughrey 1975][research_laughrey_1975]\] \[[Lee 1983][research_lee_1983]\] \[[Lee 1993][research_lee_1993]\] \[[Lee 2012][research_lee_2012]\] \[[Lee and Damodaran 2000][research_lee_damodaran_2000]\] \[[Lee and Damodaran 2001][research_lee_damodaran_2001]\] \[[Lee and Rusak 1999][research_lee_rusak_1999]\] \[[Lee and Rusak 2000][research_lee_rusak_2000]\] \[[Leelavathi and Subramanian 1969][research_leelavathi_subramanian_1969]\] \[[Lefebvre and Zha 2014][research_lefebvre_zha_2014]\] \[[Lefebvre et al 2013][research_lefebvre_dano_2013]\] \[[Lefebvre et al 2016][research_lefebvre_dano_2016]\] \[[Levy 1977][research_levylljr_1977]\] \[[Levy 1981][research_levylljr_1981]\] \[[Li 2023][research_li_2023]\] \[[Li 2024][research_li_2024]\] \[[Li and Ekici 2018][research_li_ekici_2018]\] \[[Li et al 2000][research_li_li_2000]\] \[[Li et al 2004][research_li_krist_2004]\] \[[Li et al 2006][research_li_krist_2006]\] \[[Li et al 2024][research_li_yang_2024]\] \[[Li et al 2024][research_li_zhang_2024]\] \[[Liang and Fung 1985][research_liangsm_fungky_1985]\] \[[Liebeck 1971][research_liebeck_1971]\] \[[Liebhardt 2019][research_liebhardt_2019]\] \[[Lijewski 1987][research_lijewski_1987]\] \[[Lijewski 1988][research_lijewski_1988]\] \[[Lin et al 1997][research_lin_chieng_1997]\] \[[Lindsey 1946][research_lindseywf_1946]\] \[[Liou and Sajben 1980][research_liou_sajben_1980]\] \[[Liu 1983][research_liu_1983]\] \[[Liu 1998][research_liu_1998]\] \[[Liu 2022][research_liu_2022]\] \[[Liu 2023][research_liu_2023]\] \[[Liu and Zha 2016][research_liu_zha_2016]\] \[[Liu et al 2017][research_liu_luo_2017]\] \[[Liu et al 2017][research_liu_yang_2017]\] \[[Liu et al 2021][research_liu_salazar_2021]\] \[[LlEBLEIN and Stockman 1972][research_lleblein_stockman_1972]\] \[[Loewner 2013][research_loewner_2013]\] \[[Loftin and Cohen 1948][research_loftinlaurencek_cohenkenneths_1948]\] \[[Lu et al 2012][research_lu_braun_2012]\] \[[Lucchi 1983][research_lucchi_1983]\] \[[Luo and Bao 1988][research_luo_bao_1988]\] \[[Luo and Wang 1998][research_luo_wang_1998]\] \[[Luo and Wang 1998][research_luo_wang_1998_b]\] \[[Luo et al 1997][research_luo_wang_1997]\] \[[Lutsenko et al 2017][research_lutsenko_serikbay_2017]\] \[[Lutz et al 2023][research_lutz_kleinert_2023]\] \[[Ly et al 2006][research_ly_gear_2006]\] \[[Ly et al 2010][research_ly_norrison_2010]\] \[[Lyrintzis et al 1992][research_lyrintzis_wissink_1992]\] \[[Lürkens et al 2026][research_lurkens_meinke_2026]\] \[[Syed Haseeb 2026][research_m_2026]\] \[[Maeder 1964][research_maeder_1964]\] \[[Magnetohydrodynamic Transonic Flows 1990][research_magnetohydrodynamic_transonic_1990]\] \[[Magnus and Yoshihara 1975][research_magnus_yoshihara_1975]\] \[[Makeich and Kryukov 2018][research_makeich_kryukov_2018]\] \[[Maksymiuk and Pulliam 1987][research_maksymiuk_pulliam_1987]\] \[[Maksymiuk and Watson Viken 1986][research_maksymiukcm_watsonvikensa_1986]\] \[[Maljević et al 2024][research_maljevic_dinulovic_2024]\] \[[Malone et al 1984][research_malone_sankar_1984]\] \[[Mann and Mercer 1986][research_mann_mercer_1986]\] \[[Mann 1979][research_mannmj_1979]\] \[[Manneschmidt et al 2024][research_manneschmidt_ligrani_2024]\] \[[Manokaran et al 2003][research_manokaran_vidya_2003]\] \[[Manwell 1977][research_manwell_1977]\] \[[Marion and Sharma 2025][research_marion_sharma_2025]\] \[[Martin and Lomax 1974][research_martin_lomax_1974]\] \[[Martin et al 2003][research_martinpb_mcalisterkw_2003]\] \[[Masdari et al 2018][research_masdari_talebi_2018]\] \[[Mason 1995][research_mason_1995]\] \[[Mason et al 1978][research_mason_mackenzie_1978]\] \[[Mateer et al 1987][research_mateer_seegmiller_1987]\] \[[Matsuno and Lele 2020][research_matsuno_lele_2020]\] \[[Matsushima and Takanashi 1994][research_matsushima_takanashi_1994]\] \[[Mavriplis and Harris 1986][research_mavriplis_harris_1986]\] \[[Mazumder 2024][research_mazumder_2024]\] \[[McDevitt et al 1975][research_mcdevitt_levyjr_1975]\] \[[McDonald et al 1982][research_mcdonald_shamroth_1982]\] \[[McFadden 1979][research_mcfaddengb_1979]\] \[[Mele et al 2016][research_mele_tognaccini_2016]\] \[[Melson and Streett 1993][research_melsonnduane_streettcraigl_1993]\] \[[Mikhail 1989][research_mikhail_1989_b]\] \[[Miles 1950][research_miles_1950]\] \[[Milholen and Chokani 1994][research_milholen_chokani_1994]\] \[[Milholen and Chokani 1992][research_milholenii_chokani_1992]\] \[[Mineck and Campbell 1993][research_mineckraymonde_campbellrichardl_1993]\] \[[Mineck et al 1994][research_mineckraymonde_campbellrichardl_1994]\] \[[Mitchell and Raghunathan 1994][research_mitchell_raghunathan_1994]\] \[[Mitcheltree et al 1989][research_mitcheltree_hassan_1989]\] \[[Modiano and Murman 1993][research_modianodavidl_murmanearllm_1993]\] \[[Mohan 1991][research_mohan_1991]\] \[[Mokry 1995][research_mokry_1995]\] \[[Morawetz 1987][research_morawetz_1987]\] \[[Moretti and Lippolis 1989][research_moretti_lippolis_1989]\] \[[Morton et al 1997][research_morton_beran_1997]\] \[[Mufti et al 2024][research_mufti_bhaduri_2024]\] \[[Muralidharan et al 2025][research_muralidharan_gilbertraj_2025]\] \[[Murman 1976][research_murman_1976]\] \[[Murray 1979][research_murray_1979]\] \[[Murty 1993][research_murty_1993]\] \[[Stack and Von Doenhoff 1935][research_stack_1935_16_airfoils]\] \[[Stack et al 1939][research_burble_1939_pressures]\] \[[Stack 1939][research_burble_delay_1939]\] \[[Stack 1944][research_burble_delay_1944]\] \[[Equations, tables, and charts 1953][research_naca_1135]\] \[[Nakagawa 1986][research_nakagawa_1986]\] \[[Nakamura 1982][research_nakamura_1982]\] \[[Namba 1968][research_namba_1968]\] \[[Namgoong et al 2002][research_namgoong_crossley_2002]\] \[[Narain 1983][research_narain_1983]\] \[[Ferris 1972][research_supercritical_17pct_1972]\] \[[NASA 1973][research_transonic_2d_1973]\] \[[Barnwell 1974][research_transonic_wingbody_1974]\] \[[Nash et al 1972][research_nashjf_scruggsrm_1972]\] \[[Natarajan 2022][research_natarajan_2022]\] \[[Neil and Verhoff 1982][research_neil_verhoff_1982]\] \[[Ngoc 2020][research_ngoc_2020]\] \[[Nicolaides 1982][research_nicolaides_1982]\] \[[Nietubicz and Sturek 1988][research_nietubicz_sturek_1988]\] \[[Nili Ahmadabadi et al 2013][research_niliahmadabadi_ghadak_2013]\] \[[Nixon 1974][research_nixon_1974]\] \[[Nixon 1979][research_nixon_1979]\] \[[Nixon 1980][research_nixon_1980]\] \[[Nixon and Klopfer 1984][research_nixon_klopfer_1984]\] \[[Nocilla 1972][research_nocilla_1972]\] \[[Nonlinear Green's Function Method 1982][research_nonlinear_green_s_1982]\] \[[Nonomura and Fujii 2007][research_nonomura_fujii_2007]\] \[[Norum and Shearin 1986][research_norum_shearin_1986]\] \[[Ntantis and Xezonakis 2024][research_ntantis_xezonakis_2024]\] \[[On the numerical solution][research_on_the_numerical]\] \[[P. A. Sherar 2011][research_pasherar_2011]\] \[[Balakumar et al][research_pbalakumar_prahladhiyer]\] \[[Paciorri and Sabetta 2003][research_paciorri_sabetta_2003]\] \[[Pandey and Sinha 2024][research_pandey_sinha_2024]\] \[[Pantano and Sarkar 1999][research_pantano_sarkar_1999]\] \[[Pantano and Sarkar 2002][research_pantano_sarkar_2002]\] \[[Pardee and Heaslet 1946][research_pardeeotwayom_heasletmaxa_1946]\] \[[Pathan et al 2017][research_pathan_khan_2017]\] \[[Pehlivanoglu and Yagiz 2011][research_pehlivanoglu_yagiz_2011]\] \[[Peng and Chen 2025][research_peng_chen_2025]\] \[[Peng and Chen 2026][research_peng_chen_2026]\] \[[Perkins et al 1977][research_perkins_jr_1977]\] \[[Peters and Kennedy 1977][research_peters_kennedy_1977]\] \[[Phares 1981][research_phares_1981]\] \[[Phares and Kneile 1976][research_phares_kneile_1976]\] \[[Physical Phenomena Associated with 1989][research_physical_phenomena_1989]\] \[[Pierpont 1975][research_pierpontpk_1975]\] \[[PIV investigation of high 1994][research_piv_investigation_1994]\] \[[Plaban and Takahashi 2021][research_plaban_takahashi_2021]\] \[[Plotkin 1978][research_plotkin_1978]\] \[[Balakumar and Iyer][research_ponnampalambalakumar_prahladhiyer]\] \[[Balakumar et al 2023][research_ponnampalambalakumar_prahladhiyer_2023]\] \[[Poole et al 2026][research_poole_allen_2026]\] \[[Potential Equation Methods for 1982][research_potential_equation_1982]\] \[[Potter 1984][research_potter_1984]\] \[[PrabhakaraRao and Sri Sampath. 2014][research_prabhakararao_v_2014]\] \[[Probstein 1953][research_probstein_1953]\] \[[Pröbsting et al 2022][research_probsting_yang_2022]\] \[[Puentes and Takahashi 2024][research_puentes_takahashi_2024]\] \[[Purvis and Burkhalter 1979][research_purvis_burkhalter_1979]\] \[[Puthisikamani et al 2023][research_puthisikamani_sreenivasaraja_2023]\] \[[Quagliarella and Dell 1994][research_quagliarella_dell_1994]\] \[[Quasi-transonic Flow 1986][research_quasi_transonic_flow_1986]\] \[[Lock 1990][research_rclock_1990]\] \[[Rahman et al 2015][research_rahman_hasan_2015]\] \[[Rahman et al 2015][research_rahman_labib_2015]\] \[[Rahman et al 2025][research_rahman_vowotor_2025]\] \[[Raj 1983][research_raj_1983]\] \[[Raj 1984][research_raj_1984]\] \[[Raj and Brennan 1987][research_raj_brennan_1987]\] \[[Ramamurthy and Ghaly 2009][research_ramamurthy_ghaly_2009]\] \[[Ramm 1990][research_ramm_1990_d]\] \[[Ramm 1990][research_ramm_1990_e]\] \[[Rasuo 2006][research_rasuo_2006]\] \[[Ratcliff and Carlson 1989][research_ratcliff_carlson_1989]\] \[[Raveh 2008][research_raveh_2008]\] \[[Redeker et al 1986][research_redeker_wichmann_1986]\] \[[Redford et al 2012][research_redford_sandham_2012]\] \[[Richter and Rosemann 2011][research_richter_rosemann_2011]\] \[[Rill and Becker 1992][research_rill_becker_1992]\] \[[Rivers and Wahls 1994][research_riversmelissab_wahlsricharda_1994]\] \[[Rizzetta 1977][research_rizzetta_1977_b]\] \[[Rizzetta and Yoshihara 1980][research_rizzetta_yoshihara_1980]\] \[[Rizzi 1981][research_rizzi_1981]\] \[[Rizzi 1981][research_rizzi_1981_b]\] \[[Rizzi 1982][research_rizzi_1982]\] \[[Rizzi 1985][research_rizzi_1985]\] \[[Rizzi 1995][research_rizzi_1995]\] \[[Rizzi and Eriksson 1981][research_rizzi_eriksson_1981]\] \[[Rizzi et al 1986][research_rizzi_purcell_1986]\] \[[Robinson 1978][research_robinson_1978]\] \[[Rodarte Ricciardi and Wolf 2020][research_rodartericciardi_wolf_2020]\] \[[Rodarte Ricciardi et al 2021][research_rodartericciardi_wolf_2021]\] \[[Rodriguez et al 2022][research_rodriguez_hickey_2022]\] \[[Roidl et al 2011][research_roidl_meinke_2011]\] \[[Roohani and Skews 2009][research_roohani_skews_2009]\] \[[Roos and Riddle 1977][research_roosfw_riddledw_1977]\] \[[Rose and Seginer 1977][research_rose_seginer_1977]\] \[[Rose and Seginer 1978][research_rose_seginer_1978]\] \[[Rosemann and Birkemeyer 2002][research_rosemann_birkemeyer_2002]\] \[[Rosen 1984][research_rosen_1984]\] \[[Rosen 1985][research_rosen_1985]\] \[[Ross 1987][research_rossdavids_1987]\] \[[Roy et al 2021][research_roy_das_2021]\] \[[Rumsey et al 1987][research_rumsey_thomas_1987]\] \[[Rusak 1993][research_rusak_1993]\] \[[Rusak 1994][research_rusak_1994]\] \[[Rusak and Webster 1992][research_rusak_webster_1992]\] \[[Russo et al 2020][research_russo_tognaccini_2020]\] \[[Sahu 1988][research_sahu_1988]\] \[[Sahu 1990][research_sahu_1990]\] \[[Sahu 2007][research_sahu_2007]\] \[[Sahu 2009][research_sahu_2009]\] \[[Sahu 2011][research_sahu_2011]\] \[[Sahu and Danberg 1987][research_sahu_danberg_1987]\] \[[Sahu and Heavey 1995][research_sahu_heavey_1995]\] \[[Sahu et al 1982][research_sahu_nietubicz_1982]\] \[[Sahu et al 1983][research_sahu_nietubicz_1983]\] \[[Sahu et al 1983][research_sahu_nietubicz_1983_b]\] \[[Sajben and Kroutil 1979][research_sajben_kroutil_1979]\] \[[Sajben et al 1982][research_sajben_bogar_1982]\] \[[Sakurai 1959][research_sakurai_1959]\] \[[Samant and Wigton 1983][research_samant_wigton_1983]\] \[[Samputh et al 2024][research_samputh_moey_2024]\] \[[Sangwan et al 2017][research_sangwan_sengupta_2017]\] \[[Sankar and Tassa 1981][research_sankar_tassa_1981]\] \[[Sankar et al 1985][research_sankar_malone_1985]\] \[[Sarkar 1994][research_sarkar_1994]\] \[[Sashida et al 2026][research_sashida_kawai_2026]\] \[[Schaechterle et al 1982][research_schaechterleg_ludewigkh_1982]\] \[[Schiavetta et al 2006][research_schiavetta_boelens_2006]\] \[[Schmidt 1979][research_schmidt_1979]\] \[[Schmitt et al 1983][research_schmitt_destarac_1983]\] \[[Schoolfield 1942][research_schoolfield_1942]\] \[[Schouten and Bakker 2000][research_schouten_bakker_2000]\] \[[Schröder and Meijering 2005][research_schroder_meijering_2005]\] \[[Seebass 1982][research_seebass_1982]\] \[[Seebass and Yu 1976][research_seebassar_yunj_1976]\] \[[Seegmiller et al 1978][research_seegmillerhl_marvinjg_1978]\] \[[Seginer and Rose 1977][research_seginer_rose_1977]\] \[[Sellers and Chandra 1997][research_sellers_chandra_1997]\] \[[Sevost'ianow 1967][research_sevostianow_1967]\] \[[Shahrokhi and Jahangirian 2010][research_shahrokhi_jahangirian_2010]\] \[[Shankar and Goebel 1985][research_shankar_goebel_1985]\] \[[Shankar and Malmuth 1982][research_shankar_malmuth_1982]\] \[[Shankar et al 1979][research_shankar_malmuth_1979]\] \[[Shankar et al 1979][research_shankar_malmuth_1979_b]\] \[[Shao et al 2026][research_shao_he_2026]\] \[[Sheng et al 2007][research_sheng_galbraith_2007]\] \[[Shimada et al 2009][research_shimada_shiratori_2009]\] \[[Shmikovich and Caughey 1981][research_shmikovicha_caugheyda_1981]\] \[[Shmilovich and Caughey 1982][research_shmilovich_caughey_1982]\] \[[Shubham et al 2022][research_shubham_sandberg_2022]\] \[[Siclari et al 1996][research_siclari_vannostrand_1996]\] \[[Siclari 1982][research_siclarimj_1982]\] \[[Silva and Bennett 1995][research_silva_bennett_1995]\] \[[Sinaga et al 2024][research_sinaga_yunianto_2024]\] \[[Sinclair 1988][research_sinclair_1988]\] \[[Sinha 2024][research_sinha_2024]\] \[[Small-Disturbance Theory 1959][research_small_disturbance_theory_1959]\] \[[Snyder 1987][research_snyder_1987]\] \[[Sobieczky 1979][research_sobieczky_1979]\] \[[Sobieczky 1984][research_sobieczky_1984]\] \[[Sobieczky and Dulikravich 1993][research_sobieczky_dulikravich_1993]\] \[[Sogukpinar 2018][research_sogukpinar_2018]\] \[[Sohn and Lee 2000][research_sohn_lee_2000]\] \[[Solution of the Transonic 2014][research_solution_of_2014]\] \[[Soontornpasatch 2018][research_soontornpasatch_2018]\] \[[Soontornpasatch 2018][research_soontornpasatch_2018_b]\] \[[South 1985][research_southjr_1985]\] \[[Souza Coimbra et al 2022][research_souzacoimbra_matoscampos_2022]\] \[[Spinner and Rudnik 2023][research_spinner_rudnik_2023]\] \[[Spreiter 1964][research_spreiter_1964]\] \[[Srinivasan et al 1981][research_srinivasan_chyu_1981]\] \[[Srinivasan et al 1984][research_srinivasan_mccroskey_1984]\] \[[Srinivasan et al 1986][research_srinivasan_mccroskey_1986]\] \[[Srinivasan and Steger 1981][research_srinivasang_stegerjl_1981]\] \[[Stack 1935][research_stack_1935_burble]\] \[[Stack 1943][research_stackjohn_1943]\] \[[Stack et al 1950][research_stackjohn_draleyeugenec_1950]\] \[[Stahara 1981][research_stahara_1981]\] \[[Steady Transonic Flow 2015][research_steady_transonic_2015]\] \[[Stebbins et al 2019][research_stebbins_loth_2019]\] \[[Steelant 2002][research_steelant_2002]\] \[[Steger and Klineberg 1973][research_steger_klineberg_1973]\] \[[Steimle et al 2012][research_steimle_karhoff_2012]\] \[[Corda and Vachon 2003][research_stephencorda_michaeljakevachon_2003]\] \[[Strampp 1983][research_strampp_1983]\] \[[Street 1979][research_street_1979]\] \[[Streett 1981][research_streett_1981]\] \[[Streett 1982][research_streett_1982]\] \[[Streett 1983][research_streett_1983]\] \[[Studwell and Wu 1973][research_studwell_wu_1973]\] \[[Sturek and Schiff 1980][research_sturek_schiff_1980]\] \[[Sudani et al 1993][research_sudani_sato_1993]\] \[[Sugioka et al 2018][research_sugioka_nakakita_2018]\] \[[Sun][research_sun]\] \[[Sun et al 2021][research_sun_wang_2021]\] \[[Sundaram and Wu 1983][research_sundaram_wu_1983]\] \[[Supercritical airfoil design][research_supercritical_airfoil]\] \[[Tai 1986][research_tai_1986]\] \[[Tai and Kidwell 1985][research_tai_kidwell_1985]\] \[[Tai and Kidwell 1984][research_tai_kidwelljr_1984]\] \[[Tai et al 1987][research_taitszec_husongregoryg_1987]\] \[[Takanashi 1984][research_takanashi_1984]\] \[[Takanashi 1985][research_takanashi_1985]\] \[[Takovitskii 2016][research_takovitskii_2016]\] \[[Tam 1989][research_tam_1989]\] \[[Tamba et al 2017][research_tamba_tuan_2017]\] \[[Tan et al 2024][research_tan_xu_2024]\] \[[Tang and Tan 2023][research_tang_tan_2023]\] \[[Tang et al 2000][research_tang_jiang_2000]\] \[[Tang et al 2003][research_tang_liu_2003]\] \[[Tao et al 2016][research_tao_li_2016]\] \[[Tao et al 2018][research_tao_zhao_2018]\] \[[Thivet et al 1999][research_thivet_saintmartin_1999]\] \[[Thomas and Agarwal 2022][research_thomas_agarwal_2022]\] \[[Thomas and Agarwal 2025][research_thomas_agarwal_2025]\] \[[Thomas and Holst 1983][research_thomas_holst_1983]\] \[[Thompson and Epstein 1977][research_thompson_epstein_1977]\] \[[Titus et al 2013][research_titus_alexander_2013]\] \[[Tomita 1959][research_tomita_1959]\] \[[Tourrette 1996][research_tourrette_1996]\] \[[Trailing Edge Circulation Control 2006][research_trailing_edge_2006]\] \[[Tranen 1974][research_tranen_1974]\] \[[Transonic Airfoil Design by 2011][research_transonic_airfoil_2011]\] \[[Transonic Airfoil Shape Design 2015][research_transonic_airfoil_2015]\] \[[Transonic Airfoil Theory 1986][research_transonic_airfoil_1986]\] \[[Transonic Computational Experience for 1982][research_transonic_computational_1982]\] \[[Transonic Design Using Computational 1982][research_transonic_design_1982]\] \[[Transonic Maneuver/Cruise Airfoil Design 1980][research_transonic_maneuver_cruise_1980]\] \[[Transonic Navier-Stokes flow computations 1972][research_transonic_navier_stokes_1972]\] \[[Transonic regular reﬂection for 2007][research_transonic_regular_2007]\] \[[Transonic Wing Shape Design 2015][research_transonic_wing_2015]\] \[[Transonic, Shock, and Multidimensional 1982][research_transonic_shock_1982]\] \[[Trefny 2020][research_trefny_2020]\] \[[Trenker 2003][research_trenker_2003]\] \[[Trenker et al 2000][research_trenker_geissler_2000]\] \[[Tsien 2012][research_tsien_2012]\] \[[Tsien and Kuo 2012][research_tsien_kuo_2012]\] \[[Tsien 1944][research_tsienhsueshen_1944]\] \[[Turner et al 2025][research_turner_seo_2025]\] \[[Tursi 2003][research_tursi_2003]\] \[[v. Krzywoblocki 1960][research_vkrzywoblocki_1960]\] \[[Van Der Vooren et al 1982][research_vandervooren_vanderkolk_1982]\] \[[Varwig 1963][research_varwig_1963]\] \[[Vatsa 1987][research_vatsa_1987]\] \[[Vavalle and Qin 2007][research_vavalle_qin_2007]\] \[[Veldman 2005][research_veldman_2005]\] \[[Velkova 2017][research_velkova_2017]\] \[[Verhoff 2005][research_verhoff_2005]\] \[[Vicini et al 1997][research_vicini_quagliarella_1997]\] \[[Viegas and Rubesin 1991][research_viegas_rubesin_1991]\] \[[Viegas and Rubesin 1992][research_viegas_rubesin_1992]\] \[[Vikramaditya and Viji 2023][research_vikramaditya_viji_2023]\] \[[Visbal 1988][research_visbal_1988]\] \[[Vishwanathan][research_vishwanathan]\] \[[Volpe 1986][research_volpe_1986]\] \[[Volpe and Grossman 1978][research_volpe_grossman_1978]\] \[[Von Doenhoff et al 1947][research_vondoenhoffalberte_stiverslouiss_1947]\] \[[Vos and Farokhi 2015][research_vos_farokhi_2015]\] \[[Vos and Vaessen 2013][research_vos_vaessen_2013]\] \[[Waggoner 1980][research_waggoner_1980]\] \[[Walitt et al 1977][research_walitt_king_1977]\] \[[Walitt and Liu 1976][research_walittl_liucy_1976]\] \[[Walkden 1958][research_walkden_1958]\] \[[Wallace and Monk 1966][research_wallace_monk_1966]\] \[[Wang and Andreopoulos 2003][research_wang_andreopoulos_2003]\] \[[Wang and Andreopoulos 2009][research_wang_andreopoulos_2009]\] \[[Wang and Luo][research_wang_luo]\] \[[Wang and Rusak 2001][research_wang_rusak_2001]\] \[[Wang and Zha 2019][research_wang_zha_2019]\] \[[Wang et al 2002][research_wang_damodaran_2002]\] \[[Wang et al 2011][research_wang_chen_2011]\] \[[Wang et al 2022][research_wang_qu_2022]\] \[[Watts et al 1988][research_wattsmichaele_crossjeffreyl_1988]\] \[[Weatherill and Ehlers 1989][research_weatherillwarrenh_ehlersfedward_1989]\] \[[Weed et al 1983][research_weed_carlson_1983]\] \[[Weed et al 1984][research_weed_carlson_1984]\] \[[Whitcomb and Clark 1965][research_whitcomb_clark_1965]\] \[[Whitcomb 1974][research_whitcombrt_1974]\] \[[Whitcomb 1976][research_whitcombrt_1976]\] \[[Whitfield and Jameson 1983][research_whitfield_jameson_1983]\] \[[Whitfield and Thompson 1989][research_whitfield_thompson_1989]\] \[[Whitlow and Seidel 1985][research_whitlow_seidel_1985]\] \[[Wigley 1988][research_wigleydavida_1988]\] \[[Williams 1979][research_williams_1979]\] \[[Williams 1980][research_williams_1980]\] \[[Williams and Kesling 1980][research_williams_kesling_1980]\] \[[Williams et al 1985][research_williams_bland_1985]\] \[[Wilson et al 1987][research_wilson_kalkhoran_1987]\] \[[Wissink et al 1995][research_wissink_lyrintzis_1995]\] \[[Woan and Chakravarthy 1988][research_woan_chakravarthy_1988]\] \[[Wolf et al 2014][research_wolf_azevedo_2014]\] \[[Wood and Conlon 1983][research_wood_conlon_1983]\] \[[Wooden et al 2007][research_wooden_smith_2007]\] \[[Woolard 1980][research_woolard_1980]\] \[[Xia et al 1993][research_xia_zhu_1993]\] \[[Xing and Damodaran 2003][research_xing_damodaran_2003]\] \[[Xiong and Nguyen 2023][research_xiong_nguyen_2023_c]\] \[[Xiong et al 2019][research_xiong_fugate_2019]\] \[[Xiong et al 2020][research_xiong_fugate_2020]\] \[[Xu and Yin 2008][research_xu_yin_2008]\] \[[Xue et al 2024][research_xue_feng_2024]\] \[[Xue et al 2025][research_xue_feng_2025]\] \[[Yang et al 2025][research_yang_wu_2025]\] \[[Yee et al 1997][research_yee_lee_1997]\] \[[Yee et al 1998][research_yee_lee_1998]\] \[[Yeom and Chang 2012][research_yeom_chang_2012]\] \[[Yu 1979][research_yu_1979]\] \[[Yu 1980][research_yu_1980]\] \[[Yu 1981][research_yu_1981]\] \[[Yu and Campbell 1992][research_yu_campbell_1992]\] \[[Yu et al 2025][research_yu_zhou_2025]\] \[[Zahir and Gao 2013][research_zahir_gao_2013]\] \[[Zauner et al 2018][research_zauner_detullio_2018]\] \[[Zeigler and Drew 1985][research_zeigler_drew_1985]\] \[[Zhang et al 1988][research_zhang_yang_1988]\] \[[Zhang et al 1990][research_zhang_yu_1990]\] \[[Zhang et al 2017][research_zhang_shan_2017]\] \[[Zhang et al 2021][research_zhang_zou_2021]\] \[[Zhao 1988][research_zhao_1988]\] \[[Zhao et al 2013][research_zhao_ren_2013]\] \[[Zhou 1994][research_zhou_1994]\] \[[Zhou et al 2026][research_zhou_ji_2026]\] \[[Zhu et al 1992][research_zhu_xia_1992]\] \[[Zhu et al 1994][research_zhu_xia_1994]\] \[[Zi-qiang and Xue-Song 1992][research_ziqiang_xuesong_1992]\] \[[Zigangareyeva and Kiselev 1997][research_zigangareyeva_kiselev_1997]\] \[[Zimper and Rein 2014][research_zimper_rein_2014]\] \[[Zores 1995][research_zores_1995]\] \[[Zuosheng 1986][research_zuosheng_1986]\] \[[Čanić and Keyfitz 1996][research_canic_keyfitz_1996]\] \[[Čanić et al 2000][research_canic_keyfitz_2000]\] \[[Čanić et al 2001][research_canic_kim_2001]\]

### Ground test methods, the transonic tunnel and the free-fall body

**The instruments that could not reach the band in 1947, and those that later did.** Transonic tunnel design and calibration, slotted, perforated and adaptive walls, wall interference and blockage corrections, and the free-fall and rocket-model methods. **Walls, interference or blockage are the subject of 219 of the 546 titles**, which is the measure of how much of transonic ground testing became a problem of correcting the tunnel rather than of testing the model.

**546 records.** \[[A predictive controller for 1991][research_a_predictive_1991]\] \[[Abdel-Fattah and Link 1992][research_abdelfattah_link_1992]\] \[[Abele and Sanlorenzo 1975][research_abele_sanlorenzo_1975]\] \[[Abele et al 1973][research_abele_ruger_1973]\] \[[Adams and Rubin 1958][research_adams_rubin_1958]\] \[[Adcock et al 1975][research_adcock_kilgore_1975]\] \[[Agarwal et al 1992][research_agarwal_miley_1992]\] \[[Agrell et al 1987][research_agrell_pettersson_1987]\] \[[Al-Saadi 1993][research_alsaadijassima_1993]\] \[[Al-Saadi and Dejarnette 1992][research_alsaadijassima_dejarnettefredr_1992]\] \[[Alexander et al 1975][research_alexander_griffin_1975]\] \[[An experimental and computational 1978][research_an_experimental_1978]\] \[[Anderson et al 1970][research_anderson_anderson_1970]\] \[[Arnaiz et al 1980][research_arnaizhh_petersonjbjr_1980]\] \[[Arney et al 1963][research_arney_gd_1963]\] \[[Arney et al 1964][research_arney_georged_1964]\] \[[Asim et al 2022][research_asim_masud_2022]\] \[[Asymptotic methods for the 1991][research_asymptotic_methods_1991]\] \[[Austin 1966][research_austin_1966]\] \[[Bailey and Miller 1981][research_bailey_miller_1981]\] \[[Balakrishna 1989][research_balakrishnas_1989]\] \[[Bamber 1961][research_bamber_1961]\] \[[Barnes 1965][research_barnes_og_1965]\] \[[Barnwell et al 1986][research_barnwell_edwards_1986]\] \[[Barnwell 1976][research_barnwellrw_1976_b]\] \[[Barnwell et al 1979][research_barnwellrw_sewallwg_1979]\] \[[Barrows 2006][research_barrowsdannya_2006]\] \[[Begnini et al 2018][research_begnini_bones_2018]\] \[[Belesiotis-Kataras and Timme 2020][research_belesiotiskataras_timme_2020]\] \[[Belesiotis-Kataras and Timme 2021][research_belesiotiskataras_timme_2021]\] \[[Bell 1963][research_bell_1963]\] \[[Belligoli et al 2019][research_belligoli_dwight_2019]\] \[[Belligoli et al 2019][research_belligoli_dwight_2019_b]\] \[[Belligoli et al 2021][research_belligoli_dwight_2021]\] \[[Bengelink et al 1986][research_bengelink_doerzbacher_1986]\] \[[Berndt 1964][research_berndt_1964]\] \[[Berndt 1976][research_berndt_1976]\] \[[Bhat et al 1990][research_bhatmk_vakiliad_1990]\] \[[Bies 1966][research_bies_1966]\] \[[Billingsley 1976][research_billingsley_1976]\] \[[Binion 1974][research_binion_jr_1974]\] \[[Binion and Lo 1970][research_binion_lo_1970]\] \[[Binion 1971][research_binion_tw_1971]\] \[[Binion 1975][research_binion_tw_1975]\] \[[Binion 1976][research_binion_tw_1976]\] \[[Binion 1969][research_binionjr_1969]\] \[[Binion and Lo 1972][research_binionjr_lo_1972]\] \[[Blackwell 1979][research_blackwell_1979]\] \[[Blackwell and Pounds 1977][research_blackwell_pounds_1977]\] \[[Blackwell 1978][research_blackwelljr_1978]\] \[[Blaha 1969][research_blaha_1969]\] \[[Blanco et al 2019][research_blanco_battiato_2019]\] \[[Bliss 1980][research_bliss_1980]\] \[[Boiarski and Daum 1972][research_boiarski_daum_1972]\] \[[Boppe 1977][research_boppe_1977]\] \[[Borden 1930][research_borden_1930]\] \[[Boutemedjet et al 2018][research_boutemedjet_samardzic_2018]\] \[[Boylan 1963][research_boylan_1963]\] \[[Brady et al 1954][research_brady_maier_1954]\] \[[Hiller et al][research_brettrhiller_richardlcampbell]\] \[[Hiller et al][research_brettrhiller_richardlcampbell_b]\] \[[Brion et al 2026][research_brion_rembaut_2026]\] \[[Britcher and Landman 2024][research_britcher_landman_2024]\] \[[Brooks et al 1980][research_brooks_stainback_1980]\] \[[Brooks et al 1994][research_brookscuylerwjr_harrischarlesd_1994]\] \[[Broughton et al 1995][research_broughton_rainbird_1995]\] \[[Browne 1990][research_browne_1990]\] \[[Burghiu 2023][research_burghiu_2023]\] \[[Burrin et al 1986][research_burrin_salikuddin_1986]\] \[[Butler 1976][research_butler_1976]\] \[[Bynum et al 1970][research_bynum_ledford_1970]\] \[[Cahill et al 2010][research_cahill_minter_2010]\] \[[Cain 1979][research_cain_1979]\] \[[Capone 1975][research_capone_1975]\] \[[Carden 1963][research_carden_1963]\] \[[Carr et al 1998][research_carr_chandrasekhara_1998]\] \[[Carter 1988][research_carter_1988]\] \[[Castro et al 2000][research_castro_ekaterinaris_2000]\] \[[Castro et al 2001][research_castro_jones_2001]\] \[[Castro et al 2002][research_castro_ekaterinaris_2002]\] \[[Castro et al 2003][research_castro_jones_2003]\] \[[Chan 1980][research_chan_1980]\] \[[Chan 1980][research_chan_1980_b]\] \[[Chan 1985][research_chan_1985]\] \[[Chau et al 2026][research_chau_piotrowski_2026]\] \[[Chen et al 2024][research_chen_wang_2024]\] \[[Cheng et al 2015][research_cheng_lowenberg_2015]\] \[[Chevalier 1960][research_chevalier_1960]\] \[[Chew 1953][research_chew_1953]\] \[[Chew 1955][research_chew_1955]\] \[[Chung et al 1994][research_chung_miau_1994]\] \[[Chung et al 1995][research_chung_miau_1995]\] \[[Chwalowski et al 2016][research_chwalowskipawel_quoneliot_2016]\] \[[Clemens and Cortner 1963][research_clemens_cortner_1963]\] \[[Cole and Malmuth 1982][research_cole_malmuth_1982]\] \[[Cole et al 2003][research_cole_noll_2003]\] \[[Collazo Garcia and Ansell 2019][research_collazogarcia_ansell_2019]\] \[[Comparison of Aircraft Noise 1975][research_comparison_of_1975]\] \[[Cook and Schleiniger 1993][research_cook_schleiniger_1993]\] \[[Cook 1978][research_cookwj_1978]\] \[[Cooksey et al 1964][research_cooksey_dillenschneider_1964]\] \[[Coppin et al 2025][research_coppin_martin_2025]\] \[[Couch 1972][research_couch_1972]\] \[[Coulton][research_coulton]\] \[[Covert and Haldeman 1978][research_covert_haldeman_1978]\] \[[Crafton et al 2004][research_crafton_elliott_2004]\] \[[Crain et al 1965][research_crain_brown_1965]\] \[[Crites et al 1992][research_crites_rueger_1992]\] \[[Crowder et al 1998][research_crowder_amiryants_1998]\] \[[Crozier et al 2014][research_crozier_chargy_2014]\] \[[Cumming and Lowe 1971][research_cumming_lowe_1971]\] \[[Cunningham and Den Boer 1992][research_cunninghamjr_denboer_1992]\] \[[Czysz 1963][research_czysz_1963]\] \[[David and Hale 1978][research_david_hale_1978]\] \[[Davis 2019][research_davis_2019]\] \[[DeLoach 2012][research_deloach_2012]\] \[[DeLoach 2014][research_deloach_2014]\] \[[Denham and Owens 2016][research_denham_owens_2016]\] \[[Dick 1955][research_dick_1955]\] \[[Diggins 1951][research_diggins_1951]\] \[[Dittmar 1989][research_dittmar_1989]\] \[[Dix and Mattasits 1980][research_dix_mattasits_1980]\] \[[Djomehri et al 1995][research_djomehrimjahed_buningpieterg_1995]\] \[[Dods and Hanly 1972][research_dodsjr_hanly_1972]\] \[[Dodson 2005][research_dodson_2005]\] \[[Doig et al 2013][research_doig_bogdan_2013]\] \[[Doria and South 1982][research_doria_southjr_1982]\] \[[Dougherty 1977][research_dougherty_ns_1977]\] \[[Dougherty et al 1975][research_dougherty_ns_1975]\] \[[Dowell and Bliss 1978][research_dowell_bliss_1978]\] \[[Draper and Moran 1973][research_draper_moran_1973]\] \[[Drela 2022][research_drela_2022]\] \[[Dupuis 1988][research_dupuis_1988]\] \[[Duraisamy et al 2006][research_duraisamy_mccroskey_2006]\] \[[Edwards 2009][research_edwards_2009]\] \[[Edwards 1997][research_edwardsjohnw_1997]\] \[[Englar 1970][research_englar_1970]\] \[[Epstein and Albers 1948][research_epstein_albers_1948]\] \[[Erickson 1991][research_ericksongarye_1991]\] \[[Everhart 1986][research_everhart_1986]\] \[[Everhart 1987][research_everhart_1987]\] \[[Everhart and Barnwell 1978][research_everhart_barnwell_1978]\] \[[Everhart and Barnwell 1978][research_everhartjl_barnwellrw_1978]\] \[[Everhart 1987][research_everhartjoell_1987]\] \[[Everhart and Goradia 1991][research_everhartjoell_goradiasureshh_1991]\] \[[Eversman 1989][research_eversman_1989]\] \[[Fejtek 1994][research_fejtek_1994]\] \[[Ferri and Baronti 1973][research_ferri_baronti_1973]\] \[[Fischer 2018][research_fischer_2018]\] \[[Fisher et al 1990][research_fisher_banks_1990]\] \[[Franzmann et al 2022][research_franzmann_leopold_2022]\] \[[Freestone and Henington 1982][research_freestone_henington_1982]\] \[[Fukami et al 2004][research_fukami_higashino_2004]\] \[[Gallington and Miller 1970][research_gallington_miller_1970]\] \[[Galyen et al 2014][research_galyen_mills_2014]\] \[[Gao et al 2025][research_gao_tyrrell_2025]\] \[[Gardenier 1956][research_gardenier_1956]\] \[[Garrell 2002][research_garrell_2002]\] \[[Garriz et al 1990][research_garriz_newman_1990]\] \[[Ghazi 1993][research_ghazi_1993]\] \[[Gillard 1998][research_gillard_1998]\] \[[Gillard 1999][research_gillard_1999]\] \[[Gilliam 1976][research_gilliam_1976]\] \[[Glazkov and Semenov 2024][research_glazkov_semenov_2024]\] \[[Glezer 2009][research_glezer_2009]\] \[[Glezer 2012][research_glezer_2012]\] \[[Glowacki 1971][research_glowacki_1971]\] \[[Goenka 1994][research_goenka_1994]\] \[[Goethert 1956][research_goethert_1956]\] \[[Goethert and Lukasiewicz 1963][research_goethert_lukasiewicz_1963]\] \[[Goffert et al 2014][research_goffert_ortega_2014]\] \[[Goffert et al 2015][research_goffert_ortega_2015]\] \[[Goffert et al 2016][research_goffert_ortega_2016]\] \[[Golestani et al 2017][research_golestani_soltani_2017]\] \[[Goodman 1973][research_goodman_1973]\] \[[Goodyear Aerospace Corp Akron Oh 1958][research_goodyearaerospacecorpakronoh_1958]\] \[[Goodyer and Wolf 1980][research_goodyer_wolf_1980]\] \[[Grant and Sevier 1960][research_grantfrederickc_sevierjohnrjr_1960]\] \[[Green and Newman 1987][research_greenlawrencel_newmanperrya_1987]\] \[[Green and Newman 1991][research_greenlawrencel_newmanperrya_1991]\] \[[Greenwell 2021][research_greenwell_2021]\] \[[Griffiths and Visser 2000][research_griffiths_visser_2000]\] \[[Grunnet 1984][research_grunnet_1984]\] \[[Guangyuan et al 2021][research_guangyuan_dawei_2021]\] \[[Gumbert and Newman 1984][research_gumbert_newman_1984]\] \[[Gumbert et al 1989][research_gumbertclyder_greenlawrencel_1989]\] \[[Gunn 1966][research_gunn_1966]\] \[[Gunn 1970][research_gunn_1970]\] \[[Hall 1978][research_hall_1978]\] \[[Hall 1985][research_hall_1985]\] \[[Hall 1978][research_hallrm_1978]\] \[[Haney et al 1979][research_haney_johnson_1979]\] \[[Hartley and Jacocks 1968][research_hartley_jacocks_1968]\] \[[Hartmann 2012][research_hartmann_2012]\] \[[Hartmann 2013][research_hartmann_2013]\] \[[Harun and Amer Abbas 2024][research_harun_amerabbas_2024]\] \[[Hashimoto et al 2010][research_hashimoto_aoyama_2010]\] \[[Hashimoto et al 2011][research_hashimoto_kohzai_2011]\] \[[Hastings 1954][research_hastings_1954]\] \[[Hawke 2026][research_hawke_2026]\] \[[Hawthorne 1976][research_hawthornepj_1976]\] \[[Heidebrecht 2006][research_heidebrecht_2006]\] \[[Heidebrecht 2013][research_heidebrecht_2013]\] \[[Heim 1991][research_heim_1991]\] \[[Hemsch and Iyer 2004][research_hemschmichaelj_iyervenkit_2004]\] \[[Hendershot 1968][research_hendershot_1968]\] \[[Hendershot 1969][research_hendershot_1969]\] \[[Hensel 1964][research_hensel_1964]\] \[[Hergert and Bengelink 1984][research_hergert_bengelink_1984]\] \[[Hergert et al 2001][research_hergert_smith_2001]\] \[[Hermann 1950][research_hermann_1950]\] \[[Heyson 1961][research_heyson_1961]\] \[[Hieser et al 1956][research_hiesergerald_kudlaciklouis_1956]\] \[[Hiller et al 2021][research_hiller_campbell_2021]\] \[[Hillje and Tymms 1978][research_hillje_tymms_1978]\] \[[Hindash and Spaid 1991][research_hindash_spaid_1991]\] \[[Hoe et al 2012][research_hoe_owens_2012]\] \[[Holder 1963][research_holder_1963]\] \[[Holst and Bock][research_holst_bock]\] \[[Holst and Thomas 1982][research_holst_thomas_1982]\] \[[Honaker 1982][research_honakerwc_1982]\] \[[Hong et al 1995][research_hong_ahn_1995]\] \[[Hortsen et al 1983][research_hortsen_boer_1983]\] \[[Howard and Bray 1992][research_howard_bray_1992]\] \[[Hu 1992][research_hu_1992]\] \[[Hu 1995][research_hu_1995]\] \[[Huang et al 2026][research_huang_liang_2026]\] \[[Hwang and Park 2026][research_hwang_park_2026]\] \[[Investigation of flexible nozzle 1979][research_investigation_of_1979]\] \[[Iwai et al 2019][research_iwai_suzuki_2019]\] \[[Iyer et al 2004][research_iyer_kuhl_2004]\] \[[Jackson 1976][research_jackson_1976]\] \[[Jacocks 1969][research_jacocks_1969]\] \[[Jacocks 1969][research_jacocks_1969_b]\] \[[Jacocks 1970][research_jacocks_1970]\] \[[Jacocks and Hartley 1969][research_jacocks_hartley_1969]\] \[[Jaffe 1972][research_jaffe_1972]\] \[[Grauer and Waite][research_jaredagrauer_josiahmwaite]\] \[[Jenkins 1983][research_jenkinsrv_1983_b]\] \[[Jenkins 1986][research_jenkinsrv_1986]\] \[[Jenkins et al 1984][research_jenkinsrv_johnsonwgjr_1984]\] \[[Jenkins 1989][research_jenkinsrenaldov_1989]\] \[[Jenkins et al 1988][research_jenkinsrenaldov_hillacquillas_1988]\] \[[Jin et al 2013][research_jin_ren_2013]\] \[[Jinks et al 2016][research_jinks_bruce_2016]\] \[[Lamar et al 2001][research_johnelamar_cliffordjobara_2001]\] \[[Johnson][research_johnson]\] \[[Johnson et al 1970][research_johnson_josepha_1970]\] \[[Johnson and Adcock 1981][research_johnsoncb_adcockjb_1981]\] \[[Johnson et al 1986][research_johnsoncb_murthyav_1986]\] \[[Johnston 1998][research_johnston_1998]\] \[[Joppa 1968][research_joppa_1968]\] \[[Joppa 1969][research_joppa_1969]\] \[[Xiong et al][research_juntaoxiong_nhannguyen]\] \[[Xiong et al][research_juntaoxiong_nhannguyen_b]\] \[[Kacprzynski 1975][research_kacprzynski_1975]\] \[[Kalkhoran and Otugen 1994][research_kalkhoran_otugen_1994]\] \[[Kameda et al 2008][research_kameda_seki_2008]\] \[[Karlsson and Sedin 1979][research_karlsson_sedin_1979]\] \[[Kashitani et al 2010][research_kashitani_yamaguchi_2010_b]\] \[[Kaups et al 1989][research_kaups_mehta_1989]\] \[[Kehlet 1954][research_kehletalanb_1954]\] \[[Kemp 1991][research_kempwilliambjr_1991]\] \[[Kennelly et al 1990][research_kennellyrobertajr_krooilanm_1990]\] \[[Khalid and Mokry 1996][research_khalid_mokry_1996]\] \[[Kim et al][research_kim_cho]\] \[[King and Johnson 1980][research_king_johnson_1980]\] \[[King and Johnson 1986][research_king_johnson_1986]\] \[[Kmak 2000][research_kmak_2000]\] \[[Knackstedt 1952][research_knackstedt_1952]\] \[[Kohzai et al 2010][research_kohzai_sudani_2010]\] \[[Kolar and Lile 1971][research_kolar_lile_1971]\] \[[Kolesar et al 1970][research_kolesar_kassianides_1970]\] \[[Kraft 1974][research_kraft_1974]\] \[[Kraft and Lo 1977][research_kraft_lo_1977]\] \[[Kraft et al 1979][research_kraft_parker_1979]\] \[[Krupovage 1978][research_krupovage_1978]\] \[[Krynytzky 2001][research_krynytzky_2001]\] \[[Krynytzky 2004][research_krynytzky_2004]\] \[[Krynytzky and Hergert 2002][research_krynytzky_hergert_2002]\] \[[Krynytzky et al 2010][research_krynytzky_johnsen_2010]\] \[[Kubo 2018][research_kubo_2018]\] \[[Kuwahara 1987][research_kuwahara_1987]\] \[[Kyser 1956][research_kyser_1956]\] \[[Ladson 1973][research_ladsoncl_1973]\] \[[Ladson 1975][research_ladsoncl_1975]\] \[[Ladson and Ray 1984][research_ladsoncl_rayej_1984]\] \[[Lafferty and Marren 1996][research_lafferty_marren_1996]\] \[[Lawing and Johnson 1986][research_lawing_johnson_1986]\] \[[Lawing and Kilgore 1981][research_lawingpl_kilgorera_1981]\] \[[Layukallo and Nakamura 1999][research_layukallo_nakamura_1999]\] \[[Lederer 1994][research_lederer_1994]\] \[[Lee 1980][research_lee_1980]\] \[[Lehman and Stearman 1977][research_lehman_stearman_1977]\] \[[Leonard 1982][research_leonardhwayne_1982]\] \[[Li and Cai 2016][research_li_cai_2016]\] \[[Lifshitz et al 1996][research_lifshitz_solnstev_1996]\] \[[Lift effect on transonic 1980][research_lift_effect_1980]\] \[[Lijewski 1978][research_lijewski_1978]\] \[[Little and Cubbage 1961][research_littlebhjr_cubbagejamesjjr_1961]\] \[[Litwhiler][research_litwhiler]\] \[[Ljungskog et al 2019][research_ljungskog_sebben_2019]\] \[[Lo 1969][research_lo_1969]\] \[[Lo 1972][research_lo_1972]\] \[[Lo 1974][research_lo_1974]\] \[[Lo and Glassman 1975][research_lo_glassman_1975]\] \[[Lo and Oliver 1970][research_lo_oliver_1970]\] \[[Lo and Ulbrich 1991][research_lo_ulbrich_1991]\] \[[Lo et al 1995][research_lo_qian_1995]\] \[[Lombardi and Morelli 1995][research_lombardi_morelli_1995]\] \[[Lombardi et al 2003][research_lombardi_salvetti_2003]\] \[[Long 1990][research_long_1990]\] \[[Long and Gladen 1988][research_long_gladen_1988]\] \[[Lowry et al 2001][research_lowry_smith_2001]\] \[[Luers and Fiscus 1984][research_luers_fiscus_1984]\] \[[Ma et al 2016][research_ma_wang_2016]\] \[[Maeder and Hall 1955][research_maeder_hall_1955]\] \[[Malmuth 1984][research_malmuth_1984]\] \[[Malmuth 1987][research_malmuth_1987]\] \[[Malmuth and Cole 1984][research_malmuth_cole_1984]\] \[[Malmuth et al 1993][research_malmuth_jafroudi_1993]\] \[[Manjith 2026][research_manjith_2026]\] \[[Marino and Bonfiglioli 2012][research_marino_bonfiglioli_2012]\] \[[Marino et al 2009][research_marino_imperatore_2009]\] \[[Martindale et al 1988][research_martindale_butler_1988]\] \[[Maseland et al 2006][research_maseland_laban_2006]\] \[[Mason et al 2020][research_mason_lovejoy_2020]\] \[[Mason et al 2023][research_mason_davila_2023]\] \[[Mateer and Bertelrud 1983][research_mateer_bertelrud_1983]\] \[[Matsushita et al 1998][research_matsushita_saitoh_1998]\] \[[Matthews and Key 1977][research_matthews_key_1977]\] \[[Maydew 1957][research_maydew_1957]\] \[[McCanless and Boone 1974][research_mccanlessgfjr_boonejr_1974]\] \[[McCarthy et al 1955][research_mccarthy_jackf_1955]\] \[[McCarthy et al 1955][research_mccarthy_johnf_1955]\] \[[McClain and Pountney 1982][research_mcclain_pountney_1982]\] \[[McConnell 2004][research_mcconnell_2004]\] \[[McCroskey 1987][research_mccroskeywj_1987]\] \[[Medved 1993][research_medved_1993]\] \[[Melnik and Ives 1973][research_melnik_ives_1973]\] \[[Mercer et al 1980][research_mercer_geller_1980]\] \[[Metzger 1997][research_metzger_1997]\] \[[Miklos and Ingram 1975][research_miklos_ingram_1975]\] \[[Milillo 1972][research_milillo_1972]\] \[[Miller 1976][research_miller_1976]\] \[[Miller 1983][research_miller_1983]\] \[[Milligan and Bailey 1963][research_milligan_bailey_1963]\] \[[Mills 2004][research_mills_2004]\] \[[Mineck and Green 1990][research_mineck_green_1990]\] \[[Mineck 1989][research_mineckraymonde_1989]\] \[[Mitchell and Peck 1950][research_mitchelljessel_peckrobertf_1950_b]\] \[[Moes et al 1993][research_moestimothyr_whitmorestephena_1993]\] \[[Mokry 1989][research_mokry_1989]\] \[[Mokry 1990][research_mokry_1990]\] \[[Mokry 1995][research_mokry_1995_b]\] \[[Mokry 2001][research_mokry_2001]\] \[[Mokry and Khalid 2000][research_mokry_khalid_2000]\] \[[Mott 1954][research_mott_1954]\] \[[Muhlstein and Coe 1975][research_muhlsteinjr_coe_1975]\] \[[Mukhopadhyay 1999][research_mukhopadhyay_1999]\] \[[Mukhopadhyay 2000][research_mukhopadhyay_2000]\] \[[Mukhopadhyay 1999][research_mukhopadhyayvivek_1999]\] \[[Murman 1972][research_murman_1972]\] \[[Murman 1979][research_murman_1979]\] \[[Murthy and Wedemeyer 1990][research_murthy_wedemeyer_1990]\] \[[Murthy 1987][research_murthyav_1987]\] \[[Sinclair and Mace 1956][research_pitot_vane_1956]\] \[[Nagel and Thomas 1965][research_nagel_thomas_1965]\] \[[Nambu et al 2012][research_nambu_hashimoto_2012]\] \[[NASA 1982][research_calspan_ejector_1982]\] \[[National Advisory Committee for Aeronautics 1932][research_nationaladvisorycommitteeforaeronautics_1932]\] \[[Neal 1970][research_neal_1970]\] \[[Nelson and Mouch 1978][research_nelson_mouch_1978]\] \[[Newman et al 1988][research_newman_kemp_1988]\] \[[Newman and Anderson 1978][research_newmanpa_andersonec_1978]\] \[[Nichols and Jackson 1962][research_nichols_jackson_1962]\] \[[Nichols 1974][research_nicholsme_1974]\] \[[Noboru and Saito 2008][research_noboru_saito_2008]\] \[[Norris et al 1989][research_norris_paris_1989]\] \[[oliveira et al 2016][research_oliveira_avelar_2016]\] \[[Olson and Stridsberg 1979][research_olson_stridsberg_1979]\] \[[Ongarato 1969][research_ongarato_1969]\] \[[Owen 1981][research_owen_1981]\] \[[Pallister et al 1992][research_pallister_parker_1992]\] \[[Pan and Kuo 2021][research_pan_kuo_2021]\] \[[Parker and Black 1988][research_parkerjr_black_1988]\] \[[Patterson 1967][research_patterson_1967]\] \[[Payne and McConnell 2004][research_payne_mcconnell_2004]\] \[[Newman and Barnwell 1983][research_perryanewman_richardwbarnwell_1983]\] \[[Perry et al 2007][research_perryboydiii_silvawaltera_2007]\] \[[Persoon et al 1983][research_persoon_horsten_1983]\] \[[Persoon et al 1984][research_persoon_horsten_1984]\] \[[Petronevich 2016][research_petronevich_2016]\] \[[Petty 1975][research_petty_1975]\] \[[Phillips and Waggoner 1988][research_phillips_waggoner_1988]\] \[[Phillips and Waggoner 1990][research_phillips_waggoner_1990]\] \[[Piatak 1994][research_piatak_1994]\] \[[Pindzola and Chew 1960][research_pindzola_chew_1960]\] \[[Pindzola and Mozer 1956][research_pindzola_mozer_1956]\] \[[Platou 1968][research_platou_1968]\] \[[Plentovich et al 1984][research_plentovicheb_ladsoncl_1984]\] \[[Polivanov 2022][research_polivanovpa_2022]\] \[[Poole and Cromack 1970][research_poole_cromack_1970]\] \[[Potter et al 1961][research_potter_kinslow_1961]\] \[[Pounds 1972][research_pounds_1972]\] \[[Pounds and Walker 1980][research_pounds_walker_1980]\] \[[Prudhomme and Seraudie][research_prudhomme_seraudie]\] \[[Putnam and Meyers 1975][research_putnam_meyers_1975]\] \[[Qian and Guan 2012][research_qian_guan_2012]\] \[[Qu et al 2012][research_qu_zhang_2012]\] \[[Radespiel 1989][research_radespiel_1989]\] \[[Ramm 1990][research_ramm_1990_c]\] \[[Rasuo 2006][research_rasuo_2006_b]\] \[[Ray and Ladson 1984][research_rayej_ladsoncl_1984]\] \[[Recommended Practice Calibration of 2003][research_recommended_practice_2003]\] \[[Reed 1984][research_reed_1984]\] \[[Reed 1975][research_reedwhiii_1975]\] \[[Reed 1976][research_reedwhiii_1976]\] \[[Regan 1964][research_regan_1964]\] \[[Reis et al 2014][research_reis_falcaofilho_2014]\] \[[Rembaut and Brion 2026][research_rembaut_brion_2026]\] \[[Resonance prediction for slotted 1986][research_resonance_prediction_1986]\] \[[Richardson 1976][research_richardson_1976]\] \[[Richey et al 1976][research_richey_petersen_1976]\] \[[Ristić 1991][research_ristic_1991]\] \[[Rivera and Florance 2000][research_rivera_florance_2000]\] \[[Rizk 1982][research_rizk_1982]\] \[[Rizk 1986][research_rizk_1986]\] \[[Rizk and Lovell 1986][research_rizk_lovell_1986]\] \[[Rizk and Smithmeyer 1982][research_rizk_smithmeyer_1982]\] \[[Rizk et al 1988][research_rizk_lovell_1988]\] \[[Roth and Barrett 2009][research_roth_barrett_2009]\] \[[Ruhlin and Murphy 1981][research_ruhlin_murphy_1981]\] \[[Ruhlin and Pratt-Barlow 1981][research_ruhlin_prattbarlow_1981]\] \[[Ruhlin et al 1974][research_ruhlin_destuynder_1974]\] \[[Ruhlin et al 1982][research_ruhlin_rauchjr_1982]\] \[[Rumph and Schairer 1940][research_rumph_schairer_1940]\] \[[Ruyten 1999][research_ruyten_1999]\] \[[Satyanarayana et al 1981][research_satyanarayana_schairer_1981]\] \[[Savin 2019][research_savin_2019]\] \[[Schairer and Mendoza 1982][research_schaireret_mendozajp_1982]\] \[[Schairer 1994][research_schaireredwardt_1994]\] \[[Schairer et al 1989][research_schaireredwardt_leegeorge_1989]\] \[[Schairer et al 1991][research_schaireredwardt_leegeorge_1991]\] \[[Schuman 2018][research_schuman_2018]\] \[[Schwartz et al 2024][research_schwartz_gudmundsson_2024]\] \[[Schwarzt and Wuest 1964][research_schwarzt_wuest_1964]\] \[[Sedin and Sorensen 1984][research_sedin_sorensen_1984]\] \[[Sedin and Sorensen 1986][research_sedin_sorensen_1986]\] \[[Selerowicz 2020][research_selerowicz_2020]\] \[[Shankar et al 1978][research_shankar_malmuth_1978]\] \[[Shantz 1953][research_shantz_1953]\] \[[Shepheard 1965][research_shepheard_1965]\] \[[Sickles and Erickson 1990][research_sickles_ericksonjr_1990]\] \[[Silva and Bennett 1990][research_silva_bennett_1990]\] \[[Silva and Bennett 1992][research_silva_bennett_1992]\] \[[Sim 1997][research_simalexg_1997]\] \[[Sims and Carter 1981][research_sims_carter_1981]\] \[[Sinclair 1996][research_sinclair_1996]\] \[[Sloan et al 1962][research_sloan_eh_1962]\] \[[Smith 1953][research_smith_1953]\] \[[Smith 1966][research_smith_1966]\] \[[Smith et al 2026][research_smith_karns_2026]\] \[[Soltani et al 2011][research_soltani_marzabadi_2011]\] \[[Spahr and Kyrlach 1960][research_spahr_kyrlach_1960]\] \[[Spaid 1984][research_spaid_1984]\] \[[Springer 1998][research_springer_1998]\] \[[Spurlin and Lueck 1984][research_spurlin_lueck_1984]\] \[[Stahara and Spreiter 1979][research_stahara_spreiter_1979]\] \[[Stahara and Spreiter 1980][research_stahara_spreiter_1980]\] \[[Stallings and Hartman 1981][research_stallings_hartman_1981]\] \[[Stargill 1983][research_stargill_1983]\] \[[Starr 1975][research_starr_1975]\] \[[Starr 1978][research_starr_1978]\] \[[Steinle et al 1999][research_steinle_jr_1999]\] \[[Steinle et al 2004][research_steinle_hawkins_2004]\] \[[Stewart and Walters 1996][research_stewart_walters_1996]\] \[[Streather 1972][research_streather_1972]\] \[[Strike 1982][research_strike_wt_1982]\] \[[Sudani et al 2001][research_sudani_sato_2001]\] \[[Sudani et al 2003][research_sudani_sato_2003]\] \[[Symington 1940][research_symington_1940]\] \[[Taylor 1951][research_taylor_1951]\] \[[Thomas and Lan 1991][research_thomas_lan_1991]\] \[[Tidbury 1945][research_tidbury_1945]\] \[[Tijdeman et al 1979][research_tijdeman_vannunen_1979]\] \[[Tijdeman et al 1979][research_tijdeman_vannunen_1979_b]\] \[[Chau and Duensing][research_timothychau_jaredcduensing]\] \[[Transonic wind tunnel wall 1982][research_transonic_wind_1982]\] \[[Trimmer and Clark 1963][research_trimmer_clark_1963]\] \[[Tsushima et al 2023][research_tsushima_saitoh_2023]\] \[[Ueno and Sudani 2008][research_ueno_sudani_2008]\] \[[Ulbrich 2002][research_ulbrich_2002]\] \[[Ulbrich 2010][research_ulbrich_2010]\] \[[Ulbrich and Boone 1998][research_ulbrich_boone_1998]\] \[[Ulbrich and Boone 2001][research_ulbrich_boone_2001]\] \[[Ulbrich and Boone 2004][research_ulbrich_boone_2004]\] \[[Ulbrich et al 2018][research_ulbrichn_amayam_2018]\] \[[Ulbrich and Boone 2003][research_ulbrichnorbert_boonealanr_2003]\] \[[Vatsa and Wedan 1988][research_vatsa_wedan_1988]\] \[[Velasquez 2013][research_velasquez_2013]\] \[[Verhaagen 1997][research_verhaagen_1997]\] \[[Vidal et al 1976][research_vidalrj_ericksonjcjr_1976]\] \[[Volkova 2021][research_volkova_2021]\] \[[Volkova et al 2020][research_volkova_ivanov_2020]\] \[[von Knoblauch et al 2014][research_vonknoblauch_moreno_2014]\] \[[McCroskey 1988][research_wjmccroskey_1988]\] \[[Wagner 1982][research_wagner_1982]\] \[[Wagner 1985][research_wagner_1985]\] \[[Walker 2005][research_walkerericlee_2005]\] \[[Wallace 1952][research_wallace_1952]\] \[[Wang 2025][research_wang_2025]\] \[[Wang and Zhou 2020][research_wang_zhou_2020]\] \[[Weeks 1973][research_weeks_1973]\] \[[Weiand et al 2017][research_weiand_michelis_2017]\] \[[Weiss 2008][research_weiss_2008]\] \[[White 2004][research_white_2004]\] \[[White 1952][research_whitemauriced_1952]\] \[[Whitefield et al 1981][research_whitefield_griffith_1981]\] \[[Whittley and Garland 1961][research_whittley_garland_1961]\] \[[Wight 1964][research_wight_1964]\] \[[Willard and Kranzler 1996][research_willard_kranzler_1996]\] \[[Winchenbach et al 1982][research_winchenbach_chelekis_1982]\] \[[Wind Tunnel 2022][research_wind_tunnel_2022]\] \[[Wind Tunnel/Flight Test Correlation 1978][research_wind_tunnel_flight_1978]\] \[[Wing tunnel model for 1998][research_wing_tunnel_1998]\] \[[Wiriadidjaja et al 2012][research_wiriadidjaja_rafie_2012]\] \[[Wolf and Wolf 1997][research_wolf_wolf_1997]\] \[[Wood and Roberts 1989][research_wood_roberts_1989]\] \[[Wu et al 1982][research_wu_collins_1982]\] \[[Wu et al 1983][research_wu_collins_1983]\] \[[Wu and Collins 1984][research_wujm_collinsfg_1984]\] \[[Xie et al 2020][research_xie_liu_2020]\] \[[Xin et al 2013][research_xin_dawei_2013]\] \[[Xiong et al 2023][research_xiong_nguyen_2023_d]\] \[[Yamaguchi et al 1993][research_yamaguchi_yorozu_1993]\] \[[Yamaguchi et al 1994][research_yamaguchi_yorozu_1994]\] \[[Yetter et al 1982][research_yetter_evelyn_1982]\] \[[Yinsheng Luo et al 2011][research_yinshengluo_shaobangxing_2011]\] \[[Yoshida et al 2021][research_yoshida_bragg_2021]\] \[[Yu et al 2014][research_yu_lv_2014]\] \[[Zhang et al 2017][research_zhang_gao_2017]\] \[[Zhang et al 2019][research_zhang_dai_2019]\] \[[Zhao and Wang 2025][research_zhao_wang_2025]\] \[[Zhao et al 2023][research_zhao_jia_2023]\] \[[Zinovyev et al 2012][research_zinovyev_lebiga_2012]\]

### The transonic drag rise, wave drag and the area rule

**The first half of the keystone.** Drag rise and drag divergence, wave drag of bodies and wings, the area rule, base drag and the flight and tunnel measurement of drag through the band. **The flight-determined drag of named aircraft sits here beside the minimum wave drag body**, which is the pairing the article's fuselage arithmetic draws on.

**497 records.** \[[A Series of Airfoils 1982][research_a_series_1982]\] \[[Ghate et al][research_adityasghate_gaetankkenway]\] \[[Adiwidodo and Wijaya 2022][research_adiwidodo_wijaya_2022]\] \[[Ageev and Pavlenko 2016][research_ageev_pavlenko_2016]\] \[[Aguwa and Chen 2026][research_aguwa_chen_2026]\] \[[Alam and Pant 2019][research_alam_pant_2019]\] \[[Alhussan 2007][research_alhussan_2007]\] \[[Allison and Mineck 1996][research_allisondenniso_mineckraymonde_1996]\] \[[Almohammadi 2022][research_almohammadi_2022]\] \[[An evaluation of sailplane 1974][research_an_evaluation_1974]\] \[[Anatolievich and Andreevich 2020][research_anatolievich_andreevich_2020]\] \[[Anders and Watson 1985][research_anders_watson_1985]\] \[[Appendix F Flight Test 1999][research_appendix_f_1999]\] \[[Arguchintseva and Pilyugin 2008][research_arguchintseva_pilyugin_2008]\] \[[Armenta and Takahashi 2021][research_armenta_takahashi_2021]\] \[[Arnaiz 1975][research_arnaiz_1975]\] \[[Arnaiz 1977][research_arnaizhh_1977]\] \[[Atthar 2026][research_atthar_2026]\] \[[Aul'chenko 2006][research_aulchenko_2006]\] \[[Aul'chenko and Zamuraev 2012][research_aulchenko_zamuraev_2012]\] \[[Aul'chenko et al 1985][research_aulchenko_latypov_1985]\] \[[Austin and Van Nostrand 1995][research_austin_vannostrand_1995]\] \[[Austin et al 1997][research_austin_siclari_1997]\] \[[Azarova 2022][research_azarova_2022]\] \[[Bailey and Starr 1976][research_bailey_starr_1976]\] \[[Balusamy et al 2024][research_balusamy_a_2024]\] \[[Bartasevicius and Hornung 2023][research_bartasevicius_hornung_2023]\] \[[Bauer et al 2016][research_bauer_grund_2016]\] \[[Bauer et al 2026][research_bauer_garabedian_2026]\] \[[Bawa and Michalski 2025][research_bawa_michalski_2025]\] \[[Beeler et al 1956][research_beeler_1956]\] \[[Benedikt 1953][research_benedikt_1953]\] \[[Bernstein 1997][research_bernstein_1997]\] \[[Biber 2005][research_biber_2005]\] \[[Biot 1949][research_biot_1949]\] \[[Blanchard et al 1980][research_blanchard_phillips_1980]\] \[[Blanchard 1953][research_blanchardwillards_1953]\] \[[Bogomolov 1968][research_bogomolov_1968]\] \[[Bourisli and Hamadeh 2020][research_bourisli_hamadeh_2020]\] \[[Boyd 1965][research_boyd_1965]\] \[[Brazzel 1963][research_brazzel_1963]\] \[[Brower 1989][research_browerjr_1989]\] \[[Brown 2004][research_brown_2004]\] \[[Brutyan et al 2020][research_brutyan_volkov_2020]\] \[[Bull and Bridges 1983][research_bull_bridges_1983]\] \[[Bull and Bridges 1985][research_bull_bridges_1985]\] \[[Bulygina 1958][research_bulygina_1958]\] \[[Busemann 1964][research_busemann_1964]\] \[[Caballero 2001][research_caballero_2001]\] \[[Calarese and Walterick 1978][research_calarese_walterick_1978]\] \[[Camberos et al 2014][research_camberos_kolonay_2014]\] \[[Camberos et al 2015][research_camberos_kolonay_2015]\] \[[Carlsen 1994][research_carlsen_1994]\] \[[Carlsen 1995][research_carlsen_1995]\] \[[Carlson et al 2004][research_carlson_glauser_2004]\] \[[Carmel and Turner 1957][research_carmelmelvinm_turnerkennethl_1957]\] \[[Celmins 1990][research_celmins_1990]\] \[[Chan et al 2017][research_chan_jones_2017]\] \[[Chang 1962][research_chang_1962]\] \[[Chao and van Dam 1998][research_chao_vandam_1998]\] \[[CHAPTER NINE. The Minimum 1990][research_chapter_nine_1990]\] \[[Chaussee 1978][research_chaussee_1978]\] \[[Chen and Zhang 2006][research_chen_zhang_2006]\] \[[Chen et al 2021][research_chen_dong_2021]\] \[[Cheung et al 1995][research_cheung_aaronson_1995]\] \[[Choi et al 2016][research_choi_kang_2016]\] \[[Chow 1984][research_chow_1984]\] \[[Chow 1985][research_chow_1985]\] \[[Chow and Huang 1982][research_chow_huang_1982]\] \[[Cole and Malmuth 2005][research_cole_malmuth_2005]\] \[[Cole and Malmuth 1989][research_colejuliand_malmuthnormand_1989]\] \[[Connolly 1965][research_connolly_1965]\] \[[Crabill 1956][research_crabillnormanl_1956]\] \[[Daum and Zalovcik 1946][research_daumfredl_zalovcikjohna_1946]\] \[[Debiasi et al 2010][research_debiasi_yan_2010]\] \[[Demeritte and Gauzza 1958][research_demeritte_gauzza_1958_b]\] \[[Demeritte et al 1958][research_demeritte_gauzza_1958]\] \[[Deng and Qin 2021][research_deng_qin_2021]\] \[[Desai et al 1977][research_desai_viswanathan_1977]\] \[[Destarac and van der Vooren 2004][research_destarac_vandervooren_2004]\] \[[Dickey 1959][research_dickeyrobertr_1959]\] \[[Dietz 2005][research_dietz_2005]\] \[[Dixon and Hunsaker 2023][research_dixon_hunsaker_2023]\] \[[Dodbele et al 1986][research_dodbele_vandam_1986]\] \[[Doherty et al 2018][research_doherty_wang_2018]\] \[[Domingos et al 2024][research_domingos_ribeiro_2024]\] \[[Drag Polar Measurement in 2021][research_drag_polar_2021]\] \[[Dress 1988][research_dress_1988]\] \[[Dress 1989][research_dress_1989]\] \[[Du et al 2025][research_du_guo_2025]\] \[[Durham et al 1996][research_durham_bolling_1996]\] \[[Durmus 2021][research_durmus_2021]\] \[[Eghlima and Mansour 2017][research_eghlima_mansour_2017]\] \[[Eliasson and Peng 2007][research_eliasson_peng_2007]\] \[[Eliasson and Peng 2008][research_eliasson_peng_2008]\] \[[Ellinwood 1967][research_ellinwood_1967]\] \[[Eminton and Lord 1956][research_eminton_lord_1956]\] \[[Eppler 2003][research_eppler_2003]\] \[[Famellos et al 2024][research_famellos_skevas_2024]\] \[[Fan 2013][research_fan_2013]\] \[[Farrokhfal and Pishevar 2014][research_farrokhfal_pishevar_2014]\] \[[Fauci and Imperatore][research_fauci_imperatore]\] \[[Fediaevsky 1935][research_fediaevsky_1935]\] \[[Fedorov et al 1997][research_fedorov_malmuth_1997]\] \[[Fei et al 2026][research_fei_wang_2026]\] \[[Fertis 1988][research_fertis_1988]\] \[[Florio et al 2019][research_florio_mckibbin_2019]\] \[[Fournis 2022][research_fournis_2022]\] \[[Fraenkel 1958][research_fraenkel_1958]\] \[[Fraenkel 1958][research_fraenkel_1958_b]\] \[[Fu 1995][research_fu_1995]\] \[[Fu and Liang 1991][research_fu_liang_1991]\] \[[Fu and Liang 1993][research_fu_liang_1993]\] \[[Fujino and Kawamura 2003][research_fujino_kawamura_2003]\] \[[Fusi et al 2015][research_fusi_quaranta_2015]\] \[[Gada and Rahai 2016][research_gada_rahai_2016]\] \[[Ganesh 1994][research_ganesh_1994]\] \[[Gao 2023][research_gao_2023]\] \[[George-Falvy 1971][research_georgefalvy_1971]\] \[[Ghate et al 2021][research_ghate_kenway_2021]\] \[[Gillan 1993][research_gillan_1993]\] \[[Gillespie 1960][research_gillespiewarrenjr_1960]\] \[[Gillespie and Arbic 1950][research_gillespiewarrenjr_arbicrichardg_1950]\] \[[Glagolev et al 2000][research_glagolev_zubkov_2000]\] \[[Glazkov et al 2016][research_glazkov_gorbushin_2016]\] \[[Goradia and Bobbitt 1988][research_goradiash_bobbittpj_1988]\] \[[Gorski 1998][research_gorski_1998]\] \[[Graham et al 1954][research_graham_lagerstrom_1954]\] \[[Graham et al 1945][research_grahamdonaldj_nitzberggeralde_1945]\] \[[Greene 1957][research_greene_1957]\] \[[Guan 2013][research_guan_2013]\] \[[Guan 2014][research_guan_2014]\] \[[Guan 2014][research_guan_2014_b]\] \[[Gudilin et al 1996][research_gudilin_lashkov_1996]\] \[[Guy et al 2001][research_guy_mclaughlin_2001]\] \[[Hackett 2000][research_hackett_2000]\] \[[Hall et al 1953][research_halljr_hopkorn_1953]\] \[[Hanson 1989][research_hanson_1989]\] \[[Hares et al 2026][research_hares_brioua_2026]\] \[[Hart and Schmitz 2022][research_hart_schmitz_2022]\] \[[Haryanto et al 2014][research_haryanto_utomo_2014]\] \[[Hasalli Hj Ibrahim et al 2019][research_hasallihjibrahim_dzulhelmybinamari_2019]\] \[[Hasegawa and Sakaue 2017][research_hasegawa_sakaue_2017]\] \[[Haselton and Goode][research_haselton_goode]\] \[[Henning 1954][research_henningallenb_1954]\] \[[Henning 1957][research_henningallenb_1957]\] \[[Hicks and Moulton 1988][research_hicks_moulton_1988]\] \[[Hinchliffe and Qin 2016][research_hinchliffe_qin_2016]\] \[[Hinchliffe and Qin 2017][research_hinchliffe_qin_2017]\] \[[Hoffman 1958][research_hoffmans_1958]\] \[[Holdaway 1955][research_holdawaygeorgeh_1955]\] \[[Holdaway and Hatfield 1957][research_holdawaygeorgeh_hatfieldelainew_1957]\] \[[Holdaway et al 1959][research_holdawaygeorgeh_mellenthinjacka_1959]\] \[[Howell and Braslow 1955][research_howellrobertr_braslowalbertl_1955]\] \[[Hsiung and Chow 1993][research_hsiung_chow_1993]\] \[[Hsiung et al 1997][research_hsiung_onn_1997]\] \[[Huan and Modi 1995][research_huan_modi_1995]\] \[[Hue and Molton 2020][research_hue_molton_2020]\] \[[Huerta 1969][research_huerta_1969]\] \[[Huijts and Voskuijl 2015][research_huijts_voskuijl_2015]\] \[[Hunziker 1960][research_hunziker_1960]\] \[[Ibrahim and Filippone 2006][research_ibrahim_filippone_2006]\] \[[Ibrahim and Filippone 2007][research_ibrahim_filippone_2007]\] \[[Imai 1952][research_imai_1952]\] \[[Inger 1991][research_inger_1991]\] \[[Ishrak et al 2024][research_ishrak_shuvo_2024]\] \[[Jaeger et al 2026][research_jaeger_thome_2026]\] \[[Jain 1988][research_jain_1988]\] \[[Jankiewicz 2026][research_jankiewicz_2026]\] \[[Jenkins 1986][research_jenkins_1986]\] \[[Jesudasan et al 2026][research_jesudasan_doherty_2026]\] \[[Joarder 2018][research_joarder_2018]\] \[[Johnson 1953][research_johnson_1953]\] \[[Jones and Van Dyke 1958][research_jones_vandyke_1958]\] \[[Jones et al 2000][research_jones_townsend_2000]\] \[[Joshi 1996][research_joshi_1996]\] \[[Jumper 1983][research_jumper_1983]\] \[[Kale and Pendharkar 2021][research_kale_pendharkar_2021]\] \[[Kamiya et al 1978][research_kamiya_nishi_1978]\] \[[Kaneko et al 2024][research_kaneko_oyama_2024]\] \[[Kaneko et al 2024][research_kaneko_oyama_2024_b]\] \[[Katz 2013][research_katz_2013]\] \[[Kawamura and Karashima 1957][research_kawamura_karashima_1957]\] \[[Kendall 1984][research_kendall_1984]\] \[[Khlebnikov 1990][research_khlebnikov_1990]\] \[[Kieszek 2024][research_kieszek_2024]\] \[[Kieszek et al 2024][research_kieszek_majcher_2024]\] \[[Kim and Liou 2019][research_kim_liou_2019]\] \[[Klausmeyer 2004][research_klausmeyer_2004]\] \[[Knaus 1981][research_knaus_1981]\] \[[Knight et al 2011][research_knight_braun_2011]\] \[[Knight et al 2012][research_knight_braun_2012]\] \[[Konovalov et al 1998][research_konovalov_lashkov_1998]\] \[[Kornilov 2006][research_kornilov_2006]\] \[[Korsun et al 2024][research_korsun_poplavsky_2024]\] \[[Kostic et al 2002][research_kostic_mitrovic_2002]\] \[[Kraft and Mathews 1950][research_kraftchristophercjr_mathewscharlesw_1950]\] \[[Kraiko and Pudovikov 1998][research_kraiko_pudovikov_1998]\] \[[Kraiko and Shelomovskii 1984][research_kraiko_shelomovskii_1984]\] \[[Kraiko and Tilliaeva 1973][research_kraiko_tilliaeva_1973]\] \[[Kraiko and Tkalenko 1967][research_kraiko_tkalenko_1967]\] \[[Kraiko et al 2025][research_kraiko_tillyaeva_2025]\] \[[Krivec et al 1984][research_krivec_ling_1984]\] \[[Kulfan 2008][research_kulfan_2008]\] \[[Kulfan 2009][research_kulfan_2009]\] \[[Kusunose et al 1999][research_kusunose_crowder_1999]\] \[[Kutney and Piszkin 1963][research_kutney_piszkin_1963]\] \[[Kutney and Piszkin 1964][research_kutney_piszkin_1964]\] \[[Küchemann 1957][research_kuchemann_1957]\] \[[Lacerda Montes et al 2025][research_lacerdamontes_alves_2025]\] \[[Lahmili et al 2026][research_lahmili_bouchaala_2026]\] \[[Landahl and Widnall 1979][research_landahl_widnall_1979]\] \[[Landahl and Widnall 1980][research_landahl_widnall_1980]\] \[[Landahl and Widnall 1981][research_landahl_widnall_1981]\] \[[Landahl and Widnall 1982][research_landahl_widnall_1982]\] \[[Lapshina and Ostapenko 2009][research_lapshina_ostapenko_2009]\] \[[Lasauskas 2005][research_lasauskas_2005]\] \[[Lednicer and Roncz 1989][research_lednicer_roncz_1989]\] \[[Lee 1981][research_lee_1981]\] \[[Lefebvre and Zha 2014][research_lefebvre_zha_2014_b]\] \[[Li et al 2002][research_li_huyse_2002]\] \[[Li et al 2023][research_li_yu_2023]\] \[[Li et al 2023][research_li_zhang_2023]\] \[[Liang and Fu 1991][research_liang_fu_1991]\] \[[Licher 1956][research_licher_1956]\] \[[Lift/Drag Ratios of Optimised 1962][research_lift_drag_ratios_1962]\] \[[Lighthill 1956][research_lighthill_1956]\] \[[Lin 2025][research_lin_2025]\] \[[Liu et al 2012][research_liu_tao_2012]\] \[[Lomax and Heaslet 1956][research_lomax_heaslet_1956]\] \[[Lord and Eminton 1954][research_lord_eminton_1954]\] \[[Loving 1961][research_lovingdonaldl_1961_b]\] \[[Low Drag Airfoil Design 1980][research_low_drag_1980]\] \[[Luchuk 1957][research_luchuk_1957]\] \[[Luckert 1973][research_luckert_1973]\] \[[Lundry 1967][research_lundry_1967]\] \[[Luo 2024][research_luo_2024]\] \[[Ma 2025][research_ma_2025]\] \[[MacAllister 1955][research_macallister_1955]\] \[[Macha 1977][research_macha_1977]\] \[[Mair 1965][research_mair_1965]\] \[[Maklakov 2001][research_maklakov_2001]\] \[[Malmuth et al 1986][research_malmuth_wu_1986]\] \[[Malmuth et al 1987][research_malmuth_wu_1987]\] \[[Mani et al 2010][research_mani_rider_2010]\] \[[Margolis 1947][research_margoliskenneth_1947]\] \[[Markhotok 2021][research_markhotok_2021]\] \[[Mason 1982][research_mason_1982]\] \[[Masson et al 1998][research_masson_veilleux_1998]\] \[[Masson et al 1999][research_masson_veilleux_1999]\] \[[Masson et al 1999][research_masson_veilleux_1999_b]\] \[[Masuda and Yoshida 1991][research_masuda_yoshida_1991]\] \[[Mavriplis and Levy 2002][research_mavriplis_levy_2002]\] \[[Mavriplis and Levy 2005][research_mavriplis_levy_2005]\] \[[Mavriplis and Levy 2001][research_mavriplisdj_levydavidw_2001]\] \[[Mazurov and Takovitskii 2022][research_mazurov_takovitskii_2022]\] \[[McFall and Hollinger 1953][research_mcfalljohncjr_hollingerjamesa_1953]\] \[[McVey et al 1969][research_mcvey_rejeske_1969]\] \[[Mele et al 2015][research_mele_ostieri_2015]\] \[[Mele et al 2017][research_mele_ostieri_2017]\] \[[Melin et al 2010][research_melin_isikveren_2010]\] \[[Memon and Altman 2016][research_memon_altman_2016]\] \[[Mertens et al 1986][research_mertens_klevenhusen_1986]\] \[[Mertens et al 1987][research_mertens_klevenhusen_1987]\] \[[Methods for Drag Determination 2003][research_methods_for_2003]\] \[[Miles 1953][research_miles_1953]\] \[[Miles 1954][research_miles_1954]\] \[[Milholen and Owens 2005][research_milholen_owens_2005]\] \[[Minimum drag shapes 1962][research_minimum_drag_1962]\] \[[Mironov and Serdyuk 2012][research_mironov_serdyuk_2012]\] \[[Mitcham et al 1951][research_mitchamgradyl_blanchardwillardsjr_1951]\] \[[Mitcham et al 1952][research_mitchamgradyl_blanchardwillards_1952]\] \[[Moga 1980][research_moga_1980]\] \[[Moga and Dejarnette 1981][research_moga_dejarnette_1981]\] \[[Morales Tirado et al 2019][research_moralestirado_quagliarella_2019]\] \[[Morelli et al 1976][research_morelli_fioravanti_1976]\] \[[Moulden et al 1974][research_moulden_wu_1974]\] \[[Muller and Gasko 1967][research_muller_gasko_1967]\] \[[Muller and Wesshaar 1994][research_muller_wesshaar_1994]\] \[[Munk 1921][research_munk_1921]\] \[[Murman and Cole 1974][research_murman_cole_1974]\] \[[Murthy and Rose 1977][research_murthy_rose_1977]\] \[[NACA 1945][research_freefall_1945]\] \[[Mathews and Thompson 1947][research_freefall_65009_1947]\] \[[Thompson and Mathews 1947][research_freefall_sweptfwd_1947]\] \[[Mathews and Thompson 1947][research_freefall_wingbody_1947]\] \[[Cheatham and Kurbjun 1948][research_transonic_drag_wingbody_1948]\] \[[NACA 1949][research_comparative_drag_1949]\] \[[NACA 1950][research_comparative_drag_1950]\] \[[Kurbjun and Thompson 1953][research_freefall_interference_1953]\] \[[Holdaway 1954][research_drag_rise_reduction_1954]\] \[[Kelly and Osborne 1954][research_fuselage_mods_drag_1954]\] \[[Pierpont 1957][research_transonic_predict_1957]\] \[[Nagamatsu and Ficarra 1985][research_nagamatsu_ficarra_1985]\] \[[Nagamatsu and Orozco 1984][research_nagamatsu_orozco_1984]\] \[[Nagamatsu et al 1987][research_nagamatsu_trilling_1987]\] \[[Nagamatsu and Dyer 1984][research_nagamatsuht_dyerr_1984]\] \[[Nagamatsu et al 1982][research_nagamatsuht_browerwbjr_1982]\] \[[Nagamatsu et al 1983][research_nagamatsuht_ficarrar_1983]\] \[[Naida and Fonarev 1995][research_naida_fonarev_1995]\] \[[Naida and Fonarev 1996][research_naida_fonarev_1996]\] \[[Nark 1968][research_nark_1968]\] \[[Bellman 1959][research_transonic_summary_1959]\] \[[Howell and Korst 1971][research_drag_rise_notches_1971]\] \[[Usry and Wallace 1971][research_supercritical_body_1971]\] \[[Garabedian 1976][research_wave_drag_computation_1976]\] \[[Saltzman et al 1994][research_fsw_liftdrag_1994]\] \[[Nelson and Stoney 1953][research_nelsonrobertl_stoneywilliamejr_1953]\] \[[Nelson and Welsh 1957][research_nelsonrobertl_welshclementj_1957]\] \[[Nelson and Welsh 1960][research_nelsonrobertl_welshclementj_1960]\] \[[Nesteruk and Cartwright 2011][research_nesteruk_cartwright_2011]\] \[[Newell et al 1963][research_newell_dolbin_1963]\] \[[Nghiem and Norstrud 1989][research_nghiem_norstrud_1989]\] \[[Nielsen 1985][research_nielsen_1985]\] \[[Nielsen 1985][research_nielsen_1985_b]\] \[[Niewald and Parker 1999][research_niewald_parker_1999]\] \[[Nikfetrat et al 1992][research_nikfetrat_vandam_1992]\] \[[Nikolic and Jumper 2004][research_nikolic_jumper_2004]\] \[[Nixon 2003][research_nixon_2003]\] \[[Nunn and Bry 1982][research_nunn_bry_1982]\] \[[Ohashi et al 2019][research_ohashi_morita_2019]\] \[[Ohashi et al 2020][research_ohashi_morita_2020]\] \[[Ohashi et al 2021][research_ohashi_fukagata_2021]\] \[[Olsen et al 1984][research_olsen_shaw_1984]\] \[[Olson and Bielat 1955][research_olsonrolande_bielatralphp_1955]\] \[[Osawa and Hewitt 1986][research_osawa_hewitt_1986]\] \[[Osnes and Vartdal 2022][research_osnes_vartdal_2022]\] \[[Oswatitsch 1980][research_oswatitsch_1980]\] \[[Page 1956][research_pagewilliama_1956]\] \[[Pahle et al 2012][research_pahle_berger_2012]\] \[[Palaniappan and Jameson 2004][research_palaniappan_jameson_2004]\] \[[Panda and Warrior 2021][research_panda_warrior_2021]\] \[[Parks and Kehlet 1952][research_parksjamesh_kehletalanb_1952]\] \[[Patel et al 1979][research_patel_lee_1979]\] \[[Peigin and Epstein 2007][research_peigin_epstein_2007]\] \[[Peigin and Epstein 2015][research_peigin_epstein_2015]\] \[[Peters 1985][research_peters_1985]\] \[[Pfeifle et al 2022][research_pfeifle_notter_2022]\] \[[Phillips 1984][research_phillipsps_1984]\] \[[Pierpont 1959][research_pierpontpk_1959]\] \[[Pike 1999][research_pike_1999]\] \[[Pilyugin and Khlebnikov 2005][research_pilyugin_khlebnikov_2005]\] \[[Pinebrook and Dalton 1983][research_pinebrook_dalton_1983]\] \[[Pinebrook and Dalton 1983][research_pinebrook_dalton_1983_b]\] \[[Poll and Schumann 2024][research_poll_schumann_2024]\] \[[Powers 1988][research_powers_1988]\] \[[Powers et al 1986][research_powerssheryllgoecke_huffmanjarrettk_1986]\] \[[Prediction and Verification of 1985][research_prediction_and_1985]\] \[[Prescott 1963][research_prescott_1963]\] \[[Price 1978][research_price_1978]\] \[[Price 1981][research_pricejr_1981]\] \[[Puspitasari and Napitupulu 2023][research_puspitasari_napitupulu_2023]\] \[[Qin 2012][research_qin_2012]\] \[[Quadros et al 2018][research_quadros_khan_2018]\] \[[Ragni et al 2010][research_ragni_vanoudheusden_2010]\] \[[Ramaswamy and Viswanathan 1975][research_ramaswamy_viswanathan_1975]\] \[[Ramm 1990][research_ramm_1990]\] \[[Rein et al 2009][research_rein_rosemann_2009]\] \[[Reubush 1975][research_reubush_1975]\] \[[Whitcomb 1956][research_richardtwhitcomb_1956]\] \[[Riggins et al 1999][research_riggins_nelson_1999]\] \[[Rittenhouse 1959][research_rittenhouse_1959]\] \[[Roach and Froning 1996][research_roach_froning_1996]\] \[[Roberts 1963][research_roberts_1963]\] \[[Robinson 1953][research_robinsonharoldl_1953]\] \[[Rodi et al 2019][research_rodi_stoldt_2019]\] \[[Rogers 2010][research_rogers_2010]\] \[[Rooney et al 1977][research_rooney_craig_1977]\] \[[Roy et al 2021][research_roy_sandhu_2021]\] \[[Rusak and Wang 1999][research_rusak_wang_1999]\] \[[Russo et al 2020][research_russo_tognaccini_2020_b]\] \[[Sachs 1980][research_sachs_1980]\] \[[Sahu 1986][research_sahu_1986]\] \[[Saltzman and Ayers 1981][research_saltzman_ayers_1981]\] \[[Saltzman and Ayers 1982][research_saltzman_ayers_1982]\] \[[Sammonds 1970][research_sammonds_1970]\] \[[Sawyer and Trant 1950][research_sawyerrichardh_trantjamespjr_1950]\] \[[Schermerhorn 1969][research_schermerhorn_1969]\] \[[Schermerhorn and DeMeritte 1960][research_schermerhorn_demeritte_1960]\] \[[Schnerr and Dohrmann 1991][research_schnerr_dohrmann_1991]\] \[[Schnerr and Dohrmann 1994][research_schnerr_dohrmann_1994]\] \[[Schwartzberg 1975][research_schwartzberg_1975]\] \[[Sclafani et al 2010][research_sclafani_dehaan_2010]\] \[[Sears 1947][research_sears_1947]\] \[[Sedney 1954][research_sedney_1954]\] \[[Seebass 1974][research_seebassar_1974]\] \[[Seider and Haenel 1991][research_seider_haenel_1991]\] \[[Seraj and Martins 2023][research_seraj_martins_2023]\] \[[Seraj and Martins 2025][research_seraj_martins_2025]\] \[[Serdarevic-Kadic and Terzic 2019][research_serdarevickadic_terzic_2019]\] \[[Sforza 2018][research_sforza_2018]\] \[[Sforza 2020][research_sforza_2020]\] \[[Shanbhag and Narasimha 1970][research_shanbhag_narasimha_1970]\] \[[Shearin and Jones 1989][research_shearin_jones_1989]\] \[[Sheibani et al 2024][research_sheibani_jafarian_2024]\] \[[Sheila Tobing 2022][research_sheilatobing_2022]\] \[[Shibata et al 2018][research_shibata_tanaka_2018]\] \[[Shipilin 1964][research_shipilin_1964]\] \[[Shou-ying and Shi-jun 1982][research_shouying_shijun_1982]\] \[[Singh and Dwivedi 2022][research_singh_dwivedi_2022]\] \[[Sinha 2007][research_sinha_2007]\] \[[Sinkovec et al 2015][research_sinkovec_loshek_2015]\] \[[Siva Krishna Reddy et al 2021][research_sivakrishnareddy_sah_2021]\] \[[Sklar and Rusak 2020][research_sklar_rusak_2020]\] \[[Slingerland 2003][research_slingerland_2003]\] \[[Smetana and Knepper 1973][research_smetana_knepper_1973]\] \[[Smith 1997][research_smith_1997]\] \[[Smith and Klettner 2022][research_smith_klettner_2022]\] \[[Sorbilli et al 2018][research_sorbilli_dibianchi_2018]\] \[[Sotoudeh and Ferman 2019][research_sotoudeh_ferman_2019]\] \[[Spaid et al 1983][research_spaidfw_dahlinja_1983]\] \[[Squire 1965][research_squire_1965]\] \[[Squire 1975][research_squire_1975]\] \[[Squire and Nasser 1993][research_squire_nasser_1993]\] \[[Sreekanth 1961][research_sreekanth_1961]\] \[[Sreekanth 1962][research_sreekanth_1962]\] \[[Starr and Varner 1976][research_starr_varner_1976]\] \[[Steger and Baldwin 1972][research_stegerjl_baldwinbs_1972]\] \[[Steppert and Epple 2017][research_steppert_epple_2017]\] \[[Stevens and Purser 1955][research_stevensjosephe_purserpaule_1955]\] \[[Stevens 1950][research_stevensjosephe_1950]\] \[[Stevens 1955][research_stevensjosephe_1955]\] \[[Strand 1960][research_strand_1960]\] \[[Sun and Hansen 1982][research_sun_hansen_1982]\] \[[Sun et al 2025][research_sun_zhang_2025]\] \[[Sun et al 2026][research_sun_zhang_2026]\] \[[Suzuki et al 2010][research_suzuki_rinoie_2010]\] \[[Swamy et al 1978][research_swamy_ahmed_1978]\] \[[Takahashi 2013][research_takahashi_2013]\] \[[Takahashi et al 2010][research_takahashi_german_2010]\] \[[Takovitskii 2003][research_takovitskii_2003]\] \[[Takovitskii 2003][research_takovitskii_2003_b]\] \[[Takovitskii 2006][research_takovitskii_2006]\] \[[Takovitskii 2006][research_takovitskii_2006_b]\] \[[Takovitskii 2018][research_takovitskii_2018]\] \[[Takovitskii 2020][research_takovitskii_2020]\] \[[Takovitskii 2022][research_takovitskii_2022]\] \[[Takovitskii 2024][research_takovitskii_2024]\] \[[Tanaka et al 2024][research_tanaka_isoda_2024]\] \[[Tao et al 2019][research_tao_sun_2019]\] \[[Tetervin 1963][research_tetervin_1963]\] \[[Tetrault et al 2000][research_tetrault_schetz_2000]\] \[[The effects of aft-loaded 1989][research_the_effects_1989]\] \[[Tkalenko 1969][research_tkalenko_1969]\] \[[Torres and Rahai 2024][research_torres_rahai_2024]\] \[[Tun Nurhanis et al 2023][research_tunnurhanis_ambareenkhan_2023]\] \[[Ueno et al 2007][research_ueno_yamamoto_2007]\] \[[Vachon and Ray 2004][research_vachonmichaeljacob_rayronaldj_2004]\] \[[Vadillo and Agarwal 2007][research_vadillo_agarwal_2007]\] \[[Vadillo and Agarwal 2009][research_vadillo_agarwal_2009]\] \[[Van Dam 1986][research_vandam_1986]\] \[[Van Der Vooren and Van Der Wees 1990][research_vandervooren_vanderwees_1990]\] \[[van Es 2002][research_vanes_2002]\] \[[Vasil'ev 1966][research_vasilev_1966]\] \[[Viswanath 1988][research_viswanath_1988]\] \[[Viswanath and Mukund 1995][research_viswanath_mukund_1995]\] \[[Viswanath and Patil 1997][research_viswanath_patil_1997]\] \[[Viswanath and Rajendra 1990][research_viswanath_rajendra_1990]\] \[[Vozhdaev and Teperin 2020][research_vozhdaev_teperin_2020]\] \[[Walker 1973][research_walker_1973]\] \[[Wallskog 1954][research_wallskogharveya_1954]\] \[[Wallskog 1954][research_wallskogharveya_1954_b]\] \[[Ward 1968][research_ward_1968]\] \[[Weidinger 1927][research_weidingerhanns_1927]\] \[[Wetmore 1947][research_wetmorejw_1947]\] \[[Whitcomb 1952][research_whitcomb_1952]\] \[[Whitcomb 1953][research_whitcombrichardt_1953]\] \[[Whitcomb and Sevier 1960][research_whitcombrichardt_sevierjohnrjr_1960]\] \[[White 1963][research_white_1963]\] \[[White 1977][research_white_1977]\] \[[Whitfield and Griffith 1963][research_whitfield_griffith_1963]\] \[[Wislicenus and Daidzic 2022][research_wislicenus_daidzic_2022]\] \[[Wood 1944][research_woodclotaire_1944]\] \[[Wood 1988][research_woodrichardm_1988]\] \[[Wu et al 2025][research_wu_yuan_2025]\] \[[Xiong et al 2021][research_xiong_bartels_2021_b]\] \[[Xiong et al 2022][research_xiong_nguyen_2022]\] \[[Xiong et al 2023][research_xiong_nguyen_2023]\] \[[Xue et al 2020][research_xue_ren_2020]\] \[[Yechout and Schweikhard 1984][research_yechout_schweikhard_1984]\] \[[Yefremov et al 2005][research_yefremov_kraiko_2005]\] \[[Yoshida and Tokuyama 1992][research_yoshida_tokuyama_1992]\] \[[Yu et al 1983][research_yu_chen_1983]\] \[[Yuhara et al 2018][research_yuhara_kubota_2018]\] \[[Zalovcik 1944][research_zalovcikjohna_1944]\] \[[Zalovcik 1945][research_zalovcikjohna_1945]\] \[[Zeleke et al 2023][research_zeleke_asfaw_2023]\] \[[Zhang and Du 2025][research_zhang_du_2025]\] \[[Zhao 2023][research_zhao_2023]\] \[[Zhao et al 2022][research_zhao_wu_2022]\] \[[Zheng and Liu 2011][research_zheng_liu_2011]\] \[[Zheng et al 2012][research_zheng_feng_2012]\] \[[Zhigulev and Zhilin 1959][research_zhigulev_zhilin_1959]\] \[[Zhu and Qin 2021][research_zhu_qin_2021]\] \[[Zingg et al 2006][research_zingg_diosady_2006]\] \[[Zong et al 2023][research_zong_wu_2023]\] \[[Ümütlü et al 2022][research_umutlu_kiral_2022]\]

### Control authority, the all-moving tail and longitudinal trim

**The second half of the keystone, and the subject of the article's central finding.** Tail and elevator effectiveness, hinge moments, the all-moving surface, trim, pitch-up, downwash at the tail and longitudinal and lateral stability through the band. **Hinge moments are named in 58 of these titles and an all-movable surface or stabilator in 41**, and flutter is named in 59, which is the risk the article records the X-1 accepting in exchange for authority.

**470 records.** \[[Abichandani and Rosenberg 1952][research_abichandani_rosenberg_1952]\] \[[Adamov and Chasovnikov 2025][research_adamov_chasovnikov_2025]\] \[[Adams and Silsby 1947][research_adamsricharde_silsbynormans_1947]\] \[[Ai et al 2023][research_ai_bai_2023]\] \[[Ai et al 2023][research_ai_bai_2023_b]\] \[[Ai et al 2024][research_ai_bai_2024]\] \[[Ai et al 2026][research_ai_bai_2026]\] \[[Aidala 1985][research_aidala_1985]\] \[[Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974]\] \[[Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974_b]\] \[[Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_b]\] \[[Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991_b]\] \[[Air Force Test Pilot School Edwards Afb Ca 1992][research_airforcetestpilotschooledwardsafbca_1992]\] \[[Aircraft Stability Characteristics in 2021][research_aircraft_stability_2021]\] \[[Aircraft Stability Derivatives 1998][research_aircraft_stability_1998]\] \[[Airplane Trim 2012][research_airplane_trim_2012]\] \[[Airplane Trim 2022][research_airplane_trim_2022]\] \[[Akmese et al 2009][research_akmese_comert_2009]\] \[[Alden and Schindel 1952][research_alden_schindel_1952]\] \[[Ameduri et al 2005][research_ameduri_concilio_2005]\] \[[Amendola et al 2018][research_amendola_dimino_2018]\] \[[Amin et al 2016][research_amin_shah_2016]\] \[[Amprikidis et al 2003][research_amprikidis_cooper_2003]\] \[[An and Williams 2025][research_an_williams_2025]\] \[[An and Williams 2026][research_an_williams_2026]\] \[[Andersen et al 1997][research_andersen_kolonay_1997]\] \[[Andersen et al 1998][research_andersen_kolonay_1998]\] \[[Andersen et al 1998][research_andersen_kolonay_1998_b]\] \[[Anderson 1984][research_anderson_1984]\] \[[Anderson and Bray 1951][research_andersonsethb_brayrichards_1951]\] \[[Ang 1987][research_ang_1987]\] \[[Ansell et al 2010][research_ansell_bragg_2010]\] \[[Ansell et al 2011][research_ansell_bragg_2011]\] \[[Ansell et al 2011][research_ansell_bragg_2011_b]\] \[[Ansell et al 2013][research_ansell_kerho_2013]\] \[[Arnold 1942][research_arnold_1942]\] \[[Asher et al 1957][research_asher_martuccelli_1957]\] \[[Atkinson 2016][research_atkinson_2016]\] \[[Avkhadiev and Elizarov 2001][research_avkhadiev_elizarov_2001]\] \[[Axelson 1947][research_axelsonja_1947]\] \[[Babister 1980][research_babister_1980]\] \[[Bai et al 2022][research_bai_cao_2022]\] \[[Bai et al 2017][research_bai_qian_2017]\] \[[Balakrishna and Niranjana 1987][research_balakrishna_niranjana_1987]\] \[[Ball 1978][research_ball_1978]\] \[[Ball 1979][research_ball_1979]\] \[[Bean and Lee 1994][research_bean_lee_1994]\] \[[Bendiksen 1993][research_bendiksen_1993]\] \[[Benyamen et al 2020][research_benyamen_mckinnis_2020]\] \[[Bergen and Arnold 1940][research_bergen_arnold_1940]\] \[[Berry and Gilyard 1973][research_berry_gilyard_1973]\] \[[Bharadvaj 1990][research_bharadvaj_1990]\] \[[Bharadvaj 1991][research_bharadvaj_1991]\] \[[Bielat 1959][research_bielatralphp_1959]\] \[[Bihrle and Billy 1980][research_bihrle_jr_1980]\] \[[Black][research_black]\] \[[Bluman and Gandhi 2011][research_bluman_gandhi_2011]\] \[[Bogatyrev 2017][research_bogatyrev_2017]\] \[[Boling and Zha 2021][research_boling_zha_2021]\] \[[Boothe et al 1974][research_boothe_chen_1974]\] \[[Boroughs and Das 1999][research_boroughs_das_1999]\] \[[Bouquet and Vos 2017][research_bouquet_vos_2017]\] \[[Bouton 1951][research_bouton_1951]\] \[[Bragg and Soltani 1990][research_bragg_soltani_1990]\] \[[Brandon et al 1995][research_brandon_brown_1995]\] \[[Brincklow et al 2021][research_brincklow_montgomery_2021]\] \[[Bronz 2019][research_bronz_2019]\] \[[Bruno Santos et al 2020][research_brunosantos_oliveira_2020]\] \[[Bryson 2021][research_bryson_2021]\] \[[Burcham et al 1997][research_burchamfrankwjr_burkenjohnj_1997]\] \[[Burcham and Burken 1994][research_burchamjr_burken_1994]\] \[[Burcham and Pappas 1996][research_burchamjr_pappas_1996]\] \[[Burcham et al 1993][research_burchamjr_maine_1993]\] \[[Burnham 1995][research_burnham_1995]\] \[[Byrdsong and Brooks 1980][research_byrdsongta_brookscwjr_1980]\] \[[Cabaleiro de la Hoz and Fioriti 2021][research_cabaleirodelahoz_fioriti_2021]\] \[[Candon et al 2024][research_candon_hale_2024]\] \[[Cao and Lyu 2024][research_cao_lyu_2024]\] \[[Cao et al 2025][research_cao_lin_2025]\] \[[Capone et al 1983][research_capone_mason_1983]\] \[[Capone and Mason 1984][research_caponefj_masonml_1984]\] \[[Cassel et al 1969][research_cassel_durando_1969]\] \[[Catalano and Fremaux 1987][research_catalano_fremaux_1987]\] \[[Cecrdle 2011][research_cecrdle_2011]\] \[[Chandrasekharan et al 2015][research_chandrasekharan_iarocci_2015]\] \[[Chapter 4. Wing-Tail Plane 1957][research_chapter_4_1957]\] \[[Chen and Liu 2014][research_chen_liu_2014]\] \[[Chen and Mears 1957][research_chen_mears_1957]\] \[[Cheng 2009][research_cheng_2009]\] \[[Chin 1992][research_chin_1992]\] \[[Chin and Lentink 2019][research_chin_lentink_2019]\] \[[Clark 2026][research_clark_2026]\] \[[Clay 1967][research_clay_1967]\] \[[Clevenson and Thompson 1957][research_clevensonsa_thompsonrf_1957]\] \[[Cole et al 1990][research_colestanleyr_mossstevenw_1990]\] \[[Cornette and Rigby 1962][research_cornettees_rigbyrn_1962]\] \[[Cox et al 1997][research_cox_jackson_1997]\] \[[Crane 1948][research_craneharoldl_1948]\] \[[Crane 1948][research_craneharoldl_1948_b]\] \[[Crane and Beckhardt 1948][research_craneharoldl_beckhardtarnoldr_1948]\] \[[Crane and Sommer 1961][research_craneharoldl_sommerrobertw_1961]\] \[[Cristian and Vasile 2010][research_cristian_vasile_2010]\] \[[Cui et al 2022][research_cui_yue_2022]\] \[[D'Ewart et al 1958][research_dewart_jr_1958]\] \[[Birdsall 1970][research_dlbirdsall_1970]\] \[[Dannenberg et al 1960][research_dannenbergre_gambuccibj_1960]\] \[[de Melo et al 2024][research_demelo_bussamra_2024]\] \[[Deiler and Sachs 2026][research_deiler_sachs_2026]\] \[[Duffy 1989][research_duffy_1989]\] \[[Duncan 1950][research_duncan_1950]\] \[[Dvorak et al 1947][research_dvorak_kosiak_1947]\] \[[Eades et al 1964][research_eades_jr_1964]\] \[[Eastep et al 1998][research_eastep_andersen_1998]\] \[[Eastep et al 2001][research_eastep_andersen_2001]\] \[[Eckhaus 1962][research_eckhaus_1962]\] \[[Eldredge et al 2009][research_eldredge_wang_2009]\] \[[English 1955][research_englishrolandd_1955]\] \[[Erickson 1962][research_erickson_1962]\] \[[Ericsson 1997][research_ericsson_1997]\] \[[Everhart and Goradia 1988][research_everhart_goradia_1988]\] \[[Everhart and Bobbitt 1994][research_everhartjoell_bobbittpercyj_1994]\] \[[Everhart 1988][research_everhartjoellee_1988]\] \[[Faber and Crane 1961][research_faberstanley_craneharoldl_1961]\] \[[Faber and Eggleston 1953][research_faberstanley_egglestonjohnm_1953]\] \[[Fenwick and Allen 2007][research_fenwick_allen_2007]\] \[[Ferris 1975][research_ferrisjc_1975]\] \[[Fetterman 1959][research_fettermandejr_1959]\] \[[Fisher and Williams 1958][research_fisherlewisr_williamsjamesl_1958]\] \[[Foss and Swihart 1956][research_fosswejr_swihartjm_1956]\] \[[Fox and Woodward 1974][research_foxchj_woodwardfa_1974]\] \[[Franks 1953][research_franksralphw_1953]\] \[[French et al 1987][research_french_noll_1987]\] \[[Gageik et al 2018][research_gageik_nies_2018]\] \[[Gamble and Inman 2018][research_gamble_inman_2018]\] \[[Gambucci et al 1958][research_gambuccibj_sorensonrm_1958]\] \[[Gao et al 2021][research_gao_an_2021]\] \[[Garcia et al 2001][research_garcia_slingerland_2001]\] \[[Gardner and Curfman 1947][research_gardnerwilliamn_curfmanhowardjjr_1947]\] \[[Gerontakos and Lee 2007][research_gerontakos_lee_2007]\] \[[Giannelis et al 2019][research_giannelis_murray_2019]\] \[[Gibson et al 1958][research_gibsonfw_herrrw_1958]\] \[[Gillespie and Dietz 1952][research_gillespiewarrenjr_dietzalberte_1952]\] \[[Gillis and Mitchell 1957][research_gillisclarencel_mitchelljessel_1957]\] \[[Gillis et al 1950][research_gillisclarencel_peckrobertf_1950]\] \[[Goal et al 2012][research_goal_sun_2012]\] \[[Gong and Zhang 2025][research_gong_zhang_2025]\] \[[Goodrich and Sliwa 1987][research_goodrich_sliwa_1987]\] \[[Gopalarathnam and McAvoy 2001][research_gopalarathnam_mcavoy_2001]\] \[[Graham and Koenig 1951][research_grahamdavid_koenigdavidg_1951]\] \[[Graham and Koenig 1952][research_grahamdavid_koenigdavidg_1952]\] \[[Gray 2008][research_gray_2008]\] \[[Grismer et al 2000][research_grismer_kinsey_2000]\] \[[Gross et al 1986][research_gross_chandler_1986]\] \[[Grosser 1965][research_grosser_1965]\] \[[Guo et al 1988][research_guo_wang_1988]\] \[[Guo et al 2022][research_guo_zhang_2022]\] \[[Gurbacki and Bragg 1999][research_gurbacki_bragg_1999]\] \[[Gurbacki and Bragg 2001][research_gurbacki_bragg_2001]\] \[[Han et al 2023][research_han_liu_2023]\] \[[Hanel et al 2004][research_hanel_neuhuber_2004]\] \[[Hanson 1959][research_hansonpw_1959]\] \[[Hastings and Mitcham 1954][research_hastingsearlc_mitchamgradyl_1954]\] \[[He et al 2016][research_he_yang_2016]\] \[[He et al 2020][research_he_song_2020]\] \[[He et al 2021][research_he_wang_2021]\] \[[Heller et al 2006][research_heller_holmberg_2006]\] \[[Heron and Myose 2007][research_heron_myose_2007]\] \[[Hieser and Reid 1954][research_hiesergerald_reidcharlesf_1954]\] \[[Hitachi and Liu 2010][research_hitachi_liu_2010]\] \[[Hoang and Bui 2019][research_hoang_bui_2019]\] \[[Hoang et al 1993][research_hoang_rediniotis_1993]\] \[[Horizontal Tail Loads 1996][research_horizontal_tail_1996]\] \[[Hu et al 2011][research_hu_zhao_2011]\] \[[Hughes and Mennell 1974][research_hughesmt_mennellrc_1974]\] \[[Hunn 1953][research_hunn_1953]\] \[[Huttsell et al 1976][research_huttselllj_nollte_1976]\] \[[Hwang and Pi 1979][research_hwang_pi_1979]\] \[[Hwang et al 1991][research_hwang_chen_1991]\] \[[Illi et al 2013][research_illi_fingskes_2013]\] \[[Initial flight test of 1989][research_initial_flight_1989]\] \[[Irfan et al 2026][research_irfan_nanangburhan_2026]\] \[[Ishida and Ueshima 2026][research_ishida_ueshima_2026]\] \[[Isogai 2016][research_isogai_2016]\] \[[Isogai 2024][research_isogai_2024]\] \[[Jabbar et al 2026][research_jabbar_setiawan_2026]\] \[[Jayachandran et al 1987][research_jayachandran_bhanu_1987]\] \[[Jenney et al 1982][research_jenney_schreadley_1982]\] \[[Ji et al 2024][research_ji_huang_2024]\] \[[Jiang 2000][research_jiang_2000]\] \[[Jiang et al 2000][research_jiang_an_2000]\] \[[Jones and Farmer 1959][research_jonesgeorgewjr_farmermosesg_1959]\] \[[Karpouzian and Librescu 1992][research_karpouzian_librescu_1992]\] \[[Karthik et al 1999][research_karthik_tulapurkara_1999]\] \[[Kass 1970][research_kass_1970]\] \[[Keith and Selberg 1984][research_keith_selberg_1984]\] \[[Kelly 2014][research_kelly_2014]\] \[[Kempel et al 1975][research_kempelrw_danawh_1975]\] \[[Khan and Deng 2012][research_khan_deng_2012]\] \[[Khot et al 1997][research_khot_eastep_1997]\] \[[Kim and Marciniak 1999][research_kim_marciniak_1999]\] \[[Kim and Marciniak 2002][research_kim_marciniak_2002]\] \[[Kim et al 2003][research_kim_lee_2003]\] \[[Kim et al 2008][research_kim_kim_2008]\] \[[Klausmeyer 2018][research_klausmeyer_2018]\] \[[Klim et al 2013][research_klim_zeppetelli_2013]\] \[[Kline 2026][research_kline_2026]\] \[[Koenig 1953][research_koenigdavidg_1953]\] \[[Koenig 1953][research_koenigdavidg_1953_b]\] \[[Koreanschi et al 2014][research_koreanschi_oliviu_2014]\] \[[Kornev and Pimenov 2022][research_kornev_pimenov_2022]\] \[[Kryvokhatko and Masko 2018][research_kryvokhatko_masko_2018]\] \[[Krzywoblocki 1943][research_krzywoblocki_1943]\] \[[Kuhn et al 1993][research_kuhn_wardwell_1993]\] \[[Kumar et al 2001][research_kumar_viswanath_2001]\] \[[Kumar et al 2002][research_kumar_viswanath_2002]\] \[[Kumar et al 2021][research_kumar_sunil_2021]\] \[[Kuzmin 2013][research_kuzmin_2013]\] \[[Lai et al 2014][research_lai_zhang_2014]\] \[[Lan et al 1995][research_lan_hsu_1995]\] \[[Landers et al 1997][research_landers_landrum_1997]\] \[[Lauchle 1974][research_lauchle_1974]\] \[[Le Provost et al 2018][research_leprovost_he_2018]\] \[[Lee 2000][research_lee_2000]\] \[[Lee 2026][research_lee_2026]\] \[[Lee et al 2020][research_lee_sim_2020]\] \[[Lensi 2000][research_lensi_2000]\] \[[Levinsky et al 1968][research_levinsky_thommen_1968]\] \[[Levy 1992][research_levy_1992]\] \[[Li 2015][research_li_2015]\] \[[Li et al 2016][research_li_hirota_2016]\] \[[Li et al 2025][research_li_zhang_2025]\] \[[Li et al 2026][research_li_wen_2026]\] \[[Lin 2025][research_lin_2025_b]\] \[[Lin et al 2026][research_lin_wang_2026]\] \[[Lindsey and Milam 1974][research_lindseyai_milammd_1974]\] \[[Liu and Fung 1985][research_liu_fung_1985]\] \[[Liu and Platzer 1970][research_liu_platzer_1970]\] \[[Liu and Singh 1995][research_liu_singh_1995]\] \[[Longitudinal Control and Trim 2003][research_longitudinal_control_2003]\] \[[Longitudinal Trim and Stability 2016][research_longitudinal_trim_2016]\] \[[Luh and Mack 1984][research_luh_mack_1984]\] \[[Luoma 1954][research_luomaarvoa_1954]\] \[[Machado et al 2024][research_machado_chau_2024]\] \[[Manning and Gleason 1992][research_manning_gleason_1992]\] \[[Matheny and Gatlin 1978][research_mathenynw_gatlindh_1978]\] \[[Matranga and Armistead 1958][research_matrangagenej_armisteadkatharineh_1958]\] \[[McAllister 1994][research_mcallister_1994]\] \[[McLean 1994][research_mclean_1994]\] \[[Mehta 1986][research_mehta_1986]\] \[[Mennell 1976][research_mennellrc_1976]\] \[[Menshchikov and Somov 2019][research_menshchikov_somov_2019]\] \[[Mercer and Maiden 1972][research_mercerce_maidendl_1972]\] \[[Michal and Mitcham 1949][research_michaldavidh_mitchamgradyl_1949]\] \[[Miller and Ribbens 1999][research_miller_ribbens_1999]\] \[[Miller et al 2003][research_miller_jacques_2003]\] \[[Min et al 2024][research_min_xian_2024]\] \[[Mirowitz 1975][research_mirowitzli_1975]\] \[[Mitcham et al 1956][research_mitchamgradyl_stevensjosephe_1956]\] \[[Mitcham 1949][research_mitchamgradyl_1949]\] \[[Mitcham and Blanchard 1950][research_mitchamgradyl_blanchardwillardsjr_1950]\] \[[Mitchell and Peck 1950][research_mitchelljessel_peckrobertf_1950]\] \[[Mohamed et al 2021][research_mohamed_abdelhady_2021]\] \[[Montano et al 2024][research_montano_dimino_2024]\] \[[Moorthamers and Anemaat 2023][research_moorthamers_anemaat_2023]\] \[[Moreno et al 2012][research_moreno_taylor_2012]\] \[[Morito and Rowe 1972][research_moritoii_rowe_1972]\] \[[Morra and Nicolosi 2025][research_morra_nicolosi_2025]\] \[[Morse 1945][research_morse_1945]\] \[[Moseley and Thompson 1957][research_moseleywcjr_thompsonrf_1957]\] \[[Moses 1997][research_mosesrobertw_1997]\] \[[Moses 1997][research_mosesrobertw_1997_b]\] \[[Moses 1999][research_mosesrobertw_1999]\] \[[Moua et al 2008][research_mouachengm_coxtimothyh_2008]\] \[[Mulder et al 2009][research_mulder_lubbers_2009]\] \[[Harmon 1945][research_allmovable_comparison_1945]\] \[[Kleckner 1945][research_allmovable_prelim_1945]\] \[[Kleckner 1946][research_allmovable_geared_1946]\] \[[Hunter and Reeder 1946][research_spring_tab_1946]\] \[[Matthews and Mathews 1948][research_xs1_freefall_1948]\] \[[Drake 1950][research_x1_lateral_1950]\] \[[Fischel and Nugent 1953][research_longitudinal_accel_1953]\] \[[Anderson and Bray 1955][research_pitchup_evaluation_1955]\] \[[McDearmon and Boatright 1956][research_x1a_interference_1956]\] \[[Abbott and Land 1957][research_allmovable_flutter_1957]\] \[[Gibson et al 1957][research_x1e_flutter_1957]\] \[[Henderson 1957][research_x1e_lateral_1957]\] \[[Rainey and Igoe 1958][research_buffet_loads_1958]\] \[[Nagaraja et al 1982][research_nagaraja_lakin_1982]\] \[[Nagy and Kirsten 1976][research_nagy_kirsten_1976]\] \[[Nallapula et al 2012][research_nallapula_schade_2012]\] \[[Sellers 1958][research_allmovable_flutter_1958]\] \[[Peterson and Menees 1959][research_unswept_stability_1959]\] \[[Hurt and Whitten 1960][research_pitchup_control_1960]\] \[[Nguyen and Xiong 2021][research_transonic_correction_2021]\] \[[Nguyen and Xiong 2023][research_control_derivative_2023]\] \[[Nazarenko and Nevezhina 1972][research_nazarenko_nevezhina_1972]\] \[[Nguyen and Xiong 2022][research_nguyen_xiong_2022_b]\] \[[Nguyen and Xiong 2023][research_nguyen_xiong_2023]\] \[[Ni et al 2012][research_ni_hu_2012]\] \[[Nie et al 2026][research_nie_zhang_2026]\] \[[Nielsen et al 1984][research_nielsen_goodwin_1984]\] \[[Nikolitsch 1978][research_nikolitsch_1978]\] \[[Okolo et al 2015][research_okolo_dogan_2015]\] \[[Ordaz et al 2015][research_ordaz_geiselhart_2015]\] \[[Osborne and Tempelmeyer 1954][research_osborneroberts_tempelmeyerkennethe_1954]\] \[[Ostgaard 1962][research_ostgaard_1962]\] \[[Otto 1974][research_otto_1974]\] \[[Owens et al 2002][research_owenslr_wahlsra_2002]\] \[[Padua and Preisighe Viana 2025][research_padua_preisigheviana_2025]\] \[[Park and Abla 1982][research_park_abla_1982]\] \[[Park and Abla 1983][research_park_abla_1983]\] \[[Park and Chung 2012][research_park_chung_2012]\] \[[Parker et al 1991][research_parker_spain_1991]\] \[[Pashilkar 1996][research_pashilkar_1996]\] \[[Pavlenko and Reslan 2022][research_pavlenko_reslan_2022]\] \[[Paziresh et al 2017][research_paziresh_nikseresht_2017]\] \[[Pengelley and Wilson 1954][research_pengelley_wilson_1954]\] \[[Perry 1978][research_perrybiii_1978]\] \[[Persoon et al 1980][research_persoon_roos_1980]\] \[[Petrocchi et al 2023][research_petrocchi_mauriello_2023]\] \[[Phillips 1948][research_phillips_1948]\] \[[Phillips and West 2019][research_phillips_west_2019]\] \[[Pitt 1995][research_pitt_1995]\] \[[Pitt et al 2016][research_pitt_sexton_2016]\] \[[Prakash et al 2009][research_prakash_uthup_2009]\] \[[Prior et al 2023][research_prior_rozinka_2023]\] \[[Pushtaev 1989][research_pushtaev_1989]\] \[[Qi et al 2012][research_qi_he_2012]\] \[[Qi et al 2014][research_qi_he_2014]\] \[[Qiu and Sun 2009][research_qiu_sun_2009]\] \[[Rajagopal and Ortiz 1998][research_rajagopal_ortiz_1998]\] \[[Rajamurthy 2002][research_rajamurthy_2002]\] \[[Ramachandra et al 1980][research_ramachandra_sudhakar_1980]\] \[[Ran et al 2026][research_ran_wang_2026]\] \[[Ranaudo et al 1986][research_ranaudorj_mikkelsenkl_1986]\] \[[Rathert et al 1949][research_rathertgeorgeajr_hansoncarlm_1949]\] \[[Ratliff and Pagilla 2008][research_ratliff_pagilla_2008]\] \[[Rediniotis et al 1994][research_rediniotis_klute_1994]\] \[[Reimann 2016][research_reimann_2016]\] \[[Reissner 1943][research_reissner_1943]\] \[[Resende et al 1997][research_resende_nakagawa_1997]\] \[[Reuther et al 1992][research_reuther_vandam_1992]\] \[[Rhoads 1952][research_rhoads_1952]\] \[[Ricci et al 2006][research_ricci_scotti_2006]\] \[[Riebe and MacLeod 1950][research_riebejohnm_macleodrichardg_1950]\] \[[Riso et al 2018][research_riso_divincenzo_2018]\] \[[Rosenberg 1944][research_rosenberg_1944]\] \[[Ruhlin and Sandford 1975][research_ruhlincl_sandfordmc_1975]\] \[[Ruhlin et al 1968][research_ruhlincl_sandfordmc_1968]\] \[[Ruhlin et al 1976][research_ruhlincl_doggettrvjr_1976]\] \[[Ruhlin et al 1980][research_ruhlincl_doggettrvjr_1980]\] \[[Ruhlin and Tuovila 1961][research_ruhlincharlesl_tuovilawj_1961]\] \[[Runyan et al 1952][research_runyan_cunningham_1952]\] \[[Wallace et al][research_ryanwallace_jamesreynolds]\] \[[Sachs 1969][research_sachs_1969]\] \[[Sachs 1977][research_sachs_1977]\] \[[Sadoff 1953][research_sadoffmelvin_1953]\] \[[Safronov and Safronov 1994][research_safronov_safronov_1994]\] \[[Safronov et al 2023][research_safronov_semon_2023]\] \[[Safronov et al 2024][research_safronov_semon_2024]\] \[[Sahyoun et al 2026][research_sahyoun_boose_2026]\] \[[Saitoh et al 1995][research_saitoh_hashidate_1995]\] \[[Sanghi et al 2020][research_sanghi_riso_2020]\] \[[Sawyer and Trant 1947][research_sawyerrichardh_trantjamespjr_1947]\] \[[Sayers 1936][research_sayers_1936]\] \[[Schaeffler and Telionis 1998][research_schaeffler_telionis_1998]\] \[[Schauerte and Schreyer 2024][research_schauerte_schreyer_2024]\] \[[Schauerte and Schreyer 2025][research_schauerte_schreyer_2025_b]\] \[[Schmitt et al 1990][research_schmitt_reneaux_1990]\] \[[Scott et al 2024][research_scott_candon_2024]\] \[[Sebastia and Hornung 2023][research_sebastia_hornung_2023]\] \[[Sebastia et al 2024][research_sebastia_wurz_2024]\] \[[Seckel 1964][research_seckel_1964]\] \[[Seidel et al 1985][research_seidel_sandford_1985]\] \[[Shankar 2013][research_shankar_2013]\] \[[Sherrouse and McWhorter 1992][research_sherrouse_mcwhorter_1992]\] \[[Sheta 2004][research_sheta_2004]\] \[[Shmilovich and Caughey][research_shmilovich_caughey]\] \[[Shmilovich and Caughey 1985][research_shmilovich_caughey_1985]\] \[[Sieradzki 2016][research_sieradzki_2016]\] \[[Silsby and Kennedy 1947][research_silsbynormans_kennedyrobertm_1947]\] \[[Silva et al 2004][research_silva_mello_2004]\] \[[Silva et al 2005][research_silva_mello_2005]\] \[[Silva et al 2006][research_silva_mello_2006]\] \[[Silva et al 2006][research_silva_mello_2006_b]\] \[[Simsek and Tekinalp 2015][research_simsek_tekinalp_2015]\] \[[Singh and McDonough 2014][research_singh_mcdonough_2014]\] \[[Singhasenee et al 2026][research_singhasenee_lamon_2026]\] \[[Slingerland 2005][research_slingerland_2005]\] \[[Smith 1974][research_smithhc_1974]\] \[[Smith 1954][research_smithwilliardg_1954]\] \[[Solarte-Pineda et al 2026][research_solartepineda_bravomosquera_2026]\] \[[Solies 1992][research_solies_1992]\] \[[Solies 1992][research_solies_1992_b]\] \[[Solies 1994][research_solies_1994]\] \[[Sotoudeh et al 2010][research_sotoudeh_hodges_2010]\] \[[Sreenivasulu et al 2025][research_sreenivasulu_neelapu_2025]\] \[[Srichitturi 2026][research_srichitturi_2026]\] \[[Staelens et al 2007][research_staelens_blackwelder_2007]\] \[[Static Longitudinal Stability Flight 2003][research_static_longitudinal_2003]\] \[[Steer 2003][research_steer_2003]\] \[[Steger and Bailey 1979][research_steger_bailey_1979]\] \[[Steger and Bailey 1980][research_steger_bailey_1980]\] \[[Stegmüller et al 2026][research_stegmuller_haybock_2026]\] \[[Suleman et al 2000][research_suleman_crawford_2000]\] \[[Sun and Hu 2005][research_sun_hu_2005]\] \[[Szema and Shankar 1984][research_szema_shankar_1984]\] \[[Tamayama et al 2003][research_tamayama_kheirandish_2003]\] \[[Tang 1971][research_tangmh_1971]\] \[[Tang and Pearson 1971][research_tangmh_pearsongpe_1971]\] \[[Taraborrelli 2023][research_taraborrelli_2023]\] \[[Teperin et al 2018][research_teperin_teperina_2018]\] \[[Thacker and Lan 1993][research_thacker_lan_1993]\] \[[Thompson and Moseley 1956][research_thompsonrobertf_moseleywilliamcjr_1956]\] \[[Thomson 1946][research_thomson_1946]\] \[[Ting et al 2014][research_ting_nguyen_2014]\] \[[Tischler 2018][research_tischler_2018]\] \[[Tleulinov and Jafarzade 2019][research_tleulinov_jafarzade_2019]\] \[[Tobak and Lessing 1961][research_tobakmurray_lessinghenryc_1961]\] \[[Tomek and Boyden 2000][research_tomek_boyden_2000]\] \[[Tuovila and Hess 1959][research_tuovilawj_hessrobertw_1959]\] \[[Turner 1982][research_turner_1982]\] \[[Tấn 2020][research_tan_2020]\] \[[Ueno and Miwa 2001][research_ueno_miwa_2001]\] \[[Ulug and Cigeroglu 2025][research_ulug_cigeroglu_2025]\] \[[Urie and Reaser 1979][research_urie_reaser_1979]\] \[[van Arnhem et al 2019][research_vanarnhem_devries_2019]\] \[[Van Dam and Hicks 1990][research_vandam_hicks_1990]\] \[[van Dommelen et al 2019][research_vandommelen_dsilva_2019]\] \[[van Es 2003][research_vanes_2003]\] \[[van Wezel et al 2025][research_vanwezel_pool_2025]\] \[[Vianto et al 2021][research_vianto_tobing_2021]\] \[[Vincent and Botez 2015][research_vincent_botez_2015]\] \[[Vindigni 2024][research_vindigni_2024]\] \[[Vindigni et al 2024][research_vindigni_mantegna_2024]\] \[[Vindigni et al 2024][research_vindigni_mantegna_2024_b]\] \[[Vinh et al 1988][research_vinhlamson_edwardsjohnw_1988]\] \[[Wang 2019][research_wang_2019]\] \[[Wang et al 2013][research_wang_hu_2013]\] \[[Wang et al 2021][research_wang_wu_2021]\] \[[Weingarten 2003][research_weingarten_2003]\] \[[Weingarten and Chalk 1982][research_weingarten_chalk_1982]\] \[[Weisshaar and Zeiler 1982][research_weisshaar_zeiler_1982]\] \[[Wermeser et al 2024][research_wermeser_takarics_2024]\] \[[Wetzel and Pfyl 1954][research_wetzelbentone_pfylfranka_1954]\] \[[Whitmer et al 2012][research_whitmer_kelkar_2012]\] \[[Williams-Hayes 2005][research_williamshayes_2005]\] \[[Woodward 1973][research_woodwardfa_1973]\] \[[Wright 1945][research_wright_1945]\] \[[Xie et al 2019][research_xie_zhao_2019]\] \[[Xiong and Nguyen 2022][research_xiong_nguyen_2022_c]\] \[[Xiong and Nguyen 2024][research_xiong_nguyen_2024_b]\] \[[Xu and Qiu 2011][research_xu_qiu_2011]\] \[[Yigit and Millidere 2021][research_yigit_millidere_2021]\] \[[You 2026][research_you_2026]\] \[[Yurkovich 1996][research_yurkovich_1996]\] \[[Zahn and Breitsamter 2020][research_zahn_breitsamter_2020]\] \[[Zamuraev and Kalinina 2018][research_zamuraev_kalinina_2018]\] \[[Zhang and Ye 2010][research_zhang_ye_2010]\] \[[Zhang and Ye 2015][research_zhang_ye_2015]\] \[[Zhang and Zhang 2013][research_zhang_zhang_2013]\] \[[Zhang et al 2013][research_zhang_yu_2013]\] \[[Zhang et al 2023][research_zhang_su_2023]\] \[[Zhang et al 2024][research_zhang_zhao_2024]\] \[[Zhao and Hu 2009][research_zhao_hu_2009]\] \[[Zhao et al 2020][research_zhao_he_2020]\] \[[Zheng-hong 1992][research_zhenghong_1992]\] \[[Zhong et al 2025][research_zhong_xia_2025]\] \[[Zink et al 2001][research_zink_mavris_2001]\]

### Shock and boundary-layer interaction and shock-induced separation

**The mechanism behind both the control failure and the buffet.** Shock and boundary-layer interaction, shock-induced separation and its control by vortex generators, bumps and suction. **Only five of these 469 records predate 1960**, so the mechanism the X-1 met in flight acquired most of its literature long after the aircraft had flown through it.

**469 records.** \[[A computational procedure for 1980][research_a_computational_1980]\] \[[A computational study on 1994][research_a_computational_1994]\] \[[Adamson 1976][research_adamson_1976]\] \[[Adamson and Feo 1975][research_adamsonjr_feo_1975]\] \[[Adhikary and Narayanaswamy 2026][research_adhikary_narayanaswamy_2026]\] \[[Agarwal et al 1988][research_agarwal_deese_1988]\] \[[Agostini et al 2012][research_agostini_larcheveque_2012]\] \[[Agostini et al 2013][research_agostini_larcheveque_2013]\] \[[Altstatt 1977][research_altstatt_1977]\] \[[Anderson and Benson 1983][research_andersonbh_bensontj_1983]\] \[[Schoneich et al][research_antoniogiovannischoneich_thomasjwhalen]\] \[[Anyiwo and Bushnell 1982][research_anyiwojc_bushnelldm_1982]\] \[[Application of a Shock-Turbulent 1982][research_application_of_1982_b]\] \[[Ayok 2026][research_ayok_2026]\] \[[Babinsky 2007][research_babinsky_2007]\] \[[Babinsky and Délery 2011][research_babinsky_delery_2011]\] \[[Babinsky and Ogawa 2006][research_babinsky_ogawa_2006]\] \[[Bahi et al 1983][research_bahi_ross_1983]\] \[[Balasubramanian et al 2017][research_balasubramanian_anandhanarayanan_2017]\] \[[Barnhart et al 1988][research_barnhart_greber_1988]\] \[[Barter and Dolling 1996][research_barter_dolling_1996]\] \[[Barter and Dolling 1995][research_barterjohnw_dollingdavids_1995]\] \[[Barter and Dolling 1995][research_barterjohnw_dollingdavids_1995_b]\] \[[Baskaran and Muruganandam 2022][research_baskaran_muruganandam_2022]\] \[[Bauer and Hernandez 1988][research_bauer_hernandez_1988]\] \[[Bauer and Garabedian 1973][research_bauerf_garabedianp_1973]\] \[[Bazyma and Rashkovan 2003][research_bazyma_rashkovan_2003]\] \[[Benay and Pot 1986][research_benay_pot_1986]\] \[[Benay et al 1989][research_benay_coet_1989]\] \[[Benay et al 2001][research_benay_berthouze_2001]\] \[[Benhachmi et al 1989][research_benhachmidriss_greberisaac_1989]\] \[[Bennett et al 1991][research_bennett_dansberry_1991]\] \[[Bennett et al 1993][research_bennett_dansberry_1993]\] \[[Bergier][research_bergier]\] \[[Bernardini and Pirozzoli 2011][research_bernardini_pirozzoli_2011]\] \[[Bertelrud 1989][research_bertelrudarild_1989]\] \[[Bhanderi and Babinsky 2004][research_bhanderi_babinsky_2004]\] \[[Bhanderi and Babinsky 2005][research_bhanderi_babinsky_2005]\] \[[Bhardwaj and Sriram 2019][research_bhardwaj_sriram_2019]\] \[[Bhola and Sengupta 2019][research_bhola_sengupta_2019]\] \[[Bich Ngoc and Hung 2011][research_bichngoc_hung_2011]\] \[[Bird 1991][research_birdga_1991]\] \[[Biswas and Jimbo 2015][research_biswas_jimbo_2015]\] \[[Black 1968][research_black_1968]\] \[[Black 1969][research_black_1969]\] \[[Blackwell 1969][research_blackwelljajr_1969]\] \[[Blosch et al 1992][research_blosch_carroll_1992]\] \[[Blosch et al 1993][research_blosch_carroll_1993]\] \[[Bodin and Fuchs 2008][research_bodin_fuchs_2008]\] \[[Bodonyi and Smith 1986][research_bodonyi_smith_1986]\] \[[Bogdonoff 1987][research_bogdonoff_1987]\] \[[Bogdonoff 1989][research_bogdonoff_1989]\] \[[Bogdonoff and Smits 1992][research_bogdonoff_smits_1992]\] \[[Bohning and Doerffer 2002][research_bohning_doerffer_2002]\] \[[Bohning et al 1994][research_bohning_thiede_1994]\] \[[Brilliant and Adamson 1974][research_brilliant_adamson_1974]\] \[[Brilliant and Adamson 1973][research_brilliant_adamsonjr_1973]\] \[[Brouwer et al 2017][research_brouwer_2017]\] \[[Brown et al 1986][research_brown_kussoy_1986]\] \[[Bur and Corbel 2000][research_bur_corbel_2000]\] \[[Bur et al 1997][research_bur_corbel_1997]\] \[[Bur et al 1998][research_bur_corbel_1998]\] \[[Bur et al 2000][research_bur_benay_2000]\] \[[Bur et al 2002][research_bur_benay_2002]\] \[[Bur et al 2009][research_bur_coponet_2009]\] \[[Burdges 1979][research_burdges_1979]\] \[[Burdges 1981][research_burdges_1981]\] \[[Burrows et al 2021][research_burrows_vukasinovic_2021]\] \[[Cahill 1986][research_cahill_1986]\] \[[Canoville and Lewis 2025][research_canoville_lewis_2025]\] \[[Carter and Hafez 1982][research_carter_hafez_1982]\] \[[Chakrabartty and Dhanalakshmi 1995][research_chakrabartty_dhanalakshmi_1995]\] \[[Chakraborty et al 2022][research_chakraborty_roy_2022]\] \[[Chakravarty and Narayanaswamy 2026][research_chakravarty_narayanaswamy_2026]\] \[[Chandravamsi et al 2023][research_chandravamsi_bhardwaj_2023]\] \[[Chanzy][research_chanzy]\] \[[Chen 1990][research_chen_1990]\] \[[Chen et al 2009][research_chen_xu_2009]\] \[[Chen et al 2014][research_chen_zhang_2014]\] \[[Cheng and Smith 1994][research_cheng_smith_1994]\] \[[Chevalier and Robertson 1963][research_chevalier_robertson_1963]\] \[[Childs and Seebaugh 1969][research_childsme_seebaughwr_1969]\] \[[Childs and Seebaugh 1970][research_childsme_seebaughwr_1970]\] \[[Choudhuri and Knight 1995][research_choudhuri_knight_1995]\] \[[Choudhuri and Knight 1996][research_choudhuri_knight_1996]\] \[[Chriss et al 1990][research_chrissrm_hingstwr_1990]\] \[[Chung et al 2021][research_chung_su_2021]\] \[[Chyu and Kuwahara 1982][research_chyu_kuwahara_1982]\] \[[Cinnella 2001][research_cinnella_2001]\] \[[Cohen and Motallebi 2006][research_cohen_motallebi_2006]\] \[[Cohen and Motallebi 2008][research_cohen_motallebi_2008]\] \[[Comfort and Todisco 1969][research_comfort_todisco_1969]\] \[[Comparison of flowfield surveys 1994][research_comparison_of_1994]\] \[[Cook][research_cook]\] \[[Coon and Chapman 1991][research_coon_chapman_1991]\] \[[Coschignano and Babinsky 2018][research_coschignano_babinsky_2018]\] \[[Coschignano and Babinsky 2019][research_coschignano_babinsky_2019]\] \[[Cunningham and Plentovich 1987][research_cunninghamjr_plentovich_1987]\] \[[Cuppoletti et al 2016][research_cuppoletti_saucier_2016]\] \[[Czerwinska et al 2001][research_czerwinska_doerffer_2001]\] \[[da Silva Tuan et al 2024][research_tuan_malatesta_2024]\] \[[Dai and Zhang 2023][research_dai_zhang_2023]\] \[[Dargel 1997][research_dargel_1997]\] \[[Friedlander et al][research_davidjfriedlander_nicholasjgeorgiadis]\] \[[Davis 2015][research_davis_2015]\] \[[Davis and Malcolm 1980][research_davis_malcolm_1980]\] \[[Davis et al 1998][research_davisdo_willisbp_1998]\] \[[De Vanna 2025][research_devanna_2025]\] \[[Degrez and Ginoux 1987][research_degrez_ginoux_1987]\] \[[Degrez and Vandromme 1986][research_degrez_vandromme_1986]\] \[[Dehghan Manshadi and Rabani 2016][research_dehghanmanshadi_rabani_2016]\] \[[Delery 1981][research_delery_1981]\] \[[Deshpande and Poggie 2020][research_deshpande_poggie_2020]\] \[[Deveikis 1983][research_deveikiswd_1983]\] \[[Dickinson et al 2024][research_dickinson_babinsky_2024]\] \[[Doerffer and Telega 2013][research_doerffer_telega_2013]\] \[[Dolling 1986][research_dolling_1986]\] \[[Dolling 1988][research_dolling_1988]\] \[[Dolling 1993][research_dolling_1993]\] \[[Dolling 2000][research_dolling_2000]\] \[[Dolling and Bogdonoff 1980][research_dolling_bogdonoff_1980]\] \[[Dolling and Brusniak 1987][research_dolling_brusniak_1987]\] \[[Dolling and Clemens 2003][research_dolling_clemens_2003]\] \[[Dolling et al 2003][research_dolling_clemens_2003_b]\] \[[Dolling 1993][research_dollingds_1993]\] \[[Dolling and Barter 1995][research_dollingdavids_barterjohnw_1995]\] \[[Donaldson 1944][research_donaldsoncolemandup_1944]\] \[[Dor et al 1989][research_dor_mignosi_1989]\] \[[Dou et al 2006][research_dou_khoo_2006]\] \[[Drikakis and Durst 1994][research_drikakis_durst_1994]\] \[[Dudley and Torres 2007][research_dudley_torres_2007]\] \[[Dunagan][research_dunagan]\] \[[Dunagan et al 1986][research_dunaganstephene_brownjamesl_1986]\] \[[Dupont et al 2011][research_dupont_debieve_2011]\] \[[Dvorak and Choi 1982][research_dvorak_choi_1982]\] \[[Dvořák 1965][research_dvorak_1965]\] \[[Délery 1989][research_delery_1989]\] \[[Edelmann et al 2009][research_edelmann_roberts_2009]\] \[[Edwards 2007][research_edwards_2007]\] \[[Edwards et al 1985][research_edwards_carter_1985]\] \[[Edwards et al 1986][research_edwards_carter_1986]\] \[[Edwards et al 1986][research_edwards_whitfield_1986]\] \[[Edwards 1996][research_edwardsjohnw_1996]\] \[[Ekaterinaris 2010][research_ekaterinaris_2010]\] \[[Elham and Timmer 2016][research_elham_timmer_2016]\] \[[Ericsson 1973][research_ericsson_1973]\] \[[Ericsson 1975][research_ericsson_1975]\] \[[Ericsson 1989][research_ericsson_1989]\] \[[Ericsson 1970][research_ericssonle_1970]\] \[[Estruch-Samper et al 2014][research_estruchsamper_vanstone_2014]\] \[[Fagbade and Heinz 2024][research_fagbade_heinz_2024]\] \[[Ferrari et al 2021][research_ferrari_morais_2021]\] \[[Flaszynski 2016][research_flaszynski_2016]\] \[[Frew et al 1993][research_frew_galassi_1993]\] \[[Fuehrer 1969][research_fuehrer_1969]\] \[[Fulker and Ashill 1986][research_fulker_ashill_1986]\] \[[Gada and Rahai 2023][research_gada_rahai_2023]\] \[[Gahlot and Singh 2021][research_gahlot_singh_2021]\] \[[Gally 1994][research_gallythomasa_1994]\] \[[Gartner and Amitay 2016][research_gartner_amitay_2016]\] \[[Ge and Gan 2026][research_ge_gan_2026]\] \[[Geissler 1997][research_geissler_1997]\] \[[Geoghegan et al 2020][research_geoghegan_giannelis_2020_b]\] \[[Georgiadis et al 2013][research_georgiadisnicholasj_vyasmanana_2013]\] \[[Gerolymos and Vallet 2003][research_gerolymos_vallet_2003]\] \[[Gerolymos et al 2003][research_gerolymos_sauret_2003]\] \[[Giannelis and Vio 2016][research_giannelis_vio_2016]\] \[[Giepman et al 2015][research_giepman_srivastava_2015]\] \[[Goldberg and Reshotko 1980][research_goldbergu_reshotkoe_1980]\] \[[Gonsalez and Dolling 1993][research_gonsalez_dolling_1993]\] \[[Goodman et al 1985][research_goodmanwl_morrisetteel_1985]\] \[[Goodwin et al 1967][research_goodwinfk_lynesll_1967]\] \[[Gramann and Dolling 1987][research_gramann_dolling_1987]\] \[[Grasso and Falconi 1993][research_grasso_falconi_1993]\] \[[Grossi][research_grossi]\] \[[Grosvenor et al 2012][research_grosvenor_zheltovodov_2012]\] \[[Gupta][research_gupta]\] \[[Gupta et al 2021][research_gupta_datta_2021]\] \[[Hadjadj and Dussauge 2009][research_hadjadj_dussauge_2009]\] \[[Hakkinen et al 1959][research_hakkinenrj_greberi_1959]\] \[[Hamed 1993][research_hamed_1993]\] \[[Hamed and Mohamed 2001][research_hamed_mohamed_2001]\] \[[Hamed et al 1992][research_hameda_shihsh_1992]\] \[[Hamed et al 1993][research_hameda_yeuanjj_1993]\] \[[Hamid and Hasan 2015][research_hamid_hasan_2015]\] \[[Hasan and Alam 2014][research_hasan_alam_2014]\] \[[Hasan et al 2012][research_hasan_matsuo_2012]\] \[[Hatayama et al 2025][research_hatayama_tanaka_2025]\] \[[Haupt et al 1985][research_haupt_buff_1985]\] \[[Hayashi and Aso 1988][research_hayashi_aso_1988]\] \[[Reising et al][research_heathhreising_jonathansasson]\] \[[Reising and Davis][research_heathhreising_davidodavis]\] \[[Hegde et al 2015][research_hegde_funderburk_2015]\] \[[Held and Fuchs 1999][research_held_fuchs_1999]\] \[[Held and Fuchs 1999][research_held_fuchs_1999_b]\] \[[Hillier and Netterfield 1990][research_hillier_netterfield_1990]\] \[[Hingst and Jurkovich 1982][research_hingstwr_jurkovichm_1982]\] \[[Hingst and Tanji 1983][research_hingstwr_tanjift_1983]\] \[[Hirt 2015][research_hirtstefaniem_2015]\] \[[Hirt and Vyas 2013][research_hirtstefaniem_vyasmanana_2013]\] \[[Holden et al 2013][research_holden_wadhams_2013]\] \[[Holden 1966][research_holdenms_1966]\] \[[Hope and Kunz 2019][research_hope_kunz_2019]\] \[[Horstman et al 1985][research_horstmancc_kussoymi_1985]\] \[[Hou et al 2003][research_hou_clemens_2003]\] \[[Hung and Maccormack 1978][research_hungcm_maccormackrw_1978]\] \[[Hung and Buning 1984][research_hungcm_buningpg_1984]\] \[[Hung 1989][research_hungchingmao_1989]\] \[[Hung 1990][research_hungchingmao_1990]\] \[[Hung and Buning 1985][research_hungchingmao_buningpieterg_1985]\] \[[Hussaini et al 1980][research_hussainimy_baldwinbs_1980]\] \[[Inger 1976][research_inger_1976]\] \[[Inger 1979][research_inger_1979]\] \[[Inger 1979][research_inger_1979_b]\] \[[Inger 1981][research_inger_1981]\] \[[Inger 1982][research_inger_1982]\] \[[Inger 1983][research_inger_1983]\] \[[Inger 1983][research_inger_1983_b]\] \[[Inger 1988][research_inger_1988]\] \[[Inger 1988][research_inger_1988_b]\] \[[Inger 2011][research_inger_2011]\] \[[Inger and Mason 1976][research_inger_mason_1976]\] \[[Inger and Mason 1976][research_inger_mason_1976_b]\] \[[Inger and Nandanan 1986][research_inger_nandanan_1986]\] \[[Inger et al 1997][research_inger_gendt_1997]\] \[[Iyer et al 2017][research_iyer_park_2017]\] \[[Delery et al 1986][research_jdelery_jgmarvin_1986]\] \[[Jacquin et al 2005][research_jacquin_molton_2005]\] \[[Jacquin et al 2009][research_jacquin_molton_2009]\] \[[Jewell et al 2013][research_jewell_shepherd_2013]\] \[[Johnson and Papamoschou 2010][research_johnson_papamoschou_2010]\] \[[Sasson et al][research_jonathansasson_heathhreising]\] \[[Jones and Jarrett 2018][research_jones_jarrett_2018]\] \[[Ramachandra et al 2023][research_k_bhardwaj_2023]\] \[[Kalra et al 2007][research_kalra_zaidi_2007]\] \[[Kalra et al 2007][research_kalra_zaidi_2007_b]\] \[[Kandil and Menzies 1996][research_kandil_menzies_1996]\] \[[Kaneko et al 2000][research_kaneko_menshov_2000]\] \[[Karnick and Venkatraman 2017][research_karnick_venkatraman_2017]\] \[[Kashitani et al 2008][research_kashitani_yamaguchi_2008]\] \[[Kelly 1988][research_kelly_1988]\] \[[Kim and Park 2026][research_kim_park_2026]\] \[[Kim et al 1996][research_kim_matsuo_1996]\] \[[Kim et al 1996][research_kimhyun_hingstwarrenr_1996]\] \[[Kimmel et al 2015][research_kimmel_borg_2015]\] \[[Kimmel and Prabhu 2015][research_kimmelrogerl_prabhudinesh_2015]\] \[[Kleifges and Dolling 1993][research_kleifges_dolling_1993]\] \[[Klopfer and Nielsen 1980][research_klopfer_nielsen_1980]\] \[[Knight 1982][research_knight_1982]\] \[[Knight 1983][research_knight_1983]\] \[[Knight 1992][research_knight_1992]\] \[[Koren 1989][research_koren_1989]\] \[[Krishnan and Sandham 2007][research_krishnan_sandham_2007]\] \[[Krogmann et al 1984][research_krogmann_stanewsky_1984]\] \[[Krogmann et al 1985][research_krogmann_stanewsky_1985]\] \[[Kuntavanish and Cancel 1983][research_kuntavanish_cancel_1983]\] \[[Kuntz et al 1986][research_kuntz_amatucci_1986]\] \[[Kurade et al 2021][research_kurade_venkatakrishnan_2021]\] \[[Kussoy and Horstman 1992][research_kussoymi_horstmankc_1992]\] \[[Kyle et al 2001][research_kyle_orourke_2001]\] \[[Lan et al 1994][research_lan_luo_1994]\] \[[Law 1975][research_law_1975]\] \[[Lee 1990][research_lee_1990]\] \[[Lee 2001][research_lee_2001]\] \[[Lee and Gross 2022][research_lee_gross_2022]\] \[[Lee and Jin 1988][research_lee_jin_1988]\] \[[Leger and Poggie 2014][research_leger_poggie_2014]\] \[[Levin and Fabish 1962][research_levin_fabish_1962]\] \[[Levy et al 1977][research_levy_shamroth_1977]\] \[[Li 1977][research_li_1977]\] \[[Li et al 2025][research_li_he_2025]\] \[[Liou et al 2000][research_liou_huang_2000]\] \[[Liu and Squire 1986][research_liu_squire_1986]\] \[[Liu and Yang 2016][research_liu_yang_2016]\] \[[Liu et al 2022][research_liu_salazar_2022]\] \[[Lombardi et al 1997][research_lombardi_salvetti_1997]\] \[[Loth and Lee 2008][research_loth_lee_2008]\] \[[Lu and Settles 1989][research_lufrankk_settlesgarys_1989]\] \[[Lynch and Fancher 1983][research_lynch_fancher_1983]\] \[[Ma et al 2024][research_ma_yu_2024]\] \[[Maccormack 1971][research_maccormackrw_1971]\] \[[Mahalingesh][research_mahalingesh]\] \[[Mahalingesh et al 2023][research_mahalingesh_piponniau_2023]\] \[[Malkocoglu et al 2020][research_malkocoglu_barada_2020]\] \[[Manisankar and Verma 2023][research_manisankar_verma_2023]\] \[[Marino et al 2025][research_marino_eberle_2025]\] \[[Marino et al 2026][research_marino_eberle_2026]\] \[[Mark 1958][research_markherman_1958]\] \[[Martin 2011][research_martin_2011]\] \[[Mason and Inger 1975][research_mason_inger_1975]\] \[[Mateer et al 1976][research_mateer_brosh_1976]\] \[[McLean and Matoi 1986][research_mclean_matoi_1986]\] \[[McParlin and Adamczak 2003][research_mcparlin_adamczak_2003]\] \[[Melnik and Grossman 1974][research_melnikre_grossmanb_1974]\] \[[Messiter et al 1971][research_messiter_feo_1971]\] \[[Messiter and Adamson 1979][research_messiteraf_adamsontcjr_1979]\] \[[Mignosi et al 1986][research_mignosi_dor_1986]\] \[[Mirels 1977][research_mirels_1977]\] \[[Mitsuo and Aoki 2018][research_mitsuo_aoki_2018]\] \[[Modarress and Johnson 1976][research_modarress_johnson_1976]\] \[[Moroianu et al 2005][research_moroianu_caraeni_2005]\] \[[Mosbarger and King 1995][research_mosbarger_king_1995]\] \[[Mounts and Barber 1992][research_mounts_barber_1992]\] \[[Muck and Smits 1984][research_muck_smits_1984]\] \[[Mundell and Mabey 1986][research_mundell_mabey_1986]\] \[[Munguía et al 2019][research_munguia_mukhopadhaya_2019]\] \[[Murphy 1970][research_murphyjd_1970]\] \[[Murphy 1971][research_murphyjd_1971]\] \[[Murphy et al 1968][research_murphyjd_rosewc_1968]\] \[[Murray and Hillier 2009][research_murray_hillier_2009]\] \[[Runckel and Henderson 1952][research_vortex_generator_1952]\] \[[Nagarajan and Baraiya 2023][research_nagarajan_baraiya_2023]\] \[[Namura and Jeong 2013][research_namura_jeong_2013_b]\] \[[Namura et al 2013][research_namura_jeong_2013]\] \[[Narayanswami et al 1993][research_narayanswamin_horstmancc_1993]\] \[[Sasson et al 2022][research_sbli_experiments_2022]\] \[[Nicola and Cirino 2002][research_nicola_cirino_2002]\] \[[Obayashi et al 1985][research_obayashi_kuwahara_1985]\] \[[Ogawa and Babinsky 2006][research_ogawa_babinsky_2006]\] \[[Ogawa et al 2007][research_ogawa_babinsky_2007]\] \[[Ogawa et al 2008][research_ogawa_babinsky_2008]\] \[[Ogawa et al 2008][research_ogawa_watanabe_2008]\] \[[Oliver et al 2006][research_oliverab_lillardrp_2006]\] \[[Oliver et al 2007][research_oliverab_lillardrp_2007]\] \[[Om and Childs 1983][research_om_childs_1983]\] \[[Om and Childs 1985][research_om_childs_1985]\] \[[Om et al 1982][research_om_childs_1982]\] \[[Oskam et al 1978][research_oskam_vas_1978]\] \[[Oyeniran et al 2022][research_oyeniran_miyake_2022]\] \[[Padova and Falk 1980][research_padova_falk_1980]\] \[[Pal and Roy 2024][research_pal_roy_2024]\] \[[Panaras and Inger 1977][research_panaras_inger_1977]\] \[[Pane][research_pane]\] \[[Pang et al 2026][research_pang_zhang_2026]\] \[[Pearcey 1961][research_pearcey_1961]\] \[[Pickles and Narayanaswamy 2020][research_pickles_2020]\] \[[Pirozzoli and Bernardini 2010][research_pirozzoli_bernardini_2010]\] \[[Pirozzoli and Bernardini 2010][research_pirozzoli_bernardini_2010_b]\] \[[Pirozzoli et al 2010][research_pirozzoli_bernardini_2010_c]\] \[[Placek and Ruchała 2018][research_placek_ruchala_2018]\] \[[Placek and Stryczniewicz 2016][research_placek_stryczniewicz_2016]\] \[[Plotkin 1972][research_plotkinkj_1972]\] \[[Polivanov et al 2016][research_polivanov_sidorenko_2016]\] \[[Polivanov et al 2017][research_polivanov_sidorenko_2017]\] \[[Popinski 2019][research_popinski_2019]\] \[[Prabakar et al 2017][research_prabakar_srikanth_2017]\] \[[Purohit 1987][research_purohit_1987]\] \[[Raghunathan and Coll 1981][research_raghunathan_coll_1981]\] \[[Raghunathan and McLlwain 1990][research_raghunathan_mcllwain_1990]\] \[[Raghunathan et al 1979][research_raghunathan_coll_1979]\] \[[Raghunathan et al 1998][research_raghunathan_mitchell_1998]\] \[[Rahman et al 2016][research_rahman_labib_2016]\] \[[Ram et al 1985][research_ram_vemuru_1985]\] \[[Ramaswamy and Schreyer 2021][research_ramaswamy_schreyer_2021]\] \[[Ramaswamy and Schreyer 2022][research_ramaswamy_schreyer_2022]\] \[[Ramaswamy and Schreyer 2026][research_ramaswamy_schreyer_2026]\] \[[Chriss 1991][research_randallmchriss_1991]\] \[[Reda and Murphy 1972][research_redadc_murphyjd_1972]\] \[[Roscoe et al 1984][research_roscoe_shamroth_1984]\] \[[Rose 1970][research_rosewc_1970]\] \[[Rubbert et al 1976][research_rubbertpe_lup_1976]\] \[[Rumsey 2010][research_rumseychristopherl_2010]\] \[[Rushton 1966][research_rushton_1966]\] \[[Ryzhov 1993][research_ryzhov_1993]\] \[[Sansica et al 2013][research_sansica_sandham_2013]\] \[[Sansica et al 2014][research_sansica_sandham_2014]\] \[[Sartor][research_sartor]\] \[[Sartor et al 2012][research_sartor_losfeld_2012]\] \[[Sartor et al 2013][research_sartor_clement_2013]\] \[[Schmisseur and Dolling 1992][research_schmisseur_dolling_1992]\] \[[Schreyer 2023][research_schreyer_2023]\] \[[Schuelein 2014][research_schuelein_2014]\] \[[Seginer and Rose 1976][research_seginer_rose_1976]\] \[[Seifert and Pack 2001][research_seifert_pack_2001]\] \[[Sengupta et al 2021][research_sengupta_roy_2021]\] \[[Sengupta et al 2022][research_sengupta_chakraborty_2022]\] \[[Settles 1981][research_settles_1981]\] \[[Shang et al 1976][research_shang_hankeyjr_1976]\] \[[Sharma and Ghosh 2014][research_sharma_ghosh_2014]\] \[[Shea 1978][research_sheaiii_1978]\] \[[Shieh 1988][research_shieh_1988]\] \[[Shinde and Gaitonde 2022][research_shinde_gaitonde_2022]\] \[[Sidorenko et al 2017][research_sidorenko_budovskii_2017]\] \[[Singh and Sasidharan 2026][research_singh_sasidharan_2026]\] \[[Sirieix et al][research_sirieix_delery]\] \[[Sivasubramanian and Fasel 2015][research_sivasubramanian_fasel_2015]\] \[[Smith et al 2004][research_smith_babinsky_2004]\] \[[Smits 1988][research_smits_1988]\] \[[Smits and Miles 2002][research_smits_miles_2002]\] \[[Spottswood et al 2015][research_spottswood_beberniss_2015]\] \[[Sridharan et al 2024][research_sridharan_padmanabhan_2024]\] \[[Sriram and Jagadeesh 2014][research_sriram_jagadeesh_2014]\] \[[Sriram and Jagadeesh 2016][research_sriram_jagadeesh_2016]\] \[[Stacey][research_stacey]\] \[[Stallings 1982][research_stallingsjr_1982]\] \[[Stanewsky and Little 1971][research_stanewsky_little_1971]\] \[[Stubblefield et al 2025][research_stubblefield_kunz_2025]\] \[[Study on the separation 2023][research_study_on_2023_b]\] \[[Sugioka et al 2023][research_sugioka_nakajima_2023]\] \[[Sun et al 2020][research_sun_miao_2020]\] \[[Szulc et al 2023][research_szulc_doerffer_2023]\] \[[Szwaba 2005][research_szwaba_2005]\] \[[Szwaba and Doerffer 2017][research_szwaba_doerffer_2017]\] \[[Thiede and Krogmann 1986][research_thiede_krogmann_1986]\] \[[Thiede and Krogmann 1989][research_thiede_krogmann_1989]\] \[[Thomas 1991][research_thomas_1991]\] \[[Threadgill and Bruce 2014][research_threadgill_bruce_2014]\] \[[Liu et al 2021][research_tianshuliu_davidmsalazar_2021]\] \[[Tilmann 2001][research_tilmann_2001]\] \[[Tinney 2014][research_tinney_2014]\] \[[Titchener and Babinsky 2015][research_titchener_babinsky_2015]\] \[[Token 1974][research_token_1974]\] \[[Touber and Sandham 2009][research_touber_sandham_2009]\] \[[Tourrette 1993][research_tourrette_1993]\] \[[Tuck and Dostovalova 2000][research_tuck_dostovalova_2000]\] \[[Uzun and Malik 2018][research_uzun_malik_2018]\] \[[Uzun and Malik 2019][research_uzun_malik_2019]\] \[[Vadillo et al][research_vadillo_agarwal]\] \[[Vadillo et al 2005][research_vadillo_agarwal_2005]\] \[[Vaisakh and Muruganandam 2018][research_vaisakh_muruganandam_2018]\] \[[Vaisakh et al 2019][research_vaisakh_ramprakash_2019]\] \[[Vayala and Sriram 2024][research_vayala_sriram_2024]\] \[[Vayala et al 2025][research_vayala_vadlamani_2025]\] \[[Velichko and Lifshits 1983][research_velichko_lifshits_1983]\] \[[Verma and Chidambaranathan 2022][research_verma_chidambaranathan_2022]\] \[[Verma and Haidn 2009][research_verma_haidn_2009]\] \[[Verma and Manisankar 2018][research_verma_manisankar_2018]\] \[[Verma and Manisankar 2024][research_verma_manisankar_2024]\] \[[Vidal et al 1973][research_vidal_wittliff_1973]\] \[[Viswanath et al 1978][research_viswanath_sankaran_1978]\] \[[Viswanath et al 1983][research_viswanath_sankaran_1983]\] \[[Vukasinovic et al 2013][research_vukasinovic_gissen_2013]\] \[[Vyas et al 2016][research_vyasmanana_waindimmbu_2016]\] \[[Vyas et al 2018][research_vyasmanana_yoderdennisa_2018]\] \[[Vyas et al 2019][research_vyasmanana_yoderdennisa_2019]\] \[[Wai and Yoshihara 1982][research_wai_yoshihara_1982]\] \[[Wai and Yoshihara 1984][research_wai_yoshihara_1984]\] \[[Wainwright 1962][research_wainwright_1962]\] \[[Wang et al 2023][research_wang_wang_2023]\] \[[Wang et al 2024][research_wang_gan_2024]\] \[[Warning and McQuilling 2022][research_warning_mcquilling_2022]\] \[[Warning et al 2024][research_warning_lambert_2024]\] \[[Wilmoth 1977][research_wilmothrg_1977]\] \[[Wise and Sterbentz 1957][research_wisegeorgea_sterbentzwilliamh_1957]\] \[[Wollblad et al 2006][research_wollblad_davidson_2006]\] \[[Wolles 1997][research_wolles_1997]\] \[[Wong 1974][research_wong_1974]\] \[[Wong 1977][research_wong_1977]\] \[[Wu 1975][research_wu_1975]\] \[[Wu et al 1977][research_wu_chen_1977]\] \[[Xiao and Tsai 2004][research_xiao_tsai_2004_b]\] \[[Yamamoto et al 2012][research_yamamoto_tanaka_2012]\] \[[Yang et al 2015][research_yang_yan_2015]\] \[[Yang et al 2016][research_yang_yao_2016]\] \[[Yang and Greber 1993][research_yangweili_greberisaac_1993]\] \[[Yoon and Chung 1996][research_yoon_chung_1996]\] \[[Yoshikawa 1982][research_yoshikawa_1982]\] \[[You et al 2013][research_you_bromby_2013]\] \[[Zater and Bahi 2024][research_zater_bahi_2024]\] \[[Zebiri et al 2019][research_zebiri_piquet_2019]\] \[[Zhang 2013][research_zhang_2013]\] \[[Zhang et al 2020][research_zhang_ma_2020]\] \[[Zhang et al 2022][research_zhang_hirahara_2022]\] \[[Zhang et al 2024][research_zhang_tian_2024]\] \[[Zhao 2016][research_zhao_2016]\] \[[Zhao et al 2026][research_zhao_yang_2026]\] \[[Zhou et al 2017][research_zhou_chen_2017]\] \[[Zhou et al 2017][research_zhou_hou_2017]\] \[[Zhu et al 2019][research_zhu_li_2019]\]

### Aeroelasticity, flutter and flight loads

**The structure the unknown loads were designed against.** Transonic flutter, static aeroelasticity, flight loads and their measurement by strain gauge and pressure survey.

**370 records.** \[[Abraham-Doman and Merrett 2014][research_abrahamdoman_merrett_2014]\] \[[Aerodynamic and Static Aeroelastic 2014][research_aerodynamic_and_2014]\] \[[Aeroelasticity Problems in Compressible 2010][research_aeroelasticity_problems_2010]\] \[[Afkhami and Alighanbari 2007][research_afkhami_alighanbari_2007]\] \[[Alder 2014][research_alder_2014]\] \[[Alder 2015][research_alder_2015]\] \[[Allen 1954][research_allen_1954]\] \[[Allen et al 2005][research_allen_lizotte_2005]\] \[[Arizono et al 2008][research_arizono_kheirandish_2008]\] \[[Armstrong et al 2006][research_armstrong_lindberg_2006]\] \[[Asadi and Farsadi 2020][research_asadi_farsadi_2020]\] \[[Ashley 1979][research_ashley_1979]\] \[[Ashley 1980][research_ashley_1980]\] \[[Aul'chenko et al 2010][research_aulchenko_zamuraev_2010]\] \[[Auls'chenko et al 2006][research_aulschenko_zamuraev_2006]\] \[[Avkhadiev et al 1995][research_avkhadiev_elizarov_1995]\] \[[Banavara and Dimitrov 2014][research_banavara_dimitrov_2014]\] \[[Bekemeyer and Timme 2017][research_bekemeyer_timme_2017]\] \[[Bendiksen 1987][research_bendiksen_1987]\] \[[Bendiksen 1992][research_bendiksen_1992]\] \[[Bendiksen 1994][research_bendiksen_1994]\] \[[Bendiksen 1998][research_bendiksen_1998]\] \[[Bendiksen 1999][research_bendiksen_1999]\] \[[Bendiksen 2004][research_bendiksen_2004]\] \[[Bendiksen 2004][research_bendiksen_2004_b]\] \[[Bendiksen 2006][research_bendiksen_2006]\] \[[Bendiksen 2007][research_bendiksen_2007]\] \[[Bendiksen 2008][research_bendiksen_2008]\] \[[Bendiksen 2009][research_bendiksen_2009]\] \[[Bendiksen 2009][research_bendiksen_2009_b]\] \[[Bendiksen 2013][research_bendiksen_2013]\] \[[Bendiksen 2015][research_bendiksen_2015]\] \[[Bendiksen and Davis 1995][research_bendiksen_davis_1995]\] \[[Bendiksen and Hwang 1996][research_bendiksen_hwang_1996]\] \[[Bendiksen et al 1997][research_bendiksen_hwang_1997]\] \[[Bendiksen and Kousen 1989][research_bendiksenoddvaro_kousenkennetha_1989]\] \[[Bennett and Abel 1981][research_bennett_abel_1981]\] \[[Bennett et al 1988][research_bennett_batina_1988]\] \[[Bennett et al 1989][research_bennett_batina_1989]\] \[[Bennett and Batina 1989][research_bennettrobertm_batinajohnt_1989]\] \[[Beran and Morton 1997][research_beran_morton_1997]\] \[[Bhat 2018][research_bhat_2018]\] \[[Bhatia and Beran 2014][research_bhatia_beran_2014]\] \[[Bhatia and Beran 2016][research_bhatia_beran_2016]\] \[[Bhatia and Beran 2017][research_bhatia_beran_2017]\] \[[Bhatia and Beran 2017][research_bhatia_beran_2017_b]\] \[[Bhatia and Beran 2017][research_bhatia_beran_2017_c]\] \[[Bland and Edwards 1983][research_bland_edwards_1983]\] \[[Bons and Martins 2020][research_bons_martins_2020]\] \[[Borland and Rizzetta 1981][research_borland_rizzetta_1981]\] \[[Borland and Rizzetta 1982][research_borland_rizzetta_1982]\] \[[Borland and Manro 1983][research_borlandcj_manrome_1983]\] \[[Boswinkle and Smith 1958][research_boswinklerwjr_smithsliii_1958]\] \[[Boyd 1977][research_boyd_1977]\] \[[Stanford and Jacobson][research_bretkstanford_kevinejacobson]\] \[[Stanford et al][research_bretkstanford_andrewsthelen]\] \[[Stanford et al][research_bretkstanford_anniesauer]\] \[[Stanford et al][research_bretkstanford_stevenjmassey]\] \[[Burris and Bender 1969][research_burris_bender_1969]\] \[[Busan 1998][research_busan_1998]\] \[[Buxbaum and Svenson 1972][research_buxbaum_svenson_1972]\] \[[Buxton et al 1997][research_buxton_beran_1997]\] \[[Byreddy et al 2003][research_byreddy_grandhi_2003]\] \[[Carloni and Azevedo 2023][research_carloni_azevedo_2023]\] \[[Casey 1988][research_casey_1988]\] \[[Castellani et al 2016][research_castellani_cooper_2016]\] \[[Cenko and Madson 1993][research_cenko_madson_1993]\] \[[Chen et al 2002][research_chen_sulaeman_2002]\] \[[Chen et al 2006][research_chen_zha_2006]\] \[[Chen et al 2020][research_chen_gao_2020]\] \[[Chen et al 2026][research_chen_zhang_2026]\] \[[Cheng 1982][research_cheng_1982]\] \[[Chestnutt 1966][research_chestnutt_1966]\] \[[Chipman et al 1985][research_chipman_rauch_1985]\] \[[Clarke et al 2005][research_clarke_allen_2005]\] \[[Coates and Thamburaj 2008][research_coates_thamburaj_2008]\] \[[Colera and Pérez-Saborid 2018][research_colera_perezsaborid_2018]\] \[[Collar 1946][research_collar_1946]\] \[[Cunningham et al 1989][research_cunninghamherbertj_bennettrobertm_1989]\] \[[Currao 2024][research_currao_2024]\] \[[Currao and He 2024][research_currao_he_2024]\] \[[Currao and Yeh 2026][research_currao_yeh_2026]\] \[[Davis and Bendiksen 1993][research_davis_bendiksen_1993]\] \[[Deangelis 1981][research_deangelis_1981]\] \[[Dimitriadis 2025][research_dimitriadis_2025]\] \[[Djayapertapa and Allen 2002][research_djayapertapa_allen_2002]\] \[[Djayapertapa and Allen 2004][research_djayapertapa_allen_2004]\] \[[Dobbs and Hodson 1979][research_dobbssk_hodsonch_1979]\] \[[Doggett and Cunningham 1976][research_doggettrvjr_cunninghamhj_1976]\] \[[Doggett et al 1959][research_doggettrvjr_morganhg_1959]\] \[[Doggett et al 1989][research_doggettrobertvjr_soistmanndavidl_1989]\] \[[Dowell 1986][research_dowell_1986]\] \[[Dowell and Hall 2003][research_dowell_hall_2003]\] \[[Dowell and Ilgamov 1988][research_dowell_ilgamov_1988]\] \[[Dugundji 1965][research_dugundji_1965]\] \[[Dugundji et al 1962][research_dugundji_dowell_1962]\] \[[Eastep and Olsen 1979][research_eastep_olsen_1979]\] \[[Eastep and Olsen 1980][research_eastep_olsen_1980]\] \[[Ecer 1989][research_ecer_1989]\] \[[Edwards et al 1982][research_edwards_bennett_1982]\] \[[Edwards et al 2001][research_edwards_schuster_2001]\] \[[Edwards et al 2009][research_edwards_spain_2009]\] \[[Erickson et al 1989][research_erickson_schreiner_1989]\] \[[Evaluation of methods for 1981][research_evaluation_of_1981]\] \[[Experimental transonic flutter characteristics 1990][research_experimental_transonic_1990]\] \[[Farhat 1998][research_farhat_1998]\] \[[Farhat 2000][research_farhat_2000]\] \[[Farhat 2001][research_farhat_2001]\] \[[Farsadi et al 2019][research_farsadi_asadi_2019]\] \[[Feng 2023][research_feng_2023]\] \[[Finaish et al 1995][research_finaish_frigerio_1995]\] \[[Flight-Loads Prediction and Structural-Life 1981][research_flight_loads_prediction_1981]\] \[[Foughner and Bensinger 1977][research_foughnerjtjr_bensingerct_1977]\] \[[French 1988][research_french_1988]\] \[[Fugate et al 2019][research_fugate_nguyen_2019]\] \[[Fuhs 1971][research_fuhs_1971]\] \[[Fung and Shieh 1993][research_fung_shieh_1993]\] \[[Gadsden and Habibi 2007][research_gadsden_habibi_2007]\] \[[Gallman et al 1986][research_gallman_yang_1986]\] \[[Gallman et al 1988][research_gallman_batina_1988]\] \[[Garrelick et al 1997][research_garrelick_martini_1997]\] \[[Garrick and Reed 1981][research_garrick_reed_1981]\] \[[Ghoreyshi et al 2013][research_ghoreyshi_cummings_2013]\] \[[Gilman 1961][research_gilmanjjr_1961]\] \[[Gloss and Washburn 1977][research_gloss_washburn_1977]\] \[[Gloss and Washburn 1978][research_gloss_washburn_1978]\] \[[Goates et al 2025][research_goates_vandommelen_2025]\] \[[Godavarthi et al 2026][research_godavarthi_seo_2026]\] \[[Goetz 1972][research_goetzrc_1972]\] \[[Goetz and Stonesifer 1961][research_goetzrc_stonesiferjc_1961]\] \[[Goland et al 1954][research_goland_luke_1954]\] \[[Gong et al 2024][research_gong_wang_2024]\] \[[Gordnier and Melville 1998][research_gordnier_melville_1998]\] \[[Gordnier and Melville 2000][research_gordnier_melville_2000]\] \[[Graham 1947][research_grahamdonaldj_1947]\] \[[Green and Fernandez 1994][research_green_fernandez_1994]\] \[[Grohmann et al 1999][research_grohmann_kroplin_1999]\] \[[Grosser et al 1983][research_grosserwf_brittrt_1983]\] \[[Gurley and Ruhlin 1962][research_gurleyjrjr_ruhlincl_1962]\] \[[Guruswamy and Tu 1988][research_guruswamy_tu_1988]\] \[[Guruswamy and Tu 1989][research_guruswamy_tu_1989]\] \[[Halder et al 2019][research_halder_damodaran_2019]\] \[[Hart 1984][research_hart_1984]\] \[[He and Cui 2022][research_he_cui_2022]\] \[[He and Williams 2022][research_he_williams_2022]\] \[[He and Williams 2023][research_he_williams_2023]\] \[[He et al 2014][research_he_yang_2014]\] \[[Heeg and Chwalowski 2017][research_heeg_chwalowski_2017]\] \[[Heeg and Chwalowski 2019][research_heegjennifer_chwalowskipawel_2019]\] \[[Hitch 1981][research_hitch_1981]\] \[[Hoshi et al 2020][research_hoshi_kuya_2020]\] \[[Hu et al 2024][research_hu_lu_2024]\] \[[Hubbard et al 2014][research_hubbard_fontenot_2014]\] \[[Huo et al 2026][research_huo_wang_2026]\] \[[Imai et al 2021][research_imai_nakakita_2021]\] \[[Imai et al 2022][research_imai_nakakita_2022]\] \[[Ishii and Yanagizawa 1967][research_ishiit_yanagizawam_1967]\] \[[Isogai 1979][research_isogai_1979]\] \[[Isogai 1981][research_isogai_1981]\] \[[Jacobson et al 2021][research_jacobson_stanford_2021]\] \[[Jameson et al 2008][research_jameson_vassberg_2008]\] \[[Janardhan et al 2003][research_janardhan_grandhi_2003_b]\] \[[Jirasek et al 2014][research_jirasek_cavagna_2014]\] \[[Jones and Platzer 1998][research_jones_platzer_1998]\] \[[Jones and Unangst 1963][research_jonesgwjr_unangstjr_1963]\] \[[Jutte et al 2024][research_jutte_mason_2024]\] \[[Kapania and Issac 1994][research_kapania_issac_1994]\] \[[Kapania et al 1993][research_kapaniarakeshk_issacjasonc_1993]\] \[[Kassem and Banerjee][research_kassem_banerjee]\] \[[Kawakami et al 2007][research_kawakami_takatoya_2007]\] \[[Kearns 1962][research_kearns_1962]\] \[[Kehoe 1988][research_kehoe_1988]\] \[[Jacobson and Stanford][research_kevinejacobson_bretkstanford_b]\] \[[Jacobson et al][research_kevinejacobson_bretkstanford]\] \[[Khan et al 2021][research_khan_mallik_2021]\] \[[Khan et al 2023][research_khan_kapania_2023]\] \[[Kholodar et al 2002][research_kholodar_thomas_2002]\] \[[Kholodar et al 2004][research_kholodar_dowell_2004_b]\] \[[Kikuchi et al 2026][research_kikuchi_miyake_2026]\] \[[Kim and Lee 2001][research_kim_lee_2001]\] \[[Klifi and Lili 2013][research_klifi_lili_2013]\] \[[Klyde et al 2004][research_klyde_harris_2004]\] \[[Kodigaddi 2026][research_kodigaddi_2026]\] \[[Kolonay and Yang 1998][research_kolonay_yang_1998]\] \[[Kousen and Bendiksen 1994][research_kousen_bendiksen_1994]\] \[[Krener 2001][research_krener_2001]\] \[[Kuhl et al 1958][research_kuhlae_littlemv_1958]\] \[[Kukreja 2008][research_kukreja_2008]\] \[[Kuzmin and Babarykin 2023][research_kuzmin_babarykin_2023]\] \[[Kuzmina et al 2018][research_kuzmina_ishmuratov_2018]\] \[[Kwon et al 2005][research_kwon_park_2005]\] \[[Lauten et al 1954][research_lautenwtjr_lundstromrr_1954]\] \[[Lee 2008][research_lee_2008]\] \[[Lee and Eyi 1991][research_lee_eyi_1991]\] \[[Lee and Eyi 1993][research_lee_eyi_1993]\] \[[Lee et al 2006][research_lee_lee_2006]\] \[[Li and Qin 2020][research_li_qin_2020]\] \[[Liu and Mignolet 2005][research_liu_mignolet_2005]\] \[[Liu et al 2016][research_liu_zhao_2016]\] \[[Liu et al 2020][research_liu_gao_2020]\] \[[Liu et al 2023][research_liu_pang_2023]\] \[[Lokos et al 2002][research_lokos_olney_2002]\] \[[Lokos et al 2005][research_lokos_lizotte_2005]\] \[[Long 2006][research_long_2006]\] \[[Lu and Yeh 1993][research_lu_yeh_1993]\] \[[Lu et al 1995][research_lu_pan_1995]\] \[[Lundstrom et al 1948][research_lundstromreginaldr_lautenwilliamtjr_1948]\] \[[Machida et al 2005][research_machida_kikuchi_2005]\] \[[Madson and Talbot 1996][research_madson_talbot_1996]\] \[[Maewal 1984][research_maewal_1984]\] \[[Mai 2025][research_mai_2025]\] \[[Maines et al 2007][research_maines_smith_2007]\] \[[Mallik et al 2013][research_mallik_kapania_2013]\] \[[Malvestudo et al 1957][research_malvestudofranks_cooneythomasv_1957]\] \[[Maskew 1983][research_maskewb_1983]\] \[[Mathur et al 2004][research_mathur_carr_2004]\] \[[Matsushita and Miyata 2003][research_matsushita_miyata_2003]\] \[[Matsushita et al][research_matsushita_miyata]\] \[[Matsushita et al][research_matsushita_miyata_b]\] \[[Medan et al 1981][research_medanrt_magnusae_1981]\] \[[Mellquist and Bendiksen 2014][research_mellquist_bendiksen_2014]\] \[[Mellquist and Bendiksen 2015][research_mellquist_bendiksen_2015]\] \[[Miskin and Takahashi 2019][research_miskin_takahashi_2019]\] \[[Miyaji and Takegawa 2022][research_miyaji_takegawa_2022]\] \[[Miyake and Terashima 2022][research_miyake_terashima_2022]\] \[[Miyake and Terashima 2023][research_miyake_terashima_2023]\] \[[Mohr et al 1988][research_mohr_yang_1988]\] \[[Molyneux 1960][research_molyneux_1960]\] \[[Moosavi et al 2005][research_moosavi_naddafoskouei_2005]\] \[[Morton and Beran 1995][research_morton_beran_1995]\] \[[Morton and Beran 1996][research_morton_beran_1996]\] \[[Morton and Beran 1996][research_morton_beran_1996_b]\] \[[Morton and Beran 1999][research_morton_beran_1999]\] \[[Mottershead and Cooper 2012][research_mottershead_cooper_2012]\] \[[Murphy et al 1983][research_murphy_rogers_1983]\] \[[Myers et al 1983][research_myersmr_guruswamyp_1983]\] \[[NACA Conference on Aircraft 1957][research_loads_flutter_conf_1957]\] \[[Nakakita and Arizono 2009][research_nakakita_arizono_2009]\] \[[Flight Flutter Testing Symposium 1975][research_flutter_symposium_1975]\] \[[Pena et al 2018][research_fiber_optic_loads_2018]\] \[[Naval Air Systems Command Patuxent River Md 1999][research_navalairsystemscommandpatuxentrivermd_1999]\] \[[Naval Air Systems Command Patuxent River Md 2000][research_navalairsystemscommandpatuxentrivermd_2000]\] \[[Nellessen et al 1996][research_nellessen_britten_1996]\] \[[Newton 1965][research_newton_1965]\] \[[Nguyen and Xiong 2022][research_nguyen_xiong_2022]\] \[[Nguyen et al 2019][research_nguyen_fugate_2019]\] \[[Nguyen et al][research_nhannguyen_jasonfugate]\] \[[Nicolas et al 2016][research_nicolas_sullivan_2016]\] \[[Niven and Tait 2000][research_niven_tait_2000]\] \[[O'Kelly 1954][research_okellyburker_1954]\] \[[Opgenoord et al 2017][research_opgenoord_drela_2017]\] \[[Opstal 2011][research_opstal_2011]\] \[[Oskam 1983][research_oskam_1983]\] \[[Otiefy and Negm 2010][research_otiefy_negm_2010]\] \[[Otiefy and Negm 2011][research_otiefy_negm_2011]\] \[[Pak et al 1991][research_pak_friedmann_1991]\] \[[Pak et al 1995][research_pak_friedmann_1995]\] \[[Patel and Lefas 2025][research_patel_lefas_2025]\] \[[Patel and Lefas 2026][research_patel_lefas_2026]\] \[[Perkins and Brice 1966][research_perkins_brice_1966]\] \[[Piette et al 1985][research_piette_crooks_1985]\] \[[Piette and Cazier 1989][research_piettedouglass_cazierfrankwjr_1989]\] \[[Prediction of transonic flutter 1981][research_prediction_of_1981]\] \[[Raab and Rohde-Brandenburger 2020][research_raab_rohdebrandenburger_2020]\] \[[Ragni et al 2009][research_ragni_ashok_2009]\] \[[Rakin 1981][research_rakin_1981]\] \[[Ramkumar and Weisshaar 1977][research_ramkumar_weisshaar_1977]\] \[[Reddy et al 1988][research_reddy_srivastava_1988]\] \[[Reed 1985][research_reedwhiii_1985]\] \[[Regier et al 1947][research_regierarthura_barmbyjohng_1947]\] \[[Richard and Putter 2003][research_richard_putter_2003]\] \[[Rizzetta 1977][research_rizzetta_1977]\] \[[Rogers 1970][research_rogers_1970]\] \[[Rosen 1988][research_rosen_1988]\] \[[Ruhlin et al 1983][research_ruhlin_rauch_1983]\] \[[Ruhlin and Young 1964][research_ruhlincl_youngls_1964]\] \[[Ruhlin et al 1986][research_ruhlincl_bhatiakg_1986]\] \[[Bland 1979][research_srbland_1979]\] \[[Saitoh et al 2012][research_saitoh_tamayama_2012]\] \[[Sandford et al 1974][research_sandford_abel_1974]\] \[[Sandford et al 1974][research_sandfordmc_ruhlincl_1974]\] \[[Scanlan 1948][research_scanlan_1948]\] \[[Schewe and Mai 2018][research_schewe_mai_2018]\] \[[Schewe and Mai 2019][research_schewe_mai_2019]\] \[[Shahjahan and Ahuja 2026][research_shahjahan_ahuja_2026]\] \[[Shankar and Ide 1989][research_shankar_ide_1989]\] \[[Shi et al 2023][research_shi_he_2023]\] \[[Silva et al 2002][research_silva_mello_2002]\] \[[Singh et al 2016][research_singh_mishra_2016]\] \[[Smith and Richards 2023][research_smith_richards_2023]\] \[[Soneda et al 2025][research_soneda_tsushima_2025]\] \[[Song et al 2011][research_song_lu_2011]\] \[[Srivastava et al 2002][research_srivastava_bakhle_2002]\] \[[Srivastava et al 2019][research_srivastava_damodaran_2019]\] \[[Stanford and Jacobson 2023][research_stanford_jacobson_2023]\] \[[Stanford and Jacobson 2024][research_stanford_jacobson_2024]\] \[[Stanford et al 2015][research_stanford_wieseman_2015]\] \[[Stanford et al 2022][research_stanford_sauer_2022]\] \[[Stanford et al 2024][research_stanford_thelen_2024]\] \[[Stanford et al 2025][research_stanford_thelen_2025]\] \[[Stanford et al 2026][research_stanford_massey_2026]\] \[[Stardter 1979][research_stardterh_1979]\] \[[Static Aeroelasticity Effect 2014][research_static_aeroelasticity_2014]\] \[[Steimle et al 2010][research_steimle_schroder_2010]\] \[[Stevenson 1981][research_stevensonjr_1981]\] \[[Strganac 1988][research_strganac_1988]\] \[[Striz 1991][research_striz_1991]\] \[[Szwabowski and Baker 2023][research_szwabowski_baker_2023]\] \[[Takahashi 2021][research_takahashi_2021]\] \[[Takahashi 2021][research_takahashi_2021_b]\] \[[Terashima and Fujii 2003][research_terashima_fujii_2003]\] \[[Terashima and Fujii 2004][research_terashima_fujii_2004]\] \[[Terashima and Fujii 2007][research_terashima_fujii_2007]\] \[[Thawait et al 2022][research_thawait_tandaiya_2022]\] \[[Theodorsen 1935][research_theodorsen_1935]\] \[[Thomas et al 2001][research_thomas_dowell_2001]\] \[[Tjatra et al 1992][research_tjatra_kapania_1992]\] \[[Transonic Wing Flutter Analysis 2005][research_transonic_wing_2005]\] \[[Triplett 1980][research_triplett_1980]\] \[[Triplett et al 1973][research_triplett_kappus_1973]\] \[[Turner et al 2023][research_turner_seo_2023]\] \[[Turner et al 2024][research_turner_seo_2024]\] \[[Turner et al 2024][research_turner_seo_2024_b]\] \[[Ueda 1983][research_ueda_1983]\] \[[Ullah et al 2021][research_ullah_lutz_2021]\] \[[Ullah et al 2022][research_ullah_kamoun_2022]\] \[[Unangst 1959][research_unangstjohnr_1959]\] \[[Vaiuso et al 2025][research_vaiuso_immordino_2025]\] \[[Vaiuso et al 2025][research_vaiuso_immordino_2025_b]\] \[[Voracek 2007][research_voracekdavid_2007]\] \[[Waisanen and Perangelo 1972][research_waisanen_perangelo_1972]\] \[[Waite et al 2019][research_waite_stanford_2019]\] \[[Wang et al 2024][research_wang_guo_2024]\] \[[Wang et al 2026][research_wang_song_2026]\] \[[Weatherill and Ehlers 1983][research_weatherill_ehlers_1983]\] \[[Weatherill and Zartarian 1958][research_weatherill_zartarian_1958]\] \[[Weber et al 1999][research_weber_jones_1999]\] \[[Weber et al 2001][research_weber_jones_2001]\] \[[Weisshaar 1972][research_weisshaar_1972]\] \[[Weisshaar 1979][research_weisshaar_1979]\] \[[Whitcomb 1944][research_whitcombrichardt_1944]\] \[[Wieseman et al 2005][research_wieseman_silva_2005]\] \[[Wing Loads 1996][research_wing_loads_1996]\] \[[Witteveen and Bijl 2009][research_witteveen_bijl_2009]\] \[[Xiong et al 2022][research_xiong_nguyen_2022_b]\] \[[Yan et al 2016][research_yan_ragab_2016]\] \[[Yan et al 2017][research_yan_ragab_2017]\] \[[Yang and Wan 1978][research_yang_wan_1978]\] \[[Yang et al 1980][research_yang_guruswamy_1980]\] \[[Yang et al 1980][research_yang_guruswamy_1980_b]\] \[[Yang et al 1980][research_yang_striz_1980]\] \[[Yang et al 1981][research_yang_guruswamy_1981]\] \[[Yang et al 1981][research_yang_striz_1981]\] \[[Yang et al 2016][research_yang_he_2016]\] \[[Yang et al 2017][research_yang_huang_2017]\] \[[Yang et al 2019][research_yang_huang_2019]\] \[[Yates 1963][research_yates_1963]\] \[[Yates et al 1982][research_yates_wynne_1982]\] \[[Yates et al 1983][research_yates_wynne_1983]\] \[[Yates et al 1982][research_yatesjr_wynne_1982]\] \[[Yongping et al 2026][research_yongping_zengjun_2026]\] \[[Zeng et al 2012][research_zeng_chen_2012]\] \[[Zhang et al 2008][research_zhang_xu_2008]\] \[[Zhang et al 2016][research_zhang_ding_2016]\] \[[Zhang et al 2021][research_zhang_guo_2021]\] \[[Zhao et al 2024][research_zhao_li_2024]\] \[[Zhao et al 2012][research_zhao_zhu_2012]\] \[[Zhou et al 2016][research_zhou_li_2016]\] \[[Zwaan 1984][research_zwaan_1984]\] \[[Ángel Muñoz and Colera 2020][research_angelmunoz_colera_2020]\]

### Reynolds number, transition and the scale problem

**Why the tunnel and the aeroplane disagreed.** Reynolds number effects at transonic speed, boundary-layer transition in tunnels and in flight, laminar flow and the high-Reynolds-number facilities built to close the gap.

**297 records.** \[[Ahlefeldt 2017][research_ahlefeldt_2017]\] \[[Ahmed et al 1989][research_ahmed_wentz_1989]\] \[[Albrecht et al 2022][research_albrecht_olson_2022]\] \[[Alexander et al 1973][research_alexander_griffin_1973]\] \[[Anders et al 1998][research_andersjb_andersonwk_1998]\] \[[Anyoji et al 2015][research_anyoji_numata_2015]\] \[[Archambaud et al 2004][research_archambaud_louis_2004]\] \[[Asai et al 1996][research_asai_kanda_1996]\] \[[Asai et al 1997][research_asai_kanda_1997]\] \[[Aulehla 1992][research_aulehla_1992]\] \[[Azzazy et al 1987][research_azzazy_modarress_1987]\] \[[Azzazy et al 1989][research_azzazy_modarress_1989]\] \[[Back 1970][research_back_1970]\] \[[Balakumar 2018][research_balakumar_2018]\] \[[Barnes and Visbal 2017][research_barnes_visbal_2017]\] \[[Barnes and Visbal 2018][research_barnes_visbal_2018]\] \[[Barnes and Visbal 2020][research_barnes_visbal_2020]\] \[[Barnes and Visbal 2021][research_barnes_visbal_2021]\] \[[Barnes and Visbal 2023][research_barnes_visbal_2023]\] \[[Belisle et al 2010][research_belisle_neale_2010]\] \[[Belisle et al 2012][research_belisle_roberts_2012]\] \[[Berkowitz et al 1977][research_berkowitz_kyriss_1977]\] \[[Bhat 1971][research_bhat_1971]\] \[[Bidwell 1991][research_bidwell_1991]\] \[[Bobbitt 1990][research_bobbitt_1990]\] \[[Bobenrieth Miserda et al 2006][research_bobenriethmiserda_lauterjung_2006]\] \[[Borovoy et al 2012][research_borovoy_mosharov_2012]\] \[[Boundary-layer-transition measurements on hemispheres 1959][research_boundary_layer_transition_measurements_1959]\] \[[Bourdet et al 2003][research_bourdet_bouhadji_2003]\] \[[Braune and Hebler 2018][research_braune_hebler_2018]\] \[[Hiller et al][research_bretthiller_richardcampbell]\] \[[Brion et al 2017][research_brion_dandois_2017]\] \[[Burdges et al 1975][research_burdgeskp_blackwelljajr_1975]\] \[[Busquet][research_busquet]\] \[[Campbell et al 1986][research_campbell_waggoner_1986]\] \[[Chang et al 2022][research_chang_cai_2022]\] \[[Chase 1992][research_chase_1992]\] \[[Chen et al 2023][research_chen_wei_2023]\] \[[Chu and Lawing 1990][research_chujulio_lawingpiercel_1990]\] \[[Chu et al 1990][research_chujulio_flechnerstuartg_1990]\] \[[Chung 2000][research_chung_2000_b]\] \[[Ciobaca and Dandois 2017][research_ciobaca_dandois_2017]\] \[[Clark and Pelkman 2001][research_clark_pelkman_2001]\] \[[Coder 2021][research_coder_2021]\] \[[Coder 2023][research_coder_2023]\] \[[Coder 2025][research_coder_2025]\] \[[Coder 2026][research_coder_2026]\] \[[Cogo 2024][research_cogo_2024]\] \[[Collazo Garcia and Ansell 2018][research_collazogarcia_ansell_2018]\] \[[Collazo Garcia et al 2021][research_collazogarcia_saxtonfox_2021]\] \[[Collins 1974][research_collins_1974]\] \[[Cook et al 1975][research_cookwj_presleyll_1975]\] \[[Cook et al 1978][research_cookwj_chaneymj_1978]\] \[[Cook et al 1978][research_cookwj_presleyll_1978]\] \[[Cornish 1963][research_cornish_1963]\] \[[Crowder 2018][research_crowder_2018]\] \[[Curtin et al 2002][research_curtinmm_boguedr_2002]\] \[[D'Afiero 2025][research_dafiero_2025]\] \[[Deiwert 1974][research_deiwert_1974]\] \[[Deiwert 1975][research_deiwert_1975]\] \[[Deiwert 1975][research_deiwertgs_1975]\] \[[Deiwert and Bailey 1979][research_deiwertgs_baileyhe_1979]\] \[[Demetriades 1977][research_demetriades_1977]\] \[[Denison et al 2019][research_denisonmarie_garaianirban_2019]\] \[[Dougherty 2021][research_dougherty_2021]\] \[[Dougherty and Fisher 1980][research_doughertyjr_fisher_1980]\] \[[Dougherty and Steinle 1974][research_doughertyjr_steinlejr_1974]\] \[[Drela 1991][research_drela_1991]\] \[[Drela 1992][research_drela_1992]\] \[[Drela and Giles 1986][research_drela_giles_1986]\] \[[Du et al 2026][research_du_yu_2026]\] \[[Edwards 2008][research_edwards_2008]\] \[[Egorov 2025][research_egorov_2025]\] \[[Eppink 2023][research_eppink_2023]\] \[[Beyak et al][research_ethansbeyak_meelanchoudhari]\] \[[Falco 1991][research_falco_1991]\] \[[Fan et al 2005][research_fan_yi_2005]\] \[[Fan et al 2021][research_fan_yu_2021]\] \[[Fauci et al 2006][research_fauci_nicoli_2006]\] \[[Fehrs and Helm 2025][research_fehrs_helm_2025]\] \[[Fisher and Cobleigh 1994][research_fisher_cobleigh_1994]\] \[[Freudinger and Kehoe 1990][research_freudingerlawrencec_kehoemichaelw_1990]\] \[[Furlong and Fitzpatrick 1947][research_furlonggchester_fitzpatrickjamese_1947]\] \[[Gartenberg et al 1992][research_gartenberg_johnson_1992]\] \[[Geib and Maidnik 1983][research_geib_maidnik_1983]\] \[[Goldhammer and Steinle 1990][research_goldhammermarki_steinlefrankwjr_1990]\] \[[Goldstein 2004][research_goldstein_2004]\] \[[Goodrich et al 1983][research_goodrich_derry_1983]\] \[[Goradia et al 1989][research_goradiash_bobbittpj_1989]\] \[[Guilarte Herrero et al 2021][research_guilarteherrero_noguchi_2021]\] \[[Gupta and Ansell 2018][research_gupta_ansell_2018]\] \[[Gürdamar et al 2006][research_gurdamar_cete_2006]\] \[[Hader and Fasel 2023][research_hader_fasel_2023]\] \[[Haines 2000][research_haines_2000]\] \[[Hall and Kern 1996][research_hall_kern_1996]\] \[[Hall et al 1989][research_hall_carraway_1989]\] \[[Han et al 2016][research_han_chen_2016]\] \[[Hara and Abe 2008][research_hara_abe_2008]\] \[[Harris et al 1989][research_harrischarlesd_brookscuylerwjr_1989]\] \[[Harvey and Bobbitt 1981][research_harvey_bobbitt_1981]\] \[[Harvey and Pride 1982][research_harveywd_pridejd_1982]\] \[[Hellstrom et al 1994][research_hellstrom_davidson_1994]\] \[[Helm et al 2024][research_helm_grabe_2024]\] \[[Hess et al 1987][research_hess_seidel_1987]\] \[[Hess et al 1989][research_hess_seidel_1989]\] \[[Hess 1989][research_hessrw_1989]\] \[[Hickey et al 2016][research_hickey_hussain_2016]\] \[[Hiller et al 2025][research_hiller_campbell_2025]\] \[[Holmes et al 1986][research_holmes_croom_1986]\] \[[Hong and Jung 2024][research_hong_jung_2024]\] \[[Horstmann et al 1990][research_horstmann_quast_1990]\] \[[Hu et al 2025][research_hu_huang_2025]\] \[[Husain et al 2026][research_husain_piotrowski_2026]\] \[[Inger 1984][research_inger_1984]\] \[[Inger 1985][research_inger_1985]\] \[[Jackson 1978][research_jackson_1978]\] \[[Jacobs et al 1939][research_jacobsen_abbottirah_1939]\] \[[Jenkins 1983][research_jenkinsrv_1983]\] \[[Jiménez Navarro][research_jimeneznavarro]\] \[[Johnson et al 1986][research_johnsoncb_johnsonwgjr_1986]\] \[[Johnson et al 1986][research_johnsoncharlesb_dressdavida_1986]\] \[[Johnson and Hill 1985][research_johnsonwgjr_hillas_1985_c]\] \[[Johnson et al 1982][research_johnsonwgjr_hillas_1982]\] \[[Johnson et al 1985][research_johnsonwgjr_hillas_1985]\] \[[Johnson et al 1985][research_johnsonwgjr_hillas_1985_b]\] \[[Jun et al 2009][research_jun_zhenghong_2009]\] \[[Kamboj 2026][research_kamboj_2026]\] \[[Katanoda et al 2001][research_katanoda_handa_2001]\] \[[Kelnhofer 1969][research_kelnhofer_1969]\] \[[Kendall 1982][research_kendall_1982]\] \[[Kilgore et al 1974][research_kilgore_adcock_1974]\] \[[Kim and Chang 2009][research_kim_chang_2009]\] \[[Klein 2019][research_klein_2019]\] \[[Klioutchnikov and Ballmann][research_klioutchnikov_ballmann]\] \[[Kluwick and Kornfeld 2013][research_kluwick_kornfeld_2013]\] \[[Kocheemoolayil and Lele 2016][research_kocheemoolayil_lele_2016]\] \[[Kothari and Anderson 1987][research_kothari_anderson_1987]\] \[[Krahn 1955][research_krahn_1955]\] \[[Kula et al 2025][research_kula_aslangil_2025]\] \[[Kulfan 2002][research_kulfan_2002]\] \[[Kumawat et al 2025][research_kumawat_kumar_2025]\] \[[Runyan and Steers 1980][research_ljamesrunyan_louislsteers_1980]\] \[[Ladson and Hill 1987][research_ladsoncharlesl_hillsacquilla_1987]\] \[[Ladson et al 1987][research_ladsoncharlesl_hillacquillas_1987]\] \[[Laster et al 1998][research_laster_stanewsky_1998]\] \[[Lees 1956][research_lees_1956]\] \[[Lees and Reshotko 1962][research_lees_reshotko_1962]\] \[[Lepicovsky et al 1986][research_lepicovsky_ahuja_1986]\] \[[Li et al 2020][research_li_wang_2020]\] \[[Li et al 2021][research_li_choudhari_2021]\] \[[Li et al 2026][research_li_han_2026]\] \[[Liebeck 1989][research_liebeck_1989]\] \[[Liu and Mirels 1980][research_liu_mirels_1980]\] \[[Liu et al 2012][research_liu_wang_2012]\] \[[Liu et al 2016][research_liu_yang_2016_b]\] \[[Liu et al 2023][research_liu_li_2023]\] \[[Liu et al 2026][research_liu_peng_2026]\] \[[Lopez Lopez et al 2026][research_lopezlopez_haramurabastos_2026]\] \[[Lorber and Carta 1989][research_lorberpeterf_cartafranklino_1989]\] \[[Luckring 2003][research_luckring_2003]\] \[[Luckring and Hiller 2025][research_luckring_hiller_2025]\] \[[Lumley 1986][research_lumley_1986]\] \[[Luo et al 2024][research_luo_tang_2024]\] \[[Luther 1957][research_luther_1957]\] \[[Lynde and Campbell 2017][research_lynde_campbell_2017]\] \[[Lyons et al 1961][research_lyons_wc_1961]\] \[[Ma et al 2024][research_ma_li_2024]\] \[[Mace and Adamson 1985][research_mace_adamsonjr_1985]\] \[[Mach Number and Reynolds 2022][research_mach_number_2022]\] \[[Malik and Li 1993][research_malik_li_1993]\] \[[Marsden et al 2005][research_marsden_bogey_2005]\] \[[Martin 2008][research_martin_2008]\] \[[Matsui 1963][research_matsui_1963]\] \[[McElderry 1973][research_mcelderry_1973]\] \[[Mee 2001][research_mee_2001]\] \[[Meier et al 1987][research_meier_michel_1987]\] \[[Meijering and Schroeder 2001][research_meijering_schroeder_2001]\] \[[Melnik et al 1977][research_melnik_chow_1977]\] \[[Merienne et al 2019][research_merienne_brion_2019]\] \[[Bozeman et al][research_michaeldbozeman_richardlcampbell]\] \[[Miller 1985][research_miller_1985]\] \[[Mineck and Lawing 1987][research_mineckraymonde_lawingpiercel_1987]\] \[[Miotto et al 2021][research_miotto_wolf_2021]\] \[[Mirels 1986][research_mirels_1986]\] \[[Miyagoshi and Daisuke 2021][research_miyagoshi_daisuke_2021]\] \[[Miyakawa et al 1985][research_miyakawa_hirose_1985]\] \[[Mori et al 2024][research_mori_yakeno_2024]\] \[[Morizawa et al 2018][research_morizawa_nonomura_2018]\] \[[Murthy and Steinle 1986][research_murthy_steinle_1986]\] \[[Banner et al 1958][research_transition_flight_1958]\] \[[Nangia et al 2023][research_nangia_ghoreyshi_2023]\] \[[Narsipur 2022][research_narsipur_2022]\] \[[Berry et al 2016][research_blt_shuttle_2016]\] \[[Hiller et al 2024][research_slotted_nlf_2024]\] \[[Nayfeh 1992][research_nayfeh_1992]\] \[[Nie et al 2022][research_nie_song_2022]\] \[[Obara et al 1991][research_obara_lee_1991]\] \[[Olivier et al 2002][research_olivier_reichel_2002]\] \[[Olivier et al 2003][research_olivier_reichel_2003]\] \[[Olson et al 2026][research_olson_albrecht_2026]\] \[[Om et al 2001][research_om_curtin_2001]\] \[[Pate 1980][research_pate_1980]\] \[[Pekardan and Alexeenko 2016][research_pekardan_alexeenko_2016]\] \[[Pekardan and Alexeenko 2018][research_pekardan_alexeenko_2018]\] \[[Peltzer 2008][research_peltzer_2008]\] \[[Perez et al 2025][research_perez_hader_2025]\] \[[Persh 1956][research_persh_1956]\] \[[Plath][research_plath]\] \[[Plath et al 2024][research_plath_renac_2024]\] \[[Plentovich 1986][research_plentovicheb_1986]\] \[[Price and Earl A. 1981][research_price_earla_1981]\] \[[Quast et al 1990][research_quast_henke_1990]\] \[[Raghunathan 1983][research_raghunathan_1983]\] \[[Raghunathan and McAdam 1985][research_raghunathan_mcadam_1985]\] \[[Ray et al 1974][research_ray_kilgore_1974]\] \[[Reaser et al 1983][research_reaser_hallissy_1983]\] \[[Reed 1990][research_reed_1990]\] \[[Reibert et al 1997][research_reibert_saric_1997]\] \[[Report No. 637, Determination 1939][research_report_no_1939]\] \[[Reynolds Averaged Navier-Stokes Computations 1982][research_reynolds_averaged_1982]\] \[[Rivers et al 2001][research_rivers_wahls_2001]\] \[[Roberts 1963][research_roberts_1963_b]\] \[[Roberts et al 2012][research_roberts_reed_2012]\] \[[Robinson et al 1974][research_robinson_high_1974_b]\] \[[Roepke 1972][research_roepke_1972]\] \[[Saadeh et al 2026][research_saadeh_chau_2026]\] \[[Sankar and Tassa 1980][research_sankar_tassa_1980]\] \[[Saric 1997][research_saric_1997]\] \[[Saric 1998][research_saric_1998]\] \[[Saric 2010][research_saric_2010]\] \[[Sarlak 2017][research_sarlak_2017]\] \[[Sashida et al 2024][research_sashida_aoyama_2024]\] \[[Saunders 1996][research_saunders_1996]\] \[[Schloemer 1966][research_schloemer_1966]\] \[[Schrauf et al 1998][research_schrauf_perraud_1998]\] \[[Seraudie et al 1985][research_seraudiea_blancharda_1985]\] \[[Settles and Bogdonoff 1981][research_settlesgs_bogdonoffsm_1981]\] \[[Sewall et al 1985][research_sewallwilliamg_mcgheerobertj_1985]\] \[[Sidorenko et al 2018][research_sidorenko_kirilovskiy_2018]\] \[[Smith and Cebeci 1967][research_smith_cebeci_1967]\] \[[Smith 1958][research_smithccjr_1958]\] \[[Smith 1958][research_smithcharlescjr_1958]\] \[[Smith 1961][research_smithcharlescjr_1961]\] \[[Somers 2005][research_somers_2005]\] \[[Spaid and Lynch 1996][research_spaid_lynch_1996]\] \[[Stanewsky et al 1984][research_stanewskye_demurief_1984]\] \[[Starr and Schueler 1973][research_starr_schueler_1973]\] \[[Sternberg 1954][research_sternberg_1954]\] \[[Stetson 1981][research_stetson_1981]\] \[[Stock 2002][research_stock_2002]\] \[[Stremel 1993][research_stremel_1993]\] \[[Suwa et al 2012][research_suwa_nose_2012]\] \[[Tam and Ju 2011][research_tam_ju_2011]\] \[[Tanner 1963][research_tanner_1963]\] \[[Three-dimensional boundary-layer transition on 1994][research_three_dimensional_boundary_layer_1994]\] \[[Tokugawa and Yoshida 2006][research_tokugawa_yoshida_2006]\] \[[Tomek et al 2002][research_tomek_hall_2002]\] \[[Toot 1989][research_toot_1989]\] \[[Transonic flight test of 1994][research_transonic_flight_1994]\] \[[Tripathi et al 2023][research_tripathi_mistri_2023]\] \[[Turbeville and Schneider 2021][research_turbeville_schneider_2021]\] \[[Tô et al 2019][research_to_simiriotis_2019]\] \[[Utkina et al 2023][research_utkina_kozelkov_2023]\] \[[Vaglio-Laurin 1978][research_vagliolaurin_1978]\] \[[Valarezo et al 1993][research_valarezo_dominik_1993]\] \[[Valarezo et al 1992][research_valarezowaltero_dominikchetj_1992]\] \[[van der Vooren 2008][research_vandervooren_2008]\] \[[Vigneswaran 2026][research_vigneswaran_2026]\] \[[Vijgen et al 1988][research_vijgen_dodbele_1988]\] \[[Vijgen et al 1990][research_vijgen_vandam_1990]\] \[[Vinodh et al 2023][research_vinodh_sridhar_2023]\] \[[Vittal-Shenoy et al 2023][research_vittalshenoy_gojon_2023]\] \[[Wahls et al 2001][research_wahls_owens_2001]\] \[[Valarezo et al 1993][research_walterovalarezo_chetjdominik_1993]\] \[[Wang 1998][research_wang_1998]\] \[[Wang and Zha 2020][research_wang_zha_2020]\] \[[Wang et al 1994][research_wang_herbert_1994]\] \[[Wang et al 2025][research_wang_wang_2025]\] \[[Ward and Miley 1983][research_ward_miley_1983]\] \[[Weyburne 2009][research_weyburne_2009]\] \[[White 1969][research_white_1969]\] \[[Wilby 1967][research_wilby_1967]\] \[[Wilson and Chou 1985][research_wilson_chou_1985]\] \[[Wilson et al 1975][research_wilson_chandra_1975]\] \[[Wright and Zoby 1977][research_wright_zoby_1977]\] \[[Xu et al 2020][research_xu_liu_2020]\] \[[Yoo][research_yoo]\] \[[Yoshioka et al][research_yoshioka_kohama]\] \[[Yoshioka et al 2009][research_yoshioka_kikuchi_2009]\] \[[Yuan et al 2019][research_yuan_wan_2019]\] \[[Zanin 1985][research_zanin_1985]\] \[[Zauner et al 2019][research_zauner_detullio_2019]\] \[[Zhang et al 2020][research_zhang_li_2020]\] \[[Zhao et al 2017][research_zhao_gao_2017]\] \[[Zhao et al 2024][research_zhao_liu_2024]\] \[[Zhao et al 2025][research_zhao_li_2025]\] \[[Zoppini et al 2022][research_zoppini_ragni_2022]\]

### Buffet onset and the separated wake

**The unsteady consequence of shock-induced separation.** Buffet onset boundaries, buffet loads and their alleviation. **This is the youngest cluster in the survey**, with 215 of its 273 records dated 2000 or later, and 184 of the titles name transonic or shock buffet specifically, which bears out the article's reading that buffet onset is still being characterized rather than settled.

**273 records.** \[[A Comparison of Different 2022][research_a_comparison_2022]\] \[[A New Steady Approach 2006][research_a_new_2006]\] \[[Arif et al 2023][research_arif_singh_2023]\] \[[Asada and Kawai 2024][research_asada_kawai_2024]\] \[[Asai 2022][research_asai_2022]\] \[[Baker and Johnson 1955][research_bakerthomasf_johnsonwallacee_1955]\] \[[Balleur et al 2002][research_balleur_girodrouxlavigne_2002]\] \[[Barakos and Drikakis 1999][research_barakos_drikakis_1999]\] \[[Barbut et al 2010][research_barbut_braza_2010]\] \[[Barnard 1969][research_barnard_1969]\] \[[Bean and Lee 1995][research_bean_lee_1995]\] \[[Bean and Wood 1996][research_bean_wood_1996]\] \[[Ben-Gida 2025][research_bengida_2025]\] \[[Benepe et al 1975][research_benepe_cunninghamjr_1975]\] \[[Benepe et al 1978][research_benepedb_cunninghamamjr_1978]\] \[[Benoit and Legrain 1987][research_benoit_legrain_1987]\] \[[Bonnifet et al 2017][research_bonnifet_gerolymos_2017]\] \[[Breitsamter and Laschka 1994][research_breitsamter_laschka_1994]\] \[[Browne et al 2024][research_browne_maldonado_2024]\] \[[Browne et al 2025][research_browne_maldonado_2025]\] \[[Brunet and Deck 2008][research_brunet_deck_2008]\] \[[Butler and Jones 1984][research_butler_jones_1984]\] \[[Canbazoglu et al 1996][research_canbazoglu_lin_1996]\] \[[Candon et al 2019][research_candon_levinski_2019]\] \[[Cao et al 2024][research_cao_fu_2024]\] \[[Carrese et al 2016][research_carrese_marzocca_2016]\] \[[Chen et al 2009][research_chen_ulker_2009]\] \[[Chen et al 2022][research_chen_gao_2022]\] \[[Chen et al 2023][research_chen_gao_2023]\] \[[Chesneau and Wood 1995][research_chesneau_wood_1995]\] \[[Chiarelli and Bonomo 2019][research_chiarelli_bonomo_2019]\] \[[Christison Gray and Martins 2026][research_christisongray_martins_2026]\] \[[Chung 2017][research_chung_2017]\] \[[Chung et al 2002][research_chung_lee_2002]\] \[[Chung et al 2003][research_chung_lee_2003]\] \[[Chwalowski et al 2022][research_chwalowski_massey_2022]\] \[[Cohen 1970][research_cohen_1970]\] \[[Cornette 1961][research_cornetteeldens_1961]\] \[[Crouch et al 2008][research_crouch_garbaruk_2008]\] \[[Crouch et al 2009][research_crouch_garbaruk_2009]\] \[[Crouch et al 2018][research_crouch_garbaruk_2018]\] \[[Crouch et al 2019][research_crouch_garbaruk_2019]\] \[[Crouch et al 2024][research_crouch_ahrabi_2024]\] \[[D'Aguanno et al 2021][research_daguanno_schrijer_2021]\] \[[D'Aguanno et al 2021][research_daguanno_schrijer_2021_b]\] \[[D'Aguanno et al 2021][research_daguanno_schrijer_2021_c]\] \[[D'Aguanno et al 2022][research_daguanno_campspons_2022]\] \[[Damstrom and Mayes 1970][research_damstrom_mayes_1970]\] \[[Damstrom and Mayes 1971][research_damstrom_mayes_1971]\] \[[Dandois 2016][research_dandois_2016]\] \[[Dandois et al 2018][research_dandois_mary_2018]\] \[[Dang and Yang 2010][research_dang_yang_2010]\] \[[Dang et al 2019][research_dang_zhao_2019]\] \[[Das et al 2020][research_das_carrese_2020]\] \[[Das et al 2022][research_das_marzocca_2022]\] \[[Davis and Wornom 1958][research_davisddjr_wornomde_1958]\] \[[Deck 2004][research_deck_2004]\] \[[Deck 2005][research_deck_2005]\] \[[Degregori and Kim 2021][research_degregori_kim_2021]\] \[[Deng et al 2023][research_deng_zhang_2023]\] \[[Di Pasquale 2024][research_dipasquale_2024]\] \[[Di Pasquale and Prince 2023][research_dipasquale_prince_2023]\] \[[Dias et al 2023][research_dias_budisic_2023]\] \[[Dive Testing for Flutter 2003][research_dive_testing_2003]\] \[[Eldridge-Allegra et al 2023][research_eldridgeallegra_xu_2023]\] \[[Eldridge-Allegra et al 2024][research_eldridgeallegra_roseman_2024]\] \[[Erickson 1974][research_ericksonll_1974]\] \[[Farhangnia et al 1996][research_farhangnia_guruswamy_1996]\] \[[Ferman and Turner 1999][research_ferman_turner_1999]\] \[[Ferman and Turner 1999][research_ferman_turner_1999_b]\] \[[Firsov et al 2017][research_firsov_isaenkov_2017]\] \[[Firsov et al 2018][research_firsov_moralev_2018]\] \[[Fu et al 2023][research_fu_sun_2023]\] \[[Fu et al 2026][research_fu_feng_2026]\] \[[Fujino and Suzuki 2024][research_fujino_suzuki_2024]\] \[[Fukumoto et al 2023][research_fukumoto_kouchi_2023]\] \[[Fukushima and Kawai 2017][research_fukushima_kawai_2017]\] \[[Fukushima and Kawai 2017][research_fukushima_kawai_2017_b]\] \[[Fukushima and Kawai 2018][research_fukushima_kawai_2018]\] \[[Fukushima and Kawai 2019][research_fukushima_kawai_2019]\] \[[Fukushima et al 2020][research_fukushima_tamaki_2020]\] \[[Gao et al 2018][research_gao_zhang_2018]\] \[[Gao et al 2019][research_gao_zhang_2019]\] \[[Garnier and Deck 2010][research_garnier_deck_2010]\] \[[Geissler 2003][research_geissler_2003]\] \[[Geoghegan et al 2018][research_geoghegan_giannelis_2018]\] \[[Geoghegan et al 2020][research_geoghegan_giannelis_2020]\] \[[Gillan 1995][research_gillan_1995]\] \[[Goc et al 2023][research_goc_agrawal_2023]\] \[[Goc et al 2025][research_goc_agrawal_2025]\] \[[Goncalves et al 2003][research_goncalves_robinet_2003]\] \[[Gong et al 2024][research_gong_gao_2024]\] \[[Goushcha and Sekula 2025][research_goushcha_sekula_2025]\] \[[Grossi et al 2012][research_grossi_braza_2012]\] \[[Grossi et al 2014][research_grossi_braza_2014]\] \[[Han et al 2022][research_han_xu_2022]\] \[[Hartmann et al 2013][research_hartmann_feldhusen_2013]\] \[[Hasan and Alam 2013][research_hasan_alam_2013]\] \[[Hass et al 2024][research_hass_housman_2024]\] \[[Herr et al 2023][research_herr_spinner_2023]\] \[[Hirose and Miwa 1989][research_hirose_miwa_1989]\] \[[Hollingsworth and Cohen 1971][research_hollingsworth_cohen_1971]\] \[[Houtman et al 2023][research_houtman_vevek_2023]\] \[[Hu et al 2024][research_hu_zhu_2024]\] \[[Hwang and Pi 1975][research_hwang_pi_1975]\] \[[Hwang and Pi 1975][research_hwang_pi_1975_b]\] \[[Ishida et al 2016][research_ishida_ishiko_2016]\] \[[Ishida et al 2017][research_ishida_hashimoto_2017]\] \[[Iwatani et al 2022][research_iwatani_asada_2022]\] \[[Izumi et al 2015][research_izumi_ogino_2015]\] \[[Ramey et al][research_jmichealramey_martinksekula]\] \[[Jia et al 2024][research_jia_li_2024]\] \[[Jiang et al 2019][research_jiang_tian_2019]\] \[[Jinli and Zhichun 2013][research_jinli_zhichun_2013]\] \[[Kanchi et al 2026][research_kanchi_he_2026]\] \[[Kang et al 2024][research_kang_chen_2024]\] \[[Kikuchi et al 2024][research_kikuchi_kouchi_2024]\] \[[Koike et al 2016][research_koike_ueno_2016]\] \[[Kojima and Hashimoto 2023][research_kojima_hashimoto_2023]\] \[[Kojima et al 2019][research_kojima_kameda_2019]\] \[[Korthäuer et al 2023][research_korthauer_accorinti_2023]\] \[[Kouchi et al 2017][research_kouchi_yamaguchi_2017]\] \[[Kumada and Sawada 2016][research_kumada_sawada_2016]\] \[[Kuya et al 2020][research_kuya_boda_2020]\] \[[Kuz'min 2007][research_kuzmin_2007]\] \[[Kuz'min 2009][research_kuzmin_2009]\] \[[Kuz'min and Shilkin 2009][research_kuzmin_shilkin_2009]\] \[[Lagemann 2024][research_lagemann_2024]\] \[[Lagemann et al 2022][research_lagemann_mateling_2022]\] \[[Lagemann et al 2024][research_lagemann_brunton_2024]\] \[[Le Balleur and Girodroux-Lavigne 1989][research_leballeur_girodrouxlavigne_1989]\] \[[Lee 1990][research_lee_1990_b]\] \[[Lee and Ohman 1984][research_lee_ohman_1984]\] \[[Lee and Tang 1989][research_lee_tang_1989]\] \[[Lei et al 2025][research_lei_zhang_2025]\] \[[Lemley and Mullans 1973][research_lemley_mullans_1973]\] \[[Lemley and Mullans 1974][research_lemley_mullans_1974]\] \[[Liu et al 2016][research_liu_wang_2016]\] \[[Liu et al 2022][research_liu_han_2022]\] \[[Liu et al 2024][research_liu_chen_2024]\] \[[Luber 2018][research_luber_2018]\] \[[Ma et al 2024][research_ma_gao_2024]\] \[[Mabey 1989][research_mabey_1989]\] \[[Mabey and Lee 1986][research_mabey_lee_1986]\] \[[Mabey et al 1992][research_mabeydg_boydenrp_1992]\] \[[Mabey et al 1995][research_mabeydg_boydenrp_1995]\] \[[Maeyama et al 2026][research_maeyama_asada_2026]\] \[[Maldonado et al 2024][research_maldonado_housman_2024]\] \[[Masini et al 2019][research_masini_timme_2019]\] \[[Masini et al 2020][research_masini_timme_2020]\] \[[Mayer et al 2019][research_mayer_lutz_2019]\] \[[Mayes et al 1970][research_mayes_lores_1970]\] \[[Mayya et al 2022][research_mayya_karnick_2022]\] \[[Meng et al 2024][research_meng_zhu_2024]\] \[[Candon et al][research_michaelcandon_vincenzomuscarello]\] \[[Molton et al 2013][research_molton_dandois_2013]\] \[[Moses et al 2001][research_mosesrobertw_wiesemancarold_2001]\] \[[Moss et al 1991][research_mossstevenw_colestanleyr_1991]\] \[[Murray et al 2020][research_murray_giannellis_2020]\] \[[Mason 1953][research_buffet_rocket_models_1953]\] \[[Nahom Jidovetski et al 2025][research_nahomjidovetski_raveh_2025]\] \[[Friend and Sefic 1972][research_f104_buffet_1972]\] \[[Benepe et al 1974][research_buffet_response_1974]\] \[[Deangelis and Monaghan 1977][research_f8_buffet_1977]\] \[[Benepe et al 1978][research_buffet_response_1978]\] \[[Moses and Huttsell 2000][research_f22_fin_buffet_2000]\] \[[Nash et al 2025][research_nash_timme_2025]\] \[[Nie et al 2024][research_nie_zheng_2024]\] \[[Nixon 2001][research_nixon_2001]\] \[[Nixon 2020][research_nixon_2020]\] \[[Ohmichi et al 2017][research_ohmichi_ishida_2017]\] \[[Ohmichi et al 2018][research_ohmichi_ishida_2018]\] \[[Goushcha and Sekula][research_oleggoushcha_martinksekula]\] \[[Ozgoren et al 2001][research_ozgoren_sahin_2001]\] \[[Pazner et al 2019][research_pazner_franco_2019]\] \[[Petrocchi and Barakos 2023][research_petrocchi_barakos_2023]\] \[[Petrocchi and Barakos 2023][research_petrocchi_barakos_2023_b]\] \[[Petrocchi and Barakos 2024][research_petrocchi_barakos_2024]\] \[[Petrocchi et al 2022][research_petrocchi_steijl_2022]\] \[[Phillips et al 2003][research_phillips_lambert_2003]\] \[[Physics-assisted reduced-order modeling for 2023][research_physics_assisted_reduced_order_2023]\] \[[Plante][research_plante]\] \[[Plante and Laurendeau 2019][research_plante_laurendeau_2019]\] \[[Plante et al 2017][research_plante_dandois_2017]\] \[[Polivanov and Sidorenko 2026][research_polivanov_sidorenko_2026]\] \[[Poplingher and Raveh 2018][research_poplingher_raveh_2018]\] \[[Poplingher and Raveh 2022][research_poplingher_raveh_2022]\] \[[Poplingher et al 2019][research_poplingher_raveh_2019]\] \[[Poplingher et al 2022][research_poplingher_mallik_2022]\] \[[Qi et al 2026][research_qi_gao_2026]\] \[[Ren et al 2020][research_ren_chen_2020]\] \[[Ren et al 2022][research_ren_gao_2022]\] \[[Ren et al 2026][research_ren_ma_2026]\] \[[Riddle 1975][research_riddledw_1975]\] \[[Rokoni and Hasan 2013][research_rokoni_hasan_2013]\] \[[Roos 1979][research_roos_1979]\] \[[Roos 1980][research_roos_1980]\] \[[Roos 1985][research_roosfw_1985]\] \[[Sansica and Hashimoto 2023][research_sansica_hashimoto_2023]\] \[[Sansica and Hashimoto 2023][research_sansica_hashimoto_2023_b]\] \[[Schauerte and Schreyer 2022][research_schauerte_schreyer_2022]\] \[[Schauerte and Schreyer 2023][research_schauerte_schreyer_2023]\] \[[Schauerte and Schreyer 2023][research_schauerte_schreyer_2023_b]\] \[[Schauerte and Schreyer 2025][research_schauerte_schreyer_2025]\] \[[Schauerte and Schreyer 2025][research_schauerte_schreyer_2025_c]\] \[[Schauerte et al 2026][research_schauerte_kwong_2026]\] \[[Shen and Zuo 2026][research_shen_zuo_2026]\] \[[Shiqi et al 2018][research_shiqi_tian_2018]\] \[[Singh and Venkatraman 2023][research_singh_venkatraman_2023]\] \[[Singh and Venkatraman 2026][research_singh_venkatraman_2026]\] \[[Singh et al 2022][research_singh_karnick_2022]\] \[[Song et al 2024][research_song_wong_2024]\] \[[Song et al 2025][research_song_wong_2025]\] \[[Soudakov et al 2017][research_soudakov_petrov_2017]\] \[[Soudakov et al 2017][research_soudakov_sidorenko_2017]\] \[[Stanewsky and Basler 1989][research_stanewsky_basler_1989]\] \[[Steimle et al 2008][research_steimle_schroder_2008]\] \[[Study on flow noise 2023][research_study_on_2023]\] \[[Su and Chow 1993][research_su_chow_1993]\] \[[Su and Chow 1995][research_su_chow_1995]\] \[[Sugioka et al 2015][research_sugioka_numata_2015]\] \[[Sugioka et al 2018][research_sugioka_koike_2018]\] \[[Szubert et al 2015][research_szubert_grossi_2015]\] \[[Takuma et al 2026][research_takuma_hagita_2026]\] \[[Tamaki and Kawai 2023][research_tamaki_kawai_2023]\] \[[Tao et al 2023][research_tao_zheng_2023]\] \[[The Phenomenon of Buffeting 1931][research_the_phenomenon_1931]\] \[[Thomas and Dowell 2011][research_thomas_dowell_2011]\] \[[Thomas and Dowell 2015][research_thomas_dowell_2015]\] \[[Thomas and Dowell 2020][research_thomas_dowell_2020]\] \[[Tian et al 2017][research_tian_feng_2017]\] \[[Tian et al 2017][research_tian_gao_2017]\] \[[Timme and Thormann 2016][research_timme_thormann_2016]\] \[[Triplett 1982][research_triplett_1982]\] \[[Triplett 1983][research_triplett_1983]\] \[[Völkl et al 2026][research_volkl_weiner_2026]\] \[[Waldmann et al 2023][research_waldmann_ehrle_2023]\] \[[Wang et al 2024][research_wang_liu_2024]\] \[[Wei et al 2023][research_wei_zheng_2023]\] \[[Wei et al 2024][research_wei_zheng_2024]\] \[[Wei et al 2026][research_wei_liu_2026]\] \[[Weiner and Semaan 2022][research_weiner_semaan_2022]\] \[[Weiner and Semaan 2023][research_weiner_semaan_2023]\] \[[Xiao et al 2004][research_xiao_tsai_2004]\] \[[Xiao et al 2006][research_xiao_tsai_2006]\] \[[Xiong and Liu 2013][research_xiong_liu_2013]\] \[[Xiong and Nguyen 2024][research_xiong_nguyen_2024]\] \[[Xu and Dowell 2026][research_xu_dowell_2026]\] \[[Xu et al 2019][research_xu_saleh_2019]\] \[[Yamasaki and Lele 2024][research_yamasaki_lele_2024]\] \[[Yan et al 2026][research_yan_dai_2026]\] \[[Yang et al 2024][research_yang_li_2024]\] \[[Yang et al 2024][research_yang_li_2024_b]\] \[[Young et al 1992][research_youngjr_hergert_1992]\] \[[Yu et al 2026][research_yu_bose_2026]\] \[[Yu Xing et al 2015][research_yuxing_gangwang_2015]\] \[[Zahn and Breitsamter 2022][research_zahn_breitsamter_2022]\] \[[Zahn et al 2025][research_zahn_zieher_2025]\] \[[Zauner and Sandham 2020][research_zauner_sandham_2020]\] \[[Zauner et al 2023][research_zauner_moise_2023]\] \[[Zhang et al 2026][research_zhang_deng_2026]\] \[[Zhang and Qu 2015][research_zhang_qu_2015]\] \[[Zhang et al 2021][research_zhang_yang_2021]\] \[[Zhang et al 2025][research_zhang_zuo_2025]\] \[[Zhang et al 2026][research_zhang_dou_2026]\] \[[Zhang et al 2026][research_zhang_kou_2026]\] \[[Zhang et al 2026][research_zhang_kou_2026_b]\] \[[Zhao et al 2020][research_zhao_dai_2020]\] \[[Zhou et al 2018][research_zhou_feng_2018]\] \[[Zhu et al 2020][research_zhu_wang_2020]\] \[[Zhu et al 2025][research_zhu_yang_2025]\] \[[Zhu et al 2026][research_zhu_yang_2026]\] \[[Zimmermann et al 2018][research_zimmermann_mayer_2018]\]

### Flight test technique, instrumentation and flight measurement

**The method the X-1 established.** Flight test technique, instrumentation, in-flight thrust and drag determination, parameter identification and envelope expansion.

**142 records.** \[[Adams et al 1983][research_adams_thompson_1983]\] \[[Adams et al 1983][research_adams_thompson_1983_b]\] \[[Advanced Ducted Propulsor In-Flight][research_advanced_ducted]\] \[[Air Force Flight Test Center Edwards Afb Ca 2002][research_airforceflighttestcenteredwardsafbca_2002]\] \[[Air Force Test Pilot School Edwards Afb Ca 1962][research_airforcetestpilotschooledwardsafbca_1962]\] \[[Air Force Test Pilot School Edwards Afb Ca 1962][research_airforcetestpilotschooledwardsafbca_1962_b]\] \[[Air Force Test Pilot School Edwards Afb Ca 1962][research_airforcetestpilotschooledwardsafbca_1962_c]\] \[[Air Force Test Pilot School Edwards Afb Ca 1979][research_airforcetestpilotschooledwardsafbca_1979]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990]\] \[[Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991]\] \[[Air Force Test Pilot School Edwards Afb Ca 1992][research_airforcetestpilotschooledwardsafbca_1992_b]\] \[[Aircraft and Flight Test 2021][research_aircraft_and_2021]\] \[[Altman 1965][research_altman_1965]\] \[[Anderson and Vincent 1985][research_anderson_vincent_1985]\] \[[Anderson et al 1983][research_anderson_vincent_1983]\] \[[Armstrong 1977][research_armstrong_1977]\] \[[Blanchard et al 1993][research_blanchard_larman_1993]\] \[[Bleimeyer 1981][research_bleimeyer_1981]\] \[[Braman et al 1983][research_braman_schweikhard_1983]\] \[[Bronz et al 2017][research_bronz_garciademarina_2017]\] \[[Brown and Bastian 2008][research_brown_bastian_2008]\] \[[Brown and Bradley 1981][research_brown_bradley_1981]\] \[[Bursey and Dickinson 1990][research_bursey_dickinson_1990]\] \[[Burtch 2015][research_burtch_2015]\] \[[Byrdsong 1977][research_byrdsongta_1977]\] \[[Caiger and Gould 1971][research_caiger_gould_1971]\] \[[Canter and Groves 1994][research_canter_groves_1994]\] \[[Carpenter et al 2025][research_carpenter_hantsche_2025]\] \[[Chandler and Chisholm 1993][research_chandler_chisholm_1993]\] \[[Cheney 1988][research_cheney_1988]\] \[[Cook et al 2004][research_cook_ghee_2004]\] \[[Cumming et al 2016][research_cummingstephenb_smithmarks_2016]\] \[[Davison 1963][research_davison_1963]\] \[[Deckert 1981][research_deckert_1981]\] \[[Deepa and Gupta 2023][research_deepa_gupta_2023]\] \[[Di Fiore dos Santos et al 2000][research_difioredossantos_lewis_2000]\] \[[Duran 2026][research_duran_2026]\] \[[Enciu 2019][research_enciu_2019]\] \[[Energy Approach To Performance 2003][research_energy_approach_2003]\] \[[Ertugrul and Koyuncu 2023][research_ertugrul_koyuncu_2023]\] \[[Ferrara et al 2006][research_ferrara_consalvo_2006]\] \[[Fischenberg 1995][research_fischenberg_1995]\] \[[Fisher et al 1956][research_fisher_gertsen_1956]\] \[[Fosdick 1970][research_fosdick_1970]\] \[[Gallagher 1968][research_gallagher_1968]\] \[[Gea et al 1991][research_gea_chyu_1991]\] \[[Gee et al 1976][research_gee_jenks_1976]\] \[[General Electric Co Cincinnati Oh 1964][research_generalelectriccocincinnatioh_1964]\] \[[Gera 1986][research_gera_1986]\] \[[Gera et al 1981][research_gera_wilson_1981]\] \[[Gilyard and Orme 1992][research_gilyard_orme_1992]\] \[[Godwin et al 1964][research_godwin_frazier_1964]\] \[[Goupil][research_goupil]\] \[[Grauer and Morelli 2023][research_grauer_morelli_2023]\] \[[Gray 2016][research_gray_2016]\] \[[Gregory et al 2011][research_gregory_xargay_2011]\] \[[Haglund and Kane 1974][research_haglund_kane_1974]\] \[[Haglund and Kane 1973][research_haglundgt_kaneej_1973]\] \[[Harper et al 2025][research_harper_mishra_2025]\] \[[Hartmann et al 1979][research_hartmann_stein_1979]\] \[[Haxter and Spehr 2018][research_haxter_spehr_2018]\] \[[Heineck et al 2016][research_heineck_banks_2016]\] \[[Hicks and Petersen 1988][research_hicksjohnw_petersenkevinl_1988]\] \[[Hicks and Petersen 1989][research_hicksjohnw_petersenkevinl_1989]\] \[[Hicks et al 1987][research_hicksjohnw_kaniajan_1987]\] \[[Hoff 2007][research_hoff_2007]\] \[[Huang et al 2001][research_huang_folk_2001]\] \[[In-Flight Thrust Determination][research_in_flight_thrust_b]\] \[[In-Flight Thrust Determination for][research_in_flight_thrust]\] \[[Ishikawa et al 2007][research_ishikawa_kwak_2007]\] \[[Ishikawa et al 2008][research_ishikawa_kwak_2008]\] \[[Jaffe 1975][research_jaffep_1975]\] \[[Reynolds et al][research_jamesreynolds_ethanbaumann]\] \[[Grauer and Boucher][research_jaredagrauer_matthewjboucher]\] \[[Jet Thrust Measurement In 2003][research_jet_thrust_2003]\] \[[Hicks et al 1987][research_johnwhicks_jankania_1987]\] \[[Jones et al 2013][research_jonesdaniels_buitrongt_2013]\] \[[Kandath et al 2023][research_kandath_pushpangathan_2023]\] \[[Keener 1959][research_keenerer_1959]\] \[[Keener and Pierce 1950][research_keenerer_piercem_1950]\] \[[Kimberlin 1987][research_kimberlin_1987]\] \[[Kwak et al 2006][research_kwak_yoshida_2006]\] \[[Lamy 1983][research_lamy_1983]\] \[[Level Flight Performance Flight 2003][research_level_flight_2003]\] \[[Lux 1978][research_luxdp_1978]\] \[[Lykins and Keshmiri 2010][research_lykins_keshmiri_2010]\] \[[Makowski 1964][research_makowski_1964]\] \[[Malaek et al 2006][research_malaek_izadi_2006]\] \[[Mallozzi et al 2014][research_mallozzi_depaolis_2014]\] \[[Marshall and Schweikhard 1973][research_marshallrt_schweikhardwg_1973]\] \[[Mason 2013][research_mason_2013]\] \[[Matheny and Panageas 1981][research_matheny_panageas_1981]\] \[[McNally and Bach 1988][research_mcnally_bachjr_1988]\] \[[McNeill et al 1961][research_mcneillwatere_mcleanjohnd_1961]\] \[[Merceruio][research_merceruio]\] \[[Morelli 2000][research_morelli_2000]\] \[[Murakami et al 2007][research_murakami_tada_2007]\] \[[Mungall 1948][research_geared_tab_1948]\] \[[Drake 1957][research_high_altitude_1957]\] \[[Saltzman and Ayers 1995][research_supersonic_research_1995]\] \[[Gelzer and Peebles 2015][research_hsfrs_rcs_2015]\] \[[Negrão et al 1998][research_negrao_fanton_1998]\] \[[Nicolosi et al 2011][research_nicolosi_demarco_2011]\] \[[Ogren et al 1974][research_ogren_sotanski_1974]\] \[[Orme and Gilyard 1993][research_orme_gilyard_1993]\] \[[Panton et al 1980][research_panton_oberkampf_1980]\] \[[Patel et al 2023][research_patel_deodhare_2023]\] \[[Payne and Samuels 1990][research_payne_samuels_1990]\] \[[Performance Evaluation by Flight 1995][research_performance_evaluation_1995]\] \[[Propeller/Propfan In-Flight Thrust Determination][research_propeller_propfan_in_flight]\] \[[Ratnayake 2010][research_ratnayake_2010]\] \[[Ray 1994][research_ray_1994]\] \[[Ray et al 2002][research_rayronaldj_cobleighbrentr_2002]\] \[[Rice 1946][research_rice_1946]\] \[[Richwine and Del Frate 1995][research_richwinedavidm_delfratejohnh_1995]\] \[[Riddle et al 1981][research_riddle_innis_1981]\] \[[Roberts et al 1966][research_roberts_smith_1966]\] \[[Rosenberg and Schuch 1983][research_rosenberg_schuch_1983]\] \[[Sabzehparvar 2005][research_sabzehparvar_2005]\] \[[Sakata 2002][research_sakata_2002]\] \[[Sang and Schetz 2002][research_sang_schetz_2002]\] \[[Sarigul-Klijn et al 2006][research_sarigulklijn_sarigulklijn_2006]\] \[[Sarohia et al 1980][research_sarohia_parthasarathy_1980]\] \[[Scafetta 1983][research_scafetta_1983]\] \[[Schumacher 1952][research_schumacher_1952]\] \[[Sefic and Maxwell 1987][research_seficwalterj_maxwellcleom_1987]\] \[[Simpson 1972][research_simpson_1972]\] \[[Simpson 1979][research_simpson_1979]\] \[[Stoliker and Carter 2003][research_stolikerpatrickc_carterjohn_2003]\] \[[Strutz 1972][research_strutzlw_1972]\] \[[Sugioka et al 2026][research_sugioka_nakajima_2026]\] \[[Taranto and Abdulrahim 2023][research_taranto_abdulrahim_2023]\] \[[Taylor and Ratnayake 2011][research_taylor_ratnayake_2011]\] \[[Thompson 1966][research_thompson_1966]\] \[[Time-Dependent In-Flight Thrust Determination][research_time_dependent_in_flight]\] \[[Uncertainty of In-Flight Thrust][research_uncertainty_of]\] \[[Veletas 2026][research_veletas_2026]\] \[[Wang et al 2026][research_wang_song_2026_b]\] \[[Weiss et al 2022][research_weiss_staudacher_2022]\] \[[Whitbeck et al 1982][research_whitbeck_smith_1982]\] \[[Williams 1956][research_williams_1956]\] \[[Yip et al 1995][research_yip_vijgen_1995]\]

### The X-1, its sibling research airplanes and the later research fleet

**The aircraft's own record and the record of the fleet it began.** Flight, tunnel and free-fall reports on the X-1 and its variants, the Douglas D-558 series flown alongside it, the X-2, X-5 and X-15, and the later research airplanes that inherited the method. **This is the oldest cluster in the survey**, with 82 of its 123 records dated before 1960, and it is almost entirely report literature of the National Advisory Committee for Aeronautics and its successor. **The Navy's D-558 appears in more of these titles than the X-1 does**, 50 against nineteen, and those D-558 titles report loads, pressures, buffeting and handling qualities flight by flight across the long instrumented programme of the D-558-II.

**123 records.** \[[Aerodynamic and Landing Measurements 1960][research_aerodynamic_and_1960]\] \[[Angle and Lundstrom 1948][research_angleellwyne_lundstromreginaldr_1948]\] \[[Ankenbruck 1954][research_ankenbruckhermano_1954]\] \[[Ankenbruck and Dahlen 1953][research_ankenbruckhermano_dahlentheodoree_1953]\] \[[Ankenbruck and Wolowicz 1954][research_ankenbruckhermano_wolowiczchesterh_1954]\] \[[Baer-Riedhart 1981][research_baerriedhart_1981]\] \[[Baker 1953][research_bakerthomasf_1953]\] \[[Baker 1953][research_bakerthomasf_1953_b]\] \[[Baker 1954][research_bakerthomasf_1954]\] \[[Bartlett 1975][research_bartlettdw_1975]\] \[[Bartlett and Harris 1974][research_bartlettdw_harriscd_1974]\] \[[Bartlett and Sangiorgio 1975][research_bartlettdw_sangiorgiog_1975]\] \[[Bartlett et al 1973][research_bartlettdw_harriscd_1973]\] \[[Bielat and Campbell 1953][research_bielatralphp_campbellgeorges_1953]\] \[[Bland and Young 1961][research_blandsr_youngls_1961]\] \[[Boyden 1974][research_boydenrp_1974]\] \[[Brunn and Stillwell 1956][research_brunncyrild_stillwellwendellh_1956]\] \[[Burcham et al 1995][research_burchamfrankwjr_gatlindonaldh_1995]\] \[[Burcham and Ray 1987][research_burchamjr_ray_1987]\] \[[Childs 1953][research_childsjoanm_1953]\] \[[Curry and Sim 1982][research_curry_sim_1982]\] \[[Curry and Sim 1984][research_curryre_simag_1984]\] \[[Dahlen 1953][research_dahlentheodoree_1953]\] \[[Dicarlo et al 1992][research_dicarlo_brown_1992]\] \[[Drake and McKay 1953][research_drakehubertm_mckayjohnb_1953]\] \[[Dunning 1959][research_dunningrw_1959]\] \[[Ferris 1973][research_ferrisjc_1973]\] \[[Fischel 1954][research_fischeljack_1954]\] \[[Fischel and Brunn 1954][research_fischeljack_brunncyrild_1954]\] \[[Fischel and Reisert 1956][research_fischeljack_reisertdonald_1956]\] \[[Fischel et al 1957][research_fischeljack_darvillerobertw_1957]\] \[[Fisher 1969][research_fisherdf_1969]\] \[[Gates and Sternfield 1950][research_gatesordwaybjr_sternfieldleonard_1950]\] \[[Grant and Robinson 1953][research_grantfrederickc_robinsonrossb_1953]\] \[[Greene 1958][research_greenelp_1958]\] \[[Grigsby 1954][research_grigsbycarle_1954]\] \[[Hewes and Hassell 1960][research_hewesdonalde_hasselljamesljr_1960]\] \[[Drake 1949][research_hubertmdrake_1949]\] \[[Hussein and Chudoba 2016][research_hussein_chudoba_2016]\] \[[in't Veld Alexander and Karwal Arun 2012][research_intveldalexanderc_karwalarunk_2012]\] \[[Jackson et al 1978][research_jacksonlr_kirkhamfs_1978]\] \[[Johnson 1958][research_johnsonclintont_1958]\] \[[Jordan 1972][research_jordanfljr_1972]\] \[[Jordan and Keener 1955][research_jordangarethh_keenerearlr_1955]\] \[[Keener et al 1951][research_keenerearlr_bandishrozaliam_1951]\] \[[Keener et al 1958][research_keenerearlr_mcleodnormanj_1958]\] \[[Kelly 1955][research_kellythomasc_1955]\] \[[Kemp and King 1956][research_kempwilliambjr_kingthomasjjr_1956]\] \[[Kempel et al 1988][research_kempelrobertw_mcneillwaltere_1988]\] \[[Kirkham et al 1974][research_kirkham_jackson_1974]\] \[[Love and Young 1966][research_loveje_youngwr_1966]\] \[[Matranga 1961][research_matrangagenej_1961]\] \[[Mayer and Valentine 1950][research_mayerjohnp_valentinegeorgem_1950]\] \[[Mayer and Valentine 1951][research_mayerjohnp_valentinegeorgem_1951]\] \[[Mayer et al 1950][research_mayerjohnp_valentinegeorgem_1950_b]\] \[[McDearmon 1956][research_mcdearmonrussellw_1956]\] \[[Moul 1957][research_moulmt_1957]\] \[[Mattson 1947][research_xs1_model_1947]\] \[[Drake et al 1948][research_xs1_accelerated_1948]\] \[[Matthews 1948][research_xs1_downwash_1948]\] \[[Williams et al 1948][research_xs1_handling_1948]\] \[[Beeler and Mayer 1948][research_xs1_loads_1948]\] \[[Mattson and Loving 1948][research_xs1_model_stability_1948]\] \[[Polhamus 1950][research_x1_dynamic_stability_1950]\] \[[Peele 1953][research_d558_slat_1953]\] \[[Knapp and Johnson 1953][research_x1_base_pressures_1953]\] \[[Knapp et al 1953][research_x1_fuselage_pressures_1953]\] \[[Saltzman 1953][research_x1_liftdrag_1953]\] \[[Rogers 1953][research_x1_tail_loads_1953]\] \[[Knapp and Jordan 1953][research_x1_wing_loads_1953]\] \[[Knapp and Jordan 1953][research_x1_wing_pressures_1953]\] \[[Day 1953][research_x2_glide_1953]\] \[[Finch and Walker 1953][research_x5_stability_1953]\] \[[Ankenbruck 1954][research_d558_handling_1954]\] \[[Reed 1955][research_x5_tail_loads_1955]\] \[[McDearmon and Clark 1956][research_x1a_damping_1956]\] \[[McDearmon and Clark 1956][research_x1e_damping_1956]\] \[[Nugent 1957][research_d558_stores_1957]\] \[[Beeler 1961][research_x15_conference_1958]\] \[[Donlan et al 1976][research_xs1_tunnel_1976]\] \[[Smith 1959][research_x1e_stability_1959]\] \[[Day and Reisert 1959][research_x2_mach32_1959]\] \[[Dana 1993][research_x15_lessons_1993]\] \[[Nugent 1954][research_nugentjack_1954]\] \[[Osborne and Stafford 1960][research_osborners_staffordvc_1960]\] \[[Osborne 1949][research_osborneroberts_1949]\] \[[Patterson 1966][research_pattersonjcjr_1966]\] \[[Peele 1954][research_peelejamesr_1954]\] \[[Pendley 1947][research_pendleyroberte_1947]\] \[[Progress of the X-15 1965][research_progress_of_1965]\] \[[Re 1974][research_rerj_1974]\] \[[Redeker and Voersmann 1988][research_redeker_voersmann_1988]\] \[[Research-Airplane-Committee Report on Conference 1958][research_research_airplane_committee_report_1958]\] \[[Day and Stillwell 1952][research_richardeday_wendellhstillwell_1952]\] \[[Quinn and Olinger 1969][research_robertdquinn_frankvolinger_1969]\] \[[Robinson et al 1955][research_robinsonglennh_cothrengeorgeejr_1955]\] \[[Robinson 1948][research_robinsonharoldl_1948]\] \[[Robinson 1954][research_robinsonrossb_1954]\] \[[Row and Fischel 1963][research_row_fischel_1963]\] \[[Sanderson 1965][research_sanderson_1965]\] \[[Silvers and King 1955][research_silvershnorman_kingthomasjjr_1955]\] \[[Sim and Curry 1978][research_simag_curryre_1978]\] \[[Sim and Curry 1984][research_simag_curryre_1984]\] \[[Sisk and Mooney 1953][research_siskthomasr_mooneyjohnm_1953]\] \[[Sjoberg 1950][research_sjobergsa_1950]\] \[[Sjoberg and Champine 1949][research_sjobergsa_champinera_1949]\] \[[Sjoberg et al 1951][research_sjobergsa_peelejamesr_1951]\] \[[Smith 1954][research_smithnormanf_1954]\] \[[Spearman 1953][research_spearmanmleroy_1953]\] \[[Spitzer et al 1972][research_spitzerre_rumseypc_1972]\] \[[Stillwell and Wilmerding 1951][research_stillwellwh_wilmerdingjv_1951]\] \[[Taillon 1958][research_taillonnormanv_1958]\] \[[Vogler 1956][research_voglerraymondd_1956]\] \[[Williams 1991][research_williamswalterc_1991]\] \[[Wilmerding et al 1950][research_wilmerdingjv_stillwellwh_1950]\] \[[Wilson 1967][research_wilsonrj_1967]\] \[[Winston 1969][research_winstonmm_1969]\] \[[Wolowicz and Rediess 1957][research_wolowiczchesterh_rediesshermana_1957]\] \[[Wright 1948][research_wrightjohnb_1948]\] \[[Wright 1948][research_wrightjohnb_1948_b]\] \[[Wright 1948][research_wrightjohnb_1948_c]\] \[[Wright and Loving 1953][research_wrightjohnd_lovingdonaldl_1953]\] \[[Young 1961][research_youngls_1961]\]

### Transonic and supersonic aircraft design, and the sonic boom

**What the transonic result was used for.** Wing and configuration design for transonic and supersonic speeds, supersonic flight and the sonic boom, including the overland acceptability question the article closes on.

**109 records.** \[[Afsar et al 2019][research_afsar_sescu_2019]\] \[[Anderson and Averett 1972][research_anderson_averett_1972]\] \[[Biber 2015][research_biber_2015]\] \[[Pomeroy et al][research_brentwpomeroy_richardlcampbell]\] \[[Brodsky 1970][research_brodsky_1970]\] \[[Bryson 1971][research_brysonjr_1971]\] \[[Budhdev et al 2026][research_budhdev_senthilkumar_2026]\] \[[Carlson and Miller 1969][research_carlsonhw_millerds_1969]\] \[[Carlson et al 1965][research_carlsonharryw_mcleanfedward_1965]\] \[[Celestino et al 2026][research_celestino_olichevishalila_2026]\] \[[Chaloner and Verdinelli 1995][research_chaloner_verdinelli_1995]\] \[[Chau and Zingg 2022][research_chau_zingg_2022]\] \[[Droney et al 2020][research_christopherkdroney_anthonyjsclafani_2020]\] \[[Clark and Adler 2016][research_clark_adler_2016]\] \[[Clyde et al 1984][research_clyde_bonner_1984]\] \[[Coen 2022][research_coen_2022]\] \[[Coen et al 2017][research_coen_loubeau_2017]\] \[[Commercial Transports-Aerodynamic Design for 1982][research_commercial_transports_aerodynamic_1982]\] \[[Crown 1950][research_crown_1950]\] \[[Davies 2020][research_davies_2020]\] \[[Davies 2025][research_davies_2025_b]\] \[[Davis 1985][research_davisjr_1985]\] \[[Davis and Mitchell 1960][research_davisoh_mitchellga_1960]\] \[[DeRoo and Takahashi 2024][research_deroo_takahashi_2024]\] \[[Ding et al 2023][research_ding_han_2023]\] \[[Durston][research_dondurston]\] \[[Driver 1974][research_driver_1974]\] \[[Duan et al 2026][research_duan_wan_2026]\] \[[Electronic autopilot controls supersonic 1956][research_electronic_autopilot_1956]\] \[[Gardner 1978][research_gardner_1978]\] \[[Giles and Drela 1986][research_giles_drela_1986]\] \[[Giles and Drela 1987][research_giles_drela_1987]\] \[[Guo et al 2025][research_guo_wang_2025]\] \[[Haines 1957][research_haines_1957]\] \[[Hartzuiker 1986][research_hartzuiker_1986]\] \[[Hecht 2009][research_hecht_2009]\] \[[History of Supersonic Transport 2020][research_history_of_2020]\] \[[Holdaway and Mellenthin 1960][research_holdawaygeorgeh_mellenthinjacka_1960_b]\] \[[Holst 1999][research_holst_1999]\] \[[Hooker 2014][research_hooker_2014]\] \[[Imig 1973][research_imig_1973]\] \[[Item and Baysal 1995][research_itemcemc_baysaloktay_1995]\] \[[James 1998][research_james_1998]\] \[[Janardhan and Grandhi 2003][research_janardhan_grandhi_2003]\] \[[Jones 1977][research_jones_1977]\] \[[Julian Ooi 2024][research_julianooi_2024]\] \[[Kapania et al 2018][research_kapaniarakeshk_schetzjosepha_2018]\] \[[Kishi et al 2023][research_kishi_yashiro_2023]\] \[[Kolonay and Blair 1994][research_kolonay_blair_1994]\] \[[Krone 1980][research_kronejr_1980]\] \[[Kuhlman et al 1988][research_kuhlman_cerney_1988]\] \[[Laar et al 2024][research_laar_atherstone_2024]\] \[[Lassiter 1981][research_lassiter_1981]\] \[[Li and Geiselhart 2021][research_li_geiselhart_2021]\] \[[Liebhardt 2021][research_liebhardt_2021]\] \[[Liebhardt 2025][research_liebhardt_2025]\] \[[Lin 1982][research_lin_1982]\] \[[Lin 1982][research_lin_1982_b]\] \[[Lock 1961][research_lock_1961]\] \[[Lock 1964][research_lock_1964]\] \[[Lock and Bridgewater 1967][research_lock_bridgewater_1967]\] \[[Lock and Rogers 1962][research_lock_rogers_1962]\] \[[Loving 1961][research_lovingdonaldl_1961]\] \[[MacDonald and Alonso 2020][research_macdonald_alonso_2020]\] \[[Madden 2010][research_madden_2010]\] \[[Malmuth et al 1983][research_malmuth_wu_1983]\] \[[Malmuth et al 1984][research_malmuth_wu_1984]\] \[[Mann and Mercer 1985][research_mann_mercer_1985]\] \[[Mann et al 1983][research_mann_campbell_1983]\] \[[Matsushima and Takanashi 1996][research_matsushima_takanashi_1996]\] \[[McConnell 2006][research_mcconnell_2006]\] \[[Murphy and Schmidt 1953][research_murphy_schmidt_1953]\] \[[NACA Conference on Aerodynamic 1949][research_transonic_conference_1949]\] \[[NACA Conference on Aerodynamic 1947][research_naca_conference_1947]\] \[[Nicolaides and Brady 1959][research_nicolaides_brady_1959]\] \[[Nixon and Nixon 1997][research_nixon_nixon_1997]\] \[[O'Brien and Takahashi 2023][research_obrien_takahashi_2023]\] \[[Pittman et al 1984][research_pittmanjl_millerds_1984]\] \[[Pope and Street 1959][research_pope_street_1959]\] \[[Porter 1965][research_porter_1965]\] \[[Pritulo et al 1995][research_pritulo_gubanov_1995]\] \[[Properties and Design of 2012][research_properties_and_2012]\] \[[Rekhy et al 2020][research_rekhy_shneider_2020]\] \[[Rosenhead 1956][research_rosenhead_1956]\] \[[Segee et al 2016][research_segee_schetz_2016]\] \[[Sisk and Andrews 1963][research_sisk_andrews_1963]\] \[[Slapnicar][research_slapnicar]\] \[[Smith and Campbell 1992][research_smithleighann_campbellrichardl_1992]\] \[[Smolderen 1972][research_smolderen_1972]\] \[[Sobieczky 1983][research_sobieczky_1983]\] \[[Sobieczky and Giessler 1999][research_sobieczky_giessler_1999]\] \[[Spacht 1980][research_spacht_1980]\] \[[Sparkes 2024][research_sparkes_2024]\] \[[Spearman 1979][research_spearmanml_1979]\] \[[Sudhi et al 2021][research_sudhi_radespiel_2021]\] \[[Supersonic Flight 2014][research_supersonic_flight_2014]\] \[[Supersonic Flight 2025][research_supersonic_flight_2025]\] \[[Takovitskii 2023][research_takovitskii_2023]\] \[[Transonic and supersonic flight 1992][research_transonic_and_1992]\] \[[Turbojet and turbofan engines 1964][research_turbojet_and_1964]\] \[[Voet et al 2023][research_voet_speth_2023]\] \[[Wells 1953][research_wells_1953]\] \[[Whitcomb 1983][research_whitcombrt_1983]\] \[[Whitford 1991][research_whitford_1991]\] \[[Williams 1965][research_williams_1965]\] \[[Winarto and Stalker 1984][research_winarto_stalker_1984]\] \[[Xiong et al 2021][research_xiong_bartels_2021]\] \[[Xiong et al 2023][research_xiong_nguyen_2023_b]\] \[[Yagiz and Kandil 2009][research_yagiz_kandil_2009]\]

### Air data, the pitot-static system and knowing the Mach number

**The hardest measurement in the programme.** Pitot and static probes, airspeed and static-source calibration, flush air-data systems and Mach number measurement in flight.

**109 records.** \[[Adams][research_adams]\] \[[Air Force Test Pilot School Edwards Afb Ca 1967][research_airforcetestpilotschooledwardsafbca_1967]\] \[[Air Force Test Pilot School Edwards Afb Ca 1967][research_airforcetestpilotschooledwardsafbca_1967_b]\] \[[Airfoil static-pressure thrust 1990][research_airfoil_static_pressure_1990]\] \[[Airspeed Calibration 2021][research_airspeed_calibration_2021]\] \[[Airspeed Indicator Pitot Static][research_airspeed_indicator]\] \[[Airspeed Indicator Pitot Static][research_airspeed_indicator_b]\] \[[Airspeed Vs Flight Path 2003][research_airspeed_vs_2003]\] \[[Baer 1966][research_baer_1966]\] \[[Bailey et al 1996][research_bailey_knoedler_1996]\] \[[Balla et al 2014][research_balla_rhode_2014]\] \[[Bertelrud 1980][research_bertelrud_1980]\] \[[Bertelrud 1981][research_bertelrud_1981]\] \[[Carbonara and Binnie 1938][research_carbonara_binnie_1938]\] \[[Cline et al 1986][research_cline_hyde_1986]\] \[[Colgren 1996][research_colgren_1996]\] \[[Computation of low density 1985][research_computation_of_1985]\] \[[Crassidis 2005][research_crassidis_2005]\] \[[Curley 1991][research_curley_1991]\] \[[DeLeo and Hagen 1963][research_deleo_hagen_1963]\] \[[Derajat and Hariowibowo 2018][research_derajat_hariowibowo_2018]\] \[[Design and Installation of][research_design_and]\] \[[Dias 2023][research_dias_2023]\] \[[Effect of wind shear 1990][research_effect_of_1990]\] \[[Ellison and Latz 2003][research_ellison_latz_2003]\] \[[Evangelista and Mori 2025][research_evangelista_mori_2025]\] \[[Fischer et al 1971][research_fischer_maddalon_1971]\] \[[Flint and Niewoehner 2011][research_flint_niewoehner_2011]\] \[[Fontaine and Ali 2023][research_fontaine_ali_2023]\] \[[Foster and Cunningham 2010][research_foster_cunningham_2010]\] \[[Freund 2014][research_freund_2014]\] \[[Friehmelt and Jost 2000][research_friehmelt_jost_2000]\] \[[Giez et al 2016][research_giez_mallaun_2016]\] \[[Glaser 1952][research_glaser_1952]\] \[[Gratton 2014][research_gratton_2014]\] \[[Gratton 2018][research_gratton_2018]\] \[[Hagen and Seidel][research_hagen_seidel]\] \[[Hillje and Nelson 1981][research_hillje_nelson_1981]\] \[[Hui and Collins 2001][research_hui_collins_2001]\] \[[Ice and Rain Minimum][research_ice_and]\] \[[Iwai 2018][research_iwai_2018]\] \[[Jarvinen 2013][research_jarvinen_2013]\] \[[Jurado and McGehee 2019][research_jurado_mcgehee_2019]\] \[[Kannenberg and Boyd 1994][research_kannenberg_boyd_1994]\] \[[Karlgaard and Schoenenberger 2017][research_karlgaard_schoenenberger_2017]\] \[[Karns et al 2017][research_karns_strike_2017]\] \[[Kenney 1939][research_kenney_1939]\] \[[Kettle 1954][research_kettle_1954]\] \[[Kimberlin and Sims 1992][research_kimberlin_sims_1992]\] \[[Knoedler et al][research_knoedler_bailey]\] \[[Knoedler et al 1996][research_knoedler_bailey_1996]\] \[[Kokin and Lysenko 1972][research_kokin_lysenko_1972]\] \[[Larson and Siemers 1980][research_larsontj_siemerspmiii_1980]\] \[[Larson et al 1987][research_larsonterryj_whitmorestephena_1987]\] \[[Latif et al 2006][research_latif_masud_2006]\] \[[Latif et al 2007][research_latif_masud_2007]\] \[[Lee et al 2017][research_lee_park_2017]\] \[[Li et al 2022][research_li_lin_2022]\] \[[Lugo et al 2014][research_lugo_tolson_2014]\] \[[Luo 1987][research_luo_1987]\] \[[Maintenance of Pitot-Static Systems][research_maintenance_of]\] \[[Marquardt 1976][research_marquardt_1976]\] \[[Martos et al 2011][research_martos_kiszely_2011]\] \[[Maximum Allowable Airspeed Instruments][research_maximum_allowable]\] \[[McGann 1995][research_mcgann_1995]\] \[[McLaren et al 2007][research_mclaren_jayashankar_2007]\] \[[Merriam and Spaulding 1935][research_merriam_spaulding_1935]\] \[[Milne and Martos 2012][research_milne_martos_2012]\] \[[Minimum Performance Standard for][research_minimum_performance]\] \[[Minimum Performance Standard for][research_minimum_performance_b]\] \[[Mironov et al 2019][research_mironov_aniskin_2019]\] \[[Hasel and Coletti 1948][research_pitot_supersonic_1948]\] \[[Thompson et al 1950][research_airspeed_calibration_1950]\] \[[Niewoehner 2006][research_niewoehner_2006]\] \[[Ower and Pankhurst 1977][research_ower_pankhurst_1977]\] \[[Ower and Pankhurst 1977][research_ower_pankhurst_1977_b]\] \[[Paris and Alaverdi 1998][research_paris_alaverdi_1998]\] \[[Park 2017][research_park_2017]\] \[[Parks and Bach 1990][research_parks_bachjr_1990]\] \[[Pruett et al 1981][research_pruett_wolf_1981]\] \[[Report no. 264, Differential 1927][research_report_no_1927]\] \[[Rizzi and Schmidt 1978][research_rizzi_schmidt_1978]\] \[[Robinson and Blanchard 2003][research_robinson_blanchard_2003]\] \[[Roh et al 2006][research_roh_park_2006]\] \[[Savage and Bommerscheim 1962][research_savage_bommerscheim_1962]\] \[[Savin 1958][research_savinraymondc_1958]\] \[[Siemers et al 1983][research_siemersiii_wolf_1983]\] \[[Sklenář and Matějů 2022][research_sklenar_mateju_2022]\] \[[Smetana 1965][research_smetana_1965]\] \[[Strack 1964][research_strack_1964]\] \[[Swafford et al 1995][research_swafford_bomba_1995]\] \[[Tacina et al 2004][research_tacina_fernandez_2004]\] \[[Takahashi et al 2026][research_takahashi_2026_airdata]\] \[[Taylor 2012][research_taylor_2012]\] \[[Tilmans et al 2024][research_tilmans_jackisch_2024]\] \[[Timofeev and Aniskin 2018][research_timofeev_aniskin_2018]\] \[[VanderWyst 2008][research_vanderwyst_2008]\] \[[Vasconcelos et al 2011][research_vasconcelos_leite_2011]\] \[[Véras et al 2022][research_veras_souzademouralima_2022]\] \[[Wada 1924][research_wada_1924]\] \[[Wang et al 2026][research_wang_kang_2026]\] \[[Woeste 1992][research_woeste_1992]\] \[[Wolf et al 1988][research_wolf_henry_1988]\] \[[Woodford and Hansen 1985][research_woodford_hansen_1985]\] \[[Wootton 1967][research_wootton_1967]\] \[[Xiong et al 2011][research_xiong_shang_2011]\] \[[Yang et al 2026][research_yang_li_2026]\] \[[Young][research_young]\] \[[Zolovcik 1950][research_zolovcikjohna_1950]\]

### Rocket propulsion and the pressure-fed engine

**The engine and the energy it supplied.** Rocket-powered aircraft, pressure-fed liquid engines, air launch and the energy-state treatment of performance. **The twelve pressure-fed titles here all concern rockets, launch vehicles and test stands rather than aircraft**, and nine of the eighteen titles naming a rocket together with an aircraft date from before 1960, so the literature that matches the X-1's own engine and airframe combination is small.

**61 records.** \[[Abada et al 2024][research_abada_kbab_2024]\] \[[Airplane and rocket flight 1990][research_airplane_and_1990]\] \[[Baxter 1947][research_baxter_1947]\] \[[Bonometti and Sorensen 2006][research_bonometti_sorensen_2006]\] \[[Bryson and Desai 1968][research_brysonjr_desai_1968]\] \[[Burdett 1947][research_burdett_1947]\] \[[Burgess 1946][research_burgess_1946]\] \[[Burton et al 2007][research_burton_loth_2007]\] \[[Carey 1964][research_carey_1964]\] \[[Carey 1965][research_carey_1965]\] \[[Cicala and Miele 1956][research_cicala_miele_1956]\] \[[El-Sayed 2016][research_elsayed_2016]\] \[[Fritz and Sackheim 1982][research_fritz_sackheim_1982]\] \[[Fritz et al 2025][research_fritz_patel_2025]\] \[[Gangeh et al 2023][research_gangeh_bui_2023]\] \[[Goh 2008][research_goh_2008]\] \[[Grosdemange and Schaeffer 1990][research_grosdemange_schaeffer_1990]\] \[[Hataue 1991][research_hataue_1991]\] \[[Hoyt 2006][research_hoyt_2006]\] \[[Huse 1948][research_huse_1948]\] \[[James 1981][research_jamesjr_1981]\] \[[Johnson 1972][research_johnson_1972]\] \[[Joshi et al 2023][research_joshi_salahudden_2023]\] \[[Kish et al 2019][research_kish_wilde_2019]\] \[[Kleppin et al 1980][research_kleppin_ruetenik_1980]\] \[[Lempert 1975][research_lempert_1975]\] \[[Ley 1936][research_ley_1936]\] \[[Martin and Jackson 1994][research_martin_jackson_1994]\] \[[Massa 2014][research_massa_2014]\] \[[Miele 1955][research_miele_1955]\] \[[Miele 1957][research_miele_1957]\] \[[Mobley and Jones 1989][research_mobley_jones_1989]\] \[[Montaini and Carlotti 2026][research_montaini_carlotti_2026]\] \[[Norris 1979][research_norris_1979]\] \[[Olejnik and Zalewski 2020][research_olejnik_zalewski_2020]\] \[[Oruc and Baklacioglu 2022][research_oruc_baklacioglu_2022]\] \[[Oruc and Baklacioglu 2023][research_oruc_baklacioglu_2023]\] \[[Parlier 1986][research_parlier_1986]\] \[[Piecewicz and Kindsvogel 1943][research_piecewicz_kindsvogel_1943]\] \[[Poth et al 1993][research_pothjr_fisher_1993]\] \[[Pritts 1974][research_pritts_1974]\] \[[Quinn 1999][research_quinn_1999]\] \[[Reinhardt 1948][research_reinhardt_1948]\] \[[Ringas 2022][research_ringas_2022]\] \[[Rocket-Powered Aircraft 2017][research_rocket_powered_aircraft_2017]\] \[[Rothmund and Harlow 1999][research_rothmund_harlow_1999]\] \[[Rubin 1971][research_rubin_1971]\] \[[Ruetenik and Smiley 1978][research_ruetenik_smiley_1978]\] \[[Sakaki et al 2015][research_sakaki_kakudo_2015]\] \[[Sakaki et al 2016][research_sakaki_kakudo_2016]\] \[[Sarigul-Klijn et al 2005][research_sarigulklijn_sarigulklijn_2005]\] \[[Sarigul-Klijn et al 2008][research_sarigulklijn_sarigulklijn_2008]\] \[[Sarigulklijn et al 2012][research_sarigulklijn_sarigulklijn_2012]\] \[[Sorensen and Blevins 2001][research_sorensen_blevins_2001]\] \[[Sá Gontijo et al 2025][research_sagontijo_filho_2025]\] \[[Tsutsumi et al 2012][research_tsutsumi_takaki_2012]\] \[[Vernacchia et al 2022][research_vernacchia_2022]\] \[[Vlasyk and Korshunova 2025][research_vlasyk_korshunova_2025]\] \[[Wang et al 2022][research_wang_li_2022]\] \[[Wu et al 1999][research_wu_fuller_1999]\] \[[Zhang and Zhang 2020][research_zhang_zhang_2020]\]

### Other transonic, high-speed and flight research literature

**The residual, reported and not hidden.** On-subject high-speed aerodynamic work belonging to no cluster above, including inlets, nozzles and afterbodies, vortex flow over delta and swept wings, slender bodies and projectiles, and supersonic jet noise. **The residual holds about a tenth of the survey**, which reflects a band that every high-speed vehicle must cross rather than a subject with sharp edges.

**476 records.** \[[Abu-Mostafa and Reed 1984][research_abumostafaas_reedtd_1984]\] \[[Adams and John C. 1968][research_adams_johnc_1968]\] \[[Adaptive Transonic Aeroservoelasticity 2016][research_adaptive_transonic_2016]\] \[[Advanced Fuel Research Inc East Hartford Ct 1957][research_advancedfuelresearchinceasthartfordct_1957]\] \[[Aerodynamic Forces on Aircraft 1995][research_aerodynamic_forces_1995]\] \[[Agopian 1974][research_agopiankg_1974]\] \[[Ahmed and Selvarajan 1991][research_ahmed_selvarajan_1991]\] \[[Aircraft Performance 2026][research_aircraft_performance_2026]\] \[[Alvi 2005][research_alvi_2005]\] \[[Amouyal and Weihs 2015][research_amouyal_weihs_2015]\] \[[Amouyal and Weihs 2016][research_amouyal_weihs_2016]\] \[[André et al 2013][research_andre_castelain_2013]\] \[[Appendix C Aircraft Performance 1997][research_appendix_c_1997]\] \[[Appich 1978][research_appichjr_1978]\] \[[Ardema and Williams 1972][research_ardema_williams_1972]\] \[[Army War Coll Carlisle Barracks Pa 1952][research_armywarcollcarlislebarrackspa_1952]\] \[[Arunajatesan et al 2008][research_arunajatesan_cattafesta_2008]\] \[[Askari and Soltani 2019][research_askari_soltani_2019]\] \[[Atifatul Ismah Ismail 2021][research_atifatulismahismail_2021]\] \[[Atta and Nayfeh 1978][research_atta_nayfeh_1978]\] \[[Axelson 1975][research_axelson_1975]\] \[[Axelson 1977][research_axelson_1977]\] \[[Babinsky 2014][research_babinsky_2014]\] \[[Bacci and Saddington 2022][research_bacci_saddington_2022]\] \[[Bacci and Saddington 2026][research_bacci_saddington_2026_b]\] \[[Bacci et al 2026][research_bacci_saddington_2026]\] \[[Bai et al 2015][research_bai_li_2015]\] \[[Balsa and Goldstein 1990][research_balsa_goldstein_1990]\] \[[Bare et al 1987][research_bare_reubush_1987]\] \[[Barrett-Gonzalez and Wolf 2021][research_barrett_gonzalez_2021]\] \[[Barufaldi et al 2019][research_barufaldi_morales_2019]\] \[[Bashkirov and Ogorodnikov 2018][research_bashkirov_ogorodnikov_2018]\] \[[Batill et al 1982][research_batill_nelson_1982]\] \[[Batina 1988][research_batina_1988_c]\] \[[Batina 1989][research_batina_1989_b]\] \[[Bauer et al 1983][research_bauerf_garabedianp_1983]\] \[[Bendiksen 2011][research_bendiksen_2011]\] \[[Bertelrud and Graves 1994][research_bertelrud_graves_1994]\] \[[Bippes 1990][research_bippes_1990]\] \[[Black et al 1963][research_black_carleton_1963]\] \[[Bodapati 1984][research_bodapati_1984]\] \[[Bodapati 1984][research_bodapati_1984_b]\] \[[Bodapati and Lee 1986][research_bodapati_lee_1986]\] \[[Bodspat et al 1980][research_bodspat_schairer_1980]\] \[[Bogdnoff 1953][research_bogdnoff_1953]\] \[[Bowers 1980][research_bowers_1980]\] \[[Boyles 1986][research_boylesjr_1986]\] \[[Briggs et al 1982][research_briggs_reed_1982]\] \[[Bruce et al 1984][research_brucejr_fuller_1984]\] \[[Brunton et al 2020][research_brunton_noack_2020]\] \[[Bryce and Pinker 1977][research_bryce_pinker_1977]\] \[[Bryson and Rumpfkeil 2016][research_bryson_rumpfkeil_2016]\] \[[Buckingham 1914][research_buckingham_1914]\] \[[Burstein 1965][research_burstein_1965]\] \[[Campbell 1984][research_campbell_1984]\] \[[Candler 2001][research_candler_2001]\] \[[Capone et al 1987][research_capone_re_1987]\] \[[Capone and Maiden 1977][research_caponefj_maidendl_1977]\] \[[Carter et al 2009][research_carter_vicroy_2009]\] \[[Cebeci 1974][research_cebecit_1974]\] \[[Celik and Roberts 1992][research_celik_roberts_1992]\] \[[Chakraborty et al 2015][research_chakraborty_ozcan_2015]\] \[[Chan et al 2017][research_chan_hooker_2017]\] \[[Chapman et al 1992][research_chapman_bonness_1992]\] \[[Chaudhuri 1977][research_chaudhuri_1977]\] \[[Chen 2018][research_chen_2018]\] \[[Chen and Liu 2000][research_chen_liu_2000]\] \[[Chen et al 1989][research_chen_cantwell_1989]\] \[[Chen et al 1990][research_chen_cantwell_1990]\] \[[Chen-Chi 1983][research_chenchi_1983]\] \[[Cheng 1977][research_cheng_1977]\] \[[Cheng 1989][research_cheng_1989]\] \[[Cheng and Hafez 1975][research_cheng_hafez_1975]\] \[[Chou and Smith 1978][research_chou_smith_1978]\] \[[Chow 1979][research_chow_1979]\] \[[Christian et al 2023][research_christian_gee_2023]\] \[[Chung 2000][research_chung_2000]\] \[[Chung 2002][research_chung_2002]\] \[[Chung 2003][research_chung_2003]\] \[[Chung 2007][research_chung_2007]\] \[[Cler 1995][research_cler_1995]\] \[[Coen et al 2023][research_coen_loubeau_2023]\] \[[Cole 1985][research_cole_1985]\] \[[Cole 1986][research_cole_1986]\] \[[Cole et al 1980][research_cole_cook_1980]\] \[[Collins 1970][research_collins_1970]\] \[[Conti et al 1972][research_contirj_thomaspd_1972]\] \[[Cook 1979][research_cook_1979]\] \[[Cook 1995][research_cook_1995]\] \[[Cosenza and Kummeth 1974][research_cosenza_kummeth_1974]\] \[[Cottrell and Lijewski 1987][research_cottrell_lijewski_1987]\] \[[Cottrell et al 1987][research_cottrell_martinez_1987]\] \[[Coustols et al 1995][research_coustols_prudhomme_1995]\] \[[Crisalli et al 1979][research_crisalli_stahara_1979]\] \[[Cunningham 1994][research_cunningham_1994]\] \[[Cunningham 1974][research_cunninghamamjr_1974]\] \[[Currao and Jiang 2026][research_currao_jiang_2026]\] \[[D. Supersonic and Transonic 1954][research_d_supersonic_1954]\] \[[Dahlke 1969][research_dahlke_1969]\] \[[Danberg and Tschirschnitz 1983][research_danberg_tschirschnitz_1983]\] \[[Das and Cohen 2017][research_das_cohen_2017]\] \[[Das and Kim 2016][research_das_kim_2016]\] \[[DeBonis et al 1995][research_debonis_georgiadis_1995]\] \[[Demetriades 1985][research_demetriades_1985]\] \[[Devan 1987][research_devan_1987]\] \[[Devan and Kania 1985][research_devan_kania_1985]\] \[[Di Fabbio et al 2022][research_difabbio_tangermann_2022]\] \[[Diesperov and Ryzhov 1971][research_diesperov_ryzhov_1971]\] \[[Dippold and Zaman 2015][research_dippold_zaman_2015]\] \[[Durston][research_dondurston_b]\] \[[Donlan 1976][research_donlan_collected_1976]\] \[[Dorsch and Brun 1953][research_dorschrobertg_brunrinaldoj_1953]\] \[[Dowell et al 1981][research_dowell_williams_1981]\] \[[Dowell et al 2001][research_dowell_thomas_2001]\] \[[Dupuis 2002][research_dupuis_2002]\] \[[Efrati and Raveh 2026][research_efrati_raveh_2026]\] \[[El-Naggar et al 2004][research_elnaggar_klamo_2004]\] \[[Elbanna and Carlson 1989][research_elbanna_carlson_1989]\] \[[ElRamly][research_elramly]\] \[[Engelbrecht][research_engelbrecht]\] \[[Epstein 1954][research_epstein_1954]\] \[[Erickson and Rogers 1987][research_erickson_rogers_1987]\] \[[Erickson et al 1989][research_erickson_hall_1989]\] \[[Erickson et al 1990][research_erickson_schreiner_1990_b]\] \[[Erickson and Gonzalez 2004][research_ericksongarye_gonzalezhugoa_2004]\] \[[Erickson and Gonzalez 2005][research_ericksongarye_gonzalezhugoa_2005]\] \[[Ericsson 1986][research_ericsson_1986]\] \[[European Transonic Windtunnel Project 1990][research_european_transonic_1990]\] \[[Experience Gained During Development 2010][research_experience_gained_2010]\] \[[Experimental Testing at Transonic 1982][research_experimental_testing_1982]\] \[[Farbridge and Smith 1977][research_farbridge_smith_1977]\] \[[Farbridge and Smith 1978][research_farbridge_smith_1978]\] \[[Fay and Riddell 1958][research_fay_riddell_1958]\] \[[Ferrand and Aubert 1994][research_ferrand_aubert_1994]\] \[[Finat'ev et al 1968][research_finatev_shcherbakov_1968]\] \[[Fisher 1978][research_fisherdf_1978]\] \[[Fitzhugh 1970][research_fitzhugh_1970]\] \[[Flax 1973][research_flax_1973]\] \[[Flores and Van Dalsem 1985][research_flores_vandalsem_1985]\] \[[Flores and Van Dalsem 1986][research_flores_vandalsem_1986]\] \[[Fraser 1975][research_fraser_1975]\] \[[Fujii][research_fujii]\] \[[Fuller and Williams 1986][research_fuller_williams_1986]\] \[[Fuller 1982][research_fullerde_1982]\] \[[Fuller et al 1981][research_fullerde_glossbb_1981]\] \[[G. The Experimental Aerodynamics 1957][research_g_the_1957]\] \[[Garabedian 1974][research_garabedian_1974]\] \[[Garrell et al 2006][research_garrell_nowakowski_2006]\] \[[Gartner and Amitay 2015][research_gartner_amitay_2015]\] \[[Gee et al 2025][research_gee_olaveson_2025]\] \[[Georgiadis et al 2021][research_georgiadis_wernet_2021]\] \[[Georgiadis et al 2024][research_georgiadis_wernet_2024]\] \[[German 1975][research_german_1975]\] \[[German Development of the 2010][research_german_development_2010]\] \[[Ghoreyshi et al 2017][research_ghoreyshi_darragh_2017]\] \[[Gloss 1984][research_gloss_1984]\] \[[Gloss 1992][research_gloss_1992]\] \[[Goodheart et al 2003][research_goodheart_dykas_2003]\] \[[Goorjian and Obayashi 1989][research_goorjianpeterm_obayashishigeru_1989]\] \[[Goorjian and Obayashi 1990][research_goorjianpeterm_obayashishigeru_1990]\] \[[Griffin and Jonas 1983][research_griffin_jonas_1983]\] \[[Grund and Konarski 1971][research_grund_konarski_1971]\] \[[Guiler][research_guiler]\] \[[Guy et al 1999][research_guy_morrow_1999]\] \[[Hammerton and Kerschen 1998][research_hammertonpw_kerschenej_1998]\] \[[Hanly 1974][research_hanly_1974]\] \[[Hanman et al 2025][research_hanman_yao_2025]\] \[[Hanson and Fink 1978][research_hansondb_finkmr_1978]\] \[[Hanumantharayappa et al 2022][research_hanumantharayappa_thantanapally_2022]\] \[[Harrison et al 2016][research_harrison_darragh_2016]\] \[[Hayes 1968][research_hayesc_1968]\] \[[Heath 2014][research_heath_2014]\] \[[Heltsley and Cline 1979][research_heltsley_cline_1979]\] \[[Hemsch 1988][research_hemsch_1988]\] \[[Henderson 1990][research_henderson_1990]\] \[[Henderson 1991][research_henderson_1991]\] \[[Herring 2008][research_herring_2008]\] \[[Hersch 1970][research_hersch_1970]\] \[[Holdaway and Mellenthin 1960][research_holdawaygeorgeh_mellenthinjacka_1960]\] \[[Hornung and Elsenaar 1988][research_hornung_elsenaar_1988]\] \[[Horstman 1982][research_horstman_1982]\] \[[Horstman 1983][research_horstman_1983]\] \[[Howell 1980][research_howell_1980]\] \[[Hsieh 1975][research_hsieh_1975]\] \[[Hsu and Anderson 1961][research_hsu_anderson_1961]\] \[[Hube 1978][research_hube_1978]\] \[[Humphries et al 1998][research_humphries_gillan_1998]\] \[[Theoretical studies to refine 1970][research_ii_1970]\] \[[Iyer and Takahashi 2025][research_iyer_takahashi_2025]\] \[[Jacobs et al 2012][research_jacobs_ran_2012]\] \[[Jagharghi et al 1995][research_jagharghi_cler_1995]\] \[[Jente 2022][research_jente_2022]\] \[[Jettmar 1984][research_jettmar_1984]\] \[[Jingeleski et al 2013][research_jingeleski_schetz_2013]\] \[[Johnson 1986][research_johnson_1986]\] \[[Johnson and King 1986][research_johnson_king_1986]\] \[[Jones 1947][research_jones_1947]\] \[[Jones 1976][research_jonesrt_1976]\] \[[June et al 2025][research_june_hickey_2025]\] \[[Kabaleeshwaran et al 2026][research_kabaleeshwaran_das_2026]\] \[[Kandil and Hu 1988][research_kandil_hu_1988]\] \[[Kandil and Kamdil 1994][research_kandil_kamdil_1994]\] \[[Karpovich and Frankl 1951][research_karpovichea_franklfi_1951]\] \[[Kaul 2024][research_kaul_2024]\] \[[Kaul and Nguyen 2019][research_kaul_nguyen_2019]\] \[[Kaul and Nguyen 2019][research_kaulupenderk_nguyennhant_2019]\] \[[Kayser et al 1986][research_kayser_clay_1986]\] \[[Kelly et al 2025][research_kelly_jamal_2025]\] \[[Kennelly et al 1999][research_kennellyrobertajr_carmichaelralphl_1999]\] \[[Kentfield and Spragins 2004][research_kentfield_spragins_2004]\] \[[Kickert Reiner 2012][research_kickertreiner_2012]\] \[[Kim and Winchenbach 1985][research_kim_winchenbach_1985]\] \[[King et al 2012][research_kingrudolpha_andinomarlyny_2012]\] \[[King et al 2013][research_kingrudolpha_andinomarlyny_2013]\] \[[Klug et al 2021][research_klug_naik_2021]\] \[[Knott 1974][research_knott_1974]\] \[[Ko et al 2003][research_ko_mason_2003]\] \[[Koenig 1984][research_koenig_1984]\] \[[Konrath 2015][research_konrath_2015]\] \[[Konrath et al 2006][research_konrath_schroder_2006]\] \[[Kontogiannis et al 2019][research_kontogiannis_parenteau_2019]\] \[[Kordan et al 1985][research_kordan_vonlavante_1985]\] \[[Kraiko and Shapovalov 2022][research_kraiko_shapovalov_2022]\] \[[Krone 1980][research_kronejr_1980_b]\] \[[Kroos 1995][research_kroos_1995]\] \[[Krothapalli et al 2003][research_krothapalli_alvi_2003]\] \[[Kruiswyk and Dutton 1989][research_kruiswyk_dutton_1989]\] \[[Kruse et al 2012][research_kruse_wunderlich_2012]\] \[[Kummer et al 2012][research_kummer_allred_2012]\] \[[Kusunose et al 1987][research_kusunose_marcum_1987]\] \[[Kuz'min 2010][research_kuzmin_2010]\] \[[Küchemann 1962][research_kuchemann_1962]\] \[[Labbe et al 2009][research_labbesteveng_gilbertmichaelg_2009]\] \[[Lacey 1979][research_lacey_1979]\] \[[Lacy and Sclafani 2016][research_lacy_sclafani_2016]\] \[[Lada and Kontis 2009][research_lada_kontis_2009]\] \[[Lada and Kontis 2011][research_lada_kontis_2011]\] \[[Laderman 1979][research_laderman_1979]\] \[[Lagen and Seiner 1990][research_lagennicholast_seinerjohnm_1990]\] \[[Large 1981][research_large_1981]\] \[[Lashkov et al 2016][research_lashkov_karpenko_2016]\] \[[Latham et al 1977][research_lathame_gawienowskij_1977]\] \[[Lavala and Das 2025][research_lavala_das_2025]\] \[[Lester and Gragston 2021][research_lester_gragston_2021]\] \[[Lester and Gragston 2022][research_lester_gragston_2022]\] \[[Lewis and Neel 1964][research_lewis_neel_1964]\] \[[Lijewski 1993][research_lijewski_1993]\] \[[Lindley 1956][research_lindley_1956]\] \[[Lindsey 1954][research_lindseywalterf_1954]\] \[[Linearized Theory Transonic 1986][research_linearized_theory_1986]\] \[[Liu et al 2019][research_liu_dong_2019]\] \[[Liu et al 2023][research_liu_liu_2023]\] \[[Lockheed-Georgia Co Marietta 1969][research_lockheedgeorgiacomarietta_1969]\] \[[Long 2003][research_long_2003]\] \[[Loupy and Barakos 2017][research_loupy_barakos_2017]\] \[[Mack 1979][research_mack_1979]\] \[[Mack 1989][research_mack_1989]\] \[[Majdalani and Maicke 2010][research_majdalani_maicke_2010]\] \[[Malmuth et al 1985][research_malmuth_wu_1985]\] \[[Mao et al 2023][research_mao_jing_2023]\] \[[Mao et al 2023][research_mao_jing_2023_b]\] \[[Martínez et al 2015][research_martinez_gennaro_2015]\] \[[Mason 1993][research_mason_1993]\] \[[McIntyre et al 1998][research_mcintyre_bowersox_1998]\] \[[McIntyre et al 1999][research_mcintyre_bowersox_1999]\] \[[McKinney and Gloss 1982][research_mckinney_gloss_1982]\] \[[Medved 1990][research_medved_1990]\] \[[Mehta 1988][research_mehta_1988]\] \[[Mehta and Mehta 1997][research_mehta_mehta_1997]\] \[[Mendenhall 1980][research_mendenhall_1980]\] \[[Menon and Skews 2009][research_menon_skews_2009]\] \[[Menzies and Kandil 1996][research_menzies_kandil_1996]\] \[[Menzies et al 1995][research_menzies_kandil_1995]\] \[[Meyers et al 1992][research_meyersjamesf_leejosephw_1992]\] \[[Mikhail 1989][research_mikhail_1989]\] \[[Mikhalev 2008][research_mikhalev_2008]\] \[[Mixing and Mixing Enhancement 1991][research_mixing_and_1991]\] \[[Molki and Ogbozor 2026][research_molki_ogbozor_2026]\] \[[Moore 1972][research_moore_1972]\] \[[Moore and Frei 1983][research_moore_frei_1983]\] \[[Morrida et al 2017][research_morrida_delucca_2017]\] \[[Myers and Ruo 1983][research_myers_ruo_1983]\] \[[Robinson and Becker 1942][research_cowling_highspeed_1942]\] \[[Henderson et al 1952][research_f86_squadron_1952]\] \[[Hamer and Mayo 1953][research_f84g_squadron_1953]\] \[[Nakagawa and Dahm 2000][research_nakagawa_dahm_2000]\] \[[Nangia and Palmer 2000][research_nangia_palmer_2000]\] \[[Nangia et al 2003][research_nangia_palmer_2003]\] \[[Butchart et al 1959][research_jet_transport_highspeed_1959]\] \[[Moes et al 1998][research_aerospike_sr71_1998]\] \[[Nastase and Rudianu 1990][research_nastase_rudianu_1990]\] \[[Nastase and Weisensee 1984][research_nastase_weisensee_1984]\] \[[Nenni 1980][research_nenni_1980]\] \[[Nguyen and Xiong 2023][research_nguyen_xiong_2023_b]\] \[[Nguyen and Xiong][research_nhannguyen_juntaoxiong]\] \[[Nichols and Goral 1952][research_nicholsmarkr_goraledwinb_1952]\] \[[Nichols and Rinkoski 1952][research_nicholsmarkr_rinkoskidonaldw_1952]\] \[[Nichols and Goral 1947][research_nicholsmarkr_goraledwinb_1947]\] \[[Nicholson and lowry 1966][research_nicholson_lowry_1966]\] \[[Nicks and McKinney 1978][research_nicks_mckinney_1978]\] \[[Nietubicz 1975][research_nietubicz_1975]\] \[[Nietubicz et al 1984][research_nietubicz_sahu_1984]\] \[[Nixon and Nixon 1997][research_nixon_nixon_1997_b]\] \[[Nixon and Tzuoo 1986][research_nixon_tzuoo_1986]\] \[[Nixon and Tzuoo 1987][research_nixon_tzuoo_1987]\] \[[Nomura 2003][research_nomura_2003]\] \[[Nonomura and Fujii 2008][research_nonomura_fujii_2008]\] \[[Norum and Brown 1993][research_norum_brown_1993]\] \[[Nyquist 1928][research_nyquist_1928]\] \[[Timothy and Lewis 2001][research_o_lewis_2001]\] \[[Oberkampf 1978][research_oberkampf_1978]\] \[[Olles et al 2004][research_olles_lynn_2004]\] \[[Olsen 1966][research_olsen_1966]\] \[[Ormsbee 1962][research_ormsbee_1962]\] \[[Osborne 1957][research_osborneroberts_1957]\] \[[Oswald 1932][research_oswald_1932]\] \[[Owen and Owen 2014][research_owen_owen_2014]\] \[[Owens et al 2003][research_owens_capone_2003]\] \[[Oyama et al 2008][research_oyama_ito_2008]\] \[[Ozawa and Nonomura 2024][research_ozawa_nonomura_2024]\] \[[Palko 1972][research_palko_1972]\] \[[Palko 1973][research_palko_1973]\] \[[Palko 1974][research_palko_1974]\] \[[Panda et al 2005][research_pandajayanta_seasholtzrichardg_2005]\] \[[Pao 1976][research_pao_1976]\] \[[Parthasarathy and Massier 1976][research_parthasarathy_massier_1976]\] \[[Petynia et al 1958][research_petyniawilliamw_croomdelwinr_1958]\] \[[Pipko 1966][research_pipko_1966]\] \[[Pittsburgh Univ Washington Dc Research Staff 1966][research_pittsburghunivwashingtondcresearchstaff_1966]\] \[[Platzer 2010][research_platzer_2010]\] \[[Plentovich 1988][research_plentovich_1988]\] \[[Polivanov 2018][research_polivanov_2018]\] \[[Polonsky 2026][research_polonsky_2026]\] \[[Prandtl 1928][research_prandtl_1928]\] \[[Prata et al 2022][research_prata_2022]\] \[[Price 1979][research_price_jr_1979]\] \[[Putnam and Mace 1983][research_putnam_mace_1983]\] \[[Pyle 1965][research_pylejs_1965]\] \[[Qin et al 2000][research_qin_zhu_2000]\] \[[Ramm 1990][research_ramm_1990_b]\] \[[Ranawake 2015][research_ranawake_2015]\] \[[Ranlet 1965][research_ranlet_1965]\] \[[Raveh 2011][research_raveh_2011]\] \[[Reichert 1947][research_reichert_1947]\] \[[Rein et al 2025][research_rein_henne_2025]\] \[[Review of Transonic Aerodynamics 1982][research_review_of_1982]\] \[[Richter and Rosemann 2002][research_richter_rosemann_2002]\] \[[Rimer et al 1983][research_rimer_chipman_1983]\] \[[Riou et al 2010][research_riou_garnier_2010]\] \[[Rizk 1980][research_rizk_1980]\] \[[Rizk 1981][research_rizk_1981]\] \[[Robinson and High 1974][research_robinson_high_1974]\] \[[Robinson and Robinson 1950][research_robinson_robinson_1950]\] \[[Rodemich and Andrew 1965][research_rodemich_andrew_1965]\] \[[Roecker 1955][research_roecker_1955]\] \[[Rogers and Walter K. 1953][research_rogers_walterk_1953]\] \[[Rogers and Walter K. 1958][research_rogers_walterk_1958]\] \[[Roiati et al 2023][research_roiati_anderson_2023]\] \[[Rom 1965][research_rom_1965]\] \[[Ross 2021][research_ross_2021]\] \[[Roussel et al 2015][research_roussel_alizard_2015]\] \[[Runyan and Woolston 1957][research_runyanharryl_woolstondonalds_1957]\] \[[Ruo et al 1973][research_ruo_theisen_1973]\] \[[Ruo 1978][research_ruosy_1978]\] \[[Russell et al 2022][research_russell_werner_2022]\] \[[Sabin 1957][research_sabin_1957]\] \[[Sahu 2008][research_sahu_2008]\] \[[Sanghi et al 2025][research_sanghi_riso_2025]\] \[[Sarohia 1977][research_sarohia_1977]\] \[[Schlinker et al 2010][research_schlinker_simonich_2010]\] \[[Schmeer and Runckel 1962][research_schmeerjamesw_runckeljackf_1962]\] \[[Schuster and Byrd 2003][research_schusterdavidm_byrdjamese_2003]\] \[[Selberg et al 1991][research_selbergbrucep_rokhsazkamran_1991]\] \[[Kelly et al][research_sethkelly_tausifjamal]\] \[[Kelly et al][research_sethwkelly_tausifjamal]\] \[[Sewall 1984][research_sewall_1984]\] \[[Shannon 1948][research_shannon_1948]\] \[[Sheridan et al 2017][research_sheridan_young_2017]\] \[[Shi et al 2019][research_shi_wen_2019]\] \[[Shi et al 2020][research_shi_chen_2020]\] \[[Shmyglevskii 1960][research_shmyglevskii_1960]\] \[[Sichel 1970][research_sichel_1970]\] \[[Sichel and Yin 1966][research_sichel_yin_1966]\] \[[Sigal 1984][research_sigal_1984]\] \[[Silva 1993][research_silva_1993]\] \[[Sinclair 1981][research_sinclair_1981]\] \[[Skujins and Cesnik 2011][research_skujins_cesnik_2011]\] \[[Smetana 1973][research_smetana_1973]\] \[[Smith et al 2008][research_smith_henfling_2008]\] \[[Smith and Farbridge 1979][research_smithronaldc_farbridgeje_1979]\] \[[Soltani and Farahani 2011][research_soltani_farahani_2011]\] \[[Spreiter 1959][research_spreiter_1959]\] \[[Srakowski et al 1980][research_srakowski_shrewsbury_1980]\] \[[Steer 2000][research_steer_2000]\] \[[Stengel 1969][research_stengel_1969]\] \[[Stock 1975][research_stock_1975]\] \[[Stone 1945][research_stone_1945]\] \[[Strome 1969][research_strome_1969]\] \[[Subramani et al 2025][research_subramani_m_2025]\] \[[Sugioka et al 2021][research_sugioka_2021]\] \[[Supersonic Cruise 1981][research_supersonic_cruise_1981]\] \[[Supersonic Maneuvers in a 1981][research_supersonic_maneuvers_1981]\] \[[Supersonic Turn 1981][research_supersonic_turn_1981]\] \[[Sutherland 1893][research_sutherland_1893]\] \[[Swafford 1979][research_swafford_1979]\] \[[Szodruch 1980][research_szodruchj_1980]\] \[[Takahashi and Stone 2019][research_takahashi_stone_2019]\] \[[Takahashi et al 2019][research_takahashi_boccieri_2019]\] \[[Takikawa et al 2025][research_takikawa_hosono_2025]\] \[[Tamada and Shibaoka 1955][research_tamada_shibaoka_1955]\] \[[Tatsumi and Takanashi 1985][research_tatsumi_takanashi_1985]\] \[[Tempelmeyer and Osborne 1955][research_tempelmeyerkennethe_osborneroberts_1955]\] \[[Terakado et al 2016][research_terakado_nonomura_2016]\] \[[Tewari 1993][research_tewari_1993]\] \[[Tournier et al 2005][research_tournier_paduano_2005]\] \[[Transonic Aerodynamics 1982][research_transonic_aerodynamics_1982]\] \[[Transonic Aerodynamics 1986][research_transonic_aerodynamics_1986]\] \[[Transonic Aerodynamics Problems in 1993][research_transonic_aerodynamics_1993]\] \[[Transonic Aerodynamics-History and Statement 1982][research_transonic_aerodynamics_history_1982]\] \[[Transonic Aircraft Configurations 2012][research_transonic_aircraft_2012]\] \[[Transonic and Supersonic Flows 2012][research_transonic_and_2012]\] \[[Transonic Expansion Procedures Simple 1986][research_transonic_expansion_1986]\] \[[Transonic Far Fields 1986][research_transonic_far_1986]\] \[[Triebstein 1986][research_triebstein_1986]\] \[[Trilling and Covert 1955][research_trilling_covert_1955]\] \[[Ueda and Dowell 1984][research_uedat_dowelleh_1984]\] \[[Unsteady supersonic flow past 1981][research_unsteady_supersonic_1981]\] \[[Unsteady Transonic Aerodynamics 1989][research_unsteady_transonic_1989]\] \[[Usry et al 1991][research_usryjimmyw_meyersjamesf_1991]\] \[[Varner 1974][research_varner_1974]\] \[[Vasenev and Kharitonov 1991][research_vasenev_kharitonov_1991]\] \[[Vasil'chenko 1981][research_vasilchenko_1981]\] \[[Vaughn 1982][research_vaughnjr_1982]\] \[[Veltin et al 2010][research_veltin_day_2010]\] \[[Verma and Rathakrishnan 2002][research_verma_rathakrishnan_2002]\] \[[Vinh and Tzeng 1993][research_vinh_tzeng_1993]\] \[[Vinh and Tzeng 1994][research_vinh_tzeng_1994]\] \[[Vinoth and Rathakrishnan 2005][research_vinoth_rathakrishnan_2005]\] \[[Viswanath and Brown 1982][research_viswanath_brown_1982]\] \[[Viswanath and Brown 1983][research_viswanath_brown_1983]\] \[[Viswanath and Brown 1982][research_viswanathpr_brownjl_1982]\] \[[Volpe and Jameson 1990][research_volpe_jameson_1990]\] \[[Vos and Farokhi 2015][research_vos_farokhi_2015_b]\] \[[Vos and Farokhi 2015][research_vos_farokhi_2015_c]\] \[[Vos and Farokhi 2015][research_vos_farokhi_2015_d]\] \[[Waggoner 1982][research_waggoner_1982]\] \[[Walchli and Langan 1999][research_walchli_langan_1999]\] \[[Wallace 1953][research_wallace_1953]\] \[[Wasserman 1952][research_wasserman_1952]\] \[[Wat and Sarohia 1981][research_wat_sarohia_1981]\] \[[Watanabe et al 2005][research_watanabe_maekawa_2005]\] \[[Wegener 1977][research_wegener_1977]\] \[[Weinacht 2014][research_weinacht_2014]\] \[[Wells 2017][research_wells_2017]\] \[[Wenzhong and Rongwei 2008][research_wenzhong_rongwei_2008]\] \[[Werner et al 2022][research_werner_schutte_2022]\] \[[Werner et al 2024][research_werner_henne_2024]\] \[[Wick et al 2017][research_wick_hooker_2017]\] \[[Wiggen et al 2018][research_wiggen_henne_2018]\] \[[Wilks 2006][research_wilks_2006]\] \[[Drake and Williams 1958][research_williams_drake_1948]\] \[[Williams and Hunt 1980][research_williams_hunt_1980]\] \[[Woodson and Dejarnette 1986][research_woodsonsh_dejarnettefr_1986]\] \[[Wright 1936][research_wright_1936]\] \[[Wu and Moulden 1976][research_wu_moulden_1976]\] \[[Xiong et al 2021][research_xiong_nguyen_2021]\] \[[Yang 1972][research_yang_1972]\] \[[Yaros 1978][research_yaros_1978]\] \[[Young et al 1988][research_young_oran_1988]\] \[[Young et al 1990][research_youngjr_popernackjr_1990]\] \[[Yue 2026][research_yue_2026]\] \[[Zartarian 1956][research_zartarian_1956]\] \[[Zartarian and Hsu 1955][research_zartarian_hsu_1955]\] \[[Zhang and Edwards 1990][research_zhang_edwards_1990]\] \[[Zhou et al 2025][research_zhou_cao_2025]\] \[[Zuccolo et al 2020][research_zuccolo_christie_2020]\]

## Where the Framing Breaks Down

Treating the X-1 through the drag-rise keystone is productive but incomplete in four ways.

The aircraft was scored publicly as a record attempt rather than as an instrument, and that framing distorted the programme. The Army Air Forces interest in a first supersonic flight and the NACA interest in a systematic data campaign were in tension, and the resolution favoured the demonstration \[[Hansen 1987][book_hansen_1987_engineer_in_charge]\]. A purely instrumental reading of the X-1 misses that the aircraft was also a political object, and the same tension recurs across the series.

The sound barrier framing was wrong. There was no barrier. There was a drag rise of finite magnitude, a stability change, and a control failure, and all three were tractable. The persistence of the barrier language in the popular record obscures that the programme's contribution was quantitative rather than a breach of a limit.

The keystone understates the contribution of the tail. If the research question is drag, the aircraft answered it. If the question is what blocked transonic flight in operational aircraft, the answer is control authority rather than thrust, and the all-moving tail was the fix. Reading the X-1 through drag alone gets the historical causation backwards.

The counterfactual is unresolved. The Miles M.52 was cancelled with a design that had an all-moving tail and a projected performance in the same class \[[Wikipedia Article on the Miles M.52][ref_miles_m52]\]. Whether a British programme would have reached the same result earlier is not answerable from the record, and the literature on the cancellation is partisan on both sides. This series states the dispute without adjudicating it.

## The Source Base

The primary record for this aircraft is unusually good and it is public. The NACA report series covers the acceptance tests, the flight loads, the pressure distributions, the lift and drag, and the dynamic stability, and it is available through the [NASA Technical Reports Server][ref_ntrs] and the [NASA History Office][ref_nasa_history]. That density is a consequence of the institutional arrangement described in the [series opener][related_post_a297_xplanes_framing], in which a NACA research component obliged the programme to publish. It is also why the X-1 receives a full treatment in this series while several later designations do not.

The secondary literature is large and of mixed reliability. The standard programme histories are [Hallion 1972][book_hallion_1972_supersonic_flight] and [Hallion 1981][book_hallion_1981_on_the_frontier], with the pilot culture in [Hallion 1981][book_hallion_1981_test_pilots] and the institutional account in [Gorn 2001][book_gorn_2001_expanding_envelope] and [Bilstein 1989][book_bilstein_1989_orders]. The aircraft-specific works are [Rotundo 1994][book_rotundo_1994_into_the_unknown] and [Pisano van der Linden and Winter 2006][book_pisano_et_al_2006], with the roster context in [Miller 2001][book_miller_2001_x_planes], [Jenkins Landis and Miller 2003][book_jenkins_landis_miller_2003], [Winchester 2005][book_winchester_2005_x_planes], and [Peebles 2014][book_peebles_2014_probing_the_sky]. The Langley side is [Hansen 1987][book_hansen_1987_engineer_in_charge] and [Hansen 2004][book_hansen_2004_bird_on_the_wing], with the tunnel programmes in [Chambers and Chambers 2008][book_chambers_2008_radical_wings]. [Wolfe 1979][book_wolfe_1979_right_stuff] and [Yeager and Janos 1985][book_yeager_janos_1985] are the popular and participant accounts respectively and should be read as such. [Gunston 1992][book_gunston_1992_faster_than_sound] and [Constant 1980][book_constant_1980] supply the wider propulsion and configuration context, [von Karman and Edson 1967][book_von_karman_edson_1967] and [Gorn 1992][book_gorn_1992_universal_man] the theoretical lineage, and [Anderson 1997][book_anderson_1997_history_aerodynamics] the history of the aerodynamics itself.

The engineering texts used for the relations above are [Anderson 2001][book_anderson_2001_fundamentals], [Anderson 2002][book_anderson_2002_modern_compressible], [Anderson 2012][book_anderson_2012_introduction_flight], [Anderson 2012][book_anderson_2012_aircraft_performance], [Shapiro 1953][book_shapiro_1953], [Liepmann and Roshko 1957][book_liepmann_roshko_1957], [Ashley and Landahl 1965][book_ashley_landahl_1965], [Kuchemann 1978][book_kuchemann_1978], [Kuethe and Chow 1998][book_kuethe_chow_1998], [Bertin and Cummings 2013][book_bertin_cummings_2013], [Schlichting and Gersten 2017][book_schlichting_gersten_2017], [White 2006][book_white_2006_viscous], and [Hurt 1965][book_hurt_1965]. The design methods are [Raymer 2018][book_raymer_2018], [Nicolai and Carichner 2010][book_nicolai_carichner_2010], [Torenbeek 1982][book_torenbeek_1982], [Roskam 1985][book_roskam_1985], [Stinton 2001][book_stinton_2001], and [Whitford 1987][book_whitford_1987]. The structures are [Bruhn 1973][book_bruhn_1973], [Niu 1988][book_niu_1988_airframe], and [Megson 2016][book_megson_2016]. The propulsion is [Sutton and Biblarz 2016][book_sutton_biblarz_2016], [Huzel and Huang 1992][book_huzel_huang_1992], and [Hill and Peterson 1991][book_hill_peterson_1991], with the sizing worked at model scale in [A118 Propulsion and Power Sizing][related_post_a118_propulsion_sizing]. The flight test discipline is [Kimberlin 2003][book_kimberlin_2003] and [Ward Strganac and Niewoehner 2006][book_ward_strganac_niewoehner_2006]. The epistemology is [Vincenti 1990][book_vincenti_1990], [Petroski 1985][book_petroski_1985], and [Ferguson 1992][book_ferguson_1992], and the organizational reading of risk is [Perrow 1984][book_perrow_1984] and [Vaughan 1996][book_vaughan_1996]. [Cover and Thomas 2006][book_cover_thomas_2006] supplies the information accounting.

Two collections deserve separate mention. [Donlan 1976][research_donlan_collected_1976] gathers the collected works of one of the engineers closest to the configuration decisions, and the 1949 [NACA transonic conference][research_transonic_conference_1949] records the state of the problem two years after the first supersonic flight, which is a useful check on how much the flight actually settled at the time.

**The survey rests on 4,845 research records drawn from Crossref, the NASA Technical Reports Server and the Defense Technical Information Center**, of which 1,232 are report primaries by the identifier rule set out under The Definition of Primary, being 25.4 percent. **Every one of the 166 research records cited in the prose is also in the survey, and 109 of those are primaries**, so the argument rests on the report literature far more heavily than the survey as a whole does.

### The Definition of Primary

**Primacy is a property of the document, and this survey derives it from the identifier.** A record is a report primary when it is a NASA Technical Reports Server record or carries a digital object identifier under the 10.21236 prefix, which Crossref registers for Defense Technical Information Center reports. Of the 1,232 primaries, 773 are NASA Technical Reports Server records and 459 are Defense Technical Information Center reports. **The rule counts the reports of the NACA as primaries because they are deposited in the NASA Technical Reports Server**, and it does not reach the conference and journal papers of the American Institute of Aeronautics and Astronautics, so 25.4 percent is a lower bound on how much of this survey is first-hand.

### Thin Subjects

**Six subjects that this article's derivations depend on have thin literatures.** Each count below is the number of research records in this survey whose title carries at least one of the listed terms, with a hyphen read as a space.

| Subject | Title terms counted | Records |
|---|---|---|
| the static-source position error and its calibration | position error, static source, static pressure error, static system error | 6 |
| the pitot probe above Mach one | pitot, together with supersonic or Mach | 20 |
| tunnel choking and blockage | choke, choked, choking, blockage | 10 |
| energy height and specific excess power | energy height, specific excess power, energy state, energy maneuverability, energy manoeuvrability, energy method | 9 |
| the pressure-fed engine and its tank pressurization | pressure fed, pressurant, pressurization, pressurisation, tank pressure, hoop stress | 12 |
| the learning curve of airframe cost | learning curve, unit cost, cost of airplanes, production cost | 1 |

**The static-source position error is the thinnest of the measurement subjects, and it is the one the determination of Mach 1.06 rested on.** Six titles name it, the oldest a paper of 1939 on its reduction, against twenty that concern the pitot probe in supersonic flow, many of them in tunnels, jets and rarefied flow rather than on an aircraft. **The article's argument that knowing the Mach number was the hardest measurement in the programme therefore rests on the NACA calibration reports it cites and on the relations it derives** rather than on a large literature.

**The pressure-fed engine has a literature, but none of its twelve titles concerns an aircraft.** Every one is a rocket, launch-vehicle or test-stand study, so the tank and pressurant arithmetic for the X-1 stands on the relations themselves and on the propulsion texts cited above.

**Tunnel choking and blockage is thin in a different sense.** Its titles concern blockage corrections and interference in tunnels that already work, with one on choked tunnel flow itself, because the slotted and perforated walls that ended choking moved the literature on to wall interference, which the ground-test cluster holds in volume.

**Energy height and specific excess power are a performance method rather than a research subject**, and the earliest of their nine titles is an energy-state approximation for supersonic aircraft from 1968. **The learning curve belongs to production economics rather than to high-speed flight, so its single record here is the paper of Wright**, which is the source the article's unit-cost arithmetic uses.

### What the Survey Admits

**A record is admitted only when a person reading its title finds it on this article's subject**, which here means the transonic aerodynamic, control, structural, measurement and propulsion literature of the aeroplane, found first by this subject's vocabulary and then read. Many words this subject depends on also name something else, and a record that shares only such a word is excluded. Supersonic flow and the bow shock also belong to astrophysics and the magnetosphere. Flutter is also a cardiac rhythm and a defect of tape recorders, and an elevator is also a lift in a building. Compressibility correction factors also belong to gas chromatography and coal porosimetry, position error to radar and emitter localisation, the pitot tube to industrial flow metering, and the word buffet to a meal and to a metaphor in policy writing. Transonic flow also passes through turbine cascades, fans, ejectors and cold-spray nozzles, and rocket propulsion also serves launch vehicles, weapons and escape systems. Launch vehicles and their fairings, entry capsules and orbiter heating, rotorcraft, flapping flight, supersonic combustion, space plasma shocks and wind engineering share this subject's physics or its instruments and are excluded as different subjects. Records that are parts of works or editorial events rather than works are excluded, meaning figure and table records, peer-review reports, erratum, correction, withdrawal and retraction notices, and journal front matter. A review of a book, a reference or definition entry, a notice such as an editorial, announcement or news item, and a second deposit of a document already in the survey are likewise not admitted, while an authored encyclopedia article and a textbook chapter are research works and are kept.

**Some records of doubtful relevance are kept.** Projectile, shell and store aerodynamics at transonic speed, transonic propellers, aircraft performance studies that bear on energy and excess power, the air-data systems of entry vehicles, the gliding aerodynamics of the Shuttle orbiter, air launch of rockets from aircraft, low-speed separation and Reynolds-number studies that the vocabulary admits, and hypersonic shock and boundary-layer work each share a method or a mechanism with this subject, so each is kept and a reader may weigh it accordingly.

**Every research title has been read for relevance, so the off-topic share that remains is a matter of reading judgement.** That reading leaves none of the 4,845 known to be off topic, which is a statement about titles rather than about the substance of each work, and a work whose title misdescribes it may remain.

## Epistemic State

Established historical fact includes the existence and sponsorship of the programme, the three airframes, the eight-percent and ten-percent wings on the first two aircraft, the XLR11 engine and its propellants, the air launch from a B-29, the all-moving stabilizer, the flight of 14 October 1947 at approximately Mach 1.06, the flight of 26 March 1948 at approximately Mach 1.45, the loss of the third airframe to a ground explosion, and the preservation of the first airframe by the National Air and Space Museum. These are documented in the NACA reports cited and in the standard secondary accounts.

Established engineering analysis includes every relation in the sizing sections. The Prandtl-Glauert transformation, the critical pressure coefficient, the Sears wave drag result, the Tsiolkovsky relation, the tail volume and control power relations, the hoop stress relation, and the Rayleigh supersonic pitot formula are standard results. The worked numbers are the author's own arithmetic applied to published inputs and are labelled as derived.

Inference includes the reading of the aircraft through a single drag-rise keystone, and the sizing narrative in which the engine was chosen to exceed a pessimistic unknown drag. The design record supports that reading and does not state it in those terms.

Weakly supported are the representative values used where the record does not give the actual figure. The incompressible peak pressure coefficients of negative 0.30 and negative 0.38 used to compute critical Mach numbers, the transonic drag peak near 0.05, the tail lift-curve slope, the tail efficiency, the elevator effectiveness parameter and its degraded value, the tank pressure and radius, and the allowable stress are all plausible values for the period rather than measured properties of this aircraft. The conclusions they support are qualitative, namely that thinner is better by a stated order of magnitude and that the elevator runs out of authority while the stabilizer does not. The decimals should not be quoted as X-1 data.

Contested is the priority question around the all-moving tail and the influence of the Miles M.52. The NACA flight research of 1945 and 1946 is documented and public. The transfer of British data to Bell is asserted by British accounts, among them [Wood 1975][book_wood_1975_project_cancelled] and the Miles chief aerodynamicist \[[Wikipedia Article on the Miles M.52][ref_miles_m52]\], while the American record attributes the adjustable stabilizer to the recommendation of Stack and Gilruth of the NACA \[[Hansen 1987][book_hansen_1987_engineer_in_charge]\]. This article establishes that a domestic basis existed and takes the question no further.

Unresolved in the sources consulted is the date of the first glide flight, given as 19 January 1946 by Hallion and as 25 January 1946 by the NASA inventory.

A note on temporal position. This article carries an editorial date of 2025-10-07 and is written from current knowledge, including contemporary literature published well after that date in the sources cited.

## Out of Scope

This article does not cover the X-1A, X-1B, X-1D, or X-1E in detail beyond the context given, since the second-generation aircraft differ enough in purpose to deserve separate treatment. It does not cover the Navy D-558 series flown alongside the X-1, which falls outside the X designation. It does not treat the biography of the pilots except where a decision bears on the engineering, and it does not attempt a resolution of the Miles M.52 dispute.

It does not derive the standard relations reused here from first principles, since the [series opener][related_post_a297_xplanes_framing] does that once for all seventy-two articles. Nor does it treat the [flight envelope][ref_flight_envelope] and [wing loading][ref_wing_loading] machinery, the [measurement uncertainty][ref_measurement_uncertainty] and [propagation][ref_propagation_of_uncertainty] apparatus, or the [standard atmosphere][ref_isa] beyond what the worked examples require.

It does not cover the parallel British and German transonic efforts except where the [Miles M.52][ref_miles_m52] bears on the tail decision, and it does not treat the [de Havilland DH 108][ref_de_havilland_swallow] loss of 1946 except as context for how dangerous the band was understood to be. It does not survey the [list of X-planes][ref_list_of_x_planes] or the wider category of [experimental aircraft][ref_experimental_aircraft], which the opener covers, and it does not treat [Edwards Air Force Base][ref_edwards_afb] or the [Armstrong Flight Research Center][ref_armstrong_frc] and its [predecessor organizations][ref_nasa_armstrong] as institutions in their own right.

It does not address [oblique shock][ref_oblique_shock] and [expansion fan][ref_expansion_fan] relations, which the aircraft never needed at its Mach numbers, nor [supersonic][ref_supersonic_speed] cruise as a design problem, nor the [rocket engine][ref_rocket_engine] as a general subject beyond the sizing above. The [transonic][ref_transonic] regime is the subject and the boundaries of that subject are drawn narrowly on purpose. Space policy context appears in [A90 Introduction to Space Studies][related_post_a90_intro_space_studies], configuration questions for large high-speed vehicles in [A106 Two-Stage Flying Delta Wing Vehicles][related_post_a106_two_stage_delta_wing], structural sizing at model scale in [A127 Structures and the Flight Envelope][related_post_a127_structures_flight_envelope], the computing and simulation infrastructure in [A237 Framing and the Co-Development Mechanism][related_post_a237_aerospace_framing] and [A241 Aerospace Simulation and Real-Time Systems][related_post_a241_aerospace_simulation], and the [airspeed][ref_airspeed_indicator] and [flight test][ref_flight_test] disciplines in the works cited above. The [National Air and Space Museum][ref_smithsonian_nasm] holds the airframe, and [NASA][ref_nasa] and the [NACA][ref_naca] hold the record.

## Conclusion

The Bell X-1 was an instrument built to measure a number that theory could not predict and that no ground facility could reach. The number is a transonic drag coefficient of roughly 0.05 against an aircraft capable of overcoming 0.173, which is to say the drag rise was real, finite, and considerably less formidable than the design allowance made for it.

The more consequential finding was not about drag at all. It was that pitch control failed before thrust did, that the failure mechanism was shock-induced separation destroying elevator effectiveness, and that an all-moving surface with no hinge line in the flow was immune to it. The arithmetic of the trim requirement shows the elevator needing eighteen degrees of deflection it did not have while the stabilizer needed under two. Those two figures separate an aircraft that can be flown through Mach one from one that cannot.

The aircraft also established the method. Incremental expansion, dedicated instrumentation, ground reduction between flights, and a fleet sized for attrition are all present here in their first mature form, and every article that follows in this series inherits them.

The next article takes the [Bell X-2][ref_bell_x2], which pushed the same approach into a thermal regime beyond any the X-1 flew in, and which killed a pilot demonstrating a coupling mode that static force testing could not see.

## References

### Books

- [Anderson 1997 A History of Aerodynamics][book_anderson_1997_history_aerodynamics]
- [Anderson 2001 Fundamentals of Aerodynamics][book_anderson_2001_fundamentals]
- [Anderson 2002 Modern Compressible Flow][book_anderson_2002_modern_compressible]
- [Anderson 2012 Aircraft Performance and Design][book_anderson_2012_aircraft_performance]
- [Anderson 2012 Introduction to Flight][book_anderson_2012_introduction_flight]
- [Ashley and Landahl 1965 Aerodynamics of Wings and Bodies][book_ashley_landahl_1965]
- [Baals and Corliss 1981 Wind Tunnels of NASA][book_baals_corliss_1981]
- [Barlow Rae and Pope 1999 Low-Speed Wind Tunnel Testing][book_barlow_rae_pope_1999]
- [Bertin and Cummings 2013 Aerodynamics for Engineers][book_bertin_cummings_2013]
- [Bevington and Robinson 2002 Data Reduction and Error Analysis][book_bevington_robinson_2002]
- [Bilstein 1989 Orders of Magnitude, A History of the NACA and NASA][book_bilstein_1989_orders]
- [Bisplinghoff Ashley and Halfman 1955 Aeroelasticity][book_bisplinghoff_ashley_halfman_1955]
- [Box Hunter and Hunter 2005 Statistics for Experimenters][book_box_hunter_hunter_2005]
- [Brown 2006 Wings on My Sleeve][book_brown_1988_wings_on_my_sleeve]
- [Bruhn 1973 Analysis and Design of Flight Vehicle Structures][book_bruhn_1973]
- [Chambers and Chambers 2008 Radical Wings and Wind Tunnels][book_chambers_2008_radical_wings]
- [Constant 1980 The Origins of the Turbojet Revolution][book_constant_1980]
- [Cover and Thomas 2006 Elements of Information Theory][book_cover_thomas_2006]
- [Etkin and Reid 1996 Dynamics of Flight, Stability and Control][book_etkin_reid_1996]
- [Ferguson 1992 Engineering and the Mind's Eye][book_ferguson_1992]
- [Fung 1955 An Introduction to the Theory of Aeroelasticity][book_fung_1955]
- [Gelman et al 2013 Bayesian Data Analysis][book_gelman_et_al_2013]
- [Gorn 1992 The Universal Man, Theodore von Karman][book_gorn_1992_universal_man]
- [Gorn 2001 Expanding the Envelope, Flight Research at NACA and NASA][book_gorn_2001_expanding_envelope]
- [Gunston 1992 Faster Than Sound][book_gunston_1992_faster_than_sound]
- [Hallion 1972 Supersonic Flight, Breaking the Sound Barrier and Beyond][book_hallion_1972_supersonic_flight]
- [Hallion 1981 On the Frontier, Flight Research at Dryden][book_hallion_1981_on_the_frontier]
- [Hallion 1981 Test Pilots, The Frontiersmen of Flight][book_hallion_1981_test_pilots]
- [Hansen 1987 Engineer in Charge][book_hansen_1987_engineer_in_charge]
- [Hansen 2004 The Bird Is on the Wing][book_hansen_2004_bird_on_the_wing]
- [Hill and Peterson 1991 Mechanics and Thermodynamics of Propulsion][book_hill_peterson_1991]
- [Hurt 1965 Aerodynamics for Naval Aviators][book_hurt_1965]
- [Huzel and Huang 1992 Modern Engineering for Design of Liquid-Propellant Rocket Engines][book_huzel_huang_1992]
- [Jenkins Landis and Miller 2003 American X-Vehicles, An Inventory X-1 to X-50][book_jenkins_landis_miller_2003]
- [Kimberlin 2003 Flight Testing of Fixed-Wing Aircraft][book_kimberlin_2003]
- [Kuchemann 1978 The Aerodynamic Design of Aircraft][book_kuchemann_1978]
- [Kuethe and Chow 1998 Foundations of Aerodynamics][book_kuethe_chow_1998]
- [Liepmann and Roshko 1957 Elements of Gasdynamics][book_liepmann_roshko_1957]
- [McRuer Ashkenas and Graham 1973 Aircraft Dynamics and Automatic Control][book_mcruer_ashkenas_graham_1973]
- [Megson 2016 Aircraft Structures for Engineering Students][book_megson_2016]
- [Miller 2001 The X-Planes, X-1 to X-45][book_miller_2001_x_planes]
- [Nelson 1998 Flight Stability and Automatic Control][book_nelson_1998]
- [Nicolai and Carichner 2010 Fundamentals of Aircraft and Airship Design][book_nicolai_carichner_2010]
- [Niu 1988 Airframe Structural Design][book_niu_1988_airframe]
- [Peebles 2014 Probing the Sky, Selected NACA Research Airplanes][book_peebles_2014_probing_the_sky]
- [Perrow 1984 Normal Accidents][book_perrow_1984]
- [Petroski 1985 To Engineer Is Human][book_petroski_1985]
- [Pisano van der Linden and Winter 2006 Chuck Yeager and the Bell X-1][book_pisano_et_al_2006]
- [Pope and Goin 1965 High-Speed Wind Tunnel Testing][book_pope_goin_1965]
- [Raymer 2018 Aircraft Design, A Conceptual Approach][book_raymer_2018]
- [Roskam 1985 Airplane Design][book_roskam_1985]
- [Rotundo 1994 Into the Unknown, The X-1 Story][book_rotundo_1994_into_the_unknown]
- [Schlichting and Gersten 2017 Boundary-Layer Theory][book_schlichting_gersten_2017]
- [Shapiro 1953 The Dynamics and Thermodynamics of Compressible Fluid Flow][book_shapiro_1953]
- [Stengel 2004 Flight Dynamics][book_stengel_2004]
- [Stinton 2001 The Design of the Aeroplane][book_stinton_2001]
- [Sutton and Biblarz 2016 Rocket Propulsion Elements][book_sutton_biblarz_2016]
- [Taylor 1997 An Introduction to Error Analysis][book_taylor_1997_error_analysis]
- [Torenbeek 1982 Synthesis of Subsonic Airplane Design][book_torenbeek_1982]
- [Vaughan 1996 The Challenger Launch Decision][book_vaughan_1996]
- [Vincenti 1990 What Engineers Know and How They Know It][book_vincenti_1990]
- [von Karman and Edson 1967 The Wind and Beyond][book_von_karman_edson_1967]
- [Ward Strganac and Niewoehner 2006 Introduction to Flight Test Engineering][book_ward_strganac_niewoehner_2006]
- [White 2006 Viscous Fluid Flow][book_white_2006_viscous]
- [Whitford 1987 Design for Air Combat][book_whitford_1987]
- [Winchester 2005 X-Planes and Prototypes][book_winchester_2005_x_planes]
- [Wolfe 1979 The Right Stuff][book_wolfe_1979_right_stuff]
- [Wood 1975 Project Cancelled][book_wood_1975_project_cancelled]
- [Yeager and Janos 1985 Yeager, An Autobiography][book_yeager_janos_1985]

### Reference

- [NACA Research Memorandum L51E08, X-1 Lift and Drag With the 8-Percent Wing][ref_naca_rm_l51e08]
- [NASA Armstrong Flight Research Center][ref_nasa_armstrong]
- [NASA History Office][ref_nasa_history]
- [NASA Technical Reports Server][ref_ntrs]
- [National Air and Space Museum Record for the Bell X-1][ref_nasm_x1]
- [Wikipedia Article on Aeroelasticity][ref_aeroelasticity]
- [Wikipedia Article on Airspeed][ref_airspeed_indicator]
- [Wikipedia Article on Bell Aircraft][ref_bell_aircraft]
- [Wikipedia Article on Chuck Yeager][ref_yeager]
- [Wikipedia Article on Cylinder Stress][ref_hoop_stress]
- [Wikipedia Article on Duralumin][ref_duralumin]
- [Wikipedia Article on Dynamic Pressure][ref_dynamic_pressure]
- [Wikipedia Article on Edwards Air Force Base][ref_edwards_afb]
- [Wikipedia Article on Ethanol][ref_ethanol_fuel]
- [Wikipedia Article on Experimental Aircraft][ref_experimental_aircraft]
- [Wikipedia Article on Flight Testing][ref_flight_test]
- [Wikipedia Article on Flow Separation][ref_flow_separation]
- [Wikipedia Article on Liquid Oxygen][ref_liquid_oxygen]
- [Wikipedia Article on Longitudinal Static Stability][ref_longitudinal_static_stability]
- [Wikipedia Article on Mach Tuck][ref_mach_tuck]
- [Wikipedia Article on Measurement Uncertainty][ref_measurement_uncertainty]
- [Wikipedia Article on NASA][ref_nasa]
- [Wikipedia Article on Propagation of Uncertainty][ref_propagation_of_uncertainty]
- [Wikipedia Article on Reaction Motors][ref_reaction_motors]
- [Wikipedia Article on Specific Impulse][ref_specific_impulse]
- [Wikipedia Article on Supersonic Speed][ref_supersonic_speed]
- [Wikipedia Article on Telemetry][ref_telemetry]
- [Wikipedia Article on the Accelerometer][ref_accelerometer]
- [Wikipedia Article on the Aerodynamic Center][ref_aerodynamic_center]
- [Wikipedia Article on the Area Rule][ref_whitcomb_area_rule]
- [Wikipedia Article on the Armstrong Flight Research Center][ref_armstrong_frc]
- [Wikipedia Article on the Aspect Ratio][ref_aspect_ratio]
- [Wikipedia Article on the Bell X-1][ref_bell_x1]
- [Wikipedia Article on the Bell X-2][ref_bell_x2]
- [Wikipedia Article on the Bell X-5][ref_bell_x5]
- [Wikipedia Article on the Boeing B-29 Superfortress][ref_b29]
- [Wikipedia Article on the Boundary Layer][ref_boundary_layer]
- [Wikipedia Article on the Control Surface][ref_hinge_moment]
- [Wikipedia Article on the Critical Mach Number][ref_critical_mach]
- [Wikipedia Article on the de Havilland DH 108][ref_de_havilland_swallow]
- [Wikipedia Article on the Douglas X-3 Stiletto][ref_douglas_x3]
- [Wikipedia Article on the Drag Coefficient][ref_drag_coefficient]
- [Wikipedia Article on the Drag Divergence Mach Number][ref_drag_divergence]
- [Wikipedia Article on the Drag Polar][ref_drag_polar]
- [Wikipedia Article on the Elevator][ref_elevator_aircraft]
- [Wikipedia Article on the Factor of Safety][ref_factor_of_safety]
- [Wikipedia Article on the Flight Envelope][ref_flight_envelope]
- [Wikipedia Article on the International Standard Atmosphere][ref_isa]
- [Wikipedia Article on the Lift Coefficient][ref_lift_coefficient]
- [Wikipedia Article on the Load Factor][ref_load_factor]
- [Wikipedia Article on the Lockheed F-104 Starfighter][ref_f104]
- [Wikipedia Article on the Lockheed P-38 Lightning][ref_p38]
- [Wikipedia Article on the Mach Number][ref_mach_number]
- [Wikipedia Article on the Miles M.52][ref_miles_m52]
- [Wikipedia Article on the NACA Airfoil Series][ref_naca_airfoil]
- [Wikipedia Article on the National Advisory Committee for Aeronautics][ref_naca]
- [Wikipedia Article on the National Air and Space Museum][ref_smithsonian_nasm]
- [Wikipedia Article on the North American F-100 Super Sabre][ref_f100]
- [Wikipedia Article on the North American F-86 Sabre][ref_f86]
- [Wikipedia Article on the North American X-15][ref_na_x15]
- [Wikipedia Article on the Northrop X-4 Bantam][ref_northrop_x4]
- [Wikipedia Article on the Oblique Shock][ref_oblique_shock]
- [Wikipedia Article on the Pitot Tube][ref_pitot_tube]
- [Wikipedia Article on the Pitot-Static System][ref_position_error]
- [Wikipedia Article on the Prandtl-Glauert Singularity][ref_prandtl_glauert_singularity]
- [Wikipedia Article on the Prandtl-Glauert Transformation][ref_prandtl_glauert]
- [Wikipedia Article on the Prandtl-Meyer Expansion Fan][ref_expansion_fan]
- [Wikipedia Article on the Pressure-Fed Engine][ref_pressure_fed]
- [Wikipedia Article on the Reaction Motors XLR11][ref_xlr11]
- [Wikipedia Article on the Reynolds Number][ref_reynolds_number]
- [Wikipedia Article on the Rocket Engine][ref_rocket_engine]
- [Wikipedia Article on the Sears-Haack Body][ref_sears_haack]
- [Wikipedia Article on the Shock Wave][ref_shock_wave]
- [Wikipedia Article on the Sound Barrier][ref_sound_barrier]
- [Wikipedia Article on the Speed of Sound][ref_speed_of_sound]
- [Wikipedia Article on the Stabilator][ref_stabilator]
- [Wikipedia Article on the Strain Gauge][ref_strain_gauge]
- [Wikipedia Article on the Swept Wing][ref_swept_wing]
- [Wikipedia Article on the Tailplane][ref_tailplane]
- [Wikipedia Article on the Trim Tab][ref_trim_tab]
- [Wikipedia Article on the Tsiolkovsky Rocket Equation][ref_tsiolkovsky]
- [Wikipedia Article on the U.S. Standard Atmosphere][ref_us_standard_atmosphere]
- [Wikipedia Article on the Wind Tunnel][ref_wind_tunnel]
- [Wikipedia Article on Transonic Flow][ref_transonic]
- [Wikipedia Article on Wave Drag][ref_wave_drag]
- [Wikipedia Article on Wing Loading][ref_wing_loading]
- [Wikipedia List of X-1 Flights][ref_list_of_x1_flights]
- [Wikipedia List of X-Planes][ref_list_of_x_planes]
- [Wikipedia Section on Buffeting][ref_buffeting]
- [Wikipedia Section on the Bell X-1 Variants][ref_bell_x1a]
- [Wikipedia Section on the History of Muroc and Edwards][ref_muroc]
- [Wikipedia Section on the Normal Shock][ref_normal_shock]
- [Wikipedia Section on the Pitot Tube in Supersonic Flow][ref_rayleigh_pitot]

### Research

- [A Comparison of Different Approaches for Predicting Transonic Buffet Onset on Infinite Swept Wings 2022][research_a_comparison_2022]
- [A computational procedure for transonic airfoil flow including a special solution for shock boundary layer interaction 1980][research_a_computational_1980]
- [A computational study on shock-wave/turbulent-boundary-layer interaction with two-equation turbulence models 1994][research_a_computational_1994]
- [A New Steady Approach to Predict the Transonic Buffet Onset 2006][research_a_new_2006]
- [A predictive controller for the Mach number in a transonic wind tunnel 1991][research_a_predictive_1991]
- [A self-adaptive computational method applied to transonic turbulent projectile aerodynamics 1989][research_a_self_adaptive_1989]
- [A Series of Airfoils Designed by Transonic Drag Minimization for Gates Learjet Aircraft 1982][research_a_series_1982]
- [A-7 Transonic Wing Designs 1982][research_a_7_transonic_1982]
- [Abada et al 2024][research_abada_kbab_2024]
- [Abbott and Land 1957][research_allmovable_flutter_1957]
- [Abdel-Fattah and Link 1992][research_abdelfattah_link_1992]
- [Abed et al 2024][research_abed_alhamadani_2024]
- [Abele and Sanlorenzo 1975][research_abele_sanlorenzo_1975]
- [Abele et al 1973][research_abele_ruger_1973]
- [Abichandani and Rosenberg 1952][research_abichandani_rosenberg_1952]
- [Abraham-Doman and Merrett 2014][research_abrahamdoman_merrett_2014]
- [Abu-Mostafa and Reed 1984][research_abumostafaas_reedtd_1984]
- [Ackeret 1925][research_ackeret_1925]
- [Adamczyk 1973][research_adamczyk_1973]
- [Adamov and Chasovnikov 2025][research_adamov_chasovnikov_2025]
- [Adams][research_adams]
- [Adams and John C. 1968][research_adams_johnc_1968]
- [Adams and Rubin 1958][research_adams_rubin_1958]
- [Adams and Silsby 1947][research_adamsricharde_silsbynormans_1947]
- [Adams et al 1983][research_adams_thompson_1983]
- [Adams et al 1983][research_adams_thompson_1983_b]
- [Adamson 1976][research_adamson_1976]
- [Adamson and Feo 1975][research_adamsonjr_feo_1975]
- [Adamson et al 1980][research_adamson_jr_1980]
- [Adaptive Transonic Aeroservoelasticity 2016][research_adaptive_transonic_2016]
- [Adcock et al 1975][research_adcock_kilgore_1975]
- [Adhikary and Narayanaswamy 2026][research_adhikary_narayanaswamy_2026]
- [Adiwidodo and Wijaya 2022][research_adiwidodo_wijaya_2022]
- [Advanced Ducted Propulsor In-Flight Thrust Determination][research_advanced_ducted]
- [Advanced Fuel Research Inc East Hartford Ct 1957][research_advancedfuelresearchinceasthartfordct_1957]
- [Advanced technology airfoil research, volume 1, part 2 1978][research_advanced_technology_1978]
- [Aerodynamic and Landing Measurements Obtained During the First Powered Flight of the North American X-15 Research Airplane 1960][research_aerodynamic_and_1960]
- [Aerodynamic and Static Aeroelastic Analysis of a Transonic Wing using Hybrid Unstructured Flow Solver 2014][research_aerodynamic_and_2014]
- [Aerodynamic Forces on Aircraft 1995][research_aerodynamic_forces_1995]
- [Aeroelasticity Problems in Compressible Subsonic and Transonic Flow 2010][research_aeroelasticity_problems_2010]
- [Afkhami and Alighanbari 2007][research_afkhami_alighanbari_2007]
- [Afsar et al 2019][research_afsar_sescu_2019]
- [Agarwal and Deese 1983][research_agarwal_deese_1983]
- [Agarwal and Deese 1983][research_agarwal_deese_1983_b]
- [Agarwal et al 1988][research_agarwal_deese_1988]
- [Agarwal et al 1992][research_agarwal_miley_1992]
- [Ageev and Pavlenko 2016][research_ageev_pavlenko_2016]
- [Agopian 1974][research_agopiankg_1974]
- [Agostini et al 2012][research_agostini_larcheveque_2012]
- [Agostini et al 2013][research_agostini_larcheveque_2013]
- [Agrawal et al 1990][research_agrawal_lowrie_1990]
- [Agrawal et al 1991][research_agrawal_kinard_1991]
- [Agrell and Elmeland 1984][research_agrell_elmeland_1984]
- [Agrell and Elmeland 1985][research_agrell_elmeland_1985]
- [Agrell et al 1987][research_agrell_pettersson_1987]
- [Aguwa and Chen 2026][research_aguwa_chen_2026]
- [Ahlefeldt 2017][research_ahlefeldt_2017]
- [Ahmed and Selvarajan 1991][research_ahmed_selvarajan_1991]
- [Ahmed et al 1989][research_ahmed_wentz_1989]
- [Ahn and Drela 1998][research_ahn_drela_1998]
- [Ahn et al 1999][research_ahn_yee_1999]
- [Ahn et al 2001][research_ahn_kim_2001]
- [Ahn et al 2001][research_ahn_kim_2001_b]
- [Ai et al 2023][research_ai_bai_2023]
- [Ai et al 2023][research_ai_bai_2023_b]
- [Ai et al 2024][research_ai_bai_2024]
- [Ai et al 2026][research_ai_bai_2026]
- [Aidala 1985][research_aidala_1985]
- [Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974]
- [Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974_b]
- [Air Force Flight Test Center Edwards Afb Ca 2002][research_airforceflighttestcenteredwardsafbca_2002]
- [Air Force Test Pilot School Edwards Afb Ca 1962][research_airforcetestpilotschooledwardsafbca_1962]
- [Air Force Test Pilot School Edwards Afb Ca 1962][research_airforcetestpilotschooledwardsafbca_1962_b]
- [Air Force Test Pilot School Edwards Afb Ca 1962][research_airforcetestpilotschooledwardsafbca_1962_c]
- [Air Force Test Pilot School Edwards Afb Ca 1967][research_airforcetestpilotschooledwardsafbca_1967]
- [Air Force Test Pilot School Edwards Afb Ca 1967][research_airforcetestpilotschooledwardsafbca_1967_b]
- [Air Force Test Pilot School Edwards Afb Ca 1979][research_airforcetestpilotschooledwardsafbca_1979]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_b]
- [Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991]
- [Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991_b]
- [Air Force Test Pilot School Edwards Afb Ca 1992][research_airforcetestpilotschooledwardsafbca_1992]
- [Air Force Test Pilot School Edwards Afb Ca 1992][research_airforcetestpilotschooledwardsafbca_1992_b]
- [Aircraft and Flight Test Instrumentation 2021][research_aircraft_and_2021]
- [Aircraft Performance 2026][research_aircraft_performance_2026]
- [Aircraft Stability Characteristics in a Single Horizontal Tail Failure and Evaluation of Countermeasures for Safe Landing 2021][research_aircraft_stability_2021]
- [Aircraft Stability Derivatives 1998][research_aircraft_stability_1998]
- [Airfoil Integrals 2001][research_airfoil_integrals_2001]
- [Airfoil static-pressure thrust - Flight-test verification 1990][research_airfoil_static_pressure_1990]
- [Airplane and rocket flight 1990][research_airplane_and_1990]
- [Airplane Trim 2012][research_airplane_trim_2012]
- [Airplane Trim 2022][research_airplane_trim_2022]
- [Airspeed Calibration 2021][research_airspeed_calibration_2021]
- [Airspeed Indicator Pitot Static][research_airspeed_indicator]
- [Airspeed Indicator Pitot Static Reciprocating Engine Powered Aircraft][research_airspeed_indicator_b]
- [Airspeed Vs Flight Path Angle Performance Method For Powered-Lift Aircraft 2003][research_airspeed_vs_2003]
- [Akmese et al 2009][research_akmese_comert_2009]
- [Al-Saadi 1993][research_alsaadijassima_1993]
- [Al-Saadi and Dejarnette 1992][research_alsaadijassima_dejarnettefredr_1992]
- [Alam and Pant 2019][research_alam_pant_2019]
- [Albone et al 1976][research_albone_hall_1976]
- [Albrecht et al 2022][research_albrecht_olson_2022]
- [Alden and Schindel 1952][research_alden_schindel_1952]
- [Alder 2014][research_alder_2014]
- [Alder 2015][research_alder_2015]
- [Alexander et al 1973][research_alexander_griffin_1973]
- [Alexander et al 1975][research_alexander_griffin_1975]
- [Alexander et al 2005][research_alexandermichaelg_andersscottg_2005]
- [Alguacil et al 2023][research_alguacil_becherucci_2023]
- [Alhussan 2007][research_alhussan_2007]
- [Allan and Owens 2006][research_allan_owens_2006]
- [Allen 1954][research_allen_1954]
- [Allen et al 2005][research_allen_lizotte_2005]
- [Allison and Mineck 1993][research_allisondenniso_mineckraymonde_1993]
- [Allison and Mineck 1996][research_allisondenniso_mineckraymonde_1996]
- [Almohammadi 2022][research_almohammadi_2022]
- [Alshabu et al 2007][research_alshabu_hermes_2007]
- [Alternative Methods for Modeling Unsteady Transonic Flows 1989][research_alternative_methods_1989]
- [Altman 1965][research_altman_1965]
- [Altstatt 1977][research_altstatt_1977]
- [Alvi 2005][research_alvi_2005]
- [Ameduri et al 2005][research_ameduri_concilio_2005]
- [Amendola et al 2018][research_amendola_dimino_2018]
- [Amiet 1974][research_amiet_1974]
- [Amin et al 2016][research_amin_shah_2016]
- [Amouyal and Weihs 2015][research_amouyal_weihs_2015]
- [Amouyal and Weihs 2016][research_amouyal_weihs_2016]
- [Amprikidis et al 2003][research_amprikidis_cooper_2003]
- [An and Williams 2025][research_an_williams_2025]
- [An and Williams 2026][research_an_williams_2026]
- [An evaluation of sailplane drag coefficient parameters from flight test results 1974][research_an_evaluation_1974]
- [An experimental and computational investigation of a swept-wing flowat subsonic speeds 1978][research_an_experimental_1978]
- [An Experimental Study on Transonic Airfoil Flows in a Shock Tube 2006][research_an_experimental_2006]
- [Anatolievich and Andreevich 2020][research_anatolievich_andreevich_2020]
- [Anders and Watson 1985][research_anders_watson_1985]
- [Anders et al 1998][research_andersjb_andersonwk_1998]
- [Anders et al 1999][research_anders_anderson_1999]
- [Andersen et al 1997][research_andersen_kolonay_1997]
- [Andersen et al 1998][research_andersen_kolonay_1998]
- [Andersen et al 1998][research_andersen_kolonay_1998_b]
- [Anderson 1984][research_anderson_1984]
- [Anderson and Averett 1972][research_anderson_averett_1972]
- [Anderson and Benson 1983][research_andersonbh_bensontj_1983]
- [Anderson and Bray 1951][research_andersonsethb_brayrichards_1951]
- [Anderson and Bray 1955][research_pitchup_evaluation_1955]
- [Anderson and Vincent 1985][research_anderson_vincent_1985]
- [Anderson et al 1970][research_anderson_anderson_1970]
- [Anderson et al 1983][research_anderson_vincent_1983]
- [Andrew and Stenton 1967][research_andrew_stenton_1967]
- [André et al 2013][research_andre_castelain_2013]
- [Ang 1987][research_ang_1987]
- [Angle and Lundstrom 1948][research_angleellwyne_lundstromreginaldr_1948]
- [Anhichem et al 2025][research_anhichem_timme_2025]
- [Ankenbruck 1954][research_ankenbruckhermano_1954]
- [Ankenbruck 1954][research_d558_handling_1954]
- [Ankenbruck and Dahlen 1953][research_ankenbruckhermano_dahlentheodoree_1953]
- [Ankenbruck and Wolowicz 1954][research_ankenbruckhermano_wolowiczchesterh_1954]
- [Ansell et al 2010][research_ansell_bragg_2010]
- [Ansell et al 2011][research_ansell_bragg_2011]
- [Ansell et al 2011][research_ansell_bragg_2011_b]
- [Ansell et al 2013][research_ansell_kerho_2013]
- [Anyiwo and Bushnell 1982][research_anyiwojc_bushnelldm_1982]
- [Anyoji et al 2015][research_anyoji_numata_2015]
- [Appendix C Aircraft Performance Summary 1997][research_appendix_c_1997]
- [Appendix F Flight Test for Drag Parameters 1999][research_appendix_f_1999]
- [Appich 1978][research_appichjr_1978]
- [Application of a Shock-Turbulent Boundary-Layer Interaction Theory in Transonic Flowfield Analysis 1982][research_application_of_1982_b]
- [Application of Computational Methods to Transonic Wing Design 1982][research_application_of_1982]
- [Applied Computational Transonics-Capabilities and Limitations 1982][research_applied_computational_1982]
- [Ar 2013][research_ar_2013]
- [Archambaud et al 2004][research_archambaud_louis_2004]
- [Ardema and Williams 1972][research_ardema_williams_1972]
- [Arguchintseva and Pilyugin 2008][research_arguchintseva_pilyugin_2008]
- [Arif et al 2023][research_arif_singh_2023]
- [Arizono et al 2008][research_arizono_kheirandish_2008]
- [Armenta and Takahashi 2021][research_armenta_takahashi_2021]
- [Armstrong 1977][research_armstrong_1977]
- [Armstrong et al 1952][research_armstrong_holt_1952]
- [Armstrong et al 2006][research_armstrong_lindberg_2006]
- [Army War Coll Carlisle Barracks Pa 1952][research_armywarcollcarlislebarrackspa_1952]
- [Arnaiz 1975][research_arnaiz_1975]
- [Arnaiz 1977][research_arnaizhh_1977]
- [Arnaiz et al 1980][research_arnaizhh_petersonjbjr_1980]
- [Arnault et al 2016][research_arnault_dandois_2016]
- [Arney et al 1963][research_arney_gd_1963]
- [Arney et al 1964][research_arney_georged_1964]
- [Arnold 1942][research_arnold_1942]
- [Arnold and Thiele 1993][research_arnold_thiele_1993]
- [Arnold and Thiele 1994][research_arnold_thiele_1994]
- [Arthur 1984][research_arthur_1984]
- [Arunajatesan et al 2008][research_arunajatesan_cattafesta_2008]
- [Asada and Kawai 2024][research_asada_kawai_2024]
- [Asadi and Farsadi 2020][research_asadi_farsadi_2020]
- [Asai 2022][research_asai_2022]
- [Asai et al 1996][research_asai_kanda_1996]
- [Asai et al 1997][research_asai_kanda_1997]
- [Asher et al 1957][research_asher_martuccelli_1957]
- [Ashley 1979][research_ashley_1979]
- [Ashley 1980][research_ashley_1980]
- [Asim et al 2022][research_asim_masud_2022]
- [Askari and Soltani 2019][research_askari_soltani_2019]
- [Asymptotic methods for the prediction of transonic wind tunnel wall interference 1991][research_asymptotic_methods_1991]
- [Atifatul Ismah Ismail 2021][research_atifatulismahismail_2021]
- [Atkinson 2016][research_atkinson_2016]
- [Atta and Nayfeh 1978][research_atta_nayfeh_1978]
- [Atta and Vadyak 1983][research_attaeh_vadyakj_1983]
- [Atthar 2026][research_atthar_2026]
- [Aul'chenko 2006][research_aulchenko_2006]
- [Aul'chenko and Zamuraev 2012][research_aulchenko_zamuraev_2012]
- [Aul'chenko et al 1985][research_aulchenko_latypov_1985]
- [Aul'chenko et al 2010][research_aulchenko_zamuraev_2010]
- [Aul'chenko et al 2014][research_aulchenko_zamuraev_2014]
- [Aulehla 1992][research_aulehla_1992]
- [Auls'chenko et al 2006][research_aulschenko_zamuraev_2006]
- [Austin 1966][research_austin_1966]
- [Austin and Van Nostrand 1995][research_austin_vannostrand_1995]
- [Austin et al 1997][research_austin_siclari_1997]
- [Avkhadiev and Elizarov 2001][research_avkhadiev_elizarov_2001]
- [Avkhadiev et al 1992][research_avkhadiev_elizarov_1992]
- [Avkhadiev et al 1995][research_avkhadiev_elizarov_1995]
- [Axelson 1947][research_axelsonja_1947]
- [Axelson 1975][research_axelson_1975]
- [Axelson 1977][research_axelson_1977]
- [Ayok 2026][research_ayok_2026]
- [Azarova 2022][research_azarova_2022]
- [Azzazy et al 1987][research_azzazy_modarress_1987]
- [Azzazy et al 1989][research_azzazy_modarress_1989]
- [Babinsky 2007][research_babinsky_2007]
- [Babinsky 2014][research_babinsky_2014]
- [Babinsky and Délery 2011][research_babinsky_delery_2011]
- [Babinsky and Ogawa 2006][research_babinsky_ogawa_2006]
- [Babister 1980][research_babister_1980]
- [Bacci and Saddington 2022][research_bacci_saddington_2022]
- [Bacci and Saddington 2026][research_bacci_saddington_2026_b]
- [Bacci et al 2026][research_bacci_saddington_2026]
- [Bachaio 1983][research_bachaio_1983]
- [Back 1970][research_back_1970]
- [Baer 1966][research_baer_1966]
- [Baer-Riedhart 1981][research_baerriedhart_1981]
- [Bahi et al 1983][research_bahi_ross_1983]
- [Bai et al 2015][research_bai_li_2015]
- [Bai et al 2017][research_bai_qian_2017]
- [Bai et al 2022][research_bai_cao_2022]
- [Bailey and Ballhaus][research_bailey_ballhaus]
- [Bailey and Ballhaus 1973][research_baileyfr_ballhauswf_1973]
- [Bailey and Miller 1981][research_bailey_miller_1981]
- [Bailey and Starr 1976][research_bailey_starr_1976]
- [Bailey et al 1996][research_bailey_knoedler_1996]
- [Baker 1953][research_bakerthomasf_1953]
- [Baker 1953][research_bakerthomasf_1953_b]
- [Baker 1954][research_bakerthomasf_1954]
- [Baker and Forsey 1981][research_baker_forsey_1981]
- [Baker and Forsey 1983][research_baker_forsey_1983]
- [Baker and Johnson 1955][research_bakerthomasf_johnsonwallacee_1955]
- [Baker et al 1961][research_baker_schuman_1961]
- [Balakrishna 1989][research_balakrishnas_1989]
- [Balakrishna and Niranjana 1987][research_balakrishna_niranjana_1987]
- [Balakrishnan 2004][research_balakrishnan_2004]
- [Balakumar 2018][research_balakumar_2018]
- [Balakumar and Iyer][research_ponnampalambalakumar_prahladhiyer]
- [Balakumar et al][research_pbalakumar_prahladhiyer]
- [Balakumar et al 2023][research_ponnampalambalakumar_prahladhiyer_2023]
- [Balasubramanian et al 2017][research_balasubramanian_anandhanarayanan_2017]
- [Ball 1978][research_ball_1978]
- [Ball 1979][research_ball_1979]
- [Balla et al 2014][research_balla_rhode_2014]
- [Balleur et al 2002][research_balleur_girodrouxlavigne_2002]
- [Balsa and Goldstein 1990][research_balsa_goldstein_1990]
- [Balusamy et al 2024][research_balusamy_a_2024]
- [Bamber 1961][research_bamber_1961]
- [Banavara and Dimitrov 2014][research_banavara_dimitrov_2014]
- [Banner et al 1958][research_transition_flight_1958]
- [Barakos and Drikakis 1999][research_barakos_drikakis_1999]
- [Barbut et al 2010][research_barbut_braza_2010]
- [Bardina et al 1988][research_bardina_lombard_1988]
- [Bare et al 1987][research_bare_reubush_1987]
- [Barnard 1969][research_barnard_1969]
- [Barnes 1965][research_barnes_og_1965]
- [Barnes and Visbal 2017][research_barnes_visbal_2017]
- [Barnes and Visbal 2018][research_barnes_visbal_2018]
- [Barnes and Visbal 2020][research_barnes_visbal_2020]
- [Barnes and Visbal 2021][research_barnes_visbal_2021]
- [Barnes and Visbal 2023][research_barnes_visbal_2023]
- [Barnhart et al 1988][research_barnhart_greber_1988]
- [Barnwell 1974][research_transonic_wingbody_1974]
- [Barnwell 1975][research_barnwellrw_1975]
- [Barnwell 1976][research_barnwellrw_1976]
- [Barnwell 1976][research_barnwellrw_1976_b]
- [Barnwell et al 1979][research_barnwellrw_sewallwg_1979]
- [Barnwell et al 1986][research_barnwell_edwards_1986]
- [Baron 1954][research_baron_1954]
- [Barrett-Gonzalez and Wolf 2021][research_barrett_gonzalez_2021]
- [Barrows 2006][research_barrowsdannya_2006]
- [Bartasevicius and Hornung 2023][research_bartasevicius_hornung_2023]
- [Barter and Dolling 1995][research_barterjohnw_dollingdavids_1995]
- [Barter and Dolling 1995][research_barterjohnw_dollingdavids_1995_b]
- [Barter and Dolling 1996][research_barter_dolling_1996]
- [Bartlett 1975][research_bartlettdw_1975]
- [Bartlett and Harris 1974][research_bartlettdw_harriscd_1974]
- [Bartlett and Sangiorgio 1975][research_bartlettdw_sangiorgiog_1975]
- [Bartlett et al 1973][research_bartlettdw_harriscd_1973]
- [Barufaldi et al 2019][research_barufaldi_morales_2019]
- [Bashkirov and Ogorodnikov 2018][research_bashkirov_ogorodnikov_2018]
- [Basic Equations for Unsteady Transonic Flow 1989][research_basic_equations_1989]
- [Baskaran and Muruganandam 2022][research_baskaran_muruganandam_2022]
- [Basu and Niyogi 1987][research_basu_niyogi_1987]
- [Batill et al 1982][research_batill_nelson_1982]
- [Batina 1986][research_batina_1986]
- [Batina 1986][research_batina_1986_b]
- [Batina 1986][research_batina_1986_c]
- [Batina 1987][research_batina_1987]
- [Batina 1988][research_batina_1988]
- [Batina 1988][research_batina_1988_b]
- [Batina 1988][research_batina_1988_c]
- [Batina 1989][research_batina_1989]
- [Batina 1989][research_batina_1989_b]
- [Batina and Yang 1985][research_batina_yang_1985]
- [Batina et al 1989][research_batina_seidel_1989]
- [Bauer and Garabedian 1973][research_bauerf_garabedianp_1973]
- [Bauer and Hernandez 1988][research_bauer_hernandez_1988]
- [Bauer et al 1977][research_bauer_garabedian_1977]
- [Bauer et al 1983][research_bauerf_garabedianp_1983]
- [Bauer et al 2016][research_bauer_grund_2016]
- [Bauer et al 2026][research_bauer_garabedian_2026]
- [Bawa and Michalski 2025][research_bawa_michalski_2025]
- [Baxter 1947][research_baxter_1947]
- [Bazgir and Takovitskii 2018][research_bazgir_takovitskii_2018]
- [Bazyma and Rashkovan 2003][research_bazyma_rashkovan_2003]
- [Bean and Lee 1994][research_bean_lee_1994]
- [Bean and Lee 1995][research_bean_lee_1995]
- [Bean and Wood 1996][research_bean_wood_1996]
- [Beeler 1961][research_x15_conference_1958]
- [Beeler and Mayer 1948][research_xs1_loads_1948]
- [Beeler et al 1956][research_beeler_1956]
- [Begnini et al 2018][research_begnini_bones_2018]
- [Bekemeyer and Timme 2017][research_bekemeyer_timme_2017]
- [Belesiotis-Kataras and Timme 2020][research_belesiotiskataras_timme_2020]
- [Belesiotis-Kataras and Timme 2021][research_belesiotiskataras_timme_2021]
- [Belisle et al 2010][research_belisle_neale_2010]
- [Belisle et al 2012][research_belisle_roberts_2012]
- [Bell 1963][research_bell_1963]
- [Belligoli et al 2019][research_belligoli_dwight_2019]
- [Belligoli et al 2019][research_belligoli_dwight_2019_b]
- [Belligoli et al 2021][research_belligoli_dwight_2021]
- [Bellman 1959][research_transonic_summary_1959]
- [Ben-Gida 2025][research_bengida_2025]
- [Benay and Pot 1986][research_benay_pot_1986]
- [Benay et al 1989][research_benay_coet_1989]
- [Benay et al 2001][research_benay_berthouze_2001]
- [Bendiksen 1987][research_bendiksen_1987]
- [Bendiksen 1992][research_bendiksen_1992]
- [Bendiksen 1993][research_bendiksen_1993]
- [Bendiksen 1994][research_bendiksen_1994]
- [Bendiksen 1998][research_bendiksen_1998]
- [Bendiksen 1999][research_bendiksen_1999]
- [Bendiksen 2004][research_bendiksen_2004]
- [Bendiksen 2004][research_bendiksen_2004_b]
- [Bendiksen 2006][research_bendiksen_2006]
- [Bendiksen 2007][research_bendiksen_2007]
- [Bendiksen 2008][research_bendiksen_2008]
- [Bendiksen 2009][research_bendiksen_2009]
- [Bendiksen 2009][research_bendiksen_2009_b]
- [Bendiksen 2011][research_bendiksen_2011]
- [Bendiksen 2013][research_bendiksen_2013]
- [Bendiksen 2015][research_bendiksen_2015]
- [Bendiksen and Davis 1995][research_bendiksen_davis_1995]
- [Bendiksen and Hwang 1996][research_bendiksen_hwang_1996]
- [Bendiksen and Kousen 1989][research_bendiksenoddvaro_kousenkennetha_1989]
- [Bendiksen et al 1997][research_bendiksen_hwang_1997]
- [Benedikt 1953][research_benedikt_1953]
- [Benepe et al 1974][research_buffet_response_1974]
- [Benepe et al 1975][research_benepe_cunninghamjr_1975]
- [Benepe et al 1978][research_benepedb_cunninghamamjr_1978]
- [Benepe et al 1978][research_buffet_response_1978]
- [Bengelink et al 1986][research_bengelink_doerzbacher_1986]
- [Benhachmi et al 1989][research_benhachmidriss_greberisaac_1989]
- [Bennett and Abel 1981][research_bennett_abel_1981]
- [Bennett and Batina 1989][research_bennettrobertm_batinajohnt_1989]
- [Bennett et al 1987][research_bennett_bland_1987]
- [Bennett et al 1988][research_bennett_batina_1988]
- [Bennett et al 1989][research_bennett_batina_1989]
- [Bennett et al 1991][research_bennett_dansberry_1991]
- [Bennett et al 1993][research_bennett_dansberry_1993]
- [Benoit and Legrain 1987][research_benoit_legrain_1987]
- [Benyamen et al 2020][research_benyamen_mckinnis_2020]
- [Beran and Morton 1997][research_beran_morton_1997]
- [Bergen and Arnold 1940][research_bergen_arnold_1940]
- [Bergier][research_bergier]
- [Bergman 1948][research_bergman_1948]
- [Bergman 1949][research_bergman_1949]
- [Berkowitz et al 1977][research_berkowitz_kyriss_1977]
- [Bernardini and Pirozzoli 2011][research_bernardini_pirozzoli_2011]
- [Berndt 1964][research_berndt_1964]
- [Berndt 1976][research_berndt_1976]
- [Bernstein 1953][research_bernstein_1953]
- [Bernstein 1997][research_bernstein_1997]
- [Berry 1986][research_berrysa_1986]
- [Berry and Gilyard 1973][research_berry_gilyard_1973]
- [Berry et al 1985][research_berry_yang_1985]
- [Berry et al 2016][research_blt_shuttle_2016]
- [Bertelrud 1980][research_bertelrud_1980]
- [Bertelrud 1981][research_bertelrud_1981]
- [Bertelrud 1989][research_bertelrudarild_1989]
- [Bertelrud and Graves 1994][research_bertelrud_graves_1994]
- [Bertelrud et al 1980][research_bertelrud_bergmann_1980]
- [Beyak et al][research_ethansbeyak_meelanchoudhari]
- [Bhaduri et al 2024][research_bhaduri_sugarno_2024]
- [Bhanderi and Babinsky 2004][research_bhanderi_babinsky_2004]
- [Bhanderi and Babinsky 2005][research_bhanderi_babinsky_2005]
- [Bharadvaj 1990][research_bharadvaj_1990]
- [Bharadvaj 1991][research_bharadvaj_1991]
- [Bhardwaj and Sriram 2019][research_bhardwaj_sriram_2019]
- [Bhat 1971][research_bhat_1971]
- [Bhat 2018][research_bhat_2018]
- [Bhat et al 1990][research_bhatmk_vakiliad_1990]
- [Bhatia and Beran 2014][research_bhatia_beran_2014]
- [Bhatia and Beran 2016][research_bhatia_beran_2016]
- [Bhatia and Beran 2017][research_bhatia_beran_2017]
- [Bhatia and Beran 2017][research_bhatia_beran_2017_b]
- [Bhatia and Beran 2017][research_bhatia_beran_2017_c]
- [Bhola and Sengupta 2019][research_bhola_sengupta_2019]
- [Biber 2005][research_biber_2005]
- [Biber 2015][research_biber_2015]
- [Biber and Tilmann 2003][research_biber_tilmann_2003]
- [Bich Ngoc and Hung 2011][research_bichngoc_hung_2011]
- [Bidwell 1991][research_bidwell_1991]
- [Bielat 1959][research_bielatralphp_1959]
- [Bielat and Campbell 1953][research_bielatralphp_campbellgeorges_1953]
- [Bies 1966][research_bies_1966]
- [Bihrle and Billy 1980][research_bihrle_jr_1980]
- [Biibosunov and Karybekov 1967][research_biibosunov_karybekov_1967]
- [Billingsley 1976][research_billingsley_1976]
- [Binion 1969][research_binionjr_1969]
- [Binion 1971][research_binion_tw_1971]
- [Binion 1974][research_binion_jr_1974]
- [Binion 1975][research_binion_tw_1975]
- [Binion 1976][research_binion_tw_1976]
- [Binion and Lo 1970][research_binion_lo_1970]
- [Binion and Lo 1972][research_binionjr_lo_1972]
- [Biot 1949][research_biot_1949]
- [Bippes 1990][research_bippes_1990]
- [Bird 1991][research_birdga_1991]
- [Birdsall 1970][research_dlbirdsall_1970]
- [Biswas and Jimbo 2015][research_biswas_jimbo_2015]
- [Biswas et al 2025][research_biswas_mustak_2025]
- [Black][research_black]
- [Black 1968][research_black_1968]
- [Black 1969][research_black_1969]
- [Black et al 1963][research_black_carleton_1963]
- [Blackwell 1969][research_blackwelljajr_1969]
- [Blackwell 1969][research_jamesablackwelljr_1969]
- [Blackwell 1978][research_blackwelljr_1978]
- [Blackwell 1979][research_blackwell_1979]
- [Blackwell and Pounds 1977][research_blackwell_pounds_1977]
- [Blaha 1969][research_blaha_1969]
- [Blanchard 1953][research_blanchardwillards_1953]
- [Blanchard et al 1980][research_blanchard_phillips_1980]
- [Blanchard et al 1993][research_blanchard_larman_1993]
- [Blanco et al 2019][research_blanco_battiato_2019]
- [Bland 1979][research_srbland_1979]
- [Bland and Edwards 1983][research_bland_edwards_1983]
- [Bland and Young 1961][research_blandsr_youngls_1961]
- [Bleimeyer 1981][research_bleimeyer_1981]
- [Bliss 1980][research_bliss_1980]
- [Blosch et al 1992][research_blosch_carroll_1992]
- [Blosch et al 1993][research_blosch_carroll_1993]
- [Blose 1949][research_blose_1949]
- [Bluman and Gandhi 2011][research_bluman_gandhi_2011]
- [Bobbitt 1990][research_bobbitt_1990]
- [Bobenrieth Miserda et al 2006][research_bobenriethmiserda_lauterjung_2006]
- [Bodapati 1984][research_bodapati_1984]
- [Bodapati 1984][research_bodapati_1984_b]
- [Bodapati and Lee 1986][research_bodapati_lee_1986]
- [Bodin and Fuchs 2008][research_bodin_fuchs_2008]
- [Bodonyi and Smith 1986][research_bodonyi_smith_1986]
- [Bodspat et al 1980][research_bodspat_schairer_1980]
- [Boelens 2017][research_boelens_2017]
- [Bogatyrev 2017][research_bogatyrev_2017]
- [Bogdnoff 1953][research_bogdnoff_1953]
- [Bogdonoff 1987][research_bogdonoff_1987]
- [Bogdonoff 1989][research_bogdonoff_1989]
- [Bogdonoff and Smits 1992][research_bogdonoff_smits_1992]
- [Bogomolov 1968][research_bogomolov_1968]
- [Bohning and Doerffer 2002][research_bohning_doerffer_2002]
- [Bohning et al 1994][research_bohning_thiede_1994]
- [Boiarski and Daum 1972][research_boiarski_daum_1972]
- [Boling and Zha 2021][research_boling_zha_2021]
- [Boling et al 2020][research_boling_zha_2020]
- [Bonnifet et al 2017][research_bonnifet_gerolymos_2017]
- [Bonometti and Sorensen 2006][research_bonometti_sorensen_2006]
- [Bons and Martins 2020][research_bons_martins_2020]
- [Boothe et al 1974][research_boothe_chen_1974]
- [Boppe 1977][research_boppe_1977]
- [Boppe 1978][research_boppe_1978]
- [Boppe 1980][research_boppecw_1980]
- [Borden 1930][research_borden_1930]
- [Borland 1979][research_borland_1979]
- [Borland and Manro 1983][research_borlandcj_manrome_1983]
- [Borland and Rizzetta 1981][research_borland_rizzetta_1981]
- [Borland and Rizzetta 1982][research_borland_rizzetta_1982]
- [Borland and Sotomayer 1989][research_borland_sotomayer_1989]
- [Boroughs and Das 1999][research_boroughs_das_1999]
- [Borovoy et al 2012][research_borovoy_mosharov_2012]
- [Boswinkle and Smith 1958][research_boswinklerwjr_smithsliii_1958]
- [Boundary-layer-transition measurements on hemispheres of various surface roughnesses in a wind tunnel at mach numbers from 2.48 to 3.55 1959][research_boundary_layer_transition_measurements_1959]
- [Boundry value problems for transonic flow 2002][research_boundry_value_2002]
- [Bouquet and Vos 2017][research_bouquet_vos_2017]
- [Bourdet et al 2003][research_bourdet_bouhadji_2003]
- [Bourguet et al 2011][research_bourguet_braza_2011]
- [Bourisli and Hamadeh 2020][research_bourisli_hamadeh_2020]
- [Boutemedjet et al 2018][research_boutemedjet_samardzic_2018]
- [Bouton 1951][research_bouton_1951]
- [Bowers 1980][research_bowers_1980]
- [Boyd 1965][research_boyd_1965]
- [Boyd 1977][research_boyd_1977]
- [Boyden 1974][research_boydenrp_1974]
- [Boylan 1963][research_boylan_1963]
- [Boyle 2002][research_boyle_2002]
- [Boyle 2003][research_boyle_2003]
- [Boyles 1986][research_boylesjr_1986]
- [Bozeman et al][research_michaeldbozeman_richardlcampbell]
- [Brady et al 1954][research_brady_maier_1954]
- [Bragg and Soltani 1990][research_bragg_soltani_1990]
- [Braman et al 1983][research_braman_schweikhard_1983]
- [Branch et al 2023][research_branch_zang_2023]
- [Brandon et al 1995][research_brandon_brown_1995]
- [Braune and Hebler 2018][research_braune_hebler_2018]
- [Bray 1998][research_bray_1998]
- [Brazzel 1963][research_brazzel_1963]
- [Bredif 1983][research_bredif_1983]
- [Breitsamter and Laschka 1994][research_breitsamter_laschka_1994]
- [Briggs et al 1982][research_briggs_reed_1982]
- [Brilliant and Adamson 1973][research_brilliant_adamsonjr_1973]
- [Brilliant and Adamson 1974][research_brilliant_adamson_1974]
- [Brincklow et al 2021][research_brincklow_montgomery_2021]
- [Brion et al 2017][research_brion_dandois_2017]
- [Brion et al 2026][research_brion_rembaut_2026]
- [Britcher and Landman 2024][research_britcher_landman_2024]
- [Brodsky 1970][research_brodsky_1970]
- [Bronz 2019][research_bronz_2019]
- [Bronz et al 2017][research_bronz_garciademarina_2017]
- [Brooks et al 1980][research_brooks_stainback_1980]
- [Brooks et al 1994][research_brookscuylerwjr_harrischarlesd_1994]
- [Brosh et al 1983][research_brosh_kussoy_1983]
- [Broughton et al 1995][research_broughton_rainbird_1995]
- [Brouwer et al 2017][research_brouwer_2017]
- [Brower 1989][research_browerjr_1989]
- [Brown 2004][research_brown_2004]
- [Brown and Bastian 2008][research_brown_bastian_2008]
- [Brown and Bradley 1981][research_brown_bradley_1981]
- [Brown and Harris 1984][research_brown_harris_1984]
- [Brown et al 1986][research_brown_kussoy_1986]
- [Browne 1990][research_browne_1990]
- [Browne et al 2024][research_browne_maldonado_2024]
- [Browne et al 2025][research_browne_maldonado_2025]
- [Bruce et al 1984][research_brucejr_fuller_1984]
- [Brunet and Deck 2008][research_brunet_deck_2008]
- [Brunn and Stillwell 1956][research_brunncyrild_stillwellwendellh_1956]
- [Bruno Santos et al 2020][research_brunosantos_oliveira_2020]
- [Brunton et al 2020][research_brunton_noack_2020]
- [Brutyan et al 2020][research_brutyan_volkov_2020]
- [Bryce and Pinker 1977][research_bryce_pinker_1977]
- [Bryson 1971][research_brysonjr_1971]
- [Bryson 2021][research_bryson_2021]
- [Bryson and Desai 1968][research_brysonjr_desai_1968]
- [Bryson and Rumpfkeil 2016][research_bryson_rumpfkeil_2016]
- [Buckingham 1914][research_buckingham_1914]
- [Budhdev et al 2026][research_budhdev_senthilkumar_2026]
- [Bueno et al 2014][research_bueno_sandovalgoes_2014]
- [Bull and Bridges 1983][research_bull_bridges_1983]
- [Bull and Bridges 1985][research_bull_bridges_1985]
- [Bulygina 1958][research_bulygina_1958]
- [Bur and Berthouze 2003][research_bur_berthouze_2003]
- [Bur and Corbel 2000][research_bur_corbel_2000]
- [Bur et al 1997][research_bur_corbel_1997]
- [Bur et al 1998][research_bur_corbel_1998]
- [Bur et al 2000][research_bur_benay_2000]
- [Bur et al 2002][research_bur_benay_2002]
- [Bur et al 2009][research_bur_coponet_2009]
- [Burcham and Burken 1994][research_burchamjr_burken_1994]
- [Burcham and Pappas 1996][research_burchamjr_pappas_1996]
- [Burcham and Ray 1987][research_burchamjr_ray_1987]
- [Burcham et al 1993][research_burchamjr_maine_1993]
- [Burcham et al 1995][research_burchamfrankwjr_gatlindonaldh_1995]
- [Burcham et al 1997][research_burchamfrankwjr_burkenjohnj_1997]
- [Burdett 1947][research_burdett_1947]
- [Burdges 1973][research_burdges_1973]
- [Burdges 1979][research_burdges_1979]
- [Burdges 1981][research_burdges_1981]
- [Burdges et al 1975][research_burdgeskp_blackwelljajr_1975]
- [Burgess 1946][research_burgess_1946]
- [Burghiu 2023][research_burghiu_2023]
- [Burnham 1995][research_burnham_1995]
- [Burns and Danehy 2017][research_burns_danehy_2017]
- [Burrin et al 1986][research_burrin_salikuddin_1986]
- [Burris and Bender 1969][research_burris_bender_1969]
- [Burrows et al 2019][research_burrows_vukasinovic_2019]
- [Burrows et al 2021][research_burrows_vukasinovic_2021]
- [Bursey and Dickinson 1990][research_bursey_dickinson_1990]
- [Burstein 1965][research_burstein_1965]
- [Burtch 2015][research_burtch_2015]
- [Burton et al 2007][research_burton_loth_2007]
- [Busan 1998][research_busan_1998]
- [Busemann 1964][research_busemann_1964]
- [Busquet][research_busquet]
- [Butchart et al 1959][research_jet_transport_highspeed_1959]
- [Butler 1976][research_butler_1976]
- [Butler and Jones 1984][research_butler_jones_1984]
- [Buxbaum and Svenson 1972][research_buxbaum_svenson_1972]
- [Buxton et al 1997][research_buxton_beran_1997]
- [Buzzi and Fico 2006][research_buzzi_fico_2006]
- [Bynum et al 1970][research_bynum_ledford_1970]
- [Byrdsong 1977][research_byrdsongta_1977]
- [Byrdsong and Brooks 1980][research_byrdsongta_brookscwjr_1980]
- [Byreddy et al 2003][research_byreddy_grandhi_2003]
- [Cabaleiro de la Hoz and Fioriti 2021][research_cabaleirodelahoz_fioriti_2021]
- [Caballero 2001][research_caballero_2001]
- [Cahill 1986][research_cahill_1986]
- [Cahill et al 2010][research_cahill_minter_2010]
- [Cahn and Garcia 1971][research_cahn_garcia_1971]
- [Caiger and Gould 1971][research_caiger_gould_1971]
- [Cain 1979][research_cain_1979]
- [Calarese and Walterick 1978][research_calarese_walterick_1978]
- [Camberos et al 2014][research_camberos_kolonay_2014]
- [Camberos et al 2015][research_camberos_kolonay_2015]
- [Campbell 1984][research_campbell_1984]
- [Campbell and Smith 1987][research_campbell_smith_1987]
- [Campbell et al 1986][research_campbell_waggoner_1986]
- [Canbazoglu et al 1996][research_canbazoglu_lin_1996]
- [Candler 2001][research_candler_2001]
- [Candon et al][research_michaelcandon_vincenzomuscarello]
- [Candon et al 2019][research_candon_levinski_2019]
- [Candon et al 2024][research_candon_hale_2024]
- [Canic and Keyfitz 1995][research_canic_keyfitz_1995]
- [Canoville and Lewis 2025][research_canoville_lewis_2025]
- [Canter and Groves 1994][research_canter_groves_1994]
- [Cao and Lyu 2024][research_cao_lyu_2024]
- [Cao et al 2024][research_cao_fu_2024]
- [Cao et al 2025][research_cao_lin_2025]
- [Capone 1975][research_capone_1975]
- [Capone and Maiden 1977][research_caponefj_maidendl_1977]
- [Capone and Mason 1984][research_caponefj_masonml_1984]
- [Capone et al 1983][research_capone_mason_1983]
- [Capone et al 1987][research_capone_re_1987]
- [Carbonara and Binnie 1938][research_carbonara_binnie_1938]
- [Carden 1963][research_carden_1963]
- [Carey 1964][research_carey_1964]
- [Carey 1965][research_carey_1965]
- [Carloni and Azevedo 2023][research_carloni_azevedo_2023]
- [Carlsen 1994][research_carlsen_1994]
- [Carlsen 1995][research_carlsen_1995]
- [Carlson 1976][research_carlson_1976]
- [Carlson 1979][research_carlsonla_1979]
- [Carlson 1981][research_carlson_1981]
- [Carlson and Miller 1969][research_carlsonhw_millerds_1969]
- [Carlson and Weed 1985][research_carlson_weed_1985]
- [Carlson et al 1965][research_carlsonharryw_mcleanfedward_1965]
- [Carlson et al 1985][research_carlson_pendergraftjr_1985]
- [Carlson et al 2004][research_carlson_glauser_2004]
- [Carmel and Turner 1957][research_carmelmelvinm_turnerkennethl_1957]
- [Carpenter et al 2025][research_carpenter_hantsche_2025]
- [Carr et al 1998][research_carr_chandrasekhara_1998]
- [Carrese et al 2016][research_carrese_marzocca_2016]
- [Carter 1988][research_carter_1988]
- [Carter and Hafez 1982][research_carter_hafez_1982]
- [Carter et al 2009][research_carter_vicroy_2009]
- [Casey 1988][research_casey_1988]
- [Cassel et al 1969][research_cassel_durando_1969]
- [Castellani et al 2016][research_castellani_cooper_2016]
- [Castro et al 2000][research_castro_ekaterinaris_2000]
- [Castro et al 2001][research_castro_jones_2001]
- [Castro et al 2002][research_castro_ekaterinaris_2002]
- [Castro et al 2003][research_castro_jones_2003]
- [Catalano and Fremaux 1987][research_catalano_fremaux_1987]
- [Caughey 1976][research_caughey_1976]
- [Caughey 1982][research_caughey_1982]
- [Caughey and Jameson 1977][research_caughey_jameson_1977]
- [Caughey and Jameson 1979][research_caughey_jameson_1979]
- [Caughey and Jameson 1979][research_caughey_jameson_1979_b]
- [Cavcar 2006][research_cavcar_2006]
- [Cebeci 1974][research_cebecit_1974]
- [Cecrdle 2011][research_cecrdle_2011]
- [Celestino et al 2026][research_celestino_olichevishalila_2026]
- [Celik and Roberts 1992][research_celik_roberts_1992]
- [Celmins 1990][research_celmins_1990]
- [Cenko and Madson 1993][research_cenko_madson_1993]
- [CFD Analysis of RAE 2822 Supercritical Airfoil at Transonic MACH Speeds 2015][research_cfd_analysis_of_2015]
- [Chakrabartty 1990][research_chakrabartty_1990]
- [Chakrabartty and Dhanalakshmi 1995][research_chakrabartty_dhanalakshmi_1995]
- [Chakraborty et al 2015][research_chakraborty_ozcan_2015]
- [Chakraborty et al 2022][research_chakraborty_roy_2022]
- [Chakravarty and Narayanaswamy 2026][research_chakravarty_narayanaswamy_2026]
- [Chaloner and Verdinelli 1995][research_chaloner_verdinelli_1995]
- [Chan 1980][research_chan_1980]
- [Chan 1980][research_chan_1980_b]
- [Chan 1985][research_chan_1985]
- [Chan et al 1976][research_chan_chen_1976]
- [Chan et al 1997][research_chan_yeung_1997]
- [Chan et al 2017][research_chan_hooker_2017]
- [Chan et al 2017][research_chan_jones_2017]
- [Chandler and Chisholm 1993][research_chandler_chisholm_1993]
- [Chandrasekhara 1994][research_chandrasekhara_1994]
- [Chandrasekhara and Carr 1989][research_chandrasekhara_carr_1989]
- [Chandrasekhara and Carr 1990][research_chandrasekhara_carr_1990]
- [Chandrasekharan et al 2015][research_chandrasekharan_iarocci_2015]
- [Chandravamsi et al 2023][research_chandravamsi_bhardwaj_2023]
- [Chang 1962][research_chang_1962]
- [Chang 1981][research_chang_1981]
- [Chang et al 2022][research_chang_cai_2022]
- [Chanzy][research_chanzy]
- [Chao and Shijun 1996][research_chao_shijun_1996]
- [Chao and van Dam 1998][research_chao_vandam_1998]
- [Chaparro et al 2016][research_chaparro_fujiwara_2016]
- [Chaparro et al 2017][research_chaparro_fujiwara_2017]
- [Chaplin 2013][research_chaplin_2013]
- [Chapman et al 1992][research_chapman_bonness_1992]
- [Chapter 4. Wing-Tail Plane Interference at Supersonic Speeds 1957][research_chapter_4_1957]
- [CHAPTER NINE. The Minimum Drag of Thin Wings 1990][research_chapter_nine_1990]
- [Chase 1992][research_chase_1992]
- [Chassaing and Lucor 2010][research_chassaing_lucor_2010]
- [Chau and Duensing][research_timothychau_jaredcduensing]
- [Chau and Zingg 2022][research_chau_zingg_2022]
- [Chau et al 2026][research_chau_piotrowski_2026]
- [Chaudhuri 1977][research_chaudhuri_1977]
- [Chaudhuri and Balasubramanyan 1982][research_chaudhuri_balasubramanyan_1982]
- [Chaussee 1978][research_chaussee_1978]
- [Cheatham and Kurbjun 1948][research_transonic_drag_wingbody_1948]
- [Chen 1981][research_chen_1981]
- [Chen 1982][research_chen_1982]
- [Chen 1983][research_chen_1983]
- [Chen 1990][research_chen_1990]
- [Chen 2018][research_chen_2018]
- [Chen and Bui 1990][research_chen_bui_1990]
- [Chen and Chan 1976][research_chen_chan_1976]
- [Chen and Gat 2022][research_chen_gat_2022]
- [Chen and Liu 2000][research_chen_liu_2000]
- [Chen and Liu 2014][research_chen_liu_2014]
- [Chen and Mears 1957][research_chen_mears_1957]
- [Chen and Thuerey 2024][research_chen_thuerey_2024]
- [Chen and Zhang 2006][research_chen_zhang_2006]
- [Chen et al 1979][research_chen_sajben_1979]
- [Chen et al 1982][research_chen_verhoff_1982]
- [Chen et al 1984][research_chen_vassberg_1984]
- [Chen et al 1985][research_chen_clark_1985]
- [Chen et al 1985][research_chen_vassberg_1985]
- [Chen et al 1985][research_chencl_chowcy_1985]
- [Chen et al 1987][research_chen_li_1987]
- [Chen et al 1989][research_chen_cantwell_1989]
- [Chen et al 1990][research_chen_cantwell_1990]
- [Chen et al 2002][research_chen_sulaeman_2002]
- [Chen et al 2006][research_chen_zha_2006]
- [Chen et al 2009][research_chen_ulker_2009]
- [Chen et al 2009][research_chen_xu_2009]
- [Chen et al 2014][research_chen_zhang_2014]
- [Chen et al 2020][research_chen_gao_2020]
- [Chen et al 2021][research_chen_dong_2021]
- [Chen et al 2022][research_chen_gao_2022]
- [Chen et al 2023][research_chen_gao_2023]
- [Chen et al 2023][research_chen_wei_2023]
- [Chen et al 2024][research_chen_wang_2024]
- [Chen et al 2026][research_chen_wang_2026]
- [Chen et al 2026][research_chen_wang_2026_b]
- [Chen et al 2026][research_chen_zhang_2026]
- [Chen-Chi 1983][research_chenchi_1983]
- [Cheney 1988][research_cheney_1988]
- [Cheng 1977][research_cheng_1977]
- [Cheng 1982][research_cheng_1982]
- [Cheng 1989][research_cheng_1989]
- [Cheng 2009][research_cheng_2009]
- [Cheng and Hafez 1973][research_cheng_hafez_1973]
- [Cheng and Hafez 1973][research_cheng_hafez_1973_b]
- [Cheng and Hafez 1975][research_cheng_hafez_1975]
- [Cheng and Luo 1996][research_cheng_luo_1996]
- [Cheng and Smith 1994][research_cheng_smith_1994]
- [Cheng et al 1980][research_cheng_meng_1980]
- [Cheng et al 2015][research_cheng_lowenberg_2015]
- [Chern and Keyfitz 2016][research_chern_keyfitz_2016]
- [Chesneau and Wood 1995][research_chesneau_wood_1995]
- [Chestnutt 1966][research_chestnutt_1966]
- [Cheung et al 1995][research_cheung_aaronson_1995]
- [Chevalier 1960][research_chevalier_1960]
- [Chevalier and Robertson 1963][research_chevalier_robertson_1963]
- [Chew 1953][research_chew_1953]
- [Chew 1955][research_chew_1955]
- [Chiara Iorio][research_chiaraiorio]
- [Chiarelli and Bonomo 2019][research_chiarelli_bonomo_2019]
- [Chieng 1991][research_chieng_1991]
- [Childs 1953][research_childsjoanm_1953]
- [Childs and Seebaugh 1969][research_childsme_seebaughwr_1969]
- [Childs and Seebaugh 1970][research_childsme_seebaughwr_1970]
- [Chin 1992][research_chin_1992]
- [Chin and Lentink 2019][research_chin_lentink_2019]
- [Chin and Rizzetta 1979][research_chin_rizzetta_1979]
- [Chipman et al 1985][research_chipman_rauch_1985]
- [Chmielewski 1986][research_chmielewski_1986]
- [Choi et al 2016][research_choi_kang_2016]
- [Chou and Smith 1978][research_chou_smith_1978]
- [Choudhuri and Knight 1995][research_choudhuri_knight_1995]
- [Choudhuri and Knight 1996][research_choudhuri_knight_1996]
- [Chow 1979][research_chow_1979]
- [Chow 1984][research_chow_1984]
- [Chow 1985][research_chow_1985]
- [Chow 1986][research_chowcy_1986]
- [Chow and Huang 1982][research_chow_huang_1982]
- [Chow et al 1985][research_chowcy_holsttl_1985]
- [Chow et al 1987][research_chowchuenyen_vandalsemwilliamr_1987]
- [Chriss 1991][research_randallmchriss_1991]
- [Chriss et al 1990][research_chrissrm_hingstwr_1990]
- [Christian et al 2023][research_christian_gee_2023]
- [Christison Gray and Martins 2026][research_christisongray_martins_2026]
- [Chu and Lawing 1990][research_chujulio_lawingpiercel_1990]
- [Chu et al 1990][research_chujulio_flechnerstuartg_1990]
- [Chung 2000][research_chung_2000]
- [Chung 2000][research_chung_2000_b]
- [Chung 2002][research_chung_2002]
- [Chung 2003][research_chung_2003]
- [Chung 2007][research_chung_2007]
- [Chung 2017][research_chung_2017]
- [Chung et al 1994][research_chung_miau_1994]
- [Chung et al 1995][research_chung_miau_1995]
- [Chung et al 2002][research_chung_lee_2002]
- [Chung et al 2003][research_chung_lee_2003]
- [Chung et al 2021][research_chung_su_2021]
- [Chwalowski et al 2016][research_chwalowskipawel_quoneliot_2016]
- [Chwalowski et al 2017][research_chwalowski_heeg_2017]
- [Chwalowski et al 2022][research_chwalowski_massey_2022]
- [Chyu and Davis 1979][research_chyu_davis_1979]
- [Chyu and Davis 1984][research_chyuwj_davisss_1984]
- [Chyu and Davis 1985][research_chyuwj_davisss_1985]
- [Chyu and Kuwahara 1982][research_chyu_kuwahara_1982]
- [Chyu and Schiff 1981][research_chyu_schiff_1981]
- [Cicala and Miele 1956][research_cicala_miele_1956]
- [Cinnella 2001][research_cinnella_2001]
- [Cinnella and Congedo 2006][research_cinnella_congedo_2006]
- [Ciobaca and Dandois 2017][research_ciobaca_dandois_2017]
- [Clark 2026][research_clark_2026]
- [Clark and Adler 2016][research_clark_adler_2016]
- [Clark and Pelkman 2001][research_clark_pelkman_2001]
- [Clark et al 2010][research_clark_bain_2010]
- [Clarke et al 2005][research_clarke_allen_2005]
- [Clay 1967][research_clay_1967]
- [Clemens and Cortner 1963][research_clemens_cortner_1963]
- [Cler 1995][research_cler_1995]
- [Clevenson and Thompson 1957][research_clevensonsa_thompsonrf_1957]
- [Cline et al 1986][research_cline_hyde_1986]
- [Clyde et al 1984][research_clyde_bonner_1984]
- [Coakley 1987][research_coakley_1987]
- [Coates and Thamburaj 2008][research_coates_thamburaj_2008]
- [Coder 2021][research_coder_2021]
- [Coder 2023][research_coder_2023]
- [Coder 2025][research_coder_2025]
- [Coder 2026][research_coder_2026]
- [Coen 2022][research_coen_2022]
- [Coen et al 2017][research_coen_loubeau_2017]
- [Coen et al 2023][research_coen_loubeau_2023]
- [Cogo 2024][research_cogo_2024]
- [Cohen 1970][research_cohen_1970]
- [Cohen and Motallebi 2006][research_cohen_motallebi_2006]
- [Cohen and Motallebi 2008][research_cohen_motallebi_2008]
- [Cole 1985][research_cole_1985]
- [Cole 1986][research_cole_1986]
- [Cole 1988][research_cole_1988]
- [Cole and Malmuth 1982][research_cole_malmuth_1982]
- [Cole and Malmuth 1989][research_cole_malmuth_1989]
- [Cole and Malmuth 1989][research_colejuliand_malmuthnormand_1989]
- [Cole and Malmuth 2005][research_cole_malmuth_2005]
- [Cole et al 1980][research_cole_cook_1980]
- [Cole et al 1990][research_colestanleyr_mossstevenw_1990]
- [Cole et al 2003][research_cole_noll_2003]
- [Colera and Pérez-Saborid 2018][research_colera_perezsaborid_2018]
- [Colgren 1996][research_colgren_1996]
- [Collar 1946][research_collar_1946]
- [Collazo Garcia and Ansell 2018][research_collazogarcia_ansell_2018]
- [Collazo Garcia and Ansell 2019][research_collazogarcia_ansell_2019]
- [Collazo Garcia and Ansell 2021][research_collazogarcia_ansell_2021]
- [Collazo Garcia et al 2021][research_collazogarcia_saxtonfox_2021]
- [Collins 1970][research_collins_1970]
- [Collins 1974][research_collins_1974]
- [Comfort and Todisco 1969][research_comfort_todisco_1969]
- [Commercial Transports-Aerodynamic Design for Cruise Performance Efficiency 1982][research_commercial_transports_aerodynamic_1982]
- [Comparison of Aircraft Noise Measured in Flight Test and in a NASA Ames Wind Tunnel 1975][research_comparison_of_1975]
- [Comparison of flowfield surveys and computations of a crossing-shock wave/boundary layer interaction 1994][research_comparison_of_1994]
- [Compressible, Subsonic Flows and Transonic Flows 2021][research_compressible_subsonic_2021]
- [Compressible, Subsonic Flows and Transonic Flows 2025][research_compressible_subsonic_2025]
- [Computation of low density supersonic flow over a pitot tube 1985][research_computation_of_1985]
- [Computational Methods for Unsteady Transonic Flows 1989][research_computational_methods_1989]
- [Connolly 1965][research_connolly_1965]
- [Consigny et al 1983][research_consigny_gravelle_1983]
- [Conti et al 1972][research_contirj_thomaspd_1972]
- [Cook][research_cook]
- [Cook 1978][research_cookwj_1978]
- [Cook 1979][research_cook_1979]
- [Cook 1995][research_cook_1995]
- [Cook and Schleiniger 1993][research_cook_schleiniger_1993]
- [Cook et al 1975][research_cookwj_presleyll_1975]
- [Cook et al 1978][research_cookwj_chaneymj_1978]
- [Cook et al 1978][research_cookwj_presleyll_1978]
- [Cook et al 2004][research_cook_ghee_2004]
- [Cook-Ioannidis 1991][research_cookioannidis_1991]
- [Cooksey et al 1964][research_cooksey_dillenschneider_1964]
- [Coon and Chapman 1991][research_coon_chapman_1991]
- [Coppin et al 2025][research_coppin_martin_2025]
- [Corda and Vachon 2003][research_stephencorda_michaeljakevachon_2003]
- [Cornette 1961][research_cornetteeldens_1961]
- [Cornette and Rigby 1962][research_cornettees_rigbyrn_1962]
- [Cornish 1963][research_cornish_1963]
- [Coschignano and Babinsky 2018][research_coschignano_babinsky_2018]
- [Coschignano and Babinsky 2019][research_coschignano_babinsky_2019]
- [Cosentino and Holst 1984][research_cosentinogb_holsttl_1984]
- [Cosentino and Holst 1985][research_cosentino_holst_1985]
- [Cosenza and Kummeth 1974][research_cosenza_kummeth_1974]
- [Cottrell and Lijewski 1987][research_cottrell_lijewski_1987]
- [Cottrell et al 1987][research_cottrell_martinez_1987]
- [Couch 1972][research_couch_1972]
- [Coulton][research_coulton]
- [Coustols et al 1995][research_coustols_prudhomme_1995]
- [Coustols et al 1997][research_coustols_seraudie_1997]
- [Covert and Haldeman 1978][research_covert_haldeman_1978]
- [Cox et al 1997][research_cox_jackson_1997]
- [Crabill 1956][research_crabillnormanl_1956]
- [Crafton et al 2004][research_crafton_elliott_2004]
- [Crain et al 1965][research_crain_brown_1965]
- [Cramer 2001][research_cramer_2001]
- [Cramer et al 1992][research_cramer_tarkenton_1992]
- [Crane 1948][research_craneharoldl_1948]
- [Crane 1948][research_craneharoldl_1948_b]
- [Crane and Beckhardt 1948][research_craneharoldl_beckhardtarnoldr_1948]
- [Crane and Sommer 1961][research_craneharoldl_sommerrobertw_1961]
- [Crassidis 2005][research_crassidis_2005]
- [Crisalli et al 1979][research_crisalli_stahara_1979]
- [Cristian and Vasile 2010][research_cristian_vasile_2010]
- [Crites et al 1992][research_crites_rueger_1992]
- [Crouch et al 2008][research_crouch_garbaruk_2008]
- [Crouch et al 2009][research_crouch_garbaruk_2009]
- [Crouch et al 2018][research_crouch_garbaruk_2018]
- [Crouch et al 2019][research_crouch_garbaruk_2019]
- [Crouch et al 2024][research_crouch_ahrabi_2024]
- [Crowder 2018][research_crowder_2018]
- [Crowder et al 1998][research_crowder_amiryants_1998]
- [Crown 1950][research_crown_1950]
- [Crozier et al 2014][research_crozier_chargy_2014]
- [Cui et al 2022][research_cui_yue_2022]
- [Cumming and Lowe 1971][research_cumming_lowe_1971]
- [Cumming et al 2016][research_cummingstephenb_smithmarks_2016]
- [Cunningham 1974][research_cunninghamamjr_1974]
- [Cunningham 1994][research_cunningham_1994]
- [Cunningham and Den Boer 1992][research_cunninghamjr_denboer_1992]
- [Cunningham and Plentovich 1987][research_cunninghamjr_plentovich_1987]
- [Cunningham et al 1989][research_cunninghamherbertj_bennettrobertm_1989]
- [Cuppoletti et al 2016][research_cuppoletti_saucier_2016]
- [Curley 1991][research_curley_1991]
- [Currao 2024][research_currao_2024]
- [Currao and He 2024][research_currao_he_2024]
- [Currao and Jiang 2026][research_currao_jiang_2026]
- [Currao and Yeh 2026][research_currao_yeh_2026]
- [Curry and Sim 1982][research_curry_sim_1982]
- [Curry and Sim 1984][research_curryre_simag_1984]
- [Curtin et al 2002][research_curtinmm_boguedr_2002]
- [Czerwinska et al 2001][research_czerwinska_doerffer_2001]
- [Czysz 1963][research_czysz_1963]
- [D'Afiero 2025][research_dafiero_2025]
- [D'Aguanno et al 2021][research_daguanno_schrijer_2021]
- [D'Aguanno et al 2021][research_daguanno_schrijer_2021_b]
- [D'Aguanno et al 2021][research_daguanno_schrijer_2021_c]
- [D'Aguanno et al 2022][research_daguanno_campspons_2022]
- [D'Ewart et al 1958][research_dewart_jr_1958]
- [D. Supersonic and Transonic Small Perturbation Theory 1954][research_d_supersonic_1954]
- [da Silva Tuan et al 2024][research_tuan_malatesta_2024]
- [Dahlen 1953][research_dahlentheodoree_1953]
- [Dahlke 1969][research_dahlke_1969]
- [Dai and Zhang 2023][research_dai_zhang_2023]
- [Daley and Humphreys 1947][research_daleybernardn_humphreysmiltond_1947]
- [Damstrom and Mayes 1970][research_damstrom_mayes_1970]
- [Damstrom and Mayes 1971][research_damstrom_mayes_1971]
- [Dana 1993][research_x15_lessons_1993]
- [Danberg and Tschirschnitz 1983][research_danberg_tschirschnitz_1983]
- [Danberg et al 1985][research_danberg_heavey_1985]
- [Dandois 2016][research_dandois_2016]
- [Dandois et al 2018][research_dandois_mary_2018]
- [Dang and Yang 2010][research_dang_yang_2010]
- [Dang et al 2019][research_dang_zhao_2019]
- [Dannenberg et al 1960][research_dannenbergre_gambuccibj_1960]
- [Dargel 1997][research_dargel_1997]
- [Dargel and Thiede 1987][research_dargel_thiede_1987]
- [Das and Cohen 2017][research_das_cohen_2017]
- [Das and Kim 2016][research_das_kim_2016]
- [Das et al 2020][research_das_carrese_2020]
- [Das et al 2022][research_das_marzocca_2022]
- [Daum and Zalovcik 1946][research_daumfredl_zalovcikjohna_1946]
- [David and Hale 1978][research_david_hale_1978]
- [Davies 2020][research_davies_2020]
- [Davies 2020][research_davies_2020_b]
- [Davies 2020][research_davies_2020_c]
- [Davies 2025][research_davies_2025]
- [Davies 2025][research_davies_2025_b]
- [Davies 2025][research_davies_2025_c]
- [Davis 1985][research_davisjr_1985]
- [Davis 2015][research_davis_2015]
- [Davis 2019][research_davis_2019]
- [Davis and Bendiksen 1993][research_davis_bendiksen_1993]
- [Davis and Malcolm 1979][research_davisss_malcolmgn_1979]
- [Davis and Malcolm 1980][research_davis_malcolm_1980]
- [Davis and Mitchell 1960][research_davisoh_mitchellga_1960]
- [Davis and Wornom 1958][research_davisddjr_wornomde_1958]
- [Davis et al 1998][research_davisdo_willisbp_1998]
- [Davison 1963][research_davison_1963]
- [Day 1953][research_x2_glide_1953]
- [Day and Reisert 1959][research_x2_mach32_1959]
- [Day and Stillwell 1952][research_richardeday_wendellhstillwell_1952]
- [de Faria Mello and Sankar 1999][research_defariamello_sankar_1999]
- [de Mattos and Wagner 1994][research_demattos_wagner_1994]
- [de Melo et al 2024][research_demelo_bussamra_2024]
- [De Vanna 2025][research_devanna_2025]
- [Deangelis 1981][research_deangelis_1981]
- [Deangelis and Monaghan 1977][research_f8_buffet_1977]
- [Debiasi et al 2010][research_debiasi_yan_2010]
- [DeBonis et al 1995][research_debonis_georgiadis_1995]
- [Deck 2004][research_deck_2004]
- [Deck 2005][research_deck_2005]
- [Decker and Miller 2019][research_decker_miller_2019]
- [Deckert 1981][research_deckert_1981]
- [Deepa and Gupta 2023][research_deepa_gupta_2023]
- [Deere et al 2016][research_deere_luckring_2016]
- [Deese and Agarwal 1987][research_deese_agarwal_1987]
- [Deese and Agarwal 1988][research_deese_agarwal_1988]
- [Degregori and Kim 2021][research_degregori_kim_2021]
- [Degrez and Ginoux 1987][research_degrez_ginoux_1987]
- [Degrez and Vandromme 1986][research_degrez_vandromme_1986]
- [Dehghan Manshadi and Rabani 2016][research_dehghanmanshadi_rabani_2016]
- [Deiler and Sachs 2026][research_deiler_sachs_2026]
- [Deiwert 1974][research_deiwert_1974]
- [Deiwert 1975][research_deiwert_1975]
- [Deiwert 1975][research_deiwertgs_1975]
- [Deiwert and Bailey 1979][research_deiwertgs_baileyhe_1979]
- [Deiwert et al 1975][research_deiwertgs_mcdevittjb_1975]
- [DeLeo and Hagen 1963][research_deleo_hagen_1963]
- [Delery 1981][research_delery_1981]
- [Delery et al 1986][research_jdelery_jgmarvin_1986]
- [DeLoach 2012][research_deloach_2012]
- [DeLoach 2014][research_deloach_2014]
- [Demeritte and Gauzza 1958][research_demeritte_gauzza_1958_b]
- [Demeritte et al 1958][research_demeritte_gauzza_1958]
- [Demetriades 1977][research_demetriades_1977]
- [Demetriades 1985][research_demetriades_1985]
- [Denegri and Dubben 2005][research_denegri_dubben_2005]
- [Deng and Qin 2021][research_deng_qin_2021]
- [Deng et al 2023][research_deng_zhang_2023]
- [Denham and Owens 2016][research_denham_owens_2016]
- [Denison et al 2019][research_denisonmarie_garaianirban_2019]
- [Derajat and Hariowibowo 2018][research_derajat_hariowibowo_2018]
- [DeRoo and Takahashi 2024][research_deroo_takahashi_2024]
- [Desai et al 1977][research_desai_viswanathan_1977]
- [Deshpande and Poggie 2020][research_deshpande_poggie_2020]
- [Design and CFD Analysis of Supercritical Airfoil 0714 Under Ground-Level Atmospheric Conditions 2024][research_design_and_2024]
- [Design and Installation of Pitot-Static Systems for Transport Aircraft][research_design_and]
- [DeSpirito 2008][research_despirito_2008]
- [DeSpirito 2009][research_despirito_2009]
- [Destarac and van der Vooren 2004][research_destarac_vandervooren_2004]
- [Devan 1987][research_devan_1987]
- [Devan and Kania 1985][research_devan_kania_1985]
- [Deveikis 1983][research_deveikiswd_1983]
- [Dhurandhar et al 2026][research_dhurandhar_sharma_2026]
- [Di Fabbio et al 2022][research_difabbio_tangermann_2022]
- [Di Fiore dos Santos et al 2000][research_difioredossantos_lewis_2000]
- [Di Pasquale 2024][research_dipasquale_2024]
- [Di Pasquale and Prince 2023][research_dipasquale_prince_2023]
- [Dias 2023][research_dias_2023]
- [Dias et al 2023][research_dias_budisic_2023]
- [Dicarlo et al 1992][research_dicarlo_brown_1992]
- [Dick 1955][research_dick_1955]
- [Dickey 1959][research_dickeyrobertr_1959]
- [Dickinson et al 2024][research_dickinson_babinsky_2024]
- [Diesperov and Ryzhov 1971][research_diesperov_ryzhov_1971]
- [Dietrich et al 1984][research_dietrich_kromer_1984]
- [Dietz 2005][research_dietz_2005]
- [Dietz et al 2004][research_dietz_schewe_2004]
- [Dietz et al 2005][research_dietz_schewe_2005]
- [Diggins 1951][research_diggins_1951]
- [Dimitriadis 2025][research_dimitriadis_2025]
- [Ding et al 2023][research_ding_han_2023]
- [Dippold and Zaman 2015][research_dippold_zaman_2015]
- [Dittmar 1989][research_dittmar_1989]
- [Dive Testing for Flutter, Vibration, and Buffeting 2003][research_dive_testing_2003]
- [Dix and Mattasits 1980][research_dix_mattasits_1980]
- [Dixon and Hunsaker 2023][research_dixon_hunsaker_2023]
- [Djayapertapa and Allen 2000][research_djayapertapa_allen_2000]
- [Djayapertapa and Allen 2002][research_djayapertapa_allen_2002]
- [Djayapertapa and Allen 2004][research_djayapertapa_allen_2004]
- [Djojodihardjo 2023][research_djojodihardjo_2023]
- [Djomehri et al 1995][research_djomehrimjahed_buningpieterg_1995]
- [Dobbs and Hodson 1979][research_dobbssk_hodsonch_1979]
- [Dodbele et al 1986][research_dodbele_vandam_1986]
- [Dods and Hanly 1972][research_dodsjr_hanly_1972]
- [Dodson 2005][research_dodson_2005]
- [Doerffer and Telega 2013][research_doerffer_telega_2013]
- [Doggett and Cunningham 1976][research_doggettrvjr_cunninghamhj_1976]
- [Doggett et al 1959][research_doggettrvjr_morganhg_1959]
- [Doggett et al 1989][research_doggettrobertvjr_soistmanndavidl_1989]
- [Doherty 2017][research_doherty_2017]
- [Doherty et al 2018][research_doherty_wang_2018]
- [Doig et al 2013][research_doig_bogdan_2013]
- [Dolling 1986][research_dolling_1986]
- [Dolling 1988][research_dolling_1988]
- [Dolling 1993][research_dolling_1993]
- [Dolling 1993][research_dollingds_1993]
- [Dolling 2000][research_dolling_2000]
- [Dolling and Barter 1995][research_dollingdavids_barterjohnw_1995]
- [Dolling and Bogdonoff 1980][research_dolling_bogdonoff_1980]
- [Dolling and Brusniak 1987][research_dolling_brusniak_1987]
- [Dolling and Clemens 2003][research_dolling_clemens_2003]
- [Dolling et al 2003][research_dolling_clemens_2003_b]
- [Domingos et al 2024][research_domingos_ribeiro_2024]
- [Donaldson 1944][research_donaldsoncolemandup_1944]
- [Donegan 1984][research_donegan_1984]
- [Donlan 1976][research_donlan_collected_1976]
- [Donlan et al 1976][research_xs1_tunnel_1976]
- [Donovan and Takahashi 2010][research_donovan_takahashi_2010]
- [Dor et al 1989][research_dor_mignosi_1989]
- [Doria and South 1982][research_doria_southjr_1982]
- [Dorsch and Brun 1953][research_dorschrobertg_brunrinaldoj_1953]
- [Dou et al 2006][research_dou_khoo_2006]
- [Dougherty 1977][research_dougherty_ns_1977]
- [Dougherty 2021][research_dougherty_2021]
- [Dougherty and Fisher 1980][research_doughertyjr_fisher_1980]
- [Dougherty and Steinle 1974][research_doughertyjr_steinlejr_1974]
- [Dougherty et al 1975][research_dougherty_ns_1975]
- [Dowell 1986][research_dowell_1986]
- [Dowell and Bliss 1978][research_dowell_bliss_1978]
- [Dowell and Hall 2003][research_dowell_hall_2003]
- [Dowell and Ilgamov 1988][research_dowell_ilgamov_1988]
- [Dowell et al 1981][research_dowell_williams_1981]
- [Dowell et al 2001][research_dowell_thomas_2001]
- [Drag Polar Measurement in Level Flight 2021][research_drag_polar_2021]
- [Dragoş 2003][research_dragos_2003]
- [Drake 1949][research_hubertmdrake_1949]
- [Drake 1950][research_x1_lateral_1950]
- [Drake 1957][research_high_altitude_1957]
- [Drake and McKay 1953][research_drakehubertm_mckayjohnb_1953]
- [Drake and Williams 1958][research_williams_drake_1948]
- [Drake et al 1948][research_xs1_accelerated_1948]
- [Draper and Moran 1973][research_draper_moran_1973]
- [Drela 1991][research_drela_1991]
- [Drela 1992][research_drela_1992]
- [Drela 1992][research_drelamark_1992]
- [Drela 2022][research_drela_2022]
- [Drela and Giles 1986][research_drela_giles_1986]
- [Dress 1988][research_dress_1988]
- [Dress 1989][research_dress_1989]
- [Drikakis and Durst 1994][research_drikakis_durst_1994]
- [Driver 1974][research_driver_1974]
- [Droney et al 2020][research_christopherkdroney_anthonyjsclafani_2020]
- [Drèze and di Mare 2024][research_dreze_dimare_2024]
- [Du et al 2025][research_du_guo_2025]
- [Du et al 2026][research_du_yu_2026]
- [Duan et al 2026][research_duan_wan_2026]
- [Dudley and Torres 2007][research_dudley_torres_2007]
- [Duffy 1989][research_duffy_1989]
- [Dugundji 1965][research_dugundji_1965]
- [Dugundji et al 1962][research_dugundji_dowell_1962]
- [Dunagan][research_dunagan]
- [Dunagan et al 1986][research_dunaganstephene_brownjamesl_1986]
- [Duncan 1950][research_duncan_1950]
- [Dunning 1959][research_dunningrw_1959]
- [Dupont et al 2011][research_dupont_debieve_2011]
- [Dupuis 1988][research_dupuis_1988]
- [Dupuis 2002][research_dupuis_2002]
- [Duraisamy et al 2006][research_duraisamy_mccroskey_2006]
- [Duran 2026][research_duran_2026]
- [Durham et al 1996][research_durham_bolling_1996]
- [Durmus 2021][research_durmus_2021]
- [Durston][research_dondurston]
- [Durston][research_dondurston_b]
- [Dutton and Addy 1980][research_dutton_addy_1980]
- [Dvorak and Choi 1982][research_dvorak_choi_1982]
- [Dvorak et al 1947][research_dvorak_kosiak_1947]
- [Dvořák 1965][research_dvorak_1965]
- [Dykas et al 2017][research_dykas_szymanski_2017]
- [Délery 1989][research_delery_1989]
- [Eades et al 1964][research_eades_jr_1964]
- [Eastep and Olsen 1979][research_eastep_olsen_1979]
- [Eastep and Olsen 1980][research_eastep_olsen_1980]
- [Eastep et al 1998][research_eastep_andersen_1998]
- [Eastep et al 2001][research_eastep_andersen_2001]
- [Eberle 1981][research_eberle_1981]
- [Ecer 1985][research_ecer_1985]
- [Ecer 1989][research_ecer_1989]
- [Eckhaus 1962][research_eckhaus_1962]
- [Edelmann et al 2009][research_edelmann_roberts_2009]
- [Edwards 1996][research_edwardsjohnw_1996]
- [Edwards 1997][research_edwardsjohnw_1997]
- [Edwards 2007][research_edwards_2007]
- [Edwards 2008][research_edwards_2008]
- [Edwards 2009][research_edwards_2009]
- [Edwards et al 1982][research_edwards_bennett_1982]
- [Edwards et al 1985][research_edwards_carter_1985]
- [Edwards et al 1986][research_edwards_carter_1986]
- [Edwards et al 1986][research_edwards_whitfield_1986]
- [Edwards et al 2001][research_edwards_schuster_2001]
- [Edwards et al 2009][research_edwards_spain_2009]
- [Effect of wind shear on the airspeed during the airplane landing approach 1990][research_effect_of_1990]
- [Efrati and Raveh 2026][research_efrati_raveh_2026]
- [Eghlima and Mansour 2017][research_eghlima_mansour_2017]
- [Egorov 2025][research_egorov_2025]
- [Ekaterinaris 2010][research_ekaterinaris_2010]
- [El-Naggar et al 2004][research_elnaggar_klamo_2004]
- [El-Sayed 2016][research_elsayed_2016]
- [Elbanna and Carlson 1989][research_elbanna_carlson_1989]
- [Eldern et al][research_eldern_vos]
- [Eldredge et al 2009][research_eldredge_wang_2009]
- [Eldridge-Allegra et al 2023][research_eldridgeallegra_xu_2023]
- [Eldridge-Allegra et al 2024][research_eldridgeallegra_roseman_2024]
- [Electronic autopilot controls supersonic flight 1956][research_electronic_autopilot_1956]
- [Elham and Timmer 2016][research_elham_timmer_2016]
- [Eliasson and Peng 2007][research_eliasson_peng_2007]
- [Eliasson and Peng 2008][research_eliasson_peng_2008]
- [Ellinwood 1967][research_ellinwood_1967]
- [Ellison and Latz 2003][research_ellison_latz_2003]
- [ElRamly][research_elramly]
- [Eminton and Lord 1956][research_eminton_lord_1956]
- [Enciu 2019][research_enciu_2019]
- [Energy Approach To Performance Flight Testing 2003][research_energy_approach_2003]
- [Engelbrecht][research_engelbrecht]
- [Englar 1970][research_englar_1970]
- [English 1955][research_englishrolandd_1955]
- [Eppink 2023][research_eppink_2023]
- [Eppler 2003][research_eppler_2003]
- [Epstein 1954][research_epstein_1954]
- [Epstein and Albers 1948][research_epstein_albers_1948]
- [Epstein et al 1989][research_epstein_luntz_1989]
- [Equations, tables, and charts 1953][research_naca_1135]
- [Erickson 1962][research_erickson_1962]
- [Erickson 1974][research_ericksonll_1974]
- [Erickson 1991][research_ericksongarye_1991]
- [Erickson and Gonzalez 2004][research_ericksongarye_gonzalezhugoa_2004]
- [Erickson and Gonzalez 2005][research_ericksongarye_gonzalezhugoa_2005]
- [Erickson and Rogers 1987][research_erickson_rogers_1987]
- [Erickson et al 1989][research_erickson_hall_1989]
- [Erickson et al 1989][research_erickson_schreiner_1989]
- [Erickson et al 1990][research_erickson_schreiner_1990]
- [Erickson et al 1990][research_erickson_schreiner_1990_b]
- [Ericsson 1970][research_ericssonle_1970]
- [Ericsson 1973][research_ericsson_1973]
- [Ericsson 1975][research_ericsson_1975]
- [Ericsson 1986][research_ericsson_1986]
- [Ericsson 1989][research_ericsson_1989]
- [Ericsson 1997][research_ericsson_1997]
- [Ertugrul and Koyuncu 2023][research_ertugrul_koyuncu_2023]
- [Essawy 1985][research_essawy_1985]
- [Estruch-Samper et al 2014][research_estruchsamper_vanstone_2014]
- [European Transonic Windtunnel Project 1990][research_european_transonic_1990]
- [Euvrard and Tournemine][research_euvrard_tournemine]
- [Evaluation of methods for prediction and prevention of wing/store flutter 1981][research_evaluation_of_1981]
- [Evangelista and Mori 2025][research_evangelista_mori_2025]
- [Evans 1987][research_evans_1987]
- [Everhart 1986][research_everhart_1986]
- [Everhart 1987][research_everhart_1987]
- [Everhart 1987][research_everhartjoell_1987]
- [Everhart 1988][research_everhartjoellee_1988]
- [Everhart and Barnwell 1978][research_everhart_barnwell_1978]
- [Everhart and Barnwell 1978][research_everhartjl_barnwellrw_1978]
- [Everhart and Bobbitt 1994][research_everhartjoell_bobbittpercyj_1994]
- [Everhart and Goradia 1988][research_everhart_goradia_1988]
- [Everhart and Goradia 1991][research_everhartjoell_goradiasureshh_1991]
- [Evers 1999][research_evers_1999]
- [Evers 2001][research_evers_2001]
- [Evers and Peake 1998][research_evers_peake_1998]
- [Eversman 1989][research_eversman_1989]
- [Experience Gained During Development and Testing of the First Swept-Wing Jet Aircraft 2010][research_experience_gained_2010]
- [Experimental Testing at Transonic Speeds 1982][research_experimental_testing_1982]
- [Experimental transonic flutter characteristics of supersonic cruise configurations 1990][research_experimental_transonic_1990]
- [Extension of FLO Codes to Transonic Flow Prediction for Fighter Configurations 1982][research_extension_of_1982]
- [Faber and Crane 1961][research_faberstanley_craneharoldl_1961]
- [Faber and Eggleston 1953][research_faberstanley_egglestonjohnm_1953]
- [Fagbade and Heinz 2024][research_fagbade_heinz_2024]
- [Falco 1991][research_falco_1991]
- [Famellos et al 2024][research_famellos_skevas_2024]
- [Fan 2013][research_fan_2013]
- [Fan et al 2005][research_fan_yi_2005]
- [Fan et al 2021][research_fan_yu_2021]
- [Fanning and Mueller 1978][research_fanning_mueller_1978]
- [Farbridge and Smith 1977][research_farbridge_smith_1977]
- [Farbridge and Smith 1978][research_farbridge_smith_1978]
- [Farhangnia et al 1996][research_farhangnia_guruswamy_1996]
- [Farhat 1998][research_farhat_1998]
- [Farhat 2000][research_farhat_2000]
- [Farhat 2001][research_farhat_2001]
- [Farrokhfal and Pishevar 2014][research_farrokhfal_pishevar_2014]
- [Farsadi et al 2019][research_farsadi_asadi_2019]
- [Fauci and Imperatore][research_fauci_imperatore]
- [Fauci et al 2006][research_fauci_nicoli_2006]
- [Fay and Riddell 1958][research_fay_riddell_1958]
- [Fediaevsky 1935][research_fediaevsky_1935]
- [Fedorov et al 1997][research_fedorov_malmuth_1997]
- [Fehrs and Helm 2025][research_fehrs_helm_2025]
- [Fei et al 2026][research_fei_wang_2026]
- [Fejtek 1994][research_fejtek_1994]
- [Feldhusen-Hoffmann et al 2017][research_feldhusenhoffmann_statnikov_2017]
- [Feng 2023][research_feng_2023]
- [Fenwick and Allen 2007][research_fenwick_allen_2007]
- [Ferman and Turner 1999][research_ferman_turner_1999]
- [Ferman and Turner 1999][research_ferman_turner_1999_b]
- [Fernandez et al 2018][research_fernandez_hoffmann_2018]
- [Ferrand and Aubert 1994][research_ferrand_aubert_1994]
- [Ferrara et al 2006][research_ferrara_consalvo_2006]
- [Ferrari 1962][research_ferrari_1962]
- [Ferrari et al 2021][research_ferrari_morais_2021]
- [Ferri and Baronti 1973][research_ferri_baronti_1973]
- [Ferris 1972][research_supercritical_17pct_1972]
- [Ferris 1973][research_ferrisjc_1973]
- [Ferris 1975][research_ferrisjc_1975]
- [Fertis 1988][research_fertis_1988]
- [Fetterman 1959][research_fettermandejr_1959]
- [Finaish et al 1995][research_finaish_frigerio_1995]
- [Finat'ev et al 1968][research_finatev_shcherbakov_1968]
- [Finch and Walker 1953][research_x5_stability_1953]
- [Fink 1971][research_fink_1971]
- [Firsov et al 2017][research_firsov_isaenkov_2017]
- [Firsov et al 2018][research_firsov_moralev_2018]
- [Fischel 1954][research_fischeljack_1954]
- [Fischel and Brunn 1954][research_fischeljack_brunncyrild_1954]
- [Fischel and Nugent 1953][research_longitudinal_accel_1953]
- [Fischel and Reisert 1956][research_fischeljack_reisertdonald_1956]
- [Fischel et al 1957][research_fischeljack_darvillerobertw_1957]
- [Fischenberg 1995][research_fischenberg_1995]
- [Fischer 2018][research_fischer_2018]
- [Fischer et al 1971][research_fischer_maddalon_1971]
- [Fishelov 1988][research_fishelov_1988]
- [Fisher 1969][research_fisherdf_1969]
- [Fisher 1978][research_fisherdf_1978]
- [Fisher and Cobleigh 1994][research_fisher_cobleigh_1994]
- [Fisher and Williams 1958][research_fisherlewisr_williamsjamesl_1958]
- [Fisher et al 1956][research_fisher_gertsen_1956]
- [Fisher et al 1990][research_fisher_banks_1990]
- [Fitzhugh 1970][research_fitzhugh_1970]
- [Fix 1980][research_fix_1980]
- [Flaszynski 2016][research_flaszynski_2016]
- [Flax 1973][research_flax_1973]
- [Flight Flutter Testing Symposium 1975][research_flutter_symposium_1975]
- [Flight-Loads Prediction and Structural-Life Management 1981][research_flight_loads_prediction_1981]
- [Flint and Niewoehner 2011][research_flint_niewoehner_2011]
- [Flores and Van Dalsem 1985][research_flores_vandalsem_1985]
- [Flores and Van Dalsem 1986][research_flores_vandalsem_1986]
- [Flores et al 1984][research_flores_holst_1984]
- [Florio et al 2019][research_florio_mckibbin_2019]
- [Fontaine and Ali 2023][research_fontaine_ali_2023]
- [Forsey 1983][research_forsey_1983]
- [Forster and Steijl 2015][research_forster_steijl_2015]
- [Fosdick 1970][research_fosdick_1970]
- [Foss and Swihart 1956][research_fosswejr_swihartjm_1956]
- [Foster and Cunningham 2010][research_foster_cunningham_2010]
- [Foughner and Bensinger 1977][research_foughnerjtjr_bensingerct_1977]
- [Fournis 2022][research_fournis_2022]
- [Fox and Woodward 1974][research_foxchj_woodwardfa_1974]
- [Fraenkel 1958][research_fraenkel_1958]
- [Fraenkel 1958][research_fraenkel_1958_b]
- [Francés et al 2024][research_frances_solerarico_2024]
- [Franks 1953][research_franksralphw_1953]
- [Franzmann et al 2022][research_franzmann_leopold_2022]
- [Fraser 1975][research_fraser_1975]
- [Freestone and Henington 1982][research_freestone_henington_1982]
- [French 1988][research_french_1988]
- [French et al 1987][research_french_noll_1987]
- [Freudinger and Kehoe 1990][research_freudingerlawrencec_kehoemichaelw_1990]
- [Freund 2014][research_freund_2014]
- [Frew et al 1993][research_frew_galassi_1993]
- [Friedewald 2020][research_friedewald_2020]
- [Friedlander et al][research_davidjfriedlander_nicholasjgeorgiadis]
- [Friehmelt and Jost 2000][research_friehmelt_jost_2000]
- [Friend and Sakamoto 1978][research_friendel_sakamotogm_1978]
- [Friend and Sefic 1972][research_f104_buffet_1972]
- [Fritz and Sackheim 1982][research_fritz_sackheim_1982]
- [Fritz et al 2025][research_fritz_patel_2025]
- [Frolov 2015][research_frolov_2015]
- [Fu 1995][research_fu_1995]
- [Fu and Liang 1991][research_fu_liang_1991]
- [Fu and Liang 1993][research_fu_liang_1993]
- [Fu et al 2023][research_fu_sun_2023]
- [Fu et al 2026][research_fu_feng_2026]
- [Fuchs 1981][research_fuchs_1981]
- [Fuehrer 1969][research_fuehrer_1969]
- [Fugate et al 2019][research_fugate_nguyen_2019]
- [Fuglsang and Williams 1985][research_fuglsang_williams_1985]
- [Fuhs 1971][research_fuhs_1971]
- [Fujii][research_fujii]
- [Fujii and Obayashi 1986][research_fujii_obayashi_1986]
- [Fujii and Obayashi 1987][research_fujii_obayashi_1987]
- [Fujino and Kawamura 2003][research_fujino_kawamura_2003]
- [Fujino and Suzuki 2024][research_fujino_suzuki_2024]
- [Fujiwara et al 2016][research_fujiwara_chaparro_2016]
- [Fukami et al 2004][research_fukami_higashino_2004]
- [Fukumoto et al 2023][research_fukumoto_kouchi_2023]
- [Fukushima and Kawai 2017][research_fukushima_kawai_2017]
- [Fukushima and Kawai 2017][research_fukushima_kawai_2017_b]
- [Fukushima and Kawai 2018][research_fukushima_kawai_2018]
- [Fukushima and Kawai 2019][research_fukushima_kawai_2019]
- [Fukushima et al 2020][research_fukushima_tamaki_2020]
- [Fulker and Ashill 1986][research_fulker_ashill_1986]
- [Fuller 1982][research_fullerde_1982]
- [Fuller and Williams 1986][research_fuller_williams_1986]
- [Fuller et al 1981][research_fullerde_glossbb_1981]
- [Fung 1982][research_fung_1982]
- [Fung 1982][research_fung_1982_b]
- [Fung and Shieh 1993][research_fung_shieh_1993]
- [Furlong and Fitzpatrick 1947][research_furlonggchester_fitzpatrickjamese_1947]
- [Fusi et al 2015][research_fusi_quaranta_2015]
- [Fuzaro Miotto and Wolf 2020][research_fuzaromiotto_wolf_2020]
- [G. The Experimental Aerodynamics of Wings at Transonic and Supersonic Speeds 1957][research_g_the_1957]
- [Gada and Rahai 2016][research_gada_rahai_2016]
- [Gada and Rahai 2023][research_gada_rahai_2023]
- [Gadsden and Habibi 2007][research_gadsden_habibi_2007]
- [Gageik et al 2018][research_gageik_nies_2018]
- [Gahlot and Singh 2021][research_gahlot_singh_2021]
- [Gallagher 1968][research_gallagher_1968]
- [Gallington and Miller 1970][research_gallington_miller_1970]
- [Gallman et al 1986][research_gallman_yang_1986]
- [Gallman et al 1988][research_gallman_batina_1988]
- [Gally 1994][research_gallythomasa_1994]
- [Gally and Carlson 1987][research_gally_carlson_1987]
- [Galyen et al 2014][research_galyen_mills_2014]
- [Gamble and Inman 2018][research_gamble_inman_2018]
- [Gambucci et al 1958][research_gambuccibj_sorensonrm_1958]
- [Ganesh 1994][research_ganesh_1994]
- [Gangeh et al 2023][research_gangeh_bui_2023]
- [Gao 2023][research_gao_2023]
- [Gao et al 2003][research_gao_luo_2003]
- [Gao et al 2017][research_gao_qu_2017]
- [Gao et al 2018][research_gao_qu_2018]
- [Gao et al 2018][research_gao_zhang_2018]
- [Gao et al 2019][research_gao_zhang_2019]
- [Gao et al 2021][research_gao_an_2021]
- [Gao et al 2025][research_gao_tyrrell_2025]
- [Garabedian 1964][research_garabedian_1964]
- [Garabedian 1974][research_garabedian_1974]
- [Garabedian 1976][research_wave_drag_computation_1976]
- [Garabedian 1994][research_garabedian_1994]
- [Garabedian and McFadden 1982][research_garabedianp_mcfaddeng_1982]
- [Garabedian and McFadden 1982][research_garabedianp_mcfaddeng_1982_b]
- [Garcia et al 2001][research_garcia_slingerland_2001]
- [Gardenier 1956][research_gardenier_1956]
- [Gardner 1978][research_gardner_1978]
- [Gardner and Curfman 1947][research_gardnerwilliamn_curfmanhowardjjr_1947]
- [Garnier and Deck 2010][research_garnier_deck_2010]
- [Garnier et al 2009][research_garnier_adams_2009]
- [Garrelick et al 1997][research_garrelick_martini_1997]
- [Garrell 2002][research_garrell_2002]
- [Garrell et al 2006][research_garrell_nowakowski_2006]
- [Garrick and Reed 1981][research_garrick_reed_1981]
- [Garriz et al 1990][research_garriz_newman_1990]
- [Gartenberg et al 1992][research_gartenberg_johnson_1992]
- [Gartner and Amitay 2015][research_gartner_amitay_2015]
- [Gartner and Amitay 2016][research_gartner_amitay_2016]
- [Gates and Sternfield 1950][research_gatesordwaybjr_sternfieldleonard_1950]
- [Gatski and Bonnet 2009][research_gatski_bonnet_2009]
- [Gatski and Bonnet 2013][research_gatski_bonnet_2013]
- [Gatski and Bonnet 2013][research_gatski_bonnet_2013_b]
- [Gautam and Prasad 2025][research_gautam_prasad_2025]
- [Ge and Gan 2026][research_ge_gan_2026]
- [Gea et al 1991][research_gea_chyu_1991]
- [Gebelein 1939][research_gebeleinh_1939]
- [Gee et al 1976][research_gee_jenks_1976]
- [Gee et al 2025][research_gee_olaveson_2025]
- [Geffen 1978][research_geffen_1978]
- [Geib and Maidnik 1983][research_geib_maidnik_1983]
- [Geissler 1997][research_geissler_1997]
- [Geissler 2003][research_geissler_2003]
- [Gelzer and Peebles 2015][research_hsfrs_rcs_2015]
- [General Electric Co Cincinnati Oh 1964][research_generalelectriccocincinnatioh_1964]
- [Geoghegan et al 2018][research_geoghegan_giannelis_2018]
- [Geoghegan et al 2020][research_geoghegan_giannelis_2020]
- [Geoghegan et al 2020][research_geoghegan_giannelis_2020_b]
- [George-Falvy 1971][research_georgefalvy_1971]
- [Georgiadis et al 2013][research_georgiadisnicholasj_vyasmanana_2013]
- [Georgiadis et al 2021][research_georgiadis_wernet_2021]
- [Georgiadis et al 2024][research_georgiadis_wernet_2024]
- [Gera 1986][research_gera_1986]
- [Gera et al 1981][research_gera_wilson_1981]
- [German 1975][research_german_1975]
- [German Development of the Swept Wing 1935-1945 2010][research_german_development_2010]
- [Gerolymos and Vallet 2003][research_gerolymos_vallet_2003]
- [Gerolymos et al 2003][research_gerolymos_sauret_2003]
- [Gerontakos and Lee 2007][research_gerontakos_lee_2007]
- [Ghaffari 2005][research_ghaffarifarhad_2005]
- [Ghate et al][research_adityasghate_gaetankkenway]
- [Ghate et al 2021][research_ghate_kenway_2021]
- [Ghayour and Baysal 1999][research_ghayour_baysal_1999]
- [Ghazi 1993][research_ghazi_1993]
- [Ghoreyshi et al 2013][research_ghoreyshi_cummings_2013]
- [Ghoreyshi et al 2017][research_ghoreyshi_darragh_2017]
- [Ghoreyshi et al 2024][research_ghoreyshi_aref_2024]
- [Ghoreyshi et al 2025][research_ghoreyshi_aref_2025]
- [Giannelis and Vio 2016][research_giannelis_vio_2016]
- [Giannelis et al 2019][research_giannelis_murray_2019]
- [Gibbings 1966][research_gibbings_1966]
- [Gibbons 1992][research_gibbons_1992]
- [Gibbons and Batina 1989][research_gibbons_batina_1989]
- [Gibbons and Batina 1990][research_gibbons_batina_1990]
- [Gibson et al 1957][research_x1e_flutter_1957]
- [Gibson et al 1958][research_gibsonfw_herrrw_1958]
- [Giepman et al 2015][research_giepman_srivastava_2015]
- [Giez et al 2016][research_giez_mallaun_2016]
- [Gilbarg and Shiffman 1954][research_gilbarg_shiffman_1954]
- [Giles and Drela 1986][research_giles_drela_1986]
- [Giles and Drela 1987][research_giles_drela_1987]
- [Gill et al 2016][research_gill_zhang_2016]
- [Gillan 1993][research_gillan_1993]
- [Gillan 1995][research_gillan_1995]
- [Gillard 1998][research_gillard_1998]
- [Gillard 1999][research_gillard_1999]
- [Gillespie 1960][research_gillespiewarrenjr_1960]
- [Gillespie and Arbic 1950][research_gillespiewarrenjr_arbicrichardg_1950]
- [Gillespie and Dietz 1952][research_gillespiewarrenjr_dietzalberte_1952]
- [Gilliam 1976][research_gilliam_1976]
- [Gilliot et al 2004][research_gilliot_monnier_2004]
- [Gillis and Mitchell 1957][research_gillisclarencel_mitchelljessel_1957]
- [Gillis et al 1950][research_gillisclarencel_peckrobertf_1950]
- [Gilman 1961][research_gilmanjjr_1961]
- [Gilyard and Orme 1992][research_gilyard_orme_1992]
- [Glagolev et al 2000][research_glagolev_zubkov_2000]
- [Glaser 1952][research_glaser_1952]
- [Glauert 1928][research_glauert_1928]
- [Glauert 1983][research_glauert_1983]
- [Glazkov and Semenov 2024][research_glazkov_semenov_2024]
- [Glazkov et al 2016][research_glazkov_gorbushin_2016]
- [Glezer 2009][research_glezer_2009]
- [Glezer 2012][research_glezer_2012]
- [Gloss 1984][research_gloss_1984]
- [Gloss 1992][research_gloss_1992]
- [Gloss and Washburn 1977][research_gloss_washburn_1977]
- [Gloss and Washburn 1978][research_gloss_washburn_1978]
- [Glowacki 1971][research_glowacki_1971]
- [Goal et al 2012][research_goal_sun_2012]
- [Goates et al 2025][research_goates_vandommelen_2025]
- [Goc et al 2023][research_goc_agrawal_2023]
- [Goc et al 2025][research_goc_agrawal_2025]
- [Godavarthi et al 2026][research_godavarthi_seo_2026]
- [Godwin et al 1964][research_godwin_frazier_1964]
- [Goenka 1994][research_goenka_1994]
- [Goethert 1956][research_goethert_1956]
- [Goethert and Lukasiewicz 1963][research_goethert_lukasiewicz_1963]
- [Goetz 1972][research_goetzrc_1972]
- [Goetz and Stonesifer 1961][research_goetzrc_stonesiferjc_1961]
- [Goffert et al 2014][research_goffert_ortega_2014]
- [Goffert et al 2015][research_goffert_ortega_2015]
- [Goffert et al 2016][research_goffert_ortega_2016]
- [Goh 2008][research_goh_2008]
- [Goland et al 1954][research_goland_luke_1954]
- [Goldberg and Reshotko 1980][research_goldbergu_reshotkoe_1980]
- [Goldberg et al 1985][research_goldberg_gorski_1985]
- [Goldhammer and Steinle 1990][research_goldhammermarki_steinlefrankwjr_1990]
- [Goldstein 2004][research_goldstein_2004]
- [Golestani et al 2017][research_golestani_soltani_2017]
- [Golubev et al 2010][research_golubev_hollenshade_2010]
- [Gompertz et al 2012][research_gompertz_jensen_2012]
- [Goncalves et al 2003][research_goncalves_robinet_2003]
- [Gong and Zhang 2025][research_gong_zhang_2025]
- [Gong et al 2024][research_gong_gao_2024]
- [Gong et al 2024][research_gong_wang_2024]
- [Gonsalez and Dolling 1993][research_gonsalez_dolling_1993]
- [Gonzalez et al 2026][research_gonzalez_ilie_2026]
- [Goodheart et al 2003][research_goodheart_dykas_2003]
- [Goodman 1973][research_goodman_1973]
- [Goodman et al 1985][research_goodmanwl_morrisetteel_1985]
- [Goodrich and Sliwa 1987][research_goodrich_sliwa_1987]
- [Goodrich et al 1983][research_goodrich_derry_1983]
- [Goodwin et al 1967][research_goodwinfk_lynesll_1967]
- [Goodyear Aerospace Corp Akron Oh 1958][research_goodyearaerospacecorpakronoh_1958]
- [Goodyer and Wolf 1980][research_goodyer_wolf_1980]
- [Goorjian 1984][research_goorjian_1984]
- [Goorjian and Buskirk 1985][research_goorjian_buskirk_1985]
- [Goorjian and Obayashi 1989][research_goorjianpeterm_obayashishigeru_1989]
- [Goorjian and Obayashi 1990][research_goorjianpeterm_obayashishigeru_1990]
- [Goorjian et al 1983][research_goorjian_meagher_1983]
- [Gopalarathnam and McAvoy 2001][research_gopalarathnam_mcavoy_2001]
- [Gopesh. M. P and Manivel. M 2016][research_gopeshmp_manivelm_2016]
- [Goradia and Bobbitt 1988][research_goradiash_bobbittpj_1988]
- [Goradia et al 1989][research_goradiash_bobbittpj_1989]
- [Gordnier and Melville 1998][research_gordnier_melville_1998]
- [Gordnier and Melville 2000][research_gordnier_melville_2000]
- [Gorski 1998][research_gorski_1998]
- [Goupil][research_goupil]
- [Goushcha and Sekula][research_oleggoushcha_martinksekula]
- [Goushcha and Sekula 2025][research_goushcha_sekula_2025]
- [Graham 1947][research_grahamdonaldj_1947]
- [Graham 1948][research_grahamdonaldj_1948]
- [Graham 1949][research_grahamdonaldj_1949]
- [Graham and Koenig 1951][research_grahamdavid_koenigdavidg_1951]
- [Graham and Koenig 1952][research_grahamdavid_koenigdavidg_1952]
- [Graham et al 1945][research_grahamdonaldj_nitzberggeralde_1945]
- [Graham et al 1954][research_graham_lagerstrom_1954]
- [Gramann and Dolling 1987][research_gramann_dolling_1987]
- [Grant and Robinson 1953][research_grantfrederickc_robinsonrossb_1953]
- [Grant and Sevier 1960][research_grantfrederickc_sevierjohnrjr_1960]
- [Graphs of Critical Mach Number 2014][research_graphs_of_2014]
- [Grasso and Falconi 1993][research_grasso_falconi_1993]
- [Gratton 2014][research_gratton_2014]
- [Gratton 2018][research_gratton_2018]
- [Grauer and Boucher][research_jaredagrauer_matthewjboucher]
- [Grauer and Morelli 2023][research_grauer_morelli_2023]
- [Grauer and Waite][research_jaredagrauer_josiahmwaite]
- [Gray 2008][research_gray_2008]
- [Gray 2016][research_gray_2016]
- [Green 2008][research_green_2008]
- [Green and Fernandez 1994][research_green_fernandez_1994]
- [Green and Newman 1987][research_greenlawrencel_newmanperrya_1987]
- [Green and Newman 1991][research_greenlawrencel_newmanperrya_1991]
- [Greene 1957][research_greene_1957]
- [Greene 1958][research_greenelp_1958]
- [Greenwell 2021][research_greenwell_2021]
- [Gregg and Misegades 1987][research_gregg_misegades_1987]
- [Gregory et al 2011][research_gregory_xargay_2011]
- [Griffin and Jonas 1983][research_griffin_jonas_1983]
- [Griffiths and Visser 2000][research_griffiths_visser_2000]
- [Grigsby 1954][research_grigsbycarle_1954]
- [Grismer et al 2000][research_grismer_kinsey_2000]
- [Grohmann et al 1999][research_grohmann_kroplin_1999]
- [Grosdemange and Schaeffer 1990][research_grosdemange_schaeffer_1990]
- [Gross and Steinle 1975][research_grossar_steinlefwjr_1975]
- [Gross et al 1986][research_gross_chandler_1986]
- [Grosser 1965][research_grosser_1965]
- [Grosser et al 1983][research_grosserwf_brittrt_1983]
- [Grossi][research_grossi]
- [Grossi et al 2012][research_grossi_braza_2012]
- [Grossi et al 2014][research_grossi_braza_2014]
- [Grossman and Volpe 1977][research_grossman_volpe_1977]
- [Grossman and Volpe 1977][research_grossman_volpe_1977_b]
- [Grosvenor et al 2012][research_grosvenor_zheltovodov_2012]
- [Grund and Konarski 1971][research_grund_konarski_1971]
- [Grunnet 1984][research_grunnet_1984]
- [Guan 2013][research_guan_2013]
- [Guan 2014][research_guan_2014]
- [Guan 2014][research_guan_2014_b]
- [Guangyuan et al 2021][research_guangyuan_dawei_2021]
- [Guderley 1956][research_guderley_1956]
- [Guderley 1980][research_guderley_1980]
- [Guderley 1982][research_guderley_1982]
- [Guderley 1983][research_guderley_1983]
- [Guderley and Clemm 1979][research_guderley_clemm_1979]
- [Gudilin et al 1996][research_gudilin_lashkov_1996]
- [Guilarte Herrero et al 2021][research_guilarteherrero_noguchi_2021]
- [Guiler][research_guiler]
- [Gumbert and Newman 1984][research_gumbert_newman_1984]
- [Gumbert et al 1989][research_gumbertclyder_greenlawrencel_1989]
- [Gunn 1966][research_gunn_1966]
- [Gunn 1970][research_gunn_1970]
- [Guo et al 1988][research_guo_wang_1988]
- [Guo et al 2022][research_guo_zhang_2022]
- [Guo et al 2025][research_guo_wang_2025]
- [Gupta][research_gupta]
- [Gupta and Ansell 2018][research_gupta_ansell_2018]
- [Gupta et al 2021][research_gupta_datta_2021]
- [Gurbacki and Bragg 1999][research_gurbacki_bragg_1999]
- [Gurbacki and Bragg 2001][research_gurbacki_bragg_2001]
- [Gurley and Ruhlin 1962][research_gurleyjrjr_ruhlincl_1962]
- [Guruswamy and Goorjian 1987][research_guruswamy_goorjian_1987]
- [Guruswamy and Goorjian 1988][research_guruswamy_goorjian_1988]
- [Guruswamy and Tu 1988][research_guruswamy_tu_1988]
- [Guruswamy and Tu 1989][research_guruswamy_tu_1989]
- [Guy et al 1999][research_guy_morrow_1999]
- [Guy et al 2001][research_guy_mclaughlin_2001]
- [Gülçat 2010][research_gulcat_2010]
- [Gülçat 2015][research_gulcat_2015]
- [Gülçat 2021][research_gulcat_2021]
- [Gürdamar et al 2006][research_gurdamar_cete_2006]
- [Hackett 2000][research_hackett_2000]
- [Hacıogˇlu and Özkol 2003][research_hacioglu_ozkol_2003]
- [Hader and Fasel 2023][research_hader_fasel_2023]
- [Haderlie and Crossley 2009][research_haderlie_crossley_2009]
- [Hadjadj and Dussauge 2009][research_hadjadj_dussauge_2009]
- [Hafez 1982][research_hafez_1982]
- [Hafez 1985][research_hafezmm_1985]
- [Hafez 1999][research_hafez_1999]
- [Hafez and Cheng 1975][research_hafez_cheng_1975]
- [Hafez and Cheng 1977][research_hafez_cheng_1977]
- [Hafez and Lovell 1984][research_hafez_lovell_1984]
- [Hafez and Wahba][research_hafez_wahba]
- [Hagen and Seidel][research_hagen_seidel]
- [Hager et al 1992][research_hager_eyi_1992]
- [Hager et al 1993][research_hager_eyi_1993]
- [Hager et al 1994][research_hager_eyi_1994]
- [Haglund and Kane 1973][research_haglundgt_kaneej_1973]
- [Haglund and Kane 1974][research_haglund_kane_1974]
- [Haglund and Kane 1974][research_haglundgt_kaneej_1974]
- [Haines 1957][research_haines_1957]
- [Haines 1990][research_haines_1990]
- [Haines 2000][research_haines_2000]
- [Hakkinen et al 1959][research_hakkinenrj_greberi_1959]
- [Halder et al 2019][research_halder_damodaran_2019]
- [Hall 1978][research_hall_1978]
- [Hall 1978][research_hallrm_1978]
- [Hall 1985][research_hall_1985]
- [Hall and Kern 1996][research_hall_kern_1996]
- [Hall et al 1953][research_halljr_hopkorn_1953]
- [Hall et al 1989][research_hall_carraway_1989]
- [Hall et al 2011][research_hall_atassi_2011]
- [Hamed 1993][research_hamed_1993]
- [Hamed and Mohamed 2001][research_hamed_mohamed_2001]
- [Hamed et al 1992][research_hameda_shihsh_1992]
- [Hamed et al 1993][research_hameda_yeuanjj_1993]
- [Hamer and Mayo 1953][research_f84g_squadron_1953]
- [Hamid and Hasan 2015][research_hamid_hasan_2015]
- [Hammer and Olivier 2019][research_hammer_olivier_2019]
- [Hammerton and Kerschen 1998][research_hammertonpw_kerschenej_1998]
- [Han et al 2016][research_han_chen_2016]
- [Han et al 2022][research_han_xu_2022]
- [Han et al 2023][research_han_liu_2023]
- [Handa et al 2003][research_handa_masuda_2003]
- [Hanel et al 2004][research_hanel_neuhuber_2004]
- [Haney et al 1979][research_haney_johnson_1979]
- [Hanly 1974][research_hanly_1974]
- [Hanman et al 2025][research_hanman_yao_2025]
- [Hansen 1976][research_hansen_1976]
- [Hanson 1959][research_hansonpw_1959]
- [Hanson 1989][research_hanson_1989]
- [Hanson and Fink 1978][research_hansondb_finkmr_1978]
- [Hanumantharayappa et al 2022][research_hanumantharayappa_thantanapally_2022]
- [Hara and Abe 2008][research_hara_abe_2008]
- [Harbeck and Jameson 2005][research_harbeck_jameson_2005]
- [Hares et al 2026][research_hares_brioua_2026]
- [Harmon 1945][research_allmovable_comparison_1945]
- [Harper et al 2025][research_harper_mishra_2025]
- [Harris 1975][research_charlesdharris_1975]
- [Harris et al 1989][research_harrischarlesd_brookscuylerwjr_1989]
- [Harrison et al 2016][research_harrison_darragh_2016]
- [Hart 1984][research_hart_1984]
- [Hart and Schmitz 2022][research_hart_schmitz_2022]
- [Hartley and Jacocks 1968][research_hartley_jacocks_1968]
- [Hartmann 2012][research_hartmann_2012]
- [Hartmann 2013][research_hartmann_2013]
- [Hartmann et al 1979][research_hartmann_stein_1979]
- [Hartmann et al 2013][research_hartmann_feldhusen_2013]
- [Hartwich 1991][research_hartwich_1991]
- [Hartzuiker 1986][research_hartzuiker_1986]
- [Harun and Amer Abbas 2024][research_harun_amerabbas_2024]
- [Harvey and Bobbitt 1981][research_harvey_bobbitt_1981]
- [Harvey and Pride 1982][research_harveywd_pridejd_1982]
- [Haryanto et al 2014][research_haryanto_utomo_2014]
- [Hasalli Hj Ibrahim et al 2019][research_hasallihjibrahim_dzulhelmybinamari_2019]
- [Hasan and Alam 2013][research_hasan_alam_2013]
- [Hasan and Alam 2014][research_hasan_alam_2014]
- [Hasan et al 2012][research_hasan_matsuo_2012]
- [Hasegawa and Sakaue 2017][research_hasegawa_sakaue_2017]
- [Hasel and Coletti 1948][research_pitot_supersonic_1948]
- [Haselton and Goode][research_haselton_goode]
- [Hashimoto et al 2010][research_hashimoto_aoyama_2010]
- [Hashimoto et al 2011][research_hashimoto_kohzai_2011]
- [Hass et al 2024][research_hass_housman_2024]
- [Hassan and Sobieczky 1981][research_hassan_sobieczky_1981]
- [Hastings 1954][research_hastings_1954]
- [Hastings and Mitcham 1954][research_hastingsearlc_mitchamgradyl_1954]
- [Hataue 1991][research_hataue_1991]
- [Hatayama et al 2025][research_hatayama_tanaka_2025]
- [Haupt et al 1985][research_haupt_buff_1985]
- [Hawke 2026][research_hawke_2026]
- [Hawthorne 1976][research_hawthornepj_1976]
- [Haxter and Spehr 2018][research_haxter_spehr_2018]
- [Hayabe and Kwak 2025][research_hayabe_kwak_2025]
- [Hayashi and Aso 1988][research_hayashi_aso_1988]
- [Hayes 1968][research_hayesc_1968]
- [He and Cui 2022][research_he_cui_2022]
- [He and Williams 2022][research_he_williams_2022]
- [He and Williams 2023][research_he_williams_2023]
- [He et al 2014][research_he_yang_2014]
- [He et al 2016][research_he_yang_2016]
- [He et al 2020][research_he_song_2020]
- [He et al 2021][research_he_wang_2021]
- [Heath 2014][research_heath_2014]
- [Hecht 2009][research_hecht_2009]
- [Heeg and Chwalowski 2017][research_heeg_chwalowski_2017]
- [Heeg and Chwalowski 2019][research_heegjennifer_chwalowskipawel_2019]
- [Hegde et al 2015][research_hegde_funderburk_2015]
- [Heidebrecht 2006][research_heidebrecht_2006]
- [Heidebrecht 2013][research_heidebrecht_2013]
- [Heim 1991][research_heim_1991]
- [Heineck et al 2016][research_heineck_banks_2016]
- [Held and Fuchs 1998][research_held_fuchs_1998]
- [Held and Fuchs 1999][research_held_fuchs_1999]
- [Held and Fuchs 1999][research_held_fuchs_1999_b]
- [Heller et al 2006][research_heller_holmberg_2006]
- [Hellstrom et al 1994][research_hellstrom_davidson_1994]
- [Helm et al 2024][research_helm_grabe_2024]
- [Heltsley and Cline 1979][research_heltsley_cline_1979]
- [Heltsley et al 1981][research_heltsley_crosswy_1981]
- [Hemsch 1988][research_hemsch_1988]
- [Hemsch and Iyer 2004][research_hemschmichaelj_iyervenkit_2004]
- [Hendershot 1968][research_hendershot_1968]
- [Hendershot 1969][research_hendershot_1969]
- [Henderson 1957][research_x1e_lateral_1957]
- [Henderson 1990][research_henderson_1990]
- [Henderson 1991][research_henderson_1991]
- [Henderson et al 1952][research_f86_squadron_1952]
- [Henne 1980][research_henne_1980]
- [Henne 1981][research_henne_1981]
- [Henne and Hicks 1978][research_henne_hicks_1978]
- [Henne and Hicks 1978][research_hennepa_hicksrm_1978]
- [Henning 1954][research_henningallenb_1954]
- [Henning 1957][research_henningallenb_1957]
- [Hensel 1964][research_hensel_1964]
- [Herbert 1973][research_herbert_1973]
- [Hergert and Bengelink 1984][research_hergert_bengelink_1984]
- [Hergert et al 2001][research_hergert_smith_2001]
- [Hermann 1950][research_hermann_1950]
- [Hermes et al 2008][research_hermes_klioutchnikov_2008]
- [Hermes et al 2012][research_hermes_nies_2012]
- [Hermes et al 2013][research_hermes_klioutchnikov_2013]
- [Heron and Myose 2007][research_heron_myose_2007]
- [Herr et al 2023][research_herr_spinner_2023]
- [Herring 2008][research_herring_2008]
- [Hersch 1970][research_hersch_1970]
- [Hess 1989][research_hessrw_1989]
- [Hess and Gardner 1949][research_hessrobertv_gardnercliffords_1949]
- [Hess et al 1987][research_hess_seidel_1987]
- [Hess et al 1989][research_hess_seidel_1989]
- [Hewes and Hassell 1960][research_hewesdonalde_hasselljamesljr_1960]
- [Hewlett 1987][research_hewlett_1987]
- [Heyson 1961][research_heyson_1961]
- [Hickey et al 2016][research_hickey_hussain_2016]
- [Hicks 1981][research_hicks_1981]
- [Hicks and Moulton 1988][research_hicks_moulton_1988]
- [Hicks and Petersen 1988][research_hicksjohnw_petersenkevinl_1988]
- [Hicks and Petersen 1989][research_hicksjohnw_petersenkevinl_1989]
- [Hicks et al 1987][research_hicksjohnw_kaniajan_1987]
- [Hicks et al 1987][research_johnwhicks_jankania_1987]
- [Hieser and Reid 1954][research_hiesergerald_reidcharlesf_1954]
- [Hieser et al 1956][research_hiesergerald_kudlaciklouis_1956]
- [Hillenherms et al 2001][research_hillenherms_schroeder_2001]
- [Hillenherms et al 2004][research_hillenherms_schroder_2004]
- [Hiller et al][research_bretthiller_richardcampbell]
- [Hiller et al][research_brettrhiller_richardlcampbell]
- [Hiller et al][research_brettrhiller_richardlcampbell_b]
- [Hiller et al 2021][research_hiller_campbell_2021]
- [Hiller et al 2024][research_slotted_nlf_2024]
- [Hiller et al 2025][research_hiller_campbell_2025]
- [Hillier and Netterfield 1990][research_hillier_netterfield_1990]
- [Hillje and Nelson 1981][research_hillje_nelson_1981]
- [Hillje and Tymms 1978][research_hillje_tymms_1978]
- [Hinchliffe and Qin 2016][research_hinchliffe_qin_2016]
- [Hinchliffe and Qin 2017][research_hinchliffe_qin_2017]
- [Hindash and Spaid 1991][research_hindash_spaid_1991]
- [Hindman 1992][research_hindman_1992]
- [Hingst and Jurkovich 1982][research_hingstwr_jurkovichm_1982]
- [Hingst and Tanji 1983][research_hingstwr_tanjift_1983]
- [Hirose and Miwa 1989][research_hirose_miwa_1989]
- [Hirose et al 1985][research_hirose_takanashi_1985]
- [Hirose et al 1987][research_hirose_takanashi_1987]
- [Hirt 2015][research_hirtstefaniem_2015]
- [Hirt and Vyas 2013][research_hirtstefaniem_vyasmanana_2013]
- [History of Supersonic Transport Aircraft Development 2020][research_history_of_2020]
- [Hitachi and Liu 2010][research_hitachi_liu_2010]
- [Hitch 1981][research_hitch_1981]
- [Hitzel 2015][research_hitzel_2015]
- [Hitzel 2017][research_hitzel_2017]
- [Hitzel 2017][research_hitzel_2017_b]
- [Hoang and Bui 2019][research_hoang_bui_2019]
- [Hoang et al 1993][research_hoang_rediniotis_1993]
- [Hoe et al 2012][research_hoe_owens_2012]
- [Hoff 2007][research_hoff_2007]
- [Hoffman 1958][research_hoffmans_1958]
- [Holdaway 1954][research_drag_rise_reduction_1954]
- [Holdaway 1955][research_holdawaygeorgeh_1955]
- [Holdaway and Hatfield 1957][research_holdawaygeorgeh_hatfieldelainew_1957]
- [Holdaway and Mellenthin 1960][research_holdawaygeorgeh_mellenthinjacka_1960]
- [Holdaway and Mellenthin 1960][research_holdawaygeorgeh_mellenthinjacka_1960_b]
- [Holdaway et al 1959][research_holdawaygeorgeh_mellenthinjacka_1959]
- [Holden 1966][research_holdenms_1966]
- [Holden et al 2013][research_holden_wadhams_2013]
- [Holder 1963][research_holder_1963]
- [Hollingsworth and Cohen 1971][research_hollingsworth_cohen_1971]
- [Holmes et al 1986][research_holmes_croom_1986]
- [Holst 1981][research_holst_1981]
- [Holst 1987][research_holst_1987]
- [Holst 1988][research_holst_1988]
- [Holst 1999][research_holst_1999]
- [Holst and Bock][research_holst_bock]
- [Holst and Thomas 1982][research_holst_thomas_1982]
- [Holt 1982][research_holt_1982]
- [Honaker 1982][research_honakerwc_1982]
- [Hong and Jung 2024][research_hong_jung_2024]
- [Hong et al 1995][research_hong_ahn_1995]
- [Hood and Anderson 1942][research_hoodmanleyj_andersonjosephl_1942]
- [Hooker 1931][research_hooker_1931]
- [Hooker 2014][research_hooker_2014]
- [Hope and Kunz 2019][research_hope_kunz_2019]
- [Horibata 2001][research_horibata_2001]
- [Horizontal Tail Loads 1996][research_horizontal_tail_1996]
- [Hornung and Elsenaar 1988][research_hornung_elsenaar_1988]
- [Horstman 1982][research_horstman_1982]
- [Horstman 1983][research_horstman_1983]
- [Horstman et al 1985][research_horstmancc_kussoymi_1985]
- [Horstmann et al 1990][research_horstmann_quast_1990]
- [Hortsen et al 1983][research_hortsen_boer_1983]
- [Hoshi et al 2020][research_hoshi_kuya_2020]
- [Hou et al 1995][research_hounkateshwar_taylor_1995]
- [Hou et al 2003][research_hou_clemens_2003]
- [Houtman et al 2023][research_houtman_timme_2023]
- [Houtman et al 2023][research_houtman_vevek_2023]
- [Howard and Bray 1992][research_howard_bray_1992]
- [Howell 1980][research_howell_1980]
- [Howell and Braslow 1955][research_howellrobertr_braslowalbertl_1955]
- [Howell and Korst 1971][research_drag_rise_notches_1971]
- [Hoyt 2006][research_hoyt_2006]
- [Hsieh 1975][research_hsieh_1975]
- [Hsieh 1975][research_hsieh_1975_b]
- [Hsiung and Chow 1993][research_hsiung_chow_1993]
- [Hsiung et al 1997][research_hsiung_onn_1997]
- [Hsu 1987][research_hsu_1987]
- [Hsu 1988][research_hsu_1988]
- [Hsu and Anderson 1961][research_hsu_anderson_1961]
- [Hsu and Liu 1990][research_hsuch_liuch_1990]
- [Hu 1992][research_hu_1992]
- [Hu 1995][research_hu_1995]
- [Hu 2023][research_hu_2023]
- [Hu and Kandil 1990][research_hu_kandil_1990]
- [Hu et al 2011][research_hu_zhao_2011]
- [Hu et al 2018][research_hu_qu_2018]
- [Hu et al 2024][research_hu_lu_2024]
- [Hu et al 2024][research_hu_zhu_2024]
- [Hu et al 2025][research_hu_huang_2025]
- [Huan and Modi 1995][research_huan_modi_1995]
- [Huang et al 2001][research_huang_folk_2001]
- [Huang et al 2026][research_huang_liang_2026]
- [Hubbard et al 2011][research_hubbard_mcfarland_2011]
- [Hubbard et al 2014][research_hubbard_fontenot_2014]
- [Hube 1978][research_hube_1978]
- [Hue and Molton 2020][research_hue_molton_2020]
- [Huerta 1969][research_huerta_1969]
- [Huff et al 1987][research_huff_wu_1987]
- [Hughes and Mennell 1974][research_hughesmt_mennellrc_1974]
- [Hui and Collins 2001][research_hui_collins_2001]
- [Huijts and Voskuijl 2015][research_huijts_voskuijl_2015]
- [Humphries et al 1998][research_humphries_gillan_1998]
- [Hung 1989][research_hungchingmao_1989]
- [Hung 1990][research_hungchingmao_1990]
- [Hung and Buning 1984][research_hungcm_buningpg_1984]
- [Hung and Buning 1985][research_hungchingmao_buningpieterg_1985]
- [Hung and Maccormack 1978][research_hungcm_maccormackrw_1978]
- [Hunn 1953][research_hunn_1953]
- [Hunter and Reeder 1946][research_spring_tab_1946]
- [Hunziker 1960][research_hunziker_1960]
- [Huo et al 2026][research_huo_wang_2026]
- [Hurley 1975][research_hurley_1975]
- [Hurley et al 1975][research_hurleyfx_spaidfw_1975]
- [Hurt and Whitten 1960][research_pitchup_control_1960]
- [Husain et al 2026][research_husain_piotrowski_2026]
- [Huse 1948][research_huse_1948]
- [Hussaini et al 1980][research_hussainimy_baldwinbs_1980]
- [Hussein and Chudoba 2016][research_hussein_chudoba_2016]
- [Huttsell et al 1976][research_huttselllj_nollte_1976]
- [Hwang and Park 2026][research_hwang_park_2026]
- [Hwang and Pi 1975][research_hwang_pi_1975]
- [Hwang and Pi 1975][research_hwang_pi_1975_b]
- [Hwang and Pi 1979][research_hwang_pi_1979]
- [Hwang et al 1991][research_hwang_chen_1991]
- [Hybrid Approach to Transonic Inviscid Flow with Moderate to Strong Shock Wave 1982][research_hybrid_approach_1982]
- [Ibrahim and Filippone 2006][research_ibrahim_filippone_2006]
- [Ibrahim and Filippone 2007][research_ibrahim_filippone_2007]
- [Ice and Rain Minimum Qualification Standards for Pitot and Pitot-static Probes][research_ice_and]
- [Illi et al 2013][research_illi_fingskes_2013]
- [Imai 1952][research_imai_1952]
- [Imai et al 2021][research_imai_nakakita_2021]
- [Imai et al 2022][research_imai_nakakita_2022]
- [Imig 1973][research_imig_1973]
- [in't Veld Alexander and Karwal Arun 2012][research_intveldalexanderc_karwalarunk_2012]
- [In-Flight Thrust Determination][research_in_flight_thrust_b]
- [In-Flight Thrust Determination for Aircraft with Thrust Vectoring][research_in_flight_thrust]
- [Inger 1976][research_inger_1976]
- [Inger 1979][research_inger_1979]
- [Inger 1979][research_inger_1979_b]
- [Inger 1981][research_inger_1981]
- [Inger 1982][research_inger_1982]
- [Inger 1983][research_inger_1983]
- [Inger 1983][research_inger_1983_b]
- [Inger 1984][research_inger_1984]
- [Inger 1985][research_inger_1985]
- [Inger 1988][research_inger_1988]
- [Inger 1988][research_inger_1988_b]
- [Inger 1991][research_inger_1991]
- [Inger 2011][research_inger_2011]
- [Inger and Kayser 1983][research_inger_kayser_1983]
- [Inger and Mason 1976][research_inger_mason_1976]
- [Inger and Mason 1976][research_inger_mason_1976_b]
- [Inger and Nandanan 1986][research_inger_nandanan_1986]
- [Inger et al 1997][research_inger_gendt_1997]
- [Initial flight test of a ground deployed system for flying qualitiesassessment 1989][research_initial_flight_1989]
- [Integral Equation Method in Transonic Flow 1982][research_integral_equation_1982]
- [Inverse Airfoil Design A Classical Approach Updated for Transonic Applications 1990][research_inverse_airfoil_1990]
- [Investigation of flexible nozzle wall-flutter incidents in the NASA-Ames Research Center 11- by 11-foot transonic wind tunnel 1979][research_investigation_of_1979]
- [Irfan et al 2026][research_irfan_nanangburhan_2026]
- [Ishida and Ueshima 2026][research_ishida_ueshima_2026]
- [Ishida et al 2016][research_ishida_ishiko_2016]
- [Ishida et al 2017][research_ishida_hashimoto_2017]
- [Ishii and Yanagizawa 1967][research_ishiit_yanagizawam_1967]
- [Ishikawa et al 2007][research_ishikawa_kwak_2007]
- [Ishikawa et al 2008][research_ishikawa_kwak_2008]
- [Ishrak et al 2024][research_ishrak_shuvo_2024]
- [Isogai 1979][research_isogai_1979]
- [Isogai 1981][research_isogai_1981]
- [Isogai 2016][research_isogai_2016]
- [Isogai 2024][research_isogai_2024]
- [Item and Baysal 1995][research_itemcemc_baysaloktay_1995]
- [Ito and Takanashi 1991][research_ito_takanashi_1991]
- [Iwai 2018][research_iwai_2018]
- [Iwai et al 2019][research_iwai_suzuki_2019]
- [Iwatani et al 2022][research_iwatani_asada_2022]
- [Iyer and Takahashi 2025][research_iyer_takahashi_2025]
- [Iyer et al 2004][research_iyer_kuhl_2004]
- [Iyer et al 2017][research_iyer_park_2017]
- [Izumi et al 2015][research_izumi_ogino_2015]
- [Jabbar et al 2026][research_jabbar_setiawan_2026]
- [Jackson 1976][research_jackson_1976]
- [Jackson 1978][research_jackson_1978]
- [Jackson et al 1978][research_jacksonlr_kirkhamfs_1978]
- [Jacobs et al 1939][research_jacobsen_abbottirah_1939]
- [Jacobs et al 2002][research_jacobs_kopriva_2002]
- [Jacobs et al 2012][research_jacobs_ran_2012]
- [Jacobson and Stanford][research_kevinejacobson_bretkstanford_b]
- [Jacobson et al][research_kevinejacobson_bretkstanford]
- [Jacobson et al 2021][research_jacobson_stanford_2021]
- [Jacocks 1969][research_jacocks_1969]
- [Jacocks 1969][research_jacocks_1969_b]
- [Jacocks 1970][research_jacocks_1970]
- [Jacocks and Hartley 1969][research_jacocks_hartley_1969]
- [Jacquin et al 2005][research_jacquin_molton_2005]
- [Jacquin et al 2009][research_jacquin_molton_2009]
- [Jaeger et al 2026][research_jaeger_thome_2026]
- [Jaffe 1972][research_jaffe_1972]
- [Jaffe 1975][research_jaffep_1975]
- [Jagharghi et al 1995][research_jagharghi_cler_1995]
- [Jain 1988][research_jain_1988]
- [James 1981][research_jamesjr_1981]
- [James 1998][research_james_1998]
- [Jameson][research_jameson]
- [Jameson][research_jameson_b]
- [Jameson 1973][research_jameson_1973]
- [Jameson 1977][research_jameson_1977]
- [Jameson 1979][research_jamesona_1979]
- [Jameson 1982][research_jameson_1982]
- [Jameson and Caughey 1977][research_jameson_caughey_1977]
- [Jameson and Caughey 1977][research_jamesona_caugheyda_1977]
- [Jameson et al 2008][research_jameson_vassberg_2008]
- [Janardhan and Grandhi 2003][research_janardhan_grandhi_2003]
- [Janardhan et al 2003][research_janardhan_grandhi_2003_b]
- [Jankiewicz 2026][research_jankiewicz_2026]
- [Jansen et al 2024][research_jansen_glockner_2024]
- [Jansen et al 2025][research_jansen_glockner_2025]
- [Jarvinen 2013][research_jarvinen_2013]
- [Jayachandran et al 1987][research_jayachandran_bhanu_1987]
- [Jegdi 'c 2019][research_jegdic_2019]
- [Jenkins 1983][research_jenkinsrv_1983]
- [Jenkins 1983][research_jenkinsrv_1983_b]
- [Jenkins 1986][research_jenkins_1986]
- [Jenkins 1986][research_jenkinsrv_1986]
- [Jenkins 1989][research_jenkinsrenaldov_1989]
- [Jenkins et al 1984][research_jenkinsrv_johnsonwgjr_1984]
- [Jenkins et al 1988][research_jenkinsrenaldov_hillacquillas_1988]
- [Jenney et al 1982][research_jenney_schreadley_1982]
- [Jente 2022][research_jente_2022]
- [Jeon et al 2014][research_jeon_kim_2014]
- [Jepps 1981][research_jepps_1981]
- [Jesudasan et al 2026][research_jesudasan_doherty_2026]
- [Jet Thrust Measurement In Flight 2003][research_jet_thrust_2003]
- [Jettmar 1984][research_jettmar_1984]
- [Jewell et al 2013][research_jewell_shepherd_2013]
- [Ji and Liu 1996][research_ji_liu_1996]
- [Ji et al 2024][research_ji_huang_2024]
- [Ji et al 2025][research_ji_yang_2025]
- [Jia et al 2024][research_jia_li_2024]
- [Jiang 2000][research_jiang_2000]
- [Jiang 2024][research_jiang_2024]
- [Jiang et al 2000][research_jiang_an_2000]
- [Jiang et al 2019][research_jiang_tian_2019]
- [Jiang et al 2023][research_jiang_wang_2023]
- [Jiménez Navarro][research_jimeneznavarro]
- [Jin et al 2013][research_jin_ren_2013]
- [Jing et al 2025][research_jing_lu_2025]
- [Jingeleski et al 2013][research_jingeleski_schetz_2013]
- [Jinks et al 2016][research_jinks_bruce_2016]
- [Jinli and Zhichun 2013][research_jinli_zhichun_2013]
- [Jirasek et al 2014][research_jirasek_cavagna_2014]
- [Joarder 2018][research_joarder_2018]
- [Joh et al 1991][research_johcy_grossmanb_1991]
- [Johnson][research_johnson]
- [Johnson 1953][research_johnson_1953]
- [Johnson 1958][research_johnsonclintont_1958]
- [Johnson 1972][research_johnson_1972]
- [Johnson 1982][research_johnson_1982]
- [Johnson 1986][research_johnson_1986]
- [Johnson and Adcock 1981][research_johnsoncb_adcockjb_1981]
- [Johnson and Bachalo 1978][research_johnson_bachalo_1978]
- [Johnson and Bachalo 1980][research_johnson_bachalo_1980]
- [Johnson and Hill 1985][research_johnsonwgjr_hillas_1985_c]
- [Johnson and King 1986][research_johnson_king_1986]
- [Johnson and Papamoschou 2010][research_johnson_papamoschou_2010]
- [Johnson et al 1970][research_johnson_josepha_1970]
- [Johnson et al 1979][research_johnson_owen_1979]
- [Johnson et al 1982][research_johnsonwgjr_hillas_1982]
- [Johnson et al 1985][research_johnsonwgjr_hillas_1985]
- [Johnson et al 1985][research_johnsonwgjr_hillas_1985_b]
- [Johnson et al 1986][research_johnsoncb_johnsonwgjr_1986]
- [Johnson et al 1986][research_johnsoncb_murthyav_1986]
- [Johnson et al 1986][research_johnsoncharlesb_dressdavida_1986]
- [Johnston 1992][research_johnston_1992]
- [Johnston 1998][research_johnston_1998]
- [Jokari and Kamali 2025][research_jokari_kamali_2025]
- [Jokari and Kamali 2026][research_jokari_kamali_2026]
- [Jones 1947][research_jones_1947]
- [Jones 1976][research_jonesrt_1976]
- [Jones 1977][research_jones_1977]
- [Jones and Farmer 1959][research_jonesgeorgewjr_farmermosesg_1959]
- [Jones and Jarrett 2018][research_jones_jarrett_2018]
- [Jones and Platzer 1998][research_jones_platzer_1998]
- [Jones and Unangst 1963][research_jonesgwjr_unangstjr_1963]
- [Jones and Van Dyke 1958][research_jones_vandyke_1958]
- [Jones et al 2000][research_jones_townsend_2000]
- [Jones et al 2013][research_jonesdaniels_buitrongt_2013]
- [Joppa 1968][research_joppa_1968]
- [Joppa 1969][research_joppa_1969]
- [Jordan 1972][research_jordanfljr_1972]
- [Jordan and Keener 1955][research_jordangarethh_keenerearlr_1955]
- [Joshi 1996][research_joshi_1996]
- [Joshi and Thomas 2025][research_joshi_thomas_2025]
- [Joshi et al 2023][research_joshi_salahudden_2023]
- [Jou and Metcalfe 1984][research_jou_metcalfe_1984]
- [Jou and Mueller 1985][research_jou_mueller_1985]
- [Julian Ooi 2024][research_julianooi_2024]
- [Jumper 1983][research_jumper_1983]
- [Jun et al 2009][research_jun_zhenghong_2009]
- [June et al 2025][research_june_hickey_2025]
- [Jurado and McGehee 2019][research_jurado_mcgehee_2019]
- [Jutte et al 2024][research_jutte_mason_2024]
- [Kabaleeshwaran et al 2026][research_kabaleeshwaran_das_2026]
- [Kacprzynski 1975][research_kacprzynski_1975]
- [Kady and Takahashi 2014][research_kady_takahashi_2014]
- [Kafyeke et al 1988][research_kafyeke_piperni_1988]
- [Kale and Pendharkar 2021][research_kale_pendharkar_2021]
- [Kalkhoran and Otugen 1994][research_kalkhoran_otugen_1994]
- [Kalkhoran and Sforza 1992][research_kalkhoran_sforza_1992]
- [Kalkhoran and Wilson 1992][research_kalkhoran_wilson_1992]
- [Kalkhoran et al 1989][research_kalkhoran_wilson_1989]
- [Kallstrom][research_kristenkallstrom]
- [Kalra et al 2007][research_kalra_zaidi_2007]
- [Kalra et al 2007][research_kalra_zaidi_2007_b]
- [Kamboj 2026][research_kamboj_2026]
- [Kameda et al 2008][research_kameda_seki_2008]
- [Kamiya et al 1978][research_kamiya_nishi_1978]
- [Kanchi et al 2026][research_kanchi_he_2026]
- [Kandath et al 2023][research_kandath_pushpangathan_2023]
- [Kandil and Hu 1988][research_kandil_hu_1988]
- [Kandil and Hu 1990][research_kandil_hu_1990]
- [Kandil and Kamdil 1994][research_kandil_kamdil_1994]
- [Kandil and Menzies 1996][research_kandil_menzies_1996]
- [Kandil et al 1993][research_kandil_kandil_1993]
- [Kandil et al 1993][research_kandil_kandil_1993_b]
- [Kandil et al 1994][research_kandil_kalisch_1994]
- [Kaneko et al 2000][research_kaneko_menshov_2000]
- [Kaneko et al 2024][research_kaneko_oyama_2024]
- [Kaneko et al 2024][research_kaneko_oyama_2024_b]
- [Kang et al 2024][research_kang_chen_2024]
- [Kannenberg and Boyd 1994][research_kannenberg_boyd_1994]
- [Kapania and Issac 1994][research_kapania_issac_1994]
- [Kapania et al 1993][research_kapaniarakeshk_issacjasonc_1993]
- [Kapania et al 2018][research_kapaniarakeshk_schetzjosepha_2018]
- [Karlgaard and Schoenenberger 2017][research_karlgaard_schoenenberger_2017]
- [Karlsson and Sedin 1979][research_karlsson_sedin_1979]
- [Karnick and Venkatraman 2017][research_karnick_venkatraman_2017]
- [Karns et al 2017][research_karns_strike_2017]
- [Karpouzian and Librescu 1992][research_karpouzian_librescu_1992]
- [Karpovich and Frankl 1951][research_karpovichea_franklfi_1951]
- [Karthik et al 1999][research_karthik_tulapurkara_1999]
- [Kashitani et al 2008][research_kashitani_yamaguchi_2008]
- [Kashitani et al 2010][research_kashitani_yamaguchi_2010]
- [Kashitani et al 2010][research_kashitani_yamaguchi_2010_b]
- [Kashitani et al 2012][research_kashitani_miura_2012]
- [Kashitani et al 2020][research_kashitani_taguchi_2020]
- [Kasim Biber and Trenton White 2019][research_kasimbiber_trentonwhite_2019]
- [Kass 1970][research_kass_1970]
- [Kassem and Banerjee][research_kassem_banerjee]
- [Katanoda et al 2001][research_katanoda_handa_2001]
- [Katz 2013][research_katz_2013]
- [Kaul 2021][research_kaul_2021]
- [Kaul 2022][research_kaul_2022]
- [Kaul 2024][research_kaul_2024]
- [Kaul and Nguyen 2019][research_kaul_nguyen_2019]
- [Kaul and Nguyen 2019][research_kaulupenderk_nguyennhant_2019]
- [Kaups et al 1989][research_kaups_mehta_1989]
- [Kawakami et al 2007][research_kawakami_takatoya_2007]
- [Kawamura and Karashima 1957][research_kawamura_karashima_1957]
- [Kaya 2025][research_kaya_2025]
- [Kayser et al 1986][research_kayser_clay_1986]
- [Kearns 1962][research_kearns_1962]
- [Keener 1959][research_keenerer_1959]
- [Keener 1984][research_keener_1984]
- [Keener 1985][research_keener_1985]
- [Keener and Pierce 1950][research_keenerer_piercem_1950]
- [Keener et al 1951][research_keenerearlr_bandishrozaliam_1951]
- [Keener et al 1958][research_keenerearlr_mcleodnormanj_1958]
- [Kehlet 1954][research_kehletalanb_1954]
- [Kehoe 1988][research_kehoe_1988]
- [Keith and Selberg 1984][research_keith_selberg_1984]
- [Kelly 1955][research_kellythomasc_1955]
- [Kelly 1988][research_kelly_1988]
- [Kelly 2014][research_kelly_2014]
- [Kelly and Osborne 1954][research_fuselage_mods_drag_1954]
- [Kelly et al][research_sethkelly_tausifjamal]
- [Kelly et al][research_sethwkelly_tausifjamal]
- [Kelly et al 2025][research_kelly_jamal_2025]
- [Kelnhofer 1969][research_kelnhofer_1969]
- [Kemp 1991][research_kempwilliambjr_1991]
- [Kemp and King 1956][research_kempwilliambjr_kingthomasjjr_1956]
- [Kempel et al 1975][research_kempelrw_danawh_1975]
- [Kempel et al 1988][research_kempelrobertw_mcneillwaltere_1988]
- [Kendall 1982][research_kendall_1982]
- [Kendall 1984][research_kendall_1984]
- [Kennelly 1983][research_kennellyjr_1983]
- [Kennelly et al 1990][research_kennellyrobertajr_krooilanm_1990]
- [Kennelly et al 1999][research_kennellyrobertajr_carmichaelralphl_1999]
- [Kenney 1939][research_kenney_1939]
- [Kentfield and Spragins 2004][research_kentfield_spragins_2004]
- [Kerlick et al 1982][research_kerlick_nixon_1982]
- [Kerlick et al 1983][research_kerlick_nixon_1983]
- [Kerschen and Tsai 1989][research_kerschen_tsai_1989]
- [Kesic and Majic 2004][research_kesic_majic_2004]
- [Kettle 1954][research_kettle_1954]
- [Keyfitz and Canic 1998][research_keyfitz_canic_1998]
- [Keyfitz et al 1977][research_keyfitz_melnik_1977]
- [Keyfitz et al 1978][research_keyfitz_melnik_1978]
- [Keyfitz et al 1979][research_keyfitz_melnik_1979]
- [Khalid and Mokry 1996][research_khalid_mokry_1996]
- [Khan and Deng 2012][research_khan_deng_2012]
- [Khan et al 2021][research_khan_mallik_2021]
- [Khan et al 2023][research_khan_kapania_2023]
- [Khanal et al 2009][research_khanal_knowles_2009]
- [Khlebnikov 1990][research_khlebnikov_1990]
- [Kholodar et al 2002][research_kholodar_thomas_2002]
- [Kholodar et al 2004][research_kholodar_dowell_2004]
- [Kholodar et al 2004][research_kholodar_dowell_2004_b]
- [Khot et al 1997][research_khot_eastep_1997]
- [Kickert Reiner 2012][research_kickertreiner_2012]
- [Kieszek 2024][research_kieszek_2024]
- [Kieszek et al 2024][research_kieszek_majcher_2024]
- [Kikuchi et al 2024][research_kikuchi_kouchi_2024]
- [Kikuchi et al 2026][research_kikuchi_miyake_2026]
- [Kilgore et al 1974][research_kilgore_adcock_1974]
- [Kim 2006][research_kim_2006]
- [Kim and Chang 2009][research_kim_chang_2009]
- [Kim and Chokani 1990][research_kim_chokani_1990]
- [Kim and Lee 2001][research_kim_lee_2001]
- [Kim and Liou 2019][research_kim_liou_2019]
- [Kim and Marciniak 1999][research_kim_marciniak_1999]
- [Kim and Marciniak 2002][research_kim_marciniak_2002]
- [Kim and Park 2026][research_kim_park_2026]
- [Kim and Rho 1998][research_kim_rho_1998]
- [Kim and Sung 1993][research_kim_sung_1993]
- [Kim and Sung 1995][research_kim_sung_1995]
- [Kim and Winchenbach 1985][research_kim_winchenbach_1985]
- [Kim et al][research_kim_cho]
- [Kim et al 1996][research_kim_matsuo_1996]
- [Kim et al 1996][research_kimhyun_hingstwarrenr_1996]
- [Kim et al 2003][research_kim_lee_2003]
- [Kim et al 2008][research_kim_kim_2008]
- [Kim et al 2012][research_kim_lee_2012]
- [Kimberlin 1987][research_kimberlin_1987]
- [Kimberlin and Sims 1992][research_kimberlin_sims_1992]
- [Kimmel and Prabhu 2015][research_kimmelrogerl_prabhudinesh_2015]
- [Kimmel et al 2015][research_kimmel_borg_2015]
- [King and Johnson 1980][research_king_johnson_1980]
- [King and Johnson 1986][research_king_johnson_1986]
- [King et al 2012][research_kingrudolpha_andinomarlyny_2012]
- [King et al 2013][research_kingrudolpha_andinomarlyny_2013]
- [Kirkham et al 1974][research_kirkham_jackson_1974]
- [Kirkman and Takahashi 2016][research_kirkman_takahashi_2016]
- [Kirkman and Takahashi 2017][research_kirkman_takahashi_2017]
- [Kish et al 2019][research_kish_wilde_2019]
- [Kishi et al 2023][research_kishi_yashiro_2023]
- [Klausmeyer 2004][research_klausmeyer_2004]
- [Klausmeyer 2018][research_klausmeyer_2018]
- [Kleckner 1945][research_allmovable_prelim_1945]
- [Kleckner 1946][research_allmovable_geared_1946]
- [Kleifges and Dolling 1993][research_kleifges_dolling_1993]
- [Klein 2019][research_klein_2019]
- [Kleppin et al 1980][research_kleppin_ruetenik_1980]
- [Klevenhusen 1980][research_klevenhusen_1980]
- [Klifi and Lili 2013][research_klifi_lili_2013]
- [Klim et al 2013][research_klim_zeppetelli_2013]
- [Kline 2026][research_kline_2026]
- [Klioutchnikov and Ballmann][research_klioutchnikov_ballmann]
- [Klioutchnikov and Olivier 2010][research_klioutchnikov_olivier_2010]
- [Klioutchnikov et al 2008][research_klioutchnikov_ballmann_2008]
- [Klopfer and Nielsen 1980][research_klopfer_nielsen_1980]
- [Klug et al 2021][research_klug_naik_2021]
- [Klunker and Newman 1974][research_klunker_newman_1974]
- [Klutchnikov and Ballmann 2004][research_klutchnikov_ballmann_2004]
- [Kluwick and Cox 2018][research_kluwick_cox_2018]
- [Kluwick and Kornfeld 2013][research_kluwick_kornfeld_2013]
- [Klyde et al 2004][research_klyde_harris_2004]
- [Kmak 2000][research_kmak_2000]
- [Knackstedt 1952][research_knackstedt_1952]
- [Knapp and Johnson 1953][research_x1_base_pressures_1953]
- [Knapp and Jordan 1953][research_x1_wing_loads_1953]
- [Knapp and Jordan 1953][research_x1_wing_pressures_1953]
- [Knapp et al 1953][research_x1_fuselage_pressures_1953]
- [Knaus 1981][research_knaus_1981]
- [Knight 1982][research_knight_1982]
- [Knight 1983][research_knight_1983]
- [Knight 1992][research_knight_1992]
- [Knight et al 2011][research_knight_braun_2011]
- [Knight et al 2012][research_knight_braun_2012]
- [Knipfer and Schewe 1999][research_knipfer_schewe_1999]
- [Knoedler et al][research_knoedler_bailey]
- [Knoedler et al 1996][research_knoedler_bailey_1996]
- [Knott 1974][research_knott_1974]
- [Ko et al 2003][research_ko_mason_2003]
- [Kocheemoolayil and Lele 2016][research_kocheemoolayil_lele_2016]
- [Kodigaddi 2026][research_kodigaddi_2026]
- [Kodigaddi et al 2024][research_kodigaddi_khazi_2024]
- [Koenig 1953][research_koenigdavidg_1953]
- [Koenig 1953][research_koenigdavidg_1953_b]
- [Koenig 1984][research_koenig_1984]
- [Kohzai et al 2010][research_kohzai_sudani_2010]
- [Koike et al 2016][research_koike_ueno_2016]
- [Kojima and Hashimoto 2022][research_kojima_hashimoto_2022]
- [Kojima and Hashimoto 2023][research_kojima_hashimoto_2023]
- [Kojima et al 2019][research_kojima_kameda_2019]
- [Kokin and Lysenko 1972][research_kokin_lysenko_1972]
- [Kolar and Lile 1971][research_kolar_lile_1971]
- [Kolesar et al 1970][research_kolesar_kassianides_1970]
- [Kolonay and Blair 1994][research_kolonay_blair_1994]
- [Kolonay and Yang 1998][research_kolonay_yang_1998]
- [Konig et al 2018][research_konig_singh_2018]
- [Konovalov et al 1998][research_konovalov_lashkov_1998]
- [Konrath 2015][research_konrath_2015]
- [Konrath et al 2006][research_konrath_schroder_2006]
- [Kontogiannis et al 2019][research_kontogiannis_parenteau_2019]
- [Kordan et al 1985][research_kordan_vonlavante_1985]
- [Koreanschi et al 2014][research_koreanschi_oliviu_2014]
- [Koren 1989][research_koren_1989]
- [Kornev and Pimenov 2022][research_kornev_pimenov_2022]
- [Kornilov 2006][research_kornilov_2006]
- [Korsun et al 2024][research_korsun_poplavsky_2024]
- [Korthäuer et al 2023][research_korthauer_accorinti_2023]
- [Kostic et al 2002][research_kostic_mitrovic_2002]
- [Kothari and Anderson 1987][research_kothari_anderson_1987]
- [Kouchi et al 2017][research_kouchi_yamaguchi_2017]
- [Kousen and Bendiksen 1994][research_kousen_bendiksen_1994]
- [Koziel and Leifsson 2011][research_koziel_leifsson_2011]
- [Kraft 1974][research_kraft_1974]
- [Kraft and Lo 1977][research_kraft_lo_1977]
- [Kraft and Mathews 1950][research_kraftchristophercjr_mathewscharlesw_1950]
- [Kraft et al 1979][research_kraft_parker_1979]
- [Krahn 1955][research_krahn_1955]
- [Kraiko 1987][research_kraiko_1987]
- [Kraiko and Pudovikov 1998][research_kraiko_pudovikov_1998]
- [Kraiko and Shapovalov 2022][research_kraiko_shapovalov_2022]
- [Kraiko and Shelomovskii 1984][research_kraiko_shelomovskii_1984]
- [Kraiko and Tilliaeva 1973][research_kraiko_tilliaeva_1973]
- [Kraiko and Tkalenko 1967][research_kraiko_tkalenko_1967]
- [Kraiko et al 2025][research_kraiko_tillyaeva_2025]
- [Kraljic and Rusak 2021][research_kraljic_rusak_2021]
- [Krener 2001][research_krener_2001]
- [Krenz 1979][research_krenz_1979]
- [Krishnan and Sandham 2007][research_krishnan_sandham_2007]
- [Krivec et al 1984][research_krivec_ling_1984]
- [Krogmann et al 1984][research_krogmann_stanewsky_1984]
- [Krogmann et al 1985][research_krogmann_stanewsky_1985]
- [Krone 1980][research_kronejr_1980]
- [Krone 1980][research_kronejr_1980_b]
- [Kroos 1995][research_kroos_1995]
- [Krothapalli et al 2003][research_krothapalli_alvi_2003]
- [Kruiswyk and Dutton 1989][research_kruiswyk_dutton_1989]
- [Krupovage 1978][research_krupovage_1978]
- [Kruse et al 2012][research_kruse_wunderlich_2012]
- [Krynytzky 2001][research_krynytzky_2001]
- [Krynytzky 2004][research_krynytzky_2004]
- [Krynytzky and Hergert 2002][research_krynytzky_hergert_2002]
- [Krynytzky et al 2010][research_krynytzky_johnsen_2010]
- [Kryvokhatko and Masko 2018][research_kryvokhatko_masko_2018]
- [Krzywoblocki 1943][research_krzywoblocki_1943]
- [Kubo 2018][research_kubo_2018]
- [Kuhl et al 1958][research_kuhlae_littlemv_1958]
- [Kuhlman et al 1988][research_kuhlman_cerney_1988]
- [Kuhn et al 1993][research_kuhn_wardwell_1993]
- [Kukreja 2008][research_kukreja_2008]
- [Kula et al 2025][research_kula_aslangil_2025]
- [Kulfan 2002][research_kulfan_2002]
- [Kulfan 2008][research_kulfan_2008]
- [Kulfan 2009][research_kulfan_2009]
- [Kumada and Sawada 2016][research_kumada_sawada_2016]
- [Kumar and Das 1989][research_kumar_das_1989]
- [Kumar et al 2001][research_kumar_viswanath_2001]
- [Kumar et al 2002][research_kumar_viswanath_2002]
- [Kumar et al 2021][research_kumar_sunil_2021]
- [Kumaravel et al 2015][research_kumaravel_jeyajothiraj_2015]
- [Kumawat et al 2025][research_kumawat_kumar_2025]
- [Kummer et al 2012][research_kummer_allred_2012]
- [Kuntavanish and Cancel 1983][research_kuntavanish_cancel_1983]
- [Kuntz et al 1986][research_kuntz_amatucci_1986]
- [Kurade et al 2021][research_kurade_venkatakrishnan_2021]
- [Kurbatskii and Montanari 2006][research_kurbatskii_montanari_2006]
- [Kurbjun and Thompson 1953][research_freefall_interference_1953]
- [Kurosaka et al 1981][research_kurosaka_chou_1981]
- [Kurus et al 2021][research_kurus_takahashi_2021]
- [Kussoy and Horstman 1992][research_kussoymi_horstmankc_1992]
- [Kusunose et al 1987][research_kusunose_marcum_1987]
- [Kusunose et al 1999][research_kusunose_crowder_1999]
- [Kutler and Lomax 1971][research_kutlerp_lomaxh_1971]
- [Kutney and Piszkin 1963][research_kutney_piszkin_1963]
- [Kutney and Piszkin 1964][research_kutney_piszkin_1964]
- [Kuwahara 1987][research_kuwahara_1987]
- [Kuya et al 2020][research_kuya_boda_2020]
- [Kuz'min 2005][research_kuzmin_2005]
- [Kuz'min 2006][research_kuzmin_2006]
- [Kuz'min 2007][research_kuzmin_2007]
- [Kuz'min 2009][research_kuzmin_2009]
- [Kuz'min 2010][research_kuzmin_2010]
- [Kuz'min and Shilkin 2009][research_kuzmin_shilkin_2009]
- [Kuzmin 2013][research_kuzmin_2013]
- [Kuzmin and Babarykin 2023][research_kuzmin_babarykin_2023]
- [Kuzmina et al 2018][research_kuzmina_ishmuratov_2018]
- [Kwak et al 2006][research_kwak_yoshida_2006]
- [Kwon and Vepa 2022][research_kwon_vepa_2022]
- [Kwon and Vepa 2022][research_kwon_vepa_2022_b]
- [Kwon et al 2005][research_kwon_park_2005]
- [Kyle et al 2001][research_kyle_orourke_2001]
- [Kyser 1956][research_kyser_1956]
- [Küchemann 1957][research_kuchemann_1957]
- [Küchemann 1962][research_kuchemann_1962]
- [Laar et al 2024][research_laar_atherstone_2024]
- [Labbe et al 2009][research_labbesteveng_gilbertmichaelg_2009]
- [Lacerda Montes et al 2025][research_lacerdamontes_alves_2025]
- [Lacey 1979][research_lacey_1979]
- [Lacy and Sclafani 2016][research_lacy_sclafani_2016]
- [Lada and Kontis 2009][research_lada_kontis_2009]
- [Lada and Kontis 2011][research_lada_kontis_2011]
- [Laderman 1979][research_laderman_1979]
- [Ladson 1973][research_ladsoncl_1973]
- [Ladson 1975][research_ladsoncl_1975]
- [Ladson and Hill 1987][research_ladsoncharlesl_hillsacquilla_1987]
- [Ladson and Ray 1984][research_ladsoncl_rayej_1984]
- [Ladson et al 1987][research_ladsoncharlesl_hillacquillas_1987]
- [Lafferty and Marren 1996][research_lafferty_marren_1996]
- [Lagemann 2024][research_lagemann_2024]
- [Lagemann et al 2022][research_lagemann_mateling_2022]
- [Lagemann et al 2024][research_lagemann_brunton_2024]
- [Lagen and Seiner 1990][research_lagennicholast_seinerjohnm_1990]
- [Lahmili et al 2026][research_lahmili_bouchaala_2026]
- [Lai et al 2014][research_lai_zhang_2014]
- [Laitone 1951][research_laitone_1951]
- [Lamah and Harris 1983][research_lamah_harris_1983]
- [Lamar et al 2001][research_johnelamar_cliffordjobara_2001]
- [Lamy 1983][research_lamy_1983]
- [Lan 1989][research_lancedward_1989]
- [Lan et al 1994][research_lan_luo_1994]
- [Lan et al 1995][research_lan_hsu_1995]
- [Landahl 1959][research_landahl_1959]
- [Landahl and Rubbert 1966][research_landahl_rubbert_1966]
- [Landahl and Widnall 1979][research_landahl_widnall_1979]
- [Landahl and Widnall 1980][research_landahl_widnall_1980]
- [Landahl and Widnall 1981][research_landahl_widnall_1981]
- [Landahl and Widnall 1982][research_landahl_widnall_1982]
- [Landers et al 1997][research_landers_landrum_1997]
- [Lapshina and Ostapenko 2009][research_lapshina_ostapenko_2009]
- [Large 1981][research_large_1981]
- [Larson 1984][research_larson_1984]
- [Larson and Siemers 1980][research_larsontj_siemerspmiii_1980]
- [Larson et al 1987][research_larsonterryj_whitmorestephena_1987]
- [Lasauskas 2005][research_lasauskas_2005]
- [Lashkov et al 2016][research_lashkov_karpenko_2016]
- [Lassiter 1981][research_lassiter_1981]
- [Laster et al 1998][research_laster_stanewsky_1998]
- [Latham et al 1977][research_lathame_gawienowskij_1977]
- [Latif et al 2006][research_latif_masud_2006]
- [Latif et al 2007][research_latif_masud_2007]
- [Lauchle 1974][research_lauchle_1974]
- [Lauer and Ansell 2022][research_lauer_ansell_2022]
- [Laughrey 1975][research_laughrey_1975]
- [Lauten et al 1954][research_lautenwtjr_lundstromrr_1954]
- [Lavala and Das 2025][research_lavala_das_2025]
- [Law 1975][research_law_1975]
- [Lawing and Johnson 1986][research_lawing_johnson_1986]
- [Lawing and Kilgore 1981][research_lawingpl_kilgorera_1981]
- [Layukallo and Nakamura 1999][research_layukallo_nakamura_1999]
- [Le Balleur and Girodroux-Lavigne 1989][research_leballeur_girodrouxlavigne_1989]
- [Le Provost et al 2018][research_leprovost_he_2018]
- [Lederer 1994][research_lederer_1994]
- [Lednicer and Roncz 1989][research_lednicer_roncz_1989]
- [Lee 1980][research_lee_1980]
- [Lee 1981][research_lee_1981]
- [Lee 1983][research_lee_1983]
- [Lee 1990][research_lee_1990]
- [Lee 1990][research_lee_1990_b]
- [Lee 1993][research_lee_1993]
- [Lee 2000][research_lee_2000]
- [Lee 2001][research_lee_2001]
- [Lee 2008][research_lee_2008]
- [Lee 2012][research_lee_2012]
- [Lee 2026][research_lee_2026]
- [Lee and Damodaran 2000][research_lee_damodaran_2000]
- [Lee and Damodaran 2001][research_lee_damodaran_2001]
- [Lee and Eyi 1991][research_lee_eyi_1991]
- [Lee and Eyi 1993][research_lee_eyi_1993]
- [Lee and Gross 2022][research_lee_gross_2022]
- [Lee and Jin 1988][research_lee_jin_1988]
- [Lee and Ohman 1984][research_lee_ohman_1984]
- [Lee and Rusak 1999][research_lee_rusak_1999]
- [Lee and Rusak 2000][research_lee_rusak_2000]
- [Lee and Tang 1989][research_lee_tang_1989]
- [Lee et al 2006][research_lee_lee_2006]
- [Lee et al 2017][research_lee_park_2017]
- [Lee et al 2020][research_lee_sim_2020]
- [Leelavathi and Subramanian 1969][research_leelavathi_subramanian_1969]
- [Lees 1956][research_lees_1956]
- [Lees and Reshotko 1962][research_lees_reshotko_1962]
- [Lefebvre and Zha 2014][research_lefebvre_zha_2014]
- [Lefebvre and Zha 2014][research_lefebvre_zha_2014_b]
- [Lefebvre et al 2013][research_lefebvre_dano_2013]
- [Lefebvre et al 2016][research_lefebvre_dano_2016]
- [Leger and Poggie 2014][research_leger_poggie_2014]
- [Lehman and Stearman 1977][research_lehman_stearman_1977]
- [Lei et al 2025][research_lei_zhang_2025]
- [Lemley and Mullans 1973][research_lemley_mullans_1973]
- [Lemley and Mullans 1974][research_lemley_mullans_1974]
- [Lempert 1975][research_lempert_1975]
- [Lensi 2000][research_lensi_2000]
- [Leonard 1982][research_leonardhwayne_1982]
- [Lepicovsky et al 1986][research_lepicovsky_ahuja_1986]
- [Lester and Gragston 2021][research_lester_gragston_2021]
- [Lester and Gragston 2022][research_lester_gragston_2022]
- [Level Flight Performance Flight Test and Data Reduction Methods for Propeller-Driven Aircraft 2003][research_level_flight_2003]
- [Levin and Fabish 1962][research_levin_fabish_1962]
- [Levinsky et al 1968][research_levinsky_thommen_1968]
- [Levy 1977][research_levylljr_1977]
- [Levy 1981][research_levylljr_1981]
- [Levy 1992][research_levy_1992]
- [Levy et al 1977][research_levy_shamroth_1977]
- [Lewis and Neel 1964][research_lewis_neel_1964]
- [Ley 1936][research_ley_1936]
- [Li 1977][research_li_1977]
- [Li 2015][research_li_2015]
- [Li 2023][research_li_2023]
- [Li 2024][research_li_2024]
- [Li and Cai 2016][research_li_cai_2016]
- [Li and Ekici 2018][research_li_ekici_2018]
- [Li and Geiselhart 2021][research_li_geiselhart_2021]
- [Li and Qin 2020][research_li_qin_2020]
- [Li et al 2000][research_li_li_2000]
- [Li et al 2002][research_li_huyse_2002]
- [Li et al 2004][research_li_krist_2004]
- [Li et al 2006][research_li_krist_2006]
- [Li et al 2016][research_li_hirota_2016]
- [Li et al 2020][research_li_wang_2020]
- [Li et al 2021][research_li_choudhari_2021]
- [Li et al 2022][research_li_lin_2022]
- [Li et al 2023][research_li_yu_2023]
- [Li et al 2023][research_li_zhang_2023]
- [Li et al 2024][research_li_yang_2024]
- [Li et al 2024][research_li_zhang_2024]
- [Li et al 2025][research_li_he_2025]
- [Li et al 2025][research_li_zhang_2025]
- [Li et al 2026][research_li_han_2026]
- [Li et al 2026][research_li_wen_2026]
- [Liang and Fu 1991][research_liang_fu_1991]
- [Liang and Fung 1985][research_liangsm_fungky_1985]
- [Licher 1956][research_licher_1956]
- [Liebeck 1971][research_liebeck_1971]
- [Liebeck 1989][research_liebeck_1989]
- [Liebhardt 2019][research_liebhardt_2019]
- [Liebhardt 2021][research_liebhardt_2021]
- [Liebhardt 2025][research_liebhardt_2025]
- [Lifshitz et al 1996][research_lifshitz_solnstev_1996]
- [Lift effect on transonic wind-tunnel blockage 1980][research_lift_effect_1980]
- [Lift/Drag Ratios of Optimised Slewed Wings at Supersonic Speeds 1962][research_lift_drag_ratios_1962]
- [Lighthill 1956][research_lighthill_1956]
- [Lijewski 1978][research_lijewski_1978]
- [Lijewski 1987][research_lijewski_1987]
- [Lijewski 1988][research_lijewski_1988]
- [Lijewski 1993][research_lijewski_1993]
- [Lin 1982][research_lin_1982]
- [Lin 1982][research_lin_1982_b]
- [Lin 2025][research_lin_2025]
- [Lin 2025][research_lin_2025_b]
- [Lin et al 1997][research_lin_chieng_1997]
- [Lin et al 2026][research_lin_wang_2026]
- [Lindley 1956][research_lindley_1956]
- [Lindsey 1946][research_lindseywf_1946]
- [Lindsey 1954][research_lindseywalterf_1954]
- [Lindsey and Milam 1974][research_lindseyai_milammd_1974]
- [Linearized Theory Transonic Breakdown 1986][research_linearized_theory_1986]
- [Liou and Sajben 1980][research_liou_sajben_1980]
- [Liou et al 2000][research_liou_huang_2000]
- [Little and Cubbage 1961][research_littlebhjr_cubbagejamesjjr_1961]
- [Litwhiler][research_litwhiler]
- [Liu 1983][research_liu_1983]
- [Liu 1998][research_liu_1998]
- [Liu 2022][research_liu_2022]
- [Liu 2023][research_liu_2023]
- [Liu and Fung 1985][research_liu_fung_1985]
- [Liu and Mignolet 2005][research_liu_mignolet_2005]
- [Liu and Mirels 1980][research_liu_mirels_1980]
- [Liu and Platzer 1970][research_liu_platzer_1970]
- [Liu and Singh 1995][research_liu_singh_1995]
- [Liu and Squire 1986][research_liu_squire_1986]
- [Liu and Yang 2016][research_liu_yang_2016]
- [Liu and Zha 2016][research_liu_zha_2016]
- [Liu et al 2012][research_liu_tao_2012]
- [Liu et al 2012][research_liu_wang_2012]
- [Liu et al 2016][research_liu_wang_2016]
- [Liu et al 2016][research_liu_yang_2016_b]
- [Liu et al 2016][research_liu_zhao_2016]
- [Liu et al 2017][research_liu_luo_2017]
- [Liu et al 2017][research_liu_yang_2017]
- [Liu et al 2019][research_liu_dong_2019]
- [Liu et al 2020][research_liu_gao_2020]
- [Liu et al 2021][research_liu_salazar_2021]
- [Liu et al 2021][research_tianshuliu_davidmsalazar_2021]
- [Liu et al 2022][research_liu_han_2022]
- [Liu et al 2022][research_liu_salazar_2022]
- [Liu et al 2023][research_liu_li_2023]
- [Liu et al 2023][research_liu_liu_2023]
- [Liu et al 2023][research_liu_pang_2023]
- [Liu et al 2024][research_liu_chen_2024]
- [Liu et al 2026][research_liu_peng_2026]
- [Ljungskog et al 2019][research_ljungskog_sebben_2019]
- [LlEBLEIN and Stockman 1972][research_lleblein_stockman_1972]
- [Lo 1969][research_lo_1969]
- [Lo 1972][research_lo_1972]
- [Lo 1974][research_lo_1974]
- [Lo and Glassman 1975][research_lo_glassman_1975]
- [Lo and Oliver 1970][research_lo_oliver_1970]
- [Lo and Ulbrich 1991][research_lo_ulbrich_1991]
- [Lo et al 1995][research_lo_qian_1995]
- [Lock 1961][research_lock_1961]
- [Lock 1964][research_lock_1964]
- [Lock 1990][research_rclock_1990]
- [Lock and Bridgewater 1967][research_lock_bridgewater_1967]
- [Lock and Rogers 1962][research_lock_rogers_1962]
- [Lockheed-Georgia Co Marietta 1969][research_lockheedgeorgiacomarietta_1969]
- [Loewner 2013][research_loewner_2013]
- [Loftin and Cohen 1948][research_loftinlaurencek_cohenkenneths_1948]
- [Lokos et al 2002][research_lokos_olney_2002]
- [Lokos et al 2005][research_lokos_lizotte_2005]
- [Lomax and Heaslet 1956][research_lomax_heaslet_1956]
- [Lombardi and Morelli 1995][research_lombardi_morelli_1995]
- [Lombardi et al 1997][research_lombardi_salvetti_1997]
- [Lombardi et al 2003][research_lombardi_salvetti_2003]
- [Long 1990][research_long_1990]
- [Long 2003][research_long_2003]
- [Long 2006][research_long_2006]
- [Long and Gladen 1988][research_long_gladen_1988]
- [Longitudinal Control and Trim Theory and Flight Test Methods 2003][research_longitudinal_control_2003]
- [Longitudinal Trim and Stability 2016][research_longitudinal_trim_2016]
- [Lopez Lopez et al 2026][research_lopezlopez_haramurabastos_2026]
- [Lorber and Carta 1989][research_lorberpeterf_cartafranklino_1989]
- [Lord and Eminton 1954][research_lord_eminton_1954]
- [Loth and Lee 2008][research_loth_lee_2008]
- [Loupy and Barakos 2017][research_loupy_barakos_2017]
- [Love and Young 1966][research_loveje_youngwr_1966]
- [Loving 1961][research_lovingdonaldl_1961]
- [Loving 1961][research_lovingdonaldl_1961_b]
- [Low Drag Airfoil Design Utilizing Passive Laminar Flow and Coupled Diffusion Control 1980][research_low_drag_1980]
- [Lowry et al 2001][research_lowry_smith_2001]
- [Lu and Settles 1989][research_lufrankk_settlesgarys_1989]
- [Lu and Yeh 1993][research_lu_yeh_1993]
- [Lu et al 1995][research_lu_pan_1995]
- [Lu et al 2012][research_lu_braun_2012]
- [Luber 2018][research_luber_2018]
- [Lucchi 1983][research_lucchi_1983]
- [Luchuk 1957][research_luchuk_1957]
- [Luckert 1973][research_luckert_1973]
- [Luckring 2003][research_luckring_2003]
- [Luckring and Hiller 2025][research_luckring_hiller_2025]
- [Luers and Fiscus 1984][research_luers_fiscus_1984]
- [Lugo et al 2014][research_lugo_tolson_2014]
- [Luh and Mack 1984][research_luh_mack_1984]
- [Lumley 1986][research_lumley_1986]
- [Lundry 1967][research_lundry_1967]
- [Lundstrom et al 1948][research_lundstromreginaldr_lautenwilliamtjr_1948]
- [Luo 1987][research_luo_1987]
- [Luo 2024][research_luo_2024]
- [Luo and Bao 1988][research_luo_bao_1988]
- [Luo and Wang 1998][research_luo_wang_1998]
- [Luo and Wang 1998][research_luo_wang_1998_b]
- [Luo et al 1997][research_luo_wang_1997]
- [Luo et al 2024][research_luo_tang_2024]
- [Luoma 1954][research_luomaarvoa_1954]
- [Luther 1957][research_luther_1957]
- [Lutsenko et al 2017][research_lutsenko_serikbay_2017]
- [Lutz et al 2023][research_lutz_kleinert_2023]
- [Lux 1978][research_luxdp_1978]
- [Ly et al 2006][research_ly_gear_2006]
- [Ly et al 2010][research_ly_norrison_2010]
- [Lykins and Keshmiri 2010][research_lykins_keshmiri_2010]
- [Lynch and Fancher 1983][research_lynch_fancher_1983]
- [Lynde and Campbell 2017][research_lynde_campbell_2017]
- [Lyons et al 1961][research_lyons_wc_1961]
- [Lyrintzis et al 1992][research_lyrintzis_wissink_1992]
- [Lürkens et al 2026][research_lurkens_meinke_2026]
- [Ma 2025][research_ma_2025]
- [Ma et al 2016][research_ma_wang_2016]
- [Ma et al 2024][research_ma_gao_2024]
- [Ma et al 2024][research_ma_li_2024]
- [Ma et al 2024][research_ma_yu_2024]
- [Mabey 1989][research_mabey_1989]
- [Mabey and Lee 1986][research_mabey_lee_1986]
- [Mabey et al 1992][research_mabeydg_boydenrp_1992]
- [Mabey et al 1995][research_mabeydg_boydenrp_1995]
- [MacAllister 1955][research_macallister_1955]
- [Maccormack 1971][research_maccormackrw_1971]
- [MacDonald and Alonso 2020][research_macdonald_alonso_2020]
- [Mace and Adamson 1985][research_mace_adamsonjr_1985]
- [Mach Number and Reynolds Number 2022][research_mach_number_2022]
- [Macha 1977][research_macha_1977]
- [Machado et al 2024][research_machado_chau_2024]
- [Machida et al 2005][research_machida_kikuchi_2005]
- [Mack 1979][research_mack_1979]
- [Mack 1989][research_mack_1989]
- [Madden 2010][research_madden_2010]
- [Madson and Talbot 1996][research_madson_talbot_1996]
- [Maeder 1964][research_maeder_1964]
- [Maeder and Hall 1955][research_maeder_hall_1955]
- [Maewal 1984][research_maewal_1984]
- [Maeyama et al 2026][research_maeyama_asada_2026]
- [Magnetohydrodynamic Transonic Flows 1990][research_magnetohydrodynamic_transonic_1990]
- [Magnus and Yoshihara 1975][research_magnus_yoshihara_1975]
- [Mahalingesh][research_mahalingesh]
- [Mahalingesh et al 2023][research_mahalingesh_piponniau_2023]
- [Mai 2025][research_mai_2025]
- [Maines et al 2007][research_maines_smith_2007]
- [Maintenance of Pitot-Static Systems of Transport Aircraft][research_maintenance_of]
- [Mair 1965][research_mair_1965]
- [Majdalani and Maicke 2010][research_majdalani_maicke_2010]
- [Makeich and Kryukov 2018][research_makeich_kryukov_2018]
- [Maklakov 2001][research_maklakov_2001]
- [Makowski 1964][research_makowski_1964]
- [Maksymiuk and Pulliam 1987][research_maksymiuk_pulliam_1987]
- [Maksymiuk and Watson Viken 1986][research_maksymiukcm_watsonvikensa_1986]
- [Malaek et al 2006][research_malaek_izadi_2006]
- [Maldonado et al 2024][research_maldonado_housman_2024]
- [Malik and Li 1993][research_malik_li_1993]
- [Maljević et al 2024][research_maljevic_dinulovic_2024]
- [Malkocoglu et al 2020][research_malkocoglu_barada_2020]
- [Mallik et al 2013][research_mallik_kapania_2013]
- [Mallozzi et al 2014][research_mallozzi_depaolis_2014]
- [Malmuth 1984][research_malmuth_1984]
- [Malmuth 1987][research_malmuth_1987]
- [Malmuth and Cole 1984][research_malmuth_cole_1984]
- [Malmuth et al 1983][research_malmuth_wu_1983]
- [Malmuth et al 1984][research_malmuth_wu_1984]
- [Malmuth et al 1985][research_malmuth_wu_1985]
- [Malmuth et al 1986][research_malmuth_wu_1986]
- [Malmuth et al 1987][research_malmuth_wu_1987]
- [Malmuth et al 1993][research_malmuth_jafroudi_1993]
- [Malone et al 1984][research_malone_sankar_1984]
- [Malvestudo et al 1957][research_malvestudofranks_cooneythomasv_1957]
- [Mani et al 2010][research_mani_rider_2010]
- [Manisankar and Verma 2023][research_manisankar_verma_2023]
- [Manjith 2026][research_manjith_2026]
- [Mann 1979][research_mannmj_1979]
- [Mann and Mercer 1985][research_mann_mercer_1985]
- [Mann and Mercer 1986][research_mann_mercer_1986]
- [Mann et al 1983][research_mann_campbell_1983]
- [Manneschmidt et al 2024][research_manneschmidt_ligrani_2024]
- [Manning and Gleason 1992][research_manning_gleason_1992]
- [Manokaran et al 2003][research_manokaran_vidya_2003]
- [Manwell 1977][research_manwell_1977]
- [Mao et al 2023][research_mao_jing_2023]
- [Mao et al 2023][research_mao_jing_2023_b]
- [Margolis 1947][research_margoliskenneth_1947]
- [Marino and Bonfiglioli 2012][research_marino_bonfiglioli_2012]
- [Marino et al 2009][research_marino_imperatore_2009]
- [Marino et al 2025][research_marino_eberle_2025]
- [Marino et al 2026][research_marino_eberle_2026]
- [Marion and Sharma 2025][research_marion_sharma_2025]
- [Mark 1958][research_markherman_1958]
- [Markhotok 2021][research_markhotok_2021]
- [Marquardt 1976][research_marquardt_1976]
- [Marsden et al 2005][research_marsden_bogey_2005]
- [Marshall and Schweikhard 1973][research_marshallrt_schweikhardwg_1973]
- [Martin 2008][research_martin_2008]
- [Martin 2011][research_martin_2011]
- [Martin and Jackson 1994][research_martin_jackson_1994]
- [Martin and Lomax 1974][research_martin_lomax_1974]
- [Martin et al 2003][research_martinpb_mcalisterkw_2003]
- [Martindale et al 1988][research_martindale_butler_1988]
- [Martos et al 2011][research_martos_kiszely_2011]
- [Martínez et al 2015][research_martinez_gennaro_2015]
- [Masdari et al 2018][research_masdari_talebi_2018]
- [Maseland et al 2006][research_maseland_laban_2006]
- [Masini et al 2019][research_masini_timme_2019]
- [Masini et al 2020][research_masini_timme_2020]
- [Maskew 1983][research_maskewb_1983]
- [Mason 1953][research_buffet_rocket_models_1953]
- [Mason 1982][research_mason_1982]
- [Mason 1993][research_mason_1993]
- [Mason 1995][research_mason_1995]
- [Mason 2013][research_mason_2013]
- [Mason and Inger 1975][research_mason_inger_1975]
- [Mason et al 1978][research_mason_mackenzie_1978]
- [Mason et al 2020][research_mason_lovejoy_2020]
- [Mason et al 2023][research_mason_davila_2023]
- [Massa 2014][research_massa_2014]
- [Masson et al 1998][research_masson_veilleux_1998]
- [Masson et al 1999][research_masson_veilleux_1999]
- [Masson et al 1999][research_masson_veilleux_1999_b]
- [Masuda and Yoshida 1991][research_masuda_yoshida_1991]
- [Mateer and Bertelrud 1983][research_mateer_bertelrud_1983]
- [Mateer et al 1976][research_mateer_brosh_1976]
- [Mateer et al 1987][research_mateer_seegmiller_1987]
- [Matheny and Gatlin 1978][research_mathenynw_gatlindh_1978]
- [Matheny and Panageas 1981][research_matheny_panageas_1981]
- [Mathews and Thompson 1947][research_freefall_65009_1947]
- [Mathews and Thompson 1947][research_freefall_wingbody_1947]
- [Mathur et al 2004][research_mathur_carr_2004]
- [Matranga 1961][research_matrangagenej_1961]
- [Matranga and Armistead 1958][research_matrangagenej_armisteadkatharineh_1958]
- [Matsui 1963][research_matsui_1963]
- [Matsuno and Lele 2020][research_matsuno_lele_2020]
- [Matsushima and Takanashi 1994][research_matsushima_takanashi_1994]
- [Matsushima and Takanashi 1996][research_matsushima_takanashi_1996]
- [Matsushita and Miyata 2003][research_matsushita_miyata_2003]
- [Matsushita et al][research_matsushita_miyata]
- [Matsushita et al][research_matsushita_miyata_b]
- [Matsushita et al 1998][research_matsushita_saitoh_1998]
- [Matthews 1948][research_xs1_downwash_1948]
- [Matthews and Key 1977][research_matthews_key_1977]
- [Matthews and Mathews 1948][research_xs1_freefall_1948]
- [Mattson 1947][research_xs1_model_1947]
- [Mattson and Loving 1948][research_xs1_model_stability_1948]
- [Mavriplis and Harris 1986][research_mavriplis_harris_1986]
- [Mavriplis and Levy 2001][research_mavriplisdj_levydavidw_2001]
- [Mavriplis and Levy 2002][research_mavriplis_levy_2002]
- [Mavriplis and Levy 2005][research_mavriplis_levy_2005]
- [Maximum Allowable Airspeed Instruments Reciprocating Engine Powered Aircraft][research_maximum_allowable]
- [Maydew 1957][research_maydew_1957]
- [Mayer and Valentine 1950][research_mayerjohnp_valentinegeorgem_1950]
- [Mayer and Valentine 1951][research_mayerjohnp_valentinegeorgem_1951]
- [Mayer et al 1950][research_mayerjohnp_valentinegeorgem_1950_b]
- [Mayer et al 2019][research_mayer_lutz_2019]
- [Mayes et al 1970][research_mayes_lores_1970]
- [Mayya et al 2022][research_mayya_karnick_2022]
- [Mazumder 2024][research_mazumder_2024]
- [Mazurov and Takovitskii 2022][research_mazurov_takovitskii_2022]
- [McAllister 1994][research_mcallister_1994]
- [McCanless and Boone 1974][research_mccanlessgfjr_boonejr_1974]
- [McCarthy et al 1955][research_mccarthy_jackf_1955]
- [McCarthy et al 1955][research_mccarthy_johnf_1955]
- [McClain and Pountney 1982][research_mcclain_pountney_1982]
- [McConnell 2004][research_mcconnell_2004]
- [McConnell 2006][research_mcconnell_2006]
- [McCroskey 1987][research_mccroskeywj_1987]
- [McCroskey 1988][research_wjmccroskey_1988]
- [McDearmon 1956][research_mcdearmonrussellw_1956]
- [McDearmon and Boatright 1956][research_x1a_interference_1956]
- [McDearmon and Clark 1956][research_x1a_damping_1956]
- [McDearmon and Clark 1956][research_x1e_damping_1956]
- [McDevitt et al 1975][research_mcdevitt_levyjr_1975]
- [McDonald et al 1982][research_mcdonald_shamroth_1982]
- [McElderry 1973][research_mcelderry_1973]
- [McFadden 1979][research_mcfaddengb_1979]
- [McFadden and Bons][research_evanjmcfadden_jeffreypbons]
- [McFall and Hollinger 1953][research_mcfalljohncjr_hollingerjamesa_1953]
- [McGann 1995][research_mcgann_1995]
- [McIntyre et al 1998][research_mcintyre_bowersox_1998]
- [McIntyre et al 1999][research_mcintyre_bowersox_1999]
- [McKinney and Gloss 1982][research_mckinney_gloss_1982]
- [McLaren et al 2007][research_mclaren_jayashankar_2007]
- [McLean 1994][research_mclean_1994]
- [McLean and Matoi 1986][research_mclean_matoi_1986]
- [McNally and Bach 1988][research_mcnally_bachjr_1988]
- [McNeill et al 1961][research_mcneillwatere_mcleanjohnd_1961]
- [McParlin and Adamczak 2003][research_mcparlin_adamczak_2003]
- [McVey et al 1969][research_mcvey_rejeske_1969]
- [Medan et al 1981][research_medanrt_magnusae_1981]
- [Medved 1990][research_medved_1990]
- [Medved 1993][research_medved_1993]
- [Mee 2001][research_mee_2001]
- [Mehta 1986][research_mehta_1986]
- [Mehta 1988][research_mehta_1988]
- [Mehta and Mehta 1997][research_mehta_mehta_1997]
- [Meier et al 1987][research_meier_michel_1987]
- [Meijering and Schroeder 2001][research_meijering_schroeder_2001]
- [Mele et al 2015][research_mele_ostieri_2015]
- [Mele et al 2016][research_mele_tognaccini_2016]
- [Mele et al 2017][research_mele_ostieri_2017]
- [Melin et al 2010][research_melin_isikveren_2010]
- [Mellquist and Bendiksen 2014][research_mellquist_bendiksen_2014]
- [Mellquist and Bendiksen 2015][research_mellquist_bendiksen_2015]
- [Melnik and Grossman 1974][research_melnikre_grossmanb_1974]
- [Melnik and Ives 1973][research_melnik_ives_1973]
- [Melnik et al 1977][research_melnik_chow_1977]
- [Melson and Streett 1993][research_melsonnduane_streettcraigl_1993]
- [Memon and Altman 2016][research_memon_altman_2016]
- [Mendenhall 1980][research_mendenhall_1980]
- [Meng et al 2024][research_meng_zhu_2024]
- [Mennell 1976][research_mennellrc_1976]
- [Menon and Skews 2009][research_menon_skews_2009]
- [Menshchikov and Somov 2019][research_menshchikov_somov_2019]
- [Menzies and Kandil 1996][research_menzies_kandil_1996]
- [Menzies et al 1995][research_menzies_kandil_1995]
- [Mercer and Maiden 1972][research_mercerce_maidendl_1972]
- [Mercer et al 1980][research_mercer_geller_1980]
- [Merceruio][research_merceruio]
- [Merienne et al 2019][research_merienne_brion_2019]
- [Merriam and Spaulding 1935][research_merriam_spaulding_1935]
- [Mertens et al 1986][research_mertens_klevenhusen_1986]
- [Mertens et al 1987][research_mertens_klevenhusen_1987]
- [Messiter and Adamson 1979][research_messiteraf_adamsontcjr_1979]
- [Messiter et al 1971][research_messiter_feo_1971]
- [Methods for Drag Determination in Flight 2003][research_methods_for_2003]
- [Metzger 1997][research_metzger_1997]
- [Meyers et al 1992][research_meyersjamesf_leejosephw_1992]
- [Michal and Mitcham 1949][research_michaldavidh_mitchamgradyl_1949]
- [Miele 1955][research_miele_1955]
- [Miele 1957][research_miele_1957]
- [Mignosi et al 1986][research_mignosi_dor_1986]
- [Mikhail 1989][research_mikhail_1989]
- [Mikhail 1989][research_mikhail_1989_b]
- [Mikhalev 2008][research_mikhalev_2008]
- [Miklos and Ingram 1975][research_miklos_ingram_1975]
- [Miles 1950][research_miles_1950]
- [Miles 1953][research_miles_1953]
- [Miles 1954][research_miles_1954]
- [Milholen and Chokani 1992][research_milholenii_chokani_1992]
- [Milholen and Chokani 1994][research_milholen_chokani_1994]
- [Milholen and Owens 2005][research_milholen_owens_2005]
- [Milillo 1972][research_milillo_1972]
- [Miller 1976][research_miller_1976]
- [Miller 1983][research_miller_1983]
- [Miller 1985][research_miller_1985]
- [Miller and Ribbens 1999][research_miller_ribbens_1999]
- [Miller et al 2003][research_miller_jacques_2003]
- [Milligan and Bailey 1963][research_milligan_bailey_1963]
- [Mills 2004][research_mills_2004]
- [Milne and Martos 2012][research_milne_martos_2012]
- [Min et al 2024][research_min_xian_2024]
- [Mineck 1989][research_mineckraymonde_1989]
- [Mineck and Campbell 1993][research_mineckraymonde_campbellrichardl_1993]
- [Mineck and Green 1990][research_mineck_green_1990]
- [Mineck and Lawing 1987][research_mineckraymonde_lawingpiercel_1987]
- [Mineck et al 1994][research_mineckraymonde_campbellrichardl_1994]
- [Minimum drag shapes 1962][research_minimum_drag_1962]
- [Minimum Performance Standard for Pitot and Pitot-Static Probes][research_minimum_performance_b]
- [Minimum Performance Standard for Pitot and Pitot-Static Tubes][research_minimum_performance]
- [Miotto et al 2021][research_miotto_wolf_2021]
- [Mirels 1977][research_mirels_1977]
- [Mirels 1986][research_mirels_1986]
- [Mironov and Serdyuk 2012][research_mironov_serdyuk_2012]
- [Mironov et al 2019][research_mironov_aniskin_2019]
- [Mirowitz 1975][research_mirowitzli_1975]
- [Miskin and Takahashi 2019][research_miskin_takahashi_2019]
- [Mitcham 1949][research_mitchamgradyl_1949]
- [Mitcham and Blanchard 1950][research_mitchamgradyl_blanchardwillardsjr_1950]
- [Mitcham et al 1951][research_mitchamgradyl_blanchardwillardsjr_1951]
- [Mitcham et al 1952][research_mitchamgradyl_blanchardwillards_1952]
- [Mitcham et al 1956][research_mitchamgradyl_stevensjosephe_1956]
- [Mitchell and Peck 1950][research_mitchelljessel_peckrobertf_1950]
- [Mitchell and Peck 1950][research_mitchelljessel_peckrobertf_1950_b]
- [Mitchell and Raghunathan 1994][research_mitchell_raghunathan_1994]
- [Mitcheltree et al 1989][research_mitcheltree_hassan_1989]
- [Mitsuo and Aoki 2018][research_mitsuo_aoki_2018]
- [Mixing and Mixing Enhancement in Supersonic Reacting Flowfields 1991][research_mixing_and_1991]
- [Miyagoshi and Daisuke 2021][research_miyagoshi_daisuke_2021]
- [Miyaji and Takegawa 2022][research_miyaji_takegawa_2022]
- [Miyakawa et al 1985][research_miyakawa_hirose_1985]
- [Miyake and Terashima 2022][research_miyake_terashima_2022]
- [Miyake and Terashima 2023][research_miyake_terashima_2023]
- [Mobley and Jones 1989][research_mobley_jones_1989]
- [Modarress and Johnson 1976][research_modarress_johnson_1976]
- [Modiano and Murman 1993][research_modianodavidl_murmanearllm_1993]
- [Moes et al 1993][research_moestimothyr_whitmorestephena_1993]
- [Moes et al 1998][research_aerospike_sr71_1998]
- [Moga 1980][research_moga_1980]
- [Moga and Dejarnette 1981][research_moga_dejarnette_1981]
- [Mohamed et al 2021][research_mohamed_abdelhady_2021]
- [Mohan 1991][research_mohan_1991]
- [Mohr et al 1988][research_mohr_yang_1988]
- [Mokry 1989][research_mokry_1989]
- [Mokry 1990][research_mokry_1990]
- [Mokry 1995][research_mokry_1995]
- [Mokry 1995][research_mokry_1995_b]
- [Mokry 2001][research_mokry_2001]
- [Mokry and Khalid 2000][research_mokry_khalid_2000]
- [Molki and Ogbozor 2026][research_molki_ogbozor_2026]
- [Molton et al 2013][research_molton_dandois_2013]
- [Molyneux 1960][research_molyneux_1960]
- [Montaini and Carlotti 2026][research_montaini_carlotti_2026]
- [Montano et al 2024][research_montano_dimino_2024]
- [Moore 1972][research_moore_1972]
- [Moore and Frei 1983][research_moore_frei_1983]
- [Moorthamers and Anemaat 2023][research_moorthamers_anemaat_2023]
- [Moosavi et al 2005][research_moosavi_naddafoskouei_2005]
- [Morales Tirado et al 2019][research_moralestirado_quagliarella_2019]
- [Morawetz 1987][research_morawetz_1987]
- [Morelli 2000][research_morelli_2000]
- [Morelli et al 1976][research_morelli_fioravanti_1976]
- [Moreno et al 2012][research_moreno_taylor_2012]
- [Moretti and Lippolis 1989][research_moretti_lippolis_1989]
- [Mori et al 2024][research_mori_yakeno_2024]
- [Morito and Rowe 1972][research_moritoii_rowe_1972]
- [Morizawa et al 2018][research_morizawa_nonomura_2018]
- [Moroianu et al 2005][research_moroianu_caraeni_2005]
- [Morra and Nicolosi 2025][research_morra_nicolosi_2025]
- [Morrida et al 2017][research_morrida_delucca_2017]
- [Morse 1945][research_morse_1945]
- [Morton and Beran 1995][research_morton_beran_1995]
- [Morton and Beran 1996][research_morton_beran_1996]
- [Morton and Beran 1996][research_morton_beran_1996_b]
- [Morton and Beran 1999][research_morton_beran_1999]
- [Morton et al 1997][research_morton_beran_1997]
- [Mosbarger and King 1995][research_mosbarger_king_1995]
- [Moseley and Thompson 1957][research_moseleywcjr_thompsonrf_1957]
- [Moses 1997][research_mosesrobertw_1997]
- [Moses 1997][research_mosesrobertw_1997_b]
- [Moses 1999][research_mosesrobertw_1999]
- [Moses and Huttsell 2000][research_f22_fin_buffet_2000]
- [Moses et al 2001][research_mosesrobertw_wiesemancarold_2001]
- [Moss et al 1991][research_mossstevenw_colestanleyr_1991]
- [Mott 1954][research_mott_1954]
- [Mottershead and Cooper 2012][research_mottershead_cooper_2012]
- [Moua et al 2008][research_mouachengm_coxtimothyh_2008]
- [Moul 1957][research_moulmt_1957]
- [Moulden et al 1974][research_moulden_wu_1974]
- [Mounts and Barber 1992][research_mounts_barber_1992]
- [Muck and Smits 1984][research_muck_smits_1984]
- [Mufti et al 2024][research_mufti_bhaduri_2024]
- [Muhlstein and Coe 1975][research_muhlsteinjr_coe_1975]
- [Mukhopadhyay 1999][research_mukhopadhyay_1999]
- [Mukhopadhyay 1999][research_mukhopadhyayvivek_1999]
- [Mukhopadhyay 2000][research_mukhopadhyay_2000]
- [Mulder et al 2009][research_mulder_lubbers_2009]
- [Muller and Gasko 1967][research_muller_gasko_1967]
- [Muller and Wesshaar 1994][research_muller_wesshaar_1994]
- [Mundell and Mabey 1986][research_mundell_mabey_1986]
- [Mungall 1948][research_geared_tab_1948]
- [Munguía et al 2019][research_munguia_mukhopadhaya_2019]
- [Munk 1921][research_munk_1921]
- [Murakami et al 2007][research_murakami_tada_2007]
- [Muralidharan et al 2025][research_muralidharan_gilbertraj_2025]
- [Murman 1972][research_murman_1972]
- [Murman 1976][research_murman_1976]
- [Murman 1979][research_murman_1979]
- [Murman and Cole 1974][research_murman_cole_1974]
- [Murphy 1970][research_murphyjd_1970]
- [Murphy 1971][research_murphyjd_1971]
- [Murphy and Schmidt 1953][research_murphy_schmidt_1953]
- [Murphy et al 1968][research_murphyjd_rosewc_1968]
- [Murphy et al 1983][research_murphy_rogers_1983]
- [Murray 1979][research_murray_1979]
- [Murray and Hillier 2009][research_murray_hillier_2009]
- [Murray et al 2020][research_murray_giannellis_2020]
- [Murthy 1987][research_murthyav_1987]
- [Murthy and Rose 1977][research_murthy_rose_1977]
- [Murthy and Steinle 1986][research_murthy_steinle_1986]
- [Murthy and Wedemeyer 1990][research_murthy_wedemeyer_1990]
- [Murty 1993][research_murty_1993]
- [Myers and Ruo 1983][research_myers_ruo_1983]
- [Myers et al 1983][research_myersmr_guruswamyp_1983]
- [NACA 1945 Drag Measurement at Transonic Speeds on a Freely Falling Body][research_freefall_1945]
- [NACA 1949 Comparative Drag Measurements at Transonic Speeds of Rectangular and Sweptback Airfoils][research_comparative_drag_1949]
- [NACA 1950 Comparative Drag Measurements at Transonic Speeds of Rectangular and Sweptback Airfoils][research_comparative_drag_1950]
- [NACA Conference on Aerodynamic 1949][research_transonic_conference_1949]
- [NACA Conference on Aerodynamic Problems of Transonic Airplane Design 1947][research_naca_conference_1947]
- [NACA Conference on Aircraft 1957][research_loads_flutter_conf_1957]
- [Nagamatsu and Dyer 1984][research_nagamatsuht_dyerr_1984]
- [Nagamatsu and Ficarra 1985][research_nagamatsu_ficarra_1985]
- [Nagamatsu and Orozco 1984][research_nagamatsu_orozco_1984]
- [Nagamatsu et al 1982][research_nagamatsuht_browerwbjr_1982]
- [Nagamatsu et al 1983][research_nagamatsuht_ficarrar_1983]
- [Nagamatsu et al 1987][research_nagamatsu_trilling_1987]
- [Nagaraja et al 1982][research_nagaraja_lakin_1982]
- [Nagarajan and Baraiya 2023][research_nagarajan_baraiya_2023]
- [Nagel and Thomas 1965][research_nagel_thomas_1965]
- [Nagy and Kirsten 1976][research_nagy_kirsten_1976]
- [Nahom Jidovetski et al 2025][research_nahomjidovetski_raveh_2025]
- [Naida and Fonarev 1995][research_naida_fonarev_1995]
- [Naida and Fonarev 1996][research_naida_fonarev_1996]
- [Nakagawa 1986][research_nakagawa_1986]
- [Nakagawa and Dahm 2000][research_nakagawa_dahm_2000]
- [Nakakita and Arizono 2009][research_nakakita_arizono_2009]
- [Nakamura 1982][research_nakamura_1982]
- [Nallapula et al 2012][research_nallapula_schade_2012]
- [Namba 1968][research_namba_1968]
- [Nambu et al 2012][research_nambu_hashimoto_2012]
- [Namgoong et al 2002][research_namgoong_crossley_2002]
- [Namura and Jeong 2013][research_namura_jeong_2013_b]
- [Namura et al 2013][research_namura_jeong_2013]
- [Nangia and Palmer 2000][research_nangia_palmer_2000]
- [Nangia et al 2003][research_nangia_palmer_2003]
- [Nangia et al 2023][research_nangia_ghoreyshi_2023]
- [Narain 1983][research_narain_1983]
- [Narayanswami et al 1993][research_narayanswamin_horstmancc_1993]
- [Nark 1968][research_nark_1968]
- [Narsipur 2022][research_narsipur_2022]
- [NASA 1973 Experimental and Theoretical Investigations in Two-Dimensional Transonic Flow][research_transonic_2d_1973]
- [NASA 1982 The Effect of Ejector Augmentation on Test-Section Flow Quality in a Transonic Tunnel][research_calspan_ejector_1982]
- [Nash et al 1972][research_nashjf_scruggsrm_1972]
- [Nash et al 2025][research_nash_timme_2025]
- [Nastase and Rudianu 1990][research_nastase_rudianu_1990]
- [Nastase and Weisensee 1984][research_nastase_weisensee_1984]
- [Natarajan 2022][research_natarajan_2022]
- [National Advisory Committee for Aeronautics 1932][research_nationaladvisorycommitteeforaeronautics_1932]
- [Naval Air Systems Command Patuxent River Md 1999][research_navalairsystemscommandpatuxentrivermd_1999]
- [Naval Air Systems Command Patuxent River Md 2000][research_navalairsystemscommandpatuxentrivermd_2000]
- [Nayfeh 1992][research_nayfeh_1992]
- [Nazarenko and Nevezhina 1972][research_nazarenko_nevezhina_1972]
- [Neal 1970][research_neal_1970]
- [Negrão et al 1998][research_negrao_fanton_1998]
- [Neil and Verhoff 1982][research_neil_verhoff_1982]
- [Nellessen et al 1996][research_nellessen_britten_1996]
- [Nelson and Mouch 1978][research_nelson_mouch_1978]
- [Nelson and Stoney 1953][research_nelsonrobertl_stoneywilliamejr_1953]
- [Nelson and Welsh 1957][research_nelsonrobertl_welshclementj_1957]
- [Nelson and Welsh 1960][research_nelsonrobertl_welshclementj_1960]
- [Nenni 1980][research_nenni_1980]
- [Nesteruk and Cartwright 2011][research_nesteruk_cartwright_2011]
- [Newell et al 1963][research_newell_dolbin_1963]
- [Newman and Anderson 1978][research_newmanpa_andersonec_1978]
- [Newman and Barnwell 1983][research_perryanewman_richardwbarnwell_1983]
- [Newman et al 1988][research_newman_kemp_1988]
- [Newton 1965][research_newton_1965]
- [Nghiem and Norstrud 1989][research_nghiem_norstrud_1989]
- [Ngoc 2020][research_ngoc_2020]
- [Nguyen and Xiong][research_nhannguyen_juntaoxiong]
- [Nguyen and Xiong 2021][research_transonic_correction_2021]
- [Nguyen and Xiong 2022][research_nguyen_xiong_2022]
- [Nguyen and Xiong 2022][research_nguyen_xiong_2022_b]
- [Nguyen and Xiong 2023][research_control_derivative_2023]
- [Nguyen and Xiong 2023][research_nguyen_xiong_2023]
- [Nguyen and Xiong 2023][research_nguyen_xiong_2023_b]
- [Nguyen et al][research_nhannguyen_jasonfugate]
- [Nguyen et al 2019][research_nguyen_fugate_2019]
- [Ni et al 2012][research_ni_hu_2012]
- [Nichols 1974][research_nicholsme_1974]
- [Nichols and Goral 1947][research_nicholsmarkr_goraledwinb_1947]
- [Nichols and Goral 1952][research_nicholsmarkr_goraledwinb_1952]
- [Nichols and Jackson 1962][research_nichols_jackson_1962]
- [Nichols and Rinkoski 1952][research_nicholsmarkr_rinkoskidonaldw_1952]
- [Nicholson and lowry 1966][research_nicholson_lowry_1966]
- [Nicks and McKinney 1978][research_nicks_mckinney_1978]
- [Nicola and Cirino 2002][research_nicola_cirino_2002]
- [Nicolaides 1982][research_nicolaides_1982]
- [Nicolaides and Brady 1959][research_nicolaides_brady_1959]
- [Nicolas et al 2016][research_nicolas_sullivan_2016]
- [Nicolosi et al 2011][research_nicolosi_demarco_2011]
- [Nie et al 2022][research_nie_song_2022]
- [Nie et al 2024][research_nie_zheng_2024]
- [Nie et al 2026][research_nie_zhang_2026]
- [Nielsen 1985][research_nielsen_1985]
- [Nielsen 1985][research_nielsen_1985_b]
- [Nielsen et al 1984][research_nielsen_goodwin_1984]
- [Nietubicz 1975][research_nietubicz_1975]
- [Nietubicz and Sturek 1988][research_nietubicz_sturek_1988]
- [Nietubicz et al 1984][research_nietubicz_sahu_1984]
- [Niewald and Parker 1999][research_niewald_parker_1999]
- [Niewoehner 2006][research_niewoehner_2006]
- [Nikfetrat et al 1992][research_nikfetrat_vandam_1992]
- [Nikolic and Jumper 2004][research_nikolic_jumper_2004]
- [Nikolitsch 1978][research_nikolitsch_1978]
- [Nili Ahmadabadi et al 2013][research_niliahmadabadi_ghadak_2013]
- [Niven and Tait 2000][research_niven_tait_2000]
- [Nixon 1974][research_nixon_1974]
- [Nixon 1979][research_nixon_1979]
- [Nixon 1980][research_nixon_1980]
- [Nixon 2001][research_nixon_2001]
- [Nixon 2003][research_nixon_2003]
- [Nixon 2020][research_nixon_2020]
- [Nixon and Klopfer 1984][research_nixon_klopfer_1984]
- [Nixon and Nixon 1997][research_nixon_nixon_1997]
- [Nixon and Nixon 1997][research_nixon_nixon_1997_b]
- [Nixon and Tzuoo 1986][research_nixon_tzuoo_1986]
- [Nixon and Tzuoo 1987][research_nixon_tzuoo_1987]
- [Noboru and Saito 2008][research_noboru_saito_2008]
- [Nocilla 1972][research_nocilla_1972]
- [Nomura 2003][research_nomura_2003]
- [Nonlinear Green's Function Method for Unsteady Transonic Flows 1982][research_nonlinear_green_s_1982]
- [Nonomura and Fujii 2007][research_nonomura_fujii_2007]
- [Nonomura and Fujii 2008][research_nonomura_fujii_2008]
- [Norris 1979][research_norris_1979]
- [Norris et al 1989][research_norris_paris_1989]
- [Norum and Brown 1993][research_norum_brown_1993]
- [Norum and Shearin 1986][research_norum_shearin_1986]
- [Ntantis and Xezonakis 2024][research_ntantis_xezonakis_2024]
- [Nugent 1954][research_nugentjack_1954]
- [Nugent 1957][research_d558_stores_1957]
- [Nunn and Bry 1982][research_nunn_bry_1982]
- [Nyquist 1928][research_nyquist_1928]
- [O'Brien and Takahashi 2023][research_obrien_takahashi_2023]
- [O'Kelly 1954][research_okellyburker_1954]
- [Obara et al 1991][research_obara_lee_1991]
- [Obayashi et al 1985][research_obayashi_kuwahara_1985]
- [Oberkampf 1978][research_oberkampf_1978]
- [Ogawa and Babinsky 2006][research_ogawa_babinsky_2006]
- [Ogawa et al 2007][research_ogawa_babinsky_2007]
- [Ogawa et al 2008][research_ogawa_babinsky_2008]
- [Ogawa et al 2008][research_ogawa_watanabe_2008]
- [Ogren et al 1974][research_ogren_sotanski_1974]
- [Ohashi et al 2019][research_ohashi_morita_2019]
- [Ohashi et al 2020][research_ohashi_morita_2020]
- [Ohashi et al 2021][research_ohashi_fukagata_2021]
- [Ohmichi et al 2017][research_ohmichi_ishida_2017]
- [Ohmichi et al 2018][research_ohmichi_ishida_2018]
- [Okolo et al 2015][research_okolo_dogan_2015]
- [Olejnik and Zalewski 2020][research_olejnik_zalewski_2020]
- [oliveira et al 2016][research_oliveira_avelar_2016]
- [Oliver et al 2006][research_oliverab_lillardrp_2006]
- [Oliver et al 2007][research_oliverab_lillardrp_2007]
- [Olivier et al 2002][research_olivier_reichel_2002]
- [Olivier et al 2003][research_olivier_reichel_2003]
- [Olles et al 2004][research_olles_lynn_2004]
- [Olsen 1966][research_olsen_1966]
- [Olsen et al 1984][research_olsen_shaw_1984]
- [Olson and Bielat 1955][research_olsonrolande_bielatralphp_1955]
- [Olson and Stridsberg 1979][research_olson_stridsberg_1979]
- [Olson et al 2026][research_olson_albrecht_2026]
- [Om and Childs 1983][research_om_childs_1983]
- [Om and Childs 1985][research_om_childs_1985]
- [Om et al 1982][research_om_childs_1982]
- [Om et al 2001][research_om_curtin_2001]
- [On the numerical solution of high Mach number flows][research_on_the_numerical]
- [Ongarato 1969][research_ongarato_1969]
- [Opgenoord et al 2017][research_opgenoord_drela_2017]
- [Opstal 2011][research_opstal_2011]
- [Ordaz et al 2015][research_ordaz_geiselhart_2015]
- [Orme and Gilyard 1993][research_orme_gilyard_1993]
- [Ormsbee 1962][research_ormsbee_1962]
- [Oruc and Baklacioglu 2022][research_oruc_baklacioglu_2022]
- [Oruc and Baklacioglu 2023][research_oruc_baklacioglu_2023]
- [Osawa and Hewitt 1986][research_osawa_hewitt_1986]
- [Osborne 1949][research_osborneroberts_1949]
- [Osborne 1957][research_osborneroberts_1957]
- [Osborne and Stafford 1960][research_osborners_staffordvc_1960]
- [Osborne and Tempelmeyer 1954][research_osborneroberts_tempelmeyerkennethe_1954]
- [Oskam 1983][research_oskam_1983]
- [Oskam et al 1978][research_oskam_vas_1978]
- [Osnes and Vartdal 2022][research_osnes_vartdal_2022]
- [Ostgaard 1962][research_ostgaard_1962]
- [Oswald 1932][research_oswald_1932]
- [Oswatitsch 1980][research_oswatitsch_1980]
- [Otiefy and Negm 2010][research_otiefy_negm_2010]
- [Otiefy and Negm 2011][research_otiefy_negm_2011]
- [Otto 1974][research_otto_1974]
- [Owen 1981][research_owen_1981]
- [Owen and Owen 2014][research_owen_owen_2014]
- [Owens et al 2002][research_owenslr_wahlsra_2002]
- [Owens et al 2003][research_owens_capone_2003]
- [Ower and Pankhurst 1977][research_ower_pankhurst_1977]
- [Ower and Pankhurst 1977][research_ower_pankhurst_1977_b]
- [Oyama et al 2008][research_oyama_ito_2008]
- [Oyeniran et al 2022][research_oyeniran_miyake_2022]
- [Ozawa and Nonomura 2024][research_ozawa_nonomura_2024]
- [Ozgoren et al 2001][research_ozgoren_sahin_2001]
- [P. A. Sherar 2011][research_pasherar_2011]
- [Paciorri and Sabetta 2003][research_paciorri_sabetta_2003]
- [Padova and Falk 1980][research_padova_falk_1980]
- [Padua and Preisighe Viana 2025][research_padua_preisigheviana_2025]
- [Page 1956][research_pagewilliama_1956]
- [Pahle et al 2012][research_pahle_berger_2012]
- [Pak et al 1991][research_pak_friedmann_1991]
- [Pak et al 1995][research_pak_friedmann_1995]
- [Pal and Roy 2024][research_pal_roy_2024]
- [Palaniappan and Jameson 2004][research_palaniappan_jameson_2004]
- [Palko 1972][research_palko_1972]
- [Palko 1973][research_palko_1973]
- [Palko 1974][research_palko_1974]
- [Pallister et al 1992][research_pallister_parker_1992]
- [Pan and Kuo 2021][research_pan_kuo_2021]
- [Panaras and Inger 1977][research_panaras_inger_1977]
- [Panda and Warrior 2021][research_panda_warrior_2021]
- [Panda et al 2005][research_pandajayanta_seasholtzrichardg_2005]
- [Pandey and Sinha 2024][research_pandey_sinha_2024]
- [Pane][research_pane]
- [Pang et al 2026][research_pang_zhang_2026]
- [Pantano and Sarkar 1999][research_pantano_sarkar_1999]
- [Pantano and Sarkar 2002][research_pantano_sarkar_2002]
- [Panton et al 1980][research_panton_oberkampf_1980]
- [Pao 1976][research_pao_1976]
- [Pardee and Heaslet 1946][research_pardeeotwayom_heasletmaxa_1946]
- [Paris and Alaverdi 1998][research_paris_alaverdi_1998]
- [Park 2017][research_park_2017]
- [Park and Abla 1982][research_park_abla_1982]
- [Park and Abla 1983][research_park_abla_1983]
- [Park and Chung 2012][research_park_chung_2012]
- [Parker and Black 1988][research_parkerjr_black_1988]
- [Parker et al 1991][research_parker_spain_1991]
- [Parks and Bach 1990][research_parks_bachjr_1990]
- [Parks and Kehlet 1952][research_parksjamesh_kehletalanb_1952]
- [Parlier 1986][research_parlier_1986]
- [Parthasarathy and Massier 1976][research_parthasarathy_massier_1976]
- [Pashilkar 1996][research_pashilkar_1996]
- [Pate 1980][research_pate_1980]
- [Patel and Lefas 2025][research_patel_lefas_2025]
- [Patel and Lefas 2026][research_patel_lefas_2026]
- [Patel et al 1979][research_patel_lee_1979]
- [Patel et al 2023][research_patel_deodhare_2023]
- [Pathan et al 2017][research_pathan_khan_2017]
- [Patterson 1966][research_pattersonjcjr_1966]
- [Patterson 1967][research_patterson_1967]
- [Pavlenko and Reslan 2022][research_pavlenko_reslan_2022]
- [Payne and McConnell 2004][research_payne_mcconnell_2004]
- [Payne and Samuels 1990][research_payne_samuels_1990]
- [Paziresh et al 2017][research_paziresh_nikseresht_2017]
- [Pazner et al 2019][research_pazner_franco_2019]
- [Pearcey 1961][research_pearcey_1961]
- [Peele 1953][research_d558_slat_1953]
- [Peele 1954][research_peelejamesr_1954]
- [Pehlivanoglu and Yagiz 2011][research_pehlivanoglu_yagiz_2011]
- [Peigin and Epstein 2007][research_peigin_epstein_2007]
- [Peigin and Epstein 2015][research_peigin_epstein_2015]
- [Pekardan and Alexeenko 2016][research_pekardan_alexeenko_2016]
- [Pekardan and Alexeenko 2018][research_pekardan_alexeenko_2018]
- [Peltzer 2008][research_peltzer_2008]
- [Pena et al 2018][research_fiber_optic_loads_2018]
- [Pendley 1947][research_pendleyroberte_1947]
- [Peng and Chen 2025][research_peng_chen_2025]
- [Peng and Chen 2026][research_peng_chen_2026]
- [Pengelley and Wilson 1954][research_pengelley_wilson_1954]
- [Perez et al 2025][research_perez_hader_2025]
- [Performance Evaluation by Flight Tests 1995][research_performance_evaluation_1995]
- [Perkins and Brice 1966][research_perkins_brice_1966]
- [Perkins et al 1977][research_perkins_jr_1977]
- [Perry 1978][research_perrybiii_1978]
- [Perry et al 2007][research_perryboydiii_silvawaltera_2007]
- [Persh 1956][research_persh_1956]
- [Persoon et al 1980][research_persoon_roos_1980]
- [Persoon et al 1983][research_persoon_horsten_1983]
- [Persoon et al 1984][research_persoon_horsten_1984]
- [Peters 1985][research_peters_1985]
- [Peters and Kennedy 1977][research_peters_kennedy_1977]
- [Peterson and Menees 1959][research_unswept_stability_1959]
- [Petrocchi and Barakos 2023][research_petrocchi_barakos_2023]
- [Petrocchi and Barakos 2023][research_petrocchi_barakos_2023_b]
- [Petrocchi and Barakos 2024][research_petrocchi_barakos_2024]
- [Petrocchi et al 2022][research_petrocchi_steijl_2022]
- [Petrocchi et al 2023][research_petrocchi_mauriello_2023]
- [Petronevich 2016][research_petronevich_2016]
- [Petty 1975][research_petty_1975]
- [Petynia et al 1958][research_petyniawilliamw_croomdelwinr_1958]
- [Pfeifle et al 2022][research_pfeifle_notter_2022]
- [Phares 1981][research_phares_1981]
- [Phares and Kneile 1976][research_phares_kneile_1976]
- [Phillips 1948][research_phillips_1948]
- [Phillips 1984][research_phillipsps_1984]
- [Phillips and Waggoner 1988][research_phillips_waggoner_1988]
- [Phillips and Waggoner 1990][research_phillips_waggoner_1990]
- [Phillips and West 2019][research_phillips_west_2019]
- [Phillips et al 2003][research_phillips_lambert_2003]
- [Physical Phenomena Associated with Unsteady Transonic Flows 1989][research_physical_phenomena_1989]
- [Physics-assisted reduced-order modeling for identifying dominant features of transonic buffet 2023][research_physics_assisted_reduced_order_2023]
- [Piatak 1994][research_piatak_1994]
- [Pickles and Narayanaswamy 2020][research_pickles_2020]
- [Piecewicz and Kindsvogel 1943][research_piecewicz_kindsvogel_1943]
- [Pierpont 1957][research_transonic_predict_1957]
- [Pierpont 1959][research_pierpontpk_1959]
- [Pierpont 1975][research_pierpontpk_1975]
- [Piette and Cazier 1989][research_piettedouglass_cazierfrankwjr_1989]
- [Piette et al 1985][research_piette_crooks_1985]
- [Pike 1999][research_pike_1999]
- [Pilyugin and Khlebnikov 2005][research_pilyugin_khlebnikov_2005]
- [Pindzola and Chew 1960][research_pindzola_chew_1960]
- [Pindzola and Mozer 1956][research_pindzola_mozer_1956]
- [Pinebrook and Dalton 1983][research_pinebrook_dalton_1983]
- [Pinebrook and Dalton 1983][research_pinebrook_dalton_1983_b]
- [Pipko 1966][research_pipko_1966]
- [Pirozzoli and Bernardini 2010][research_pirozzoli_bernardini_2010]
- [Pirozzoli and Bernardini 2010][research_pirozzoli_bernardini_2010_b]
- [Pirozzoli et al 2010][research_pirozzoli_bernardini_2010_c]
- [Pitt 1995][research_pitt_1995]
- [Pitt et al 2016][research_pitt_sexton_2016]
- [Pittman et al 1984][research_pittmanjl_millerds_1984]
- [Pittsburgh Univ Washington Dc Research Staff 1966][research_pittsburghunivwashingtondcresearchstaff_1966]
- [PIV investigation of high speed flow over a pitching airfoil 1994][research_piv_investigation_1994]
- [Plaban and Takahashi 2021][research_plaban_takahashi_2021]
- [Placek and Ruchała 2018][research_placek_ruchala_2018]
- [Placek and Stryczniewicz 2016][research_placek_stryczniewicz_2016]
- [Plante][research_plante]
- [Plante and Laurendeau 2019][research_plante_laurendeau_2019]
- [Plante et al 2017][research_plante_dandois_2017]
- [Plath][research_plath]
- [Plath et al 2024][research_plath_renac_2024]
- [Platou 1968][research_platou_1968]
- [Platzer 2010][research_platzer_2010]
- [Plentovich 1986][research_plentovicheb_1986]
- [Plentovich 1988][research_plentovich_1988]
- [Plentovich et al 1984][research_plentovicheb_ladsoncl_1984]
- [Plotkin 1972][research_plotkinkj_1972]
- [Plotkin 1978][research_plotkin_1978]
- [Polhamus 1950][research_x1_dynamic_stability_1950]
- [Polivanov 2018][research_polivanov_2018]
- [Polivanov 2022][research_polivanovpa_2022]
- [Polivanov and Sidorenko 2026][research_polivanov_sidorenko_2026]
- [Polivanov et al 2016][research_polivanov_sidorenko_2016]
- [Polivanov et al 2017][research_polivanov_sidorenko_2017]
- [Poll and Schumann 2024][research_poll_schumann_2024]
- [Polonsky 2026][research_polonsky_2026]
- [Pomeroy et al][research_brentwpomeroy_richardlcampbell]
- [Poole and Cromack 1970][research_poole_cromack_1970]
- [Poole et al 2026][research_poole_allen_2026]
- [Pope and Street 1959][research_pope_street_1959]
- [Popinski 2019][research_popinski_2019]
- [Poplingher and Raveh 2018][research_poplingher_raveh_2018]
- [Poplingher and Raveh 2022][research_poplingher_raveh_2022]
- [Poplingher et al 2019][research_poplingher_raveh_2019]
- [Poplingher et al 2022][research_poplingher_mallik_2022]
- [Porter 1965][research_porter_1965]
- [Potential Equation Methods for Transonic Flow Prediction 1982][research_potential_equation_1982]
- [Poth et al 1993][research_pothjr_fisher_1993]
- [Potter 1984][research_potter_1984]
- [Potter et al 1961][research_potter_kinslow_1961]
- [Pounds 1972][research_pounds_1972]
- [Pounds and Walker 1980][research_pounds_walker_1980]
- [Powers 1988][research_powers_1988]
- [Powers et al 1986][research_powerssheryllgoecke_huffmanjarrettk_1986]
- [Prabakar et al 2017][research_prabakar_srikanth_2017]
- [PrabhakaraRao and Sri Sampath. 2014][research_prabhakararao_v_2014]
- [Prakash et al 2009][research_prakash_uthup_2009]
- [Prandtl 1928][research_prandtl_1928]
- [Prata et al 2022][research_prata_2022]
- [Prediction and Verification of Aerodynamic Drag, Part II Wind-Tunnel/Flight Correlation of Lift, Drag, and Pitching Moment 1985][research_prediction_and_1985]
- [Prediction of transonic flutter for a supercritical wing by modified strip analysis and comparison with experiment 1981][research_prediction_of_1981]
- [Prescott 1963][research_prescott_1963]
- [Price 1978][research_price_1978]
- [Price 1979][research_price_jr_1979]
- [Price 1981][research_pricejr_1981]
- [Price and Earl A. 1981][research_price_earla_1981]
- [Prior et al 2023][research_prior_rozinka_2023]
- [Pritts 1974][research_pritts_1974]
- [Pritulo et al 1995][research_pritulo_gubanov_1995]
- [Probstein 1953][research_probstein_1953]
- [Progress of the X-15 Research Airplane Program 1965][research_progress_of_1965]
- [Propeller/Propfan In-Flight Thrust Determination][research_propeller_propfan_in_flight]
- [Properties and Design of Slender Aircraft for Supersonic Flight 2012][research_properties_and_2012]
- [Prudhomme and Seraudie][research_prudhomme_seraudie]
- [Pruett et al 1981][research_pruett_wolf_1981]
- [Pröbsting et al 2022][research_probsting_yang_2022]
- [Puentes and Takahashi 2024][research_puentes_takahashi_2024]
- [Purohit 1987][research_purohit_1987]
- [Purvis and Burkhalter 1979][research_purvis_burkhalter_1979]
- [Pushtaev 1989][research_pushtaev_1989]
- [Puspitasari and Napitupulu 2023][research_puspitasari_napitupulu_2023]
- [Puthisikamani et al 2023][research_puthisikamani_sreenivasaraja_2023]
- [Putnam and Mace 1983][research_putnam_mace_1983]
- [Putnam and Meyers 1975][research_putnam_meyers_1975]
- [Pyle 1965][research_pylejs_1965]
- [Qi et al 2012][research_qi_he_2012]
- [Qi et al 2014][research_qi_he_2014]
- [Qi et al 2026][research_qi_gao_2026]
- [Qian and Guan 2012][research_qian_guan_2012]
- [Qin 2012][research_qin_2012]
- [Qin et al 2000][research_qin_zhu_2000]
- [Qiu and Sun 2009][research_qiu_sun_2009]
- [Qu et al 2012][research_qu_zhang_2012]
- [Quadros et al 2018][research_quadros_khan_2018]
- [Quagliarella and Dell 1994][research_quagliarella_dell_1994]
- [Quasi-transonic Flow 1986][research_quasi_transonic_flow_1986]
- [Quast et al 1990][research_quast_henke_1990]
- [Quinn 1999][research_quinn_1999]
- [Quinn and Olinger 1969][research_robertdquinn_frankvolinger_1969]
- [Raab and Rohde-Brandenburger 2020][research_raab_rohdebrandenburger_2020]
- [Radespiel 1989][research_radespiel_1989]
- [Raghunathan 1983][research_raghunathan_1983]
- [Raghunathan and Coll 1981][research_raghunathan_coll_1981]
- [Raghunathan and McAdam 1985][research_raghunathan_mcadam_1985]
- [Raghunathan and McLlwain 1990][research_raghunathan_mcllwain_1990]
- [Raghunathan et al 1979][research_raghunathan_coll_1979]
- [Raghunathan et al 1998][research_raghunathan_mitchell_1998]
- [Ragni et al 2009][research_ragni_ashok_2009]
- [Ragni et al 2010][research_ragni_vanoudheusden_2010]
- [Rahman et al 2015][research_rahman_hasan_2015]
- [Rahman et al 2015][research_rahman_labib_2015]
- [Rahman et al 2016][research_rahman_labib_2016]
- [Rahman et al 2025][research_rahman_vowotor_2025]
- [Rainey and Igoe 1958][research_buffet_loads_1958]
- [Raj 1983][research_raj_1983]
- [Raj 1984][research_raj_1984]
- [Raj and Brennan 1987][research_raj_brennan_1987]
- [Rajagopal and Ortiz 1998][research_rajagopal_ortiz_1998]
- [Rajamurthy 2002][research_rajamurthy_2002]
- [Rakin 1981][research_rakin_1981]
- [Ram et al 1985][research_ram_vemuru_1985]
- [Ramachandra et al 1980][research_ramachandra_sudhakar_1980]
- [Ramachandra et al 2023][research_k_bhardwaj_2023]
- [Ramamurthy and Ghaly 2009][research_ramamurthy_ghaly_2009]
- [Ramaswamy and Schreyer 2021][research_ramaswamy_schreyer_2021]
- [Ramaswamy and Schreyer 2022][research_ramaswamy_schreyer_2022]
- [Ramaswamy and Schreyer 2026][research_ramaswamy_schreyer_2026]
- [Ramaswamy and Viswanathan 1975][research_ramaswamy_viswanathan_1975]
- [Ramey et al][research_jmichealramey_martinksekula]
- [Ramkumar and Weisshaar 1977][research_ramkumar_weisshaar_1977]
- [Ramm 1990][research_ramm_1990]
- [Ramm 1990][research_ramm_1990_b]
- [Ramm 1990][research_ramm_1990_c]
- [Ramm 1990][research_ramm_1990_d]
- [Ramm 1990][research_ramm_1990_e]
- [Ran et al 2026][research_ran_wang_2026]
- [Ranaudo et al 1986][research_ranaudorj_mikkelsenkl_1986]
- [Ranawake 2015][research_ranawake_2015]
- [Ranlet 1965][research_ranlet_1965]
- [Rasuo 2006][research_rasuo_2006]
- [Rasuo 2006][research_rasuo_2006_b]
- [Ratcliff and Carlson 1989][research_ratcliff_carlson_1989]
- [Rathert et al 1949][research_rathertgeorgeajr_hansoncarlm_1949]
- [Ratliff and Pagilla 2008][research_ratliff_pagilla_2008]
- [Ratnayake 2010][research_ratnayake_2010]
- [Raveh 2008][research_raveh_2008]
- [Raveh 2011][research_raveh_2011]
- [Ray 1994][research_ray_1994]
- [Ray and Ladson 1984][research_rayej_ladsoncl_1984]
- [Ray et al 1974][research_ray_kilgore_1974]
- [Ray et al 2002][research_rayronaldj_cobleighbrentr_2002]
- [Re 1974][research_rerj_1974]
- [Reaser et al 1983][research_reaser_hallissy_1983]
- [Recommended Practice Calibration of Subsonic and Transonic Wind Tunnels AIAA R-093-2003 2018 2003][research_recommended_practice_2003]
- [Reda and Murphy 1972][research_redadc_murphyjd_1972]
- [Reddy et al 1988][research_reddy_srivastava_1988]
- [Redeker and Voersmann 1988][research_redeker_voersmann_1988]
- [Redeker et al 1986][research_redeker_wichmann_1986]
- [Redford et al 2012][research_redford_sandham_2012]
- [Rediniotis et al 1994][research_rediniotis_klute_1994]
- [Reed 1955][research_x5_tail_loads_1955]
- [Reed 1975][research_reedwhiii_1975]
- [Reed 1976][research_reedwhiii_1976]
- [Reed 1984][research_reed_1984]
- [Reed 1985][research_reedwhiii_1985]
- [Reed 1990][research_reed_1990]
- [Regan 1964][research_regan_1964]
- [Regier et al 1947][research_regierarthura_barmbyjohng_1947]
- [Reibert et al 1997][research_reibert_saric_1997]
- [Reichert 1947][research_reichert_1947]
- [Reimann 2016][research_reimann_2016]
- [Rein et al 2009][research_rein_rosemann_2009]
- [Rein et al 2025][research_rein_henne_2025]
- [Reinhardt 1948][research_reinhardt_1948]
- [Reis et al 2014][research_reis_falcaofilho_2014]
- [Reising and Davis][research_heathhreising_davidodavis]
- [Reising et al][research_heathhreising_jonathansasson]
- [Reissner 1943][research_reissner_1943]
- [Rekhy et al 2020][research_rekhy_shneider_2020]
- [Rembaut and Brion 2026][research_rembaut_brion_2026]
- [Ren et al 2020][research_ren_chen_2020]
- [Ren et al 2022][research_ren_gao_2022]
- [Ren et al 2026][research_ren_ma_2026]
- [Report no. 264, Differential pressures on a pitot-venturi and pitot-static nozzle over 360° Pitch and Yaw 1927][research_report_no_1927]
- [Report No. 637, Determination of boundary-layer transition on three symmetrical airfoils in the N. A. C. A. full-scale wind tunnel 1939][research_report_no_1939]
- [Research-Airplane-Committee Report on Conference on the Progress of the X-15 Project A Compilation of the Papers Presented 1958][research_research_airplane_committee_report_1958]
- [Resende et al 1997][research_resende_nakagawa_1997]
- [Resonance prediction for slotted wind tunnel by the finite element method 1986][research_resonance_prediction_1986]
- [Reubush 1975][research_reubush_1975]
- [Reuther et al 1992][research_reuther_vandam_1992]
- [Review of Transonic Aerodynamics 1982][research_review_of_1982]
- [Reynolds Averaged Navier-Stokes Computations of Transonic Flows-the State-of-the-Art 1982][research_reynolds_averaged_1982]
- [Reynolds et al][research_jamesreynolds_ethanbaumann]
- [Rhoads 1952][research_rhoads_1952]
- [Ricci et al 2006][research_ricci_scotti_2006]
- [Rice 1946][research_rice_1946]
- [Richard and Putter 2003][research_richard_putter_2003]
- [Richardson 1976][research_richardson_1976]
- [Richey et al 1976][research_richey_petersen_1976]
- [Richter and Rosemann 2002][research_richter_rosemann_2002]
- [Richter and Rosemann 2011][research_richter_rosemann_2011]
- [Richwine and Del Frate 1995][research_richwinedavidm_delfratejohnh_1995]
- [Riddle 1975][research_riddledw_1975]
- [Riddle et al 1981][research_riddle_innis_1981]
- [Riebe and MacLeod 1950][research_riebejohnm_macleodrichardg_1950]
- [Riggins et al 1999][research_riggins_nelson_1999]
- [Rill and Becker 1992][research_rill_becker_1992]
- [Rimer et al 1983][research_rimer_chipman_1983]
- [Ringas 2022][research_ringas_2022]
- [Riou et al 2010][research_riou_garnier_2010]
- [Riso et al 2018][research_riso_divincenzo_2018]
- [Ristić 1991][research_ristic_1991]
- [Rittenhouse 1959][research_rittenhouse_1959]
- [Rivera and Florance 2000][research_rivera_florance_2000]
- [Rivers and Wahls 1994][research_riversmelissab_wahlsricharda_1994]
- [Rivers et al 2001][research_rivers_wahls_2001]
- [Rizk 1980][research_rizk_1980]
- [Rizk 1981][research_rizk_1981]
- [Rizk 1982][research_rizk_1982]
- [Rizk 1986][research_rizk_1986]
- [Rizk and Lovell 1986][research_rizk_lovell_1986]
- [Rizk and Smithmeyer 1982][research_rizk_smithmeyer_1982]
- [Rizk et al 1988][research_rizk_lovell_1988]
- [Rizzetta 1977][research_rizzetta_1977]
- [Rizzetta 1977][research_rizzetta_1977_b]
- [Rizzetta and Yoshihara 1980][research_rizzetta_yoshihara_1980]
- [Rizzi 1981][research_rizzi_1981]
- [Rizzi 1981][research_rizzi_1981_b]
- [Rizzi 1982][research_rizzi_1982]
- [Rizzi 1985][research_rizzi_1985]
- [Rizzi 1995][research_rizzi_1995]
- [Rizzi and Eriksson 1981][research_rizzi_eriksson_1981]
- [Rizzi and Schmidt 1978][research_rizzi_schmidt_1978]
- [Rizzi et al 1986][research_rizzi_purcell_1986]
- [Roach and Froning 1996][research_roach_froning_1996]
- [Roberts 1963][research_roberts_1963]
- [Roberts 1963][research_roberts_1963_b]
- [Roberts et al 1966][research_roberts_smith_1966]
- [Roberts et al 2012][research_roberts_reed_2012]
- [Robinson 1948][research_robinsonharoldl_1948]
- [Robinson 1953][research_robinsonharoldl_1953]
- [Robinson 1954][research_robinsonrossb_1954]
- [Robinson 1978][research_robinson_1978]
- [Robinson and Becker 1942][research_cowling_highspeed_1942]
- [Robinson and Blanchard 2003][research_robinson_blanchard_2003]
- [Robinson and High 1974][research_robinson_high_1974]
- [Robinson and Robinson 1950][research_robinson_robinson_1950]
- [Robinson et al 1955][research_robinsonglennh_cothrengeorgeejr_1955]
- [Robinson et al 1974][research_robinson_high_1974_b]
- [Rocket-Powered Aircraft 2017][research_rocket_powered_aircraft_2017]
- [Rodarte Ricciardi and Wolf 2020][research_rodartericciardi_wolf_2020]
- [Rodarte Ricciardi et al 2021][research_rodartericciardi_wolf_2021]
- [Rodemich and Andrew 1965][research_rodemich_andrew_1965]
- [Rodi et al 2019][research_rodi_stoldt_2019]
- [Rodriguez et al 2022][research_rodriguez_hickey_2022]
- [Roecker 1955][research_roecker_1955]
- [Roepke 1972][research_roepke_1972]
- [Rogers 1953][research_x1_tail_loads_1953]
- [Rogers 1970][research_rogers_1970]
- [Rogers 2010][research_rogers_2010]
- [Rogers and Walter K. 1953][research_rogers_walterk_1953]
- [Rogers and Walter K. 1958][research_rogers_walterk_1958]
- [Roh et al 2006][research_roh_park_2006]
- [Roiati et al 2023][research_roiati_anderson_2023]
- [Roidl et al 2011][research_roidl_meinke_2011]
- [Rokoni and Hasan 2013][research_rokoni_hasan_2013]
- [Rom 1965][research_rom_1965]
- [Roohani and Skews 2009][research_roohani_skews_2009]
- [Rooney et al 1977][research_rooney_craig_1977]
- [Roos 1979][research_roos_1979]
- [Roos 1980][research_roos_1980]
- [Roos 1985][research_roosfw_1985]
- [Roos and Riddle 1977][research_roosfw_riddledw_1977]
- [Roscoe et al 1984][research_roscoe_shamroth_1984]
- [Rose 1970][research_rosewc_1970]
- [Rose and Seginer 1977][research_rose_seginer_1977]
- [Rose and Seginer 1978][research_rose_seginer_1978]
- [Rosemann and Birkemeyer 2002][research_rosemann_birkemeyer_2002]
- [Rosen 1984][research_rosen_1984]
- [Rosen 1985][research_rosen_1985]
- [Rosen 1988][research_rosen_1988]
- [Rosenberg 1944][research_rosenberg_1944]
- [Rosenberg and Schuch 1983][research_rosenberg_schuch_1983]
- [Rosenhead 1956][research_rosenhead_1956]
- [Ross 1987][research_rossdavids_1987]
- [Ross 2021][research_ross_2021]
- [Roth and Barrett 2009][research_roth_barrett_2009]
- [Rothmund and Harlow 1999][research_rothmund_harlow_1999]
- [Roussel et al 2015][research_roussel_alizard_2015]
- [Row and Fischel 1963][research_row_fischel_1963]
- [Roy et al 2021][research_roy_das_2021]
- [Roy et al 2021][research_roy_sandhu_2021]
- [Rubbert et al 1976][research_rubbertpe_lup_1976]
- [Rubin 1971][research_rubin_1971]
- [Ruetenik and Smiley 1978][research_ruetenik_smiley_1978]
- [Ruhlin and Murphy 1981][research_ruhlin_murphy_1981]
- [Ruhlin and Pratt-Barlow 1981][research_ruhlin_prattbarlow_1981]
- [Ruhlin and Sandford 1975][research_ruhlincl_sandfordmc_1975]
- [Ruhlin and Tuovila 1961][research_ruhlincharlesl_tuovilawj_1961]
- [Ruhlin and Young 1964][research_ruhlincl_youngls_1964]
- [Ruhlin et al 1968][research_ruhlincl_sandfordmc_1968]
- [Ruhlin et al 1974][research_ruhlin_destuynder_1974]
- [Ruhlin et al 1976][research_ruhlincl_doggettrvjr_1976]
- [Ruhlin et al 1980][research_ruhlincl_doggettrvjr_1980]
- [Ruhlin et al 1982][research_ruhlin_rauchjr_1982]
- [Ruhlin et al 1983][research_ruhlin_rauch_1983]
- [Ruhlin et al 1986][research_ruhlincl_bhatiakg_1986]
- [Rumph and Schairer 1940][research_rumph_schairer_1940]
- [Rumsey 2010][research_rumseychristopherl_2010]
- [Rumsey et al 1987][research_rumsey_thomas_1987]
- [Runckel and Henderson 1952][research_vortex_generator_1952]
- [Runyan and Steers 1980][research_ljamesrunyan_louislsteers_1980]
- [Runyan and Woolston 1957][research_runyanharryl_woolstondonalds_1957]
- [Runyan et al 1952][research_runyan_cunningham_1952]
- [Ruo 1978][research_ruosy_1978]
- [Ruo et al 1973][research_ruo_theisen_1973]
- [Rusak 1993][research_rusak_1993]
- [Rusak 1994][research_rusak_1994]
- [Rusak and Wang 1999][research_rusak_wang_1999]
- [Rusak and Webster 1992][research_rusak_webster_1992]
- [Rushton 1966][research_rushton_1966]
- [Russell et al 2022][research_russell_werner_2022]
- [Russo et al 2020][research_russo_tognaccini_2020]
- [Russo et al 2020][research_russo_tognaccini_2020_b]
- [Ruyten 1999][research_ruyten_1999]
- [Ryzhov 1993][research_ryzhov_1993]
- [Saadeh et al 2026][research_saadeh_chau_2026]
- [Sabin 1957][research_sabin_1957]
- [Sabzehparvar 2005][research_sabzehparvar_2005]
- [Sachs 1969][research_sachs_1969]
- [Sachs 1977][research_sachs_1977]
- [Sachs 1980][research_sachs_1980]
- [Sadoff 1953][research_sadoffmelvin_1953]
- [Safronov and Safronov 1994][research_safronov_safronov_1994]
- [Safronov et al 2023][research_safronov_semon_2023]
- [Safronov et al 2024][research_safronov_semon_2024]
- [Sahu 1986][research_sahu_1986]
- [Sahu 1988][research_sahu_1988]
- [Sahu 1990][research_sahu_1990]
- [Sahu 2007][research_sahu_2007]
- [Sahu 2008][research_sahu_2008]
- [Sahu 2009][research_sahu_2009]
- [Sahu 2011][research_sahu_2011]
- [Sahu and Danberg 1987][research_sahu_danberg_1987]
- [Sahu and Heavey 1995][research_sahu_heavey_1995]
- [Sahu et al 1982][research_sahu_nietubicz_1982]
- [Sahu et al 1983][research_sahu_nietubicz_1983]
- [Sahu et al 1983][research_sahu_nietubicz_1983_b]
- [Sahyoun et al 2026][research_sahyoun_boose_2026]
- [Saitoh et al 1995][research_saitoh_hashidate_1995]
- [Saitoh et al 2012][research_saitoh_tamayama_2012]
- [Sajben and Kroutil 1979][research_sajben_kroutil_1979]
- [Sajben et al 1982][research_sajben_bogar_1982]
- [Sakaki et al 2015][research_sakaki_kakudo_2015]
- [Sakaki et al 2016][research_sakaki_kakudo_2016]
- [Sakata 2002][research_sakata_2002]
- [Sakurai 1959][research_sakurai_1959]
- [Saltzman 1953][research_x1_liftdrag_1953]
- [Saltzman and Ayers 1981][research_saltzman_ayers_1981]
- [Saltzman and Ayers 1982][research_saltzman_ayers_1982]
- [Saltzman and Ayers 1995][research_supersonic_research_1995]
- [Saltzman et al 1994][research_fsw_liftdrag_1994]
- [Samant and Wigton 1983][research_samant_wigton_1983]
- [Sammonds 1970][research_sammonds_1970]
- [Samputh et al 2024][research_samputh_moey_2024]
- [Sanderson 1965][research_sanderson_1965]
- [Sandford et al 1974][research_sandford_abel_1974]
- [Sandford et al 1974][research_sandfordmc_ruhlincl_1974]
- [Sang and Schetz 2002][research_sang_schetz_2002]
- [Sanghi et al 2020][research_sanghi_riso_2020]
- [Sanghi et al 2025][research_sanghi_riso_2025]
- [Sangwan et al 2017][research_sangwan_sengupta_2017]
- [Sankar and Tassa 1980][research_sankar_tassa_1980]
- [Sankar and Tassa 1981][research_sankar_tassa_1981]
- [Sankar et al 1985][research_sankar_malone_1985]
- [Sansica and Hashimoto 2023][research_sansica_hashimoto_2023]
- [Sansica and Hashimoto 2023][research_sansica_hashimoto_2023_b]
- [Sansica et al 2013][research_sansica_sandham_2013]
- [Sansica et al 2014][research_sansica_sandham_2014]
- [Saric 1997][research_saric_1997]
- [Saric 1998][research_saric_1998]
- [Saric 2010][research_saric_2010]
- [Sarigul-Klijn et al 2005][research_sarigulklijn_sarigulklijn_2005]
- [Sarigul-Klijn et al 2006][research_sarigulklijn_sarigulklijn_2006]
- [Sarigul-Klijn et al 2008][research_sarigulklijn_sarigulklijn_2008]
- [Sarigulklijn et al 2012][research_sarigulklijn_sarigulklijn_2012]
- [Sarkar 1994][research_sarkar_1994]
- [Sarlak 2017][research_sarlak_2017]
- [Sarohia 1977][research_sarohia_1977]
- [Sarohia et al 1980][research_sarohia_parthasarathy_1980]
- [Sartor][research_sartor]
- [Sartor et al 2012][research_sartor_losfeld_2012]
- [Sartor et al 2013][research_sartor_clement_2013]
- [Sashida et al 2024][research_sashida_aoyama_2024]
- [Sashida et al 2026][research_sashida_kawai_2026]
- [Sasson et al][research_jonathansasson_heathhreising]
- [Sasson et al 2022][research_sbli_experiments_2022]
- [Satyanarayana et al 1981][research_satyanarayana_schairer_1981]
- [Saunders 1996][research_saunders_1996]
- [Savage and Bommerscheim 1962][research_savage_bommerscheim_1962]
- [Savin 1958][research_savinraymondc_1958]
- [Savin 2019][research_savin_2019]
- [Sawyer and Trant 1947][research_sawyerrichardh_trantjamespjr_1947]
- [Sawyer and Trant 1950][research_sawyerrichardh_trantjamespjr_1950]
- [Sayers 1936][research_sayers_1936]
- [Scafetta 1983][research_scafetta_1983]
- [Scanlan 1948][research_scanlan_1948]
- [Schaechterle et al 1982][research_schaechterleg_ludewigkh_1982]
- [Schaeffler and Telionis 1998][research_schaeffler_telionis_1998]
- [Schairer 1994][research_schaireredwardt_1994]
- [Schairer and Mendoza 1982][research_schaireret_mendozajp_1982]
- [Schairer et al 1989][research_schaireredwardt_leegeorge_1989]
- [Schairer et al 1991][research_schaireredwardt_leegeorge_1991]
- [Schauerte and Schreyer 2022][research_schauerte_schreyer_2022]
- [Schauerte and Schreyer 2023][research_schauerte_schreyer_2023]
- [Schauerte and Schreyer 2023][research_schauerte_schreyer_2023_b]
- [Schauerte and Schreyer 2024][research_schauerte_schreyer_2024]
- [Schauerte and Schreyer 2025][research_schauerte_schreyer_2025]
- [Schauerte and Schreyer 2025][research_schauerte_schreyer_2025_b]
- [Schauerte and Schreyer 2025][research_schauerte_schreyer_2025_c]
- [Schauerte et al 2026][research_schauerte_kwong_2026]
- [Schermerhorn 1969][research_schermerhorn_1969]
- [Schermerhorn and DeMeritte 1960][research_schermerhorn_demeritte_1960]
- [Schewe and Mai 2018][research_schewe_mai_2018]
- [Schewe and Mai 2019][research_schewe_mai_2019]
- [Schiavetta et al 2006][research_schiavetta_boelens_2006]
- [Schlinker et al 2010][research_schlinker_simonich_2010]
- [Schloemer 1966][research_schloemer_1966]
- [Schmeer and Runckel 1962][research_schmeerjamesw_runckeljackf_1962]
- [Schmidt 1979][research_schmidt_1979]
- [Schmisseur and Dolling 1992][research_schmisseur_dolling_1992]
- [Schmitt et al 1983][research_schmitt_destarac_1983]
- [Schmitt et al 1990][research_schmitt_reneaux_1990]
- [Schnerr and Dohrmann 1991][research_schnerr_dohrmann_1991]
- [Schnerr and Dohrmann 1994][research_schnerr_dohrmann_1994]
- [Schoneich et al][research_antoniogiovannischoneich_thomasjwhalen]
- [Schoolfield 1942][research_schoolfield_1942]
- [Schouten and Bakker 2000][research_schouten_bakker_2000]
- [Schrauf et al 1998][research_schrauf_perraud_1998]
- [Schreyer 2023][research_schreyer_2023]
- [Schröder and Meijering 2005][research_schroder_meijering_2005]
- [Schuelein 2014][research_schuelein_2014]
- [Schumacher 1952][research_schumacher_1952]
- [Schuman 2018][research_schuman_2018]
- [Schuster and Byrd 2003][research_schusterdavidm_byrdjamese_2003]
- [Schwartz et al 2024][research_schwartz_gudmundsson_2024]
- [Schwartzberg 1975][research_schwartzberg_1975]
- [Schwarzt and Wuest 1964][research_schwarzt_wuest_1964]
- [Sclafani et al 2010][research_sclafani_dehaan_2010]
- [Scott et al 2024][research_scott_candon_2024]
- [Sears 1947][research_sears_1947]
- [Sebastia and Hornung 2023][research_sebastia_hornung_2023]
- [Sebastia et al 2024][research_sebastia_wurz_2024]
- [Seckel 1964][research_seckel_1964]
- [Sedin and Sorensen 1984][research_sedin_sorensen_1984]
- [Sedin and Sorensen 1986][research_sedin_sorensen_1986]
- [Sedney 1954][research_sedney_1954]
- [Seebass 1974][research_seebassar_1974]
- [Seebass 1982][research_seebass_1982]
- [Seebass and Yu 1976][research_seebassar_yunj_1976]
- [Seegmiller et al 1978][research_seegmillerhl_marvinjg_1978]
- [Sefic and Maxwell 1987][research_seficwalterj_maxwellcleom_1987]
- [Segee et al 2016][research_segee_schetz_2016]
- [Seginer and Rose 1976][research_seginer_rose_1976]
- [Seginer and Rose 1977][research_seginer_rose_1977]
- [Seidel et al 1985][research_seidel_sandford_1985]
- [Seider and Haenel 1991][research_seider_haenel_1991]
- [Seifert and Pack 2001][research_seifert_pack_2001]
- [Selberg et al 1991][research_selbergbrucep_rokhsazkamran_1991]
- [Selerowicz 2020][research_selerowicz_2020]
- [Sellers 1958][research_allmovable_flutter_1958]
- [Sellers and Chandra 1997][research_sellers_chandra_1997]
- [Sengupta et al 2021][research_sengupta_roy_2021]
- [Sengupta et al 2022][research_sengupta_chakraborty_2022]
- [Seraj and Martins 2023][research_seraj_martins_2023]
- [Seraj and Martins 2025][research_seraj_martins_2025]
- [Seraudie et al 1985][research_seraudiea_blancharda_1985]
- [Serdarevic-Kadic and Terzic 2019][research_serdarevickadic_terzic_2019]
- [Settles 1981][research_settles_1981]
- [Settles and Bogdonoff 1981][research_settlesgs_bogdonoffsm_1981]
- [Sevost'ianow 1967][research_sevostianow_1967]
- [Sewall 1984][research_sewall_1984]
- [Sewall et al 1985][research_sewallwilliamg_mcgheerobertj_1985]
- [Sforza 2018][research_sforza_2018]
- [Sforza 2020][research_sforza_2020]
- [Shahjahan and Ahuja 2026][research_shahjahan_ahuja_2026]
- [Shahrokhi and Jahangirian 2010][research_shahrokhi_jahangirian_2010]
- [Shanbhag and Narasimha 1970][research_shanbhag_narasimha_1970]
- [Shang et al 1976][research_shang_hankeyjr_1976]
- [Shankar 2013][research_shankar_2013]
- [Shankar and Goebel 1985][research_shankar_goebel_1985]
- [Shankar and Ide 1989][research_shankar_ide_1989]
- [Shankar and Malmuth 1982][research_shankar_malmuth_1982]
- [Shankar et al 1978][research_shankar_malmuth_1978]
- [Shankar et al 1979][research_shankar_malmuth_1979]
- [Shankar et al 1979][research_shankar_malmuth_1979_b]
- [Shannon 1948][research_shannon_1948]
- [Shantz 1953][research_shantz_1953]
- [Shao et al 2026][research_shao_he_2026]
- [Sharma and Ghosh 2014][research_sharma_ghosh_2014]
- [Shea 1978][research_sheaiii_1978]
- [Shearin and Jones 1989][research_shearin_jones_1989]
- [Sheibani et al 2024][research_sheibani_jafarian_2024]
- [Sheila Tobing 2022][research_sheilatobing_2022]
- [Shen and Zuo 2026][research_shen_zuo_2026]
- [Sheng et al 2007][research_sheng_galbraith_2007]
- [Shepheard 1965][research_shepheard_1965]
- [Sheridan et al 2017][research_sheridan_young_2017]
- [Sherrouse and McWhorter 1992][research_sherrouse_mcwhorter_1992]
- [Sheta 2004][research_sheta_2004]
- [Shi et al 2019][research_shi_wen_2019]
- [Shi et al 2020][research_shi_chen_2020]
- [Shi et al 2023][research_shi_he_2023]
- [Shibata et al 2018][research_shibata_tanaka_2018]
- [Shieh 1988][research_shieh_1988]
- [Shimada et al 2009][research_shimada_shiratori_2009]
- [Shinde and Gaitonde 2022][research_shinde_gaitonde_2022]
- [Shipilin 1964][research_shipilin_1964]
- [Shiqi et al 2018][research_shiqi_tian_2018]
- [Shmikovich and Caughey 1981][research_shmikovicha_caugheyda_1981]
- [Shmilovich and Caughey][research_shmilovich_caughey]
- [Shmilovich and Caughey 1982][research_shmilovich_caughey_1982]
- [Shmilovich and Caughey 1985][research_shmilovich_caughey_1985]
- [Shmyglevskii 1960][research_shmyglevskii_1960]
- [Shou-ying and Shi-jun 1982][research_shouying_shijun_1982]
- [Shubham et al 2022][research_shubham_sandberg_2022]
- [Sichel 1970][research_sichel_1970]
- [Sichel and Yin 1966][research_sichel_yin_1966]
- [Sickles and Erickson 1990][research_sickles_ericksonjr_1990]
- [Siclari 1982][research_siclarimj_1982]
- [Siclari et al 1996][research_siclari_vannostrand_1996]
- [Sidorenko et al 2017][research_sidorenko_budovskii_2017]
- [Sidorenko et al 2018][research_sidorenko_kirilovskiy_2018]
- [Siemers et al 1983][research_siemersiii_wolf_1983]
- [Sieradzki 2016][research_sieradzki_2016]
- [Sigal 1984][research_sigal_1984]
- [Silsby and Kennedy 1947][research_silsbynormans_kennedyrobertm_1947]
- [Silva 1993][research_silva_1993]
- [Silva and Bennett 1990][research_silva_bennett_1990]
- [Silva and Bennett 1992][research_silva_bennett_1992]
- [Silva and Bennett 1995][research_silva_bennett_1995]
- [Silva et al 2002][research_silva_mello_2002]
- [Silva et al 2004][research_silva_mello_2004]
- [Silva et al 2005][research_silva_mello_2005]
- [Silva et al 2006][research_silva_mello_2006]
- [Silva et al 2006][research_silva_mello_2006_b]
- [Silvers and King 1955][research_silvershnorman_kingthomasjjr_1955]
- [Sim 1997][research_simalexg_1997]
- [Sim and Curry 1978][research_simag_curryre_1978]
- [Sim and Curry 1984][research_simag_curryre_1984]
- [Simpson 1972][research_simpson_1972]
- [Simpson 1979][research_simpson_1979]
- [Sims and Carter 1981][research_sims_carter_1981]
- [Simsek and Tekinalp 2015][research_simsek_tekinalp_2015]
- [Sinaga et al 2024][research_sinaga_yunianto_2024]
- [Sinclair 1981][research_sinclair_1981]
- [Sinclair 1988][research_sinclair_1988]
- [Sinclair 1996][research_sinclair_1996]
- [Sinclair and Mace 1956][research_pitot_vane_1956]
- [Singh and Dwivedi 2022][research_singh_dwivedi_2022]
- [Singh and McDonough 2014][research_singh_mcdonough_2014]
- [Singh and Sasidharan 2026][research_singh_sasidharan_2026]
- [Singh and Venkatraman 2023][research_singh_venkatraman_2023]
- [Singh and Venkatraman 2026][research_singh_venkatraman_2026]
- [Singh et al 2016][research_singh_mishra_2016]
- [Singh et al 2022][research_singh_karnick_2022]
- [Singhasenee et al 2026][research_singhasenee_lamon_2026]
- [Sinha 2007][research_sinha_2007]
- [Sinha 2024][research_sinha_2024]
- [Sinkovec et al 2015][research_sinkovec_loshek_2015]
- [Sirieix et al][research_sirieix_delery]
- [Sisk and Andrews 1963][research_sisk_andrews_1963]
- [Sisk and Mooney 1953][research_siskthomasr_mooneyjohnm_1953]
- [Siva Krishna Reddy et al 2021][research_sivakrishnareddy_sah_2021]
- [Sivasubramanian and Fasel 2015][research_sivasubramanian_fasel_2015]
- [Sjoberg 1950][research_sjobergsa_1950]
- [Sjoberg and Champine 1949][research_sjobergsa_champinera_1949]
- [Sjoberg et al 1951][research_sjobergsa_peelejamesr_1951]
- [Sklar and Rusak 2020][research_sklar_rusak_2020]
- [Sklenář and Matějů 2022][research_sklenar_mateju_2022]
- [Skujins and Cesnik 2011][research_skujins_cesnik_2011]
- [Slapnicar][research_slapnicar]
- [Slingerland 2003][research_slingerland_2003]
- [Slingerland 2005][research_slingerland_2005]
- [Sloan et al 1962][research_sloan_eh_1962]
- [Small-Disturbance Theory 1959][research_small_disturbance_theory_1959]
- [Smetana 1965][research_smetana_1965]
- [Smetana 1973][research_smetana_1973]
- [Smetana and Knepper 1973][research_smetana_knepper_1973]
- [Smith 1953][research_smith_1953]
- [Smith 1954][research_smithnormanf_1954]
- [Smith 1954][research_smithwilliardg_1954]
- [Smith 1958][research_smithccjr_1958]
- [Smith 1958][research_smithcharlescjr_1958]
- [Smith 1959][research_x1e_stability_1959]
- [Smith 1961][research_smithcharlescjr_1961]
- [Smith 1966][research_smith_1966]
- [Smith 1974][research_smithhc_1974]
- [Smith 1997][research_smith_1997]
- [Smith and Campbell 1992][research_smithleighann_campbellrichardl_1992]
- [Smith and Cebeci 1967][research_smith_cebeci_1967]
- [Smith and Farbridge 1979][research_smithronaldc_farbridgeje_1979]
- [Smith and Klettner 2022][research_smith_klettner_2022]
- [Smith and Richards 2023][research_smith_richards_2023]
- [Smith et al 2004][research_smith_babinsky_2004]
- [Smith et al 2008][research_smith_henfling_2008]
- [Smith et al 2026][research_smith_karns_2026]
- [Smits 1988][research_smits_1988]
- [Smits and Miles 2002][research_smits_miles_2002]
- [Smolderen 1972][research_smolderen_1972]
- [Snyder 1987][research_snyder_1987]
- [Sobieczky 1979][research_sobieczky_1979]
- [Sobieczky 1983][research_sobieczky_1983]
- [Sobieczky 1984][research_sobieczky_1984]
- [Sobieczky and Dulikravich 1993][research_sobieczky_dulikravich_1993]
- [Sobieczky and Giessler 1999][research_sobieczky_giessler_1999]
- [Sogukpinar 2018][research_sogukpinar_2018]
- [Sohn and Lee 2000][research_sohn_lee_2000]
- [Solarte-Pineda et al 2026][research_solartepineda_bravomosquera_2026]
- [Solies 1992][research_solies_1992]
- [Solies 1992][research_solies_1992_b]
- [Solies 1994][research_solies_1994]
- [Soltani and Farahani 2011][research_soltani_farahani_2011]
- [Soltani et al 2011][research_soltani_marzabadi_2011]
- [Solution of the Transonic Small Disturbance Equation 2014][research_solution_of_2014]
- [Somers 2005][research_somers_2005]
- [Soneda et al 2025][research_soneda_tsushima_2025]
- [Song et al 2011][research_song_lu_2011]
- [Song et al 2024][research_song_wong_2024]
- [Song et al 2025][research_song_wong_2025]
- [Soontornpasatch 2018][research_soontornpasatch_2018]
- [Soontornpasatch 2018][research_soontornpasatch_2018_b]
- [Sorbilli et al 2018][research_sorbilli_dibianchi_2018]
- [Sorensen and Blevins 2001][research_sorensen_blevins_2001]
- [Sotoudeh and Ferman 2019][research_sotoudeh_ferman_2019]
- [Sotoudeh et al 2010][research_sotoudeh_hodges_2010]
- [Soudakov et al 2017][research_soudakov_petrov_2017]
- [Soudakov et al 2017][research_soudakov_sidorenko_2017]
- [South 1985][research_southjr_1985]
- [Souza Coimbra et al 2022][research_souzacoimbra_matoscampos_2022]
- [Spacht 1980][research_spacht_1980]
- [Spahr and Kyrlach 1960][research_spahr_kyrlach_1960]
- [Spaid 1984][research_spaid_1984]
- [Spaid and Lynch 1996][research_spaid_lynch_1996]
- [Spaid et al 1983][research_spaidfw_dahlinja_1983]
- [Sparkes 2024][research_sparkes_2024]
- [Spearman 1953][research_spearmanmleroy_1953]
- [Spearman 1979][research_spearmanml_1979]
- [Spinner and Rudnik 2023][research_spinner_rudnik_2023]
- [Spitzer et al 1972][research_spitzerre_rumseypc_1972]
- [Spottswood et al 2015][research_spottswood_beberniss_2015]
- [Spreiter 1959][research_spreiter_1959]
- [Spreiter 1964][research_spreiter_1964]
- [Springer 1998][research_springer_1998]
- [Spurlin and Lueck 1984][research_spurlin_lueck_1984]
- [Squire 1965][research_squire_1965]
- [Squire 1975][research_squire_1975]
- [Squire and Nasser 1993][research_squire_nasser_1993]
- [Srakowski et al 1980][research_srakowski_shrewsbury_1980]
- [Sreekanth 1961][research_sreekanth_1961]
- [Sreekanth 1962][research_sreekanth_1962]
- [Sreenivasulu et al 2025][research_sreenivasulu_neelapu_2025]
- [Srichitturi 2026][research_srichitturi_2026]
- [Sridharan et al 2024][research_sridharan_padmanabhan_2024]
- [Srinivasan and Steger 1981][research_srinivasang_stegerjl_1981]
- [Srinivasan et al 1981][research_srinivasan_chyu_1981]
- [Srinivasan et al 1984][research_srinivasan_mccroskey_1984]
- [Srinivasan et al 1986][research_srinivasan_mccroskey_1986]
- [Sriram and Jagadeesh 2014][research_sriram_jagadeesh_2014]
- [Sriram and Jagadeesh 2016][research_sriram_jagadeesh_2016]
- [Srivastava et al 2002][research_srivastava_bakhle_2002]
- [Srivastava et al 2019][research_srivastava_damodaran_2019]
- [Stacey][research_stacey]
- [Stack 1935][research_stack_1935_burble]
- [Stack 1939][research_burble_delay_1939]
- [Stack 1943][research_stackjohn_1943]
- [Stack 1944][research_burble_delay_1944]
- [Stack and Von Doenhoff 1935][research_stack_1935_16_airfoils]
- [Stack et al 1939][research_burble_1939_pressures]
- [Stack et al 1950][research_stackjohn_draleyeugenec_1950]
- [Staelens et al 2007][research_staelens_blackwelder_2007]
- [Stahara 1981][research_stahara_1981]
- [Stahara and Spreiter 1979][research_stahara_spreiter_1979]
- [Stahara and Spreiter 1980][research_stahara_spreiter_1980]
- [Stallings 1982][research_stallingsjr_1982]
- [Stallings and Hartman 1981][research_stallings_hartman_1981]
- [Stanewsky and Basler 1989][research_stanewsky_basler_1989]
- [Stanewsky and Little 1971][research_stanewsky_little_1971]
- [Stanewsky et al 1984][research_stanewskye_demurief_1984]
- [Stanford and Jacobson][research_bretkstanford_kevinejacobson]
- [Stanford and Jacobson 2023][research_stanford_jacobson_2023]
- [Stanford and Jacobson 2024][research_stanford_jacobson_2024]
- [Stanford et al][research_bretkstanford_andrewsthelen]
- [Stanford et al][research_bretkstanford_anniesauer]
- [Stanford et al][research_bretkstanford_stevenjmassey]
- [Stanford et al 2015][research_stanford_wieseman_2015]
- [Stanford et al 2022][research_stanford_sauer_2022]
- [Stanford et al 2024][research_stanford_thelen_2024]
- [Stanford et al 2025][research_stanford_thelen_2025]
- [Stanford et al 2026][research_stanford_massey_2026]
- [Stardter 1979][research_stardterh_1979]
- [Stargill 1983][research_stargill_1983]
- [Starr 1975][research_starr_1975]
- [Starr 1978][research_starr_1978]
- [Starr and Schueler 1973][research_starr_schueler_1973]
- [Starr and Varner 1976][research_starr_varner_1976]
- [Static Aeroelasticity Effect of Wing Flexibility on Lift Distribution and Divergence 2014][research_static_aeroelasticity_2014]
- [Static Longitudinal Stability Flight Test Methods 2003][research_static_longitudinal_2003]
- [Steady Transonic Flow 2015][research_steady_transonic_2015]
- [Stebbins et al 2019][research_stebbins_loth_2019]
- [Steelant 2002][research_steelant_2002]
- [Steer 2000][research_steer_2000]
- [Steer 2003][research_steer_2003]
- [Steger and Bailey 1979][research_steger_bailey_1979]
- [Steger and Bailey 1980][research_steger_bailey_1980]
- [Steger and Baldwin 1972][research_stegerjl_baldwinbs_1972]
- [Steger and Klineberg 1973][research_steger_klineberg_1973]
- [Stegmüller et al 2026][research_stegmuller_haybock_2026]
- [Steimle et al 2008][research_steimle_schroder_2008]
- [Steimle et al 2010][research_steimle_schroder_2010]
- [Steimle et al 2012][research_steimle_karhoff_2012]
- [Steinle et al 1999][research_steinle_jr_1999]
- [Steinle et al 2004][research_steinle_hawkins_2004]
- [Stengel 1969][research_stengel_1969]
- [Steppert and Epple 2017][research_steppert_epple_2017]
- [Sternberg 1954][research_sternberg_1954]
- [Stetson 1981][research_stetson_1981]
- [Stevens 1950][research_stevensjosephe_1950]
- [Stevens 1955][research_stevensjosephe_1955]
- [Stevens and Purser 1955][research_stevensjosephe_purserpaule_1955]
- [Stevenson 1981][research_stevensonjr_1981]
- [Stewart and Walters 1996][research_stewart_walters_1996]
- [Stillwell and Wilmerding 1951][research_stillwellwh_wilmerdingjv_1951]
- [Stock 1975][research_stock_1975]
- [Stock 2002][research_stock_2002]
- [Stoliker and Carter 2003][research_stolikerpatrickc_carterjohn_2003]
- [Stone 1945][research_stone_1945]
- [Strack 1964][research_strack_1964]
- [Strampp 1983][research_strampp_1983]
- [Strand 1960][research_strand_1960]
- [Streather 1972][research_streather_1972]
- [Street 1979][research_street_1979]
- [Streett 1981][research_streett_1981]
- [Streett 1982][research_streett_1982]
- [Streett 1983][research_streett_1983]
- [Stremel 1993][research_stremel_1993]
- [Strganac 1988][research_strganac_1988]
- [Strike 1982][research_strike_wt_1982]
- [Striz 1991][research_striz_1991]
- [Strome 1969][research_strome_1969]
- [Strutz 1972][research_strutzlw_1972]
- [Stubblefield et al 2025][research_stubblefield_kunz_2025]
- [Studwell and Wu 1973][research_studwell_wu_1973]
- [Study on flow noise characteristic of transonic deep buffeting over an airfoil 2023][research_study_on_2023]
- [Study on the separation in the shock wave/boundary layer interaction induced by a curved fin 2023][research_study_on_2023_b]
- [Sturek and Schiff 1980][research_sturek_schiff_1980]
- [Su and Chow 1993][research_su_chow_1993]
- [Su and Chow 1995][research_su_chow_1995]
- [Subramani et al 2025][research_subramani_m_2025]
- [Sudani et al 1993][research_sudani_sato_1993]
- [Sudani et al 2001][research_sudani_sato_2001]
- [Sudani et al 2003][research_sudani_sato_2003]
- [Sudhi et al 2021][research_sudhi_radespiel_2021]
- [Sugioka et al 2015][research_sugioka_numata_2015]
- [Sugioka et al 2018][research_sugioka_koike_2018]
- [Sugioka et al 2018][research_sugioka_nakakita_2018]
- [Sugioka et al 2021][research_sugioka_2021]
- [Sugioka et al 2023][research_sugioka_nakajima_2023]
- [Sugioka et al 2026][research_sugioka_nakajima_2026]
- [Suleman et al 2000][research_suleman_crawford_2000]
- [Sun][research_sun]
- [Sun and Hansen 1982][research_sun_hansen_1982]
- [Sun and Hu 2005][research_sun_hu_2005]
- [Sun et al 2020][research_sun_miao_2020]
- [Sun et al 2021][research_sun_wang_2021]
- [Sun et al 2025][research_sun_zhang_2025]
- [Sun et al 2026][research_sun_zhang_2026]
- [Sundaram and Wu 1983][research_sundaram_wu_1983]
- [Supercritical airfoil design][research_supercritical_airfoil]
- [Supersonic Cruise 1981][research_supersonic_cruise_1981]
- [Supersonic Flight 2014][research_supersonic_flight_2014]
- [Supersonic Flight 2025][research_supersonic_flight_2025]
- [Supersonic Maneuvers in a Vertical Plane 1981][research_supersonic_maneuvers_1981]
- [Supersonic Turn 1981][research_supersonic_turn_1981]
- [Sutherland 1893][research_sutherland_1893]
- [Suwa et al 2012][research_suwa_nose_2012]
- [Suzuki et al 2010][research_suzuki_rinoie_2010]
- [Swafford 1979][research_swafford_1979]
- [Swafford et al 1995][research_swafford_bomba_1995]
- [Swamy et al 1978][research_swamy_ahmed_1978]
- [Syed Haseeb 2026][research_m_2026]
- [Symington 1940][research_symington_1940]
- [Szema and Shankar 1984][research_szema_shankar_1984]
- [Szodruch 1980][research_szodruchj_1980]
- [Szubert et al 2015][research_szubert_grossi_2015]
- [Szulc et al 2023][research_szulc_doerffer_2023]
- [Szwaba 2005][research_szwaba_2005]
- [Szwaba and Doerffer 2017][research_szwaba_doerffer_2017]
- [Szwabowski and Baker 2023][research_szwabowski_baker_2023]
- [Sá Gontijo et al 2025][research_sagontijo_filho_2025]
- [Tacina et al 2004][research_tacina_fernandez_2004]
- [Tai 1986][research_tai_1986]
- [Tai and Kidwell 1984][research_tai_kidwelljr_1984]
- [Tai and Kidwell 1985][research_tai_kidwell_1985]
- [Tai et al 1987][research_taitszec_husongregoryg_1987]
- [Taillon 1958][research_taillonnormanv_1958]
- [Takahashi 2013][research_takahashi_2013]
- [Takahashi 2021][research_takahashi_2021]
- [Takahashi 2021][research_takahashi_2021_b]
- [Takahashi and Stone 2019][research_takahashi_stone_2019]
- [Takahashi et al 2010][research_takahashi_german_2010]
- [Takahashi et al 2019][research_takahashi_boccieri_2019]
- [Takahashi et al 2026][research_takahashi_2026_airdata]
- [Takanashi 1984][research_takanashi_1984]
- [Takanashi 1985][research_takanashi_1985]
- [Takikawa et al 2025][research_takikawa_hosono_2025]
- [Takovitskii 2003][research_takovitskii_2003]
- [Takovitskii 2003][research_takovitskii_2003_b]
- [Takovitskii 2006][research_takovitskii_2006]
- [Takovitskii 2006][research_takovitskii_2006_b]
- [Takovitskii 2016][research_takovitskii_2016]
- [Takovitskii 2018][research_takovitskii_2018]
- [Takovitskii 2020][research_takovitskii_2020]
- [Takovitskii 2022][research_takovitskii_2022]
- [Takovitskii 2023][research_takovitskii_2023]
- [Takovitskii 2024][research_takovitskii_2024]
- [Takuma et al 2026][research_takuma_hagita_2026]
- [Tam 1989][research_tam_1989]
- [Tam and Ju 2011][research_tam_ju_2011]
- [Tamada and Shibaoka 1955][research_tamada_shibaoka_1955]
- [Tamaki and Kawai 2023][research_tamaki_kawai_2023]
- [Tamayama et al 2003][research_tamayama_kheirandish_2003]
- [Tamba et al 2017][research_tamba_tuan_2017]
- [Tan et al 2024][research_tan_xu_2024]
- [Tanaka et al 2024][research_tanaka_isoda_2024]
- [Tang 1971][research_tangmh_1971]
- [Tang and Pearson 1971][research_tangmh_pearsongpe_1971]
- [Tang and Tan 2023][research_tang_tan_2023]
- [Tang et al 2000][research_tang_jiang_2000]
- [Tang et al 2003][research_tang_liu_2003]
- [Tanner 1963][research_tanner_1963]
- [Tao et al 2016][research_tao_li_2016]
- [Tao et al 2018][research_tao_zhao_2018]
- [Tao et al 2019][research_tao_sun_2019]
- [Tao et al 2023][research_tao_zheng_2023]
- [Taraborrelli 2023][research_taraborrelli_2023]
- [Taranto and Abdulrahim 2023][research_taranto_abdulrahim_2023]
- [Tatsumi and Takanashi 1985][research_tatsumi_takanashi_1985]
- [Taylor 1951][research_taylor_1951]
- [Taylor 2012][research_taylor_2012]
- [Taylor and Ratnayake 2011][research_taylor_ratnayake_2011]
- [Tempelmeyer and Osborne 1955][research_tempelmeyerkennethe_osborneroberts_1955]
- [Teperin et al 2018][research_teperin_teperina_2018]
- [Terakado et al 2016][research_terakado_nonomura_2016]
- [Terashima and Fujii 2003][research_terashima_fujii_2003]
- [Terashima and Fujii 2004][research_terashima_fujii_2004]
- [Terashima and Fujii 2007][research_terashima_fujii_2007]
- [Tetervin 1963][research_tetervin_1963]
- [Tetrault et al 2000][research_tetrault_schetz_2000]
- [Tewari 1993][research_tewari_1993]
- [Thacker and Lan 1993][research_thacker_lan_1993]
- [Thawait et al 2022][research_thawait_tandaiya_2022]
- [The effects of aft-loaded airfoils on aircraft trim drag 1989][research_the_effects_1989]
- [The Phenomenon of Buffeting 1931][research_the_phenomenon_1931]
- [Theodorsen 1979][research_theodorsen_1935]
- [Theoretical studies to refine 1970][research_ii_1970]
- [Thiede and Krogmann 1986][research_thiede_krogmann_1986]
- [Thiede and Krogmann 1989][research_thiede_krogmann_1989]
- [Thivet et al 1999][research_thivet_saintmartin_1999]
- [Thomas 1991][research_thomas_1991]
- [Thomas and Agarwal 2022][research_thomas_agarwal_2022]
- [Thomas and Agarwal 2025][research_thomas_agarwal_2025]
- [Thomas and Dowell 2011][research_thomas_dowell_2011]
- [Thomas and Dowell 2015][research_thomas_dowell_2015]
- [Thomas and Dowell 2020][research_thomas_dowell_2020]
- [Thomas and Holst 1983][research_thomas_holst_1983]
- [Thomas and Lan 1991][research_thomas_lan_1991]
- [Thomas et al 2001][research_thomas_dowell_2001]
- [Thompson 1966][research_thompson_1966]
- [Thompson and Epstein 1977][research_thompson_epstein_1977]
- [Thompson and Mathews 1947][research_freefall_sweptfwd_1947]
- [Thompson and Moseley 1956][research_thompsonrobertf_moseleywilliamcjr_1956]
- [Thompson et al 1950][research_airspeed_calibration_1950]
- [Thomson 1946][research_thomson_1946]
- [Threadgill and Bruce 2014][research_threadgill_bruce_2014]
- [Three-dimensional boundary-layer transition on a swept wing at Mach 3.5 1994][research_three_dimensional_boundary_layer_1994]
- [Tian et al 2017][research_tian_feng_2017]
- [Tian et al 2017][research_tian_gao_2017]
- [Tidbury 1945][research_tidbury_1945]
- [Tijdeman et al 1979][research_tijdeman_vannunen_1979]
- [Tijdeman et al 1979][research_tijdeman_vannunen_1979_b]
- [Tilmann 2001][research_tilmann_2001]
- [Tilmans et al 2024][research_tilmans_jackisch_2024]
- [Time-Dependent In-Flight Thrust Determination][research_time_dependent_in_flight]
- [Timme and Thormann 2016][research_timme_thormann_2016]
- [Timofeev and Aniskin 2018][research_timofeev_aniskin_2018]
- [Timothy and Lewis 2001][research_o_lewis_2001]
- [Ting et al 2014][research_ting_nguyen_2014]
- [Tinney 2014][research_tinney_2014]
- [Tischler 2018][research_tischler_2018]
- [Titchener and Babinsky 2015][research_titchener_babinsky_2015]
- [Titus et al 2013][research_titus_alexander_2013]
- [Tjatra et al 1992][research_tjatra_kapania_1992]
- [Tkalenko 1969][research_tkalenko_1969]
- [Tleulinov and Jafarzade 2019][research_tleulinov_jafarzade_2019]
- [Tobak and Lessing 1961][research_tobakmurray_lessinghenryc_1961]
- [Token 1974][research_token_1974]
- [Tokugawa and Yoshida 2006][research_tokugawa_yoshida_2006]
- [Tomek and Boyden 2000][research_tomek_boyden_2000]
- [Tomek et al 2002][research_tomek_hall_2002]
- [Tomita 1959][research_tomita_1959]
- [Toot 1989][research_toot_1989]
- [Torres and Rahai 2024][research_torres_rahai_2024]
- [Touber and Sandham 2009][research_touber_sandham_2009]
- [Tournier et al 2005][research_tournier_paduano_2005]
- [Tourrette 1993][research_tourrette_1993]
- [Tourrette 1996][research_tourrette_1996]
- [Trailing Edge Circulation Control of an Airfoil at Transonic Mach Numbers 2006][research_trailing_edge_2006]
- [Tranen 1974][research_tranen_1974]
- [Transonic Aerodynamics 1982][research_transonic_aerodynamics_1982]
- [Transonic Aerodynamics 1986][research_transonic_aerodynamics_1986]
- [Transonic Aerodynamics Problems in Asymptotic Theory 1993][research_transonic_aerodynamics_1993]
- [Transonic Aerodynamics-History and Statement of the Problem 1982][research_transonic_aerodynamics_history_1982]
- [Transonic Aircraft Configurations 2012][research_transonic_aircraft_2012]
- [Transonic Airfoil Design by the Inverse Method Using Variable-Fidelity Modelling 2011][research_transonic_airfoil_2011]
- [Transonic Airfoil Shape Design 2015][research_transonic_airfoil_2015]
- [Transonic Airfoil Theory 1986][research_transonic_airfoil_1986]
- [Transonic and supersonic flight 1992][research_transonic_and_1992]
- [Transonic and Supersonic Flows 2012][research_transonic_and_2012]
- [Transonic Computational Experience for Advanced Tactical Aircraft 1982][research_transonic_computational_1982]
- [Transonic Design Using Computational Aerodynamics 1982][research_transonic_design_1982]
- [Transonic Expansion Procedures Simple Solutions, Integral Relations 1986][research_transonic_expansion_1986]
- [Transonic Far Fields 1986][research_transonic_far_1986]
- [Transonic flight test of a laminar flow leading edge with surface excrescences 1994][research_transonic_flight_1994]
- [Transonic Maneuver/Cruise Airfoil Design Employing Active Diffusion Control 1980][research_transonic_maneuver_cruise_1980]
- [Transonic Navier-Stokes flow computations over wing-fuselage geometries 1972][research_transonic_navier_stokes_1972]
- [Transonic regular reﬂection for the unsteady transonic small disturbance equation-details of the subsonic solution Katarina Jegdic´, Barbara Lee... 2007][research_transonic_regular_2007]
- [Transonic wind tunnel wall interference corrections for three-dimensional models 1982][research_transonic_wind_1982]
- [Transonic Wing Flutter Analysis Using a Parallel Euler Solver 2005][research_transonic_wing_2005]
- [Transonic Wing Shape Design 2015][research_transonic_wing_2015]
- [Transonic, Shock, and Multidimensional Flows 1982][research_transonic_shock_1982]
- [Trefny 2020][research_trefny_2020]
- [Trenker 2003][research_trenker_2003]
- [Trenker et al 2000][research_trenker_geissler_2000]
- [Triebstein 1986][research_triebstein_1986]
- [Trilling and Covert 1955][research_trilling_covert_1955]
- [Trimmer and Clark 1963][research_trimmer_clark_1963]
- [Tripathi et al 2023][research_tripathi_mistri_2023]
- [Triplett 1980][research_triplett_1980]
- [Triplett 1982][research_triplett_1982]
- [Triplett 1983][research_triplett_1983]
- [Triplett et al 1973][research_triplett_kappus_1973]
- [Tsien 1944][research_tsienhsueshen_1944]
- [Tsien 2012][research_tsien_2012]
- [Tsien and Kuo 2012][research_tsien_kuo_2012]
- [Tsushima et al 2023][research_tsushima_saitoh_2023]
- [Tsutsumi et al 2012][research_tsutsumi_takaki_2012]
- [Tuck and Dostovalova 2000][research_tuck_dostovalova_2000]
- [Tun Nurhanis et al 2023][research_tunnurhanis_ambareenkhan_2023]
- [Tuovila and Hess 1959][research_tuovilawj_hessrobertw_1959]
- [Turbeville and Schneider 2021][research_turbeville_schneider_2021]
- [Turbojet and turbofan engines for a mach 3 supersonic transport 1964][research_turbojet_and_1964]
- [Turner 1982][research_turner_1982]
- [Turner et al 2023][research_turner_seo_2023]
- [Turner et al 2024][research_turner_seo_2024]
- [Turner et al 2024][research_turner_seo_2024_b]
- [Turner et al 2025][research_turner_seo_2025]
- [Tursi 2003][research_tursi_2003]
- [Tô et al 2019][research_to_simiriotis_2019]
- [Tấn 2020][research_tan_2020]
- [Ueda 1983][research_ueda_1983]
- [Ueda and Dowell 1984][research_uedat_dowelleh_1984]
- [Ueno and Miwa 2001][research_ueno_miwa_2001]
- [Ueno and Sudani 2008][research_ueno_sudani_2008]
- [Ueno et al 2007][research_ueno_yamamoto_2007]
- [Ulbrich 2002][research_ulbrich_2002]
- [Ulbrich 2010][research_ulbrich_2010]
- [Ulbrich and Boone 1998][research_ulbrich_boone_1998]
- [Ulbrich and Boone 2001][research_ulbrich_boone_2001]
- [Ulbrich and Boone 2003][research_ulbrichnorbert_boonealanr_2003]
- [Ulbrich and Boone 2004][research_ulbrich_boone_2004]
- [Ulbrich et al 2018][research_ulbrichn_amayam_2018]
- [Ullah et al 2021][research_ullah_lutz_2021]
- [Ullah et al 2022][research_ullah_kamoun_2022]
- [Ulug and Cigeroglu 2025][research_ulug_cigeroglu_2025]
- [Unangst 1959][research_unangstjohnr_1959]
- [Uncertainty of In-Flight Thrust Determination][research_uncertainty_of]
- [Unsteady supersonic flow past a harmonically pitching and plunging cone 1981][research_unsteady_supersonic_1981]
- [Unsteady Transonic Aerodynamics 1989][research_unsteady_transonic_1989]
- [Urie and Reaser 1979][research_urie_reaser_1979]
- [Usry and Wallace 1971][research_supercritical_body_1971]
- [Usry et al 1991][research_usryjimmyw_meyersjamesf_1991]
- [Utkina et al 2023][research_utkina_kozelkov_2023]
- [Uzun and Malik 2018][research_uzun_malik_2018]
- [Uzun and Malik 2019][research_uzun_malik_2019]
- [v. Krzywoblocki 1960][research_vkrzywoblocki_1960]
- [Vachon and Ray 2004][research_vachonmichaeljacob_rayronaldj_2004]
- [Vadillo and Agarwal 2007][research_vadillo_agarwal_2007]
- [Vadillo and Agarwal 2009][research_vadillo_agarwal_2009]
- [Vadillo et al][research_vadillo_agarwal]
- [Vadillo et al 2005][research_vadillo_agarwal_2005]
- [Vaglio-Laurin 1978][research_vagliolaurin_1978]
- [Vaisakh and Muruganandam 2018][research_vaisakh_muruganandam_2018]
- [Vaisakh et al 2019][research_vaisakh_ramprakash_2019]
- [Vaiuso et al 2025][research_vaiuso_immordino_2025]
- [Vaiuso et al 2025][research_vaiuso_immordino_2025_b]
- [Valarezo et al 1992][research_valarezowaltero_dominikchetj_1992]
- [Valarezo et al 1993][research_valarezo_dominik_1993]
- [Valarezo et al 1993][research_walterovalarezo_chetjdominik_1993]
- [van Arnhem et al 2019][research_vanarnhem_devries_2019]
- [Van Dam 1986][research_vandam_1986]
- [Van Dam and Hicks 1990][research_vandam_hicks_1990]
- [van der Vooren 2008][research_vandervooren_2008]
- [Van Der Vooren and Van Der Wees 1990][research_vandervooren_vanderwees_1990]
- [Van Der Vooren et al 1982][research_vandervooren_vanderkolk_1982]
- [van Dommelen et al 2019][research_vandommelen_dsilva_2019]
- [van Es 2002][research_vanes_2002]
- [van Es 2003][research_vanes_2003]
- [van Wezel et al 2025][research_vanwezel_pool_2025]
- [VanderWyst 2008][research_vanderwyst_2008]
- [Varner 1974][research_varner_1974]
- [Varwig 1963][research_varwig_1963]
- [Vasconcelos et al 2011][research_vasconcelos_leite_2011]
- [Vasenev and Kharitonov 1991][research_vasenev_kharitonov_1991]
- [Vasil'chenko 1981][research_vasilchenko_1981]
- [Vasil'ev 1966][research_vasilev_1966]
- [Vatsa 1987][research_vatsa_1987]
- [Vatsa and Wedan 1988][research_vatsa_wedan_1988]
- [Vaughn 1982][research_vaughnjr_1982]
- [Vavalle and Qin 2007][research_vavalle_qin_2007]
- [Vayala and Sriram 2024][research_vayala_sriram_2024]
- [Vayala et al 2025][research_vayala_vadlamani_2025]
- [Velasquez 2013][research_velasquez_2013]
- [Veldman 2005][research_veldman_2005]
- [Veletas 2026][research_veletas_2026]
- [Velichko and Lifshits 1983][research_velichko_lifshits_1983]
- [Velkova 2017][research_velkova_2017]
- [Veltin et al 2010][research_veltin_day_2010]
- [Verhaagen 1997][research_verhaagen_1997]
- [Verhoff 2005][research_verhoff_2005]
- [Verma and Chidambaranathan 2022][research_verma_chidambaranathan_2022]
- [Verma and Haidn 2009][research_verma_haidn_2009]
- [Verma and Manisankar 2018][research_verma_manisankar_2018]
- [Verma and Manisankar 2024][research_verma_manisankar_2024]
- [Verma and Rathakrishnan 2002][research_verma_rathakrishnan_2002]
- [Vernacchia et al 2022][research_vernacchia_2022]
- [Vianto et al 2021][research_vianto_tobing_2021]
- [Vicini et al 1997][research_vicini_quagliarella_1997]
- [Vidal et al 1973][research_vidal_wittliff_1973]
- [Vidal et al 1976][research_vidalrj_ericksonjcjr_1976]
- [Viegas and Rubesin 1991][research_viegas_rubesin_1991]
- [Viegas and Rubesin 1992][research_viegas_rubesin_1992]
- [Vigneswaran 2026][research_vigneswaran_2026]
- [Vijgen et al 1988][research_vijgen_dodbele_1988]
- [Vijgen et al 1990][research_vijgen_vandam_1990]
- [Vikramaditya and Viji 2023][research_vikramaditya_viji_2023]
- [Vincent and Botez 2015][research_vincent_botez_2015]
- [Vindigni 2024][research_vindigni_2024]
- [Vindigni et al 2024][research_vindigni_mantegna_2024]
- [Vindigni et al 2024][research_vindigni_mantegna_2024_b]
- [Vinh and Tzeng 1993][research_vinh_tzeng_1993]
- [Vinh and Tzeng 1994][research_vinh_tzeng_1994]
- [Vinh et al 1988][research_vinhlamson_edwardsjohnw_1988]
- [Vinodh et al 2023][research_vinodh_sridhar_2023]
- [Vinoth and Rathakrishnan 2005][research_vinoth_rathakrishnan_2005]
- [Visbal 1988][research_visbal_1988]
- [Vishwanathan][research_vishwanathan]
- [Viswanath 1988][research_viswanath_1988]
- [Viswanath and Brown 1982][research_viswanath_brown_1982]
- [Viswanath and Brown 1982][research_viswanathpr_brownjl_1982]
- [Viswanath and Brown 1983][research_viswanath_brown_1983]
- [Viswanath and Mukund 1995][research_viswanath_mukund_1995]
- [Viswanath and Patil 1997][research_viswanath_patil_1997]
- [Viswanath and Rajendra 1990][research_viswanath_rajendra_1990]
- [Viswanath et al 1978][research_viswanath_sankaran_1978]
- [Viswanath et al 1983][research_viswanath_sankaran_1983]
- [Vittal-Shenoy et al 2023][research_vittalshenoy_gojon_2023]
- [Vlasyk and Korshunova 2025][research_vlasyk_korshunova_2025]
- [Voet et al 2023][research_voet_speth_2023]
- [Vogler 1956][research_voglerraymondd_1956]
- [Volkova 2021][research_volkova_2021]
- [Volkova et al 2020][research_volkova_ivanov_2020]
- [Volpe 1986][research_volpe_1986]
- [Volpe and Grossman 1978][research_volpe_grossman_1978]
- [Volpe and Jameson 1990][research_volpe_jameson_1990]
- [Von Doenhoff et al 1947][research_vondoenhoffalberte_stiverslouiss_1947]
- [von Knoblauch et al 2014][research_vonknoblauch_moreno_2014]
- [Voracek 2007][research_voracekdavid_2007]
- [Vos and Farokhi 2015][research_vos_farokhi_2015]
- [Vos and Farokhi 2015][research_vos_farokhi_2015_b]
- [Vos and Farokhi 2015][research_vos_farokhi_2015_c]
- [Vos and Farokhi 2015][research_vos_farokhi_2015_d]
- [Vos and Vaessen 2013][research_vos_vaessen_2013]
- [Vozhdaev and Teperin 2020][research_vozhdaev_teperin_2020]
- [Vukasinovic et al 2013][research_vukasinovic_gissen_2013]
- [Vyas et al 2016][research_vyasmanana_waindimmbu_2016]
- [Vyas et al 2018][research_vyasmanana_yoderdennisa_2018]
- [Vyas et al 2019][research_vyasmanana_yoderdennisa_2019]
- [Véras et al 2022][research_veras_souzademouralima_2022]
- [Völkl et al 2026][research_volkl_weiner_2026]
- [Wada 1924][research_wada_1924]
- [Waggoner 1980][research_waggoner_1980]
- [Waggoner 1982][research_waggoner_1982]
- [Wagner 1982][research_wagner_1982]
- [Wagner 1985][research_wagner_1985]
- [Wahls et al 2001][research_wahls_owens_2001]
- [Wai and Yoshihara 1982][research_wai_yoshihara_1982]
- [Wai and Yoshihara 1984][research_wai_yoshihara_1984]
- [Wainwright 1962][research_wainwright_1962]
- [Waisanen and Perangelo 1972][research_waisanen_perangelo_1972]
- [Waite et al 2019][research_waite_stanford_2019]
- [Walchli and Langan 1999][research_walchli_langan_1999]
- [Waldmann et al 2023][research_waldmann_ehrle_2023]
- [Walitt and Liu 1976][research_walittl_liucy_1976]
- [Walitt et al 1977][research_walitt_king_1977]
- [Walkden 1958][research_walkden_1958]
- [Walker 1973][research_walker_1973]
- [Walker 2005][research_walkerericlee_2005]
- [Wallace 1952][research_wallace_1952]
- [Wallace 1953][research_wallace_1953]
- [Wallace and Monk 1966][research_wallace_monk_1966]
- [Wallace et al][research_ryanwallace_jamesreynolds]
- [Wallskog 1954][research_wallskogharveya_1954]
- [Wallskog 1954][research_wallskogharveya_1954_b]
- [Wang 1998][research_wang_1998]
- [Wang 2019][research_wang_2019]
- [Wang 2025][research_wang_2025]
- [Wang and Andreopoulos 2003][research_wang_andreopoulos_2003]
- [Wang and Andreopoulos 2009][research_wang_andreopoulos_2009]
- [Wang and Luo][research_wang_luo]
- [Wang and Rusak 2001][research_wang_rusak_2001]
- [Wang and Zha 2019][research_wang_zha_2019]
- [Wang and Zha 2020][research_wang_zha_2020]
- [Wang and Zhou 2020][research_wang_zhou_2020]
- [Wang et al 1994][research_wang_herbert_1994]
- [Wang et al 2002][research_wang_damodaran_2002]
- [Wang et al 2011][research_wang_chen_2011]
- [Wang et al 2013][research_wang_hu_2013]
- [Wang et al 2021][research_wang_wu_2021]
- [Wang et al 2022][research_wang_li_2022]
- [Wang et al 2022][research_wang_qu_2022]
- [Wang et al 2023][research_wang_wang_2023]
- [Wang et al 2024][research_wang_gan_2024]
- [Wang et al 2024][research_wang_guo_2024]
- [Wang et al 2024][research_wang_liu_2024]
- [Wang et al 2025][research_wang_wang_2025]
- [Wang et al 2026][research_wang_kang_2026]
- [Wang et al 2026][research_wang_song_2026]
- [Wang et al 2026][research_wang_song_2026_b]
- [Ward 1968][research_ward_1968]
- [Ward and Miley 1983][research_ward_miley_1983]
- [Warning and McQuilling 2022][research_warning_mcquilling_2022]
- [Warning et al 2024][research_warning_lambert_2024]
- [Wasserman 1952][research_wasserman_1952]
- [Wat and Sarohia 1981][research_wat_sarohia_1981]
- [Watanabe et al 2005][research_watanabe_maekawa_2005]
- [Watts et al 1988][research_wattsmichaele_crossjeffreyl_1988]
- [Weatherill and Ehlers 1983][research_weatherill_ehlers_1983]
- [Weatherill and Ehlers 1989][research_weatherillwarrenh_ehlersfedward_1989]
- [Weatherill and Zartarian 1958][research_weatherill_zartarian_1958]
- [Weber et al 1999][research_weber_jones_1999]
- [Weber et al 2001][research_weber_jones_2001]
- [Weed et al 1983][research_weed_carlson_1983]
- [Weed et al 1984][research_weed_carlson_1984]
- [Weeks 1973][research_weeks_1973]
- [Wegener 1977][research_wegener_1977]
- [Wei et al 2023][research_wei_zheng_2023]
- [Wei et al 2024][research_wei_zheng_2024]
- [Wei et al 2026][research_wei_liu_2026]
- [Weiand et al 2017][research_weiand_michelis_2017]
- [Weidinger 1927][research_weidingerhanns_1927]
- [Weinacht 2014][research_weinacht_2014]
- [Weiner and Semaan 2022][research_weiner_semaan_2022]
- [Weiner and Semaan 2023][research_weiner_semaan_2023]
- [Weingarten 2003][research_weingarten_2003]
- [Weingarten and Chalk 1982][research_weingarten_chalk_1982]
- [Weiss 2008][research_weiss_2008]
- [Weiss et al 2022][research_weiss_staudacher_2022]
- [Weisshaar 1972][research_weisshaar_1972]
- [Weisshaar 1979][research_weisshaar_1979]
- [Weisshaar and Zeiler 1982][research_weisshaar_zeiler_1982]
- [Wells 1953][research_wells_1953]
- [Wells 2017][research_wells_2017]
- [Wenzhong and Rongwei 2008][research_wenzhong_rongwei_2008]
- [Wermeser et al 2024][research_wermeser_takarics_2024]
- [Werner et al 2022][research_werner_schutte_2022]
- [Werner et al 2024][research_werner_henne_2024]
- [Wetmore 1947][research_wetmorejw_1947]
- [Wetzel and Pfyl 1954][research_wetzelbentone_pfylfranka_1954]
- [Weyburne 2009][research_weyburne_2009]
- [Whitbeck et al 1982][research_whitbeck_smith_1982]
- [Whitcomb 1944][research_whitcombrichardt_1944]
- [Whitcomb 1953][research_whitcombrichardt_1953]
- [Whitcomb 1956][research_richardtwhitcomb_1956]
- [Whitcomb 1956][research_whitcomb_1952]
- [Whitcomb 1974][research_whitcombrt_1974]
- [Whitcomb 1976][research_whitcombrt_1976]
- [Whitcomb 1983][research_whitcombrt_1983]
- [Whitcomb and Clark 1965][research_whitcomb_clark_1965]
- [Whitcomb and Sevier 1960][research_whitcombrichardt_sevierjohnrjr_1960]
- [White 1952][research_whitemauriced_1952]
- [White 1963][research_white_1963]
- [White 1969][research_white_1969]
- [White 1977][research_white_1977]
- [White 2004][research_white_2004]
- [Whitefield et al 1981][research_whitefield_griffith_1981]
- [Whitfield and Griffith 1963][research_whitfield_griffith_1963]
- [Whitfield and Jameson 1983][research_whitfield_jameson_1983]
- [Whitfield and Thompson 1989][research_whitfield_thompson_1989]
- [Whitford 1991][research_whitford_1991]
- [Whitlow and Seidel 1985][research_whitlow_seidel_1985]
- [Whitmer et al 2012][research_whitmer_kelkar_2012]
- [Whittley and Garland 1961][research_whittley_garland_1961]
- [Wick et al 2017][research_wick_hooker_2017]
- [Wieseman et al 2005][research_wieseman_silva_2005]
- [Wiggen et al 2018][research_wiggen_henne_2018]
- [Wight 1964][research_wight_1964]
- [Wigley 1988][research_wigleydavida_1988]
- [Wilby 1967][research_wilby_1967]
- [Wilks 2006][research_wilks_2006]
- [Willard and Kranzler 1996][research_willard_kranzler_1996]
- [Williams 1956][research_williams_1956]
- [Williams 1965][research_williams_1965]
- [Williams 1979][research_williams_1979]
- [Williams 1980][research_williams_1980]
- [Williams 1991][research_williamswalterc_1991]
- [Williams and Hunt 1980][research_williams_hunt_1980]
- [Williams and Kesling 1980][research_williams_kesling_1980]
- [Williams et al 1948][research_xs1_handling_1948]
- [Williams et al 1985][research_williams_bland_1985]
- [Williams-Hayes 2005][research_williamshayes_2005]
- [Wilmerding et al 1950][research_wilmerdingjv_stillwellwh_1950]
- [Wilmoth 1977][research_wilmothrg_1977]
- [Wilson 1967][research_wilsonrj_1967]
- [Wilson and Chou 1985][research_wilson_chou_1985]
- [Wilson et al 1975][research_wilson_chandra_1975]
- [Wilson et al 1987][research_wilson_kalkhoran_1987]
- [Winarto and Stalker 1984][research_winarto_stalker_1984]
- [Winchenbach et al 1982][research_winchenbach_chelekis_1982]
- [Wind Tunnel 2022][research_wind_tunnel_2022]
- [Wind Tunnel/Flight Test Correlation Program on the B-1 nacelle afterbody/nozzle at transonic conditions 1978][research_wind_tunnel_flight_1978]
- [Wing Loads 1996][research_wing_loads_1996]
- [Wing tunnel model for simulating an infinite swept wing 1998][research_wing_tunnel_1998]
- [Winston 1969][research_winstonmm_1969]
- [Wiriadidjaja et al 2012][research_wiriadidjaja_rafie_2012]
- [Wise and Sterbentz 1957][research_wisegeorgea_sterbentzwilliamh_1957]
- [Wislicenus and Daidzic 2022][research_wislicenus_daidzic_2022]
- [Wissink et al 1995][research_wissink_lyrintzis_1995]
- [Witteveen and Bijl 2009][research_witteveen_bijl_2009]
- [Woan and Chakravarthy 1988][research_woan_chakravarthy_1988]
- [Woeste 1992][research_woeste_1992]
- [Wolf and Wolf 1997][research_wolf_wolf_1997]
- [Wolf et al 1988][research_wolf_henry_1988]
- [Wolf et al 2014][research_wolf_azevedo_2014]
- [Wollblad et al 2006][research_wollblad_davidson_2006]
- [Wolles 1997][research_wolles_1997]
- [Wolowicz and Rediess 1957][research_wolowiczchesterh_rediesshermana_1957]
- [Wong 1974][research_wong_1974]
- [Wong 1977][research_wong_1977]
- [Wood 1944][research_woodclotaire_1944]
- [Wood 1988][research_woodrichardm_1988]
- [Wood and Conlon 1983][research_wood_conlon_1983]
- [Wood and Roberts 1989][research_wood_roberts_1989]
- [Wooden et al 2007][research_wooden_smith_2007]
- [Woodford and Hansen 1985][research_woodford_hansen_1985]
- [Woodson and Dejarnette 1986][research_woodsonsh_dejarnettefr_1986]
- [Woodward 1973][research_woodwardfa_1973]
- [Woolard 1980][research_woolard_1980]
- [Wootton 1967][research_wootton_1967]
- [Wright 1936][research_wright_1936]
- [Wright 1945][research_wright_1945]
- [Wright 1948][research_wrightjohnb_1948]
- [Wright 1948][research_wrightjohnb_1948_b]
- [Wright 1948][research_wrightjohnb_1948_c]
- [Wright and Loving 1953][research_wrightjohnd_lovingdonaldl_1953]
- [Wright and Zoby 1977][research_wright_zoby_1977]
- [Wu 1975][research_wu_1975]
- [Wu and Collins 1984][research_wujm_collinsfg_1984]
- [Wu and Moulden 1976][research_wu_moulden_1976]
- [Wu et al 1977][research_wu_chen_1977]
- [Wu et al 1982][research_wu_collins_1982]
- [Wu et al 1983][research_wu_collins_1983]
- [Wu et al 1999][research_wu_fuller_1999]
- [Wu et al 2025][research_wu_yuan_2025]
- [Xia et al 1993][research_xia_zhu_1993]
- [Xiao and Tsai 2004][research_xiao_tsai_2004_b]
- [Xiao et al 2004][research_xiao_tsai_2004]
- [Xiao et al 2006][research_xiao_tsai_2006]
- [Xie et al 2019][research_xie_zhao_2019]
- [Xie et al 2020][research_xie_liu_2020]
- [Xin et al 2013][research_xin_dawei_2013]
- [Xing and Damodaran 2003][research_xing_damodaran_2003]
- [Xiong and Liu 2013][research_xiong_liu_2013]
- [Xiong and Nguyen 2022][research_xiong_nguyen_2022_c]
- [Xiong and Nguyen 2023][research_xiong_nguyen_2023_c]
- [Xiong and Nguyen 2024][research_xiong_nguyen_2024]
- [Xiong and Nguyen 2024][research_xiong_nguyen_2024_b]
- [Xiong et al][research_juntaoxiong_nhannguyen]
- [Xiong et al][research_juntaoxiong_nhannguyen_b]
- [Xiong et al 2011][research_xiong_shang_2011]
- [Xiong et al 2019][research_xiong_fugate_2019]
- [Xiong et al 2020][research_xiong_fugate_2020]
- [Xiong et al 2021][research_xiong_bartels_2021]
- [Xiong et al 2021][research_xiong_bartels_2021_b]
- [Xiong et al 2021][research_xiong_nguyen_2021]
- [Xiong et al 2022][research_xiong_nguyen_2022]
- [Xiong et al 2022][research_xiong_nguyen_2022_b]
- [Xiong et al 2023][research_xiong_nguyen_2023]
- [Xiong et al 2023][research_xiong_nguyen_2023_b]
- [Xiong et al 2023][research_xiong_nguyen_2023_d]
- [Xu and Dowell 2026][research_xu_dowell_2026]
- [Xu and Qiu 2011][research_xu_qiu_2011]
- [Xu and Yin 2008][research_xu_yin_2008]
- [Xu et al 2019][research_xu_saleh_2019]
- [Xu et al 2020][research_xu_liu_2020]
- [Xue et al 2020][research_xue_ren_2020]
- [Xue et al 2024][research_xue_feng_2024]
- [Xue et al 2025][research_xue_feng_2025]
- [Yagiz and Kandil 2009][research_yagiz_kandil_2009]
- [Yamaguchi et al 1993][research_yamaguchi_yorozu_1993]
- [Yamaguchi et al 1994][research_yamaguchi_yorozu_1994]
- [Yamamoto et al 2012][research_yamamoto_tanaka_2012]
- [Yamasaki and Lele 2024][research_yamasaki_lele_2024]
- [Yan et al 2016][research_yan_ragab_2016]
- [Yan et al 2017][research_yan_ragab_2017]
- [Yan et al 2026][research_yan_dai_2026]
- [Yang 1972][research_yang_1972]
- [Yang and Greber 1993][research_yangweili_greberisaac_1993]
- [Yang and Wan 1978][research_yang_wan_1978]
- [Yang et al 1980][research_yang_guruswamy_1980]
- [Yang et al 1980][research_yang_guruswamy_1980_b]
- [Yang et al 1980][research_yang_striz_1980]
- [Yang et al 1981][research_yang_guruswamy_1981]
- [Yang et al 1981][research_yang_striz_1981]
- [Yang et al 2015][research_yang_yan_2015]
- [Yang et al 2016][research_yang_he_2016]
- [Yang et al 2016][research_yang_yao_2016]
- [Yang et al 2017][research_yang_huang_2017]
- [Yang et al 2019][research_yang_huang_2019]
- [Yang et al 2024][research_yang_li_2024]
- [Yang et al 2024][research_yang_li_2024_b]
- [Yang et al 2025][research_yang_wu_2025]
- [Yang et al 2026][research_yang_li_2026]
- [Yaros 1978][research_yaros_1978]
- [Yates 1963][research_yates_1963]
- [Yates et al 1982][research_yates_wynne_1982]
- [Yates et al 1982][research_yatesjr_wynne_1982]
- [Yates et al 1983][research_yates_wynne_1983]
- [Yechout and Schweikhard 1984][research_yechout_schweikhard_1984]
- [Yee et al 1997][research_yee_lee_1997]
- [Yee et al 1998][research_yee_lee_1998]
- [Yefremov et al 2005][research_yefremov_kraiko_2005]
- [Yeom and Chang 2012][research_yeom_chang_2012]
- [Yetter et al 1982][research_yetter_evelyn_1982]
- [Yigit and Millidere 2021][research_yigit_millidere_2021]
- [Yinsheng Luo et al 2011][research_yinshengluo_shaobangxing_2011]
- [Yip et al 1995][research_yip_vijgen_1995]
- [Yongping et al 2026][research_yongping_zengjun_2026]
- [Yoo][research_yoo]
- [Yoon and Chung 1996][research_yoon_chung_1996]
- [Yoshida and Tokuyama 1992][research_yoshida_tokuyama_1992]
- [Yoshida et al 2021][research_yoshida_bragg_2021]
- [Yoshikawa 1982][research_yoshikawa_1982]
- [Yoshioka et al][research_yoshioka_kohama]
- [Yoshioka et al 2009][research_yoshioka_kikuchi_2009]
- [You 2026][research_you_2026]
- [You et al 2013][research_you_bromby_2013]
- [Young][research_young]
- [Young 1961][research_youngls_1961]
- [Young et al 1988][research_young_oran_1988]
- [Young et al 1990][research_youngjr_popernackjr_1990]
- [Young et al 1992][research_youngjr_hergert_1992]
- [Yu 1979][research_yu_1979]
- [Yu 1980][research_yu_1980]
- [Yu 1981][research_yu_1981]
- [Yu and Campbell 1992][research_yu_campbell_1992]
- [Yu et al 1983][research_yu_chen_1983]
- [Yu et al 2014][research_yu_lv_2014]
- [Yu et al 2025][research_yu_zhou_2025]
- [Yu et al 2026][research_yu_bose_2026]
- [Yu Xing et al 2015][research_yuxing_gangwang_2015]
- [Yuan et al 2019][research_yuan_wan_2019]
- [Yue 2026][research_yue_2026]
- [Yuhara et al 2018][research_yuhara_kubota_2018]
- [Yurkovich 1996][research_yurkovich_1996]
- [Zahir and Gao 2013][research_zahir_gao_2013]
- [Zahn and Breitsamter 2020][research_zahn_breitsamter_2020]
- [Zahn and Breitsamter 2022][research_zahn_breitsamter_2022]
- [Zahn et al 2025][research_zahn_zieher_2025]
- [Zalovcik 1944][research_zalovcikjohna_1944]
- [Zalovcik 1945][research_zalovcikjohna_1945]
- [Zamuraev and Kalinina 2018][research_zamuraev_kalinina_2018]
- [Zanin 1985][research_zanin_1985]
- [Zartarian 1956][research_zartarian_1956]
- [Zartarian and Hsu 1955][research_zartarian_hsu_1955]
- [Zater and Bahi 2024][research_zater_bahi_2024]
- [Zauner and Sandham 2020][research_zauner_sandham_2020]
- [Zauner et al 2018][research_zauner_detullio_2018]
- [Zauner et al 2019][research_zauner_detullio_2019]
- [Zauner et al 2023][research_zauner_moise_2023]
- [Zebiri et al 2019][research_zebiri_piquet_2019]
- [Zeigler and Drew 1985][research_zeigler_drew_1985]
- [Zeleke et al 2023][research_zeleke_asfaw_2023]
- [Zeng et al 2012][research_zeng_chen_2012]
- [Zhang 2013][research_zhang_2013]
- [Zhang and Du 2025][research_zhang_du_2025]
- [Zhang and Edwards 1990][research_zhang_edwards_1990]
- [Zhang and Qu 2015][research_zhang_qu_2015]
- [Zhang and Ye 2010][research_zhang_ye_2010]
- [Zhang and Ye 2015][research_zhang_ye_2015]
- [Zhang and Zhang 2013][research_zhang_zhang_2013]
- [Zhang and Zhang 2020][research_zhang_zhang_2020]
- [Zhang et al 1988][research_zhang_yang_1988]
- [Zhang et al 1990][research_zhang_yu_1990]
- [Zhang et al 2008][research_zhang_xu_2008]
- [Zhang et al 2013][research_zhang_yu_2013]
- [Zhang et al 2016][research_zhang_ding_2016]
- [Zhang et al 2017][research_zhang_gao_2017]
- [Zhang et al 2017][research_zhang_shan_2017]
- [Zhang et al 2019][research_zhang_dai_2019]
- [Zhang et al 2020][research_zhang_li_2020]
- [Zhang et al 2020][research_zhang_ma_2020]
- [Zhang et al 2021][research_zhang_guo_2021]
- [Zhang et al 2021][research_zhang_yang_2021]
- [Zhang et al 2021][research_zhang_zou_2021]
- [Zhang et al 2022][research_zhang_hirahara_2022]
- [Zhang et al 2023][research_zhang_su_2023]
- [Zhang et al 2024][research_zhang_tian_2024]
- [Zhang et al 2024][research_zhang_zhao_2024]
- [Zhang et al 2025][research_zhang_zuo_2025]
- [Zhang et al 2026][research_zhang_deng_2026]
- [Zhang et al 2026][research_zhang_dou_2026]
- [Zhang et al 2026][research_zhang_kou_2026]
- [Zhang et al 2026][research_zhang_kou_2026_b]
- [Zhao 1988][research_zhao_1988]
- [Zhao 2016][research_zhao_2016]
- [Zhao 2023][research_zhao_2023]
- [Zhao and Hu 2009][research_zhao_hu_2009]
- [Zhao and Wang 2025][research_zhao_wang_2025]
- [Zhao et al 2012][research_zhao_zhu_2012]
- [Zhao et al 2013][research_zhao_ren_2013]
- [Zhao et al 2017][research_zhao_gao_2017]
- [Zhao et al 2020][research_zhao_dai_2020]
- [Zhao et al 2020][research_zhao_he_2020]
- [Zhao et al 2022][research_zhao_wu_2022]
- [Zhao et al 2023][research_zhao_jia_2023]
- [Zhao et al 2024][research_zhao_li_2024]
- [Zhao et al 2024][research_zhao_liu_2024]
- [Zhao et al 2025][research_zhao_li_2025]
- [Zhao et al 2026][research_zhao_yang_2026]
- [Zheng and Liu 2011][research_zheng_liu_2011]
- [Zheng et al 2012][research_zheng_feng_2012]
- [Zheng-hong 1992][research_zhenghong_1992]
- [Zhigulev and Zhilin 1959][research_zhigulev_zhilin_1959]
- [Zhong et al 2025][research_zhong_xia_2025]
- [Zhou 1994][research_zhou_1994]
- [Zhou et al 2016][research_zhou_li_2016]
- [Zhou et al 2017][research_zhou_chen_2017]
- [Zhou et al 2017][research_zhou_hou_2017]
- [Zhou et al 2018][research_zhou_feng_2018]
- [Zhou et al 2025][research_zhou_cao_2025]
- [Zhou et al 2026][research_zhou_ji_2026]
- [Zhu and Qin 2021][research_zhu_qin_2021]
- [Zhu et al 1992][research_zhu_xia_1992]
- [Zhu et al 1994][research_zhu_xia_1994]
- [Zhu et al 2019][research_zhu_li_2019]
- [Zhu et al 2020][research_zhu_wang_2020]
- [Zhu et al 2025][research_zhu_yang_2025]
- [Zhu et al 2026][research_zhu_yang_2026]
- [Zi-qiang and Xue-Song 1992][research_ziqiang_xuesong_1992]
- [Zigangareyeva and Kiselev 1997][research_zigangareyeva_kiselev_1997]
- [Zimmermann et al 2018][research_zimmermann_mayer_2018]
- [Zimper and Rein 2014][research_zimper_rein_2014]
- [Zingg et al 2006][research_zingg_diosady_2006]
- [Zink et al 2001][research_zink_mavris_2001]
- [Zinovyev et al 2012][research_zinovyev_lebiga_2012]
- [Zolovcik 1950][research_zolovcikjohna_1950]
- [Zong et al 2023][research_zong_wu_2023]
- [Zoppini et al 2022][research_zoppini_ragni_2022]
- [Zores 1995][research_zores_1995]
- [Zuccolo et al 2020][research_zuccolo_christie_2020]
- [Zuosheng 1986][research_zuosheng_1986]
- [Zwaan 1984][research_zwaan_1984]
- [Ángel Muñoz and Colera 2020][research_angelmunoz_colera_2020]
- [Ümütlü et al 2022][research_umutlu_kiral_2022]
- [Čanić and Keyfitz 1996][research_canic_keyfitz_1996]
- [Čanić et al 2000][research_canic_keyfitz_2000]
- [Čanić et al 2001][research_canic_kim_2001]

### Related Post

- [A106 Two-Stage Flying Delta Wing Vehicles][related_post_a106_two_stage_delta_wing]
- [A118 Propulsion and Power Sizing for Small Fixed-Wing UAVs][related_post_a118_propulsion_sizing]
- [A122 Stability, Control, and Configuration for Fixed-Wing UAVs][related_post_a122_stability_configuration]
- [A123 Dynamic Stability and Control for Fixed-Wing UAVs][related_post_a123_dynamic_stability]
- [A127 Structures and the Flight Envelope for Fixed-Wing UAVs][related_post_a127_structures_flight_envelope]
- [A217 Rocket Propellant Chemistry, A Design-Tradeoff Space][related_post_a217_rocket_propellant_chemistry]
- [A237 Framing and the Co-Development Mechanism][related_post_a237_aerospace_framing]
- [A241 Aerospace Simulation and Real-Time Systems][related_post_a241_aerospace_simulation]
- [A297 X-Planes, Framing and the Research Aircraft Model][related_post_a297_xplanes_framing]
- [A90 Introduction to Space Studies][related_post_a90_intro_space_studies]
- [A96 History of Rocketplanes][related_post_a96_history_rocketplanes]

[book_anderson_1997_history_aerodynamics]: https://openlibrary.org/works/OL1993322W
[book_anderson_2001_fundamentals]: https://openlibrary.org/works/OL3232211W
[book_anderson_2002_modern_compressible]: https://openlibrary.org/works/OL1993329W
[book_anderson_2012_aircraft_performance]: https://openlibrary.org/works/OL1993317W
[book_anderson_2012_introduction_flight]: https://openlibrary.org/works/OL1993331W
[book_ashley_landahl_1965]: https://openlibrary.org/works/OL42971075W
[book_baals_corliss_1981]: https://openlibrary.org/works/OL31504107W
[book_barlow_rae_pope_1999]: https://openlibrary.org/works/OL1921571W
[book_bertin_cummings_2013]: https://openlibrary.org/works/OL21437883W
[book_bevington_robinson_2002]: https://openlibrary.org/works/OL44935135W
[book_bilstein_1989_orders]: https://openlibrary.org/works/OL18823771W
[book_bisplinghoff_ashley_halfman_1955]: https://openlibrary.org/works/OL3240762W
[book_box_hunter_hunter_2005]: https://openlibrary.org/works/OL28985605W
[book_brown_1988_wings_on_my_sleeve]: https://openlibrary.org/works/OL8273515W
[book_bruhn_1973]: https://openlibrary.org/works/OL8796483W
[book_chambers_2008_radical_wings]: https://openlibrary.org/works/OL5834577W
[book_constant_1980]: https://openlibrary.org/works/OL6325070W
[book_cover_thomas_2006]: https://openlibrary.org/works/OL21500808W
[book_etkin_reid_1996]: https://openlibrary.org/works/OL19844466W
[book_ferguson_1992]: https://openlibrary.org/works/OL4119982W
[book_fung_1955]: https://openlibrary.org/works/OL2655267W
[book_gelman_et_al_2013]: https://openlibrary.org/works/OL12630389W
[book_gorn_1992_universal_man]: https://openlibrary.org/works/OL4400575W
[book_gorn_2001_expanding_envelope]: https://openlibrary.org/works/OL4400572W
[book_gunston_1992_faster_than_sound]: https://openlibrary.org/works/OL774338W
[book_hallion_1972_supersonic_flight]: https://openlibrary.org/works/OL2688456W
[book_hallion_1981_on_the_frontier]: https://openlibrary.org/works/OL2688458W
[book_hallion_1981_test_pilots]: https://openlibrary.org/works/OL2688457W
[book_hansen_1987_engineer_in_charge]: https://openlibrary.org/works/OL37594565W
[book_hansen_2004_bird_on_the_wing]: https://openlibrary.org/works/OL3492401W
[book_hill_peterson_1991]: https://openlibrary.org/works/OL8229940W
[book_hurt_1965]: https://openlibrary.org/works/OL4297319W
[book_huzel_huang_1992]: https://openlibrary.org/works/OL27313820W
[book_jenkins_landis_miller_2003]: https://openlibrary.org/works/OL20394726W
[book_kimberlin_2003]: https://openlibrary.org/works/OL8874080W
[book_kuchemann_1978]: https://openlibrary.org/works/OL22640504W
[book_kuethe_chow_1998]: https://openlibrary.org/works/OL2661785W
[book_liepmann_roshko_1957]: https://openlibrary.org/works/OL13214987W
[book_mcruer_ashkenas_graham_1973]: https://openlibrary.org/works/OL13424815W
[book_megson_2016]: https://openlibrary.org/works/OL4809615W
[book_miller_2001_x_planes]: https://openlibrary.org/works/OL7006680W
[book_nelson_1998]: https://openlibrary.org/works/OL11288560W
[book_nicolai_carichner_2010]: https://openlibrary.org/works/OL15909375W
[book_niu_1988_airframe]: https://openlibrary.org/works/OL19561185W
[book_peebles_2014_probing_the_sky]: https://openlibrary.org/works/OL23215820W
[book_perrow_1984]: https://openlibrary.org/works/OL4468929W
[book_petroski_1985]: https://openlibrary.org/works/OL112186W
[book_pisano_et_al_2006]: https://openlibrary.org/works/OL4301215W
[book_pope_goin_1965]: https://openlibrary.org/works/OL3791131W
[book_raymer_2018]: https://openlibrary.org/works/OL17855977W
[book_roskam_1985]: https://openlibrary.org/works/OL6612019W
[book_rotundo_1994_into_the_unknown]: https://openlibrary.org/works/OL3920129W
[book_schlichting_gersten_2017]: https://openlibrary.org/works/OL20524688W
[book_shapiro_1953]: https://openlibrary.org/works/OL5908243W
[book_stengel_2004]: https://openlibrary.org/works/OL3486012W
[book_stinton_2001]: https://openlibrary.org/works/OL1911152W
[book_sutton_biblarz_2016]: https://openlibrary.org/works/OL21470530W
[book_taylor_1997_error_analysis]: https://openlibrary.org/works/OL3232610W
[book_torenbeek_1982]: https://openlibrary.org/works/OL9096469W
[book_vaughan_1996]: https://openlibrary.org/works/OL2962391W
[book_vincenti_1990]: https://openlibrary.org/works/OL4805206W
[book_von_karman_edson_1967]: https://openlibrary.org/works/OL7117470W
[book_ward_strganac_niewoehner_2006]: https://openlibrary.org/works/OL19810630W
[book_white_2006_viscous]: https://openlibrary.org/works/OL1911849W
[book_whitford_1987]: https://openlibrary.org/works/OL5054670W
[book_winchester_2005_x_planes]: https://openlibrary.org/works/OL8492617W
[book_wolfe_1979_right_stuff]: https://openlibrary.org/works/OL1925474W
[book_wood_1975_project_cancelled]: https://openlibrary.org/works/OL4333017W
[book_yeager_janos_1985]: https://openlibrary.org/works/OL4628050W
[ref_accelerometer]: https://en.wikipedia.org/wiki/Accelerometer
[ref_aerodynamic_center]: https://en.wikipedia.org/wiki/Aerodynamic_center
[ref_aeroelasticity]: https://en.wikipedia.org/wiki/Aeroelasticity
[ref_airspeed_indicator]: https://en.wikipedia.org/wiki/Airspeed
[ref_armstrong_frc]: https://en.wikipedia.org/wiki/Armstrong_Flight_Research_Center
[ref_aspect_ratio]: https://en.wikipedia.org/wiki/Aspect_ratio_(aeronautics)
[ref_b29]: https://en.wikipedia.org/wiki/Boeing_B-29_Superfortress
[ref_bell_aircraft]: https://en.wikipedia.org/wiki/Bell_Aircraft
[ref_bell_x1]: https://en.wikipedia.org/wiki/Bell_X-1
[ref_bell_x1a]: https://en.wikipedia.org/wiki/Bell_X-1#Variants
[ref_bell_x2]: https://en.wikipedia.org/wiki/Bell_X-2
[ref_bell_x5]: https://en.wikipedia.org/wiki/Bell_X-5
[ref_boundary_layer]: https://en.wikipedia.org/wiki/Boundary_layer
[ref_buffeting]: https://en.wikipedia.org/wiki/Aeroelasticity#Buffeting
[ref_critical_mach]: https://en.wikipedia.org/wiki/Critical_Mach_number
[ref_de_havilland_swallow]: https://en.wikipedia.org/wiki/De_Havilland_DH_108
[ref_douglas_x3]: https://en.wikipedia.org/wiki/Douglas_X-3_Stiletto
[ref_drag_coefficient]: https://en.wikipedia.org/wiki/Drag_coefficient
[ref_drag_divergence]: https://en.wikipedia.org/wiki/Drag_divergence_Mach_number
[ref_drag_polar]: https://en.wikipedia.org/wiki/Drag_polar
[ref_duralumin]: https://en.wikipedia.org/wiki/Duralumin
[ref_dynamic_pressure]: https://en.wikipedia.org/wiki/Dynamic_pressure
[ref_edwards_afb]: https://en.wikipedia.org/wiki/Edwards_Air_Force_Base
[ref_elevator_aircraft]: https://en.wikipedia.org/wiki/Elevator_(aeronautics)
[ref_ethanol_fuel]: https://en.wikipedia.org/wiki/Ethanol
[ref_expansion_fan]: https://en.wikipedia.org/wiki/Prandtl%E2%80%93Meyer_expansion_fan
[ref_experimental_aircraft]: https://en.wikipedia.org/wiki/Experimental_aircraft
[ref_f100]: https://en.wikipedia.org/wiki/North_American_F-100_Super_Sabre
[ref_f104]: https://en.wikipedia.org/wiki/Lockheed_F-104_Starfighter
[ref_f86]: https://en.wikipedia.org/wiki/North_American_F-86_Sabre
[ref_factor_of_safety]: https://en.wikipedia.org/wiki/Factor_of_safety
[ref_flight_envelope]: https://en.wikipedia.org/wiki/Flight_envelope
[ref_flight_test]: https://en.wikipedia.org/wiki/Flight_test
[ref_flow_separation]: https://en.wikipedia.org/wiki/Flow_separation
[ref_hinge_moment]: https://en.wikipedia.org/wiki/Control_surface
[ref_hoop_stress]: https://en.wikipedia.org/wiki/Cylinder_stress
[ref_isa]: https://en.wikipedia.org/wiki/International_Standard_Atmosphere
[ref_lift_coefficient]: https://en.wikipedia.org/wiki/Lift_coefficient
[ref_liquid_oxygen]: https://en.wikipedia.org/wiki/Liquid_oxygen
[ref_list_of_x1_flights]: https://en.wikipedia.org/wiki/List_of_X-1_flights
[ref_list_of_x_planes]: https://en.wikipedia.org/wiki/List_of_X-planes
[ref_load_factor]: https://en.wikipedia.org/wiki/Load_factor_(aeronautics)
[ref_longitudinal_static_stability]: https://en.wikipedia.org/wiki/Longitudinal_static_stability
[ref_mach_number]: https://en.wikipedia.org/wiki/Mach_number
[ref_mach_tuck]: https://en.wikipedia.org/wiki/Mach_tuck
[ref_measurement_uncertainty]: https://en.wikipedia.org/wiki/Measurement_uncertainty
[ref_miles_m52]: https://en.wikipedia.org/wiki/Miles_M.52
[ref_muroc]: https://en.wikipedia.org/wiki/Edwards_Air_Force_Base#History
[ref_na_x15]: https://en.wikipedia.org/wiki/North_American_X-15
[ref_naca]: https://en.wikipedia.org/wiki/National_Advisory_Committee_for_Aeronautics
[ref_naca_airfoil]: https://en.wikipedia.org/wiki/NACA_airfoil
[ref_naca_rm_l51e08]: https://ntrs.nasa.gov/citations/19930086696
[ref_nasa]: https://en.wikipedia.org/wiki/NASA
[ref_nasa_armstrong]: https://www.nasa.gov/centers-and-facilities/armstrong/
[ref_nasa_history]: https://www.nasa.gov/history/
[ref_nasm_x1]: https://airandspace.si.edu/collection-objects/bell-x-1
[ref_normal_shock]: https://en.wikipedia.org/wiki/Shock_wave#Normal_shock
[ref_northrop_x4]: https://en.wikipedia.org/wiki/Northrop_X-4_Bantam
[ref_ntrs]: https://ntrs.nasa.gov/
[ref_oblique_shock]: https://en.wikipedia.org/wiki/Oblique_shock
[ref_p38]: https://en.wikipedia.org/wiki/Lockheed_P-38_Lightning
[ref_pitot_tube]: https://en.wikipedia.org/wiki/Pitot_tube
[ref_position_error]: https://en.wikipedia.org/wiki/Pitot-static_system
[ref_prandtl_glauert]: https://en.wikipedia.org/wiki/Prandtl%E2%80%93Glauert_transformation
[ref_prandtl_glauert_singularity]: https://en.wikipedia.org/wiki/Prandtl%E2%80%93Glauert_singularity
[ref_pressure_fed]: https://en.wikipedia.org/wiki/Pressure-fed_engine
[ref_propagation_of_uncertainty]: https://en.wikipedia.org/wiki/Propagation_of_uncertainty
[ref_rayleigh_pitot]: https://en.wikipedia.org/wiki/Pitot_tube#Supersonic_flow
[ref_reaction_motors]: https://en.wikipedia.org/wiki/Reaction_Motors
[ref_reynolds_number]: https://en.wikipedia.org/wiki/Reynolds_number
[ref_rocket_engine]: https://en.wikipedia.org/wiki/Rocket_engine
[ref_sears_haack]: https://en.wikipedia.org/wiki/Sears%E2%80%93Haack_body
[ref_shock_wave]: https://en.wikipedia.org/wiki/Shock_wave
[ref_smithsonian_nasm]: https://en.wikipedia.org/wiki/National_Air_and_Space_Museum
[ref_sound_barrier]: https://en.wikipedia.org/wiki/Sound_barrier
[ref_specific_impulse]: https://en.wikipedia.org/wiki/Specific_impulse
[ref_speed_of_sound]: https://en.wikipedia.org/wiki/Speed_of_sound
[ref_stabilator]: https://en.wikipedia.org/wiki/Stabilator
[ref_strain_gauge]: https://en.wikipedia.org/wiki/Strain_gauge
[ref_supersonic_speed]: https://en.wikipedia.org/wiki/Supersonic_speed
[ref_swept_wing]: https://en.wikipedia.org/wiki/Swept_wing
[ref_tailplane]: https://en.wikipedia.org/wiki/Tailplane
[ref_telemetry]: https://en.wikipedia.org/wiki/Telemetry
[ref_transonic]: https://en.wikipedia.org/wiki/Transonic
[ref_trim_tab]: https://en.wikipedia.org/wiki/Trim_tab
[ref_tsiolkovsky]: https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation
[ref_us_standard_atmosphere]: https://en.wikipedia.org/wiki/U.S._Standard_Atmosphere
[ref_wave_drag]: https://en.wikipedia.org/wiki/Wave_drag
[ref_whitcomb_area_rule]: https://en.wikipedia.org/wiki/Area_rule
[ref_wind_tunnel]: https://en.wikipedia.org/wiki/Wind_tunnel
[ref_wing_loading]: https://en.wikipedia.org/wiki/Wing_loading
[ref_xlr11]: https://en.wikipedia.org/wiki/Reaction_Motors_XLR11
[ref_yeager]: https://en.wikipedia.org/wiki/Chuck_Yeager
[related_post_a106_two_stage_delta_wing]: {% post_url 2026-03-12-two_stage_flying_delta_wing_vehicles_for_civil_and_national_security_applications %}
[related_post_a118_propulsion_sizing]: {% post_url 2026-06-02-propulsion_and_power_sizing_for_fixed_wing_uavs %}
[related_post_a122_stability_configuration]: {% post_url 2026-06-05-stability_control_and_configuration_for_fixed_wing_uavs %}
[related_post_a123_dynamic_stability]: {% post_url 2026-06-06-dynamic_stability_and_control_for_fixed_wing_uavs %}
[related_post_a127_structures_flight_envelope]: {% post_url 2026-06-10-structures_and_the_flight_envelope_for_fixed_wing_uavs %}
[related_post_a217_rocket_propellant_chemistry]: {% post_url 2026-02-01-rocket_propellant_chemistry_a_design_tradeoff_space %}
[related_post_a237_aerospace_framing]: {% post_url 2026-07-13-framing_and_the_co_development_mechanism %}
[related_post_a241_aerospace_simulation]: {% post_url 2026-07-17-aerospace_simulation_and_real_time_systems %}
[related_post_a297_xplanes_framing]: {% post_url 2025-10-06-x_planes_framing %}
[related_post_a90_intro_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[related_post_a96_history_rocketplanes]: {% post_url 2026-02-27-history_of_rocketplanes %}
[research_a_7_transonic_1982]: https://doi.org/10.2514/5.9781600865558.0431.0450
[research_a_comparison_2022]: https://doi.org/10.14529/jsfi220401
[research_a_computational_1980]: https://doi.org/10.2514/6.1980-1389
[research_a_computational_1994]: https://doi.org/10.2514/6.1994-2276
[research_a_new_2006]: https://doi.org/10.5139/jksas.2006.34.5.012
[research_a_predictive_1991]: https://doi.org/10.1109/37.103359
[research_a_self_adaptive_1989]: https://doi.org/10.2514/6.1989-837
[research_a_series_1982]: https://doi.org/10.2514/5.9781600865558.0489.0509
[research_abada_kbab_2024]: https://doi.org/10.13111/2066-8201.2024.16.2.1
[research_abdelfattah_link_1992]: https://doi.org/10.21236/ada251676
[research_abed_alhamadani_2024]: https://doi.org/10.18280/mmep.111029
[research_abele_ruger_1973]: https://doi.org/10.21236/ad0766892
[research_abele_sanlorenzo_1975]: https://doi.org/10.21236/ada013139
[research_abichandani_rosenberg_1952]: https://doi.org/10.2514/8.2362
[research_abrahamdoman_merrett_2014]: https://doi.org/10.2514/6.2014-0194
[research_abumostafaas_reedtd_1984]: https://ntrs.nasa.gov/citations/19860020299
[research_ackeret_1925]: https://ntrs.nasa.gov/citations/19930087085
[research_adamczyk_1973]: https://doi.org/10.2514/6.1973-683
[research_adamov_chasovnikov_2025]: https://doi.org/10.1134/s0869864325010081
[research_adams]: https://doi.org/10.22215/etd/2017-11821
[research_adams_johnc_1968]: https://doi.org/10.21236/ad0667523
[research_adams_rubin_1958]: https://doi.org/10.21236/ad0200634
[research_adams_thompson_1983]: https://doi.org/10.4271/831438
[research_adams_thompson_1983_b]: https://doi.org/10.4271/831439
[research_adamson_1976]: https://doi.org/10.1007/978-3-642-81005-3_27
[research_adamson_jr_1980]: https://doi.org/10.21236/ada088662
[research_adamsonjr_feo_1975]: https://doi.org/10.1137/0129013
[research_adamsricharde_silsbynormans_1947]: https://ntrs.nasa.gov/citations/20030063953
[research_adaptive_transonic_2016]: https://doi.org/10.1002/9781118823491.ch11
[research_adcock_kilgore_1975]: https://doi.org/10.2514/6.1975-143
[research_adhikary_narayanaswamy_2026]: https://doi.org/10.2139/ssrn.6161266
[research_adityasghate_gaetankkenway]: https://ntrs.nasa.gov/citations/20205011379
[research_adiwidodo_wijaya_2022]: https://doi.org/10.51278/ajse.v1i1.396
[research_advanced_ducted]: https://doi.org/10.4271/air5450
[research_advanced_technology_1978]: https://ntrs.nasa.gov/citations/19790011818
[research_advancedfuelresearchinceasthartfordct_1957]: https://doi.org/10.21236/ada390317
[research_aerodynamic_and_1960]: https://ntrs.nasa.gov/citations/19980228350
[research_aerodynamic_and_2014]: https://doi.org/10.15242/iie.e1214053
[research_aerodynamic_forces_1995]: https://doi.org/10.2514/5.9781600868535.0081.0124
[research_aeroelasticity_problems_2010]: https://doi.org/10.2514/5.9781600867552.0335.0373
[research_aerospike_sr71_1998]: https://ntrs.nasa.gov/citations/19980217098
[research_afkhami_alighanbari_2007]: https://doi.org/10.1049/iet-cta:20060455
[research_afsar_sescu_2019]: https://doi.org/10.2514/6.2019-2731
[research_agarwal_deese_1983]: https://doi.org/10.2514/6.1983-1935
[research_agarwal_deese_1983_b]: https://doi.org/10.2514/6.1983-501
[research_agarwal_deese_1988]: https://doi.org/10.2514/6.1988-3800
[research_agarwal_miley_1992]: https://doi.org/10.2514/6.1992-4089
[research_ageev_pavlenko_2016]: https://doi.org/10.1108/aeat-02-2015-0052
[research_agopiankg_1974]: https://ntrs.nasa.gov/citations/19740022508
[research_agostini_larcheveque_2012]: https://doi.org/10.1051/eucass/201203157
[research_agostini_larcheveque_2013]: https://doi.org/10.1615/tsfp8.530
[research_agrawal_kinard_1991]: https://doi.org/10.2514/6.1991-3205
[research_agrawal_lowrie_1990]: https://doi.org/10.2514/6.1990-3015
[research_agrell_elmeland_1984]: https://doi.org/10.2514/6.1984-2158
[research_agrell_elmeland_1985]: https://doi.org/10.2514/3.45185
[research_agrell_pettersson_1987]: https://doi.org/10.2514/6.1987-2610
[research_aguwa_chen_2026]: https://doi.org/10.3233/atde260524
[research_ahlefeldt_2017]: https://doi.org/10.2514/1.j055262
[research_ahmed_selvarajan_1991]: https://doi.org/10.2514/6.1991-1711
[research_ahmed_wentz_1989]: https://doi.org/10.2514/3.45870
[research_ahn_drela_1998]: https://doi.org/10.2514/6.1998-928
[research_ahn_kim_2001]: https://doi.org/10.2514/2.2841
[research_ahn_kim_2001_b]: https://doi.org/10.2514/2.2780
[research_ahn_yee_1999]: https://doi.org/10.2514/6.1999-403
[research_ai_bai_2023]: https://doi.org/10.3390/aerospace10050434
[research_ai_bai_2023_b]: https://doi.org/10.1177/14613484231207195
[research_ai_bai_2024]: https://doi.org/10.1007/978-981-97-4010-9_96
[research_ai_bai_2026]: https://doi.org/10.1016/j.ast.2025.111339
[research_aidala_1985]: https://doi.org/10.21236/ada171075
[research_aircraft_and_2021]: https://doi.org/10.1002/9781118949818.ch3
[research_aircraft_performance_2026]: https://doi.org/10.1017/9781009399913.006
[research_aircraft_stability_1998]: https://doi.org/10.2514/5.9781600862052.0333.0354
[research_aircraft_stability_2021]: https://doi.org/10.47176/jafm.14.03.31974
[research_airfoil_integrals_2001]: https://doi.org/10.1017/cbo9780511810329.018
[research_airfoil_static_pressure_1990]: https://doi.org/10.2514/6.1990-3286
[research_airforceflighttestcenteredwardsafbca_1974]: https://doi.org/10.21236/ada011561
[research_airforceflighttestcenteredwardsafbca_1974_b]: https://doi.org/10.21236/ada011562
[research_airforceflighttestcenteredwardsafbca_2002]: https://doi.org/10.21236/ada402888
[research_airforcetestpilotschooledwardsafbca_1962]: https://doi.org/10.21236/ada320203
[research_airforcetestpilotschooledwardsafbca_1962_b]: https://doi.org/10.21236/ada320207
[research_airforcetestpilotschooledwardsafbca_1962_c]: https://doi.org/10.21236/ada320208
[research_airforcetestpilotschooledwardsafbca_1967]: https://doi.org/10.21236/ada320209
[research_airforcetestpilotschooledwardsafbca_1967_b]: https://doi.org/10.21236/ada320224
[research_airforcetestpilotschooledwardsafbca_1979]: https://doi.org/10.21236/ada320202
[research_airforcetestpilotschooledwardsafbca_1988]: https://doi.org/10.21236/ada319984
[research_airforcetestpilotschooledwardsafbca_1990]: https://doi.org/10.21236/ada320062
[research_airforcetestpilotschooledwardsafbca_1990_b]: https://doi.org/10.21236/ada319977
[research_airforcetestpilotschooledwardsafbca_1991]: https://doi.org/10.21236/ada320218
[research_airforcetestpilotschooledwardsafbca_1991_b]: https://doi.org/10.21236/ada319981
[research_airforcetestpilotschooledwardsafbca_1992]: https://doi.org/10.21236/ada319982
[research_airforcetestpilotschooledwardsafbca_1992_b]: https://doi.org/10.21236/ada320221
[research_airplane_and_1990]: https://doi.org/10.1017/cbo9780511622892.012
[research_airplane_trim_2012]: https://doi.org/10.1017/cbo9781139161893.010
[research_airplane_trim_2022]: https://doi.org/10.2514/5.9781624106408.0223.0240
[research_airspeed_calibration_1950]: https://ntrs.nasa.gov/citations/19930090286
[research_airspeed_calibration_2021]: https://doi.org/10.1002/9781118949818.ch8
[research_airspeed_indicator]: https://doi.org/10.4271/as391a
[research_airspeed_indicator_b]: https://doi.org/10.4271/as391c
[research_airspeed_vs_2003]: https://doi.org/10.2514/5.9781600861840.0169.0175
[research_akmese_comert_2009]: https://doi.org/10.2514/6.2009-6302
[research_alam_pant_2019]: https://doi.org/10.2514/1.c034887
[research_albone_hall_1976]: https://doi.org/10.1007/978-3-642-81005-3_56
[research_albrecht_olson_2022]: https://doi.org/10.2514/6.2022-1055
[research_alden_schindel_1952]: https://doi.org/10.2514/8.2140
[research_alder_2014]: https://doi.org/10.2514/6.2014-2448
[research_alder_2015]: https://doi.org/10.2514/1.j054013
[research_alexander_griffin_1973]: https://doi.org/10.21236/ad0763725
[research_alexander_griffin_1975]: https://doi.org/10.21236/ada017286
[research_alexandermichaelg_andersscottg_2005]: https://ntrs.nasa.gov/citations/20050165090
[research_alguacil_becherucci_2023]: https://doi.org/10.2514/6.2023-3635
[research_alhussan_2007]: https://doi.org/10.1007/978-3-540-75995-9_83
[research_allan_owens_2006]: https://doi.org/10.2514/6.2006-845
[research_allen_1954]: https://doi.org/10.4271/540162
[research_allen_lizotte_2005]: https://doi.org/10.2514/6.2005-6313
[research_allisondenniso_mineckraymonde_1993]: https://ntrs.nasa.gov/citations/19940020113
[research_allisondenniso_mineckraymonde_1996]: https://ntrs.nasa.gov/citations/19960039925
[research_allmovable_comparison_1945]: https://ntrs.nasa.gov/citations/19930092948
[research_allmovable_flutter_1957]: https://ntrs.nasa.gov/citations/19630010646
[research_allmovable_flutter_1958]: https://ntrs.nasa.gov/citations/19660010452
[research_allmovable_geared_1946]: https://ntrs.nasa.gov/citations/19930081790
[research_allmovable_prelim_1945]: https://ntrs.nasa.gov/citations/19930092870
[research_almohammadi_2022]: https://doi.org/10.1016/j.aej.2021.07.008
[research_alsaadijassima_1993]: https://ntrs.nasa.gov/citations/19940011321
[research_alsaadijassima_dejarnettefredr_1992]: https://ntrs.nasa.gov/citations/19920039529
[research_alshabu_hermes_2007]: https://doi.org/10.2514/6.2007-4000
[research_alternative_methods_1989]: https://doi.org/10.2514/5.9781600865947.0349.0376
[research_altman_1965]: https://doi.org/10.2514/6.1965-220
[research_altstatt_1977]: https://doi.org/10.21236/ada040023
[research_alvi_2005]: https://doi.org/10.21236/ada458295
[research_ameduri_concilio_2005]: https://doi.org/10.1117/12.600965
[research_amendola_dimino_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00018-6
[research_amiet_1974]: https://doi.org/10.2514/3.49212
[research_amin_shah_2016]: https://doi.org/10.1109/icet.2016.7813234
[research_amouyal_weihs_2015]: https://doi.org/10.5176/2382-5758_2.1.12
[research_amouyal_weihs_2016]: https://doi.org/10.7603/s40957-015-0002-1
[research_amprikidis_cooper_2003]: https://doi.org/10.2514/6.2003-1413
[research_an_evaluation_1974]: https://doi.org/10.2514/6.1974-1020
[research_an_experimental_1978]: https://doi.org/10.2514/6.1978-1200
[research_an_experimental_2006]: https://doi.org/10.5139/jksas.2006.34.2.011
[research_an_williams_2025]: https://doi.org/10.2514/6.2025-1083
[research_an_williams_2026]: https://doi.org/10.2514/1.j065357
[research_anatolievich_andreevich_2020]: https://doi.org/10.25046/aj050613
[research_anders_anderson_1999]: https://doi.org/10.2514/2.2557
[research_anders_watson_1985]: https://doi.org/10.2514/6.1985-520
[research_andersen_kolonay_1997]: https://doi.org/10.2514/6.1997-1385
[research_andersen_kolonay_1998]: https://doi.org/10.2514/6.1998-529
[research_andersen_kolonay_1998_b]: https://doi.org/10.2514/2.2378
[research_andersjb_andersonwk_1998]: https://ntrs.nasa.gov/citations/20040090510
[research_anderson_1984]: https://doi.org/10.2514/6.1984-2093
[research_anderson_anderson_1970]: https://doi.org/10.21236/ad0876366
[research_anderson_averett_1972]: https://doi.org/10.2514/6.1972-764
[research_anderson_vincent_1983]: https://doi.org/10.2514/6.1983-2746
[research_anderson_vincent_1985]: https://doi.org/10.1109/cdc.1985.268918
[research_andersonbh_bensontj_1983]: https://ntrs.nasa.gov/citations/19830013928
[research_andersonsethb_brayrichards_1951]: https://ntrs.nasa.gov/citations/19930086840
[research_andre_castelain_2013]: https://doi.org/10.2514/6.2013-2079
[research_andrew_stenton_1967]: https://doi.org/10.2514/6.1967-16
[research_ang_1987]: https://doi.org/10.2514/6.1987-2357
[research_angelmunoz_colera_2020]: https://doi.org/10.1016/j.jsv.2020.115342
[research_angleellwyne_lundstromreginaldr_1948]: https://ntrs.nasa.gov/citations/19930085541
[research_anhichem_timme_2025]: https://doi.org/10.2514/1.j064617
[research_ankenbruckhermano_1954]: https://ntrs.nasa.gov/citations/19930087952
[research_ankenbruckhermano_dahlentheodoree_1953]: https://ntrs.nasa.gov/citations/19930087460
[research_ankenbruckhermano_wolowiczchesterh_1954]: https://ntrs.nasa.gov/citations/19930088491
[research_ansell_bragg_2010]: https://doi.org/10.2514/6.2010-4225
[research_ansell_bragg_2011]: https://doi.org/10.2514/1.c031435
[research_ansell_bragg_2011_b]: https://doi.org/10.4271/2011-38-0066
[research_ansell_kerho_2013]: https://doi.org/10.2514/6.2013-2654
[research_antoniogiovannischoneich_thomasjwhalen]: https://ntrs.nasa.gov/citations/20205002897
[research_anyiwojc_bushnelldm_1982]: https://ntrs.nasa.gov/citations/19820050734
[research_anyoji_numata_2015]: https://doi.org/10.2514/1.j053468
[research_appendix_c_1997]: https://doi.org/10.2514/5.9781600861529.0325.0326
[research_appendix_f_1999]: https://doi.org/10.2514/5.9781624103704.0459.0464
[research_appichjr_1978]: https://doi.org/10.2514/6.1978-1348
[research_application_of_1982]: https://doi.org/10.2514/5.9781600865558.0405.0430
[research_application_of_1982_b]: https://doi.org/10.2514/5.9781600865558.0621.0636
[research_applied_computational_1982]: https://doi.org/10.2514/5.9781600865558.0511.0543
[research_ar_2013]: https://doi.org/10.4172/2168-9792.1000112
[research_archambaud_louis_2004]: https://doi.org/10.2514/6.2004-2245
[research_ardema_williams_1972]: https://doi.org/10.2514/6.1972-794
[research_arguchintseva_pilyugin_2008]: https://doi.org/10.1134/s0015462808040157
[research_arif_singh_2023]: https://doi.org/10.2514/6.2023-1567
[research_arizono_kheirandish_2008]: https://doi.org/10.2514/6.2008-1897
[research_armenta_takahashi_2021]: https://doi.org/10.2514/6.2021-2441
[research_armstrong_1977]: https://doi.org/10.21236/adb029224
[research_armstrong_holt_1952]: https://doi.org/10.2514/8.2435
[research_armstrong_lindberg_2006]: https://doi.org/10.21236/ada463491
[research_armywarcollcarlislebarrackspa_1952]: https://doi.org/10.21236/ada390507
[research_arnaiz_1975]: https://doi.org/10.2514/6.1975-964
[research_arnaizhh_1977]: https://ntrs.nasa.gov/citations/19770017156
[research_arnaizhh_petersonjbjr_1980]: https://ntrs.nasa.gov/citations/19800009724
[research_arnault_dandois_2016]: https://doi.org/10.1016/j.compfluid.2016.06.006
[research_arney_gd_1963]: https://doi.org/10.21236/ad0295759
[research_arney_georged_1964]: https://doi.org/10.21236/ad0453130
[research_arnold_1942]: https://doi.org/10.2514/8.10949
[research_arnold_thiele_1993]: https://doi.org/10.2514/6.1993-3462
[research_arnold_thiele_1994]: https://doi.org/10.2514/3.12275
[research_arthur_1984]: https://doi.org/10.2514/6.1984-428
[research_arunajatesan_cattafesta_2008]: https://doi.org/10.2514/6.2008-3861
[research_asada_kawai_2024]: https://doi.org/10.2514/6.2024-0494
[research_asadi_farsadi_2020]: https://doi.org/10.1016/j.ast.2020.105853
[research_asai_2022]: https://doi.org/10.52843/cassyni.pd9g9h
[research_asai_kanda_1996]: https://doi.org/10.2514/6.1996-2185
[research_asai_kanda_1997]: https://doi.org/10.2514/2.2132
[research_asher_martuccelli_1957]: https://doi.org/10.21236/ad0142088
[research_ashley_1979]: https://doi.org/10.2514/6.1979-765
[research_ashley_1980]: https://doi.org/10.2514/3.57891
[research_asim_masud_2022]: https://doi.org/10.2514/6.2022-0690
[research_askari_soltani_2019]: https://doi.org/10.2514/1.c035328
[research_asymptotic_methods_1991]: https://doi.org/10.2514/6.1991-1712
[research_atifatulismahismail_2021]: https://doi.org/10.37934/cfdl.13.9.5771
[research_atkinson_2016]: https://doi.org/10.2514/6.2016-1185
[research_atta_nayfeh_1978]: https://doi.org/10.2514/6.1978-1206
[research_attaeh_vadyakj_1983]: https://ntrs.nasa.gov/citations/19840005090
[research_atthar_2026]: https://doi.org/10.2139/ssrn.7300738
[research_aulchenko_2006]: https://doi.org/10.1007/s10891-006-0190-2
[research_aulchenko_latypov_1985]: https://doi.org/10.1007/bf01091039
[research_aulchenko_zamuraev_2010]: https://doi.org/10.1134/s1063785010060179
[research_aulchenko_zamuraev_2012]: https://doi.org/10.1007/s10891-012-0785-8
[research_aulchenko_zamuraev_2014]: https://doi.org/10.1007/s10891-014-1054-9
[research_aulehla_1992]: https://doi.org/10.2514/3.46200
[research_aulschenko_zamuraev_2006]: https://doi.org/10.1134/s1063785006010020
[research_austin_1966]: https://doi.org/10.21236/ad0479000
[research_austin_siclari_1997]: https://doi.org/10.1117/12.274664
[research_austin_vannostrand_1995]: https://doi.org/10.1117/12.209348
[research_avkhadiev_elizarov_1992]: https://doi.org/10.1007/bf01051194
[research_avkhadiev_elizarov_1995]: https://doi.org/10.1017/s0956792500001947
[research_avkhadiev_elizarov_2001]: https://doi.org/10.1017/s1446181100012232
[research_axelson_1975]: https://doi.org/10.2514/6.1975-996
[research_axelson_1977]: https://doi.org/10.2514/3.58819
[research_axelsonja_1947]: https://ntrs.nasa.gov/citations/19790079934
[research_ayok_2026]: https://doi.org/10.32920/32288709.v1
[research_azarova_2022]: https://doi.org/10.3390/en15228627
[research_azzazy_modarress_1987]: https://doi.org/10.2514/6.1987-1430
[research_azzazy_modarress_1989]: https://doi.org/10.2514/3.10127
[research_babinsky_2007]: https://doi.org/10.21236/ada476419
[research_babinsky_2014]: https://doi.org/10.21236/ada602774
[research_babinsky_delery_2011]: https://doi.org/10.1017/cbo9780511842757.003
[research_babinsky_ogawa_2006]: https://doi.org/10.2514/6.2006-3698
[research_babister_1980]: https://doi.org/10.1016/b978-0-08-024768-7.50010-7
[research_bacci_saddington_2022]: https://doi.org/10.2514/6.2022-3008
[research_bacci_saddington_2026]: https://doi.org/10.2514/6.2026-4279
[research_bacci_saddington_2026_b]: https://doi.org/10.1016/j.dt.2025.11.032
[research_bachaio_1983]: https://doi.org/10.2514/6.1983-1793
[research_back_1970]: https://doi.org/10.2514/3.5758
[research_baer_1966]: https://doi.org/10.21236/ad0477832
[research_baerriedhart_1981]: https://doi.org/10.2514/6.1981-2467
[research_bahi_ross_1983]: https://doi.org/10.2514/6.1983-137
[research_bai_cao_2022]: https://doi.org/10.1016/j.tsep.2022.101297
[research_bai_li_2015]: https://doi.org/10.1115/imece2015-53062
[research_bai_qian_2017]: https://doi.org/10.1177/1461348417733930
[research_bailey_ballhaus]: https://doi.org/10.1007/bfb0112670
[research_bailey_knoedler_1996]: https://doi.org/10.21236/ada303524
[research_bailey_miller_1981]: https://doi.org/10.2514/3.7764
[research_bailey_starr_1976]: https://doi.org/10.2514/3.7262
[research_baileyfr_ballhauswf_1973]: https://ntrs.nasa.gov/citations/19740034201
[research_baker_forsey_1981]: https://doi.org/10.2514/6.1981-1015
[research_baker_forsey_1983]: https://doi.org/10.2514/3.8028
[research_baker_schuman_1961]: https://doi.org/10.21236/ad0610391
[research_bakerthomasf_1953]: https://ntrs.nasa.gov/citations/19930087804
[research_bakerthomasf_1953_b]: https://ntrs.nasa.gov/citations/19930087898
[research_bakerthomasf_1954]: https://ntrs.nasa.gov/citations/19930088116
[research_bakerthomasf_johnsonwallacee_1955]: https://ntrs.nasa.gov/citations/19930088625
[research_balakrishna_niranjana_1987]: https://doi.org/10.2514/6.1987-2626
[research_balakrishnan_2004]: https://doi.org/10.2514/1.5101
[research_balakrishnas_1989]: https://ntrs.nasa.gov/citations/19900006641
[research_balakumar_2018]: https://doi.org/10.2514/6.2018-4036
[research_balasubramanian_anandhanarayanan_2017]: https://doi.org/10.1007/s12046-017-0610-3
[research_ball_1978]: https://doi.org/10.2514/6.1978-1500
[research_ball_1979]: https://doi.org/10.2514/3.58559
[research_balla_rhode_2014]: https://doi.org/10.2514/1.j052608
[research_balleur_girodrouxlavigne_2002]: https://doi.org/10.1007/978-3-540-45856-2_9
[research_balsa_goldstein_1990]: https://doi.org/10.1017/s0022112090000544
[research_balusamy_a_2024]: https://doi.org/10.1108/aeat-04-2023-0088
[research_bamber_1961]: https://doi.org/10.21236/ad0267450
[research_banavara_dimitrov_2014]: https://doi.org/10.1007/978-3-319-03158-3_37
[research_barakos_drikakis_1999]: https://doi.org/10.1615/tsfp1.1590
[research_barbut_braza_2010]: https://doi.org/10.1007/978-3-642-14168-3_16
[research_bardina_lombard_1988]: https://doi.org/10.2514/6.1988-2585
[research_bare_reubush_1987]: https://doi.org/10.2514/6.1987-1749
[research_barnard_1969]: https://doi.org/10.2514/6.1969-793
[research_barnes_og_1965]: https://doi.org/10.21236/ad0654783
[research_barnes_visbal_2017]: https://doi.org/10.2514/6.2017-3320
[research_barnes_visbal_2018]: https://doi.org/10.2514/6.2018-0823
[research_barnes_visbal_2020]: https://doi.org/10.2514/6.2020-3043
[research_barnes_visbal_2021]: https://doi.org/10.2514/6.2021-1650
[research_barnes_visbal_2023]: https://doi.org/10.2514/1.j062380
[research_barnhart_greber_1988]: https://doi.org/10.2514/6.1988-308
[research_barnwell_edwards_1986]: https://doi.org/10.2514/6.1986-755
[research_barnwellrw_1975]: https://ntrs.nasa.gov/citations/19750016609
[research_barnwellrw_1976]: https://ntrs.nasa.gov/citations/19760014063
[research_barnwellrw_1976_b]: https://ntrs.nasa.gov/citations/19760055663
[research_barnwellrw_sewallwg_1979]: https://ntrs.nasa.gov/citations/19790011887
[research_baron_1954]: https://doi.org/10.21236/ad0055902
[research_barrett_gonzalez_2021]: https://doi.org/10.3390/act10100265
[research_barrowsdannya_2006]: https://ntrs.nasa.gov/citations/20070003495
[research_bartasevicius_hornung_2023]: https://doi.org/10.2514/6.2023-0372
[research_barter_dolling_1996]: https://doi.org/10.2514/6.1996-2043
[research_barterjohnw_dollingdavids_1995]: https://ntrs.nasa.gov/citations/19960009428
[research_barterjohnw_dollingdavids_1995_b]: https://ntrs.nasa.gov/citations/19960009429
[research_bartlettdw_1975]: https://ntrs.nasa.gov/citations/19830002803
[research_bartlettdw_harriscd_1973]: https://ntrs.nasa.gov/citations/19830002762
[research_bartlettdw_harriscd_1974]: https://ntrs.nasa.gov/citations/19830002751
[research_bartlettdw_sangiorgiog_1975]: https://ntrs.nasa.gov/citations/19830002815
[research_barufaldi_morales_2019]: https://doi.org/10.2514/6.2019-0830
[research_bashkirov_ogorodnikov_2018]: https://doi.org/10.1007/s42401-018-0007-y
[research_basic_equations_1989]: https://doi.org/10.2514/5.9781600865947.0057.0073
[research_baskaran_muruganandam_2022]: https://doi.org/10.2514/6.2022-1371
[research_basu_niyogi_1987]: https://doi.org/10.1007/bf01174653
[research_batill_nelson_1982]: https://doi.org/10.2514/6.1982-188
[research_batina_1986]: https://doi.org/10.2514/3.45398
[research_batina_1986_b]: https://doi.org/10.2514/3.45324
[research_batina_1986_c]: https://doi.org/10.2514/3.45302
[research_batina_1987]: https://doi.org/10.2514/6.1987-109
[research_batina_1988]: https://doi.org/10.2514/6.1988-2278
[research_batina_1988_b]: https://doi.org/10.2514/3.45629
[research_batina_1988_c]: https://doi.org/10.2514/6.1988-105
[research_batina_1989]: https://doi.org/10.2514/3.45799
[research_batina_1989_b]: https://doi.org/10.2514/3.45734
[research_batina_seidel_1989]: https://doi.org/10.2514/3.45718
[research_batina_yang_1985]: https://doi.org/10.2514/3.45137
[research_bauer_garabedian_1977]: https://doi.org/10.1007/978-3-642-48852-8_3
[research_bauer_garabedian_2026]: https://doi.org/10.1201/9781003760528-2
[research_bauer_grund_2016]: https://doi.org/10.20944/preprints201607.0061.v1
[research_bauer_hernandez_1988]: https://doi.org/10.2514/6.1988-2567
[research_bauerf_garabedianp_1973]: https://ntrs.nasa.gov/citations/19740041850
[research_bauerf_garabedianp_1983]: https://ntrs.nasa.gov/citations/19850008521
[research_bawa_michalski_2025]: https://doi.org/10.2514/6.2025-104785
[research_baxter_1947]: https://doi.org/10.1108/eb031538
[research_bazgir_takovitskii_2018]: https://doi.org/10.1051/matecconf/201822105001
[research_bazyma_rashkovan_2003]: https://doi.org/10.2514/6.2003-5302
[research_bean_lee_1994]: https://doi.org/10.2514/6.1994-1800
[research_bean_lee_1995]: https://doi.org/10.2514/3.46885
[research_bean_wood_1996]: https://doi.org/10.2514/3.47012
[research_beeler_1956]: https://ntrs.nasa.gov/citations/19930084521
[research_begnini_bones_2018]: https://doi.org/10.2514/6.2018-3004
[research_bekemeyer_timme_2017]: https://doi.org/10.2514/6.2017-4361
[research_belesiotiskataras_timme_2020]: https://doi.org/10.2514/6.2020-1985
[research_belesiotiskataras_timme_2021]: https://doi.org/10.2514/6.2021-0611
[research_belisle_neale_2010]: https://doi.org/10.2514/6.2010-4381
[research_belisle_roberts_2012]: https://doi.org/10.2514/6.2012-2667
[research_bell_1963]: https://doi.org/10.21236/ad0418711
[research_belligoli_dwight_2019]: https://doi.org/10.2514/6.2019-2976
[research_belligoli_dwight_2019_b]: https://doi.org/10.2514/6.2019-0939
[research_belligoli_dwight_2021]: https://doi.org/10.2514/1.j059558
[research_benay_berthouze_2001]: https://doi.org/10.2514/2.1267
[research_benay_coet_1989]: https://doi.org/10.1007/978-3-642-73948-4_18
[research_benay_pot_1986]: https://doi.org/10.1007/978-3-642-82770-9_22
[research_bendiksen_1987]: https://doi.org/10.2514/6.1987-911
[research_bendiksen_1992]: https://doi.org/10.2514/6.1992-2121
[research_bendiksen_1993]: https://doi.org/10.2514/6.1993-1479
[research_bendiksen_1994]: https://doi.org/10.1115/imece1994-1448
[research_bendiksen_1998]: https://doi.org/10.2514/6.1998-1726
[research_bendiksen_1999]: https://doi.org/10.2514/6.1999-1350
[research_bendiksen_2004]: https://doi.org/10.2514/6.2004-1694
[research_bendiksen_2004_b]: https://doi.org/10.1016/j.jfluidstructs.2004.01.005
[research_bendiksen_2006]: https://doi.org/10.1115/pvp2006-icpvt-11-93960
[research_bendiksen_2007]: https://doi.org/10.2514/6.2007-2017
[research_bendiksen_2008]: https://doi.org/10.2514/1.29547
[research_bendiksen_2009]: https://doi.org/10.2514/1.36413
[research_bendiksen_2009_b]: https://doi.org/10.2514/6.2009-2313
[research_bendiksen_2011]: https://doi.org/10.1016/j.paerosci.2010.07.001
[research_bendiksen_2013]: https://doi.org/10.2514/6.2013-1593
[research_bendiksen_2015]: https://doi.org/10.2514/6.2015-0438
[research_bendiksen_davis_1995]: https://doi.org/10.2514/6.1995-1486
[research_bendiksen_hwang_1996]: https://doi.org/10.2514/6.1996-1343
[research_bendiksen_hwang_1997]: https://doi.org/10.2514/6.1997-1269
[research_bendiksenoddvaro_kousenkennetha_1989]: https://ntrs.nasa.gov/citations/19890009887
[research_benedikt_1953]: https://doi.org/10.2514/8.2809
[research_benepe_cunninghamjr_1975]: https://doi.org/10.2514/6.1975-68
[research_benepedb_cunninghamamjr_1978]: https://ntrs.nasa.gov/citations/19780025170
[research_bengelink_doerzbacher_1986]: https://doi.org/10.2514/6.1986-759
[research_bengida_2025]: https://doi.org/10.2514/6.2025-3583
[research_benhachmidriss_greberisaac_1989]: https://ntrs.nasa.gov/citations/19890041036
[research_bennett_abel_1981]: https://doi.org/10.2514/6.1981-652
[research_bennett_batina_1988]: https://doi.org/10.2514/6.1988-2347
[research_bennett_batina_1989]: https://doi.org/10.2514/3.45854
[research_bennett_bland_1987]: https://doi.org/10.2514/6.1987-851
[research_bennett_dansberry_1991]: https://doi.org/10.2514/6.1991-1107
[research_bennett_dansberry_1993]: https://doi.org/10.2514/3.46314
[research_bennettrobertm_batinajohnt_1989]: https://ntrs.nasa.gov/citations/19900046299
[research_benoit_legrain_1987]: https://doi.org/10.2514/6.1987-2356
[research_benyamen_mckinnis_2020]: https://doi.org/10.1109/aero47225.2020.9172481
[research_beran_morton_1997]: https://doi.org/10.2514/2.4172
[research_bergen_arnold_1940]: https://doi.org/10.2514/8.1231
[research_bergier]: https://doi.org/10.70675/6e6752d9z395bz4da8z8691z37734dd62f09
[research_bergman_1948]: https://doi.org/10.21236/ada301214
[research_bergman_1949]: https://doi.org/10.21236/ada298367
[research_berkowitz_kyriss_1977]: https://doi.org/10.2514/6.1977-125
[research_bernardini_pirozzoli_2011]: https://doi.org/10.1504/ijesms.2011.038750
[research_berndt_1964]: https://doi.org/10.1007/978-3-642-88337-8_19
[research_berndt_1976]: https://doi.org/10.21236/ada035308
[research_bernstein_1953]: https://doi.org/10.2514/8.2844
[research_bernstein_1997]: https://doi.org/10.1017/s0001924000065969
[research_berry_gilyard_1973]: https://doi.org/10.2514/6.1973-831
[research_berry_yang_1985]: https://doi.org/10.2514/6.1985-586
[research_berrysa_1986]: https://ntrs.nasa.gov/citations/19860017742
[research_bertelrud_1980]: https://doi.org/10.2514/6.1980-423
[research_bertelrud_1981]: https://doi.org/10.2514/6.1981-1216
[research_bertelrud_bergmann_1980]: https://doi.org/10.2514/6.1980-5
[research_bertelrud_graves_1994]: https://doi.org/10.2514/6.1994-2152
[research_bertelrudarild_1989]: https://ntrs.nasa.gov/citations/19890011557
[research_bhaduri_sugarno_2024]: https://doi.org/10.1063/5.0234999
[research_bhanderi_babinsky_2004]: https://doi.org/10.2514/6.2004-2147
[research_bhanderi_babinsky_2005]: https://doi.org/10.2514/6.2005-4896
[research_bharadvaj_1990]: https://doi.org/10.2514/6.1990-935
[research_bharadvaj_1991]: https://doi.org/10.2514/3.10817
[research_bhardwaj_sriram_2019]: https://doi.org/10.3850/978-981-11-2730-4_0291-cd
[research_bhat_1971]: https://doi.org/10.1016/0022-460x(71)90574-8
[research_bhat_2018]: https://doi.org/10.1201/9781315370613-9
[research_bhatia_beran_2014]: https://doi.org/10.2514/6.2014-0336
[research_bhatia_beran_2016]: https://doi.org/10.2514/6.2016-4119
[research_bhatia_beran_2017]: https://doi.org/10.2514/1.j055930
[research_bhatia_beran_2017_b]: https://doi.org/10.2514/1.j055839
[research_bhatia_beran_2017_c]: https://doi.org/10.2514/1.c034301
[research_bhatmk_vakiliad_1990]: https://ntrs.nasa.gov/citations/19910006668
[research_bhola_sengupta_2019]: https://doi.org/10.1063/1.5099206
[research_biber_2005]: https://doi.org/10.2514/6.2005-619
[research_biber_2015]: https://doi.org/10.2514/6.2015-0031
[research_biber_tilmann_2003]: https://doi.org/10.2514/6.2003-1095
[research_bichngoc_hung_2011]: https://doi.org/10.15625/0866-7136/33/3/210
[research_bidwell_1991]: https://doi.org/10.2514/6.1991-447
[research_bielatralphp_1959]: https://ntrs.nasa.gov/citations/19980232001
[research_bielatralphp_campbellgeorges_1953]: https://ntrs.nasa.gov/citations/19930087724
[research_bies_1966]: https://doi.org/10.1121/1.1942855
[research_bihrle_jr_1980]: https://doi.org/10.21236/ada082335
[research_biibosunov_karybekov_1967]: https://doi.org/10.1007/bf01015148
[research_billingsley_1976]: https://doi.org/10.21236/ada024445
[research_binion_jr_1974]: https://doi.org/10.21236/ad0787658
[research_binion_lo_1970]: https://doi.org/10.2514/3.44121
[research_binion_tw_1971]: https://doi.org/10.21236/ad0723294
[research_binion_tw_1975]: https://doi.org/10.21236/ada012000
[research_binion_tw_1976]: https://doi.org/10.21236/ada031997
[research_binionjr_1969]: https://doi.org/10.2514/6.1969-171
[research_binionjr_lo_1972]: https://doi.org/10.2514/6.1972-1009
[research_biot_1949]: https://doi.org/10.1090/qam/28157
[research_bippes_1990]: https://doi.org/10.1007/978-3-642-84103-3_38
[research_birdga_1991]: https://ntrs.nasa.gov/citations/19910058761
[research_biswas_jimbo_2015]: https://doi.org/10.1115/gtindia2015-1225
[research_biswas_mustak_2025]: https://doi.org/10.11648/j.eas.20251002.11
[research_black]: https://doi.org/10.22215/etd/1993-02521
[research_black_1968]: https://doi.org/10.2514/6.1968-361
[research_black_1969]: https://doi.org/10.2514/3.43999
[research_black_carleton_1963]: https://doi.org/10.21236/ad0409079
[research_blackwell_1979]: https://doi.org/10.2514/3.58514
[research_blackwell_pounds_1977]: https://doi.org/10.2514/3.58877
[research_blackwelljajr_1969]: https://ntrs.nasa.gov/citations/19690006789
[research_blackwelljr_1978]: https://doi.org/10.2514/6.1978-806
[research_blaha_1969]: https://doi.org/10.2514/6.1969-427
[research_blanchard_larman_1993]: https://doi.org/10.2514/6.1993-836
[research_blanchard_phillips_1980]: https://doi.org/10.2514/6.1980-1578
[research_blanchardwillards_1953]: https://ntrs.nasa.gov/citations/20090023638
[research_blanco_battiato_2019]: https://doi.org/10.2514/6.2019-3095
[research_bland_edwards_1983]: https://doi.org/10.2514/6.1983-959
[research_blandsr_youngls_1961]: https://ntrs.nasa.gov/citations/19660024039
[research_bleimeyer_1981]: https://doi.org/10.2514/6.1981-2515
[research_bliss_1980]: https://doi.org/10.21236/ada093301
[research_blosch_carroll_1992]: https://doi.org/10.2514/6.1992-3668
[research_blosch_carroll_1993]: https://doi.org/10.2514/3.11921
[research_blose_1949]: https://doi.org/10.21236/ada377827
[research_blt_shuttle_2016]: https://ntrs.nasa.gov/citations/20160010109
[research_bluman_gandhi_2011]: https://doi.org/10.4050/jahs.56.032005
[research_bobbitt_1990]: https://doi.org/10.1007/978-1-4612-3430-2_15
[research_bobenriethmiserda_lauterjung_2006]: https://doi.org/10.2514/6.2006-452
[research_bodapati_1984]: https://doi.org/10.2514/6.1984-1563
[research_bodapati_1984_b]: https://doi.org/10.2514/6.1984-597
[research_bodapati_lee_1986]: https://doi.org/10.2514/3.9546
[research_bodin_fuchs_2008]: https://doi.org/10.2514/6.2008-4174
[research_bodonyi_smith_1986]: https://doi.org/10.1016/0045-7930(86)90002-2
[research_bodspat_schairer_1980]: https://doi.org/10.2514/6.1980-441
[research_boelens_2017]: https://doi.org/10.2514/1.c033211
[research_bogatyrev_2017]: https://doi.org/10.1615/tsagiscij.2017020745
[research_bogdnoff_1953]: https://doi.org/10.21236/ad0009823
[research_bogdonoff_1987]: https://doi.org/10.21236/ada187642
[research_bogdonoff_1989]: https://doi.org/10.21236/ada205923
[research_bogdonoff_smits_1992]: https://doi.org/10.21236/ada250209
[research_bogomolov_1968]: https://doi.org/10.1007/bf01016243
[research_bohning_doerffer_2002]: https://doi.org/10.1007/978-3-540-45856-2_4
[research_bohning_thiede_1994]: https://doi.org/10.1007/978-3-7091-9310-5_25
[research_boiarski_daum_1972]: https://doi.org/10.21236/ad0761500
[research_boling_zha_2020]: https://doi.org/10.2514/6.2020-2792
[research_boling_zha_2021]: https://doi.org/10.2514/6.2021-1732
[research_bonnifet_gerolymos_2017]: https://doi.org/10.2514/6.2017-3955
[research_bonometti_sorensen_2006]: https://doi.org/10.2514/6.2006-7277
[research_bons_martins_2020]: https://doi.org/10.3390/aerospace7080118
[research_boothe_chen_1974]: https://doi.org/10.21236/ad0782218
[research_boppe_1977]: https://doi.org/10.2514/6.1977-207
[research_boppe_1978]: https://doi.org/10.2514/6.1978-104
[research_boppecw_1980]: https://ntrs.nasa.gov/citations/19800016802
[research_borden_1930]: https://doi.org/10.21236/ada377418
[research_borland_1979]: https://doi.org/10.21236/ada069839
[research_borland_rizzetta_1981]: https://doi.org/10.2514/6.1981-608
[research_borland_rizzetta_1982]: https://doi.org/10.2514/3.7993
[research_borland_sotomayer_1989]: https://doi.org/10.2514/6.1989-2230
[research_borlandcj_manrome_1983]: https://ntrs.nasa.gov/citations/19830013892
[research_boroughs_das_1999]: https://doi.org/10.2514/6.1999-1280
[research_borovoy_mosharov_2012]: https://doi.org/10.1051/eucass/201203015
[research_boswinklerwjr_smithsliii_1958]: https://ntrs.nasa.gov/citations/19660027826
[research_boundary_layer_transition_measurements_1959]: https://doi.org/10.1016/0043-1648(59)90193-0
[research_boundry_value_2002]: https://doi.org/10.1108/aeat.2002.12774eae.003
[research_bouquet_vos_2017]: https://doi.org/10.2514/6.2017-0236
[research_bourdet_bouhadji_2003]: https://doi.org/10.1023/b:appl.0000014932.28421.9e
[research_bourguet_braza_2011]: https://doi.org/10.1016/j.jcp.2010.09.019
[research_bourisli_hamadeh_2020]: https://doi.org/10.2514/6.2020-1297
[research_boutemedjet_samardzic_2018]: https://doi.org/10.1016/j.measurement.2017.11.043
[research_bouton_1951]: https://doi.org/10.2514/8.1879
[research_bowers_1980]: https://doi.org/10.2514/6.1980-1158
[research_boyd_1965]: https://doi.org/10.2514/6.1965-752
[research_boyd_1977]: https://doi.org/10.21236/ada053640
[research_boydenrp_1974]: https://ntrs.nasa.gov/citations/19830002753
[research_boylan_1963]: https://doi.org/10.21236/ad0402935
[research_boyle_2002]: https://doi.org/10.2514/6.2002-2818
[research_boyle_2003]: https://doi.org/10.2514/6.2003-4083
[research_boylesjr_1986]: https://doi.org/10.2514/6.1986-783
[research_brady_maier_1954]: https://doi.org/10.21236/ad0055205
[research_bragg_soltani_1990]: https://doi.org/10.2514/3.45928
[research_braman_schweikhard_1983]: https://doi.org/10.2514/6.1983-2751
[research_branch_zang_2023]: https://doi.org/10.2514/6.2023-3506
[research_brandon_brown_1995]: https://doi.org/10.2514/6.1995-3457
[research_braune_hebler_2018]: https://doi.org/10.2514/6.2018-3641
[research_bray_1998]: https://doi.org/10.2514/6.1998-2632
[research_brazzel_1963]: https://doi.org/10.21236/ad0423963
[research_bredif_1983]: https://doi.org/10.2514/6.1983-507
[research_breitsamter_laschka_1994]: https://doi.org/10.2514/3.46560
[research_brentwpomeroy_richardlcampbell]: https://ntrs.nasa.gov/citations/20230016801
[research_bretkstanford_andrewsthelen]: https://ntrs.nasa.gov/citations/20240007174
[research_bretkstanford_anniesauer]: https://ntrs.nasa.gov/citations/20210024619
[research_bretkstanford_kevinejacobson]: https://ntrs.nasa.gov/citations/20220017734
[research_bretkstanford_stevenjmassey]: https://ntrs.nasa.gov/citations/20250010633
[research_bretthiller_richardcampbell]: https://ntrs.nasa.gov/citations/20240015891
[research_brettrhiller_richardlcampbell]: https://ntrs.nasa.gov/citations/20210016792
[research_brettrhiller_richardlcampbell_b]: https://ntrs.nasa.gov/citations/20230016544
[research_briggs_reed_1982]: https://doi.org/10.21236/ada125764
[research_brilliant_adamson_1974]: https://doi.org/10.2514/3.49228
[research_brilliant_adamsonjr_1973]: https://doi.org/10.2514/6.1973-239
[research_brincklow_montgomery_2021]: https://doi.org/10.2514/6.2021-0327
[research_brion_dandois_2017]: https://doi.org/10.1051/eucass/2016090365
[research_brion_rembaut_2026]: https://doi.org/10.2514/6.2026-4457
[research_britcher_landman_2024]: https://doi.org/10.1016/b978-0-12-818099-0.00002-1
[research_brodsky_1970]: https://doi.org/10.21236/ad0716026
[research_bronz_2019]: https://doi.org/10.2514/6.2019-3171
[research_bronz_garciademarina_2017]: https://doi.org/10.2514/6.2017-0698
[research_brooks_stainback_1980]: https://doi.org/10.2514/6.1980-434
[research_brookscuylerwjr_harrischarlesd_1994]: https://ntrs.nasa.gov/citations/19950004327
[research_brosh_kussoy_1983]: https://doi.org/10.2514/6.1983-1757
[research_broughton_rainbird_1995]: https://doi.org/10.1016/0167-6105(94)00005-x
[research_brouwer_2017]: https://doi.org/10.2514/1.j056030
[research_browerjr_1989]: https://doi.org/10.2514/6.1989-3382
[research_brown_2004]: https://doi.org/10.2514/6.2004-4949
[research_brown_bastian_2008]: https://doi.org/10.2514/6.2008-1651
[research_brown_bradley_1981]: https://doi.org/10.2514/6.1981-2390
[research_brown_harris_1984]: https://doi.org/10.2514/6.1984-875
[research_brown_kussoy_1986]: https://doi.org/10.1007/978-3-642-82770-9_12
[research_browne_1990]: https://doi.org/10.2514/6.1990-7
[research_browne_maldonado_2024]: https://doi.org/10.2514/6.2024-0065
[research_browne_maldonado_2025]: https://doi.org/10.2514/1.c037981
[research_brucejr_fuller_1984]: https://doi.org/10.2514/6.1984-584
[research_brunet_deck_2008]: https://doi.org/10.2514/6.2008-4152
[research_brunncyrild_stillwellwendellh_1956]: https://ntrs.nasa.gov/citations/19930089147
[research_brunosantos_oliveira_2020]: https://doi.org/10.5151/siintec2020-analysisofelevator
[research_brunton_noack_2020]: https://doi.org/10.1146/annurev-fluid-010719-060214
[research_brutyan_volkov_2020]: https://doi.org/10.1134/s1063785020060188
[research_bryce_pinker_1977]: https://doi.org/10.2514/6.1977-1327
[research_bryson_2021]: https://doi.org/10.21236/ad1146662
[research_bryson_rumpfkeil_2016]: https://doi.org/10.2514/6.2016-0294
[research_brysonjr_1971]: https://doi.org/10.2514/6.1971-913
[research_brysonjr_desai_1968]: https://doi.org/10.2514/6.1968-877
[research_buckingham_1914]: https://doi.org/10.1103/physrev.4.345
[research_budhdev_senthilkumar_2026]: https://doi.org/10.2514/6.2026-111949
[research_bueno_sandovalgoes_2014]: https://doi.org/10.1155/2014/597827
[research_buffet_loads_1958]: https://ntrs.nasa.gov/citations/19930093826
[research_buffet_response_1974]: https://ntrs.nasa.gov/citations/19740043918
[research_buffet_response_1978]: https://ntrs.nasa.gov/citations/19780025173
[research_buffet_rocket_models_1953]: https://ntrs.nasa.gov/citations/20050041783
[research_bull_bridges_1983]: https://doi.org/10.2514/6.1983-2750
[research_bull_bridges_1985]: https://doi.org/10.2514/3.45108
[research_bulygina_1958]: https://doi.org/10.1016/0021-8928(58)90043-1
[research_bur_benay_2000]: https://doi.org/10.2514/6.2000-933
[research_bur_benay_2002]: https://doi.org/10.1007/978-3-540-45856-2_3
[research_bur_berthouze_2003]: https://doi.org/10.1007/978-94-010-0017-8_8
[research_bur_coponet_2009]: https://doi.org/10.1007/s00193-009-0234-6
[research_bur_corbel_1997]: https://doi.org/10.2514/6.1997-217
[research_bur_corbel_1998]: https://doi.org/10.2514/2.376
[research_bur_corbel_2000]: https://doi.org/10.2514/6.2000-2610
[research_burble_1939_pressures]: https://ntrs.nasa.gov/citations/19930091721
[research_burble_delay_1939]: https://ntrs.nasa.gov/citations/20090015112
[research_burble_delay_1944]: https://ntrs.nasa.gov/citations/19930081766
[research_burchamfrankwjr_burkenjohnj_1997]: https://ntrs.nasa.gov/citations/19980210483
[research_burchamfrankwjr_gatlindonaldh_1995]: https://ntrs.nasa.gov/citations/19950026589
[research_burchamjr_burken_1994]: https://doi.org/10.2514/6.1994-2123
[research_burchamjr_maine_1993]: https://doi.org/10.2514/6.1993-1820
[research_burchamjr_pappas_1996]: https://doi.org/10.2514/6.1996-3742
[research_burchamjr_ray_1987]: https://doi.org/10.2514/6.1987-2877
[research_burdett_1947]: https://doi.org/10.2514/8.4136
[research_burdges_1973]: https://doi.org/10.2514/6.1973-792
[research_burdges_1979]: https://doi.org/10.2514/6.1979-1499
[research_burdges_1981]: https://doi.org/10.2514/3.57509
[research_burdgeskp_blackwelljajr_1975]: https://ntrs.nasa.gov/citations/19750013179
[research_burgess_1946]: https://doi.org/10.2514/8.4076
[research_burghiu_2023]: https://doi.org/10.13111/2066-8201.2023.15.4.5
[research_burnham_1995]: https://doi.org/10.2514/6.1995-1338
[research_burns_danehy_2017]: https://doi.org/10.2514/6.2017-0026
[research_burrin_salikuddin_1986]: https://doi.org/10.2514/6.1986-1888
[research_burris_bender_1969]: https://doi.org/10.21236/ad0865310
[research_burrows_vukasinovic_2019]: https://doi.org/10.2514/6.2019-3687
[research_burrows_vukasinovic_2021]: https://doi.org/10.1007/s00348-021-03280-x
[research_bursey_dickinson_1990]: https://doi.org/10.2514/6.1990-1906
[research_burstein_1965]: https://doi.org/10.21236/ad0623323
[research_burtch_2015]: https://doi.org/10.2514/6.2015-2236
[research_burton_loth_2007]: https://doi.org/10.2514/6.2007-5841
[research_busan_1998]: https://doi.org/10.21236/ada340820
[research_busemann_1964]: https://doi.org/10.1063/1.1711387
[research_busquet]: https://doi.org/10.70675/014497b4z6e9ez43ebza05bz26351f1481dd
[research_butler_1976]: https://doi.org/10.21236/ada023690
[research_butler_jones_1984]: https://doi.org/10.1017/s000192400002073x
[research_buxbaum_svenson_1972]: https://doi.org/10.1016/b978-0-08-017526-3.50019-1
[research_buxton_beran_1997]: https://doi.org/10.2514/6.1997-834
[research_buzzi_fico_2006]: https://doi.org/10.2514/6.2006-3670
[research_bynum_ledford_1970]: https://doi.org/10.21236/ad0714565
[research_byrdsongta_1977]: https://ntrs.nasa.gov/citations/19770010053
[research_byrdsongta_brookscwjr_1980]: https://ntrs.nasa.gov/citations/19830002872
[research_byreddy_grandhi_2003]: https://doi.org/10.21236/ada417124
[research_cabaleirodelahoz_fioriti_2021]: https://doi.org/10.1177/09544100211063110
[research_caballero_2001]: https://doi.org/10.1007/978-3-540-45359-8_40
[research_cahill_1986]: https://doi.org/10.4271/861846
[research_cahill_minter_2010]: https://doi.org/10.2514/6.2010-1716
[research_cahn_garcia_1971]: https://doi.org/10.2514/3.44233
[research_caiger_gould_1971]: https://doi.org/10.1007/978-1-4684-8346-8_9
[research_cain_1979]: https://doi.org/10.21236/ada379310
[research_calarese_walterick_1978]: https://doi.org/10.2514/6.1978-1180
[research_calspan_ejector_1982]: https://ntrs.nasa.gov/citations/19820041123
[research_camberos_kolonay_2014]: https://doi.org/10.2514/6.2014-1194
[research_camberos_kolonay_2015]: https://doi.org/10.1017/s0001924000011349
[research_campbell_1984]: https://doi.org/10.2514/6.1984-2150
[research_campbell_smith_1987]: https://doi.org/10.2514/6.1987-2552
[research_campbell_waggoner_1986]: https://doi.org/10.2514/6.1986-314
[research_canbazoglu_lin_1996]: https://doi.org/10.2514/3.46920
[research_candler_2001]: https://doi.org/10.21236/ada387503
[research_candon_hale_2024]: https://doi.org/10.2514/6.2024-1266
[research_candon_levinski_2019]: https://doi.org/10.2514/6.2019-0763
[research_canic_keyfitz_1995]: https://doi.org/10.2172/764166
[research_canic_keyfitz_1996]: https://doi.org/10.1006/jdeq.1996.0040
[research_canic_keyfitz_2000]: https://doi.org/10.4310/maa.2000.v7.n2.a4
[research_canic_kim_2001]: https://doi.org/10.1007/978-3-0348-8370-2_23
[research_canoville_lewis_2025]: https://doi.org/10.2139/ssrn.5336052
[research_canter_groves_1994]: https://doi.org/10.2514/6.1994-2171
[research_cao_fu_2024]: https://doi.org/10.1007/978-981-97-3998-1_113
[research_cao_lin_2025]: https://doi.org/10.2139/ssrn.5375639
[research_cao_lyu_2024]: https://doi.org/10.3390/act13090369
[research_capone_1975]: https://doi.org/10.2514/6.1975-1315
[research_capone_mason_1983]: https://doi.org/10.2514/6.1983-86
[research_capone_re_1987]: https://doi.org/10.2514/6.1987-1836
[research_caponefj_maidendl_1977]: https://ntrs.nasa.gov/citations/19780004094
[research_caponefj_masonml_1984]: https://ntrs.nasa.gov/citations/19870001437
[research_carbonara_binnie_1938]: https://doi.org/10.2514/8.678
[research_carden_1963]: https://doi.org/10.21236/ad0401921
[research_carey_1964]: https://doi.org/10.2514/6.1964-268
[research_carey_1965]: https://doi.org/10.2514/3.28141
[research_carloni_azevedo_2023]: https://doi.org/10.2514/6.2023-1196
[research_carlsen_1994]: https://doi.org/10.2514/6.1994-1841
[research_carlsen_1995]: https://doi.org/10.2514/3.46836
[research_carlson_1976]: https://doi.org/10.2514/3.58667
[research_carlson_1981]: https://doi.org/10.1007/978-3-663-14008-5_11
[research_carlson_glauser_2004]: https://doi.org/10.2514/6.2004-579
[research_carlson_pendergraftjr_1985]: https://doi.org/10.2514/6.1985-1264
[research_carlson_weed_1985]: https://doi.org/10.2514/6.1985-4075
[research_carlsonharryw_mcleanfedward_1965]: https://ntrs.nasa.gov/citations/20000011993
[research_carlsonhw_millerds_1969]: https://ntrs.nasa.gov/citations/19700004052
[research_carlsonla_1979]: https://ntrs.nasa.gov/citations/19790009634
[research_carmelmelvinm_turnerkennethl_1957]: https://ntrs.nasa.gov/citations/20090023600
[research_carpenter_hantsche_2025]: https://doi.org/10.2514/6.2025-0194
[research_carr_chandrasekhara_1998]: https://doi.org/10.2514/6.1998-332
[research_carrese_marzocca_2016]: https://doi.org/10.2514/6.2016-1552
[research_carter_1988]: https://doi.org/10.2514/6.1988-2045
[research_carter_hafez_1982]: https://doi.org/10.21236/ada121299
[research_carter_vicroy_2009]: https://doi.org/10.2514/6.2009-935
[research_casey_1988]: https://doi.org/10.21236/ada195699
[research_cassel_durando_1969]: https://doi.org/10.21236/ad0862483
[research_castellani_cooper_2016]: https://doi.org/10.1155/2016/4805817
[research_castro_ekaterinaris_2000]: https://doi.org/10.2514/6.2000-984
[research_castro_ekaterinaris_2002]: https://doi.org/10.2514/2.1803
[research_castro_jones_2001]: https://doi.org/10.2514/6.2001-2725
[research_castro_jones_2003]: https://doi.org/10.1007/978-94-010-0017-8_12
[research_catalano_fremaux_1987]: https://doi.org/10.2514/3.45493
[research_caughey_1976]: https://doi.org/10.2514/3.58626
[research_caughey_1982]: https://doi.org/10.1016/b978-0-12-493280-7.50009-7
[research_caughey_jameson_1977]: https://doi.org/10.2514/6.1977-677
[research_caughey_jameson_1979]: https://doi.org/10.2514/3.61092
[research_caughey_jameson_1979_b]: https://doi.org/10.2514/6.1979-1513
[research_cavcar_2006]: https://doi.org/10.2514/1.14252
[research_cebecit_1974]: https://ntrs.nasa.gov/citations/19740037543
[research_cecrdle_2011]: https://doi.org/10.2514/6.2011-1849
[research_celestino_olichevishalila_2026]: https://doi.org/10.2514/6.2026-4342
[research_celik_roberts_1992]: https://doi.org/10.2514/6.1992-4430
[research_celmins_1990]: https://doi.org/10.21236/ada224217
[research_cenko_madson_1993]: https://doi.org/10.2514/6.1993-855
[research_cfd_analysis_of_2015]: https://doi.org/10.15623/ijret.2015.0409047
[research_chakrabartty_1990]: https://doi.org/10.1007/bf01176987
[research_chakrabartty_dhanalakshmi_1995]: https://doi.org/10.2514/3.12756
[research_chakraborty_ozcan_2015]: https://doi.org/10.2514/6.2015-3287
[research_chakraborty_roy_2022]: https://doi.org/10.1063/5.0104299
[research_chakravarty_narayanaswamy_2026]: https://doi.org/10.2514/6.2026-1244
[research_chaloner_verdinelli_1995]: https://doi.org/10.1214/ss/1177009939
[research_chan_1980]: https://doi.org/10.2514/3.57983
[research_chan_1980_b]: https://doi.org/10.2514/3.44667
[research_chan_1985]: https://doi.org/10.1007/bf00949035
[research_chan_chen_1976]: https://doi.org/10.21236/adb013236
[research_chan_hooker_2017]: https://doi.org/10.2514/6.2017-0098
[research_chan_jones_2017]: https://doi.org/10.2514/6.2017-3246
[research_chan_yeung_1997]: https://doi.org/10.2514/6.1997-295
[research_chandler_chisholm_1993]: https://doi.org/10.2514/6.1993-2544
[research_chandrasekhara_1994]: https://doi.org/10.21236/ada291804
[research_chandrasekhara_carr_1989]: https://doi.org/10.2514/6.1989-23
[research_chandrasekhara_carr_1990]: https://doi.org/10.2514/3.25313
[research_chandrasekharan_iarocci_2015]: https://doi.org/10.4271/2015-01-2566
[research_chandravamsi_bhardwaj_2023]: https://doi.org/10.1063/5.0132358
[research_chang_1962]: https://doi.org/10.21236/ad0274359
[research_chang_1981]: https://doi.org/10.2172/6571749
[research_chang_cai_2022]: https://doi.org/10.2514/1.j061209
[research_chanzy]: https://doi.org/10.70675/7b37fd70z8fa1z4932za5c1z2fe8a3577a93
[research_chao_shijun_1996]: https://doi.org/10.2514/6.1996-2441
[research_chao_vandam_1998]: https://doi.org/10.2514/6.1998-2783
[research_chaparro_fujiwara_2016]: https://doi.org/10.2514/6.2016-3418
[research_chaparro_fujiwara_2017]: https://doi.org/10.2514/6.2017-4221
[research_chaplin_2013]: https://doi.org/10.2514/6.2013-2911
[research_chapman_bonness_1992]: https://doi.org/10.2514/6.1992-651
[research_chapter_4_1957]: https://doi.org/10.1515/9781400879908-010
[research_chapter_nine_1990]: https://doi.org/10.1515/9781400860777.159
[research_charlesdharris_1975]: https://ntrs.nasa.gov/citations/19830002805
[research_chase_1992]: https://doi.org/10.21236/ada257253
[research_chassaing_lucor_2010]: https://doi.org/10.2514/1.42637
[research_chau_piotrowski_2026]: https://doi.org/10.2514/1.c038646
[research_chau_zingg_2022]: https://doi.org/10.2514/1.c036389
[research_chaudhuri_1977]: https://doi.org/10.21236/ada064016
[research_chaudhuri_balasubramanyan_1982]: https://doi.org/10.2514/6.1982-958
[research_chaussee_1978]: https://doi.org/10.2514/6.1978-212
[research_chen_1981]: https://doi.org/10.2514/6.1981-381
[research_chen_1982]: https://doi.org/10.2514/6.1982-162
[research_chen_1983]: https://doi.org/10.2514/3.8162
[research_chen_1990]: https://doi.org/10.2514/6.1990-1415
[research_chen_2018]: https://doi.org/10.1063/1.5033619
[research_chen_bui_1990]: https://doi.org/10.2514/6.1990-1586
[research_chen_cantwell_1989]: https://doi.org/10.2514/6.1989-285
[research_chen_cantwell_1990]: https://doi.org/10.1063/1.857606
[research_chen_chan_1976]: https://doi.org/10.21236/adb014225
[research_chen_clark_1985]: https://doi.org/10.2514/6.1985-1642
[research_chen_dong_2021]: https://doi.org/10.1016/j.enconman.2021.114339
[research_chen_gao_2020]: https://doi.org/10.1016/j.ast.2020.105871
[research_chen_gao_2022]: https://doi.org/10.1016/j.ast.2022.107668
[research_chen_gao_2023]: https://doi.org/10.3390/aerospace10050486
[research_chen_gat_2022]: https://doi.org/10.2139/ssrn.4218361
[research_chen_li_1987]: https://doi.org/10.2514/6.1987-521
[research_chen_liu_2000]: https://doi.org/10.2514/6.2000-1486
[research_chen_liu_2014]: https://doi.org/10.4028/www.scientific.net/amm.574.480
[research_chen_mears_1957]: https://doi.org/10.21236/ad0144320
[research_chen_sajben_1979]: https://doi.org/10.2514/3.61280
[research_chen_sulaeman_2002]: https://doi.org/10.21236/ada399365
[research_chen_thuerey_2024]: https://doi.org/10.1063/5.0238413
[research_chen_ulker_2009]: https://doi.org/10.2514/1.42489
[research_chen_vassberg_1984]: https://doi.org/10.2514/6.1984-2157
[research_chen_vassberg_1985]: https://doi.org/10.2514/3.9191
[research_chen_verhoff_1982]: https://doi.org/10.2514/6.1982-108
[research_chen_wang_2024]: https://doi.org/10.1063/5.0228209
[research_chen_wang_2026]: https://doi.org/10.2139/ssrn.6110070
[research_chen_wang_2026_b]: https://doi.org/10.1016/j.ast.2026.112456
[research_chen_wei_2023]: https://doi.org/10.1177/09544100231207558
[research_chen_xu_2009]: https://doi.org/10.1615/tsfp6.1700
[research_chen_zha_2006]: https://doi.org/10.2514/6.2006-3216
[research_chen_zhang_2006]: https://doi.org/10.2514/6.2006-3334
[research_chen_zhang_2014]: https://doi.org/10.2514/6.2014-2368
[research_chen_zhang_2026]: https://doi.org/10.2139/ssrn.7380660
[research_chenchi_1983]: https://doi.org/10.21236/ada128041
[research_chencl_chowcy_1985]: https://ntrs.nasa.gov/citations/19850019516
[research_cheney_1988]: https://doi.org/10.2514/6.1988-2125
[research_cheng_1977]: https://doi.org/10.2514/3.7330
[research_cheng_1982]: https://doi.org/10.1016/b978-0-12-493280-7.50010-3
[research_cheng_1989]: https://doi.org/10.1137/1031070
[research_cheng_2009]: https://doi.org/10.1017/s1727719100002938
[research_cheng_hafez_1973]: https://doi.org/10.2514/6.1973-88
[research_cheng_hafez_1973_b]: https://doi.org/10.2514/3.6902
[research_cheng_hafez_1975]: https://doi.org/10.1017/s0022112075003011
[research_cheng_lowenberg_2015]: https://doi.org/10.2514/6.2015-2717
[research_cheng_luo_1996]: https://doi.org/10.2514/3.13194
[research_cheng_meng_1980]: https://doi.org/10.2514/6.1980-342
[research_cheng_smith_1994]: https://doi.org/10.1007/bf00944968
[research_chern_keyfitz_2016]: https://doi.org/10.3934/dcds.2016.36.4213
[research_chesneau_wood_1995]: https://doi.org/10.2514/6.1995-439
[research_chestnutt_1966]: https://doi.org/10.21236/ad0629632
[research_cheung_aaronson_1995]: https://doi.org/10.2514/3.46700
[research_chevalier_1960]: https://doi.org/10.21236/ad0241785
[research_chevalier_robertson_1963]: https://doi.org/10.21236/ad0423095
[research_chew_1953]: https://doi.org/10.21236/ad0026928
[research_chew_1955]: https://doi.org/10.21236/ad0069609
[research_chiaraiorio]: https://doi.org/10.20868/upm.thesis.39096
[research_chiarelli_bonomo_2019]: https://doi.org/10.1155/2019/8210235
[research_chieng_1991]: https://doi.org/10.2514/6.1991-171
[research_childsjoanm_1953]: https://ntrs.nasa.gov/citations/19930087404
[research_childsme_seebaughwr_1969]: https://ntrs.nasa.gov/citations/19690054765
[research_childsme_seebaughwr_1970]: https://ntrs.nasa.gov/citations/19700060332
[research_chin_1992]: https://doi.org/10.2514/6.1992-2617
[research_chin_lentink_2019]: https://doi.org/10.1007/s00348-019-2838-7
[research_chin_rizzetta_1979]: https://doi.org/10.1115/1.3424650
[research_chipman_rauch_1985]: https://doi.org/10.2514/6.1985-689
[research_chmielewski_1986]: https://doi.org/10.2514/6.1986-1794
[research_choi_kang_2016]: https://doi.org/10.3795/ksme-b.2016.40.12.785
[research_chou_smith_1978]: https://doi.org/10.2514/6.1978-1359
[research_choudhuri_knight_1995]: https://doi.org/10.2514/6.1995-782
[research_choudhuri_knight_1996]: https://doi.org/10.1017/s0022112096001450
[research_chow_1979]: https://doi.org/10.21236/ada071899
[research_chow_1984]: https://doi.org/10.2514/6.1984-230
[research_chow_1985]: https://doi.org/10.2514/3.8925
[research_chow_huang_1982]: https://doi.org/10.1017/s002211208200113x
[research_chowchuenyen_vandalsemwilliamr_1987]: https://ntrs.nasa.gov/citations/19870035308
[research_chowcy_1986]: https://ntrs.nasa.gov/citations/19860021224
[research_chowcy_holsttl_1985]: https://ntrs.nasa.gov/citations/19860026332
[research_chrissrm_hingstwr_1990]: https://ntrs.nasa.gov/citations/19900065563
[research_christian_gee_2023]: https://doi.org/10.2514/6.2023-3351
[research_christisongray_martins_2026]: https://doi.org/10.2514/6.2026-1010
[research_christopherkdroney_anthonyjsclafani_2020]: https://ntrs.nasa.gov/citations/20205005698
[research_chujulio_flechnerstuartg_1990]: https://ntrs.nasa.gov/citations/19920022002
[research_chujulio_lawingpiercel_1990]: https://ntrs.nasa.gov/citations/19930020260
[research_chung_2000]: https://doi.org/10.2514/2.2620
[research_chung_2000_b]: https://doi.org/10.2514/2.2714
[research_chung_2002]: https://doi.org/10.2514/2.3029
[research_chung_2003]: https://doi.org/10.2514/2.7201
[research_chung_2007]: https://doi.org/10.2514/1.32203
[research_chung_2017]: https://doi.org/10.5139/ijass.2017.18.1.1
[research_chung_lee_2002]: https://doi.org/10.2514/6.2002-2934
[research_chung_lee_2003]: https://doi.org/10.2514/2.3160
[research_chung_miau_1994]: https://doi.org/10.2514/6.1994-2515
[research_chung_miau_1995]: https://doi.org/10.2514/6.1995-238
[research_chung_su_2021]: https://doi.org/10.3390/aerospace8060157
[research_chwalowski_heeg_2017]: https://doi.org/10.2514/6.2017-0190
[research_chwalowski_massey_2022]: https://doi.org/10.2514/6.2022-1347
[research_chwalowskipawel_quoneliot_2016]: https://ntrs.nasa.gov/citations/20160007539
[research_chyu_davis_1979]: https://doi.org/10.2514/6.1979-1554
[research_chyu_kuwahara_1982]: https://doi.org/10.2514/6.1982-350
[research_chyu_schiff_1981]: https://doi.org/10.2514/6.1981-73
[research_chyuwj_davisss_1984]: https://ntrs.nasa.gov/citations/19850004008
[research_chyuwj_davisss_1985]: https://ntrs.nasa.gov/citations/19850016863
[research_cicala_miele_1956]: https://doi.org/10.2514/8.7047
[research_cinnella_2001]: https://doi.org/10.1007/978-3-642-56535-9_21
[research_cinnella_congedo_2006]: https://doi.org/10.2514/6.2006-3881
[research_ciobaca_dandois_2017]: https://doi.org/10.2514/6.2017-3245
[research_clark_2026]: https://doi.org/10.2514/6.2026-2112
[research_clark_adler_2016]: https://doi.org/10.1109/aero.2016.7500618
[research_clark_bain_2010]: https://doi.org/10.2514/6.2010-877
[research_clark_pelkman_2001]: https://doi.org/10.2514/6.2001-910
[research_clarke_allen_2005]: https://doi.org/10.2514/6.2005-6316
[research_clay_1967]: https://doi.org/10.21236/ad0661549
[research_clemens_cortner_1963]: https://doi.org/10.21236/ad0296400
[research_cler_1995]: https://doi.org/10.2514/6.1995-2608
[research_clevensonsa_thompsonrf_1957]: https://ntrs.nasa.gov/citations/19630006361
[research_cline_hyde_1986]: https://doi.org/10.2514/3.25825
[research_clyde_bonner_1984]: https://doi.org/10.21236/ada148355
[research_coakley_1987]: https://doi.org/10.2514/6.1987-416
[research_coates_thamburaj_2008]: https://doi.org/10.2514/1.21905
[research_coder_2021]: https://doi.org/10.2514/1.c035887
[research_coder_2023]: https://doi.org/10.2514/6.2023-2452
[research_coder_2025]: https://doi.org/10.21203/rs.3.rs-6389577/v1
[research_coder_2026]: https://doi.org/10.1007/s13272-026-00956-0
[research_coen_2022]: https://doi.org/10.25144/14333
[research_coen_loubeau_2017]: https://doi.org/10.1121/1.4987783
[research_coen_loubeau_2023]: https://doi.org/10.3397/in_2022_0993
[research_cogo_2024]: https://doi.org/10.21741/9781644903193-4
[research_cohen_1970]: https://doi.org/10.2514/6.1970-584
[research_cohen_motallebi_2006]: https://doi.org/10.1017/s0001924000001196
[research_cohen_motallebi_2008]: https://doi.org/10.1017/s0001924000002372
[research_cole_1985]: https://doi.org/10.21236/ada159101
[research_cole_1986]: https://doi.org/10.2514/6.1986-9
[research_cole_1988]: https://doi.org/10.21236/ada196247
[research_cole_cook_1980]: https://doi.org/10.21236/ada207109
[research_cole_malmuth_1982]: https://doi.org/10.2514/6.1982-933
[research_cole_malmuth_1989]: https://doi.org/10.1016/0093-6413(89)90038-4
[research_cole_malmuth_2005]: https://doi.org/10.1098/rspa.2004.1376
[research_cole_noll_2003]: https://doi.org/10.2514/2.6873
[research_colejuliand_malmuthnormand_1989]: https://ntrs.nasa.gov/citations/19890011567
[research_colera_perezsaborid_2018]: https://doi.org/10.1016/j.jsv.2018.01.041
[research_colestanleyr_mossstevenw_1990]: https://ntrs.nasa.gov/citations/19910004099
[research_colgren_1996]: https://doi.org/10.2514/6.1996-3743
[research_collar_1946]: https://doi.org/10.1017/s0368393100120358
[research_collazogarcia_ansell_2018]: https://doi.org/10.2514/6.2018-3177
[research_collazogarcia_ansell_2019]: https://doi.org/10.2514/6.2019-2858
[research_collazogarcia_ansell_2021]: https://doi.org/10.2514/6.2021-1432
[research_collazogarcia_saxtonfox_2021]: https://doi.org/10.2514/6.2021-1646
[research_collins_1970]: https://doi.org/10.2514/6.1970-552
[research_collins_1974]: https://doi.org/10.2514/3.49433
[research_comfort_todisco_1969]: https://doi.org/10.2514/6.1969-8
[research_commercial_transports_aerodynamic_1982]: https://doi.org/10.2514/5.9781600865558.0081.0147
[research_comparative_drag_1949]: https://ntrs.nasa.gov/citations/19930083198
[research_comparative_drag_1950]: https://ntrs.nasa.gov/citations/19930092048
[research_comparison_of_1975]: https://doi.org/10.2514/5.9781600865121.0493.0506
[research_comparison_of_1994]: https://doi.org/10.2514/6.1994-2273
[research_compressible_subsonic_2021]: https://doi.org/10.1017/9781009105842.010
[research_compressible_subsonic_2025]: https://doi.org/10.1017/9781009501293.010
[research_computation_of_1985]: https://doi.org/10.2514/6.1985-1032
[research_computational_methods_1989]: https://doi.org/10.2514/5.9781600865947.0211.0261
[research_connolly_1965]: https://doi.org/10.21236/ad0467829
[research_consigny_gravelle_1983]: https://doi.org/10.2514/6.1983-1809
[research_contirj_thomaspd_1972]: https://ntrs.nasa.gov/citations/19720013201
[research_control_derivative_2023]: https://ntrs.nasa.gov/citations/20230018641
[research_cook]: https://doi.org/10.31274/rtd-180815-4335
[research_cook_1979]: https://doi.org/10.1090/qam/542990
[research_cook_1995]: https://doi.org/10.2514/6.1995-476
[research_cook_ghee_2004]: https://doi.org/10.2514/6.2004-5052
[research_cook_schleiniger_1993]: https://doi.org/10.1137/1.9781611970975.ch4
[research_cookioannidis_1991]: https://doi.org/10.21236/ada239292
[research_cooksey_dillenschneider_1964]: https://doi.org/10.2514/6.1964-1108
[research_cookwj_1978]: https://ntrs.nasa.gov/citations/19780018210
[research_cookwj_chaneymj_1978]: https://ntrs.nasa.gov/citations/19790003842
[research_cookwj_presleyll_1975]: https://ntrs.nasa.gov/citations/19760052584
[research_cookwj_presleyll_1978]: https://ntrs.nasa.gov/citations/19780048421
[research_coon_chapman_1991]: https://doi.org/10.2514/6.1991-1620
[research_coppin_martin_2025]: https://doi.org/10.2514/6.2025-1840
[research_cornetteeldens_1961]: https://ntrs.nasa.gov/citations/20040003909
[research_cornettees_rigbyrn_1962]: https://ntrs.nasa.gov/citations/19620005297
[research_cornish_1963]: https://doi.org/10.21236/ad0426784
[research_coschignano_babinsky_2018]: https://doi.org/10.2514/6.2018-1513
[research_coschignano_babinsky_2019]: https://doi.org/10.2514/6.2019-1844
[research_cosentino_holst_1985]: https://doi.org/10.2514/6.1985-424
[research_cosentinogb_holsttl_1984]: https://ntrs.nasa.gov/citations/19840019650
[research_cosenza_kummeth_1974]: https://doi.org/10.2514/6.1974-620
[research_cottrell_lijewski_1987]: https://doi.org/10.2514/6.1987-2480
[research_cottrell_martinez_1987]: https://doi.org/10.2514/6.1987-519
[research_couch_1972]: https://doi.org/10.2514/6.1972-1008
[research_coulton]: https://doi.org/10.1109/iciasf.1989.77657
[research_coustols_prudhomme_1995]: https://doi.org/10.2514/3.46862
[research_coustols_seraudie_1997]: https://doi.org/10.2514/2.2175
[research_covert_haldeman_1978]: https://doi.org/10.21236/ada053758
[research_cowling_highspeed_1942]: https://ntrs.nasa.gov/citations/19930091823
[research_cox_jackson_1997]: https://doi.org/10.2514/6.1997-3654
[research_crabillnormanl_1956]: https://ntrs.nasa.gov/citations/20050030066
[research_crafton_elliott_2004]: https://doi.org/10.21236/ada426476
[research_crain_brown_1965]: https://doi.org/10.21236/ad0470147
[research_cramer_2001]: https://doi.org/10.2514/6.2001-2751
[research_cramer_tarkenton_1992]: https://doi.org/10.1063/1.858405
[research_craneharoldl_1948]: https://ntrs.nasa.gov/citations/19930085546
[research_craneharoldl_1948_b]: https://ntrs.nasa.gov/citations/20050028619
[research_craneharoldl_beckhardtarnoldr_1948]: https://ntrs.nasa.gov/citations/20050031072
[research_craneharoldl_sommerrobertw_1961]: https://ntrs.nasa.gov/citations/19980227996
[research_crassidis_2005]: https://doi.org/10.2514/6.2005-5919
[research_crisalli_stahara_1979]: https://doi.org/10.21236/ada082005
[research_cristian_vasile_2010]: https://doi.org/10.13111/2066-8201.2010.2.2.13
[research_crites_rueger_1992]: https://doi.org/10.2514/6.1992-3983
[research_crouch_ahrabi_2024]: https://doi.org/10.1017/jfm.2024.499
[research_crouch_garbaruk_2008]: https://doi.org/10.2514/6.2008-4233
[research_crouch_garbaruk_2009]: https://doi.org/10.1017/s0022112009006673
[research_crouch_garbaruk_2018]: https://doi.org/10.2514/6.2018-3229
[research_crouch_garbaruk_2019]: https://doi.org/10.1017/jfm.2019.748
[research_crowder_2018]: https://doi.org/10.1201/9780203752876-27
[research_crowder_amiryants_1998]: https://doi.org/10.2514/6.1998-2872
[research_crown_1950]: https://doi.org/10.21236/ad0062509
[research_crozier_chargy_2014]: https://doi.org/10.2514/6.2014-2108
[research_cui_yue_2022]: https://doi.org/10.1109/ccdc55256.2022.10034405
[research_cumming_lowe_1971]: https://doi.org/10.2514/6.1971-292
[research_cummingstephenb_smithmarks_2016]: https://ntrs.nasa.gov/citations/20160007775
[research_cunningham_1994]: https://doi.org/10.1115/imece1994-1440
[research_cunninghamamjr_1974]: https://ntrs.nasa.gov/citations/19750028543
[research_cunninghamherbertj_bennettrobertm_1989]: https://ntrs.nasa.gov/citations/19890009886
[research_cunninghamjr_denboer_1992]: https://doi.org/10.2514/6.1992-2125
[research_cunninghamjr_plentovich_1987]: https://doi.org/10.2514/6.1987-2553
[research_cuppoletti_saucier_2016]: https://doi.org/10.2514/6.2016-4763
[research_curley_1991]: https://doi.org/10.1108/eb037169
[research_currao_2024]: https://doi.org/10.1017/jfm.2024.238
[research_currao_he_2024]: https://doi.org/10.2514/1.j063735
[research_currao_jiang_2026]: https://doi.org/10.1017/flo.2026.10056
[research_currao_yeh_2026]: https://doi.org/10.2139/ssrn.6450319
[research_curry_sim_1982]: https://doi.org/10.2514/6.1982-1329
[research_curryre_simag_1984]: https://ntrs.nasa.gov/citations/19870000670
[research_curtinmm_boguedr_2002]: https://ntrs.nasa.gov/citations/20030003815
[research_czerwinska_doerffer_2001]: https://doi.org/10.1115/imece2001/fed-24928
[research_czysz_1963]: https://doi.org/10.21236/ad0407689
[research_d558_handling_1954]: https://ntrs.nasa.gov/citations/19930088510
[research_d558_slat_1953]: https://ntrs.nasa.gov/citations/19930087819
[research_d558_stores_1957]: https://ntrs.nasa.gov/citations/19930090294
[research_d_supersonic_1954]: https://doi.org/10.1515/9781400877553-006
[research_dafiero_2025]: https://doi.org/10.1063/5.0266901
[research_daguanno_campspons_2022]: https://doi.org/10.2514/6.2022-1807
[research_daguanno_schrijer_2021]: https://doi.org/10.2514/6.2021-2558
[research_daguanno_schrijer_2021_b]: https://doi.org/10.1063/5.0062729
[research_daguanno_schrijer_2021_c]: https://doi.org/10.1007/s00348-021-03319-z
[research_dahlentheodoree_1953]: https://ntrs.nasa.gov/citations/19930089125
[research_dahlke_1969]: https://doi.org/10.21236/ad0871323
[research_dai_zhang_2023]: https://doi.org/10.3390/aerospace10060553
[research_daleybernardn_humphreysmiltond_1947]: https://ntrs.nasa.gov/citations/20050071700
[research_damstrom_mayes_1970]: https://doi.org/10.2514/6.1970-341
[research_damstrom_mayes_1971]: https://doi.org/10.2514/3.44266
[research_danberg_heavey_1985]: https://doi.org/10.21236/ada159017
[research_danberg_tschirschnitz_1983]: https://doi.org/10.2514/6.1983-545
[research_dandois_2016]: https://doi.org/10.1063/1.4937426
[research_dandois_mary_2018]: https://doi.org/10.1017/jfm.2018.470
[research_dang_yang_2010]: https://doi.org/10.2514/6.2010-3051
[research_dang_zhao_2019]: https://doi.org/10.3390/app9194132
[research_dannenbergre_gambuccibj_1960]: https://ntrs.nasa.gov/citations/19660024025
[research_dargel_1997]: https://doi.org/10.1007/978-3-322-90711-0_14
[research_dargel_thiede_1987]: https://doi.org/10.2514/6.1987-412
[research_das_carrese_2020]: https://doi.org/10.2514/6.2020-1988
[research_das_cohen_2017]: https://doi.org/10.2514/1.j055895
[research_das_kim_2016]: https://doi.org/10.2514/1.b35840
[research_das_marzocca_2022]: https://doi.org/10.2514/6.2022-1956
[research_daumfredl_zalovcikjohna_1946]: https://ntrs.nasa.gov/citations/19930092751
[research_david_hale_1978]: https://doi.org/10.21236/ada065822
[research_davidjfriedlander_nicholasjgeorgiadis]: https://ntrs.nasa.gov/citations/20240014430
[research_davies_2020]: https://doi.org/10.1201/9780429261152-11
[research_davies_2020_b]: https://doi.org/10.1201/9780429261152-8
[research_davies_2020_c]: https://doi.org/10.1201/9780429261152-9
[research_davies_2025]: https://doi.org/10.1201/9781032692883-10
[research_davies_2025_b]: https://doi.org/10.1201/9781032692883-12
[research_davies_2025_c]: https://doi.org/10.1201/9781032692883-9
[research_davis_2015]: https://doi.org/10.1115/ajkfluids2015-6342
[research_davis_2019]: https://doi.org/10.2514/6.2019-3094
[research_davis_bendiksen_1993]: https://doi.org/10.2514/6.1993-1476
[research_davis_malcolm_1980]: https://doi.org/10.2514/3.50886
[research_davisddjr_wornomde_1958]: https://ntrs.nasa.gov/citations/19630002658
[research_davisdo_willisbp_1998]: https://ntrs.nasa.gov/citations/19980201099
[research_davisjr_1985]: https://doi.org/10.2514/6.1985-425
[research_davisoh_mitchellga_1960]: https://ntrs.nasa.gov/citations/19630006260
[research_davison_1963]: https://doi.org/10.2514/6.1963-1802
[research_davisss_malcolmgn_1979]: https://ntrs.nasa.gov/citations/19790045009
[research_deangelis_1981]: https://doi.org/10.2514/6.1981-2450
[research_debiasi_yan_2010]: https://doi.org/10.2514/6.2010-4244
[research_debonis_georgiadis_1995]: https://doi.org/10.2514/6.1995-2614
[research_deck_2004]: https://doi.org/10.2514/6.2004-5378
[research_deck_2005]: https://doi.org/10.2514/1.9885
[research_decker_miller_2019]: https://doi.org/10.2514/6.2019-0278
[research_deckert_1981]: https://doi.org/10.2514/6.1981-1796
[research_deepa_gupta_2023]: https://doi.org/10.61653/joast.v65i2.2013.727
[research_deere_luckring_2016]: https://doi.org/10.2514/6.2016-0266
[research_deese_agarwal_1987]: https://doi.org/10.2514/6.1987-1200
[research_deese_agarwal_1988]: https://doi.org/10.2514/3.45709
[research_defariamello_sankar_1999]: https://doi.org/10.1002/(sici)1097-0363(19990315)29:5<575::aid-fld801>3.0.co;2-2
[research_degregori_kim_2021]: https://doi.org/10.1063/5.0036821
[research_degrez_ginoux_1987]: https://doi.org/10.21236/ada187334
[research_degrez_vandromme_1986]: https://doi.org/10.1007/978-3-642-82770-9_5
[research_dehghanmanshadi_rabani_2016]: https://doi.org/10.1007/s10409-016-0586-y
[research_deiler_sachs_2026]: https://doi.org/10.2514/6.2026-2087
[research_deiwert_1974]: https://doi.org/10.2514/6.1974-603
[research_deiwert_1975]: https://doi.org/10.2514/3.60547
[research_deiwertgs_1975]: https://ntrs.nasa.gov/citations/19750058122
[research_deiwertgs_baileyhe_1979]: https://ntrs.nasa.gov/citations/19790011867
[research_deiwertgs_mcdevittjb_1975]: https://ntrs.nasa.gov/citations/19760002933
[research_deleo_hagen_1963]: https://doi.org/10.21236/ad0427231
[research_delery_1981]: https://doi.org/10.2514/6.1981-1245
[research_delery_1989]: https://doi.org/10.1007/978-3-642-83584-1_29
[research_deloach_2012]: https://doi.org/10.2514/6.2012-3174
[research_deloach_2014]: https://doi.org/10.2514/6.2014-0097
[research_demattos_wagner_1994]: https://doi.org/10.2514/6.1994-1897
[research_demelo_bussamra_2024]: https://doi.org/10.21203/rs.3.rs-3761279/v1
[research_demeritte_gauzza_1958]: https://doi.org/10.21236/ad0491185
[research_demeritte_gauzza_1958_b]: https://doi.org/10.21236/ad0491184
[research_demetriades_1977]: https://doi.org/10.21236/ada049535
[research_demetriades_1985]: https://doi.org/10.21236/ada179580
[research_denegri_dubben_2005]: https://doi.org/10.2514/6.2005-2296
[research_deng_qin_2021]: https://doi.org/10.2514/1.j060528
[research_deng_zhang_2023]: https://doi.org/10.3390/aerospace10060537
[research_denham_owens_2016]: https://doi.org/10.2514/6.2016-3105
[research_denisonmarie_garaianirban_2019]: https://ntrs.nasa.gov/citations/20190027028
[research_derajat_hariowibowo_2018]: https://doi.org/10.1088/1742-6596/1005/1/012028
[research_deroo_takahashi_2024]: https://doi.org/10.2514/6.2024-2214
[research_desai_viswanathan_1977]: https://doi.org/10.2514/3.44585
[research_deshpande_poggie_2020]: https://doi.org/10.2514/6.2020-0581
[research_design_and]: https://doi.org/10.4271/arp920a
[research_design_and_2024]: https://doi.org/10.52783/jisem.v9i4.74
[research_despirito_2008]: https://doi.org/10.2514/6.2008-427
[research_despirito_2009]: https://doi.org/10.21236/ada508090
[research_destarac_vandervooren_2004]: https://doi.org/10.1016/j.ast.2004.03.004
[research_devan_1987]: https://doi.org/10.2514/6.1987-2296
[research_devan_kania_1985]: https://doi.org/10.2514/6.1985-1810
[research_devanna_2025]: https://doi.org/10.1063/5.0278759
[research_deveikiswd_1983]: https://ntrs.nasa.gov/citations/19830020107
[research_dewart_jr_1958]: https://doi.org/10.21236/ad0155543
[research_dhurandhar_sharma_2026]: https://doi.org/10.1063/5.0310616
[research_dias_2023]: https://doi.org/10.2514/6.2023-0982
[research_dias_budisic_2023]: https://doi.org/10.31224/3001
[research_dicarlo_brown_1992]: https://doi.org/10.2514/6.1992-4094
[research_dick_1955]: https://doi.org/10.21236/ad0079957
[research_dickeyrobertr_1959]: https://ntrs.nasa.gov/citations/19980231999
[research_dickinson_babinsky_2024]: https://doi.org/10.2514/6.2024-2845
[research_diesperov_ryzhov_1971]: https://doi.org/10.1016/0041-5553(71)90113-3
[research_dietrich_kromer_1984]: https://doi.org/10.2514/3.44991
[research_dietz_2005]: https://doi.org/10.2514/1.11881
[research_dietz_schewe_2004]: https://doi.org/10.1016/j.jfluidstructs.2003.07.019
[research_dietz_schewe_2005]: https://doi.org/10.1142/9789812703439_0003
[research_difabbio_tangermann_2022]: https://doi.org/10.2514/6.2022-1204
[research_difioredossantos_lewis_2000]: https://doi.org/10.4271/2000-01-3251
[research_diggins_1951]: https://doi.org/10.21236/ad0895227
[research_dimitriadis_2025]: https://doi.org/10.2514/6.2025-0874
[research_ding_han_2023]: https://doi.org/10.2514/1.j062410
[research_dipasquale_2024]: https://doi.org/10.2514/6.2024-2723
[research_dipasquale_prince_2023]: https://doi.org/10.3390/aerospace10060569
[research_dippold_zaman_2015]: https://doi.org/10.2514/6.2015-0734
[research_dittmar_1989]: https://doi.org/10.2514/6.1989-1059
[research_dive_testing_2003]: https://doi.org/10.2514/5.9781600861840.0417.0426
[research_dix_mattasits_1980]: https://doi.org/10.21236/ada087237
[research_dixon_hunsaker_2023]: https://doi.org/10.2514/6.2023-1512
[research_djayapertapa_allen_2000]: https://doi.org/10.2514/6.2000-4226
[research_djayapertapa_allen_2002]: https://doi.org/10.2514/6.2002-2713
[research_djayapertapa_allen_2004]: https://doi.org/10.1108/09615530410532231
[research_djojodihardjo_2023]: https://doi.org/10.1007/978-981-16-8078-6_26
[research_djomehrimjahed_buningpieterg_1995]: https://ntrs.nasa.gov/citations/20020005120
[research_dlbirdsall_1970]: https://doi.org/10.1017/s0001924000114812
[research_dobbssk_hodsonch_1979]: https://ntrs.nasa.gov/citations/19790017255
[research_dodbele_vandam_1986]: https://doi.org/10.2514/6.1986-316
[research_dodsjr_hanly_1972]: https://doi.org/10.2514/6.1972-1004
[research_dodson_2005]: https://doi.org/10.21236/ada437187
[research_doerffer_telega_2013]: https://doi.org/10.1007/s11630-013-0656-4
[research_doggettrobertvjr_soistmanndavidl_1989]: https://ntrs.nasa.gov/citations/19900004889
[research_doggettrvjr_cunninghamhj_1976]: https://ntrs.nasa.gov/citations/19770013564
[research_doggettrvjr_morganhg_1959]: https://ntrs.nasa.gov/citations/19660024036
[research_doherty_2017]: https://doi.org/10.2514/6.2017-3056
[research_doherty_wang_2018]: https://doi.org/10.2514/6.2018-3953
[research_doig_bogdan_2013]: https://doi.org/10.2514/6.2013-642
[research_dolling_1986]: https://doi.org/10.1007/978-3-642-82770-9_27
[research_dolling_1988]: https://doi.org/10.2514/6.1988-305
[research_dolling_1993]: https://doi.org/10.2514/6.1993-284
[research_dolling_2000]: https://doi.org/10.2514/6.2000-2596
[research_dolling_bogdonoff_1980]: https://doi.org/10.21236/ada084768
[research_dolling_brusniak_1987]: https://doi.org/10.2514/6.1987-1368
[research_dolling_clemens_2003]: https://doi.org/10.21236/ada414559
[research_dolling_clemens_2003_b]: https://doi.org/10.21236/ada411523
[research_dollingdavids_barterjohnw_1995]: https://ntrs.nasa.gov/citations/19960009427
[research_dollingds_1993]: https://ntrs.nasa.gov/citations/19940010727
[research_domingos_ribeiro_2024]: https://doi.org/10.2514/6.2024-4561
[research_donaldsoncolemandup_1944]: https://ntrs.nasa.gov/citations/20140002003
[research_dondurston]: https://ntrs.nasa.gov/citations/20220009235
[research_dondurston_b]: https://ntrs.nasa.gov/citations/20230002822
[research_donegan_1984]: https://doi.org/10.21236/ada143764
[research_donlan_collected_1976]: https://ntrs.nasa.gov/citations/19770022115
[research_donovan_takahashi_2010]: https://doi.org/10.2514/6.2010-9025
[research_dor_mignosi_1989]: https://doi.org/10.1007/978-3-642-83584-1_34
[research_doria_southjr_1982]: https://doi.org/10.2514/6.1982-223
[research_dorschrobertg_brunrinaldoj_1953]: https://ntrs.nasa.gov/citations/19810068687
[research_dou_khoo_2006]: https://doi.org/10.1007/s00193-006-0044-z
[research_dougherty_2021]: https://doi.org/10.2514/6.2021-1875
[research_dougherty_ns_1975]: https://doi.org/10.21236/ada013728
[research_dougherty_ns_1977]: https://doi.org/10.21236/ada045347
[research_doughertyjr_fisher_1980]: https://doi.org/10.2514/6.1980-154
[research_doughertyjr_steinlejr_1974]: https://doi.org/10.2514/6.1974-627
[research_dowell_1986]: https://doi.org/10.1007/978-1-4612-4972-6_2
[research_dowell_bliss_1978]: https://doi.org/10.21236/ada055735
[research_dowell_hall_2003]: https://doi.org/10.21236/ada426408
[research_dowell_ilgamov_1988]: https://doi.org/10.1007/978-1-4612-3908-6_7
[research_dowell_thomas_2001]: https://doi.org/10.2514/6.2001-1212
[research_dowell_williams_1981]: https://doi.org/10.2514/6.1981-643
[research_drag_polar_2021]: https://doi.org/10.1002/9781118949818.ch7
[research_drag_rise_notches_1971]: https://ntrs.nasa.gov/citations/19710050864
[research_drag_rise_reduction_1954]: https://ntrs.nasa.gov/citations/19930093744
[research_dragos_2003]: https://doi.org/10.1007/978-94-015-1248-0_9
[research_drakehubertm_mckayjohnb_1953]: https://ntrs.nasa.gov/citations/19930087560
[research_draper_moran_1973]: https://doi.org/10.21236/ad0755840
[research_drela_1991]: https://doi.org/10.2514/6.1991-3337
[research_drela_1992]: https://doi.org/10.2514/3.46292
[research_drela_2022]: https://doi.org/10.2514/6.2022-1531
[research_drela_giles_1986]: https://doi.org/10.2514/6.1986-1786
[research_drelamark_1992]: https://ntrs.nasa.gov/citations/19920018315
[research_dress_1988]: https://doi.org/10.2514/6.1988-2010
[research_dress_1989]: https://doi.org/10.2514/3.10224
[research_dreze_dimare_2024]: https://doi.org/10.2139/ssrn.4962305
[research_drikakis_durst_1994]: https://doi.org/10.1002/fld.1650180405
[research_driver_1974]: https://doi.org/10.2514/6.1974-987
[research_du_guo_2025]: https://doi.org/10.1063/5.0251573
[research_du_yu_2026]: https://doi.org/10.3390/aerospace13040361
[research_duan_wan_2026]: https://doi.org/10.3390/aerospace13010096
[research_dudley_torres_2007]: https://doi.org/10.2514/6.2007-72
[research_duffy_1989]: https://doi.org/10.2514/6.1989-3383
[research_dugundji_1965]: https://doi.org/10.21236/ad0624995
[research_dugundji_dowell_1962]: https://doi.org/10.21236/ad0278235
[research_dunagan]: https://doi.org/10.32469/10355/98343
[research_dunaganstephene_brownjamesl_1986]: https://ntrs.nasa.gov/citations/19880003924
[research_duncan_1950]: https://doi.org/10.1017/s0001925900000378
[research_dunningrw_1959]: https://ntrs.nasa.gov/citations/19650003092
[research_dupont_debieve_2011]: https://doi.org/10.1017/cbo9780511842757.009
[research_dupuis_1988]: https://doi.org/10.2514/6.1988-4378
[research_dupuis_2002]: https://doi.org/10.2514/6.2002-4414
[research_duraisamy_mccroskey_2006]: https://doi.org/10.2514/6.2006-2993
[research_duran_2026]: https://doi.org/10.2514/6.2026-2637
[research_durham_bolling_1996]: https://doi.org/10.2514/6.1996-3410
[research_durmus_2021]: https://doi.org/10.1108/aeat-02-2021-0038
[research_dutton_addy_1980]: https://doi.org/10.21236/ada084787
[research_dvorak_1965]: https://doi.org/10.1016/b978-0-08-011860-4.50007-0
[research_dvorak_choi_1982]: https://doi.org/10.21236/ada112146
[research_dvorak_kosiak_1947]: https://doi.org/10.21236/adb812169
[research_dykas_szymanski_2017]: https://doi.org/10.1007/s11630-017-0932-9
[research_eades_jr_1964]: https://doi.org/10.21236/ad0352807
[research_eastep_andersen_1998]: https://doi.org/10.2514/6.1998-4932
[research_eastep_andersen_2001]: https://doi.org/10.2514/2.2842
[research_eastep_olsen_1979]: https://doi.org/10.2514/6.1979-1632
[research_eastep_olsen_1980]: https://doi.org/10.2514/3.50866
[research_eberle_1981]: https://doi.org/10.1007/978-3-663-14008-5_8
[research_ecer_1985]: https://doi.org/10.21236/ada162168
[research_ecer_1989]: https://doi.org/10.21236/ada212851
[research_eckhaus_1962]: https://doi.org/10.2514/8.9589
[research_edelmann_roberts_2009]: https://doi.org/10.1007/978-3-540-85181-3_82
[research_edwards_2007]: https://doi.org/10.21236/ada482276
[research_edwards_2008]: https://doi.org/10.2514/1.30082
[research_edwards_2009]: https://doi.org/10.2514/1.30080
[research_edwards_bennett_1982]: https://doi.org/10.2514/6.1982-685
[research_edwards_carter_1985]: https://doi.org/10.2514/6.1985-371
[research_edwards_carter_1986]: https://doi.org/10.2514/3.9345
[research_edwards_schuster_2001]: https://doi.org/10.2514/6.2001-1291
[research_edwards_spain_2009]: https://doi.org/10.2514/1.30079
[research_edwards_whitfield_1986]: https://doi.org/10.1007/978-3-642-82770-9_7
[research_edwardsjohnw_1996]: https://ntrs.nasa.gov/citations/19960054470
[research_edwardsjohnw_1997]: https://ntrs.nasa.gov/citations/20040100770
[research_effect_of_1990]: https://doi.org/10.2514/6.1990-2838
[research_efrati_raveh_2026]: https://doi.org/10.2514/6.2026-0804
[research_eghlima_mansour_2017]: https://doi.org/10.1016/j.actaastro.2017.01.008
[research_egorov_2025]: https://doi.org/10.7868/s3034508125030077
[research_ekaterinaris_2010]: https://doi.org/10.2514/1.45526
[research_elbanna_carlson_1989]: https://doi.org/10.2514/6.1989-532
[research_eldern_vos]: https://doi.org/10.1007/3-540-56394-6_259
[research_eldredge_wang_2009]: https://doi.org/10.2514/6.2009-3687
[research_eldridgeallegra_roseman_2024]: https://doi.org/10.2514/6.2024-1945
[research_eldridgeallegra_xu_2023]: https://doi.org/10.2514/6.2023-1426
[research_electronic_autopilot_1956]: https://doi.org/10.1109/ee.1956.6441922
[research_elham_timmer_2016]: https://doi.org/10.2514/6.2016-0160
[research_eliasson_peng_2007]: https://doi.org/10.2514/6.2007-897
[research_eliasson_peng_2008]: https://doi.org/10.2514/1.31252
[research_ellinwood_1967]: https://doi.org/10.2514/3.4083
[research_ellison_latz_2003]: https://doi.org/10.2514/6.2003-5319
[research_elnaggar_klamo_2004]: https://doi.org/10.2514/1.3416
[research_elramly]: https://doi.org/10.22215/etd/1975-00290
[research_elsayed_2016]: https://doi.org/10.1007/978-1-4471-6796-9
[research_eminton_lord_1956]: https://doi.org/10.1017/s0368393100132407
[research_enciu_2019]: https://doi.org/10.7763/ijmo.2019.v9.729
[research_energy_approach_2003]: https://doi.org/10.2514/5.9781600861840.0143.0151
[research_engelbrecht]: https://doi.org/10.31274/rtd-180813-14663
[research_englar_1970]: https://doi.org/10.21236/ad0882075
[research_englishrolandd_1955]: https://ntrs.nasa.gov/citations/19930088612
[research_eppink_2023]: https://doi.org/10.2514/6.2023-3999
[research_eppler_2003]: https://doi.org/10.1016/s1270-9638(03)00029-4
[research_epstein_1954]: https://doi.org/10.21236/ad0037709
[research_epstein_albers_1948]: https://doi.org/10.2514/8.11529
[research_epstein_luntz_1989]: https://doi.org/10.2514/3.45835
[research_erickson_1962]: https://doi.org/10.2514/8.9884
[research_erickson_hall_1989]: https://doi.org/10.2514/6.1989-2222
[research_erickson_rogers_1987]: https://doi.org/10.2514/6.1987-1262
[research_erickson_schreiner_1989]: https://doi.org/10.2514/6.1989-3345
[research_erickson_schreiner_1990]: https://doi.org/10.2514/6.1990-3023
[research_erickson_schreiner_1990_b]: https://doi.org/10.2514/6.1990-2814
[research_ericksongarye_1991]: https://ntrs.nasa.gov/citations/19920005750
[research_ericksongarye_gonzalezhugoa_2004]: https://ntrs.nasa.gov/citations/20050060675
[research_ericksongarye_gonzalezhugoa_2005]: https://ntrs.nasa.gov/citations/20050050949
[research_ericksonll_1974]: https://ntrs.nasa.gov/citations/19740006518
[research_ericsson_1973]: https://doi.org/10.2514/6.1973-308
[research_ericsson_1975]: https://doi.org/10.2514/3.59805
[research_ericsson_1986]: https://doi.org/10.2514/6.1986-1773
[research_ericsson_1989]: https://doi.org/10.2514/3.10315
[research_ericsson_1997]: https://doi.org/10.2514/2.2233
[research_ericssonle_1970]: https://ntrs.nasa.gov/citations/19700065747
[research_ertugrul_koyuncu_2023]: https://doi.org/10.2514/6.2023-1344
[research_essawy_1985]: https://doi.org/10.21608/asat.1985.26462
[research_estruchsamper_vanstone_2014]: https://doi.org/10.1007/s00193-014-0514-7
[research_ethansbeyak_meelanchoudhari]: https://ntrs.nasa.gov/citations/20230016659
[research_european_transonic_1990]: https://doi.org/10.1108/eb037033
[research_euvrard_tournemine]: https://doi.org/10.1007/bfb0112688
[research_evaluation_of_1981]: https://doi.org/10.2514/6.1981-606
[research_evangelista_mori_2025]: https://doi.org/10.4050/f-0081-2025-0128
[research_evanjmcfadden_jeffreypbons]: https://ntrs.nasa.gov/citations/20240014861
[research_evans_1987]: https://doi.org/10.2514/6.1987-1355
[research_everhart_1986]: https://doi.org/10.2514/6.1986-749
[research_everhart_1987]: https://doi.org/10.4271/871757
[research_everhart_barnwell_1978]: https://doi.org/10.2514/6.1978-805
[research_everhart_goradia_1988]: https://doi.org/10.2514/6.1988-2029
[research_everhartjl_barnwellrw_1978]: https://ntrs.nasa.gov/citations/19790011819
[research_everhartjoell_1987]: https://ntrs.nasa.gov/citations/19880051548
[research_everhartjoell_bobbittpercyj_1994]: https://ntrs.nasa.gov/citations/19940025042
[research_everhartjoell_goradiasureshh_1991]: https://ntrs.nasa.gov/citations/19920000788
[research_everhartjoellee_1988]: https://ntrs.nasa.gov/citations/19880006433
[research_evers_1999]: https://doi.org/10.2514/6.1999-1972
[research_evers_2001]: https://doi.org/10.2514/2.1298
[research_evers_peake_1998]: https://doi.org/10.2514/6.1998-2320
[research_eversman_1989]: https://doi.org/10.2514/6.1989-1097
[research_experience_gained_2010]: https://doi.org/10.2514/5.9781600867552.0443.0543
[research_experimental_testing_1982]: https://doi.org/10.2514/5.9781600865558.0189.0238
[research_experimental_transonic_1990]: https://doi.org/10.2514/6.1990-979
[research_extension_of_1982]: https://doi.org/10.2514/5.9781600865558.0467.0487
[research_f104_buffet_1972]: https://ntrs.nasa.gov/citations/19720022354
[research_f22_fin_buffet_2000]: https://ntrs.nasa.gov/citations/20000052124
[research_f84g_squadron_1953]: https://ntrs.nasa.gov/citations/20050019469
[research_f86_squadron_1952]: https://ntrs.nasa.gov/citations/20050019265
[research_f8_buffet_1977]: https://ntrs.nasa.gov/citations/19770025136
[research_faberstanley_craneharoldl_1961]: https://ntrs.nasa.gov/citations/20040027953
[research_faberstanley_egglestonjohnm_1953]: https://ntrs.nasa.gov/citations/19930087822
[research_fagbade_heinz_2024]: https://doi.org/10.3390/app14072705
[research_falco_1991]: https://doi.org/10.21236/ada250210
[research_famellos_skevas_2024]: https://doi.org/10.3390/aerospace11050385
[research_fan_2013]: https://doi.org/10.4028/www.scientific.net/amm.0.259
[research_fan_yi_2005]: https://doi.org/10.2514/6.2005-3551
[research_fan_yu_2021]: https://doi.org/10.2514/1.c036138
[research_fanning_mueller_1978]: https://doi.org/10.2514/6.1978-206
[research_farbridge_smith_1977]: https://doi.org/10.2514/6.1977-606
[research_farbridge_smith_1978]: https://doi.org/10.2514/3.58443
[research_farhangnia_guruswamy_1996]: https://doi.org/10.2514/6.1996-286
[research_farhat_1998]: https://doi.org/10.21236/ada361695
[research_farhat_2000]: https://doi.org/10.21236/ada389378
[research_farhat_2001]: https://doi.org/10.21236/ada387498
[research_farrokhfal_pishevar_2014]: https://doi.org/10.5028/jatm.v6i4.403
[research_farsadi_asadi_2019]: https://doi.org/10.1016/j.ast.2019.105353
[research_fauci_imperatore]: https://doi.org/10.1109/iciasf.2001.960279
[research_fauci_nicoli_2006]: https://doi.org/10.2514/6.2006-3638
[research_fay_riddell_1958]: https://doi.org/10.2514/8.7517
[research_fediaevsky_1935]: https://doi.org/10.2514/8.114
[research_fedorov_malmuth_1997]: https://doi.org/10.2514/6.1997-2231
[research_fehrs_helm_2025]: https://doi.org/10.2514/6.2025-1714
[research_fei_wang_2026]: https://doi.org/10.1145/3817124.3817365
[research_fejtek_1994]: https://doi.org/10.2514/6.1994-2604
[research_feldhusenhoffmann_statnikov_2017]: https://doi.org/10.1007/s00348-017-2466-z
[research_feng_2023]: https://doi.org/10.54097/br1qsb29
[research_fenwick_allen_2007]: https://doi.org/10.2514/6.2007-3805
[research_ferman_turner_1999]: https://doi.org/10.21236/ada416808
[research_ferman_turner_1999_b]: https://doi.org/10.21236/ada377712
[research_fernandez_hoffmann_2018]: https://doi.org/10.2514/6.2018-3376
[research_ferrand_aubert_1994]: https://doi.org/10.2514/6.1994-1876
[research_ferrara_consalvo_2006]: https://doi.org/10.2514/6.2006-5987
[research_ferrari_1962]: https://doi.org/10.1016/b978-0-08-006550-2.50034-x
[research_ferrari_morais_2021]: https://doi.org/10.2514/6.2021-1839
[research_ferri_baronti_1973]: https://doi.org/10.2514/3.6670
[research_ferrisjc_1973]: https://ntrs.nasa.gov/citations/19830002757
[research_ferrisjc_1975]: https://ntrs.nasa.gov/citations/19830002811
[research_fertis_1988]: https://doi.org/10.2514/6.1988-2210
[research_fettermandejr_1959]: https://ntrs.nasa.gov/citations/19650018534
[research_fiber_optic_loads_2018]: https://ntrs.nasa.gov/citations/20190033242
[research_finaish_frigerio_1995]: https://doi.org/10.2514/6.1995-311
[research_finatev_shcherbakov_1968]: https://doi.org/10.1007/bf00828936
[research_fink_1971]: https://doi.org/10.2514/3.59161
[research_firsov_isaenkov_2017]: https://doi.org/10.2514/6.2017-0714
[research_firsov_moralev_2018]: https://doi.org/10.2514/6.2018-2050
[research_fischeljack_1954]: https://ntrs.nasa.gov/citations/19930088041
[research_fischeljack_brunncyrild_1954]: https://ntrs.nasa.gov/citations/19930088333
[research_fischeljack_darvillerobertw_1957]: https://ntrs.nasa.gov/citations/19930090143
[research_fischeljack_reisertdonald_1956]: https://ntrs.nasa.gov/citations/19930090225
[research_fischenberg_1995]: https://doi.org/10.2514/6.1995-3438
[research_fischer_2018]: https://doi.org/10.1007/978-3-658-21379-4_3
[research_fischer_maddalon_1971]: https://doi.org/10.2514/3.6282
[research_fishelov_1988]: https://doi.org/10.1137/0909015
[research_fisher_banks_1990]: https://doi.org/10.2514/6.1990-3018
[research_fisher_cobleigh_1994]: https://doi.org/10.2514/6.1994-1826
[research_fisher_gertsen_1956]: https://doi.org/10.21236/ad0092459
[research_fisherdf_1969]: https://ntrs.nasa.gov/citations/19690028683
[research_fisherdf_1978]: https://ntrs.nasa.gov/citations/19780024121
[research_fisherlewisr_williamsjamesl_1958]: https://ntrs.nasa.gov/citations/19980232008
[research_fitzhugh_1970]: https://doi.org/10.2514/3.44161
[research_fix_1980]: https://doi.org/10.21236/ada084636
[research_flaszynski_2016]: https://doi.org/10.2514/6.2016-3769
[research_flax_1973]: https://doi.org/10.2514/3.50532
[research_flight_loads_prediction_1981]: https://doi.org/10.17226/19736
[research_flint_niewoehner_2011]: https://doi.org/10.2514/1.c031023
[research_flores_holst_1984]: https://doi.org/10.2514/6.1984-300
[research_flores_vandalsem_1985]: https://doi.org/10.2514/6.1985-5004
[research_flores_vandalsem_1986]: https://doi.org/10.2514/3.45390
[research_florio_mckibbin_2019]: https://doi.org/10.21914/anziamj.v59i0.13408
[research_flutter_symposium_1975]: https://ntrs.nasa.gov/citations/19760003007
[research_fontaine_ali_2023]: https://doi.org/10.46254/sa04.20230298
[research_forsey_1983]: https://doi.org/10.2514/6.1983-1805
[research_forster_steijl_2015]: https://doi.org/10.2514/6.2015-1709
[research_fosdick_1970]: https://doi.org/10.21236/ad0880677
[research_fosswejr_swihartjm_1956]: https://ntrs.nasa.gov/citations/19660010447
[research_foster_cunningham_2010]: https://doi.org/10.2514/6.2010-1350
[research_foughnerjtjr_bensingerct_1977]: https://ntrs.nasa.gov/citations/19780003061
[research_fournis_2022]: https://doi.org/10.2514/6.2022-3886
[research_foxchj_woodwardfa_1974]: https://ntrs.nasa.gov/citations/19730000470
[research_fraenkel_1958]: https://doi.org/10.1017/s000192590000130x
[research_fraenkel_1958_b]: https://doi.org/10.1017/s000192590001074x
[research_frances_solerarico_2024]: https://doi.org/10.23967/eccomas.2024.160
[research_franksralphw_1953]: https://ntrs.nasa.gov/citations/19930087386
[research_franzmann_leopold_2022]: https://doi.org/10.3390/aerospace9020051
[research_fraser_1975]: https://doi.org/10.1017/s0001924000034898
[research_freefall_1945]: https://ntrs.nasa.gov/citations/20150021184
[research_freefall_65009_1947]: https://ntrs.nasa.gov/citations/20030063971
[research_freefall_interference_1953]: https://ntrs.nasa.gov/citations/19930087730
[research_freefall_sweptfwd_1947]: https://ntrs.nasa.gov/citations/19930085802
[research_freefall_wingbody_1947]: https://ntrs.nasa.gov/citations/19930085806
[research_freestone_henington_1982]: https://doi.org/10.21236/ada122799
[research_french_1988]: https://doi.org/10.2514/6.1988-4376
[research_french_noll_1987]: https://doi.org/10.2514/6.1987-909
[research_freudingerlawrencec_kehoemichaelw_1990]: https://ntrs.nasa.gov/citations/19900015819
[research_freund_2014]: https://doi.org/10.5162/etc2014/6.3
[research_frew_galassi_1993]: https://doi.org/10.2514/6.1993-2481
[research_friedewald_2020]: https://doi.org/10.3390/aerospace8010007
[research_friehmelt_jost_2000]: https://doi.org/10.2514/6.2000-4191
[research_friendel_sakamotogm_1978]: https://ntrs.nasa.gov/citations/19790004885
[research_fritz_patel_2025]: https://doi.org/10.2514/6.2025-99629
[research_fritz_sackheim_1982]: https://doi.org/10.2514/6.1982-1108
[research_frolov_2015]: https://doi.org/10.4028/www.scientific.net/amm.798.513
[research_fsw_liftdrag_1994]: https://ntrs.nasa.gov/citations/19950012150
[research_fu_1995]: https://doi.org/10.1108/02644409510799758
[research_fu_feng_2026]: https://doi.org/10.1016/j.cja.2026.104092
[research_fu_liang_1991]: https://doi.org/10.2514/6.1991-2260
[research_fu_liang_1993]: https://doi.org/10.2514/6.1993-3416
[research_fu_sun_2023]: https://doi.org/10.2514/1.j061340
[research_fuchs_1981]: https://doi.org/10.1007/978-3-663-14008-5_6
[research_fuehrer_1969]: https://doi.org/10.21236/ad0695562
[research_fugate_nguyen_2019]: https://doi.org/10.2514/6.2019-3028
[research_fuglsang_williams_1985]: https://doi.org/10.2514/6.1985-600
[research_fuhs_1971]: https://doi.org/10.2514/3.44270
[research_fujii]: https://doi.org/10.1007/3-540-10694-4_28
[research_fujii_obayashi_1986]: https://doi.org/10.2514/6.1986-1831
[research_fujii_obayashi_1987]: https://doi.org/10.2514/3.9829
[research_fujino_kawamura_2003]: https://doi.org/10.2514/6.2003-933
[research_fujino_suzuki_2024]: https://doi.org/10.2514/6.2024-4390
[research_fujiwara_chaparro_2016]: https://doi.org/10.2514/6.2016-3568
[research_fukami_higashino_2004]: https://doi.org/10.2514/6.2004-5176
[research_fukumoto_kouchi_2023]: https://doi.org/10.2514/6.2023-1180
[research_fukushima_kawai_2017]: https://doi.org/10.2514/6.2017-0495
[research_fukushima_kawai_2017_b]: https://doi.org/10.1615/tsfp10.1190
[research_fukushima_kawai_2018]: https://doi.org/10.2514/1.j056537
[research_fukushima_kawai_2019]: https://doi.org/10.2514/6.2019-1846
[research_fukushima_tamaki_2020]: https://doi.org/10.2514/6.2020-1982
[research_fulker_ashill_1986]: https://doi.org/10.1007/978-3-642-82770-9_19
[research_fuller_williams_1986]: https://doi.org/10.2514/6.1986-748
[research_fullerde_1982]: https://ntrs.nasa.gov/citations/19820024788
[research_fullerde_glossbb_1981]: https://ntrs.nasa.gov/citations/19810020601
[research_fung_1982]: https://doi.org/10.2514/6.1982-956
[research_fung_1982_b]: https://doi.org/10.21236/ada215096
[research_fung_shieh_1993]: https://doi.org/10.2514/3.11330
[research_furlonggchester_fitzpatrickjamese_1947]: https://ntrs.nasa.gov/citations/19930081927
[research_fuselage_mods_drag_1954]: https://ntrs.nasa.gov/citations/20050028506
[research_fusi_quaranta_2015]: https://doi.org/10.2514/6.2015-1722
[research_fuzaromiotto_wolf_2020]: https://doi.org/10.26678/abcm.encit2020.cit20-0073
[research_g_the_1957]: https://doi.org/10.1515/9781400879908-016
[research_gada_rahai_2016]: https://doi.org/10.1115/imece2016-66177
[research_gada_rahai_2023]: https://doi.org/10.4271/2023-01-0979
[research_gadsden_habibi_2007]: https://doi.org/10.1115/imece2007-41897
[research_gageik_nies_2018]: https://doi.org/10.1016/j.ast.2018.05.011
[research_gahlot_singh_2021]: https://doi.org/10.1002/htj.22329
[research_gallagher_1968]: https://doi.org/10.2514/6.1968-880
[research_gallington_miller_1970]: https://doi.org/10.2514/6.1970-971
[research_gallman_batina_1988]: https://doi.org/10.2514/3.45587
[research_gallman_yang_1986]: https://doi.org/10.2514/6.1986-902
[research_gally_carlson_1987]: https://doi.org/10.2514/6.1987-2551
[research_gallythomasa_1994]: https://ntrs.nasa.gov/citations/19950016874
[research_galyen_mills_2014]: https://doi.org/10.2514/6.2014-1243
[research_gamble_inman_2018]: https://doi.org/10.1117/12.2287471
[research_gambuccibj_sorensonrm_1958]: https://ntrs.nasa.gov/citations/19660024053
[research_ganesh_1994]: https://doi.org/10.1115/imece1994-0647
[research_gangeh_bui_2023]: https://doi.org/10.2514/6.2023-72230
[research_gao_2023]: https://doi.org/10.1109/insai60116.2023.00050
[research_gao_an_2021]: https://doi.org/10.1016/b978-0-12-822990-3.00008-5
[research_gao_luo_2003]: https://doi.org/10.2514/6.2003-1267
[research_gao_qu_2017]: https://doi.org/10.2514/6.2017-3405
[research_gao_qu_2018]: https://doi.org/10.2514/6.2018-1784
[research_gao_tyrrell_2025]: https://doi.org/10.2514/6.2025-2022
[research_gao_zhang_2018]: https://doi.org/10.1016/j.ast.2018.03.047
[research_gao_zhang_2019]: https://doi.org/10.1063/1.5087014
[research_garabedian_1964]: https://doi.org/10.1007/978-3-642-88337-8_8
[research_garabedian_1974]: https://doi.org/10.1016/b978-0-12-044850-0.50020-4
[research_garabedian_1994]: https://doi.org/10.21236/ada292797
[research_garabedianp_mcfaddeng_1982]: https://ntrs.nasa.gov/citations/19820040291
[research_garabedianp_mcfaddeng_1982_b]: https://ntrs.nasa.gov/citations/19830048709
[research_garcia_slingerland_2001]: https://doi.org/10.2514/6.2001-5237
[research_gardenier_1956]: https://doi.org/10.21236/ad0084917
[research_gardner_1978]: https://doi.org/10.54648/aila1978021
[research_gardnerwilliamn_curfmanhowardjjr_1947]: https://ntrs.nasa.gov/citations/19930085706
[research_garnier_adams_2009]: https://doi.org/10.1007/978-90-481-2819-8_8
[research_garnier_deck_2010]: https://doi.org/10.1007/978-3-642-14139-3_16
[research_garrelick_martini_1997]: https://doi.org/10.21236/ada329470
[research_garrell_2002]: https://doi.org/10.2514/6.2002-2790
[research_garrell_nowakowski_2006]: https://doi.org/10.2514/6.2006-3147
[research_garrick_reed_1981]: https://doi.org/10.2514/3.57579
[research_garriz_newman_1990]: https://doi.org/10.2514/6.1990-1433
[research_gartenberg_johnson_1992]: https://doi.org/10.2514/3.10936
[research_gartner_amitay_2015]: https://doi.org/10.2514/6.2015-2484
[research_gartner_amitay_2016]: https://doi.org/10.2514/6.2016-3770
[research_gatesordwaybjr_sternfieldleonard_1950]: https://ntrs.nasa.gov/citations/20050019392
[research_gatski_bonnet_2009]: https://doi.org/10.1016/b978-0-08-044565-6.00007-5
[research_gatski_bonnet_2013]: https://doi.org/10.1016/b978-0-12-397027-5.00002-2
[research_gatski_bonnet_2013_b]: https://doi.org/10.1016/b978-0-12-397027-5.00008-3
[research_gautam_prasad_2025]: https://doi.org/10.2514/6.2025-3775
[research_ge_gan_2026]: https://doi.org/10.2139/ssrn.6796508
[research_gea_chyu_1991]: https://doi.org/10.2514/6.1991-1628
[research_geared_tab_1948]: https://ntrs.nasa.gov/citations/19930082436
[research_gebeleinh_1939]: https://ntrs.nasa.gov/citations/19930094530
[research_gee_jenks_1976]: https://doi.org/10.2514/6.1976-1991
[research_gee_olaveson_2025]: https://doi.org/10.2514/1.j064208
[research_geffen_1978]: https://doi.org/10.21236/ada062066
[research_geib_maidnik_1983]: https://doi.org/10.21236/ada247843
[research_geissler_1997]: https://doi.org/10.1007/978-3-322-90711-0_16
[research_geissler_2003]: https://doi.org/10.1016/s1270-9638(03)00065-8
[research_generalelectriccocincinnatioh_1964]: https://doi.org/10.21236/ad0447839
[research_geoghegan_giannelis_2018]: https://doi.org/10.2514/6.2018-1787
[research_geoghegan_giannelis_2020]: https://doi.org/10.2514/6.2020-1989
[research_geoghegan_giannelis_2020_b]: https://doi.org/10.3390/fluids5020046
[research_georgefalvy_1971]: https://doi.org/10.2514/6.1971-289
[research_georgiadis_wernet_2021]: https://doi.org/10.2514/6.2021-2834
[research_georgiadis_wernet_2024]: https://doi.org/10.2514/1.j063186
[research_georgiadisnicholasj_vyasmanana_2013]: https://ntrs.nasa.gov/citations/20130010178
[research_gera_1986]: https://doi.org/10.2514/6.1986-167
[research_gera_wilson_1981]: https://doi.org/10.2514/6.1981-2505
[research_german_1975]: https://doi.org/10.2514/6.1975-1320
[research_german_development_2010]: https://doi.org/10.2514/4.867552
[research_gerolymos_sauret_2003]: https://doi.org/10.2514/6.2003-3465
[research_gerolymos_vallet_2003]: https://doi.org/10.1007/978-94-010-0017-8_24
[research_gerontakos_lee_2007]: https://doi.org/10.2514/1.27577
[research_ghaffarifarhad_2005]: https://ntrs.nasa.gov/citations/20050198856
[research_ghate_kenway_2021]: https://doi.org/10.2514/6.2021-1439
[research_ghayour_baysal_1999]: https://doi.org/10.2514/6.1999-654
[research_ghazi_1993]: https://doi.org/10.2514/6.1993-3641
[research_ghoreyshi_aref_2024]: https://doi.org/10.2514/6.2024-4158
[research_ghoreyshi_aref_2025]: https://doi.org/10.2514/1.j064753
[research_ghoreyshi_cummings_2013]: https://doi.org/10.2514/1.j052309
[research_ghoreyshi_darragh_2017]: https://doi.org/10.1016/j.ast.2017.06.024
[research_giannelis_murray_2019]: https://doi.org/10.2514/6.2019-1339
[research_giannelis_vio_2016]: https://doi.org/10.2514/6.2016-2028
[research_gibbings_1966]: https://doi.org/10.2514/3.43754
[research_gibbons_1992]: https://doi.org/10.2514/6.1992-2503
[research_gibbons_batina_1989]: https://doi.org/10.2514/6.1989-1283
[research_gibbons_batina_1990]: https://doi.org/10.2514/3.45936
[research_gibsonfw_herrrw_1958]: https://ntrs.nasa.gov/citations/19660030332
[research_giepman_srivastava_2015]: https://doi.org/10.2514/6.2015-2779
[research_giez_mallaun_2016]: https://doi.org/10.2514/6.2016-3707
[research_gilbarg_shiffman_1954]: https://doi.org/10.1512/iumj.1954.3.53010
[research_giles_drela_1986]: https://doi.org/10.2514/6.1986-1793
[research_giles_drela_1987]: https://doi.org/10.2514/3.9768
[research_gill_zhang_2016]: https://doi.org/10.2514/6.2016-2872
[research_gillan_1993]: https://doi.org/10.2514/6.1993-3419
[research_gillan_1995]: https://doi.org/10.2514/3.12644
[research_gillard_1998]: https://doi.org/10.21236/ada362903
[research_gillard_1999]: https://doi.org/10.2514/6.1999-4015
[research_gillespiewarrenjr_1960]: https://ntrs.nasa.gov/citations/20040046997
[research_gillespiewarrenjr_arbicrichardg_1950]: https://ntrs.nasa.gov/citations/20090023625
[research_gillespiewarrenjr_dietzalberte_1952]: https://ntrs.nasa.gov/citations/19930087047
[research_gilliam_1976]: https://doi.org/10.2514/6.1976-215
[research_gilliot_monnier_2004]: https://doi.org/10.1007/978-3-642-18795-7_5
[research_gillisclarencel_mitchelljessel_1957]: https://ntrs.nasa.gov/citations/19930092326
[research_gillisclarencel_peckrobertf_1950]: https://ntrs.nasa.gov/citations/19930086055
[research_gilmanjjr_1961]: https://ntrs.nasa.gov/citations/19670022808
[research_gilyard_orme_1992]: https://doi.org/10.2514/6.1992-3743
[research_glagolev_zubkov_2000]: https://doi.org/10.1007/bf02699473
[research_glaser_1952]: https://doi.org/10.1088/0950-7671/29/7/306
[research_glauert_1928]: https://doi.org/10.1098/rspa.1928.0039
[research_glauert_1983]: https://doi.org/10.1017/cbo9780511574481
[research_glazkov_gorbushin_2016]: https://doi.org/10.1063/1.4963950
[research_glazkov_semenov_2024]: https://doi.org/10.53954/9785604990148_62
[research_glezer_2009]: https://doi.org/10.21236/ada584974
[research_glezer_2012]: https://doi.org/10.21236/ada564711
[research_gloss_1984]: https://doi.org/10.2514/6.1984-585
[research_gloss_1992]: https://doi.org/10.2514/6.1992-156
[research_gloss_washburn_1977]: https://doi.org/10.2514/6.1977-1132
[research_gloss_washburn_1978]: https://doi.org/10.2514/3.58347
[research_glowacki_1971]: https://doi.org/10.21236/ad0727591
[research_goal_sun_2012]: https://doi.org/10.2514/6.2012-3980
[research_goates_vandommelen_2025]: https://doi.org/10.2514/6.2025-1752
[research_goc_agrawal_2023]: https://doi.org/10.2514/6.2023-4338
[research_goc_agrawal_2025]: https://doi.org/10.2514/1.c038129
[research_godavarthi_seo_2026]: https://doi.org/10.2514/6.2026-2313
[research_godwin_frazier_1964]: https://doi.org/10.21236/ad0613504
[research_goenka_1994]: https://doi.org/10.2514/6.1994-2509
[research_goethert_1956]: https://doi.org/10.21236/ad0084159
[research_goethert_lukasiewicz_1963]: https://doi.org/10.1115/1.3630090
[research_goetzrc_1972]: https://ntrs.nasa.gov/citations/19720023216
[research_goetzrc_stonesiferjc_1961]: https://ntrs.nasa.gov/citations/19660022440
[research_goffert_ortega_2014]: https://doi.org/10.1111/ext.12085
[research_goffert_ortega_2015]: https://doi.org/10.5028/jatm.v7i1.417
[research_goffert_ortega_2016]: https://doi.org/10.1007/s40799-016-0049-1
[research_goh_2008]: https://doi.org/10.1109/ccdc.2008.4597574
[research_goland_luke_1954]: https://doi.org/10.21236/ad0050212
[research_goldberg_gorski_1985]: https://doi.org/10.2514/6.1985-4081
[research_goldbergu_reshotkoe_1980]: https://ntrs.nasa.gov/citations/19800012047
[research_goldhammermarki_steinlefrankwjr_1990]: https://ntrs.nasa.gov/citations/19910039785
[research_goldstein_2004]: https://doi.org/10.21236/ada430475
[research_golestani_soltani_2017]: https://doi.org/10.24200/sci.2017.4089
[research_golubev_hollenshade_2010]: https://doi.org/10.2514/6.2010-4868
[research_gompertz_jensen_2012]: https://doi.org/10.4050/vfs-f68-000098
[research_goncalves_robinet_2003]: https://doi.org/10.1615/tsfp3.1910
[research_gong_gao_2024]: https://doi.org/10.3390/aerospace11020121
[research_gong_wang_2024]: https://doi.org/10.1063/5.0232492
[research_gong_zhang_2025]: https://doi.org/10.2514/1.j064330
[research_gonsalez_dolling_1993]: https://doi.org/10.2514/6.1993-776
[research_gonzalez_ilie_2026]: https://doi.org/10.2514/6.2026-0866
[research_goodheart_dykas_2003]: https://doi.org/10.1002/pamm.200310171
[research_goodman_1973]: https://doi.org/10.2514/3.60287
[research_goodmanwl_morrisetteel_1985]: https://ntrs.nasa.gov/citations/19850045726
[research_goodrich_derry_1983]: https://doi.org/10.2514/6.1983-485
[research_goodrich_sliwa_1987]: https://doi.org/10.2514/6.1987-2590
[research_goodwinfk_lynesll_1967]: https://ntrs.nasa.gov/citations/19700022323
[research_goodyearaerospacecorpakronoh_1958]: https://doi.org/10.21236/ad0215773
[research_goodyer_wolf_1980]: https://doi.org/10.2514/6.1980-440
[research_goorjian_1984]: https://doi.org/10.2514/6.1984-91
[research_goorjian_buskirk_1985]: https://doi.org/10.2514/3.9153
[research_goorjian_meagher_1983]: https://doi.org/10.2514/6.1983-371
[research_goorjianpeterm_obayashishigeru_1989]: https://ntrs.nasa.gov/citations/19900009885
[research_goorjianpeterm_obayashishigeru_1990]: https://ntrs.nasa.gov/citations/19910049569
[research_gopalarathnam_mcavoy_2001]: https://doi.org/10.2514/6.2001-2409
[research_gopeshmp_manivelm_2016]: https://doi.org/10.17577/ijertv5is050411
[research_goradiash_bobbittpj_1988]: https://ntrs.nasa.gov/citations/19890040858
[research_goradiash_bobbittpj_1989]: https://ntrs.nasa.gov/citations/19910014825
[research_gordnier_melville_1998]: https://doi.org/10.2514/6.1998-1729
[research_gordnier_melville_2000]: https://doi.org/10.2514/2.2683
[research_gorski_1998]: https://doi.org/10.21236/ada360504
[research_goupil]: https://doi.org/10.15368/theses.2020.10
[research_goushcha_sekula_2025]: https://doi.org/10.2514/6.2025-1124
[research_graham_lagerstrom_1954]: https://doi.org/10.21236/ad0063453
[research_grahamdavid_koenigdavidg_1951]: https://ntrs.nasa.gov/citations/19930086542
[research_grahamdavid_koenigdavidg_1952]: https://ntrs.nasa.gov/citations/19930087959
[research_grahamdonaldj_1947]: https://ntrs.nasa.gov/citations/19930082040
[research_grahamdonaldj_1948]: https://ntrs.nasa.gov/citations/19930082444
[research_grahamdonaldj_1949]: https://ntrs.nasa.gov/citations/19930092012
[research_grahamdonaldj_nitzberggeralde_1945]: https://ntrs.nasa.gov/citations/19930091909
[research_gramann_dolling_1987]: https://doi.org/10.2514/3.9823
[research_grantfrederickc_robinsonrossb_1953]: https://ntrs.nasa.gov/citations/19930089137
[research_grantfrederickc_sevierjohnrjr_1960]: https://ntrs.nasa.gov/citations/19980230620
[research_graphs_of_2014]: https://doi.org/10.1016/b978-0-12-419953-8.00021-8
[research_grasso_falconi_1993]: https://doi.org/10.2514/6.1993-778
[research_gratton_2014]: https://doi.org/10.1007/978-3-319-11409-5_3
[research_gratton_2018]: https://doi.org/10.1007/978-3-319-75617-2_3
[research_grauer_morelli_2023]: https://doi.org/10.2514/1.c037583
[research_gray_2008]: https://doi.org/10.2514/6.2008-1648
[research_gray_2016]: https://doi.org/10.2514/6.2016-1034
[research_green_2008]: https://doi.org/10.2514/6.2008-6379
[research_green_fernandez_1994]: https://doi.org/10.2514/6.1994-2107
[research_greene_1957]: https://doi.org/10.21236/ad0132012
[research_greenelp_1958]: https://ntrs.nasa.gov/citations/19930092381
[research_greenlawrencel_newmanperrya_1987]: https://ntrs.nasa.gov/citations/19870057679
[research_greenlawrencel_newmanperrya_1991]: https://ntrs.nasa.gov/citations/19910010730
[research_greenwell_2021]: https://doi.org/10.1017/aer.2021.107
[research_gregg_misegades_1987]: https://doi.org/10.2514/6.1987-520
[research_gregory_xargay_2011]: https://doi.org/10.2514/6.2011-6608
[research_griffin_jonas_1983]: https://doi.org/10.2514/6.1983-1835
[research_griffiths_visser_2000]: https://doi.org/10.2514/6.2000-4020
[research_grigsbycarle_1954]: https://ntrs.nasa.gov/citations/19930088297
[research_grismer_kinsey_2000]: https://doi.org/10.2514/6.2000-4325
[research_grohmann_kroplin_1999]: https://doi.org/10.1142/9789814291071_0043
[research_grosdemange_schaeffer_1990]: https://doi.org/10.2514/6.1990-1835
[research_gross_chandler_1986]: https://doi.org/10.23919/acc.1986.4789163
[research_grossar_steinlefwjr_1975]: https://ntrs.nasa.gov/citations/19760002976
[research_grosser_1965]: https://doi.org/10.2514/6.1965-789
[research_grosserwf_brittrt_1983]: https://ntrs.nasa.gov/citations/19830013947
[research_grossi]: https://doi.org/10.70675/6d7459f3zd527z472bz9b2fzee6587767e3f
[research_grossi_braza_2012]: https://doi.org/10.1007/978-3-642-31818-4_32
[research_grossi_braza_2014]: https://doi.org/10.2514/1.j052873
[research_grossman_volpe_1977]: https://doi.org/10.21236/ada043460
[research_grossman_volpe_1977_b]: https://doi.org/10.2514/6.1977-688
[research_grosvenor_zheltovodov_2012]: https://doi.org/10.1051/eucass/201203119
[research_grund_konarski_1971]: https://doi.org/10.2514/6.1971-720
[research_grunnet_1984]: https://doi.org/10.2514/3.45016
[research_guan_2013]: https://doi.org/10.4028/www.scientific.net/amm.477-478.240
[research_guan_2014]: https://doi.org/10.1017/s0001924000010010
[research_guan_2014_b]: https://doi.org/10.2514/1.j052305
[research_guangyuan_dawei_2021]: https://doi.org/10.1088/1742-6596/1877/1/012034
[research_guderley_1956]: https://doi.org/10.2514/8.3697
[research_guderley_1980]: https://doi.org/10.21236/ada087740
[research_guderley_1982]: https://doi.org/10.21236/ada120206
[research_guderley_1983]: https://doi.org/10.21236/ada129268
[research_guderley_clemm_1979]: https://doi.org/10.21236/ada072523
[research_gudilin_lashkov_1996]: https://doi.org/10.1007/bf02030231
[research_guilarteherrero_noguchi_2021]: https://doi.org/10.1007/s00348-021-03164-0
[research_guiler]: https://doi.org/10.33915/etd.2779
[research_gulcat_2010]: https://doi.org/10.1007/978-3-642-14761-6_6
[research_gulcat_2015]: https://doi.org/10.1007/978-981-10-0018-8_6
[research_gulcat_2021]: https://doi.org/10.1007/978-3-030-60777-7_6
[research_gumbert_newman_1984]: https://doi.org/10.2514/6.1984-2151
[research_gumbertclyder_greenlawrencel_1989]: https://ntrs.nasa.gov/citations/19900008332
[research_gunn_1966]: https://doi.org/10.21236/ad0633277
[research_gunn_1970]: https://doi.org/10.21236/ad0867975
[research_guo_wang_1988]: https://doi.org/10.21236/ada191553
[research_guo_wang_2025]: https://doi.org/10.1016/j.ast.2025.109966
[research_guo_zhang_2022]: https://doi.org/10.32604/cmes.2022.020638
[research_gupta]: https://doi.org/10.70675/80705d16zf54cz4d27z8ea2z49d17cd6100b
[research_gupta_ansell_2018]: https://doi.org/10.2514/6.2018-0354
[research_gupta_datta_2021]: https://doi.org/10.2514/6.2021-2756
[research_gurbacki_bragg_1999]: https://doi.org/10.2514/6.1999-3149
[research_gurbacki_bragg_2001]: https://doi.org/10.2514/2.2801
[research_gurdamar_cete_2006]: https://doi.org/10.2514/6.2006-3170
[research_gurleyjrjr_ruhlincl_1962]: https://ntrs.nasa.gov/citations/19660025705
[research_guruswamy_goorjian_1987]: https://doi.org/10.2514/6.1987-1240
[research_guruswamy_goorjian_1988]: https://doi.org/10.2514/3.10063
[research_guruswamy_tu_1988]: https://doi.org/10.2514/6.1988-2308
[research_guruswamy_tu_1989]: https://doi.org/10.2514/3.45756
[research_guy_mclaughlin_2001]: https://doi.org/10.2514/6.2001-888
[research_guy_morrow_1999]: https://doi.org/10.2514/6.1999-4178
[research_hacioglu_ozkol_2003]: https://doi.org/10.1108/00022660310484275
[research_hackett_2000]: https://doi.org/10.2514/6.2000-672
[research_hader_fasel_2023]: https://doi.org/10.2514/6.2023-0287
[research_haderlie_crossley_2009]: https://doi.org/10.2514/6.2009-6950
[research_hadjadj_dussauge_2009]: https://doi.org/10.1007/s00193-009-0238-2
[research_hafez_1982]: https://doi.org/10.1007/978-3-662-12610-3_24
[research_hafez_1999]: https://doi.org/10.2514/6.1999-1055
[research_hafez_cheng_1975]: https://doi.org/10.2514/6.1975-51
[research_hafez_cheng_1977]: https://doi.org/10.2514/3.60711
[research_hafez_lovell_1984]: https://doi.org/10.1007/978-3-662-09014-5_20
[research_hafez_wahba]: https://doi.org/10.1007/3-540-31801-1_20
[research_hafezmm_1985]: https://ntrs.nasa.gov/citations/19860036189
[research_hagen_seidel]: https://doi.org/10.1109/dasc.1993.283561
[research_hager_eyi_1992]: https://doi.org/10.2514/6.1992-4681
[research_hager_eyi_1993]: https://doi.org/10.2514/6.1993-3112
[research_hager_eyi_1994]: https://doi.org/10.2514/3.46624
[research_haglund_kane_1974]: https://doi.org/10.2514/3.60409
[research_haglundgt_kaneej_1973]: https://ntrs.nasa.gov/citations/19730009295
[research_haglundgt_kaneej_1974]: https://ntrs.nasa.gov/citations/19740023383
[research_haines_1957]: https://doi.org/10.1017/s0368393100128986
[research_haines_1990]: https://doi.org/10.2514/6.1990-1414
[research_haines_2000]: https://doi.org/10.1017/s0001924000091879
[research_hakkinenrj_greberi_1959]: https://ntrs.nasa.gov/citations/19980231989
[research_halder_damodaran_2019]: https://doi.org/10.2514/6.2019-3390
[research_hall_1978]: https://doi.org/10.2514/6.1978-811
[research_hall_1985]: https://doi.org/10.2514/6.1985-229
[research_hall_atassi_2011]: https://doi.org/10.2514/6.2011-2861
[research_hall_carraway_1989]: https://doi.org/10.2514/6.1989-2205
[research_hall_kern_1996]: https://doi.org/10.2514/6.1996-2400
[research_halljr_hopkorn_1953]: https://ntrs.nasa.gov/citations/19650003113
[research_hallrm_1978]: https://ntrs.nasa.gov/citations/19780012131
[research_hamed_1993]: https://doi.org/10.21236/ada268106
[research_hamed_mohamed_2001]: https://doi.org/10.2514/6.2001-225
[research_hameda_shihsh_1992]: https://ntrs.nasa.gov/citations/19920071384
[research_hameda_yeuanjj_1993]: https://ntrs.nasa.gov/citations/19930064187
[research_hamid_hasan_2015]: https://doi.org/10.1016/j.proeng.2015.05.022
[research_hammer_olivier_2019]: https://doi.org/10.1117/12.2524708
[research_hammertonpw_kerschenej_1998]: https://ntrs.nasa.gov/citations/19980210002
[research_han_chen_2016]: https://doi.org/10.2514/6.2016-2041
[research_han_liu_2023]: https://doi.org/10.1088/1742-6596/2472/1/012051
[research_han_xu_2022]: https://doi.org/10.1063/5.0066047
[research_handa_masuda_2003]: https://doi.org/10.2514/2.1914
[research_hanel_neuhuber_2004]: https://doi.org/10.2514/6.2004-4752
[research_haney_johnson_1979]: https://doi.org/10.2514/6.1979-80
[research_hanly_1974]: https://doi.org/10.2514/6.1974-634
[research_hanman_yao_2025]: https://doi.org/10.3390/fluids10020027
[research_hansen_1976]: https://doi.org/10.1007/978-3-642-81005-3_18
[research_hanson_1989]: https://doi.org/10.2514/6.1989-1081
[research_hansondb_finkmr_1978]: https://ntrs.nasa.gov/citations/19780024890
[research_hansonpw_1959]: https://ntrs.nasa.gov/citations/19660024794
[research_hanumantharayappa_thantanapally_2022]: https://doi.org/10.2514/6.2022-2990
[research_hara_abe_2008]: https://doi.org/10.1504/pcfd.2008.021321
[research_harbeck_jameson_2005]: https://doi.org/10.2514/6.2005-1041
[research_hares_brioua_2026]: https://doi.org/10.2139/ssrn.6136988
[research_harper_mishra_2025]: https://doi.org/10.2514/6.2025-1567
[research_harrischarlesd_brookscuylerwjr_1989]: https://ntrs.nasa.gov/citations/19890012391
[research_harrison_darragh_2016]: https://doi.org/10.2514/6.2016-4179
[research_hart_1984]: https://doi.org/10.2514/6.1984-2390
[research_hart_schmitz_2022]: https://doi.org/10.2514/6.2022-2482
[research_hartley_jacocks_1968]: https://doi.org/10.21236/ad0837078
[research_hartmann_2012]: https://doi.org/10.2514/6.2012-459
[research_hartmann_2013]: https://doi.org/10.1002/fld.3762
[research_hartmann_feldhusen_2013]: https://doi.org/10.1063/1.4791603
[research_hartmann_stein_1979]: https://doi.org/10.2514/6.1979-1702
[research_hartwich_1991]: https://doi.org/10.2514/6.1991-3286
[research_hartzuiker_1986]: https://doi.org/10.2514/6.1986-731
[research_harun_amerabbas_2024]: https://doi.org/10.5772/intechopen.1005253
[research_harvey_bobbitt_1981]: https://doi.org/10.2514/6.1981-1225
[research_harveywd_pridejd_1982]: https://ntrs.nasa.gov/citations/19820012276
[research_haryanto_utomo_2014]: https://doi.org/10.4028/www.scientific.net/amm.493.123
[research_hasallihjibrahim_dzulhelmybinamari_2019]: https://doi.org/10.14419/ijet.v8i1.1.24780
[research_hasan_alam_2013]: https://doi.org/10.1016/j.proeng.2013.03.123
[research_hasan_alam_2014]: https://doi.org/10.1615/interjfluidmechres.v41.i5.50
[research_hasan_matsuo_2012]: https://doi.org/10.1016/j.ijmecsci.2011.11.004
[research_hasegawa_sakaue_2017]: https://doi.org/10.2514/6.2017-0283
[research_haselton_goode]: https://doi.org/10.1109/oceans.1989.587280
[research_hashimoto_aoyama_2010]: https://doi.org/10.2514/6.2010-4201
[research_hashimoto_kohzai_2011]: https://doi.org/10.2514/6.2011-3017
[research_hass_housman_2024]: https://doi.org/10.2514/6.2024-4263
[research_hassan_sobieczky_1981]: https://doi.org/10.2514/6.1981-1235
[research_hastings_1954]: https://doi.org/10.21236/ad0030474
[research_hastingsearlc_mitchamgradyl_1954]: https://ntrs.nasa.gov/citations/20090023311
[research_hataue_1991]: https://doi.org/10.1016/0045-7930(91)90053-k
[research_hatayama_tanaka_2025]: https://doi.org/10.2139/ssrn.5433522
[research_haupt_buff_1985]: https://doi.org/10.2514/6.1985-103
[research_hawke_2026]: https://doi.org/10.64631/dfjy6198
[research_hawthornepj_1976]: https://ntrs.nasa.gov/citations/19760022074
[research_haxter_spehr_2018]: https://doi.org/10.2514/6.2018-3275
[research_hayabe_kwak_2025]: https://doi.org/10.2514/6.2025-0257
[research_hayashi_aso_1988]: https://doi.org/10.2514/6.1988-426
[research_hayesc_1968]: https://ntrs.nasa.gov/citations/19680012533
[research_he_cui_2022]: https://doi.org/10.32604/icces.2022.08753
[research_he_song_2020]: https://doi.org/10.2514/6.2020-1908
[research_he_wang_2021]: https://doi.org/10.2514/6.2021-2534
[research_he_williams_2022]: https://doi.org/10.2514/6.2022-0044
[research_he_williams_2023]: https://doi.org/10.2514/1.j062442
[research_he_yang_2014]: https://doi.org/10.1360/132013-258
[research_he_yang_2016]: https://doi.org/10.1016/j.jfluidstructs.2015.11.014
[research_heath_2014]: https://doi.org/10.21236/ada606473
[research_heathhreising_davidodavis]: https://ntrs.nasa.gov/citations/20230016768
[research_heathhreising_jonathansasson]: https://ntrs.nasa.gov/citations/20240014435
[research_hecht_2009]: https://doi.org/10.1016/s0262-4079(09)60350-x
[research_heeg_chwalowski_2017]: https://doi.org/10.2514/6.2017-0191
[research_heegjennifer_chwalowskipawel_2019]: https://ntrs.nasa.gov/citations/20200002638
[research_hegde_funderburk_2015]: https://doi.org/10.2514/6.2015-2934
[research_heidebrecht_2006]: https://doi.org/10.1243/09544100jaero92
[research_heidebrecht_2013]: https://doi.org/10.1504/ijesms.2013.052378
[research_heim_1991]: https://doi.org/10.21236/adb152669
[research_heineck_banks_2016]: https://doi.org/10.2514/6.2016-3356
[research_held_fuchs_1998]: https://doi.org/10.2514/6.1998-405
[research_held_fuchs_1999]: https://doi.org/10.1007/978-94-015-9285-7_10
[research_held_fuchs_1999_b]: https://doi.org/10.1615/tsfp1.2030
[research_heller_holmberg_2006]: https://doi.org/10.2514/6.2006-6485
[research_hellstrom_davidson_1994]: https://doi.org/10.2514/6.1994-309
[research_helm_grabe_2024]: https://doi.org/10.2514/6.2024-2686
[research_heltsley_cline_1979]: https://doi.org/10.21236/ada068328
[research_heltsley_crosswy_1981]: https://doi.org/10.21236/ada103929
[research_hemsch_1988]: https://doi.org/10.2514/6.1988-216
[research_hemschmichaelj_iyervenkit_2004]: https://ntrs.nasa.gov/citations/20040191536
[research_hendershot_1968]: https://doi.org/10.2514/6.1968-238
[research_hendershot_1969]: https://doi.org/10.2514/6.1969-335
[research_henderson_1990]: https://doi.org/10.1115/90-gt-338
[research_henderson_1991]: https://doi.org/10.1115/1.2906530
[research_henne_1980]: https://doi.org/10.2514/6.1980-330
[research_henne_1981]: https://doi.org/10.2514/3.57472
[research_henne_hicks_1978]: https://doi.org/10.2514/6.1978-105
[research_hennepa_hicksrm_1978]: https://ntrs.nasa.gov/citations/19780020110
[research_henningallenb_1954]: https://ntrs.nasa.gov/citations/19930090493
[research_henningallenb_1957]: https://ntrs.nasa.gov/citations/19930089916
[research_hensel_1964]: https://doi.org/10.2514/6.1964-1109
[research_herbert_1973]: https://doi.org/10.2514/3.60262
[research_hergert_bengelink_1984]: https://doi.org/10.2514/6.1984-587
[research_hergert_smith_2001]: https://doi.org/10.2514/6.2001-452
[research_hermann_1950]: https://doi.org/10.21236/ada377566
[research_hermes_klioutchnikov_2008]: https://doi.org/10.2514/6.2008-627
[research_hermes_klioutchnikov_2013]: https://doi.org/10.1016/j.ast.2012.01.009
[research_hermes_nies_2012]: https://doi.org/10.1007/978-3-642-25685-1_76
[research_heron_myose_2007]: https://doi.org/10.2514/6.2007-6725
[research_herr_spinner_2023]: https://doi.org/10.2514/6.2023-0246
[research_herring_2008]: https://doi.org/10.2514/1.36107
[research_hersch_1970]: https://doi.org/10.2514/6.1970-92
[research_hess_seidel_1987]: https://doi.org/10.2514/6.1987-35
[research_hess_seidel_1989]: https://doi.org/10.2514/3.45810
[research_hessrobertv_gardnercliffords_1949]: https://ntrs.nasa.gov/citations/19930082467
[research_hessrw_1989]: https://ntrs.nasa.gov/citations/19890009888
[research_hewesdonalde_hasselljamesljr_1960]: https://ntrs.nasa.gov/citations/19980223968
[research_hewlett_1987]: https://doi.org/10.2514/3.45515
[research_heyson_1961]: https://doi.org/10.4050/jahs.6.1
[research_hickey_hussain_2016]: https://doi.org/10.1017/jfm.2016.224
[research_hicks_1981]: https://doi.org/10.4271/810565
[research_hicks_moulton_1988]: https://doi.org/10.2514/6.1988-2144
[research_hicksjohnw_kaniajan_1987]: https://ntrs.nasa.gov/citations/19870035128
[research_hicksjohnw_petersenkevinl_1988]: https://ntrs.nasa.gov/citations/19890004053
[research_hicksjohnw_petersenkevinl_1989]: https://ntrs.nasa.gov/citations/19900001550
[research_hiesergerald_kudlaciklouis_1956]: https://ntrs.nasa.gov/citations/20050029376
[research_hiesergerald_reidcharlesf_1954]: https://ntrs.nasa.gov/citations/20090023314
[research_high_altitude_1957]: https://ntrs.nasa.gov/citations/19820068145
[research_hillenherms_schroder_2004]: https://doi.org/10.1016/j.ast.2004.07.001
[research_hillenherms_schroeder_2001]: https://doi.org/10.2514/6.2001-2468
[research_hiller_campbell_2021]: https://doi.org/10.2514/6.2021-2525
[research_hiller_campbell_2025]: https://doi.org/10.2514/6.2025-0244
[research_hillier_netterfield_1990]: https://doi.org/10.1063/1.39454
[research_hillje_nelson_1981]: https://doi.org/10.2514/6.1981-2457
[research_hillje_tymms_1978]: https://doi.org/10.2514/6.1978-792
[research_hinchliffe_qin_2016]: https://doi.org/10.2514/6.2016-0560
[research_hinchliffe_qin_2017]: https://doi.org/10.2514/1.j055319
[research_hindash_spaid_1991]: https://doi.org/10.2514/6.1991-15
[research_hindman_1992]: https://doi.org/10.21236/ada264833
[research_hingstwr_jurkovichm_1982]: https://ntrs.nasa.gov/citations/19820024799
[research_hingstwr_tanjift_1983]: https://ntrs.nasa.gov/citations/19830013929
[research_hirose_miwa_1989]: https://doi.org/10.1007/978-3-642-83584-1_39
[research_hirose_takanashi_1985]: https://doi.org/10.2514/6.1985-1592
[research_hirose_takanashi_1987]: https://doi.org/10.2514/3.9629
[research_hirtstefaniem_2015]: https://ntrs.nasa.gov/citations/20150002101
[research_hirtstefaniem_vyasmanana_2013]: https://ntrs.nasa.gov/citations/20150007505
[research_history_of_2020]: https://doi.org/10.1002/9781119667063.ch1
[research_hitachi_liu_2010]: https://doi.org/10.2514/6.2010-7856
[research_hitch_1981]: https://doi.org/10.2514/3.57477
[research_hitzel_2015]: https://doi.org/10.2514/6.2015-2871
[research_hitzel_2017]: https://doi.org/10.2514/1.c034025
[research_hitzel_2017_b]: https://doi.org/10.2514/1.c033246
[research_hoang_bui_2019]: https://doi.org/10.1007/s12206-019-0120-9
[research_hoang_rediniotis_1993]: https://doi.org/10.2514/6.1993-185
[research_hoe_owens_2012]: https://doi.org/10.2514/6.2012-4645
[research_hoff_2007]: https://doi.org/10.4271/2007-01-2542
[research_hoffmans_1958]: https://ntrs.nasa.gov/citations/19650003122
[research_holdawaygeorgeh_1955]: https://ntrs.nasa.gov/citations/19930088768
[research_holdawaygeorgeh_hatfieldelainew_1957]: https://ntrs.nasa.gov/citations/19930089658
[research_holdawaygeorgeh_mellenthinjacka_1959]: https://ntrs.nasa.gov/citations/19980232906
[research_holdawaygeorgeh_mellenthinjacka_1960]: https://ntrs.nasa.gov/citations/19980227180
[research_holdawaygeorgeh_mellenthinjacka_1960_b]: https://ntrs.nasa.gov/citations/19980235518
[research_holden_wadhams_2013]: https://doi.org/10.21236/ada582401
[research_holdenms_1966]: https://ntrs.nasa.gov/citations/19660027557
[research_holder_1963]: https://doi.org/10.2514/3.2155
[research_hollingsworth_cohen_1971]: https://doi.org/10.2514/3.59167
[research_holmes_croom_1986]: https://doi.org/10.2514/6.1986-9786
[research_holst_1981]: https://doi.org/10.2514/6.1981-1010
[research_holst_1987]: https://doi.org/10.2514/6.1987-1460
[research_holst_1988]: https://doi.org/10.2514/3.45706
[research_holst_1999]: https://doi.org/10.2514/6.1999-3133
[research_holst_bock]: https://doi.org/10.1109/iciasf.1997.644679
[research_holst_thomas_1982]: https://doi.org/10.2514/6.1982-105
[research_holt_1982]: https://doi.org/10.21236/ada216174
[research_honakerwc_1982]: https://ntrs.nasa.gov/citations/19820024821
[research_hong_ahn_1995]: https://doi.org/10.2514/6.1995-1812
[research_hong_jung_2024]: https://doi.org/10.6112/kscfe.2024.29.2.013
[research_hoodmanleyj_andersonjosephl_1942]: https://ntrs.nasa.gov/citations/20090016695
[research_hooker_1931]: https://doi.org/10.1017/s0368393100112386
[research_hooker_2014]: https://doi.org/10.2514/6.2014-1285
[research_hope_kunz_2019]: https://doi.org/10.2514/1.j057456
[research_horibata_2001]: https://doi.org/10.1007/978-3-642-56535-9_106
[research_horizontal_tail_1996]: https://doi.org/10.2514/5.9781600862465.0115.0142
[research_hornung_elsenaar_1988]: https://doi.org/10.1016/0169-5983(88)90096-2
[research_horstman_1982]: https://doi.org/10.2514/6.1982-1021
[research_horstman_1983]: https://doi.org/10.2514/3.8237
[research_horstmancc_kussoymi_1985]: https://ntrs.nasa.gov/citations/19850060829
[research_horstmann_quast_1990]: https://doi.org/10.2514/3.45910
[research_hortsen_boer_1983]: https://doi.org/10.21236/ada130488
[research_hoshi_kuya_2020]: https://doi.org/10.2514/6.2020-0091
[research_hou_clemens_2003]: https://doi.org/10.2514/6.2003-441
[research_hounkateshwar_taylor_1995]: https://doi.org/10.2514/6.1995-1692
[research_houtman_timme_2023]: https://doi.org/10.1017/flo.2023.8
[research_houtman_vevek_2023]: https://doi.org/10.2514/6.2023-3242
[research_howard_bray_1992]: https://doi.org/10.2514/6.1992-4075
[research_howell_1980]: https://doi.org/10.2514/6.1980-415
[research_howellrobertr_braslowalbertl_1955]: https://ntrs.nasa.gov/citations/20050019382
[research_hoyt_2006]: https://doi.org/10.2514/6.2006-7278
[research_hsfrs_rcs_2015]: https://ntrs.nasa.gov/citations/20160000534
[research_hsieh_1975]: https://doi.org/10.2514/6.1975-83
[research_hsieh_1975_b]: https://doi.org/10.2514/3.7007
[research_hsiung_chow_1993]: https://doi.org/10.2514/6.1993-417
[research_hsiung_onn_1997]: https://doi.org/10.1299/jsmeb.40.93
[research_hsu_1987]: https://doi.org/10.2514/6.1987-1237
[research_hsu_1988]: https://doi.org/10.2514/6.1988-217
[research_hsu_anderson_1961]: https://doi.org/10.2514/8.8910
[research_hsuch_liuch_1990]: https://ntrs.nasa.gov/citations/19900058881
[research_hu_1992]: https://doi.org/10.1016/0955-7997(92)90038-9
[research_hu_1995]: https://doi.org/10.1016/0955-7997(95)00083-6
[research_hu_2023]: https://doi.org/10.1117/12.2682010
[research_hu_huang_2025]: https://doi.org/10.2514/1.j064541
[research_hu_kandil_1990]: https://doi.org/10.1007/978-3-642-84238-2_22
[research_hu_lu_2024]: https://doi.org/10.3390/aerospace11110932
[research_hu_qu_2018]: https://doi.org/10.2514/6.2018-4114
[research_hu_zhao_2011]: https://doi.org/10.2514/6.2011-6366
[research_hu_zhu_2024]: https://doi.org/10.1088/1742-6596/2879/1/012032
[research_huan_modi_1995]: https://doi.org/10.1115/imece1995-0953
[research_huang_folk_2001]: https://doi.org/10.2514/6.2001-124
[research_huang_liang_2026]: https://doi.org/10.3390/s26051476
[research_hubbard_fontenot_2014]: https://doi.org/10.2514/1.c032339
[research_hubbard_mcfarland_2011]: https://doi.org/10.2514/6.2011-6289
[research_hube_1978]: https://doi.org/10.21236/ada067908
[research_hubertmdrake_1949]: https://ntrs.nasa.gov/citations/19930085857
[research_hue_molton_2020]: https://doi.org/10.1063/1.5143068
[research_huerta_1969]: https://doi.org/10.21236/ad0855156
[research_huff_wu_1987]: https://doi.org/10.2514/6.1987-420
[research_hughesmt_mennellrc_1974]: https://ntrs.nasa.gov/citations/19750005750
[research_hui_collins_2001]: https://doi.org/10.2514/6.2001-410
[research_huijts_voskuijl_2015]: https://doi.org/10.1016/j.ast.2015.07.001
[research_humphries_gillan_1998]: https://doi.org/10.2514/6.1998-946
[research_hungchingmao_1989]: https://ntrs.nasa.gov/citations/19900002654
[research_hungchingmao_1990]: https://ntrs.nasa.gov/citations/19910049572
[research_hungchingmao_buningpieterg_1985]: https://ntrs.nasa.gov/citations/19990066634
[research_hungcm_buningpg_1984]: https://ntrs.nasa.gov/citations/19840038514
[research_hungcm_maccormackrw_1978]: https://ntrs.nasa.gov/citations/19780038682
[research_hunn_1953]: https://doi.org/10.1017/s0368393100131128
[research_hunziker_1960]: https://doi.org/10.1007/bf01595402
[research_huo_wang_2026]: https://doi.org/10.3390/aerospace13040352
[research_hurley_1975]: https://doi.org/10.2514/3.49684
[research_hurleyfx_spaidfw_1975]: https://ntrs.nasa.gov/citations/19750049892
[research_husain_piotrowski_2026]: https://doi.org/10.2514/6.2026-1695
[research_huse_1948]: https://doi.org/10.4271/480048
[research_hussainimy_baldwinbs_1980]: https://ntrs.nasa.gov/citations/19800058965
[research_hussein_chudoba_2016]: https://doi.org/10.2514/6.2016-3464
[research_huttselllj_nollte_1976]: https://ntrs.nasa.gov/citations/19770014086
[research_hwang_chen_1991]: https://doi.org/10.2514/6.1991-2423
[research_hwang_park_2026]: https://doi.org/10.5139/jksas.2026.54.2.117
[research_hwang_pi_1975]: https://doi.org/10.2514/3.44487
[research_hwang_pi_1975_b]: https://doi.org/10.2514/6.1975-70
[research_hwang_pi_1979]: https://doi.org/10.2514/3.58518
[research_hybrid_approach_1982]: https://doi.org/10.2514/5.9781600865558.0605.0620
[research_ibrahim_filippone_2006]: https://doi.org/10.2514/6.2006-3853
[research_ibrahim_filippone_2007]: https://doi.org/10.2514/1.30439
[research_ice_and]: https://doi.org/10.4271/as5562
[research_ii_1970]: https://doi.org/10.2514/6.1970-944
[research_illi_fingskes_2013]: https://doi.org/10.2514/6.2013-2510
[research_imai_1952]: https://doi.org/10.2514/8.2355
[research_imai_nakakita_2021]: https://doi.org/10.2514/6.2021-0127
[research_imai_nakakita_2022]: https://doi.org/10.1007/s00348-022-03527-1
[research_imig_1973]: https://doi.org/10.1520/stp38845s
[research_in_flight_thrust]: https://doi.org/10.4271/air6007
[research_in_flight_thrust_b]: https://doi.org/10.4271/air1703
[research_inger_1976]: https://doi.org/10.2514/6.1976-463
[research_inger_1979]: https://doi.org/10.2514/3.58519
[research_inger_1979_b]: https://doi.org/10.2514/6.1979-5
[research_inger_1981]: https://doi.org/10.2514/6.1981-1244
[research_inger_1982]: https://doi.org/10.1007/978-3-662-12610-3_10
[research_inger_1983]: https://doi.org/10.21236/ada123389
[research_inger_1983_b]: https://doi.org/10.2514/3.44911
[research_inger_1984]: https://doi.org/10.2514/6.1984-94
[research_inger_1985]: https://doi.org/10.2514/3.45155
[research_inger_1988]: https://doi.org/10.2514/6.1988-2590
[research_inger_1988_b]: https://doi.org/10.2514/6.1988-2592
[research_inger_1991]: https://doi.org/10.2514/6.1991-3210
[research_inger_2011]: https://doi.org/10.1017/cbo9780511842757.010
[research_inger_gendt_1997]: https://doi.org/10.2514/6.1997-65
[research_inger_kayser_1983]: https://doi.org/10.2514/6.1983-2076
[research_inger_mason_1976]: https://doi.org/10.1007/978-3-642-81005-3_25
[research_inger_mason_1976_b]: https://doi.org/10.2514/3.61460
[research_inger_nandanan_1986]: https://doi.org/10.2514/6.1986-1035
[research_initial_flight_1989]: https://doi.org/10.2514/6.1989-3359
[research_integral_equation_1982]: https://doi.org/10.1007/3-540-11499-8
[research_intveldalexanderc_karwalarunk_2012]: https://doi.org/10.3233/978-1-61499-119-9-400
[research_inverse_airfoil_1990]: https://doi.org/10.2514/5.9781600865985.0191.0220
[research_investigation_of_1979]: https://doi.org/10.2514/6.1979-797
[research_irfan_nanangburhan_2026]: https://doi.org/10.35261/barometer.v11i2.13201
[research_ishida_hashimoto_2017]: https://doi.org/10.2514/6.2017-0494
[research_ishida_ishiko_2016]: https://doi.org/10.2514/6.2016-1310
[research_ishida_ueshima_2026]: https://doi.org/10.2514/1.c038925
[research_ishiit_yanagizawam_1967]: https://ntrs.nasa.gov/citations/19670030828
[research_ishikawa_kwak_2007]: https://doi.org/10.2514/6.2007-3925
[research_ishikawa_kwak_2008]: https://doi.org/10.2514/1.33595
[research_ishrak_shuvo_2024]: https://doi.org/10.2514/6.2024-90206
[research_isogai_1979]: https://doi.org/10.2514/3.61226
[research_isogai_1981]: https://doi.org/10.2514/3.7853
[research_isogai_2016]: https://doi.org/10.2322/tjsass.59.25
[research_isogai_2024]: https://doi.org/10.2322/tjsass.67.260
[research_itemcemc_baysaloktay_1995]: https://ntrs.nasa.gov/citations/19960008471
[research_ito_takanashi_1991]: https://doi.org/10.2514/6.1991-3202
[research_iwai_2018]: https://doi.org/10.1299/jsmemecj.2018.g0500104
[research_iwai_suzuki_2019]: https://doi.org/10.1299/jsmemecj.2019.j05515
[research_iwatani_asada_2022]: https://doi.org/10.2514/6.2022-0461
[research_iyer_kuhl_2004]: https://doi.org/10.2514/6.2004-2306
[research_iyer_park_2017]: https://doi.org/10.2514/6.2017-3953
[research_iyer_takahashi_2025]: https://doi.org/10.2514/6.2025-3226
[research_izumi_ogino_2015]: https://doi.org/10.2514/6.2015-0259
[research_jabbar_setiawan_2026]: https://doi.org/10.35261/barometer.v11i2.13206
[research_jackson_1976]: https://doi.org/10.21236/adb008985
[research_jackson_1978]: https://doi.org/10.21236/ada057877
[research_jacksonlr_kirkhamfs_1978]: https://ntrs.nasa.gov/citations/19790005909
[research_jacobs_kopriva_2002]: https://doi.org/10.2514/6.2002-3595
[research_jacobs_ran_2012]: https://doi.org/10.2514/6.2012-2889
[research_jacobsen_abbottirah_1939]: https://ntrs.nasa.gov/citations/20090015023
[research_jacobson_stanford_2021]: https://doi.org/10.2514/6.2021-2700
[research_jacocks_1969]: https://doi.org/10.21236/ad0851575
[research_jacocks_1969_b]: https://doi.org/10.21236/ad0857045
[research_jacocks_1970]: https://doi.org/10.21236/ad0868290
[research_jacocks_hartley_1969]: https://doi.org/10.21236/ad0853841
[research_jacquin_molton_2005]: https://doi.org/10.2514/6.2005-4902
[research_jacquin_molton_2009]: https://doi.org/10.2514/1.30190
[research_jaeger_thome_2026]: https://doi.org/10.2514/6.2026-4164
[research_jaffe_1972]: https://doi.org/10.2514/6.1972-983
[research_jaffep_1975]: https://ntrs.nasa.gov/citations/19750008472
[research_jagharghi_cler_1995]: https://doi.org/10.2514/6.1995-639
[research_jain_1988]: https://doi.org/10.14429/dsj.38.4836
[research_james_1998]: https://doi.org/10.1108/rr.1998.12.1.25.27
[research_jamesablackwelljr_1969]: https://ntrs.nasa.gov/citations/19830002814
[research_jamesjr_1981]: https://doi.org/10.2514/6.1981-1905
[research_jameson]: https://doi.org/10.1007/bfb0074531
[research_jameson_1973]: https://doi.org/10.2514/6.1973-3002
[research_jameson_1977]: https://doi.org/10.2172/7093932
[research_jameson_1982]: https://doi.org/10.1016/b978-0-12-493280-7.50008-5
[research_jameson_b]: https://doi.org/10.1007/3-540-09119-x_97
[research_jameson_caughey_1977]: https://doi.org/10.2172/7308750
[research_jameson_vassberg_2008]: https://doi.org/10.2514/6.2008-145
[research_jamesona_1979]: https://ntrs.nasa.gov/citations/19790061249
[research_jamesona_caugheyda_1977]: https://ntrs.nasa.gov/citations/19770020127
[research_jamesreynolds_ethanbaumann]: https://ntrs.nasa.gov/citations/20240007413
[research_janardhan_grandhi_2003]: https://doi.org/10.21236/ada417106
[research_janardhan_grandhi_2003_b]: https://doi.org/10.2514/6.2003-1944
[research_jankiewicz_2026]: https://doi.org/10.21741/9781644904251-46
[research_jansen_glockner_2024]: https://doi.org/10.2139/ssrn.4748366
[research_jansen_glockner_2025]: https://doi.org/10.1016/j.cpc.2025.109742
[research_jaredagrauer_josiahmwaite]: https://ntrs.nasa.gov/citations/20230016314
[research_jaredagrauer_matthewjboucher]: https://ntrs.nasa.gov/citations/20200002775
[research_jarvinen_2013]: https://doi.org/10.2514/6.2013-655
[research_jayachandran_bhanu_1987]: https://doi.org/10.1007/978-94-009-3655-3_28
[research_jdelery_jgmarvin_1986]: https://ntrs.nasa.gov/citations/19860019701
[research_jegdic_2019]: https://doi.org/10.12732/ijam.v32i1.6
[research_jenkins_1986]: https://doi.org/10.4271/861767
[research_jenkinsrenaldov_1989]: https://ntrs.nasa.gov/citations/19890008197
[research_jenkinsrenaldov_hillacquillas_1988]: https://ntrs.nasa.gov/citations/19880015196
[research_jenkinsrv_1983]: https://ntrs.nasa.gov/citations/19840003073
[research_jenkinsrv_1983_b]: https://ntrs.nasa.gov/citations/19840005083
[research_jenkinsrv_1986]: https://ntrs.nasa.gov/citations/19860015191
[research_jenkinsrv_johnsonwgjr_1984]: https://ntrs.nasa.gov/citations/19840025314
[research_jenney_schreadley_1982]: https://doi.org/10.21236/ada117244
[research_jente_2022]: https://doi.org/10.2514/6.2022-2826
[research_jeon_kim_2014]: https://doi.org/10.3795/ksme-b.2014.38.3.219
[research_jepps_1981]: https://doi.org/10.1007/978-3-663-14008-5_9
[research_jesudasan_doherty_2026]: https://doi.org/10.1016/j.ast.2025.110727
[research_jet_thrust_2003]: https://doi.org/10.2514/5.9781600861840.0069.0074
[research_jet_transport_highspeed_1959]: https://ntrs.nasa.gov/citations/19980228311
[research_jettmar_1984]: https://doi.org/10.2514/6.1984-2114
[research_jewell_shepherd_2013]: https://doi.org/10.21236/ada595841
[research_ji_huang_2024]: https://doi.org/10.3390/aerospace11010080
[research_ji_liu_1996]: https://doi.org/10.2514/6.1996-63
[research_ji_yang_2025]: https://doi.org/10.2139/ssrn.5229428
[research_jia_li_2024]: https://doi.org/10.1061/jaeeez.aseng-4978
[research_jiang_2000]: https://doi.org/10.2514/6.2000-510
[research_jiang_2024]: https://doi.org/10.3397/in_2024_3407
[research_jiang_an_2000]: https://doi.org/10.2514/6.2000-4324
[research_jiang_tian_2019]: https://doi.org/10.1016/j.ast.2019.03.043
[research_jiang_wang_2023]: https://doi.org/10.1063/5.0139656
[research_jimeneznavarro]: https://doi.org/10.70675/f6a56be9ze2f7z4811z8af4ze14f69bda00f
[research_jin_ren_2013]: https://doi.org/10.2514/6.2013-641
[research_jing_lu_2025]: https://doi.org/10.3390/app15137309
[research_jingeleski_schetz_2013]: https://doi.org/10.2514/6.2013-2403
[research_jinks_bruce_2016]: https://doi.org/10.2514/6.2016-1553
[research_jinli_zhichun_2013]: https://doi.org/10.1016/j.proeng.2013.08.028
[research_jirasek_cavagna_2014]: https://doi.org/10.2514/6.2014-0421
[research_jmichealramey_martinksekula]: https://ntrs.nasa.gov/citations/20205002605
[research_joarder_2018]: https://doi.org/10.1007/s00193-018-0868-3
[research_johcy_grossmanb_1991]: https://ntrs.nasa.gov/citations/19920004743
[research_johnelamar_cliffordjobara_2001]: https://ntrs.nasa.gov/citations/20010047400
[research_johnson]: https://doi.org/10.15368/theses.2018.96
[research_johnson_1953]: https://doi.org/10.7249/rm1188
[research_johnson_1972]: https://doi.org/10.21236/ad0754909
[research_johnson_1982]: https://doi.org/10.1007/978-3-662-12610-3_31
[research_johnson_1986]: https://doi.org/10.1007/978-1-4612-4972-6_18
[research_johnson_bachalo_1978]: https://doi.org/10.2514/6.1978-1117
[research_johnson_bachalo_1980]: https://doi.org/10.2514/3.50725
[research_johnson_josepha_1970]: https://doi.org/10.21236/ad0702806
[research_johnson_king_1986]: https://doi.org/10.1007/978-3-642-82770-9_3
[research_johnson_owen_1979]: https://doi.org/10.2514/6.1979-1500
[research_johnson_papamoschou_2010]: https://doi.org/10.1063/1.3278523
[research_johnsoncb_adcockjb_1981]: https://ntrs.nasa.gov/citations/19810054670
[research_johnsoncb_johnsonwgjr_1986]: https://ntrs.nasa.gov/citations/19870045352
[research_johnsoncb_murthyav_1986]: https://ntrs.nasa.gov/citations/19870002368
[research_johnsoncharlesb_dressdavida_1986]: https://ntrs.nasa.gov/citations/19880014350
[research_johnsonclintont_1958]: https://ntrs.nasa.gov/citations/19930090009
[research_johnsonwgjr_hillas_1982]: https://ntrs.nasa.gov/citations/19840019616
[research_johnsonwgjr_hillas_1985]: https://ntrs.nasa.gov/citations/19850021614
[research_johnsonwgjr_hillas_1985_b]: https://ntrs.nasa.gov/citations/19850021615
[research_johnsonwgjr_hillas_1985_c]: https://ntrs.nasa.gov/citations/19860006729
[research_johnston_1992]: https://doi.org/10.2514/6.1992-2653
[research_johnston_1998]: https://doi.org/10.2514/6.1998-2736
[research_johnwhicks_jankania_1987]: https://ntrs.nasa.gov/citations/19870011558
[research_jokari_kamali_2025]: https://doi.org/10.2139/ssrn.5718547
[research_jokari_kamali_2026]: https://doi.org/10.21203/rs.3.rs-8768983/v1
[research_jonathansasson_heathhreising]: https://ntrs.nasa.gov/citations/20220017565
[research_jones_1947]: https://ntrs.nasa.gov/citations/19930091936
[research_jones_1977]: https://doi.org/10.1016/0094-5765(77)90035-2
[research_jones_jarrett_2018]: https://doi.org/10.2514/1.j056725
[research_jones_platzer_1998]: https://doi.org/10.2514/6.1998-517
[research_jones_townsend_2000]: https://doi.org/10.2514/6.2000-268
[research_jones_vandyke_1958]: https://doi.org/10.2514/8.7560
[research_jonesdaniels_buitrongt_2013]: https://ntrs.nasa.gov/citations/20130014511
[research_jonesgeorgewjr_farmermosesg_1959]: https://ntrs.nasa.gov/citations/19980223588
[research_jonesgwjr_unangstjr_1963]: https://ntrs.nasa.gov/citations/19630002604
[research_jonesrt_1976]: https://ntrs.nasa.gov/citations/19760011995
[research_joppa_1968]: https://doi.org/10.2514/6.1968-399
[research_joppa_1969]: https://doi.org/10.2514/3.44037
[research_jordanfljr_1972]: https://ntrs.nasa.gov/citations/19830002759
[research_jordangarethh_keenerearlr_1955]: https://ntrs.nasa.gov/citations/19930088562
[research_joshi_1996]: https://doi.org/10.2514/3.55724
[research_joshi_salahudden_2023]: https://doi.org/10.2514/6.2023-1556
[research_joshi_thomas_2025]: https://doi.org/10.1109/aero63441.2025.11068430
[research_jou_metcalfe_1984]: https://doi.org/10.21236/ada150123
[research_jou_mueller_1985]: https://doi.org/10.21236/ada172853
[research_julianooi_2024]: https://doi.org/10.52403/ijshr.20240450
[research_jumper_1983]: https://doi.org/10.2514/3.44961
[research_jun_zhenghong_2009]: https://doi.org/10.1016/s1000-9361(08)60091-6
[research_june_hickey_2025]: https://doi.org/10.2514/6.2025-3884
[research_juntaoxiong_nhannguyen]: https://ntrs.nasa.gov/citations/20220019224
[research_juntaoxiong_nhannguyen_b]: https://ntrs.nasa.gov/citations/20230018144
[research_jurado_mcgehee_2019]: https://doi.org/10.2514/1.c034964
[research_jutte_mason_2024]: https://doi.org/10.2514/6.2024-2811
[research_k_bhardwaj_2023]: https://doi.org/10.2514/6.2023-0242
[research_kabaleeshwaran_das_2026]: https://doi.org/10.1017/aer.2026.10236
[research_kacprzynski_1975]: https://doi.org/10.2514/6.1975-81
[research_kady_takahashi_2014]: https://doi.org/10.2514/6.2014-0024
[research_kafyeke_piperni_1988]: https://doi.org/10.4271/881483
[research_kale_pendharkar_2021]: https://doi.org/10.1088/1742-6596/2089/1/012024
[research_kalkhoran_otugen_1994]: https://doi.org/10.21236/ada299229
[research_kalkhoran_sforza_1992]: https://doi.org/10.2514/6.1992-2631
[research_kalkhoran_wilson_1989]: https://doi.org/10.2514/6.1989-1833
[research_kalkhoran_wilson_1992]: https://doi.org/10.2514/3.11183
[research_kalra_zaidi_2007]: https://doi.org/10.2514/6.2007-222
[research_kalra_zaidi_2007_b]: https://doi.org/10.2514/6.2007-4138
[research_kamboj_2026]: https://doi.org/10.31224/7922
[research_kameda_seki_2008]: https://doi.org/10.2514/6.2008-6418
[research_kamiya_nishi_1978]: https://doi.org/10.2514/6.1978-1221
[research_kanchi_he_2026]: https://doi.org/10.2514/6.2026-4639
[research_kandath_pushpangathan_2023]: https://doi.org/10.1109/icuas57906.2023.10155971
[research_kandil_hu_1988]: https://doi.org/10.1007/978-3-663-13997-3_8
[research_kandil_hu_1990]: https://doi.org/10.2514/3.45907
[research_kandil_kalisch_1994]: https://doi.org/10.2514/6.1994-1887
[research_kandil_kamdil_1994]: https://doi.org/10.2514/6.1994-1426
[research_kandil_kandil_1993]: https://doi.org/10.2514/6.1993-2973
[research_kandil_kandil_1993_b]: https://doi.org/10.2514/6.1993-3472
[research_kandil_menzies_1996]: https://doi.org/10.2514/6.1996-828
[research_kaneko_menshov_2000]: https://doi.org/10.2514/6.2000-2600
[research_kaneko_oyama_2024]: https://doi.org/10.2514/6.2024-0890
[research_kaneko_oyama_2024_b]: https://doi.org/10.2514/6.2024-3588
[research_kang_chen_2024]: https://doi.org/10.3390/aerospace11090722
[research_kannenberg_boyd_1994]: https://doi.org/10.2514/6.1994-3301
[research_kapania_issac_1994]: https://doi.org/10.2514/3.59995
[research_kapaniarakeshk_issacjasonc_1993]: https://ntrs.nasa.gov/citations/19930050174
[research_kapaniarakeshk_schetzjosepha_2018]: https://ntrs.nasa.gov/citations/20180008436
[research_karlgaard_schoenenberger_2017]: https://doi.org/10.2514/6.2017-0470
[research_karlsson_sedin_1979]: https://doi.org/10.2514/3.61249
[research_karnick_venkatraman_2017]: https://doi.org/10.1017/jfm.2017.629
[research_karns_strike_2017]: https://doi.org/10.2514/6.2017-0333
[research_karpouzian_librescu_1992]: https://doi.org/10.2514/6.1992-2469
[research_karpovichea_franklfi_1951]: https://ntrs.nasa.gov/citations/19930093957
[research_karthik_tulapurkara_1999]: https://doi.org/10.2514/2.2529
[research_kashitani_miura_2012]: https://doi.org/10.1007/s11630-012-0565-y
[research_kashitani_taguchi_2020]: https://doi.org/10.2514/6.2020-1356
[research_kashitani_yamaguchi_2008]: https://doi.org/10.2514/6.2008-850
[research_kashitani_yamaguchi_2010]: https://doi.org/10.2514/6.2010-744
[research_kashitani_yamaguchi_2010_b]: https://doi.org/10.2322/tjsass.52.193
[research_kasimbiber_trentonwhite_2019]: https://doi.org/10.17265/2159-5275/2019.06.004
[research_kass_1970]: https://doi.org/10.2514/6.1970-875
[research_kassem_banerjee]: https://doi.org/10.4203/ccp.108.110
[research_katanoda_handa_2001]: https://doi.org/10.2514/2.5829
[research_katz_2013]: https://doi.org/10.2514/6.2013-2659
[research_kaul_2021]: https://doi.org/10.1115/1.4050800
[research_kaul_2022]: https://doi.org/10.1115/1.4055911
[research_kaul_2024]: https://doi.org/10.1016/j.ast.2024.109376
[research_kaul_nguyen_2019]: https://doi.org/10.2514/6.2019-2037
[research_kaulupenderk_nguyennhant_2019]: https://ntrs.nasa.gov/citations/20190030746
[research_kaups_mehta_1989]: https://doi.org/10.2514/3.45774
[research_kawakami_takatoya_2007]: https://doi.org/10.2514/6.2007-4174
[research_kawamura_karashima_1957]: https://doi.org/10.2322/jjsass1953.5.93
[research_kaya_2025]: https://doi.org/10.36306/konjes.1743613
[research_kayser_clay_1986]: https://doi.org/10.2514/6.1986-785
[research_kearns_1962]: https://doi.org/10.21236/ad0650981
[research_keener_1984]: https://doi.org/10.2514/6.1984-2092
[research_keener_1985]: https://doi.org/10.2514/3.45163
[research_keenerearlr_bandishrozaliam_1951]: https://ntrs.nasa.gov/citations/19930086693
[research_keenerearlr_mcleodnormanj_1958]: https://ntrs.nasa.gov/citations/19930090188
[research_keenerer_1959]: https://ntrs.nasa.gov/citations/19650003087
[research_keenerer_piercem_1950]: https://ntrs.nasa.gov/citations/19650068445
[research_kehletalanb_1954]: https://ntrs.nasa.gov/citations/20090023148
[research_kehoe_1988]: https://doi.org/10.2514/6.1988-2075
[research_keith_selberg_1984]: https://doi.org/10.2514/3.48244
[research_kelly_1988]: https://doi.org/10.2514/6.1988-2129
[research_kelly_2014]: https://doi.org/10.2514/6.2014-0614
[research_kelly_jamal_2025]: https://doi.org/10.2514/6.2025-3092
[research_kellythomasc_1955]: https://ntrs.nasa.gov/citations/19930088852
[research_kelnhofer_1969]: https://doi.org/10.1115/69-gt-55
[research_kempelrobertw_mcneillwaltere_1988]: https://ntrs.nasa.gov/citations/19880035069
[research_kempelrw_danawh_1975]: https://ntrs.nasa.gov/citations/19750018943
[research_kempwilliambjr_1991]: https://ntrs.nasa.gov/citations/19910011842
[research_kempwilliambjr_kingthomasjjr_1956]: https://ntrs.nasa.gov/citations/19930089459
[research_kendall_1982]: https://doi.org/10.21236/ada115404
[research_kendall_1984]: https://doi.org/10.2514/6.1984-2164
[research_kennellyjr_1983]: https://doi.org/10.2514/6.1983-1864
[research_kennellyrobertajr_carmichaelralphl_1999]: https://ntrs.nasa.gov/citations/20050243387
[research_kennellyrobertajr_krooilanm_1990]: https://ntrs.nasa.gov/citations/19920022969
[research_kenney_1939]: https://doi.org/10.1108/eb030526
[research_kentfield_spragins_2004]: https://doi.org/10.2514/1.558
[research_kerlick_nixon_1982]: https://doi.org/10.2514/6.1982-159
[research_kerlick_nixon_1983]: https://doi.org/10.2514/3.8175
[research_kerschen_tsai_1989]: https://doi.org/10.2514/6.1989-1082
[research_kesic_majic_2004]: https://doi.org/10.2514/6.2004-1055
[research_kettle_1954]: https://doi.org/10.1017/s0368393100102159
[research_kevinejacobson_bretkstanford]: https://ntrs.nasa.gov/citations/20210017172
[research_kevinejacobson_bretkstanford_b]: https://ntrs.nasa.gov/citations/20210024495
[research_keyfitz_canic_1998]: https://doi.org/10.1137/s0036139996300
[research_keyfitz_melnik_1977]: https://doi.org/10.2514/6.1977-676
[research_keyfitz_melnik_1978]: https://doi.org/10.1093/qjmam/31.2.137
[research_keyfitz_melnik_1979]: https://doi.org/10.2514/3.61115
[research_khalid_mokry_1996]: https://doi.org/10.2514/3.47034
[research_khan_deng_2012]: https://doi.org/10.1109/ibcast.2012.6177558
[research_khan_kapania_2023]: https://doi.org/10.2514/6.2023-3944
[research_khan_mallik_2021]: https://doi.org/10.2514/6.2021-1354
[research_khanal_knowles_2009]: https://doi.org/10.2514/6.2009-701
[research_khlebnikov_1990]: https://doi.org/10.1007/bf01049830
[research_kholodar_dowell_2004]: https://doi.org/10.2514/1.618
[research_kholodar_dowell_2004_b]: https://doi.org/10.2514/1.467
[research_kholodar_thomas_2002]: https://doi.org/10.2514/6.2002-1211
[research_khot_eastep_1997]: https://doi.org/10.2514/6.1997-1268
[research_kickertreiner_2012]: https://doi.org/10.3233/978-1-61499-119-9-393
[research_kieszek_2024]: https://doi.org/10.15866/irease.v17i6.25671
[research_kieszek_majcher_2024]: https://doi.org/10.15632/jtam-pl/189805
[research_kikuchi_kouchi_2024]: https://doi.org/10.2514/6.2024-0905
[research_kikuchi_miyake_2026]: https://doi.org/10.2514/6.2026-4526
[research_kilgore_adcock_1974]: https://doi.org/10.2514/6.1974-80
[research_kim_2006]: https://doi.org/10.1016/j.na.2005.05.046
[research_kim_chang_2009]: https://doi.org/10.2514/6.2009-3501
[research_kim_cho]: https://doi.org/10.1109/hpc.1997.592127
[research_kim_chokani_1990]: https://doi.org/10.2514/6.1990-3101
[research_kim_kim_2008]: https://doi.org/10.2514/1.37435
[research_kim_lee_2001]: https://doi.org/10.2514/6.2001-1464
[research_kim_lee_2003]: https://doi.org/10.2514/6.2003-1412
[research_kim_lee_2012]: https://doi.org/10.3795/ksme-b.2012.36.1.061
[research_kim_liou_2019]: https://doi.org/10.1016/j.ast.2018.11.047
[research_kim_marciniak_1999]: https://doi.org/10.2514/6.1999-1468
[research_kim_marciniak_2002]: https://doi.org/10.2514/2.2936
[research_kim_matsuo_1996]: https://doi.org/10.1007/bf02535741
[research_kim_park_2026]: https://doi.org/10.6112/kscfe.2026.31.2.084
[research_kim_rho_1998]: https://doi.org/10.2514/6.1998-599
[research_kim_sung_1993]: https://doi.org/10.2514/6.1993-3474
[research_kim_sung_1995]: https://doi.org/10.2514/3.46722
[research_kim_winchenbach_1985]: https://doi.org/10.2514/6.1985-1777
[research_kimberlin_1987]: https://doi.org/10.4271/872314
[research_kimberlin_sims_1992]: https://doi.org/10.2514/6.1992-4090
[research_kimhyun_hingstwarrenr_1996]: https://ntrs.nasa.gov/citations/19970009931
[research_kimmel_borg_2015]: https://doi.org/10.21236/ada623564
[research_kimmelrogerl_prabhudinesh_2015]: https://ntrs.nasa.gov/citations/20160003109
[research_king_johnson_1980]: https://doi.org/10.2514/6.1980-1366
[research_king_johnson_1986]: https://doi.org/10.2514/3.9448
[research_kingrudolpha_andinomarlyny_2012]: https://ntrs.nasa.gov/citations/20120001277
[research_kingrudolpha_andinomarlyny_2013]: https://ntrs.nasa.gov/citations/20160005103
[research_kirkham_jackson_1974]: https://doi.org/10.2514/6.1974-988
[research_kirkman_takahashi_2016]: https://doi.org/10.2514/6.2016-4329
[research_kirkman_takahashi_2017]: https://doi.org/10.2514/6.2017-0266
[research_kish_wilde_2019]: https://doi.org/10.1109/aero.2019.8741812
[research_kishi_yashiro_2023]: https://doi.org/10.3390/aerospace10080717
[research_klausmeyer_2004]: https://doi.org/10.2514/6.2004-553
[research_klausmeyer_2018]: https://doi.org/10.2514/6.2018-2992
[research_kleifges_dolling_1993]: https://doi.org/10.2514/6.1993-3281
[research_klein_2019]: https://doi.org/10.2514/6.2019-1180
[research_kleppin_ruetenik_1980]: https://doi.org/10.21236/ada093729
[research_klevenhusen_1980]: https://doi.org/10.2514/6.1980-340
[research_klifi_lili_2013]: https://doi.org/10.1016/j.crme.2013.04.003
[research_klim_zeppetelli_2013]: https://doi.org/10.4271/2013-01-2232
[research_kline_2026]: https://doi.org/10.2514/6.2026-4317
[research_klioutchnikov_ballmann]: https://doi.org/10.1007/978-1-4020-5152-2_85
[research_klioutchnikov_ballmann_2008]: https://doi.org/10.1007/978-3-540-75712-2_61
[research_klioutchnikov_olivier_2010]: https://doi.org/10.2514/6.2010-924
[research_klopfer_nielsen_1980]: https://doi.org/10.2514/6.1980-126
[research_klug_naik_2021]: https://doi.org/10.2514/6.2021-1649
[research_klunker_newman_1974]: https://doi.org/10.2514/3.59233
[research_klutchnikov_ballmann_2004]: https://doi.org/10.1007/978-1-4020-2313-2_24
[research_kluwick_cox_2018]: https://doi.org/10.1017/jfm.2018.368
[research_kluwick_kornfeld_2013]: https://doi.org/10.1063/1.4825476
[research_klyde_harris_2004]: https://doi.org/10.21236/ada426452
[research_kmak_2000]: https://doi.org/10.2514/6.2000-2680
[research_knackstedt_1952]: https://doi.org/10.21236/ad0008717
[research_knaus_1981]: https://doi.org/10.2514/6.1981-2420
[research_knight_1982]: https://doi.org/10.21236/ada127118
[research_knight_1983]: https://doi.org/10.21236/ada138722
[research_knight_1992]: https://doi.org/10.21236/ada265275
[research_knight_braun_2011]: https://doi.org/10.2514/6.2011-3963
[research_knight_braun_2012]: https://doi.org/10.2514/1.c031731
[research_knipfer_schewe_1999]: https://doi.org/10.2514/6.1999-653
[research_knoedler_bailey]: https://doi.org/10.1109/plans.1996.509128
[research_knoedler_bailey_1996]: https://doi.org/10.2514/6.1996-3417
[research_knott_1974]: https://doi.org/10.21236/ad0786467
[research_ko_mason_2003]: https://doi.org/10.2514/6.2003-4062
[research_kocheemoolayil_lele_2016]: https://doi.org/10.2514/6.2016-2919
[research_kodigaddi_2026]: https://doi.org/10.21203/rs.3.rs-10227402/v1
[research_kodigaddi_khazi_2024]: https://doi.org/10.37591/jopc.v11i13.136771
[research_koenig_1984]: https://doi.org/10.21236/ada150667
[research_koenigdavidg_1953]: https://ntrs.nasa.gov/citations/19930087427
[research_koenigdavidg_1953_b]: https://ntrs.nasa.gov/citations/19930087582
[research_kohzai_sudani_2010]: https://doi.org/10.2514/6.2010-4200
[research_koike_ueno_2016]: https://doi.org/10.2514/6.2016-4044
[research_kojima_hashimoto_2022]: https://doi.org/10.2514/6.2022-0464
[research_kojima_hashimoto_2023]: https://doi.org/10.2514/6.2023-1425
[research_kojima_kameda_2019]: https://doi.org/10.1007/978-3-319-91017-8_134
[research_kokin_lysenko_1972]: https://doi.org/10.1007/bf01205387
[research_kolar_lile_1971]: https://doi.org/10.21236/ada377254
[research_kolesar_kassianides_1970]: https://doi.org/10.21236/ad0734233
[research_kolonay_blair_1994]: https://doi.org/10.2514/6.1994-1551
[research_kolonay_yang_1998]: https://doi.org/10.2514/2.7578
[research_konig_singh_2018]: https://doi.org/10.2514/6.2018-3171
[research_konovalov_lashkov_1998]: https://doi.org/10.1007/bf02698171
[research_konrath_2015]: https://doi.org/10.2514/6.2015-1095
[research_konrath_schroder_2006]: https://doi.org/10.2514/6.2006-3003
[research_kontogiannis_parenteau_2019]: https://doi.org/10.2514/6.2019-2116
[research_kordan_vonlavante_1985]: https://doi.org/10.2514/6.1985-2
[research_koreanschi_oliviu_2014]: https://doi.org/10.2514/6.2014-3170
[research_koren_1989]: https://doi.org/10.1002/fld.1650090106
[research_kornev_pimenov_2022]: https://doi.org/10.34759/trd-2022-123-07
[research_kornilov_2006]: https://doi.org/10.1134/s0869864306040032
[research_korsun_poplavsky_2024]: https://doi.org/10.31857/s0002338824030066
[research_korthauer_accorinti_2023]: https://doi.org/10.2514/1.j061915
[research_kostic_mitrovic_2002]: https://doi.org/10.2514/6.2002-545
[research_kothari_anderson_1987]: https://doi.org/10.2514/3.45477
[research_kouchi_yamaguchi_2017]: https://doi.org/10.2514/6.2017-0265
[research_kousen_bendiksen_1994]: https://doi.org/10.2514/3.46644
[research_koziel_leifsson_2011]: https://doi.org/10.2514/6.2011-3177
[research_kraft_1974]: https://doi.org/10.21236/ada000922
[research_kraft_lo_1977]: https://doi.org/10.2514/3.60654
[research_kraft_parker_1979]: https://doi.org/10.21236/ada076555
[research_kraftchristophercjr_mathewscharlesw_1950]: https://ntrs.nasa.gov/citations/19930086168
[research_krahn_1955]: https://doi.org/10.21236/ad0075314
[research_kraiko_1987]: https://doi.org/10.1016/0021-8928(87)90131-6
[research_kraiko_pudovikov_1998]: https://doi.org/10.1007/bf02698225
[research_kraiko_shapovalov_2022]: https://doi.org/10.1134/s0015462822040073
[research_kraiko_shelomovskii_1984]: https://doi.org/10.1007/bf01090918
[research_kraiko_tilliaeva_1973]: https://doi.org/10.1016/0021-8928(73)90088-9
[research_kraiko_tillyaeva_2025]: https://doi.org/10.1134/s0015462824604716
[research_kraiko_tkalenko_1967]: https://doi.org/10.1007/bf01019533
[research_kraljic_rusak_2021]: https://doi.org/10.2514/1.j060139
[research_krener_2001]: https://doi.org/10.21236/ada430327
[research_krenz_1979]: https://doi.org/10.2514/6.1979-692
[research_krishnan_sandham_2007]: https://doi.org/10.1063/1.2432158
[research_kristenkallstrom]: https://ntrs.nasa.gov/citations/20220000003
[research_krivec_ling_1984]: https://doi.org/10.4271/841539
[research_krogmann_stanewsky_1984]: https://doi.org/10.2514/6.1984-98
[research_krogmann_stanewsky_1985]: https://doi.org/10.2514/3.45077
[research_kronejr_1980]: https://doi.org/10.2514/6.1980-3047
[research_kronejr_1980_b]: https://doi.org/10.2514/6.1980-1882
[research_kroos_1995]: https://doi.org/10.2514/6.1995-2642
[research_krothapalli_alvi_2003]: https://doi.org/10.21236/ada414914
[research_kruiswyk_dutton_1989]: https://doi.org/10.2514/6.1989-210
[research_krupovage_1978]: https://doi.org/10.2514/6.1978-807
[research_kruse_wunderlich_2012]: https://doi.org/10.2514/6.2012-3208
[research_krynytzky_2001]: https://doi.org/10.2514/6.2001-161
[research_krynytzky_2004]: https://doi.org/10.2514/6.2004-2310
[research_krynytzky_hergert_2002]: https://doi.org/10.2514/6.2002-2782
[research_krynytzky_johnsen_2010]: https://doi.org/10.2514/6.2010-4341
[research_kryvokhatko_masko_2018]: https://doi.org/10.5772/intechopen.70228
[research_krzywoblocki_1943]: https://doi.org/10.2514/8.11023
[research_kubo_2018]: https://doi.org/10.2514/6.2018-0297
[research_kuchemann_1957]: https://doi.org/10.1017/s0368393100130536
[research_kuchemann_1962]: https://doi.org/10.1016/b978-0-08-006550-2.50019-3
[research_kuhlae_littlemv_1958]: https://ntrs.nasa.gov/citations/19660030327
[research_kuhlman_cerney_1988]: https://doi.org/10.2514/6.1988-7
[research_kuhn_wardwell_1993]: https://doi.org/10.2514/6.1993-4816
[research_kukreja_2008]: https://doi.org/10.2514/1.32799
[research_kula_aslangil_2025]: https://doi.org/10.2514/6.2025-3533
[research_kulfan_2002]: https://doi.org/10.2514/6.2002-2839
[research_kulfan_2008]: https://doi.org/10.2514/6.2008-132
[research_kulfan_2009]: https://doi.org/10.2514/1.42823
[research_kumada_sawada_2016]: https://doi.org/10.2514/6.2016-1346
[research_kumar_das_1989]: https://doi.org/10.1007/978-3-642-83584-1_26
[research_kumar_sunil_2021]: https://doi.org/10.1007/978-981-15-9601-8_13
[research_kumar_viswanath_2001]: https://doi.org/10.2514/6.2001-582
[research_kumar_viswanath_2002]: https://doi.org/10.2514/2.3826
[research_kumaravel_jeyajothiraj_2015]: https://doi.org/10.15866/irease.v8i2.6036
[research_kumawat_kumar_2025]: https://doi.org/10.1007/s12046-025-02857-0
[research_kummer_allred_2012]: https://doi.org/10.2514/6.2012-3702
[research_kuntavanish_cancel_1983]: https://doi.org/10.2514/6.1983-2761
[research_kuntz_amatucci_1986]: https://doi.org/10.2514/6.1986-348
[research_kurade_venkatakrishnan_2021]: https://doi.org/10.1017/aer.2021.99
[research_kurbatskii_montanari_2006]: https://doi.org/10.2514/6.2006-661
[research_kurosaka_chou_1981]: https://doi.org/10.2514/6.1981-275
[research_kurus_takahashi_2021]: https://doi.org/10.2514/6.2021-2432
[research_kussoymi_horstmankc_1992]: https://ntrs.nasa.gov/citations/19930015348
[research_kusunose_crowder_1999]: https://doi.org/10.2514/6.1999-275
[research_kusunose_marcum_1987]: https://doi.org/10.2514/6.1987-1196
[research_kutlerp_lomaxh_1971]: https://ntrs.nasa.gov/citations/19710055606
[research_kutney_piszkin_1963]: https://doi.org/10.2514/6.1963-276
[research_kutney_piszkin_1964]: https://doi.org/10.2514/3.43551
[research_kuwahara_1987]: https://doi.org/10.2514/6.1987-37
[research_kuya_boda_2020]: https://doi.org/10.2514/1.c035902
[research_kuzmin_2005]: https://doi.org/10.1142/9789812703187_0013
[research_kuzmin_2006]: https://doi.org/10.1007/s10697-006-0081-4
[research_kuzmin_2007]: https://doi.org/10.1007/978-3-540-75995-9_64
[research_kuzmin_2009]: https://doi.org/10.1016/j.compfluid.2008.01.017
[research_kuzmin_2010]: https://doi.org/10.1142/9789814313377_0022
[research_kuzmin_2013]: https://doi.org/10.5139/ijass.2013.14.3.210
[research_kuzmin_babarykin_2023]: https://doi.org/10.1063/5.0177488
[research_kuzmin_shilkin_2009]: https://doi.org/10.1007/978-3-540-92779-2_134
[research_kuzmina_ishmuratov_2018]: https://doi.org/10.1016/j.trpro.2018.02.017
[research_kwak_yoshida_2006]: https://doi.org/10.2514/6.2006-3483
[research_kwon_park_2005]: https://doi.org/10.2514/6.2005-2294
[research_kwon_vepa_2022]: https://doi.org/10.1177/10775463211052370
[research_kwon_vepa_2022_b]: https://doi.org/10.1017/aer.2022.5
[research_kyle_orourke_2001]: https://doi.org/10.2514/6.2001-2856
[research_kyser_1956]: https://doi.org/10.21236/ad0412378
[research_laar_atherstone_2024]: https://doi.org/10.2514/6.2024-2669
[research_labbesteveng_gilbertmichaelg_2009]: https://ntrs.nasa.gov/citations/20090033116
[research_lacerdamontes_alves_2025]: https://doi.org/10.26678/abcm.cobem2023.cob2023-1895
[research_lacey_1979]: https://doi.org/10.21236/ada085065
[research_lacy_sclafani_2016]: https://doi.org/10.2514/6.2016-0308
[research_lada_kontis_2009]: https://doi.org/10.1007/978-3-540-85181-3_76
[research_lada_kontis_2011]: https://doi.org/10.2514/1.c031174
[research_laderman_1979]: https://doi.org/10.21236/ada070254
[research_ladsoncharlesl_hillacquillas_1987]: https://ntrs.nasa.gov/citations/19880009181
[research_ladsoncharlesl_hillsacquilla_1987]: https://ntrs.nasa.gov/citations/19880009187
[research_ladsoncl_1973]: https://ntrs.nasa.gov/citations/19730014612
[research_ladsoncl_1975]: https://ntrs.nasa.gov/citations/19760004992
[research_ladsoncl_rayej_1984]: https://ntrs.nasa.gov/citations/19840019596
[research_lafferty_marren_1996]: https://doi.org/10.21236/ada329697
[research_lagemann_2024]: https://doi.org/10.52843/cassyni.p1bbsw
[research_lagemann_brunton_2024]: https://doi.org/10.1038/s41467-024-49361-3
[research_lagemann_mateling_2022]: https://doi.org/10.55037/lxlaser.20th.83
[research_lagennicholast_seinerjohnm_1990]: https://ntrs.nasa.gov/citations/19900016329
[research_lahmili_bouchaala_2026]: https://doi.org/10.2514/1.c039028
[research_lai_zhang_2014]: https://doi.org/10.2514/6.2014-1200
[research_laitone_1951]: https://doi.org/10.2514/8.1951
[research_lamah_harris_1983]: https://doi.org/10.2514/6.1983-884
[research_lamy_1983]: https://doi.org/10.2514/6.1983-2736
[research_lan_hsu_1995]: https://doi.org/10.2514/6.1995-3442
[research_lan_luo_1994]: https://doi.org/10.2514/6.1994-3455
[research_lancedward_1989]: https://ntrs.nasa.gov/citations/19890015835
[research_landahl_1959]: https://doi.org/10.1016/b978-1-4831-9832-3.50015-2
[research_landahl_rubbert_1966]: https://doi.org/10.2514/6.1966-90
[research_landahl_widnall_1979]: https://doi.org/10.21236/ada065667
[research_landahl_widnall_1980]: https://doi.org/10.21236/ada215086
[research_landahl_widnall_1981]: https://doi.org/10.21236/ada215124
[research_landahl_widnall_1982]: https://doi.org/10.21236/ada214846
[research_landers_landrum_1997]: https://doi.org/10.2514/6.1997-2248
[research_lapshina_ostapenko_2009]: https://doi.org/10.1134/s1028335809010108
[research_large_1981]: https://doi.org/10.1017/s0001924000030062
[research_larson_1984]: https://doi.org/10.2514/6.1984-2147
[research_larsonterryj_whitmorestephena_1987]: https://ntrs.nasa.gov/citations/19870020064
[research_larsontj_siemerspmiii_1980]: https://ntrs.nasa.gov/citations/19800023881
[research_lasauskas_2005]: https://doi.org/10.3846/16487788.2005.9635906
[research_lashkov_karpenko_2016]: https://doi.org/10.1063/1.4949524
[research_lassiter_1981]: https://doi.org/10.3397/1.2832189
[research_laster_stanewsky_1998]: https://doi.org/10.2514/6.1998-2878
[research_lathame_gawienowskij_1977]: https://ntrs.nasa.gov/citations/19770017116
[research_latif_masud_2006]: https://doi.org/10.2514/6.2006-1385
[research_latif_masud_2007]: https://doi.org/10.2514/1.22775
[research_lauchle_1974]: https://doi.org/10.2514/3.62987
[research_lauer_ansell_2022]: https://doi.org/10.2514/6.2022-3662
[research_laughrey_1975]: https://doi.org/10.2514/6.1975-1292
[research_lautenwtjr_lundstromrr_1954]: https://ntrs.nasa.gov/citations/19630003991
[research_lavala_das_2025]: https://doi.org/10.1134/s0015462824604741
[research_law_1975]: https://doi.org/10.21236/ada014738
[research_lawing_johnson_1986]: https://doi.org/10.2514/6.1986-745
[research_lawingpl_kilgorera_1981]: https://ntrs.nasa.gov/citations/19810022594
[research_layukallo_nakamura_1999]: https://doi.org/10.2514/6.1999-3413
[research_leballeur_girodrouxlavigne_1989]: https://doi.org/10.1007/978-3-642-83584-1_4
[research_lederer_1994]: https://doi.org/10.21236/ada289934
[research_lednicer_roncz_1989]: https://doi.org/10.2514/6.1989-2203
[research_lee_1980]: https://doi.org/10.21236/ada091906
[research_lee_1981]: https://doi.org/10.21236/ada098822
[research_lee_1983]: https://doi.org/10.2514/6.1983-264
[research_lee_1990]: https://doi.org/10.2514/3.25144
[research_lee_1990_b]: https://doi.org/10.1017/s0001924000022752
[research_lee_1993]: https://doi.org/10.2514/6.1993-3481
[research_lee_2000]: https://doi.org/10.1016/s0376-0421(00)00003-8
[research_lee_2001]: https://doi.org/10.1016/s0376-0421(01)00003-3
[research_lee_2008]: https://doi.org/10.1299/jfst.3.195
[research_lee_2012]: https://doi.org/10.6112/kscfe.2012.17.4.093
[research_lee_2026]: https://doi.org/10.1007/s42405-026-01257-w
[research_lee_damodaran_2000]: https://doi.org/10.2514/6.2000-782
[research_lee_damodaran_2001]: https://doi.org/10.2514/6.2001-265
[research_lee_eyi_1991]: https://doi.org/10.2514/6.1991-3287
[research_lee_eyi_1993]: https://doi.org/10.2514/3.46419
[research_lee_gross_2022]: https://doi.org/10.2514/6.2022-3988
[research_lee_jin_1988]: https://doi.org/10.1007/978-3-642-61381-4_413
[research_lee_lee_2006]: https://doi.org/10.5139/ijass.2006.7.2.121
[research_lee_ohman_1984]: https://doi.org/10.2514/3.44987
[research_lee_park_2017]: https://doi.org/10.5139/jksas.2017.45.7.531
[research_lee_rusak_1999]: https://doi.org/10.2514/6.1999-3189
[research_lee_rusak_2000]: https://doi.org/10.2514/6.2000-2460
[research_lee_sim_2020]: https://doi.org/10.1007/s42405-020-00279-2
[research_lee_tang_1989]: https://doi.org/10.2514/3.45785
[research_leelavathi_subramanian_1969]: https://doi.org/10.2514/3.5348
[research_lees_1956]: https://doi.org/10.2514/8.6977
[research_lees_reshotko_1962]: https://doi.org/10.21236/ad0288100
[research_lefebvre_dano_2013]: https://doi.org/10.2514/6.2013-490
[research_lefebvre_dano_2016]: https://doi.org/10.2514/1.c033113
[research_lefebvre_zha_2014]: https://doi.org/10.2514/6.2014-0195
[research_lefebvre_zha_2014_b]: https://doi.org/10.2514/6.2014-2683
[research_leger_poggie_2014]: https://doi.org/10.2514/6.2014-0951
[research_lehman_stearman_1977]: https://doi.org/10.21236/ada039245
[research_lei_zhang_2025]: https://doi.org/10.1134/s0869864324060222
[research_lemley_mullans_1973]: https://doi.org/10.2514/6.1973-311
[research_lemley_mullans_1974]: https://doi.org/10.2514/3.60344
[research_lempert_1975]: https://doi.org/10.21236/ada004190
[research_lensi_2000]: https://doi.org/10.2514/6.2000-3901
[research_leonardhwayne_1982]: https://ntrs.nasa.gov/citations/19890068685
[research_lepicovsky_ahuja_1986]: https://doi.org/10.2514/6.1986-1941
[research_leprovost_he_2018]: https://doi.org/10.2514/6.2018-0326
[research_lester_gragston_2021]: https://doi.org/10.1364/ao.433085
[research_lester_gragston_2022]: https://doi.org/10.2514/6.2022-1165
[research_level_flight_2003]: https://doi.org/10.2514/5.9781600861840.0083.0096
[research_levin_fabish_1962]: https://doi.org/10.21236/ad0298671
[research_levinsky_thommen_1968]: https://doi.org/10.21236/ad0680969
[research_levy_1992]: https://doi.org/10.2514/6.1992-4193
[research_levy_shamroth_1977]: https://doi.org/10.21236/ada040843
[research_levylljr_1977]: https://ntrs.nasa.gov/citations/19770054177
[research_levylljr_1981]: https://ntrs.nasa.gov/citations/19810010216
[research_lewis_neel_1964]: https://doi.org/10.21236/ad0600469
[research_ley_1936]: https://doi.org/10.1108/eb030095
[research_li_1977]: https://doi.org/10.2514/6.1977-168
[research_li_2015]: https://doi.org/10.2514/6.2015-2581
[research_li_2023]: https://doi.org/10.54254/2755-2721/12/20230331
[research_li_2024]: https://doi.org/10.61173/02vmsx61
[research_li_cai_2016]: https://doi.org/10.1109/ccdc.2016.7531202
[research_li_choudhari_2021]: https://doi.org/10.2514/6.2021-2905
[research_li_ekici_2018]: https://doi.org/10.2514/1.j056969
[research_li_geiselhart_2021]: https://doi.org/10.2514/1.j059237
[research_li_han_2026]: https://doi.org/10.1063/5.0326169
[research_li_he_2025]: https://doi.org/10.1016/j.jcp.2025.114158
[research_li_hirota_2016]: https://doi.org/10.1007/s00193-016-0637-0
[research_li_huyse_2002]: https://doi.org/10.1007/s00158-002-0212-4
[research_li_krist_2004]: https://doi.org/10.2514/6.2004-4629
[research_li_krist_2006]: https://doi.org/10.2514/1.13921
[research_li_li_2000]: https://doi.org/10.2514/2.2621
[research_li_lin_2022]: https://doi.org/10.1109/tim.2022.3162267
[research_li_qin_2020]: https://doi.org/10.2514/1.c035696
[research_li_wang_2020]: https://doi.org/10.1155/2020/5812129
[research_li_wen_2026]: https://doi.org/10.1109/tie.2025.3603058
[research_li_yang_2024]: https://doi.org/10.1109/dasc62030.2024.10749356
[research_li_yu_2023]: https://doi.org/10.1016/j.oceaneng.2023.114909
[research_li_zhang_2023]: https://doi.org/10.1063/5.0130176
[research_li_zhang_2024]: https://doi.org/10.2514/1.j063387
[research_li_zhang_2025]: https://doi.org/10.1051/jnwpu/20254350888
[research_liang_fu_1991]: https://doi.org/10.2514/6.1991-3213
[research_liangsm_fungky_1985]: https://ntrs.nasa.gov/citations/19850058558
[research_licher_1956]: https://doi.org/10.2514/8.3718
[research_liebeck_1971]: https://doi.org/10.21236/ad0737126
[research_liebeck_1989]: https://doi.org/10.1007/978-3-642-84010-4_23
[research_liebhardt_2019]: https://doi.org/10.2514/6.2019-3387
[research_liebhardt_2021]: https://doi.org/10.2514/6.2021-3188
[research_liebhardt_2025]: https://doi.org/10.2514/6.2025-3267
[research_lifshitz_solnstev_1996]: https://doi.org/10.2514/6.1996-1981
[research_lift_drag_ratios_1962]: https://doi.org/10.1017/s0001925900002274
[research_lift_effect_1980]: https://doi.org/10.2514/3.44692
[research_lighthill_1956]: https://doi.org/10.1017/s0022112056000196
[research_lijewski_1978]: https://doi.org/10.21236/ada070919
[research_lijewski_1987]: https://doi.org/10.2514/6.1987-2273
[research_lijewski_1988]: https://doi.org/10.2514/3.26018
[research_lijewski_1993]: https://doi.org/10.2514/6.1993-3023
[research_lin_1982]: https://doi.org/10.2514/6.1982-366
[research_lin_1982_b]: https://doi.org/10.2514/6.1982-1326
[research_lin_2025]: https://doi.org/10.5220/0014773000004818
[research_lin_2025_b]: https://doi.org/10.2139/ssrn.5228262
[research_lin_chieng_1997]: https://doi.org/10.2514/6.1997-725
[research_lin_wang_2026]: https://doi.org/10.1038/s41598-026-35265-3
[research_lindley_1956]: https://doi.org/10.1214/aoms/1177728069
[research_lindseyai_milammd_1974]: https://ntrs.nasa.gov/citations/19750007652
[research_lindseywalterf_1954]: https://ntrs.nasa.gov/citations/19930093724
[research_lindseywf_1946]: https://ntrs.nasa.gov/citations/19930092792
[research_linearized_theory_1986]: https://doi.org/10.1016/b978-0-444-87958-5.50005-4
[research_liou_huang_2000]: https://doi.org/10.1016/s0045-7930(99)00010-9
[research_liou_sajben_1980]: https://doi.org/10.2514/6.1980-195
[research_littlebhjr_cubbagejamesjjr_1961]: https://ntrs.nasa.gov/citations/19980227798
[research_litwhiler]: https://doi.org/10.18260/1-2--3345
[research_liu_1983]: https://doi.org/10.2514/6.1983-261
[research_liu_1998]: https://doi.org/10.1016/b978-008043319-6/50045-5
[research_liu_2022]: https://doi.org/10.1007/978-981-19-4586-1_13
[research_liu_2023]: https://doi.org/10.54097/hset.v37i.6084
[research_liu_chen_2024]: https://doi.org/10.3390/app14219628
[research_liu_dong_2019]: https://doi.org/10.1007/978-3-030-29688-9_13
[research_liu_fung_1985]: https://doi.org/10.2514/6.1985-4058
[research_liu_gao_2020]: https://doi.org/10.1007/s40435-020-00694-z
[research_liu_han_2022]: https://doi.org/10.1016/j.ast.2022.107636
[research_liu_li_2023]: https://doi.org/10.1063/5.0158003
[research_liu_liu_2023]: https://doi.org/10.3390/aerospace10100903
[research_liu_luo_2017]: https://doi.org/10.1016/j.taml.2017.09.011
[research_liu_mignolet_2005]: https://doi.org/10.21236/ada439001
[research_liu_mirels_1980]: https://doi.org/10.21236/ada084435
[research_liu_pang_2023]: https://doi.org/10.1016/j.measurement.2023.113165
[research_liu_peng_2026]: https://doi.org/10.3390/aerospace13090797
[research_liu_platzer_1970]: https://doi.org/10.2514/6.1970-190
[research_liu_salazar_2021]: https://doi.org/10.1007/s00348-021-03305-5
[research_liu_salazar_2022]: https://doi.org/10.1007/s00193-022-01102-5
[research_liu_singh_1995]: https://doi.org/10.2514/6.1995-3293
[research_liu_squire_1986]: https://doi.org/10.1007/978-3-642-82770-9_8
[research_liu_tao_2012]: https://doi.org/10.1109/isdea.2012.624
[research_liu_wang_2012]: https://doi.org/10.1016/j.proeng.2012.01.998
[research_liu_wang_2016]: https://doi.org/10.2514/6.2016-4386
[research_liu_yang_2016]: https://doi.org/10.1080/19942060.2016.1210029
[research_liu_yang_2016_b]: https://doi.org/10.2514/6.2016-3980
[research_liu_yang_2017]: https://doi.org/10.2514/6.2017-4362
[research_liu_zha_2016]: https://doi.org/10.2514/6.2016-3472
[research_liu_zhao_2016]: https://doi.org/10.1155/2016/7673146
[research_ljamesrunyan_louislsteers_1980]: https://ntrs.nasa.gov/citations/19810042099
[research_ljungskog_sebben_2019]: https://doi.org/10.4271/2019-01-0656
[research_lleblein_stockman_1972]: https://doi.org/10.2514/3.58977
[research_lo_1969]: https://doi.org/10.2514/3.5585
[research_lo_1972]: https://doi.org/10.2514/3.50149
[research_lo_1974]: https://doi.org/10.21236/ad0785349
[research_lo_glassman_1975]: https://doi.org/10.21236/ada017706
[research_lo_oliver_1970]: https://doi.org/10.21236/ad0704123
[research_lo_qian_1995]: https://doi.org/10.2514/6.1995-794
[research_lo_ulbrich_1991]: https://doi.org/10.2514/6.1991-400
[research_loads_flutter_conf_1957]: https://ntrs.nasa.gov/citations/19710070068
[research_lock_1961]: https://doi.org/10.1017/s0001925900001980
[research_lock_1964]: https://doi.org/10.1007/978-3-642-88337-8_18
[research_lock_bridgewater_1967]: https://doi.org/10.1016/0376-0421(67)90004-8
[research_lock_rogers_1962]: https://doi.org/10.1016/b978-0-08-006550-2.50020-x
[research_lockheedgeorgiacomarietta_1969]: https://doi.org/10.21236/ad0700436
[research_loewner_2013]: https://doi.org/10.1016/b978-1-4832-3272-0.50028-4
[research_loftinlaurencek_cohenkenneths_1948]: https://ntrs.nasa.gov/citations/19930082303
[research_lokos_lizotte_2005]: https://doi.org/10.2514/6.2005-6315
[research_lokos_olney_2002]: https://doi.org/10.2514/6.2002-2926
[research_lomax_heaslet_1956]: https://doi.org/10.2514/8.3731
[research_lombardi_morelli_1995]: https://doi.org/10.2514/3.46748
[research_lombardi_salvetti_1997]: https://doi.org/10.2514/6.1997-1838
[research_lombardi_salvetti_2003]: https://doi.org/10.2514/2.3163
[research_long_1990]: https://doi.org/10.2514/6.1990-1419
[research_long_2003]: https://doi.org/10.2514/6.2003-3100
[research_long_2006]: https://doi.org/10.2514/1.5236
[research_long_gladen_1988]: https://doi.org/10.2514/6.1988-2063
[research_longitudinal_accel_1953]: https://ntrs.nasa.gov/citations/19930087532
[research_longitudinal_control_2003]: https://doi.org/10.2514/5.9781600861840.0275.0284
[research_longitudinal_trim_2016]: https://doi.org/10.1201/b15956-7
[research_lopezlopez_haramurabastos_2026]: https://doi.org/10.2514/6.2026-4551
[research_lorberpeterf_cartafranklino_1989]: https://ntrs.nasa.gov/citations/19890009889
[research_lord_eminton_1954]: https://doi.org/10.2514/8.3128
[research_loth_lee_2008]: https://doi.org/10.21236/ada478600
[research_loupy_barakos_2017]: https://doi.org/10.2514/6.2017-3252
[research_loveje_youngwr_1966]: https://ntrs.nasa.gov/citations/19670032612
[research_lovingdonaldl_1961]: https://ntrs.nasa.gov/citations/19980227277
[research_lovingdonaldl_1961_b]: https://ntrs.nasa.gov/citations/20040008071
[research_low_drag_1980]: https://doi.org/10.2514/5.9781600865466.0212.0232
[research_lowry_smith_2001]: https://doi.org/10.21236/ada387335
[research_lu_braun_2012]: https://doi.org/10.1007/978-3-642-25688-2_73
[research_lu_pan_1995]: https://doi.org/10.2514/3.12633
[research_lu_yeh_1993]: https://doi.org/10.2514/6.1993-3285
[research_luber_2018]: https://doi.org/10.2514/6.2018-3643
[research_lucchi_1983]: https://doi.org/10.2514/6.1983-1884
[research_luchuk_1957]: https://doi.org/10.21236/ad0151668
[research_luckert_1973]: https://doi.org/10.2514/6.1973-295
[research_luckring_2003]: https://doi.org/10.2514/6.2003-753
[research_luckring_hiller_2025]: https://doi.org/10.2514/6.2025-2018
[research_luers_fiscus_1984]: https://doi.org/10.21236/ada139566
[research_lufrankk_settlesgarys_1989]: https://ntrs.nasa.gov/citations/19890054707
[research_lugo_tolson_2014]: https://doi.org/10.2514/6.2014-0388
[research_luh_mack_1984]: https://doi.org/10.2514/6.1984-255
[research_lumley_1986]: https://doi.org/10.21236/ada177609
[research_lundry_1967]: https://doi.org/10.2514/3.43797
[research_lundstromreginaldr_lautenwilliamtjr_1948]: https://ntrs.nasa.gov/citations/19930085467
[research_luo_1987]: https://doi.org/10.2514/6.1987-2613
[research_luo_2024]: https://doi.org/10.54097/02a7ej10
[research_luo_bao_1988]: https://doi.org/10.2514/3.45620
[research_luo_tang_2024]: https://doi.org/10.20944/preprints202409.0973.v1
[research_luo_wang_1997]: https://doi.org/10.2514/6.1997-2242
[research_luo_wang_1998]: https://doi.org/10.2514/2.2257
[research_luo_wang_1998_b]: https://doi.org/10.1016/s0045-7825(98)00112-1
[research_luomaarvoa_1954]: https://ntrs.nasa.gov/citations/20090023318
[research_lurkens_meinke_2026]: https://doi.org/10.2514/6.2026-4698
[research_luther_1957]: https://doi.org/10.2514/8.3910
[research_lutsenko_serikbay_2017]: https://doi.org/10.1088/1757-899x/234/1/012016
[research_lutz_kleinert_2023]: https://doi.org/10.2514/1.c036829
[research_luxdp_1978]: https://ntrs.nasa.gov/citations/19790011831
[research_ly_gear_2006]: https://doi.org/10.21914/anziamj.v47i0.1046
[research_ly_norrison_2010]: https://doi.org/10.21914/anziamj.v51i0.2658
[research_lykins_keshmiri_2010]: https://doi.org/10.2514/6.2010-7648
[research_lynch_fancher_1983]: https://doi.org/10.2514/6.1983-1421
[research_lynde_campbell_2017]: https://doi.org/10.2514/6.2017-3058
[research_lyons_wc_1961]: https://doi.org/10.21236/ad0271681
[research_lyrintzis_wissink_1992]: https://doi.org/10.2514/3.11263
[research_m_2026]: https://doi.org/10.36227/techrxiv.176827253.34525913/v1
[research_ma_2025]: https://doi.org/10.5220/0014450700004861
[research_ma_gao_2024]: https://doi.org/10.1016/j.ast.2024.109649
[research_ma_li_2024]: https://doi.org/10.2514/1.j064239
[research_ma_wang_2016]: https://doi.org/10.2514/6.2016-3575
[research_ma_yu_2024]: https://doi.org/10.1063/5.0241388
[research_mabey_1989]: https://doi.org/10.2514/3.45805
[research_mabey_lee_1986]: https://doi.org/10.1007/978-3-642-82770-9_28
[research_mabeydg_boydenrp_1992]: https://ntrs.nasa.gov/citations/19930002422
[research_mabeydg_boydenrp_1995]: https://ntrs.nasa.gov/citations/19950059152
[research_macallister_1955]: https://doi.org/10.21236/ad0062045
[research_maccormackrw_1971]: https://ntrs.nasa.gov/citations/19710055623
[research_macdonald_alonso_2020]: https://doi.org/10.2514/6.2020-1295
[research_mace_adamsonjr_1985]: https://doi.org/10.2514/6.1985-369
[research_mach_number_2022]: https://doi.org/10.15394/eaglepub.2022.1066.n13
[research_macha_1977]: https://doi.org/10.2514/3.58828
[research_machado_chau_2024]: https://doi.org/10.2514/6.2024-3767
[research_machida_kikuchi_2005]: https://doi.org/10.2514/6.2005-835
[research_mack_1979]: https://doi.org/10.2514/6.1979-264
[research_mack_1989]: https://doi.org/10.1007/978-3-642-83584-1_18
[research_madden_2010]: https://doi.org/10.2514/6.2010-7919
[research_madson_talbot_1996]: https://doi.org/10.2514/6.1996-2454
[research_maeder_1964]: https://doi.org/10.1007/978-3-642-88337-8_9
[research_maeder_hall_1955]: https://doi.org/10.21236/ada951947
[research_maewal_1984]: https://doi.org/10.21236/ada149071
[research_maeyama_asada_2026]: https://doi.org/10.2514/6.2026-4445
[research_magnetohydrodynamic_transonic_1990]: https://doi.org/10.1142/9789814439220_0008
[research_magnus_yoshihara_1975]: https://doi.org/10.2514/6.1975-98
[research_mahalingesh]: https://doi.org/10.70675/7ef0dd42z798ez4c52z8d9cz7c6c30678d23
[research_mahalingesh_piponniau_2023]: https://doi.org/10.2514/6.2023-0093
[research_mai_2025]: https://doi.org/10.36838/v7i6.53
[research_maines_smith_2007]: https://doi.org/10.2514/6.2007-878
[research_maintenance_of]: https://doi.org/10.4271/air975b
[research_mair_1965]: https://doi.org/10.1017/s0001925900003589
[research_majdalani_maicke_2010]: https://doi.org/10.2514/6.2010-6844
[research_makeich_kryukov_2018]: https://doi.org/10.1088/1742-6596/1009/1/012009
[research_maklakov_2001]: https://doi.org/10.1134/1.1401226
[research_makowski_1964]: https://doi.org/10.2514/6.1964-635
[research_maksymiuk_pulliam_1987]: https://doi.org/10.2514/6.1987-415
[research_maksymiukcm_watsonvikensa_1986]: https://ntrs.nasa.gov/citations/19860000153
[research_malaek_izadi_2006]: https://doi.org/10.2514/1.13197
[research_maldonado_housman_2024]: https://doi.org/10.2514/6.2024-3639
[research_malik_li_1993]: https://doi.org/10.2514/6.1993-77
[research_maljevic_dinulovic_2024]: https://doi.org/10.5937/oteh24007m
[research_malkocoglu_barada_2020]: https://doi.org/10.2514/6.2020-2759
[research_mallik_kapania_2013]: https://doi.org/10.2514/6.2013-1454
[research_mallozzi_depaolis_2014]: https://doi.org/10.1007/978-3-319-11541-2_26
[research_malmuth_1984]: https://doi.org/10.2514/6.1984-1625
[research_malmuth_1987]: https://doi.org/10.1017/s0022112087000831
[research_malmuth_cole_1984]: https://doi.org/10.21236/ada141431
[research_malmuth_jafroudi_1993]: https://doi.org/10.2514/3.11703
[research_malmuth_wu_1983]: https://doi.org/10.2514/6.1983-184
[research_malmuth_wu_1984]: https://doi.org/10.2514/3.48256
[research_malmuth_wu_1985]: https://doi.org/10.2514/6.1985-478
[research_malmuth_wu_1986]: https://doi.org/10.2514/6.1986-1798
[research_malmuth_wu_1987]: https://doi.org/10.2514/3.45417
[research_malone_sankar_1984]: https://doi.org/10.2514/6.1984-1566
[research_malvestudofranks_cooneythomasv_1957]: https://ntrs.nasa.gov/citations/19930089925
[research_mani_rider_2010]: https://doi.org/10.2514/6.2010-4221
[research_manisankar_verma_2023]: https://doi.org/10.1007/s00193-023-01129-2
[research_manjith_2026]: https://doi.org/10.2514/6.2026-111390
[research_mann_campbell_1983]: https://doi.org/10.2514/6.1983-1859
[research_mann_mercer_1985]: https://doi.org/10.2514/6.1985-4069
[research_mann_mercer_1986]: https://doi.org/10.2514/3.56774
[research_manneschmidt_ligrani_2024]: https://doi.org/10.1007/s00193-024-01202-4
[research_manning_gleason_1992]: https://doi.org/10.2514/6.1992-4425
[research_mannmj_1979]: https://ntrs.nasa.gov/citations/19790008633
[research_manokaran_vidya_2003]: https://doi.org/10.2514/6.2003-1253
[research_manwell_1977]: https://doi.org/10.1080/00036817708839171
[research_mao_jing_2023]: https://doi.org/10.3390/aerospace10100837
[research_mao_jing_2023_b]: https://doi.org/10.3390/aerospace10010040
[research_margoliskenneth_1947]: https://ntrs.nasa.gov/citations/19930082080
[research_marino_bonfiglioli_2012]: https://doi.org/10.1115/fedsm2012-72487
[research_marino_eberle_2025]: https://doi.org/10.2514/6.2025-0035
[research_marino_eberle_2026]: https://doi.org/10.2514/1.c038608
[research_marino_imperatore_2009]: https://doi.org/10.2514/6.2009-1485
[research_marion_sharma_2025]: https://doi.org/10.2514/6.2025-97857
[research_markherman_1958]: https://ntrs.nasa.gov/citations/20050019632
[research_markhotok_2021]: https://doi.org/10.5772/intechopen.86858
[research_marquardt_1976]: https://doi.org/10.21236/ada044956
[research_marsden_bogey_2005]: https://doi.org/10.2514/6.2005-2817
[research_marshallrt_schweikhardwg_1973]: https://ntrs.nasa.gov/citations/19730007281
[research_martin_2008]: https://doi.org/10.2514/6.2008-7337
[research_martin_2011]: https://doi.org/10.21236/ada547547
[research_martin_jackson_1994]: https://doi.org/10.2514/6.1994-3160
[research_martin_lomax_1974]: https://doi.org/10.2514/6.1974-11
[research_martindale_butler_1988]: https://doi.org/10.2514/6.1988-2014
[research_martinez_gennaro_2015]: https://doi.org/10.1016/j.piutam.2015.03.063
[research_martinpb_mcalisterkw_2003]: https://ntrs.nasa.gov/citations/20030069003
[research_martos_kiszely_2011]: https://doi.org/10.2514/6.2011-6669
[research_masdari_talebi_2018]: https://doi.org/10.24200/sci.2018.51306.2104
[research_maseland_laban_2006]: https://doi.org/10.2514/6.2006-3639
[research_masini_timme_2019]: https://doi.org/10.1017/jfm.2019.906
[research_masini_timme_2020]: https://doi.org/10.2514/1.j059219
[research_maskewb_1983]: https://ntrs.nasa.gov/citations/19840004044
[research_mason_1982]: https://doi.org/10.2514/6.1982-97
[research_mason_1993]: https://doi.org/10.2514/6.1993-649
[research_mason_1995]: https://doi.org/10.2514/6.1995-741
[research_mason_2013]: https://doi.org/10.2514/6.2013-4245
[research_mason_davila_2023]: https://doi.org/10.2514/6.2023-1321
[research_mason_inger_1975]: https://doi.org/10.2514/6.1975-831
[research_mason_lovejoy_2020]: https://doi.org/10.2514/6.2020-0474
[research_mason_mackenzie_1978]: https://doi.org/10.2514/6.1978-101
[research_massa_2014]: https://doi.org/10.1017/jfm.2014.495
[research_masson_veilleux_1998]: https://doi.org/10.2514/2.2365
[research_masson_veilleux_1999]: https://doi.org/10.2514/6.1999-3187
[research_masson_veilleux_1999_b]: https://doi.org/10.2514/6.1999-527
[research_masuda_yoshida_1991]: https://doi.org/10.2514/6.1991-3105
[research_mateer_bertelrud_1983]: https://doi.org/10.2514/6.1983-1725
[research_mateer_brosh_1976]: https://doi.org/10.2514/6.1976-161
[research_mateer_seegmiller_1987]: https://doi.org/10.2514/6.1987-1241
[research_matheny_panageas_1981]: https://doi.org/10.2514/6.1981-2433
[research_mathenynw_gatlindh_1978]: https://ntrs.nasa.gov/citations/19780012197
[research_mathur_carr_2004]: https://doi.org/10.2514/6.2004-2835
[research_matrangagenej_1961]: https://ntrs.nasa.gov/citations/20040047146
[research_matrangagenej_armisteadkatharineh_1958]: https://ntrs.nasa.gov/citations/19930089937
[research_matsui_1963]: https://doi.org/10.21236/ad0403496
[research_matsuno_lele_2020]: https://doi.org/10.2514/6.2020-0573
[research_matsushima_takanashi_1994]: https://doi.org/10.2514/6.1994-1864
[research_matsushima_takanashi_1996]: https://doi.org/10.2514/6.1996-2465
[research_matsushita_miyata]: https://doi.org/10.1109/phycon.2003.1236814
[research_matsushita_miyata_2003]: https://doi.org/10.1299/jsmehs.2003.40.259
[research_matsushita_miyata_b]: https://doi.org/10.1109/sice.2002.1195240
[research_matsushita_saitoh_1998]: https://doi.org/10.2514/6.1998-1728
[research_matthews_key_1977]: https://doi.org/10.2514/3.58821
[research_mavriplis_harris_1986]: https://doi.org/10.2514/6.1986-1796
[research_mavriplis_levy_2002]: https://doi.org/10.2514/6.2002-838
[research_mavriplis_levy_2005]: https://doi.org/10.2514/1.8233
[research_mavriplisdj_levydavidw_2001]: https://ntrs.nasa.gov/citations/20020019227
[research_maximum_allowable]: https://doi.org/10.4271/as418a
[research_maydew_1957]: https://doi.org/10.2172/4328733
[research_mayer_lutz_2019]: https://doi.org/10.2514/1.c034969
[research_mayerjohnp_valentinegeorgem_1950]: https://ntrs.nasa.gov/citations/19930086185
[research_mayerjohnp_valentinegeorgem_1950_b]: https://ntrs.nasa.gov/citations/19930086246
[research_mayerjohnp_valentinegeorgem_1951]: https://ntrs.nasa.gov/citations/19930086597
[research_mayes_lores_1970]: https://doi.org/10.2514/3.44207
[research_mayya_karnick_2022]: https://doi.org/10.2514/6.2022-4173
[research_mazumder_2024]: https://doi.org/10.21203/rs.3.rs-4706004/v1
[research_mazurov_takovitskii_2022]: https://doi.org/10.1134/s0015462822010074
[research_mcallister_1994]: https://doi.org/10.2514/6.1994-2609
[research_mccanlessgfjr_boonejr_1974]: https://ntrs.nasa.gov/citations/19750030313
[research_mccarthy_jackf_1955]: https://doi.org/10.21236/ad0110593
[research_mccarthy_johnf_1955]: https://doi.org/10.21236/ad0103035
[research_mcclain_pountney_1982]: https://doi.org/10.2514/6.1982-601
[research_mcconnell_2004]: https://doi.org/10.2514/6.2004-5048
[research_mcconnell_2006]: https://doi.org/10.2514/6.2006-3925
[research_mccroskeywj_1987]: https://ntrs.nasa.gov/citations/19880002254
[research_mcdearmonrussellw_1956]: https://ntrs.nasa.gov/citations/19930089379
[research_mcdevitt_levyjr_1975]: https://doi.org/10.2514/6.1975-878
[research_mcdonald_shamroth_1982]: https://doi.org/10.1016/b978-0-12-493280-7.50014-0
[research_mcelderry_1973]: https://doi.org/10.21236/ada377039
[research_mcfaddengb_1979]: https://ntrs.nasa.gov/citations/19790019965
[research_mcfalljohncjr_hollingerjamesa_1953]: https://ntrs.nasa.gov/citations/19930087467
[research_mcgann_1995]: https://doi.org/10.1117/12.211483
[research_mcintyre_bowersox_1998]: https://doi.org/10.2514/2.3410
[research_mcintyre_bowersox_1999]: https://doi.org/10.2514/6.1999-991
[research_mckinney_gloss_1982]: https://doi.org/10.2514/6.1982-604
[research_mclaren_jayashankar_2007]: https://doi.org/10.21236/ada479288
[research_mclean_1994]: https://doi.org/10.1049/cp:19940361
[research_mclean_matoi_1986]: https://doi.org/10.1007/978-3-642-82770-9_25
[research_mcnally_bachjr_1988]: https://doi.org/10.2514/6.1988-2134
[research_mcneillwatere_mcleanjohnd_1961]: https://ntrs.nasa.gov/citations/20040008111
[research_mcparlin_adamczak_2003]: https://doi.org/10.2514/6.2003-599
[research_mcvey_rejeske_1969]: https://doi.org/10.21236/ad0861763
[research_medanrt_magnusae_1981]: https://ntrs.nasa.gov/citations/19850002614
[research_medved_1990]: https://doi.org/10.2514/6.1990-1417
[research_medved_1993]: https://doi.org/10.1007/bf00191780
[research_mee_2001]: https://doi.org/10.2514/6.2001-208
[research_mehta_1986]: https://doi.org/10.2514/6.1986-346
[research_mehta_1988]: https://doi.org/10.2514/3.9845
[research_mehta_mehta_1997]: https://doi.org/10.2514/6.1997-2256
[research_meier_michel_1987]: https://doi.org/10.1007/978-3-642-82994-9_2
[research_meijering_schroeder_2001]: https://doi.org/10.2514/6.2001-2987
[research_mele_ostieri_2015]: https://doi.org/10.2514/6.2015-1272
[research_mele_ostieri_2017]: https://doi.org/10.2514/1.c034288
[research_mele_tognaccini_2016]: https://doi.org/10.2514/1.c033220
[research_melin_isikveren_2010]: https://doi.org/10.2514/1.c000197
[research_mellquist_bendiksen_2014]: https://doi.org/10.2514/6.2014-0674
[research_mellquist_bendiksen_2015]: https://doi.org/10.2514/6.2015-0443
[research_melnik_chow_1977]: https://doi.org/10.2514/6.1977-680
[research_melnik_ives_1973]: https://doi.org/10.2514/6.1973-660
[research_melnikre_grossmanb_1974]: https://ntrs.nasa.gov/citations/19740051585
[research_melsonnduane_streettcraigl_1993]: https://ntrs.nasa.gov/citations/19930000092
[research_memon_altman_2016]: https://doi.org/10.2514/6.2016-1847
[research_mendenhall_1980]: https://doi.org/10.2514/6.1980-1559
[research_meng_zhu_2024]: https://doi.org/10.1063/5.0217336
[research_mennellrc_1976]: https://ntrs.nasa.gov/citations/19760023185
[research_menon_skews_2009]: https://doi.org/10.1007/978-3-540-85181-3_32
[research_menshchikov_somov_2019]: https://doi.org/10.1063/1.5086976
[research_menzies_kandil_1995]: https://doi.org/10.2514/6.1995-1771
[research_menzies_kandil_1996]: https://doi.org/10.2514/6.1996-3391
[research_mercer_geller_1980]: https://doi.org/10.2514/6.1980-156
[research_mercerce_maidendl_1972]: https://ntrs.nasa.gov/citations/19720022360
[research_merceruio]: https://doi.org/10.33915/etd.291
[research_merienne_brion_2019]: https://doi.org/10.2514/6.2019-0025
[research_merriam_spaulding_1935]: https://doi.org/10.2514/8.129
[research_mertens_klevenhusen_1986]: https://doi.org/10.2514/6.1986-512
[research_mertens_klevenhusen_1987]: https://doi.org/10.2514/3.9703
[research_messiter_feo_1971]: https://doi.org/10.2514/3.6337
[research_messiteraf_adamsontcjr_1979]: https://ntrs.nasa.gov/citations/19790011875
[research_methods_for_2003]: https://doi.org/10.2514/5.9781600861840.0161.0168
[research_metzger_1997]: https://doi.org/10.21236/ada329681
[research_meyersjamesf_leejosephw_1992]: https://ntrs.nasa.gov/citations/20040121148
[research_michaelcandon_vincenzomuscarello]: https://ntrs.nasa.gov/citations/25937195111786
[research_michaeldbozeman_richardlcampbell]: https://ntrs.nasa.gov/citations/20230016470
[research_michaldavidh_mitchamgradyl_1949]: https://ntrs.nasa.gov/citations/20010062500
[research_miele_1955]: https://doi.org/10.2514/8.6736
[research_miele_1957]: https://doi.org/10.2514/8.3993
[research_mignosi_dor_1986]: https://doi.org/10.1007/978-3-642-82770-9_18
[research_mikhail_1989]: https://doi.org/10.2514/6.1989-332
[research_mikhail_1989_b]: https://doi.org/10.2514/6.1989-1820
[research_mikhalev_2008]: https://doi.org/10.1134/s0869864308030104
[research_miklos_ingram_1975]: https://doi.org/10.21236/ada014735
[research_miles_1950]: https://doi.org/10.2514/8.1568
[research_miles_1953]: https://doi.org/10.2514/8.2780
[research_miles_1954]: https://doi.org/10.2514/8.3162
[research_milholen_chokani_1994]: https://doi.org/10.2514/3.46593
[research_milholen_owens_2005]: https://doi.org/10.2514/6.2005-462
[research_milholenii_chokani_1992]: https://doi.org/10.2514/6.1992-4036
[research_milillo_1972]: https://doi.org/10.21236/ad0751461
[research_miller_1976]: https://doi.org/10.21236/ada030430
[research_miller_1983]: https://doi.org/10.2514/6.1983-1838
[research_miller_1985]: https://doi.org/10.2514/6.1985-75
[research_miller_jacques_2003]: https://doi.org/10.2514/6.2003-5407
[research_miller_ribbens_1999]: https://doi.org/10.2514/6.1999-637
[research_milligan_bailey_1963]: https://doi.org/10.21236/ad0295507
[research_mills_2004]: https://doi.org/10.2514/6.2004-1138
[research_milne_martos_2012]: https://doi.org/10.2514/6.2012-2855
[research_min_xian_2024]: https://doi.org/10.1108/mmms-11-2023-0376
[research_mineck_green_1990]: https://doi.org/10.2514/6.1990-1406
[research_mineckraymonde_1989]: https://ntrs.nasa.gov/citations/19890011589
[research_mineckraymonde_campbellrichardl_1993]: https://ntrs.nasa.gov/citations/19930064287
[research_mineckraymonde_campbellrichardl_1994]: https://ntrs.nasa.gov/citations/19950005763
[research_mineckraymonde_lawingpiercel_1987]: https://ntrs.nasa.gov/citations/19870014161
[research_minimum_drag_1962]: https://doi.org/10.1016/0016-0032(62)90867-0
[research_minimum_performance]: https://doi.org/10.4271/as8006
[research_minimum_performance_b]: https://doi.org/10.4271/as8006a
[research_miotto_wolf_2021]: https://doi.org/10.2514/6.2021-1652
[research_mirels_1977]: https://doi.org/10.21236/ada048445
[research_mirels_1986]: https://doi.org/10.21236/ada173715
[research_mironov_aniskin_2019]: https://doi.org/10.3390/mi10040235
[research_mironov_serdyuk_2012]: https://doi.org/10.1134/s0869864312020047
[research_mirowitzli_1975]: https://ntrs.nasa.gov/citations/19760003026
[research_miskin_takahashi_2019]: https://doi.org/10.2514/6.2019-3068
[research_mitchamgradyl_1949]: https://ntrs.nasa.gov/citations/20010062502
[research_mitchamgradyl_blanchardwillards_1952]: https://ntrs.nasa.gov/citations/20050029440
[research_mitchamgradyl_blanchardwillardsjr_1950]: https://ntrs.nasa.gov/citations/20050019416
[research_mitchamgradyl_blanchardwillardsjr_1951]: https://ntrs.nasa.gov/citations/20050030030
[research_mitchamgradyl_stevensjosephe_1956]: https://ntrs.nasa.gov/citations/19930084649
[research_mitchell_raghunathan_1994]: https://doi.org/10.2514/6.1994-1903
[research_mitchelljessel_peckrobertf_1950]: https://ntrs.nasa.gov/citations/20090023623
[research_mitchelljessel_peckrobertf_1950_b]: https://ntrs.nasa.gov/citations/20090026497
[research_mitcheltree_hassan_1989]: https://doi.org/10.2514/6.1989-557
[research_mitsuo_aoki_2018]: https://doi.org/10.1299/jsmemecj.2018.s0520301
[research_mixing_and_1991]: https://doi.org/10.2514/5.9781600866104.0383.0455
[research_miyagoshi_daisuke_2021]: https://doi.org/10.1299/jsmehs.2021.58.f012
[research_miyaji_takegawa_2022]: https://doi.org/10.1299/jfst.2022jfst0004
[research_miyakawa_hirose_1985]: https://doi.org/10.2514/6.1985-5025
[research_miyake_terashima_2022]: https://doi.org/10.1007/978-981-19-2689-1_47
[research_miyake_terashima_2023]: https://doi.org/10.2514/1.j063099
[research_mobley_jones_1989]: https://doi.org/10.2514/6.1989-2763
[research_modarress_johnson_1976]: https://doi.org/10.2514/6.1976-374
[research_modianodavidl_murmanearllm_1993]: https://ntrs.nasa.gov/citations/19930063205
[research_moestimothyr_whitmorestephena_1993]: https://ntrs.nasa.gov/citations/19930009921
[research_moga_1980]: https://doi.org/10.21236/ada091235
[research_moga_dejarnette_1981]: https://doi.org/10.2514/6.1981-75
[research_mohamed_abdelhady_2021]: https://doi.org/10.1007/s00348-021-03282-9
[research_mohan_1991]: https://doi.org/10.2514/6.1991-598
[research_mohr_yang_1988]: https://doi.org/10.2514/6.1988-2304
[research_mokry_1989]: https://doi.org/10.2514/6.1989-147
[research_mokry_1990]: https://doi.org/10.2514/3.10473
[research_mokry_1995]: https://doi.org/10.2514/6.1995-1879
[research_mokry_1995_b]: https://doi.org/10.2514/3.46839
[research_mokry_2001]: https://doi.org/10.2514/6.2001-160
[research_mokry_khalid_2000]: https://doi.org/10.2514/6.2000-2375
[research_molki_ogbozor_2026]: https://doi.org/10.1615/tfec2026.aer.060367
[research_molton_dandois_2013]: https://doi.org/10.2514/1.j051000
[research_molyneux_1960]: https://doi.org/10.1108/eb033339
[research_montaini_carlotti_2026]: https://doi.org/10.2514/1.a36622
[research_montano_dimino_2024]: https://doi.org/10.3390/aerospace11040266
[research_moore_1972]: https://doi.org/10.21236/ad0754098
[research_moore_frei_1983]: https://doi.org/10.2514/6.1983-1834
[research_moorthamers_anemaat_2023]: https://doi.org/10.2514/6.2023-0033
[research_moosavi_naddafoskouei_2005]: https://doi.org/10.1016/j.tws.2004.10.001
[research_moralestirado_quagliarella_2019]: https://doi.org/10.2514/6.2019-0972
[research_morawetz_1987]: https://doi.org/10.1090/conm/060/873535
[research_morelli_2000]: https://doi.org/10.2514/6.2000-3902
[research_morelli_fioravanti_1976]: https://doi.org/10.4271/760186
[research_moreno_taylor_2012]: https://doi.org/10.2514/6.2012-1465
[research_moretti_lippolis_1989]: https://doi.org/10.1007/978-3-322-87875-5_14
[research_mori_yakeno_2024]: https://doi.org/10.2514/6.2024-4486
[research_moritoii_rowe_1972]: https://doi.org/10.2514/6.1972-378
[research_morizawa_nonomura_2018]: https://doi.org/10.2322/tjsass.61.258
[research_moroianu_caraeni_2005]: https://doi.org/10.2514/6.2005-312
[research_morra_nicolosi_2025]: https://doi.org/10.2514/6.2025-3424
[research_morrida_delucca_2017]: https://doi.org/10.2514/6.2017-3654
[research_morse_1945]: https://doi.org/10.1108/eb031266
[research_morton_beran_1995]: https://doi.org/10.2514/6.1995-1905
[research_morton_beran_1996]: https://doi.org/10.2514/6.1996-60
[research_morton_beran_1996_b]: https://doi.org/10.2514/6.1996-1975
[research_morton_beran_1997]: https://doi.org/10.2514/6.1997-1772
[research_morton_beran_1999]: https://doi.org/10.2514/2.2447
[research_mosbarger_king_1995]: https://doi.org/10.2514/6.1995-3462
[research_moseleywcjr_thompsonrf_1957]: https://ntrs.nasa.gov/citations/19630004887
[research_mosesrobertw_1997]: https://ntrs.nasa.gov/citations/19970022378
[research_mosesrobertw_1997_b]: https://ntrs.nasa.gov/citations/20040110392
[research_mosesrobertw_1999]: https://ntrs.nasa.gov/citations/19990028762
[research_mosesrobertw_wiesemancarold_2001]: https://ntrs.nasa.gov/citations/20040086060
[research_mossstevenw_colestanleyr_1991]: https://ntrs.nasa.gov/citations/19910047386
[research_mott_1954]: https://doi.org/10.21236/ad0041678
[research_mottershead_cooper_2012]: https://doi.org/10.21236/ada571493
[research_mouachengm_coxtimothyh_2008]: https://ntrs.nasa.gov/citations/20080006639
[research_moulden_wu_1974]: https://doi.org/10.2514/6.1974-1175
[research_moulmt_1957]: https://ntrs.nasa.gov/citations/19650003117
[research_mounts_barber_1992]: https://doi.org/10.2514/6.1992-751
[research_muck_smits_1984]: https://doi.org/10.2514/6.1984-97
[research_mufti_bhaduri_2024]: https://doi.org/10.1063/5.0185370
[research_muhlsteinjr_coe_1975]: https://doi.org/10.2514/6.1975-142
[research_mukhopadhyay_1999]: https://doi.org/10.2514/6.1999-1396
[research_mukhopadhyay_2000]: https://doi.org/10.2514/2.4635
[research_mukhopadhyayvivek_1999]: https://ntrs.nasa.gov/citations/19990050943
[research_mulder_lubbers_2009]: https://doi.org/10.2514/6.2009-5692
[research_muller_gasko_1967]: https://doi.org/10.2514/3.43825
[research_muller_wesshaar_1994]: https://doi.org/10.2514/6.1994-1775
[research_mundell_mabey_1986]: https://doi.org/10.1017/s0001924000015864
[research_munguia_mukhopadhaya_2019]: https://doi.org/10.2514/6.2019-0695
[research_munk_1921]: https://ntrs.nasa.gov/citations/19800006779
[research_murakami_tada_2007]: https://doi.org/10.2514/6.2007-2897
[research_muralidharan_gilbertraj_2025]: https://doi.org/10.55041/ijsrem52300
[research_murman_1972]: https://doi.org/10.2514/6.1972-1007
[research_murman_1976]: https://doi.org/10.1007/978-3-642-81005-3_44
[research_murman_1979]: https://doi.org/10.2514/6.1979-1533
[research_murman_cole_1974]: https://doi.org/10.2514/6.1974-540
[research_murphy_rogers_1983]: https://doi.org/10.2514/6.1983-1027
[research_murphy_schmidt_1953]: https://doi.org/10.21236/ad0023468
[research_murphyjd_1970]: https://ntrs.nasa.gov/citations/19700012067
[research_murphyjd_1971]: https://ntrs.nasa.gov/citations/19710005497
[research_murphyjd_rosewc_1968]: https://ntrs.nasa.gov/citations/19680058775
[research_murray_1979]: https://doi.org/10.1017/s0001925900008659
[research_murray_giannellis_2020]: https://doi.org/10.2514/6.2020-1987
[research_murray_hillier_2009]: https://doi.org/10.1007/978-3-540-85181-3_69
[research_murthy_rose_1977]: https://doi.org/10.2514/6.1977-687
[research_murthy_steinle_1986]: https://doi.org/10.2514/6.1986-764
[research_murthy_wedemeyer_1990]: https://doi.org/10.2514/3.45971
[research_murthyav_1987]: https://ntrs.nasa.gov/citations/19870005754
[research_murty_1993]: https://doi.org/10.2514/3.46317
[research_myers_ruo_1983]: https://doi.org/10.2514/6.1983-885
[research_myersmr_guruswamyp_1983]: https://ntrs.nasa.gov/citations/19830048630
[research_naca_1135]: https://ntrs.nasa.gov/citations/19930091059
[research_naca_conference_1947]: https://ntrs.nasa.gov/citations/19790079919
[research_nagamatsu_ficarra_1985]: https://doi.org/10.2514/6.1985-207
[research_nagamatsu_orozco_1984]: https://doi.org/10.2514/6.1984-1682
[research_nagamatsu_trilling_1987]: https://doi.org/10.2514/6.1987-1263
[research_nagamatsuht_browerwbjr_1982]: https://ntrs.nasa.gov/citations/19820014335
[research_nagamatsuht_dyerr_1984]: https://ntrs.nasa.gov/citations/19850018354
[research_nagamatsuht_ficarrar_1983]: https://ntrs.nasa.gov/citations/19840008067
[research_nagaraja_lakin_1982]: https://doi.org/10.2514/3.61555
[research_nagarajan_baraiya_2023]: https://doi.org/10.2514/6.2023-2188
[research_nagel_thomas_1965]: https://doi.org/10.2514/6.1965-208
[research_nagy_kirsten_1976]: https://doi.org/10.21236/adb012970
[research_nahomjidovetski_raveh_2025]: https://doi.org/10.2514/6.2025-0624
[research_naida_fonarev_1995]: https://doi.org/10.1007/bf02369774
[research_naida_fonarev_1996]: https://doi.org/10.1007/bf02369855
[research_nakagawa_1986]: https://doi.org/10.1098/rspa.1986.0097
[research_nakagawa_dahm_2000]: https://doi.org/10.2514/6.2000-664
[research_nakakita_arizono_2009]: https://doi.org/10.2514/6.2009-3847
[research_nakamura_1982]: https://doi.org/10.1143/jpsj.51.4084
[research_nallapula_schade_2012]: https://doi.org/10.2514/6.2012-3142
[research_namba_1968]: https://doi.org/10.1299/kikai1938.34.1923
[research_nambu_hashimoto_2012]: https://doi.org/10.2514/6.2012-3229
[research_namgoong_crossley_2002]: https://doi.org/10.2514/6.2002-5641
[research_namura_jeong_2013]: https://doi.org/10.2514/6.2013-251
[research_namura_jeong_2013_b]: https://doi.org/10.2322/tjsass.56.293
[research_nangia_ghoreyshi_2023]: https://doi.org/10.2514/6.2023-0821
[research_nangia_palmer_2000]: https://doi.org/10.2514/6.2000-4409
[research_nangia_palmer_2003]: https://doi.org/10.2514/6.2003-605
[research_narain_1983]: https://doi.org/10.2514/6.1983-186
[research_narayanswamin_horstmancc_1993]: https://ntrs.nasa.gov/citations/19930061729
[research_nark_1968]: https://doi.org/10.4271/680200
[research_narsipur_2022]: https://doi.org/10.1007/s00162-022-00621-2
[research_nash_timme_2025]: https://doi.org/10.2514/6.2025-3767
[research_nashjf_scruggsrm_1972]: https://ntrs.nasa.gov/citations/19740001917
[research_nastase_rudianu_1990]: https://doi.org/10.1515/9783112571101-032
[research_nastase_weisensee_1984]: https://doi.org/10.1515/9783112550908-091
[research_natarajan_2022]: https://doi.org/10.1063/5.0077679
[research_nationaladvisorycommitteeforaeronautics_1932]: https://doi.org/10.1016/s0016-0032(32)91536-1
[research_navalairsystemscommandpatuxentrivermd_1999]: https://doi.org/10.21236/ada384654
[research_navalairsystemscommandpatuxentrivermd_2000]: https://doi.org/10.21236/ada384646
[research_nayfeh_1992]: https://doi.org/10.21236/ada254489
[research_nazarenko_nevezhina_1972]: https://doi.org/10.1007/bf01186488
[research_neal_1970]: https://doi.org/10.4271/700237
[research_negrao_fanton_1998]: https://doi.org/10.4271/982869
[research_neil_verhoff_1982]: https://doi.org/10.2514/6.1982-936
[research_nellessen_britten_1996]: https://doi.org/10.1007/978-3-322-89849-4_36
[research_nelson_mouch_1978]: https://doi.org/10.21236/ada056045
[research_nelsonrobertl_stoneywilliamejr_1953]: https://ntrs.nasa.gov/citations/19930093736
[research_nelsonrobertl_welshclementj_1957]: https://ntrs.nasa.gov/citations/19930089280
[research_nelsonrobertl_welshclementj_1960]: https://ntrs.nasa.gov/citations/19980227964
[research_nenni_1980]: https://doi.org/10.21236/ada081647
[research_nesteruk_cartwright_2011]: https://doi.org/10.1088/1742-6596/318/2/022042
[research_newell_dolbin_1963]: https://doi.org/10.21236/ad0425705
[research_newman_kemp_1988]: https://doi.org/10.4271/881454
[research_newmanpa_andersonec_1978]: https://ntrs.nasa.gov/citations/19780015162
[research_newton_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50006-3
[research_nghiem_norstrud_1989]: https://doi.org/10.2514/3.10339
[research_ngoc_2020]: https://doi.org/10.1007/s12206-020-0426-7
[research_nguyen_fugate_2019]: https://doi.org/10.2514/6.2019-0217
[research_nguyen_xiong_2022]: https://doi.org/10.2514/6.2022-1325
[research_nguyen_xiong_2022_b]: https://doi.org/10.2514/6.2022-3596
[research_nguyen_xiong_2023]: https://doi.org/10.2514/6.2023-3945
[research_nguyen_xiong_2023_b]: https://doi.org/10.2514/6.2023-0998
[research_nhannguyen_jasonfugate]: https://ntrs.nasa.gov/citations/20200002955
[research_nhannguyen_juntaoxiong]: https://ntrs.nasa.gov/citations/20230000002
[research_ni_hu_2012]: https://doi.org/10.2514/6.2012-1979
[research_nichols_jackson_1962]: https://doi.org/10.21236/ad0287183
[research_nicholsmarkr_goraledwinb_1947]: https://ntrs.nasa.gov/citations/20050071701
[research_nicholsmarkr_goraledwinb_1952]: https://ntrs.nasa.gov/citations/19930083896
[research_nicholsmarkr_rinkoskidonaldw_1952]: https://ntrs.nasa.gov/citations/19930083216
[research_nicholsme_1974]: https://ntrs.nasa.gov/citations/19740025206
[research_nicholson_lowry_1966]: https://doi.org/10.21236/ad0635106
[research_nicks_mckinney_1978]: https://doi.org/10.2514/6.1978-770
[research_nicola_cirino_2002]: https://doi.org/10.1007/978-3-540-45856-2_7
[research_nicolaides_1982]: https://doi.org/10.21236/ada127944
[research_nicolaides_brady_1959]: https://doi.org/10.21236/ad0219843
[research_nicolas_sullivan_2016]: https://doi.org/10.3390/aerospace3030018
[research_nicolosi_demarco_2011]: https://doi.org/10.2514/1.c031056
[research_nie_song_2022]: https://doi.org/10.2514/1.c036377
[research_nie_zhang_2026]: https://doi.org/10.1063/5.0343289
[research_nie_zheng_2024]: https://doi.org/10.3390/app14167149
[research_nielsen_1985]: https://doi.org/10.2514/6.1985-449
[research_nielsen_1985_b]: https://doi.org/10.2514/3.45222
[research_nielsen_goodwin_1984]: https://doi.org/10.2514/6.1984-312
[research_nietubicz_1975]: https://doi.org/10.21236/ada009704
[research_nietubicz_sahu_1984]: https://doi.org/10.2514/6.1984-326
[research_nietubicz_sturek_1988]: https://doi.org/10.2514/6.1988-1995
[research_niewald_parker_1999]: https://doi.org/10.2514/6.1999-768
[research_niewoehner_2006]: https://doi.org/10.2514/1.18976
[research_nikfetrat_vandam_1992]: https://doi.org/10.2514/6.1992-169
[research_nikolic_jumper_2004]: https://doi.org/10.2514/6.2004-217
[research_nikolitsch_1978]: https://doi.org/10.2514/6.1978-63
[research_niliahmadabadi_ghadak_2013]: https://doi.org/10.1016/j.compfluid.2013.05.007
[research_niven_tait_2000]: https://doi.org/10.1017/s0001924000017875
[research_nixon_1974]: https://doi.org/10.2514/3.60334
[research_nixon_1979]: https://doi.org/10.2514/6.1979-76
[research_nixon_1980]: https://doi.org/10.2514/3.7681
[research_nixon_2001]: https://doi.org/10.2514/6.2001-713
[research_nixon_2003]: https://doi.org/10.4271/2003-01-3021
[research_nixon_2020]: https://doi.org/10.2514/6.2020-2729
[research_nixon_klopfer_1984]: https://doi.org/10.21236/ada143641
[research_nixon_nixon_1997]: https://doi.org/10.2514/6.1997-2241
[research_nixon_nixon_1997_b]: https://doi.org/10.2514/6.1997-2240
[research_nixon_tzuoo_1986]: https://doi.org/10.21236/ada167748
[research_nixon_tzuoo_1987]: https://doi.org/10.2514/3.45510
[research_noboru_saito_2008]: https://doi.org/10.4050/vfs-f64-000032
[research_nocilla_1972]: https://doi.org/10.1007/bf02128893
[research_nomura_2003]: https://doi.org/10.2514/6.2003-4145
[research_nonlinear_green_s_1982]: https://doi.org/10.2514/5.9781600865558.0565.0603
[research_nonomura_fujii_2007]: https://doi.org/10.1115/fedsm2007-37539
[research_nonomura_fujii_2008]: https://doi.org/10.2514/6.2008-6587
[research_norris_1979]: https://doi.org/10.2514/6.1979-1666
[research_norris_paris_1989]: https://doi.org/10.2514/6.1989-3378
[research_norum_brown_1993]: https://doi.org/10.2514/6.1993-4388
[research_norum_shearin_1986]: https://doi.org/10.2514/6.1986-1945
[research_ntantis_xezonakis_2024]: https://doi.org/10.1016/j.rineng.2024.103189
[research_nugentjack_1954]: https://ntrs.nasa.gov/citations/19930088200
[research_nunn_bry_1982]: https://doi.org/10.21236/ada117268
[research_nyquist_1928]: https://doi.org/10.1109/T-AIEE.1928.5055024
[research_o_lewis_2001]: https://doi.org/10.2514/6.2001-561
[research_obara_lee_1991]: https://doi.org/10.2514/6.1991-3282
[research_obayashi_kuwahara_1985]: https://doi.org/10.2514/6.1985-183
[research_oberkampf_1978]: https://doi.org/10.2514/6.1978-1337
[research_obrien_takahashi_2023]: https://doi.org/10.2514/6.2023-3233
[research_ogawa_babinsky_2006]: https://doi.org/10.2514/6.2006-879
[research_ogawa_babinsky_2007]: https://doi.org/10.2514/6.2007-324
[research_ogawa_babinsky_2008]: https://doi.org/10.2514/1.32049
[research_ogawa_watanabe_2008]: https://doi.org/10.2514/6.2008-717
[research_ogren_sotanski_1974]: https://doi.org/10.21236/ad0784134
[research_ohashi_fukagata_2021]: https://doi.org/10.2514/1.j060415
[research_ohashi_morita_2019]: https://doi.org/10.1115/ajkfluids2019-5067
[research_ohashi_morita_2020]: https://doi.org/10.1299/jfst.2020jfst0008
[research_ohmichi_ishida_2017]: https://doi.org/10.2514/6.2017-1436
[research_ohmichi_ishida_2018]: https://doi.org/10.2514/1.j056855
[research_okellyburker_1954]: https://ntrs.nasa.gov/citations/20090023309
[research_okolo_dogan_2015]: https://doi.org/10.2514/1.c032865
[research_oleggoushcha_martinksekula]: https://ntrs.nasa.gov/citations/20240015072
[research_olejnik_zalewski_2020]: https://doi.org/10.5604/01.3001.0014.8874
[research_oliveira_avelar_2016]: https://doi.org/10.26678/abcm.encit2016.cit2016-0655
[research_oliverab_lillardrp_2006]: https://ntrs.nasa.gov/citations/20080026342
[research_oliverab_lillardrp_2007]: https://ntrs.nasa.gov/citations/20070003681
[research_olivier_reichel_2002]: https://doi.org/10.2514/6.2002-301
[research_olivier_reichel_2003]: https://doi.org/10.2514/2.2098
[research_olles_lynn_2004]: https://doi.org/10.2514/6.2004-3922
[research_olsen_1966]: https://doi.org/10.21236/ad0647369
[research_olsen_shaw_1984]: https://doi.org/10.2514/6.1984-109
[research_olson_albrecht_2026]: https://doi.org/10.2514/1.j066774
[research_olson_stridsberg_1979]: https://doi.org/10.2514/6.1979-1534
[research_olsonrolande_bielatralphp_1955]: https://ntrs.nasa.gov/citations/19930088632
[research_om_childs_1982]: https://doi.org/10.2514/6.1982-990
[research_om_childs_1983]: https://doi.org/10.2514/6.1983-1402
[research_om_childs_1985]: https://doi.org/10.2514/3.9117
[research_om_curtin_2001]: https://doi.org/10.2514/6.2001-909
[research_on_the_numerical]: https://doi.org/10.12681/eadd/57847
[research_ongarato_1969]: https://doi.org/10.2514/3.44021
[research_opgenoord_drela_2017]: https://doi.org/10.2514/6.2017-4340
[research_opstal_2011]: https://doi.org/10.2174/1874146001104010001
[research_ordaz_geiselhart_2015]: https://doi.org/10.2514/1.c033160
[research_orme_gilyard_1993]: https://doi.org/10.2514/6.1993-1821
[research_ormsbee_1962]: https://doi.org/10.21236/ad0295993
[research_oruc_baklacioglu_2022]: https://doi.org/10.1016/j.energy.2022.125069
[research_oruc_baklacioglu_2023]: https://doi.org/10.1016/j.energy.2023.126819
[research_osawa_hewitt_1986]: https://doi.org/10.2514/6.1986-1828
[research_osborneroberts_1949]: https://ntrs.nasa.gov/citations/19930085883
[research_osborneroberts_1957]: https://ntrs.nasa.gov/citations/20050028481
[research_osborneroberts_tempelmeyerkennethe_1954]: https://ntrs.nasa.gov/citations/20090023161
[research_osborners_staffordvc_1960]: https://ntrs.nasa.gov/citations/19630002684
[research_oskam_1983]: https://doi.org/10.2514/6.1983-1855
[research_oskam_vas_1978]: https://doi.org/10.21236/ada057010
[research_osnes_vartdal_2022]: https://doi.org/10.1063/5.0086399
[research_ostgaard_1962]: https://doi.org/10.4271/620343
[research_oswald_1932]: https://ntrs.nasa.gov/citations/19930091482
[research_oswatitsch_1980]: https://doi.org/10.1007/978-3-322-91082-0_20
[research_otiefy_negm_2010]: https://doi.org/10.1088/0964-1726/19/12/125001
[research_otiefy_negm_2011]: https://doi.org/10.1016/j.ijsolstr.2010.09.005
[research_otto_1974]: https://doi.org/10.2514/3.60374
[research_owen_1981]: https://doi.org/10.2514/6.1981-156
[research_owen_owen_2014]: https://doi.org/10.2514/6.2014-0617
[research_owens_capone_2003]: https://doi.org/10.2514/6.2003-750
[research_owenslr_wahlsra_2002]: https://ntrs.nasa.gov/citations/20020023445
[research_ower_pankhurst_1977]: https://doi.org/10.1016/b978-0-08-021281-4.50010-5
[research_ower_pankhurst_1977_b]: https://doi.org/10.1016/b978-0-08-021281-4.50009-9
[research_oyama_ito_2008]: https://doi.org/10.2514/6.2008-354
[research_oyeniran_miyake_2022]: https://doi.org/10.2514/1.j062054
[research_ozawa_nonomura_2024]: https://doi.org/10.2514/6.2024-3200
[research_ozgoren_sahin_2001]: https://doi.org/10.2514/2.2891
[research_paciorri_sabetta_2003]: https://doi.org/10.2514/2.3967
[research_padova_falk_1980]: https://doi.org/10.21236/ada088831
[research_padua_preisigheviana_2025]: https://doi.org/10.2514/6.2025-3459
[research_pagewilliama_1956]: https://ntrs.nasa.gov/citations/19930088967
[research_pahle_berger_2012]: https://doi.org/10.2514/6.2012-4802
[research_pak_friedmann_1991]: https://doi.org/10.2514/6.1991-986
[research_pak_friedmann_1995]: https://doi.org/10.1177/107754639500100401
[research_pal_roy_2024]: https://doi.org/10.1063/5.0225469
[research_palaniappan_jameson_2004]: https://doi.org/10.2514/6.2004-5383
[research_palko_1972]: https://doi.org/10.2514/6.1972-1026
[research_palko_1973]: https://doi.org/10.21236/ad0769307
[research_palko_1974]: https://doi.org/10.21236/ad0787659
[research_pallister_parker_1992]: https://doi.org/10.2514/6.1992-3985
[research_pan_kuo_2021]: https://doi.org/10.1115/1.0004529v
[research_panaras_inger_1977]: https://doi.org/10.1115/77-gt-34
[research_panda_warrior_2021]: https://doi.org/10.1115/1.4050644
[research_pandajayanta_seasholtzrichardg_2005]: https://ntrs.nasa.gov/citations/20050051955
[research_pandey_sinha_2024]: https://doi.org/10.2514/6.2024-0249
[research_pane]: https://doi.org/10.14264/c671a2a
[research_pang_zhang_2026]: https://doi.org/10.1063/5.0347600
[research_pantano_sarkar_1999]: https://doi.org/10.1615/tsfp1.100
[research_pantano_sarkar_2002]: https://doi.org/10.1017/s0022112001006978
[research_panton_oberkampf_1980]: https://doi.org/10.2514/3.57897
[research_pao_1976]: https://doi.org/10.2514/6.1976-488
[research_pardeeotwayom_heasletmaxa_1946]: https://ntrs.nasa.gov/citations/19930092734
[research_paris_alaverdi_1998]: https://doi.org/10.2514/6.1998-4450
[research_park_2017]: https://doi.org/10.5139/ijass.2017.18.2.344
[research_park_abla_1982]: https://doi.org/10.2514/6.1982-183
[research_park_abla_1983]: https://doi.org/10.2514/3.19811
[research_park_chung_2012]: https://doi.org/10.5139/jksas.2012.40.2.165
[research_parker_spain_1991]: https://doi.org/10.2514/6.1991-936
[research_parkerjr_black_1988]: https://doi.org/10.2514/6.1988-2001
[research_parks_bachjr_1990]: https://doi.org/10.2514/6.1990-3082
[research_parksjamesh_kehletalanb_1952]: https://ntrs.nasa.gov/citations/19930087101
[research_parlier_1986]: https://doi.org/10.2514/6.1986-9810
[research_parthasarathy_massier_1976]: https://doi.org/10.2514/6.1976-505
[research_pasherar_2011]: https://doi.org/10.5897/sre11.487
[research_pashilkar_1996]: https://doi.org/10.2514/6.1996-3505
[research_pate_1980]: https://doi.org/10.21236/ada384962
[research_patel_deodhare_2023]: https://doi.org/10.61653/joast.v58i4.2006.741
[research_patel_lee_1979]: https://doi.org/10.1007/978-3-642-46395-2_11
[research_patel_lefas_2025]: https://doi.org/10.2514/6.2025-0818
[research_patel_lefas_2026]: https://doi.org/10.2514/1.c038444
[research_pathan_khan_2017]: https://doi.org/10.1109/i2ct.2017.8226299
[research_patterson_1967]: https://doi.org/10.21236/ad0649376
[research_pattersonjcjr_1966]: https://ntrs.nasa.gov/citations/19660008599
[research_pavlenko_reslan_2022]: https://doi.org/10.34759/vst-2022-3-17-28
[research_payne_mcconnell_2004]: https://doi.org/10.2514/6.2004-5050
[research_payne_samuels_1990]: https://doi.org/10.4050/vfs-f46-1008
[research_paziresh_nikseresht_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000704
[research_pazner_franco_2019]: https://doi.org/10.2514/6.2019-1152
[research_pbalakumar_prahladhiyer]: https://ntrs.nasa.gov/citations/20220017612
[research_pearcey_1961]: https://doi.org/10.1016/b978-1-4832-1323-1.50021-x
[research_peelejamesr_1954]: https://ntrs.nasa.gov/citations/19930088105
[research_pehlivanoglu_yagiz_2011]: https://doi.org/10.2514/1.c031066
[research_peigin_epstein_2007]: https://doi.org/10.2514/1.26746
[research_peigin_epstein_2015]: https://doi.org/10.2514/1.j053594
[research_pekardan_alexeenko_2016]: https://doi.org/10.2514/6.2016-4429
[research_pekardan_alexeenko_2018]: https://doi.org/10.2514/1.j056051
[research_peltzer_2008]: https://doi.org/10.1007/s00348-007-0455-3
[research_pendleyroberte_1947]: https://ntrs.nasa.gov/citations/20050019291
[research_peng_chen_2025]: https://doi.org/10.1063/5.0289544
[research_peng_chen_2026]: https://doi.org/10.1016/j.ast.2026.113385
[research_pengelley_wilson_1954]: https://doi.org/10.21236/ad0061591
[research_perez_hader_2025]: https://doi.org/10.2514/6.2025-3602
[research_performance_evaluation_1995]: https://doi.org/10.2514/5.9781600868535.0419.0462
[research_perkins_brice_1966]: https://doi.org/10.21236/ad0632829
[research_perkins_jr_1977]: https://doi.org/10.21236/ada062274
[research_perryanewman_richardwbarnwell_1983]: https://ntrs.nasa.gov/citations/19850003703
[research_perrybiii_1978]: https://ntrs.nasa.gov/citations/19780023100
[research_perryboydiii_silvawaltera_2007]: https://ntrs.nasa.gov/citations/20070021483
[research_persh_1956]: https://doi.org/10.21236/ad0119103
[research_persoon_horsten_1983]: https://doi.org/10.2514/6.1983-1031
[research_persoon_horsten_1984]: https://doi.org/10.2514/3.45061
[research_persoon_roos_1980]: https://doi.org/10.21236/ada097094
[research_peters_1985]: https://doi.org/10.2514/6.1985-1463
[research_peters_kennedy_1977]: https://doi.org/10.2514/6.1977-106
[research_petrocchi_barakos_2023]: https://doi.org/10.2514/6.2023-2276
[research_petrocchi_barakos_2023_b]: https://doi.org/10.2514/6.2023-3527
[research_petrocchi_barakos_2024]: https://doi.org/10.1016/j.ast.2024.109134
[research_petrocchi_mauriello_2023]: https://doi.org/10.1016/j.ast.2023.108478
[research_petrocchi_steijl_2022]: https://doi.org/10.23967/eccomas.2022.278
[research_petronevich_2016]: https://doi.org/10.1063/1.4963929
[research_petty_1975]: https://doi.org/10.21236/ada016728
[research_petyniawilliamw_croomdelwinr_1958]: https://ntrs.nasa.gov/citations/19980231992
[research_pfeifle_notter_2022]: https://doi.org/10.2514/1.c036490
[research_phares_1981]: https://doi.org/10.21236/ada103021
[research_phares_kneile_1976]: https://doi.org/10.21236/ada028059
[research_phillips_1948]: https://ntrs.nasa.gov/citations/19930082293
[research_phillips_lambert_2003]: https://doi.org/10.2514/2.3135
[research_phillips_waggoner_1988]: https://doi.org/10.2514/6.1988-2538
[research_phillips_waggoner_1990]: https://doi.org/10.2514/3.45959
[research_phillips_west_2019]: https://doi.org/10.2514/1.c034932
[research_phillipsps_1984]: https://ntrs.nasa.gov/citations/19840009059
[research_physical_phenomena_1989]: https://doi.org/10.2514/5.9781600865947.0001.0055
[research_physics_assisted_reduced_order_2023]: https://doi.org/10.1063/5.0152127
[research_piatak_1994]: https://doi.org/10.2514/6.1994-3
[research_pickles_2020]: https://doi.org/10.2514/1.j059624
[research_piecewicz_kindsvogel_1943]: https://doi.org/10.2514/8.10356
[research_pierpontpk_1959]: https://ntrs.nasa.gov/citations/19660024792
[research_pierpontpk_1975]: https://ntrs.nasa.gov/citations/19750063347
[research_piette_crooks_1985]: https://doi.org/10.2514/6.1985-664
[research_piettedouglass_cazierfrankwjr_1989]: https://ntrs.nasa.gov/citations/19890009890
[research_pike_1999]: https://doi.org/10.1098/rsta.1999.0424
[research_pilyugin_khlebnikov_2005]: https://doi.org/10.1007/s10697-005-0073-9
[research_pindzola_chew_1960]: https://doi.org/10.21236/ad0241573
[research_pindzola_mozer_1956]: https://doi.org/10.21236/ad0087754
[research_pinebrook_dalton_1983]: https://doi.org/10.1016/0270-0255(83)90048-9
[research_pinebrook_dalton_1983_b]: https://doi.org/10.1016/0045-7825(83)90020-8
[research_pipko_1966]: https://doi.org/10.21236/ad0646293
[research_pirozzoli_bernardini_2010]: https://doi.org/10.1016/j.proeng.2010.09.032
[research_pirozzoli_bernardini_2010_b]: https://doi.org/10.1016/j.piutam.2010.10.032
[research_pirozzoli_bernardini_2010_c]: https://doi.org/10.1017/s0022112010001710
[research_pitchup_control_1960]: https://ntrs.nasa.gov/citations/19980227095
[research_pitchup_evaluation_1955]: https://ntrs.nasa.gov/citations/19930092243
[research_pitot_supersonic_1948]: https://ntrs.nasa.gov/citations/19930085521
[research_pitot_vane_1956]: https://ntrs.nasa.gov/citations/19930084583
[research_pitt_1995]: https://doi.org/10.2514/6.1995-1387
[research_pitt_sexton_2016]: https://doi.org/10.2514/6.2016-1960
[research_pittmanjl_millerds_1984]: https://ntrs.nasa.gov/citations/19870000609
[research_pittsburghunivwashingtondcresearchstaff_1966]: https://doi.org/10.21236/ad0482131
[research_piv_investigation_1994]: https://doi.org/10.2514/6.1994-533
[research_plaban_takahashi_2021]: https://doi.org/10.2514/6.2021-2423
[research_placek_ruchala_2018]: https://doi.org/10.1016/j.trpro.2018.02.029
[research_placek_stryczniewicz_2016]: https://doi.org/10.5604/12314005.1213604
[research_plante]: https://doi.org/10.70675/4579ebe8z5299z46f6z8e4fz76e3d841710d
[research_plante_dandois_2017]: https://doi.org/10.2514/6.2017-3903
[research_plante_laurendeau_2019]: https://doi.org/10.2514/1.j057224
[research_plath]: https://doi.org/10.70675/9415f5c4zb15ez4e25z87c4z376e176813a2
[research_plath_renac_2024]: https://doi.org/10.2139/ssrn.4874603
[research_platou_1968]: https://doi.org/10.2514/6.1968-388
[research_platzer_2010]: https://doi.org/10.1002/9780470686652.eae033
[research_plentovich_1988]: https://doi.org/10.2514/6.1988-2032
[research_plentovicheb_1986]: https://ntrs.nasa.gov/citations/19860010880
[research_plentovicheb_ladsoncl_1984]: https://ntrs.nasa.gov/citations/19840011219
[research_plotkin_1978]: https://doi.org/10.1115/1.3424324
[research_plotkinkj_1972]: https://ntrs.nasa.gov/citations/19730003554
[research_polivanov_2018]: https://doi.org/10.1063/1.5065215
[research_polivanov_sidorenko_2016]: https://doi.org/10.1063/1.4963993
[research_polivanov_sidorenko_2017]: https://doi.org/10.1088/1742-6596/894/1/012073
[research_polivanov_sidorenko_2026]: https://doi.org/10.3390/aerospace13020120
[research_polivanovpa_2022]: https://doi.org/10.21883/tpl.2022.14.52056.18862
[research_poll_schumann_2024]: https://doi.org/10.1017/aer.2024.10
[research_polonsky_2026]: https://doi.org/10.2514/1.c038869
[research_ponnampalambalakumar_prahladhiyer]: https://ntrs.nasa.gov/citations/20240010749
[research_ponnampalambalakumar_prahladhiyer_2023]: https://ntrs.nasa.gov/citations/20220018364
[research_poole_allen_2026]: https://doi.org/10.2514/1.c038630
[research_poole_cromack_1970]: https://doi.org/10.21236/ad0709158
[research_pope_street_1959]: https://doi.org/10.1063/1.3060679
[research_popinski_2019]: https://doi.org/10.1615/ihtc3.1880
[research_poplingher_mallik_2022]: https://doi.org/10.2514/6.2022-2314
[research_poplingher_raveh_2018]: https://doi.org/10.2514/6.2018-2910
[research_poplingher_raveh_2019]: https://doi.org/10.2514/1.j057893
[research_poplingher_raveh_2022]: https://doi.org/10.2514/6.2022-2483
[research_porter_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50011-7
[research_potential_equation_1982]: https://doi.org/10.2514/5.9781600865558.0239.0296
[research_pothjr_fisher_1993]: https://doi.org/10.2514/6.1993-3955
[research_potter_1984]: https://doi.org/10.21236/ada146357
[research_potter_kinslow_1961]: https://doi.org/10.21236/ad0262466
[research_pounds_1972]: https://doi.org/10.2514/6.1972-1011
[research_pounds_walker_1980]: https://doi.org/10.2514/6.1980-461
[research_powers_1988]: https://doi.org/10.2514/6.1988-2553
[research_powerssheryllgoecke_huffmanjarrettk_1986]: https://ntrs.nasa.gov/citations/19880004917
[research_prabakar_srikanth_2017]: https://doi.org/10.1007/978-3-319-46213-4_42
[research_prabhakararao_v_2014]: https://doi.org/10.17950/ijer/v3s7/704
[research_prakash_uthup_2009]: https://doi.org/10.2514/6.2009-3631
[research_prandtl_1928]: https://ntrs.nasa.gov/citations/19930090813
[research_prata_2022]: https://doi.org/10.2514/1.j060516
[research_prediction_and_1985]: https://doi.org/10.2514/5.9781600865732.0173.0206
[research_prediction_of_1981]: https://doi.org/10.2514/6.1981-609
[research_prescott_1963]: https://doi.org/10.4271/630092
[research_price_1978]: https://doi.org/10.21236/ada050891
[research_price_earla_1981]: https://doi.org/10.21236/ada104905
[research_price_jr_1979]: https://doi.org/10.21236/ada078693
[research_pricejr_1981]: https://doi.org/10.2514/6.1981-1493
[research_prior_rozinka_2023]: https://doi.org/10.2514/6.2023-4398
[research_pritts_1974]: https://doi.org/10.21236/adb010173
[research_pritulo_gubanov_1995]: https://doi.org/10.2514/6.1995-3946
[research_probstein_1953]: https://doi.org/10.21236/ad0009822
[research_probsting_yang_2022]: https://doi.org/10.1063/5.0107181
[research_progress_of_1965]: https://ntrs.nasa.gov/citations/19730062061
[research_propeller_propfan_in_flight]: https://doi.org/10.4271/air4065a
[research_properties_and_2012]: https://doi.org/10.2514/5.9781600869228.0338.0438
[research_prudhomme_seraudie]: https://doi.org/10.1109/iciasf.1989.77673
[research_pruett_wolf_1981]: https://doi.org/10.2514/6.1981-2455
[research_puentes_takahashi_2024]: https://doi.org/10.2514/6.2024-0001
[research_purohit_1987]: https://doi.org/10.2514/3.9694
[research_purvis_burkhalter_1979]: https://doi.org/10.2514/3.7617
[research_pushtaev_1989]: https://doi.org/10.1016/0041-5553(89)90024-4
[research_puspitasari_napitupulu_2023]: https://doi.org/10.1063/5.0115047
[research_puthisikamani_sreenivasaraja_2023]: https://doi.org/10.61653/joast.v74i4.2022.47
[research_putnam_mace_1983]: https://doi.org/10.2514/3.44843
[research_putnam_meyers_1975]: https://doi.org/10.2514/6.1975-1425
[research_pylejs_1965]: https://ntrs.nasa.gov/citations/19650024836
[research_qi_gao_2026]: https://doi.org/10.3390/aerospace13060496
[research_qi_he_2012]: https://doi.org/10.2514/6.2012-300
[research_qi_he_2014]: https://doi.org/10.1063/1.4866182
[research_qian_guan_2012]: https://doi.org/10.4028/www.scientific.net/amr.487.267
[research_qin_2012]: https://doi.org/10.1007/978-3-642-25688-2_7
[research_qin_zhu_2000]: https://doi.org/10.2514/6.2000-4329
[research_qiu_sun_2009]: https://doi.org/10.1109/iciea.2009.5138445
[research_qu_zhang_2012]: https://doi.org/10.2514/6.2012-892
[research_quadros_khan_2018]: https://doi.org/10.2478/mme-2018-0085
[research_quagliarella_dell_1994]: https://doi.org/10.2514/6.1994-1896
[research_quasi_transonic_flow_1986]: https://doi.org/10.1016/b978-0-444-87958-5.50010-8
[research_quast_henke_1990]: https://doi.org/10.2514/6.1990-3045
[research_quinn_1999]: https://doi.org/10.2514/6.1999-2622
[research_raab_rohdebrandenburger_2020]: https://doi.org/10.2514/6.2020-0512
[research_radespiel_1989]: https://doi.org/10.2514/6.1989-1790
[research_raghunathan_1983]: https://doi.org/10.2514/6.1983-1726
[research_raghunathan_coll_1979]: https://doi.org/10.2514/3.7636
[research_raghunathan_coll_1981]: https://doi.org/10.2514/3.7765
[research_raghunathan_mcadam_1985]: https://doi.org/10.2514/3.8949
[research_raghunathan_mcllwain_1990]: https://doi.org/10.2514/3.45896
[research_raghunathan_mitchell_1998]: https://doi.org/10.1007/s001930050113
[research_ragni_ashok_2009]: https://doi.org/10.1088/0957-0233/20/7/074005
[research_ragni_vanoudheusden_2010]: https://doi.org/10.1088/0957-0233/22/1/017003
[research_rahman_hasan_2015]: https://doi.org/10.1016/j.proeng.2015.05.021
[research_rahman_labib_2015]: https://doi.org/10.4236/ojfd.2015.54031
[research_rahman_labib_2016]: https://doi.org/10.1063/1.4958385
[research_rahman_vowotor_2025]: https://doi.org/10.2139/ssrn.5220226
[research_raj_1983]: https://doi.org/10.2514/6.1983-262
[research_raj_1984]: https://doi.org/10.2514/3.48237
[research_raj_brennan_1987]: https://doi.org/10.2514/6.1987-40
[research_rajagopal_ortiz_1998]: https://doi.org/10.2514/6.1998-679
[research_rajamurthy_2002]: https://doi.org/10.2514/6.2002-4712
[research_rakin_1981]: https://doi.org/10.2514/6.1981-2461
[research_ram_vemuru_1985]: https://doi.org/10.2514/6.1985-522
[research_ramachandra_sudhakar_1980]: https://doi.org/10.2514/3.44679
[research_ramamurthy_ghaly_2009]: https://doi.org/10.2514/6.2009-3512
[research_ramaswamy_schreyer_2021]: https://doi.org/10.2514/1.j059674
[research_ramaswamy_schreyer_2022]: https://doi.org/10.1007/s10494-022-00324-y
[research_ramaswamy_schreyer_2026]: https://doi.org/10.2514/1.b39869
[research_ramaswamy_viswanathan_1975]: https://doi.org/10.2514/3.44506
[research_ramkumar_weisshaar_1977]: https://doi.org/10.1016/0022-460x(77)90505-3
[research_ramm_1990]: https://doi.org/10.1093/oso/9780195060973.003.0005
[research_ramm_1990_b]: https://doi.org/10.1093/oso/9780195060973.003.0009
[research_ramm_1990_c]: https://doi.org/10.1093/oso/9780195060973.003.0010
[research_ramm_1990_d]: https://doi.org/10.1093/oso/9780195060973.003.0007
[research_ramm_1990_e]: https://doi.org/10.1093/oso/9780195060973.003.0004
[research_ran_wang_2026]: https://doi.org/10.1155/ijae/6910745
[research_ranaudorj_mikkelsenkl_1986]: https://ntrs.nasa.gov/citations/19860013111
[research_ranawake_2015]: https://doi.org/10.21236/ada622331
[research_randallmchriss_1991]: https://ntrs.nasa.gov/citations/19910023126
[research_ranlet_1965]: https://doi.org/10.21236/ad0467022
[research_rasuo_2006]: https://doi.org/10.2514/6.2006-3877
[research_rasuo_2006_b]: https://doi.org/10.1007/978-1-4020-4150-1_46
[research_ratcliff_carlson_1989]: https://doi.org/10.2514/6.1989-2204
[research_rathertgeorgeajr_hansoncarlm_1949]: https://ntrs.nasa.gov/citations/19930085522
[research_ratliff_pagilla_2008]: https://doi.org/10.1109/acc.2008.4586722
[research_ratnayake_2010]: https://doi.org/10.2514/6.2010-477
[research_raveh_2008]: https://doi.org/10.2514/6.2008-1756
[research_raveh_2011]: https://doi.org/10.2514/1.c031224
[research_ray_1994]: https://doi.org/10.2514/6.1994-2115
[research_ray_kilgore_1974]: https://doi.org/10.2514/6.1974-631
[research_rayej_ladsoncl_1984]: https://ntrs.nasa.gov/citations/19850003725
[research_rayronaldj_cobleighbrentr_2002]: https://ntrs.nasa.gov/citations/20030005804
[research_rclock_1990]: https://doi.org/10.1017/s0001924000022326
[research_reaser_hallissy_1983]: https://doi.org/10.2514/6.1983-1792
[research_recommended_practice_2003]: https://doi.org/10.2514/4.476624
[research_redadc_murphyjd_1972]: https://ntrs.nasa.gov/citations/19720050367
[research_reddy_srivastava_1988]: https://doi.org/10.2514/6.1988-2348
[research_redeker_voersmann_1988]: https://doi.org/10.2514/6.1988-2165
[research_redeker_wichmann_1986]: https://doi.org/10.2514/3.45321
[research_redford_sandham_2012]: https://doi.org/10.1016/j.paerosci.2011.08.002
[research_rediniotis_klute_1994]: https://doi.org/10.2514/3.12044
[research_reed_1984]: https://doi.org/10.2514/6.1984-1678
[research_reed_1990]: https://doi.org/10.21236/ada226351
[research_reedwhiii_1975]: https://ntrs.nasa.gov/citations/19750015538
[research_reedwhiii_1976]: https://ntrs.nasa.gov/citations/19760018188
[research_reedwhiii_1985]: https://ntrs.nasa.gov/citations/19860004750
[research_regan_1964]: https://doi.org/10.21236/ad0451010
[research_regierarthura_barmbyjohng_1947]: https://ntrs.nasa.gov/citations/19930081955
[research_reibert_saric_1997]: https://doi.org/10.2514/6.1997-1816
[research_reichert_1947]: https://doi.org/10.2514/8.4133
[research_reimann_2016]: https://doi.org/10.2514/6.2016-3578
[research_rein_henne_2025]: https://doi.org/10.2514/1.j065181
[research_rein_rosemann_2009]: https://doi.org/10.1007/978-3-540-85181-3_83
[research_reinhardt_1948]: https://doi.org/10.4271/480049
[research_reis_falcaofilho_2014]: https://doi.org/10.1016/j.measurement.2014.01.021
[research_reissner_1943]: https://doi.org/10.1115/1.4018865
[research_rekhy_shneider_2020]: https://doi.org/10.2514/6.2020-3241
[research_rembaut_brion_2026]: https://doi.org/10.1007/s13272-026-01011-8
[research_ren_chen_2020]: https://doi.org/10.1063/5.0020496
[research_ren_gao_2022]: https://doi.org/10.3390/act11060155
[research_ren_ma_2026]: https://doi.org/10.2514/1.j066757
[research_report_no_1927]: https://doi.org/10.1016/s0016-0032(27)92139-5
[research_report_no_1939]: https://doi.org/10.1016/s0016-0032(39)90856-2
[research_rerj_1974]: https://ntrs.nasa.gov/citations/19830002754
[research_research_airplane_committee_report_1958]: https://ntrs.nasa.gov/citations/19930092380
[research_resende_nakagawa_1997]: https://doi.org/10.2514/6.1997-1025
[research_resonance_prediction_1986]: https://doi.org/10.2514/6.1986-898
[research_reubush_1975]: https://doi.org/10.2514/6.1975-1294
[research_reuther_vandam_1992]: https://doi.org/10.2514/3.46159
[research_review_of_1982]: https://doi.org/10.2514/5.9781600865558.0001.0001
[research_reynolds_averaged_1982]: https://doi.org/10.2514/5.9781600865558.0297.0375
[research_rhoads_1952]: https://doi.org/10.21236/ad0014479
[research_ricci_scotti_2006]: https://doi.org/10.1016/j.ymssp.2005.08.020
[research_rice_1946]: https://doi.org/10.21236/adb803248
[research_richard_putter_2003]: https://doi.org/10.2514/6.2003-1952
[research_richardeday_wendellhstillwell_1952]: https://ntrs.nasa.gov/citations/19930087318
[research_richardson_1976]: https://doi.org/10.21236/adb012971
[research_richardtwhitcomb_1956]: https://ntrs.nasa.gov/citations/19650070830
[research_richey_petersen_1976]: https://doi.org/10.2514/6.1976-673
[research_richter_rosemann_2002]: https://doi.org/10.1017/s0001924000012987
[research_richter_rosemann_2011]: https://doi.org/10.2514/6.2011-3354
[research_richwinedavidm_delfratejohnh_1995]: https://ntrs.nasa.gov/citations/19950065585
[research_riddle_innis_1981]: https://doi.org/10.2514/6.1981-2409
[research_riddledw_1975]: https://ntrs.nasa.gov/citations/19750036196
[research_riebejohnm_macleodrichardg_1950]: https://ntrs.nasa.gov/citations/20050030032
[research_riggins_nelson_1999]: https://doi.org/10.2514/2.756
[research_rill_becker_1992]: https://doi.org/10.2514/3.46213
[research_rimer_chipman_1983]: https://doi.org/10.2514/6.1983-2125
[research_ringas_2022]: https://doi.org/10.1007/978-3-030-89887-8_2
[research_riou_garnier_2010]: https://doi.org/10.2514/1.j050531
[research_riso_divincenzo_2018]: https://doi.org/10.2514/1.c034787
[research_ristic_1991]: https://doi.org/10.1007/bf00211796
[research_rittenhouse_1959]: https://doi.org/10.21236/ad0207771
[research_rivera_florance_2000]: https://doi.org/10.2514/6.2000-1768
[research_rivers_wahls_2001]: https://doi.org/10.2514/6.2001-2462
[research_riversmelissab_wahlsricharda_1994]: https://ntrs.nasa.gov/citations/19950010493
[research_rizk_1980]: https://doi.org/10.2514/6.1980-125
[research_rizk_1981]: https://doi.org/10.2514/3.57482
[research_rizk_1982]: https://doi.org/10.2514/3.44788
[research_rizk_1986]: https://doi.org/10.21236/ada166766
[research_rizk_lovell_1986]: https://doi.org/10.2514/6.1986-124
[research_rizk_lovell_1988]: https://doi.org/10.2514/6.1988-141
[research_rizk_smithmeyer_1982]: https://doi.org/10.2514/3.44767
[research_rizzetta_1977]: https://doi.org/10.21236/ada057505
[research_rizzetta_1977_b]: https://doi.org/10.21236/ada056946
[research_rizzetta_yoshihara_1980]: https://doi.org/10.2514/6.1980-128
[research_rizzi_1981]: https://doi.org/10.1007/978-3-663-14008-5_16
[research_rizzi_1981_b]: https://doi.org/10.1007/978-3-663-14008-5_18
[research_rizzi_1982]: https://doi.org/10.2514/3.7981
[research_rizzi_1985]: https://doi.org/10.2514/3.45127
[research_rizzi_1995]: https://doi.org/10.1007/978-3-642-79440-7_9
[research_rizzi_eriksson_1981]: https://doi.org/10.2514/6.1981-999
[research_rizzi_purcell_1986]: https://doi.org/10.1007/978-3-642-82770-9_23
[research_rizzi_schmidt_1978]: https://doi.org/10.2514/6.1978-1115
[research_roach_froning_1996]: https://doi.org/10.2514/6.1996-3413
[research_robertdquinn_frankvolinger_1969]: https://ntrs.nasa.gov/citations/19920075483
[research_roberts_1963]: https://doi.org/10.21236/ad0420853
[research_roberts_1963_b]: https://doi.org/10.21236/ad0431307
[research_roberts_reed_2012]: https://doi.org/10.2514/6.2012-2668
[research_roberts_smith_1966]: https://doi.org/10.21236/ad0635953
[research_robinson_1978]: https://doi.org/10.21236/ada057363
[research_robinson_blanchard_2003]: https://doi.org/10.21236/ada419763
[research_robinson_high_1974]: https://doi.org/10.21236/ad0781377
[research_robinson_high_1974_b]: https://doi.org/10.2514/6.1974-1148
[research_robinson_robinson_1950]: https://doi.org/10.21236/adb812174
[research_robinsonglennh_cothrengeorgeejr_1955]: https://ntrs.nasa.gov/citations/19930088812
[research_robinsonharoldl_1948]: https://ntrs.nasa.gov/citations/19930085531
[research_robinsonharoldl_1953]: https://ntrs.nasa.gov/citations/19930087423
[research_robinsonrossb_1954]: https://ntrs.nasa.gov/citations/19930088329
[research_rocket_powered_aircraft_2017]: https://doi.org/10.2307/j.ctvx072b5.11
[research_rodartericciardi_wolf_2020]: https://doi.org/10.26678/abcm.encit2020.cit20-0119
[research_rodartericciardi_wolf_2021]: https://doi.org/10.2514/6.2021-0455
[research_rodemich_andrew_1965]: https://doi.org/10.21236/ad0618097
[research_rodi_stoldt_2019]: https://doi.org/10.2514/6.2019-2812
[research_rodriguez_hickey_2022]: https://doi.org/10.1115/gt2022-80350
[research_roecker_1955]: https://doi.org/10.21236/ad0078604
[research_roepke_1972]: https://doi.org/10.2514/6.1972-1035
[research_rogers_1970]: https://doi.org/10.21236/ada367071
[research_rogers_2010]: https://doi.org/10.2514/1.45654
[research_rogers_walterk_1953]: https://doi.org/10.21236/ad0013358
[research_rogers_walterk_1958]: https://doi.org/10.21236/ad0200177
[research_roh_park_2006]: https://doi.org/10.2514/6.2006-6282
[research_roiati_anderson_2023]: https://doi.org/10.4050/sm_2023_prop-998
[research_roidl_meinke_2011]: https://doi.org/10.2514/6.2011-3974
[research_rokoni_hasan_2013]: https://doi.org/10.3329/jme.v43i1.15782
[research_rom_1965]: https://doi.org/10.21236/ad0617943
[research_roohani_skews_2009]: https://doi.org/10.1007/978-3-540-85181-3_98
[research_rooney_craig_1977]: https://doi.org/10.2514/6.1977-996
[research_roos_1979]: https://doi.org/10.2514/6.1979-351
[research_roos_1980]: https://doi.org/10.2514/3.57965
[research_roosfw_1985]: https://ntrs.nasa.gov/citations/19850058569
[research_roosfw_riddledw_1977]: https://ntrs.nasa.gov/citations/19770022156
[research_roscoe_shamroth_1984]: https://doi.org/10.21236/ada141551
[research_rose_seginer_1977]: https://doi.org/10.2514/6.1977-681
[research_rose_seginer_1978]: https://doi.org/10.2514/3.58399
[research_rosemann_birkemeyer_2002]: https://doi.org/10.1007/978-3-540-45856-2_12
[research_rosen_1984]: https://doi.org/10.2514/3.45057
[research_rosen_1985]: https://doi.org/10.2514/6.1985-423
[research_rosen_1988]: https://doi.org/10.2514/6.1988-3
[research_rosenberg_1944]: https://doi.org/10.2514/8.11091
[research_rosenberg_schuch_1983]: https://doi.org/10.2514/6.1983-2749
[research_rosenhead_1956]: https://doi.org/10.1038/177400a0
[research_rosewc_1970]: https://ntrs.nasa.gov/citations/19700012068
[research_ross_2021]: https://doi.org/10.1109/mspec.2021.9311455
[research_rossdavids_1987]: https://ntrs.nasa.gov/citations/19880033237
[research_roth_barrett_2009]: https://doi.org/10.21236/ada504165
[research_rothmund_harlow_1999]: https://doi.org/10.2514/6.1999-2901
[research_roussel_alizard_2015]: https://doi.org/10.2514/6.2015-2618
[research_row_fischel_1963]: https://doi.org/10.2514/6.1963-75
[research_roy_das_2021]: https://doi.org/10.1007/978-981-15-7711-6_72
[research_roy_sandhu_2021]: https://doi.org/10.1007/s00193-021-01009-7
[research_rubbertpe_lup_1976]: https://ntrs.nasa.gov/citations/19760056907
[research_rubin_1971]: https://doi.org/10.21236/ad0730669
[research_ruetenik_smiley_1978]: https://doi.org/10.21236/ada062408
[research_ruhlin_destuynder_1974]: https://doi.org/10.2514/6.1974-406
[research_ruhlin_murphy_1981]: https://doi.org/10.2514/6.1981-650
[research_ruhlin_prattbarlow_1981]: https://doi.org/10.2514/6.1981-654
[research_ruhlin_rauch_1983]: https://doi.org/10.2514/3.44933
[research_ruhlin_rauchjr_1982]: https://doi.org/10.2514/6.1982-721
[research_ruhlincharlesl_tuovilawj_1961]: https://ntrs.nasa.gov/citations/19980227183
[research_ruhlincl_bhatiakg_1986]: https://ntrs.nasa.gov/citations/19870004356
[research_ruhlincl_doggettrvjr_1976]: https://ntrs.nasa.gov/citations/19760021070
[research_ruhlincl_doggettrvjr_1980]: https://ntrs.nasa.gov/citations/19800016826
[research_ruhlincl_sandfordmc_1968]: https://ntrs.nasa.gov/citations/19680007586
[research_ruhlincl_sandfordmc_1975]: https://ntrs.nasa.gov/citations/19760007429
[research_ruhlincl_youngls_1964]: https://ntrs.nasa.gov/citations/19640020185
[research_rumph_schairer_1940]: https://doi.org/10.2514/8.1192
[research_rumsey_thomas_1987]: https://doi.org/10.2514/6.1987-413
[research_rumseychristopherl_2010]: https://ntrs.nasa.gov/citations/20100037235
[research_runyan_cunningham_1952]: https://doi.org/10.2514/8.2220
[research_runyanharryl_woolstondonalds_1957]: https://ntrs.nasa.gov/citations/19930091012
[research_ruo_theisen_1973]: https://doi.org/10.2514/6.1973-316
[research_ruosy_1978]: https://ntrs.nasa.gov/citations/19790002828
[research_rusak_1993]: https://doi.org/10.1137/1.9781611970975.ch2
[research_rusak_1994]: https://doi.org/10.1137/s0036139991250050
[research_rusak_wang_1999]: https://doi.org/10.2514/6.1999-3106
[research_rusak_webster_1992]: https://doi.org/10.2514/6.1992-2649
[research_rushton_1966]: https://doi.org/10.2514/6.1966-495
[research_russell_werner_2022]: https://doi.org/10.2514/6.2022-0158
[research_russo_tognaccini_2020]: https://doi.org/10.2514/1.j059080
[research_russo_tognaccini_2020_b]: https://doi.org/10.2514/6.2020-0447
[research_ruyten_1999]: https://doi.org/10.21236/ada370964
[research_ryanwallace_jamesreynolds]: https://ntrs.nasa.gov/citations/20230004174
[research_ryzhov_1993]: https://doi.org/10.1137/1.9781611970975.ch3
[research_saadeh_chau_2026]: https://doi.org/10.2514/6.2026-0868
[research_sabin_1957]: https://doi.org/10.21236/ad0156637
[research_sabzehparvar_2005]: https://doi.org/10.2514/1.12837
[research_sachs_1969]: https://doi.org/10.2514/3.44111
[research_sachs_1977]: https://doi.org/10.2514/3.44623
[research_sachs_1980]: https://doi.org/10.2514/3.44685
[research_sadoffmelvin_1953]: https://ntrs.nasa.gov/citations/19930087620
[research_safronov_safronov_1994]: https://doi.org/10.1007/bf02209419
[research_safronov_semon_2023]: https://doi.org/10.32347/2410-2547.2023.110.81-96
[research_safronov_semon_2024]: https://doi.org/10.32347/2410-2547.2024.113.116-123
[research_sagontijo_filho_2025]: https://doi.org/10.26678/abcm.cobem2023.cob2023-1931
[research_sahu_1986]: https://doi.org/10.21236/ada171462
[research_sahu_1988]: https://doi.org/10.2514/6.1988-4038
[research_sahu_1990]: https://doi.org/10.2514/3.25123
[research_sahu_2007]: https://doi.org/10.21236/ada471736
[research_sahu_2008]: https://doi.org/10.2514/6.2008-7115
[research_sahu_2009]: https://doi.org/10.2514/6.2009-3852
[research_sahu_2011]: https://doi.org/10.2514/6.2011-6336
[research_sahu_danberg_1987]: https://doi.org/10.2514/6.1987-2291
[research_sahu_heavey_1995]: https://doi.org/10.2514/6.1995-3459
[research_sahu_nietubicz_1982]: https://doi.org/10.2514/6.1982-1358
[research_sahu_nietubicz_1983]: https://doi.org/10.21236/ada130293
[research_sahu_nietubicz_1983_b]: https://doi.org/10.21236/ada135783
[research_sahyoun_boose_2026]: https://doi.org/10.1007/s13272-026-00954-2
[research_saitoh_hashidate_1995]: https://doi.org/10.2514/6.1995-3926
[research_saitoh_tamayama_2012]: https://doi.org/10.2478/s13531-012-0008-2
[research_sajben_bogar_1982]: https://doi.org/10.21236/ada118473
[research_sajben_kroutil_1979]: https://doi.org/10.21236/ada075261
[research_sakaki_kakudo_2015]: https://doi.org/10.2514/6.2015-3845
[research_sakaki_kakudo_2016]: https://doi.org/10.2514/6.2016-5080
[research_sakata_2002]: https://doi.org/10.2514/6.2002-527
[research_sakurai_1959]: https://doi.org/10.1143/jpsj.14.658
[research_saltzman_ayers_1981]: https://doi.org/10.2514/6.1981-2475
[research_saltzman_ayers_1982]: https://doi.org/10.2514/3.61561
[research_samant_wigton_1983]: https://doi.org/10.2514/6.1983-1806
[research_sammonds_1970]: https://doi.org/10.2514/6.1970-564
[research_samputh_moey_2024]: https://doi.org/10.3846/aviation.2024.21495
[research_sanderson_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50017-8
[research_sandford_abel_1974]: https://doi.org/10.2514/6.1974-403
[research_sandfordmc_ruhlincl_1974]: https://ntrs.nasa.gov/citations/19740019292
[research_sang_schetz_2002]: https://doi.org/10.2514/6.2002-533
[research_sanghi_riso_2020]: https://doi.org/10.2514/6.2020-2645
[research_sanghi_riso_2025]: https://doi.org/10.2514/1.c038166
[research_sangwan_sengupta_2017]: https://doi.org/10.1063/1.4995457
[research_sankar_malone_1985]: https://doi.org/10.2514/6.1985-4061
[research_sankar_tassa_1980]: https://doi.org/10.2514/6.1980-10
[research_sankar_tassa_1981]: https://doi.org/10.2514/3.50976
[research_sansica_hashimoto_2023]: https://doi.org/10.2514/1.j062808
[research_sansica_hashimoto_2023_b]: https://doi.org/10.2514/6.2023-1989
[research_sansica_sandham_2013]: https://doi.org/10.2514/6.2013-2982
[research_sansica_sandham_2014]: https://doi.org/10.1063/1.4894427
[research_saric_1997]: https://doi.org/10.21236/ada388392
[research_saric_1998]: https://doi.org/10.21236/ada359230
[research_saric_2010]: https://doi.org/10.21236/ada564004
[research_sarigulklijn_sarigulklijn_2005]: https://doi.org/10.2514/6.2005-621
[research_sarigulklijn_sarigulklijn_2006]: https://doi.org/10.2514/1.18559
[research_sarigulklijn_sarigulklijn_2008]: https://doi.org/10.2514/6.2008-7835
[research_sarigulklijn_sarigulklijn_2012]: https://doi.org/10.2514/6.2012-5156
[research_sarkar_1994]: https://doi.org/10.1115/1.3124401
[research_sarlak_2017]: https://doi.org/10.1088/1742-6596/854/1/012040
[research_sarohia_1977]: https://doi.org/10.2514/6.1977-1328
[research_sarohia_parthasarathy_1980]: https://doi.org/10.2514/6.1980-1032
[research_sartor]: https://doi.org/10.70675/0127f7c9zede5z4492z9342z76d03852c137
[research_sartor_clement_2013]: https://doi.org/10.2514/6.2013-2735
[research_sartor_losfeld_2012]: https://doi.org/10.1007/s00348-012-1330-4
[research_sashida_aoyama_2024]: https://doi.org/10.2514/6.2024-0299
[research_sashida_kawai_2026]: https://doi.org/10.2514/6.2026-0101
[research_satyanarayana_schairer_1981]: https://doi.org/10.2514/3.44701
[research_saunders_1996]: https://doi.org/10.2514/6.1996-227
[research_savage_bommerscheim_1962]: https://doi.org/10.1520/stp46011s
[research_savin_2019]: https://doi.org/10.1615/tsagiscij.2019032794
[research_savinraymondc_1958]: https://ntrs.nasa.gov/citations/19630002629
[research_sawyerrichardh_trantjamespjr_1947]: https://ntrs.nasa.gov/citations/20050019378
[research_sawyerrichardh_trantjamespjr_1950]: https://ntrs.nasa.gov/citations/20050028471
[research_sayers_1936]: https://doi.org/10.1108/eb030090
[research_sbli_experiments_2022]: https://ntrs.nasa.gov/citations/20220017569
[research_scafetta_1983]: https://doi.org/10.2514/6.1983-1075
[research_scanlan_1948]: https://doi.org/10.21236/ada955900
[research_schaechterleg_ludewigkh_1982]: https://ntrs.nasa.gov/citations/19830015055
[research_schaeffler_telionis_1998]: https://doi.org/10.2514/6.1998-673
[research_schaireredwardt_1994]: https://ntrs.nasa.gov/citations/19950057303
[research_schaireredwardt_leegeorge_1989]: https://ntrs.nasa.gov/citations/19900004091
[research_schaireredwardt_leegeorge_1991]: https://ntrs.nasa.gov/citations/19920030577
[research_schaireret_mendozajp_1982]: https://ntrs.nasa.gov/citations/19820016338
[research_schauerte_kwong_2026]: https://doi.org/10.2514/6.2026-2314
[research_schauerte_schreyer_2022]: https://doi.org/10.55037/lxlaser.20th.136
[research_schauerte_schreyer_2023]: https://doi.org/10.2514/6.2023-0431
[research_schauerte_schreyer_2023_b]: https://doi.org/10.2514/1.j062349
[research_schauerte_schreyer_2024]: https://doi.org/10.2514/6.2024-1946
[research_schauerte_schreyer_2025]: https://doi.org/10.2514/6.2025-3837
[research_schauerte_schreyer_2025_b]: https://doi.org/10.2514/1.j064687
[research_schauerte_schreyer_2025_c]: https://doi.org/10.2514/1.j063856
[research_schermerhorn_1969]: https://doi.org/10.21236/ad0863422
[research_schermerhorn_demeritte_1960]: https://doi.org/10.21236/ad0884854
[research_schewe_mai_2018]: https://doi.org/10.1016/j.jfluidstructs.2018.04.021
[research_schewe_mai_2019]: https://doi.org/10.1016/j.jfluidstructs.2018.07.005
[research_schiavetta_boelens_2006]: https://doi.org/10.2514/6.2006-3171
[research_schlinker_simonich_2010]: https://doi.org/10.2514/6.2010-3925
[research_schloemer_1966]: https://doi.org/10.21236/ad0638133
[research_schmeerjamesw_runckeljackf_1962]: https://ntrs.nasa.gov/citations/19980231067
[research_schmidt_1979]: https://doi.org/10.1007/978-3-642-67220-0_6
[research_schmisseur_dolling_1992]: https://doi.org/10.2514/6.1992-748
[research_schmitt_destarac_1983]: https://doi.org/10.2514/6.1983-1804
[research_schmitt_reneaux_1990]: https://doi.org/10.2514/6.1990-3042
[research_schnerr_dohrmann_1991]: https://doi.org/10.2514/6.1991-1716
[research_schnerr_dohrmann_1994]: https://doi.org/10.2514/3.11956
[research_schoolfield_1942]: https://doi.org/10.2514/8.10935
[research_schouten_bakker_2000]: https://doi.org/10.2514/6.2000-2018
[research_schrauf_perraud_1998]: https://doi.org/10.2514/2.2409
[research_schreyer_2023]: https://doi.org/10.52843/cassyni.2ynr19
[research_schroder_meijering_2005]: https://doi.org/10.1002/gamm.201490013
[research_schuelein_2014]: https://doi.org/10.2514/6.2014-3332
[research_schumacher_1952]: https://doi.org/10.21236/ada075866
[research_schuman_2018]: https://doi.org/10.2514/6.2018-3875
[research_schusterdavidm_byrdjamese_2003]: https://ntrs.nasa.gov/citations/20030009796
[research_schwartz_gudmundsson_2024]: https://doi.org/10.2514/6.2024-2134
[research_schwartzberg_1975]: https://doi.org/10.21236/ada017321
[research_schwarzt_wuest_1964]: https://doi.org/10.2514/6.1964-564
[research_sclafani_dehaan_2010]: https://doi.org/10.2514/6.2010-4219
[research_scott_candon_2024]: https://doi.org/10.2514/6.2024-2440
[research_sears_1947]: https://doi.org/10.1090/qam/20394
[research_sebastia_hornung_2023]: https://doi.org/10.2514/6.2023-3528
[research_sebastia_wurz_2024]: https://doi.org/10.2514/6.2024-3997
[research_seckel_1964]: https://doi.org/10.1016/b978-0-12-634450-9.50026-9
[research_sedin_sorensen_1984]: https://doi.org/10.2514/6.1984-243
[research_sedin_sorensen_1986]: https://doi.org/10.2514/3.9287
[research_sedney_1954]: https://doi.org/10.21236/ad0041671
[research_seebass_1982]: https://doi.org/10.1016/b978-0-12-493280-7.50007-3
[research_seebassar_1974]: https://ntrs.nasa.gov/citations/19740022516
[research_seebassar_yunj_1976]: https://ntrs.nasa.gov/citations/19760015402
[research_seegmillerhl_marvinjg_1978]: https://ntrs.nasa.gov/citations/19780036804
[research_seficwalterj_maxwellcleom_1987]: https://ntrs.nasa.gov/citations/19870000497
[research_segee_schetz_2016]: https://doi.org/10.2514/6.2016-4039
[research_seginer_rose_1976]: https://doi.org/10.2514/6.1976-330
[research_seginer_rose_1977]: https://doi.org/10.2514/6.1977-210
[research_seidel_sandford_1985]: https://doi.org/10.2514/6.1985-598
[research_seider_haenel_1991]: https://doi.org/10.2514/6.1991-184
[research_seifert_pack_2001]: https://doi.org/10.2514/2.2815
[research_selbergbrucep_rokhsazkamran_1991]: https://ntrs.nasa.gov/citations/19910055593
[research_selerowicz_2020]: https://doi.org/10.24425/ame.2009.132091
[research_sellers_chandra_1997]: https://doi.org/10.1108/02644409710157596
[research_sengupta_chakraborty_2022]: https://doi.org/10.1063/5.0088362
[research_sengupta_roy_2021]: https://doi.org/10.1063/5.0075692
[research_seraj_martins_2023]: https://doi.org/10.2514/6.2023-3472
[research_seraj_martins_2025]: https://doi.org/10.2514/1.c037899
[research_seraudiea_blancharda_1985]: https://ntrs.nasa.gov/citations/19870001401
[research_serdarevickadic_terzic_2019]: https://doi.org/10.2507/daaam.scibook.2019.06
[research_sethkelly_tausifjamal]: https://ntrs.nasa.gov/citations/20250006503
[research_sethwkelly_tausifjamal]: https://ntrs.nasa.gov/citations/20250005725
[research_settles_1981]: https://doi.org/10.21236/ada110423
[research_settlesgs_bogdonoffsm_1981]: https://ntrs.nasa.gov/citations/19810014882
[research_sevostianow_1967]: https://doi.org/10.1016/0021-8928(67)90207-9
[research_sewall_1984]: https://doi.org/10.2514/6.1984-599
[research_sewallwilliamg_mcgheerobertj_1985]: https://ntrs.nasa.gov/citations/19880004696
[research_sforza_2018]: https://doi.org/10.2514/6.2018-0273
[research_sforza_2020]: https://doi.org/10.2514/1.c035717
[research_shahjahan_ahuja_2026]: https://doi.org/10.2514/6.2026-4665
[research_shahrokhi_jahangirian_2010]: https://doi.org/10.1080/03052150903305468
[research_shanbhag_narasimha_1970]: https://doi.org/10.1002/nme.1620020213
[research_shang_hankeyjr_1976]: https://doi.org/10.2514/6.1976-95
[research_shankar_2013]: https://doi.org/10.2514/6.2013-4924
[research_shankar_goebel_1985]: https://doi.org/10.2514/6.1985-428
[research_shankar_ide_1989]: https://doi.org/10.1007/978-3-642-83584-1_37
[research_shankar_malmuth_1978]: https://doi.org/10.2514/6.1978-103
[research_shankar_malmuth_1979]: https://doi.org/10.2514/6.1979-344
[research_shankar_malmuth_1979_b]: https://doi.org/10.2514/6.1979-1565
[research_shankar_malmuth_1982]: https://doi.org/10.21236/ada121662
[research_shannon_1948]: https://doi.org/10.1002/j.1538-7305.1948.tb01338.x
[research_shantz_1953]: https://doi.org/10.21236/ad0037850
[research_shao_he_2026]: https://doi.org/10.2139/ssrn.6351262
[research_sharma_ghosh_2014]: https://doi.org/10.2514/6.2014-1246
[research_sheaiii_1978]: https://doi.org/10.2514/6.1978-1170
[research_shearin_jones_1989]: https://doi.org/10.2514/6.1989-1069
[research_sheibani_jafarian_2024]: https://doi.org/10.1063/5.0237182
[research_sheilatobing_2022]: https://doi.org/10.37934/cfdl.14.5.1623
[research_shen_zuo_2026]: https://doi.org/10.1016/j.ast.2026.112628
[research_sheng_galbraith_2007]: https://doi.org/10.2514/6.2007-1075
[research_shepheard_1965]: https://doi.org/10.21236/ad0630924
[research_sheridan_young_2017]: https://doi.org/10.1007/978-3-319-46213-4_109
[research_sherrouse_mcwhorter_1992]: https://doi.org/10.1520/stp20160s
[research_sheta_2004]: https://doi.org/10.2514/1.9327
[research_shi_chen_2020]: https://doi.org/10.2514/1.j058773
[research_shi_he_2023]: https://doi.org/10.1016/j.cja.2023.05.016
[research_shi_wen_2019]: https://doi.org/10.2514/6.2019-2957
[research_shibata_tanaka_2018]: https://doi.org/10.1299/jsmekansai.2018.93.p036
[research_shieh_1988]: https://doi.org/10.2514/6.1988-3614
[research_shimada_shiratori_2009]: https://doi.org/10.1299/jsmemecjo.2009.7.0_233
[research_shinde_gaitonde_2022]: https://doi.org/10.2514/6.2022-1975
[research_shipilin_1964]: https://doi.org/10.1016/0021-8928(64)90113-3
[research_shiqi_tian_2018]: https://doi.org/10.2514/6.2018-0790
[research_shmikovicha_caugheyda_1981]: https://ntrs.nasa.gov/citations/19810025342
[research_shmilovich_caughey]: https://doi.org/10.1007/3-540-13917-6_190
[research_shmilovich_caughey_1982]: https://doi.org/10.1016/0021-9991(82)90062-6
[research_shmilovich_caughey_1985]: https://doi.org/10.2514/3.45169
[research_shmyglevskii_1960]: https://doi.org/10.1016/0021-8928(60)90118-0
[research_shouying_shijun_1982]: https://doi.org/10.1007/3-540-11948-5_42
[research_shubham_sandberg_2022]: https://doi.org/10.1016/j.jsv.2022.116762
[research_sichel_1970]: https://doi.org/10.21236/ad0869875
[research_sichel_yin_1966]: https://doi.org/10.21236/ad0636253
[research_sickles_ericksonjr_1990]: https://doi.org/10.2514/6.1990-1408
[research_siclari_vannostrand_1996]: https://doi.org/10.2514/6.1996-329
[research_siclarimj_1982]: https://ntrs.nasa.gov/citations/19820043555
[research_sidorenko_budovskii_2017]: https://doi.org/10.1134/s1063785017060268
[research_sidorenko_kirilovskiy_2018]: https://doi.org/10.1063/1.5065356
[research_siemersiii_wolf_1983]: https://doi.org/10.2514/6.1983-118
[research_sieradzki_2016]: https://doi.org/10.5604/05096669.1226890
[research_sigal_1984]: https://doi.org/10.2514/6.1984-2091
[research_silsbynormans_kennedyrobertm_1947]: https://ntrs.nasa.gov/citations/20050029399
[research_silva_1993]: https://doi.org/10.2514/6.1993-1590
[research_silva_bennett_1990]: https://doi.org/10.2514/6.1990-1033
[research_silva_bennett_1992]: https://doi.org/10.2514/6.1992-2082
[research_silva_bennett_1995]: https://doi.org/10.2514/3.46678
[research_silva_mello_2002]: https://doi.org/10.2514/6.2002-2971
[research_silva_mello_2004]: https://doi.org/10.2514/6.2004-5375
[research_silva_mello_2005]: https://doi.org/10.2514/6.2005-5098
[research_silva_mello_2006]: https://doi.org/10.2514/6.2006-2982
[research_silva_mello_2006_b]: https://doi.org/10.2514/1.16886
[research_silvershnorman_kingthomasjjr_1955]: https://ntrs.nasa.gov/citations/19930090325
[research_simag_curryre_1978]: https://ntrs.nasa.gov/citations/19790001897
[research_simag_curryre_1984]: https://ntrs.nasa.gov/citations/19870001438
[research_simalexg_1997]: https://ntrs.nasa.gov/citations/19970027378
[research_simpson_1972]: https://doi.org/10.2514/6.1972-785
[research_simpson_1979]: https://doi.org/10.21236/ada075226
[research_sims_carter_1981]: https://doi.org/10.2514/6.1981-2387
[research_simsek_tekinalp_2015]: https://doi.org/10.2514/6.2015-1480
[research_sinaga_yunianto_2024]: https://doi.org/10.47001/irjiet/2024.805038
[research_sinclair_1981]: https://doi.org/10.21236/ada093722
[research_sinclair_1988]: https://doi.org/10.2514/6.1988-2027
[research_sinclair_1996]: https://doi.org/10.2514/6.1996-2181
[research_singh_dwivedi_2022]: https://doi.org/10.47893/gret.2022.1050
[research_singh_karnick_2022]: https://doi.org/10.2514/6.2022-4172
[research_singh_mcdonough_2014]: https://doi.org/10.2514/6.2014-2050
[research_singh_mishra_2016]: https://doi.org/10.1007/s11668-016-0209-8
[research_singh_sasidharan_2026]: https://doi.org/10.2514/6.2026-4485
[research_singh_venkatraman_2023]: https://doi.org/10.2514/6.2023-1566
[research_singh_venkatraman_2026]: https://doi.org/10.2514/1.j065133
[research_singhasenee_lamon_2026]: https://doi.org/10.2514/6.2026-0319
[research_sinha_2007]: https://doi.org/10.2514/6.2007-4425
[research_sinha_2024]: https://doi.org/10.2514/6.2024-90621
[research_sinkovec_loshek_2015]: https://doi.org/10.2514/6.2015-1888
[research_sirieix_delery]: https://doi.org/10.1007/bfb0021336
[research_sisk_andrews_1963]: https://doi.org/10.2514/6.1963-1808
[research_siskthomasr_mooneyjohnm_1953]: https://ntrs.nasa.gov/citations/19930087506
[research_sivakrishnareddy_sah_2021]: https://doi.org/10.1088/1742-6596/2054/1/012013
[research_sivasubramanian_fasel_2015]: https://doi.org/10.2514/6.2015-2641
[research_sjobergsa_1950]: https://ntrs.nasa.gov/citations/19930086174
[research_sjobergsa_champinera_1949]: https://ntrs.nasa.gov/citations/19930085989
[research_sjobergsa_peelejamesr_1951]: https://ntrs.nasa.gov/citations/19930086520
[research_sklar_rusak_2020]: https://doi.org/10.2514/6.2020-0752
[research_sklenar_mateju_2022]: https://doi.org/10.3846/aviation.2022.15963
[research_skujins_cesnik_2011]: https://doi.org/10.2514/6.2011-6525
[research_slapnicar]: https://doi.org/10.14264/69b8f75
[research_slingerland_2003]: https://doi.org/10.2514/6.2003-6750
[research_slingerland_2005]: https://doi.org/10.2514/6.2005-815
[research_sloan_eh_1962]: https://doi.org/10.21236/ad0274219
[research_slotted_nlf_2024]: https://ntrs.nasa.gov/citations/20240014322
[research_small_disturbance_theory_1959]: https://doi.org/10.1016/b978-0-12-395596-8.50009-5
[research_smetana_1965]: https://doi.org/10.1017/s0001924000060140
[research_smetana_1973]: https://doi.org/10.21236/ad0763295
[research_smetana_knepper_1973]: https://doi.org/10.2514/3.44355
[research_smith_1953]: https://doi.org/10.21236/ad0007625
[research_smith_1966]: https://doi.org/10.21236/ad0639982
[research_smith_1997]: https://doi.org/10.4271/971478
[research_smith_babinsky_2004]: https://doi.org/10.2514/1.11479
[research_smith_cebeci_1967]: https://doi.org/10.21236/ad0656430
[research_smith_henfling_2008]: https://doi.org/10.2514/6.2008-832
[research_smith_karns_2026]: https://doi.org/10.2514/6.2026-4658
[research_smith_klettner_2022]: https://doi.org/10.1063/5.0120124
[research_smith_richards_2023]: https://doi.org/10.1093/mnras/stad2879
[research_smithccjr_1958]: https://ntrs.nasa.gov/citations/19710082837
[research_smithcharlescjr_1958]: https://ntrs.nasa.gov/citations/19980227972
[research_smithcharlescjr_1961]: https://ntrs.nasa.gov/citations/19980230621
[research_smithhc_1974]: https://ntrs.nasa.gov/citations/19740013410
[research_smithleighann_campbellrichardl_1992]: https://ntrs.nasa.gov/citations/19920024240
[research_smithnormanf_1954]: https://ntrs.nasa.gov/citations/19930088195
[research_smithronaldc_farbridgeje_1979]: https://ntrs.nasa.gov/citations/19990034126
[research_smithwilliardg_1954]: https://ntrs.nasa.gov/citations/20090025453
[research_smits_1988]: https://doi.org/10.21236/ada194164
[research_smits_miles_2002]: https://doi.org/10.21236/ada405454
[research_smolderen_1972]: https://doi.org/10.2514/3.58952
[research_snyder_1987]: https://doi.org/10.2514/6.1987-1162
[research_sobieczky_1979]: https://doi.org/10.2514/6.1979-1556
[research_sobieczky_1983]: https://doi.org/10.2514/6.1983-1862
[research_sobieczky_1984]: https://doi.org/10.1146/annurev.fluid.16.1.337
[research_sobieczky_dulikravich_1993]: https://doi.org/10.1117/12.152751
[research_sobieczky_giessler_1999]: https://doi.org/10.2514/6.1999-3127
[research_sogukpinar_2018]: https://doi.org/10.1063/1.5025956
[research_sohn_lee_2000]: https://doi.org/10.2514/6.2000-4523
[research_solartepineda_bravomosquera_2026]: https://doi.org/10.2514/1.c038573
[research_solies_1992]: https://doi.org/10.2514/3.46264
[research_solies_1992_b]: https://doi.org/10.2514/6.1992-4082
[research_solies_1994]: https://doi.org/10.2514/3.46495
[research_soltani_farahani_2011]: https://doi.org/10.1111/j.1747-1567.2011.00772.x
[research_soltani_marzabadi_2011]: https://doi.org/10.1111/j.1747-1567.2010.00696.x
[research_solution_of_2014]: https://doi.org/10.2514/5.9781624102646.0089.0102
[research_somers_2005]: https://doi.org/10.2172/15011667
[research_soneda_tsushima_2025]: https://doi.org/10.2514/6.2025-0819
[research_song_lu_2011]: https://doi.org/10.2514/1.c031038
[research_song_wong_2024]: https://doi.org/10.2514/6.2024-2148
[research_song_wong_2025]: https://doi.org/10.2514/6.2025-2185
[research_soontornpasatch_2018]: https://doi.org/10.1109/esit.2018.8665283
[research_soontornpasatch_2018_b]: https://doi.org/10.1088/1757-899x/405/1/012002
[research_sorbilli_dibianchi_2018]: https://doi.org/10.2514/6.2018-1653
[research_sorensen_blevins_2001]: https://doi.org/10.2514/6.2001-3520
[research_sotoudeh_ferman_2019]: https://doi.org/10.2514/6.2019-0762
[research_sotoudeh_hodges_2010]: https://doi.org/10.2514/1.46974
[research_soudakov_petrov_2017]: https://doi.org/10.2514/6.2017-0489
[research_soudakov_sidorenko_2017]: https://doi.org/10.2514/6.2017-0713
[research_southjr_1985]: https://doi.org/10.2514/6.1985-366
[research_souzacoimbra_matoscampos_2022]: https://doi.org/10.26678/abcm.encit2022.cit22-0442
[research_spacht_1980]: https://doi.org/10.2514/6.1980-1885
[research_spahr_kyrlach_1960]: https://doi.org/10.2172/4138802
[research_spaid_1984]: https://doi.org/10.2514/6.1984-100
[research_spaid_lynch_1996]: https://doi.org/10.2514/6.1996-682
[research_spaidfw_dahlinja_1983]: https://ntrs.nasa.gov/citations/19830025575
[research_sparkes_2024]: https://doi.org/10.1016/s0262-4079(24)00111-8
[research_spearmanml_1979]: https://ntrs.nasa.gov/citations/19790063882
[research_spearmanmleroy_1953]: https://ntrs.nasa.gov/citations/19930087915
[research_spinner_rudnik_2023]: https://doi.org/10.2514/6.2023-0810
[research_spitzerre_rumseypc_1972]: https://ntrs.nasa.gov/citations/19720054463
[research_spottswood_beberniss_2015]: https://doi.org/10.21236/ada618183
[research_spreiter_1959]: https://doi.org/10.2514/8.8165
[research_spreiter_1964]: https://doi.org/10.1007/978-3-642-88337-8_12
[research_spring_tab_1946]: https://ntrs.nasa.gov/citations/19930092531
[research_springer_1998]: https://doi.org/10.2514/6.1998-2875
[research_spurlin_lueck_1984]: https://doi.org/10.2514/6.1984-612
[research_squire_1965]: https://doi.org/10.1017/s0001925900003474
[research_squire_1975]: https://doi.org/10.1017/s0001925900007149
[research_squire_nasser_1993]: https://doi.org/10.1017/s000192400002635x
[research_srakowski_shrewsbury_1980]: https://doi.org/10.2514/6.1980-1333
[research_srbland_1979]: https://ntrs.nasa.gov/citations/19800001963
[research_sreekanth_1961]: https://doi.org/10.21236/ad0258967
[research_sreekanth_1962]: https://doi.org/10.2514/8.6144
[research_sreenivasulu_neelapu_2025]: https://doi.org/10.61653/joast.v77i3.2025.1088
[research_srichitturi_2026]: https://doi.org/10.21203/rs.3.rs-11247822/v1
[research_sridharan_padmanabhan_2024]: https://doi.org/10.1109/aero58975.2024.10521013
[research_srinivasan_chyu_1981]: https://doi.org/10.2514/6.1981-1206
[research_srinivasan_mccroskey_1984]: https://doi.org/10.2514/6.1984-254
[research_srinivasan_mccroskey_1986]: https://doi.org/10.21236/ada169116
[research_srinivasang_stegerjl_1981]: https://ntrs.nasa.gov/citations/19820013285
[research_sriram_jagadeesh_2014]: https://doi.org/10.1016/j.ast.2014.04.003
[research_sriram_jagadeesh_2016]: https://doi.org/10.1017/aer.2016.45
[research_srivastava_bakhle_2002]: https://doi.org/10.1115/gt2002-30319
[research_srivastava_damodaran_2019]: https://doi.org/10.2514/6.2019-1527
[research_stacey]: https://doi.org/10.14264/e4e8d91
[research_stack_1935_16_airfoils]: https://ntrs.nasa.gov/citations/19930091566
[research_stack_1935_burble]: https://ntrs.nasa.gov/citations/19930081326
[research_stackjohn_1943]: https://ntrs.nasa.gov/citations/19930091842
[research_stackjohn_draleyeugenec_1950]: https://ntrs.nasa.gov/citations/19930092056
[research_staelens_blackwelder_2007]: https://doi.org/10.2514/6.2007-4176
[research_stahara_1981]: https://doi.org/10.21236/ada095376
[research_stahara_spreiter_1979]: https://doi.org/10.21236/ada068767
[research_stahara_spreiter_1980]: https://doi.org/10.2514/3.50731
[research_stallings_hartman_1981]: https://doi.org/10.21236/ada103383
[research_stallingsjr_1982]: https://doi.org/10.2514/6.1982-372
[research_stanewsky_basler_1989]: https://doi.org/10.1007/978-3-642-83584-1_38
[research_stanewsky_little_1971]: https://doi.org/10.2514/3.59192
[research_stanewskye_demurief_1984]: https://ntrs.nasa.gov/citations/19840015507
[research_stanford_jacobson_2023]: https://doi.org/10.2514/6.2023-0589
[research_stanford_jacobson_2024]: https://doi.org/10.2514/1.c037679
[research_stanford_massey_2026]: https://doi.org/10.2514/6.2026-0811
[research_stanford_sauer_2022]: https://doi.org/10.2514/6.2022-0632
[research_stanford_thelen_2024]: https://doi.org/10.2514/6.2024-4025
[research_stanford_thelen_2025]: https://doi.org/10.2514/1.j065151
[research_stanford_wieseman_2015]: https://doi.org/10.2514/6.2015-1127
[research_stardterh_1979]: https://ntrs.nasa.gov/citations/19830022164
[research_stargill_1983]: https://doi.org/10.2514/6.1983-2132
[research_starr_1975]: https://doi.org/10.21236/ada017666
[research_starr_1978]: https://doi.org/10.2514/6.1978-164
[research_starr_schueler_1973]: https://doi.org/10.2514/6.1973-212
[research_starr_varner_1976]: https://doi.org/10.2514/6.1976-90
[research_static_aeroelasticity_2014]: https://doi.org/10.1002/9781118700440.ch7
[research_static_longitudinal_2003]: https://doi.org/10.2514/5.9781600861840.0223.0233
[research_steady_transonic_2015]: https://doi.org/10.1201/b19396-13
[research_stebbins_loth_2019]: https://doi.org/10.2514/6.2019-0328
[research_steelant_2002]: https://doi.org/10.1016/b978-008044114-6/50019-3
[research_steer_2000]: https://doi.org/10.2514/6.2000-4109
[research_steer_2003]: https://doi.org/10.2514/6.2003-5308
[research_steger_bailey_1979]: https://doi.org/10.2514/6.1979-134
[research_steger_bailey_1980]: https://doi.org/10.2514/3.50756
[research_steger_klineberg_1973]: https://doi.org/10.2514/3.50502
[research_stegerjl_baldwinbs_1972]: https://ntrs.nasa.gov/citations/19730001587
[research_stegmuller_haybock_2026]: https://doi.org/10.2514/1.c038577
[research_steimle_karhoff_2012]: https://doi.org/10.2514/1.j051187
[research_steimle_schroder_2008]: https://doi.org/10.2514/6.2008-6908
[research_steimle_schroder_2010]: https://doi.org/10.1007/978-3-642-04088-7_13
[research_steinle_hawkins_2004]: https://doi.org/10.2514/6.2004-2494
[research_steinle_jr_1999]: https://doi.org/10.21236/ada370968
[research_stengel_1969]: https://doi.org/10.2514/6.1969-813
[research_stephencorda_michaeljakevachon_2003]: https://ntrs.nasa.gov/citations/20030053340
[research_steppert_epple_2017]: https://doi.org/10.1115/imece2017-71872
[research_sternberg_1954]: https://doi.org/10.21236/ad0045102
[research_stetson_1981]: https://doi.org/10.2514/6.1981-1226
[research_stevensjosephe_1950]: https://ntrs.nasa.gov/citations/20050030014
[research_stevensjosephe_1955]: https://ntrs.nasa.gov/citations/20050029377
[research_stevensjosephe_purserpaule_1955]: https://ntrs.nasa.gov/citations/19930088595
[research_stevensonjr_1981]: https://ntrs.nasa.gov/citations/19810022602
[research_stewart_walters_1996]: https://doi.org/10.4050/vfs-f52-2032
[research_stillwellwh_wilmerdingjv_1951]: https://ntrs.nasa.gov/citations/19930086606
[research_stock_1975]: https://doi.org/10.1016/0017-9310(75)90165-9
[research_stock_2002]: https://doi.org/10.1016/s1270-9638(02)01166-5
[research_stolikerpatrickc_carterjohn_2003]: https://ntrs.nasa.gov/citations/20110023811
[research_stone_1945]: https://doi.org/10.21236/ada801302
[research_strack_1964]: https://doi.org/10.2514/3.2412
[research_strampp_1983]: https://doi.org/10.1016/0020-7462(83)90030-6
[research_strand_1960]: https://doi.org/10.2514/8.8662
[research_streather_1972]: https://doi.org/10.1017/s0001924000043426
[research_street_1979]: https://doi.org/10.2514/6.1979-304
[research_streett_1981]: https://doi.org/10.2514/6.1981-1266
[research_streett_1982]: https://doi.org/10.2514/3.51149
[research_streett_1983]: https://doi.org/10.2514/6.1983-1949
[research_stremel_1993]: https://doi.org/10.2514/6.1993-206
[research_strganac_1988]: https://doi.org/10.2514/6.1988-2033
[research_strike_wt_1982]: https://doi.org/10.21236/ada116279
[research_striz_1991]: https://doi.org/10.21236/ada248487
[research_strome_1969]: https://doi.org/10.21236/ad0865977
[research_strutzlw_1972]: https://ntrs.nasa.gov/citations/19720023253
[research_stubblefield_kunz_2025]: https://doi.org/10.1016/j.jfluidstructs.2025.104278
[research_studwell_wu_1973]: https://doi.org/10.2514/3.60273
[research_study_on_2023]: https://doi.org/10.1063/5.0138636
[research_study_on_2023_b]: https://doi.org/10.1063/5.0155076
[research_sturek_schiff_1980]: https://doi.org/10.2514/6.1980-1586
[research_su_chow_1993]: https://doi.org/10.2514/6.1993-3024
[research_su_chow_1995]: https://doi.org/10.2514/3.46815
[research_subramani_m_2025]: https://doi.org/10.1108/aeat-04-2024-0109
[research_sudani_sato_1993]: https://doi.org/10.2514/6.1993-90
[research_sudani_sato_2001]: https://doi.org/10.2514/6.2001-2423
[research_sudani_sato_2003]: https://doi.org/10.2514/2.3071
[research_sudhi_radespiel_2021]: https://doi.org/10.2514/6.2021-2606
[research_sugioka_2021]: https://doi.org/10.1007/s00348-020-03118-y
[research_sugioka_koike_2018]: https://doi.org/10.1007/s00348-018-2565-5
[research_sugioka_nakajima_2023]: https://doi.org/10.1088/1361-6501/acf8e2
[research_sugioka_nakajima_2026]: https://doi.org/10.1016/j.ast.2026.112729
[research_sugioka_nakakita_2018]: https://doi.org/10.2514/6.2018-1030
[research_sugioka_numata_2015]: https://doi.org/10.2514/6.2015-0025
[research_suleman_crawford_2000]: https://doi.org/10.1115/imece2000-1711
[research_sun]: https://doi.org/10.14711/thesis-991012638163603412
[research_sun_hansen_1982]: https://doi.org/10.2514/6.1982-308
[research_sun_hu_2005]: https://doi.org/10.1515/ijnsns.2005.6.1.25
[research_sun_miao_2020]: https://doi.org/10.1063/5.0018763
[research_sun_wang_2021]: https://doi.org/10.1063/5.0060604
[research_sun_zhang_2025]: https://doi.org/10.2139/ssrn.5251753
[research_sun_zhang_2026]: https://doi.org/10.1016/j.ast.2025.110841
[research_sundaram_wu_1983]: https://doi.org/10.2514/6.1983-1852
[research_supercritical_17pct_1972]: https://ntrs.nasa.gov/citations/19830002804
[research_supercritical_airfoil]: https://doi.org/10.1007/3-540-11499-8_5
[research_supercritical_body_1971]: https://ntrs.nasa.gov/citations/19720004249
[research_supersonic_cruise_1981]: https://doi.org/10.1016/b978-0-444-41961-3.50017-6
[research_supersonic_flight_2014]: https://doi.org/10.2307/j.ctv15wxpxz.9
[research_supersonic_flight_2025]: https://doi.org/10.1002/9781394309290.ch5
[research_supersonic_maneuvers_1981]: https://doi.org/10.1016/b978-0-444-41961-3.50019-x
[research_supersonic_research_1995]: https://ntrs.nasa.gov/citations/19960016997
[research_supersonic_turn_1981]: https://doi.org/10.1016/b978-0-444-41961-3.50018-8
[research_sutherland_1893]: https://doi.org/10.1080/14786449308620508
[research_suwa_nose_2012]: https://doi.org/10.2514/6.2012-3029
[research_suzuki_rinoie_2010]: https://doi.org/10.2514/1.46152
[research_swafford_1979]: https://doi.org/10.21236/ada067423
[research_swafford_bomba_1995]: https://doi.org/10.2514/6.1995-1839
[research_swamy_ahmed_1978]: https://doi.org/10.2514/6.1978-809
[research_symington_1940]: https://doi.org/10.4271/400114
[research_szema_shankar_1984]: https://doi.org/10.2514/6.1984-427
[research_szodruchj_1980]: https://ntrs.nasa.gov/citations/19810005753
[research_szubert_grossi_2015]: https://doi.org/10.1016/j.jfluidstructs.2015.03.005
[research_szulc_doerffer_2023]: https://doi.org/10.1108/hff-06-2023-0338
[research_szwaba_2005]: https://doi.org/10.1007/s11630-005-0009-z
[research_szwaba_doerffer_2017]: https://doi.org/10.1007/978-3-319-44866-4_60
[research_szwabowski_baker_2023]: https://doi.org/10.2514/6.2023-3949
[research_tacina_fernandez_2004]: https://doi.org/10.2514/6.2004-2719
[research_tai_1986]: https://doi.org/10.1007/978-3-642-82770-9_6
[research_tai_kidwell_1985]: https://doi.org/10.2514/3.45217
[research_tai_kidwelljr_1984]: https://doi.org/10.2514/6.1984-2162
[research_taillonnormanv_1958]: https://ntrs.nasa.gov/citations/19930090061
[research_taitszec_husongregoryg_1987]: https://ntrs.nasa.gov/citations/19870055062
[research_takahashi_2013]: https://doi.org/10.2514/6.2013-281
[research_takahashi_2021]: https://doi.org/10.1299/jsmecmd.2021.34.163
[research_takahashi_2021_b]: https://doi.org/10.23967/coupled.2021.040
[research_takahashi_2026_airdata]: https://doi.org/10.2514/1.j065479
[research_takahashi_boccieri_2019]: https://doi.org/10.2514/6.2019-0813
[research_takahashi_german_2010]: https://doi.org/10.2514/6.2010-846
[research_takahashi_stone_2019]: https://doi.org/10.2514/6.2019-1309
[research_takanashi_1984]: https://doi.org/10.2514/6.1984-2155
[research_takanashi_1985]: https://doi.org/10.2514/3.45182
[research_takikawa_hosono_2025]: https://doi.org/10.1007/978-981-96-4775-0_18
[research_takovitskii_2003]: https://doi.org/10.1023/b:flui.0000015235.61628.78
[research_takovitskii_2003_b]: https://doi.org/10.1016/s0021-8928(03)90044-x
[research_takovitskii_2006]: https://doi.org/10.1007/s10697-006-0045-8
[research_takovitskii_2006_b]: https://doi.org/10.1016/j.jappmathmech.2006.07.017
[research_takovitskii_2016]: https://doi.org/10.1615/tsagiscij.2017019462
[research_takovitskii_2018]: https://doi.org/10.1134/s0015462818060095
[research_takovitskii_2020]: https://doi.org/10.2514/6.2020-3120
[research_takovitskii_2022]: https://doi.org/10.1134/s0015462822050111
[research_takovitskii_2023]: https://doi.org/10.61653/joast.v61i1.2009.632
[research_takovitskii_2024]: https://doi.org/10.1134/s0015462823602966
[research_takuma_hagita_2026]: https://doi.org/10.1063/5.0319443
[research_tam_1989]: https://doi.org/10.2514/6.1989-1088
[research_tam_ju_2011]: https://doi.org/10.2514/6.2011-2711
[research_tamada_shibaoka_1955]: https://doi.org/10.2514/8.3325
[research_tamaki_kawai_2023]: https://doi.org/10.2514/6.2023-0429
[research_tamayama_kheirandish_2003]: https://doi.org/10.2322/tjsass.46.186
[research_tamba_tuan_2017]: https://doi.org/10.1007/978-3-319-46213-4_105
[research_tan_2020]: https://doi.org/10.34238/tnu-jst.3614
[research_tan_xu_2024]: https://doi.org/10.1063/5.0189252
[research_tanaka_isoda_2024]: https://doi.org/10.1299/jfst.2024jfst0033
[research_tang_jiang_2000]: https://doi.org/10.2514/6.2000-797
[research_tang_liu_2003]: https://doi.org/10.1007/978-94-010-0017-8_9
[research_tang_tan_2023]: https://doi.org/10.1109/itnec56291.2023.10082199
[research_tangmh_1971]: https://ntrs.nasa.gov/citations/19710015105
[research_tangmh_pearsongpe_1971]: https://ntrs.nasa.gov/citations/19710029224
[research_tanner_1963]: https://doi.org/10.21236/ad0418754
[research_tao_li_2016]: https://doi.org/10.1016/j.cja.2016.10.018
[research_tao_sun_2019]: https://doi.org/10.1016/j.ast.2019.06.041
[research_tao_zhao_2018]: https://doi.org/10.1142/s0217984918400407
[research_tao_zheng_2023]: https://doi.org/10.1117/12.2681882
[research_taraborrelli_2023]: https://doi.org/10.21741/9781644902813-92
[research_taranto_abdulrahim_2023]: https://doi.org/10.2514/6.2023-71776
[research_tatsumi_takanashi_1985]: https://doi.org/10.2514/6.1985-4077
[research_taylor_1951]: https://doi.org/10.21236/ad0044274
[research_taylor_2012]: https://doi.org/10.2514/6.2012-4410
[research_taylor_ratnayake_2011]: https://doi.org/10.2514/6.2011-6276
[research_tempelmeyerkennethe_osborneroberts_1955]: https://ntrs.nasa.gov/citations/20050029389
[research_teperin_teperina_2018]: https://doi.org/10.1615/tsagiscij.2018029236
[research_terakado_nonomura_2016]: https://doi.org/10.2514/6.2016-3015
[research_terashima_fujii_2003]: https://doi.org/10.1007/978-3-642-59334-5_52
[research_terashima_fujii_2004]: https://doi.org/10.2514/6.2004-2234
[research_terashima_fujii_2007]: https://doi.org/10.2514/1.24489
[research_tetervin_1963]: https://doi.org/10.21236/ad0400708
[research_tetrault_schetz_2000]: https://doi.org/10.2514/6.2000-509
[research_tewari_1993]: https://doi.org/10.2514/3.46445
[research_thacker_lan_1993]: https://doi.org/10.2514/6.1993-3617
[research_thawait_tandaiya_2022]: https://doi.org/10.1615/tfec2022.aer.040842
[research_the_effects_1989]: https://doi.org/10.2514/6.1989-836
[research_the_phenomenon_1931]: https://doi.org/10.1108/eb029365
[research_theodorsen_1935]: https://ntrs.nasa.gov/citations/19800006788
[research_thiede_krogmann_1986]: https://doi.org/10.1007/978-3-642-82770-9_10
[research_thiede_krogmann_1989]: https://doi.org/10.1007/978-3-642-83584-1_30
[research_thivet_saintmartin_1999]: https://doi.org/10.2514/6.1999-525
[research_thomas_1991]: https://doi.org/10.21236/ada247792
[research_thomas_agarwal_2022]: https://doi.org/10.2514/6.2022-0463
[research_thomas_agarwal_2025]: https://doi.org/10.2514/6.2025-0031
[research_thomas_dowell_2001]: https://doi.org/10.2514/6.2001-1209
[research_thomas_dowell_2011]: https://doi.org/10.2514/6.2011-2077
[research_thomas_dowell_2015]: https://doi.org/10.2514/6.2015-3435
[research_thomas_dowell_2020]: https://doi.org/10.2514/6.2020-3137
[research_thomas_holst_1983]: https://doi.org/10.2514/6.1983-499
[research_thomas_lan_1991]: https://doi.org/10.2514/6.1991-3300
[research_thompson_1966]: https://doi.org/10.2514/6.1966-838
[research_thompson_epstein_1977]: https://doi.org/10.21236/ada042231
[research_thompsonrobertf_moseleywilliamcjr_1956]: https://ntrs.nasa.gov/citations/19930089197
[research_thomson_1946]: https://doi.org/10.1115/1.4018403
[research_threadgill_bruce_2014]: https://doi.org/10.2514/6.2014-0439
[research_three_dimensional_boundary_layer_1994]: https://doi.org/10.2514/6.1994-2375
[research_tian_feng_2017]: https://doi.org/10.2514/1.c033574
[research_tian_gao_2017]: https://doi.org/10.1016/j.cja.2017.07.011
[research_tianshuliu_davidmsalazar_2021]: https://ntrs.nasa.gov/citations/20210013539
[research_tidbury_1945]: https://doi.org/10.1108/eb031263
[research_tijdeman_vannunen_1979]: https://doi.org/10.21236/ada071420
[research_tijdeman_vannunen_1979_b]: https://doi.org/10.21236/ada077370
[research_tilmann_2001]: https://doi.org/10.2514/6.2001-731
[research_tilmans_jackisch_2024]: https://doi.org/10.21203/rs.3.rs-4420771/v1
[research_time_dependent_in_flight]: https://doi.org/10.4271/air5020
[research_timme_thormann_2016]: https://doi.org/10.2514/6.2016-3848
[research_timofeev_aniskin_2018]: https://doi.org/10.1063/1.5065283
[research_timothychau_jaredcduensing]: https://ntrs.nasa.gov/citations/20250006220
[research_ting_nguyen_2014]: https://doi.org/10.2514/6.2014-0837
[research_tinney_2014]: https://doi.org/10.21236/ada613848
[research_tischler_2018]: https://doi.org/10.1201/9781315136820-2
[research_titchener_babinsky_2015]: https://doi.org/10.1007/s00193-015-0551-x
[research_titus_alexander_2013]: https://doi.org/10.1063/1.4799176
[research_tjatra_kapania_1992]: https://doi.org/10.1016/0956-0521(92)90100-w
[research_tkalenko_1969]: https://doi.org/10.1007/bf01032473
[research_tleulinov_jafarzade_2019]: https://doi.org/10.1088/1742-6596/1158/4/042027
[research_to_simiriotis_2019]: https://doi.org/10.1016/j.jfluidstructs.2019.02.011
[research_tobakmurray_lessinghenryc_1961]: https://ntrs.nasa.gov/citations/20150018562
[research_token_1974]: https://doi.org/10.21236/ada002685
[research_tokugawa_yoshida_2006]: https://doi.org/10.2514/6.2006-3165
[research_tomek_boyden_2000]: https://doi.org/10.2514/6.2000-266
[research_tomek_hall_2002]: https://doi.org/10.2514/6.2002-418
[research_tomita_1959]: https://doi.org/10.1299/jsme1958.2.663
[research_toot_1989]: https://doi.org/10.1007/978-3-642-84010-4_27
[research_torres_rahai_2024]: https://doi.org/10.1115/fedsm2024-129793
[research_touber_sandham_2009]: https://doi.org/10.1007/s00193-009-0222-x
[research_tournier_paduano_2005]: https://doi.org/10.2514/6.2005-4734
[research_tourrette_1993]: https://doi.org/10.2514/6.1993-3110
[research_tourrette_1996]: https://doi.org/10.2514/6.1996-2034
[research_trailing_edge_2006]: https://doi.org/10.2514/5.9781600866838.0245.0276
[research_tranen_1974]: https://doi.org/10.2514/6.1974-501
[research_transition_flight_1958]: https://ntrs.nasa.gov/citations/19630008170
[research_transonic_2d_1973]: https://ntrs.nasa.gov/citations/19730051411
[research_transonic_aerodynamics_1982]: https://doi.org/10.2514/4.865558
[research_transonic_aerodynamics_1986]: https://doi.org/10.1016/c2009-0-09683-4
[research_transonic_aerodynamics_1993]: https://doi.org/10.1137/1.9781611970975
[research_transonic_aerodynamics_history_1982]: https://doi.org/10.2514/5.9781600865558.0003.0079
[research_transonic_aircraft_2012]: https://doi.org/10.2514/5.9781600869174.0171.0220
[research_transonic_airfoil_1986]: https://doi.org/10.1016/b978-0-444-87958-5.50008-x
[research_transonic_airfoil_2011]: https://doi.org/10.5220/0003646204740482
[research_transonic_airfoil_2015]: https://doi.org/10.1142/9781783266296_0010
[research_transonic_and_1992]: https://doi.org/10.1017/cbo9780511607134.012
[research_transonic_and_2012]: https://doi.org/10.2514/5.9781600869174.0129.0170
[research_transonic_computational_1982]: https://doi.org/10.2514/5.9781600865558.0451.0465
[research_transonic_conference_1949]: https://ntrs.nasa.gov/citations/19650074048
[research_transonic_correction_2021]: https://ntrs.nasa.gov/citations/20210018198
[research_transonic_design_1982]: https://doi.org/10.2514/5.9781600865558.0377.0402
[research_transonic_drag_wingbody_1948]: https://ntrs.nasa.gov/citations/19930093786
[research_transonic_expansion_1986]: https://doi.org/10.1016/b978-0-444-87958-5.50006-6
[research_transonic_far_1986]: https://doi.org/10.1016/b978-0-444-87958-5.50007-8
[research_transonic_flight_1994]: https://doi.org/10.2514/6.1994-2142
[research_transonic_maneuver_cruise_1980]: https://doi.org/10.2514/5.9781600865466.0187.0211
[research_transonic_navier_stokes_1972]: https://doi.org/10.2514/3.46413
[research_transonic_predict_1957]: https://ntrs.nasa.gov/citations/19660024789
[research_transonic_regular_2007]: https://doi.org/10.1201/9781420011159-10
[research_transonic_shock_1982]: https://doi.org/10.1016/c2013-0-11177-4
[research_transonic_summary_1959]: https://ntrs.nasa.gov/citations/19980228028
[research_transonic_wind_1982]: https://doi.org/10.2514/6.1982-588
[research_transonic_wing_2005]: https://doi.org/10.5139/jksas.2005.33.10.010
[research_transonic_wing_2015]: https://doi.org/10.1142/9781783266296_0011
[research_transonic_wingbody_1974]: https://ntrs.nasa.gov/citations/19740036062
[research_trefny_2020]: https://doi.org/10.2514/6.2020-3771
[research_trenker_2003]: https://doi.org/10.2514/2.3152
[research_trenker_geissler_2000]: https://doi.org/10.2514/6.2000-4419
[research_triebstein_1986]: https://doi.org/10.2514/3.45291
[research_trilling_covert_1955]: https://doi.org/10.2514/8.3413
[research_trimmer_clark_1963]: https://doi.org/10.21236/ad0422287
[research_tripathi_mistri_2023]: https://doi.org/10.2514/6.2023-2110
[research_triplett_1980]: https://doi.org/10.2514/6.1980-794
[research_triplett_1982]: https://doi.org/10.2514/6.1982-641
[research_triplett_1983]: https://doi.org/10.2514/3.48193
[research_triplett_kappus_1973]: https://doi.org/10.2514/6.1973-194
[research_tsien_2012]: https://doi.org/10.1016/b978-0-12-398277-3.50008-7
[research_tsien_kuo_2012]: https://doi.org/10.1016/b978-0-12-398277-3.50019-1
[research_tsienhsueshen_1944]: https://ntrs.nasa.gov/citations/19930085006
[research_tsushima_saitoh_2023]: https://doi.org/10.1016/j.ast.2023.108476
[research_tsutsumi_takaki_2012]: https://doi.org/10.2514/6.2012-2900
[research_tuan_malatesta_2024]: https://doi.org/10.1007/s40430-024-05272-4
[research_tuck_dostovalova_2000]: https://doi.org/10.1017/s0001924000091880
[research_tunnurhanis_ambareenkhan_2023]: https://doi.org/10.37934/arfmts.109.1.210225
[research_tuovilawj_hessrobertw_1959]: https://ntrs.nasa.gov/citations/19630008165
[research_turbeville_schneider_2021]: https://doi.org/10.2514/6.2021-2878
[research_turbojet_and_1964]: https://doi.org/10.2514/6.1964-244
[research_turner_1982]: https://doi.org/10.2514/3.44757
[research_turner_seo_2023]: https://doi.org/10.2514/6.2023-0083
[research_turner_seo_2024]: https://doi.org/10.2514/1.j063142
[research_turner_seo_2024_b]: https://doi.org/10.2514/6.2024-1354
[research_turner_seo_2025]: https://doi.org/10.2514/6.2025-1494
[research_tursi_2003]: https://doi.org/10.2514/6.2003-3787
[research_ueda_1983]: https://doi.org/10.2514/6.1983-958
[research_uedat_dowelleh_1984]: https://ntrs.nasa.gov/citations/19840038716
[research_ueno_miwa_2001]: https://doi.org/10.2514/6.2001-406
[research_ueno_sudani_2008]: https://doi.org/10.2514/6.2008-849
[research_ueno_yamamoto_2007]: https://doi.org/10.2514/6.2007-4566
[research_ulbrich_2002]: https://doi.org/10.2514/6.2002-307
[research_ulbrich_2010]: https://doi.org/10.2514/6.2010-742
[research_ulbrich_boone_1998]: https://doi.org/10.2514/6.1998-707
[research_ulbrich_boone_2001]: https://doi.org/10.2514/6.2001-1112
[research_ulbrich_boone_2004]: https://doi.org/10.2514/6.2004-605
[research_ulbrichn_amayam_2018]: https://ntrs.nasa.gov/citations/20180000582
[research_ulbrichnorbert_boonealanr_2003]: https://ntrs.nasa.gov/citations/20040081237
[research_ullah_kamoun_2022]: https://doi.org/10.2514/6.2022-1334
[research_ullah_lutz_2021]: https://doi.org/10.2514/6.2021-1831
[research_ulug_cigeroglu_2025]: https://doi.org/10.13052/97887-438-0146-7_15
[research_umutlu_kiral_2022]: https://doi.org/10.52460/issc.2022.047
[research_unangstjohnr_1959]: https://ntrs.nasa.gov/citations/19980236841
[research_uncertainty_of]: https://doi.org/10.4271/air1678a
[research_unsteady_supersonic_1981]: https://doi.org/10.2514/6.1981-1874
[research_unsteady_transonic_1989]: https://doi.org/10.2514/4.865947
[research_unswept_stability_1959]: https://ntrs.nasa.gov/citations/19980228241
[research_urie_reaser_1979]: https://doi.org/10.2514/6.1979-1653
[research_usryjimmyw_meyersjamesf_1991]: https://ntrs.nasa.gov/citations/20040121158
[research_utkina_kozelkov_2023]: https://doi.org/10.3390/fluids8100276
[research_uzun_malik_2018]: https://doi.org/10.2514/6.2018-3854
[research_uzun_malik_2019]: https://doi.org/10.2514/1.j057850
[research_vachonmichaeljacob_rayronaldj_2004]: https://ntrs.nasa.gov/citations/20040013408
[research_vadillo_agarwal]: https://doi.org/10.1007/3-540-31801-1_50
[research_vadillo_agarwal_2005]: https://doi.org/10.2514/6.2005-486
[research_vadillo_agarwal_2007]: https://doi.org/10.2514/6.2007-712
[research_vadillo_agarwal_2009]: https://doi.org/10.1007/978-3-540-92779-2_91
[research_vagliolaurin_1978]: https://doi.org/10.21236/ada064645
[research_vaisakh_muruganandam_2018]: https://doi.org/10.1177/0954410018793789
[research_vaisakh_ramprakash_2019]: https://doi.org/10.1007/978-3-319-91020-8_135
[research_vaiuso_immordino_2025]: https://doi.org/10.2139/ssrn.5084491
[research_vaiuso_immordino_2025_b]: https://doi.org/10.2139/ssrn.5152963
[research_valarezo_dominik_1993]: https://doi.org/10.2514/3.46399
[research_valarezowaltero_dominikchetj_1992]: https://ntrs.nasa.gov/citations/19930018257
[research_vanarnhem_devries_2019]: https://doi.org/10.2514/6.2019-3036
[research_vandam_1986]: https://doi.org/10.2514/6.1986-1824
[research_vandam_hicks_1990]: https://doi.org/10.2514/6.1990-3212
[research_vandervooren_2008]: https://doi.org/10.1016/j.ast.2007.11.001
[research_vandervooren_vanderkolk_1982]: https://doi.org/10.2514/6.1982-935
[research_vandervooren_vanderwees_1990]: https://doi.org/10.2514/6.1990-576
[research_vanderwyst_2008]: https://doi.org/10.2514/6.2008-6583
[research_vandommelen_dsilva_2019]: https://doi.org/10.2514/6.2019-3569
[research_vanes_2002]: https://doi.org/10.2514/2.2997
[research_vanes_2003]: https://doi.org/10.2514/2.3106
[research_vanwezel_pool_2025]: https://doi.org/10.2514/6.2025-1252
[research_varner_1974]: https://doi.org/10.2514/6.1974-633
[research_varwig_1963]: https://doi.org/10.21236/ad0403045
[research_vasconcelos_leite_2011]: https://doi.org/10.1109/sibgrapi.2011.38
[research_vasenev_kharitonov_1991]: https://doi.org/10.1007/978-3-642-84447-8_46
[research_vasilchenko_1981]: https://doi.org/10.1007/bf01092388
[research_vasilev_1966]: https://doi.org/10.1007/bf01022289
[research_vatsa_1987]: https://doi.org/10.2514/3.45456
[research_vatsa_wedan_1988]: https://doi.org/10.2514/6.1988-102
[research_vaughnjr_1982]: https://doi.org/10.2514/6.1982-414
[research_vavalle_qin_2007]: https://doi.org/10.2514/1.19688
[research_vayala_sriram_2024]: https://doi.org/10.1007/978-981-97-6099-2_6
[research_vayala_vadlamani_2025]: https://doi.org/10.1063/5.0246043
[research_velasquez_2013]: https://doi.org/10.32855/2642-2492.1597
[research_veldman_2005]: https://doi.org/10.2514/6.2005-4801
[research_veletas_2026]: https://doi.org/10.2514/6.2026-2636
[research_velichko_lifshits_1983]: https://doi.org/10.1007/bf01091104
[research_velkova_2017]: https://doi.org/10.19062/1842-9238.2017.15.3.1
[research_veltin_day_2010]: https://doi.org/10.2514/6.2010-3924
[research_veras_souzademouralima_2022]: https://doi.org/10.4271/2022-01-0025
[research_verhaagen_1997]: https://doi.org/10.21236/ada327879
[research_verhoff_2005]: https://doi.org/10.2514/6.2005-5193
[research_verma_chidambaranathan_2022]: https://doi.org/10.2514/1.j061678
[research_verma_haidn_2009]: https://doi.org/10.1007/s00193-009-0211-0
[research_verma_manisankar_2018]: https://doi.org/10.2514/1.j056460
[research_verma_manisankar_2024]: https://doi.org/10.2514/1.j064000
[research_verma_rathakrishnan_2002]: https://doi.org/10.1515/tjj.2002.19.3.179
[research_vernacchia_2022]: https://doi.org/10.2514/1.b38104
[research_vianto_tobing_2021]: https://doi.org/10.47355/avia.v3i2.49
[research_vicini_quagliarella_1997]: https://doi.org/10.2514/6.1997-82
[research_vidal_wittliff_1973]: https://doi.org/10.2514/6.1973-661
[research_vidalrj_ericksonjcjr_1976]: https://ntrs.nasa.gov/citations/19760018136
[research_viegas_rubesin_1991]: https://doi.org/10.2514/6.1991-1783
[research_viegas_rubesin_1992]: https://doi.org/10.2514/3.11235
[research_vigneswaran_2026]: https://doi.org/10.1063/5.0349190
[research_vijgen_dodbele_1988]: https://doi.org/10.2514/6.1988-8
[research_vijgen_vandam_1990]: https://doi.org/10.2514/3.10537
[research_vikramaditya_viji_2023]: https://doi.org/10.21203/rs.3.rs-2998770/v1
[research_vincent_botez_2015]: https://doi.org/10.2514/6.2015-0904
[research_vindigni_2024]: https://doi.org/10.21741/9781644903193-27
[research_vindigni_mantegna_2024]: https://doi.org/10.1016/j.jsv.2023.118151
[research_vindigni_mantegna_2024_b]: https://doi.org/10.1088/1742-6596/2746/1/012007
[research_vinh_tzeng_1993]: https://doi.org/10.2514/6.1993-3659
[research_vinh_tzeng_1994]: https://doi.org/10.2514/6.1994-3469
[research_vinhlamson_edwardsjohnw_1988]: https://ntrs.nasa.gov/citations/19880063385
[research_vinodh_sridhar_2023]: https://doi.org/10.1007/978-3-031-37160-8_35
[research_vinoth_rathakrishnan_2005]: https://doi.org/10.1007/bf03181544
[research_visbal_1988]: https://doi.org/10.2514/6.1988-132
[research_vishwanathan]: https://doi.org/10.33915/etd.1816
[research_viswanath_1988]: https://doi.org/10.2514/3.45586
[research_viswanath_brown_1982]: https://doi.org/10.2514/6.1982-348
[research_viswanath_brown_1983]: https://doi.org/10.2514/3.8156
[research_viswanath_mukund_1995]: https://doi.org/10.2514/3.12838
[research_viswanath_patil_1997]: https://doi.org/10.2514/2.3231
[research_viswanath_rajendra_1990]: https://doi.org/10.1017/s0001924000023095
[research_viswanath_sankaran_1978]: https://doi.org/10.2514/6.1978-1168
[research_viswanath_sankaran_1983]: https://doi.org/10.2514/3.44935
[research_viswanathpr_brownjl_1982]: https://ntrs.nasa.gov/citations/19830005122
[research_vittalshenoy_gojon_2023]: https://doi.org/10.1177/1475472x221150173
[research_vkrzywoblocki_1960]: https://doi.org/10.1007/978-3-7091-3994-3_5
[research_vlasyk_korshunova_2025]: https://doi.org/10.18372/1990-5548.86.20555
[research_voet_speth_2023]: https://doi.org/10.2514/6.2023-3725
[research_voglerraymondd_1956]: https://ntrs.nasa.gov/citations/19930089402
[research_volkl_weiner_2026]: https://doi.org/10.2139/ssrn.7193341
[research_volkova_2021]: https://doi.org/10.34759/vst-2021-4-28-38
[research_volkova_ivanov_2020]: https://doi.org/10.34759/vst-2020-3-37-48
[research_volpe_1986]: https://doi.org/10.2514/6.1986-1819
[research_volpe_grossman_1978]: https://doi.org/10.21236/ada058425
[research_volpe_jameson_1990]: https://doi.org/10.2514/3.45923
[research_vondoenhoffalberte_stiverslouiss_1947]: https://ntrs.nasa.gov/citations/19930081886
[research_vonknoblauch_moreno_2014]: https://doi.org/10.2514/6.2014-0676
[research_voracekdavid_2007]: https://ntrs.nasa.gov/citations/20070024435
[research_vortex_generator_1952]: https://ntrs.nasa.gov/citations/20050041843
[research_vos_farokhi_2015]: https://doi.org/10.1007/978-94-017-9747-4_7
[research_vos_farokhi_2015_b]: https://doi.org/10.1007/978-94-017-9747-4_3
[research_vos_farokhi_2015_c]: https://doi.org/10.1007/978-94-017-9747-4_8
[research_vos_farokhi_2015_d]: https://doi.org/10.1007/978-94-017-9747-4
[research_vos_vaessen_2013]: https://doi.org/10.2514/6.2013-4299
[research_vozhdaev_teperin_2020]: https://doi.org/10.1615/tsagiscij.2020034176
[research_vukasinovic_gissen_2013]: https://doi.org/10.2514/6.2013-529
[research_vyasmanana_waindimmbu_2016]: https://ntrs.nasa.gov/citations/20170000245
[research_vyasmanana_yoderdennisa_2018]: https://ntrs.nasa.gov/citations/20180001494
[research_vyasmanana_yoderdennisa_2019]: https://ntrs.nasa.gov/citations/20190025709
[research_wada_1924]: https://doi.org/10.1299/jsmemagazine.27.90_869
[research_waggoner_1980]: https://doi.org/10.2514/6.1980-129
[research_waggoner_1982]: https://doi.org/10.2514/6.1982-163
[research_wagner_1982]: https://doi.org/10.1007/978-3-642-81932-2_29
[research_wagner_1985]: https://doi.org/10.21236/ada379810
[research_wahls_owens_2001]: https://doi.org/10.2514/6.2001-912
[research_wai_yoshihara_1982]: https://doi.org/10.1007/978-3-662-12610-3_28
[research_wai_yoshihara_1984]: https://doi.org/10.2514/6.1984-265
[research_wainwright_1962]: https://doi.org/10.21236/ad0297175
[research_waisanen_perangelo_1972]: https://doi.org/10.2514/6.1972-784
[research_waite_stanford_2019]: https://doi.org/10.2514/6.2019-3025
[research_walchli_langan_1999]: https://doi.org/10.2514/6.1999-3194
[research_waldmann_ehrle_2023]: https://doi.org/10.1007/s00348-023-03642-7
[research_walitt_king_1977]: https://doi.org/10.2514/6.1977-679
[research_walittl_liucy_1976]: https://ntrs.nasa.gov/citations/19770016110
[research_walkden_1958]: https://doi.org/10.1017/s0001925900001372
[research_walker_1973]: https://doi.org/10.2514/6.1973-1306
[research_walkerericlee_2005]: https://ntrs.nasa.gov/citations/20050240931
[research_wallace_1952]: https://doi.org/10.21236/ad0043099
[research_wallace_1953]: https://doi.org/10.21236/ad0044732
[research_wallace_monk_1966]: https://doi.org/10.2514/3.43704
[research_wallskogharveya_1954]: https://ntrs.nasa.gov/citations/20090022754
[research_wallskogharveya_1954_b]: https://ntrs.nasa.gov/citations/20090023601
[research_walterovalarezo_chetjdominik_1993]: https://ntrs.nasa.gov/citations/19940013951
[research_wang_1998]: https://doi.org/10.21236/ada338920
[research_wang_2019]: https://doi.org/10.1063/1.5087963
[research_wang_2025]: https://doi.org/10.54254/2755-2721/2026.ka27405
[research_wang_andreopoulos_2003]: https://doi.org/10.1115/fedsm2003-45079
[research_wang_andreopoulos_2009]: https://doi.org/10.1007/s00348-009-0738-y
[research_wang_chen_2011]: https://doi.org/10.2514/6.2011-658
[research_wang_damodaran_2002]: https://doi.org/10.2514/2.1714
[research_wang_gan_2024]: https://doi.org/10.2139/ssrn.4899147
[research_wang_guo_2024]: https://doi.org/10.1017/jfm.2024.55
[research_wang_herbert_1994]: https://doi.org/10.2514/6.1994-2374
[research_wang_hu_2013]: https://doi.org/10.2514/6.2013-4421
[research_wang_kang_2026]: https://doi.org/10.1007/978-981-95-3028-1_37
[research_wang_li_2022]: https://doi.org/10.1109/ahpcai57455.2022.10087863
[research_wang_liu_2024]: https://doi.org/10.1007/s40747-024-01612-y
[research_wang_luo]: https://doi.org/10.1007/bfb0041863
[research_wang_qu_2022]: https://doi.org/10.1016/j.ast.2022.107645
[research_wang_rusak_2001]: https://doi.org/10.2514/6.2001-2750
[research_wang_song_2026]: https://doi.org/10.1016/j.ast.2026.113044
[research_wang_song_2026_b]: https://doi.org/10.2139/ssrn.7560478
[research_wang_wang_2023]: https://doi.org/10.3390/aerospace10080729
[research_wang_wang_2025]: https://doi.org/10.2514/1.j064918
[research_wang_wu_2021]: https://doi.org/10.1016/j.jfluidstructs.2021.103286
[research_wang_zha_2019]: https://doi.org/10.2514/6.2019-3169
[research_wang_zha_2020]: https://doi.org/10.2514/6.2020-2666
[research_wang_zhou_2020]: https://doi.org/10.1088/1742-6596/1626/1/012183
[research_ward_1968]: https://doi.org/10.2514/3.43928
[research_ward_miley_1983]: https://doi.org/10.2514/6.1983-2689
[research_warning_lambert_2024]: https://doi.org/10.2514/1.b39044
[research_warning_mcquilling_2022]: https://doi.org/10.2514/6.2022-0603
[research_wasserman_1952]: https://doi.org/10.21236/ad0015929
[research_wat_sarohia_1981]: https://doi.org/10.2514/6.1981-2027
[research_watanabe_maekawa_2005]: https://doi.org/10.1299/jsmeicjwsf.2005.189
[research_wattsmichaele_crossjeffreyl_1988]: https://ntrs.nasa.gov/citations/19890004845
[research_wave_drag_computation_1976]: https://ntrs.nasa.gov/citations/19770033814
[research_weatherill_ehlers_1983]: https://doi.org/10.2514/6.1983-960
[research_weatherill_zartarian_1958]: https://doi.org/10.21236/ad0142154
[research_weatherillwarrenh_ehlersfedward_1989]: https://ntrs.nasa.gov/citations/19890010722
[research_weber_jones_1999]: https://doi.org/10.2514/6.1999-798
[research_weber_jones_2001]: https://doi.org/10.1016/s1270-9638(01)01099-9
[research_weed_carlson_1983]: https://doi.org/10.21236/ada129573
[research_weed_carlson_1984]: https://doi.org/10.2514/6.1984-2156
[research_weeks_1973]: https://doi.org/10.21236/ada378187
[research_wegener_1977]: https://doi.org/10.21236/ada038280
[research_wei_liu_2026]: https://doi.org/10.1063/5.0311606
[research_wei_zheng_2023]: https://doi.org/10.21203/rs.3.rs-3509474/v1
[research_wei_zheng_2024]: https://doi.org/10.3390/app14135463
[research_weiand_michelis_2017]: https://doi.org/10.2514/1.j055481
[research_weidingerhanns_1927]: https://ntrs.nasa.gov/citations/19930090796
[research_weinacht_2014]: https://doi.org/10.21236/ada607593
[research_weiner_semaan_2022]: https://doi.org/10.2514/6.2022-2591
[research_weiner_semaan_2023]: https://doi.org/10.2514/1.j062546
[research_weingarten_2003]: https://doi.org/10.2514/6.2003-5464
[research_weingarten_chalk_1982]: https://doi.org/10.2514/6.1982-1296
[research_weiss_2008]: https://doi.org/10.2514/6.2008-4033
[research_weiss_staudacher_2022]: https://doi.org/10.3390/machines10100846
[research_weisshaar_1972]: https://doi.org/10.2514/3.59048
[research_weisshaar_1979]: https://doi.org/10.21236/adb042815
[research_weisshaar_zeiler_1982]: https://doi.org/10.2514/6.1982-1325
[research_wells_1953]: https://doi.org/10.4271/530163
[research_wells_2017]: https://doi.org/10.2514/6.2017-1628
[research_wenzhong_rongwei_2008]: https://doi.org/10.1016/s1000-9361(08)60027-8
[research_wermeser_takarics_2024]: https://doi.org/10.23919/ecc64448.2024.10590847
[research_werner_henne_2024]: https://doi.org/10.2514/6.2024-2333
[research_werner_schutte_2022]: https://doi.org/10.2514/6.2022-0295
[research_wetmorejw_1947]: https://ntrs.nasa.gov/citations/19790079920
[research_wetzelbentone_pfylfranka_1954]: https://ntrs.nasa.gov/citations/19930088269
[research_weyburne_2009]: https://doi.org/10.21236/ada519312
[research_whitbeck_smith_1982]: https://doi.org/10.21236/ada134175
[research_whitcomb_1952]: https://ntrs.nasa.gov/citations/19930092271
[research_whitcomb_clark_1965]: https://ntrs.nasa.gov/citations/19720066117
[research_whitcombrichardt_1944]: https://ntrs.nasa.gov/citations/19930092722
[research_whitcombrichardt_1953]: https://ntrs.nasa.gov/citations/20050019402
[research_whitcombrichardt_sevierjohnrjr_1960]: https://ntrs.nasa.gov/citations/19980223605
[research_whitcombrt_1974]: https://ntrs.nasa.gov/citations/19740058562
[research_whitcombrt_1976]: https://ntrs.nasa.gov/citations/19760015066
[research_whitcombrt_1983]: https://ntrs.nasa.gov/citations/19840004011
[research_white_1963]: https://doi.org/10.21236/ad0296103
[research_white_1969]: https://doi.org/10.21236/ad0700246
[research_white_1977]: https://doi.org/10.21236/ada038392
[research_white_2004]: https://doi.org/10.21236/ada421045
[research_whitefield_griffith_1981]: https://doi.org/10.2514/6.1981-2474
[research_whitemauriced_1952]: https://ntrs.nasa.gov/citations/19930087169
[research_whitfield_griffith_1963]: https://doi.org/10.21236/ad0298278
[research_whitfield_jameson_1983]: https://doi.org/10.2514/6.1983-236
[research_whitfield_thompson_1989]: https://doi.org/10.21236/ada210402
[research_whitford_1991]: https://doi.org/10.2514/3.46102
[research_whitlow_seidel_1985]: https://doi.org/10.2514/3.8913
[research_whitmer_kelkar_2012]: https://doi.org/10.1109/acc.2012.6315558
[research_whittley_garland_1961]: https://doi.org/10.21236/ad0271500
[research_wick_hooker_2017]: https://doi.org/10.2514/6.2017-0099
[research_wieseman_silva_2005]: https://doi.org/10.2514/6.2005-1995
[research_wiggen_henne_2018]: https://doi.org/10.1007/s13272-018-0293-4
[research_wight_1964]: https://doi.org/10.1017/s0368393100080627
[research_wigleydavida_1988]: https://ntrs.nasa.gov/citations/19880019549
[research_wilby_1967]: https://doi.org/10.21236/ad0824482
[research_wilks_2006]: https://doi.org/10.21236/ada447214
[research_willard_kranzler_1996]: https://doi.org/10.21236/ada345019
[research_williams_1956]: https://doi.org/10.4271/560050
[research_williams_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50012-9
[research_williams_1979]: https://doi.org/10.2514/6.1979-204
[research_williams_1980]: https://doi.org/10.2514/3.50797
[research_williams_bland_1985]: https://doi.org/10.2514/3.9115
[research_williams_drake_1948]: https://ntrs.nasa.gov/citations/19650070849
[research_williams_hunt_1980]: https://doi.org/10.2514/6.1980-1809
[research_williams_kesling_1980]: https://doi.org/10.4050/vfs-f36-007
[research_williamshayes_2005]: https://doi.org/10.2514/6.2005-6995
[research_williamswalterc_1991]: https://ntrs.nasa.gov/citations/19910010759
[research_wilmerdingjv_stillwellwh_1950]: https://ntrs.nasa.gov/citations/19930086145
[research_wilmothrg_1977]: https://ntrs.nasa.gov/citations/19780005074
[research_wilson_chandra_1975]: https://doi.org/10.2514/6.1975-169
[research_wilson_chou_1985]: https://doi.org/10.2514/6.1985-315
[research_wilson_kalkhoran_1987]: https://doi.org/10.2514/6.1987-208
[research_wilsonrj_1967]: https://ntrs.nasa.gov/citations/19670005606
[research_winarto_stalker_1984]: https://doi.org/10.1017/s0001924000020625
[research_winchenbach_chelekis_1982]: https://doi.org/10.2514/6.1982-1365
[research_wind_tunnel_2022]: https://doi.org/10.1002/9781119988281.ch3
[research_wind_tunnel_flight_1978]: https://doi.org/10.2514/6.1978-989
[research_wing_loads_1996]: https://doi.org/10.2514/5.9781600862465.0163.0190
[research_wing_tunnel_1998]: https://doi.org/10.1108/aeat.1998.12770ead.003
[research_winstonmm_1969]: https://ntrs.nasa.gov/citations/19690021255
[research_wiriadidjaja_rafie_2012]: https://doi.org/10.4028/www.scientific.net/amm.225.60
[research_wisegeorgea_sterbentzwilliamh_1957]: https://ntrs.nasa.gov/citations/19930090210
[research_wislicenus_daidzic_2022]: https://doi.org/10.3390/aerospace9040192
[research_wissink_lyrintzis_1995]: https://doi.org/10.2514/6.1995-576
[research_witteveen_bijl_2009]: https://doi.org/10.4208/cicp.2009.v6.p403
[research_wjmccroskey_1988]: https://ntrs.nasa.gov/citations/19890007476
[research_woan_chakravarthy_1988]: https://doi.org/10.2514/6.1988-2547
[research_woeste_1992]: https://doi.org/10.2514/6.1992-133
[research_wolf_azevedo_2014]: https://doi.org/10.5151/meceng-wccm2012-18222
[research_wolf_henry_1988]: https://doi.org/10.2514/6.1988-2053
[research_wolf_wolf_1997]: https://doi.org/10.2514/6.1997-2223
[research_wollblad_davidson_2006]: https://doi.org/10.2514/1.20358
[research_wolles_1997]: https://doi.org/10.1007/978-3-322-90711-0_18
[research_wolowiczchesterh_rediesshermana_1957]: https://ntrs.nasa.gov/citations/19930089762
[research_wong_1974]: https://doi.org/10.2514/6.1974-1063
[research_wong_1977]: https://doi.org/10.2514/6.1977-147
[research_wood_conlon_1983]: https://doi.org/10.2514/6.1983-83
[research_wood_roberts_1989]: https://doi.org/10.2514/6.1989-149
[research_woodclotaire_1944]: https://ntrs.nasa.gov/citations/19930092753
[research_wooden_smith_2007]: https://doi.org/10.2514/6.2007-4433
[research_woodford_hansen_1985]: https://doi.org/10.21236/ada157854
[research_woodrichardm_1988]: https://ntrs.nasa.gov/citations/19880014381
[research_woodsonsh_dejarnettefr_1986]: https://ntrs.nasa.gov/citations/19860017723
[research_woodwardfa_1973]: https://ntrs.nasa.gov/citations/19730016318
[research_woolard_1980]: https://doi.org/10.2514/3.57886
[research_wootton_1967]: https://doi.org/10.1017/s0001924000055263
[research_wright_1936]: https://doi.org/10.2514/8.155
[research_wright_1945]: https://doi.org/10.21236/adb813734
[research_wright_zoby_1977]: https://doi.org/10.2514/3.60821
[research_wrightjohnb_1948]: https://ntrs.nasa.gov/citations/19930085315
[research_wrightjohnb_1948_b]: https://ntrs.nasa.gov/citations/19930085349
[research_wrightjohnb_1948_c]: https://ntrs.nasa.gov/citations/19930085814
[research_wrightjohnd_lovingdonaldl_1953]: https://ntrs.nasa.gov/citations/20050019302
[research_wu_1975]: https://doi.org/10.21236/ada014802
[research_wu_chen_1977]: https://doi.org/10.21236/ada048615
[research_wu_collins_1982]: https://doi.org/10.2514/6.1982-230
[research_wu_collins_1983]: https://doi.org/10.2514/3.8189
[research_wu_fuller_1999]: https://doi.org/10.2514/6.1999-2877
[research_wu_moulden_1976]: https://doi.org/10.2514/6.1976-326
[research_wu_yuan_2025]: https://doi.org/10.1016/j.ast.2025.110437
[research_wujm_collinsfg_1984]: https://ntrs.nasa.gov/citations/19850003710
[research_x15_conference_1958]: https://ntrs.nasa.gov/citations/19710070129
[research_x15_lessons_1993]: https://ntrs.nasa.gov/citations/19930039008
[research_x1_base_pressures_1953]: https://ntrs.nasa.gov/citations/19930087429
[research_x1_dynamic_stability_1950]: https://ntrs.nasa.gov/citations/19930086028
[research_x1_fuselage_pressures_1953]: https://ntrs.nasa.gov/citations/19930089110
[research_x1_lateral_1950]: https://ntrs.nasa.gov/citations/19930086424
[research_x1_liftdrag_1953]: https://ntrs.nasa.gov/citations/19930087731
[research_x1_tail_loads_1953]: https://ntrs.nasa.gov/citations/19930087824
[research_x1_wing_loads_1953]: https://ntrs.nasa.gov/citations/19930087661
[research_x1_wing_pressures_1953]: https://ntrs.nasa.gov/citations/19930087577
[research_x1a_damping_1956]: https://ntrs.nasa.gov/citations/19930088921
[research_x1a_interference_1956]: https://ntrs.nasa.gov/citations/19930089573
[research_x1e_damping_1956]: https://ntrs.nasa.gov/citations/19930089155
[research_x1e_flutter_1957]: https://ntrs.nasa.gov/citations/19930089755
[research_x1e_lateral_1957]: https://ntrs.nasa.gov/citations/19930089811
[research_x1e_stability_1959]: https://ntrs.nasa.gov/citations/19630003098
[research_x2_glide_1953]: https://ntrs.nasa.gov/citations/19930087801
[research_x2_mach32_1959]: https://ntrs.nasa.gov/citations/19980227870
[research_x5_stability_1953]: https://ntrs.nasa.gov/citations/19930087479
[research_x5_tail_loads_1955]: https://ntrs.nasa.gov/citations/19930088802
[research_xia_zhu_1993]: https://doi.org/10.2514/6.1993-3482
[research_xiao_tsai_2004]: https://doi.org/10.2514/6.2004-1056
[research_xiao_tsai_2004_b]: https://doi.org/10.2514/6.2004-926
[research_xiao_tsai_2006]: https://doi.org/10.2514/1.16658
[research_xie_liu_2020]: https://doi.org/10.1109/icet49382.2020.9119701
[research_xie_zhao_2019]: https://doi.org/10.1109/icusai47366.2019.9124755
[research_xin_dawei_2013]: https://doi.org/10.1109/icdma.2013.324
[research_xing_damodaran_2003]: https://doi.org/10.1007/978-3-642-59334-5_91
[research_xiong_bartels_2021]: https://doi.org/10.2514/6.2021-0337
[research_xiong_bartels_2021_b]: https://doi.org/10.2514/6.2021-2528
[research_xiong_fugate_2019]: https://doi.org/10.2514/6.2019-3026
[research_xiong_fugate_2020]: https://doi.org/10.2514/6.2020-0451
[research_xiong_liu_2013]: https://doi.org/10.2514/6.2013-3205
[research_xiong_nguyen_2021]: https://doi.org/10.2514/6.2021-0336
[research_xiong_nguyen_2022]: https://doi.org/10.2514/6.2022-4150
[research_xiong_nguyen_2022_b]: https://doi.org/10.2514/6.2022-0300
[research_xiong_nguyen_2022_c]: https://doi.org/10.2514/6.2022-4151
[research_xiong_nguyen_2023]: https://doi.org/10.2514/6.2023-1575
[research_xiong_nguyen_2023_b]: https://doi.org/10.2514/6.2023-1573
[research_xiong_nguyen_2023_c]: https://doi.org/10.2514/6.2023-4528
[research_xiong_nguyen_2023_d]: https://doi.org/10.2514/6.2023-1571
[research_xiong_nguyen_2024]: https://doi.org/10.2514/6.2024-4056
[research_xiong_nguyen_2024_b]: https://doi.org/10.2514/6.2024-2668
[research_xiong_shang_2011]: https://doi.org/10.4028/www.scientific.net/amm.148-149.121
[research_xs1_accelerated_1948]: https://ntrs.nasa.gov/citations/19930085320
[research_xs1_downwash_1948]: https://ntrs.nasa.gov/citations/19930085539
[research_xs1_freefall_1948]: https://ntrs.nasa.gov/citations/19930085511
[research_xs1_handling_1948]: https://ntrs.nasa.gov/citations/19930085327
[research_xs1_loads_1948]: https://ntrs.nasa.gov/citations/19930085882
[research_xs1_model_1947]: https://ntrs.nasa.gov/citations/19930085595
[research_xs1_model_stability_1948]: https://ntrs.nasa.gov/citations/19930085331
[research_xs1_tunnel_1976]: https://ntrs.nasa.gov/citations/19770022127
[research_xu_dowell_2026]: https://doi.org/10.2514/6.2026-2312
[research_xu_liu_2020]: https://doi.org/10.1088/1742-6596/1507/8/082010
[research_xu_qiu_2011]: https://doi.org/10.4028/www.scientific.net/amm.148-149.833
[research_xu_saleh_2019]: https://doi.org/10.2514/1.j057573
[research_xu_yin_2008]: https://doi.org/10.1016/j.jde.2007.12.011
[research_xue_feng_2024]: https://doi.org/10.2514/1.j063274
[research_xue_feng_2025]: https://doi.org/10.1016/j.ast.2025.110184
[research_xue_ren_2020]: https://doi.org/10.1016/j.cja.2020.03.030
[research_yagiz_kandil_2009]: https://doi.org/10.2514/6.2009-3763
[research_yamaguchi_yorozu_1993]: https://doi.org/10.2514/6.1993-421
[research_yamaguchi_yorozu_1994]: https://doi.org/10.2514/3.46613
[research_yamamoto_tanaka_2012]: https://doi.org/10.2514/6.2012-2895
[research_yamasaki_lele_2024]: https://doi.org/10.2514/6.2024-4524
[research_yan_dai_2026]: https://doi.org/10.1063/5.0326645
[research_yan_ragab_2016]: https://doi.org/10.2514/6.2016-1225
[research_yan_ragab_2017]: https://doi.org/10.1007/s11071-017-3894-2
[research_yang_1972]: https://doi.org/10.2514/3.6657
[research_yang_guruswamy_1980]: https://doi.org/10.21236/ada084172
[research_yang_guruswamy_1980_b]: https://doi.org/10.2514/3.44652
[research_yang_guruswamy_1981]: https://doi.org/10.2514/6.1981-603
[research_yang_he_2016]: https://doi.org/10.1016/j.jfluidstructs.2016.07.013
[research_yang_huang_2017]: https://doi.org/10.2514/1.g002690
[research_yang_huang_2019]: https://doi.org/10.1016/j.jsv.2019.01.006
[research_yang_li_2024]: https://doi.org/10.2514/6.2024-1227
[research_yang_li_2024_b]: https://doi.org/10.2514/1.j063634
[research_yang_li_2026]: https://doi.org/10.2139/ssrn.6248058
[research_yang_striz_1980]: https://doi.org/10.2514/6.1980-736
[research_yang_striz_1981]: https://doi.org/10.2514/3.57576
[research_yang_wan_1978]: https://doi.org/10.21236/ada061942
[research_yang_wu_2025]: https://doi.org/10.1063/5.0280452
[research_yang_yan_2015]: https://doi.org/10.2514/6.2015-1240
[research_yang_yao_2016]: https://doi.org/10.2514/6.2016-0045
[research_yangweili_greberisaac_1993]: https://ntrs.nasa.gov/citations/19930064296
[research_yaros_1978]: https://doi.org/10.21236/ada050401
[research_yates_1963]: https://doi.org/10.2514/6.1963-205
[research_yates_wynne_1982]: https://doi.org/10.2514/3.44803
[research_yates_wynne_1983]: https://doi.org/10.2514/3.44952
[research_yatesjr_wynne_1982]: https://doi.org/10.2514/6.1982-647
[research_yechout_schweikhard_1984]: https://doi.org/10.2514/6.1984-563
[research_yee_lee_1997]: https://doi.org/10.2514/6.1997-1628
[research_yee_lee_1998]: https://doi.org/10.2514/2.438
[research_yefremov_kraiko_2005]: https://doi.org/10.1016/j.jappmathmech.2005.09.001
[research_yeom_chang_2012]: https://doi.org/10.1007/978-3-642-25685-1_11
[research_yetter_evelyn_1982]: https://doi.org/10.2514/6.1982-1045
[research_yigit_millidere_2021]: https://doi.org/10.2514/6.2021-2999
[research_yinshengluo_shaobangxing_2011]: https://doi.org/10.1109/aimsec.2011.6009954
[research_yip_vijgen_1995]: https://doi.org/10.2514/3.46752
[research_yongping_zengjun_2026]: https://doi.org/10.2139/ssrn.7319827
[research_yoo]: https://doi.org/10.70675/a3b30812zfc99z4b50za1aczb2565be062a1
[research_yoon_chung_1996]: https://doi.org/10.2514/6.1996-2005
[research_yoshida_bragg_2021]: https://doi.org/10.2514/6.2021-2680
[research_yoshida_tokuyama_1992]: https://doi.org/10.2514/6.1992-4218
[research_yoshikawa_1982]: https://doi.org/10.2514/6.1982-1362
[research_yoshioka_kikuchi_2009]: https://doi.org/10.1088/0169-5983/41/2/021408
[research_yoshioka_kohama]: https://doi.org/10.1109/iciasf.2005.1569929
[research_you_2026]: https://doi.org/10.2139/ssrn.6802803
[research_you_bromby_2013]: https://doi.org/10.21236/ada608653
[research_young]: https://doi.org/10.1109/naecon.1993.290841
[research_young_oran_1988]: https://doi.org/10.2514/6.1988-701
[research_youngjr_hergert_1992]: https://doi.org/10.2514/6.1992-4032
[research_youngjr_popernackjr_1990]: https://doi.org/10.2514/6.1990-1416
[research_youngls_1961]: https://ntrs.nasa.gov/citations/19660024038
[research_yu_1979]: https://doi.org/10.2514/6.1979-75
[research_yu_1980]: https://doi.org/10.2514/3.50744
[research_yu_1981]: https://doi.org/10.2514/6.1981-1258
[research_yu_bose_2026]: https://doi.org/10.2514/6.2026-1052
[research_yu_campbell_1992]: https://doi.org/10.2514/6.1992-2651
[research_yu_chen_1983]: https://doi.org/10.2514/6.1983-1928
[research_yu_lv_2014]: https://doi.org/10.4028/www.scientific.net/amr.1006-1007.26
[research_yu_zhou_2025]: https://doi.org/10.1007/978-981-95-3007-6_9
[research_yuan_wan_2019]: https://doi.org/10.1360/sspma-2019-0162
[research_yue_2026]: https://doi.org/10.2514/6.2026-4344
[research_yuhara_kubota_2018]: https://doi.org/10.2514/6.2018-0046
[research_yurkovich_1996]: https://doi.org/10.2514/6.1996-1447
[research_yuxing_gangwang_2015]: https://doi.org/10.1109/ibcast.2015.7058545
[research_zahir_gao_2013]: https://doi.org/10.19026/rjaset.5.4266
[research_zahn_breitsamter_2020]: https://doi.org/10.3390/aerospace7110162
[research_zahn_breitsamter_2022]: https://doi.org/10.1007/s13272-022-00619-w
[research_zahn_zieher_2025]: https://doi.org/10.3390/aerospace12050415
[research_zalovcikjohna_1944]: https://ntrs.nasa.gov/citations/19930092748
[research_zalovcikjohna_1945]: https://ntrs.nasa.gov/citations/19930093001
[research_zamuraev_kalinina_2018]: https://doi.org/10.1063/1.5065295
[research_zanin_1985]: https://doi.org/10.1007/978-3-642-82462-3_67
[research_zartarian_1956]: https://doi.org/10.21236/ad0110592
[research_zartarian_hsu_1955]: https://doi.org/10.21236/ad0110591
[research_zater_bahi_2024]: https://doi.org/10.1134/s086986432403020x
[research_zauner_detullio_2018]: https://doi.org/10.2514/6.2018-2911
[research_zauner_detullio_2019]: https://doi.org/10.2514/1.j057335
[research_zauner_moise_2023]: https://doi.org/10.1007/s10494-023-00415-4
[research_zauner_sandham_2020]: https://doi.org/10.1103/physrevfluids.5.083903
[research_zebiri_piquet_2019]: https://doi.org/10.3850/978-981-11-2730-4_0082-cd
[research_zeigler_drew_1985]: https://doi.org/10.2514/3.9015
[research_zeleke_asfaw_2023]: https://doi.org/10.3103/s1068799823040190
[research_zeng_chen_2012]: https://doi.org/10.2514/6.2012-4856
[research_zhang_2013]: https://doi.org/10.2514/6.2013-2952
[research_zhang_dai_2019]: https://doi.org/10.1016/j.ast.2019.105364
[research_zhang_deng_2026]: https://doi.org/10.3390/aerospace13010098
[research_zhang_ding_2016]: https://doi.org/10.1080/19942060.2016.1152200
[research_zhang_dou_2026]: https://doi.org/10.2139/ssrn.7265786
[research_zhang_du_2025]: https://doi.org/10.21203/rs.3.rs-8086442/v1
[research_zhang_edwards_1990]: https://doi.org/10.2514/6.1990-3087
[research_zhang_gao_2017]: https://doi.org/10.2514/6.2017-3967
[research_zhang_guo_2021]: https://doi.org/10.1155/2021/5553304
[research_zhang_hirahara_2022]: https://doi.org/10.1088/1742-6596/2217/1/012006
[research_zhang_kou_2026]: https://doi.org/10.2139/ssrn.7371644
[research_zhang_kou_2026_b]: https://doi.org/10.21203/rs.3.rs-9886298/v1
[research_zhang_li_2020]: https://doi.org/10.1016/j.ast.2020.106101
[research_zhang_ma_2020]: https://doi.org/10.1088/1742-6596/1631/1/012152
[research_zhang_qu_2015]: https://doi.org/10.2514/6.2015-0068
[research_zhang_shan_2017]: https://doi.org/10.1360/n092016-00329
[research_zhang_su_2023]: https://doi.org/10.1007/978-981-19-7652-0_67
[research_zhang_tian_2024]: https://doi.org/10.3390/app142210234
[research_zhang_xu_2008]: https://doi.org/10.1109/asc-icsc.2008.4675399
[research_zhang_yang_1988]: https://doi.org/10.2514/3.45613
[research_zhang_yang_2021]: https://doi.org/10.3390/aerospace8080203
[research_zhang_ye_2010]: https://doi.org/10.1016/j.actaastro.2009.09.016
[research_zhang_ye_2015]: https://doi.org/10.2514/1.c032552
[research_zhang_yu_1990]: https://doi.org/10.2514/6.1990-3099
[research_zhang_yu_2013]: https://doi.org/10.1155/2013/714168
[research_zhang_zhang_2013]: https://doi.org/10.4028/www.scientific.net/amm.397-400.218
[research_zhang_zhang_2020]: https://doi.org/10.1016/j.actaastro.2019.11.012
[research_zhang_zhao_2024]: https://doi.org/10.1063/5.0214653
[research_zhang_zou_2021]: https://doi.org/10.1007/s00193-021-01061-3
[research_zhang_zuo_2025]: https://doi.org/10.2514/1.j064891
[research_zhao_1988]: https://doi.org/10.2514/6.1988-3735
[research_zhao_2016]: https://doi.org/10.2514/6.2016-0075
[research_zhao_2023]: https://doi.org/10.1088/1742-6596/2442/1/012038
[research_zhao_dai_2020]: https://doi.org/10.1016/j.cja.2019.12.022
[research_zhao_gao_2017]: https://doi.org/10.2514/6.2017-1414
[research_zhao_he_2020]: https://doi.org/10.1016/j.ast.2019.105635
[research_zhao_hu_2009]: https://doi.org/10.2514/1.39464
[research_zhao_jia_2023]: https://doi.org/10.3390/pr11061683
[research_zhao_li_2024]: https://doi.org/10.1016/j.taml.2024.100540
[research_zhao_li_2025]: https://doi.org/10.2139/ssrn.5213523
[research_zhao_liu_2024]: https://doi.org/10.1016/j.actaastro.2024.07.040
[research_zhao_ren_2013]: https://doi.org/10.2514/6.2013-537
[research_zhao_wang_2025]: https://doi.org/10.2139/ssrn.5637616
[research_zhao_wu_2022]: https://doi.org/10.3389/fbioe.2022.927064
[research_zhao_yang_2026]: https://doi.org/10.1016/j.ast.2025.110742
[research_zhao_zhu_2012]: https://doi.org/10.1016/j.compfluid.2012.01.002
[research_zheng_feng_2012]: https://doi.org/10.4028/www.scientific.net/amr.566.676
[research_zheng_liu_2011]: https://doi.org/10.4028/www.scientific.net/amm.110-116.1506
[research_zhenghong_1992]: https://doi.org/10.1007/bf02481800
[research_zhigulev_zhilin_1959]: https://doi.org/10.1016/0021-8928(59)90004-8
[research_zhong_xia_2025]: https://doi.org/10.1007/978-981-95-2998-8_44
[research_zhou_1994]: https://doi.org/10.2514/6.1994-2345
[research_zhou_cao_2025]: https://doi.org/10.1016/j.measurement.2024.115716
[research_zhou_chen_2017]: https://doi.org/10.1016/j.taml.2017.11.006
[research_zhou_feng_2018]: https://doi.org/10.2514/1.c034432
[research_zhou_hou_2017]: https://doi.org/10.1016/j.compfluid.2017.07.014
[research_zhou_ji_2026]: https://doi.org/10.1016/j.ast.2026.113973
[research_zhou_li_2016]: https://doi.org/10.1016/j.jfluidstructs.2016.07.002
[research_zhu_li_2019]: https://doi.org/10.2514/1.j058011
[research_zhu_qin_2021]: https://doi.org/10.2514/1.j059914
[research_zhu_wang_2020]: https://doi.org/10.1142/s0217979220400834
[research_zhu_xia_1992]: https://doi.org/10.1007/bf01170804
[research_zhu_xia_1994]: https://doi.org/10.1007/978-3-7091-9310-5_31
[research_zhu_yang_2025]: https://doi.org/10.2139/ssrn.5615374
[research_zhu_yang_2026]: https://doi.org/10.2139/ssrn.6994998
[research_zigangareyeva_kiselev_1997]: https://doi.org/10.1016/s0021-8928(97)00012-9
[research_zimmermann_mayer_2018]: https://doi.org/10.2514/1.j056193
[research_zimper_rein_2014]: https://doi.org/10.2514/6.2014-2005
[research_zingg_diosady_2006]: https://doi.org/10.2514/6.2006-3656
[research_zink_mavris_2001]: https://doi.org/10.2514/2.2884
[research_zinovyev_lebiga_2012]: https://doi.org/10.1051/eucass/201203003
[research_ziqiang_xuesong_1992]: https://doi.org/10.2514/3.46142
[research_zolovcikjohna_1950]: https://ntrs.nasa.gov/citations/19930082701
[research_zong_wu_2023]: https://doi.org/10.2514/1.j062099
[research_zoppini_ragni_2022]: https://doi.org/10.2139/ssrn.4036119
[research_zores_1995]: https://doi.org/10.2514/6.1995-1818
[research_zuccolo_christie_2020]: https://doi.org/10.2514/6.2020-1997
[research_zuosheng_1986]: https://doi.org/10.1016/b978-0-08-034357-0.50024-9
[research_zwaan_1984]: https://doi.org/10.2514/6.1984-871
