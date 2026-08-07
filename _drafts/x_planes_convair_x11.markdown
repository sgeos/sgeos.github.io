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

It is also the vehicle the previous article was about without naming. The [X-10][related_post_a307_north_american_x10] was the testbed for the Navaho, an intercontinental cruise missile that was cancelled in July 1957 because a ballistic weapon of the same range arrives in about thirty-two minutes where an airbreathing one is exposed for a hundred and seventy-two. **The X-11 is that ballistic weapon.** It is the Atlas A, the first flying article of the programme that killed the Navaho, and it first flew on 11 June 1957, four weeks before the cancellation message. The standard inventory entry is [Jenkins Landis and Miller 2003 American X-Vehicles, An Inventory X-1 to X-50][book_jenkins_landis_miller_2003], the vehicle compilation is [Miller 2001 The X-Planes, X-1 to X-45][book_miller_2001], and the structural principle has its own literature under the name [balloon tank][ref_balloon_tank].

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

or 15.7 percent of the ideal velocity, which is a reasonable figure for gravity and drag losses on a vertical-rising ballistic ascent and is adopted here as a calibration rather than derived. With it fixed, the structural mass can be varied and carried all the way through to a range. Holding the propellant load constant and scaling only the structure,

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

The caution the table requires is that the loss figure was calibrated so the baseline reproduces the previous article's ten thousand kilometres, so the first row is fixed by construction. The **sensitivity** is the result, not the absolute range, and the sensitivity is robust because it depends on the logarithm rather than on the calibration.

### The Keystone Is Exercised Early, Which Is Why This Testbed Worked

The [X-10][related_post_a307_north_american_x10] flew for twenty-eight minutes against a mission of a hundred and seventy-two, and the article's central result was that its keystone quantity, a gyroscope drift rate, accumulates with time and therefore could not be measured over so short a window. The X-11 has the opposite property and it is worth stating plainly because it is the sharpest contrast the series has yet produced.

**The Atlas structure is fully loaded within the first two minutes of flight.** Maximum dynamic pressure occurs about a minute after lift-off, the highest axial acceleration occurs at booster cutoff, and both fall inside a 133 second burn. The two loads can be written as fractions of the mission and the comparison is stark. For the Atlas the structurally sizing events occur at

$$\frac{t_{\text{sizing}}}{t_{\text{mission}}} = \frac{133}{1932} = 0.069$$

taking the mission as the 1932 second ballistic flight time derived in the previous article, so **the structure is finished being tested seven percent of the way through the mission**. For the X-10 the corresponding ratio was

$$\frac{t_{\text{flown}}}{t_{\text{mission}}} = \frac{1653}{10{,}333} = 0.16$$

and the keystone was still not exercised, because a drift rate is not a load. **The X-11 tested more of its keystone in seven percent of its mission than the X-10 did in sixteen percent of its**, which is the compact form of the whole comparison. A flight that goes no further than a hundred and twenty kilometres of apogee and a fifth of the intercontinental burnout speed still applies every structural load the mission will ever apply. **A keystone that is exercised early can be validated cheaply. A keystone that accumulates cannot.** The X-11 flew a fraction of the weapon's mission and tested its keystone completely, and the X-10 flew a fraction of its weapon's mission and tested its keystone hardly at all, and the difference is not programme competence but the mathematical character of the quantity each was built to establish.

## Programme Origin

Convair had been working on long-range missiles since 1946 under project MX-774, a study that the Air Force cancelled in 1947 and that Convair partly continued on its own money. The work resumed as MX-1593 in 1951 and became the Atlas. The design authority throughout was Karel Bossart, whose contribution is the pressure-stabilised tank and whose reported inspiration was a cylindrical party balloon.

The German inheritance that shaped the American ballistic effort generally is [Neufeld 1995 The Rocket and the Reich][book_neufeld_1995], and the institutional history of the Air Force missile and space organisation is [Walker Bernstein and Lang 2005 Seize the High Ground][book_walker_powell_2005]. **The point worth holding is that Convair reached the pressure-stabilised structure from an aircraft background rather than from a rocket one.** A company that builds thin-skinned pressurised fuselages has the instinct that a pressure vessel can be a primary structure, and the monocoque analysis the field already had is [Hoff 1942][research_hoff_1942], [Wang and Ramamritham 1947][research_wang_ramamritham_1947], and [Kaufman 1958][research_kaufman_1958].

The programme designation the record actually uses is **WS 107A-1**, and the missile family became SM-65 with variants lettered A through F. The X-11 designation was assigned to the Atlas A and the X-12 to the Atlas B, which the next article treats. **Whether either designation was ever used operationally is not clear from the accessible record**, and the Epistemic State says so. What is clear is that these are the fourth and fifth consecutive X numbers attached to vehicles that were never research aircraft, following the [X-8][related_post_a305_aerojet_x8], the [X-9][related_post_a306_bell_x9], and the [X-10][related_post_a307_north_american_x10], and that the pattern the previous article identified, of a separate series being absorbed rather than of the X-series broadening on the merits, now has more cases than it had exceptions.

### The One-and-a-Half Stage Arrangement

The Atlas carries three engines and jettisons two of them. All three ignite on the ground, and at booster cutoff the two outboard engines and their skirt are dropped while the sustainer continues on the same tanks. The arrangement exists because igniting a large liquid engine at altitude was not trusted in 1955, so the vehicle stages its **engines** without staging its **tanks**.

That decision interacts directly with the keystone. A conventional two-stage vehicle discards a whole tank set, which is where most of the structural benefit of staging comes from. The Atlas discards only engines and skirt, so it gets a smaller staging benefit and has to make it up in structural efficiency. **The balloon tank and the one-and-a-half stage arrangement are the same decision seen twice**, since the vehicle that cannot drop its tanks must make its tanks weigh almost nothing. Staging optimisation of the period is [Schurmann 1957][research_schurmann_1957], [Parkyn 1958][research_parkyn_1958], and [Wertheimer 1957][research_wertheimer_1957], with the gravitational term in [Sellers 1948][research_sellers_1948].

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

which has a consequence every pressure vessel shares. **The hoop direction is always the first to yield, so a tank that bursts splits along its length rather than around its circumference**, and the weld that runs longitudinally is therefore the one that decides the vehicle.

At a flight tank pressure of about 60 pounds per square inch and the heavy gauge this gives

$$\sigma_{\theta} = \frac{413{,}685 \times 1.524}{0.000940} = 671 \, \text{MPa}$$

against a yield near 965 megapascals for the material in its extra-full-hard condition, a margin of 1.44. At the light gauge the same pressure would give

$$\sigma_{\theta} = \frac{413{,}685 \times 1.524}{0.000356} = 1773 \, \text{MPa}$$

which exceeds the ultimate strength of the material. **The light gauge therefore cannot exist anywhere the pressure is high**, and that is not a criticism of the calculation but a demonstration of the design rule. The gauge is tapered to the local stress, and the local stress is dominated not by ullage pressure but by the head of propellant above the station under acceleration,

$$\Delta p = \rho \, n \, g \, h$$

For liquid oxygen at 1141 kilogrammes per cubic metre, ten metres of head, and six times gravity near burnout,

$$\Delta p = 1141 \times 6 \times 9.80665 \times 10 = 671{,}000 \, \text{Pa} = 97 \, \text{psi}$$

