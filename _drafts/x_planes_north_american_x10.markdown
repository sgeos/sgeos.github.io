---
layout: post
mathjax: true
comments: true
title: "X-Planes: North American X-10"
date: 2025-10-16 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 11
---

<!-- A307 -->
<script>console.log("A307");</script>

The [North American X-10][ref_x10] started its engines on a runway, took off on its own undercarriage, climbed to fifteen kilometres, accelerated past Mach two, flew a thousand kilometres down a range, turned, came back, lowered its gear, and landed. No one was aboard for any of it. Thirteen were built and one survives. This article is the eleventh in the [X-Planes series][related_post_a297_xplanes_framing], following the [X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], the [X-4][related_post_a301_northrop_x4], the [X-5][related_post_a302_bell_x5], the [X-6][related_post_a303_convair_x6], the [X-7][related_post_a304_lockheed_x7], the [X-8][related_post_a305_aerojet_x8], and the [X-9][related_post_a306_bell_x9].

It is the third article in a row whose subject is not conventionally called an aircraft, and it is the one that makes that description hard to defend. The [X-8][related_post_a305_aerojet_x8] was a sounding rocket and the [X-9][related_post_a306_bell_x9] was an expendable missile, but the X-10 took off and landed on wheels, was flown repeatedly, and was designed from the outset to be brought home. **What separates it from an aircraft is not its shape and not its operation but its purpose**, and that purpose is worth naming precisely, because it turns out to determine everything else about the vehicle. The standard inventory entry is [Jenkins Landis and Miller 2003 American X-Vehicles, An Inventory X-1 to X-50][book_jenkins_landis_miller_2003], the designation history is [Parsch 2002 RTV-A-5 X-10][ref_parsch_x10] with the parent weapon at [Parsch 2002 SM-64][ref_parsch_sm64], the vehicle compilation is [Miller 2001 The X-Planes, X-1 to X-45][book_miller_2001], the programme monograph is [Gibson 1996 The Navaho Missile Project][book_gibson_1996], and the class history is [Werrell 1985 The Evolution of the Cruise Missile][book_werrell_1985].

## The Research Question

The X-10 was the flying testbed for the [Navaho][ref_navaho], an intercontinental supersonic cruise missile that North American Aviation developed for the Air Force under project MX-770 from 1946. The Navaho was to carry a thermonuclear warhead five thousand five hundred nautical miles at a Mach number near three and arrive close enough to the target to destroy it. Every part of that sentence was hard, but only one part had never been done at all.

### The Binding Constraint Is Time, Not Speed

Every previous vehicle in this series answered a question that could be asked in a few minutes of flight. The [X-1][related_post_a298_bell_x1] needed seconds at Mach one. The [X-2][related_post_a299_bell_x2] needed a few minutes above Mach three. The [X-7][related_post_a304_lockheed_x7] needed a ramjet to run long enough to measure it. Even the [X-8][related_post_a305_aerojet_x8], whose whole existence was about observing time above the atmosphere, worked in units of hundreds of seconds.

The Navaho mission is different in kind. At the design range of the enlarged XSM-64A and a cruise Mach number of 3.25 at twenty-four kilometres, where the speed of sound is

$$a = \sqrt{\gamma R T} = \sqrt{1.4 \times 287.05 \times 220.6} = 297.8 \, \text{m/s}$$

the cruise speed is $v = 3.25 \times 297.8 = 967.8$ metres per second and the time of flight over ten thousand kilometres is

$$t = \frac{R_{\text{mission}}}{v} = \frac{1.0 \times 10^{7}}{967.8} = 10{,}333 \, \text{s} = 2.87 \, \text{hours}$$

**Nothing in the series so far has had to work for three hours.** That single fact reorganises the entire engineering problem, because the dominant error in a self-contained navigation system does not depend on how far the vehicle has flown or how fast. It depends on how long the system has been running.

### The Specification Is a Drift Rate

A guided weapon is specified by an accuracy. The reported Air Force requirement for the Navaho was a [circular error probable][ref_cep] near eight hundred metres, and the reported achieved performance of the inertial navigator was a position error growing at about 1.6 kilometres for every hour of flight. Both figures come from secondary compilations rather than from a released programme document, and the Epistemic State below says so. What can be done with them, and what the sources do not do, is to convert them into a component specification.

An inertial navigator that has no external reference accumulates position error from the drift of its gyroscopes. For a platform held level by feedback from its own computed position, the secular part of that error is

$$\delta x_{\text{secular}} = R_{e} \, \varepsilon \, t$$

where $R_{e}$ is the Earth radius, $\varepsilon$ is the gyroscope drift rate in radians per second, and $t$ is elapsed time. The derivation is below. Inverting it against the requirement gives the drift rate the weapon needed,

$$\varepsilon_{\text{req}} = \frac{\mathrm{CEP}}{R_{e} t} = \frac{800}{6.371 \times 10^{6} \times 10{,}333} = 1.215 \times 10^{-8} \, \text{rad/s}$$

which in the units the gyroscope industry actually uses is

$$\varepsilon_{\text{req}} = 1.215 \times 10^{-8} \times 206{,}265 = 0.0025 \, \text{deg/hr}$$

and inverting the reported achievement the same way gives

$$\varepsilon_{\text{ach}} = \frac{1600}{6.371 \times 10^{6} \times 3600} = 6.976 \times 10^{-8} \, \text{rad/s} = 0.0144 \, \text{deg/hr}$$

**The programme needed two and a half thousandths of a degree per hour and got about fourteen thousandths.** The shortfall is a factor of

$$\frac{\varepsilon_{\text{ach}}}{\varepsilon_{\text{req}}} = \frac{0.0144}{0.0025} = 5.74$$

and the same factor reappears if the achieved drift is simply propagated to full range, since $R_{e} \varepsilon_{\text{ach}} t = 4.59$ kilometres against a requirement of 800 metres, a ratio of 5.74. The two routes agree because they are the same relation read in opposite directions, which is a consistency check rather than an independent confirmation. **The X-10 exists because in 1950 nobody knew whether the smaller number was reachable**, and the honest summary of the programme is that it was not reached in time.

### The Schuler Loop Decides Which Errors Grow and Which Do Not

The reason drift rather than accelerometer quality was the binding problem is not obvious, and it follows from the feedback structure that every inertial navigator of the period used. An accelerometer cannot distinguish acceleration from gravity, so a navigator must know which way is down, and it establishes that from its own computed position. That closes a loop. Writing $\delta v$ for the velocity error and $\phi$ for the platform tilt, with $\nabla$ the accelerometer bias and $\varepsilon$ the gyroscope drift, the single-channel error equations are

$$\dot{\delta v} = -g \phi + \nabla$$

$$\dot{\phi} = \frac{\delta v}{R_{e}} + \varepsilon$$

Differentiating the first and substituting the second eliminates the tilt and leaves a single second-order equation,

$$\ddot{\delta v} + \frac{g}{R_{e}} \delta v = -g \varepsilon$$

The homogeneous solution is a pure oscillation, since the equation has no damping term at all,

$$\delta v_{h}(t) = C_{1} \cos \omega_{s} t + C_{2} \sin \omega_{s} t$$

and the absence of damping is a property of the mechanisation rather than an oversight. A damped loop would track gravity rather than the vehicle. This is an undamped oscillator at the [Schuler frequency][ref_schuler]

$$\omega_{s} = \sqrt{\frac{g}{R_{e}}} = \sqrt{\frac{9.80665}{6.371 \times 10^{6}}} = 1.2407 \times 10^{-3} \, \text{rad/s}$$

with period

$$T_{s} = \frac{2\pi}{\omega_{s}} = 5064 \, \text{s} = 84.4 \, \text{minutes}$$

The period is a property of the planet and not of the instrument, and the reason it matters here is that the two error sources enter the same equation in structurally different places. The accelerometer bias enters as an initial condition on $\dot{\delta v}$ and produces

$$\delta x_{\nabla}(t) = \frac{\nabla}{\omega_{s}^{2}} \left( 1 - \cos \omega_{s} t \right) = \frac{\nabla R_{e}}{g} \left( 1 - \cos \omega_{s} t \right)$$

which is **bounded for all time** at $2 \nabla R_{e} / g$. The gyroscope drift enters as a forcing term and produces

$$\delta x_{\varepsilon}(t) = -R_{e} \varepsilon \left( t - \frac{\sin \omega_{s} t}{\omega_{s}} \right)$$

which contains a ramp and therefore **grows without limit**. For an accelerometer bias of one ten-thousandth of a gravity, which is representative of good instruments of the period, the bounded excursion is

$$\delta x_{\nabla,\max} = \frac{2 \times 9.807 \times 10^{-4} \times 6.371 \times 10^{6}}{9.80665} = 1274 \, \text{m}$$

**A navigator with a poor accelerometer misses by 1.3 kilometres no matter how long it flies, and a navigator with a poor gyroscope misses by more every minute it stays airborne.** This is why the Navaho programme and every programme like it fought over gyroscopes. The Schuler mechanisation is [Staas 1963][research_staas_c_1963], the error equations in the form used here are [Lange and Parkinson 1965][research_lange_parkinson_1965] and [Lange and Parkinson 1966][research_lange_parkinson_1966], the identification of which error source dominates is [Eisner and Goodman 1964][research_eisner_goodman_1964], and the original observation that a pendulum tuned to this period is insensitive to vehicle acceleration is available in translation as [Schuler and Slater 1967][research_schuler_slater_1967]. Period system descriptions are [Slater 1956][research_slater_1956], [Statsinger 1959][research_statsinger_1959], [Prizevoits 1961][research_prizevoits_1961], [Whitcombe 1961][research_whitcombe_1961], and [Duncan 1968][research_duncan_1968], with the standard treatment in [Britting 1971 Inertial Navigation Systems Analysis][book_britting_1971] and the modern one in [Titterton and Weston 2004 Strapdown Inertial Navigation Technology][book_titterton_weston_2004].

### The Crossover Time, Which Is the Number the X-10 Failed

Setting the growing error equal to the bounded one gives the time at which drift takes over as the dominant term,

$$R_{e} \varepsilon t_{\times} = \frac{2 \nabla R_{e}}{g} \quad \Longrightarrow \quad t_{\times} = \frac{2 \nabla}{g \varepsilon}$$

and with the numbers above,

$$t_{\times} = \frac{2 \times 9.807 \times 10^{-4}}{9.80665 \times 6.976 \times 10^{-8}} = 2867 \, \text{s} = 47.8 \, \text{minutes}$$

**Before forty-eight minutes of flight the accelerometers dominate the error, and after it the gyroscopes do.** Hold that number. It is the one the rest of this article turns on, and it is the reason a vehicle that flew beautifully could not answer the question it was built for.

### What the X-9 Question Was, and Why This Is Not It

The [X-9][related_post_a306_bell_x9] also had an accuracy specification and also drove it down into components, but the resemblance stops there. The X-9's error was geometric. It depended on where the missile was relative to its launcher and its target, and the article showed that the two candidate guidance architectures had error gradients of opposite sign in range. Nothing about it depended on the clock.

The X-10's error is dynamic. It does not care where the vehicle is. It cares only how long the instruments have been integrating, and no geometry improves it. **The only thing that resets a dynamic error is an external observation**, which is why the Navaho carried a star tracker and why the vehicle is properly described as stellar-inertial rather than inertial.

### What the Star Tracker Buys, and What It Costs

A star tracker measures the platform attitude against inertial space, and a measurement of attitude bounds the tilt that the gyroscopes have been allowed to accumulate. A residual tilt $\phi_{0}$ acts on the loop exactly as an acceleration error $g \phi_{0}$ does, so its position consequence is bounded rather than secular, at

$$\delta x_{\phi} = 2 R_{e} \phi_{0}$$

The reported stellar-inertial accuracy is a circular error probable of about 1500 feet, which is 457 metres. Inverting through the bounded-error route gives a residual tilt of

$$\phi_{0} = \frac{457}{2 \times 6.371 \times 10^{6}} = 3.588 \times 10^{-5} \, \text{rad} = 7.4 \, \text{arcsec}$$

and inverting instead through the cross-track route, in which an azimuth error $\psi$ produces a miss of $\psi$ times the distance flown, gives

$$\psi = \frac{457}{1.0 \times 10^{7}} = 4.572 \times 10^{-5} \, \text{rad} = 9.4 \, \text{arcsec}$$

**Two independent inversions of the same reported figure agree within a factor of 1.3**, which is weak evidence that the figure is self-consistent and that the instrument implied by it is a star tracker good to something under ten arcseconds in daylight. That was a demanding instrument in the middle 1950s and it is the part of the Navaho guidance system that has aged best. Against the pure-inertial performance the improvement is

$$\frac{R_{e} \varepsilon_{\text{ach}} t}{\mathrm{CEP}_{\text{stellar}}} = \frac{4592}{457} = 10.0$$

a factor of ten. The tracker also sets its own schedule, because drift regrows the fixed error in

