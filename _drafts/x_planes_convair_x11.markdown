---
layout: post
mathjax: true
comments: true
title: "X-Planes: Convair X-11"
date: 2025-10-17 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 12
---

<!-- A308 -->
<script>console.log("A308");</script>

The [Convair X-11][ref_x11] could not stand up. Left on its own with the tanks empty and unpressurised it would fold under its own weight, so it was kept inflated with nitrogen at five pounds per square inch from the moment it left the factory until the moment it was destroyed. This article is the twelfth in the [X-Planes series][related_post_a297_xplanes_framing], following the [X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], the [X-4][related_post_a301_northrop_x4], the [X-5][related_post_a302_bell_x5], the [X-6][related_post_a303_convair_x6], the [X-7][related_post_a304_lockheed_x7], the [X-8][related_post_a305_aerojet_x8], the [X-9][related_post_a306_bell_x9], and the [X-10][related_post_a307_north_american_x10].

It is also the vehicle the previous article was about without naming. The [X-10][related_post_a307_north_american_x10] was the testbed for the Navaho, an intercontinental cruise missile that was cancelled in July 1957 because a ballistic weapon of the same range arrives in about thirty-two minutes where an airbreathing one is exposed for a hundred and seventy-two. **The X-11 is that ballistic weapon.** It is the Atlas A, the first flying article of the programme that killed the Navaho, and it first flew on 11 June 1957, four weeks before the cancellation message. The standard inventory entry remains [Jenkins Landis and Miller 2003 American X-Vehicles, An Inventory X-1 to X-50][book_jenkins_landis_miller_2003], the vehicle compilation comes from [Miller 2001 The X-Planes, X-1 to X-45][book_miller_2001], and the structural principle has its own literature under the name [balloon tank][ref_balloon_tank].

## The Research Question

An intercontinental ballistic missile is a mass-fraction problem before it is anything else, and the reason is that the rocket equation is unforgiving in a way no other transport relation is.

### Why Structure Is the Binding Constraint

The velocity a rocket can reach is

$$\Delta v = v_{e} \ln \frac{m_{0}}{m_{f}}$$

where $v_e$ is the effective exhaust velocity and the mass ratio is gross mass over burnout mass. The burnout mass is structure plus payload, so **every kilogramme of structure is a kilogramme that must be accelerated to the full burnout velocity and then thrown at the target for no effect**. The logarithm is the difficulty. Improving the exhaust velocity gives a linear return, and improving the mass ratio gives a return that is only logarithmic, which means an intercontinental weapon must sit far out on a curve that is flattening under it.

The Atlas achieved a burnout mass of 5,395 kilogrammes on a gross mass of 117,900, so its structural mass fraction is

$$\frac{m_{s}}{m_{0}} = \frac{5395}{117{,}900} = 0.0458$$

and its propellant mass fraction is 95.4 percent. The mass ratio is therefore

$$\frac{m_{0}}{m_{f}} = \frac{117{,}900}{5395} = 21.85$$

At a specific impulse of 282 seconds the effective exhaust velocity is $v_e = 282 \times 9.80665 = 2765$ metres per second, and the ideal velocity is

$$\Delta v = 2765 \times \ln 21.85 = 8530 \, \text{m/s}$$

**Four and a half percent is an extraordinary number for a structure that has to survive launch.** An airliner's structure is a quarter of its take-off weight. The Atlas is a fuel tank with an engine bolted underneath and almost nothing else, and the article's subject is what that costs and what it buys. The relation itself and the design practice built on it are [Sutton and Biblarz 2016 Rocket Propulsion Elements][book_sutton_biblarz_2016], with the period treatment of the limiting mass ratio in [Wertheimer 1957][research_wertheimer_1957] and the gravitational correction that separates ideal from achieved velocity in [Sellers 1948][research_sellers_1948] and [Feodosiev and Siniarev 1959][research_feodosiev_siniarev_1959].

### The Payoff, Carried Through to Range

The [previous article][related_post_a307_north_american_x10] derived the burnout speed a minimum-energy ballistic trajectory needs to cover ten thousand kilometres, which is 7193 metres per second. Setting that against the ideal velocity above gives the losses the ascent must absorb,

$$v_{\text{loss}} = \Delta v - v_{bo} = 8530 - 7193 = 1337 \, \text{m/s}$$

or 15.7 percent of the ideal velocity, which is a reasonable figure for gravity and drag losses on a vertical-rising ballistic ascent and is adopted here as a calibration and not derived. With it fixed, the structural mass can be varied and carried all the way through to a range. Holding the propellant load constant and scaling only the structure,

$$v_{bo}(k) = v_{e} \ln \frac{m_{p} + k m_{s}}{k m_{s}} - v_{\text{loss}}$$

and feeding the result into the range relation of the previous article, which is

$$\sin \frac{\Phi}{2} = \frac{\lambda}{2 - \lambda}, \qquad \lambda = \frac{v_{bo}^{2}}{g R_{e}}, \qquad R = R_{e} \Phi$$

gives

| Structure | Burnout speed | Range |
|-----------|---------------|-------|
| as built | 7193 m/s | 9,999 km |
| 1.5 times | 6134 m/s | 5,676 km |
| 2 times | 5400 m/s | 3,941 km |
| 3 times | 4397 m/s | 2,346 km |

**Making the structure half as efficient costs sixty-one percent of the range.** A vehicle at one and a half times the Atlas structural mass is not a worse intercontinental missile. It is an intermediate-range missile, which is a different weapon with a different basing problem and a different strategic meaning. That is the whole argument for the balloon tank, and it is why a programme accepted a vehicle that cannot be left standing without a nitrogen supply.

The trajectory machinery behind those numbers is period material, not a modern reconstruction. [Ostner 1962][research_ostner_1962] reduces ballistic trajectory computation to what a range could run and [Walters 1967][research_walters_1967], the closed-form treatments are [Punga and Campbell 1962][research_punga_campbell_1962] and [Bell 1965][research_bell_1965], [Stancil 1963][research_stancil_1963] optimises by steepest ascent, [Lubowe 1965][research_lubowe_1965] brings dynamic programming to optimum staging, and [Randall 1970][research_randall_1970] traces the effect of staging on the resulting trajectory, with performance bookkeeping in [Adams and Stoll 1969][research_adams_stoll_1969] and payload-optimal trajectories in [Elliott and Rau 1968][research_elliott_rau_1968].

The caution the table requires is that the loss figure was calibrated so the baseline reproduces the previous article's ten thousand kilometres, so the first row is fixed by construction. The **sensitivity** is the result, not the absolute range, and the sensitivity is robust because it depends on the logarithm and not on the calibration.

### The Keystone Is Exercised Early, Which Is Why This Testbed Worked

The [X-10][related_post_a307_north_american_x10] flew for twenty-eight minutes against a mission of a hundred and seventy-two, and the article's central result was that its keystone quantity, a gyroscope drift rate, accumulates with time and therefore could not be measured over so short a window. The X-11 has the opposite property and it is worth stating plainly because it is the sharpest contrast the series has yet produced.

**The Atlas structure is fully loaded within the first two minutes of flight.** Maximum dynamic pressure occurs about a minute after lift-off, the highest axial acceleration occurs at booster cutoff, and both fall inside a 133 second burn. The two loads can be written as fractions of the mission and the comparison is stark. For the Atlas the structurally sizing events occur at

$$\frac{t_{\text{sizing}}}{t_{\text{mission}}} = \frac{133}{1932} = 0.069$$

taking the mission as the 1932 second ballistic flight time derived in the previous article, so **the structure is finished being tested seven percent of the way through the mission**. For the X-10 the corresponding ratio was

$$\frac{t_{\text{flown}}}{t_{\text{mission}}} = \frac{1653}{10{,}333} = 0.16$$

and the keystone was still not exercised, because a drift rate is not a load. **The X-11 tested more of its keystone in seven percent of its mission than the X-10 did in sixteen percent of its**, which is the compact form of the whole comparison. That the structurally sizing events cluster early is not an accident of this vehicle but a property of any rocket ascent, and the period literature establishing where they fall runs through [Wood 1961][research_wood_1961] on missile structural dynamics, [Gerald and Runyan 1962][research_gerald_runyan_1962] on the launch-vehicle case, and the ground-wind and ascent-load material cited below. **The general point that a test article need only span the sizing envelope, not the mission is implicit in structural test practice** and is stated directly in [Abraham 1963][research_abraham_1963], which is about how to load a large article representatively and not exhaustively. A flight that goes no further than a hundred and twenty kilometres of apogee and a fifth of the intercontinental burnout speed still applies every structural load the mission will ever apply. **A keystone that is exercised early can be validated cheaply. A keystone that accumulates cannot.** The X-11 flew a fraction of the weapon's mission and tested its keystone completely, and the X-10 flew a fraction of its weapon's mission and tested its keystone hardly at all, and the difference is not programme competence but the mathematical character of the quantity each was built to establish.

## Programme Origin

Convair had been working on long-range missiles since 1946 under project MX-774, a study that the Air Force cancelled in 1947 and that Convair partly continued on its own money. The work resumed as MX-1593 in 1951 and became the Atlas. The design authority throughout was Karel Bossart, whose contribution is the pressure-stabilised tank and whose reported inspiration was a cylindrical party balloon.

The German inheritance that shaped the American ballistic effort generally occupies [Neufeld 1995 The Rocket and the Reich][book_neufeld_1995], and [Walker Bernstein and Lang 2005 Seize the High Ground][book_walker_powell_2005] carries the institutional history of the Air Force missile and space organisation, with a period account of the ballistic missile division's own evolution in [Rockefeller and Alfred 1960][research_rockefeller_alfred_1960]. Contemporary surveys of the whole weapon class are [Botterill 1961][research_botterill_1961] and [Lenihan 1962][research_lenihan_1962], which are useful precisely because they record what was thought at the time, not what turned out to be true. **The point worth holding is that Convair reached the pressure-stabilised structure from an aircraft background and not from a rocket one.** A company that builds thin-skinned pressurised fuselages has the instinct that a pressure vessel can be a primary structure, and the monocoque analysis the field already had runs from [Hoff 1942][research_hoff_1942], [Wang and Ramamritham 1947][research_wang_ramamritham_1947], and [Kaufman 1958][research_kaufman_1958].

The programme designation the record actually uses is **WS 107A-1**, and the missile family became SM-65 with variants lettered A through F. The X-11 designation was assigned to the Atlas A and the X-12 to the Atlas B, which the next article treats. **Whether either designation was ever used operationally is not clear from the accessible record**, and the Epistemic State says so. What is clear is that these are the fourth and fifth consecutive X numbers attached to vehicles that were never research aircraft, following the [X-8][related_post_a305_aerojet_x8], the [X-9][related_post_a306_bell_x9], and the [X-10][related_post_a307_north_american_x10], and that the pattern the previous article identified, of a separate series being absorbed, not of the X-series broadening on the merits, now has more cases than it had exceptions.

### Why the Idea Was Available to Convair and Not to Others

The pressure-stabilised tank is usually told as a flash of insight, and the party-balloon anecdote encourages that. The more useful reading is that Convair was the company most likely to have it, and for a reason that has nothing to do with rockets.

**An aircraft company that builds pressurised fuselages already believes that a pressure vessel can be primary structure.** A transport fuselage is a thin shell that carries bending, torsion, and cabin pressure at once, and the analysis for it existed, in [Hoff 1942][research_hoff_1942], [Wang and Ramamritham 1947][research_wang_ramamritham_1947], and [Kaufman 1958][research_kaufman_1958]. What Convair did was to remove the frames and stringers that a fuselage keeps because it must survive depressurisation, and to accept in exchange a structure that must never be depressurised.

That is a trade an aircraft company can see and a rocket company might not, because it is a trade about what the structure is allowed to fail at and not about how strong it is. **The Atlas is not a stronger tank. It is a tank that has been permitted to have a failure mode nobody would tolerate in an aeroplane**, in exchange for a mass fraction nobody could reach any other way, and permitting that failure mode is a programme decision, not an engineering one.

The decision also depended on the mission. A weapon is expended, so a structure that cannot survive loss of pressure is acceptable in a way it would not be for something expected to be reused, ferried, stored unattended, or damaged and repaired. **The X-10 in the previous article was recoverable and therefore could not make this trade.** The two are four weeks and one designation apart and their structural philosophies are opposite, and the reason is the same one that separated their keystones.

### The One-and-a-Half Stage Arrangement

The Atlas carries three engines and jettisons two of them. All three ignite on the ground, and at booster cutoff the two outboard engines and their skirt are dropped while the sustainer continues on the same tanks. The arrangement exists because igniting a large liquid engine at altitude was not trusted in 1955, so the vehicle stages its **engines** without staging its **tanks**.

That decision interacts directly with the keystone. A conventional two-stage vehicle discards a whole tank set, which is where most of the structural benefit of staging comes from. The Atlas discards only engines and skirt, so it gets a smaller staging benefit and has to make it up in structural efficiency. **The balloon tank and the one-and-a-half stage arrangement are the same decision seen twice**, since the vehicle that cannot drop its tanks must make its tanks weigh almost nothing. [Schurmann 1957][research_schurmann_1957], [Parkyn 1958][research_parkyn_1958], and [Wertheimer 1957][research_wertheimer_1957] optimise staging for the period, with the gravitational term in [Sellers 1948][research_sellers_1948].

## Sizing From First Principles

### The Shell, and How Thin It Actually Is

The Atlas is a cylinder ten feet in diameter and just over twenty-three metres long, so the tank radius is

$$r = \frac{10 \times 0.3048}{2} = 1.524 \, \text{m}$$

and the skin is 301 extra-full-hard stainless steel between 0.014 and 0.037 inches thick, which is 0.356 to 0.940 millimetres. The ratio that governs everything about a thin shell is radius over thickness,

$$\frac{r}{t} = \frac{1.524}{0.000356} = 4286 \qquad \frac{r}{t} = \frac{1.524}{0.000940} = 1622$$

Those numbers are hard to feel, so here is a benchmark. An aluminium drink can has a radius near 33 millimetres and a wall near 0.1 millimetres, giving

$$\left. \frac{r}{t} \right|_{\text{can}} = \frac{0.033}{0.0001} = 330$$

**The Atlas skin is between five and thirteen times thinner in proportion than a drink can**, and a drink can also cannot be stood on unless it is sealed and pressurised, which is the same physics on a scale one can hold.

### Membrane Stress, and Why the Gauge Is Tapered

A pressurised thin cylinder carries its load in membrane tension. The hoop stress is

$$\sigma_{\theta} = \frac{p r}{t}$$

and the axial stress from the same pressure acting on the ends is half of it,

$$\sigma_{z} = \frac{p r}{2 t}$$

The ratio is fixed by geometry and not by design,

$$\frac{\sigma_{\theta}}{\sigma_{z}} = 2$$

which has a consequence every pressure vessel shares. **The hoop direction is always the first to yield, so a tank that bursts splits along its length and not around its circumference**, and the weld that runs longitudinally is therefore the one that decides the vehicle.

At a flight tank pressure of about 60 pounds per square inch and the heavy gauge this gives

$$\sigma_{\theta} = \frac{413{,}685 \times 1.524}{0.000940} = 671 \, \text{MPa}$$

against a yield near 965 megapascals for the material in its extra-full-hard condition, a margin of 1.44. At the light gauge the same pressure would give

$$\sigma_{\theta} = \frac{413{,}685 \times 1.524}{0.000356} = 1773 \, \text{MPa}$$

which exceeds the ultimate strength of the material. **The light gauge therefore cannot exist anywhere the pressure is high**, and that is not a criticism of the calculation but a demonstration of the design rule. The gauge is tapered to the local stress, and the local stress is dominated not by ullage pressure but by the head of propellant above the station under acceleration,

$$\Delta p = \rho \, n \, g \, h$$

For liquid oxygen at 1141 kilogrammes per cubic metre, ten metres of head, and six times gravity near burnout,

$$\Delta p = 1141 \times 6 \times 9.80665 \times 10 = 671{,}000 \, \text{Pa} = 97 \, \text{psi}$$

which is **more than one and a half times the ullage pressure**. The bottom of the tank is the hardest-worked part of the vehicle and it is thickest there, and this is only possible at all because a membrane structure can be thinned where the load is small without any of the discontinuities that a stiffened structure would introduce. Membrane analysis of the period runs through [Bahiman and Thole 1965][research_bahiman_thole_1965], with monocoque ring analysis in [Hoff 1942][research_hoff_1942] and material data in [Manning and Price 1961][research_manning_price_1961], [Johnson and Kelsen 1969][research_johnson_kelsen_1969], and [Kuentz 1969][research_kuentz_1969].

### The Common Bulkhead, Which Is the Other Half of the Idea

The Atlas carries liquid oxygen and kerosene in one shell divided by a single dome, not in two tanks with structure between them. The saving is a whole pressure dome and the intertank barrel that would separate them, and for a shell of this diameter that is a large fraction of the dry mass. A hemispherical dome of radius $r$ has an area of

$$A_{\text{dome}} = 2 \pi r^{2} = 2 \pi \times 1.524^{2} = 14.6 \, \text{m}^{2}$$

and an intertank barrel long enough to clear two domes adds roughly

$$A_{\text{barrel}} = 2 \pi r \times 2r = 4 \pi r^{2} = 29.2 \, \text{m}^{2}$$

so the common bulkhead removes on the order of forty square metres of shell, which at the average gauge is

$$m_{\text{saved}} = 43.8 \times 0.000648 \times 8000 = 227 \, \text{kg}$$

or **about four percent of the whole empty vehicle from one design decision**. The cost is that the bulkhead now separates a cryogen at 90 kelvin from a hydrocarbon at ambient temperature, so it must insulate as well as carry load, and a leak across it mixes the propellants inside the vehicle. **The common bulkhead is the Atlas idea that outlived the balloon tank**, and it is standard on cryogenic stages today for exactly the reason computed here. [Weiss and Goodman 1960][research_weiss_goodman_1960] takes up the insulation problem it creates, with and [Walton and Simmons 1962][research_walton_simmons_1962], and the vehicle that took the arrangement furthest in the period, and which kept the balloon tank as well, is described in [Chitwood 1962][research_chitwood_1962]. Membrane analysis of the domes themselves appears in [Bahiman and Thole 1965][research_bahiman_thole_1965] and [Adam and King 1965][research_adam_king_1965].

### What Is Inside, and the Gas That Holds It All Up

The tank volume follows from the geometry,

$$V = \pi r^{2} L = \pi \times 1.524^{2} \times 18 = 131 \, \text{m}^{3}$$

and at a mixture ratio near 2.25 the propellant load divides into

$$m_{\text{LOX}} = m_{p} \frac{MR}{1 + MR} = 112{,}505 \times \frac{2.25}{3.25} = 77{,}888 \, \text{kg}$$

with the balance of 34,617 kilogrammes as kerosene. At densities of 1141 and 800 kilogrammes per cubic metre the volumes are 68.3 and 43.3 cubic metres, so the propellant occupies

$$\frac{111.5}{131} = 0.85$$

of the tank, leaving fifteen percent for ullage, insulation, and the domes, which is a sane figure and a weak confirmation that the assumed tank length is about right.

Against all of that, the mass of nitrogen needed to hold five pounds per square inch of gauge pressure through the whole volume is

$$m_{N_{2}} = \frac{p V}{R T} = \frac{34{,}474 \times 131}{296.8 \times 290} = 52.6 \, \text{kg}$$

**Fifty-three kilogrammes of gas holds up five thousand three hundred and ninety-five kilogrammes of steel**, a ratio of 103 to one. That single comparison is the whole design in one line.

The gas is also, unlike everything else aboard, entirely recoverable and entirely cheap, which is the part of the bargain that made it acceptable. Nitrogen at five pounds per square inch costs nothing and weighs nothing that matters, and a structure that trades steel for nitrogen is trading an expensive mass for a free one.

Getting the gas in and keeping it there is a discipline of its own, and the period worked it thoroughly because every large liquid vehicle needed it. [Kaplan 1961][research_kaplan_1961] selects a pressurisation system, autogenous systems that use the propellant's own vapour are [Morey and Koshar 1961][research_morey_koshar_1961] and [Coxe and Tatom 1962][research_coxe_tatom_1962], pressurised transfer and discharge of cryogens are [Humphrey 1961][research_humphrey_1961] and [Nein and Head 1962][research_nein_head_1962], and the dilution and conditioning problems that arise before launch are [Greenfield 1960][research_greenfield_1960], with test facility practice in [Mandell and White 1960][research_mandell_white_1960]. **On a conventional vehicle this apparatus feeds the engines. On this one it also holds the vehicle up**, which is why a pressurisation fault here is a structural event.

A useful figure of merit for a tank is its mass per unit of volume contained,

$$\eta_{\text{tank}} = \frac{m_{\text{skin}}}{V} = \frac{893}{131} = 6.8 \, \text{kg/m}^{3}$$

