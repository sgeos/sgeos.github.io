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

The first of those follows from the energy released per fission event and the mass of the nucleus that supplies it,

$$E_f \approx 200 \ \text{MeV} = 3.20 \times 10^{-11} \ \text{joules}, \qquad E_{\text{fission}} = \frac{E_f \, N_A}{M_{235}}$$

gives a ratio of

$$\frac{E_{\text{fission}}}{E_{\text{chem}}} = 1.9 \times 10^{6}$$

The rate at which a reactor must consume nuclei to hold a given power follows immediately,

$$\dot{N}_f = \frac{P}{E_f}$$

so a hundred megawatt core is fissioning

$$\dot{N}_f = \frac{10^{8}}{3.20 \times 10^{-11}} = 3.12 \times 10^{18} \ \text{nuclei per second}$$

and that number, rather than the power, is what determines everything difficult about the aircraft, because each of those events emits radiation as well as heat.

A strategic bomber of the period consumed fuel by the tens of tonnes. The same energy delivered by fission is measured in grams. The figure of merit that governs a conventional bomber collapses. Endurance for a fuel-burning aircraft is the fuel divided by the flow required, which is the thrust-specific fuel consumption, abbreviated TSFC, multiplied by the thrust,

$$t_{\text{endurance}} = \frac{m_{\text{fuel}}}{\text{TSFC} \times F}$$

and for a nuclear aircraft that consumption is not small but effectively zero,

$$\text{TSFC} = \frac{\dot{m}_{\text{fuel}}}{F} \longrightarrow 0 \quad \Longrightarrow \quad t_{\text{endurance}} \longrightarrow \text{limited by something else}$$

**The quantity that had bounded every bomber ever built stops bounding anything, and the binding constraint moves to the crew, the lubricating oil, and the reactor.** The mission this bought was a bomber that could remain airborne for days or weeks, holding a target at risk continuously rather than surging to reach it, and in 1946 that was an argument nobody in the Air Force needed persuading of. The [Army Air Forces began a project on Nuclear Energy for the Propulsion of Aircraft][research_gasser_1947] in May of that year, abbreviated NEPA.

The objection is equally easy to state. A reactor at power is an intense source of gamma rays and neutrons, and the crew must survive the flight. Shielding is dense material, dense material is heavy, and the aircraft must carry all of it all of the time. The keystone is therefore not whether a reactor can produce the thrust, which was never seriously in doubt, but whether what must be wrapped around it leaves an aircraft worth building.

A second constraint enters through the same door and deserves stating early. A reactor sustains itself when the neutron population reproduces, which is the criticality condition

$$k_{\text{eff}} = \frac{\text{production}}{\text{absorption} + \text{leakage}} = 1$$

and leakage grows as a core is made small. For a bare core the non-leakage probability is approximately

$$P_{\text{NL}} \approx \frac{1}{1 + B^{2} M^{2}}, \qquad B^{2} = \left( \frac{\pi}{R} \right)^{2} \ \text{for a sphere}$$

with $M^2$ the migration area. **An aircraft reactor must be compact, compact cores leak, and leaked neutrons must be paid for with enrichment or with a reflector.** Every aircraft reactor in this programme therefore used highly enriched fuel, which is a proliferation fact as well as an engineering one, with no counterpart in any other aircraft in this series.

That framing was understood at the outset. The [Lexington Project][research_stever_1948] convened at the Massachusetts Institute of Technology in 1948 to assess feasibility, and its verdict, that the thing was possible but would take fifteen years and a great deal of money, turned out to be very nearly exactly right in duration and wrong only in supposing that the endpoint would be reached. The study was thorough in a way its one-line summary conceals. It produced numbered reports on [aircraft][research_redding_1948] and on [aircraft configuration][research_hobbs_1948], recorded [a meeting with Boeing][research_klein_1948], assessed something as specific as [the tolerance of aerial reconnaissance film to nuclear radiation][research_goodman_1948], and was indexed well enough that [the index survives][research_aec_1948] as a document in its own right. **It also established the comparison baseline**, since [Shoults 1948][research_shoults_1948] examined the ability of chemically propelled aircraft to complete the same missions, which is the question that eventually killed the programme and which was therefore asked at the beginning and answered wrongly. The analysis of the mission case ran alongside, including [studies of nuclear aircraft for antisubmarine warfare][research_aec_1950] where endurance rather than speed is the whole of the requirement, and [the performance parameters that would govern any such aircraft][research_ruffman_1952]. Configuration studies followed in quantity. [Hutton 1952][research_hutton_1952] compares fourteen nuclear-powered airplanes against one another, which is the kind of document that exists only when a subject has passed from speculation into engineering.

## Programme Origin

The institutional history is a sequence of transfers, and each transfer is a symptom.

Project NEPA began on 28 May 1946 under the Army Air Forces, funded at ten million dollars in 1947, and ran as a study effort until May 1951. It was then replaced by the joint Atomic Energy Commission and Air Force programme called Aircraft Nuclear Propulsion, abbreviated ANP. The [quarterly progress reports][research_cottrell_1951] begin in that period and continue, in an unbroken series, for a decade. The programme pursued two propulsion architectures in parallel, which is the first sign that nobody was confident which would work.

The [direct air cycle][research_shoults_1958] was assigned to General Electric at Evendale, Ohio. It is a turbojet with the combustor replaced by a reactor core. Air leaves the compressor, passes through the core, is heated by fission, and expands through the turbine. It is mechanically simple and thermodynamically direct, and it has the property that the working fluid passes through the reactor and comes out radioactive.

The indirect cycle went to Pratt and Whitney at Middletown, Connecticut. A liquid metal or molten salt loop carries heat from the core to a [heat exchanger][ref_heat_exchanger], and the air is heated there without ever entering the core. It is cleaner and it costs a temperature drop across the exchanger, an entire secondary loop with pumps and radiators, and the mass of all of it. The [circulating fuel reflector-moderator reactor][research_bigelow_1957] was its central concept.

Under project MX-1589 Convair was to modify two B-36 airframes. One would carry a reactor to measure shielding, and one would become the X-6. The [B-36][ref_b36] was chosen for the reason that governs this entire article, which is that it was the largest aircraft available. Its gross mass of about 186,000 kilograms over a wing of 443 square metres gives

$$\frac{W}{S} = \frac{186{,}000 \times 9.80665}{443} = 4.12 \times 10^{3} \ \text{newtons per square metre}$$

at an aspect ratio of

$$A = \frac{b^{2}}{S} = \frac{70.1^{2}}{443} = 11.1$$

which is a high-aspect-ratio, lightly loaded aeroplane built for endurance, and therefore the right starting point for a mission defined by staying airborne. Follow-on aircraft would have used the swept-wing [YB-60][ref_yb60]. The X-6 itself would have been powered by General Electric X-40 engines, which were [J47][ref_j47] derivatives adapted to nuclear heating, drawing on a P-1 reactor.

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

A reactor at power produces prompt fission gammas, fission product decay gammas, and fast neutrons, all in quantities proportional to the fission rate and therefore to the power. Taking about eight of the two hundred megaelectronvolts per fission as escaping gamma energy,

$$P_\gamma \approx 0.04 \, P = 4.0 \ \text{megawatts}$$

which at a mean photon energy near one megaelectronvolt is a source strength of

$$S_\gamma = \frac{P_\gamma}{\bar{E}_\gamma} = \frac{4.0 \times 10^{6}}{1.60 \times 10^{-13}} = 2.50 \times 10^{19} \ \text{photons per second}$$

and the neutron source follows from the yield per fission,

$$S_n = \nu \, \dot{N}_f = 2.4 \times 3.12 \times 10^{18} = 7.49 \times 10^{18} \ \text{neutrons per second}$$

Both scale linearly with the power, which is the fact the next two sections turn on.

The dose rate at distance $r$ from a shielded source is governed by an exponential attenuation with a buildup correction,

$$\dot{D}(r, x) = \frac{k \, P}{4 \pi r^{2}} \, B(\mu x) \, e^{-\mu x}$$

in which $x$ is the shield thickness, $\mu$ the linear attenuation coefficient of the shield material, and $B$ the buildup factor accounting for photons that scatter into the beam rather than being removed from it. That factor is not a fudge but a computed quantity. [Auslender 1957][research_auslender_1957] obtains it for layered configurations by Monte Carlo, which is the method still used. The corresponding neutron quantity is the effective removal cross-section tabulated by [Chapman 1955][research_chapman_1955], and the fast-neutron spectrum and dose-rate calculations that convert a flux into a dose are [Eggen 1961][research_eggen_1961]. **Every coefficient this article uses was measured or computed under this programme or its immediate neighbours.** Both quantities remain active research subjects rather than settled constants. Buildup factors are still being computed to greater depth and by new methods, with [Sun et al 2025][research_sun_2025_2] carrying Monte Carlo evaluation to a hundred mean free paths, [Kang and Zu 2026][research_kang_2026] and [Yang et al 2026][research_yang_2026] replacing the tabulations with learned models, and [Hashim et al 2026][research_hashim_2026] treating the multilayer case this article's divided shield requires. The neutron side is [Soliman 2025][research_soliman_2025], whose subject is the energy dependence of the removal cross-section, which is the approximation the single-value treatment above hides. Cross-section generation as a computational discipline is [Jiaju et al 2025][research_jiaju_2025]. The factor $k$ collects the source spectrum and the conversion from fluence to dose.

Two features of that expression govern everything. The distance term is a power law and the shield term is an exponential, and an exponential wins every argument it is in.

It is worth establishing what is being attenuated from, because the figure decides the shield. Unshielded at ten metres the photon fluence rate is

$$\varphi = \frac{S_\gamma}{4 \pi r^{2}} = \frac{2.50 \times 10^{19}}{4 \pi \times 100} = 1.99 \times 10^{16} \ \text{per square metre per second}$$

and the dose rate follows from the energy fluence and the mass energy-absorption coefficient of tissue,

$$\dot{D} = \varphi \, \bar{E}_\gamma \left( \frac{\mu_{en}}{\rho} \right)_{\text{tissue}} = 1.99 \times 10^{16} \times 1.60 \times 10^{-13} \times 3.09 \times 10^{-3}$$

$$\dot{D} = 9.8 \ \text{grays per second}$$

**Ten grays per second, when about five grays is a lethal whole-body dose.** One second of exposure at ten metres from an unshielded hundred megawatt core kills the crew. That is the number the shield must reduce, and stating it makes clear why the programme could not economize.

Solving for the thickness required to hold the dose at a limit $\dot{D}_0$,

$$x = \frac{1}{\mu} \ln \left( \frac{k \, P \, B}{4 \pi r^{2} \dot{D}_0} \right)$$

For [lead][ref_lead_element] at photon energies around one megaelectronvolt the mass [attenuation coefficient][ref_attenuation] is about 0.070 square centimetres per gram, so with a density of 11.34 grams per cubic centimetre,

$$\mu = 0.070 \times 11.34 = 0.794 \ \text{per centimetre}$$

giving a tenth-value layer of

$$x_{1/10} = \frac{\ln 10}{\mu} = \frac{2.303}{0.794} = 2.90 \ \text{centimetres}$$

so every 2.9 centimetres of lead removes ninety percent of what reaches it.

The attenuation demanded follows from the mission rather than from taste. Allowing the crew fifty millisieverts over a hundred-hour flight sets a rate limit of

$$\dot{D}_0 = \frac{0.05}{100} = 5 \times 10^{-4} \ \text{grays per hour}$$

against an unshielded rate of $3.54 \times 10^{4}$ grays per hour, so

$$\mathcal{A} = \frac{\dot{D}_{\text{unshielded}}}{\dot{D}_0} = \frac{3.54 \times 10^{4}}{5 \times 10^{-4}} = 7.1 \times 10^{7}$$

and with a buildup factor of ten the thickness is

$$x = \frac{\ln \left( \mathcal{A} B \right)}{\mu} = \frac{\ln \left( 7.1 \times 10^{8} \right)}{0.794} = \frac{20.4}{0.794} = 25.7 \ \text{centimetres}$$

**Twenty-six centimetres of lead, and that is the gamma shield alone.** That is the number the programme spent fifteen years trying to reduce.

Neutrons need a different material and are attenuated by a removal cross-section rather than by a photon coefficient,

$$\varphi_n(x) = \varphi_n(0) \, e^{-\Sigma_R x}$$

with $\Sigma_R$ near 0.095 per centimetre for [lithium hydride][ref_lih], which is the aircraft shield material of choice because it supplies hydrogen at low density and captures the moderated neutrons in lithium without emitting a penetrating capture gamma. [Waldrop 1958][research_waldrop_1958] treats it explicitly as a mobile neutron shield, which is the aircraft requirement stated as a material specification, and specimens were irradiated and tested, with [two of the test series][research_lee_1958_2] documented [separately][research_reagan_1958]. The hydride family more broadly is surveyed in [Cernak 1960][research_cernak_1960_2]. For comparison the heavy alternative, structural concrete, is characterized by [Blizard 1958][research_blizard_1958], and its unsuitability for an aircraft is a matter of density rather than of physics. The unshielded fast neutron dose rate at ten metres works out to some $7.5 \times 10^{5}$ sieverts per hour, so the attenuation required is $1.5 \times 10^{9}$ and

$$x_n = \frac{\ln \left( 1.5 \times 10^{9} \right)}{0.095} = 222 \ \text{centimetres}$$

**Two and a quarter metres of lithium hydride.** The two shields are not simply additive, since lead scatters neutrons inelastically and lithium hydride attenuates photons, so a layered design achieves both requirements in less material than the sum. The sum is nevertheless the honest upper bound, and the true figure lies between the lead alone and the two together.

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

$$m_{\text{shield}} = \rho_s A x = 11{,}340 \times 14.1 \times 0.257 = 4.12 \times 10^{4} \ \text{kilograms}$$

or 41 tonnes of lead, which against a gross weight of 186 tonnes is

$$\frac{m_{\text{shield}}}{m_{\text{gross}}} = \frac{41{,}200}{186{,}000} = 0.221$$

**Twenty-two percent of the aircraft is gamma shielding**, and adding the neutron layer computed above takes the upper bound to

$$\frac{m_{\text{Pb}} + m_{\text{LiH}}}{m_{\text{gross}}} = \frac{41{,}200 + 24{,}500}{186{,}000} = 0.353$$

The comparison that matters is not with the gross weight but with the payload, since a B-36 carried a maximum bomb load of about 39,000 kilograms,

$$\frac{m_{\text{shield}}}{m_{\text{payload}}} = \frac{41{,}200}{39{,}000} = 1.06$$

**The gamma shield alone weighs slightly more than the entire bomb load, and the full shield weighs about 1.7 times it.** A nuclear bomber buys unlimited range by giving up the payload that made the range worth having, and that sentence is the programme in one line. The trade is not fatal in principle, since a larger aircraft dilutes a fixed shield mass, and this is exactly why the design kept growing and why the follow-on was to be the larger YB-60. It is fatal in practice because the aircraft that dilutes the shield adequately is one nobody wanted to buy.

This was understood at the time. [Shield optimization][research_blizard_1953] was a named research subject with its own literature by 1953, [shield weights][research_woodsum_1957] were tracked as a programme metric, and the effect of the shield on the centre of gravity was itself a design problem serious enough to warrant [its own study][research_phelps_1961]. Shield synthesis was pushed to the point of [formal minimum-weight optimization][research_troubetzkoy_1961], and the computational tools were built in-house, with [shield analysis programs][research_capo_1957] and [their successors][research_edwards_1958] developed specifically for the task.

### Divided Shielding and the Trick That Was Not Enough

The shield mass above assumes shielding the reactor. There is a cheaper arrangement and the programme used it.

A **divided shield** puts part of the material at the reactor and part around the crew. The reactor shield need only cover the solid angle subtended by the crew compartment, and the crew shield handles radiation that reaches the crew by other paths, principally scattering from the air itself. Writing the total as a sum,

$$m_{\text{total}} = \rho_s A_r x_r + \rho_c A_c x_c$$

subject to the constraint that the direct and scattered contributions together meet the dose limit,

$$\dot{D}_{\text{direct}} \left( x_r \right) + \dot{D}_{\text{scatter}} \left( x_r, x_c \right) \le \dot{D}_0$$

the optimum divides the material between the two according to the relative areas. Forming the Lagrangian and differentiating with respect to each thickness gives the condition that the marginal dose reduction per unit mass be equal in both shields,