$$t_{\text{fix}} = \frac{\mathrm{CEP}_{\text{stellar}}}{R_{e} \varepsilon_{\text{ach}}} = \frac{457}{6.371 \times 10^{6} \times 6.976 \times 10^{-8}} = 1029 \, \text{s} = 17.1 \, \text{minutes}$$

so a mission of nearly three hours needs on the order of ten successful star fixes and cannot tolerate a long cloud deck or a tracker fault. Stellar-inertial navigation of exactly this period is [Horsfall 1958][research_horsfall_1958], the application to cruise vehicles specifically is [Blumhagen 1963][research_blumhagen_1963], the optimal formulation is [Bona and Hutchinson 1965][research_bona_hutchinson_1965], and the aiding argument in general is [Stevens 1958][research_stevens_1958]. Celestial practice that the automatic tracker mechanised is [Herrick 1946][research_herrick_1946], [Franklin 1954][research_franklin_1954], [Shufeldt 1961][research_shufeldt_1961], and [Williams 1966][research_williams_1966], with tracker engineering in [Klestadt 1971][research_klestadt_1971], [Ogletree et al 1972][research_ogletree_1972], and [Schenkel 1974][research_schenkel_1974].

### The Vertical Channel Is Unstable, Not Merely Inaccurate

The horizontal channels oscillate at the Schuler period and are therefore well behaved. The vertical channel is not, and the difference is qualitative. Gravity decreases with altitude, so a navigator that believes it is too high computes a gravity too small, under-corrects its measured acceleration, and concludes that it is higher still. Linearising the gravity gradient gives

$$\ddot{\delta h} = \frac{2g}{R_{e}} \delta h$$

which has no oscillatory solution at all. It is a pure exponential with time constant

$$\tau_{v} = \sqrt{\frac{R_{e}}{2g}} = \sqrt{\frac{6.371 \times 10^{6}}{19.613}} = 570 \, \text{s}$$

and a doubling time of

$$t_{2} = \tau_{v} \ln 2 = 395 \, \text{s} = 6.6 \, \text{minutes}$$

Over the Navaho's mission this is 18.1 e-foldings, a growth factor of

$$e^{10{,}333 / 570} = 7.5 \times 10^{7}$$

**A purely inertial altitude is not merely poor over three hours, it is meaningless.** Any inertial navigator intended for sustained flight must therefore bound its vertical channel with an external measurement, which in this period meant a barometric altimeter, and the resulting hybrid is not a detail of implementation but a structural necessity. The design of exactly such a system is [Aschaffenburg 1962][research_aschaffenburg_1962], and the damping of inertial systems generally is [Grammatikos et al 1967][research_grammatikos_1967]. Aiding from other external references of the period is [Fegley and Weygandt 1963][research_fegley_weygandt_1963] on Doppler radar and [Groot 1965][research_groot_1965] on Loran, both of which the Navaho rejected because both require transmissions the mission could not rely on.

### The Gravity Field Has to Be Known Over the Target Country

An accelerometer measures specific force and the navigator subtracts a modelled gravity to obtain acceleration. Where the real gravity vector is not where the model says, the residual enters exactly as a tilt does. A deflection of the vertical $\xi$ therefore produces a bounded position error of

$$\delta x_{\xi} = 2 R_{e} \xi$$

and deflections of five to twenty arcseconds are ordinary over continental terrain, giving

$$\delta x_{\xi} = 2 \times 6.371 \times 10^{6} \times \frac{10}{206{,}265} = 618 \, \text{m}$$

for ten arcseconds. **That is seventy-seven percent of the entire eight-hundred-metre accuracy requirement, consumed by not knowing the shape of the Earth's gravity field along the flight path.** The error is deterministic rather than random, so it could in principle be compensated, but only by surveying gravity along a route that crosses the territory the weapon is aimed at. This is the one term in the budget that no instrument improvement addresses and it is rarely mentioned in accounts of the programme.

### The Platform Oven Is a First-Order Component

Gyroscope drift is temperature dependent, and a representative sensitivity for instruments of the period is on the order of a hundredth of a degree per hour for each kelvin of temperature change. Requiring the drift specification of 0.0025 degrees per hour to be held against that sensitivity implies a platform temperature control of

$$\Delta T = \frac{0.0025}{0.01} = 0.25 \, \text{K}$$

**A quarter of a kelvin, held for three hours, inside a vehicle whose skin is at a hundred degrees Celsius or more.** The temperature-controlled oven around an inertial platform is usually described as packaging. It is not. It is the component that makes the drift specification meaningful, and the thermal environment computed in the structural section above is what it has to work against.

### The Budget Does Not Close

Collecting the terms at full range and combining them in quadrature, as independent contributions to a radial error should be combined, gives for the pure inertial case

$$\sigma_{\text{total}} = \sqrt{4592^{2} + 1274^{2} + 2909^{2} + 618^{2}} = 5617 \, \text{m}$$

against an eight-hundred-metre requirement, a factor of 7.0. That is consistent with the reported failure to meet the requirement and requires no comment. The stellar-inertial case is the uncomfortable one. Replacing the drift and alignment terms with the reported stellar residual and keeping the others gives

$$\sigma_{\text{stellar}} = \sqrt{457^{2} + 1274^{2} + 618^{2}} = 1488 \, \text{m}$$

**against a reported stellar-inertial accuracy of 457 metres, which the budget exceeds by a factor of 3.3.** Worse, the deflection-of-the-vertical term alone is 618 metres, so at the assumed values it exceeds the reported figure by itself and leaves no room for anything else.

Three readings are available and the article does not choose between them. The instruments may have been substantially better than the representative values assumed here, in which case the assumptions rather than the report are wrong. The reported figure may describe a best demonstrated result rather than an operational circular error probable, which is a common and usually unmarked distinction in programme literature. Or, and this is the reading that seems to the author most likely and least often stated, **the demonstration was flown down the Atlantic Missile Range, whose gravity field was surveyed and whose geometry was known, and not over the territory the weapon was designed to cross.** An accuracy measured where the gravity field is known is not evidence of accuracy where it is not. The Epistemic State records this as inference rather than fact.

### Alignment on the Ground Is the Equal of Drift in the Air

One further inversion is worth making because it constrains an operation rather than a component. An azimuth misalignment at launch produces a cross-track error proportional to distance flown, so

$$\delta y = \psi \, R_{\text{mission}}$$

and at ten thousand kilometres a misalignment of one arcminute produces

$$\delta y = 2.909 \times 10^{-4} \times 1.0 \times 10^{7} = 2909 \, \text{m}$$

Running it the other way, the achieved drift error of 4.59 kilometres is equivalent to an azimuth misalignment of 1.58 arcminutes. **A minute and a half of arc in how the missile is pointed before it moves is worth as much as three hours of gyroscope drift**, which means the ground alignment procedure was not a preliminary to the guidance problem but a coequal part of it. Alignment and initialisation of the period are [Dasaro 1970][research_dasaro_1970] and [Sutherland et al 1968][research_sutherland_1968], with later treatment in [Maybeck 1973][research_maybeck_1973] and [Hellings 1973][research_hellings_1973].

## Programme Origin

North American Aviation received the MX-770 contract in 1946 for a supersonic surface-to-surface missile, initially of modest range, and the requirement grew repeatedly until it became intercontinental. **The growth is the most important fact about the programme and it is usually reported as a footnote.** A weapon specified at a few hundred nautical miles and a weapon specified at five thousand five hundred are not the same weapon scaled, because the navigation error of a self-contained system grows with flight time while the target does not get larger. Each extension of the range requirement tightened the drift specification in exact proportion, and the vehicle that had to demonstrate compliance was ordered before anyone knew what the final number would be.

The technical inheritance was German. Wartime German work on long-range guided weapons, both the ballistic line that produced the V-2 and the winged extensions that were studied but never flown, was distributed among American contractors after 1945, and North American received engineers, documents, and a rocket engine to reverse-engineer. The engine work is the thread that outlived everything else in the programme, and a captured-programme engine study of exactly this kind is [Singelmann and Mueller 1948][research_singelmann_mueller_1948]. The parallel American effort at Northrop under MX-775 produced the subsonic Snark, whose free-flight aerodynamic testing appears in the same NACA series as the X-10's own and is cited below, and the two programmes are the airbreathing halves of a competition that the ballistic missiles eventually won outright. The programme resolved into three flying articles. The X-10 was the aerodynamic and guidance testbed, turbojet powered and recoverable. The G-26, designated XSM-64, was the ramjet-powered vehicle launched by a liquid rocket booster. The G-38, designated XSM-64A, was the enlarged full-range weapon. Only the first two flew.

Setting the three side by side shows how little of the weapon the testbed represented.

| | X-10 | G-26, XSM-64 | G-38, XSM-64A |
|---|---|---|---|
| Role | aerodynamic and guidance testbed | ramjet test and evaluation | full-range weapon |
| Cruise propulsion | two Westinghouse J40 turbojets | two Wright XRJ47-W-5 ramjets | two Wright XRJ47-W-7 ramjets |
| Launch | runway take-off, own power | liquid rocket booster | liquid rocket booster |
| Recovery | runway landing, reusable | expendable | expendable |
| Cruise Mach | 2.05 demonstrated | 2.75 design | 3.25 design |
| Cruise altitude | about 13.7 km | about 24 km | above 24 km |
| Range | about 1000 to 1400 km reported | 5600 km design | 10,000 km design |
| Structure | aluminium | elevated-temperature | elevated-temperature |
| Guidance | radio command, then N-6 | N-6 stellar-inertial | N-6 stellar-inertial |
| Warhead | none | none carried | W-39 thermonuclear |

**Only two rows of that table are common to all three columns**, the canard configuration and the guidance system. Everything else that decided whether the weapon worked changed between the testbed and the weapon, which is the tabular form of the argument the article makes at length below.

The designation history is unusually tangled even by the standards of this series. The vehicle was ordered as RTV-A-5 in 1950 and redesignated X-10 in 1951, while the weapon itself passed through SSM-A-2, XB-64, and XSM-64. **The X-10 therefore received an X designation not because it was a research aeroplane but because the research-and-test-vehicle series it had been assigned to was folded into the X series.** This is now the third consecutive article in which that is true. The [X-8][related_post_a305_aerojet_x8] was RTV-A-1, the [X-9][related_post_a306_bell_x9] was RTV-A-4, and the X-10 was RTV-A-5, and all three became X numbers in the same reorganisation rather than by any assessment of the individual vehicles. **The three anomalies this series has been treating as three separate puzzles are one administrative act seen three times**, which is a considerably duller explanation than the vehicles deserve and is very probably the correct one. The series will return to it at [A368][ref_series_close].

### What a Recoverable Testbed Was For

The X-10's recoverability is usually described as a cost measure, and cost was certainly part of it, but the deeper reason follows from what the vehicle was measuring. **A drift rate is not a number but a distribution.** Two gyroscopes from the same production run drift at different rates, the same gyroscope drifts differently on different days, and the quantity a weapon programme actually needs is the spread rather than a single value. Estimating a spread requires repetition.

For a normally distributed quantity the relative precision of an estimated standard deviation from $n$ samples is approximately

$$\frac{\sigma_{s}}{s} \approx \frac{1}{\sqrt{2(n-1)}}$$

so pinning a drift standard deviation to within twenty percent requires

$$n = 1 + \frac{1}{2 (0.2)^{2}} = 13.5 \, \text{flights}$$

and to within thirty percent still requires between six and seven. The reported number of dedicated N-6 autonavigator flights is five, which gives

$$\frac{\sigma_{s}}{s} = \frac{1}{\sqrt{2 \times 4}} = 0.354$$

**a thirty-five percent uncertainty on the very quantity the programme was trying to establish.** Reusability was the instrument that was supposed to fix this, and the flight test record below shows that it did not, because the fleet was consumed faster than it accumulated flights. Statistical background is [Papoulis 2002 Probability, Random Variables and Stochastic Processes][book_papoulis_2002], and inertial system testing as a discipline is [Amacker 1967][research_amacker_1967].

## Sizing From First Principles

### The Flights Were Shorter Than the Crossover Time

The X-10's demonstrated navigation leg is reported as exceeding a thousand kilometres. At its maximum Mach number of 2.05 and a service ceiling near 13,650 metres, where the speed of sound is 295.1 metres per second, the speed is $v = 604.9$ metres per second and the leg takes

$$t_{\text{X-10}} = \frac{1.0 \times 10^{6}}{604.9} = 1653 \, \text{s} = 27.6 \, \text{minutes}$$

Against the crossover time computed above this is

$$\frac{t_{\text{X-10}}}{t_{\times}} = \frac{1653}{2867} = 0.58$$

**The X-10 flew for a little over half the time needed for gyroscope drift to become the dominant error.** The two contributions on such a flight are

$$\delta x_{\varepsilon} = R_{e} \varepsilon_{\text{ach}} t_{\text{X-10}} = 735 \, \text{m}$$

$$\delta x_{\nabla} = \frac{\nabla R_{e}}{g} \left( 1 - \cos \omega_{s} t_{\text{X-10}} \right) = 931 \, \text{m}$$

