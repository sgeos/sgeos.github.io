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

**Against the 1.245 that 1,700 nautical miles of crossrange requires, that is agreement to 2.3 percent**, reached from two directions that share nothing.

That the check works at all rests on Newtonian theory being a good approximation in this regime, which is a question with its own literature, in [Dyke 1951][research_dyke_1951], [HAYES 1959][research_hayes_1959], [Freeman 1960][research_freeman_1960], [Freeman 1960, A Note on the Explosion Solution o][research_freeman_1960_2], [Freeman 1962][research_freeman_1962], [Lunev and Pavlov 1966][research_lunev_pavlov_1966], [DSOUZA 1970][research_dsouza_1970], [Barren and Mandl 1978][research_barren_mandl_1978], [Verhoff et al 1990][research_verhoff_1990]. The theory is exact only in the limit of infinite Mach number and zero shock standoff, and its accuracy on real bodies at finite Mach number is what those papers establish. One is a mission requirement inverted through an orbital mechanics approximation. The other is impact theory applied to a flat plate. The wind-tunnel record for such shapes is extensive, in [Bernot and Robinson 1958][research_bernot_robinson_1958], [Robinson and Bernot 1958][research_robinson_bernot_1958], [Kaufman and G. 1963][research_kaufman_g_1963], [Meckler 1965][research_meckler_1965], [Giles and Thomas 1966][research_giles_thomas_1966], [Graves and Carmel 1968][research_graves_carmel_1968], [Merz 1968][research_merz_1968], [Pfaff 1968][research_pfaff_1968], [Goldberg et al 1969][research_goldberg_1969].

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

The heating correlation underneath all of this is itself a fitted result rather than a derivation, and the measurement programme behind it ran for two decades, in [Luce and Jr 1949][research_luce_jr_1949], [Johnson and Rubesin 1949][research_johnson_rubesin_1949], [Emmons 1951][research_emmons_1951], [Bryson 1952][research_bryson_1952], [Emmons 1955][research_emmons_1955], [McLellan 1955][research_mclellan_1955], [SNODGRASS 1955][research_snodgrass_1955], [BUDIANSKY and MAYERS 1956][research_budiansky_mayers_1956], [Masters and Cohen 1957][research_masters_cohen_1957], [VANDREY 1957][research_vandrey_1957], [Maslen and Ostrach 1957][research_maslen_ostrach_1957], [MIELE 1957][research_miele_1957], [Warmbrod 1963][research_warmbrod_1963], [Reba 1964][research_reba_1964], [Vanmol and Anderson 1992][research_vanmol_anderson_1992].

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

The ballistic entry problem was worked thoroughly in exactly these years, in [Scherberg and Rubin 1953][research_scherberg_rubin_1953], [PHILLIPS and COHEN 1959][research_phillips_cohen_1959], [Foster 1960][research_foster_1960], [Schweppe 1964][research_schweppe_1964], [REINIKKA and SARTELL 1965][research_reinikka_sartell_1965], [Platus 1980][research_platus_1980], [Vinh and Lin 1982][research_vinh_lin_1982], [Hough 1982][research_hough_1982], [HOUGH 1982, Ballistic entry motion using a gen][research_hough_1982_2], [Zimmermann et al 1996][research_zimmermann_1996], [Tillier 1998][research_tillier_1998], and one of those addresses **drag modulation to reduce deceleration loads**, which is the ballistic vehicle's own attempt at the softening that lift provides for free.

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

**The emissivity in that expression is doing real work and is not well constrained.** Temperature goes as the inverse fourth root of it, so a surface at 0.6 rather than 0.85 runs about 250 degrees hotter, and the measurement of emissivity on refractory metals and oxides at these temperatures was an active subject rather than a settled one, in [Sully et al 1952][research_sully_1952], [Armstrong et al 1961][research_armstrong_1961], [Pai 1966][research_pai_1966], [Vertogradskii 1969][research_vertogradskii_1969], [Peletskii and Shur 1977][research_peletskii_shur_1977], [WANG et al 2011][research_wang_2011].

