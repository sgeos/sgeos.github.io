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

The facilities themselves became a substantial field, and the reason is that none of them ever solved the problem outright. Shock tubes, shock and expansion tunnels, arc-heated jets, ballistic ranges, and ceramic-heated and hotshot tunnels each buy one part of the condition at the cost of another, across [Bleakney et al 1949][research_bleakney_1949], [Lundquist 1952][research_lundquist_1952], [Wegener and Lobb 1952][research_wegener_lobb_1952], [MACK 1954][research_mack_1954], [Walker and Wolowicz 1960][research_walker_wolowicz_1960], [Palmer and Knox 1960][research_palmer_knox_1960], [FILLER 1960][research_filler_1960], [Trimpi 1962, A Preliminary Theoretical Study of][research_trimpi_1962_2], [Bradley et al 1981][research_bradley_1981], [Park and Balakrishnan 1985][research_park_balakrishnan_1985], [Takahashi and Teshima 1985][research_takahashi_teshima_1985], [YANG et al 1985][research_yang_1985], [Hanson 2000][research_hanson_2000], [Yungster and Radhakrishnan 2001][research_yungster_radhakrishnan_2001], [Holden 2004][research_holden_2004], [Balakalyani and Jagadeesh 2019][research_balakalyani_jagadeesh_2019], [Gildfind 2019][research_gildfind_2019], [Wang and Jiang 2020][research_wang_jiang_2020]. **Every one of those is a partial simulation too**, which is worth saying before criticising the X-17 for being one.

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

The solution and its descendants are the standard treatment of the problem, in [Scherberg and Rubin 1953][research_scherberg_rubin_1953], [Eilertson and Wing 1966][research_eilertson_wing_1966], [Speyer and Womble 1971][research_speyer_womble_1971], [KNIGHT and QUINN 1971][research_knight_quinn_1971], [Maples 1973][research_maples_1973], [GREENE and WILLIAMSON 1981][research_greene_williamson_1981], [Vinh and Lin 1982][research_vinh_lin_1982], [Desai et al 1999][research_desai_1999], [Zhang et al 2010][research_zhang_2010], [Zhou et al 2012][research_zhou_2012], [Zhao and Zhou 2013][research_zhao_zhou_2013], [Pei et al 2021][research_pei_2021], [Su et al 2021][research_su_2021], [Ma et al 2022][research_ma_2022].

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

where $R_n$ is the nose radius and $K = 1.7415 \times 10^{-4}$ in SI units. That correlation sits on top of a large measurement and analysis programme, since the constant is empirical and the exponents are the result of boundary-layer theory checked against experiment, in [Luce and Jr 1949][research_luce_jr_1949], [Emmons 1951][research_emmons_1951], [Allen and Eggers 1953][research_allen_eggers_1953], [Jonas 1953][research_jonas_1953], [VAGLIG-LAURIN 1960][research_vaglig_laurin_1960], [CRESCI et al 1960][research_cresci_1960], [SEIDMAN 1960][research_seidman_1960], [Neice et al 1960][research_neice_1960], [Gonzales 1981][research_gonzales_1981], [Thornton 1981][research_thornton_1981], [Nomura 1983][research_nomura_1983], [GAI et al 1985][research_gai_1985], [Mizoguchi et al 2006][research_mizoguchi_2006], [Clemente and Ferrarella 2010][research_clemente_ferrarella_2010], [Tashakkor et al 2011][research_tashakkor_2011], [Tauber et al 2012][research_tauber_2012], [Si et al 2019][research_si_2019], [Manjhi and Kumar 2020][research_manjhi_kumar_2020], [Han et al 2020][research_han_2020], [Lefevre et al 2022][research_lefevre_2022]. The structure of that relation is the whole opportunity. **Density enters under a square root and velocity enters cubed**, so a deficit in velocity can be repaid by an excess of density, and the exchange rate is steep. Holding the heating rate fixed,

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

**The properties of high-temperature air are the single largest supporting literature this article rests on**, because every quantity in the heating calculation depends on them and none of them is constant. Thermodynamic, transport, and reaction-rate properties, dissociation and ionisation equilibria, and the relaxation processes that decide whether equilibrium is reached at all run through [Hansen and Heims 1958][research_hansen_heims_1958], [Hansen 1959][research_hansen_1959], [Bachynski et al 1959][research_bachynski_1959], [Jahn and Grosse 1959][research_jahn_grosse_1959], [Bachynski et al 1960][research_bachynski_1960], [Gardner 1961][research_gardner_1961], [KVASHINA and KOROBEINIKOV 1961][research_kvashina_korobeinikov_1961], [Beckwith and Cohen 1963][research_beckwith_cohen_1963], [Li 1981][research_li_1981], [Jaffe 1986][research_jaffe_1986], [Kaul 1986][research_kaul_1986], [Zoby et al 1988][research_zoby_1988], [Scalabrin and Boyd 2005][research_scalabrin_boyd_2005], [Chazot et al 2008][research_chazot_2008], [Manning 2009][research_manning_2009], [Chen and Milos 2011][research_chen_milos_2011], [Kim et al 2020][research_kim_2020], [Surzhikov 2020, Numerical Analysis of Shock Layer][research_surzhikov_2020_2], [Pan et al 2021][research_pan_2021], [Freno et al 2021][research_freno_2021].

### Radiation, Which Is a Fourth Thing Missed and Was Not Mentioned

Convective heating is not the only mechanism. The shock layer also radiates, and that contribution scales far more steeply with velocity,

$$\dot{q}_{\text{rad}} \sim R_n\, \rho^{1.2}\, V^{8.5}$$

against the square root and cube of convection. At equal density the velocity term alone gives

$$\left(\frac{7{,}000}{4{,}023}\right)^{8.5} = 110.7$$

so **the X-17 sees roughly one part in 111 of the radiative heating an intercontinental re-entry produces.** Extending the same exponent, lunar return at 11 kilometres per second is 5,162 times the X-17's radiative environment, which is why radiation dominates there and is negligible here.

Shock-layer radiation has its own measurement and modelling literature, developed largely because lunar return made it unavoidable, in [Coulson and Furukawa 1960][research_coulson_furukawa_1960], [Compton and Cooper 1964][research_compton_cooper_1964], [Davis 1964][research_davis_1964], [Moss and Kumar 1981][research_moss_kumar_1981], [GUPTA et al 1990][research_gupta_1990], [Tauber and Sutton 1991][research_tauber_sutton_1991], [Winter et al 2011][research_winter_2011], [Cruden 2011][research_cruden_2011], [Johnston et al 2012][research_johnston_2012], [Collen et al 2023][research_collen_2023], [McGilvray et al 2024][research_mcgilvray_2024], [Ravichandran et al 2025][research_ravichandran_2025].

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

The flow field that produces that scaling, namely a detached bow shock with a subsonic region behind it, was worked out over the same period and is the subject of [KANE 1951][research_kane_1951], [Sherman 1951][research_sherman_1951], [Stalder and Nielsen 1954][research_stalder_nielsen_1954], [LI and GEIGER 1957][research_li_geiger_1957], [Bird 1960][research_bird_1960], [Ashkenas and Wegener 1961][research_ashkenas_wegener_1961], [Aroesty 1963][research_aroesty_1963], [Dohnanyi 1964][research_dohnanyi_1964], [CHRUSCIEL and POOL 1983][research_chrusciel_pool_1983], [Singh and Tiwari 1990][research_singh_tiwari_1990], [Singh et al 1991][research_singh_1991], [Fiala and Hillier 2003][research_fiala_hillier_2003], [Josyula and Bailey 2009][research_josyula_bailey_2009], [Korzun et al 2013][research_korzun_2013], [Tang et al 2021][research_tang_2021], [Yang et al 2022][research_yang_2022].

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

Those figures are not casual. The high-temperature behaviour of refractory metals, carbides, ceramics, and the coatings that protect them is a developed field, and the emissivity that appears in the relation above is itself an engineered property, across [Moore et al 1948][research_moore_1948], [Cohen and Homer 1959][research_cohen_homer_1959], [Mathauser et al 1960][research_mathauser_1960], [Fiorello 1961][research_fiorello_1961], [Trout 1963][research_trout_1963], [Foyle 1963][research_foyle_1963], [Wheeler et al 1986][research_wheeler_1986], [Deininger and King 1988][research_deininger_king_1988], [Leiser et al 1992][research_leiser_1992], [Lee et al 1994][research_lee_1994], [Perepezko 2002][research_perepezko_2002], [Vasudevan and Leonard 2002][research_vasudevan_leonard_2002], [Perepezko 2006][research_perepezko_2006], [ZHOU et al 2025][research_zhou_2025].

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

The theory of that blockage is set out in [Swann and South 1961][research_swann_south_1961], requirements analysis in [Roberts 1960][research_roberts_1960], the measurement of rates in [Winters and Bracalente 1961][research_winters_bracalente_1961], and material screening in arc-heated air in [Chapman 1963][research_chapman_1963] and [Dickey and Haacker 1963][research_dickey_haacker_1963]. The subject grew from a screening exercise into a modelled one and the line of it is [HIDALGO 1960][research_hidalgo_1960], [Linder 1961][research_linder_1961], [Gunderson 1962][research_gunderson_1962], [Herman and Melnik 1962][research_herman_melnik_1962], [Compton et al 1963][research_compton_1963], [Kumar et al 1980][research_kumar_1980], [Green and Davy 1981][research_green_davy_1981], [LINCOLN 1981][research_lincoln_1981], [Park et al 1983][research_park_1983], [Park et al 1983, Ablation of carbonaceous materials][research_park_1983_2], [Liu et al 2002][research_liu_2002], [Korabelnikov and Kuranov 2002][research_korabelnikov_kuranov_2002], [Curry 2004][research_curry_2004], [Kerr 2006][research_kerr_2006], [Pekker and Cambier 2006][research_pekker_cambier_2006], [Feldman et al 2019][research_feldman_2019], [Paglia et al 2019][research_paglia_2019], [Sun and Zhu 2019][research_sun_zhu_2019], [Shi et al 2020][research_shi_2020]. Glass and quartz shields, which melt and run rather than char, are treated in [Warmbrod 1963][research_warmbrod_1963].

There is a second and less obvious difference between a pulse and a soak. Heat diffuses into the material a distance

$$\delta = \sqrt{\alpha t}, \qquad \alpha = \frac{k}{\rho_m c}$$

and for a phenolic ablator $\alpha = 1.43 \times 10^{-7}$ square metres per second, so

$$\delta_{6\,\text{s}} = 0.93\ \text{mm}, \qquad \delta_{25\,\text{s}} = 1.89\ \text{mm}$$

a ratio of 2.04, which is the square root of the time ratio. Transient conduction into a heated structure, and the thermal stresses it produces, is the other half of the material problem and is treated across [Altman and Chang 1965][research_altman_chang_1965], [Tate 1969][research_tate_1969], [Moyer and Wool 1970][research_moyer_wool_1970], [Moyer and Wool 1970, Aerotherm Charring Material Therma][research_moyer_wool_1970_2], [Rathjen 1977][research_rathjen_1977], [Adelman 1979][research_adelman_1979], [Ko and Fields 1987][research_ko_fields_1987], [Milos and Chen 2010][research_milos_chen_2010], [Weng and Martin 2014][research_weng_martin_2014], [Weng and Martin 2015][research_weng_martin_2015], [Tatar 2020][research_tatar_2020], [Wang et al 2024][research_wang_2024].

**The X-17's pulse heats half the depth an intercontinental re-entry does.** A material can therefore pass an X-17 test on its surface behaviour and still fail on what happens to the structure behind it, which is a failure mode the vehicle was structurally incapable of finding.

**The X-17's contribution here is that it exposed real materials at full scale to a correct heat flux.** That is a screening capability, and it is exactly what the trade described above preserved.

### The Structure and Staging

The first stage lifts a 4,831 kilogramme vehicle on 48,000 pounds force, giving a launch thrust-to-weight ratio of

$$\frac{T}{W} = \frac{48{,}000}{10{,}650} = 4.51$$

which is high and appropriate for a vehicle that must clear the dense atmosphere quickly. The upper stages together develop 137,650 pounds force, or 612 kilonewtons, against a much smaller remaining mass, which is what supplies the 2,339 metres per second of downward velocity computed above.