so on a maximum-speed X-10 sortie the accelerometer term is the larger of the two. The vehicle built to prove a gyroscope specification flew in the regime where gyroscopes were not the main source of error.

### Worse Than Small, Because the Two Errors Are Not Separable

Being the smaller term is a nuisance. Being an indistinguishable term is fatal, and that is the actual situation. The measured position error over a flight is a sum of the two shapes,

$$\delta x(t) = A \left( 1 - \cos \omega_{s} t \right) + B \left( t - \frac{\sin \omega_{s} t}{\omega_{s}} \right)$$

and recovering $B$, which carries the drift rate, means separating two functions of time. How well that can be done depends on how nearly parallel the two shapes are over the observation window. Over one full Schuler period the answer is remarkable. Removing means and integrating,

$$\int_{0}^{T_{s}} \left( -\cos \omega_{s} t \right) \left( t - \frac{\sin \omega_{s} t}{\omega_{s}} - \frac{T_{s}}{2} \right) dt = 0$$

because each of the three resulting integrals vanishes over a whole period. **The accelerometer and gyroscope error signatures are exactly orthogonal over one Schuler period**, which means a flight of eighty-four minutes separates them perfectly and a flight of any other length does not. Evaluating the correlation numerically over the actual windows gives

$$r(t_{\text{X-10}}) = 0.974 \qquad r(T_{s}) = 0.000 \qquad r(t_{\text{Navaho}}) = -0.042$$

and the cost of that correlation in estimator variance is the usual inflation factor

$$\mathrm{VIF} = \frac{1}{1 - r^{2}}$$

which evaluates to **19.7 on an X-10 flight** and 1.002 on a Navaho mission.

Because the correlation depends only on the length of the observation window, the whole question becomes a design-of-experiments problem with a single free variable, and it has a clean answer. Sweeping the window length and evaluating the inflation factor gives

| Window | Correlation | Variance inflation |
|--------|-------------|--------------------|
| 8.4 min | 0.985 | 34.0 |
| 25.3 min | 0.977 | 21.6 |
| 42.2 min | 0.940 | 8.60 |
| 59.1 min | 0.764 | 2.40 |
| 76.0 min | 0.237 | 1.06 |
| 84.4 min | 0.000 | 1.00 |
| 101.3 min | -0.189 | 1.04 |

**The optimum is exactly one Schuler period and the penalty for falling short of it is severe and nonlinear.** Halving the window from 84 minutes to 42 costs a factor of 8.6 in variance, and halving it again costs a factor of 21.6. The X-10's supersonic leg sits near the top of that table. A test programme that understood the structure would have specified a flight of eighty-four minutes and would have flown it as slowly as the airframe allowed, and nothing in the accessible record suggests anyone framed the requirement that way. A least-squares separation of the drift rate from X-10 data carries almost twenty times the variance that the same instrumentation would give over a full Schuler period. **This is the sharpest statement of the X-10's limitation available, and it is not a statement about the vehicle's quality.** It is a statement that the observation window was the wrong length.

### Flying Slower Would Have Measured More

The result has a consequence that inverts ordinary intuition about testing. Because drift accumulates with time and the crossover is a time, covering the same ground more slowly puts the flight on the correct side of the threshold. Taking the same thousand-kilometre leg at Mach 0.9 at twelve kilometres, where the speed is 265.6 metres per second,

$$t_{\text{sub}} = \frac{1.0 \times 10^{6}}{265.6} = 3766 \, \text{s} = 62.8 \, \text{minutes}$$

which is 1.31 times the crossover time rather than 0.58 times it. On such a flight the secular term is 1674 metres against a bounded term of 663 metres, the drift now dominating by a factor of 2.5, and the correlation falls to $r = 0.677$ for a variance inflation of 1.85 rather than 19.7. **The subsonic flight is more than ten times more informative about the drift rate than the supersonic one.** The X-10 was supersonic because the Navaho was supersonic and the airframe had to be validated, but for the navigation question specifically, speed was the enemy of the measurement.

### The Configuration, and What Was Actually Measured

The X-10 was a canard delta with twin vertical tails and side-mounted inlets feeding two Westinghouse J40 turbojets. Its wing area of 425 square feet is 39.48 square metres and its span of 8.59 metres gives an aspect ratio of

$$AR = \frac{b^{2}}{S} = \frac{8.59^{2}}{39.48} = 1.87$$

which is very low and is the signature of a configuration designed for supersonic cruise rather than for efficiency at any other condition. Two wind-tunnel and free-flight investigations of the actual configuration survive in the public record and they are the primary technical base for this article. [Pfyl 1952][research_pfyl_1952] reports tunnel measurements on a 0.07-scale model of the MX-770, and [Bond and Swanson 1953][research_bond_swanson_1953] reports a free-flight rocket-boosted 0.12-scale model tested by the Pilotless Aircraft Research Division from Mach 0.8 to 1.7.

The free-flight report states results that are quantitative enough to check against. It finds the canard pitching effectiveness maintained across the speed range with supersonic values somewhat greater than subsonic, the aerodynamic centre moving rearward transonically and forward again supersonically, a drag-rise Mach number near 0.90, a supersonic minimum drag coefficient about twice the subsonic value, and base drag amounting to about twenty-five percent of the configuration's minimum drag supersonically. Canard aerodynamics of the period is [Crane and Adams 1950][research_crane_adams_1950], [Niewald and Moul 1950][research_niewald_moul_1950], [Driver 1957][research_driver_1957], [Sleeman 1957][research_sleeman_1957], [Driver 1958][research_driver_1958], [Spearman and Robinson 1958][research_spearman_robinson_1958], [Fournier 1961][research_fournier_1961], [Peterson 1961][research_peterson_1961], and [Spencer 1961][research_spencer_1961], with the configuration text at [Nielsen 1960 Missile Aerodynamics][book_nielsen_1960]. The comparable free-flight programme on the competing Northrop Snark is [Arbic and Gillespie 1953][research_arbic_gillespie_1953] and [Gillespie and Arbic 1951][research_gillespie_arbic_1951].

### The Inlet, Which Measured Worse Than a Plain Normal Shock

The most striking single measurement in the free-flight report is that duct total-pressure recovery fell with Mach number and was **somewhat less than normal-shock recovery**. That deserves a benchmark. Across a normal shock the total-pressure ratio is

$$\frac{p_{02}}{p_{01}} = \left[ \frac{\frac{(\gamma+1) M^{2}}{2}}{1 + \frac{\gamma-1}{2} M^{2}} \right]^{\frac{\gamma}{\gamma-1}} \left[ \frac{\gamma+1}{2 \gamma M^{2} - (\gamma-1)} \right]^{\frac{1}{\gamma-1}}$$

which at the top of the tested range gives

$$\left. \frac{p_{02}}{p_{01}} \right|_{M = 1.70} = 0.856$$

A single normal shock is the crudest supersonic inlet there is, so recovering less than it means the duct was losing more to internal friction, spillage, and diffusion than the shock system was losing to the shock. For comparison, a two-shock inlet using one oblique shock from a sixteen-degree wedge followed by a normal shock, at the vehicle's own maximum Mach number of 2.05, recovers

$$\left. \frac{p_{02}}{p_{01}} \right|_{\text{two-shock}, M = 2.05} = 0.889$$

against 0.698 for a single normal shock at the same condition, an improvement of twenty-seven percent in delivered total pressure. **The measured configuration was leaving a large fraction of that on the table**, and since net thrust scales roughly with delivered total pressure at fixed geometry, the propulsive consequence is direct. The caution the abstract forces is that this was a 0.12-scale free-flight model, and small ducts at model Reynolds numbers lose more to friction than full-scale ones do, so the measurement bounds the model rather than the vehicle.

### The Vehicle's Own Speed Record Bounds Its Inlet

That caution can be turned into a quantitative constraint, because the full-scale vehicle demonstrated Mach 2.05 and a vehicle that cannot balance its drag does not reach a speed. The static pressure at the service ceiling is 14,902 pascals and the isentropic ram total-pressure ratio at Mach 2.05 is

$$\frac{p_{0}}{p_{\infty}} = \left( 1 + \frac{\gamma-1}{2} M^{2} \right)^{\frac{\gamma}{\gamma-1}} = 8.458$$

so the total pressure delivered to the compressor face, for an inlet of recovery $\eta$, is $14{,}902 \times 8.458 \times \eta$. Scaling the sea-level static installed thrust of 96,971 newtons by the ratio of that quantity to sea-level total pressure, and requiring it to exceed the drag of 75,042 newtons computed above, gives a break-even recovery of

$$\eta_{\min} = \frac{D \, p_{0,\text{SL}}}{T_{\text{static}} \, p_{\infty} \, (p_{0}/p_{\infty})} = 0.622$$

which is

$$\frac{\eta_{\min}}{\eta_{\text{normal shock}}} = \frac{0.622}{0.698} = 0.892$$

**The full-scale inlet had to recover within about eleven percent of normal-shock values or the vehicle could not have reached the speed it is recorded as reaching.** Working the same relation forward, a two-shock inlet gives a thrust margin of 1.43 over drag, a plain normal shock gives 1.12, ninety percent of normal shock gives 1.01, and eighty-five percent gives 0.95 and therefore fails.

This is an inference rather than a measurement and it inherits every assumption in the drag estimate, so the honest statement is that it links two uncertain quantities rather than determining either. What it does establish is that the free-flight model's sub-normal-shock duct recovery cannot have been a property of the full-scale vehicle at full-scale conditions, because the vehicle's own demonstrated performance forbids it. **The model-scale explanation is the correct one, and the article can say so on the vehicle's own evidence rather than on a plausibility argument.** Supersonic inlet work of the period is [Ferri and Nucci 1951][research_ferri_nucci_1951], [Hermann 1950][research_hermann_1950], [Diggins 1951][research_diggins_1951], [Esenwein 1952][research_esenwein_1952], [Allen and Beke 1953][research_allen_beke_1953], [Kochendorfer 1953][research_kochendorfer_1953], [Pfyl 1955][research_pfyl_1955], [Hermann 1956][research_hermann_1956], [Kouyoumjian 1957][research_kouyoumjian_1957], [Mitchell and Campbell 1957][research_mitchell_campbell_1957], [Yeager and Gertsma 1958][research_yeager_gertsma_1958], [Blackaby et al 1959][research_blackaby_1959], [Mickola 1961][research_mickola_1961], and [Mahoney 1962][research_mahoney_1962], with the standard treatment in [Seddon and Goldsmith 1999 Intake Aerodynamics][book_seddon_goldsmith_1999] and the compressible-flow relations in [Anderson 2002 Modern Compressible Flow][book_anderson_2002_modern_compressible].

### Drag, and What the Reported Ranges Cannot Mean

Taking the free-flight finding of a supersonic minimum drag coefficient about twice the subsonic value, and a subsonic value of 0.020 as representative for the class, the zero-lift drag at the ceiling and maximum Mach number follows from the dynamic pressure

$$q = \tfrac{1}{2} \rho v^{2} = \tfrac{1}{2} \times 0.2397 \times 604.9^{2} = 43{,}838 \, \text{Pa}$$

giving $D_{0} = 2 C_{D,\text{sub}} q S = 69{,}235$ newtons. The lift coefficient needed to hold level flight at the maximum take-off mass of 19,187 kilogrammes is

$$C_{L} = \frac{W}{q S} = \frac{188{,}160}{43{,}838 \times 39.48} = 0.109$$

and with an induced-drag factor $k = 1/(\pi AR e) = 0.284$ at an efficiency of 0.6 the induced drag is 5807 newtons, for a total of 75,042 newtons and a lift-to-drag ratio of

$$\frac{L}{D} = \frac{188{,}160}{75{,}042} = 2.51$$

That figure is the one to carry into the range equation. For a jet the Breguet form is

$$R = \frac{v}{g \, c} \frac{L}{D} \ln \frac{W_{0}}{W_{1}}$$

and at a thrust specific fuel consumption of 1.0 per hour, which is generous for an early turbojet, a mass ratio of 1.8 gives

$$R = \frac{604.9}{9.80665 \times (1/3600)} \times 2.51 \times \ln 1.8 = 327 \, \text{km}$$

The mass ratio does not have to be assumed, because the weights are reported. An empty weight of 25,800 pounds is 11,703 kilogrammes and a maximum take-off weight of 42,300 pounds is 19,187 kilogrammes, so the fuel available is 7484 kilogrammes, a fuel fraction of

$$\frac{m_{f}}{m_{0}} = \frac{7484}{19{,}187} = 0.390$$

and the mass ratio is

$$\frac{W_{0}}{W_{1}} = \frac{19{,}187}{11{,}703} = 1.640$$

Substituting the reported mass ratio rather than a guessed one gives a maximum-Mach range of

$$R = \frac{604.9}{9.80665 \times (1/3600)} \times 2.51 \times \ln 1.640 = 275 \, \text{km}$$