**Those two numbers select the two materials.** [René 41][ref_rene41] is a nickel superalloy usable to about 1,800 degrees Fahrenheit, which covers the primary structure. The nose and leading edges need [coated molybdenum][ref_molybdenum], graphite and [zirconia][ref_zirconia], good to around 3,000 degrees. The radiatively cooled structure was studied as a class rather than only as a Dyna-Soar component, in [Montsinger and Camilli 1944][research_montsinger_camilli_1944], [Montsinger and Camilli 1944, Thermal Protection or Transformers][research_montsinger_camilli_1944_2], [Serlin 1957][research_serlin_1957], [Jenness 1958][research_jenness_1958], [HOVEY 1965][research_hovey_1965], [STRAUSS 1967][research_strauss_1967], [RIVERS 1968][research_rivers_1968], [BAUER and KUMMER 1970][research_bauer_kummer_1970], [Alexander and Stanley 1999][research_alexander_stanley_1999], [Stanley et al 2000][research_stanley_2000], [Olds and Cowart 2001, Evaluation of Advanced Thermal Pro][research_olds_cowart_2001_2], [Liu et al 2002][research_liu_2002], [Daryabeigi et al 2006][research_daryabeigi_2006], [Hudson and Stephens 2006][research_hudson_stephens_2006], [Glass 2008][research_glass_2008], [Clarke 2008][research_clarke_2008], [Kowal 2011][research_kowal_2011]. **The coating rather than the metal is the pacing item**, because an uncoated refractory metal oxidises catastrophically in air at the temperatures that make it worth using, and the coating literature of 1960 to 1965 is correspondingly dense, in [MO 1963][research_mo_1963], [Criscione et al 1964][research_criscione_1964], [Turns and Hildebrand 1964][research_turns_hildebrand_1964], [Kaplow et al 1964][research_kaplow_1964], [Stetson and Wimber 1967][research_stetson_wimber_1967], [Phillips 1970][research_phillips_1970], [Peterson and Winter 1970][research_peterson_winter_1970], [Scott 1972][research_scott_1972], [Greenspan and Rizzitano 1972][research_greenspan_rizzitano_1972], [Wheeler and Brainard 1980][research_wheeler_brainard_1980], [Smeggil 1981][research_smeggil_1981], [Miller et al 1983][research_miller_1983], [Weaver 1983][research_weaver_1983], [Mahan 1984][research_mahan_1984], [Santiago-Aviles 1988][research_santiago_aviles_1988], [Glass and Camarda 1990][research_glass_camarda_1990], [Weiss and Srinivasan 1994][research_weiss_srinivasan_1994], [Malone and Walech 1995][research_malone_walech_1995].

The hot-structure experiments of the period are in [Pride et al 1960][research_pride_1960], [Baird 1964][research_baird_1964], [Brunner 1966][research_brunner_1966], [Brunner et al 1966, Study of thermal protection requir][research_brunner_1966_2], [Avery 1981][research_avery_1981], [Ko and Fields 1987][research_ko_fields_1987], [Blosser 1988][research_blosser_1988], [Goldstein 1992][research_goldstein_1992], [Carroll et al 1995][research_carroll_1995], [Blosser 1996][research_blosser_1996] and the materials work in [Maxwell 1952][research_maxwell_1952], [Mathauser et al 1960][research_mathauser_1960], [Peters and Rasnick 1961][research_peters_rasnick_1961], [Pride et al 1962][research_pride_1962], [Gangler 1963][research_gangler_1963], [Bliton and Rausch 1963][research_bliton_rausch_1963], [Bowers 1963][research_bowers_1963], [Bowers and Esch 1963][research_bowers_esch_1963], [Leeds 1963][research_leeds_1963], [HUGILL and GAIENNIE 1963][research_hugill_gaiennie_1963].

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

**The problem is not strength but accommodation.** Every shingle must be free to slide against its frame while remaining gas-tight.

The thermal stress problem in a hot structure was recognised early and worked continuously, in [GOLDBERG 1956][research_goldberg_1956], [Hughes 1956][research_hughes_1956], [Chen 1958][research_chen_1958], [Chen 1958, Closure to “Discussion of ‘Transie][research_chen_1958_2], [Dusinberre 1958][research_dusinberre_1958], [Buchsbaum 1963][research_buchsbaum_1963], [Pastine 1966][research_pastine_1966], [Stecura 1982][research_stecura_1982], [Stecura 1984][research_stecura_1984], [Strangman and Neumann 1985][research_strangman_neumann_1985], [Miller 1990][research_miller_1990], [Dinwiddie et al 1995][research_dinwiddie_1995]. **Two of those are the X-20's exact problem stated in the abstract**, being the temperature distribution and thermal stresses in a hypersonic wing structure, and transient temperature and thermal stresses in the skin of a hypersonic vehicle, both from the years the configuration was being chosen.

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

or about 1,365 statute miles of energy height, all of which must be disposed of before touchdown.