which can be read as the penalty paid for carrying a cubic metre of propellant. Against a propellant density averaging

$$\bar{\rho}_{p} = \frac{m_{p}}{V_{p}} = \frac{112{,}505}{111.5} = 1009 \, \text{kg/m}^{3}$$

the tank costs **less than seven kilogrammes for every tonne of propellant it holds**, which is the number that makes a mass ratio of twenty-two possible at all.

### Buckling, Which Is the Failure Mode That Matters

A thin cylinder in axial compression does not fail by crushing. It buckles, and the classical critical stress is

$$\sigma_{cr} = \frac{E t}{r \sqrt{3 (1 - \nu^{2})}}$$

which for the heavy gauge at a Young's modulus of 193 gigapascals gives

$$\sigma_{cr} = \frac{193 \times 10^{9} \times 0.000940}{1.524 \times 1.652} = 72.0 \, \text{MPa}$$

and for the light gauge 27.3 megapascals. **That figure is not what a real shell achieves.** Thin cylinders buckle far below the classical value because the post-buckling equilibrium path falls away steeply and any small imperfection lets the shell find it, which is the result of [Karman and Tsien 1941][research_karman_tsien_1941] and the post-buckling behaviour of [Michielsen 1948][research_michielsen_1948]. Design practice applies a knockdown factor, and at the radius-to-thickness ratios here a factor of 0.2 to 0.3 is representative, giving an allowable of

$$\sigma_{\text{allow}} = 0.2 \times 72.0 = 14.4 \, \text{MPa}$$

for the heavy gauge and 5.5 megapascals for the light one. **A structure whose tensile capacity is 965 megapascals has a compressive capacity of five**, a ratio of nearly two hundred, and that asymmetry is the entire reason the design exists.

It is worth ruling out the other buckling mode explicitly, because a twenty-three metre column is an obvious candidate for it. Treating the vehicle as a cantilever beam of thin-walled section, the second moment of area is

$$I = \pi r^{3} t = \pi \times 1.524^{3} \times 0.000648 = 7.20 \times 10^{-3} \, \text{m}^{4}$$

and the Euler critical load with an effective length factor of two for a fixed base and free top is

$$P_{cr} = \frac{\pi^{2} E I}{(K L)^{2}} = \frac{\pi^{2} \times 193 \times 10^{9} \times 7.20 \times 10^{-3}}{(2 \times 23.11)^{2}} = 6.42 \, \text{MN}$$

against an empty weight of 52.9 kilonewtons, a margin of 121. **It does not fold as a column. It crumples as a shell**, and the distinction matters because the two failure modes are separated by two orders of magnitude and only one of them is helped by pressure. Shell stability work of the period spans [Nickell 1961][research_nickell_1961], [Hausrath and Dittoe 1962][research_hausrath_dittoe_1962], [Hoff et al 1962][research_hoff_1962], and [Bozich 1967][research_bozich_1967], with the external-pressure case in [Shaw et al 1952][research_shaw_1952] and [Reynolds 1960][research_reynolds_1960], the conical case in [Mescall 1961][research_mescall_1961], torsional buckling in [Mow and Sadowsky 1962][research_mow_sadowsky_1962], and dynamic buckling in [Coppa and Nash 1962][research_coppa_nash_1962] and [Coppa and Nash 1964][research_coppa_nash_1964]. **The alternatives to a bare pressurised shell were being measured at the same time**, with stiffener sizing in [Nott 1963][research_nott_1963] and sandwich construction under combined loading in [Wang et al 1953][research_wang_1953], and the Atlas decision is only intelligible against that comparison.

### What Five Pounds per Square Inch Buys

Internal pressure produces axial tension, and a fibre that is in tension cannot buckle. The tension from the standing nitrogen pressure alone is

$$\sigma_{z} = \frac{34{,}474 \times 1.524}{2 \times 0.000940} = 27.9 \, \text{MPa}$$

at the heavy gauge and 73.9 megapascals at the light one. Set those against the knocked-down buckling allowables of 14.4 and 5.5 megapascals respectively and the result is stark. **Five pounds per square inch of nitrogen roughly doubles the effective compressive capability of the heavy gauge and multiplies the light gauge by more than thirteen.** The pressure is not a convenience. It is the larger part of the structure.

The relation can also be inverted, and inverting it explains where the number five came from. Requiring the axial tension from pressure to equal the knocked-down buckling allowable gives

$$p_{\text{req}} = \frac{2 t \sigma_{\text{allow}}}{r}$$

which at the heavy gauge is

$$p_{\text{req}} = \frac{2 \times 0.000940 \times 14.4 \times 10^{6}}{1.524} = 17{,}768 \, \text{Pa} = 2.58 \, \text{psi}$$

and at the light gauge only 0.37 pounds per square inch, because the buckling allowable falls faster with thickness than the pressure tension does. **The governing case is the heavy gauge and it needs 2.58 pounds per square inch, so the reported five-pound standing specification carries a margin of 1.94 on the calculation performed here.**

The relation used here is a first-order one and the period had a better one. [Peterson 1960][research_peterson_1960] correlates the measured buckling strength of pressurised cylinders against the pressure parameter directly, which is the empirical form the design offices actually used, and [Weingarten 1962][research_weingarten_1962] extends it. The reason such a correlation was needed and not a theory appears in [Babcock and Sechler 1962][research_babcock_sechler_1962] and [Babcock and Sechler 1963][research_babcock_sechler_1963], which measure how much of the classical strength an initial imperfection removes, with the post-buckling behaviour that makes the sensitivity so severe in [Thielemann 1962][research_thielemann_1962] and [Greenspon 1963][research_greenspon_1963]. A specification that lands at roughly twice the computed requirement is what a designer writes when the computed requirement rests on a knockdown factor he does not trust, which is exactly the situation described above.

The cleanest statement of the principle is in bending, not in compression. For a thin-walled cylinder the second moment of area is $I = \pi r^{3} t$, so a bending moment produces an extreme-fibre stress of $M r / I$. Setting that equal to the axial tension from pressure gives the moment at which the most compressed fibre first reaches zero stress,

$$\frac{M r}{\pi r^{3} t} = \frac{p r}{2 t} \quad \Longrightarrow \quad M_{\text{crit}} = \frac{\pi p r^{3}}{2}$$

**The thickness cancels.** The moment a pressure-stabilised cylinder can carry before any part of it goes into compression depends on the pressure and the radius and not at all on how thin the skin is, which is the mathematical form of the claim that the pressure is doing the work. At the standing pressure this is

$$M_{\text{crit}} = \frac{\pi \times 34{,}474 \times 1.524^{3}}{2} = 0.192 \, \text{MN m}$$

equivalent to a lateral force of 8.3 kilonewtons at the top of a 23 metre vehicle, and at flight pressure it is 2.30 meganewton metres, or 99.5 kilonewtons. **A missile standing on the pad in a wind is held up by a pressure a bicycle tyre would find low**, and the flight case is twelve times stiffer because the tanks are pressurised harder once loaded.

That moment converts to a wind speed, which is the form an operations manual would want it in. Taking the wind as a uniform load on a cylinder of drag coefficient 1.2, the drag force is $F = \tfrac{1}{2} \rho V^{2} C_{D} D L$ acting at mid-height, so the moment at the base is

$$M = \tfrac{1}{4} \rho V^{2} C_{D} D L^{2}$$

and inverting it for the standing case gives

$$V = \sqrt{\frac{4 M_{\text{crit}}}{\rho C_{D} D L^{2}}} = \sqrt{\frac{4 \times 1.917 \times 10^{5}}{1.225 \times 1.2 \times 3.048 \times 23.11^{2}}} = 17.9 \, \text{m/s}$$

or **thirty-five knots before any fibre of the standing vehicle goes into compression**, falling to about twenty-eight knots with a factor of 1.5 applied to the moment. At flight pressure the same relation gives 120 knots.

Two things follow. **The standing limit is an ordinary windy day**, which is why the ground-wind literature cited below was not an academic interest for this programme, and why a vehicle left on the pad through weather is at risk in a way a stiffened one is not. And **the margin improves by a factor of three and a half the moment the tanks are pressurised for flight**, so the dangerous condition is the one that lasts for days and not the one that lasts for minutes. That inversion, in which the vehicle is most fragile when nothing is happening to it, is the operational signature of the whole design. **The measurement this whole section describes was actually made.** [Miller and Gerus 1966][research_miller_gerus_1966] reports the bending strength of a large thin-walled pressure-stabilised cylinder, which is the relation derived above tested on hardware of the right size, and it is the single most directly relevant document found for this article. [Ichino and Takahashi 1965][research_ichino_takahashi_1965] treats the non-symmetrical bending state of such a shell, [Ugural and Cheng 1968][research_ugural_cheng_1968] takes pure bending, [Kempner and Chen 1974][research_kempner_chen_1974] handles the oval case that an imperfect cylinder becomes, and [Wang 1973][research_wang_1973] measures post-buckling of cold-formed thin-walled stainless specifically.

Pressure-stabilised beams under load are treated directly by [Steeves 1975][research_steeves_1975] and [Steeves 1975, A Linear Analysis of the Deformati][research_steeves_1975_2], [Weingarten 1962][research_weingarten_1962] isolates the effect of internal pressure on cylinder buckling, and collapse tests of pressurised membrane-like cylinders are [Leaumont 1965][research_leaumont_1965], with monocoque dome stability in [Adam and King 1965][research_adam_king_1965] and creep buckling, which matters for a tank held pressurised for long periods, in [Samuelson 1968][research_samuelson_1968].

### What the Structure Actually Weighs

The bare skin of a tank eighteen metres long at the average gauge masses

$$m_{\text{skin}} = 2 \pi r L t \rho = 2 \pi \times 1.524 \times 18 \times 0.000648 \times 8000 = 893 \, \text{kg}$$

which is 16.5 percent of the whole empty vehicle. A stiffened design carrying the same compression without pressure needs frames and stringers, conventionally adding forty to sixty percent above bare skin, which would take the tank alone to between 1250 and 1430 kilogrammes. **That increment is real but it is not by itself the factor of one and a half the range table above uses**, and the article does not claim it is. The sensitivity table is a sensitivity table. What the comparison does establish is the direction and the order, and the direction is the one the programme chose.

The general form of the comparison is worth writing down because it shows where the advantage comes from. A pressure-stabilised wall is sized by tension,

$$t_{\text{press}} = \frac{p r}{\sigma_{\text{allow,tension}}}$$

and a stiffened wall carrying the same vehicle is sized by an equivalent compressive allowable that includes its stiffening,

$$t_{\text{stiff}} = \frac{N_{x}}{\sigma_{\text{allow,compression}}}$$

so the ratio of the two depends on the ratio of the allowables, which for this material and this radius-to-thickness ratio is

$$\frac{\sigma_{\text{tension}}}{\sigma_{\text{compression}}} = \frac{965}{14.4} = 67$$

**The tensile allowable is sixty-seven times the compressive one.** That factor does not translate directly into a mass ratio, because the two walls carry different loads and the stiffened one adds material in a different place, but it is the reason the comparison comes out the way it does and it is the number a designer in 1951 would have been looking at. Stiffened-shell optimisation as the period practised it appears in [Nickell 1961][research_nickell_1961] and [Nott 1963][research_nott_1963], the structural design practice belongs to [Bruhn 1973 Analysis and Design of Flight Vehicle Structures][book_bruhn_1973], and the material behaviour that fixes the tensile allowable comes from [Manning and Price 1961][research_manning_price_1961], [Johnson and Kelsen 1969][research_johnson_kelsen_1969], and [Kuentz 1969][research_kuentz_1969].

## Dependent Systems

### The Engines, and Why Three of Them Start on the Ground

The Atlas A carried two booster engines developing 341,128 pounds of thrust between them, which is 1.517 meganewtons. At the Atlas gross mass this is a lift-off thrust-to-weight of

$$\frac{T}{W} = \frac{1.517 \times 10^{6}}{117{,}900 \times 9.80665} = 1.31$$

and the propellant flow follows from the exhaust velocity,

$$\dot{m} = \frac{T}{v_{e}} = \frac{1.517 \times 10^{6}}{2765} = 549 \, \text{kg/s}$$

so a 133 second burn consumes 73.0 tonnes, which is 65 percent of the full Atlas propellant load. Liquid engine practice of the period runs from [Summerfield 1960][research_summerfield_1960], with a released Rocketdyne specification of the same line in [Scott 1963][research_scott_1963] and the specific-impulse bookkeeping in [Dafler 1962][research_dafler_1962]. Combustion instability, which was the era's most persistent liquid-engine problem, is [Grey 1953][research_grey_1953], [Matthews 1957][research_matthews_1957], and [Harrje 1959][research_harrje_1959]. [Hegg 1964][research_hegg_1964] designs the gimbal actuation for thrust vector control, and the turbopump that feeds the whole arrangement has its own design-criteria treatment in [NACA 1975][research_naca_1975], with propellant flow calibration in [Berg 1968][research_berg_1968].

### Ascent Loads, and the Worst Two Minutes

The structural case is set by the ascent, and within the ascent by two moments. Dynamic pressure rises as the vehicle accelerates and falls as the atmosphere thins, so it peaks,

$$q = \tfrac{1}{2} \rho(h) v(h)^{2}$$

and for a vertically rising vehicle the peak can be located by differentiating. With an exponential atmosphere of scale height $H$ and a constant acceleration $a$, the dynamic pressure is

$$q(t) = \tfrac{1}{2} \rho_{0} e^{-a t^{2} / (2H)} (a t)^{2}$$

and setting the derivative to zero gives

$$\frac{dq}{dt} = 0 \quad \Longrightarrow \quad t_{q} = \sqrt{\frac{2H}{a}}$$

For a scale height of 7200 metres and an acceleration of three metres per second squared net of gravity,

$$t_{q} = \sqrt{\frac{2 \times 7200}{3}} = 69 \, \text{s}$$

at an altitude of $\tfrac{1}{2} a t_{q}^{2} = H = 7.2$ kilometres, which is the pleasing result that **a constant-acceleration vertical ascent reaches maximum dynamic pressure at exactly one scale height**, independent of the acceleration. The value at that point follows by substitution,

$$q_{\max} = \tfrac{1}{2} \rho_{0} e^{-1} (a t_{q})^{2} = \tfrac{1}{2} \rho_{0} e^{-1} \times 2 a H$$

which for the same numbers gives

$$q_{\max} = \tfrac{1}{2} \times 1.225 \times 0.3679 \times 2 \times 3 \times 7200 = 9736 \, \text{Pa}$$

or about 1.4 pounds per square inch of dynamic pressure. **The aerodynamic pressure the vehicle must survive is two percent of the pressure it carries internally**, which is the clearest possible statement of where this structure's loads actually come from. It is a pressure vessel that happens to fly, not an aeroplane that happens to hold propellant. The real trajectory is not vertical and the acceleration is not constant, so the actual figure is nearer eleven kilometres and a little over a minute, but the structure of the answer is the structure of the real one. Axial acceleration does the opposite. It grows monotonically as propellant burns away,

$$n(t) = \frac{T}{\left( m_{0} - \dot{m} t \right) g}$$

so at lift-off it is 1.31 and near booster cutoff, with two thirds of the propellant gone, it approaches

$$n = \frac{1.517 \times 10^{6}}{\left( 117{,}900 - 72{,}977 \right) \times 9.80665} = 3.44$$

**The worst bending load and the worst axial load therefore arrive at different times**, which is fortunate, because a pressure-stabilised structure that had to carry both at once would need a pressure it could not contain. Ascent load analysis of the period begins with [Wood 1961][research_wood_1961], with the aerodynamic side in [Binion et al 1962][research_binion_1962].

**The load case that is easiest to forget is the one before the engines light.** A slender missile standing on a pad sheds vortices in a steady wind and can be driven into resonant transverse oscillation, and for a pressure-stabilised vehicle the pressure that resists it is the standing five pounds rather than the flight sixty. The period treated this as a subject in its own right, in [Bohne 1964][research_bohne_1964] and [Buell 1964][research_buell_1964] on the sources of ground-wind loads, [Simon 1965][research_simon_1965] on the flow-field parameters that govern the oscillation, [Jones and Farmer 1966][research_jones_farmer_1966] and [Jones and Farmer 1967][research_jones_farmer_1967] on wind-tunnel studies of the Saturn vehicles, [Coffin 1970][research_coffin_1970] on simulating the response, and the extreme-value statistics that decide what wind to design against in [Miller 1967][research_miller_1967]. A whole meeting was devoted to it, reported in [NACA 1966][research_naca_1966]. **The axial equivalent, in which an elastically supported vehicle oscillates along its own axis on the pad, is [Radovcich 1965][research_radovcich_1965].**

Angle of attack is what turns dynamic pressure into a bending moment. The normal force on a slender body at small incidence is

$$N = q S C_{N\alpha} \alpha$$

and taking the reference area as the cross-section, $S = \pi r^{2} = 7.30$ square metres, a normal-force slope of two per radian, and three degrees of incidence at maximum dynamic pressure,

$$N = 9736 \times 7.30 \times 2 \times 0.0524 = 7447 \, \text{N}$$

which acting at a lever arm of ten metres gives a bending moment of 74 kilonewton metres. Against the pressure-stabilised capacity of 2.30 meganewton metres at flight pressure this is **three percent**, so there is an enormous margin in bending while pressurised and essentially none while not. The incidence comes from wind. A vehicle rising through a shear layer sees a lateral relative wind and must either fly at an angle to it, which costs bending moment, or steer into it, which costs trajectory. That trade is the reason load-relief steering exists and it is treated below in its modern form.

### The Sustainer, and What Staging Actually Buys

Dropping two engines and a skirt at booster cutoff removes mass that the remaining propellant would otherwise have to accelerate. The benefit is the difference between finishing the burn with and without that mass,

$$\Delta v_{\text{gain}} = v_{e} \left[ \ln \frac{m_{1}}{m_{f}} - \ln \frac{m_{1} + m_{j}}{m_{f} + m_{j}} \right]$$

where $m_j$ is the jettisoned mass and $m_1$ is the mass at staging. That expression is worth evaluating rather than describing, and evaluating it overturns the obvious reading.

The booster phase consumes $\dot{m} t_b = 549 \times 133 = 72{,}977$ kilogrammes, leaving

$$m_{\text{sust}} = m_{p} - \dot{m} t_{b} = 112{,}505 - 72{,}977 = 39{,}528 \, \text{kg}$$

for the sustainer, so the mass at staging after jettison is $m_1 = 5395 + 39{,}528 = 44{,}923$ kilogrammes. Taking a jettisoned booster package of three tonnes, the sustainer phase delivers

$$\Delta v_{\text{dropped}} = 2765 \ln \frac{44{,}923}{5395} = 5861 \, \text{m/s}$$

if the package is discarded and

$$\Delta v_{\text{carried}} = 2765 \ln \frac{47{,}923}{8395} = 4817 \, \text{m/s}$$

if it is not, so the gain is

$$\Delta v_{\text{gain}} = 5861 - 4817 = 1044 \, \text{m/s}$$

**That is twelve percent of the whole ideal velocity for the sake of dropping three tonnes of engine.** The intuition that a half-stage gives up most of the benefit of staging is wrong, and it is wrong because the benefit of staging depends on the ratio of jettisoned mass to burnout mass rather than to gross mass. Three tonnes against a burnout mass of five and a half is an enormous fraction, even though it is under three percent of the vehicle at lift-off.

**The one-and-a-half stage arrangement therefore captures most of the value of staging while avoiding an altitude ignition**, which is a considerably better bargain than it looks, and the balloon tank is what makes the burnout mass small enough for the bargain to be that good. The two decisions reinforce each other rather than trading against each other. Staging optimisation of the period is [Schurmann 1957][research_schurmann_1957] and [Parkyn 1958][research_parkyn_1958], and the separation event itself, which imposes its own aerodynamic and jet-interference loads, is [Binion et al 1962][research_binion_1962] and [Binion 1964][research_binion_w_1964].

### Structural Proof Testing, Which This Design Makes Unusually Easy

A stiffened shell fails by buckling under compression, and applying a representative compressive load to a twenty-three metre cylinder requires a test rig comparable in size and cost to the article. A pressure-stabilised tank fails by yielding under tension, and applying a representative tensile load requires a compressor. **Every tank can therefore be proof-tested to a defined fraction of its own failure mode before it ever flies**, which is not true of the alternative.

The proof factor relates the test pressure to the design pressure,

$$k_{p} = \frac{p_{\text{proof}}}{p_{\text{design}}}$$

and a factor between 1.1 and 1.25 is conventional for a pressure vessel that will be reused, with the burst factor higher still,

$$k_{b} = \frac{p_{\text{burst}}}{p_{\text{design}}} \geq 1.5$$

which at the flight pressure and heavy gauge implies a burst hoop stress of

$$\sigma_{\text{burst}} = 1.5 \times 671 = 1007 \, \text{MPa}$$