Solid propellant was the only sensible choice. It requires no pumps, tolerates being stored, and can be fired in any attitude, which matters greatly for a stage that ignites while pointing at the ground after a ballistic coast. Motor design and case work of the period appear in [Bua 1963][research_bua_1963] and [Harris 1963][research_harris_1963], internal insulation in [WALTON and SIMMONS 1962][research_walton_simmons_1962] and [Sale 1964][research_sale_1964], and the ablation problem inside the motor itself in [KUBY et al 1962][research_kuby_1962]. Multistage trajectory optimisation is treated in [Boyce 1963][research_boyce_1963]. Solid motor performance, grain and case design, nozzle erosion, and the staging problem generally are covered by [LAWRENCE 1945][research_lawrence_1945], [Matthews 1957][research_matthews_1957], [CAMPBELL 1962][research_campbell_1962], [KUBY 1964][research_kuby_1964], [PARKER and SUMMERFIELD 1964][research_parker_summerfield_1964], [HORTON 1964][research_horton_1964], [PRICE 1964][research_price_1964], [FONG 1964][research_fong_1964], [Perlmutter and DePierre 1965][research_perlmutter_depierre_1965], [DEMORE 1965][research_demore_1965], [Landers et al 1991][research_landers_1991], [Pamadi et al 2006][research_pamadi_2006], [Clayton 2017][research_clayton_2017], [Clayton 2017, Arc Jet Test and Analysis of Asbes][research_clayton_2017_2].

### Stability and the Attitude Problem

A vehicle that coasts to apogee, tips over, and then fires has an attitude problem the flight-mechanics literature of the period addresses directly. The vehicle must be pointed correctly before the second stage lights, and any angle of attack at ignition is amplified by the burn.

Spin stabilisation is the usual answer and appears in [Levine et al 1960][research_levine_1960]. Re-entry body dynamics generally are treated in [Holway and Prislin 1966][research_holway_prislin_1966], with later work on roll behaviour and angle-of-attack control in [KRYVORUKA and ASHURST 1973][research_kryvoruka_ashurst_1973] and [Platus 1980][research_platus_1980]. The ballistic missile free-flight problem in general is [WHEELON 1959][research_wheelon_1959]. The dynamics of a blunt body descending through an atmosphere, including the angle-of-attack oscillation that any imperfect release produces and the roll behaviour that couples into it, are treated in [Nix 1959][research_nix_1959], [SCHERMERHORN and DEMERITTE 1960][research_schermerhorn_demeritte_1960], [Prislin 1966][research_prislin_1966], [Price 1967][research_price_1967], [Platus 1967][research_platus_1967], [BARBERA 1981][research_barbera_1981], [MCDOWELL and WILLIAMSON 1982][research_mcdowell_williamson_1982], [Ivanov et al 2007][research_ivanov_2007], [Schoenenberger 2013][research_schoenenberger_2013], [Kazemba et al 2013][research_kazemba_2013], [Sevier et al 2016][research_sevier_2016], [Bharghava 2024][research_bharghava_2024]. **A vehicle that tips over and fires has an attitude error at ignition by construction**, and the literature above is what says how large it is allowed to be.

### Instrumentation, Which Is the Actual Product

The vehicle exists to return numbers, and at these conditions returning numbers is difficult. Thermocouples must survive a surface that is being consumed, telemetry must work through a partially ionised layer, and the whole record must be transmitted before the article is destroyed.

The free-flight heating measurement technique and its interpretation are the direct subject of [Murphy and Rubesin 1965][research_murphy_rubesin_1965], and a closely comparable free-flight heat transfer and ablation measurement on a blunted body appears in [Winters 1964][research_winters_1964]. Comparison of tunnel and flight data for an instrumented hypersonic rocket is in [Maydew 1964][research_maydew_1964]. The technique of measuring aerodynamic heating on a body in free flight, and of extracting a heat transfer coefficient from a temperature history, is its own discipline and runs through [Liddell et al 1947][research_liddell_1947], [Hamaker et al 1953][research_hamaker_1953], [Rogers and K. 1953][research_rogers_k_1953], [Charters et al 1955][research_charters_1955], [Compton et al 1960][research_compton_1960], [Reeves and Threlkeld 1963][research_reeves_threlkeld_1963], [Welton 1965][research_welton_1965], [Dayman 1965][research_dayman_1965], [Development 1984][research_development_1984], [Strawa et al 1990][research_strawa_1990], [Kidner 1993][research_kidner_1993], [Whitmore and Moes 1994][research_whitmore_moes_1994], [Guelhan et al 2012][research_guelhan_2012], [Hergert et al 2017][research_hergert_2017].

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

**A factor of 2.7 rests on where transition happens**, which is a first-order design question rather than a refinement. Transition on blunted bodies is treated in [Jillie and Hopkins 1961][research_jillie_hopkins_1961] and [MASAKI and YAKURA 1968][research_masaki_yakura_1968], and the laminar and turbulent heating comparison is the substance of [Murphy and Rubesin 1965][research_murphy_rubesin_1965]. **Transition is the least settled quantity in the whole calculation and has stayed that way**, across [TIFFORD 1945][research_tifford_1945], [Scherrer et al 1949][research_scherrer_1949], [Lee 1953][research_lee_1953], [Lange and Gieseler 1953][research_lange_gieseler_1953], [STETSON 1960][research_stetson_1960], [Adcock et al 1965][research_adcock_1965], [Adcock et al 1967][research_adcock_1967], [Finson et al 1980][research_finson_1980], [Reed and Abu-Mostafa 1982][research_reed_abu_mostafa_1982], [Ting et al 1986][research_ting_1986], [Reda 2001][research_reda_2001], [Maslov 2001][research_maslov_2001], [Kimmel 2003][research_kimmel_2003], [Ren et al 2019][research_ren_2019], [Patrick 2019][research_patrick_2019], [Miró and Pinna 2020][research_miro_pinna_2020].

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

That makes this an unusually apt subject for a contemporary survey. The X-17 partitioned a re-entry into what it could reproduce and what it could not, and **the modern field has the same partition with better instruments on both sides of it.** What follows is organised by that partition rather than by chronology.

### Prediction Replaced Measurement as the Primary Tool, and Then Needed Validating

The largest single change is that the heat flux the X-17 went to such lengths to produce is now, in the first instance, computed. Aerothermodynamic prediction for entry and hypersonic vehicles is a mature computational discipline, in [Franze and Barz 2025][research_franze_barz_2025], [Franze and Barz 2025, Correction][research_franze_barz_2025_2], [G and G 2025][research_g_g_2025], [Gokul and Malaikannan 2025][research_gokul_malaikannan_2025], [Horing et al 2025][research_horing_2025], [Huang et al 2025][research_huang_2025], [Jiang and Deng 2025][research_jiang_deng_2025], [Khraibut and Gai 2025][research_khraibut_gai_2025], [Chen et al 2026][research_chen_2026], [He et al 2026][research_he_2026], [Peng and Wang 2026][research_peng_wang_2026], [Rajput et al 2026][research_rajput_2026], [Rataczak et al 2026][research_rataczak_2026], [Rizzi et al 2026][research_rizzi_2026], [Yang et al 2026][research_yang_2026], [Zhang et al 2026, Thermal model test and multi-scale][research_zhang_2026_2].

**That does not remove the need for the X-17's kind of data. It relocates it.** A computed heat flux is only as good as the models inside it, and the field's central activity is now validation against experiment rather than measurement in place of theory. **The X-17 produced numbers because there was no alternative. Its modern equivalent produces numbers to check a code against**, which is a different epistemic role for the same measurement.

### The Facilities Still Cannot Do It

Arc-heated facilities remain the workhorse for material screening and are still being characterised rather than trusted, as in [Gokcen and Alunni 2019][research_gokcen_alunni_2019] and [Alunni et al 2019][research_alunni_2019]. Shock tubes and expansion tubes remain the way to reach genuine flight enthalpy for very short times, as in [Chandel et al 2019][research_chandel_2019]. The facility literature is large and is largely about characterising the imperfection rather than removing it, across [Deng et al 2025][research_deng_2025], [Kim et al 2025][research_kim_2025], [Kim et al 2025, Experimental study of nose-tip blu][research_kim_2025_2], [Li et al 2025][research_li_2025], [Novak et al 2025][research_novak_2025], [Oswald et al 2025][research_oswald_2025], [Pitakarnnop and Wiwatapinai 2025][research_pitakarnnop_wiwatapinai_2025], [Shen et al 2025][research_shen_2025], [Shi et al 2025][research_shi_2025], [Sreenivasulu et al 2025][research_sreenivasulu_2025], [Choi et al 2026][research_choi_2026], [Dean et al 2026][research_dean_2026], [Raybon et al 2026][research_raybon_2026], [Surujhlal et al 2026][research_surujhlal_2026], [Willier et al 2026][research_willier_2026].

**The X-17's fundamental problem, that no ground facility gives full enthalpy at full scale for full duration, is unresolved seventy years later.** What has changed is that the shortfall is now measured and quoted rather than argued about, which is the same improvement this article credits the X-17's own partition with.

### The Chemistry the X-17 Missed Is the Modern Subject

The nonequilibrium chemistry the X-17 surrendered is now the central computational difficulty, in [Kline et al 2019][research_kline_2019] and the radiation modelling of [Winter et al 2019][research_winter_2019]. The current work spans vibrational relaxation and two-temperature models, state-to-state kinetics, rarefied and direct-simulation methods, and the catalytic wall boundary condition that decides how much of the dissociation energy is returned to the surface, across [Aiken et al 2025][research_aiken_2025], [Carter and Boyd 2025][research_carter_boyd_2025], [He et al 2025][research_he_2025], [Leonov and Miles 2025][research_leonov_miles_2025], [Li and Jing 2025][research_li_jing_2025], [Melnik et al 2025][research_melnik_2025], [Varma and Zhong 2025][research_varma_zhong_2025], [Wang et al 2025][research_wang_2025], [Chinnappan and Kim 2026][research_chinnappan_kim_2026], [Chu et al 2026][research_chu_2026], [Gao et al 2026][research_gao_2026], [Guo and Cao 2026][research_guo_cao_2026], [Jiang et al 2026][research_jiang_2026], [Liu et al 2026, Flow regimes and transitions in hy][research_liu_2026_2], [Pu et al 2026][research_pu_2026], [Tong et al 2026][research_tong_2026], [Varma and Zhong 2026][research_varma_zhong_2026], [Weifeng et al 2026][research_weifeng_2026].

**What the X-17 gave up because nobody could use it is now the part that is hardest to get right**, which is a reversal worth stating. The vehicle surrendered the chemistry as the cheapest of three requirements to abandon. **It is now the most expensive**, because everything else in a modern prediction is comparatively well posed and the chemistry is where the model form uncertainty lives.

### Ablation Became a Predictive Model Rather Than a Screening Result

The X-17 could tell a designer that a material survived. Modern practice demands a model that says why and predicts the recession, as in [Wang et al 2019][research_wang_2019]. Charring ablator response, pyrolysis, surface chemistry, and recession prediction are now coupled models validated against arc-jet and flight data, in [Austin 2025][research_austin_2025], [Cai and Gao 2025][research_cai_gao_2025], [Cheng et al 2025][research_cheng_2025], [Duncheskie and Isaacson 2025][research_duncheskie_isaacson_2025], [Li et al 2025, Ablation resistance evaluation of][research_li_2025_3], [Maout et al 2025][research_maout_2025], [Song and Kim 2025][research_song_kim_2025], [Tomasian and Jennings 2025][research_tomasian_jennings_2025], [Wang et al 2025, Arc Jet Testing and Modeling Study][research_wang_2025_3], [Cabrera and West 2026][research_cabrera_west_2026], [Girish and Manu 2026][research_girish_manu_2026], [Guan et al 2026][research_guan_2026], [Li et al 2026][research_li_2026], [Tański et al 2026][research_tanski_2026], [Wang et al 2026][research_wang_2026], [Xu et al 2026][research_xu_2026].

**That is a change in kind rather than degree**, and it is what allows a heat shield to be designed rather than selected. The X-17 could report that a material survived. **A modern model reports how much of it is left and why**, which is the difference between a screening result and an engineering prediction.

### Radiation Became Its Own Modelling Problem

The article computes that the X-17 saw about one part in 111 of an intercontinental re-entry's radiative heating, and that lunar return is a further factor of forty-seven above that. Radiation is now modelled spectrally and coupled to the flow, in [Albqmi and Sivanandam 2024][research_albqmi_sivanandam_2024], [Bazhinov and Kravtsov 2025][research_bazhinov_kravtsov_2025], [Gai and Cao 2025][research_gai_cao_2025], [Johnston and Mazaheri 2025][research_johnston_mazaheri_2025], [Maloney et al 2025][research_maloney_2025], [Wang 2025, Anvil-radiation diurnal interactio][research_wang_2025_2], [Zarubina 2025][research_zarubina_2025], [Zhang et al 2025, Nitrogen molecular radiation in hy][research_zhang_2025_2], [Zhu et al 2025][research_zhu_2025], [Gai and Cao 2026][research_gai_cao_2026], [Tabuchi and Fujino 2026][research_tabuchi_fujino_2026], [Zjavka 2026][research_zjavka_2026].

**That work exists because the X-17's regime is the last one in which radiation could safely be ignored.** Everything faster has to account for it, which is why the subject grew immediately after the period this article covers rather than during it.

### Thermal Protection Stopped Being Ablation Alone