**The reported ranges are 3.7 and 5.0 times that figure.** Since the mass ratio is now data rather than assumption, the discrepancy has to be absorbed by the lift-to-drag ratio, by the specific fuel consumption, or by the cruise speed. Working the relation backwards for a subsonic cruise at Mach 0.9, the lift-to-drag ratio required to reach the smaller reported range is

$$\frac{L}{D} = \frac{R g c}{v \ln (W_{0}/W_{1})} = \frac{1.009 \times 10^{6} \times 9.80665 \times (1/3600)}{265.6 \times 0.4944} = 20.9$$

falling to 12.6 if the specific fuel consumption is a very optimistic 0.6 per hour, and rising to 28.4 for the larger reported range. **A wing of aspect ratio 1.87 does not achieve a lift-to-drag ratio of twelve, let alone twenty-one**, under any assumption about the rest of the aeroplane. The conclusion is therefore stronger than a caution about the maximum-Mach case. The reported ranges cannot be reconciled with the reported weights on any cruise condition the vehicle could actually fly. This matters beyond bookkeeping, because it means the operational X-10 sortie may well have spent enough time aloft to sit on the useful side of the crossover computed above, and the flight durations rather than the range figures are what the navigation question turns on. Wave-drag and area-rule work of the period is [Whitcomb 1953][research_whitcomb_1953], [Margolis et al 1958][research_margolis_1958], and [Nelson and Welsh 1960][research_nelson_welsh_1960], with base drag in [Englert et al 1954][research_englert_1954] and [Slocumb and Andrews 1961][research_slocumb_andrews_1961].

**The two reported ranges disagree by a factor of 1.36 and this article does not resolve which is right.** Naming the disagreement is the correct treatment, and the Epistemic State repeats it.

## Dependent Systems

### The Autonavigator

The guidance system was North American's N-6, an inertial platform with an automatic star tracker, sometimes rendered NAVAN. The X-10 flew earlier radio-command equipment as well, with an AN/ARW-56 receiver against an AN/ARW-55 ground transmitter, and the later Cape Canaveral vehicles carried the autonavigator proper. **The programme therefore had two guidance systems aboard the same airframe for different purposes**, one to fly the vehicle where the range wanted it and one to be measured. That arrangement is what made the vehicle recoverable at all, since a test article guided only by the thing under test cannot be relied upon to come back.

### The Autopilot Inner Loop

An unmanned supersonic vehicle needs an autopilot before it needs guidance, because the guidance loop closes around a vehicle that is already stabilised. The canard configuration's aerodynamic centre travel reported by [Bond and Swanson 1953][research_bond_swanson_1953], moving rearward through the transonic region and forward again supersonically, is precisely the behaviour that forces gain scheduling, since the static margin and therefore the short-period frequency change with Mach number along the flight path. The magnitude is worth computing. Approximating the short-period frequency by the pitch-stiffness term alone,

$$\omega_{n} \approx \sqrt{-M_{\alpha}} = \sqrt{\frac{q S \bar{c} \, C_{L\alpha} \, h_{n}}{I_{yy}}}$$

where $h_{n}$ is the static margin, and evaluating at the two ends of the flight envelope with a mean chord of 4.60 metres and a pitch inertia near $5.8 \times 10^{5}$ kilogramme square metres, the frequency runs from

$$\omega_{n} = 0.63 \, \text{rad/s} \quad \text{at Mach 0.95 with a 3 percent margin}$$

to

$$\omega_{n} = 2.03 \, \text{rad/s} \quad \text{at Mach 2.05 with a 10 percent margin}$$

**a factor of 3.2 across conditions the vehicle passes through on every single flight.** A fixed-gain pitch loop cannot hold consistent damping across that spread, so the autopilot had to schedule on dynamic pressure or Mach number, and it had to do so with analogue hardware. This is the sense in which the X-10's autopilot was a harder piece of engineering than its guidance. Roll stabilisation of a supersonic pilotless aircraft in this exact period is [Zarovsky 1951][research_zarovsky_1951], with autopilot forms in [Seaberg 1950][research_seaberg_1950] and system practice in [Hart 1956][research_hart_1956]. Servomechanism engineering of the period is [Lebell 1956][research_lebell_1956], [Evans 1957][research_evans_1957], [Kuba and Kazda 1958][research_kuba_kazda_1958], and [Etzweiler 1969][research_etzweiler_1969], with later formulations in [Fagin et al 1969][research_fagin_1969] and [Johnson 1971][research_johnson_1971] and the cruise-missile case specifically in [Gully and Skelley 1975][research_gully_skelley_1975]. The standard texts are [Blakelock 1991 Automatic Control of Aircraft and Missiles][book_blakelock_1991] and [Etkin and Reid 1996 Dynamics of Flight][book_etkin_reid_1996].

### The Turbojets, and the Engine That Was Not Tested

The X-10 flew on two Westinghouse J40 turbojets, an engine whose development difficulties were substantial and whose troubles are usually recorded against the naval aircraft that were obliged to use it. For the X-10 the relevant point is narrower. A turbojet at Mach 2 is operating far from the condition its compressor was designed for, and the design problem was being actively worked in the open literature at the time by [Hurley 1951][research_hurley_1951], [Gabriel et al 1953][research_gabriel_1953], [Alford and Auyer 1954][research_alford_auyer_1954], and [Palmer 1956][research_palmer_1956], with the non-afterburning supersonic application in [Cesaro and Walker 1955][research_cesaro_walker_1955] and afterburner behaviour in [Fleming et al 1956][research_fleming_1956]. Inlet and engine compatibility, which the thrust calculation above treats as a single recovery number, is a dynamic problem in its own right and is [Calogeras 1969][research_calogeras_1969] and [Calogeras and Coltrin 1969][research_calogeras_coltrin_1969], with dynamic simulation in [Chun and Swanson 1964][research_chun_swanson_1964] and test method in [Burris 1966][research_burris_1966].

**The engine the Navaho actually needed was flown by nobody in this programme.** The Wright XRJ47 ramjet intended for the weapon was evaluated separately, and [Reilly and Welna 1955][research_reilly_welna_1955] reports a preliminary evaluation of the flight-weight XRJ47-W-5, which is the single most directly relevant propulsion document in the accessible record and concerns an engine the X-10 never carried. Ramjet engine requirements for supersonic flight generally are [Walker 1952][research_walker_1952] with materials in [Besserer 1952][research_besserer_1952], and the combined-cycle idea that would have let one vehicle do both jobs is [Vault 1957][research_vault_1957], which postdates the X-10 and describes exactly the arrangement its recoverability requirement had forced the programme to do without.

### The Structure, and the Temperature That Bounds It

Aerodynamic heating sets what the airframe may be made of. The recovery temperature at a recovery factor of 0.89 is

$$T_{r} = T_{\infty} \left( 1 + r \frac{\gamma - 1}{2} M^{2} \right)$$

and at the X-10's maximum Mach number and ceiling this gives

$$T_{r} = 216.65 \left( 1 + 0.89 \times 0.2 \times 2.05^{2} \right) = 378.7 \, \text{K} = 105.6 \, ^{\circ}\text{C}$$

which sits comfortably inside the service range of aluminium alloys, conventionally taken near 423 kelvin. The same relation at the Navaho's cruise condition of Mach 3.25 at twenty-four kilometres gives

$$T_{r} = 220.6 \left( 1 + 0.89 \times 0.2 \times 3.25^{2} \right) = 635.5 \, \text{K} = 362.4 \, ^{\circ}\text{C}$$

which does not. Solving for the Mach number at which the recovery temperature reaches the aluminium limit,

$$M_{\text{Al}} = \sqrt{\frac{2}{r (\gamma - 1)} \left( \frac{T_{\text{Al}}}{T_{\infty}} - 1 \right)} = 2.27$$

**The aluminium frontier lies at Mach 2.27 and the X-10's maximum was Mach 2.05.** That is not a coincidence and it is not a near miss. The X-10 was built of aluminium, so it could not be flown past the point where aluminium stops working, and the Navaho's structural problem therefore lay entirely outside the testbed's envelope. Heating and high-temperature structure of the period is [Luce and Jr 1949][research_luce_jr_1949], [Drakin 1963][research_drakin_1963], [Harri 1964][research_harri_1964], and [Heimerl and Hardrath 1965][research_heimerl_hardrath_1965], with later material in [Davis et al 1972][research_davis_1972] and [Chou and Smith 1974][research_chou_smith_1974]. The design-criteria problem that a sustained supersonic vehicle poses, which is that the structure must be sized for a thermal state that persists rather than for a transient, is [Stauffer 1964][research_stauffer_1964], with materials selection in [Fairbairn 1964][research_fairbairn_1964] and a later structural concept study for a comparable configuration in [Sakata et al 1975][research_sakata_1975]. Heat transfer and boundary-layer measurement of the kind that would have been needed to verify any of it is [Rumsey and Lee 1961][research_rumsey_lee_1961], and unsteady loads and dynamic response are [Morito and Sidwell 1967][research_morito_sidwell_1967].

**The thermal argument and the navigation argument meet at the instrument platform.** The oven that holds the gyroscopes to a quarter of a kelvin is mounted inside a structure whose skin the relation above puts at 106 degrees Celsius on an X-10 flight and 362 on the Navaho's, and it must hold that quarter kelvin for three hours while the surrounding structure soaks. This is a coupling the article's two main threads share and it is not usually drawn.

### Power, Which an Unmanned Vehicle Cannot Ask For

Everything aboard the X-10 that moved or computed needed power, and unlike a piloted aeroplane there was nobody to reset a breaker or select an alternate source. The hydraulic system drove the control surfaces and the landing gear, the electrical system ran the platform oven, the autopilot, the telemetry, and the command receiver, and a failure in either was unrecoverable in a way that the same failure on a piloted aircraft would not have been. The platform oven is the least forgiving load, because it must hold its temperature from before take-off through the whole flight, and an oven that loses power does not fail immediately but drifts, which is worse. Servo and actuator engineering of the period is [Biernson 1965][research_biernson_1965] and [Davies and Haines 1965][research_davies_haines_1965], with instrument servomechanism behaviour including limit cycling in [Marstrander and Lueg 1969][research_marstrander_lueg_1969].

**The reliability arithmetic of an unmanned vehicle is unforgiving in a way that is easy to state and was hard to act on in 1955.** If a mission requires $n$ subsystems all to work and each works with probability $p$, the mission succeeds with probability

$$P_{\text{mission}} = p^{n}$$

so ten subsystems at ninety-five percent each give

$$P = 0.95^{10} = 0.599$$

a mission success rate of about sixty percent from components that would each individually be called reliable. **The X-10 completed twenty-seven development flights and lost twelve of thirteen airframes**, which is entirely consistent with that arithmetic and requires no single villain. Reliability estimation as the period practised it is [Blumenthal and Denton 1962][research_blumenthal_denton_1962].

### Landing Gear, Brakes, and the Strip Built for a Machine

The X-10 had to land itself, and the record shows that this is what destroyed the fleet. Taking a landing mass of twelve tonnes after fuel burn, the wing loading is 2980 newtons per square metre and at a maximum lift coefficient of unity the stall speed at sea level is

$$v_{\text{stall}} = \sqrt{\frac{2W}{\rho S C_{L,\max}}} = \sqrt{\frac{2 \times 117{,}680}{1.225 \times 39.48 \times 1.0}} = 69.8 \, \text{m/s}$$

or 136 knots, with an approach at 1.2 times that giving 83.7 metres per second, which is 163 knots. The kinetic energy to be dissipated is

$$E = \tfrac{1}{2} m v^{2} = \tfrac{1}{2} \times 12{,}000 \times 83.7^{2} = 42.0 \, \text{MJ}$$

and at a braking friction coefficient of 0.4 the ground roll is

$$s = \frac{v^{2}}{2 \mu g} = \frac{7006}{2 \times 0.4 \times 9.80665} = 893 \, \text{m}$$

The Air Force built a landing strip 200 feet wide and 10,000 feet long at Cape Canaveral specifically for this vehicle, and it survives as the Skid Strip. At 3048 metres it is 3.4 times the computed braking distance, which is the margin an unmanned vehicle with no pilot to correct a drift needs and did not always get. A drag chute is worth having because its force scales with the square of speed while braking force does not, so it does its work early. A chute matching the brakes at touchdown speed needs an area of

$$S_{c} = \frac{\mu W}{\frac{1}{2} \rho v^{2} C_{D,c}} = \frac{47{,}072}{\frac{1}{2} \times 1.225 \times 7006 \times 1.4} = 7.83 \, \text{m}^{2}$$

which is a canopy of 3.16 metres diameter, and deploying it roughly halves the stopping distance. Landing dynamics and gear work of the period is [Stowell et al 1948][research_stowell_1948], [Yntema and Milwitzky 1952][research_yntema_milwitzky_1952], [Horne and Leland 1962][research_horne_leland_1962], and [Kordes and Mc Kay 1962][research_kordes_mc_kay_1962], with recovery-system design in [Knacke 1992 Parachute Recovery Systems Design Manual][book_knacke_1992] and gear design in [Currey 1988 Aircraft Landing Gear Design][book_currey_1988]. Barrier and arresting practice is [Lawrence 1952][research_lawrence_1952].