against an assumed ultimate of 1276, a margin of 1.27 on the material rather than on the design. Applying a proof factor of 1.25 to the 60 pound flight pressure gives a hoop stress at the heavy gauge of

$$\sigma_{\theta} = 1.25 \times 671 = 839 \, \text{MPa}$$

which is 87 percent of the assumed yield, so the proof test is a genuine test and not a formality. [Abraham 1963][research_abraham_1963] shows how the period tested large articles structurally, with the combined static and dynamic loading problem in [Roberts and Wilhem 1964][research_roberts_wilhem_1964]. **The design's failure mode is its own acceptance test**, and that is a real and rarely stated advantage of the balloon tank over a stiffened shell whose critical load can only be estimated.

### The Thermal Environment, Which Is Mild by the Standards of This Series

The [X-10][related_post_a307_north_american_x10] article computed a recovery temperature of 636 kelvin for a vehicle cruising at Mach 3.25 for three hours, and concluded that aluminium would not serve. A ballistic booster has the opposite problem. It passes through the dense atmosphere quickly and is out of it before the skin can equilibrate,

$$\tau_{\text{skin}} = \frac{\rho c \delta}{h}$$

and for stainless steel at the Atlas gauge, taking a density of 8000 kilogrammes per cubic metre, a specific heat of 500 joules per kilogramme kelvin, and a convective coefficient of 200 watts per square metre kelvin,

$$\tau_{\text{skin}} = \frac{8000 \times 500 \times 0.00094}{200} = 18.8 \, \text{s}$$

which is comparable to the time spent near maximum dynamic pressure rather than short against it. **The skin does partially equilibrate, but it does so against a recovery temperature that is only high for a few tens of seconds**, and the propellant behind it is a very large heat sink at cryogenic temperature. The structural problem is therefore mechanical rather than thermal, which is the reverse of every vehicle in this series since the [X-2][related_post_a299_bell_x2]. Aerodynamic heating of entry vehicles runs through [Allen 1966][research_allen_1966] and [Murphy and Rubesin 1965][research_murphy_rubesin_1965], and [Winstead 1966][research_winstead_1966] handles the thermal control of a cryogenic vehicle, with propellant leakage effects in [Nast and Williams 1967][research_nast_williams_1967].

### The Acoustic and Vibration Environment

A rocket at lift-off sits in its own exhaust noise, and the overall sound pressure level near the base of a large booster reaches values that damage thin panels by fatigue rather than by static overload. The relation that governs the damage is not a stress but a spectrum, and the accumulated damage over an exposure follows a cycle count rather than a peak. **A thin welded shell is the structure most exposed to that mechanism**, and the weld lines are where it acts.

The level can be estimated. The mechanical power in the jet is

$$P_{\text{jet}} = \tfrac{1}{2} \dot{m} v_{e}^{2} = \tfrac{1}{2} \times 549 \times 2765^{2} = 2.10 \, \text{GW}$$

of which rocket exhausts convert something near half of one percent into sound, so the radiated acoustic power is about 10.5 megawatts. Spreading that over a hemisphere at thirty metres gives an intensity of

$$I = \frac{P_{\text{ac}}}{2 \pi d^{2}} = \frac{1.05 \times 10^{7}}{2 \pi \times 900} = 1855 \, \text{W/m}^{2}$$

and a sound pressure level of

$$L_{p} = 10 \log_{10} \frac{I}{10^{-12}} = 153 \, \text{dB}$$

falling to 142 decibels at a hundred metres. The pressure fluctuation follows from the intensity directly, which avoids rounding the level,

$$p_{\text{rms}} = \sqrt{I \rho c} = \sqrt{1855 \times 1.225 \times 343} = 883 \, \text{Pa}$$

so **a hundred and fifty-three decibels is a pressure fluctuation of about 0.13 pounds per square inch**, which is small against the sixty inside the tank but is applied at hundreds of hertz for the duration of the lift-off transient, and fatigue does not care about the mean. The mechanism has its own period discipline under the name sonic fatigue. [Vreeland 1960][research_vreeland_1960] gives a test method, [Wang 1966][research_wang_1966] a prediction model, [Ballentine et al 1966][research_ballentine_1966] the combined-environment case, and [Hines 1966][research_hines_1966] the specimen fabrication such tests require. The statistical machinery it rests on comes from [Crandall and Mark 1963][research_crandall_mark_1963], with transmission in [Crandall and Mark 1963, Transmission of Random Vibration][research_crandall_mark_1963_2] and failure in [Crandall and Mark 1963, Failure Due to Random Vibration][research_crandall_mark_1963_3]. [Boyd 1963][research_boyd_1963] measured the environment at the launch site itself for Cape Canaveral, with facility acoustics in [Tyzzer and Pernet 1964][research_tyzzer_pernet_1964], the launch-vehicle dynamics overview in [Hung and Hunt 1964][research_hung_hunt_1964], and vibration environment specification and correlation in [Snyder et al 1974][research_snyder_1974], with the acoustic measurement practice of the period in [Keast 1961][research_keast_1961].

### Slosh, Which a Balloon Tank Makes Worse

A tank with no internal structure has nothing to break up the free surface of its propellant, and a large moving mass of liquid inside a vehicle being steered by thrust vectoring couples into the control loop. **The same decision that removed the stringers removed the natural baffling**, so baffles had to be added back deliberately as the one internal structure the design admits.

The frequency that matters is the first lateral sloshing mode of a cylindrical tank, which for fill depths that are not shallow is

$$\omega_{s} = \sqrt{\frac{1.841 \, g_{\text{eff}}}{r} \tanh \frac{1.841 h}{r}}$$

and under acceleration the effective gravity is the axial load factor times $g$, so **the slosh frequency rises through the flight as the vehicle accelerates and falls as the tank drains**. At the Atlas radius and a load factor of three the deep-tank limit gives

$$\omega_{s} = \sqrt{\frac{1.841 \times 3 \times 9.80665}{1.524}} = 5.96 \, \text{rad/s}$$

or 0.95 hertz, which sits uncomfortably close to the bandwidth of a thrust-vector control loop. [Stephens 1965][research_stephens_1965] damps slosh with flexible baffles, with measurement in [Wilner et al 1960][research_wilner_1960] and the shell-vibration side in [DIGiovanii and Dugundji 1965][research_digiovanii_dugundji_1965].

### Pogo, Which Is the Structure and the Propulsion Talking to Each Other

A liquid rocket whose structure has a longitudinal mode near the frequency at which its feed system and engine respond can close a loop through the propellant column, and the vehicle oscillates along its own axis. [Rubin 1965][research_rubin_1965] and [Rubin 1966][research_rubin_1966] set out the mechanism, the naming and early study are [Goldman and Miessner 1965][research_goldman_miessner_1965] and [Goldman and Miessner 1966][research_goldman_miessner_1966], [Marcus et al 1969][research_marcus_1969] develops the accumulator remedy, and the best-known case is [Hill et al 1969][research_hill_1969] on Saturn V. **A pressure-stabilised vehicle is unusually exposed to this**, because its longitudinal stiffness is partly a function of tank pressure and therefore changes as the tanks drain.

The scale of the problem is set by how soft the vehicle is. A solid steel bar of the same length has a fixed-free axial mode at

$$f_{1} = \frac{c}{4L} = \frac{1}{4L} \sqrt{\frac{E}{\rho}} = \frac{4912}{4 \times 23.11} = 53 \, \text{Hz}$$

but a launch vehicle is not a solid bar. It is a thin shell containing a large mass of liquid, and its first axial mode sits an order of magnitude lower, in the region of twenty hertz, which is uncomfortably close to the response of a feed system and turbopump. **The instability condition is that the structural mode and the propulsion response overlap in frequency with enough gain around the loop**, and both quantities move during the flight, the structure because the tanks drain and the propulsion because the inlet pressure falls. Missile structural dynamics of the period runs through [Wood 1961][research_wood_1961], with clustered-vehicle bending in [Loewy 1965][research_loewy_1965], shell vibration in [DIGiovanii and Dugundji 1965][research_digiovanii_dugundji_1965], the ribbed-shell stability case in [Amiro 1962][research_amiro_1962], and the launch-vehicle overview in [Gerald and Runyan 1962][research_gerald_runyan_1962].

### Guidance, Which the Atlas A Did Not Carry

The Atlas A flew without an operational guidance system. Its flights were programmed, and the guidance question belonged to later variants and to the radio-inertial system the early Atlas used before an all-inertial set replaced it. Ballistic missile guidance of the period spans [Whitcombe 1961][research_whitcombe_1961], [Slifka 1960][research_slifka_1960] field-tests such a system, the measurement problem of establishing where a missile actually went is [Cooper 1961][research_cooper_1961], the explicit guidance equations that a self-contained system must solve are [MacPherson 1963][research_macpherson_1963], and a later integrated formulation is [Russell 1964][research_russell_1964] with [Larson 1965][research_larson_1965] on Titan III and cost-driven inertial development in [Crose 1965][research_crose_1965]. The simulation apparatus such work depends on is [Juarez 1961][research_juarez_1961].

**The accuracy relation is worth stating even though the X-11 did not exercise it**, because it explains why a ballistic weapon is a velocity-control problem rather than a navigation problem, and because it can be derived from the range relation the previous article established rather than asserted.

That relation gives the range angle through

$$\sin \frac{\Phi}{2} = \frac{\lambda}{2 - \lambda}, \qquad \lambda = \frac{v^{2}}{g R_{e}}, \qquad R = R_{e} \Phi$$

and the sensitivity of range to burnout speed follows by chaining the three derivatives. From the definition of $\lambda$,

$$\frac{d \lambda}{\lambda} = 2 \frac{dv}{v}$$

from the range-angle relation,

$$\frac{d}{d\lambda} \sin \frac{\Phi}{2} = \frac{2}{(2 - \lambda)^{2}} \quad \Longrightarrow \quad \frac{d\Phi}{d\lambda} = \frac{4}{(2-\lambda)^{2} \cos (\Phi/2)}$$

and combining them gives the logarithmic sensitivity

$$\frac{\partial \ln R}{\partial \ln v} = \frac{2 \lambda}{\Phi} \cdot \frac{4}{(2 - \lambda)^{2} \cos (\Phi/2)}$$

At the intercontinental condition of $\lambda = 0.828$ and $\Phi = 1.570$ radians this evaluates to

$$\frac{\partial \ln R}{\partial \ln v} = 4.34$$

**One part in a thousand of velocity error is therefore about four and a third parts in a thousand of range**, or forty-three kilometres at ten thousand. A weapon required to land within eight hundred metres, which is the figure the previous article inverted for the Navaho, needs a velocity accuracy of

$$\frac{\delta v}{v} = \frac{1}{4.34} \times \frac{800}{10^{7}} = 1.84 \times 10^{-5}$$

or **0.13 metres per second out of 7193**. Cutting the engines at the right instant to a tenth of a metre per second is the whole of the ballistic accuracy problem, and it is a problem that lasts for the two minutes of powered flight rather than for the thirty-two of the trajectory. That is why the previous article's vehicle needed a navigator and this one needs a clock, and it is the sharpest single difference between the two weapons.

### The Reentry Vehicle, Which Is Not the Missile

Everything above concerns a vehicle whose job ends at burnout. What arrives at the target is a separate body that must survive a reentry the booster never experiences, and the Atlas A carried no operational reentry vehicle at all.

The governing result is worth stating because it is unusually clean. For a ballistic body entering an exponential atmosphere on a straight path, the peak deceleration is

$$a_{\max} = \frac{v_{e}^{2} \sin \gamma}{2 e H}$$

where $\gamma$ is the entry flight path angle and $H$ the scale height, and the striking feature is that **the ballistic coefficient does not appear**. A heavy dense body and a light one decelerate equally hard, and differ only in the altitude at which they do it. For an entry speed of seven kilometres per second at thirty degrees,

$$a_{\max} = \frac{7000^{2} \times 0.5}{2 \times 2.718 \times 7200} = 626 \, \text{m/s}^{2} = 64 g$$

The result is period material and not a later reconstruction. [Scherberg and Rubin 1953][research_scherberg_rubin_1953] computes the decelerations of a ballistic missile on reentry in exactly this form, four years before the X-11 flew, and the closed-form lifting extension is [Bell 1965][research_bell_1965]. The motion of the body about its own axes while this is happening is [Murphy 1961][research_murphy_1961], the char-layer response of the heat shield is [Dolton and Reed 1966][research_dolton_reed_1966], and estimating where such a body actually is while it flies is [Schweppe 1964][research_schweppe_1964]. The defensive problem this creates, which the [previous article][related_post_a307_north_american_x10] found revived in the modern glide-vehicle literature, was already being posed in the period by [Faulkner 1961][research_faulkner_1961] and [Faulkner and Ward 1961][research_faulkner_ward_1961].

**The reentry body is decelerated at sixty-four times gravity while the booster that launched it never exceeded three and a half.** The two halves of a ballistic missile are different structural problems by a factor of nearly twenty, which is the reason they are different articles built by different people, and the reason the X-11 could be a complete test of one while carrying none of the other. Nose-cone and ablation work of the period covers [Stetson 1964][research_stetson_1964], [Wachi and Gilmartin 1966][research_wachi_gilmartin_1966], and [Rindal and Dahm 1967][research_rindal_dahm_1967], with hemispherical-nose heat transfer in [Nardo and Sadler 1962][research_nardo_sadler_1962], flight heating measurements in [Snodgrass 1955][research_snodgrass_1955], and the roll-resonance problem in [Platus 1967][research_platus_1967].

### Ground Handling, Which the Structure Dictates

A structure that collapses unpressurised cannot be handled like an aeroplane. It requires a nitrogen supply at every point in its life, transport fixtures that support it without imposing a bending moment above the pressure-stabilised limit computed above, and a launch complex that keeps it inflated while it is fuelled. **The structural decision propagates into buildings and vehicles and procedures**, and the accessible record of that apparatus is unusually good, in [General Dynamics San Diego Ca Convair Div 1966][research_div_1966] and its companion volumes and in [Peters and Hall 1963][research_peters_hall_1963] on system-test data for the engine system.

The propellant loading problem deserves its own note, because a balloon tank couples loading to structure in a way a conventional tank does not. Filling the tank changes the pressure the walls must hold, changes the mass the walls must carry, and changes the temperature of the material, and all three happen while it stands unsupported on a pad. **Loading is a structural operation and not merely a fluid transfer.** [Whitcombe 1961, Optimum Propellant Loading And Pro][research_whitcombe_1961_2] optimises propellant loading and utilisation, and ground support equipment practice of the period runs from [Moore 1958][research_moore_1958] and [Newton and Makrides 1954][research_newton_makrides_1954], with launch complex activation in [Powell 1962][research_powell_1962].

The boil-off that follows is a second coupling, and its rate explains why topping continues until moments before launch. With a wetted area of

$$A = 2 \pi r L = 2 \pi \times 1.524 \times 18 = 172 \, \text{m}^{2}$$

an uninsulated tank at a convective coefficient of ten watts per square metre kelvin against a two hundred kelvin difference admits

$$\dot{Q} = h A \Delta T = 10 \times 172 \times 200 = 345 \, \text{kW}$$

and at a latent heat of 213 kilojoules per kilogramme the boil-off is

$$\dot{m}_{\text{boil}} = \frac{\dot{Q}}{L_{v}} = \frac{3.45 \times 10^{5}}{2.13 \times 10^{5}} = 1.62 \, \text{kg/s}$$

or 5826 kilogrammes an hour, which is **seven and a half percent of the oxygen load every hour**. Liquid oxygen at 90 kelvin against an ambient near 290 therefore boils continuously, the tank must be topped until moments before launch, and the ullage pressure must be regulated throughout. The insulation that reduces the rate appears in [Weiss and Goodman 1960][research_weiss_goodman_1960] and [Walton and Simmons 1962][research_walton_simmons_1962], and the conditioning of the propellant before launch is [Greenfield 1960][research_greenfield_1960]. A pressure regulation failure is a structural failure on this vehicle rather than a propulsion inconvenience, which is the recurring theme of the whole design. [Slider 1967][research_slider_1967] analyses pressure buildup in a cryogenic tank, and two-phase pumping of cryogenic propellants is [Stinson and Gross 1972][research_stinson_gross_1972].

## The Flight Test Record

Eight Atlas A vehicles flew from Cape Canaveral between 11 June 1957 and 3 June 1958, four successfully. All flights were from Launch Complex 12 or 14, and all were short-range, reaching apogees near 120 kilometres.

| Date | Serial | Apogee | Outcome |
|------|--------|--------|---------|
| 1957-06-11 | 4A | 2 km | failure |
| 1957-09-25 | 6A | 3 km | failure |
| 1957-12-17 | 12A | 120 km | success |
| 1958-01-10 | 10A | 120 km | success |
| 1958-02-07 | 13A | 120 km | failure |
| 1958-02-20 | 11A | 90 km | failure |
| 1958-04-05 | 15A | 100 km | failure |
| 1958-06-03 | 16A | 120 km | success |

The first flight reached two kilometres and was destroyed, and the reported detail that matters for this article is that **the vehicle tumbled and the structure held**. A pressure-stabilised shell that survives a tumble at low altitude has demonstrated the one thing about it that everyone doubted, and it did so under a load case nobody designed for. A tumbling body sees its bending moment applied at an arbitrary angle and reversed once per revolution, which is the worst possible use of a structure whose compressive capacity is two hundred times smaller than its tensile one. That it held is evidence that the pressure stabilisation was working exactly as the relation above says it should, since the relation does not care about the direction of the moment. A tumbling vehicle at rotation rate $\Omega$ also loads itself centrifugally, and the transverse acceleration at the tip of a body of length $L$ rotating about its centre is

$$a_{\text{tip}} = \Omega^{2} \frac{L}{2}$$

so even a slow tumble at one revolution per second gives

$$a_{\text{tip}} = (2 \pi)^{2} \times 11.6 = 458 \, \text{m/s}^{2} = 47 g$$

at the nose, applied as a bending load along the whole vehicle. **The structure that everyone expected to fold survived a load case nobody had designed for.**

The flight-by-flight record for the operational variants is in the Flight Test Working Group reports, of which [General Dynamics/Astronautics San Diegoca 1961][research_diegoca_1961] is one, and the survival-probability analysis such a programme generates is [Beer and Lennox 1965][research_beer_lennox_1965].

### What the Eight Flights Were Actually For

It is worth separating what the programme intended each flight to establish from what the flight record shows, because the two are not the same and the difference explains the apparent poor showing.

The first two flights, in June and September 1957, reached two and three kilometres. Neither was a performance flight in any sense. They were attempts to get a vehicle off the pad and through the first seconds of powered flight, and the first of them delivered the single most important structural result of the programme by tumbling and holding together. **A flight that reaches two kilometres and is destroyed has still exercised the structure through lift-off, through the acoustic transient, and through an off-design load case**, and the vehicle passed all three.

The third and fourth flights, in December 1957 and January 1958, reached 120 kilometres and are recorded as successes. Those are the flights that establish the vehicle as a vehicle. The fifth, sixth, and seventh failed at 120, 90, and 100 kilometres, which is a pattern of getting most of the way and then losing something, and the reported causes are consistent with that reading. The eighth, in June 1958, succeeded.

**The programme therefore obtained its structural answer on flight one and spent the remaining seven flights on propulsion, plumbing, and pneumatics.** That ordering is the opposite of what the article's organisation implies, and it is worth stating plainly. An article built around the balloon tank naturally presents the structure as the programme's central difficulty, and the flight record says the structure was the thing that worked first and never stopped working.

The failures were concentrated in propulsion and plumbing rather than in structure. The reported causes include exhaust-gas recirculation overheating the boat-tail, propellant duct failures, and pneumatic and guidance faults, and the remedies were heat shielding, steel plumbing in place of lighter material, and revised venting. **The programme's difficulty was never the thing that looked impossible.**

### What a Fifty Percent Success Rate Means

Four of eight is a success rate of 0.5, which sounds alarming and is normal for a first flight article. What the number actually supports is narrow. Treating the flights as independent Bernoulli trials, the standard error on the estimate is

$$\sigma_{\hat{p}} = \sqrt{\frac{p(1-p)}{n}} = \sqrt{\frac{0.25}{8}} = 0.177$$

so the estimate is 0.50 plus or minus about 0.18, and any true reliability between roughly 0.15 and 0.85 is consistent with the observation. **Eight flights cannot distinguish a mediocre vehicle from a good one**, and the programme knew it, which is why Atlas B followed immediately rather than after a verdict.

It is tempting to read a learning curve into the sequence and the data do not support one. The outcomes in order were failure, failure, success, success, failure, failure, failure, success, so the first four flights produced two successes and the last four produced one. The standard error on a four-flight estimate is

$$\sigma = \sqrt{\frac{p(1-p)}{4}} = 0.25$$