which is **more than one and a half times the ullage pressure**. The bottom of the tank is the hardest-worked part of the vehicle and it is thickest there, and this is only possible at all because a membrane structure can be thinned where the load is small without any of the discontinuities that a stiffened structure would introduce. Membrane analysis of the period is [Bahiman and Thole 1965][research_bahiman_thole_1965], with monocoque ring analysis in [Hoff 1942][research_hoff_1942] and material data in [Manning and Price 1961][research_manning_price_1961], [Johnson and Kelsen 1969][research_johnson_kelsen_1969], and [Kuentz 1969][research_kuentz_1969].

### The Common Bulkhead, Which Is the Other Half of the Idea

The Atlas carries liquid oxygen and kerosene in one shell divided by a single dome rather than in two tanks with structure between them. The saving is a whole pressure dome and the intertank barrel that would separate them, and for a vehicle of this diameter that is a large fraction of the dry mass. A hemispherical dome of radius $r$ has an area of

$$A_{\text{dome}} = 2 \pi r^{2} = 2 \pi \times 1.524^{2} = 14.6 \, \text{m}^{2}$$

and an intertank barrel long enough to clear two domes adds roughly

$$A_{\text{barrel}} = 2 \pi r \times 2r = 4 \pi r^{2} = 29.2 \, \text{m}^{2}$$

so the common bulkhead removes on the order of forty square metres of shell, which at the average gauge is

$$m_{\text{saved}} = 43.8 \times 0.000648 \times 8000 = 227 \, \text{kg}$$

or **about four percent of the whole empty vehicle from one design decision**. The cost is that the bulkhead now separates a cryogen at 90 kelvin from a hydrocarbon at ambient temperature, so it must insulate as well as carry load, and a leak across it mixes the propellants inside the vehicle. **The common bulkhead is the Atlas idea that outlived the balloon tank**, and it is standard on cryogenic stages today for exactly the reason computed here.

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

**Fifty-three kilogrammes of gas holds up five thousand three hundred and ninety-five kilogrammes of steel**, a ratio of 103 to one. That single comparison is the article in one line.

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

against an empty weight of 52.9 kilonewtons, a margin of 121. **The vehicle does not fold as a column. It crumples as a shell**, and the distinction matters because the two failure modes are separated by two orders of magnitude and only one of them is helped by pressure. Shell stability work of the period is [Nickell 1961][research_nickell_1961], [Hausrath and Dittoe 1962][research_hausrath_dittoe_1962], [Hoff et al 1962][research_hoff_1962], and [Bozich 1967][research_bozich_1967], with the external-pressure case in [Shaw et al 1952][research_shaw_1952] and dynamic buckling in [Coppa and Nash 1962][research_coppa_nash_1962].

### What Five Pounds per Square Inch Buys

Internal pressure produces axial tension, and a fibre that is in tension cannot buckle. The tension from the standing nitrogen pressure alone is

$$\sigma_{z} = \frac{34{,}474 \times 1.524}{2 \times 0.000940} = 27.9 \, \text{MPa}$$

at the heavy gauge and 73.9 megapascals at the light one. Set those against the knocked-down buckling allowables of 14.4 and 5.5 megapascals respectively and the result is stark. **Five pounds per square inch of nitrogen roughly doubles the effective compressive capability of the heavy gauge and multiplies the light gauge by more than thirteen.** The pressure is not a convenience. It is the larger part of the structure.

The relation can also be inverted, and inverting it explains where the number five came from. Requiring the axial tension from pressure to equal the knocked-down buckling allowable gives

$$p_{\text{req}} = \frac{2 t \sigma_{\text{allow}}}{r}$$

which at the heavy gauge is

$$p_{\text{req}} = \frac{2 \times 0.000940 \times 14.4 \times 10^{6}}{1.524} = 17{,}768 \, \text{Pa} = 2.58 \, \text{psi}$$

and at the light gauge only 0.37 pounds per square inch, because the buckling allowable falls faster with thickness than the pressure tension does. **The governing case is the heavy gauge and it needs 2.58 pounds per square inch, so the reported five-pound standing specification carries a margin of 1.94 on the calculation performed here.** A specification that lands at roughly twice the computed requirement is what a designer writes when the computed requirement rests on a knockdown factor he does not trust, which is exactly the situation described above.

The cleanest statement of the principle is in bending rather than in compression. For a thin-walled cylinder the second moment of area is $I = \pi r^{3} t$, so a bending moment produces an extreme-fibre stress of $M r / I$. Setting that equal to the axial tension from pressure gives the moment at which the most compressed fibre first reaches zero stress,

$$\frac{M r}{\pi r^{3} t} = \frac{p r}{2 t} \quad \Longrightarrow \quad M_{\text{crit}} = \frac{\pi p r^{3}}{2}$$

**The thickness cancels.** The moment a pressure-stabilised cylinder can carry before any part of it goes into compression depends on the pressure and the radius and not at all on how thin the skin is, which is the mathematical form of the claim that the pressure is doing the work. At the standing pressure this is

$$M_{\text{crit}} = \frac{\pi \times 34{,}474 \times 1.524^{3}}{2} = 0.192 \, \text{MN m}$$

equivalent to a lateral force of 8.3 kilonewtons at the top of a 23 metre vehicle, and at flight pressure it is 2.30 meganewton metres, or 99.5 kilonewtons. **The vehicle standing on the pad in a wind is held up by a pressure a bicycle tyre would find low**, and the flight case is twelve times stiffer because the tanks are pressurised harder once loaded. Pressure-stabilised beams under load are treated directly by [Steeves 1975][research_steeves_1975] and [Steeves 1975, A Linear Analysis of the Deformati][research_steeves_1975_2], the effect of internal pressure on cylinder buckling specifically is [Weingarten 1962][research_weingarten_1962], and collapse tests of pressurised membrane-like cylinders are [Leaumont 1965][research_leaumont_1965], with monocoque dome stability in [Adam and King 1965][research_adam_king_1965].

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

**The tensile allowable is sixty-seven times the compressive one.** That factor does not translate directly into a mass ratio, because the two walls carry different loads and the stiffened one adds material in a different place, but it is the reason the comparison comes out the way it does and it is the number a designer in 1951 would have been looking at.

## Dependent Systems

### The Engines, and Why Three of Them Start on the Ground

The Atlas A carried two booster engines developing 341,128 pounds of thrust between them, which is 1.517 meganewtons. At the Atlas gross mass this is a lift-off thrust-to-weight of

$$\frac{T}{W} = \frac{1.517 \times 10^{6}}{117{,}900 \times 9.80665} = 1.31$$

and the propellant flow follows from the exhaust velocity,

$$\dot{m} = \frac{T}{v_{e}} = \frac{1.517 \times 10^{6}}{2765} = 549 \, \text{kg/s}$$

so a 133 second burn consumes 73.0 tonnes, which is 65 percent of the full Atlas propellant load. Liquid engine practice of the period is [Summerfield 1960][research_summerfield_1960], with a released Rocketdyne specification of the same line in [Scott 1963][research_scott_1963] and the specific-impulse bookkeeping in [Dafler 1962][research_dafler_1962]. Combustion instability, which was the era's most persistent liquid-engine problem, is [Grey 1953][research_grey_1953], [Matthews 1957][research_matthews_1957], and [Harrje 1959][research_harrje_1959]. Gimbal actuation for thrust vector control is [Hegg 1964][research_hegg_1964].

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

**The vehicle therefore meets its worst bending load and its worst axial load at different times**, which is fortunate, because a pressure-stabilised structure that had to carry both at once would need a pressure it could not contain. Ascent load analysis of the period is [Wood 1961][research_wood_1961], with the aerodynamic side in [Binion et al 1962][research_binion_1962].