The X-17 screened ablators because at 1,398 watts per square centimetre nothing else works, and this article proves that with a Stefan-Boltzmann calculation. The modern field has more options, because it has materials that did not exist, in [Belrhiti et al 2025][research_belrhiti_2025], [Chen et al 2025, Effect of Thermal Protection Syste][research_chen_2025_2], [Daryabeigi and Kurz 2025][research_daryabeigi_kurz_2025], [Lv et al 2025][research_lv_2025], [Wang et al 2025, Ultra-high temperature mechanical][research_wang_2025_4], [Wang and Han 2025][research_wang_han_2025], [Yue et al 2025][research_yue_2025], [Alberts et al 2026][research_alberts_2026], [He et al 2026, Thermal erosion characteristics of][research_he_2026_2], [Jing et al 2026][research_jing_2026], [Kim and Choi 2026][research_kim_choi_2026], [M et al 2026][research_m_2026], [Vigil and Pérez 2026][research_vigil_perez_2026], [Zhou et al 2026][research_zhou_2026].

**The re-radiation argument this article makes is exactly the calculation that ultra-high temperature ceramics are designed against.** A material that survives 4,127 kelvin passively would have changed the X-17's conclusion entirely, and the hafnium carbide that appears in the article's own table as the single survivor is precisely the family the current literature pursues. **The answer has moved from consuming the surface to not consuming it**, at least at the fluxes where that is possible.

### Free Flight Is Still the Ground Truth

Rough-wall turbulent heat transfer measured in hypersonic free flight, in [Wilder and Prabhu 2019][research_wilder_prabhu_2019], is the direct descendant of the X-17's technique at small scale. Flight experiments, entry probe reconstructions, sounding rocket payloads and sample return capsules continue to supply the data that no facility can, across [Dutta and Karlgaard 2024][research_dutta_karlgaard_2024], [An et al 2025][research_an_2025], [Bishop et al 2025][research_bishop_2025], [KC et al 2025][research_kc_2025], [Murphy and Browne 2025][research_murphy_browne_2025], [Ozaki et al 2025][research_ozaki_2025], [Silber et al 2025][research_silber_2025], [Silber and Bowman 2025][research_silber_bowman_2025], [Nagata et al 2026][research_nagata_2026], [Nishikawa et al 2026][research_nishikawa_2026], [Saito et al 2026][research_saito_2026], [Silber 2026][research_silber_2026], [Silber and Scamfer 2026][research_silber_scamfer_2026], [Takahashi et al 2026][research_takahashi_2026].

**Flight remains the only place the real condition occurs**, which is the same reason the X-17 was built. The difference is that a modern flight experiment is instrumented to validate a specific model rather than to characterise an environment, and it is usually a by-product of a mission flown for another purpose rather than a vehicle built solely to obtain the condition. **Nobody now builds an X-17**, and the reason is not that the problem was solved.

### Transition Is Still the Least Settled Quantity

The article computes a turbulent heating penalty of 2.70 at the quoted Reynolds number and notes that where transition occurs is therefore a first-order design question. **That question is still open.** Hypersonic transition prediction, instability and receptivity theory, and roughness-induced transition remain active, in [Li et al 2024, Gas Kinetic Scheme Coupled with Hi][research_li_2024_3], [Liu et al 2024, Control of roughness-induced trans][research_liu_2024_2], [Liu et al 2024, Roughness-Induced Transition in Su][research_liu_2024_3], [Caillaud et al 2025][research_caillaud_2025], [Hollis 2025][research_hollis_2025], [Ji et al 2025][research_ji_2025], [Zou et al 2025][research_zou_2025], [Cerminara et al 2026][research_cerminara_2026], [Johnston et al 2026][research_johnston_2026], [Milman and Karp 2026][research_milman_karp_2026], [Varma et al 2026][research_varma_2026], [Zeng et al 2026][research_zeng_2026], [Zhang et al 2026][research_zhang_2026], [Zhang et al 2026, Effect of wall mass injection on r][research_zhang_2026_3].

**Seventy years on, the single quantity that most strongly multiplies the heat load is the one least reliably predicted**, which is a fair summary of why hypersonic vehicles are still conservatively designed.

### Entry Descent and Landing Is Where the Problem Actually Went

The X-17's descendants are not weapons but planetary entry systems, and the discipline that inherited its question calls itself entry, descent and landing, in [Deng et al 2023][research_deng_2023], [Dimino et al 2023][research_dimino_2023], [Jara et al 2023][research_jara_2023], [Karlgaard et al 2023][research_karlgaard_2023], [Dutta et al 2024][research_dutta_2024], [He 2024][research_he_2024], [Jalaja et al 2024][research_jalaja_2024], [Vershinin et al 2024][research_vershinin_2024], [Zubiaurre et al 2024][research_zubiaurre_2024], [Dutta 2025][research_dutta_2025], [Saranathan 2025][research_saranathan_2025], [Son et al 2025][research_son_2025], [Chadalavada et al 2026][research_chadalavada_2026], [Venkatapathy and Hash 2026][research_venkatapathy_hash_2026].

**The transfer is direct.** A Mars entry vehicle is a blunt body with an ablative or insulative shield whose ballistic coefficient decides the altitude at which it decelerates, which is precisely the Allen-Eggers argument this article uses. **What changed is that the atmosphere is somebody else's**, and the density profile carries an uncertainty no terrestrial calculation has to bear.

### Knowing What Is Wrong Became a Discipline

This article's contribution is a partition into reproduced and not reproduced, with ratios attached. The modern equivalent is uncertainty quantification, which does the same job continuously and with error bars, in [Zhao et al 2020][research_zhao_2020], [Li et al 2021, Uncertainty analysis of the high p][research_li_2021_2], [Salem et al 2021][research_salem_2021], [Xie et al 2021][research_xie_2021], [Wang and Luo 2022][research_wang_luo_2022], [Tian et al 2023, Sensitivity analysis and safety ad][research_tian_2023_2], [Blanco 2025][research_blanco_2025], [Deng et al 2026][research_deng_2026], [Graham and Fossati 2026][research_graham_fossati_2026], [Somé and Niyobuhungiro 2026][research_some_niyobuhungiro_2026].

**That is the deepest continuity between the X-17 and the present.** The vehicle's value was never that it reproduced a re-entry, because it did not. **It was that the people using its data knew which parts to trust**, and the modern field has turned that judgement into a method.

### The Subject Is Funded Again

Hypersonic flight has returned as a defence and access-to-space priority, and with it the whole apparatus of thermal protection, aerothermodynamic prediction and test infrastructure, in [Das et al 2024][research_das_2024], [Dongre 2024][research_dongre_2024], [Cai and Zhuang 2025][research_cai_zhuang_2025], [Liu et al 2025][research_liu_2025], [Qi et al 2025][research_qi_2025], [Shao et al 2025][research_shao_2025], [Wang et al 2025, Working medium selection for Hyper][research_wang_2025_5], [Zhao et al 2025][research_zhao_2025], [Li et al 2026, Sequential convex optimization for][research_li_2026_3], [Luo et al 2026][research_luo_2026], [Thompson 2026][research_thompson_2026], [Xue et al 2026][research_xue_2026], [Zhang et al 2026, Suboptimal Stochastic Differential][research_zhang_2026_5], [Zhao et al 2026][research_zhao_2026].

**The X-17's problem is being re-encountered rather than remembered.** A vehicle that must sustain hypersonic flight for minutes rather than survive a re-entry for seconds inverts the article's total-heat-load finding, since it is the integral rather than the peak that binds.

### An Application That Did Not Exist in 1956

Nothing in the X-17's world anticipated the modern problem of making a spacecraft **fail** to survive re-entry. Design for demise, breakup modelling, and re-entry casualty risk are now regulatory concerns, in [Santos and Sampaio 2021][research_santos_sampaio_2021], [Department Of Astrophysics 2022][research_department_of_astrophysics_2022], [Wilmer et al 2022][research_wilmer_2022], [Ferreira et al 2024][research_ferreira_2024], [Gao et al 2024, Reentry Risk and Safety Assessment][research_gao_2024_2], [Bettinger et al 2025][research_bettinger_2025], [Jain and Hastings 2025][research_jain_hastings_2025], [Ocaya and Malevu 2025][research_ocaya_malevu_2025], [Chen et al 2026, Design-for-demise-oriented modelin][research_chen_2026_3], [Liu et al 2026, Survivability assessment of conste][research_liu_2026_4], [Navaz and Ntantis 2026][research_navaz_ntantis_2026], [Öztürk et al 2026][research_ozturk_2026].

**The relations are identical and the objective is reversed.** Ballistic coefficient, ablation rate and heat load are computed in order to guarantee that a structure comes apart and burns rather than to guarantee that it does not. **The X-17 measured how to survive. Its instruments now serve an industry that sometimes needs the opposite**, which is the sharpest available illustration of how general the underlying physics turned out to be.

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

### The Shape of the Reference Base

Of 422 research references, **214 predate 2019 and 208 do not**, so the base divides almost exactly in half. The distribution is 33 documents from before 1960, 94 from the 1960s and 1970s, 43 from the 1980s and 1990s, 44 from 2000 to 2018, and 208 from 2019 onward. The contemporary half is large because **the X-17's question was never answered**, so surveying the present state of it is surveying an open problem rather than an epilogue.

**The pre-1960 material was nearly absent until it was looked for.** The first harvest used a 1985 cutoff on its period sweep, which let later work crowd out the contemporaneous literature, and the pool held only twenty records from before 1960 for a vehicle that flew in 1956. A second sweep with a 1960 cutoff took that to 157. **The documents the X-17's own engineers would have been reading are the most valuable primary material this article can have**, and they had to be asked for specifically.

**Thirty candidate references were rejected across the two reference passes after being read rather than matched.** A title search for refractory returned furnace fillers, the mullitization of alumina raw material, silicon carbide power converters, and the near-infrared reflectance of rocks for asteroid science. A search for high temperature air returned a pneumatic air motor. A search for chemical kinetics returned the oxidation of n-butane and chemiluminescence in propane-butane flames. A search for heat flux returned microchannel heat sinks. A search for nonequilibrium returned a two-temperature Ising model. A search for ionisation returned electron impact on krypton. A search for demise, meaning the deliberate destruction of a spacecraft during re-entry, returned a paper on dataveillance and the demise of interpretive flexibility. And a search for thermal protection system returned the development of a passive thermal protection system for **divers**, which is a wetsuit.

**The pattern is the one the previous article recorded, that a keyword diagnostic inside a field is useless outside it**, and the only method that catches it is reading the titles. A counter-observation is worth recording alongside it. An automated relevance scan run after insertion flagged a further ten citations, and **every one proved to be a false positive of the scan's own keyword list**, including a ceramic-heated tunnel, high-emissivity coatings, and expansion-tube flow characterisation. The reading step finds real defects and the automated step generates noise in both directions.

## Epistemic State

**Historical fact.** A quarter-scale vehicle flew in May 1955 and the first full X-17 in April 1956, with 25 further flights to March 1957. The vehicle was a three-stage solid-propellant rocket using a Thiokol XM20 Sergeant first stage and Recruit upper stages. Hemispherical, cubic paraboloid, and blunt nose shapes were flown. The blunt shape was adopted for Atlas and Titan. The vehicle served as a Polaris flight test vehicle in 1957 and 1958 and boosted the three Operation Argus high-altitude nuclear tests in 1958. A flight on 24 April 1957 reached 9,000 miles per hour.

**Disputed in the record.** The overall length, given as 40 feet 4 inches and as 41 feet. The apogee, given as about 100 miles, about 500,000 feet, and 250 miles. This article resolves neither.

**Engineering analysis, reproducible from the stated inputs.** The requirement that a passive surface reach 4,127 kelvin to reject the matched flux, which exceeds the melting point of tungsten and the sublimation point of graphite and therefore makes ablation mandatory rather than merely convenient. The Allen-Eggers results, namely a peak deceleration of 43.7 g independent of ballistic coefficient, a velocity at peak heating of 5,925 metres per second also independent of it, and peak-heating altitudes from 31.3 kilometres at a ballistic coefficient of 1,000 down to 12.3 at 13,983. **The ballistic coefficient ceiling above which the X-17 cannot match the heating rate at any altitude, at about 6,300 kilogrammes per square metre even at sea level and about 2,500 at a practical floor.** That the assumed reference corresponds to 1,453. The radiative heating ratios of 110.7 against an intercontinental re-entry and 5,162 against lunar return. The Damköhler ratio of 16.09. The ablation mass loss and recession figures. The thermal penetration depths of 0.93 and 1.89 millimetres. The turbulent heating penalty of 2.70. The free-fall speed of 1,684 metres per second from the lower apogee and the resulting factor of 13.63 in heating rate. The required density ratio of 27.74 and the matching altitude of 13.97 kilometres. The equal heating rates of 1,398 watts per square centimetre. The stagnation enthalpies of 8.094 and 24.50 megajoules per kilogramme and their ratio of 3.027. The binary scaling ratio of 9.25. The nose radius heating ratios. The ballistic coefficient ratio of 3.33. The Reynolds numbers.