which is one flight in four, so a difference of one success between the halves is exactly the size of the noise. **The programme neither demonstrably improved nor demonstrably worsened across its eight flights**, and any account that describes the record as a learning curve is reading a trend into a sequence too short to carry one.

The width of that interval is itself the argument for flying often, and the relation makes it explicit. Halving the interval requires quadrupling the flights,

$$n = \frac{p (1-p)}{\sigma_{\hat{p}}^{2}}$$

so an estimate good to five percentage points at a true reliability near one half needs

$$n = \frac{0.25}{0.05^{2}} = 100 \, \text{flights}$$

which no ballistic missile programme was ever going to fly as development articles. **Reliability for such a vehicle is therefore established by inference from ground test and by accumulating operational rounds, not by the flight test programme**, and the Difficulties Review volumes of [General Dynamics San Diego Ca Convair Div 1966][research_div_1966] are what that inference actually looks like when written down.

## Comparison With Ground Prediction

The Atlas structure was tested on the ground more thoroughly than most, because a pressure-stabilised tank can be proof-tested to its actual failure mode simply by pressurising it, which is not true of a stiffened shell whose failure mode is compressive buckling under a load that is hard to apply. **The design is unusually testable on the ground for the same reason it is unusual in flight.**

The gap between ground and flight is therefore not in the structure but in the combined environment. A tank can be pressure-tested, a shell can be buckling-tested, and neither test applies the acoustic field, the vibration, the thermal gradient, and the axial acceleration at once. [Nickell 1961][research_nickell_1961] and [Leaumont 1965][research_leaumont_1965] carry the period's shell-buckling experiment, and the standing difficulty that experiments scatter far below theory is the subject of [Karman and Tsien 1941][research_karman_tsien_1941] and remains the reason a knockdown factor exists at all.

The scatter deserves a number, because it is the largest single uncertainty in the article. Experimental buckling loads for cylinders in this range of radius to thickness fall between roughly fifteen and sixty percent of the classical value,

$$0.15 \leq \frac{\sigma_{\exp}}{\sigma_{cr}} \leq 0.60 \qquad \frac{0.60}{0.15} = 4$$

a spread of four to one, and the design factor of 0.20 used above sits at

$$\frac{0.20 - 0.15}{0.60 - 0.15} = 0.11$$

or the eleventh percentile of the observed band, which is to say very near the worst case observed. **A structure designed against a four-to-one experimental scatter is being designed against ignorance rather than against a load**, and the pressure-stabilised solution sidesteps the whole difficulty by arranging that no fibre goes into compression at all. That is the deepest sense in which the balloon tank is not merely lighter but epistemically cleaner. Its failure mode is yield, which is predictable to a few percent, rather than buckling, which is not. The standard treatments are [Timoshenko and Gere 1961 Theory of Elastic Stability][book_timoshenko_gere_1961] and [Brush and Almroth 1975 Buckling of Bars, Plates and Shells][book_brush_almroth_1975], with vehicle structural practice in [Bruhn 1973 Analysis and Design of Flight Vehicle Structures][book_bruhn_1973].

### What the Ground Could Not Reproduce

Three things about the flight environment resist ground reproduction and all three bear on this structure specifically.

**The loads arrive together.** A proof test applies pressure. A static test applies axial load. A vibration table applies acceleration. The article at maximum dynamic pressure has internal pressure, axial acceleration, a bending moment from incidence, an acoustic field, and a thermal gradient across the skin, all at once, and the interaction between them is what a combined-environment test exists to explore and what the period could rarely afford. [Roberts and Wilhem 1964][research_roberts_wilhem_1964] and [Ballentine et al 1966][research_ballentine_1966] are attempts at exactly that combination.

**The structure changes during the flight.** The tank drains, so the mass distribution, the axial stiffness, the slosh frequency, and the acceleration all move continuously through the burn. A ground test holds the article in one configuration and repeats it. **A balloon tank is the extreme case of this, because even its stiffness is a function of a state variable that is being consumed**, and no static test reproduces it.

**The failure mode of interest is statistical.** The buckling scatter of four to one is not measurement error. It is the real variation between nominally identical shells, so a single test article establishes one draw from a distribution rather than a property of the design. The article's whole argument about eight flights being too few to estimate reliability applies with equal force to shell tests, and with less excuse, because ground articles are cheaper.

## What the Data Changed

### Into Atlas, and Then Into Everything

The X-11 fed directly into the Atlas B, which is the [X-12][ref_series_close] and the next article, and thence into the operational Atlas D, E, and F. The line then did something no other early ballistic missile did. **It became a launch vehicle and stayed one for sixty years.** Atlas launched Mercury, the Agena upper stage, and a long series of planetary missions, and the balloon-tank principle carried into the Centaur upper stage, which still uses it.

The reason it could is arithmetic rather than sentiment. Circular orbital speed at two hundred kilometres is

$$v_{\text{orb}} = \sqrt{\frac{\mu}{R_{e} + h}} = \sqrt{\frac{3.986 \times 10^{14}}{6.571 \times 10^{6}}} = 7788 \, \text{m/s}$$

against the 7193 metres per second an intercontinental trajectory needs, a difference of

$$v_{\text{orb}} - v_{bo} = 595 \, \text{m/s}$$

or seven percent of the ideal velocity. **An intercontinental ballistic missile is already ninety-two percent of the way to orbit**, and the remaining eight percent is a small upper stage. That is why every early space programme was built on a ballistic missile and why none was built on a cruise missile, and it is the deepest reason the Atlas outlived the Navaho by six decades.

Trajectory [Frazier 1967][research_frazier_1967] optimises for the Atlas and Agena combination, and the control systems that a large launch vehicle of the following generation required are [Borelli and Carroll 1967][research_borelli_carroll_1967].

**The reason the Atlas became a launcher and the Navaho became nothing is worth stating in the terms this pair of articles has established.** A booster is a machine for adding velocity, and velocity is useful for any mission that needs it. A cruise missile is a machine for carrying a warhead a particular distance at a particular speed, and nothing else wants that. The Atlas survived its own obsolescence as a weapon because its keystone quantity, mass fraction, is valuable to every customer, while the Navaho's keystone quantity, sustained autonomous navigation accuracy, was valuable only to the mission that was cancelled.

### The Lineage, and What It Cost to Keep

The Atlas that launched Mercury was not the Atlas A. It was the D, with a heavier structure, a man-rating programme behind it, and an abort-sensing system the weapon never carried. The lineage nonetheless kept the balloon tank for six decades, through Atlas D, E, F, and the Atlas-Agena and Atlas-Centaur combinations, and into the Atlas II and III. It was abandoned only with the Atlas V, whose common core booster is a conventional isogrid aluminium structure and which retained the name and almost nothing else.

**The reason the tank survived so long is that a launch vehicle is judged by payload rather than by convenience**, and the balloon tank pays for itself in payload every flight. The reason it was eventually abandoned is that payload stopped being the only thing being judged.

The arithmetic of the transition is available from the relations already used. A structure heavier by the stiffening increment computed above costs, at the Atlas mass fractions, about eleven percent of range or the equivalent in payload. **Eleven percent of payload is a large penalty on a weapon and a manageable one on a commercial launcher**, because a launcher can be sized upward while a missile has to fit its basing. That single asymmetry explains the whole trajectory of the design, from indispensable in 1957 to obsolete by 2002, without any appeal to changing fashion.

Centaur is the exception that confirms it. It kept the balloon tank because an upper stage pays the mass penalty at the worst possible place in the vehicle, where every kilogramme of structure trades one-for-one against payload rather than being diluted by the stages beneath it. **The higher up a vehicle a structure sits, the more a balloon tank is worth**, which is why the idea survives in exactly the position where its disadvantages matter least and its advantages matter most.

### What It Did Not Change

The pressure-stabilised structure did not become the standard way to build launch vehicles. Almost everything since is a conventionally stiffened aluminium or composite structure, accepting a worse mass fraction in exchange for a vehicle that can be set down empty, handled without a nitrogen cart, and inspected without a pressure regime. **The Atlas won its argument and then lost it**, and the reason is that mass fraction stopped being the binding constraint once vehicles grew and staging improved, while handling cost never stopped mattering.

## The Contemporary Literature

### Shell Buckling, Where the Knockdown Factor Is Finally Being Dismantled

The design allowable used above is a blanket factor applied to a classical result, which is an admission that the theory does not predict the experiment. That has been the state of the art since [Karman and Tsien 1941][research_karman_tsien_1941] and it is now being replaced by methods that model the imperfection rather than hide behind a factor.

[Evkin 2026][research_evkin_2026] computes imperfection sensitivity rather than assuming it, [Ventura et al 2023][research_ventura_2023] takes the asymptotic numerical route to pressurised-cylinder buckling, and stochastic and dynamic treatments are [Yu et al 2024][research_yu_2024] and [Ozoigbo et al 2025][research_ozoigbo_2025], [Jiao et al 2023][research_jiao_2023] takes thin-walled behaviour under combined loading, and gauge-sensitivity methods are [Zhang 2022][research_zhang_2022]. **The most directly relevant modern paper derives knockdown factors for common-bulkhead structures**, which is this configuration exactly, in [Lee et al 2024][research_lee_2024].

The newer work goes further and tries to predict the lower bound rather than assume it. [Lin et al 2025][research_lin_2025] drives a lower-bound buckling prediction with machine learning, [Du and Groh 2026][research_du_groh_2026] predicts the buckling load from the pre-buckling stress distribution, [Porenta et al 2025][research_porenta_2025] builds a shell finite element for the purpose, [Chaabani et al 2025][research_chaabani_2025] applies high-order elements to the nonlinear problem, and post-buckling dynamics are [Yang et al 2026, Comparative Study on Post-Buckling][research_yang_2026_2] and [Peshkhoev 2026][research_peshkhoev_2026]. Grid-stiffened composite cylinders, the design the Atlas rejected, are [Velmurugan and Buragohain 2023][research_velmurugan_buragohain_2023], with multiscale buckling-aware design in [Liu et al 2026][research_liu_2026] and sandwich tubes under bending in [Ni et al 2026][research_ni_2026].

**The direction of travel is worth naming.** A knockdown factor is a confession that the analyst cannot model the article in front of him. Every one of these papers is an attempt to withdraw the confession, and the Atlas is the vehicle that avoided needing it by arranging that no fibre goes into compression at all.

### Shell Analysis Itself, Which Is No Longer Done by Hand

The relations this article uses are closed-form membrane and buckling results because those are what the period had and what a reader can check. Modern shell analysis is numerical, and the specific problem the article poses has been solved properly. Static bending of a pressurised cylindrical shell, which is the exact configuration of the keystone derivation, is [Samadzadeh et al 2024][research_samadzadeh_2024]. [Yu 2026][research_yu_2026] takes the externally pressurised case, [Jin 2025][research_jin_2025] puts internal pressure on a non-circular shell, geometrically nonlinear formulations are [Azizi and Dornisch 2025][research_azizi_dornisch_2025] and [Chaabani et al 2025][research_chaabani_2025], and a launch-vehicle-like article is analysed and tested in [Tillotson Rudd et al 2024][research_rudd_2024].

**The probabilistic turn is the important one.** [Sadovský et al 2024][research_sadovsky_2024] identifies buckling resistance as a distribution rather than a value, which is what a knockdown factor was always crudely approximating. A design factor of 0.2 is a one-number summary of a probability distribution nobody could compute in 1951 and everybody can compute now.

### Inflatable and Pressure-Stabilised Structure, Which Came Back Under Another Name

The relation derived above, that a pressurised cylinder resists bending until the compressive stress from the moment overcomes the tensile stress from pressure, is the governing relation of a field that is now called inflatable structures rather than pressure-stabilised ones.

Inflatable tube bending is modelled and validated experimentally in [Gong et al 2026][research_gong_2026], [Ge et al 2026][research_ge_2026], and [Zhang et al 2025, Bending test and numerical analysi][research_zhang_2025_5], which measure exactly the quantity computed above. Wrinkling, which is what the failure looks like when the pressure loses, is [Wang et al 2026][research_wang_2026] under bending and torsion and [Gashe et al 2025][research_gashe_2025] under shear and compression. Tapered inflatable lattices are [Kundu and Mukhopadhyay 2025][research_kundu_mukhopadhyay_2025], deployable reflector application is [Im et al 2025][research_im_2025], precision analysis is [Hu et al 2025][research_hu_2025], and habitat use is [Kömle et al 2025][research_komle_2025].

**Bossart's idea did not die. It moved to spacecraft that must be small when launched and large when deployed**, where the mass argument is even stronger than it was for the Atlas, and the analysis those programmes use is the analysis this article performs.

### Propellant Tanks, Where the Rocket Equation Has Not Changed

Tank structure remains where launch-vehicle mass is won and lost, and the modern literature is dominated by cryogenics because the propellants moved. [Kim et al 2025][research_kim_2025] optimises a launch vehicle tank structurally, the common-bulkhead arrangement the Atlas pioneered appears in [Zhang et al 2025, Improving storage performance of a][research_zhang_2025_2] and [Zhang et al 2025, Feasibility study on synthermal st][research_zhang_2025_3], [Narayana Yenugula et al 2025][research_yenugula_2025] adds vacuum insulation to a thermo-structural analysis, all-composite cryogenic tanks are [Rhee et al 2025][research_rhee_2025], [Cheng et al 2025][research_cheng_2025] couples the analysis concurrently, [Bershadskyi et al 2022][research_bershadskyi_2022] verifies a tank operational-pressure model, and two-way fluid-structure and thermal-structure interaction appears in [Ajeesh et al 2026][research_ajeesh_2026].

The boil-off computed above at seven and a half percent of the oxygen load per hour is now attacked directly. [Zhang et al 2025, Multi-objective optimization of cr][research_zhang_2025_7] optimises for zero boil-off, boil-off gas reduction appears in [Nikonchuk 2026][research_nikonchuk_2026] and [Lu et al 2026][research_lu_2026], double-shell vacuum insulation behaviour is [Lee et al 2026, Boil-Off Rate Behavior in a Double][research_lee_2026_2], [Zhang et al 2026][research_zhang_2026] and [Yu et al 2026, Design and evaluation of thermal i][research_yu_2026_2] take insulation heat and mass transfer, [Leng et al 2026][research_leng_2026] compares thermodynamic performance, and the whole thermal-fluid management problem belongs to [Chung 2026][research_chung_2026].

**The Atlas topped its tanks until moments before launch because it had no alternative.** A modern cryogenic stage intended to loiter in orbit cannot do that, which is why zero-boil-off is a research programme rather than a convenience.

### Sloshing, Which the Balloon Tank Made Worse and Which Is Still Being Baffled

A tank with no internal structure has nothing to break the free surface, and the modern literature is still largely about where to put the baffles. [Liu et al 2025][research_liu_2025] varies vertical baffle height, annular perforated baffles are [Lu and Cao 2026][research_lu_cao_2026], and three-dimensional resonant sloshing in a cylindrical tank appears in [Lu and Cao 2025][research_lu_cao_2025] with the wave-response comparison in [Lu and Cao 2025, Comparative study on wave response][research_lu_cao_2025_2], [Aguiar et al 2025][research_aguiar_2025] mitigates it passively, slosh effects and baffle requirements are [Solomon and Tamiru 2026][research_solomon_tamiru_2026] and [Pei 2021][research_pei_2021], [Jeon et al 2024][research_jeon_2024] varies baffle influence, and the coupling into vehicle dynamics appears in [Xu and Xu 2024][research_xu_xu_2024] and [Roithmayr and Pei 2024][research_roithmayr_pei_2024] on touchdown stability.

**One modern paper is a direct descendant.** [Lee and Baek 2026][research_lee_baek_2026] analyses the vibration of a redesigned stainless-steel propellant tank on a current launch vehicle, which is the same material, the same structural philosophy, and the same coupling problem the Atlas met seventy years earlier.

### Pogo, Which Is Still an Active Design Problem

[Zhao and Tan 2026][research_zhao_tan_2026] reduces the model for suppression design, [Zhao et al 2024][research_zhao_2024] and [Tan et al 2023][research_tan_2023] suppress it actively, [Dolgopolov and Nikolayev 2024][research_dolgopolov_nikolayev_2024] models it nonlinearly, and suppressor hardware appears in [Yoon et al 2021][research_yoon_2021] and [Mitra et al 2021][research_mitra_2021], the strap-on configuration is [Liu et al 2020][research_liu_2020], and stability analysis is [Raji et al 2019][research_raji_2019]. **That an instability first met on 1960s vehicles still supports an active design literature is a measure of how tightly propulsion and structure couple in a thin-walled liquid rocket**, and a pressure-stabilised vehicle is the extreme case because its axial stiffness is partly pressure.

### Ground Wind and Buffet, the Load Case the Draft Omitted

The primary pass established that a slender vehicle on a pad can be driven into resonance by vortex shedding, and that for this vehicle the resisting pressure is the standing five pounds rather than the flight sixty. That subject is now general structural dynamics rather than a launch-vehicle speciality. [Sahu et al 2024][research_sahu_2024] takes vortex-induced vibration of a circular cylinder in the supercritical regime, which is the regime a vehicle of this diameter stands in, [Zhang et al 2024, Fluid-structure interaction analys][research_zhang_2024_4] and [Vîlceanu et al 2024][research_vilceanu_2024] couple fluid to structure, and damper effectiveness appears in [Wang et al 2024, Numerical study on the effectivene][research_wang_2024_2], and ground-mounted validation is [Eshete et al 2024][research_eshete_2024].

The ascent equivalent is transonic buffet, which is [Polivanov and Sidorenko 2026][research_polivanov_sidorenko_2026] on the oscillation modes, [Lei et al 2025][research_lei_2025] and [Gong et al 2024][research_gong_2024] on control and suppression, [Zahn et al 2025][research_zahn_2025] on learned prediction, and [Singh et al 2026][research_singh_2026] on active control over a payload fairing. Load alleviation, which is the modern answer to designing for the worst wind, is [Tantaroudas and Karachalios 2026][research_tantaroudas_karachalios_2026], [Rieck et al 2026][research_rieck_2026], and [Gao et al 2024][research_gao_2024].

### Acoustics and Sonic Fatigue

The 153 decibels computed above is a fatigue problem rather than a strength problem, and the modern treatment is statistical. [Qiu et al 2026][research_qiu_2026] gives a damage-equivalent stress amplitude under random loading, [Zhang et al 2026, Fatigue life and failure location][research_zhang_2026_2] predicts fatigue life and failure location, [Pan et al 2026][research_pan_2026] grows cracks under variable amplitude, [Reddy et al 2026][research_reddy_2026] tests a functional article vibro-acoustically, and thermo-vibro-acoustic analysis with structural mitigation appears in [Abhishek Hari, 2026][research_abhishek_hari_2026], suppression on a corrugated structure is [Zhou et al 2025, Vibro-acoustic analysis and suppre][research_zhou_2025_2], and acoustic resonance in an aerospace duct is [Wang et al 2026, Experimental investigation of acou][research_wang_2026_2].

### Flaws, Fracture, and What a Proof Test Actually Proves

The proof test the article describes loads the tank to a fraction of its failure stress and concludes that it will hold. What it actually establishes is that no flaw large enough to propagate at that stress is present, which is a statement about fracture mechanics rather than about strength. Modern treatment of that distinction is [Agarwal et al 2025][research_agarwal_2025] on crack analysis by extended finite elements, [Mullin et al 2025][research_mullin_2025] on critical flaw sizes and crack driving force, and [Zhao et al 2026][research_zhao_2026] on a physics-informed neural network for the same problem. Comparative small-scale test methods are [Ding et al 2025][research_ding_2025], burst testing of vessels is [Lüders et al 2025][research_luders_2025] and [Paleti et al 2026][research_paleti_2026], and weld inspection standards applied to vessels are [Dian Fitria Ramdani and Dene Herwanto 2026][research_ramdani_2026]. Sensor-based anomaly detection integrated with structural monitoring is [Zhou et al 2024][research_zhou_2024].

**On a vehicle whose wall is under a millimetre thick, a flaw that matters is smaller than an inspector can reliably see**, which is why the proof test rather than the inspection is the acceptance gate, and why the gate works.

### Modal Survey and Test Correlation, Which Is How a Structure Is Believed

The bending and axial modes of a launcher decide its control stability and its pogo margin, and those modes are measured rather than trusted. [Panda et al 2025][research_panda_2025] identifies acoustic sources on a launch vehicle, which is the modern form of the environment estimated above at 153 decibels. Low-frequency elastic mode identification belongs to [Song et al 2026][research_song_2026], and the wider identification literature that supplies the methods is [Erdogan and Tekin 2025][research_erdogan_tekin_2025], [Yang and Chen 2025][research_yang_chen_2025], and [Huang et al 2025, Modal Identification of a Wind Tur][research_huang_2025_2]. **A balloon-tank stage has to be modal-surveyed at pressure**, because its stiffness is not a property of the hardware alone, and that is a test complication the article has not otherwise mentioned.