Angle of attack is what turns dynamic pressure into a bending moment. The normal force on a slender body at small incidence is

$$N = q S C_{N\alpha} \alpha$$

and taking the reference area as the cross-section, $S = \pi r^{2} = 7.30$ square metres, a normal-force slope of two per radian, and three degrees of incidence at maximum dynamic pressure,

$$N = 9736 \times 7.30 \times 2 \times 0.0524 = 7447 \, \text{N}$$

which acting at a lever arm of ten metres gives a bending moment of 74 kilonewton metres. Against the pressure-stabilised capacity of 2.30 meganewton metres at flight pressure this is **three percent**, so the vehicle has an enormous margin in bending while pressurised and essentially none while not. The incidence comes from wind. A vehicle rising through a shear layer sees a lateral relative wind and must either fly at an angle to it, which costs bending moment, or steer into it, which costs trajectory. That trade is the reason load-relief steering exists and it is treated below in its modern form.

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

which is 87 percent of the assumed yield, so the proof test is a genuine test and not a formality. Structural testing of large articles as the period practised it is [Abraham 1963][research_abraham_1963]. **The design's failure mode is its own acceptance test**, and that is a real and rarely stated advantage of the balloon tank over a stiffened shell whose critical load can only be estimated.

### The Thermal Environment, Which Is Mild by the Standards of This Series

The [X-10][related_post_a307_north_american_x10] article computed a recovery temperature of 636 kelvin for a vehicle cruising at Mach 3.25 for three hours, and concluded that aluminium would not serve. A ballistic booster has the opposite problem. It passes through the dense atmosphere quickly and is out of it before the skin can equilibrate,

$$\tau_{\text{skin}} = \frac{\rho c \delta}{h}$$

and for stainless steel at the Atlas gauge, taking a density of 8000 kilogrammes per cubic metre, a specific heat of 500 joules per kilogramme kelvin, and a convective coefficient of 200 watts per square metre kelvin,

$$\tau_{\text{skin}} = \frac{8000 \times 500 \times 0.00094}{200} = 18.8 \, \text{s}$$

which is comparable to the time spent near maximum dynamic pressure rather than short against it. **The skin does partially equilibrate, but it does so against a recovery temperature that is only high for a few tens of seconds**, and the propellant behind it is a very large heat sink at cryogenic temperature. The structural problem is therefore mechanical rather than thermal, which is the reverse of every vehicle in this series since the [X-2][related_post_a299_bell_x2]. Aerodynamic heating of entry vehicles is [Allen 1966][research_allen_1966] and [Murphy and Rubesin 1965][research_murphy_rubesin_1965], and the thermal control of a cryogenic vehicle is [Winstead 1966][research_winstead_1966], with propellant leakage effects in [Nast and Williams 1967][research_nast_williams_1967].

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

so **a hundred and fifty-three decibels is a pressure fluctuation of about 0.13 pounds per square inch**, which is small against the sixty inside the tank but is applied at hundreds of hertz for the duration of the lift-off transient, and fatigue does not care about the mean. Vibration environment specification and correlation is [Snyder et al 1974][research_snyder_1974], and the acoustic measurement practice of the period is [Keast 1961][research_keast_1961].

### Slosh, Which a Balloon Tank Makes Worse

A tank with no internal structure has nothing to break up the free surface of its propellant, and a large moving mass of liquid inside a vehicle being steered by thrust vectoring couples into the control loop. **The same decision that removed the stringers removed the natural baffling**, so baffles had to be added back deliberately as the one internal structure the design admits.

The frequency that matters is the first lateral sloshing mode of a cylindrical tank, which for fill depths that are not shallow is

$$\omega_{s} = \sqrt{\frac{1.841 \, g_{\text{eff}}}{r} \tanh \frac{1.841 h}{r}}$$

and under acceleration the effective gravity is the axial load factor times $g$, so **the slosh frequency rises through the flight as the vehicle accelerates and falls as the tank drains**. At the Atlas radius and a load factor of three the deep-tank limit gives

$$\omega_{s} = \sqrt{\frac{1.841 \times 3 \times 9.80665}{1.524}} = 5.96 \, \text{rad/s}$$

or 0.95 hertz, which sits uncomfortably close to the bandwidth of a thrust-vector control loop. Slosh damping by flexible baffles is [Stephens 1965][research_stephens_1965], with measurement in [Wilner et al 1960][research_wilner_1960] and the shell-vibration side in [DIGiovanii and Dugundji 1965][research_digiovanii_dugundji_1965].

### Pogo, Which Is the Structure and the Propulsion Talking to Each Other

A liquid rocket whose structure has a longitudinal mode near the frequency at which its feed system and engine respond can close a loop through the propellant column, and the vehicle oscillates along its own axis. The mechanism is [Rubin 1965][research_rubin_1965] and [Rubin 1966][research_rubin_1966], the naming and early study are [Goldman and Miessner 1965][research_goldman_miessner_1965] and [Goldman and Miessner 1966][research_goldman_miessner_1966], the accumulator remedy is [Marcus et al 1969][research_marcus_1969], and the best-known case is [Hill et al 1969][research_hill_1969] on Saturn V. **A pressure-stabilised vehicle is unusually exposed to this**, because its longitudinal stiffness is partly a function of tank pressure and therefore changes as the tanks drain.

The scale of the problem is set by how soft the vehicle is. A solid steel bar of the same length has a fixed-free axial mode at

$$f_{1} = \frac{c}{4L} = \frac{1}{4L} \sqrt{\frac{E}{\rho}} = \frac{4912}{4 \times 23.11} = 53 \, \text{Hz}$$

but a launch vehicle is not a solid bar. It is a thin shell containing a large mass of liquid, and its first axial mode sits an order of magnitude lower, in the region of twenty hertz, which is uncomfortably close to the response of a feed system and turbopump. **The instability condition is that the structural mode and the propulsion response overlap in frequency with enough gain around the loop**, and both quantities move during the flight, the structure because the tanks drain and the propulsion because the inlet pressure falls. Missile structural dynamics of the period is [Wood 1961][research_wood_1961], with clustered-vehicle bending in [Loewy 1965][research_loewy_1965] and shell vibration in [DIGiovanii and Dugundji 1965][research_digiovanii_dugundji_1965].

### Guidance, Which the Atlas A Did Not Carry

The Atlas A flew without an operational guidance system. Its flights were programmed, and the guidance question belonged to later variants and to the radio-inertial system the early Atlas used before an all-inertial set replaced it. Ballistic missile guidance of the period is [Whitcombe 1961][research_whitcombe_1961], field testing of such a system is [Slifka 1960][research_slifka_1960], the measurement problem of establishing where a missile actually went is [Cooper 1961][research_cooper_1961], and a later integrated formulation is [Russell 1964][research_russell_1964] with [Larson 1965][research_larson_1965] on Titan III.

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

**The reentry body is decelerated at sixty-four times gravity while the booster that launched it never exceeded three and a half.** The two halves of a ballistic missile are different structural problems by a factor of nearly twenty, which is the reason they are different articles built by different people, and the reason the X-11 could be a complete test of one while carrying none of the other. Nose-cone and ablation work of the period is [Stetson 1964][research_stetson_1964], [Wachi and Gilmartin 1966][research_wachi_gilmartin_1966], and [Rindal and Dahm 1967][research_rindal_dahm_1967], with hemispherical-nose heat transfer in [Nardo and Sadler 1962][research_nardo_sadler_1962], flight heating measurements in [Snodgrass 1955][research_snodgrass_1955], and the roll-resonance problem in [Platus 1967][research_platus_1967].

