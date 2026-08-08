---
layout: post
mathjax: true
comments: true
title: "X-Planes: Lockheed X-17"
date: 2025-10-23 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 18
---

<!-- A314 -->
<script>console.log("A314");</script>

The [Lockheed X-17][ref_x17] went up, turned over, and fired two rocket stages **downward**. That is a strange thing to do to a rocket, and everything worth saying about the vehicle follows from why it was necessary. This article is the eighteenth in the [X-Planes series][related_post_a297_xplanes_framing], following the [X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], the [X-4][related_post_a301_northrop_x4], the [X-5][related_post_a302_bell_x5], the [X-6][related_post_a303_convair_x6], the [X-7][related_post_a304_lockheed_x7], the [X-8][related_post_a305_aerojet_x8], the [X-9][related_post_a306_bell_x9], the [X-10][related_post_a307_north_american_x10], the [X-11][related_post_a308_convair_x11], the [X-12][related_post_a309_convair_x12], the [X-13][related_post_a310_ryan_x13], the [X-14][related_post_a311_bell_x14], the [X-15][related_post_a312_north_american_x15], and the [X-16][related_post_a313_bell_x16].

In 1954 nobody knew what happened to an intercontinental ballistic missile warhead when it came back into the atmosphere. That was not a gap in the theory. It was a gap in the ability to produce the condition at all. No wind tunnel could make air that energetic, no ground facility could hold it for long enough, and dropping something from as high as anyone could reach did not produce anything like the right speed. **The X-17 exists because the only remaining way to obtain the condition was to build a vehicle that manufactured it in flight.**

The standard inventory entry remains [Jenkins Landis and Miller 2003 American X-Vehicles, An Inventory X-1 to X-50][book_jenkins_landis_miller_2003] and the vehicle compilation is [Miller 2001 The X-Planes, X-1 to X-45][book_miller_2001]. The programme context is [Neufeld 1990 The Development of Ballistic Missiles in the United States Air Force][book_neufeld_1990], and the physics throughout is that of [Anderson 2019 Hypersonic and High-Temperature Gas Dynamics][book_anderson_2019].

## The Research Question

The obvious statement of the question is how a nose cone survives re-entry. That is the motivation rather than the question, because it does not say what had to be measured or why measuring it was hard.

### The Keystone Is What a Test Range Can and Cannot Reproduce

**The keystone is partial simulation.** A re-entry is not one condition but several simultaneous ones, and a test vehicle can match some of them and must abandon the rest. Which ones it matches is a design decision, and the value of the resulting data depends entirely on whether the abandoned ones mattered for the question being asked.

Three quantities have to be right at once for a full reproduction.

**The velocity**, because the energy per unit mass of the oncoming air is one half of the velocity squared, and that energy is what dissociates and ionises the gas. Velocity sets the chemistry.

**The heating rate**, because that is what the structure has to survive, and it depends on density as well as velocity.

**The degree of chemical nonequilibrium**, because the gas may or may not have time to reach equilibrium while crossing the shock layer, and which of those is true changes the heat transfer.

**A test vehicle has two things it can adjust, namely the altitude it flies at and the size of the article it carries. Two adjustments cannot satisfy three conditions.** One requirement must be surrendered, and the whole article is an account of which one the X-17 gave up and what that cost.

### Why This Was the Binding Unknown in 1954

The ground facilities of the period could not close the gap. A shock tube produces high enthalpy for microseconds, and the expansion tube that improved on it was not proposed until [Trimpi 1962][research_trimpi_1962]. An arc-heated jet can run for minutes but produces a contaminated, non-uniform stream whose enthalpy is hard to know, and calibrating one against material response was still being worked out in [Chapman 1963][research_chapman_1963]. A ballistic range fires a small model at high speed through still air, which is genuinely a re-entry in miniature, but the model is centimetres across and the flight lasts milliseconds, as in [Yee et al 1961][research_yee_1961]. Free-flight technique in a conventional tunnel, treated in [Dayman 1962][research_dayman_1962] and [Levy and Mc Devitt 1964][research_levy_mc_devitt_1964], has the same limitation.

None of that gives a full-scale article, in real air, for tens of seconds. **The X-17 was built to obtain exactly the thing no facility could provide, and the vehicle's peculiar architecture is a direct consequence of that requirement rather than of any preference for rockets.**

## Programme Origin

The requirement came from the Air Force ballistic missile programme, which by 1954 was moving quickly toward the Atlas and needed to know what shape a warhead should be. The problem was acute because the answer was counterintuitive. A missile designer's instinct is that a sharp body is better, since sharp bodies have less drag, and less drag had been the right answer for every previous flight regime.

For a re-entering body it is the wrong answer, and the reason was established by Allen and Eggers at the National Advisory Committee for Aeronautics. **A blunt body pushes a detached bow shock ahead of itself and dumps most of the kinetic energy into the air rather than into the vehicle.** A sharp body carries a shock attached to its own nose and heats itself. The theory is compactly presented in [Eggers et al 1958][research_eggers_1958], published after the X-17 had already flown.

That is the origin of the tension the programme resolved. **The theory said blunt. Nobody had flown it. The X-17 was built to settle the question with hardware.**

### The Vehicle

Sources give the X-17 as a three-stage solid-propellant rocket of 40 feet 4 inches in length and 10,650 pounds at launch, though some accounts give 41 feet. The first stage is a Thiokol XM20 Sergeant of 48,000 pounds force, the second is a cluster of three Thiokol XM19 Recruit motors at 33,900 pounds force each, and the third is a single XM19E1 Recruit at 35,950 pounds force. Diameters step down from 2 feet 7 inches to 1 foot 5 inches to 9.7 inches.

**The flight profile is the design.** The first stage lifts the vehicle to roughly 17 miles and burns out. The vehicle then coasts unpowered to apogee, tips over, and falls. On the way down the second stage fires, burns out, separates, and the third stage fires, driving the nose cone into progressively denser air. The peak speed reported is Mach 14.5, and on 24 April 1957 a flight reached 9,000 miles per hour.

The downward velocity the upper stages must supply follows from the rocket equation,