**Inference, and clearly labelled.** That the heating-rate match was fitted to the class of body the vehicle was built to test, rather than being a general capability, follows from the ballistic-coefficient ceiling and the coincidence that the assumed reference sits below it. It is an argument from internal consistency and not from any document. That the X-17 surrendered velocity deliberately rather than as a consequence of what its motors happened to deliver is an inference from the design's internal consistency and not from any document. That the chemistry it missed did not matter for the 1956 question is an argument about what could be used rather than about what was true. That the shape result was a confirmation rather than a discovery follows from the publication order of the theory.

**What the record does not settle and this article does not claim.** What the X-17 actually measured, since no flight data were located. What trajectory any flight followed. Whether the ablators screened on it behaved the same way at intercontinental enthalpy, which is precisely the extrapolation the partial simulation does not license.

**What the publication review added and what it changed.** The contemporary survey was expanded from 38 references to 208 across twelve fields. Two of its observations bear on the article's own argument rather than merely extending it. **The chemistry the X-17 surrendered as the cheapest of three requirements is now the most expensive**, because everything else in a modern prediction is comparatively well posed and the chemistry is where the model form uncertainty lives. And **the relations are now run in reverse for spacecraft demise**, where ballistic coefficient, ablation rate and heat load are computed to guarantee that a structure comes apart rather than that it survives, which is the sharpest available demonstration of how general the physics turned out to be.

**Information postdating the editorial date.** The contemporary literature section is written from current knowledge per the series convention.

## Out of Scope

The Atlas and Titan programmes themselves are treated only as consumers of this vehicle's result. Operation Argus is named and its physics is not discussed. The Polaris programme is outside this article. The detailed chemistry of dissociating air is cited rather than derived. No attempt is made to reconstruct an actual flight trajectory. Radiative heating is treated only through its velocity scaling, which is sufficient to show that the X-17 could not reproduce it, and the shock-layer radiation transport that would be needed to compute it properly is cited rather than derived.

## Conclusion

The X-17 fired rockets downward because falling was not enough, and the margin is not close. **Free fall from its own apogee would have produced under a tenth of the heating rate it was built to study**, and the whole peculiar architecture follows from that single factor of fourteen.

What it bought with that architecture was a partial simulation, and the partition is sharp. **It reproduced the heating rate exactly, at full scale, with a real material, and it reproduced 33 percent of the stagnation enthalpy and therefore none of the chemistry.** The nonequilibrium state it missed by a factor of nine in the wrong direction, and the total heat load by a factor of four.

**That trade was correct for 1956 and would be wrong today**, which is the most interesting thing about the vehicle. The programme surrendered the gas physics because nobody could compute it, and kept the heat flux because everybody needed to design against it. Seventy years later the chemistry is the hard part, the material response is modelled rather than screened, and no facility has yet been built that reproduces the whole condition. **The X-17's compromise has been inherited rather than resolved.**

## References

### Books

- [Anderson 2019 Hypersonic and High-Temperature Gas Dynamics][book_anderson_2019]
- [Jenkins Landis and Miller 2003 American X-Vehicles, An Inventory X-1 to X-50][book_jenkins_landis_miller_2003]
- [Miller 2001 The X-Planes, X-1 to X-45][book_miller_2001]
- [Neufeld 1990 The Development of Ballistic Missiles in the United States Air Force][book_neufeld_1990]

[book_anderson_2019]: https://openlibrary.org/search?q=Anderson+Hypersonic+and+High+Temperature+Gas+Dynamics
[book_jenkins_landis_miller_2003]: https://openlibrary.org/search?q=Jenkins+Landis+Miller+American+X+Vehicles
[book_miller_2001]: https://openlibrary.org/search?q=Miller+The+X+Planes+X-1+to+X-45
[book_neufeld_1990]: https://openlibrary.org/search?q=Neufeld+Development+of+Ballistic+Missiles+United+States+Air+Force

### Reference

- [Atlas][ref_atlas]
- [Lockheed X-17][ref_x17]
- [Operation Argus][ref_argus]
- [Titan][ref_titan]

[ref_argus]: https://en.wikipedia.org/wiki/Operation_Argus
[ref_atlas]: https://en.wikipedia.org/wiki/SM-65_Atlas
[ref_titan]: https://en.wikipedia.org/wiki/HGM-25A_Titan_I
[ref_x17]: https://en.wikipedia.org/wiki/Lockheed_X-17

### Related Post

- [X-1][related_post_a298_bell_x1]
- [X-10][related_post_a307_north_american_x10]
- [X-11][related_post_a308_convair_x11]
- [X-12][related_post_a309_convair_x12]
- [X-13][related_post_a310_ryan_x13]
- [X-14][related_post_a311_bell_x14]
- [X-15][related_post_a312_north_american_x15]
- [X-16][related_post_a313_bell_x16]
- [X-2][related_post_a299_bell_x2]
- [X-3][related_post_a300_douglas_x3]
- [X-4][related_post_a301_northrop_x4]
- [X-5][related_post_a302_bell_x5]
- [X-6][related_post_a303_convair_x6]
- [X-7][related_post_a304_lockheed_x7]
- [X-8][related_post_a305_aerojet_x8]
- [X-9][related_post_a306_bell_x9]
- [X-Planes series][related_post_a297_xplanes_framing]

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

### Research