### Ground Handling, Which the Structure Dictates

A vehicle that collapses unpressurised cannot be handled like an aeroplane. It requires a nitrogen supply at every point in its life, transport fixtures that support it without imposing a bending moment above the pressure-stabilised limit computed above, and a launch complex that keeps it inflated while it is fuelled. **The structural decision propagates into buildings and vehicles and procedures**, and the accessible record of that apparatus is unusually good, in [General Dynamics Convair 1966][research_div_1966] and its companion volumes and in [Peters and Hall 1963][research_peters_hall_1963] on system-test data for the engine system.

The propellant loading problem deserves its own note, because a balloon tank couples loading to structure in a way a conventional tank does not. Filling the tank changes the pressure the walls must hold, changes the mass the walls must carry, and changes the temperature of the material, and all three happen while the vehicle is standing unsupported on a pad. **Loading is a structural operation and not merely a fluid transfer.** Optimum propellant loading and utilisation is [Whitcombe 1961, Optimum Propellant Loading And Pro][research_whitcombe_1961_2], and ground support equipment practice of the period is [Moore 1958][research_moore_1958] and [Newton and Makrides 1954][research_newton_makrides_1954], with launch complex activation in [Powell 1962][research_powell_1962].

The boil-off that follows is a second coupling, and its rate explains why topping continues until moments before launch. With a wetted area of

$$A = 2 \pi r L = 2 \pi \times 1.524 \times 18 = 172 \, \text{m}^{2}$$

an uninsulated tank at a convective coefficient of ten watts per square metre kelvin against a two hundred kelvin difference admits

$$\dot{Q} = h A \Delta T = 10 \times 172 \times 200 = 345 \, \text{kW}$$

and at a latent heat of 213 kilojoules per kilogramme the boil-off is

$$\dot{m}_{\text{boil}} = \frac{\dot{Q}}{L_{v}} = \frac{3.45 \times 10^{5}}{2.13 \times 10^{5}} = 1.62 \, \text{kg/s}$$

or 5826 kilogrammes an hour, which is **seven and a half percent of the oxygen load every hour**. Liquid oxygen at 90 kelvin against an ambient near 290 therefore boils continuously, the tank must be topped until moments before launch, and the ullage pressure must be regulated throughout. A pressure regulation failure is a structural failure on this vehicle rather than a propulsion inconvenience, which is the recurring theme of the whole design. Pressure buildup analysis for a cryogenic tank is [Slider 1967][research_slider_1967], and two-phase pumping of cryogenic propellants is [Stinson and Gross 1972][research_stinson_gross_1972].

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

The first flight reached two kilometres and was destroyed, and the reported detail that matters for this article is that **the vehicle tumbled and the structure held**. A pressure-stabilised shell that survives a tumble at low altitude has demonstrated the one thing about it that everyone doubted, and it did so under a load case nobody designed for. A tumbling vehicle sees its bending moment applied at an arbitrary angle and reversed once per revolution, which is the worst possible use of a structure whose compressive capacity is two hundred times smaller than its tensile one. That it held is evidence that the pressure stabilisation was working exactly as the relation above says it should, since the relation does not care about the direction of the moment. A tumbling vehicle at rotation rate $\Omega$ also loads itself centrifugally, and the transverse acceleration at the tip of a body of length $L$ rotating about its centre is

$$a_{\text{tip}} = \Omega^{2} \frac{L}{2}$$

so even a slow tumble at one revolution per second gives

$$a_{\text{tip}} = (2 \pi)^{2} \times 11.6 = 458 \, \text{m/s}^{2} = 47 g$$

at the nose, applied as a bending load along the whole vehicle. **The structure that everyone expected to fold survived a load case nobody had designed for.**

The flight-by-flight record for the operational variants is in the Flight Test Working Group reports, of which [Diegoca 1961][research_diegoca_1961] is one, and the survival-probability analysis such a programme generates is [Beer and Lennox 1965][research_beer_lennox_1965].

The failures were concentrated in propulsion and plumbing rather than in structure. The reported causes include exhaust-gas recirculation overheating the boat-tail, propellant duct failures, and pneumatic and guidance faults, and the remedies were heat shielding, steel plumbing in place of lighter material, and revised venting. **The programme's difficulty was never the thing that looked impossible.**

### What a Fifty Percent Success Rate Means

Four of eight is a success rate of 0.5, which sounds alarming and is normal for a first flight article. What the number actually supports is narrow. Treating the flights as independent Bernoulli trials, the standard error on the estimate is

$$\sigma_{\hat{p}} = \sqrt{\frac{p(1-p)}{n}} = \sqrt{\frac{0.25}{8}} = 0.177$$

so the estimate is 0.50 plus or minus about 0.18, and any true reliability between roughly 0.15 and 0.85 is consistent with the observation. **Eight flights cannot distinguish a mediocre vehicle from a good one**, and the programme knew it, which is why Atlas B followed immediately rather than after a verdict.

The width of that interval is itself the argument for flying often, and the relation makes it explicit. Halving the interval requires quadrupling the flights,

$$n = \frac{p (1-p)}{\sigma_{\hat{p}}^{2}}$$

so an estimate good to five percentage points at a true reliability near one half needs

$$n = \frac{0.25}{0.05^{2}} = 100 \, \text{flights}$$

which no ballistic missile programme was ever going to fly as development articles. **Reliability for such a vehicle is therefore established by inference from ground test and by accumulating operational rounds, not by the flight test programme**, and the Difficulties Review volumes of [General Dynamics Convair 1966][research_div_1966] are what that inference actually looks like when written down.

## Comparison With Ground Prediction

The Atlas structure was tested on the ground more thoroughly than most, because a pressure-stabilised tank can be proof-tested to its actual failure mode simply by pressurising it, which is not true of a stiffened shell whose failure mode is compressive buckling under a load that is hard to apply. **The design is unusually testable on the ground for the same reason it is unusual in flight.**

The gap between ground and flight is therefore not in the structure but in the combined environment. A tank can be pressure-tested, a shell can be buckling-tested, and neither test applies the acoustic field, the vibration, the thermal gradient, and the axial acceleration at once. Shell-buckling experiment of the period is [Nickell 1961][research_nickell_1961] and [Leaumont 1965][research_leaumont_1965], and the standing difficulty that experiments scatter far below theory is the subject of [Karman and Tsien 1941][research_karman_tsien_1941] and remains the reason a knockdown factor exists at all.

The scatter deserves a number, because it is the largest single uncertainty in the article. Experimental buckling loads for cylinders in this range of radius to thickness fall between roughly fifteen and sixty percent of the classical value,

$$0.15 \leq \frac{\sigma_{\exp}}{\sigma_{cr}} \leq 0.60 \qquad \frac{0.60}{0.15} = 4$$

a spread of four to one, and the design factor of 0.20 used above sits at

$$\frac{0.20 - 0.15}{0.60 - 0.15} = 0.11$$

or the eleventh percentile of the observed band, which is to say very near the worst case observed. **A structure designed against a four-to-one experimental scatter is being designed against ignorance rather than against a load**, and the pressure-stabilised solution sidesteps the whole difficulty by arranging that no fibre goes into compression at all. That is the deepest sense in which the balloon tank is not merely lighter but epistemically cleaner. Its failure mode is yield, which is predictable to a few percent, rather than buckling, which is not. The standard treatments are [Timoshenko and Gere 1961 Theory of Elastic Stability][book_timoshenko_gere_1961] and [Brush and Almroth 1975 Buckling of Bars, Plates and Shells][book_brush_almroth_1975], with vehicle structural practice in [Bruhn 1973 Analysis and Design of Flight Vehicle Structures][book_bruhn_1973].