$$\Delta v = I_{sp}\, g_0 \ln\frac{m_0}{m_1}$$

and at a period-typical solid specific impulse of 235 seconds the 2,339 metres per second computed below requires

$$\frac{m_0}{m_1} = \exp\left(\frac{2{,}339}{235 \times 9.807}\right) = 2.759$$

or **63.8 percent propellant by mass** in the descending stack. That is an ordinary figure for a solid motor and is why the architecture was practical at all rather than merely conceivable.

**Published apogees disagree, and not slightly.** One account gives about 100 miles, another about 500,000 feet, and a third 250 miles. The first two agree to within five kilometres. The third is two and a half times the first. This article computes across the range where the answer depends on it and says so.

## Sizing From First Principles

### The Atmosphere

The standard model is used throughout, with pressure in the isothermal layer following

$$p(z) = p_{11} \exp\left(-\frac{g_0 (z - z_{11})}{R T_{11}}\right)$$

and density from the ideal gas law,

$$\rho = \frac{p}{R T}$$

The two densities that matter below are $\rho = 0.008214$ kilogrammes per cubic metre at 35 kilometres, which is a representative intercontinental peak-heating altitude, and $\rho = 0.2278$ at 13.97 kilometres, which is where the X-17's condition lands.

### Part One, Falling Is Not Enough

The first thing to establish is that the downward stages were necessary rather than merely convenient. A body released at apogee and allowed to fall converts height into speed, and neglecting drag entirely, which is generous to the falling case,

$$v_{\text{ff}} = \sqrt{2 g \Delta h}$$

Taking the lower published apogee of 160.9 kilometres and a target altitude of 15 kilometres,

$$v_{\text{ff}} = \sqrt{2 \times 9.72 \times 145{,}900} = 1{,}684\ \text{m/s}$$

which is Mach 5.71. The achieved speed was 4,023 metres per second, so the ratio in speed is

$$\frac{v_{\text{achieved}}}{v_{\text{ff}}} = \frac{4{,}023}{1{,}684} = 2.389$$

**That factor of 2.4 in speed is not the interesting number. Convective heating goes as the cube of speed**, so the ratio that matters is

$$\left(\frac{v_{\text{achieved}}}{v_{\text{ff}}}\right)^{3} = 2.389^{3} = 13.63$$

**Firing the stages downward multiplies the heating rate by nearly fourteen.** A vehicle that merely fell from the same apogee would have produced less than a tenth of the thermal condition it was built to study, which would have been useless. The downward stages are not an enhancement of the experiment. They are the experiment.

The velocity they must supply, over and above what gravity gives, is

$$\Delta v = 4{,}023 - 1{,}684 = 2{,}339\ \text{m/s}$$

neglecting drag during the burn, which makes this a lower bound.

Even the largest published apogee does not rescue the falling case. From 402 kilometres, free fall reaches 2,744 metres per second, which is Mach 9.30 and still only

$$\left(\frac{4{,}023}{2{,}744}\right)^{3} = 3.15$$

times short in heating. **The conclusion that the stages were necessary does not depend on which apogee figure is correct**, which is worth stating given that the sources disagree.

### The Trajectory the Vehicle Is Simulating a Point On

Before comparing conditions it is worth writing down what is being compared to. Allen and Eggers solved ballistic entry into an exponential atmosphere in closed form. With $\rho = \rho_0 e^{-z/H}$ at a constant flight path angle $\gamma$ and a ballistic coefficient $\beta = m/(C_D A)$,

$$V(z) = V_e \exp\left[-\frac{\rho_0 H}{2 \beta \sin\gamma} e^{-z/H}\right]$$

Two consequences follow immediately and neither depends on the vehicle. The peak deceleration is

$$a_{\max} = \frac{V_e^{2} \sin\gamma}{2 e H}$$

which contains **no ballistic coefficient at all**, so every ballistic entry at a given speed and angle pulls the same peak load. At a 20 degree entry angle and 7,000 metres per second that is 43.7 g. And the velocity at peak heating is

$$V_{\dot{q},\max} = V_e e^{-1/6} = 0.8465\, V_e = 5{,}925\ \text{m/s}$$

again independent of $\beta$. **What the ballistic coefficient controls is the altitude at which all of this happens**, and that is the whole of the blunt-body argument stated quantitatively.

| Ballistic coefficient, kg/m² | Altitude of peak heating, km |
|---|---|
| 1,000 | 31.3 |
| 2,000 | 26.3 |
| 4,195 | 21.0 |
| 13,983 | 12.3 |

**A blunt body has its worst moment nineteen kilometres higher than a slender one**, in air a factor of twenty thinner, which is why it survives.

**The important structural point for this article is that a re-entry is a curve and not a condition.** The heating rate rises, peaks, and falls, and the vehicle lives through all of it. The X-17 manufactures one point on that curve and holds it briefly. Everything below about matching should be read with that in mind.

### Part Two, What Can Be Traded

Stagnation-point convective heating is given by the Sutton and Graves correlation,

$$\dot{q} = K \sqrt{\frac{\rho}{R_n}}\, V^{3}$$

where $R_n$ is the nose radius and $K = 1.7415 \times 10^{-4}$ in SI units. The structure of that relation is the whole opportunity. **Density enters under a square root and velocity enters cubed**, so a deficit in velocity can be repaid by an excess of density, and the exchange rate is steep. Holding the heating rate fixed,

$$\rho \propto V^{-6}$$

Taking a representative intercontinental condition of 7,000 metres per second and the X-17's 4,023, the velocity ratio is 1.740, so the required density ratio is

$$\left(\frac{7{,}000}{4{,}023}\right)^{6} = 27.74$$

The X-17 must therefore fly where the air is nearly twenty-eight times denser, which is

$$\rho = 27.74 \times 0.008214 = 0.2278\ \text{kg/m}^{3}$$

and that density occurs at **13.97 kilometres**. Evaluating both conditions at a nose radius of 0.15 metres gives