**The topic is narrow in the literature and the reason is instructive.** Terminal energy management for an unpowered orbital vehicle became a subject only once such a vehicle was actually going to be flown, in [MORTH 1972][research_morth_1972], [Tsukamoto et al 1999][research_tsukamoto_1999], [Jiang and Yang 2014][research_jiang_yang_2014], [Yang et al 2016][research_yang_2016]. The X-20 posed the problem and the Space Shuttle is where it was solved. **Too much on arrival and the vehicle overshoots with no way to slow down, too little and it lands short.** The pilot's task and the automation that supports it are the subject of [Lee and Mason 1960][research_lee_mason_1960] and [Young and Goode 1962][research_young_goode_1962], and the modern descendants of that problem are in [Fine 1967][research_fine_1967], [KRYVORUKA and ASHURST 1973][research_kryvoruka_ashurst_1973], [Lu 1996, Entry guidance and trajectory cont][research_lu_1996_2], [Lu 1997][research_lu_1997], [Hanson et al 1998][research_hanson_1998], [Fuhry 1999][research_fuhry_1999], [Calhoun 2000][research_calhoun_2000], [Burchett 2003][research_burchett_2003].

Attitude control at the top of the glide is reaction jets, because there is no air to work against. Control blends to aerodynamic surfaces as the vehicle descends, and [Fine 1967][research_fine_1967] treats the case where attitude is used specifically to hold skin temperature down. The wider control problem is treated in [Chowdhry et al 2001][research_chowdhry_2001], [Hanson and Jones 2004][research_hanson_jones_2004], [Janardanan and Jayakumar 2006][research_janardanan_jayakumar_2006], [NING et al 2007][research_ning_2007], [Morio et al 2009][research_morio_2009], [Halbe et al 2010][research_halbe_2010], [Matsumoto et al 2015][research_matsumoto_2015], [Zhi et al 2015][research_zhi_2015], [Gu et al 2016][research_gu_2016], [Liu et al 2016][research_liu_2016].

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

What did fly was the instrumentation. [ASSET][ref_asset] flew sub-scale radiatively cooled structures on Thor boosters between 1963 and 1965 and returned data on exactly the panels the X-20 would have used. The programme's own engineering record survives in unusual depth for a cancelled aircraft, and the wider boost-glide line it belongs to is documented alongside it, in [WA 1963][research_wa_1963], [Rock 1964][research_rock_1964], [NACA 1967, Study of the influence of size of][research_naca_1967_2], [Bryson et al 1968][research_bryson_1968], [Kempel et al 1971][research_kempel_1971], [Repic et al 1974][research_repic_1974], [Garcia 1975][research_garcia_1975], [Powell and Cruz 1991][research_powell_cruz_1991], [Kempel et al 1994][research_kempel_1994], [Barret 1999][research_barret_1999], [Scallion 1999][research_scallion_1999], [Chaudhary et al 2001][research_chaudhary_2001], [Taylor 2004][research_taylor_2004], [Dumbacher 2004][research_dumbacher_2004], [Jacobson 2004][research_jacobson_2004], [Jacobson 2004, X-37 Flight Demonstrator][research_jacobson_2004_2].

The launch side is comparatively thin here, because the vehicle never reached it, and what exists concerns the booster rather than the glider, in [Houser and Runciman 1971][research_houser_runciman_1971], [Stofan 1973][research_stofan_1973], [Lofland 1980][research_lofland_1980], [Benson et al 1993][research_benson_1993], [Hoffman 1996][research_hoffman_1996], [Maloney 2011][research_maloney_2011], [Dittemore and Harding 2011][research_dittemore_harding_2011], [Tarabini et al 2013][research_tarabini_2013], [Reed et al 2016][research_reed_2016].

## Comparison With Ground Prediction

The comparison cannot be made, and that is the finding rather than an omission.

