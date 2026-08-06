---
layout: post
mathjax: true
comments: true
title: "X-Planes: Convair X-6"
date: 2025-10-12 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 7
---

<!-- A303 -->
<script>console.log("A303");</script>

The [Convair X-6][ref_convair_x6] was never built. It is the first article in this series about an aircraft that did not exist, and the interesting thing about it is not the absence but the residue, because the programme that would have produced it ran for fifteen years, spent about a billion dollars, and left a technical record larger than that of most aircraft in this series that actually flew. This article is the seventh in the [X-Planes series][related_post_a297_xplanes_framing], following the [X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], the [X-4][related_post_a301_northrop_x4], and the [X-5][related_post_a302_bell_x5]. The National Advisory Committee for Aeronautics, abbreviated NACA throughout and reconstituted in 1958 as the National Aeronautics and Space Administration, abbreviated NASA, contributed cycle analysis. The [Atomic Energy Commission][ref_aec] and the Air Force supplied the money and the reactors.

The keystone question is whether a reactor can be flown. The answer is yes, and one was, and the aircraft that carried it proved that the answer did not matter.

## The Research Question

The keystone is whether the mass of shielding a reactor requires can be carried by an aircraft that still has a reason to fly.

The attraction is easy to state and it is enormous. Fission releases about eighty million times more energy per unit mass than combustion, so an aircraft that heats its air with a reactor rather than by burning fuel is not range-limited in any sense a designer of the 1940s would recognize. Writing the energy released per kilogram of uranium-235 fissioned against the lower heating value of kerosene,

$$E_{\text{fission}} \approx 8.2 \times 10^{13} \ \text{joules per kilogram}, \qquad E_{\text{chem}} \approx 4.3 \times 10^{7} \ \text{joules per kilogram}$$

gives a ratio of

$$\frac{E_{\text{fission}}}{E_{\text{chem}}} = 1.9 \times 10^{6}$$

A strategic bomber of the period consumed fuel by the tens of tonnes. The same energy delivered by fission is measured in grams. The mission this bought was a bomber that could remain airborne for days or weeks, holding a target at risk continuously rather than surging to reach it, and in 1946 that was an argument nobody in the Air Force needed persuading of. The [Army Air Forces began a project on Nuclear Energy for the Propulsion of Aircraft][research_gasser_1947] in May of that year, abbreviated NEPA.

The objection is equally easy to state. A reactor at power is an intense source of gamma rays and neutrons, and the crew must survive the flight. Shielding is dense material, dense material is heavy, and the aircraft must carry all of it all of the time. The keystone is therefore not whether a reactor can produce the thrust, which was never seriously in doubt, but whether what must be wrapped around it leaves an aircraft worth building.

That framing was understood at the outset. The [Lexington Project][research_stever_1948] convened at the Massachusetts Institute of Technology in 1948 to assess feasibility, and its verdict, that the thing was possible but would take fifteen years and a great deal of money, turned out to be very nearly exactly right in duration and wrong only in supposing that the endpoint would be reached. The analysis of the mission case ran alongside, including [studies of nuclear aircraft for antisubmarine warfare][research_aec_1950] where endurance rather than speed is the whole of the requirement, and [the performance parameters that would govern any such aircraft][research_ruffman_1952].

## Programme Origin

The institutional history is a sequence of transfers, and each transfer is a symptom.

Project NEPA began on 28 May 1946 under the Army Air Forces, funded at ten million dollars in 1947, and ran as a study effort until May 1951. It was then replaced by the joint Atomic Energy Commission and Air Force programme called Aircraft Nuclear Propulsion, abbreviated ANP. The [quarterly progress reports][research_cottrell_1951] begin in that period and continue, in an unbroken series, for a decade. The programme pursued two propulsion architectures in parallel, which is the first sign that nobody was confident which would work.

The [direct air cycle][research_shoults_1958] was assigned to General Electric at Evendale, Ohio. It is a turbojet with the combustor replaced by a reactor core. Air leaves the compressor, passes through the core, is heated by fission, and expands through the turbine. It is mechanically simple and thermodynamically direct, and it has the property that the working fluid passes through the reactor and comes out radioactive.

The indirect cycle went to Pratt and Whitney at Middletown, Connecticut. A liquid metal or molten salt loop carries heat from the core to a [heat exchanger][ref_heat_exchanger], and the air is heated there without ever entering the core. It is cleaner and it costs a temperature drop across the exchanger, an entire secondary loop with pumps and radiators, and the mass of all of it. The [circulating fuel reflector-moderator reactor][research_bigelow_1957] was its central concept.

Under project MX-1589 Convair was to modify two B-36 airframes. One would carry a reactor to measure shielding, and one would become the X-6. The [B-36][ref_b36] was chosen for the reason that governs this entire article, which is that it was the largest aircraft available. Follow-on aircraft would have used the swept-wing [YB-60][ref_yb60]. The X-6 itself would have been powered by General Electric X-40 engines, which were [J47][ref_j47] derivatives adapted to nuclear heating, drawing on a P-1 reactor.

The first airframe was built and flown. The second was not.

## Sizing From First Principles

The keystone relationship is the shield mass, and it can be derived from the reactor power and the geometry with nothing more exotic than an exponential.

### How Much Power the Aircraft Needs

Start with the thrust. A B-36 at cruise weighs about 186,000 kilograms and flies at a lift-to-drag ratio near eighteen, so the thrust required is

$$F = \frac{W}{L/D} = \frac{186{,}000 \times 9.80665}{18} = 1.01 \times 10^{5} \ \text{newtons}$$

At a cruise speed of 200 metres per second the propulsive power is

$$P_{\text{prop}} = F V = 1.01 \times 10^{5} \times 200 = 20.3 \ \text{megawatts}$$

and the thermal power the reactor must supply follows from the overall efficiency of the propulsion system,

$$P_{\text{thermal}} = \frac{P_{\text{prop}}}{\eta_{\text{overall}}}, \qquad \eta_{\text{overall}} = \eta_{\text{thermal}} \, \eta_{\text{propulsive}}$$

which for a turbojet of the period is near 0.20, giving

$$P_{\text{thermal}} = \frac{20.3}{0.20} = 101 \ \text{megawatts}$$

**About a hundred megawatts of thermal power, which is a substantial power reactor by any standard and was an enormous one to propose putting in an aeroplane in 1950.** The figure is not sensitive to the assumptions in any way that matters, since an efficiency of 0.25 gives 81 megawatts and 0.30 gives 68.

The fuel consumption that buys is the promise made concrete. At a hundred megawatts for a hundred hours,

$$m_{\text{U-235}} = \frac{P \, t}{E_{\text{fission}}} = \frac{10^{8} \times 3.6 \times 10^{5}}{8.2 \times 10^{13}} = 0.44 \ \text{kilograms}$$

against the 837 tonnes of kerosene that would deliver the same energy. **A nuclear bomber burns less than half a kilogram of fuel on a hundred-hour mission.** Every difficulty in this article is the price of that number.

### What the Reactor Emits

A reactor at power produces prompt fission gammas, fission product decay gammas, and fast neutrons, all in quantities proportional to the fission rate and therefore to the power. The dose rate at distance $r$ from a shielded source is governed by an exponential attenuation with a buildup correction,

$$\dot{D}(r, x) = \frac{k \, P}{4 \pi r^{2}} \, B(\mu x) \, e^{-\mu x}$$

in which $x$ is the shield thickness, $\mu$ the linear attenuation coefficient of the shield material, and $B$ the buildup factor accounting for photons that scatter into the beam rather than being removed from it. The factor $k$ collects the source spectrum and the conversion from fluence to dose.

Two features of that expression govern everything. The distance term is a power law and the shield term is an exponential, and an exponential wins every argument it is in.

Solving for the thickness required to hold the dose at a limit $\dot{D}_0$,

$$x = \frac{1}{\mu} \ln \left( \frac{k \, P \, B}{4 \pi r^{2} \dot{D}_0} \right)$$

For [lead][ref_lead_element] at photon energies around one megaelectronvolt the mass [attenuation coefficient][ref_attenuation] is about 0.070 square centimetres per gram, so with a density of 11.34 grams per cubic centimetre,

$$\mu = 0.070 \times 11.34 = 0.794 \ \text{per centimetre}$$

giving a tenth-value layer of

$$x_{1/10} = \frac{\ln 10}{\mu} = \frac{2.303}{0.794} = 2.90 \ \text{centimetres}$$

so every 2.9 centimetres of lead removes ninety percent of what reaches it. Demanding an attenuation of $10^{7}$ with a buildup factor of ten,

$$x = \frac{\ln \left( 10^{8} \right)}{0.794} = \frac{18.4}{0.794} = 23.2 \ \text{centimetres}$$

**Twenty-three centimetres of lead.** That is the number the programme spent fifteen years trying to reduce.

### The Result That Decides the Programme

Here is the property of the exponential that is easy to miss and that turns out to be the whole argument. Because thickness depends on the logarithm of the power, increasing the reactor power barely thickens the shield,

$$\Delta x = \frac{1}{\mu} \ln \left( \frac{P_2}{P_1} \right)$$

Going from one megawatt to a thousand, a factor of a thousand in power, costs

$$\Delta x = \frac{\ln 1000}{0.794} = 8.7 \ \text{centimetres}$$

of additional lead. **The shield is not a cost proportional to the reactor. It is a large fixed overhead that a bigger reactor barely increases.** That single fact determines which aircraft can be nuclear and which cannot, and it does so in the opposite direction from intuition. A small nuclear aircraft is not easier than a large one. It is impossible, because it must carry nearly the same shield with far less aircraft to carry it.

### The Optimum Separation

Distance is the other lever and it trades against structure. Putting the reactor further from the crew reduces the dose as $r^{-2}$ and therefore permits a thinner shield, but the fuselage that holds them apart has mass of its own.

Take a shadow shield of area $A$ covering the forward face of the reactor, with the crew compartment at distance $r$. Holding the crew dose fixed and solving the attenuation relation for thickness gives

$$x(r) = \frac{1}{\mu} \left[ \ln \left( \frac{k P B}{4 \pi \dot{D}_0} \right) - 2 \ln r \right]$$

so the shield mass falls logarithmically with separation,

$$m_{\text{shield}}(r) = \rho_s A \, x(r) = C - \frac{2 \rho_s A}{\mu} \ln r$$

while the structure needed to span that distance grows linearly at $\lambda$ kilograms per metre,

$$m_{\text{struct}}(r) = \lambda r$$

The total has an interior minimum. Differentiating and setting to zero,

$$\frac{d m_{\text{total}}}{d r} = -\frac{2 \rho_s A}{\mu r} + \lambda = 0 \quad \Longrightarrow \quad r^{*} = \frac{2 \rho_s A}{\mu \lambda}$$

Evaluating with lead at 11,340 kilograms per cubic metre, a forward hemisphere of 1.5 metre radius giving $A = 14.1$ square metres, $\mu = 79.4$ per metre, and a fuselage structural mass of 400 kilograms per metre,

$$r^{*} = \frac{2 \times 11{,}340 \times 14.1}{79.4 \times 400} = 10.1 \ \text{metres}$$

**About ten metres of separation is optimal, and a B-36 fuselage is 49 metres long.** The airframe is large enough to hold the optimum comfortably, which is a further statement of why this aircraft and not a smaller one. The [NB-36H][ref_nb36h] put the reactor in the aft bomb bay and the crew in the nose, which is that geometry.

### The Number That Ends the Argument

With the separation chosen and the thickness computed, the shield mass follows,

$$m_{\text{shield}} = \rho_s A x = 11{,}340 \times 14.1 \times 0.232 = 3.7 \times 10^{4} \ \text{kilograms}$$

or 37 tonnes, which against a gross weight of 186 tonnes is

$$\frac{m_{\text{shield}}}{m_{\text{gross}}} = \frac{37{,}200}{186{,}000} = 0.20$$

**A fifth of the aircraft is shielding.** The comparison that matters is not with the gross weight but with the payload, since a B-36 carried a maximum bomb load of about 39,000 kilograms and the shield estimated here is 37,200.

$$\frac{m_{\text{shield}}}{m_{\text{payload}}} \approx 0.95$$

**The shield weighs approximately what the bomb load weighs.** A nuclear bomber buys unlimited range by giving up the payload that made the range worth having, and that sentence is the programme in one line. The trade is not fatal in principle, since a larger aircraft dilutes a fixed shield mass, and this is exactly why the design kept growing and why the follow-on was to be the larger YB-60. It is fatal in practice because the aircraft that dilutes the shield adequately is one nobody wanted to buy.

The programme knew this. [Shield optimization][research_blizard_1953] was a named research subject with its own literature by 1953, [shield weights][research_woodsum_1957] were tracked as a programme metric, and the effect of the shield on the centre of gravity was itself a design problem serious enough to warrant [its own study][research_phelps_1961]. Shield synthesis was pushed to the point of [formal minimum-weight optimization][research_troubetzkoy_1961], and the computational tools were built in-house, with [shield analysis programs][research_capo_1957] and [their successors][research_edwards_1958] developed specifically for the task.

### Divided Shielding and the Trick That Was Not Enough

The shield mass above assumes shielding the reactor. There is a cheaper arrangement and the programme used it.

A **divided shield** puts part of the material at the reactor and part around the crew. The reactor shield need only cover the solid angle subtended by the crew compartment, and the crew shield handles radiation that reaches the crew by other paths, principally scattering from the air itself. Writing the total as a sum,

$$m_{\text{total}} = \rho_s A_r x_r + \rho_c A_c x_c$$

subject to the constraint that the direct and scattered contributions together meet the dose limit,

$$\dot{D}_{\text{direct}} \left( x_r \right) + \dot{D}_{\text{scatter}} \left( x_r, x_c \right) \le \dot{D}_0$$