$$\dot{q} = 1.7415 \times 10^{-4} \sqrt{\frac{0.008214}{0.15}} \times 7{,}000^{3} = 1{,}398\ \text{W/cm}^{2}$$

for the intercontinental case and the same 1,398 watts per square centimetre for the X-17, which agrees by construction. **The X-17 could reproduce an intercontinental heating rate at 57 percent of the velocity by flying at a tenth of the altitude, and that is the trick the whole vehicle exists to perform.**

### The Reference Condition Is a Choice, and Deriving It Exposes a Limit

The 7,000 metres per second at 35 kilometres used above is representative rather than derived, and the trajectory solution allows it to be derived instead. Taking the Allen-Eggers peak-heating point for a given ballistic coefficient and asking what altitude the X-17 would need in order to match it gives the following.

| Ballistic coefficient, kg/m² | Reference peak, W/cm² | Altitude X-17 needs, km |
|---|---|---|
| 1,000 | 1,135 | 16.62 |
| 1,453 | 1,398 | 13.97 |
| 2,000 | 1,674 | 11.68 |
| 4,195 | 2,563 | 4.63 |
| 8,000 | 3,705 | **impossible** |
| 13,983 | 5,087 | **impossible** |

**The assumed reference corresponds to a ballistic coefficient of 1,453 kilogrammes per square metre**, which is a blunt, light body. That is not a coincidence and it was not stated in the choosing. It is exactly the class of re-entry vehicle the X-17 was built to test.

The rows marked impossible are the finding. The X-17 cannot produce more heating than it produces at its lowest altitude,

$$\dot{q}_{\max} = K \sqrt{\frac{\rho_{\text{SL}}}{R_n}}\, V^{3} = 3{,}241\ \text{W/cm}^{2}$$

at sea level, and 1,881 watts per square centimetre at a more realistic 10 kilometre floor. Above a ballistic coefficient of about **6,300 kilogrammes per square metre even at sea level, and about 2,500 at a practical floor, no altitude exists at which the X-17 matches the heating rate at all.**

**So the heating-rate match is not a general capability of the vehicle. It is conditional on the class of body being simulated.** The X-17 could reproduce the thermal environment of a blunt first-generation re-entry vehicle and could not have reproduced that of a dense slender one, because its velocity is simply too low and no amount of flying lower repairs that. The technique and the vehicle were fitted to each other, and when re-entry vehicles later became slender and dense the technique stopped applying.

### Part Three, What Cannot Be Traded

Stagnation enthalpy is the energy per unit mass the oncoming air brings,

$$h_0 = \frac{V^{2}}{2}$$

and there is **no density in it at all**. Evaluating,

$$h_{0,\text{X-17}} = \frac{4{,}023^{2}}{2} = 8.094\ \text{MJ/kg}$$

against the reference condition,

$$h_{0,\text{ICBM}} = \frac{7{,}000^{2}}{2} = 24.50\ \text{MJ/kg}$$

The ratio is 3.027, so **the X-17 reached 33.0 percent of the energy per unit mass that an intercontinental re-entry delivers.** No choice of altitude changes that, because altitude does not appear in the relation.

What that energy does to the air is the point. The perfect-gas stagnation temperature it would imply is

$$T_0 = T_\infty + \frac{h_0}{c_p}$$

which gives 8,274 kelvin for the X-17 and 24,627 for the intercontinental case. **Both figures are physically meaningless**, because the air dissociates and ionises long before either, absorbing the energy in chemistry rather than in temperature. The [previous article in this series][related_post_a312_north_american_x15] computed the limit at which the perfect-gas assumption fails, at Mach 7.06, and the X-17 flew at Mach 14.5, which is **2.05 times that limit.**

The relevant thresholds are approximate and standard. Oxygen dissociation begins near 2,500 kelvin and is substantially complete near 4,000. Nitrogen dissociation begins near 4,000. Ionisation becomes significant near 9,000. At 8 megajoules per kilogramme the shock layer is fully dissociated in oxygen and partly in nitrogen. At 24.5 it is far advanced in nitrogen dissociation with ionisation beginning, which is why radio blackout is a re-entry phenomenon and not an X-17 phenomenon.

**These are different gases doing the heating**, and the difference has a geometric consequence that is easy to overlook. For a perfect gas the strong-shock density ratio has a hard ceiling,

$$\frac{\rho_2}{\rho_1} \rightarrow \frac{\gamma + 1}{\gamma - 1} = 6\quad \text{at}\ \gamma = 1.4$$

Dissociation absorbs energy, lowers the effective ratio of specific heats, and lets the gas compress far more than that. Since shock standoff scales inversely,

$$\frac{\delta}{R_n} \sim \frac{\rho_1}{\rho_2}$$

a perfect gas holds its shock 25 millimetres off a 15 centimetre nose while a strongly dissociating one holds it at 8. **The shock sits closer to the body in the gas the X-17 did not produce**, which changes the boundary layer edge conditions and therefore the heating distribution away from the stagnation point, where most of the surface actually is. The rate at which the air ionises behind a shock was measured in [Lin 1961][research_lin_1961] and [Lin et al 1962][research_lin_1962], the equilibrium properties tabulated in [Viegas and Howe 1962][research_viegas_howe_1962], the transport properties in [Yun and Mason 1962][research_yun_mason_1962], and the effect on hypersonic flow fields analysed in [Hermann et al 1962][research_hermann_1962]. Stagnation heat transfer specifically in partially ionised air was measured in [Rose and Stankevics 1963][research_rose_stankevics_1963], and radiation from the hot gas in [Archer 1963][research_archer_1963] and [Page 1963][research_page_1963].

### Radiation, Which Is a Fourth Thing Missed and Was Not Mentioned

Convective heating is not the only mechanism. The shock layer also radiates, and that contribution scales far more steeply with velocity,

$$\dot{q}_{\text{rad}} \sim R_n\, \rho^{1.2}\, V^{8.5}$$

against the square root and cube of convection. At equal density the velocity term alone gives

$$\left(\frac{7{,}000}{4{,}023}\right)^{8.5} = 110.7$$

