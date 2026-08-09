---
layout: post
mathjax: true
comments: true
title: "X-Planes: Boeing X-20 Dyna-Soar"
date: 2025-10-26 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 21
---

<!-- A317 -->
<script>console.log("A317");</script>

The [Boeing X-20 Dyna-Soar][ref_x20] was to come back from orbit by flying rather than falling, and the difference is not a matter of style. A capsule sheds its orbital energy in about a minute, lands wherever the arithmetic puts it, and is used once. A glider sheds the same energy over half an hour, can choose its landing site from seventeen hundred nautical miles either side of its ground track, and lands on a runway. **The X-20 was cancelled in December 1963 without flying, so everything in this article is a prediction the vehicle never got to test.** This article is the twenty-first in the [X-Planes series][related_post_a297_xplanes_framing], following the [X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], the [X-4][related_post_a301_northrop_x4], the [X-5][related_post_a302_bell_x5], the [X-6][related_post_a303_convair_x6], the [X-7][related_post_a304_lockheed_x7], the [X-8][related_post_a305_aerojet_x8], the [X-9][related_post_a306_bell_x9], the [X-10][related_post_a307_north_american_x10], the [X-11][related_post_a308_convair_x11], the [X-12][related_post_a309_convair_x12], the [X-13][related_post_a310_ryan_x13], the [X-14][related_post_a311_bell_x14], the [X-15][related_post_a312_north_american_x15], the [X-16][related_post_a313_bell_x16], the [X-17][related_post_a314_lockheed_x17], the [X-18][related_post_a315_hiller_x18], and the [X-19][related_post_a316_curtiss_wright_x19].

The series has met high-speed heating twice already. The [X-15][related_post_a312_north_american_x15] asked how an aircraft survives a brief hypersonic dash, and the [X-17][related_post_a314_lockheed_x17] asked how a blunt body survives a ballistic reentry that is over in a minute. **The X-20 asks the opposite question and gets the opposite answer**, because a lifting reentry inverts which part of the heating problem is hard.

The standard inventory entry remains [Jenkins Landis and Miller 2003 American X-Vehicles, An Inventory X-1 to X-50][book_jenkins_landis_miller_2003] and the vehicle compilation is [Miller 2001 The X-Planes, X-1 to X-45][book_miller_2001]. The programme has an official history in [Geiger 1963][research_geiger_1963], which is unusual for a cancelled aircraft, and the flight mechanics are the subject of [Vinh Busemann and Culp 1980 Hypersonic and Planetary Entry Flight Mechanics][book_vinh_1980].

## The Research Question

### The Keystone Is What Lift Costs and What It Buys

**The keystone is the exchange rate between crossrange and heat.**

A vehicle returning from orbit has to get rid of about ten million foot-pounds of kinetic energy for every pound of itself. Where that energy goes is not in question, since it goes into the air and comes back as heat. What is in question is **how fast**, and lift is the control the designer has over the answer.

Add lift and the vehicle flies a shallower path, decelerates more gently, travels further, and can steer. Add lift and the heating lasts longer. The article's whole business is working out what that trade actually costs, because the answer is not the one the trade appears to offer.

### Why This Was the Binding Unknown in 1957

By 1957 the ballistic answer was understood. Allen and Eggers had shown that a blunt body survives reentry by putting its energy into the air rather than into itself, and the [X-17][related_post_a314_lockheed_x17] had flown to measure it.

**A ballistic capsule cannot choose where it lands.** For a reconnaissance or bombing vehicle, which is what the Air Force wanted, that is disqualifying. Crossrange is the ability to land somewhere other than directly under the orbit, and it is what makes a once-a-day overflight into an aircraft that can come home on the pass it chooses.

The unknown was not whether lift produces crossrange. It obviously does. **The unknown was whether the thermal price of the lift could be paid by a structure that a pilot could sit inside**, and the design literature of the moment was working on exactly that, in [Kelly 1958][research_kelly_1958], [Doggett 1959][research_doggett_1959], [Paulson and Shanks 1959][research_paulson_shanks_1959], [NY 1959][research_ny_1959], [Rotelli 1960][research_rotelli_1960], [Czarnecki and Davison 1960][research_czarnecki_davison_1960], [Campbell and Shepler 1960][research_campbell_shepler_1960], [Helper et al 1960][research_helper_1960], [Lee and Mason 1960][research_lee_mason_1960], [Paulson and Shanks 1961][research_paulson_shanks_1961], [Seiff and Wilkins 1961][research_seiff_wilkins_1961], [Walker 1962][research_walker_1962].

## Programme Origin

The lineage runs back to the Sänger and Bredt antipodal bomber study, whose report circulated widely after 1945 and whose skip-glide trajectory is the ancestor of every boost-glide proposal that followed. It reappeared in the United States as a family of separate programmes. BOMI for bomber missile, Brass Bell for reconnaissance, ROBO for rocket bomber, and HYWARDS for a hypersonic research vehicle.

On 10 October 1957 the Air Research and Development Command consolidated HYWARDS, Brass Bell and ROBO into a single three-step programme, System 464L, under the name Dyna-Soar, a contraction of dynamic soaring. **That was six days after Sputnik.**

The programme ran from 24 October 1957 to 10 December 1963 and spent about 660 million dollars. Boeing won the airframe. Titan I and Titan II were both too small and the [Titan III][ref_titan3] was selected in late 1961. Seven pilots were assigned, among them [Neil Armstrong][ref_armstrong].

[Robert McNamara][ref_mcnamara] cancelled it on 10 December 1963, shortly after construction of the first airframe had begun, on the ground that it had no settled mission. The same announcement funded the [Manned Orbiting Laboratory][ref_mol], which was itself cancelled in 1969 without flying a crew.

## Sizing From First Principles

### The Vehicle