### Launch Aerodynamics, Computed Rather Than Tunnelled

The ascent loads the article estimates from a scale height and a normal-force slope are now computed. Stage separation, which the Atlas performs uniquely by dropping engines rather than tanks, is simulated against wind-tunnel test in [Kumar et al 2023][research_kumar_2023]. Reusable vehicle aerodynamics is [Prasad 2022][research_prasad_2022], aerodynamic damping extraction is [Wang and Chen 2022][research_wang_chen_2022], turbulence-model sensitivity is [Yang et al 2022][research_yang_2022] and [Zhao et al 2022][research_zhao_2022], and interference reduction is [Liao et al 2023][research_liao_2023]. Inflatable decelerator aerodynamics, which is the pressure-stabilised structure meeting the reentry problem, is [Rioseco Olave et al 2023][research_olave_2023], [Yun and Liu 2023][research_yun_liu_2023], and [Jalaja et al 2024][research_jalaja_2024].

### Ascent Loads, Guidance, and the Trajectory

[Sun et al 2024][research_sun_2024] optimises the ascent convexly, approximate analytical solutions are [Yu et al 2023][research_yu_2023] and [Yu et al 2024, Approximate analytical solutions f][research_yu_2024_2], [He et al 2024][research_he_2024] relieves load by rolling, [Zhou et al 2025][research_zhou_2025] learns the attitude control that does it, [Jayan et al 2024][research_jayan_2024] estimates the resulting loads, computational fluid dynamics for ascent belongs to [Dalle et al 2024][research_dalle_2024] with Reynolds and aeroelastic scaling in [Ivanco et al 2024][research_ivanco_2024], chance-constrained optimisation is [Guo et al 2026][research_guo_2026], adaptive sequential convex programming is [Li et al 2024, Adaptive Sequential Convex Program][research_li_2024_3], and the thermal environment of the ascending vehicle is [Sun et al 2026][research_sun_2026]. Interstage structural design, which is the part the Atlas famously did not have, is [De Luca et al 2026][research_luca_2026].

**The engine-cutoff accuracy the article computes at 0.13 metres per second is now a solved control problem**, and the papers above solve harder versions of it while carrying loads the Atlas would not have survived.

### Engines and Health Monitoring, Which Is Where the Failures Actually Were

Four of eight Atlas A flights failed and the failures were propulsion and plumbing. That is now the most instrumented part of a launch vehicle. [Cha et al 2024][research_cha_2024] diagnoses the startup transient, [Cha and Ko 2025][research_cha_ko_2025] generalises the fault factor, [Kamenskii and Martirosov 2021][research_kamenskii_martirosov_2021] monitors current state, and the priming pressure surge belongs to [Das and Padmanabhan 2022][research_das_padmanabhan_2022], turbopump flow is [Zhou et al 2022][research_zhou_2022], thrust control is [Yao et al 2022][research_yao_2022], and thrust vector control is [Benfriha et al 2026][research_benfriha_2026] and [Saiki et al 2026][research_saiki_2026]. **The Atlas A programme diagnosed its failures by reading telemetry and inspecting wreckage. A modern vehicle carries the diagnosis aboard.**

### Reliability, Which Answers the Question Eight Flights Could Not

The binomial interval computed above is wide because eight is a small number. [Wagenblast and Bettinger 2024][research_wagenblast_bettinger_2024] estimates launch vehicle reliability statistically, [Li et al 2025, Reliability design and management][research_li_2025_2] manages it on an operational vehicle, [Muthukumar et al 2020][research_muthukumar_2020] estimates it for a control system, safety and operational reliability methodology belongs to [Khamlak 2026][research_khamlak_2026], and modern estimation methods are [Zhu 2026][research_zhu_2026] and [Almetwally et al 2026][research_almetwally_2026]. Certification by machine-learning model validation is [Neumaier et al 2025][research_neumaier_2025]. **The methods now used to certify a vehicle on a handful of flights are the methods the Atlas A programme needed and did not have.**

### Structural Health Monitoring and the Digital Twin

A stage that must be kept pressurised at all times has a structural state worth watching continuously, and that is now possible. [Louw and Kearsley 2026][research_louw_kearsley_2026] and [Chehrzad and Khoramishad 2026][research_chehrzad_khoramishad_2026] monitor large structures, [Calderon Hurtado et al 2026][research_hurtado_2026] validates the instrumentation in the field, and the digital-twin framing belongs to [Tao and Qi 2025][research_tao_qi_2025]. **Had the Atlas been built now it would have known its own pressure margin in real time**, which is the single capability that would most have changed how it was handled.

### Manufacture, Where a Thin Welded Shell Is Still Difficult

The Atlas skin is a welded stainless assembly at a gauge where welding distortion is comparable to the thickness. [Płaczek et al 2023][research_paczek_2023] and [Qiu et al 2023][research_qiu_2023] fatigue welded joints in thin-walled structure, [Zhang and He 2024][research_zhang_he_2024] treats the welds by high-frequency mechanical impact, [Edwards et al 2023][research_edwards_2023] models microstructure in duplex stainless, [Lee et al 2024][research_engineering_2024] takes springback and cold-roll forming, additive manufacture of stainless for rocket application belongs to [Thomas 2022][research_thomas_2022], hybrid additive and subtractive manufacture is [Wu et al 2026][research_wu_2026], friction stir weld heat treatment is [Ghio and Cerri 2026][research_ghio_cerri_2026], and critical flaw sizing is [Mullin et al 2025][research_mullin_2025].

**Weld inspection has become a machine-vision problem**, in [Luo et al 2026][research_luo_2026], [Thompson et al 2025][research_thompson_2025], [Luo et al 2025][research_luo_2025], [Zhao et al 2025, Swrd][research_zhao_2025_2], and [Mukherjee et al 2025][research_mukherjee_2025]. On a vehicle where the longitudinal weld decides the structure, that capability is not incidental.

The period's own difficulties with the same material are worth setting beside all of it, because they are the same difficulties. Examination of welds in stainless sheet is [Nolan 1964][research_nolan_1964], welding of thin-sheet stainless is [Apatovskii et al 1967][research_apatovskii_1967], the electron-beam process that made thin aerospace welds practical is [Kern and Lubin 1963][research_kern_lubin_1963], press forming is [Tozawa 1969][research_tozawa_1969], strain and failure of thin stainless sheet under load is [Khil'chevskii and Kadyshev 1973][research_khil_chevskii_kadyshev_1973], and fatigue-spectrum development is [McCulloch 1960][research_mcculloch_1960]. **Sixty years of instrumentation has not changed what can go wrong with a thin weld. It has changed how early it is found.**

### The Material, Which Is Being Characterised Better Than It Was

The article assumes a yield of 965 megapascals and an ultimate of 1276 for 301 stainless in its extra-full-hard condition, and those are handbook values of the period. Modern characterisation of the same class of material at the temperatures a cryogenic tank sees is [Xu et al 2025, Cryogenic mechanical properties an][research_xu_2025_5], with the effect of cryogenic treatment on microstructure in [Liu and Yuan 2025][research_liu_yuan_2025] and [Wang et al 2026, Influence of Solution and Cryogeni][research_wang_2026_3], load-bearing behaviour in [Wang et al 2026, Experimental and numerical study o][research_wang_2026_4], and forming behaviour under assisted deformation in [Yadav and Gautam 2025][research_yadav_gautam_2025]. Bimetallic additive construction is [Narayanaswamy et al 2025][research_narayanaswamy_2025].

**The proof test the article describes has become a dataset.** Hydraulic burst-pressure testing of pressure vessels is now published as data rather than as a certificate, in [Lüders et al 2025][research_luders_2025], and quality control of thin steel structure is [Liu et al 2025, Quality control method of steel st][research_liu_2025_4]. A designer choosing a knockdown factor today has an evidence base the Atlas team did not, which is the whole content of the shell-buckling section above.

### The Tank After the Mission, Which Nobody Considered

A pressure-stabilised stage that reaches orbit is a large thin-walled pressure vessel in space with residual propellant in it, and that is now recognised as a hazard rather than a curiosity. [Trushlyakov et al 2024][research_trushlyakov_2024] passivates propellant residues in orbit, [Liu et al 2026, Spacecraft System-Level Survivabil][research_liu_2026_3] assesses survivability against the resulting debris, mitigation strategy across orbital regimes belongs to [Navaz and Ntantis 2026][research_navaz_ntantis_2026], and conceptual design against those criteria is [Layachi et al 2025][research_layachi_2025]. **The sustainer reached orbital velocity on many missions and was left there full of gas at pressure**, which nobody in 1957 regarded as anything at all and which the current literature regards as a fragmentation risk.

### Reentry, Which the X-11 Did Not Carry

[Morgado et al 2022][research_morgado_2022] and [Sharma et al 2024][research_sharma_2024] take reentry aerothermodynamics, [Appar and Kumar 2021][research_appar_kumar_2021] ablates at the fluid-solid interface, [Ren 2025, Novel insights into flow mechanics][research_ren_2025_2] examines the flow mechanics of it, [Gerasimov 2025][research_gerasimov_2025] takes ablative carbon protection and [Tian et al 2025][research_tian_2025] an aerogel ceramic, aerothermodynamic sensitivity and optimisation belongs to [Horing et al 2025][research_horing_2025], reachability of a manoeuvring body is [Webb et al 2026][research_webb_2026] and [Su et al 2026][research_su_2026], learned guidance is [Marchetti and Minisci 2021][research_marchetti_minisci_2021], covariance propagation for a high-order system is [Chen et al 2025][research_chen_2025], and the defensive problem of identifying what is coming is [Tonko and Lambiase 2024][research_tonko_lambiase_2024]. The uncontrolled case, which is the same physics applied to debris, is [Öztürk et al 2026][research_ozturk_2026], [Fernando and Charalambous 2026][research_fernando_charalambous_2026], and [Bigham and Puri 2025][research_bigham_puri_2025].

### Economics, Reuse, and the Argument the Atlas Won and Then Lost

The Atlas traded handling cost for mass fraction, and the modern literature is explicit that the trade has reversed. [Du et al 2025][research_du_2025] estimates lifecycle cost for a reusable vehicle, [Lee et al 2026][research_lee_2026] compares recovery methods, [Li et al 2026][research_li_2026] and [Tariq et al 2026][research_tariq_2026] control the landing, and [Xu et al 2025][research_xu_2025] and [Ren et al 2025][research_ren_2025] make that control fault tolerant. **The paper that closes the circle with this article is [Jo and Ahn 2022][research_jo_ahn_2022]**, which optimises the staging of a reusable launch vehicle for minimum lifecycle cost rather than for minimum mass, and thereby inverts the objective function the Atlas was designed against. **Launch cost deflation as an economic phenomenon in its own right is [Christie 2026][research_christie_2026]**, which is the endpoint of an argument the Atlas started by making mass fraction the only thing that mattered.

The strategic side has not gone away either. Silo design is [Sree et al 2025][research_sree_2025], and deterrence posture analysis is [Banevičienė 2026][research_baneviciene_2026] and [Zainel and Saiedy 2025][research_zainel_saiedy_2025]. **The weapon the X-11 was built to become is still in service in its descendants**, which is not true of anything else this series has covered.

That continuity is worth one closing observation about what a survey of this kind can and cannot see. Everything above is drawn from open literature, and open literature is systematically thicker where a technology found civilian use. The Atlas has sixty years of launch-vehicle publication behind it and the Navaho has four years of cancelled-programme reporting, so a comparison of the two archives measures what happened to each programme afterwards at least as much as it measures what each programme did. **The Source Base section below states that as a finding rather than leaving it as a bias**, because it is both.

## What a Conventional Vehicle Would Have Had to Achieve

It has been argued throughout that the balloon tank was necessary, and the range table appears to prove it. That table, however, compares the Atlas against a heavier version of itself, which is not the comparison a designer in 1951 faced. **The real alternative was a conventional two-stage vehicle**, which discards a whole tank set and therefore gets a much larger staging benefit than the Atlas half-stage does. Setting the two against each other is the comparison this discussion owes.

Take a two-stage vehicle carrying the same total propellant, split equally between the stages, with each stage having a structural fraction $f$ of its own loaded mass. The stage structures are then

$$m_{s} = \frac{f \, m_{p} / 2}{1 - f}$$

and the total ideal velocity is the sum of two logarithms rather than one,

$$\Delta v = v_{e} \left[ \ln \frac{m_{\text{all}}}{m_{\text{all}} - m_{p}/2} + \ln \frac{m_{2}}{m_{s}} \right]$$

Evaluating it across the structural fractions a conventional stage of the period could actually achieve, and carrying each result through the same loss calibration and the same range relation, gives

| Two-stage structural fraction | Gross mass | Ideal velocity | Range |
|---|---|---|---|
| 0.08 | 122,288 kg | 8689 m/s | 11,047 km |
| 0.10 | 125,006 kg | 8021 m/s | 7,521 km |
| 0.12 | 127,847 kg | 7467 m/s | 5,665 km |

against the Atlas at 117,900 kilogrammes, 8530 metres per second, and 9,999 kilometres.

**The crossover sits near a structural fraction of nine percent, and conventional stages of the period achieved between eight and twelve.** So the honest conclusion is not that the balloon tank was the only way to build an intercontinental missile. It is that **the balloon tank made a single-and-a-half-stage vehicle competitive with a two-stage one**, and that the choice between them was close enough to turn on things other than mass, which is exactly what happened when the ballistic missile field went two-stage and never came back.

This does not weaken the article's argument so much as locate it. The rocket equation punishes structural mass whatever the configuration. The Atlas spent its structural budget on a radical tank and saved a staging event. Titan spent it on a conventional tank and paid for an altitude ignition. **Both were answers to the same logarithm and the difference between them is roughly one percentage point of structural fraction**, which is a smaller margin than the drama of the balloon tank suggests.

## How Much of This Rests on the Knockdown Factor

The article's most quotable number is that the tensile allowable exceeds the compressive one by a factor of sixty-seven, and that number is not a measurement. It is a classical buckling stress multiplied by a factor of 0.2 chosen from a band of experimental scatter. It is worth asking how much the conclusion moves when that choice moves.

| Knockdown | Compressive allowable | Pressure needed | Margin on the 5 psi spec | Tensile over compressive |
|---|---|---|---|---|
| 0.15 | 10.8 MPa | 1.93 psi | 2.59 | 89 |
| 0.20 | 14.4 MPa | 2.58 psi | 1.94 | 67 |
| 0.30 | 21.6 MPa | 3.87 psi | 1.29 | 45 |
| 0.50 | 36.0 MPa | 6.44 psi | 0.78 | 27 |

Two things follow. **The qualitative claim is robust and the quantitative one is not.** Across the whole plausible range the tensile allowable exceeds the compressive one by between twenty-seven and eighty-nine times, so the asymmetry that motivates the entire design survives any reasonable choice, but the specific figure of sixty-seven does not and should be read as an order rather than a value.

**The second thing is a consistency check the article can actually use.** At a knockdown of 0.5 the five-pound standing pressure would be insufficient, with a margin below one. The reported specification is therefore consistent only with a knockdown somewhere between about 0.15 and 0.4, which is precisely the band the experimental literature reports. **The vehicle's own maintenance specification independently brackets the design factor its engineers must have used**, which is a small result but a satisfying one, because it is the only place in this article where a number from the operational record constrains a number from the design process.

## Where the Framing Breaks Down

Treating the X-11 through the mass-fraction keystone illuminates the design but misleads in three ways.

**It was not a complete missile.** No operational guidance, no reentry vehicle, no warhead, and a range a fifth of the requirement. The X-11 is the airframe and the booster propulsion and nothing else.

**The structure was not the programme's actual difficulty.** Four of eight flights failed, and the failures were plumbing, heating, and pneumatics. A treatment organised around the balloon tank gives the impression that the daring part was the hard part, and the flight record says the opposite, and the record that shows it is the Difficulties Review of [General Dynamics San Diego Ca Convair Div 1966][research_div_1966] rather than any structural document.

**Mass fraction stopped being binding.** The keystone that justified the design is the reason the design was abandoned, since later vehicles could afford heavier structure and could not afford the handling.

**The keystone is a structural principle rather than a vehicle.** Almost everything this article derives applies to the Atlas family, to Centaur, and to any pressure-stabilised shell, and very little of it is specific to the eight articles that flew as Atlas A. A treatment organised this way tells the reader about a design idea and uses one machine as the occasion. That is a legitimate way to write about a testbed whose own record is thin, and it should be said out loud rather than left as an impression.

**And the comparison the article makes is with itself.** The range table varies the Atlas structure and the two-stage section varies a hypothetical alternative, but neither is a comparison with a vehicle that was actually built. Titan I flew, used a conventional structure, reached intercontinental range, and is not analysed here. The honest position is that this article establishes what the balloon tank was worth in the abstract and leaves the empirical comparison to a reader with both sets of mass properties, which the accessible record did not supply.

**The mass figures are not the vehicle's own.** The structural fraction, the mass ratio, and everything computed from them use Atlas D numbers, because Atlas A mass data was not found in the accessible record. The Atlas A was heavier and less capable than the D and the range table therefore describes the family rather than the article that flew. The Epistemic State repeats this, and it is the largest single weakness in the quantitative argument.

## What the X-11 Was Worth

A testbed is worth what it removed from the programme's uncertainty, and that can be stated for this one more precisely than for most.

**It removed the structural question completely and on the first flight.** Before June 1957 the proposition that a shell thinner in proportion than a drink can, held up by five pounds of nitrogen, would survive launch was an argument. After a vehicle tumbled at two kilometres and held together it was a fact, and no later Atlas flight added to that knowledge. One flight, two kilometres, and the largest single risk in the programme was retired.

**It removed most of the propulsion question over seven further flights**, which is a poor return per flight and the only return available, because propulsion faults are individually rare and collectively common and there is no substitute for accumulating them.

**It removed almost nothing about guidance, reentry, or range**, because it carried no operational guidance, no reentry vehicle, and flew a fifth of the required speed. Those were the Atlas B and the later variants.

The programme's own sequencing confirms the reading. Atlas B began flying in July 1958, five weeks after the last Atlas A, which is not the interval of a programme waiting for a verdict. **The A was allowed to overlap its successor because the question it existed to answer had been settled a year earlier and everything since had been debugging**, and debugging is work that transfers to the next article rather than gating it.

The distribution is lopsided and it is the distribution a good testbed should have. **The riskiest item was retired first and cheapest**, and the items that could only be settled by building the real weapon were left to the real weapon. Set against the [X-10][related_post_a307_north_american_x10], which retired almost nothing because its risk was a quantity that accumulates, the X-11 is what a testbed looks like when the physics cooperates.

## The Designation, Which by Now Is the Series Question

The [previous article][related_post_a307_north_american_x10] found that the [X-8][related_post_a305_aerojet_x8], the [X-9][related_post_a306_bell_x9], and the [X-10][related_post_a307_north_american_x10] were all RTV-A vehicles before they were X vehicles, and concluded that three apparent anomalies were one administrative act seen three times. The X-11 does not fit that explanation, and the misfit is informative.

**The Atlas A was never an RTV-A vehicle.** It came from a weapon programme with its own designation lineage, running SSM-A, then B-65, then SM-65, and the X-11 label sits beside that lineage rather than inside it. So whatever attached an X number to this vehicle was not the RTV absorption that explains the previous three. The accessible record does not say what it was, and no document found for this article uses the X designation at all.

Three readings are available and the article does not choose between them.

**The X number may have been an allocation that was made and never used.** This is the reading the absence of any document using it supports, and it would put the X-11 and X-12 in the same category as the reserved-but-unassigned cases the series meets later at [A336][ref_series_close] and elsewhere. A designation that exists in the numbering registry and nowhere else is a bookkeeping entry rather than a name.

**It may have been a test-article designation for the pre-operational vehicles specifically**, distinguishing the eight Atlas A articles from the weapon they were prototyping, in the way that an X number legitimately distinguishes a research article from a production one. On this reading the label is doing exactly the job the X series exists for, and the fact that nobody used it in writing is an accident of a programme that had a perfectly good name already.

**Or it may be a later retrofit by compilers rather than a period assignment at all.** Inventories of X-vehicles have an incentive to fill gaps, and X-11 and X-12 are gaps that the Atlas A and Atlas B fit neatly. The series has already met one case where a compilation attributes a designation that nomenclature records reportedly deny, in the X-23, and the reasoning there applies here.

**What the case establishes for the series is narrower than a resolution and more useful than a guess.** The previous article's explanation was that the X-series absorbed a different series wholesale. That explanation is correct for three vehicles and does not extend to this one, which means the broadening of the X-series has at least two mechanisms rather than one. A series that has admitted a sounding rocket, an air-launched missile, an autonomous testbed, and now an intercontinental ballistic missile did not do so by a single decision, and any account that offers one is too tidy. The closing article at [A368][ref_series_close] has to carry both mechanisms and probably more.