so **the X-17 sees roughly one part in 111 of the radiative heating an intercontinental re-entry produces.** Extending the same exponent, lunar return at 11 kilometres per second is 5,162 times the X-17's radiative environment, which is why radiation dominates there and is negligible here.

**The X-17's condition is purely convection-dominated and an intercontinental re-entry is beginning not to be.** That is a fourth respect in which the simulation is partial, and unlike the other three it is not a consequence of the density trade. It follows from velocity alone and is therefore unfixable by any choice of altitude.

### The Third Requirement, Which Is Also Missed

Chemical nonequilibrium has its own similarity parameter. Reaction rates depend on the square of density while the time available depends on body size over velocity, so the governing group is the product of density and length,

$$\Pi = \rho L$$

Comparing an intercontinental body of 1.5 metres with an X-17 nose of 0.5 metres,

$$\Pi_{\text{ICBM}} = 0.008214 \times 1.5 = 0.01232\ \text{kg/m}^{2}$$

while the test vehicle at its matching altitude gives

$$\Pi_{\text{X-17}} = 0.2278 \times 0.5 = 0.1139\ \text{kg/m}^{2}$$

a ratio of **9.25**. The same statement can be made as a rate comparison through the Damköhler number, which is the ratio of the time the gas spends in the shock layer to the time its chemistry needs,

$$Da = \frac{t_{\text{flow}}}{t_{\text{chem}}} \sim \frac{\rho L}{V}$$

Below one the gas has no time to react and the flow is frozen. Above one it reaches equilibrium. Evaluating,

$$\frac{Da_{\text{X-17}}}{Da_{\text{ICBM}}} = \frac{0.2278 \times 0.5 / 4{,}023}{0.008214 \times 1.5 / 7{,}000} = 16.09$$

**Flying lower to buy the heating rate overshoots the binary scaling parameter by nearly an order of magnitude**, which pushes the shock layer toward chemical equilibrium and away from the nonequilibrium state a real re-entry has. The X-17 therefore missed the third requirement as well as the first, and in a direction that made its flow more benign and more predictable rather than less.

### The Total Heat Load Is a Fourth Quantity

Peak rate is what fails a structure suddenly. Total load is what consumes an ablator, and it is a different integral,

$$Q = \int \dot{q}\, dt$$

A steep powered dive and a shallow intercontinental re-entry can share a peak rate and differ entirely in the integral. Taking representative exposure times of 6 seconds and 25 seconds with a triangular rate history,

$$Q_{\text{X-17}} \approx \tfrac{1}{2} \times 1{,}398 \times 6 = 41.9\ \text{MJ/m}^{2}$$

against a re-entry lasting four times as long,

$$Q_{\text{ICBM}} \approx \tfrac{1}{2} \times 1{,}398 \times 25 = 174.7\ \text{MJ/m}^{2}$$

The exposure times are representative rather than measured, and the ratio of 4.17 is the point rather than the values. **A material that survives the X-17's pulse has not been shown to survive an intercontinental re-entry's soak.**

### What the Programme Actually Bought

Collecting the four comparisons gives the article's central table.

| Quantity | Reproduced | Why |
|---|---|---|
| Stagnation heating rate | **Yes, exactly** | density traded against velocity |
| Nose radius and full scale | **Yes** | the article was full size |
| Boundary layer state and transition | **Yes, arguably better** | Reynolds number is high at low altitude |
| Stagnation enthalpy and chemistry | **No, 33 percent** | enthalpy carries no density |
| Nonequilibrium state | **No, 9.25 times off** | binary scaling overshot |
| Total heat load | **No, about a quarter** | exposure is far shorter |
| Radiative heating | **No, about one percent** | radiation scales as $V^{8.5}$ |
| The trajectory as a whole | **No, one point only** | a re-entry is a curve |

**The X-17 surrendered velocity and therefore chemistry, and bought heating rate, scale, and material response.** For a nose cone designer in 1956 who needed to know whether a given ablator on a given shape would survive a given heat flux, that was the right trade, because the chemistry he could not have used anyway. **The programme gave up the thing nobody could yet compute and kept the thing everybody needed to measure.**

## Dependent Systems

### The Nose, Which Is the Experiment

Heating falls as the inverse square root of nose radius, so bluntness is the primary defence,

$$\dot{q} \propto \frac{1}{\sqrt{R_n}}$$

Evaluated at the X-17's condition,

| Nose radius, m | Heating, W/cm² | Relative |
|---|---|---|
| 0.02 | 3,828 | 2.74 |
| 0.05 | 2,421 | 1.73 |
| 0.15 | 1,398 | 1.00 |
| 0.30 | 988 | 0.71 |

**A 2 centimetre nose takes 2.74 times the heat flux of a 15 centimetre one.** That is the first half of the blunt-body argument. The second half is that a blunt body decelerates higher, because ballistic coefficient sets penetration,

$$\beta = \frac{m}{C_D A}$$

For a 200 kilogramme body at the third-stage diameter, a blunt hemisphere at a drag coefficient of 1.0 gives 4,195 kilogrammes per square metre and a slender cone at 0.3 gives 13,983, a ratio of **3.33**. **The slender body carries over three times the ballistic coefficient and therefore arrives fast in dense air, which is the worst possible combination.** It is heated harder by its own sharpness and for longer by its own penetration.

The X-17 flew hemispherical, cubic paraboloid, and blunt nose shapes and the programme concluded that blunt was correct for both Atlas and Titan. Period measurements on the same question appear in [Nardo and Sadler 1962][research_nardo_sadler_1962], [Conti 1961][research_conti_1961], and [Oguchi 1962][research_oguchi_1962], with the asymmetric case in [SWIGART 1962][research_swigart_1962].

### The Ablator, Which Is the Answer to the Heat That Arrives Anyway

Bluntness reduces the flux. It does not remove it, and the claim that no passive material survives is checkable in one line rather than assertable. A surface in steady state rejects heat by radiating it,

$$\dot{q} = \varepsilon \sigma T^{4}$$

so the temperature a passive surface must reach to reject the incident flux is