the optimum divides the material between the two according to the relative areas, and because the reactor shadow shield can be small in area while the crew compartment shield must wrap a larger volume, the division is not obvious in advance. This is the calculation [Blizard 1953][research_blizard_1953] set out and that the [supercritical water reactor shield design procedure][research_deganahl_1954] and the [AC-series power plant shield calculations][research_mitchell_1954] applied to particular configurations.

The scattered term is the reason the trick has a floor. Radiation that leaves the reactor in any direction can scatter off the surrounding air and arrive at the crew from outside the shadow, an effect that grows with air density and therefore falls with altitude, which is why [the effect of altitude and flight speed on shielding requirements][research_edwards_1954] was a subject in its own right. A shadow shield alone is insufficient in an atmosphere. The aircraft must fly high to make its own shielding lighter, which is a coupling between the flight condition and the structural mass that no conventional aircraft has.

Material choice attacked the same problem from the other end. Gamma attenuation wants high atomic number and density, and neutron attenuation wants hydrogen. [Lithium hydride][ref_lih] supplies hydrogen at low density and captures neutrons in the lithium without producing a penetrating capture gamma, which makes it very nearly the ideal aircraft neutron shield, and [its properties were characterized in detail][research_welch_1961] under the programme. The [investigation of metallic hydrides as moderators, reflectors, and shields][research_gilbertjr_1955] pursued the same family.

## Dependent Systems

### The Direct Cycle and What It Does to the Air

Passing the working fluid through the core is simple and it has a consequence.

The thrust of a turbojet follows from the momentum change,

$$F = \dot{m} \left( V_e - V_0 \right), \qquad V_e = \sqrt{2 c_p T_4 \left[ 1 - \left( \frac{p_0}{p_4} \right)^{\frac{\gamma - 1}{\gamma}} \right]}$$

and the heat the reactor must add to reach turbine inlet temperature $T_4$ from compressor discharge temperature $T_3$ is

$$P_{\text{thermal}} = \dot{m} \, c_p \left( T_4 - T_3 \right)$$

Nothing in either relation cares where the heat came from. The reactor is a heat source with a temperature limit, exactly as a combustor is, and the design problem is to get $T_4$ as high as the turbine will tolerate.

That is where the difficulty lies. A combustor reaches flame temperatures far above what the turbine can take and the design problem is dilution. **A reactor must reach turbine inlet temperature in its own fuel elements, which must therefore run hotter than the air they are heating.** For a 1950s turbine tolerating something like 1150 kelvin at inlet, the fuel element surface must exceed that, and a fuel element at that temperature in a fast air stream is a materials problem of the first order. The programme built an entire literature on it, from [metallic fuel element materials][research_level_1962] through [high-temperature work reported at the ANP materials meetings][research_aec_1959_3].

The air itself becomes radioactive. Natural argon is 0.93 percent of the atmosphere and argon-40 captures a neutron to become [argon-41][ref_argon41], a gamma emitter with a 110 minute half-life. The activity produced scales with the neutron flux, the residence time, and the mass flow,

$$A_{41} = \sigma_c \, \phi \, N_{40} \left( 1 - e^{-\lambda t_{\text{res}}} \right)$$

so a direct-cycle aircraft trails a plume of activated air behind it continuously. The programme studied this and treated it as tolerable in flight, which by the standards of the period it was, and which by any later standard it was not. It also means that a fuel element failure releases fission products directly into the exhaust, which is a different and much less tolerable proposition. The [nuclear aircraft safety analysis programme][research_aec_1957_3] existed to bound exactly these questions.

The [direct cycle nuclear turbojet was tested][research_shoults_1958], which is the fact that matters most in this section. The Heat Transfer Reactor Experiments at the Idaho site ran a reactor coupled to a turbojet on the ground and produced thrust from fission. HTRE-1, HTRE-2, and HTRE-3 form the series, with the [hazards analysis][research_gamertsfelder_1954] preceding them and [the operation manuals][research_woodbridge_1955] describing the assembly. **The programme reached the point of a working nuclear turbojet on a test stand.** [Thornton and Blumberg 1961][research_thornton_1961] report that the HTREs fulfilled their test goals, in a paper published the year the programme was cancelled.

They also had an accident. The [HTRE No. 3 nuclear excursion][research_aec_1959_2] has its own summary report, and its existence is a reminder that this was a reactor programme with reactor risks conducted at aircraft schedules.

### The Indirect Cycle and What It Costs

Keeping the air out of the core costs a temperature drop and a great deal of hardware.

An intermediate loop introduces a heat exchanger between the reactor and the air, and a heat exchanger of effectiveness $\varepsilon$ delivers

$$T_{4} = T_3 + \varepsilon \left( T_{\text{reactor}} - T_3 \right)$$

so the reactor must run hotter than the turbine inlet by the amount the exchanger cannot recover,

$$T_{\text{reactor}} - T_4 = \left( 1 - \varepsilon \right) \left( T_{\text{reactor}} - T_3 \right)$$

An effectiveness of 0.9 with a compressor discharge at 600 kelvin and a required turbine inlet of 1150 kelvin demands a reactor outlet of

$$T_{\text{reactor}} = T_3 + \frac{T_4 - T_3}{\varepsilon} = 600 + \frac{550}{0.9} = 1211 \ \text{kelvin}$$

which is sixty kelvin hotter than the direct cycle needs, and the exchanger mass is added on top. The mass penalty of a heat exchanger scales with the heat transferred and inversely with the temperature difference driving it,

$$m_{\text{HX}} \propto \frac{P_{\text{thermal}}}{U \, \Delta T_{\text{lm}}}$$

so demanding high effectiveness, which means small $\Delta T$, makes the exchanger large exactly when the mass budget is already spent. The [Pratt and Whitney circulating fuel reflector-moderator reactor][research_bigelow_1957] and the [lithium-cooled reactor experiment][research_hedden_1962] represent the state that programme reached, which never approached flight hardware. The engine performance studies are extensive, with [reactor, shield and performance data for a nuclear turbojet][research_larson_1958], [powerplant performance for a supersonic nuclear turbojet][research_larson_1958_2], [advanced characteristics for supersonic aircraft][research_larson_1959], and [nuclear JT-11 turbojet performance][research_larson_1959_2] all by the same author, alongside the [ANP powerplant data compilation][research_meyer_1965] that closes the series.

The NACA contribution sits here. [Humble et al 1950][research_humble_1950] give a preliminary analysis of three cycles for nuclear aircraft propulsion, [Doyle 1951][research_doyle_1951] and [Doyle 1948][research_doyle_1948] work a mercury-vapour intermediate cycle, and [Cavicchi et al 1959][research_cavicchi_1959] design a subsonic nuclear logistic aircraft around a helium-cooled reactor. The state of the art was summarized by [Finger and Rom 1962][research_finger_1962] and in the [proceedings of the nuclear propulsion conference][research_naca_1962] the same year, by which point the subject had already moved to space.

### Decay Heat, and Why the Aircraft Cannot Be Parked

Shutting down a reactor stops the fission but not the heat.

Fission products continue to decay after shutdown, and the thermal power follows an empirical law of the Way-Wigner form,

$$\frac{P_{\text{decay}}(t)}{P_0} \approx 0.066 \, t^{-0.2}$$

with $t$ in seconds after shutdown. Evaluating for a hundred megawatt core,

$$P_{\text{decay}}(1 \ \text{s}) = 6.6 \ \text{MW}, \qquad P_{\text{decay}}(1 \ \text{h}) = 1.28 \ \text{MW}, \qquad P_{\text{decay}}(1 \ \text{day}) = 0.68 \ \text{MW}$$

**An hour after landing the reactor is still producing more than a megawatt.** In a direct-cycle aircraft the cooling medium is the air flowing through the engines, so the airflow must be maintained on the ground, after shutdown, indefinitely, or the core melts. A nuclear aircraft cannot simply be parked. It requires ground equipment to sustain core cooling, and the mass of heat that must go somewhere is comparable to a large industrial furnace running continuously in a hangar.

The time integral makes the point sharper. Total energy released after shutdown up to time $T$ is

$$E_{\text{decay}} = \int_0^{T} 0.066 \, P_0 \, t^{-0.2} \, dt = \frac{0.066 \, P_0}{0.8} T^{0.8}$$

which for a day comes to 73 gigajoules, an average of 850 kilowatts sustained around the clock. That is an operational burden with no analogue in any other aircraft in this series, and it is a burden that exists whether or not the aircraft ever flies again. [Reactor coolant flow optimization for the Aircraft Shield Test Reactor][research_ross_1960] is the programme's version of this problem, and the modern treatments of [decay heat removal][research_bali_2025] and [long-term cooling during transients][research_mochizuki_2026] show it never went away.

### Radiation and the Aircraft Itself

The crew is not the only thing that must survive the reactor.

Dose accumulates in materials as well as people, and the failure modes differ. Organic materials cross-link or embrittle, semiconductors accumulate lattice damage and charge, and lubricants polymerize. The accumulated dose at a component is the integral of the local rate over the mission,

$$D_{\text{component}} = \int_0^{t_{\text{mission}}} \dot{D}(\mathbf{r}, t) \, dt$$

and because the components are distributed through the airframe rather than concentrated in one shielded volume, they cannot all be behind the shadow shield. The programme therefore had to develop [radiation-resistant motors for nuclear aircraft controls][research_fries_1958] and an entire design practice for [electronic systems intended to work in nuclear aircraft][research_levine_1960], restated the following year as [a major influence on such designs][research_levine_1961]. That is [radiation hardening][ref_rad_hardening] as an engineering discipline, and its origins are here.

### The Crew, and the Dose They Were Allowed

The dose limit is the boundary condition on the entire shield calculation, and it is not a physical constant.

Mission dose is the product of rate and duration,

$$D_{\text{mission}} = \dot{D} \, t_{\text{mission}}$$

so an endurance mission is precisely the case where a modest dose rate becomes unacceptable. **The mission that justifies the aircraft is the mission that makes its shielding hardest.** A four-hour sortie at a given dose rate is a quarter of the dose of a sixteen-hour one, and the whole argument for nuclear propulsion was flights measured in days.

Choosing $\dot{D}_0$ therefore chooses the shield mass, through the logarithm,

$$m_{\text{shield}} \propto \ln \left( \frac{1}{\dot{D}_0} \right)$$

and because the dependence is logarithmic, accepting ten times the dose saves only one tenth-value layer of material, which is 2.9 centimetres of lead and about four and a half tonnes on the geometry above. **Relaxing the crew dose limit by a factor of ten buys back about two percent of the aircraft.** That asymmetry is worth stating plainly, because it means the programme could not have been rescued by accepting a more dangerous aircraft. The exponential that makes shielding effective also makes it insensitive to how much risk one is willing to impose on the crew.

## The Flight Test Record

One aircraft flew and it was not the X-6.

The [NB-36H][ref_nb36h], a B-36H-20-CF with serial 51-5712 that had been damaged by a tornado at [Carswell Air Force Base][ref_carswell] on 1 September 1952, was rebuilt as the Nuclear Test Aircraft. It carried the Aircraft Shield Test Reactor, a one megawatt air-cooled reactor of about 16,000 kilograms, hung in a bomb bay on a hook so it could be lowered into a shielded pit between flights. Water served as moderator and coolant and dumped its heat overboard through water-to-air exchangers. **The reactor never powered the aircraft.** Its purpose was to be a source, and the aircraft's purpose was to measure what that source did to a crew compartment and to the equipment around it.

The crew section was rebuilt in lead and rubber at a mass variously reported between eleven and twelve tonnes, with leaded glass in the windows. The aircraft flew 47 times between 17 September 1955 and March 1957, accumulating 215 flight hours of which the reactor was operated during 89.

The measurements are the programme's most valuable output and they are documented. The reactor was [calibrated][research_nance_1957], its [fast neutron spectra measured][research_schaeffer_1958], and it was operated in conjunction with the [Tower Shielding Facility][research_kress_1958] so that airborne results could be compared against a ground installation where the geometry was known exactly. The Tower Shielding Facility itself required [its own critical experiments][research_magnuson_1956] and a [conceptual design study][research_frankfort_1956], and [multilayer shield experiments][research_henry_1958] ran alongside. The comparison of measured against calculated dose is the entire point, since a shield design method that has been validated against flight is worth more than one that has not.

What the flights established is that the shielding worked. The crew was not endangered. What they also established, and what mattered more, is that this was true for a one megawatt source in an aircraft that carried nothing else, and that the shield for a hundred megawatt propulsion reactor would be the mass computed above.

The NB-36H was scrapped, the X-6 was never begun, and the programme was cancelled in March 1961.

## Comparison With Ground Prediction

The X-6 inverts the usual relationship, because there was no flight against which to check the prediction, and the prediction is all there is.

For every other aircraft in this series the interesting question is where the ground facilities were wrong. Here the ground facilities are the entire record. The Aircraft Reactor Experiment, the Heat Transfer Reactor Experiments, the Tower Shielding Facility, and the NB-36H measurements form a body of validated engineering that was never assembled into an aeroplane, and the honest assessment is that the prediction was largely right and the programme was cancelled for reasons the prediction supported rather than contradicted.

The one place where flight added something the ground could not is the air-scattering term. A reactor on a tower over a field is not a reactor at altitude in a moving aircraft, and the scattered dose depends on the density and geometry of the air around the source. That is why the NB-36H flew rather than merely sitting on a stand, and it is why [Edwards 1954][research_edwards_1954] is a document about altitude and flight speed rather than about geometry alone.

The deeper comparison is between what the programme predicted about itself and what happened to it. The Lexington Project in 1948 said fifteen years and a great deal of money. The programme ran fifteen years, spent about a billion dollars, and was cancelled. **The feasibility study was correct about the cost and the schedule and wrong only in assuming that a correct cost and schedule would be paid.**