**Every number in this article is a prediction against which no X-20 measurement exists**, because the vehicle never left the ground. The wind tunnel record for the configuration is extensive, in [Lovelace 1961][research_lovelace_1961], [Meckler 1964][research_meckler_1964], [Kaufman and G. 1964][research_kaufman_g_1964], [Murphy and Rubesin 1965][research_murphy_rubesin_1965], [Rochelle et al 1972][research_rochelle_1972], [Stainback et al 1972][research_stainback_1972], [Meng 1973][research_meng_1973], [Rosner and Cibrian 1974][research_rosner_cibrian_1974], [Sherman 1978][research_sherman_1978], [Baker and Kramer 1982][research_baker_kramer_1982], and none of it is flight data for this airframe. The configuration's aerodynamics were measured extensively in ground facilities, in [Luther Neal 1963][research_luther_neal_1963], [Ellison and Spencer 1971][research_ellison_spencer_1971], [Nelms and Thomas 1971][research_nelms_thomas_1971], [Arrington and Ashby 1972][research_arrington_ashby_1972], [Nelms 1972][research_nelms_1972], [Clark 1973][research_clark_1973], [Spencer and Fournier 1973][research_spencer_fournier_1973], [Dziubala et al 1973][research_dziubala_1973], [Penland et al 1974][research_penland_1974], [Creel and Penland 1974][research_creel_penland_1974], [Clark and Richie 1977][research_clark_richie_1977], [NACA 1981][research_naca_1981], [CA 1987][research_ca_1987], [Anderson and Jr 1988][research_anderson_jr_1988], [Anderson and D. 1991][research_anderson_d_1991], [Cockrell et al 1996][research_cockrell_1996], and the lifting-entry trajectory work that framed them is in [TERASAKI 1963][research_terasaki_1963], [CLAPP 1965][research_clapp_1965], [ZVARA 1966][research_zvara_1966], [GOLDBERG 1966][research_goldberg_1966], [MASAKI and YAKURA 1968][research_masaki_yakura_1968], [Townend 1979][research_townend_1979], [Johnson et al 1982][research_johnson_1982], [Spearman 1984][research_spearman_1984], [Ling et al 1991][research_ling_1991], [Ishimoto 1995][research_ishimoto_1995], [Li and Cui 2008][research_li_cui_2008], [Wu et al 2009][research_wu_2009], [Li et al 2010][research_li_2010], [Chao et al 2010][research_chao_2010].

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

### The Shape of the Reference Base

The coverage audit that preceded this pass produced the clearest instance in this series of a dependency between passes. **Five topics were thin in the pool, and they were exactly the five the equation pass had promoted.**

**Newtonian impact theory stood at zero records.** The article's independent cross-check on its own keystone had no reference base whatever, for the straightforward reason that the draft harvest could not know the cross-check would come to exist. Thermal expansion stood at eleven, emissivity at one, the ballistic coefficient at six, and energy management at four. A targeted search took them to fifteen, forty-seven, twenty-eight, twelve and seventeen.

**Everything the draft was already about was deep and under-used**, which is the opposite problem and admits no search-based fix. Radiative cooling held seventy-eight records against ten cited, refractory coatings seventy-three against seven, and launch seventy-nine against fifteen. Spreading the selection was the whole of the work there.

**Three homonym families had to be learned by reading**, and none was caught by any rule. In spectroscopy an impact theory is a model of collisional line broadening and has nothing to do with hypersonic flow. In aviation the terminal area is the airspace around an airport, so a search for terminal energy management returns air traffic control including a paper on Orly. And thermal expansion is a materials-science subject in plutonium, phthalocyanines and lithium hydride, none of which this article has any use for. A high-emissivity coating for television picture tubes was also returned and rejected.

**A process defect was found in this pass and is worth recording.** Four references rejected by reading during the draft pass reappeared in this one, because each pass rebuilds its rejection list from scratch rather than carrying forward decisions already made. Among them was a study of the thermal protection capacity of aviator's textiles, meaning clothing rather than vehicle structure. **The exclusion rule that should have caught it used a word boundary, and the word boundary is what let the plural through**, which is the opposite failure from the substring matching this series has documented three times. The rejection list is now written to a file so that later passes inherit it.

**One topic stays genuinely narrow and is reported rather than padded.** Terminal energy management for an unpowered orbital vehicle has four usable period references, because the subject did not exist until a vehicle was actually going to fly it.

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

**A rejection carried across passes rather than repeated.** Twenty-eight candidate references were rejected after being read rather than by any rule, across three passes, and the list is now persisted so that a later pass cannot reselect them. Four had already slipped back once before that was done.

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