- [Adcock et al 1965][research_adcock_1965]
- [Adcock et al 1967][research_adcock_1967]
- [Adelman 1979][research_adelman_1979]
- [Aiken et al 2025][research_aiken_2025]
- [Alberts et al 2026][research_alberts_2026]
- [Albqmi and Sivanandam 2024][research_albqmi_sivanandam_2024]
- [Allen and Eggers 1953][research_allen_eggers_1953]
- [Altman and Chang 1965][research_altman_chang_1965]
- [Alunni et al 2019][research_alunni_2019]
- [An et al 2025][research_an_2025]
- [Archer 1963][research_archer_1963]
- [Aroesty 1963][research_aroesty_1963]
- [Ashkenas and Wegener 1961][research_ashkenas_wegener_1961]
- [Austin 2025][research_austin_2025]
- [Bachynski et al 1959][research_bachynski_1959]
- [Bachynski et al 1960][research_bachynski_1960]
- [Balakalyani and Jagadeesh 2019][research_balakalyani_jagadeesh_2019]
- [BARBERA 1981][research_barbera_1981]
- [Bazhinov and Kravtsov 2025][research_bazhinov_kravtsov_2025]
- [Beckwith and Cohen 1963][research_beckwith_cohen_1963]
- [Belrhiti et al 2025][research_belrhiti_2025]
- [Bettinger et al 2025][research_bettinger_2025]
- [Bharghava 2024][research_bharghava_2024]
- [Bird 1960][research_bird_1960]
- [Bishop et al 2025][research_bishop_2025]
- [Blanco 2025][research_blanco_2025]
- [Bleakney et al 1949][research_bleakney_1949]
- [Boyce 1963][research_boyce_1963]
- [Bradley et al 1981][research_bradley_1981]
- [Bua 1963][research_bua_1963]
- [Cabrera and West 2026][research_cabrera_west_2026]
- [Cai and Gao 2025][research_cai_gao_2025]
- [Cai and Zhuang 2025][research_cai_zhuang_2025]
- [Caillaud et al 2025][research_caillaud_2025]
- [CAMPBELL 1962][research_campbell_1962]
- [Carter and Boyd 2025][research_carter_boyd_2025]
- [Cerminara et al 2026][research_cerminara_2026]
- [Chadalavada et al 2026][research_chadalavada_2026]
- [Chandel et al 2019][research_chandel_2019]
- [Chapman 1963][research_chapman_1963]
- [Charters et al 1955][research_charters_1955]
- [Chazot et al 2008][research_chazot_2008]
- [Chen and Milos 2011][research_chen_milos_2011]
- [Chen et al 2025, Effect of Thermal Protection Syste][research_chen_2025_2]
- [Chen et al 2026][research_chen_2026]
- [Chen et al 2026, Design-for-demise-oriented modelin][research_chen_2026_3]
- [Cheng et al 2025][research_cheng_2025]
- [Chinnappan and Kim 2026][research_chinnappan_kim_2026]
- [Choi et al 2026][research_choi_2026]
- [CHRUSCIEL and POOL 1983][research_chrusciel_pool_1983]
- [Chu et al 2026][research_chu_2026]
- [Clayton 2017][research_clayton_2017]
- [Clayton 2017, Arc Jet Test and Analysis of Asbes][research_clayton_2017_2]
- [Clemente and Ferrarella 2010][research_clemente_ferrarella_2010]
- [Cohen and Homer 1959][research_cohen_homer_1959]
- [Collen et al 2023][research_collen_2023]
- [Compton and Cooper 1964][research_compton_cooper_1964]
- [Compton et al 1960][research_compton_1960]
- [Compton et al 1963][research_compton_1963]
- [Conti 1961][research_conti_1961]
- [Coulson and Furukawa 1960][research_coulson_furukawa_1960]
- [CRESCI et al 1960][research_cresci_1960]
- [Cruden 2011][research_cruden_2011]
- [Curry 2004][research_curry_2004]
- [Daryabeigi and Kurz 2025][research_daryabeigi_kurz_2025]
- [Das et al 2024][research_das_2024]
- [Davis 1964][research_davis_1964]
- [Dayman 1962][research_dayman_1962]
- [Dayman 1965][research_dayman_1965]
- [Dean et al 2026][research_dean_2026]
- [Deininger and King 1988][research_deininger_king_1988]
- [DEMORE 1965][research_demore_1965]
- [Deng et al 2023][research_deng_2023]
- [Deng et al 2025][research_deng_2025]
- [Deng et al 2026][research_deng_2026]
- [Department Of Astrophysics 2022][research_department_of_astrophysics_2022]
- [Desai et al 1999][research_desai_1999]
- [Development 1984][research_development_1984]
- [Dickey and Haacker 1963][research_dickey_haacker_1963]
- [Dimino et al 2023][research_dimino_2023]
- [Dohnanyi 1964][research_dohnanyi_1964]
- [Dongre 2024][research_dongre_2024]
- [Duncheskie and Isaacson 2025][research_duncheskie_isaacson_2025]
- [Dutta 2025][research_dutta_2025]
- [Dutta and Karlgaard 2024][research_dutta_karlgaard_2024]
- [Dutta et al 2024][research_dutta_2024]
- [Eggers et al 1958][research_eggers_1958]
- [Eilertson and Wing 1966][research_eilertson_wing_1966]
- [Emmons 1951][research_emmons_1951]
- [Feldman et al 2019][research_feldman_2019]
- [Ferreira et al 2024][research_ferreira_2024]
- [Fiala and Hillier 2003][research_fiala_hillier_2003]
- [FILLER 1960][research_filler_1960]
- [Finson et al 1980][research_finson_1980]
- [Fiorello 1961][research_fiorello_1961]
- [FONG 1964][research_fong_1964]
- [Foyle 1963][research_foyle_1963]
- [Franze and Barz 2025][research_franze_barz_2025]
- [Franze and Barz 2025, Correction][research_franze_barz_2025_2]
- [Freno et al 2021][research_freno_2021]
- [G and G 2025][research_g_g_2025]
- [Gai and Cao 2025][research_gai_cao_2025]
- [Gai and Cao 2026][research_gai_cao_2026]
- [GAI et al 1985][research_gai_1985]
- [Gao et al 2024, Reentry Risk and Safety Assessment][research_gao_2024_2]
- [Gao et al 2026][research_gao_2026]
- [Gardner 1961][research_gardner_1961]
- [Gildfind 2019][research_gildfind_2019]
- [Girish and Manu 2026][research_girish_manu_2026]
- [Gokcen and Alunni 2019][research_gokcen_alunni_2019]
- [Gokul and Malaikannan 2025][research_gokul_malaikannan_2025]
- [Gonzales 1981][research_gonzales_1981]
- [Graham and Fossati 2026][research_graham_fossati_2026]
- [Green and Davy 1981][research_green_davy_1981]
- [GREENE and WILLIAMSON 1981][research_greene_williamson_1981]
- [Guan et al 2026][research_guan_2026]
- [Guelhan et al 2012][research_guelhan_2012]
- [Gunderson 1962][research_gunderson_1962]
- [Guo and Cao 2026][research_guo_cao_2026]
- [GUPTA et al 1990][research_gupta_1990]
- [Hamaker et al 1953][research_hamaker_1953]
- [Han et al 2020][research_han_2020]
- [Hansen 1959][research_hansen_1959]
- [Hansen and Heims 1958][research_hansen_heims_1958]
- [Hanson 2000][research_hanson_2000]
- [Harris 1963][research_harris_1963]
- [He 2024][research_he_2024]
- [He et al 2025][research_he_2025]
- [He et al 2026][research_he_2026]
- [He et al 2026, Thermal erosion characteristics of][research_he_2026_2]
- [Hergert et al 2017][research_hergert_2017]
- [Herman and Melnik 1962][research_herman_melnik_1962]
- [Hermann et al 1962][research_hermann_1962]
- [HIDALGO 1960][research_hidalgo_1960]
- [Holden 2004][research_holden_2004]
- [Hollis 2025][research_hollis_2025]
- [Holway and Prislin 1966][research_holway_prislin_1966]
- [Horing et al 2025][research_horing_2025]
- [HORTON 1964][research_horton_1964]
- [Huang et al 2025][research_huang_2025]
- [Ivanov et al 2007][research_ivanov_2007]
- [Jaffe 1986][research_jaffe_1986]
- [Jahn and Grosse 1959][research_jahn_grosse_1959]
- [Jain and Hastings 2025][research_jain_hastings_2025]
- [Jalaja et al 2024][research_jalaja_2024]
- [Jara et al 2023][research_jara_2023]
- [Ji et al 2025][research_ji_2025]
- [Jiang and Deng 2025][research_jiang_deng_2025]
- [Jiang et al 2026][research_jiang_2026]
- [Jillie and Hopkins 1961][research_jillie_hopkins_1961]
- [Jing et al 2026][research_jing_2026]
- [Johnston and Mazaheri 2025][research_johnston_mazaheri_2025]
- [Johnston et al 2012][research_johnston_2012]
- [Johnston et al 2026][research_johnston_2026]
- [Jonas 1953][research_jonas_1953]
- [Josyula and Bailey 2009][research_josyula_bailey_2009]
- [KANE 1951][research_kane_1951]
- [Karlgaard et al 2023][research_karlgaard_2023]
- [Kaul 1986][research_kaul_1986]
- [Kazemba et al 2013][research_kazemba_2013]
- [KC et al 2025][research_kc_2025]
- [Kerr 2006][research_kerr_2006]
- [Khraibut and Gai 2025][research_khraibut_gai_2025]
- [Kidner 1993][research_kidner_1993]
- [Kim and Choi 2026][research_kim_choi_2026]
- [Kim et al 2020][research_kim_2020]
- [Kim et al 2025][research_kim_2025]
- [Kim et al 2025, Experimental study of nose-tip blu][research_kim_2025_2]
- [Kimmel 2003][research_kimmel_2003]
- [Kline et al 2019][research_kline_2019]
- [KNIGHT and QUINN 1971][research_knight_quinn_1971]
- [Ko and Fields 1987][research_ko_fields_1987]
- [Korabelnikov and Kuranov 2002][research_korabelnikov_kuranov_2002]
- [Korzun et al 2013][research_korzun_2013]
- [KRYVORUKA and ASHURST 1973][research_kryvoruka_ashurst_1973]
- [KUBY 1964][research_kuby_1964]
- [KUBY et al 1962][research_kuby_1962]
- [Kumar et al 1980][research_kumar_1980]
- [KVASHINA and KOROBEINIKOV 1961][research_kvashina_korobeinikov_1961]
- [Landers et al 1991][research_landers_1991]
- [Lange and Gieseler 1953][research_lange_gieseler_1953]
- [LAWRENCE 1945][research_lawrence_1945]
- [Lee 1953][research_lee_1953]
- [Lee et al 1994][research_lee_1994]
- [Lefevre et al 2022][research_lefevre_2022]
- [Leiser et al 1992][research_leiser_1992]
- [Leonov and Miles 2025][research_leonov_miles_2025]
- [Levine et al 1960][research_levine_1960]
- [Levy and Mc Devitt 1964][research_levy_mc_devitt_1964]
- [Li 1981][research_li_1981]
- [LI and GEIGER 1957][research_li_geiger_1957]
- [Li and Jing 2025][research_li_jing_2025]
- [Li et al 2021, Uncertainty analysis of the high p][research_li_2021_2]
- [Li et al 2024, Gas Kinetic Scheme Coupled with Hi][research_li_2024_3]
- [Li et al 2025][research_li_2025]
- [Li et al 2025, Ablation resistance evaluation of][research_li_2025_3]
- [Li et al 2026][research_li_2026]
- [Li et al 2026, Sequential convex optimization for][research_li_2026_3]
- [Liddell et al 1947][research_liddell_1947]
- [Lin 1961][research_lin_1961]
- [Lin et al 1962][research_lin_1962]
- [LINCOLN 1981][research_lincoln_1981]
- [Linder 1961][research_linder_1961]
- [Liu et al 2002][research_liu_2002]
- [Liu et al 2024, Control of roughness-induced trans][research_liu_2024_2]
- [Liu et al 2024, Roughness-Induced Transition in Su][research_liu_2024_3]
- [Liu et al 2025][research_liu_2025]
- [Liu et al 2026, Flow regimes and transitions in hy][research_liu_2026_2]
- [Liu et al 2026, Survivability assessment of conste][research_liu_2026_4]
- [Luce and Jr 1949][research_luce_jr_1949]
- [Lundquist 1952][research_lundquist_1952]
- [Luo et al 2026][research_luo_2026]
- [Lv et al 2025][research_lv_2025]
- [M et al 2026][research_m_2026]
- [Ma et al 2022][research_ma_2022]
- [MACK 1954][research_mack_1954]
- [Maloney et al 2025][research_maloney_2025]
- [Manjhi and Kumar 2020][research_manjhi_kumar_2020]
- [Manning 2009][research_manning_2009]
- [Maout et al 2025][research_maout_2025]
- [Maples 1973][research_maples_1973]
- [MASAKI and YAKURA 1968][research_masaki_yakura_1968]
- [Maslov 2001][research_maslov_2001]
- [Mathauser et al 1960][research_mathauser_1960]
- [Matthews 1957][research_matthews_1957]
- [Maydew 1964][research_maydew_1964]
- [MCDOWELL and WILLIAMSON 1982][research_mcdowell_williamson_1982]
- [McGilvray et al 2024][research_mcgilvray_2024]
- [Melnik et al 2025][research_melnik_2025]
- [Milman and Karp 2026][research_milman_karp_2026]
- [Milos and Chen 2010][research_milos_chen_2010]
- [Miró and Pinna 2020][research_miro_pinna_2020]
- [Mizoguchi et al 2006][research_mizoguchi_2006]
- [Moore et al 1948][research_moore_1948]
- [Moss and Kumar 1981][research_moss_kumar_1981]
- [Moyer and Wool 1970][research_moyer_wool_1970]
- [Moyer and Wool 1970, Aerotherm Charring Material Therma][research_moyer_wool_1970_2]
- [Murphy and Browne 2025][research_murphy_browne_2025]
- [Murphy and Rubesin 1965][research_murphy_rubesin_1965]
- [Nagata et al 2026][research_nagata_2026]
- [Nardo and Sadler 1962][research_nardo_sadler_1962]
- [Navaz and Ntantis 2026][research_navaz_ntantis_2026]
- [Neice et al 1960][research_neice_1960]
- [Nishikawa et al 2026][research_nishikawa_2026]
- [Nix 1959][research_nix_1959]
- [Nomura 1983][research_nomura_1983]
- [Novak et al 2025][research_novak_2025]
- [Ocaya and Malevu 2025][research_ocaya_malevu_2025]
- [Oguchi 1962][research_oguchi_1962]
- [Oswald et al 2025][research_oswald_2025]
- [Ozaki et al 2025][research_ozaki_2025]
- [Page 1963][research_page_1963]
- [Paglia et al 2019][research_paglia_2019]
- [Palmer and Knox 1960][research_palmer_knox_1960]
- [Pamadi et al 2006][research_pamadi_2006]
- [Pan et al 2021][research_pan_2021]
- [Park and Balakrishnan 1985][research_park_balakrishnan_1985]
- [Park et al 1983][research_park_1983]
- [Park et al 1983, Ablation of carbonaceous materials][research_park_1983_2]
- [PARKER and SUMMERFIELD 1964][research_parker_summerfield_1964]
- [Patrick 2019][research_patrick_2019]
- [Pei et al 2021][research_pei_2021]
- [Pekker and Cambier 2006][research_pekker_cambier_2006]
- [Peng and Wang 2026][research_peng_wang_2026]
- [Perepezko 2002][research_perepezko_2002]
- [Perepezko 2006][research_perepezko_2006]
- [Perlmutter and DePierre 1965][research_perlmutter_depierre_1965]
- [Pitakarnnop and Wiwatapinai 2025][research_pitakarnnop_wiwatapinai_2025]
- [Platus 1967][research_platus_1967]
- [Platus 1980][research_platus_1980]
- [PRICE 1964][research_price_1964]
- [Price 1967][research_price_1967]
- [Prislin 1966][research_prislin_1966]
- [Pu et al 2026][research_pu_2026]
- [Qi et al 2025][research_qi_2025]
- [Rajput et al 2026][research_rajput_2026]
- [Rataczak et al 2026][research_rataczak_2026]
- [Rathjen 1977][research_rathjen_1977]
- [Ravichandran et al 2025][research_ravichandran_2025]
- [Raybon et al 2026][research_raybon_2026]
- [Reda 2001][research_reda_2001]
- [Reed and Abu-Mostafa 1982][research_reed_abu_mostafa_1982]
- [Reeves and Threlkeld 1963][research_reeves_threlkeld_1963]
- [Ren et al 2019][research_ren_2019]
- [Rizzi et al 2026][research_rizzi_2026]
- [Roberts 1960][research_roberts_1960]
- [Rogers and K. 1953][research_rogers_k_1953]
- [Rose and Stankevics 1963][research_rose_stankevics_1963]
- [Saito et al 2026][research_saito_2026]
- [Sale 1964][research_sale_1964]
- [Salem et al 2021][research_salem_2021]
- [Santos and Sampaio 2021][research_santos_sampaio_2021]
- [Saranathan 2025][research_saranathan_2025]
- [Scalabrin and Boyd 2005][research_scalabrin_boyd_2005]
- [Scherberg and Rubin 1953][research_scherberg_rubin_1953]
- [SCHERMERHORN and DEMERITTE 1960][research_schermerhorn_demeritte_1960]
- [Scherrer et al 1949][research_scherrer_1949]
- [Schoenenberger 2013][research_schoenenberger_2013]
- [SEIDMAN 1960][research_seidman_1960]
- [Sevier et al 2016][research_sevier_2016]
- [Shao et al 2025][research_shao_2025]
- [Shen et al 2025][research_shen_2025]
- [Sherman 1951][research_sherman_1951]
- [Shi et al 2020][research_shi_2020]
- [Shi et al 2025][research_shi_2025]
- [Si et al 2019][research_si_2019]
- [Silber 2026][research_silber_2026]
- [Silber and Bowman 2025][research_silber_bowman_2025]
- [Silber and Scamfer 2026][research_silber_scamfer_2026]
- [Silber et al 2025][research_silber_2025]
- [Singh and Tiwari 1990][research_singh_tiwari_1990]
- [Singh et al 1991][research_singh_1991]
- [Somé and Niyobuhungiro 2026][research_some_niyobuhungiro_2026]
- [Son et al 2025][research_son_2025]
- [Song and Kim 2025][research_song_kim_2025]
- [Speyer and Womble 1971][research_speyer_womble_1971]
- [Sreenivasulu et al 2025][research_sreenivasulu_2025]
- [Stalder and Nielsen 1954][research_stalder_nielsen_1954]
- [STETSON 1960][research_stetson_1960]
- [Strawa et al 1990][research_strawa_1990]
- [Su et al 2021][research_su_2021]
- [Sun and Zhu 2019][research_sun_zhu_2019]
- [Surujhlal et al 2026][research_surujhlal_2026]
- [Surzhikov 2020, Numerical Analysis of Shock Layer][research_surzhikov_2020_2]
- [Swann and South 1961][research_swann_south_1961]
- [SWIGART 1962][research_swigart_1962]
- [Tabuchi and Fujino 2026][research_tabuchi_fujino_2026]
- [Takahashi and Teshima 1985][research_takahashi_teshima_1985]
- [Takahashi et al 2026][research_takahashi_2026]
- [Tang et al 2021][research_tang_2021]
- [Tashakkor et al 2011][research_tashakkor_2011]
- [Tatar 2020][research_tatar_2020]
- [Tate 1969][research_tate_1969]
- [Tauber and Sutton 1991][research_tauber_sutton_1991]
- [Tauber et al 2012][research_tauber_2012]
- [Tański et al 2026][research_tanski_2026]
- [Thompson 2026][research_thompson_2026]
- [Thornton 1981][research_thornton_1981]
- [Tian et al 2023, Sensitivity analysis and safety ad][research_tian_2023_2]
- [TIFFORD 1945][research_tifford_1945]
- [Ting et al 1986][research_ting_1986]
- [Tomasian and Jennings 2025][research_tomasian_jennings_2025]
- [Tong et al 2026][research_tong_2026]
- [Trimpi 1962][research_trimpi_1962]
- [Trimpi 1962, A Preliminary Theoretical Study of][research_trimpi_1962_2]
- [Trout 1963][research_trout_1963]
- [VAGLIG-LAURIN 1960][research_vaglig_laurin_1960]
- [Varma and Zhong 2025][research_varma_zhong_2025]
- [Varma and Zhong 2026][research_varma_zhong_2026]
- [Varma et al 2026][research_varma_2026]
- [Vasudevan and Leonard 2002][research_vasudevan_leonard_2002]
- [Venkatapathy and Hash 2026][research_venkatapathy_hash_2026]
- [Vershinin et al 2024][research_vershinin_2024]
- [Viegas and Howe 1962][research_viegas_howe_1962]
- [Vigil and Pérez 2026][research_vigil_perez_2026]
- [Vinh and Lin 1982][research_vinh_lin_1982]
- [Walker and Wolowicz 1960][research_walker_wolowicz_1960]
- [WALTON and SIMMONS 1962][research_walton_simmons_1962]
- [Wang 2025, Anvil-radiation diurnal interactio][research_wang_2025_2]
- [Wang and Han 2025][research_wang_han_2025]
- [Wang and Jiang 2020][research_wang_jiang_2020]
- [Wang and Luo 2022][research_wang_luo_2022]
- [Wang et al 2019][research_wang_2019]
- [Wang et al 2024][research_wang_2024]
- [Wang et al 2025][research_wang_2025]
- [Wang et al 2025, Arc Jet Testing and Modeling Study][research_wang_2025_3]
- [Wang et al 2025, Ultra-high temperature mechanical][research_wang_2025_4]
- [Wang et al 2025, Working medium selection for Hyper][research_wang_2025_5]
- [Wang et al 2026][research_wang_2026]
- [Warmbrod 1963][research_warmbrod_1963]
- [Wegener and Lobb 1952][research_wegener_lobb_1952]
- [Weifeng et al 2026][research_weifeng_2026]
- [Welton 1965][research_welton_1965]
- [Weng and Martin 2014][research_weng_martin_2014]
- [Weng and Martin 2015][research_weng_martin_2015]
- [Wheeler et al 1986][research_wheeler_1986]
- [WHEELON 1959][research_wheelon_1959]
- [Whitmore and Moes 1994][research_whitmore_moes_1994]
- [Wilder and Prabhu 2019][research_wilder_prabhu_2019]
- [Willier et al 2026][research_willier_2026]
- [Wilmer et al 2022][research_wilmer_2022]
- [Winter et al 2011][research_winter_2011]
- [Winter et al 2019][research_winter_2019]
- [Winters 1964][research_winters_1964]
- [Winters and Bracalente 1961][research_winters_bracalente_1961]
- [Xie et al 2021][research_xie_2021]
- [Xu et al 2026][research_xu_2026]
- [Xue et al 2026][research_xue_2026]
- [YANG et al 1985][research_yang_1985]
- [Yang et al 2022][research_yang_2022]
- [Yang et al 2026][research_yang_2026]
- [Yee et al 1961][research_yee_1961]
- [Yue et al 2025][research_yue_2025]
- [Yun and Mason 1962][research_yun_mason_1962]
- [Yungster and Radhakrishnan 2001][research_yungster_radhakrishnan_2001]
- [Zarubina 2025][research_zarubina_2025]
- [Zeng et al 2026][research_zeng_2026]
- [Zhang et al 2010][research_zhang_2010]
- [Zhang et al 2025, Nitrogen molecular radiation in hy][research_zhang_2025_2]
- [Zhang et al 2026][research_zhang_2026]
- [Zhang et al 2026, Effect of wall mass injection on r][research_zhang_2026_3]
- [Zhang et al 2026, Suboptimal Stochastic Differential][research_zhang_2026_5]
- [Zhang et al 2026, Thermal model test and multi-scale][research_zhang_2026_2]
- [Zhao and Zhou 2013][research_zhao_zhou_2013]
- [Zhao et al 2020][research_zhao_2020]
- [Zhao et al 2025][research_zhao_2025]
- [Zhao et al 2026][research_zhao_2026]
- [Zhou et al 2012][research_zhou_2012]
- [ZHOU et al 2025][research_zhou_2025]
- [Zhou et al 2026][research_zhou_2026]
- [Zhu et al 2025][research_zhu_2025]
- [Zjavka 2026][research_zjavka_2026]
- [Zoby et al 1988][research_zoby_1988]
- [Zou et al 2025][research_zou_2025]
- [Zubiaurre et al 2024][research_zubiaurre_2024]
- [Öztürk et al 2026][research_ozturk_2026]