## What the Data Changed

The aircraft was never built and the programme's output was substantial, which is the case this article exists to make.

The most durable result is a reactor. The Aircraft Reactor Experiment, abbreviated ARE, run at [Oak Ridge][ref_ornl] in 1954, was the world's first [molten salt reactor][ref_msr], using a circulating fluoride salt as both fuel and coolant. It was built because a molten salt core offers high temperature at low pressure, which is exactly what an aircraft wants, and it ran successfully. [Its operation][research_cottrell_1955_2] and [the operating account of Bettis 1957][research_bettis_1957] document the experiment, [the hazards summary][research_cottrell_1952_3] preceded it, [the components of its fused-salt and sodium circuits][research_savage_1958] are described in detail, and it was [disassembled and examined afterward][research_cottrell_1958]. [ORNL's aircraft nuclear power plant designs][research_fraas_1954] give the surrounding context.

**That reactor is the ancestor of a technology now under active commercial development.** The molten salt reactor is a serious contemporary subject, and the modern literature is treated below. An aircraft programme that produced no aircraft produced a reactor concept that outlived it by seventy years and is being commercialized as this is written. That is not a consolation prize. It is a better return than most flown programmes achieve.

The second consequence is a design discipline. Shielding analysis as a computational activity, radiation-hardened components, and the practice of validating shield codes against measurement are all recognizable as ANP outputs. When nuclear propulsion returned as a subject it returned for space rather than for air, and it inherited these tools directly. The [NERVA][ref_nerva] programme and its [nuclear thermal rocket][ref_ntr] successors, the [radiation shielding weight problem in space][research_beever_1965], and the [symposia on protection against radiations in space][research_reetz_1965] are the same discipline redirected. The [Plum Brook hazards work][research_naca_1963] shows the transition in progress at NASA.

The third is a negative result that was correct. Air-breathing nuclear propulsion for crewed aircraft has not been revived by anyone, anywhere, in the sixty-five years since. The Soviet Union flew its own testbed, the [Tu-95LAL][ref_tu95lal], and reached the same conclusion. The [Project Pluto][ref_project_pluto] nuclear ramjet, which dispensed with the crew and therefore with most of the shield, is the exception that proves the rule, since removing the crew removes the constraint this article is about.

## The Contemporary Literature

The subject did not end. It moved, and it split into three descendants that no longer resemble one another.

### Molten Salt Reactors

The Aircraft Reactor Experiment's direct line is now a substantial commercial and academic field. [Holcomb 2025][research_holcomb_2025] treats thermal-spectrum molten salt breeder fuel cycles, [McFarlane 2024][research_mcfarlane_2024] argues that the fuel cycle rather than the reactor is the hard part, and [Creasman et al 2024][research_creasman_2024] compute fuel depletion for a molten salt demonstration reactor. Modelling work includes [Fischer and Bureš 2024][research_fischer_2024], whose subject is the Molten Salt Reactor Experiment itself, the ARE's own successor at Oak Ridge, and [Mochizuki 2024][research_mochizuki_2024] on load following. The chemistry that makes a circulating fuel salt difficult is pursued by [Cheng et al 2025][research_cheng_2025] on noble metal fission product aggregation and [Niu et al 2024][research_niu_2024] on extracting molybdenum-99 from fuel salt, with [Yilmaz et al 2025][research_yilmaz_2025] on thorium fuelling and [Mishra et al 2024][research_mishra_2024] supplying an irradiated fuel salt data library. Accident behaviour is [Dunkle and Bogetic 2026][research_dunkle_2026]. **A 1954 aircraft reactor experiment is the origin of all of it.**

### Shielding

The shield-mass problem this article derives is now solved computationally rather than empirically, but it is the same problem. [Ahmed 2026][research_ahmed_2026] reviews neutron shielding mechanisms and materials, [Liu et al 2026][research_liu_2026] present a dual-stage shielding optimization method, and [Huang et al 2025][research_huang_2025] optimize the shield of a heat pipe cooled reactor, which is a compact mobile reactor and therefore the same class of problem as an aircraft. [Lee and Cho 2025][research_lee_2025] address the question this article calls the boundary condition, namely how to set the radiation target level that the whole design then follows from.

Materials work continues along the lines the programme opened. [Bhardwaj et al 2024][research_bhardwaj_2024] fabricate neutron-absorbing metal hydride ceramic matrix composites, which is the lithium hydride idea in modern form, and [Stone et al 2024][research_stone_2024], [Khan et al 2025][research_khan_2025], and [Sekkat et al 2026][research_sekkat_2026] develop composite and additively manufactured shields. Space reactor shielding specifically is [Han et al 2025][research_han_2025] and [Han et al 2025][research_han_2025_2], with [Oğul et al 2026][research_ogul_2026] treating a small modular reactor. The crewed-vehicle version of the problem, which is the X-6's problem with the source moved outside, appears in [DeWitt and Benton 2024][research_dewitt_2024] on secondary proton buildup, [Matthiä and Berger 2024][research_matthia_2024] on lunar surface exposure, and [Yıldırım and Opçin 2026][research_yildirim_2026] on multilayer composites.

### Nuclear Propulsion Where the Shield Is Affordable

Nuclear propulsion survived in the two places where the constraint this article derives does not bind, which are vehicles with no crew and vehicles where nothing else will do.

Space is the second case. [Alnuaimi and Kim 2026][research_alnuaimi_2026] assess a liquid uranium-manganese nuclear thermal rocket, [Guilbaud et al 2024][research_guilbaud_2024] restudy the KIWI-B-4E core from the Rover programme with modern methods, and [Aueron and Thomas 2024][research_aueron_2024] examine electric-pump-fed nuclear thermal propulsion. Nuclear electric systems appear in [Ma et al 2026][research_ma_2026] and mission studies in [Ancona et al 2025][research_ancona_2025]. **[Duan et al 2026][research_duan_2026] analyse the reactivity safety of an air-cooled nuclear thermal propulsion reactor, which is the direct air cycle returning under a different name for a different vehicle.**

The microreactor is the other descendant, and it inherits the X-6's real problem, which is a reactor that must operate away from the infrastructure a power station enjoys. [Parisi and Arafat 2026][research_parisi_2026] describe the MARVEL microreactor, [Domingos et al 2026][research_domingos_2026] and [Rangel et al 2026][research_rangel_2026] treat fuel choices including designs avoiding enriched uranium, and the economics that decide whether any of it happens are [Abdussami et al 2025][research_abdussami_2025], [Kim and Macfarlane 2026][research_kim_2026], and [Shobeiri et al 2025][research_shobeiri_2025]. Accident source terms and tolerant fuels are [Sun et al 2025][research_sun_2025] and [Elkhawas et al 2025][research_elkhawas_2025], with materials in [Islam and Haque 2025][research_islam_2025] and [Lan et al 2024][research_lan_2024].

### What Took Its Place in Aviation

The question the X-6 was built to answer, which is how to fly without carrying the energy as chemical fuel, is live again and is being answered differently.

Hydrogen is the leading candidate and it has the same structural character as nuclear propulsion, which is that the energy is cheap and the container is expensive. [Li 2024][research_li_2024] reviews hydrogen-powered aircraft, [Jagtap et al 2024][research_jagtap_2024] and [Wahler et al 2025][research_wahler_2025] work the conceptual design and the aerostructural trade, [Sasi et al 2025][research_sasi_2025] treat hydrogen and ammonia turbofans, [Lu et al 2025][research_lu_2025] recover exhaust heat in a cryogenic installation, and [Zhang et al 2026][research_zhang_2026] address crashworthiness, which is the hydrogen version of the question the [nuclear aircraft safety programme][research_aec_1957_3] asked about dispersing a core. Batteries are the other candidate and their specific energy remains the binding constraint, as [Cetegen et al 2025][research_cetegen_2025] and [Peng et al 2024][research_peng_2024] show.

**Every one of these is a fixed-overhead problem of the kind this article derives for the shield.** A cryogenic tank, like a shield, has a mass that does not shrink in proportion to the mission and that must be carried whether or not it is doing anything at that moment. The X-6's arithmetic is a special case of a general pattern in aircraft design, and recognizing it as such is worth more than the aircraft would have been.

## Where the Framing Breaks Down

The keystone framework fits an unbuilt aircraft badly in three ways, and the ways are instructive.

There was no flight, so there was no measurement of the keystone. Everything in the sizing section above is a calculation, and calculations were available in 1948. An instrument model that treats a research aircraft as reducing uncertainty has nothing to work with when the aircraft does not exist, and the honest reading is that the X-6 reduced uncertainty about the programme's cost rather than about its physics.

The programme's most valuable output is unrelated to its keystone. A molten salt reactor is not an answer to the question of whether shielding can be carried. It is a reactor concept that happened to suit an aircraft's requirements for high temperature at low pressure, and it survived because those requirements recur in contexts having nothing to do with aircraft. A framework that scores a programme against its own question will miss this entirely, and it is the most important thing that happened.

The cancellation was not a technical decision and the framework has no place to put that. Intercontinental ballistic missiles made the indefinitely loitering bomber strategically uninteresting, and aerial refuelling made unlimited range achievable by other means. The X-6 was not defeated by its shield. **It was made pointless by two unrelated technologies while it was still arguing with its shield**, which is a much more common way for engineering programmes to end than failure is.

## The Source Base

The source base for this article differs from every other in the series in one structural respect, and it is worth stating explicitly.

**The primary record is not in the NASA archive.** ANP was an Atomic Energy Commission and Air Force programme, so its reports went to the AEC and are held today by the Department of Energy, discoverable through the Office of Scientific and Technical Information rather than through the [NASA Technical Reports Server][ref_ntrs]. The consequence for anyone retracing this work is that the standard search for an X-plane returns almost nothing, and the standard conclusion, that the record is thin, is exactly wrong. The record is enormous and is in a different building.

The programme record proper is the quarterly and semiannual progress report series, running from [Cottrell 1951][research_cottrell_1951] through [1952][research_cottrell_1952], [1952][research_cottrell_1952_2], [Savolainen 1954][research_savolainen_1954], [1957][research_aec_1957], [Jordan 1957][research_jordan_1957], [1957][research_aec_1957_2], [1957][research_na_1957], and [1959][research_aec_1959], with the [administrative account of Dibble 1958][research_dibble_1958] and the [technical briefing of Perry 1958][research_perry_1958] giving the management view. The founding documents are [Gasser 1947][research_gasser_1947] on the NEPA project, the [Lexington Project minutes][research_stever_1948] and [their companion][research_stever_1948_2], and the [NEPA quarterly report of 1950][research_aec_1950_2]. Late-programme summaries are [the General Electric direct-air-cycle programme report][research_comassar_1962], [the reactor and shield physics volume][research_edwards_1962], and [the powerplant data compilation][research_meyer_1965]. [Study of seaplane systems employing nuclear power][research_aec_1959_4] shows how far the application space was searched, and [the engineering proposal for nuclear turbojet development][research_schmickrath_1960] shows what was still being proposed at the end. [Shielding computer program specifications][research_edwards_1957], [the two-component method of shield analysis][research_moteff_1960], [a shield specification][research_johnson_1960], [shield weights for a Boeing mission][research_lee_1958], [the LID tank shield study][research_kam_1961], [the seventh shielding information meeting papers][research_aec_1961], [aircraft reactor control systems][research_gorker_1955], and [HTRE fuel reprocessing studies][research_cannon_1961] fill in the technical detail. [Two-dimensional diffusion theory applied to a fuel-plate-removal experiment][research_gotsky_1959], [tungsten-uranium dioxide fuel retention][research_gedwill_1965], and [ceramic fibre development][research_gates_1961] are NACA and NASA contributions to the surrounding materials problem.

The secondary literature on the aircraft itself is thin, which is the opposite of the primary situation. [Miller 2001][book_miller_2001_x_planes], [Jenkins Landis and Miller 2003][book_jenkins_landis_miller_2003], [Winchester 2005][book_winchester_2005_x_planes], and [Peebles 2014][book_peebles_2014_probing_the_sky] give the roster treatment, and [Hallion 1972][book_hallion_1972_supersonic_flight], [Hallion 1981][book_hallion_1981_on_the_frontier], [Gorn 2001][book_gorn_2001_expanding_envelope], and [Bilstein 1989][book_bilstein_1989_orders] supply institutional context, with [Gunston 1992][book_gunston_1992_faster_than_sound] the wider framing.

The engineering texts behind the relations are [Hill and Peterson 1991][book_hill_peterson_1991] and [Sutton and Biblarz 2016][book_sutton_biblarz_2016] for propulsion, [Incropera and DeWitt][book_incropera_heat_transfer], [Carslaw and Jaeger 1959][book_carslaw_jaeger_1959], and [Boley and Weiner 1960][book_boley_weiner_1960] for heat transfer and thermal stress, [Anderson 2001][book_anderson_2001_fundamentals], [Anderson 2012][book_anderson_2012_aircraft_performance], and [Bertin and Cummings 2013][book_bertin_cummings_2013] for aerodynamics, and [Raymer 2018][book_raymer_2018], [Nicolai and Carichner 2010][book_nicolai_carichner_2010], [Torenbeek 1982][book_torenbeek_1982], and [Roskam 1985][book_roskam_1985] for design method and mass estimation. Structures are [Bruhn 1973][book_bruhn_1973], [Niu 1988][book_niu_1988_airframe], and [Megson 2016][book_megson_2016]. Error analysis is [Taylor 1997][book_taylor_1997_error_analysis] and [Bevington and Robinson 2002][book_bevington_robinson_2002], with design of experiments in [Box Hunter and Hunter 2005][book_box_hunter_hunter_2005] and [Gelman et al 2013][book_gelman_et_al_2013], and information accounting in [Cover and Thomas 2006][book_cover_thomas_2006]. The epistemology is [Vincenti 1990][book_vincenti_1990], [Petroski 1985][book_petroski_1985], and [Ferguson 1992][book_ferguson_1992], and the organizational reading, which this article leans on more than most, is [Perrow 1984][book_perrow_1984], [Vaughan 1996][book_vaughan_1996], [Sagan 1993][book_sagan_1993], and [Reason 1990][book_reason_1990_human_error]. Institutional histories are [Baals and Corliss 1981][book_baals_corliss_1981], [Hansen 1987][book_hansen_1987_engineer_in_charge], and [Chambers and Chambers 2008][book_chambers_2008_radical_wings], with [Heppenheimer 2007][book_heppenheimer_2007_heat_barrier] and [Jenkins 2000][book_jenkins_2000_hypersonics] on the high-speed thread and [Launius and Jenkins 2012][book_launius_jenkins_2012] and [Merlin 2009][book_merlin_2009_blackbird] on the successors.

