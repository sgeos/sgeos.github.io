---
layout: post
mathjax: true
comments: true
title: "X-Planes: Bell X-2"
date: 2025-10-08 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 3
---

<!-- A299 -->
<script>console.log("A299");</script>

The [Bell X-2][ref_bell_x2] was built to fly where the air itself becomes the structural problem. Above roughly Mach 2.5 the temperature recovered at the surface of an airframe exceeds what aluminium can carry, and the aircraft was commissioned to find out what happens past that line and what a structure must be made of to survive it. This article is the third in the [X-Planes series][related_post_a297_xplanes_framing] and the second per-aircraft treatment, following the [Bell X-1][related_post_a298_bell_x1]. The National Advisory Committee for Aeronautics, abbreviated NACA throughout and reconstituted in 1958 as the National Aeronautics and Space Administration, abbreviated NASA, supplied the research programme. The United States Air Force supplied the requirement. [Bell Aircraft][ref_bell_aircraft] supplied the airframe and [Curtiss-Wright][ref_curtiss_wright] the engine. Both aircraft were destroyed and two of the three men who flew the surviving one are not the reason the programme is remembered, though one of them should be. The X-2 answered its thermal question and then delivered a second answer nobody had asked for, at the cost of the pilot who found it.

## The Research Question

The keystone is aerodynamic heating, and specifically the temperature a structure reaches in sustained flight between Mach 2 and Mach 3.

The [X-1][related_post_a298_bell_x1] had no thermal problem. At its Mach 1.45 record the [stagnation temperature][ref_stagnation_temperature] was 308 kelvin, which is warm afternoon air and imposes no material constraint whatever. The reason is that stagnation temperature rises with the square of Mach number,

$$T_0 = T_\infty \left( 1 + \frac{\gamma - 1}{2} M_\infty^2 \right)$$

with $T_\infty$ the free-stream static temperature in kelvin, $\gamma$ the ratio of specific heats, and $M_\infty$ the free-stream [Mach number][ref_mach_number]. A quadratic that is negligible at Mach 1.5 is not negligible at Mach 3. Evaluating in the isothermal layer above 11 kilometres, where $T_\infty = 216.65$ kelvin, gives 659 kelvin at Mach 3.196 against 308 kelvin at Mach 1.45. The rise above ambient nearly quintuples while the Mach number merely doubles.

The same isentropic family fixes the pressure and density the structure sees,

$$\frac{p_0}{p} = \left( 1 + \frac{\gamma - 1}{2} M^2 \right)^{\frac{\gamma}{\gamma - 1}}, \qquad \frac{\rho_0}{\rho} = \left( 1 + \frac{\gamma - 1}{2} M^2 \right)^{\frac{1}{\gamma - 1}}$$

with the whole set tabulated in [NACA Report 1135][research_naca_1135], and the local geometry of every disturbance follows the Mach angle

$$\mu_M = \arcsin \frac{1}{M}$$

which at Mach 3.196 is 18.2 degrees, so shocks lie close to the surface and the flow field is compact. Where a [shock][ref_shock_wave] does stand normal to the flow the Rankine-Hugoniot relations give

$$\frac{p_2}{p_1} = \frac{2 \gamma M_1^2 - (\gamma - 1)}{\gamma + 1}, \qquad \frac{T_2}{T_1} = \frac{\left[ 2 \gamma M_1^2 - (\gamma - 1) \right] \left[ (\gamma - 1) M_1^2 + 2 \right]}{(\gamma + 1)^2 M_1^2}$$

and at Mach 3.196 the static pressure rises by a factor of 11.8 and the static temperature by 2.92 across a single normal shock. What a surface actually reaches is lower, because a [boundary layer][ref_boundary_layer] does not bring the flow entirely to rest and does not recover the whole temperature rise. The recovery temperature is

$$T_r = T_\infty \left( 1 + r \frac{\gamma - 1}{2} M_\infty^2 \right), \qquad r \approx Pr^{1/2} \ \text{laminar}, \qquad r \approx Pr^{1/3} \ \text{turbulent}$$

with $r$ the recovery factor and $Pr$ the [Prandtl number][ref_prandtl_number]. At $r = 0.89$, appropriate for turbulent flow in air, the recovery temperature at Mach 3.196 is 611 kelvin.

Before going further it is worth confirming that the perfect-gas assumption behind every relation above survives at this condition, because it does not at the temperatures the [X-15][ref_na_x15] would later reach. Vibrational modes of diatomic nitrogen and oxygen begin to activate near 800 kelvin, at which point the ratio of specific heats departs from 1.4 through

$$\gamma(T) = 1 + \frac{R}{c_v(T)}, \qquad c_v(T) = \frac{5}{2} R + R \left( \frac{\theta_v / T}{e^{\theta_v / T} - 1} \right)^2 e^{\theta_v / T}$$

with $\theta_v$ the characteristic vibrational temperature, near 2270 kelvin for oxygen and 3390 for nitrogen. Dissociation follows well above that. At a stagnation temperature of 659 kelvin the vibrational contribution is a few percent and dissociation is absent entirely, so air behaves as a calorically perfect gas throughout the X-2 envelope and $\gamma = 1.4$ holds. Where that assumption fails, which is everywhere above roughly Mach 5, the consequences reach into the boundary layer as in [NASA 1986][research_real_gas_boundary_layer_1986], into its stability as in [Malik and Anderson 1991][research_real_gas_stability_1991], into trim as in [Park and Yoon 1989][research_real_gas_trim_1989], and into whether a ground facility can reproduce the flow at all, which is the subject of [Gully et al 1987][research_real_gas_facility_1987]. That is a real simplification the aircraft enjoyed and the X-15 did not.

The recovery temperature of 611 kelvin is the whole programme. Aluminium alloys of the period lose useful strength above roughly 400 kelvin and are unusable above 500. At 611 kelvin steady state an aluminium airframe does not fail dramatically. It creeps, which is worse, because [creep][ref_creep_deformation] is time-dependent and a structure that survives a two-minute exposure may not survive a ten-minute one. The design question was therefore not whether the aircraft could reach Mach 3 but what it should be made of, and how long it could stay there.

Three sub-questions follow, and the article treats each in turn. What is the actual heat flux into the structure, as opposed to the temperature of the air. How does the structure respond in time, since a short exposure and a steady state are different problems. And what does a material chosen for temperature and not for strength cost in mass.

A fourth question was not asked and turned out to matter more. At Mach 3 an airframe with most of its mass in a long fuselage and very little in short swept wings has inertia properties that couple its rotational axes together, and the aerodynamic restoring moments that would ordinarily suppress that coupling weaken with Mach number. That is treated in its place below, and it is what killed the aircraft.

## Programme Origin

The X-2 was authorized in 1945, the same year as the X-1, under a United States Army Air Forces contract to Bell with a NACA research component. It did not fly under power until 1955. That ten-year gap is the most informative fact about the programme and is worth explaining, not noting.

Two things were being invented at once. The first was a structure in a material nobody built airframes from. The second was a throttleable liquid rocket engine, which is a substantially harder problem than the fixed-thrust chambers of the [X-1][related_post_a298_bell_x1], and the Curtiss-Wright XLR25 took years to become flightworthy. A programme that must invent two things sequentially takes longer than the sum of the parts, because each waits on the other for integration.

The delay had a consequence the programme did not intend. By the time the X-2 flew, the [X-15][ref_na_x15] was already being designed to a far more ambitious specification, and the research airplane committee documented in [Beeler 1961][research_x15_conference_1958] was looking past Mach 3 toward Mach 6 and beyond. The X-2 therefore delivered its data into a community that had partly moved on, which is a recurring hazard for long programmes and one this series will meet again.

The configuration decisions follow from the keystone. The wing was swept 40 degrees and of low [aspect ratio][ref_aspect_ratio], on the reasoning of [Jones 1947][research_jones_1947] that sweep reduces the effective Mach number normal to the leading edge. The structure was stainless steel and K-Monel, a nickel-copper alloy related to [Monel][ref_monel], chosen for temperature capability and not for specific strength. The aircraft was air-launched from a [Boeing B-50 Superfortress][ref_b50], a larger carrier than the X-1 needed, because the X-2 was heavier and needed more altitude at release.

One further decision deserves separate mention because it bears on how the programme ended. The X-2 had no [ejection seat][ref_ejection_seat]. It had a jettisonable nose capsule, the stability of which the NACA had investigated as early as [Goddwin 1949][research_nose_capsule_1949]. The pilot was expected to separate the entire forward fuselage, stabilize, and then leave it under a personal parachute at lower altitude. The [X-15][ref_na_x15] programme reached a different conclusion and used an ejection seat, as [Hegenwald 1958][research_x15_escape_1958] records.

## Sizing From First Principles

The keystone relationship is the thermal balance at the surface, and working it through selects the material.

The quantity of interest is the [heat flux][ref_heat_flux] crossing the surface, in watts per square metre. Heat arrives by convection from the boundary layer, driven by the difference between the recovery temperature and the wall temperature,

$$\dot{q}_{\text{conv}} = h_c \left( T_r - T_w \right)$$

with $h_c$ the convective coefficient in watts per square metre kelvin and $T_w$ the wall temperature. The coefficient is conventionally non-dimensionalized as a Stanton number and tied to skin friction by the Reynolds analogy,

$$St = \frac{h_c}{\rho_\infty V_\infty c_p}, \qquad St \approx \frac{C_f}{2} Pr^{-2/3}$$

where the [Prandtl number][ref_prandtl_number] and the Nusselt number, the two groups this correlation is built from, are

$$Pr = \frac{\mu c_p}{k_a}, \qquad Nu = \frac{h_c L}{k_a}$$

with $k_a$ the thermal conductivity of the air, and conduction within the solid follows Fourier's law,

$$\mathbf{q} = -k_w \nabla T$$

in the form given by [Eckert 1956][research_eckert_1956], with the compressible boundary-layer profiles from [Chapman and Rubesin 1949][research_chapman_rubesin_1949]. For a turbulent boundary layer on a flat plate the skin friction follows

$$C_f = \frac{0.0592}{Re_x^{1/5}}, \qquad Re_x = \frac{\rho_\infty V_\infty x}{\mu}$$

with the viscosity from the relation of [Sutherland 1893][research_sutherland_1893],

$$\mu = \mu_{\text{ref}} \left( \frac{T}{T_{\text{ref}}} \right)^{3/2} \frac{T_{\text{ref}} + S}{T + S}$$

At the flight condition this gives a unit [Reynolds number][ref_reynolds_number] of

$$\frac{Re}{L} = \frac{\rho_\infty V_\infty}{\mu} = \frac{0.0882 \times 943}{1.42 \times 10^{-5}} = 5.86 \times 10^{6} \ \text{per metre}$$

The single largest uncertainty in the whole thermal estimate is whether that boundary layer is laminar or turbulent, because the heating ratio between the two states is

$$\frac{St_{\text{turb}}}{St_{\text{lam}}} = \frac{0.0296 \, Re_x^{-1/5}}{0.332 \, Re_x^{-1/2}} = 0.089 \, Re_x^{3/10}$$

which at $Re_x = 10^{7}$ is a factor of about eleven. A structure sized for laminar heating and flown turbulent is not conservatively designed, it is wrong, and that is why transition location, not peak temperature is the quantity the community chased for the next fifty years. At a stagnation point the flux is given to good accuracy by the correlation used throughout this series,

$$\dot{q}_s = k_{SG} \sqrt{\frac{\rho_\infty}{R_n}} \, V_\infty^3, \qquad k_{SG} = 1.7415 \times 10^{-4}$$

with $R_n$ the effective nose radius in metres, resting on the theory of [Fay and Riddell 1958][research_fay_riddell_1958] and the blunt-body analysis of [Lees 1956][research_lees_1956]. Take the condition of the final flight. At 19,992 metres the standard atmosphere gives a static pressure of 5481 pascals and a density of 0.0882 kilograms per cubic metre, the [speed of sound][ref_speed_of_sound] is 295.0 metres per second, and at Mach 3.196 the true airspeed is 943 metres per second. With an effective nose radius of 0.05 metres,

$$\dot{q}_s = 1.7415 \times 10^{-4} \times \sqrt{\frac{0.0882}{0.05}} \times 943^3 = 1.94 \times 10^{5} \ \text{watts per square metre}$$

or 194 kilowatts per square metre. If the structure could only radiate that away, the equilibrium wall temperature would follow from the [Stefan-Boltzmann law][ref_stefan_boltzmann],

$$T_{\text{eq}} = \left( \frac{\dot{q}_s}{\varepsilon \sigma_{SB}} \right)^{1/4}$$

with $\varepsilon$ the emissivity and $\sigma_{SB} = 5.670 \times 10^{-8}$ watts per square metre per kelvin to the fourth. At $\varepsilon = 0.8$ this gives 1438 kelvin, which no airframe alloy of 1955 could hold.

The X-2 survived because it never reached equilibrium. This is the central design insight of the aircraft and it is a statement about time and not temperature. Whether a thin skin can be treated as isothermal through its thickness is decided by the [Biot number][ref_biot_number],

$$Bi = \frac{h_c t_w}{k_w}$$

with $t_w$ the wall thickness and $k_w$ the wall [thermal conductivity][ref_thermal_conductivity]. For a metallic skin of a millimetre or two this is small, so a lumped transient balance applies,

$$\rho_w c_w t_w \frac{dT_w}{dt} = \dot{q}_{\text{conv}} - \varepsilon \sigma_{SB} T_w^4$$

with $\rho_w$ the density and $c_w$ the specific heat. The thermal mass per unit area is

$$C_A = \rho_w c_w t_w$$

and for stainless steel at 8000 kilograms per cubic metre, a specific heat of 500 joules per kilogram kelvin, and a 1.6 millimetre skin this is 6400 joules per square metre kelvin. Neglecting reradiation while the skin is still cold, the initial heating rate is

$$\left. \frac{dT_w}{dt} \right|_{t=0} = \frac{\dot{q}_s}{C_A} = \frac{1.94 \times 10^{5}}{6400} = 30 \ \text{kelvin per second}$$

so the skin climbs from an initial 250 kelvin to 800 kelvin in about eighteen seconds. That is the design margin of the entire aircraft. The X-2 was a heat sink flown fast for a short time, not a thermally equilibrated vehicle, and the exposure duration is a hard limit, not a soft one. The relevant diffusion timescale is set by the [Fourier number][ref_fourier_number],

$$Fo = \frac{\alpha_{\text{th}} t}{t_w^2}, \qquad \alpha_{\text{th}} = \frac{k_w}{\rho_w c_w}$$

and for a thin metallic skin $Fo$ exceeds unity in well under a second, confirming that the skin equilibrates through its thickness far faster than it heats, which is what licenses the lumped treatment. Two refinements matter for a real structure. Radiation leaves the surface toward a cold sky rather than into a blackbody enclosure, so the net radiative term carries a view factor $F$ and an effective sink temperature,

$$\dot{q}_{\text{rad}} = \varepsilon \sigma_{SB} F \left( T_w^4 - T_{\text{sink}}^4 \right)$$

and because $T_{\text{sink}}$ is small compared with $T_w$ the correction is modest, which is why the simpler form is used above. Conduction into the substructure is not modest. Treating the skin and the underlying structure as two lumped masses connected by a conductance $h_j$ per unit area gives

$$C_{A,s} \frac{dT_s}{dt} = \dot{q}_{\text{conv}} - \varepsilon \sigma_{SB} T_s^4 - h_j \left( T_s - T_b \right)$$

$$C_{A,b} \frac{dT_b}{dt} = h_j \left( T_s - T_b \right)$$

whose difference $T_s - T_b$ is exactly the $\Delta T$ that drives the thermal stress below. The system has a characteristic equalization time

$$\tau_{\text{eq}} = \frac{1}{h_j} \left( \frac{C_{A,s} C_{A,b}}{C_{A,s} + C_{A,b}} \right)$$

and a design that makes $\tau_{\text{eq}}$ short reduces thermal stress at the cost of dumping heat into the primary structure, while one that makes it long protects the structure and maximizes the gradient. Neither is free, and the choice is the central thermal-structural tradeoff of every aircraft in this part of the series.

A material figure of merit captures it. The thermal shock resistance parameter

$$R_{TS} = \frac{\sigma_{\text{allow}} \left( 1 - \nu \right) k_w}{E \alpha_T}$$

rewards strength and conductivity and penalizes stiffness and expansion, and it ranks materials very differently from specific strength. Stainless steel scores poorly on specific strength and adequately on $R_{TS}$, which is a second and independent reason it was the right choice. The general problem is the [heat equation][ref_heat_equation] treated by [Carslaw and Jaeger 1959][book_carslaw_jaeger_1959], and the flight-relevant computation by [Quinn and Gong 2000][research_transient_surface_temp_2000].

The quantity that decides survival over a whole flight rather than at an instant is the integrated load,

$$Q = \int_0^{t_f} \dot{q}_{\text{conv}} \, dt$$

and peak rate and total load are traded against one another rather than minimized together. A steep fast profile has a high peak and a small integral. A shallow sustained one has the reverse. The X-2 flew the first kind by necessity and the [SR-71][ref_sr71] later flew the second by design, which is why one is a heat sink and the other is thermally equilibrated. The diffusion depth reached in a time $t$ is

$$\delta_{\text{th}} \sim \sqrt{\alpha_{\text{th}} t}$$

and for stainless steel with a thermal diffusivity near $4 \times 10^{-6}$ square metres per second this is 8.9 millimetres in twenty seconds, comfortably more than the skin thickness and comfortably less than the structural depth, which is precisely the regime in which skin and substructure reach different temperatures and the thermal stress problem below becomes acute. Hold that eighteen-second figure. On the final flight the engine burned about twelve and a half seconds longer than planned.

## Dependent Systems

### Materials and the Thermal Structure

Material selection is the keystone made concrete, and it is a selection against temperature rather than against strength.

The figure of merit is not the room-temperature allowable but the allowable at the skin temperature the trajectory produces,

$$\left. \frac{\sigma_{\text{allow}}(T)}{\rho_m} \right|_{T = T_w}$$

The evidence for that selection is a body of sheet-property testing that ran alongside the airframe programmes and is rarely cited with them. Compressive strength and creep lifetime of the standard aluminium of the period were measured directly in [Mathauser and Deveikis 1955][research_creep_2024t3_1955] and [Mathauser and Deveikis 1957][research_creep_2024t3_1957], and the stainless steels that replaced it were characterized under rapid heating, which is the relevant condition for a heat-sink structure rather than a soaked one, in [Manning and Price 1961][research_stainless_rapid_heat_1961] and [NASA 1961][research_rapid_compression_1961]. Testing practice itself had to be established, since a short-time elevated-temperature test is not a room-temperature test performed hot, and [Manning and Heimerl 1960][research_elevated_tensile_practice_1960] addresses that. Earlier aluminium property work appears in [NACA 1943][research_alclad_aging_1943]. Aluminium alloys hold useful strength to roughly 400 kelvin. [Titanium alloys][ref_titanium_alloys] reach roughly 800. [Stainless steel][ref_stainless_steel] and the nickel-copper K-Monel used on the X-2 reach roughly 900 to 1000 in short exposure. Against a recovery temperature of 611 kelvin the aluminium option is excluded outright and the steel option has margin, at a cost in density of nearly a factor of three.

That density penalty propagates through the whole airframe. For a given bending moment the required spar cap area is

$$A_{\text{cap}} = \frac{M_{\text{root}}}{\sigma_{\text{allow}} h_s}$$

and the cap mass per unit length is $\rho_m A_{\text{cap}}$, so the structural mass scales as

$$m_s \propto \frac{\rho_m}{\sigma_{\text{allow}}(T_w)}$$

which is the inverse of the temperature-derated specific strength.

Two time-dependent mechanisms sit underneath that static allowable and neither appears in a stress calculation. The first is [creep][ref_creep_deformation]. A metal held under load at elevated temperature deforms progressively, and the standard correlation collapses time and temperature into the Larson-Miller parameter

$$P_{LM} = T \left( C + \log_{10} t_r \right)$$

with $T$ in kelvin, $t_r$ the rupture time in hours, and $C$ near 20 for most steels. Because $P_{LM}$ is a single-valued function of stress for a given alloy, a fixed rupture parameter trades temperature against the logarithm of time. Inverting the definition gives the rupture time at any temperature,

$$\log_{10} t_r = \frac{P_{LM}}{T} - C$$

so that at constant stress the ratio between two temperatures is

$$\log_{10} \frac{t_2}{t_1} = P_{LM} \left( \frac{1}{T_2} - \frac{1}{T_1} \right)$$

Take a one-hour rupture life at 700 kelvin, which fixes $P_{LM} = 700 \times (20 + 0) = 1.4 \times 10^{4}$. Raising the skin to 800 kelvin gives

$$\log_{10} \frac{t_2}{t_1} = 1.4 \times 10^{4} \left( \frac{1}{800} - \frac{1}{700} \right) = -2.5$$

so a hundred kelvin near this range costs two and a half orders of magnitude in life. That is the quantitative reason a short exposure is survivable and a sustained one is a different aircraft.

The second is oxidation. Protective-scale growth on a nickel-bearing alloy follows a parabolic rate law,

$$x_{\text{ox}}^2 = k_p t, \qquad k_p = k_0 \exp \left( -\frac{E_a}{R_u T} \right)$$

with $x_{\text{ox}}$ the scale thickness, $E_a$ an activation energy, and $R_u$ the universal gas constant. The Arrhenius factor means oxidation rate, like creep, is exponentially sensitive to temperature while the accumulated damage grows only as the square root of time. Both mechanisms therefore reward exactly the flight profile the X-2 flew, which is fast and brief. Steel at high temperature is competitive with aluminium at low temperature on this measure only because the aluminium allowable collapses, and that is the entire argument for the material choice.

The second thermal effect, after the loss of strength with temperature, is more dangerous than the first. A structure heated non-uniformly and prevented from expanding develops [thermal stress][ref_thermal_stress] directly,

$$\sigma_{\text{th}} = \frac{E \alpha_T \Delta T}{1 - \nu}$$

with $E$ the elastic modulus, $\alpha_T$ the coefficient of [thermal expansion][ref_thermal_expansion], $\nu$ the Poisson ratio, and $\Delta T$ the temperature difference across the constrained region. For stainless steel at 193 gigapascals, a coefficient of $17.3 \times 10^{-6}$ per kelvin, and a Poisson ratio of 0.3, a modest hundred-kelvin difference between a hot skin and a cooler substructure gives

$$\sigma_{\text{th}} = \frac{193 \times 10^{9} \times 17.3 \times 10^{-6} \times 100}{0.7} = 477 \ \text{megapascals}$$

which already exceeds the yield strength of annealed stainless steel. At the three-hundred-kelvin difference a real transient produces, the figure is 1431 megapascals, which is structurally meaningless because the material would have yielded long before. The conclusion is not that the structure fails. It is that the structure must not be fully constrained. High-speed airframes use floating skin panels, slip joints, and corrugated webs precisely so that $\Delta T$ never acts across a rigid load path, and the X-2 is an early instance of that discipline. The joint problem is treated explicitly in [Matza 1990][research_dissimilar_joints_1990], and the prediction against measurement, which is the only way to know whether the discipline worked, in [Jenkins 1979][research_thermal_stress_correlation_1979] and later on a dedicated test article in [Morris 1990][research_dryden_hwts_thermal_1990] and [Plank 1975][research_hypersonic_wing_structure_1975]. Structural concepts for sustained rather than transient exposure are surveyed in [Taylor and Jackson 1980][research_thermostructural_hypersonic_1980] and [Jackson and Taylor 1976][research_hypersonic_research_structure_1976], and active cooling as an alternative to material capability in [NASA 1991][research_cooling_hypersonic_1991]. Two conventional checks accompany it. Thin panels buckle before they yield, at

$$\sigma_{cr} = \frac{k \pi^2 E}{12 \left( 1 - \nu^2 \right)} \left( \frac{t_s}{b_s} \right)^2$$

with $t_s$ the skin thickness, $b_s$ the stiffener pitch, and $k$ near four for a simply supported panel, and the modulus $E$ itself falls with temperature so the buckling allowable degrades faster than the yield allowable. The root bending moment for an elliptic spanwise distribution at load factor $n$ is

$$M_{\text{root}} = \frac{n W b}{3 \pi}$$

feeding the cap area relation above, and the [wing loading][ref_wing_loading] and manoeuvring boundary follow the usual

$$\frac{W}{S}, \qquad V_A = \sqrt{\frac{2 n_{\max} W}{\rho S C_{L,\max}}}$$

The aircraft was never manoeuvre-limited in the sense the [X-1][ref_bell_x1] was, because at 39 kilopascals and a low maximum lift coefficient it could not generate limit load aerodynamically at altitude at all. The theory is [Boley and Weiner 1960][book_boley_weiner_1960], with modern treatments of the temperature-dependent case in [Su et al 2021][research_su_hwu_2021] and the graded case in [Yildirim et al 2020][research_yildirim_2020].

Oxidation, whose rate law is given above, is the third effect and the least discussed. A nickel-bearing alloy at 800 kelvin in moving air loses material to oxidation over time, which is a life limit rather than a strength limit. The NACA characterized the mechanism in metals directly in [Hill et al 1956][research_oxidation_ignition_1956], which treats oxidation and ignition together because at sufficient temperature in moving air the two are the same phenomenon at different rates. The nickel-copper alloy family the X-2 used has continued to receive attention, as [NASA 1989][research_monel_k500_1989] shows, and the creep behaviour of the nickel-base alloys that succeeded it is measured in [NASA 1985][research_creep_single_crystal_1985] and [NASA 1993][research_creep_rupture_superalloy_1993], with the panel fabrication problem in [Greene and Northrup 1975][research_rene41_panels_1975]. Contemporary coating work addressing the same mechanism appears in [Zubair et al 2022][research_zubair_ejaz_2022] and [Tian et al 2023][research_tian_zhang_2023].

### The Swept Wing

The wing was swept 40 degrees, and simple sweep theory gives the reason directly. Only the velocity component normal to the leading edge governs the compressible behaviour, so

$$M_{\text{eff}} = M_\infty \cos \Lambda, \qquad C_{L\alpha, \Lambda} = C_{L\alpha} \cos \Lambda$$

with $\Lambda$ the sweep angle. At Mach 3.196 the effective normal Mach number is 2.448, and the section behaves as though in a substantially slower flow. The cost is a lift-curve slope reduced by the same factor of 0.766, which raises the stall and landing speed through

$$V_{\text{stall}} = \sqrt{\frac{2W}{\rho S C_{L,\max} \cos \Lambda}}$$

and is why every swept-wing research aircraft of the period landed fast. Sweep also raises the [critical Mach number][ref_transonic] at which local flow first reaches sonic conditions, approximately as

$$M_{\text{crit}, \Lambda} \approx \frac{M_{\text{crit}, 0}}{\sqrt{\cos \Lambda}}$$

which for 40 degrees is a gain of about fourteen percent, and it lengthens the structural load path, since for a given span the spar runs a distance $b / (2 \cos \Lambda)$ from root to tip and the root bending moment rises accordingly,

$$M_{\text{root}, \Lambda} \approx \frac{M_{\text{root}, 0}}{\cos \Lambda}$$

A swept wing is therefore heavier than a straight one of the same span carrying the same load, before any thermal penalty is applied.

Two aeroelastic limits accompany it and both tighten as the structure heats, because the elastic modulus falls with temperature and every stiffness below is proportional to it. Static divergence of a typical section occurs at

$$q_D = \frac{K_\theta}{e S C_{L\alpha}}$$

with $K_\theta$ the torsional stiffness and $e$ the distance from the elastic axis to the aerodynamic centre. Aft sweep raises $q_D$, because bending washes the tip out rather than in. Control reversal is the sharper limit for a thin swept wing, since an aileron deflection twists the surface against its own rolling moment, and the reversal dynamic pressure is

$$q_R = \frac{K_\theta \, C_{L\delta}}{S \bar{c} \, C_{L\alpha} \left| C_{m\delta} \right|}$$

above which a roll input produces roll in the wrong direction. Dynamic behaviour is governed by the reduced frequency and flutter speed index,

$$k = \frac{\omega b}{2 V}, \qquad F_i = \frac{V_f}{b \omega_\alpha \sqrt{\mu_m}}, \qquad \mu_m = \frac{m_w}{\pi \rho b^2}$$

following [Theodorsen 1935][research_theodorsen_1935], with the programme history in [Garrick and Reed 1981][research_garrick_reed_1981] and the field bounded by [Collar 1946][research_collar_1946]. A heated structure is a softer structure, so the aeroelastic boundaries move down exactly as the thermal ones are approached, which is the coupling that makes the aerothermoelastic problem a single problem rather than two. That the modal characteristics themselves shift with temperature was later measured directly in [Snyder and Kehoe 1991][research_heated_plate_modes_1991] and correlated against analysis in [Kehoe and Deaton 1993][research_hot_structure_vibration_1993]. Control reversal on a flexible swept wing had already been formulated in [Diederich 1951][research_flexible_wing_lateral_1951], and the divergence problem in its most severe form, on forward-swept wings, generated a literature of its own in [Ricketts and Doggett 1980][research_fsw_divergence_tunnel_1980], [Bland 1980][research_fsw_airfoil_divergence_1980], [Cole 1986][research_fsw_divergence_study_1986], [Schuster and Lokos 1988][research_fsw_flight_divergence_1988], and [Weisshaar and Zeiler 1982][research_flexible_fsw_dynamics_1982], with the oblique-wing case in [A study of the 1973][research_oblique_wing_divergence_1973] and asymmetric sweep flutter in [Weisshaar and Crittenden 1976][research_asymmetric_sweep_flutter_1976]. Contemporary treatment of swept-wing aerodynamic characteristics appears in [Samputh et al 2024][research_samputh_moey_2024].

Supersonic aerodynamics of the [swept wing][ref_swept_wing] follow the linearized result of [Ackeret 1925][research_ackeret_1925], which for a thin surface at incidence gives

$$C_L = \frac{4 \alpha}{\sqrt{M_\infty^2 - 1}}, \qquad C_{D,\text{wave}} = \frac{4 \alpha^2}{\sqrt{M_\infty^2 - 1}}$$

and the important feature for this aircraft is the denominator. The [Prandtl-Glauert][ref_transonic] factor for supersonic flow,

$$\beta_s = \sqrt{M_\infty^2 - 1}$$

grows with Mach number, so lift-curve slope falls as $1/\beta_s$. At Mach 1.5 it is 3.578 per radian and at Mach 3.196 it is 1.318, a reduction by a factor of 2.72. Every aerodynamic surface on the aircraft, including the ones that keep it pointing forward, loses effectiveness in the same proportion. That is the seed of the accident.

[Dynamic pressure][ref_dynamic_pressure] at the final flight condition is

$$q = \frac{\gamma}{2} p M^2 = 0.7 \times 5481 \times 10.214 = 3.92 \times 10^{4} \ \text{pascals}$$

Lift and drag at that condition follow from the reference area through

$$L = q S C_L, \qquad D = q S C_D, \qquad C_L = \frac{W}{q S}$$

and with a mass near 5600 kilograms the level-flight equivalent [lift coefficient][ref_lift_coefficient] is 0.058, which is very low and reflects an aircraft flying fast rather than flying hard. Supersonic [lift-to-drag][ref_lift_to_drag] for a configuration of this class is bounded well below the subsonic value, since the wave term does not vanish,

$$C_D = C_{D0} + C_{D,\text{wave}} + \frac{C_L^2}{\pi A e}$$

and at this lift coefficient the induced term is negligible, so the aircraft is entirely wave and friction limited. The friction contribution referred to wing area follows from the turbulent flat-plate coefficient and the wetted-area ratio,

$$C_{D,f} = C_f \frac{S_{\text{wet}}}{S}$$

which over the 13.7 metre body length gives a length Reynolds number of $8.0 \times 10^{7}$, a skin friction coefficient of 0.0016, and, for a wetted-area ratio near four, a friction drag coefficient of about 0.006. The base contributes

$$C_{D,\text{base}} = -C_{p,b} \frac{A_b}{S}$$

with $C_{p,b}$ the base pressure coefficient, which for a rocket aircraft flying with the engine shut down is a substantial term and one reason the unpowered return is draggier than the powered climb. This is worth pausing on, because the intuitive account of the accident blames thin air and it is wrong. The X-2 at Mach 3.196 was in higher dynamic pressure than the [X-15][ref_na_x15] at Mach 6.7, which sees 32 kilopascals. Aerodynamic surfaces on the X-2 had force available. What they had lost was not dynamic pressure but lift-curve slope, and those are different failures with different remedies.

### Propulsion and the Throttleable Engine

The Curtiss-Wright XLR25 delivered about 66.7 kilonewtons from two chambers and, unlike the [X-1][related_post_a298_bell_x1] engine, could be throttled continuously rather than switched in quanta. Thrust follows the usual momentum and pressure terms,

$$F = \dot{m} v_e + (p_e - p_a) A_e$$

with $\dot{m}$ the mass flow, $v_e$ the exhaust velocity, and $A_e$ the exit area. Normalizing gives the [specific impulse][ref_specific_impulse],

$$I_{sp} = \frac{F}{\dot{m} g_0}$$

and at a value near 210 seconds for a turbopump-fed liquid oxygen and diluted alcohol engine, the mass flow at full thrust is

$$\dot{m} = \frac{66{,}723}{210 \times 9.80665} = 32.4 \ \text{kilograms per second}$$

Chamber and nozzle performance separate through the characteristic velocity and thrust coefficient,

$$c^{*} = \frac{p_0 A_t}{\dot{m}}, \qquad C_F = \frac{F}{p_0 A_t}, \qquad I_{sp} = \frac{c^{*} C_F}{g_0}$$

with $A_t$ the throat area, and the expansion ratio follows from the exit Mach number through

$$\varepsilon_n = \frac{A_e}{A_t} = \frac{1}{M_e} \left[ \frac{2}{\gamma + 1} \left( 1 + \frac{\gamma - 1}{2} M_e^2 \right) \right]^{\frac{\gamma + 1}{2 (\gamma - 1)}}$$

A [turbopump][ref_turbopump]-fed engine, unlike the pressure-fed X-1 installation, requires shaft power proportional to the pressure rise and the volumetric flow,

$$\mathcal{P}_{\text{pump}} = \frac{\dot{m} \, \Delta p}{\rho_{\text{prop}} \, \eta_{\text{pump}}}$$

and at 32.4 kilograms per second against a pressure rise of a few megapascals this is hundreds of kilowatts, supplied by a gas generator that is itself a combustion device requiring its own development, with even the material compatibility of the pump internals a research question, as [Stoltzfus and Benz 1986][research_turbopump_ignition_1986] shows for ignition resistance in oxygen-rich environments.

Throttling deserves emphasis because it is the part of the engine that took the years. A rocket chamber is stable over a narrow range of injector pressure drop and mixture ratio, and reducing thrust attacks both. The problem has a substantial modern literature, surveyed comprehensively in [Casiano et al 2009][research_throttling_review_2009] and traced historically in [Betts and Frederick 2010][research_throttling_history_2010], with deep-throttling demonstrators reported in [Giuliano et al 2007][research_cece_throttling_2007], alternative architectures in [Sackheim et al 2005][research_throttleable_engine_2005], and the injector scaling that governs it in [Kenny et al 2006][research_injector_throttling_2006]. That a capability the X-2 needed in 1955 still supports a review literature in 2010 is the measure of how hard it was. The turbine that drives the pumps must balance that demand,

$$\mathcal{P}_{\text{turb}} = \dot{m}_{gg} \, c_p \, T_{gg} \, \eta_t \left[ 1 - \left( \frac{p_{\text{out}}}{p_{gg}} \right)^{\frac{\gamma - 1}{\gamma}} \right] = \mathcal{P}_{\text{pump}}$$

and the gas generator flow $\dot{m}_{gg}$ is propellant that produces no useful thrust, so the arrangement costs specific impulse directly,

$$I_{sp,\text{eff}} = I_{sp} \left( 1 - \frac{\dot{m}_{gg}}{\dot{m}} \right)$$

Propellant volume follows from the densities,

$$V_{\text{tank}} = \frac{m_{ox}}{\rho_{ox}} + \frac{m_f}{\rho_f}$$

and the exit Mach number that sets the expansion ratio is recovered by inverting the area relation numerically, since it cannot be written explicitly in $M_e$. That is a large part of why the engine took as long as it did, and it is the concrete content of the claim above that the programme was inventing two things at once. Throttling changes $\dot{m}$ and therefore $p_0$, so a throttled chamber runs at lower pressure and slightly lower $c^{*}$, and the achievable throttle range is bounded below by injector stability,

$$\Delta p_{\text{inj}} \gtrsim 0.2 \, p_0$$

which cannot be maintained as $p_0$ falls without a variable injector. That inequality is why deep throttling was hard in 1955 and remains the governing constraint on throttleable liquid engines. With a launch mass of 11,299 kilograms and an empty mass of 5613 kilograms, the propellant load of 5686 kilograms gives a full-thrust burn time of

$$t_b = \frac{m_p}{\dot{m}} = \frac{5686}{32.4} = 175 \ \text{seconds}$$

and an ideal velocity increment from the [Tsiolkovsky relation][ref_tsiolkovsky] of

$$\Delta v = I_{sp} g_0 \ln \frac{m_0}{m_f} = 2059 \times \ln \frac{11{,}299}{5613} = 1441 \ \text{metres per second}$$

The energy accounting closes as it did for the X-1. Release from the B-50 at roughly 10,000 metres and 250 metres per second is an energy height of

$$h_e = h + \frac{V^2}{2g} = 13{,}187 \ \text{metres}$$

and the final condition of 19,992 metres at 943 metres per second is 65,326 metres, a gain of 52.1 kilometres. The specific energy delivered is $g \Delta h_e = 5.11 \times 10^{5}$ joules per kilogram against an ideal budget of $\Delta v^2 / 2 = 1.04 \times 10^{6}$, so

$$\eta_{\text{traj}} = \frac{g \Delta h_e}{\Delta v^2 / 2} = 0.49$$

which is within a percentage point of the X-1 figure and confirms that the published masses and thrust are mutually consistent. The remaining budget quantities are the mass fractions and thrust-to-weight,

$$\frac{m_p}{m_0} = \frac{5686}{11{,}299} = 0.50, \qquad \frac{T}{W} = \frac{66{,}723}{11{,}299 \times 9.80665} = 0.60$$

both higher than the X-1 figures of 0.41 and 0.49, which is the propulsive consequence of demanding Mach 3 rather than Mach 1.5. The rate at which energy height could be added is the specific excess power,

$$P_s = \frac{V \left( T - D \right)}{W}, \qquad \frac{dh_e}{dt} = P_s$$

and the climb angle available follows from the same excess through $\sin \gamma = (T - D) / W$. Throttling matters here because it decouples the burn duration from the thrust level, and a pilot who needs to remain inside a thermal exposure limit needs exactly that control. The propellant tradeoff space is covered in [A217 Rocket Propellant Chemistry][related_post_a217_rocket_propellant_chemistry], and modern work on regenerative cooling of such chambers appears in [Jeon and Park 2023][research_jeon_park_2023]. Small rocket-propelled research vehicles remain a live architecture, as [Vernacchia et al 2022][research_vernacchia_2022] describe.

### Stability and Control at Mach 3

This is the subsystem that ended the programme, and the argument can be made quantitatively.

[Directional stability][ref_directional_stability] is supplied by the vertical tail, whose contribution to the yawing-moment derivative is

$$C_{n\beta} = V_V \, C_{L\alpha_v} \, \eta_v, \qquad V_V = \frac{S_v l_v}{S b}$$

with $V_V$ the vertical tail volume coefficient, $S_v$ and $l_v$ the tail area and arm, $b$ the span, and $\eta_v$ the tail efficiency. The tail lift-curve slope carries the supersonic $1/\beta_s$ dependence derived above, so

$$C_{n\beta}(M) \propto \frac{1}{\sqrt{M_\infty^2 - 1}}$$

and directional stiffness at Mach 3.196 is 2.72 times weaker than at Mach 1.5 for the same geometry. The vertical tail also sits in a flow field disturbed by everything ahead of it, and the interference effects that result were measured at supersonic speeds in [Edwards 1956][research_vtail_interference_1956]. Later approaches to recovering directional control when the tail alone cannot supply it include forebody shaping, as in [Spearman and Driver 1959][research_forebody_deflection_1959], actuated strakes combined with thrust vectoring in [Lallman et al 1998][research_thrust_vectoring_strakes_1998], and the general effector prediction problem in [Maughmer et al 1990][research_control_effectors_1990]. The related departure mode on slender configurations is modelled in [Hong 1993][research_wing_rock_delta_1993]. Longitudinal stiffness behaves similarly, and the [aerodynamic centre][ref_aerodynamic_center] has by then migrated aft, so the aircraft is stiff in pitch and weak in yaw. The longitudinal counterpart is the [static margin][ref_longitudinal_static_stability],

$$SM = \frac{x_{np} - x_{cg}}{\bar{c}}, \qquad C_{m\alpha} = -C_{L\alpha} \, SM$$

and the damped modes that result are the short period and the [phugoid][ref_phugoid],

$$\omega_{sp} \approx \sqrt{\frac{-M_\alpha Z_w}{V} - M_q \frac{Z_w}{V}}, \qquad \omega_{ph} \approx \frac{g \sqrt{2}}{V}$$

with the phugoid period at 943 metres per second exceeding two minutes and therefore irrelevant on a flight of this length. Laterally the modes are the [Dutch roll][ref_dutch_roll], the roll subsidence, and the spiral,

$$\omega_{dr} \approx \sqrt{\frac{q S b \, C_{n\beta}}{I_z}}, \qquad \tau_r \approx -\frac{I_x}{L_p}, \qquad L_\beta N_r - L_r N_\beta > 0$$

the last being the spiral stability condition. The damping derivatives that would suppress a disturbance, principally $C_{mq}$ and $C_{nr}$, scale as

$$C_{mq}, \, C_{nr} \propto \frac{1}{\sqrt{M_\infty^2 - 1}} \cdot \frac{1}{V}$$

so they weaken twice over at high Mach number, once through the lift-curve slope and once through the rate normalization. An aircraft at Mach 3 is therefore stiff, fast-responding, and very lightly damped, which is the least forgiving combination available. That asymmetry matters for what follows.

[Inertia coupling][ref_inertia_coupling] arises from the gyroscopic terms in the [Euler moment equations][ref_euler_equations_rigid],

$$I_y \dot{q} = M + \left( I_z - I_x \right) p r, \qquad I_z \dot{r} = N + \left( I_x - I_y \right) p q$$

with $p$, $q$, and $r$ the roll, pitch, and yaw rates and $I_x$, $I_y$, $I_z$ the principal [moments of inertia][ref_moment_of_inertia]. These terms vanish in single-axis analysis and grow with the product of roll rate and the inertia difference. The phenomenon was predicted by [Phillips 1948][research_phillips_1948] before any aircraft met it, and its programme history is set out in [Day 1997][research_coupling_history_1997].

The X-2 configuration maximizes the danger. Mass is concentrated in a long fuselage holding propellant, and the wings are short and swept, so $I_z - I_x$ is large. Divergence follows when the roll rate approaches the lower of the two aerodynamic natural frequencies,

$$\omega_\alpha = \sqrt{\frac{q S \bar{c} \left| C_{m\alpha} \right|}{I_y}}, \qquad \omega_\beta = \sqrt{\frac{q S b \, C_{n\beta}}{I_z}}, \qquad p_{\text{crit}} \approx \min \left( \omega_\alpha, \omega_\beta \right)$$

Evaluate with representative values. Take a reference area of 24.16 square metres, a mean chord of 2.4 metres, a span of 9.83 metres, a mass at the test point of 5600 kilograms, radii of gyration giving $I_y = 9.4 \times 10^{4}$ and $I_z = 1.07 \times 10^{5}$ kilogram square metres, a pitch stiffness of 0.3 per radian, and a directional stiffness of 0.1 per radian weakened by Mach number. Then

$$\omega_\alpha = 2.69 \ \text{radians per second}, \qquad \omega_\beta = 2.95 \ \text{radians per second}$$

$$p_{\text{crit}} \approx 2.69 \ \text{radians per second} = 154 \ \text{degrees per second}$$

The roll rate an input produces follows from the balance of aileron moment against roll damping,

$$p_{ss} = -\frac{C_{l \delta_a} \, \delta_a}{C_{l p}} \cdot \frac{2V}{b}$$

with $C_{l\delta_a}$ the aileron effectiveness and $C_{lp}$ the roll damping derivative, and the time constant of the approach to that steady rate is

$$\tau_r = -\frac{2 I_x V}{q S b^2 C_{lp}}$$

Both derivatives carry the supersonic $1 / \beta_s$ falloff, so aileron effectiveness and roll damping weaken together and the ratio that sets $p_{ss}$ is roughly preserved while the response slows. The time to reach that steady rate from a step input follows the first-order response

$$p(t) = p_{ss} \left( 1 - e^{-t / \tau_r} \right)$$

so the critical rate is crossed at

$$t_{\text{crit}} = -\tau_r \ln \left( 1 - \frac{p_{\text{crit}}}{p_{ss}} \right)$$

and for a commanded rate twice the critical one with a roll time constant of half a second, the threshold is passed in about 0.35 seconds, well before the pilot could perceive the rate as excessive. The practical consequence is that a control input which produced an acceptable roll rate at Mach 1.5 produces a comparable one at Mach 3.2, so the pilot has no natural feedback that the safe boundary has moved. A fighter of the period rolled at two to three hundred degrees per second. The X-2 at Mach 3.196 therefore had a critical roll rate comfortably inside what a pilot could command with a normal control input, and nothing in the cockpit told him where that boundary was. The inertia ratios that govern the severity are

$$\mu_1 = \frac{I_z - I_x}{I_y}, \qquad \mu_2 = \frac{I_x - I_y}{I_z}$$

and both are large for this configuration. The values above are representative rather than measured properties of this airframe, and the conclusion they support is the order of magnitude rather than the decimal.

### The Divergence Derived

The critical roll rate above is a threshold. What happens past it is worth deriving, because it explains why the motion was unrecoverable rather than merely uncomfortable.

Linearize the pitch and yaw equations about a steady roll rate $p$, retaining the gyroscopic terms and the aerodynamic stiffnesses, and neglect damping, which is small at this condition for the reasons given above. Writing $\alpha$ and $\beta$ for the angle of attack and sideslip perturbations, the coupled system is

$$\ddot{\alpha} + \omega_\alpha^2 \alpha = \left( \frac{I_z - I_x}{I_y} \right) p \, \dot{\beta} + p^2 \alpha$$

$$\ddot{\beta} + \omega_\beta^2 \beta = \left( \frac{I_x - I_y}{I_z} \right) p \, \dot{\alpha} + p^2 \beta$$

in which two distinct effects appear. The terms in $p \dot{\beta}$ and $p \dot{\alpha}$ exchange energy between the two axes, and the terms in $p^2$ subtract directly from the aerodynamic stiffness. Seeking solutions of the form $e^{\lambda t}$ gives a quartic characteristic equation whose stability boundary reduces, when the cross-coupling is neglected, to the pair of conditions

$$\omega_\alpha^2 - p^2 > 0, \qquad \omega_\beta^2 - p^2 > 0$$

which is the threshold quoted above, restated as the roll rate at which the effective stiffness in one axis reaches zero. Past that point the corresponding root is real and positive and the motion diverges exponentially rather than oscillating.

The growth rate follows directly. For a roll rate exceeding the pitch threshold the unstable root is

$$\lambda = \sqrt{p^2 - \omega_\alpha^2}$$

so at a roll rate of 3.5 radians per second against $\omega_\alpha = 2.69$,

$$\lambda = \sqrt{3.5^2 - 2.69^2} = 2.24 \ \text{per second}$$

with an e-folding time of

$$\tau_{\text{div}} = \frac{1}{\lambda} = 0.45 \ \text{seconds}$$

An initial one-degree disturbance therefore reaches thirty degrees of angle of attack in

$$t = \tau_{\text{div}} \ln \frac{30}{1} = 0.45 \times 3.40 = 1.5 \ \text{seconds}$$

That is the number that matters. A pilot cannot diagnose an unfamiliar divergence, decide, and act inside a second and a half, and at Mach 3 there is no margin to absorb the excursion. The X-3 encounters and the fighter departures of the same era share this arithmetic, and it is why the response across the fleet was to prevent the entry rather than to train the recovery.

The loads that follow are not survivable either. An angle of attack excursion $\Delta \alpha$ at dynamic pressure $q$ produces a normal load factor increment

$$\Delta n = \frac{q S C_{L\alpha} \Delta \alpha}{W}$$

and at 39.2 kilopascals, a reference area of 24.16 square metres, a lift-curve slope of 1.3 per radian and a weight of 54.9 kilonewtons, a thirty degree excursion gives

$$\Delta n = \frac{39{,}188 \times 24.16 \times 1.3 \times 0.524}{54{,}900} = 11.7$$

which exceeds any structural limit the aircraft carried and exceeds human tolerance in the lateral axis by a wide margin. The aircraft did not fail structurally before the pilot lost the ability to act, but the two thresholds are close enough that the distinction is academic.

The aircraft had no other means of control. It carried no [reaction control system][ref_rcs]. When the aerodynamic surfaces lost authority there was nothing else, and the [X-15][ref_na_x15] carried reaction controls specifically because this class of problem had by then been recognized, a lineage traced in [Gelzer and Peebles 2015][research_hsfrs_rcs_2015].

### Instrumentation

The measurements the programme existed to make were skin temperatures, which meant [thermocouples][ref_thermocouple] distributed through the structure rather than the pressure orifices that dominated the [X-1][related_post_a298_bell_x1] installation. A thermocouple embedded in a skin measures the skin, not the gas, and converting one to the other requires the heat balance derived above, so the data reduction is a thermal inverse problem rather than a direct reading.

The sensor has its own dynamics. A [thermocouple][ref_thermocouple] junction of characteristic dimension $d$ responds with a first-order lag

$$\tau_{tc} = \frac{\rho_j c_j}{h_c} \cdot \frac{V_j}{A_j} \approx \frac{\rho_j c_j d}{6 h_c}$$

and for a half-millimetre steel bead against a convective coefficient of a few hundred watts per square metre kelvin this is of order half a second. Against a skin heating at thirty kelvin per second that lag is not negligible, and the indicated temperature trails the true one by

$$T_{\text{true}} - T_{\text{indicated}} \approx \tau_{tc} \frac{dT}{dt} \approx 20 \ \text{kelvin}$$

which must be corrected out. A probe measuring gas rather than metal has a further error, since it recovers only part of the stagnation temperature,

$$T_{\text{probe}} = T_\infty \left( 1 + r_p \frac{\gamma - 1}{2} M^2 \right)$$

with $r_p$ the probe recovery factor, typically between 0.85 and 0.98 and itself a calibration quantity.

Airspeed and Mach number came from a pitot-static installation with the same difficulties treated at length for the X-1 and calibrated by the same methods, including [Hasel and Coletti 1948][research_pitot_supersonic_1948] on supersonic pitot behaviour and [Thompson et al 1950][research_airspeed_calibration_1950] on flight calibration of airspeed systems. At Mach 3 the bow shock is strong, so the Rayleigh correction is large and unambiguous. The supersonic pitot relation is

$$\frac{p_{02}}{p_1} = \left[ \frac{(\gamma + 1)^2 M_1^2}{4 \gamma M_1^2 - 2(\gamma - 1)} \right]^{\frac{\gamma}{\gamma - 1}} \cdot \frac{1 - \gamma + 2 \gamma M_1^2}{\gamma + 1}$$

and at Mach 3.196 it gives 13.6 against an isentropic value of 49.1, so the two differ by a factor of 3.6. Compare the [X-1][ref_bell_x1] at Mach 1.06, where the same two expressions differ by 0.02 percent and the measurement is nearly degenerate. The X-2 knew its Mach number far better than the X-1 knew its own, which is a counterintuitive and entirely real consequence of shock strength growing with Mach number. The sensitivity of the inferred Mach number to a pressure error,

$$\frac{dM}{M} = \frac{1 + \frac{\gamma - 1}{2} M^2}{\gamma M^2} \cdot \frac{d \left( p_{02} / p_1 \right)}{p_{02} / p_1}$$

falls as $M$ rises, so high-speed air data is intrinsically better conditioned than transonic air data.

Uncertainty propagates by the usual relation,

$$u_c^2(y) = \sum_i \left( \frac{\partial y}{\partial x_i} \right)^2 u^2(x_i)$$

as set out in [Taylor 1997][book_taylor_1997_error_analysis] and [Bevington and Robinson 2002][book_bevington_robinson_2002], and the heating measurement carries an amplification of its own. Recovering the convective flux from a measured temperature history requires differentiating that history,

$$\dot{q}_{\text{conv}} = C_A \frac{dT_w}{dt} + \varepsilon \sigma_{SB} T_w^4$$

and differentiation amplifies noise, so a temperature record good to one percent does not give a flux good to one percent. Strain gauging a hot structure is itself a research problem, since the gauge, its adhesive, and its lead wires all respond to temperature as well as to strain, and the apparent strain that results must be calibrated out. [NASA 1979][research_yf12_strain_gauges_1979] documents that on a supersonic aircraft wing, and the loads calibration methodology it feeds is described in [Jenkins and Kuhl 1977][research_loads_calibration_1977]. [Strain gauges][ref_strain_gauge], [accelerometers][ref_accelerometer], and [telemetry][ref_telemetry] carried the remainder, and the modern descendant of the whole discipline is surveyed in [Grauer and Morelli 2023][research_grauer_morelli_2023]. The uncertainty framing that now accompanies such campaigns is treated by [Weiss et al 2022][research_weiss_staudacher_2022], and modern air data practice by [Jurado and McGehee 2019][research_jurado_mcgehee_2019] and [Takahashi et al 2026][research_takahashi_2026_airdata].

### Escape

The escape provision deserves a subsection because it was used once in flight and failed.

The X-2 carried a jettisonable nose capsule rather than an [ejection seat][ref_ejection_seat], on the reasoning that a seat exposes an occupant to a dynamic pressure of

$$q_{\text{exposure}} = \frac{1}{2} \rho V^2$$

which at the flight conditions of interest is tens of kilopascals and produces windblast loads no unprotected person survives. A capsule protects against that. It also introduces a sequence that must all work, being separation, stabilization, deceleration, parachute deployment, and finally egress or ground impact under canopy. The reliability of a series chain is the product of its links,

$$P_{\text{success}} = \prod_{i=1}^{n} p_i$$

so a system of five links each at ninety percent succeeds only 59 percent of the time. The capsule must also decelerate, and its trajectory is governed by its ballistic coefficient

$$\beta_c = \frac{m_c}{C_D A_c}$$

with a terminal descent speed in the lower atmosphere of

$$V_{\text{term}} = \sqrt{\frac{2 \beta_c g}{\rho}}$$

so a compact heavy capsule falls fast and must deploy a parachute to survive, while a light draggy one decelerates aerodynamically but is harder to stabilize. The deceleration during atmospheric capture scales as

$$a_{\max} \approx \frac{V_e^2 \sin \gamma_e}{2 e H}$$

with $H$ the atmospheric scale height, which is the same Allen-Eggers result used for entry vehicles elsewhere in this series. Descent under canopy closes the chain. A parachute of drag area $C_D A_p$ carrying a capsule of mass $m_c$ reaches a terminal speed

$$V_{\text{term}} = \sqrt{\frac{2 m_c g}{\rho \, C_D A_p}}$$

and for a 450 kilogram capsule descending at seven metres per second at sea level the required drag area $C_D A_p$ is 147 square metres, which at a canopy drag coefficient of 1.4 is 105 square metres of cloth and a canopy roughly twelve metres across. Deploying something that size at speed produces an opening load

$$F_{\text{open}} = C_X \, q \, C_D A_p$$

with $C_X$ the opening shock factor, so deployment must be delayed until dynamic pressure has fallen or the canopy must be reefed. That delay is itself a link, and it is the link that failed. Supersonic deceleration and parachute deployment remain difficult enough that they are still flight-tested as their own problem, as [Tanner et al 2015][research_ldsd_ballute_2015] and [Van Norman et al 2015][research_ldsd_dynamics_2015] report for a planetary decelerator six decades later. The wind tunnel stability work on such a capsule in [Goddwin 1949][research_nose_capsule_1949] addresses one link. It cannot address the others. The [X-15][ref_na_x15] programme chose a seat instead, as documented in [Hegenwald 1958][research_x15_escape_1958], accepting the windblast problem in exchange for a shorter chain.

## The Flight Test Record

The first aircraft, serial 46-675, began glide flights in 1952. The first landing is documented in [Day and Stillwell 1952][research_x2_first_landing_1952] and the glide programme in [Day 1953][research_x2_glide_1953]. On 12 May 1953 it was destroyed during a captive flight when a propellant explosion occurred while still attached to the carrier. Bell test pilot Jean Ziegler and a B-50 crew member were killed, and the wreckage fell into Lake Ontario. The programme continued with the second aircraft, 46-674.

Powered flying with 46-674 proceeded through 1955 and 1956 by the incremental method established with the X-1. Frank Everest reached Mach 2.87 on 23 July 1956. Iven Kincheloe reached 126,200 feet on 7 September 1956, which was then the greatest altitude any person had attained and earned him a widely repeated description as the first man in space, a claim that is not correct against the [Karman line][ref_karman_line] at 100 kilometres but was reasonable in the language of the period. Kincheloe flew chase for the final flight in a [North American F-100 Super Sabre][ref_f100].

On 27 September 1956 Milburn Apt flew the aircraft for the first time. He reached Mach 3.196 at 65,589 feet, becoming the first person to exceed Mach 3. The engine burned about twelve and a half seconds longer than planned, which carried him further and faster than the profile intended and left him further from the lake bed than he should have been. He initiated a turn back toward [Edwards Air Force Base][ref_edwards_afb] while still above Mach 3. The aircraft departed into an inertia-coupled divergence and tumbled. Apt separated the nose capsule. The capsule's primary parachute did not deploy successfully and he was killed on impact. The aircraft was destroyed and the programme ended with that flight.

The state of the art the programme was operating within is captured in the [NACA 1958 conference on high-speed aerodynamics][research_highspeed_conference_1958], which convened as the X-2 was flying. The flight behaviour is reported in [Day and Reisert 1959][research_x2_mach32_1959], which is the primary technical account and should be read by anyone who wants the details rather than the narrative.

Two arithmetic points about the record are worth stating. First, the recorded speed of 2094 miles per hour and the recorded Mach number of 3.196 are not exactly consistent under the standard atmosphere, which gives 943 metres per second or 2109 miles per hour at that Mach number and altitude. The 0.7 percent discrepancy reflects a real atmosphere differing from the standard model, and neither figure should be quoted to four significant figures. Second, the twelve and a half seconds of extra burn is a large fraction of the eighteen-second thermal margin derived above, and while the aircraft was not lost to heating, the overburn is the same kind of margin erosion.

The programme can be scored against the information accounting used in the [series opener][related_post_a297_xplanes_framing]. With a prior uncertainty $\sigma_0$, a per-flight measurement uncertainty $\sigma_m$, and a target $\sigma_T$, the required flight count in a given condition band is

$$n^{*} = \left\lceil \sigma_m^2 \left( \frac{1}{\sigma_T^2} - \frac{1}{\sigma_0^2} \right) \right\rceil$$

and the information returned is

$$I_n = \frac{1}{2} \ln \frac{\sigma_0^2}{\sigma_n^2}$$

following [Lindley 1956][research_lindley_1956] and [Chaloner and Verdinelli 1995][research_chaloner_verdinelli_1995]. The X-2 flew twenty flights across two airframes, glides included, and reached its design condition once. Against a fleet sized by the attrition condition

$$\sum_{i=0}^{n_a - 1} \binom{n}{i} p^i (1-p)^{n-i} \ge 1 - \alpha$$

a per-flight loss probability of ten percent, which is what the record actually shows, would demand five or more airframes for ninety-five percent confidence of completing twenty flights. Two were built. The programme was under-resourced against its own risk from the beginning, and continuing after the first loss with a single airframe made that worse. The two aircraft made twenty flights between June 1952 and September 1956, glides included, and the powered flights number between ten and thirteen depending on the account, [Bell X-2][ref_bell_x2] giving ten. The programme therefore cost two aircraft, two pilots, and one carrier crew member across twenty flights, which is the worst loss rate of any aircraft in this series.

### The Unpowered Return

Every X-2 flight ended the way every [X-1][ref_bell_x1] flight ended, with an unpowered arrival on a lake bed, and the aircraft was worse at it than its predecessor.

An unpowered glide holds

$$\tan \gamma_g = \frac{1}{L / D}, \qquad w_s = \frac{V}{L / D}$$

with $\gamma_g$ the glide angle and $w_s$ the sink rate. The best glide ratio follows from the subsonic drag polar,

$$\left( \frac{L}{D} \right)_{\max} = \frac{1}{2} \sqrt{\frac{\pi A e}{C_{D0}}}$$

and with an aspect ratio of

$$A = \frac{b^2}{S} = \frac{9.83^2}{24.16} = 4.0$$

an efficiency factor of 0.8 and a zero-lift drag coefficient near 0.02, this gives 11.2 and a glide angle of 5.1 degrees. The landing weight after propellant exhaustion is 55.0 kilonewtons, so with a swept-wing maximum lift coefficient reduced by $\cos \Lambda$ the stall speed is

$$V_{\text{stall}} = \sqrt{\frac{2W}{\rho S C_{L,\max}}} = \sqrt{\frac{2 \times 55{,}048}{1.10 \times 24.16 \times 0.9}} = 68 \ \text{metres per second}$$

An approach flown at 1.3 times stall is 88 metres per second with a sink rate of

$$w_s = \frac{88}{11.2} = 7.9 \ \text{metres per second}$$

That is a fast, steep, single-attempt arrival with no engine and a wing optimized for Mach 3 rather than for landing. The [X-15][ref_na_x15] inherited the same problem and its first-flight launch and landing characteristics are reported in [Finch and Matranga 1959][research_x15_first_flight_1959] and [McKay 1959][research_x15_first_landing_1959], which are the closest available comparison. Low-speed behaviour of the thin unswept research airplanes, for contrast, appears in [Sadoff and Sisk 1950][research_x4_stall_1950]. The low aspect ratio that suits supersonic flight is precisely what makes the glide poor, and the sweep that raises the critical Mach number is precisely what raises the stall speed. Both penalties are paid on every return, and they are the routine cost of the configuration rather than an incidental one.

## Comparison With Ground Prediction

The X-2 was predicted from ground data as the X-1 had been, and the pattern of agreement and disagreement is instructive.

Static stability and control characteristics were measured on scale models, including the lateral and aileron work in [Fournier and Silvers 1958][research_x2_lateral_model_1958] and the configuration studies of [NACA 1956][research_config_stability_1956], with sweep and tail-height effects in [Fisher and Williams 1958][research_sweep_tail_height_1958] and the wider fighter-configuration context in [Wetzel 1954][research_fighter_sweep_model_1954] and [Spreemann and Few 1954][research_prelim_static_1954]. Those methods predict the static derivatives acceptably.

What they could not predict was the coupled dynamic behaviour, for a reason that is structural rather than a matter of tunnel quality. Inertia coupling depends on the inertia distribution of the full-scale aircraft, and a wind tunnel model is not dynamically similar in inertia unless it is deliberately built to be. The formal statement is the one [Buckingham 1914][research_buckingham_1914] supplies, that a relation among $n$ dimensional quantities involving $k$ independent dimensions reduces to a relation among

$$n - k \ \text{dimensionless groups}$$

so the number of parameters a scale test must reproduce is fixed by the physics rather than chosen by the experimenter. A dynamically similar model must match not only the [Mach number][ref_mach_number] and Reynolds number but the mass ratio and the non-dimensional inertias,

$$\mu_m = \frac{m}{\rho S b}, \qquad \hat{I}_x = \frac{I_x}{\rho S b^3}, \qquad \hat{I}_y = \frac{I_y}{\rho S \bar{c}^3}, \qquad \hat{I}_z = \frac{I_z}{\rho S b^3}$$

and must also match the reduced frequency that sets how fast the motion is relative to the flow,

$$k = \frac{\omega b}{2 V}$$

A geometrically scaled force model built for a balance matches the first two groups and none of the last four, because its mass and inertia are set by whatever it is machined from. The coupling boundary depends on $\hat{I}_z - \hat{I}_x$ and therefore cannot appear. Matching requires the mass ratio and the inertia ratios to scale together with the aerodynamic parameters, and a static force model matches none of them. The quantity that killed the X-2 was therefore invisible to the dominant ground method by construction, not by oversight. Free-flight and dynamically scaled models address this, and the balance techniques required are described in [Sharpes and Carroll 1973][research_roll_coupling_balance_1973]. Building one is a mass-properties problem rather than an aerodynamic one. For a geometric scale $1/k$ the model mass and inertias must satisfy

$$m_m = \frac{m_f}{k^3} \cdot \frac{\rho_m}{\rho_f}, \qquad I_m = \frac{I_f}{k^5} \cdot \frac{\rho_m}{\rho_f}$$

with subscripts $m$ and $f$ for model and full scale and $\rho$ the ambient density in each case, and the fifth-power dependence means an inertia error that is trivial at full scale is enormous when scaled back. Meeting it requires ballasting a hollow model to a specified inertia tensor, which is a different craft from machining a force model. It was not unknown. The Langley free-flight tunnel had been investigating dynamic stability and control on dynamically scaled models since at least [Grana and Shanks 1952][research_free_flight_tunnel_1952], and the free-spinning tunnel applied the same discipline to departure and recovery, as [Bowman and Healy 1960][research_spin_tunnel_1960] shows. Those facilities were the right instrument for the X-2 question and were not used on it. Later research aircraft were characterized this way as a matter of course, as [Boyden 1974][research_supercritical_dynamic_1974] illustrates, and the quality of the flow in which such tests are run became a design subject in its own right in [NASA 1990][research_low_disturbance_tunnels_1990]. The analysis that eventually made the phenomenon predictable, including the effect of a non-constant pitching-moment derivative in [Davari and Laitone 1977][research_nonconstant_cma_1977], came after the aircraft it would have saved.

Heating prediction had a parallel problem. The correlations were validated against free-flight bodies at conditions the tunnels could not reach, including [Rumsey and Lee 1958][research_heat_transfer_mach146_1958] at Mach numbers up to 14.6, the rocket-propelled models of [Stephens 1959][research_rocket_model_heating_1959], cone measurements in [Rumsey and Lee 1961][research_cone_heat_transfer_1961], and polished-nose skin temperature measurements in [Rashis and Bond 1961][research_skin_temp_freeflight_1961]. Transition location remained the dominant uncertainty, because laminar and turbulent heating differ by a large factor and the transition point was not predictable, a difficulty measured in flight by [Banner et al 1958][research_transition_flight_1958] and still under active study in [Nie et al 2022][research_nie_song_2022] and [Egorov 2025][research_egorov_2025].

## What the Data Changed

The thermal result was delivered and it was used. The X-2 established that a steel airframe could carry a Mach 3 exposure of limited duration, that the binding constraint is time at temperature rather than temperature alone, and that thermal stress rather than thermal weakening governs the structural design. Those conclusions fed directly into the [X-15][ref_na_x15], whose skin and structural temperatures were measured in flight in [Reed and Watts 1961][research_x15_skin_temps_1961] and whose heating results appear in [Banner et al 1962][research_x15_heating_1962] and whose programme lessons are gathered in [Dana 1993][research_x15_lessons_1993], and into the survey of heating across the hypersonic research fleet in [Lawing 1981][research_hypersonic_heating_survey_1981]. The design lineage runs onward to sustained high-temperature cruise in the [XB-70][ref_xb70] and the [SR-71][ref_sr71], the latter treated by [Merlin 2009][book_merlin_2009_blackbird], and to actively cooled structures of the kind studied in [Ellis et al 1978][research_cooled_honeycomb_1978] and trajectory shaping for cold-wall vehicles in [Lawing 1975][research_coldwall_descent_1975].

The coupling result was more consequential and was not the result anyone wanted. Apt's loss, following the [X-3][ref_douglas_x3] encounters and the near-losses on early swept-wing fighters, converted inertia coupling from a predicted curiosity into a design constraint. The consequences are visible in three places. Roll rate limits entered flight manuals across the fleet. Artificial damping became standard, as [Moul and Brown 1959][research_artificial_pitch_damping_1959] anticipated and every subsequent high-speed aircraft implemented. And vertical tails grew, because the only way to hold $C_{n\beta}$ at Mach 3 against the $1/\beta_s$ falloff is to increase $V_V$, which is why the [XB-70][ref_xb70] and the [SR-71][ref_sr71] carry the tail areas they do. The requirement is explicit. Holding $C_{n\beta}$ constant from Mach 1.5 to Mach 3.2 against the falloff demands

$$\frac{S_{v,2}}{S_{v,1}} = \frac{\beta_{s,2}}{\beta_{s,1}} = \frac{\sqrt{3.196^2 - 1}}{\sqrt{1.5^2 - 1}} = 2.72$$

so a tail sized for the lower Mach number must almost triple in area to give the same stiffness at the higher one, or the aircraft must accept artificial stabilization instead. Both routes were taken, and the second is why every high-speed aircraft after the X-2 carries a yaw damper. A rate feedback to the rudder,

$$\delta_r = -k_r \, r$$

augments the natural yaw damping derivative to

$$C_{nr, \text{aug}} = C_{nr} - k_r \, C_{n \delta_r} \frac{2V}{b}$$

so the Dutch roll damping ratio becomes

$$\zeta_{dr, \text{aug}} \approx -\frac{C_{nr, \text{aug}}}{2} \sqrt{\frac{q S b}{I_z}} \cdot \frac{b}{2V} \cdot \frac{1}{\omega_{dr}}$$

and a gain chosen to hold $\zeta_{dr}$ near 0.3 across the envelope recovers by feedback what the tail lost to Mach number. The same argument applied in pitch gives the pitch damper that [Moul and Brown 1959][research_artificial_pitch_damping_1959] investigated. Artificial damping does not, however, raise the divergence threshold derived above, because that threshold is set by stiffness rather than damping, and a damper cannot restore a stiffness that the $1 / \beta_s$ falloff has removed. That distinction is why roll rate limits were imposed alongside the dampers rather than instead of them. The [XB-70 stability summary][research_xb70_stability_1973] records that inheritance directly, and the modern sizing problem is treated by [Xie et al 2023][research_xie_cai_2023] and [Goud and Dwivedi 2022][research_goud_dwivedi_2022].

The escape result was negative and it also propagated. The capsule concept was not abandoned but its reliability chain was taken more seriously, and the X-15 chose an ejection seat.

There is a fourth consequence that is easy to miss. The X-2 is the clearest case in this series of a programme whose stated keystone and actual contribution diverge. It was built for heat and is remembered for coupling. An account that scores it only against its thermal objective records a success. An account that scores it against what it taught the community records something larger and much more expensive.

## The Contemporary Literature

| Cluster | Records |
|---|---|
| Swept wings and supersonic configuration aerodynamics | 478 |
| Rocket propulsion, throttling and combustion stability | 441 |
| Aeroelasticity, flutter and control effectiveness | 416 |
| Aerodynamic heating and the recovery temperature | 403 |
| Directional stability, damping and supersonic stability | 375 |
| High-temperature materials, creep and oxidation | 368 |
| Escape, capsules and parachute recovery | 301 |
| Boundary layers, transition and skin friction | 283 |
| Inertia coupling, roll coupling and departure | 234 |
| Instrumentation and measurement at temperature | 167 |
| Stability augmentation, flight control and envelope protection | 131 |
| Research airplanes, flight test and the unpowered return | 80 |
| Hot structures, thermal stress and aerothermoelasticity | 71 |
| Thermal protection and ablation | 51 |
| Real gas, hypersonic flow and similitude | 17 |
| Other high-speed aeronautical and foundational literature | 68 |
| **Total** | **3,884** |

Both of the X-2 threads are live, and the coupling thread has moved further than the thermal one.

Aerothermal structural analysis is now routinely coupled rather than sequential. [Chen and Zhao 2019][research_chen_zhao_2019] and [Ji and Xie 2022][research_ji_xie_2022] treat aerothermoelastic behaviour of hypersonic vehicles with reduced-order methods, and [Hu and Mahadevan 2019][research_hu_mahadevan_2019] frame the panel problem as a reliability question, which is the honest framing when the loads are uncertain. Thermal protection has become a materials discipline in its own right, with selection criteria in [Aronov and Klyagin 2021][research_aronov_klyagin_2021] and reusable material evaluation in [Chinnaraj et al 2024][research_chinnaraj_kim_2024]. Where ablation rather than heat sink is the mechanism, the modelling now runs from molecular processes upward as in [Prata et al 2022][research_prata_2022] and [Martin and Panesi 2022][research_martin_panesi_2022]. The all-moving surface at temperature, which is the X-2 control configuration in a modern setting, is analysed by [Bai et al 2022][research_bai_cao_2022].

Coupled rotational dynamics is where the contemporary literature is richest, and it has largely become a nonlinear dynamical systems subject. [Xu et al 2019][research_xu_yue_2019] study the chaotic regime of yaw, pitch, and roll coupling directly, which is the mathematics behind what Apt experienced. Bifurcation analysis is now the standard tool for locating departure boundaries, as [Nguyen et al 2021][research_nguyen_lowenberg_2021] demonstrate, and post-stall dynamics of large aircraft are treated by [Cen et al 2020][research_cen_li_2020]. Prevention has become a control problem, with dedicated architectures in [Altunkaya and Catak 2025][research_altunkaya_2025] and [Yildiz et al 2019][research_yildiz_akcal_2019], and envelope protection in [Lang et al 2025][research_lang_wang_2025]. The pilot side of the same loop is examined by [Shams et al 2026][research_shams_khouli_2026].

The institutional continuation is worth naming, because the X-2 accident belongs to a category that acquired a formal research programme. NASA treats loss of control as a named research area, with directions set out in [Belcastro 2014][research_loc_directions_2014], precursor analysis in [Belcastro et al 2014][research_loc_precursors_2014], subscale flight research in [Cunningham et al 2008][research_subscale_upset_2008], propulsion-only control as a backup in [Bull et al 1997][research_propulsion_backup_1997], and simulator fidelity for upset training in [Cunningham et al 2019][research_stall_training_2019]. Reading the 1956 accident against that programme is the clearest available demonstration that the X-2 found something real.

The material side has become quantitative in a way it was not in 1955. Creep rupture life is now predicted rather than tabulated, with mechanistic treatments in [Zhou et al 2024][research_zhou_yuan_2024] and [Zhang et al 2024][research_zhang_feng_2024] and a machine-learned correlation in [Wang et al 2024][research_wang_zhao_creep_2024], which is the direct descendant of the Larson-Miller parameter used above. Oxidation is likewise treated as a kinetic problem with engineered protection, as in [Kılıçay 2020][research_kilicay_2020], and thermal protection has become a modular design discipline in [Pan et al 2026][research_pan_zhang_2026].

Aerothermoelasticity has acquired the thing the X-2 most conspicuously lacked, which is a scaling theory. [Huang et al 2019][research_huang_friedmann_2019] derive scaling laws for hypersonic skin panels, so a subscale test can now be designed to represent a full-scale coupled response rather than merely to look like it. That is the formal answer to the similarity failure this article describes, arriving sixty years late. Semianalytical and coupled treatments follow in [Li et al 2024][research_li_wan_2024] and [Zhang et al 2026][research_zhang_zhao_2026], and the dynamically scaled flight test technique itself is surveyed by [Kong et al 2023][research_kong_pan_2023].

Rotational coupling now has a dedicated parametric literature. [Shen et al 2019][research_shen_huang_2019] study the effect of the yaw-to-roll coupling ratio directly, which is the non-dimensional group that governs the divergence derived above, and departure prediction has become a computable rather than an experimental question in [Tu et al 2024][research_tu_yan_2024] and [Askari and Cremaschi 2023][research_askari_2023]. The damping derivatives that were too weak to help the X-2 are now computed rather than measured, as [Guo and Ren 2019][research_guo_ren_2019] describe. Control laws carry envelope protection as a design requirement in [Moreira et al 2022][research_moreira_gripp_2022] and [Liang et al 2026][research_liang_lu_2026].

The unpowered return has its own guidance literature, with approach and landing for a gliding vehicle treated by [Al-Bakri et al 2020][research_albakri_2020] and single-segment guidance by [S. Hameed and G. R 2021][research_hameed_2021]. A pilot flying an X-2 to a lake bed by eye was performing unaided what is now a solved control problem.

Escape configuration continues to evolve, and [Sreenivasulu et al 2021][research_sreenivasulu_2021] trace that evolution across programmes, which is the appropriate context for the capsule decision this article criticizes.

Combustion instability, which is the mechanism that makes deep throttling hard, is simulated directly in [Xiong et al 2020][research_xiong_morgan_2020] and [Xiong et al 2022][research_xiong_liu_2022]. Real-gas and thermochemical nonequilibrium effects, which the X-2 stayed below and the X-15 did not, are computed in [Pan et al 2021][research_pan_cao_2021] and [Zeng et al 2023][research_zeng_yuan_2023].

Measurement has advanced on exactly the two fronts this article identified as limiting. Thermocouple attachment and its effect on the indicated temperature is studied by [Yang et al 2020][research_yang_yu_2020], transient distribution measurement by [Ji et al 2021][research_ji_duan_2021], and high-temperature strain gauging, which is the problem that defeated instrumentation on hot structures for decades, by [Wang et al 2025][research_wang_zong_2025]. The uncertainty framework that ties it together is compared across standards by [Zhao et al 2025][research_zhao_zhang_2025].

Supersonic configuration design continues in [Duan et al 2026][research_duan_wan_2026], [Takovitskii 2023][research_takovitskii_2023], and [Samputh et al 2024][research_samputh_moey_2024], and the civil supersonic question that the whole lineage opened is being reopened, as [Ross 2021][research_ross_2021] reports. Envelope expansion still proceeds by increments, as [Deepa and Gupta 2023][research_deepa_gupta_2023] describe, and structural load sensing has moved to fibre optics as in [Pena et al 2018][research_fiber_optic_loads_2018].

### Swept wings and supersonic configuration aerodynamics

**The external flow of a thin swept wing at supersonic speed.** Linearized supersonic wing theory, wing and body interference, drag due to lift, low-aspect-ratio planforms, and the supersonic transport and research configurations that inherited the layout. **The linearized theory collected here, named in 26 titles, is the source of the falloff in lift-curve slope with Mach number** that the article applies to the vertical tail.

**478 records.** \[[Aamir et al 2026][research_aamir_abbasi_2026]\] \[[Abarbanel 1977][research_abarbanel_1977]\] \[[Abuaf 1976][research_abuaf_1976]\] \[[Ackeret 1925][research_ackeret_1925]\] \[[Adams and Rubin 1958][research_adams_rubin_1958]\] \[[Advanced Fuel Research Inc East Hartford Ct 1957][research_advancedfuelresearchinceasthartfordct_1957]\] \[[Aerodynamic Phenomena in Supersonic 2020][research_aerodynamic_phenomena_2020]\] \[[Ageev and Pavlenko 2016][research_ageev_pavlenko_2016]\] \[[Ageev et al 2020][research_ageev_sosura_2020]\] \[[Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991]\] \[[Alvi 2012][research_alvi_2012]\] \[[An experimental and computational 1978][research_an_experimental_1978]\] \[[Anderson 1959][research_anderson_1959]\] \[[Anderson 1960][research_anderson_1960]\] \[[Andrew 1981][research_andrew_1981]\] \[[Aprovitola et al 2021][research_aprovitola_dinuzzo_2021]\] \[[Aprovitola et al 2022][research_aprovitola_dyblenko_2022]\] \[[Armstrong 1979][research_armstrong_1979]\] \[[Army War Coll Carlisle Barracks Pa 1952][research_armywarcollcarlislebarrackspa_1952]\] \[[Ashworth et al 1988][research_ashworth_mouch_1988]\] \[[Baals and Harris 1968][research_baals_harrisjr_1968]\] \[[Baals et al 1970][research_baals_robins_1970]\] \[[Babinsky 2014][research_babinsky_2014]\] \[[Bai et al 2015][research_bai_li_2015]\] \[[Barrett-Gonzalez and Wolf 2021][research_barrettgonzalez_wolf_2021]\] \[[Bartlett and Harris 1972][research_bartlett_harris_1972]\] \[[Bartlett and Re 1972][research_bartlett_re_1972]\] \[[Bartlett et al 1973][research_bartlett_harris_1973]\] \[[Bauer and Wood 1989][research_bauer_wood_1989]\] \[[Beeler et al 1956][research_beeler_1956]\] \[[Ben-Gida and Gurka 2022][research_bengida_gurka_2022]\] \[[Bennet-Clark 1972][research_bennetclark_1972]\] \[[Berger et al 2011][research_berger_carmona_2011]\] \[[Bernal 2016][research_bernal_2016]\] \[[Bertelrud 1981][research_bertelrud_1981]\] \[[Bippes 1990][research_bippes_1990]\] \[[Birckelbaw 1992][research_birckelbaw_1992]\] \[[Bishop 1951][research_bishop_1951]\] \[[Blank 1995][research_blank_1995]\] \[[Blood et al 2015][research_blood_ivanov_2015]\] \[[Bloxsom 1958][research_bloxsom_1958]\] \[[Bogdnoff 1953][research_bogdnoff_1953]\] \[[Bonavolontà et al 2024][research_bonavolonta_manoj_2024]\] \[[Bonnema and Smith 1988][research_bonnema_smith_1988]\] \[[Bowman 1995][research_bowman_1995]\] \[[Boyd 1965][research_boyd_1965]\] \[[Bradley et al 1969][research_bradley_johnston_1969]\] \[[Bridges 2008][research_bridges_2008]\] \[[Brown 1989][research_brown_1989]\] \[[Bui 2016][research_bui_2016]\] \[[Bui 2018][research_bui_2018]\] \[[Burris 1966][research_burris_1966]\] \[[Bushnell and Tripi 1986][research_bushnell_tripi_1986]\] \[[Byrnes 1951][research_byrnes_1951]\] \[[Calculation of Low Aspect 2008][research_calculation_of_2008]\] \[[Candler 2001][research_candler_2001]\] \[[Carafoli 1969][research_carafoli_1969]\] \[[Carafoli 1969][research_carafoli_1969_b]\] \[[Carlson 1964][research_carlson_1964]\] \[[Cassanova 1967][research_cassanova_1967]\] \[[Catalano and Sturek 2001][research_catalano_sturek_2001]\] \[[Catalano and Sturek 2001][research_catalano_sturek_2001_b]\] \[[Celmins 1990][research_celmins_1990]\] \[[Chang 1980][research_chang_1980]\] \[[Chapter 3. Aerodynamics of 1957][research_chapter_3_1957]\] \[[Chapter 3. Aerodynamics of 1960][research_chapter_3_1960]\] \[[Chapter 5. Wing-Body Interference 1957][research_chapter_5_1957]\] \[[Chaudhuri 1977][research_chaudhuri_1977]\] \[[Chen et al 2001][research_chen_khalid_2001]\] \[[Chen et al 2026][research_chen_wu_2026]\] \[[Cheng 1982][research_cheng_1982]\] \[[Chin et al 2020][research_chin_turpin_2020]\] \[[Chow 1979][research_chow_1979]\] \[[Clark and Adler 2016][research_clark_adler_2016]\] \[[Cockbill 2018][research_cockbill_2018]\] \[[Cookson 1976][research_cookson_1976]\] \[[Cosyn and Vierendeels 2005][research_cosyn_vierendeels_2005]\] \[[Covell et al 1990][research_covell_hernandez_1990]\] \[[Curry and Sim 1982][research_curry_sim_1982]\] \[[Darden 1984][research_darden_1984]\] \[[Davis][research_davis]\] \[[Davis and Marshall 2020][research_davis_marshall_2020]\] \[[de Nicola et al 1994][research_denicola_tognaccini_1994]\] \[[DeSpirito 2009][research_despirito_2009]\] \[[DeSpirito 2013][research_despirito_2013]\] \[[Devan 1989][research_devan_1989]\] \[[Dicarlo et al 1992][research_dicarlo_brown_1992]\] \[[Diggins 1951][research_diggins_1951]\] \[[Dikbas and Atik 2018][research_dikbas_atik_2018]\] \[[Driver 1974][research_driver_1974]\] \[[Duan et al 2026][research_duan_wan_2026]\] \[[Dukhnovskiy et al 2023][research_dukhnovskiy_lobkovskiy_2023]\] \[[Dupuis 1988][research_dupuis_1988]\] \[[Edwards 2014][research_edwards_2014]\] \[[Ehlers et al 1976][research_ehlers_johnson_1976]\] \[[Ehlers et al 1978][research_ehlers_epton_1978]\] \[[ElRamly][research_elramly]\] \[[Engelbrecht][research_engelbrecht]\] \[[Epstein 1954][research_epstein_1954]\] \[[Erickson et al 1990][research_erickson_schreiner_1990]\] \[[Erickson et al 1990][research_erickson_schreiner_1990_b]\] \[[Ericsson 1986][research_ericsson_1986]\] \[[ESDU Data Item estimates 1998][research_esdu_data_1998]\] \[[Experience Gained During Development 2010][research_experience_gained_2010]\] \[[Fasel and Sandberg 2006][research_fasel_sandberg_2006]\] \[[Fejer et al 1964][research_fejer_heath_1964]\] \[[Ferrari 1948][research_ferrari_1948]\] \[[Flat Wings in Inviscid 2020][research_flat_wings_2020]\] \[[Flax 1953][research_flax_1953]\] \[[Fleeter et al 1974][research_fleeter_mcclure_1974]\] \[[Fornasier 1984][research_fornasier_1984]\] \[[Fox and Breedlove 1974][research_foxjr_breedlovejr_1974]\] \[[Fujita et al 2004][research_fujita_matsushima_2004]\] \[[Fuller 1952][research_fuller_1952]\] \[[Furukawa and Makino 2007][research_furukawa_makino_2007]\] \[[G. The Experimental Aerodynamics 1957][research_g_the_1957]\] \[[German Development of the 2010][research_german_development_2010]\] \[[Glauert 1928][research_glauert_1928]\] \[[Goldbaum 1956][research_goldbaum_1956]\] \[[Goodyer 1990][research_goodyer_1990]\] \[[Gopal and Maddalena 2018][research_gopal_maddalena_2018]\] \[[Gopalarathnam et al 1997][research_gopalarathnam_selig_1997]\] \[[Gordnier 1993][research_gordnier_1993]\] \[[Gordnier 1995][research_gordnier_1995]\] \[[Gould 2001][research_gould_2001]\] \[[Graham 1958][research_graham_1958]\] \[[Graham et al 1954][research_graham_lagerstrom_1954]\] \[[Gratzer and O'Donnell 1965][research_gratzer_odonnell_1965]\] \[[Gratzer and Odonnell 1964][research_gratzer_odonnell_1964]\] \[[Gresham et al 2009][research_gresham_wang_2009]\] \[[Griffin and Jonas 1983][research_griffin_jonas_1983]\] \[[Gringorten 1967][research_gringorten_1967]\] \[[Gringorten and Tattelman 1970][research_gringorten_tattelman_1970]\] \[[Guderley 1987][research_guderley_1987]\] \[[Guderley 1988][research_guderley_1988]\] \[[Guiler and Huebsch 2005][research_guiler_huebsch_2005]\] \[[Guimarães et al 2021][research_guimaraes_cesnik_2021]\] \[[Gunn 1947][research_gunn_1947]\] \[[Gunn 1947][research_gunn_1947_b]\] \[[Guo et al 1988][research_guo_wang_1988]\] \[[Guttman and Crutcher 1968][research_guttman_crutcher_1968]\] \[[Hagerman and Hofstetter 1969][research_hagerman_hofstetter_1969]\] \[[Hallstaff 1961][research_hallstaff_1961]\] \[[Hammer et al 2021][research_hammer_garmann_2021]\] \[[Hammer et al 2023][research_hammer_garmann_2023]\] \[[Hancock 1959][research_hancock_1959]\] \[[Harris and Fasel 1996][research_harris_fasel_1996]\] \[[Hartley et al 1965][research_hartley_furey_1965]\] \[[Hassan et al 2010][research_hassan_abbass_2010]\] \[[Hayes 1946][research_hayes_1946]\] \[[Hendershot 1969][research_hendershot_1969]\] \[[Hensel 1964][research_hensel_1964]\] \[[Hermann 1950][research_hermann_1950]\] \[[Herrmann 2008][research_herrmann_2008]\] \[[Herrmann and Orlowski 1997][research_herrmann_orlowski_1997]\] \[[Hicks and Moulton 1988][research_hicks_moulton_1988]\] \[[History of Supersonic Transport 2020][research_history_of_2020]\] \[[Hong 1965][research_hong_1965]\] \[[Hoover 1947][research_hoover_1947]\] \[[Hosangadi et al 2015][research_hosangadi_paul_2015]\] \[[Hu et al 2012][research_hu_jameson_2012]\] \[[Hua et al 2025][research_hua_wang_2025]\] \[[Huffman and Fox 1985][research_huffman_foxjr_1985]\] \[[Theoretical studies to refine 1970][research_ii_1970]\] \[[Influence of wing geometry 1989][research_influence_of_1989]\] \[[Iosilevskii 2025][research_iosilevskii_2025]\] \[[Ishikawa et al 2007][research_ishikawa_kwak_2007]\] \[[Ishikawa et al 2008][research_ishikawa_kwak_2008]\] \[[Jameson 1977][research_jameson_1977]\] \[[Jameson and Caughey 1977][research_jameson_caughey_1977]\] \[[Jameson et al 2005][research_jameson_shankaran_2005]\] \[[Jamwal et al 2018][research_jamwal_hosangadi_2018]\] \[[Jiajan et al 2013][research_jiajan_chue_2013]\] \[[Jischke 1978][research_jischke_1978]\] \[[Johnson 1985][research_johnson_1985]\] \[[Johnson et al 1970][research_johnson_josepha_1970]\] \[[Johnson III and Wu 1974][research_johnsoniii_wu_1974]\] \[[Johnston 1998][research_johnston_1998]\] \[[Jones 1947][research_jones_1947]\] \[[Jones 1959][research_jones_1959]\] \[[Jones 1962][research_jones_1962]\] \[[Jones 1980][research_jones_1980]\] \[[Jordan 1972][research_jordan_1972]\] \[[Kandil et al 1993][research_kandil_kandil_1993]\] \[[Kariappa and Smith 1972][research_kariappa_smith_1972]\] \[[Kase et al 2020][research_kase_mizoguchi_2020]\] \[[Katz 1989][research_katz_1989]\] \[[Keenan and Kuhlman 1991][research_keenan_kuhlman_1991]\] \[[Keener 1984][research_keener_1984]\] \[[Khan et al 2019][research_khan_masud_2019]\] \[[Kim 2009][research_kim_2009]\] \[[Kim and Lee 2000][research_kim_lee_2000]\] \[[Klopfer and Nielsen 1979][research_klopfer_nielsen_1979]\] \[[Kolodner 1950][research_kolodner_1950]\] \[[Kopzon 1958][research_kopzon_1958]\] \[[Korivi et al 1998][research_korivi_newman_1998]\] \[[Krone 1980][research_kronejr_1980]\] \[[Krone 1980][research_kronejr_1980_b]\] \[[Kryvokhatko 2023][research_kryvokhatko_2023]\] \[[Kryvokhatko 2025][research_kryvokhatko_2025]\] \[[Kuhlman and Brown 1989][research_kuhlman_brown_1989]\] \[[Kuhlman and Liaw 1987][research_kuhlman_liaw_1987]\] \[[Kuhlman et al 1988][research_kuhlman_cerney_1988]\] \[[Kulfan and Sigalla 1978][research_kulfan_sigalla_1978]\] \[[Küchemann 1962][research_kuchemann_1962]\] \[[Laitone 1964][research_laitone_1964]\] \[[Lamar 1975][research_lamar_1975]\] \[[Lapygin and Tret'yakov 1986][research_lapygin_tretyakov_1986]\] \[[Larson 1987][research_larson_1987]\] \[[Lavrishcheva et al 2024][research_lavrishcheva_staroverov_2024]\] \[[Lee and Kim 2010][research_lee_kim_2010]\] \[[Lees 1959][research_lees_1959]\] \[[Lei et al 2016][research_lei_zhao_2016]\] \[[Li 2023][research_li_2023]\] \[[Li and Geiselhart 2026][research_li_geiselhart_2026]\] \[[Li and Stewart 1953][research_li_stewart_1953]\] \[[Li et al 1999][research_li_sobieczky_1999]\] \[[Li et al 2026][research_li_chen_2026]\] \[[Liang et al 2026][research_liang_lu_2026]\] \[[Licher 1956][research_licher_1956]\] \[[Lift/Drag Ratios of Optimised 1962][research_lift_drag_ratios_1962]\] \[[Lijewski 1980][research_lijewski_1980]\] \[[Lin 2025][research_lin_2025]\] \[[Lisunov 1960][research_lisunov_1960]\] \[[Liu 2022][research_liu_2022]\] \[[Liu and Lu 2011][research_liu_lu_2011]\] \[[Liu and Weng 2007][research_liu_weng_2007]\] \[[Liu et al 2025][research_liu_zhang_2025]\] \[[Livne 2023][research_livne_2023]\] \[[Livne 2023][research_livne_2023_c]\] \[[Livne 2023][research_livne_2023_d]\] \[[Lobanovskii 1983][research_lobanovskii_1983]\] \[[Lock 1958][research_lock_1958]\] \[[Lock 1963][research_lock_1963]\] \[[Lock and Bridgewater 1967][research_lock_bridgewater_1967]\] \[[Lovell 2001][research_lovell_2001]\] \[[Low aspect ratio wing 1992][research_low_aspect_1992]\] \[[Lucero 1984][research_lucero_1984]\] \[[Lucero 1985][research_lucero_1985]\] \[[Ludloff and Reiche 1947][research_ludloff_reiche_1947]\] \[[Machida et al 2007][research_machida_takatoya_2007]\] \[[Machida et al 2007][research_machida_yoshida_2007]\] \[[Magee et al 2015][research_magee_fugal_2015]\] \[[Maikapar 1966][research_maikapar_1966]\] \[[Maikapar 1993][research_maikapar_1993]\] \[[Makino and Noguchi 2003][research_makino_noguchi_2003]\] \[[Mangano and Martins 2021][research_mangano_martins_2021]\] \[[Mann and Carlson 1991][research_mann_carlson_1991]\] \[[Mann and Carlson 1994][research_mann_carlson_1994]\] \[[Mann and Mercer 1985][research_mann_mercer_1985]\] \[[Mansour 1984][research_mansour_1984]\] \[[Martin and Gerber 1953][research_martin_gerber_1953_b]\] \[[Martin and Gerber 1955][research_martin_gerber_1955]\] \[[Maruyama et al 2009][research_maruyama_matsushima_2009]\] \[[Mason 1983][research_mason_1983]\] \[[Masud et al 2017][research_masud_arif_2017]\] \[[Masud et al 2018][research_masud_khan_2018]\] \[[Mateescu 1986][research_mateescu_1986]\] \[[Matsuo and Kim 1993][research_matsuo_kim_1993]\] \[[Matthews et al 2025][research_matthews_prince_2025]\] \[[McCutchen 2006][research_mccutchen_2006]\] \[[McGrath 1993][research_mcgrath_1993]\] \[[McGrath 1995][research_mcgrath_1995]\] \[[McGrath et al 1989][research_mcgrath_walker_1989]\] \[[McMillin and Wood 1986][research_mcmillin_wood_1986]\] \[[Merkli 1975][research_merkli_1975]\] \[[Methodic for three-dimensional parametric 2024][research_methodic_for_2024]\] \[[Mikhail 1989][research_mikhail_1989]\] \[[Miles 1953][research_miles_1953]\] \[[Miller and Schemensky 1979][research_miller_schemensky_1979]\] \[[Miller and Wood 1983][research_miller_wood_1983]\] \[[Miller et al 1982][research_miller_wykes_1982]\] \[[Miller et al 1983][research_miller_wykes_1983]\] \[[Min et al 2026][research_min_jinjun_2026]\] \[[Mizoguchi et al 2014][research_mizoguchi_kajikawa_2014]\] \[[MlDDLETON and Carlson 1965][research_mlddleton_carlson_1965]\] \[[Moffeit et al 2023][research_moffeit_kumar_2023]\] \[[Moga 1980][research_moga_1980]\] \[[Moga and Dejarnette 1981][research_moga_dejarnette_1981]\] \[[Moin and Lele 1998][research_moin_lele_1998]\] \[[Monaghan and Friend 1973][research_monaghan_friend_1973]\] \[[Montoya 1970][research_montoya_1970]\] \[[Moore and Frei 1983][research_moore_frei_1983]\] \[[Moorthamers et al 2021][research_moorthamers_wiberg_2021]\] \[[Morikawa 1951][research_morikawa_1951]\] \[[Morikawa 1953][research_morikawa_1953]\] \[[Morito and Sidwell 1967][research_morito_sidwell_1967]\] \[[Morton 1956][research_morton_1956]\] \[[Mueller and Torres 2001][research_mueller_torres_2001]\] \[[Murakami et al 2008][research_murakami_kwak_2008]\] \[[Mysliwetz 1963][research_mysliwetz_1963]\] \[[Nadim Melhem et al 2024][research_nadimmelhem_richardmunroe_2024]\] \[[Nangia et al 2003][research_nangia_palmer_2003]\] \[[Narayan 1975][research_narayan_1975]\] \[[Narayan et al 2025][research_narayan_kumar_2025]\] \[[Bellman 1959][research_transonic_summary_1959]\] \[[Saltzman and Ayers 1995][research_supersonic_research_1995]\] \[[Van Norman et al 2015][research_ldsd_dynamics_2015]\] \[[Naval Ordnance Systems Command Washington Dc 1957][research_navalordnancesystemscommandwashingtondc_1957]\] \[[Newey][research_newey]\] \[[Nguyen 2025][research_nguyen_2025]\] \[[Nichols 1974][research_nichols_1974]\] \[[Nicolaides and Brady 1959][research_nicolaides_brady_1959]\] \[[Nielsen 1986][research_nielsen_1986]\] \[[Nietubicz 1975][research_nietubicz_1975]\] \[[Nusca 1984][research_nusca_1984]\] \[[Oggioni et al 2026][research_oggioni_riboldi_2026]\] \[[Ojiaku and Prakash 2026][research_ojiaku_prakash_2026]\] \[[Oktay and Asma 2000][research_oktay_asma_2000]\] \[[Olsen and Seegmiller 1993][research_olsen_seegmiller_1993]\] \[[Opalka 1968][research_opalka_1968]\] \[[Orme and Conners 1994][research_orme_conners_1994]\] \[[Orme and Gilyard 1993][research_orme_gilyard_1993]\] \[[Ormsbee 1962][research_ormsbee_1962]\] \[[Ortamevzi 2015][research_ortamevzi_2015]\] \[[Osipov 2019][research_osipov_2019]\] \[[Oswatitsch 1980][research_oswatitsch_1980]\] \[[Owens and Wahls 2001][research_owens_wahls_2001]\] \[[Pelletier and Mueller 1999][research_pelletier_mueller_1999]\] \[[Pfaff 1965][research_pfaff_1965]\] \[[Pipko 1966][research_pipko_1966]\] \[[Pittman and Bonhaus 1987][research_pittman_bonhaus_1987]\] \[[Pittman and Siclari 1984][research_pittman_siclari_1984]\] \[[Pivko 1956][research_pivko_1956]\] \[[Platou 1959][research_platou_1959]\] \[[Popytalov and Samsonov 1978][research_popytalov_samsonov_1978]\] \[[Portnoy 1961][research_portnoy_1961]\] \[[Prakash et al 2009][research_prakash_uthup_2009]\] \[[Pritchard 1969][research_pritchard_1969]\] \[[Probstein 1953][research_probstein_1953]\] \[[Properties and Design of 2012][research_properties_and_2012]\] \[[Radkey et al 1976][research_radkey_welge_1976]\] \[[Radkey et al 1978][research_radkey_welge_1978]\] \[[Rain Erosion Tests on 1955][research_rain_erosion_1955]\] \[[Raman 1999][research_raman_1999]\] \[[Rasmussen 1978][research_rasmussen_1978]\] \[[Ray and Kassing 1986][research_ray_kassing_1986]\] \[[Reed 1984][research_reed_1984]\] \[[Reuther 2002][research_reuther_2002]\] \[[Reuther and Jameson 1995][research_reuther_jameson_1995]\] \[[Reuther et al 1996][research_reuther_rimlinger_1996]\] \[[Reuther et al 1999][research_reuther_alonso_1999]\] \[[Rizk and Ben-Shmuel 1985][research_rizk_benshmuel_1985]\] \[[Rizzetta 1995][research_rizzetta_1995]\] \[[Roberts 1948][research_roberts_1948]\] \[[Robins and Carlson 1979][research_robins_carlson_1979]\] \[[Robinson 1948][research_robinson_1948]\] \[[Robinson and Robinson 1950][research_robinson_robinson_1950]\] \[[Robinson et al 2025][research_robinson_ouhabi_2025]\] \[[Roecker 1955][research_roecker_1955]\] \[[Rohl and Schrage 1992][research_rohl_schrage_1992]\] \[[Rom 1965][research_rom_1965]\] \[[Roos 1985][research_roos_1985]\] \[[Rose and Pittman 1989][research_rose_pittman_1989]\] \[[Rose et al 1988][research_rose_miller_1988]\] \[[Ross 2021][research_ross_2021]\] \[[Rowell 1964][research_rowell_1964]\] \[[Sabin 1957][research_sabin_1957]\] \[[Sadiq Ali Mir et al 2025][research_sadiqalimir_suhanaarsh_2025]\] \[[Sahoo and Peetala 2010][research_sahoo_peetala_2010]\] \[[Sahu 1986][research_sahu_1986]\] \[[Sahu 2007][research_sahu_2007]\] \[[Sahu 2011][research_sahu_2011]\] \[[Sakata 2002][research_sakata_2002]\] \[[Sakata and Davis 1977][research_sakata_davis_1977]\] \[[Sakata et al 1975][research_sakata_davis_1975]\] \[[Samputh et al 2024][research_samputh_moey_2024]\] \[[Sanghi et al 2024][research_sanghi_cesnik_2024]\] \[[Sanz 1986][research_sanz_1986]\] \[[Saric 2010][research_saric_2010]\] \[[Sathaye et al 2004][research_sathaye_yuan_2004]\] \[[Sboev D 2024][research_sboevd_2024]\] \[[Schmidt 1992][research_schmidt_1992]\] \[[Schmitt 1970][research_schmitt_1970]\] \[[Schmitt et al 1983][research_schmitt_destarac_1983]\] \[[Schnell 2023][research_schnell_2023]\] \[[Seacord and Teitelbaum 1947][research_seacord_teitelbaum_1947]\] \[[Sears 1947][research_sears_1947]\] \[[Sebastian 1967][research_sebastian_1967]\] \[[Serpieri and Kotsonis 2015][research_serpieri_kotsonis_2015]\] \[[Shankara and Nandi 1978][research_shankara_nandi_1978]\] \[[Shantz 1953][research_shantz_1953]\] \[[Sharif et al 2022][research_sharif_abbas_2022]\] \[[Sher et al 2022][research_sher_maqsood_2022]\] \[[Shields and Mohseni 2012][research_shields_mohseni_2012_b]\] \[[Shirokov et al 2024][research_shirokov_strelets_2024]\] \[[Shiryaev and Serebryansky 2022][research_shiryaev_serebryansky_2022]\] \[[Shiryaev et al 2023][research_shiryaev_maysak_2023]\] \[[Siag and Kumar 2026][research_siag_kumar_2026]\] \[[Siclari 1990][research_siclari_1990]\] \[[Siclari 1992][research_siclari_1992]\] \[[Sigal 1987][research_sigal_1987]\] \[[Silton 2003][research_silton_2003]\] \[[Silton et al 2017][research_silton_youn_2017]\] \[[Sim and Curry 1985][research_sim_curry_1985]\] \[[Smith 1953][research_smith_1953]\] \[[Smith 1961][research_smith_1961]\] \[[Smith 1969][research_smith_1969]\] \[[Smith et al 2025][research_smith_ramachandran_2025]\] \[[Snyder and Memory 2005][research_snyder_memory_2005]\] \[[Sotomayer and Weeks 1978][research_sotomayer_weeks_1978]\] \[[Spacht 1980][research_spacht_1980]\] \[[Sparkes 2024][research_sparkes_2024]\] \[[Spearman 1979][research_spearman_1979]\] \[[Stallings and Hartman 1981][research_stallings_hartman_1981]\] \[[Stanišić 1962][research_stanisic_1962]\] \[[Steimle et al 2008][research_steimle_schroder_2008]\] \[[Stengel 1969][research_stengel_1969]\] \[[Stengel 1970][research_stengel_1970]\] \[[Stewart 1946][research_stewart_1946]\] \[[Stewart 1956][research_stewart_1956]\] \[[Stewartson 1950][research_stewartson_1950]\] \[[Stewartson 1950][research_stewartson_1950_b]\] \[[Stewartson 1952][research_stewartson_1952]\] \[[Stoldt et al 2020][research_stoldt_johansen_2020]\] \[[Sturek and Mylin 1981][research_sturek_mylin_1981]\] \[[Sturek and Schiff 1981][research_sturek_schiff_1981]\] \[[Supersonic Aircraft High-Speed Civil 1997][research_supersonic_aircraft_1997]\] \[[Supersonic Flight 2025][research_supersonic_flight_2025]\] \[[Supersonic Flows Over Wings 2021][research_supersonic_flows_2021]\] \[[Supersonic Flows Over Wings 2025][research_supersonic_flows_2025]\] \[[Supersonic Three-dimensional Wing Theory 1960][research_supersonic_three_dimensional_1960]\] \[[Supersonic transport wing minimum 1992][research_supersonic_transport_1992]\] \[[Takovitskii 2023][research_takovitskii_2023]\] \[[Tamayo][research_tamayo]\] \[[Taylor and Gursul 2004][research_taylor_gursul_2004]\] \[[Technical applications for an 1976][research_technical_applications_1976]\] \[[Thibert and Arnal 2000][research_thibert_arnal_2000]\] \[[Thomas 1942][research_thomas_1942]\] \[[Thomas and Miller 1979][research_thomas_miller_1979]\] \[[Tilmann 1998][research_tilmann_1998]\] \[[Toong 1978][research_toong_1978]\] \[[Tuling et al 2013][research_tuling_dala_2013]\] \[[U.S. Supersonic Commercial Aircraft 1997][research_u_s_supersonic_1997]\] \[[Ueno et al 1998][research_ueno_matsuno_1998]\] \[[Van Dam 1986][research_vandam_1986]\] \[[Varvanifarahani 2004][research_varvanifarahani_2004]\] \[[Vaughn 1982][research_vaughnjr_1982]\] \[[Velden 1997][research_velden_1997]\] \[[Veley et al 2008][research_veley_khot_2008]\] \[[Verma and Hadjadj 2015][research_verma_hadjadj_2015]\] \[[Visbal 2012][research_visbal_2012]\] \[[Visbal 2017][research_visbal_2017]\] \[[Visbal and Garmann 2012][research_visbal_garmann_2012]\] \[[Vishwanathan][research_vishwanathan]\] \[[Walker 1973][research_walker_1973]\] \[[Wallace 1952][research_wallace_1952]\] \[[Wang 2024][research_wang_2024]\] \[[Wasserman 1952][research_wasserman_1952]\] \[[Webber and Houghton 1963][research_webber_houghton_1963]\] \[[Wegener 1977][research_wegener_1977]\] \[[Weinacht 2014][research_weinacht_2014]\] \[[Welge et al 1976][research_welge_radkey_1976]\] \[[Whitcomb 1952][research_whitcomb_1952]\] \[[Wilks 2006][research_wilks_2006]\] \[[Williams and Hunt 1980][research_williams_hunt_1980]\] \[[Wimpress and Swihart 1964][research_wimpress_swihart_1964]\] \[[Wing Theory in Supersonic 1969][research_wing_theory_1969]\] \[[Wing tunnel model for 1998][research_wing_tunnel_1998]\] \[[Wolfe 1964][research_wolfe_1964]\] \[[Wolkovitch 1984][research_wolkovitch_1984]\] \[[Wood and Bauer 1988][research_wood_bauer_1988]\] \[[Wood and Covell 1987][research_wood_covell_1987]\] \[[Wood and Miller 1984][research_wood_miller_1984]\] \[[Woodward 1968][research_woodward_1968]\] \[[Xu 2023][research_xu_2023]\] \[[Xue et al 2014][research_xue_khawaja_2014]\] \[[Yamazaki and Kusunose 2016][research_yamazaki_kusunose_2016]\] \[[Yates and Zeydel 1963][research_yates_zeydel_1963]\] \[[Yip et al 1980][research_yip_parlett_1980]\] \[[Yonezawa and Obayashi 2010][research_yonezawa_obayashi_2010]\] \[[Yoshida et al 2021][research_yoshida_bragg_2021]\] \[[Yu and Bernal 2016][research_yu_bernal_2016]\] \[[Zartarian 1956][research_zartarian_1956]\] \[[Zartarian and Hsu 1955][research_zartarian_hsu_1955]\] \[[Zhang 1995][research_zhang_1995]\] \[[Zhang and Taira 2022][research_zhang_taira_2022]\] \[[Zhu et al 2026][research_zhu_zhu_2026]\]

### Rocket propulsion, throttling and combustion stability

**The engine, and the reason a throttleable one took years.** Liquid rocket engines, turbopumps and gas generators, throttling, and combustion instability, with a smaller number of solid and hybrid motors whose instability shares the same acoustics. **Throttling is a small part of this literature and instability a large one.** Throttling or variable thrust is named in 56 titles, against 120 that name an instability, an oscillation or combustion stability, which is the relation the article describes, since reducing thrust moves a chamber toward the conditions in which it becomes unstable.

**441 records.** \[[A System Analysis of 2004][research_a_system_2004]\] \[[Abbe et al 1967][research_abbe_mclaughlin_1967]\] \[[Airplane and rocket flight 1990][research_airplane_and_1990]\] \[[Akmandor and Nagashima 1999][research_akmandor_nagashima_1999]\] \[[Alcock and Hagar 1989][research_alcock_hagar_1989]\] \[[Anderson et al 1995][research_anderson_ryan_1995]\] \[[Anderson et al 2012][research_anderson_son_2012]\] \[[Anderson et al 2013][research_anderson_heister_2013]\] \[[Anderson et al 2015][research_anderson_heister_2015]\] \[[Anikina et al 2026][research_anikina_renshaw_2026]\] \[[Aoki and Ota 1986][research_aoki_ota_1986]\] \[[Armstrong 1989][research_armstrong_1989]\] \[[Armstrong and Kilner 1953][research_armstrong_kilner_1953]\] \[[Armstrong and Miller 1968][research_armstrong_miller_1968]\] \[[Armstrong and Schlumberger 1990][research_armstrong_schlumberger_1990]\] \[[Av and Jayabalakrishnan 2026][research_av_d_2026]\] \[[Ayran et al 2026][research_ayran_bayezit_2026]\] \[[Back and Cuffel 1972][research_back_cuffel_1972]\] \[[Bai et al 2020][research_bai_cheng_2020]\] \[[Baier et al 2019][research_baier_karnam_2019]\] \[[Bairamov and Bairamov 2022][research_bairamov_bairamov_2022]\] \[[Baker 1967][research_baker_1967]\] \[[Baker 1968][research_baker_1968]\] \[[Balepin 2006][research_balepin_2006]\] \[[Banerjee and Utreja 1975][research_banerjee_utreja_1975]\] \[[Baum and Levine 1984][research_baum_levine_1984]\] \[[Bazarov 1994][research_bazarov_1994]\] \[[Bazarov 1998][research_bazarov_1998]\] \[[Bellows et al 1984][research_bellows_brewster_1984]\] \[[Beltran and Kosvic 1966][research_beltran_kosvic_1966]\] \[[Benditt 1963][research_benditt_1963]\] \[[Benjamin and McConnaughey 1991][research_benjamin_mcconnaughey_1991]\] \[[Bentsman et al 1991][research_bentsman_wilcutts_1991]\] \[[Bergstrom and Raghunathan 1972][research_bergstrom_raghunathan_1972]\] \[[Bermudez 2024][research_bermudez_2024]\] \[[Biao et al 2024][research_biao_changlin_2024]\] \[[Blaha 1969][research_blaha_1969]\] \[[Bosson et al 1993][research_bosson_caisso_1993]\] \[[Bower and Thomas 2018][research_bower_thomas_2018]\] \[[Bowers 1980][research_bowers_1980]\] \[[Bowman 1967][research_bowman_1967]\] \[[Bradley et al 2018][research_bradley_sharp_2018]\] \[[Brazzel 1963][research_brazzel_1963]\] \[[Breshears et al 1966][research_breshears_mccafferty_1966]\] \[[Breshears et al 1967][research_breshears_mccafferty_1967]\] \[[Brodsky 1970][research_brodsky_1970]\] \[[Brown 2022][research_brown_2022]\] \[[Brownlee 1963][research_brownlee_1963]\] \[[Buckmann et al 1989][research_buckmann_shimp_1989]\] \[[Buckmann et al 1992][research_buckmann_shrimp_1992]\] \[[Burdett 1946][research_burdett_1946]\] \[[Burdett 1947][research_burdett_1947]\] \[[Burstein et al 1972][research_burstein_chinitz_1972]\] \[[Burton et al 2007][research_burton_loth_2007]\] \[[Buschulte 1970][research_buschulte_1970]\] \[[Buschulte 1971][research_buschulte_1971]\] \[[Cai et al 2005][research_cai_tong_2005]\] \[[Carman 1970][research_carman_1970]\] \[[Chandler 2023][research_chandler_2023]\] \[[Chandler 2024][research_chandler_2024]\] \[[Chandler and Herrera 2025][research_chandler_herrera_2025]\] \[[Chandler et al 2026][research_chandler_herrera_2026]\] \[[Chehroudi 2009][research_chehroudi_2009]\] \[[Chehroudi 2010][research_chehroudi_2010]\] \[[Chen and Zhao 2005][research_chen_zhao_2005]\] \[[Cheng 1956][research_cheng_1956]\] \[[Cheng 1985][research_cheng_1985]\] \[[Cheng and Farmer 2002][research_cheng_farmer_2002]\] \[[Cheng et al 2016][research_cheng_li_2016]\] \[[Cheng et al 2018][research_cheng_li_2018]\] \[[Chew 1973][research_chew_1973]\] \[[Chiaverini et al 2002][research_chiaverini_malecki_2002]\] \[[Childs 1974][research_childs_1974]\] \[[Childs and Moyer 1985][research_childs_moyer_1985]\] \[[Chiu 1987][research_chiu_1987]\] \[[Cho et al 2004][research_cho_kim_2004]\] \[[Chu and Xu 2014][research_chu_xu_2014]\] \[[Clark 1967][research_clark_1967]\] \[[Collins et al 1990][research_collins_martinez_1990]\] \[[Combustion Characteristics of Fuel-rich 2005][research_combustion_characteristics_2005]\] \[[Combustion Instability Analysis Numerical 1995][research_combustion_instability_1995]\] \[[Combustion Instability and Transient 2007][research_combustion_instability_2007]\] \[[Contreras et al 2026][research_contreras_fontanetta_2026]\] \[[Coogan 2015][research_coogan_2015]\] \[[Cosens and Newton 1988][research_cosens_newton_1988]\] \[[Crocco 1951][research_crocco_1951]\] \[[Crocco 1952][research_crocco_1952]\] \[[Crocco 1965][research_crocco_1965]\] \[[Crocco and Cheng 1953][research_crocco_cheng_1953]\] \[[Crocco et al 1960][research_crocco_grey_1960]\] \[[Crocco et al 1962][research_crocco_harrje_1962]\] \[[Crown and Heybey 1950][research_crown_heybey_1950]\] \[[Daidzic et al 1991][research_daidzic_tropea_1991]\] \[[Delcher et al 1989][research_delcher_dergevorkian_1989]\] \[[Demiyanenko et al 2004][research_demiyanenko_dmitrenko_2004]\] \[[Demjanenko et al 2003][research_demjanenko_dmitrenko_2003]\] \[[Design of Turbopump Propellant 1992][research_design_of_1992]\] \[[Development of a Software 2008][research_development_of_2008]\] \[[Dolgih 2025][research_dolgih_2025]\] \[[Donahue 2004][research_donahue_2004]\] \[[Dorosh and Leontiev 2014][research_dorosh_leontiev_2014]\] \[[Dresia et al 2023][research_dresia_adler_2023]\] \[[Dressler 2006][research_dressler_2006]\] \[[Du 2017][research_du_2017]\] \[[Du et al 2026][research_du_he_2026]\] \[[Dubois and Habiballah 1991][research_dubois_habiballah_1991]\] \[[Dubois et al 1995][research_dubois_habiballah_1995]\] \[[Dukeman 2002][research_dukeman_2002]\] \[[Eaton and Graefe 1952][research_eaton_graefe_1952]\] \[[Eberhart et al 2012][research_eberhart_lineberry_2012]\] \[[Ekimogloy et al 2026][research_ekimogloy_stelk_2026]\] \[[Ellerbrock and Ziegenhagen 2006][research_ellerbrock_ziegenhagen_2006]\] \[[Farvin and Peddieson 1988][research_farvin_peddieson_1988]\] \[[Fatuev 2006][research_fatuev_2006]\] \[[Feng et al 2009][research_feng_cheng_2009]\] \[[Fidler and Hays 2026][research_fidler_hays_2026]\] \[[Fidler et al 2025][research_fidler_jenkins_2025]\] \[[Filimonov 1968][research_filimonov_1968]\] \[[Filin and Mkrtchyan 2021][research_filin_mkrtchyan_2021]\] \[[Finseth 1991][research_finseth_1991]\] \[[Flandro et al 2004][research_flandro_sims_2004]\] \[[Flandro et al 2004][research_flandro_sims_2004_b]\] \[[France's Liquid Propellant Rocket-Engine 2006][research_france_s_liquid_2006]\] \[[Friedland 1965][research_friedland_1965]\] \[[Friedman and Bhat 1986][research_friedman_bhat_1986]\] \[[Fundamental Mechanisms of Combustion 1995][research_fundamental_mechanisms_1995]\] \[[Furst 1973][research_furst_1973]\] \[[Furst 1975][research_furst_1975]\] \[[Galli][research_galli]\] \[[Ganesan et al 2025][research_ganesan_subburayan_2025]\] \[[Gardner 1951][research_gardner_1951]\] \[[Gemranova 2021][research_gemranova_2021]\] \[[Giuliano et al 2010][research_giuliano_leonard_2010]\] \[[Goertz 1995][research_goertz_1995]\] \[[Gomet et al 2014][research_gomet_robin_2014]\] \[[Gotsulenko and Gotsulenko 2013][research_gotsulenko_gotsulenko_2013]\] \[[Graefe and Gordon 1957][research_graefe_gordon_1957]\] \[[Greatrix 2018][research_greatrix_2018]\] \[[Greatrix 2021][research_greatrix_2021]\] \[[Greenwood et al 1970][research_greenwood_prozan_1970]\] \[[Grenda et al 1991][research_grenda_venkateswaran_1991]\] \[[Grey 1953][research_grey_1953]\] \[[Grey 1954][research_grey_1954]\] \[[Gribben et al 1998][research_gribben_driscoll_1998]\] \[[Gromski et al 2010][research_gromski_majamaki_2010]\] \[[Grosdemange and Schaeffer 1990][research_grosdemange_schaeffer_1990]\] \[[Gulczyński et al 2024][research_gulczynski_hahn_2024]\] \[[Guo et al 2022][research_guo_xu_2022]\] \[[Gurov 2001][research_gurov_2001]\] \[[Gut et al 2025][research_gut_parzybut_2025]\] \[[Haga 2024][research_haga_2024]\] \[[Hakim et al 2020][research_hakim_tahdi_2020]\] \[[Ham-Battista et al 1993][research_hambattista_helmick_1993]\] \[[Hampson 1984][research_hampson_1984]\] \[[Hardgrove and Krieg 1984][research_hardgrove_kriegjr_1984]\] \[[Harper 1969][research_harper_1969]\] \[[Harrje 1959][research_harrje_1959]\] \[[Harvey 1970][research_harvey_1970]\] \[[Heister 2008][research_heister_2008]\] \[[Henson and Robertson 1962][research_henson_robertson_1962]\] \[[Hiraki et al 2019][research_hiraki_inoue_2019]\] \[[Hollinger 1965][research_hollinger_1965]\] \[[Hong et al 2009][research_hong_kim_2009]\] \[[Hou et al 2018][research_hou_fu_2018]\] \[[Hu et al 2026][research_hu_he_2026]\] \[[Huang 2000][research_huang_2000]\] \[[Huang 2002][research_huang_2002]\] \[[Huang 2002][research_huang_2002_b]\] \[[Huang et al 2000][research_huang_zhou_2000]\] \[[Huang et al 2000][research_huang_zhou_2000_b]\] \[[Huang et al 2024][research_huang_cheng_2024]\] \[[Huang et al 2024][research_huang_cheng_2024_b]\] \[[Hulka 2008][research_hulka_2008]\] \[[Hussein et al 2026][research_hussein_etzenbach_2026]\] \[[Hyde and Argueta 2025][research_hyde_argueta_2025]\] \[[Il'Yashenko 1963][research_ilyashenko_1963]\] \[[Instability Phenomenology and Case 1995][research_instability_phenomenology_1995]\] \[[Instability Phenomenology and Case 1995][research_instability_phenomenology_1995_b]\] \[[Instability Phenomenology and Case 1995][research_instability_phenomenology_1995_c]\] \[[Instability Phenomenology and Case 1995][research_instability_phenomenology_1995_d]\] \[[Instrumentation For Research On 1960][research_instrumentation_for_1960]\] \[[Integrated Thermal Monitoring for 2025][research_integrated_thermal_2025]\] \[[Ivanov 2021][research_ivanov_2021]\] \[[Ivanov and Borisov 2014][research_ivanov_borisov_2014]\] \[[Jacob and George 2024][research_jacob_george_2024]\] \[[Jacob et al 2010][research_jacob_flandro_2010]\] \[[James 1981][research_jamesjr_1981]\] \[[Japan's Liquid Propellant Rocket-Engine 2006][research_japan_s_liquid_2006]\] \[[Jayan and Raghunandan 2003][research_jayan_raghunandan_2003]\] \[[Jeng and Litchford 1991][research_jeng_litchford_1991]\] \[[Jensen 2005][research_jensen_2005]\] \[[Jeon and Park 2023][research_jeon_park_2023]\] \[[Jeon and Park 2026][research_jeon_park_2026]\] \[[Jeon et al 2004][research_jeon_lee_2004]\] \[[Jeon et al 2013][research_jeon_kwak_2013]\] \[[Jha 2024][research_jha_2024]\] \[[Jurado et al 1990][research_jurado_shade_1990]\] \[[Kachler and Beaurain 2005][research_kachler_beaurain_2005]\] \[[Kakudo et al 2021][research_kakudo_yokoyama_2021]\] \[[Kamijo 1983][research_kamijo_1983]\] \[[Kamijo et al 1981][research_kamijo_sogame_1981]\] \[[Kamijo et al 1982][research_kamijo_sogame_1982]\] \[[Kanda 2013][research_kanda_2013]\] \[[Kanda 2019][research_kanda_2019]\] \[[Kanda et al 2021][research_kanda_kikuchi_2021]\] \[[Kanda et al 2023][research_kanda_mishina_2023]\] \[[Karlgaard et al 2018][research_karlgaard_tynis_2018]\] \[[Karlgaard et al 2019][research_karlgaard_tynis_2019]\] \[[Kenzakowski et al 1997][research_kenzakowski_york_1997]\] \[[Khan and Qamar 2020][research_khan_qamar_2020]\] \[[Khan and Qamar 2020][research_khan_qamar_2020_b]\] \[[Kim et al 1992][research_kim_chen_1992]\] \[[Kim et al 2004][research_kim_chung_2004]\] \[[Kimura et al 2010][research_kimura_sato_2010]\] \[[Kiris et al 2000][research_kiris_dochankwak_2000]\] \[[Kishimoto et al 2022][research_kishimoto_morita_2022]\] \[[Kobayashi et al 2011][research_kobayashi_daimon_2011]\] \[[Kosykh 2025][research_kosykh_2025]\] \[[Kosykh 2026][research_kosykh_2026]\] \[[Kumar et al 2025][research_kumar_rallapalli_2025]\] \[[Kwon et al 2004][research_kwon_lee_2004]\] \[[Kyzmenko and Yakovlev 2018][research_kyzmenko_yakovlev_2018]\] \[[Lacefield and Sprow 1994][research_lacefield_sprow_1994]\] \[[Lafont and Bosson 1983][research_lafont_bosson_1983]\] \[[Latvala and Anderson 1959][research_latvala_anderson_1959]\] \[[Lee et al 2021][research_lee_han_2021]\] \[[Leto et al 2016][research_leto_votta_2016]\] \[[Levine 1965][research_levine_1965]\] \[[Li et al 2026][research_li_ganippa_2026]\] \[[Li et al 2026][research_li_ganippa_2026_b]\] \[[Lim et al 2020][research_lim_kim_2020]\] \[[Limerick 1991][research_limerick_1991]\] \[[Lin et al 1993][research_lin_chan_1993]\] \[[Liquid Oxygen Test of 2009][research_liquid_oxygen_2009]\] \[[Liquid Propellant Rocket-Engine Organizations 2006][research_liquid_propellant_2006]\] \[[Liquid Rocket Engine Combustion 1995][research_liquid_rocket_1995]\] \[[Liquid Rocket Engine Reliability][research_liquid_rocket]\] \[[Liquid Rocket Engine Thrust 2018][research_liquid_rocket_2018]\] \[[Liu et al 1995][research_liu_wang_1995]\] \[[Liu et al 2023][research_liu_liu_2023]\] \[[Liu et al 2024][research_liu_liu_2024]\] \[[Lores and Zinn 1973][research_lores_zinn_1973]\] \[[Low Frequency Oscillations in 2008][research_low_frequency_2008]\] \[[Lukashevich et al 2023][research_lukashevich_morozov_2023]\] \[[Lurui Xia et al 2008][research_luruixia_niaoqinghu_2008]\] \[[Muthaiah et al 2023][research_m_saini_2023]\] \[[Majumder 2019][research_majumder_2019]\] \[[Martin 2007][research_martin_2007]\] \[[Martinez et al 1990][research_martinez_reinert_1990]\] \[[Matthews 1957][research_matthews_1957]\] \[[Maxwell and Jacocks 1962][research_maxwell_jacocks_1962]\] \[[Mayer and Kruelle 1992][research_mayer_kruelle_1992]\] \[[McAmis et al 1992][research_mcamis_lankford_1992]\] \[[Kenna et al 1964][research_mckenna_walker_1964]\] \[[Meisl 1986][research_meisl_1986]\] \[[Mikhail 1979][research_mikhail_1979]\] \[[Ming et al 2016][research_ming_bingjun_2016]\] \[[Mishina et al 2020][research_mishina_umeoka_2020]\] \[[Mitchell 1969][research_mitchell_1969]\] \[[Miura 2010][research_miura_2010]\] \[[Moger and Ramsay 1964][research_moger_ramsay_1964]\] \[[Mohammadi et al 2015][research_mohammadi_mehdi_2015]\] \[[Moore et al 2024][research_moore_morse_2024]\] \[[Morrisette and Goldberg 1978][research_morrisette_goldberg_1978]\] \[[Mukambetov and Borovik 2022][research_mukambetov_borovik_2022]\] \[[Multifractal Detrended Fluctuation Analysis 2023][research_multifractal_detrended_2023]\] \[[Murashkin et al 2020][research_murashkin_bruyaka_2020]\] \[[Murphy and Voss 1996][research_murphy_voss_1996]\] \[[Murzionak][research_murzionak]\] \[[Muthaiah et al 2025][research_muthaiah_saini_2025]\] \[[Müller et al 2021][research_muller_traudt_2021]\] \[[Nair and Vaidyanathan 2022][research_nair_vaidyanathan_2022]\] \[[Nam et al 2018][research_nam_moon_2018]\] \[[Nardi Rezende 2018][research_nardirezende_2018]\] \[[Stoltzfus and Benz 1986][research_turbopump_ignition_1986]\] \[[Sackheim et al 2005][research_throttleable_engine_2005]\] \[[Kenny et al 2006][research_injector_throttling_2006]\] \[[Giuliano et al 2007][research_cece_throttling_2007]\] \[[Casiano et al 2009][research_throttling_review_2009]\] \[[Betts and Frederick 2010][research_throttling_history_2010]\] \[[Nelson and Bresnahan 1983][research_nelson_bresnahan_1983]\] \[[Newell and Rajagopal 1993][research_newell_rajagopal_1993]\] \[[Nguyen and Sirignano 2018][research_nguyen_sirignano_2018]\] \[[Nguyen and Sirignano 2019][research_nguyen_sirignano_2019]\] \[[Nguyen et al 2017][research_nguyen_popov_2017]\] \[[Non-linear throttling analysis of 1999][research_non_linear_throttling_1999]\] \[[Numerical Method and Simulations 2016][research_numerical_method_2016]\] \[[Numerical Studies on the 2003][research_numerical_studies_2003]\] \[[Nusca 2007][research_nusca_2007]\] \[[Nusca 2008][research_nusca_2008]\] \[[Nusca 2010][research_nusca_2010]\] \[[Of current interest Liquid 1958][research_of_current_1958]\] \[[Oh et al 2024][research_oh_shin_2024]\] \[[Okayasu et al 1983][research_okayasu_higashino_1983]\] \[[Okayasu et al 2002][research_okayasu_ohta_2002]\] \[[Olejnik and Zalewski 2020][research_olejnik_zalewski_2020]\] \[[Optimal Design of Fuel-Rich 2004][research_optimal_design_2004]\] \[[Osherov and Natan 1999][research_osherov_natan_1999]\] \[[Otto and Flage 1960][research_otto_flage_1960]\] \[[Pages and Achipa 2026][research_pages_achipa_2026]\] \[[Palej and Palacz 2018][research_palej_palacz_2018]\] \[[Parate 2020][research_parate_2020]\] \[[Park and Ahn 2020][research_park_ahn_2020]\] \[[Park and Jeon 2024][research_park_jeon_2024]\] \[[Park et al 2024][research_park_lee_2024]\] \[[Parkinson et al 1995][research_parkinson_skorodelov_1995]\] \[[Pastuszko et al 2024][research_pastuszko_chauvo_2024]\] \[[Pempie and Vernin 2001][research_pempie_vernin_2001]\] \[[Perez et al 2024][research_perez_johns_2024]\] \[[Pervaiz et al 1994][research_pervaiz_erler_1994]\] \[[Pharokhipanah and Bouckenooghe 2024][research_pharokhipanah_bouckenooghe_2024]\] \[[Popov et al 2013][research_popov_sideris_2013]\] \[[Popov et al 2014][research_popov_sideris_2014]\] \[[Popov et al 2016][research_popov_sideris_2016]\] \[[Popov et al 2017][research_popov_sideris_2017]\] \[[Pressurization of Liquid Propellant 2019][research_pressurization_of_2019]\] \[[Price 1964][research_price_1964]\] \[[Price 1965][research_price_1965]\] \[[Price 1980][research_price_1980]\] \[[Price and Earl A. 1970][research_price_earla_1970]\] \[[Princeton Univ Nj 1952][research_princetonunivnj_1952]\] \[[Prokopenko 2026][research_prokopenko_2026]\] \[[Pustovyi 2026][research_pustovyi_2026]\] \[[Qi et al 2022][research_qi_cheng_2022]\] \[[Qin et al 2016][research_qin_zhang_2016]\] \[[Reardon 1997][research_reardon_1997]\] \[[Reardon et al 1964][research_reardon_crocco_1964]\] \[[Reubush and Mercer 1974][research_reubush_mercer_1974]\] \[[Rezende 2021][research_rezende_2021]\] \[[Rhee et al 2008][research_rhee_lee_2008]\] \[[Rice et al 2010][research_rice_flandro_2010]\] \[[Richecoeur et al 2008][research_richecoeur_ducruix_2008]\] \[[Rivard 1965][research_rivard_1965]\] \[[Rock and Habchi 1997][research_rock_habchi_1997]\] \[[Rocket-Powered Aircraft 2017][research_rocket_powered_aircraft_2017]\] \[[Rocketdyne Canoga Park Ca 1961][research_rocketdynecanogaparkca_1961]\] \[[Roland et al 2016][research_roland_edwards_2016]\] \[[Rollstin 1986][research_rollstin_1986]\] \[[Rotordynamic Analysis of a 2008][research_rotordynamic_analysis_2008]\] \[[Ruffin et al 2018][research_ruffin_barato_2018]\] \[[Ruffin et al 2019][research_ruffin_paccagnella_2019]\] \[[Ruffin et al 2022][research_ruffin_paccagnella_2022]\] \[[Ruth et al 1990][research_ruth_ahn_1990]\] \[[Ryan 1966][research_ryan_1966]\] \[[Ryazantsev et al 2026][research_ryazantsev_lomakin_2026]\] \[[Sakaki et al 2015][research_sakaki_kakudo_2015]\] \[[Sakaki et al 2016][research_sakaki_kakudo_2016]\] \[[Sakaki et al 2018][research_sakaki_funahashi_2018]\] \[[Santiago 1996][research_santiago_1996]\] \[[Sarotte][research_sarotte]\] \[[Savkovic 2008][research_savkovic_2008]\] \[[Schallhorn et al 1998][research_schallhorn_majumdar_1998]\] \[[Schoenman 1984][research_schoenman_1984]\] \[[Scott 1963][research_scott_1963]\] \[[Senchev et al 2022][research_senchev_zubrilin_2022]\] \[[Seo et al 2018][research_seo_cho_2018]\] \[[Seshime et al 2026][research_seshime_haga_2026]\] \[[Sexsmith et al 2025][research_sexsmith_clay_2025]\] \[[Shelley et al 2001][research_shelley_leclaire_2001]\] \[[Shi et al 2023][research_shi_zi_2023]\] \[[Shimizu et al 2008][research_shimizu_mizobuchi_2008]\] \[[Shimura and Kamijo 1985][research_shimura_kamijo_1985]\] \[[Shoyama et al 2024][research_shoyama_wada_2024]\] \[[Sibanda 2023][research_sibanda_2023]\] \[[Siebenhaar and Campbell 1987][research_siebenhaar_campbell_1987]\] \[[Sirignano and Popov 2013][research_sirignano_popov_2013]\] \[[Smith 1964][research_smith_1964]\] \[[Solid Rocket Combustion Instability-An 1992][research_solid_rocket_1992]\] \[[Son et al 2012][research_son_koo_2012]\] \[[Sonneveldt et al 2019][research_sonneveldt_clark_2019]\] \[[Souverein et al 2019][research_souverein_maeding_2019]\] \[[Special Features of Antiaircraft 2010][research_special_features_2010]\] \[[Stability Testing Methodology Scaling 1995][research_stability_testing_1995]\] \[[Steppert and Epple 2017][research_steppert_epple_2017]\] \[[Stillwell and Larson 1960][research_stillwell_larson_1960]\] \[[Stillwell and Larson 1960][research_stillwell_larson_1960_b]\] \[[Strietzel and Shefler 1963][research_strietzel_shefler_1963]\] \[[Strome 1969][research_strome_1969]\] \[[Stuber et al 2012][research_stuber_prasadh_2012]\] \[[Summerfield 1951][research_summerfield_1951]\] \[[Summerfield 1960][research_summerfield_1960]\] \[[Sutton 1970][research_sutton_1970]\] \[[Takada et al 2009][research_takada_kikuchi_2009]\] \[[Tan and Wang 2024][research_tan_wang_2024]\] \[[Tani et al 2010][research_tani_shimiya_2010]\] \[[Tao et al 2006][research_tao_jiping_2006]\] \[[Tobey and Bastress 1966][research_tobey_bastress_1966]\] \[[Torres Zanardi et al 2019][research_torreszanardi_bacchi_2019]\] \[[Tucker et al 1993][research_tucker_dehoff_1993]\] \[[Twardy 1975][research_twardy_1975]\] \[[Tyurenkova et al 2024][research_tyurenkova_smirnova_2024]\] \[[Umeoka et al 2021][research_umeoka_mishina_2021]\] \[[Urbano et al 2016][research_urbano_selle_2016]\] \[[Vadera 2019][research_vadera_2019]\] \[[Van Hooser et al 1999][research_vanhooser_bailey_1999]\] \[[Venkateswaran et al 1991][research_venkateswaran_grenda_1991]\] \[[Ventrice et al 1979][research_ventrice_fang_1979]\] \[[Ventrice et al 1979][research_ventrice_fang_1979_b]\] \[[Vernacchia et al 2022][research_vernacchia_2022]\] \[[Waesche and Summerfield 1965][research_waesche_summerfield_1965]\] \[[Walsh and Jacoby 1972][research_walsh_jacoby_1972]\] \[[Wang 2019][research_wang_2019_b]\] \[[Wang et al 2000][research_wang_zhou_2000]\] \[[Wang et al 2022][research_wang_li_2022_c]\] \[[Wang et al 2025][research_wang_kim_2025]\] \[[Whitmore et al 2015][research_whitmore_merkley_2015]\] \[[Williams 2004][research_williams_2004]\] \[[Williams 2004][research_williams_2004_b]\] \[[Xiong et al 2022][research_xiong_liu_2022]\] \[[Xiong et al 2020][research_xiong_morgan_2020]\] \[[Xiong et al 2024][research_xiong_liu_2024]\] \[[Yang 2004][research_yang_2004]\] \[[Yang and Sun 2012][research_yang_sun_2012]\] \[[Yang et al 2019][research_yang_li_2019]\] \[[Yoon and Moon 2026][research_yoon_moon_2026]\] \[[Yoon et al 2013][research_yoon_jeon_2013]\] \[[Yu et al 2025][research_yu_yang_2025]\] \[[Yuhui and Zhenguo 2002][research_yuhui_zhenguo_2002]\] \[[Yuwei et al 2024][research_yuwei_wu_2024]\] \[[Zapata Usandivaras][research_zapatausandivaras]\] \[[Zapata Usandivaras et al 2024][research_zapatausandivaras_bauerheim_2024]\] \[[Zhang 2016][research_zhang_2016]\] \[[Zhang and Li 2017][research_zhang_li_2017]\] \[[Zhang et al 2026][research_zhang_zhao_2026]\] \[[Zhang et al 2012][research_zhang_ga_2012]\] \[[Zhang et al 2025][research_zhang_li_2025]\] \[[Zhang et al 2025][research_zhang_zhang_2025]\] \[[Zhang et al 2026][research_zhang_zhang_2026]\] \[[Zhao et al 2011][research_zhao_yu_2011]\] \[[Zhao et al 2022][research_zhao_cai_2022]\] \[[Zhou et al 2022][research_zhou_chen_2022]\] \[[Zhou et al 2026][research_zhou_dong_2026]\] \[[Zhu et al 2025][research_zhu_wang_2025]\] \[[Zhuang et al 1998][research_zhuang_nie_1998]\] \[[Zhuang et al 1999][research_zhuang_nie_1999]\] \[[Zinn 1968][research_zinn_1968]\] \[[Zinn and Powell 1971][research_zinn_powell_1971]\] \[[Zinn and Savell 1969][research_zinn_savell_1969]\] \[[Zook 2024][research_zook_2024]\] \[[Zubanov and Shabliy 2014][research_zubanov_shabliy_2014]\] \[[Zuev et al 2020][research_zuev_arngold_2020]\]

### Aeroelasticity, flutter and control effectiveness

**The thin structure in the airstream.** Static aeroelasticity and divergence, aileron effectiveness and reversal, wing flutter, and the flutter of skin panels. **Panel flutter is the largest single subject here, with 108 titles**, and it is the aeroelastic problem of a thin skin at supersonic speed, which is the structure the X-2 flew.

**416 records.** \[[Aerodynamic and Static Aeroelastic 2014][research_aerodynamic_and_2014]\] \[[Aeroelastic Tests of an 1963][research_aeroelastic_tests_1963]\] \[[Ahmad et al 2014][research_ahmad_rahman_2014]\] \[[Akaydin et al 2015][research_akaydin_moiniyekta_2015]\] \[[Alder 2014][research_alder_2014]\] \[[Alder 2015][research_alder_2015]\] \[[Alighanbari 2002][research_alighanbari_2002]\] \[[Alsaif et al 2015][research_alsaif_foda_2015]\] \[[Aly et al 2002][research_aly_ogot_2002]\] \[[Alyanak and Pendleton 2014][research_alyanak_pendleton_2014]\] \[[Alyanak and Pendleton 2017][research_alyanak_pendleton_2017]\] \[[Amendola et al 2018][research_amendola_dimino_2018]\] \[[Amirzadegan 2026][research_amirzadegan_2026]\] \[[An Aeroelastic Metamodel Based 2013][research_an_aeroelastic_2013]\] \[[Anderson 1965][research_anderson_1965]\] \[[Arnold 1942][research_arnold_1942]\] \[[Atik et al 2012][research_atik_baran_2012]\] \[[Awadalla Ali Haj Ahmed 2024][research_awadallaalihajahmed_2024]\] \[[Azzouz et al 2011][research_azzouz_smith_2011]\] \[[Babister 1980][research_babister_1980_b]\] \[[Badiei et al 2014][research_badiei_sadr_2014]\] \[[Bae et al 2005][research_bae_seigler_2005]\] \[[Bai et al 2022][research_bai_cao_2022]\] \[[Barr 1971][research_barr_1971]\] \[[Barthelemy and Bergen 1988][research_barthelemy_bergen_1988]\] \[[Barthelemy and Bergen 1989][research_barthelemy_bergen_1989]\] \[[Beldica et al 2001][research_beldica_hilton_2001]\] \[[Beran et al 2005][research_beran_hur_2005]\] \[[Berci 2017][research_berci_2017]\] \[[Bhatia and Beran 2017][research_bhatia_beran_2017]\] \[[Bi et al 2017][research_bi_xie_2017]\] \[[Birman 1989][research_birman_1989]\] \[[Bismarck-Nasr 1993][research_bismarcknasr_1993]\] \[[Blair and Weisshaar 1982][research_blair_weisshaar_1982]\] \[[Bochkarev and Matveyenko 2008][research_bochkarev_matveyenko_2008]\] \[[Boehm et al 2001][research_boehm_flick_2001]\] \[[Bohlmann et al 1990][research_bohlmann_eckstrom_1990]\] \[[Bohon and Dixon 1964][research_bohon_dixon_1964]\] \[[Bond et al 2008][research_bond_canfield_2008]\] \[[Boyd 1977][research_boyd_1977]\] \[[Boyer et al 2016][research_boyer_mcnamara_2016]\] \[[Buddhamatya et al 2026][research_buddhamatya_miranda_2026]\] \[[Bugała 2025][research_bugala_2025]\] \[[Bugała and Payenskyy 2025][research_bugala_payenskyy_2025]\] \[[Bugała et al 2023][research_bugala_sznajder_2023]\] \[[Burkhart 1980][research_burkhart_1980]\] \[[Böhnisch et al 2026][research_bohnisch_braun_2026]\] \[[Calligeros and Dugundji 1963][research_calligeros_dugundji_1963]\] \[[Candida et al 2019][research_candida_souzadepaula_2019]\] \[[Carr 1982][research_carr_1982]\] \[[Carrera et al 2013][research_carrera_varello_2013]\] \[[Carter and Stearman 1967][research_carter_stearman_1967]\] \[[Carter and Stearman 1968][research_carter_stearman_1968]\] \[[Cella and Biancolini 2012][research_cella_biancolini_2012]\] \[[Chandiramani et al 1995][research_chandiramani_plaut_1995]\] \[[Chaussee and Enriquez 2026][research_chaussee_enriquez_2026]\] \[[Chen et al 1998][research_chen_chang_1998]\] \[[Cho and Chang 2001][research_cho_chang_2001]\] \[[Choi et al 2020][research_choi_lim_2020]\] \[[Chopra 1975][research_chopra_1975]\] \[[Chuban 2020][research_chuban_2020]\] \[[Clarke et al 2005][research_clarke_allen_2005]\] \[[Cole 1990][research_cole_1990]\] \[[Collar 1946][research_collar_1946]\] \[[Craig and Erbug 1976][research_craig_erbug_1976]\] \[[Craig 1971][research_craigjr_1971]\] \[[Cunningham 2017][research_cunningham_2017]\] \[[Currao and Yeh 2026][research_currao_yeh_2026]\] \[[Das et al 2021][research_das_venkatraman_2021]\] \[[Davis and Bendiksen 1993][research_davis_bendiksen_1993]\] \[[de Melo et al 2024][research_demelo_bussamra_2024]\] \[[Deere et al 2024][research_deere_viken_2024]\] \[[Dillinger et al 2019][research_dillinger_abdalla_2019]\] \[[Dixon and Mei 1993][research_dixon_mei_1993]\] \[[Doengi et al 1995][research_doengi_dinkler_1995]\] \[[Dogan Kuzey and Yıldırım Dalkıran 2026][research_dogankuzey_yildirimdalkiran_2026]\] \[[Doggett and Soistmann 1989][research_doggettjr_soistmann_1989]\] \[[Dongi et al 1996][research_dongi_dinkler_1996]\] \[[Dowell 1964][research_dowell_1964]\] \[[Dowell 1964][research_dowell_1964_b]\] \[[Dowell 1970][research_dowell_1970]\] \[[Dowell 1970][research_dowell_1970_b]\] \[[Dowell 1972][research_dowell_1972]\] \[[Dowell 1983][research_dowell_1983]\] \[[Dowell 1996][research_dowell_1996]\] \[[Dowell 1999][research_dowell_1999]\] \[[Dowell and Bendiksen 2010][research_dowell_bendiksen_2010]\] \[[Dowell and Voss 1964][research_dowell_voss_1964]\] \[[Dowell et al 1990][research_dowell_katz_1990]\] \[[Dugundji 1965][research_dugundji_1965]\] \[[Dugundji 1966][research_dugundji_1966]\] \[[Edwards 1992][research_edwards_1992]\] \[[Ehlers and Weisshaar 1993][research_ehlers_weisshaar_1993]\] \[[Ellen 1969][research_ellen_1969]\] \[[Elshazly et al 2025][research_elshazly_kassem_2025]\] \[[Epstein et al 1994][research_epstein_srinivasan_1994]\] \[[Evensen 1976][research_evensen_1976]\] \[[Farhat 2001][research_farhat_2001]\] \[[Faroughi et al 2012][research_faroughi_malekzadeh_2012]\] \[[Feldwisch and Schulze 2021][research_feldwisch_schulze_2021]\] \[[Filippou et al 2024][research_filippou_kilimtzidis_2024]\] \[[Firouz-Abadi et al 2013][research_firouzabadi_askarian_2013]\] \[[Flax 1977][research_flax_1977]\] \[[Forster et al 1996][research_forster_kolonay_1996]\] \[[French et al 1988][research_french_noll_1988]\] \[[Fung 1958][research_fung_1958]\] \[[Fung 1963][research_fung_1963]\] \[[Furuya and Fukuchi 2001][research_furuya_fukuchi_2001]\] \[[Försching 2004][research_forsching_2004]\] \[[Försching and Senft 1991][research_forsching_senft_1991]\] \[[Gao et al 2011][research_gao_yang_2011]\] \[[Garcia and Guruswamy 1999][research_garcia_guruswamy_1999]\] \[[Garrick and Reed 1981][research_garrick_reed_1981]\] \[[Gaspers 1972][research_gaspersjr_1972]\] \[[Gee 2000][research_gee_2000]\] \[[Gee and Sipcic 1999][research_gee_sipcic_1999]\] \[[Ghalandari et al 2022][research_ghalandari_mahariq_2022]\] \[[Gilbert et al 1984][research_gilbert_schmidt_1984]\] \[[Goland 1952][research_goland_1952]\] \[[Goldstein 1975][research_goldstein_1975]\] \[[Gordnier and Visbal 2000][research_gordnier_visbal_2000]\] \[[Gordnier and Visbal 2001][research_gordnier_visbal_2001]\] \[[Gordnier and Visbal 2003][research_gordnier_visbal_2003]\] \[[Green and Fernandez 1994][research_green_fernandez_1994]\] \[[Grohmann et al 1999][research_grohmann_kroplin_1999]\] \[[Grosser 1965][research_grosser_1965]\] \[[Gu et al 2024][research_gu_healy_2024]\] \[[Guimarães et al 2020][research_guimaraes_rade_2020]\] \[[Guo and Mei][research_guo_mei]\] \[[Guo et al 2022][research_guo_zhang_2022]\] \[[Gwin 1974][research_gwin_1974]\] \[[Haas and Chopra 1987][research_haas_chopra_1987]\] \[[Hajela and Glowasky 1991][research_hajela_glowasky_1991]\] \[[Han and Yang 1983][research_han_yang_1983]\] \[[Hashimoto et al 2003][research_hashimoto_menshov_2003]\] \[[Hashimoto et al 2009][research_hashimoto_aoyama_2009]\] \[[Hassan 1994][research_hassan_1994]\] \[[He et al 2020][research_he_song_2020]\] \[[He et al 2021][research_he_wang_2021]\] \[[Hemmig et al 1980][research_hemmig_venkayya_1980]\] \[[Hilger and Ritter 2021][research_hilger_ritter_2021]\] \[[Hopkins and Dowell 1994][research_hopkins_dowell_1994]\] \[[Hou and Satyanarayana 2000][research_hou_satyanarayana_2000]\] \[[Hubbard et al 2014][research_hubbard_fontenot_2014]\] \[[Hwu and Tsai 2002][research_hwu_tsai_2002]\] \[[Ibrahim 1989][research_ibrahim_1989]\] \[[Ibrahim 1990][research_ibrahim_1990]\] \[[Ibrahim et al 2004][research_ibrahim_beloiu_2004]\] \[[Ide and Ominsky 1990][research_ide_ominsky_1990]\] \[[Isogai 2013][research_isogai_2013]\] \[[Izadpanahi][research_izadpanahi]\] \[[Izadpanahi and Mardanpour 2018][research_izadpanahi_mardanpour_2018]\] \[[Pratheepan and Bruce Ralphin Rose 2015][research_j_j_2015]\] \[[Jegarkandi Mohsen et al 2009][research_jegarkandimohsen_nobariali_2009]\] \[[Jiang et al 2000][research_jiang_an_2000]\] \[[Johns 1958][research_johns_1958]\] \[[Johns 1960][research_johns_1960]\] \[[Jung and Reimerdes 2003][research_jung_reimerdes_2003]\] \[[Kariappa and Somashekar 1969][research_kariappa_somashekar_1969]\] \[[Karpel et al 2004][research_karpel_moulin_2004]\] \[[Karpouzian and Librescu 1992][research_karpouzian_librescu_1992]\] \[[Kawakami et al 2007][research_kawakami_takatoya_2007]\] \[[Kawakami et al 2008][research_kawakami_takatoya_2008]\] \[[Kayran 2004][research_kayran_2004]\] \[[Kenyon and Shinde 2025][research_kenyon_shinde_2025]\] \[[Kholodar 2023][research_kholodar_2023]\] \[[Kim and Kim 2015][research_kim_kim_2015_b]\] \[[Kim and Park 1999][research_kim_park_1999]\] \[[Kim and Song 2013][research_kim_song_2013]\] \[[Kodigaddi 2026][research_kodigaddi_2026]\] \[[Kolonay and Yang 1998][research_kolonay_yang_1998]\] \[[Koo 2001][research_koo_2001]\] \[[Koreanschi et al 2014][research_koreanschi_oliviu_2014]\] \[[Kornev et al 2021][research_kornev_ambrozhevich_2021]\] \[[Kouchakzadeh et al 2010][research_kouchakzadeh_rasekh_2010]\] \[[Krause and Dinkler 1998][research_krause_dinkler_1998]\] \[[Krüger et al 2014][research_kruger_klimmek_2014]\] \[[Kudryavtsev 2014][research_kudryavtsev_2014]\] \[[Kumar et al 2023][research_kumar_onkar_2023]\] \[[Kuo et al 1972][research_kuo_morino_1972]\] \[[Kurzin and Mazutskii 2013][research_kurzin_mazutskii_2013]\] \[[Körbahti and Uzal 2004][research_korbahti_uzal_2004]\] \[[Lagerstrom and Graham 1949][research_lagerstrom_graham_1949]\] \[[Lai et al 1995][research_lai_huang_1995]\] \[[Lee 1994][research_lee_1994_b]\] \[[Lee and Cho 1991][research_lee_cho_1991]\] \[[Lee et al 1990][research_lee_miura_1990]\] \[[Lee et al 1991][research_lee_miura_1991]\] \[[Lee et al 1994][research_lee_kim_1994]\] \[[Lemley 1968][research_lemley_1968]\] \[[Lesoinne 2007][research_lesoinne_2007]\] \[[Levy 1992][research_levy_1992]\] \[[Li et al 2010][research_li_zhang_2010]\] \[[Li et al 2013][research_li_yang_2013]\] \[[Librescu and Simovich 1988][research_librescu_simovich_1988]\] \[[Librescu and Thangjitham 1989][research_librescu_thangjitham_1989]\] \[[Librescu and Thangjitham 1991][research_librescu_thangjitham_1991]\] \[[Librescu et al 2004][research_librescu_marzocca_2004]\] \[[Lin 1999][research_lin_1999]\] \[[Liu et al 2011][research_liu_yin_2011]\] \[[Liu et al 2019][research_liu_cook_2019]\] \[[Livne 2023][research_livne_2023_b]\] \[[Livne and Mineau 1996][research_livne_mineau_1996]\] \[[Lottati 1985][research_lottati_1985]\] \[[Lyrio et al 2019][research_lyrio_azevedo_2019]\] \[[Ma et al 2017][research_ma_su_2017]\] \[[MacMurdy et al 1994][research_macmurdy_guruswamy_1994]\] \[[Mailybaev and Seiranyan 1998][research_mailybaev_seiranyan_1998]\] \[[Mao et al 2019][research_mao_xie_2019]\] \[[Mao et al 2023][research_mao_guo_2023]\] \[[Mardanpour et al 2013][research_mardanpour_richards_2013]\] \[[Mardanpour et al 2014][research_mardanpour_richards_2014]\] \[[Marzocca et al 2001][research_marzocca_librescu_2001]\] \[[McTavish][research_mctavish]\] \[[Mei 1977][research_mei_1977]\] \[[Mei 1978][research_mei_1978]\] \[[Mei et al 2012][research_mei_zhang_2012]\] \[[Melek and Kaya 2009][research_melek_kaya_2009]\] \[[Melville and Gordnier 1998][research_melville_gordnier_1998]\] \[[Melvin and Zhao 2024][research_melvin_zhao_2024]\] \[[Meng et al 2020][research_meng_kaihua_2020]\] \[[Menshchikov and Somov 2019][research_menshchikov_somov_2019]\] \[[Mikilyan 2024][research_mikilyan_2024]\] \[[Miles 1949][research_miles_1949]\] \[[Ming-de 1984][research_mingde_1984]\] \[[Mitrotta et al 2025][research_mitrotta_pirrera_2025]\] \[[Moon 2003][research_moon_2003]\] \[[Moon and Kim 2001][research_moon_kim_2001]\] \[[Morino 1969][research_morino_1969]\] \[[Moshtaghzadeh et al 2022][research_moshtaghzadeh_izadpanahi_2022]\] \[[Muhlstein 1966][research_muhlsteinjr_1966]\] \[[Munk 1950][research_munk_1950]\] \[[NACA Conference on Aircraft 1957][research_loads_flutter_conf_1957]\] \[[Naftaly and Raveh 2025][research_naftaly_raveh_2025]\] \[[Nakai et al 1967][research_nakai_takagi_1967]\] \[[A study of the 1973][research_oblique_wing_divergence_1973]\] \[[Weisshaar and Crittenden 1976][research_asymmetric_sweep_flutter_1976]\] \[[Bland 1980][research_fsw_airfoil_divergence_1980]\] \[[Ricketts and Doggett 1980][research_fsw_divergence_tunnel_1980]\] \[[Cole 1986][research_fsw_divergence_study_1986]\] \[[Schuster and Lokos 1988][research_fsw_flight_divergence_1988]\] \[[Newman III et al 1999][research_newmaniii_newman_1999]\] \[[Newton 1965][research_newton_1965]\] \[[Nguyen 2008][research_nguyen_2008]\] \[[Nguyen et al 2016][research_nguyen_ting_2016]\] \[[Nguyen et al 2017][research_nguyen_ting_2017]\] \[[Nieto Gómez and Chimeno Manguán 2025][research_nietogomez_chimenomanguan_2025]\] \[[Nikbay et al 2009][research_nikbay_oncu_2009]\] \[[Njuguna 2007][research_njuguna_2007]\] \[[Noll et al 1983][research_noll_eastep_1983]\] \[[Noll et al 1984][research_noll_eastep_1984]\] \[[Nonlinear panel flutter in 1991][research_nonlinear_panel_1991]\] \[[O'Donnell and Mohseni 2017][research_odonnell_mohseni_2017]\] \[[Olson 1967][research_olson_1967]\] \[[Ouyang et al 2021][research_ouyang_zeng_2021]\] \[[Oyibo 1984][research_oyibo_1984]\] \[[Ozcatalbas et al 2018][research_ozcatalbas_acar_2018]\] \[[Chiozzotto 2016][research_pchiozzotto_2016]\] \[[Palakurthy et al 2022][research_palakurthy_zope_2022]\] \[[Panel flutter in a 1991][research_panel_flutter_1991]\] \[[Pany 2023][research_pany_2023]\] \[[Parker et al 1991][research_parker_spain_1991]\] \[[Parks 1965][research_parks_1965]\] \[[Parks 1966][research_parks_1966]\] \[[Patil 2003][research_patil_2003]\] \[[Pecora and Pecora 2018][research_pecora_pecora_2018]\] \[[Perera and Guo 2008][research_perera_guo_2008]\] \[[Piccolo Serafim et al 2023][research_piccoloserafim_freydin_2023]\] \[[Pierson 1972][research_pierson_1972]\] \[[Pierson 1975][research_pierson_1975]\] \[[Pitcher and Maple 2008][research_pitcher_maple_2008]\] \[[Pitt 2004][research_pitt_2004]\] \[[Plath][research_plath]\] \[[Plaut 1968][research_plaut_1968]\] \[[Plaut 1971][research_plaut_1971]\] \[[Popescu 1999][research_popescu_1999]\] \[[Popescu 2000][research_popescu_2000]\] \[[Prakash et al 2023][research_prakash_ganapathi_2023]\] \[[Prathap 1978][research_prathap_1978]\] \[[Qiao et al 2018][research_qiao_zhou_2018]\] \[[Qiao et al 2019][research_qiao_zhou_2019]\] \[[Rajamurugu et al 2024][research_rajamurugu_satyam_2024]\] \[[Rajamurugu et al 2024][research_rajamurugu_satyam_2024_b]\] \[[Randels 1954][research_randels_1954]\] \[[Raveh and Levy 2004][research_raveh_levy_2004]\] \[[Razi and Ghadiri 2008][research_razi_ghadiri_2008]\] \[[Rea et al 2017][research_rea_pecora_2017]\] \[[Rea et al 2018][research_rea_pecora_2018]\] \[[Rehman 2022][research_rehman_2022]\] \[[Reich et al 2002][research_reich_raveh_2002]\] \[[Reimann et al 2026][research_reimann_franze_2026]\] \[[Reimer et al][research_reimer_braun]\] \[[Resende 1992][research_resende_1992]\] \[[Ribeiro et al 2022][research_ribeiro_casalino_2022]\] \[[Ribeiro et al 2022][research_ribeiro_casalino_2022_b]\] \[[Rimer et al 1983][research_rimer_chipman_1983]\] \[[Ritter et al 2017][research_ritter_dillinger_2017]\] \[[Ritter et al 2021][research_ritter_hilger_2021]\] \[[Ritter et al 2023][research_ritter_fehrs_2023]\] \[[Rocha Da Costa][research_rochadacosta]\] \[[Rodden 1964][research_rodden_1964]\] \[[Rodden 1989][research_rodden_1989]\] \[[Rodden 1989][research_rodden_1989_b]\] \[[Rongrong et al 2018][research_rongrong_zhengyin_2018]\] \[[Rosenberg 1944][research_rosenberg_1944]\] \[[Runyan et al 1970][research_runyan_forsberg_1970]\] \[[Rutkowski 1979][research_rutkowski_1979]\] \[[Sacchi et al 2026][research_sacchi_sneddon_2026]\] \[[Safronov et al 2023][research_safronov_semon_2023]\] \[[Sanghi et al 2020][research_sanghi_riso_2020]\] \[[Santos and Pegado 2019][research_santos_pegado_2019]\] \[[Sarma and Varadan 1988][research_sarma_varadan_1988]\] \[[Saunders 1963][research_saunders_1963]\] \[[Schewe and Mai 2018][research_schewe_mai_2018]\] \[[Schmidt 1991][research_schmidt_1991]\] \[[Scott and Weisshaar 1991][research_scott_weisshaar_1991]\] \[[Scott and Weisshaar 1994][research_scott_weisshaar_1994]\] \[[Seiner and Librescu 1983][research_seiner_librescu_1983]\] \[[Sergienko and Sergienko 1997][research_sergienko_sergienko_1997]\] \[[Shan et al 2019][research_shan_tian_2019]\] \[[Shanthakumar 1977][research_shanthakumar_1977]\] \[[Shinde et al 2018][research_shinde_mcnamara_2018]\] \[[Shinde et al 2019][research_shinde_mcnamara_2019]\] \[[Shishaeva and Vedeneev 2013][research_shishaeva_vedeneev_2013]\] \[[Shivaji et al 2025][research_shivaji_basavaraju_2025]\] \[[Silva][research_silva]\] \[[Silva][research_silva_b]\] \[[Sinay and Reiss 1981][research_sinay_reiss_1981]\] \[[Sotoudeh 2015][research_sotoudeh_2015]\] \[[Squires 2004][research_squires_2004]\] \[[Stanford 2016][research_stanford_2016]\] \[[Stanford and Beran 2011][research_stanford_beran_2011]\] \[[Static Aeroelasticity Effect 2014][research_static_aeroelasticity_2014]\] \[[Striz 1991][research_striz_1991]\] \[[Su et al 2018][research_su_wang_2018]\] \[[Suleman 2007][research_suleman_2007]\] \[[Suleman et al 2000][research_suleman_crawford_2000]\] \[[Suleman et al 2002][research_suleman_crawford_2002]\] \[[Sun 2024][research_sun_2024]\] \[[Sun et al 2024][research_sun_zhou_2024]\] \[[Syed et al 2022][research_syed_moshtaghzadeh_2022]\] \[[Tadi 2002][research_tadi_2002]\] \[[Tamura and Yumitori 2024][research_tamura_yumitori_2024]\] \[[Theodorsen 1935][research_theodorsen_1935]\] \[[Thomson 1946][research_thomson_1946]\] \[[Tian et al 2016][research_tian_yang_2016]\] \[[Ting et al 2014][research_ting_lebofsky_2014]\] \[[Ting et al 2014][research_ting_nguyen_2014]\] \[[Tizzi 1994][research_tizzi_1994]\] \[[Torrigiani and Berci 2021][research_torrigiani_berci_2021]\] \[[Triplett 1980][research_triplett_1980]\] \[[Tsushima et al 2019][research_tsushima_yokozeki_2019]\] \[[Udrescu 1998][research_udrescu_1998]\] \[[Varello et al 2013][research_varello_lamberti_2013]\] \[[Vedeneev 2012][research_vedeneev_2012]\] \[[Vedeneev 2013][research_vedeneev_2013]\] \[[Vindigni 2023][research_vindigni_2023]\] \[[Vindigni 2024][research_vindigni_2024]\] \[[Vindigni et al 2024][research_vindigni_mantegna_2024]\] \[[Voss et al 2026][research_voss_tang_2026]\] \[[Wan et al 2011][research_wan_zhang_2011]\] \[[Wang 2019][research_wang_2019]\] \[[Wang and Ma 2024][research_wang_ma_2024]\] \[[Wang et al 2018][research_wang_su_2018]\] \[[Wang et al 2021][research_wang_wu_2021]\] \[[Wang et al 2022][research_wang_li_2022]\] \[[Wansaseub et al 2020][research_wansaseub_sleesongsom_2020]\] \[[Weatherill and Zartarian 1958][research_weatherill_zartarian_1958]\] \[[Weisshaar 1977][research_weisshaar_1977]\] \[[Weisshaar 1978][research_weisshaar_1978]\] \[[Weisshaar 1979][research_weisshaar_1979]\] \[[Weisshaar 1980][research_weisshaar_1980]\] \[[Weisshaar 1981][research_weisshaar_1981]\] \[[Weisshaar 1985][research_weisshaar_1985]\] \[[Weisshaar 1990][research_weisshaar_1990]\] \[[Woo 1992][research_woo_1992]\] \[[Woods et al 1989][research_woods_gilbert_1989]\] \[[Woods et al 1990][research_woods_gilbert_1990]\] \[[Woodward 1956][research_woodward_1956]\] \[[Wooldridge 1960][research_wooldridge_1960]\] \[[Wunderlich and Dähne 2017][research_wunderlich_dahne_2017]\] \[[Wunderlich et al 2017][research_wunderlich_dahne_2017_b]\] \[[Xiao 2016][research_xiao_2016]\] \[[Xie et al 2007][research_xie_leng_2007]\] \[[Xie et al 2016][research_xie_liu_2016]\] \[[Xu and He 2019][research_xu_he_2019]\] \[[xu et al 2023][research_xu_song_2023]\] \[[Xue and Mei 1992][research_xue_mei_1992]\] \[[Xue and Mei 1993][research_xue_mei_1993]\] \[[Xue et al 1990][research_xue_mei_1990]\] \[[Xue et al 2019][research_xue_ye_2019]\] \[[Yang et al 2003][research_yang_obayashi_2003]\] \[[Yang et al 2009][research_yang_chen_2009]\] \[[Yang et al 2012][research_yang_yang_2012]\] \[[Yates 1963][research_yates_1963]\] \[[Ye and Ye 2021][research_ye_ye_2021]\] \[[Yi et al 2015][research_yi_jun_2015]\] \[[Yilmaz and Kayran 2024][research_yilmaz_kayran_2024]\] \[[Yu and Hornung 2026][research_yu_hornung_2026]\] \[[Yu et al 2014][research_yu_lv_2014]\] \[[Zeiler 1999][research_zeiler_1999]\] \[[Zhang et al 2016][research_zhang_yang_2016]\] \[[Zhang et al 2018][research_zhang_lv_2018]\] \[[Zhang et al 2018][research_zhang_zhou_2018]\] \[[Zhang et al 2018][research_zhang_zhou_2018_b]\] \[[Zhang et al 2021][research_zhang_guo_2021]\] \[[Zhang JunHong et al 2010][research_zhangjunhong_hanjinglong_2010]\] \[[Zhao and Cao 2015][research_zhao_cao_2015]\] \[[Zhao and Kapania 2017][research_zhao_kapania_2017]\] \[[Zhao et al 2020][research_zhao_he_2020]\] \[[Zhou 1995][research_zhou_1995]\] \[[Zhou and Yang 2013][research_zhou_yang_2013]\] \[[Zhou et al 2022][research_zhou_wang_2022]\] \[[Zhou et al 2024][research_zhou_nie_2024]\] \[[Zhu and Breuer 2022][research_zhu_breuer_2022]\] \[[Zimmerman and Weissenburger 1964][research_zimmerman_weissenburger_1964]\]

### Aerodynamic heating and the recovery temperature

**The keystone.** Aerodynamic heating, the recovery factor and recovery temperature, convective heat transfer through compressible boundary layers, stagnation-point heating and the Reynolds analogy. **The stagnation point is the best-documented location, with 85 titles**, because the flux peaks there. The cluster also holds 43 titles on the Reynolds analogy, many of them outside aeronautics, kept because the analogy is the construct the article uses to obtain its convective coefficient. **Its median publication year of 1983 is the earliest of any cluster**, which agrees with the review's statement that the coupling thread has moved further than the thermal one.

**403 records.** \[[Abbas et al 1992][research_abbas_ibrahim_1992]\] \[[Abramov and Butkovskii 2018][research_abramov_butkovskii_2018]\] \[[Abuaf et al 1997][research_abuaf_dorri_1997]\] \[[Aerodynamic Heating and Thermal 1978][research_aerodynamic_heating_1978]\] \[[Aerothermal Environment for the 1978][research_aerothermal_environment_1978]\] \[[Alexander 1970][research_alexander_1970]\] \[[Alkidas and Durbetaki 1972][research_alkidas_durbetaki_1972]\] \[[Anderson 1968][research_anderson_1968]\] \[[Anderson 1968][research_anderson_1968_b]\] \[[Anderson 1968][research_andersonjr_1968]\] \[[Andreopoulos 1982][research_andreopoulos_1982]\] \[[Assessment of Key Aerothermal 1992][research_assessment_of_1992]\] \[[Babineaux and Horton 1966][research_babineaux_horton_1966]\] \[[Back and Cuffel 1970][research_back_cuffel_1970_b]\] \[[Back and Cuffel 1970][research_back_cuffel_1970_c]\] \[[Back and Cuffel 1971][research_back_cuffel_1971]\] \[[Back et al 1966][research_back_cuffel_1966]\] \[[Back et al 1967][research_back_cuffel_1967]\] \[[Back et al 1970][research_back_cuffel_1970]\] \[[Back et al 1984][research_back_cuffel_1984]\] \[[Bade 1962][research_bade_1962]\] \[[Bade 1975][research_bade_1975]\] \[[Bahrami 2012][research_bahrami_2012]\] \[[Balakrishnan and Kurian 2014][research_balakrishnan_kurian_2014]\] \[[Bartz 1955][research_bartz_1955]\] \[[Bartz 1965][research_bartz_1965]\] \[[Baryshev et al 1972][research_baryshev_vinogradov_1972]\] \[[Bashkin et al 2005][research_bashkin_egorov_2005]\] \[[Bassina et al 2001][research_bassina_strelets_2001]\] \[[Bauer et al 1978][research_bauer_winkler_1978]\] \[[Beck 1984][research_beck_1984]\] \[[Beck 1984][research_beck_1984_b]\] \[[Belnap et al 2002][research_belnap_vanrij_2002]\] \[[Biberman et al 1978][research_biberman_bronin_1978]\] \[[Biberman et al 1978][research_biberman_bronin_1978_b]\] \[[Biswas et al 2026][research_biswas_michels_2026]\] \[[Blair and Edwards 1982][research_blair_edwards_1982]\] \[[Bogucz et al 1988][research_bogucz_dirik_1988]\] \[[Bott and Bradshaw 1998][research_bott_bradshaw_1998]\] \[[Brandon et al 1979][research_brandon_britt_1979]\] \[[Brewster 2014][research_brewster_2014]\] \[[Brociek et al 2023][research_brociek_hetmaniok_2023]\] \[[Brooke 1957][research_brooke_1957]\] \[[Brunner 1959][research_brunner_1959]\] \[[Bryson and Edwards 1952][research_bryson_edwards_1952]\] \[[Burbank et al 1962][research_burbank_collins_1962]\] \[[Burmeister 1994][research_burmeister_1994]\] \[[Busing 1964][research_busing_1964]\] \[[Callaghan and Mason 1964][research_callaghan_mason_1964]\] \[[Carlson and Nerem 1968][research_carlson_nerem_1968]\] \[[Caruso and Naegeli 1976][research_caruso_naegeli_1976]\] \[[Cary 1968][research_cary_1968]\] \[[Cavazzuti 2020][research_cavazzuti_2020]\] \[[Chang and Nottage 1961][research_chang_nottage_1961]\] \[[Chao and Jeng 1965][research_chao_jeng_1965]\] \[[Chapman and Rubesin 1949][research_chapman_rubesin_1949]\] \[[Chauvin and Speegle 1957][research_chauvin_speegle_1957]\] \[[Chen 1971][research_chen_1971]\] \[[Chen et al 2024][research_chen_zhu_2024]\] \[[Cheng and Fu 2024][research_cheng_fu_2024]\] \[[Chou and Kalina 1982][research_chou_kalina_1982]\] \[[Chou and Smith 1974][research_chou_smith_1974]\] \[[Chou and Smith 1978][research_chou_smith_1978]\] \[[Chow 1963][research_chow_1963]\] \[[Clarke 1980][research_clarke_1980]\] \[[Coleburn and Drimmer 1961][research_coleburn_drimmer_1961]\] \[[Coleburn and Drimmer 1962][research_coleburn_drimmer_1962]\] \[[Coleman et al 1983][research_coleman_hodge_1983]\] \[[Coleman et al 1989][research_coleman_taylor_1989]\] \[[Compressible turbulent boundary layer 1970][research_compressible_turbulent_1970]\] \[[Compton and Cooper 1965][research_compton_cooper_1965]\] \[[Cook and Richards 1977][research_cook_richards_1977]\] \[[Czarnecki et al 1968][research_czarnecki_deveikis_1968]\] \[[Dahm 1966][research_dahm_1966]\] \[[Dai et al 2023][research_dai_zhao_2023]\] \[[Daryabeigi 2001][research_daryabeigi_2001]\] \[[Davis and Flügge-Lotz 1964][research_davis_fluggelotz_1964]\] \[[De Chant 1998][research_dechant_1998]\] \[[De Filippis and Serpico 1998][research_defilippis_serpico_1998]\] \[[Debieve et al 1997][research_debieve_dupont_1997]\] \[[Debrestian and Anderson 1994][research_debrestian_anderson_1994]\] \[[Demetriades 1977][research_demetriades_1977]\] \[[des Clers and Sternberg 1952][research_desclers_sternberg_1952]\] \[[Dirling et al 1970][research_dirling_rigdon_1970]\] \[[Dmitrenko 2019][research_dmitrenko_2019]\] \[[Dombrovsky and Reviznikov 2014][research_dombrovsky_reviznikov_2014]\] \[[Dombrovsky et al 2016][research_dombrovsky_reviznikov_2016]\] \[[Dong and Fan 1998][research_dong_fan_1998]\] \[[Dorrance 1961][research_dorrance_1961]\] \[[Dorrance and Dore 1954][research_dorrance_dore_1954]\] \[[Duan and He 2014][research_duan_he_2014]\] \[[Eckert 1956][research_eckert_1956]\] \[[Edquist et al][research_edquist_mahzari]\] \[[Edwards et al 2024][research_edwards_constantin_2024]\] \[[Edwards et al 2025][research_edwards_constantin_2025]\] \[[Effects of Aerodynamic Heating 1980][research_effects_of_1980]\] \[[Eftekhari et al 2025][research_eftekhari_siroueinejad_2025]\] \[[Elghobashi and Wassel 1980][research_elghobashi_wassel_1980]\] \[[Ellison 1969][research_ellison_1969]\] \[[Fallis 1953][research_fallis_1953]\] \[[Fay and Kemp 1963][research_fay_kemp_1963]\] \[[Fay and Riddell 1958][research_fay_riddell_1958]\] \[[Feldman and Bahder 1989][research_feldman_bahder_1989]\] \[[Ferraiuolo and Manca 2012][research_ferraiuolo_manca_2012]\] \[[Ferraiuolo et al 2009][research_ferraiuolo_manca_2009]\] \[[Ferrari 1955][research_ferrari_1955]\] \[[Fey et al 1993][research_fey_jeltsch_1993]\] \[[Finson et al 1981][research_finson_clarke_1981]\] \[[Fiore et al 2026][research_fiore_fabiani_2026]\] \[[Fischer and Norris 1949][research_fischer_norris_1949]\] \[[Formalev et al 2023][research_formalev_garibyan_2023]\] \[[Forooghi et al 2018][research_forooghi_magagnato_2018]\] \[[Foroozan et al 2025][research_foroozan_ianiro_2025]\] \[[Funazaki 1994][research_funazaki_1994]\] \[[Gaviglio 1987][research_gaviglio_1987]\] \[[Gerhart 1973][research_gerhart_1973]\] \[[Gerhart 1975][research_gerhart_1975]\] \[[Germerdonk et al 1990][research_germerdonk_biegel_1990]\] \[[Gokcen 1995][research_gokcen_1995]\] \[[Gokcen 1996][research_gokcen_1996]\] \[[Gokcen 1996][research_gokcen_1996_b]\] \[[Gokcen 1997][research_gokcen_1997]\] \[[Goodrich et al 1979][research_goodrich_derry_1979]\] \[[Gorla 1984][research_gorla_1984]\] \[[Gorla 1984][research_gorla_1984_b]\] \[[Granville and Boxall 1960][research_granville_boxall_1960]\] \[[Gros 1963][research_gros_1963]\] \[[Guinn 1961][research_guinn_1961]\] \[[Guo et al 2025][research_guo_zhang_2025]\] \[[Gupta et al 1992][research_gupta_jones_1992]\] \[[Gurentsov et al 2002][research_gurentsov_shikov_2002]\] \[[Gözükara and Ceylan 2024][research_gozukara_ceylan_2024]\] \[[Hanford and Wilson 1992][research_hanford_wilson_1992]\] \[[Hanford and Wilson 1992][research_hanford_wilson_1992_b]\] \[[Hanna and Stephens 1991][research_hanna_stephens_1991]\] \[[Hao et al 2024][research_hao_liu_2024]\] \[[Hargrave et al 1985][research_hargrave_fairweather_1985]\] \[[Harri 1964][research_harri_1964]\] \[[Harvazinski et al 2024][research_harvazinski_mehta_2024]\] \[[Hassan et al 2021][research_hassan_kunz_2021]\] \[[Hatton 1964][research_hatton_1964]\] \[[Hatton 1965][research_hatton_1965]\] \[[Hatton and Eustace 2019][research_hatton_eustace_2019]\] \[[Hayashi and Aso 1988][research_hayashi_aso_1988]\] \[[Heard 1965][research_heardjr_1965]\] \[[Heat Transfer in Incompressible 2013][research_heat_transfer_2013]\] \[[Hender 1982][research_hender_1982]\] \[[Hermann 2025][research_hermann_2025]\] \[[High and Bowman 1995][research_high_bowman_1995]\] \[[Hirschberg and Van Muiswinkel 1977][research_hirschberg_vanmuiswinkel_1977]\] \[[Horagiri and Nagai 2014][research_horagiri_nagai_2014]\] \[[Horton and Zeh 1966][research_horton_zeh_1966]\] \[[Horton and Zeh 1967][research_horton_zeh_1967]\] \[[Hosni et al 1991][research_hosni_coleman_1991]\] \[[Houra et al 2014][research_houra_nagano_2014]\] \[[Huang et al 2023][research_huang_lu_2023]\] \[[Hubble et al 2008][research_hubble_fu_2008]\] \[[Hube 1978][research_hube_1978]\] \[[Huston et al 1948][research_huston_warfield_1948]\] \[[Hürst et al 1994][research_hurst_schulz_1994]\] \[[Influence of Corrugation-Roughness Shape 1980][research_influence_of_1980]\] \[[Isakson 1957][research_isakson_1957]\] \[[Jayanti][research_jayanti]\] \[[Jeng and Reddy Gorla 1973][research_jeng_reddygorla_1973]\] \[[Jenke 1979][research_jenke_1979]\] \[[Jenness 1958][research_jenness_1958]\] \[[Jhajj et al 2014][research_jhajj_caron_2014]\] \[[Ji et al 2021][research_ji_duan_2021]\] \[[Jiang and Campbell 2008][research_jiang_campbell_2008]\] \[[Jin et al 2019][research_jin_xu_2019]\] \[[Johnson and Rubesin 1949][research_johnson_rubesin_1949]\] \[[Jones 1952][research_jones_1952]\] \[[Jones and Richie 1974][research_jones_richie_1974]\] \[[Junkhan 1978][research_junkhan_1978]\] \[[Kandula and Haddad 2007][research_kandula_haddad_2007]\] \[[Kaufman and Louis G. 1964][research_kaufman_louisg_1964]\] \[[Kaye and Brown 1954][research_kaye_brown_1954]\] \[[Kaye and Yeh 1955][research_kaye_yeh_1955]\] \[[Keel 1977][research_keeljr_1977]\] \[[Keçeci et al 2025][research_kececi_karakus_2025]\] \[[Kilburg 1968][research_kilburg_1968]\] \[[Kithcart and Klett 1995][research_kithcart_klett_1995]\] \[[Kumari and Nath 1982][research_kumari_nath_1982]\] \[[Kuwata 2021][research_kuwata_2021]\] \[[Kuwata 2026][research_kuwata_2026]\] \[[Laderman 1978][research_laderman_1978]\] \[[Lakshmi et al 2021][research_lakshmi_ramprabhu_2021]\] \[[Le Fur 1959][research_lefur_1959]\] \[[Leadon and Scott 1956][research_leadon_scott_1956]\] \[[Lee 1998][research_lee_1998]\] \[[Lee et al 1969][research_lee_yanta_1969]\] \[[Lees 1956][research_lees_1956]\] \[[Leontiev and Pavlyuchenko 2004][research_leontiev_pavlyuchenko_2004]\] \[[Leontiev and Pavlyuchenko 2008][research_leontiev_pavlyuchenko_2008]\] \[[Leontiev et al 2006][research_leontiev_lushchik_2006]\] \[[Leontiev et al 2017][research_leontiev_lushchik_2017]\] \[[Leontiev et al 2022][research_leontiev_lushchik_2022]\] \[[Leslie 1978][research_leslie_1978]\] \[[Levine and Rumsey 1958][research_levine_rumsey_1958]\] \[[Li and Eri 2007][research_li_eri_2007]\] \[[Li et al 2015][research_li_lv_2015]\] \[[Li et al 2015][research_li_narita_2015]\] \[[Li et al 2017][research_li_chen_2017]\] \[[Lin and Yang 2005][research_lin_yang_2005]\] \[[Liu et al 2012][research_liu_lv_2012]\] \[[Liu et al 2013][research_liu_li_2013]\] \[[Luce 1949][research_luce_jr_1949]\] \[[Luikov et al 1967][research_luikov_sergeev_1967]\] \[[Lunev 1971][research_lunev_1971]\] \[[Lushchik and Reshmin 2025][research_lushchik_reshmin_2025]\] \[[Luxton 1968][research_luxton_1968]\] \[[Mach Number and Wall 1978][research_mach_number_1978]\] \[[Maciejewski 1995][research_maciejewski_1995]\] \[[Mackay and Nagamatsu 1954][research_mackay_nagamatsu_1954]\] \[[Maekawa and Watanabe 2007][research_maekawa_watanabe_2007]\] \[[Manjhi and Kumar 2018][research_manjhi_kumar_2018]\] \[[Manjhi et al 2020][research_manjhi_kumar_2020]\] \[[Maples 1979][research_maples_1979]\] \[[Markov 1984][research_markov_1984]\] \[[Masoudi 1999][research_masoudi_1999]\] \[[Mastanaiah 1978][research_mastanaiah_1978]\] \[[Matthews et al 1972][research_matthews_buchanan_1972]\] \[[Mayle et al 1979][research_mayle_blair_1979]\] \[[Mehta 1986][research_mehta_1986]\] \[[Mehta 2012][research_mehta_2012]\] \[[Meier 1975][research_meier_1975]\] \[[Meier and Rotta 1971][research_meier_rotta_1971]\] \[[Merlet and Rumsey 1961][research_merlet_rumsey_1961]\] \[[Mobley and Summers][research_mobley_summers]\] \[[Moffat and Kays 1984][research_moffat_kays_1984]\] \[[Mohammadiun and Rahimi 2012][research_mohammadiun_rahimi_2012]\] \[[Morimoto et al 2015][research_morimoto_yamashita_2015]\] \[[Rodert 1940][research_heating_ice_1940]\] \[[Rumsey and Lee 1958][research_heat_transfer_mach146_1958]\] \[[Stephens 1959][research_rocket_model_heating_1959]\] \[[Rumsey and Lee 1961][research_cone_heat_transfer_1961]\] \[[Rashis and Bond 1961][research_skin_temp_freeflight_1961]\] \[[Banner et al 1962][research_x15_heating_1962]\] \[[Quinn and Gong 2000][research_transient_surface_temp_2000]\] \[[Negaard 1979][research_negaard_1979]\] \[[Nemish and Chernopiskii 1974][research_nemish_chernopiskii_1974]\] \[[Nestler 1978][research_nestler_1978]\] \[[Neumann and Freeman 2012][research_neumann_freeman_2012]\] \[[Okuno and Park 1968][research_okuno_park_1968]\] \[[Olstad 1969][research_olstad_1969]\] \[[Ott and Anderson 1994][research_ott_anderson_1994]\] \[[Owen 1971][research_owen_1971]\] \[[Spiridakos et al 2020][research_pspiridakos_cmarkatos_2020]\] \[[Palchekovskaya 2014][research_palchekovskaya_2014]\] \[[Pan et al 2010][research_pan_wu_2010]\] \[[Pappas 1954][research_pappas_1954]\] \[[Park and Ahn 1998][research_park_ahn_1998]\] \[[Park and Ahn 1999][research_park_ahn_1999]\] \[[Park et al 2024][research_park_moon_2024]\] \[[Pasiuk 1963][research_pasiuk_1963]\] \[[Pasiuk et al 1963][research_pasiuk_hastings_1963]\] \[[Patel 2016][research_patel_2016]\] \[[Phinney 1974][research_phinney_1974]\] \[[Pish et al 2019][research_pish_moradi_2019]\] \[[Pletcher 1971][research_pletcher_1971]\] \[[Pope 1968][research_pope_1968]\] \[[Pressure-temperature relation for constant-area 1958][research_pressure_temperature_relation_1958]\] \[[Procacci et al 2026][research_procacci_digiorgio_2026]\] \[[Qayoum and Panigrahi 2014][research_qayoum_panigrahi_2014]\] \[[Qin et al 2017][research_qin_xu_2017]\] \[[Ragulin and Shvalev 1983][research_ragulin_shvalev_1983]\] \[[Raju et al 1978][research_raju_chandra_1978]\] \[[Rakow and Waas 2005][research_rakow_waas_2005]\] \[[Rand 1963][research_rand_1963]\] \[[Readshaw 1961][research_readshaw_1961]\] \[[Reddy et al 2014][research_reddy_saikia_2014]\] \[[Ren et al 2021][research_ren_zhang_2021]\] \[[Rezaei et al 2025][research_rezaei_jafari_2025]\] \[[Rhisat and Molki 2024][research_rhisat_molki_2024]\] \[[Rieken et al 2020][research_rieken_berry_2020]\] \[[Rigby and Rae 1989][research_rigby_rae_1989]\] \[[Robinson 1952][research_robinson_1952]\] \[[Rodrigues 2026][research_rodrigues_2026]\] \[[Rom et al 1970][research_rom_seginer_1970]\] \[[Romanenko and Kharchenko 1963][research_romanenko_kharchenko_1963]\] \[[Rose and Stankevics 1963][research_rose_stankevics_1963]\] \[[Roy et al 2019][research_roy_saikia_2019]\] \[[Ru-ren Chow 1963][research_rurenchow_1963]\] \[[Ruan and Xiao 2025][research_ruan_xiao_2025]\] \[[Rubio and Ballard 1967][research_rubio_ballard_1967]\] \[[Rumsey and Lee 1961][research_rumsey_lee_1961]\] \[[Saavedra et al 2015][research_saavedra_lavagnoli_2015]\] \[[Saha et al 2019][research_saha_ranjan_2019]\] \[[Sambamurthi et al 1989][research_sambamurthi_warmbrod_1989]\] \[[Sano 1981][research_sano_1981]\] \[[Sasoh and Fujiwara 1990][research_sasoh_fujiwara_1990]\] \[[Savoldi et al 2025][research_savoldi_cammi_2025]\] \[[Sawyer 1977][research_sawyer_1977]\] \[[Scala 1961][research_scala_1961]\] \[[Scala 1962][research_scala_1962]\] \[[Scherrer et al 1949][research_scherrer_gowen_1949]\] \[[Schoeler 1987][research_schoeler_1987]\] \[[Schubert 1979][research_schubert_1979]\] \[[Seidman 1978][research_seidman_1978]\] \[[Shadloo and Hadjadj 2017][research_shadloo_hadjadj_2017]\] \[[Sharma et al 2018][research_sharma_shadloo_2018]\] \[[Sharma et al 2019][research_sharma_shadloo_2019]\] \[[Sheldon 1967][research_sheldon_1967]\] \[[Shevelev and Syzranova 2009][research_shevelev_syzranova_2009]\] \[[Shih 1976][research_shih_1976]\] \[[Shuttle Eleven Cove Aerodynamic 1978][research_shuttle_eleven_1978]\] \[[Sibulkin 1954][research_sibulkin_1954]\] \[[Sibulkin 1956][research_sibulkin_1956]\] \[[Sibulkin 1958][research_sibulkin_1958]\] \[[Simmers and Coney 1979][research_simmers_coney_1979]\] \[[Simonson 1975][research_simonson_1975]\] \[[Simonson 1988][research_simonson_1988]\] \[[Simsek et al 2016][research_simsek_kuran_2016]\] \[[Singh and Molki 2024][research_singh_molki_2024]\] \[[Sivykh and Zaulichny 1978][research_sivykh_zaulichny_1978]\] \[[Smith 1967][research_smith_1967]\] \[[Snodgrass 1955][research_snodgrass_1955]\] \[[So 1994][research_so_1994]\] \[[So 2020][research_so_2020]\] \[[Som 2021][research_som_2021]\] \[[Sommer and Short 1955][research_sommer_short_1955]\] \[[Spaid and Frishett 1972][research_spaid_frishett_1972]\] \[[Specker 2002][research_specker_2002]\] \[[Speegle 1958][research_speegle_1958]\] \[[Sprinks 1963][research_sprinks_1963]\] \[[Stalder et al 1950][research_stalder_rubesin_1950]\] \[[Stine and Scherrer 1952][research_stine_scherrer_1952]\] \[[Stock 1975][research_stock_1975]\] \[[Stulov and Shapiro 1969][research_stulov_shapiro_1969]\] \[[Sturek et al 1983][research_sturek_kayser_1983]\] \[[Sturek et al 1983][research_sturek_kayser_1983_b]\] \[[Su et al 2013][research_su_eri_2013]\] \[[Sucec 2020][research_sucec_2020]\] \[[Suchov et al 2022][research_suchov_kazmerchukh_2022]\] \[[Sunakawa and Uemura 1961][research_sunakawa_uemura_1961]\] \[[Sundén and Fu 2017][research_sunden_fu_2017]\] \[[Sutera and Williams 1968][research_sutera_williams_1968]\] \[[Sutton 1968][research_sutton_1968]\] \[[Sutton and Graves 1971][research_sutton_graves_1971]\] \[[Sutton et al 1995][research_sutton_troiler_1995]\] \[[Swanson 1958][research_swanson_1958]\] \[[Takahashi et al 2013][research_takahashi_yamada_2013]\] \[[Takahashi et al 2015][research_takahashi_yamada_2015]\] \[[Tashakkor et al 2011][research_tashakkor_canabal_2011]\] \[[Thornton and Dechaumphai 1987][research_thornton_dechaumphai_1987]\] \[[Titov et al 2010][research_titov_leontiev_2010]\] \[[Token 1974][research_token_1974]\] \[[Tokuda and Yang 1966][research_tokuda_yang_1966]\] \[[Tokuda and Yang 2019][research_tokuda_yang_2019]\] \[[Tong 1965][research_tong_1965]\] \[[Tong and Giedt 1963][research_tong_giedt_1963]\] \[[Tong et al 2024][research_tong_ji_2024]\] \[[Traci and Wilcox 1974][research_traci_wilcox_1974]\] \[[Traci and Wilcox 1975][research_traci_wilcox_1975]\] \[[Tucker and Maslen 1951][research_tucker_maslen_1951]\] \[[Turbulent External Boundary Layers 2023][research_turbulent_external_2023]\] \[[van Oudheusden 2004][research_vanoudheusden_2004]\] \[[Vancrayenest et al 2005][research_vancrayenest_tran_2005]\] \[[Vanfossen and Simoneau 1994][research_vanfossen_simoneau_1994]\] \[[Vanfossen et al 1994][research_vanfossen_simoneau_1994_b]\] \[[Vasantha and Nath 1986][research_vasantha_nath_1986]\] \[[Vasilevsky 2022][research_vasilevsky_2022]\] \[[Venema et al 2011][research_venema_vonterzi_2011]\] \[[Vigdorovich 2015][research_vigdorovich_2015]\] \[[Vigdorovich 2017][research_vigdorovich_2017]\] \[[Vinokur 1970][research_vinokur_1970]\] \[[Voisinet and Lee 1972][research_voisinet_lee_1972]\] \[[Voronkin 1971][research_voronkin_1971]\] \[[Wagner][research_wagner]\] \[[Wang and Bidek 1994][research_wang_bidek_1994]\] \[[Wang et al 1991][research_wang_hingst_1991]\] \[[Wang et al 2013][research_wang_li_2013]\] \[[Wang et al 2016][research_wang_vojtek_2016]\] \[[Wang et al 2026][research_wang_li_2026]\] \[[Webb 1971][research_webb_1971]\] \[[Wells 1989][research_wells_1989]\] \[[West and Brandis 2018][research_west_brandis_2018]\] \[[Whitten et al 1970][research_whitten_moffat_1970]\] \[[Wilson 1978][research_wilson_1978]\] \[[Winkler 1954][research_winkler_1954]\] \[[Winovich 1968][research_winovich_1968]\] \[[Woodworth et al 2023][research_woodworth_salazar_2023]\] \[[Woronowicz and Baganoff 1991][research_woronowicz_baganoff_1991]\] \[[Wortman 1970][research_wortman_1970]\] \[[Wortman 1971][research_wortman_1971]\] \[[Wu and Moin 2010][research_wu_moin_2010]\] \[[Wu et al 2013][research_wu_wu_2013]\] \[[Wu et al 2014][research_wu_wu_2014]\] \[[Xie et al 2013][research_xie_qi_2013]\] \[[Xie et al 2013][research_xie_wang_2013]\] \[[Xie et al 2016][research_xie_zhang_2016]\] \[[Xiong and Lele 2003][research_xiong_lele_2003]\] \[[Xiong and Lele 2004][research_xiong_lele_2004]\] \[[Xu et al 2025][research_xu_huang_2025]\] \[[Ahmed, et al 2011][research_y_n_2011]\] \[[Yang and Clark 1975][research_yang_clark_1975]\] \[[Yee et al 1961][research_yee_bailey_1961]\] \[[Yih et al 1952][research_yih_cermak_1952]\] \[[Young 1965][research_young_1965]\] \[[Yuceil and Dolling 1994][research_yuceil_dolling_1994]\] \[[Zhao et al 2009][research_zhao_zhang_2009]\] \[[Zhao et al 2016][research_zhao_wei_2016]\] \[[Ziefuß and Mehdizadeh 2020][research_ziefuss_mehdizadeh_2020]\]

### Directional stability, damping and supersonic stability

**What keeps the aircraft pointing forward, and what damps it.** Lateral and directional stability and handling qualities, static and dynamic stability derivatives, yaw dampers and the vertical tail. **A stability derivative is named in 63 titles**, and these are the quantities the article shows weaken twice at high Mach number, once through the lift-curve slope and once through the rate normalization.

**375 records.** \[[R.Yass et al 2009][research_aryass_hfarhood_2009]\] \[[Abou-Amer 2020][research_abouamer_2020]\] \[[Abramov et al 2005][research_abramov_goman_2005]\] \[[Adams 1972][research_adams_1972]\] \[[Ahmed and Worley 2008][research_ahmed_worley_2008]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990]\] \[[Aircraft lateral-directional handling qualities 2011][research_aircraft_lateral_directional_2011]\] \[[Aircraft Stability and Control 2003][research_aircraft_stability_2003]\] \[[Aircraft Stability and Control 2014][research_aircraft_stability_2014]\] \[[Aircraft Stability and Control 2024][research_aircraft_stability_2024]\] \[[Alaian et al 2016][research_alaian_basuno_2016]\] \[[Alemdaroglu et al 2002][research_alemdaroglu_iyigun_2002]\] \[[Alexander 1948][research_alexander_1948]\] \[[An Introduction to the 1966][research_an_introduction_1966]\] \[[Anderson and Innis 1965][research_anderson_innis_1965]\] \[[Anderson and Schroers 1972][research_anderson_schroers_1972]\] \[[Appendix G Development of 2003][research_appendix_g_2003]\] \[[Approximate Expressions for the 2007][research_approximate_expressions_2007]\] \[[Arabshahi et al 2011][research_arabshahi_taylor_2011]\] \[[Asadi and Wang 2017][research_asadi_wang_2017]\] \[[Asher et al 1957][research_asher_martuccelli_1957]\] \[[Ashraf and Van Kampen 2020][research_ashraf_vankampen_2020]\] \[[Babister 1980][research_babister_1980]\] \[[Balas et al 1996][research_balas_packard_1996]\] \[[Battaglia et al 2024][research_battaglia_baldieri_2024]\] \[[Bazile and Calderara 2012][research_bazile_calderara_2012]\] \[[Berg 1991][research_berg_1991]\] \[[Bhagwandin and Sahu 2011][research_bhagwandin_sahu_2011]\] \[[Bhagwandin and Sahu 2013][research_bhagwandin_sahu_2013]\] \[[Bhagwandin and Sahu 2014][research_bhagwandin_sahu_2014]\] \[[Bischoff and Palmer 1982][research_bischoff_palmer_1982]\] \[[Bischoff and Palmer 1983][research_bischoff_palmer_1983]\] \[[Bismarck-Nasr and Bones 2000][research_bismarcknasr_bones_2000]\] \[[Blake et al 2009][research_blake_gotwald_2009]\] \[[Bloy and Lea 1995][research_bloy_lea_1995]\] \[[Bolas 1929][research_bolas_1929]\] \[[Boling and Zha 2021][research_boling_zha_2021]\] \[[Bollech and Kelly 1954][research_bollech_kelly_1954]\] \[[Bozeman et al 2018][research_bozeman_tai_2018]\] \[[Brandeau 1978][research_brandeau_1978]\] \[[Braun 1959][research_braun_1959]\] \[[Brenckmann 1964][research_brenckmann_1964]\] \[[Bruner 1983][research_bruner_1983]\] \[[Bryson 1954][research_bryson_1954]\] \[[Bull and Kidd 1955][research_bull_kidd_1955]\] \[[Burns 1965][research_burns_1965]\] \[[Burt 1974][research_burt_1974]\] \[[Burt 1975][research_burt_1975]\] \[[Butler 1976][research_butler_1976]\] \[[Campbell and Abramovitz 1975][research_campbell_abramovitz_1975]\] \[[Carafoli 1969][research_carafoli_1969_c]\] \[[Chakravarty 1987][research_chakravarty_1987]\] \[[Chambers and Hall 2004][research_chambers_hall_2004]\] \[[Chapleo and Nair 1994][research_chapleo_nair_1994]\] \[[Chapter 4. Wing-Tail Plane 1957][research_chapter_4_1957]\] \[[Chavez and Vogel 2003][research_chavez_vogel_2003]\] \[[Chen and Xie 2024][research_chen_xie_2024]\] \[[Chen et al 2026][research_chen_gray_2026]\] \[[Cheng et al 2002][research_cheng_mei_2002]\] \[[Cheng et al 2003][research_cheng_lee_2003]\] \[[Chiu and Lin 1994][research_chiu_lin_1994]\] \[[Chowdhury et al 2021][research_chowdhury_keshmiri_2021]\] \[[Chuan et al 2016][research_chuan_feng_2016]\] \[[Ciliberti and Nicolosi 2025][research_ciliberti_nicolosi_2025]\] \[[Ciliberti et al 2017][research_ciliberti_dellavecchia_2017]\] \[[Connors and Swaim 1968][research_connors_swaim_1968]\] \[[Cook 2007][research_cook_2007]\] \[[Cooper et al 1970][research_cooper_wells_1970]\] \[[Corona-Sanchez and Rodriguez-Cortes 2015][research_coronasanchez_rodriguezcortes_2015]\] \[[Costigan and Calico 1989][research_costigan_calico_1989]\] \[[Covell et al 1992][research_covell_walker_1992]\] \[[Crasta and Khan 2014][research_crasta_khan_2014]\] \[[Crider 2004][research_crider_2004]\] \[[Crittenden et al 1977][research_crittenden_weisshaar_1977]\] \[[Crittenden et al 1978][research_crittenden_weishaar_1978]\] \[[Dahiya 2017][research_dahiya_2017]\] \[[Danowsky et al 2008][research_danowsky_thompson_2008]\] \[[Davidson and Andrisani 1996][research_davidson_andrisani_1996]\] \[[Davis 1957][research_davis_1957]\] \[[de Paula et al 2017][research_depaula_porto_2017]\] \[[Definitions of Aerodynamic Stability 2007][research_definitions_of_2007]\] \[[Della Vecchia et al 2015][research_dellavecchia_nicolosi_2015]\] \[[Demetriades 1983][research_demetriades_1983]\] \[[Deng et al 2024][research_deng_liu_2024]\] \[[DeSpirito et al 2008][research_despirito_silton_2008]\] \[[Development of Longitudinal and 2014][research_development_of_2014]\] \[[Development of Longitudinal and 2024][research_development_of_2024]\] \[[Dolan 1964][research_dolan_1964]\] \[[Doubrava et al 2008][research_doubrava_waszniowski_2008]\] \[[Dress et al 1992][research_dress_boyden_1992]\] \[[Dress et al 1994][research_dress_boyden_1994]\] \[[Driver 1958][research_driver_1958]\] \[[Dunning 1957][research_dunning_1957]\] \[[Dynamic Lateral-Directional Stability Theory 2003][research_dynamic_lateral_directional_2003]\] \[[Dynamic Stability and Control][research_dynamic_stability]\] \[[Ellen 1968][research_ellen_1968]\] \[[Ericsson 2001][research_ericsson_2001]\] \[[Experimental Dynamic Stability Investigation 2025][research_experimental_dynamic_2025]\] \[[Flax 1986][research_flax_1986]\] \[[Foster et al 1993][research_foster_ross_1993]\] \[[Fournier and Sleeman 1960][research_fournier_sleeman_1960]\] \[[Franklin 1971][research_franklin_1971]\] \[[Frazier 1991][research_frazier_1991]\] \[[Fung 1954][research_fung_1954]\] \[[Garrard 1998][research_garrard_1998]\] \[[Gerlach 1967][research_gerlach_1967]\] \[[Ghoreyshi et al 2026][research_ghoreyshi_aref_2026]\] \[[Ghosh et al 1998][research_ghosh_raisinghani_1998]\] \[[Gillis and Toll 1962][research_gillis_toll_1962]\] \[[Gilyard et al 1972][research_gilyard_berry_1972]\] \[[GNair et al 2012][research_gnair_mv_2012]\] \[[Go 2009][research_go_2009]\] \[[Goldsmith 1964][research_goldsmith_1964]\] \[[Goodman 1956][research_goodman_1956]\] \[[Goud and Dwivedi 2022][research_goud_dwivedi_2022]\] \[[Granata et al 2024][research_granata_savino_2024]\] \[[Granata et al 2024][research_granata_savino_2024_b]\] \[[Gratton 2014][research_gratton_2014]\] \[[Gratton 2018][research_gratton_2018]\] \[[Green and Spence 2004][research_green_spence_2004_b]\] \[[Green et al 2004][research_green_spence_2004]\] \[[Grenestedt 2008][research_grenestedt_2008]\] \[[Grenestedt et al 2006][research_grenestedt_ridder_2006]\] \[[Guan and Guo 2016][research_guan_guo_2016]\] \[[Guglieri and Quagliotti 1993][research_guglieri_quagliotti_1993]\] \[[Guo and Mei 2002][research_guo_mei_2002]\] \[[Guo and Mei 2003][research_guo_mei_2003]\] \[[Guo and Ren 2015][research_guo_ren_2015]\] \[[Guo and Ren 2019][research_guo_ren_2019]\] \[[Hall and Boothe 1972][research_hall_boothe_1972]\] \[[Hanson et al 2011][research_hanson_schaefer_2011]\] \[[Harris and Robinson 1960][research_harris_robinson_1960]\] \[[Harris and Robinson 1960][research_harris_robinson_1960_b]\] \[[Harvazinski et al 2014][research_harvazinski_sankaran_2014]\] \[[Hillier 1970][research_hillier_1970]\] \[[Hitch 1978][research_hitch_1978]\] \[[Hodgkinson et al 1990][research_hodgkinson_potsdam_1990]\] \[[Holzapfel et al 2006][research_holzapfel_dacosta_2006]\] \[[Huang 2016][research_huang_2016]\] \[[Ifju et al 2001][research_ifju_waszak_2001]\] \[[Innocenzi et al 2023][research_innocenzi_bruce_2023]\] \[[Irving 1966][research_irving_1966]\] \[[Jirásek et al 2018][research_jirasek_cummings_2018]\] \[[Johnson and Yang 1985][research_johnson_yang_1985]\] \[[Jones 1950][research_jones_1950]\] \[[Jones 1967][research_jones_1967]\] \[[Jones 1976][research_jones_1976]\] \[[Jones and Nisbet 1976][research_jones_nisbet_1976]\] \[[Joshi and Rickard 1981][research_joshi_rickard_1981]\] \[[Juliawan et al 2024][research_juliawan_lee_2024]\] \[[Kaattari 1959][research_kaattari_1959]\] \[[Kandil et al 1993][research_kandil_kandil_1993_b]\] \[[Kanneganti et al 2022][research_kanneganti_charan_2022]\] \[[Kayser et al 1978][research_kayser_sturek_1978]\] \[[Kazemba et al 2012][research_kazemba_braun_2012]\] \[[Kazemba et al 2017][research_kazemba_braun_2017]\] \[[Ke et al 2009][research_ke_wang_2009]\] \[[Kehrer 1964][research_kehrer_1964]\] \[[Kim et al 2024][research_kim_siddiqui_2024]\] \[[Klausmeyer 2026][research_klausmeyer_2026]\] \[[Krasil'nikov and Shmanenkov 2000][research_krasilnikov_shmanenkov_2000]\] \[[Krasnoshapka 1968][research_krasnoshapka_1968]\] \[[Kyo-Nam Koo][research_kyonamkoo]\] \[[Lallman 1985][research_lallman_1985]\] \[[Lamb et al 1981][research_lamb_sawyer_1981]\] \[[Lamb et al 1981][research_lamb_sawyer_1981_b]\] \[[Lampton and Valasek 2006][research_lampton_valasek_2006]\] \[[Landweber and Johnson 1951][research_landweber_johnson_1951]\] \[[Langham 1979][research_langham_1979]\] \[[Langston et al 2016][research_langston_nelson_2016]\] \[[Lateral-Directional Dynamics 1998][research_lateral_directional_dynamics_1998]\] \[[Lateral-Directional Stability Theory and 2003][research_lateral_directional_stability_2003]\] \[[Laudeman 1972][research_laudeman_1972]\] \[[Lebacqz et al 1974][research_lebacqz_radford_1974]\] \[[Lee and Yoon 2008][research_lee_yoon_2008]\] \[[Lee et al 2013][research_lee_kim_2013]\] \[[Lemon et al 2011][research_lemon_litt_2011]\] \[[Lensi 2000][research_lensi_2000]\] \[[Leopold et al][research_leopold_gastebois]\] \[[Lesalli and Cahyono 2020][research_lesalli_cahyono_2020]\] \[[Levin 1981][research_levin_1981]\] \[[Levin 1984][research_levin_1984]\] \[[Linehan and Mohseni 2016][research_linehan_mohseni_2016]\] \[[Liu 2024][research_liu_2024]\] \[[Liu and Platzer 1970][research_liu_platzer_1970]\] \[[Liu et al 2027][research_liu_liu_2027]\] \[[Livneh 1995][research_livneh_1995]\] \[[Livneh 1995][research_livneh_1995_b]\] \[[Long Lu and Turkoglu 2015][research_longlu_turkoglu_2015]\] \[[Longitudinal and Lateral Linear 2014][research_longitudinal_and_2014]\] \[[Lottati 1985][research_lottati_1985_b]\] \[[Lottati 1987][research_lottati_1987]\] \[[Lowenberg 2010][research_lowenberg_2010]\] \[[Lu][research_lu]\] \[[Lu and Turkoglu 2016][research_lu_turkoglu_2016]\] \[[Lu and Turkoglu 2018][research_lu_turkoglu_2018]\] \[[Lungu and Lungu 2015][research_lungu_lungu_2015]\] \[[Lungu and Lungu 2016][research_lungu_lungu_2016]\] \[[Luu and Ochi 2023][research_luu_ochi_2023]\] \[[Lysenko 1987][research_lysenko_1987]\] \[[Lyu et al 2022][research_lyu_gong_2022]\] \[[Lyu et al 2023][research_lyu_ye_2023]\] \[[Magee et al 2022][research_magee_hayes_2022]\] \[[Magee et al 2024][research_magee_hayes_2024]\] \[[Magee et al 2025][research_magee_hayes_2025]\] \[[Makarov and Pavlenko 2016][research_makarov_pavlenko_2016]\] \[[Martin and Gerber 1953][research_martin_gerber_1953]\] \[[Mason and Ravi 1994][research_mason_ravi_1994]\] \[[Matějů 2019][research_mateju_2019]\] \[[May et al 2011][research_may_lemon_2011]\] \[[Metin et al 2023][research_metin_uzuner_2023]\] \[[Mi 2021][research_mi_2021]\] \[[Michaelsen 1957][research_michaelsen_1957]\] \[[Miller and Franklin 1968][research_miller_franklin_1968]\] \[[Mitcham et al 1951][research_mitcham_blanchard_1951]\] \[[Mohamed and Dongare 2021][research_mohamed_dongare_2021]\] \[[Mohamed and Joy 2021][research_mohamed_joy_2021]\] \[[Mohammed 2007][research_mohammed_2007]\] \[[Morris 1966][research_morris_1966]\] \[[Moulton et al 2024][research_moulton_abraham_2024]\] \[[Muhlstein 1972][research_muhlsteinjr_1972]\] \[[Murphy and Klein 2010][research_murphy_klein_2010]\] \[[Musa et al 2015][research_musa_mansor_2015]\] \[[Musa et al 2026][research_musa_mansor_2026]\] \[[Abdulwahab 2009][research_nabdulwahab_2009]\] \[[Barufaldi et al 2020][research_nbarufaldi_hvictorjr_2020]\] \[[Grana and Shanks 1952][research_free_flight_tunnel_1952]\] \[[Finch and Walker 1953][research_x5_stability_1953]\] \[[Wetzel 1954][research_fighter_sweep_model_1954]\] \[[Spreemann and Few 1954][research_prelim_static_1954]\] \[[Anderson and Bray 1955][research_pitchup_evaluation_1955]\] \[[Reed 1955][research_x5_tail_loads_1955]\] \[[NACA 1956][research_config_stability_1956]\] \[[Edwards 1956][research_vtail_interference_1956]\] \[[Fournier and Silvers 1958][research_x2_lateral_model_1958]\] \[[Nae 2026][research_nae_2026]\] \[[Napolitano and Kincheloe 1996][research_napolitano_kincheloe_1996]\] \[[Narayan 1974][research_narayan_1974]\] \[[Fisher and Williams 1958][research_sweep_tail_height_1958]\] \[[Moul and Brown 1959][research_artificial_pitch_damping_1959]\] \[[Spearman and Driver 1959][research_forebody_deflection_1959]\] \[[Boyden 1974][research_supercritical_dynamic_1974]\] \[[Weisshaar and Zeiler 1982][research_flexible_fsw_dynamics_1982]\] \[[Owens et al 2002][research_reynolds_sst_2002]\] \[[Nepomuceno et al 2022][research_nepomuceno_moura_2022]\] \[[Newman and Buttrill 1995][research_newman_buttrill_1995]\] \[[Ogburn 1998][research_ogburn_1998]\] \[[Ogren et al 1974][research_ogren_sotanski_1974]\] \[[Okumoto and Elsanker 1973][research_okumoto_elsanker_1973]\] \[[Orlik-Ruckemann et al 1972][research_orlikruckemann_laberge_1972]\] \[[Owens et al 2007][research_owens_wahls_2007]\] \[[Oyibo 1983][research_oyibo_1983]\] \[[Ozcan et al 2025][research_ozcan_tekyurt_2025]\] \[[Pakhomov 2015][research_pakhomov_2015]\] \[[Pan and Huang 2018][research_pan_huang_2018]\] \[[Pan and Huang 2019][research_pan_huang_2019]\] \[[Park and Green 2000][research_park_green_2000]\] \[[Park et al 2001][research_park_lee_2001]\] \[[Parlett 1961][research_parlett_1961]\] \[[Peterson 1961][research_peterson_1961]\] \[[Peterson 2024][research_peterson_2024]\] \[[Peterson and Menees 1961][research_peterson_menees_1961]\] \[[Phillips 1948][research_phillips_1948]\] \[[Platzer and Sherer 1967][research_platzer_sherer_1967]\] \[[Platzer and Sherer 1968][research_platzer_sherer_1968]\] \[[Posingies 1968][research_posingies_1968]\] \[[Price 1943][research_price_1943]\] \[[Putman 1969][research_putman_1969]\] \[[Qasrawi and East 1981][research_qasrawi_east_1981]\] \[[Qi et al 2026][research_qi_zhang_2026]\] \[[Raghavan and Ananthkrishnan 2005][research_raghavan_ananthkrishnan_2005]\] \[[Raghavan and Ananthkrishnan 2023][research_raghavan_ananthkrishnan_2023]\] \[[Rajamurthy 2002][research_rajamurthy_2002]\] \[[Ratnayake et al 2011][research_ratnayake_waggoner_2011]\] \[[Ravi and Mason 1994][research_ravi_mason_1994]\] \[[Razgonyaev and Mason 1995][research_razgonyaev_mason_1995]\] \[[Re 1974][research_re_1974]\] \[[Regan 1964][research_regan_1964]\] \[[Ricciardi et al 2026][research_ricciardi_trout_2026]\] \[[Rodden and Bellinger 1982][research_rodden_bellinger_1982]\] \[[Rogal 1965][research_rogal_1965]\] \[[Roll Damping Analysis of 2023][research_roll_damping_2023]\] \[[Roysdon and Khalid 2010][research_roysdon_khalid_2010]\] \[[Roysdon and Khalid 2011][research_roysdon_khalid_2011]\] \[[Russell 1996][research_russell_1996]\] \[[Russell 1996][research_russell_1996_b]\] \[[Sachan et al 2025][research_sachan_r_2025]\] \[[Sachs 1977][research_sachs_1977]\] \[[Sachs 2007][research_sachs_2007_b]\] \[[Sadraey 2022][research_sadraey_2022]\] \[[Sadraey 2022][research_sadraey_2022_b]\] \[[Sargolzaie et al 2022][research_sargolzaie_fazeli_2022]\] \[[Schade and Hassell 1953][research_schade_hassell_1953]\] \[[Schairer 1941][research_schairer_1941]\] \[[Schnoebelen and Yechout 2003][research_schnoebelen_yechout_2003]\] \[[Schoenenberger 2013][research_schoenenberger_2013]\] \[[Schuman 2018][research_schuman_2018]\] \[[Schwanz 1972][research_schwanz_1972]\] \[[Seaver et al 2023][research_seaver_bennett_2023]\] \[[Seckel 1964][research_seckel_1964]\] \[[Seckel 1964][research_seckel_1964_b]\] \[[Seckel 1964][research_seckel_1964_c]\] \[[Seckel 1964][research_seckel_1964_d]\] \[[Shah and Granda 1998][research_shah_granda_1998]\] \[[Shamikh 2013][research_shamikh_2013]\] \[[Shams Taleghani et al 2025][research_shamstaleghani_yektaei_2025]\] \[[Shanbhag et al 2016][research_shanbhag_bashir_2016]\] \[[Shi et al 2024][research_shi_chen_2024]\] \[[Shields and Mohseni 2012][research_shields_mohseni_2012]\] \[[Shields and Mohseni 2013][research_shields_mohseni_2013]\] \[[Shrivastava and Stengel 1989][research_shrivastava_stengel_1989]\] \[[Shyprykevich and Sawyer 1973][research_shyprykevich_sawyer_1973]\] \[[Singh and Jategaonkar 1996][research_singh_jategaonkar_1996]\] \[[Sinha and Ananthkrishnan 2002][research_sinha_ananthkrishnan_2002]\] \[[Sinha and Ananthkrishnan 2017][research_sinha_ananthkrishnan_2017]\] \[[Sivan 1971][research_sivan_1971]\] \[[Sleeman 1957][research_sleeman_1957]\] \[[Smith 1982][research_smith_1982]\] \[[Snell 1993][research_snell_1993]\] \[[Snyder and Weisshaar 2013][research_snyder_weisshaar_2013]\] \[[Song et al 2014][research_song_yang_2014]\] \[[Sparks et al 1994][research_sparks_buffington_1994]\] \[[Spearman 1980][research_spearman_1980]\] \[[Spearman et al 1956][research_spearman_robinson_1956]\] \[[Srivastava 2009][research_srivastava_2009]\] \[[Stalnaker 2004][research_stalnaker_2004]\] \[[Static Longitudinal Stability Flight 2003][research_static_longitudinal_2003]\] \[[Static Stability and Control][research_static_stability]\] \[[Steinberg et al 1972][research_steinberg_uselton_1972]\] \[[Stenfelt and Ringertz 2009][research_stenfelt_ringertz_2009]\] \[[Stengel 1980][research_stengel_1980]\] \[[Stengel and Miller 1978][research_stengel_miller_1978]\] \[[Stone 1945][research_stone_1945]\] \[[Stough et al 1991][research_stoughiii_whipple_1991]\] \[[Suryanarayana et al 2022][research_suryanarayana_singh_2022]\] \[[Susanto et al 2021][research_susanto_bayusetiawan_2021]\] \[[Swaim and Connor 1968][research_swaim_connor_1968]\] \[[Szema and Shankar 1984][research_szema_shankar_1984]\] \[[Sznajder 2025][research_sznajder_2025]\] \[[Takahashi et al 2023][research_takahashi_griffin_2023]\] \[[Takahashi et al 2024][research_takahashi_griffin_2024]\] \[[Tatar and Masdari 2019][research_tatar_masdari_2019]\] \[[Taylor and Yoo 2011][research_taylor_yoo_2011]\] \[[Teper and Stapleford 1965][research_teper_stapleford_1965]\] \[[The design and development 1966][research_the_design_1966]\] \[[The Stability and Control 1968][research_the_stability_1968]\] \[[The Transformation of Aerodynamic 2007][research_the_transformation_2007]\] \[[Ting et al 2025][research_ting_wiersema_2025]\] \[[Tokugawa et al 2026][research_tokugawa_ishida_2026]\] \[[Tournes and Landrum][research_tournes_landrum]\] \[[Urnes and Nielsen 2010][research_urnes_nielsen_2010]\] \[[Uselton et al 1975][research_uselton_freemanjr_1975]\] \[[Vepa 2023][research_vepa_2023]\] \[[Vomaske et al 1961][research_vomaske_sadoff_1961]\] \[[Wang et al 2016][research_wang_liu_2016]\] \[[Wang et al 2021][research_wang_zhou_2021]\] \[[Wang et al 2022][research_wang_zhao_2022]\] \[[Weinacht 1998][research_weinacht_1998]\] \[[Wen et al 2013][research_wen_deng_2013]\] \[[Westin and de Freitas Pinto 2008][research_westin_defreitaspinto_2008]\] \[[Wilhelm and Schafranek 1986][research_wilhelm_schafranek_1986]\] \[[Williams et al 2025][research_williams_niestroy_2025]\] \[[Winograd and Miles 1956][research_winograd_miles_1956]\] \[[Woodiga et al 2015][research_woodiga_liu_2015]\] \[[Wu and Radespiel 2017][research_wu_radespiel_2017]\] \[[Wu et al 2018][research_wu_lv_2018]\] \[[Wykes 1968][research_wykes_1968]\] \[[Wolowicz and Yancey 1973][research_xb70_stability_1973]\] \[[Xie et al 2023][research_xie_cai_2023]\] \[[Xiong and Nguyen 2024][research_xiong_nguyen_2024]\] \[[Yahalom 1971][research_yahalom_1971]\] \[[Yin et al 2025][research_yin_jiang_2025]\] \[[Zhao et al 2016][research_zhao_xie_2016]\] \[[Zhu et al 2012][research_zhu_wen_2012]\] \[[Özöztürk et al 2011][research_ozozturk_kayran_2011]\]

### High-temperature materials, creep and oxidation

**The material question the keystone selects.** Creep, stress rupture and the Larson-Miller parameter, elevated-temperature tensile properties, and high-temperature oxidation and protective coatings, for steels and for nickel, titanium, aluminium and refractory alloys. **This literature is about materials rather than aircraft.** Only 6 of its 368 titles name an aircraft, an airframe, flight or aerospace, and many concern power-plant steels, turbine superalloys and coatings. They are kept because the creep correlation and the parabolic oxidation law the article uses are properties of the alloy rather than of its application.

**368 records.** \[[A.Yu. et al 2023][research_ayu_aa_2023]\] \[[Abdollahi and Ehsani 2016][research_abdollahi_ehsani_2016]\] \[[Abe 2021][research_abe_2021]\] \[[Abe et al 2016][research_abe_tabuchi_2016]\] \[[Ai and Qu 2011][research_ai_qu_2011]\] \[[Alam et al 2010][research_alam_rao_2010]\] \[[Alle 1967][research_alle_1967]\] \[[Allen et al 2004][research_allen_keustermans_2004]\] \[[Alnaser et al 2021][research_alnaser_yunus_2021]\] \[[Amano and Momose 1992][research_amano_momose_1992]\] \[[An Evaluation of the 1970][research_an_evaluation_1970]\] \[[Ando 2017][research_ando_2017]\] \[[Anwar et al 2022][research_anwar_mabruri_2022]\] \[[Atabay et al 2021][research_atabay_sanchezmata_2021]\] \[[Babu et al 2018][research_babu_murty_2018]\] \[[Bai et al 1994][research_bai_hou_1994]\] \[[Barrett 1982][research_barrett_1982]\] \[[Barrett 1992][research_barrett_1992]\] \[[Barrett 1997][research_barrett_1997]\] \[[Barrett 1999][research_barrett_1999]\] \[[Barrett and Lowell 1974][research_barrett_lowell_1974]\] \[[Barrett and Lowell 1981][research_barrett_lowell_1981]\] \[[Barton et al 2021][research_barton_zaremba_2021]\] \[[Bashu et al 1987][research_bashu_singh_1987]\] \[[Belyavin et al 2014][research_belyavin_kurenkova_2014]\] \[[Bettles and Gibson 2003][research_bettles_gibson_2003]\] \[[Bewlay et al 1999][research_bewlay_jackson_1999]\] \[[Bian et al 2024][research_bian_li_2024]\] \[[Bolton 2014][research_bolton_2014]\] \[[Booker and Booker 1980][research_booker_booker_1980]\] \[[Booker and Booker 1980][research_booker_booker_1980_b]\] \[[Booker et al 1982][research_booker_booker_1982]\] \[[Brady et al 1996][research_brady_brindley_1996]\] \[[Brady et al 1997][research_brady_smialek_1997]\] \[[Brinkman et al 1991][research_brinkman_booker_1991]\] \[[Brodrick 1962][research_brodrick_1962]\] \[[Brossard et al 2005][research_brossard_balmain_2005]\] \[[Brossard et al 2013][research_brossard_bouchaud_2013]\] \[[Byrne and Pickles 1990][research_byrne_pickles_1990]\] \[[Campbell et al 1965][research_campbell_gebler_1965]\] \[[Campo et al 1982][research_campo_ferrara_1982]\] \[[Carlson and Schwope 1952][research_carlson_schwope_1952]\] \[[Carroll et al 2011][research_carroll_cabet_2011]\] \[[Chakravarty and Narayanaswamy 2025][research_chakravarty_narayanaswamy_2025]\] \[[Chaku and McMahon 1974][research_chaku_mcmahon_1974]\] \[[Chalupová et al 2020][research_chalupova_steinbruck_2020]\] \[[Chang and Lin 2012][research_chang_lin_2012]\] \[[Chang et al 1953][research_chang_nordheim_1953]\] \[[Cheng et al 2016][research_cheng_fan_2016]\] \[[Cho and Findley 1983][research_cho_findley_1983]\] \[[Chorunov 2011][research_chorunov_2011]\] \[[Choudhary 2012][research_choudhary_2012]\] \[[Chyrkin et al 2010][research_chyrkin_huczkowski_2010]\] \[[Chyrkin et al 2015][research_chyrkin_sloof_2015]\] \[[Conrad 1959][research_conrad_1959]\] \[[Cook 1985][research_cook_1985]\] \[[Creep and stress rupture 1981][research_creep_and_1981]\] \[[Creep Rupture 2009][research_creep_rupture_2009]\] \[[Creep Rupture Properties 2004][research_creep_rupture_2004]\] \[[Cui and Lundin 2004][research_cui_lundin_2004]\] \[[Daniels et al 1956][research_daniels_masuda_1956]\] \[[Davies et al 2024][research_davies_parker_2024]\] \[[Davis 1964][research_davis_1964]\] \[[DeFries 1971][research_defries_1971]\] \[[Degischer et al 1987][research_degischer_aigner_1987]\] \[[DeGregoria 2015][research_degregoria_2015]\] \[[Dempers et al 1999][research_dempers_nikbin_1999]\] \[[Deng et al 2024][research_deng_qin_2024]\] \[[Densification of titanium alloy 2003][research_densification_of_2003]\] \[[Development of Creep-Resistant NiAl Ti,Hf 1997][research_development_of_1997]\] \[[Dewa et al 2018][research_dewa_park_2018]\] \[[Diaz 1985][research_diaz_1985]\] \[[Ding and Findley 1982][research_ding_findley_1982]\] \[[Ding and Subramaniam 1989][research_ding_subramaniam_1989]\] \[[Dong et al 2011][research_dong_shin_2011]\] \[[Dong et al 2023][research_dong_huang_2023]\] \[[Dong et al 2023][research_dong_lu_2023]\] \[[Dreshfield 1996][research_dreshfield_1996]\] \[[Du et al 2025][research_du_liu_2025]\] \[[Dwivedi 1983][research_dwivedi_1983]\] \[[Ebenezer et al 2022][research_ebenezer_koteswararao_2022]\] \[[Effects of Elevated Temperature 1968][research_effects_of_1968]\] \[[EI-Sawy and Shatynski 1982][research_eisawy_shatynski_1982]\] \[[Ekvall et al 1989][research_ekvall_rainen_1989]\] \[[Ekvall et al 1990][research_ekvall_rainen_1990]\] \[[Elevated-Temperature Properties of Ferritic 1990][research_elevated_temperature_properties_1990]\] \[[Elevated-Temperature Properties of Stainless 1990][research_elevated_temperature_properties_1990_b]\] \[[Elgallad et al 2023][research_elgallad_chen_2023]\] \[[England][research_england]\] \[[Ennis et al 1995][research_ennis_schuster_1995]\] \[[Es-Souni 2000][research_essouni_2000]\] \[[Es-Souni 2001][research_essouni_2001]\] \[[Favor et al 1957][research_favor_achbach_1957]\] \[[Feldman 1987][research_feldman_1987]\] \[[Fenn 1962][research_fenn_1962]\] \[[Flagella 1967][research_flagella_1967]\] \[[Flagella and Tarr 1967][research_flagella_tarr_1967]\] \[[Formation and Evaluation of 2020][research_formation_and_2020]\] \[[Fox-Rabinovich et al 2006][research_foxrabinovich_wilkinson_2006]\] \[[Freeman et al 1969][research_freeman_goodell_1969]\] \[[Freudenthal 1963][research_freudenthal_1963]\] \[[Fromont 1992][research_fromont_1992]\] \[[Galsworthy and Heawood 1982][research_galsworthy_heawood_1982]\] \[[Ganesh Kumar et al 2018][research_ganeshkumar_ganesan_2018]\] \[[Gao et al 2026][research_gao_jiang_2026]\] \[[Garfinkle 1974][research_garfinkle_1974]\] \[[Genot 2021][research_genot_2021]\] \[[Ghatak and Robi 2015][research_ghatak_robi_2015]\] \[[Giedt et al 1952][research_giedt_sherby_1952]\] \[[Gillig and Guarnieri 1956][research_gillig_guarnieri_1956]\] \[[Goodell and Freeman 1973][research_goodell_freeman_1973]\] \[[Gordon and Speiser 1960][research_gordon_speiser_1960]\] \[[Goswami 1995][research_goswami_1995]\] \[[Gourgues and Andrieu 2003][research_gourgues_andrieu_2003]\] \[[Gregory et al 1998][research_gregory_cooke_1998]\] \[[Grobstein and Doychak 1989][research_grobstein_doychak_1989]\] \[[Guarnieri 1954][research_guarnieri_1954]\] \[[Halford 1972][research_halford_1972]\] \[[Han et al 2020][research_han_su_2020]\] \[[Harbec and Todkill 1965][research_harbec_todkill_1965]\] \[[Harmathy and Stanzak 1970][research_harmathy_stanzak_1970]\] \[[Hayhurst 1974][research_hayhurst_1974]\] \[[Hayhurst 2001][research_hayhurst_2001]\] \[[Hebsur and Stephens 1991][research_hebsur_stephens_1991]\] \[[Hebsur et al 1988][research_hebsur_stephens_1988]\] \[[Hebsur et al 1989][research_hebsur_stephens_1989]\] \[[Henderson and Komenda 1998][research_henderson_komenda_1998]\] \[[Hibner et al 1997][research_hibner_sizek_1997]\] \[[High Temperature Tensile and 1962][research_high_temperature_1962]\] \[[Hill et al 1970][research_hill_misra_1970]\] \[[Hirschberg et al 1972][research_hirschberg_spera_1972]\] \[[Holt 1977][research_holt_1977]\] \[[Holtz 1964][research_holtz_1964]\] \[[Hou 2008][research_hou_2008]\] \[[Hou et al 2023][research_hou_liu_2023]\] \[[House et al 2021][research_house_ayoola_2021]\] \[[Hsu 2026][research_hsu_2026]\] \[[Hu et al 2023][research_hu_tan_2023]\] \[[Huang and Valentin 1974][research_huang_valentin_1974]\] \[[Huang et al 2021][research_huang_hu_2021]\] \[[Huysmans et al 2017][research_huysmans_vekeman_2017]\] \[[Hyde 1986][research_hyde_1986]\] \[[Hyers 2009][research_hyers_2009]\] \[[Imai et al 1992][research_imai_hirata_1992]\] \[[Ivanov 2008][research_ivanov_2008]\] \[[Jablonowski et al 1957][research_jablonowski_shober_1957]\] \[[Jaffe and Dorn 1960][research_jaffe_dorn_1960]\] \[[Jain 1986][research_jain_1986]\] \[[Jiang et al 2013][research_jiang_lin_2013]\] \[[Jiang et al 2026][research_jiang_liu_2026]\] \[[Jones et al 1984][research_jones_bylina_1984]\] \[[Joy et al 2024][research_joy_talapatra_2024]\] \[[Jung et al 2001][research_jung_wee_2001]\] \[[Katipelli and Dahotre 2001][research_katipelli_dahotre_2001]\] \[[Khakpour et al 2015][research_khakpour_soltani_2015]\] \[[Kies and Schwartz 1974][research_kies_schwartz_1974]\] \[[Kimura and Sawada 2022][research_kimura_sawada_2022]\] \[[King 1962][research_king_1962]\] \[[King and Ethridge 1985][research_king_ethridge_1985]\] \[[Klemm et al 1998][research_klemm_herrmann_1998]\] \[[Klueh and King 1977][research_klueh_king_1977]\] \[[Klueh and King 1982][research_klueh_king_1982]\] \[[Koizumi et al 1986][research_koizumi_tomizuka_1986]\] \[[Konno and Furuichi 1992][research_konno_furuichi_1992]\] \[[Kornilov 1958][research_kornilov_1958]\] \[[Korth 2000][research_korth_2000]\] \[[Krivenyuk et al 1971][research_krivenyuk_tsvilyuk_1971]\] \[[Kumar and Choubey 2023][research_kumar_choubey_2023]\] \[[Kılıçay 2020][research_kilicay_2020]\] \[[La et al 2022][research_la_wang_2022]\] \[[Lai and Findley 1979][research_lai_findley_1979]\] \[[Lai and Findley 1980][research_lai_findley_1980]\] \[[Lapin 1999][research_lapin_1999]\] \[[Lazarev 1988][research_lazarev_1988]\] \[[Lee et al 2023][research_lee_lee_2023]\] \[[Lemkey 1975][research_lemkey_1975]\] \[[Lemkey et al 1987][research_lemkey_smeggil_1987]\] \[[Li 2008][research_li_2008]\] \[[Li and Shi 2011][research_li_shi_2011]\] \[[Li and Yamaguchi 2022][research_li_yamaguchi_2022]\] \[[Li et al 2014][research_li_huang_2014]\] \[[Li et al 2019][research_li_zu_2019]\] \[[Li et al 2022][research_li_lv_2022]\] \[[Li et al 2023][research_li_wei_2023]\] \[[Liang et al 2023][research_liang_wu_2023]\] \[[Lin et al 2025][research_lin_liu_2025]\] \[[Liu and Li 2012][research_liu_li_2012]\] \[[Liu and Natesan 1988][research_liu_natesan_1988]\] \[[Liu and Oshida 1984][research_liu_oshida_1984]\] \[[Liu et al 2022][research_liu_li_2022]\] \[[Liu et al 2025][research_liu_gao_2025]\] \[[Locci et al 2000][research_locci_brady_2000]\] \[[Lowell and Barrett 1990][research_lowell_barrett_1990]\] \[[Ma et al 2012][research_ma_he_2012]\] \[[Ma et al 2021][research_ma_han_2021]\] \[[Mahorter and Robert G. 1961][research_mahorter_robertg_1961]\] \[[Malecka 2016][research_malecka_2016]\] \[[Mansy et al 1982][research_mansy_gobran_1982]\] \[[Mao et al 2022][research_mao_li_2022]\] \[[Maode and Sandström 1988][research_maode_sandstrom_1988]\] \[[Maruyama et al 1978][research_maruyama_oikawa_1978]\] \[[Maruyama et al 1992][research_maruyama_bi_1992]\] \[[Masterson 1963][research_masterson_1963]\] \[[Mathematical Modeling and Experimental 2018][research_mathematical_modeling_2018]\] \[[Mathew et al 2008][research_mathew_parameswaran_2008]\] \[[Maziasz 2004][research_maziasz_2004]\] \[[Maziasz and Swindeman 2001][research_maziasz_swindeman_2001]\] \[[McAlarney et al 1982][research_mcalarney_arons_1982]\] \[[McMurtrey 2018][research_mcmurtrey_2018]\] \[[Microstructure and High Temperature 2025][research_microstructure_and_2025]\] \[[Miller and Langdon 1980][research_miller_langdon_1980]\] \[[Mills 2002][research_mills_2002]\] \[[Moftakhar and Glinka 1998][research_moftakhar_glinka_1998]\] \[[Molins et al 1991][research_molins_andrieu_1991]\] \[[Moore and McDonald 1946][research_moore_mcdonald_1946]\] \[[Mukherjee and Martin 1963][research_mukherjee_martin_1963]\] \[[Mullendore and Grant 1964][research_mullendore_grant_1964]\] \[[NACA 1943][research_alclad_aging_1943]\] \[[Mathauser and Deveikis 1955][research_creep_2024t3_1955]\] \[[Hill et al 1956][research_oxidation_ignition_1956]\] \[[Mathauser and Deveikis 1957][research_creep_2024t3_1957]\] \[[Nagelschmidt et al 2025][research_nagelschmidt_herbrich_2025]\] \[[Narita et al 2001][research_narita_hayashi_2001]\] \[[Narita et al 2023][research_narita_sakata_2023]\] \[[Manning and Heimerl 1960][research_elevated_tensile_practice_1960]\] \[[Manning and Price 1961][research_stainless_rapid_heat_1961]\] \[[NASA 1985][research_creep_single_crystal_1985]\] \[[NASA 1989][research_monel_k500_1989]\] \[[Snyder and Kehoe 1991][research_heated_plate_modes_1991]\] \[[NASA 1993][research_creep_rupture_superalloy_1993]\] \[[Nickel et al 1992][research_nickel_fu_1992]\] \[[Nikulin et al 2010][research_nikulin_kaibyshev_2010]\] \[[Nilsson and Sandström 1988][research_nilsson_sandstrom_1988]\] \[[Nix 1982][research_nix_1982]\] \[[Nix 1984][research_nix_1984]\] \[[Nobakhti and Soltani 2014][research_nobakhti_soltani_2014]\] \[[Nobakhti and Soltani 2016][research_nobakhti_soltani_2016]\] \[[Nouri et al 2019][research_nouri_sahmani_2019]\] \[[Nyman 1965][research_nyman_1965]\] \[[Odabas et al 2025][research_odabas_karaoglanli_2025]\] \[[Oldrieve 1975][research_oldrieve_1975]\] \[[Pahutová et al 1969][research_pahutova_cadek_1969]\] \[[Papirno and Gerard 1962][research_papirno_gerard_1962]\] \[[Passos][research_passos]\] \[[Peichl et al 1987][research_peichl_wortmann_1987]\] \[[Penkalla et al 1988][research_penkalla_schubert_1988]\] \[[Piltch et al 1994][research_piltch_jihfen_1994]\] \[[Plummer et al][research_plummer_mendelev]\] \[[Prediction of Creep Rupture 2010][research_prediction_of_2010]\] \[[Prescott et al 1992][research_prescott_mitchell_1992]\] \[[Pritchard et al 2013][research_pritchard_carroll_2013]\] \[[Pryzybylski 1990][research_pryzybylski_1990]\] \[[Qu et al 2026][research_qu_xie_2026]\] \[[Quan et al 2022][research_quan_lianyiwang_2022]\] \[[Rahimian et al 2017][research_rahimian_ji_2017]\] \[[Rainen and Ekvall 1988][research_rainen_ekvall_1988]\] \[[Ramirez et al 2017][research_ramirez_haque_2017]\] \[[Reigel 2004][research_reigel_2004]\] \[[Render et al 2026][research_render_bello_2026]\] \[[Rice 1981][research_rice_1981]\] \[[Roach and VanEcho 1981][research_roach_vanecho_1981]\] \[[Roach and VanEcho 1984][research_roach_vanecho_1984]\] \[[Rolls and Arayici 1985][research_rolls_arayici_1985]\] \[[Rosa 1982][research_rosa_1982]\] \[[Rosli et al 2022][research_rosli_razak_2022]\] \[[Rouillard et al 2009][research_rouillard_cabet_2009]\] \[[Rupp and McMurtrey 2020][research_rupp_mcmurtrey_2020]\] \[[Rupp and McMurtrey 2021][research_rupp_mcmurtrey_2021]\] \[[Saito et al 2006][research_saito_hayashi_2006]\] \[[Salley and Kovacevich 1964][research_salley_kovacevich_1964]\] \[[Sato et al 2001][research_sato_sawada_2001]\] \[[Sawaragi 1995][research_sawaragi_1995]\] \[[Sessions et al 1977][research_sessions_mcmahon_1977]\] \[[Shahinian and Achter 1963][research_shahinian_achter_1963]\] \[[Sharma et al 2007][research_sharma_choi_2007]\] \[[Sharpe 1984][research_sharpe_jr_1984]\] \[[Shen et al 2019][research_shen_zhang_2019]\] \[[Sherby et al 1953][research_sherby_frenkel_1953]\] \[[Sherby et al 1956][research_sherby_lytton_1956]\] \[[Shi et al 2025][research_shi_guan_2025]\] \[[Shifler 2013][research_shifler_2013]\] \[[Shingledecker et al 2007][research_shingledecker_glanton_2007]\] \[[Shu et al 2023][research_shu_baik_2023]\] \[[Simmons and Cross 1954][research_simmons_cross_1954]\] \[[Singer 1964][research_singer_1964]\] \[[Sircar et al 1988][research_sircar_ribaudo_1988]\] \[[Smith 1973][research_smith_1973]\] \[[Smith 1975][research_smith_1975]\] \[[Spooner and Foley][research_spooner_foley]\] \[[Stepanova and Prokhorova 2016][research_stepanova_prokhorova_2016]\] \[[Stephens 1991][research_stephens_1991]\] \[[Stephenson 1966][research_stephenson_1966]\] \[[Stewart and Rowe 1962][research_stewart_rowe_1962]\] \[[Stoop and Shahinian 1966][research_stoop_shahinian_1966]\] \[[Sugamata et al 2006][research_sugamata_genei_2006]\] \[[Sun et al 2023][research_sun_miao_2023]\] \[[Sun et al 2025][research_sun_miao_2025]\] \[[Surianarayanan et al 1989][research_surianarayanan_iyer_1989]\] \[[Sutton et al 1997][research_sutton_chao_1997]\] \[[Swindeman 1970][research_swindeman_1970]\] \[[Taira and Ohnami 1962][research_taira_ohnami_1962]\] \[[Tanaka 1994][research_tanaka_1994]\] \[[Taylor et al 1987][research_taylor_guttmann_1987]\] \[[Tenney 1974][research_tenney_1974]\] \[[Terai 1968][research_terai_1968]\] \[[Tian et al 2023][research_tian_zhang_2023]\] \[[Tirpak 1985][research_tirpak_1985]\] \[[Totemeier 2007][research_totemeier_2007]\] \[[Tsuji et al 1994][research_tsuji_tanabe_1994]\] \[[Uemura et al 2020][research_uemura_kamata_2020]\] \[[Uludag and Turan 2015][research_uludag_turan_2015]\] \[[Van Echo 1964][research_vanecho_1964]\] \[[Varlese et al 2013][research_varlese_tului_2013]\] \[[Vasudev et al 2019][research_vasudev_thakur_2019]\] \[[Vasudevan and Leonard 2002][research_vasudevan_leonard_2002]\] \[[Visuttipitukul, et al 2009][research_visuttipitukul_chansaksoong_2009]\] \[[von Willingh and Knutsen 2022][research_vonwillingh_knutsen_2022]\] \[[Wang et al 2024][research_wang_zhao_creep_2024]\] \[[Wang et al 1992][research_wang_lou_1992]\] \[[Wang et al 2010][research_wang_mykhaylonka_2010]\] \[[Wang et al 2014][research_wang_tian_2014]\] \[[Wang et al 2018][research_wang_han_2018]\] \[[Wang et al 2018][research_wang_hawkins_2018]\] \[[Wang et al 2020][research_wang_ji_2020]\] \[[Wang et al 2020][research_wang_liu_2020]\] \[[Wang et al 2020][research_wang_xie_2020]\] \[[Wang et al 2025][research_wang_leary_2025]\] \[[Ward and Blackburn 1976][research_ward_blackburn_1976]\] \[[Ward and Blackburn 1976][research_ward_blackburn_1976_b]\] \[[Wei et al 2024][research_wei_zhang_2024]\] \[[Welded 18 Cr, 8 1958][research_welded_18_1958]\] \[[Welded Inconel W and 1958][research_welded_inconel_1958]\] \[[Wells and McBride 1967][research_wells_mcbride_1967]\] \[[Willems 1987][research_willems_1987]\] \[[Wright 1988][research_wright_1988]\] \[[Xi and Liu 2011][research_xi_liu_2011]\] \[[Xiang et al 2008][research_xiang_rose_2008]\] \[[Xiang et al 2020][research_xiang_xie_2020]\] \[[Xu and Guo 2003][research_xu_guo_2003]\] \[[Xu et al 2010][research_xu_yao_2010]\] \[[Yahya A. AL-Salman et al 2013][research_yahyaaalsalman_mahmoodahmood_2013]\] \[[Yan et al 1989][research_yan_munn_1989]\] \[[Yan et al 2021][research_yan_tai_2021]\] \[[Yang and Li 2023][research_yang_li_2023]\] \[[Yang and Li 2023][research_yang_li_2023_b]\] \[[Yang et al 2023][research_yang_sun_2023]\] \[[Yang et al 2024][research_yang_liang_2024]\] \[[Yao et al 2014][research_yao_he_2014]\] \[[Yerkovich and Guarnieri 1955][research_yerkovich_guarnieri_1955]\] \[[Yoo et al 2004][research_yoo_shin_2004]\] \[[Yoon et al 2012][research_yoon_jeon_2012]\] \[[Young 2016][research_young_2016]\] \[[Young 2016][research_young_2016_b]\] \[[Yount et al 1968][research_yount_smith_1968]\] \[[Zhang 2009][research_zhang_2009]\] \[[Zhang et al 2024][research_zhang_feng_2024]\] \[[Zhang and Geng 2013][research_zhang_geng_2013]\] \[[Zhang et al 2016][research_zhang_wang_2016]\] \[[Zhang et al 2022][research_zhang_xiao_2022]\] \[[Zhang et al 2023][research_zhang_li_2023]\] \[[Zhang et al 2024][research_zhang_li_2024]\] \[[Zhang et al 2024][research_zhang_xin_2024]\] \[[Zhang et al 2026][research_zhang_zhang_2026_b]\] \[[Zhang, et al 2011][research_zhang_peng_2011]\] \[[Zhou et al 2024][research_zhou_yuan_2024]\] \[[Zhu et al 2025][research_zhu_wu_2025]\] \[[Zima 1956][research_zima_1956]\] \[[Zubair et al 2022][research_zubair_ejaz_2022]\]

### Escape, capsules and parachute recovery

**The escape chain that failed.** Ejection seats, escape capsules and crew modules, windblast, and parachute deployment, opening shock and supersonic decelerators. **Parachutes dominate, with 166 titles, against 64 on ejection seats and 22 on capsules and crew modules.** Supersonic parachutes for Mars entry are the subject of 23 of the records, which is the opening-shock and reefing problem the article identifies as the link that failed, studied for a different vehicle.

**301 records.** \[[A special escape capsule 1952][research_a_special_1952]\] \[[A supersonic parachute 1949][research_a_supersonic_1949]\] \[[Abensur 2008][research_abensur_2008]\] \[[Adams 2014][research_adams_2014]\] \[[Aero has finished upgraded 2006][research_aero_has_2006]\] \[[Aircraft crew escape system 2014][research_aircraft_crew_2014]\] \[[Altgelt and Ward 1968][research_altgelt_ward_1968]\] \[[Anthony 2005][research_anthony_2005]\] \[[Aryaman et al 2023][research_aryaman_naveenraj_2023]\] \[[As'ad et al 2022][research_asad_avery_2022]\] \[[As'ad et al 2024][research_asad_avery_2024]\] \[[Babcock and Wiltse 1965][research_babcock_wiltse_1965]\] \[[Baber et al 1962][research_baber_carter_1962]\] \[[Babish III 1966][research_babishiii_1966]\] \[[Baker][research_baker]\] \[[Bao et al 2021][research_bao_zhou_2021]\] \[[Barlog 1979][research_barlog_1979]\] \[[Barnhardt et al 2007][research_barnhardt_drayna_2007]\] \[[Barry and Bassick 1995][research_barry_bassick_1995]\] \[[Bassett et al 2018][research_bassett_pei_2018]\] \[[Blachowski and Ostrowski 2001][research_blachowski_ostrowski_2001]\] \[[Blanchard and Raper 1960][research_blanchard_raper_1960]\] \[[Boustani et al 2019][research_boustani_barad_2019]\] \[[Boustani et al 2020][research_boustani_anugrah_2020]\] \[[Boustani et al 2022][research_boustani_kenway_2022]\] \[[Bozack 1970][research_bozack_1970]\] \[[Bozack and Doerr 1981][research_bozack_doerr_1981]\] \[[Bradfield and Thomasson 1966][research_bradfield_thomasson_1966]\] \[[Brandeau et al 2015][research_brandeau_gallon_2015]\] \[[Brinkman 1992][research_brinkman_1992]\] \[[Brooks and Dejarnette 1970][research_brooksjr_dejarnette_1970]\] \[[Brunner and Nerem 1970][research_brunner_nerem_1970]\] \[[Budd Co Fort Washington Pa Technical Center 1978][research_buddcofortwashingtonpatechnicalcenter_1978]\] \[[Buller 2017][research_buller_2017]\] \[[Burns and Ray 1967][research_burns_ray_1967]\] \[[Butler et al 1983][research_butler_fleck_1983]\] \[[Cadieux and Barad 2024][research_cadieux_barad_2024]\] \[[Cadieux and Barad 2025][research_cadieux_barad_2025]\] \[[Cadieux and Barad 2026][research_cadieux_barad_2026]\] \[[Cadieux et al 2023][research_cadieux_angel_2023]\] \[[Cao et al 2026][research_cao_siqi_2026]\] \[[Caruso and Mendenhall 1992][research_caruso_mendenhall_1992]\] \[[Cheng and Pellettiere 2005][research_cheng_pellettiere_2005]\] \[[Chiang 1980][research_chiang_1980]\] \[[Clark et al 2015][research_clark_gallon_2015]\] \[[Clark et al 2015][research_clark_manning_2015]\] \[[Coleman et al 2026][research_coleman_lobbia_2026]\] \[[Computational aerodynamic analysis of 1994][research_computational_aerodynamic_1994]\] \[[Connors and Sachs 1957][research_connors_sachs_1957]\] \[[Cook 2013][research_cook_2013]\] \[[Craley and Desabrais 2007][research_craley_desabrais_2007]\] \[[Crew escape propulsion system 2003][research_crew_escape_2003]\] \[[Crew escape, rescue and][research_crew_escape]\] \[[Crothers 1997][research_crothers_1997]\] \[[Cummings and Adams 1982][research_cummings_adams_1982]\] \[[Datta et al][research_datta_wiltsee]\] \[[Davidescu et al 2026][research_davidescu_andrei_2026]\] \[[Deans 1964][research_deans_1964]\] \[[Dehua et al 2006][research_dehua_jinjun_2006]\] \[[Derkevorkian et al 2019][research_derkevorkian_avery_2019]\] \[[Dillon et al 1990][research_dillon_king_1990]\] \[[Disselkoen et al 1989][research_disselkoen_heise_1989]\] \[[Doherr 2003][research_doherr_2003]\] \[[Douglas Aircraft Co Long Beach Ca 1983][research_douglasaircraftcolongbeachca_1983]\] \[[Du 2013][research_du_2013]\] \[[Eckles and Slater 1975][research_eckles_slater_1975]\] \[[Ejection Seat 2003][research_ejection_seat_2003]\] \[[Ejection Seat 2015][research_ejection_seat_2015]\] \[[Ejection Seat Testing 2021][research_ejection_seat_2021]\] \[[Elson et al 1997][research_elson_lingard_1997]\] \[[Engstrom and Lang 1961][research_engstrom_lang_1961]\] \[[Ericksen et al 1984][research_ericksen_pepper_1984]\] \[[Failure by Stress-Corrosion Cracking 2019][research_failure_by_2019]\] \[[Ford 1979][research_ford_1979]\] \[[Ford 1985][research_ford_1985]\] \[[French 1964][research_french_1964]\] \[[French 1967][research_french_1967]\] \[[French 1971][research_french_1971]\] \[[French 1979][research_french_1979]\] \[[French 1980][research_french_1980]\] \[[French 1988][research_french_1988]\] \[[Gallon and Witkowski 2015][research_gallon_witkowski_2015]\] \[[Gallon et al 2013][research_gallon_witkowski_2013]\] \[[Gao et al 2016][research_gao_zhang_2016]\] \[[Ghasimi and Rabinovitch 2023][research_ghasimi_rabinovitch_2023]\] \[[Giersch et al 2015][research_giersch_clark_2015]\] \[[Gladh et al 2013][research_gladh_ang_2013]\] \[[Gragg and Haars 1975][research_gragg_haars_1975]\] \[[Gragg et al 1982][research_gragg_evans_1982]\] \[[Greene 1970][research_greene_1970]\] \[[Gross and Mawhinney 1970][research_gross_mawhinney_1970]\] \[[Guan et al 2013][research_guan_zhu_2013]\] \[[Habchi and Hufford 1995][research_habchi_hufford_1995]\] \[[Habchi et al 1992][research_habchi_przekwas_1992]\] \[[Habchi et al 1995][research_habchi_hufford_1995_b]\] \[[Heinrich 1966][research_heinrich_1966]\] \[[Heinrich 1972][research_heinrich_1972]\] \[[Heinrich and Hektner 1970][research_heinrich_hektner_1970]\] \[[Heinrich and Noreen 1968][research_heinrich_noreen_1968]\] \[[Heinrich and Saari 1975][research_heinrich_saari_1975]\] \[[Heinrich and Saari 1978][research_heinrich_saari_1978]\] \[[Heinrich et al 1974][research_heinrich_noreen_1974]\] \[[Hellyer and Sherhod][research_hellyer_sherhod]\] \[[Henke and Nerem 1968][research_henke_nerem_1968]\] \[[Henry et al 2017][research_henry_patel_2017]\] \[[Hermes crew escape system 1990][research_hermes_crew_1990]\] \[[Hinada et al 1991][research_hinada_inatani_1991]\] \[[Hiraki et al 1997][research_hiraki_hinada_1997]\] \[[Hodell and Rosner 1957][research_hodell_rosner_1957]\] \[[Homan 1970][research_homan_1970]\] \[[Horenstein and Roberts 1993][research_horenstein_roberts_1993]\] \[[Howland 1979][research_howland_1979]\] \[[Huang et al 2020][research_huang_avery_2020]\] \[[Hufford and Habchi 1994][research_hufford_habchi_1994]\] \[[Ibrahim 1965][research_ibrahim_1965]\] \[[Jamison 1966][research_jamison_1966]\] \[[Jamison 1967][research_jamison_1967]\] \[[Jana et al 2021][research_jana_sreedhar_2021]\] \[[Jenkins 2018][research_jenkins_2018]\] \[[Jia et al 2013][research_jia_han_2013]\] \[[Jia-Lin et al 2014][research_jialin_lei_2014]\] \[[Jines 1980][research_jines_1980]\] \[[Johari and Desabrais 2002][research_johari_desabrais_2002]\] \[[Johnson 1986][research_johnson_1986]\] \[[Johnson 1989][research_johnson_1989]\] \[[Johnson and Faurote 1972][research_johnson_faurote_1972]\] \[[Johnson and Pilla 2012][research_johnsonms_pilla_2012]\] \[[Jones 1966][research_jones_1966]\] \[[Kandis and Witkowski 2019][research_kandis_witkowski_2019]\] \[[Karunakaran 2018][research_karunakaran_2018]\] \[[Keck 1975][research_keck_1975]\] \[[Keller and Plaga 2008][research_keller_plaga_2008]\] \[[Khader and Huston 1987][research_khader_huston_1987]\] \[[Kimata et al 2015][research_kimata_taguchi_2015]\] \[[Klimas 1973][research_klimas_1973]\] \[[Klimas and Rogers 1975][research_klimas_rogers_1975]\] \[[Kokane et al 2026][research_kokane_mahbuburrahman_2026]\] \[[Kou and Zhan 2022][research_kou_zhan_2022]\] \[[Kowaleczko et al 2018][research_kowaleczko_dlugolecki_2018]\] \[[Kowaleczko et al 2025][research_kowaleczko_pietraszek_2025]\] \[[Lee 1984][research_lee_1984]\] \[[Lee 1989][research_lee_1989]\] \[[Lee 1993][research_lee_1993]\] \[[Lee 1994][research_lee_1994]\] \[[Li and Han 2021][research_li_han_2021]\] \[[Liever and Habchi 2004][research_liever_habchi_2004]\] \[[Lin 1986][research_lin_1986]\] \[[Lingard and Darley 2005][research_lingard_darley_2005]\] \[[Lingard et al 1989][research_lingard_barnard_1989]\] \[[Lingard et al 2013][research_lingard_underwood_2013]\] \[[Littell et al 1967][research_littell_bailey_1967]\] \[[Liu et al 2022][research_liu_gao_2022]\] \[[Lorch 1981][research_lorch_1981]\] \[[Lorenz and Lam 2026][research_lorenz_lam_2026]\] \[[Lowry et al 1994][research_lowry_mellen_1994]\] \[[Ludtke 1973][research_ludtke_1973]\] \[[Ludtke 1986][research_ludtke_1986]\] \[[Maca and Lee 1996][research_macaiii_lee_1996]\] \[[Maloney 2011][research_maloney_2011]\] \[[Manjith 2026][research_manjith_2026]\] \[[Manzuk 1970][research_manzuk_1970]\] \[[Mao et al 2011][research_mao_lin_2011]\] \[[Martin 1956][research_martin_1956]\] \[[Martin-Baker at the 1988][research_martin_baker_at_1988]\] \[[Mastropietro et al 2013][research_mastropietro_pauken_2013]\] \[[Matsuo and Butler 1983][research_matsuo_butler_1983]\] \[[McCarty and Smith 1982][research_mccarty_smith_1982]\] \[[McEwan 1970][research_mcewan_1970]\] \[[McGrath 2003][research_mcgrath_2003]\] \[[McMullen 1973][research_mcmullen_1973]\] \[[Meyer 1958][research_meyer_1958]\] \[[Mickey and Stuart 1967][research_mickey_stuartjr_1967]\] \[[Militký et al 2025][research_militky_wiener_2025]\] \[[Millard et al 1989][research_millard_machin_1989]\] \[[Miller 1975][research_miller_jr_1975]\] \[[Moog 1975][research_moog_1975]\] \[[Murray 1961][research_murray_1961]\] \[[Murtaza and Indluru 2026][research_murtaza_indluru_2026]\] \[[Hegenwald 1958][research_x15_escape_1958]\] \[[Tanner et al 2015][research_ldsd_ballute_2015]\] \[[Nelsen 1995][research_nelsen_1995]\] \[[Niemi 1992][research_niemi_jr_1992]\] \[[O'Brien et al][research_obrien_frazier]\] \[[O'Farrell et al 2016][research_ofarrell_brandeau_2016]\] \[[O'Farrell et al 2018][research_ofarrell_karlgaard_2018]\] \[[O'Farrell et al 2022][research_ofarrell_clark_2022]\] \[[O'Farrell et al 2023][research_ofarrell_leylek_2023]\] \[[Ojetola et al 2011][research_ojetola_onyebueke_2011]\] \[[Optimum time of delay 1942][research_optimum_time_1942]\] \[[Ortega et al 2017][research_ortega_flores_2017]\] \[[Ouyang et al 2026][research_ouyang_zhang_2026]\] \[[Parate 2022][research_parate_2022]\] \[[Payne 1969][research_payne_1969]\] \[[Payne 1973][research_payne_1973]\] \[[Payne and Band 1976][research_payne_band_1976]\] \[[Pearson 1960][research_pearson_1960]\] \[[Pearson 1961][research_pearson_1961]\] \[[Pedersen 1961][research_pedersen_1961]\] \[[Pellettlere et al 2003][research_pellettlere_nguyen_2003]\] \[[Pepelea et al 2018][research_pepelea_cojocaru_2018]\] \[[Perry 2007][research_perry_2007]\] \[[Peterson and Roberts 1973][research_peterson_roberts_1973]\] \[[Peterson et al 2018][research_peterson_derkevorkian_2018]\] \[[Piacentino et al 1978][research_piacentino_mcenerney_1978]\] \[[Pickl 1989][research_pickl_1989]\] \[[Pilot Escape Capsule 1961][research_pilot_escape_1961]\] \[[Pint et al 2003][research_pint_pellettiere_2003]\] \[[Placco 2023][research_placco_2023]\] \[[Placco 2023][research_placco_2023_b]\] \[[Placco et al 2026][research_placco_hancock_2026]\] \[[Pleasants 1975][research_pleasants_1975]\] \[[Potvin 2007][research_potvin_2007]\] \[[Potvin and Potvin 1997][research_potvin_potvin_1997]\] \[[Potvin and Ray 2019][research_potvin_ray_2019]\] \[[Purvis 1983][research_purvis_1983]\] \[[Purvis 1984][research_purvis_1984]\] \[[Purvis 1984][research_purvis_1984_b]\] \[[Rabinovitch et al 2018][research_rabinovitch_huang_2018]\] \[[Rabinovitch et al 2019][research_rabinovitch_griffin_2019]\] \[[Rabinovitch et al 2019][research_rabinovitch_huang_2019]\] \[[Rabinovitch et al 2022][research_rabinovitch_asad_2022]\] \[[Rahman et al 2024][research_rahman_bandal_2024]\] \[[Rahman et al 2024][research_rahman_chandel_2024]\] \[[Rahman et al 2025][research_rahman_bandal_2025]\] \[[Robert 1988][research_robert_1988]\] \[[Robertson et al 2006][research_robertson_charles_2006]\] \[[Rock and Habchi 1998][research_rock_habchi_1998]\] \[[Rock et al 1999][research_rock_habchi_1999]\] \[[Roelke et al 2025][research_roelke_green_2025]\] \[[Rooks et al 2020][research_rooks_novotny_2020]\] \[[Rosales and Stoltzfus 2009][research_rosales_stoltzfus_2009]\] \[[Ross 1972][research_ross_1972]\] \[[Subash et al 2024][research_s_babup_2024]\] \[[Sadeck and Lee 2009][research_sadeck_lee_2009]\] \[[Sant and Allen 2011][research_sant_allen_2011]\] \[[Saravanan et al 2021][research_saravanan_tennyson_2021]\] \[[Scherberg and Ferguson 1952][research_scherberg_ferguson_1952]\] \[[Schmalhofer and White 1966][research_schmalhoferjr_white_1966]\] \[[Schneck 1978][research_schneck_1978]\] \[[Seeney et al 1968][research_seeney_bull_1968]\] \[[Shaffer and Brinkley 1974][research_shaffer_brinkley_1974]\] \[[Shannon 1973][research_shannon_1973]\] \[[Siegel et al 2024][research_siegel_ofarrell_2024]\] \[[Sims 1963][research_sims_1963]\] \[[Smitha et al 2021][research_smitha_joy_2021]\] \[[Smollett 1955][research_smollett_1955]\] \[[Somanath et al 2021][research_somanath_unnikrishnannair_2021]\] \[[Spaceflight crew escape system 2004][research_spaceflight_crew_2004]\] \[[Specker and Brinkley 1983][research_specker_brinkley_1983]\] \[[Speelman 1977][research_speelman_1977]\] \[[Speelman 1975][research_speelmaniii_1975]\] \[[Spinal injuries in the 1980][research_spinal_injuries_1980]\] \[[Sreenivasulu et al 2021][research_sreenivasulu_2021]\] \[[Stech 1977][research_stech_1977]\] \[[Study on Critical Parachute 2024][research_study_on_2024]\] \[[Sundberg 1975][research_sundberg_1975]\] \[[Tadios 1991][research_tadios_1991]\] \[[Taguchi et al 2015][research_taguchi_semba_2015]\] \[[Taguchi et al 2021][research_taguchi_mori_2021]\] \[[Takabayashi and Kitamura 2019][research_takabayashi_kitamura_2019]\] \[[Takabayashi et al 2019][research_takabayashi_fukumoto_2019]\] \[[Tang and Qian 2016][research_tang_qian_2016]\] \[[Tang et al 2021][research_tang_wang_2021]\] \[[Tauby 1979][research_tauby_1979]\] \[[Tharion et al 2025][research_tharion_yang_2025]\] \[[The advanced stabilised ejection 1974][research_the_advanced_1974]\] \[[Tian and Chen 2012][research_tian_chen_2012]\] \[[Tibbits and Ivanov 2015][research_tibbits_ivanov_2015]\] \[[Toni 1968][research_toni_1968]\] \[[Wang 1999][research_wang_1999]\] \[[Wang et al 2021][research_wang_tang_2021]\] \[[Wang et al 2021][research_wang_tang_2021_b]\] \[[Ward and Myers 1967][research_ward_myers_1967]\] \[[Ware et al 1988][research_ware_spencerjr_1988]\] \[[Watkins 1986][research_watkins_1986]\] \[[Watson 1975][research_watson_1975]\] \[[Watts et al 1947][research_watts_mendelson_1947]\] \[[Wei et al 2024][research_wei_xin_2024]\] \[[Wernet et al 2009][research_wernet_locke_2009]\] \[[West et al 1980][research_west_ummel_1980]\] \[[White 1974][research_white_1974]\] \[[Wolf 1999][research_wolf_1999]\] \[[Wolf 2002][research_wolf_2002]\] \[[Wolf 2019][research_wolf_2019]\] \[[Wolf and Fallon 2011][research_wolf_fallon_2011]\] \[[Wolf and Ivanov 2008][research_wolf_ivanov_2008]\] \[[Wong and Mastroianni 1999][research_wong_mastroianni_1999]\] \[[Xiaodong et al 2010][research_xiaodong_guiping_2010]\] \[[Xu et al 2011][research_xu_yang_2011]\] \[[Xue et al 2019][research_xue_luo_2019]\] \[[Xue et al 2019][research_xue_wang_2019]\] \[[Yang 2021][research_yang_2021]\] \[[Yang et al 2018][research_yang_yu_2018]\] \[[Yasumura and Kitamura 2021][research_yasumura_kitamura_2021]\] \[[Ye et al 2026][research_ye_gu_2026]\] \[[Yipton and Blachowski 1996][research_yipton_blachowski_1996]\] \[[Zhang 2003][research_zhang_2003]\] \[[Zhang and Yi 2011][research_zhang_yi_2011]\] \[[Zhang et al 2013][research_zhang_cheng_2013]\] \[[Zhao and Li 2019][research_zhao_li_2019]\] \[[Zhu et al 2024][research_zhu_voo_2024]\]

### Boundary layers, transition and skin friction

**The layer that sets the heating.** Compressible laminar and turbulent boundary layers, transition, shock and boundary-layer interaction, and skin friction at supersonic speed. **Transition is named in 78 titles**, consistent with the article's statement that transition location rather than peak temperature is the quantity the community pursued, because the heating ratio between the two states is an order of magnitude.

**283 records.** \[[Adams 1974][research_adams_1974]\] \[[Adams 1972][research_adamsjr_1972]\] \[[Agarwal 1982][research_agarwal_1982]\] \[[Agrawal et al 1991][research_agrawal_kinard_1991]\] \[[Allee 1976][research_allee_eg_1976]\] \[[Aniskin et al 2015][research_aniskin_mironov_2015]\] \[[Antonov 1971][research_antonov_1971]\] \[[Arai et al 2000][research_arai_noto_2000]\] \[[Archambaud et al 2004][research_archambaud_louis_2004]\] \[[Archambaud et al 2009][research_archambaud_arnal_2009]\] \[[Arnal et al 1990][research_arnal_vignau_1990]\] \[[Arnette et al 1995][research_arnette_samimy_1995]\] \[[Babucke and Rist 2009][research_babucke_rist_2009]\] \[[Bachalo et al 1977][research_bachalo_modarress_1977]\] \[[Banks 2008][research_banks_2008]\] \[[Banks 2008][research_banks_2008_b]\] \[[Banks et al 2012][research_banks_frederick_2012]\] \[[Banks et al 2012][research_banks_fredericks_2012]\] \[[Barnwell 1989][research_barnwell_1989]\] \[[Behrens 1971][research_behrens_1971]\] \[[Bell 1963][research_bell_1963]\] \[[Beresh et al 2010][research_beresh_henfling_2010]\] \[[Berger et al 2011][research_berger_anderson_2011]\] \[[Berry et al 2006][research_berry_horvath_2006]\] \[[Berry et al 2008][research_berry_horvath_2008]\] \[[Bisek and Brown 2015][research_bisek_brown_2015]\] \[[Bogdonoff and Kepler 1955][research_bogdonoff_kepler_1955]\] \[[Brandt and Bons 2024][research_brandt_bons_2024]\] \[[Braslow 1966][research_braslow_1966]\] \[[Brooks 1971][research_brooks_1971]\] \[[Brundrett et al 1972][research_brundrett_nicoll_1972]\] \[[Bui 2013][research_bui_2013]\] \[[Cao et al 2006][research_cao_huang_2006]\] \[[Carpenter et al 2008][research_carpenter_saric_2008]\] \[[Carpenter et al 2009][research_carpenter_saric_2009]\] \[[Chern et al 2014][research_chern_lobser_2014]\] \[[Chou and Childs 1983][research_chou_childs_1983]\] \[[Chuvakhov 2020][research_chuvakhov_2020]\] \[[Coats 1973][research_coats_1973]\] \[[Collier et al 1990][research_collier_bartlett_1990]\] \[[De Tullio et al 2013][research_detullio_paredes_2013]\] \[[Degani and Smits 1985][research_degani_smits_1985]\] \[[Demetriades 1985][research_demetriades_1985]\] \[[DeSpirito 2014][research_despirito_2014]\] \[[DeSpirito 2015][research_despirito_2015]\] \[[Din et al 2018][research_din_egorov_2018]\] \[[Donovan and Smits 1990][research_donovan_smits_1990]\] \[[Dougherty and Fisher 1980][research_dougherty_fisher_1980]\] \[[Dovgal et al 1990][research_dovgal_levchenko_1990]\] \[[Dris and Jamal 2019][research_dris_jamal_2019]\] \[[Ducros et al 1995][research_ducros_comte_1995]\] \[[Effect of uniformly distributed 1959][research_effect_of_1959]\] \[[Egorov 2025][research_egorov_2025]\] \[[Egorov et al 2018][research_egorov_fedorov_2018]\] \[[Ekoto et al 2007][research_ekoto_bowersox_2007]\] \[[Eppink 2023][research_eppink_2023]\] \[[Erlebacher and Hussaini 1990][research_erlebacher_hussaini_1990]\] \[[Fasel et al 2008][research_fasel_husmeier_2008]\] \[[Ferrari 1958][research_ferrari_1958]\] \[[Fezer and Kloker 2000][research_fezer_kloker_2000]\] \[[Fick et al 1996][research_fick_gaitonde_1996]\] \[[Frendi 1996][research_frendi_1996]\] \[[Frendi 1997][research_frendi_1997]\] \[[Ganapathisubramani 2007][research_ganapathisubramani_2007]\] \[[Gaponov 2000][research_gaponov_2000]\] \[[Gaponov et al 1995][research_gaponov_kosinov_1995]\] \[[Gartling 1970][research_gartling_1970]\] \[[Ghosh and Modi 2021][research_ghosh_modi_2021]\] \[[Ghosh and Modi 2021][research_ghosh_modi_2021_b]\] \[[Girgis and Liu 2000][research_girgis_liu_2000]\] \[[Goldfeld and Zatoloka 1985][research_goldfeld_zatoloka_1985]\] \[[Gomez et al 2009][research_gomez_flutet_2009]\] \[[Gromov and Larin 1982][research_gromov_larin_1982]\] \[[Groth 1961][research_groth_1961]\] \[[Guo et al 1994][research_guo_adams_1994]\] \[[Hader and Fasel 2023][research_hader_fasel_2023]\] \[[Hahn and Frendi 2012][research_hahn_frendi_2012]\] \[[Hahn and Frendi 2013][research_hahn_frendi_2013]\] \[[Hallberg et al 2008][research_hallberg_cenko_2008]\] \[[Hamed 1993][research_hamed_1993]\] \[[Hamed and Li 2008][research_hamed_li_2008]\] \[[Han et al 2022][research_han_he_2022]\] \[[Hanine et al 1992][research_hanine_kourta_1992]\] \[[Hayostek and Amitay 2018][research_hayostek_amitay_2018]\] \[[Horstman and Hung 1979][research_horstman_hung_1979]\] \[[Horstman et al 1978][research_horstman_kussoy_1978]\] \[[Hrubecky 1995][research_hrubecky_1995]\] \[[Huang 2005][research_huang_2005]\] \[[Huang and Liou 1994][research_huang_liou_1994]\] \[[Hung and Buning 1985][research_hung_buning_1985]\] \[[Hung and Chaussee 1981][research_hung_chaussee_1981]\] \[[Hung and Maccormack 1978][research_hung_maccormack_1978]\] \[[Inger 1984][research_inger_1984]\] \[[Inger 1985][research_inger_1985]\] \[[Inger 1986][research_inger_1986]\] \[[Inger 1988][research_inger_1988]\] \[[Inger 1995][research_inger_1995]\] \[[Iyer et al 1992][research_iyer_spall_1992]\] \[[Jammalamadaka et al 2014][research_jammalamadaka_li_2014]\] \[[Jayaram et al 1987][research_jayaram_taylor_1987]\] \[[Jiang et al 2006][research_jiang_choudhari_2006]\] \[[Jing-Lei and Hui-Yang 2007][research_jinglei_huiyang_2007]\] \[[Karabis et al 2000][research_karabis_shaw_2000]\] \[[Kegerise et al 2010][research_kegerise_owens_2010]\] \[[Khotyanovsky and Kudryavtsev 2016][research_khotyanovsky_kudryavtsev_2016]\] \[[Kiber 1977][research_kiber_1977]\] \[[Kimmel and Prabhu 2015][research_kimmel_prabhu_2015]\] \[[Kimmel et al 2015][research_kimmel_borg_2015]\] \[[Klineberg et al 1970][research_klineberg_kubota_1970]\] \[[Klopfer and Nielsen 1980][research_klopfer_nielsen_1980]\] \[[Knight 1982][research_knight_1982]\] \[[Knight and Zheltovodov 2011][research_knight_zheltovodov_2011]\] \[[Konrad et al 1992][research_konrad_smits_1992]\] \[[Konrad et al 1993][research_konrad_smits_1993]\] \[[Kosinov et al 1990][research_kosinov_maslov_1990]\] \[[Kosinov et al 2000][research_kosinov_yermolaev_2000]\] \[[Kosinov et al 2000][research_kosinov_yermolaev_2000_b]\] \[[Kosinov et al 2017][research_kosinov_yermolaev_2017]\] \[[Kovalev et al 2015][research_kovalev_kudryavtsev_2015]\] \[[Kozlov et al 2009][research_kozlov_zverkov_2009]\] \[[Krishnan and Sandham 2005][research_krishnan_sandham_2005]\] \[[Ladenburg and Bershader 1949][research_ladenburg_bershader_1949]\] \[[Laderman 1979][research_laderman_1979]\] \[[Laderman and Demetriades 1977][research_laderman_demetriades_1977]\] \[[Laganelli 1970][research_laganelli_1970]\] \[[Law 1974][research_law_1974]\] \[[Law 1975][research_law_1975]\] \[[Law 1976][research_law_1976]\] \[[Lee and Gross 2020][research_lee_gross_2020]\] \[[Lee and Gross 2021][research_lee_gross_2021]\] \[[Lees and Reshotko 1962][research_lees_reshotko_1962]\] \[[Lilley 1965][research_lilley_1965]\] \[[Lipatov and Tugazakov 2018][research_lipatov_tugazakov_2018]\] \[[Liu et al 2021][research_liu_luo_2021]\] \[[Loth and Lee 2008][research_loth_lee_2008]\] \[[Lowe et al 2014][research_lowe_byun_2014]\] \[[Lutz 1989][research_lutz_1989]\] \[[Lysenko 1989][research_lysenko_1989]\] \[[Lysenko 1995][research_lysenko_1995]\] \[[Lysenko and Maslov 1981][research_lysenko_maslov_1981]\] \[[Lysenko and Maslov 1985][research_lysenko_maslov_1985]\] \[[Lysenko et al 2017][research_lysenko_smorodsky_2017]\] \[[Lysenko et al 2025][research_lysenko_smorodsky_2025]\] \[[Mabey and Gaudet 1975][research_mabey_gaudet_1975]\] \[[Maddalon et al 1990][research_maddalon_collier_1990]\] \[[Maestrello 1969][research_maestrello_1969]\] \[[Malik and Li 1993][research_malik_li_1993]\] \[[Manavasi et al 2011][research_manavasi_morell_2011]\] \[[Martin 1953][research_martin_1953]\] \[[Martin 2008][research_martin_2008]\] \[[Mashburn 1969][research_mashburn_1969]\] \[[Maslov et al 2016][research_maslov_aniskin_2016]\] \[[Melvill Jones 1938][research_melvilljones_1938]\] \[[Meyers et al 2025][research_meyers_duong_2025]\] \[[Mi et al 2023][research_mi_yi_2023]\] \[[Mielke and Kleiser 2000][research_mielke_kleiser_2000]\] \[[Mielke et al 1999][research_mielke_kleiser_1999]\] \[[Miner and Lewis 1973][research_miner_lewis_1973]\] \[[Mironov 1965][research_mironov_1965]\] \[[Miyazawa 1973][research_miyazawa_1973]\] \[[Miyazawa 1974][research_miyazawa_1974]\] \[[Monaghan 1953][research_monaghan_1953]\] \[[Morajkar and Gamba 2016][research_morajkar_gamba_2016]\] \[[Lawing 1981][research_hypersonic_heating_survey_1981]\] \[[NASA 1986][research_real_gas_boundary_layer_1986]\] \[[Malik and Anderson 1991][research_real_gas_stability_1991]\] \[[Berry et al 2016][research_blt_shuttle_2016]\] \[[Sasson et al 2022][research_sbli_experiments_2022]\] \[[Ni et al 2016][research_ni_lu_2016]\] \[[Nie et al 2022][research_nie_song_2022]\] \[[Nomura 2003][research_nomura_2003]\] \[[Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952]\] \[[Northrop Aircraft Inc Hawthorne Ca 1953][research_northropaircraftinchawthorneca_1953]\] \[[Novopashin 1985][research_novopashin_1985]\] \[[Ohira et al 2013][research_ohira_kwak_2013]\] \[[Om et al 1982][research_om_childs_1982]\] \[[Oorebeek and Babinsky 2013][research_oorebeek_babinsky_2013]\] \[[Owen 1969][research_owen_1969]\] \[[Padova and Falk 1980][research_padova_falk_1980]\] \[[Patel and Czarnecki 1975][research_patel_czarnecki_1975]\] \[[Patel and Czarnecki 1977][research_patel_czarnecki_1977]\] \[[Pavlyuchenko et al 1985][research_pavlyuchenko_tyutin_1985]\] \[[Peltzer et al 2008][research_peltzer_nitsche_2008]\] \[[Perez et al 2025][research_perez_hader_2025]\] \[[Perraud et al 2003][research_perraud_moens_2003]\] \[[Peters and Phares 1976][research_peters_phares_1976]\] \[[Pizzaia and Rossmann 2018][research_pizzaia_rossmann_2018]\] \[[Polak 1974][research_polak_1974]\] \[[Pressure Fluctuations Underlying Attached 1975][research_pressure_fluctuations_1975]\] \[[Rambacher et al 2024][research_rambacher_butler_2024]\] \[[Rao and Lundgren 1997][research_rao_lundgren_1997]\] \[[Reda 1977][research_reda_1977]\] \[[Redford et al 2009][research_redford_sandham_2009]\] \[[Reibert et al 1997][research_reibert_saric_1997]\] \[[Reichert][research_reichert]\] \[[Reshotko and Khan 1980][research_reshotko_khan_1980]\] \[[Rosen et al 1979][research_rosen_pavish_1979]\] \[[Rosen et al 1980][research_rosen_pavish_1980]\] \[[Rossmann and Pizzaia 2014][research_rossmann_pizzaia_2014]\] \[[Roux and Bontoux 1975][research_roux_bontoux_1975]\] \[[Saida 1986][research_saida_1986]\] \[[Sakaue et al 2000][research_sakaue_asai_2000]\] \[[Samimy et al 1994][research_samimy_arnette_1994]\] \[[Schuelein 2008][research_schuelein_2008]\] \[[Schueler 1963][research_schueler_1963]\] \[[Sedney 1956][research_sedney_1956]\] \[[Semionov and Kosinov 2000][research_semionov_kosinov_2000]\] \[[Semionov et al 2006][research_semionov_kosinov_2006]\] \[[Semionov et al 2009][research_semionov_kosinov_2009]\] \[[Semionov et al 2024][research_semionov_kosinov_2024]\] \[[Settles 1986][research_settles_1986]\] \[[Settles and Bogdonoff 1973][research_settles_bogdonoff_1973]\] \[[Settles et al 1975][research_settles_bogdonoff_1975]\] \[[Shahab et al 2009][research_shahab_lehnasch_2009]\] \[[Sharma][research_sharma]\] \[[Shock Wave-Boundary Layer Interactions][research_shock_wave_boundary]\] \[[Silva-Freire 1988][research_silvafreire_1988]\] \[[Sivasegaram and Whitelaw 1971][research_sivasegaram_whitelaw_1971]\] \[[Smith and Smits 1988][research_smith_smits_1988]\] \[[Smith and Smits 1992][research_smith_smits_1992]\] \[[Smith and Smits 1993][research_smith_smits_1993]\] \[[Smits 1984][research_smits_1984]\] \[[Smits 1985][research_smits_1985]\] \[[Smits 1988][research_smits_1988]\] \[[Soudakov et al 2009][research_soudakov_egorov_2009]\] \[[Spaid 1972][research_spaid_1972]\] \[[Speziale and Sarkar 1991][research_speziale_sarkar_1991]\] \[[Spring 1972][research_spring_1972]\] \[[Spyropoulos and Blaisdell 1998][research_spyropoulos_blaisdell_1998]\] \[[Stallings 1982][research_stallingsjr_1982]\] \[[Stockbridge 1988][research_stockbridge_1988]\] \[[Sturek 1973][research_sturek_1973]\] \[[Su et al 2024][research_su_long_2024]\] \[[Sun and Childs 1975][research_sun_childs_1975]\] \[[Sun and Childs 1976][research_sun_childs_1976]\] \[[Sun et al 2017][research_sun_hu_2017]\] \[[Sun et al 2020][research_sun_yang_2020]\] \[[Teramoto et al 2017][research_teramoto_sanada_2017]\] \[[Thomas and Fan 1971][research_thomas_fan_1971]\] \[[Three-dimensional boundary-layer transition on 1994][research_three_dimensional_boundary_layer_1994]\] \[[Tokugawa and Yoshida 2006][research_tokugawa_yoshida_2006]\] \[[Tourbier and Fasel 1994][research_tourbier_fasel_1994]\] \[[Turbulent SPOT in the 2024][research_turbulent_spot_in_2024]\] \[[Urbin et al 1999][research_urbin_knight_1999]\] \[[Ustinov 2013][research_ustinov_2013]\] \[[Van Driest and Blumer 1961][research_vandriest_blumer_1961]\] \[[Vandromme and Zeman 1992][research_vandromme_zeman_1992]\] \[[Vigdorovich 2023][research_vigdorovich_2023]\] \[[Vigdorovich 2023][research_vigdorovich_2023_b]\] \[[Vigdorovich 2024][research_vigdorovich_2024]\] \[[Vigdorovich 2025][research_vigdorovich_2025]\] \[[von Terzi et al 2009][research_vonterzi_mayer_2009]\] \[[Waindim et al 2014][research_waindim_gaitonde_2014]\] \[[Wainwright 1962][research_wainwright_1962]\] \[[Waltrup and Schetz 1972][research_waltrup_schetz_1972]\] \[[Waltrup and Schetz 1973][research_waltrup_schetz_1973]\] \[[Wang 1993][research_wang_1993]\] \[[Wang and Wang 2016][research_wang_wang_2016]\] \[[Wang et al 1994][research_wang_herbert_1994]\] \[[Wang et al 2016][research_wang_wang_2016_b]\] \[[Wang et al 2025][research_wang_tu_2025]\] \[[Warren et al 1997][research_warren_hassan_1997]\] \[[Waskiewicz et al 1981][research_waskiewicz_dejongh_1981]\] \[[Watmuff and Smits 1987][research_watmuff_smits_1987]\] \[[Wentz and Nyenhuis 1984][research_wentzjr_nyenhuis_1984]\] \[[Wilcox 1991][research_wilcoxjr_1991]\] \[[Wilson 1950][research_wilson_1950]\] \[[Wilson and Maurer 1971][research_wilson_maurer_1971]\] \[[Wu and Martin 2007][research_wu_martin_2007]\] \[[Wu et al 2019][research_wu_liang_2019]\] \[[Xiao et al 2025][research_xiao_wu_2025]\] \[[Xiao et al 2026][research_xiao_wu_2026]\] \[[Yamane et al 1997][research_yamane_ishihara_1997]\] \[[Yao and Hussain 2019][research_yao_hussain_2019]\] \[[Yatskikh et al 2018][research_yatskikh_kosinov_2018]\] \[[Yu et al 2023][research_yu_dong_2023]\] \[[Yuan and Zhou 2000][research_yuan_zhou_2000]\] \[[Zalovcik 1945][research_zalovcik_1945]\] \[[Zhao et al 2025][research_zhao_wu_2025]\] \[[Zheltovodov and Knight 2011][research_zheltovodov_knight_2011]\] \[[Zheltovodov et al 1985][research_zheltovodov_pavlov_1985]\] \[[Znamenskaya et al 2008][research_znamenskaya_latfullin_2008]\] \[[Zoppini et al 2022][research_zoppini_ragni_2022]\]

### Inertia coupling, roll coupling and departure

**The phenomenon that ended the programme, under the name the field now gives it.** Inertia and roll coupling, departure and spin, bifurcation analysis of aircraft dynamics, and loss of control and upset recovery. **The coupling literature has become a loss-of-control literature.** Of its 234 titles, 151 name loss of control or upset and 26 name bifurcation. **Its median publication year of 2012 is the latest of any cluster**, which agrees with the review's statement that the coupling thread has moved further than the thermal one.

**234 records.** \[[A'Harrah 2007][research_aharrah_2007]\] \[[Abdelkefi et al 2011][research_abdelkefi_vasconcellos_2011]\] \[[Advani and Field 2011][research_advani_field_2011]\] \[[Advani et al 2016][research_advani_schroeder_2016]\] \[[AHarrah 2007][research_aharrah_2007_b]\] \[[Air Force Test Pilot School Edwards Afb Ca 1989][research_airforcetestpilotschooledwardsafbca_1989]\] \[[Akcal et al 2018][research_akcal_hostas_2018]\] \[[Altunkaya and Catak 2025][research_altunkaya_2025]\] \[[Askari and Cremaschi 2023][research_askari_2023]\] \[[Avanzini and Matteis 1997][research_avanzini_matteis_1997]\] \[[Baghdadi et al 2009][research_baghdadi_lowenberg_2009]\] \[[Baghdadi et al 2011][research_baghdadi_lowenberg_2011]\] \[[Bajpai et al 2008][research_bajpai_beytin_2008]\] \[[Balachandran and Atkins 2014][research_balachandran_atkins_2014]\] \[[Balachandran and Atkins 2016][research_balachandran_atkins_2016]\] \[[Barlow et al 2012][research_barlow_stepanyan_2012]\] \[[Bateman 2010][research_bateman_2010]\] \[[Belcastro][research_belcastro]\] \[[Belcastro 2011][research_belcastro_2011]\] \[[Belcastro 2012][research_belcastro_2012]\] \[[Belcastro 2012][research_belcastro_2012_b]\] \[[Belcastro and Foster 2010][research_belcastro_foster_2010]\] \[[Belcastro and Jacobson 2010][research_belcastro_jacobson_2010]\] \[[Belcastro et al 2005][research_belcastro_khong_2005]\] \[[Belcastro et al 2005][research_belcastro_khong_2005_b]\] \[[Belcastro et al 2016][research_belcastro_newman_2016]\] \[[Bigler 1986][research_bigler_1986]\] \[[Bihrle and Barnhart 1982][research_bihrle_barnhart_1982]\] \[[Boskovic et al 2005][research_boskovic_bergstrom_2005]\] \[[Bowman et al 1978][research_bowmanjr_stough_1978]\] \[[Brenner et al 2005][research_brenner_thompson_2005]\] \[[Brincklow et al 2021][research_brincklow_montgomery_2021]\] \[[Brincklow et al 2024][research_brincklow_montgomery_2024]\] \[[Bromfield and Landry 2019][research_bromfield_landry_2019]\] \[[Brooks and Ransbury 2012][research_brooks_ransbury_2012]\] \[[Burki-Cohen 2010][research_burkicohen_2010]\] \[[Burris and Hutchins 1970][research_burris_hutchins_1970]\] \[[Bürki-Cohen and Sparko 2008][research_burkicohen_sparko_2008]\] \[[Campbell et al][research_campbell_grauer]\] \[[Campbell et al 2021][research_campbell_grauer_2021]\] \[[Campbell et al 2021][research_campbell_grauer_2021_b]\] \[[Cano and Sobel 2016][research_cano_sobel_2016]\] \[[Cao and Yao 2019][research_cao_yao_2019]\] \[[Cao et al 2020][research_cao_yao_2020]\] \[[Carbaugh 2008][research_carbaugh_2008]\] \[[Carroll 2015][research_carroll_2015]\] \[[Carroll and Mehra 1982][research_carroll_mehra_1982]\] \[[Cen et al 2020][research_cen_li_2020]\] \[[Chan and Chang][research_chan_chang]\] \[[Chang et al 2008][research_chang_kwatny_2008]\] \[[Chang et al 2016][research_chang_kwatny_2016]\] \[[Chapman et al 2024][research_chapman_robb_2024]\] \[[Charles et al 2002][research_charles_lowenberg_2002]\] \[[Chung and Chung 2008][research_chung_chung_2008]\] \[[Comtois and Glaser 2010][research_comtois_glaser_2010]\] \[[Cox 2010][research_cox_2010]\] \[[Cox et al 2012][research_cox_cunningham_2012]\] \[[Crespo et al 2012][research_crespo_kenny_2012]\] \[[Crider 2008][research_crider_2008]\] \[[Crider 2010][research_crider_2010]\] \[[Crider 2010][research_crider_2010_b]\] \[[Cunis][research_cunis]\] \[[Cunis 2025][research_cunis_2025]\] \[[Cunis et al 2020][research_cunis_liaomcpherson_2020]\] \[[Dantsker et al 2017][research_dantsker_ananda_2017]\] \[[Das 2026][research_das_2026]\] \[[Dillman and Stanley 2003][research_dillman_stanley_2003]\] \[[Dongmo 2011][research_dongmo_2011]\] \[[Dongmo 2011][research_dongmo_2011_b]\] \[[Dongmo 2012][research_dongmo_2012]\] \[[Dongmo 2012][research_dongmo_2012_b]\] \[[Dongmo 2015][research_dongmo_2015]\] \[[Dongmo 2015][research_dongmo_2015_b]\] \[[Dongmo 2016][research_dongmo_2016]\] \[[Dongmo 2017][research_dongmo_2017]\] \[[Dutoi et al 2008][research_dutoi_richards_2008]\] \[[Engelbrecht et al 2013][research_engelbrecht_pauck_2013]\] \[[Etherington et al 2020][research_etherington_kramer_2020]\] \[[Fan et al 2017][research_fan_liu_2017]\] \[[Ferranti et al 2015][research_ferranti_wan_2015]\] \[[Foster and Shah][research_foster_shah]\] \[[Frink et al 2016][research_frink_murphy_2016]\] \[[Fu et al 2024][research_fu_shi_2024]\] \[[Fuller 2012][research_fuller_2012]\] \[[Gandhi et al 2012][research_gandhi_richards_2012]\] \[[Gandhi et al 2014][research_gandhi_richards_2014]\] \[[Garcia et al 2015][research_garcia_keshmiri_2015]\] \[[Gill et al 2012][research_gill_lowenberg_2012]\] \[[Gillis 1957][research_gillis_1957]\] \[[Glaser and McCarthy 2012][research_glaser_mccarthy_2012]\] \[[Groen Eric and Fucke Lars 2012][research_groeneric_fuckelars_2012]\] \[[Hacker and Oprişiu 1974][research_hacker_oprisiu_1974]\] \[[Hale et al 2015][research_hale_patil_2015]\] \[[Heald and Brassell 1976][research_heald_brassell_1976]\] \[[Hess 2013][research_hess_2013]\] \[[Holloway and Johnson 2008][research_holloway_johnson_2008]\] \[[Holzinger and Cunis 2024][research_holzinger_cunis_2024]\] \[[Hreha and Lutze 1983][research_hreha_lutze_1983]\] \[[Hreha and Lutze 1984][research_hreha_lutze_1984]\] \[[Huang et al 2021][research_huang_fu_2021]\] \[[Hui and Tobak 1982][research_hui_tobak_1982]\] \[[Hyde et al 2018][research_hyde_brown_2018]\] \[[Inertia Coupling and Spin 2004][research_inertia_coupling_2004]\] \[[Inertia Coupling and Spin 2015][research_inertia_coupling_2015]\] \[[Jacobson 2010][research_jacobson_2010]\] \[[Jacobson 2010][research_jacobson_2010_b]\] \[[Jayaraman et al 2022][research_jayaraman_saini_2022]\] \[[Ji et al 2011][research_ji_wang_2011]\] \[[Johnston and Hogge 1974][research_johnston_hogge_1974]\] \[[Johnston and Hogge 1976][research_johnston_hogge_1976]\] \[[Kasdaglis et al 2016][research_kasdaglis_bernard_2016]\] \[[Khatri and Sinha 2011][research_khatri_sinha_2011]\] \[[Khatri and Subbarao 2024][research_khatri_subbarao_2024]\] \[[Khot et al 1997][research_khot_eastep_1997]\] \[[Khrabrov et al 2013][research_khrabrov_sidoryuk_2013]\] \[[Klyde and McRuer 2008][research_klyde_mcruer_2008]\] \[[Klyde et al 2004][research_klyde_thompson_2004]\] \[[Klyde et al 2011][research_klyde_liang_2011]\] \[[Klyde et al 2014][research_klyde_lampton_2014]\] \[[Klyde et al 2017][research_klyde_lampton_2017]\] \[[Ko and Grant 2012][research_ko_grant_2012]\] \[[Kochan et al 2005][research_kochan_breiter_2005]\] \[[Kogler and Quam 1983][research_kogler_quam_1983]\] \[[Koopman and Zammit-Mangion 2025][research_koopman_zammitmangion_2025]\] \[[Kwatny et al 2008][research_kwatny_belcastro_2008]\] \[[Kwatny et al 2009][research_kwatny_dongmo_2009]\] \[[Kwatny et al 2010][research_kwatny_dongmo_2010]\] \[[Lang et al 2022][research_lang_cen_2022]\] \[[Le Vie 2016][research_levie_2016]\] \[[Liang et al 2022][research_liang_yang_2022]\] \[[Litt et al 2014][research_litt_liu_2014]\] \[[Littleboy et al 1997][research_littleboy_smith_1997]\] \[[Liu and Grant 2009][research_liu_grant_2009]\] \[[Liu and Grant 2010][research_liu_grant_2010]\] \[[Logan et al 2007][research_logan_davis_2007]\] \[[Lombaerts 2019][research_lombaerts_2019]\] \[[Lombaerts et al 2016][research_lombaerts_schuet_2016]\] \[[Loss-of-Control Mishaps in Revenue][research_loss_of_control_mishaps]\] \[[Macedo][research_macedo]\] \[[Macedo et al 2020][research_macedo_bidinotto_2020]\] \[[MacMillen and Thompson 1999][research_macmillen_thompson_1999]\] \[[Matsushita et al][research_matsushita_miyata]\] \[[McDonough and Kolmanovsky 2017][research_mcdonough_kolmanovsky_2017]\] \[[McDonough et al 2014][research_mcdonough_kolmanovsky_2014]\] \[[Mehra and Carroll 1980][research_mehra_carroll_1980]\] \[[Moore et al 1980][research_moore_skow_1980]\] \[[Morelli et al 2013][research_morelli_cunningham_2013]\] \[[Mukherjee and Sinha 2016][research_mukherjee_sinha_2016]\] \[[Mumaw et al 2019][research_mumaw_haworth_2019]\] \[[Murri et al 1983][research_murri_croom_1983]\] \[[Sadoff and Sisk 1950][research_x4_stall_1950]\] \[[Jacobsen and Greif 1972][research_lift_roll_coupling_1972]\] \[[Sharpes and Carroll 1973][research_roll_coupling_balance_1973]\] \[[Hong 1993][research_wing_rock_delta_1993]\] \[[Cunningham et al 2008][research_subscale_upset_2008]\] \[[Belcastro 2014][research_loc_directions_2014]\] \[[Belcastro et al 2014][research_loc_precursors_2014]\] \[[Nguyen 1979][research_nguyen_1979]\] \[[Nguyen et al 2021][research_nguyen_lowenberg_2021]\] \[[Ni et al 2025][research_ni_wang_2025]\] \[[Pauck and Engelbrecht 2012][research_pauck_engelbrecht_2012]\] \[[Pinsky and Essary 1994][research_pinsky_essary_1994]\] \[[Poolla and Ishihara 2015][research_poolla_ishihara_2015]\] \[[Pourtakdoust and Fazelzadeh 2003][research_pourtakdoust_fazelzadeh_2003]\] \[[Priest et al 2010][research_priest_ernisse_2010]\] \[[Pugh et al 2023][research_pugh_goman_2023]\] \[[Qiu et al 2021][research_qiu_dai_2021]\] \[[Rafi et al 2017][research_rafi_steck_2017]\] \[[Rafi et al 2019][research_rafi_steck_2019]\] \[[Rafi et al 2020][research_rafi_steck_2020]\] \[[Rafi et al 2021][research_rafi_steck_2021]\] \[[Rajaram et al 2017][research_rajaram_rafi_2017]\] \[[Ransbury and Carroll 2014][research_ransbury_carroll_2014]\] \[[Reuter et al][research_reuter_mcgehee]\] \[[Rhodeside 1986][research_rhodeside_1986]\] \[[Richards et al 2012][research_richards_gandhi_2012]\] \[[Richards et al 2016][research_richards_gandhi_2016]\] \[[Richards et al 2018][research_richards_gandhi_2018]\] \[[Roemer et al 2011][research_roemer_ge_2011]\] \[[Rolling Maneuvers 1996][research_rolling_maneuvers_1996]\] \[[Roux and Cruciani 2007][research_roux_cruciani_2007]\] \[[Sayyed et al 2025][research_sayyed_konar_2025]\] \[[Schlimm 2015][research_schlimm_2015]\] \[[Schmidt and Wright 1991][research_schmidt_wright_1991]\] \[[Schnell et al 2006][research_schnell_keller_2006]\] \[[Schroeder 2012][research_schroeder_2012]\] \[[Schroeder 2016][research_schroeder_2016]\] \[[Schuet et al 2017][research_schuet_lombaerts_2017]\] \[[Setoguchi and Kanazaki 2020][research_setoguchi_kanazaki_2020]\] \[[Shams and Noorian 2025][research_shams_noorian_2025]\] \[[Shearwood et al 2021][research_shearwood_nabawy_2021]\] \[[Shen et al 2019][research_shen_huang_2019]\] \[[Smaili et al 2017][research_smaili_breeman_2017]\] \[[Snell et al 1991][research_snell_garrardjr_1991]\] \[[Sparks and Moerder 2002][research_sparks_moerder_2002]\] \[[Stanford 2022][research_stanford_2022]\] \[[Stanford 2023][research_stanford_2023]\] \[[Stone 1957][research_stone_1957]\] \[[Suarez et al 1992][research_suarez_kramer_1992]\] \[[Summers et al 2006][research_summers_burkholder_2006]\] \[[Tang 2019][research_tang_2019]\] \[[Temgoua Dongmo and Kwatny][research_temgouadongmo_kwatny]\] \[[Thomas et al 2005][research_thomas_bajpai_2005]\] \[[Thompson et al 2004][research_thompson_klyde_2004]\] \[[Tinger 1987][research_tinger_1987]\] \[[Tobak and Schiff 1974][research_tobak_schiff_1974]\] \[[Tobak and Schiff 1975][research_tobak_schiff_1975]\] \[[Tobak and Schiff 1975][research_tobak_schiff_1975_b]\] \[[Tong et al 2023][research_tong_zhou_2023]\] \[[Tu et al 2024][research_tu_yan_2024]\] \[[Uribe Quintero et al 2024][research_uribequintero_takahashi_2024]\] \[[Urnes and Smith 2011][research_urnes_smith_2011]\] \[[Wadley et al 2005][research_wadley_hopper_2005]\] \[[Wang 2011][research_wang_2011]\] \[[Weissman 1972][research_weissman_1972]\] \[[Weissman 1973][research_weissman_1973]\] \[[Weissman 1975][research_weissman_1975]\] \[[Wilborn and Foster 2004][research_wilborn_foster_2004]\] \[[Wu et al 2020][research_wu_li_2020]\] \[[Wu et al 2021][research_wu_zhao_2021]\] \[[Wykes 1957][research_wykes_1957]\] \[[Xin and Shi 2016][research_xin_shi_2016]\] \[[Xu et al 2019][research_xu_yue_2019]\] \[[Xu and Zhang 2020][research_xu_zhang_2020]\] \[[Yildiz et al 2019][research_yildiz_akcal_2019]\] \[[Yildiz et al 2018][research_yildiz_akcal_2018]\] \[[Zaichik et al 2019][research_zaichik_yashin_2019]\] \[[Zhang and Chen 2016][research_zhang_chen_2016]\] \[[Zhao and Jim Zhu 2017][research_zhao_jimzhu_2017]\] \[[Zhao and Zhu 2016][research_zhao_zhu_2016]\] \[[Zhao and Zhu 2016][research_zhao_zhu_2016_b]\] \[[Zhao and Zhu 2016][research_zhao_zhu_2016_c]\] \[[Zhou et al 2017][research_zhou_yang_2017]\] \[[Zohar and Er-El 1988][research_zohar_erel_1988]\]

### Instrumentation and measurement at temperature

**What the programme existed to measure, and with what.** Thermocouples and their response, high-temperature strain gauges, flight instrumentation, air data and boundary-layer measurement in flight. **Strain measurement is named in 60 titles**, which bears out the article's statement that strain gauging a hot structure is itself a research problem.

**167 records.** \[[A Thermocouple for Transient 1962][research_a_thermocouple_1962]\] \[[Aerodynamic and Landing Measurements 1960][research_aerodynamic_and_1960]\] \[[Agarwal et al 1992][research_agarwal_miley_1992]\] \[[Ahmed et al 1989][research_ahmed_wentz_1989]\] \[[Allen 1972][research_allen_1972]\] \[[Allen 2004][research_allen_2004]\] \[[Anderson et al 2010][research_anderson_campbell_2010]\] \[[Baer 1966][research_baer_1966]\] \[[Bagheri et al 1990][research_bagheri_strataridakis_1990]\] \[[Bauerle 1961][research_bauerle_1961]\] \[[Blanchard et al 1996][research_blanchard_wilmoth_1996]\] \[[Blue and Low 1953][research_blue_low_1953]\] \[[Brittain 1989][research_brittain_1989]\] \[[Brooks et al 2017][research_brooks_gupta_2017]\] \[[Cagáň et al 2015][research_cagan_rosa_2015]\] \[[Campbell et al 2012][research_campbell_berger_2012]\] \[[Chen 1993][research_chen_1993]\] \[[Clark et al 2007][research_clark_jones_2007]\] \[[Collier et al 1987][research_collier_johnson_1987]\] \[[Compensated High Temperature Strain 1994][research_compensated_high_1994]\] \[[Connelly 1982][research_connelly_1982]\] \[[Covington 1966][research_covington_1966]\] \[[Davis et al 2015][research_davis_pedrazzani_2015]\] \[[Day and Guthrie 1958][research_day_guthrie_1958]\] \[[Demetriades and McCullough 1985][research_demetriades_mccullough_1985]\] \[[Driftmyer 1988][research_driftmyer_1988]\] \[[E et al 2026][research_e_fan_2026]\] \[[Effects of Atmospheric Structure 1979][research_effects_of_1979]\] \[[Ferris 1973][research_ferris_1973]\] \[[Fisher 1969][research_fisher_1969]\] \[[Fisher and Dougherty 1982][research_fisher_dougherty_1982]\] \[[Flight Measurements of Tile 1983][research_flight_measurements_1983]\] \[[Fulmer and Wirtz 1964][research_fulmer_wirtz_1964]\] \[[Gerlach 1965][research_gerlach_1965]\] \[[Gillette and Vaughn 1968][research_gillette_vaughn_1968]\] \[[Goett and Bicknell 1939][research_goett_bicknell_1939]\] \[[Gonzalez 1977][research_gonzalez_1977]\] \[[Gregorek et al 1977][research_gregorek_hoffmann_1977]\] \[[Gregory and You 2011][research_gregory_you_2011]\] \[[Grindrod and Noden 1968][research_grindrod_noden_1968]\] \[[Guide for High-Temperature Static][research_guide_for]\] \[[Haglaga 1970][research_haglaga_1970]\] \[[Hao et al 2026][research_hao_kong_2026]\] \[[Harris 1972][research_harris_1972]\] \[[Harris and Bartlett 1972][research_harris_bartlett_1972]\] \[[Hasehemian 1986][research_hasehemian_1986]\] \[[Havener 1985][research_havener_1985]\] \[[Herring 2009][research_herring_2009]\] \[[High temperature resistance strain 1975][research_high_temperature_1975]\] \[[High-Temperature, Thin-Film Strain Gages 2005][research_high_temperature_thin_film_2005]\] \[[Holmes and Moore 1992][research_holmes_moore_1992]\] \[[Horstman and Kussoy 1967][research_horstman_kussoy_1967]\] \[[Hudson 1989][research_hudson_1989]\] \[[Hulse et al 1984][research_hulse_bailey_1984]\] \[[Hulse et al 1985][research_hulse_bailey_1985]\] \[[Hulse et al 1987][research_hulse_bailey_1987]\] \[[Hulse et al 1991][research_hulse_bailey_1991]\] \[[Jacobsen 1974][research_jacobsen_1974]\] \[[Jacobsen 1977][research_jacobsen_1977]\] \[[Johnson 1988][research_johnson_1988]\] \[[Jun and Kochan 2014][research_jun_kochan_2014]\] \[[Jun et al 2017][research_jun_kochan_2017]\] \[[Jurado and McGehee 2019][research_jurado_mcgehee_2019]\] \[[Kalkhoran and Otugen 1994][research_kalkhoran_otugen_1994]\] \[[Kambiz Farahmand 2001][research_kambizfarahmandjonathanwkaufm_2001]\] \[[Kayser et al 1986][research_kayser_clay_1986]\] \[[Kistler 1959][research_kistler_1959]\] \[[Knapp et al 1953][research_knapp_jordan_1953]\] \[[Kochan 2020][research_kochan_2020]\] \[[Korsun et al 2023][research_korsun_om_2023]\] \[[Kwak et al 2006][research_kwak_yoshida_2006]\] \[[Lam and Stollenwerk 1966][research_lam_stollenwerk_1966]\] \[[Latif et al 2007][research_latif_masud_2007]\] \[[Law 1973][research_law_1973]\] \[[Lei 1987][research_lei_1987]\] \[[Lei 1991][research_lei_1991]\] \[[Lei 1992][research_lei_1992]\] \[[Lei 1992][research_lei_1992_b]\] \[[Lei 1994][research_lei_1994]\] \[[Lei and Williams 1990][research_lei_williams_1990]\] \[[Lei et al 1993][research_lei_fichtel_1993]\] \[[Lei et al 1996][research_lei_castelli_1996]\] \[[Lemcoe 1973][research_lemcoe_1973]\] \[[Lemcoe 1992][research_lemcoe_1992]\] \[[Lewis and Banner 1971][research_lewis_banner_1971]\] \[[Li et al 2018][research_li_zhang_2018]\] \[[Lindley 1956][research_lindley_1956]\] \[[Liu and Li 2021][research_liu_li_2021]\] \[[Liu et al 2023][research_liu_pang_2023]\] \[[Loposer and Rumsey 1954][research_loposer_rumsey_1954]\] \[[Martina 1958][research_martina_1958]\] \[[Martos et al 2011][research_martos_kiszely_2011]\] \[[McElderry 1973][research_mcelderry_1973]\] \[[Meritt et al 2017][research_meritt_schetz_2017]\] \[[Miniature high temperature strain 1972][research_miniature_high_1972]\] \[[Minkina 1999][research_minkina_1999]\] \[[Miura et al 1983][research_miura_fukai_1983]\] \[[Moore 1991][research_moore_1991]\] \[[Hasel and Coletti 1948][research_pitot_supersonic_1948]\] \[[Thompson et al 1950][research_airspeed_calibration_1950]\] \[[Saltzman 1953][research_x1_liftdrag_1953]\] \[[Day 1953][research_x2_glide_1953]\] \[[Banner et al 1958][research_transition_flight_1958]\] \[[McKay 1959][research_x15_first_landing_1959]\] \[[Reed and Watts 1961][research_x15_skin_temps_1961]\] \[[Jenkins and Kuhl 1977][research_loads_calibration_1977]\] \[[NASA 1979][research_yf12_strain_gauges_1979]\] \[[Ouhabi and Narsipur 2025][research_ouhabi_narsipur_2025]\] \[[Pereira and Roberts 1997][research_pereira_roberts_1997]\] \[[Pieniazek 2025][research_pieniazek_2025]\] \[[Pitts and Murbach 1982][research_pitts_murbach_1982]\] \[[Podnebesnov 1984][research_podnebesnov_1984]\] \[[Pohuliaiko and Vernyhora 2026][research_pohuliaiko_vernyhora_2026]\] \[[Porter 1965][research_porter_1965]\] \[[Qian et al 2026][research_qian_tang_2026]\] \[[Quinn and Gong 1978][research_quinn_gong_1978]\] \[[Reardon 1989][research_reardon_1989]\] \[[Rechter and Harada 1961][research_rechter_harada_1961]\] \[[Rizzi et al 1997][research_rizzi_delvo_1997]\] \[[Rohrbach and Knublauch 1968][research_rohrbach_knublauch_1968]\] \[[Ruban et al 1991][research_ruban_fot_1991]\] \[[Sanderson 1965][research_sanderson_1965]\] \[[Sawada and Nishiwaki 1991][research_sawada_nishiwaki_1991]\] \[[Schafer 1962][research_schafer_1962]\] \[[Schmidt 1988][research_schmidt_1988]\] \[[Schreyer et al 2009][research_schreyer_gaisbauer_2009]\] \[[Sewell and Chew 1994][research_sewell_chew_1994]\] \[[Sharpe 1975][research_sharpe_1975]\] \[[Sharpe and Oh 2003][research_sharpe_oh_2003]\] \[[Smart et al 1994][research_smart_kalkhoran_1994]\] \[[Stewart 1958][research_stewart_1958]\] \[[Stubblefield et al 2025][research_stubblefield_kunz_2025]\] \[[Study of thermocouple transient 2019][research_study_of_thermocouple_2019]\] \[[Su et al 1992][research_su_gilbert_1992]\] \[[Takahashi et al 2026][research_takahashi_2026_airdata]\] \[[Takegawa and Furuichi 2022][research_takegawa_furuichi_2022]\] \[[The analysis of thermocouple 2018][research_the_analysis_of_2018]\] \[[Tian et al 2026][research_tian_pan_2026]\] \[[vanDam et al 1995][research_vandam_los_1995]\] \[[Veresnikov and Goncharenko 2025][research_veresnikov_goncharenko_2025]\] \[[Vijgen et al 1992][research_vijgen_hardin_1992]\] \[[Vranas 1976][research_vranas_1976]\] \[[Walter and Redman 1954][research_walter_redman_1954]\] \[[Wang et al 2025][research_wang_zong_2025]\] \[[Washington and Humphrey 1969][research_washington_humphrey_1969]\] \[[Weiss et al 2022][research_weiss_staudacher_2022]\] \[[Westphal et al 2006][research_westphal_bleazard_2006]\] \[[Williams 1965][research_williams_1965]\] \[[Wilson 1971][research_wilson_1971]\] \[[Wilson 1973][research_wilson_1973]\] \[[Wilson and Egger 1975][research_wilson_egger_1975]\] \[[Wnuk et al 1990][research_wnuk_wnuk_1990]\] \[[Wolf and Bossert 2001][research_wolf_bossert_2001]\] \[[Wright and Zoby 1977][research_wright_zoby_1977]\] \[[Xi et al 2020][research_xi_wanqing_2020]\] \[[Xie et al 2024][research_xie_cui_2024]\] \[[Xu et al 2017][research_xu_tian_2017]\] \[[Yakovenko and Fedosov 2025][research_yakovenko_fedosov_2025]\] \[[Yang et al 2020][research_yang_yu_2020]\] \[[Yanta et al 1989][research_yanta_collier_1989]\] \[[Zhang and Liu 2014][research_zhang_liu_2014]\] \[[Zhang et al 2018][research_zhang_shao_2018]\] \[[Zhao et al 2025][research_zhao_zhang_2025]\] \[[Zhao et al 2023][research_zhao_zhang_2023]\] \[[Zhao et al 2024][research_zhao_li_2024]\] \[[Zhao et al 2025][research_zhao_wan_2025]\] \[[Ziegler 1988][research_ziegler_1988]\]

### Stability augmentation, flight control and envelope protection

**The remedy the community adopted.** Stability augmentation systems, yaw and pitch dampers, flight control systems and the handling qualities of augmented aircraft, which is the route of artificial stabilization the article describes as taken after the X-2.

**131 records.** \[[Aircraft Flight Control Systems][research_aircraft_flight]\] \[[Analysis of the Stability 2024][research_analysis_of_the_2024]\] \[[Arnold 1968][research_arnold_1968]\] \[[Ashkenas 1965][research_ashkenas_1965]\] \[[Aslam et al 2025][research_aslam_islam_2025]\] \[[Attinello 1956][research_attinello_1956]\] \[[Automatic flight control system 2000][research_automatic_flight_2000]\] \[[Babinsky 2007][research_babinsky_2007]\] \[[Baer-Riedhart 1981][research_baerriedhart_1981]\] \[[Barbosa et al 2019][research_barbosa_bertolin_2019]\] \[[Beldica and Hilton 1999][research_beldica_hilton_1999]\] \[[Bengtson et al 1975][research_bengtson_dickovich_1975]\] \[[Berry and Powers 1970][research_berry_powers_1970]\] \[[Berry et al 1976][research_berry_mallick_1976]\] \[[Bolton and Collins 1975][research_bolton_collins_1975]\] \[[Burcham and Burken 1994][research_burchamjr_burken_1994]\] \[[Burcham and Pappas 1996][research_burchamjr_pappas_1996]\] \[[Burcham et al 1993][research_burchamjr_maine_1993]\] \[[Burton and Kneeland 1981][research_burton_kneelandjr_1981]\] \[[Carlin and Blair 1983][research_carlin_blair_1983]\] \[[Carpentieri Rona et al 2018][research_carpentierirona_gonzalezramirez_2018]\] \[[Cheng et al 2003][research_cheng_rizer_2003]\] \[[Chipman et al 1982][research_chipman_zislin_1982]\] \[[Crosby and Griffith 1969][research_crosby_griffith_1969]\] \[[Curtiss 1971][research_curtiss_1971]\] \[[de Carvalho Pereira and Júnior 2003][research_decarvalhopereira_junior_2003]\] \[[Dempster and Arnold 1969][research_dempster_arnold_1969]\] \[[Dempster and Roger 1967][research_dempster_roger_1967]\] \[[Dobos-Bubno and Hartsook 1977][research_dobosbubno_hartsook_1977]\] \[[Driscoll 1966][research_driscoll_1966]\] \[[Fosdick 1970][research_fosdick_1970]\] \[[Frampton et al 1995][research_frampton_clark_1995]\] \[[Garren 1962][research_garren_1962]\] \[[Gera et al 1981][research_gera_wilson_1981]\] \[[Griffin and Eastep 1981][research_griffin_eastep_1981]\] \[[Griffith and Crosby 1970][research_griffith_crosby_1970]\] \[[Ground and flight testing 2000][research_ground_and_2000]\] \[[Guiler][research_guiler]\] \[[Hart 1956][research_hart_1956]\] \[[Hess 1997][research_hess_1997]\] \[[Hess and Hess 1997][research_hess_hess_1997]\] \[[Hoh et al 1981][research_hoh_myers_1981]\] \[[Horsnell 1967][research_horsnell_1967]\] \[[Hu et al 2021][research_hu_ferrari_2021]\] \[[Islam et al 2025][research_islam_ali_2025]\] \[[Jeffrie and Rolston 1972][research_jeffrie_rolston_1972]\] \[[Jines 1983][research_jines_1983]\] \[[Johnson and Weir 1969][research_johnson_weir_1969]\] \[[Johnston et al 1974][research_johnston_ashkenas_1974]\] \[[Kaloust 2002][research_kaloust_2002]\] \[[Kannan and Bhat 2005][research_kannan_bhat_2005]\] \[[Kass 1970][research_kass_1970]\] \[[Kehrer 1971][research_kehrer_1971]\] \[[Kempel et al 1988][research_kempel_mcneill_1988]\] \[[Kempel et al 1988][research_kempel_mcneill_1988_b]\] \[[Kohlman 1977][research_kohlman_1977]\] \[[Korbahti 2009][research_korbahti_2009]\] \[[Krishnaswamy et al][research_krishnaswamy_papageorgiou]\] \[[Lada and Kontis 2005][research_lada_kontis_2005]\] \[[Lada and Kontis 2009][research_lada_kontis_2009]\] \[[Lang et al 2025][research_lang_wang_2025]\] \[[Larsen et al 1963][research_larsen_litz_1963]\] \[[Lavretsky 2019][research_lavretsky_2019]\] \[[Lotze et al 1975][research_lotze_sensburg_1975]\] \[[Lotze et al 1977][research_lotze_sensburg_1977]\] \[[Mansor et al 2015][research_mansor_nogoud_2015]\] \[[Mao and Liang 2019][research_mao_liang_2019]\] \[[May et al 2023][research_may_li_2023]\] \[[McKee 1967][research_mckee_1967]\] \[[Methodology for Investigation of][research_methodology_for]\] \[[Mitcham 1949][research_mitcham_1949]\] \[[Mitcham et al 1956][research_mitcham_stevens_1956]\] \[[Mitikiri and Mohseni 2018][research_mitikiri_mohseni_2018]\] \[[Montgomery and Hatch 1969][research_montgomery_hatch_1969]\] \[[Moon 2004][research_moon_2004]\] \[[Moreira et al 2022][research_moreira_gripp_2022]\] \[[Muller 1967][research_muller_1967]\] \[[Myers and Walsh 1988][research_myers_walsh_1988]\] \[[Diederich 1951][research_flexible_wing_lateral_1951]\] \[[Najafi et al 2024][research_najafi_kharrat_2024]\] \[[Bull et al 1997][research_propulsion_backup_1997]\] \[[Gelzer and Peebles 2015][research_hsfrs_rcs_2015]\] \[[Pena et al 2018][research_fiber_optic_loads_2018]\] \[[Nettleton 1965][research_nettleton_1965]\] \[[Niel][research_niel]\] \[[Noll et al 1983][research_noll_calico_1983]\] \[[Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952_b]\] \[[O'hara 1971][research_ohara_1971]\] \[[Patil and Hodges 2000][research_patil_hodges_2000]\] \[[Petersen 1981][research_petersen_1981]\] \[[Quinn 1986][research_quinn_1986]\] \[[Rafi and Steck 2013][research_rafi_steck_2013]\] \[[Rafi et al 2012][research_rafi_steck_2012]\] \[[Rimer et al 1984][research_rimer_chipman_1984]\] \[[Rimer et al 1986][research_rimer_chipman_1986]\] \[[Ro et al 1992][research_ro_barlow_1992]\] \[[Rohling 1969][research_rohling_1969]\] \[[Ruflin and Grantham 1984][research_ruflin_grantham_1984]\] \[[Rushby 1993][research_rushby_1993]\] \[[Sato 2022][research_sato_2022]\] \[[Schaefer et al 2011][research_schaefer_hanson_2011]\] \[[Semionov and Kosinov 2007][research_semionov_kosinov_2007]\] \[[Shweyk et al 2012][research_shweyk_hyde_2012]\] \[[Silvestre and Paglione 2008][research_silvestre_paglione_2008]\] \[[Singh and Chowdhury 2021][research_singh_chowdhury_2021]\] \[[Solies 1995][research_solies_1995]\] \[[Song et al 1992][research_song_librescu_1992]\] \[[Sreenatha and Kulkarni][research_sreenatha_kulkarni]\] \[[Streb 1973][research_streb_1973]\] \[[Suleman and Venkayya 1994][research_suleman_venkayya_1994]\] \[[Suleman and Venkayya 1996][research_suleman_venkayya_1996]\] \[[Sun and Hu 2005][research_sun_hu_2005]\] \[[Swaim 1970][research_swaim_1970]\] \[[Swarnkar and Kothari 2016][research_swarnkar_kothari_2016]\] \[[Sánchez et al 2024][research_sanchez_cajas_2024]\] \[[Takahashi et al 2018][research_takahashi_munakata_2018]\] \[[Teper and Stapleford 1966][research_teper_stapleford_1966]\] \[[Tomczyk 2001][research_tomczyk_2001]\] \[[Urnes et al 1990][research_urnes_stewart_1990]\] \[[Vincent and Botez 2015][research_vincent_botez_2015]\] \[[Wagdi 1979][research_wagdi_1979]\] \[[Wang et al 2014][research_wang_han_2014]\] \[[Watts 1976][research_watts_1976]\] \[[Weingarten and Chalk 1982][research_weingarten_chalk_1982]\] \[[Weisshaar and Ryan 1986][research_weisshaar_ryan_1986]\] \[[Wells and Urnes 1994][research_wells_urnes_1994]\] \[[Wen et al 2014][research_wen_wu_2014]\] \[[Wendt 1948][research_wendt_1948]\] \[[Zhang et al 2019][research_zhang_liu_2019]\] \[[Zhou et al 2019][research_zhou_xie_2019]\] \[[Özer 2025][research_ozer_2025]\]

### Research airplanes, flight test and the unpowered return

**The research aircraft as an instrument, and how it came home.** Research aircraft programmes from the X-2 and X-15 onward, air launch, and the approach and landing of unpowered vehicles. **Unpowered approach and landing is the subject of 14 titles**, most of them guidance and trajectory planning for the final approach, which is the solved control problem the review above describes.

**80 records.** \[[Adkins and Armstrong 1965][research_adkins_armstrong_1965]\] \[[Al Bakri][research_albakri]\] \[[Al-Bakri et al 2020][research_albakri_2020]\] \[[AL-Bakri and Kluever 2017][research_albakri_kluever_2017]\] \[[Ananthkrishnan 2004][research_ananthkrishnan_2004]\] \[[Andrews 1977][research_andrews_1977]\] \[[Armstrong 1977][research_armstrong_1977]\] \[[Boothe 1971][research_boothe_1971]\] \[[Brice and Sugano 1978][research_brice_sugano_1978]\] \[[Bryson 1969][research_brysonjr_1969]\] \[[Clay 2004][research_clay_2004]\] \[[Corda et al 1998][research_corda_neal_1998]\] \[[Curry et al 1992][research_curry_mendenhall_1992]\] \[[Deangelis 1991][research_deangelis_1991]\] \[[Deepa and Gupta 2023][research_deepa_gupta_2023]\] \[[Energy Analysis of High-Speed 1991][research_energy_analysis_1991]\] \[[Gilruth 1962][research_gilruth_1962]\] \[[Grauer and Morelli 2023][research_grauer_morelli_2023]\] \[[Grewal et al 1976][research_grewal_schneider_1976]\] \[[Hewes and Hassell 1960][research_hewes_hassell_1960]\] \[[High-speed flight 1986][research_high_speed_flight_1986]\] \[[High-Speed Flight 1996][research_high_speed_flight_1996]\] \[[High-Speed Flight 2009][research_high_speed_flight_2009]\] \[[High-Speed Flight 2010][research_high_speed_flight_2010]\] \[[High-Speed Flight Thermal Management 1996][research_high_speed_flight_1996_b]\] \[[Hoffman et al 1970][research_hoffman_zvara_1970]\] \[[Huang et al 2014][research_huang_zhang_2014]\] \[[Joshi et al 2023][research_joshi_salahudden_2023]\] \[[Kirk and Miller 1962][research_kirk_miller_1962]\] \[[Kirkham et al 1974][research_kirkham_jackson_1974]\] \[[Kluever 2004][research_kluever_2004]\] \[[Kluever 2007][research_kluever_2007]\] \[[Kluever and Neal 2015][research_kluever_neal_2015]\] \[[Kolli 2024][research_kolli_2024]\] \[[Kong et al 2023][research_kong_pan_2023]\] \[[Madagan 1969][research_madagan_1969]\] \[[Malcolm and Rakich 1970][research_malcolm_rakich_1970]\] \[[Malcolm and Rakich 1971][research_malcolm_rakich_1971]\] \[[Molloy 1999][research_molloy_1999]\] \[[Goddwin 1949][research_nose_capsule_1949]\] \[[Day and Stillwell 1952][research_x2_first_landing_1952]\] \[[Drake 1957][research_high_altitude_1957]\] \[[Beeler 1961][research_x15_conference_1958]\] \[[Finch and Matranga 1959][research_x15_first_flight_1959]\] \[[Day and Reisert 1959][research_x2_mach32_1959]\] \[[Hurt and Whitten 1960][research_pitchup_control_1960]\] \[[Dana 1993][research_x15_lessons_1993]\] \[[Cunningham et al 2019][research_stall_training_2019]\] \[[Nowak and Kelly 1976][research_nowak_kelly_1976]\] \[[Nowak and Kelly 1977][research_nowak_kelly_1977]\] \[[Perkins et al 1993][research_perkins_halljr_1993]\] \[[Pierson and Chen 1979][research_pierson_chen_1979]\] \[[Pittsburgh Univ Washington Dc Research Staff 1966][research_pittsburghunivwashingtondcresearchstaff_1966]\] \[[Poth et al 1993][research_pothjr_fisher_1993]\] \[[Propulsion Systems from Takeoff 1991][research_propulsion_systems_1991]\] \[[Putnam 1983][research_putnam_1983]\] \[[Rocha et al 2023][research_rocha_saska_2023]\] \[[Row and Fischel 1963][research_row_fischel_1963]\] \[[S. Hameed and G. R 2021][research_hameed_2021]\] \[[Saltzman 1961][research_saltzman_1961]\] \[[Sarigul-Klijn et al 2006][research_sarigulklijn_sarigulklijn_2006]\] \[[Sarigulklijn et al 2012][research_sarigulklijn_sarigulklijn_2012]\] \[[Shevchuk et al 2017][research_shevchuk_kravchuk_2017]\] \[[Sidhu 2023][research_sidhu_2023]\] \[[The Bell X-22A V/STOL 1990][research_the_bell_1990]\] \[[The Challenges of High-speed 2020][research_the_challenges_2020]\] \[[Thermal Structures and Materials 1992][research_thermal_structures_1992]\] \[[Van Thullenar 1957][research_vanthullenar_1957]\] \[[Vector Quality Assessment of 2017][research_vector_quality_2017]\] \[[Wang et al 2022][research_wang_li_2022_b]\] \[[Welsh et al 1970][research_welsh_winchenbach_1970]\] \[[Williams 1991][research_williams_1991]\] \[[Drake and Williams 1958][research_williams_drake_1948]\] \[[Wimpress 1966][research_wimpress_1966]\] \[[Wiswell et al 1961][research_wiswell_olekszyk_1961]\] \[[Yan and He 2020][research_yan_he_2020]\] \[[Yoo and Duensing 2019][research_yoo_duensing_2019]\] \[[Zhang and Zhang 2020][research_zhang_zhang_2020]\] \[[Zhao et al 2014][research_zhao_sheng_2014]\] \[[Zhao et al 2026][research_zhao_qiao_2026]\]

### Hot structures, thermal stress and aerothermoelasticity

**The article's central design subject.** Hot structures, thermal buckling of skin panels, flutter of heated panels and aerothermoelasticity. **It is among the smaller clusters, and 62 of its 70 dated records appeared in 1970 or later**, after the aircraft that first flew hot structures.

**71 records.** \[[Abbas et al 2012][research_abbas_rui_2012]\] \[[Ahmadi and Pourshahsavari 2016][research_ahmadi_pourshahsavari_2016]\] \[[Al-Khaleefi 2004][research_alkhaleefi_2004]\] \[[Alfano et al 2014][research_alfano_gardi_2014]\] \[[Cerantola et al 2024][research_cerantola_handford_2024]\] \[[Chai et al 2017][research_chai_song_2017]\] \[[Chai et al 2019][research_chai_li_2019]\] \[[Chai et al 2020][research_chai_li_2020]\] \[[Chandrashekhara 1991][research_chandrashekhara_1991]\] \[[Chen and Zhao 2019][research_chen_zhao_2019]\] \[[Collier 1994][research_collier_1994]\] \[[Deng et al 2023][research_deng_wang_2023]\] \[[Dimitrienko et al 2015][research_dimitrienko_koryakov_2015]\] \[[Fields 1978][research_fields_1978]\] \[[Frostig and Thomsen 2008][research_frostig_thomsen_2008]\] \[[Gellatly and Gallagher 1964][research_gellatly_gallagher_1964]\] \[[Guo et al 2004][research_guo_przekop_2004]\] \[[Hata 2001][research_hata_2001]\] \[[Hoff 1956][research_hoff_1956]\] \[[Houbolt and Menkes 1968][research_houbolt_menkes_1968]\] \[[Huang and Friedmann 2016][research_huang_friedmann_2016]\] \[[Huang et al 2019][research_huang_friedmann_2019]\] \[[Hudson and Stephens 2006][research_hudson_stephens_2006]\] \[[Ibrahim et al 2007][research_ibrahim_tawfik_2007]\] \[[Jeng-Shian and Wei-Chong 1991][research_jengshian_weichong_1991]\] \[[Jenkins and Quinn 1996][research_jenkins_quinn_1996]\] \[[Ji and Xie 2022][research_ji_xie_2022]\] \[[Johnson and Young 1972][research_johnson_young_1972]\] \[[Johnston 1964][research_johnston_1964]\] \[[Lawrence 1964][research_lawrence_1964]\] \[[Li and Song 2013][research_li_song_2013]\] \[[Li et al 2024][research_li_wan_2024]\] \[[Mahlmeister et al 1955][research_mahlmeister_ishimoto_1955]\] \[[Matsumoto and Sekiya 1975][research_matsumoto_sekiya_1975]\] \[[McHugh and Leszcz 2024][research_mchugh_leszcz_2024]\] \[[Jenkins 1979][research_thermal_stress_correlation_1979]\] \[[Taylor and Jackson 1980][research_thermostructural_hypersonic_1980]\] \[[Matza 1990][research_dissimilar_joints_1990]\] \[[Morris 1990][research_dryden_hwts_thermal_1990]\] \[[Kehoe and Deaton 1993][research_hot_structure_vibration_1993]\] \[[Olsson 1978][research_olsson_1978]\] \[[Rivers and Glass 2006][research_rivers_glass_2006]\] \[[Rodgers 1992][research_rodgers_1992]\] \[[Schoneman 2019][research_schoneman_2019]\] \[[Sharifzadeh et al 2014][research_sharifzadeh_hendrick_2014]\] \[[Spivey 2009][research_spivey_2009]\] \[[Spivey 2010][research_spivey_2010]\] \[[Spivey 2011][research_spivey_2011]\] \[[Su et al 2021][research_su_hwu_2021]\] \[[Sugiura and Ushijima 2024][research_sugiura_ushijima_2024]\] \[[Taira 1964][research_taira_1964]\] \[[Techniques for Hot Structures 1992][research_techniques_for_1992]\] \[[Thornton and Dechaumphai 1987][research_thornton_dechaumphai_1987_b]\] \[[Thornton and Dechaumphai 1988][research_thornton_dechaumphai_1988]\] \[[Trussell and Thomson 1960][research_trussell_thomson_1960]\] \[[Valentine et al 2004][research_valentine_meyer_2004]\] \[[Vescovini and Dozio 2018][research_vescovini_dozio_2018]\] \[[Walker][research_walker]\] \[[Wang et al 2017][research_wang_yang_2017]\] \[[Xia et al 2022][research_xia_kong_2022]\] \[[Ye and Ye 2020][research_ye_ye_2020]\] \[[Ye et al 2021][research_ye_ye_2021_b]\] \[[Yildirim et al 2020][research_yildirim_2020]\] \[[You et al 2020][research_you_liu_2020]\] \[[Yu et al 2025][research_yu_guo_2025]\] \[[Yuan et al 2014][research_yuan_wang_2014]\] \[[Yuan et al 2015][research_yuan_song_2015]\] \[[Zhai et al 2021][research_zhai_ma_2021]\] \[[Zhang et al 2026][research_zhang_zhou_2026]\] \[[Zhao and Liew 2010][research_zhao_liew_2010]\] \[[Zhu et al 2022][research_zhu_yao_2022]\]

### Thermal protection and ablation

**The thermal lineage past the X-2.** Thermal protection systems, ablation and heat shields for entry vehicles, which the article's source discussion names as the direction in which the thermal problem was taken.

**51 records.** \[[Arc-Heater Code-Validation Tests of 1978][research_arc_heater_code_validation_1978]\] \[[Aronov and Klyagin 2021][research_aronov_klyagin_2021]\] \[[Baker 1969][research_baker_1969]\] \[[Bano et al 2026][research_bano_fraser_2026]\] \[[Chapman and Matting 1965][research_chapman_matting_1965]\] \[[Chauvin et al 1968][research_chauvin_erb_1968]\] \[[Chen and Blosser 2002][research_chen_blosser_2002]\] \[[Chen and Chen 2014][research_chen_chen_2014]\] \[[Cheng et al 2000][research_cheng_mei_2000]\] \[[Chinnaraj et al 2024][research_chinnaraj_kim_2024]\] \[[Cunningham 1972][research_cunningham_1972]\] \[[Dec and Mitcheltree 2002][research_dec_mitcheltree_2002]\] \[[Deming Zhang et al][research_demingzhang_guiqingchen]\] \[[Dolan 1970][research_dolan_1970]\] \[[Duan et al 2001][research_duan_mei_2001]\] \[[Fan 2015][research_fan_2015]\] \[[Finson et al 1980][research_finson_clarke_1980]\] \[[Florence and Hiltz 1968][research_florence_hiltz_1968]\] \[[Gupta and Ramkumar 2015][research_gupta_ramkumar_2015]\] \[[Hardy et al 2005][research_hardy_bronowski_2005]\] \[[Heng and Sherman 1996][research_heng_sherman_1996]\] \[[Hoschke et al 2013][research_hoschke_price_2013]\] \[[Kaul et al 2002][research_kaul_stuckey_2002]\] \[[Kim 2017][research_kim_2017]\] \[[Kowal 2011][research_kowal_2011]\] \[[Kuo 1976][research_kuo_1976]\] \[[Lacombe and Rouges 1990][research_lacombe_rouges_1990]\] \[[Martin and Panesi 2022][research_martin_panesi_2022]\] \[[Natali et al 2013][research_natali_rallini_2013]\] \[[Palmer et al 1995][research_palmer_henline_1995]\] \[[Pan et al 2026][research_pan_zhang_2026]\] \[[Prata et al 2022][research_prata_2022]\] \[[Preliminary Design of the 1983][research_preliminary_design_1983]\] \[[Rakow and Waas 2004][research_rakow_waas_2004]\] \[[Santos et al 2008][research_santos_beck_2008]\] \[[Skolnik and Putnam 2022][research_skolnik_putnam_2022]\] \[[Strouhal and Curry 1966][research_strouhal_curry_1966]\] \[[Tallman 1965][research_tallman_1965]\] \[[Thermal performance evaluation of 1972][research_thermal_performance_1972]\] \[[Thermal Protection System Conception 2013][research_thermal_protection_2013]\] \[[Tile-Gap Flow in the 1983][research_tile_gap_flow_1983]\] \[[Vlahopoulos and He 2009][research_vlahopoulos_he_2009]\] \[[Wang et al 2018][research_wang_wu_2018]\] \[[Whitnah 1967][research_whitnah_1967]\] \[[Wiedemann et al 1986][research_wiedemann_clark_1986]\] \[[Wright and Zoby 1971][research_wright_zoby_1971]\] \[[Wurster 1981][research_wurster_1981]\] \[[Xin et al 2026][research_xin_xu_2026]\] \[[Yakimov 2018][research_yakimov_2018]\] \[[Yakimov 2018][research_yakimov_2018_b]\] \[[Yakimov 2018][research_yakimov_2018_c]\]

### Real gas, hypersonic flow and similitude

**The regime the X-2 stayed below, and the similarity it could not achieve.** Real-gas and nonequilibrium effects, dissociation, and dynamic similarity in scale testing. It is small, and the article's perfect-gas check shows these effects are absent at Mach 3.2, so little of the argument rests on it.

**17 records.** \[[Chang 1962][research_chang_1962]\] \[[Hu and Mahadevan 2019][research_hu_mahadevan_2019]\] \[[Jordan et al 2004][research_jordan_langford_2004]\] \[[Bowman and Healy 1960][research_spin_tunnel_1960]\] \[[Lawing 1975][research_coldwall_descent_1975]\] \[[Plank 1975][research_hypersonic_wing_structure_1975]\] \[[Jackson and Taylor 1976][research_hypersonic_research_structure_1976]\] \[[Ellis et al 1978][research_cooled_honeycomb_1978]\] \[[Gully et al 1987][research_real_gas_facility_1987]\] \[[Park and Yoon 1989][research_real_gas_trim_1989]\] \[[Maughmer et al 1990][research_control_effectors_1990]\] \[[NASA 1991][research_cooling_hypersonic_1991]\] \[[Newsom and Anglin 1975][research_newsom_anglin_1975]\] \[[Pan et al 2021][research_pan_cao_2021]\] \[[Patterson 1966][research_patterson_1966]\] \[[Tushavina 2022][research_tushavina_2022]\] \[[Zeng et al 2023][research_zeng_yuan_2023]\]

### Other high-speed aeronautical and foundational literature

**The residual, reported and not hidden.** High-speed aircraft design in general, the properties of aircraft structural metals after rapid heating, and the foundational works of information theory, experimental design and similarity on which the article's accounting rests.

**68 records.** \[[Advanced Metallics for High-Temperature 1992][research_advanced_metallics_1992]\] \[[Aerodynamic Components of Aircraft 1957][research_aerodynamic_components_1957]\] \[[An et al 2023][research_an_jiepan_2023]\] \[[Ananthkrishnan and Sinha 2023][research_ananthkrishnan_sinha_2023]\] \[[Asghar et al 2018][research_asghar_allan_2018]\] \[[Ashokkumar 2023][research_ashokkumar_2023]\] \[[Boland et al 1993][research_boland_riley_1993]\] \[[Brownfield and Badger 1960][research_brownfield_badger_1960]\] \[[Brunton et al 2020][research_brunton_noack_2020]\] \[[Buchanan and Cayse 1988][research_buchanan_cayse_1988]\] \[[Buckingham 1914][research_buckingham_1914]\] \[[Chaloner and Verdinelli 1995][research_chaloner_verdinelli_1995]\] \[[Chalot et al 1994][research_chalot_mallet_1994]\] \[[Clarkson 1935][research_clarkson_1935]\] \[[Coetzee et al 2013][research_coetzee_krauskopf_2013]\] \[[Culick and Jahnke 1988][research_culick_jahnke_1988]\] \[[Venkateswara Rao][research_d]\] \[[Dhosi et al 1963][research_dhosi_widmer_1963]\] \[[Dhosi et al 1964][research_dhosi_widmer_1964]\] \[[Feng and Wang 2008][research_feng_wang_2008]\] \[[Fofonov 2021][research_fofonov_2021]\] \[[Fortney and Avery 1957][research_fortney_avery_1957]\] \[[German 2011][research_german_2011]\] \[[Goman et al 1997][research_goman_khramtsovsky_1997]\] \[[Gomes and Suleman 2004][research_gomes_suleman_2004]\] \[[Gomillion 1976][research_gomillion_1976]\] \[[Hashin and Humphreys 1980][research_hashin_humphreys_1980]\] \[[High Speed Problems of 1962][research_high_speed_1962]\] \[[Hughes 1964][research_hughes_1964]\] \[[Ishin 2022][research_ishin_2022]\] \[[Kusko 1957][research_kusko_1957]\] \[[Lai et al 2021][research_lai_cunis_2021]\] \[[Leng 1995][research_leng_1995]\] \[[Leonard 1938][research_leonard_1938]\] \[[Mach Number and Reynolds 2022][research_mach_number_2022]\] \[[Maqsood and Go 2011][research_maqsood_go_2011]\] \[[Martinez 1961][research_martinez_1961]\] \[[NACA Conference on High-speed 1958][research_highspeed_conference_1958]\] \[[Equations, tables, and charts 1953][research_naca_1135]\] \[[NASA 1961][research_rapid_compression_1961]\] \[[Greene and Northrup 1975][research_rene41_panels_1975]\] \[[Davari and Laitone 1977][research_nonconstant_cma_1977]\] \[[NASA 1990][research_low_disturbance_tunnels_1990]\] \[[Day 1997][research_coupling_history_1997]\] \[[Lallman et al 1998][research_thrust_vectoring_strakes_1998]\] \[[Nonweiler 1959][research_nonweiler_1959]\] \[[Northrop Aircraft Inc Hawthorne Ca 1953][research_northropaircraftinchawthorneca_1953_b]\] \[[Nyquist 1928][research_nyquist_1928]\] \[[Patnaik et al 1998][research_patnaik_guptill_1998]\] \[[Pollock and Wild 2024][research_pollock_wild_2024]\] \[[Prandtl 1928][research_prandtl_1928]\] \[[Rajadas et al 1998][research_rajadas_juryiv_1998]\] \[[Roberts 1999][research_roberts_1999]\] \[[Roe and Kattus 1957][research_roe_kattus_1957]\] \[[Salay and Elliott 1996][research_salay_elliott_1996]\] \[[Shams][research_shams]\] \[[Shams et al 2026][research_shams_khouli_2026]\] \[[Shannon 1948][research_shannon_1948]\] \[[Sleight et al 2008][research_sleight_paddock_2008]\] \[[Sutherland 1893][research_sutherland_1893]\] \[[Takeda 1970][research_takeda_1970]\] \[[Velger and Shinar 1983][research_velger_shinar_1983]\] \[[Viviani et al 2021][research_viviani_aprovitola_2021]\] \[[Whitehead 1991][research_whiteheadjr_1991]\] \[[Wilson et al 1973][research_wilson_cazier_1973]\] \[[Wright 1936][research_wright_1936]\] \[[Zaludin 2012][research_zaludin_2012]\] \[[Zu and Tan 2022][research_zu_tan_2022]\]

## Where the Framing Breaks Down

Reading the X-2 through the heating keystone is defensible and it is incomplete in four ways.

The keystone was answered and the aircraft is not remembered for it. That is the sharpest instance in this series so far of a mismatch between stated research question and delivered contribution, and it argues that the keystone framework describes design intent rather than historical significance. Both are worth having. They are not the same thing.

The programme took ten years and delivered into a community already working on the X-15. A framework that scores an aircraft on the information it returned does not capture the penalty for returning that information late, and the X-2 pays that penalty heavily. Its thermal data were valuable and would have been more valuable in 1950.

The instrument model treats the aircraft as the unit of analysis, and for the X-2 the more informative unit may be the accident. What propagated through the community was not a data set but an event, and events propagate differently from reports. That is uncomfortable for a framework built on information economics and it should be said plainly.

The safety record resists the framing entirely. Two aircraft, two pilots, and a carrier crewman lost across twenty flights, glides included, is not a rate any information-value calculation would endorse, and the attrition sizing used elsewhere in this series would have predicted a fleet larger than two. The programme continued after the first loss with a single remaining airframe and no replacement, which is a decision the framework has nothing to say about. [Perrow 1984][book_perrow_1984], [Vaughan 1996][book_vaughan_1996], [Sagan 1993][book_sagan_1993], and [Reason 1990][book_reason_1990_human_error] are the appropriate correctives.

## The Source Base

The primary technical record is thinner than the X-1's and the reason is institutional. The X-2 was an Air Force programme with NACA participation rather than a NACA-led effort, more of its documentation was originally classified, and the programme ended abruptly with the loss of the only remaining aircraft, so there was no consolidation phase. [Day and Reisert 1959][research_x2_mach32_1959] is the substantial public technical account and the glide and landing reports of [Day and Stillwell 1952][research_x2_first_landing_1952] and [Day 1953][research_x2_glide_1953] cover the early phase. Beyond that the aircraft appears mostly in comparative summaries such as [Bellman 1959][research_transonic_summary_1959] and [Saltzman and Ayers 1995][research_supersonic_research_1995].

The secondary literature is correspondingly thin and uneven. [Miller 2001][book_miller_2001_x_planes], [Jenkins Landis and Miller 2003][book_jenkins_landis_miller_2003], [Winchester 2005][book_winchester_2005_x_planes], and [Peebles 2014][book_peebles_2014_probing_the_sky] give the roster treatment. [Hallion 1972][book_hallion_1972_supersonic_flight], [Hallion 1981][book_hallion_1981_on_the_frontier], and [Hallion 1981][book_hallion_1981_test_pilots] give the programme and pilot context, with the institutional account in [Gorn 2001][book_gorn_2001_expanding_envelope] and [Bilstein 1989][book_bilstein_1989_orders]. [Heppenheimer 2007][book_heppenheimer_2007_heat_barrier] is the standard history of the thermal problem the aircraft was built for and is the single best companion to this article. [Gunston 1992][book_gunston_1992_faster_than_sound] and [Wolfe 1979][book_wolfe_1979_right_stuff] supply the popular framing, the latter to be read as literature. The X-15 works of [Jenkins 2007][book_jenkins_2007_x15], [Jenkins 2000][book_jenkins_2000_hypersonics], and [Thompson 1992][book_thompson_1992_edge_of_space] are where the X-2's inheritance is visible, and [Launius and Jenkins 2012][book_launius_jenkins_2012] extends the thermal lineage to entry vehicles.

The engineering texts behind the relations are [Anderson 2001][book_anderson_2001_fundamentals], [Anderson 2002][book_anderson_2002_modern_compressible], [Anderson 2006][book_anderson_2006_hypersonic], [Anderson 2012][book_anderson_2012_aircraft_performance], [Anderson 1997][book_anderson_1997_history_aerodynamics], [Bertin 1994][book_bertin_1994_hypersonic], [Bertin and Cummings 2013][book_bertin_cummings_2013], [Truitt 1960][book_truitt_1960], [Shapiro 1953][book_shapiro_1953], [Liepmann and Roshko 1957][book_liepmann_roshko_1957], [Ashley and Landahl 1965][book_ashley_landahl_1965], [Kuchemann 1978][book_kuchemann_1978], [Schlichting and Gersten 2017][book_schlichting_gersten_2017], and [White 2006][book_white_2006_viscous], with heat transfer in [Incropera and DeWitt][book_incropera_heat_transfer]. Flight dynamics is [Etkin and Reid 1996][book_etkin_reid_1996], [Nelson 1998][book_nelson_1998], [Stengel 2004][book_stengel_2004], [Stevens and Lewis 2015][book_stevens_lewis_2015], [McRuer Ashkenas and Graham 1973][book_mcruer_ashkenas_graham_1973], and [Hurt 1965][book_hurt_1965], with the design methods in [Raymer 2018][book_raymer_2018], [Nicolai and Carichner 2010][book_nicolai_carichner_2010], and [Whitford 1987][book_whitford_1987]. Structures are [Bruhn 1973][book_bruhn_1973], [Niu 1988][book_niu_1988_airframe], and [Megson 2016][book_megson_2016], aeroelasticity is [Bisplinghoff Ashley and Halfman 1955][book_bisplinghoff_ashley_halfman_1955], [Fung 1955][book_fung_1955], and [Dowell 2014][book_dowell_2014], and propulsion is [Sutton and Biblarz 2016][book_sutton_biblarz_2016], [Huzel and Huang 1992][book_huzel_huang_1992], and [Hill and Peterson 1991][book_hill_peterson_1991]. Flight test practice is [Kimberlin 2003][book_kimberlin_2003] and [Ward Strganac and Niewoehner 2006][book_ward_strganac_niewoehner_2006]. The epistemology is [Vincenti 1990][book_vincenti_1990], [Petroski 1985][book_petroski_1985], and [Ferguson 1992][book_ferguson_1992], the information accounting is [Cover and Thomas 2006][book_cover_thomas_2006] with experimental design in [Box Hunter and Hunter 2005][book_box_hunter_hunter_2005], [Gelman et al 2013][book_gelman_et_al_2013], [Lindley 1956][research_lindley_1956], and [Chaloner and Verdinelli 1995][research_chaloner_verdinelli_1995], and the sampling and channel results are [Nyquist 1928][research_nyquist_1928] and [Shannon 1948][research_shannon_1948]. Tunnel history is [Baals and Corliss 1981][book_baals_corliss_1981], [Hansen 1987][book_hansen_1987_engineer_in_charge], and [Chambers and Chambers 2008][book_chambers_2008_radical_wings].

Further primary sources bear on the arguments above without belonging to any one section. [Drake and Williams 1958][research_williams_drake_1948] state the rationale for dedicated research aircraft. [Buckingham 1914][research_buckingham_1914] fixes how many dimensionless groups a scale test must match, which is the formal reason a static model cannot represent an inertia-coupling problem. [Sutherland 1893][research_sutherland_1893] supplies the viscosity relation behind every Reynolds number quoted here. [Collar 1946][research_collar_1946], [Theodorsen 1935][research_theodorsen_1935], [Garrick and Reed 1981][research_garrick_reed_1981], and the [NACA 1957 loads and flutter conference][research_loads_flutter_conf_1957] bound the aeroelastic problem that a hot thin structure makes worse, and [Stubblefield et al 2025][research_stubblefield_kunz_2025] show the modern measurement of it. The wider drag and heating context appears in [Sears 1947][research_sears_1947], [Glauert 1928][research_glauert_1928], [Prandtl 1928][research_prandtl_1928], [Whitcomb 1952][research_whitcomb_1952], [Eckert 1956][research_eckert_1956], [Chapman and Rubesin 1949][research_chapman_rubesin_1949], [Nonweiler 1959][research_nonweiler_1959], [Rodert 1940][research_heating_ice_1940] on the earliest recognition that aerodynamic heating is measurable at all, [Sasson et al 2022][research_sbli_experiments_2022], [Berry et al 2016][research_blt_shuttle_2016], and [Saltzman 1953][research_x1_liftdrag_1953]. Programme cost behaviour at these quantities follows [Wright 1936][research_wright_1936], the drag-measurement technique is [Beeler et al 1956][research_beeler_1956], the pitch-up thread that shares the same stability lineage is [Anderson and Bray 1955][research_pitchup_evaluation_1955] and [Hurt and Whitten 1960][research_pitchup_control_1960], the sibling X-5 work is [Finch and Walker 1953][research_x5_stability_1953] and [Reed 1955][research_x5_tail_loads_1955], the roll-coupling analysis extends through [Davari and Laitone 1977][research_nonconstant_cma_1977] and [Jacobsen and Greif 1972][research_lift_roll_coupling_1972], the high-altitude context is [Drake 1957][research_high_altitude_1957], and Reynolds-number effects on supersonic transport stability are [Owens et al 2002][research_reynolds_sst_2002]. Machine learning has since entered the modelling of all of it, as [Brunton et al 2020][research_brunton_noack_2020] survey. The equivalent problems at model scale are worked on this blog in [Propulsion and Power Sizing for Small Fixed-Wing UAVs][related_post_a118_propulsion_sizing], [Stability, Control, and Configuration for Fixed-Wing UAVs][related_post_a122_stability_configuration], [Dynamic Stability and Control for Fixed-Wing UAVs][related_post_a123_dynamic_stability], and [Structures and the Flight Envelope for Fixed-Wing UAVs][related_post_a127_structures_flight_envelope], the rocketplane lineage in [History of Rocketplanes][related_post_a96_history_rocketplanes], large high-speed configurations in [Two-Stage Flying Delta Wing Vehicles for Civil and National Security Applications][related_post_a106_two_stage_delta_wing], the computing and simulation infrastructure in [Aerospace, Programming Languages, and Information Technology Co-Development: Framing and the Co-Development Mechanism][related_post_a237_aerospace_framing] and [Aerospace, Programming Languages, and Information Technology Co-Development: Aerospace Simulation and Real-Time Systems][related_post_a241_aerospace_simulation], and the space policy context in [Introduction to Space Studies][related_post_a90_intro_space_studies].

**The survey rests on 3,884 research records drawn from Crossref, the NASA Technical Reports Server and the Defense Technical Information Center**, of which 763 are report primaries by the identifier rule set out under The Definition of Primary, being 19.6 percent. Of those primaries, 407 are Technical Reports Server records and 356 are Defense Technical Information Center reports. The survey includes the 193 research records cited in the argument above, each placed in the cluster its title describes. The median publication year of the dated records is 1998, 1,980 of them, or 51.8 percent, appeared before 2000, and 1,068, or 28.0 percent, appeared in 2015 or later.

### The Definition of Primary

**Primacy is a property of the document, and this survey derives it from the identifier.** A record is a report primary when it is a NASA Technical Reports Server url or carries a digital object identifier under the 10.21236 prefix, which Crossref registers for Defense Technical Information Center reports. **The same report can be reachable through Crossref and through the Defense Technical Information Center under two different labels**, and a rule keyed on where a record was found rather than on what it is would count such a report as secondary.

**The rule reaches the aircraft's own documents and stops short of much first-hand work.** Every record whose title names the X-2 is a report primary by this rule. Journal papers by the engineers who did the work are not, so 19.6 percent is a lower bound on how much of this survey is first-hand.

### Thin Subjects

**Five subjects that this article's derivations and conclusions depend on have thin literatures.** Each count below is the number of research records in this survey whose title carries at least one of the listed terms, with every hyphen read as a space.

| Subject | Title terms counted | Records |
|---|---|---|
| the Bell X-2 itself | x 2 research airplane, x 2 airplane, bell x 2, x 2 research aircraft | 5 |
| Monel and nickel-copper alloys | monel, k monel, nickel copper | 1 |
| inertia and roll coupling | inertia coupling, inertial coupling, roll coupling, rolling coupling, roll yaw coupling, yaw roll coupling, pitch roll coupling, pitch yaw roll coupling, inertial roll coupling, rolling maneuvers, rolling manoeuvres | 24 |
| the Larson-Miller parameter | larson miller | 15 |
| the recovery factor and recovery temperature | recovery factor, recovery factors, recovery temperature, temperature recovery | 14 |

**The aircraft itself is the thinnest subject.** Five records carry the X-2 in their titles, all of them reports of the National Advisory Committee for Aeronautics or of NASA dated from 1949 to 1959, which is the institutional thinness the first paragraph of this section describes. The aircraft's structural alloy is thinner still. One record names a nickel-copper alloy, and it concerns the friction and wear of Monel K-500 in high-pressure oxygen, which bears on the compatibility of pump internals rather than on the airframe. The article's thermal properties for the skin are therefore representative values for stainless steel, as the Epistemic State section records.

**The recovery factor and the Larson-Miller parameter are settled subjects.** Both are correlations that the article applies rather than derives. Of the 14 recovery-factor records, 7 date from before 1960, when the measurements were made. The 15 Larson-Miller records concern creep-life prediction for steels and nickel alloys, and none of them names an aircraft or flight application.

**Inertia coupling by name is a small literature for the phenomenon that ended the programme.** The term is carried by 24 records, against the 234 records of the cluster that holds the departure and loss-of-control work, because the field now writes about the consequence rather than the mechanism.

### What the Survey Admits

**A record is admitted only when a person reading its title finds it on this article's subject**, which is aerodynamic heating, the hot structure and its materials, the coupled rotational dynamics, the dependent systems of propulsion, escape and instrumentation, and the high-speed aerodynamics and flight research that frame them. Many words this subject depends on also name something else, and a record that shares only such a word is excluded. A yaw damper is also a component of a railway bogie, and yaw stability control belongs to road vehicles. Flutter also names a cardiac arrhythmia, and upset recovery also names a process-plant procedure and a fault in semiconductor memory. Departure also names airport scheduling, and loss of control also names a disorder of eating. Creep and oxidation are also studied in nuclear fuel cladding, in reactor and petrochemical plant, and in building members exposed to fire, and an escape capsule is also built for divers, miners and offshore platforms. Stagnation-point heat transfer is also the subject of jet impingement cooling and of similarity solutions for stretching and shrinking sheets, and supersonic flow is also the medium of combustion research, chemical lasers and molecular-beam spectroscopy. Rotorcraft and vertical takeoff aircraft, powered approach and landing systems, and aircraft subsystems unrelated to heating or stability, such as bearings, brakes, cabin conditioning and electrical power, are excluded as outside the subject. Correction and retraction notices are excluded as well, because a survey counts research works and those are editorial events. A review of a book, an encyclopedia or dictionary entry of two pages or fewer, an unsigned news item and a second deposit of a document already held are not admitted on the same ground, while an authored encyclopedia article of more than two pages is a research work and is kept.

**Some records of doubtful relevance are kept.** Studies of the Reynolds analogy outside aeronautics, creep and oxidation studies of power-plant and turbine alloys, supersonic parachute deployment for Mars entry, and the lateral and directional stability of vertical and short takeoff aircraft each share a construct or a method with this article's argument, so each is kept and a reader may weigh it accordingly.

**Every research title in the survey has been read for relevance, so the off-topic share that remains is a matter of reading judgement.** A reading of titles cannot show that a work is relevant in substance, so this is a statement about titles only.

## Epistemic State

Established historical fact includes the 1945 authorization, the two airframes and their serials, the stainless steel and K-Monel construction, the 40 degree wing sweep, the Curtiss-Wright XLR25 engine and its throttleability, the air launch from a B-50, the jettisonable nose capsule in place of an ejection seat, the loss of 46-675 with Jean Ziegler and a carrier crew member on 12 May 1953, Frank Everest reaching Mach 2.87 on 23 July 1956, Iven Kincheloe reaching 126,200 feet on 7 September 1956, and Milburn Apt reaching Mach 3.196 on 27 September 1956 before being lost to a coupled divergence with a capsule parachute failure. These are documented in the sources cited.

Established engineering analysis includes every relation in the sizing sections. The stagnation and recovery temperature relations, the Sutton-Graves correlation, the Stefan-Boltzmann law, the lumped transient balance, the Biot and Fourier numbers, the thermal stress relation, simple sweep theory, the Ackeret result, the Tsiolkovsky relation, the tail volume relations, and the Euler moment equations are standard results. The worked numbers are the author's own arithmetic applied to published inputs and are labelled as derived.

Inference includes the reading of the aircraft through a thermal keystone, and the causal account of the accident in which weakened directional stiffness and large inertia asymmetry combine to place the critical roll rate inside the commandable range. The account is consistent with the primary report and with the subsequent literature, and it is an account rather than a finding of that report.

Weakly supported are the representative values used where the record does not give the figure. The moments of inertia, the radii of gyration behind them, the pitch and directional stiffness coefficients, the effective nose radius, the skin thickness and its thermal properties, the emissivity, and the tail volume are plausible values for an aircraft of this class rather than measured properties of this airframe. They support an order of magnitude and a direction. The critical roll rate of 154 degrees per second should be read as indicating a boundary within normal control authority, not as a number this aircraft carried.

Contested or unresolved in the sources consulted is the precise trigger for Apt's turn, which is variously attributed to a desire to conserve energy for the return, to disorientation, and to a misjudgement of remaining distance, with no source establishing which. The total powered flight count is given inconsistently across secondary accounts. And the recorded speed and Mach number for the final flight are mutually inconsistent by about 0.7 percent under the standard atmosphere, which this article states rather than reconciles.

A note on temporal position. This article carries an editorial date of 2025-10-08 and is written from current knowledge, including contemporary literature published well after that date.

## Out of Scope

This article does not treat the X-1 series beyond the comparisons drawn, which are covered in [X-Planes: Bell X-1][related_post_a298_bell_x1], nor the [X-15][ref_na_x15], which receives its own article later in the series and where the thermal problem is taken far further. It does not cover the Navy research airplanes, the [X-3][ref_douglas_x3], the [X-4][ref_northrop_x4], or the [X-5][ref_bell_x5] except as context, and the last two appear in their own articles. It does not derive the standard relations reused here, since the [series opener][related_post_a297_xplanes_framing] does that once for all seventy-two articles, including the [flight envelope][ref_flight_envelope], [load factor][ref_load_factor], [wing loading][ref_wing_loading], [lift][ref_lift_coefficient] and [drag][ref_drag_coefficient] coefficient, [lift-to-drag][ref_lift_to_drag], [Reynolds number][ref_reynolds_number], and [measurement uncertainty][ref_measurement_uncertainty] and [propagation][ref_propagation_of_uncertainty] machinery, and the [standard atmosphere][ref_isa] and its [tabulated form][ref_us_standard_atmosphere].

It does not attempt an accident investigation. The primary report exists and this article defers to it rather than reconstructing the sequence from secondary narrative. It does not treat the biographies of [Apt][ref_mel_apt], [Kincheloe][ref_kincheloe], or [Everest][ref_everest] beyond what bears on the engineering, and the book-length account of the period by [Everest 1958][book_everest_1958_fastest_man] is a participant source to be read as such. It does not survey the [list of X-planes][ref_list_of_x_planes] or [experimental aircraft][ref_experimental_aircraft] generally, nor [Edwards][ref_edwards_afb] and the [Armstrong Flight Research Center][ref_armstrong_frc] and its [predecessor organizations][ref_nasa_armstrong] as institutions, nor the [National Museum of the United States Air Force][ref_nmusaf] holdings, nor the [sound barrier][ref_sound_barrier] as a cultural object, nor [hypersonic flight][ref_hypersonic_flight] and the [oblique shock][ref_oblique_shock], [shock wave][ref_shock_wave], [wave drag][ref_wave_drag], [flow separation][ref_flow_separation], [supersonic][ref_supersonic_speed] and [turbopump][ref_turbopump] topics beyond the sizing above, nor [Inconel][ref_inconel], [duralumin][ref_duralumin], [yield][ref_yield_strength], [liquid oxygen][ref_liquid_oxygen], the [rocket engine][ref_rocket_engine], [stabilators][ref_stabilator], the [escape crew capsule][ref_escape_crew_capsule] as a general subject, [Dutch roll][ref_dutch_roll] and the [phugoid][ref_phugoid], [flight dynamics][ref_flight_dynamics] and [longitudinal static stability][ref_longitudinal_static_stability] in general, [wind tunnels][ref_wind_tunnel], [flight testing][ref_flight_test], the [NACA][ref_naca] and [NASA][ref_nasa] as organizations, or the [NASA fact sheet][ref_nasa_x2_factsheet] beyond what is cited. The [NASA Technical Reports Server][ref_ntrs] and the [NASA History Office][ref_nasa_history] hold the record.

## Conclusion

The Bell X-2 was built to answer a question about temperature and it answered it. A recovery temperature of 611 kelvin at Mach 3.196 excludes aluminium, admits steel, and makes the binding constraint the time spent at temperature rather than the temperature itself. An eighteen-second margin from 250 to 800 kelvin is what a 1.6 millimetre steel skin buys against a 194 kilowatt per square metre stagnation flux, and the aircraft was flown as a heat sink rather than as an equilibrated structure. Thermal stress, not thermal weakening, is what actually governs the design, since a hundred-kelvin gradient across a constrained load path already exceeds yield.

The aircraft then delivered a second answer at a price nobody had budgeted. Directional stiffness falls as the inverse of the supersonic Prandtl-Glauert factor, so a tail sized for Mach 1.5 is 2.7 times weaker at Mach 3.2. Combine that with a long fuselage, short wings, and a large inertia asymmetry and the critical roll rate falls to something a pilot can command without knowing he has done so. There was no reaction control system to fall back on and the escape chain had five links. Milburn Apt found all of that in a single flight, and the community changed roll rate limits, adopted artificial damping, and grew vertical tails because he did.

The X-2 is therefore the first aircraft in this series where the keystone framework, applied honestly, reports a success and the historical record reports something else. That divergence is worth carrying forward, because it will recur.

The next article takes the [Douglas X-3 Stiletto][ref_douglas_x3], which was built to sustain supersonic flight on a low-aspect-ratio wing, never reached the speed it was designed for, and made its most valuable contribution to exactly the coupling problem that destroyed the X-2.

## References

### Books

- [Anderson 1997 A History of Aerodynamics][book_anderson_1997_history_aerodynamics]
- [Anderson 2001 Fundamentals of Aerodynamics][book_anderson_2001_fundamentals]
- [Anderson 2002 Modern Compressible Flow][book_anderson_2002_modern_compressible]
- [Anderson 2006 Hypersonic and High-Temperature Gas Dynamics][book_anderson_2006_hypersonic]
- [Anderson 2012 Aircraft Performance and Design][book_anderson_2012_aircraft_performance]
- [Ashley and Landahl 1965 Aerodynamics of Wings and Bodies][book_ashley_landahl_1965]
- [Baals and Corliss 1981 Wind Tunnels of NASA][book_baals_corliss_1981]
- [Bertin 1994 Hypersonic Aerothermodynamics][book_bertin_1994_hypersonic]
- [Bertin and Cummings 2013 Aerodynamics for Engineers][book_bertin_cummings_2013]
- [Bevington and Robinson 2002 Data Reduction and Error Analysis][book_bevington_robinson_2002]
- [Bilstein 1989 Orders of Magnitude, A History of the NACA and NASA][book_bilstein_1989_orders]
- [Bisplinghoff Ashley and Halfman 1955 Aeroelasticity][book_bisplinghoff_ashley_halfman_1955]
- [Boley and Weiner 1960 Theory of Thermal Stresses][book_boley_weiner_1960]
- [Box Hunter and Hunter 2005 Statistics for Experimenters][book_box_hunter_hunter_2005]
- [Bruhn 1973 Analysis and Design of Flight Vehicle Structures][book_bruhn_1973]
- [Carslaw and Jaeger 1959 Conduction of Heat in Solids][book_carslaw_jaeger_1959]
- [Chambers and Chambers 2008 Radical Wings and Wind Tunnels][book_chambers_2008_radical_wings]
- [Cover and Thomas 2006 Elements of Information Theory][book_cover_thomas_2006]
- [Dowell 2014 A Modern Course in Aeroelasticity][book_dowell_2014]
- [Etkin and Reid 1996 Dynamics of Flight, Stability and Control][book_etkin_reid_1996]
- [Everest 1958 The Fastest Man Alive][book_everest_1958_fastest_man]
- [Ferguson 1992 Engineering and the Mind's Eye][book_ferguson_1992]
- [Fung 1955 An Introduction to the Theory of Aeroelasticity][book_fung_1955]
- [Gelman et al 2013 Bayesian Data Analysis][book_gelman_et_al_2013]
- [Gorn 2001 Expanding the Envelope, Flight Research at NACA and NASA][book_gorn_2001_expanding_envelope]
- [Gunston 1992 Faster Than Sound][book_gunston_1992_faster_than_sound]
- [Hallion 1972 Supersonic Flight, Breaking the Sound Barrier and Beyond][book_hallion_1972_supersonic_flight]
- [Hallion 1981 On the Frontier, Flight Research at Dryden][book_hallion_1981_on_the_frontier]
- [Hallion 1981 Test Pilots, The Frontiersmen of Flight][book_hallion_1981_test_pilots]
- [Hansen 1987 Engineer in Charge][book_hansen_1987_engineer_in_charge]
- [Heppenheimer 2007 Facing the Heat Barrier, A History of Hypersonics][book_heppenheimer_2007_heat_barrier]
- [Hill and Peterson 1991 Mechanics and Thermodynamics of Propulsion][book_hill_peterson_1991]
- [Hurt 1965 Aerodynamics for Naval Aviators][book_hurt_1965]
- [Huzel and Huang 1992 Modern Engineering for Design of Liquid-Propellant Rocket Engines][book_huzel_huang_1992]
- [Incropera and DeWitt, Fundamentals of Heat and Mass Transfer][book_incropera_heat_transfer]
- [Jenkins 2000 Hypersonics Before the Shuttle][book_jenkins_2000_hypersonics]
- [Jenkins 2007 X-15, Extending the Frontiers of Flight][book_jenkins_2007_x15]
- [Jenkins Landis and Miller 2003 American X-Vehicles, An Inventory X-1 to X-50][book_jenkins_landis_miller_2003]
- [Kimberlin 2003 Flight Testing of Fixed-Wing Aircraft][book_kimberlin_2003]
- [Kuchemann 1978 The Aerodynamic Design of Aircraft][book_kuchemann_1978]
- [Launius and Jenkins 2012 Coming Home, Reentry and Recovery from Space][book_launius_jenkins_2012]
- [Liepmann and Roshko 1957 Elements of Gasdynamics][book_liepmann_roshko_1957]
- [McRuer Ashkenas and Graham 1973 Aircraft Dynamics and Automatic Control][book_mcruer_ashkenas_graham_1973]
- [Megson 2016 Aircraft Structures for Engineering Students][book_megson_2016]
- [Merlin 2009 Design and Development of the Blackbird][book_merlin_2009_blackbird]
- [Miller 2001 The X-Planes, X-1 to X-45][book_miller_2001_x_planes]
- [Nelson 1998 Flight Stability and Automatic Control][book_nelson_1998]
- [Nicolai and Carichner 2010 Fundamentals of Aircraft and Airship Design][book_nicolai_carichner_2010]
- [Niu 1988 Airframe Structural Design][book_niu_1988_airframe]
- [Peebles 2014 Probing the Sky, Selected NACA Research Airplanes][book_peebles_2014_probing_the_sky]
- [Perrow 1984 Normal Accidents][book_perrow_1984]
- [Petroski 1985 To Engineer Is Human][book_petroski_1985]
- [Raymer 2018 Aircraft Design, A Conceptual Approach][book_raymer_2018]
- [Reason 1990 Human Error][book_reason_1990_human_error]
- [Sagan 1993 The Limits of Safety][book_sagan_1993]
- [Schlichting and Gersten 2017 Boundary-Layer Theory][book_schlichting_gersten_2017]
- [Shapiro 1953 The Dynamics and Thermodynamics of Compressible Fluid Flow][book_shapiro_1953]
- [Stengel 2004 Flight Dynamics][book_stengel_2004]
- [Stevens and Lewis 2015 Aircraft Control and Simulation][book_stevens_lewis_2015]
- [Sutton and Biblarz 2016 Rocket Propulsion Elements][book_sutton_biblarz_2016]
- [Taylor 1997 An Introduction to Error Analysis][book_taylor_1997_error_analysis]
- [Thompson 1992 At the Edge of Space][book_thompson_1992_edge_of_space]
- [Truitt 1960 Fundamentals of Aerodynamic Heating][book_truitt_1960]
- [Vaughan 1996 The Challenger Launch Decision][book_vaughan_1996]
- [Vincenti 1990 What Engineers Know and How They Know It][book_vincenti_1990]
- [Ward Strganac and Niewoehner 2006 Introduction to Flight Test Engineering][book_ward_strganac_niewoehner_2006]
- [White 2006 Viscous Fluid Flow][book_white_2006_viscous]
- [Whitford 1987 Design for Air Combat][book_whitford_1987]
- [Winchester 2005 X-Planes and Prototypes][book_winchester_2005_x_planes]
- [Wolfe 1979 The Right Stuff][book_wolfe_1979_right_stuff]

### Reference

- [NASA Armstrong Fact Sheet on the Bell X-2 Starbuster][ref_nasa_x2_factsheet]
- [NASA Armstrong Flight Research Center][ref_nasa_armstrong]
- [NASA History Office][ref_nasa_history]
- [NASA Technical Reports Server][ref_ntrs]
- [Wikipedia Article on Bell Aircraft][ref_bell_aircraft]
- [Wikipedia Article on Creep Deformation][ref_creep_deformation]
- [Wikipedia Article on Curtiss-Wright][ref_curtiss_wright]
- [Wikipedia Article on Directional Stability][ref_directional_stability]
- [Wikipedia Article on Duralumin][ref_duralumin]
- [Wikipedia Article on Dutch Roll][ref_dutch_roll]
- [Wikipedia Article on Dynamic Pressure][ref_dynamic_pressure]
- [Wikipedia Article on Edwards Air Force Base][ref_edwards_afb]
- [Wikipedia Article on Euler's Equations for Rigid Body Dynamics][ref_euler_equations_rigid]
- [Wikipedia Article on Experimental Aircraft][ref_experimental_aircraft]
- [Wikipedia Article on Flight Dynamics][ref_flight_dynamics]
- [Wikipedia Article on Flight Testing][ref_flight_test]
- [Wikipedia Article on Flow Separation][ref_flow_separation]
- [Wikipedia Article on Frank Everest][ref_everest]
- [Wikipedia Article on Heat Flux][ref_heat_flux]
- [Wikipedia Article on Hypersonic Flight][ref_hypersonic_flight]
- [Wikipedia Article on Inconel][ref_inconel]
- [Wikipedia Article on Inertia Coupling][ref_inertia_coupling]
- [Wikipedia Article on Iven Kincheloe][ref_kincheloe]
- [Wikipedia Article on Liquid Oxygen][ref_liquid_oxygen]
- [Wikipedia Article on Longitudinal Static Stability][ref_longitudinal_static_stability]
- [Wikipedia Article on Measurement Uncertainty][ref_measurement_uncertainty]
- [Wikipedia Article on Milburn G. Apt][ref_mel_apt]
- [Wikipedia Article on Monel][ref_monel]
- [Wikipedia Article on NASA][ref_nasa]
- [Wikipedia Article on Propagation of Uncertainty][ref_propagation_of_uncertainty]
- [Wikipedia Article on Specific Impulse][ref_specific_impulse]
- [Wikipedia Article on Stagnation Temperature][ref_stagnation_temperature]
- [Wikipedia Article on Stainless Steel][ref_stainless_steel]
- [Wikipedia Article on Supersonic Speed][ref_supersonic_speed]
- [Wikipedia Article on Telemetry][ref_telemetry]
- [Wikipedia Article on the Accelerometer][ref_accelerometer]
- [Wikipedia Article on the Aerodynamic Center][ref_aerodynamic_center]
- [Wikipedia Article on the Armstrong Flight Research Center][ref_armstrong_frc]
- [Wikipedia Article on the Aspect Ratio][ref_aspect_ratio]
- [Wikipedia Article on the Bell X-1][ref_bell_x1]
- [Wikipedia Article on the Bell X-2][ref_bell_x2]
- [Wikipedia Article on the Bell X-5][ref_bell_x5]
- [Wikipedia Article on the Biot Number][ref_biot_number]
- [Wikipedia Article on the Boeing B-50 Superfortress][ref_b50]
- [Wikipedia Article on the Boundary Layer][ref_boundary_layer]
- [Wikipedia Article on the Douglas X-3 Stiletto][ref_douglas_x3]
- [Wikipedia Article on the Drag Coefficient][ref_drag_coefficient]
- [Wikipedia Article on the Ejection Seat][ref_ejection_seat]
- [Wikipedia Article on the Escape Crew Capsule][ref_escape_crew_capsule]
- [Wikipedia Article on the Flight Envelope][ref_flight_envelope]
- [Wikipedia Article on the Fourier Number][ref_fourier_number]
- [Wikipedia Article on the Heat Equation][ref_heat_equation]
- [Wikipedia Article on the International Standard Atmosphere][ref_isa]
- [Wikipedia Article on the Karman Line][ref_karman_line]
- [Wikipedia Article on the Lift Coefficient][ref_lift_coefficient]
- [Wikipedia Article on the Lift-to-Drag Ratio][ref_lift_to_drag]
- [Wikipedia Article on the Load Factor][ref_load_factor]
- [Wikipedia Article on the Lockheed SR-71 Blackbird][ref_sr71]
- [Wikipedia Article on the Mach Number][ref_mach_number]
- [Wikipedia Article on the Moment of Inertia][ref_moment_of_inertia]
- [Wikipedia Article on the National Advisory Committee for Aeronautics][ref_naca]
- [Wikipedia Article on the National Museum of the United States Air Force][ref_nmusaf]
- [Wikipedia Article on the North American F-100 Super Sabre][ref_f100]
- [Wikipedia Article on the North American X-15][ref_na_x15]
- [Wikipedia Article on the North American XB-70 Valkyrie][ref_xb70]
- [Wikipedia Article on the Northrop X-4 Bantam][ref_northrop_x4]
- [Wikipedia Article on the Oblique Shock][ref_oblique_shock]
- [Wikipedia Article on the Phugoid][ref_phugoid]
- [Wikipedia Article on the Prandtl Number][ref_prandtl_number]
- [Wikipedia Article on the Reaction Control System][ref_rcs]
- [Wikipedia Article on the Reynolds Number][ref_reynolds_number]
- [Wikipedia Article on the Rocket Engine][ref_rocket_engine]
- [Wikipedia Article on the Shock Wave][ref_shock_wave]
- [Wikipedia Article on the Sound Barrier][ref_sound_barrier]
- [Wikipedia Article on the Speed of Sound][ref_speed_of_sound]
- [Wikipedia Article on the Stabilator][ref_stabilator]
- [Wikipedia Article on the Stefan-Boltzmann Law][ref_stefan_boltzmann]
- [Wikipedia Article on the Strain Gauge][ref_strain_gauge]
- [Wikipedia Article on the Swept Wing][ref_swept_wing]
- [Wikipedia Article on the Thermocouple][ref_thermocouple]
- [Wikipedia Article on the Tsiolkovsky Rocket Equation][ref_tsiolkovsky]
- [Wikipedia Article on the Turbopump][ref_turbopump]
- [Wikipedia Article on the U.S. Standard Atmosphere][ref_us_standard_atmosphere]
- [Wikipedia Article on the Wind Tunnel][ref_wind_tunnel]
- [Wikipedia Article on Thermal Conductivity][ref_thermal_conductivity]
- [Wikipedia Article on Thermal Expansion][ref_thermal_expansion]
- [Wikipedia Article on Thermal Stress][ref_thermal_stress]
- [Wikipedia Article on Titanium Alloys][ref_titanium_alloys]
- [Wikipedia Article on Transonic Flow][ref_transonic]
- [Wikipedia Article on Wave Drag][ref_wave_drag]
- [Wikipedia Article on Wing Loading][ref_wing_loading]
- [Wikipedia Article on Yield in Engineering][ref_yield_strength]
- [Wikipedia List of X-Planes][ref_list_of_x_planes]

### Research

- [A special escape capsule 1952][research_a_special_1952]
- [A study of the 1973][research_oblique_wing_divergence_1973]
- [A supersonic parachute 1949][research_a_supersonic_1949]
- [A System Analysis of 2004][research_a_system_2004]
- [A Thermocouple for Transient 1962][research_a_thermocouple_1962]
- [A'Harrah 2007][research_aharrah_2007]
- [A.Yu. et al 2023][research_ayu_aa_2023]
- [Aamir et al 2026][research_aamir_abbasi_2026]
- [Abarbanel 1977][research_abarbanel_1977]
- [Abbas et al 1992][research_abbas_ibrahim_1992]
- [Abbas et al 2012][research_abbas_rui_2012]
- [Abbe et al 1967][research_abbe_mclaughlin_1967]
- [Abdelkefi et al 2011][research_abdelkefi_vasconcellos_2011]
- [Abdollahi and Ehsani 2016][research_abdollahi_ehsani_2016]
- [Abdulwahab 2009][research_nabdulwahab_2009]
- [Abe 2021][research_abe_2021]
- [Abe et al 2016][research_abe_tabuchi_2016]
- [Abensur 2008][research_abensur_2008]
- [Abou-Amer 2020][research_abouamer_2020]
- [Abramov and Butkovskii 2018][research_abramov_butkovskii_2018]
- [Abramov et al 2005][research_abramov_goman_2005]
- [Abuaf 1976][research_abuaf_1976]
- [Abuaf et al 1997][research_abuaf_dorri_1997]
- [Ackeret 1925][research_ackeret_1925]
- [Adams 1972][research_adams_1972]
- [Adams 1972][research_adamsjr_1972]
- [Adams 1974][research_adams_1974]
- [Adams 2014][research_adams_2014]
- [Adams and Rubin 1958][research_adams_rubin_1958]
- [Adkins and Armstrong 1965][research_adkins_armstrong_1965]
- [Advanced Fuel Research Inc East Hartford Ct 1957][research_advancedfuelresearchinceasthartfordct_1957]
- [Advanced Metallics for High-Temperature 1992][research_advanced_metallics_1992]
- [Advani and Field 2011][research_advani_field_2011]
- [Advani et al 2016][research_advani_schroeder_2016]
- [Aero has finished upgraded 2006][research_aero_has_2006]
- [Aerodynamic and Landing Measurements 1960][research_aerodynamic_and_1960]
- [Aerodynamic and Static Aeroelastic 2014][research_aerodynamic_and_2014]
- [Aerodynamic Components of Aircraft 1957][research_aerodynamic_components_1957]
- [Aerodynamic Heating and Thermal 1978][research_aerodynamic_heating_1978]
- [Aerodynamic Phenomena in Supersonic 2020][research_aerodynamic_phenomena_2020]
- [Aeroelastic Tests of an 1963][research_aeroelastic_tests_1963]
- [Aerothermal Environment for the 1978][research_aerothermal_environment_1978]
- [Agarwal 1982][research_agarwal_1982]
- [Agarwal et al 1992][research_agarwal_miley_1992]
- [Ageev and Pavlenko 2016][research_ageev_pavlenko_2016]
- [Ageev et al 2020][research_ageev_sosura_2020]
- [Agrawal et al 1991][research_agrawal_kinard_1991]
- [AHarrah 2007][research_aharrah_2007_b]
- [Ahmad et al 2014][research_ahmad_rahman_2014]
- [Ahmadi and Pourshahsavari 2016][research_ahmadi_pourshahsavari_2016]
- [Ahmed and Worley 2008][research_ahmed_worley_2008]
- [Ahmed et al 1989][research_ahmed_wentz_1989]
- [Ahmed, et al 2011][research_y_n_2011]
- [Ai and Qu 2011][research_ai_qu_2011]
- [Air Force Test Pilot School Edwards Afb Ca 1989][research_airforcetestpilotschooledwardsafbca_1989]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990]
- [Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991]
- [Aircraft crew escape system 2014][research_aircraft_crew_2014]
- [Aircraft Flight Control Systems][research_aircraft_flight]
- [Aircraft lateral-directional handling qualities 2011][research_aircraft_lateral_directional_2011]
- [Aircraft Stability and Control 2003][research_aircraft_stability_2003]
- [Aircraft Stability and Control 2014][research_aircraft_stability_2014]
- [Aircraft Stability and Control 2024][research_aircraft_stability_2024]
- [Airplane and rocket flight 1990][research_airplane_and_1990]
- [Akaydin et al 2015][research_akaydin_moiniyekta_2015]
- [Akcal et al 2018][research_akcal_hostas_2018]
- [Akmandor and Nagashima 1999][research_akmandor_nagashima_1999]
- [Al Bakri][research_albakri]
- [AL-Bakri and Kluever 2017][research_albakri_kluever_2017]
- [Al-Bakri et al 2020][research_albakri_2020]
- [Al-Khaleefi 2004][research_alkhaleefi_2004]
- [Alaian et al 2016][research_alaian_basuno_2016]
- [Alam et al 2010][research_alam_rao_2010]
- [Alcock and Hagar 1989][research_alcock_hagar_1989]
- [Alder 2014][research_alder_2014]
- [Alder 2015][research_alder_2015]
- [Alemdaroglu et al 2002][research_alemdaroglu_iyigun_2002]
- [Alexander 1948][research_alexander_1948]
- [Alexander 1970][research_alexander_1970]
- [Alfano et al 2014][research_alfano_gardi_2014]
- [Alighanbari 2002][research_alighanbari_2002]
- [Alkidas and Durbetaki 1972][research_alkidas_durbetaki_1972]
- [Alle 1967][research_alle_1967]
- [Allee 1976][research_allee_eg_1976]
- [Allen 1972][research_allen_1972]
- [Allen 2004][research_allen_2004]
- [Allen et al 2004][research_allen_keustermans_2004]
- [Alnaser et al 2021][research_alnaser_yunus_2021]
- [Alsaif et al 2015][research_alsaif_foda_2015]
- [Altgelt and Ward 1968][research_altgelt_ward_1968]
- [Altunkaya and Catak 2025][research_altunkaya_2025]
- [Alvi 2012][research_alvi_2012]
- [Aly et al 2002][research_aly_ogot_2002]
- [Alyanak and Pendleton 2014][research_alyanak_pendleton_2014]
- [Alyanak and Pendleton 2017][research_alyanak_pendleton_2017]
- [Amano and Momose 1992][research_amano_momose_1992]
- [Amendola et al 2018][research_amendola_dimino_2018]
- [Amirzadegan 2026][research_amirzadegan_2026]
- [An Aeroelastic Metamodel Based 2013][research_an_aeroelastic_2013]
- [An et al 2023][research_an_jiepan_2023]
- [An Evaluation of the 1970][research_an_evaluation_1970]
- [An experimental and computational 1978][research_an_experimental_1978]
- [An Introduction to the 1966][research_an_introduction_1966]
- [Analysis of the Stability 2024][research_analysis_of_the_2024]
- [Ananthkrishnan 2004][research_ananthkrishnan_2004]
- [Ananthkrishnan and Sinha 2023][research_ananthkrishnan_sinha_2023]
- [Anderson 1959][research_anderson_1959]
- [Anderson 1960][research_anderson_1960]
- [Anderson 1965][research_anderson_1965]
- [Anderson 1968][research_anderson_1968]
- [Anderson 1968][research_anderson_1968_b]
- [Anderson 1968][research_andersonjr_1968]
- [Anderson and Bray 1955][research_pitchup_evaluation_1955]
- [Anderson and Innis 1965][research_anderson_innis_1965]
- [Anderson and Schroers 1972][research_anderson_schroers_1972]
- [Anderson et al 1995][research_anderson_ryan_1995]
- [Anderson et al 2010][research_anderson_campbell_2010]
- [Anderson et al 2012][research_anderson_son_2012]
- [Anderson et al 2013][research_anderson_heister_2013]
- [Anderson et al 2015][research_anderson_heister_2015]
- [Ando 2017][research_ando_2017]
- [Andreopoulos 1982][research_andreopoulos_1982]
- [Andrew 1981][research_andrew_1981]
- [Andrews 1977][research_andrews_1977]
- [Anikina et al 2026][research_anikina_renshaw_2026]
- [Aniskin et al 2015][research_aniskin_mironov_2015]
- [Anthony 2005][research_anthony_2005]
- [Antonov 1971][research_antonov_1971]
- [Anwar et al 2022][research_anwar_mabruri_2022]
- [Aoki and Ota 1986][research_aoki_ota_1986]
- [Appendix G Development of 2003][research_appendix_g_2003]
- [Approximate Expressions for the 2007][research_approximate_expressions_2007]
- [Aprovitola et al 2021][research_aprovitola_dinuzzo_2021]
- [Aprovitola et al 2022][research_aprovitola_dyblenko_2022]
- [Arabshahi et al 2011][research_arabshahi_taylor_2011]
- [Arai et al 2000][research_arai_noto_2000]
- [Arc-Heater Code-Validation Tests of 1978][research_arc_heater_code_validation_1978]
- [Archambaud et al 2004][research_archambaud_louis_2004]
- [Archambaud et al 2009][research_archambaud_arnal_2009]
- [Armstrong 1977][research_armstrong_1977]
- [Armstrong 1979][research_armstrong_1979]
- [Armstrong 1989][research_armstrong_1989]
- [Armstrong and Kilner 1953][research_armstrong_kilner_1953]
- [Armstrong and Miller 1968][research_armstrong_miller_1968]
- [Armstrong and Schlumberger 1990][research_armstrong_schlumberger_1990]
- [Army War Coll Carlisle Barracks Pa 1952][research_armywarcollcarlislebarrackspa_1952]
- [Arnal et al 1990][research_arnal_vignau_1990]
- [Arnette et al 1995][research_arnette_samimy_1995]
- [Arnold 1942][research_arnold_1942]
- [Arnold 1968][research_arnold_1968]
- [Aronov and Klyagin 2021][research_aronov_klyagin_2021]
- [Aryaman et al 2023][research_aryaman_naveenraj_2023]
- [As'ad et al 2022][research_asad_avery_2022]
- [As'ad et al 2024][research_asad_avery_2024]
- [Asadi and Wang 2017][research_asadi_wang_2017]
- [Asghar et al 2018][research_asghar_allan_2018]
- [Asher et al 1957][research_asher_martuccelli_1957]
- [Ashkenas 1965][research_ashkenas_1965]
- [Ashokkumar 2023][research_ashokkumar_2023]
- [Ashraf and Van Kampen 2020][research_ashraf_vankampen_2020]
- [Ashworth et al 1988][research_ashworth_mouch_1988]
- [Askari and Cremaschi 2023][research_askari_2023]
- [Aslam et al 2025][research_aslam_islam_2025]
- [Assessment of Key Aerothermal 1992][research_assessment_of_1992]
- [Atabay et al 2021][research_atabay_sanchezmata_2021]
- [Atik et al 2012][research_atik_baran_2012]
- [Attinello 1956][research_attinello_1956]
- [Automatic flight control system 2000][research_automatic_flight_2000]
- [Av and Jayabalakrishnan 2026][research_av_d_2026]
- [Avanzini and Matteis 1997][research_avanzini_matteis_1997]
- [Awadalla Ali Haj Ahmed 2024][research_awadallaalihajahmed_2024]
- [Ayran et al 2026][research_ayran_bayezit_2026]
- [Azzouz et al 2011][research_azzouz_smith_2011]
- [Baals and Harris 1968][research_baals_harrisjr_1968]
- [Baals et al 1970][research_baals_robins_1970]
- [Babcock and Wiltse 1965][research_babcock_wiltse_1965]
- [Baber et al 1962][research_baber_carter_1962]
- [Babineaux and Horton 1966][research_babineaux_horton_1966]
- [Babinsky 2007][research_babinsky_2007]
- [Babinsky 2014][research_babinsky_2014]
- [Babish III 1966][research_babishiii_1966]
- [Babister 1980][research_babister_1980]
- [Babister 1980][research_babister_1980_b]
- [Babu et al 2018][research_babu_murty_2018]
- [Babucke and Rist 2009][research_babucke_rist_2009]
- [Bachalo et al 1977][research_bachalo_modarress_1977]
- [Back and Cuffel 1970][research_back_cuffel_1970_b]
- [Back and Cuffel 1970][research_back_cuffel_1970_c]
- [Back and Cuffel 1971][research_back_cuffel_1971]
- [Back and Cuffel 1972][research_back_cuffel_1972]
- [Back et al 1966][research_back_cuffel_1966]
- [Back et al 1967][research_back_cuffel_1967]
- [Back et al 1970][research_back_cuffel_1970]
- [Back et al 1984][research_back_cuffel_1984]
- [Bade 1962][research_bade_1962]
- [Bade 1975][research_bade_1975]
- [Badiei et al 2014][research_badiei_sadr_2014]
- [Bae et al 2005][research_bae_seigler_2005]
- [Baer 1966][research_baer_1966]
- [Baer-Riedhart 1981][research_baerriedhart_1981]
- [Baghdadi et al 2009][research_baghdadi_lowenberg_2009]
- [Baghdadi et al 2011][research_baghdadi_lowenberg_2011]
- [Bagheri et al 1990][research_bagheri_strataridakis_1990]
- [Bahrami 2012][research_bahrami_2012]
- [Bai et al 1994][research_bai_hou_1994]
- [Bai et al 2015][research_bai_li_2015]
- [Bai et al 2020][research_bai_cheng_2020]
- [Bai et al 2022][research_bai_cao_2022]
- [Baier et al 2019][research_baier_karnam_2019]
- [Bairamov and Bairamov 2022][research_bairamov_bairamov_2022]
- [Bajpai et al 2008][research_bajpai_beytin_2008]
- [Baker][research_baker]
- [Baker 1967][research_baker_1967]
- [Baker 1968][research_baker_1968]
- [Baker 1969][research_baker_1969]
- [Balachandran and Atkins 2014][research_balachandran_atkins_2014]
- [Balachandran and Atkins 2016][research_balachandran_atkins_2016]
- [Balakrishnan and Kurian 2014][research_balakrishnan_kurian_2014]
- [Balas et al 1996][research_balas_packard_1996]
- [Balepin 2006][research_balepin_2006]
- [Banerjee and Utreja 1975][research_banerjee_utreja_1975]
- [Banks 2008][research_banks_2008]
- [Banks 2008][research_banks_2008_b]
- [Banks et al 2012][research_banks_frederick_2012]
- [Banks et al 2012][research_banks_fredericks_2012]
- [Banner et al 1958][research_transition_flight_1958]
- [Banner et al 1962][research_x15_heating_1962]
- [Bano et al 2026][research_bano_fraser_2026]
- [Bao et al 2021][research_bao_zhou_2021]
- [Barbosa et al 2019][research_barbosa_bertolin_2019]
- [Barlog 1979][research_barlog_1979]
- [Barlow et al 2012][research_barlow_stepanyan_2012]
- [Barnhardt et al 2007][research_barnhardt_drayna_2007]
- [Barnwell 1989][research_barnwell_1989]
- [Barr 1971][research_barr_1971]
- [Barrett 1982][research_barrett_1982]
- [Barrett 1992][research_barrett_1992]
- [Barrett 1997][research_barrett_1997]
- [Barrett 1999][research_barrett_1999]
- [Barrett and Lowell 1974][research_barrett_lowell_1974]
- [Barrett and Lowell 1981][research_barrett_lowell_1981]
- [Barrett-Gonzalez and Wolf 2021][research_barrettgonzalez_wolf_2021]
- [Barry and Bassick 1995][research_barry_bassick_1995]
- [Barthelemy and Bergen 1988][research_barthelemy_bergen_1988]
- [Barthelemy and Bergen 1989][research_barthelemy_bergen_1989]
- [Bartlett and Harris 1972][research_bartlett_harris_1972]
- [Bartlett and Re 1972][research_bartlett_re_1972]
- [Bartlett et al 1973][research_bartlett_harris_1973]
- [Barton et al 2021][research_barton_zaremba_2021]
- [Bartz 1955][research_bartz_1955]
- [Bartz 1965][research_bartz_1965]
- [Barufaldi et al 2020][research_nbarufaldi_hvictorjr_2020]
- [Baryshev et al 1972][research_baryshev_vinogradov_1972]
- [Bashkin et al 2005][research_bashkin_egorov_2005]
- [Bashu et al 1987][research_bashu_singh_1987]
- [Bassett et al 2018][research_bassett_pei_2018]
- [Bassina et al 2001][research_bassina_strelets_2001]
- [Bateman 2010][research_bateman_2010]
- [Battaglia et al 2024][research_battaglia_baldieri_2024]
- [Bauer and Wood 1989][research_bauer_wood_1989]
- [Bauer et al 1978][research_bauer_winkler_1978]
- [Bauerle 1961][research_bauerle_1961]
- [Baum and Levine 1984][research_baum_levine_1984]
- [Bazarov 1994][research_bazarov_1994]
- [Bazarov 1998][research_bazarov_1998]
- [Bazile and Calderara 2012][research_bazile_calderara_2012]
- [Beck 1984][research_beck_1984]
- [Beck 1984][research_beck_1984_b]
- [Beeler 1961][research_x15_conference_1958]
- [Beeler et al 1956][research_beeler_1956]
- [Behrens 1971][research_behrens_1971]
- [Belcastro][research_belcastro]
- [Belcastro 2011][research_belcastro_2011]
- [Belcastro 2012][research_belcastro_2012]
- [Belcastro 2012][research_belcastro_2012_b]
- [Belcastro 2014][research_loc_directions_2014]
- [Belcastro and Foster 2010][research_belcastro_foster_2010]
- [Belcastro and Jacobson 2010][research_belcastro_jacobson_2010]
- [Belcastro et al 2005][research_belcastro_khong_2005]
- [Belcastro et al 2005][research_belcastro_khong_2005_b]
- [Belcastro et al 2014][research_loc_precursors_2014]
- [Belcastro et al 2016][research_belcastro_newman_2016]
- [Beldica and Hilton 1999][research_beldica_hilton_1999]
- [Beldica et al 2001][research_beldica_hilton_2001]
- [Bell 1963][research_bell_1963]
- [Bellman 1959][research_transonic_summary_1959]
- [Bellows et al 1984][research_bellows_brewster_1984]
- [Belnap et al 2002][research_belnap_vanrij_2002]
- [Beltran and Kosvic 1966][research_beltran_kosvic_1966]
- [Belyavin et al 2014][research_belyavin_kurenkova_2014]
- [Ben-Gida and Gurka 2022][research_bengida_gurka_2022]
- [Benditt 1963][research_benditt_1963]
- [Bengtson et al 1975][research_bengtson_dickovich_1975]
- [Benjamin and McConnaughey 1991][research_benjamin_mcconnaughey_1991]
- [Bennet-Clark 1972][research_bennetclark_1972]
- [Bentsman et al 1991][research_bentsman_wilcutts_1991]
- [Beran et al 2005][research_beran_hur_2005]
- [Berci 2017][research_berci_2017]
- [Beresh et al 2010][research_beresh_henfling_2010]
- [Berg 1991][research_berg_1991]
- [Berger et al 2011][research_berger_anderson_2011]
- [Berger et al 2011][research_berger_carmona_2011]
- [Bergstrom and Raghunathan 1972][research_bergstrom_raghunathan_1972]
- [Bermudez 2024][research_bermudez_2024]
- [Bernal 2016][research_bernal_2016]
- [Berry and Powers 1970][research_berry_powers_1970]
- [Berry et al 1976][research_berry_mallick_1976]
- [Berry et al 2006][research_berry_horvath_2006]
- [Berry et al 2008][research_berry_horvath_2008]
- [Berry et al 2016][research_blt_shuttle_2016]
- [Bertelrud 1981][research_bertelrud_1981]
- [Bettles and Gibson 2003][research_bettles_gibson_2003]
- [Betts and Frederick 2010][research_throttling_history_2010]
- [Bewlay et al 1999][research_bewlay_jackson_1999]
- [Bhagwandin and Sahu 2011][research_bhagwandin_sahu_2011]
- [Bhagwandin and Sahu 2013][research_bhagwandin_sahu_2013]
- [Bhagwandin and Sahu 2014][research_bhagwandin_sahu_2014]
- [Bhatia and Beran 2017][research_bhatia_beran_2017]
- [Bi et al 2017][research_bi_xie_2017]
- [Bian et al 2024][research_bian_li_2024]
- [Biao et al 2024][research_biao_changlin_2024]
- [Biberman et al 1978][research_biberman_bronin_1978]
- [Biberman et al 1978][research_biberman_bronin_1978_b]
- [Bigler 1986][research_bigler_1986]
- [Bihrle and Barnhart 1982][research_bihrle_barnhart_1982]
- [Bippes 1990][research_bippes_1990]
- [Birckelbaw 1992][research_birckelbaw_1992]
- [Birman 1989][research_birman_1989]
- [Bischoff and Palmer 1982][research_bischoff_palmer_1982]
- [Bischoff and Palmer 1983][research_bischoff_palmer_1983]
- [Bisek and Brown 2015][research_bisek_brown_2015]
- [Bishop 1951][research_bishop_1951]
- [Bismarck-Nasr 1993][research_bismarcknasr_1993]
- [Bismarck-Nasr and Bones 2000][research_bismarcknasr_bones_2000]
- [Biswas et al 2026][research_biswas_michels_2026]
- [Blachowski and Ostrowski 2001][research_blachowski_ostrowski_2001]
- [Blaha 1969][research_blaha_1969]
- [Blair and Edwards 1982][research_blair_edwards_1982]
- [Blair and Weisshaar 1982][research_blair_weisshaar_1982]
- [Blake et al 2009][research_blake_gotwald_2009]
- [Blanchard and Raper 1960][research_blanchard_raper_1960]
- [Blanchard et al 1996][research_blanchard_wilmoth_1996]
- [Bland 1980][research_fsw_airfoil_divergence_1980]
- [Blank 1995][research_blank_1995]
- [Blood et al 2015][research_blood_ivanov_2015]
- [Bloxsom 1958][research_bloxsom_1958]
- [Bloy and Lea 1995][research_bloy_lea_1995]
- [Blue and Low 1953][research_blue_low_1953]
- [Bochkarev and Matveyenko 2008][research_bochkarev_matveyenko_2008]
- [Boehm et al 2001][research_boehm_flick_2001]
- [Bogdnoff 1953][research_bogdnoff_1953]
- [Bogdonoff and Kepler 1955][research_bogdonoff_kepler_1955]
- [Bogucz et al 1988][research_bogucz_dirik_1988]
- [Bohlmann et al 1990][research_bohlmann_eckstrom_1990]
- [Bohon and Dixon 1964][research_bohon_dixon_1964]
- [Boland et al 1993][research_boland_riley_1993]
- [Bolas 1929][research_bolas_1929]
- [Boling and Zha 2021][research_boling_zha_2021]
- [Bollech and Kelly 1954][research_bollech_kelly_1954]
- [Bolton 2014][research_bolton_2014]
- [Bolton and Collins 1975][research_bolton_collins_1975]
- [Bonavolontà et al 2024][research_bonavolonta_manoj_2024]
- [Bond et al 2008][research_bond_canfield_2008]
- [Bonnema and Smith 1988][research_bonnema_smith_1988]
- [Booker and Booker 1980][research_booker_booker_1980]
- [Booker and Booker 1980][research_booker_booker_1980_b]
- [Booker et al 1982][research_booker_booker_1982]
- [Boothe 1971][research_boothe_1971]
- [Boskovic et al 2005][research_boskovic_bergstrom_2005]
- [Bosson et al 1993][research_bosson_caisso_1993]
- [Bott and Bradshaw 1998][research_bott_bradshaw_1998]
- [Boustani et al 2019][research_boustani_barad_2019]
- [Boustani et al 2020][research_boustani_anugrah_2020]
- [Boustani et al 2022][research_boustani_kenway_2022]
- [Bower and Thomas 2018][research_bower_thomas_2018]
- [Bowers 1980][research_bowers_1980]
- [Bowman 1967][research_bowman_1967]
- [Bowman 1995][research_bowman_1995]
- [Bowman and Healy 1960][research_spin_tunnel_1960]
- [Bowman et al 1978][research_bowmanjr_stough_1978]
- [Boyd 1965][research_boyd_1965]
- [Boyd 1977][research_boyd_1977]
- [Boyden 1974][research_supercritical_dynamic_1974]
- [Boyer et al 2016][research_boyer_mcnamara_2016]
- [Bozack 1970][research_bozack_1970]
- [Bozack and Doerr 1981][research_bozack_doerr_1981]
- [Bozeman et al 2018][research_bozeman_tai_2018]
- [Bradfield and Thomasson 1966][research_bradfield_thomasson_1966]
- [Bradley et al 1969][research_bradley_johnston_1969]
- [Bradley et al 2018][research_bradley_sharp_2018]
- [Brady et al 1996][research_brady_brindley_1996]
- [Brady et al 1997][research_brady_smialek_1997]
- [Brandeau 1978][research_brandeau_1978]
- [Brandeau et al 2015][research_brandeau_gallon_2015]
- [Brandon et al 1979][research_brandon_britt_1979]
- [Brandt and Bons 2024][research_brandt_bons_2024]
- [Braslow 1966][research_braslow_1966]
- [Braun 1959][research_braun_1959]
- [Brazzel 1963][research_brazzel_1963]
- [Brenckmann 1964][research_brenckmann_1964]
- [Brenner et al 2005][research_brenner_thompson_2005]
- [Breshears et al 1966][research_breshears_mccafferty_1966]
- [Breshears et al 1967][research_breshears_mccafferty_1967]
- [Brewster 2014][research_brewster_2014]
- [Brice and Sugano 1978][research_brice_sugano_1978]
- [Bridges 2008][research_bridges_2008]
- [Brincklow et al 2021][research_brincklow_montgomery_2021]
- [Brincklow et al 2024][research_brincklow_montgomery_2024]
- [Brinkman 1992][research_brinkman_1992]
- [Brinkman et al 1991][research_brinkman_booker_1991]
- [Brittain 1989][research_brittain_1989]
- [Brociek et al 2023][research_brociek_hetmaniok_2023]
- [Brodrick 1962][research_brodrick_1962]
- [Brodsky 1970][research_brodsky_1970]
- [Bromfield and Landry 2019][research_bromfield_landry_2019]
- [Brooke 1957][research_brooke_1957]
- [Brooks 1971][research_brooks_1971]
- [Brooks and Dejarnette 1970][research_brooksjr_dejarnette_1970]
- [Brooks and Ransbury 2012][research_brooks_ransbury_2012]
- [Brooks et al 2017][research_brooks_gupta_2017]
- [Brossard et al 2005][research_brossard_balmain_2005]
- [Brossard et al 2013][research_brossard_bouchaud_2013]
- [Brown 1989][research_brown_1989]
- [Brown 2022][research_brown_2022]
- [Brownfield and Badger 1960][research_brownfield_badger_1960]
- [Brownlee 1963][research_brownlee_1963]
- [Brundrett et al 1972][research_brundrett_nicoll_1972]
- [Bruner 1983][research_bruner_1983]
- [Brunner 1959][research_brunner_1959]
- [Brunner and Nerem 1970][research_brunner_nerem_1970]
- [Brunton et al 2020][research_brunton_noack_2020]
- [Bryson 1954][research_bryson_1954]
- [Bryson 1969][research_brysonjr_1969]
- [Bryson and Edwards 1952][research_bryson_edwards_1952]
- [Buchanan and Cayse 1988][research_buchanan_cayse_1988]
- [Buckingham 1914][research_buckingham_1914]
- [Buckmann et al 1989][research_buckmann_shimp_1989]
- [Buckmann et al 1992][research_buckmann_shrimp_1992]
- [Budd Co Fort Washington Pa Technical Center 1978][research_buddcofortwashingtonpatechnicalcenter_1978]
- [Buddhamatya et al 2026][research_buddhamatya_miranda_2026]
- [Bugała 2025][research_bugala_2025]
- [Bugała and Payenskyy 2025][research_bugala_payenskyy_2025]
- [Bugała et al 2023][research_bugala_sznajder_2023]
- [Bui 2013][research_bui_2013]
- [Bui 2016][research_bui_2016]
- [Bui 2018][research_bui_2018]
- [Bull and Kidd 1955][research_bull_kidd_1955]
- [Bull et al 1997][research_propulsion_backup_1997]
- [Buller 2017][research_buller_2017]
- [Burbank et al 1962][research_burbank_collins_1962]
- [Burcham and Burken 1994][research_burchamjr_burken_1994]
- [Burcham and Pappas 1996][research_burchamjr_pappas_1996]
- [Burcham et al 1993][research_burchamjr_maine_1993]
- [Burdett 1946][research_burdett_1946]
- [Burdett 1947][research_burdett_1947]
- [Burkhart 1980][research_burkhart_1980]
- [Burki-Cohen 2010][research_burkicohen_2010]
- [Burmeister 1994][research_burmeister_1994]
- [Burns 1965][research_burns_1965]
- [Burns and Ray 1967][research_burns_ray_1967]
- [Burris 1966][research_burris_1966]
- [Burris and Hutchins 1970][research_burris_hutchins_1970]
- [Burstein et al 1972][research_burstein_chinitz_1972]
- [Burt 1974][research_burt_1974]
- [Burt 1975][research_burt_1975]
- [Burton and Kneeland 1981][research_burton_kneelandjr_1981]
- [Burton et al 2007][research_burton_loth_2007]
- [Buschulte 1970][research_buschulte_1970]
- [Buschulte 1971][research_buschulte_1971]
- [Bushnell and Tripi 1986][research_bushnell_tripi_1986]
- [Busing 1964][research_busing_1964]
- [Butler 1976][research_butler_1976]
- [Butler et al 1983][research_butler_fleck_1983]
- [Byrne and Pickles 1990][research_byrne_pickles_1990]
- [Byrnes 1951][research_byrnes_1951]
- [Böhnisch et al 2026][research_bohnisch_braun_2026]
- [Bürki-Cohen and Sparko 2008][research_burkicohen_sparko_2008]
- [Cadieux and Barad 2024][research_cadieux_barad_2024]
- [Cadieux and Barad 2025][research_cadieux_barad_2025]
- [Cadieux and Barad 2026][research_cadieux_barad_2026]
- [Cadieux et al 2023][research_cadieux_angel_2023]
- [Cagáň et al 2015][research_cagan_rosa_2015]
- [Cai et al 2005][research_cai_tong_2005]
- [Calculation of Low Aspect 2008][research_calculation_of_2008]
- [Callaghan and Mason 1964][research_callaghan_mason_1964]
- [Calligeros and Dugundji 1963][research_calligeros_dugundji_1963]
- [Campbell and Abramovitz 1975][research_campbell_abramovitz_1975]
- [Campbell et al][research_campbell_grauer]
- [Campbell et al 1965][research_campbell_gebler_1965]
- [Campbell et al 2012][research_campbell_berger_2012]
- [Campbell et al 2021][research_campbell_grauer_2021]
- [Campbell et al 2021][research_campbell_grauer_2021_b]
- [Campo et al 1982][research_campo_ferrara_1982]
- [Candida et al 2019][research_candida_souzadepaula_2019]
- [Candler 2001][research_candler_2001]
- [Cano and Sobel 2016][research_cano_sobel_2016]
- [Cao and Yao 2019][research_cao_yao_2019]
- [Cao et al 2006][research_cao_huang_2006]
- [Cao et al 2020][research_cao_yao_2020]
- [Cao et al 2026][research_cao_siqi_2026]
- [Carafoli 1969][research_carafoli_1969]
- [Carafoli 1969][research_carafoli_1969_b]
- [Carafoli 1969][research_carafoli_1969_c]
- [Carbaugh 2008][research_carbaugh_2008]
- [Carlin and Blair 1983][research_carlin_blair_1983]
- [Carlson 1964][research_carlson_1964]
- [Carlson and Nerem 1968][research_carlson_nerem_1968]
- [Carlson and Schwope 1952][research_carlson_schwope_1952]
- [Carman 1970][research_carman_1970]
- [Carpenter et al 2008][research_carpenter_saric_2008]
- [Carpenter et al 2009][research_carpenter_saric_2009]
- [Carpentieri Rona et al 2018][research_carpentierirona_gonzalezramirez_2018]
- [Carr 1982][research_carr_1982]
- [Carrera et al 2013][research_carrera_varello_2013]
- [Carroll 2015][research_carroll_2015]
- [Carroll and Mehra 1982][research_carroll_mehra_1982]
- [Carroll et al 2011][research_carroll_cabet_2011]
- [Carter and Stearman 1967][research_carter_stearman_1967]
- [Carter and Stearman 1968][research_carter_stearman_1968]
- [Caruso and Mendenhall 1992][research_caruso_mendenhall_1992]
- [Caruso and Naegeli 1976][research_caruso_naegeli_1976]
- [Cary 1968][research_cary_1968]
- [Casiano et al 2009][research_throttling_review_2009]
- [Cassanova 1967][research_cassanova_1967]
- [Catalano and Sturek 2001][research_catalano_sturek_2001]
- [Catalano and Sturek 2001][research_catalano_sturek_2001_b]
- [Cavazzuti 2020][research_cavazzuti_2020]
- [Cella and Biancolini 2012][research_cella_biancolini_2012]
- [Celmins 1990][research_celmins_1990]
- [Cen et al 2020][research_cen_li_2020]
- [Cerantola et al 2024][research_cerantola_handford_2024]
- [Chai et al 2017][research_chai_song_2017]
- [Chai et al 2019][research_chai_li_2019]
- [Chai et al 2020][research_chai_li_2020]
- [Chakravarty 1987][research_chakravarty_1987]
- [Chakravarty and Narayanaswamy 2025][research_chakravarty_narayanaswamy_2025]
- [Chaku and McMahon 1974][research_chaku_mcmahon_1974]
- [Chaloner and Verdinelli 1995][research_chaloner_verdinelli_1995]
- [Chalot et al 1994][research_chalot_mallet_1994]
- [Chalupová et al 2020][research_chalupova_steinbruck_2020]
- [Chambers and Hall 2004][research_chambers_hall_2004]
- [Chan and Chang][research_chan_chang]
- [Chandiramani et al 1995][research_chandiramani_plaut_1995]
- [Chandler 2023][research_chandler_2023]
- [Chandler 2024][research_chandler_2024]
- [Chandler and Herrera 2025][research_chandler_herrera_2025]
- [Chandler et al 2026][research_chandler_herrera_2026]
- [Chandrashekhara 1991][research_chandrashekhara_1991]
- [Chang 1962][research_chang_1962]
- [Chang 1980][research_chang_1980]
- [Chang and Lin 2012][research_chang_lin_2012]
- [Chang and Nottage 1961][research_chang_nottage_1961]
- [Chang et al 1953][research_chang_nordheim_1953]
- [Chang et al 2008][research_chang_kwatny_2008]
- [Chang et al 2016][research_chang_kwatny_2016]
- [Chao and Jeng 1965][research_chao_jeng_1965]
- [Chapleo and Nair 1994][research_chapleo_nair_1994]
- [Chapman and Matting 1965][research_chapman_matting_1965]
- [Chapman and Rubesin 1949][research_chapman_rubesin_1949]
- [Chapman et al 2024][research_chapman_robb_2024]
- [Chapter 3. Aerodynamics of 1957][research_chapter_3_1957]
- [Chapter 3. Aerodynamics of 1960][research_chapter_3_1960]
- [Chapter 4. Wing-Tail Plane 1957][research_chapter_4_1957]
- [Chapter 5. Wing-Body Interference 1957][research_chapter_5_1957]
- [Charles et al 2002][research_charles_lowenberg_2002]
- [Chaudhuri 1977][research_chaudhuri_1977]
- [Chaussee and Enriquez 2026][research_chaussee_enriquez_2026]
- [Chauvin and Speegle 1957][research_chauvin_speegle_1957]
- [Chauvin et al 1968][research_chauvin_erb_1968]
- [Chavez and Vogel 2003][research_chavez_vogel_2003]
- [Chehroudi 2009][research_chehroudi_2009]
- [Chehroudi 2010][research_chehroudi_2010]
- [Chen 1971][research_chen_1971]
- [Chen 1993][research_chen_1993]
- [Chen and Blosser 2002][research_chen_blosser_2002]
- [Chen and Chen 2014][research_chen_chen_2014]
- [Chen and Xie 2024][research_chen_xie_2024]
- [Chen and Zhao 2005][research_chen_zhao_2005]
- [Chen and Zhao 2019][research_chen_zhao_2019]
- [Chen et al 1998][research_chen_chang_1998]
- [Chen et al 2001][research_chen_khalid_2001]
- [Chen et al 2024][research_chen_zhu_2024]
- [Chen et al 2026][research_chen_gray_2026]
- [Chen et al 2026][research_chen_wu_2026]
- [Cheng 1956][research_cheng_1956]
- [Cheng 1982][research_cheng_1982]
- [Cheng 1985][research_cheng_1985]
- [Cheng and Farmer 2002][research_cheng_farmer_2002]
- [Cheng and Fu 2024][research_cheng_fu_2024]
- [Cheng and Pellettiere 2005][research_cheng_pellettiere_2005]
- [Cheng et al 2000][research_cheng_mei_2000]
- [Cheng et al 2002][research_cheng_mei_2002]
- [Cheng et al 2003][research_cheng_lee_2003]
- [Cheng et al 2003][research_cheng_rizer_2003]
- [Cheng et al 2016][research_cheng_fan_2016]
- [Cheng et al 2016][research_cheng_li_2016]
- [Cheng et al 2018][research_cheng_li_2018]
- [Chern et al 2014][research_chern_lobser_2014]
- [Chew 1973][research_chew_1973]
- [Chiang 1980][research_chiang_1980]
- [Chiaverini et al 2002][research_chiaverini_malecki_2002]
- [Childs 1974][research_childs_1974]
- [Childs and Moyer 1985][research_childs_moyer_1985]
- [Chin et al 2020][research_chin_turpin_2020]
- [Chinnaraj et al 2024][research_chinnaraj_kim_2024]
- [Chiozzotto 2016][research_pchiozzotto_2016]
- [Chipman et al 1982][research_chipman_zislin_1982]
- [Chiu 1987][research_chiu_1987]
- [Chiu and Lin 1994][research_chiu_lin_1994]
- [Cho and Chang 2001][research_cho_chang_2001]
- [Cho and Findley 1983][research_cho_findley_1983]
- [Cho et al 2004][research_cho_kim_2004]
- [Choi et al 2020][research_choi_lim_2020]
- [Chopra 1975][research_chopra_1975]
- [Chorunov 2011][research_chorunov_2011]
- [Chou and Childs 1983][research_chou_childs_1983]
- [Chou and Kalina 1982][research_chou_kalina_1982]
- [Chou and Smith 1974][research_chou_smith_1974]
- [Chou and Smith 1978][research_chou_smith_1978]
- [Choudhary 2012][research_choudhary_2012]
- [Chow 1963][research_chow_1963]
- [Chow 1979][research_chow_1979]
- [Chowdhury et al 2021][research_chowdhury_keshmiri_2021]
- [Chu and Xu 2014][research_chu_xu_2014]
- [Chuan et al 2016][research_chuan_feng_2016]
- [Chuban 2020][research_chuban_2020]
- [Chung and Chung 2008][research_chung_chung_2008]
- [Chuvakhov 2020][research_chuvakhov_2020]
- [Chyrkin et al 2010][research_chyrkin_huczkowski_2010]
- [Chyrkin et al 2015][research_chyrkin_sloof_2015]
- [Ciliberti and Nicolosi 2025][research_ciliberti_nicolosi_2025]
- [Ciliberti et al 2017][research_ciliberti_dellavecchia_2017]
- [Clark 1967][research_clark_1967]
- [Clark and Adler 2016][research_clark_adler_2016]
- [Clark et al 2007][research_clark_jones_2007]
- [Clark et al 2015][research_clark_gallon_2015]
- [Clark et al 2015][research_clark_manning_2015]
- [Clarke 1980][research_clarke_1980]
- [Clarke et al 2005][research_clarke_allen_2005]
- [Clarkson 1935][research_clarkson_1935]
- [Clay 2004][research_clay_2004]
- [Coats 1973][research_coats_1973]
- [Cockbill 2018][research_cockbill_2018]
- [Coetzee et al 2013][research_coetzee_krauskopf_2013]
- [Cole 1986][research_fsw_divergence_study_1986]
- [Cole 1990][research_cole_1990]
- [Coleburn and Drimmer 1961][research_coleburn_drimmer_1961]
- [Coleburn and Drimmer 1962][research_coleburn_drimmer_1962]
- [Coleman et al 1983][research_coleman_hodge_1983]
- [Coleman et al 1989][research_coleman_taylor_1989]
- [Coleman et al 2026][research_coleman_lobbia_2026]
- [Collar 1946][research_collar_1946]
- [Collier 1994][research_collier_1994]
- [Collier et al 1987][research_collier_johnson_1987]
- [Collier et al 1990][research_collier_bartlett_1990]
- [Collins et al 1990][research_collins_martinez_1990]
- [Combustion Characteristics of Fuel-rich 2005][research_combustion_characteristics_2005]
- [Combustion Instability Analysis Numerical 1995][research_combustion_instability_1995]
- [Combustion Instability and Transient 2007][research_combustion_instability_2007]
- [Compensated High Temperature Strain 1994][research_compensated_high_1994]
- [Compressible turbulent boundary layer 1970][research_compressible_turbulent_1970]
- [Compton and Cooper 1965][research_compton_cooper_1965]
- [Computational aerodynamic analysis of 1994][research_computational_aerodynamic_1994]
- [Comtois and Glaser 2010][research_comtois_glaser_2010]
- [Connelly 1982][research_connelly_1982]
- [Connors and Sachs 1957][research_connors_sachs_1957]
- [Connors and Swaim 1968][research_connors_swaim_1968]
- [Conrad 1959][research_conrad_1959]
- [Contreras et al 2026][research_contreras_fontanetta_2026]
- [Coogan 2015][research_coogan_2015]
- [Cook 1985][research_cook_1985]
- [Cook 2007][research_cook_2007]
- [Cook 2013][research_cook_2013]
- [Cook and Richards 1977][research_cook_richards_1977]
- [Cookson 1976][research_cookson_1976]
- [Cooper et al 1970][research_cooper_wells_1970]
- [Corda et al 1998][research_corda_neal_1998]
- [Corona-Sanchez and Rodriguez-Cortes 2015][research_coronasanchez_rodriguezcortes_2015]
- [Cosens and Newton 1988][research_cosens_newton_1988]
- [Costigan and Calico 1989][research_costigan_calico_1989]
- [Cosyn and Vierendeels 2005][research_cosyn_vierendeels_2005]
- [Covell et al 1990][research_covell_hernandez_1990]
- [Covell et al 1992][research_covell_walker_1992]
- [Covington 1966][research_covington_1966]
- [Cox 2010][research_cox_2010]
- [Cox et al 2012][research_cox_cunningham_2012]
- [Craig 1971][research_craigjr_1971]
- [Craig and Erbug 1976][research_craig_erbug_1976]
- [Craley and Desabrais 2007][research_craley_desabrais_2007]
- [Crasta and Khan 2014][research_crasta_khan_2014]
- [Creep and stress rupture 1981][research_creep_and_1981]
- [Creep Rupture 2009][research_creep_rupture_2009]
- [Creep Rupture Properties 2004][research_creep_rupture_2004]
- [Crespo et al 2012][research_crespo_kenny_2012]
- [Crew escape propulsion system 2003][research_crew_escape_2003]
- [Crew escape, rescue and][research_crew_escape]
- [Crider 2004][research_crider_2004]
- [Crider 2008][research_crider_2008]
- [Crider 2010][research_crider_2010]
- [Crider 2010][research_crider_2010_b]
- [Crittenden et al 1977][research_crittenden_weisshaar_1977]
- [Crittenden et al 1978][research_crittenden_weishaar_1978]
- [Crocco 1951][research_crocco_1951]
- [Crocco 1952][research_crocco_1952]
- [Crocco 1965][research_crocco_1965]
- [Crocco and Cheng 1953][research_crocco_cheng_1953]
- [Crocco et al 1960][research_crocco_grey_1960]
- [Crocco et al 1962][research_crocco_harrje_1962]
- [Crosby and Griffith 1969][research_crosby_griffith_1969]
- [Crothers 1997][research_crothers_1997]
- [Crown and Heybey 1950][research_crown_heybey_1950]
- [Cui and Lundin 2004][research_cui_lundin_2004]
- [Culick and Jahnke 1988][research_culick_jahnke_1988]
- [Cummings and Adams 1982][research_cummings_adams_1982]
- [Cunis][research_cunis]
- [Cunis 2025][research_cunis_2025]
- [Cunis et al 2020][research_cunis_liaomcpherson_2020]
- [Cunningham 1972][research_cunningham_1972]
- [Cunningham 2017][research_cunningham_2017]
- [Cunningham et al 2008][research_subscale_upset_2008]
- [Cunningham et al 2019][research_stall_training_2019]
- [Currao and Yeh 2026][research_currao_yeh_2026]
- [Curry and Sim 1982][research_curry_sim_1982]
- [Curry et al 1992][research_curry_mendenhall_1992]
- [Curtiss 1971][research_curtiss_1971]
- [Czarnecki et al 1968][research_czarnecki_deveikis_1968]
- [Dahiya 2017][research_dahiya_2017]
- [Dahm 1966][research_dahm_1966]
- [Dai et al 2023][research_dai_zhao_2023]
- [Daidzic et al 1991][research_daidzic_tropea_1991]
- [Dana 1993][research_x15_lessons_1993]
- [Daniels et al 1956][research_daniels_masuda_1956]
- [Danowsky et al 2008][research_danowsky_thompson_2008]
- [Dantsker et al 2017][research_dantsker_ananda_2017]
- [Darden 1984][research_darden_1984]
- [Daryabeigi 2001][research_daryabeigi_2001]
- [Das 2026][research_das_2026]
- [Das et al 2021][research_das_venkatraman_2021]
- [Datta et al][research_datta_wiltsee]
- [Davari and Laitone 1977][research_nonconstant_cma_1977]
- [Davidescu et al 2026][research_davidescu_andrei_2026]
- [Davidson and Andrisani 1996][research_davidson_andrisani_1996]
- [Davies et al 2024][research_davies_parker_2024]
- [Davis][research_davis]
- [Davis 1957][research_davis_1957]
- [Davis 1964][research_davis_1964]
- [Davis and Bendiksen 1993][research_davis_bendiksen_1993]
- [Davis and Flügge-Lotz 1964][research_davis_fluggelotz_1964]
- [Davis and Marshall 2020][research_davis_marshall_2020]
- [Davis et al 2015][research_davis_pedrazzani_2015]
- [Day 1953][research_x2_glide_1953]
- [Day 1997][research_coupling_history_1997]
- [Day and Guthrie 1958][research_day_guthrie_1958]
- [Day and Reisert 1959][research_x2_mach32_1959]
- [Day and Stillwell 1952][research_x2_first_landing_1952]
- [de Carvalho Pereira and Júnior 2003][research_decarvalhopereira_junior_2003]
- [De Chant 1998][research_dechant_1998]
- [De Filippis and Serpico 1998][research_defilippis_serpico_1998]
- [de Melo et al 2024][research_demelo_bussamra_2024]
- [de Nicola et al 1994][research_denicola_tognaccini_1994]
- [de Paula et al 2017][research_depaula_porto_2017]
- [De Tullio et al 2013][research_detullio_paredes_2013]
- [Deangelis 1991][research_deangelis_1991]
- [Deans 1964][research_deans_1964]
- [Debieve et al 1997][research_debieve_dupont_1997]
- [Debrestian and Anderson 1994][research_debrestian_anderson_1994]
- [Dec and Mitcheltree 2002][research_dec_mitcheltree_2002]
- [Deepa and Gupta 2023][research_deepa_gupta_2023]
- [Deere et al 2024][research_deere_viken_2024]
- [Definitions of Aerodynamic Stability 2007][research_definitions_of_2007]
- [DeFries 1971][research_defries_1971]
- [Degani and Smits 1985][research_degani_smits_1985]
- [Degischer et al 1987][research_degischer_aigner_1987]
- [DeGregoria 2015][research_degregoria_2015]
- [Dehua et al 2006][research_dehua_jinjun_2006]
- [Delcher et al 1989][research_delcher_dergevorkian_1989]
- [Della Vecchia et al 2015][research_dellavecchia_nicolosi_2015]
- [Demetriades 1977][research_demetriades_1977]
- [Demetriades 1983][research_demetriades_1983]
- [Demetriades 1985][research_demetriades_1985]
- [Demetriades and McCullough 1985][research_demetriades_mccullough_1985]
- [Deming Zhang et al][research_demingzhang_guiqingchen]
- [Demiyanenko et al 2004][research_demiyanenko_dmitrenko_2004]
- [Demjanenko et al 2003][research_demjanenko_dmitrenko_2003]
- [Dempers et al 1999][research_dempers_nikbin_1999]
- [Dempster and Arnold 1969][research_dempster_arnold_1969]
- [Dempster and Roger 1967][research_dempster_roger_1967]
- [Deng et al 2023][research_deng_wang_2023]
- [Deng et al 2024][research_deng_liu_2024]
- [Deng et al 2024][research_deng_qin_2024]
- [Densification of titanium alloy 2003][research_densification_of_2003]
- [Derkevorkian et al 2019][research_derkevorkian_avery_2019]
- [des Clers and Sternberg 1952][research_desclers_sternberg_1952]
- [Design of Turbopump Propellant 1992][research_design_of_1992]
- [DeSpirito 2009][research_despirito_2009]
- [DeSpirito 2013][research_despirito_2013]
- [DeSpirito 2014][research_despirito_2014]
- [DeSpirito 2015][research_despirito_2015]
- [DeSpirito et al 2008][research_despirito_silton_2008]
- [Devan 1989][research_devan_1989]
- [Development of a Software 2008][research_development_of_2008]
- [Development of Creep-Resistant NiAl Ti,Hf 1997][research_development_of_1997]
- [Development of Longitudinal and 2014][research_development_of_2014]
- [Development of Longitudinal and 2024][research_development_of_2024]
- [Dewa et al 2018][research_dewa_park_2018]
- [Dhosi et al 1963][research_dhosi_widmer_1963]
- [Dhosi et al 1964][research_dhosi_widmer_1964]
- [Diaz 1985][research_diaz_1985]
- [Dicarlo et al 1992][research_dicarlo_brown_1992]
- [Diederich 1951][research_flexible_wing_lateral_1951]
- [Diggins 1951][research_diggins_1951]
- [Dikbas and Atik 2018][research_dikbas_atik_2018]
- [Dillinger et al 2019][research_dillinger_abdalla_2019]
- [Dillman and Stanley 2003][research_dillman_stanley_2003]
- [Dillon et al 1990][research_dillon_king_1990]
- [Dimitrienko et al 2015][research_dimitrienko_koryakov_2015]
- [Din et al 2018][research_din_egorov_2018]
- [Ding and Findley 1982][research_ding_findley_1982]
- [Ding and Subramaniam 1989][research_ding_subramaniam_1989]
- [Dirling et al 1970][research_dirling_rigdon_1970]
- [Disselkoen et al 1989][research_disselkoen_heise_1989]
- [Dixon and Mei 1993][research_dixon_mei_1993]
- [Dmitrenko 2019][research_dmitrenko_2019]
- [Dobos-Bubno and Hartsook 1977][research_dobosbubno_hartsook_1977]
- [Doengi et al 1995][research_doengi_dinkler_1995]
- [Dogan Kuzey and Yıldırım Dalkıran 2026][research_dogankuzey_yildirimdalkiran_2026]
- [Doggett and Soistmann 1989][research_doggettjr_soistmann_1989]
- [Doherr 2003][research_doherr_2003]
- [Dolan 1964][research_dolan_1964]
- [Dolan 1970][research_dolan_1970]
- [Dolgih 2025][research_dolgih_2025]
- [Dombrovsky and Reviznikov 2014][research_dombrovsky_reviznikov_2014]
- [Dombrovsky et al 2016][research_dombrovsky_reviznikov_2016]
- [Donahue 2004][research_donahue_2004]
- [Dong and Fan 1998][research_dong_fan_1998]
- [Dong et al 2011][research_dong_shin_2011]
- [Dong et al 2023][research_dong_huang_2023]
- [Dong et al 2023][research_dong_lu_2023]
- [Dongi et al 1996][research_dongi_dinkler_1996]
- [Dongmo 2011][research_dongmo_2011]
- [Dongmo 2011][research_dongmo_2011_b]
- [Dongmo 2012][research_dongmo_2012]
- [Dongmo 2012][research_dongmo_2012_b]
- [Dongmo 2015][research_dongmo_2015]
- [Dongmo 2015][research_dongmo_2015_b]
- [Dongmo 2016][research_dongmo_2016]
- [Dongmo 2017][research_dongmo_2017]
- [Donovan and Smits 1990][research_donovan_smits_1990]
- [Dorosh and Leontiev 2014][research_dorosh_leontiev_2014]
- [Dorrance 1961][research_dorrance_1961]
- [Dorrance and Dore 1954][research_dorrance_dore_1954]
- [Doubrava et al 2008][research_doubrava_waszniowski_2008]
- [Dougherty and Fisher 1980][research_dougherty_fisher_1980]
- [Douglas Aircraft Co Long Beach Ca 1983][research_douglasaircraftcolongbeachca_1983]
- [Dovgal et al 1990][research_dovgal_levchenko_1990]
- [Dowell 1964][research_dowell_1964]
- [Dowell 1964][research_dowell_1964_b]
- [Dowell 1970][research_dowell_1970]
- [Dowell 1970][research_dowell_1970_b]
- [Dowell 1972][research_dowell_1972]
- [Dowell 1983][research_dowell_1983]
- [Dowell 1996][research_dowell_1996]
- [Dowell 1999][research_dowell_1999]
- [Dowell and Bendiksen 2010][research_dowell_bendiksen_2010]
- [Dowell and Voss 1964][research_dowell_voss_1964]
- [Dowell et al 1990][research_dowell_katz_1990]
- [Drake 1957][research_high_altitude_1957]
- [Drake and Williams 1958][research_williams_drake_1948]
- [Dreshfield 1996][research_dreshfield_1996]
- [Dresia et al 2023][research_dresia_adler_2023]
- [Dress et al 1992][research_dress_boyden_1992]
- [Dress et al 1994][research_dress_boyden_1994]
- [Dressler 2006][research_dressler_2006]
- [Driftmyer 1988][research_driftmyer_1988]
- [Dris and Jamal 2019][research_dris_jamal_2019]
- [Driscoll 1966][research_driscoll_1966]
- [Driver 1958][research_driver_1958]
- [Driver 1974][research_driver_1974]
- [Du 2013][research_du_2013]
- [Du 2017][research_du_2017]
- [Du et al 2025][research_du_liu_2025]
- [Du et al 2026][research_du_he_2026]
- [Duan and He 2014][research_duan_he_2014]
- [Duan et al 2001][research_duan_mei_2001]
- [Duan et al 2026][research_duan_wan_2026]
- [Dubois and Habiballah 1991][research_dubois_habiballah_1991]
- [Dubois et al 1995][research_dubois_habiballah_1995]
- [Ducros et al 1995][research_ducros_comte_1995]
- [Dugundji 1965][research_dugundji_1965]
- [Dugundji 1966][research_dugundji_1966]
- [Dukeman 2002][research_dukeman_2002]
- [Dukhnovskiy et al 2023][research_dukhnovskiy_lobkovskiy_2023]
- [Dunning 1957][research_dunning_1957]
- [Dupuis 1988][research_dupuis_1988]
- [Dutoi et al 2008][research_dutoi_richards_2008]
- [Dwivedi 1983][research_dwivedi_1983]
- [Dynamic Lateral-Directional Stability Theory 2003][research_dynamic_lateral_directional_2003]
- [Dynamic Stability and Control][research_dynamic_stability]
- [E et al 2026][research_e_fan_2026]
- [Eaton and Graefe 1952][research_eaton_graefe_1952]
- [Ebenezer et al 2022][research_ebenezer_koteswararao_2022]
- [Eberhart et al 2012][research_eberhart_lineberry_2012]
- [Eckert 1956][research_eckert_1956]
- [Eckles and Slater 1975][research_eckles_slater_1975]
- [Edquist et al][research_edquist_mahzari]
- [Edwards 1956][research_vtail_interference_1956]
- [Edwards 1992][research_edwards_1992]
- [Edwards 2014][research_edwards_2014]
- [Edwards et al 2024][research_edwards_constantin_2024]
- [Edwards et al 2025][research_edwards_constantin_2025]
- [Effect of uniformly distributed 1959][research_effect_of_1959]
- [Effects of Aerodynamic Heating 1980][research_effects_of_1980]
- [Effects of Atmospheric Structure 1979][research_effects_of_1979]
- [Effects of Elevated Temperature 1968][research_effects_of_1968]
- [Eftekhari et al 2025][research_eftekhari_siroueinejad_2025]
- [Egorov 2025][research_egorov_2025]
- [Egorov et al 2018][research_egorov_fedorov_2018]
- [Ehlers and Weisshaar 1993][research_ehlers_weisshaar_1993]
- [Ehlers et al 1976][research_ehlers_johnson_1976]
- [Ehlers et al 1978][research_ehlers_epton_1978]
- [EI-Sawy and Shatynski 1982][research_eisawy_shatynski_1982]
- [Ejection Seat 2003][research_ejection_seat_2003]
- [Ejection Seat 2015][research_ejection_seat_2015]
- [Ejection Seat Testing 2021][research_ejection_seat_2021]
- [Ekimogloy et al 2026][research_ekimogloy_stelk_2026]
- [Ekoto et al 2007][research_ekoto_bowersox_2007]
- [Ekvall et al 1989][research_ekvall_rainen_1989]
- [Ekvall et al 1990][research_ekvall_rainen_1990]
- [Elevated-Temperature Properties of Ferritic 1990][research_elevated_temperature_properties_1990]
- [Elevated-Temperature Properties of Stainless 1990][research_elevated_temperature_properties_1990_b]
- [Elgallad et al 2023][research_elgallad_chen_2023]
- [Elghobashi and Wassel 1980][research_elghobashi_wassel_1980]
- [Ellen 1968][research_ellen_1968]
- [Ellen 1969][research_ellen_1969]
- [Ellerbrock and Ziegenhagen 2006][research_ellerbrock_ziegenhagen_2006]
- [Ellis et al 1978][research_cooled_honeycomb_1978]
- [Ellison 1969][research_ellison_1969]
- [ElRamly][research_elramly]
- [Elshazly et al 2025][research_elshazly_kassem_2025]
- [Elson et al 1997][research_elson_lingard_1997]
- [Energy Analysis of High-Speed 1991][research_energy_analysis_1991]
- [Engelbrecht][research_engelbrecht]
- [Engelbrecht et al 2013][research_engelbrecht_pauck_2013]
- [England][research_england]
- [Engstrom and Lang 1961][research_engstrom_lang_1961]
- [Ennis et al 1995][research_ennis_schuster_1995]
- [Eppink 2023][research_eppink_2023]
- [Epstein 1954][research_epstein_1954]
- [Epstein et al 1994][research_epstein_srinivasan_1994]
- [Equations, tables, and charts 1953][research_naca_1135]
- [Ericksen et al 1984][research_ericksen_pepper_1984]
- [Erickson et al 1990][research_erickson_schreiner_1990]
- [Erickson et al 1990][research_erickson_schreiner_1990_b]
- [Ericsson 1986][research_ericsson_1986]
- [Ericsson 2001][research_ericsson_2001]
- [Erlebacher and Hussaini 1990][research_erlebacher_hussaini_1990]
- [Es-Souni 2000][research_essouni_2000]
- [Es-Souni 2001][research_essouni_2001]
- [ESDU Data Item estimates 1998][research_esdu_data_1998]
- [Etherington et al 2020][research_etherington_kramer_2020]
- [Evensen 1976][research_evensen_1976]
- [Experience Gained During Development 2010][research_experience_gained_2010]
- [Experimental Dynamic Stability Investigation 2025][research_experimental_dynamic_2025]
- [Failure by Stress-Corrosion Cracking 2019][research_failure_by_2019]
- [Fallis 1953][research_fallis_1953]
- [Fan 2015][research_fan_2015]
- [Fan et al 2017][research_fan_liu_2017]
- [Farhat 2001][research_farhat_2001]
- [Faroughi et al 2012][research_faroughi_malekzadeh_2012]
- [Farvin and Peddieson 1988][research_farvin_peddieson_1988]
- [Fasel and Sandberg 2006][research_fasel_sandberg_2006]
- [Fasel et al 2008][research_fasel_husmeier_2008]
- [Fatuev 2006][research_fatuev_2006]
- [Favor et al 1957][research_favor_achbach_1957]
- [Fay and Kemp 1963][research_fay_kemp_1963]
- [Fay and Riddell 1958][research_fay_riddell_1958]
- [Fejer et al 1964][research_fejer_heath_1964]
- [Feldman 1987][research_feldman_1987]
- [Feldman and Bahder 1989][research_feldman_bahder_1989]
- [Feldwisch and Schulze 2021][research_feldwisch_schulze_2021]
- [Feng and Wang 2008][research_feng_wang_2008]
- [Feng et al 2009][research_feng_cheng_2009]
- [Fenn 1962][research_fenn_1962]
- [Ferraiuolo and Manca 2012][research_ferraiuolo_manca_2012]
- [Ferraiuolo et al 2009][research_ferraiuolo_manca_2009]
- [Ferranti et al 2015][research_ferranti_wan_2015]
- [Ferrari 1948][research_ferrari_1948]
- [Ferrari 1955][research_ferrari_1955]
- [Ferrari 1958][research_ferrari_1958]
- [Ferris 1973][research_ferris_1973]
- [Fey et al 1993][research_fey_jeltsch_1993]
- [Fezer and Kloker 2000][research_fezer_kloker_2000]
- [Fick et al 1996][research_fick_gaitonde_1996]
- [Fidler and Hays 2026][research_fidler_hays_2026]
- [Fidler et al 2025][research_fidler_jenkins_2025]
- [Fields 1978][research_fields_1978]
- [Filimonov 1968][research_filimonov_1968]
- [Filin and Mkrtchyan 2021][research_filin_mkrtchyan_2021]
- [Filippou et al 2024][research_filippou_kilimtzidis_2024]
- [Finch and Matranga 1959][research_x15_first_flight_1959]
- [Finch and Walker 1953][research_x5_stability_1953]
- [Finseth 1991][research_finseth_1991]
- [Finson et al 1980][research_finson_clarke_1980]
- [Finson et al 1981][research_finson_clarke_1981]
- [Fiore et al 2026][research_fiore_fabiani_2026]
- [Firouz-Abadi et al 2013][research_firouzabadi_askarian_2013]
- [Fischer and Norris 1949][research_fischer_norris_1949]
- [Fisher 1969][research_fisher_1969]
- [Fisher and Dougherty 1982][research_fisher_dougherty_1982]
- [Fisher and Williams 1958][research_sweep_tail_height_1958]
- [Flagella 1967][research_flagella_1967]
- [Flagella and Tarr 1967][research_flagella_tarr_1967]
- [Flandro et al 2004][research_flandro_sims_2004]
- [Flandro et al 2004][research_flandro_sims_2004_b]
- [Flat Wings in Inviscid 2020][research_flat_wings_2020]
- [Flax 1953][research_flax_1953]
- [Flax 1977][research_flax_1977]
- [Flax 1986][research_flax_1986]
- [Fleeter et al 1974][research_fleeter_mcclure_1974]
- [Flight Measurements of Tile 1983][research_flight_measurements_1983]
- [Florence and Hiltz 1968][research_florence_hiltz_1968]
- [Fofonov 2021][research_fofonov_2021]
- [Ford 1979][research_ford_1979]
- [Ford 1985][research_ford_1985]
- [Formalev et al 2023][research_formalev_garibyan_2023]
- [Formation and Evaluation of 2020][research_formation_and_2020]
- [Fornasier 1984][research_fornasier_1984]
- [Forooghi et al 2018][research_forooghi_magagnato_2018]
- [Foroozan et al 2025][research_foroozan_ianiro_2025]
- [Forster et al 1996][research_forster_kolonay_1996]
- [Fortney and Avery 1957][research_fortney_avery_1957]
- [Fosdick 1970][research_fosdick_1970]
- [Foster and Shah][research_foster_shah]
- [Foster et al 1993][research_foster_ross_1993]
- [Fournier and Silvers 1958][research_x2_lateral_model_1958]
- [Fournier and Sleeman 1960][research_fournier_sleeman_1960]
- [Fox and Breedlove 1974][research_foxjr_breedlovejr_1974]
- [Fox-Rabinovich et al 2006][research_foxrabinovich_wilkinson_2006]
- [Frampton et al 1995][research_frampton_clark_1995]
- [France's Liquid Propellant Rocket-Engine 2006][research_france_s_liquid_2006]
- [Franklin 1971][research_franklin_1971]
- [Frazier 1991][research_frazier_1991]
- [Freeman et al 1969][research_freeman_goodell_1969]
- [French 1964][research_french_1964]
- [French 1967][research_french_1967]
- [French 1971][research_french_1971]
- [French 1979][research_french_1979]
- [French 1980][research_french_1980]
- [French 1988][research_french_1988]
- [French et al 1988][research_french_noll_1988]
- [Frendi 1996][research_frendi_1996]
- [Frendi 1997][research_frendi_1997]
- [Freudenthal 1963][research_freudenthal_1963]
- [Friedland 1965][research_friedland_1965]
- [Friedman and Bhat 1986][research_friedman_bhat_1986]
- [Frink et al 2016][research_frink_murphy_2016]
- [Fromont 1992][research_fromont_1992]
- [Frostig and Thomsen 2008][research_frostig_thomsen_2008]
- [Fu et al 2024][research_fu_shi_2024]
- [Fujita et al 2004][research_fujita_matsushima_2004]
- [Fuller 1952][research_fuller_1952]
- [Fuller 2012][research_fuller_2012]
- [Fulmer and Wirtz 1964][research_fulmer_wirtz_1964]
- [Funazaki 1994][research_funazaki_1994]
- [Fundamental Mechanisms of Combustion 1995][research_fundamental_mechanisms_1995]
- [Fung 1954][research_fung_1954]
- [Fung 1958][research_fung_1958]
- [Fung 1963][research_fung_1963]
- [Furst 1973][research_furst_1973]
- [Furst 1975][research_furst_1975]
- [Furukawa and Makino 2007][research_furukawa_makino_2007]
- [Furuya and Fukuchi 2001][research_furuya_fukuchi_2001]
- [Försching 2004][research_forsching_2004]
- [Försching and Senft 1991][research_forsching_senft_1991]
- [G. The Experimental Aerodynamics 1957][research_g_the_1957]
- [Galli][research_galli]
- [Gallon and Witkowski 2015][research_gallon_witkowski_2015]
- [Gallon et al 2013][research_gallon_witkowski_2013]
- [Galsworthy and Heawood 1982][research_galsworthy_heawood_1982]
- [Ganapathisubramani 2007][research_ganapathisubramani_2007]
- [Gandhi et al 2012][research_gandhi_richards_2012]
- [Gandhi et al 2014][research_gandhi_richards_2014]
- [Ganesan et al 2025][research_ganesan_subburayan_2025]
- [Ganesh Kumar et al 2018][research_ganeshkumar_ganesan_2018]
- [Gao et al 2011][research_gao_yang_2011]
- [Gao et al 2016][research_gao_zhang_2016]
- [Gao et al 2026][research_gao_jiang_2026]
- [Gaponov 2000][research_gaponov_2000]
- [Gaponov et al 1995][research_gaponov_kosinov_1995]
- [Garcia and Guruswamy 1999][research_garcia_guruswamy_1999]
- [Garcia et al 2015][research_garcia_keshmiri_2015]
- [Gardner 1951][research_gardner_1951]
- [Garfinkle 1974][research_garfinkle_1974]
- [Garrard 1998][research_garrard_1998]
- [Garren 1962][research_garren_1962]
- [Garrick and Reed 1981][research_garrick_reed_1981]
- [Gartling 1970][research_gartling_1970]
- [Gaspers 1972][research_gaspersjr_1972]
- [Gaviglio 1987][research_gaviglio_1987]
- [Gee 2000][research_gee_2000]
- [Gee and Sipcic 1999][research_gee_sipcic_1999]
- [Gellatly and Gallagher 1964][research_gellatly_gallagher_1964]
- [Gelzer and Peebles 2015][research_hsfrs_rcs_2015]
- [Gemranova 2021][research_gemranova_2021]
- [Genot 2021][research_genot_2021]
- [Gera et al 1981][research_gera_wilson_1981]
- [Gerhart 1973][research_gerhart_1973]
- [Gerhart 1975][research_gerhart_1975]
- [Gerlach 1965][research_gerlach_1965]
- [Gerlach 1967][research_gerlach_1967]
- [German 2011][research_german_2011]
- [German Development of the 2010 German Development of the Swept Wing 1935-1945][research_german_development_2010]
- [Germerdonk et al 1990][research_germerdonk_biegel_1990]
- [Ghalandari et al 2022][research_ghalandari_mahariq_2022]
- [Ghasimi and Rabinovitch 2023][research_ghasimi_rabinovitch_2023]
- [Ghatak and Robi 2015][research_ghatak_robi_2015]
- [Ghoreyshi et al 2026][research_ghoreyshi_aref_2026]
- [Ghosh and Modi 2021][research_ghosh_modi_2021]
- [Ghosh and Modi 2021][research_ghosh_modi_2021_b]
- [Ghosh et al 1998][research_ghosh_raisinghani_1998]
- [Giedt et al 1952][research_giedt_sherby_1952]
- [Giersch et al 2015][research_giersch_clark_2015]
- [Gilbert et al 1984][research_gilbert_schmidt_1984]
- [Gill et al 2012][research_gill_lowenberg_2012]
- [Gillette and Vaughn 1968][research_gillette_vaughn_1968]
- [Gillig and Guarnieri 1956][research_gillig_guarnieri_1956]
- [Gillis 1957][research_gillis_1957]
- [Gillis and Toll 1962][research_gillis_toll_1962]
- [Gilruth 1962][research_gilruth_1962]
- [Gilyard et al 1972][research_gilyard_berry_1972]
- [Girgis and Liu 2000][research_girgis_liu_2000]
- [Giuliano et al 2007][research_cece_throttling_2007]
- [Giuliano et al 2010][research_giuliano_leonard_2010]
- [Gladh et al 2013][research_gladh_ang_2013]
- [Glaser and McCarthy 2012][research_glaser_mccarthy_2012]
- [Glauert 1928][research_glauert_1928]
- [GNair et al 2012][research_gnair_mv_2012]
- [Go 2009][research_go_2009]
- [Goddwin 1949][research_nose_capsule_1949]
- [Goertz 1995][research_goertz_1995]
- [Goett and Bicknell 1939][research_goett_bicknell_1939]
- [Gokcen 1995][research_gokcen_1995]
- [Gokcen 1996][research_gokcen_1996]
- [Gokcen 1996][research_gokcen_1996_b]
- [Gokcen 1997][research_gokcen_1997]
- [Goland 1952][research_goland_1952]
- [Goldbaum 1956][research_goldbaum_1956]
- [Goldfeld and Zatoloka 1985][research_goldfeld_zatoloka_1985]
- [Goldsmith 1964][research_goldsmith_1964]
- [Goldstein 1975][research_goldstein_1975]
- [Goman et al 1997][research_goman_khramtsovsky_1997]
- [Gomes and Suleman 2004][research_gomes_suleman_2004]
- [Gomet et al 2014][research_gomet_robin_2014]
- [Gomez et al 2009][research_gomez_flutet_2009]
- [Gomillion 1976][research_gomillion_1976]
- [Gonzalez 1977][research_gonzalez_1977]
- [Goodell and Freeman 1973][research_goodell_freeman_1973]
- [Goodman 1956][research_goodman_1956]
- [Goodrich et al 1979][research_goodrich_derry_1979]
- [Goodyer 1990][research_goodyer_1990]
- [Gopal and Maddalena 2018][research_gopal_maddalena_2018]
- [Gopalarathnam et al 1997][research_gopalarathnam_selig_1997]
- [Gordnier 1993][research_gordnier_1993]
- [Gordnier 1995][research_gordnier_1995]
- [Gordnier and Visbal 2000][research_gordnier_visbal_2000]
- [Gordnier and Visbal 2001][research_gordnier_visbal_2001]
- [Gordnier and Visbal 2003][research_gordnier_visbal_2003]
- [Gordon and Speiser 1960][research_gordon_speiser_1960]
- [Gorla 1984][research_gorla_1984]
- [Gorla 1984][research_gorla_1984_b]
- [Goswami 1995][research_goswami_1995]
- [Gotsulenko and Gotsulenko 2013][research_gotsulenko_gotsulenko_2013]
- [Goud and Dwivedi 2022][research_goud_dwivedi_2022]
- [Gould 2001][research_gould_2001]
- [Gourgues and Andrieu 2003][research_gourgues_andrieu_2003]
- [Graefe and Gordon 1957][research_graefe_gordon_1957]
- [Gragg and Haars 1975][research_gragg_haars_1975]
- [Gragg et al 1982][research_gragg_evans_1982]
- [Graham 1958][research_graham_1958]
- [Graham et al 1954][research_graham_lagerstrom_1954]
- [Grana and Shanks 1952][research_free_flight_tunnel_1952]
- [Granata et al 2024][research_granata_savino_2024]
- [Granata et al 2024][research_granata_savino_2024_b]
- [Granville and Boxall 1960][research_granville_boxall_1960]
- [Gratton 2014][research_gratton_2014]
- [Gratton 2018][research_gratton_2018]
- [Gratzer and O'Donnell 1965][research_gratzer_odonnell_1965]
- [Gratzer and Odonnell 1964][research_gratzer_odonnell_1964]
- [Grauer and Morelli 2023][research_grauer_morelli_2023]
- [Greatrix 2018][research_greatrix_2018]
- [Greatrix 2021][research_greatrix_2021]
- [Green and Fernandez 1994][research_green_fernandez_1994]
- [Green and Spence 2004][research_green_spence_2004_b]
- [Green et al 2004][research_green_spence_2004]
- [Greene 1970][research_greene_1970]
- [Greene and Northrup 1975][research_rene41_panels_1975]
- [Greenwood et al 1970][research_greenwood_prozan_1970]
- [Gregorek et al 1977][research_gregorek_hoffmann_1977]
- [Gregory and You 2011][research_gregory_you_2011]
- [Gregory et al 1998][research_gregory_cooke_1998]
- [Grenda et al 1991][research_grenda_venkateswaran_1991]
- [Grenestedt 2008][research_grenestedt_2008]
- [Grenestedt et al 2006][research_grenestedt_ridder_2006]
- [Gresham et al 2009][research_gresham_wang_2009]
- [Grewal et al 1976][research_grewal_schneider_1976]
- [Grey 1953][research_grey_1953]
- [Grey 1954][research_grey_1954]
- [Gribben et al 1998][research_gribben_driscoll_1998]
- [Griffin and Eastep 1981][research_griffin_eastep_1981]
- [Griffin and Jonas 1983][research_griffin_jonas_1983]
- [Griffith and Crosby 1970][research_griffith_crosby_1970]
- [Grindrod and Noden 1968][research_grindrod_noden_1968]
- [Gringorten 1967][research_gringorten_1967]
- [Gringorten and Tattelman 1970][research_gringorten_tattelman_1970]
- [Grobstein and Doychak 1989][research_grobstein_doychak_1989]
- [Groen Eric and Fucke Lars 2012][research_groeneric_fuckelars_2012]
- [Grohmann et al 1999][research_grohmann_kroplin_1999]
- [Gromov and Larin 1982][research_gromov_larin_1982]
- [Gromski et al 2010][research_gromski_majamaki_2010]
- [Gros 1963][research_gros_1963]
- [Grosdemange and Schaeffer 1990][research_grosdemange_schaeffer_1990]
- [Gross and Mawhinney 1970][research_gross_mawhinney_1970]
- [Grosser 1965][research_grosser_1965]
- [Groth 1961][research_groth_1961]
- [Ground and flight testing 2000][research_ground_and_2000]
- [Gu et al 2024][research_gu_healy_2024]
- [Guan and Guo 2016][research_guan_guo_2016]
- [Guan et al 2013][research_guan_zhu_2013]
- [Guarnieri 1954][research_guarnieri_1954]
- [Guderley 1987][research_guderley_1987]
- [Guderley 1988][research_guderley_1988]
- [Guglieri and Quagliotti 1993][research_guglieri_quagliotti_1993]
- [Guide for High-Temperature Static][research_guide_for]
- [Guiler][research_guiler]
- [Guiler and Huebsch 2005][research_guiler_huebsch_2005]
- [Guimarães et al 2020][research_guimaraes_rade_2020]
- [Guimarães et al 2021][research_guimaraes_cesnik_2021]
- [Guinn 1961][research_guinn_1961]
- [Gulczyński et al 2024][research_gulczynski_hahn_2024]
- [Gully et al 1987][research_real_gas_facility_1987]
- [Gunn 1947][research_gunn_1947]
- [Gunn 1947][research_gunn_1947_b]
- [Guo and Mei][research_guo_mei]
- [Guo and Mei 2002][research_guo_mei_2002]
- [Guo and Mei 2003][research_guo_mei_2003]
- [Guo and Ren 2015][research_guo_ren_2015]
- [Guo and Ren 2019][research_guo_ren_2019]
- [Guo et al 1988][research_guo_wang_1988]
- [Guo et al 1994][research_guo_adams_1994]
- [Guo et al 2004][research_guo_przekop_2004]
- [Guo et al 2022][research_guo_xu_2022]
- [Guo et al 2022][research_guo_zhang_2022]
- [Guo et al 2025][research_guo_zhang_2025]
- [Gupta and Ramkumar 2015][research_gupta_ramkumar_2015]
- [Gupta et al 1992][research_gupta_jones_1992]
- [Gurentsov et al 2002][research_gurentsov_shikov_2002]
- [Gurov 2001][research_gurov_2001]
- [Gut et al 2025][research_gut_parzybut_2025]
- [Guttman and Crutcher 1968][research_guttman_crutcher_1968]
- [Gwin 1974][research_gwin_1974]
- [Gözükara and Ceylan 2024][research_gozukara_ceylan_2024]
- [Haas and Chopra 1987][research_haas_chopra_1987]
- [Habchi and Hufford 1995][research_habchi_hufford_1995]
- [Habchi et al 1992][research_habchi_przekwas_1992]
- [Habchi et al 1995][research_habchi_hufford_1995_b]
- [Hacker and Oprişiu 1974][research_hacker_oprisiu_1974]
- [Hader and Fasel 2023][research_hader_fasel_2023]
- [Haga 2024][research_haga_2024]
- [Hagerman and Hofstetter 1969][research_hagerman_hofstetter_1969]
- [Haglaga 1970][research_haglaga_1970]
- [Hahn and Frendi 2012][research_hahn_frendi_2012]
- [Hahn and Frendi 2013][research_hahn_frendi_2013]
- [Hajela and Glowasky 1991][research_hajela_glowasky_1991]
- [Hakim et al 2020][research_hakim_tahdi_2020]
- [Hale et al 2015][research_hale_patil_2015]
- [Halford 1972][research_halford_1972]
- [Hall and Boothe 1972][research_hall_boothe_1972]
- [Hallberg et al 2008][research_hallberg_cenko_2008]
- [Hallstaff 1961][research_hallstaff_1961]
- [Ham-Battista et al 1993][research_hambattista_helmick_1993]
- [Hamed 1993][research_hamed_1993]
- [Hamed and Li 2008][research_hamed_li_2008]
- [Hammer et al 2021][research_hammer_garmann_2021]
- [Hammer et al 2023][research_hammer_garmann_2023]
- [Hampson 1984][research_hampson_1984]
- [Han and Yang 1983][research_han_yang_1983]
- [Han et al 2020][research_han_su_2020]
- [Han et al 2022][research_han_he_2022]
- [Hancock 1959][research_hancock_1959]
- [Hanford and Wilson 1992][research_hanford_wilson_1992]
- [Hanford and Wilson 1992][research_hanford_wilson_1992_b]
- [Hanine et al 1992][research_hanine_kourta_1992]
- [Hanna and Stephens 1991][research_hanna_stephens_1991]
- [Hanson et al 2011][research_hanson_schaefer_2011]
- [Hao et al 2024][research_hao_liu_2024]
- [Hao et al 2026][research_hao_kong_2026]
- [Harbec and Todkill 1965][research_harbec_todkill_1965]
- [Hardgrove and Krieg 1984][research_hardgrove_kriegjr_1984]
- [Hardy et al 2005][research_hardy_bronowski_2005]
- [Hargrave et al 1985][research_hargrave_fairweather_1985]
- [Harmathy and Stanzak 1970][research_harmathy_stanzak_1970]
- [Harper 1969][research_harper_1969]
- [Harri 1964][research_harri_1964]
- [Harris 1972][research_harris_1972]
- [Harris and Bartlett 1972][research_harris_bartlett_1972]
- [Harris and Fasel 1996][research_harris_fasel_1996]
- [Harris and Robinson 1960][research_harris_robinson_1960]
- [Harris and Robinson 1960][research_harris_robinson_1960_b]
- [Harrje 1959][research_harrje_1959]
- [Hart 1956][research_hart_1956]
- [Hartley et al 1965][research_hartley_furey_1965]
- [Harvazinski et al 2014][research_harvazinski_sankaran_2014]
- [Harvazinski et al 2024][research_harvazinski_mehta_2024]
- [Harvey 1970][research_harvey_1970]
- [Hasehemian 1986][research_hasehemian_1986]
- [Hasel and Coletti 1948][research_pitot_supersonic_1948]
- [Hashimoto et al 2003][research_hashimoto_menshov_2003]
- [Hashimoto et al 2009][research_hashimoto_aoyama_2009]
- [Hashin and Humphreys 1980][research_hashin_humphreys_1980]
- [Hassan 1994][research_hassan_1994]
- [Hassan et al 2010][research_hassan_abbass_2010]
- [Hassan et al 2021][research_hassan_kunz_2021]
- [Hata 2001][research_hata_2001]
- [Hatton 1964][research_hatton_1964]
- [Hatton 1965][research_hatton_1965]
- [Hatton and Eustace 2019][research_hatton_eustace_2019]
- [Havener 1985][research_havener_1985]
- [Hayashi and Aso 1988][research_hayashi_aso_1988]
- [Hayes 1946][research_hayes_1946]
- [Hayhurst 1974][research_hayhurst_1974]
- [Hayhurst 2001][research_hayhurst_2001]
- [Hayostek and Amitay 2018][research_hayostek_amitay_2018]
- [He et al 2020][research_he_song_2020]
- [He et al 2021][research_he_wang_2021]
- [Heald and Brassell 1976][research_heald_brassell_1976]
- [Heard 1965][research_heardjr_1965]
- [Heat Transfer in Incompressible 2013][research_heat_transfer_2013]
- [Hebsur and Stephens 1991][research_hebsur_stephens_1991]
- [Hebsur et al 1988][research_hebsur_stephens_1988]
- [Hebsur et al 1989][research_hebsur_stephens_1989]
- [Hegenwald 1958][research_x15_escape_1958]
- [Heinrich 1966][research_heinrich_1966]
- [Heinrich 1972][research_heinrich_1972]
- [Heinrich and Hektner 1970][research_heinrich_hektner_1970]
- [Heinrich and Noreen 1968][research_heinrich_noreen_1968]
- [Heinrich and Saari 1975][research_heinrich_saari_1975]
- [Heinrich and Saari 1978][research_heinrich_saari_1978]
- [Heinrich et al 1974][research_heinrich_noreen_1974]
- [Heister 2008][research_heister_2008]
- [Hellyer and Sherhod][research_hellyer_sherhod]
- [Hemmig et al 1980][research_hemmig_venkayya_1980]
- [Hender 1982][research_hender_1982]
- [Hendershot 1969][research_hendershot_1969]
- [Henderson and Komenda 1998][research_henderson_komenda_1998]
- [Heng and Sherman 1996][research_heng_sherman_1996]
- [Henke and Nerem 1968][research_henke_nerem_1968]
- [Henry et al 2017][research_henry_patel_2017]
- [Hensel 1964][research_hensel_1964]
- [Henson and Robertson 1962][research_henson_robertson_1962]
- [Hermann 1950][research_hermann_1950]
- [Hermann 2025][research_hermann_2025]
- [Hermes crew escape system 1990][research_hermes_crew_1990]
- [Herring 2009][research_herring_2009]
- [Herrmann 2008][research_herrmann_2008]
- [Herrmann and Orlowski 1997][research_herrmann_orlowski_1997]
- [Hess 1997][research_hess_1997]
- [Hess 2013][research_hess_2013]
- [Hess and Hess 1997][research_hess_hess_1997]
- [Hewes and Hassell 1960][research_hewes_hassell_1960]
- [Hibner et al 1997][research_hibner_sizek_1997]
- [Hicks and Moulton 1988][research_hicks_moulton_1988]
- [High and Bowman 1995][research_high_bowman_1995]
- [High Speed Problems of 1962][research_high_speed_1962]
- [High temperature resistance strain 1975][research_high_temperature_1975]
- [High Temperature Tensile and 1962][research_high_temperature_1962]
- [High-speed flight 1986][research_high_speed_flight_1986]
- [High-Speed Flight 1996][research_high_speed_flight_1996]
- [High-Speed Flight 2009][research_high_speed_flight_2009]
- [High-Speed Flight 2010][research_high_speed_flight_2010]
- [High-Speed Flight Thermal Management 1996][research_high_speed_flight_1996_b]
- [High-Temperature, Thin-Film Strain Gages 2005][research_high_temperature_thin_film_2005]
- [Hilger and Ritter 2021][research_hilger_ritter_2021]
- [Hill et al 1956][research_oxidation_ignition_1956]
- [Hill et al 1970][research_hill_misra_1970]
- [Hillier 1970][research_hillier_1970]
- [Hinada et al 1991][research_hinada_inatani_1991]
- [Hiraki et al 1997][research_hiraki_hinada_1997]
- [Hiraki et al 2019][research_hiraki_inoue_2019]
- [Hirschberg and Van Muiswinkel 1977][research_hirschberg_vanmuiswinkel_1977]
- [Hirschberg et al 1972][research_hirschberg_spera_1972]
- [History of Supersonic Transport 2020][research_history_of_2020]
- [Hitch 1978][research_hitch_1978]
- [Hodell and Rosner 1957][research_hodell_rosner_1957]
- [Hodgkinson et al 1990][research_hodgkinson_potsdam_1990]
- [Hoff 1956][research_hoff_1956]
- [Hoffman et al 1970][research_hoffman_zvara_1970]
- [Hoh et al 1981][research_hoh_myers_1981]
- [Hollinger 1965][research_hollinger_1965]
- [Holloway and Johnson 2008][research_holloway_johnson_2008]
- [Holmes and Moore 1992][research_holmes_moore_1992]
- [Holt 1977][research_holt_1977]
- [Holtz 1964][research_holtz_1964]
- [Holzapfel et al 2006][research_holzapfel_dacosta_2006]
- [Holzinger and Cunis 2024][research_holzinger_cunis_2024]
- [Homan 1970][research_homan_1970]
- [Hong 1965][research_hong_1965]
- [Hong 1993][research_wing_rock_delta_1993]
- [Hong et al 2009][research_hong_kim_2009]
- [Hoover 1947][research_hoover_1947]
- [Hopkins and Dowell 1994][research_hopkins_dowell_1994]
- [Horagiri and Nagai 2014][research_horagiri_nagai_2014]
- [Horenstein and Roberts 1993][research_horenstein_roberts_1993]
- [Horsnell 1967][research_horsnell_1967]
- [Horstman and Hung 1979][research_horstman_hung_1979]
- [Horstman and Kussoy 1967][research_horstman_kussoy_1967]
- [Horstman et al 1978][research_horstman_kussoy_1978]
- [Horton and Zeh 1966][research_horton_zeh_1966]
- [Horton and Zeh 1967][research_horton_zeh_1967]
- [Hosangadi et al 2015][research_hosangadi_paul_2015]
- [Hoschke et al 2013][research_hoschke_price_2013]
- [Hosni et al 1991][research_hosni_coleman_1991]
- [Hou 2008][research_hou_2008]
- [Hou and Satyanarayana 2000][research_hou_satyanarayana_2000]
- [Hou et al 2018][research_hou_fu_2018]
- [Hou et al 2023][research_hou_liu_2023]
- [Houbolt and Menkes 1968][research_houbolt_menkes_1968]
- [Houra et al 2014][research_houra_nagano_2014]
- [House et al 2021][research_house_ayoola_2021]
- [Howland 1979][research_howland_1979]
- [Hreha and Lutze 1983][research_hreha_lutze_1983]
- [Hreha and Lutze 1984][research_hreha_lutze_1984]
- [Hrubecky 1995][research_hrubecky_1995]
- [Hsu 2026][research_hsu_2026]
- [Hu and Mahadevan 2019][research_hu_mahadevan_2019]
- [Hu et al 2012][research_hu_jameson_2012]
- [Hu et al 2021][research_hu_ferrari_2021]
- [Hu et al 2023][research_hu_tan_2023]
- [Hu et al 2026][research_hu_he_2026]
- [Hua et al 2025][research_hua_wang_2025]
- [Huang 2000][research_huang_2000]
- [Huang 2002][research_huang_2002]
- [Huang 2002][research_huang_2002_b]
- [Huang 2005][research_huang_2005]
- [Huang 2016][research_huang_2016]
- [Huang and Friedmann 2016][research_huang_friedmann_2016]
- [Huang and Liou 1994][research_huang_liou_1994]
- [Huang and Valentin 1974][research_huang_valentin_1974]
- [Huang et al 2000][research_huang_zhou_2000]
- [Huang et al 2000][research_huang_zhou_2000_b]
- [Huang et al 2014][research_huang_zhang_2014]
- [Huang et al 2019][research_huang_friedmann_2019]
- [Huang et al 2020][research_huang_avery_2020]
- [Huang et al 2021][research_huang_fu_2021]
- [Huang et al 2021][research_huang_hu_2021]
- [Huang et al 2023][research_huang_lu_2023]
- [Huang et al 2024][research_huang_cheng_2024]
- [Huang et al 2024][research_huang_cheng_2024_b]
- [Hubbard et al 2014][research_hubbard_fontenot_2014]
- [Hubble et al 2008][research_hubble_fu_2008]
- [Hube 1978][research_hube_1978]
- [Hudson 1989][research_hudson_1989]
- [Hudson and Stephens 2006][research_hudson_stephens_2006]
- [Huffman and Fox 1985][research_huffman_foxjr_1985]
- [Hufford and Habchi 1994][research_hufford_habchi_1994]
- [Hughes 1964][research_hughes_1964]
- [Hui and Tobak 1982][research_hui_tobak_1982]
- [Hulka 2008][research_hulka_2008]
- [Hulse et al 1984][research_hulse_bailey_1984]
- [Hulse et al 1985][research_hulse_bailey_1985]
- [Hulse et al 1987][research_hulse_bailey_1987]
- [Hulse et al 1991][research_hulse_bailey_1991]
- [Hung and Buning 1985][research_hung_buning_1985]
- [Hung and Chaussee 1981][research_hung_chaussee_1981]
- [Hung and Maccormack 1978][research_hung_maccormack_1978]
- [Hurt and Whitten 1960][research_pitchup_control_1960]
- [Hussein et al 2026][research_hussein_etzenbach_2026]
- [Huston et al 1948][research_huston_warfield_1948]
- [Huysmans et al 2017][research_huysmans_vekeman_2017]
- [Hwu and Tsai 2002][research_hwu_tsai_2002]
- [Hyde 1986][research_hyde_1986]
- [Hyde and Argueta 2025][research_hyde_argueta_2025]
- [Hyde et al 2018][research_hyde_brown_2018]
- [Hyers 2009][research_hyers_2009]
- [Hürst et al 1994][research_hurst_schulz_1994]
- [Ibrahim 1965][research_ibrahim_1965]
- [Ibrahim 1989][research_ibrahim_1989]
- [Ibrahim 1990][research_ibrahim_1990]
- [Ibrahim et al 2004][research_ibrahim_beloiu_2004]
- [Ibrahim et al 2007][research_ibrahim_tawfik_2007]
- [Ide and Ominsky 1990][research_ide_ominsky_1990]
- [Ifju et al 2001][research_ifju_waszak_2001]
- [Il'Yashenko 1963][research_ilyashenko_1963]
- [Imai et al 1992][research_imai_hirata_1992]
- [Inertia Coupling and Spin 2004][research_inertia_coupling_2004]
- [Inertia Coupling and Spin 2015][research_inertia_coupling_2015]
- [Influence of Corrugation-Roughness Shape 1980][research_influence_of_1980]
- [Influence of wing geometry 1989][research_influence_of_1989]
- [Inger 1984][research_inger_1984]
- [Inger 1985][research_inger_1985]
- [Inger 1986][research_inger_1986]
- [Inger 1988][research_inger_1988]
- [Inger 1995][research_inger_1995]
- [Innocenzi et al 2023][research_innocenzi_bruce_2023]
- [Instability Phenomenology and Case 1995][research_instability_phenomenology_1995]
- [Instability Phenomenology and Case 1995][research_instability_phenomenology_1995_b]
- [Instability Phenomenology and Case 1995][research_instability_phenomenology_1995_c]
- [Instability Phenomenology and Case 1995][research_instability_phenomenology_1995_d]
- [Instrumentation For Research On 1960][research_instrumentation_for_1960]
- [Integrated Thermal Monitoring for 2025][research_integrated_thermal_2025]
- [Iosilevskii 2025][research_iosilevskii_2025]
- [Irving 1966][research_irving_1966]
- [Isakson 1957][research_isakson_1957]
- [Ishikawa et al 2007][research_ishikawa_kwak_2007]
- [Ishikawa et al 2008][research_ishikawa_kwak_2008]
- [Ishin 2022][research_ishin_2022]
- [Islam et al 2025][research_islam_ali_2025]
- [Isogai 2013][research_isogai_2013]
- [Ivanov 2008][research_ivanov_2008]
- [Ivanov 2021][research_ivanov_2021]
- [Ivanov and Borisov 2014][research_ivanov_borisov_2014]
- [Iyer et al 1992][research_iyer_spall_1992]
- [Izadpanahi][research_izadpanahi]
- [Izadpanahi and Mardanpour 2018][research_izadpanahi_mardanpour_2018]
- [Jablonowski et al 1957][research_jablonowski_shober_1957]
- [Jackson and Taylor 1976][research_hypersonic_research_structure_1976]
- [Jacob and George 2024][research_jacob_george_2024]
- [Jacob et al 2010][research_jacob_flandro_2010]
- [Jacobsen 1974][research_jacobsen_1974]
- [Jacobsen 1977][research_jacobsen_1977]
- [Jacobsen and Greif 1972][research_lift_roll_coupling_1972]
- [Jacobson 2010][research_jacobson_2010]
- [Jacobson 2010][research_jacobson_2010_b]
- [Jaffe and Dorn 1960][research_jaffe_dorn_1960]
- [Jain 1986][research_jain_1986]
- [James 1981][research_jamesjr_1981]
- [Jameson 1977][research_jameson_1977]
- [Jameson and Caughey 1977][research_jameson_caughey_1977]
- [Jameson et al 2005][research_jameson_shankaran_2005]
- [Jamison 1966][research_jamison_1966]
- [Jamison 1967][research_jamison_1967]
- [Jammalamadaka et al 2014][research_jammalamadaka_li_2014]
- [Jamwal et al 2018][research_jamwal_hosangadi_2018]
- [Jana et al 2021][research_jana_sreedhar_2021]
- [Japan's Liquid Propellant Rocket-Engine 2006][research_japan_s_liquid_2006]
- [Jayan and Raghunandan 2003][research_jayan_raghunandan_2003]
- [Jayanti][research_jayanti]
- [Jayaram et al 1987][research_jayaram_taylor_1987]
- [Jayaraman et al 2022][research_jayaraman_saini_2022]
- [Jeffrie and Rolston 1972][research_jeffrie_rolston_1972]
- [Jegarkandi Mohsen et al 2009][research_jegarkandimohsen_nobariali_2009]
- [Jeng and Litchford 1991][research_jeng_litchford_1991]
- [Jeng and Reddy Gorla 1973][research_jeng_reddygorla_1973]
- [Jeng-Shian and Wei-Chong 1991][research_jengshian_weichong_1991]
- [Jenke 1979][research_jenke_1979]
- [Jenkins 1979][research_thermal_stress_correlation_1979]
- [Jenkins 2018][research_jenkins_2018]
- [Jenkins and Kuhl 1977][research_loads_calibration_1977]
- [Jenkins and Quinn 1996][research_jenkins_quinn_1996]
- [Jenness 1958][research_jenness_1958]
- [Jensen 2005][research_jensen_2005]
- [Jeon and Park 2023][research_jeon_park_2023]
- [Jeon and Park 2026][research_jeon_park_2026]
- [Jeon et al 2004][research_jeon_lee_2004]
- [Jeon et al 2013][research_jeon_kwak_2013]
- [Jha 2024][research_jha_2024]
- [Jhajj et al 2014][research_jhajj_caron_2014]
- [Ji and Xie 2022][research_ji_xie_2022]
- [Ji et al 2011][research_ji_wang_2011]
- [Ji et al 2021][research_ji_duan_2021]
- [Jia et al 2013][research_jia_han_2013]
- [Jia-Lin et al 2014][research_jialin_lei_2014]
- [Jiajan et al 2013][research_jiajan_chue_2013]
- [Jiang and Campbell 2008][research_jiang_campbell_2008]
- [Jiang et al 2000][research_jiang_an_2000]
- [Jiang et al 2006][research_jiang_choudhari_2006]
- [Jiang et al 2013][research_jiang_lin_2013]
- [Jiang et al 2026][research_jiang_liu_2026]
- [Jin et al 2019][research_jin_xu_2019]
- [Jines 1980][research_jines_1980]
- [Jines 1983][research_jines_1983]
- [Jing-Lei and Hui-Yang 2007][research_jinglei_huiyang_2007]
- [Jirásek et al 2018][research_jirasek_cummings_2018]
- [Jischke 1978][research_jischke_1978]
- [Johari and Desabrais 2002][research_johari_desabrais_2002]
- [Johns 1958][research_johns_1958]
- [Johns 1960][research_johns_1960]
- [Johnson 1985][research_johnson_1985]
- [Johnson 1986][research_johnson_1986]
- [Johnson 1988][research_johnson_1988]
- [Johnson 1989][research_johnson_1989]
- [Johnson and Faurote 1972][research_johnson_faurote_1972]
- [Johnson and Pilla 2012][research_johnsonms_pilla_2012]
- [Johnson and Rubesin 1949][research_johnson_rubesin_1949]
- [Johnson and Weir 1969][research_johnson_weir_1969]
- [Johnson and Yang 1985][research_johnson_yang_1985]
- [Johnson and Young 1972][research_johnson_young_1972]
- [Johnson et al 1970][research_johnson_josepha_1970]
- [Johnson III and Wu 1974][research_johnsoniii_wu_1974]
- [Johnston 1964][research_johnston_1964]
- [Johnston 1998][research_johnston_1998]
- [Johnston and Hogge 1974][research_johnston_hogge_1974]
- [Johnston and Hogge 1976][research_johnston_hogge_1976]
- [Johnston et al 1974][research_johnston_ashkenas_1974]
- [Jones 1947][research_jones_1947]
- [Jones 1950][research_jones_1950]
- [Jones 1952][research_jones_1952]
- [Jones 1959][research_jones_1959]
- [Jones 1962][research_jones_1962]
- [Jones 1966][research_jones_1966]
- [Jones 1967][research_jones_1967]
- [Jones 1976][research_jones_1976]
- [Jones 1980][research_jones_1980]
- [Jones and Nisbet 1976][research_jones_nisbet_1976]
- [Jones and Richie 1974][research_jones_richie_1974]
- [Jones et al 1984][research_jones_bylina_1984]
- [Jordan 1972][research_jordan_1972]
- [Jordan et al 2004][research_jordan_langford_2004]
- [Joshi and Rickard 1981][research_joshi_rickard_1981]
- [Joshi et al 2023][research_joshi_salahudden_2023]
- [Joy et al 2024][research_joy_talapatra_2024]
- [Juliawan et al 2024][research_juliawan_lee_2024]
- [Jun and Kochan 2014][research_jun_kochan_2014]
- [Jun et al 2017][research_jun_kochan_2017]
- [Jung and Reimerdes 2003][research_jung_reimerdes_2003]
- [Jung et al 2001][research_jung_wee_2001]
- [Junkhan 1978][research_junkhan_1978]
- [Jurado and McGehee 2019][research_jurado_mcgehee_2019]
- [Jurado et al 1990][research_jurado_shade_1990]
- [Kaattari 1959][research_kaattari_1959]
- [Kachler and Beaurain 2005][research_kachler_beaurain_2005]
- [Kakudo et al 2021][research_kakudo_yokoyama_2021]
- [Kalkhoran and Otugen 1994][research_kalkhoran_otugen_1994]
- [Kaloust 2002][research_kaloust_2002]
- [Kambiz Farahmand 2001][research_kambizfarahmandjonathanwkaufm_2001]
- [Kamijo 1983][research_kamijo_1983]
- [Kamijo et al 1981][research_kamijo_sogame_1981]
- [Kamijo et al 1982][research_kamijo_sogame_1982]
- [Kanda 2013][research_kanda_2013]
- [Kanda 2019][research_kanda_2019]
- [Kanda et al 2021][research_kanda_kikuchi_2021]
- [Kanda et al 2023][research_kanda_mishina_2023]
- [Kandil et al 1993][research_kandil_kandil_1993]
- [Kandil et al 1993][research_kandil_kandil_1993_b]
- [Kandis and Witkowski 2019][research_kandis_witkowski_2019]
- [Kandula and Haddad 2007][research_kandula_haddad_2007]
- [Kannan and Bhat 2005][research_kannan_bhat_2005]
- [Kanneganti et al 2022][research_kanneganti_charan_2022]
- [Karabis et al 2000][research_karabis_shaw_2000]
- [Kariappa and Smith 1972][research_kariappa_smith_1972]
- [Kariappa and Somashekar 1969][research_kariappa_somashekar_1969]
- [Karlgaard et al 2018][research_karlgaard_tynis_2018]
- [Karlgaard et al 2019][research_karlgaard_tynis_2019]
- [Karpel et al 2004][research_karpel_moulin_2004]
- [Karpouzian and Librescu 1992][research_karpouzian_librescu_1992]
- [Karunakaran 2018][research_karunakaran_2018]
- [Kasdaglis et al 2016][research_kasdaglis_bernard_2016]
- [Kase et al 2020][research_kase_mizoguchi_2020]
- [Kass 1970][research_kass_1970]
- [Katipelli and Dahotre 2001][research_katipelli_dahotre_2001]
- [Katz 1989][research_katz_1989]
- [Kaufman and Louis G. 1964][research_kaufman_louisg_1964]
- [Kaul et al 2002][research_kaul_stuckey_2002]
- [Kawakami et al 2007][research_kawakami_takatoya_2007]
- [Kawakami et al 2008][research_kawakami_takatoya_2008]
- [Kaye and Brown 1954][research_kaye_brown_1954]
- [Kaye and Yeh 1955][research_kaye_yeh_1955]
- [Kayran 2004][research_kayran_2004]
- [Kayser et al 1978][research_kayser_sturek_1978]
- [Kayser et al 1986][research_kayser_clay_1986]
- [Kazemba et al 2012][research_kazemba_braun_2012]
- [Kazemba et al 2017][research_kazemba_braun_2017]
- [Ke et al 2009][research_ke_wang_2009]
- [Keck 1975][research_keck_1975]
- [Keel 1977][research_keeljr_1977]
- [Keenan and Kuhlman 1991][research_keenan_kuhlman_1991]
- [Keener 1984][research_keener_1984]
- [Kegerise et al 2010][research_kegerise_owens_2010]
- [Kehoe and Deaton 1993][research_hot_structure_vibration_1993]
- [Kehrer 1964][research_kehrer_1964]
- [Kehrer 1971][research_kehrer_1971]
- [Keller and Plaga 2008][research_keller_plaga_2008]
- [Kempel et al 1988][research_kempel_mcneill_1988]
- [Kempel et al 1988][research_kempel_mcneill_1988_b]
- [Kenna et al 1964][research_mckenna_walker_1964]
- [Kenny et al 2006][research_injector_throttling_2006]
- [Kenyon and Shinde 2025][research_kenyon_shinde_2025]
- [Kenzakowski et al 1997][research_kenzakowski_york_1997]
- [Keçeci et al 2025][research_kececi_karakus_2025]
- [Khader and Huston 1987][research_khader_huston_1987]
- [Khakpour et al 2015][research_khakpour_soltani_2015]
- [Khan and Qamar 2020][research_khan_qamar_2020]
- [Khan and Qamar 2020][research_khan_qamar_2020_b]
- [Khan et al 2019][research_khan_masud_2019]
- [Khatri and Sinha 2011][research_khatri_sinha_2011]
- [Khatri and Subbarao 2024][research_khatri_subbarao_2024]
- [Kholodar 2023][research_kholodar_2023]
- [Khot et al 1997][research_khot_eastep_1997]
- [Khotyanovsky and Kudryavtsev 2016][research_khotyanovsky_kudryavtsev_2016]
- [Khrabrov et al 2013][research_khrabrov_sidoryuk_2013]
- [Kiber 1977][research_kiber_1977]
- [Kies and Schwartz 1974][research_kies_schwartz_1974]
- [Kilburg 1968][research_kilburg_1968]
- [Kim 2009][research_kim_2009]
- [Kim 2017][research_kim_2017]
- [Kim and Kim 2015][research_kim_kim_2015_b]
- [Kim and Lee 2000][research_kim_lee_2000]
- [Kim and Park 1999][research_kim_park_1999]
- [Kim and Song 2013][research_kim_song_2013]
- [Kim et al 1992][research_kim_chen_1992]
- [Kim et al 2004][research_kim_chung_2004]
- [Kim et al 2024][research_kim_siddiqui_2024]
- [Kimata et al 2015][research_kimata_taguchi_2015]
- [Kimmel and Prabhu 2015][research_kimmel_prabhu_2015]
- [Kimmel et al 2015][research_kimmel_borg_2015]
- [Kimura and Sawada 2022][research_kimura_sawada_2022]
- [Kimura et al 2010][research_kimura_sato_2010]
- [King 1962][research_king_1962]
- [King and Ethridge 1985][research_king_ethridge_1985]
- [Kiris et al 2000][research_kiris_dochankwak_2000]
- [Kirk and Miller 1962][research_kirk_miller_1962]
- [Kirkham et al 1974][research_kirkham_jackson_1974]
- [Kishimoto et al 2022][research_kishimoto_morita_2022]
- [Kistler 1959][research_kistler_1959]
- [Kithcart and Klett 1995][research_kithcart_klett_1995]
- [Klausmeyer 2026][research_klausmeyer_2026]
- [Klemm et al 1998][research_klemm_herrmann_1998]
- [Klimas 1973][research_klimas_1973]
- [Klimas and Rogers 1975][research_klimas_rogers_1975]
- [Klineberg et al 1970][research_klineberg_kubota_1970]
- [Klopfer and Nielsen 1979][research_klopfer_nielsen_1979]
- [Klopfer and Nielsen 1980][research_klopfer_nielsen_1980]
- [Klueh and King 1977][research_klueh_king_1977]
- [Klueh and King 1982][research_klueh_king_1982]
- [Kluever 2004][research_kluever_2004]
- [Kluever 2007][research_kluever_2007]
- [Kluever and Neal 2015][research_kluever_neal_2015]
- [Klyde and McRuer 2008][research_klyde_mcruer_2008]
- [Klyde et al 2004][research_klyde_thompson_2004]
- [Klyde et al 2011][research_klyde_liang_2011]
- [Klyde et al 2014][research_klyde_lampton_2014]
- [Klyde et al 2017][research_klyde_lampton_2017]
- [Knapp et al 1953][research_knapp_jordan_1953]
- [Knight 1982][research_knight_1982]
- [Knight and Zheltovodov 2011][research_knight_zheltovodov_2011]
- [Ko and Grant 2012][research_ko_grant_2012]
- [Kobayashi et al 2011][research_kobayashi_daimon_2011]
- [Kochan 2020][research_kochan_2020]
- [Kochan et al 2005][research_kochan_breiter_2005]
- [Kodigaddi 2026][research_kodigaddi_2026]
- [Kogler and Quam 1983][research_kogler_quam_1983]
- [Kohlman 1977][research_kohlman_1977]
- [Koizumi et al 1986][research_koizumi_tomizuka_1986]
- [Kokane et al 2026][research_kokane_mahbuburrahman_2026]
- [Kolli 2024][research_kolli_2024]
- [Kolodner 1950][research_kolodner_1950]
- [Kolonay and Yang 1998][research_kolonay_yang_1998]
- [Kong et al 2023][research_kong_pan_2023]
- [Konno and Furuichi 1992][research_konno_furuichi_1992]
- [Konrad et al 1992][research_konrad_smits_1992]
- [Konrad et al 1993][research_konrad_smits_1993]
- [Koo 2001][research_koo_2001]
- [Koopman and Zammit-Mangion 2025][research_koopman_zammitmangion_2025]
- [Kopzon 1958][research_kopzon_1958]
- [Korbahti 2009][research_korbahti_2009]
- [Koreanschi et al 2014][research_koreanschi_oliviu_2014]
- [Korivi et al 1998][research_korivi_newman_1998]
- [Kornev et al 2021][research_kornev_ambrozhevich_2021]
- [Kornilov 1958][research_kornilov_1958]
- [Korsun et al 2023][research_korsun_om_2023]
- [Korth 2000][research_korth_2000]
- [Kosinov et al 1990][research_kosinov_maslov_1990]
- [Kosinov et al 2000][research_kosinov_yermolaev_2000]
- [Kosinov et al 2000][research_kosinov_yermolaev_2000_b]
- [Kosinov et al 2017][research_kosinov_yermolaev_2017]
- [Kosykh 2025][research_kosykh_2025]
- [Kosykh 2026][research_kosykh_2026]
- [Kou and Zhan 2022][research_kou_zhan_2022]
- [Kouchakzadeh et al 2010][research_kouchakzadeh_rasekh_2010]
- [Kovalev et al 2015][research_kovalev_kudryavtsev_2015]
- [Kowal 2011][research_kowal_2011]
- [Kowaleczko et al 2018][research_kowaleczko_dlugolecki_2018]
- [Kowaleczko et al 2025][research_kowaleczko_pietraszek_2025]
- [Kozlov et al 2009][research_kozlov_zverkov_2009]
- [Krasil'nikov and Shmanenkov 2000][research_krasilnikov_shmanenkov_2000]
- [Krasnoshapka 1968][research_krasnoshapka_1968]
- [Krause and Dinkler 1998][research_krause_dinkler_1998]
- [Krishnan and Sandham 2005][research_krishnan_sandham_2005]
- [Krishnaswamy et al][research_krishnaswamy_papageorgiou]
- [Krivenyuk et al 1971][research_krivenyuk_tsvilyuk_1971]
- [Krone 1980][research_kronejr_1980]
- [Krone 1980][research_kronejr_1980_b]
- [Kryvokhatko 2023][research_kryvokhatko_2023]
- [Kryvokhatko 2025][research_kryvokhatko_2025]
- [Krüger et al 2014][research_kruger_klimmek_2014]
- [Kudryavtsev 2014][research_kudryavtsev_2014]
- [Kuhlman and Brown 1989][research_kuhlman_brown_1989]
- [Kuhlman and Liaw 1987][research_kuhlman_liaw_1987]
- [Kuhlman et al 1988][research_kuhlman_cerney_1988]
- [Kulfan and Sigalla 1978][research_kulfan_sigalla_1978]
- [Kumar and Choubey 2023][research_kumar_choubey_2023]
- [Kumar et al 2023][research_kumar_onkar_2023]
- [Kumar et al 2025][research_kumar_rallapalli_2025]
- [Kumari and Nath 1982][research_kumari_nath_1982]
- [Kuo 1976][research_kuo_1976]
- [Kuo et al 1972][research_kuo_morino_1972]
- [Kurzin and Mazutskii 2013][research_kurzin_mazutskii_2013]
- [Kusko 1957][research_kusko_1957]
- [Kuwata 2021][research_kuwata_2021]
- [Kuwata 2026][research_kuwata_2026]
- [Kwak et al 2006][research_kwak_yoshida_2006]
- [Kwatny et al 2008][research_kwatny_belcastro_2008]
- [Kwatny et al 2009][research_kwatny_dongmo_2009]
- [Kwatny et al 2010][research_kwatny_dongmo_2010]
- [Kwon et al 2004][research_kwon_lee_2004]
- [Kyo-Nam Koo][research_kyonamkoo]
- [Kyzmenko and Yakovlev 2018][research_kyzmenko_yakovlev_2018]
- [Körbahti and Uzal 2004][research_korbahti_uzal_2004]
- [Küchemann 1962][research_kuchemann_1962]
- [Kılıçay 2020][research_kilicay_2020]
- [La et al 2022][research_la_wang_2022]
- [Lacefield and Sprow 1994][research_lacefield_sprow_1994]
- [Lacombe and Rouges 1990][research_lacombe_rouges_1990]
- [Lada and Kontis 2005][research_lada_kontis_2005]
- [Lada and Kontis 2009][research_lada_kontis_2009]
- [Ladenburg and Bershader 1949][research_ladenburg_bershader_1949]
- [Laderman 1978][research_laderman_1978]
- [Laderman 1979][research_laderman_1979]
- [Laderman and Demetriades 1977][research_laderman_demetriades_1977]
- [Lafont and Bosson 1983][research_lafont_bosson_1983]
- [Laganelli 1970][research_laganelli_1970]
- [Lagerstrom and Graham 1949][research_lagerstrom_graham_1949]
- [Lai and Findley 1979][research_lai_findley_1979]
- [Lai and Findley 1980][research_lai_findley_1980]
- [Lai et al 1995][research_lai_huang_1995]
- [Lai et al 2021][research_lai_cunis_2021]
- [Laitone 1964][research_laitone_1964]
- [Lakshmi et al 2021][research_lakshmi_ramprabhu_2021]
- [Lallman 1985][research_lallman_1985]
- [Lallman et al 1998][research_thrust_vectoring_strakes_1998]
- [Lam and Stollenwerk 1966][research_lam_stollenwerk_1966]
- [Lamar 1975][research_lamar_1975]
- [Lamb et al 1981][research_lamb_sawyer_1981]
- [Lamb et al 1981][research_lamb_sawyer_1981_b]
- [Lampton and Valasek 2006][research_lampton_valasek_2006]
- [Landweber and Johnson 1951][research_landweber_johnson_1951]
- [Lang et al 2022][research_lang_cen_2022]
- [Lang et al 2025][research_lang_wang_2025]
- [Langham 1979][research_langham_1979]
- [Langston et al 2016][research_langston_nelson_2016]
- [Lapin 1999][research_lapin_1999]
- [Lapygin and Tret'yakov 1986][research_lapygin_tretyakov_1986]
- [Larsen et al 1963][research_larsen_litz_1963]
- [Larson 1987][research_larson_1987]
- [Lateral-Directional Dynamics 1998][research_lateral_directional_dynamics_1998]
- [Lateral-Directional Stability Theory and 2003][research_lateral_directional_stability_2003]
- [Latif et al 2007][research_latif_masud_2007]
- [Latvala and Anderson 1959][research_latvala_anderson_1959]
- [Laudeman 1972][research_laudeman_1972]
- [Lavretsky 2019][research_lavretsky_2019]
- [Lavrishcheva et al 2024][research_lavrishcheva_staroverov_2024]
- [Law 1973][research_law_1973]
- [Law 1974][research_law_1974]
- [Law 1975][research_law_1975]
- [Law 1976][research_law_1976]
- [Lawing 1975][research_coldwall_descent_1975]
- [Lawing 1981][research_hypersonic_heating_survey_1981]
- [Lawrence 1964][research_lawrence_1964]
- [Lazarev 1988][research_lazarev_1988]
- [Le Fur 1959][research_lefur_1959]
- [Le Vie 2016][research_levie_2016]
- [Leadon and Scott 1956][research_leadon_scott_1956]
- [Lebacqz et al 1974][research_lebacqz_radford_1974]
- [Lee 1984][research_lee_1984]
- [Lee 1989][research_lee_1989]
- [Lee 1993][research_lee_1993]
- [Lee 1994][research_lee_1994]
- [Lee 1994][research_lee_1994_b]
- [Lee 1998][research_lee_1998]
- [Lee and Cho 1991][research_lee_cho_1991]
- [Lee and Gross 2020][research_lee_gross_2020]
- [Lee and Gross 2021][research_lee_gross_2021]
- [Lee and Kim 2010][research_lee_kim_2010]
- [Lee and Yoon 2008][research_lee_yoon_2008]
- [Lee et al 1969][research_lee_yanta_1969]
- [Lee et al 1990][research_lee_miura_1990]
- [Lee et al 1991][research_lee_miura_1991]
- [Lee et al 1994][research_lee_kim_1994]
- [Lee et al 2013][research_lee_kim_2013]
- [Lee et al 2021][research_lee_han_2021]
- [Lee et al 2023][research_lee_lee_2023]
- [Lees 1956][research_lees_1956]
- [Lees 1959][research_lees_1959]
- [Lees and Reshotko 1962][research_lees_reshotko_1962]
- [Lei 1987][research_lei_1987]
- [Lei 1991][research_lei_1991]
- [Lei 1992][research_lei_1992]
- [Lei 1992][research_lei_1992_b]
- [Lei 1994][research_lei_1994]
- [Lei and Williams 1990][research_lei_williams_1990]
- [Lei et al 1993][research_lei_fichtel_1993]
- [Lei et al 1996][research_lei_castelli_1996]
- [Lei et al 2016][research_lei_zhao_2016]
- [Lemcoe 1973][research_lemcoe_1973]
- [Lemcoe 1992][research_lemcoe_1992]
- [Lemkey 1975][research_lemkey_1975]
- [Lemkey et al 1987][research_lemkey_smeggil_1987]
- [Lemley 1968][research_lemley_1968]
- [Lemon et al 2011][research_lemon_litt_2011]
- [Leng 1995][research_leng_1995]
- [Lensi 2000][research_lensi_2000]
- [Leonard 1938][research_leonard_1938]
- [Leontiev and Pavlyuchenko 2004][research_leontiev_pavlyuchenko_2004]
- [Leontiev and Pavlyuchenko 2008][research_leontiev_pavlyuchenko_2008]
- [Leontiev et al 2006][research_leontiev_lushchik_2006]
- [Leontiev et al 2017][research_leontiev_lushchik_2017]
- [Leontiev et al 2022][research_leontiev_lushchik_2022]
- [Leopold et al][research_leopold_gastebois]
- [Lesalli and Cahyono 2020][research_lesalli_cahyono_2020]
- [Leslie 1978][research_leslie_1978]
- [Lesoinne 2007][research_lesoinne_2007]
- [Leto et al 2016][research_leto_votta_2016]
- [Levin 1981][research_levin_1981]
- [Levin 1984][research_levin_1984]
- [Levine 1965][research_levine_1965]
- [Levine and Rumsey 1958][research_levine_rumsey_1958]
- [Levy 1992][research_levy_1992]
- [Lewis and Banner 1971][research_lewis_banner_1971]
- [Li 2008][research_li_2008]
- [Li 2023][research_li_2023]
- [Li and Eri 2007][research_li_eri_2007]
- [Li and Geiselhart 2026][research_li_geiselhart_2026]
- [Li and Han 2021][research_li_han_2021]
- [Li and Shi 2011][research_li_shi_2011]
- [Li and Song 2013][research_li_song_2013]
- [Li and Stewart 1953][research_li_stewart_1953]
- [Li and Yamaguchi 2022][research_li_yamaguchi_2022]
- [Li et al 1999][research_li_sobieczky_1999]
- [Li et al 2010][research_li_zhang_2010]
- [Li et al 2013][research_li_yang_2013]
- [Li et al 2014][research_li_huang_2014]
- [Li et al 2015][research_li_lv_2015]
- [Li et al 2015][research_li_narita_2015]
- [Li et al 2017][research_li_chen_2017]
- [Li et al 2018][research_li_zhang_2018]
- [Li et al 2019][research_li_zu_2019]
- [Li et al 2022][research_li_lv_2022]
- [Li et al 2023][research_li_wei_2023]
- [Li et al 2024][research_li_wan_2024]
- [Li et al 2026][research_li_chen_2026]
- [Li et al 2026][research_li_ganippa_2026]
- [Li et al 2026][research_li_ganippa_2026_b]
- [Liang et al 2022][research_liang_yang_2022]
- [Liang et al 2023][research_liang_wu_2023]
- [Liang et al 2026][research_liang_lu_2026]
- [Librescu and Simovich 1988][research_librescu_simovich_1988]
- [Librescu and Thangjitham 1989][research_librescu_thangjitham_1989]
- [Librescu and Thangjitham 1991][research_librescu_thangjitham_1991]
- [Librescu et al 2004][research_librescu_marzocca_2004]
- [Licher 1956][research_licher_1956]
- [Liever and Habchi 2004][research_liever_habchi_2004]
- [Lift/Drag Ratios of Optimised 1962][research_lift_drag_ratios_1962]
- [Lijewski 1980][research_lijewski_1980]
- [Lilley 1965][research_lilley_1965]
- [Lim et al 2020][research_lim_kim_2020]
- [Limerick 1991][research_limerick_1991]
- [Lin 1986][research_lin_1986]
- [Lin 1999][research_lin_1999]
- [Lin 2025][research_lin_2025]
- [Lin and Yang 2005][research_lin_yang_2005]
- [Lin et al 1993][research_lin_chan_1993]
- [Lin et al 2025][research_lin_liu_2025]
- [Lindley 1956][research_lindley_1956]
- [Linehan and Mohseni 2016][research_linehan_mohseni_2016]
- [Lingard and Darley 2005][research_lingard_darley_2005]
- [Lingard et al 1989][research_lingard_barnard_1989]
- [Lingard et al 2013][research_lingard_underwood_2013]
- [Lipatov and Tugazakov 2018][research_lipatov_tugazakov_2018]
- [Liquid Oxygen Test of 2009][research_liquid_oxygen_2009]
- [Liquid Propellant Rocket-Engine Organizations 2006 Liquid Propellant Rocket-Engine Organizations Worldwide, 1932 to 2003][research_liquid_propellant_2006]
- [Liquid Rocket Engine Combustion 1995][research_liquid_rocket_1995]
- [Liquid Rocket Engine Reliability][research_liquid_rocket]
- [Liquid Rocket Engine Thrust 2018][research_liquid_rocket_2018]
- [Lisunov 1960][research_lisunov_1960]
- [Litt et al 2014][research_litt_liu_2014]
- [Littell et al 1967][research_littell_bailey_1967]
- [Littleboy et al 1997][research_littleboy_smith_1997]
- [Liu 2022][research_liu_2022]
- [Liu 2024][research_liu_2024]
- [Liu and Grant 2009][research_liu_grant_2009]
- [Liu and Grant 2010][research_liu_grant_2010]
- [Liu and Li 2012][research_liu_li_2012]
- [Liu and Li 2021][research_liu_li_2021]
- [Liu and Lu 2011][research_liu_lu_2011]
- [Liu and Natesan 1988][research_liu_natesan_1988]
- [Liu and Oshida 1984][research_liu_oshida_1984]
- [Liu and Platzer 1970][research_liu_platzer_1970]
- [Liu and Weng 2007][research_liu_weng_2007]
- [Liu et al 1995][research_liu_wang_1995]
- [Liu et al 2011][research_liu_yin_2011]
- [Liu et al 2012][research_liu_lv_2012]
- [Liu et al 2013][research_liu_li_2013]
- [Liu et al 2019][research_liu_cook_2019]
- [Liu et al 2021][research_liu_luo_2021]
- [Liu et al 2022][research_liu_gao_2022]
- [Liu et al 2022][research_liu_li_2022]
- [Liu et al 2023][research_liu_liu_2023]
- [Liu et al 2023][research_liu_pang_2023]
- [Liu et al 2024][research_liu_liu_2024]
- [Liu et al 2025][research_liu_gao_2025]
- [Liu et al 2025][research_liu_zhang_2025]
- [Liu et al 2027][research_liu_liu_2027]
- [Livne 2023][research_livne_2023]
- [Livne 2023][research_livne_2023_b]
- [Livne 2023][research_livne_2023_c]
- [Livne 2023][research_livne_2023_d]
- [Livne and Mineau 1996][research_livne_mineau_1996]
- [Livneh 1995][research_livneh_1995]
- [Livneh 1995][research_livneh_1995_b]
- [Lobanovskii 1983][research_lobanovskii_1983]
- [Locci et al 2000][research_locci_brady_2000]
- [Lock 1958][research_lock_1958]
- [Lock 1963][research_lock_1963]
- [Lock and Bridgewater 1967][research_lock_bridgewater_1967]
- [Logan et al 2007][research_logan_davis_2007]
- [Lombaerts 2019][research_lombaerts_2019]
- [Lombaerts et al 2016][research_lombaerts_schuet_2016]
- [Long Lu and Turkoglu 2015][research_longlu_turkoglu_2015]
- [Longitudinal and Lateral Linear 2014][research_longitudinal_and_2014]
- [Loposer and Rumsey 1954][research_loposer_rumsey_1954]
- [Lorch 1981][research_lorch_1981]
- [Lorenz and Lam 2026][research_lorenz_lam_2026]
- [Lores and Zinn 1973][research_lores_zinn_1973]
- [Loss-of-Control Mishaps in Revenue][research_loss_of_control_mishaps]
- [Loth and Lee 2008][research_loth_lee_2008]
- [Lottati 1985][research_lottati_1985]
- [Lottati 1985][research_lottati_1985_b]
- [Lottati 1987][research_lottati_1987]
- [Lotze et al 1975][research_lotze_sensburg_1975]
- [Lotze et al 1977][research_lotze_sensburg_1977]
- [Lovell 2001][research_lovell_2001]
- [Low aspect ratio wing 1992][research_low_aspect_1992]
- [Low Frequency Oscillations in 2008][research_low_frequency_2008]
- [Lowe et al 2014][research_lowe_byun_2014]
- [Lowell and Barrett 1990][research_lowell_barrett_1990]
- [Lowenberg 2010][research_lowenberg_2010]
- [Lowry et al 1994][research_lowry_mellen_1994]
- [Lu][research_lu]
- [Lu and Turkoglu 2016][research_lu_turkoglu_2016]
- [Lu and Turkoglu 2018][research_lu_turkoglu_2018]
- [Luce 1949][research_luce_jr_1949]
- [Lucero 1984][research_lucero_1984]
- [Lucero 1985][research_lucero_1985]
- [Ludloff and Reiche 1947][research_ludloff_reiche_1947]
- [Ludtke 1973][research_ludtke_1973]
- [Ludtke 1986][research_ludtke_1986]
- [Luikov et al 1967][research_luikov_sergeev_1967]
- [Lukashevich et al 2023][research_lukashevich_morozov_2023]
- [Lunev 1971][research_lunev_1971]
- [Lungu and Lungu 2015][research_lungu_lungu_2015]
- [Lungu and Lungu 2016][research_lungu_lungu_2016]
- [Lurui Xia et al 2008][research_luruixia_niaoqinghu_2008]
- [Lushchik and Reshmin 2025][research_lushchik_reshmin_2025]
- [Lutz 1989][research_lutz_1989]
- [Luu and Ochi 2023][research_luu_ochi_2023]
- [Luxton 1968][research_luxton_1968]
- [Lyrio et al 2019][research_lyrio_azevedo_2019]
- [Lysenko 1987][research_lysenko_1987]
- [Lysenko 1989][research_lysenko_1989]
- [Lysenko 1995][research_lysenko_1995]
- [Lysenko and Maslov 1981][research_lysenko_maslov_1981]
- [Lysenko and Maslov 1985][research_lysenko_maslov_1985]
- [Lysenko et al 2017][research_lysenko_smorodsky_2017]
- [Lysenko et al 2025][research_lysenko_smorodsky_2025]
- [Lyu et al 2022][research_lyu_gong_2022]
- [Lyu et al 2023][research_lyu_ye_2023]
- [Ma et al 2012][research_ma_he_2012]
- [Ma et al 2017][research_ma_su_2017]
- [Ma et al 2021][research_ma_han_2021]
- [Mabey and Gaudet 1975][research_mabey_gaudet_1975]
- [Maca and Lee 1996][research_macaiii_lee_1996]
- [Macedo][research_macedo]
- [Macedo et al 2020][research_macedo_bidinotto_2020]
- [Mach Number and Reynolds 2022][research_mach_number_2022]
- [Mach Number and Wall 1978][research_mach_number_1978]
- [Machida et al 2007][research_machida_takatoya_2007]
- [Machida et al 2007][research_machida_yoshida_2007]
- [Maciejewski 1995][research_maciejewski_1995]
- [Mackay and Nagamatsu 1954][research_mackay_nagamatsu_1954]
- [MacMillen and Thompson 1999][research_macmillen_thompson_1999]
- [MacMurdy et al 1994][research_macmurdy_guruswamy_1994]
- [Madagan 1969][research_madagan_1969]
- [Maddalon et al 1990][research_maddalon_collier_1990]
- [Maekawa and Watanabe 2007][research_maekawa_watanabe_2007]
- [Maestrello 1969][research_maestrello_1969]
- [Magee et al 2015][research_magee_fugal_2015]
- [Magee et al 2022][research_magee_hayes_2022]
- [Magee et al 2024][research_magee_hayes_2024]
- [Magee et al 2025][research_magee_hayes_2025]
- [Mahlmeister et al 1955][research_mahlmeister_ishimoto_1955]
- [Mahorter and Robert G. 1961][research_mahorter_robertg_1961]
- [Maikapar 1966][research_maikapar_1966]
- [Maikapar 1993][research_maikapar_1993]
- [Mailybaev and Seiranyan 1998][research_mailybaev_seiranyan_1998]
- [Majumder 2019][research_majumder_2019]
- [Makarov and Pavlenko 2016][research_makarov_pavlenko_2016]
- [Makino and Noguchi 2003][research_makino_noguchi_2003]
- [Malcolm and Rakich 1970][research_malcolm_rakich_1970]
- [Malcolm and Rakich 1971][research_malcolm_rakich_1971]
- [Malecka 2016][research_malecka_2016]
- [Malik and Anderson 1991][research_real_gas_stability_1991]
- [Malik and Li 1993][research_malik_li_1993]
- [Maloney 2011][research_maloney_2011]
- [Manavasi et al 2011][research_manavasi_morell_2011]
- [Mangano and Martins 2021][research_mangano_martins_2021]
- [Manjhi and Kumar 2018][research_manjhi_kumar_2018]
- [Manjhi et al 2020][research_manjhi_kumar_2020]
- [Manjith 2026][research_manjith_2026]
- [Mann and Carlson 1991][research_mann_carlson_1991]
- [Mann and Carlson 1994][research_mann_carlson_1994]
- [Mann and Mercer 1985][research_mann_mercer_1985]
- [Manning and Heimerl 1960][research_elevated_tensile_practice_1960]
- [Manning and Price 1961][research_stainless_rapid_heat_1961]
- [Mansor et al 2015][research_mansor_nogoud_2015]
- [Mansour 1984][research_mansour_1984]
- [Mansy et al 1982][research_mansy_gobran_1982]
- [Manzuk 1970][research_manzuk_1970]
- [Mao and Liang 2019][research_mao_liang_2019]
- [Mao et al 2011][research_mao_lin_2011]
- [Mao et al 2019][research_mao_xie_2019]
- [Mao et al 2022][research_mao_li_2022]
- [Mao et al 2023][research_mao_guo_2023]
- [Maode and Sandström 1988][research_maode_sandstrom_1988]
- [Maples 1979][research_maples_1979]
- [Maqsood and Go 2011][research_maqsood_go_2011]
- [Mardanpour et al 2013][research_mardanpour_richards_2013]
- [Mardanpour et al 2014][research_mardanpour_richards_2014]
- [Markov 1984][research_markov_1984]
- [Martin 1953][research_martin_1953]
- [Martin 1956][research_martin_1956]
- [Martin 2007][research_martin_2007]
- [Martin 2008][research_martin_2008]
- [Martin and Gerber 1953][research_martin_gerber_1953]
- [Martin and Gerber 1953][research_martin_gerber_1953_b]
- [Martin and Gerber 1955][research_martin_gerber_1955]
- [Martin and Panesi 2022][research_martin_panesi_2022]
- [Martin-Baker at the 1988][research_martin_baker_at_1988]
- [Martina 1958][research_martina_1958]
- [Martinez 1961][research_martinez_1961]
- [Martinez et al 1990][research_martinez_reinert_1990]
- [Martos et al 2011][research_martos_kiszely_2011]
- [Maruyama et al 1978][research_maruyama_oikawa_1978]
- [Maruyama et al 1992][research_maruyama_bi_1992]
- [Maruyama et al 2009][research_maruyama_matsushima_2009]
- [Marzocca et al 2001][research_marzocca_librescu_2001]
- [Mashburn 1969][research_mashburn_1969]
- [Maslov et al 2016][research_maslov_aniskin_2016]
- [Mason 1983][research_mason_1983]
- [Mason and Ravi 1994][research_mason_ravi_1994]
- [Masoudi 1999][research_masoudi_1999]
- [Mastanaiah 1978][research_mastanaiah_1978]
- [Masterson 1963][research_masterson_1963]
- [Mastropietro et al 2013][research_mastropietro_pauken_2013]
- [Masud et al 2017][research_masud_arif_2017]
- [Masud et al 2018][research_masud_khan_2018]
- [Mateescu 1986][research_mateescu_1986]
- [Mathauser and Deveikis 1955][research_creep_2024t3_1955]
- [Mathauser and Deveikis 1957][research_creep_2024t3_1957]
- [Mathematical Modeling and Experimental 2018][research_mathematical_modeling_2018]
- [Mathew et al 2008][research_mathew_parameswaran_2008]
- [Matsumoto and Sekiya 1975][research_matsumoto_sekiya_1975]
- [Matsuo and Butler 1983][research_matsuo_butler_1983]
- [Matsuo and Kim 1993][research_matsuo_kim_1993]
- [Matsushita et al][research_matsushita_miyata]
- [Matthews 1957][research_matthews_1957]
- [Matthews et al 1972][research_matthews_buchanan_1972]
- [Matthews et al 2025][research_matthews_prince_2025]
- [Matza 1990][research_dissimilar_joints_1990]
- [Matějů 2019][research_mateju_2019]
- [Maughmer et al 1990][research_control_effectors_1990]
- [Maxwell and Jacocks 1962][research_maxwell_jacocks_1962]
- [May et al 2011][research_may_lemon_2011]
- [May et al 2023][research_may_li_2023]
- [Mayer and Kruelle 1992][research_mayer_kruelle_1992]
- [Mayle et al 1979][research_mayle_blair_1979]
- [Maziasz 2004][research_maziasz_2004]
- [Maziasz and Swindeman 2001][research_maziasz_swindeman_2001]
- [McAlarney et al 1982][research_mcalarney_arons_1982]
- [McAmis et al 1992][research_mcamis_lankford_1992]
- [McCarty and Smith 1982][research_mccarty_smith_1982]
- [McCutchen 2006][research_mccutchen_2006]
- [McDonough and Kolmanovsky 2017][research_mcdonough_kolmanovsky_2017]
- [McDonough et al 2014][research_mcdonough_kolmanovsky_2014]
- [McElderry 1973][research_mcelderry_1973]
- [McEwan 1970][research_mcewan_1970]
- [McGrath 1993][research_mcgrath_1993]
- [McGrath 1995][research_mcgrath_1995]
- [McGrath 2003][research_mcgrath_2003]
- [McGrath et al 1989][research_mcgrath_walker_1989]
- [McHugh and Leszcz 2024][research_mchugh_leszcz_2024]
- [McKay 1959][research_x15_first_landing_1959]
- [McKee 1967][research_mckee_1967]
- [McMillin and Wood 1986][research_mcmillin_wood_1986]
- [McMullen 1973][research_mcmullen_1973]
- [McMurtrey 2018][research_mcmurtrey_2018]
- [McTavish][research_mctavish]
- [Mehra and Carroll 1980][research_mehra_carroll_1980]
- [Mehta 1986][research_mehta_1986]
- [Mehta 2012][research_mehta_2012]
- [Mei 1977][research_mei_1977]
- [Mei 1978][research_mei_1978]
- [Mei et al 2012][research_mei_zhang_2012]
- [Meier 1975][research_meier_1975]
- [Meier and Rotta 1971][research_meier_rotta_1971]
- [Meisl 1986][research_meisl_1986]
- [Melek and Kaya 2009][research_melek_kaya_2009]
- [Melvill Jones 1938][research_melvilljones_1938]
- [Melville and Gordnier 1998][research_melville_gordnier_1998]
- [Melvin and Zhao 2024][research_melvin_zhao_2024]
- [Meng et al 2020][research_meng_kaihua_2020]
- [Menshchikov and Somov 2019][research_menshchikov_somov_2019]
- [Meritt et al 2017][research_meritt_schetz_2017]
- [Merkli 1975][research_merkli_1975]
- [Merlet and Rumsey 1961][research_merlet_rumsey_1961]
- [Methodic for three-dimensional parametric 2024][research_methodic_for_2024]
- [Methodology for Investigation of][research_methodology_for]
- [Metin et al 2023][research_metin_uzuner_2023]
- [Meyer 1958][research_meyer_1958]
- [Meyers et al 2025][research_meyers_duong_2025]
- [Mi 2021][research_mi_2021]
- [Mi et al 2023][research_mi_yi_2023]
- [Michaelsen 1957][research_michaelsen_1957]
- [Mickey and Stuart 1967][research_mickey_stuartjr_1967]
- [Microstructure and High Temperature 2025][research_microstructure_and_2025]
- [Mielke and Kleiser 2000][research_mielke_kleiser_2000]
- [Mielke et al 1999][research_mielke_kleiser_1999]
- [Mikhail 1979][research_mikhail_1979]
- [Mikhail 1989][research_mikhail_1989]
- [Mikilyan 2024][research_mikilyan_2024]
- [Miles 1949][research_miles_1949]
- [Miles 1953][research_miles_1953]
- [Militký et al 2025][research_militky_wiener_2025]
- [Millard et al 1989][research_millard_machin_1989]
- [Miller 1975][research_miller_jr_1975]
- [Miller and Franklin 1968][research_miller_franklin_1968]
- [Miller and Langdon 1980][research_miller_langdon_1980]
- [Miller and Schemensky 1979][research_miller_schemensky_1979]
- [Miller and Wood 1983][research_miller_wood_1983]
- [Miller et al 1982][research_miller_wykes_1982]
- [Miller et al 1983][research_miller_wykes_1983]
- [Mills 2002][research_mills_2002]
- [Min et al 2026][research_min_jinjun_2026]
- [Miner and Lewis 1973][research_miner_lewis_1973]
- [Ming et al 2016][research_ming_bingjun_2016]
- [Ming-de 1984][research_mingde_1984]
- [Miniature high temperature strain 1972][research_miniature_high_1972]
- [Minkina 1999][research_minkina_1999]
- [Mironov 1965][research_mironov_1965]
- [Mishina et al 2020][research_mishina_umeoka_2020]
- [Mitcham 1949][research_mitcham_1949]
- [Mitcham et al 1951][research_mitcham_blanchard_1951]
- [Mitcham et al 1956][research_mitcham_stevens_1956]
- [Mitchell 1969][research_mitchell_1969]
- [Mitikiri and Mohseni 2018][research_mitikiri_mohseni_2018]
- [Mitrotta et al 2025][research_mitrotta_pirrera_2025]
- [Miura 2010][research_miura_2010]
- [Miura et al 1983][research_miura_fukai_1983]
- [Miyazawa 1973][research_miyazawa_1973]
- [Miyazawa 1974][research_miyazawa_1974]
- [Mizoguchi et al 2014][research_mizoguchi_kajikawa_2014]
- [MlDDLETON and Carlson 1965][research_mlddleton_carlson_1965]
- [Mobley and Summers][research_mobley_summers]
- [Moffat and Kays 1984][research_moffat_kays_1984]
- [Moffeit et al 2023][research_moffeit_kumar_2023]
- [Moftakhar and Glinka 1998][research_moftakhar_glinka_1998]
- [Moga 1980][research_moga_1980]
- [Moga and Dejarnette 1981][research_moga_dejarnette_1981]
- [Moger and Ramsay 1964][research_moger_ramsay_1964]
- [Mohamed and Dongare 2021][research_mohamed_dongare_2021]
- [Mohamed and Joy 2021][research_mohamed_joy_2021]
- [Mohammadi et al 2015][research_mohammadi_mehdi_2015]
- [Mohammadiun and Rahimi 2012][research_mohammadiun_rahimi_2012]
- [Mohammed 2007][research_mohammed_2007]
- [Moin and Lele 1998][research_moin_lele_1998]
- [Molins et al 1991][research_molins_andrieu_1991]
- [Molloy 1999][research_molloy_1999]
- [Monaghan 1953][research_monaghan_1953]
- [Monaghan and Friend 1973][research_monaghan_friend_1973]
- [Montgomery and Hatch 1969][research_montgomery_hatch_1969]
- [Montoya 1970][research_montoya_1970]
- [Moog 1975][research_moog_1975]
- [Moon 2003][research_moon_2003]
- [Moon 2004][research_moon_2004]
- [Moon and Kim 2001][research_moon_kim_2001]
- [Moore 1991][research_moore_1991]
- [Moore and Frei 1983][research_moore_frei_1983]
- [Moore and McDonald 1946][research_moore_mcdonald_1946]
- [Moore et al 1980][research_moore_skow_1980]
- [Moore et al 2024][research_moore_morse_2024]
- [Moorthamers et al 2021][research_moorthamers_wiberg_2021]
- [Morajkar and Gamba 2016][research_morajkar_gamba_2016]
- [Moreira et al 2022][research_moreira_gripp_2022]
- [Morelli et al 2013][research_morelli_cunningham_2013]
- [Morikawa 1951][research_morikawa_1951]
- [Morikawa 1953][research_morikawa_1953]
- [Morimoto et al 2015][research_morimoto_yamashita_2015]
- [Morino 1969][research_morino_1969]
- [Morito and Sidwell 1967][research_morito_sidwell_1967]
- [Morris 1966][research_morris_1966]
- [Morris 1990][research_dryden_hwts_thermal_1990]
- [Morrisette and Goldberg 1978][research_morrisette_goldberg_1978]
- [Morton 1956][research_morton_1956]
- [Moshtaghzadeh et al 2022][research_moshtaghzadeh_izadpanahi_2022]
- [Moul and Brown 1959][research_artificial_pitch_damping_1959]
- [Moulton et al 2024][research_moulton_abraham_2024]
- [Mueller and Torres 2001][research_mueller_torres_2001]
- [Muhlstein 1966][research_muhlsteinjr_1966]
- [Muhlstein 1972][research_muhlsteinjr_1972]
- [Mukambetov and Borovik 2022][research_mukambetov_borovik_2022]
- [Mukherjee and Martin 1963][research_mukherjee_martin_1963]
- [Mukherjee and Sinha 2016][research_mukherjee_sinha_2016]
- [Mullendore and Grant 1964][research_mullendore_grant_1964]
- [Muller 1967][research_muller_1967]
- [Multifractal Detrended Fluctuation Analysis 2023][research_multifractal_detrended_2023]
- [Mumaw et al 2019][research_mumaw_haworth_2019]
- [Munk 1950][research_munk_1950]
- [Murakami et al 2008][research_murakami_kwak_2008]
- [Murashkin et al 2020][research_murashkin_bruyaka_2020]
- [Murphy and Klein 2010][research_murphy_klein_2010]
- [Murphy and Voss 1996][research_murphy_voss_1996]
- [Murray 1961][research_murray_1961]
- [Murri et al 1983][research_murri_croom_1983]
- [Murtaza and Indluru 2026][research_murtaza_indluru_2026]
- [Murzionak][research_murzionak]
- [Musa et al 2015][research_musa_mansor_2015]
- [Musa et al 2026][research_musa_mansor_2026]
- [Muthaiah et al 2023][research_m_saini_2023]
- [Muthaiah et al 2025][research_muthaiah_saini_2025]
- [Myers and Walsh 1988][research_myers_walsh_1988]
- [Mysliwetz 1963][research_mysliwetz_1963]
- [Müller et al 2021][research_muller_traudt_2021]
- [NACA 1943 The Effect of Artificial Aging on the Tensile Properties of Alclad Aluminium][research_alclad_aging_1943]
- [NACA 1956 Some Effects of Aircraft Configuration on Static Longitudinal and Directional Stability][research_config_stability_1956]
- [NACA Conference on Aircraft 1957][research_loads_flutter_conf_1957]
- [NACA Conference on High-speed 1958][research_highspeed_conference_1958]
- [Nadim Melhem et al 2024][research_nadimmelhem_richardmunroe_2024]
- [Nae 2026][research_nae_2026]
- [Naftaly and Raveh 2025][research_naftaly_raveh_2025]
- [Nagelschmidt et al 2025][research_nagelschmidt_herbrich_2025]
- [Nair and Vaidyanathan 2022][research_nair_vaidyanathan_2022]
- [Najafi et al 2024][research_najafi_kharrat_2024]
- [Nakai et al 1967][research_nakai_takagi_1967]
- [Nam et al 2018][research_nam_moon_2018]
- [Nangia et al 2003][research_nangia_palmer_2003]
- [Napolitano and Kincheloe 1996][research_napolitano_kincheloe_1996]
- [Narayan 1974][research_narayan_1974]
- [Narayan 1975][research_narayan_1975]
- [Narayan et al 2025][research_narayan_kumar_2025]
- [Nardi Rezende 2018][research_nardirezende_2018]
- [Narita et al 2001][research_narita_hayashi_2001]
- [Narita et al 2023][research_narita_sakata_2023]
- [NASA 1961 Rapid-Rate Compression Testing of Sheet Materials at High Temperatures][research_rapid_compression_1961]
- [NASA 1979 Elevated-Temperature Effects on Strain Gauges on the YF-12A Wing][research_yf12_strain_gauges_1979]
- [NASA 1985 Elevated Temperature Creep-Rupture Behaviour of a Single Crystal Nickel-Base Superalloy][research_creep_single_crystal_1985]
- [NASA 1986 Compressible Laminar Boundary Layer with Real Gas Effects][research_real_gas_boundary_layer_1986]
- [NASA 1989 Surface Modification of Monel K-500 to Reduce Friction and Wear][research_monel_k500_1989]
- [NASA 1990 Design and Operational Features of Low-Disturbance Wind Tunnels at Langley][research_low_disturbance_tunnels_1990]
- [NASA 1991 Analysis of Cooling Systems for Hypersonic Aircraft][research_cooling_hypersonic_1991]
- [NASA 1993 Creep-Rupture Strength of a Nickel-Base Superalloy at 1400 Kelvin][research_creep_rupture_superalloy_1993]
- [Natali et al 2013][research_natali_rallini_2013]
- [Naval Ordnance Systems Command Washington Dc 1957][research_navalordnancesystemscommandwashingtondc_1957]
- [Negaard 1979][research_negaard_1979]
- [Nelsen 1995][research_nelsen_1995]
- [Nelson and Bresnahan 1983][research_nelson_bresnahan_1983]
- [Nemish and Chernopiskii 1974][research_nemish_chernopiskii_1974]
- [Nepomuceno et al 2022][research_nepomuceno_moura_2022]
- [Nestler 1978][research_nestler_1978]
- [Nettleton 1965][research_nettleton_1965]
- [Neumann and Freeman 2012][research_neumann_freeman_2012]
- [Newell and Rajagopal 1993][research_newell_rajagopal_1993]
- [Newey][research_newey]
- [Newman and Buttrill 1995][research_newman_buttrill_1995]
- [Newman III et al 1999][research_newmaniii_newman_1999]
- [Newsom and Anglin 1975][research_newsom_anglin_1975]
- [Newton 1965][research_newton_1965]
- [Nguyen 1979][research_nguyen_1979]
- [Nguyen 2008][research_nguyen_2008]
- [Nguyen 2025][research_nguyen_2025]
- [Nguyen and Sirignano 2018][research_nguyen_sirignano_2018]
- [Nguyen and Sirignano 2019][research_nguyen_sirignano_2019]
- [Nguyen et al 2016][research_nguyen_ting_2016]
- [Nguyen et al 2017][research_nguyen_popov_2017]
- [Nguyen et al 2017][research_nguyen_ting_2017]
- [Nguyen et al 2021][research_nguyen_lowenberg_2021]
- [Ni et al 2016][research_ni_lu_2016]
- [Ni et al 2025][research_ni_wang_2025]
- [Nichols 1974][research_nichols_1974]
- [Nickel et al 1992][research_nickel_fu_1992]
- [Nicolaides and Brady 1959][research_nicolaides_brady_1959]
- [Nie et al 2022][research_nie_song_2022]
- [Niel][research_niel]
- [Nielsen 1986][research_nielsen_1986]
- [Niemi 1992][research_niemi_jr_1992]
- [Nieto Gómez and Chimeno Manguán 2025][research_nietogomez_chimenomanguan_2025]
- [Nietubicz 1975][research_nietubicz_1975]
- [Nikbay et al 2009][research_nikbay_oncu_2009]
- [Nikulin et al 2010][research_nikulin_kaibyshev_2010]
- [Nilsson and Sandström 1988][research_nilsson_sandstrom_1988]
- [Nix 1982][research_nix_1982]
- [Nix 1984][research_nix_1984]
- [Njuguna 2007][research_njuguna_2007]
- [Nobakhti and Soltani 2014][research_nobakhti_soltani_2014]
- [Nobakhti and Soltani 2016][research_nobakhti_soltani_2016]
- [Noll et al 1983][research_noll_calico_1983]
- [Noll et al 1983][research_noll_eastep_1983]
- [Noll et al 1984][research_noll_eastep_1984]
- [Nomura 2003][research_nomura_2003]
- [Non-linear throttling analysis of 1999][research_non_linear_throttling_1999]
- [Nonlinear panel flutter in 1991][research_nonlinear_panel_1991]
- [Nonweiler 1959][research_nonweiler_1959]
- [Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952]
- [Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952_b]
- [Northrop Aircraft Inc Hawthorne Ca 1953][research_northropaircraftinchawthorneca_1953]
- [Northrop Aircraft Inc Hawthorne Ca 1953][research_northropaircraftinchawthorneca_1953_b]
- [Nouri et al 2019][research_nouri_sahmani_2019]
- [Novopashin 1985][research_novopashin_1985]
- [Nowak and Kelly 1976][research_nowak_kelly_1976]
- [Nowak and Kelly 1977][research_nowak_kelly_1977]
- [Numerical Method and Simulations 2016][research_numerical_method_2016]
- [Numerical Studies on the 2003][research_numerical_studies_2003]
- [Nusca 1984][research_nusca_1984]
- [Nusca 2007][research_nusca_2007]
- [Nusca 2008][research_nusca_2008]
- [Nusca 2010][research_nusca_2010]
- [Nyman 1965][research_nyman_1965]
- [Nyquist 1928][research_nyquist_1928]
- [O'Brien et al][research_obrien_frazier]
- [O'Donnell and Mohseni 2017][research_odonnell_mohseni_2017]
- [O'Farrell et al 2016][research_ofarrell_brandeau_2016]
- [O'Farrell et al 2018][research_ofarrell_karlgaard_2018]
- [O'Farrell et al 2022][research_ofarrell_clark_2022]
- [O'Farrell et al 2023][research_ofarrell_leylek_2023]
- [O'hara 1971][research_ohara_1971]
- [Odabas et al 2025][research_odabas_karaoglanli_2025]
- [Of current interest Liquid 1958][research_of_current_1958]
- [Ogburn 1998][research_ogburn_1998]
- [Oggioni et al 2026][research_oggioni_riboldi_2026]
- [Ogren et al 1974][research_ogren_sotanski_1974]
- [Oh et al 2024][research_oh_shin_2024]
- [Ohira et al 2013][research_ohira_kwak_2013]
- [Ojetola et al 2011][research_ojetola_onyebueke_2011]
- [Ojiaku and Prakash 2026][research_ojiaku_prakash_2026]
- [Okayasu et al 1983][research_okayasu_higashino_1983]
- [Okayasu et al 2002][research_okayasu_ohta_2002]
- [Oktay and Asma 2000][research_oktay_asma_2000]
- [Okumoto and Elsanker 1973][research_okumoto_elsanker_1973]
- [Okuno and Park 1968][research_okuno_park_1968]
- [Oldrieve 1975][research_oldrieve_1975]
- [Olejnik and Zalewski 2020][research_olejnik_zalewski_2020]
- [Olsen and Seegmiller 1993][research_olsen_seegmiller_1993]
- [Olson 1967][research_olson_1967]
- [Olsson 1978][research_olsson_1978]
- [Olstad 1969][research_olstad_1969]
- [Om et al 1982][research_om_childs_1982]
- [Oorebeek and Babinsky 2013][research_oorebeek_babinsky_2013]
- [Opalka 1968][research_opalka_1968]
- [Optimal Design of Fuel-Rich 2004][research_optimal_design_2004]
- [Optimum time of delay 1942][research_optimum_time_1942]
- [Orlik-Ruckemann et al 1972][research_orlikruckemann_laberge_1972]
- [Orme and Conners 1994][research_orme_conners_1994]
- [Orme and Gilyard 1993][research_orme_gilyard_1993]
- [Ormsbee 1962][research_ormsbee_1962]
- [Ortamevzi 2015][research_ortamevzi_2015]
- [Ortega et al 2017][research_ortega_flores_2017]
- [Osherov and Natan 1999][research_osherov_natan_1999]
- [Osipov 2019][research_osipov_2019]
- [Oswatitsch 1980][research_oswatitsch_1980]
- [Ott and Anderson 1994][research_ott_anderson_1994]
- [Otto and Flage 1960][research_otto_flage_1960]
- [Ouhabi and Narsipur 2025][research_ouhabi_narsipur_2025]
- [Ouyang et al 2021][research_ouyang_zeng_2021]
- [Ouyang et al 2026][research_ouyang_zhang_2026]
- [Owen 1969][research_owen_1969]
- [Owen 1971][research_owen_1971]
- [Owens and Wahls 2001][research_owens_wahls_2001]
- [Owens et al 2002][research_reynolds_sst_2002]
- [Owens et al 2007][research_owens_wahls_2007]
- [Oyibo 1983][research_oyibo_1983]
- [Oyibo 1984][research_oyibo_1984]
- [Ozcan et al 2025][research_ozcan_tekyurt_2025]
- [Ozcatalbas et al 2018][research_ozcatalbas_acar_2018]
- [Padova and Falk 1980][research_padova_falk_1980]
- [Pages and Achipa 2026][research_pages_achipa_2026]
- [Pahutová et al 1969][research_pahutova_cadek_1969]
- [Pakhomov 2015][research_pakhomov_2015]
- [Palakurthy et al 2022][research_palakurthy_zope_2022]
- [Palchekovskaya 2014][research_palchekovskaya_2014]
- [Palej and Palacz 2018][research_palej_palacz_2018]
- [Palmer et al 1995][research_palmer_henline_1995]
- [Pan and Huang 2018][research_pan_huang_2018]
- [Pan and Huang 2019][research_pan_huang_2019]
- [Pan et al 2010][research_pan_wu_2010]
- [Pan et al 2021][research_pan_cao_2021]
- [Pan et al 2026][research_pan_zhang_2026]
- [Panel flutter in a 1991][research_panel_flutter_1991]
- [Pany 2023][research_pany_2023]
- [Papirno and Gerard 1962][research_papirno_gerard_1962]
- [Pappas 1954][research_pappas_1954]
- [Parate 2020][research_parate_2020]
- [Parate 2022][research_parate_2022]
- [Park and Ahn 1998][research_park_ahn_1998]
- [Park and Ahn 1999][research_park_ahn_1999]
- [Park and Ahn 2020][research_park_ahn_2020]
- [Park and Green 2000][research_park_green_2000]
- [Park and Jeon 2024][research_park_jeon_2024]
- [Park and Yoon 1989][research_real_gas_trim_1989]
- [Park et al 2001][research_park_lee_2001]
- [Park et al 2024][research_park_lee_2024]
- [Park et al 2024][research_park_moon_2024]
- [Parker et al 1991][research_parker_spain_1991]
- [Parkinson et al 1995][research_parkinson_skorodelov_1995]
- [Parks 1965][research_parks_1965]
- [Parks 1966][research_parks_1966]
- [Parlett 1961][research_parlett_1961]
- [Pasiuk 1963][research_pasiuk_1963]
- [Pasiuk et al 1963][research_pasiuk_hastings_1963]
- [Passos][research_passos]
- [Pastuszko et al 2024][research_pastuszko_chauvo_2024]
- [Patel 2016][research_patel_2016]
- [Patel and Czarnecki 1975][research_patel_czarnecki_1975]
- [Patel and Czarnecki 1977][research_patel_czarnecki_1977]
- [Patil 2003][research_patil_2003]
- [Patil and Hodges 2000][research_patil_hodges_2000]
- [Patnaik et al 1998][research_patnaik_guptill_1998]
- [Patterson 1966][research_patterson_1966]
- [Pauck and Engelbrecht 2012][research_pauck_engelbrecht_2012]
- [Pavlyuchenko et al 1985][research_pavlyuchenko_tyutin_1985]
- [Payne 1969][research_payne_1969]
- [Payne 1973][research_payne_1973]
- [Payne and Band 1976][research_payne_band_1976]
- [Pearson 1960][research_pearson_1960]
- [Pearson 1961][research_pearson_1961]
- [Pecora and Pecora 2018][research_pecora_pecora_2018]
- [Pedersen 1961][research_pedersen_1961]
- [Peichl et al 1987][research_peichl_wortmann_1987]
- [Pelletier and Mueller 1999][research_pelletier_mueller_1999]
- [Pellettlere et al 2003][research_pellettlere_nguyen_2003]
- [Peltzer et al 2008][research_peltzer_nitsche_2008]
- [Pempie and Vernin 2001][research_pempie_vernin_2001]
- [Pena et al 2018][research_fiber_optic_loads_2018]
- [Penkalla et al 1988][research_penkalla_schubert_1988]
- [Pepelea et al 2018][research_pepelea_cojocaru_2018]
- [Pereira and Roberts 1997][research_pereira_roberts_1997]
- [Perera and Guo 2008][research_perera_guo_2008]
- [Perez et al 2024][research_perez_johns_2024]
- [Perez et al 2025][research_perez_hader_2025]
- [Perkins et al 1993][research_perkins_halljr_1993]
- [Perraud et al 2003][research_perraud_moens_2003]
- [Perry 2007][research_perry_2007]
- [Pervaiz et al 1994][research_pervaiz_erler_1994]
- [Peters and Phares 1976][research_peters_phares_1976]
- [Petersen 1981][research_petersen_1981]
- [Peterson 1961][research_peterson_1961]
- [Peterson 2024][research_peterson_2024]
- [Peterson and Menees 1961][research_peterson_menees_1961]
- [Peterson and Roberts 1973][research_peterson_roberts_1973]
- [Peterson et al 2018][research_peterson_derkevorkian_2018]
- [Pfaff 1965][research_pfaff_1965]
- [Pharokhipanah and Bouckenooghe 2024][research_pharokhipanah_bouckenooghe_2024]
- [Phillips 1948][research_phillips_1948]
- [Phinney 1974][research_phinney_1974]
- [Piacentino et al 1978][research_piacentino_mcenerney_1978]
- [Piccolo Serafim et al 2023][research_piccoloserafim_freydin_2023]
- [Pickl 1989][research_pickl_1989]
- [Pieniazek 2025][research_pieniazek_2025]
- [Pierson 1972][research_pierson_1972]
- [Pierson 1975][research_pierson_1975]
- [Pierson and Chen 1979][research_pierson_chen_1979]
- [Pilot Escape Capsule 1961][research_pilot_escape_1961]
- [Piltch et al 1994][research_piltch_jihfen_1994]
- [Pinsky and Essary 1994][research_pinsky_essary_1994]
- [Pint et al 2003][research_pint_pellettiere_2003]
- [Pipko 1966][research_pipko_1966]
- [Pish et al 2019][research_pish_moradi_2019]
- [Pitcher and Maple 2008][research_pitcher_maple_2008]
- [Pitt 2004][research_pitt_2004]
- [Pittman and Bonhaus 1987][research_pittman_bonhaus_1987]
- [Pittman and Siclari 1984][research_pittman_siclari_1984]
- [Pitts and Murbach 1982][research_pitts_murbach_1982]
- [Pittsburgh Univ Washington Dc Research Staff 1966][research_pittsburghunivwashingtondcresearchstaff_1966]
- [Pivko 1956][research_pivko_1956]
- [Pizzaia and Rossmann 2018][research_pizzaia_rossmann_2018]
- [Placco 2023][research_placco_2023]
- [Placco 2023][research_placco_2023_b]
- [Placco et al 2026][research_placco_hancock_2026]
- [Plank 1975][research_hypersonic_wing_structure_1975]
- [Plath][research_plath]
- [Platou 1959][research_platou_1959]
- [Platzer and Sherer 1967][research_platzer_sherer_1967]
- [Platzer and Sherer 1968][research_platzer_sherer_1968]
- [Plaut 1968][research_plaut_1968]
- [Plaut 1971][research_plaut_1971]
- [Pleasants 1975][research_pleasants_1975]
- [Pletcher 1971][research_pletcher_1971]
- [Plummer et al][research_plummer_mendelev]
- [Podnebesnov 1984][research_podnebesnov_1984]
- [Pohuliaiko and Vernyhora 2026][research_pohuliaiko_vernyhora_2026]
- [Polak 1974][research_polak_1974]
- [Pollock and Wild 2024][research_pollock_wild_2024]
- [Poolla and Ishihara 2015][research_poolla_ishihara_2015]
- [Pope 1968][research_pope_1968]
- [Popescu 1999][research_popescu_1999]
- [Popescu 2000][research_popescu_2000]
- [Popov et al 2013][research_popov_sideris_2013]
- [Popov et al 2014][research_popov_sideris_2014]
- [Popov et al 2016][research_popov_sideris_2016]
- [Popov et al 2017][research_popov_sideris_2017]
- [Popytalov and Samsonov 1978][research_popytalov_samsonov_1978]
- [Porter 1965][research_porter_1965]
- [Portnoy 1961][research_portnoy_1961]
- [Posingies 1968][research_posingies_1968]
- [Poth et al 1993][research_pothjr_fisher_1993]
- [Potvin 2007][research_potvin_2007]
- [Potvin and Potvin 1997][research_potvin_potvin_1997]
- [Potvin and Ray 2019][research_potvin_ray_2019]
- [Pourtakdoust and Fazelzadeh 2003][research_pourtakdoust_fazelzadeh_2003]
- [Prakash et al 2009][research_prakash_uthup_2009]
- [Prakash et al 2023][research_prakash_ganapathi_2023]
- [Prandtl 1928][research_prandtl_1928]
- [Prata et al 2022][research_prata_2022]
- [Prathap 1978][research_prathap_1978]
- [Pratheepan and Bruce Ralphin Rose 2015][research_j_j_2015]
- [Prediction of Creep Rupture 2010][research_prediction_of_2010]
- [Preliminary Design of the 1983][research_preliminary_design_1983]
- [Prescott et al 1992][research_prescott_mitchell_1992]
- [Pressure Fluctuations Underlying Attached 1975][research_pressure_fluctuations_1975]
- [Pressure-temperature relation for constant-area 1958][research_pressure_temperature_relation_1958]
- [Pressurization of Liquid Propellant 2019][research_pressurization_of_2019]
- [Price 1943][research_price_1943]
- [Price 1964][research_price_1964]
- [Price 1965][research_price_1965]
- [Price 1980][research_price_1980]
- [Price and Earl A. 1970][research_price_earla_1970]
- [Priest et al 2010][research_priest_ernisse_2010]
- [Princeton Univ Nj 1952][research_princetonunivnj_1952]
- [Pritchard 1969][research_pritchard_1969]
- [Pritchard et al 2013][research_pritchard_carroll_2013]
- [Probstein 1953][research_probstein_1953]
- [Procacci et al 2026][research_procacci_digiorgio_2026]
- [Prokopenko 2026][research_prokopenko_2026]
- [Properties and Design of 2012][research_properties_and_2012]
- [Propulsion Systems from Takeoff 1991][research_propulsion_systems_1991]
- [Pryzybylski 1990][research_pryzybylski_1990]
- [Pugh et al 2023][research_pugh_goman_2023]
- [Purvis 1983][research_purvis_1983]
- [Purvis 1984][research_purvis_1984]
- [Purvis 1984][research_purvis_1984_b]
- [Pustovyi 2026][research_pustovyi_2026]
- [Putman 1969][research_putman_1969]
- [Putnam 1983][research_putnam_1983]
- [Qasrawi and East 1981][research_qasrawi_east_1981]
- [Qayoum and Panigrahi 2014][research_qayoum_panigrahi_2014]
- [Qi et al 2022][research_qi_cheng_2022]
- [Qi et al 2026][research_qi_zhang_2026]
- [Qian et al 2026][research_qian_tang_2026]
- [Qiao et al 2018][research_qiao_zhou_2018]
- [Qiao et al 2019][research_qiao_zhou_2019]
- [Qin et al 2016][research_qin_zhang_2016]
- [Qin et al 2017][research_qin_xu_2017]
- [Qiu et al 2021][research_qiu_dai_2021]
- [Qu et al 2026][research_qu_xie_2026]
- [Quan et al 2022][research_quan_lianyiwang_2022]
- [Quinn 1986][research_quinn_1986]
- [Quinn and Gong 1978][research_quinn_gong_1978]
- [Quinn and Gong 2000][research_transient_surface_temp_2000]
- [R.Yass et al 2009][research_aryass_hfarhood_2009]
- [Rabinovitch et al 2018][research_rabinovitch_huang_2018]
- [Rabinovitch et al 2019][research_rabinovitch_griffin_2019]
- [Rabinovitch et al 2019][research_rabinovitch_huang_2019]
- [Rabinovitch et al 2022][research_rabinovitch_asad_2022]
- [Radkey et al 1976][research_radkey_welge_1976]
- [Radkey et al 1978][research_radkey_welge_1978]
- [Rafi and Steck 2013][research_rafi_steck_2013]
- [Rafi et al 2012][research_rafi_steck_2012]
- [Rafi et al 2017][research_rafi_steck_2017]
- [Rafi et al 2019][research_rafi_steck_2019]
- [Rafi et al 2020][research_rafi_steck_2020]
- [Rafi et al 2021][research_rafi_steck_2021]
- [Raghavan and Ananthkrishnan 2005][research_raghavan_ananthkrishnan_2005]
- [Raghavan and Ananthkrishnan 2023][research_raghavan_ananthkrishnan_2023]
- [Ragulin and Shvalev 1983][research_ragulin_shvalev_1983]
- [Rahimian et al 2017][research_rahimian_ji_2017]
- [Rahman et al 2024][research_rahman_bandal_2024]
- [Rahman et al 2024][research_rahman_chandel_2024]
- [Rahman et al 2025][research_rahman_bandal_2025]
- [Rain Erosion Tests on 1955][research_rain_erosion_1955]
- [Rainen and Ekvall 1988][research_rainen_ekvall_1988]
- [Rajadas et al 1998][research_rajadas_juryiv_1998]
- [Rajamurthy 2002][research_rajamurthy_2002]
- [Rajamurugu et al 2024][research_rajamurugu_satyam_2024]
- [Rajamurugu et al 2024][research_rajamurugu_satyam_2024_b]
- [Rajaram et al 2017][research_rajaram_rafi_2017]
- [Raju et al 1978][research_raju_chandra_1978]
- [Rakow and Waas 2004][research_rakow_waas_2004]
- [Rakow and Waas 2005][research_rakow_waas_2005]
- [Raman 1999][research_raman_1999]
- [Rambacher et al 2024][research_rambacher_butler_2024]
- [Ramirez et al 2017][research_ramirez_haque_2017]
- [Rand 1963][research_rand_1963]
- [Randels 1954][research_randels_1954]
- [Ransbury and Carroll 2014][research_ransbury_carroll_2014]
- [Rao and Lundgren 1997][research_rao_lundgren_1997]
- [Rashis and Bond 1961][research_skin_temp_freeflight_1961]
- [Rasmussen 1978][research_rasmussen_1978]
- [Ratnayake et al 2011][research_ratnayake_waggoner_2011]
- [Raveh and Levy 2004][research_raveh_levy_2004]
- [Ravi and Mason 1994][research_ravi_mason_1994]
- [Ray and Kassing 1986][research_ray_kassing_1986]
- [Razgonyaev and Mason 1995][research_razgonyaev_mason_1995]
- [Razi and Ghadiri 2008][research_razi_ghadiri_2008]
- [Re 1974][research_re_1974]
- [Rea et al 2017][research_rea_pecora_2017]
- [Rea et al 2018][research_rea_pecora_2018]
- [Readshaw 1961][research_readshaw_1961]
- [Reardon 1989][research_reardon_1989]
- [Reardon 1997][research_reardon_1997]
- [Reardon et al 1964][research_reardon_crocco_1964]
- [Rechter and Harada 1961][research_rechter_harada_1961]
- [Reda 1977][research_reda_1977]
- [Reddy et al 2014][research_reddy_saikia_2014]
- [Redford et al 2009][research_redford_sandham_2009]
- [Reed 1955][research_x5_tail_loads_1955]
- [Reed 1984][research_reed_1984]
- [Reed and Watts 1961][research_x15_skin_temps_1961]
- [Regan 1964][research_regan_1964]
- [Rehman 2022][research_rehman_2022]
- [Reibert et al 1997][research_reibert_saric_1997]
- [Reich et al 2002][research_reich_raveh_2002]
- [Reichert][research_reichert]
- [Reigel 2004][research_reigel_2004]
- [Reimann et al 2026][research_reimann_franze_2026]
- [Reimer et al][research_reimer_braun]
- [Ren et al 2021][research_ren_zhang_2021]
- [Render et al 2026][research_render_bello_2026]
- [Resende 1992][research_resende_1992]
- [Reshotko and Khan 1980][research_reshotko_khan_1980]
- [Reubush and Mercer 1974][research_reubush_mercer_1974]
- [Reuter et al][research_reuter_mcgehee]
- [Reuther 2002][research_reuther_2002]
- [Reuther and Jameson 1995][research_reuther_jameson_1995]
- [Reuther et al 1996][research_reuther_rimlinger_1996]
- [Reuther et al 1999][research_reuther_alonso_1999]
- [Rezaei et al 2025][research_rezaei_jafari_2025]
- [Rezende 2021][research_rezende_2021]
- [Rhee et al 2008][research_rhee_lee_2008]
- [Rhisat and Molki 2024][research_rhisat_molki_2024]
- [Rhodeside 1986][research_rhodeside_1986]
- [Ribeiro et al 2022][research_ribeiro_casalino_2022]
- [Ribeiro et al 2022][research_ribeiro_casalino_2022_b]
- [Ricciardi et al 2026][research_ricciardi_trout_2026]
- [Rice 1981][research_rice_1981]
- [Rice et al 2010][research_rice_flandro_2010]
- [Richards et al 2012][research_richards_gandhi_2012]
- [Richards et al 2016][research_richards_gandhi_2016]
- [Richards et al 2018][research_richards_gandhi_2018]
- [Richecoeur et al 2008][research_richecoeur_ducruix_2008]
- [Ricketts and Doggett 1980][research_fsw_divergence_tunnel_1980]
- [Rieken et al 2020][research_rieken_berry_2020]
- [Rigby and Rae 1989][research_rigby_rae_1989]
- [Rimer et al 1983][research_rimer_chipman_1983]
- [Rimer et al 1984][research_rimer_chipman_1984]
- [Rimer et al 1986][research_rimer_chipman_1986]
- [Ritter et al 2017][research_ritter_dillinger_2017]
- [Ritter et al 2021][research_ritter_hilger_2021]
- [Ritter et al 2023][research_ritter_fehrs_2023]
- [Rivard 1965][research_rivard_1965]
- [Rivers and Glass 2006][research_rivers_glass_2006]
- [Rizk and Ben-Shmuel 1985][research_rizk_benshmuel_1985]
- [Rizzetta 1995][research_rizzetta_1995]
- [Rizzi et al 1997][research_rizzi_delvo_1997]
- [Ro et al 1992][research_ro_barlow_1992]
- [Roach and VanEcho 1981][research_roach_vanecho_1981]
- [Roach and VanEcho 1984][research_roach_vanecho_1984]
- [Robert 1988][research_robert_1988]
- [Roberts 1948][research_roberts_1948]
- [Roberts 1999][research_roberts_1999]
- [Robertson et al 2006][research_robertson_charles_2006]
- [Robins and Carlson 1979][research_robins_carlson_1979]
- [Robinson 1948][research_robinson_1948]
- [Robinson 1952][research_robinson_1952]
- [Robinson and Robinson 1950][research_robinson_robinson_1950]
- [Robinson et al 2025][research_robinson_ouhabi_2025]
- [Rocha Da Costa][research_rochadacosta]
- [Rocha et al 2023][research_rocha_saska_2023]
- [Rock and Habchi 1997][research_rock_habchi_1997]
- [Rock and Habchi 1998][research_rock_habchi_1998]
- [Rock et al 1999][research_rock_habchi_1999]
- [Rocket-Powered Aircraft 2017][research_rocket_powered_aircraft_2017]
- [Rocketdyne Canoga Park Ca 1961][research_rocketdynecanogaparkca_1961]
- [Rodden 1964][research_rodden_1964]
- [Rodden 1989][research_rodden_1989]
- [Rodden 1989][research_rodden_1989_b]
- [Rodden and Bellinger 1982][research_rodden_bellinger_1982]
- [Rodert 1940][research_heating_ice_1940]
- [Rodgers 1992][research_rodgers_1992]
- [Rodrigues 2026][research_rodrigues_2026]
- [Roe and Kattus 1957][research_roe_kattus_1957]
- [Roecker 1955][research_roecker_1955]
- [Roelke et al 2025][research_roelke_green_2025]
- [Roemer et al 2011][research_roemer_ge_2011]
- [Rogal 1965][research_rogal_1965]
- [Rohl and Schrage 1992][research_rohl_schrage_1992]
- [Rohling 1969][research_rohling_1969]
- [Rohrbach and Knublauch 1968][research_rohrbach_knublauch_1968]
- [Roland et al 2016][research_roland_edwards_2016]
- [Roll Damping Analysis of 2023][research_roll_damping_2023]
- [Rolling Maneuvers 1996][research_rolling_maneuvers_1996]
- [Rolls and Arayici 1985][research_rolls_arayici_1985]
- [Rollstin 1986][research_rollstin_1986]
- [Rom 1965][research_rom_1965]
- [Rom et al 1970][research_rom_seginer_1970]
- [Romanenko and Kharchenko 1963][research_romanenko_kharchenko_1963]
- [Rongrong et al 2018][research_rongrong_zhengyin_2018]
- [Rooks et al 2020][research_rooks_novotny_2020]
- [Roos 1985][research_roos_1985]
- [Rosa 1982][research_rosa_1982]
- [Rosales and Stoltzfus 2009][research_rosales_stoltzfus_2009]
- [Rose and Pittman 1989][research_rose_pittman_1989]
- [Rose and Stankevics 1963][research_rose_stankevics_1963]
- [Rose et al 1988][research_rose_miller_1988]
- [Rosen et al 1979][research_rosen_pavish_1979]
- [Rosen et al 1980][research_rosen_pavish_1980]
- [Rosenberg 1944][research_rosenberg_1944]
- [Rosli et al 2022][research_rosli_razak_2022]
- [Ross 1972][research_ross_1972]
- [Ross 2021][research_ross_2021]
- [Rossmann and Pizzaia 2014][research_rossmann_pizzaia_2014]
- [Rotordynamic Analysis of a 2008][research_rotordynamic_analysis_2008]
- [Rouillard et al 2009][research_rouillard_cabet_2009]
- [Roux and Bontoux 1975][research_roux_bontoux_1975]
- [Roux and Cruciani 2007][research_roux_cruciani_2007]
- [Row and Fischel 1963][research_row_fischel_1963]
- [Rowell 1964][research_rowell_1964]
- [Roy et al 2019][research_roy_saikia_2019]
- [Roysdon and Khalid 2010][research_roysdon_khalid_2010]
- [Roysdon and Khalid 2011][research_roysdon_khalid_2011]
- [Ru-ren Chow 1963][research_rurenchow_1963]
- [Ruan and Xiao 2025][research_ruan_xiao_2025]
- [Ruban et al 1991][research_ruban_fot_1991]
- [Rubio and Ballard 1967][research_rubio_ballard_1967]
- [Ruffin et al 2018][research_ruffin_barato_2018]
- [Ruffin et al 2019][research_ruffin_paccagnella_2019]
- [Ruffin et al 2022][research_ruffin_paccagnella_2022]
- [Ruflin and Grantham 1984][research_ruflin_grantham_1984]
- [Rumsey and Lee 1958][research_heat_transfer_mach146_1958]
- [Rumsey and Lee 1961][research_cone_heat_transfer_1961]
- [Rumsey and Lee 1961][research_rumsey_lee_1961]
- [Runyan et al 1970][research_runyan_forsberg_1970]
- [Rupp and McMurtrey 2020][research_rupp_mcmurtrey_2020]
- [Rupp and McMurtrey 2021][research_rupp_mcmurtrey_2021]
- [Rushby 1993][research_rushby_1993]
- [Russell 1996][research_russell_1996]
- [Russell 1996][research_russell_1996_b]
- [Ruth et al 1990][research_ruth_ahn_1990]
- [Rutkowski 1979][research_rutkowski_1979]
- [Ryan 1966][research_ryan_1966]
- [Ryazantsev et al 2026][research_ryazantsev_lomakin_2026]
- [S. Hameed and G. R 2021][research_hameed_2021]
- [Saavedra et al 2015][research_saavedra_lavagnoli_2015]
- [Sabin 1957][research_sabin_1957]
- [Sacchi et al 2026][research_sacchi_sneddon_2026]
- [Sachan et al 2025][research_sachan_r_2025]
- [Sachs 1977][research_sachs_1977]
- [Sachs 2007][research_sachs_2007_b]
- [Sackheim et al 2005][research_throttleable_engine_2005]
- [Sadeck and Lee 2009][research_sadeck_lee_2009]
- [Sadiq Ali Mir et al 2025][research_sadiqalimir_suhanaarsh_2025]
- [Sadoff and Sisk 1950][research_x4_stall_1950]
- [Sadraey 2022][research_sadraey_2022]
- [Sadraey 2022][research_sadraey_2022_b]
- [Safronov et al 2023][research_safronov_semon_2023]
- [Saha et al 2019][research_saha_ranjan_2019]
- [Sahoo and Peetala 2010][research_sahoo_peetala_2010]
- [Sahu 1986][research_sahu_1986]
- [Sahu 2007][research_sahu_2007]
- [Sahu 2011][research_sahu_2011]
- [Saida 1986][research_saida_1986]
- [Saito et al 2006][research_saito_hayashi_2006]
- [Sakaki et al 2015][research_sakaki_kakudo_2015]
- [Sakaki et al 2016][research_sakaki_kakudo_2016]
- [Sakaki et al 2018][research_sakaki_funahashi_2018]
- [Sakata 2002][research_sakata_2002]
- [Sakata and Davis 1977][research_sakata_davis_1977]
- [Sakata et al 1975][research_sakata_davis_1975]
- [Sakaue et al 2000][research_sakaue_asai_2000]
- [Salay and Elliott 1996][research_salay_elliott_1996]
- [Salley and Kovacevich 1964][research_salley_kovacevich_1964]
- [Saltzman 1953][research_x1_liftdrag_1953]
- [Saltzman 1961][research_saltzman_1961]
- [Saltzman and Ayers 1995][research_supersonic_research_1995]
- [Sambamurthi et al 1989][research_sambamurthi_warmbrod_1989]
- [Samimy et al 1994][research_samimy_arnette_1994]
- [Samputh et al 2024][research_samputh_moey_2024]
- [Sanderson 1965][research_sanderson_1965]
- [Sanghi et al 2020][research_sanghi_riso_2020]
- [Sanghi et al 2024][research_sanghi_cesnik_2024]
- [Sano 1981][research_sano_1981]
- [Sant and Allen 2011][research_sant_allen_2011]
- [Santiago 1996][research_santiago_1996]
- [Santos and Pegado 2019][research_santos_pegado_2019]
- [Santos et al 2008][research_santos_beck_2008]
- [Sanz 1986][research_sanz_1986]
- [Saravanan et al 2021][research_saravanan_tennyson_2021]
- [Sargolzaie et al 2022][research_sargolzaie_fazeli_2022]
- [Saric 2010][research_saric_2010]
- [Sarigul-Klijn et al 2006][research_sarigulklijn_sarigulklijn_2006]
- [Sarigulklijn et al 2012][research_sarigulklijn_sarigulklijn_2012]
- [Sarma and Varadan 1988][research_sarma_varadan_1988]
- [Sarotte][research_sarotte]
- [Sasoh and Fujiwara 1990][research_sasoh_fujiwara_1990]
- [Sasson et al 2022][research_sbli_experiments_2022]
- [Sathaye et al 2004][research_sathaye_yuan_2004]
- [Sato 2022][research_sato_2022]
- [Sato et al 2001][research_sato_sawada_2001]
- [Saunders 1963][research_saunders_1963]
- [Savkovic 2008][research_savkovic_2008]
- [Savoldi et al 2025][research_savoldi_cammi_2025]
- [Sawada and Nishiwaki 1991][research_sawada_nishiwaki_1991]
- [Sawaragi 1995][research_sawaragi_1995]
- [Sawyer 1977][research_sawyer_1977]
- [Sayyed et al 2025][research_sayyed_konar_2025]
- [Sboev D 2024][research_sboevd_2024]
- [Scala 1961][research_scala_1961]
- [Scala 1962][research_scala_1962]
- [Schade and Hassell 1953][research_schade_hassell_1953]
- [Schaefer et al 2011][research_schaefer_hanson_2011]
- [Schafer 1962][research_schafer_1962]
- [Schairer 1941][research_schairer_1941]
- [Schallhorn et al 1998][research_schallhorn_majumdar_1998]
- [Scherberg and Ferguson 1952][research_scherberg_ferguson_1952]
- [Scherrer et al 1949][research_scherrer_gowen_1949]
- [Schewe and Mai 2018][research_schewe_mai_2018]
- [Schlimm 2015][research_schlimm_2015]
- [Schmalhofer and White 1966][research_schmalhoferjr_white_1966]
- [Schmidt 1988][research_schmidt_1988]
- [Schmidt 1991][research_schmidt_1991]
- [Schmidt 1992][research_schmidt_1992]
- [Schmidt and Wright 1991][research_schmidt_wright_1991]
- [Schmitt 1970][research_schmitt_1970]
- [Schmitt et al 1983][research_schmitt_destarac_1983]
- [Schneck 1978][research_schneck_1978]
- [Schnell 2023][research_schnell_2023]
- [Schnell et al 2006][research_schnell_keller_2006]
- [Schnoebelen and Yechout 2003][research_schnoebelen_yechout_2003]
- [Schoeler 1987][research_schoeler_1987]
- [Schoenenberger 2013][research_schoenenberger_2013]
- [Schoenman 1984][research_schoenman_1984]
- [Schoneman 2019][research_schoneman_2019]
- [Schreyer et al 2009][research_schreyer_gaisbauer_2009]
- [Schroeder 2012][research_schroeder_2012]
- [Schroeder 2016][research_schroeder_2016]
- [Schubert 1979][research_schubert_1979]
- [Schuelein 2008][research_schuelein_2008]
- [Schueler 1963][research_schueler_1963]
- [Schuet et al 2017][research_schuet_lombaerts_2017]
- [Schuman 2018][research_schuman_2018]
- [Schuster and Lokos 1988][research_fsw_flight_divergence_1988]
- [Schwanz 1972][research_schwanz_1972]
- [Scott 1963][research_scott_1963]
- [Scott and Weisshaar 1991][research_scott_weisshaar_1991]
- [Scott and Weisshaar 1994][research_scott_weisshaar_1994]
- [Seacord and Teitelbaum 1947][research_seacord_teitelbaum_1947]
- [Sears 1947][research_sears_1947]
- [Seaver et al 2023][research_seaver_bennett_2023]
- [Sebastian 1967][research_sebastian_1967]
- [Seckel 1964][research_seckel_1964]
- [Seckel 1964][research_seckel_1964_b]
- [Seckel 1964][research_seckel_1964_c]
- [Seckel 1964][research_seckel_1964_d]
- [Sedney 1956][research_sedney_1956]
- [Seeney et al 1968][research_seeney_bull_1968]
- [Seidman 1978][research_seidman_1978]
- [Seiner and Librescu 1983][research_seiner_librescu_1983]
- [Semionov and Kosinov 2000][research_semionov_kosinov_2000]
- [Semionov and Kosinov 2007][research_semionov_kosinov_2007]
- [Semionov et al 2006][research_semionov_kosinov_2006]
- [Semionov et al 2009][research_semionov_kosinov_2009]
- [Semionov et al 2024][research_semionov_kosinov_2024]
- [Senchev et al 2022][research_senchev_zubrilin_2022]
- [Seo et al 2018][research_seo_cho_2018]
- [Sergienko and Sergienko 1997][research_sergienko_sergienko_1997]
- [Serpieri and Kotsonis 2015][research_serpieri_kotsonis_2015]
- [Seshime et al 2026][research_seshime_haga_2026]
- [Sessions et al 1977][research_sessions_mcmahon_1977]
- [Setoguchi and Kanazaki 2020][research_setoguchi_kanazaki_2020]
- [Settles 1986][research_settles_1986]
- [Settles and Bogdonoff 1973][research_settles_bogdonoff_1973]
- [Settles et al 1975][research_settles_bogdonoff_1975]
- [Sewell and Chew 1994][research_sewell_chew_1994]
- [Sexsmith et al 2025][research_sexsmith_clay_2025]
- [Shadloo and Hadjadj 2017][research_shadloo_hadjadj_2017]
- [Shaffer and Brinkley 1974][research_shaffer_brinkley_1974]
- [Shah and Granda 1998][research_shah_granda_1998]
- [Shahab et al 2009][research_shahab_lehnasch_2009]
- [Shahinian and Achter 1963][research_shahinian_achter_1963]
- [Shamikh 2013][research_shamikh_2013]
- [Shams][research_shams]
- [Shams and Noorian 2025][research_shams_noorian_2025]
- [Shams et al 2026][research_shams_khouli_2026]
- [Shams Taleghani et al 2025][research_shamstaleghani_yektaei_2025]
- [Shan et al 2019][research_shan_tian_2019]
- [Shanbhag et al 2016][research_shanbhag_bashir_2016]
- [Shankara and Nandi 1978][research_shankara_nandi_1978]
- [Shannon 1948][research_shannon_1948]
- [Shannon 1973][research_shannon_1973]
- [Shanthakumar 1977][research_shanthakumar_1977]
- [Shantz 1953][research_shantz_1953]
- [Sharif et al 2022][research_sharif_abbas_2022]
- [Sharifzadeh et al 2014][research_sharifzadeh_hendrick_2014]
- [Sharma][research_sharma]
- [Sharma et al 2007][research_sharma_choi_2007]
- [Sharma et al 2018][research_sharma_shadloo_2018]
- [Sharma et al 2019][research_sharma_shadloo_2019]
- [Sharpe 1975][research_sharpe_1975]
- [Sharpe 1984][research_sharpe_jr_1984]
- [Sharpe and Oh 2003][research_sharpe_oh_2003]
- [Sharpes and Carroll 1973][research_roll_coupling_balance_1973]
- [Shearwood et al 2021][research_shearwood_nabawy_2021]
- [Sheldon 1967][research_sheldon_1967]
- [Shelley et al 2001][research_shelley_leclaire_2001]
- [Shen et al 2019][research_shen_huang_2019]
- [Shen et al 2019][research_shen_zhang_2019]
- [Sher et al 2022][research_sher_maqsood_2022]
- [Sherby et al 1953][research_sherby_frenkel_1953]
- [Sherby et al 1956][research_sherby_lytton_1956]
- [Shevchuk et al 2017][research_shevchuk_kravchuk_2017]
- [Shevelev and Syzranova 2009][research_shevelev_syzranova_2009]
- [Shi et al 2023][research_shi_zi_2023]
- [Shi et al 2024][research_shi_chen_2024]
- [Shi et al 2025][research_shi_guan_2025]
- [Shields and Mohseni 2012][research_shields_mohseni_2012]
- [Shields and Mohseni 2012][research_shields_mohseni_2012_b]
- [Shields and Mohseni 2013][research_shields_mohseni_2013]
- [Shifler 2013][research_shifler_2013]
- [Shih 1976][research_shih_1976]
- [Shimizu et al 2008][research_shimizu_mizobuchi_2008]
- [Shimura and Kamijo 1985][research_shimura_kamijo_1985]
- [Shinde et al 2018][research_shinde_mcnamara_2018]
- [Shinde et al 2019][research_shinde_mcnamara_2019]
- [Shingledecker et al 2007][research_shingledecker_glanton_2007]
- [Shirokov et al 2024][research_shirokov_strelets_2024]
- [Shiryaev and Serebryansky 2022][research_shiryaev_serebryansky_2022]
- [Shiryaev et al 2023][research_shiryaev_maysak_2023]
- [Shishaeva and Vedeneev 2013][research_shishaeva_vedeneev_2013]
- [Shivaji et al 2025][research_shivaji_basavaraju_2025]
- [Shock Wave-Boundary Layer Interactions][research_shock_wave_boundary]
- [Shoyama et al 2024][research_shoyama_wada_2024]
- [Shrivastava and Stengel 1989][research_shrivastava_stengel_1989]
- [Shu et al 2023][research_shu_baik_2023]
- [Shuttle Eleven Cove Aerodynamic 1978][research_shuttle_eleven_1978]
- [Shweyk et al 2012][research_shweyk_hyde_2012]
- [Shyprykevich and Sawyer 1973][research_shyprykevich_sawyer_1973]
- [Siag and Kumar 2026][research_siag_kumar_2026]
- [Sibanda 2023][research_sibanda_2023]
- [Sibulkin 1954][research_sibulkin_1954]
- [Sibulkin 1956][research_sibulkin_1956]
- [Sibulkin 1958][research_sibulkin_1958]
- [Siclari 1990][research_siclari_1990]
- [Siclari 1992][research_siclari_1992]
- [Sidhu 2023][research_sidhu_2023]
- [Siebenhaar and Campbell 1987][research_siebenhaar_campbell_1987]
- [Siegel et al 2024][research_siegel_ofarrell_2024]
- [Sigal 1987][research_sigal_1987]
- [Silton 2003][research_silton_2003]
- [Silton et al 2017][research_silton_youn_2017]
- [Silva][research_silva]
- [Silva][research_silva_b]
- [Silva-Freire 1988][research_silvafreire_1988]
- [Silvestre and Paglione 2008][research_silvestre_paglione_2008]
- [Sim and Curry 1985][research_sim_curry_1985]
- [Simmers and Coney 1979][research_simmers_coney_1979]
- [Simmons and Cross 1954][research_simmons_cross_1954]
- [Simonson 1975][research_simonson_1975]
- [Simonson 1988][research_simonson_1988]
- [Sims 1963][research_sims_1963]
- [Simsek et al 2016][research_simsek_kuran_2016]
- [Sinay and Reiss 1981][research_sinay_reiss_1981]
- [Singer 1964][research_singer_1964]
- [Singh and Chowdhury 2021][research_singh_chowdhury_2021]
- [Singh and Jategaonkar 1996][research_singh_jategaonkar_1996]
- [Singh and Molki 2024][research_singh_molki_2024]
- [Sinha and Ananthkrishnan 2002][research_sinha_ananthkrishnan_2002]
- [Sinha and Ananthkrishnan 2017][research_sinha_ananthkrishnan_2017]
- [Sircar et al 1988][research_sircar_ribaudo_1988]
- [Sirignano and Popov 2013][research_sirignano_popov_2013]
- [Sivan 1971][research_sivan_1971]
- [Sivasegaram and Whitelaw 1971][research_sivasegaram_whitelaw_1971]
- [Sivykh and Zaulichny 1978][research_sivykh_zaulichny_1978]
- [Skolnik and Putnam 2022][research_skolnik_putnam_2022]
- [Sleeman 1957][research_sleeman_1957]
- [Sleight et al 2008][research_sleight_paddock_2008]
- [Smaili et al 2017][research_smaili_breeman_2017]
- [Smart et al 1994][research_smart_kalkhoran_1994]
- [Smith 1953][research_smith_1953]
- [Smith 1961][research_smith_1961]
- [Smith 1964][research_smith_1964]
- [Smith 1967][research_smith_1967]
- [Smith 1969][research_smith_1969]
- [Smith 1973][research_smith_1973]
- [Smith 1975][research_smith_1975]
- [Smith 1982][research_smith_1982]
- [Smith and Smits 1988][research_smith_smits_1988]
- [Smith and Smits 1992][research_smith_smits_1992]
- [Smith and Smits 1993][research_smith_smits_1993]
- [Smith et al 2025][research_smith_ramachandran_2025]
- [Smitha et al 2021][research_smitha_joy_2021]
- [Smits 1984][research_smits_1984]
- [Smits 1985][research_smits_1985]
- [Smits 1988][research_smits_1988]
- [Smollett 1955][research_smollett_1955]
- [Snell 1993][research_snell_1993]
- [Snell et al 1991][research_snell_garrardjr_1991]
- [Snodgrass 1955][research_snodgrass_1955]
- [Snyder and Kehoe 1991][research_heated_plate_modes_1991]
- [Snyder and Memory 2005][research_snyder_memory_2005]
- [Snyder and Weisshaar 2013][research_snyder_weisshaar_2013]
- [So 1994][research_so_1994]
- [So 2020][research_so_2020]
- [Solid Rocket Combustion Instability-An 1992][research_solid_rocket_1992]
- [Solies 1995][research_solies_1995]
- [Som 2021][research_som_2021]
- [Somanath et al 2021][research_somanath_unnikrishnannair_2021]
- [Sommer and Short 1955][research_sommer_short_1955]
- [Son et al 2012][research_son_koo_2012]
- [Song et al 1992][research_song_librescu_1992]
- [Song et al 2014][research_song_yang_2014]
- [Sonneveldt et al 2019][research_sonneveldt_clark_2019]
- [Sotomayer and Weeks 1978][research_sotomayer_weeks_1978]
- [Sotoudeh 2015][research_sotoudeh_2015]
- [Soudakov et al 2009][research_soudakov_egorov_2009]
- [Souverein et al 2019][research_souverein_maeding_2019]
- [Spaceflight crew escape system 2004][research_spaceflight_crew_2004]
- [Spacht 1980][research_spacht_1980]
- [Spaid 1972][research_spaid_1972]
- [Spaid and Frishett 1972][research_spaid_frishett_1972]
- [Sparkes 2024][research_sparkes_2024]
- [Sparks and Moerder 2002][research_sparks_moerder_2002]
- [Sparks et al 1994][research_sparks_buffington_1994]
- [Spearman 1979][research_spearman_1979]
- [Spearman 1980][research_spearman_1980]
- [Spearman and Driver 1959][research_forebody_deflection_1959]
- [Spearman et al 1956][research_spearman_robinson_1956]
- [Special Features of Antiaircraft 2010][research_special_features_2010]
- [Specker 2002][research_specker_2002]
- [Specker and Brinkley 1983][research_specker_brinkley_1983]
- [Speegle 1958][research_speegle_1958]
- [Speelman 1975][research_speelmaniii_1975]
- [Speelman 1977][research_speelman_1977]
- [Speziale and Sarkar 1991][research_speziale_sarkar_1991]
- [Spinal injuries in the 1980][research_spinal_injuries_1980]
- [Spiridakos et al 2020][research_pspiridakos_cmarkatos_2020]
- [Spivey 2009][research_spivey_2009]
- [Spivey 2010][research_spivey_2010]
- [Spivey 2011][research_spivey_2011]
- [Spooner and Foley][research_spooner_foley]
- [Spreemann and Few 1954][research_prelim_static_1954]
- [Spring 1972][research_spring_1972]
- [Sprinks 1963][research_sprinks_1963]
- [Spyropoulos and Blaisdell 1998][research_spyropoulos_blaisdell_1998]
- [Squires 2004][research_squires_2004]
- [Sreenatha and Kulkarni][research_sreenatha_kulkarni]
- [Sreenivasulu et al 2021][research_sreenivasulu_2021]
- [Srivastava 2009][research_srivastava_2009]
- [Stability Testing Methodology Scaling 1995][research_stability_testing_1995]
- [Stalder et al 1950][research_stalder_rubesin_1950]
- [Stallings 1982][research_stallingsjr_1982]
- [Stallings and Hartman 1981][research_stallings_hartman_1981]
- [Stalnaker 2004][research_stalnaker_2004]
- [Stanford 2016][research_stanford_2016]
- [Stanford 2022][research_stanford_2022]
- [Stanford 2023][research_stanford_2023]
- [Stanford and Beran 2011][research_stanford_beran_2011]
- [Stanišić 1962][research_stanisic_1962]
- [Static Aeroelasticity Effect 2014][research_static_aeroelasticity_2014]
- [Static Longitudinal Stability Flight 2003][research_static_longitudinal_2003]
- [Static Stability and Control][research_static_stability]
- [Stech 1977][research_stech_1977]
- [Steimle et al 2008][research_steimle_schroder_2008]
- [Steinberg et al 1972][research_steinberg_uselton_1972]
- [Stenfelt and Ringertz 2009][research_stenfelt_ringertz_2009]
- [Stengel 1969][research_stengel_1969]
- [Stengel 1970][research_stengel_1970]
- [Stengel 1980][research_stengel_1980]
- [Stengel and Miller 1978][research_stengel_miller_1978]
- [Stepanova and Prokhorova 2016][research_stepanova_prokhorova_2016]
- [Stephens 1959][research_rocket_model_heating_1959]
- [Stephens 1991][research_stephens_1991]
- [Stephenson 1966][research_stephenson_1966]
- [Steppert and Epple 2017][research_steppert_epple_2017]
- [Stewart 1946][research_stewart_1946]
- [Stewart 1956][research_stewart_1956]
- [Stewart 1958][research_stewart_1958]
- [Stewart and Rowe 1962][research_stewart_rowe_1962]
- [Stewartson 1950][research_stewartson_1950]
- [Stewartson 1950][research_stewartson_1950_b]
- [Stewartson 1952][research_stewartson_1952]
- [Stillwell and Larson 1960][research_stillwell_larson_1960]
- [Stillwell and Larson 1960][research_stillwell_larson_1960_b]
- [Stine and Scherrer 1952][research_stine_scherrer_1952]
- [Stock 1975][research_stock_1975]
- [Stockbridge 1988][research_stockbridge_1988]
- [Stoldt et al 2020][research_stoldt_johansen_2020]
- [Stoltzfus and Benz 1986][research_turbopump_ignition_1986]
- [Stone 1945][research_stone_1945]
- [Stone 1957][research_stone_1957]
- [Stoop and Shahinian 1966][research_stoop_shahinian_1966]
- [Stough et al 1991][research_stoughiii_whipple_1991]
- [Streb 1973][research_streb_1973]
- [Strietzel and Shefler 1963][research_strietzel_shefler_1963]
- [Striz 1991][research_striz_1991]
- [Strome 1969][research_strome_1969]
- [Strouhal and Curry 1966][research_strouhal_curry_1966]
- [Stubblefield et al 2025][research_stubblefield_kunz_2025]
- [Stuber et al 2012][research_stuber_prasadh_2012]
- [Study of thermocouple transient 2019][research_study_of_thermocouple_2019]
- [Study on Critical Parachute 2024][research_study_on_2024]
- [Stulov and Shapiro 1969][research_stulov_shapiro_1969]
- [Sturek 1973][research_sturek_1973]
- [Sturek and Mylin 1981][research_sturek_mylin_1981]
- [Sturek and Schiff 1981][research_sturek_schiff_1981]
- [Sturek et al 1983][research_sturek_kayser_1983]
- [Sturek et al 1983][research_sturek_kayser_1983_b]
- [Su et al 1992][research_su_gilbert_1992]
- [Su et al 2013][research_su_eri_2013]
- [Su et al 2018][research_su_wang_2018]
- [Su et al 2021][research_su_hwu_2021]
- [Su et al 2024][research_su_long_2024]
- [Suarez et al 1992][research_suarez_kramer_1992]
- [Subash et al 2024][research_s_babup_2024]
- [Sucec 2020][research_sucec_2020]
- [Suchov et al 2022][research_suchov_kazmerchukh_2022]
- [Sugamata et al 2006][research_sugamata_genei_2006]
- [Sugiura and Ushijima 2024][research_sugiura_ushijima_2024]
- [Suleman 2007][research_suleman_2007]
- [Suleman and Venkayya 1994][research_suleman_venkayya_1994]
- [Suleman and Venkayya 1996][research_suleman_venkayya_1996]
- [Suleman et al 2000][research_suleman_crawford_2000]
- [Suleman et al 2002][research_suleman_crawford_2002]
- [Summerfield 1951][research_summerfield_1951]
- [Summerfield 1960][research_summerfield_1960]
- [Summers et al 2006][research_summers_burkholder_2006]
- [Sun 2024][research_sun_2024]
- [Sun and Childs 1975][research_sun_childs_1975]
- [Sun and Childs 1976][research_sun_childs_1976]
- [Sun and Hu 2005][research_sun_hu_2005]
- [Sun et al 2017][research_sun_hu_2017]
- [Sun et al 2020][research_sun_yang_2020]
- [Sun et al 2023][research_sun_miao_2023]
- [Sun et al 2024][research_sun_zhou_2024]
- [Sun et al 2025][research_sun_miao_2025]
- [Sunakawa and Uemura 1961][research_sunakawa_uemura_1961]
- [Sundberg 1975][research_sundberg_1975]
- [Sundén and Fu 2017][research_sunden_fu_2017]
- [Supersonic Aircraft High-Speed Civil 1997][research_supersonic_aircraft_1997]
- [Supersonic Flight 2025][research_supersonic_flight_2025]
- [Supersonic Flows Over Wings 2021][research_supersonic_flows_2021]
- [Supersonic Flows Over Wings 2025][research_supersonic_flows_2025]
- [Supersonic Three-dimensional Wing Theory 1960][research_supersonic_three_dimensional_1960]
- [Supersonic transport wing minimum 1992][research_supersonic_transport_1992]
- [Surianarayanan et al 1989][research_surianarayanan_iyer_1989]
- [Suryanarayana et al 2022][research_suryanarayana_singh_2022]
- [Susanto et al 2021][research_susanto_bayusetiawan_2021]
- [Sutera and Williams 1968][research_sutera_williams_1968]
- [Sutherland 1893][research_sutherland_1893]
- [Sutton 1968][research_sutton_1968]
- [Sutton 1970][research_sutton_1970]
- [Sutton and Graves 1971][research_sutton_graves_1971]
- [Sutton et al 1995][research_sutton_troiler_1995]
- [Sutton et al 1997][research_sutton_chao_1997]
- [Swaim 1970][research_swaim_1970]
- [Swaim and Connor 1968][research_swaim_connor_1968]
- [Swanson 1958][research_swanson_1958]
- [Swarnkar and Kothari 2016][research_swarnkar_kothari_2016]
- [Swindeman 1970][research_swindeman_1970]
- [Syed et al 2022][research_syed_moshtaghzadeh_2022]
- [Szema and Shankar 1984][research_szema_shankar_1984]
- [Sznajder 2025][research_sznajder_2025]
- [Sánchez et al 2024][research_sanchez_cajas_2024]
- [Tadi 2002][research_tadi_2002]
- [Tadios 1991][research_tadios_1991]
- [Taguchi et al 2015][research_taguchi_semba_2015]
- [Taguchi et al 2021][research_taguchi_mori_2021]
- [Taira 1964][research_taira_1964]
- [Taira and Ohnami 1962][research_taira_ohnami_1962]
- [Takabayashi and Kitamura 2019][research_takabayashi_kitamura_2019]
- [Takabayashi et al 2019][research_takabayashi_fukumoto_2019]
- [Takada et al 2009][research_takada_kikuchi_2009]
- [Takahashi et al 2013][research_takahashi_yamada_2013]
- [Takahashi et al 2015][research_takahashi_yamada_2015]
- [Takahashi et al 2018][research_takahashi_munakata_2018]
- [Takahashi et al 2023][research_takahashi_griffin_2023]
- [Takahashi et al 2024][research_takahashi_griffin_2024]
- [Takahashi et al 2026][research_takahashi_2026_airdata]
- [Takeda 1970][research_takeda_1970]
- [Takegawa and Furuichi 2022][research_takegawa_furuichi_2022]
- [Takovitskii 2023][research_takovitskii_2023]
- [Tallman 1965][research_tallman_1965]
- [Tamayo][research_tamayo]
- [Tamura and Yumitori 2024][research_tamura_yumitori_2024]
- [Tan and Wang 2024][research_tan_wang_2024]
- [Tanaka 1994][research_tanaka_1994]
- [Tang 2019][research_tang_2019]
- [Tang and Qian 2016][research_tang_qian_2016]
- [Tang et al 2021][research_tang_wang_2021]
- [Tani et al 2010][research_tani_shimiya_2010]
- [Tanner et al 2015][research_ldsd_ballute_2015]
- [Tao et al 2006][research_tao_jiping_2006]
- [Tashakkor et al 2011][research_tashakkor_canabal_2011]
- [Tatar and Masdari 2019][research_tatar_masdari_2019]
- [Tauby 1979][research_tauby_1979]
- [Taylor and Gursul 2004][research_taylor_gursul_2004]
- [Taylor and Jackson 1980][research_thermostructural_hypersonic_1980]
- [Taylor and Yoo 2011][research_taylor_yoo_2011]
- [Taylor et al 1987][research_taylor_guttmann_1987]
- [Technical applications for an 1976][research_technical_applications_1976]
- [Techniques for Hot Structures 1992][research_techniques_for_1992]
- [Temgoua Dongmo and Kwatny][research_temgouadongmo_kwatny]
- [Tenney 1974][research_tenney_1974]
- [Teper and Stapleford 1965][research_teper_stapleford_1965]
- [Teper and Stapleford 1966][research_teper_stapleford_1966]
- [Terai 1968][research_terai_1968]
- [Teramoto et al 2017][research_teramoto_sanada_2017]
- [Tharion et al 2025][research_tharion_yang_2025]
- [The advanced stabilised ejection 1974][research_the_advanced_1974]
- [The analysis of thermocouple 2018][research_the_analysis_of_2018]
- [The Bell X-22A V/STOL 1990][research_the_bell_1990]
- [The Challenges of High-speed 2020][research_the_challenges_2020]
- [The design and development 1966][research_the_design_1966]
- [The Stability and Control 1968][research_the_stability_1968]
- [The Transformation of Aerodynamic 2007][research_the_transformation_2007]
- [Theodorsen 1979][research_theodorsen_1935]
- [Theoretical studies to refine 1970][research_ii_1970]
- [Thermal performance evaluation of 1972][research_thermal_performance_1972]
- [Thermal Protection System Conception 2013][research_thermal_protection_2013]
- [Thermal Structures and Materials 1992][research_thermal_structures_1992]
- [Thibert and Arnal 2000][research_thibert_arnal_2000]
- [Thomas 1942][research_thomas_1942]
- [Thomas and Fan 1971][research_thomas_fan_1971]
- [Thomas and Miller 1979][research_thomas_miller_1979]
- [Thomas et al 2005][research_thomas_bajpai_2005]
- [Thompson et al 1950][research_airspeed_calibration_1950]
- [Thompson et al 2004][research_thompson_klyde_2004]
- [Thomson 1946][research_thomson_1946]
- [Thornton and Dechaumphai 1987][research_thornton_dechaumphai_1987]
- [Thornton and Dechaumphai 1987][research_thornton_dechaumphai_1987_b]
- [Thornton and Dechaumphai 1988][research_thornton_dechaumphai_1988]
- [Three-dimensional boundary-layer transition on 1994][research_three_dimensional_boundary_layer_1994]
- [Tian and Chen 2012][research_tian_chen_2012]
- [Tian et al 2016][research_tian_yang_2016]
- [Tian et al 2023][research_tian_zhang_2023]
- [Tian et al 2026][research_tian_pan_2026]
- [Tibbits and Ivanov 2015][research_tibbits_ivanov_2015]
- [Tile-Gap Flow in the 1983][research_tile_gap_flow_1983]
- [Tilmann 1998][research_tilmann_1998]
- [Ting et al 2014][research_ting_lebofsky_2014]
- [Ting et al 2014][research_ting_nguyen_2014]
- [Ting et al 2025][research_ting_wiersema_2025]
- [Tinger 1987][research_tinger_1987]
- [Tirpak 1985][research_tirpak_1985]
- [Titov et al 2010][research_titov_leontiev_2010]
- [Tizzi 1994][research_tizzi_1994]
- [Tobak and Schiff 1974][research_tobak_schiff_1974]
- [Tobak and Schiff 1975][research_tobak_schiff_1975]
- [Tobak and Schiff 1975][research_tobak_schiff_1975_b]
- [Tobey and Bastress 1966][research_tobey_bastress_1966]
- [Token 1974][research_token_1974]
- [Tokuda and Yang 1966][research_tokuda_yang_1966]
- [Tokuda and Yang 2019][research_tokuda_yang_2019]
- [Tokugawa and Yoshida 2006][research_tokugawa_yoshida_2006]
- [Tokugawa et al 2026][research_tokugawa_ishida_2026]
- [Tomczyk 2001][research_tomczyk_2001]
- [Tong 1965][research_tong_1965]
- [Tong and Giedt 1963][research_tong_giedt_1963]
- [Tong et al 2023][research_tong_zhou_2023]
- [Tong et al 2024][research_tong_ji_2024]
- [Toni 1968][research_toni_1968]
- [Toong 1978][research_toong_1978]
- [Torres Zanardi et al 2019][research_torreszanardi_bacchi_2019]
- [Torrigiani and Berci 2021][research_torrigiani_berci_2021]
- [Totemeier 2007][research_totemeier_2007]
- [Tourbier and Fasel 1994][research_tourbier_fasel_1994]
- [Tournes and Landrum][research_tournes_landrum]
- [Traci and Wilcox 1974][research_traci_wilcox_1974]
- [Traci and Wilcox 1975][research_traci_wilcox_1975]
- [Triplett 1980][research_triplett_1980]
- [Trussell and Thomson 1960][research_trussell_thomson_1960]
- [Tsuji et al 1994][research_tsuji_tanabe_1994]
- [Tsushima et al 2019][research_tsushima_yokozeki_2019]
- [Tu et al 2024][research_tu_yan_2024]
- [Tucker and Maslen 1951][research_tucker_maslen_1951]
- [Tucker et al 1993][research_tucker_dehoff_1993]
- [Tuling et al 2013][research_tuling_dala_2013]
- [Turbulent External Boundary Layers 2023][research_turbulent_external_2023]
- [Turbulent SPOT in the 2024][research_turbulent_spot_in_2024]
- [Tushavina 2022][research_tushavina_2022]
- [Twardy 1975][research_twardy_1975]
- [Tyurenkova et al 2024][research_tyurenkova_smirnova_2024]
- [U.S. Supersonic Commercial Aircraft 1997][research_u_s_supersonic_1997]
- [Udrescu 1998][research_udrescu_1998]
- [Uemura et al 2020][research_uemura_kamata_2020]
- [Ueno et al 1998][research_ueno_matsuno_1998]
- [Uludag and Turan 2015][research_uludag_turan_2015]
- [Umeoka et al 2021][research_umeoka_mishina_2021]
- [Urbano et al 2016][research_urbano_selle_2016]
- [Urbin et al 1999][research_urbin_knight_1999]
- [Uribe Quintero et al 2024][research_uribequintero_takahashi_2024]
- [Urnes and Nielsen 2010][research_urnes_nielsen_2010]
- [Urnes and Smith 2011][research_urnes_smith_2011]
- [Urnes et al 1990][research_urnes_stewart_1990]
- [Uselton et al 1975][research_uselton_freemanjr_1975]
- [Ustinov 2013][research_ustinov_2013]
- [Vadera 2019][research_vadera_2019]
- [Valentine et al 2004][research_valentine_meyer_2004]
- [Van Dam 1986][research_vandam_1986]
- [Van Driest and Blumer 1961][research_vandriest_blumer_1961]
- [Van Echo 1964][research_vanecho_1964]
- [Van Hooser et al 1999][research_vanhooser_bailey_1999]
- [Van Norman et al 2015][research_ldsd_dynamics_2015]
- [van Oudheusden 2004][research_vanoudheusden_2004]
- [Van Thullenar 1957][research_vanthullenar_1957]
- [Vancrayenest et al 2005][research_vancrayenest_tran_2005]
- [vanDam et al 1995][research_vandam_los_1995]
- [Vandromme and Zeman 1992][research_vandromme_zeman_1992]
- [Vanfossen and Simoneau 1994][research_vanfossen_simoneau_1994]
- [Vanfossen et al 1994][research_vanfossen_simoneau_1994_b]
- [Varello et al 2013][research_varello_lamberti_2013]
- [Varlese et al 2013][research_varlese_tului_2013]
- [Varvanifarahani 2004][research_varvanifarahani_2004]
- [Vasantha and Nath 1986][research_vasantha_nath_1986]
- [Vasilevsky 2022][research_vasilevsky_2022]
- [Vasudev et al 2019][research_vasudev_thakur_2019]
- [Vasudevan and Leonard 2002][research_vasudevan_leonard_2002]
- [Vaughn 1982][research_vaughnjr_1982]
- [Vector Quality Assessment of 2017][research_vector_quality_2017]
- [Vedeneev 2012][research_vedeneev_2012]
- [Vedeneev 2013][research_vedeneev_2013]
- [Velden 1997][research_velden_1997]
- [Veley et al 2008][research_veley_khot_2008]
- [Velger and Shinar 1983][research_velger_shinar_1983]
- [Venema et al 2011][research_venema_vonterzi_2011]
- [Venkateswara Rao][research_d]
- [Venkateswaran et al 1991][research_venkateswaran_grenda_1991]
- [Ventrice et al 1979][research_ventrice_fang_1979]
- [Ventrice et al 1979][research_ventrice_fang_1979_b]
- [Vepa 2023][research_vepa_2023]
- [Veresnikov and Goncharenko 2025][research_veresnikov_goncharenko_2025]
- [Verma and Hadjadj 2015][research_verma_hadjadj_2015]
- [Vernacchia et al 2022][research_vernacchia_2022]
- [Vescovini and Dozio 2018][research_vescovini_dozio_2018]
- [Vigdorovich 2015][research_vigdorovich_2015]
- [Vigdorovich 2017][research_vigdorovich_2017]
- [Vigdorovich 2023][research_vigdorovich_2023]
- [Vigdorovich 2023][research_vigdorovich_2023_b]
- [Vigdorovich 2024][research_vigdorovich_2024]
- [Vigdorovich 2025][research_vigdorovich_2025]
- [Vijgen et al 1992][research_vijgen_hardin_1992]
- [Vincent and Botez 2015][research_vincent_botez_2015]
- [Vindigni 2023][research_vindigni_2023]
- [Vindigni 2024][research_vindigni_2024]
- [Vindigni et al 2024][research_vindigni_mantegna_2024]
- [Vinokur 1970][research_vinokur_1970]
- [Visbal 2012][research_visbal_2012]
- [Visbal 2017][research_visbal_2017]
- [Visbal and Garmann 2012][research_visbal_garmann_2012]
- [Vishwanathan][research_vishwanathan]
- [Visuttipitukul, et al 2009][research_visuttipitukul_chansaksoong_2009]
- [Viviani et al 2021][research_viviani_aprovitola_2021]
- [Vlahopoulos and He 2009][research_vlahopoulos_he_2009]
- [Voisinet and Lee 1972][research_voisinet_lee_1972]
- [Vomaske et al 1961][research_vomaske_sadoff_1961]
- [von Terzi et al 2009][research_vonterzi_mayer_2009]
- [von Willingh and Knutsen 2022][research_vonwillingh_knutsen_2022]
- [Voronkin 1971][research_voronkin_1971]
- [Voss et al 2026][research_voss_tang_2026]
- [Vranas 1976][research_vranas_1976]
- [Wadley et al 2005][research_wadley_hopper_2005]
- [Waesche and Summerfield 1965][research_waesche_summerfield_1965]
- [Wagdi 1979][research_wagdi_1979]
- [Wagner][research_wagner]
- [Waindim et al 2014][research_waindim_gaitonde_2014]
- [Wainwright 1962][research_wainwright_1962]
- [Walker][research_walker]
- [Walker 1973][research_walker_1973]
- [Wallace 1952][research_wallace_1952]
- [Walsh and Jacoby 1972][research_walsh_jacoby_1972]
- [Walter and Redman 1954][research_walter_redman_1954]
- [Waltrup and Schetz 1972][research_waltrup_schetz_1972]
- [Waltrup and Schetz 1973][research_waltrup_schetz_1973]
- [Wan et al 2011][research_wan_zhang_2011]
- [Wang 1993][research_wang_1993]
- [Wang 1999][research_wang_1999]
- [Wang 2011][research_wang_2011]
- [Wang 2019][research_wang_2019]
- [Wang 2019][research_wang_2019_b]
- [Wang 2024][research_wang_2024]
- [Wang and Bidek 1994][research_wang_bidek_1994]
- [Wang and Ma 2024][research_wang_ma_2024]
- [Wang and Wang 2016][research_wang_wang_2016]
- [Wang et al 1991][research_wang_hingst_1991]
- [Wang et al 1992][research_wang_lou_1992]
- [Wang et al 1994][research_wang_herbert_1994]
- [Wang et al 2000][research_wang_zhou_2000]
- [Wang et al 2010][research_wang_mykhaylonka_2010]
- [Wang et al 2013][research_wang_li_2013]
- [Wang et al 2014][research_wang_han_2014]
- [Wang et al 2014][research_wang_tian_2014]
- [Wang et al 2016][research_wang_liu_2016]
- [Wang et al 2016][research_wang_vojtek_2016]
- [Wang et al 2016][research_wang_wang_2016_b]
- [Wang et al 2017][research_wang_yang_2017]
- [Wang et al 2018][research_wang_han_2018]
- [Wang et al 2018][research_wang_hawkins_2018]
- [Wang et al 2018][research_wang_su_2018]
- [Wang et al 2018][research_wang_wu_2018]
- [Wang et al 2020][research_wang_ji_2020]
- [Wang et al 2020][research_wang_liu_2020]
- [Wang et al 2020][research_wang_xie_2020]
- [Wang et al 2021][research_wang_tang_2021]
- [Wang et al 2021][research_wang_tang_2021_b]
- [Wang et al 2021][research_wang_wu_2021]
- [Wang et al 2021][research_wang_zhou_2021]
- [Wang et al 2022][research_wang_li_2022]
- [Wang et al 2022][research_wang_li_2022_b]
- [Wang et al 2022][research_wang_li_2022_c]
- [Wang et al 2022][research_wang_zhao_2022]
- [Wang et al 2024][research_wang_zhao_creep_2024]
- [Wang et al 2025][research_wang_kim_2025]
- [Wang et al 2025][research_wang_leary_2025]
- [Wang et al 2025][research_wang_tu_2025]
- [Wang et al 2025][research_wang_zong_2025]
- [Wang et al 2026][research_wang_li_2026]
- [Wansaseub et al 2020][research_wansaseub_sleesongsom_2020]
- [Ward and Blackburn 1976][research_ward_blackburn_1976]
- [Ward and Blackburn 1976][research_ward_blackburn_1976_b]
- [Ward and Myers 1967][research_ward_myers_1967]
- [Ware et al 1988][research_ware_spencerjr_1988]
- [Warren et al 1997][research_warren_hassan_1997]
- [Washington and Humphrey 1969][research_washington_humphrey_1969]
- [Waskiewicz et al 1981][research_waskiewicz_dejongh_1981]
- [Wasserman 1952][research_wasserman_1952]
- [Watkins 1986][research_watkins_1986]
- [Watmuff and Smits 1987][research_watmuff_smits_1987]
- [Watson 1975][research_watson_1975]
- [Watts 1976][research_watts_1976]
- [Watts et al 1947][research_watts_mendelson_1947]
- [Weatherill and Zartarian 1958][research_weatherill_zartarian_1958]
- [Webb 1971][research_webb_1971]
- [Webber and Houghton 1963][research_webber_houghton_1963]
- [Wegener 1977][research_wegener_1977]
- [Wei et al 2024][research_wei_xin_2024]
- [Wei et al 2024][research_wei_zhang_2024]
- [Weinacht 1998][research_weinacht_1998]
- [Weinacht 2014][research_weinacht_2014]
- [Weingarten and Chalk 1982][research_weingarten_chalk_1982]
- [Weiss et al 2022][research_weiss_staudacher_2022]
- [Weisshaar 1977][research_weisshaar_1977]
- [Weisshaar 1978][research_weisshaar_1978]
- [Weisshaar 1979][research_weisshaar_1979]
- [Weisshaar 1980][research_weisshaar_1980]
- [Weisshaar 1981][research_weisshaar_1981]
- [Weisshaar 1985][research_weisshaar_1985]
- [Weisshaar 1990][research_weisshaar_1990]
- [Weisshaar and Crittenden 1976][research_asymmetric_sweep_flutter_1976]
- [Weisshaar and Ryan 1986][research_weisshaar_ryan_1986]
- [Weisshaar and Zeiler 1982][research_flexible_fsw_dynamics_1982]
- [Weissman 1972][research_weissman_1972]
- [Weissman 1973][research_weissman_1973]
- [Weissman 1975][research_weissman_1975]
- [Welded 18 Cr, 8 1958][research_welded_18_1958]
- [Welded Inconel W and 1958][research_welded_inconel_1958]
- [Welge et al 1976][research_welge_radkey_1976]
- [Wells 1989][research_wells_1989]
- [Wells and McBride 1967][research_wells_mcbride_1967]
- [Wells and Urnes 1994][research_wells_urnes_1994]
- [Welsh et al 1970][research_welsh_winchenbach_1970]
- [Wen et al 2013][research_wen_deng_2013]
- [Wen et al 2014][research_wen_wu_2014]
- [Wendt 1948][research_wendt_1948]
- [Wentz and Nyenhuis 1984][research_wentzjr_nyenhuis_1984]
- [Wernet et al 2009][research_wernet_locke_2009]
- [West and Brandis 2018][research_west_brandis_2018]
- [West et al 1980][research_west_ummel_1980]
- [Westin and de Freitas Pinto 2008][research_westin_defreitaspinto_2008]
- [Westphal et al 2006][research_westphal_bleazard_2006]
- [Wetzel 1954][research_fighter_sweep_model_1954]
- [Whitcomb 1956][research_whitcomb_1952]
- [White 1974][research_white_1974]
- [Whitehead 1991][research_whiteheadjr_1991]
- [Whitmore et al 2015][research_whitmore_merkley_2015]
- [Whitnah 1967][research_whitnah_1967]
- [Whitten et al 1970][research_whitten_moffat_1970]
- [Wiedemann et al 1986][research_wiedemann_clark_1986]
- [Wilborn and Foster 2004][research_wilborn_foster_2004]
- [Wilcox 1991][research_wilcoxjr_1991]
- [Wilhelm and Schafranek 1986][research_wilhelm_schafranek_1986]
- [Wilks 2006][research_wilks_2006]
- [Willems 1987][research_willems_1987]
- [Williams 1965][research_williams_1965]
- [Williams 1991][research_williams_1991]
- [Williams 2004][research_williams_2004]
- [Williams 2004][research_williams_2004_b]
- [Williams and Hunt 1980][research_williams_hunt_1980]
- [Williams et al 2025][research_williams_niestroy_2025]
- [Wilson 1950][research_wilson_1950]
- [Wilson 1971][research_wilson_1971]
- [Wilson 1973][research_wilson_1973]
- [Wilson 1978][research_wilson_1978]
- [Wilson and Egger 1975][research_wilson_egger_1975]
- [Wilson and Maurer 1971][research_wilson_maurer_1971]
- [Wilson et al 1973][research_wilson_cazier_1973]
- [Wimpress 1966][research_wimpress_1966]
- [Wimpress and Swihart 1964][research_wimpress_swihart_1964]
- [Wing Theory in Supersonic 1969][research_wing_theory_1969]
- [Wing tunnel model for 1998][research_wing_tunnel_1998]
- [Winkler 1954][research_winkler_1954]
- [Winograd and Miles 1956][research_winograd_miles_1956]
- [Winovich 1968][research_winovich_1968]
- [Wiswell et al 1961][research_wiswell_olekszyk_1961]
- [Wnuk et al 1990][research_wnuk_wnuk_1990]
- [Wolf 1999][research_wolf_1999]
- [Wolf 2002][research_wolf_2002]
- [Wolf 2019][research_wolf_2019]
- [Wolf and Bossert 2001][research_wolf_bossert_2001]
- [Wolf and Fallon 2011][research_wolf_fallon_2011]
- [Wolf and Ivanov 2008][research_wolf_ivanov_2008]
- [Wolfe 1964][research_wolfe_1964]
- [Wolkovitch 1984][research_wolkovitch_1984]
- [Wolowicz and Yancey 1973][research_xb70_stability_1973]
- [Wong and Mastroianni 1999][research_wong_mastroianni_1999]
- [Woo 1992][research_woo_1992]
- [Wood and Bauer 1988][research_wood_bauer_1988]
- [Wood and Covell 1987][research_wood_covell_1987]
- [Wood and Miller 1984][research_wood_miller_1984]
- [Woodiga et al 2015][research_woodiga_liu_2015]
- [Woods et al 1989][research_woods_gilbert_1989]
- [Woods et al 1990][research_woods_gilbert_1990]
- [Woodward 1956][research_woodward_1956]
- [Woodward 1968][research_woodward_1968]
- [Woodworth et al 2023][research_woodworth_salazar_2023]
- [Wooldridge 1960][research_wooldridge_1960]
- [Woronowicz and Baganoff 1991][research_woronowicz_baganoff_1991]
- [Wortman 1970][research_wortman_1970]
- [Wortman 1971][research_wortman_1971]
- [Wright 1936][research_wright_1936]
- [Wright 1988][research_wright_1988]
- [Wright and Zoby 1971][research_wright_zoby_1971]
- [Wright and Zoby 1977][research_wright_zoby_1977]
- [Wu and Martin 2007][research_wu_martin_2007]
- [Wu and Moin 2010][research_wu_moin_2010]
- [Wu and Radespiel 2017][research_wu_radespiel_2017]
- [Wu et al 2013][research_wu_wu_2013]
- [Wu et al 2014][research_wu_wu_2014]
- [Wu et al 2018][research_wu_lv_2018]
- [Wu et al 2019][research_wu_liang_2019]
- [Wu et al 2020][research_wu_li_2020]
- [Wu et al 2021][research_wu_zhao_2021]
- [Wunderlich and Dähne 2017][research_wunderlich_dahne_2017]
- [Wunderlich et al 2017][research_wunderlich_dahne_2017_b]
- [Wurster 1981][research_wurster_1981]
- [Wykes 1957][research_wykes_1957]
- [Wykes 1968][research_wykes_1968]
- [Xi and Liu 2011][research_xi_liu_2011]
- [Xi et al 2020][research_xi_wanqing_2020]
- [Xia et al 2022][research_xia_kong_2022]
- [Xiang et al 2008][research_xiang_rose_2008]
- [Xiang et al 2020][research_xiang_xie_2020]
- [Xiao 2016][research_xiao_2016]
- [Xiao et al 2025][research_xiao_wu_2025]
- [Xiao et al 2026][research_xiao_wu_2026]
- [Xiaodong et al 2010][research_xiaodong_guiping_2010]
- [Xie et al 2007][research_xie_leng_2007]
- [Xie et al 2013][research_xie_qi_2013]
- [Xie et al 2013][research_xie_wang_2013]
- [Xie et al 2016][research_xie_liu_2016]
- [Xie et al 2016][research_xie_zhang_2016]
- [Xie et al 2023][research_xie_cai_2023]
- [Xie et al 2024][research_xie_cui_2024]
- [Xin and Shi 2016][research_xin_shi_2016]
- [Xin et al 2026][research_xin_xu_2026]
- [Xiong and Lele 2003][research_xiong_lele_2003]
- [Xiong and Lele 2004][research_xiong_lele_2004]
- [Xiong and Nguyen 2024][research_xiong_nguyen_2024]
- [Xiong et al 2020][research_xiong_morgan_2020]
- [Xiong et al 2022][research_xiong_liu_2022]
- [Xiong et al 2024][research_xiong_liu_2024]
- [Xu 2023][research_xu_2023]
- [Xu and Guo 2003][research_xu_guo_2003]
- [Xu and He 2019][research_xu_he_2019]
- [Xu and Zhang 2020][research_xu_zhang_2020]
- [Xu et al 2010][research_xu_yao_2010]
- [Xu et al 2011][research_xu_yang_2011]
- [Xu et al 2017][research_xu_tian_2017]
- [Xu et al 2019][research_xu_yue_2019]
- [xu et al 2023][research_xu_song_2023]
- [Xu et al 2025][research_xu_huang_2025]
- [Xue and Mei 1992][research_xue_mei_1992]
- [Xue and Mei 1993][research_xue_mei_1993]
- [Xue et al 1990][research_xue_mei_1990]
- [Xue et al 2014][research_xue_khawaja_2014]
- [Xue et al 2019][research_xue_luo_2019]
- [Xue et al 2019][research_xue_wang_2019]
- [Xue et al 2019][research_xue_ye_2019]
- [Yahalom 1971][research_yahalom_1971]
- [Yahya A. AL-Salman et al 2013][research_yahyaaalsalman_mahmoodahmood_2013]
- [Yakimov 2018][research_yakimov_2018]
- [Yakimov 2018][research_yakimov_2018_b]
- [Yakimov 2018][research_yakimov_2018_c]
- [Yakovenko and Fedosov 2025][research_yakovenko_fedosov_2025]
- [Yamane et al 1997][research_yamane_ishihara_1997]
- [Yamazaki and Kusunose 2016][research_yamazaki_kusunose_2016]
- [Yan and He 2020][research_yan_he_2020]
- [Yan et al 1989][research_yan_munn_1989]
- [Yan et al 2021][research_yan_tai_2021]
- [Yang 2004][research_yang_2004]
- [Yang 2021][research_yang_2021]
- [Yang and Clark 1975][research_yang_clark_1975]
- [Yang and Li 2023][research_yang_li_2023]
- [Yang and Li 2023][research_yang_li_2023_b]
- [Yang and Sun 2012][research_yang_sun_2012]
- [Yang et al 2003][research_yang_obayashi_2003]
- [Yang et al 2009][research_yang_chen_2009]
- [Yang et al 2012][research_yang_yang_2012]
- [Yang et al 2018][research_yang_yu_2018]
- [Yang et al 2019][research_yang_li_2019]
- [Yang et al 2020][research_yang_yu_2020]
- [Yang et al 2023][research_yang_sun_2023]
- [Yang et al 2024][research_yang_liang_2024]
- [Yanta et al 1989][research_yanta_collier_1989]
- [Yao and Hussain 2019][research_yao_hussain_2019]
- [Yao et al 2014][research_yao_he_2014]
- [Yasumura and Kitamura 2021][research_yasumura_kitamura_2021]
- [Yates 1963][research_yates_1963]
- [Yates and Zeydel 1963][research_yates_zeydel_1963]
- [Yatskikh et al 2018][research_yatskikh_kosinov_2018]
- [Ye and Ye 2020][research_ye_ye_2020]
- [Ye and Ye 2021][research_ye_ye_2021]
- [Ye et al 2021][research_ye_ye_2021_b]
- [Ye et al 2026][research_ye_gu_2026]
- [Yee et al 1961][research_yee_bailey_1961]
- [Yerkovich and Guarnieri 1955][research_yerkovich_guarnieri_1955]
- [Yi et al 2015][research_yi_jun_2015]
- [Yih et al 1952][research_yih_cermak_1952]
- [Yildirim et al 2020][research_yildirim_2020]
- [Yildiz et al 2018][research_yildiz_akcal_2018]
- [Yildiz et al 2019][research_yildiz_akcal_2019]
- [Yilmaz and Kayran 2024][research_yilmaz_kayran_2024]
- [Yin et al 2025][research_yin_jiang_2025]
- [Yip et al 1980][research_yip_parlett_1980]
- [Yipton and Blachowski 1996][research_yipton_blachowski_1996]
- [Yonezawa and Obayashi 2010][research_yonezawa_obayashi_2010]
- [Yoo and Duensing 2019][research_yoo_duensing_2019]
- [Yoo et al 2004][research_yoo_shin_2004]
- [Yoon and Moon 2026][research_yoon_moon_2026]
- [Yoon et al 2012][research_yoon_jeon_2012]
- [Yoon et al 2013][research_yoon_jeon_2013]
- [Yoshida et al 2021][research_yoshida_bragg_2021]
- [You et al 2020][research_you_liu_2020]
- [Young 1965][research_young_1965]
- [Young 2016][research_young_2016]
- [Young 2016][research_young_2016_b]
- [Yount et al 1968][research_yount_smith_1968]
- [Yu and Bernal 2016][research_yu_bernal_2016]
- [Yu and Hornung 2026][research_yu_hornung_2026]
- [Yu et al 2014][research_yu_lv_2014]
- [Yu et al 2023][research_yu_dong_2023]
- [Yu et al 2025][research_yu_guo_2025]
- [Yu et al 2025][research_yu_yang_2025]
- [Yuan and Zhou 2000][research_yuan_zhou_2000]
- [Yuan et al 2014][research_yuan_wang_2014]
- [Yuan et al 2015][research_yuan_song_2015]
- [Yuceil and Dolling 1994][research_yuceil_dolling_1994]
- [Yuhui and Zhenguo 2002][research_yuhui_zhenguo_2002]
- [Yuwei et al 2024][research_yuwei_wu_2024]
- [Zaichik et al 2019][research_zaichik_yashin_2019]
- [Zalovcik 1945][research_zalovcik_1945]
- [Zaludin 2012][research_zaludin_2012]
- [Zapata Usandivaras][research_zapatausandivaras]
- [Zapata Usandivaras et al 2024][research_zapatausandivaras_bauerheim_2024]
- [Zartarian 1956][research_zartarian_1956]
- [Zartarian and Hsu 1955][research_zartarian_hsu_1955]
- [Zeiler 1999][research_zeiler_1999]
- [Zeng et al 2023][research_zeng_yuan_2023]
- [Zhai et al 2021][research_zhai_ma_2021]
- [Zhang 1995][research_zhang_1995]
- [Zhang 2003][research_zhang_2003]
- [Zhang 2009][research_zhang_2009]
- [Zhang 2016][research_zhang_2016]
- [Zhang and Chen 2016][research_zhang_chen_2016]
- [Zhang and Geng 2013][research_zhang_geng_2013]
- [Zhang and Li 2017][research_zhang_li_2017]
- [Zhang and Liu 2014][research_zhang_liu_2014]
- [Zhang and Taira 2022][research_zhang_taira_2022]
- [Zhang and Yi 2011][research_zhang_yi_2011]
- [Zhang and Zhang 2020][research_zhang_zhang_2020]
- [Zhang et al 2012][research_zhang_ga_2012]
- [Zhang et al 2013][research_zhang_cheng_2013]
- [Zhang et al 2016][research_zhang_wang_2016]
- [Zhang et al 2016][research_zhang_yang_2016]
- [Zhang et al 2018][research_zhang_lv_2018]
- [Zhang et al 2018][research_zhang_shao_2018]
- [Zhang et al 2018][research_zhang_zhou_2018]
- [Zhang et al 2018][research_zhang_zhou_2018_b]
- [Zhang et al 2019][research_zhang_liu_2019]
- [Zhang et al 2021][research_zhang_guo_2021]
- [Zhang et al 2022][research_zhang_xiao_2022]
- [Zhang et al 2023][research_zhang_li_2023]
- [Zhang et al 2024][research_zhang_feng_2024]
- [Zhang et al 2024][research_zhang_li_2024]
- [Zhang et al 2024][research_zhang_xin_2024]
- [Zhang et al 2025][research_zhang_li_2025]
- [Zhang et al 2025][research_zhang_zhang_2025]
- [Zhang et al 2026][research_zhang_zhang_2026]
- [Zhang et al 2026][research_zhang_zhang_2026_b]
- [Zhang et al 2026][research_zhang_zhao_2026]
- [Zhang et al 2026][research_zhang_zhou_2026]
- [Zhang JunHong et al 2010][research_zhangjunhong_hanjinglong_2010]
- [Zhang, et al 2011][research_zhang_peng_2011]
- [Zhao and Cao 2015][research_zhao_cao_2015]
- [Zhao and Jim Zhu 2017][research_zhao_jimzhu_2017]
- [Zhao and Kapania 2017][research_zhao_kapania_2017]
- [Zhao and Li 2019][research_zhao_li_2019]
- [Zhao and Liew 2010][research_zhao_liew_2010]
- [Zhao and Zhu 2016][research_zhao_zhu_2016]
- [Zhao and Zhu 2016][research_zhao_zhu_2016_b]
- [Zhao and Zhu 2016][research_zhao_zhu_2016_c]
- [Zhao et al 2009][research_zhao_zhang_2009]
- [Zhao et al 2011][research_zhao_yu_2011]
- [Zhao et al 2014][research_zhao_sheng_2014]
- [Zhao et al 2016][research_zhao_wei_2016]
- [Zhao et al 2016][research_zhao_xie_2016]
- [Zhao et al 2020][research_zhao_he_2020]
- [Zhao et al 2022][research_zhao_cai_2022]
- [Zhao et al 2023][research_zhao_zhang_2023]
- [Zhao et al 2024][research_zhao_li_2024]
- [Zhao et al 2025][research_zhao_wan_2025]
- [Zhao et al 2025][research_zhao_wu_2025]
- [Zhao et al 2025][research_zhao_zhang_2025]
- [Zhao et al 2026][research_zhao_qiao_2026]
- [Zheltovodov and Knight 2011][research_zheltovodov_knight_2011]
- [Zheltovodov et al 1985][research_zheltovodov_pavlov_1985]
- [Zhou 1995][research_zhou_1995]
- [Zhou and Yang 2013][research_zhou_yang_2013]
- [Zhou et al 2017][research_zhou_yang_2017]
- [Zhou et al 2019][research_zhou_xie_2019]
- [Zhou et al 2022][research_zhou_chen_2022]
- [Zhou et al 2022][research_zhou_wang_2022]
- [Zhou et al 2024][research_zhou_nie_2024]
- [Zhou et al 2024][research_zhou_yuan_2024]
- [Zhou et al 2026][research_zhou_dong_2026]
- [Zhu and Breuer 2022][research_zhu_breuer_2022]
- [Zhu et al 2012][research_zhu_wen_2012]
- [Zhu et al 2022][research_zhu_yao_2022]
- [Zhu et al 2024][research_zhu_voo_2024]
- [Zhu et al 2025][research_zhu_wang_2025]
- [Zhu et al 2025][research_zhu_wu_2025]
- [Zhu et al 2026][research_zhu_zhu_2026]
- [Zhuang et al 1998][research_zhuang_nie_1998]
- [Zhuang et al 1999][research_zhuang_nie_1999]
- [Ziefuß and Mehdizadeh 2020][research_ziefuss_mehdizadeh_2020]
- [Ziegler 1988][research_ziegler_1988]
- [Zima 1956][research_zima_1956]
- [Zimmerman and Weissenburger 1964][research_zimmerman_weissenburger_1964]
- [Zinn 1968][research_zinn_1968]
- [Zinn and Powell 1971][research_zinn_powell_1971]
- [Zinn and Savell 1969][research_zinn_savell_1969]
- [Znamenskaya et al 2008][research_znamenskaya_latfullin_2008]
- [Zohar and Er-El 1988][research_zohar_erel_1988]
- [Zook 2024][research_zook_2024]
- [Zoppini et al 2022][research_zoppini_ragni_2022]
- [Zu and Tan 2022][research_zu_tan_2022]
- [Zubair et al 2022][research_zubair_ejaz_2022]
- [Zubanov and Shabliy 2014][research_zubanov_shabliy_2014]
- [Zuev et al 2020][research_zuev_arngold_2020]
- [Özer 2025][research_ozer_2025]
- [Özöztürk et al 2011][research_ozozturk_kayran_2011]

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
- [A298 X-Planes, Bell X-1][related_post_a298_bell_x1]
- [A90 Introduction to Space Studies][related_post_a90_intro_space_studies]
- [A96 History of Rocketplanes][related_post_a96_history_rocketplanes]

[book_anderson_1997_history_aerodynamics]: https://openlibrary.org/works/OL1993322W
[book_anderson_2001_fundamentals]: https://openlibrary.org/works/OL3232211W
[book_anderson_2002_modern_compressible]: https://openlibrary.org/works/OL1993329W
[book_anderson_2006_hypersonic]: https://openlibrary.org/works/OL1993330W
[book_anderson_2012_aircraft_performance]: https://openlibrary.org/works/OL1993317W
[book_ashley_landahl_1965]: https://openlibrary.org/works/OL42971075W
[book_baals_corliss_1981]: https://openlibrary.org/works/OL31504107W
[book_bertin_1994_hypersonic]: https://openlibrary.org/works/OL3287053W
[book_bertin_cummings_2013]: https://openlibrary.org/works/OL21437883W
[book_bevington_robinson_2002]: https://openlibrary.org/works/OL44935135W
[book_bilstein_1989_orders]: https://openlibrary.org/works/OL18823771W
[book_bisplinghoff_ashley_halfman_1955]: https://openlibrary.org/works/OL3240762W
[book_boley_weiner_1960]: https://openlibrary.org/works/OL19334049W
[book_box_hunter_hunter_2005]: https://openlibrary.org/works/OL28985605W
[book_bruhn_1973]: https://openlibrary.org/works/OL8796483W
[book_carslaw_jaeger_1959]: https://openlibrary.org/works/OL34686169W
[book_chambers_2008_radical_wings]: https://openlibrary.org/works/OL5834577W
[book_cover_thomas_2006]: https://openlibrary.org/works/OL21500808W
[book_dowell_2014]: https://openlibrary.org/works/OL20677670W
[book_etkin_reid_1996]: https://openlibrary.org/works/OL19844466W
[book_everest_1958_fastest_man]: https://openlibrary.org/works/OL6556341W
[book_ferguson_1992]: https://openlibrary.org/works/OL4119982W
[book_fung_1955]: https://openlibrary.org/works/OL2655267W
[book_gelman_et_al_2013]: https://openlibrary.org/works/OL12630389W
[book_gorn_2001_expanding_envelope]: https://openlibrary.org/works/OL4400572W
[book_gunston_1992_faster_than_sound]: https://openlibrary.org/works/OL774338W
[book_hallion_1972_supersonic_flight]: https://openlibrary.org/works/OL2688456W
[book_hallion_1981_on_the_frontier]: https://openlibrary.org/works/OL2688458W
[book_hallion_1981_test_pilots]: https://openlibrary.org/works/OL2688457W
[book_hansen_1987_engineer_in_charge]: https://openlibrary.org/works/OL37594565W
[book_heppenheimer_2007_heat_barrier]: https://openlibrary.org/works/OL39929219W
[book_hill_peterson_1991]: https://openlibrary.org/works/OL8229940W
[book_hurt_1965]: https://openlibrary.org/works/OL4297319W
[book_huzel_huang_1992]: https://openlibrary.org/works/OL27313820W
[book_incropera_heat_transfer]: https://openlibrary.org/works/OL2975219W
[book_jenkins_2000_hypersonics]: https://openlibrary.org/works/OL813290W
[book_jenkins_2007_x15]: https://ntrs.nasa.gov/citations/20080008340
[book_jenkins_landis_miller_2003]: https://openlibrary.org/works/OL20394726W
[book_kimberlin_2003]: https://openlibrary.org/works/OL8874080W
[book_kuchemann_1978]: https://openlibrary.org/works/OL22640504W
[book_launius_jenkins_2012]: https://openlibrary.org/works/OL39998199W
[book_liepmann_roshko_1957]: https://openlibrary.org/works/OL13214987W
[book_mcruer_ashkenas_graham_1973]: https://openlibrary.org/works/OL13424815W
[book_megson_2016]: https://openlibrary.org/works/OL4809615W
[book_merlin_2009_blackbird]: https://openlibrary.org/works/OL11706498W
[book_miller_2001_x_planes]: https://openlibrary.org/works/OL7006680W
[book_nelson_1998]: https://openlibrary.org/works/OL11288560W
[book_nicolai_carichner_2010]: https://openlibrary.org/works/OL15909375W
[book_niu_1988_airframe]: https://openlibrary.org/works/OL19561185W
[book_peebles_2014_probing_the_sky]: https://openlibrary.org/works/OL23215820W
[book_perrow_1984]: https://openlibrary.org/works/OL4468929W
[book_petroski_1985]: https://openlibrary.org/works/OL112186W
[book_raymer_2018]: https://openlibrary.org/works/OL17855977W
[book_reason_1990_human_error]: https://openlibrary.org/works/OL9006915W
[book_sagan_1993]: https://openlibrary.org/works/OL3492159W
[book_schlichting_gersten_2017]: https://openlibrary.org/works/OL20524688W
[book_shapiro_1953]: https://openlibrary.org/works/OL5908243W
[book_stengel_2004]: https://openlibrary.org/works/OL3486012W
[book_stevens_lewis_2015]: https://openlibrary.org/works/OL21570717W
[book_sutton_biblarz_2016]: https://openlibrary.org/works/OL21470530W
[book_taylor_1997_error_analysis]: https://openlibrary.org/works/OL3232610W
[book_thompson_1992_edge_of_space]: https://openlibrary.org/works/OL1994111W
[book_truitt_1960]: https://openlibrary.org/works/OL178473W
[book_vaughan_1996]: https://openlibrary.org/works/OL2962391W
[book_vincenti_1990]: https://openlibrary.org/works/OL4805206W
[book_ward_strganac_niewoehner_2006]: https://openlibrary.org/works/OL19810630W
[book_white_2006_viscous]: https://openlibrary.org/works/OL1911849W
[book_whitford_1987]: https://openlibrary.org/works/OL5054670W
[book_winchester_2005_x_planes]: https://openlibrary.org/works/OL8492617W
[book_wolfe_1979_right_stuff]: https://openlibrary.org/works/OL1925474W
[ref_accelerometer]: https://en.wikipedia.org/wiki/Accelerometer
[ref_aerodynamic_center]: https://en.wikipedia.org/wiki/Aerodynamic_center
[ref_armstrong_frc]: https://en.wikipedia.org/wiki/Armstrong_Flight_Research_Center
[ref_aspect_ratio]: https://en.wikipedia.org/wiki/Aspect_ratio_(aeronautics)
[ref_b50]: https://en.wikipedia.org/wiki/Boeing_B-50_Superfortress
[ref_bell_aircraft]: https://en.wikipedia.org/wiki/Bell_Aircraft
[ref_bell_x1]: https://en.wikipedia.org/wiki/Bell_X-1
[ref_bell_x2]: https://en.wikipedia.org/wiki/Bell_X-2
[ref_bell_x5]: https://en.wikipedia.org/wiki/Bell_X-5
[ref_biot_number]: https://en.wikipedia.org/wiki/Biot_number
[ref_boundary_layer]: https://en.wikipedia.org/wiki/Boundary_layer
[ref_creep_deformation]: https://en.wikipedia.org/wiki/Creep_(deformation)
[ref_curtiss_wright]: https://en.wikipedia.org/wiki/Curtiss-Wright
[ref_directional_stability]: https://en.wikipedia.org/wiki/Directional_stability
[ref_douglas_x3]: https://en.wikipedia.org/wiki/Douglas_X-3_Stiletto
[ref_drag_coefficient]: https://en.wikipedia.org/wiki/Drag_coefficient
[ref_duralumin]: https://en.wikipedia.org/wiki/Duralumin
[ref_dutch_roll]: https://en.wikipedia.org/wiki/Dutch_roll
[ref_dynamic_pressure]: https://en.wikipedia.org/wiki/Dynamic_pressure
[ref_edwards_afb]: https://en.wikipedia.org/wiki/Edwards_Air_Force_Base
[ref_ejection_seat]: https://en.wikipedia.org/wiki/Ejection_seat
[ref_escape_crew_capsule]: https://en.wikipedia.org/wiki/Escape_crew_capsule
[ref_euler_equations_rigid]: https://en.wikipedia.org/wiki/Euler%27s_equations_(rigid_body_dynamics)
[ref_everest]: https://en.wikipedia.org/wiki/Frank_Kendall_Everest_Jr.
[ref_experimental_aircraft]: https://en.wikipedia.org/wiki/Experimental_aircraft
[ref_f100]: https://en.wikipedia.org/wiki/North_American_F-100_Super_Sabre
[ref_flight_dynamics]: https://en.wikipedia.org/wiki/Flight_dynamics_(fixed-wing_aircraft)
[ref_flight_envelope]: https://en.wikipedia.org/wiki/Flight_envelope
[ref_flight_test]: https://en.wikipedia.org/wiki/Flight_test
[ref_flow_separation]: https://en.wikipedia.org/wiki/Flow_separation
[ref_fourier_number]: https://en.wikipedia.org/wiki/Fourier_number
[ref_heat_equation]: https://en.wikipedia.org/wiki/Heat_equation
[ref_heat_flux]: https://en.wikipedia.org/wiki/Heat_flux
[ref_hypersonic_flight]: https://en.wikipedia.org/wiki/Hypersonic_flight
[ref_inconel]: https://en.wikipedia.org/wiki/Inconel
[ref_inertia_coupling]: https://en.wikipedia.org/wiki/Inertia_coupling
[ref_isa]: https://en.wikipedia.org/wiki/International_Standard_Atmosphere
[ref_karman_line]: https://en.wikipedia.org/wiki/K%C3%A1rm%C3%A1n_line
[ref_kincheloe]: https://en.wikipedia.org/wiki/Iven_Carl_Kincheloe_Jr.
[ref_lift_coefficient]: https://en.wikipedia.org/wiki/Lift_coefficient
[ref_lift_to_drag]: https://en.wikipedia.org/wiki/Lift-to-drag_ratio
[ref_liquid_oxygen]: https://en.wikipedia.org/wiki/Liquid_oxygen
[ref_list_of_x_planes]: https://en.wikipedia.org/wiki/List_of_X-planes
[ref_load_factor]: https://en.wikipedia.org/wiki/Load_factor_(aeronautics)
[ref_longitudinal_static_stability]: https://en.wikipedia.org/wiki/Longitudinal_static_stability
[ref_mach_number]: https://en.wikipedia.org/wiki/Mach_number
[ref_measurement_uncertainty]: https://en.wikipedia.org/wiki/Measurement_uncertainty
[ref_mel_apt]: https://en.wikipedia.org/wiki/Milburn_G._Apt
[ref_moment_of_inertia]: https://en.wikipedia.org/wiki/Moment_of_inertia
[ref_monel]: https://en.wikipedia.org/wiki/Monel
[ref_na_x15]: https://en.wikipedia.org/wiki/North_American_X-15
[ref_naca]: https://en.wikipedia.org/wiki/National_Advisory_Committee_for_Aeronautics
[ref_nasa]: https://en.wikipedia.org/wiki/NASA
[ref_nasa_armstrong]: https://www.nasa.gov/centers-and-facilities/armstrong/
[ref_nasa_history]: https://www.nasa.gov/history/
[ref_nasa_x2_factsheet]: https://www.nasa.gov/wp-content/uploads/2021/09/120323main_fs-079-dfrc.pdf
[ref_nmusaf]: https://en.wikipedia.org/wiki/National_Museum_of_the_United_States_Air_Force
[ref_northrop_x4]: https://en.wikipedia.org/wiki/Northrop_X-4_Bantam
[ref_ntrs]: https://ntrs.nasa.gov/
[ref_oblique_shock]: https://en.wikipedia.org/wiki/Oblique_shock
[ref_phugoid]: https://en.wikipedia.org/wiki/Phugoid
[ref_prandtl_number]: https://en.wikipedia.org/wiki/Prandtl_number
[ref_propagation_of_uncertainty]: https://en.wikipedia.org/wiki/Propagation_of_uncertainty
[ref_rcs]: https://en.wikipedia.org/wiki/Reaction_control_system
[ref_reynolds_number]: https://en.wikipedia.org/wiki/Reynolds_number
[ref_rocket_engine]: https://en.wikipedia.org/wiki/Rocket_engine
[ref_shock_wave]: https://en.wikipedia.org/wiki/Shock_wave
[ref_sound_barrier]: https://en.wikipedia.org/wiki/Sound_barrier
[ref_specific_impulse]: https://en.wikipedia.org/wiki/Specific_impulse
[ref_speed_of_sound]: https://en.wikipedia.org/wiki/Speed_of_sound
[ref_sr71]: https://en.wikipedia.org/wiki/Lockheed_SR-71_Blackbird
[ref_stabilator]: https://en.wikipedia.org/wiki/Stabilator
[ref_stagnation_temperature]: https://en.wikipedia.org/wiki/Stagnation_temperature
[ref_stainless_steel]: https://en.wikipedia.org/wiki/Stainless_steel
[ref_stefan_boltzmann]: https://en.wikipedia.org/wiki/Stefan%E2%80%93Boltzmann_law
[ref_strain_gauge]: https://en.wikipedia.org/wiki/Strain_gauge
[ref_supersonic_speed]: https://en.wikipedia.org/wiki/Supersonic_speed
[ref_swept_wing]: https://en.wikipedia.org/wiki/Swept_wing
[ref_telemetry]: https://en.wikipedia.org/wiki/Telemetry
[ref_thermal_conductivity]: https://en.wikipedia.org/wiki/Thermal_conductivity
[ref_thermal_expansion]: https://en.wikipedia.org/wiki/Thermal_expansion
[ref_thermal_stress]: https://en.wikipedia.org/wiki/Thermal_stress
[ref_thermocouple]: https://en.wikipedia.org/wiki/Thermocouple
[ref_titanium_alloys]: https://en.wikipedia.org/wiki/Titanium_alloy
[ref_transonic]: https://en.wikipedia.org/wiki/Transonic
[ref_tsiolkovsky]: https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation
[ref_turbopump]: https://en.wikipedia.org/wiki/Turbopump
[ref_us_standard_atmosphere]: https://en.wikipedia.org/wiki/U.S._Standard_Atmosphere
[ref_wave_drag]: https://en.wikipedia.org/wiki/Wave_drag
[ref_wind_tunnel]: https://en.wikipedia.org/wiki/Wind_tunnel
[ref_wing_loading]: https://en.wikipedia.org/wiki/Wing_loading
[ref_xb70]: https://en.wikipedia.org/wiki/North_American_XB-70_Valkyrie
[ref_yield_strength]: https://en.wikipedia.org/wiki/Yield_(engineering)
[related_post_a106_two_stage_delta_wing]: {% post_url 2026-03-12-two_stage_flying_delta_wing_vehicles_for_civil_and_national_security_applications %}
[related_post_a118_propulsion_sizing]: {% post_url 2026-06-02-propulsion_and_power_sizing_for_fixed_wing_uavs %}
[related_post_a122_stability_configuration]: {% post_url 2026-06-05-stability_control_and_configuration_for_fixed_wing_uavs %}
[related_post_a123_dynamic_stability]: {% post_url 2026-06-06-dynamic_stability_and_control_for_fixed_wing_uavs %}
[related_post_a127_structures_flight_envelope]: {% post_url 2026-06-10-structures_and_the_flight_envelope_for_fixed_wing_uavs %}
[related_post_a217_rocket_propellant_chemistry]: {% post_url 2026-02-01-rocket_propellant_chemistry_a_design_tradeoff_space %}
[related_post_a237_aerospace_framing]: {% post_url 2026-07-13-framing_and_the_co_development_mechanism %}
[related_post_a241_aerospace_simulation]: {% post_url 2026-07-17-aerospace_simulation_and_real_time_systems %}
[related_post_a297_xplanes_framing]: {% post_url 2025-10-06-x_planes_framing %}
[related_post_a298_bell_x1]: {% post_url 2025-10-07-x_planes_bell_x1 %}
[related_post_a90_intro_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[related_post_a96_history_rocketplanes]: {% post_url 2026-02-27-history_of_rocketplanes %}
[research_a_special_1952]: https://doi.org/10.1016/0016-0032(52)90873-9
[research_a_supersonic_1949]: https://doi.org/10.1016/0016-0032(49)90725-5
[research_a_system_2004]: https://doi.org/10.5139/jksas.2004.32.5.109
[research_a_thermocouple_1962]: https://doi.org/10.1595/003214062x64149149
[research_aamir_abbasi_2026]: https://doi.org/10.2514/1.c038958
[research_abarbanel_1977]: https://doi.org/10.21236/ada035568
[research_abbas_ibrahim_1992]: https://doi.org/10.2514/6.1992-2132
[research_abbas_rui_2012]: https://doi.org/10.1115/1.4005537
[research_abbe_mclaughlin_1967]: https://doi.org/10.2514/6.1967-474
[research_abdelkefi_vasconcellos_2011]: https://doi.org/10.1007/s11071-011-0245-6
[research_abdollahi_ehsani_2016]: https://doi.org/10.1007/s11661-016-3813-z
[research_abe_2021]: https://doi.org/10.1080/09603409.2021.1935637
[research_abe_tabuchi_2016]: https://doi.org/10.31399/asm.cp.am-epri-2016p0125
[research_abensur_2008]: https://doi.org/10.2514/6.2008-4775
[research_abouamer_2020]: https://doi.org/10.21608/bfemu.2020.126840
[research_abramov_butkovskii_2018]: https://doi.org/10.1016/j.ijheatmasstransfer.2017.10.011
[research_abramov_goman_2005]: https://doi.org/10.2514/6.2005-6331
[research_abuaf_1976]: https://doi.org/10.21236/ada037674
[research_abuaf_dorri_1997]: https://doi.org/10.1115/97-gt-385
[research_ackeret_1925]: https://ntrs.nasa.gov/citations/19930087085
[research_adams_1972]: https://doi.org/10.2514/6.1972-962
[research_adams_1974]: https://doi.org/10.1016/0017-9310(74)90006-4
[research_adams_2014]: https://doi.org/10.1109/aero.2014.6836489
[research_adams_rubin_1958]: https://doi.org/10.21236/ad0200634
[research_adamsjr_1972]: https://doi.org/10.2514/6.1972-186
[research_adkins_armstrong_1965]: https://ntrs.nasa.gov/citations/19730062071
[research_advanced_metallics_1992]: https://doi.org/10.2514/5.9781600866128.0161.0179
[research_advancedfuelresearchinceasthartfordct_1957]: https://doi.org/10.21236/ada390317
[research_advani_field_2011]: https://doi.org/10.2514/6.2011-6698
[research_advani_schroeder_2016]: https://doi.org/10.2514/6.2016-1430
[research_aero_has_2006]: https://doi.org/10.1108/aeat.2006.12778bab.021
[research_aerodynamic_and_1960]: https://ntrs.nasa.gov/citations/19980228350
[research_aerodynamic_and_2014]: https://doi.org/10.15242/iie.e1214053
[research_aerodynamic_components_1957]: https://doi.org/10.1515/9781400879908
[research_aerodynamic_heating_1978]: https://doi.org/10.2514/4.865336
[research_aerodynamic_phenomena_2020]: https://doi.org/10.1002/9781119667063.ch4
[research_aeroelastic_tests_1963]: https://ntrs.nasa.gov/citations/20070030987
[research_aerothermal_environment_1978]: https://doi.org/10.2514/5.9781600865336.0003.0026
[research_agarwal_1982]: https://ntrs.nasa.gov/citations/19820038553
[research_agarwal_miley_1992]: https://doi.org/10.2514/6.1992-4089
[research_ageev_pavlenko_2016]: https://doi.org/10.1108/aeat-02-2015-0052
[research_ageev_sosura_2020]: https://doi.org/10.1615/tsagiscij.2021037731
[research_agrawal_kinard_1991]: https://doi.org/10.2514/3.46088
[research_aharrah_2007]: https://ntrs.nasa.gov/citations/20080009626
[research_aharrah_2007_b]: https://ntrs.nasa.gov/citations/20100011189
[research_ahmad_rahman_2014]: https://doi.org/10.1109/ibcast.2014.6778168
[research_ahmadi_pourshahsavari_2016]: https://doi.org/10.15632/jtam-pl.54.1.135
[research_ahmed_wentz_1989]: https://ntrs.nasa.gov/citations/19900025962
[research_ahmed_worley_2008]: https://doi.org/10.2514/6.2008-366
[research_ai_qu_2011]: https://doi.org/10.5772/13392
[research_aircraft_crew_2014]: https://doi.org/10.1201/b17399-114
[research_aircraft_flight]: https://doi.org/10.4271/air4094
[research_aircraft_lateral_directional_2011]: https://doi.org/10.1049/pbce074e_ch9
[research_aircraft_stability_2003]: https://doi.org/10.2514/5.9781600862069.0433.0472
[research_aircraft_stability_2014]: https://doi.org/10.2514/5.9781624102547.0465.0508
[research_aircraft_stability_2024]: https://doi.org/10.2514/5.9781624107252.0467.0510
[research_airforcetestpilotschooledwardsafbca_1989]: https://doi.org/10.21236/ada319980
[research_airforcetestpilotschooledwardsafbca_1990]: https://doi.org/10.21236/ada319978
[research_airforcetestpilotschooledwardsafbca_1991]: https://doi.org/10.21236/ada320218
[research_airplane_and_1990]: https://doi.org/10.1017/cbo9780511622892.012
[research_airspeed_calibration_1950]: https://ntrs.nasa.gov/citations/19930090286
[research_akaydin_moiniyekta_2015]: https://doi.org/10.2514/6.2015-2418
[research_akcal_hostas_2018]: https://doi.org/10.1109/aero.2018.8396500
[research_akmandor_nagashima_1999]: https://doi.org/10.2514/6.1999-874
[research_alaian_basuno_2016]: https://doi.org/10.3923/itj.2017.44.50
[research_alam_rao_2010]: https://doi.org/10.1007/s11085-010-9190-x
[research_albakri]: https://doi.org/10.32469/10355/70012
[research_albakri_2020]: https://doi.org/10.2514/1.g004934
[research_albakri_kluever_2017]: https://doi.org/10.4236/aast.2017.24004
[research_alclad_aging_1943]: https://ntrs.nasa.gov/citations/19930093377
[research_alcock_hagar_1989]: https://doi.org/10.2514/6.1989-2851
[research_alder_2014]: https://doi.org/10.2514/6.2014-2448
[research_alder_2015]: https://doi.org/10.2514/1.j054013
[research_alemdaroglu_iyigun_2002]: https://doi.org/10.2514/6.2002-528
[research_alexander_1948]: https://ntrs.nasa.gov/citations/20010062506
[research_alexander_1970]: https://doi.org/10.21236/ad0875525
[research_alfano_gardi_2014]: https://doi.org/10.1002/9781118700853.ch16
[research_alighanbari_2002]: https://doi.org/10.2514/2.2986
[research_alkhaleefi_2004]: https://doi.org/10.1142/s0219455404001252
[research_alkidas_durbetaki_1972]: https://doi.org/10.1115/1.3449960
[research_alle_1967]: https://doi.org/10.1108/eb034316
[research_allee_eg_1976]: https://doi.org/10.21236/adb014360
[research_allen_1972]: https://doi.org/10.2514/3.50153
[research_allen_2004]: https://doi.org/10.2514/6.2004-5450
[research_allen_keustermans_2004]: https://doi.org/10.1179/mht.2004.008
[research_alnaser_yunus_2021]: https://doi.org/10.3390/ma14185119
[research_alsaif_foda_2015]: https://doi.org/10.1142/s0219455414500849
[research_altgelt_ward_1968]: https://doi.org/10.2514/6.1968-932
[research_altunkaya_2025]: https://doi.org/10.2514/1.g008188
[research_alvi_2012]: https://doi.org/10.21236/ada563916
[research_aly_ogot_2002]: https://doi.org/10.2514/2.3035
[research_alyanak_pendleton_2014]: https://doi.org/10.2514/6.2014-3158
[research_alyanak_pendleton_2017]: https://doi.org/10.2514/1.c033040
[research_amano_momose_1992]: https://doi.org/10.1016/b978-0-444-88970-6.50018-x
[research_amendola_dimino_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00018-6
[research_amirzadegan_2026]: https://doi.org/10.1177/10775463261462920
[research_an_aeroelastic_2013]: https://doi.org/10.36884/jafm.6.01.19503
[research_an_evaluation_1970]: https://doi.org/10.1520/ds11s1-eb
[research_an_experimental_1978]: https://doi.org/10.2514/6.1978-1200
[research_an_introduction_1966]: https://doi.org/10.1016/c2013-0-08104-2
[research_an_jiepan_2023]: https://doi.org/10.1109/icsp58490.2023.10248535
[research_analysis_of_the_2024]: https://doi.org/10.36948/ijfmr.2024.v06i03.19290
[research_ananthkrishnan_2004]: https://doi.org/10.2514/6.2004-4950
[research_ananthkrishnan_sinha_2023]: https://doi.org/10.61653/joast.v65i4.2013.877
[research_anderson_1959]: https://doi.org/10.21236/ad0312275
[research_anderson_1960]: https://doi.org/10.21236/ad0315671
[research_anderson_1965]: https://doi.org/10.2514/6.1965-1105
[research_anderson_1968]: https://doi.org/10.2514/3.4593
[research_anderson_1968_b]: https://doi.org/10.2514/3.4970
[research_anderson_campbell_2010]: https://ntrs.nasa.gov/citations/20100001399
[research_anderson_heister_2013]: https://doi.org/10.21236/ada577052
[research_anderson_heister_2015]: https://doi.org/10.21236/ad1001343
[research_anderson_innis_1965]: https://doi.org/10.2514/6.1965-715
[research_anderson_ryan_1995]: https://doi.org/10.2514/6.1995-2357
[research_anderson_schroers_1972]: https://ntrs.nasa.gov/citations/19730008267
[research_anderson_son_2012]: https://doi.org/10.21236/ada566310
[research_andersonjr_1968]: https://doi.org/10.2514/6.1968-164
[research_ando_2017]: https://doi.org/10.1049/cp.2017.0319
[research_andreopoulos_1982]: https://doi.org/10.1615/ihtc7.1760
[research_andrew_1981]: https://doi.org/10.2514/6.1981-1674
[research_andrews_1977]: https://doi.org/10.2514/6.1977-1204
[research_anikina_renshaw_2026]: https://doi.org/10.2514/6.2026-115072
[research_aniskin_mironov_2015]: https://doi.org/10.1007/s10404-015-1588-y
[research_anthony_2005]: https://doi.org/10.1049/cp:20050101
[research_antonov_1971]: https://doi.org/10.1007/bf01013990
[research_anwar_mabruri_2022]: https://doi.org/10.1063/5.0085989
[research_aoki_ota_1986]: https://doi.org/10.2221/jcsj.21.2
[research_appendix_g_2003]: https://doi.org/10.2514/5.9781600862069.0609.0612
[research_approximate_expressions_2007]: https://doi.org/10.1016/b978-075066927-6/50025-8
[research_aprovitola_dinuzzo_2021]: https://doi.org/10.3390/en14206615
[research_aprovitola_dyblenko_2022]: https://doi.org/10.3390/aerospace9080411
[research_arabshahi_taylor_2011]: https://doi.org/10.2514/6.2011-3348
[research_arai_noto_2000]: https://doi.org/10.2514/6.2000-4327
[research_arc_heater_code_validation_1978]: https://doi.org/10.2514/5.9781600865336.0261.0273
[research_archambaud_arnal_2009]: https://doi.org/10.1007/978-90-481-3723-7_10
[research_archambaud_louis_2004]: https://doi.org/10.2514/6.2004-2245
[research_armstrong_1977]: https://doi.org/10.21236/adb029224
[research_armstrong_1979]: https://doi.org/10.21236/ada063518
[research_armstrong_1989]: https://doi.org/10.2514/6.1989-2739
[research_armstrong_kilner_1953]: https://doi.org/10.21236/ad0009747
[research_armstrong_miller_1968]: https://doi.org/10.2514/3.43932
[research_armstrong_schlumberger_1990]: https://doi.org/10.2514/6.1990-2120
[research_armywarcollcarlislebarrackspa_1952]: https://doi.org/10.21236/ada390507
[research_arnal_vignau_1990]: https://doi.org/10.1007/978-3-642-84103-3_62
[research_arnette_samimy_1995]: https://doi.org/10.2514/3.60007
[research_arnold_1942]: https://doi.org/10.2514/8.10949
[research_arnold_1968]: https://doi.org/10.2514/6.1968-1068
[research_aronov_klyagin_2021]: https://doi.org/10.34759/tpt-2021-13-10-456-466
[research_artificial_pitch_damping_1959]: https://ntrs.nasa.gov/citations/19980228212
[research_aryaman_naveenraj_2023]: https://doi.org/10.1016/j.matpr.2023.06.022
[research_aryass_hfarhood_2009]: https://doi.org/10.30684/etj.27.9.16
[research_asad_avery_2022]: https://doi.org/10.2514/6.2022-0351
[research_asad_avery_2024]: https://doi.org/10.2514/6.2024-4656
[research_asadi_wang_2017]: https://doi.org/10.1016/j.compositesb.2017.03.001
[research_asghar_allan_2018]: https://doi.org/10.1115/gt2018-76661
[research_asher_martuccelli_1957]: https://doi.org/10.21236/ad0142088
[research_ashkenas_1965]: https://doi.org/10.21236/ad0627659
[research_ashokkumar_2023]: https://doi.org/10.2514/6.2023-0293
[research_ashraf_vankampen_2020]: https://doi.org/10.2514/6.2020-1845
[research_ashworth_mouch_1988]: https://doi.org/10.2514/6.1988-563
[research_askari_2023]: https://doi.org/10.3390/aerospace10060513
[research_aslam_islam_2025]: https://doi.org/10.2514/6.2025-2429
[research_assessment_of_1992]: https://doi.org/10.2514/5.9781600866128.0059.0091
[research_asymmetric_sweep_flutter_1976]: https://ntrs.nasa.gov/citations/19760014076
[research_atabay_sanchezmata_2021]: https://doi.org/10.1016/j.jallcom.2020.157645
[research_atik_baran_2012]: https://doi.org/10.2514/6.2012-2765
[research_attinello_1956]: https://doi.org/10.4271/560012
[research_automatic_flight_2000]: https://doi.org/10.2514/5.9781600866555.0170.0196
[research_av_d_2026]: https://doi.org/10.1002/prep.70238
[research_avanzini_matteis_1997]: https://doi.org/10.2514/2.4108
[research_awadallaalihajahmed_2024]: https://doi.org/10.47191/etj/v9i10.08
[research_ayran_bayezit_2026]: https://doi.org/10.20944/preprints202608.1941.v1
[research_ayu_aa_2023]: https://doi.org/10.36236/1999-7590-2023-15-4-256-262
[research_azzouz_smith_2011]: https://doi.org/10.2514/6.2011-1994
[research_baals_harrisjr_1968]: https://doi.org/10.2514/6.1968-1018
[research_baals_robins_1970]: https://doi.org/10.2514/3.59441
[research_babcock_wiltse_1965]: https://doi.org/10.2514/6.1965-152
[research_baber_carter_1962]: https://ntrs.nasa.gov/citations/19670022650
[research_babineaux_horton_1966]: https://ntrs.nasa.gov/citations/19660038601
[research_babinsky_2007]: https://doi.org/10.21236/ada476419
[research_babinsky_2014]: https://doi.org/10.21236/ada602774
[research_babishiii_1966]: https://doi.org/10.2514/6.1966-1506
[research_babister_1980]: https://doi.org/10.1016/b978-0-08-024768-7.50017-x
[research_babister_1980_b]: https://doi.org/10.1016/b978-0-08-024768-7.50019-3
[research_babu_murty_2018]: https://doi.org/10.7449/2018/mst_2018_670_679
[research_babucke_rist_2009]: https://doi.org/10.1007/978-90-481-3723-7_14
[research_bachalo_modarress_1977]: https://doi.org/10.2514/6.1977-47
[research_back_cuffel_1966]: https://ntrs.nasa.gov/citations/19670036108
[research_back_cuffel_1967]: https://ntrs.nasa.gov/citations/19670056085
[research_back_cuffel_1970]: https://doi.org/10.1115/1.3449668
[research_back_cuffel_1970_b]: https://doi.org/10.2514/3.6051
[research_back_cuffel_1970_c]: https://ntrs.nasa.gov/citations/19700068457
[research_back_cuffel_1971]: https://doi.org/10.1115/1.3449837
[research_back_cuffel_1972]: https://doi.org/10.1115/1.3449911
[research_back_cuffel_1984]: https://ntrs.nasa.gov/citations/19840053700
[research_bade_1962]: https://doi.org/10.1063/1.1706589
[research_bade_1975]: https://doi.org/10.1063/1.861259
[research_badiei_sadr_2014]: https://doi.org/10.1061/(asce)as.1943-5525.0000263
[research_bae_seigler_2005]: https://doi.org/10.2514/1.4397
[research_baer_1966]: https://doi.org/10.21236/ad0477832
[research_baerriedhart_1981]: https://doi.org/10.2514/6.1981-2467
[research_baghdadi_lowenberg_2009]: https://doi.org/10.2514/6.2009-6305
[research_baghdadi_lowenberg_2011]: https://doi.org/10.2514/1.51468
[research_bagheri_strataridakis_1990]: https://doi.org/10.2514/6.1990-20
[research_bahrami_2012]: https://ntrs.nasa.gov/citations/20120016518
[research_bai_cao_2022]: https://doi.org/10.1016/j.tsep.2022.101297
[research_bai_cheng_2020]: https://doi.org/10.1016/j.expthermflusci.2019.110038
[research_bai_hou_1994]: https://doi.org/10.1016/b978-0-444-81994-9.50052-x
[research_bai_li_2015]: https://doi.org/10.1115/imece2015-53062
[research_baier_karnam_2019]: https://doi.org/10.2514/6.2019-1302
[research_bairamov_bairamov_2022]: https://doi.org/10.34759/trd-2022-125-03
[research_bajpai_beytin_2008]: https://doi.org/10.2514/6.2008-6657
[research_baker]: https://doi.org/10.14264/345057
[research_baker_1967]: https://doi.org/10.2514/6.1967-427
[research_baker_1968]: https://doi.org/10.2514/3.29307
[research_baker_1969]: https://doi.org/10.2514/3.29848
[research_balachandran_atkins_2014]: https://doi.org/10.2514/6.2014-0785
[research_balachandran_atkins_2016]: https://doi.org/10.2514/6.2016-0094
[research_balakrishnan_kurian_2014]: https://doi.org/10.2514/1.a32712
[research_balas_packard_1996]: https://doi.org/10.2514/6.1996-3781
[research_balepin_2006]: https://doi.org/10.2514/6.2006-4695
[research_banerjee_utreja_1975]: https://doi.org/10.2514/6.1975-1383
[research_banks_2008]: https://ntrs.nasa.gov/citations/20080030370
[research_banks_2008_b]: https://ntrs.nasa.gov/citations/20080042408
[research_banks_frederick_2012]: https://ntrs.nasa.gov/citations/20120015436
[research_banks_fredericks_2012]: https://ntrs.nasa.gov/citations/20120014341
[research_bano_fraser_2026]: https://doi.org/10.1109/metroaerospace69299.2026.11646676
[research_bao_zhou_2021]: https://doi.org/10.3389/fbioe.2021.759442
[research_barbosa_bertolin_2019]: https://doi.org/10.2514/6.2019-0365
[research_barlog_1979]: https://doi.org/10.2514/6.1979-418
[research_barlow_stepanyan_2012]: https://ntrs.nasa.gov/citations/20130001722
[research_barnhardt_drayna_2007]: https://doi.org/10.2514/6.2007-2529
[research_barnwell_1989]: https://doi.org/10.2514/6.1989-1864
[research_barr_1971]: https://doi.org/10.2514/6.1971-328
[research_barrett_1982]: https://ntrs.nasa.gov/citations/19830003021
[research_barrett_1992]: https://ntrs.nasa.gov/citations/19930008880
[research_barrett_1997]: https://ntrs.nasa.gov/citations/19970025059
[research_barrett_1999]: https://ntrs.nasa.gov/citations/20050187019
[research_barrett_lowell_1974]: https://ntrs.nasa.gov/citations/19740013021
[research_barrett_lowell_1981]: https://ntrs.nasa.gov/citations/19810017697
[research_barrettgonzalez_wolf_2021]: https://doi.org/10.3390/act10100265
[research_barry_bassick_1995]: https://doi.org/10.4271/951545
[research_barthelemy_bergen_1988]: https://doi.org/10.2514/6.1988-2301
[research_barthelemy_bergen_1989]: https://doi.org/10.2514/3.45829
[research_bartlett_harris_1972]: https://ntrs.nasa.gov/citations/19780016137
[research_bartlett_harris_1973]: https://ntrs.nasa.gov/citations/19830002762
[research_bartlett_re_1972]: https://ntrs.nasa.gov/citations/19780016135
[research_barton_zaremba_2021]: https://doi.org/10.1080/09603409.2021.1895541
[research_bartz_1955]: https://doi.org/10.1115/1.4014652
[research_bartz_1965]: https://doi.org/10.1016/s0065-2717(08)70261-2
[research_baryshev_vinogradov_1972]: https://doi.org/10.1007/bf01186475
[research_bashkin_egorov_2005]: https://doi.org/10.1007/s10740-005-0118-0
[research_bashu_singh_1987]: https://doi.org/10.1080/02619180.1987.11753339
[research_bassett_pei_2018]: https://doi.org/10.2514/6.2018-0014
[research_bassina_strelets_2001]: https://doi.org/10.1615/heattransres.v32.i7-8.50
[research_bateman_2010]: https://doi.org/10.2514/6.2010-8139
[research_battaglia_baldieri_2024]: https://doi.org/10.1002/masy.202300184
[research_bauer_winkler_1978]: https://doi.org/10.1615/ihtc6.1020
[research_bauer_wood_1989]: https://doi.org/10.2514/6.1989-2167
[research_bauerle_1961]: https://doi.org/10.1063/1.1717351
[research_baum_levine_1984]: https://doi.org/10.21236/ada176271
[research_bazarov_1994]: https://doi.org/10.2514/6.1994-2978
[research_bazarov_1998]: https://doi.org/10.2514/6.1998-4039
[research_bazile_calderara_2012]: https://doi.org/10.1051/eucass/201203053
[research_beck_1984]: https://doi.org/10.21236/ada143254
[research_beck_1984_b]: https://doi.org/10.21236/ada328840
[research_beeler_1956]: https://ntrs.nasa.gov/citations/19930084521
[research_behrens_1971]: https://doi.org/10.2514/6.1971-127
[research_belcastro]: https://ntrs.nasa.gov/citations/20200007067
[research_belcastro_2011]: https://ntrs.nasa.gov/citations/20110012012
[research_belcastro_2012]: https://doi.org/10.2514/6.2012-4762
[research_belcastro_2012_b]: https://doi.org/10.2514/6.2012-4987
[research_belcastro_foster_2010]: https://doi.org/10.2514/6.2010-8004
[research_belcastro_jacobson_2010]: https://doi.org/10.2514/6.2010-8142
[research_belcastro_khong_2005]: https://doi.org/10.2514/6.2005-6427
[research_belcastro_khong_2005_b]: https://ntrs.nasa.gov/citations/20050223581
[research_belcastro_newman_2016]: https://ntrs.nasa.gov/citations/20160007744
[research_beldica_hilton_1999]: https://doi.org/10.2514/6.1999-1423
[research_beldica_hilton_2001]: https://doi.org/10.2514/6.2001-1647
[research_bell_1963]: https://doi.org/10.21236/ad0418711
[research_bellows_brewster_1984]: https://doi.org/10.2514/6.1984-1286
[research_belnap_vanrij_2002]: https://doi.org/10.1016/s0017-9310(02)00042-x
[research_beltran_kosvic_1966]: https://doi.org/10.2514/6.1966-603
[research_belyavin_kurenkova_2014]: https://doi.org/10.15407/tpwj2014.02.02
[research_benditt_1963]: https://doi.org/10.21236/ad0407063
[research_bengida_gurka_2022]: https://doi.org/10.1088/1748-3190/ac9bb5
[research_bengtson_dickovich_1975]: https://doi.org/10.21236/ada016932
[research_benjamin_mcconnaughey_1991]: https://doi.org/10.2514/6.1991-2361
[research_bennetclark_1972]: https://doi.org/10.1038/239451b0
[research_bentsman_wilcutts_1991]: https://doi.org/10.23919/acc.1991.4791943
[research_beran_hur_2005]: https://doi.org/10.2514/6.2005-1944
[research_berci_2017]: https://doi.org/10.1063/1.4992672
[research_beresh_henfling_2010]: https://doi.org/10.2514/6.2010-4274
[research_berg_1991]: https://doi.org/10.2514/6.1991-2630
[research_berger_anderson_2011]: https://ntrs.nasa.gov/citations/20110013660
[research_berger_carmona_2011]: https://doi.org/10.2514/6.2011-3663
[research_bergstrom_raghunathan_1972]: https://doi.org/10.2514/3.50252
[research_bermudez_2024]: https://doi.org/10.52202/078371-0180
[research_bernal_2016]: https://doi.org/10.2514/6.2016-0287
[research_berry_horvath_2006]: https://ntrs.nasa.gov/citations/20060022550
[research_berry_horvath_2008]: https://ntrs.nasa.gov/citations/20080023461
[research_berry_mallick_1976]: https://ntrs.nasa.gov/citations/19770011063
[research_berry_powers_1970]: https://doi.org/10.2514/6.1970-566
[research_bertelrud_1981]: https://doi.org/10.2514/6.1981-2418
[research_bettles_gibson_2003]: https://doi.org/10.1002/3527603565.ch1
[research_bewlay_jackson_1999]: https://doi.org/10.21236/ada369335
[research_bhagwandin_sahu_2011]: https://doi.org/10.2514/6.2011-3028
[research_bhagwandin_sahu_2013]: https://doi.org/10.21236/ada592550
[research_bhagwandin_sahu_2014]: https://doi.org/10.2514/1.a32734
[research_bhatia_beran_2017]: https://doi.org/10.2514/1.j055839
[research_bi_xie_2017]: https://doi.org/10.2514/6.2017-1349
[research_bian_li_2024]: https://doi.org/10.2139/ssrn.4916263
[research_biao_changlin_2024]: https://doi.org/10.1109/phm-beijing63284.2024.10874779
[research_biberman_bronin_1978]: https://doi.org/10.1007/bf01050539
[research_biberman_bronin_1978_b]: https://doi.org/10.1615/ihtc6.2820
[research_bigler_1986]: https://doi.org/10.2514/6.1986-9729
[research_bihrle_barnhart_1982]: https://doi.org/10.2514/3.44789
[research_bippes_1990]: https://doi.org/10.1007/978-3-642-84103-3_38
[research_birckelbaw_1992]: https://doi.org/10.2514/6.1992-2611
[research_birman_1989]: https://doi.org/10.2514/6.1989-1167
[research_bischoff_palmer_1982]: https://doi.org/10.2514/6.1982-1610
[research_bischoff_palmer_1983]: https://doi.org/10.21236/ada327418
[research_bisek_brown_2015]: https://doi.org/10.2514/6.2015-2802
[research_bishop_1951]: https://doi.org/10.1093/qmath/2.1.291
[research_bismarcknasr_1993]: https://doi.org/10.2514/3.49073
[research_bismarcknasr_bones_2000]: https://doi.org/10.2514/2.1014
[research_biswas_michels_2026]: https://doi.org/10.2514/6.2026-0511
[research_blachowski_ostrowski_2001]: https://doi.org/10.2514/6.2001-3635
[research_blaha_1969]: https://doi.org/10.2514/6.1969-427
[research_blair_edwards_1982]: https://doi.org/10.21236/ada126465
[research_blair_weisshaar_1982]: https://doi.org/10.2514/3.44806
[research_blake_gotwald_2009]: https://doi.org/10.2514/1.44911
[research_blanchard_raper_1960]: https://ntrs.nasa.gov/citations/19670022198
[research_blanchard_wilmoth_1996]: https://doi.org/10.2514/6.1996-2467
[research_blank_1995]: https://doi.org/10.2514/6.1995-1816
[research_blood_ivanov_2015]: https://doi.org/10.1109/aero.2015.7119246
[research_bloxsom_1958]: https://doi.org/10.2514/8.7403
[research_bloy_lea_1995]: https://doi.org/10.2514/3.46741
[research_blt_shuttle_2016]: https://ntrs.nasa.gov/citations/20160010109
[research_blue_low_1953]: https://ntrs.nasa.gov/citations/19930083810
[research_bochkarev_matveyenko_2008]: https://doi.org/10.7242/1999-6691/2008.1.3.24
[research_boehm_flick_2001]: https://doi.org/10.2514/6.2001-1372
[research_bogdnoff_1953]: https://doi.org/10.21236/ad0009823
[research_bogdonoff_kepler_1955]: https://doi.org/10.2514/8.3358
[research_bogucz_dirik_1988]: https://doi.org/10.2514/6.1988-3771
[research_bohlmann_eckstrom_1990]: https://doi.org/10.2514/3.25319
[research_bohnisch_braun_2026]: https://doi.org/10.1016/j.ast.2025.110763
[research_bohon_dixon_1964]: https://doi.org/10.2514/6.1964-1028
[research_boland_riley_1993]: https://doi.org/10.2514/6.1993-3648
[research_bolas_1929]: https://doi.org/10.1108/eb029094
[research_boling_zha_2021]: https://doi.org/10.2514/6.2021-1732
[research_bollech_kelly_1954]: https://ntrs.nasa.gov/citations/20090022756
[research_bolton_2014]: https://doi.org/10.1179/1878641314y.0000000007
[research_bolton_collins_1975]: https://doi.org/10.2514/3.59877
[research_bonavolonta_manoj_2024]: https://doi.org/10.2514/6.2024-2114
[research_bond_canfield_2008]: https://doi.org/10.2514/6.2008-139
[research_bonnema_smith_1988]: https://doi.org/10.2514/6.1988-2118
[research_booker_booker_1980]: https://doi.org/10.2172/5493673
[research_booker_booker_1980_b]: https://doi.org/10.2172/5493697
[research_booker_booker_1982]: https://doi.org/10.2172/5154547
[research_boothe_1971]: https://doi.org/10.2514/6.1971-771
[research_boskovic_bergstrom_2005]: https://doi.org/10.2514/6.2005-6340
[research_bosson_caisso_1993]: https://doi.org/10.2514/6.1993-1906
[research_bott_bradshaw_1998]: https://doi.org/10.2514/6.1998-531
[research_boustani_anugrah_2020]: https://doi.org/10.2514/6.2020-1050
[research_boustani_barad_2019]: https://doi.org/10.2514/6.2019-3279
[research_boustani_kenway_2022]: https://doi.org/10.2514/6.2022-0904
[research_bower_thomas_2018]: https://doi.org/10.2514/6.2018-4460
[research_bowers_1980]: https://doi.org/10.2514/6.1980-1158
[research_bowman_1967]: https://doi.org/10.21236/ad0649860
[research_bowman_1995]: https://doi.org/10.21236/ada297936
[research_bowmanjr_stough_1978]: https://doi.org/10.2514/6.1978-1477
[research_boyd_1965]: https://doi.org/10.2514/6.1965-752
[research_boyd_1977]: https://doi.org/10.21236/ada053640
[research_boyer_mcnamara_2016]: https://doi.org/10.2514/6.2016-1091
[research_bozack_1970]: https://doi.org/10.2514/6.1970-1208
[research_bozack_doerr_1981]: https://doi.org/10.2514/6.1981-2517
[research_bozeman_tai_2018]: https://doi.org/10.2514/6.2018-2063
[research_bradfield_thomasson_1966]: https://doi.org/10.2514/6.1966-1521
[research_bradley_johnston_1969]: https://doi.org/10.2514/6.1969-776
[research_bradley_sharp_2018]: https://doi.org/10.2514/6.2018-4865
[research_brady_brindley_1996]: https://ntrs.nasa.gov/citations/19970019705
[research_brady_smialek_1997]: https://ntrs.nasa.gov/citations/20050180496
[research_brandeau_1978]: https://doi.org/10.2514/6.1978-1460
[research_brandeau_gallon_2015]: https://doi.org/10.2514/6.2015-2129
[research_brandon_britt_1979]: https://ntrs.nasa.gov/citations/19790035682
[research_brandt_bons_2024]: https://doi.org/10.2514/6.2024-0693
[research_braslow_1966]: https://ntrs.nasa.gov/citations/19660020887
[research_braun_1959]: https://ntrs.nasa.gov/citations/19980232074
[research_brazzel_1963]: https://doi.org/10.21236/ad0423963
[research_brenckmann_1964]: https://doi.org/10.2514/6.1964-804
[research_brenner_thompson_2005]: https://ntrs.nasa.gov/citations/20050215401
[research_breshears_mccafferty_1966]: https://doi.org/10.2514/6.1966-949
[research_breshears_mccafferty_1967]: https://ntrs.nasa.gov/citations/19670048105
[research_brewster_2014]: https://doi.org/10.1115/1.4028442
[research_brice_sugano_1978]: https://doi.org/10.2514/6.1978-1446
[research_bridges_2008]: https://doi.org/10.2514/1.34919
[research_brincklow_montgomery_2021]: https://doi.org/10.2514/6.2021-0327
[research_brincklow_montgomery_2024]: https://doi.org/10.1017/aer.2024.21
[research_brinkman_1992]: https://doi.org/10.21236/ada389071
[research_brinkman_booker_1991]: https://doi.org/10.7449/1991/superalloys_1991_519_536
[research_brittain_1989]: https://ntrs.nasa.gov/citations/19900005218
[research_brociek_hetmaniok_2023]: https://doi.org/10.1016/j.applthermaleng.2022.119405
[research_brodrick_1962]: https://doi.org/10.21236/ad0286832
[research_brodsky_1970]: https://doi.org/10.21236/ad0716026
[research_bromfield_landry_2019]: https://doi.org/10.2514/6.2019-3612
[research_brooke_1957]: https://doi.org/10.21236/ad0154531
[research_brooks_1971]: https://doi.org/10.2514/6.1971-294
[research_brooks_gupta_2017]: https://doi.org/10.2514/6.2017-3325
[research_brooks_ransbury_2012]: https://doi.org/10.2514/6.2012-4496
[research_brooksjr_dejarnette_1970]: https://doi.org/10.2514/6.1970-1176
[research_brossard_balmain_2005]: https://doi.org/10.1007/s11085-005-5705-2
[research_brossard_bouchaud_2013]: https://doi.org/10.1007/s11085-013-9426-7
[research_brown_1989]: https://doi.org/10.2514/6.1989-2112
[research_brown_2022]: https://doi.org/10.1007/978-3-031-18207-5_3
[research_brownfield_badger_1960]: https://doi.org/10.21236/ad0247150
[research_brownlee_1963]: https://doi.org/10.2514/6.1963-228
[research_brundrett_nicoll_1972]: https://doi.org/10.1115/1.3449865
[research_bruner_1983]: https://doi.org/10.4271/830711
[research_brunner_1959]: https://doi.org/10.1115/1.4008191
[research_brunner_nerem_1970]: https://doi.org/10.2514/6.1970-1177
[research_brunton_noack_2020]: https://doi.org/10.1146/annurev-fluid-010719-060214
[research_bryson_1954]: https://doi.org/10.2514/8.2916
[research_bryson_edwards_1952]: https://doi.org/10.2514/8.2343
[research_brysonjr_1969]: https://doi.org/10.2514/6.1969-865
[research_buchanan_cayse_1988]: https://doi.org/10.2514/6.1988-2030
[research_buckingham_1914]: https://doi.org/10.1103/physrev.4.345
[research_buckmann_shimp_1989]: https://doi.org/10.2514/6.1989-2305
[research_buckmann_shrimp_1992]: https://doi.org/10.2514/3.23445
[research_buddcofortwashingtonpatechnicalcenter_1978]: https://doi.org/10.21236/ada076373
[research_buddhamatya_miranda_2026]: https://doi.org/10.2514/6.2026-2116
[research_bugala_2025]: https://doi.org/10.2478/tar-2025-0008
[research_bugala_payenskyy_2025]: https://doi.org/10.1108/aeat-05-2025-0183
[research_bugala_sznajder_2023]: https://doi.org/10.2478/tar-2023-0023
[research_bui_2013]: https://doi.org/10.2514/6.2013-3032
[research_bui_2016]: https://doi.org/10.2514/6.2016-3720
[research_bui_2018]: https://doi.org/10.2514/6.2018-3808
[research_bull_kidd_1955]: https://doi.org/10.21236/ad0106019
[research_buller_2017]: https://doi.org/10.1016/j.procs.2017.09.042
[research_burbank_collins_1962]: https://ntrs.nasa.gov/citations/19630001117
[research_burchamjr_burken_1994]: https://doi.org/10.2514/6.1994-2123
[research_burchamjr_maine_1993]: https://doi.org/10.2514/6.1993-1820
[research_burchamjr_pappas_1996]: https://doi.org/10.2514/6.1996-3742
[research_burdett_1946]: https://doi.org/10.2514/8.4117
[research_burdett_1947]: https://doi.org/10.2514/8.4136
[research_burkhart_1980]: https://doi.org/10.2514/6.1980-741
[research_burkicohen_2010]: https://doi.org/10.2514/6.2010-8008
[research_burkicohen_sparko_2008]: https://doi.org/10.2514/6.2008-6871
[research_burmeister_1994]: https://doi.org/10.1017/cbo9780511608346.011
[research_burns_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50005-1
[research_burns_ray_1967]: https://ntrs.nasa.gov/citations/19670019706
[research_burris_1966]: https://doi.org/10.2514/6.1966-741
[research_burris_hutchins_1970]: https://doi.org/10.2514/6.1970-904
[research_burstein_chinitz_1972]: https://doi.org/10.2514/6.1972-1146
[research_burt_1974]: https://doi.org/10.2514/6.1974-86
[research_burt_1975]: https://doi.org/10.2514/3.59795
[research_burton_kneelandjr_1981]: https://doi.org/10.2514/6.1981-2465
[research_burton_loth_2007]: https://doi.org/10.2514/6.2007-5841
[research_buschulte_1970]: https://doi.org/10.1007/978-94-011-7551-7_21
[research_buschulte_1971]: https://doi.org/10.2514/6.1971-740
[research_bushnell_tripi_1986]: https://doi.org/10.2514/6.1986-773
[research_busing_1964]: https://doi.org/10.1016/b978-0-08-011007-3.50012-3
[research_butler_1976]: https://doi.org/10.21236/ada032654
[research_butler_fleck_1983]: https://doi.org/10.21236/adb079184
[research_byrne_pickles_1990]: https://doi.org/10.1016/b978-0-08-040423-3.50022-7
[research_byrnes_1951]: https://doi.org/10.1016/0002-9394(51)90563-6
[research_cadieux_angel_2023]: https://doi.org/10.2514/6.2023-1336
[research_cadieux_barad_2024]: https://doi.org/10.2514/6.2024-4225
[research_cadieux_barad_2025]: https://doi.org/10.1016/j.compfluid.2025.106800
[research_cadieux_barad_2026]: https://doi.org/10.2514/6.2026-3810
[research_cagan_rosa_2015]: https://doi.org/10.4028/www.scientific.net/amm.732.199
[research_cai_tong_2005]: https://doi.org/10.2514/6.2005-3743
[research_calculation_of_2008]: https://doi.org/10.5139/jksas.2008.36.11.1039
[research_callaghan_mason_1964]: https://doi.org/10.1016/0009-2509(64)85087-9
[research_calligeros_dugundji_1963]: https://doi.org/10.2514/3.2033
[research_campbell_abramovitz_1975]: https://doi.org/10.2514/6.1975-1028
[research_campbell_berger_2012]: https://ntrs.nasa.gov/citations/20120016806
[research_campbell_gebler_1965]: https://ntrs.nasa.gov/citations/19660011729
[research_campbell_grauer]: https://ntrs.nasa.gov/citations/20205009996
[research_campbell_grauer_2021]: https://doi.org/10.2514/6.2021-0778
[research_campbell_grauer_2021_b]: https://ntrs.nasa.gov/citations/20205002641
[research_campo_ferrara_1982]: https://doi.org/10.1007/978-94-009-7907-9_23
[research_candida_souzadepaula_2019]: https://doi.org/10.26678/abcm.diname2019.din2019-0103
[research_candler_2001]: https://doi.org/10.21236/ada387503
[research_cano_sobel_2016]: https://doi.org/10.4236/eng.2016.84016
[research_cao_huang_2006]: https://doi.org/10.1007/s10483-006-0401-1
[research_cao_siqi_2026]: https://doi.org/10.2139/ssrn.7181668
[research_cao_yao_2019]: https://doi.org/10.3390/math7090787
[research_cao_yao_2020]: https://doi.org/10.22541/au.158594503.37165006
[research_carafoli_1969]: https://doi.org/10.1016/b978-0-08-012330-1.50005-4
[research_carafoli_1969_b]: https://doi.org/10.1016/b978-0-08-012330-1.50008-x
[research_carafoli_1969_c]: https://doi.org/10.1016/b978-0-08-012330-1.50009-1
[research_carbaugh_2008]: https://doi.org/10.2514/6.2008-6866
[research_carlin_blair_1983]: https://doi.org/10.2514/6.1983-2564
[research_carlson_1964]: https://doi.org/10.2514/6.1964-590
[research_carlson_nerem_1968]: https://doi.org/10.1016/0017-9310(68)90071-9
[research_carlson_schwope_1952]: https://doi.org/10.21236/ada076046
[research_carman_1970]: https://doi.org/10.2514/6.1970-207
[research_carpenter_saric_2008]: https://doi.org/10.2514/6.2008-7335
[research_carpenter_saric_2009]: https://doi.org/10.1007/978-90-481-3723-7_15
[research_carpentierirona_gonzalezramirez_2018]: https://doi.org/10.2514/6.2018-0604
[research_carr_1982]: https://doi.org/10.1007/978-1-4612-5929-9_5
[research_carrera_varello_2013]: https://doi.org/10.1007/s13272-013-0063-2
[research_carroll_2015]: https://doi.org/10.2514/6.2015-2902
[research_carroll_cabet_2011]: https://doi.org/10.1520/jai103797
[research_carroll_mehra_1982]: https://doi.org/10.2514/3.56198
[research_carter_stearman_1967]: https://doi.org/10.2514/6.1967-78
[research_carter_stearman_1968]: https://doi.org/10.2514/3.4438
[research_caruso_mendenhall_1992]: https://doi.org/10.2514/6.1992-403
[research_caruso_naegeli_1976]: https://ntrs.nasa.gov/citations/19760025417
[research_cary_1968]: https://ntrs.nasa.gov/citations/19680046144
[research_cassanova_1967]: https://doi.org/10.21236/ad0659372
[research_catalano_sturek_2001]: https://doi.org/10.21236/ada395936
[research_catalano_sturek_2001_b]: https://doi.org/10.21236/ada398641
[research_cavazzuti_2020]: https://doi.org/10.1016/j.ijheatmasstransfer.2020.119608
[research_cece_throttling_2007]: https://ntrs.nasa.gov/citations/20090028814
[research_cella_biancolini_2012]: https://doi.org/10.2514/1.c031293
[research_celmins_1990]: https://doi.org/10.21236/ada224217
[research_cen_li_2020]: https://doi.org/10.1177/0954410020944085
[research_cerantola_handford_2024]: https://doi.org/10.2514/6.2024-2295
[research_chai_li_2019]: https://doi.org/10.2514/1.j058307
[research_chai_li_2020]: https://doi.org/10.1016/j.ast.2020.106000
[research_chai_song_2017]: https://doi.org/10.1016/j.actaastro.2017.08.016
[research_chakravarty_1987]: https://doi.org/10.2514/6.1987-2257
[research_chakravarty_narayanaswamy_2025]: https://doi.org/10.2514/6.2025-1492
[research_chaku_mcmahon_1974]: https://doi.org/10.1007/bf02644112
[research_chaloner_verdinelli_1995]: https://doi.org/10.1214/ss/1177009939
[research_chalot_mallet_1994]: https://doi.org/10.2514/6.1994-814
[research_chalupova_steinbruck_2020]: https://doi.org/10.14311/app.2020.28.0008
[research_chambers_hall_2004]: https://doi.org/10.2514/1.4470
[research_chan_chang]: https://doi.org/10.17918/00000087
[research_chandiramani_plaut_1995]: https://doi.org/10.1007/bf02823212
[research_chandler_2023]: https://doi.org/10.2514/6.2023-1665
[research_chandler_2024]: https://doi.org/10.2514/6.2024-0996
[research_chandler_herrera_2025]: https://doi.org/10.2514/6.2025-0763
[research_chandler_herrera_2026]: https://doi.org/10.2514/6.2026-2756
[research_chandrashekhara_1991]: https://doi.org/10.2514/6.1991-915
[research_chang_1962]: https://doi.org/10.21236/ad0274359
[research_chang_1980]: https://doi.org/10.1115/1.3240622
[research_chang_kwatny_2008]: https://doi.org/10.2514/6.2008-6507
[research_chang_kwatny_2016]: https://doi.org/10.2514/6.2016-0880
[research_chang_lin_2012]: https://doi.org/10.1166/asl.2012.4090
[research_chang_nordheim_1953]: https://doi.org/10.21236/ad0000961
[research_chang_nottage_1961]: https://doi.org/10.1016/0016-0032(61)90605-6
[research_chao_jeng_1965]: https://doi.org/10.1115/1.3689076
[research_chapleo_nair_1994]: https://doi.org/10.2514/6.1994-812
[research_chapman_matting_1965]: https://ntrs.nasa.gov/citations/19650047518
[research_chapman_robb_2024]: https://doi.org/10.2514/6.2024-2648
[research_chapman_rubesin_1949]: https://doi.org/10.2514/8.11853
[research_chapter_3_1957]: https://doi.org/10.1515/9781400879908-005
[research_chapter_3_1960]: https://doi.org/10.1515/9781400874941-004
[research_chapter_4_1957]: https://doi.org/10.1515/9781400879908-010
[research_chapter_5_1957]: https://doi.org/10.1515/9781400879908-011
[research_charles_lowenberg_2002]: https://doi.org/10.2514/6.2002-4751
[research_chaudhuri_1977]: https://doi.org/10.21236/ada064016
[research_chaussee_enriquez_2026]: https://doi.org/10.2514/6.2026-2113
[research_chauvin_erb_1968]: https://doi.org/10.2514/6.1968-1142
[research_chauvin_speegle_1957]: https://ntrs.nasa.gov/citations/19660024020
[research_chavez_vogel_2003]: https://doi.org/10.1115/imece2003-42864
[research_chehroudi_2009]: https://doi.org/10.2514/6.2009-237
[research_chehroudi_2010]: https://doi.org/10.2514/1.38451
[research_chen_1971]: https://doi.org/10.2514/6.1971-166
[research_chen_1993]: https://ntrs.nasa.gov/citations/19930041520
[research_chen_blosser_2002]: https://doi.org/10.2514/6.2002-501
[research_chen_chang_1998]: https://doi.org/10.2514/6.1998-907
[research_chen_chen_2014]: https://doi.org/10.4028/www.scientific.net/amr.912-914.427
[research_chen_gray_2026]: https://doi.org/10.2514/6.2026-1489
[research_chen_khalid_2001]: https://doi.org/10.2514/6.2001-2485
[research_chen_wu_2026]: https://doi.org/10.1063/5.0348275
[research_chen_xie_2024]: https://doi.org/10.1088/1742-6596/2882/1/012003
[research_chen_zhao_2005]: https://doi.org/10.2514/6.2005-3741
[research_chen_zhao_2019]: https://doi.org/10.1155/2019/8384639
[research_chen_zhu_2024]: https://doi.org/10.2139/ssrn.5009866
[research_cheng_1956]: https://doi.org/10.2514/8.6930
[research_cheng_1982]: https://doi.org/10.1016/b978-0-12-493280-7.50010-3
[research_cheng_1985]: https://doi.org/10.1007/978-1-4684-4298-4_13
[research_cheng_fan_2016]: https://doi.org/10.1016/j.corsci.2016.07.010
[research_cheng_farmer_2002]: https://doi.org/10.2514/6.2002-785
[research_cheng_fu_2024]: https://doi.org/10.1017/jfm.2024.981
[research_cheng_lee_2003]: https://doi.org/10.2514/2.3116
[research_cheng_li_2016]: https://doi.org/10.1080/00102202.2016.1248238
[research_cheng_li_2018]: https://doi.org/10.2514/1.b36799
[research_cheng_mei_2000]: https://doi.org/10.2514/6.2000-1335
[research_cheng_mei_2002]: https://doi.org/10.2514/6.2002-1285
[research_cheng_pellettiere_2005]: https://doi.org/10.4271/2005-01-3263
[research_cheng_rizer_2003]: https://doi.org/10.4271/2003-01-3001
[research_chern_lobser_2014]: https://doi.org/10.2514/6.2014-0437
[research_chew_1973]: https://doi.org/10.21236/ad0764730
[research_chiang_1980]: https://doi.org/10.21236/ada092721
[research_chiaverini_malecki_2002]: https://doi.org/10.2514/6.2002-4149
[research_childs_1974]: https://doi.org/10.2514/6.1974-1078
[research_childs_moyer_1985]: https://doi.org/10.1115/1.3239676
[research_chin_turpin_2020]: https://doi.org/10.2514/1.c035749
[research_chinnaraj_kim_2024]: https://doi.org/10.3390/ma17215229
[research_chipman_zislin_1982]: https://doi.org/10.2514/6.1982-684
[research_chiu_1987]: https://doi.org/10.2514/6.1987-2033
[research_chiu_lin_1994]: https://doi.org/10.2514/3.46643
[research_cho_chang_2001]: https://doi.org/10.1016/s0045-7930(00)00010-4
[research_cho_findley_1983]: https://doi.org/10.21236/ada137976
[research_cho_kim_2004]: https://doi.org/10.1016/j.cryogenics.2004.02.009
[research_choi_lim_2020]: https://doi.org/10.5139/jksas.2020.48.8.555
[research_chopra_1975]: https://doi.org/10.2514/3.49789
[research_chorunov_2011]: https://doi.org/10.1080/09507111003655127
[research_chou_childs_1983]: https://doi.org/10.2514/6.1983-1672
[research_chou_kalina_1982]: https://doi.org/10.1615/ihtc7.1610
[research_chou_smith_1974]: https://doi.org/10.21236/ada001135
[research_chou_smith_1978]: https://doi.org/10.2514/6.1978-1359
[research_choudhary_2012]: https://doi.org/10.1515/htmp.2011.125
[research_chow_1963]: https://doi.org/10.2514/3.1772
[research_chow_1979]: https://doi.org/10.21236/ada071899
[research_chowdhury_keshmiri_2021]: https://doi.org/10.1109/icuas51884.2021.9476811
[research_chu_xu_2014]: https://doi.org/10.2514/6.2014-3416
[research_chuan_feng_2016]: https://doi.org/10.2514/6.2016-0513
[research_chuban_2020]: https://doi.org/10.1615/tsagiscij.2020034274
[research_chung_chung_2008]: https://doi.org/10.2514/6.2008-6868
[research_chuvakhov_2020]: https://doi.org/10.1134/s0015462820010048
[research_chyrkin_huczkowski_2010]: https://doi.org/10.1007/s11085-010-9225-3
[research_chyrkin_sloof_2015]: https://doi.org/10.1179/0960340914z.00000000082
[research_ciliberti_dellavecchia_2017]: https://doi.org/10.1016/j.paerosci.2017.11.001
[research_ciliberti_nicolosi_2025]: https://doi.org/10.1186/s42774-024-00189-x
[research_clark_1967]: https://doi.org/10.2514/6.1967-441
[research_clark_adler_2016]: https://doi.org/10.1109/aero.2016.7500618
[research_clark_gallon_2015]: https://doi.org/10.2514/6.2015-2130
[research_clark_jones_2007]: https://ntrs.nasa.gov/citations/20070038953
[research_clark_manning_2015]: https://doi.org/10.2514/6.2015-2100
[research_clarke_1980]: https://doi.org/10.1016/0017-9310(80)90079-4
[research_clarke_allen_2005]: https://doi.org/10.2514/6.2005-6316
[research_clarkson_1935]: https://doi.org/10.1017/s0368393100111575
[research_clay_2004]: https://doi.org/10.2514/1.3880
[research_coats_1973]: https://doi.org/10.21236/ad0755843
[research_cockbill_2018]: https://doi.org/10.1063/1.5041743
[research_coetzee_krauskopf_2013]: https://doi.org/10.2514/1.c031883
[research_coldwall_descent_1975]: https://ntrs.nasa.gov/citations/19750016601
[research_cole_1990]: https://doi.org/10.2514/6.1990-981
[research_coleburn_drimmer_1961]: https://doi.org/10.21236/ad0326783
[research_coleburn_drimmer_1962]: https://doi.org/10.21236/ad0329109
[research_coleman_hodge_1983]: https://doi.org/10.21236/ada141943
[research_coleman_lobbia_2026]: https://doi.org/10.2514/6.2026-3855
[research_coleman_taylor_1989]: https://doi.org/10.21236/ada212099
[research_collar_1946]: https://doi.org/10.1017/s0368393100120358
[research_collier_1994]: https://doi.org/10.2514/6.1994-1579
[research_collier_bartlett_1990]: https://doi.org/10.1007/978-3-642-84103-3_30
[research_collier_johnson_1987]: https://ntrs.nasa.gov/citations/19900003242
[research_collins_martinez_1990]: https://doi.org/10.2514/6.1990-2231
[research_combustion_characteristics_2005]: https://doi.org/10.5139/jksas.2005.33.6.064
[research_combustion_instability_1995]: https://doi.org/10.2514/5.9781600866371.0475.0502
[research_combustion_instability_2007]: https://doi.org/10.2514/5.9781600866876.0351.0412
[research_compensated_high_1994]: https://ntrs.nasa.gov/citations/19950018205
[research_compressible_turbulent_1970]: https://doi.org/10.2514/6.1970-742
[research_compton_cooper_1965]: https://ntrs.nasa.gov/citations/19650016996
[research_computational_aerodynamic_1994]: https://doi.org/10.2514/6.1994-395
[research_comtois_glaser_2010]: https://doi.org/10.2514/6.2010-7798
[research_cone_heat_transfer_1961]: https://ntrs.nasa.gov/citations/19980235513
[research_config_stability_1956]: https://ntrs.nasa.gov/citations/19930089016
[research_connelly_1982]: https://doi.org/10.21236/ada120473
[research_connors_sachs_1957]: https://doi.org/10.21236/ad0124308
[research_connors_swaim_1968]: https://doi.org/10.2514/6.1968-59
[research_conrad_1959]: https://doi.org/10.1115/1.4008574
[research_contreras_fontanetta_2026]: https://doi.org/10.2514/6.2026-0983
[research_control_effectors_1990]: https://ntrs.nasa.gov/citations/19900012418
[research_coogan_2015]: https://doi.org/10.2514/6.2015-3762
[research_cook_1985]: https://doi.org/10.1080/02619180.1985.11753293
[research_cook_2007]: https://doi.org/10.1016/b978-075066927-6/50016-7
[research_cook_2013]: https://doi.org/10.2514/6.2013-1353
[research_cook_richards_1977]: https://doi.org/10.2514/3.7419
[research_cookson_1976]: https://doi.org/10.21236/ada035309
[research_cooled_honeycomb_1978]: https://ntrs.nasa.gov/citations/19780014460
[research_cooling_hypersonic_1991]: https://ntrs.nasa.gov/citations/19920035219
[research_cooper_wells_1970]: https://doi.org/10.4271/700794
[research_corda_neal_1998]: https://ntrs.nasa.gov/citations/19980223961
[research_coronasanchez_rodriguezcortes_2015]: https://doi.org/10.1109/icuas.2015.7152381
[research_cosens_newton_1988]: https://doi.org/10.2514/6.1988-3309
[research_costigan_calico_1989]: https://doi.org/10.2514/6.1989-17
[research_cosyn_vierendeels_2005]: https://doi.org/10.2514/6.2005-4609
[research_coupling_history_1997]: https://ntrs.nasa.gov/citations/19970019603
[research_covell_hernandez_1990]: https://doi.org/10.2514/6.1990-3210
[research_covell_walker_1992]: https://ntrs.nasa.gov/citations/19920015734
[research_covington_1966]: https://doi.org/10.2514/6.1966-441
[research_cox_2010]: https://doi.org/10.2514/6.2010-8002
[research_cox_cunningham_2012]: https://doi.org/10.2514/6.2012-5029
[research_craig_erbug_1976]: https://doi.org/10.1016/0045-7949(76)90049-3
[research_craigjr_1971]: https://doi.org/10.2514/6.1971-330
[research_craley_desabrais_2007]: https://doi.org/10.2514/6.2007-2575
[research_crasta_khan_2014]: https://doi.org/10.9790/5728-10530108
[research_creep_2024t3_1955]: https://ntrs.nasa.gov/citations/19930093819
[research_creep_2024t3_1957]: https://ntrs.nasa.gov/citations/19930092300
[research_creep_and_1981]: https://doi.org/10.1016/0010-4361(81)90474-2
[research_creep_rupture_2004]: https://doi.org/10.31399/asm.tb.aacppa.t51140243
[research_creep_rupture_2009]: https://doi.org/10.31399/asm.tb.fdmht.t52060021
[research_creep_rupture_superalloy_1993]: https://ntrs.nasa.gov/citations/19930036559
[research_creep_single_crystal_1985]: https://ntrs.nasa.gov/citations/19850045661
[research_crespo_kenny_2012]: https://doi.org/10.2514/6.2012-5026
[research_crew_escape]: https://doi.org/10.1007/978-0-387-73979-3_4
[research_crew_escape_2003]: https://doi.org/10.1108/aeat.2003.12775cab.033
[research_crider_2004]: https://doi.org/10.2514/6.2004-6293
[research_crider_2008]: https://doi.org/10.2514/6.2008-6864
[research_crider_2010]: https://doi.org/10.1017/s0001924000004103
[research_crider_2010_b]: https://doi.org/10.2514/6.2010-8003
[research_crittenden_weishaar_1978]: https://doi.org/10.2514/3.58383
[research_crittenden_weisshaar_1977]: https://doi.org/10.2514/6.1977-454
[research_crocco_1951]: https://doi.org/10.2514/8.4393
[research_crocco_1952]: https://doi.org/10.2514/8.4410
[research_crocco_1965]: https://doi.org/10.1016/s0082-0784(65)80249-1
[research_crocco_cheng_1953]: https://doi.org/10.2514/8.4623
[research_crocco_grey_1960]: https://doi.org/10.2514/8.5020
[research_crocco_harrje_1962]: https://doi.org/10.2514/8.6022
[research_crosby_griffith_1969]: https://doi.org/10.4050/vfs-f25-007
[research_crothers_1997]: https://doi.org/10.21236/ada343061
[research_crown_heybey_1950]: https://doi.org/10.21236/ad0058088
[research_cui_lundin_2004]: https://doi.org/10.1007/s11661-004-0198-1
[research_culick_jahnke_1988]: https://ntrs.nasa.gov/citations/19880063395
[research_cummings_adams_1982]: https://doi.org/10.21236/ada115424
[research_cunis]: https://doi.org/10.70675/5f4b14cez5181z4604zaf8dz27dc1744e316
[research_cunis_2025]: https://doi.org/10.1007/978-3-031-82681-8_8
[research_cunis_liaomcpherson_2020]: https://doi.org/10.1109/ccta41146.2020.9206158
[research_cunningham_1972]: https://doi.org/10.2514/3.50310
[research_cunningham_2017]: https://doi.org/10.2514/6.2017-1651
[research_currao_yeh_2026]: https://doi.org/10.2139/ssrn.6450319
[research_curry_mendenhall_1992]: https://ntrs.nasa.gov/citations/19920022564
[research_curry_sim_1982]: https://doi.org/10.2514/6.1982-1329
[research_curtiss_1971]: https://doi.org/10.2514/3.59098
[research_czarnecki_deveikis_1968]: https://ntrs.nasa.gov/citations/19680023582
[research_d]: https://doi.org/10.32657/10356/62132
[research_dahiya_2017]: https://doi.org/10.26438/ijcse/v5i9.2126
[research_dahm_1966]: https://doi.org/10.2172/4536140
[research_dai_zhao_2023]: https://doi.org/10.2514/1.t6675
[research_daidzic_tropea_1991]: https://doi.org/10.2514/6.1991-2280
[research_daniels_masuda_1956]: https://doi.org/10.21236/ad0102409
[research_danowsky_thompson_2008]: https://doi.org/10.2514/6.2008-6370
[research_dantsker_ananda_2017]: https://doi.org/10.2514/6.2017-4078
[research_darden_1984]: https://doi.org/10.2514/6.1984-138
[research_daryabeigi_2001]: https://doi.org/10.2514/6.2001-2834
[research_das_2026]: https://doi.org/10.2514/6.2026-112783
[research_das_venkatraman_2021]: https://doi.org/10.2514/6.2021-0730
[research_datta_wiltsee]: https://doi.org/10.1109/rams.2006.1677429
[research_davidescu_andrei_2026]: https://doi.org/10.13111/2066-8201.2026.18.2.3
[research_davidson_andrisani_1996]: https://ntrs.nasa.gov/citations/19970008392
[research_davies_parker_2024]: https://doi.org/10.1115/pvp2024-122668
[research_davis]: https://doi.org/10.15368/theses.2018.158
[research_davis_1957]: https://doi.org/10.2514/8.3998
[research_davis_1964]: https://doi.org/10.21236/ad0606108
[research_davis_bendiksen_1993]: https://doi.org/10.2514/6.1993-1476
[research_davis_fluggelotz_1964]: https://doi.org/10.1016/0017-9310(64)90110-3
[research_davis_marshall_2020]: https://doi.org/10.2514/6.2020-1748
[research_davis_pedrazzani_2015]: https://doi.org/10.2514/6.2015-1922
[research_day_guthrie_1958]: https://doi.org/10.21236/ad0339907
[research_deangelis_1991]: https://ntrs.nasa.gov/citations/19920068783
[research_deans_1964]: https://ntrs.nasa.gov/citations/19650029856
[research_debieve_dupont_1997]: https://doi.org/10.2514/2.86
[research_debrestian_anderson_1994]: https://doi.org/10.2514/3.522
[research_dec_mitcheltree_2002]: https://doi.org/10.2514/6.2002-910
[research_decarvalhopereira_junior_2003]: https://doi.org/10.4271/2003-01-3587
[research_dechant_1998]: https://doi.org/10.1016/s0142-727x(98)10010-3
[research_deepa_gupta_2023]: https://doi.org/10.61653/joast.v65i2.2013.727
[research_deere_viken_2024]: https://ntrs.nasa.gov/citations/20230010662
[research_defilippis_serpico_1998]: https://doi.org/10.2514/2.6386
[research_definitions_of_2007]: https://doi.org/10.1016/b978-075066927-6/50019-2
[research_defries_1971]: https://doi.org/10.21236/ad0726952
[research_degani_smits_1985]: https://ntrs.nasa.gov/citations/19850058654
[research_degischer_aigner_1987]: https://doi.org/10.1007/978-94-009-1347-9_47
[research_degregoria_2015]: https://doi.org/10.21236/ad1003573
[research_dehua_jinjun_2006]: https://doi.org/10.2514/1.20160
[research_delcher_dergevorkian_1989]: https://doi.org/10.2514/6.1989-2416
[research_dellavecchia_nicolosi_2015]: https://doi.org/10.2514/6.2015-2255
[research_demelo_bussamra_2024]: https://doi.org/10.1007/s40430-024-05077-5
[research_demetriades_1977]: https://doi.org/10.21236/ada049535
[research_demetriades_1983]: https://doi.org/10.21236/ada137056
[research_demetriades_1985]: https://doi.org/10.21236/ada179580
[research_demetriades_mccullough_1985]: https://doi.org/10.1017/s0022112085002166
[research_demingzhang_guiqingchen]: https://doi.org/10.1109/isscaa.2006.1627654
[research_demiyanenko_dmitrenko_2004]: https://doi.org/10.2514/6.2004-3685
[research_demjanenko_dmitrenko_2003]: https://doi.org/10.2514/6.2003-5072
[research_dempers_nikbin_1999]: https://doi.org/10.4028/www.scientific.net/kem.171-174.153
[research_dempster_arnold_1969]: https://doi.org/10.2514/3.44062
[research_dempster_roger_1967]: https://doi.org/10.2514/3.43878
[research_deng_liu_2024]: https://doi.org/10.1142/s0219455425501901
[research_deng_qin_2024]: https://doi.org/10.2139/ssrn.4939437
[research_deng_wang_2023]: https://doi.org/10.1088/1742-6596/2472/1/012001
[research_denicola_tognaccini_1994]: https://doi.org/10.2514/6.1994-1821
[research_densification_of_2003]: https://doi.org/10.1016/s0026-0657(03)80361-2
[research_depaula_porto_2017]: https://doi.org/10.2514/6.2017-1759
[research_derkevorkian_avery_2019]: https://doi.org/10.2514/6.2019-3276
[research_desclers_sternberg_1952]: https://doi.org/10.2514/8.2411
[research_design_of_1992]: https://doi.org/10.2514/5.9781600866197.0155.0218
[research_despirito_2009]: https://doi.org/10.21236/ada508090
[research_despirito_2013]: https://doi.org/10.21236/ada592880
[research_despirito_2014]: https://doi.org/10.21236/ada606669
[research_despirito_2015]: https://doi.org/10.21236/ada619525
[research_despirito_silton_2008]: https://doi.org/10.2514/6.2008-214
[research_detullio_paredes_2013]: https://doi.org/10.1017/jfm.2013.520
[research_devan_1989]: https://doi.org/10.2514/6.1989-2195
[research_development_of_1997]: https://ntrs.nasa.gov/citations/20050177117
[research_development_of_2008]: https://doi.org/10.5139/jksas.2008.36.11.1132
[research_development_of_2014]: https://doi.org/10.2514/5.9781624102547.0661.0664
[research_development_of_2024]: https://doi.org/10.2514/5.9781624107252.0731.0734
[research_dewa_park_2018]: https://doi.org/10.3390/met8020103
[research_dhosi_widmer_1963]: https://doi.org/10.21236/ad0426476
[research_dhosi_widmer_1964]: https://doi.org/10.21236/ad0600903
[research_diaz_1985]: https://ntrs.nasa.gov/citations/19860003902
[research_dicarlo_brown_1992]: https://doi.org/10.2514/6.1992-4094
[research_diggins_1951]: https://doi.org/10.21236/ad0895227
[research_dikbas_atik_2018]: https://doi.org/10.2514/6.2018-4127
[research_dillinger_abdalla_2019]: https://doi.org/10.1007/s13272-019-00397-y
[research_dillman_stanley_2003]: https://doi.org/10.22488/okstate.18.100316
[research_dillon_king_1990]: https://doi.org/10.2514/6.1990-234
[research_dimitrienko_koryakov_2015]: https://doi.org/10.12988/ams.2015.55405
[research_din_egorov_2018]: https://doi.org/10.1134/s0015462818050063
[research_ding_findley_1982]: https://doi.org/10.21236/ada125023
[research_ding_subramaniam_1989]: https://doi.org/10.1016/b978-0-08-040182-9.50088-6
[research_dirling_rigdon_1970]: https://ntrs.nasa.gov/citations/19700009521
[research_disselkoen_heise_1989]: https://doi.org/10.2514/3.45834
[research_dissimilar_joints_1990]: https://ntrs.nasa.gov/citations/19900000598
[research_dixon_mei_1993]: https://doi.org/10.2514/3.11606
[research_dmitrenko_2019]: https://doi.org/10.17654/hm018020463
[research_dobosbubno_hartsook_1977]: https://doi.org/10.21236/ada062008
[research_doengi_dinkler_1995]: https://doi.org/10.2514/6.1995-1078
[research_dogankuzey_yildirimdalkiran_2026]: https://doi.org/10.1108/aeat-08-2025-0283
[research_doggettjr_soistmann_1989]: https://doi.org/10.2514/6.1989-1325
[research_doherr_2003]: https://doi.org/10.2514/6.2003-2173
[research_dolan_1964]: https://doi.org/10.2514/6.1964-806
[research_dolan_1970]: https://doi.org/10.2514/6.1970-277
[research_dolgih_2025]: https://doi.org/10.18287/2409-4579-2025-11-2-46-55
[research_dombrovsky_reviznikov_2014]: https://doi.org/10.1615/ihtc15.rad.008214
[research_dombrovsky_reviznikov_2016]: https://doi.org/10.1016/j.ijheatmasstransfer.2015.10.072
[research_donahue_2004]: https://doi.org/10.2514/1.9200
[research_dong_fan_1998]: https://doi.org/10.1115/imece1998-0722
[research_dong_huang_2023]: https://doi.org/10.2139/ssrn.4622102
[research_dong_lu_2023]: https://doi.org/10.1016/j.surfcoat.2023.129608
[research_dong_shin_2011]: https://doi.org/10.1166/asl.2011.1696
[research_dongi_dinkler_1996]: https://doi.org/10.2514/3.13216
[research_dongmo_2011]: https://doi.org/10.2514/6.2011-1562
[research_dongmo_2011_b]: https://doi.org/10.2514/6.2011-6305
[research_dongmo_2012]: https://doi.org/10.2514/6.2012-4545
[research_dongmo_2012_b]: https://doi.org/10.2514/6.2012-4548
[research_dongmo_2015]: https://doi.org/10.2514/6.2015-1542
[research_dongmo_2015_b]: https://doi.org/10.2514/6.2015-1543
[research_dongmo_2016]: https://doi.org/10.2514/6.2016-0402
[research_dongmo_2017]: https://doi.org/10.2514/6.2017-1019
[research_donovan_smits_1990]: https://doi.org/10.2514/6.1990-19
[research_dorosh_leontiev_2014]: https://doi.org/10.7463/1214.0740931
[research_dorrance_1961]: https://doi.org/10.2514/8.5385
[research_dorrance_dore_1954]: https://doi.org/10.2514/8.3050
[research_doubrava_waszniowski_2008]: https://doi.org/10.2514/6.2008-6527
[research_dougherty_fisher_1980]: https://ntrs.nasa.gov/citations/19800038567
[research_douglasaircraftcolongbeachca_1983]: https://doi.org/10.21236/ada133628
[research_dovgal_levchenko_1990]: https://doi.org/10.1007/978-3-642-84103-3_9
[research_dowell_1964]: https://doi.org/10.2514/3.2669
[research_dowell_1964_b]: https://doi.org/10.2514/6.1964-92
[research_dowell_1970]: https://doi.org/10.2514/3.5680
[research_dowell_1970_b]: https://doi.org/10.2514/6.1970-76
[research_dowell_1972]: https://doi.org/10.2514/6.1972-350
[research_dowell_1983]: https://doi.org/10.21236/ada135133
[research_dowell_1996]: https://doi.org/10.21236/ada325524
[research_dowell_1999]: https://doi.org/10.21236/ada362982
[research_dowell_bendiksen_2010]: https://doi.org/10.1002/9780470686652.eae152
[research_dowell_katz_1990]: https://doi.org/10.2514/3.10453
[research_dowell_voss_1964]: https://doi.org/10.2514/6.1964-491
[research_dreshfield_1996]: https://doi.org/10.7449/1996/superalloys_1996_383_389
[research_dresia_adler_2023]: https://doi.org/10.2514/6.2023-0137
[research_dress_boyden_1992]: https://doi.org/10.2514/6.1992-5009
[research_dress_boyden_1994]: https://doi.org/10.2514/3.46536
[research_dressler_2006]: https://doi.org/10.2514/6.2006-5220
[research_driftmyer_1988]: https://doi.org/10.2514/6.1988-2023
[research_dris_jamal_2019]: https://doi.org/10.1109/isacs48493.2019.9068904
[research_driscoll_1966]: https://doi.org/10.4271/660220
[research_driver_1958]: https://ntrs.nasa.gov/citations/19980232000
[research_driver_1974]: https://doi.org/10.2514/6.1974-987
[research_dryden_hwts_thermal_1990]: https://ntrs.nasa.gov/citations/19940004702
[research_du_2013]: https://doi.org/10.4028/www.scientific.net/amm.390.57
[research_du_2017]: https://doi.org/10.26226/morressier.59c106e9d462b80292389e5d
[research_du_he_2026]: https://doi.org/10.1016/j.actaastro.2025.08.039
[research_du_liu_2025]: https://doi.org/10.22541/au.175549325.55054671/v1
[research_duan_he_2014]: https://doi.org/10.1016/j.icheatmasstransfer.2014.04.022
[research_duan_mei_2001]: https://doi.org/10.2514/6.2001-1659
[research_duan_wan_2026]: https://doi.org/10.3390/aerospace13010096
[research_dubois_habiballah_1991]: https://doi.org/10.2514/6.1991-1860
[research_dubois_habiballah_1995]: https://doi.org/10.2514/6.1995-607
[research_ducros_comte_1995]: https://doi.org/10.1007/978-3-642-78823-9_18
[research_dugundji_1965]: https://doi.org/10.21236/ad0624995
[research_dugundji_1966]: https://doi.org/10.2514/3.3657
[research_dukeman_2002]: https://doi.org/10.2514/6.2002-4559
[research_dukhnovskiy_lobkovskiy_2023]: https://doi.org/10.1007/978-981-19-9010-6_15
[research_dunning_1957]: https://ntrs.nasa.gov/citations/19930089807
[research_dupuis_1988]: https://doi.org/10.2514/6.1988-4378
[research_dutoi_richards_2008]: https://doi.org/10.2514/6.2008-6502
[research_dwivedi_1983]: https://doi.org/10.1080/02619180.1983.11753202
[research_dynamic_lateral_directional_2003]: https://doi.org/10.2514/5.9781600861840.0311.0322
[research_dynamic_stability]: https://doi.org/10.1007/978-3-540-46573-7_11
[research_e_fan_2026]: https://doi.org/10.3390/mi17101163
[research_eaton_graefe_1952]: https://doi.org/10.21236/ad0002911
[research_ebenezer_koteswararao_2022]: https://doi.org/10.1016/j.matpr.2022.03.595
[research_eberhart_lineberry_2012]: https://doi.org/10.2514/6.2012-4204
[research_eckert_1956]: https://doi.org/10.1115/1.4014011
[research_eckles_slater_1975]: https://doi.org/10.2514/6.1975-1054
[research_edquist_mahzari]: https://ntrs.nasa.gov/citations/20220007618
[research_edwards_1992]: https://doi.org/10.2514/6.1992-4002
[research_edwards_2014]: https://doi.org/10.21236/ada605092
[research_edwards_constantin_2024]: https://doi.org/10.2514/6.2024-4275
[research_edwards_constantin_2025]: https://doi.org/10.2514/1.t7070
[research_effect_of_1959]: https://doi.org/10.1016/0043-1648(59)90190-5
[research_effects_of_1968]: https://doi.org/10.1111/j.1559-3584.1968.tb04566.x
[research_effects_of_1979]: https://doi.org/10.2514/5.9781600865381.0003.0021
[research_effects_of_1980]: https://doi.org/10.2514/5.9781600865435.0247.0268
[research_eftekhari_siroueinejad_2025]: https://doi.org/10.1134/s0025654425602496
[research_egorov_2025]: https://doi.org/10.7868/s3034508125030077
[research_egorov_fedorov_2018]: https://doi.org/10.1615/tsagiscij.2018028749
[research_ehlers_epton_1978]: https://doi.org/10.2514/6.1978-15
[research_ehlers_johnson_1976]: https://doi.org/10.2514/6.1976-381
[research_ehlers_weisshaar_1993]: https://doi.org/10.1117/12.152754
[research_eisawy_shatynski_1982]: https://doi.org/10.1080/02619180.1982.11753190
[research_ejection_seat_2003]: https://doi.org/10.2307/jj.36105931.18
[research_ejection_seat_2015]: https://doi.org/10.2307/jj.18376951.108
[research_ejection_seat_2021]: https://doi.org/10.12968/s1478-2774(22)50457-3
[research_ekimogloy_stelk_2026]: https://doi.org/10.2514/6.2026-112651
[research_ekoto_bowersox_2007]: https://doi.org/10.2514/6.2007-1142
[research_ekvall_rainen_1989]: https://doi.org/10.2514/6.1989-1407
[research_ekvall_rainen_1990]: https://doi.org/10.2514/3.45944
[research_elevated_temperature_properties_1990]: https://doi.org/10.31399/asm.hb.v01.a0001035
[research_elevated_temperature_properties_1990_b]: https://doi.org/10.31399/asm.hb.v01.a0001048
[research_elevated_tensile_practice_1960]: https://ntrs.nasa.gov/citations/19980227092
[research_elgallad_chen_2023]: https://doi.org/10.1007/s11665-023-08306-5
[research_elghobashi_wassel_1980]: https://doi.org/10.1016/0017-9310(80)90053-8
[research_ellen_1968]: https://doi.org/10.2514/3.4951
[research_ellen_1969]: https://doi.org/10.2514/3.5153
[research_ellerbrock_ziegenhagen_2006]: https://doi.org/10.1016/j.actaastro.2006.04.013
[research_ellison_1969]: https://ntrs.nasa.gov/citations/19690013192
[research_elramly]: https://doi.org/10.22215/etd/1975-00290
[research_elshazly_kassem_2025]: https://doi.org/10.1088/1742-6596/3070/1/012001
[research_elson_lingard_1997]: https://doi.org/10.2514/6.1997-1548
[research_energy_analysis_1991]: https://doi.org/10.2514/5.9781600866104.0143.0235
[research_engelbrecht]: https://doi.org/10.31274/rtd-180813-14663
[research_engelbrecht_pauck_2013]: https://doi.org/10.2514/6.2013-5172
[research_england]: https://doi.org/10.23860/diss-4284
[research_engstrom_lang_1961]: https://doi.org/10.21236/ad0266714
[research_ennis_schuster_1995]: https://doi.org/10.1080/09603409.1995.11689504
[research_eppink_2023]: https://doi.org/10.2514/6.2023-3999
[research_epstein_1954]: https://doi.org/10.21236/ad0037709
[research_epstein_srinivasan_1994]: https://doi.org/10.2514/6.1994-1488
[research_ericksen_pepper_1984]: https://doi.org/10.2514/6.1984-813
[research_erickson_schreiner_1990]: https://doi.org/10.2514/6.1990-2814
[research_erickson_schreiner_1990_b]: https://doi.org/10.2514/6.1990-3023
[research_ericsson_1986]: https://doi.org/10.2514/6.1986-1773
[research_ericsson_2001]: https://doi.org/10.2514/2.2855
[research_erlebacher_hussaini_1990]: https://doi.org/10.1007/978-3-642-84103-3_59
[research_esdu_data_1998]: https://doi.org/10.1108/aeat.1998.12770fab.033
[research_essouni_2000]: https://doi.org/10.1016/s1044-5803(00)00069-3
[research_essouni_2001]: https://doi.org/10.1016/s1044-5803(01)00136-x
[research_etherington_kramer_2020]: https://ntrs.nasa.gov/citations/20200002795
[research_evensen_1976]: https://doi.org/10.2514/3.7275
[research_experience_gained_2010]: https://doi.org/10.2514/5.9781600867552.0443.0543
[research_experimental_dynamic_2025]: https://doi.org/10.47176/jafm.18.5.2854
[research_failure_by_2019]: https://doi.org/10.31399/asm.fach.aero.c0006387
[research_fallis_1953]: https://doi.org/10.2514/8.2775
[research_fan_2015]: https://doi.org/10.4028/www.scientific.net/amr.1091.103
[research_fan_liu_2017]: https://doi.org/10.2514/6.2017-1721
[research_farhat_2001]: https://doi.org/10.21236/ada397705
[research_faroughi_malekzadeh_2012]: https://doi.org/10.1177/1077546312455211
[research_farvin_peddieson_1988]: https://doi.org/10.1016/0895-7177(88)90557-2
[research_fasel_husmeier_2008]: https://doi.org/10.21236/ada482024
[research_fasel_sandberg_2006]: https://doi.org/10.21236/ada459372
[research_fatuev_2006]: https://doi.org/10.2514/6.iac-06-c4.p.1.05
[research_favor_achbach_1957]: https://doi.org/10.21236/ad0142069
[research_fay_kemp_1963]: https://doi.org/10.21236/ad0405723
[research_fay_riddell_1958]: https://doi.org/10.2514/8.7517
[research_fejer_heath_1964]: https://doi.org/10.21236/ad0603313
[research_feldman_1987]: https://doi.org/10.21236/ada302261
[research_feldman_bahder_1989]: https://doi.org/10.21236/ada310380
[research_feldwisch_schulze_2021]: https://doi.org/10.1007/978-3-030-79561-0_50
[research_feng_cheng_2009]: https://doi.org/10.2514/6.2009-4864
[research_feng_wang_2008]: https://doi.org/10.1109/aim.2008.4601822
[research_fenn_1962]: https://doi.org/10.1520/stp46992s
[research_ferraiuolo_manca_2009]: https://doi.org/10.1115/imece2009-12327
[research_ferraiuolo_manca_2012]: https://doi.org/10.1016/j.ijthermalsci.2011.10.019
[research_ferranti_wan_2015]: https://doi.org/10.1016/j.ifacol.2015.11.278
[research_ferrari_1948]: https://doi.org/10.2514/8.11582
[research_ferrari_1955]: https://doi.org/10.1007/978-3-663-20219-6_35
[research_ferrari_1958]: https://doi.org/10.1007/978-3-642-45885-9_21
[research_ferris_1973]: https://ntrs.nasa.gov/citations/19830002757
[research_fey_jeltsch_1993]: https://doi.org/10.1016/0045-7930(93)90022-2
[research_fezer_kloker_2000]: https://doi.org/10.1007/978-3-662-03997-7_62
[research_fiber_optic_loads_2018]: https://ntrs.nasa.gov/citations/20190033242
[research_fick_gaitonde_1996]: https://doi.org/10.2514/6.1996-2059
[research_fidler_hays_2026]: https://doi.org/10.2514/6.2026-114630
[research_fidler_jenkins_2025]: https://doi.org/10.2514/6.2025-99401
[research_fields_1978]: https://ntrs.nasa.gov/citations/19790013270
[research_fighter_sweep_model_1954]: https://ntrs.nasa.gov/citations/20090025891
[research_filimonov_1968]: https://doi.org/10.1007/bf00895855
[research_filin_mkrtchyan_2021]: https://doi.org/10.34759/vst-2021-2-63-72
[research_filippou_kilimtzidis_2024]: https://doi.org/10.20944/preprints202401.0348.v1
[research_finseth_1991]: https://doi.org/10.2514/6.1991-208
[research_finson_clarke_1980]: https://doi.org/10.21236/ada082438
[research_finson_clarke_1981]: https://doi.org/10.21236/ada096381
[research_fiore_fabiani_2026]: https://doi.org/10.1016/j.actaastro.2026.04.060
[research_firouzabadi_askarian_2013]: https://doi.org/10.1016/j.jfluidstructs.2012.09.005
[research_fischer_norris_1949]: https://doi.org/10.1115/1.4017110
[research_fisher_1969]: https://ntrs.nasa.gov/citations/19690028683
[research_fisher_dougherty_1982]: https://ntrs.nasa.gov/citations/19820018351
[research_flagella_1967]: https://doi.org/10.2172/4189092
[research_flagella_tarr_1967]: https://doi.org/10.2172/4571253
[research_flandro_sims_2004]: https://doi.org/10.2514/6.2004-3516
[research_flandro_sims_2004_b]: https://doi.org/10.2514/6.2004-4162
[research_flat_wings_2020]: https://doi.org/10.1002/9781119667063.ch6
[research_flax_1953]: https://doi.org/10.2514/8.2694
[research_flax_1977]: https://doi.org/10.2514/3.60639
[research_flax_1986]: https://doi.org/10.2514/3.48708
[research_fleeter_mcclure_1974]: https://doi.org/10.2514/6.1974-622
[research_flexible_fsw_dynamics_1982]: https://ntrs.nasa.gov/citations/19820055567
[research_flexible_wing_lateral_1951]: https://ntrs.nasa.gov/citations/19930092079
[research_flight_measurements_1983]: https://doi.org/10.2514/5.9781600865626.0255.0270
[research_florence_hiltz_1968]: https://doi.org/10.2514/6.1968-304
[research_fofonov_2021]: https://doi.org/10.33257/phchgd.22.6.965
[research_ford_1979]: https://doi.org/10.1108/eb035554
[research_ford_1985]: https://doi.org/10.1108/eb036142
[research_forebody_deflection_1959]: https://ntrs.nasa.gov/citations/19980228222
[research_formalev_garibyan_2023]: https://doi.org/10.1134/s0018151x23030203
[research_formation_and_2020]: https://doi.org/10.47176/jame.39.1.3531
[research_fornasier_1984]: https://doi.org/10.2514/6.1984-1646
[research_forooghi_magagnato_2018]: https://doi.org/10.1615/ihtc16.cov.021429
[research_foroozan_ianiro_2025]: https://doi.org/10.1103/bs9l-bhqz
[research_forsching_2004]: https://doi.org/10.1007/978-3-642-18484-0_11
[research_forsching_senft_1991]: https://doi.org/10.1017/s0001924000024301
[research_forster_kolonay_1996]: https://doi.org/10.2514/6.1996-4010
[research_fortney_avery_1957]: https://doi.org/10.21236/ad0142007
[research_fosdick_1970]: https://doi.org/10.21236/ad0880677
[research_foster_ross_1993]: https://doi.org/10.2514/6.1993-3647
[research_foster_shah]: https://ntrs.nasa.gov/citations/20200003251
[research_fournier_sleeman_1960]: https://ntrs.nasa.gov/citations/19650003196
[research_foxjr_breedlovejr_1974]: https://doi.org/10.2514/6.1974-186
[research_foxrabinovich_wilkinson_2006]: https://doi.org/10.1016/j.intermet.2005.05.011
[research_frampton_clark_1995]: https://doi.org/10.2514/6.1995-1079
[research_france_s_liquid_2006]: https://doi.org/10.2514/5.9781600868870.0785.0814
[research_franklin_1971]: https://doi.org/10.2514/3.44303
[research_frazier_1991]: https://doi.org/10.2514/6.1991-3173
[research_free_flight_tunnel_1952]: https://ntrs.nasa.gov/citations/20050029465
[research_freeman_goodell_1969]: https://ntrs.nasa.gov/citations/19690006824
[research_french_1964]: https://doi.org/10.2514/3.2778
[research_french_1967]: https://doi.org/10.2514/3.59571
[research_french_1971]: https://doi.org/10.2514/3.44290
[research_french_1979]: https://doi.org/10.2514/6.1979-450
[research_french_1980]: https://doi.org/10.2514/3.57735
[research_french_1988]: https://doi.org/10.2514/6.1988-2139
[research_french_noll_1988]: https://doi.org/10.2514/3.45593
[research_frendi_1996]: https://doi.org/10.2514/6.1996-433
[research_frendi_1997]: https://doi.org/10.2514/2.87
[research_freudenthal_1963]: https://doi.org/10.21236/ad0403508
[research_friedland_1965]: https://doi.org/10.2514/6.1965-533
[research_friedman_bhat_1986]: https://doi.org/10.2514/6.1986-1480
[research_frink_murphy_2016]: https://ntrs.nasa.gov/citations/20160007537
[research_fromont_1992]: https://doi.org/10.1080/08871949.1992.11752483
[research_frostig_thomsen_2008]: https://doi.org/10.2514/1.31704
[research_fsw_airfoil_divergence_1980]: https://ntrs.nasa.gov/citations/19800068478
[research_fsw_divergence_study_1986]: https://ntrs.nasa.gov/citations/19860017807
[research_fsw_divergence_tunnel_1980]: https://ntrs.nasa.gov/citations/19800020786
[research_fsw_flight_divergence_1988]: https://ntrs.nasa.gov/citations/19880015249
[research_fu_shi_2024]: https://doi.org/10.1063/5.0232908
[research_fujita_matsushima_2004]: https://doi.org/10.2514/1.3455
[research_fuller_1952]: https://doi.org/10.2514/8.2404
[research_fuller_2012]: https://doi.org/10.2514/6.2012-4896
[research_fulmer_wirtz_1964]: https://doi.org/10.21236/ad0618368
[research_funazaki_1994]: https://doi.org/10.1115/94-gt-025
[research_fundamental_mechanisms_1995]: https://doi.org/10.2514/5.9781600866371.0307.0343
[research_fung_1954]: https://doi.org/10.2514/8.3122
[research_fung_1958]: https://doi.org/10.2514/8.7557
[research_fung_1963]: https://doi.org/10.2514/3.1661
[research_furst_1973]: https://doi.org/10.4271/730926
[research_furst_1975]: https://doi.org/10.2514/6.1975-1301
[research_furukawa_makino_2007]: https://doi.org/10.2514/6.2007-4166
[research_furuya_fukuchi_2001]: https://doi.org/10.2514/6.2001-1631
[research_g_the_1957]: https://doi.org/10.1515/9781400879908-016
[research_galli]: https://doi.org/10.70675/97c77627zc51bz4cb0za02bzf5547129624d
[research_gallon_witkowski_2013]: https://doi.org/10.2514/6.2013-1329
[research_gallon_witkowski_2015]: https://doi.org/10.2514/6.2015-2162
[research_galsworthy_heawood_1982]: https://doi.org/10.1007/978-94-009-7907-9_38
[research_ganapathisubramani_2007]: https://doi.org/10.1063/1.2772303
[research_gandhi_richards_2012]: https://doi.org/10.2514/6.2012-4820
[research_gandhi_richards_2014]: https://doi.org/10.2514/6.2014-0444
[research_ganesan_subburayan_2025]: https://doi.org/10.3390/engproc2025093029
[research_ganeshkumar_ganesan_2018]: https://doi.org/10.1080/09603409.2018.1456039
[research_gao_jiang_2026]: https://doi.org/10.2139/ssrn.7168428
[research_gao_yang_2011]: https://doi.org/10.4028/www.scientific.net/amr.217-218.107
[research_gao_zhang_2016]: https://doi.org/10.1016/j.asr.2016.03.010
[research_gaponov_2000]: https://doi.org/10.1007/978-3-662-03997-7_58
[research_gaponov_kosinov_1995]: https://doi.org/10.1007/978-3-642-79765-1_21
[research_garcia_guruswamy_1999]: https://doi.org/10.2514/6.1999-796
[research_garcia_keshmiri_2015]: https://doi.org/10.2514/6.2015-1545
[research_gardner_1951]: https://ntrs.nasa.gov/citations/20050029468
[research_garfinkle_1974]: https://doi.org/10.1007/bf02644020
[research_garrard_1998]: https://doi.org/10.2514/2.7612
[research_garren_1962]: https://ntrs.nasa.gov/citations/19620000276
[research_garrick_reed_1981]: https://doi.org/10.2514/3.57579
[research_gartling_1970]: https://doi.org/10.21236/ad0734154
[research_gaspersjr_1972]: https://doi.org/10.2514/6.1972-403
[research_gaviglio_1987]: https://doi.org/10.1016/0017-9310(87)90010-x
[research_gee_2000]: https://doi.org/10.1023/a:1008374401581
[research_gee_sipcic_1999]: https://doi.org/10.2514/2.765
[research_gellatly_gallagher_1964]: https://doi.org/10.21236/ad0431959
[research_gemranova_2021]: https://doi.org/10.34759/vst-2021-2-24-32
[research_genot_2021]: https://doi.org/10.1016/j.combustflame.2021.111563
[research_gera_wilson_1981]: https://doi.org/10.2514/6.1981-2505
[research_gerhart_1973]: https://doi.org/10.2514/3.6677
[research_gerhart_1975]: https://doi.org/10.2514/3.60489
[research_gerlach_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50009-9
[research_gerlach_1967]: https://doi.org/10.1016/b978-1-4831-9836-1.50013-7
[research_german_2011]: https://doi.org/10.2514/6.2011-641
[research_german_development_2010]: https://doi.org/10.2514/4.867552
[research_germerdonk_biegel_1990]: https://doi.org/10.1615/ihtc9.2460
[research_ghalandari_mahariq_2022]: https://doi.org/10.32604/cmc.2022.020884
[research_ghasimi_rabinovitch_2023]: https://doi.org/10.2514/6.2023-0461
[research_ghatak_robi_2015]: https://doi.org/10.1007/s12666-015-0803-6
[research_ghoreyshi_aref_2026]: https://doi.org/10.2514/6.2026-1328
[research_ghosh_modi_2021]: https://doi.org/10.2514/6.2021-1670
[research_ghosh_modi_2021_b]: https://doi.org/10.2514/6.2021-1843
[research_ghosh_raisinghani_1998]: https://doi.org/10.2514/2.2407
[research_giedt_sherby_1952]: https://doi.org/10.21236/ad0000691
[research_giersch_clark_2015]: https://doi.org/10.2514/6.2015-2135
[research_gilbert_schmidt_1984]: https://doi.org/10.2514/3.8566
[research_gill_lowenberg_2012]: https://doi.org/10.2514/6.2012-4648
[research_gillette_vaughn_1968]: https://doi.org/10.21236/ad0834962
[research_gillig_guarnieri_1956]: https://doi.org/10.21236/ad0091903
[research_gillis_1957]: https://ntrs.nasa.gov/citations/19930089776
[research_gillis_toll_1962]: https://doi.org/10.1515/9781400875030-004
[research_gilruth_1962]: https://doi.org/10.1515/9781400875030-014
[research_gilyard_berry_1972]: https://doi.org/10.2514/6.1972-961
[research_girgis_liu_2000]: https://doi.org/10.1007/978-3-662-03997-7_80
[research_giuliano_leonard_2010]: https://doi.org/10.2514/6.2010-6724
[research_gladh_ang_2013]: https://doi.org/10.3357/asem.3637.2013
[research_glaser_mccarthy_2012]: https://doi.org/10.2514/6.2012-4490
[research_glauert_1928]: https://doi.org/10.1098/rspa.1928.0039
[research_gnair_mv_2012]: https://doi.org/10.5120/7252-0368
[research_go_2009]: https://doi.org/10.2514/1.39025
[research_goertz_1995]: https://doi.org/10.2514/6.1995-2966
[research_goett_bicknell_1939]: https://ntrs.nasa.gov/citations/19930081546
[research_gokcen_1995]: https://doi.org/10.2514/6.1995-156
[research_gokcen_1996]: https://doi.org/10.2514/3.780
[research_gokcen_1996_b]: https://doi.org/10.2514/6.1996-352
[research_gokcen_1997]: https://doi.org/10.2514/2.6236
[research_goland_1952]: https://doi.org/10.21236/ad0004240
[research_goldbaum_1956]: https://doi.org/10.21236/ad0092263
[research_goldfeld_zatoloka_1985]: https://doi.org/10.1007/978-3-642-82462-3_64
[research_goldsmith_1964]: https://doi.org/10.2514/6.1964-588
[research_goldstein_1975]: https://doi.org/10.2514/3.6984
[research_goman_khramtsovsky_1997]: https://doi.org/10.2514/6.1997-3721
[research_gomes_suleman_2004]: https://doi.org/10.2514/6.2004-4608
[research_gomet_robin_2014]: https://doi.org/10.1016/j.actaastro.2013.08.016
[research_gomez_flutet_2009]: https://doi.org/10.1103/physreve.79.035301
[research_gomillion_1976]: https://doi.org/10.21236/ada029144
[research_gonzalez_1977]: https://ntrs.nasa.gov/citations/19790010870
[research_goodell_freeman_1973]: https://doi.org/10.1520/stp36502s
[research_goodman_1956]: https://doi.org/10.2514/8.3566
[research_goodrich_derry_1979]: https://doi.org/10.2514/6.1979-1042
[research_goodyer_1990]: https://doi.org/10.2514/6.1990-3086
[research_gopal_maddalena_2018]: https://doi.org/10.1063/1.5030091
[research_gopalarathnam_selig_1997]: https://doi.org/10.2514/6.1997-2232
[research_gordnier_1993]: https://doi.org/10.2514/6.1993-2975
[research_gordnier_1995]: https://doi.org/10.2514/3.46746
[research_gordnier_visbal_2000]: https://doi.org/10.2514/6.2000-2337
[research_gordnier_visbal_2001]: https://doi.org/10.2514/6.2001-571
[research_gordnier_visbal_2003]: https://doi.org/10.1061/(asce)0893-1321(2003)16:4(155)
[research_gordon_speiser_1960]: https://doi.org/10.21236/ad0266990
[research_gorla_1984]: https://ntrs.nasa.gov/citations/19840017875
[research_gorla_1984_b]: https://ntrs.nasa.gov/citations/19850059631
[research_goswami_1995]: https://doi.org/10.1515/htmp.1995.14.1.1
[research_gotsulenko_gotsulenko_2013]: https://doi.org/10.1007/s10891-013-0816-0
[research_goud_dwivedi_2022]: https://doi.org/10.47893/gret.2022.1057
[research_gould_2001]: https://doi.org/10.2514/6.2001-369
[research_gourgues_andrieu_2003]: https://doi.org/10.1016/s0921-5093(02)00837-7
[research_gozukara_ceylan_2024]: https://doi.org/10.3390/computation12080162
[research_graefe_gordon_1957]: https://doi.org/10.21236/ad0139048
[research_gragg_evans_1982]: https://doi.org/10.21236/ada122870
[research_gragg_haars_1975]: https://doi.org/10.2514/6.1975-1402
[research_graham_1958]: https://doi.org/10.2514/8.7885
[research_graham_lagerstrom_1954]: https://doi.org/10.21236/ad0063453
[research_granata_savino_2024]: https://doi.org/10.2514/6.2024-2135
[research_granata_savino_2024_b]: https://doi.org/10.3390/aerospace11030213
[research_granville_boxall_1960]: https://doi.org/10.1088/0508-3443/11/10/305
[research_gratton_2014]: https://doi.org/10.1007/978-3-319-11409-5_13
[research_gratton_2018]: https://doi.org/10.1007/978-3-319-75617-2_13
[research_gratzer_odonnell_1964]: https://doi.org/10.2514/6.1964-589
[research_gratzer_odonnell_1965]: https://doi.org/10.2514/3.43686
[research_grauer_morelli_2023]: https://doi.org/10.2514/1.c037583
[research_greatrix_2018]: https://doi.org/10.2514/6.2018-4527
[research_greatrix_2021]: https://doi.org/10.32920/14638521
[research_green_fernandez_1994]: https://doi.org/10.2514/6.1994-2107
[research_green_spence_2004]: https://doi.org/10.2514/6.2004-15
[research_green_spence_2004_b]: https://doi.org/10.2514/6.2004-377
[research_greene_1970]: https://doi.org/10.2514/3.29878
[research_greenwood_prozan_1970]: https://doi.org/10.2514/6.1970-844
[research_gregorek_hoffmann_1977]: https://doi.org/10.4271/770461
[research_gregory_cooke_1998]: https://ntrs.nasa.gov/citations/19980206041
[research_gregory_you_2011]: https://ntrs.nasa.gov/citations/20110013020
[research_grenda_venkateswaran_1991]: https://doi.org/10.2514/6.1991-2085
[research_grenestedt_2008]: https://doi.org/10.2514/1.40401
[research_grenestedt_ridder_2006]: https://doi.org/10.2514/1.20523
[research_gresham_wang_2009]: https://doi.org/10.1007/s00348-009-0726-2
[research_grewal_schneider_1976]: https://doi.org/10.1016/s1474-6670(17)67131-3
[research_grey_1953]: https://doi.org/10.21236/ad0036007
[research_grey_1954]: https://doi.org/10.21236/ad0042856
[research_gribben_driscoll_1998]: https://doi.org/10.2514/6.1998-3362
[research_griffin_eastep_1981]: https://doi.org/10.2514/6.1981-637
[research_griffin_jonas_1983]: https://doi.org/10.2514/6.1983-1835
[research_griffith_crosby_1970]: https://doi.org/10.4050/jahs.15.2.10
[research_grindrod_noden_1968]: https://doi.org/10.1111/j.1475-1305.1968.tb01365.x
[research_gringorten_1967]: https://doi.org/10.21236/ad0656309
[research_gringorten_tattelman_1970]: https://doi.org/10.21236/ad0712017
[research_grobstein_doychak_1989]: https://ntrs.nasa.gov/citations/19900037797
[research_groeneric_fuckelars_2012]: https://doi.org/10.3233/978-1-61499-063-5-239
[research_grohmann_kroplin_1999]: https://doi.org/10.1142/9789814291071_0043
[research_gromov_larin_1982]: https://doi.org/10.1007/bf01091296
[research_gromski_majamaki_2010]: https://doi.org/10.2514/6.2010-6725
[research_gros_1963]: https://doi.org/10.21236/ad0436090
[research_grosdemange_schaeffer_1990]: https://doi.org/10.2514/6.1990-1835
[research_gross_mawhinney_1970]: https://doi.org/10.2514/6.1970-1213
[research_grosser_1965]: https://doi.org/10.2514/6.1965-789
[research_groth_1961]: https://doi.org/10.1016/b978-1-4832-1323-1.50018-x
[research_ground_and_2000]: https://doi.org/10.2514/5.9781600866555.0197.0224
[research_gu_healy_2024]: https://doi.org/10.2514/6.2024-0618
[research_guan_guo_2016]: https://doi.org/10.1142/9789813145603_0037
[research_guan_zhu_2013]: https://doi.org/10.2514/6.2013-386
[research_guarnieri_1954]: https://doi.org/10.1520/stp48004s
[research_guderley_1987]: https://doi.org/10.21236/ada193773
[research_guderley_1988]: https://doi.org/10.21236/ada191408
[research_guglieri_quagliotti_1993]: https://doi.org/10.2514/3.46357
[research_guide_for]: https://doi.org/10.1520/e1319
[research_guiler]: https://doi.org/10.33915/etd.2779
[research_guiler_huebsch_2005]: https://doi.org/10.2514/6.2005-4981
[research_guimaraes_cesnik_2021]: https://doi.org/10.2514/6.2021-2531
[research_guimaraes_rade_2020]: https://doi.org/10.2514/6.2020-0941
[research_guinn_1961]: https://doi.org/10.2514/8.5403
[research_gulczynski_hahn_2024]: https://doi.org/10.3390/aerospace11100808
[research_gunn_1947]: https://doi.org/10.1098/rsta.1947.0005
[research_gunn_1947_b]: https://doi.org/10.1098/rsta.1947.0006
[research_guo_adams_1994]: https://ntrs.nasa.gov/citations/19950014657
[research_guo_mei]: https://doi.org/10.4203/ccp.79.83
[research_guo_mei_2002]: https://doi.org/10.2514/6.2002-1486
[research_guo_mei_2003]: https://doi.org/10.2514/2.1940
[research_guo_przekop_2004]: https://doi.org/10.2514/1.5669
[research_guo_ren_2015]: https://doi.org/10.2514/6.2015-2559
[research_guo_ren_2019]: https://doi.org/10.1186/s42774-019-0018-3
[research_guo_wang_1988]: https://doi.org/10.21236/ada191553
[research_guo_xu_2022]: https://doi.org/10.3389/fenrg.2021.810439
[research_guo_zhang_2022]: https://doi.org/10.32604/cmes.2022.020638
[research_guo_zhang_2025]: https://doi.org/10.1007/978-981-95-3007-6_39
[research_gupta_jones_1992]: https://ntrs.nasa.gov/citations/19920022037
[research_gupta_ramkumar_2015]: https://doi.org/10.12783/fae.2015.0401.02
[research_gurentsov_shikov_2002]: https://doi.org/10.1615/heattransres.v33.i3-4.20
[research_gurov_2001]: https://doi.org/10.2514/6.2001-3395
[research_gut_parzybut_2025]: https://doi.org/10.3390/aerospace12070617
[research_guttman_crutcher_1968]: https://doi.org/10.1080/00431672.1968.9932828
[research_gwin_1974]: https://doi.org/10.2514/6.1974-349
[research_haas_chopra_1987]: https://doi.org/10.2514/6.1987-920
[research_habchi_hufford_1995]: https://doi.org/10.2514/6.1995-1837
[research_habchi_hufford_1995_b]: https://doi.org/10.2514/6.1995-187
[research_habchi_przekwas_1992]: https://doi.org/10.4271/921924
[research_hacker_oprisiu_1974]: https://doi.org/10.1016/0376-0421(74)90005-0
[research_hader_fasel_2023]: https://doi.org/10.2514/6.2023-0287
[research_haga_2024]: https://doi.org/10.52843/cassyni.t07j48
[research_hagerman_hofstetter_1969]: https://doi.org/10.2514/6.1969-794
[research_haglaga_1970]: https://doi.org/10.21236/ada367066
[research_hahn_frendi_2012]: https://doi.org/10.2514/6.2012-2172
[research_hahn_frendi_2013]: https://doi.org/10.2514/1.j052101
[research_hajela_glowasky_1991]: https://doi.org/10.2514/6.1991-3191
[research_hakim_tahdi_2020]: https://doi.org/10.1109/icst50505.2020.9732776
[research_hale_patil_2015]: https://doi.org/10.2514/6.2015-2329
[research_halford_1972]: https://doi.org/10.1007/bf02643239
[research_hall_boothe_1972]: https://doi.org/10.2514/3.58945
[research_hallberg_cenko_2008]: https://doi.org/10.2514/6.2008-6381
[research_hallstaff_1961]: https://doi.org/10.1108/eb033356
[research_hambattista_helmick_1993]: https://doi.org/10.2514/6.1993-1396
[research_hamed_1993]: https://doi.org/10.21236/ada268106
[research_hamed_li_2008]: https://doi.org/10.2514/6.2008-67
[research_hameed_2021]: https://doi.org/10.1016/j.ast.2021.106777
[research_hammer_garmann_2021]: https://doi.org/10.2514/6.2021-2948
[research_hammer_garmann_2023]: https://doi.org/10.2514/1.j063039
[research_hampson_1984]: https://doi.org/10.4271/841619
[research_han_he_2022]: https://doi.org/10.1063/5.0121259
[research_han_su_2020]: https://doi.org/10.20944/preprints202007.0120.v1
[research_han_yang_1983]: https://doi.org/10.2514/3.8267
[research_hancock_1959]: https://doi.org/10.1017/s0001925900001487
[research_hanford_wilson_1992]: https://doi.org/10.1115/92-gt-197
[research_hanford_wilson_1992_b]: https://ntrs.nasa.gov/citations/19930035425
[research_hanine_kourta_1992]: https://doi.org/10.1007/978-3-663-13974-4_40
[research_hanna_stephens_1991]: https://doi.org/10.2514/6.1991-4007
[research_hanson_schaefer_2011]: https://ntrs.nasa.gov/citations/20110023802
[research_hao_kong_2026]: https://doi.org/10.1109/jsen.2026.3737217
[research_hao_liu_2024]: https://doi.org/10.1016/j.tsep.2024.102516
[research_harbec_todkill_1965]: https://doi.org/10.4095/325333
[research_hardgrove_kriegjr_1984]: https://doi.org/10.2514/6.1984-1254
[research_hardy_bronowski_2005]: https://doi.org/10.2172/923159
[research_hargrave_fairweather_1985]: https://doi.org/10.1016/0142-727x(85)90042-6
[research_harmathy_stanzak_1970]: https://doi.org/10.1520/stp44718s
[research_harper_1969]: https://doi.org/10.2514/6.1969-420
[research_harri_1964]: https://doi.org/10.2172/4597699
[research_harris_1972]: https://ntrs.nasa.gov/citations/19780016136
[research_harris_bartlett_1972]: https://ntrs.nasa.gov/citations/19780016134
[research_harris_fasel_1996]: https://doi.org/10.2514/6.1996-686
[research_harris_robinson_1960]: https://ntrs.nasa.gov/citations/19650003200
[research_harris_robinson_1960_b]: https://ntrs.nasa.gov/citations/19680068658
[research_harrje_1959]: https://doi.org/10.21236/ad0212816
[research_hart_1956]: https://doi.org/10.21236/ad0108104
[research_hartley_furey_1965]: https://doi.org/10.21236/ad0626655
[research_harvazinski_mehta_2024]: https://doi.org/10.2514/6.2024-0149
[research_harvazinski_sankaran_2014]: https://doi.org/10.2514/6.2014-0577
[research_harvey_1970]: https://doi.org/10.2514/6.1970-703
[research_hasehemian_1986]: https://doi.org/10.21236/ada182715
[research_hashimoto_aoyama_2009]: https://doi.org/10.2514/1.35786
[research_hashimoto_menshov_2003]: https://doi.org/10.2514/6.2003-3721
[research_hashin_humphreys_1980]: https://doi.org/10.21236/ada089414
[research_hassan_1994]: https://doi.org/10.1080/08905459408905204
[research_hassan_abbass_2010]: https://doi.org/10.31026/j.eng.2010.03.21
[research_hassan_kunz_2021]: https://doi.org/10.1115/1.4052437
[research_hata_2001]: https://doi.org/10.1080/01495730150500415
[research_hatton_1964]: https://doi.org/10.1016/0017-9310(64)90144-9
[research_hatton_1965]: https://doi.org/10.1016/0017-9310(65)90032-3
[research_hatton_eustace_2019]: https://doi.org/10.1615/ihtc3.1760
[research_havener_1985]: https://doi.org/10.2514/6.1985-1613
[research_hayashi_aso_1988]: https://doi.org/10.2514/6.1988-426
[research_hayes_1946]: https://doi.org/10.1090/qam/18073
[research_hayhurst_1974]: https://doi.org/10.1016/0020-7403(74)90041-1
[research_hayhurst_2001]: https://doi.org/10.1016/b978-012443341-0/50085-5
[research_hayostek_amitay_2018]: https://doi.org/10.2514/6.2018-3729
[research_he_song_2020]: https://doi.org/10.2514/6.2020-1908
[research_he_wang_2021]: https://doi.org/10.2514/6.2021-2534
[research_heald_brassell_1976]: https://doi.org/10.2514/6.1976-891
[research_heardjr_1965]: https://doi.org/10.2514/6.1965-112
[research_heat_transfer_2013]: https://doi.org/10.1201/b16194-7
[research_heat_transfer_mach146_1958]: https://ntrs.nasa.gov/citations/19930089952
[research_heated_plate_modes_1991]: https://ntrs.nasa.gov/citations/19910012798
[research_heating_ice_1940]: https://ntrs.nasa.gov/citations/20090014120
[research_hebsur_stephens_1988]: https://ntrs.nasa.gov/citations/19890003346
[research_hebsur_stephens_1989]: https://ntrs.nasa.gov/citations/19900037806
[research_hebsur_stephens_1991]: https://ntrs.nasa.gov/citations/20080007418
[research_heinrich_1966]: https://doi.org/10.2514/3.43713
[research_heinrich_1972]: https://doi.org/10.1017/s0001924000044481
[research_heinrich_hektner_1970]: https://doi.org/10.21236/ad0869329
[research_heinrich_noreen_1968]: https://doi.org/10.2514/6.1968-924
[research_heinrich_noreen_1974]: https://doi.org/10.21236/ada005271
[research_heinrich_saari_1975]: https://doi.org/10.2514/6.1975-1382
[research_heinrich_saari_1978]: https://doi.org/10.2514/3.58321
[research_heister_2008]: https://doi.org/10.21236/ada494724
[research_hellyer_sherhod]: https://doi.org/10.1109/naecon.1988.195109
[research_hemmig_venkayya_1980]: https://doi.org/10.2514/3.57972
[research_hender_1982]: https://doi.org/10.2514/6.1982-860
[research_hendershot_1969]: https://doi.org/10.2514/6.1969-335
[research_henderson_komenda_1998]: https://doi.org/10.1115/98-gt-488
[research_heng_sherman_1996]: https://doi.org/10.1063/1.49920
[research_henke_nerem_1968]: https://doi.org/10.2514/6.1968-947
[research_henry_patel_2017]: https://doi.org/10.2514/6.2017-3535
[research_hensel_1964]: https://doi.org/10.2514/6.1964-1109
[research_henson_robertson_1962]: https://doi.org/10.21236/ad0275641
[research_hermann_1950]: https://doi.org/10.21236/ada377566
[research_hermann_2025]: https://doi.org/10.1016/j.ijheatmasstransfer.2025.126907
[research_hermes_crew_1990]: https://doi.org/10.1016/0045-8732(90)90128-b
[research_herring_2009]: https://doi.org/10.2514/1.42004
[research_herrmann_2008]: https://doi.org/10.2514/1.32673
[research_herrmann_orlowski_1997]: https://doi.org/10.1007/978-3-322-86573-1_24
[research_hess_1997]: https://doi.org/10.2514/2.4169
[research_hess_2013]: https://doi.org/10.3390/aerospace1010001
[research_hess_hess_1997]: https://doi.org/10.2514/6.1997-454
[research_hewes_hassell_1960]: https://ntrs.nasa.gov/citations/19980223968
[research_hibner_sizek_1997]: https://doi.org/10.7449/1997/superalloys_1997_491_501
[research_hicks_moulton_1988]: https://doi.org/10.2514/6.1988-2144
[research_high_altitude_1957]: https://ntrs.nasa.gov/citations/19820068145
[research_high_bowman_1995]: https://doi.org/10.2514/6.1995-157
[research_high_speed_1962]: https://doi.org/10.1515/9781400875030
[research_high_speed_flight_1986]: https://doi.org/10.1016/0016-3287(86)90050-9
[research_high_speed_flight_1996]: https://doi.org/10.2514/5.9781600862540.0001.0026
[research_high_speed_flight_1996_b]: https://doi.org/10.2514/5.9781600866401.0517.0579
[research_high_speed_flight_2009]: https://doi.org/10.1007/978-1-4020-8664-9_9
[research_high_speed_flight_2010]: https://doi.org/10.1002/9780470710944.ch15
[research_high_temperature_1962]: https://doi.org/10.1595/003214062x64148149
[research_high_temperature_1975]: https://doi.org/10.1111/j.1475-1305.1975.tb00141.x
[research_high_temperature_thin_film_2005]: https://ntrs.nasa.gov/citations/20050170415
[research_highspeed_conference_1958]: https://ntrs.nasa.gov/citations/19710069971
[research_hilger_ritter_2021]: https://doi.org/10.3390/aerospace8100308
[research_hill_misra_1970]: https://ntrs.nasa.gov/citations/19700000202
[research_hillier_1970]: https://doi.org/10.1017/s0001925900005394
[research_hinada_inatani_1991]: https://doi.org/10.2514/6.1991-859
[research_hiraki_hinada_1997]: https://doi.org/10.2514/6.1997-1529
[research_hiraki_inoue_2019]: https://doi.org/10.1088/1755-1315/240/5/052028
[research_hirschberg_spera_1972]: https://ntrs.nasa.gov/citations/19720007871
[research_hirschberg_vanmuiswinkel_1977]: https://doi.org/10.1016/0017-9310(77)90054-0
[research_history_of_2020]: https://doi.org/10.1002/9781119667063.ch1
[research_hitch_1978]: https://doi.org/10.2514/3.58464
[research_hodell_rosner_1957]: https://doi.org/10.21236/ad0142103
[research_hodgkinson_potsdam_1990]: https://doi.org/10.2514/6.1990-2825
[research_hoff_1956]: https://doi.org/10.2514/8.3715
[research_hoffman_zvara_1970]: https://doi.org/10.2514/3.29898
[research_hoh_myers_1981]: https://doi.org/10.21236/ada100045
[research_hollinger_1965]: https://ntrs.nasa.gov/citations/19650019254
[research_holloway_johnson_2008]: https://doi.org/10.1049/cp:20080732
[research_holmes_moore_1992]: https://ntrs.nasa.gov/citations/19930004484
[research_holt_1977]: https://doi.org/10.1520/jte10560j
[research_holtz_1964]: https://ntrs.nasa.gov/citations/19640017947
[research_holzapfel_dacosta_2006]: https://doi.org/10.2514/6.2006-6222
[research_holzinger_cunis_2024]: https://doi.org/10.1109/ccta60707.2024.10666640
[research_homan_1970]: https://doi.org/10.21236/ad0870914
[research_hong_1965]: https://doi.org/10.2514/6.1965-622
[research_hong_kim_2009]: https://doi.org/10.3795/ksme-b.2009.33.12.933
[research_hoover_1947]: https://doi.org/10.4271/470087
[research_hopkins_dowell_1994]: https://doi.org/10.2514/6.1994-1486
[research_horagiri_nagai_2014]: https://doi.org/10.2514/6.2014-1408
[research_horenstein_roberts_1993]: https://doi.org/10.2514/6.1993-1210
[research_horsnell_1967]: https://doi.org/10.2514/6.1967-570
[research_horstman_hung_1979]: https://doi.org/10.2514/6.1979-2
[research_horstman_kussoy_1967]: https://doi.org/10.2514/6.1967-165
[research_horstman_kussoy_1978]: https://ntrs.nasa.gov/citations/19780057950
[research_horton_zeh_1966]: https://ntrs.nasa.gov/citations/19670002779
[research_horton_zeh_1967]: https://ntrs.nasa.gov/citations/19670054296
[research_hosangadi_paul_2015]: https://doi.org/10.2514/6.2015-3159
[research_hoschke_price_2013]: https://doi.org/10.4028/www.scientific.net/kem.558.268
[research_hosni_coleman_1991]: https://doi.org/10.2514/6.1991-161
[research_hot_structure_vibration_1993]: https://ntrs.nasa.gov/citations/19940032137
[research_hou_2008]: https://doi.org/10.3724/sp.j.1077.2008.00213
[research_hou_fu_2018]: https://doi.org/10.1080/00102202.2018.1551214
[research_hou_liu_2023]: https://doi.org/10.2139/ssrn.4410410
[research_hou_satyanarayana_2000]: https://doi.org/10.2514/6.2000-4824
[research_houbolt_menkes_1968]: https://doi.org/10.2514/6.1968-283
[research_houra_nagano_2014]: https://doi.org/10.1615/ihtc15.ttr.009325
[research_house_ayoola_2021]: https://doi.org/10.1017/s143192762101000x
[research_howland_1979]: https://doi.org/10.21236/ada072444
[research_hreha_lutze_1983]: https://doi.org/10.2514/6.1983-367
[research_hreha_lutze_1984]: https://doi.org/10.2514/3.48223
[research_hrubecky_1995]: https://doi.org/10.1007/978-1-4899-5696-5_20
[research_hsfrs_rcs_2015]: https://ntrs.nasa.gov/citations/20160000534
[research_hsu_2026]: https://doi.org/10.1016/b978-0-443-33542-6.00005-2
[research_hu_ferrari_2021]: https://doi.org/10.1016/j.ast.2021.106729
[research_hu_he_2026]: https://doi.org/10.1016/j.ast.2026.112837
[research_hu_jameson_2012]: https://doi.org/10.2514/1.c031417
[research_hu_mahadevan_2019]: https://doi.org/10.2514/1.j057865
[research_hu_tan_2023]: https://doi.org/10.20944/preprints202306.1962.v1
[research_hua_wang_2025]: https://doi.org/10.3390/aerospace12040327
[research_huang_2000]: https://doi.org/10.2514/6.2000-3770
[research_huang_2002]: https://doi.org/10.1360/02yb9047
[research_huang_2002_b]: https://doi.org/10.1360/02yb9072
[research_huang_2005]: https://doi.org/10.1360/142005-19
[research_huang_2016]: https://doi.org/10.1109/ecc.2016.7810266
[research_huang_avery_2020]: https://doi.org/10.2514/6.2020-0313
[research_huang_cheng_2024]: https://doi.org/10.1007/978-981-97-6485-3_7
[research_huang_cheng_2024_b]: https://doi.org/10.1007/978-981-97-6485-3_8
[research_huang_friedmann_2016]: https://doi.org/10.2514/6.2016-1090
[research_huang_friedmann_2019]: https://doi.org/10.2514/1.j057499
[research_huang_fu_2021]: https://doi.org/10.1115/1.0001749v
[research_huang_hu_2021]: https://doi.org/10.1007/s11665-021-06080-w
[research_huang_liou_1994]: https://ntrs.nasa.gov/citations/19950019657
[research_huang_lu_2023]: https://doi.org/10.3390/app13084925
[research_huang_valentin_1974]: https://doi.org/10.2172/4293677
[research_huang_zhang_2014]: https://doi.org/10.4028/www.scientific.net/amm.670-671.1410
[research_huang_zhou_2000]: https://doi.org/10.2514/6.2000-3297
[research_huang_zhou_2000_b]: https://doi.org/10.2514/6.2000-3298
[research_hubbard_fontenot_2014]: https://doi.org/10.2514/1.c032339
[research_hubble_fu_2008]: https://doi.org/10.2514/6.2008-4118
[research_hube_1978]: https://doi.org/10.21236/ada067908
[research_hudson_1989]: https://ntrs.nasa.gov/citations/19900057437
[research_hudson_stephens_2006]: https://ntrs.nasa.gov/citations/20060056099
[research_huffman_foxjr_1985]: https://doi.org/10.2514/6.1985-276
[research_hufford_habchi_1994]: https://doi.org/10.2514/6.1994-751
[research_hughes_1964]: https://doi.org/10.1017/s0001925900010842
[research_hui_tobak_1982]: https://doi.org/10.2514/6.1982-244
[research_hulka_2008]: https://doi.org/10.2514/6.2008-5113
[research_hulse_bailey_1984]: https://ntrs.nasa.gov/citations/19870001755
[research_hulse_bailey_1985]: https://ntrs.nasa.gov/citations/19880001760
[research_hulse_bailey_1987]: https://ntrs.nasa.gov/citations/19870019436
[research_hulse_bailey_1991]: https://ntrs.nasa.gov/citations/19920004819
[research_hung_buning_1985]: https://ntrs.nasa.gov/citations/19990066634
[research_hung_chaussee_1981]: https://ntrs.nasa.gov/citations/19980033934
[research_hung_maccormack_1978]: https://ntrs.nasa.gov/citations/19780038682
[research_hurst_schulz_1994]: https://doi.org/10.1115/94-gt-173
[research_hussein_etzenbach_2026]: https://doi.org/10.2514/6.2026-1001
[research_huston_warfield_1948]: https://ntrs.nasa.gov/citations/19930082417
[research_huysmans_vekeman_2017]: https://doi.org/10.5937/zzk1704169h
[research_hwu_tsai_2002]: https://doi.org/10.2514/2.2945
[research_hyde_1986]: https://doi.org/10.1080/02619180.1986.11753312
[research_hyde_argueta_2025]: https://doi.org/10.2514/6.2025-0109
[research_hyde_brown_2018]: https://doi.org/10.2514/6.2018-1021
[research_hyers_2009]: https://doi.org/10.21236/ada524249
[research_hypersonic_heating_survey_1981]: https://ntrs.nasa.gov/citations/19810054730
[research_hypersonic_research_structure_1976]: https://ntrs.nasa.gov/citations/19760062425
[research_hypersonic_wing_structure_1975]: https://ntrs.nasa.gov/citations/19750048598
[research_ibrahim_1965]: https://doi.org/10.21236/ad0465722
[research_ibrahim_1989]: https://doi.org/10.2514/6.1989-1166
[research_ibrahim_1990]: https://doi.org/10.2514/6.1990-986
[research_ibrahim_beloiu_2004]: https://doi.org/10.1115/imece2004-60184
[research_ibrahim_tawfik_2007]: https://doi.org/10.2514/1.27866
[research_ide_ominsky_1990]: https://doi.org/10.2514/6.1990-1075
[research_ifju_waszak_2001]: https://doi.org/10.2514/6.2001-4005
[research_ii_1970]: https://doi.org/10.2514/6.1970-944
[research_ilyashenko_1963]: https://doi.org/10.2514/3.1523
[research_imai_hirata_1992]: https://doi.org/10.1016/b978-0-444-88970-6.50044-0
[research_inertia_coupling_2004]: https://doi.org/10.2514/5.9781600862274.0631.0676
[research_inertia_coupling_2015]: https://doi.org/10.2514/5.9781624102745.0681.0730
[research_influence_of_1980]: https://doi.org/10.2514/5.9781600865435.0332.0359
[research_influence_of_1989]: https://doi.org/10.2514/6.1989-85
[research_inger_1984]: https://doi.org/10.2514/6.1984-1555
[research_inger_1985]: https://doi.org/10.2514/6.1985-1669
[research_inger_1986]: https://doi.org/10.1007/978-3-642-82770-9_24
[research_inger_1988]: https://doi.org/10.21236/ada206145
[research_inger_1995]: https://doi.org/10.2514/6.1995-229
[research_injector_throttling_2006]: https://ntrs.nasa.gov/citations/20060047749
[research_innocenzi_bruce_2023]: https://doi.org/10.2514/6.2023-1170
[research_instability_phenomenology_1995]: https://doi.org/10.2514/5.9781600866371.0003.0037
[research_instability_phenomenology_1995_b]: https://doi.org/10.2514/5.9781600866371.0039.0071
[research_instability_phenomenology_1995_c]: https://doi.org/10.2514/5.9781600866371.0089.0112
[research_instability_phenomenology_1995_d]: https://doi.org/10.2514/5.9781600866371.0113.0142
[research_instrumentation_for_1960]: https://doi.org/10.2514/5.9781600864759.0119.0143
[research_integrated_thermal_2025]: https://doi.org/10.37285/bsp.sacad2025.15
[research_iosilevskii_2025]: https://doi.org/10.1007/978-3-031-73625-4_11
[research_irving_1966]: https://doi.org/10.1016/b978-1-4832-0019-4.50011-9
[research_isakson_1957]: https://doi.org/10.2514/8.3917
[research_ishikawa_kwak_2007]: https://doi.org/10.2514/6.2007-3925
[research_ishikawa_kwak_2008]: https://doi.org/10.2514/1.33595
[research_ishin_2022]: https://doi.org/10.33257/phchgd.23.6.1026
[research_islam_ali_2025]: https://doi.org/10.2514/6.2025-2430
[research_isogai_2013]: https://doi.org/10.2322/tjsass.56.303
[research_ivanov_2008]: https://doi.org/10.1134/s0033173208040139
[research_ivanov_2021]: https://doi.org/10.34759/vst-2021-2-33-45
[research_ivanov_borisov_2014]: https://doi.org/10.18287/2541-7533-2012-0-3-2(34)-302-306
[research_iyer_spall_1992]: https://doi.org/10.2514/6.1992-2630
[research_izadpanahi]: https://doi.org/10.25148/etd.fidc008911
[research_izadpanahi_mardanpour_2018]: https://doi.org/10.5772/intechopen.75804
[research_j_j_2015]: https://doi.org/10.14445/23488360/ijme-v2i6p103
[research_jablonowski_shober_1957]: https://doi.org/10.2172/4003021
[research_jacob_flandro_2010]: https://doi.org/10.2514/6.2010-6800
[research_jacob_george_2024]: https://doi.org/10.1007/s41403-024-00463-w
[research_jacobsen_1974]: https://ntrs.nasa.gov/citations/19740060871
[research_jacobsen_1977]: https://ntrs.nasa.gov/citations/19770053548
[research_jacobson_2010]: https://doi.org/10.2514/6.2010-8007
[research_jacobson_2010_b]: https://ntrs.nasa.gov/citations/20100036832
[research_jaffe_dorn_1960]: https://doi.org/10.21236/ada328524
[research_jain_1986]: https://doi.org/10.1080/02619180.1986.11753330
[research_jamesjr_1981]: https://doi.org/10.2514/6.1981-1905
[research_jameson_1977]: https://doi.org/10.2172/7093932
[research_jameson_caughey_1977]: https://doi.org/10.2172/7308750
[research_jameson_shankaran_2005]: https://doi.org/10.2514/6.2005-1013
[research_jamison_1966]: https://doi.org/10.2514/6.1966-1501
[research_jamison_1967]: https://doi.org/10.2514/3.28894
[research_jammalamadaka_li_2014]: https://doi.org/10.1063/1.4873495
[research_jamwal_hosangadi_2018]: https://doi.org/10.2514/6.2018-3956
[research_jana_sreedhar_2021]: https://doi.org/10.18520/cs/v120/i1/147-151
[research_japan_s_liquid_2006]: https://doi.org/10.2514/5.9781600868870.0815.0842
[research_jayan_raghunandan_2003]: https://doi.org/10.1615/atomizspr.v13.i4.10
[research_jayanti]: https://doi.org/10.1615/atoz.r.reynolds_analogy
[research_jayaram_taylor_1987]: https://ntrs.nasa.gov/citations/19870046182
[research_jayaraman_saini_2022]: https://doi.org/10.1016/j.ifacol.2023.03.032
[research_jeffrie_rolston_1972]: https://doi.org/10.2514/6.1972-761
[research_jegarkandimohsen_nobariali_2009]: https://doi.org/10.1108/00022660910941820
[research_jeng_litchford_1991]: https://doi.org/10.2514/6.1991-1985
[research_jeng_reddygorla_1973]: https://doi.org/10.1115/1.3450079
[research_jengshian_weichong_1991]: https://doi.org/10.1016/0020-7683(91)90164-b
[research_jenke_1979]: https://doi.org/10.2514/3.61189
[research_jenkins_2018]: https://doi.org/10.1201/9781351076364-7
[research_jenkins_quinn_1996]: https://ntrs.nasa.gov/citations/19960027893
[research_jenness_1958]: https://doi.org/10.1016/0038-092x(58)90049-5
[research_jensen_2005]: https://doi.org/10.2514/6.2005-4566
[research_jeon_kwak_2013]: https://doi.org/10.1016/j.ast.2012.03.005
[research_jeon_lee_2004]: https://doi.org/10.2514/6.2004-32
[research_jeon_park_2023]: https://doi.org/10.6108/kspe.2023.27.6.009
[research_jeon_park_2026]: https://doi.org/10.1016/j.applthermaleng.2026.131273
[research_jha_2024]: https://doi.org/10.2139/ssrn.4889182
[research_jhajj_caron_2014]: https://doi.org/10.1115/imece2014-38243
[research_ji_duan_2021]: https://doi.org/10.1109/jsen.2020.3015383
[research_ji_wang_2011]: https://doi.org/10.4028/www.scientific.net/amm.110-116.4343
[research_ji_xie_2022]: https://doi.org/10.32604/icces.2022.08737
[research_jia_han_2013]: https://doi.org/10.2514/6.2013-1368
[research_jiajan_chue_2013]: https://doi.org/10.1017/s0001924000008368
[research_jialin_lei_2014]: https://doi.org/10.1109/isdea.2014.150
[research_jiang_an_2000]: https://doi.org/10.2514/6.2000-4324
[research_jiang_campbell_2008]: https://doi.org/10.1016/j.ijheatmasstransfer.2007.12.006
[research_jiang_choudhari_2006]: https://doi.org/10.2514/6.2006-3224
[research_jiang_lin_2013]: https://doi.org/10.1515/htmp-2012-0172
[research_jiang_liu_2026]: https://doi.org/10.1007/s44210-025-00077-z
[research_jin_xu_2019]: https://doi.org/10.1016/j.ast.2019.03.042
[research_jines_1980]: https://doi.org/10.21236/ada087275
[research_jines_1983]: https://doi.org/10.2514/6.1983-2205
[research_jinglei_huiyang_2007]: https://doi.org/10.1088/0256-307x/24/3/048
[research_jirasek_cummings_2018]: https://doi.org/10.2514/1.c033818
[research_jischke_1978]: https://doi.org/10.21236/ada068004
[research_johari_desabrais_2002]: https://doi.org/10.21236/ada411095
[research_johns_1958]: https://doi.org/10.2514/8.7844
[research_johns_1960]: https://doi.org/10.2514/8.8424
[research_johnson_1985]: https://doi.org/10.2514/6.1985-4027
[research_johnson_1986]: https://doi.org/10.2514/6.1986-2437
[research_johnson_1988]: https://ntrs.nasa.gov/citations/19880011214
[research_johnson_1989]: https://doi.org/10.2514/6.1989-891
[research_johnson_faurote_1972]: https://doi.org/10.2514/6.1972-801
[research_johnson_josepha_1970]: https://doi.org/10.21236/ad0702806
[research_johnson_rubesin_1949]: https://doi.org/10.1115/1.4017109
[research_johnson_weir_1969]: https://doi.org/10.2514/3.44096
[research_johnson_yang_1985]: https://doi.org/10.4271/850912
[research_johnson_young_1972]: https://ntrs.nasa.gov/citations/19720016922
[research_johnsoniii_wu_1974]: https://doi.org/10.21236/ada017631
[research_johnsonms_pilla_2012]: https://doi.org/10.2514/6.2012-5133
[research_johnston_1964]: https://doi.org/10.2514/3.2245
[research_johnston_1998]: https://doi.org/10.2514/6.1998-2736
[research_johnston_ashkenas_1974]: https://doi.org/10.21236/ada014366
[research_johnston_hogge_1974]: https://doi.org/10.2514/6.1974-792
[research_johnston_hogge_1976]: https://doi.org/10.2514/3.58639
[research_jones_1947]: https://ntrs.nasa.gov/citations/19930091936
[research_jones_1950]: https://doi.org/10.2514/8.1517
[research_jones_1952]: https://ntrs.nasa.gov/citations/19930087316
[research_jones_1959]: https://doi.org/10.1016/b978-1-4831-9832-3.50006-1
[research_jones_1962]: https://doi.org/10.1093/qjmam/15.4.471
[research_jones_1966]: https://doi.org/10.21236/ad0487406
[research_jones_1967]: https://doi.org/10.1017/s0001924000056232
[research_jones_1976]: https://doi.org/10.2514/3.44558
[research_jones_1980]: https://doi.org/10.2514/6.1980-3040
[research_jones_bylina_1984]: https://doi.org/10.21236/ada142872
[research_jones_nisbet_1976]: https://doi.org/10.1017/s0001924000034138
[research_jones_richie_1974]: https://doi.org/10.2514/3.60373
[research_jordan_1972]: https://ntrs.nasa.gov/citations/19830002759
[research_jordan_langford_2004]: https://ntrs.nasa.gov/citations/20040085988
[research_joshi_rickard_1981]: https://doi.org/10.2514/6.1981-1887
[research_joshi_salahudden_2023]: https://doi.org/10.2514/6.2023-1556
[research_joy_talapatra_2024]: https://doi.org/10.2139/ssrn.4823390
[research_juliawan_lee_2024]: https://doi.org/10.2139/ssrn.5008879
[research_jun_kochan_2014]: https://doi.org/10.2478/msr-2014-0005
[research_jun_kochan_2017]: https://doi.org/10.23919/measurement.2017.7983563
[research_jung_reimerdes_2003]: https://doi.org/10.1007/978-3-540-44866-2_10
[research_jung_wee_2001]: https://doi.org/10.1023/a:1010399825117
[research_junkhan_1978]: https://doi.org/10.1115/1.3450498
[research_jurado_mcgehee_2019]: https://doi.org/10.2514/1.c034964
[research_jurado_shade_1990]: https://doi.org/10.2514/6.1990-2698
[research_kaattari_1959]: https://ntrs.nasa.gov/citations/19980228137
[research_kachler_beaurain_2005]: https://doi.org/10.2514/6.2005-3563
[research_kakudo_yokoyama_2021]: https://doi.org/10.1088/1742-6596/1909/1/012051
[research_kalkhoran_otugen_1994]: https://doi.org/10.21236/ada299229
[research_kaloust_2002]: https://doi.org/10.2514/6.2002-3489
[research_kambizfarahmandjonathanwkaufm_2001]: https://doi.org/10.1080/08916150120876
[research_kamijo_1983]: https://doi.org/10.2514/6.1983-1385
[research_kamijo_sogame_1981]: https://doi.org/10.2514/6.1981-1375
[research_kamijo_sogame_1982]: https://doi.org/10.2514/3.62241
[research_kanda_2013]: https://doi.org/10.2322/tjsass.56.49
[research_kanda_2019]: https://doi.org/10.2322/tjsass.62.331
[research_kanda_kikuchi_2021]: https://doi.org/10.2322/tjsass.64.13
[research_kanda_mishina_2023]: https://doi.org/10.1016/j.actaastro.2022.11.006
[research_kandil_kandil_1993]: https://doi.org/10.2514/6.1993-3472
[research_kandil_kandil_1993_b]: https://doi.org/10.2514/6.1993-3688
[research_kandis_witkowski_2019]: https://doi.org/10.2514/6.2019-3480
[research_kandula_haddad_2007]: https://doi.org/10.2514/1.28840
[research_kannan_bhat_2005]: https://doi.org/10.2514/1.12821
[research_kanneganti_charan_2022]: https://doi.org/10.47893/gret.2022.1085
[research_karabis_shaw_2000]: https://doi.org/10.1007/978-3-662-03997-7_71
[research_kariappa_smith_1972]: https://doi.org/10.2514/3.58948
[research_kariappa_somashekar_1969]: https://doi.org/10.2514/3.5033
[research_karlgaard_tynis_2018]: https://doi.org/10.2514/6.2018-3624
[research_karlgaard_tynis_2019]: https://doi.org/10.2514/6.2019-0014
[research_karpel_moulin_2004]: https://doi.org/10.2514/1.11483
[research_karpouzian_librescu_1992]: https://doi.org/10.2514/6.1992-2469
[research_karunakaran_2018]: https://doi.org/10.1108/aeat-09-2016-0151
[research_kasdaglis_bernard_2016]: https://doi.org/10.1145/2950112.2964574
[research_kase_mizoguchi_2020]: https://doi.org/10.1299/jsmemecj.2020.s05403
[research_kass_1970]: https://doi.org/10.2514/6.1970-875
[research_katipelli_dahotre_2001]: https://doi.org/10.1179/026708301101511185
[research_katz_1989]: https://doi.org/10.2514/3.10231
[research_kaufman_louisg_1964]: https://doi.org/10.21236/ad0601804
[research_kaul_stuckey_2002]: https://ntrs.nasa.gov/citations/20030001121
[research_kawakami_takatoya_2007]: https://doi.org/10.2514/6.2007-4174
[research_kawakami_takatoya_2008]: https://doi.org/10.2514/6.2008-6419
[research_kaye_brown_1954]: https://doi.org/10.21236/ad0045690
[research_kaye_yeh_1955]: https://doi.org/10.2514/8.3454
[research_kayran_2004]: https://doi.org/10.1115/esda2004-58467
[research_kayser_clay_1986]: https://doi.org/10.2514/6.1986-785
[research_kayser_sturek_1978]: https://doi.org/10.2514/6.1978-824
[research_kazemba_braun_2012]: https://doi.org/10.2514/6.2012-4509
[research_kazemba_braun_2017]: https://doi.org/10.2514/1.a33552
[research_ke_wang_2009]: https://doi.org/10.1109/cisp.2009.5304509
[research_kececi_karakus_2025]: https://doi.org/10.1115/ht2025-154242
[research_keck_1975]: https://doi.org/10.2514/6.1975-1379
[research_keeljr_1977]: https://doi.org/10.2514/6.1977-178
[research_keenan_kuhlman_1991]: https://doi.org/10.2514/6.1991-3305
[research_keener_1984]: https://doi.org/10.2514/6.1984-2092
[research_kegerise_owens_2010]: https://ntrs.nasa.gov/citations/20100025028
[research_kehrer_1964]: https://doi.org/10.2514/6.1964-586
[research_kehrer_1971]: https://doi.org/10.2514/6.1971-785
[research_keller_plaga_2008]: https://doi.org/10.21236/ada514712
[research_kempel_mcneill_1988]: https://doi.org/10.2514/6.1988-402
[research_kempel_mcneill_1988_b]: https://ntrs.nasa.gov/citations/19890006559
[research_kenyon_shinde_2025]: https://doi.org/10.2514/6.2025-1493
[research_kenzakowski_york_1997]: https://doi.org/10.2514/6.1997-2253
[research_khader_huston_1987]: https://doi.org/10.1115/1.3138653
[research_khakpour_soltani_2015]: https://doi.org/10.1016/j.mspro.2015.11.011
[research_khan_masud_2019]: https://doi.org/10.2514/6.2019-2307
[research_khan_qamar_2020]: https://doi.org/10.1016/j.actaastro.2020.06.021
[research_khan_qamar_2020_b]: https://doi.org/10.1088/1757-899x/715/1/012080
[research_khatri_sinha_2011]: https://doi.org/10.2514/6.2011-924
[research_khatri_subbarao_2024]: https://doi.org/10.23919/acc60939.2024.10644512
[research_kholodar_2023]: https://doi.org/10.2514/1.c036846
[research_khot_eastep_1997]: https://doi.org/10.2514/6.1997-1268
[research_khotyanovsky_kudryavtsev_2016]: https://doi.org/10.1063/1.4964000
[research_khrabrov_sidoryuk_2013]: https://doi.org/10.1051/eucass/201305621
[research_kiber_1977]: https://doi.org/10.21236/adb016616
[research_kies_schwartz_1974]: https://doi.org/10.1520/jte10086j
[research_kilburg_1968]: https://doi.org/10.2514/6.1968-374
[research_kilicay_2020]: https://doi.org/10.1016/j.surfcoat.2020.125777
[research_kim_2009]: https://doi.org/10.2514/1.37416
[research_kim_2017]: https://doi.org/10.1007/s10765-017-2285-8
[research_kim_chen_1992]: https://doi.org/10.2514/6.1992-3763
[research_kim_chung_2004]: https://doi.org/10.2514/6.2004-1337
[research_kim_kim_2015_b]: https://doi.org/10.4028/www.scientific.net/amr.1125.526
[research_kim_lee_2000]: https://doi.org/10.2514/2.2582
[research_kim_park_1999]: https://doi.org/10.2514/6.1999-1431
[research_kim_siddiqui_2024]: https://doi.org/10.2514/6.2024-3632
[research_kim_song_2013]: https://doi.org/10.2514/1.c031212
[research_kimata_taguchi_2015]: https://doi.org/10.2514/6.2015-2186
[research_kimmel_borg_2015]: https://doi.org/10.21236/ada623564
[research_kimmel_prabhu_2015]: https://ntrs.nasa.gov/citations/20160003109
[research_kimura_sato_2010]: https://doi.org/10.2514/6.2010-6727
[research_kimura_sawada_2022]: https://doi.org/10.1080/09603409.2022.2058230
[research_king_1962]: https://doi.org/10.21236/ad0296199
[research_king_ethridge_1985]: https://ntrs.nasa.gov/citations/19860000620
[research_kiris_dochankwak_2000]: https://doi.org/10.1109/sc.2000.10053
[research_kirk_miller_1962]: https://ntrs.nasa.gov/citations/19620006855
[research_kirkham_jackson_1974]: https://doi.org/10.2514/6.1974-988
[research_kishimoto_morita_2022]: https://doi.org/10.1299/jsmedsd.2022.32.2112
[research_kistler_1959]: https://doi.org/10.1063/1.1705925
[research_kithcart_klett_1995]: https://doi.org/10.1115/imece1995-1139
[research_klausmeyer_2026]: https://doi.org/10.2514/6.2026-1329
[research_klemm_herrmann_1998]: https://doi.org/10.1115/98-gt-480
[research_klimas_1973]: https://doi.org/10.2514/3.44391
[research_klimas_rogers_1975]: https://doi.org/10.2514/6.1975-1368
[research_klineberg_kubota_1970]: https://doi.org/10.2514/6.1970-230
[research_klopfer_nielsen_1979]: https://doi.org/10.21236/ada087134
[research_klopfer_nielsen_1980]: https://doi.org/10.2514/6.1980-126
[research_klueh_king_1977]: https://doi.org/10.2172/5348561
[research_klueh_king_1982]: https://doi.org/10.2172/708749
[research_kluever_2004]: https://doi.org/10.2514/1.7877
[research_kluever_2007]: https://doi.org/10.2514/1.28081
[research_kluever_neal_2015]: https://doi.org/10.2514/1.g000909
[research_klyde_lampton_2014]: https://doi.org/10.2514/6.2014-0447
[research_klyde_lampton_2017]: https://doi.org/10.2514/1.g001486
[research_klyde_liang_2011]: https://ntrs.nasa.gov/citations/20110012219
[research_klyde_mcruer_2008]: https://doi.org/10.2514/6.2008-6209
[research_klyde_thompson_2004]: https://doi.org/10.2514/6.2004-4702
[research_knapp_jordan_1953]: https://ntrs.nasa.gov/citations/19930089110
[research_knight_1982]: https://doi.org/10.21236/ada127118
[research_knight_zheltovodov_2011]: https://doi.org/10.1017/cbo9780511842757.004
[research_ko_grant_2012]: https://doi.org/10.2514/6.2012-4947
[research_kobayashi_daimon_2011]: https://doi.org/10.2514/6.2011-6028
[research_kochan_2020]: https://doi.org/10.30837/itssi.2020.13.129
[research_kochan_breiter_2005]: https://doi.org/10.1177/154193120504900333
[research_kodigaddi_2026]: https://doi.org/10.21203/rs.3.rs-10227402/v1
[research_kogler_quam_1983]: https://doi.org/10.2514/6.1983-366
[research_kohlman_1977]: https://ntrs.nasa.gov/citations/19770054210
[research_koizumi_tomizuka_1986]: https://doi.org/10.1080/02619180.1986.11753319
[research_kokane_mahbuburrahman_2026]: https://doi.org/10.1007/978-981-96-9374-0_17
[research_kolli_2024]: https://doi.org/10.58445/rars.2008
[research_kolodner_1950]: https://doi.org/10.1002/cpa.3160030203
[research_kolonay_yang_1998]: https://doi.org/10.2514/2.7578
[research_kong_pan_2023]: https://doi.org/10.1088/1742-6596/2658/1/012047
[research_konno_furuichi_1992]: https://doi.org/10.1016/b978-0-444-88970-6.50026-9
[research_konrad_smits_1992]: https://doi.org/10.2514/6.1992-310
[research_konrad_smits_1993]: https://doi.org/10.1016/b978-0-444-89802-9.50071-x
[research_koo_2001]: https://doi.org/10.2514/2.2767
[research_koopman_zammitmangion_2025]: https://doi.org/10.2514/6.2025-3337
[research_kopzon_1958]: https://doi.org/10.1016/0021-8928(58)90040-6
[research_korbahti_2009]: https://doi.org/10.1007/s00707-009-0255-3
[research_korbahti_uzal_2004]: https://doi.org/10.1108/00022660410565508
[research_koreanschi_oliviu_2014]: https://doi.org/10.2514/6.2014-3170
[research_korivi_newman_1998]: https://doi.org/10.2514/2.2338
[research_kornev_ambrozhevich_2021]: https://doi.org/10.3103/s1068799821010049
[research_kornilov_1958]: https://doi.org/10.1007/bf03397881
[research_korsun_om_2023]: https://doi.org/10.1007/978-981-19-9010-6_7
[research_korth_2000]: https://doi.org/10.1007/s11837-000-0114-0
[research_kosinov_maslov_1990]: https://doi.org/10.1007/978-3-642-84103-3_20
[research_kosinov_yermolaev_2000]: https://doi.org/10.1007/978-3-662-03997-7_70
[research_kosinov_yermolaev_2000_b]: https://doi.org/10.1007/978-3-662-03997-7_75
[research_kosinov_yermolaev_2017]: https://doi.org/10.1063/1.5007531
[research_kosykh_2025]: https://doi.org/10.62717/2221-4550-2025-1-030
[research_kosykh_2026]: https://doi.org/10.62717/3083-7057-2026-1-027
[research_kou_zhan_2022]: https://doi.org/10.1088/1742-6596/2228/1/012013
[research_kouchakzadeh_rasekh_2010]: https://doi.org/10.1016/j.compstruct.2010.05.001
[research_kovalev_kudryavtsev_2015]: https://doi.org/10.1051/eucass/201507525
[research_kowal_2011]: https://ntrs.nasa.gov/citations/20110012175
[research_kowaleczko_dlugolecki_2018]: https://doi.org/10.2478/jok-2018-0069
[research_kowaleczko_pietraszek_2025]: https://doi.org/10.61089/aot2025.a4bewn26
[research_kozlov_zverkov_2009]: https://doi.org/10.1007/978-90-481-3723-7_89
[research_krasilnikov_shmanenkov_2000]: https://doi.org/10.1023/a:1026655318584
[research_krasnoshapka_1968]: https://doi.org/10.1007/bf00889039
[research_krause_dinkler_1998]: https://doi.org/10.2514/6.1998-1841
[research_krishnan_sandham_2005]: https://doi.org/10.1615/tsfp4.690
[research_krishnaswamy_papageorgiou]: https://doi.org/10.1109/acc.2005.1470177
[research_krivenyuk_tsvilyuk_1971]: https://doi.org/10.1007/bf01533595
[research_kronejr_1980]: https://doi.org/10.2514/6.1980-1882
[research_kronejr_1980_b]: https://doi.org/10.2514/6.1980-3047
[research_kruger_klimmek_2014]: https://doi.org/10.1007/s13272-014-0117-0
[research_kryvokhatko_2023]: https://doi.org/10.1007/978-3-031-23777-5
[research_kryvokhatko_2025]: https://doi.org/10.1007/978-3-031-74809-7
[research_kuchemann_1962]: https://doi.org/10.1016/b978-0-08-006550-2.50019-3
[research_kudryavtsev_2014]: https://doi.org/10.17816/2074-0530-67451
[research_kuhlman_brown_1989]: https://doi.org/10.2514/6.1989-644
[research_kuhlman_cerney_1988]: https://doi.org/10.2514/6.1988-7
[research_kuhlman_liaw_1987]: https://doi.org/10.2514/6.1987-2482
[research_kulfan_sigalla_1978]: https://doi.org/10.2514/6.1978-147
[research_kumar_choubey_2023]: https://doi.org/10.1007/s11085-023-10157-3
[research_kumar_onkar_2023]: https://doi.org/10.1007/s00707-023-03727-8
[research_kumar_rallapalli_2025]: https://doi.org/10.52202/080553-0010
[research_kumari_nath_1982]: https://doi.org/10.1016/0017-9310(82)90016-3
[research_kuo_1976]: https://doi.org/10.2514/6.1976-1531
[research_kuo_morino_1972]: https://doi.org/10.2514/3.6645
[research_kurzin_mazutskii_2013]: https://doi.org/10.1615/tsagiscij.2013007867
[research_kusko_1957]: https://doi.org/10.1109/ee.1957.6442622
[research_kuwata_2021]: https://doi.org/10.1016/j.ijheatfluidflow.2021.108859
[research_kuwata_2026]: https://doi.org/10.1017/jfm.2026.11638
[research_kwak_yoshida_2006]: https://doi.org/10.2514/6.2006-3483
[research_kwatny_belcastro_2008]: https://doi.org/10.2514/6.2008-6506
[research_kwatny_dongmo_2009]: https://doi.org/10.2514/6.2009-6256
[research_kwatny_dongmo_2010]: https://doi.org/10.2514/6.2010-8005
[research_kwon_lee_2004]: https://doi.org/10.2514/6.2004-3363
[research_kyonamkoo]: https://doi.org/10.1109/korus.2002.1027947
[research_kyzmenko_yakovlev_2018]: https://doi.org/10.25206/1813-8225-2018-162-15-18
[research_la_wang_2022]: https://doi.org/10.2139/ssrn.4181386
[research_lacefield_sprow_1994]: https://doi.org/10.2514/6.1994-3397
[research_lacombe_rouges_1990]: https://doi.org/10.2514/6.1990-3837
[research_lada_kontis_2005]: https://doi.org/10.2514/6.2005-1298
[research_lada_kontis_2009]: https://doi.org/10.1007/978-3-540-85181-3_76
[research_ladenburg_bershader_1949]: https://doi.org/10.1103/revmodphys.21.510
[research_laderman_1978]: https://doi.org/10.2514/3.7570
[research_laderman_1979]: https://doi.org/10.21236/ada070254
[research_laderman_demetriades_1977]: https://doi.org/10.21236/ada046365
[research_lafont_bosson_1983]: https://doi.org/10.2514/6.1983-1386
[research_laganelli_1970]: https://doi.org/10.1615/ihtc4.2480
[research_lagerstrom_graham_1949]: https://doi.org/10.2514/8.11719
[research_lai_cunis_2021]: https://doi.org/10.2514/6.2021-0253
[research_lai_findley_1979]: https://doi.org/10.21236/ada070355
[research_lai_findley_1980]: https://doi.org/10.21236/ada095410
[research_lai_huang_1995]: https://doi.org/10.2514/6.1995-3257
[research_laitone_1964]: https://doi.org/10.1007/978-3-642-88337-8_5
[research_lakshmi_ramprabhu_2021]: https://doi.org/10.18520/cs/v120/i1/110-115
[research_lallman_1985]: https://ntrs.nasa.gov/citations/19860001736
[research_lam_stollenwerk_1966]: https://doi.org/10.2514/6.1966-771
[research_lamar_1975]: https://doi.org/10.2514/6.1975-249
[research_lamb_sawyer_1981]: https://ntrs.nasa.gov/citations/19810020557
[research_lamb_sawyer_1981_b]: https://ntrs.nasa.gov/citations/19810052971
[research_lampton_valasek_2006]: https://doi.org/10.2514/6.2006-6834
[research_landweber_johnson_1951]: https://doi.org/10.21236/ada953150
[research_lang_cen_2022]: https://doi.org/10.1007/s42401-022-00156-8
[research_lang_wang_2025]: https://doi.org/10.1109/taes.2025.3571683
[research_langham_1979]: https://doi.org/10.2514/6.1979-1621
[research_langston_nelson_2016]: https://doi.org/10.2514/6.2016-1036
[research_lapin_1999]: https://doi.org/10.1016/s0966-9795(98)00065-x
[research_lapygin_tretyakov_1986]: https://doi.org/10.1007/bf01409732
[research_larsen_litz_1963]: https://doi.org/10.21236/ad0402610
[research_larson_1987]: https://doi.org/10.2514/6.1987-214
[research_lateral_directional_dynamics_1998]: https://doi.org/10.2514/5.9781600862052.0207.0256
[research_lateral_directional_stability_2003]: https://doi.org/10.2514/5.9781600861840.0297.0310
[research_latif_masud_2007]: https://doi.org/10.2514/1.22775
[research_latvala_anderson_1959]: https://doi.org/10.21236/ad0208546
[research_laudeman_1972]: https://doi.org/10.2514/6.1972-780
[research_lavretsky_2019]: https://doi.org/10.2514/6.2019-1081
[research_lavrishcheva_staroverov_2024]: https://doi.org/10.53954/9785604990131_83
[research_law_1973]: https://doi.org/10.2514/6.1973-665
[research_law_1974]: https://doi.org/10.2514/3.49352
[research_law_1975]: https://doi.org/10.2514/6.1975-832
[research_law_1976]: https://doi.org/10.2514/3.61413
[research_lawrence_1964]: https://doi.org/10.2514/6.1964-489
[research_lazarev_1988]: https://doi.org/10.1515/pm-1988-250504
[research_ldsd_ballute_2015]: https://ntrs.nasa.gov/citations/20170008183
[research_ldsd_dynamics_2015]: https://ntrs.nasa.gov/citations/20150009475
[research_leadon_scott_1956]: https://doi.org/10.21236/ad0082502
[research_lebacqz_radford_1974]: https://doi.org/10.4050/vfs-f30-024
[research_lee_1984]: https://doi.org/10.2514/6.1984-820
[research_lee_1989]: https://doi.org/10.2514/3.45783
[research_lee_1993]: https://doi.org/10.2514/6.1993-1209
[research_lee_1994]: https://doi.org/10.2514/3.46621
[research_lee_1994_b]: https://doi.org/10.2514/6.1994-1695
[research_lee_1998]: https://doi.org/10.1615/ihtc11.3690
[research_lee_cho_1991]: https://doi.org/10.1016/0045-7949(91)90084-y
[research_lee_gross_2020]: https://doi.org/10.2514/6.2020-3076
[research_lee_gross_2021]: https://doi.org/10.2514/6.2021-2765
[research_lee_han_2021]: https://doi.org/10.1016/j.fpc.2021.11.014
[research_lee_kim_1994]: https://doi.org/10.2514/3.46667
[research_lee_kim_2010]: https://doi.org/10.1016/j.compstruct.2009.08.022
[research_lee_kim_2013]: https://doi.org/10.2514/6.2013-2658
[research_lee_lee_2023]: https://doi.org/10.1007/s12540-023-01445-3
[research_lee_miura_1990]: https://doi.org/10.1016/0956-0521(90)90009-a
[research_lee_miura_1991]: https://doi.org/10.2514/3.46100
[research_lee_yanta_1969]: https://doi.org/10.21236/ad0697929
[research_lee_yoon_2008]: https://doi.org/10.1016/j.simpat.2007.08.009
[research_lees_1956]: https://doi.org/10.2514/8.6977
[research_lees_1959]: https://doi.org/10.1108/eb033067
[research_lees_reshotko_1962]: https://doi.org/10.21236/ad0288100
[research_lefur_1959]: https://doi.org/10.2514/8.8258
[research_lei_1987]: https://ntrs.nasa.gov/citations/19880020722
[research_lei_1991]: https://ntrs.nasa.gov/citations/19930032424
[research_lei_1992]: https://doi.org/10.2514/6.1992-5039
[research_lei_1992_b]: https://ntrs.nasa.gov/citations/19930004483
[research_lei_1994]: https://ntrs.nasa.gov/citations/19940000020
[research_lei_castelli_1996]: https://ntrs.nasa.gov/citations/19970022434
[research_lei_fichtel_1993]: https://ntrs.nasa.gov/citations/19940014841
[research_lei_williams_1990]: https://ntrs.nasa.gov/citations/19910029839
[research_lei_zhao_2016]: https://doi.org/10.1016/j.cja.2016.06.006
[research_lemcoe_1973]: https://ntrs.nasa.gov/citations/19730009719
[research_lemcoe_1992]: https://ntrs.nasa.gov/citations/19930004481
[research_lemkey_1975]: https://ntrs.nasa.gov/citations/19750000246
[research_lemkey_smeggil_1987]: https://ntrs.nasa.gov/citations/19880022802
[research_lemley_1968]: https://doi.org/10.21236/ad0840550
[research_lemon_litt_2011]: https://doi.org/10.2514/6.2011-6308
[research_leng_1995]: https://doi.org/10.2514/3.21392
[research_lensi_2000]: https://doi.org/10.2514/6.2000-3901
[research_leonard_1938]: https://doi.org/10.2514/8.615
[research_leontiev_lushchik_2006]: https://doi.org/10.1007/s10740-006-0029-8
[research_leontiev_lushchik_2017]: https://doi.org/10.1134/s0018151x17020080
[research_leontiev_lushchik_2022]: https://doi.org/10.1134/s0018151x22030117
[research_leontiev_pavlyuchenko_2004]: https://doi.org/10.1023/b:hite.0000046528.21488.73
[research_leontiev_pavlyuchenko_2008]: https://doi.org/10.1134/s0018151x08040159
[research_leopold_gastebois]: https://doi.org/10.1109/iciasf.2005.1569900
[research_lesalli_cahyono_2020]: https://doi.org/10.28989/senatik.v6i0.402
[research_leslie_1978]: https://doi.org/10.1016/0094-4548(78)90024-3
[research_lesoinne_2007]: https://doi.org/10.21236/ada481320
[research_leto_votta_2016]: https://doi.org/10.1016/j.egypro.2016.11.078
[research_levie_2016]: https://ntrs.nasa.gov/citations/20160006310
[research_levin_1981]: https://doi.org/10.2514/6.1981-1876
[research_levin_1984]: https://doi.org/10.2514/3.48413
[research_levine_1965]: https://doi.org/10.1016/s0082-0784(65)80248-x
[research_levine_rumsey_1958]: https://ntrs.nasa.gov/citations/19980228363
[research_levy_1992]: https://doi.org/10.2514/6.1992-4193
[research_lewis_banner_1971]: https://ntrs.nasa.gov/citations/19720005345
[research_li_2008]: https://doi.org/10.21236/ada482157
[research_li_2023]: https://doi.org/10.54254/2755-2721/10/20230134
[research_li_chen_2017]: https://doi.org/10.1016/j.expthermflusci.2017.04.011
[research_li_chen_2026]: https://doi.org/10.1108/aeat-09-2025-0332
[research_li_eri_2007]: https://doi.org/10.1007/978-3-540-75995-9_90
[research_li_ganippa_2026]: https://doi.org/10.20944/preprints202601.1002.v1
[research_li_ganippa_2026_b]: https://doi.org/10.3390/aerospace13040344
[research_li_geiselhart_2026]: https://doi.org/10.2514/1.c038747
[research_li_han_2021]: https://doi.org/10.1109/accc54619.2021.00014
[research_li_huang_2014]: https://doi.org/10.1016/j.surfcoat.2013.11.024
[research_li_lv_2015]: https://doi.org/10.1016/j.infrared.2015.06.014
[research_li_lv_2022]: https://doi.org/10.3390/ma15217440
[research_li_narita_2015]: https://doi.org/10.1016/j.compstruct.2014.09.011
[research_li_shi_2011]: https://doi.org/10.1109/iceceng.2011.6057605
[research_li_sobieczky_1999]: https://doi.org/10.2514/2.2547
[research_li_song_2013]: https://doi.org/10.1016/j.jsv.2013.05.032
[research_li_stewart_1953]: https://doi.org/10.2514/8.2811
[research_li_wan_2024]: https://doi.org/10.3390/aerospace11070572
[research_li_wei_2023]: https://doi.org/10.20944/preprints202309.0273.v1
[research_li_yamaguchi_2022]: https://doi.org/10.1016/j.surfcoat.2022.128123
[research_li_yang_2013]: https://doi.org/10.4028/www.scientific.net/amm.0.738
[research_li_zhang_2010]: https://doi.org/10.1007/978-1-4419-5754-2_7
[research_li_zhang_2018]: https://doi.org/10.3390/app8122585
[research_li_zu_2019]: https://doi.org/10.1016/j.jallcom.2019.06.222
[research_liang_lu_2026]: https://doi.org/10.1360/ssi-2025-0330
[research_liang_wu_2023]: https://doi.org/10.2139/ssrn.4542433
[research_liang_yang_2022]: https://doi.org/10.3390/aerospace9100593
[research_librescu_marzocca_2004]: https://doi.org/10.2514/1.679
[research_librescu_simovich_1988]: https://doi.org/10.2514/3.45572
[research_librescu_thangjitham_1989]: https://doi.org/10.4271/891056
[research_librescu_thangjitham_1991]: https://doi.org/10.2514/3.46004
[research_licher_1956]: https://doi.org/10.2514/8.3718
[research_liever_habchi_2004]: https://doi.org/10.2514/6.2004-4726
[research_lift_drag_ratios_1962]: https://doi.org/10.1017/s0001925900002274
[research_lift_roll_coupling_1972]: https://ntrs.nasa.gov/citations/19720020370
[research_lijewski_1980]: https://doi.org/10.21236/ada104989
[research_lilley_1965]: https://doi.org/10.1016/b978-0-08-011860-4.50014-8
[research_lim_kim_2020]: https://doi.org/10.6108/kspe.2020.24.4.055
[research_limerick_1991]: https://doi.org/10.2514/6.1991-2209
[research_lin_1986]: https://doi.org/10.2514/6.1986-2474
[research_lin_1999]: https://doi.org/10.1017/s1727719100000356
[research_lin_2025]: https://doi.org/10.5220/0014773000004818
[research_lin_chan_1993]: https://doi.org/10.2514/6.1993-2575
[research_lin_liu_2025]: https://doi.org/10.1016/j.matchar.2025.115653
[research_lin_yang_2005]: https://doi.org/10.1108/00022660510597232
[research_lindley_1956]: https://doi.org/10.1214/aoms/1177728069
[research_linehan_mohseni_2016]: https://doi.org/10.2514/6.2016-1063
[research_lingard_barnard_1989]: https://doi.org/10.2514/6.1989-889
[research_lingard_darley_2005]: https://doi.org/10.2514/6.2005-1607
[research_lingard_underwood_2013]: https://doi.org/10.2514/6.2013-1365
[research_lipatov_tugazakov_2018]: https://doi.org/10.1134/s001546281802012x
[research_liquid_oxygen_2009]: https://doi.org/10.5139/jksas.2009.37.8.805
[research_liquid_propellant_2006]: https://doi.org/10.2514/5.9781600868870.0293.0302
[research_liquid_rocket]: https://doi.org/10.4271/arp4900
[research_liquid_rocket_1995]: https://doi.org/10.2514/4.866371
[research_liquid_rocket_2018]: https://doi.org/10.4271/0768093333
[research_lisunov_1960]: https://doi.org/10.1016/0021-8928(60)90159-3
[research_litt_liu_2014]: https://doi.org/10.2514/6.2014-0036
[research_littell_bailey_1967]: https://doi.org/10.4271/670575
[research_littleboy_smith_1997]: https://doi.org/10.2514/6.1997-3717
[research_liu_2022]: https://doi.org/10.1007/978-981-19-4586-1_12
[research_liu_2024]: https://doi.org/10.1088/1742-6596/2691/1/012030
[research_liu_cook_2019]: https://doi.org/10.2514/6.2019-0209
[research_liu_gao_2022]: https://doi.org/10.1049/icp.2022.1775
[research_liu_gao_2025]: https://doi.org/10.1016/j.jallcom.2025.184096
[research_liu_grant_2009]: https://doi.org/10.2514/6.2009-5828
[research_liu_grant_2010]: https://doi.org/10.2514/6.2010-7797
[research_liu_li_2012]: https://doi.org/10.4028/www.scientific.net/amr.538-541.1601
[research_liu_li_2013]: https://doi.org/10.1109/iscid.2013.206
[research_liu_li_2021]: https://doi.org/10.1116/6.0000776
[research_liu_li_2022]: https://doi.org/10.1016/j.ceramint.2021.12.310
[research_liu_liu_2023]: https://doi.org/10.2139/ssrn.4590657
[research_liu_liu_2024]: https://doi.org/10.1016/j.energy.2024.132861
[research_liu_liu_2027]: https://doi.org/10.1016/j.ast.2026.113723
[research_liu_lu_2011]: https://doi.org/10.21236/ada564811
[research_liu_luo_2021]: https://doi.org/10.1103/physrevfluids.6.044603
[research_liu_lv_2012]: https://doi.org/10.4028/www.scientific.net/amr.490-495.2314
[research_liu_natesan_1988]: https://doi.org/10.1557/proc-119-213
[research_liu_oshida_1984]: https://ntrs.nasa.gov/citations/19840012606
[research_liu_pang_2023]: https://doi.org/10.1016/j.measurement.2023.113165
[research_liu_platzer_1970]: https://doi.org/10.2514/6.1970-190
[research_liu_wang_1995]: https://doi.org/10.2514/6.1995-3117
[research_liu_weng_2007]: https://doi.org/10.1007/978-3-540-75995-9_87
[research_liu_yin_2011]: https://doi.org/10.1117/12.880323
[research_liu_zhang_2025]: https://doi.org/10.1063/5.0282257
[research_livne_2023]: https://doi.org/10.2514/6.2023-0228
[research_livne_2023_b]: https://doi.org/10.2514/6.2023-0229
[research_livne_2023_c]: https://doi.org/10.2514/6.2023-0230
[research_livne_2023_d]: https://doi.org/10.2514/6.2023-0231
[research_livne_mineau_1996]: https://doi.org/10.2514/6.1996-4172
[research_livneh_1995]: https://doi.org/10.2514/3.56682
[research_livneh_1995_b]: https://doi.org/10.2514/6.1995-3307
[research_loads_calibration_1977]: https://ntrs.nasa.gov/citations/20020086520
[research_loads_flutter_conf_1957]: https://ntrs.nasa.gov/citations/19710070068
[research_lobanovskii_1983]: https://doi.org/10.1007/bf01090577
[research_loc_directions_2014]: https://ntrs.nasa.gov/citations/20200007706
[research_loc_precursors_2014]: https://ntrs.nasa.gov/citations/20140003949
[research_locci_brady_2000]: https://ntrs.nasa.gov/citations/20050192197
[research_lock_1958]: https://doi.org/10.1017/s002211205800029x
[research_lock_1963]: https://doi.org/10.1017/s0001924000062758
[research_lock_bridgewater_1967]: https://doi.org/10.1016/0376-0421(67)90004-8
[research_logan_davis_2007]: https://doi.org/10.2514/6.2007-459
[research_lombaerts_2019]: https://ntrs.nasa.gov/citations/20190000458
[research_lombaerts_schuet_2016]: https://ntrs.nasa.gov/citations/20170000836
[research_longitudinal_and_2014]: https://doi.org/10.1201/b17346-10
[research_longlu_turkoglu_2015]: https://doi.org/10.1109/aero.2015.7118952
[research_loposer_rumsey_1954]: https://ntrs.nasa.gov/citations/20030068110
[research_lorch_1981]: https://doi.org/10.21236/ada109808
[research_lorenz_lam_2026]: https://doi.org/10.2514/6.2026-3830
[research_lores_zinn_1973]: https://doi.org/10.2514/6.1973-217
[research_loss_of_control_mishaps]: https://doi.org/10.4271/air6237
[research_loth_lee_2008]: https://doi.org/10.21236/ada478600
[research_lottati_1985]: https://doi.org/10.2514/3.45238
[research_lottati_1985_b]: https://doi.org/10.2514/3.9141
[research_lottati_1987]: https://doi.org/10.2514/3.45523
[research_lotze_sensburg_1975]: https://doi.org/10.2514/6.1975-1025
[research_lotze_sensburg_1977]: https://doi.org/10.2514/3.58786
[research_lovell_2001]: https://doi.org/10.1007/978-3-540-45359-8_14
[research_low_aspect_1992]: https://doi.org/10.2514/3.11843
[research_low_disturbance_tunnels_1990]: https://ntrs.nasa.gov/citations/19900050881
[research_low_frequency_2008]: https://doi.org/10.2514/5.9781600866913.0001.0042
[research_lowe_byun_2014]: https://doi.org/10.2514/6.2014-0233
[research_lowell_barrett_1990]: https://ntrs.nasa.gov/citations/19900015895
[research_lowenberg_2010]: https://doi.org/10.1002/9780470686652.eae255
[research_lowry_mellen_1994]: https://doi.org/10.1520/jfs13699j
[research_lu]: https://doi.org/10.31979/etd.4ys8-zqt7
[research_lu_turkoglu_2016]: https://doi.org/10.2514/6.2016-1624
[research_lu_turkoglu_2018]: https://doi.org/10.1155/2018/8654031
[research_luce_jr_1949]: https://doi.org/10.21236/ada278113
[research_lucero_1984]: https://doi.org/10.2514/6.1984-575
[research_lucero_1985]: https://doi.org/10.2514/3.25719
[research_ludloff_reiche_1947]: https://doi.org/10.1063/1.1697825
[research_ludtke_1973]: https://doi.org/10.21236/ad0768755
[research_ludtke_1986]: https://doi.org/10.2514/6.1986-2440
[research_luikov_sergeev_1967]: https://doi.org/10.1016/0017-9310(67)90026-9
[research_lukashevich_morozov_2023]: https://doi.org/10.1063/5.0133158
[research_lunev_1971]: https://doi.org/10.1007/bf01019801
[research_lungu_lungu_2015]: https://doi.org/10.1002/asjc.1133
[research_lungu_lungu_2016]: https://doi.org/10.1016/j.neucom.2015.06.084
[research_luruixia_niaoqinghu_2008]: https://doi.org/10.1109/isscaa.2008.4776202
[research_lushchik_reshmin_2025]: https://doi.org/10.1134/s0015462825603882
[research_lutz_1989]: https://doi.org/10.2514/3.10185
[research_luu_ochi_2023]: https://doi.org/10.2322/tastj.21.1
[research_luxton_1968]: https://doi.org/10.1017/s0001925900004649
[research_lyrio_azevedo_2019]: https://doi.org/10.26678/abcm.cobem2019.cob2019-1123
[research_lysenko_1987]: https://ntrs.nasa.gov/citations/19870007364
[research_lysenko_1989]: https://doi.org/10.1007/bf01075167
[research_lysenko_1995]: https://doi.org/10.1007/978-3-642-79765-1_25
[research_lysenko_maslov_1981]: https://doi.org/10.1007/bf00907553
[research_lysenko_maslov_1985]: https://doi.org/10.1007/978-3-642-82462-3_60
[research_lysenko_smorodsky_2017]: https://doi.org/10.1063/1.5007535
[research_lysenko_smorodsky_2025]: https://doi.org/10.7868/s3034534025040041
[research_lyu_gong_2022]: https://doi.org/10.1155/2022/2490675
[research_lyu_ye_2023]: https://doi.org/10.3390/app13116598
[research_m_saini_2023]: https://doi.org/10.2139/ssrn.4559948
[research_ma_han_2021]: https://doi.org/10.1016/j.corsci.2021.109417
[research_ma_he_2012]: https://doi.org/10.1515/htmp-2011-0150
[research_ma_su_2017]: https://doi.org/10.2991/mecae-17.2017.72
[research_mabey_gaudet_1975]: https://doi.org/10.2514/3.44494
[research_macaiii_lee_1996]: https://doi.org/10.2514/6.1996-3499
[research_macedo]: https://doi.org/10.11606/d.18.2021.tde-08022022-160017
[research_macedo_bidinotto_2020]: https://doi.org/10.2514/6.2020-2911
[research_mach_number_1978]: https://doi.org/10.2514/5.9781600865336.0156.0174
[research_mach_number_2022]: https://doi.org/10.15394/eaglepub.2022.1066.n13
[research_machida_takatoya_2007]: https://doi.org/10.2514/6.2007-2118
[research_machida_yoshida_2007]: https://doi.org/10.2514/6.2007-854
[research_maciejewski_1995]: https://doi.org/10.1115/imece1995-1127
[research_mackay_nagamatsu_1954]: https://doi.org/10.2514/8.2922
[research_macmillen_thompson_1999]: https://doi.org/10.1007/978-94-011-5320-1_45
[research_macmurdy_guruswamy_1994]: https://doi.org/10.2514/6.1994-1587
[research_madagan_1969]: https://doi.org/10.2514/6.1969-133
[research_maddalon_collier_1990]: https://doi.org/10.1007/978-3-642-84103-3_4
[research_maekawa_watanabe_2007]: https://doi.org/10.1115/ht2007-32910
[research_maestrello_1969]: https://doi.org/10.1016/0022-460x(69)90200-4
[research_magee_fugal_2015]: https://ntrs.nasa.gov/citations/20160000771
[research_magee_hayes_2022]: https://doi.org/10.2514/6.2022-1802
[research_magee_hayes_2024]: https://doi.org/10.2514/6.2024-0900
[research_magee_hayes_2025]: https://doi.org/10.2514/6.2025-2363
[research_mahlmeister_ishimoto_1955]: https://doi.org/10.21236/ad0093337
[research_mahorter_robertg_1961]: https://doi.org/10.21236/ad0266590
[research_maikapar_1966]: https://doi.org/10.1016/0021-8928(66)90071-2
[research_maikapar_1993]: https://doi.org/10.1007/bf01050055
[research_mailybaev_seiranyan_1998]: https://doi.org/10.1007/bf02698170
[research_majumder_2019]: https://doi.org/10.26634/jme.9.3.15806
[research_makarov_pavlenko_2016]: https://doi.org/10.2514/6.2016-3723
[research_makino_noguchi_2003]: https://doi.org/10.2514/6.2003-3574
[research_malcolm_rakich_1970]: https://doi.org/10.2514/6.1970-554
[research_malcolm_rakich_1971]: https://doi.org/10.2514/3.6205
[research_malecka_2016]: https://doi.org/10.5772/63998
[research_malik_li_1993]: https://doi.org/10.2514/6.1993-77
[research_maloney_2011]: https://ntrs.nasa.gov/citations/20110012275
[research_manavasi_morell_2011]: https://doi.org/10.2514/6.2011-307
[research_mangano_martins_2021]: https://doi.org/10.2514/1.c036216
[research_manjhi_kumar_2018]: https://doi.org/10.1080/08916152.2018.1431738
[research_manjhi_kumar_2020]: https://doi.org/10.1007/978-981-15-0124-1_63
[research_manjith_2026]: https://doi.org/10.31224/8400
[research_mann_carlson_1991]: https://doi.org/10.2514/6.1991-3302
[research_mann_carlson_1994]: https://doi.org/10.2514/3.46452
[research_mann_mercer_1985]: https://doi.org/10.2514/6.1985-4069
[research_mansor_nogoud_2015]: https://doi.org/10.1109/iccneee.2015.7381444
[research_mansour_1984]: https://doi.org/10.2514/6.1984-522
[research_mansy_gobran_1982]: https://doi.org/10.1515/9783112494387-008
[research_manzuk_1970]: https://doi.org/10.2514/6.1970-1211
[research_mao_guo_2023]: https://doi.org/10.54097/hset.v77i.14411
[research_mao_li_2022]: https://doi.org/10.3390/met12061029
[research_mao_liang_2019]: https://doi.org/10.1051/matecconf/201929102005
[research_mao_lin_2011]: https://doi.org/10.2514/1.c031196
[research_mao_xie_2019]: https://doi.org/10.1155/2019/5847627
[research_maode_sandstrom_1988]: https://doi.org/10.1080/02619180.1988.11753393
[research_maples_1979]: https://doi.org/10.21236/ada069807
[research_maqsood_go_2011]: https://doi.org/10.1007/s11071-011-0300-3
[research_mardanpour_richards_2013]: https://doi.org/10.2514/6.2013-1571
[research_mardanpour_richards_2014]: https://doi.org/10.1016/j.jfluidstructs.2013.09.018
[research_markov_1984]: https://doi.org/10.1007/bf01093921
[research_martin_1953]: https://doi.org/10.2514/8.2561
[research_martin_1956]: https://doi.org/10.1017/s000192400012648x
[research_martin_2007]: https://doi.org/10.1109/aero.2007.352949
[research_martin_2008]: https://doi.org/10.2514/6.2008-7337
[research_martin_baker_at_1988]: https://doi.org/10.1108/eb036720
[research_martin_gerber_1953]: https://doi.org/10.21236/ad0005479
[research_martin_gerber_1953_b]: https://doi.org/10.21236/ad0014217
[research_martin_gerber_1955]: https://doi.org/10.2514/8.3301
[research_martin_panesi_2022]: https://doi.org/10.2514/1.a35029
[research_martina_1958]: https://doi.org/10.1520/stp45045s
[research_martinez_1961]: https://doi.org/10.21236/ad0265941
[research_martinez_reinert_1990]: https://doi.org/10.2514/6.1990-2236
[research_martos_kiszely_2011]: https://doi.org/10.2514/6.2011-6669
[research_maruyama_bi_1992]: https://doi.org/10.1016/b978-0-444-88970-6.50039-7
[research_maruyama_matsushima_2009]: https://doi.org/10.2514/1.40313
[research_maruyama_oikawa_1978]: https://doi.org/10.1016/0036-9748(78)90185-0
[research_marzocca_librescu_2001]: https://doi.org/10.2514/6.2001-714
[research_mashburn_1969]: https://doi.org/10.21236/ad0690947
[research_maslov_aniskin_2016]: https://doi.org/10.1063/1.4963927
[research_mason_1983]: https://doi.org/10.2514/6.1983-1858
[research_mason_ravi_1994]: https://doi.org/10.2514/3.46520
[research_masoudi_1999]: https://doi.org/10.1016/s0017-9310(99)00018-6
[research_mastanaiah_1978]: https://doi.org/10.1016/0017-9310(78)90204-1
[research_masterson_1963]: https://doi.org/10.21236/ad0408957
[research_mastropietro_pauken_2013]: https://doi.org/10.2514/6.2013-3348
[research_masud_arif_2017]: https://doi.org/10.2514/6.2017-0269
[research_masud_khan_2018]: https://doi.org/10.2514/6.2018-2057
[research_mateescu_1986]: https://doi.org/10.2514/6.1986-1826
[research_mateju_2019]: https://doi.org/10.13164/conf.read.2018.13
[research_mathematical_modeling_2018]: https://doi.org/10.15593/perm.mech/eng.2018.3.09
[research_mathew_parameswaran_2008]: https://doi.org/10.1016/j.matchar.2007.03.007
[research_matsumoto_sekiya_1975]: https://doi.org/10.1299/kikai1938.41.736
[research_matsuo_butler_1983]: https://doi.org/10.21236/ada139928
[research_matsuo_kim_1993]: https://doi.org/10.1007/bf01414745
[research_matsushita_miyata]: https://doi.org/10.1109/sice.2002.1195240
[research_matthews_1957]: https://doi.org/10.21236/ad0127419
[research_matthews_buchanan_1972]: https://ntrs.nasa.gov/citations/19720013207
[research_matthews_prince_2025]: https://doi.org/10.2514/6.2025-2831
[research_maxwell_jacocks_1962]: https://doi.org/10.21236/ad0270596
[research_may_lemon_2011]: https://doi.org/10.2514/6.2011-6307
[research_may_li_2023]: https://doi.org/10.3390/math11061462
[research_mayer_kruelle_1992]: https://doi.org/10.2514/6.1992-3389
[research_mayle_blair_1979]: https://doi.org/10.1115/1.3451021
[research_maziasz_2004]: https://doi.org/10.2172/885787
[research_maziasz_swindeman_2001]: https://doi.org/10.2172/940246
[research_mcalarney_arons_1982]: https://doi.org/10.1007/bf02642884
[research_mcamis_lankford_1992]: https://doi.org/10.2514/6.1992-3730
[research_mccarty_smith_1982]: https://doi.org/10.2514/6.1982-705
[research_mccutchen_2006]: https://doi.org/10.2514/1.12330
[research_mcdonough_kolmanovsky_2014]: https://doi.org/10.2514/6.2014-0786
[research_mcdonough_kolmanovsky_2017]: https://doi.org/10.2514/1.g001747
[research_mcelderry_1973]: https://doi.org/10.21236/ada377039
[research_mcewan_1970]: https://doi.org/10.2514/6.1970-1168
[research_mcgrath_1993]: https://doi.org/10.2514/6.1993-3505
[research_mcgrath_1995]: https://doi.org/10.2514/3.46805
[research_mcgrath_2003]: https://doi.org/10.2514/6.2003-4667
[research_mcgrath_walker_1989]: https://doi.org/10.2514/6.1989-2193
[research_mchugh_leszcz_2024]: https://doi.org/10.1115/ssdm2024-121670
[research_mckee_1967]: https://doi.org/10.4271/670528
[research_mckenna_walker_1964]: https://doi.org/10.2514/6.1964-81
[research_mcmillin_wood_1986]: https://doi.org/10.2514/6.1986-1799
[research_mcmullen_1973]: https://doi.org/10.2514/6.1973-440
[research_mcmurtrey_2018]: https://doi.org/10.2172/1484686
[research_mctavish]: https://doi.org/10.22215/etd/2008-08205
[research_mehra_carroll_1980]: https://doi.org/10.2514/6.1980-1599
[research_mehta_1986]: https://doi.org/10.1007/bf00999733
[research_mehta_2012]: https://doi.org/10.1007/s00231-012-1095-6
[research_mei_1977]: https://doi.org/10.2514/3.60760
[research_mei_1978]: https://doi.org/10.2514/3.7401
[research_mei_zhang_2012]: https://doi.org/10.1115/1.4006948
[research_meier_1975]: https://doi.org/10.1007/bf01681557
[research_meier_rotta_1971]: https://doi.org/10.2514/3.50021
[research_meisl_1986]: https://doi.org/10.2514/6.1986-1408
[research_melek_kaya_2009]: https://doi.org/10.1109/rast.2009.5158184
[research_melville_gordnier_1998]: https://doi.org/10.2514/6.1998-2657
[research_melvilljones_1938]: https://doi.org/10.1108/eb030310
[research_melvin_zhao_2024]: https://doi.org/10.1115/1.4066309
[research_meng_kaihua_2020]: https://doi.org/10.1109/icus50048.2020.9274846
[research_menshchikov_somov_2019]: https://doi.org/10.1063/1.5086976
[research_meritt_schetz_2017]: https://doi.org/10.2514/6.2017-3982
[research_merkli_1975]: https://doi.org/10.21236/ada033630
[research_merlet_rumsey_1961]: https://ntrs.nasa.gov/citations/19980230644
[research_methodic_for_2024]: https://doi.org/10.36652/0042-4633-2024-103-8-672-678
[research_methodology_for]: https://doi.org/10.4271/air5875
[research_metin_uzuner_2023]: https://doi.org/10.2514/6.2023-1572
[research_meyer_1958]: https://doi.org/10.21236/ad0208856
[research_meyers_duong_2025]: https://doi.org/10.1017/jfm.2025.10288
[research_mi_2021]: https://doi.org/10.1016/j.dt.2020.06.005
[research_mi_yi_2023]: https://doi.org/10.2139/ssrn.4587629
[research_michaelsen_1957]: https://doi.org/10.1108/eb032860
[research_mickey_stuartjr_1967]: https://doi.org/10.2514/6.1967-202
[research_microstructure_and_2025]: https://doi.org/10.3901/jme.2025.04.137
[research_mielke_kleiser_1999]: https://doi.org/10.1063/1.4739160
[research_mielke_kleiser_2000]: https://doi.org/10.1007/978-3-662-03997-7_59
[research_mikhail_1979]: https://doi.org/10.21236/ada076116
[research_mikhail_1989]: https://doi.org/10.2514/6.1989-332
[research_mikilyan_2024]: https://doi.org/10.1109/aero58975.2024.10521224
[research_miles_1949]: https://doi.org/10.2514/8.11836
[research_miles_1953]: https://doi.org/10.1017/s0001925900000901
[research_militky_wiener_2025]: https://doi.org/10.3390/eng6040080
[research_millard_machin_1989]: https://doi.org/10.2514/6.1989-19
[research_miller_franklin_1968]: https://doi.org/10.2514/3.43919
[research_miller_jr_1975]: https://doi.org/10.21236/ada014805
[research_miller_langdon_1980]: https://doi.org/10.1016/0036-9748(80)90090-3
[research_miller_schemensky_1979]: https://doi.org/10.2514/6.1979-62
[research_miller_wood_1983]: https://doi.org/10.2514/6.1983-1816
[research_miller_wykes_1982]: https://doi.org/10.2514/6.1982-683
[research_miller_wykes_1983]: https://doi.org/10.2514/3.44931
[research_mills_2002]: https://doi.org/10.21236/ada402603
[research_min_jinjun_2026]: https://doi.org/10.2514/1.c039058
[research_miner_lewis_1973]: https://doi.org/10.2514/6.1973-696
[research_ming_bingjun_2016]: https://doi.org/10.1109/aus.2016.7748198
[research_mingde_1984]: https://doi.org/10.1007/bf01875890
[research_miniature_high_1972]: https://doi.org/10.1111/j.1475-1305.1972.tb01762.x
[research_minkina_1999]: https://doi.org/10.1524/teme.1999.66.10.399
[research_mironov_1965]: https://doi.org/10.1007/bf00831824
[research_mishina_umeoka_2020]: https://doi.org/10.1299/jsmemecj.2020.j19104
[research_mitcham_1949]: https://ntrs.nasa.gov/citations/20010062502
[research_mitcham_blanchard_1951]: https://ntrs.nasa.gov/citations/20050030030
[research_mitcham_stevens_1956]: https://ntrs.nasa.gov/citations/19930084649
[research_mitchell_1969]: https://doi.org/10.2514/6.1969-483
[research_mitikiri_mohseni_2018]: https://doi.org/10.2514/6.2018-0876
[research_mitrotta_pirrera_2025]: https://doi.org/10.2514/6.2025-2811
[research_miura_2010]: https://doi.org/10.3182/20100906-5-jp-2022.00026
[research_miura_fukai_1983]: https://doi.org/10.1252/kakoronbunshu.9.642
[research_miyazawa_1973]: https://ntrs.nasa.gov/citations/19740059647
[research_miyazawa_1974]: https://ntrs.nasa.gov/citations/19750007829
[research_mizoguchi_kajikawa_2014]: https://doi.org/10.2514/6.2014-2014
[research_mlddleton_carlson_1965]: https://doi.org/10.2514/3.43650
[research_mobley_summers]: https://ntrs.nasa.gov/citations/20240009390
[research_moffat_kays_1984]: https://doi.org/10.1016/s0065-2717(08)70206-5
[research_moffeit_kumar_2023]: https://doi.org/10.2514/6.2023-1191
[research_moftakhar_glinka_1998]: https://doi.org/10.1115/98-gt-263
[research_moga_1980]: https://doi.org/10.21236/ada091235
[research_moga_dejarnette_1981]: https://doi.org/10.2514/6.1981-75
[research_moger_ramsay_1964]: https://doi.org/10.21236/ad0601589
[research_mohamed_dongare_2021]: https://doi.org/10.1007/978-981-16-0104-0_4
[research_mohamed_joy_2021]: https://doi.org/10.1017/aer.2021.61
[research_mohammadi_mehdi_2015]: https://doi.org/10.5120/ijca2015907034
[research_mohammadiun_rahimi_2012]: https://doi.org/10.2514/1.t3833
[research_mohammed_2007]: https://doi.org/10.30684/etj.25.6.5
[research_moin_lele_1998]: https://doi.org/10.21236/ada343835
[research_molins_andrieu_1991]: https://doi.org/10.7449/1991/superalloys_1991_589_602
[research_molloy_1999]: https://doi.org/10.21236/ada389456
[research_monaghan_1953]: https://doi.org/10.2514/8.2563
[research_monaghan_friend_1973]: https://ntrs.nasa.gov/citations/19730019173
[research_monel_k500_1989]: https://ntrs.nasa.gov/citations/19910032246
[research_montgomery_hatch_1969]: https://doi.org/10.2514/3.44061
[research_montoya_1970]: https://ntrs.nasa.gov/citations/19700026377
[research_moog_1975]: https://doi.org/10.2514/6.1975-1381
[research_moon_2003]: https://doi.org/10.1016/s0167-4730(02)00049-8
[research_moon_2004]: https://doi.org/10.1016/s0263-8223(04)00094-7
[research_moon_kim_2001]: https://doi.org/10.2514/6.2001-1658
[research_moore_1991]: https://ntrs.nasa.gov/citations/19930032613
[research_moore_frei_1983]: https://doi.org/10.2514/6.1983-1834
[research_moore_mcdonald_1946]: https://doi.org/10.1520/stp44974s
[research_moore_morse_2024]: https://doi.org/10.2514/6.2024-86251
[research_moore_skow_1980]: https://doi.org/10.2514/6.1980-173
[research_moorthamers_wiberg_2021]: https://doi.org/10.2514/6.2021-1825
[research_morajkar_gamba_2016]: https://doi.org/10.2514/6.2016-1590
[research_moreira_gripp_2022]: https://doi.org/10.2514/1.g006443
[research_morelli_cunningham_2013]: https://doi.org/10.2514/6.2013-4976
[research_morikawa_1951]: https://doi.org/10.2514/8.1915
[research_morikawa_1953]: https://doi.org/10.2514/8.2607
[research_morimoto_yamashita_2015]: https://doi.org/10.2514/6.2015-2080
[research_morino_1969]: https://doi.org/10.2514/3.5121
[research_morito_sidwell_1967]: https://doi.org/10.2514/6.1967-1140
[research_morris_1966]: https://doi.org/10.2514/6.1966-770
[research_morrisette_goldberg_1978]: https://ntrs.nasa.gov/citations/19780022611
[research_morton_1956]: https://doi.org/10.1108/eb032772
[research_moshtaghzadeh_izadpanahi_2022]: https://doi.org/10.2514/6.2022-0536
[research_moulton_abraham_2024]: https://doi.org/10.2514/6.2024-2480
[research_mueller_torres_2001]: https://doi.org/10.21236/ada397533
[research_muhlsteinjr_1966]: https://doi.org/10.2514/6.1966-769
[research_muhlsteinjr_1972]: https://doi.org/10.2514/6.1972-402
[research_mukambetov_borovik_2022]: https://doi.org/10.18698/2308-6033-2022-1-2146
[research_mukherjee_martin_1963]: https://doi.org/10.1016/0022-5088(63)90004-3
[research_mukherjee_sinha_2016]: https://doi.org/10.2514/6.2016-1037
[research_mullendore_grant_1964]: https://doi.org/10.1016/b978-0-08-010580-2.50009-8
[research_muller_1967]: https://doi.org/10.2514/3.59369
[research_muller_traudt_2021]: https://doi.org/10.1088/1742-6596/1909/1/012049
[research_multifractal_detrended_2023]: https://doi.org/10.37285/bsp.sasat2023.19
[research_mumaw_haworth_2019]: https://ntrs.nasa.gov/citations/20190004927
[research_munk_1950]: https://doi.org/10.1063/1.1699616
[research_murakami_kwak_2008]: https://doi.org/10.2514/6.2008-7488
[research_murashkin_bruyaka_2020]: https://doi.org/10.3103/s1068799820010158
[research_murphy_klein_2010]: https://doi.org/10.2514/6.2010-8122
[research_murphy_voss_1996]: https://doi.org/10.2514/6.1996-3277
[research_murray_1961]: https://doi.org/10.21236/ad0256874
[research_murri_croom_1983]: https://doi.org/10.2514/6.1983-1837
[research_murtaza_indluru_2026]: https://doi.org/10.25259/ijasm_5_2025
[research_murzionak]: https://doi.org/10.22215/etd/2013-06868
[research_musa_mansor_2015]: https://doi.org/10.2514/6.2015-1498
[research_musa_mansor_2026]: https://doi.org/10.2139/ssrn.7319830
[research_muthaiah_saini_2025]: https://doi.org/10.1016/j.apacoust.2024.110361
[research_myers_walsh_1988]: https://doi.org/10.2514/6.1988-2175
[research_mysliwetz_1963]: https://doi.org/10.2514/3.1821
[research_nabdulwahab_2009]: https://doi.org/10.30684/etj.27.7.11
[research_naca_1135]: https://ntrs.nasa.gov/citations/19930091059
[research_nadimmelhem_richardmunroe_2024]: https://doi.org/10.1201/9781003516903-2
[research_nae_2026]: https://doi.org/10.2514/6.2026-2110
[research_naftaly_raveh_2025]: https://doi.org/10.2514/6.2025-1021
[research_nagelschmidt_herbrich_2025]: https://doi.org/10.1016/j.engfracmech.2025.111582
[research_nair_vaidyanathan_2022]: https://doi.org/10.1016/j.asr.2022.03.023
[research_najafi_kharrat_2024]: https://doi.org/10.2139/ssrn.4952360
[research_nakai_takagi_1967]: https://doi.org/10.2514/6.1967-1340
[research_nam_moon_2018]: https://doi.org/10.6108/kspe.2018.22.6.104
[research_nangia_palmer_2003]: https://doi.org/10.2514/6.2003-605
[research_napolitano_kincheloe_1996]: https://doi.org/10.2514/6.1996-3851
[research_narayan_1974]: https://doi.org/10.1017/s0001925900006880
[research_narayan_1975]: https://doi.org/10.1017/s0001925900007332
[research_narayan_kumar_2025]: https://doi.org/10.1108/aeat-10-2024-0288
[research_nardirezende_2018]: https://doi.org/10.4271/r-465
[research_narita_hayashi_2001]: https://doi.org/10.5006/c2001-01157
[research_narita_sakata_2023]: https://doi.org/10.1201/9781003421498-14
[research_natali_rallini_2013]: https://doi.org/10.1002/mame.201300267
[research_navalordnancesystemscommandwashingtondc_1957]: https://doi.org/10.21236/ada278207
[research_nbarufaldi_hvictorjr_2020]: https://doi.org/10.48011/asba.v2i1.1319
[research_negaard_1979]: https://doi.org/10.21236/ada363019
[research_nelsen_1995]: https://doi.org/10.2514/6.1995-1558
[research_nelson_bresnahan_1983]: https://doi.org/10.2514/6.1983-1287
[research_nemish_chernopiskii_1974]: https://doi.org/10.1007/bf00882951
[research_nepomuceno_moura_2022]: https://doi.org/10.2514/6.2022-4059
[research_nestler_1978]: https://doi.org/10.1615/ihtc6.2800
[research_nettleton_1965]: https://doi.org/10.2514/6.1965-713
[research_neumann_freeman_2012]: https://doi.org/10.2514/1.a32201
[research_newell_rajagopal_1993]: https://doi.org/10.1115/93-gt-238
[research_newey]: https://doi.org/10.15368/theses.2020.107
[research_newman_buttrill_1995]: https://doi.org/10.2514/6.1995-3250
[research_newmaniii_newman_1999]: https://doi.org/10.1016/s0045-7930(98)00047-4
[research_newsom_anglin_1975]: https://ntrs.nasa.gov/citations/19750022036
[research_newton_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50006-3
[research_nguyen_1979]: https://doi.org/10.4271/791083
[research_nguyen_2008]: https://doi.org/10.2514/6.2008-194
[research_nguyen_2025]: https://doi.org/10.5937/vojtehg73-57712
[research_nguyen_lowenberg_2021]: https://doi.org/10.2514/1.g005197
[research_nguyen_popov_2017]: https://doi.org/10.2514/6.2017-0822
[research_nguyen_sirignano_2018]: https://doi.org/10.2514/6.2018-4948
[research_nguyen_sirignano_2019]: https://doi.org/10.2514/1.j057743
[research_nguyen_ting_2016]: https://doi.org/10.2514/6.2016-1094
[research_nguyen_ting_2017]: https://doi.org/10.2514/6.2017-4219
[research_ni_lu_2016]: https://doi.org/10.3390/en9030154
[research_ni_wang_2025]: https://doi.org/10.1088/1742-6596/3044/1/012001
[research_nichols_1974]: https://ntrs.nasa.gov/citations/19740025212
[research_nickel_fu_1992]: https://doi.org/10.1115/92-gt-434
[research_nicolaides_brady_1959]: https://doi.org/10.21236/ad0219843
[research_nie_song_2022]: https://doi.org/10.2514/1.c036377
[research_niel]: https://doi.org/10.70675/0a5746acz2780z42a1z83e4zb2dace818ceb
[research_nielsen_1986]: https://doi.org/10.2514/6.1986-568
[research_niemi_jr_1992]: https://doi.org/10.21236/ada250882
[research_nietogomez_chimenomanguan_2025]: https://doi.org/10.3390/aerospace12090783
[research_nietubicz_1975]: https://doi.org/10.21236/ada009704
[research_nikbay_oncu_2009]: https://doi.org/10.2514/1.41491
[research_nikulin_kaibyshev_2010]: https://doi.org/10.1088/1742-6596/240/1/012071
[research_nilsson_sandstrom_1988]: https://doi.org/10.1080/02619180.1988.11753398
[research_nix_1982]: https://doi.org/10.21236/ada125199
[research_nix_1984]: https://doi.org/10.21236/ada151107
[research_njuguna_2007]: https://doi.org/10.1002/stc.170
[research_nobakhti_soltani_2014]: https://doi.org/10.1111/ext.12104
[research_nobakhti_soltani_2016]: https://doi.org/10.1007/s40799-016-0067-z
[research_noll_calico_1983]: https://doi.org/10.2514/6.1983-2220
[research_noll_eastep_1983]: https://doi.org/10.2514/6.1983-991
[research_noll_eastep_1984]: https://doi.org/10.2514/3.48246
[research_nomura_2003]: https://doi.org/10.2514/6.2003-4145
[research_non_linear_throttling_1999]: https://doi.org/10.1016/s0140-6701(99)98484-9
[research_nonconstant_cma_1977]: https://ntrs.nasa.gov/citations/19780032271
[research_nonlinear_panel_1991]: https://doi.org/10.2514/6.1991-1172
[research_nonweiler_1959]: https://doi.org/10.1017/s0368393100071662
[research_northropaircraftinchawthorneca_1952]: https://doi.org/10.21236/ad0004591
[research_northropaircraftinchawthorneca_1952_b]: https://doi.org/10.21236/ad0024361
[research_northropaircraftinchawthorneca_1953]: https://doi.org/10.21236/ad0013465
[research_northropaircraftinchawthorneca_1953_b]: https://doi.org/10.21236/ad0022941
[research_nose_capsule_1949]: https://ntrs.nasa.gov/citations/20050019284
[research_nouri_sahmani_2019]: https://doi.org/10.1088/2053-1591/ab56ab
[research_novopashin_1985]: https://doi.org/10.1007/978-3-642-82462-3_65
[research_nowak_kelly_1976]: https://doi.org/10.2514/6.1976-1523
[research_nowak_kelly_1977]: https://doi.org/10.2514/3.58769
[research_numerical_method_2016]: https://doi.org/10.1002/9781118890035.ch8
[research_numerical_studies_2003]: https://doi.org/10.5293/kfma.2003.6.4.050
[research_nusca_1984]: https://doi.org/10.2514/6.1984-325
[research_nusca_2007]: https://doi.org/10.2514/6.2007-5562
[research_nusca_2008]: https://doi.org/10.2514/6.2008-4545
[research_nusca_2010]: https://doi.org/10.2514/6.2010-1518
[research_nyman_1965]: https://doi.org/10.2172/4588085
[research_nyquist_1928]: https://doi.org/10.1109/T-AIEE.1928.5055024
[research_oblique_wing_divergence_1973]: https://ntrs.nasa.gov/citations/19730009309
[research_obrien_frazier]: https://doi.org/10.1109/naecon.1989.40304
[research_odabas_karaoglanli_2025]: https://doi.org/10.1016/j.surfcoat.2025.132439
[research_odonnell_mohseni_2017]: https://doi.org/10.2514/6.2017-1270
[research_of_current_1958]: https://doi.org/10.1109/ee.1958.6445643
[research_ofarrell_brandeau_2016]: https://doi.org/10.2514/6.2016-3242
[research_ofarrell_clark_2022]: https://doi.org/10.1109/aero53065.2022.9843430
[research_ofarrell_karlgaard_2018]: https://doi.org/10.1109/aero.2018.8396502
[research_ofarrell_leylek_2023]: https://doi.org/10.1109/aero55745.2023.10115818
[research_ogburn_1998]: https://ntrs.nasa.gov/citations/20040090522
[research_oggioni_riboldi_2026]: https://doi.org/10.3390/engproc2026142017
[research_ogren_sotanski_1974]: https://doi.org/10.21236/ad0784134
[research_oh_shin_2024]: https://doi.org/10.5139/jksas.2024.52.3.201
[research_ohara_1971]: https://doi.org/10.1017/s0001924000045358
[research_ohira_kwak_2013]: https://doi.org/10.2514/6.2013-342
[research_ojetola_onyebueke_2011]: https://doi.org/10.4271/2011-01-0806
[research_ojiaku_prakash_2026]: https://doi.org/10.21203/rs.3.rs-9271663/v1
[research_okayasu_higashino_1983]: https://doi.org/10.2514/6.1983-1388
[research_okayasu_ohta_2002]: https://doi.org/10.1016/s0094-5765(01)00163-1
[research_oktay_asma_2000]: https://doi.org/10.2514/6.2000-392
[research_okumoto_elsanker_1973]: https://doi.org/10.21236/ad0767182
[research_okuno_park_1968]: https://ntrs.nasa.gov/citations/19680025282
[research_oldrieve_1975]: https://ntrs.nasa.gov/citations/19750015688
[research_olejnik_zalewski_2020]: https://doi.org/10.5604/01.3001.0014.8874
[research_olsen_seegmiller_1993]: https://doi.org/10.2514/3.49105
[research_olson_1967]: https://doi.org/10.2514/3.4422
[research_olsson_1978]: https://doi.org/10.2514/3.7530
[research_olstad_1969]: https://doi.org/10.2514/3.5062
[research_om_childs_1982]: https://ntrs.nasa.gov/citations/19820048416
[research_oorebeek_babinsky_2013]: https://doi.org/10.2514/6.2013-526
[research_opalka_1968]: https://doi.org/10.21236/ad0393552
[research_optimal_design_2004]: https://doi.org/10.5139/jksas.2004.32.5.091
[research_optimum_time_1942]: https://doi.org/10.1016/s0016-0032(42)90434-4
[research_orlikruckemann_laberge_1972]: https://doi.org/10.2514/3.61771
[research_orme_conners_1994]: https://doi.org/10.2514/6.1994-3210
[research_orme_gilyard_1993]: https://doi.org/10.2514/6.1993-1821
[research_ormsbee_1962]: https://doi.org/10.21236/ad0295993
[research_ortamevzi_2015]: https://doi.org/10.20535/2219-380413201569737
[research_ortega_flores_2017]: https://doi.org/10.2514/1.c033677
[research_osherov_natan_1999]: https://doi.org/10.1017/s0001924000027913
[research_osipov_2019]: https://doi.org/10.26467/2079-0619-2019-22-1-63-75
[research_oswatitsch_1980]: https://doi.org/10.1007/978-3-322-91082-0_19
[research_ott_anderson_1994]: https://doi.org/10.2514/3.553
[research_otto_flage_1960]: https://doi.org/10.4271/600403
[research_ouhabi_narsipur_2025]: https://doi.org/10.1017/aer.2024.131
[research_ouyang_zeng_2021]: https://doi.org/10.1155/2021/5535192
[research_ouyang_zhang_2026]: https://doi.org/10.1016/j.ast.2026.112419
[research_owen_1969]: https://doi.org/10.2514/6.1969-9
[research_owen_1971]: https://doi.org/10.1016/0017-9310(71)90163-3
[research_owens_wahls_2001]: https://doi.org/10.2514/6.2001-911
[research_owens_wahls_2007]: https://doi.org/10.2514/1.22519
[research_oxidation_ignition_1956]: https://ntrs.nasa.gov/citations/19930093830
[research_oyibo_1983]: https://doi.org/10.2514/3.8145
[research_oyibo_1984]: https://doi.org/10.2514/3.48423
[research_ozcan_tekyurt_2025]: https://doi.org/10.23919/iccas66577.2025.11301141
[research_ozcatalbas_acar_2018]: https://doi.org/10.1109/icmae.2018.8467693
[research_ozer_2025]: https://doi.org/10.1109/access.2025.3648550
[research_ozozturk_kayran_2011]: https://doi.org/10.2514/6.2011-1918
[research_padova_falk_1980]: https://doi.org/10.21236/ada088831
[research_pages_achipa_2026]: https://doi.org/10.2514/6.2026-114634
[research_pahutova_cadek_1969]: https://doi.org/10.1016/0001-6160(69)90080-7
[research_pakhomov_2015]: https://doi.org/10.1134/s1028335815120071
[research_palakurthy_zope_2022]: https://doi.org/10.2514/6.2022-0738
[research_palchekovskaya_2014]: https://doi.org/10.1615/ihtc15.tdy.009827
[research_palej_palacz_2018]: https://doi.org/10.2478/tar-2018-0024
[research_palmer_henline_1995]: https://doi.org/10.2514/6.1995-2080
[research_pan_cao_2021]: https://doi.org/10.1088/1742-6596/2012/1/012100
[research_pan_huang_2018]: https://doi.org/10.1177/0954410018817449
[research_pan_huang_2019]: https://doi.org/10.5028/jatm.v11.1074
[research_pan_wu_2010]: https://doi.org/10.1016/j.optlaseng.2010.04.007
[research_pan_zhang_2026]: https://doi.org/10.3390/en19071616
[research_panel_flutter_1991]: https://doi.org/10.2514/6.1991-746
[research_pany_2023]: https://doi.org/10.2339/politeknik.1139958
[research_papirno_gerard_1962]: https://doi.org/10.21236/ada398798
[research_pappas_1954]: https://ntrs.nasa.gov/citations/19930084126
[research_parate_2020]: https://doi.org/10.28991/hij-2020-01-03-03
[research_parate_2022]: https://doi.org/10.1080/23311916.2022.2034267
[research_park_ahn_1998]: https://doi.org/10.2514/6.1998-832
[research_park_ahn_1999]: https://doi.org/10.2514/2.6426
[research_park_ahn_2020]: https://doi.org/10.1016/j.actaastro.2020.08.019
[research_park_green_2000]: https://doi.org/10.2514/6.2000-4321
[research_park_jeon_2024]: https://doi.org/10.2139/ssrn.4801252
[research_park_lee_2001]: https://doi.org/10.2514/6.2001-4014
[research_park_lee_2024]: https://doi.org/10.1007/s42405-024-00760-2
[research_park_moon_2024]: https://doi.org/10.1016/j.ijheatmasstransfer.2024.125917
[research_parker_spain_1991]: https://doi.org/10.2514/6.1991-936
[research_parkinson_skorodelov_1995]: https://doi.org/10.1016/0094-5765(95)00089-i
[research_parks_1965]: https://doi.org/10.2514/6.1965-1108
[research_parks_1966]: https://doi.org/10.2514/3.3412
[research_parlett_1961]: https://ntrs.nasa.gov/citations/19980227999
[research_pasiuk_1963]: https://doi.org/10.21236/ad0448887
[research_pasiuk_hastings_1963]: https://doi.org/10.2514/3.1760
[research_passos]: https://doi.org/10.11606/t.18.2025.tde-10062025-150419
[research_pastuszko_chauvo_2024]: https://doi.org/10.52202/078371-0218
[research_patel_2016]: https://doi.org/10.2514/6.2016-4415
[research_patel_czarnecki_1975]: https://ntrs.nasa.gov/citations/19760005228
[research_patel_czarnecki_1977]: https://ntrs.nasa.gov/citations/19770026495
[research_patil_2003]: https://doi.org/10.2514/6.2003-1487
[research_patil_hodges_2000]: https://doi.org/10.2514/6.2000-1627
[research_patnaik_guptill_1998]: https://doi.org/10.2514/2.2395
[research_patterson_1966]: https://ntrs.nasa.gov/citations/19660008599
[research_pauck_engelbrecht_2012]: https://doi.org/10.2514/6.2012-4646
[research_pavlyuchenko_tyutin_1985]: https://doi.org/10.1007/978-3-642-82462-3_68
[research_payne_1969]: https://doi.org/10.2514/3.44048
[research_payne_1973]: https://doi.org/10.1017/s0001924000040331
[research_payne_band_1976]: https://doi.org/10.21236/ada038193
[research_pchiozzotto_2016]: https://doi.org/10.1007/s13272-016-0204-5
[research_pearson_1960]: https://ntrs.nasa.gov/citations/19670022687
[research_pearson_1961]: https://ntrs.nasa.gov/citations/19630010659
[research_pecora_pecora_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00014-9
[research_pedersen_1961]: https://doi.org/10.21236/ad0267502
[research_peichl_wortmann_1987]: https://doi.org/10.1007/978-94-009-1347-9_36
[research_pelletier_mueller_1999]: https://doi.org/10.2514/6.1999-3182
[research_pellettlere_nguyen_2003]: https://doi.org/10.21236/ada417363
[research_peltzer_nitsche_2008]: https://doi.org/10.2514/1.35184
[research_pempie_vernin_2001]: https://doi.org/10.2514/6.2001-3256
[research_penkalla_schubert_1988]: https://doi.org/10.7449/1988/superalloys_1988_643_652
[research_pepelea_cojocaru_2018]: https://doi.org/10.1063/1.5081592
[research_pereira_roberts_1997]: https://ntrs.nasa.gov/citations/20050179347
[research_perera_guo_2008]: https://doi.org/10.2514/6.2008-5969
[research_perez_hader_2025]: https://doi.org/10.2514/6.2025-3602
[research_perez_johns_2024]: https://doi.org/10.2514/6.2024-84114
[research_perkins_halljr_1993]: https://doi.org/10.2514/6.1993-3991
[research_perraud_moens_2003]: https://doi.org/10.2514/6.2003-3796
[research_perry_2007]: https://doi.org/10.21236/ada519316
[research_pervaiz_erler_1994]: https://doi.org/10.4271/941209
[research_peters_phares_1976]: https://doi.org/10.21236/ada030015
[research_petersen_1981]: https://doi.org/10.2514/6.1981-2417
[research_peterson_1961]: https://ntrs.nasa.gov/citations/19980227076
[research_peterson_2024]: https://doi.org/10.2514/6.2024-2873
[research_peterson_derkevorkian_2018]: https://doi.org/10.2514/6.2018-1539
[research_peterson_menees_1961]: https://ntrs.nasa.gov/citations/20040008213
[research_peterson_roberts_1973]: https://doi.org/10.2514/6.1973-480
[research_pfaff_1965]: https://doi.org/10.21236/ad0467448
[research_pharokhipanah_bouckenooghe_2024]: https://doi.org/10.52202/078371-0178
[research_phillips_1948]: https://ntrs.nasa.gov/citations/19930082293
[research_phinney_1974]: https://doi.org/10.1016/0094-4548(74)90156-8
[research_piacentino_mcenerney_1978]: https://doi.org/10.21236/ada062429
[research_piccoloserafim_freydin_2023]: https://doi.org/10.2514/6.2023-0584
[research_pickl_1989]: https://doi.org/10.2514/6.1989-878
[research_pieniazek_2025]: https://doi.org/10.3390/s25154634
[research_pierson_1972]: https://doi.org/10.2514/6.1972-170
[research_pierson_1975]: https://doi.org/10.1002/nme.1620090203
[research_pierson_chen_1979]: https://doi.org/10.2514/3.58520
[research_pilot_escape_1961]: https://doi.org/10.1108/eb033385
[research_piltch_jihfen_1994]: https://ntrs.nasa.gov/citations/20060005568
[research_pinsky_essary_1994]: https://doi.org/10.2514/3.21238
[research_pint_pellettiere_2003]: https://doi.org/10.4271/2003-01-2212
[research_pipko_1966]: https://doi.org/10.21236/ad0646293
[research_pish_moradi_2019]: https://doi.org/10.1016/j.actaastro.2018.10.021
[research_pitcher_maple_2008]: https://doi.org/10.2514/6.2008-4057
[research_pitchup_control_1960]: https://ntrs.nasa.gov/citations/19980227095
[research_pitchup_evaluation_1955]: https://ntrs.nasa.gov/citations/19930092243
[research_pitot_supersonic_1948]: https://ntrs.nasa.gov/citations/19930085521
[research_pitt_2004]: https://doi.org/10.2514/6.2004-1754
[research_pittman_bonhaus_1987]: https://doi.org/10.2514/6.1987-2638
[research_pittman_siclari_1984]: https://doi.org/10.2514/3.45047
[research_pitts_murbach_1982]: https://doi.org/10.2514/6.1982-840
[research_pittsburghunivwashingtondcresearchstaff_1966]: https://doi.org/10.21236/ad0482131
[research_pivko_1956]: https://doi.org/10.1108/eb032722
[research_pizzaia_rossmann_2018]: https://doi.org/10.1063/1.5056540
[research_placco_2023]: https://doi.org/10.21741/9781644902677-20
[research_placco_2023_b]: https://doi.org/10.21741/9781644902813-42
[research_placco_hancock_2026]: https://doi.org/10.1007/s00707-026-04659-9
[research_plath]: https://doi.org/10.70675/9415f5c4zb15ez4e25z87c4z376e176813a2
[research_platou_1959]: https://doi.org/10.21236/ad0212064
[research_platzer_sherer_1967]: https://doi.org/10.2514/6.1967-607
[research_platzer_sherer_1968]: https://doi.org/10.2514/3.29366
[research_plaut_1968]: https://doi.org/10.2514/3.4719
[research_plaut_1971]: https://doi.org/10.2514/3.6143
[research_pleasants_1975]: https://doi.org/10.2514/6.1975-1403
[research_pletcher_1971]: https://doi.org/10.2514/6.1971-165
[research_plummer_mendelev]: https://ntrs.nasa.gov/citations/20250009647
[research_podnebesnov_1984]: https://doi.org/10.1007/bf00861133
[research_pohuliaiko_vernyhora_2026]: https://doi.org/10.5162/ettc2026/b1.1
[research_polak_1974]: https://doi.org/10.2514/3.49497
[research_pollock_wild_2024]: https://doi.org/10.2139/ssrn.4765698
[research_poolla_ishihara_2015]: https://doi.org/10.4236/ica.2015.64023
[research_pope_1968]: https://doi.org/10.2514/3.4554
[research_popescu_1999]: https://doi.org/10.1023/a:1008348332176
[research_popescu_2000]: https://doi.org/10.2514/6.2000-1624
[research_popov_sideris_2013]: https://doi.org/10.2514/6.2013-3777
[research_popov_sideris_2014]: https://doi.org/10.2514/6.2014-0134
[research_popov_sideris_2016]: https://doi.org/10.2514/6.2016-1932
[research_popov_sideris_2017]: https://doi.org/10.2514/1.j055276
[research_popytalov_samsonov_1978]: https://doi.org/10.1007/bf01050534
[research_porter_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50011-7
[research_portnoy_1961]: https://doi.org/10.1093/qjmam/14.1.29
[research_posingies_1968]: https://doi.org/10.21236/ad0680275
[research_pothjr_fisher_1993]: https://doi.org/10.2514/6.1993-3955
[research_potvin_2007]: https://doi.org/10.2514/1.24061
[research_potvin_potvin_1997]: https://doi.org/10.2514/6.1997-1544
[research_potvin_ray_2019]: https://doi.org/10.2514/6.2019-3486
[research_pourtakdoust_fazelzadeh_2003]: https://doi.org/10.1023/a:1025616916033
[research_prakash_ganapathi_2023]: https://doi.org/10.61653/joast.v56i4.2004.843
[research_prakash_uthup_2009]: https://doi.org/10.2514/6.2009-3631
[research_prandtl_1928]: https://ntrs.nasa.gov/citations/19930090813
[research_prata_2022]: https://doi.org/10.2514/1.j060516
[research_prathap_1978]: https://doi.org/10.2514/3.60973
[research_prediction_of_2010]: https://doi.org/10.1533/9780857090805.2.297
[research_prelim_static_1954]: https://ntrs.nasa.gov/citations/20090026295
[research_preliminary_design_1983]: https://doi.org/10.2514/5.9781600865626.0385.0415
[research_prescott_mitchell_1992]: https://doi.org/10.1016/b978-0-444-88970-6.50014-2
[research_pressure_fluctuations_1975]: https://doi.org/10.2514/5.9781600865121.0243.0262
[research_pressure_temperature_relation_1958]: https://doi.org/10.1016/0043-1648(58)90011-5
[research_pressurization_of_2019]: https://doi.org/10.1017/9781108581714.009
[research_price_1943]: https://doi.org/10.1108/eb031071
[research_price_1964]: https://doi.org/10.2514/6.1964-146
[research_price_1965]: https://doi.org/10.1016/s0082-0784(65)80247-8
[research_price_1980]: https://doi.org/10.2514/6.1980-1260
[research_price_earla_1970]: https://doi.org/10.21236/ad0871144
[research_priest_ernisse_2010]: https://doi.org/10.2514/6.2010-8009
[research_princetonunivnj_1952]: https://doi.org/10.21236/ad0036008
[research_pritchard_1969]: https://doi.org/10.1007/bf00932462
[research_pritchard_carroll_2013]: https://doi.org/10.1115/pvp2013-97251
[research_probstein_1953]: https://doi.org/10.21236/ad0009822
[research_procacci_digiorgio_2026]: https://doi.org/10.1017/jfm.2026.11546
[research_prokopenko_2026]: https://doi.org/10.62717/3083-7057-2026-1-030
[research_properties_and_2012]: https://doi.org/10.2514/5.9781600869228.0338.0438
[research_propulsion_backup_1997]: https://ntrs.nasa.gov/citations/19970017380
[research_propulsion_systems_1991]: https://doi.org/10.2514/5.9781600866104.0021.0100
[research_pryzybylski_1990]: https://doi.org/10.1016/b978-0-08-040423-3.50030-6
[research_pspiridakos_cmarkatos_2020]: https://doi.org/10.5772/intechopen.91041
[research_pugh_goman_2023]: https://doi.org/10.3850/978-981-18-8071-1_p628-cd
[research_purvis_1983]: https://doi.org/10.2514/3.56727
[research_purvis_1984]: https://doi.org/10.2514/6.1984-786
[research_purvis_1984_b]: https://doi.org/10.2514/6.1984-787
[research_pustovyi_2026]: https://doi.org/10.62717/3083-7057-2026-1-031
[research_putman_1969]: https://doi.org/10.21236/ad0859807
[research_putnam_1983]: https://doi.org/10.2514/6.1983-2687
[research_qasrawi_east_1981]: https://doi.org/10.1017/s0001925900008982
[research_qayoum_panigrahi_2014]: https://doi.org/10.1080/01457632.2014.923980
[research_qi_cheng_2022]: https://doi.org/10.3390/aerospace9120788
[research_qi_zhang_2026]: https://doi.org/10.1016/j.ast.2025.111340
[research_qian_tang_2026]: https://doi.org/10.1016/j.cej.2026.182575
[research_qiao_zhou_2018]: https://doi.org/10.2514/6.2018-4148
[research_qiao_zhou_2019]: https://doi.org/10.1109/aero.2019.8742016
[research_qin_xu_2017]: https://doi.org/10.1016/j.actaastro.2016.12.037
[research_qin_zhang_2016]: https://doi.org/10.2514/6.2016-5087
[research_qiu_dai_2021]: https://doi.org/10.1109/iscsic54682.2021.00016
[research_qu_xie_2026]: https://doi.org/10.3390/coatings16010116
[research_quan_lianyiwang_2022]: https://doi.org/10.1016/j.compositesb.2022.109906
[research_quinn_1986]: https://ntrs.nasa.gov/citations/19860019481
[research_quinn_gong_1978]: https://ntrs.nasa.gov/citations/19780024122
[research_rabinovitch_asad_2022]: https://doi.org/10.2514/6.2022-2746
[research_rabinovitch_griffin_2019]: https://doi.org/10.2514/6.2019-1629
[research_rabinovitch_huang_2018]: https://doi.org/10.2514/6.2018-1542
[research_rabinovitch_huang_2019]: https://doi.org/10.2514/6.2019-3275
[research_radkey_welge_1976]: https://doi.org/10.2514/6.1976-955
[research_radkey_welge_1978]: https://doi.org/10.2514/3.58369
[research_rafi_steck_2012]: https://doi.org/10.2514/6.2012-4444
[research_rafi_steck_2013]: https://doi.org/10.2514/6.2013-5209
[research_rafi_steck_2017]: https://doi.org/10.2514/6.2017-1716
[research_rafi_steck_2019]: https://doi.org/10.2514/6.2019-0368
[research_rafi_steck_2020]: https://doi.org/10.2514/6.2020-0850
[research_rafi_steck_2021]: https://doi.org/10.2514/6.2021-0757
[research_raghavan_ananthkrishnan_2005]: https://doi.org/10.2514/6.2005-6029
[research_raghavan_ananthkrishnan_2023]: https://doi.org/10.61653/joast.v61i3.2009.554
[research_ragulin_shvalev_1983]: https://doi.org/10.1007/bf00827075
[research_rahimian_ji_2017]: https://doi.org/10.1007/978-3-319-51541-0_52
[research_rahman_bandal_2024]: https://doi.org/10.1201/9781003450252-63
[research_rahman_bandal_2025]: https://doi.org/10.1007/s12046-025-02758-2
[research_rahman_chandel_2024]: https://doi.org/10.1051/matecconf/202439303002
[research_rain_erosion_1955]: https://doi.org/10.1108/eb032564
[research_rainen_ekvall_1988]: https://doi.org/10.1007/bf03258903
[research_rajadas_juryiv_1998]: https://doi.org/10.2514/6.1998-1818
[research_rajamurthy_2002]: https://doi.org/10.2514/6.2002-4712
[research_rajamurugu_satyam_2024]: https://doi.org/10.15282/ijame.21.2.2024.3.0866
[research_rajamurugu_satyam_2024_b]: https://doi.org/10.4273/ijvss.16.1.04
[research_rajaram_rafi_2017]: https://doi.org/10.2514/6.2017-1022
[research_raju_chandra_1978]: https://doi.org/10.2514/3.60929
[research_rakow_waas_2004]: https://doi.org/10.2514/6.2004-1710
[research_rakow_waas_2005]: https://doi.org/10.2514/1.9741
[research_raman_1999]: https://doi.org/10.2514/2.2523
[research_rambacher_butler_2024]: https://doi.org/10.2514/6.2024-1936
[research_ramirez_haque_2017]: https://doi.org/10.1115/pvp2017-65816
[research_rand_1963]: https://doi.org/10.21236/ad0419249
[research_randels_1954]: https://doi.org/10.2514/8.3250
[research_ransbury_carroll_2014]: https://doi.org/10.2514/6.2014-1006
[research_rao_lundgren_1997]: https://ntrs.nasa.gov/citations/19970012796
[research_rapid_compression_1961]: https://ntrs.nasa.gov/citations/20150020857
[research_rasmussen_1978]: https://doi.org/10.21236/ada068003
[research_ratnayake_waggoner_2011]: https://doi.org/10.2514/6.2011-3014
[research_raveh_levy_2004]: https://doi.org/10.2514/6.2004-1515
[research_ravi_mason_1994]: https://doi.org/10.2514/3.46519
[research_ray_kassing_1986]: https://doi.org/10.2514/6.1986-276
[research_razgonyaev_mason_1995]: https://doi.org/10.2514/6.1995-759
[research_razi_ghadiri_2008]: https://doi.org/10.1243/09544100jaero224
[research_re_1974]: https://ntrs.nasa.gov/citations/19830002754
[research_rea_pecora_2017]: https://doi.org/10.18178/ijmerr.6.6.
[research_rea_pecora_2018]: https://doi.org/10.18178/ijmerr.6.6.440-450
[research_readshaw_1961]: https://doi.org/10.1108/eb033353
[research_real_gas_boundary_layer_1986]: https://ntrs.nasa.gov/citations/19860035065
[research_real_gas_facility_1987]: https://ntrs.nasa.gov/citations/19880000661
[research_real_gas_stability_1991]: https://ntrs.nasa.gov/citations/19910051830
[research_real_gas_trim_1989]: https://ntrs.nasa.gov/citations/19890041076
[research_reardon_1989]: https://ntrs.nasa.gov/citations/19890018663
[research_reardon_1997]: https://doi.org/10.1016/s0010-2180(96)00180-0
[research_reardon_crocco_1964]: https://doi.org/10.2514/3.2631
[research_rechter_harada_1961]: https://doi.org/10.21236/ad0276261
[research_reda_1977]: https://doi.org/10.21236/ada054591
[research_reddy_saikia_2014]: https://doi.org/10.2514/1.t4190
[research_redford_sandham_2009]: https://doi.org/10.1007/978-90-481-3723-7_54
[research_reed_1984]: https://doi.org/10.2514/6.1984-1678
[research_regan_1964]: https://doi.org/10.21236/ad0600975
[research_rehman_2022]: https://doi.org/10.13111/2066-8201.2022.14.3.8
[research_reibert_saric_1997]: https://doi.org/10.2514/6.1997-1816
[research_reich_raveh_2002]: https://doi.org/10.2514/6.2002-1633
[research_reichert]: https://doi.org/10.31274/rtd-180813-9238
[research_reigel_2004]: https://ntrs.nasa.gov/citations/20050186586
[research_reimann_franze_2026]: https://doi.org/10.2514/6.2026-0414
[research_reimer_braun]: https://doi.org/10.1007/978-3-540-36183-1_31
[research_ren_zhang_2021]: https://doi.org/10.1016/j.applthermaleng.2021.116677
[research_render_bello_2026]: https://doi.org/10.1080/09603409.2026.2708541
[research_rene41_panels_1975]: https://ntrs.nasa.gov/citations/19750015960
[research_resende_1992]: https://doi.org/10.2514/6.1992-2128
[research_reshotko_khan_1980]: https://doi.org/10.1007/978-3-642-81485-3_18
[research_reubush_mercer_1974]: https://ntrs.nasa.gov/citations/19740020411
[research_reuter_mcgehee]: https://doi.org/10.17077/etd.005195
[research_reuther_2002]: https://doi.org/10.2514/6.2002-2838
[research_reuther_alonso_1999]: https://doi.org/10.1016/s0045-7930(98)00050-4
[research_reuther_jameson_1995]: https://doi.org/10.1115/imece1995-0954
[research_reuther_rimlinger_1996]: https://doi.org/10.2514/6.1996-4045
[research_reynolds_sst_2002]: https://ntrs.nasa.gov/citations/20020023445
[research_rezaei_jafari_2025]: https://doi.org/10.1016/j.icheatmasstransfer.2025.108959
[research_rezende_2021]: https://doi.org/10.2514/6.2021-3358
[research_rhee_lee_2008]: https://doi.org/10.1007/s12206-008-0514-6
[research_rhisat_molki_2024]: https://doi.org/10.1115/imece2024-144718
[research_rhodeside_1986]: https://doi.org/10.2514/6.1986-492
[research_ribeiro_casalino_2022]: https://doi.org/10.2139/ssrn.4314579
[research_ribeiro_casalino_2022_b]: https://doi.org/10.2514/6.2022-3595
[research_ricciardi_trout_2026]: https://doi.org/10.2514/6.2026-2285
[research_rice_1981]: https://doi.org/10.21236/ada233316
[research_rice_flandro_2010]: https://doi.org/10.2514/6.2010-7153
[research_richards_gandhi_2012]: https://doi.org/10.2514/6.2012-4821
[research_richards_gandhi_2016]: https://doi.org/10.2514/6.2016-0879
[research_richards_gandhi_2018]: https://doi.org/10.2514/6.2018-1864
[research_richecoeur_ducruix_2008]: https://doi.org/10.1016/j.actaastro.2006.12.034
[research_rieken_berry_2020]: https://ntrs.nasa.gov/citations/20200002796
[research_rigby_rae_1989]: https://doi.org/10.2514/6.1989-1690
[research_rimer_chipman_1983]: https://doi.org/10.2514/6.1983-2125
[research_rimer_chipman_1984]: https://doi.org/10.2514/6.1984-1866
[research_rimer_chipman_1986]: https://doi.org/10.2514/3.20069
[research_ritter_dillinger_2017]: https://doi.org/10.2514/6.2017-0637
[research_ritter_fehrs_2023]: https://doi.org/10.2514/6.2023-0762
[research_ritter_hilger_2021]: https://doi.org/10.2514/6.2021-1713
[research_rivard_1965]: https://doi.org/10.2514/6.1965-560
[research_rivers_glass_2006]: https://ntrs.nasa.gov/citations/20060020757
[research_rizk_benshmuel_1985]: https://doi.org/10.2514/6.1985-168
[research_rizzetta_1995]: https://doi.org/10.2514/6.1995-2282
[research_rizzi_delvo_1997]: https://doi.org/10.1007/978-1-4615-5947-4_186
[research_ro_barlow_1992]: https://doi.org/10.2514/6.1992-46
[research_roach_vanecho_1981]: https://doi.org/10.5006/c1981-81238
[research_roach_vanecho_1984]: https://doi.org/10.5006/c1984-84014
[research_robert_1988]: https://ntrs.nasa.gov/citations/19890010487
[research_roberts_1948]: https://doi.org/10.1002/sapm194827149
[research_roberts_1999]: https://doi.org/10.3141/1662-02
[research_robertson_charles_2006]: https://ntrs.nasa.gov/citations/20110013586
[research_robins_carlson_1979]: https://doi.org/10.2514/6.1979-1871
[research_robinson_1948]: https://doi.org/10.1093/qjmam/1.1.408
[research_robinson_1952]: https://doi.org/10.21236/ad0019401
[research_robinson_ouhabi_2025]: https://doi.org/10.2514/6.2025-3234
[research_robinson_robinson_1950]: https://doi.org/10.21236/adb812174
[research_rocha_saska_2023]: https://doi.org/10.1109/icuas57906.2023.10156610
[research_rochadacosta]: https://doi.org/10.22215/etd/2017-11781
[research_rock_habchi_1997]: https://doi.org/10.21236/ada353481
[research_rock_habchi_1998]: https://doi.org/10.2514/6.1998-767
[research_rock_habchi_1999]: https://doi.org/10.2514/6.1999-3184
[research_rocket_model_heating_1959]: https://ntrs.nasa.gov/citations/19980232232
[research_rocket_powered_aircraft_2017]: https://doi.org/10.2307/j.ctvx072b5.11
[research_rocketdynecanogaparkca_1961]: https://doi.org/10.21236/ad0257300
[research_rodden_1964]: https://doi.org/10.2514/3.2614
[research_rodden_1989]: https://doi.org/10.2514/3.45825
[research_rodden_1989_b]: https://doi.org/10.2514/3.45842
[research_rodden_bellinger_1982]: https://doi.org/10.2514/3.61559
[research_rodgers_1992]: https://doi.org/10.2514/6.1992-2400
[research_rodrigues_2026]: https://doi.org/10.2514/1.t7458
[research_roe_kattus_1957]: https://doi.org/10.21236/ad0142003
[research_roecker_1955]: https://doi.org/10.21236/ad0078604
[research_roelke_green_2025]: https://doi.org/10.2514/6.2025-2422
[research_roemer_ge_2011]: https://doi.org/10.2514/6.2011-6369
[research_rogal_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50004-x
[research_rohl_schrage_1992]: https://doi.org/10.2514/6.1992-4721
[research_rohling_1969]: https://doi.org/10.2514/3.44097
[research_rohrbach_knublauch_1968]: https://doi.org/10.1515/mt-1968-100401
[research_roland_edwards_2016]: https://doi.org/10.2514/6.2016-5364
[research_roll_coupling_balance_1973]: https://ntrs.nasa.gov/citations/19740003568
[research_roll_damping_2023]: https://doi.org/10.37285/bsp.sasat2023.22
[research_rolling_maneuvers_1996]: https://doi.org/10.2514/5.9781600862465.0027.0036
[research_rolls_arayici_1985]: https://doi.org/10.1080/02619180.1985.11753295
[research_rollstin_1986]: https://doi.org/10.2514/6.1986-2558
[research_rom_1965]: https://doi.org/10.21236/ad0617943
[research_rom_seginer_1970]: https://doi.org/10.21236/ad0710347
[research_romanenko_kharchenko_1963]: https://doi.org/10.1016/0017-9310(63)90043-7
[research_rongrong_zhengyin_2018]: https://doi.org/10.1177/0954410018807810
[research_rooks_novotny_2020]: https://doi.org/10.1093/milmed/usaa519
[research_roos_1985]: https://doi.org/10.2514/6.1985-1609
[research_rosa_1982]: https://doi.org/10.1016/0010-938x(82)90094-4
[research_rosales_stoltzfus_2009]: https://doi.org/10.1520/jai102287
[research_rose_miller_1988]: https://doi.org/10.2514/6.1988-480
[research_rose_pittman_1989]: https://doi.org/10.2514/6.1989-343
[research_rose_stankevics_1963]: https://doi.org/10.21236/ad0406269
[research_rosen_pavish_1979]: https://doi.org/10.2514/6.1979-141
[research_rosen_pavish_1980]: https://doi.org/10.2514/6.1980-135
[research_rosenberg_1944]: https://doi.org/10.2514/8.11091
[research_rosli_razak_2022]: https://doi.org/10.30880/ijie.2022.14.08.013
[research_ross_1972]: https://doi.org/10.2514/3.58967
[research_ross_2021]: https://doi.org/10.1109/mspec.2021.9311455
[research_rossmann_pizzaia_2014]: https://doi.org/10.2514/6.2014-0590
[research_rotordynamic_analysis_2008]: https://doi.org/10.5139/jksas.2008.36.7.688
[research_rouillard_cabet_2009]: https://doi.org/10.1016/j.corsci.2009.01.019
[research_roux_bontoux_1975]: https://doi.org/10.2514/3.49802
[research_roux_cruciani_2007]: https://doi.org/10.2514/6.2007-6630
[research_row_fischel_1963]: https://doi.org/10.2514/6.1963-75
[research_rowell_1964]: https://doi.org/10.4271/640327
[research_roy_saikia_2019]: https://doi.org/10.2514/6.2019-0339
[research_roysdon_khalid_2010]: https://doi.org/10.2514/6.2010-9167
[research_roysdon_khalid_2011]: https://doi.org/10.2514/6.2011-1563
[research_ruan_xiao_2025]: https://doi.org/10.1017/jfm.2025.10690
[research_ruban_fot_1991]: https://doi.org/10.1007/bf00978798
[research_rubio_ballard_1967]: https://doi.org/10.21236/ad0660321
[research_ruffin_barato_2018]: https://doi.org/10.2514/6.2018-4664
[research_ruffin_paccagnella_2019]: https://doi.org/10.2514/6.2019-4266
[research_ruffin_paccagnella_2022]: https://doi.org/10.2514/1.b38504
[research_ruflin_grantham_1984]: https://ntrs.nasa.gov/citations/19840059585
[research_rumsey_lee_1961]: https://ntrs.nasa.gov/citations/20040047150
[research_runyan_forsberg_1970]: https://ntrs.nasa.gov/citations/19700027279
[research_rupp_mcmurtrey_2020]: https://doi.org/10.1115/pvp2020-21587
[research_rupp_mcmurtrey_2021]: https://doi.org/10.1115/1.0000147v
[research_rurenchow_1963]: https://doi.org/10.21236/ad0412486
[research_rushby_1993]: https://doi.org/10.1007/978-1-4615-3220-0_5
[research_russell_1996]: https://doi.org/10.1016/b978-034063170-6/50008-6
[research_russell_1996_b]: https://doi.org/10.1016/b978-034063170-6/50013-x
[research_ruth_ahn_1990]: https://doi.org/10.2514/6.1990-2299
[research_rutkowski_1979]: https://doi.org/10.2514/3.58539
[research_ryan_1966]: https://doi.org/10.2514/6.1966-1520
[research_ryazantsev_lomakin_2026]: https://doi.org/10.36652/1813-1336-2026-22-4-147-150
[research_s_babup_2024]: https://doi.org/10.4271/2024-26-0453
[research_saavedra_lavagnoli_2015]: https://doi.org/10.2514/6.2015-0258
[research_sabin_1957]: https://doi.org/10.21236/ad0156637
[research_sacchi_sneddon_2026]: https://doi.org/10.2514/6.2026-1445
[research_sachan_r_2025]: https://doi.org/10.1109/space65882.2025.11170809
[research_sachs_1977]: https://doi.org/10.2514/3.44623
[research_sachs_2007_b]: https://doi.org/10.2514/6.2007-6311
[research_sadeck_lee_2009]: https://doi.org/10.2514/1.37444
[research_sadiqalimir_suhanaarsh_2025]: https://doi.org/10.61359/11.2106-2537
[research_sadraey_2022]: https://doi.org/10.1007/978-3-031-18765-0_4
[research_sadraey_2022_b]: https://doi.org/10.1007/978-3-031-18765-0_6
[research_safronov_semon_2023]: https://doi.org/10.32347/2410-2547.2023.110.81-96
[research_saha_ranjan_2019]: https://doi.org/10.1007/978-3-030-20776-2_5
[research_sahoo_peetala_2010]: https://doi.org/10.1115/1.4001128
[research_sahu_1986]: https://doi.org/10.21236/ada171462
[research_sahu_2007]: https://doi.org/10.21236/ada471736
[research_sahu_2011]: https://doi.org/10.2514/6.2011-3026
[research_saida_1986]: https://doi.org/10.1007/978-3-642-82770-9_20
[research_saito_hayashi_2006]: https://doi.org/10.4028/0-87849-409-x.309
[research_sakaki_funahashi_2018]: https://doi.org/10.1016/j.combustflame.2018.04.017
[research_sakaki_kakudo_2015]: https://doi.org/10.2514/6.2015-3845
[research_sakaki_kakudo_2016]: https://doi.org/10.2514/6.2016-5080
[research_sakata_2002]: https://doi.org/10.2514/6.2002-527
[research_sakata_davis_1975]: https://ntrs.nasa.gov/citations/19750055457
[research_sakata_davis_1977]: https://ntrs.nasa.gov/citations/19770018637
[research_sakaue_asai_2000]: https://doi.org/10.1007/978-3-662-03997-7_73
[research_salay_elliott_1996]: https://doi.org/10.2514/3.46903
[research_salley_kovacevich_1964]: https://doi.org/10.21236/ad0607274
[research_saltzman_1961]: https://ntrs.nasa.gov/citations/19980227195
[research_sambamurthi_warmbrod_1989]: https://doi.org/10.2514/6.1989-1732
[research_samimy_arnette_1994]: https://doi.org/10.1063/1.868279
[research_samputh_moey_2024]: https://doi.org/10.3846/aviation.2024.21495
[research_sanchez_cajas_2024]: https://doi.org/10.3846/aviation.2024.22577
[research_sanderson_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50017-8
[research_sanghi_cesnik_2024]: https://doi.org/10.2514/1.c037470
[research_sanghi_riso_2020]: https://doi.org/10.2514/6.2020-2645
[research_sano_1981]: https://doi.org/10.1115/1.3244484
[research_sant_allen_2011]: https://doi.org/10.2514/6.2011-2621
[research_santiago_1996]: https://doi.org/10.2514/6.1996-3013
[research_santos_beck_2008]: https://doi.org/10.2514/6.2008-4134
[research_santos_pegado_2019]: https://doi.org/10.26678/abcm.cobem2019.cob2019-0370
[research_sanz_1986]: https://doi.org/10.2514/3.9447
[research_saravanan_tennyson_2021]: https://doi.org/10.18520/cs/v120/i1/105-109
[research_sargolzaie_fazeli_2022]: https://doi.org/10.30699/jsst.2022.1299
[research_saric_2010]: https://doi.org/10.21236/ada564004
[research_sarigulklijn_sarigulklijn_2006]: https://doi.org/10.2514/1.18559
[research_sarigulklijn_sarigulklijn_2012]: https://doi.org/10.2514/6.2012-5156
[research_sarma_varadan_1988]: https://doi.org/10.2514/3.9935
[research_sarotte]: https://doi.org/10.70675/7e4e5805z21f6z4e0bz8874z44abf9aa6d38
[research_sasoh_fujiwara_1990]: https://doi.org/10.2514/6.1990-2113
[research_sathaye_yuan_2004]: https://doi.org/10.2514/6.2004-4970
[research_sato_2022]: https://doi.org/10.1016/j.ifacol.2022.11.293
[research_sato_sawada_2001]: https://doi.org/10.1016/s0921-5093(01)01083-8
[research_saunders_1963]: https://doi.org/10.2514/3.1491
[research_savkovic_2008]: https://doi.org/10.5937/vojtehg0802147s
[research_savoldi_cammi_2025]: https://doi.org/10.1615/thmt-25.1130
[research_sawada_nishiwaki_1991]: https://doi.org/10.1016/0020-7403(91)90017-w
[research_sawaragi_1995]: https://doi.org/10.1080/09507119509548844
[research_sawyer_1977]: https://ntrs.nasa.gov/citations/19840002436
[research_sayyed_konar_2025]: https://doi.org/10.1109/icc69100.2025.11372428
[research_sbli_experiments_2022]: https://ntrs.nasa.gov/citations/20220017569
[research_sboevd_2024]: https://doi.org/10.53954/9785605099659_25
[research_scala_1961]: https://ntrs.nasa.gov/citations/19620000948
[research_scala_1962]: https://ntrs.nasa.gov/citations/19620001431
[research_schade_hassell_1953]: https://ntrs.nasa.gov/citations/19930092179
[research_schaefer_hanson_2011]: https://ntrs.nasa.gov/citations/20110015953
[research_schafer_1962]: https://doi.org/10.21236/ad0296912
[research_schairer_1941]: https://doi.org/10.2514/8.10709
[research_schallhorn_majumdar_1998]: https://doi.org/10.2514/6.1998-3684
[research_scherberg_ferguson_1952]: https://doi.org/10.21236/ad0005010
[research_scherrer_gowen_1949]: https://ntrs.nasa.gov/citations/19930085534
[research_schewe_mai_2018]: https://doi.org/10.1016/j.jfluidstructs.2018.04.021
[research_schlimm_2015]: https://doi.org/10.2514/6.2015-2900
[research_schmalhoferjr_white_1966]: https://doi.org/10.2514/6.1966-1514
[research_schmidt_1988]: https://doi.org/10.21236/ada196136
[research_schmidt_1991]: https://doi.org/10.2514/6.1991-3316
[research_schmidt_1992]: https://doi.org/10.1520/stp15039s
[research_schmidt_wright_1991]: https://doi.org/10.2514/6.1991-2885
[research_schmitt_1970]: https://doi.org/10.1520/stp26877s
[research_schmitt_destarac_1983]: https://doi.org/10.2514/6.1983-1804
[research_schneck_1978]: https://doi.org/10.21236/ada059023
[research_schnell_2023]: https://doi.org/10.2514/6.2023-3726
[research_schnell_keller_2006]: https://doi.org/10.1109/dasc.2006.313709
[research_schnoebelen_yechout_2003]: https://doi.org/10.2514/6.2003-204
[research_schoeler_1987]: https://doi.org/10.21236/ada195832
[research_schoenenberger_2013]: https://doi.org/10.2514/6.2013-356
[research_schoenman_1984]: https://ntrs.nasa.gov/citations/19840052370
[research_schoneman_2019]: https://doi.org/10.2514/6.2019-1119
[research_schreyer_gaisbauer_2009]: https://doi.org/10.1007/978-90-481-3723-7_102
[research_schroeder_2012]: https://doi.org/10.2514/6.2012-4567
[research_schroeder_2016]: https://doi.org/10.2514/6.2016-1429
[research_schubert_1979]: https://doi.org/10.1016/0017-9310(79)90014-0
[research_schuelein_2008]: https://doi.org/10.2514/6.2008-4208
[research_schueler_1963]: https://doi.org/10.21236/ad0299290
[research_schuet_lombaerts_2017]: https://doi.org/10.2514/1.g001729
[research_schuman_2018]: https://doi.org/10.2514/6.2018-3875
[research_schwanz_1972]: https://doi.org/10.21236/ada006391
[research_scott_1963]: https://doi.org/10.21236/ad0410255
[research_scott_weisshaar_1991]: https://doi.org/10.2514/6.1991-1067
[research_scott_weisshaar_1994]: https://doi.org/10.2514/3.46476
[research_seacord_teitelbaum_1947]: https://ntrs.nasa.gov/citations/20010062501
[research_sears_1947]: https://doi.org/10.1090/qam/20394
[research_seaver_bennett_2023]: https://doi.org/10.2514/6.2023-3293
[research_sebastian_1967]: https://doi.org/10.2514/3.43837
[research_seckel_1964]: https://doi.org/10.1016/b978-0-12-634450-9.50019-1
[research_seckel_1964_b]: https://doi.org/10.1016/b978-0-12-634450-9.50020-8
[research_seckel_1964_c]: https://doi.org/10.1016/b978-0-12-634450-9.50021-x
[research_seckel_1964_d]: https://doi.org/10.1016/b978-0-12-634450-9.50028-2
[research_sedney_1956]: https://doi.org/10.21236/ad0120099
[research_seeney_bull_1968]: https://doi.org/10.21236/ad0856902
[research_seidman_1978]: https://doi.org/10.2514/6.1978-163
[research_seiner_librescu_1983]: https://doi.org/10.2514/3.60137
[research_semionov_kosinov_2000]: https://doi.org/10.1007/978-3-662-03997-7_68
[research_semionov_kosinov_2006]: https://doi.org/10.1007/1-4020-4159-4_50
[research_semionov_kosinov_2007]: https://doi.org/10.1134/s0869864307030031
[research_semionov_kosinov_2009]: https://doi.org/10.1007/978-90-481-3723-7_61
[research_semionov_kosinov_2024]: https://doi.org/10.53954/9785604990131_146
[research_senchev_zubrilin_2022]: https://doi.org/10.34759/tpt-2022-14-1-42-48
[research_seo_cho_2018]: https://doi.org/10.6108/kspe.2018.22.4.108
[research_sergienko_sergienko_1997]: https://doi.org/10.2514/6.1997-3231
[research_serpieri_kotsonis_2015]: https://doi.org/10.2514/6.2015-2576
[research_seshime_haga_2026]: https://doi.org/10.1121/10.0045842
[research_sessions_mcmahon_1977]: https://doi.org/10.1016/0025-5416(77)90189-6
[research_setoguchi_kanazaki_2020]: https://doi.org/10.2514/6.2020-0534
[research_settles_1986]: https://doi.org/10.2514/6.1986-1099
[research_settles_bogdonoff_1973]: https://doi.org/10.2514/6.1973-666
[research_settles_bogdonoff_1975]: https://doi.org/10.2514/6.1975-7
[research_sewell_chew_1994]: https://ntrs.nasa.gov/citations/19950005296
[research_sexsmith_clay_2025]: https://doi.org/10.2514/6.2025-1921
[research_shadloo_hadjadj_2017]: https://doi.org/10.1080/10407782.2017.1353380
[research_shaffer_brinkley_1974]: https://doi.org/10.21236/ada459005
[research_shah_granda_1998]: https://doi.org/10.2514/6.1998-4448
[research_shahab_lehnasch_2009]: https://doi.org/10.1615/ichmt.2009.turbulheatmasstransf.640
[research_shahinian_achter_1963]: https://doi.org/10.21236/ad0414806
[research_shamikh_2013]: https://doi.org/10.31185/ejuow.vol1.iss2.10
[research_shams]: https://doi.org/10.22215/etd/2023-15773
[research_shams_khouli_2026]: https://doi.org/10.1115/1.4071374
[research_shams_noorian_2025]: https://doi.org/10.2139/ssrn.5280925
[research_shamstaleghani_yektaei_2025]: https://doi.org/10.3390/fluids10110277
[research_shan_tian_2019]: https://doi.org/10.1142/s0219455419501025
[research_shanbhag_bashir_2016]: https://doi.org/10.17654/fm019040879
[research_shankara_nandi_1978]: https://doi.org/10.1063/1.324582
[research_shannon_1948]: https://doi.org/10.1002/j.1538-7305.1948.tb01338.x
[research_shannon_1973]: https://doi.org/10.2514/6.1973-1340
[research_shanthakumar_1977]: https://doi.org/10.1016/0022-460x(77)90474-6
[research_shantz_1953]: https://doi.org/10.21236/ad0037850
[research_sharif_abbas_2022]: https://doi.org/10.47893/gret.2022.1084
[research_sharifzadeh_hendrick_2014]: https://doi.org/10.2514/6.2014-2294
[research_sharma]: https://doi.org/10.70675/e7b4e823z3828z492az952aza4608ac21014
[research_sharma_choi_2007]: https://doi.org/10.4028/www.scientific.net/amr.26-28.233
[research_sharma_shadloo_2018]: https://doi.org/10.1080/10407782.2018.1464785
[research_sharma_shadloo_2019]: https://doi.org/10.1016/j.ijheatfluidflow.2019.108430
[research_sharpe_1975]: https://doi.org/10.1007/bf02318364
[research_sharpe_jr_1984]: https://doi.org/10.21236/ada142675
[research_sharpe_oh_2003]: https://doi.org/10.1299/jsmeatem.2003.2._os06w0394
[research_shearwood_nabawy_2021]: https://doi.org/10.2514/6.2021-1826
[research_sheldon_1967]: https://doi.org/10.21236/ad0856658
[research_shelley_leclaire_2001]: https://doi.org/10.21236/ada410056
[research_shen_huang_2019]: https://doi.org/10.1016/j.cja.2019.04.007
[research_shen_zhang_2019]: https://doi.org/10.1088/2053-1591/ab2a66
[research_sher_maqsood_2022]: https://doi.org/10.2514/6.2022-0433
[research_sherby_frenkel_1953]: https://doi.org/10.21236/ad0005979
[research_sherby_lytton_1956]: https://doi.org/10.21236/ad0091682
[research_shevchuk_kravchuk_2017]: https://doi.org/10.18372/1990-5548.54.12308
[research_shevelev_syzranova_2009]: https://doi.org/10.1615/ichmt.2009.conv.350
[research_shi_chen_2024]: https://doi.org/10.1016/j.tws.2024.111614
[research_shi_guan_2025]: https://doi.org/10.1016/j.matlet.2025.138660
[research_shi_zi_2023]: https://doi.org/10.1109/isssr58837.2023.00033
[research_shields_mohseni_2012]: https://doi.org/10.2514/1.j051151
[research_shields_mohseni_2012_b]: https://doi.org/10.2514/6.2012-3117
[research_shields_mohseni_2013]: https://doi.org/10.2514/6.2013-3192
[research_shifler_2013]: https://doi.org/10.21236/ada572675
[research_shih_1976]: https://doi.org/10.2514/6.1976-319
[research_shimizu_mizobuchi_2008]: https://doi.org/10.2514/6.2008-4548
[research_shimura_kamijo_1985]: https://doi.org/10.2514/3.25731
[research_shinde_mcnamara_2018]: https://doi.org/10.2514/6.2018-3548
[research_shinde_mcnamara_2019]: https://doi.org/10.2514/6.2019-3716
[research_shingledecker_glanton_2007]: https://doi.org/10.2172/901496
[research_shirokov_strelets_2024]: https://doi.org/10.3103/s1068799824010082
[research_shiryaev_maysak_2023]: https://doi.org/10.1051/e3sconf/202338305009
[research_shiryaev_serebryansky_2022]: https://doi.org/10.1109/mlsd55143.2022.9934688
[research_shishaeva_vedeneev_2013]: https://doi.org/10.1615/vismechproc.2014011122
[research_shivaji_basavaraju_2025]: https://doi.org/10.1063/5.0265477
[research_shock_wave_boundary]: https://doi.org/10.1007/0-387-26305-5_10
[research_shoyama_wada_2024]: https://doi.org/10.1016/j.actaastro.2024.08.005
[research_shrivastava_stengel_1989]: https://doi.org/10.2514/3.20369
[research_shu_baik_2023]: https://doi.org/10.2139/ssrn.4327697
[research_shuttle_eleven_1978]: https://doi.org/10.2514/5.9781600865336.0027.0048
[research_shweyk_hyde_2012]: https://doi.org/10.2514/6.2012-4579
[research_shyprykevich_sawyer_1973]: https://doi.org/10.2514/6.1973-192
[research_siag_kumar_2026]: https://doi.org/10.2514/6.2026-1323
[research_sibanda_2023]: https://doi.org/10.32920/23581587
[research_sibulkin_1954]: https://ntrs.nasa.gov/citations/19630042866
[research_sibulkin_1956]: https://doi.org/10.2514/8.3524
[research_sibulkin_1958]: https://doi.org/10.2514/8.7381
[research_siclari_1990]: https://doi.org/10.2514/6.1990-595
[research_siclari_1992]: https://doi.org/10.2514/3.10891
[research_sidhu_2023]: https://doi.org/10.64336/001c.70226
[research_siebenhaar_campbell_1987]: https://doi.org/10.2514/6.1987-2116
[research_siegel_ofarrell_2024]: https://doi.org/10.2514/6.2024-4222
[research_sigal_1987]: https://doi.org/10.2514/6.1987-2429
[research_silton_2003]: https://doi.org/10.2514/6.2003-3936
[research_silton_youn_2017]: https://doi.org/10.12783/ballistics2017/16805
[research_silva]: https://doi.org/10.11606/003273318
[research_silva_b]: https://doi.org/10.14393/ufu.te.2022.345
[research_silvafreire_1988]: https://doi.org/10.1016/0017-9310(88)90172-x
[research_silvestre_paglione_2008]: https://doi.org/10.2514/6.2008-208
[research_sim_curry_1985]: https://ntrs.nasa.gov/citations/19870009137
[research_simmers_coney_1979]: https://doi.org/10.1016/0017-9310(79)90116-9
[research_simmons_cross_1954]: https://doi.org/10.1520/stp160-eb
[research_simonson_1975]: https://doi.org/10.1007/978-1-349-15605-4_7
[research_simonson_1988]: https://doi.org/10.1007/978-1-349-19351-6_7
[research_sims_1963]: https://doi.org/10.21236/ad0334868
[research_simsek_kuran_2016]: https://doi.org/10.2514/6.2016-4428
[research_sinay_reiss_1981]: https://doi.org/10.2514/3.7876
[research_singer_1964]: https://doi.org/10.21236/ad0444808
[research_singh_chowdhury_2021]: https://doi.org/10.47531/mantech/ecc.2021.42
[research_singh_jategaonkar_1996]: https://doi.org/10.2514/3.46993
[research_singh_molki_2024]: https://doi.org/10.1615/tfec2024.ada.049215
[research_sinha_ananthkrishnan_2002]: https://doi.org/10.2514/2.3014
[research_sinha_ananthkrishnan_2017]: https://doi.org/10.1201/9781315151977-6
[research_sircar_ribaudo_1988]: https://doi.org/10.1117/12.947700
[research_sirignano_popov_2013]: https://doi.org/10.2514/1.j052512
[research_sivan_1971]: https://doi.org/10.2514/6.1971-792
[research_sivasegaram_whitelaw_1971]: https://doi.org/10.1017/s0001925900005825
[research_sivykh_zaulichny_1978]: https://doi.org/10.1615/ihtc6.1000
[research_skin_temp_freeflight_1961]: https://ntrs.nasa.gov/citations/20040047118
[research_skolnik_putnam_2022]: https://doi.org/10.2139/ssrn.4147322
[research_sleeman_1957]: https://ntrs.nasa.gov/citations/20050019253
[research_sleight_paddock_2008]: https://ntrs.nasa.gov/citations/20080013397
[research_smaili_breeman_2017]: https://doi.org/10.2514/1.g001756
[research_smart_kalkhoran_1994]: https://doi.org/10.2514/6.1994-2576
[research_smith_1953]: https://doi.org/10.21236/ad0007625
[research_smith_1961]: https://doi.org/10.1017/s0001925900002067
[research_smith_1964]: https://doi.org/10.1017/s0368393100080871
[research_smith_1967]: https://doi.org/10.21236/ad0655370
[research_smith_1969]: https://doi.org/10.1017/s0001924000086152
[research_smith_1973]: https://doi.org/10.1520/ds50-eb
[research_smith_1975]: https://doi.org/10.1520/ds58-eb
[research_smith_1982]: https://doi.org/10.21236/ada113996
[research_smith_ramachandran_2025]: https://doi.org/10.1093/mnras/staf1179
[research_smith_smits_1988]: https://doi.org/10.2514/6.1988-500
[research_smith_smits_1992]: https://doi.org/10.1007/978-1-4612-2792-2_29
[research_smith_smits_1993]: https://doi.org/10.1007/978-94-011-1689-3_37
[research_smitha_joy_2021]: https://doi.org/10.18520/cs/v120/i1/161-165
[research_smits_1984]: https://doi.org/10.2514/6.1984-169
[research_smits_1985]: https://doi.org/10.2514/6.1985-299
[research_smits_1988]: https://doi.org/10.21236/ada191494
[research_smollett_1955]: https://doi.org/10.21236/ad0077438
[research_snell_1993]: https://doi.org/10.2514/6.1993-3775
[research_snell_garrardjr_1991]: https://doi.org/10.2514/6.1991-2711
[research_snodgrass_1955]: https://doi.org/10.2514/8.6860
[research_snyder_memory_2005]: https://doi.org/10.2514/6.2005-4608
[research_snyder_weisshaar_2013]: https://doi.org/10.2514/1.c031978
[research_so_1994]: https://doi.org/10.1016/0017-9310(94)90159-7
[research_so_2020]: https://doi.org/10.1007/s00231-020-02901-1
[research_solid_rocket_1992]: https://doi.org/10.2514/5.9781600866159.0001.0016
[research_solies_1995]: https://doi.org/10.2514/6.1995-3912
[research_som_2021]: https://doi.org/10.1115/power2021-65820
[research_somanath_unnikrishnannair_2021]: https://doi.org/10.18520/cs/v120/i1/81-88
[research_sommer_short_1955]: https://ntrs.nasa.gov/citations/19930084096
[research_son_koo_2012]: https://doi.org/10.1007/s11630-012-0564-z
[research_song_librescu_1992]: https://doi.org/10.2514/3.11633
[research_song_yang_2014]: https://doi.org/10.1016/j.cja.2014.08.003
[research_sonneveldt_clark_2019]: https://doi.org/10.2514/6.2019-3482
[research_sotomayer_weeks_1978]: https://doi.org/10.2514/3.58378
[research_sotoudeh_2015]: https://doi.org/10.2514/6.2015-1182
[research_soudakov_egorov_2009]: https://doi.org/10.1007/978-90-481-3723-7_62
[research_souverein_maeding_2019]: https://doi.org/10.1051/eucass/201911591
[research_spaceflight_crew_2004]: https://doi.org/10.1108/aeat.2004.12776caf.006
[research_spacht_1980]: https://doi.org/10.2514/6.1980-1885
[research_spaid_1972]: https://doi.org/10.2514/3.50320
[research_spaid_frishett_1972]: https://doi.org/10.2514/3.50245
[research_sparkes_2024]: https://doi.org/10.1016/s0262-4079(24)00111-8
[research_sparks_buffington_1994]: https://doi.org/10.1080/00207179408923110
[research_sparks_moerder_2002]: https://doi.org/10.1109/acc.2002.1024494
[research_spearman_1979]: https://doi.org/10.2514/6.1979-1815
[research_spearman_1980]: https://doi.org/10.2514/6.1980-1623
[research_spearman_robinson_1956]: https://ntrs.nasa.gov/citations/20050028458
[research_special_features_2010]: https://doi.org/10.2514/5.9781600867552.0545.0614
[research_specker_2002]: https://doi.org/10.21236/ada403779
[research_specker_brinkley_1983]: https://doi.org/10.21236/ada360100
[research_speegle_1958]: https://ntrs.nasa.gov/citations/19630002622
[research_speelman_1977]: https://doi.org/10.2514/3.58791
[research_speelmaniii_1975]: https://doi.org/10.2514/6.1975-1384
[research_speziale_sarkar_1991]: https://ntrs.nasa.gov/citations/19910009077
[research_spin_tunnel_1960]: https://ntrs.nasa.gov/citations/19980223580
[research_spinal_injuries_1980]: https://doi.org/10.1016/0022-460x(80)90375-2
[research_spivey_2009]: https://ntrs.nasa.gov/citations/20090009754
[research_spivey_2010]: https://ntrs.nasa.gov/citations/20100039161
[research_spivey_2011]: https://ntrs.nasa.gov/citations/20110023803
[research_spooner_foley]: https://doi.org/10.1520/stp43876s
[research_spring_1972]: https://doi.org/10.21236/ad0753358
[research_sprinks_1963]: https://doi.org/10.2514/3.1586
[research_spyropoulos_blaisdell_1998]: https://doi.org/10.2514/2.325
[research_squires_2004]: https://doi.org/10.21236/ada427305
[research_sreenatha_kulkarni]: https://doi.org/10.1109/sicici.1992.637660
[research_sreenivasulu_2021]: https://doi.org/10.18520/cs/v120/i1/96-104
[research_srivastava_2009]: https://doi.org/10.1007/s00193-009-0198-6
[research_stability_testing_1995]: https://doi.org/10.2514/5.9781600866371.0545.0564
[research_stainless_rapid_heat_1961]: https://ntrs.nasa.gov/citations/20040006332
[research_stalder_rubesin_1950]: https://ntrs.nasa.gov/citations/19930082751
[research_stall_training_2019]: https://ntrs.nasa.gov/citations/20200002681
[research_stallings_hartman_1981]: https://doi.org/10.21236/ada103383
[research_stallingsjr_1982]: https://doi.org/10.2514/6.1982-372
[research_stalnaker_2004]: https://doi.org/10.2514/6.2004-210
[research_stanford_2016]: https://doi.org/10.2514/6.2016-1097
[research_stanford_2022]: https://doi.org/10.2514/6.2022-3786
[research_stanford_2023]: https://doi.org/10.2514/1.j062218
[research_stanford_beran_2011]: https://doi.org/10.2514/1.c031185
[research_stanisic_1962]: https://doi.org/10.1090/qam/142273
[research_static_aeroelasticity_2014]: https://doi.org/10.1002/9781118700440.ch7
[research_static_longitudinal_2003]: https://doi.org/10.2514/5.9781600861840.0223.0233
[research_static_stability]: https://doi.org/10.1007/978-3-540-46573-7_9
[research_stech_1977]: https://doi.org/10.21236/ada036035
[research_steimle_schroder_2008]: https://doi.org/10.2514/6.2008-6908
[research_steinberg_uselton_1972]: https://doi.org/10.2514/6.1972-1012
[research_stenfelt_ringertz_2009]: https://doi.org/10.2514/1.41092
[research_stengel_1969]: https://doi.org/10.2514/6.1969-813
[research_stengel_1970]: https://doi.org/10.2514/3.44200
[research_stengel_1980]: https://doi.org/10.2514/3.55959
[research_stengel_miller_1978]: https://doi.org/10.2514/6.1978-1361
[research_stepanova_prokhorova_2016]: https://doi.org/10.4028/www.scientific.net/msf.870.528
[research_stephens_1991]: https://doi.org/10.1063/1.40029
[research_stephenson_1966]: https://doi.org/10.2172/4521067
[research_steppert_epple_2017]: https://doi.org/10.1115/imece2017-71872
[research_stewart_1946]: https://doi.org/10.1090/qam/17096
[research_stewart_1956]: https://doi.org/10.2514/8.3590
[research_stewart_1958]: https://doi.org/10.1520/stp45044s
[research_stewart_rowe_1962]: https://doi.org/10.2172/4580752
[research_stewartson_1950]: https://doi.org/10.1017/s0305004100025779
[research_stewartson_1950_b]: https://doi.org/10.1093/qjmam/3.2.182
[research_stewartson_1952]: https://doi.org/10.1093/qjmam/5.2.137
[research_stillwell_larson_1960]: https://ntrs.nasa.gov/citations/20040008088
[research_stillwell_larson_1960_b]: https://ntrs.nasa.gov/citations/20040008099
[research_stine_scherrer_1952]: https://ntrs.nasa.gov/citations/19930083361
[research_stock_1975]: https://doi.org/10.1016/0017-9310(75)90165-9
[research_stockbridge_1988]: https://doi.org/10.2514/6.1988-272
[research_stoldt_johansen_2020]: https://doi.org/10.2514/6.2020-2758
[research_stone_1945]: https://doi.org/10.21236/ada801302
[research_stone_1957]: https://ntrs.nasa.gov/citations/19630008164
[research_stoop_shahinian_1966]: https://doi.org/10.21236/ad0647889
[research_stoughiii_whipple_1991]: https://doi.org/10.2514/6.1991-3220
[research_streb_1973]: https://doi.org/10.2514/3.60203
[research_strietzel_shefler_1963]: https://doi.org/10.21236/ad0426766
[research_striz_1991]: https://doi.org/10.21236/ada248487
[research_strome_1969]: https://doi.org/10.21236/ad0865977
[research_strouhal_curry_1966]: https://doi.org/10.2514/6.1966-1718
[research_stubblefield_kunz_2025]: https://doi.org/10.1016/j.jfluidstructs.2025.104278
[research_stuber_prasadh_2012]: https://doi.org/10.2514/6.2012-5155
[research_study_of_thermocouple_2019]: https://doi.org/10.20535/2219-3804202019194307
[research_study_on_2024]: https://doi.org/10.25236/ajets.2024.070505
[research_stulov_shapiro_1969]: https://doi.org/10.1007/bf01014970
[research_sturek_1973]: https://doi.org/10.2514/6.1973-166
[research_sturek_kayser_1983]: https://doi.org/10.21236/ada128036
[research_sturek_kayser_1983_b]: https://doi.org/10.21236/ada134992
[research_sturek_mylin_1981]: https://doi.org/10.2514/6.1981-1900
[research_sturek_schiff_1981]: https://doi.org/10.21236/ada110016
[research_su_eri_2013]: https://doi.org/10.4028/www.scientific.net/amm.0.1234
[research_su_gilbert_1992]: https://ntrs.nasa.gov/citations/19940036325
[research_su_hwu_2021]: https://doi.org/10.1080/01495739.2021.2000344
[research_su_long_2024]: https://doi.org/10.1017/jfm.2024.439
[research_su_wang_2018]: https://doi.org/10.1145/3208833.3208850
[research_suarez_kramer_1992]: https://doi.org/10.2514/6.1992-2716
[research_subscale_upset_2008]: https://ntrs.nasa.gov/citations/20080034480
[research_sucec_2020]: https://doi.org/10.1115/1.4047504
[research_suchov_kazmerchukh_2022]: https://doi.org/10.20535/0203-3771442022284205
[research_sugamata_genei_2006]: https://doi.org/10.4028/www.scientific.net/msf.519-521.1175
[research_sugiura_ushijima_2024]: https://doi.org/10.1299/jsmemp.2024.31.a4-14
[research_suleman_2007]: https://doi.org/10.21236/ada525877
[research_suleman_crawford_2000]: https://doi.org/10.1115/imece2000-1711
[research_suleman_crawford_2002]: https://doi.org/10.1177/104538902761402477
[research_suleman_venkayya_1994]: https://doi.org/10.2514/6.1994-1744
[research_suleman_venkayya_1996]: https://doi.org/10.2514/6.1996-3997
[research_summerfield_1951]: https://doi.org/10.21236/ada952489
[research_summerfield_1960]: https://doi.org/10.1515/9781400879953-005
[research_summers_burkholder_2006]: https://doi.org/10.2514/6.2006-6550
[research_sun_2024]: https://doi.org/10.1088/1742-6596/2882/1/012087
[research_sun_childs_1975]: https://doi.org/10.2514/3.49670
[research_sun_childs_1976]: https://ntrs.nasa.gov/citations/19760012293
[research_sun_hu_2005]: https://doi.org/10.1515/ijnsns.2005.6.1.25
[research_sun_hu_2017]: https://doi.org/10.1063/1.4995293
[research_sun_miao_2023]: https://doi.org/10.1007/s12540-023-01485-9
[research_sun_miao_2025]: https://doi.org/10.1016/j.apsusc.2025.162501
[research_sun_yang_2020]: https://doi.org/10.1080/14685248.2020.1849709
[research_sun_zhou_2024]: https://doi.org/10.3390/aerospace11121045
[research_sunakawa_uemura_1961]: https://doi.org/10.1299/kikai1938.27.1074
[research_sundberg_1975]: https://doi.org/10.2514/6.1975-1380
[research_sunden_fu_2017]: https://doi.org/10.1016/b978-0-12-809760-1.00003-x
[research_supercritical_dynamic_1974]: https://ntrs.nasa.gov/citations/19830002753
[research_supersonic_aircraft_1997]: https://doi.org/10.2514/5.9781600866449.0173.0210
[research_supersonic_flight_2025]: https://doi.org/10.1002/9781394309290.ch5
[research_supersonic_flows_2021]: https://doi.org/10.1017/9781009105842.012
[research_supersonic_flows_2025]: https://doi.org/10.1017/9781009501293.012
[research_supersonic_research_1995]: https://ntrs.nasa.gov/citations/19960016997
[research_supersonic_three_dimensional_1960]: https://doi.org/10.1515/9781400877706-009
[research_supersonic_transport_1992]: https://doi.org/10.2514/6.1992-2372
[research_surianarayanan_iyer_1989]: https://doi.org/10.1080/02619180.1989.11753410
[research_suryanarayana_singh_2022]: https://doi.org/10.1016/j.ast.2022.107567
[research_susanto_bayusetiawan_2021]: https://doi.org/10.1109/icomitee53461.2021.9650314
[research_sutera_williams_1968]: https://doi.org/10.1016/0017-9310(68)90022-7
[research_sutherland_1893]: https://doi.org/10.1080/14786449308620508
[research_sutton_1968]: https://doi.org/10.1007/978-3-642-46109-5_5
[research_sutton_1970]: https://doi.org/10.21236/ad0722473
[research_sutton_chao_1997]: https://doi.org/10.21236/ada340457
[research_sutton_graves_1971]: https://ntrs.nasa.gov/citations/19720003329
[research_sutton_troiler_1995]: https://doi.org/10.2514/6.1995-2014
[research_swaim_1970]: https://doi.org/10.2514/3.44151
[research_swaim_connor_1968]: https://doi.org/10.2514/3.43907
[research_swanson_1958]: https://ntrs.nasa.gov/citations/19630010650
[research_swarnkar_kothari_2016]: https://doi.org/10.1016/j.ifacol.2016.03.117
[research_sweep_tail_height_1958]: https://ntrs.nasa.gov/citations/19980232008
[research_swindeman_1970]: https://doi.org/10.2172/4102369
[research_syed_moshtaghzadeh_2022]: https://doi.org/10.2514/6.2022-2557
[research_szema_shankar_1984]: https://doi.org/10.2514/6.1984-427
[research_sznajder_2025]: https://doi.org/10.2478/tar-2025-0021
[research_tadi_2002]: https://doi.org/10.1016/s0045-7949(02)00039-1
[research_tadios_1991]: https://doi.org/10.2514/6.1991-883
[research_taguchi_mori_2021]: https://doi.org/10.2514/6.2021-0612
[research_taguchi_semba_2015]: https://doi.org/10.2514/6.2015-2133
[research_taira_1964]: https://doi.org/10.1016/b978-0-08-010580-2.50010-4
[research_taira_ohnami_1962]: https://doi.org/10.1299/jsme1958.5.10
[research_takabayashi_fukumoto_2019]: https://doi.org/10.1007/978-3-319-91017-8_129
[research_takabayashi_kitamura_2019]: https://doi.org/10.2322/astj.jsass-d-18-00016
[research_takada_kikuchi_2009]: https://doi.org/10.2322/tstj.7.pa_65
[research_takahashi_2026_airdata]: https://doi.org/10.2514/1.j065479
[research_takahashi_griffin_2023]: https://doi.org/10.2514/6.2023-3231
[research_takahashi_griffin_2024]: https://doi.org/10.3390/aerospace12010012
[research_takahashi_munakata_2018]: https://doi.org/10.3390/aerospace5010019
[research_takahashi_yamada_2013]: https://doi.org/10.2514/6.2013-1303
[research_takahashi_yamada_2015]: https://doi.org/10.2514/1.a33170
[research_takeda_1970]: https://doi.org/10.5100/jje.6.137
[research_takegawa_furuichi_2022]: https://doi.org/10.1299/jsmemecj.2022.s053-05
[research_takovitskii_2023]: https://doi.org/10.61653/joast.v61i1.2009.632
[research_tallman_1965]: https://doi.org/10.2172/4600512
[research_tamayo]: https://doi.org/10.22215/etd/2023-15474
[research_tamura_yumitori_2024]: https://doi.org/10.2514/6.2024-2446
[research_tan_wang_2024]: https://doi.org/10.1007/978-981-97-3998-1_17
[research_tanaka_1994]: https://doi.org/10.1007/bf00356809
[research_tang_2019]: https://doi.org/10.2514/6.2019-3274
[research_tang_qian_2016]: https://doi.org/10.1080/13873954.2016.1149492
[research_tang_wang_2021]: https://doi.org/10.1115/fedsm2021-65585
[research_tani_shimiya_2010]: https://doi.org/10.1115/fedsm-icnmm2010-30613
[research_tao_jiping_2006]: https://doi.org/10.2514/6.2006-4883
[research_tashakkor_canabal_2011]: https://ntrs.nasa.gov/citations/20110014627
[research_tatar_masdari_2019]: https://doi.org/10.1016/j.ast.2019.06.046
[research_tauby_1979]: https://doi.org/10.21236/ada081055
[research_taylor_gursul_2004]: https://doi.org/10.2514/6.2004-2618
[research_taylor_guttmann_1987]: https://doi.org/10.1007/978-94-009-1347-9_46
[research_taylor_yoo_2011]: https://doi.org/10.2514/6.2011-6253
[research_technical_applications_1976]: https://doi.org/10.2514/6.1976-892
[research_techniques_for_1992]: https://doi.org/10.2514/5.9781600866128.0255.0277
[research_temgouadongmo_kwatny]: https://doi.org/10.17918/etd-3252
[research_tenney_1974]: https://ntrs.nasa.gov/citations/19750006817
[research_teper_stapleford_1965]: https://doi.org/10.2514/6.1965-1237
[research_teper_stapleford_1966]: https://doi.org/10.2514/3.43725
[research_terai_1968]: https://doi.org/10.4262/denkiseiko.39.287
[research_teramoto_sanada_2017]: https://doi.org/10.2514/1.j055368
[research_tharion_yang_2025]: https://doi.org/10.2139/ssrn.5282533
[research_the_advanced_1974]: https://doi.org/10.1108/eb035129
[research_the_analysis_of_2018]: https://doi.org/10.20535/2219-3804192018162296
[research_the_bell_1990]: https://doi.org/10.2514/6.1990-3207
[research_the_challenges_2020]: https://doi.org/10.1002/9781119667063.ch2
[research_the_design_1966]: https://doi.org/10.1016/0043-1648(66)90182-7
[research_the_stability_1968]: https://doi.org/10.1108/eb034386
[research_the_transformation_2007]: https://doi.org/10.1016/b978-075066927-6/50026-x
[research_theodorsen_1935]: https://ntrs.nasa.gov/citations/19800006788
[research_thermal_performance_1972]: https://doi.org/10.2514/6.1972-388
[research_thermal_protection_2013]: https://doi.org/10.2514/5.9781624101717.0001.0030
[research_thermal_stress_correlation_1979]: https://ntrs.nasa.gov/citations/19790012818
[research_thermal_structures_1992]: https://doi.org/10.2514/4.866128
[research_thermostructural_hypersonic_1980]: https://ntrs.nasa.gov/citations/19800039780
[research_thibert_arnal_2000]: https://doi.org/10.1016/s0376-0421(00)00010-5
[research_thomas_1942]: https://doi.org/10.21236/ad0494220
[research_thomas_bajpai_2005]: https://doi.org/10.2514/6.2005-6428
[research_thomas_fan_1971]: https://doi.org/10.1016/0017-9310(71)90232-8
[research_thomas_miller_1979]: https://doi.org/10.2514/6.1979-404
[research_thompson_klyde_2004]: https://doi.org/10.2514/6.2004-5064
[research_thomson_1946]: https://doi.org/10.2514/8.11345
[research_thornton_dechaumphai_1987]: https://doi.org/10.2514/6.1987-1610
[research_thornton_dechaumphai_1987_b]: https://doi.org/10.2514/6.1987-700
[research_thornton_dechaumphai_1988]: https://doi.org/10.2514/3.45702
[research_three_dimensional_boundary_layer_1994]: https://doi.org/10.2514/6.1994-2375
[research_throttleable_engine_2005]: https://ntrs.nasa.gov/citations/20060009006
[research_throttling_history_2010]: https://ntrs.nasa.gov/citations/20100033271
[research_throttling_review_2009]: https://ntrs.nasa.gov/citations/20090037061
[research_thrust_vectoring_strakes_1998]: https://ntrs.nasa.gov/citations/19980232887
[research_tian_chen_2012]: https://doi.org/10.4028/www.scientific.net/amm.229-231.1811
[research_tian_pan_2026]: https://doi.org/10.1088/1742-6596/3226/1/012009
[research_tian_yang_2016]: https://doi.org/10.1061/(asce)as.1943-5525.0000652
[research_tian_zhang_2023]: https://doi.org/10.3390/coatings13081427
[research_tibbits_ivanov_2015]: https://doi.org/10.2514/6.2015-2152
[research_tile_gap_flow_1983]: https://doi.org/10.2514/5.9781600865626.0271.0299
[research_tilmann_1998]: https://doi.org/10.21236/ada359861
[research_ting_lebofsky_2014]: https://doi.org/10.2514/6.2014-0838
[research_ting_nguyen_2014]: https://doi.org/10.2514/6.2014-0837
[research_ting_wiersema_2025]: https://doi.org/10.2514/6.2025-2361
[research_tinger_1987]: https://doi.org/10.2514/6.1987-2561
[research_tirpak_1985]: https://doi.org/10.21236/ada163487
[research_titov_leontiev_2010]: https://doi.org/10.1115/ihtc14-22585
[research_tizzi_1994]: https://doi.org/10.1016/0045-7949(94)90001-9
[research_tobak_schiff_1974]: https://doi.org/10.2514/6.1974-85
[research_tobak_schiff_1975]: https://doi.org/10.2514/3.49698
[research_tobak_schiff_1975_b]: https://doi.org/10.2514/3.49699
[research_tobey_bastress_1966]: https://doi.org/10.21236/ad0655792
[research_token_1974]: https://doi.org/10.21236/ada002685
[research_tokuda_yang_1966]: https://ntrs.nasa.gov/citations/19670037101
[research_tokuda_yang_2019]: https://doi.org/10.1615/ihtc3.1840
[research_tokugawa_ishida_2026]: https://doi.org/10.1007/978-981-96-9829-5_36
[research_tokugawa_yoshida_2006]: https://doi.org/10.2514/6.2006-3165
[research_tomczyk_2001]: https://doi.org/10.2514/6.2001-4264
[research_tong_1965]: https://doi.org/10.2514/3.2979
[research_tong_giedt_1963]: https://doi.org/10.21236/ad0403711
[research_tong_ji_2024]: https://doi.org/10.1016/j.compfluid.2024.106444
[research_tong_zhou_2023]: https://doi.org/10.3390/aerospace10100886
[research_toni_1968]: https://doi.org/10.2514/6.1968-925
[research_toong_1978]: https://doi.org/10.21236/ada061976
[research_torreszanardi_bacchi_2019]: https://doi.org/10.2514/6.2019-4431
[research_torrigiani_berci_2021]: https://doi.org/10.2514/6.2021-1911
[research_totemeier_2007]: https://doi.org/10.1115/creep2007-26372
[research_tourbier_fasel_1994]: https://doi.org/10.2514/6.1994-2286
[research_tournes_landrum]: https://doi.org/10.1109/ssst.2001.918558
[research_traci_wilcox_1974]: https://doi.org/10.2514/6.1974-515
[research_traci_wilcox_1975]: https://doi.org/10.2514/3.60465
[research_transient_surface_temp_2000]: https://ntrs.nasa.gov/citations/20010002830
[research_transition_flight_1958]: https://ntrs.nasa.gov/citations/19630008170
[research_transonic_summary_1959]: https://ntrs.nasa.gov/citations/19980228028
[research_triplett_1980]: https://doi.org/10.2514/6.1980-794
[research_trussell_thomson_1960]: https://ntrs.nasa.gov/citations/19980227990
[research_tsuji_tanabe_1994]: https://doi.org/10.1016/0022-3115(94)90202-x
[research_tsushima_yokozeki_2019]: https://doi.org/10.1016/j.ast.2019.03.025
[research_tu_yan_2024]: https://doi.org/10.1007/s42405-024-00735-3
[research_tucker_dehoff_1993]: https://doi.org/10.2514/6.1993-1861
[research_tucker_maslen_1951]: https://ntrs.nasa.gov/citations/19930082955
[research_tuling_dala_2013]: https://doi.org/10.2514/6.2013-2823
[research_turbopump_ignition_1986]: https://ntrs.nasa.gov/citations/19890006633
[research_turbulent_external_2023]: https://doi.org/10.1002/9781119766797.ch10
[research_turbulent_spot_in_2024]: https://doi.org/10.15372/pmtf202415496
[research_tushavina_2022]: https://doi.org/10.34759/tpt-2022-14-12-531-538
[research_twardy_1975]: https://doi.org/10.1016/0094-5765(75)90006-5
[research_tyurenkova_smirnova_2024]: https://doi.org/10.1016/j.actaastro.2024.09.035
[research_u_s_supersonic_1997]: https://doi.org/10.17226/5848
[research_udrescu_1998]: https://doi.org/10.2514/6.1998-1843
[research_uemura_kamata_2020]: https://doi.org/10.1515/htmp-2020-0039
[research_ueno_matsuno_1998]: https://doi.org/10.2514/6.1998-2520
[research_uludag_turan_2015]: https://doi.org/10.7763/ijmmm.2015.v3.176
[research_umeoka_mishina_2021]: https://doi.org/10.1016/j.actaastro.2020.08.024
[research_urbano_selle_2016]: https://doi.org/10.1016/j.combustflame.2016.03.020
[research_urbin_knight_1999]: https://doi.org/10.2514/6.1999-427
[research_uribequintero_takahashi_2024]: https://doi.org/10.2514/6.2024-4048
[research_urnes_nielsen_2010]: https://doi.org/10.2514/6.2010-3470
[research_urnes_smith_2011]: https://doi.org/10.2514/6.2011-1567
[research_urnes_stewart_1990]: https://ntrs.nasa.gov/citations/19910003389
[research_uselton_freemanjr_1975]: https://doi.org/10.2514/6.1975-1026
[research_ustinov_2013]: https://doi.org/10.1615/tsagiscij.2013007932
[research_vadera_2019]: https://doi.org/10.2514/6.2019-3860
[research_valentine_meyer_2004]: https://ntrs.nasa.gov/citations/20040086536
[research_vancrayenest_tran_2005]: https://ntrs.nasa.gov/citations/20070014636
[research_vandam_1986]: https://doi.org/10.2514/6.1986-1824
[research_vandam_los_1995]: https://ntrs.nasa.gov/citations/19960016119
[research_vandriest_blumer_1961]: https://doi.org/10.21236/ad0265237
[research_vandromme_zeman_1992]: https://ntrs.nasa.gov/citations/19940010286
[research_vanecho_1964]: https://doi.org/10.21236/ad0609343
[research_vanfossen_simoneau_1994]: https://ntrs.nasa.gov/citations/19940020008
[research_vanfossen_simoneau_1994_b]: https://ntrs.nasa.gov/citations/19950022298
[research_vanhooser_bailey_1999]: https://doi.org/10.2514/6.1999-2189
[research_vanoudheusden_2004]: https://doi.org/10.1115/1.1637626
[research_vanthullenar_1957]: https://doi.org/10.1080/00431672.1957.9924976
[research_varello_lamberti_2013]: https://doi.org/10.5139/ijass.2013.14.4.310
[research_varlese_tului_2013]: https://doi.org/10.1016/j.intermet.2013.02.001
[research_varvanifarahani_2004]: https://doi.org/10.1016/s0924-0136(04)00424-8
[research_vasantha_nath_1986]: https://doi.org/10.1016/0017-9310(86)90019-0
[research_vasilevsky_2022]: https://doi.org/10.31772/2712-8970-2022-23-4-671-687
[research_vasudev_thakur_2019]: https://doi.org/10.1016/j.surfcoat.2019.02.012
[research_vasudevan_leonard_2002]: https://doi.org/10.21236/ada403745
[research_vaughnjr_1982]: https://doi.org/10.2514/6.1982-414
[research_vector_quality_2017]: https://doi.org/10.4018/978-1-5225-2509-7.ch009
[research_vedeneev_2012]: https://doi.org/10.1016/j.jfluidstructs.2011.12.011
[research_vedeneev_2013]: https://doi.org/10.1017/jfm.2013.522
[research_velden_1997]: https://doi.org/10.1007/978-3-7091-2658-5_16
[research_veley_khot_2008]: https://doi.org/10.21236/ada478915
[research_velger_shinar_1983]: https://doi.org/10.2514/3.44823
[research_venema_vonterzi_2011]: https://doi.org/10.1115/gt2011-45312
[research_venkateswaran_grenda_1991]: https://doi.org/10.2514/6.1991-1609
[research_ventrice_fang_1979]: https://doi.org/10.2514/3.61316
[research_ventrice_fang_1979_b]: https://doi.org/10.2514/6.1979-156
[research_vepa_2023]: https://doi.org/10.1201/9781003266310-6
[research_veresnikov_goncharenko_2025]: https://doi.org/10.1007/s42401-025-00371-z
[research_verma_hadjadj_2015]: https://doi.org/10.1007/s00193-015-0587-y
[research_vernacchia_2022]: https://doi.org/10.2514/1.b38104
[research_vescovini_dozio_2018]: https://doi.org/10.3390/jcs2040058
[research_vigdorovich_2015]: https://doi.org/10.1615/ichmt.2015.thmt-15.190
[research_vigdorovich_2017]: https://doi.org/10.1134/s0015462817050052
[research_vigdorovich_2023]: https://doi.org/10.1063/5.0166028
[research_vigdorovich_2023_b]: https://doi.org/10.1063/5.0174389
[research_vigdorovich_2024]: https://doi.org/10.1063/5.0219655
[research_vigdorovich_2025]: https://doi.org/10.1017/jfm.2025.10634
[research_vijgen_hardin_1992]: https://ntrs.nasa.gov/citations/19930018259
[research_vincent_botez_2015]: https://doi.org/10.2514/6.2015-0904
[research_vindigni_2023]: https://doi.org/10.21741/9781644902677-31
[research_vindigni_2024]: https://doi.org/10.21741/9781644903193-27
[research_vindigni_mantegna_2024]: https://doi.org/10.1016/j.jsv.2023.118151
[research_vinokur_1970]: https://doi.org/10.1017/s0022112070002239
[research_visbal_2012]: https://doi.org/10.2514/6.2012-3279
[research_visbal_2017]: https://doi.org/10.1103/physrevfluids.2.024703
[research_visbal_garmann_2012]: https://doi.org/10.1115/fedsm2012-72405
[research_vishwanathan]: https://doi.org/10.33915/etd.1816
[research_visuttipitukul_chansaksoong_2009]: https://doi.org/10.1515/htmp.2009.28.6.401
[research_viviani_aprovitola_2021]: https://doi.org/10.1016/j.actaastro.2020.09.006
[research_vlahopoulos_he_2009]: https://doi.org/10.4271/2009-01-0564
[research_voisinet_lee_1972]: https://doi.org/10.21236/ad0757330
[research_vomaske_sadoff_1961]: https://ntrs.nasa.gov/citations/19980227082
[research_vonterzi_mayer_2009]: https://doi.org/10.1007/978-90-481-3723-7_67
[research_vonwillingh_knutsen_2022]: https://doi.org/10.1080/09603409.2022.2058227
[research_voronkin_1971]: https://doi.org/10.1007/bf01015073
[research_voss_tang_2026]: https://doi.org/10.2514/6.2026-1156
[research_vranas_1976]: https://ntrs.nasa.gov/citations/19760017435
[research_vtail_interference_1956]: https://ntrs.nasa.gov/citations/19660010448
[research_wadley_hopper_2005]: https://doi.org/10.2514/6.2005-5934
[research_waesche_summerfield_1965]: https://doi.org/10.21236/ad0634278
[research_wagdi_1979]: https://doi.org/10.2514/6.1979-260
[research_wagner]: https://doi.org/10.1109/iciasf.1993.687662
[research_waindim_gaitonde_2014]: https://doi.org/10.2514/6.2014-0940
[research_wainwright_1962]: https://doi.org/10.21236/ad0297175
[research_walker]: https://ntrs.nasa.gov/citations/20210013929
[research_walker_1973]: https://doi.org/10.2514/6.1973-1306
[research_wallace_1952]: https://doi.org/10.21236/ad0043099
[research_walsh_jacoby_1972]: https://doi.org/10.2514/6.1972-1183
[research_walter_redman_1954]: https://doi.org/10.21236/ad0037422
[research_waltrup_schetz_1972]: https://doi.org/10.2514/6.1972-311
[research_waltrup_schetz_1973]: https://doi.org/10.2514/3.50435
[research_wan_zhang_2011]: https://doi.org/10.1007/s11431-011-4446-5
[research_wang_1993]: https://ntrs.nasa.gov/citations/19930005569
[research_wang_1999]: https://doi.org/10.2514/6.1999-1722
[research_wang_2011]: https://doi.org/10.1017/s0001924000005868
[research_wang_2019]: https://doi.org/10.1063/1.5087963
[research_wang_2019_b]: https://doi.org/10.3901/jme.2019.07.119
[research_wang_2024]: https://doi.org/10.2316/j.2024.201-0461
[research_wang_bidek_1994]: https://ntrs.nasa.gov/citations/19940020637
[research_wang_han_2014]: https://doi.org/10.4028/www.scientific.net/amm.551.530
[research_wang_han_2018]: https://doi.org/10.1016/j.matchar.2018.02.031
[research_wang_hawkins_2018]: https://doi.org/10.2172/1476397
[research_wang_herbert_1994]: https://doi.org/10.2514/6.1994-2374
[research_wang_hingst_1991]: https://ntrs.nasa.gov/citations/19910011772
[research_wang_ji_2020]: https://doi.org/10.1016/j.corsci.2020.108894
[research_wang_kim_2025]: https://doi.org/10.6108/kspe.2025.29.3.009
[research_wang_leary_2025]: https://ntrs.nasa.gov/citations/20250009358
[research_wang_li_2013]: https://doi.org/10.1016/j.ijheatmasstransfer.2013.03.021
[research_wang_li_2022]: https://doi.org/10.1007/s42405-022-00442-x
[research_wang_li_2022_b]: https://doi.org/10.1109/ahpcai57455.2022.10087863
[research_wang_li_2022_c]: https://doi.org/10.1109/icid57362.2022.9969694
[research_wang_li_2026]: https://doi.org/10.2139/ssrn.6025078
[research_wang_liu_2016]: https://doi.org/10.2514/6.2016-3528
[research_wang_liu_2020]: https://doi.org/10.1016/j.surfcoat.2020.126473
[research_wang_lou_1992]: https://doi.org/10.1016/b978-0-444-88970-6.50017-8
[research_wang_ma_2024]: https://doi.org/10.3390/aerospace11080677
[research_wang_mykhaylonka_2010]: https://doi.org/10.1016/j.corsci.2010.07.031
[research_wang_su_2018]: https://doi.org/10.1088/1757-899x/452/4/042048
[research_wang_tang_2021]: https://doi.org/10.1115/1.0001612v
[research_wang_tang_2021_b]: https://doi.org/10.1115/fedsm2021-65583
[research_wang_tian_2014]: https://doi.org/10.1016/j.surfcoat.2014.04.057
[research_wang_tu_2025]: https://doi.org/10.2139/ssrn.5292423
[research_wang_vojtek_2016]: https://doi.org/10.2514/6.2016-5521
[research_wang_wang_2016]: https://doi.org/10.1063/1.4944536
[research_wang_wang_2016_b]: https://doi.org/10.1063/1.4963382
[research_wang_wu_2018]: https://doi.org/10.1051/matecconf/201817902001
[research_wang_wu_2021]: https://doi.org/10.1016/j.jfluidstructs.2021.103286
[research_wang_xie_2020]: https://doi.org/10.1016/j.jallcom.2020.154271
[research_wang_yang_2017]: https://doi.org/10.1016/j.jsv.2017.07.033
[research_wang_zhao_2022]: https://doi.org/10.3390/aerospace9080433
[research_wang_zhao_creep_2024]: https://doi.org/10.20517/jmi.2024.33
[research_wang_zhou_2000]: https://doi.org/10.2514/6.2000-3299
[research_wang_zhou_2021]: https://doi.org/10.1016/j.jfluidstructs.2021.103296
[research_wang_zong_2025]: https://doi.org/10.3390/ma18071588
[research_wansaseub_sleesongsom_2020]: https://doi.org/10.1007/s42405-019-00246-6
[research_ward_blackburn_1976]: https://doi.org/10.1115/1.3443370
[research_ward_blackburn_1976_b]: https://doi.org/10.2172/7328665
[research_ward_myers_1967]: https://doi.org/10.21236/ad0815090
[research_ware_spencerjr_1988]: https://doi.org/10.2514/6.1988-2136
[research_warren_hassan_1997]: https://doi.org/10.2514/6.1997-2245
[research_washington_humphrey_1969]: https://doi.org/10.21236/ad0699359
[research_waskiewicz_dejongh_1981]: https://doi.org/10.2514/6.1981-1653
[research_wasserman_1952]: https://doi.org/10.21236/ad0015929
[research_watkins_1986]: https://doi.org/10.2514/6.1986-2448
[research_watmuff_smits_1987]: https://doi.org/10.21236/ada186366
[research_watson_1975]: https://doi.org/10.2514/6.1975-1367
[research_watts_1976]: https://doi.org/10.21236/ada030344
[research_watts_mendelson_1947]: https://doi.org/10.1126/science.105.2735.583
[research_weatherill_zartarian_1958]: https://doi.org/10.21236/ad0142154
[research_webb_1971]: https://doi.org/10.1007/bf01002474
[research_webber_houghton_1963]: https://doi.org/10.1108/eb033812
[research_wegener_1977]: https://doi.org/10.21236/ada038280
[research_wei_xin_2024]: https://doi.org/10.20944/preprints202409.0084.v1
[research_wei_zhang_2024]: https://doi.org/10.1016/j.jallcom.2024.175737
[research_weinacht_1998]: https://doi.org/10.2514/6.1998-395
[research_weinacht_2014]: https://doi.org/10.21236/ada607593
[research_weingarten_chalk_1982]: https://doi.org/10.2514/6.1982-1296
[research_weiss_staudacher_2022]: https://doi.org/10.3390/machines10100846
[research_weisshaar_1977]: https://doi.org/10.2514/3.44579
[research_weisshaar_1978]: https://doi.org/10.21236/adb032318
[research_weisshaar_1979]: https://doi.org/10.21236/adb042815
[research_weisshaar_1980]: https://doi.org/10.2514/6.1980-795
[research_weisshaar_1981]: https://doi.org/10.2514/3.57542
[research_weisshaar_1985]: https://doi.org/10.2514/3.48607
[research_weisshaar_1990]: https://doi.org/10.2514/6.1990-1078
[research_weisshaar_ryan_1986]: https://doi.org/10.2514/3.45282
[research_weissman_1972]: https://doi.org/10.2514/6.1972-984
[research_weissman_1973]: https://doi.org/10.2514/3.60216
[research_weissman_1975]: https://doi.org/10.2514/3.59904
[research_welded_18_1958]: https://doi.org/10.1520/stp47092s
[research_welded_inconel_1958]: https://doi.org/10.1520/stp47109s
[research_welge_radkey_1976]: https://doi.org/10.2514/6.1976-757
[research_wells_1989]: https://ntrs.nasa.gov/citations/19890060258
[research_wells_mcbride_1967]: https://doi.org/10.1179/000844367795164268
[research_wells_urnes_1994]: https://ntrs.nasa.gov/citations/19940022929
[research_welsh_winchenbach_1970]: https://doi.org/10.2514/3.5659
[research_wen_deng_2013]: https://doi.org/10.1016/j.proeng.2013.12.032
[research_wen_wu_2014]: https://doi.org/10.1109/chicc.2014.6895555
[research_wendt_1948]: https://doi.org/10.4271/480181
[research_wentzjr_nyenhuis_1984]: https://doi.org/10.2514/6.1984-2189
[research_wernet_locke_2009]: https://doi.org/10.2514/6.2009-70
[research_west_brandis_2018]: https://doi.org/10.2514/6.2018-3767
[research_west_ummel_1980]: https://doi.org/10.21236/ada096597
[research_westin_defreitaspinto_2008]: https://doi.org/10.4271/2008-36-0247
[research_westphal_bleazard_2006]: https://doi.org/10.2514/6.2006-3828
[research_whitcomb_1952]: https://ntrs.nasa.gov/citations/19930092271
[research_white_1974]: https://doi.org/10.2514/6.1974-267
[research_whiteheadjr_1991]: https://doi.org/10.2514/6.1991-3100
[research_whitmore_merkley_2015]: https://doi.org/10.2514/6.2015-3940
[research_whitnah_1967]: https://ntrs.nasa.gov/citations/19670050718
[research_whitten_moffat_1970]: https://doi.org/10.1615/ihtc4.2540
[research_wiedemann_clark_1986]: https://ntrs.nasa.gov/citations/19860016940
[research_wilborn_foster_2004]: https://doi.org/10.2514/6.2004-4811
[research_wilcoxjr_1991]: https://doi.org/10.2514/6.1991-198
[research_wilhelm_schafranek_1986]: https://doi.org/10.2514/3.45377
[research_wilks_2006]: https://doi.org/10.21236/ada447214
[research_willems_1987]: https://doi.org/10.1007/978-1-4613-1893-4_164
[research_williams_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50012-9
[research_williams_1991]: https://ntrs.nasa.gov/citations/19910010759
[research_williams_2004]: https://doi.org/10.21236/ada420091
[research_williams_2004_b]: https://doi.org/10.21236/ada425218
[research_williams_drake_1948]: https://ntrs.nasa.gov/citations/19650070849
[research_williams_hunt_1980]: https://doi.org/10.2514/6.1980-1809
[research_williams_niestroy_2025]: https://doi.org/10.2514/6.2025-1451
[research_wilson_1950]: https://doi.org/10.2514/8.1727
[research_wilson_1971]: https://ntrs.nasa.gov/citations/19710049984
[research_wilson_1973]: https://doi.org/10.2514/3.6929
[research_wilson_1978]: https://doi.org/10.1016/0017-9310(78)90115-1
[research_wilson_cazier_1973]: https://ntrs.nasa.gov/citations/19730021212
[research_wilson_egger_1975]: https://ntrs.nasa.gov/citations/19750000069
[research_wilson_maurer_1971]: https://doi.org/10.2514/3.6148
[research_wimpress_1966]: https://doi.org/10.1108/eb034156
[research_wimpress_swihart_1964]: https://doi.org/10.2514/3.43561
[research_wing_rock_delta_1993]: https://ntrs.nasa.gov/citations/19930017961
[research_wing_theory_1969]: https://doi.org/10.1016/c2013-0-02078-6
[research_wing_tunnel_1998]: https://doi.org/10.1108/aeat.1998.12770ead.003
[research_winkler_1954]: https://doi.org/10.21236/ad0058826
[research_winograd_miles_1956]: https://doi.org/10.1017/s0001925900010167
[research_winovich_1968]: https://doi.org/10.2514/6.1968-405
[research_wiswell_olekszyk_1961]: https://ntrs.nasa.gov/citations/19710070148
[research_wnuk_wnuk_1990]: https://ntrs.nasa.gov/citations/19900004444
[research_wolf_1999]: https://doi.org/10.2514/6.1999-1702
[research_wolf_2002]: https://doi.org/10.1007/bf02719190
[research_wolf_2019]: https://doi.org/10.31399/asm.fach.aero.c9001605
[research_wolf_bossert_2001]: https://doi.org/10.2514/6.2001-4313
[research_wolf_fallon_2011]: https://doi.org/10.2514/6.2011-2555
[research_wolf_ivanov_2008]: https://doi.org/10.2514/6.2008-6942
[research_wolfe_1964]: https://doi.org/10.1016/b978-0-08-010580-2.50018-9
[research_wolkovitch_1984]: https://doi.org/10.2514/6.1984-2471
[research_wong_mastroianni_1999]: https://doi.org/10.21236/ada362873
[research_woo_1992]: https://doi.org/10.2514/6.1992-4765
[research_wood_bauer_1988]: https://doi.org/10.2514/6.1988-481
[research_wood_covell_1987]: https://doi.org/10.2514/6.1987-2477
[research_wood_miller_1984]: https://doi.org/10.2514/6.1984-2208
[research_woodiga_liu_2015]: https://doi.org/10.1177/0954410015594823
[research_woods_gilbert_1989]: https://doi.org/10.2514/6.1989-1385
[research_woods_gilbert_1990]: https://doi.org/10.2514/3.25336
[research_woodward_1956]: https://doi.org/10.1108/eb032671
[research_woodward_1968]: https://doi.org/10.2514/6.1968-55
[research_woodworth_salazar_2023]: https://doi.org/10.1016/j.ijheatmasstransfer.2023.123960
[research_wooldridge_1960]: https://doi.org/10.1108/eb033272
[research_woronowicz_baganoff_1991]: https://doi.org/10.2514/6.1991-1314
[research_wortman_1970]: https://doi.org/10.2514/6.1970-809
[research_wortman_1971]: https://doi.org/10.2514/3.6306
[research_wright_1936]: https://doi.org/10.2514/8.155
[research_wright_1988]: https://doi.org/10.21236/ada204103
[research_wright_zoby_1971]: https://ntrs.nasa.gov/citations/19770076296
[research_wright_zoby_1977]: https://doi.org/10.2514/6.1977-719
[research_wu_li_2020]: https://doi.org/10.1088/1757-899x/790/1/012162
[research_wu_liang_2019]: https://doi.org/10.1103/physrevfluids.4.044602
[research_wu_lv_2018]: https://doi.org/10.1016/j.ast.2018.07.037
[research_wu_martin_2007]: https://doi.org/10.2514/1.27021
[research_wu_moin_2010]: https://doi.org/10.1063/1.3475816
[research_wu_radespiel_2017]: https://doi.org/10.1007/s00348-017-2310-5
[research_wu_wu_2013]: https://doi.org/10.4028/www.scientific.net/amm.321-324.618
[research_wu_wu_2014]: https://doi.org/10.1177/0142331214525073
[research_wu_zhao_2021]: https://doi.org/10.1109/iccasit53235.2021.9633501
[research_wunderlich_dahne_2017]: https://doi.org/10.1007/s13272-017-0251-6
[research_wunderlich_dahne_2017_b]: https://doi.org/10.1007/s13272-017-0266-z
[research_wurster_1981]: https://doi.org/10.2514/6.1981-1090
[research_wykes_1957]: https://doi.org/10.4271/570163
[research_wykes_1968]: https://doi.org/10.2514/6.1968-1067
[research_x15_conference_1958]: https://ntrs.nasa.gov/citations/19710070129
[research_x15_escape_1958]: https://ntrs.nasa.gov/citations/19930092389
[research_x15_first_flight_1959]: https://ntrs.nasa.gov/citations/19980236840
[research_x15_first_landing_1959]: https://ntrs.nasa.gov/citations/19980227362
[research_x15_heating_1962]: https://ntrs.nasa.gov/citations/19660020178
[research_x15_lessons_1993]: https://ntrs.nasa.gov/citations/19930039008
[research_x15_skin_temps_1961]: https://ntrs.nasa.gov/citations/19630004036
[research_x1_liftdrag_1953]: https://ntrs.nasa.gov/citations/19930087731
[research_x2_first_landing_1952]: https://ntrs.nasa.gov/citations/19930087318
[research_x2_glide_1953]: https://ntrs.nasa.gov/citations/19930087801
[research_x2_lateral_model_1958]: https://ntrs.nasa.gov/citations/19930089979
[research_x2_mach32_1959]: https://ntrs.nasa.gov/citations/19980227870
[research_x4_stall_1950]: https://ntrs.nasa.gov/citations/19930090543
[research_x5_stability_1953]: https://ntrs.nasa.gov/citations/19930087479
[research_x5_tail_loads_1955]: https://ntrs.nasa.gov/citations/19930088802
[research_xb70_stability_1973]: https://ntrs.nasa.gov/citations/19730023226
[research_xi_liu_2011]: https://doi.org/10.1007/s12034-011-0199-9
[research_xi_wanqing_2020]: https://doi.org/10.1088/1757-899x/799/1/012004
[research_xia_kong_2022]: https://doi.org/10.32604/icces.2022.08765
[research_xiang_rose_2008]: https://doi.org/10.1016/j.scriptamat.2008.02.034
[research_xiang_xie_2020]: https://doi.org/10.1016/j.vacuum.2020.109190
[research_xiao_2016]: https://doi.org/10.11648/j.ijmea.20160402.15
[research_xiao_wu_2025]: https://doi.org/10.2139/ssrn.5760733
[research_xiao_wu_2026]: https://doi.org/10.2139/ssrn.7030618
[research_xiaodong_guiping_2010]: https://doi.org/10.2514/6.2010-8086
[research_xie_cai_2023]: https://doi.org/10.2514/1.c037239
[research_xie_cui_2024]: https://doi.org/10.1088/1361-6501/ad4c8c
[research_xie_leng_2007]: https://doi.org/10.1155/2008/957561
[research_xie_liu_2016]: https://doi.org/10.1155/2016/5090719
[research_xie_qi_2013]: https://doi.org/10.1115/1.4007919
[research_xie_wang_2013]: https://doi.org/10.1016/j.applthermaleng.2013.06.002
[research_xie_zhang_2016]: https://doi.org/10.1115/1.4034914
[research_xin_shi_2016]: https://doi.org/10.1115/1.4034049
[research_xin_xu_2026]: https://doi.org/10.1016/j.applthermaleng.2026.130208
[research_xiong_lele_2003]: https://doi.org/10.2514/6.2003-1259
[research_xiong_lele_2004]: https://doi.org/10.21236/ada422883
[research_xiong_liu_2022]: https://doi.org/10.2514/1.j061255
[research_xiong_liu_2024]: https://doi.org/10.2139/ssrn.4911204
[research_xiong_morgan_2020]: https://doi.org/10.2514/1.j058036
[research_xiong_nguyen_2024]: https://doi.org/10.2514/6.2024-2668
[research_xu_2023]: https://doi.org/10.54254/2753-8818/18/20230256
[research_xu_guo_2003]: https://doi.org/10.5006/1.3277567
[research_xu_he_2019]: https://doi.org/10.1007/978-981-13-3305-7_212
[research_xu_huang_2025]: https://doi.org/10.1016/j.energy.2025.135007
[research_xu_song_2023]: https://doi.org/10.2139/ssrn.4549793
[research_xu_tian_2017]: https://doi.org/10.1016/j.proci.2016.08.071
[research_xu_yang_2011]: https://doi.org/10.4028/www.scientific.net/amr.287-290.2883
[research_xu_yao_2010]: https://doi.org/10.1016/j.cap.2009.09.003
[research_xu_yue_2019]: https://doi.org/10.1007/s11071-019-05159-3
[research_xu_zhang_2020]: https://doi.org/10.1109/access.2020.2981047
[research_xue_khawaja_2014]: https://doi.org/10.1063/1.4904694
[research_xue_luo_2019]: https://doi.org/10.1007/978-3-319-91017-8_114
[research_xue_mei_1990]: https://doi.org/10.2514/6.1990-982
[research_xue_mei_1992]: https://doi.org/10.2514/6.1992-2129
[research_xue_mei_1993]: https://doi.org/10.2514/3.11332
[research_xue_wang_2019]: https://doi.org/10.3850/978-981-11-2730-4_0192-cd
[research_xue_ye_2019]: https://doi.org/10.1080/19942060.2019.1663264
[research_y_n_2011]: https://doi.org/10.21608/asat.2011.27136
[research_yahalom_1971]: https://doi.org/10.21236/ad0728233
[research_yahyaaalsalman_mahmoodahmood_2013]: https://doi.org/10.33899/rjs.2013.78811
[research_yakimov_2018]: https://doi.org/10.1007/978-3-319-78217-1_1
[research_yakimov_2018_b]: https://doi.org/10.1007/978-3-319-78217-1_2
[research_yakimov_2018_c]: https://doi.org/10.1007/978-3-319-78217-1_3
[research_yakovenko_fedosov_2025]: https://doi.org/10.1109/dspa64310.2025.10977930
[research_yamane_ishihara_1997]: https://doi.org/10.1299/jsmeb.40.542
[research_yamazaki_kusunose_2016]: https://doi.org/10.2514/1.c033417
[research_yan_he_2020]: https://doi.org/10.1016/j.ast.2020.105841
[research_yan_munn_1989]: https://doi.org/10.21236/ada207161
[research_yan_tai_2021]: https://doi.org/10.1016/j.corcom.2021.10.002
[research_yang_2004]: https://doi.org/10.21236/ada428947
[research_yang_2021]: https://doi.org/10.3846/aviation.2021.15131
[research_yang_chen_2009]: https://doi.org/10.2514/1.42370
[research_yang_clark_1975]: https://doi.org/10.1016/0094-4548(75)90041-7
[research_yang_li_2019]: https://doi.org/10.1115/1.4042160
[research_yang_li_2023]: https://doi.org/10.20944/preprints202306.1678.v1
[research_yang_li_2023_b]: https://doi.org/10.3390/coatings13081336
[research_yang_liang_2024]: https://doi.org/10.1088/2053-1591/ad1f9a
[research_yang_obayashi_2003]: https://doi.org/10.2514/2.3134
[research_yang_sun_2012]: https://doi.org/10.2514/1.t3759
[research_yang_sun_2023]: https://doi.org/10.1088/1742-6596/2418/1/012059
[research_yang_yang_2012]: https://doi.org/10.1007/s11431-012-4933-3
[research_yang_yu_2018]: https://doi.org/10.1108/ec-06-2016-0195
[research_yang_yu_2020]: https://doi.org/10.1360/sst-2019-0284
[research_yanta_collier_1989]: https://doi.org/10.2514/6.1989-135
[research_yao_he_2014]: https://doi.org/10.1016/j.corsci.2013.08.029
[research_yao_hussain_2019]: https://doi.org/10.1017/jfm.2019.727
[research_yasumura_kitamura_2021]: https://doi.org/10.1299/jsmemecj.2021.s191-01
[research_yates_1963]: https://doi.org/10.2514/6.1963-205
[research_yates_zeydel_1963]: https://doi.org/10.2514/3.1536
[research_yatskikh_kosinov_2018]: https://doi.org/10.1063/1.5065315
[research_ye_gu_2026]: https://doi.org/10.3390/aerospace13090818
[research_ye_ye_2020]: https://doi.org/10.1061/(asce)as.1943-5525.0001173
[research_ye_ye_2021]: https://doi.org/10.1016/j.ast.2020.106428
[research_ye_ye_2021_b]: https://doi.org/10.1016/j.ast.2021.106909
[research_yee_bailey_1961]: https://ntrs.nasa.gov/citations/20040047120
[research_yerkovich_guarnieri_1955]: https://doi.org/10.21236/ad0092492
[research_yf12_strain_gauges_1979]: https://ntrs.nasa.gov/citations/19790042387
[research_yi_jun_2015]: https://doi.org/10.1017/s0001924000004310
[research_yih_cermak_1952]: https://doi.org/10.21236/ad0009799
[research_yildirim_2020]: https://doi.org/10.1080/01495739.2020.1770644
[research_yildiz_akcal_2018]: https://doi.org/10.2514/6.2018-1867
[research_yildiz_akcal_2019]: https://doi.org/10.2514/1.g004180
[research_yilmaz_kayran_2024]: https://doi.org/10.2514/6.2024-4232
[research_yin_jiang_2025]: https://doi.org/10.3390/aerospace12030225
[research_yip_parlett_1980]: https://ntrs.nasa.gov/citations/19810009460
[research_yipton_blachowski_1996]: https://doi.org/10.2514/6.1996-2871
[research_yonezawa_obayashi_2010]: https://doi.org/10.2514/1.46651
[research_yoo_duensing_2019]: https://doi.org/10.2514/6.2019-3698
[research_yoo_shin_2004]: https://doi.org/10.1007/s11661-004-0268-4
[research_yoon_jeon_2012]: https://doi.org/10.6108/kspe.2012.16.5.081
[research_yoon_jeon_2013]: https://doi.org/10.6108/kspe.2013.17.6.105
[research_yoon_moon_2026]: https://doi.org/10.3390/aerospace13090768
[research_yoshida_bragg_2021]: https://doi.org/10.2514/6.2021-2680
[research_you_liu_2020]: https://doi.org/10.2514/1.c035784
[research_young_1965]: https://doi.org/10.21236/ad0621085
[research_young_2016]: https://doi.org/10.1016/b978-0-08-100101-1.00006-6
[research_young_2016_b]: https://doi.org/10.1016/b978-0-08-100101-1.00007-8
[research_yount_smith_1968]: https://doi.org/10.2172/4085556
[research_yu_bernal_2016]: https://doi.org/10.2514/6.2016-1066
[research_yu_dong_2023]: https://doi.org/10.1017/jfm.2023.212
[research_yu_guo_2025]: https://doi.org/10.1016/j.tws.2024.112652
[research_yu_hornung_2026]: https://doi.org/10.2139/ssrn.7180118
[research_yu_lv_2014]: https://doi.org/10.4028/www.scientific.net/amm.633-634.1233
[research_yu_yang_2025]: https://doi.org/10.1063/5.0290649
[research_yuan_song_2015]: https://doi.org/10.2514/1.j053246
[research_yuan_wang_2014]: https://doi.org/10.1080/01495739.2014.937263
[research_yuan_zhou_2000]: https://doi.org/10.1007/978-3-662-03997-7_65
[research_yuceil_dolling_1994]: https://doi.org/10.2514/6.1994-2050
[research_yuhui_zhenguo_2002]: https://doi.org/10.2514/6.2002-3992
[research_yuwei_wu_2024]: https://doi.org/10.52202/078371-0177
[research_zaichik_yashin_2019]: https://doi.org/10.2514/6.2019-0711
[research_zalovcik_1945]: https://ntrs.nasa.gov/citations/19930093001
[research_zaludin_2012]: https://doi.org/10.11113/jt.v36.560
[research_zapatausandivaras]: https://doi.org/10.70675/831550dczec0cz4e1ez92f4z9244ce04acfa
[research_zapatausandivaras_bauerheim_2024]: https://doi.org/10.1016/j.proci.2024.105382
[research_zartarian_1956]: https://doi.org/10.21236/ad0110592
[research_zartarian_hsu_1955]: https://doi.org/10.21236/ad0110591
[research_zeiler_1999]: https://doi.org/10.2514/2.2495
[research_zeng_yuan_2023]: https://doi.org/10.1016/j.cja.2022.09.013
[research_zhai_ma_2021]: https://doi.org/10.1016/j.compstruct.2021.113869
[research_zhang_1995]: https://doi.org/10.2514/6.1995-2162
[research_zhang_2003]: https://doi.org/10.2514/6.2003-2134
[research_zhang_2009]: https://doi.org/10.3901/jme.2009.03.291
[research_zhang_2016]: https://doi.org/10.1007/978-3-662-49254-3_11
[research_zhang_chen_2016]: https://doi.org/10.2514/6.2016-3919
[research_zhang_cheng_2013]: https://doi.org/10.4028/www.scientific.net/amm.390.33
[research_zhang_feng_2024]: https://doi.org/10.32604/icces.2024.012317
[research_zhang_ga_2012]: https://doi.org/10.1007/s11431-012-4743-7
[research_zhang_geng_2013]: https://doi.org/10.4028/www.scientific.net/amr.750-752.715
[research_zhang_guo_2021]: https://doi.org/10.1155/2021/5553304
[research_zhang_li_2017]: https://doi.org/10.2514/6.2017-4669
[research_zhang_li_2023]: https://doi.org/10.1080/09603409.2023.2281111
[research_zhang_li_2024]: https://doi.org/10.1016/j.ceramint.2024.08.353
[research_zhang_li_2025]: https://doi.org/10.2139/ssrn.5759946
[research_zhang_liu_2014]: https://doi.org/10.4028/www.scientific.net/amm.668-669.920
[research_zhang_liu_2019]: https://doi.org/10.1109/ccdc.2019.8832469
[research_zhang_lv_2018]: https://doi.org/10.1007/s11071-017-3956-5
[research_zhang_peng_2011]: https://doi.org/10.1515/htmp.2011.108
[research_zhang_shao_2018]: https://doi.org/10.1142/9789813277984_0014
[research_zhang_taira_2022]: https://doi.org/10.2514/6.2022-0730
[research_zhang_wang_2016]: https://doi.org/10.1515/jaots-2016-0114
[research_zhang_xiao_2022]: https://doi.org/10.2139/ssrn.4130796
[research_zhang_xin_2024]: https://doi.org/10.3390/surfaces7040063
[research_zhang_yang_2016]: https://doi.org/10.2514/6.2016-1783
[research_zhang_yi_2011]: https://doi.org/10.1109/iceice.2011.5777944
[research_zhang_zhang_2020]: https://doi.org/10.1016/j.actaastro.2019.11.012
[research_zhang_zhang_2025]: https://doi.org/10.2139/ssrn.5870469
[research_zhang_zhang_2026]: https://doi.org/10.1117/12.3117368
[research_zhang_zhang_2026_b]: https://doi.org/10.2139/ssrn.6641999
[research_zhang_zhao_2026]: https://doi.org/10.1016/j.actaastro.2026.03.051
[research_zhang_zhou_2018]: https://doi.org/10.2514/1.j056804
[research_zhang_zhou_2018_b]: https://doi.org/10.2514/6.2018-3574
[research_zhang_zhou_2026]: https://doi.org/10.2514/1.j066769
[research_zhangjunhong_hanjinglong_2010]: https://doi.org/10.1109/icacc.2010.5487216
[research_zhao_cai_2022]: https://doi.org/10.1016/j.actaastro.2021.12.024
[research_zhao_cao_2015]: https://doi.org/10.1016/j.ast.2015.09.019
[research_zhao_he_2020]: https://doi.org/10.1016/j.ast.2019.105635
[research_zhao_jimzhu_2017]: https://doi.org/10.2514/1.g001835
[research_zhao_kapania_2017]: https://doi.org/10.2514/6.2017-4320
[research_zhao_li_2019]: https://doi.org/10.1016/j.actaastro.2019.03.027
[research_zhao_li_2024]: https://doi.org/10.1109/jsen.2024.3363510
[research_zhao_liew_2010]: https://doi.org/10.1002/nme.3059
[research_zhao_qiao_2026]: https://doi.org/10.2514/1.c038671
[research_zhao_sheng_2014]: https://doi.org/10.1109/cgncc.2014.7007465
[research_zhao_wan_2025]: https://doi.org/10.1109/transducers61432.2025.11111234
[research_zhao_wei_2016]: https://doi.org/10.1016/j.ijheatmasstransfer.2016.03.091
[research_zhao_wu_2025]: https://doi.org/10.1063/5.0285039
[research_zhao_xie_2016]: https://doi.org/10.1109/ccdc.2016.7531480
[research_zhao_yu_2011]: https://doi.org/10.4028/www.scientific.net/amr.383-390.7729
[research_zhao_zhang_2009]: https://doi.org/10.1016/j.ijthermalsci.2008.11.004
[research_zhao_zhang_2023]: https://doi.org/10.3390/s23208647
[research_zhao_zhang_2025]: https://doi.org/10.3390/s25051633
[research_zhao_zhu_2016]: https://doi.org/10.1109/acc.2016.7525145
[research_zhao_zhu_2016_b]: https://doi.org/10.1109/dasc.2016.7778101
[research_zhao_zhu_2016_c]: https://doi.org/10.1109/icuas.2016.7502671
[research_zheltovodov_knight_2011]: https://doi.org/10.1017/cbo9780511842757.005
[research_zheltovodov_pavlov_1985]: https://doi.org/10.1007/978-3-642-82462-3_61
[research_zhou_1995]: https://doi.org/10.2514/6.1995-1190
[research_zhou_chen_2022]: https://doi.org/10.5293/ijfms.2022.15.3.355
[research_zhou_dong_2026]: https://doi.org/10.1016/j.actaastro.2026.07.044
[research_zhou_nie_2024]: https://doi.org/10.2139/ssrn.4910100
[research_zhou_wang_2022]: https://doi.org/10.21203/rs.3.rs-2052840/v1
[research_zhou_xie_2019]: https://doi.org/10.12783/dtcse/iteee2019/28809
[research_zhou_yang_2013]: https://doi.org/10.4028/www.scientific.net/amm.482.42
[research_zhou_yang_2017]: https://doi.org/10.1109/icca.2017.8003042
[research_zhou_yuan_2024]: https://doi.org/10.1016/j.jmst.2023.08.046
[research_zhu_breuer_2022]: https://doi.org/10.2514/6.2022-2328
[research_zhu_voo_2024]: https://doi.org/10.1007/s11517-024-03220-x
[research_zhu_wang_2025]: https://doi.org/10.1016/j.actaastro.2024.10.013
[research_zhu_wen_2012]: https://doi.org/10.1109/icinfa.2012.6246895
[research_zhu_wu_2025]: https://doi.org/10.2139/ssrn.5257097
[research_zhu_yao_2022]: https://doi.org/10.3390/math10234506
[research_zhu_zhu_2026]: https://doi.org/10.2514/1.c038900
[research_zhuang_nie_1998]: https://doi.org/10.2514/6.1998-3690
[research_zhuang_nie_1999]: https://doi.org/10.2514/6.1999-2779
[research_ziefuss_mehdizadeh_2020]: https://doi.org/10.1016/j.ijheatfluidflow.2019.108527
[research_ziegler_1988]: https://doi.org/10.1016/s0263-2241(88)80002-2
[research_zima_1956]: https://doi.org/10.21236/ad0092520
[research_zimmerman_weissenburger_1964]: https://doi.org/10.2514/3.43581
[research_zinn_1968]: https://doi.org/10.2514/3.4908
[research_zinn_powell_1971]: https://doi.org/10.1016/s0082-0784(71)80051-6
[research_zinn_savell_1969]: https://doi.org/10.1016/s0082-0784(69)80398-x
[research_znamenskaya_latfullin_2008]: https://doi.org/10.1134/s1063785008080130
[research_zohar_erel_1988]: https://doi.org/10.2514/3.45578
[research_zook_2024]: https://doi.org/10.52202/078371-0154
[research_zoppini_ragni_2022]: https://doi.org/10.2139/ssrn.4036119
[research_zu_tan_2022]: https://doi.org/10.1109/wcmeim56910.2022.10021529
[research_zubair_ejaz_2022]: https://doi.org/10.4028/p-g44bm8
[research_zubanov_shabliy_2014]: https://doi.org/10.18287/1998-6629-2014-0-5-1(47)-148-153
[research_zuev_arngold_2020]: https://doi.org/10.34759/vst-2020-3-167-185