### Automatic Landing, Which Did Not Yet Exist

The hardest thing the X-10 did was the thing least remarked upon. Landing an aeroplane automatically was an unsolved problem in 1953, and the first airline automatic landing systems did not enter service until more than a decade later. The period literature makes the gap visible. [Helliwell 1952][research_helliwell_1952] treats automatic control in the landing approach, [Walker 1960][research_walker_1960] and [Walker 1961][research_walker_1961] describe fully automatic approach, and the systems that actually entered service are [Schoenman and Doniger 1965][research_schoenman_doniger_1965] on the Boeing and Bendix 707 installation and [Templeman and Parker 1968][research_templeman_parker_1968] on the Boeing and Sperry 727. Design considerations are [Doniger 1967][research_doniger_1967], approach guidance concepts are [Maiuzzo 1970][research_maiuzzo_1970] and [Poritzky 1970][research_poritzky_1970], and the radio-inertial lateral control limits are [MacKinnon and Madden 1972][research_macklnnon_madden_1972]. **The X-10 was landing itself on a runway a decade before airliners did**, with a guidance loop closed through a ground radio link and an autopilot, and it is fair to say that the programme discovered how hard this was by losing vehicles to it.

### The Command Link Cannot Reach the End of the Leg

The radio-command equipment is usually mentioned and never dimensioned, and dimensioning it produces a constraint that bears directly on the article's argument. A radio link between a vehicle at altitude $h$ and a station on the ground is limited by the horizon, which under standard atmospheric refraction is computed with an effective Earth radius four thirds of the true one,

$$d_{\text{horizon}} = \sqrt{2 \, k \, R_{e} \, h}, \qquad k = \frac{4}{3}$$

At the X-10's service ceiling this gives

$$d_{\text{horizon}} = \sqrt{2 \times \tfrac{4}{3} \times 6.371 \times 10^{6} \times 13{,}650} = 482 \, \text{km}$$

and adding a hundred-metre ground mast extends it only to 523 kilometres, because the vehicle's own altitude dominates. Against a reported navigation leg beyond a thousand kilometres this is

$$\frac{1000}{482} = 2.08$$

**The leg is more than twice the radio horizon, so a single ground station cannot see the vehicle through it.** Either the range operated a chain of stations, which is what Cape Canaveral in fact developed, or the vehicle spent a substantial part of every long sortie beyond command range. Both readings support the same conclusion. Past the horizon the autonavigator is not being tested as a candidate subsystem but relied upon as the only one available, and the recoverability of the vehicle is what makes that acceptable rather than reckless.

### The Turn, Which Is Cheaper Than It Looks

A vehicle that must come home has to reverse course, and at Mach 2 that sounds expensive. The turn radius at load factor $n$ is

$$r = \frac{v^{2}}{g \sqrt{n^{2} - 1}}$$

which at the vehicle's maximum speed and a load factor of two, corresponding to a bank angle of sixty degrees, gives

$$r = \frac{604.9^{2}}{9.80665 \times \sqrt{3}} = 21.5 \, \text{km}$$

so a course reversal sweeps 43 kilometres of ground track and takes

$$t_{\text{turn}} = \frac{\pi r}{v} = \frac{\pi \times 21{,}541}{604.9} = 112 \, \text{s}$$

which is 4.3 percent of a thousand-kilometre leg. **The turn is not the problem.** It is worth computing precisely because the intuition that supersonic vehicles cannot manoeuvre in useful distances is wrong at this scale, and because it removes one candidate explanation for the losses, which were concentrated on the ground.

### Instrumentation, Telemetry, and the Range

Everything the programme learned came back either in the vehicle or over a radio link. Range instrumentation and flight-test reporting practice of the period is visible in [Diegoca 1961][research_diegoca_1961], [Moyer 1963][research_moyer_1963], and [Knoblach 1974][research_knoblach_1974], with decelerator testing in [Ward and Myers 1967][research_ward_myers_1967]. The recoverable vehicle has a genuine advantage here that the [X-8][related_post_a305_aerojet_x8] and [X-9][related_post_a306_bell_x9] did not enjoy, because an instrument package that lands with the vehicle can be calibrated afterward against the same bench that calibrated it before flight, and a drift measurement is only as good as that comparison.

## The Flight Test Record

The first X-10 flight was on 14 October 1953 at Edwards Air Force Base. Five vehicles flew fifteen flights there through 1955. The programme then moved to Cape Canaveral, where the first flight on 19 August 1955 ended with the vehicle running off the runway after the brake failed to act. Twelve further flights, numbered sixteen through twenty-seven, were flown from the Cape between August 1955 and November 1956, and these included the supersonic performance demonstration to Mach 2.05 and the navigation legs beyond a thousand kilometres. Five flights were dedicated to the N-6 autonavigator.

Of the thirteen vehicles built, one survives, serial 51-9307, the first to fly, now held by the National Museum of the United States Air Force. The others were lost. Three were expended in planned dives against Grand Bahama Island, at least two were lost in landing accidents at the Cape, and three surplus vehicles flown as targets for BOMARC development between September 1958 and January 1959 were all lost, two of them burning after running off the end of the Skid Strip on 24 September and 13 November 1958. The last X-10 flew on 26 January 1959 and crashed about fifty-seven miles downrange after a power failure.

The programme therefore divides into four phases with different purposes. The Edwards phase from October 1953 established that the vehicle flew and could be recovered. The Cape phase from August 1955 extended the envelope and flew the navigation legs. The five dedicated autonavigator flights in that phase are the only part of the programme that addressed the keystone question directly. The post-cancellation phase from September 1958 used surplus airframes as targets for a different programme entirely, which is the ordinary fate of a cancelled programme's remaining hardware and tells nothing about the vehicle.

### What Was Actually Demonstrated

Stating the achievements precisely matters because the article's argument is that the vehicle worked and the test did not. The X-10 reached Mach 2.05, which is above the free-flight model's tested maximum of 1.70 and therefore beyond where either ground method had been validated. It reached about 49,000 feet. It flew navigation legs beyond a thousand kilometres. It took off and landed under automatic control on a runway. Considered as an aeroplane, and particularly as an unmanned aeroplane in 1955, this is an impressive record and there was no comparable vehicle anywhere.

The reason the record does not settle the programme's question has nothing to do with any of it. **A vehicle can be flown perfectly and still fail to constitute an experiment**, and that is what the identifiability calculation above establishes. The X-10's sorties were successful flights and weak measurements, and those are independent properties.

### The Dive Flights, Which Were a Test and Not a Disposal

Three vehicles flown at the Cape were expended in planned dives against Grand Bahama Island, and these are usually listed alongside the accidental losses as though they were the same kind of event. They were not. The Navaho's terminal phase was a dive onto the target from cruise altitude, and a dive from twenty-four kilometres at Mach three is a flight condition in its own right, with its own structural loads, its own control problem, and its own contribution to the accuracy budget. **A vehicle that navigates perfectly and then misses the dive has still missed.** Expending three airframes to fly that phase deliberately is a test decision, and it is evidence that the programme understood the terminal phase as a distinct problem even though the X-10 could only approximate its conditions.

### What the Losses Say

The attrition is worth stating as a number. Twelve of thirteen vehicles lost is

$$\frac{12}{13} = 0.923$$

and twenty-seven development flights across thirteen airframes is 2.08 flights per vehicle. **A design whose entire economic and statistical rationale was repeated use averaged two flights per article.** The causes named in the accessible record are concentrated at the end of the mission rather than in it, with brakes that did not act, drag chutes that did not deploy, barriers that were not engaged, and vehicles that veered off the strip. The vehicle flew supersonically and navigated across a range, and then could not reliably stop.

## Comparison With Ground Prediction

Three levels of evidence exist for this configuration and they can be set against one another. [Pfyl 1952][research_pfyl_1952] gives wind-tunnel data on a 0.07-scale model. [Bond and Swanson 1953][research_bond_swanson_1953] gives free-flight data on a 0.12-scale rocket-boosted model at Reynolds numbers from nine to twenty-four million. The full-scale vehicle flew to Mach 2.05, above the free-flight model's maximum of 1.70 and therefore outside the range where either ground method had been checked.

The pattern is familiar from the [X-7][related_post_a304_lockheed_x7]. Free flight extends the Reynolds number far beyond what the tunnels of the period could reach and removes support interference, at the cost of a single trajectory per model and no ability to repeat a condition. The Reynolds numbers make the point concrete. The free-flight models spanned nine to twenty-four million on wing mean aerodynamic chord, while the transonic tunnels of the period typically delivered a few million on a model of comparable size, so the free-flight technique bought roughly an order of magnitude in the parameter that governs whether the boundary layer behaves as it will at full scale.

Two of the free-flight findings are checkable against the analysis performed here and both survive. The reported drag-rise Mach number near 0.90 is consistent with a thin low-aspect-ratio configuration, and the reported doubling of minimum drag from subsonic to supersonic is what wave drag on such a shape produces. The base-drag finding of twenty-five percent of minimum drag supersonically is large but not anomalous for a configuration with a blunt afterbody carrying two engine exhausts. The duct recovery result illustrates the tension exactly, because the free-flight model's report of recovery below normal-shock values is either a real property of the inlet design or an artefact of a small duct at model scale, and **no measurement in the accessible record distinguishes those two possibilities**. The full-scale vehicle's own inlet performance does not appear in the public literature at all, which is why the thrust-balance inference above had to be constructed from the vehicle's demonstrated speed instead.

The free-flight technique itself deserves naming, because it is the method that produced the only quantitative data on this configuration that survives. Its development and its limits are [Turner 1965][research_turner_1965], and comparable applications in the same era are [Wetzel 1954][research_wetzel_1954], [Ball and Smith 1956][research_ball_smith_1956], and [Grant and Sevier 1960][research_grant_sevier_1960]. The technique's central bargain is worth restating in the terms this article has been using. **A free-flight model gives one trajectory and therefore one sample**, which is exactly the same difficulty the X-10 had with drift statistics, one level down in scale. A programme that needs a distribution and can afford only single samples is in the same trouble whether the article being flown is a scale model or a full-size vehicle.

## What the Data Changed

### The Navaho, Which Was Cancelled

Air Force Headquarters terminated the Navaho by message dated 12 July 1957. The XSM-64 had flown first on 6 November 1956 and failed after ten seconds when the pitch gyroscope failed. Three further launches through 26 June 1957 failed in turn, one impacting twenty-five nautical miles downrange, one falling back onto the pad after rising four feet, and one losing its ramjets after booster separation. Seven more tests followed through November 1958 without a full-range success. **The X-10 was the most successful part of a programme that failed**, and by the time the vehicle had demonstrated what it could demonstrate, the ballistic alternatives had made the question moot.

The strategic argument is worth stating plainly because it is not primarily an engineering one. A cruise missile flies for hours and can be intercepted throughout. A ballistic missile of the same range arrives in about thirty minutes and in 1957 could not be intercepted at all. Once Atlas and Titan were credible, an airbreathing intercontinental weapon had to justify a three-hour exposure that its competitor did not have, and no accuracy improvement available at the time was worth that. The class history is [Werrell 1985 The Evolution of the Cruise Missile][book_werrell_1985].

### What Survived

The programme's outputs outlived its purpose in three directions, and it is worth being precise about which of them the X-10 can claim.

**The engines.** The liquid rocket booster engines developed for the Navaho became the basis of the Rocketdyne line that powered Redstone, Jupiter, Thor, and Atlas, and through Atlas the American space programme. This is by a wide margin the largest technical legacy of the Navaho effort. **It belongs entirely to the booster and the X-10 had no part in it whatever**, since the X-10 carried no rocket engine and took off under turbojet power. Accounts that credit the X-10 with the Rocketdyne inheritance are crediting the wrong vehicle in the same programme.

**The navigation.** The stellar-inertial work is the legacy the X-10 can properly claim, because the X-10 is where the N-6 was flown. The architecture fed forward into later air-breathing weapons and into the inertial navigation industry, and the specific combination of a Schuler-tuned platform with an automatic celestial reference remained the standard solution for unaided long-range navigation until satellite navigation displaced it, and has returned to favour as satellite navigation has become contestable.

**The configuration.** Experience with large supersonic canard configurations, with side-mounted supersonic inlets, and with the structures and systems of sustained supersonic flight fed into subsequent work at the same company, most visibly the XB-70. The connection is real but diffuse and this article does not attempt to quantify it.

**What the X-10 did not change is the Navaho's outcome.** By the time the vehicle had flown its full programme, the weapon it served had been cancelled, and the cancellation turned on an argument about exposure time that no amount of aerodynamic or navigational success would have answered.

**The X-10's own specific contribution is harder to point at than any of these**, and honesty requires saying so. It demonstrated that a large unmanned supersonic vehicle could be flown repeatedly from a runway and recovered, which is a real result. What it did not do was settle the navigation question it was built to settle, for the reasons computed above.

## The Contemporary Literature

### Inertial Error Propagation, Which Is Now Computed Rather Than Bounded