Foundational primaries bearing on the surrounding arguments include [Williams and Drake][research_williams_drake_1948] on the research airplane rationale, [Buckingham 1914][research_buckingham_1914] on similarity, [Nyquist 1928][research_nyquist_1928] and [Shannon 1948][research_shannon_1948] on sampling and channel capacity, and [Lindley 1956][research_lindley_1956] and [Chaloner and Verdinelli 1995][research_chaloner_verdinelli_1995] on experimental design. Related work on this blog appears in [A96][related_post_a96_history_rocketplanes] on the rocketplane lineage, [A106][related_post_a106_two_stage_delta_wing] on large high-speed configurations, [A217][related_post_a217_rocket_propellant_chemistry] on propellant chemistry, [A237][related_post_a237_aerospace_framing] and [A241][related_post_a241_aerospace_simulation] on the computing and simulation infrastructure, and [A90][related_post_a90_intro_space_studies] on space policy. The [NASA History Office][ref_nasa_x3_factsheet] and the [Armstrong Flight Research Center][ref_nasa_armstrong] hold the aeronautical side of the record, with [Oak Ridge][ref_ornl] and [Idaho][ref_inl] holding the nuclear side.

## Epistemic State

Established historical fact includes the start of Project NEPA on 28 May 1946 under the Army Air Forces, its funding at ten million dollars in 1947, its replacement by the joint AEC and Air Force ANP programme in May 1951, the assignment of the direct air cycle to General Electric and the indirect cycle to Pratt and Whitney, the MX-1589 modification of two B-36 airframes, the tornado damage to 51-5712 at Carswell on 1 September 1952, its rebuilding as the NB-36H, its carriage of the one megawatt Aircraft Shield Test Reactor, its 47 flights and 215 hours between 17 September 1955 and March 1957 with the reactor operated for 89 of those hours, the operation of the Aircraft Reactor Experiment at Oak Ridge in 1954 as the first molten salt reactor, the ground testing of a direct-cycle nuclear turbojet in the HTRE series, and the cancellation of the programme in March 1961 without the X-6 being built.

Established engineering analysis includes every relation in the sizing sections. The exponential attenuation law with buildup, the logarithmic dependence of shield thickness on power and on dose limit, the separation optimum, the Way-Wigner decay heat correlation, the turbojet thrust and heat addition relations, and the heat exchanger effectiveness relation are standard results.

**Derived here and not taken from a source** are the hundred megawatt thermal power estimate for a B-36-class cruise, the 0.44 kilogram uranium consumption over a hundred hours, the 23.2 centimetre lead thickness for a $10^{7}$ attenuation, the 8.7 centimetre thickness increment for a thousandfold power increase, the 10.1 metre separation optimum, the 37 tonne shield mass and its ratios to gross weight and payload, the 1211 kelvin indirect-cycle reactor outlet requirement, and the decay heat figures. These follow by arithmetic from published dimensions and standard physical constants and can be reproduced or refuted by any reader with them.

Inference includes the central claim that the shield mass rather than any other difficulty was the binding constraint, and the subsidiary claim that the logarithmic dependence made the programme insensitive to relaxing the crew dose limit. Both are consistent with the record and with the fact that shield optimization was a named research subject throughout the programme, but neither is a statement the primary reports make in those terms.

Weakly supported are the representative values. The lift-to-drag ratio of eighteen, the overall propulsive efficiency of 0.20, the shadow shield area of 14.1 square metres, the fuselage structural mass of 400 kilograms per metre, the attenuation requirement of $10^{7}$, and the buildup factor of ten are all plausible figures for the class rather than values taken from the design. The shield mass estimate should be read as establishing an order of magnitude and a ratio, not a design number. The ratio is more trustworthy than the absolute value, and the qualitative conclusion that shielding consumes a payload-sized fraction of a B-36 is robust to any reasonable choice of inputs.

Contested or unresolved in the sources consulted is the total programme cost, given as about one billion dollars in one place and seven billion in another, a discrepancy most plausibly explained by inflation adjustment but not stated as such by either source. The crew shield mass is given as eleven tonnes in one account and twelve in another, the window thickness as six inches in one and ten to twelve in another, and the scrapping of the NB-36H is placed at Fort Worth in 1958 in one account and at Carswell in 1957 in another. None of these are load-bearing for the argument, and all are stated here as reported rather than resolved.

A note on temporal position. This article carries an editorial date of 2025-10-12 and is written from current knowledge, including contemporary literature published well after that date.

## Out of Scope

This article does not treat the [X-1][related_post_a298_bell_x1], [X-2][related_post_a299_bell_x2], [X-3][related_post_a300_douglas_x3], [X-4][related_post_a301_northrop_x4], or [X-5][related_post_a302_bell_x5] beyond the comparisons drawn, all of which have their own articles. It does not derive the standard relations reused here, since the [series opener][related_post_a297_xplanes_framing] does that once for all seventy-two articles, including the [flight envelope][ref_flight_envelope], [load factor][ref_load_factor], [wing loading][ref_wing_loading], [lift][ref_lift_coefficient] and [drag][ref_drag_coefficient] coefficients, [lift-to-drag][ref_lift_to_drag], [Reynolds][ref_reynolds_number] and [Prandtl][ref_prandtl_number] numbers, [measurement uncertainty][ref_measurement_uncertainty] and its [propagation][ref_propagation_of_uncertainty], and the [standard atmosphere][ref_isa] in its [tabulated form][ref_us_standard_atmosphere].

It does not attempt a history of the Aircraft Nuclear Propulsion programme, which is a large subject with a literature of its own and is treated here only where it bears on the aircraft. It does not treat [nuclear fission][ref_fission] or the [nuclear reactor][ref_reactor] as subjects, nor [nuclear fuel][ref_nuclear_fuel], [enriched uranium][ref_enriched_uranium], [neutron moderators][ref_moderator], or [beryllium][ref_beryllium] as materials, nor [radiation protection][ref_rad_protection] and [ionizing radiation][ref_ionizing] as disciplines, nor the [sievert][ref_sievert] and [absorbed dose][ref_absorbed_dose] as units, nor [gamma rays][ref_gamma] and [neutron radiation][ref_neutron_rad] as phenomena, nor the [half-value layer][ref_hvl] and [Monte Carlo method][ref_monte_carlo] as techniques, nor [nuclear accidents][ref_nuclear_accidents] as a category. It does not cover the [turbojet][ref_turbojet] as a machine, [transonic][ref_transonic] or [supersonic][ref_supersonic_speed] flow, [swept wings][ref_swept_wing], the [aspect ratio][ref_aspect_ratio], [Mach][ref_mach_number] and [dynamic pressure][ref_dynamic_pressure] as quantities, the [speed of sound][ref_speed_of_sound], [flight dynamics][ref_flight_dynamics], [longitudinal][ref_longitudinal_static_stability] and [directional][ref_directional_stability] stability, [aeroelasticity][ref_aeroelasticity], [buffeting][ref_buffeting], [shock waves][ref_shock_wave] and [oblique shocks][ref_oblique_shock], [wave drag][ref_wave_drag], [boundary layer][ref_boundary_layer] and [separation][ref_flow_separation] behaviour, the [aerodynamic centre][ref_aerodynamic_center], [moments of inertia][ref_moment_of_inertia], the [wing root][ref_wing_root], [wing configuration][ref_wing_configuration] as a taxonomy, [delta wings][ref_delta_wing], [stability augmentation][ref_stability_augmentation], [duralumin][ref_duralumin], [yield][ref_yield_strength], [telemetry][ref_telemetry], [strain gauges][ref_strain_gauge], [accelerometers][ref_accelerometer], [takeoff][ref_takeoff] and [landing gear][ref_landing_gear], the [sound barrier][ref_sound_barrier], [wind tunnels][ref_wind_tunnel], [flight testing][ref_flight_test], [Edwards][ref_edwards_afb] and the [Armstrong Flight Research Center][ref_armstrong_frc], [Bell Aircraft][ref_bell_aircraft], [Chuck Yeager][ref_yeager], the [NACA][ref_naca] and [NASA][ref_nasa] as organizations, the [National Museum of the United States Air Force][ref_nmusaf], the [list of X-planes][ref_list_of_x_planes], or [experimental aircraft][ref_experimental_aircraft] as a category, all of which are treated where they belong.

## Conclusion

The Convair X-6 was never built, and what it would have had to carry can be computed in a page.

A B-36 at cruise needs about a hundred megawatts of thermal power, and a reactor supplying it consumes less than half a kilogram of uranium in a hundred hours against 837 tonnes of kerosene for the same energy. That is the entire attraction and it is a factor of nearly two million. Against it stands twenty-three centimetres of lead, and the geometry that minimizes the total mass puts the reactor about ten metres from the crew, which a B-36 fuselage accommodates easily. The shield that results weighs about 37 tonnes, which is a fifth of the aircraft and very nearly the whole of its bomb load. **A nuclear bomber buys unlimited range by surrendering the payload that made the range worth having.**

The exponential that makes shielding work also makes it stubborn. Shield thickness depends on the logarithm of reactor power, so a thousandfold increase in power costs under nine centimetres of lead, which means the shield is a fixed overhead rather than a proportional cost and small nuclear aircraft are not merely difficult but excluded. The same logarithm means that accepting ten times the crew dose saves about two percent of the aircraft. The programme could not have been rescued by being braver.

One aircraft flew and it was not the X-6. The NB-36H carried a one megawatt reactor 47 times to measure what shielding actually does, and it established that the shielding worked, for a source a hundred times smaller than the one that would have propelled it. A direct-cycle nuclear turbojet ran on a test stand in Idaho and produced thrust from fission. The programme reached that point and was cancelled in 1961, not because the shield defeated it but because ballistic missiles and aerial refuelling had made an indefinitely loitering bomber a solution without a problem.

What survives is a reactor. The Aircraft Reactor Experiment ran at Oak Ridge in 1954 as the world's first molten salt reactor, built because a molten salt core gives high temperature at low pressure, which is what an aircraft wants and, as it turns out, what a good deal else wants too. Seventy years later that concept is under commercial development while the aircraft it was invented for remains unbuilt. A programme that produces no aircraft and one durable reactor technology has not failed in any sense worth the word, and the fact that it is remembered as a failure is a defect in how programmes are scored rather than in what this one did.

The next article takes the [Lockheed X-7][ref_list_of_x_planes], a ramjet test vehicle that was launched rather than flown, and asks what changes when the aircraft is expendable.

## References

### Books