The glider is small and its proportions are unlike anything else in this series. A delta of 345 square feet with a span of 20.8 feet on a length of 35.34 feet, weighing 11,386 pounds at most.

$$\text{AR} = \frac{b^{2}}{S} = \frac{20.8^{2}}{345} = 1.254$$

That aspect ratio is a quarter of an airliner's, which is what hypersonic flight demands and what subsonic flight then has to live with.

$$\frac{W}{S} = \frac{11{,}386}{345} = 33.0 \ \text{lb/ft}^{2}$$

**Thirty-three pounds per square foot, against the eighty-eight of the previous article's aircraft.** The [X-19][related_post_a316_curtiss_wright_x19] wanted the highest wing loading it could carry and this vehicle wants the lowest, and the reason is thermal rather than aerodynamic.

### The Energy

Circular orbital speed at the surface is the reference the whole problem is scaled against.

$$V_c = \sqrt{g R_e} = \sqrt{(32.174)(20{,}902{,}231)} = 25{,}933 \ \text{ft/s}$$

The quoted maximum of 17,500 miles per hour is 25,667 feet per second, which is 99.0 percent of circular speed, so this is an orbital vehicle in everything but name. Its specific kinetic energy is

$$\frac{V_c^{2}}{2g} = 1.045 \times 10^{7} \ \text{ft lb per lb}$$

Multiplying by the weight and converting mechanical to thermal units at 778.169 foot-pounds per British thermal unit,

$$Q_{\text{total}} = \frac{W}{778.169} \frac{V_c^{2}}{2g} = \frac{11{,}386 \times 1.045 \times 10^{7}}{778.169} = 1.529 \times 10^{8} \ \text{BTU}$$

**That is the number the thermal protection system exists to dispose of.** For scale, it is roughly the energy released by burning 1,133 gallons of kerosene, and it has to leave the vehicle through its skin.

### The Equilibrium Glide

A vehicle at orbital speed is nearly weightless, because the speed itself supplies most of the centripetal acceleration gravity is asking for. What lift has to carry is only the remainder.

$$L = W \left( 1 - \frac{V^{2}}{V_c^{2}} \right)$$

That bracket is the centrifugal relief and it is the reason a reentry glider flies in air a thousand times thinner than an aeroplane needs. Writing the lift out gives the density the vehicle must find at each speed.

$$\tfrac{1}{2} \rho V^{2} S C_L = W \left( 1 - \frac{V^{2}}{V_c^{2}} \right)$$

Rearranging for the density the vehicle must find,

$$\rho = \frac{2 W \left( 1 - V^{2}/V_c^{2} \right)}{V^{2} S C_L}$$

**Note what is in that expression and what is not.** Wing loading is in it. Lift-to-drag ratio is not. The altitude a glider flies at any given speed is set entirely by how heavily its wing is loaded.

Deceleration follows from the drag that the lift implies.

$$\frac{dV}{dt} = -\frac{D}{m} = -\frac{g \left( 1 - V^{2}/V_c^{2} \right)}{L/D}$$

That deceleration is largest when the centrifugal relief has gone, which is at the slow end rather than the fast one.

$$\left. \frac{dV}{dt} \right|_{\max} = \frac{g}{L/D} = \frac{32.174}{1.245} = 25.8 \ \text{ft/s}^{2} = 0.803 \, g$$

**Eight tenths of gravity, and never more**, which is gentle enough for a pilot to work through and is the second thing lift buys. A ballistic entry at the same speed reaches eight or ten times that.

Converting the density to an altitude needs the atmosphere, and above about 100,000 feet an exponential fit with a scale height $H$ near 23,800 feet is adequate.

$$\rho = \rho_0 e^{-z/H} \quad \Longrightarrow \quad z = H \ln \frac{\rho_0}{\rho}$$

which puts the vehicle near 240,000 feet where the heating peaks.

### Range and Crossrange

Downrange follows by dividing the range rate by the deceleration, which eliminates time,

$$dR = V \, dt = \frac{V \, dV}{dV/dt} = -\frac{(L/D) \, V \, dV}{g \left( 1 - V^{2}/V_c^{2} \right)}$$

and integrating gives the classical closed form.

$$R = \frac{L}{D} \frac{V_c^{2}}{2g} \ln \left[ \frac{1}{1 - (V/V_c)^{2}} \right]$$

Crossrange is the quantity the programme actually wanted, and the classical approximation for the maximum lateral distance reachable by banking is quadratic in lift-to-drag ratio.

$$\text{CR}_{\max} \approx 0.319 \, R_e \left( \frac{L}{D} \right)^{2}$$

The programme quoted 1,700 nautical miles of crossrange, which is a checkable claim rather than a slogan. Inverting the relation gives the lift-to-drag ratio it requires.

$$\frac{L}{D} = \sqrt{\frac{\text{CR}}{0.319 R_e}} = 1.245$$

**That number can be checked against the configuration rather than merely asserted about it.** At hypersonic speeds a flat surface obeys Newtonian impact theory closely, in which the pressure comes entirely from the normal momentum the surface removes from the flow.

$$C_N = 2 \sin^{2}\alpha$$

Resolving that normal force into lift and drag along the flight path,

$$C_L = 2 \sin^{2}\alpha \cos\alpha, \qquad C_D = 2 \sin^{3}\alpha$$

The article assumes a trimmed lift coefficient of 0.6, and inverting the first of those for the angle of attack it implies gives

$$\alpha = 38.14^{\circ}$$

At that angle the drag coefficient is 0.4712, and the lift-to-drag ratio is a remarkably simple thing, because the two coefficients differ by exactly one factor of the tangent.

$$\frac{L}{D} = \frac{\cos\alpha}{\sin\alpha} = \cot\alpha = 1.273$$