[research_adcock_1965]: https://ntrs.nasa.gov/citations/19650020242
[research_adcock_1967]: https://ntrs.nasa.gov/citations/19670010557
[research_adelman_1979]: https://ntrs.nasa.gov/citations/19800004187
[research_aiken_2025]: https://doi.org/10.1063/5.0294530
[research_alberts_2026]: https://doi.org/10.1016/j.actamat.2026.122613
[research_albqmi_sivanandam_2024]: https://doi.org/10.3390/computation12030043
[research_allen_eggers_1953]: https://ntrs.nasa.gov/citations/20050019430
[research_altman_chang_1965]: https://ntrs.nasa.gov/citations/19650025525
[research_alunni_2019]: https://ntrs.nasa.gov/citations/20190026513
[research_an_2025]: https://doi.org/10.1061/jaeeez.aseng-6056
[research_archer_1963]: https://doi.org/10.21236/ad0431737
[research_aroesty_1963]: https://ntrs.nasa.gov/citations/19630011721
[research_ashkenas_wegener_1961]: https://ntrs.nasa.gov/citations/19630015283
[research_austin_2025]: https://doi.org/10.33599/sj.v61no6.03
[research_bachynski_1959]: https://doi.org/10.1109/tap.1959.1144720
[research_bachynski_1960]: https://doi.org/10.1109/jrproc.1960.287607
[research_balakalyani_jagadeesh_2019]: https://doi.org/10.1016/j.measurement.2018.12.099
[research_barbera_1981]: https://doi.org/10.2514/6.1981-290
[research_bazhinov_kravtsov_2025]: https://doi.org/10.64740/ittum.1.1.6
[research_beckwith_cohen_1963]: https://ntrs.nasa.gov/citations/19630029531
[research_belrhiti_2025]: https://doi.org/10.1111/ijac.15161
[research_bettinger_2025]: https://doi.org/10.1016/j.asr.2024.11.044
[research_bharghava_2024]: https://doi.org/10.1016/j.ijheatfluidflow.2024.109413
[research_bird_1960]: https://doi.org/10.2514/8.8718
[research_bishop_2025]: https://doi.org/10.1121/10.0041857
[research_blanco_2025]: https://doi.org/10.1080/14697688.2025.2471347
[research_bleakney_1949]: https://doi.org/10.1063/1.1741395
[research_boyce_1963]: https://ntrs.nasa.gov/citations/19630006926
[research_bradley_1981]: https://ntrs.nasa.gov/citations/19820030400
[research_bua_1963]: https://doi.org/10.21236/ad0415435
[research_cabrera_west_2026]: https://doi.org/10.2514/1.a36431
[research_cai_gao_2025]: https://doi.org/10.1177/01455613241259368
[research_cai_zhuang_2025]: https://doi.org/10.1016/j.dt.2024.11.001
[research_caillaud_2025]: https://doi.org/10.1103/physrevfluids.10.043902
[research_campbell_1962]: https://doi.org/10.21236/ad0292258
[research_carter_boyd_2025]: https://doi.org/10.2514/1.t7119
[research_cerminara_2026]: https://doi.org/10.2514/1.j066062
[research_chadalavada_2026]: https://doi.org/10.2514/1.a36525
[research_chandel_2019]: https://ntrs.nasa.gov/citations/20180006681
[research_chapman_1963]: https://ntrs.nasa.gov/citations/19630005427
[research_charters_1955]: https://ntrs.nasa.gov/citations/19930093745
[research_chazot_2008]: https://doi.org/10.2514/6.2008-1252
[research_chen_2025_2]: https://doi.org/10.34133/space.0260
[research_chen_2026]: https://doi.org/10.1063/5.0335632
[research_chen_2026_3]: https://doi.org/10.1016/j.ast.2025.111267
[research_chen_milos_2011]: https://ntrs.nasa.gov/citations/20160000306
[research_cheng_2025]: https://doi.org/10.3390/aerospace12090772
[research_chinnappan_kim_2026]: https://doi.org/10.1007/s00162-026-00786-0
[research_choi_2026]: https://doi.org/10.1016/j.actaastro.2026.03.015
[research_chrusciel_pool_1983]: https://doi.org/10.2514/6.1983-1424
[research_chu_2026]: https://doi.org/10.3389/fchem.2026.1869326
[research_clayton_2017]: https://ntrs.nasa.gov/citations/20170004465
[research_clayton_2017_2]: https://ntrs.nasa.gov/citations/20170005378
[research_clemente_ferrarella_2010]: https://doi.org/10.2514/6.2010-5067
[research_cohen_homer_1959]: https://doi.org/10.1115/1.4008418
[research_collen_2023]: https://doi.org/10.2514/1.t6693
[research_compton_1960]: https://ntrs.nasa.gov/citations/19630010655
[research_compton_1963]: https://ntrs.nasa.gov/citations/19630015360
[research_compton_cooper_1964]: https://ntrs.nasa.gov/citations/19640032970
[research_conti_1961]: https://ntrs.nasa.gov/citations/19980227274
[research_coulson_furukawa_1960]: https://doi.org/10.21236/ad0251122
[research_cresci_1960]: https://doi.org/10.2514/8.8571
[research_cruden_2011]: https://doi.org/10.1063/1.3562792
[research_curry_2004]: https://ntrs.nasa.gov/citations/20100042593
[research_daryabeigi_kurz_2025]: https://ntrs.nasa.gov/citations/20250004276
[research_das_2024]: https://doi.org/10.1049/icp.2024.0657
[research_davis_1964]: https://doi.org/10.21236/ad0601998
[research_dayman_1962]: https://ntrs.nasa.gov/citations/19620006382
[research_dayman_1965]: https://ntrs.nasa.gov/citations/19650053701
[research_dean_2026]: https://ntrs.nasa.gov/citations/20260005677
[research_deininger_king_1988]: https://ntrs.nasa.gov/citations/19880000287
[research_demore_1965]: https://doi.org/10.2514/6.1965-183
[research_deng_2023]: https://doi.org/10.1029/2021rs007275
[research_deng_2025]: https://doi.org/10.1109/tps.2025.3595738
[research_deng_2026]: https://doi.org/10.1016/j.ijthermalsci.2026.110927
[research_department_of_astrophysics_2022]: https://doi.org/10.47191/etj/v7i8.02
[research_desai_1999]: https://ntrs.nasa.gov/citations/19990087367
[research_development_1984]: https://ntrs.nasa.gov/citations/19840026325
[research_dickey_haacker_1963]: https://ntrs.nasa.gov/citations/19660024017
[research_dimino_2023]: https://doi.org/10.3390/app13052783
[research_dohnanyi_1964]: https://ntrs.nasa.gov/citations/19650014698
[research_dongre_2024]: https://doi.org/10.53555/e2ha7809
[research_duncheskie_isaacson_2025]: https://doi.org/10.1177/01455613251366042
[research_dutta_2024]: https://doi.org/10.2514/1.a35771
[research_dutta_2025]: https://doi.org/10.2514/1.a36119
[research_dutta_karlgaard_2024]: https://doi.org/10.2514/1.a36101
[research_eggers_1958]: https://ntrs.nasa.gov/citations/19930085175
[research_eilertson_wing_1966]: https://ntrs.nasa.gov/citations/19660024689
[research_emmons_1951]: https://doi.org/10.1090/qam/38773
[research_feldman_2019]: https://ntrs.nasa.gov/citations/20190030273
[research_ferreira_2024]: https://doi.org/10.1029/2024gl109280
[research_fiala_hillier_2003]: https://doi.org/10.2514/6.2003-6965
[research_filler_1960]: https://doi.org/10.21236/ad0243068
[research_finson_1980]: https://doi.org/10.21236/ada082438
[research_fiorello_1961]: https://doi.org/10.21236/ad0250741
[research_fong_1964]: https://doi.org/10.2514/6.1964-125
[research_foyle_1963]: https://ntrs.nasa.gov/citations/19630029160
[research_franze_barz_2025]: https://doi.org/10.1007/s12567-024-00588-2
[research_franze_barz_2025_2]: https://doi.org/10.1007/s12567-025-00610-1
[research_freno_2021]: https://doi.org/10.1016/j.jcp.2020.109752
[research_g_g_2025]: https://doi.org/10.1063/5.0262265
[research_gai_1985]: https://doi.org/10.2514/6.1985-973
[research_gai_cao_2025]: https://doi.org/10.1063/5.0274336
[research_gai_cao_2026]: https://doi.org/10.1016/j.ijthermalsci.2025.110573
[research_gao_2024_2]: https://doi.org/10.1007/s42405-023-00652-x
[research_gao_2026]: https://doi.org/10.47176/jafm.19.2.3660
[research_gardner_1961]: https://ntrs.nasa.gov/citations/19620001485
[research_gildfind_2019]: https://doi.org/10.1007/s00193-019-00903-5
[research_girish_manu_2026]: https://doi.org/10.1016/j.ast.2026.112316
[research_gokcen_alunni_2019]: https://ntrs.nasa.gov/citations/20190028252
[research_gokul_malaikannan_2025]: https://doi.org/10.1017/aer.2025.10023
[research_gonzales_1981]: https://www.osti.gov/biblio/6625473
[research_graham_fossati_2026]: https://doi.org/10.2514/1.a36522
[research_green_davy_1981]: https://ntrs.nasa.gov/citations/19810054678
[research_greene_williamson_1981]: https://doi.org/10.2514/6.1981-168
[research_guan_2026]: https://doi.org/10.1016/j.carbon.2025.120974
[research_guelhan_2012]: https://doi.org/10.2514/6.2012-5819
[research_gunderson_1962]: https://ntrs.nasa.gov/citations/19700025116
[research_guo_cao_2026]: https://doi.org/10.1063/5.0340255
[research_gupta_1990]: https://doi.org/10.2514/6.1990-1697
[research_hamaker_1953]: https://ntrs.nasa.gov/citations/19930090972
[research_han_2020]: https://doi.org/10.1016/j.ast.2019.105673
[research_hansen_1959]: https://ntrs.nasa.gov/citations/19980237039
[research_hansen_heims_1958]: https://ntrs.nasa.gov/citations/19930085278
[research_hanson_2000]: https://doi.org/10.21236/ada384344
[research_harris_1963]: https://doi.org/10.21236/ad0402393
[research_he_2024]: https://doi.org/10.1049/icp.2024.0646
[research_he_2025]: https://doi.org/10.3390/en18133417
[research_he_2026]: https://doi.org/10.3390/electronics15143132
[research_he_2026_2]: https://doi.org/10.1016/j.jeurceramsoc.2025.117835
[research_hergert_2017]: https://ntrs.nasa.gov/citations/20180006640
[research_herman_melnik_1962]: https://doi.org/10.21236/ad0404197
[research_hermann_1962]: https://ntrs.nasa.gov/citations/19620005896
[research_hidalgo_1960]: https://doi.org/10.2514/8.5240
[research_holden_2004]: https://doi.org/10.2514/6.2004-916
[research_hollis_2025]: https://doi.org/10.2514/1.a36008
[research_holway_prislin_1966]: https://ntrs.nasa.gov/citations/19660061364
[research_horing_2025]: https://doi.org/10.2514/1.t7165
[research_horton_1964]: https://doi.org/10.2514/6.1964-133
[research_huang_2025]: https://doi.org/10.1016/j.ast.2025.110283
[research_ivanov_2007]: https://doi.org/10.2514/6.2007-4145
[research_jaffe_1986]: https://ntrs.nasa.gov/citations/19860062230
[research_jahn_grosse_1959]: https://doi.org/10.1063/1.1724420
[research_jain_hastings_2025]: https://doi.org/10.2514/1.a36069
[research_jalaja_2024]: https://doi.org/10.1007/s11668-023-01835-0
[research_jara_2023]: https://doi.org/10.1016/j.ast.2023.108571
[research_ji_2025]: https://doi.org/10.1017/jfm.2025.10378
[research_jiang_2026]: https://doi.org/10.1016/j.ast.2026.111768
[research_jiang_deng_2025]: https://doi.org/10.1088/1742-6596/2977/1/012094
[research_jillie_hopkins_1961]: https://ntrs.nasa.gov/citations/19980227973
[research_jing_2026]: https://doi.org/10.1016/j.applthermaleng.2026.130617
[research_johnston_2012]: https://doi.org/10.2514/6.2012-2866
[research_johnston_2026]: https://doi.org/10.2514/1.a36722
[research_johnston_mazaheri_2025]: https://doi.org/10.2514/1.a36291
[research_jonas_1953]: https://doi.org/10.4271/530236
[research_josyula_bailey_2009]: https://doi.org/10.1007/978-3-540-85168-4_105
[research_kane_1951]: https://doi.org/10.2514/8.1924
[research_karlgaard_2023]: https://doi.org/10.2514/1.a35440
[research_kaul_1986]: https://ntrs.nasa.gov/citations/19870040509
[research_kazemba_2013]: https://ntrs.nasa.gov/citations/20140011217
[research_kc_2025]: https://doi.org/10.1785/0220250019
[research_kerr_2006]: https://ntrs.nasa.gov/citations/20060052411
[research_khraibut_gai_2025]: https://doi.org/10.1063/5.0260326
[research_kidner_1993]: https://doi.org/10.2172/10185958
[research_kim_2020]: https://doi.org/10.1016/j.ijheatmasstransfer.2019.119059
[research_kim_2025]: https://doi.org/10.1007/s00348-025-04117-7
[research_kim_2025_2]: https://doi.org/10.1038/s41598-025-22323-5
[research_kim_choi_2026]: https://doi.org/10.3390/ma19020303
[research_kimmel_2003]: https://doi.org/10.2514/6.2003-772
[research_kline_2019]: https://ntrs.nasa.gov/citations/20200002702
[research_knight_quinn_1971]: https://doi.org/10.2514/6.1971-415
[research_ko_fields_1987]: https://ntrs.nasa.gov/citations/19880001007
[research_korabelnikov_kuranov_2002]: https://doi.org/10.2514/6.2002-913
[research_korzun_2013]: https://ntrs.nasa.gov/citations/20140000600
[research_kryvoruka_ashurst_1973]: https://doi.org/10.2514/6.1973-183
[research_kuby_1962]: https://doi.org/10.21236/ad0282734
[research_kuby_1964]: https://doi.org/10.2514/6.1964-158
[research_kumar_1980]: https://ntrs.nasa.gov/citations/19800052239
[research_kvashina_korobeinikov_1961]: https://doi.org/10.2514/8.5699
[research_landers_1991]: https://ntrs.nasa.gov/citations/19910057071
[research_lange_gieseler_1953]: https://doi.org/10.21236/ad0015004
[research_lawrence_1945]: https://doi.org/10.2514/8.4056
[research_lee_1953]: https://doi.org/10.21236/ad0018796
[research_lee_1994]: https://ntrs.nasa.gov/citations/19950003738
[research_lefevre_2022]: https://doi.org/10.2514/1.j061771
[research_leiser_1992]: https://ntrs.nasa.gov/citations/19920000019
[research_leonov_miles_2025]: https://doi.org/10.1364/oe.567227
[research_levine_1960]: https://ntrs.nasa.gov/citations/19980227768
[research_levy_mc_devitt_1964]: https://ntrs.nasa.gov/citations/19650019778
[research_li_1981]: https://ntrs.nasa.gov/citations/19820045478
[research_li_2021_2]: https://doi.org/10.1016/j.flowmeasinst.2021.101891
[research_li_2024_3]: https://doi.org/10.3390/e26020173
[research_li_2025]: https://doi.org/10.1016/j.measen.2024.101693
[research_li_2025_3]: https://doi.org/10.1016/j.ceramint.2025.07.394
[research_li_2026]: https://doi.org/10.1007/s10765-026-03772-0
[research_li_2026_3]: https://doi.org/10.1088/1742-6596/3207/1/012072
[research_li_geiger_1957]: https://doi.org/10.2514/8.3759
[research_li_jing_2025]: https://doi.org/10.1063/5.0272815
[research_liddell_1947]: https://ntrs.nasa.gov/citations/20050081862
[research_lin_1961]: https://doi.org/10.1016/0032-0633(61)90008-3
[research_lin_1962]: https://doi.org/10.1063/1.1706575
[research_lincoln_1981]: https://doi.org/10.2514/6.1981-1057
[research_linder_1961]: https://doi.org/10.1016/0032-0633(61)90153-2
[research_liu_2002]: https://doi.org/10.21236/ada403577
[research_liu_2024_2]: https://doi.org/10.1017/jfm.2024.564
[research_liu_2024_3]: https://doi.org/10.2514/1.j063833
[research_liu_2025]: https://doi.org/10.65904/3083-3450.2025.01.07
[research_liu_2026_2]: https://doi.org/10.1063/5.0323156
[research_liu_2026_4]: https://doi.org/10.1016/j.ast.2025.111057
[research_luce_jr_1949]: https://doi.org/10.21236/ada278113
[research_lundquist_1952]: https://doi.org/10.1063/1.1702215
[research_luo_2026]: https://doi.org/10.1016/j.icheatmasstransfer.2026.111984
[research_lv_2025]: https://doi.org/10.1016/j.tsep.2025.103744
[research_m_2026]: https://doi.org/10.1016/j.rineng.2026.110799
[research_ma_2022]: https://doi.org/10.54097/fcis.v2i1.3343
[research_mack_1954]: https://doi.org/10.21236/ad0032376
[research_maloney_2025]: https://doi.org/10.1029/2024jd042442
[research_manjhi_kumar_2020]: https://doi.org/10.1016/j.measurement.2020.108221
[research_manning_2009]: https://ntrs.nasa.gov/citations/20100000028
[research_maout_2025]: https://doi.org/10.1016/j.ijheatmasstransfer.2025.126999
[research_maples_1973]: https://doi.org/10.2172/4365695
[research_masaki_yakura_1968]: https://doi.org/10.2514/6.1968-1155
[research_maslov_2001]: https://doi.org/10.21236/ada408241
[research_mathauser_1960]: https://ntrs.nasa.gov/citations/19980227836
[research_matthews_1957]: https://doi.org/10.21236/ad0127419
[research_maydew_1964]: https://doi.org/10.2172/4000106
[research_mcdowell_williamson_1982]: https://doi.org/10.2514/6.1982-1376
[research_mcgilvray_2024]: https://doi.org/10.2514/1.t6892
[research_melnik_2025]: https://doi.org/10.1134/s0015462825603894
[research_milman_karp_2026]: https://doi.org/10.1017/jfm.2026.11633
[research_milos_chen_2010]: https://doi.org/10.2514/6.2010-4663
[research_miro_pinna_2020]: https://doi.org/10.1017/jfm.2020.129
[research_mizoguchi_2006]: https://doi.org/10.2514/6.2006-8068
[research_moore_1948]: https://ntrs.nasa.gov/citations/19930082291
[research_moss_kumar_1981]: https://ntrs.nasa.gov/citations/19810036320
[research_moyer_wool_1970]: https://doi.org/10.21236/ad0875062
[research_moyer_wool_1970_2]: https://doi.org/10.21236/ad0875392
[research_murphy_browne_2025]: https://doi.org/10.1088/1757-899x/1335/1/012001
[research_murphy_rubesin_1965]: https://ntrs.nasa.gov/citations/19660010795
[research_nagata_2026]: https://doi.org/10.2514/1.a36152
[research_nardo_sadler_1962]: https://doi.org/10.21236/ad0273837
[research_navaz_ntantis_2026]: https://doi.org/10.1007/s12567-026-00740-0
[research_neice_1960]: https://doi.org/10.2514/8.8546
[research_nishikawa_2026]: https://doi.org/10.1093/pasj/psaf156
[research_nix_1959]: https://ntrs.nasa.gov/citations/19630004882
[research_nomura_1983]: https://doi.org/10.2514/3.8296
[research_novak_2025]: https://doi.org/10.1016/j.measen.2024.101687
[research_ocaya_malevu_2025]: https://doi.org/10.1038/s44453-025-00007-8
[research_oguchi_1962]: https://doi.org/10.1016/b978-0-12-395595-1.50008-8
[research_oswald_2025]: https://doi.org/10.1016/j.vacuum.2025.114565
[research_ozaki_2025]: https://doi.org/10.1186/s40623-025-02271-0
[research_ozturk_2026]: https://doi.org/10.1016/j.jastp.2026.106829
[research_page_1963]: https://ntrs.nasa.gov/citations/19630015305
[research_paglia_2019]: https://doi.org/10.1016/j.polymdegradstab.2019.108979
[research_palmer_knox_1960]: https://doi.org/10.21236/ada952642
[research_pamadi_2006]: https://ntrs.nasa.gov/citations/20060055387
[research_pan_2021]: https://doi.org/10.1088/1742-6596/2012/1/012100
[research_park_1983]: https://ntrs.nasa.gov/citations/19830015075
[research_park_1983_2]: https://ntrs.nasa.gov/citations/19830051560
[research_park_balakrishnan_1985]: https://doi.org/10.2514/3.8910
[research_parker_summerfield_1964]: https://doi.org/10.2514/6.1964-126
[research_patrick_2019]: https://doi.org/10.1063/10.0000281
[research_pei_2021]: https://doi.org/10.1109/access.2021.3056517
[research_pekker_cambier_2006]: https://doi.org/10.1615/ihtc13.p4.80
[research_peng_wang_2026]: https://doi.org/10.1088/1742-6596/3256/1/012063
[research_perepezko_2002]: https://doi.org/10.21236/ada409935
[research_perepezko_2006]: https://doi.org/10.21236/ada442984
[research_perlmutter_depierre_1965]: https://doi.org/10.21236/ad0612646
[research_pitakarnnop_wiwatapinai_2025]: https://doi.org/10.1016/j.measen.2024.101688
[research_platus_1967]: https://doi.org/10.21236/ad0810587
[research_platus_1980]: https://doi.org/10.21236/ada093741
[research_price_1964]: https://doi.org/10.2514/6.1964-146
[research_price_1967]: https://ntrs.nasa.gov/citations/19670064188
[research_prislin_1966]: https://ntrs.nasa.gov/citations/19660053474
[research_pu_2026]: https://doi.org/10.1063/5.0336053
[research_qi_2025]: https://doi.org/10.3390/aerospace12070575
[research_rajput_2026]: https://doi.org/10.37868/dss.v7.id324
[research_rataczak_2026]: https://doi.org/10.2514/1.t7134
[research_rathjen_1977]: https://ntrs.nasa.gov/citations/19780007492
[research_ravichandran_2025]: https://doi.org/10.2514/1.a36225
[research_raybon_2026]: https://doi.org/10.1007/s00348-026-04279-y
[research_reda_2001]: https://ntrs.nasa.gov/citations/20010066492
[research_reed_abu_mostafa_1982]: https://ntrs.nasa.gov/citations/19820020703
[research_reeves_threlkeld_1963]: https://ntrs.nasa.gov/citations/19650025713
[research_ren_2019]: https://doi.org/10.1017/jfm.2019.756
[research_rizzi_2026]: https://doi.org/10.1007/s00158-026-04300-2
[research_roberts_1960]: https://ntrs.nasa.gov/citations/19980232223
[research_rogers_k_1953]: https://doi.org/10.21236/ad0013358
[research_rose_stankevics_1963]: https://doi.org/10.21236/ad0406269
[research_saito_2026]: https://doi.org/10.1029/2025jd045676
[research_sale_1964]: https://doi.org/10.21236/ad0609001
[research_salem_2021]: https://doi.org/10.4273/ijvss.13.1.13
[research_santos_sampaio_2021]: https://doi.org/10.34117/bjdv7n11-361
[research_saranathan_2025]: https://doi.org/10.1016/j.asr.2025.04.029
[research_scalabrin_boyd_2005]: https://doi.org/10.2514/6.2005-5203
[research_scherberg_rubin_1953]: https://doi.org/10.21236/ad0012619
[research_schermerhorn_demeritte_1960]: https://doi.org/10.21236/ad0319088
[research_scherrer_1949]: https://ntrs.nasa.gov/citations/19930085534
[research_schoenenberger_2013]: https://ntrs.nasa.gov/citations/20130003227
[research_seidman_1960]: https://doi.org/10.21236/ad0256185
[research_sevier_2016]: https://ntrs.nasa.gov/citations/20170001578
[research_shao_2025]: https://doi.org/10.3390/s25216621
[research_shen_2025]: https://doi.org/10.3390/aerospace12020120
[research_sherman_1951]: https://doi.org/10.2514/8.2037
[research_shi_2020]: https://doi.org/10.1016/j.compstruct.2020.112623
[research_shi_2025]: https://doi.org/10.1016/j.measurement.2024.116293
[research_si_2019]: https://doi.org/10.1063/1.5098543
[research_silber_2025]: https://doi.org/10.1785/0220250216
[research_silber_2026]: https://doi.org/10.1007/s00024-026-04013-z
[research_silber_bowman_2025]: https://doi.org/10.1785/0220250014
[research_silber_scamfer_2026]: https://doi.org/10.1785/0320260017
[research_singh_1991]: https://ntrs.nasa.gov/citations/19910057633
[research_singh_tiwari_1990]: https://ntrs.nasa.gov/citations/19900011634
[research_some_niyobuhungiro_2026]: https://doi.org/10.3390/math14030489
[research_son_2025]: https://doi.org/10.5139/jksas.2025.53.2.219
[research_song_kim_2025]: https://doi.org/10.1177/01455613231182234
[research_speyer_womble_1971]: https://ntrs.nasa.gov/citations/19720026711
[research_sreenivasulu_2025]: https://doi.org/10.61653/joast.v77i3.2025.1088
[research_stalder_nielsen_1954]: https://ntrs.nasa.gov/citations/19930083996
[research_stetson_1960]: https://doi.org/10.2514/8.8410
[research_strawa_1990]: https://ntrs.nasa.gov/citations/20000021400
[research_su_2021]: https://doi.org/10.1016/j.ast.2021.107200
[research_sun_zhu_2019]: https://doi.org/10.1063/1.5083820
[research_surujhlal_2026]: https://doi.org/10.1016/j.ast.2025.110846
[research_surzhikov_2020_2]: https://doi.org/10.1134/s001546282003012x
[research_swann_south_1961]: https://ntrs.nasa.gov/citations/20040003877
[research_swigart_1962]: https://doi.org/10.21236/ad0274612
[research_tabuchi_fujino_2026]: https://doi.org/10.2514/1.a36367
[research_takahashi_2026]: https://doi.org/10.2514/1.j065479
[research_takahashi_teshima_1985]: https://doi.org/10.1007/978-1-4613-2467-6_14
[research_tang_2021]: https://doi.org/10.1088/1742-6596/1748/5/052032
[research_tanski_2026]: https://doi.org/10.3390/ma19143028
[research_tashakkor_2011]: https://ntrs.nasa.gov/citations/20110014627
[research_tatar_2020]: https://doi.org/10.1007/s13369-019-04211-z
[research_tate_1969]: https://doi.org/10.21236/ad0696063
[research_tauber_2012]: https://ntrs.nasa.gov/citations/20120001655
[research_tauber_sutton_1991]: https://ntrs.nasa.gov/citations/19910048758
[research_thompson_2026]: https://doi.org/10.1063/10.0043197
[research_thornton_1981]: https://www.osti.gov/biblio/6611421
[research_tian_2023_2]: https://doi.org/10.1016/j.enbuild.2023.113603
[research_tifford_1945]: https://doi.org/10.2514/8.11230
[research_ting_1986]: https://ntrs.nasa.gov/citations/19860055208
[research_tomasian_jennings_2025]: https://doi.org/10.1148/rg.240238
[research_tong_2026]: https://doi.org/10.1016/j.actaastro.2026.04.010
[research_trimpi_1962]: https://ntrs.nasa.gov/citations/19630003230
[research_trimpi_1962_2]: https://ntrs.nasa.gov/citations/20190002214
[research_trout_1963]: https://ntrs.nasa.gov/citations/19630003222
[research_vaglig_laurin_1960]: https://doi.org/10.2514/8.8369
[research_varma_2026]: https://doi.org/10.1063/5.0331864
[research_varma_zhong_2025]: https://doi.org/10.1017/jfm.2025.10230
[research_varma_zhong_2026]: https://doi.org/10.1017/jfm.2026.11430
[research_vasudevan_leonard_2002]: https://doi.org/10.21236/ada403745
[research_venkatapathy_hash_2026]: https://doi.org/10.1177/15311074261464024
[research_vershinin_2024]: https://doi.org/10.1134/s0018151x2570021x
[research_viegas_howe_1962]: https://ntrs.nasa.gov/citations/19620006838
[research_vigil_perez_2026]: https://doi.org/10.1016/j.euromechflu.2026.204537
[research_vinh_lin_1982]: https://ntrs.nasa.gov/citations/19820019475
[research_walker_wolowicz_1960]: https://ntrs.nasa.gov/citations/19650014459
[research_walton_simmons_1962]: https://doi.org/10.21236/ad0286392
[research_wang_2019]: https://ntrs.nasa.gov/citations/20190025824
[research_wang_2024]: https://doi.org/10.1016/j.tsep.2023.102256
[research_wang_2025]: https://doi.org/10.2514/1.a36141
[research_wang_2025_2]: https://doi.org/10.5194/acp-25-5021-2025
[research_wang_2025_3]: https://doi.org/10.3390/ma18174142
[research_wang_2025_4]: https://doi.org/10.1016/j.compstruct.2025.119192
[research_wang_2025_5]: https://doi.org/10.1016/j.applthermaleng.2025.126704
[research_wang_2026]: https://doi.org/10.1016/j.actaastro.2026.08.011
[research_wang_han_2025]: https://doi.org/10.1007/s10443-025-10331-7
[research_wang_jiang_2020]: https://doi.org/10.3390/s20216179
[research_wang_luo_2022]: https://doi.org/10.3390/app122110734
[research_warmbrod_1963]: https://ntrs.nasa.gov/citations/19630005471
[research_wegener_lobb_1952]: https://doi.org/10.21236/ad0012779
[research_weifeng_2026]: https://doi.org/10.7498/aps.75.20260460
[research_welton_1965]: https://ntrs.nasa.gov/citations/19650024803
[research_weng_martin_2014]: https://doi.org/10.2514/6.2014-2121
[research_weng_martin_2015]: https://doi.org/10.2514/1.t4576
[research_wheeler_1986]: https://ntrs.nasa.gov/citations/19860000134
[research_wheelon_1959]: https://doi.org/10.2514/8.4944
[research_whitmore_moes_1994]: https://ntrs.nasa.gov/citations/19940032870
[research_wilder_prabhu_2019]: https://ntrs.nasa.gov/citations/20190028253
[research_willier_2026]: https://doi.org/10.2514/1.a36511
[research_wilmer_2022]: https://doi.org/10.1016/j.jsse.2022.02.007
[research_winter_2011]: https://ntrs.nasa.gov/citations/20120011648
[research_winter_2019]: https://ntrs.nasa.gov/citations/20190002714
[research_winters_1964]: https://ntrs.nasa.gov/citations/19640017591
[research_winters_bracalente_1961]: https://ntrs.nasa.gov/citations/20040008121
[research_xie_2021]: https://doi.org/10.1109/access.2021.3092515
[research_xu_2026]: https://doi.org/10.1016/j.corsci.2025.113382
[research_xue_2026]: https://doi.org/10.1016/j.applthermaleng.2026.130619
[research_yang_1985]: https://doi.org/10.2514/6.1985-1679
[research_yang_2022]: https://doi.org/10.1016/j.csite.2022.102085
[research_yang_2026]: https://doi.org/10.1360/sspma-2026-0100
[research_yee_1961]: https://ntrs.nasa.gov/citations/20040047120
[research_yue_2025]: https://doi.org/10.1016/j.applthermaleng.2025.127175
[research_yun_mason_1962]: https://ntrs.nasa.gov/citations/19620005758
[research_yungster_radhakrishnan_2001]: https://doi.org/10.1007/pl00004073
[research_zarubina_2025]: https://doi.org/10.7868/s3034498025110041
[research_zeng_2026]: https://doi.org/10.1063/5.0340634
[research_zhang_2010]: https://doi.org/10.1109/wcica.2010.5554588
[research_zhang_2025_2]: https://doi.org/10.1063/5.0251388
[research_zhang_2026]: https://doi.org/10.2514/1.j066725
[research_zhang_2026_2]: https://doi.org/10.1016/j.ast.2026.111885
[research_zhang_2026_3]: https://doi.org/10.1063/5.0333893
[research_zhang_2026_5]: https://doi.org/10.1007/s42401-026-00511-z
[research_zhao_2020]: https://doi.org/10.1016/j.ast.2019.105553
[research_zhao_2025]: https://doi.org/10.3390/app152312482
[research_zhao_2026]: https://doi.org/10.1016/j.csite.2026.108238
[research_zhao_zhou_2013]: https://doi.org/10.1016/j.cja.2013.10.009
[research_zhou_2012]: https://doi.org/10.2514/6.2012-4709
[research_zhou_2025]: https://doi.org/10.15541/jim20240317
[research_zhou_2026]: https://doi.org/10.1016/j.asr.2025.12.026
[research_zhu_2025]: https://doi.org/10.1016/j.ast.2025.110070
[research_zjavka_2026]: https://doi.org/10.3390/modelling7030082
[research_zoby_1988]: https://ntrs.nasa.gov/citations/19880056529
[research_zou_2025]: https://doi.org/10.1017/jfm.2025.10846
[research_zubiaurre_2024]: https://doi.org/10.1007/s11085-024-10254-x