$$\frac{1}{\rho_s A_r} \frac{\partial \dot{D}}{\partial x_r} = \frac{1}{\rho_c A_c} \frac{\partial \dot{D}}{\partial x_c}$$

and because each partial derivative carries its own exponential, the condition reduces to a relation between the two thicknesses and the ratio of areal masses,

$$\mu_r x_r - \mu_c x_c = \ln \left( \frac{\rho_c A_c \, \mu_r}{\rho_s A_r \, \mu_c} \right)$$

Because the reactor shadow shield can be small in area while the crew compartment shield must wrap a larger volume, the division is not obvious in advance. This is the calculation [Blizard 1953][research_blizard_1953] set out and that the [supercritical water reactor shield design procedure][research_deganahl_1954] and the [AC-series power plant shield calculations][research_mitchell_1954] applied to particular configurations. Solving it for a real layered geometry required machinery, and the programme built it, with [an IBM 704 shielding program][research_haffner_1958] and [a multilayer gamma flux code][research_bendall_1959] among the results. The supporting measurements are extensive, covering [centreline dose rates from source planes of different area][research_casper_1958], [gamma heating within a shield][research_duncan_1958], [the nuclear and physical properties of a graphite reactor shield][research_blosser_1958], and [duct penetration experiments at the Convair ground test reactor][research_haffner_1956], the last of which addresses the problem every real shield has, which is that pipes and cables must pass through it. A comparable ground installation is treated in [Meem 1956][research_meem_1956].

The scattered term is the reason the trick has a floor. Radiation that leaves the reactor in any direction can scatter off the surrounding air and arrive at the crew from outside the shadow, an effect that grows with air density and therefore falls with altitude, which is why [the effect of altitude and flight speed on shielding requirements][research_edwards_1954] was a subject in its own right. The scattered contribution can be written in the same form as the direct one but with the air acting as the scattering medium, so that it scales with the density along the path,

$$\dot{D}_{\text{scatter}} \propto \rho_{\text{air}}(h) \, \frac{S_\gamma}{4 \pi r^{2}} \, f_{\text{geom}}$$

and the atmosphere thins exponentially with altitude,

$$\rho_{\text{air}}(h) = \rho_0 \, e^{-h / H}, \qquad H \approx 8.4 \ \text{kilometres}$$

so climbing from sea level to twelve kilometres reduces the scattered term by

$$\frac{\rho(12{,}000)}{\rho_0} = e^{-12/8.4} = 0.24$$

A shadow shield alone is insufficient in an atmosphere. **The aircraft must fly high to make its own shielding lighter, which is a coupling between the flight condition and the structural mass that no conventional aircraft has**, and it means the shield cannot be sized without first choosing the cruise altitude.

Material choice attacked the same problem from the other end. Gamma attenuation wants high atomic number and density, and neutron attenuation wants hydrogen. [Lithium hydride][ref_lih] supplies hydrogen at low density and captures neutrons in the lithium without producing a penetrating capture gamma, which makes it very nearly the ideal aircraft neutron shield, and [its properties were characterized in detail][research_welch_1961] under the programme. The [investigation of metallic hydrides as moderators, reflectors, and shields][research_gilbertjr_1955] pursued the same family.

## Dependent Systems

### The Direct Cycle and What It Does to the Air

Passing the working fluid through the core is simple and it has a consequence.

The thrust of a turbojet follows from the momentum change,

$$F = \dot{m} \left( V_e - V_0 \right), \qquad V_e = \sqrt{2 c_p T_4 \left[ 1 - \left( \frac{p_0}{p_4} \right)^{\frac{\gamma - 1}{\gamma}} \right]}$$

and the heat the reactor must add to reach turbine inlet temperature $T_4$ from compressor discharge temperature $T_3$ is

$$P_{\text{thermal}} = \dot{m} \, c_p \left( T_4 - T_3 \right)$$

The cycle behind them is a Brayton cycle whose thermal efficiency depends on the compressor pressure ratio alone in the ideal case,

$$\eta_{\text{th}} = 1 - \left( \frac{1}{\pi_c} \right)^{\frac{\gamma - 1}{\gamma}}, \qquad T_3 = T_2 \, \pi_c^{\frac{\gamma - 1}{\gamma}}$$

Nothing in either relation cares where the heat came from. The reactor is a heat source with a temperature limit, exactly as a combustor is, and the design problem is to get $T_4$ as high as the turbine will tolerate.

That is where the difficulty lies. A combustor reaches flame temperatures far above what the turbine can take and the design problem is dilution. **A reactor must reach turbine inlet temperature in its own fuel elements, which must therefore run hotter than the air they are heating.** The margin needed follows from the convective heat transfer at the element surface,

$$q'' = h \left( T_w - T_{\text{air}} \right), \qquad \mathrm{Nu} = \frac{h D_h}{k} = 0.023 \, \mathrm{Re}^{0.8} \mathrm{Pr}^{0.4}$$

and the total surface the core must present follows from the power and the achievable flux,

$$A_{\text{fuel}} = \frac{P_{\text{thermal}}}{q''}$$

so a core transferring a hundred megawatts at a megawatt per square metre needs a hundred square metres of heated surface packed into something like a cubic metre, which is a power density of

$$\frac{P}{V} \approx 100 \ \text{megawatts per cubic metre}$$

That is an order of magnitude above a contemporary power reactor, and it is demanded by an aircraft's intolerance for volume. For a 1950s turbine tolerating something like 1150 kelvin at inlet, the fuel element surface must exceed that, and a fuel element at that temperature in a fast air stream is a materials problem of the first order. An entire literature was built on it, from [metallic fuel element materials][research_level_1962] through [high-temperature work reported at the ANP materials meetings][research_aec_1959_3]. Element development ran continuously, with [Conway 1956][research_conway_1956], [Butterfield 1956][research_butterfield_1956], [Conn 1957][research_conn_1957], and the shaped-wire study of [Tribus 1955][research_tribus_1955] representing the range of approaches tried. Inspection became its own discipline in [Marjon 1957][research_marjon_1957], measuring the element temperature required [thermocouples that would survive the environment][research_kuhlman_1957], and the cladding alloys are [Collins 1960][research_collins_1960]. **The fuel element is where an aircraft reactor differs most from a power reactor**, because it must be light, must run hotter, and must present a hundred square metres of surface to a fast air stream without shedding any of itself into the exhaust. What it does shed is the subject of [Wilks 1959][research_wilks_1959].

The modern answer to that problem is to encapsulate the fuel rather than to clad it, and the coated particle is where high-temperature reactor fuel went. [Zheng et al 2026][research_zheng_2026] compute the interaction between such particles and the matrix holding them, [Liu and Liu 2025][research_liu_2025_2] and [Poschmann et al 2025][research_poschmann_2025] model their performance including the departures from sphericity that real manufacture produces, and the coupled irradiated thermal and mechanical behaviour of the elements is [Peng et al 2025][research_peng_2025], with the transmutation products that change the properties over life in [Paul et al 2025][research_paul_2025] and the multi-scale coupling problem in [Zhang et al 2026][research_zhang_2026_2]. Gas-cooled cores of the kind the programme also examined continue in [Chong and Sagara 2026][research_chong_2026] and [Owston 2025][research_owston_2025].

Pushing air through that core costs pressure, and pressure lost between compressor and turbine is thrust not produced. The core acts as a duct with friction,

$$\frac{\Delta p}{p} = f \frac{L}{D_h} \frac{\rho V^{2}}{2 p}$$

and the fractional thrust penalty follows the fractional pressure loss closely for a turbojet, so a five percent core pressure drop is roughly a five percent thrust penalty on top of everything else. The programme measured this instead of estimating it. [Segaser 1948][research_segaser_1948] determines pressure drop factors through typical fuel element channels, which is among the earliest documents in the whole record. [Chandler 1957][research_chandler_1957] finds that surface oxidation of the elements increases the loss, which is a degradation mechanism with no combustor analogue. The temperature rise of the fluid passing the elements is computed by [Woods 1954][research_woods_1954]. **A combustor adds heat at nearly constant pressure because it is an open volume. A reactor core is a heat exchanger and behaves like one.**

The air itself becomes radioactive. Natural argon is 0.93 percent of the atmosphere and argon-40 captures a neutron to become [argon-41][ref_argon41], a gamma emitter with a 110 minute half-life. The activity produced scales with the neutron flux, the residence time, and the mass flow,

$$A_{41} = \sigma_c \, \phi \, N_{40} \left( 1 - e^{-\lambda t_{\text{res}}} \right)$$

so a direct-cycle aircraft trails a plume of activated air behind it continuously. The programme studied this and treated it as tolerable in flight, which by the standards of the period it was, and which by any later standard it was not. It also means that a fuel element failure releases fission products directly into the exhaust, which is a different and much less tolerable proposition. The [nuclear aircraft safety analysis programme][research_aec_1957_3] existed to bound exactly these questions, and the specific case of a crash is [Menegus 1958][research_menegus_1958], which computes the accidental dispersion of reactor materials and the distance that must be controlled around it. **That calculation has no counterpart in any other aircraft in this series**, because no other aircraft in this series could contaminate the ground it fell on. Aerospace nuclear safety as a discipline is [Connor 1960][research_connor_1960], and the reactor community's own accident literature, including [a maximum credible accident analysis][research_dopchie_1958] and [an account of a zero power reactor accident][research_savic_1959], supplied the methods.

The [direct cycle nuclear turbojet was tested][research_shoults_1958], which is the fact that matters most in this section. The Heat Transfer Reactor Experiments at the Idaho site ran a reactor coupled to a turbojet on the ground and produced thrust from fission. HTRE-1, HTRE-2, and HTRE-3 form the series, with the [hazards analysis][research_gamertsfelder_1954] preceding them and [the operation manuals][research_woodbridge_1955] describing the assembly. **The programme reached the point of a working nuclear turbojet on a test stand.** [Thornton and Blumberg 1961][research_thornton_1961] report that the HTREs fulfilled their test goals, in a paper published the year the programme was cancelled.

They also had an accident. The [HTRE No. 3 nuclear excursion][research_aec_1959_2] has its own summary report, and its existence is a reminder that this was a reactor programme with reactor risks conducted at aircraft schedules.

### The Indirect Cycle and What It Costs

Keeping the air out of the core costs a temperature drop and a great deal of hardware.

An intermediate loop introduces a heat exchanger between the reactor and the air, and a heat exchanger of effectiveness $\varepsilon$ delivers

$$T_{4} = T_3 + \varepsilon \left( T_{\text{reactor}} - T_3 \right)$$

so the reactor must run hotter than the turbine inlet by the amount the exchanger cannot recover,

$$T_{\text{reactor}} - T_4 = \left( 1 - \varepsilon \right) \left( T_{\text{reactor}} - T_3 \right)$$

Effectiveness is itself bought with surface area, through the number of transfer units,

$$\mathrm{NTU} = \frac{U A_{\text{HX}}}{\left( \dot{m} c_p \right)_{\min}}, \qquad \varepsilon = 1 - e^{-\mathrm{NTU}} \ \text{for a large capacity ratio}$$

so that pushing effectiveness from 0.9 to 0.95 nearly doubles the required area,

$$\mathrm{NTU} = -\ln \left( 1 - \varepsilon \right) : \quad 2.30 \longrightarrow 3.00$$

An effectiveness of 0.9 with a compressor discharge at 600 kelvin and a required turbine inlet of 1150 kelvin demands a reactor outlet of

$$T_{\text{reactor}} = T_3 + \frac{T_4 - T_3}{\varepsilon} = 600 + \frac{550}{0.9} = 1211 \ \text{kelvin}$$

which is sixty kelvin hotter than the direct cycle needs, and the exchanger mass is added on top. The mass penalty of a heat exchanger scales with the heat transferred and inversely with the temperature difference driving it,

$$m_{\text{HX}} \propto \frac{P_{\text{thermal}}}{U \, \Delta T_{\text{lm}}}$$

so demanding high effectiveness, which means small $\Delta T$, makes the exchanger large exactly when the mass budget is already spent. The loop that feeds it costs power of its own,

$$P_{\text{pump}} = \frac{\dot{m}_{\text{coolant}} \, \Delta p_{\text{loop}}}{\rho_{\text{coolant}} \, \eta_{\text{pump}}}$$

which for a liquid metal at aircraft flow rates is not negligible and which must be supplied from the same reactor, reducing the thrust available by the amount it consumes. The [Pratt and Whitney circulating fuel reflector-moderator reactor][research_bigelow_1957], whose [first volume][research_bigelow_1957_2] sets out the design, and the [lithium-cooled reactor experiment][research_hedden_1962] represent the state that programme reached, which never approached flight hardware. The critical mass and power relationship for a reflector-moderated sodium-cooled configuration is [Merriman 1955][research_merriman_1955].

The cycle space was searched more widely than the two named architectures suggest. [Schwartz 1952][research_schwartz_1952] analyses inert gas cooled reactors for supersonic application, [Schwartz 1953][research_schwartz_1953] investigates a sodium vapour compressor jet, [Alvis 1957][research_alvis_1957] examines a gas generator and free turbine arrangement, and the ramjet variants appear in [Boppart 1957][research_boppart_1957] and [Szekely 1961][research_szekely_1961], with the radiator such a vehicle needs in [Larson 1958][research_larson_1958_3]. A direct-cycle steam-cooled reactor was even examined for merchant ships in [Falkenberry 1959][research_falkenberry_1959], which shows how far the architecture was carried once it existed. Weights, dimensions, and radiation patterns for a specific installation are [Gaffin 1959][research_gaffin_1959]. The engine performance studies are extensive, with [reactor, shield and performance data for a nuclear turbojet][research_larson_1958], [powerplant performance for a supersonic nuclear turbojet][research_larson_1958_2], [advanced characteristics for supersonic aircraft][research_larson_1959], and [nuclear JT-11 turbojet performance][research_larson_1959_2] all by the same author, alongside the [ANP powerplant data compilation][research_meyer_1965] that closes the series.

The NACA contribution sits here. [Humble et al 1950][research_humble_1950] give a preliminary analysis of three cycles for nuclear aircraft propulsion, [Doyle 1951][research_doyle_1951] and [Doyle 1948][research_doyle_1948] work a mercury-vapour intermediate cycle, and [Cavicchi et al 1959][research_cavicchi_1959] design a subsonic nuclear logistic aircraft around a helium-cooled reactor. The state of the art was summarized by [Finger and Rom 1962][research_finger_1962] and in the [proceedings of the nuclear propulsion conference][research_naca_1962] the same year, by which point the subject had already moved to space.

### Decay Heat, and Why the Aircraft Cannot Be Parked

Shutting down a reactor stops the fission but not the heat.

Fission products continue to decay after shutdown, and the thermal power follows an empirical law of the Way-Wigner form,

$$\frac{P_{\text{decay}}(t)}{P_0} \approx 0.066 \, t^{-0.2}$$

with $t$ in seconds after shutdown. Evaluating for a hundred megawatt core,

$$P_{\text{decay}}(1 \ \text{s}) = 6.6 \ \text{MW}, \qquad P_{\text{decay}}(1 \ \text{h}) = 1.28 \ \text{MW}, \qquad P_{\text{decay}}(1 \ \text{day}) = 0.68 \ \text{MW}$$

**An hour after landing the reactor is still producing more than a megawatt.** What that means if the cooling stops can be written down directly. With no heat removal the core heats adiabatically,

$$\frac{dT}{dt} = \frac{P_{\text{decay}}(t)}{m_{\text{core}} \, c_{p,\text{core}}}$$

and for a five tonne core of specific heat 500 joules per kilogram kelvin at the one-hour decay power,

$$\frac{dT}{dt} = \frac{1.28 \times 10^{6}}{5000 \times 500} = 0.51 \ \text{kelvin per second}$$

or 31 kelvin per minute, so a core sitting at 1000 kelvin reaches a melting point near 1700 in

$$t_{\text{melt}} \approx \frac{700}{0.51} = 1.4 \times 10^{3} \ \text{seconds} = 23 \ \text{minutes}$$

**Twenty-three minutes from a cooling failure to a melted core, an hour after the aircraft has landed.** In a direct-cycle aircraft the cooling medium is the air flowing through the engines, so the airflow must be maintained on the ground, after shutdown, indefinitely, or the core melts. A nuclear aircraft cannot simply be parked. It requires ground equipment to sustain core cooling, and the mass of heat that must go somewhere is comparable to a large industrial furnace running continuously in a hangar.