**Against the 1.245 that 1,700 nautical miles of crossrange requires, that is agreement to 2.3 percent**, reached from two directions that share nothing. One is a mission requirement inverted through an orbital mechanics approximation. The other is impact theory applied to a flat plate. The wind-tunnel record for such shapes is extensive, in [Bernot and Robinson 1958][research_bernot_robinson_1958], [Robinson and Bernot 1958][research_robinson_bernot_1958], [Kaufman and G. 1963][research_kaufman_g_1963], [Meckler 1965][research_meckler_1965], [Giles and Thomas 1966][research_giles_thomas_1966], [Graves and Carmel 1968][research_graves_carmel_1968], [Merz 1968][research_merz_1968], [Pfaff 1968][research_pfaff_1968], [Goldberg et al 1969][research_goldberg_1969].

### The Trade, Which Is Not the Trade It Appears to Be

Now substitute the glide density into the stagnation-point heating relation, in the Sutton-Graves form this series used for the [X-17][related_post_a314_lockheed_x17], where $R_n$ is the nose radius.

$$\dot{q} = K \sqrt{\frac{\rho}{R_n}} V^{3}$$

Putting the glide density into it and collecting the constants,

$$\dot{q} \propto \sqrt{\frac{W}{S C_L}} \, V^{2} \sqrt{1 - \frac{V^{2}}{V_c^{2}}}$$

**Lift-to-drag ratio has vanished.** The peak heating rate on an equilibrium glide does not depend on it at all.

Where that peak falls is worth locating, because the answer is a pure number. Write $u = (V/V_c)^{2}$ and the heating becomes proportional to a function of $u$ alone.

$$\dot{q} \propto u \sqrt{1 - u} \cdot V_c^{2} \quad \text{so} \quad \dot{q}^{2} \propto u^{2} (1 - u)$$

Maximising the square, which has the same maximum,

$$\frac{d}{du} \left[ u^{2} (1 - u) \right] = 2u - 3u^{2} = 0 \quad \Longrightarrow \quad u = \frac{2}{3}$$

Taking the square root to recover the speed itself,

$$V_{\text{peak}} = V_c \sqrt{\tfrac{2}{3}} = 21{,}174 \ \text{ft/s}$$

**The worst heating always arrives at 81.6 percent of circular speed**, whatever the vehicle, whatever its wing loading, and whatever its lift-to-drag ratio. Only the magnitude changes.

What lift-to-drag ratio changes is the time spent near that rate, through the deceleration, and therefore the integrated load.

$$Q = \int \dot{q} \, dt = \int \frac{\dot{q}}{|dV/dt|} \, dV \propto \frac{L}{D}$$

So the three quantities scale in three different ways, and setting them beside each other is the whole argument of this article.

| Lift-to-drag ratio | Peak rate, BTU per square foot second | Total load, BTU per square foot | Crossrange, nm |
|---|---|---|---|
| 0.25 | 47.78 | 14,702 | 69 |
| 0.50 | 47.78 | 29,403 | 274 |
| 1.00 | 47.78 | 58,807 | 1,097 |
| 1.25 | 47.78 | 73,509 | 1,715 |
| 1.50 | 47.78 | 88,210 | 2,469 |
| 2.00 | 47.78 | 117,614 | 4,390 |
| 3.00 | 47.78 | 176,421 | 9,876 |

The three columns obey three different powers of the same variable, which is the whole content of the table.

$$\frac{\dot{q}_2}{\dot{q}_1} = \left( \frac{L/D_2}{L/D_1} \right)^{0} = 1, \qquad \frac{Q_2}{Q_1} = \frac{L/D_2}{L/D_1}, \qquad \frac{\text{CR}_2}{\text{CR}_1} = \left( \frac{L/D_2}{L/D_1} \right)^{2}$$

**Across the twelvefold change from 0.25 to 3.00 the peak rate does not move in the fourth decimal place, the total load rises by a factor of twelve, and the crossrange rises by a factor of one hundred and forty-four.**

That is a remarkably clean decomposition. **Peak temperature, which selects the material, is set by wing loading alone. Mission reach, which selects the programme, is set by lift-to-drag ratio alone.** The two design decisions do not interfere, which is not something a designer is often given.

### Against the Ballistic Case

The comparison that matters is with the vehicle the X-20 was an alternative to. A ballistic entry needs its own integration, along the Allen-Eggers solution rather than the glide, since a body with no lift does not fly an equilibrium anything.

$$V(z) = V_e \exp \left[ -\frac{\rho_0 H}{2 \beta \sin\gamma} e^{-z/H} \right]$$

The ballistic coefficient in that expression is the vehicle's resistance to being slowed, and it plays the part wing loading plays on the glide.

$$\beta = \frac{W}{C_D A}$$

At 50 pounds per square foot and a five degree path angle, the peak stagnation heating is 1,247 British thermal units per square foot second at about 87,000 feet, against 47.8 for the glider.

$$\frac{\dot{q}_{\text{ballistic}}}{\dot{q}_{\text{glide}}} = \frac{1{,}247}{47.8} = 26.1$$

**The total loads, however, are nearly the same.**

$$\frac{Q_{\text{ballistic}}}{Q_{\text{glide}}} = \frac{69{,}898}{73{,}509} = 0.951$$

That is not the result the framing predicted. The glider does not pay a large penalty in total heat. **What it buys is a twenty-six-fold reduction in peak rate**, and that reduction is the entire reason a radiatively cooled structure is possible.

### Radiation Equilibrium

A surface that cannot conduct heat away and cannot store it must radiate it, and it reaches whatever temperature makes the two balance.

$$\dot{q} = \varepsilon \sigma T^{4}$$

Inverting for the temperature that balance implies,

$$T = \left( \frac{\dot{q}}{\varepsilon \sigma} \right)^{1/4}$$

At the peak rate of 47.8 British thermal units per square foot second and an emissivity of 0.85, the stagnation region settles at