## The Source Base

The contrast with the previous article is sharp and it is worth stating as a controlled result.

**The Navaho record is absent from the defence archive and the Atlas record is present.** The [X-10][related_post_a307_north_american_x10] article established that querying the Defense Technical Information Center through the Crossref publisher prefix on the project number MX-770 returns nothing about the Navaho at all, while the adjacent MX-776 returns a RASCAL weapon system report. The same route on the Atlas returns the Flight Test Working Group reports for individual missiles, the multi-volume Difficulties Review of the Atlas booster and its ground support systems, propellant-loading system design, and engine system-test data. **Same archive, same route, same query form, and the difference is that one programme was cancelled in 1957 and the other flew for sixty years.** The specific documents are [General Dynamics/Astronautics San Diegoca 1961][research_diegoca_1961] and its companion flight test reports, the five volumes of [General Dynamics San Diego Ca Convair Div 1966][research_div_1966], and [Peters and Hall 1963][research_peters_hall_1963] on engine system-test data, with the programme-level history in [Rockefeller and Alfred 1960][research_rockefeller_alfred_1960].

The aerospace archive holds the structural literature rather than the vehicle, which suits this article because the keystone is a structural principle and not a vehicle detail. The shell-buckling and pressure-stabilisation literature is large, contemporary with the design, and directly applicable.

**The aerospace archive holds the discipline rather than the vehicle**, and for this article that is the right trade. The keystone is a structural principle, and the shell-buckling and pressure-stabilisation literature is large, contemporary with the design, and directly applicable. Nineteen NTRS records are cited here against eleven before the primary pass, and the ones that matter most, namely the pressurised-cylinder buckling correlation and the imperfection-sensitivity measurements, are exactly the documents a designer of this vehicle would have had on his desk.

**What is thin is the X-11 as such.** The designation appears in compilations and the flight record is well attested, but the accessible record concerns the Atlas A rather than a vehicle called X-11, and no document found for this article uses the X designation. That is the fourth consecutive article in which the X number is an administrative label rather than a name anyone used, and the pattern identified in the [previous article][related_post_a307_north_american_x10] now has more instances than the series has counterexamples in this stretch.

**The mass data is the specific gap.** Gross, empty, and propellant masses for the Atlas A itself were not found, so the article uses Atlas D figures throughout and says so wherever they appear. Since the Atlas A was an earlier and heavier article, the structural fraction used here is better than the fraction the X-11 actually achieved, and every range figure derived from it is correspondingly optimistic. The direction of the error is known even though its size is not, which is the most that can be said.

## Epistemic State

**Historical fact, well supported.** Eight Atlas A vehicles flew from Cape Canaveral between 11 June 1957 and 3 June 1958, four successfully, from Launch Complexes 12 and 14, with apogees near 120 kilometres. The programme designation was WS 107A-1 and the design authority was Karel Bossart at Convair. The structure is pressure-stabilised 301 stainless steel between 0.014 and 0.037 inches thick. The vehicle requires about five pounds per square inch of nitrogen when unfuelled and collapses without it. The Atlas uses a one-and-a-half stage arrangement in which two booster engines and a skirt are jettisoned and the sustainer continues on the same tanks. The Navaho was cancelled on 12 July 1957, four weeks after the first Atlas A flight.

**Reported but from compilations rather than programme documents.** The X-11 and X-12 designations for Atlas A and Atlas B, which no document found for this article actually uses. The masses used here, which are Atlas D figures rather than Atlas A figures, since Atlas A mass data was not found. The 282 second specific impulse and 133 second burn time. The flight-by-flight apogees and outcomes. The reported failure causes. The five pounds per square inch standing pressure, which is the article's single most quoted number and which rests on secondary compilation rather than on a specification.

**The mass substitution is the largest weakness in the quantitative argument and its direction is known.** The Atlas A was an earlier and heavier article than the D, so the structural fraction used here is better than the fraction the X-11 achieved, and every range figure derived from it is correspondingly optimistic. What the substitution does not affect is the sensitivity, since the range table varies the structure about whatever baseline is chosen, and the two-stage comparison, which is a calculation about configurations rather than about this vehicle.

**Engineering analysis, derived here and independently checkable.** The radius-to-thickness ratios and the drink-can comparison. The membrane stresses, the fixed hoop-to-axial ratio of two, and the demonstration that the light gauge cannot exist at full pressure. The acceleration head and its ratio to ullage pressure. The classical buckling stresses, the knocked-down allowables, and the sensitivity of every conclusion drawn from them to the choice of knockdown factor. The axial tension from standing pressure, the pressure required to offset buckling, and the finding that the reported five-pound specification is consistent only with a knockdown between about 0.15 and 0.4. The critical bending moment and its independence of thickness. Euler column buckling at 121 times the empty weight. The tank volume, propellant split, and nitrogen mass, giving a structure-to-gas ratio of 103. The common-bulkhead saving. The mass fractions, mass ratio, and ideal velocity. The loss calibration, the range sensitivity table, and the two-stage comparison showing a crossover near a nine percent structural fraction. The staging gain of 1044 metres per second. The thrust-to-weight, propellant flow, burn consumption, and axial load factor at cutoff. The maximum dynamic pressure, its occurrence at one scale height, and the aerodynamic bending moment. The acoustic power, sound pressure level, and pressure fluctuation. The slosh frequency. The skin thermal time constant. The Allen and Eggers peak deceleration and its independence of ballistic coefficient. The boil-off rate. The proof and burst factor chain. The tank figure of merit. The orbital comparison. The binomial standard error on the success rate and the demonstration that no trend is detectable across eight flights.

**Inference, argued but not established.** That the balloon tank and the one-and-a-half stage arrangement reinforce each other rather than trading against each other, which the staging computation supports but does not prove. That the X-11's keystone being exercised early is why a short flight sufficed, in contrast to the X-10. That pressure-stabilised vehicles are unusually exposed to pogo because longitudinal stiffness varies with tank pressure. That the design was abandoned because handling cost outlasted the mass-fraction constraint.

**A qualification the article makes against itself.** The range table compares the Atlas against a heavier version of itself, which is not the comparison a designer in 1951 faced. Setting it against a conventional two-stage vehicle instead puts the crossover near a nine percent structural fraction, which is inside the range conventional stages of the period achieved. **The balloon tank therefore made a single-and-a-half-stage vehicle competitive with a two-stage one rather than making an intercontinental missile possible at all**, and the article says so in its own section rather than leaving the stronger claim standing.

**Assumptions made explicit.** A flight tank pressure of 60 pounds per square inch, which is representative rather than sourced and which every membrane stress in the article scales with directly. Material properties for 301 extra-full-hard stainless steel of 965 megapascals yield, 1276 ultimate, and 193 gigapascals modulus. A knockdown factor of 0.2, whose effect on every conclusion drawn from it is tabulated in its own section rather than buried. A tank length of 18 metres and a steel density of 8000 kilogrammes per cubic metre. Ten metres of liquid oxygen head at six times gravity. A mixture ratio of 2.25 with propellant densities of 1141 and 800. A jettisoned booster package of three tonnes. A drag coefficient of 1.2 and a uniform wind profile for the standing case. A convective coefficient of 200 watts per square metre kelvin for the skin and 10 for the tank, a specific heat of 500, and a latent heat of 213 kilojoules per kilogramme. An acoustic conversion efficiency of half of one percent. A normal-force slope of two per radian and three degrees of incidence at maximum dynamic pressure. A scale height of 7200 metres and a net acceleration of three metres per second squared for the dynamic-pressure derivation. An entry speed of seven kilometres per second at thirty degrees for the reentry result. Equal propellant split and equal structural fraction per stage for the two-stage comparison. And the gravity and drag loss of 1337 metres per second, which is calibrated rather than derived and which fixes the first row of the range table by construction.

**Where the assumptions matter most.** The flight pressure and the knockdown factor carry more of the article than any other input. Every hoop stress, every margin, and the burst chain move linearly with the first, and the compressive allowable, the pressure-to-offset-buckling figure, and the sixty-seven-fold asymmetry all move with the second. The article tabulates the second and does not tabulate the first, which is an asymmetry in the treatment rather than in the physics, and a reader who doubts the sixty-pound figure should scale the membrane results accordingly.

**Where information postdates the editorial date.** The contemporary literature section is written from current knowledge, as the series convention requires, and the Atlas V abandonment of the balloon tank in 2002 and the subsequent history are stated from current knowledge rather than from the vantage of 1957.

## Out of Scope

The Atlas B, C, D, E, and F, of which the B is the next article. The reentry vehicle and the warhead. The radio-inertial and later all-inertial guidance systems in any depth. Silo and coffin basing. The Atlas as a space launch vehicle beyond noting that it became one. Centaur, which kept the balloon tank and deserves its own treatment. The MX-774 predecessor beyond its role in the origin. Comparative economics against Titan and Minuteman, and the two-stage comparison above is a structural calculation rather than a programme comparison. The Soviet R-7, which solved the same problem with a different configuration entirely and would make the best single comparison this article does not attempt. Manufacturing tooling and the factory, which for a structure of this gauge is a larger subject than the design and which the sources for this article barely touch. The Mercury programme and the man-rating that followed.

## Conclusion

The X-11 is a fuel tank that flies. Its skin is thinner in proportion than a drink can, its compressive strength is two hundred times smaller than its tensile strength, and it is held up by a pressure a bicycle tyre would find low. **Every one of those facts is a consequence of one relation**, which is that the rocket equation returns velocity logarithmically in mass ratio, so a weapon that must reach ten thousand kilometres has to spend its structural budget as though it were the last money it had.

The article's own arithmetic puts a number on it. Making the structure half as efficient turns an intercontinental missile into an intermediate-range one, and no amount of better engine or better trajectory recovers it. Bossart's balloon was not a clever trick. It was the only available answer to a question that had been posed in the form of a logarithm.

The article's own scrutiny qualifies that. Set against a conventional two-stage vehicle rather than against a heavier Atlas, the crossover sits near a nine percent structural fraction, which is inside what conventional stages of the period achieved. **The balloon tank did not make the intercontinental missile possible. It made this particular intercontinental missile competitive with the alternative**, by about one percentage point of structural fraction, and the field subsequently went the other way and stayed there. Bossart's answer was right for the vehicle he was building and was not the only answer to the question.

What remains true after all the qualification is the shape of the problem rather than the size of the answer. **A weapon specified by range is specified by a logarithm**, and a logarithm rewards nothing except mass ratio. Every distinctive feature of this vehicle follows from that and from nothing else. The tank is thin because the logarithm punishes thickness. The tank is pressurised because a thin tank in compression buckles at a fiftieth of the stress it can carry in tension. The engines are dropped and the tanks are not because the logarithm cares about burnout mass and an altitude ignition was not trusted. The vehicle cannot stand up because none of those decisions left anything over for standing up.

There is a second result and it belongs to the series rather than to the vehicle. **The X-10 could not test its keystone in twenty-eight minutes and the X-11 tested its keystone completely in two**, and the difference is that a structural load is applied in full early and a drift rate accumulates. The two vehicles are separated by one designation and four weeks, they were built by rival contractors for the same mission, and the reason one testbed worked and the other did not has nothing to do with either company. It is a property of the quantity being measured, and it is the sort of thing that only becomes visible when the vehicles are read in order.

The last thing worth saying is about the tank itself, which has outlived every argument made about it here. Bossart's shell is still flying, on Centaur, on the stage that has the strongest possible reason to care about mass and the weakest possible reason to care about being set down empty in a hangar. **An idea that was adopted because a weapon needed range, abandoned because a launcher needed convenience, and retained where neither consideration applies has been tested about as thoroughly as an engineering idea can be.** It turns out to be right in exactly the conditions the arithmetic above says it should be right in, which is not something one can say of many designs that are seventy years old.

## References

### Books

- [Bruhn 1973 Analysis and Design of Flight Vehicle Structures][book_bruhn_1973]
- [Brush and Almroth 1975 Buckling of Bars, Plates and Shells][book_brush_almroth_1975]
- [Jenkins Landis and Miller 2003 American X-Vehicles, An Inventory X-1 to X-50][book_jenkins_landis_miller_2003]
- [Miller 2001 The X-Planes, X-1 to X-45][book_miller_2001]
- [Neufeld 1995 The Rocket and the Reich][book_neufeld_1995]
- [Sutton and Biblarz 2016 Rocket Propulsion Elements][book_sutton_biblarz_2016]
- [Timoshenko and Gere 1961 Theory of Elastic Stability][book_timoshenko_gere_1961]
- [Walker Bernstein and Lang 2005 Seize the High Ground][book_walker_powell_2005]

[book_bruhn_1973]: https://openlibrary.org/search?q=Bruhn+Analysis+and+Design+of+Flight+Vehicle+Structures
[book_brush_almroth_1975]: https://openlibrary.org/search?q=Brush+Almroth+Buckling+of+Bars+Plates+and+Shells
[book_jenkins_landis_miller_2003]: https://openlibrary.org/search?q=Jenkins+Landis+Miller+American+X+Vehicles
[book_miller_2001]: https://openlibrary.org/search?q=Miller+The+X+Planes+X-1+to+X-45
[book_neufeld_1995]: https://openlibrary.org/search?q=Neufeld+The+Rocket+and+the+Reich
[book_sutton_biblarz_2016]: https://openlibrary.org/search?q=Sutton+Biblarz+Rocket+Propulsion+Elements
[book_timoshenko_gere_1961]: https://openlibrary.org/search?q=Timoshenko+Gere+Theory+of+Elastic+Stability
[book_walker_powell_2005]: https://openlibrary.org/search?q=Walker+Bernstein+Lang+Seize+the+High+Ground

### Reference

- [balloon tank][ref_balloon_tank]
- [Convair X-11][ref_x11]
- [X-12][ref_series_close]

[ref_balloon_tank]: https://en.wikipedia.org/wiki/Balloon_tank
[ref_series_close]: https://en.wikipedia.org/wiki/SM-65B_Atlas
[ref_x11]: https://en.wikipedia.org/wiki/SM-65A_Atlas

### Related Post

- [X-1][related_post_a298_bell_x1]
- [X-10][related_post_a307_north_american_x10]
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

### Research