The error analysis this article performs by hand is now standard and automated. Colored-noise propagation through inertial mechanisations is [Blum and Dambeck 2020][research_blum_dambeck_2020], uncertainty propagation with conic constraints is [Brouk and DeMars 2021][research_brouk_demars_2021], and sensitivity analysis for precision inertial sensors is [Bhatia and Geller 2020][research_bhatia_geller_2020]. The relevant modern point is that the crossover time computed here as a single scalar is now the output of a full covariance propagation, and that the qualitative structure of a bounded accelerometer term against a secular gyroscope term survives unchanged.

### Gyroscopes, Where the Numbers Finally Arrived

The Navaho needed 0.0025 degrees per hour and could not get it. The figure is worth holding beside the current literature, because the comparison is unusually exact.

Navigation-grade fibre-optic gyroscopes are [Shang et al 2020][research_shang_2020], [Zhao et al 2022][research_zhao_2022], [Liu et al 2023][research_liu_2023], and [Aleinik et al 2025][research_aleinik_2025]. Micro-electromechanical instruments have closed most of the remaining distance, with [Suzuki et al 2019][research_suzuki_2019] and [Nusbaum et al 2019][research_nusbaum_2019] on the approach, a bias instability of 0.09 degrees per hour in [Wu et al 2021][research_wu_2021], a high-quality-factor hemispherical resonator in [Li et al 2024][research_li_2024], and **a honeycomb disk resonator gyroscope reported at 0.003 degrees per hour in [Chen et al 2025][research_chen_2025]**.

That last figure is within twenty percent of the Navaho's requirement, and it is achieved by a micro-electromechanical device. The mechanisms that set the floor are now themselves the subject of study, in [Hiller et al 2019][research_hiller_2019] on the origins of bias instability, [Kuang et al 2022][research_kuang_2022] on its temperature dependence, which is the modern form of the platform-oven problem computed above, [Laita et al 2024][research_laita_2024] on nonlinearity, and [Zhao et al 2024][research_zhao_2024] on installation-error propagation. Gyrocompassing, which is the alignment problem this article showed to be worth 2.9 kilometres per arcminute, is treated afresh in [Bénet and Guinamard 2026][research_benet_guinamard_2026], and the combination of star tracker with gyroscope that the N-6 pioneered is [Zhu et al 2025][research_zhu_2025].

**A requirement that defeated a national weapon programme in 1957 is now met by a component**, and the seventy years between those two statements is the most direct measure available of how far ahead of its instruments the Navaho's accuracy requirement was.

### Star Trackers, Which Became Routine

Automatic celestial reference is now ordinary. Star-tracker calibration in orbit is [Siemes et al 2019][research_siemes_2019], attitude-correlated frame methods for weak signals are [Ni et al 2019][research_ni_2019], and star-pixel-coordinate integration is [Ning et al 2019][research_ning_2019]. The daylight tracking problem the Navaho solved with difficulty is now a design choice rather than a research question.

### Fault Detection, Which the X-10 Had No Means Of

An unmanned vehicle that loses an instrument has no one aboard to notice. The X-10's losses were mechanical and terminal, but the guidance failure mode was live throughout, and the first XSM-64 launch was destroyed by a pitch gyroscope failure ten seconds after lift-off. Detecting and identifying such a failure in flight became possible only later, and the founding treatment is [Potter and Deckert 1972][research_potter_deckert_1972], with modern robustness work in [Lee et al 2024][research_lee_2024] and fault-protection architecture in [Schulte and Spencer 2020][research_schulte_spencer_2020]. **The redundancy that would have saved that vehicle was not unavailable for cost reasons. The analytical basis for using it did not yet exist.**

### Navigation Without Satellites, Which Is Again a Live Problem

The Navaho's problem was navigating with no external radio reference, and this has become topical again. Terrain-referenced navigation is [Park and Park 2019][research_park_park_2019], [Kang et al 2020][research_kang_2020], and [Carroll and Canciani 2021][research_carroll_canciani_2021], with robust filtering in [Zhai and Wang 2020][research_zhai_wang_2020] and [Cui et al 2021][research_cui_2021], nonlinear alignment in [Alhassan and Ghahremani 2021][research_alhassan_ghahremani_2021], and integration architectures in [Ermakov and Gogolev 2021][research_ermakov_gogolev_2021] and [Wang et al 2020][research_wang_2020]. **The question the X-10 was built to answer is once more an open engineering question**, asked now about vehicles that must operate where satellite navigation is denied.

### Reusability, Which Is Now Argued About in the Same Terms

The X-10's economic case for recovery, and its failure to realise that case at 2.08 flights per airframe, is the same argument now conducted about launch vehicles. Life-cycle cost analysis of the kind the argument needs is [Jung et al 2022][research_jung_2022], and the recovery and reuse literature cited below approaches the problem from the trajectory side. The period's own attempt at the same reasoning is visible in the weapon-system cost material harvested for this article, which is largely about procurement rather than about the marginal cost of a flight. **The concept that the X-10 needed and did not have is the distinction between the cost of an airframe and the cost of a sortie**, and a programme that loses twelve of thirteen airframes has collapsed that distinction whether it meant to or not.

### Automatic Landing, Which Became Ordinary and Then Hard Again

Automatic landing of fixed-wing unmanned aircraft is [Brukarczyk et al 2021][research_brukarczyk_2021], reusable launch vehicle recovery trajectory planning is [Cheng et al 2021][research_cheng_2021] and [Mathavaraj and Padhi 2020][research_mathavaraj_padhi_2020], reusable landing structures are [Wang et al 2020, Parameterized Design and Dynamic A][research_wang_2020_3], and landing gear efficiency and failure work is [Han et al 2019][research_han_2019] and [Diltemiz 2021][research_diltemiz_2021]. The X-10's loss record is a reminder that recovery is a distinct engineering problem from flight, and the reusable-launch-vehicle literature has rediscovered this at much greater cost.

### Supersonic Inlets, Where the Free-Flight Anomaly Would Now Be Explained

The inlet result that this article can only bound would today be resolved computationally. Buzz onset prediction is [Yamamoto et al 2020][research_yamamoto_2020] and [Farahani et al 2019][research_farahani_2019], buzz diversity under strong disturbance is [Chen and Tan 2019][research_chen_tan_2019], external-compression inlets free of violent buzz are [Chen et al 2019][research_chen_2019], suppression mechanisms are [Luo et al 2020][research_luo_2020], sideslip effects are [Dong et al 2019][research_dong_2019], and acoustic and vibration behaviour is [Zhu et al 2020][research_zhu_2020].

### Parameter Identification, Which Is the Modern Form of the X-10's Actual Job

The X-10's task was to estimate parameters of a system from flight data, and that is now a discipline. Aerodynamic parameter identification from flight test is [Cao and Wei 2020][research_cao_wei_2020], [Hui et al 2019][research_hui_2019], and [Kulhánek 2019][research_kulhanek_2019], with in-flight lift and drag estimation in [Bergmann et al 2021][research_bergmann_2021] and unmanned flight-test evaluation in [Arif and Sasongko 2021][research_arif_sasongko_2021]. **The identifiability calculation performed above is the standard first question of that discipline and it was not asked in 1953**, which is the clearest sense in which this article applies a later method to an earlier programme.

### Gravity Modelling, Which Removed an Error the Programme Could Not

The deflection-of-the-vertical term that dominates the budget above is now largely a solved problem, because the gravity field has been surveyed from orbit to a resolution the 1950s could not approach. Satellite gravimetry and the geoid models built from it are what removed the term, and the star-tracker calibration work of [Siemes et al 2019][research_siemes_2019] belongs to the same mission family. **The single largest irreducible error in the Navaho's budget was eliminated not by a better instrument but by a better map**, and that is a kind of progress the programme could not have anticipated or purchased.

### Supersonic Cruise, Which Never Returned

Aerodynamic shape design for supersonic cruise is [Azabi et al 2019][research_azabi_2019] and [Wang et al 2020, Local aerodynamic optimisation and][research_wang_2020_2], periodic cruise guidance for hypersonic vehicles is [Gao et al 2020][research_gao_2020], integrated guidance and control for morphing hypersonic missiles is [Bao et al 2019][research_bao_2019], and ascent trajectory design is [Zhai and Yang 2020][research_zhai_yang_2020]. The airbreathing intercontinental weapon did not return, but the airbreathing hypersonic weapon is being attempted again, and the exposure-time argument that killed the Navaho applies to it in modified form.

## Where the Framing Breaks Down

Treating the X-10 through its navigation keystone illuminates the programme's central failure but misleads in five specific ways, and they together are the strongest argument that the vehicle was mismatched to its job.

**It could not test the propulsion.** The Navaho cruised on ramjets. A ramjet has no compressor, so its pressure ratio is the ram ratio

$$\frac{p_{0}}{p_{\infty}} = \left( 1 + \frac{\gamma - 1}{2} M^{2} \right)^{\frac{\gamma}{\gamma - 1}}$$

which is exactly 1.000 at rest and therefore provides no cycle at all. **A ramjet cannot take off from a runway**, so a recoverable runway-operating testbed necessarily uses a different engine, and the X-10's two turbojets tested nothing about the Navaho's propulsion. Ramjet and turbojet cycle relations are in [Hill and Peterson 1991 Mechanics and Thermodynamics of Propulsion][book_hill_peterson_1991].

**It could not test the boost phase.** The Navaho reached ramjet takeover on a liquid rocket booster, and the specific energy that booster had to supply is

$$e = \tfrac{1}{2} v^{2} + g h = \tfrac{1}{2} (818.9)^{2} + 9.80665 \times 24{,}000 = 0.571 \, \text{MJ/kg}$$

equivalent to an ideal velocity increment of 1068 metres per second. The X-10 took off under its own power and had no booster, so the entire staging event, which is where the first XSM-64 flight failed, was outside its scope.

**It could not test the structure.** The aluminium frontier at Mach 2.27 sits above the X-10's maximum of 2.05 and far below the Navaho's 3.25, so the testbed flew inside the material regime the weapon had to leave.

**It could not test the duration.** This is the argument the article has already made quantitatively, and it is the deepest of the four because the other three are obvious in hindsight while this one is not.

**It could not test the environment the accuracy was claimed in.** The budget above shows the deflection of the vertical consuming most of the requirement, and every X-10 navigation flight was made over a surveyed range. A test that removes the dominant error term by choosing where to fly measures the instrument and not the mission.

Four of these five are properties of the vehicle. The fifth is a property of the test range, and it is the only one that could have been fixed without building a different aeroplane.

What the X-10 could and did test is the aerodynamic configuration, the autopilot, the airframe systems, and the practicality of recovering a large unmanned supersonic vehicle. That is a real and useful list. It is not the list of things that decided whether the Navaho worked.

## Is It an Aircraft, and Does the Question Have an Answer

The opening promised that the X-10 makes the not-an-aircraft framing hard to defend, and the material above is enough to settle what the difficulty actually is.

Every physical test fails. The X-10 had a wing, a tail, a fuselage, retractable landing gear, air-breathing engines, and a runway. It took off, cruised, manoeuvred, descended, and landed, repeatedly, and was maintained between flights by people who serviced it as they would have serviced an aeroplane. The [X-8][related_post_a305_aerojet_x8] had none of these properties and the [X-9][related_post_a306_bell_x9] had some of them once per airframe. If the category is defined by what the object is, the X-10 is an aeroplane and the question is closed.

Every purpose test also fails, in the opposite direction. The X-10 existed to produce a number for a weapon programme. It carried no payload, served no transport function, and was expended when it stopped being useful, three of them deliberately flown into an island. **The property that makes it not an aircraft is that nothing aboard it was ever the point.**

What the article's analysis adds is that the two tests do not merely disagree, they interact. The vehicle's aircraft-like properties are precisely what compromised its measurement. It was recoverable, so it needed turbojets, so it could not test the ramjet. It was recoverable, so it was built of aluminium, so it could not exceed Mach 2.27. It was fast, because the weapon was fast, so its flights were short, so its observation window was on the wrong side of the crossover. **Every concession to being an aeroplane cost it something as an instrument**, and that trade is the most interesting thing about the vehicle.

The series has now met three consecutive designations that resist the research-aircraft model, and they resist it in three different ways. The X-8 was an instrument carrier that measured something other than itself. The X-9 was a weapon prototype that measured a control loop. The X-10 is a testbed whose form and whose function pulled against each other.

**Three exceptions with three distinct structures would not be a pattern. Three exceptions with one common origin are.** All three were RTV-A vehicles before they were X vehicles, and the Programme Origin section above records that they became X numbers together. The right conclusion is therefore not that the X-series broadened to admit sounding rockets, missiles, and testbeds on their merits, but that a separate series was absorbed and its contents inherited the letter. Whether that absorption was ever a decision, as against a filing convenience, is the question [A368][ref_series_close] has to answer, and the three cases now on the table are its evidence. The closing article at [A368][ref_series_close] is where the accumulated cases are weighed, and the X-10 contributes the sharpest single instance because it is the one where being an aeroplane was actively expensive.