$$T = \left(\frac{\dot{q}}{\varepsilon \sigma}\right)^{1/4} = \left(\frac{1.398 \times 10^{7}}{0.85 \times 5.67 \times 10^{-8}}\right)^{1/4} = 4{,}127\ \text{K}$$

at an emissivity of 0.85. Against the most refractory materials there are,

| Material | Melting or sublimation, K | Verdict |
|---|---|---|
| Steel | 1,810 | fails |
| Silica glass softens | 1,900 | fails |
| Molybdenum | 2,896 | fails |
| Tungsten | 3,695 | fails |
| Graphite sublimes | 3,900 | fails |
| Hafnium carbide | 4,200 | survives, barely |

**Every material available in 1956 fails, including tungsten and graphite.** Only hafnium carbide exceeds the required temperature and only by 73 kelvin, and it was not a structural material. **Passive re-radiation is not an option at this flux**, which makes ablation mandatory rather than merely convenient. The answer is ablation, in which the surface is consumed and carries the heat away with the mass it loses, while the injected gas thickens the boundary layer and blocks part of the incoming flux. The energy balance is

$$\dot{m} = \frac{\dot{q}_{\text{net}}}{h_{\text{eff}}}$$

where the effective heat of ablation lumps together heating the material to its ablation temperature, the phase change, and the blockage the injected gas provides. At the matched flux,

| Material | $h_{\text{eff}}$, MJ/kg | Mass loss, kg/m²/s |
|---|---|---|
| Teflon | 2.3 | 6.08 |
| Silica or quartz | 9.0 | 1.55 |
| Phenolic nylon | 12.0 | 1.16 |
| Graphite | 25.0 | 0.56 |

At a phenolic-like 12 megajoules per kilogramme and a material density of 1,400 kilogrammes per cubic metre, the surface lost over the exposure is

$$s = \frac{\dot{m} \tau}{2 \rho_m}$$

giving 2.50 millimetres over the X-17's six seconds and 10.39 over a twenty-five second re-entry.

The theory of that blockage is set out in [Swann and South 1961][research_swann_south_1961], requirements analysis in [Roberts 1960][research_roberts_1960], the measurement of rates in [Winters and Bracalente 1961][research_winters_bracalente_1961], and material screening in arc-heated air in [Chapman 1963][research_chapman_1963] and [Dickey and Haacker 1963][research_dickey_haacker_1963]. Glass and quartz shields, which melt and run rather than char, are treated in [Warmbrod 1963][research_warmbrod_1963].

There is a second and less obvious difference between a pulse and a soak. Heat diffuses into the material a distance

$$\delta = \sqrt{\alpha t}, \qquad \alpha = \frac{k}{\rho_m c}$$

and for a phenolic ablator $\alpha = 1.43 \times 10^{-7}$ square metres per second, so

$$\delta_{6\,\text{s}} = 0.93\ \text{mm}, \qquad \delta_{25\,\text{s}} = 1.89\ \text{mm}$$

a ratio of 2.04, which is the square root of the time ratio. **The X-17's pulse heats half the depth an intercontinental re-entry does.** A material can therefore pass an X-17 test on its surface behaviour and still fail on what happens to the structure behind it, which is a failure mode the vehicle was structurally incapable of finding.

**The X-17's contribution here is that it exposed real materials at full scale to a correct heat flux.** That is a screening capability, and it is exactly what the trade described above preserved.

### The Structure and Staging

The first stage lifts a 4,831 kilogramme vehicle on 48,000 pounds force, giving a launch thrust-to-weight ratio of

$$\frac{T}{W} = \frac{48{,}000}{10{,}650} = 4.51$$

which is high and appropriate for a vehicle that must clear the dense atmosphere quickly. The upper stages together develop 137,650 pounds force, or 612 kilonewtons, against a much smaller remaining mass, which is what supplies the 2,339 metres per second of downward velocity computed above.

Solid propellant was the only sensible choice. It requires no pumps, tolerates being stored, and can be fired in any attitude, which matters greatly for a stage that ignites while pointing at the ground after a ballistic coast. Motor design and case work of the period appear in [Bua 1963][research_bua_1963] and [Harris 1963][research_harris_1963], internal insulation in [WALTON and SIMMONS 1962][research_walton_simmons_1962] and [Sale 1964][research_sale_1964], and the ablation problem inside the motor itself in [KUBY et al 1962][research_kuby_1962]. Multistage trajectory optimisation is treated in [Boyce 1963][research_boyce_1963].

### Stability and the Attitude Problem

A vehicle that coasts to apogee, tips over, and then fires has an attitude problem the flight-mechanics literature of the period addresses directly. The vehicle must be pointed correctly before the second stage lights, and any angle of attack at ignition is amplified by the burn.

Spin stabilisation is the usual answer and appears in [Levine et al 1960][research_levine_1960]. Re-entry body dynamics generally are treated in [Holway and Prislin 1966][research_holway_prislin_1966], with later work on roll behaviour and angle-of-attack control in [KRYVORUKA and ASHURST 1973][research_kryvoruka_ashurst_1973] and [Platus 1980][research_platus_1980]. The ballistic missile free-flight problem in general is [WHEELON 1959][research_wheelon_1959].

### Instrumentation, Which Is the Actual Product

The vehicle exists to return numbers, and at these conditions returning numbers is difficult. Thermocouples must survive a surface that is being consumed, telemetry must work through a partially ionised layer, and the whole record must be transmitted before the article is destroyed.

The free-flight heating measurement technique and its interpretation are the direct subject of [Murphy and Rubesin 1965][research_murphy_rubesin_1965], and a closely comparable free-flight heat transfer and ablation measurement on a blunted body appears in [Winters 1964][research_winters_1964]. Comparison of tunnel and flight data for an instrumented hypersonic rocket is in [Maydew 1964][research_maydew_1964].

### Reynolds Number and Transition, Which the Low Altitude Gives Free

Flying low to buy density has a second consequence that the programme got without asking. Reynolds number is

$$Re = \frac{\rho V L}{\mu}$$

and at the X-17's condition it is very large.