- [Abhishek Hari, 2026][research_abhishek_hari_2026]
- [Abraham 1963][research_abraham_1963]
- [Adam and King 1965][research_adam_king_1965]
- [Adams and Stoll 1969][research_adams_stoll_1969]
- [Agarwal et al 2025][research_agarwal_2025]
- [Aguiar et al 2025][research_aguiar_2025]
- [Ajeesh et al 2026][research_ajeesh_2026]
- [Allen 1966][research_allen_1966]
- [Almetwally et al 2026][research_almetwally_2026]
- [Amiro 1962][research_amiro_1962]
- [Apatovskii et al 1967][research_apatovskii_1967]
- [Appar and Kumar 2021][research_appar_kumar_2021]
- [Azizi and Dornisch 2025][research_azizi_dornisch_2025]
- [Babcock and Sechler 1962][research_babcock_sechler_1962]
- [Babcock and Sechler 1963][research_babcock_sechler_1963]
- [Bahiman and Thole 1965][research_bahiman_thole_1965]
- [Ballentine et al 1966][research_ballentine_1966]
- [Banevičienė 2026][research_baneviciene_2026]
- [Beer and Lennox 1965][research_beer_lennox_1965]
- [Bell 1965][research_bell_1965]
- [Benfriha et al 2026][research_benfriha_2026]
- [Berg 1968][research_berg_1968]
- [Bershadskyi et al 2022][research_bershadskyi_2022]
- [Bigham and Puri 2025][research_bigham_puri_2025]
- [Binion 1964][research_binion_w_1964]
- [Binion et al 1962][research_binion_1962]
- [Bohne 1964][research_bohne_1964]
- [Borelli and Carroll 1967][research_borelli_carroll_1967]
- [Botterill 1961][research_botterill_1961]
- [Boyd 1963][research_boyd_1963]
- [Bozich 1967][research_bozich_1967]
- [Buell 1964][research_buell_1964]
- [Cha and Ko 2025][research_cha_ko_2025]
- [Cha et al 2024][research_cha_2024]
- [Chaabani et al 2025][research_chaabani_2025]
- [Chehrzad and Khoramishad 2026][research_chehrzad_khoramishad_2026]
- [Chen et al 2025][research_chen_2025]
- [Cheng et al 2025][research_cheng_2025]
- [Chitwood 1962][research_chitwood_1962]
- [Christie 2026][research_christie_2026]
- [Chung 2026][research_chung_2026]
- [Coffin 1970][research_coffin_1970]
- [Cooper 1961][research_cooper_1961]
- [Coppa and Nash 1962][research_coppa_nash_1962]
- [Coppa and Nash 1964][research_coppa_nash_1964]
- [Coxe and Tatom 1962][research_coxe_tatom_1962]
- [Crandall and Mark 1963][research_crandall_mark_1963]
- [Crandall and Mark 1963, Failure Due to Random Vibration][research_crandall_mark_1963_3]
- [Crandall and Mark 1963, Transmission of Random Vibration][research_crandall_mark_1963_2]
- [Crose 1965][research_crose_1965]
- [Dafler 1962][research_dafler_1962]
- [Dalle et al 2024][research_dalle_2024]
- [Das and Padmanabhan 2022][research_das_padmanabhan_2022]
- [General Dynamics/Astronautics San Diegoca 1961][research_diegoca_1961]
- [DIGiovanii and Dugundji 1965][research_digiovanii_dugundji_1965]
- [Ding et al 2025][research_ding_2025]
- [Dolgopolov and Nikolayev 2024][research_dolgopolov_nikolayev_2024]
- [Dolton and Reed 1966][research_dolton_reed_1966]
- [Du and Groh 2026][research_du_groh_2026]
- [Du et al 2025][research_du_2025]
- [Edwards et al 2023][research_edwards_2023]
- [Elliott and Rau 1968][research_elliott_rau_1968]
- [Lee et al 2024][research_engineering_2024]
- [Erdogan and Tekin 2025][research_erdogan_tekin_2025]
- [Eshete et al 2024][research_eshete_2024]
- [Evkin 2026][research_evkin_2026]
- [Faulkner 1961][research_faulkner_1961]
- [Faulkner and Ward 1961][research_faulkner_ward_1961]
- [Feodosiev and Siniarev 1959][research_feodosiev_siniarev_1959]
- [Fernando and Charalambous 2026][research_fernando_charalambous_2026]
- [Frazier 1967][research_frazier_1967]
- [Gao et al 2024][research_gao_2024]
- [Gashe et al 2025][research_gashe_2025]
- [Ge et al 2026][research_ge_2026]
- [General Dynamics San Diego Ca Convair Div 1966][research_div_1966]
- [Gerald and Runyan 1962][research_gerald_runyan_1962]
- [Gerasimov 2025][research_gerasimov_2025]
- [Ghio and Cerri 2026][research_ghio_cerri_2026]
- [Goldman and Miessner 1965][research_goldman_miessner_1965]
- [Goldman and Miessner 1966][research_goldman_miessner_1966]
- [Gong et al 2024][research_gong_2024]
- [Gong et al 2026][research_gong_2026]
- [Greenfield 1960][research_greenfield_1960]
- [Greenspon 1963][research_greenspon_1963]
- [Grey 1953][research_grey_1953]
- [Guo et al 2026][research_guo_2026]
- [Harrje 1959][research_harrje_1959]
- [Hausrath and Dittoe 1962][research_hausrath_dittoe_1962]
- [He et al 2024][research_he_2024]
- [Hegg 1964][research_hegg_1964]
- [Hill et al 1969][research_hill_1969]
- [Hines 1966][research_hines_1966]
- [Hoff 1942][research_hoff_1942]
- [Hoff et al 1962][research_hoff_1962]
- [Horing et al 2025][research_horing_2025]
- [Hu et al 2025][research_hu_2025]
- [Huang et al 2025, Modal Identification of a Wind Tur][research_huang_2025_2]
- [Humphrey 1961][research_humphrey_1961]
- [Hung and Hunt 1964][research_hung_hunt_1964]
- [Calderon Hurtado et al 2026][research_hurtado_2026]
- [Ichino and Takahashi 1965][research_ichino_takahashi_1965]
- [Im et al 2025][research_im_2025]
- [Ivanco et al 2024][research_ivanco_2024]
- [Jalaja et al 2024][research_jalaja_2024]
- [Jayan et al 2024][research_jayan_2024]
- [Jeon et al 2024][research_jeon_2024]
- [Jiao et al 2023][research_jiao_2023]
- [Jin 2025][research_jin_2025]
- [Jo and Ahn 2022][research_jo_ahn_2022]
- [Johnson and Kelsen 1969][research_johnson_kelsen_1969]
- [Jones and Farmer 1966][research_jones_farmer_1966]
- [Jones and Farmer 1967][research_jones_farmer_1967]
- [Juarez 1961][research_juarez_1961]
- [Kamenskii and Martirosov 2021][research_kamenskii_martirosov_2021]
- [Kaplan 1961][research_kaplan_1961]
- [Karman and Tsien 1941][research_karman_tsien_1941]
- [Kaufman 1958][research_kaufman_1958]
- [Keast 1961][research_keast_1961]
- [Kempner and Chen 1974][research_kempner_chen_1974]
- [Kern and Lubin 1963][research_kern_lubin_1963]
- [Khamlak 2026][research_khamlak_2026]
- [Khil'chevskii and Kadyshev 1973][research_khil_chevskii_kadyshev_1973]
- [Kim et al 2025][research_kim_2025]
- [Kuentz 1969][research_kuentz_1969]
- [Kumar et al 2023][research_kumar_2023]
- [Kundu and Mukhopadhyay 2025][research_kundu_mukhopadhyay_2025]
- [Kömle et al 2025][research_komle_2025]
- [Larson 1965][research_larson_1965]
- [Layachi et al 2025][research_layachi_2025]
- [Leaumont 1965][research_leaumont_1965]
- [Lee and Baek 2026][research_lee_baek_2026]
- [Lee et al 2024][research_lee_2024]
- [Lee et al 2026][research_lee_2026]
- [Lee et al 2026, Boil-Off Rate Behavior in a Double][research_lee_2026_2]
- [Lei et al 2025][research_lei_2025]
- [Leng et al 2026][research_leng_2026]
- [Lenihan 1962][research_lenihan_1962]
- [Li et al 2024, Adaptive Sequential Convex Program][research_li_2024_3]
- [Li et al 2025, Reliability design and management][research_li_2025_2]
- [Li et al 2026][research_li_2026]
- [Liao et al 2023][research_liao_2023]
- [Lin et al 2025][research_lin_2025]
- [Liu and Yuan 2025][research_liu_yuan_2025]
- [Liu et al 2020][research_liu_2020]
- [Liu et al 2025][research_liu_2025]
- [Liu et al 2025, Quality control method of steel st][research_liu_2025_4]
- [Liu et al 2026][research_liu_2026]
- [Liu et al 2026, Spacecraft System-Level Survivabil][research_liu_2026_3]
- [Loewy 1965][research_loewy_1965]
- [Louw and Kearsley 2026][research_louw_kearsley_2026]
- [Lu and Cao 2025][research_lu_cao_2025]
- [Lu and Cao 2025, Comparative study on wave response][research_lu_cao_2025_2]
- [Lu and Cao 2026][research_lu_cao_2026]
- [Lu et al 2026][research_lu_2026]
- [Lubowe 1965][research_lubowe_1965]
- [De Luca et al 2026][research_luca_2026]
- [Luo et al 2025][research_luo_2025]
- [Luo et al 2026][research_luo_2026]
- [Lüders et al 2025][research_luders_2025]
- [MacPherson 1963][research_macpherson_1963]
- [Mandell and White 1960][research_mandell_white_1960]
- [Manning and Price 1961][research_manning_price_1961]
- [Marchetti and Minisci 2021][research_marchetti_minisci_2021]
- [Marcus et al 1969][research_marcus_1969]
- [Matthews 1957][research_matthews_1957]
- [McCulloch 1960][research_mcculloch_1960]
- [Mescall 1961][research_mescall_1961]
- [Michielsen 1948][research_michielsen_1948]
- [Miller 1967][research_miller_1967]
- [Miller and Gerus 1966][research_miller_gerus_1966]
- [Mitra et al 2021][research_mitra_2021]
- [Moore 1958][research_moore_1958]
- [Morey and Koshar 1961][research_morey_koshar_1961]
- [Morgado et al 2022][research_morgado_2022]
- [Mow and Sadowsky 1962][research_mow_sadowsky_1962]
- [Mukherjee et al 2025][research_mukherjee_2025]
- [Mullin et al 2025][research_mullin_2025]
- [Murphy 1961][research_murphy_1961]
- [Murphy and Rubesin 1965][research_murphy_rubesin_1965]
- [Muthukumar et al 2020][research_muthukumar_2020]
- [NACA 1966][research_naca_1966]
- [NACA 1975][research_naca_1975]
- [Narayanaswamy et al 2025][research_narayanaswamy_2025]
- [Nardo and Sadler 1962][research_nardo_sadler_1962]
- [Nast and Williams 1967][research_nast_williams_1967]
- [Navaz and Ntantis 2026][research_navaz_ntantis_2026]
- [Nein and Head 1962][research_nein_head_1962]
- [Neumaier et al 2025][research_neumaier_2025]
- [Newton and Makrides 1954][research_newton_makrides_1954]
- [Ni et al 2026][research_ni_2026]
- [Nickell 1961][research_nickell_1961]
- [Nikonchuk 2026][research_nikonchuk_2026]
- [Nolan 1964][research_nolan_1964]
- [Nott 1963][research_nott_1963]
- [Rioseco Olave et al 2023][research_olave_2023]
- [Ostner 1962][research_ostner_1962]
- [Ozoigbo et al 2025][research_ozoigbo_2025]
- [Paleti et al 2026][research_paleti_2026]
- [Pan et al 2026][research_pan_2026]
- [Panda et al 2025][research_panda_2025]
- [Parkyn 1958][research_parkyn_1958]
- [Pei 2021][research_pei_2021]
- [Peshkhoev 2026][research_peshkhoev_2026]
- [Peters and Hall 1963][research_peters_hall_1963]
- [Peterson 1960][research_peterson_1960]
- [Platus 1967][research_platus_1967]
- [Polivanov and Sidorenko 2026][research_polivanov_sidorenko_2026]
- [Porenta et al 2025][research_porenta_2025]
- [Powell 1962][research_powell_1962]
- [Prasad 2022][research_prasad_2022]
- [Punga and Campbell 1962][research_punga_campbell_1962]
- [Płaczek et al 2023][research_paczek_2023]
- [Qiu et al 2023][research_qiu_2023]
- [Qiu et al 2026][research_qiu_2026]
- [Radovcich 1965][research_radovcich_1965]
- [Raji et al 2019][research_raji_2019]
- [Dian Fitria Ramdani and Dene Herwanto 2026][research_ramdani_2026]
- [Randall 1970][research_randall_1970]
- [Reddy et al 2026][research_reddy_2026]
- [Ren 2025, Novel insights into flow mechanics][research_ren_2025_2]
- [Ren et al 2025][research_ren_2025]
- [Reynolds 1960][research_reynolds_1960]
- [Rhee et al 2025][research_rhee_2025]
- [Rieck et al 2026][research_rieck_2026]
- [Rindal and Dahm 1967][research_rindal_dahm_1967]
- [Roberts and Wilhem 1964][research_roberts_wilhem_1964]
- [Rockefeller and Alfred 1960][research_rockefeller_alfred_1960]
- [Roithmayr and Pei 2024][research_roithmayr_pei_2024]
- [Rubin 1965][research_rubin_1965]
- [Rubin 1966][research_rubin_1966]
- [Tillotson Rudd et al 2024][research_rudd_2024]
- [Russell 1964][research_russell_1964]
- [Sadovský et al 2024][research_sadovsky_2024]
- [Sahu et al 2024][research_sahu_2024]
- [Saiki et al 2026][research_saiki_2026]
- [Samadzadeh et al 2024][research_samadzadeh_2024]
- [Samuelson 1968][research_samuelson_1968]
- [Scherberg and Rubin 1953][research_scherberg_rubin_1953]
- [Schurmann 1957][research_schurmann_1957]
- [Schweppe 1964][research_schweppe_1964]
- [Scott 1963][research_scott_1963]
- [Sellers 1948][research_sellers_1948]
- [Sharma et al 2024][research_sharma_2024]
- [Shaw et al 1952][research_shaw_1952]
- [Simon 1965][research_simon_1965]
- [Singh et al 2026][research_singh_2026]
- [Slider 1967][research_slider_1967]
- [Slifka 1960][research_slifka_1960]
- [Snodgrass 1955][research_snodgrass_1955]
- [Snyder et al 1974][research_snyder_1974]
- [Solomon and Tamiru 2026][research_solomon_tamiru_2026]
- [Song et al 2026][research_song_2026]
- [Sree et al 2025][research_sree_2025]
- [Stancil 1963][research_stancil_1963]
- [Steeves 1975][research_steeves_1975]
- [Steeves 1975, A Linear Analysis of the Deformati][research_steeves_1975_2]
- [Stephens 1965][research_stephens_1965]
- [Stetson 1964][research_stetson_1964]
- [Stinson and Gross 1972][research_stinson_gross_1972]
- [Su et al 2026][research_su_2026]
- [Summerfield 1960][research_summerfield_1960]
- [Sun et al 2024][research_sun_2024]
- [Sun et al 2026][research_sun_2026]
- [Tan et al 2023][research_tan_2023]
- [Tantaroudas and Karachalios 2026][research_tantaroudas_karachalios_2026]
- [Tao and Qi 2025][research_tao_qi_2025]
- [Tariq et al 2026][research_tariq_2026]
- [Thielemann 1962][research_thielemann_1962]
- [Thomas 2022][research_thomas_2022]
- [Thompson et al 2025][research_thompson_2025]
- [Tian et al 2025][research_tian_2025]
- [Tonko and Lambiase 2024][research_tonko_lambiase_2024]
- [Tozawa 1969][research_tozawa_1969]
- [Trushlyakov et al 2024][research_trushlyakov_2024]
- [Tyzzer and Pernet 1964][research_tyzzer_pernet_1964]
- [Ugural and Cheng 1968][research_ugural_cheng_1968]
- [Velmurugan and Buragohain 2023][research_velmurugan_buragohain_2023]
- [Ventura et al 2023][research_ventura_2023]
- [Vreeland 1960][research_vreeland_1960]
- [Vîlceanu et al 2024][research_vilceanu_2024]
- [Wachi and Gilmartin 1966][research_wachi_gilmartin_1966]
- [Wagenblast and Bettinger 2024][research_wagenblast_bettinger_2024]
- [Walters 1967][research_walters_1967]
- [Walton and Simmons 1962][research_walton_simmons_1962]
- [Wang 1966][research_wang_1966]
- [Wang 1973][research_wang_1973]
- [Wang and Chen 2022][research_wang_chen_2022]
- [Wang and Ramamritham 1947][research_wang_ramamritham_1947]
- [Wang et al 1953][research_wang_1953]
- [Wang et al 2024, Numerical study on the effectivene][research_wang_2024_2]
- [Wang et al 2026][research_wang_2026]
- [Wang et al 2026, Experimental and numerical study o][research_wang_2026_4]
- [Wang et al 2026, Experimental investigation of acou][research_wang_2026_2]
- [Wang et al 2026, Influence of Solution and Cryogeni][research_wang_2026_3]
- [Webb et al 2026][research_webb_2026]
- [Weingarten 1962][research_weingarten_1962]
- [Weiss and Goodman 1960][research_weiss_goodman_1960]
- [Wertheimer 1957][research_wertheimer_1957]
- [Whitcombe 1961][research_whitcombe_1961]
- [Whitcombe 1961, Optimum Propellant Loading And Pro][research_whitcombe_1961_2]
- [Wilner et al 1960][research_wilner_1960]
- [Winstead 1966][research_winstead_1966]
- [Wood 1961][research_wood_1961]
- [Wu et al 2026][research_wu_2026]
- [Xu and Xu 2024][research_xu_xu_2024]
- [Xu et al 2025][research_xu_2025]
- [Xu et al 2025, Cryogenic mechanical properties an][research_xu_2025_5]
- [Yadav and Gautam 2025][research_yadav_gautam_2025]
- [Yang and Chen 2025][research_yang_chen_2025]
- [Yang et al 2022][research_yang_2022]
- [Yang et al 2026, Comparative Study on Post-Buckling][research_yang_2026_2]
- [Yao et al 2022][research_yao_2022]
- [Narayana Yenugula et al 2025][research_yenugula_2025]
- [Yoon et al 2021][research_yoon_2021]
- [Yu 2026][research_yu_2026]
- [Yu et al 2023][research_yu_2023]
- [Yu et al 2024][research_yu_2024]
- [Yu et al 2024, Approximate analytical solutions f][research_yu_2024_2]
- [Yu et al 2026, Design and evaluation of thermal i][research_yu_2026_2]
- [Yun and Liu 2023][research_yun_liu_2023]
- [Zahn et al 2025][research_zahn_2025]
- [Zainel and Saiedy 2025][research_zainel_saiedy_2025]
- [Zhang 2022][research_zhang_2022]
- [Zhang and He 2024][research_zhang_he_2024]
- [Zhang et al 2024, Fluid-structure interaction analys][research_zhang_2024_4]
- [Zhang et al 2025, Bending test and numerical analysi][research_zhang_2025_5]
- [Zhang et al 2025, Feasibility study on synthermal st][research_zhang_2025_3]
- [Zhang et al 2025, Improving storage performance of a][research_zhang_2025_2]
- [Zhang et al 2025, Multi-objective optimization of cr][research_zhang_2025_7]
- [Zhang et al 2026][research_zhang_2026]
- [Zhang et al 2026, Fatigue life and failure location][research_zhang_2026_2]
- [Zhao and Tan 2026][research_zhao_tan_2026]
- [Zhao et al 2022][research_zhao_2022]
- [Zhao et al 2024][research_zhao_2024]
- [Zhao et al 2025, Swrd][research_zhao_2025_2]
- [Zhao et al 2026][research_zhao_2026]
- [Zhou et al 2022][research_zhou_2022]
- [Zhou et al 2024][research_zhou_2024]
- [Zhou et al 2025][research_zhou_2025]
- [Zhou et al 2025, Vibro-acoustic analysis and suppre][research_zhou_2025_2]
- [Zhu 2026][research_zhu_2026]
- [Öztürk et al 2026][research_ozturk_2026]

[research_abhishek_hari_2026]: https://doi.org/10.55041/ijsrem.fce001
[research_abraham_1963]: https://doi.org/10.2514/6.1963-2899
[research_adam_king_1965]: https://doi.org/10.1007/bf02327532
[research_adams_stoll_1969]: https://ntrs.nasa.gov/citations/19690027905
[research_agarwal_2025]: https://doi.org/10.1016/j.engfracmech.2025.111448
[research_aguiar_2025]: https://doi.org/10.1590/1679-7825/e8427
[research_ajeesh_2026]: https://doi.org/10.1016/j.est.2026.120861
[research_allen_1966]: https://ntrs.nasa.gov/citations/19660045863
[research_almetwally_2026]: https://doi.org/10.1002/qre.70299
[research_amiro_1962]: https://doi.org/10.21236/ad0295442
[research_apatovskii_1967]: https://doi.org/10.1007/bf00559980
[research_appar_kumar_2021]: https://doi.org/10.1080/10618562.2021.2017900
[research_azizi_dornisch_2025]: https://doi.org/10.1016/j.finel.2025.104416
[research_babcock_sechler_1962]: https://ntrs.nasa.gov/citations/19630000943
[research_babcock_sechler_1963]: https://ntrs.nasa.gov/citations/19630008791
[research_bahiman_thole_1965]: https://doi.org/10.21236/ada451677
[research_ballentine_1966]: https://doi.org/10.21236/ad0637506
[research_baneviciene_2026]: https://doi.org/10.1080/14751798.2026.2683157
[research_beer_lennox_1965]: https://ntrs.nasa.gov/citations/19660004121
[research_bell_1965]: https://doi.org/10.21236/ad0631590
[research_benfriha_2026]: https://doi.org/10.51485/ajss.v11i2.293
[research_berg_1968]: https://doi.org/10.21236/ad0833157
[research_bershadskyi_2022]: https://doi.org/10.33950/spacetech-2308-7625-2022-1-56-69
[research_bigham_puri_2025]: https://doi.org/10.1016/j.jsse.2025.07.006
[research_binion_1962]: https://doi.org/10.21236/ad0290303
[research_binion_w_1964]: https://doi.org/10.21236/ad0439948
[research_bohne_1964]: https://doi.org/10.2514/6.1964-1029
[research_borelli_carroll_1967]: https://doi.org/10.2514/6.1967-591
[research_botterill_1961]: https://doi.org/10.1016/0010-2180(61)90122-5
[research_boyd_1963]: https://doi.org/10.21236/ad0299033
[research_bozich_1967]: https://doi.org/10.21236/ad0656302
[research_buell_1964]: https://doi.org/10.2514/6.1964-1017
[research_cha_2024]: https://doi.org/10.3390/s24092798
[research_cha_ko_2025]: https://doi.org/10.2514/1.a36337
[research_chaabani_2025]: https://doi.org/10.1007/s00707-025-04322-9
[research_chehrzad_khoramishad_2026]: https://doi.org/10.1177/14759217261455647
[research_chen_2025]: https://doi.org/10.1007/s11071-025-11829-2
[research_cheng_2025]: https://doi.org/10.1016/j.cryogenics.2025.104098
[research_chitwood_1962]: https://doi.org/10.4271/620375
[research_christie_2026]: https://doi.org/10.58567/eal05010002
[research_chung_2026]: https://doi.org/10.32473/space.2.1.142127
[research_coffin_1970]: https://ntrs.nasa.gov/citations/19720013170
[research_cooper_1961]: https://doi.org/10.2514/8.5546
[research_coppa_nash_1962]: https://doi.org/10.21236/ad0295491
[research_coppa_nash_1964]: https://doi.org/10.21236/ad0610514
[research_coxe_tatom_1962]: https://doi.org/10.1007/978-1-4757-0531-7_29
[research_crandall_mark_1963]: https://doi.org/10.1016/b978-1-4832-3259-1.50005-8
[research_crandall_mark_1963_2]: https://doi.org/10.1016/b978-1-4832-3259-1.50006-x
[research_crandall_mark_1963_3]: https://doi.org/10.1016/b978-1-4832-3259-1.50007-1
[research_crose_1965]: https://doi.org/10.2514/6.1965-1202
[research_dafler_1962]: https://doi.org/10.1119/1.1941784
[research_dalle_2024]: https://doi.org/10.2514/1.a35809
[research_das_padmanabhan_2022]: https://doi.org/10.1016/j.jppr.2022.07.003
[research_diegoca_1961]: https://doi.org/10.21236/ad0843112
[research_digiovanii_dugundji_1965]: https://doi.org/10.21236/ad0617269
[research_ding_2025]: https://doi.org/10.1016/j.ijpvp.2025.105563
[research_div_1966]: https://doi.org/10.21236/ada028047
[research_dolgopolov_nikolayev_2024]: https://doi.org/10.1007/s12567-024-00541-3
[research_dolton_reed_1966]: https://doi.org/10.2514/6.1966-424
[research_du_2025]: https://doi.org/10.1007/s42423-025-00187-1
[research_du_groh_2026]: https://doi.org/10.1016/j.tws.2025.114379
[research_edwards_2023]: https://doi.org/10.1016/j.addma.2022.103300
[research_elliott_rau_1968]: https://ntrs.nasa.gov/citations/19680037547
[research_engineering_2024]: https://doi.org/10.14775/ksmpe.2024.23.04.009
[research_erdogan_tekin_2025]: https://doi.org/10.1142/s0219455426503839
[research_eshete_2024]: https://doi.org/10.1016/j.jweia.2024.105843
[research_evkin_2026]: https://doi.org/10.1016/j.tws.2025.114153
[research_faulkner_1961]: https://doi.org/10.21236/ad0265426
[research_faulkner_ward_1961]: https://doi.org/10.21236/ad0266582
[research_feodosiev_siniarev_1959]: https://doi.org/10.1016/b978-1-4832-3201-0.50013-9
[research_fernando_charalambous_2026]: https://doi.org/10.1126/science.adz4676
[research_frazier_1967]: https://ntrs.nasa.gov/citations/19670050873
[research_gao_2024]: https://doi.org/10.1016/j.ast.2024.109671
[research_gashe_2025]: https://doi.org/10.3390/ma18184286
[research_ge_2026]: https://doi.org/10.1007/s10999-026-09927-z
[research_gerald_runyan_1962]: https://doi.org/10.4271/620491
[research_gerasimov_2025]: https://doi.org/10.7868/s3034612625040048
[research_ghio_cerri_2026]: https://doi.org/10.1002/adem.202502199
[research_goldman_miessner_1965]: https://doi.org/10.1177/003754976500400504
[research_goldman_miessner_1966]: https://doi.org/10.1177/003754976600600117
[research_gong_2024]: https://doi.org/10.3390/aerospace11020121
[research_gong_2026]: https://doi.org/10.3390/act15060295
[research_greenfield_1960]: https://doi.org/10.1007/978-1-4684-3105-6_15
[research_greenspon_1963]: https://doi.org/10.21236/ad0429850
[research_grey_1953]: https://doi.org/10.21236/ad0036007
[research_guo_2026]: https://doi.org/10.3724/j.issn.2096-9287.2025.20250091
[research_harrje_1959]: https://doi.org/10.21236/ad0212816
[research_hausrath_dittoe_1962]: https://ntrs.nasa.gov/citations/19630000935
[research_he_2024]: https://doi.org/10.1088/1742-6596/2764/1/012061
[research_hegg_1964]: https://ntrs.nasa.gov/citations/19650011485
[research_hill_1969]: https://doi.org/10.2514/6.1969-548
[research_hines_1966]: https://doi.org/10.21236/ad0642490
[research_hoff_1942]: https://doi.org/10.2514/8.10872
[research_hoff_1962]: https://doi.org/10.21236/ad0400282
[research_horing_2025]: https://doi.org/10.2514/1.t7165
[research_hu_2025]: https://doi.org/10.3390/aerospace12080677
[research_huang_2025_2]: https://doi.org/10.1142/s0219455427501173
[research_humphrey_1961]: https://doi.org/10.1007/978-1-4757-0534-8_29
[research_hung_hunt_1964]: https://doi.org/10.2514/6.1964-1043
[research_hurtado_2026]: https://doi.org/10.1177/14759217251411530
[research_ichino_takahashi_1965]: https://doi.org/10.1299/jsme1958.8.169
[research_im_2025]: https://doi.org/10.1109/access.2025.3631840
[research_ivanco_2024]: https://doi.org/10.2514/1.a35930
[research_jalaja_2024]: https://doi.org/10.1007/s11668-023-01835-0
[research_jayan_2024]: https://doi.org/10.4271/2024-26-0452
[research_jeon_2024]: https://doi.org/10.1016/j.oceaneng.2024.117173
[research_jiao_2023]: https://doi.org/10.1142/s0219455423501973
[research_jin_2025]: https://doi.org/10.1115/1.4068383
[research_jo_ahn_2022]: https://doi.org/10.1016/j.ast.2022.107703
[research_johnson_kelsen_1969]: https://doi.org/10.1520/stp45893s
[research_jones_farmer_1966]: https://doi.org/10.2514/6.1966-1735
[research_jones_farmer_1967]: https://doi.org/10.2514/3.28838
[research_juarez_1961]: https://doi.org/10.21236/ad0607874
[research_kamenskii_martirosov_2021]: https://doi.org/10.34759/vst-2021-2-46-53
[research_kaplan_1961]: https://doi.org/10.2514/8.5635
[research_karman_tsien_1941]: https://doi.org/10.2514/8.10722
[research_kaufman_1958]: https://doi.org/10.2514/8.7521
[research_keast_1961]: https://doi.org/10.21236/ad0273892
[research_kempner_chen_1974]: https://doi.org/10.1111/j.2164-0947.1974.tb01564.x
[research_kern_lubin_1963]: https://doi.org/10.21236/ad0403681
[research_khamlak_2026]: https://doi.org/10.37547/tajet/book-26-01
[research_khil_chevskii_kadyshev_1973]: https://doi.org/10.1007/bf00762829
[research_kim_2025]: https://doi.org/10.5139/jksas.2025.53.10.1027
[research_komle_2025]: https://doi.org/10.1016/j.pss.2025.106216
[research_kuentz_1969]: https://doi.org/10.1520/stp45895s
[research_kumar_2023]: https://doi.org/10.61653/joast.v74i4.2022.45
[research_kundu_mukhopadhyay_2025]: https://doi.org/10.34133/space.0308
[research_larson_1965]: https://doi.org/10.2514/6.1965-306
[research_layachi_2025]: https://doi.org/10.1590/jatm.v17.1374
[research_leaumont_1965]: https://ntrs.nasa.gov/citations/19650014222
[research_lee_2024]: https://doi.org/10.6108/kspe.2024.28.2.023
[research_lee_2026]: https://doi.org/10.3390/aerospace13010079
[research_lee_2026_2]: https://doi.org/10.3390/aerospace13020169
[research_lee_baek_2026]: https://doi.org/10.6108/kspe.2026.30.3.070
[research_lei_2025]: https://doi.org/10.1134/s0869864324060222
[research_leng_2026]: https://doi.org/10.1016/j.ijhydene.2025.152583
[research_lenihan_1962]: https://doi.org/10.1088/0031-9112/13/10/007
[research_li_2024_3]: https://doi.org/10.1109/taes.2024.3440281
[research_li_2025_2]: https://doi.org/10.1088/3050-2454/ae0b71
[research_li_2026]: https://doi.org/10.1109/access.2026.3667479
[research_liao_2023]: https://doi.org/10.1061/jaeeez.aseng-4668
[research_lin_2025]: https://doi.org/10.1016/j.tws.2025.112960
[research_liu_2020]: https://doi.org/10.2514/1.a34551
[research_liu_2025]: https://doi.org/10.1016/j.oceaneng.2025.121674
[research_liu_2025_4]: https://doi.org/10.12688/digitaltwin.17824.1
[research_liu_2026]: https://doi.org/10.1016/j.matdes.2026.116280
[research_liu_2026_3]: https://doi.org/10.34133/space.0368
[research_liu_yuan_2025]: https://doi.org/10.1007/s11665-025-10659-y
[research_loewy_1965]: https://doi.org/10.2514/6.1965-1147
[research_louw_kearsley_2026]: https://doi.org/10.1177/14759217251405396
[research_lu_2026]: https://doi.org/10.3390/en19092109
[research_lu_cao_2025]: https://doi.org/10.1063/5.0270983
[research_lu_cao_2025_2]: https://doi.org/10.1016/j.oceaneng.2025.122526
[research_lu_cao_2026]: https://doi.org/10.1016/j.oceaneng.2026.126641
[research_lubowe_1965]: https://doi.org/10.2514/3.28135
[research_luca_2026]: https://doi.org/10.1016/j.tws.2026.115232
[research_luders_2025]: https://doi.org/10.1016/j.dib.2025.111333
[research_luo_2025]: https://doi.org/10.1080/10589759.2025.2548374
[research_luo_2026]: https://doi.org/10.1080/10589759.2026.2616433
[research_macpherson_1963]: https://doi.org/10.21236/ad0403872
[research_mandell_white_1960]: https://doi.org/10.1007/978-1-4757-0537-9_14
[research_manning_price_1961]: https://ntrs.nasa.gov/citations/20040006332
[research_marchetti_minisci_2021]: https://doi.org/10.3390/math9161868
[research_marcus_1969]: https://doi.org/10.2514/6.1969-547
[research_matthews_1957]: https://doi.org/10.21236/ad0127419
[research_mcculloch_1960]: https://doi.org/10.1520/stp45922s
[research_mescall_1961]: https://doi.org/10.21236/ad0254653
[research_michielsen_1948]: https://doi.org/10.2514/8.11706
[research_miller_1967]: https://doi.org/10.2514/6.1967-44
[research_miller_gerus_1966]: https://doi.org/10.4271/660676
[research_mitra_2021]: https://doi.org/10.1007/s42423-021-00073-6
[research_moore_1958]: https://doi.org/10.21236/ad0404839
[research_morey_koshar_1961]: https://doi.org/10.1016/b978-0-12-395682-8.50010-8
[research_morgado_2022]: https://doi.org/10.2514/1.j061071
[research_mow_sadowsky_1962]: https://doi.org/10.21236/ad0286039
[research_mukherjee_2025]: https://doi.org/10.1080/10589759.2025.2575884
[research_mullin_2025]: https://doi.org/10.1016/j.addma.2025.104985
[research_murphy_1961]: https://doi.org/10.1016/0032-0633(61)90141-6
[research_murphy_rubesin_1965]: https://ntrs.nasa.gov/citations/19660010795
[research_muthukumar_2020]: https://doi.org/10.14429/dsj.70.13708
[research_naca_1966]: https://ntrs.nasa.gov/citations/19660022936
[research_naca_1975]: https://ntrs.nasa.gov/citations/19750000135
[research_narayanaswamy_2025]: https://doi.org/10.1007/s40964-025-01036-1
[research_nardo_sadler_1962]: https://doi.org/10.21236/ad0273837
[research_nast_williams_1967]: https://doi.org/10.1007/978-1-4757-0489-1_24
[research_navaz_ntantis_2026]: https://doi.org/10.1007/s12567-026-00740-0
[research_nein_head_1962]: https://doi.org/10.1007/978-1-4757-0531-7_30
[research_neumaier_2025]: https://doi.org/10.3390/aerospace12050412
[research_newton_makrides_1954]: https://doi.org/10.21236/ad0039437
[research_ni_2026]: https://doi.org/10.1088/1742-6596/3254/2/022008
[research_nickell_1961]: https://doi.org/10.21236/ad0619097
[research_nikonchuk_2026]: https://doi.org/10.15407/pmach2026.02.022
[research_nolan_1964]: https://doi.org/10.4095/325184
[research_nott_1963]: https://doi.org/10.21236/ad0297244
[research_olave_2023]: https://doi.org/10.1016/j.ast.2023.108358
[research_ostner_1962]: https://doi.org/10.21236/ad0414825
[research_ozoigbo_2025]: https://doi.org/10.1134/s0025654425602733
[research_ozturk_2026]: https://doi.org/10.1016/j.jastp.2026.106829
[research_paczek_2023]: https://doi.org/10.3390/ma16186259
[research_paleti_2026]: https://doi.org/10.1016/j.tws.2025.114422
[research_pan_2026]: https://doi.org/10.1111/ffe.70293
[research_panda_2025]: https://doi.org/10.2514/1.a36078
[research_parkyn_1958]: https://doi.org/10.2307/3610466
[research_pei_2021]: https://doi.org/10.2514/1.a35024
[research_peshkhoev_2026]: https://doi.org/10.32326/1814-9146-2026-88-1-48-57
[research_peters_hall_1963]: https://doi.org/10.21236/ad0403115
[research_peterson_1960]: https://ntrs.nasa.gov/citations/20040016415
[research_platus_1967]: https://doi.org/10.21236/ad0810587
[research_polivanov_sidorenko_2026]: https://doi.org/10.3390/aerospace13020120
[research_porenta_2025]: https://doi.org/10.1016/j.tws.2024.112825
[research_powell_1962]: https://doi.org/10.21236/ad0424725
[research_prasad_2022]: https://doi.org/10.13111/2066-8201.2022.14.1.10
[research_punga_campbell_1962]: https://doi.org/10.2514/8.9711
[research_qiu_2023]: https://doi.org/10.1016/j.tws.2023.110871
[research_qiu_2026]: https://doi.org/10.1016/j.engfailanal.2026.110912
[research_radovcich_1965]: https://doi.org/10.2514/6.1965-1406
[research_raji_2019]: https://doi.org/10.1088/1742-6596/1355/1/012020
[research_ramdani_2026]: https://doi.org/10.35261/barometer.v11i2.13190
[research_randall_1970]: https://doi.org/10.2514/3.29945
[research_reddy_2026]: https://doi.org/10.1016/j.tws.2026.115204
[research_ren_2025]: https://doi.org/10.1016/j.ast.2025.110080
[research_ren_2025_2]: https://doi.org/10.1016/j.cja.2025.103621
[research_reynolds_1960]: https://doi.org/10.21236/ad0491094
[research_rhee_2025]: https://doi.org/10.1016/j.jer.2025.01.008
[research_rieck_2026]: https://doi.org/10.1007/s13272-026-00991-x
[research_rindal_dahm_1967]: https://doi.org/10.2172/12817504
[research_roberts_wilhem_1964]: https://doi.org/10.21236/ad0604407
[research_rockefeller_alfred_1960]: https://doi.org/10.21236/ada637368
[research_roithmayr_pei_2024]: https://doi.org/10.2514/1.a35791
[research_rubin_1965]: https://doi.org/10.2514/6.1965-1151
[research_rubin_1966]: https://doi.org/10.2514/3.28626
[research_rudd_2024]: https://doi.org/10.2514/1.j063617
[research_russell_1964]: https://doi.org/10.2514/6.1964-242
[research_sadovsky_2024]: https://doi.org/10.1016/j.engstruct.2024.117934
[research_sahu_2024]: https://doi.org/10.1063/5.0229933
[research_saiki_2026]: https://doi.org/10.29322/ijsrp.16.05.2026.p17329
[research_samadzadeh_2024]: https://doi.org/10.1016/j.heliyon.2024.e36319
[research_samuelson_1968]: https://doi.org/10.1115/1.3604693
[research_scherberg_rubin_1953]: https://doi.org/10.21236/ad0012619
[research_schurmann_1957]: https://doi.org/10.2514/8.12965
[research_schweppe_1964]: https://doi.org/10.21236/ad0609524
[research_scott_1963]: https://doi.org/10.21236/ad0410255
[research_sellers_1948]: https://doi.org/10.2514/8.4244
[research_sharma_2024]: https://doi.org/10.1063/5.0191101
[research_shaw_1952]: https://doi.org/10.21236/ad0219218
[research_simon_1965]: https://doi.org/10.2514/6.1965-1146
[research_singh_2026]: https://doi.org/10.1016/j.ast.2025.111549
[research_slider_1967]: https://doi.org/10.2118/1765-ms
[research_slifka_1960]: https://doi.org/10.1109/jrproc.1960.287405
[research_snodgrass_1955]: https://doi.org/10.2514/8.6860
[research_snyder_1974]: https://ntrs.nasa.gov/citations/19750032829
[research_solomon_tamiru_2026]: https://doi.org/10.11648/j.rd.20260703.11
[research_song_2026]: https://doi.org/10.2514/1.g009701
[research_sree_2025]: https://doi.org/10.55248/gengpi.6.0325.1222
[research_stancil_1963]: https://doi.org/10.2514/6.1963-223
[research_steeves_1975]: https://doi.org/10.21236/ada010702
[research_steeves_1975_2]: https://doi.org/10.21236/ada006493
[research_stephens_1965]: https://doi.org/10.2514/6.1965-1114
[research_stetson_1964]: https://doi.org/10.2514/6.1964-433
[research_stinson_gross_1972]: https://ntrs.nasa.gov/citations/19730004116
[research_su_2026]: https://doi.org/10.1080/23307706.2025.2556335
[research_summerfield_1960]: https://doi.org/10.1515/9781400879953-005
[research_sun_2024]: https://doi.org/10.1016/j.jfranklin.2024.106849
[research_sun_2026]: https://doi.org/10.1016/j.asr.2026.02.102
[research_tan_2023]: https://doi.org/10.1016/j.actaastro.2023.02.004
[research_tantaroudas_karachalios_2026]: https://doi.org/10.24132/acm.2026.1114
[research_tao_qi_2025]: https://doi.org/10.1080/27525783.2026.2620942
[research_tariq_2026]: https://doi.org/10.3390/pr14152458
[research_thielemann_1962]: https://ntrs.nasa.gov/citations/19630000948
[research_thomas_2022]: https://doi.org/10.1016/j.jmapro.2021.12.037
[research_thompson_2025]: https://doi.org/10.1080/09349847.2025.2580247
[research_tian_2025]: https://doi.org/10.1016/j.cej.2025.169346
[research_tonko_lambiase_2024]: https://doi.org/10.1093/europace/euae102.358
[research_tozawa_1969]: https://doi.org/10.4262/denkiseiko.40.126
[research_trushlyakov_2024]: https://doi.org/10.1016/j.cja.2023.09.018
[research_tyzzer_pernet_1964]: https://doi.org/10.21236/ad0601611
[research_ugural_cheng_1968]: https://doi.org/10.2514/3.4501
[research_velmurugan_buragohain_2023]: https://doi.org/10.61653/joast.v59i4.2007.584
[research_ventura_2023]: https://doi.org/10.1016/j.tws.2023.110835
[research_vilceanu_2024]: https://doi.org/10.1016/j.rineng.2024.102435
[research_vreeland_1960]: https://doi.org/10.1520/stp45923s
[research_wachi_gilmartin_1966]: https://doi.org/10.21236/ad0488914
[research_wagenblast_bettinger_2024]: https://doi.org/10.1016/j.jsse.2024.10.001
[research_walters_1967]: https://doi.org/10.21236/ad0658064
[research_walton_simmons_1962]: https://doi.org/10.21236/ad0286392
[research_wang_1953]: https://doi.org/10.21236/ad0013969
[research_wang_1966]: https://doi.org/10.21236/ad0648078
[research_wang_1973]: https://doi.org/10.1016/0045-7949(73)90058-8
[research_wang_2024_2]: https://doi.org/10.1016/j.jweia.2024.105849
[research_wang_2026]: https://doi.org/10.1016/j.jmatprotec.2025.119192
[research_wang_2026_2]: https://doi.org/10.1016/j.ast.2026.111915
[research_wang_2026_3]: https://doi.org/10.1002/srin.202501238
[research_wang_2026_4]: https://doi.org/10.1016/j.tws.2025.114068
[research_wang_chen_2022]: https://doi.org/10.1016/j.jweia.2022.104982
[research_wang_ramamritham_1947]: https://doi.org/10.2514/8.1498
[research_webb_2026]: https://doi.org/10.1016/j.ast.2026.112231
[research_weingarten_1962]: https://doi.org/10.2514/8.9608
[research_weiss_goodman_1960]: https://doi.org/10.1007/978-1-4757-0537-9_18
[research_wertheimer_1957]: https://doi.org/10.1119/1.1934474
[research_whitcombe_1961]: https://doi.org/10.21236/ad0259865
[research_whitcombe_1961_2]: https://doi.org/10.21236/ad0266445
[research_wilner_1960]: https://doi.org/10.1109/jrproc.1960.287484
[research_winstead_1966]: https://ntrs.nasa.gov/citations/19990115798
[research_wood_1961]: https://doi.org/10.21236/ad0421632
[research_wu_2026]: https://doi.org/10.1016/j.amf.2026.200305
[research_xu_2025]: https://doi.org/10.3390/act14110565
[research_xu_2025_5]: https://doi.org/10.1016/j.cryogenics.2025.104058
[research_xu_xu_2024]: https://doi.org/10.1088/1742-6596/2756/1/012038
[research_yadav_gautam_2025]: https://doi.org/10.1038/s41598-025-94081-3
[research_yang_2022]: https://doi.org/10.1088/1742-6596/2235/1/012015
[research_yang_2026_2]: https://doi.org/10.3390/aerospace13050408
[research_yang_chen_2025]: https://doi.org/10.1142/s0219455427710015
[research_yao_2022]: https://doi.org/10.3390/aerospace10010032
[research_yenugula_2025]: https://doi.org/10.1088/1742-6596/3066/1/012004
[research_yoon_2021]: https://doi.org/10.6108/kspe.2021.25.1.001
[research_yu_2023]: https://doi.org/10.1109/taes.2023.3235867
[research_yu_2024]: https://doi.org/10.3390/math12172742
[research_yu_2024_2]: https://doi.org/10.1016/j.cja.2024.06.006
[research_yu_2026]: https://doi.org/10.54254/2753-8818/2026.dl33570
[research_yu_2026_2]: https://doi.org/10.1016/j.applthermaleng.2026.131248
[research_yun_liu_2023]: https://doi.org/10.1088/1742-6596/2489/1/012037
[research_zahn_2025]: https://doi.org/10.3390/aerospace12050415
[research_zainel_saiedy_2025]: https://doi.org/10.64753/jcasc.v10i4.3507
[research_zhang_2022]: https://doi.org/10.1504/ijvd.2022.124871
[research_zhang_2024_4]: https://doi.org/10.1016/j.jweia.2024.105918
[research_zhang_2025_2]: https://doi.org/10.1016/j.ijheatmasstransfer.2024.126565
[research_zhang_2025_3]: https://doi.org/10.1088/1757-899x/1327/1/012158
[research_zhang_2025_5]: https://doi.org/10.1177/13694332241310673
[research_zhang_2025_7]: https://doi.org/10.1016/j.energy.2025.135365
[research_zhang_2026]: https://doi.org/10.1016/j.tca.2026.180248
[research_zhang_2026_2]: https://doi.org/10.1016/j.engfracmech.2025.111736
[research_zhang_he_2024]: https://doi.org/10.1007/s40194-024-01744-2
[research_zhao_2022]: https://doi.org/10.1016/j.applthermaleng.2022.118794
[research_zhao_2024]: https://doi.org/10.1016/j.actaastro.2023.10.035
[research_zhao_2025_2]: https://doi.org/10.1007/s10921-025-01186-w
[research_zhao_2026]: https://doi.org/10.1016/j.measurement.2026.122217
[research_zhao_tan_2026]: https://doi.org/10.1016/j.actaastro.2026.01.008
[research_zhou_2022]: https://doi.org/10.5293/ijfms.2022.15.3.355
[research_zhou_2024]: https://doi.org/10.1016/j.ifacol.2025.01.136
[research_zhou_2025]: https://doi.org/10.3390/aerospace12030203
[research_zhou_2025_2]: https://doi.org/10.1016/j.tws.2025.113196
[research_zhu_2026]: https://doi.org/10.1016/j.ress.2026.112209