## The Source Base

The accessible primary record for this vehicle is the thinnest of any article in this series so far, and the shape of the scarcity is more interesting than its extent.

**The vehicle is indexed under its project number, not its designation.** Queries against the aerospace archive for "X-10" and for "Navaho" return almost nothing usable, while "MX-770" returns [Pfyl 1952][research_pfyl_1952] and [Bond and Swanson 1953][research_bond_swanson_1953] immediately. A researcher who does not know the project number will conclude the record is empty when it is merely filed elsewhere. This generalises the archive rule the series has been accumulating, which until now has been about choosing the right archive and is here about choosing the right name within one.

**The defence archive route that worked for the X-9 fails here, and fails in a controlled way.** The [X-9][related_post_a306_bell_x9] article reached Bell's own project documents through Crossref by filtering on the Defense Technical Information Center publisher prefix and querying the project number MX-776, which returns a RASCAL weapon system report directly. The identical query form on MX-770 returns nothing about the Navaho at all. Same archive, same route, same query shape, adjacent project numbers, opposite results. **The negative result is therefore about the record and not about the method**, which is a stronger statement than this series has been able to make about a source gap before.

**Three documents in the accessible record concern the actual hardware.** They are [Pfyl 1952][research_pfyl_1952] on the 0.07-scale tunnel model, [Bond and Swanson 1953][research_bond_swanson_1953] on the 0.12-scale free-flight model, and [Church and Taylor 1959][research_church_taylor_1959] on a 0.05-scale model of the XSM-64A missile and booster, which is the weapon rather than the testbed. Everything else in this article's reference base is topical rather than vehicle-specific, drawn from the very large period literature on inertial navigation, canard aerodynamics, supersonic inlets, automatic landing, and flight test.

That distribution is what makes the article possible at all. The vehicle-specific record would support perhaps four hundred words. The topical record supports the analysis performed here, because the physics that governed the X-10 was being published in the open literature by the same laboratories at the same time, even when the vehicle itself was not.

## Epistemic State

**Historical fact, well supported.** The X-10 was the MX-770 testbed for the Navaho. Thirteen were built. The first flew on 14 October 1953 at Edwards. Fifteen flights were made at Edwards through 1955 by five vehicles, and twelve more from Cape Canaveral between August 1955 and November 1956. The first Cape flight on 19 August 1955 ended with the vehicle leaving the runway after a brake failure. A 200 by 10,000 foot strip was built at the Cape for the vehicle. Maximum demonstrated speed was Mach 2.05. The Air Force cancelled the Navaho by message dated 12 July 1957. Two X-10s supported BOMARC tests on 24 September and 13 November 1958 and both burned after leaving the Skid Strip. The final flight was 26 January 1959. One vehicle survives.

**Historical fact, reported but from secondary compilations only.** The Air Force circular error probable requirement near 800 metres, the achieved inertial drift near 1.6 kilometres per hour, the stellar-inertial accuracy near 1500 feet at maximum range, and the count of five dedicated autonavigator flights. **These four figures carry the article's central quantitative argument and none of them is traceable to a released programme document in the accessible record.** If they are wrong, the inverted gyroscope specifications are wrong by the same factor, though the structural conclusions about which error grows and which is bounded do not depend on them.

**Sources disagree and this article does not resolve it.** Reported X-10 length is 66 feet 2 inches in the designation history and 77 feet in other compilations, a difference of seventeen percent. Reported range is 1370 kilometres in one and 1009 kilometres in another. Reported service ceiling differs slightly between sources. The dimensions used in the calculations above are stated where they are used.

**Engineering analysis, derived here and independently checkable.** The Schuler frequency and period. The bounded form of the accelerometer error and the secular form of the gyroscope error. The crossover time of 47.8 minutes. The X-10 flight duration of 27.6 minutes at maximum Mach and its ratio of 0.58 to the crossover. The exact orthogonality of the two error signatures over one Schuler period, proved by direct integration, and the correlation of 0.974 over an X-10 leg with its variance inflation of 19.7. The window-length sweep showing the optimum at exactly one Schuler period. The inverted gyroscope drift requirements. The star tracker inversions and the 17.1 minute refix interval. The azimuth equivalence of 2.9 kilometres per arcminute. The vertical-channel time constant of 570 seconds, its doubling time of 6.6 minutes, and the 18.1 e-foldings over a Navaho mission. The deflection-of-the-vertical contribution of 618 metres at ten arcseconds. The platform temperature control of 0.25 kelvin implied by the drift specification. The quadrature error budgets of 5617 metres pure inertial and 1488 metres stellar-inertial. The normal-shock and two-shock recovery figures. The radio horizon of 482 kilometres and its ratio of 2.08 to the navigation leg. The turn radius of 21.5 kilometres at load factor two. The short-period frequency spread from 0.63 to 2.03 radians per second. The lift-to-drag ratio of 2.51, the reported mass ratio of 1.640, and the demonstration that the reported ranges are inconsistent with the reported weights on any cruise condition. The break-even inlet recovery of 0.622. The recovery temperatures and the Mach 2.27 aluminium frontier. The landing energy, stall speed, and braking distance. The statistical precision available from five flights and the mission-reliability product.

**Inference, argued but not established.** That the X-10's recoverability was motivated substantially by the statistical character of a drift measurement rather than by unit cost alone. That the free-flight duct recovery below normal-shock values reflects model scale rather than the full-scale inlet, which the thrust-balance argument supports but does not prove, since it inherits the drag estimate. That the reported stellar-inertial accuracy was demonstrated over surveyed range geometry and would not have transferred to unsurveyed territory. That the five testability gaps identified were understood at the time as gaps rather than accepted as adequate coverage. That the reported ranges describe a mission profile the article cannot reconstruct, the reported weights and the reported ranges being mutually inconsistent under every cruise assumption tried here.

**A budget that does not close is reported rather than reconciled.** The quadrature sum of representative error terms exceeds the reported stellar-inertial accuracy by a factor of 3.3, and the deflection-of-the-vertical term alone exceeds it. The article offers three readings and adopts none. This is the largest unresolved quantitative tension in the article and it is stated rather than smoothed.

**Assumptions made explicit.** An accelerometer bias of one ten-thousandth of a gravity, a subsonic minimum drag coefficient of 0.020, a span efficiency of 0.6, a landing mass of twelve tonnes, a maximum lift coefficient of unity, a braking friction coefficient of 0.4, a thrust specific fuel consumption of 1.0 per hour, a recovery factor of 0.89, a gyroscope temperature sensitivity of 0.01 degrees per hour per kelvin, a deflection of the vertical of ten arcseconds, a pitch inertia based on a radius of gyration of thirty percent of length, a mean chord inferred from area and aspect ratio, an effective Earth radius factor of four thirds for radio refraction, and the treatment of installed thrust as proportional to delivered total pressure. Each is representative rather than measured, and each is stated at the point of use so that a reader may substitute a better value.

**Where information postdates the editorial date.** The contemporary literature section is written from current knowledge, as the series convention requires.

## Out of Scope

The Navaho's booster engines and their descent into the Rocketdyne engine line, which deserve their own treatment and are the programme's largest legacy. The G-26 and G-38 vehicles as flight articles. The W-39 warhead. The Snark, which is the X-10's direct competitor and whose free-flight aerodynamic record is cited here only in passing. BOMARC, which appears only as the consumer of three surplus airframes. The detailed politics of the 1957 cancellation. The comparative economics of cruise against ballistic delivery, which is treated only to the depth needed to explain the cancellation. Digital computation, which arrived too late to matter to this vehicle.

## Conclusion

The X-10 was built to find out whether a machine could still know where it was after three hours of flight with nothing to look at but the stars. It was a good aeroplane. It flew to Mach 2.05, navigated across a range, and came home on its own wheels, a decade before airliners could land themselves. **It could not answer its question, and the reason is arithmetic rather than engineering.**

The error a navigator accumulates from its accelerometers is bounded by the geometry of the planet at about 1.3 kilometres. The error it accumulates from its gyroscopes grows without limit. The two are equal at forty-eight minutes and the X-10 flew for twenty-eight. Over that window the two error signatures are ninety-seven percent correlated, and the drift rate that the whole programme turned on could only be extracted from the data with twenty times the variance a longer flight would have given. The testbed flew on the wrong side of a threshold nobody had computed.

Three of the series' vehicles have now been things other than aircraft, and the X-10 is the one that shows why the distinction is hard. It had wings, wheels, a runway, and a flight test programme. What it did not have was a pilot, and the consequence of not having a pilot was that its entire reason for existing was a measurement rather than a demonstration. **A demonstration succeeds by being performed. A measurement succeeds only if the observation window is long enough**, and that is a requirement no amount of flying skill or engineering quality can substitute for.

## References

### Books

[book_anderson_2002_modern_compressible]: https://openlibrary.org/search?q=Anderson+Modern+Compressible+Flow
[book_blakelock_1991]: https://openlibrary.org/search?q=Blakelock+Automatic+Control+of+Aircraft+and+Missiles
[book_britting_1971]: https://openlibrary.org/search?q=Britting+Inertial+Navigation+Systems+Analysis
[book_currey_1988]: https://openlibrary.org/search?q=Currey+Aircraft+Landing+Gear+Design
[book_etkin_reid_1996]: https://openlibrary.org/search?q=Etkin+Reid+Dynamics+of+Flight+Stability+and+Control
[book_gibson_1996]: https://openlibrary.org/search?q=Gibson+The+Navaho+Missile+Project
[book_hill_peterson_1991]: https://openlibrary.org/search?q=Hill+Peterson+Mechanics+and+Thermodynamics+of+Propulsion
[book_jenkins_landis_miller_2003]: https://openlibrary.org/search?q=Jenkins+Landis+Miller+American+X+Vehicles
[book_knacke_1992]: https://openlibrary.org/search?q=Knacke+Parachute+Recovery+Systems+Design+Manual
[book_miller_2001]: https://openlibrary.org/search?q=Miller+The+X+Planes+X-1+to+X-45
[book_nielsen_1960]: https://openlibrary.org/search?q=Nielsen+Missile+Aerodynamics
[book_papoulis_2002]: https://openlibrary.org/search?q=Papoulis+Probability+Random+Variables+and+Stochastic+Processes
[book_seddon_goldsmith_1999]: https://openlibrary.org/search?q=Seddon+Goldsmith+Intake+Aerodynamics
[book_titterton_weston_2004]: https://openlibrary.org/search?q=Titterton+Weston+Strapdown+Inertial+Navigation+Technology
[book_werrell_1985]: https://openlibrary.org/search?q=Werrell+The+Evolution+of+the+Cruise+Missile

### Reference

[ref_cep]: https://en.wikipedia.org/wiki/Circular_error_probable
[ref_navaho]: https://en.wikipedia.org/wiki/SM-64_Navaho
[ref_parsch_sm64]: https://www.designation-systems.net/dusrm/app1/sm-64.html
[ref_parsch_x10]: https://www.designation-systems.net/dusrm/app1/x-10.html
[ref_schuler]: https://en.wikipedia.org/wiki/Schuler_tuning
[ref_series_close]: https://en.wikipedia.org/wiki/List_of_X-planes
[ref_x10]: https://en.wikipedia.org/wiki/North_American_X-10

### Research