- [Anderson 2001 Fundamentals of Aerodynamics][book_anderson_2001_fundamentals]
- [Anderson 2012 Aircraft Performance and Design][book_anderson_2012_aircraft_performance]
- [Baals and Corliss 1981 Wind Tunnels of NASA][book_baals_corliss_1981]
- [Bertin and Cummings 2013 Aerodynamics for Engineers][book_bertin_cummings_2013]
- [Bevington and Robinson 2002 Data Reduction and Error Analysis][book_bevington_robinson_2002]
- [Bilstein 1989 Orders of Magnitude, A History of the NACA and NASA][book_bilstein_1989_orders]
- [Boley and Weiner 1960 Theory of Thermal Stresses][book_boley_weiner_1960]
- [Box Hunter and Hunter 2005 Statistics for Experimenters][book_box_hunter_hunter_2005]
- [Bruhn 1973 Analysis and Design of Flight Vehicle Structures][book_bruhn_1973]
- [Carslaw and Jaeger 1959 Conduction of Heat in Solids][book_carslaw_jaeger_1959]
- [Chambers and Chambers 2008 Radical Wings and Wind Tunnels][book_chambers_2008_radical_wings]
- [Cover and Thomas 2006 Elements of Information Theory][book_cover_thomas_2006]
- [Ferguson 1992 Engineering and the Mind's Eye][book_ferguson_1992]
- [Gelman et al 2013 Bayesian Data Analysis][book_gelman_et_al_2013]
- [Gorn 2001 Expanding the Envelope, Flight Research at NACA and NASA][book_gorn_2001_expanding_envelope]
- [Gunston 1992 Faster Than Sound][book_gunston_1992_faster_than_sound]
- [Hallion 1972 Supersonic Flight, Breaking the Sound Barrier and Beyond][book_hallion_1972_supersonic_flight]
- [Hallion 1981 On the Frontier, Flight Research at Dryden][book_hallion_1981_on_the_frontier]
- [Hansen 1987 Engineer in Charge][book_hansen_1987_engineer_in_charge]
- [Heppenheimer 2007 Facing the Heat Barrier, A History of Hypersonics][book_heppenheimer_2007_heat_barrier]
- [Hill and Peterson 1991 Mechanics and Thermodynamics of Propulsion][book_hill_peterson_1991]
- [Incropera and DeWitt, Fundamentals of Heat and Mass Transfer][book_incropera_heat_transfer]
- [Jenkins 2000 Hypersonics Before the Shuttle][book_jenkins_2000_hypersonics]
- [Jenkins Landis and Miller 2003 American X-Vehicles, An Inventory X-1 to X-50][book_jenkins_landis_miller_2003]
- [Launius and Jenkins 2012 Coming Home, Reentry and Recovery from Space][book_launius_jenkins_2012]
- [Megson 2016 Aircraft Structures for Engineering Students][book_megson_2016]
- [Merlin 2009 Design and Development of the Blackbird][book_merlin_2009_blackbird]
- [Miller 2001 The X-Planes, X-1 to X-45][book_miller_2001_x_planes]
- [Nicolai and Carichner 2010 Fundamentals of Aircraft and Airship Design][book_nicolai_carichner_2010]
- [Niu 1988 Airframe Structural Design][book_niu_1988_airframe]
- [Peebles 2014 Probing the Sky, Selected NACA Research Airplanes][book_peebles_2014_probing_the_sky]
- [Perrow 1984 Normal Accidents][book_perrow_1984]
- [Petroski 1985 To Engineer Is Human][book_petroski_1985]
- [Raymer 2018 Aircraft Design, A Conceptual Approach][book_raymer_2018]
- [Reason 1990 Human Error][book_reason_1990_human_error]
- [Roskam 1985 Airplane Design][book_roskam_1985]
- [Sagan 1993 The Limits of Safety][book_sagan_1993]
- [Sutton and Biblarz 2016 Rocket Propulsion Elements][book_sutton_biblarz_2016]
- [Taylor 1997 An Introduction to Error Analysis][book_taylor_1997_error_analysis]
- [Torenbeek 1982 Synthesis of Subsonic Airplane Design][book_torenbeek_1982]
- [Vaughan 1996 The Challenger Launch Decision][book_vaughan_1996]
- [Vincenti 1990 What Engineers Know and How They Know It][book_vincenti_1990]
- [Winchester 2005 X-Planes and Prototypes][book_winchester_2005_x_planes]

### Reference

- [NASA Armstrong Flight Research Center][ref_nasa_armstrong]
- [NASA History Office][ref_nasa_x3_factsheet]
- [NASA Technical Reports Server][ref_ntrs]
- [Wikipedia Article on Absorbed Dose][ref_absorbed_dose]
- [Wikipedia Article on Aeroelasticity][ref_aeroelasticity]
- [Wikipedia Article on Argon-41][ref_argon41]
- [Wikipedia Article on Bell Aircraft][ref_bell_aircraft]
- [Wikipedia Article on Beryllium][ref_beryllium]
- [Wikipedia Article on Carswell Air Force Base][ref_carswell]
- [Wikipedia Article on Chuck Yeager][ref_yeager]
- [Wikipedia Article on Directional Stability][ref_directional_stability]
- [Wikipedia Article on Duralumin][ref_duralumin]
- [Wikipedia Article on Dynamic Pressure][ref_dynamic_pressure]
- [Wikipedia Article on Edwards Air Force Base][ref_edwards_afb]
- [Wikipedia Article on Enriched Uranium][ref_enriched_uranium]
- [Wikipedia Article on Experimental Aircraft][ref_experimental_aircraft]
- [Wikipedia Article on Flight Dynamics][ref_flight_dynamics]
- [Wikipedia Article on Flight Testing][ref_flight_test]
- [Wikipedia Article on Flow Separation][ref_flow_separation]
- [Wikipedia Article on Idaho National Laboratory][ref_inl]
- [Wikipedia Article on Ionizing Radiation][ref_ionizing]
- [Wikipedia Article on Landing Gear][ref_landing_gear]
- [Wikipedia Article on Lead][ref_lead_element]
- [Wikipedia Article on Lithium Hydride][ref_lih]
- [Wikipedia Article on Longitudinal Static Stability][ref_longitudinal_static_stability]
- [Wikipedia Article on Measurement Uncertainty][ref_measurement_uncertainty]
- [Wikipedia Article on NASA][ref_nasa]
- [Wikipedia Article on NERVA][ref_nerva]
- [Wikipedia Article on Neutron Radiation][ref_neutron_rad]
- [Wikipedia Article on Nuclear and Radiation Accidents][ref_nuclear_accidents]
- [Wikipedia Article on Nuclear Fission][ref_fission]
- [Wikipedia Article on Nuclear Fuel][ref_nuclear_fuel]
- [Wikipedia Article on Oak Ridge National Laboratory][ref_ornl]
- [Wikipedia Article on Project Pluto][ref_project_pluto]
- [Wikipedia Article on Propagation of Uncertainty][ref_propagation_of_uncertainty]
- [Wikipedia Article on Radiation Hardening][ref_rad_hardening]
- [Wikipedia Article on Radiation Protection][ref_rad_protection]
- [Wikipedia Article on Supersonic Speed][ref_supersonic_speed]
- [Wikipedia Article on Takeoff][ref_takeoff]
- [Wikipedia Article on Telemetry][ref_telemetry]
- [Wikipedia Article on the Accelerometer][ref_accelerometer]
- [Wikipedia Article on the Aerodynamic Center][ref_aerodynamic_center]
- [Wikipedia Article on the Armstrong Flight Research Center][ref_armstrong_frc]
- [Wikipedia Article on the Aspect Ratio][ref_aspect_ratio]
- [Wikipedia Article on the Attenuation Coefficient][ref_attenuation]
- [Wikipedia Article on the Boundary Layer][ref_boundary_layer]
- [Wikipedia Article on the Convair B-36 Peacemaker][ref_b36]
- [Wikipedia Article on the Convair NB-36H][ref_nb36h]
- [Wikipedia Article on the Convair X-6][ref_convair_x6]
- [Wikipedia Article on the Convair YB-60][ref_yb60]
- [Wikipedia Article on the Delta Wing][ref_delta_wing]
- [Wikipedia Article on the Drag Coefficient][ref_drag_coefficient]
- [Wikipedia Article on the Flight Envelope][ref_flight_envelope]
- [Wikipedia Article on the Gamma Ray][ref_gamma]
- [Wikipedia Article on the General Electric J47][ref_j47]
- [Wikipedia Article on the Half-Value Layer][ref_hvl]
- [Wikipedia Article on the Heat Exchanger][ref_heat_exchanger]
- [Wikipedia Article on the International Standard Atmosphere][ref_isa]
- [Wikipedia Article on the Lift Coefficient][ref_lift_coefficient]
- [Wikipedia Article on the Lift-to-Drag Ratio][ref_lift_to_drag]
- [Wikipedia Article on the Load Factor][ref_load_factor]
- [Wikipedia Article on the Mach Number][ref_mach_number]
- [Wikipedia Article on the Molten Salt Reactor][ref_msr]
- [Wikipedia Article on the Moment of Inertia][ref_moment_of_inertia]
- [Wikipedia Article on the Monte Carlo Method][ref_monte_carlo]
- [Wikipedia Article on the National Advisory Committee for Aeronautics][ref_naca]
- [Wikipedia Article on the National Museum of the United States Air Force][ref_nmusaf]
- [Wikipedia Article on the Neutron Moderator][ref_moderator]
- [Wikipedia Article on the Nuclear Reactor][ref_reactor]
- [Wikipedia Article on the Nuclear Thermal Rocket][ref_ntr]
- [Wikipedia Article on the Oblique Shock][ref_oblique_shock]
- [Wikipedia Article on the Prandtl Number][ref_prandtl_number]
- [Wikipedia Article on the Reynolds Number][ref_reynolds_number]
- [Wikipedia Article on the Shock Wave][ref_shock_wave]
- [Wikipedia Article on the Sievert][ref_sievert]
- [Wikipedia Article on the Sound Barrier][ref_sound_barrier]
- [Wikipedia Article on the Speed of Sound][ref_speed_of_sound]
- [Wikipedia Article on the Stability Augmentation System][ref_stability_augmentation]
- [Wikipedia Article on the Strain Gauge][ref_strain_gauge]
- [Wikipedia Article on the Swept Wing][ref_swept_wing]
- [Wikipedia Article on the Tupolev Tu-95LAL][ref_tu95lal]
- [Wikipedia Article on the Turbojet][ref_turbojet]
- [Wikipedia Article on the U.S. Standard Atmosphere][ref_us_standard_atmosphere]
- [Wikipedia Article on the United States Atomic Energy Commission][ref_aec]
- [Wikipedia Article on the Wind Tunnel][ref_wind_tunnel]
- [Wikipedia Article on the Wing Root][ref_wing_root]
- [Wikipedia Article on Transonic Flow][ref_transonic]
- [Wikipedia Article on Wave Drag][ref_wave_drag]
- [Wikipedia Article on Wing Configuration][ref_wing_configuration]
- [Wikipedia Article on Wing Loading][ref_wing_loading]
- [Wikipedia Article on Yield in Engineering][ref_yield_strength]
- [Wikipedia List of X-Planes][ref_list_of_x_planes]
- [Wikipedia Section on Buffeting][ref_buffeting]

### Research

- [Abdussami et al 2025 Evaluation of Nuclear Microreactor Cost-Competitiveness][research_abdussami_2025]
- [Ahmed 2026 Neutron Shielding, Advanced Mechanisms, Challenges, and Material Strategies][research_ahmed_2026]
- [Alnuaimi and Kim 2026 Feasibility and Performance of a Liquid Uranium-Manganese Nuclear Thermal Rocket][research_alnuaimi_2026]
- [Ancona et al 2025 Feasibility Study of a Mission to Sedna, Nuclear Propulsion and Advanced Concepts][research_ancona_2025]
- [Atomic Energy Commission 1950 NEPA Project quarterly progress report, April 1--June 30, 1950][research_aec_1950_2]
- [Atomic Energy Commission 1950 Nuclear Powered Aircraft for Antisubmarine Warfare][research_aec_1950]
- [Atomic Energy Commission 1957 Aircraft Nuclear Propulsion Project Quarterly Progress Report For Period Ending June 30, 1957][research_aec_1957_3]
- [Atomic Energy Commission 1957 Aircraft Nuclear Propulsion Project Quarterly Progress Report For Period Ending March 31, 1957][research_aec_1957_2]
- [Atomic Energy Commission 1957 Background Information For Nuclear Aircraft Safety Analysis Program][research_aec_1957]
- [Atomic Energy Commission 1959 Aircraft Nuclear Propulsion Project Semiannual Progress Report For Period Ending September 30, 1958][research_aec_1959_3]
- [Atomic Energy Commission 1959 Data on Nuclear J-58 Hot Day Performance and Reactor and Shield Information on a Twin 200 Mw Reactor, Six J58 Engine Powerplant][research_aec_1959_2]
- [Atomic Energy Commission 1959 Papers Presented At Anp Materials Meeting November 16-18, 1954, Wright Air Development Center, Dayton, Ohio][research_aec_1959_4]
- [Atomic Energy Commission 1959 Summary Report of HTRE No, 3 Nuclear Excursion][research_aec_1959]
- [Atomic Energy Commission 1961 Papers From Seventh Semiannual Shielding Information Meeting, October 14- 15, 1959][research_aec_1961]
- [Aueron and Thomas 2024 Assessment of Electric-Pump-Fed Nuclear Thermal Propulsion][research_aueron_2024]
- [Bali and Mayer 2025 Investigation of Decay Heat Removal Systems in the ALLEGRO Helium-Cooled Reactor][research_bali_2025]
- [Beever and Rusling 1965 The Importance of Space Radiation Shielding Weight][research_beever_1965]
- [Bettis et al 1957 The Aircraft Reactor Experiment, Operation][research_bettis_1957]
- [Bhardwaj et al 2024 Fabrication of Neutron Absorbing Metal Hydride Entrained Ceramic Matrix Composites][research_bhardwaj_2024]
- [Bigelow and Greenstreet 1957 The P & Wa Circulating Fuel Reflector-Moderator Reactor, Volume 2, Appendix A, Design Specifications And Reference Information For The][research_bigelow_1957]
- [Blizard 1953 Shield Optimization][research_blizard_1953]
- [Buckingham 1914 On Physically Similar Systems][research_buckingham_1914]
- [Cannon et al 1961 Laboratory Studies For Htre Fuel Reprocessing][research_cannon_1961]
- [Capo et al 1957 Shielding Computer Programs 01-0, 02-0, And 03-0 Reactor Shield Analysis][research_capo_1957]
- [Cavicchi et al 1959 Design Analysis of a Subsonic Nuclear Powered Logistic Airplane with Helium-Colled Reactor][research_cavicchi_1959]
- [Cetegen et al 2025 Evaluating the Economic Feasibility of Lithium-Ion Battery Energy Storage][research_cetegen_2025]
- [Chaloner and Verdinelli 1995 Bayesian Experimental Design, A Review][research_chaloner_verdinelli_1995]
- [Cheng et al 2025 Aggregation of Noble Metal Fission Products and Protactinium-233 in a Molten Salt Reactor][research_cheng_2025]
- [Comassar 1962 General Electric Direct-Air-Cycle Aircraft Nuclear Propulsion Program, Aircraft Nuclear Propulsion Application Studies (Comprehensive][research_comassar_1962]
- [Cottrell 1951 Aircraft Nuclear Propulsion Project Quarterly Progress Report For Period Ending March 10, 1951][research_cottrell_1951]
- [Cottrell 1952 Aircraft Nuclear Propulsion Project Quarterly Progress Report For Period Ending December 10, 1951][research_cottrell_1952]
- [Cottrell 1952 Aircraft Nuclear Propulsion Project Quarterly Progress Report For Period Ending June 10, 1952][research_cottrell_1952_2]
- [Cottrell 1952 Aircraft Reactor Experiment Hazards Summary Report][research_cottrell_1952_3]
- [Cottrell et al 1955 Operation Of The Aircraft Reactor Experiment][research_cottrell_1955_2]
- [Cottrell et al 1958 Disassembly And Postoperative Examination Of The Aircraft Reactor Experiment][research_cottrell_1958]
- [Creasman et al 2024 Fuel Depletion Study of the Molten Salt Demonstration Reactor][research_creasman_2024]
- [deGanahl et al 1954 Supercritical Water Reactor Shield Design Procedure][research_deganahl_1954]
- [DeWitt and Benton 2024 Secondary Proton Buildup in Space Radiation Shielding][research_dewitt_2024]
- [Dibble 1958 Aircraft Nuclear Propulsion Department, Administrative Report][research_dibble_1958]
- [Domingos et al 2026 Neutronic Behavior of Alternative Fuels in a Microreactor Design][research_domingos_2026]
- [Doyle 1948 Calculated Condenser Performance for a Mercury-Turbine Power Plant for Aircraft][research_doyle_1948]
- [Doyle 1951 Calculated performance of a mercury-compressor-jet powered airplane using a nuclear reactor as an energy source][research_doyle_1951]
- [Duan et al 2026 Reactivity Safety Analysis of an Air-Cooled Nuclear Thermal Propulsion Reactor][research_duan_2026]
- [Dunkle and Bogetic 2026 Molten Salt Reactor Loss of Flow Accident Analysis][research_dunkle_2026]
- [Edwards 1954 Effect Of Altitude And Flight Speed On Shielding Requirements][research_edwards_1954]
- [Edwards 1957 Specifications-Shielding Computer Programs 14-0, 14-1, And 14-2, Reactor Shield Analysis][research_edwards_1957]
- [Edwards and Simpson 1962 REACTOR AND SHIELD PHYSICS, Comprehensive Technical Report, General Electric Direct-Air-Cycle, Aircraft Nuclear Propulsion Program][research_edwards_1962]
- [Edwards et al 1958 Shielding Computer Program 04-0, Reactor Shield Analysis][research_edwards_1958]
- [Elkhawas et al 2025 Deployment Study of Accident Tolerant Fuels in Small Modular Advanced Reactors][research_elkhawas_2025]
- [Finger and Rom 1962 Nuclear Propulsion. State Of The Art - 1962][research_finger_1962]
- [Fischer and Bures 2024 Application of Modelica and TRANSFORM to System Modeling of the Molten Salt Reactor Experiment][research_fischer_2024]
- [Fraas and Savolainen 1954 ORNL Aircraft Nuclear Power Plant Designs][research_fraas_1954]
- [Frankfort 1956 A Conceptual Design Of A Shield Testing And Materials Irradiation Facility][research_frankfort_1956]
- [Fries 1958 Radiation-Resistant Motors For Nuclear Aircraft Controls][research_fries_1958]
- [Gamertsfelder 1954 Htre Hazards Report][research_gamertsfelder_1954]
- [Gasser 1947 The Army Air Forces NEPA Project][research_gasser_1947]
- [Gates et al 1961 Development of Ceramic Fibers for Reinforcement in Composite Materials][research_gates_1961]
- [Gedwill et al 1965 Fuel-Retention Properties of Tungsten-Uranium Dioxide Composites][research_gedwill_1965]
- [Gilbert 1955 A Program for Investigation of Metallic Hydrides as Moderators, Reflectors, and Shields for Aircraft Reactors][research_gilbertjr_1955]
- [Gorker 1955 Aircraft Reactor Control System Applicable To Turbojet And Turboprop Power Plants][research_gorker_1955]
- [Gotsky et al 1959 Two-Dimensional Diffusion Theory Analysis of Reactivity Effects of a Fuel-Plate-Removal Experiment][research_gotsky_1959]
- [Guilbaud et al 2024 Full Core Study of the KIWI-B-4E Nuclear Thermal Propulsion System][research_guilbaud_2024]
- [Han et al 2025 Design of New Shielding Materials for Space Reactor Shielding Structures][research_han_2025]
- [Han et al 2025 Optimization of Radiation Shielding Composite Materials][research_han_2025_2]
- [Hedden 1962 Design Criteria For Lithium-Cooled Reactor Experiment (Lcre) At Nrts][research_hedden_1962]
- [Henry 1958 Multilayer Shield Experiment Iv, Otf Iii][research_henry_1958]
- [Holcomb 2025 Disruptive Thermal-Spectrum Molten Salt Breeder Reactor Fuel Cycle Technology][research_holcomb_2025]
- [Huang et al 2025 Shielding Optimization of a Heat Pipe Cooled Reactor][research_huang_2025]
- [Humble et al 1950 Preliminary analysis of three cycles for nuclear propulsion of aircraft][research_humble_1950]
- [Islam and Haque 2025 A Comparative Study and Design Optimization of Potential Cladding Materials][research_islam_2025]
- [Jagtap et al 2024 Conceptual Design Optimisation of a Subsonic Hydrogen-Powered Long-Range Aircraft][research_jagtap_2024]
- [Johnson 1960 Shield specification No, 1025, [Reactor CRS-1018]][research_johnson_1960]
- [Jordan et al 1957 Aircraft Nuclear Propulsion Program, Quarterly Progress Report for Period Ending December 31, 1956, Part 1 - 5][research_jordan_1957]
- [Kam and Schamberger 1961 Military Compact Reactor Program Shield Study In The Ornl Lid Tank, Supplement][research_kam_1961]
- [Khan et al 2025 A Novel Neutron-Gamma Spectrum-Based Composite Shielding Material][research_khan_2025]
- [Kim and Macfarlane 2026 Challenges of Small Modular Reactors, A Comprehensive Exploration][research_kim_2026]
- [Kress 1958 Equipment Modifications For The Astr-Tsf Experiment][research_kress_1958]
- [Lan et al 2024 Internal Stress Analysis of Irradiated Graphite Cores in a Gas-Cooled Reactor][research_lan_2024]
- [Larson 1958 Powerplant Performance for a Supersonic Nuclear Turbojet Powerplant][research_larson_1958_2]
- [Larson 1958 Reactor, Shield and Performance Data for a Nuclear Turbojet Powerplant][research_larson_1958]
- [Larson 1959 Advanced nuclear turbojet powerplant characteristics summary for supersonic aircraft][research_larson_1959]
- [Larson 1959 Pratt and Whitney Aircraft Nuclear JT-11 Turbojet Engine Performance with Advanced Nuclear System][research_larson_1959_2]
- [Lee 1958 Shield Weights for Boeing Mission for the PWAR-11 and the PWAR-X][research_lee_1958]
- [Lee and Cho 2025 Introducing a Radiation Target Level for the Shielding Design of a Nuclear System][research_lee_2025]
- [Level 1962 Metallic Fuel element Materials, Comprehensive Technical Report, General Electric Direct-Air-Cycle, Aircraft Nuclear Propulsion Program][research_level_1962]
- [Levine and Ekern 1960 Radiation Effects On Electronic Systems, Designing Electronic Systems For Nuclear-Powered Aircraft Requires Knowing Response Of System][research_levine_1960]
- [Levine and Ekern 1961 RADIATION EFFECTS--A MAJOR INFLUENCE IN DESIGNING ELECTRONIC SYSTEMS FOR USE IN NUCLEAR-POWERED AIRCRAFT, Paper 8 of FOURTH RADIATION][research_levine_1961]
- [Li 2024 A Review of Hydrogen-Powered Aircraft][research_li_2024]
- [Lindley 1956 On a Measure of the Information Provided by an Experiment][research_lindley_1956]
- [Liu et al 2026 An Intelligent Method for Dual-Stage Radiation-Shielding Optimization][research_liu_2026]
- [Lu et al 2025 Exhaust Heat Recovery for Cryogenic Hydrogen-Powered Aircraft][research_lu_2025]
- [Ma et al 2026 Comparative Study of Power Control Methods for a Space Nuclear Electric System][research_ma_2026]
- [Magnuson and Callihan 1956 Critical Experiments for a Proposed Tower Shielding Reactor][research_magnuson_1956]
- [Matthia and Berger 2024 Radiation Exposure and Shielding Effects on the Lunar Surface][research_matthia_2024]
- [McFarlane 2024 Cradle to Grave, the Importance of the Fuel Cycle to Molten Salt Reactors][research_mcfarlane_2024]
- [Meyer 1965 ANP Powerplant Data][research_meyer_1965]
- [Mishra et al 2024 Irradiated Fuel Salt Data Library for a Molten Salt Reactor][research_mishra_2024]
- [Mitchell 1954 Shield Design Calculations For Ac-Series Power Plants][research_mitchell_1954]
- [Mochizuki 2024 Load Following Characteristics of a Molten Salt Fast Reactor][research_mochizuki_2024]
- [Mochizuki 2026 Long-Term Cooling Characteristics During Transients][research_mochizuki_2026]
- [Moteff 1960 Proposed Two-Component Method Of Nuclear Shield Analysis][research_moteff_1960]
- [NA 1957 Aircraft Nuclear Propulsion Project Quarterly Progress Report for Period Ending December 31, 1956][research_na_1957]
- [NACA 1962 Proceedings of Nuclear Propulsion Conference][research_naca_1962]
- [NACA 1963 Preliminary hazards summary for Nerva irradiation testing at Plum Brook Reactor Facility][research_naca_1963]
- [Nance 1957 Calibration Of The Astr][research_nance_1957]
- [Niu et al 2024 Selective Extraction of Molybdenum-99 from Molten Salt Reactor Fuel Salt][research_niu_2024]
- [Nyquist 1928 Certain Topics in Telegraph Transmission Theory][research_nyquist_1928]
- [Ogul et al 2026 Multilayer Radiation Shielding Assessment of the Korean SMART Small Modular Reactor][research_ogul_2026]
- [Parisi and Arafat 2026 MARVEL Microreactor System Thermal-Hydraulic Design and Analysis][research_parisi_2026]
- [Peng et al 2024 Aircraft Lithium Battery Energy Balancing Method][research_peng_2024]
- [Perry 1958 Technical Briefing for Aircraft Nuclear Propulsion Office Representatives on November 7 and 8, 1958][research_perry_1958]
- [Phelps 1961 Front shield weight and C, G][research_phelps_1961]
- [Rangel et al 2026 Conceptual Design of a Pressurized Water Microreactor Core Without Enriched Uranium][research_rangel_2026]
- [Reetz 1965 Second Symposium on Protection Against Radiations in Space][research_reetz_1965]
- [Ross 1960 Optimization Of Reactor Coolant Flow For The Aircraft Shield Test Reactor][research_ross_1960]
- [Ruffman 1952 Performance Parameters Pertinent to Nuclear Powered Aircraft][research_ruffman_1952]
- [Sasi et al 2025 Hydrogen and Ammonia Powered Turbofan Design Implications][research_sasi_2025]
- [Savage et al 1958 Components Of The Fused-Salt And Sodium Circuits Of The Aircraft Reactor Experiment][research_savage_1958]
- [Savolainen 1954 Aircraft Nuclear Propulsion Project Quarterly Progress Report For Period Ending September 10, 1954][research_savolainen_1954]
- [Schaeffer and Stokes 1958 Astr Fast Neutron Spectra][research_schaeffer_1958]
- [Schmickrath 1960 Engineering Proposal for Design and Development Work on a Nuclear Turbojet Propulsion Unit - Prepared for Aircraft Nuclear Propulsion Office][research_schmickrath_1960]
- [Sekkat et al 2026 Energy-Dependent Shielding Performance of High-Z Epoxy Composite Shields][research_sekkat_2026]
- [Shannon 1948 A Mathematical Theory of Communication][research_shannon_1948]
- [Shobeiri et al 2025 Accelerating Small Modular Reactor Deployment and the Clean Energy Transition][research_shobeiri_2025]
- [Shoults 1958 Test Of A Direct Cycle Nuclear Turbojet System][research_shoults_1958]
- [Stever 1948 Lexington Project Report # 0 - Minutes of meeting with representatives of the Army, Air Force, AEC, and NEPA -- The Need and Use of][research_stever_1948_2]
- [Stever 1948 Lexington Project Report #73, Minutes of Meeting Held May 12 and13, 1948 Between Representatives of NEPA and Project Lexington and AEC][research_stever_1948]
- [Stone et al 2024 Characterization of Aluminium and Boron Carbide Based Additively Manufactured Shielding][research_stone_2024]
- [Sun et al 2025 Preliminary Study on the Postulated Siting Accident Source Term][research_sun_2025]
- [Thornton and Blumberg 1961 ANP HTREs FULFILL TEST GOALS][research_thornton_1961]
- [Troubetzkoy and Kalos 1961 Military Compact Reactor Program Studies In The Synthesis Of Minimum Weight Shields][research_troubetzkoy_1961]
- [Wahler et al 2025 Conceptual Design and Aerostructural Trade-Offs in Hydrogen-Powered Aircraft][research_wahler_2025]
- [Welch 1961 Properties Of Lithium Hydride, Iii, Summary Of Ge-Anpd Data][research_welch_1961]
- [Williams and Drake, The Research Airplane, Past, Present, and Future][research_williams_drake_1948]
- [Woodbridge 1955 Preliminary Htre No, 1 Project 100 Operation Manual 21, Reactor Assembly, Core "A"][research_woodbridge_1955]
- [Woodsum and Rost 1957 Shield Weights][research_woodsum_1957]
- [Yildirim and Opcin 2026 Multilayer ZTA-Core Composite with Bio-Derived Coatings for Space Radiation Shielding][research_yildirim_2026]
- [Yilmaz et al 2025 Neutronic Analysis of a Thorium-Uranium Molten Salt Reactor with FLiBe Salt][research_yilmaz_2025]
- [Zhang et al 2026 Crashworthiness Design of Hydrogen-Powered Regional Aircraft][research_zhang_2026]

### Related Post

- [A106 Two-Stage Flying Delta Wing Vehicles][related_post_a106_two_stage_delta_wing]
- [A217 Rocket Propellant Chemistry, A Design-Tradeoff Space][related_post_a217_rocket_propellant_chemistry]
- [A237 Framing and the Co-Development Mechanism][related_post_a237_aerospace_framing]
- [A241 Aerospace Simulation and Real-Time Systems][related_post_a241_aerospace_simulation]
- [A297 X-Planes, Framing and the Research Aircraft Model][related_post_a297_xplanes_framing]
- [A298 X-Planes, Bell X-1][related_post_a298_bell_x1]
- [A299 X-Planes, Bell X-2][related_post_a299_bell_x2]
- [A300 X-Planes, Douglas X-3 Stiletto][related_post_a300_douglas_x3]
- [A301 X-Planes, Northrop X-4 Bantam][related_post_a301_northrop_x4]
- [A302 X-Planes, Bell X-5][related_post_a302_bell_x5]
- [A90 Introduction to Space Studies][related_post_a90_intro_space_studies]
- [A96 History of Rocketplanes][related_post_a96_history_rocketplanes]

[book_anderson_2001_fundamentals]: https://openlibrary.org/search?q=Anderson+Fundamentals+of+Aerodynamics
[book_anderson_2012_aircraft_performance]: https://openlibrary.org/search?q=Anderson+Aircraft+Performance+and+Design
[book_baals_corliss_1981]: https://openlibrary.org/search?q=Baals+Corliss+Wind+Tunnels+of+NASA
[book_bertin_cummings_2013]: https://openlibrary.org/search?q=Bertin+Cummings+Aerodynamics+for+Engineers
[book_bevington_robinson_2002]: https://openlibrary.org/search?q=Bevington+Robinson+Data+Reduction+and+Error+Analysis
[book_bilstein_1989_orders]: https://openlibrary.org/search?q=Bilstein+Orders+of+Magnitude+NACA+NASA
[book_boley_weiner_1960]: https://openlibrary.org/search?q=Boley+Weiner+Theory+of+Thermal+Stresses
[book_box_hunter_hunter_2005]: https://openlibrary.org/search?q=Box+Hunter+Statistics+for+Experimenters
[book_bruhn_1973]: https://openlibrary.org/search?q=Bruhn+Analysis+and+Design+of+Flight+Vehicle+Structures
[book_carslaw_jaeger_1959]: https://openlibrary.org/search?q=Carslaw+Jaeger+Conduction+of+Heat+in+Solids
[book_chambers_2008_radical_wings]: https://openlibrary.org/search?q=Chambers+Radical+Wings+and+Wind+Tunnels
[book_cover_thomas_2006]: https://openlibrary.org/search?q=Cover+Thomas+Elements+of+Information+Theory
[book_ferguson_1992]: https://openlibrary.org/search?q=Ferguson+Engineering+and+the+Mind+s+Eye
[book_gelman_et_al_2013]: https://openlibrary.org/search?q=Gelman+Bayesian+Data+Analysis
[book_gorn_2001_expanding_envelope]: https://openlibrary.org/search?q=Gorn+Expanding+the+Envelope+Flight+Research
[book_gunston_1992_faster_than_sound]: https://openlibrary.org/search?q=Gunston+Faster+Than+Sound
[book_hallion_1972_supersonic_flight]: https://openlibrary.org/search?q=Hallion+Supersonic+Flight+Breaking+the+Sound+Barrier
[book_hallion_1981_on_the_frontier]: https://openlibrary.org/search?q=Hallion+On+the+Frontier+Flight+Research+Dryden
[book_hansen_1987_engineer_in_charge]: https://openlibrary.org/search?q=Hansen+Engineer+in+Charge+Langley
[book_heppenheimer_2007_heat_barrier]: https://openlibrary.org/search?q=Heppenheimer+Facing+the+Heat+Barrier+Hypersonics
[book_hill_peterson_1991]: https://openlibrary.org/search?q=Hill+Peterson+Mechanics+and+Thermodynamics+of+Propulsion
[book_incropera_heat_transfer]: https://openlibrary.org/search?q=Incropera+Fundamentals+of+Heat+and+Mass+Transfer
[book_jenkins_2000_hypersonics]: https://openlibrary.org/search?q=Jenkins+Hypersonics+Before+the+Shuttle+X-15
[book_jenkins_landis_miller_2003]: https://openlibrary.org/search?q=Jenkins+Landis+Miller+American+X-Vehicles+Inventory
[book_launius_jenkins_2012]: https://openlibrary.org/search?q=Launius+Jenkins+Coming+Home+Reentry+and+Recovery+from+Space
[book_megson_2016]: https://openlibrary.org/search?q=Megson+Aircraft+Structures+for+Engineering+Students
[book_merlin_2009_blackbird]: https://openlibrary.org/search?q=Merlin+Design+and+Development+of+the+Blackbird
[book_miller_2001_x_planes]: https://openlibrary.org/search?q=Jay+Miller+The+X-Planes+X-1+to+X-45
[book_nicolai_carichner_2010]: https://openlibrary.org/search?q=Nicolai+Carichner+Fundamentals+of+Aircraft+and+Airship+Design
[book_niu_1988_airframe]: https://openlibrary.org/search?q=Niu+Airframe+Structural+Design
[book_peebles_2014_probing_the_sky]: https://openlibrary.org/search?q=Peebles+Probing+the+Sky+NACA+Research+Airplanes
[book_perrow_1984]: https://openlibrary.org/search?q=Perrow+Normal+Accidents
[book_petroski_1985]: https://openlibrary.org/search?q=Petroski+To+Engineer+Is+Human
[book_raymer_2018]: https://openlibrary.org/search?q=Raymer+Aircraft+Design+A+Conceptual+Approach
[book_reason_1990_human_error]: https://openlibrary.org/search?q=James+Reason+Human+Error
[book_roskam_1985]: https://openlibrary.org/search?q=Roskam+Airplane+Design
[book_sagan_1993]: https://openlibrary.org/search?q=Sagan+The+Limits+of+Safety
[book_sutton_biblarz_2016]: https://openlibrary.org/search?q=Sutton+Biblarz+Rocket+Propulsion+Elements
[book_taylor_1997_error_analysis]: https://openlibrary.org/search?q=Taylor+An+Introduction+to+Error+Analysis
[book_torenbeek_1982]: https://openlibrary.org/search?q=Torenbeek+Synthesis+of+Subsonic+Airplane+Design
[book_vaughan_1996]: https://openlibrary.org/search?q=Vaughan+The+Challenger+Launch+Decision
[book_vincenti_1990]: https://openlibrary.org/search?q=Vincenti+What+Engineers+Know+and+How+They+Know+It
[book_winchester_2005_x_planes]: https://openlibrary.org/search?q=Winchester+X-Planes+and+Prototypes
[ref_absorbed_dose]: https://en.wikipedia.org/wiki/Absorbed_dose
[ref_accelerometer]: https://en.wikipedia.org/wiki/Accelerometer
[ref_aec]: https://en.wikipedia.org/wiki/United_States_Atomic_Energy_Commission
[ref_aerodynamic_center]: https://en.wikipedia.org/wiki/Aerodynamic_center
[ref_aeroelasticity]: https://en.wikipedia.org/wiki/Aeroelasticity
[ref_argon41]: https://en.wikipedia.org/wiki/Argon-41
[ref_armstrong_frc]: https://en.wikipedia.org/wiki/Armstrong_Flight_Research_Center
[ref_aspect_ratio]: https://en.wikipedia.org/wiki/Aspect_ratio_(aeronautics)
[ref_attenuation]: https://en.wikipedia.org/wiki/Attenuation_coefficient
[ref_b36]: https://en.wikipedia.org/wiki/Convair_B-36_Peacemaker
[ref_bell_aircraft]: https://en.wikipedia.org/wiki/Bell_Aircraft
[ref_beryllium]: https://en.wikipedia.org/wiki/Beryllium
[ref_boundary_layer]: https://en.wikipedia.org/wiki/Boundary_layer
[ref_buffeting]: https://en.wikipedia.org/wiki/Aeroelasticity#Buffeting
[ref_carswell]: https://en.wikipedia.org/wiki/Carswell_Air_Force_Base
[ref_convair_x6]: https://en.wikipedia.org/wiki/Convair_X-6
[ref_delta_wing]: https://en.wikipedia.org/wiki/Delta_wing
[ref_directional_stability]: https://en.wikipedia.org/wiki/Directional_stability
[ref_drag_coefficient]: https://en.wikipedia.org/wiki/Drag_coefficient
[ref_duralumin]: https://en.wikipedia.org/wiki/Duralumin
[ref_dynamic_pressure]: https://en.wikipedia.org/wiki/Dynamic_pressure
[ref_edwards_afb]: https://en.wikipedia.org/wiki/Edwards_Air_Force_Base
[ref_enriched_uranium]: https://en.wikipedia.org/wiki/Enriched_uranium
[ref_experimental_aircraft]: https://en.wikipedia.org/wiki/Experimental_aircraft
[ref_fission]: https://en.wikipedia.org/wiki/Nuclear_fission
[ref_flight_dynamics]: https://en.wikipedia.org/wiki/Flight_dynamics_(fixed-wing_aircraft)
[ref_flight_envelope]: https://en.wikipedia.org/wiki/Flight_envelope
[ref_flight_test]: https://en.wikipedia.org/wiki/Flight_test
[ref_flow_separation]: https://en.wikipedia.org/wiki/Flow_separation
[ref_gamma]: https://en.wikipedia.org/wiki/Gamma_ray
[ref_heat_exchanger]: https://en.wikipedia.org/wiki/Heat_exchanger
[ref_hvl]: https://en.wikipedia.org/wiki/Half-value_layer
[ref_inl]: https://en.wikipedia.org/wiki/Idaho_National_Laboratory
[ref_ionizing]: https://en.wikipedia.org/wiki/Ionizing_radiation
[ref_isa]: https://en.wikipedia.org/wiki/International_Standard_Atmosphere
[ref_j47]: https://en.wikipedia.org/wiki/General_Electric_J47
[ref_landing_gear]: https://en.wikipedia.org/wiki/Landing_gear
[ref_lead_element]: https://en.wikipedia.org/wiki/Lead
[ref_lift_coefficient]: https://en.wikipedia.org/wiki/Lift_coefficient
[ref_lift_to_drag]: https://en.wikipedia.org/wiki/Lift-to-drag_ratio
[ref_lih]: https://en.wikipedia.org/wiki/Lithium_hydride
[ref_list_of_x_planes]: https://en.wikipedia.org/wiki/List_of_X-planes
[ref_load_factor]: https://en.wikipedia.org/wiki/Load_factor_(aeronautics)
[ref_longitudinal_static_stability]: https://en.wikipedia.org/wiki/Longitudinal_static_stability
[ref_mach_number]: https://en.wikipedia.org/wiki/Mach_number
[ref_measurement_uncertainty]: https://en.wikipedia.org/wiki/Measurement_uncertainty
[ref_moderator]: https://en.wikipedia.org/wiki/Neutron_moderator
[ref_moment_of_inertia]: https://en.wikipedia.org/wiki/Moment_of_inertia
[ref_monte_carlo]: https://en.wikipedia.org/wiki/Monte_Carlo_method
[ref_msr]: https://en.wikipedia.org/wiki/Molten_salt_reactor
[ref_naca]: https://en.wikipedia.org/wiki/National_Advisory_Committee_for_Aeronautics
[ref_nasa]: https://en.wikipedia.org/wiki/NASA
[ref_nasa_armstrong]: https://www.nasa.gov/centers-and-facilities/armstrong/
[ref_nasa_x3_factsheet]: https://www.nasa.gov/history/
[ref_nb36h]: https://en.wikipedia.org/wiki/Convair_NB-36H
[ref_nerva]: https://en.wikipedia.org/wiki/NERVA
[ref_neutron_rad]: https://en.wikipedia.org/wiki/Neutron_radiation
[ref_nmusaf]: https://en.wikipedia.org/wiki/National_Museum_of_the_United_States_Air_Force
[ref_ntr]: https://en.wikipedia.org/wiki/Nuclear_thermal_rocket
[ref_ntrs]: https://ntrs.nasa.gov/
[ref_nuclear_accidents]: https://en.wikipedia.org/wiki/Nuclear_and_radiation_accidents_and_incidents
[ref_nuclear_fuel]: https://en.wikipedia.org/wiki/Nuclear_fuel
[ref_oblique_shock]: https://en.wikipedia.org/wiki/Oblique_shock
[ref_ornl]: https://en.wikipedia.org/wiki/Oak_Ridge_National_Laboratory
[ref_prandtl_number]: https://en.wikipedia.org/wiki/Prandtl_number
[ref_project_pluto]: https://en.wikipedia.org/wiki/Project_Pluto
[ref_propagation_of_uncertainty]: https://en.wikipedia.org/wiki/Propagation_of_uncertainty
[ref_rad_hardening]: https://en.wikipedia.org/wiki/Radiation_hardening
[ref_rad_protection]: https://en.wikipedia.org/wiki/Radiation_protection
[ref_reactor]: https://en.wikipedia.org/wiki/Nuclear_reactor
[ref_reynolds_number]: https://en.wikipedia.org/wiki/Reynolds_number
[ref_shock_wave]: https://en.wikipedia.org/wiki/Shock_wave
[ref_sievert]: https://en.wikipedia.org/wiki/Sievert
[ref_sound_barrier]: https://en.wikipedia.org/wiki/Sound_barrier
[ref_speed_of_sound]: https://en.wikipedia.org/wiki/Speed_of_sound
[ref_stability_augmentation]: https://en.wikipedia.org/wiki/Stability_augmentation_system
[ref_strain_gauge]: https://en.wikipedia.org/wiki/Strain_gauge
[ref_supersonic_speed]: https://en.wikipedia.org/wiki/Supersonic_speed
[ref_swept_wing]: https://en.wikipedia.org/wiki/Swept_wing
[ref_takeoff]: https://en.wikipedia.org/wiki/Takeoff
[ref_telemetry]: https://en.wikipedia.org/wiki/Telemetry
[ref_transonic]: https://en.wikipedia.org/wiki/Transonic
[ref_tu95lal]: https://en.wikipedia.org/wiki/Tupolev_Tu-95LAL
[ref_turbojet]: https://en.wikipedia.org/wiki/Turbojet
[ref_us_standard_atmosphere]: https://en.wikipedia.org/wiki/U.S._Standard_Atmosphere
[ref_wave_drag]: https://en.wikipedia.org/wiki/Wave_drag
[ref_wind_tunnel]: https://en.wikipedia.org/wiki/Wind_tunnel
[ref_wing_configuration]: https://en.wikipedia.org/wiki/Wing_configuration
[ref_wing_loading]: https://en.wikipedia.org/wiki/Wing_loading
[ref_wing_root]: https://en.wikipedia.org/wiki/Wing_root
[ref_yb60]: https://en.wikipedia.org/wiki/Convair_YB-60
[ref_yeager]: https://en.wikipedia.org/wiki/Chuck_Yeager
[ref_yield_strength]: https://en.wikipedia.org/wiki/Yield_(engineering)
[related_post_a106_two_stage_delta_wing]: {% post_url 2026-03-12-two_stage_flying_delta_wing_vehicles_for_civil_and_national_security_applications %}
[related_post_a217_rocket_propellant_chemistry]: {% post_url 2026-02-01-rocket_propellant_chemistry_a_design_tradeoff_space %}
[related_post_a237_aerospace_framing]: {% post_url 2026-07-13-framing_and_the_co_development_mechanism %}
[related_post_a241_aerospace_simulation]: {% post_url 2026-07-17-aerospace_simulation_and_real_time_systems %}
[related_post_a297_xplanes_framing]: {% post_url 2025-10-06-x_planes_framing %}
[related_post_a298_bell_x1]: {% post_url 2025-10-07-x_planes_bell_x1 %}
[related_post_a299_bell_x2]: {% post_url 2025-10-08-x_planes_bell_x2 %}
[related_post_a300_douglas_x3]: {% post_url 2025-10-09-x_planes_douglas_x3 %}
[related_post_a301_northrop_x4]: {% post_url 2025-10-10-x_planes_northrop_x4 %}
[related_post_a302_bell_x5]: {% post_url 2025-10-11-x_planes_bell_x5 %}
[related_post_a90_intro_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[related_post_a96_history_rocketplanes]: {% post_url 2026-02-27-history_of_rocketplanes %}
[research_abdussami_2025]: https://doi.org/10.1016/j.nucengdes.2025.114295
[research_aec_1950]: https://www.osti.gov/biblio/969642
[research_aec_1950_2]: https://www.osti.gov/biblio/129477
[research_aec_1957]: https://www.osti.gov/biblio/4155584
[research_aec_1957_2]: https://www.osti.gov/biblio/4781700
[research_aec_1957_3]: https://www.osti.gov/biblio/4792703
[research_aec_1959]: https://www.osti.gov/biblio/4643464
[research_aec_1959_2]: https://www.osti.gov/biblio/12393730
[research_aec_1959_3]: https://www.osti.gov/biblio/4581034
[research_aec_1959_4]: https://www.osti.gov/biblio/4142437
[research_aec_1961]: https://www.osti.gov/biblio/4095728
[research_ahmed_2026]: https://doi.org/10.1016/j.radphyschem.2025.113544
[research_alnuaimi_2026]: https://doi.org/10.1016/j.pnucene.2026.106467
[research_ancona_2025]: https://doi.org/10.1007/s42496-025-00281-5
[research_aueron_2024]: https://doi.org/10.2514/1.a35805
[research_bali_2025]: https://doi.org/10.1016/j.nucengdes.2025.113952
[research_beever_1965]: https://ntrs.nasa.gov/citations/19650025019
[research_bettis_1957]: https://www.osti.gov/biblio/4316237
[research_bhardwaj_2024]: https://doi.org/10.3389/fnuen.2024.1352667
[research_bigelow_1957]: https://www.osti.gov/biblio/4729439
[research_blizard_1953]: https://www.osti.gov/biblio/4107755
[research_buckingham_1914]: https://doi.org/10.1103/physrev.4.345
[research_cannon_1961]: https://www.osti.gov/biblio/4842854
[research_capo_1957]: https://www.osti.gov/biblio/4293076
[research_cavicchi_1959]: https://ntrs.nasa.gov/citations/19630010644
[research_cetegen_2025]: https://doi.org/10.1016/j.energy.2025.138469
[research_chaloner_verdinelli_1995]: https://doi.org/10.1214/ss/1177009939
[research_cheng_2025]: https://doi.org/10.1016/j.nucengdes.2025.114548
[research_comassar_1962]: https://www.osti.gov/biblio/1048126
[research_cottrell_1951]: https://www.osti.gov/biblio/4137126
[research_cottrell_1952]: https://www.osti.gov/biblio/4139314
[research_cottrell_1952_2]: https://www.osti.gov/biblio/4782915
[research_cottrell_1952_3]: https://www.osti.gov/biblio/4704625
[research_cottrell_1955_2]: https://www.osti.gov/biblio/4237975
[research_cottrell_1958]: https://www.osti.gov/biblio/4223435
[research_creasman_2024]: https://doi.org/10.1016/j.nucengdes.2023.112881
[research_deganahl_1954]: https://www.osti.gov/biblio/4704905
[research_dewitt_2024]: https://doi.org/10.1016/j.lssr.2024.02.005
[research_dibble_1958]: https://www.osti.gov/biblio/10202216
[research_domingos_2026]: https://doi.org/10.1016/j.nucengdes.2026.115072
[research_doyle_1948]: https://ntrs.nasa.gov/citations/20050019308
[research_doyle_1951]: https://ntrs.nasa.gov/citations/19930086702
[research_duan_2026]: https://doi.org/10.1016/j.jandt.2026.03.002
[research_dunkle_2026]: https://doi.org/10.12688/nuclscitechnolopenres.17459.2
[research_edwards_1954]: https://www.osti.gov/biblio/4801695
[research_edwards_1957]: https://www.osti.gov/biblio/4808209
[research_edwards_1958]: https://www.osti.gov/biblio/4326622
[research_edwards_1962]: https://www.osti.gov/biblio/4491615
[research_elkhawas_2025]: https://doi.org/10.1088/1402-4896/ae05d3
[research_finger_1962]: https://ntrs.nasa.gov/citations/19630007351
[research_fischer_2024]: https://doi.org/10.1016/j.nucengdes.2023.112768
[research_fraas_1954]: https://www.osti.gov/biblio/12772844
[research_frankfort_1956]: https://www.osti.gov/biblio/4271963
[research_fries_1958]: https://www.osti.gov/biblio/4300515
[research_gamertsfelder_1954]: https://www.osti.gov/biblio/4805552
[research_gasser_1947]: https://www.osti.gov/biblio/129218
[research_gates_1961]: https://ntrs.nasa.gov/citations/20150019696
[research_gedwill_1965]: https://ntrs.nasa.gov/citations/19730064642
[research_gilbertjr_1955]: https://www.osti.gov/biblio/1240148
[research_gorker_1955]: https://www.osti.gov/biblio/4822720
[research_gotsky_1959]: https://ntrs.nasa.gov/citations/19980228446
[research_guilbaud_2024]: https://doi.org/10.1016/j.nucengdes.2024.113639
[research_han_2025]: https://doi.org/10.1109/access.2025.3610902
[research_han_2025_2]: https://doi.org/10.1109/tns.2025.3558902
[research_hedden_1962]: https://www.osti.gov/biblio/4728141
[research_henry_1958]: https://www.osti.gov/biblio/4071097
[research_holcomb_2025]: https://doi.org/10.1016/j.nucengdes.2025.114303
[research_huang_2025]: https://doi.org/10.1016/j.pnucene.2025.105763
[research_humble_1950]: https://ntrs.nasa.gov/citations/19930086366
[research_islam_2025]: https://doi.org/10.1016/j.pnucene.2025.105741
[research_jagtap_2024]: https://doi.org/10.1016/j.ijhydene.2024.11.331
[research_johnson_1960]: https://www.osti.gov/biblio/5146009
[research_jordan_1957]: https://www.osti.gov/biblio/1373535
[research_kam_1961]: https://www.osti.gov/biblio/4532885
[research_khan_2025]: https://doi.org/10.1016/j.nucengdes.2025.114215
[research_kim_2026]: https://doi.org/10.1016/j.pnucene.2025.105989
[research_kress_1958]: https://www.osti.gov/biblio/4310182
[research_lan_2024]: https://doi.org/10.1016/j.nucengdes.2024.113647
[research_larson_1958]: https://www.osti.gov/biblio/12376890
[research_larson_1958_2]: https://www.osti.gov/biblio/12393299
[research_larson_1959]: https://www.osti.gov/biblio/1245002
[research_larson_1959_2]: https://www.osti.gov/biblio/12086630
[research_lee_1958]: https://www.osti.gov/biblio/1046040
[research_lee_2025]: https://doi.org/10.1016/j.pnucene.2025.105947
[research_level_1962]: https://www.osti.gov/biblio/12475098
[research_levine_1960]: https://www.osti.gov/biblio/4192956
[research_levine_1961]: https://www.osti.gov/biblio/4070513
[research_li_2024]: https://doi.org/10.37394/23202.2024.23.43
[research_lindley_1956]: https://doi.org/10.1214/aoms/1177728069
[research_liu_2026]: https://doi.org/10.1016/j.pnucene.2025.106098
[research_lu_2025]: https://doi.org/10.1016/j.eng.2025.12.013
[research_ma_2026]: https://doi.org/10.1016/j.energy.2026.141802
[research_magnuson_1956]: https://www.osti.gov/biblio/4361517
[research_matthia_2024]: https://doi.org/10.1029/2024sw004095
[research_mcfarlane_2024]: https://doi.org/10.3389/fnuen.2024.1335980
[research_meyer_1965]: https://www.osti.gov/biblio/1048071
[research_mishra_2024]: https://doi.org/10.1016/j.dib.2023.109817
[research_mitchell_1954]: https://www.osti.gov/biblio/4817598
[research_mochizuki_2024]: https://doi.org/10.1016/j.nucengdes.2024.113472
[research_mochizuki_2026]: https://doi.org/10.1016/j.nucengdes.2025.114706
[research_moteff_1960]: https://www.osti.gov/biblio/4551077
[research_na_1957]: https://www.osti.gov/biblio/1232654
[research_naca_1962]: https://ntrs.nasa.gov/citations/19740074600
[research_naca_1963]: https://ntrs.nasa.gov/citations/19660014551
[research_nance_1957]: https://www.osti.gov/biblio/4347121
[research_niu_2024]: https://doi.org/10.1016/j.seppur.2024.127424
[research_nyquist_1928]: https://doi.org/10.1109/T-AIEE.1928.5055024
[research_ogul_2026]: https://doi.org/10.1016/j.radphyschem.2025.113419
[research_parisi_2026]: https://doi.org/10.1080/00295450.2026.2678096
[research_peng_2024]: https://doi.org/10.1016/j.est.2024.112714
[research_perry_1958]: https://www.osti.gov/biblio/993074
[research_phelps_1961]: https://www.osti.gov/biblio/946508
[research_rangel_2026]: https://doi.org/10.1016/j.nucengdes.2026.114923
[research_reetz_1965]: https://ntrs.nasa.gov/citations/19650024974
[research_ross_1960]: https://www.osti.gov/biblio/4080402
[research_ruffman_1952]: https://www.osti.gov/biblio/1015812
[research_sasi_2025]: https://doi.org/10.1115/1.4066433
[research_savage_1958]: https://www.osti.gov/biblio/4308571
[research_savolainen_1954]: https://www.osti.gov/biblio/4121762
[research_schaeffer_1958]: https://www.osti.gov/biblio/4276461
[research_schmickrath_1960]: https://www.osti.gov/biblio/12377075
[research_sekkat_2026]: https://doi.org/10.1016/j.apradiso.2026.112793
[research_shannon_1948]: https://doi.org/10.1002/j.1538-7305.1948.tb01338.x
[research_shobeiri_2025]: https://doi.org/10.3390/su17083406
[research_shoults_1958]: https://www.osti.gov/biblio/4315621
[research_stever_1948]: https://www.osti.gov/biblio/969767
[research_stever_1948_2]: https://www.osti.gov/biblio/1471204
[research_stone_2024]: https://doi.org/10.1016/j.matdes.2023.112463
[research_sun_2025]: https://doi.org/10.1016/j.jandt.2025.04.006
[research_thornton_1961]: https://www.osti.gov/biblio/4120083
[research_troubetzkoy_1961]: https://www.osti.gov/biblio/4517145
[research_wahler_2025]: https://doi.org/10.3390/aerospace12020077
[research_welch_1961]: https://www.osti.gov/biblio/4813232
[research_williams_drake_1948]: https://ntrs.nasa.gov/citations/19650070849
[research_woodbridge_1955]: https://www.osti.gov/biblio/4813340
[research_woodsum_1957]: https://www.osti.gov/biblio/991705
[research_yildirim_2026]: https://doi.org/10.1016/j.asr.2026.05.076
[research_yilmaz_2025]: https://doi.org/10.1016/j.pnucene.2025.105614
[research_zhang_2026]: https://doi.org/10.1016/j.est.2025.119987