[research_alexander_stanley_1999]: https://ntrs.nasa.gov/citations/19990116055
[research_anderson_d_1991]: https://doi.org/10.21236/ada233584
[research_anderson_jr_1988]: https://doi.org/10.21236/ada194265
[research_armstrong_1961]: https://doi.org/10.1016/0022-4073(61)90020-6
[research_arrington_ashby_1972]: https://ntrs.nasa.gov/citations/19720022344
[research_avery_1981]: https://ntrs.nasa.gov/citations/19810012587
[research_baird_1964]: https://doi.org/10.21236/ad0450460
[research_baker_kramer_1982]: https://doi.org/10.21236/ada114013
[research_barren_mandl_1978]: https://doi.org/10.2514/3.61019
[research_barret_1999]: https://ntrs.nasa.gov/citations/19990105819
[research_bauer_kummer_1970]: https://doi.org/10.2514/6.1970-273
[research_bell_1965]: https://doi.org/10.21236/ad0631590
[research_benson_1993]: https://ntrs.nasa.gov/citations/19930069750
[research_bernot_robinson_1958]: https://ntrs.nasa.gov/citations/19710074595
[research_bliton_rausch_1963]: https://ntrs.nasa.gov/citations/19640017101
[research_blosser_1988]: https://ntrs.nasa.gov/citations/19880013054
[research_blosser_1996]: https://ntrs.nasa.gov/citations/19970005361
[research_bowers_1963]: https://doi.org/10.21236/ad0409321
[research_bowers_esch_1963]: https://doi.org/10.21236/ad0421694
[research_brunner_1966]: https://ntrs.nasa.gov/citations/19670008949
[research_brunner_1966_2]: https://ntrs.nasa.gov/citations/19670008947
[research_bryson_1952]: https://doi.org/10.1090/qam/49749
[research_bryson_1968]: https://ntrs.nasa.gov/citations/19690010344
[research_buchsbaum_1963]: https://doi.org/10.21236/ad0402905
[research_budiansky_mayers_1956]: https://doi.org/10.2514/8.3735
[research_burchett_2003]: https://ntrs.nasa.gov/citations/20030093602
[research_ca_1987]: https://doi.org/10.21236/ada320212
[research_calhoun_2000]: https://ntrs.nasa.gov/citations/20000032921
[research_campbell_shepler_1960]: https://ntrs.nasa.gov/citations/19720063150
[research_carroll_1995]: https://ntrs.nasa.gov/citations/20020034891
[research_chao_2010]: https://doi.org/10.1109/isscaa.2010.5633153
[research_chaudhary_2001]: https://ntrs.nasa.gov/citations/20020023442
[research_chen_1958]: https://doi.org/10.1115/1.4012730
[research_chen_1958_2]: https://doi.org/10.1115/1.4012732
[research_chern_vinh_1978]: https://ntrs.nasa.gov/citations/19790013968
[research_chern_vinh_1980]: https://ntrs.nasa.gov/citations/19800007820
[research_chowdhry_2001]: https://doi.org/10.2514/6.2001-4043
[research_clapp_1965]: https://doi.org/10.2514/6.1965-492
[research_clark_1973]: https://ntrs.nasa.gov/citations/19740003718
[research_clark_richie_1977]: https://ntrs.nasa.gov/citations/19770017117
[research_clarke_2008]: https://doi.org/10.21236/ada500739
[research_cockrell_1996]: https://ntrs.nasa.gov/citations/19960045290
[research_creel_penland_1974]: https://ntrs.nasa.gov/citations/19740023372
[research_criscione_1964]: https://ntrs.nasa.gov/citations/19660014497
[research_czarnecki_davison_1960]: https://ntrs.nasa.gov/citations/19720063141
[research_daryabeigi_2006]: https://ntrs.nasa.gov/citations/20060022542
[research_delpino_1967]: https://ntrs.nasa.gov/citations/19690001538
[research_dinwiddie_1995]: https://ntrs.nasa.gov/citations/19960020887
[research_dittemore_harding_2011]: https://ntrs.nasa.gov/citations/20110016002
[research_dix_1967]: https://doi.org/10.21236/ad0813708
[research_doggett_1959]: https://ntrs.nasa.gov/citations/19650073709
[research_dsouza_1970]: https://doi.org/10.2514/6.1970-127
[research_dumbacher_2004]: https://ntrs.nasa.gov/citations/20040182602
[research_dusinberre_1958]: https://doi.org/10.1115/1.4012731
[research_dyke_1951]: https://doi.org/10.2514/8.2012
[research_dziubala_1973]: https://ntrs.nasa.gov/citations/19740005472
[research_ellison_spencer_1971]: https://ntrs.nasa.gov/citations/19710024532
[research_emmons_1951]: https://doi.org/10.1090/qam/38773
[research_emmons_1955]: https://doi.org/10.1007/978-3-663-20219-6_36
[research_fine_1967]: https://doi.org/10.21236/ad0654732
[research_fong_1970]: https://doi.org/10.21236/ad0866735
[research_foss_whitcomb_1960]: https://ntrs.nasa.gov/citations/19660024027
[research_foster_1960]: https://doi.org/10.1109/ire-i.1960.5006880
[research_freeman_1960]: https://doi.org/10.1017/s0022112060000451
[research_freeman_1960_2]: https://doi.org/10.2514/8.8394
[research_freeman_1962]: https://doi.org/10.1016/b978-0-12-395595-1.50021-0
[research_freeman_1996]: https://ntrs.nasa.gov/citations/19960053992
[research_freeman_1997]: https://ntrs.nasa.gov/citations/19990009876
[research_fuhry_1999]: https://doi.org/10.2514/6.1999-4211
[research_gangler_1963]: https://ntrs.nasa.gov/citations/19630029196
[research_garcia_1975]: https://ntrs.nasa.gov/citations/19760028347
[research_geiger_1963]: https://doi.org/10.21236/ada951933
[research_giles_thomas_1966]: https://ntrs.nasa.gov/citations/19660026817
[research_glass_2008]: https://ntrs.nasa.gov/citations/20080017096
[research_glass_camarda_1990]: https://ntrs.nasa.gov/citations/19910031414
[research_goldberg_1956]: https://doi.org/10.2514/8.3709
[research_goldberg_1966]: https://doi.org/10.2514/6.1966-464
[research_goldberg_1969]: https://ntrs.nasa.gov/citations/19700001407
[research_goldstein_1992]: https://ntrs.nasa.gov/citations/19930003260
[research_graves_carmel_1968]: https://ntrs.nasa.gov/citations/19680024364
[research_greenspan_rizzitano_1972]: https://doi.org/10.21236/ad0753340
[research_gu_2016]: https://doi.org/10.1109/imcec.2016.7867528
[research_halbe_2010]: https://doi.org/10.2514/6.2010-8311
[research_hanson_1998]: https://doi.org/10.2514/6.1998-4409
[research_hanson_jones_2004]: https://doi.org/10.2514/6.2004-701
[research_hayes_1959]: https://doi.org/10.1016/b978-1-4831-9832-3.50009-7
[research_helper_1960]: https://ntrs.nasa.gov/citations/19720063142
[research_hoffman_1996]: https://ntrs.nasa.gov/citations/19970001269
[research_hough_1982]: https://doi.org/10.2514/3.19788
[research_hough_1982_2]: https://doi.org/10.2514/6.1982-1480
[research_houser_runciman_1971]: https://ntrs.nasa.gov/citations/19720005230
[research_hovey_1965]: https://doi.org/10.2514/3.28175
[research_hudson_stephens_2006]: https://ntrs.nasa.gov/citations/20060056099
[research_hughes_1956]: https://doi.org/10.2172/4346693
[research_hugill_gaiennie_1963]: https://doi.org/10.21236/ad0295703
[research_ishimoto_1995]: https://doi.org/10.2514/6.1995-3286
[research_jacobson_2004]: https://ntrs.nasa.gov/citations/20040041355
[research_jacobson_2004_2]: https://ntrs.nasa.gov/citations/20040041357
[research_janardanan_jayakumar_2006]: https://doi.org/10.2514/6.2006-8076
[research_jenness_1958]: https://doi.org/10.1016/0038-092x(58)90049-5
[research_jiang_yang_2014]: https://doi.org/10.1155/2014/929731
[research_johnson_1982]: https://doi.org/10.21236/ada125406
[research_johnson_1998]: https://ntrs.nasa.gov/citations/19980107885
[research_johnson_rubesin_1949]: https://doi.org/10.1115/1.4017109
[research_kaplow_1964]: https://doi.org/10.21236/ad0602695
[research_kaufman_g_1963]: https://doi.org/10.21236/ad0431280
[research_kaufman_g_1964]: https://doi.org/10.21236/ad0609559
[research_kelly_1958]: https://ntrs.nasa.gov/citations/19930090181
[research_kempel_1971]: https://ntrs.nasa.gov/citations/19710041925
[research_kempel_1994]: https://ntrs.nasa.gov/citations/19940030197
[research_ko_fields_1987]: https://ntrs.nasa.gov/citations/19880001007
[research_kowal_2011]: https://ntrs.nasa.gov/citations/20110012175
[research_krusos_1967]: https://ntrs.nasa.gov/citations/19670025684
[research_kryvoruka_ashurst_1973]: https://doi.org/10.2514/6.1973-183
[research_lee_mason_1960]: https://ntrs.nasa.gov/citations/19720063138
[research_leeds_1963]: https://doi.org/10.21236/ad0400921
[research_li_2010]: https://doi.org/10.1109/icmet.2010.5598391
[research_li_cui_2008]: https://doi.org/10.1109/isscaa.2008.4776361
[research_ling_1991]: https://ntrs.nasa.gov/citations/19910011855
[research_liu_2002]: https://doi.org/10.21236/ada403577
[research_liu_2016]: https://doi.org/10.1109/cgncc.2016.7828785
[research_lofland_1980]: https://ntrs.nasa.gov/citations/19800015008
[research_lovelace_1961]: https://ntrs.nasa.gov/citations/19980227215
[research_lu_1996_2]: https://doi.org/10.2514/6.1996-3700
[research_lu_1997]: https://doi.org/10.2514/2.4008
[research_luce_jr_1949]: https://doi.org/10.21236/ada278113
[research_lunev_pavlov_1966]: https://doi.org/10.1007/bf01020459
[research_luther_neal_1963]: https://ntrs.nasa.gov/citations/19720065479
[research_mahan_1984]: https://doi.org/10.21236/ada146495
[research_malone_walech_1995]: https://ntrs.nasa.gov/citations/19950024110
[research_maloney_2011]: https://ntrs.nasa.gov/citations/20110012275
[research_manley_2000]: https://ntrs.nasa.gov/citations/20000040788
[research_masaki_yakura_1968]: https://doi.org/10.2514/6.1968-1155
[research_maslen_ostrach_1957]: https://doi.org/10.1090/qam/85874
[research_masters_cohen_1957]: https://doi.org/10.1063/1.1715801
[research_mathauser_1960]: https://ntrs.nasa.gov/citations/19980227836
[research_matsumoto_2015]: https://doi.org/10.2514/6.2015-1772
[research_maxwell_1952]: https://ntrs.nasa.gov/citations/19930086994
[research_mclellan_1955]: https://doi.org/10.1115/1.4014486
[research_meckler_1964]: https://doi.org/10.21236/ad0608830
[research_meckler_1965]: https://doi.org/10.21236/ad0620959
[research_meng_1973]: https://ntrs.nasa.gov/citations/19740005592
[research_merz_1968]: https://doi.org/10.21236/ad0830135
[research_miele_1957]: https://doi.org/10.2514/8.12515
[research_miller_1983]: https://ntrs.nasa.gov/citations/19840036161
[research_miller_1990]: https://ntrs.nasa.gov/citations/19910006099
[research_mo_1963]: https://doi.org/10.21236/ad0417153
[research_montsinger_camilli_1944]: https://doi.org/10.1109/ee.1944.6440234
[research_montsinger_camilli_1944_2]: https://doi.org/10.1109/t-aiee.1944.5058915
[research_morio_2009]: https://doi.org/10.1016/j.conengprac.2008.10.018
[research_morth_1972]: https://doi.org/10.2514/6.1972-833
[research_murphy_rubesin_1965]: https://ntrs.nasa.gov/citations/19660010795
[research_naca_1967_2]: https://ntrs.nasa.gov/citations/19670020694
[research_naca_1981]: https://ntrs.nasa.gov/citations/19810012492
[research_naca_1995]: https://ntrs.nasa.gov/citations/19960013899
[research_naftel_powell_1993]: https://ntrs.nasa.gov/citations/19930017827
[research_nelms_1972]: https://ntrs.nasa.gov/citations/19720016346
[research_nelms_thomas_1971]: https://ntrs.nasa.gov/citations/19720002396
[research_ning_2007]: https://doi.org/10.1016/s1000-9361(07)60001-6
[research_ny_1959]: https://doi.org/10.21236/ad0318479
[research_olds_cowart_2001]: https://ntrs.nasa.gov/citations/20010054791
[research_olds_cowart_2001_2]: https://ntrs.nasa.gov/citations/20020022190
[research_pai_1966]: https://doi.org/10.1007/978-3-7091-5730-5_11
[research_pastine_1966]: https://doi.org/10.1103/physrev.148.748
[research_paulson_shanks_1959]: https://ntrs.nasa.gov/citations/19980237090
[research_paulson_shanks_1961]: https://ntrs.nasa.gov/citations/19980227410
[research_peletskii_shur_1977]: https://doi.org/10.1007/bf00824276
[research_penland_1974]: https://ntrs.nasa.gov/citations/19740023375
[research_peters_rasnick_1961]: https://ntrs.nasa.gov/citations/20040006481
[research_peterson_winter_1970]: https://ntrs.nasa.gov/citations/19700000614
[research_pfaff_1968]: https://doi.org/10.21236/ad0832104
[research_phillips_1970]: https://ntrs.nasa.gov/citations/19700000654
[research_phillips_cohen_1959]: https://doi.org/10.2514/8.4789
[research_platus_1980]: https://doi.org/10.21236/ada093741
[research_powell_cruz_1991]: https://ntrs.nasa.gov/citations/19910034496
[research_pride_1960]: https://ntrs.nasa.gov/citations/19980223616
[research_pride_1962]: https://ntrs.nasa.gov/citations/19650014515
[research_rasky_1996]: https://ntrs.nasa.gov/citations/20020041186
[research_reba_1964]: https://doi.org/10.21236/ad0444094
[research_reed_2016]: https://ntrs.nasa.gov/citations/20160012009
[research_reinikka_sartell_1965]: https://doi.org/10.2514/3.28155
[research_repic_1974]: https://ntrs.nasa.gov/citations/19740010568
[research_rivers_1968]: https://doi.org/10.2514/3.29345
[research_robinson_bernot_1958]: https://ntrs.nasa.gov/citations/19930090105
[research_rochelle_1972]: https://ntrs.nasa.gov/citations/19720013202
[research_rock_1964]: https://doi.org/10.21236/ad0603307
[research_rosner_cibrian_1974]: https://ntrs.nasa.gov/citations/19740053212
[research_rotelli_1960]: https://ntrs.nasa.gov/citations/19720063136
[research_santiago_aviles_1988]: https://doi.org/10.21236/ada203428
[research_scallion_1999]: https://ntrs.nasa.gov/citations/19990117251
[research_scherberg_rubin_1953]: https://doi.org/10.21236/ad0012619
[research_schweppe_1964]: https://doi.org/10.21236/ad0609524
[research_scott_1972]: https://ntrs.nasa.gov/citations/19720000041
[research_seiff_wilkins_1961]: https://ntrs.nasa.gov/citations/19980227307
[research_serlin_1957]: https://doi.org/10.1126/science.126.3267.261-a
[research_sherman_1978]: https://doi.org/10.21236/ada056390
[research_smeggil_1981]: https://ntrs.nasa.gov/citations/19810022796
[research_snodgrass_1955]: https://doi.org/10.2514/8.6860
[research_spearman_1984]: https://ntrs.nasa.gov/citations/19850006478
[research_spencer_fournier_1973]: https://ntrs.nasa.gov/citations/19730018266
[research_stainback_1972]: https://ntrs.nasa.gov/citations/19790075398
[research_stanley_2000]: https://ntrs.nasa.gov/citations/20000021504
[research_stecura_1982]: https://ntrs.nasa.gov/citations/19820040090
[research_stecura_1984]: https://ntrs.nasa.gov/citations/19850012956
[research_stern_chu_1963]: https://doi.org/10.21236/ad0405109
[research_stetson_wimber_1967]: https://ntrs.nasa.gov/citations/19670026830
[research_stofan_1973]: https://ntrs.nasa.gov/citations/19730051292
[research_strangman_neumann_1985]: https://ntrs.nasa.gov/citations/19890004062
[research_strauss_1967]: https://doi.org/10.2514/3.29076
[research_sully_1952]: https://doi.org/10.1088/0508-3443/3/3/307
[research_tarabini_2013]: https://ntrs.nasa.gov/citations/20140002406
[research_taylor_2004]: https://ntrs.nasa.gov/citations/20040037790
[research_terasaki_1963]: https://doi.org/10.2514/6.1963-320
[research_tillier_1998]: https://ntrs.nasa.gov/citations/19990004144
[research_townend_1979]: https://doi.org/10.1016/0376-0421(79)90001-0
[research_tsukamoto_1999]: https://doi.org/10.2514/6.1999-4058
[research_turns_hildebrand_1964]: https://doi.org/10.21236/ad0436260
[research_vandrey_1957]: https://doi.org/10.2514/8.12849
[research_vanmol_anderson_1992]: https://ntrs.nasa.gov/citations/19920012972
[research_verhoff_1990]: https://doi.org/10.1007/978-3-662-02643-4_12
[research_vertogradskii_1969]: https://doi.org/10.1007/bf00979969
[research_vinh_lin_1982]: https://ntrs.nasa.gov/citations/19820019475
[research_wa_1963]: https://doi.org/10.21236/ad0336996
[research_walker_1962]: https://ntrs.nasa.gov/citations/19620004472
[research_wang_2011]: https://doi.org/10.3724/sp.j.1010.2010.00367
[research_warmbrod_1963]: https://ntrs.nasa.gov/citations/19630005471
[research_weaver_1983]: https://doi.org/10.21236/ada135340
[research_weiss_srinivasan_1994]: https://doi.org/10.21236/ada329833
[research_wheeler_brainard_1980]: https://ntrs.nasa.gov/citations/19800041104
[research_wong_slye_1961]: https://ntrs.nasa.gov/citations/19980232890
[research_wu_2009]: https://doi.org/10.1007/978-3-642-01513-7_27
[research_yang_2016]: https://doi.org/10.1109/cgncc.2016.7829103
[research_young_goode_1962]: https://ntrs.nasa.gov/citations/19620002806
[research_zhi_2015]: https://doi.org/10.1016/j.proeng.2014.12.633
[research_zimmermann_1996]: https://doi.org/10.2514/6.1996-3708
[research_zvara_1966]: https://doi.org/10.2514/6.1966-360

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