[research_aleinik_2025]: https://doi.org/10.1134/s2075108725700257
[research_alford_auyer_1954]: https://doi.org/10.4271/540253
[research_alhassan_ghahremani_2021]: https://doi.org/10.24425/mms.2021.137702
[research_allen_beke_1953]: https://ntrs.nasa.gov/citations/19930087574
[research_amacker_1967]: https://doi.org/10.1017/s0373463300030769
[research_arbic_gillespie_1953]: https://ntrs.nasa.gov/citations/20090026523
[research_arif_sasongko_2021]: https://doi.org/10.47355/avia.v3i1.39
[research_aschaffenburg_1962]: https://doi.org/10.21236/ad0400701
[research_azabi_2019]: https://doi.org/10.3390/aerospace6040042
[research_ball_smith_1956]: https://ntrs.nasa.gov/citations/19660010446
[research_bao_2019]: https://doi.org/10.1155/2019/6413410
[research_benet_guinamard_2026]: https://doi.org/10.33012/navi.751
[research_bergmann_2021]: https://doi.org/10.3390/aerospace8020043
[research_besserer_1952]: https://doi.org/10.21236/ad0036272
[research_bhatia_geller_2020]: https://doi.org/10.1002/navi.397
[research_biernson_1965]: https://doi.org/10.1109/tac.1965.1098076
[research_blackaby_1959]: https://ntrs.nasa.gov/citations/19980228132
[research_blum_dambeck_2020]: https://doi.org/10.3390/s20236914
[research_blumenthal_denton_1962]: https://doi.org/10.21236/ad0291603
[research_blumhagen_1963]: https://doi.org/10.1109/tane.1963.4502121
[research_bona_hutchinson_1965]: https://doi.org/10.1002/j.2161-4296.1965.tb02129.x
[research_bond_swanson_1953]: https://ntrs.nasa.gov/citations/20050029470
[research_brouk_demars_2021]: https://doi.org/10.3390/s21248457
[research_brukarczyk_2021]: https://doi.org/10.3390/aerospace8060167
[research_burris_1966]: https://doi.org/10.2514/6.1966-741
[research_calogeras_1969]: https://doi.org/10.2514/6.1969-487
[research_calogeras_coltrin_1969]: https://ntrs.nasa.gov/citations/19690054687
[research_cao_wei_2020]: https://doi.org/10.1155/2020/5603169
[research_carroll_canciani_2021]: https://doi.org/10.1002/navi.406
[research_cesaro_walker_1955]: https://ntrs.nasa.gov/citations/19670022705
[research_chen_2019]: https://doi.org/10.2514/1.j057811
[research_chen_2025]: https://doi.org/10.1038/s41378-025-01011-4
[research_chen_tan_2019]: https://doi.org/10.1016/j.ast.2019.105471
[research_cheng_2021]: https://doi.org/10.1016/j.ast.2021.106965
[research_chou_smith_1974]: https://doi.org/10.21236/ada001135
[research_chun_swanson_1964]: https://doi.org/10.2514/6.1964-598
[research_church_taylor_1959]: https://ntrs.nasa.gov/citations/19980228032
[research_crane_adams_1950]: https://ntrs.nasa.gov/citations/19930086327
[research_cui_2021]: https://doi.org/10.1016/j.ast.2021.106905
[research_dasaro_1970]: https://doi.org/10.21236/ad0706219
[research_davies_haines_1965]: https://doi.org/10.1109/tac.1965.1098148
[research_davis_1972]: https://ntrs.nasa.gov/citations/19740022813
[research_diegoca_1961]: https://doi.org/10.21236/ad0843112
[research_diggins_1951]: https://doi.org/10.21236/ad0895227
[research_diltemiz_2021]: https://doi.org/10.1016/j.engfailanal.2021.105711
[research_dong_2019]: https://doi.org/10.1063/1.5093559
[research_doniger_1967]: https://doi.org/10.2514/6.1967-406
[research_drakin_1963]: https://doi.org/10.21236/ad0295828
[research_driver_1957]: https://ntrs.nasa.gov/citations/19930089678
[research_driver_1958]: https://ntrs.nasa.gov/citations/19980232000
[research_duncan_1968]: https://doi.org/10.1002/j.2161-4296.1968.tb01584.x
[research_eisner_goodman_1964]: https://doi.org/10.2514/3.2430
[research_englert_1954]: https://ntrs.nasa.gov/citations/19930088172
[research_ermakov_gogolev_2021]: https://doi.org/10.34759/trd-2021-117-11
[research_esenwein_1952]: https://ntrs.nasa.gov/citations/19930087252
[research_etzweiler_1969]: https://doi.org/10.1109/tac.1969.1099278
[research_evans_1957]: https://doi.org/10.1109/tac.1957.1103778
[research_fagin_1969]: https://doi.org/10.1109/tac.1969.1099292
[research_fairbairn_1964]: https://doi.org/10.2514/6.1964-628
[research_farahani_2019]: https://doi.org/10.1016/j.ast.2019.02.002
[research_fegley_weygandt_1963]: https://doi.org/10.1109/tce.1963.6373364
[research_ferri_nucci_1951]: https://ntrs.nasa.gov/citations/19930083137
[research_fleming_1956]: https://ntrs.nasa.gov/citations/19670095388
[research_fournier_1961]: https://ntrs.nasa.gov/citations/19980228000
[research_franklin_1954]: https://doi.org/10.1002/j.2161-4296.1954.tb00693.x
[research_gabriel_1953]: https://ntrs.nasa.gov/citations/19930087143
[research_gao_2020]: https://doi.org/10.3390/app10082898
[research_gillespie_arbic_1951]: https://ntrs.nasa.gov/citations/20050030052
[research_grammatikos_1967]: https://doi.org/10.1109/taes.1967.5408813
[research_grant_sevier_1960]: https://ntrs.nasa.gov/citations/19980230620
[research_groot_1965]: https://doi.org/10.1017/s0373463300019214
[research_gully_skelley_1975]: https://doi.org/10.2514/6.1975-1113
[research_han_2019]: https://doi.org/10.2514/1.c035298
[research_harri_1964]: https://doi.org/10.2172/4597699
[research_hart_1956]: https://doi.org/10.21236/ad0108104
[research_heimerl_hardrath_1965]: https://ntrs.nasa.gov/citations/20000011991
[research_hellings_1973]: https://doi.org/10.21236/ad0763718
[research_helliwell_1952]: https://doi.org/10.1017/s0001925900000688
[research_hermann_1950]: https://doi.org/10.21236/ada377566
[research_hermann_1956]: https://doi.org/10.4271/560270
[research_herrick_1946]: https://doi.org/10.1002/j.2161-4296.1946.tb01079.x
[research_hiller_2019]: https://doi.org/10.1109/jmems.2019.2921607
[research_horne_leland_1962]: https://ntrs.nasa.gov/citations/19620005764
[research_horsfall_1958]: https://doi.org/10.1109/tane3.1958.4201596
[research_hui_2019]: https://doi.org/10.1061/(asce)em.1943-7889.0001542
[research_hurley_1951]: https://doi.org/10.1115/1.4016500
[research_johnson_1971]: https://doi.org/10.1109/tac.1971.1099830
[research_jung_2022]: https://doi.org/10.5762/kais.2022.23.9.185
[research_kang_2020]: https://doi.org/10.1049/iet-rsn.2020.0047
[research_klestadt_1971]: https://ntrs.nasa.gov/citations/19720012067
[research_knoblach_1974]: https://doi.org/10.21236/ada003241
[research_kochendorfer_1953]: https://ntrs.nasa.gov/citations/19930087800
[research_kordes_mc_kay_1962]: https://ntrs.nasa.gov/citations/19630002688
[research_kouyoumjian_1957]: https://ntrs.nasa.gov/citations/19660082192
[research_kuang_2022]: https://doi.org/10.2139/ssrn.4161323
[research_kuba_kazda_1958]: https://doi.org/10.1109/tac.1958.1104980
[research_kulhanek_2019]: https://doi.org/10.1108/aeat-06-2018-0162
[research_laita_2024]: https://doi.org/10.1109/jsen.2024.3462598
[research_lange_parkinson_1965]: https://doi.org/10.2514/6.1965-691
[research_lange_parkinson_1966]: https://doi.org/10.1016/b978-1-4832-2729-0.50018-1
[research_lawrence_1952]: https://doi.org/10.21236/ad0021570
[research_lebell_1956]: https://doi.org/10.1109/tac.1956.1100816
[research_lee_2024]: https://doi.org/10.3390/aerospace11040268
[research_li_2024]: https://doi.org/10.1088/1361-6501/ad6fc3
[research_liu_2023]: https://doi.org/10.1364/ol.487077
[research_luce_jr_1949]: https://doi.org/10.21236/ada278113
[research_luo_2020]: https://doi.org/10.3390/en13010217
[research_macklnnon_madden_1972]: https://doi.org/10.2514/3.59028
[research_mahoney_1962]: https://doi.org/10.4271/620299
[research_maiuzzo_1970]: https://doi.org/10.21236/ad0707129
[research_margolis_1958]: https://ntrs.nasa.gov/citations/19930084830
[research_marstrander_lueg_1969]: https://doi.org/10.1109/tac.1969.1099322
[research_mathavaraj_padhi_2020]: https://doi.org/10.1142/s230138502050003x
[research_maybeck_1973]: https://doi.org/10.21236/ad0784752
[research_mickola_1961]: https://doi.org/10.21236/ad0256347
[research_mitchell_campbell_1957]: https://ntrs.nasa.gov/citations/19930089448
[research_morito_sidwell_1967]: https://doi.org/10.2514/6.1967-1140
[research_moyer_1963]: https://doi.org/10.21236/ad0408760
[research_nelson_welsh_1960]: https://ntrs.nasa.gov/citations/19980227964
[research_ni_2019]: https://doi.org/10.1364/oe.27.015548
[research_niewald_moul_1950]: https://ntrs.nasa.gov/citations/19930086447
[research_ning_2019]: https://doi.org/10.1016/j.actaastro.2019.03.052
[research_nusbaum_2019]: https://doi.org/10.1002/navi.336
[research_ogletree_1972]: https://ntrs.nasa.gov/citations/19720021014
[research_palmer_1956]: https://doi.org/10.1108/eb032757
[research_park_park_2019]: https://doi.org/10.1109/jsen.2019.2934651
[research_peterson_1961]: https://ntrs.nasa.gov/citations/19980227076
[research_pfyl_1952]: https://ntrs.nasa.gov/citations/19710073552
[research_pfyl_1955]: https://ntrs.nasa.gov/citations/19650003100
[research_poritzky_1970]: https://doi.org/10.2514/6.1970-937
[research_potter_deckert_1972]: https://ntrs.nasa.gov/citations/19720048522
[research_prizevoits_1961]: https://doi.org/10.21236/ad0273454
[research_reilly_welna_1955]: https://ntrs.nasa.gov/citations/19660027126
[research_rumsey_lee_1961]: https://ntrs.nasa.gov/citations/19980235513
[research_sakata_1975]: https://ntrs.nasa.gov/citations/19750055457
[research_schenkel_1974]: https://doi.org/10.21236/ada008554
[research_schoenman_doniger_1965]: https://doi.org/10.4271/650571
[research_schuler_slater_1967]: https://doi.org/10.1002/j.2161-4296.1967.tb02190.x
[research_schulte_spencer_2020]: https://doi.org/10.2514/1.i010673
[research_seaberg_1950]: https://ntrs.nasa.gov/citations/20050019266
[research_shang_2020]: https://doi.org/10.3788/col202018.120601
[research_shufeldt_1961]: https://doi.org/10.21236/ad0259559
[research_siemes_2019]: https://doi.org/10.1016/j.asr.2018.10.030
[research_singelmann_mueller_1948]: https://doi.org/10.21236/ada402594
[research_slater_1956]: https://doi.org/10.21236/ada284483
[research_sleeman_1957]: https://ntrs.nasa.gov/citations/20050019253
[research_slocumb_andrews_1961]: https://ntrs.nasa.gov/citations/20040006301
[research_spearman_robinson_1958]: https://ntrs.nasa.gov/citations/19930090148
[research_spencer_1961]: https://ntrs.nasa.gov/citations/19980228059
[research_staas_c_1963]: https://doi.org/10.21236/ad0406113
[research_statsinger_1959]: https://doi.org/10.4271/590055
[research_stauffer_1964]: https://doi.org/10.2514/6.1964-627
[research_stevens_1958]: https://doi.org/10.1002/j.2161-4296.1958.tb02438.x
[research_stowell_1948]: https://ntrs.nasa.gov/citations/19930082235
[research_sutherland_1968]: https://doi.org/10.21236/ad0851067
[research_suzuki_2019]: https://doi.org/10.1541/ieejsmas.139.175
[research_templeman_parker_1968]: https://doi.org/10.2514/3.43940
[research_turner_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50015-4
[research_vault_1957]: https://doi.org/10.4271/570206
[research_walker_1952]: https://doi.org/10.21236/ad0041745
[research_walker_1960]: https://doi.org/10.1049/sqj.1960.0043
[research_walker_1961]: https://doi.org/10.1049/jiee-3.1961.0061
[research_wang_2020]: https://doi.org/10.1017/s0373463319000511
[research_wang_2020_2]: https://doi.org/10.1504/ijvd.2020.114798
[research_wang_2020_3]: https://doi.org/10.3390/sym12091572
[research_ward_myers_1967]: https://doi.org/10.21236/ad0815090
[research_wetzel_1954]: https://ntrs.nasa.gov/citations/20090025891
[research_whitcomb_1953]: https://ntrs.nasa.gov/citations/20050019402
[research_whitcombe_1961]: https://doi.org/10.21236/ad0259865
[research_williams_1966]: https://doi.org/10.1002/j.2161-4296.1966.tb01816.x
[research_wu_2021]: https://doi.org/10.1109/jsen.2021.3110054
[research_yamamoto_2020]: https://doi.org/10.1016/j.ast.2019.105523
[research_yeager_gertsma_1958]: https://ntrs.nasa.gov/citations/19930090049
[research_yntema_milwitzky_1952]: https://ntrs.nasa.gov/citations/19930083424
[research_zarovsky_1951]: https://ntrs.nasa.gov/citations/19930090535
[research_zhai_wang_2020]: https://doi.org/10.1063/5.0019305
[research_zhai_yang_2020]: https://doi.org/10.1016/j.jfranklin.2020.03.002
[research_zhao_2022]: https://doi.org/10.1364/prj.443496
[research_zhao_2024]: https://doi.org/10.1016/j.measurement.2024.114808
[research_zhu_2020]: https://doi.org/10.3390/en13082048
[research_zhu_2025]: https://doi.org/10.1109/tim.2025.3548235

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