$$T = 2{,}837 \ ^\circ\text{F} = 1{,}831 \ \text{K}$$

The flat lower surface sees far less, because it is neither stagnating the flow nor sitting behind the strongest part of the shock. Taking it at a twelfth of the stagnation value,

$$T_{\text{surface}} = \left( \frac{0.12 \, \dot{q}_{\text{peak}}}{\varepsilon \sigma} \right)^{1/4} = 1{,}480 \ ^\circ\text{F}$$

**The fourth root is what makes the structure possible.** An eightfold reduction in heating buys only a 1,357 degree reduction in temperature, but it is the reduction that puts the primary structure inside a superalloy's range.

**Those two numbers select the two materials.** [René 41][ref_rene41] is a nickel superalloy usable to about 1,800 degrees Fahrenheit, which covers the primary structure. The nose and leading edges need [coated molybdenum][ref_molybdenum], graphite and [zirconia][ref_zirconia], good to around 3,000 degrees. The hot-structure experiments of the period are in [Pride et al 1960][research_pride_1960], [Baird 1964][research_baird_1964], [Brunner 1966][research_brunner_1966], [Brunner et al 1966, Study of thermal protection requir][research_brunner_1966_2], [Avery 1981][research_avery_1981], [Ko and Fields 1987][research_ko_fields_1987], [Blosser 1988][research_blosser_1988], [Goldstein 1992][research_goldstein_1992], [Carroll et al 1995][research_carroll_1995], [Blosser 1996][research_blosser_1996] and the materials work in [Maxwell 1952][research_maxwell_1952], [Mathauser et al 1960][research_mathauser_1960], [Peters and Rasnick 1961][research_peters_rasnick_1961], [Pride et al 1962][research_pride_1962], [Gangler 1963][research_gangler_1963], [Bliton and Rausch 1963][research_bliton_rausch_1963], [Bowers 1963][research_bowers_1963], [Bowers and Esch 1963][research_bowers_esch_1963], [Leeds 1963][research_leeds_1963], [HUGILL and GAIENNIE 1963][research_hugill_gaiennie_1963].

### Why the Wing Loading Is Low

Peak heating goes as the square root of wing loading, which turns the loading into a thermal design variable rather than an aerodynamic one.

$$\dot{q}_{\text{peak}} \propto \sqrt{\frac{W}{S}}$$

| Wing loading, lb per square foot | Peak rate | Radiation equilibrium |
|---|---|---|
| 20.0 | 37.2 | 2,637 F |
| 33.0 | 47.8 | 2,837 F |
| 50.0 | 58.8 | 3,012 F |
| 88.4 | 78.2 | 3,269 F |
| 120.0 | 91.1 | 3,414 F |

Temperature depends on wing loading far more weakly than heating does, because the fourth root of a square root is an eighth root.

$$T \propto \dot{q}^{1/4} \propto \left( \frac{W}{S} \right)^{1/8}$$

**That is why the table above is so flat**, and it is also why the effect still matters. **At the X-19's eighty-eight pounds per square foot the nose would sit at 3,269 degrees**, above coated molybdenum and far beyond any superalloy. The X-20's wing is large for its weight because a smaller one would have melted, and the previous article's wing was small for its weight because a larger one would have been slow. **The same quantity, driven in opposite directions, for reasons that have nothing to do with each other.**

## Dependent Systems

### The Structure, Which Is the Aircraft

A radiatively cooled vehicle has no cool interior to hide its structure in, so the structure runs hot and must be designed to do so. The X-20's answer was a René 41 truss frame carrying insulated panels, with molybdenum shingles over the hot lower surface, and the development of that arrangement is recorded in [Helper et al 1960][research_helper_1960], [Czarnecki and Davison 1960][research_czarnecki_davison_1960] and [Baird 1964][research_baird_1964].

Thermal expansion rather than pressure sets the joint design, and the magnitude is easy to state.

$$\Delta L = \alpha L \, \Delta T$$

René 41 expands at about 8.0 times ten to the minus six per degree Fahrenheit. Over the vehicle's 35.34 foot length at a 1,500 degree rise,

$$\Delta L = (8.0 \times 10^{-6})(35.34)(1500) = 0.424 \ \text{ft} = 5.09 \ \text{in}$$

**The airframe grows five inches on the way home.** Worse, the molybdenum shingles over it expand at roughly 3.0 times ten to the minus six, so the two move differently.

$$\Delta L_{\text{mismatch}} = (\alpha_{\text{R41}} - \alpha_{\text{Mo}}) L \, \Delta T = 0.270 \ \text{in per 3 ft panel}$$

**The problem is not strength but accommodation.** Every shingle must be free to slide against its frame while remaining gas-tight, which is why the fastener and thermal-stress work in the same literature is as large as it is.

### Why Not Ablation, Which Is Where This Article Changed Its Mind

The obvious objection to a hot structure is that ablation was available, understood, and about to be used on Mercury and Apollo. This article expected to answer that a thirty-minute heat load makes ablation impossibly heavy. **It does not, and the earlier reading is withdrawn.**

Ablator mass is the total heat divided by the effective heat of ablation.

$$m_{\text{ablator}} = \frac{Q_{\text{vehicle}}}{H_{\text{eff}}}$$

Taking the vehicle heat load as 8.33 times ten to the sixth British thermal units, the mass fraction is what decides the question.

$$\frac{m_{\text{ablator}}}{W} = \frac{Q_{\text{vehicle}}}{H_{\text{eff}} W}$$

Evaluating it at the generous and the pessimistic ends of the plausible range,

$$\frac{8.33 \times 10^{6}}{(15{,}000)(11{,}386)} = 4.9\%, \qquad \frac{8.33 \times 10^{6}}{(3{,}000)(11{,}386)} = 24.4\%$$