## What the Data Changed

### Into Atlas, and Then Into Everything

The X-11 fed directly into the Atlas B, which is the [X-12][ref_series_close] and the next article, and thence into the operational Atlas D, E, and F. The line then did something no other early ballistic missile did. **It became a launch vehicle and stayed one for sixty years.** Atlas launched Mercury, the Agena upper stage, and a long series of planetary missions, and the balloon-tank principle carried into the Centaur upper stage, which still uses it.

The reason it could is arithmetic rather than sentiment. Circular orbital speed at two hundred kilometres is

$$v_{\text{orb}} = \sqrt{\frac{\mu}{R_{e} + h}} = \sqrt{\frac{3.986 \times 10^{14}}{6.571 \times 10^{6}}} = 7788 \, \text{m/s}$$

against the 7193 metres per second an intercontinental trajectory needs, a difference of

$$v_{\text{orb}} - v_{bo} = 595 \, \text{m/s}$$

or seven percent of the ideal velocity. **An intercontinental ballistic missile is already ninety-two percent of the way to orbit**, and the remaining eight percent is a small upper stage. That is why every early space programme was built on a ballistic missile and why none was built on a cruise missile, and it is the deepest reason the Atlas outlived the Navaho by six decades.

Trajectory optimisation for the Atlas and Agena combination is [Frazier 1967][research_frazier_1967], and the control systems that a large launch vehicle of the following generation required are [Borelli and Carroll 1967][research_borelli_carroll_1967].

**The reason the Atlas became a launcher and the Navaho became nothing is worth stating in the terms this pair of articles has established.** A booster is a machine for adding velocity, and velocity is useful for any mission that needs it. A cruise missile is a machine for carrying a warhead a particular distance at a particular speed, and nothing else wants that. The Atlas survived its own obsolescence as a weapon because its keystone quantity, mass fraction, is valuable to every customer, while the Navaho's keystone quantity, sustained autonomous navigation accuracy, was valuable only to the mission that was cancelled.

### What It Did Not Change

The pressure-stabilised structure did not become the standard way to build launch vehicles. Almost everything since is a conventionally stiffened aluminium or composite structure, accepting a worse mass fraction in exchange for a vehicle that can be set down empty, handled without a nitrogen cart, and inspected without a pressure regime. **The Atlas won its argument and then lost it**, and the reason is that mass fraction stopped being the binding constraint once vehicles grew and staging improved, while handling cost never stopped mattering.

## The Contemporary Literature

### Shell Buckling, Where the Knockdown Factor Is Finally Being Replaced

The design allowable used above is a blanket factor applied to a classical result, which is an admission that the theory does not predict the experiment. That has been the state of the art since [Karman and Tsien 1941][research_karman_tsien_1941] and it is now being dismantled in favour of methods that model the imperfection instead of hiding behind a factor.

Imperfection sensitivity as a computed rather than assumed quantity is [Evkin 2026][research_evkin_2026], the asymptotic numerical route to pressurised-cylinder buckling is [Ventura et al 2023][research_ventura_2023], stochastic and dynamic treatments are [Yu et al 2024][research_yu_2024] and [Ozoigbo et al 2025][research_ozoigbo_2025], thin-walled behaviour under combined loading is [Jiao et al 2023][research_jiao_2023], and gauge-sensitivity methods for assessing and mitigating buckling risk are [Zhang 2022][research_zhang_2022]. **The most directly relevant modern paper derives knockdown factors for common-bulkhead structures**, which is the Atlas configuration exactly, in [Lee et al 2024][research_lee_2024]. Grid-stiffened composite cylinders, which are the design the Atlas rejected, are [Velmurugan and Buragohain 2023][research_velmurugan_buragohain_2023], and multiscale buckling-aware design is [Liu et al 2026][research_liu_2026].

### Propellant Tanks, Where the Rocket Equation Has Not Changed

Tank structure remains the place where launch-vehicle mass is won and lost, and the modern literature is dominated by cryogenics rather than by kerosene because the propellants moved. Structural design optimisation of a launch vehicle propellant tank is [Kim et al 2025][research_kim_2025], the common-bulkhead arrangement the Atlas pioneered is [Zhang et al 2025, Improving storage performance of a][research_zhang_2025_2] and [Zhang et al 2025, Feasibility study on synthermal st][research_zhang_2025_3], thermo-structural analysis with vacuum insulation is [Yenugula et al 2025][research_yenugula_2025], all-composite cryogenic tanks are [Rhee et al 2025][research_rhee_2025], concurrent coupled analysis is [Cheng et al 2025][research_cheng_2025], and verification of a tank operational-pressure model is [Bershadskyi et al 2022][research_bershadskyi_2022]. **The common bulkhead is the Atlas idea that survived without argument**, since it removes an entire pressure dome and the intertank structure with it, and it is now standard where the balloon tank is not.

### Slosh and Pogo, Which Are Now Designed Against Rather Than Discovered

Both phenomena were discovered in flight during the period this article covers and are now predicted before it. Slosh effects and baffle requirements are [Solomon and Tamiru 2026][research_solomon_tamiru_2026] and [Pei 2021][research_pei_2021]. Pogo has a large current literature, with model reduction for suppression design in [Zhao and Tan 2026][research_zhao_tan_2026], adaptive active suppression in [Zhao et al 2024][research_zhao_2024] and [Tan et al 2023][research_tan_2023], nonlinear modelling in [Dolgopolov and Nikolayev 2024][research_dolgopolov_nikolayev_2024], suppressor hardware in [Yoon et al 2021][research_yoon_2021] and [Mitra et al 2021][research_mitra_2021], the strap-on configuration in [Liu et al 2020][research_liu_2020], and stability analysis in [Raji et al 2019][research_raji_2019]. **That an instability first met on a 1960s vehicle still supports an active design literature is a measure of how tightly propulsion and structure are coupled in a thin-walled liquid rocket**, and a pressure-stabilised vehicle is the extreme case because its axial stiffness is partly pressure.

### Ascent Loads and Load Relief, Which Became a Control Problem

The bending moment computed above is a load the vehicle can also steer away from, and doing so is now an optimisation rather than a fixed programme. Convex and concave optimisation of the ascent is [Sun et al 2024][research_sun_2024], approximate analytical ascent solutions are [Yu et al 2023][research_yu_2023] and [Yu et al 2024, Approximate analytical solutions f][research_yu_2024_2], rolling active load relief is [He et al 2024][research_he_2024], learned load-relief attitude control is [Zhou et al 2025][research_zhou_2025], dynamic ascent load estimation for a winged vehicle is [Jayan et al 2024][research_jayan_2024], and computational fluid dynamics for ascent is [Dalle et al 2024][research_dalle_2024] with Reynolds-number and aeroelastic scaling in [Ivanco et al 2024][research_ivanco_2024]. **The X-11 flew a fixed pitch programme and absorbed whatever bending moment the wind imposed**, which is the option available to a vehicle with no way to measure its own angle of attack in real time.

### Engines and Health Monitoring, Which Is Where the Failures Actually Were