The time integral makes the point sharper. Total energy released after shutdown up to time $T$ is

$$E_{\text{decay}} = \int_0^{T} 0.066 \, P_0 \, t^{-0.2} \, dt = \frac{0.066 \, P_0}{0.8} T^{0.8}$$

which for a day comes to 73 gigajoules, an average of 850 kilowatts sustained around the clock. That is an operational burden with no analogue in any other aircraft in this series, and it is a burden that exists whether or not the aircraft ever flies again. [Reactor coolant flow optimization for the Aircraft Shield Test Reactor][research_ross_1960] is the programme's version of this problem, and the modern treatments of [decay heat removal][research_bali_2025] and [long-term cooling during transients][research_mochizuki_2026] show it never went away.

### Radiation and the Aircraft Itself

The crew is not the only thing that must survive the reactor.

Dose accumulates in materials as well as people, and the failure modes differ. Organic materials cross-link or embrittle, semiconductors accumulate lattice damage and charge, and lubricants polymerize. The accumulated dose at a component is the integral of the local rate over the mission,

$$D_{\text{component}} = \int_0^{t_{\text{mission}}} \dot{D}(\mathbf{r}, t) \, dt$$

The damage mechanism in a solid is displacement rather than ionization, and it is measured in displacements per atom accumulated over the fluence,

$$\text{dpa} = \sigma_d \int_0^{t} \varphi_n \, dt = \sigma_d \, \Phi_n$$

so a component's life is set by a fluence limit rather than by a dose rate,

$$t_{\text{life}} = \frac{\Phi_{n,\text{limit}}}{\varphi_n}$$

and because the components are distributed through the airframe rather than concentrated in one shielded volume, they cannot all be behind the shadow shield. The work therefore had to develop [radiation-resistant motors for nuclear aircraft controls][research_fries_1958] and an entire design practice for [electronic systems intended to work in nuclear aircraft][research_levine_1960], restated the following year as [a major influence on such designs][research_levine_1961]. The material behaviour underneath it was catalogued systematically. [Radiation damage to elastomers, lubricants, fabrics, and plastics][research_aec_1954] is a title that conveys the breadth of the problem, with [plastic laminates][research_bauerlein_1959], [organic lubricants and polymers][research_bolt_1958], and [the behaviour of fuels and lubricants in dynamic test equipment under irradiation][research_krasnow_1959] treated separately, and [a bibliography of effects on aluminium, elastomers, and lubricants][research_cernak_1960] collecting the rest. Control system components have [their own damage study][research_anderson_1952], the field held [semiannual symposia][research_aec_1958], and the whole was gathered into [a handbook][research_aec_1956]. **An aircraft is mostly organic materials and precision mechanisms, and a reactor is hostile to both.**

That subject became an industry once electronics moved into space, and the mechanisms the ANP engineers were discovering empirically now have names and models. Displacement damage in semiconductors is reviewed by [Ha and Kim 2025][research_ha_2025], single-event effects and the hardening practices that answer them by [Aguiar and Martinelli 2026][research_aguiar_2026] and [Liu et al 2025][research_liu_2025], with circuit-level hardening in [Kumar et al 2025][research_kumar_2025] and the charge transport underneath it in [Mendes and Tomal 2025][research_mendes_2025]. **The design practice the programme invented for a bomber is now the reason a satellite works.** That is [radiation hardening][ref_rad_hardening] as an engineering discipline, and its origins are here.

### The Crew, and the Dose They Were Allowed

The dose limit is the boundary condition on the entire shield calculation, and it is not a physical constant.

Mission dose is the product of rate and duration,

$$D_{\text{mission}} = \dot{D} \, t_{\text{mission}}$$

so an endurance mission is precisely the case where a modest dose rate becomes unacceptable. **The mission that justifies the aircraft is the mission that makes its shielding hardest.** A four-hour sortie at a given dose rate is a quarter of the dose of a sixteen-hour one, and the whole argument for nuclear propulsion was flights measured in days.

The limit was not merely an engineering parameter to the programme either. A medical advisory panel was convened under NEPA. Among its subcommittee reports sits [an evaluation of the psychological aspects][research_aec_1949] of asking aircrew to fly a reactor, which is an unusual document to find in an aeronautical record and an indication of how the problem was understood at the time. The somatic effects were pursued in parallel. [Leverett 1960][research_leverett_1960] investigates lens opacity in personnel operating a portable reactor, cataract being the effect that appears first at doses below those that produce anything else measurable.

Choosing $\dot{D}_0$ therefore chooses the shield mass, through the logarithm,

$$m_{\text{shield}} \propto \ln \left( \frac{1}{\dot{D}_0} \right)$$

The sensitivity is worth writing as a derivative, since it is the quantity a programme manager would actually want,

$$\frac{\partial m_{\text{shield}}}{\partial \ln \left( 1 / \dot{D}_0 \right)} = \frac{\rho_s A}{\mu} = \frac{11{,}340 \times 14.1}{79.4} = 2.01 \times 10^{3} \ \text{kilograms per e-fold}$$

so each factor of $e$ in permitted dose is worth two tonnes, and because the dependence is logarithmic, accepting ten times the dose saves only one tenth-value layer of material, which is 2.9 centimetres of lead and about four and a half tonnes on the geometry above. **Relaxing the crew dose limit by a factor of ten buys back about two percent of the aircraft.** That asymmetry is worth stating plainly, because it means the programme could not have been rescued by accepting a more dangerous aircraft. The exponential that makes shielding effective also makes it insensitive to how much risk one is willing to impose on the crew.

## The Flight Test Record

One aircraft flew and it was not the X-6.

The [NB-36H][ref_nb36h], a B-36H-20-CF with serial 51-5712 that had been damaged by a tornado at [Carswell Air Force Base][ref_carswell] on 1 September 1952, was rebuilt as the Nuclear Test Aircraft. It carried the Aircraft Shield Test Reactor, abbreviated ASTR, a one megawatt air-cooled reactor of about 16,000 kilograms, hung in a bomb bay on a hook so it could be lowered into a shielded pit between flights. Water served as moderator and coolant and dumped its heat overboard through water-to-air exchangers. **The reactor never powered the aircraft.** Its purpose was to be a source, and the aircraft's purpose was to measure what that source did to a crew compartment and to the equipment around it.

The crew section was rebuilt in lead and rubber at a mass variously reported between eleven and twelve tonnes, with leaded glass in the windows. The aircraft flew 47 times between 17 September 1955 and March 1957, accumulating 215 flight hours of which the reactor was operated during 89.

The dose the crew accumulated is computable from the reported operating time and is the quantity the whole exercise existed to bound,

$$D_{\text{crew}} = \dot{D}_{\text{shielded}} \, t_{\text{reactor}} = \dot{D}_{\text{shielded}} \times 89 \ \text{hours}$$

so an allowance of fifty millisieverts across the whole programme sets the shielded rate at

$$\dot{D}_{\text{shielded}} = \frac{0.05}{89} = 5.6 \times 10^{-4} \ \text{sieverts per hour}$$

which is the design point the crew shield was built to and which the flights were flown to confirm.

The measurements are the programme's most valuable output and they are documented. The reactor was [calibrated][research_nance_1957], its [fast neutron spectra measured][research_schaeffer_1958], and it was operated in conjunction with the [Tower Shielding Facility][research_kress_1958] so that airborne results could be compared against a ground installation where the geometry was known exactly. The Tower Shielding Facility itself required [its own critical experiments][research_magnuson_1956] and a [conceptual design study][research_frankfort_1956], and [multilayer shield experiments][research_henry_1958] ran alongside. The comparison of measured against calculated dose is the entire point, since a shield design method that has been validated against flight is worth more than one that has not.

What the flights established is that the shielding worked. The crew was not endangered. What they also established, and what mattered more, is that this was true for a one megawatt source in an aircraft that carried nothing else, and that the shield for a hundred megawatt propulsion reactor would be the mass computed above.

The NB-36H was scrapped, the X-6 was never begun, and the programme was cancelled in March 1961.

## Comparison With Ground Prediction

The X-6 inverts the usual relationship, because there was no flight against which to check the prediction, and the prediction is all there is.

For every other aircraft in this series the interesting question is where the ground facilities were wrong. Here the ground facilities are the entire record. The Aircraft Reactor Experiment, the Heat Transfer Reactor Experiments, the Tower Shielding Facility, and the NB-36H measurements form a body of validated engineering that was never assembled into an aeroplane, and the honest assessment is that the prediction was largely right and the programme was cancelled for reasons the prediction supported instead of contradicting.

There is one check available, and it is worth performing because it is the only place in this article where the derivation can be tested against hardware that existed. Apply the shield calculation to the ASTR in the NB-36H rather than to a propulsion reactor.

The source is a hundred times weaker and the separation is greater, so the unshielded rate at the crew station scales as

$$\dot{D}_{\text{ASTR}} = \dot{D}_{100} \left( \frac{P_{\text{ASTR}}}{P_{100}} \right) \left( \frac{r_{100}}{r_{\text{ASTR}}} \right)^{2} = 9.84 \times \frac{1}{100} \times \left( \frac{10}{15} \right)^{2}$$

$$\dot{D}_{\text{ASTR}} = 0.044 \ \text{grays per second} = 157 \ \text{grays per hour}$$

Holding the crew to fifty millisieverts across the 89 hours of reactor operation demands

$$\mathcal{A} = \frac{157}{5.6 \times 10^{-4}} = 2.8 \times 10^{5}, \qquad x = \frac{\ln \left( 2.8 \times 10^{6} \right)}{0.794} = 18.7 \ \text{centimetres}$$

The NB-36H's crew shield was a bulkhead across the front of the compartment, not a wrap around it, so the area is the compartment cross-section and not its surface. Taking six square metres,

$$m = \rho_s A x = 11{,}340 \times 6.0 \times 0.187 = 1.27 \times 10^{4} \ \text{kilograms}$$

**Against a reported crew shield of eleven to twelve tonnes.** Repeating the calculation with the far more permissive occupational allowance of the 1950s, about 0.3 sieverts, gives 16.4 centimetres and 11.2 tonnes. The two bracket the reported figure. **The method used throughout this article reproduces the one aircraft in it that actually flew**, which is the closest thing to validation available for a programme that never built its aeroplane, and it is the reason the propulsion-reactor numbers above are worth taking seriously.

The one place where flight added something the ground could not is the air-scattering term. A reactor on a tower over a field is not a reactor at altitude in a moving aircraft, and the scattered dose depends on the density and geometry of the air around the source. That is why the NB-36H flew rather than merely sitting on a stand, and it is why [Edwards 1954][research_edwards_1954] is a document about altitude and flight speed rather than about geometry alone.

The deeper comparison is between what the programme predicted about itself and what happened to it. The Lexington Project in 1948 said fifteen years and a great deal of money. The programme ran fifteen years, spent about a billion dollars, and was cancelled. **The feasibility study was correct about the cost and the schedule and wrong only in assuming that a correct cost and schedule would be paid.**

## What the Data Changed

The aircraft was never built and the programme's output was substantial, which is the case this article exists to make.

The most durable result is a reactor. The Aircraft Reactor Experiment, abbreviated ARE, run at [Oak Ridge][ref_ornl] in 1954, was the world's first [molten salt reactor][ref_msr], using a circulating fluoride salt as both fuel and coolant. It was built because a molten salt core offers high temperature at low pressure, which is exactly what an aircraft wants, and it ran successfully.

That combination is worth quantifying, because it is the whole of the concept's appeal and it is why the concept outlived the aircraft. A water-cooled reactor must be pressurized to keep its coolant liquid, and the saturation pressure climbs steeply with temperature,

$$p_{\text{sat}}(T) \approx p_c \exp \left[ \frac{\Delta H_{\text{vap}}}{R} \left( \frac{1}{T_c} - \frac{1}{T} \right) \right]$$

so a pressurized water reactor at 600 kelvin sits near 15.5 megapascals while a molten fluoride salt at 1000 kelvin has a vapour pressure below a kilopascal, a ratio of

$$\frac{p_{\text{PWR}}}{p_{\text{salt}}} \approx 1.5 \times 10^{4}$$

The vessel mass follows the pressure directly, since a thin spherical shell of radius $R$ holding pressure $p$ at allowable stress $\sigma$ requires

$$t = \frac{p R}{2 \sigma} \quad \Longrightarrow \quad m_{\text{vessel}} = 4 \pi R^{2} \rho t = \frac{2 \pi \rho \, p R^{3}}{\sigma}$$

A molten salt core carries a second property that mattered less to the aircraft than it does now. Because the fuel is dissolved in the coolant, thermal expansion of the salt removes fuel from the core, so the reactivity feedback is strongly negative,

$$\alpha_T = \frac{\partial k_{\text{eff}}}{\partial T} < 0, \qquad \delta k = \alpha_T \, \delta T$$