between 556 and 2,778 pounds across every plausible effective heat of ablation. **Heavy, and entirely buildable.** The [Apollo command module][ref_apollo_cm] carried a comparable fraction.

A heat sink is a different matter.

$$m_{\text{sink}} = \frac{Q_{\text{vehicle}}}{c_p \Delta T} = 37{,}878 \ \text{lb}$$

which is 333 percent of the glider, and therefore impossible.

**So the hot structure was not forced by mass. It was chosen for reuse**, which is the one thing an ablator cannot offer and the entire reason for preferring a spaceplane to a capsule. That is a claim about programme intent rather than about physics, and the article should not pretend the arithmetic compelled it.

### Guidance and Energy Management

A glider with no engine arrives with a fixed quantity of energy and must spend all of it reaching the runway. The quantity that matters is energy height, which combines the two forms the vehicle can trade between.

$$h_e = h + \frac{V^{2}}{2g}$$

At entry, near 240,000 feet and 21,174 feet per second, that is

$$h_e = 240{,}000 + \frac{21{,}174^{2}}{2(32.174)} = 7.20 \times 10^{6} \ \text{ft}$$

or about 1,365 statute miles of energy height, all of which must be disposed of before touchdown. **Too much on arrival and the vehicle overshoots with no way to slow down, too little and it lands short.** The pilot's task and the automation that supports it are the subject of [Lee and Mason 1960][research_lee_mason_1960] and [Young and Goode 1962][research_young_goode_1962], and the modern descendants of that problem are in [Fine 1967][research_fine_1967], [KRYVORUKA and ASHURST 1973][research_kryvoruka_ashurst_1973], [Lu 1996, Entry guidance and trajectory cont][research_lu_1996_2], [Lu 1997][research_lu_1997], [Hanson et al 1998][research_hanson_1998], [Fuhry 1999][research_fuhry_1999], [Calhoun 2000][research_calhoun_2000], [Burchett 2003][research_burchett_2003].

Attitude control at the top of the glide is reaction jets, because there is no air to work against. Control blends to aerodynamic surfaces as the vehicle descends, and [Fine 1967][research_fine_1967] treats the case where attitude is used specifically to hold skin temperature down.

### Landing on Skids

The X-20 lands without power at the end of everything.

$$V_{\text{stall}} = \sqrt{\frac{2W}{\rho S C_{L,\max}}} = 99 \ \text{kt}$$

with touchdown near 114 knots. At a subsonic lift-to-drag ratio of about four for a delta of this aspect ratio, the approach is steep.

$$\gamma = \arctan \frac{1}{L/D} = 14.0^\circ, \qquad w = \frac{V}{L/D} = 48.3 \ \text{ft/s}$$

**A sink rate of 48 feet per second is not a landing, it is an arrival**, and the vehicle must flare out of it. That is the same unpowered steep approach the [X-15][related_post_a312_north_american_x15] flew and the [Space Shuttle][ref_shuttle] inherited.

The energy the gear must absorb follows from the touchdown speed.

$$E = \tfrac{1}{2} \frac{W}{g} V_{\text{touch}}^{2} = 7{,}734 \ \text{BTU}$$

The gear is not wheels. Goodyear developed retractable wire-brush skids of René 41, because a pneumatic tyre cannot survive being soaked at structural temperature during the descent and then asked to work. **The landing gear is a consequence of the thermal design**, which is how thoroughly the keystone propagates.

## The Flight Test Record

There is none. **The X-20 never flew and no airframe was completed.** Cancellation came on 10 December 1963, after roughly 660 million dollars over 6.13 years.

$$\frac{660 \times 10^{6}}{6.13} = 108 \ \text{million dollars per year}, \qquad \frac{660 \times 10^{6}}{11{,}386} = \$57{,}966 \ \text{per pound}$$

**Fifty-eight thousand dollars for every pound of a glider that did not exist**, in 1963 dollars.

What did fly was the instrumentation. [ASSET][ref_asset] flew sub-scale radiatively cooled structures on Thor boosters between 1963 and 1965 and returned data on exactly the panels the X-20 would have used. The programme's own engineering record survives in unusual depth for a cancelled aircraft, including [Geiger 1963][research_geiger_1963], [Rotelli 1960][research_rotelli_1960] and [Hargis 1964][research_hargis_1964].

## Comparison With Ground Prediction

The comparison cannot be made, and that is the finding rather than an omission.

**Every number in this article is a prediction against which no X-20 measurement exists**, because the vehicle never left the ground. The wind tunnel record for the configuration is extensive, in [Lovelace 1961][research_lovelace_1961], [Meckler 1964][research_meckler_1964], [Kaufman and G. 1964][research_kaufman_g_1964], [Murphy and Rubesin 1965][research_murphy_rubesin_1965], [Rochelle et al 1972][research_rochelle_1972], [Stainback et al 1972][research_stainback_1972], [Meng 1973][research_meng_1973], [Rosner and Cibrian 1974][research_rosner_cibrian_1974], [Sherman 1978][research_sherman_1978], [Baker and Kramer 1982][research_baker_kramer_1982], and none of it is flight data for this airframe.

What partially substitutes is ASSET, which flew the structure without the vehicle, and later the [Space Shuttle][ref_shuttle], which flew the trajectory with a different structure. **Between them they tested both halves of the X-20's answer separately and neither tested it together.**

## What the Data Changed

A programme that produced no data still changed things, which is a distinction worth keeping.

**The lifting-reentry trajectory became standard.** The Shuttle flew an equilibrium glide with bank modulation for crossrange, which is the X-20's profile with a different vehicle wrapped around it, and the guidance literature runs continuously from one to the other.