Four of eight Atlas A flights failed and the failures were propulsion and plumbing. That is now the most instrumented part of a launch vehicle. Fault diagnosis of the startup transient is [Cha et al 2024][research_cha_2024], general fault-factor health monitoring is [Cha and Ko 2025][research_cha_ko_2025], current-state monitoring is [Kamenskii and Martirosov 2021][research_kamenskii_martirosov_2021], the priming pressure surge that damages feed systems is [Das and Padmanabhan 2022][research_das_padmanabhan_2022], turbopump flow behaviour is [Zhou et al 2022][research_zhou_2022], thrust control is [Yao et al 2022][research_yao_2022], and thrust vector control appears in [Benfriha et al 2026][research_benfriha_2026] and [Saiki et al 2026][research_saiki_2026]. **The Atlas A programme diagnosed its failures by reading telemetry and inspecting wreckage.** A modern vehicle carries the diagnosis aboard.

### Reliability Estimation, Which Answers the Question Eight Flights Could Not

The binomial interval computed above is wide because eight is a small number, and the modern discipline addresses exactly that. Statistical reliability estimation for launch vehicles is [Wagenblast and Bettinger 2024][research_wagenblast_bettinger_2024], reliability design and management on an operational vehicle is [Li et al 2025, Reliability design and management][research_li_2025_2], system reliability estimation for a control system is [Muthukumar et al 2020][research_muthukumar_2020], and safety and operational reliability methodology is [Khamlak 2026][research_khamlak_2026]. **The methods now used to certify a vehicle on a handful of flights are the methods the Atlas A programme needed and did not have.**

### Manufacture, Where a Thin Welded Shell Is Still Difficult

The Atlas skin is a welded stainless assembly at a gauge where welding distortion is comparable to the thickness. Fatigue of welded joints in thin-walled structure is [Płaczek et al 2023][research_paczek_2023] and [Qiu et al 2023][research_qiu_2023], high-frequency mechanical impact treatment of welds is [Zhang and He 2024][research_zhang_he_2024], microstructure modelling in duplex stainless is [Edwards et al 2023][research_edwards_2023], springback and cold-roll forming of shells is [Engineering 2024][research_engineering_2024], and additive manufacture of stainless for rocket application is [Thomas 2022][research_thomas_2022]. The period's own difficulties with the same material are [Nolan 1964][research_nolan_1964], [Apatovskii et al 1967][research_apatovskii_1967], [Tozawa 1969][research_tozawa_1969], and [Khil'chevskii and Kadyshev 1973][research_khil_chevskii_kadyshev_1973].

### Reentry, Which the X-11 Did Not Carry and Which Is Again Contested

Reentry aerothermodynamics is [Morgado et al 2022][research_morgado_2022] and [Sharma et al 2024][research_sharma_2024], ablation at the fluid-solid interface is [Appar and Kumar 2021][research_appar_kumar_2021], reachability of a manoeuvring reentry body is [Webb et al 2026][research_webb_2026] and [Su et al 2026][research_su_2026], learned guidance for a reentry vehicle is [Marchetti and Minisci 2021][research_marchetti_minisci_2021], and the defensive problem of identifying what is coming is [Tonko and Lambiase 2024][research_tonko_lambiase_2024]. **This is the same argument the [previous article][related_post_a307_north_american_x10] found revived in the hypersonic glide literature**, approached from the other end.

## Where the Framing Breaks Down

Treating the X-11 through the mass-fraction keystone illuminates the design but misleads in three ways.

**It was not a complete missile.** No operational guidance, no reentry vehicle, no warhead, and a range a fifth of the requirement. The X-11 is the airframe and the booster propulsion and nothing else.

**The structure was not the programme's actual difficulty.** Four of eight flights failed, and the failures were plumbing, heating, and pneumatics. An article organised around the balloon tank gives the impression that the daring part was the hard part, and the flight record says the opposite.

**Mass fraction stopped being binding.** The keystone that justified the design is the reason the design was abandoned, since later vehicles could afford heavier structure and could not afford the handling.

**The mass figures are not the vehicle's own.** The structural fraction, the mass ratio, and everything computed from them use Atlas D numbers, because Atlas A mass data was not found in the accessible record. The Atlas A was heavier and less capable than the D and the range table therefore describes the family rather than the article that flew. The Epistemic State repeats this, and it is the largest single weakness in the quantitative argument.

## The Source Base

The contrast with the previous article is sharp and it is worth stating as a controlled result.

**The Navaho record is absent from the defence archive and the Atlas record is present.** The [X-10][related_post_a307_north_american_x10] article established that querying the Defense Technical Information Center through the Crossref publisher prefix on the project number MX-770 returns nothing about the Navaho at all, while the adjacent MX-776 returns a RASCAL weapon system report. The same route on the Atlas returns the Flight Test Working Group reports for individual missiles, the multi-volume Difficulties Review of the Atlas booster and its ground support systems, propellant-loading system design, and engine system-test data. **Same archive, same route, same query form, and the difference is that one programme was cancelled in 1957 and the other flew for sixty years.**

The aerospace archive holds the structural literature rather than the vehicle, which suits this article because the keystone is a structural principle and not a vehicle detail. The shell-buckling and pressure-stabilisation literature is large, contemporary with the design, and directly applicable.

**What is thin is the X-11 as such.** The designation appears in compilations and the flight record is well attested, but the accessible record concerns the Atlas A rather than a vehicle called X-11, and no document found for this article uses the X designation. That is the fourth consecutive article in which the X number is an administrative label rather than a name anyone used, and the pattern identified in the [previous article][related_post_a307_north_american_x10] now has more instances than the series has counterexamples in this stretch.

**The mass data is the specific gap.** Gross, empty, and propellant masses for the Atlas A itself were not found, so the article uses Atlas D figures throughout and says so wherever they appear. Since the Atlas A was an earlier and heavier article, the structural fraction used here is better than the fraction the X-11 actually achieved, and every range figure derived from it is correspondingly optimistic. The direction of the error is known even though its size is not, which is the most that can be said.

## Epistemic State

**Historical fact, well supported.** Eight Atlas A vehicles flew from Cape Canaveral between 11 June 1957 and 3 June 1958, four successfully, from Launch Complexes 12 and 14, with apogees near 120 kilometres. The programme designation was WS 107A-1 and the design authority was Karel Bossart at Convair. The structure is pressure-stabilised 301 stainless steel between 0.014 and 0.037 inches thick. The vehicle requires about five pounds per square inch of nitrogen when unfuelled and collapses without it. The Atlas uses a one-and-a-half stage arrangement in which two booster engines and a skirt are jettisoned and the sustainer continues on the same tanks. The Navaho was cancelled on 12 July 1957, four weeks after the first Atlas A flight.

**Reported but from compilations rather than programme documents.** The X-11 and X-12 designations for Atlas A and Atlas B. The masses used here, which are Atlas D figures rather than Atlas A figures, since Atlas A mass data was not found. The 282 second specific impulse and 133 second burn time. The flight-by-flight apogees and outcomes. The reported failure causes.

**Engineering analysis, derived here and independently checkable.** The radius-to-thickness ratios and the drink-can comparison. The membrane stresses and the demonstration that the light gauge cannot exist at full pressure. The acceleration head and its ratio to ullage pressure. The classical buckling stresses and the knocked-down allowables. The axial tension from standing pressure and its ratio to those allowables. The critical bending moment and its independence of thickness. The mass fractions, mass ratio, and ideal velocity. The loss calibration and the range sensitivity table. The thrust-to-weight, propellant flow, and burn consumption. The skin mass. The binomial standard error on the success rate.