| Altitude, km | Length, m | Reynolds number |
|---|---|---|
| 20.0 | 0.5 | $1.25 \times 10^{7}$ |
| 15.0 | 0.5 | $2.74 \times 10^{7}$ |
| 15.0 | 1.0 | $5.48 \times 10^{7}$ |
| 10.0 | 1.0 | $1.14 \times 10^{8}$ |

Sources state the vehicle reached Reynolds numbers above 24 million, which the table reproduces at 15 kilometres on a half-metre body. **That matters because a turbulent boundary layer transfers several times the heat a laminar one does.** Flat-plate correlations give the Stanton number as

$$St_{\text{lam}} \sim Re^{-1/2}, \qquad St_{\text{turb}} \sim Re^{-1/5}$$

so the turbulent-to-laminar heating ratio grows as $Re^{0.3}$, and at the quoted Reynolds number the penalty is

$$\left(\frac{2.74 \times 10^{7}}{1 \times 10^{6}}\right)^{0.3} = 2.70$$

**A factor of 2.7 rests on where transition happens**, which is a first-order design question rather than a refinement. Transition on blunted bodies is treated in [Jillie and Hopkins 1961][research_jillie_hopkins_1961] and [MASAKI and YAKURA 1968][research_masaki_yakura_1968], and the laminar and turbulent heating comparison is the substance of [Murphy and Rubesin 1965][research_murphy_rubesin_1965].

**This is the one respect in which the X-17's condition was arguably more severe than the flight it simulated**, because a real re-entry at high altitude has a lower Reynolds number and may stay laminar longer.

## The Flight Test Record

A quarter-scale proof-of-concept vehicle flew in May 1955. The first full X-17 flew in April 1956, and 25 further flights followed to March 1957, giving 26 in total.

The programme flew hemispherical, cubic paraboloid, and blunt nose shapes and returned what secondary accounts describe as the first substantial body of re-entry heat transfer data, covering boundary layer transition, external shape, and high-temperature material response. **The conclusion drawn was that the blunt shape was correct, and it was adopted for both the [Atlas][ref_atlas] and the [Titan][ref_titan].**

The vehicle then had two further lives. It served as a Polaris flight test vehicle during 1957 and 1958 in three-stage and two-stage variants, and in 1958 it was launched from ships in the South Atlantic as the booster for [Operation Argus][ref_argus], a series of three high-altitude nuclear detonations.

**That last role is worth naming plainly rather than passing over.** A vehicle built to measure heat transfer was used to place nuclear devices at high altitude to study the behaviour of trapped charged particles. It is the same airframe doing something entirely unrelated to its research purpose, and it is the only instance in this series so far of an X-designated vehicle being used to deliver a nuclear detonation.

## Comparison With Ground Prediction

This section usually sets what was predicted against what was measured. Here the comparison is unusually clean in one direction and unavailable in the other.

**What was predicted was the shape.** Blunt-body theory said that a blunt nose would dump its energy into the shock layer rather than the surface, and that prediction is quantitative and was made before the flights. **The X-17 confirmed it**, and the adoption of blunt shapes on Atlas and Titan is the confirmation being acted upon.

**What cannot be compared is the heating magnitude**, because the flight data themselves are not in the public archive. This article can state what the vehicle should have measured, from the correlation and the trajectory, and cannot state what it did measure. The correlation used here postdates the programme in its published form, and the theoretical treatment closest to what the designers would have had is [Eggers et al 1958][research_eggers_1958], which appeared after the flights had finished.

**One prediction of this article can be checked against a published statement.** The Reynolds number computed at 15 kilometres on a half-metre body is $2.74 \times 10^{7}$, and sources state the vehicle exceeded 24 million. Those agree, which is weak evidence that the trajectory reconstruction used here is approximately right.

## What the Data Changed

**The shape of every American intercontinental re-entry vehicle.** The blunt nose went onto Atlas and Titan and stayed on everything after them. That is an unusually direct and traceable consequence for a research programme.

**The screening method.** Testing full-scale ablators at a correct heat flux, however imperfect the chemistry, became the standard way of selecting materials, and the arc-jet facilities that later carried that role were validated against exactly this kind of flight data.

**The confidence to proceed.** The intercontinental missile programmes were being committed to at enormous cost on the assumption that the warhead would survive. The X-17 is the vehicle that turned that assumption into a measurement.

What it did not change is the gas physics. **The X-17 could not and did not settle anything about dissociation, ionisation, or nonequilibrium chemistry**, because it did not reach the enthalpy at which those dominate. Those were settled later and elsewhere, by shock tubes and by theory, in the literature cited above.

## The Contemporary Literature

The X-17's question is not closed, and the reason it is not closed is precisely the limitation this article has been describing. **Nobody has ever built a facility that reproduces a full re-entry**, and the field's response has been to get much better at knowing which parts are wrong.

### The Facilities Still Cannot Do It

Arc-heated facilities remain the workhorse for material screening and are still being characterised rather than trusted, as in [Gokcen and Alunni 2019][research_gokcen_alunni_2019] and [Alunni et al 2019][research_alunni_2019]. Shock tubes and expansion tubes remain the way to reach genuine flight enthalpy for very short times, as in [Chandel et al 2019][research_chandel_2019]. **The X-17's fundamental problem, that no ground facility gives full enthalpy at full scale for full duration, is unresolved seventy years later.**

### The Chemistry the X-17 Missed Is the Modern Subject

The nonequilibrium chemistry the X-17 surrendered is now the central computational difficulty, in [Kline et al 2019][research_kline_2019] and the radiation modelling of [Winter et al 2019][research_winter_2019]. **What the X-17 gave up because nobody could use it is now the part that is hardest to get right**, which is a reversal worth stating.

### Ablation Became a Predictive Model Rather Than a Screening Result

The X-17 could tell a designer that a material survived. Modern practice demands a model that says why and predicts the recession, as in [Wang et al 2019][research_wang_2019]. **That is a change in kind rather than degree**, and it is what allows a heat shield to be designed rather than selected.

### Free Flight Is Still the Ground Truth