**The hot structure did not.** The Shuttle chose ceramic tiles over a cool aluminium airframe, which is the opposite architecture, and the reasons were manufacturing and inspection rather than thermodynamics. Metallic thermal protection returned as a research subject decades later, in [Naftel and Powell 1993][research_naftel_powell_1993], [NACA 1995][research_naca_1995], [Rasky 1996][research_rasky_1996], [Freeman et al 1996][research_freeman_1996], [Freeman et al 1997][research_freeman_1997], [Johnson et al 1998][research_johnson_1998], [Manley et al 2000][research_manley_2000], [Olds and Cowart 2001][research_olds_cowart_2001].

**The crossrange requirement outlived the vehicle.** The Air Force's insistence on cross-range drove the Shuttle's delta wing, which is why an orbiter that mostly flew from and to Florida carried a planform sized for a once-around polar abort it never performed.

## The Contemporary Literature

A short treatment here, to be expanded in the publication review. **The X-20's trajectory is the one thing about it that unambiguously survived.**

### The Glide Became the Standard Return

Equilibrium glide with bank modulation for crossrange is how a winged vehicle comes back from orbit, and the guidance problem the X-20 posed is still worked, in [Fine 1967][research_fine_1967], [KRYVORUKA and ASHURST 1973][research_kryvoruka_ashurst_1973], [Lu 1996, Entry guidance and trajectory cont][research_lu_1996_2], [Lu 1997][research_lu_1997], [Hanson et al 1998][research_hanson_1998], [Fuhry 1999][research_fuhry_1999], [Calhoun 2000][research_calhoun_2000], [Burchett 2003][research_burchett_2003].

### The Structure Did Not

The Shuttle chose ceramic tiles over a cool airframe rather than a hot structure, which is the opposite architecture. Metallic thermal protection returned later as a research subject rather than as a continuation, in [Naftel and Powell 1993][research_naftel_powell_1993], [NACA 1995][research_naca_1995], [Rasky 1996][research_rasky_1996], [Freeman et al 1996][research_freeman_1996], [Freeman et al 1997][research_freeman_1997], [Johnson et al 1998][research_johnson_1998], [Manley et al 2000][research_manley_2000], [Olds and Cowart 2001][research_olds_cowart_2001].

### The Descendant Flew Forty Years Late

The [X-37][ref_x37] performs the orbital mission the X-20 was specified for, unmanned and with modern materials, and its approach and landing testing is the X-20's final phase carried out at last.

## Where the Framing Breaks Down

**The keystone describes the vehicle and not the cancellation.** Nothing in the thermal analysis explains why the programme ended, which was a judgement that it had no mission. An article organised around a heat balance will make a political decision look like an engineering one, and it was not.

**The equilibrium glide is an idealisation.** A real entry oscillates in a phugoid about the equilibrium condition rather than tracking it, and the peak rate seen in a real trajectory can exceed the equilibrium value. The treatment here is the standard first approximation and the corrections are in [Foss and Whitcomb 1960][research_foss_whitcomb_1960], [Wong and Slye 1961][research_wong_slye_1961], [Young and Goode 1962][research_young_goode_1962], [Stern and Chu 1963][research_stern_chu_1963], [Bell 1965][research_bell_1965], [Krusos 1967][research_krusos_1967], [Delpino et al 1967][research_delpino_1967], [Dix et al 1967][research_dix_1967], [Fong et al 1970][research_fong_1970], [Chern and Vinh 1978][research_chern_vinh_1978], [Chern and Vinh 1980][research_chern_vinh_1980].

**The crossrange coefficient is taken, not derived.** The relation used is the classical quadratic approximation with a standard coefficient, and its accuracy at lift-to-drag ratios near unity is not established here.

**A cancelled aircraft invites counterfactual writing** and this article tries to avoid it. Whether the X-20 would have worked is not knowable, and the useful question is only whether its reasoning was sound.

## The Source Base

The X-20 has a better documentary record than most aircraft that flew, which is a consequence of six years of a well-funded programme that produced reports instead of flights.

The Dyna-Soar engineering reports are the backbone, covering configuration evolution, structure, leading edges, cockpit displays, pilot factors and aerothermoelasticity. The materials literature of 1960 to 1964 is dense because refractory coatings were the pacing item for every hypersonic programme at once.

**What is missing is any flight data**, and no amount of documentation substitutes for it.

## Epistemic State

**Historical fact.** The programme ran from 24 October 1957 to 10 December 1963, cost about 660 million dollars, and was cancelled by Robert McNamara without any airframe being completed or flown. It consolidated HYWARDS, Brass Bell and ROBO as System 464L. Titan III was selected in late 1961. Seven pilots were assigned, including Neil Armstrong.

**Published figures taken as given.** Wing area 345 square feet, span 20.8 feet, length 35.34 feet, glider weight 11,386 pounds, empty weight 10,395 pounds, wing loading 33 pounds per square foot, crossrange 1,700 nautical miles, maximum speed 17,500 miles per hour.

**A source conflict resolved rather than repeated.** A gross mass of 22,321 pounds appears widely, and it is inconsistent with a wing loading of 33 on 345 square feet. The glider weight of 11,386 pounds reproduces the quoted loading exactly, so the larger figure is the launch configuration including the transtage, and the two are not alternatives.

**Engineering analysis.** The aspect ratio, the centrifugal relief, the equilibrium glide density and deceleration, the range and crossrange relations, the implied lift-to-drag ratio of 1.245, the invariance of peak heating with respect to lift-to-drag ratio, the total heat scaling, the ballistic comparison, the radiation equilibrium temperatures, the ablator and heat sink masses, and the landing figures are all computed here from published geometry and are not quoted from any source.

**Assumed quantities, each of which moves the answers.** A nose radius of one foot, which is not in the public record and to whose square root the peak heating is inversely proportional. A trimmed hypersonic lift coefficient of 0.6. An emissivity of 0.85. A lower-surface heating fraction of 0.12 of stagnation. A wetted area of 2.2 times wing area with an area-average heating factor of 0.15. An effective heat of ablation between 3,000 and 15,000 British thermal units per pound. A subsonic lift-to-drag ratio of four. A ballistic coefficient of 50 pounds per square foot and a five degree entry angle for the comparison case.