**Inference, argued but not established.** That the balloon tank and the one-and-a-half stage arrangement are the same decision seen twice. That the X-11's keystone being exercised early is why a short flight sufficed, in contrast to the X-10. That pressure-stabilised vehicles are unusually exposed to pogo because longitudinal stiffness varies with tank pressure. That the design was abandoned because handling cost outlasted the mass-fraction constraint.

**Assumptions made explicit.** A flight tank pressure of 60 pounds per square inch, which is representative rather than sourced. Material properties for 301 extra-full-hard stainless steel of 965 megapascals yield, 1276 ultimate, and 193 gigapascals modulus. A knockdown factor of 0.2 to 0.3. A tank length of 18 metres and a steel density of 8000 kilogrammes per cubic metre. Ten metres of liquid oxygen head at six times gravity. The gravity and drag loss of 1337 metres per second, which is calibrated rather than derived and which fixes the first row of the range table by construction.

## Out of Scope

The Atlas B, C, D, E, and F, of which the B is the next article. The reentry vehicle and the warhead. The radio-inertial and later all-inertial guidance systems in any depth. Silo and coffin basing. The Atlas as a space launch vehicle beyond noting that it became one. Centaur. The MX-774 predecessor beyond its role in the origin. Comparative economics against Titan and Minuteman.

## Conclusion

The X-11 is a fuel tank that flies. Its skin is thinner in proportion than a drink can, its compressive strength is two hundred times smaller than its tensile strength, and it is held up by a pressure a bicycle tyre would find low. **Every one of those facts is a consequence of one relation**, which is that the rocket equation returns velocity logarithmically in mass ratio, so a weapon that must reach ten thousand kilometres has to spend its structural budget as though it were the last money it had.

The article's own arithmetic puts a number on it. Making the structure half as efficient turns an intercontinental missile into an intermediate-range one, and no amount of better engine or better trajectory recovers it. Bossart's balloon was not a clever trick. It was the only available answer to a question that had been posed in the form of a logarithm.

There is a second result and it belongs to the series rather than to the vehicle. **The X-10 could not test its keystone in twenty-eight minutes and the X-11 tested its keystone completely in two**, and the difference is that a structural load is applied in full early and a drift rate accumulates. The two vehicles are separated by one designation and four weeks, they were built by rival contractors for the same mission, and the reason one testbed worked and the other did not has nothing to do with either company. It is a property of the quantity being measured, and it is the sort of thing that only becomes visible when the vehicles are read in order.

## References

### Books

[book_bruhn_1973]: https://openlibrary.org/search?q=Bruhn+Analysis+and+Design+of+Flight+Vehicle+Structures
[book_brush_almroth_1975]: https://openlibrary.org/search?q=Brush+Almroth+Buckling+of+Bars+Plates+and+Shells
[book_jenkins_landis_miller_2003]: https://openlibrary.org/search?q=Jenkins+Landis+Miller+American+X+Vehicles
[book_miller_2001]: https://openlibrary.org/search?q=Miller+The+X+Planes+X-1+to+X-45
[book_neufeld_1995]: https://openlibrary.org/search?q=Neufeld+The+Rocket+and+the+Reich
[book_sutton_biblarz_2016]: https://openlibrary.org/search?q=Sutton+Biblarz+Rocket+Propulsion+Elements
[book_timoshenko_gere_1961]: https://openlibrary.org/search?q=Timoshenko+Gere+Theory+of+Elastic+Stability
[book_walker_powell_2005]: https://openlibrary.org/search?q=Walker+Bernstein+Lang+Seize+the+High+Ground

### Reference

[ref_balloon_tank]: https://en.wikipedia.org/wiki/Balloon_tank
[ref_series_close]: https://en.wikipedia.org/wiki/SM-65B_Atlas
[ref_x11]: https://en.wikipedia.org/wiki/SM-65A_Atlas

### Research