and a power excursion is self-limiting without any control action at all. **The pressure vessel mass is proportional to the pressure, so a molten salt reactor's vessel is four orders of magnitude lighter than a water reactor's at the same size.** For an aircraft that is decisive, and for a ground station it is merely attractive, which is why the idea survived in a place it was not invented for. [Its operation][research_cottrell_1955_2] and [the operating account of Bettis 1957][research_bettis_1957] document the experiment, [the hazards summary][research_cottrell_1952_3] preceded it, [the components of its fused-salt and sodium circuits][research_savage_1958] are described in detail, and it was [disassembled and examined afterward][research_cottrell_1958]. [Oak Ridge's aircraft nuclear power plant designs][research_fraas_1954] give the surrounding context.

The pivot from aircraft to civilian power is visible in the record as it happens. [McPherson 1957][research_mcpherson_1957] is titled *Molten Salts for Civilian Power* and appeared while the aircraft programme was still running, [Briant 1957][research_briant_1957] argues molten fluorides as power reactor fuels, [Grimes 1958][research_grimes_1958] sets out the chemistry, and by [MacPherson 1960][research_macpherson_1960] the concept is being evaluated for a ten-year plan that has nothing to do with aeroplanes. **The people who built a reactor for an aircraft spent the late 1950s explaining that it would be more useful somewhere else, and they were right.**

**That reactor is the ancestor of a technology now under active commercial development.** The molten salt reactor is a serious contemporary subject, and the modern literature is treated below. An aircraft programme that produced no aircraft produced a reactor concept that outlived it by seventy years and is being commercialized as this is written. That is not a consolation prize. It is a better return than most flown programmes achieve.

The second consequence is a design discipline. Shielding analysis as a computational activity, radiation-hardened components, and the practice of validating shield codes against measurement are all recognizable as ANP outputs. When nuclear propulsion returned as a subject it returned for space rather than for air, and it inherited these tools directly. The [NERVA][ref_nerva] programme and its [nuclear thermal rocket][ref_ntr] successors, the [radiation shielding weight problem in space][research_beever_1965], and the [symposia on protection against radiations in space][research_reetz_1965] are the same discipline redirected. That redirection was already under way while ANP ran. [Schreiber 1956][research_schreiber_1956] describes the Los Alamos nuclear rocket programme that became Rover and then NERVA. The crewless branch has its own paper trail, and the [Pluto programme progress reports][research_aec_1957_4] document the nuclear ramjet in period.

The Soviet effort was watched. [Butz 1959][research_butz_1959] gives an open-literature assessment of Soviet nuclear plane concepts written while both programmes were live. The American programme's own institutional summary is [Air Force Nuclear Propulsion][research_aec_1959_6]. The [Plum Brook hazards work][research_naca_1963] shows the transition in progress at NASA.

The third is a negative result that was correct. Air-breathing nuclear propulsion for crewed aircraft has not been revived by anyone, anywhere, in the sixty-five years since. The Soviet Union flew its own testbed, the [Tu-95LAL][ref_tu95lal], and reached the same conclusion. The [Project Pluto][ref_project_pluto] nuclear ramjet, which dispensed with the crew and therefore with most of the shield, is the exception that proves the rule, since removing the crew removes the constraint this article is about.

## The Contemporary Literature

The subject did not end. It moved, and it split into three descendants that no longer resemble one another.

### Molten Salt Reactors

The Aircraft Reactor Experiment's direct line is now a substantial commercial and academic field. [Holcomb 2025][research_holcomb_2025] treats thermal-spectrum molten salt breeder fuel cycles, [McFarlane 2024][research_mcfarlane_2024] argues that the fuel cycle rather than the reactor is the hard part, and [Creasman et al 2024][research_creasman_2024] compute fuel depletion for a molten salt demonstration reactor. Modelling work includes [Fischer and Bureš 2024][research_fischer_2024], whose subject is the Molten Salt Reactor Experiment itself, the ARE's own successor at Oak Ridge, and [Mochizuki 2024][research_mochizuki_2024] on load following. The chemistry that makes a circulating fuel salt difficult is pursued by [Cheng et al 2025][research_cheng_2025] on noble metal fission product aggregation and [Niu et al 2024][research_niu_2024] on extracting molybdenum-99 from fuel salt, with [Yilmaz et al 2025][research_yilmaz_2025] on thorium fuelling and [Mishra et al 2024][research_mishra_2024] supplying an irradiated fuel salt data library. Accident behaviour is [Dunkle and Bogetic 2026][research_dunkle_2026]. The physical properties of the salts themselves, which the Oak Ridge chemists established by measurement, are now being computed from first principles by [Li et al 2026][research_li_2026], the tritium that a fluoride salt inevitably generates is [Jiang et al 2026][research_jiang_2026], and salt behaviour outside the reactor entirely, as a lubricant, is [Liu and Chen 2026][research_liu_2026_2]. Reactor kinetics with a circulating fuel, where the delayed neutron precursors leave the core before they decay, is a peculiarity of this reactor type that the ARE encountered first and that [Chen et al 2025][research_chen_2025_2] still treat. **A 1954 aircraft reactor experiment is the origin of all of it.**

### Shielding

The shield-mass problem this article derives is now solved computationally rather than empirically, but it is the same problem. [Ahmed 2026][research_ahmed_2026] reviews neutron shielding mechanisms and materials, [Liu et al 2026][research_liu_2026] present a dual-stage shielding optimization method, and [Huang et al 2025][research_huang_2025] optimize the shield of a heat pipe cooled reactor, which is a compact mobile reactor and therefore the same class of problem as an aircraft. [Lee and Cho 2025][research_lee_2025] address the question this article calls the boundary condition, namely how to set the radiation target level that the whole design then follows from.

The modern statement of the problem is a constrained optimization over a layered geometry rather than the closed-form estimate used above,

$$\min_{\mathbf{x}} \ \sum_{j} \rho_j A_j x_j \quad \text{subject to} \quad \dot{D}\left( \mathbf{x} \right) \le \dot{D}_0, \quad x_j \ge 0$$

with the dose evaluated by transport rather than by an attenuation law, which is what makes it tractable to solve well and intractable to solve by hand. The gain over a hand estimate comes from letting the layer thicknesses vary independently and from exploiting the fact that each material attenuates both radiations,

$$\dot{D} \left( \mathbf{x} \right) = \dot{D}_\gamma \prod_j B_j e^{-\mu_j x_j} + \dot{D}_n \prod_j e^{-\Sigma_{R,j} x_j}$$

which is the coupling this article set aside when it treated the lead and the lithium hydride separately and called their sum an upper bound.

Shielding materials are being developed at a rate the programme would have envied, and the search is now for composites that combine attenuation with structure rather than for a single dense element. [Ozdemir et al 2025][research_ozdemir_2025] develop a ternary gamma-shielding composite, [Sayyed et al 2025][research_sayyed_2025], [Gomaa and El-Tayebany 2026][research_gomaa_2026], and [Yavuzkanat and Sahmaran 2026][research_yavuzkanat_2026] evaluate glass systems where the shielding and the structural role are the same material, and [Jiang 2025][research_jiang_2025] pursues carbon-bearing neutron shields, which is the lithium hydride idea with the hydrogen bound differently. Facility-scale optimization appears in [Syarip et al 2025][research_syarip_2025] and [Chen 2025][research_chen_2025].

Materials work continues along the lines the programme opened. [Bhardwaj et al 2024][research_bhardwaj_2024] fabricate neutron-absorbing metal hydride ceramic matrix composites, which is the lithium hydride idea in modern form, and [Stone et al 2024][research_stone_2024], [Khan et al 2025][research_khan_2025], and [Sekkat et al 2026][research_sekkat_2026] develop composite and additively manufactured shields. Space reactor shielding specifically is [Han et al 2025][research_han_2025] and [Han et al 2025][research_han_2025_2], with [Oğul et al 2026][research_ogul_2026] treating a small modular reactor. The crewed-vehicle version of the problem, which is the X-6's problem with the source moved outside, appears in [DeWitt and Benton 2024][research_dewitt_2024] on secondary proton buildup, [Matthiä and Berger 2024][research_matthia_2024] on lunar surface exposure, and [Yıldırım and Opçin 2026][research_yildirim_2026] on multilayer composites.

### Nuclear Propulsion Where the Shield Is Affordable

Nuclear propulsion survived in the two places where the constraint this article derives does not bind, which are vehicles with no crew and vehicles where nothing else will do.

Space is the second case. [Alnuaimi and Kim 2026][research_alnuaimi_2026] assess a liquid uranium-manganese nuclear thermal rocket, [Guilbaud et al 2024][research_guilbaud_2024] restudy the KIWI-B-4E core from the Rover programme with modern methods, and [Aueron and Thomas 2024][research_aueron_2024] examine electric-pump-fed nuclear thermal propulsion. Nuclear electric systems appear in [Ma et al 2026][research_ma_2026] and mission studies in [Ancona et al 2025][research_ancona_2025]. **[Duan et al 2026][research_duan_2026] analyse the reactivity safety of an air-cooled nuclear thermal propulsion reactor, which is the direct air cycle returning under a different name for a different vehicle.**

Surface and orbital power is a further branch, and [Smith et al 2026][research_smith_2026] analyse a Kilopower-class reactor for lunar use while [Zhang et al 2026][research_zhang_2026_3] model the heat pipe startup such a system depends on. Marine propulsion never stopped, and [Delgarm et al 2025][research_delgarm_2025] optimize a naval plant while [Kim and Lee 2026][research_kim_2026_2] explicitly modernize the ML-1 architecture, which was a transportable military reactor contemporary with ANP. **Every one of those applications shares the X-6's constraint and relaxes exactly one part of it**, since a lunar reactor has no crew nearby, a ship can carry the shield, and a transportable reactor need not fly.

The microreactor is the other descendant, and it inherits the X-6's real problem, which is a reactor that must operate away from the infrastructure a power station enjoys. [Parisi and Arafat 2026][research_parisi_2026] describe the MARVEL microreactor, [Domingos et al 2026][research_domingos_2026] and [Rangel et al 2026][research_rangel_2026] treat fuel choices including designs avoiding enriched uranium, and the economics that decide whether any of it happens are [Abdussami et al 2025][research_abdussami_2025], [Kim and Macfarlane 2026][research_kim_2026], and [Shobeiri et al 2025][research_shobeiri_2025]. Accident source terms and tolerant fuels are [Sun et al 2025][research_sun_2025] and [Elkhawas et al 2025][research_elkhawas_2025], with materials in [Islam and Haque 2025][research_islam_2025] and [Lan et al 2024][research_lan_2024]. The proliferation dimension, which the X-6 raised by requiring highly enriched fuel in a compact core and which no other aircraft in this series raises at all, is treated by [Mitsuboshi and Sagara 2025][research_mitsuboshi_2025] for small modular reactors, [Bolukbasi and Margulis 2026][research_bolukbasi_2026] through fuel cycle composition, and [Chong and Sagara 2025][research_chong_2025] through burnup strategy. Isotope production as a use for the flux appears in [Chandler et al 2025][research_chandler_2025].

### What Took Its Place in Aviation

The question the X-6 was built to answer, which is how to fly without carrying the energy as chemical fuel, is live again and is being answered differently.

Hydrogen is the leading candidate and it has the same structural character as nuclear propulsion, which is that the energy is cheap and the container is expensive. [Li 2024][research_li_2024] reviews hydrogen-powered aircraft, [Jagtap et al 2024][research_jagtap_2024] and [Wahler et al 2025][research_wahler_2025] work the conceptual design and the aerostructural trade, [Sasi et al 2025][research_sasi_2025] treat hydrogen and ammonia turbofans, [Lu et al 2025][research_lu_2025] recover exhaust heat in a cryogenic installation, and [Zhang et al 2026][research_zhang_2026] address crashworthiness, which is the hydrogen version of the question the [nuclear aircraft safety programme][research_aec_1957_3] asked about dispersing a core. Batteries are the other candidate and their specific energy remains the binding constraint, as [Cetegen et al 2025][research_cetegen_2025] and [Peng et al 2024][research_peng_2024] show. The hydrogen case is surveyed by [Gopalasingam et al 2025][research_gopalasingam_2025], the tank and its ballast consequences are codesigned by [Antonakis and Glenis 2026][research_antonakis_2026], the thermodynamics of the stored liquid are [Li et al 2026][research_li_2026_2], and the drop-in alternative that avoids the tank entirely is the synthetic fuel of [Bardon et al 2025][research_bardon_2025] and [Quiroz et al 2025][research_quiroz_2025]. The same argument is being had at sea, where the mass penalty is affordable, in [Liu and Fu 2025][research_liu_2025_3].

**The mission itself has also been answered without any of this.** The X-6 existed to keep an aircraft airborne indefinitely, and that requirement is now met by vehicles with no crew to shield and very little mass to lift. [Jung et al 2025][research_jung_2025] analyse the endurance of a solar-powered high-altitude unmanned aircraft, which achieves persistence by having almost no energy demand rather than by carrying an enormous energy supply, and the structural problems such an airframe meets instead are [Sampath and Kattimani 2025][research_sampath_2025]. **A programme that spent a billion dollars to remove the fuel constraint was eventually answered by removing the crew and most of the aircraft**, which is a solution nobody in 1946 would have accepted and nobody in 2026 finds surprising.

**Every one of these is a fixed-overhead problem of the kind this article derives for the shield.** The general form is worth writing down, because it is what the X-6 is an instance of. Let an aircraft carry a fixed installation of mass $m_{\text{fix}}$ that enables a mission but performs no work during it. The payload available is what remains,

$$m_{\text{payload}} = m_{\text{gross}} - m_{\text{empty}} - m_{\text{fix}} - m_{\text{consumed}}$$

and the configuration is viable only while that difference is positive and large enough to justify the aircraft,

$$\frac{m_{\text{fix}}}{m_{\text{gross}}} < 1 - \frac{m_{\text{empty}}}{m_{\text{gross}}} - \frac{m_{\text{payload,min}}}{m_{\text{gross}}}$$

For hydrogen the fixed installation is the tank, characterized by a gravimetric index,

$$\eta_g = \frac{m_{\text{H}_2}}{m_{\text{H}_2} + m_{\text{tank}}} \quad \Longrightarrow \quad \frac{m_{\text{tank}}}{m_{\text{H}_2}} = \frac{1 - \eta_g}{\eta_g}$$

so an index of 0.35 costs 1.86 kilograms of tank per kilogram of fuel while an index of 0.7 costs 0.43, and the entire commercial argument turns on which end of that range is achievable. A cryogenic tank, like a shield, has a mass that does not shrink in proportion to the mission and that must be carried whether or not it is doing anything at that moment. The X-6's arithmetic is a special case of a general pattern in aircraft design, and recognizing it as such is worth more than the aircraft would have been.

## Where the Framing Breaks Down

The keystone framework fits an unbuilt aircraft badly in three ways, and the ways are instructive.

There was no flight, so there was no measurement of the keystone. Everything in the sizing section above is a calculation, and calculations were available in 1948. An instrument model that treats a research aircraft as reducing uncertainty has nothing to work with when the aircraft does not exist, and the honest reading is that the X-6 reduced uncertainty about the programme's cost rather than about its physics.

The programme's most valuable output is unrelated to its keystone. A molten salt reactor is not an answer to the question of whether shielding can be carried. It is a reactor concept that happened to suit an aircraft's requirements for high temperature at low pressure, and it survived because those requirements recur in contexts having nothing to do with aircraft. A framework scoring an effort against its own question will miss this entirely, and it is the most important thing that happened.

The cancellation was not a technical decision and the framework has no place to put that. Intercontinental ballistic missiles made the indefinitely loitering bomber strategically uninteresting, and aerial refuelling made unlimited range achievable by other means. The second of those can be put beside the shield directly. A tanker delivers fuel at a cost in sorties rather than in airframe mass, so the range a refuelled conventional bomber achieves is

$$R_{\text{refuelled}} = \frac{V}{c_t} \frac{L}{D} \sum_{i} \ln \left( \frac{m_{i}}{m_{f,i}} \right)$$

summed over refuelling segments, and the sum has no upper bound that the aircraft itself imposes. **Unlimited range was achieved by a logistics arrangement rather than by a propulsion technology, at zero cost in payload.** The nuclear aircraft was competing against a solution that had already won on the metric it was optimizing. The X-6 was not defeated by its shield. **It was made pointless by two unrelated technologies while it was still arguing with its shield**, which is a far more common way for engineering work to end than outright failure.

## The Source Base

The source base for this article differs from every other in the series in one structural respect, and it is worth stating explicitly.

**The primary record is not in the NASA archive.** ANP was an Atomic Energy Commission and Air Force programme, so its reports went to the AEC and are held today by the Department of Energy, discoverable through the Office of Scientific and Technical Information rather than through the [NASA Technical Reports Server][ref_ntrs]. The consequence for anyone retracing this work is that the standard search for an X-plane returns almost nothing, and the standard conclusion, that the record is thin, is exactly wrong. The record is enormous and is in a different building.

The documentary record proper is the quarterly and semiannual progress report series, running from [Cottrell 1951][research_cottrell_1951] through [1952][research_cottrell_1952], [1952][research_cottrell_1952_2], [Cottrell 1953][research_cottrell_1953], [Savolainen 1954][research_savolainen_1954], [Savolainen 1955][research_savolainen_1955], [Savolainen 1956][research_savolainen_1956], [Savolainen 1956][research_savolainen_1956_2], [1957][research_aec_1957], [Jordan 1957][research_jordan_1957], [1957][research_aec_1957_2], [1957][research_na_1957], and [1959][research_aec_1959], with the [administrative account of Dibble 1958][research_dibble_1958] and the [technical briefing of Perry 1958][research_perry_1958] giving the management view. **That series alone runs to tens of thousands of pages and is the single strongest argument against calling this a thinly documented aircraft.** The founding documents are [Gasser 1947][research_gasser_1947] on the NEPA project, the [Lexington Project minutes][research_stever_1948] and [their companion][research_stever_1948_2], and the [NEPA quarterly report of 1950][research_aec_1950_2]. Late-programme summaries are [the General Electric direct-air-cycle programme report][research_comassar_1962], [the reactor and shield physics volume][research_edwards_1962], and [the powerplant data compilation][research_meyer_1965]. [Study of seaplane systems employing nuclear power][research_aec_1959_4] shows how far the application space was searched, and [the engineering proposal for nuclear turbojet development][research_schmickrath_1960] shows what was still being proposed at the end. [Shielding computer program specifications][research_edwards_1957], [the two-component method of shield analysis][research_moteff_1960], [a shield specification][research_johnson_1960], [shield weights for a Boeing mission][research_lee_1958], [the LID tank shield study][research_kam_1961], [the seventh shielding information meeting papers][research_aec_1961], [aircraft reactor control systems][research_gorker_1955], and [HTRE fuel reprocessing studies][research_cannon_1961] fill in the technical detail. [Two-dimensional diffusion theory applied to a fuel-plate-removal experiment][research_gotsky_1959], [tungsten-uranium dioxide fuel retention][research_gedwill_1965], and [ceramic fibre development][research_gates_1961] are NACA and NASA contributions to the surrounding materials problem. Reactor kinetics has [a bibliography of its own][research_bloomfield_1959], while the computational aids of the period run to [a reactor power calculator][research_gardner_1958], both of which convey how much of this work was done before the tools existed to do it easily.

The secondary literature on the aircraft itself is thin, which is the opposite of the primary situation. [Miller 2001][book_miller_2001_x_planes], [Jenkins Landis and Miller 2003][book_jenkins_landis_miller_2003], [Winchester 2005][book_winchester_2005_x_planes], and [Peebles 2014][book_peebles_2014_probing_the_sky] give the roster treatment, and [Hallion 1972][book_hallion_1972_supersonic_flight], [Hallion 1981][book_hallion_1981_on_the_frontier], [Gorn 2001][book_gorn_2001_expanding_envelope], and [Bilstein 1989][book_bilstein_1989_orders] supply institutional context, with [Gunston 1992][book_gunston_1992_faster_than_sound] the wider framing.

The engineering texts behind the relations are [Hill and Peterson 1991][book_hill_peterson_1991] and [Sutton and Biblarz 2016][book_sutton_biblarz_2016] for propulsion, [Incropera and DeWitt][book_incropera_heat_transfer], [Carslaw and Jaeger 1959][book_carslaw_jaeger_1959], and [Boley and Weiner 1960][book_boley_weiner_1960] for heat transfer and thermal stress, [Anderson 2001][book_anderson_2001_fundamentals], [Anderson 2012][book_anderson_2012_aircraft_performance], and [Bertin and Cummings 2013][book_bertin_cummings_2013] for aerodynamics, and [Raymer 2018][book_raymer_2018], [Nicolai and Carichner 2010][book_nicolai_carichner_2010], [Torenbeek 1982][book_torenbeek_1982], and [Roskam 1985][book_roskam_1985] for design method and mass estimation. Structures are [Bruhn 1973][book_bruhn_1973], [Niu 1988][book_niu_1988_airframe], and [Megson 2016][book_megson_2016]. Error analysis is [Taylor 1997][book_taylor_1997_error_analysis] and [Bevington and Robinson 2002][book_bevington_robinson_2002], with design of experiments in [Box Hunter and Hunter 2005][book_box_hunter_hunter_2005] and [Gelman et al 2013][book_gelman_et_al_2013], and information accounting in [Cover and Thomas 2006][book_cover_thomas_2006]. The epistemology is [Vincenti 1990][book_vincenti_1990], [Petroski 1985][book_petroski_1985], and [Ferguson 1992][book_ferguson_1992], and the organizational reading, which this article leans on more than most, is [Perrow 1984][book_perrow_1984], [Vaughan 1996][book_vaughan_1996], [Sagan 1993][book_sagan_1993], and [Reason 1990][book_reason_1990_human_error]. Institutional histories are [Baals and Corliss 1981][book_baals_corliss_1981], [Hansen 1987][book_hansen_1987_engineer_in_charge], and [Chambers and Chambers 2008][book_chambers_2008_radical_wings], with [Heppenheimer 2007][book_heppenheimer_2007_heat_barrier] and [Jenkins 2000][book_jenkins_2000_hypersonics] on the high-speed thread and [Launius and Jenkins 2012][book_launius_jenkins_2012] and [Merlin 2009][book_merlin_2009_blackbird] on the successors.

Foundational primaries bearing on the surrounding arguments include [Williams and Drake][research_williams_drake_1948] on the research airplane rationale, [Buckingham 1914][research_buckingham_1914] on similarity, [Nyquist 1928][research_nyquist_1928] and [Shannon 1948][research_shannon_1948] on sampling and channel capacity, and [Lindley 1956][research_lindley_1956] and [Chaloner and Verdinelli 1995][research_chaloner_verdinelli_1995] on experimental design. Related work on this blog appears in [A96][related_post_a96_history_rocketplanes] on the rocketplane lineage, [A106][related_post_a106_two_stage_delta_wing] on large high-speed configurations, [A217][related_post_a217_rocket_propellant_chemistry] on propellant chemistry, [A237][related_post_a237_aerospace_framing] and [A241][related_post_a241_aerospace_simulation] on the computing and simulation infrastructure, and [A90][related_post_a90_intro_space_studies] on space policy. The [NASA History Office][ref_nasa_x3_factsheet] and the [Armstrong Flight Research Center][ref_nasa_armstrong] hold the aeronautical side of the record, with [Oak Ridge][ref_ornl] and [Idaho][ref_inl] holding the nuclear side.

## Epistemic State

Established historical fact includes the start of Project NEPA on 28 May 1946 under the Army Air Forces, its funding at ten million dollars in 1947, its replacement by the joint AEC and Air Force ANP programme in May 1951, the assignment of the direct air cycle to General Electric and the indirect cycle to Pratt and Whitney, the MX-1589 modification of two B-36 airframes, the tornado damage to 51-5712 at Carswell on 1 September 1952, its rebuilding as the NB-36H, its carriage of the one megawatt Aircraft Shield Test Reactor, its 47 flights and 215 hours between 17 September 1955 and March 1957 with the reactor operated for 89 of those hours, the operation of the Aircraft Reactor Experiment at Oak Ridge in 1954 as the first molten salt reactor, the ground testing of a direct-cycle nuclear turbojet in the HTRE series, and the cancellation of the programme in March 1961 without the X-6 being built.

Established engineering analysis includes every relation in the sizing sections. The exponential attenuation law with buildup, the logarithmic dependence of shield thickness on power and on dose limit, the separation optimum, the Way-Wigner decay heat correlation, the turbojet thrust and heat addition relations, and the heat exchanger effectiveness relation are standard results.

**Derived here and not taken from a source** are the hundred megawatt thermal power estimate for a B-36-class cruise, the 0.44 kilogram uranium consumption over a hundred hours, the gamma source strength and the ten gray per second unshielded dose rate at ten metres, the attenuation requirement of $7.1 \times 10^{7}$ that follows from a fifty millisievert mission limit, the 25.7 centimetre lead thickness and the 222 centimetre lithium hydride thickness, the 8.7 centimetre thickness increment for a thousandfold power increase, the 10.1 metre separation optimum, the 41 tonne gamma shield mass with a 66 tonne upper bound including neutrons and their ratios to gross weight and payload, the 100 megawatt per cubic metre core power density, the 1211 kelvin indirect-cycle reactor outlet requirement, the 23 minute adiabatic melt time, and the decay heat figures. These follow by arithmetic from published dimensions and standard physical constants and can be reproduced or refuted by any reader with them.

Inference includes the central claim that the shield mass rather than any other difficulty was the binding constraint, and the subsidiary claim that the logarithmic dependence made the programme insensitive to relaxing the crew dose limit. Both are consistent with the record and with the fact that shield optimization was a named research subject throughout the programme, but neither is a statement the primary reports make in those terms.

Weakly supported are the representative values. The lift-to-drag ratio of eighteen, the overall propulsive efficiency of 0.20, the shadow shield area of 14.1 square metres, the fuselage structural mass of 400 kilograms per metre, the fifty millisievert mission dose allowance from which the attenuation requirement follows, the four percent gamma energy fraction, the mean photon energy of one megaelectronvolt, the lithium hydride removal cross-section, the buildup factor of ten, and the five tonne core mass used in the melt-time estimate are all plausible figures for the class rather than values taken from the design. The shield mass estimate should be read as establishing an order of magnitude and a ratio, not a design number. The ratio is more trustworthy than the absolute value, and the qualitative conclusion that shielding consumes a payload-sized fraction of a B-36 is robust to any reasonable choice of inputs.

Contested or unresolved in the sources consulted is the total programme cost, given as about one billion dollars in one place and seven billion in another, a discrepancy most plausibly explained by inflation adjustment but not stated as such by either source. The crew shield mass is given as eleven tonnes in one account and twelve in another, the window thickness as six inches in one and ten to twelve in another, and the scrapping of the NB-36H is placed at Fort Worth in 1958 in one account and at Carswell in 1957 in another. None of these are load-bearing for the argument, and all are stated here as reported rather than resolved.

A note on temporal position. This article carries an editorial date of 2025-10-12 and is written from current knowledge, including contemporary literature published well after that date.

## Out of Scope

This article does not treat the [X-1][related_post_a298_bell_x1], [X-2][related_post_a299_bell_x2], [X-3][related_post_a300_douglas_x3], [X-4][related_post_a301_northrop_x4], or [X-5][related_post_a302_bell_x5] beyond the comparisons drawn, all of which have their own articles. It does not derive the standard relations reused here, since the [series opener][related_post_a297_xplanes_framing] does that once for all seventy-two articles, including the [flight envelope][ref_flight_envelope], [load factor][ref_load_factor], [wing loading][ref_wing_loading], [lift][ref_lift_coefficient] and [drag][ref_drag_coefficient] coefficients, [lift-to-drag][ref_lift_to_drag], [Reynolds][ref_reynolds_number] and [Prandtl][ref_prandtl_number] numbers, [measurement uncertainty][ref_measurement_uncertainty] and its [propagation][ref_propagation_of_uncertainty], and the [standard atmosphere][ref_isa] in its [tabulated form][ref_us_standard_atmosphere].

It does not attempt a history of the Aircraft Nuclear Propulsion programme, which is a large subject with a literature of its own and is treated here only where it bears on the aircraft. It does not treat [nuclear fission][ref_fission] or the [nuclear reactor][ref_reactor] as subjects, nor [nuclear fuel][ref_nuclear_fuel], [enriched uranium][ref_enriched_uranium], [neutron moderators][ref_moderator], or [beryllium][ref_beryllium] as materials, nor [radiation protection][ref_rad_protection] and [ionizing radiation][ref_ionizing] as disciplines, nor the [sievert][ref_sievert] and [absorbed dose][ref_absorbed_dose] as units, nor [gamma rays][ref_gamma] and [neutron radiation][ref_neutron_rad] as phenomena, nor the [half-value layer][ref_hvl] and [Monte Carlo method][ref_monte_carlo] as techniques, nor [nuclear accidents][ref_nuclear_accidents] as a category. It does not cover the [turbojet][ref_turbojet] as a machine, [transonic][ref_transonic] or [supersonic][ref_supersonic_speed] flow, [swept wings][ref_swept_wing], the [aspect ratio][ref_aspect_ratio], [Mach][ref_mach_number] and [dynamic pressure][ref_dynamic_pressure] as quantities, the [speed of sound][ref_speed_of_sound], [flight dynamics][ref_flight_dynamics], [longitudinal][ref_longitudinal_static_stability] and [directional][ref_directional_stability] stability, [aeroelasticity][ref_aeroelasticity], [buffeting][ref_buffeting], [shock waves][ref_shock_wave] and [oblique shocks][ref_oblique_shock], [wave drag][ref_wave_drag], [boundary layer][ref_boundary_layer] and [separation][ref_flow_separation] behaviour, the [aerodynamic centre][ref_aerodynamic_center], [moments of inertia][ref_moment_of_inertia], the [wing root][ref_wing_root], [wing configuration][ref_wing_configuration] as a taxonomy, [delta wings][ref_delta_wing], [stability augmentation][ref_stability_augmentation], [duralumin][ref_duralumin], [yield][ref_yield_strength], [telemetry][ref_telemetry], [strain gauges][ref_strain_gauge], [accelerometers][ref_accelerometer], [takeoff][ref_takeoff] and [landing gear][ref_landing_gear], the [sound barrier][ref_sound_barrier], [wind tunnels][ref_wind_tunnel], [flight testing][ref_flight_test], [Edwards][ref_edwards_afb] and the [Armstrong Flight Research Center][ref_armstrong_frc], [Bell Aircraft][ref_bell_aircraft], [Chuck Yeager][ref_yeager], the [NACA][ref_naca] and [NASA][ref_nasa] as organizations, the [National Museum of the United States Air Force][ref_nmusaf], the [list of X-planes][ref_list_of_x_planes], or [experimental aircraft][ref_experimental_aircraft] as a category, all of which are treated where they belong.

## Conclusion

The Convair X-6 was never built, and what it would have had to carry can be computed in a page.

A B-36 at cruise needs about a hundred megawatts of thermal power, and a reactor supplying it consumes less than half a kilogram of uranium in a hundred hours against 837 tonnes of kerosene for the same energy. That is the entire attraction and it is a factor of nearly two million. Unshielded at ten metres that reactor delivers about ten grays per second, when five grays is a lethal dose, so one second of exposure would kill the crew. Holding them to fifty millisieverts over a hundred-hour flight demands an attenuation of seven times ten to the seventh, which is twenty-six centimetres of lead, and the geometry that minimizes the total mass puts the reactor about ten metres from the crew, which a B-36 fuselage accommodates easily. The gamma shield that results weighs about 41 tonnes, which is twenty-two percent of the aircraft and slightly more than the whole of its bomb load, and the neutron layer takes the upper bound to about 66 tonnes. **A nuclear bomber buys unlimited range by surrendering the payload that made the range worth having.**

The exponential that makes shielding work also makes it stubborn. Shield thickness depends on the logarithm of reactor power, so a thousandfold increase in power costs under nine centimetres of lead, which means the shield is a fixed overhead rather than a proportional cost and small nuclear aircraft are not merely difficult but excluded. The same logarithm means that accepting ten times the crew dose saves about two percent of the aircraft. The programme could not have been rescued by being braver.

One aircraft flew and it was not the X-6. The NB-36H carried a one megawatt reactor 47 times to measure what shielding actually does, and it established that the shielding worked, for a source a hundred times smaller than the one that would have propelled it. A direct-cycle nuclear turbojet ran on a test stand in Idaho and produced thrust from fission. The programme reached that point and was cancelled in 1961, not because the shield defeated it but because ballistic missiles and aerial refuelling had made an indefinitely loitering bomber a solution without a problem.

What survives is a reactor. The Aircraft Reactor Experiment ran at Oak Ridge in 1954 as the world's first molten salt reactor, built because a molten salt core gives high temperature at low pressure, which is what an aircraft wants and, as it turns out, what a good deal else wants too. Seventy years later that concept is under commercial development while the aircraft it was invented for remains unbuilt. An effort that produces no aircraft and one durable reactor technology has not failed in any sense worth the word, and the fact that it is remembered as a failure is a defect in how such work is scored, not in what this one did.

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
- [Aguiar and Martinelli 2026 Single-Event Effects, Modeling, Prediction, Testing and Radiation Hardening][research_aguiar_2026]
- [Ahmed 2026 Neutron Shielding, Advanced Mechanisms, Challenges, and Material Strategies][research_ahmed_2026]
- [Alnuaimi and Kim 2026 Feasibility and Performance of a Liquid Uranium-Manganese Nuclear Thermal Rocket][research_alnuaimi_2026]
- [Alvis and Chessman 1957 An Investigation of the Application of the Gas Generator-Free Turbine Cycle to a Nuclear Powered Aircraft][research_alvis_1957]
- [Ancona et al 2025 Feasibility Study of a Mission to Sedna, Nuclear Propulsion and Advanced Concepts][research_ancona_2025]
- [Anderson 1952 Radiation Damage To Reactor Control System Components (Task 1404)][research_anderson_1952]
- [Antonakis and Glenis 2026 Conceptual Codesign of Cryogenic Storage and Ballast Systems for Hydrogen Aircraft][research_antonakis_2026]
- [Atomic Energy Commission 1948 Index to Lexington Project Reports][research_aec_1948]
- [Atomic Energy Commission 1949 NEPA Medical Advisory Panel Subcommittee No, IX, An Evaluation of the Psychological Problem of Crew Selection Relative to the Special][research_aec_1949]
- [Atomic Energy Commission 1950 NEPA Project quarterly progress report, April 1--June 30, 1950][research_aec_1950_2]
- [Atomic Energy Commission 1950 Nuclear Powered Aircraft for Antisubmarine Warfare][research_aec_1950]
- [Atomic Energy Commission 1954 Radiation Damage To Elastomers, Lubricants, Fabrics And Plastics][research_aec_1954]
- [Atomic Energy Commission 1956 HANDBOOK OF NUCLEAR RADIATION EFFECTS, PART 2, Preliminary Status Report][research_aec_1956]
- [Atomic Energy Commission 1957 Aircraft Nuclear Propulsion Project Quarterly Progress Report For Period Ending June 30, 1957][research_aec_1957_3]
- [Atomic Energy Commission 1957 Aircraft Nuclear Propulsion Project Quarterly Progress Report For Period Ending March 31, 1957][research_aec_1957_2]
- [Atomic Energy Commission 1957 Background Information For Nuclear Aircraft Safety Analysis Program][research_aec_1957]
- [Atomic Energy Commission 1957 Pluto Program (Bi-Monthly Progress Report, July-September, 1957)][research_aec_1957_4]
- [Atomic Energy Commission 1958 Proceedings Of The Second Semi-Annual 125A Radiation Effects Symposium, October 22-23, 1957][research_aec_1958]
- [Atomic Energy Commission 1959 Air Force Nuclear Propulsion][research_aec_1959_6]
- [Atomic Energy Commission 1959 Aircraft Nuclear Propulsion Project Semiannual Progress Report For Period Ending September 30, 1958][research_aec_1959_3]
- [Atomic Energy Commission 1959 Data on Nuclear J-58 Hot Day Performance and Reactor and Shield Information on a Twin 200 Mw Reactor, Six J58 Engine Powerplant][research_aec_1959_2]
- [Atomic Energy Commission 1959 Papers Presented At Anp Materials Meeting November 16-18, 1954, Wright Air Development Center, Dayton, Ohio][research_aec_1959_4]
- [Atomic Energy Commission 1959 Summary Report of HTRE No, 3 Nuclear Excursion][research_aec_1959]
- [Atomic Energy Commission 1961 Papers From Seventh Semiannual Shielding Information Meeting, October 14- 15, 1959][research_aec_1961]
- [Aueron and Thomas 2024 Assessment of Electric-Pump-Fed Nuclear Thermal Propulsion][research_aueron_2024]
- [Auslender 1957 A Monte Carlo Study Of The Gamma-Ray Energy Flux, Dose Rate, And Buildup Factors In A Lead-Water Slab Shield Of Finite Thickness][research_auslender_1957]
- [Bali and Mayer 2025 Investigation of Decay Heat Removal Systems in the ALLEGRO Helium-Cooled Reactor][research_bali_2025]
- [Bardon et al 2025 Greening Aviation with Sustainable Aviation Fuels][research_bardon_2025]
- [Bauerlein 1959 Effects Of Irradiation On Plastic Laminates][research_bauerlein_1959]
- [Beever and Rusling 1965 The Importance of Space Radiation Shielding Weight][research_beever_1965]
- [Bendall 1959 A Programme For Calculating The Gamma Ray Flux Through A Multilayer Shield][research_bendall_1959]
- [Bettis et al 1957 The Aircraft Reactor Experiment, Operation][research_bettis_1957]
- [Bhardwaj et al 2024 Fabrication of Neutron Absorbing Metal Hydride Entrained Ceramic Matrix Composites][research_bhardwaj_2024]
- [Bigelow and Greenstreet 1957 The P & Wa Circulating Fuel Reflector-Moderated Reactor, Volume I][research_bigelow_1957_2]
- [Bigelow and Greenstreet 1957 The P & Wa Circulating Fuel Reflector-Moderator Reactor, Volume 2, Appendix A, Design Specifications And Reference Information For The][research_bigelow_1957]
- [Blizard 1953 Shield Optimization][research_blizard_1953]
- [Blizard and Miller 1958 Radiation Attenuation Characteristics Of Structural Concrete][research_blizard_1958]
- [Bloomfield and Bennet 1959 Reactor Kinetics, A Bibliography][research_bloomfield_1959]
- [Blosser et al 1958 A Study Of The Nuclear And Physical Properties Of The Ornl Graphite Reactor Shield][research_blosser_1958]
- [Bolt et al 1958 Organic Lubricants And Polymers For Nuclear Power Plants][research_bolt_1958]
- [Bolukbasi and Margulis 2026 Impact of Americium-241 on a Proliferation-Resistant Fuel Cycle][research_bolukbasi_2026]
- [Boppart 1957 Preliminary Analysis of Supercharged Nuclear Ramjet Propulsion System][research_boppart_1957]
- [Briant and Weinberg 1957 Molten Fluorides As Power Reactor Fuels][research_briant_1957]
- [Buckingham 1914 On Physically Similar Systems][research_buckingham_1914]
- [Butterfield 1956 FUEL ELEMENT DEVELOPMENT FOR PROJECT 102, Summary Report][research_butterfield_1956]
- [Butz 1959 Soviets Study Nuclear Plane Concepts][research_butz_1959]
- [Cannon et al 1961 Laboratory Studies For Htre Fuel Reprocessing][research_cannon_1961]
- [Capo et al 1957 Shielding Computer Programs 01-0, 02-0, And 03-0 Reactor Shield Analysis][research_capo_1957]
- [Casper and Carver 1958 Comparison Of Computed Centerline Dose Rates From Different Areas Of A Source Plate][research_casper_1958]
- [Cavicchi et al 1959 Design Analysis of a Subsonic Nuclear Powered Logistic Airplane with Helium-Colled Reactor][research_cavicchi_1959]
- [Cernak 1960 HYDRIDES OF TITANIUM, YTTRIUM, AND ZIRCONIUM, A Bibliography][research_cernak_1960_2]
- [Cernak 1960 Radiation effects on aluminum, elastomers, and lubricants, A bibliography][research_cernak_1960]
- [Cetegen et al 2025 Evaluating the Economic Feasibility of Lithium-Ion Battery Energy Storage][research_cetegen_2025]
- [Chaloner and Verdinelli 1995 Bayesian Experimental Design, A Review][research_chaloner_verdinelli_1995]
- [Chandler et al 1957 Effect Of Surface Oxidation Of Fuel Elements On Pressure Loss][research_chandler_1957]
- [Chandler et al 2025 Californium-252 Production at the High Flux Isotope Reactor][research_chandler_2025]
- [Chapman and Storrs 1955 Effective Neutron Removal Cross Sections for Shielding][research_chapman_1955]
- [Chen 2025 Radiation Shielding Analysis of a Linac Extension Area Using FLUKA][research_chen_2025]
- [Chen et al 2025 Dynamic Effect of the Delayed Neutron Precursor Distribution on System Stability][research_chen_2025_2]
- [Cheng et al 2025 Aggregation of Noble Metal Fission Products and Protactinium-233 in a Molten Salt Reactor][research_cheng_2025]
- [Chong and Sagara 2025 Once-Through High Burnup Fuel Management with Dual Neutron Spectra][research_chong_2025]
- [Chong and Sagara 2026 A High-Temperature Gas-Cooled Reactor to Directly Reuse Spent Fuel][research_chong_2026]
- [Collins and McGurty 1960 High Temperature Cladding Alloys For Reactor Applications][research_collins_1960]
- [Comassar 1962 General Electric Direct-Air-Cycle Aircraft Nuclear Propulsion Program, Aircraft Nuclear Propulsion Application Studies (Comprehensive][research_comassar_1962]
- [Conn et al 1957 Progress Report-Fuel Element Task Force Applied Materials Research][research_conn_1957]
- [Connor 1960 Aerospace Nuclear Safety][research_connor_1960]
- [Conway 1956 FUEL ELEMENT DEVELOPMENT IN THE EXPERIMENTAL MECHANICAL ENGINEERING UNIT, MILESTONE IV, TASK 7511, General Engineering Development][research_conway_1956]
- [Cottrell 1951 Aircraft Nuclear Propulsion Project Quarterly Progress Report For Period Ending March 10, 1951][research_cottrell_1951]
- [Cottrell 1952 Aircraft Nuclear Propulsion Project Quarterly Progress Report For Period Ending December 10, 1951][research_cottrell_1952]
- [Cottrell 1952 Aircraft Nuclear Propulsion Project Quarterly Progress Report For Period Ending June 10, 1952][research_cottrell_1952_2]
- [Cottrell 1952 Aircraft Reactor Experiment Hazards Summary Report][research_cottrell_1952_3]
- [Cottrell 1953 Aircraft Nuclear Propulsion Project Quarterly Progress Report For Period Ending March 10, 1953][research_cottrell_1953]
- [Cottrell et al 1955 Operation Of The Aircraft Reactor Experiment][research_cottrell_1955_2]
- [Cottrell et al 1958 Disassembly And Postoperative Examination Of The Aircraft Reactor Experiment][research_cottrell_1958]
- [Creasman et al 2024 Fuel Depletion Study of the Molten Salt Demonstration Reactor][research_creasman_2024]
- [deGanahl et al 1954 Supercritical Water Reactor Shield Design Procedure][research_deganahl_1954]
- [Delgarm et al 2025 Multi-Criteria Optimization of a Nuclear Marine Propulsion System][research_delgarm_2025]
- [DeWitt and Benton 2024 Secondary Proton Buildup in Space Radiation Shielding][research_dewitt_2024]
- [Dibble 1958 Aircraft Nuclear Propulsion Department, Administrative Report][research_dibble_1958]
- [Domingos et al 2026 Neutronic Behavior of Alternative Fuels in a Microreactor Design][research_domingos_2026]
- [Dopchie et al 1958 BR-2, the maximum credible accident, Procedure and consequences][research_dopchie_1958]
- [Doyle 1948 Calculated Condenser Performance for a Mercury-Turbine Power Plant for Aircraft][research_doyle_1948]
- [Doyle 1951 Calculated performance of a mercury-compressor-jet powered airplane using a nuclear reactor as an energy source][research_doyle_1951]
- [Duan et al 2026 Reactivity Safety Analysis of an Air-Cooled Nuclear Thermal Propulsion Reactor][research_duan_2026]
- [Duncan 1958 The Calculation of Gamma-Ray Heating in Target Samples Located in the BSR Shield][research_duncan_1958]
- [Dunkle and Bogetic 2026 Molten Salt Reactor Loss of Flow Accident Analysis][research_dunkle_2026]
- [Edwards 1954 Effect Of Altitude And Flight Speed On Shielding Requirements][research_edwards_1954]
- [Edwards 1957 Specifications-Shielding Computer Programs 14-0, 14-1, And 14-2, Reactor Shield Analysis][research_edwards_1957]
- [Edwards and Simpson 1962 REACTOR AND SHIELD PHYSICS, Comprehensive Technical Report, General Electric Direct-Air-Cycle, Aircraft Nuclear Propulsion Program][research_edwards_1962]
- [Edwards et al 1958 Shielding Computer Program 04-0, Reactor Shield Analysis][research_edwards_1958]
- [Eggen et al 1961 Fast-neutron Spectra and Dose-rate Calculations][research_eggen_1961]
- [Elkhawas et al 2025 Deployment Study of Accident Tolerant Fuels in Small Modular Advanced Reactors][research_elkhawas_2025]
- [Falkenberry et al 1959 A Preliminary Study Of A Direct-Cycle Steam-Cooled Reactor For Merchant Ship Propulsion][research_falkenberry_1959]
- [Finger and Rom 1962 Nuclear Propulsion. State Of The Art - 1962][research_finger_1962]
- [Fischer and Bures 2024 Application of Modelica and TRANSFORM to System Modeling of the Molten Salt Reactor Experiment][research_fischer_2024]
- [Fraas and Savolainen 1954 ORNL Aircraft Nuclear Power Plant Designs][research_fraas_1954]
- [Frankfort 1956 A Conceptual Design Of A Shield Testing And Materials Irradiation Facility][research_frankfort_1956]
- [Fries 1958 Radiation-Resistant Motors For Nuclear Aircraft Controls][research_fries_1958]
- [Gaffin 1959 Nuclear J-58 Powerplant Weights, Dimensions, and Radiation Patterns][research_gaffin_1959]
- [Gamertsfelder 1954 Htre Hazards Report][research_gamertsfelder_1954]
- [Gardner 1958 Reactor Power Calculator][research_gardner_1958]
- [Gasser 1947 The Army Air Forces NEPA Project][research_gasser_1947]
- [Gates et al 1961 Development of Ceramic Fibers for Reinforcement in Composite Materials][research_gates_1961]
- [Gedwill et al 1965 Fuel-Retention Properties of Tungsten-Uranium Dioxide Composites][research_gedwill_1965]
- [Gilbert 1955 A Program for Investigation of Metallic Hydrides as Moderators, Reflectors, and Shields for Aircraft Reactors][research_gilbertjr_1955]
- [Gomaa and El-Tayebany 2026 Monte Carlo Study of Cadmium Oxide Effects on Borate Glass Shielding Performance][research_gomaa_2026]
- [Goodman 1948 Lexington Project Report #131, The Tolerance of Aerial Film to Nuclear Radiations][research_goodman_1948]
- [Gopalasingam et al 2025 Hydrogen Propulsion Technologies for Aviation, a Review][research_gopalasingam_2025]
- [Gorker 1955 Aircraft Reactor Control System Applicable To Turbojet And Turboprop Power Plants][research_gorker_1955]
- [Gotsky et al 1959 Two-Dimensional Diffusion Theory Analysis of Reactivity Effects of a Fuel-Plate-Removal Experiment][research_gotsky_1959]
- [Grimes et al 1958 Chemical Aspects of Molten Fluoride Reactors][research_grimes_1958]
- [Guilbaud et al 2024 Full Core Study of the KIWI-B-4E Nuclear Thermal Propulsion System][research_guilbaud_2024]
- [Ha and Kim 2025 Review of Radiation Effects in Semiconductors, Displacement Defects][research_ha_2025]
- [Haffner 1956 Duct Mockup Experiments At The Convair Ground Test Reactor][research_haffner_1956]
- [Haffner et al 1958 An Ibm 704 Program Report, Aircraft Nuclear Propulsion Shielding Program 10- 0][research_haffner_1958]
- [Han et al 2025 Design of New Shielding Materials for Space Reactor Shielding Structures][research_han_2025]
- [Han et al 2025 Optimization of Radiation Shielding Composite Materials][research_han_2025_2]
- [Hashim et al 2026 Multilayer Shields Buildup Factor for Gamma Ray Exposure][research_hashim_2026]
- [Hedden 1962 Design Criteria For Lithium-Cooled Reactor Experiment (Lcre) At Nrts][research_hedden_1962]
- [Henry 1958 Multilayer Shield Experiment Iv, Otf Iii][research_henry_1958]
- [Hobbs et al 1948 Lexington Project Report #129, Aircraft Configuration][research_hobbs_1948]
- [Holcomb 2025 Disruptive Thermal-Spectrum Molten Salt Breeder Reactor Fuel Cycle Technology][research_holcomb_2025]
- [Huang et al 2025 Shielding Optimization of a Heat Pipe Cooled Reactor][research_huang_2025]
- [Humble et al 1950 Preliminary analysis of three cycles for nuclear propulsion of aircraft][research_humble_1950]
- [Hutton et al 1952 Studies of Fourteen Nuclear-Powered Airplanes][research_hutton_1952]
- [Islam and Haque 2025 A Comparative Study and Design Optimization of Potential Cladding Materials][research_islam_2025]
- [Jagtap et al 2024 Conceptual Design Optimisation of a Subsonic Hydrogen-Powered Long-Range Aircraft][research_jagtap_2024]
- [Jiaju et al 2025 Verification of the Multi-Group Cross Section Generation Code ARES-MAC][research_jiaju_2025]
- [Jiang 2025 Design and Performance Study of Carbon-Containing Neutron Shielding Materials][research_jiang_2025]
- [Jiang et al 2026 Atomic-Scale Insights into Tritium Speciation and Interfacial Behaviour][research_jiang_2026]
- [Johnson 1960 Shield specification No, 1025, Reactor CRS-1018][research_johnson_1960]
- [Jordan et al 1957 Aircraft Nuclear Propulsion Program, Quarterly Progress Report for Period Ending December 31, 1956, Part 1 - 5][research_jordan_1957]
- [Jung et al 2025 Long Endurance Analysis of a Solar-Powered High Altitude Unmanned Aircraft][research_jung_2025]
- [Kam and Schamberger 1961 Military Compact Reactor Program Shield Study In The Ornl Lid Tank, Supplement][research_kam_1961]
- [Kang and Zu 2026 Gamma-Ray Buildup Factor Calculation via an Automated Machine Learning Framework][research_kang_2026]
- [Khan et al 2025 A Novel Neutron-Gamma Spectrum-Based Composite Shielding Material][research_khan_2025]
- [Kim and Lee 2026 Conceptual Design of a Marine Reactor Modernizing the ML-1 Architecture][research_kim_2026_2]
- [Kim and Macfarlane 2026 Challenges of Small Modular Reactors, A Comprehensive Exploration][research_kim_2026]
- [Klein 1948 Lexington Project Report #130, Meeting with Withington of Boeing Aircraft, Col, Demler of A, E, C, Washington, Col, Wassell and Col][research_klein_1948]
- [Krasnow et al 1959 The Behavior Of Fuels And Lubricants In Dynamic Test Equipment Operating In The Presence Of Gamma Radiation][research_krasnow_1959]
- [Kress 1958 Equipment Modifications For The Astr-Tsf Experiment][research_kress_1958]
- [Kuhlman and Glasgow 1957 Preliminary Report On Thermocouples For Fuel Element Plate Temperature And Control][research_kuhlman_1957]
- [Kumar et al 2025 A Robust Triple Node Upset Radiation Hardened Latch][research_kumar_2025]
- [Lan et al 2024 Internal Stress Analysis of Irradiated Graphite Cores in a Gas-Cooled Reactor][research_lan_2024]
- [Larson 1958 Pilot Radiator for Nuclear Ramjet Power Plant][research_larson_1958_3]
- [Larson 1958 Powerplant Performance for a Supersonic Nuclear Turbojet Powerplant][research_larson_1958_2]
- [Larson 1958 Reactor, Shield and Performance Data for a Nuclear Turbojet Powerplant][research_larson_1958]
- [Larson 1959 Advanced nuclear turbojet powerplant characteristics summary for supersonic aircraft][research_larson_1959]
- [Larson 1959 Pratt and Whitney Aircraft Nuclear JT-11 Turbojet Engine Performance with Advanced Nuclear System][research_larson_1959_2]
- [Lee 1958 Radiation Testing of Shield Specimen, Test Lth/Sub X/-4][research_lee_1958_2]
- [Lee 1958 Shield Weights for Boeing Mission for the PWAR-11 and the PWAR-X][research_lee_1958]
- [Lee and Cho 2025 Introducing a Radiation Target Level for the Shielding Design of a Nuclear System][research_lee_2025]
- [Level 1962 Metallic Fuel element Materials, Comprehensive Technical Report, General Electric Direct-Air-Cycle, Aircraft Nuclear Propulsion Program][research_level_1962]
- [Leverett and Beasley 1960 An Investigation Of Lens Opacity On Personnel Operating A Portable Nuclear Reactor][research_leverett_1960]
- [Levine and Ekern 1960 Radiation Effects On Electronic Systems, Designing Electronic Systems For Nuclear-Powered Aircraft Requires Knowing Response Of System][research_levine_1960]
- [Levine and Ekern 1961 Radiation Effects--a Major Influence in Designing Electronic Systems for Use in Nuclear-powered Aircraft, Paper 8 of Fourth Radiation][research_levine_1961]
- [Li 2024 A Review of Hydrogen-Powered Aircraft][research_li_2024]
- [Li et al 2026 Machine Learning Force Field Development and Physical Properties of Molten Salts][research_li_2026]
- [Li et al 2026 Thermodynamic Characteristics of Liquid Hydrogen Storage][research_li_2026_2]
- [Lindley 1956 On a Measure of the Information Provided by an Experiment][research_lindley_1956]
- [Liu and Chen 2026 Performance and Scalability of Hydrodynamic Fluoride Salt Lubrication][research_liu_2026_2]
- [Liu and Fu 2025 Decarbonizing Ocean Shipping Propulsion Power by Liquid Ammonia][research_liu_2025_3]
- [Liu and Liu 2025 Multiphysics Modelling of Three-Dimensional Aspherical TRISO Particle Fuel Performance][research_liu_2025_2]
- [Liu et al 2025 Single-Event Radiation Effects and Hardening Techniques][research_liu_2025]
- [Liu et al 2026 An Intelligent Method for Dual-Stage Radiation-Shielding Optimization][research_liu_2026]
- [Lu et al 2025 Exhaust Heat Recovery for Cryogenic Hydrogen-Powered Aircraft][research_lu_2025]
- [Ma et al 2026 Comparative Study of Power Control Methods for a Space Nuclear Electric System][research_ma_2026]
- [MacPherson 1960 Molten-Salt Reactors, Report for 1960 Ten-Year-Plan Evaluation][research_macpherson_1960]
- [Magnuson and Callihan 1956 Critical Experiments for a Proposed Tower Shielding Reactor][research_magnuson_1956]
- [Marjon 1957 Reactor Fuel Element Inspection][research_marjon_1957]
- [Matthia and Berger 2024 Radiation Exposure and Shielding Effects on the Lunar Surface][research_matthia_2024]
- [McFarlane 2024 Cradle to Grave, the Importance of the Fuel Cycle to Molten Salt Reactors][research_mcfarlane_2024]
- [McPherson 1957 Molten Salts For Civilian Power][research_mcpherson_1957]
- [Meem and Fairbanks 1956 Shielding Requirements for the Army Package Power Reactor][research_meem_1956]
- [Mendes and Tomal 2025 Charge Carrier Creation and Transport in Semiconductor Radiation Detectors][research_mendes_2025]
- [Menegus and Ring 1958 Accidental Dispersion Of Reactor Poisons And The Controlled Distance Required][research_menegus_1958]
- [Merriman and Chase 1955 Reflector Moderated Solid Fuel Element Sodium Cooled Reactor Critical Mass vs, Power Density][research_merriman_1955]
- [Meyer 1965 ANP Powerplant Data][research_meyer_1965]
- [Mishra et al 2024 Irradiated Fuel Salt Data Library for a Molten Salt Reactor][research_mishra_2024]
- [Mitchell 1954 Shield Design Calculations For Ac-Series Power Plants][research_mitchell_1954]
- [Mitsuboshi and Sagara 2025 Evaluation of Proliferation Resistance for Small and Medium Modular Reactors][research_mitsuboshi_2025]
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
- [Owston 2025 Assessment of a Novel Fuel Block and Core Arrangement for a Gas-Cooled Reactor][research_owston_2025]
- [Ozdemir et al 2025 Alternative Gamma-Ray Shielding Material, a Ternary Composite][research_ozdemir_2025]
- [Parisi and Arafat 2026 MARVEL Microreactor System Thermal-Hydraulic Design and Analysis][research_parisi_2026]
- [Paul et al 2025 Influence of Transmutation Products on the Thermophysical Properties of Fuel][research_paul_2025]
- [Peng et al 2024 Aircraft Lithium Battery Energy Balancing Method][research_peng_2024]
- [Peng et al 2025 Irradiated Thermal-Mechanical Coupling Performance of Fuel Elements][research_peng_2025]
- [Perry 1958 Technical Briefing for Aircraft Nuclear Propulsion Office Representatives on November 7 and 8, 1958][research_perry_1958]
- [Phelps 1961 Front shield weight and C, G][research_phelps_1961]
- [Poschmann et al 2025 Fuel Performance Simulations of TRISO Particle Geometries][research_poschmann_2025]
- [Quiroz et al 2025 Prospective Life Cycle Assessment of Sustainable Aviation Fuel Systems][research_quiroz_2025]
- [Rangel et al 2026 Conceptual Design of a Pressurized Water Microreactor Core Without Enriched Uranium][research_rangel_2026]
- [Reagan 1958 Radiation Testing of Shield Specimen, Test Lth/Sub X/-5 and 6][research_reagan_1958]
- [Redding 1948 Lexington Project Report # 24, Aircraft][research_redding_1948]
- [Reetz 1965 Second Symposium on Protection Against Radiations in Space][research_reetz_1965]
- [Ross 1960 Optimization Of Reactor Coolant Flow For The Aircraft Shield Test Reactor][research_ross_1960]
- [Ruffman 1952 Performance Parameters Pertinent to Nuclear Powered Aircraft][research_ruffman_1952]
- [Sampath and Kattimani 2025 Flutter Prediction for Unmanned Long Endurance Aircraft][research_sampath_2025]
- [Sasi et al 2025 Hydrogen and Ammonia Powered Turbofan Design Implications][research_sasi_2025]
- [Savage et al 1958 Components Of The Fused-Salt And Sodium Circuits Of The Aircraft Reactor Experiment][research_savage_1958]
- [Savic 1959 The Accident With The Zero Power Reactor On October 15, 1958][research_savic_1959]
- [Savolainen 1954 Aircraft Nuclear Propulsion Project Quarterly Progress Report For Period Ending September 10, 1954][research_savolainen_1954]
- [Savolainen 1955 Aircraft Nuclear Propulsion Project Quarterly Progress Report For Period Ending September 10, 1955][research_savolainen_1955]
- [Savolainen 1956 Aircraft Nuclear Propulsion Project Quarterly Progress Report For Period Ending June 10, 1956][research_savolainen_1956]
- [Savolainen 1956 Aircraft Nuclear Propulsion Project Quarterly Progress Report For Period Ending June 10, 1956][research_savolainen_1956_2]
- [Sayyed et al 2025 PSZB Glass as a Shielding Material, Physical, Mechanical, and Radiation Properties][research_sayyed_2025]
- [Schaeffer and Stokes 1958 Astr Fast Neutron Spectra][research_schaeffer_1958]
- [Schmickrath 1960 Engineering Proposal for Design and Development Work on a Nuclear Turbojet Propulsion Unit - Prepared for Aircraft Nuclear Propulsion Office][research_schmickrath_1960]
- [Schreiber 1956 LASL nuclear rocket propulsion program][research_schreiber_1956]
- [Schwartz 1952 An Analysis of Inert Gas Cooled Reactors for Application to Supersonic Nuclear Aircraft][research_schwartz_1952]
- [Schwartz 1953 Investigation of a Sodium Vapor Compressor Jet for Nuclear Propulsion of Aircraft][research_schwartz_1953]
- [Segaser 1948 The Determination Of Pressure Drop Factors Through Typical Fuel Element Channels For High Temperature Gas-Cooled Thermal Piles][research_segaser_1948]
- [Sekkat et al 2026 Energy-Dependent Shielding Performance of High-Z Epoxy Composite Shields][research_sekkat_2026]
- [Shannon 1948 A Mathematical Theory of Communication][research_shannon_1948]
- [Shobeiri et al 2025 Accelerating Small Modular Reactor Deployment and the Clean Energy Transition][research_shobeiri_2025]
- [Shoults 1948 Strategic Objectives - The Ability of Chemically Propelled Aircraft to Complete Missions Against Russian Targets][research_shoults_1948]
- [Shoults 1958 Test Of A Direct Cycle Nuclear Turbojet System][research_shoults_1958]
- [Smith et al 2026 Exergy Analysis of Kilopower Nuclear Reactor Systems for Lunar Power][research_smith_2026]
- [Soliman 2025 Energy-Dependent Neutron Removal Cross-Section][research_soliman_2025]
- [Stever 1948 Lexington Project Report # 0 - Minutes of meeting with representatives of the Army, Air Force, AEC, and NEPA -- The Need and Use of][research_stever_1948_2]
- [Stever 1948 Lexington Project Report #73, Minutes of Meeting Held May 12 and13, 1948 Between Representatives of NEPA and Project Lexington and AEC][research_stever_1948]
- [Stone et al 2024 Characterization of Aluminium and Boron Carbide Based Additively Manufactured Shielding][research_stone_2024]
- [Sun et al 2025 Calculation of Gamma-Ray Buildup Factors up to 100 Mean Free Paths by Monte Carlo][research_sun_2025_2]
- [Sun et al 2025 Preliminary Study on the Postulated Siting Accident Source Term][research_sun_2025]
- [Syarip et al 2025 Radiation Shielding Optimization of a Reactor Test Facility][research_syarip_2025]
- [Szekely 1961 A-136 Nuclear Turbo-Ram Power Plant (Invention Disclosures), Part I - Direct Cycle Aerospace Plane][research_szekely_1961]
- [Thornton and Blumberg 1961 ANP Htres Fulfill Test Goals][research_thornton_1961]
- [Tribus 1955 The Interpretation of Data Obtained on Shaped Wire Fuel Elements, Cover Carries Title, Interpretation of Thermodynamic Data on Advanced][research_tribus_1955]
- [Troubetzkoy and Kalos 1961 Military Compact Reactor Program Studies In The Synthesis Of Minimum Weight Shields][research_troubetzkoy_1961]
- [Wahler et al 2025 Conceptual Design and Aerostructural Trade-Offs in Hydrogen-Powered Aircraft][research_wahler_2025]
- [Waldrop 1958 Lithium hydride as a mobile neutron shield][research_waldrop_1958]
- [Welch 1961 Properties Of Lithium Hydride, Iii, Summary Of Ge-Anpd Data][research_welch_1961]
- [Wilks 1959 THE RELEASE OF FISSION PRODUCTS FROM REACTOR FUEL, A Literature Survey][research_wilks_1959]
- [Williams and Drake, The Research Airplane, Past, Present, and Future][research_williams_drake_1948]
- [Woodbridge 1955 Preliminary Htre No, 1 Project 100 Operation Manual 21, Reactor Assembly, Core "A"][research_woodbridge_1955]
- [Woods 1954 A Method For Calculating The Temperature Rise Of The Reactant Fluid Outside The Region Of A Turbulent Boundary Layer As A Function Of][research_woods_1954]
- [Woodsum and Rost 1957 Shield Weights][research_woodsum_1957]
- [Yang et al 2026 A Mixture of Experts Neural Network for Calculation of Gamma-Ray Buildup Factors][research_yang_2026]
- [Yavuzkanat and Sahmaran 2026 Radiation Shielding and Physical Properties of Zirconia-Modified Borosilicate Glass][research_yavuzkanat_2026]
- [Yildirim and Opcin 2026 Multilayer ZTA-Core Composite with Bio-Derived Coatings for Space Radiation Shielding][research_yildirim_2026]
- [Yilmaz et al 2025 Neutronic Analysis of a Thorium-Uranium Molten Salt Reactor with FLiBe Salt][research_yilmaz_2025]
- [Zhang et al 2026 A Rigorous Method for Multi-Scale Coupling of Pebble Bed and Fuel Element][research_zhang_2026_2]
- [Zhang et al 2026 Crashworthiness Design of Hydrogen-Powered Regional Aircraft][research_zhang_2026]
- [Zhang et al 2026 Startup Model of a High Temperature Heat Pipe Applied to a Heat Pipe Reactor][research_zhang_2026_3]
- [Zheng et al 2026 Effects of TRISO-Matrix Interactions on TRISO Fuel Performance][research_zheng_2026]

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
[research_aec_1948]: https://www.osti.gov/biblio/969803
[research_aec_1949]: https://www.osti.gov/biblio/970750
[research_aec_1950]: https://www.osti.gov/biblio/969642
[research_aec_1950_2]: https://www.osti.gov/biblio/129477
[research_aec_1954]: https://www.osti.gov/biblio/4346671
[research_aec_1956]: https://www.osti.gov/biblio/4291620
[research_aec_1957]: https://www.osti.gov/biblio/4155584
[research_aec_1957_2]: https://www.osti.gov/biblio/4781700
[research_aec_1957_3]: https://www.osti.gov/biblio/4792703
[research_aec_1957_4]: https://www.osti.gov/biblio/1470987
[research_aec_1958]: https://www.osti.gov/biblio/4313685
[research_aec_1959]: https://www.osti.gov/biblio/4643464
[research_aec_1959_2]: https://www.osti.gov/biblio/12393730
[research_aec_1959_3]: https://www.osti.gov/biblio/4581034
[research_aec_1959_4]: https://www.osti.gov/biblio/4142437
[research_aec_1959_6]: https://www.osti.gov/biblio/4176154
[research_aec_1961]: https://www.osti.gov/biblio/4095728
[research_aguiar_2026]: https://doi.org/10.3390/electronics15091903
[research_ahmed_2026]: https://doi.org/10.1016/j.radphyschem.2025.113544
[research_alnuaimi_2026]: https://doi.org/10.1016/j.pnucene.2026.106467
[research_alvis_1957]: https://www.osti.gov/biblio/1068544
[research_ancona_2025]: https://doi.org/10.1007/s42496-025-00281-5
[research_anderson_1952]: https://www.osti.gov/biblio/4813839
[research_antonakis_2026]: https://doi.org/10.2514/1.c038389
[research_aueron_2024]: https://doi.org/10.2514/1.a35805
[research_auslender_1957]: https://www.osti.gov/biblio/4333843
[research_bali_2025]: https://doi.org/10.1016/j.nucengdes.2025.113952
[research_bardon_2025]: https://doi.org/10.1016/j.jenvman.2024.123943
[research_bauerlein_1959]: https://www.osti.gov/biblio/4276643
[research_beever_1965]: https://ntrs.nasa.gov/citations/19650025019
[research_bendall_1959]: https://www.osti.gov/biblio/4245933
[research_bettis_1957]: https://www.osti.gov/biblio/4316237
[research_bhardwaj_2024]: https://doi.org/10.3389/fnuen.2024.1352667
[research_bigelow_1957]: https://www.osti.gov/biblio/4729439
[research_bigelow_1957_2]: https://www.osti.gov/biblio/4745688
[research_blizard_1953]: https://www.osti.gov/biblio/4107755
[research_blizard_1958]: https://www.osti.gov/biblio/4300525
[research_bloomfield_1959]: https://www.osti.gov/biblio/4224678
[research_blosser_1958]: https://www.osti.gov/biblio/4312376
[research_bolt_1958]: https://www.osti.gov/biblio/4325443
[research_bolukbasi_2026]: https://doi.org/10.1016/j.pnucene.2025.106220
[research_boppart_1957]: https://www.osti.gov/biblio/1063980
[research_briant_1957]: https://www.osti.gov/biblio/4322654
[research_buckingham_1914]: https://doi.org/10.1103/physrev.4.345
[research_butterfield_1956]: https://www.osti.gov/biblio/4829557
[research_butz_1959]: https://www.osti.gov/biblio/4224171
[research_cannon_1961]: https://www.osti.gov/biblio/4842854
[research_capo_1957]: https://www.osti.gov/biblio/4293076
[research_casper_1958]: https://www.osti.gov/biblio/4203323
[research_cavicchi_1959]: https://ntrs.nasa.gov/citations/19630010644
[research_cernak_1960]: https://www.osti.gov/biblio/4165502
[research_cernak_1960_2]: https://www.osti.gov/biblio/4786880
[research_cetegen_2025]: https://doi.org/10.1016/j.energy.2025.138469
[research_chaloner_verdinelli_1995]: https://doi.org/10.1214/ss/1177009939
[research_chandler_1957]: https://www.osti.gov/biblio/4791808
[research_chandler_2025]: https://doi.org/10.1016/j.anucene.2024.110920
[research_chapman_1955]: https://www.osti.gov/biblio/2565420
[research_chen_2025]: https://doi.org/10.1080/00295639.2025.2567731
[research_chen_2025_2]: https://doi.org/10.3390/en18030670
[research_cheng_2025]: https://doi.org/10.1016/j.nucengdes.2025.114548
[research_chong_2025]: https://doi.org/10.15669/pnst.7.47
[research_chong_2026]: https://doi.org/10.1080/00295450.2025.2593803
[research_collins_1960]: https://www.osti.gov/biblio/4756862
[research_comassar_1962]: https://www.osti.gov/biblio/1048126
[research_conn_1957]: https://www.osti.gov/biblio/4808952
[research_connor_1960]: https://www.osti.gov/biblio/4819884
[research_conway_1956]: https://www.osti.gov/biblio/4798853
[research_cottrell_1951]: https://www.osti.gov/biblio/4137126
[research_cottrell_1952]: https://www.osti.gov/biblio/4139314
[research_cottrell_1952_2]: https://www.osti.gov/biblio/4782915
[research_cottrell_1952_3]: https://www.osti.gov/biblio/4704625
[research_cottrell_1953]: https://www.osti.gov/biblio/4745448
[research_cottrell_1955_2]: https://www.osti.gov/biblio/4237975
[research_cottrell_1958]: https://www.osti.gov/biblio/4223435
[research_creasman_2024]: https://doi.org/10.1016/j.nucengdes.2023.112881
[research_deganahl_1954]: https://www.osti.gov/biblio/4704905
[research_delgarm_2025]: https://doi.org/10.1080/00295450.2025.2507976
[research_dewitt_2024]: https://doi.org/10.1016/j.lssr.2024.02.005
[research_dibble_1958]: https://www.osti.gov/biblio/10202216
[research_domingos_2026]: https://doi.org/10.1016/j.nucengdes.2026.115072
[research_dopchie_1958]: https://www.osti.gov/biblio/4274334
[research_doyle_1948]: https://ntrs.nasa.gov/citations/20050019308
[research_doyle_1951]: https://ntrs.nasa.gov/citations/19930086702
[research_duan_2026]: https://doi.org/10.1016/j.jandt.2026.03.002
[research_duncan_1958]: https://www.osti.gov/biblio/4281089
[research_dunkle_2026]: https://doi.org/10.12688/nuclscitechnolopenres.17459.2
[research_edwards_1954]: https://www.osti.gov/biblio/4801695
[research_edwards_1957]: https://www.osti.gov/biblio/4808209
[research_edwards_1958]: https://www.osti.gov/biblio/4326622
[research_edwards_1962]: https://www.osti.gov/biblio/4491615
[research_eggen_1961]: https://www.osti.gov/biblio/4025545
[research_elkhawas_2025]: https://doi.org/10.1088/1402-4896/ae05d3
[research_falkenberry_1959]: https://www.osti.gov/biblio/4231710
[research_finger_1962]: https://ntrs.nasa.gov/citations/19630007351
[research_fischer_2024]: https://doi.org/10.1016/j.nucengdes.2023.112768
[research_fraas_1954]: https://www.osti.gov/biblio/12772844
[research_frankfort_1956]: https://www.osti.gov/biblio/4271963
[research_fries_1958]: https://www.osti.gov/biblio/4300515
[research_gaffin_1959]: https://www.osti.gov/biblio/12086782
[research_gamertsfelder_1954]: https://www.osti.gov/biblio/4805552
[research_gardner_1958]: https://www.osti.gov/biblio/4308240
[research_gasser_1947]: https://www.osti.gov/biblio/129218
[research_gates_1961]: https://ntrs.nasa.gov/citations/20150019696
[research_gedwill_1965]: https://ntrs.nasa.gov/citations/19730064642
[research_gilbertjr_1955]: https://www.osti.gov/biblio/1240148
[research_gomaa_2026]: https://doi.org/10.1016/j.apradiso.2026.112512
[research_goodman_1948]: https://www.osti.gov/biblio/969792
[research_gopalasingam_2025]: https://doi.org/10.3390/hydrogen6040092
[research_gorker_1955]: https://www.osti.gov/biblio/4822720
[research_gotsky_1959]: https://ntrs.nasa.gov/citations/19980228446
[research_grimes_1958]: https://www.osti.gov/biblio/4305506
[research_guilbaud_2024]: https://doi.org/10.1016/j.nucengdes.2024.113639
[research_ha_2025]: https://doi.org/10.1109/edr.2025.3649435
[research_haffner_1956]: https://www.osti.gov/biblio/4813405
[research_haffner_1958]: https://www.osti.gov/biblio/4225992
[research_han_2025]: https://doi.org/10.1109/access.2025.3610902
[research_han_2025_2]: https://doi.org/10.1109/tns.2025.3558902
[research_hashim_2026]: https://doi.org/10.47831/mjpas.v4i2.333
[research_hedden_1962]: https://www.osti.gov/biblio/4728141
[research_henry_1958]: https://www.osti.gov/biblio/4071097
[research_hobbs_1948]: https://www.osti.gov/biblio/969790
[research_holcomb_2025]: https://doi.org/10.1016/j.nucengdes.2025.114303
[research_huang_2025]: https://doi.org/10.1016/j.pnucene.2025.105763
[research_humble_1950]: https://ntrs.nasa.gov/citations/19930086366
[research_hutton_1952]: https://www.osti.gov/biblio/969600
[research_islam_2025]: https://doi.org/10.1016/j.pnucene.2025.105741
[research_jagtap_2024]: https://doi.org/10.1016/j.ijhydene.2024.11.331
[research_jiaju_2025]: https://doi.org/10.1016/j.radphyschem.2025.112849
[research_jiang_2025]: https://doi.org/10.54691/y3z9ma42
[research_jiang_2026]: https://doi.org/10.1016/j.ijhydene.2026.156188
[research_johnson_1960]: https://www.osti.gov/biblio/5146009
[research_jordan_1957]: https://www.osti.gov/biblio/1373535
[research_jung_2025]: https://doi.org/10.5139/jksas.2025.53.5.527
[research_kam_1961]: https://www.osti.gov/biblio/4532885
[research_kang_2026]: https://doi.org/10.1016/j.anucene.2025.111971
[research_khan_2025]: https://doi.org/10.1016/j.nucengdes.2025.114215
[research_kim_2026]: https://doi.org/10.1016/j.pnucene.2025.105989
[research_kim_2026_2]: https://doi.org/10.1016/j.nucengdes.2026.114908
[research_klein_1948]: https://www.osti.gov/biblio/969791
[research_krasnow_1959]: https://www.osti.gov/biblio/4221826
[research_kress_1958]: https://www.osti.gov/biblio/4310182
[research_kuhlman_1957]: https://www.osti.gov/biblio/4791846
[research_kumar_2025]: https://doi.org/10.1016/j.aeue.2025.155977
[research_lan_2024]: https://doi.org/10.1016/j.nucengdes.2024.113647
[research_larson_1958]: https://www.osti.gov/biblio/12376890
[research_larson_1958_2]: https://www.osti.gov/biblio/12393299
[research_larson_1958_3]: https://www.osti.gov/biblio/1048129
[research_larson_1959]: https://www.osti.gov/biblio/1245002
[research_larson_1959_2]: https://www.osti.gov/biblio/12086630
[research_lee_1958]: https://www.osti.gov/biblio/1046040
[research_lee_1958_2]: https://www.osti.gov/biblio/4684477
[research_lee_2025]: https://doi.org/10.1016/j.pnucene.2025.105947
[research_level_1962]: https://www.osti.gov/biblio/12475098
[research_leverett_1960]: https://www.osti.gov/biblio/4195946
[research_levine_1960]: https://www.osti.gov/biblio/4192956
[research_levine_1961]: https://www.osti.gov/biblio/4070513
[research_li_2024]: https://doi.org/10.37394/23202.2024.23.43
[research_li_2026]: https://doi.org/10.1039/d6cp01382a
[research_li_2026_2]: https://doi.org/10.1016/j.applthermaleng.2026.131139
[research_lindley_1956]: https://doi.org/10.1214/aoms/1177728069
[research_liu_2025]: https://doi.org/10.1007/s10825-025-02376-5
[research_liu_2025_2]: https://doi.org/10.1016/j.nucengdes.2025.113880
[research_liu_2025_3]: https://doi.org/10.1016/j.jclepro.2024.144462
[research_liu_2026]: https://doi.org/10.1016/j.pnucene.2025.106098
[research_liu_2026_2]: https://doi.org/10.3390/jne7010011
[research_lu_2025]: https://doi.org/10.1016/j.eng.2025.12.013
[research_ma_2026]: https://doi.org/10.1016/j.energy.2026.141802
[research_macpherson_1960]: https://www.osti.gov/biblio/1341875
[research_magnuson_1956]: https://www.osti.gov/biblio/4361517
[research_marjon_1957]: https://www.osti.gov/biblio/4356988
[research_matthia_2024]: https://doi.org/10.1029/2024sw004095
[research_mcfarlane_2024]: https://doi.org/10.3389/fnuen.2024.1335980
[research_mcpherson_1957]: https://www.osti.gov/biblio/4314626
[research_meem_1956]: https://www.osti.gov/biblio/4337928
[research_mendes_2025]: https://doi.org/10.1016/j.radphyschem.2024.112437
[research_menegus_1958]: https://www.osti.gov/biblio/4350588
[research_merriman_1955]: https://www.osti.gov/biblio/1001781
[research_meyer_1965]: https://www.osti.gov/biblio/1048071
[research_mishra_2024]: https://doi.org/10.1016/j.dib.2023.109817
[research_mitchell_1954]: https://www.osti.gov/biblio/4817598
[research_mitsuboshi_2025]: https://doi.org/10.15669/pnst.7.318
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
[research_owston_2025]: https://doi.org/10.1016/j.nucengdes.2025.114040
[research_ozdemir_2025]: https://doi.org/10.1016/j.net.2025.103512
[research_parisi_2026]: https://doi.org/10.1080/00295450.2026.2678096
[research_paul_2025]: https://doi.org/10.1016/j.jnucmat.2024.155572
[research_peng_2024]: https://doi.org/10.1016/j.est.2024.112714
[research_peng_2025]: https://doi.org/10.1016/j.pnucene.2025.105633
[research_perry_1958]: https://www.osti.gov/biblio/993074
[research_phelps_1961]: https://www.osti.gov/biblio/946508
[research_poschmann_2025]: https://doi.org/10.1016/j.jnucmat.2025.155714
[research_quiroz_2025]: https://doi.org/10.1021/acs.est.5c09113
[research_rangel_2026]: https://doi.org/10.1016/j.nucengdes.2026.114923
[research_reagan_1958]: https://www.osti.gov/biblio/4692883
[research_redding_1948]: https://www.osti.gov/biblio/969761
[research_reetz_1965]: https://ntrs.nasa.gov/citations/19650024974
[research_ross_1960]: https://www.osti.gov/biblio/4080402
[research_ruffman_1952]: https://www.osti.gov/biblio/1015812
[research_sampath_2025]: https://doi.org/10.1177/09544100251362517
[research_sasi_2025]: https://doi.org/10.1115/1.4066433
[research_savage_1958]: https://www.osti.gov/biblio/4308571
[research_savic_1959]: https://www.osti.gov/biblio/4255352
[research_savolainen_1954]: https://www.osti.gov/biblio/4121762
[research_savolainen_1955]: https://www.osti.gov/biblio/4164238
[research_savolainen_1956]: https://www.osti.gov/biblio/4776381
[research_savolainen_1956_2]: https://www.osti.gov/biblio/4137101
[research_sayyed_2025]: https://doi.org/10.1016/j.oceram.2024.100729
[research_schaeffer_1958]: https://www.osti.gov/biblio/4276461
[research_schmickrath_1960]: https://www.osti.gov/biblio/12377075
[research_schreiber_1956]: https://www.osti.gov/biblio/7365651
[research_schwartz_1952]: https://www.osti.gov/biblio/1346710
[research_schwartz_1953]: https://www.osti.gov/biblio/966690
[research_segaser_1948]: https://www.osti.gov/biblio/4350744
[research_sekkat_2026]: https://doi.org/10.1016/j.apradiso.2026.112793
[research_shannon_1948]: https://doi.org/10.1002/j.1538-7305.1948.tb01338.x
[research_shobeiri_2025]: https://doi.org/10.3390/su17083406
[research_shoults_1948]: https://www.osti.gov/biblio/969672
[research_shoults_1958]: https://www.osti.gov/biblio/4315621
[research_smith_2026]: https://doi.org/10.1115/1.4072412
[research_soliman_2025]: https://doi.org/10.1016/j.anucene.2024.111171
[research_stever_1948]: https://www.osti.gov/biblio/969767
[research_stever_1948_2]: https://www.osti.gov/biblio/1471204
[research_stone_2024]: https://doi.org/10.1016/j.matdes.2023.112463
[research_sun_2025]: https://doi.org/10.1016/j.jandt.2025.04.006
[research_sun_2025_2]: https://doi.org/10.1016/j.radphyschem.2025.112696
[research_syarip_2025]: https://doi.org/10.24996/ijs.2025.66.3.8
[research_szekely_1961]: https://www.osti.gov/biblio/1821648
[research_thornton_1961]: https://www.osti.gov/biblio/4120083
[research_tribus_1955]: https://www.osti.gov/biblio/4840356
[research_troubetzkoy_1961]: https://www.osti.gov/biblio/4517145
[research_wahler_2025]: https://doi.org/10.3390/aerospace12020077
[research_waldrop_1958]: https://www.osti.gov/biblio/4468486
[research_welch_1961]: https://www.osti.gov/biblio/4813232
[research_wilks_1959]: https://www.osti.gov/biblio/4813404
[research_williams_drake_1948]: https://ntrs.nasa.gov/citations/19650070849
[research_woodbridge_1955]: https://www.osti.gov/biblio/4813340
[research_woods_1954]: https://www.osti.gov/biblio/4797190
[research_woodsum_1957]: https://www.osti.gov/biblio/991705
[research_yang_2026]: https://doi.org/10.1016/j.anucene.2026.112245
[research_yavuzkanat_2026]: https://doi.org/10.1016/j.radphyschem.2026.113698
[research_yildirim_2026]: https://doi.org/10.1016/j.asr.2026.05.076
[research_yilmaz_2025]: https://doi.org/10.1016/j.pnucene.2025.105614
[research_zhang_2026]: https://doi.org/10.1016/j.est.2025.119987
[research_zhang_2026_2]: https://doi.org/10.1016/j.pnucene.2025.106055
[research_zhang_2026_3]: https://doi.org/10.3724/j.0253-3219.2026.hjs.49.250360
[research_zheng_2026]: https://doi.org/10.1016/j.nucengdes.2026.114811