**A conclusion this article reversed while computing it.** The file was written expecting to show that a thirty-minute heat load makes ablation impossible and therefore forces a radiative structure. **The arithmetic says otherwise.** An ablator is heavy but buildable at five to twenty-four percent of glider weight, and only the heat sink is impossible. The hot structure was therefore chosen for reuse rather than compelled by mass, and the earlier reading is withdrawn in the text rather than quietly replaced.

**Two tooling defects worth recording, both from the working directory rather than from the article.**

A selector script left in the working directory from the previous article shared its name with a Python standard library module, was imported in place of it, executed on import, and overwrote this article's reference selection with output computed for a tilt-propeller aircraft. It was caught because the replacement contained propeller buckets for a spaceplane. **Nothing in the checking apparatus would have found it.**

The corpus verifier then reported zero errors and **zero warnings**, where the established baseline is zero errors and twenty-one warnings. It had inherited a scratch working directory and found nothing to check. **It was caught only because the expected number was known**, which is the argument for recording baselines rather than reading checks as pass or fail.

**Written from present knowledge.** Material postdating the editorial date is used and identified as such.

## Out of Scope

The boost trajectory and Titan III performance in detail. Abort modes, which were a large part of the programme's difficulty. Real-gas and non-equilibrium chemistry in the shock layer, which matters at these speeds and is treated only through a correlation here. Radiative heating from the shock layer as distinct from convective heating. Boundary layer transition, which sets whether the lower surface sees laminar or turbulent heating and therefore moves the surface temperature substantially. The communications blackout. Life support and the pilot's thermal environment. The military missions the vehicle was to perform, and the political history of the cancellation.

## Conclusion

The X-20 asked what lift costs on the way back from orbit, and the answer this article computes is sharper than the question.

**Lift does not raise the peak heating at all.** Peak rate on an equilibrium glide is fixed by wing loading and is indifferent to lift-to-drag ratio across at least a twelvefold range. What lift buys is crossrange, growing as the square of lift-to-drag ratio, and what it costs is total heat, growing in direct proportion. Seventeen hundred nautical miles of crossrange needs a lift-to-drag ratio of 1.25, which a flat-bottomed delta of 1957 could actually deliver.

**The comparison with a capsule is not the one usually drawn.** A ballistic entry at the same conditions imposes a peak rate twenty-six times higher and a total load essentially the same. The glider's advantage is entirely in rate, and that is what permits a structure that radiates instead of one that burns away.

**The choice of a hot structure was not forced.** Ablation would have worked at five to twenty-four percent of glider weight. It was rejected because it cannot be used twice, which means the X-20's most distinctive engineering decision was a consequence of wanting an aeroplane rather than a consequence of the heat.

The vehicle never flew, so none of this was tested. **What was tested, eventually, was the trajectory, by a larger vehicle with a different structure**, and the crossrange requirement that shaped the X-20 shaped that one too.

## References

### Books

[book_jenkins_landis_miller_2003]: https://openlibrary.org/search?q=Jenkins+Landis+Miller+American+X+Vehicles
[book_miller_2001]: https://openlibrary.org/search?q=Miller+The+X+Planes+X-1+to+X-45
[book_vinh_1980]: https://openlibrary.org/search?q=Vinh+Hypersonic+and+Planetary+Entry+Flight+Mechanics

### Reference

[ref_apollo_cm]: https://en.wikipedia.org/wiki/Apollo_command_and_service_module
[ref_armstrong]: https://en.wikipedia.org/wiki/Neil_Armstrong
[ref_asset]: https://en.wikipedia.org/wiki/ASSET_(spacecraft)
[ref_mcnamara]: https://en.wikipedia.org/wiki/Robert_McNamara
[ref_mol]: https://en.wikipedia.org/wiki/Manned_Orbiting_Laboratory
[ref_molybdenum]: https://en.wikipedia.org/wiki/Molybdenum
[ref_rene41]: https://en.wikipedia.org/wiki/Ren%C3%A9_41
[ref_shuttle]: https://en.wikipedia.org/wiki/Space_Shuttle
[ref_titan3]: https://en.wikipedia.org/wiki/Titan_IIIC
[ref_x20]: https://en.wikipedia.org/wiki/Boeing_X-20_Dyna-Soar
[ref_x37]: https://en.wikipedia.org/wiki/Boeing_X-37
[ref_zirconia]: https://en.wikipedia.org/wiki/Zirconium_dioxide

### Research