[research_abraham_1963]: https://doi.org/10.2514/6.1963-2899
[research_adam_king_1965]: https://doi.org/10.1007/bf02327532
[research_allen_1966]: https://ntrs.nasa.gov/citations/19660045863
[research_apatovskii_1967]: https://doi.org/10.1007/bf00559980
[research_appar_kumar_2021]: https://doi.org/10.1080/10618562.2021.2017900
[research_bahiman_thole_1965]: https://doi.org/10.21236/ada451677
[research_beer_lennox_1965]: https://ntrs.nasa.gov/citations/19660004121
[research_benfriha_2026]: https://doi.org/10.51485/ajss.v11i2.293
[research_bershadskyi_2022]: https://doi.org/10.33950/spacetech-2308-7625-2022-1-56-69
[research_binion_1962]: https://doi.org/10.21236/ad0290303
[research_binion_w_1964]: https://doi.org/10.21236/ad0439948
[research_borelli_carroll_1967]: https://doi.org/10.2514/6.1967-591
[research_bozich_1967]: https://doi.org/10.21236/ad0656302
[research_cha_2024]: https://doi.org/10.3390/s24092798
[research_cha_ko_2025]: https://doi.org/10.2514/1.a36337
[research_cheng_2025]: https://doi.org/10.1016/j.cryogenics.2025.104098
[research_cooper_1961]: https://doi.org/10.2514/8.5546
[research_coppa_nash_1962]: https://doi.org/10.21236/ad0295491
[research_dafler_1962]: https://doi.org/10.1119/1.1941784
[research_dalle_2024]: https://doi.org/10.2514/1.a35809
[research_das_padmanabhan_2022]: https://doi.org/10.1016/j.jppr.2022.07.003
[research_diegoca_1961]: https://doi.org/10.21236/ad0843112
[research_digiovanii_dugundji_1965]: https://doi.org/10.21236/ad0617269
[research_div_1966]: https://doi.org/10.21236/ada028047
[research_dolgopolov_nikolayev_2024]: https://doi.org/10.1007/s12567-024-00541-3
[research_edwards_2023]: https://doi.org/10.1016/j.addma.2022.103300
[research_engineering_2024]: https://doi.org/10.14775/ksmpe.2024.23.04.009
[research_evkin_2026]: https://doi.org/10.1016/j.tws.2025.114153
[research_feodosiev_siniarev_1959]: https://doi.org/10.1016/b978-1-4832-3201-0.50013-9
[research_frazier_1967]: https://ntrs.nasa.gov/citations/19670050873
[research_goldman_miessner_1965]: https://doi.org/10.1177/003754976500400504
[research_goldman_miessner_1966]: https://doi.org/10.1177/003754976600600117
[research_grey_1953]: https://doi.org/10.21236/ad0036007
[research_harrje_1959]: https://doi.org/10.21236/ad0212816
[research_hausrath_dittoe_1962]: https://ntrs.nasa.gov/citations/19630000935
[research_he_2024]: https://doi.org/10.1088/1742-6596/2764/1/012061
[research_hegg_1964]: https://ntrs.nasa.gov/citations/19650011485
[research_hill_1969]: https://doi.org/10.2514/6.1969-548
[research_hoff_1942]: https://doi.org/10.2514/8.10872
[research_hoff_1962]: https://doi.org/10.21236/ad0400282
[research_ivanco_2024]: https://doi.org/10.2514/1.a35930
[research_jayan_2024]: https://doi.org/10.4271/2024-26-0452
[research_jiao_2023]: https://doi.org/10.1142/s0219455423501973
[research_johnson_kelsen_1969]: https://doi.org/10.1520/stp45893s
[research_kamenskii_martirosov_2021]: https://doi.org/10.34759/vst-2021-2-46-53
[research_karman_tsien_1941]: https://doi.org/10.2514/8.10722
[research_kaufman_1958]: https://doi.org/10.2514/8.7521
[research_keast_1961]: https://doi.org/10.21236/ad0273892
[research_khamlak_2026]: https://doi.org/10.37547/tajet/book-26-01
[research_khil_chevskii_kadyshev_1973]: https://doi.org/10.1007/bf00762829
[research_kim_2025]: https://doi.org/10.5139/jksas.2025.53.10.1027
[research_kuentz_1969]: https://doi.org/10.1520/stp45895s
[research_larson_1965]: https://doi.org/10.2514/6.1965-306
[research_leaumont_1965]: https://ntrs.nasa.gov/citations/19650014222
[research_lee_2024]: https://doi.org/10.6108/kspe.2024.28.2.023
[research_li_2025_2]: https://doi.org/10.1088/3050-2454/ae0b71
[research_liu_2020]: https://doi.org/10.2514/1.a34551
[research_liu_2026]: https://doi.org/10.1016/j.matdes.2026.116280
[research_loewy_1965]: https://doi.org/10.2514/6.1965-1147
[research_manning_price_1961]: https://ntrs.nasa.gov/citations/20040006332
[research_marchetti_minisci_2021]: https://doi.org/10.3390/math9161868
[research_marcus_1969]: https://doi.org/10.2514/6.1969-547
[research_matthews_1957]: https://doi.org/10.21236/ad0127419
[research_michielsen_1948]: https://doi.org/10.2514/8.11706
[research_mitra_2021]: https://doi.org/10.1007/s42423-021-00073-6
[research_moore_1958]: https://doi.org/10.21236/ad0404839
[research_morgado_2022]: https://doi.org/10.2514/1.j061071
[research_murphy_rubesin_1965]: https://ntrs.nasa.gov/citations/19660010795
[research_muthukumar_2020]: https://doi.org/10.14429/dsj.70.13708
[research_nardo_sadler_1962]: https://doi.org/10.21236/ad0273837
[research_nast_williams_1967]: https://doi.org/10.1007/978-1-4757-0489-1_24
[research_newton_makrides_1954]: https://doi.org/10.21236/ad0039437
[research_nickell_1961]: https://doi.org/10.21236/ad0619097
[research_nolan_1964]: https://doi.org/10.4095/325184
[research_ozoigbo_2025]: https://doi.org/10.1134/s0025654425602733
[research_paczek_2023]: https://doi.org/10.3390/ma16186259
[research_parkyn_1958]: https://doi.org/10.2307/3610466
[research_pei_2021]: https://doi.org/10.2514/1.a35024
[research_peters_hall_1963]: https://doi.org/10.21236/ad0403115
[research_platus_1967]: https://doi.org/10.21236/ad0810587
[research_powell_1962]: https://doi.org/10.21236/ad0424725
[research_qiu_2023]: https://doi.org/10.1016/j.tws.2023.110871
[research_raji_2019]: https://doi.org/10.1088/1742-6596/1355/1/012020
[research_rhee_2025]: https://doi.org/10.1016/j.jer.2025.01.008
[research_rindal_dahm_1967]: https://doi.org/10.2172/12817504
[research_rubin_1965]: https://doi.org/10.2514/6.1965-1151
[research_rubin_1966]: https://doi.org/10.2514/3.28626
[research_russell_1964]: https://doi.org/10.2514/6.1964-242
[research_saiki_2026]: https://doi.org/10.29322/ijsrp.16.05.2026.p17329
[research_schurmann_1957]: https://doi.org/10.2514/8.12965
[research_scott_1963]: https://doi.org/10.21236/ad0410255
[research_sellers_1948]: https://doi.org/10.2514/8.4244
[research_sharma_2024]: https://doi.org/10.1063/5.0191101
[research_shaw_1952]: https://doi.org/10.21236/ad0219218
[research_slider_1967]: https://doi.org/10.2118/1765-ms
[research_slifka_1960]: https://doi.org/10.1109/jrproc.1960.287405
[research_snodgrass_1955]: https://doi.org/10.2514/8.6860
[research_snyder_1974]: https://ntrs.nasa.gov/citations/19750032829
[research_solomon_tamiru_2026]: https://doi.org/10.11648/j.rd.20260703.11
[research_steeves_1975]: https://doi.org/10.21236/ada010702
[research_steeves_1975_2]: https://doi.org/10.21236/ada006493
[research_stephens_1965]: https://doi.org/10.2514/6.1965-1114
[research_stetson_1964]: https://doi.org/10.2514/6.1964-433
[research_stinson_gross_1972]: https://ntrs.nasa.gov/citations/19730004116
[research_su_2026]: https://doi.org/10.1080/23307706.2025.2556335
[research_summerfield_1960]: https://doi.org/10.1515/9781400879953-005
[research_sun_2024]: https://doi.org/10.1016/j.jfranklin.2024.106849
[research_tan_2023]: https://doi.org/10.1016/j.actaastro.2023.02.004
[research_thomas_2022]: https://doi.org/10.1016/j.jmapro.2021.12.037
[research_tonko_lambiase_2024]: https://doi.org/10.1093/europace/euae102.358
[research_tozawa_1969]: https://doi.org/10.4262/denkiseiko.40.126
[research_velmurugan_buragohain_2023]: https://doi.org/10.61653/joast.v59i4.2007.584
[research_ventura_2023]: https://doi.org/10.1016/j.tws.2023.110835
[research_wachi_gilmartin_1966]: https://doi.org/10.21236/ad0488914
[research_wagenblast_bettinger_2024]: https://doi.org/10.1016/j.jsse.2024.10.001
[research_wang_ramamritham_1947]: https://doi.org/10.2514/8.1498
[research_webb_2026]: https://doi.org/10.1016/j.ast.2026.112231
[research_weingarten_1962]: https://doi.org/10.2514/8.9608
[research_wertheimer_1957]: https://doi.org/10.1119/1.1934474
[research_whitcombe_1961]: https://doi.org/10.21236/ad0259865
[research_whitcombe_1961_2]: https://doi.org/10.21236/ad0266445
[research_wilner_1960]: https://doi.org/10.1109/jrproc.1960.287484
[research_winstead_1966]: https://ntrs.nasa.gov/citations/19990115798
[research_wood_1961]: https://doi.org/10.21236/ad0421632
[research_yao_2022]: https://doi.org/10.3390/aerospace10010032
[research_yenugula_2025]: https://doi.org/10.1088/1742-6596/3066/1/012004
[research_yoon_2021]: https://doi.org/10.6108/kspe.2021.25.1.001
[research_yu_2023]: https://doi.org/10.1109/taes.2023.3235867
[research_yu_2024]: https://doi.org/10.3390/math12172742
[research_yu_2024_2]: https://doi.org/10.1016/j.cja.2024.06.006
[research_zhang_2022]: https://doi.org/10.1504/ijvd.2022.124871
[research_zhang_2025_2]: https://doi.org/10.1016/j.ijheatmasstransfer.2024.126565
[research_zhang_2025_3]: https://doi.org/10.1088/1757-899x/1327/1/012158
[research_zhang_he_2024]: https://doi.org/10.1007/s40194-024-01744-2
[research_zhao_2024]: https://doi.org/10.1016/j.actaastro.2023.10.035
[research_zhao_tan_2026]: https://doi.org/10.1016/j.actaastro.2026.01.008
[research_zhou_2022]: https://doi.org/10.5293/ijfms.2022.15.3.355
[research_zhou_2025]: https://doi.org/10.3390/aerospace12030203

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