Rough-wall turbulent heat transfer measured in hypersonic free flight, in [Wilder and Prabhu 2019][research_wilder_prabhu_2019], is the direct descendant of the X-17's technique at small scale. **Flight remains the only place the real condition occurs**, which is the same reason the X-17 was built.

## Where the Framing Breaks Down

Treating the X-17 through partial simulation misleads in four places.

**It implies the programme reasoned this way.** The similarity analysis above is modern in its framing. The designers knew they could not match velocity and chose to match heat flux, but the binary scaling parameter and the formal statement of three conditions against two knobs are a later way of saying it.

**It assumes a reference re-entry that is generic, and the assumption turns out to carry more weight than it looks.** The 7,000 metres per second at 35 kilometres used throughout is representative rather than the actual Atlas condition, which was classified and is not used here. Deriving the reference from the trajectory solution instead shows that it corresponds to a ballistic coefficient of 1,453 kilogrammes per square metre, and that **the heating-rate match fails entirely above about 2,500**. Every ratio in this article inherits that choice, and a reader who prefers a denser reference body gets a materially different answer, up to and including the conclusion that the X-17 could not have matched it at all.

**It treats the trajectory as known.** No published trajectory for an X-17 flight was located. The 13.97 kilometre matching altitude is where the vehicle would have had to be to match the reference heating, not a measured altitude, and the article should not be read as asserting the vehicle flew there.

**It gives the vehicle more credit for the shape result than it may deserve.** Blunt-body theory was already published and already believed. The X-17 confirmed rather than discovered, and a confirmation that agrees with the theory it tests is weaker evidence than a surprise would have been.

## The Source Base

**No primary document about the X-17 was located in any archive this series uses.** The NASA technical reports server returns astronomy false positives for the vehicle name, specifically the X-ray source GX 17+2, and nothing technical. The Defense Technical Information Center holds the surrounding re-entry literature and nothing on this vehicle. It was an Air Force ballistic-missile support programme and its reports are not in the civil archive.

**This is the second consecutive article whose subject has no archival record of its own.** The [X-16][related_post_a313_bell_x16] was cancelled and classified, and the X-17 flew and was classified. In both cases the article is carried by the literature of the question rather than of the vehicle.

Consequently **every dimension, thrust, date, and performance figure here comes from secondary compilations, and those compilations disagree.** The disagreements recorded in the text are the length at 40 feet 4 inches against 41 feet, and the apogee at about 100 miles against about 500,000 feet against 250 miles. The last of those is a factor of two and a half and no basis for choosing between them was found.

What does hold the article up is the re-entry literature itself, which is large, public, and contemporaneous. The stagnation heating correlations, the blunt-body theory, the ablation screening programme, the high-temperature air properties, the shock-tube and ballistic-range work, and the free-flight measurement technique are all primary and none is about the X-17.

## Epistemic State

**Historical fact.** A quarter-scale vehicle flew in May 1955 and the first full X-17 in April 1956, with 25 further flights to March 1957. The vehicle was a three-stage solid-propellant rocket using a Thiokol XM20 Sergeant first stage and Recruit upper stages. Hemispherical, cubic paraboloid, and blunt nose shapes were flown. The blunt shape was adopted for Atlas and Titan. The vehicle served as a Polaris flight test vehicle in 1957 and 1958 and boosted the three Operation Argus high-altitude nuclear tests in 1958. A flight on 24 April 1957 reached 9,000 miles per hour.

**Disputed in the record.** The overall length, given as 40 feet 4 inches and as 41 feet. The apogee, given as about 100 miles, about 500,000 feet, and 250 miles. This article resolves neither.

**Engineering analysis, reproducible from the stated inputs.** The requirement that a passive surface reach 4,127 kelvin to reject the matched flux, which exceeds the melting point of tungsten and the sublimation point of graphite and therefore makes ablation mandatory rather than merely convenient. The Allen-Eggers results, namely a peak deceleration of 43.7 g independent of ballistic coefficient, a velocity at peak heating of 5,925 metres per second also independent of it, and peak-heating altitudes from 31.3 kilometres at a ballistic coefficient of 1,000 down to 12.3 at 13,983. **The ballistic coefficient ceiling above which the X-17 cannot match the heating rate at any altitude, at about 6,300 kilogrammes per square metre even at sea level and about 2,500 at a practical floor.** That the assumed reference corresponds to 1,453. The radiative heating ratios of 110.7 against an intercontinental re-entry and 5,162 against lunar return. The Damköhler ratio of 16.09. The ablation mass loss and recession figures. The thermal penetration depths of 0.93 and 1.89 millimetres. The turbulent heating penalty of 2.70. The free-fall speed of 1,684 metres per second from the lower apogee and the resulting factor of 13.63 in heating rate. The required density ratio of 27.74 and the matching altitude of 13.97 kilometres. The equal heating rates of 1,398 watts per square centimetre. The stagnation enthalpies of 8.094 and 24.50 megajoules per kilogramme and their ratio of 3.027. The binary scaling ratio of 9.25. The nose radius heating ratios. The ballistic coefficient ratio of 3.33. The Reynolds numbers.

**Inference, and clearly labelled.** That the heating-rate match was fitted to the class of body the vehicle was built to test, rather than being a general capability, follows from the ballistic-coefficient ceiling and the coincidence that the assumed reference sits below it. It is an argument from internal consistency and not from any document. That the X-17 surrendered velocity deliberately rather than as a consequence of what its motors happened to deliver is an inference from the design's internal consistency and not from any document. That the chemistry it missed did not matter for the 1956 question is an argument about what could be used rather than about what was true. That the shape result was a confirmation rather than a discovery follows from the publication order of the theory.

**What the record does not settle and this article does not claim.** What the X-17 actually measured, since no flight data were located. What trajectory any flight followed. Whether the ablators screened on it behaved the same way at intercontinental enthalpy, which is precisely the extrapolation the partial simulation does not license.

**Information postdating the editorial date.** The contemporary literature section is written from current knowledge per the series convention.

## Out of Scope