[research_avery_1981]: https://ntrs.nasa.gov/citations/19810012587
[research_baird_1964]: https://doi.org/10.21236/ad0450460
[research_baker_kramer_1982]: https://doi.org/10.21236/ada114013
[research_bell_1965]: https://doi.org/10.21236/ad0631590
[research_bernot_robinson_1958]: https://ntrs.nasa.gov/citations/19710074595
[research_bliton_rausch_1963]: https://ntrs.nasa.gov/citations/19640017101
[research_blosser_1988]: https://ntrs.nasa.gov/citations/19880013054
[research_blosser_1996]: https://ntrs.nasa.gov/citations/19970005361
[research_bowers_1963]: https://doi.org/10.21236/ad0409321
[research_bowers_esch_1963]: https://doi.org/10.21236/ad0421694
[research_brunner_1966]: https://ntrs.nasa.gov/citations/19670008949
[research_brunner_1966_2]: https://ntrs.nasa.gov/citations/19670008947
[research_burchett_2003]: https://ntrs.nasa.gov/citations/20030093602
[research_calhoun_2000]: https://ntrs.nasa.gov/citations/20000032921
[research_campbell_shepler_1960]: https://ntrs.nasa.gov/citations/19720063150
[research_carroll_1995]: https://ntrs.nasa.gov/citations/20020034891
[research_chern_vinh_1978]: https://ntrs.nasa.gov/citations/19790013968
[research_chern_vinh_1980]: https://ntrs.nasa.gov/citations/19800007820
[research_czarnecki_davison_1960]: https://ntrs.nasa.gov/citations/19720063141
[research_delpino_1967]: https://ntrs.nasa.gov/citations/19690001538
[research_dix_1967]: https://doi.org/10.21236/ad0813708
[research_doggett_1959]: https://ntrs.nasa.gov/citations/19650073709
[research_fine_1967]: https://doi.org/10.21236/ad0654732
[research_fong_1970]: https://doi.org/10.21236/ad0866735
[research_foss_whitcomb_1960]: https://ntrs.nasa.gov/citations/19660024027
[research_freeman_1996]: https://ntrs.nasa.gov/citations/19960053992
[research_freeman_1997]: https://ntrs.nasa.gov/citations/19990009876
[research_fuhry_1999]: https://doi.org/10.2514/6.1999-4211
[research_gangler_1963]: https://ntrs.nasa.gov/citations/19630029196
[research_geiger_1963]: https://doi.org/10.21236/ada951933
[research_giles_thomas_1966]: https://ntrs.nasa.gov/citations/19660026817
[research_goldberg_1969]: https://ntrs.nasa.gov/citations/19700001407
[research_goldstein_1992]: https://ntrs.nasa.gov/citations/19930003260
[research_graves_carmel_1968]: https://ntrs.nasa.gov/citations/19680024364
[research_hanson_1998]: https://doi.org/10.2514/6.1998-4409
[research_hargis_1964]: https://ntrs.nasa.gov/citations/19720063747
[research_helper_1960]: https://ntrs.nasa.gov/citations/19720063142
[research_hugill_gaiennie_1963]: https://doi.org/10.21236/ad0295703
[research_johnson_1998]: https://ntrs.nasa.gov/citations/19980107885
[research_kaufman_g_1963]: https://doi.org/10.21236/ad0431280
[research_kaufman_g_1964]: https://doi.org/10.21236/ad0609559
[research_kelly_1958]: https://ntrs.nasa.gov/citations/19930090181
[research_ko_fields_1987]: https://ntrs.nasa.gov/citations/19880001007
[research_krusos_1967]: https://ntrs.nasa.gov/citations/19670025684
[research_kryvoruka_ashurst_1973]: https://doi.org/10.2514/6.1973-183
[research_lee_mason_1960]: https://ntrs.nasa.gov/citations/19720063138
[research_leeds_1963]: https://doi.org/10.21236/ad0400921
[research_lovelace_1961]: https://ntrs.nasa.gov/citations/19980227215
[research_lu_1996_2]: https://doi.org/10.2514/6.1996-3700
[research_lu_1997]: https://doi.org/10.2514/2.4008
[research_manley_2000]: https://ntrs.nasa.gov/citations/20000040788
[research_mathauser_1960]: https://ntrs.nasa.gov/citations/19980227836
[research_maxwell_1952]: https://ntrs.nasa.gov/citations/19930086994
[research_meckler_1964]: https://doi.org/10.21236/ad0608830
[research_meckler_1965]: https://doi.org/10.21236/ad0620959
[research_meng_1973]: https://ntrs.nasa.gov/citations/19740005592
[research_merz_1968]: https://doi.org/10.21236/ad0830135
[research_murphy_rubesin_1965]: https://ntrs.nasa.gov/citations/19660010795
[research_naca_1995]: https://ntrs.nasa.gov/citations/19960013899
[research_naftel_powell_1993]: https://ntrs.nasa.gov/citations/19930017827
[research_ny_1959]: https://doi.org/10.21236/ad0318479
[research_olds_cowart_2001]: https://ntrs.nasa.gov/citations/20010054791
[research_paulson_shanks_1959]: https://ntrs.nasa.gov/citations/19980237090
[research_paulson_shanks_1961]: https://ntrs.nasa.gov/citations/19980227410
[research_peters_rasnick_1961]: https://ntrs.nasa.gov/citations/20040006481
[research_pfaff_1968]: https://doi.org/10.21236/ad0832104
[research_pride_1960]: https://ntrs.nasa.gov/citations/19980223616
[research_pride_1962]: https://ntrs.nasa.gov/citations/19650014515
[research_rasky_1996]: https://ntrs.nasa.gov/citations/20020041186
[research_robinson_bernot_1958]: https://ntrs.nasa.gov/citations/19930090105
[research_rochelle_1972]: https://ntrs.nasa.gov/citations/19720013202
[research_rosner_cibrian_1974]: https://ntrs.nasa.gov/citations/19740053212
[research_rotelli_1960]: https://ntrs.nasa.gov/citations/19720063136
[research_seiff_wilkins_1961]: https://ntrs.nasa.gov/citations/19980227307
[research_sherman_1978]: https://doi.org/10.21236/ada056390
[research_stainback_1972]: https://ntrs.nasa.gov/citations/19790075398
[research_stern_chu_1963]: https://doi.org/10.21236/ad0405109
[research_walker_1962]: https://ntrs.nasa.gov/citations/19620004472
[research_wong_slye_1961]: https://ntrs.nasa.gov/citations/19980232890
[research_young_goode_1962]: https://ntrs.nasa.gov/citations/19620002806

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
[related_post_a314_lockheed_x17]: {% post_url 2025-10-23-x_planes_lockheed_x17 %}
[related_post_a315_hiller_x18]: {% post_url 2025-10-24-x_planes_hiller_x18 %}
[related_post_a316_curtiss_wright_x19]: {% post_url 2025-10-25-x_planes_curtiss_wright_x19 %}