The Atlas and Titan programmes themselves are treated only as consumers of this vehicle's result. Operation Argus is named and its physics is not discussed. The Polaris programme is outside this article. The detailed chemistry of dissociating air is cited rather than derived. No attempt is made to reconstruct an actual flight trajectory. Radiative heating is treated only through its velocity scaling, which is sufficient to show that the X-17 could not reproduce it, and the shock-layer radiation transport that would be needed to compute it properly is cited rather than derived.

## Conclusion

The X-17 fired rockets downward because falling was not enough, and the margin is not close. **Free fall from its own apogee would have produced under a tenth of the heating rate it was built to study**, and the whole peculiar architecture follows from that single factor of fourteen.

What it bought with that architecture was a partial simulation, and the partition is sharp. **It reproduced the heating rate exactly, at full scale, with a real material, and it reproduced 33 percent of the stagnation enthalpy and therefore none of the chemistry.** The nonequilibrium state it missed by a factor of nine in the wrong direction, and the total heat load by a factor of four.

**That trade was correct for 1956 and would be wrong today**, which is the most interesting thing about the vehicle. The programme surrendered the gas physics because nobody could compute it, and kept the heat flux because everybody needed to design against it. Seventy years later the chemistry is the hard part, the material response is modelled rather than screened, and no facility has yet been built that reproduces the whole condition. **The X-17's compromise has been inherited rather than resolved.**

## References

### Books

[book_anderson_2019]: https://openlibrary.org/search?q=Anderson+Hypersonic+and+High+Temperature+Gas+Dynamics
[book_jenkins_landis_miller_2003]: https://openlibrary.org/search?q=Jenkins+Landis+Miller+American+X+Vehicles
[book_miller_2001]: https://openlibrary.org/search?q=Miller+The+X+Planes+X-1+to+X-45
[book_neufeld_1990]: https://openlibrary.org/search?q=Neufeld+Development+of+Ballistic+Missiles+United+States+Air+Force

### Reference

[ref_argus]: https://en.wikipedia.org/wiki/Operation_Argus
[ref_atlas]: https://en.wikipedia.org/wiki/SM-65_Atlas
[ref_titan]: https://en.wikipedia.org/wiki/HGM-25A_Titan_I
[ref_x17]: https://en.wikipedia.org/wiki/Lockheed_X-17

### Research

[research_alunni_2019]: https://ntrs.nasa.gov/citations/20190026513
[research_archer_1963]: https://doi.org/10.21236/ad0431737
[research_boyce_1963]: https://ntrs.nasa.gov/citations/19630006926
[research_bua_1963]: https://doi.org/10.21236/ad0415435
[research_chandel_2019]: https://ntrs.nasa.gov/citations/20180006681
[research_chapman_1963]: https://ntrs.nasa.gov/citations/19630005427
[research_conti_1961]: https://ntrs.nasa.gov/citations/19980227274
[research_dayman_1962]: https://ntrs.nasa.gov/citations/19620006382
[research_dickey_haacker_1963]: https://ntrs.nasa.gov/citations/19660024017
[research_eggers_1958]: https://ntrs.nasa.gov/citations/19930085175
[research_gokcen_alunni_2019]: https://ntrs.nasa.gov/citations/20190028252
[research_harris_1963]: https://doi.org/10.21236/ad0402393
[research_hermann_1962]: https://ntrs.nasa.gov/citations/19620005896
[research_holway_prislin_1966]: https://ntrs.nasa.gov/citations/19660061364
[research_jillie_hopkins_1961]: https://ntrs.nasa.gov/citations/19980227973
[research_kline_2019]: https://ntrs.nasa.gov/citations/20200002702
[research_kryvoruka_ashurst_1973]: https://doi.org/10.2514/6.1973-183
[research_kuby_1962]: https://doi.org/10.21236/ad0282734
[research_levine_1960]: https://ntrs.nasa.gov/citations/19980227768
[research_levy_mc_devitt_1964]: https://ntrs.nasa.gov/citations/19650019778
[research_lin_1961]: https://doi.org/10.1016/0032-0633(61)90008-3
[research_lin_1962]: https://doi.org/10.1063/1.1706575
[research_masaki_yakura_1968]: https://doi.org/10.2514/6.1968-1155
[research_maydew_1964]: https://doi.org/10.2172/4000106
[research_murphy_rubesin_1965]: https://ntrs.nasa.gov/citations/19660010795
[research_nardo_sadler_1962]: https://doi.org/10.21236/ad0273837
[research_oguchi_1962]: https://doi.org/10.1016/b978-0-12-395595-1.50008-8
[research_page_1963]: https://ntrs.nasa.gov/citations/19630015305
[research_platus_1980]: https://doi.org/10.21236/ada093741
[research_roberts_1960]: https://ntrs.nasa.gov/citations/19980232223
[research_rose_stankevics_1963]: https://doi.org/10.21236/ad0406269
[research_sale_1964]: https://doi.org/10.21236/ad0609001
[research_swann_south_1961]: https://ntrs.nasa.gov/citations/20040003877
[research_swigart_1962]: https://doi.org/10.21236/ad0274612
[research_trimpi_1962]: https://ntrs.nasa.gov/citations/19630003230
[research_viegas_howe_1962]: https://ntrs.nasa.gov/citations/19620006838
[research_walton_simmons_1962]: https://doi.org/10.21236/ad0286392
[research_wang_2019]: https://ntrs.nasa.gov/citations/20190025824
[research_warmbrod_1963]: https://ntrs.nasa.gov/citations/19630005471
[research_wheelon_1959]: https://doi.org/10.2514/8.4944
[research_wilder_prabhu_2019]: https://ntrs.nasa.gov/citations/20190028253
[research_winter_2019]: https://ntrs.nasa.gov/citations/20190002714
[research_winters_1964]: https://ntrs.nasa.gov/citations/19640017591
[research_winters_bracalente_1961]: https://ntrs.nasa.gov/citations/20040008121
[research_yee_1961]: https://ntrs.nasa.gov/citations/20040047120
[research_yun_mason_1962]: https://ntrs.nasa.gov/citations/19620005758

### Related Post

[related_post_a297_xplanes_framing]: {% post_url 2025-10-06-x_planes_framing %}
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
