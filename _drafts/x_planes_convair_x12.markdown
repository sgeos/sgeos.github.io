---
layout: post
mathjax: true
comments: true
title: "X-Planes: Convair X-12"
date: 2025-10-18 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 13
---

<!-- A309 -->
<script>console.log("A309");</script>

On 18 December 1958 a [Convair X-12][ref_x12] failed to come down, and that was the point. Every other thing the vehicle did in its six and a half months of flying was aimed at coming down in exactly one place, and the machinery built to do that turned out to be the same machinery needed to not come down at all. This article is the thirteenth in the [X-Planes series][related_post_a297_xplanes_framing], following the [X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], the [X-4][related_post_a301_northrop_x4], the [X-5][related_post_a302_bell_x5], the [X-6][related_post_a303_convair_x6], the [X-7][related_post_a304_lockheed_x7], the [X-8][related_post_a305_aerojet_x8], the [X-9][related_post_a306_bell_x9], the [X-10][related_post_a307_north_american_x10], and the [X-11][related_post_a308_convair_x11].

The X-12 is the Atlas B, and it is the same airframe as the [X-11][related_post_a308_convair_x11]. The pressure-stabilised stainless steel shell, the balloon tank that collapses without nitrogen, the four and a half percent structural mass fraction, and the stage-and-a-half arrangement are all inherited unchanged, and the previous article derived them. **This article is about everything the X-11 could not test.** The Atlas A flew with a dummy sustainer, no separable booster section, no guidance computer, no nose cone, and reached about a fifth of the velocity an intercontinental weapon needs. The Atlas B carried all of it. The standard inventory entry remains [Jenkins Landis and Miller 2003 American X-Vehicles, An Inventory X-1 to X-50][book_jenkins_landis_miller_2003], the vehicle compilation is [Miller 2001 The X-Planes, X-1 to X-45][book_miller_2001], and the programme history is [Walker Bernstein and Lang 2005 Seize the High Ground][book_walker_powell_2005] and [Neufeld 1990 The Development of Ballistic Missiles in the United States Air Force][book_neufeld_1990].

## The Research Question

An intercontinental ballistic missile spends about thirty-four minutes in free fall and it cannot be steered during any of them. Everything the weapon will ever do is decided in the instant its engine stops.

### The Keystone Is the Terminal Velocity Vector

The [previous article][related_post_a308_convair_x11] established that the Atlas is a mass-fraction problem, which it is, and the mass fraction buys velocity. **This article is about what the velocity has to be worth.** For a body on a ballistic arc over a spherical non-rotating Earth, the central angle covered is fixed by the burnout speed alone through

$$\sin \frac{\Phi}{2} = \frac{\lambda}{2 - \lambda}, \qquad \lambda = \frac{v_{bo}^{2}}{g R_{e}}, \qquad R = R_{e} \Phi$$

where $\lambda$ is the ratio of kinetic energy at burnout to the energy of a grazing circular orbit, $R_e$ is the Earth radius, and $\Phi$ is the angle subtended at the centre. Ten thousand kilometres of range requires

$$\lambda = 0.8281, \qquad v_{bo} = 7193 \, \text{m/s}$$

The question this article exists to answer is what happens when that number is slightly wrong. Differentiating the range law with respect to $\lambda$ gives

$$\frac{dR}{d\lambda} = \frac{4 R_{e}}{(2 - \lambda)^{2} \sqrt{1 - u^{2}}}, \qquad u = \frac{\lambda}{2 - \lambda}$$

and chaining through $d\lambda / dv = 2\lambda / v$ gives the sensitivity of range to burnout speed,

$$\frac{dR}{dv_{bo}} = \frac{8 R_{e} \lambda}{v_{bo} (2 - \lambda)^{2} \sqrt{1 - u^{2}}} = 6.04 \, \text{km per m/s}$$

In dimensionless form the same result is

$$S = \frac{dR / R}{dv / v} = 4.34$$

so **a fractional error in cutoff speed produces a range error four and a third times larger in fraction.** Nothing else in the flight has this property. The relation and its consequences for weapon design are period material rather than a modern reconstruction, in [Kelly 1959][research_kelly_1959] on the effect of the thrust termination process on range dispersion, [Cooper 1961][research_cooper_1961] on measuring ballistic missile trajectories accurately enough to see it, and [Whitcombe 1961][research_whitcombe_1961] as the tutorial introduction the period wrote for itself.

### What That Costs in Metres Per Second

Turning the sensitivity into a requirement is a matter of dividing. A circular error probable of two nautical miles is 3.704 kilometres, so the whole error budget in burnout speed is

$$\delta v = \frac{3704}{6040} = 0.613 \, \text{m/s}$$

against a burnout speed of 7193, which is

$$\frac{\delta v}{v_{bo}} = 8.53 \times 10^{-5}$$

**One part in eleven thousand seven hundred.** That is the number the Atlas B existed to chase, and it is worth pausing on how strange it is. The missile weighs a hundred and eighteen tonnes at lift-off, burns six hundred and seventy-six kilogrammes of propellant every second, and is required to stop with its speed correct to two thirds of a metre per second, which is walking pace. A one-kilometre miss requires

$$\delta v = 0.166 \, \text{m/s}$$

or one part in forty-three thousand. Error analysis at this level appears in [Slifka 1960][research_slifka_1960] on field testing a ballistic missile guidance system, [MacPherson 1963][research_macpherson_1963] on explicit guidance equations, [Russell 1964][research_russell_1964] on unifying guidance with flight control, and, sixty years later, [Arthur and Kemp 2025][research_arthur_kemp_2025] on where the accuracy of such systems has arrived.

### What the Accuracy Was Actually For

A requirement of two thirds of a metre per second needs a justification, because it is expensive and the vehicle was already difficult. The justification is a scaling law that makes accuracy worth more than anything else the designer can buy.

Impact points scatter as a circular normal distribution, so the probability of landing within a radius $r$ of the aim point is

$$P(r) = 1 - \exp\left( -\frac{r^{2}}{2 \sigma^{2}} \right)$$

The circular error probable is the median radius, defined by $P = 1/2$, which gives

$$\text{CEP}^{2} = 2 \sigma^{2} \ln 2, \qquad \sigma = \frac{\text{CEP}}{\sqrt{2 \ln 2}} = 3.146 \, \text{km}$$

for a two nautical mile circular error probable. Substituting back, the probability of destroying a target with a lethal radius $L$ is

$$p_{k} = 1 - 2^{-(L / \text{CEP})^{2}}$$

which is a remarkably sharp function of the ratio.

| Lethal radius over circular error probable | Probability of destruction |
|---|---|
| 0.25 | 0.042 |
| 0.50 | 0.159 |
| 1.00 | 0.500 |
| 1.50 | 0.790 |
| 2.00 | 0.938 |
| 3.00 | 0.998 |

**Now the decisive step.** The lethal radius for a given effect scales as the cube root of yield,

$$L \propto Y^{1/3}$$

so holding the probability of destruction fixed while degrading the accuracy requires

$$Y \propto \text{CEP}^{3}$$

**Halving the circular error probable is worth a factor of eight in yield.** A factor of three in accuracy is worth twenty-seven, and a factor of four is worth sixty-four. And since the circular error probable is proportional to the cutoff speed error through the sensitivity derived above, the chain closes,

$$Y \propto (\delta v)^{3}$$

| Cutoff speed error | Circular error probable | Yield needed for the same effect |
|---|---|---|
| 0.613 m/s | 3.70 km | 1.00 |
| 1.000 m/s | 6.04 km | 4.34 |
| 2.000 m/s | 12.08 km | 34.7 |

**One and a third metres per second of additional cutoff error must be paid for with a weapon four and a third times larger.** That is the entire economic argument for the guidance system, for the verniers, and for the propellant utilisation system, and it is why an organisation that could not easily make warheads smaller spent its effort on making cutoff more repeatable instead. The coincidence that the yield factor at one metre per second equals the range sensitivity to three figures is arithmetic accident and carries no meaning. [Gonzalez and Denny 1970][research_gonzalez_denny_1970] computes delivery accuracy in exactly these terms, with terminal effects in [Johnson and Mosely 1964][research_johnson_mosely_1964] and the defensive mirror image in [Fye 1966][research_fye_1966].

### The Angle Is Almost Free, and That Is Not Obvious

The natural assumption is that pointing the vehicle correctly matters as much as stopping it correctly. It does not, and the reason is a stationarity result that falls out of the range law once flight path angle is admitted as a free variable. For a burnout speed $v$ at flight path angle $\gamma$ the range is

$$\tan \frac{\Phi}{2} = \frac{\lambda \sin \gamma \cos \gamma}{1 - \lambda \cos^{2} \gamma}$$

and the angle that maximises it satisfies

$$\cos 2\gamma_{\text{opt}} = \frac{\lambda}{2 - \lambda}$$

which for $\lambda = 0.8281$ gives $\gamma_{\text{opt}} = 22.52$ degrees. **A maximum is stationary, so at that angle the first derivative of range with respect to angle is identically zero**,

$$\left. \frac{\partial R}{\partial \gamma} \right|_{\gamma_{\text{opt}}} = 0, \qquad
\left. \frac{\partial^{2} R}{\partial \gamma^{2}} \right|_{\gamma_{\text{opt}}} = -5.09 \times 10^{4} \, \text{km/rad}^{2}$$

and errors in angle therefore enter the range only at second order,

$$\Delta R \approx \tfrac{1}{2} \left| \frac{\partial^{2} R}{\partial \gamma^{2}} \right| (\delta \gamma)^{2}$$

Evaluating it settles the design question completely.

| Flight path angle error | Range loss, exact | Quadratic estimate |
|---|---|---|
| 0.1 degrees | 0.077 km | 0.078 km |
| 0.5 degrees | 1.905 km | 1.938 km |
| 1.0 degrees | 7.492 km | 7.754 km |

A tenth of a degree of pointing error costs seventy-seven metres of range. The same miss would be produced by a speed error of

$$\delta v = \frac{77}{6040} = 0.0128 \, \text{m/s}$$

which is one part in five hundred and sixty thousand. The ratio of the two is worth writing down, because it is not a constant. Setting the second-order angle loss against the first-order speed loss gives

$$\frac{\delta v_{\text{budget}}}{\delta v_{\text{equiv}}(\delta \gamma)} = \frac{\delta v_{\text{budget}} \, (dR/dv)}{\tfrac{1}{2} \left| \partial^{2} R / \partial \gamma^{2} \right| (\delta \gamma)^{2}} \propto \frac{1}{(\delta \gamma)^{2}}$$

which evaluates to

| Flight path angle error | Equivalent speed error | Fraction of the budget it consumes |
|---|---|---|
| 0.05 degrees | 0.0032 m/s | 1 part in 191 |
| 0.10 degrees | 0.0128 m/s | 1 part in 48 |
| 0.50 degrees | 0.3209 m/s | 1 part in 1.9 |

**Pointing is roughly fifty times more forgiving than speed at a tenth of a degree, and the advantage grows without limit as the errors shrink**, because one term is linear and the other quadratic. The inverse-square dependence is the whole content of the claim and it also sets its limit, since at half a degree the two contributions are comparable and the angle stops being free. An autopilot holding attitude to a tenth of a degree therefore has margin and one holding half a degree does not. The optimum-trajectory literature the result belongs to opens with [Fried and Richardson 1956][research_fried_richardson_1956] and continues through the integrals of [Edelbaum and Pines 1969][research_edelbaum_pines_1969], with the Atlas-specific case worked much later in [Brusch 1977][research_brusch_1977]. This is why the Atlas guidance system is a speed-measuring instrument with an attitude system attached rather than the reverse, and it is the single structural fact that organises everything below. Related sensitivity work of the period includes [Gretz 1962][research_gretz_1962] on error sensitivities in ascent and orbital transfer and [Griner 1967][research_griner_1967] on reducing dispersion by shaping the thrust-time curve.

### Why the X-11 Could Not Address Any of This

The [X-11][related_post_a308_convair_x11] flew eight times to apogees near a hundred and twenty kilometres, which corresponds to a burnout speed under two kilometres per second, or

$$\lambda \approx 0.05$$

At that value the vehicle is not on a ballistic arc in any useful sense and the range law above returns about three hundred kilometres. **The Atlas A could not have demonstrated cutoff accuracy even if it had carried the equipment, because there was no long lever arm for an error to act on.** It also carried no separable booster section, so the staging transient that perturbs the velocity vector did not exist to be measured, and no guidance computer, so there was nothing to measure it with. The previous article concluded that the A settled its structural question on flight one and spent seven more flights debugging. **The X-12 is where the questions that actually decide whether the weapon works were asked for the first time.** [Rockefeller and Alfred 1960][research_rockefeller_alfred_1960] surrounds those questions at the programme level, with [Diegoca 1961][research_diegoca_1961] at the level of the individual missile.

## Programme Origin

### The Same Programme, One Article Later

The designation is WS 107A-1 and the missile family is SM-65, exactly as for the [X-11][related_post_a308_convair_x11]. The design authority remains Karel Bossart at Convair, the customer remains the Western Development Division under Bernard Schriever, and the contractual and institutional arrangements are unchanged. **What changed is the article, not the programme.** The Atlas B is described in the record as the first version carrying all the hardware systems the operational missile would carry, namely an operational sustainer engine, a separable booster section jettisoned on explosive bolts, an airborne guidance computer, an Azusa tracking transponder, and a detachable nose cone.

The dates say something about how the programme was run. The last Atlas A flew on 3 June 1958 and the first Atlas B flew on 19 July 1958, an interval of six weeks. **The B was not waiting on a verdict from the A.** Its articles were in production while the A was still flying, which is consistent with the previous article's finding that the A had answered its own question a year earlier and that everything after that was debugging. Programme-level history belongs to [Rockefeller and Alfred 1960][research_rockefeller_alfred_1960], and the operational context sits in [Walker Bernstein and Lang 2005 Seize the High Ground][book_walker_powell_2005] and [Neufeld 1990 The Development of Ballistic Missiles in the United States Air Force][book_neufeld_1990].

### What October 1957 Did to the Schedule

The Atlas B flew in the year between Sputnik and NASA, and the political environment it flew into is not incidental to what it was asked to do. Sputnik 1 reached orbit on 4 October 1957, Sputnik 2 on 3 November, and the United States responded with Explorer 1 on 1 February 1958 on a Juno I, which is a Redstone derivative rather than an Atlas. The Advanced Research Projects Agency was created in February 1958 specifically to prevent a repetition, and the Army programme that had actually delivered Explorer wrote its own account in [Satterfield and Akens 1958][research_satterfield_akens_1958]. **An Atlas B that could reach orbit was therefore politically valuable independently of whether it could deliver a warhead**, and the programme found a way to demonstrate both with the same vehicle inside six weeks.

That demonstration was Project SCORE, run by the Army and by the Advanced Research Projects Agency, with the communications package designed at the Army Signal Research and Development Laboratory at Fort Monmouth under Kenneth Masterman-Smith. The reported secrecy is extreme even by the standards of the period, with the accessible accounts stating that eighty-eight people knew the project existed. The satellite communications literature the period was writing at the same moment is [Handelsman 1959][research_handelsman_1959] on a stationary passive relay, [Hagan 1960][research_hagan_1960] on polar-orbit relay, [Jakes 1961][research_jakes_1961] on the transatlantic experiment through Echo I, [Haviland 1963][research_haviland_1963] on relay techniques, and [Karrenberg and Lueders 1963][research_karrenberg_lueders_1963] on the orbital aspects of a nonsynchronous system.

## Sizing From First Principles

The keystone is terminal velocity control, and it decomposes into three separate problems that the vehicle solves with three separate mechanisms. The speed at cutoff must be right, the cutoff must be commanded at the right moment, and the impulse delivered after the command must be predictable. The third is the hard one.

### The Cutoff Command Is Not the Cutoff

At sustainer cutoff the vehicle has a burnout mass near 5,395 kilogrammes and the sustainer produces 86,844 pounds of thrust, which is

$$F_{s} = 86{,}844 \times 4.4482 = 386.3 \, \text{kN}$$

so the acceleration in the last instant of powered flight is

$$a = \frac{F_{s}}{m_{bo}} = \frac{386{,}300}{5395} = 71.6 \, \text{m/s}^{2} = 7.30 g$$

The entire error budget of 0.613 metres per second is therefore consumed in

$$\Delta t = \frac{0.613}{71.6} = 8.6 \, \text{ms}$$

**The command must be issued to within about eight milliseconds, and that is the easy part.** The difficulty is what happens afterwards. A liquid engine does not stop when told. Valves close in finite time, the injector and the chamber hold propellant that continues to burn, and the resulting tail-off impulse is a property of the hardware rather than of the command. Taking a tail-off lasting 0.3 seconds at declining thrust, an uncertainty of only five percent in the delivered impulse gives

$$\delta v_{\text{tail}} = \frac{0.05 \times 0.3 \times 386{,}300}{5395} = 1.07 \, \text{m/s}$$

which is **1.8 times the entire error budget**. A missile that simply commands its sustainer to stop cannot meet the accuracy requirement no matter how good its guidance is, because the last thing it does is the least repeatable thing it does. This is precisely the subject of [Kelly 1959][research_kelly_1959], with the transient itself measured in [Rodean 1959][research_rodean_1959], and the model specification for the engine itself survives as [Scott 1963][research_scott_1963] on the Rocketdyne YLR105-NA-7 sustainer. **That the problem is generic rather than peculiar to liquid engines is clear from the solid-motor literature**, where terminating thrust requires deliberately destroying the chamber pressure and the repeatability of doing so is the subject of [Jaroudi and Mcdonald 1964][research_jaroudi_mcdonald_1964] and [Coates and Horton 1970][research_coates_horton_1970]. Every propulsion system that must stop at a commanded velocity confronts the same last-instant uncertainty.

### Which Is Why the Vehicle Has Verniers

The Atlas carries two small pressure-fed vernier engines of roughly a thousand pounds of thrust each. Their conventional description is roll control, which they do provide, but the arithmetic shows the other function is the decisive one. Two verniers give

$$F_{v} = 2 \times 1000 \times 4.4482 = 8.90 \, \text{kN}, \qquad a_{v} = \frac{8900}{5395} = 1.65 \, \text{m/s}^{2}$$

so trimming the full error budget takes

$$t = \frac{0.613}{1.65} = 0.372 \, \text{s}$$

The authority ratio between the two systems is

$$\frac{a_{s}}{a_{v}} = \frac{71.6}{1.65} = 43.4$$

**The verniers convert an eight-millisecond timing problem into a four-hundred-millisecond timing problem, and a factor of forty-three in required precision is the difference between impossible and routine.** The sustainer is shut down early by design, deliberately leaving a velocity deficit, and the verniers then add the remainder under closed-loop control until the measured speed reaches the commanded value, at which point they are cut and their own tail-off is forty-three times less consequential. The design pattern is general and appears wherever a large impulse must be terminated precisely, with [Blaszak and Fahrenholz 1960][research_blaszak_fahrenholz_1960] on thrust control by gas injection and [Platt and Hanner 1965][research_platt_hanner_1965] on the effective specific impulse of a pulsed engine as period treatments of the same idea.

### The Budget Is a Root Sum Square, Which Changes What Is Worth Fixing

The 0.613 metre per second figure is a total, and a total assembled from independent contributions combines in quadrature rather than by addition,

$$\delta v_{\text{tot}} = \sqrt{\sum_{i} \delta v_{i}^{2}}$$

An illustrative allocation makes the consequence visible. The values below are chosen to sum to something near the budget rather than taken from a document, and they are stated as an illustration of the arithmetic rather than as the Atlas allocation.

| Contribution | Equivalent speed error | Share of variance |
|---|---|---|
| Cutoff speed measurement | 0.30 m/s | 26.1 percent |
| Tail-off impulse after vernier trim | 0.25 m/s | 18.1 percent |
| Propellant residual at cutoff | 0.20 m/s | 11.6 percent |
| Attitude at cutoff | 0.15 m/s | 6.5 percent |
| Position and altitude knowledge | 0.20 m/s | 11.6 percent |
| Atmospheric and reentry dispersion | 0.30 m/s | 26.1 percent |
| Root sum square | 0.59 m/s | |

The share each term takes of the total is its share of the variance rather than of the sum,

$$s_{i} = \frac{\delta v_{i}^{2}}{\sum_{j} \delta v_{j}^{2}}$$

and improving one term by a factor $k$ moves the total by

$$\frac{\delta v_{\text{new}}}{\delta v_{\text{old}}} = \sqrt{1 - s_{i} \left( 1 - \frac{1}{k^{2}} \right)}$$

**Quadrature is unforgiving of effort spent on the wrong term.** Halving the largest single contribution moves the total from 0.59 to 0.53, an improvement of 10.3 percent for what would be a major redesign. The relation also fixes a ceiling, because letting $k$ grow without bound gives

$$\lim_{k \to \infty} \frac{\delta v_{\text{new}}}{\delta v_{\text{old}}} = \sqrt{1 - s_{i}} = 0.860$$

so **removing the largest contribution entirely, at infinite cost, would improve the total by 14.0 percent.** Halving it already captures three quarters of everything perfect elimination could buy. Nothing short of improving several terms at once moves the answer, and this is the structural reason accuracy programmes proceed slowly and by increments across many subsystems rather than by one decisive advance.

It also explains a fact about the Atlas that would otherwise look like poor engineering. The reentry body's own dispersion, from ablation asymmetry and from winds at low altitude, sits in the budget alongside everything the guidance system does, and it is not reducible by any improvement to guidance at all. **A perfect cutoff does not give a perfect weapon**, and the guidance engineer's share of the problem has a floor set by aerodynamics. Error analysis in exactly this form was worked out by [Britting 1971][research_britting_1971] and [Nash et al 1972][research_nash_1972], with the reentry contribution in [Platus 1967][research_platus_1967] and [Ammons 1973][research_ammons_1973].

### The Orbital Margin

Here is the result this article is built around, and it is a single division.

The grazing circular orbital speed is the value of $\lambda = 1$,

$$v_{\text{circ}} = \sqrt{g R_{e}} = \sqrt{9.80665 \times 6.371 \times 10^{6}} = 7904 \, \text{m/s}$$

against the 7193 metres per second that a ten-thousand-kilometre ballistic arc requires. The ratio is

$$\frac{v_{\text{circ}}}{v_{bo}} = 1.0989$$

**A weapon of intercontinental range is within ten percent of being a satellite launcher.** In terms of the energy parameter the statement is sharper still, because the maximum-range weapon sits at $\lambda = 0.828$ of the way to orbit and at $\lambda / 2 = 0.414$ of the way to escape, so

$$v_{\text{esc}} = \sqrt{2 g R_{e}} = 11{,}178 \, \text{m/s}$$

and the entire span from the longest-ranged weapon anyone wanted to build to the ability to leave the Earth altogether is a factor of 1.55 in speed. The deficit to be made up is

$$\Delta v = 7904 - 7193 = 711 \, \text{m/s}$$

which is a smaller number than the losses the ascent already absorbs, and the previous article calibrated those at 1337 metres per second. **The Atlas B did not need a new vehicle to reach orbit. It needed to give something up.** [Geckler 1960][research_geckler_1960] carries the staging and performance arithmetic behind that statement on the ideal performance of multistage rockets, [Feldman 1953][research_feldman_1953] on competing power plant components for long-range vehicles, and [Lowrey 1962][research_lowrey_1962] on minimum weight stages, with the launch vehicle the Atlas eventually became specified in [Wolfe 1966][research_wolfe_1966].

### What the Margin Costs

What it had to give up follows from the rocket equation applied to the sustainer alone. The sustainer runs at a specific impulse of 309 seconds, so

$$v_{e} = 309 \times 9.80665 = 3030 \, \text{m/s}$$

and closing a 711 metre per second gap at fixed propellant load requires the burnout mass to shrink by

$$\frac{m_{bo}}{m_{bo}'} = \exp\left( \frac{711}{3030} \right) = 1.2645$$

so

$$m_{bo}' = \frac{5395}{1.2645} = 4266 \, \text{kg}$$

The mass that must be surrendered is

$$\Delta m = 5395 - 4266 = 1129 \, \text{kg}$$

or **20.9 percent of the burnout mass**. That is approximately the mass of a period thermonuclear reentry body, and the trade is therefore exact and physical rather than rhetorical. An Atlas can carry a warhead to ten thousand kilometres or it can carry itself to orbit, and the difference between the two missions is about a tonne. Ascent and injection error sensitivities of the period are [Gretz 1962][research_gretz_1962] and [Beardslee 1964][research_beardslee_1964], and the staging arithmetic underneath belongs to [Schurmann 1957][research_schurmann_1957], [Lubowe 1965][research_lubowe_1965], and [Geckler 1960][research_geckler_1960].

### The Check Against What Actually Orbited

The prediction is testable against the flight, which is unusual for an argument of this kind. Project SCORE placed the entire Atlas B sustainer stage in orbit with a reported on-orbit mass of 3,980 kilogrammes, against the 4,266 kilogrammes the relation above allows,

$$\frac{4266 - 3980}{3980} = +7.2 \, \text{percent}$$

**A calculation carried out entirely from the range law, a published specific impulse, and a burnout mass taken from a different variant reproduces the mass of the first communications satellite to within seven percent.** The agreement should not be oversold, since the burnout mass is an Atlas D figure and the reported on-orbit mass appears elsewhere as 8,660 pounds, which is 3,928 kilogrammes, so the sources themselves disagree by 1.3 percent. What the agreement does establish is that the orbital mission and the weapon mission are the same mission with the payload changed, which is the article's central claim, and that no capability was added to make the second possible. Trajectory design for the launcher this vehicle became appears in [Frazier 1967][research_frazier_1967], and the flight performance evaluations that document the result are [NACA 1967][research_naca_1967], [NACA 1968][research_naca_1968], [NACA 1968, Atlas-Centaur Ac-12 flight perform][research_naca_1968_2], and [NACA 1969, Flight performance of the Atlas-Ag][research_naca_1969_2].

### The Orbit SCORE Actually Reached

The reported orbit is 185 by 1,484 kilometres at 32.3 degrees inclination. Taking those as given,

$$r_{p} = 6556 \, \text{km}, \qquad r_{a} = 7855 \, \text{km}, \qquad a = 7205.5 \, \text{km}$$

the eccentricity is

$$e = \frac{r_{a} - r_{p}}{r_{a} + r_{p}} = 0.0901$$

and the period follows from Kepler's third law,

$$T = 2\pi \sqrt{\frac{a^{3}}{\mu}} = 6087 \, \text{s} = 101.45 \, \text{min}$$

against the reported 101.4 minutes, which agrees to better than a tenth of a percent and confirms the orbital elements are mutually consistent rather than separately rounded. The perigee and apogee speeds are

$$v_{p} = \sqrt{\mu \left( \frac{2}{r_{p}} - \frac{1}{a} \right)} = 8141 \, \text{m/s}, \qquad v_{a} = 6795 \, \text{m/s}$$

and the specific orbital energy is

$$\varepsilon = -\frac{\mu}{2a} = -27.66 \, \text{MJ/kg}$$

against the ballistic case at

$$\varepsilon_{\text{bal}} = \tfrac{1}{2} v_{bo}^{2} - \frac{\mu}{R_{e}} = -36.69 \, \text{MJ/kg}$$

a difference of 9.03 megajoules per kilogramme. Orbit determination for exactly this class of object was being worked out by [Richards 1960][research_richards_1960] and [Richards 1961][research_richards_1961] using Doppler tracking, [Duke 1960][research_duke_1960] from optical tracking, [Siry 1960][research_siry_1960] on the state of the art, [Maxwell and Dorfman 1963][research_maxwell_dorfman_1963] on how accurate it could be made, and the seminar record in [NACA 1960][research_naca_1960].

### The Guidance Requirement Does Not Relax in Orbit

It would be reasonable to expect the orbital mission to be the easier one, and the sensitivity says otherwise. Perturbing the perigee speed and recomputing the apogee gives

| Perigee speed error | Resulting apogee altitude | Change |
|---|---|---|
| 1 m/s | 1488.2 km | +4.2 km |
| 10 m/s | 1526.6 km | +42.6 km |
| 100 m/s | 1923.8 km | +439.8 km |

so the apogee sensitivity is

$$\frac{d h_{a}}{d v_{p}} = 4.24 \, \text{km per m/s}$$

against 6.04 kilometres per metre per second for ballistic range. **The two problems have the same sensitivity to within a factor of one and a half**, which means the guidance system built to hit a target ten thousand kilometres away is neither more nor less than what is needed to place a satellite in a specified orbit. That equivalence is why every early space programme flew on a converted weapon, and it is a quantitative statement rather than a historical observation. [Beardslee 1964][research_beardslee_1964] gives the formal treatment on orbit injection error analysis and [Lange and Parkinson 1965][research_lange_parkinson_1965] on the error equations that connect inertial navigation to orbital determination.

### The Reserve That Has to Be Carried

A vehicle required to reach a specified velocity must carry propellant to cover the flights on which it performs worse than nominal, and that reserve is dead mass on every flight where it is not needed. Sizing it is a statistical exercise, and the Atlas programme ran exactly that calculation by Monte Carlo, in [Ingber 1965][research_ingber_1965].

The arithmetic is short. A reserve covering a dispersion of standard deviation $\sigma_{v}$ at $k$ standard deviations must supply

$$\Delta v_{r} = k \sigma_{v}$$

which at the sustainer exhaust velocity requires a propellant mass of

$$m_{r} = m_{bo} \left( \exp \frac{\Delta v_{r}}{v_{e}} - 1 \right)$$

| Dispersion, one standard deviation | Reserve at three standard deviations | Reserve mass | Range forgone |
|---|---|---|---|
| 10 m/s | 30 m/s | 53.7 kg | 181 km |
| 20 m/s | 60 m/s | 107.9 kg | 362 km |
| 30 m/s | 90 m/s | 162.6 kg | 544 km |

**A three-sigma reserve against a ten metre per second dispersion costs 181 kilometres of range on every flight, including the ones that did not need it.** That is the price of not knowing the vehicle's performance precisely, and it converts an uncertainty directly into a capability loss in kilometres. It is also the reason a programme invests in ground testing that narrows $\sigma_v$, since every metre per second of dispersion removed is six kilometres of range returned. [Peters and Hall 1963][research_peters_hall_1963] reports the engine system test data that narrows it on the Atlas MA-3 engine system, with the propellant loading side in [Whitcombe 1961, Optimum Propellant Loading And Pro][research_whitcombe_1961_2].

### Flight Time, and What Cannot Be Changed After Cutoff

The free-fall arc is an ellipse with semi-major axis

$$a_{\text{bal}} = \frac{R_{e}}{2 - \lambda} = 5437 \, \text{km}$$

and eccentricity

$$e_{\text{bal}} = \sqrt{1 - \lambda (2 - \lambda) \cos^{2} \gamma_{\text{opt}}} = 0.4146$$

Solving Kepler's equation between the two ends of the arc gives a time of flight of

$$t_{f} = 2058 \, \text{s} = 34.3 \, \text{min}$$

with an apogee altitude of

$$h_{\text{apo}} = a_{\text{bal}} (1 + e_{\text{bal}}) - R_{e} = 1319 \, \text{km}$$

The [X-10 article][related_post_a307_north_american_x10] gave the ballistic case as about thirty-two minutes against a hundred and seventy-two for the airbreathing Navaho, and the two figures differ because that estimate used a slightly shorter arc. **The relevant point for this article is that thirty-four minutes is entirely uncontrolled.** The weapon has no actuators, no communications, and no reason for either. Everything is decided before the first second of it, which is the strongest possible statement of why cutoff is the keystone and why the [X-10's][related_post_a307_north_american_x10] problem, which was navigating accurately for nearly three hours, has no counterpart here. [Callaway 1963][research_callaway_1963] reduces trajectory computation to what a range could actually run for the Pacific Missile Range, with the general n-stage simulation in [Juarez 1961][research_juarez_1961] and modern reconstructions of the same problem in [Xu et al 2020][research_xu_2020] and [Dudush and Snovydovych 2026][research_dudush_snovydovych_2026].

### The Earth Is Turning

One term that does not appear in the range law as written is the rotation of the Earth, and for a weapon fired between continents it is not small. The surface speed at the latitude of Cape Canaveral is

$$v_{\text{rot}} = \omega_{e} R_{e} \cos \phi = 7.292 \times 10^{-5} \times 6.371 \times 10^{6} \times \cos 28.5^{\circ} = 408 \, \text{m/s}$$

which is 5.68 percent of the burnout speed. Adding and subtracting it as a bound on the azimuth effect gives a range credit of about 3,195 kilometres for a due-east launch and a penalty of about 2,065 kilometres for a due-west one, an east-to-west swing of some 5,260 kilometres on a nominal ten thousand. Only the component along the launch azimuth $A$ is captured, so to first order the credit is

$$\delta R = \frac{dR}{dv} \, \omega_{e} R_{e} \cos \phi \cos A$$

giving 2,466 kilometres due east, 1,744 at an azimuth of 45 degrees, and nothing due north or south. **The first-order estimate of 2,466 kilometres falls 23 percent short of the exact 3,195**, which is a useful warning in its own right, since a 408 metre per second perturbation is far outside the range over which the linear sensitivity that governs the whole article remains valid. **This is an upper bound rather than a computed range, because the launch site latitude changes along the arc**, but the order is right and it explains why a missile's stated range is meaningless without a direction. It also makes azimuth a geodetic quantity rather than a navigational one, since the launch heading must be referred to the same figure of the Earth as the target, and the astronomical determination of a geodetic azimuth is its own discipline in [Bhattacharji 1970][research_bhattacharji_1970]. Optimising the heading rather than merely choosing it is [Frazier 1967][research_frazier_1967] and [Brusch 1977][research_brusch_1977]. It also explains the SCORE inclination of 32.3 degrees against a launch site latitude of 28.5, since an orbit cannot be less inclined than its launch latitude and the excess measures how far the azimuth was rotated away from due east.

### The Earth Is Not a Sphere, and That Matters More Than the Rotation

Every relation in this article has treated the Earth as a sphere of radius 6371 kilometres, and for a weapon required to land within 3.7 kilometres that approximation is not merely imprecise but disqualifying. The reference ellipsoid has

$$R_{\text{eq}} = 6378.137 \, \text{km}, \qquad R_{\text{pol}} = R_{\text{eq}} (1 - f), \qquad f = \frac{1}{298.257}$$

so the polar radius is 6356.752 kilometres and the difference is

$$\Delta R = 21.4 \, \text{km}$$

against a miss budget of 3.704 kilometres. **The flattening of the Earth is 5.8 times the entire permitted miss.** Expressed as fractions, the flattening is one part in 298 while the accuracy requirement is one part in 2,700, so the figure of the Earth is nine times coarser than the tolerance.

Two consequences follow and both are large. **The target's position must be known in the same coordinate frame as the launch site**, to a few hundred metres, across an intercontinental baseline, and in 1958 the geodetic connection between continents was itself uncertain at the kilometre level. **And the gravity field is not that of a point mass**, so the free-fall arc is not the ellipse computed above. The size of the departure follows from the same flattening. The leading zonal harmonic contributes a relative perturbing acceleration of

$$\frac{\Delta a}{g} \approx \frac{3}{2} J_{2} \left( \frac{R_{e}}{r} \right)^{2} = 1.62 \times 10^{-3}, \qquad J_{2} = 1.083 \times 10^{-3}$$

which is 0.162 percent of gravity, and acting over a free-fall arc of 2,058 seconds it displaces the impact point by of order

$$\Delta s \sim \tfrac{1}{2} \, \Delta a \, t_{f}^{2} = 34 \, \text{km}$$

**Nine times the entire miss budget.** That figure is an upper bound, since the perturbation is not constant along the arc and part of it acts along-track where the range law absorbs it, but no plausible reduction brings it below the tolerance. A weapon aimed on a point-mass gravity field misses by tens of kilometres. The oblateness term that dominates it was being worked out at exactly this moment, in [King-Hele 1958][research_king_hele_1958], [Blitzer 1959][research_blitzer_1959], [Message 1960][research_message_1960], [King-Hele 1962][research_king_hele_1962], and [Sarychev 1962][research_sarychev_1962], and the satellites that measured it were flying on vehicles like this one.

**The ballistic missile therefore created a geodetic requirement it could not itself satisfy**, and the resolution came from the same orbital capability the X-12 demonstrated. That circularity is worth naming, because it is the clearest case in this series of a weapon programme generating a scientific programme as a precondition for its own accuracy rather than as a by-product.

### How the Requirement Was Actually Met

The geodesy the weapon needed did not exist in 1958 and was largely built in the decade that followed, using satellites launched on vehicles of this family. Tracing it is worth doing, because the sequence is unusually clean and because it shows the article's own numbers being determined by other people for other reasons.

**Before satellites the field was determined from the ground and the ground could not see across an ocean.** The classical method computes the shape of the geoid from surface gravity measurements, in [Hirvonen 1954][research_hirvonen_1954], and connects a station's astronomical position to its geodetic one through the deflection of the vertical, in [Tsuboi and Hayatu 1954][research_tsuboi_hayatu_1954] and [Wolf 1954][research_wolf_1954]. The result is a datum that is internally consistent over a continent and arbitrarily offset from the datum of any other continent, and the state of that art on the eve of the satellite era is [Fischer 1961][research_fischer_1961]. **Two continents surveyed separately are two coordinate systems**, and a weapon aimed from one at the other is aiming at a number rather than a place. That the Soviet Union was solving the same problem with its own ellipsoid is [Izotov 1959][research_izotov_1959].

**A satellite sees the whole field at once, because it is inside it.** The perturbations in its orbit are a direct measurement of the harmonics of the potential, which is the theory in [Batrakov 1963][research_batrakov_1963] and [Liu 1974][research_liu_1974], and the determination proceeded rapidly once orbits were being tracked accurately. The even zonal harmonics are worked out in [King-hele et al 1963][research_king_hele_1963], [King-hele et al 1964][research_king_hele_1964], [Kozai 1964][research_kozai_1964], [Kozai 1964, New Determination of Zonal Harmoni][research_kozai_1964_2], [Cook 1965][research_cook_1965], [King-Hele and Cook 1965][research_king_hele_cook_1965], and [King-Hele et al 1966, Even zonal harmonics in the earth'][research_king_hele_1966_2], the odd ones in [King-Hele et al 1965, The odd zonal harmonics in the Ear][research_king_hele_1965_2] and [King-hele et al 1966][research_king_hele_1966], the progress summarised in [King-hele 1965][research_king_hele_1965], and the expansion pushed to the twenty-fifth order in [Felsentreger and Victor 1966][research_felsentreger_victor_1966]. **The non-zonal terms, which is to say the departures from rotational symmetry, needed Doppler tracking**, and that is [Guier 1963][research_guier_1963], with the error analysis of the Navy Doppler geodetic system itself in [Guier et al 1965][research_guier_1965].

**The geoid and the datum followed.** Determining the geoid from satellite observation is [Anderle 1966][research_anderle_1966], the equatorial radius and zero-order undulation are [Rapp 1967][research_rapp_1967] and [Veis 1968][research_veis_1968], the accuracy attainable is [Rapp 1973][research_rapp_1973], and the definitional questions are [Rapp 1974][research_rapp_1974] and [Moritz 1966][research_moritz_1966] on the boundary-value problem underneath. The purely geometric route, connecting continents by simultaneous observation of a satellite from stations on both, is the triangulation net whose error behaviour is [Lortie 1966][research_lortie_1966], with the dedicated instrument in [Nichols 1974][research_nichols_1974] and the Soviet equivalent assessed in [Wareham 1972][research_wareham_1972]. **A world datum tying the continents together is the deliverable**, and it arrives in [Eitschberger and Grafarend 1974][research_eitschberger_grafarend_1974], with regional orientations such as [Mather and Fryer 1970][research_mather_fryer_1970] and [Mather 1971][research_mather_1971] as the working examples. Combining astronomical and geodetic data statistically is [Heitz 1971][research_heitz_1971] and [Jordan 1972, Self-consistent statistical models][research_jordan_1972_2], and where the field went next, to altimetry and satellite-to-satellite tracking, is [Hudson 1971][research_hudson_1971], [Comfort 1973][research_comfort_1973], and [Fubara and Mourad 1974][research_fubara_mourad_1974].

**Sixteen years separate the first Atlas B flight from a published world geodetic datum.** For most of the period during which the Atlas force stood alert, the coordinates of its targets were less well known than the guidance system's contribution to the error budget, and this article's careful accounting of cutoff velocity to two thirds of a metre per second describes only the part of the problem the missile engineers owned. **The other part belonged to geodesists and was solved with the missile's own product.** [Remmer 1974][research_remmer_1974] is a small reminder that the discipline was still arguing about its own foundations while all of this was going on.

## Dependent Systems

Each system below is dimensioned against the cutoff requirement, and the ordering is by dependency. The structure and the tankage are not repeated here, since the [previous article][related_post_a308_convair_x11] derived them and nothing about them changed.

### The Booster Section, and What Jettison Does to the Vehicle

The Atlas B carries two booster engines of 341,130 pounds combined thrust and one sustainer of 86,844 pounds, all ignited on the ground. In newtons,

$$F_{b} = 1517.4 \, \text{kN}, \qquad F_{s} = 386.3 \, \text{kN}, \qquad F_{\text{tot}} = 1903.7 \, \text{kN}$$

so the lift-off thrust-to-weight ratio is

$$\frac{F_{\text{tot}}}{m_{0} g} = \frac{1{,}903{,}700}{117{,}900 \times 9.80665} = 1.647$$

and the booster provides 79.7 percent of the thrust. At the respective specific impulses of 282 and 309 seconds the mass flows are

$$\dot{m}_{b} = \frac{F_{b}}{282 g} = 548.7 \, \text{kg/s}, \qquad \dot{m}_{s} = \frac{F_{s}}{309 g} = 127.5 \, \text{kg/s}$$

for a combined 676.2 kilogrammes per second. Taking booster cutoff near 135 seconds, the remaining mass is

$$m_{1} = m_{0} - (\dot{m}_{b} + \dot{m}_{s}) t = 117{,}900 - 676.2 \times 135 = 26{,}615 \, \text{kg}$$

and the acceleration immediately before the event is

$$\frac{F_{\text{tot}}}{m_{1}} = 71.5 \, \text{m/s}^{2} = 7.29 g$$

Jettisoning a booster package of about three tonnes leaves 23,615 kilogrammes under sustainer thrust alone, giving

$$\frac{F_{s}}{m_{1} - m_{j}} = 16.4 \, \text{m/s}^{2} = 1.67 g$$

**Acceleration falls by a factor of 4.37 in the space of one event.** That discontinuity is the largest single transient the airframe sees after lift-off, it arrives while the guidance system is integrating, and it is the reason the staging event is a guidance problem rather than a mechanical one. Reconstructing the ideal velocity in two phases gives

$$\Delta v_{b} = 282 g \ln \frac{117{,}900}{26{,}615} = 4116 \, \text{m/s}$$

$$\Delta v_{s} = 309 g \ln \frac{23{,}615}{5395} = 4474 \, \text{m/s}$$

for a total of 8590 metres per second against the 8530 the previous article obtained from a single-phase calculation at the booster specific impulse, an agreement of 0.7 percent from independent inputs. The sustainer propellant remaining is 18,220 kilogrammes, which at 127.5 kilogrammes per second is a burn of

$$t_{s} = \frac{18{,}220}{127.5} = 142.9 \, \text{s}$$

so the sustainer phase is slightly longer than the booster phase and delivers slightly more of the velocity. **The half-stage is not a coda. It is more than half the job.** Staging optimisation of the period, which is what decides that split, is [Schurmann 1957][research_schurmann_1957], [Parkyn 1958, 2809. A note on rocket staging][research_parkyn_1958_2], [Geckler 1960][research_geckler_1960], [Lubowe 1965][research_lubowe_1965] by dynamic programming, [Gray and Alexander 1965][research_gray_alexander_1965] optimising cost against weight, [Martin 1973][research_martin_1973] on the optimum stage weight distribution, and [Burghes 1974][research_burghes_1974], with the effect of the choice on the resulting trajectory in [Randall 1970][research_randall_1970] and drag admitted in [Adkins 1970][research_adkins_1970].

### Separation Clearance

The jettisoned skirt must clear a vehicle that is still accelerating, and the arithmetic shows what does the work. At booster cutoff the dynamic pressure is near a hundred pascals, so with a skirt reference area of

$$A = \pi r^{2} = \pi (1.524)^{2} = 7.30 \, \text{m}^{2}$$

the differential deceleration from drag on the discarded section is

$$a_{d} = \frac{C_{d} q A}{m_{j}} = \frac{1.0 \times 100 \times 7.30}{3000} = 0.243 \, \text{m/s}^{2}$$

which separates the two bodies by only

$$\tfrac{1}{2} a_{d} t^{2} = 0.12 \, \text{m}$$

in a full second. The sustainer, meanwhile, is accelerating at 16.4 metres per second squared, so

$$\tfrac{1}{2} a_{s} t^{2} = 8.18 \, \text{m}$$

in the same second and about two metres in the first half second. **Separation is achieved by the sustainer flying away from the skirt rather than by the skirt falling behind**, which is why the sustainer must already be running before the booster section is released and why an arrangement that shut everything down and then restarted would have been far harder. The aerodynamic and jet-interference environment of the event occupies [Binion et al 1962][research_binion_1962] and [Binion 1964][research_binion_w_1964], and the Atlas record of separation dynamics on later configurations comes from [Heath et al 1965][research_heath_1965] on the retarding rocket and [Heath et al 1967][research_heath_1967] on Atlas-Centaur staging.

### The Sustainer

The sustainer is a single Rocketdyne chamber, and the model specification survives in the archive as [Scott 1963][research_scott_1963]. Its function follows directly from the acceleration discontinuity above. Running at a fifth of the total thrust on a vehicle that has already shed three quarters of its mass, it delivers a long low-acceleration phase during which the velocity changes slowly enough for the guidance loop to converge. The instantaneous rate of change of speed in the last seconds of sustainer burn is

$$\dot{v} = \frac{F_{s}}{m} \quad \text{rising from} \quad 16.4 \quad \text{to} \quad 71.6 \, \text{m/s}^{2}$$

as the tanks empty. The ratio between the two is worth naming, because it is not an independent quantity,

$$\frac{a_{\text{end}}}{a_{\text{start}}} = \frac{F_{s} / m_{bo}}{F_{s} / m_{1}} = \frac{m_{1}}{m_{bo}} = \frac{23{,}615}{5395} = 4.38$$

**The factor by which the vehicle becomes harder to stop is exactly its sustainer mass ratio**, which is the same quantity the rocket equation rewards, since

$$\Delta v_{s} = v_{e} \ln \frac{m_{1}}{m_{bo}} = 4474 \, \text{m/s}$$

is a logarithm of the identical number. **The mass fraction that makes the Atlas an intercontinental weapon is the same mass fraction that makes it hard to stop**, and this is the article's first genuine tension between the [previous one's][related_post_a308_convair_x11] keystone and this one's. A heavier vehicle would be easier to terminate accurately and could not reach the target.

Knowing where on that curve the engine actually sits requires knowing its specific impulse to better than the accuracy the mission demands, which is a harder measurement than it sounds and which the period solved by inference from the trajectory rather than by instrumenting the engine. [Powers 1960][research_powers_1960] determines vacuum specific impulse precisely from trajectory data, and [Dafler 1962][research_dafler_1962] sets out what the quantity does and does not mean for vehicle performance. The thermal instrumentation that a stand test relies on has its own response limits, in [Hoff 1967][research_hoff_1967], and spectroscopic monitoring of a running engine is [Strauss 1964][research_strauss_1964]. **A specific impulse quoted to three figures is a trajectory reconstruction, not a measurement**, which is worth remembering given that the 309 second figure carries most of this article's orbital arithmetic.

### Propellant Utilisation

A cutoff commanded on measured velocity is only available if propellant remains when the velocity is reached. If the two tanks do not empty together the engine shuts down on depletion of whichever runs out first, at a velocity nobody chose. The propellant utilisation system exists to prevent that, by trimming the mixture ratio in flight so that both tanks reach depletion simultaneously. The residual mass stranded by a mixture ratio error $\delta r$ on a nominal ratio $r$ is approximately

$$m_{\text{res}} \approx m_{p} \frac{|\delta r|}{(1 + r)^{2}} \cdot (1 + r)$$

and the velocity that residual would have bought is

$$\delta v = v_{e} \ln \left( 1 + \frac{m_{\text{res}}}{m_{bo}} \right)$$

so even a residual of fifty kilogrammes on a burnout mass of 5,395 costs

$$\delta v = 3030 \ln (1.00927) = 28 \, \text{m/s}$$

which is **forty-five times the entire error budget**. Propellant utilisation is therefore not an efficiency measure but an accuracy measure, and the period wrote about it in exactly those terms in [Whitcombe 1961, Optimum Propellant Loading And Pro][research_whitcombe_1961_2], with the Atlas programme's own difficulties recorded in [General Dynamics Convair 1966, Propellant Utilization][research_div_1966] and the control dynamics of the equivalent Centaur system in [Ringland and Stubblefield 1965][research_ringland_stubblefield_1965], [Magrini 1967][research_magrini_1967], and [Berns et al 1968][research_berns_1968].

### The Autopilot, and a Bending Mode That Will Not Stay Still

Before the guidance system can command a velocity, the vehicle has to be a rigid body that points where it is told, and it is not one. The Atlas is a twenty-three metre tube of about three metres diameter, a fineness ratio near 7.5, with no fins and a centre of pressure ahead of the centre of mass. **It is statically unstable in pitch and yaw throughout the atmospheric phase and flies only because the engines are gimballed.**

The instability has a rate. Taking a pitch inertia for a uniform rod of

$$I = \frac{m L^{2}}{12} = 2.65 \times 10^{6} \, \text{kg m}^{2}$$

at a representative mass of sixty tonnes, with a normal force coefficient slope near two and the centre of pressure four metres ahead of the centre of mass, the divergence rate at a maximum dynamic pressure of 35 kilopascals is

$$\omega = \sqrt{\frac{q A C_{N\alpha} \Delta x}{I}} = 0.879 \, \text{rad/s}$$

so an attitude disturbance grows by a factor of $e$ in

$$\tau = \frac{1}{\omega} = 1.14 \, \text{s}$$

The control authority available against it is one degree of gimbal producing

$$\dot{\omega} = \frac{F \, \delta \, \ell}{I} = 0.119 \, \text{rad/s}^{2} = 6.84 \, \text{deg/s}^{2}$$

which is ample. **The difficulty is not authority but bandwidth**, because the loop that stabilises the rigid body must be fast compared with 1.14 seconds and slow compared with the structure.

The structure sets the upper limit. Treating the vehicle as a free-free beam with a thin-shell second moment of area

$$I_{xx} = \pi r^{3} t = 5.6 \times 10^{-3} \, \text{m}^{4}$$

the first bending frequency is

$$f_{1} = \frac{\beta_{1}^{2}}{2 \pi L^{2}} \sqrt{\frac{E I_{xx}}{\mu}}, \qquad \beta_{1} L = 4.730$$

which evaluates to

$$f_{1} = 4.32 \, \text{Hz} = 27.2 \, \text{rad/s}$$

The autopilot bandwidth must therefore live inside a window of

$$\frac{2 \pi f_{1}}{\omega} = 31$$

between the rate the vehicle diverges and the rate its structure resonates. Thirty-one to one sounds generous and is not, because a loop must be several times faster than the divergence and several times slower than the mode to avoid exciting it, which consumes most of the interval.

**And now the connection to the previous article that this one has otherwise avoided.** The bending frequency above assumes a fixed elastic modulus and geometry, and for a pressure-stabilised shell that assumption fails. The [X-11 article][related_post_a308_convair_x11] established that the Atlas structure has no compressive strength without tank pressure, so its effective bending stiffness is a function of a state variable that is being consumed throughout the flight. **The bending mode the autopilot filter is designed to reject moves during the ascent**, in a direction and by an amount that depends on the pressurisation schedule rather than on the airframe alone. The previous article raised this for pogo, and the same physics applies to the attitude loop with a different consequence. Missile structural dynamics of the period is surveyed in [Wood 1961][research_wood_1961], the launch-phase problem in [Gerald and Runyan 1962][research_gerald_runyan_1962], optimal control of a flexible vehicle in [Rynaski 1967][research_rynaski_1967], and automated autopilot design for exactly this class of problem in [Hauser 1972][research_hauser_1972]. The programme's own record survives as [General Dynamics Convair 1966, Autopilot][research_div_1966_4], and a pneumatic alternative the period considered is [Griffith and Byrd 1963][research_griffith_byrd_1963].

### Slosh, Which Gets Worse Exactly When It Matters

The propellant is a free surface in a tank a little over three metres across, and its first lateral mode in a cylindrical tank under axial acceleration $a$ is

$$f_{s} = \frac{1}{2\pi} \sqrt{\frac{1.841 \, a}{r}}$$

The Atlas is unusual in that its axial acceleration varies by a factor of 4.4 during the sustainer phase alone, so

$$f_{s} = 0.708 \, \text{Hz at } 1.67 g, \qquad f_{s} = 1.480 \, \text{Hz at } 7.30 g$$

**The slosh frequency rises by a factor of 2.09 through the phase in which cutoff accuracy is decided**, while the bending frequency falls as propellant leaves the tanks and the effective mass distribution changes. Two frequencies moving toward each other while the vehicle approaches the one instant that must be precise is an unattractive arrangement, and it is why the propellant slosh problem on this vehicle is a cutoff-accuracy problem rather than only a stability problem. [Wilner et al 1960][research_wilner_1960] built an instrument to see it, with baffle damping in [Stephens 1965][research_stephens_1965].

### Guidance, and Why It Sat on the Ground

The Atlas A through D used radio guidance. The missile carried an inertial reference and a transponder, a ground station tracked it and computed the corrections, and the corrections were sent back up by radio. To a modern reader this looks like a compromise forced by immature technology, and it partly was, but the sensitivity analysis above shows it was also the right architecture for the problem as posed.

The quantity that must be measured to one part in eleven thousand is speed, and speed relative to the ground is exactly what a ground-based Doppler measurement produces directly. An inertial platform, by contrast, produces speed by integrating acceleration, so its velocity error accumulates as

$$\delta v(t) = \int_{0}^{t} \varepsilon_{a} \, dt' = \varepsilon_{a} t$$

for an accelerometer bias $\varepsilon_a$, and over a powered flight of about 280 seconds a bias of only

$$\varepsilon_{a} = \frac{0.613}{280} = 2.2 \times 10^{-3} \, \text{m/s}^{2} = 2.2 \times 10^{-4} g$$

exhausts the entire budget. **Two hundred and twenty micro-g of accelerometer bias was not achievable in 1958 and is not trivial now.**

The gyroscopes carry a companion requirement that is easier to state and harder to intuit. A platform that has tilted by an angle $\theta$ resolves a component of gravity into its horizontal accelerometers, so a static tilt gives a velocity error of $g \theta t$ and the allowance is

$$\theta \leq \frac{\delta v}{g t} = 2.23 \times 10^{-4} \, \text{rad} = 46 \, \text{arcseconds}$$

If instead the tilt accumulates at a constant drift rate $\varepsilon$, then $\theta = \varepsilon t$ and the error integrates twice,

$$\delta v = \tfrac{1}{2} g \varepsilon t^{2}, \qquad \varepsilon \leq \frac{2 \, \delta v}{g t^{2}} = 1.59 \times 10^{-6} \, \text{rad/s}$$

which is

$$\varepsilon \leq 0.329 \, \text{degrees per hour}$$

**A third of a degree per hour, and gyroscopes of the period drifted at of order one degree per hour.** The gap between the available instrument and the required one is therefore a factor of about three rather than the orders of magnitude the difficulty of the problem suggests, and the honest reading is that all-inertial guidance was close in 1958 rather than remote. What the ground link bought was not a capability that did not exist but a margin, and the margin mattered because the accelerometer and the gyroscope errors add in quadrature alongside everything else in the budget.

The period instrument literature supports that reading rather than the one the eight-year gap suggests. Measuring drift at all required a dedicated instrument, in [Byerly 1957][research_byerly_1957], and the mechanisms that produce it were being isolated one at a time, with gimbal-supported vibration effects in [Crawley and Maunder 1966][research_crawley_maunder_1966], rate-gyroscope response in [Gryglaszewski 1963][research_gryglaszewski_1963], and low angular momentum designs in [Pijoan 1970][research_pijoan_1970]. **Alignment on the pad is a separate problem from drift in flight and is the one a ground-guided missile can avoid entirely**, since it needs no absolute azimuth reference of its own, and gyrocompass alignment to arbitrary attitudes is [Kouba and Mason 1962][research_kouba_mason_1962]. Where the technology eventually went is visible in [Harding and Lawson 1968][research_harding_lawson_1968] on a superconducting gyroscope and its drift model, and the design trends that followed are [George 1974][research_george_1974]. The statistical machinery for propagating all of it through a guidance loop arrives with [Taylor and Price 1974][research_taylor_price_1974]. Putting the measurement on the ground removes the integration entirely, at the price of a radio link and a vehicle that cannot be fired if the link is jammed or the station is destroyed, which is exactly why the later Atlas E and F went all-inertial once components allowed. The period literature on both sides of that trade includes [Whitcombe 1961][research_whitcombe_1961], [Broxmeyer 1962][research_broxmeyer_1962] on damping an inertial system, [Britting 1971][research_britting_1971] on unified error analysis, [Wilkinson 1971][research_wilkinson_1971] on the floated gyroscope error model, and [Becker 1973][research_becker_1973] on command guidance as a control system.

The comparison with the [X-10][related_post_a307_north_american_x10] is instructive and runs the other way. The Navaho needed autonomous navigation because it flew for nearly three hours over hostile territory and a ground link was not available. The Atlas needed accurate velocity for about five minutes over friendly territory and a ground link was. **The two vehicles chose opposite architectures for the same reason, which is that each put the measurement where the physics of its own mission allowed it to be put.**

### Azusa

The tracking system that supported this was Azusa, a radio interferometer developed at Convair and installed at Cape Canaveral by about 1954, which by the end of 1958 could follow a missile some six hundred nautical miles downrange. Its lineage is worth noting, since it emerged from the same NUL-774 and MX-774 work at Consolidated Vultee that produced the Atlas airframe itself. **The vehicle and the instrument that measured it came out of the same building.**

An interferometer measures a direction cosine from the phase difference between two antennas separated by a baseline $B$. For a signal of wavelength $\lambda_r$ the fringe spacing in angle is

$$\Delta \theta_{\text{fringe}} = \frac{\lambda_{r}}{B}$$

At C-band near five gigahertz the wavelength is 6.00 centimetres, so

| Baseline | Fringe spacing | One percent of a fringe | Cross-range error at 1111 km |
|---|---|---|---|
| 10 m | 5.996 mrad | 59.96 µrad | 66.6 m |
| 50 m | 1.199 mrad | 11.99 µrad | 13.3 m |
| 100 m | 0.600 mrad | 6.00 µrad | 6.7 m |

where the one percent figure is an assumed phase-measurement fraction rather than a published performance, and is stated here to show the scaling rather than to characterise the instrument. The velocity measurement is the more important one and is easier. A Doppler shift $f_d$ corresponds to a range rate

$$\dot{r} = \frac{f_{d} \lambda_{r}}{2}$$

so at six centimetres a one-hertz frequency resolution resolves

$$\dot{r} = 0.030 \, \text{m/s}$$

and the 0.613 metre per second budget corresponds to about twenty hertz, which is undemanding. **The physics is on the side of the ground station, and this is the quantitative reason radio guidance was good enough to build an operational weapon around.** The technique itself is borrowed rather than invented. Radio interferometry was developed for astronomy, and the instrument that established it is [Ryle 1952][research_ryle_1952], with the tracking variant appearing in [Rowson 1962][research_rowson_1962] and the multiple-baseline arrangement that resolves the fringe ambiguity in [Gerharz 1963][research_gerharz_1963]. **A missile tracker and a radio telescope are the same instrument pointed at different things**, and the ambiguity problem is identical in both, since a single baseline gives a direction cosine only to within an integer number of fringes. [Vickers and Dyer 1971][research_vickers_dyer_1971] measures radio interferometer noise in exactly this application, with Doppler position and velocity determination in [Hix 1968][research_hix_1968] and radar-derived velocity in [Saunders 1965][research_saunders_1965].

### Where the Loop's Latency Actually Comes From

A ground-based guidance loop invites an obvious objection, which is that the signal has to travel. It does not survive arithmetic. At a slant range of five hundred kilometres the round trip is

$$t_{\text{prop}} = \frac{2d}{c} = 3.34 \, \text{ms}$$

against a cutoff window of 8.6 milliseconds. Propagation is a third of the window, which is significant but not disqualifying, and it shrinks with range rather than growing, since the vehicle is closest to the station when accuracy matters least and the geometry was chosen accordingly. **The binding latency was computation, not distance**, which is why the ground station carried a computer large enough that it could not have been flown.

The sample rate matters more. At cutoff the vehicle gains speed at 71.6 metres per second squared, so between successive updates at rate $f$ the speed changes by

$$\Delta v = \frac{a}{f}$$

giving 71.6 metres per second at one hertz, 7.16 at ten, and 1.43 at fifty. **Even a fifty hertz loop cannot resolve the error budget from samples alone**, which means the cutoff command has to be predicted forward from a fitted trajectory rather than triggered on a measurement, and the prediction is where the guidance equations do their work. [MacPherson 1963][research_macpherson_1963] formulates explicit guidance for exactly this purpose, with the flight control integration in [Russell 1964][research_russell_1964] and the command guidance formulation in [Becker 1973][research_becker_1973].

### The Nose Cone

The Atlas B carried a detachable nose cone, which the Atlas A did not. Its design problem is set by the reentry velocity, which for a minimum-energy intercontinental trajectory is the burnout velocity returned. Using the classical Allen and Eggers result for a ballistic entry into an exponential atmosphere of scale height $H$ at inertial flight path angle $\gamma_e$, the peak deceleration is

$$a_{\max} = \frac{v_{e}^{2} \sin \gamma_{e}}{2 e H}$$

which for 7193 metres per second at 22.5 degrees and a scale height of 7.2 kilometres gives

$$a_{\max} = 506 \, \text{m/s}^{2} = 52 g$$

and is **independent of the ballistic coefficient**, a result the [previous article][related_post_a308_convair_x11] also used. The ballistic coefficient sets where it happens rather than how large it is,

$$h_{\max} = H \ln \frac{\rho_{0} H}{\beta \sin \gamma_{e}}, \qquad \beta = \frac{m}{C_{d} A}$$

so a body of 1,400 kilogrammes on a one-metre base has

$$\beta = \frac{1400}{1.0 \times 0.785} = 1783 \, \text{kg/m}^{2}, \qquad h_{\max} = 18.4 \, \text{km}$$

with the speed there reduced to

$$v = v_{e} e^{-1/2} = 4363 \, \text{m/s}$$

The stagnation-point heating at that condition, from the Sutton and Graves correlation, is

$$\dot{q} = 1.83 \times 10^{-4} \sqrt{\frac{\rho}{R_{n}}} \, v^{3} = 6.62 \times 10^{6} \, \text{W/m}^{2} = 662 \, \text{W/cm}^{2}$$

where the constant is the SI value and the correlation returns watts per square metre, so the conversion is stated rather than folded in.

**A heavy body arrives low and fast, which minimises the time available for heat to soak into the structure and maximises the rate at which it arrives.** That is the ablation problem, and it is why a high ballistic coefficient is chosen for accuracy and paid for in heat shield. The period record on this begins with [Scherberg and Rubin 1953][research_scherberg_rubin_1953] on decelerations of a ballistic missile on reentry, [Roberts 1960][research_roberts_1960] on ablation shield requirements, [Stetson 1964][research_stetson_1964] on cone ablation results, [Dolton and Reed 1966][research_dolton_reed_1966] on char-layer response in high-performance ballistic reentry, and [Thomas and Perlbachs 1967][research_thomas_perlbachs_1967] on applying ground test data to reentry vehicle design.

### Telemetry Through the Plasma

A reentering body ionises the air ahead of it, and an ionised sheath reflects radio waves below its plasma frequency

$$f_{p} = \frac{1}{2\pi} \sqrt{\frac{n_{e} e^{2}}{\varepsilon_{0} m_{e}}} \approx 8.98 \sqrt{n_{e}} \, \text{Hz}$$

with the electron density in reciprocal cubic metres. Inverting it gives the density at which a given link fails.

| Link | Frequency | Electron density at cutoff |
|---|---|---|
| Telemetry, very high frequency | 250 MHz | $7.75 \times 10^{14}$ per cubic metre |
| Telemetry, S-band | 2.2 GHz | $6.00 \times 10^{16}$ per cubic metre |
| Azusa, C-band | 5.0 GHz | $3.10 \times 10^{17}$ per cubic metre |

Inverting the plasma frequency relation gives the critical density directly,

$$n_{e} = \left( \frac{f}{8.98} \right)^{2}$$

so the ratio between any two links is the square of their frequency ratio,

$$\frac{n_{e,2}}{n_{e,1}} = \left( \frac{f_{2}}{f_{1}} \right)^{2} = \left( \frac{2200}{250} \right)^{2} = 77.4$$

**S-band tolerates seventy-seven times the ionisation that very high frequency does**, which is the whole reason telemetry moved up in frequency, and it is a square-law consequence rather than an incremental improvement. The problem is not confined to reentry either, since the exhaust plume of a large liquid engine is itself conducting and can break down an antenna during powered flight, which is the subject of [Poehler 1961][research_poehler_1961]. Reentry attenuation for S-band telemetry specifically was measured by [Golden 1969][research_golden_1969], the diagnostic instruments flown to measure the sheath are [Frankenthal 1964][research_frankenthal_1964] and [Fuhs et al 1966][research_fuhs_1966], and telemetry hardware built to survive the environment comes from [Wright and Ruscus 1959][research_wright_ruscus_1959] and [Mermagen 1964][research_mermagen_1964].

**This is where the ground-based guidance architecture stops being free.** A missile that depends on a radio link for its velocity measurement has an interval, at the end of powered flight and again at reentry, in which the link degrades for reasons that have nothing to do with the equipment. The Atlas cut off before the worst of it, which is one more reason the cutoff had to be predicted forward rather than commanded on a live measurement.

### Instrumentation, Telemetry, and the Range

A development flight is an instrument, and the accuracy question above cannot be answered without measuring the trajectory more accurately than the missile flies it. That is a hard requirement and the period took it seriously, in [Cooper 1961][research_cooper_1961] on the accuracy of measuring ballistic missile trajectories and [Gerlach 1965][research_gerlach_1965] on high-accuracy instrumentation for non-steady flight measurement. [Schweppe 1964][research_schweppe_1964] estimates a reentry body's state and ballistic coefficient in real time from tracking data, and the Kalman techniques that later made it routine are [Aldrich and Krabill 1972][research_aldrich_krabill_1972]. Simulation support for the vehicle as a whole comes from [Juarez 1961][research_juarez_1961], whose general n-stage missile dynamics program is the kind of tool that made a ten-flight programme interpretable. The physical instrumentation behind it is [Bonney 1960][research_bonney_1960] on radar ballistic instrumentation, [Matson 1963][research_matson_1963] on the airborne transponder that closes the tracking loop, and [Belsterling 1965][research_belsterling_1965] on the analog computer driving the range safety display. **The bottleneck was rarely the sensor and usually the reduction**, which is the subject of [Kingsley 1967][research_kingsley_1967], because a flight produces more data in five minutes than a period computing installation could process in a day.

## The Flight Test Record

Ten Atlas B vehicles flew from Cape Canaveral between 19 July 1958 and 4 February 1959, from Launch Complexes 11, 13, and 14. Six are recorded as successes.

| Date | Serial | Pad | Result | Note |
|------|--------|-----|--------|------|
| 1958-07-19 | 3B | LC-11 | failure | flight control failure at T plus 43 s |
| 1958-08-02 | 4B | LC-13 | success | first booster separation |
| 1958-08-29 | 5B | LC-11 | success | |
| 1958-09-14 | 8B | LC-14 | success | |
| 1958-09-18 | 6B | LC-13 | failure | turbopump failure at T plus 82 s |
| 1958-11-18 | 9B | LC-11 | partial | upgraded turbopumps, premature shutdown |
| 1958-11-29 | 12B | LC-14 | success | full range, 6,325 statute miles |
| 1958-12-18 | 10B | LC-11 | success | orbited SCORE |
| 1959-01-16 | 13B | LC-14 | failure | loss of thrust at T plus 121 s |
| 1959-02-04 | 11B | LC-11 | success | |

Two entries carry the weight of the programme and the rest are the programme earning the right to have them. The flight test reporting apparatus that produced these entries survives as [Diegoca 1961][research_diegoca_1961], with range trajectory practice in [Callaway 1963][research_callaway_1963] and the measurement accuracy question in [Cooper 1961][research_cooper_1961].

### The Full-Range Flight

On 28 or 29 November 1958, depending on the source, missile 12B flew 6,325 statute miles down the Atlantic Missile Range. Converting,

$$6325 \times 1.609344 = 10{,}179 \, \text{km} = 5496 \, \text{nautical miles}$$

which requires

$$v_{bo} = 7222 \, \text{m/s}$$

or 29 metres per second more than the ten-thousand-kilometre case used throughout this article. **That flight is the moment the vehicle became an intercontinental ballistic missile in fact rather than in intention**, and it is the first demonstration by the United States of a full-range delivery. The date disagreement between sources is minor and is recorded rather than resolved, since one account gives 28 November while the flight-by-flight compilation gives 29 November.

The velocity margin is worth noting. Reaching 10,179 kilometres rather than 10,000 required four tenths of one percent more speed, and the sensitivity relation gives the same answer from the other direction,

$$\frac{\delta R}{R} = S \frac{\delta v}{v} \quad \Rightarrow \quad \frac{179}{10000} = 4.34 \times \frac{29}{7193} = 0.0175$$

which reproduces the 1.79 percent range increment to within the rounding of the inputs. The relation that governs the weapon's accuracy is the same relation that governs its reach, and there is no way to have one without the other. Minimum-energy trajectory work of the period underlying both includes [Stancil 1963][research_stancil_1963] and [Ostner 1962][research_ostner_1962], with the closed-form treatment in [Punga and Campbell 1962][research_punga_campbell_1962].

### SCORE

Three weeks later, on 18 December 1958, missile 10B did not shut down at a ballistic velocity. The entire sustainer stage entered orbit carrying a 68 kilogramme communications package built into the fairing pods, with the vehicle body itself acting as the antenna structure. The satellite carried two redundant tape recorders of four minutes capacity each, received on 150 megahertz, and transmitted on 132 megahertz. It broadcast a pre-recorded Christmas message from President Eisenhower, operated on batteries for about twelve days, and reentered on 21 January 1959 after thirty-four days in orbit.

Converting the mission duration into revolutions,

$$N = \frac{34 \times 86400}{6087} = 483 \, \text{orbits}$$

of which the batteries supported

$$N_{\text{active}} = \frac{12 \times 86400}{6087} = 170$$

The recorder capacity against the orbital period is a ratio worth stating, since

$$\frac{T}{t_{\text{tape}}} = \frac{6087}{240} = 25.4$$

means the satellite could store four minutes of the ninety-nine and a half it spent out of contact on each revolution. **SCORE was a store-and-forward relay with a duty cycle of four percent**, and the architecture of every later communications satellite is a response to that number. A four-minute tape at three kilohertz of voice bandwidth carries, by the Nyquist criterion,

$$n = 2 B t = 2 \times 3000 \times 240 = 1.44 \times 10^{6} \, \text{samples}$$

which at six bits per sample is about a megabit, and the entire information content of the first voice broadcast from space therefore fits comfortably in a modern text message attachment. The communications satellite literature being written around it includes [Handelsman 1959][research_handelsman_1959], [Hagan 1960][research_hagan_1960], [Jakes 1961][research_jakes_1961], [Haviland 1963][research_haviland_1963], [Karrenberg and Lueders 1963][research_karrenberg_lueders_1963], and [Gruenberg and Johnson 1964][research_gruenberg_johnson_1964], and the orbit determination that made a satellite findable comes from [Denham 1965][research_denham_1965] and [Townsend 1966][research_townsend_1966].

### What the Downlink Actually Managed

The record describes the broadcast as weak, and it is worth checking whether the physics agrees. At 132 megahertz the wavelength is 2.27 metres, and the free-space loss at the 1,484 kilometre apogee is

$$L = \left( \frac{4 \pi d}{\lambda_{r}} \right)^{2} = 138.3 \, \text{dB}$$

Assuming a transmit power near eight watts, a body-mounted antenna of unity gain, and a ground antenna of ten decibels, the received power is

$$P_{r} = \frac{P_{t} G_{t} G_{r}}{L} = 1.19 \times 10^{-12} \, \text{W} = -89.3 \, \text{dBm}$$

against a noise floor at a system temperature of 2,000 kelvin and a six kilohertz bandwidth of

$$N = k T_{\text{sys}} B = -127.8 \, \text{dBm}$$

for a signal-to-noise ratio of 38.6 decibels. **The link was comfortable for a tracking station and unavailable to the public**, which resolves the apparent contradiction, since the reported weakness refers to what a listener without a directional antenna at 132 megahertz could receive and not to the link the project actually flew. That is also why the message reached most Americans as a rebroadcast on commercial news rather than directly. The assumed transmit power and antenna gains are estimates and are flagged as such in the Epistemic State. Diversity reception and the error behaviour of links of this class belongs to [Daly 1967][research_daly_1967], with Doppler-based observer positioning from the same kind of signal in [Hix 1968][research_hix_1968].

### Orbital Lifetime

The thirty-four day lifetime is consistent with the orbit and the vehicle. The area-to-mass ratio of a three-metre diameter stage at 3,980 kilogrammes is

$$\frac{A}{m} = \frac{\pi (1.524)^{2}}{3980} = 1.83 \times 10^{-3} \, \text{m}^{2}/\text{kg}$$

giving a ballistic coefficient of

$$\beta = \frac{m}{C_{d} A} = \frac{3980}{2.2 \times 7.30} = 248 \, \text{kg/m}^{2}$$

which is heavy for a satellite and is why an object with a 185 kilometre perigee survived as long as it did. The mean specific energy shed per revolution is

$$\frac{\Delta \varepsilon}{N} = \frac{1}{483} \left( \frac{\mu}{2 a} - \frac{\mu}{2 R_{e}} \right) = 7.5 \, \text{kJ/kg}$$

Atmospheric drag on satellites was an active subject at exactly this moment, in [Jastrow and Pearse 1957][research_jastrow_pearse_1957], [Parkyn 1958][research_parkyn_1958], [Wildhack 1958][research_wildhack_1958], [Brouwer and Hori 1961][research_brouwer_hori_1961], [Westerman 1963][research_westerman_1963], and [Geyling 1964][research_geyling_1964], with the oblateness terms that dominate the orbit's other secular behaviour in [King-Hele 1958][research_king_hele_1958], [Blitzer 1959][research_blitzer_1959], [Message 1960][research_message_1960], and [Message 1960, On Mr King-Hele's Theory of the Ef][research_message_1960_2]. **Oblateness and drag are not independent**, since the flattening changes the density a satellite meets at a given altitude and therefore its lifetime, which is [Johnston 1966][research_johnston_1966], and it torques the body as well, in [Schlegel 1966][research_schlegel_1966]. Determining where an object of this kind actually is remained hard enough to support its own literature, in [Moriarty 1966][research_moriarty_1966] and [Lubowe 1969][research_lubowe_1969].

### What the Ten Flights Support Statistically

Six of ten is a success rate of 0.6, and the standard error is

$$\sigma = \sqrt{\frac{p(1-p)}{n}} = \sqrt{\frac{0.24}{10}} = 0.155$$

against the Atlas A at 0.50 plus or minus 0.177. The improvement is 0.10, and pooling the two programmes gives a pooled proportion of 0.556 and a standard error on the difference of

$$\sigma_{\Delta} = \sqrt{p(1-p) \left( \frac{1}{n_{A}} + \frac{1}{n_{B}} \right)} = 0.236$$

so

$$z = \frac{0.10}{0.236} = 0.42$$

**The Atlas B is not measurably more reliable than the Atlas A even though it carried more systems and did far more.** That is not a criticism of either. It is a statement about what eighteen flights can support, and the previous article made the same point about eight. Reaching a five-percentage-point standard error would need

$$n = \frac{p(1-p)}{\sigma^{2}} = 99 \, \text{flights}$$

which is not how a missile programme establishes reliability. The statistical machinery for doing better than counting successes arrived later and is [Taylor and Price 1974][research_taylor_price_1974], whose covariance analysis propagates component errors through a guidance loop without requiring flights at all. **A programme that cannot afford a hundred flights must substitute analysis for sampling**, and that substitution is the intellectual content of the entire reliability discipline that followed. Reliability came from the Difficulties Review process instead, and the five surviving volumes of [General Dynamics Convair 1966, Propellant Utilization][research_div_1966], [General Dynamics Convair 1966, Propulsion Interface][research_div_1966_2], [General Dynamics Convair 1966, Pneumatics][research_div_1966_3], [General Dynamics Convair 1966, Autopilot][research_div_1966_4], and [General Dynamics Convair 1966, Electrical][research_div_1966_5] are what that looked like written down. The flight test reports for individual missiles are [Diegoca 1961][research_diegoca_1961].

Placing the failures on the mass and acceleration history makes the pattern sharper. At the combined mass flow of 676.2 kilogrammes per second computed above, the first failure at T plus 43 seconds occurred with

$$m = 117{,}900 - 676.2 \times 43 = 88{,}823 \, \text{kg}$$

still aboard, which is before maximum dynamic pressure and during the phase where the vehicle is least controllable, so a flight control failure there is the least surprising of the four. The turbopump failure at T plus 82 seconds came after

$$676.2 \times 82 = 55{,}448 \, \text{kg}$$

or 49.3 percent of the propellant load had passed through the machinery, which is a plausible point for a wear or thermal failure rather than a start transient. The loss of thrust at T plus 121 seconds is the most informative, since nominal booster cutoff is near 135 seconds and the vehicle at that moment has

$$m = 36{,}080 \, \text{kg}, \qquad \frac{F_{\text{tot}}}{mg} = 5.38$$

so it failed fourteen seconds short of staging at more than five times its own weight. **Three of the four failures are in the booster phase and none is in a system the Atlas B introduced.**

**The failure causes point away from the new systems.** Flight control on the first, a turbopump on the fifth, a premature shutdown on the sixth, and a loss of thrust on the ninth are all propulsion and control faults rather than guidance, separation, or nose cone faults. The systems the Atlas B was built to prove are not the systems that broke, which repeats the pattern the Atlas A showed when its structure survived and its plumbing did not.

## Comparison With Ground Prediction

### What Could Be Tested on the Ground

The engine could be tested, and was, on stands that ran full-duration burns. The specification in [Scott 1963][research_scott_1963] is a document produced by that process. The guidance computation could be tested against simulated trajectories, in the manner of [Juarez 1961][research_juarez_1961]. The nose cone could be tested in shock tunnels and on sounding rockets, which is what [Stetson 1964][research_stetson_1964] and [Thomas and Perlbachs 1967][research_thomas_perlbachs_1967] describe.

### What Could Not

**The separation event could not be reproduced at all.** It occurs at about a hundred pascals of dynamic pressure, which is a vacuum by any ground standard, with two bodies of very different mass separating under thrust while a plume expands into the gap between them. Jet interference at that altitude was measured by [Binion et al 1962][research_binion_1962] and [Binion 1964][research_binion_w_1964], and the reason those papers exist is that no ground facility of the period could do it. A wind tunnel can produce the Mach number or the pressure altitude but not both at scale with a running engine.

**The ground wind loads on the pad could be measured and were, and they were a genuine problem.** A slender pressure-stabilised vehicle standing on a launcher in a crosswind sheds vortices and responds to them, and the Atlas is the vehicle the extreme-value analysis of that problem was written about, in [Miller 1967][research_miller_1967]. The general treatment spans [Buell 1964, Some sources of ground-wind loads][research_buell_1964_2], [Bohne 1964][research_bohne_1964], and the meeting record in [NACA 1966][research_naca_1966], with buffet pressures for the Mercury and Atlas configuration collated in [Shelton 1966][research_shelton_1966] and the launch-vehicle buffeting problem surveyed in [Rainey 1964][research_rainey_1964]. This is the one part of the flight environment the ground could reproduce well, because the vehicle is stationary and the wind is real.

**The cutoff transient could not be reproduced in the flight configuration.** A static test measures thrust decay against a rigid stand. In flight the same decay acts on a vehicle whose structure is a pressurised membrane, whose propellant is sloshing, and whose acceleration is falling through the transient. The one measurement that matters, namely the total impulse delivered after the command, is exactly the one the stand cannot reproduce, and this is why the article's whole error budget rests on flight data.

**The accuracy could not be measured better than the range could measure it.** This deserves a relation rather than an assertion, because it sets a hard requirement on the ground segment. An imperfect instrument inflates the measured scatter in quadrature,

$$\sigma_{\text{meas}}^{2} = \sigma_{\text{true}}^{2} + \sigma_{\text{inst}}^{2}$$

so holding the apparent inflation below a fraction $\eta$ requires

$$\frac{\sigma_{\text{inst}}}{\sigma_{\text{true}}} \leq \sqrt{(1 + \eta)^{2} - 1}$$

which for a five percent ceiling gives 0.320, or an instrument **3.1 times better than the missile it is certifying**. In the units used throughout that is 0.196 metres per second of range measurement error against a 0.613 metre per second budget. A ground station accurate to a few metres per second cannot certify a missile required to be accurate to two thirds of one, so the instrumentation had to be improved alongside the weapon. That is a recurring shape in this series and appeared already in the [X-7][related_post_a304_lockheed_x7] and [X-10][related_post_a307_north_american_x10] articles.

## What the Data Changed

### Into the Operational Force

The Atlas B fed directly into the C, D, E, and F variants and into the first American operational intercontinental ballistic missile force. The radio guidance the B flew stayed through the D and was replaced by all-inertial guidance in the E and F. The drift budget derived above says that transition was nearer than it looks, since the requirement is a third of a degree per hour against period instruments at of order one, so

$$\frac{\varepsilon_{\text{period}}}{\varepsilon_{\text{required}}} \approx \frac{1.0}{0.329} = 3.0$$

**A factor of three, not the orders of magnitude the eight-year gap between the B and the F might suggest.** What took the time was not the gyroscope but everything around it, namely the calibration, the alignment on the pad, the thermal control, and the confidence that a system with no external reference could be trusted with the mission, and none of those appears in the error budget. The Atlas force was short-lived as a weapon, being retired from that role by 1965, and the reason is that a cryogenic missile requiring lengthy fuelling was overtaken by storable and solid-fuelled weapons that could be launched in minutes. The inertial systems that replaced radio guidance in the E and F are the subject of [Whitcombe 1961][research_whitcombe_1961], [Broxmeyer 1962][research_broxmeyer_1962], [Larson 1965][research_larson_1965] for the contemporary Titan III, [Amacker and Graff 1965][research_amacker_graff_1965] on how such systems were tested, and [Widnall et al 1974][research_widnall_1974] on improving the observability of their error sources, with the precise-timing dependency in [Ehrsam et al 1978][research_ehrsam_1978]. The manned application the launcher inherited appears in [Boynton 1967][research_boynton_1967].

### Into the Launch Vehicle Line

The more consequential inheritance is the one SCORE announced. The Atlas became a launch vehicle and stayed one for decades, flying Mercury, the Agena upper stage, Centaur, and a long series of planetary missions. **The transition required no new capability, only a different payload**, which is the quantitative content of the twenty-one percent burnout mass trade computed above. Atlas-Centaur staging and separation are documented in [Heath et al 1965][research_heath_1965] and [Heath et al 1967][research_heath_1967], the interstage structural behaviour in [Lall 1965][research_lall_1965], and the propellant utilisation lineage in [Ringland and Stubblefield 1965][research_ringland_stubblefield_1965] and [Berns et al 1968][research_berns_1968].

### Why the Atlas Lost, and It Was Not Accuracy

This article has spent its length on accuracy, and the honest conclusion is that accuracy is not what decided the Atlas force's fate. The vehicle was retired from the weapon role by 1965, less than seven years after the X-12 first flew, and the reason is arithmetic of a different kind.

An intercontinental ballistic missile arrives in 34.3 minutes, which this article computed from the range law. Warning of a launch arrives strictly later than the launch, so the time available to respond is less than that. The Atlas burns liquid oxygen, which cannot be stored aboard indefinitely, so a round held on alert must be fuelled before it can be fired. Taking a loading time on the order of fifteen minutes,

$$\frac{t_{\text{load}}}{t_{\text{flight}}} = \frac{15}{34.3} = 0.44$$

**A missile that consumes forty-four percent of the adversary's flight time before it can be launched is not a second-strike weapon, and no improvement in accuracy repairs that.** The problem is worse than the ratio suggests, because boil-off means a loaded vehicle cannot simply be held loaded. Against an ullage margin $\mu$ the holding time before a top-up is required is

$$t_{\text{hold}} = \frac{\mu}{\dot{m} / m}$$

so a five percent margin against a one percent per day loss gives

$$t_{\text{hold}} = \frac{0.05}{0.01} = 5 \, \text{days}$$

**Readiness therefore has a clock on it even when nothing is wrong**, which makes indefinite alert impossible in principle rather than merely inconvenient, and every top-up is a maintenance action on a fuelled weapon.

The cryogenic literature of the period is unusually direct about how hard this was. Storage vessel design is [Hallett et al 1960][research_hallett_1960], the measurement of boil-off itself is [Jacobs 1964][research_jacobs_1964] and [Flack et al 1969][research_flack_1969], and subcritical storage under varying acceleration is [Polk 1962][research_polk_1962]. Transferring the fluid without warming or contaminating it is [Humphrey 1961][research_humphrey_1961] and [Greenfield 1960][research_greenfield_1960], with contamination as a distinct hazard in [Foster et al 1960][research_foster_1960] and [Foster 1961][research_foster_1961], and the overpressure behaviour of a liquid oxygen and kerosene combination in [Smalley 1961][research_smalley_1961]. **Discharging a large tank without collapsing its pressure is its own problem** and is exactly what a balloon tank cannot tolerate, which is [Nein and Head 1962][research_nein_head_1962], with the pressurisation systems that answer it in [Morey and Koshar 1961][research_morey_koshar_1961], [Coxe and Tatom 1962][research_coxe_tatom_1962], and [Kaplan 1961][research_kaplan_1961]. **Every one of those documents is a reason the storable and solid-fuelled competitors won**, and none of them is about accuracy.

Minuteman, which replaced it, loads nothing. A solid motor is ready when it is built, and the whole of the Atlas's careful accuracy engineering was made irrelevant by a propellant choice. **The keystone this article identified is real and was decisive for whether the weapon worked, and it was not decisive for whether the weapon was kept**, which is a distinction worth drawing explicitly because an article organised around a keystone will tend to blur it. Alert-rate economics belongs to [Kravitsky 2007][research_kravitsky_2007], the post-Cold-War role to [O'Rourke 2010][research_o_rourke_2010], and silo deployment survivability as an optimisation is [Dai et al 2019][research_dai_2019].

The consolation is that the launch vehicle role had no such requirement. **A satellite launch can wait for its propellant**, and every property that made the Atlas a poor weapon after 1962 was irrelevant to the mission it then performed for forty years.

### Into the Communications Satellite

SCORE established three things that were not obvious in 1958. A satellite could carry a useful payload rather than a beacon, a spacecraft could be commanded from the ground to record and replay, and the entire upper stage could serve as the spacecraft. The store-and-forward duty cycle of four percent computed above is precisely the constraint that drove the next decade toward higher orbits, and the geostationary answer was already being written down in [Handelsman 1959][research_handelsman_1959] before SCORE flew. **SCORE is the demonstration that made the argument about orbits a practical one rather than a theoretical one.**

Its immediate successor makes the lineage explicit. Project Courier took the store-and-forward architecture SCORE had flown and built a purpose-designed satellite around it, in [Maresca 1960][research_maresca_1960] and [Mottley et al 1960][research_mottley_1960], and the tape recorder that had been the weak component became a subject in its own right, in [Clement 1965][research_clement_1965] on qualifying one for launch vibration and [Bahm and Hoffman 1971][research_bahm_hoffman_1971] on making one last in orbit. **The four percent duty cycle was attacked from both ends at once**, by raising the orbit so the satellite was visible for longer and by making the relay active so that nothing needed storing at all, and the active-repeater line runs through [Aein 1964][research_aein_1964], [Blum 1966][research_blum_1966], and [Horvath and Blum 1966][research_horvath_blum_1966]. The system studies that followed are [Whelan 1968][research_whelan_1968] and [Sundstrom and Brown 1969][research_sundstrom_brown_1969]. **Within a decade the store-and-forward satellite had become a special case rather than the only case**, which is the ordinary fate of a first demonstration.

## The Contemporary Literature

The relations this article derives are not historical curiosities. Every one of them is still an active research subject, and in several cases the modern work is a direct continuation of the period problem rather than a distant relative.

**Ascent guidance has become an optimisation problem solved onboard.** The Atlas computed corrections on the ground because it could not compute them in the air. Modern vehicles solve a constrained optimal control problem in flight, and the enabling result is that the ascent problem can be posed convexly, in [Miao et al 2022][research_miao_2022] on successive convexification for replanning after a nonfatal anomaly and [Hwang 2019][research_hwang_2019] on full-space quasi-Lagrange-Newton trajectory optimisation for a multistage vehicle. [Cho et al 2021, Integrated Framework for Staging a][research_cho_2021_2] integrates staging and trajectory optimisation under range safety constraints, which is the same coupling between where the pieces fall and where the payload goes that the Atlas managed by choosing an azimuth.

**Staging optimisation continues, with a changed objective function.** [Jo and Ahn 2021][research_jo_ahn_2021] optimises staging while accounting for velocity losses, which is the calibration this article inherited from the previous one, and [Jo and Ahn 2022][research_jo_ahn_2022] replaces minimum mass with minimum lifecycle cost, which inverts the criterion the Atlas was designed against. [Sabaghzadeh and Khansari 2022][research_sabaghzadeh_khansari_2022] treats it as a multi-objective problem, and [Jo et al 2021][research_jo_2021] analyses staging and injection performance together in the way this article's orbital margin section does.

**Separation dynamics is now a multibody simulation problem.** [Pamadi et al 2016][research_pamadi_2016] develops the constraint force methodology, [Albertson et al 2012][research_albertson_2012] runs end-to-end trajectory simulation including separation, and [Zhang et al 2022][research_zhang_2022] applies model-based systems engineering to a first-stage separation system. The aerodynamic side occupies [Yan et al 2025][research_yan_2025] and [Kumar et al 2023][research_kumar_2023], and [Ermakov et al 2025][research_ermakov_2025] pursues separation without pyrotechnics, which is the direct descendant of the explosive bolts the Atlas B introduced.

**Inertial navigation error analysis is the same subject with better instruments.** [Cavacece 2024][research_cavacece_2024] works the error analysis in quaternion form, and the accelerometer bias budget derived above is the quantity all of it is about. [Arthur and Kemp 2025][research_arthur_kemp_2025] assesses where ballistic missile guidance accuracy has arrived, which is the natural endpoint of the one-part-in-eleven-thousand requirement this article opens with.

**Upper stages left in orbit are now a recognised hazard.** SCORE was an entire stage placed deliberately in orbit and left there, and [Trushlyakov et al 2024][research_trushlyakov_2024] passivates propellant residues in exactly that situation, [Aslanov and Sizov 2020][research_aslanov_sizov_2020] studies removal of a spent upper stage, and [Ingram 2026][research_ingram_2026] assesses remediation and salvage of orbital-discarded stages. **The first communications satellite is also the first large piece of deliberate orbital debris**, and the modern literature treats the two facts as the same fact.

**Reentry remains a guidance problem as much as a heating problem.** [Su et al 2026][research_su_2026] treats initial descent guidance for a lifting reentry vehicle, which is the capability the Atlas nose cone deliberately did not have, since a purely ballistic body is more accurate precisely because it cannot be steered and therefore cannot be steered wrongly.

## Where the Framing Breaks Down

**The error budget is reconstructed, not documented.** The two nautical mile circular error probable used throughout is a plausible figure for an early Atlas and is not taken from a programme document found for this article. Everything downstream of it, including the headline one part in eleven thousand seven hundred, scales inversely with that assumption. The scaling is linear and immediate,

$$\delta v = \frac{\text{CEP}}{dR/dv}$$

| Assumed circular error probable | Speed budget | Fractional requirement |
|---|---|---|
| 1 nautical mile | 0.307 m/s | 1 part in 23,458 |
| 2 nautical miles | 0.613 m/s | 1 part in 11,729 |
| 5 nautical miles | 1.533 m/s | 1 part in 4,692 |

so at five nautical miles the problem is materially easier and at one it is roughly twice as hard as anything this article claims. **The qualitative conclusion that speed dominates angle survives any choice, because it rests on a stationarity argument rather than on a number, but the specific figures do not.**

**Treating cutoff as the whole problem understates the atmosphere.** The range law used here is for a spherical non-rotating Earth with no atmosphere on the way up or down, and the reentry body's own dispersion, from ablation asymmetry, from roll resonance, and from winds at low altitude, contributes to the miss distance independently of anything the guidance system did. [Platus 1967][research_platus_1967] on roll resonance and [Ammons 1973][research_ammons_1973] on low-level wind measurement error are the shape of that contribution, with the high-altitude wind response of a missile in [Maas 1962][research_maas_1962], the criterion problem in [Bidwell 1967][research_bidwell_1967], and the Atlas programme's own flight-wind restriction procedure in [Mattson 1965][research_mattson_1965]. **The reentry body has a dispersion budget of its own and it was treated as a design variable**, which is exactly what [Johannessen 1964][research_johannessen_1964] does for the Mark 12 body, while the aerodynamic behaviour that produces it is [Murphy 1961][research_murphy_1961] on the pitching and yawing motion of nose cone configurations and [Sharenson 1966][research_sharenson_1966] on high-altitude drag effects. An article organised around cutoff accuracy will naturally attribute the whole error to cutoff, and that is wrong.

**The orbital margin argument assumes the propellant is there to spend.** The twenty-one percent burnout mass trade holds at fixed propellant load, and it is an idealisation in which the vehicle flies the same ascent and simply stops later. A real orbital mission flies a different trajectory with different losses, so the true trade is somewhat worse than computed. The seven percent agreement with the SCORE mass is therefore partly fortuitous and should be read as an order-of-magnitude confirmation rather than as a validation.

**The spherical Earth assumption is carried throughout and it is inadequate to the requirement.** This is stated in the sizing discussion above and it deserves repeating as a limitation of the analysis rather than of the missile. Every range figure in this article is computed on a sphere, and the flattening alone is 5.8 times the miss budget, so the numbers here establish scalings and sensitivities and do not establish where anything would land. A real targeting solution requires an ellipsoidal Earth, a gravity model, and a geodetic tie between launch site and target, none of which this article attempts.

**The X-12 designation may not describe an article at all.** This is the same difficulty the [previous article][related_post_a308_convair_x11] recorded and it is discussed below.

## What the X-12 Was Worth

Separating what this vehicle established from what it merely carried is the useful exercise, because the Atlas B carried a great deal and established less than the inventory suggests.

**It established that the staging event works.** The second flight, on 2 August 1958, was the first booster separation, and every Atlas afterwards depended on it. The acceleration discontinuity of a factor of 4.37, the clearance provided by a sustainer that never stops, and the guidance system's ability to integrate through the transient were all demonstrated on that flight and never seriously doubted again.

**It established full range.** The 12B flight on 28 November 1958 is the vehicle's most consequential single result and the one the programme existed to obtain. Nothing before it had shown that the United States possessed an intercontinental ballistic missile.

**It established that the same vehicle reaches orbit.** SCORE is the demonstration and the twenty-one percent mass trade is the explanation.

**It established almost nothing about accuracy.** This is the finding that cuts against the article's own organisation and it should be stated plainly. Ten development flights with a mixture of objectives cannot measure a circular error probable, and the accuracy the Atlas eventually achieved was established by the operational force over years. **The X-12 posed the accuracy problem and built the machinery for it. It did not answer it.** The answer belongs to the D, E, and F, and to the all-inertial systems the E and F introduced.

**It established nothing at all about basing, alert posture, or reaction time**, which turned out to matter more than accuracy for the Atlas specifically, since the vehicle's cryogenic propellant and lengthy fuelling made it unsuited to the alert requirements that emerged almost immediately.

## The Designation, Which by Now Is the Series Question

The X-12 designation is attributed to the Atlas B in compilations and no document found for this article uses it. That is the identical situation the [X-11][related_post_a308_convair_x11] article recorded, and the three readings it offered apply here without modification. The designation may have been assigned and never used operationally, leaving a registry entry and nothing else. It may be a later retrofit by compilers filling a numeric gap that the Atlas B fits neatly. Or it may have had a genuine period use that the accessible record simply does not reach.

What this article can add is one observation about the mechanism. The [X-10][related_post_a307_north_american_x10] article concluded that the X-8, X-9, and X-10 were RTV-A test vehicles absorbed wholesale into the X series, and the [X-11][related_post_a308_convair_x11] article found that explanation does not extend to the Atlas A because it was never an RTV-A vehicle. **The X-12 confirms the limit rather than resolving it.** The Atlas B is the fifth consecutive X number attached to a vehicle that was never a research aircraft, and the second consecutive one attached to a weapon system article in serial production. Whatever mechanism assigned these numbers, it was not the mechanism that produced the [X-1][related_post_a298_bell_x1] through the [X-6][related_post_a303_convair_x6], and the closing article of this series will have to carry at least two and probably more.

## The Source Base

**The Atlas record in the defence archive is genuinely rich and it is not evenly distributed.** Querying the Defense Technical Information Center through the Crossref publisher prefix returns Flight Test Working Group reports for individual missiles, the five volumes of the Difficulties Review covering propellant utilisation, the propulsion interface, pneumatics, the autopilot, and the electrical system, and the model specification for the sustainer engine itself. **What it does not return is anything using the X-12 designation.**

The asymmetry the [previous article][related_post_a308_convair_x11] identified holds and deepens. The Navaho, cancelled in 1957, leaves four years of programme reporting. The Atlas, which flew for sixty years as a launch vehicle, leaves a continuous literature in which the weapon programme is the earliest layer and the launch vehicle work is the thickest. **The archive is a record of what happened to a programme afterwards rather than of what it was**, and for this article that bias is helpful, since the Atlas-Centaur separation and propellant utilisation studies of the mid-1960s document mechanisms that the Atlas B introduced and that nobody wrote up at the time.

The satellite side has the opposite shape. Project SCORE was run under extreme secrecy by a different service, and the accessible technical record for the payload is thin compared with the vehicle that carried it. What survives well is the surrounding orbital mechanics and communications literature, which was being written at exactly that moment for reasons that had nothing to do with SCORE.

**The third body of literature this article draws on was not sought and turned out to be the largest.** The geodesy section exists because the equation pass established that the flattening of the Earth exceeds the miss budget by a factor of 5.8, and the harvest assembled for a missile article contained nothing about datums, geoids, or zonal harmonics. A sweep aimed at them returned an entire discipline, openly published in the astronomical and geodetic journals, running continuously from the early 1950s to the mid 1970s and overlapping the Atlas force's whole operational life. **The weapon literature is classified, fragmentary, and archived under project numbers. The literature the weapon depended on is none of those things**, because determining the shape of the Earth was not a secret and could not usefully have been made one. That asymmetry is the most striking source-base feature of this article and it was found by following a relation rather than a topic.

## Epistemic State

**Historical fact, well supported.** Ten Atlas B vehicles flew from Cape Canaveral between 19 July 1958 and 4 February 1959 from Launch Complexes 11, 13, and 14, with six recorded successes. The Atlas B was the first Atlas with an operational sustainer, a separable booster section on explosive bolts, an airborne guidance computer, an Azusa transponder, and a detachable nose cone. Missile 12B flew 6,325 statute miles in late November 1958. Missile 10B placed the Project SCORE payload in orbit on 18 December 1958, which broadcast a recorded message from President Eisenhower, operated about twelve days on batteries, and reentered on 21 January 1959. SCORE was run by the Army and the Advanced Research Projects Agency with the payload developed at Fort Monmouth. The Atlas A through D used radio guidance and the E and F used all-inertial guidance. Azusa was a radio interferometer at Cape Canaveral developed from work at Consolidated Vultee.

**Reported but from compilations rather than programme documents.** The X-12 designation itself, which no document found for this article uses. The flight-by-flight serials, pads, and failure causes. The engine thrusts of 341,130 and 86,844 pounds and the specific impulses of 282 and 309 seconds. The masses used throughout, which are Atlas D figures carried forward from the [previous article][related_post_a308_convair_x11] because Atlas B figures were not found. The SCORE orbit of 185 by 1,484 kilometres at 32.3 degrees. The on-orbit mass, which is reported as both 3,980 kilogrammes and 8,660 pounds, figures that differ by 1.3 percent. The 88-person secrecy figure. The date of the full-range flight, which sources give as both 28 and 29 November 1958.

**Assumed for the purpose of calculation and stated as such.** The two nautical mile circular error probable. The booster cutoff time of 135 seconds and the jettisoned booster package mass of three tonnes. The vernier thrust of a thousand pounds each. The 1,400 kilogramme reentry body on a one-metre base. The SCORE transmit power of eight watts and the ground antenna gain of ten decibels. The one percent phase-measurement fraction in the Azusa table. The five percent tail-off impulse uncertainty. **The period gyroscope drift of order one degree per hour**, against which the derived requirement of 0.329 is compared, which is the least well sourced number in the article and which the conclusion drawn from it depends on directly. The illustrative six-term error allocation, which sums to something near the budget and is not the Atlas allocation. The five percent ullage margin in the boil-off holding time. The five percent measurement-inflation ceiling used to size the range instrumentation requirement. The one percent per day liquid oxygen boil-off rate. Every one of these is an engineering estimate chosen to show a scaling, and each is identified at the point of use.

**Engineering analysis, derived here and independently checkable.** The range law and its inversion for 10,000 kilometres. The range-to-velocity sensitivity of 6.04 kilometres per metre per second and its dimensionless form of 4.34. The velocity budget of 0.613 metres per second and the fractional requirement of one part in 11,728. The optimum flight path angle of 22.52 degrees, the vanishing first derivative of range with respect to it, the second derivative, and the resulting table of range losses. The cutoff timing requirement of 8.6 milliseconds. The tail-off impulse estimate of 1.07 metres per second and its ratio of 1.8 to the budget. The vernier acceleration, trim time, and authority ratio of 43.4. The grazing circular speed, the ten percent orbital margin, and the escape comparison. The mass ratio of 1.2645, the 4,266 kilogramme allowance, and the 20.9 percent trade. The comparison with the SCORE mass at 7.2 percent. The SCORE orbital elements, period, perigee and apogee speeds, and specific energies. The apogee sensitivity of 4.24 kilometres per metre per second. The ballistic semi-major axis, eccentricity, flight time of 34.3 minutes, and apogee altitude. The Earth rotation speed and the azimuth bound. The lift-off thrust-to-weight ratio, mass flows, mass at booster cutoff, the acceleration discontinuity of 4.37, the two-phase ideal velocity of 8,590 metres per second, and the sustainer burn time. The separation clearance comparison. The propellant residual sensitivity. The accelerometer bias budget of 220 micro-g. The interferometer fringe table and the Doppler resolution. The Allen and Eggers peak deceleration, altitude, and speed, the ballistic coefficient, and the stagnation heating. The unit conversions on the full-range flight and their consistency with the sensitivity relation. The SCORE revolution counts, duty cycle, Nyquist sample count, link budget, area-to-mass ratio, and energy loss per revolution. The binomial standard errors and the pooled z statistic of 0.42. The inverse-square dependence of the angle-to-speed forgiveness ratio and its table, showing 191 at a twentieth of a degree and 1.9 at half a degree. The variance-share relation, the improvement relation, and its ceiling of 14.0 percent at infinite cost. The first-order azimuth relation for the Earth rotation credit, giving 2,466 kilometres due east against an exact 3,195, a shortfall of 23 percent that measures where the linear sensitivity stops being valid. The oblateness perturbation of 1.62 parts in a thousand and the resulting impact displacement of order 34 kilometres, or nine times the miss budget. The identity that the factor by which the vehicle becomes harder to stop is exactly its sustainer mass ratio of 4.38. The static tilt allowance of 46 arcseconds, the gyroscope drift allowance of 0.329 degrees per hour, and the factor of about three separating it from period instruments. The inversion of the plasma frequency relation and the square-law ratio of 77.4. The quadrature relation setting the range instrument at 3.1 times better than the article it certifies, or 0.196 metres per second. The linear scaling of the speed budget with the assumed circular error probable across one, two, and five nautical miles. The boil-off holding time of five days.

**Inference, argued but not established.** That the verniers exist primarily for velocity trim rather than for roll control, which the arithmetic supports strongly but which no document found here states. That radio guidance was the correct architecture for the accuracy requirement rather than merely the available one, which rests on the accelerometer bias and gyroscope drift comparisons. **The strength of that inference was reduced by the equation pass rather than increased**, since deriving the drift requirement put period instruments within a factor of about three of it, so the honest reading is that all-inertial guidance was close in 1958 rather than out of reach, and the ground link bought margin rather than capability. That the reported weakness of the SCORE broadcast refers to public reception rather than to the tracking link. That the Atlas B established the staging event and full range but not accuracy. That the designation question has at least two mechanisms and that this vehicle confirms the limit of the first without resolving anything.

**Reported from the geodetic literature rather than derived here.** That the classical pre-satellite method determined the geoid from surface gravity and connected astronomical to geodetic position through the deflection of the vertical, leaving continental datums internally consistent and mutually offset. That satellite orbit perturbations determine the zonal harmonics of the potential directly, that Doppler tracking was required for the non-zonal terms, and that a world geodetic datum tying the continents together was published in the mid 1970s. **The claim that the target coordinates were, for much of the Atlas force's operational life, less well known than the guidance system's own contribution to the error budget is an inference from that chronology and is not established by any document found here.** It is stated as an argument and the sixteen-year interval it rests on is a matter of publication dates rather than of when the underlying knowledge became available to a targeting organisation, which may well have been earlier and classified.

**A caution about the specific impulse.** The 309 second sustainer figure carries most of this article's orbital arithmetic, including the 20.9 percent mass trade and the comparison with the SCORE mass. As the sustainer discussion notes, a specific impulse quoted to three figures for a period engine is a trajectory reconstruction rather than a direct measurement, so the precision of the downstream results is lower than their presentation suggests.

**Written from current knowledge.** This article is dated 2025-10-18 and draws on literature published after that date where the modern discussion is the natural continuation of the period problem, in line with the series convention.

## Out of Scope

The Atlas C, D, E, and F in any detail. The warhead and its physics package. Silo and coffin basing, alert posture, and reaction time, which decided the Atlas force's fate and which this article touches only to say so. The Mercury programme and man-rating. Centaur, which inherited the balloon tank and the propellant utilisation architecture and deserves separate treatment. The Agena upper stage. The Burroughs ground guidance computer as a computing machine rather than as a guidance element. The full history of Project SCORE as a political act. The Soviet R-7, which reached orbit fourteen months before SCORE with a different configuration and remains the comparison this series has not made. Ballistic missile defence, which is the mirror image of everything computed here. Manufacturing and the factory. The economics of the Atlas force against Titan and Minuteman.

## Conclusion

The [X-11][related_post_a308_convair_x11] answered whether a structure that light could exist. **The X-12 answered whether the thing built out of it could be stopped at the right moment**, which is a different question and the one that decides whether a ballistic missile is a weapon or an expensive firework.

The answer came out of a single sensitivity. Range responds to burnout speed with a gain of 4.34, so a two nautical mile miss allows two thirds of a metre per second out of seven thousand two hundred, while the flight path angle enters only at second order and a tenth of a degree costs seventy-seven metres. **The vehicle is therefore a speed-measuring instrument that happens to have a warhead on it**, and every distinctive feature of the Atlas B follows. The verniers exist because the sustainer's tail-off is twice the entire error budget. The guidance sits on the ground because measuring speed directly avoids an integration that 1958 accelerometers could not survive. The propellant utilisation system exists because fifty kilogrammes of stranded propellant is worth forty-five error budgets.

And then the same machinery did something else. Ten percent more speed than the weapon needed, bought by giving up twenty-one percent of the burnout mass, turns the trajectory into an orbit. **The Atlas B demonstrated a full-range delivery on 28 November 1958 and put a stage in orbit twenty days later, and it did not need a modification to do it.** The first communications satellite is a ballistic missile that was told to stop a little later than usual, and the calculation that predicts its mass to within seven percent uses nothing but the range law and a specific impulse.

That is the whole content of the phrase space launch vehicle, and the X-12 is where it stops being a metaphor.

## References

### Books

[book_jenkins_landis_miller_2003]: https://openlibrary.org/search?q=Jenkins+Landis+Miller+American+X+Vehicles
[book_miller_2001]: https://openlibrary.org/search?q=Miller+The+X+Planes+X-1+to+X-45
[book_neufeld_1990]: https://openlibrary.org/search?q=Neufeld+Development+of+Ballistic+Missiles+United+States+Air+Force
[book_walker_powell_2005]: https://openlibrary.org/search?q=Walker+Bernstein+Lang+Seize+the+High+Ground

### Reference

[ref_x12]: https://en.wikipedia.org/wiki/SM-65B_Atlas

### Research

[research_adkins_1970]: https://doi.org/10.2514/3.30032
[research_aein_1964]: https://doi.org/10.1109/tset.1964.4337583
[research_albertson_2012]: https://ntrs.nasa.gov/citations/20120014503
[research_aldrich_krabill_1972]: https://doi.org/10.2514/6.1972-838
[research_amacker_graff_1965]: https://doi.org/10.2514/6.1965-1247
[research_ammons_1973]: https://doi.org/10.2514/6.1973-296
[research_anderle_1966]: https://doi.org/10.21236/ad0631212
[research_arthur_kemp_2025]: https://doi.org/10.1080/08929882.2025.2557088
[research_aslanov_sizov_2020]: https://doi.org/10.1016/j.actaastro.2019.11.027
[research_bahm_hoffman_1971]: https://ntrs.nasa.gov/citations/19720030101
[research_batrakov_1963]: https://doi.org/10.1007/978-3-642-48130-7_8
[research_beardslee_1964]: https://doi.org/10.21236/ad0616993
[research_becker_1973]: https://doi.org/10.2514/6.1973-835
[research_belsterling_1965]: https://doi.org/10.2514/3.28248
[research_berns_1968]: https://ntrs.nasa.gov/citations/19680027035
[research_bhattacharji_1970]: https://doi.org/10.1007/bf02585745
[research_bidwell_1967]: https://doi.org/10.2514/3.29071
[research_binion_1962]: https://doi.org/10.21236/ad0290303
[research_binion_w_1964]: https://doi.org/10.21236/ad0439948
[research_blaszak_fahrenholz_1960]: https://doi.org/10.21236/ad0321352
[research_blitzer_1959]: https://doi.org/10.1126/science.129.3345.329
[research_blum_1966]: https://doi.org/10.2514/6.1966-300
[research_bohne_1964]: https://doi.org/10.2514/6.1964-1029
[research_bonney_1960]: https://doi.org/10.1109/iret-mil.1960.5008294
[research_boynton_1967]: https://ntrs.nasa.gov/citations/19670008816
[research_britting_1971]: https://doi.org/10.2514/6.1971-901
[research_brouwer_hori_1961]: https://doi.org/10.1086/108399
[research_broxmeyer_1962]: https://doi.org/10.1016/b978-0-12-395586-9.50018-0
[research_brusch_1977]: https://ntrs.nasa.gov/citations/19770062120
[research_buell_1964_2]: https://doi.org/10.2514/6.1964-1017
[research_burghes_1974]: https://doi.org/10.1080/0020739740050101
[research_byerly_1957]: https://doi.org/10.1017/s0373463300016945
[research_callaway_1963]: https://doi.org/10.21236/ad0405121
[research_cavacece_2024]: https://doi.org/10.1515/jmdai-2023-0005
[research_cho_2021_2]: https://doi.org/10.1007/s42405-020-00348-6
[research_clement_1965]: https://ntrs.nasa.gov/citations/19650022844
[research_coates_horton_1970]: https://doi.org/10.21236/ad0871583
[research_comfort_1973]: https://doi.org/10.1029/jb078i029p06845
[research_cook_1965]: https://doi.org/10.1111/j.1365-246x.1965.tb03061.x
[research_cooper_1961]: https://doi.org/10.2514/8.5546
[research_coxe_tatom_1962]: https://doi.org/10.1007/978-1-4757-0531-7_29
[research_crawley_maunder_1966]: https://doi.org/10.1007/978-3-662-29364-5_60
[research_dafler_1962]: https://doi.org/10.1119/1.1941784
[research_dai_2019]: https://doi.org/10.1088/1757-899x/677/4/042084
[research_daly_1967]: https://doi.org/10.21236/ad0731418
[research_denham_1965]: https://doi.org/10.21236/ad0468532
[research_diegoca_1961]: https://doi.org/10.21236/ad0843112
[research_div_1966]: https://doi.org/10.21236/ada028048
[research_div_1966_2]: https://doi.org/10.21236/ada028047
[research_div_1966_3]: https://doi.org/10.21236/ada028046
[research_div_1966_4]: https://doi.org/10.21236/ada027762
[research_div_1966_5]: https://doi.org/10.21236/ada027766
[research_dolton_reed_1966]: https://doi.org/10.2514/6.1966-424
[research_dudush_snovydovych_2026]: https://doi.org/10.62524/msj.2025.3.4.20
[research_duke_1960]: https://doi.org/10.5594/j00037
[research_edelbaum_pines_1969]: https://doi.org/10.2514/6.1969-904
[research_ehrsam_1978]: https://ntrs.nasa.gov/citations/19790016565
[research_eitschberger_grafarend_1974]: https://doi.org/10.1007/bf02522149
[research_ermakov_2025]: https://doi.org/10.1007/s42401-025-00348-y
[research_feldman_1953]: https://doi.org/10.2514/8.4622
[research_felsentreger_victor_1966]: https://ntrs.nasa.gov/citations/19670009425
[research_fischer_1961]: https://doi.org/10.1007/bf02854151
[research_flack_1969]: https://doi.org/10.1016/b978-0-08-013402-4.50050-1
[research_foster_1960]: https://doi.org/10.21236/ad0261738
[research_foster_1961]: https://doi.org/10.21236/ad0272377
[research_frankenthal_1964]: https://doi.org/10.21236/ad0610257
[research_frazier_1967]: https://ntrs.nasa.gov/citations/19670050873
[research_fried_richardson_1956]: https://doi.org/10.1063/1.1722521
[research_fubara_mourad_1974]: https://doi.org/10.1139/tcs-1974-0097
[research_fuhs_1966]: https://doi.org/10.2514/6.1966-1633
[research_fye_1966]: https://doi.org/10.21236/ada522410
[research_geckler_1960]: https://doi.org/10.2514/8.5145
[research_george_1974]: https://doi.org/10.4271/740873
[research_gerald_runyan_1962]: https://doi.org/10.4271/620491
[research_gerharz_1963]: https://doi.org/10.1080/00207216308937523
[research_gerlach_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50009-9
[research_geyling_1964]: https://doi.org/10.2514/3.2518
[research_golden_1969]: https://doi.org/10.21236/ad0858522
[research_gonzalez_denny_1970]: https://doi.org/10.21236/ad0878792
[research_gray_alexander_1965]: https://doi.org/10.2514/3.28125
[research_greenfield_1960]: https://doi.org/10.1007/978-1-4684-3105-6_15
[research_gretz_1962]: https://doi.org/10.2514/8.6408
[research_griffith_byrd_1963]: https://doi.org/10.2514/6.1963-330
[research_griner_1967]: https://doi.org/10.2514/6.1967-1322
[research_gruenberg_johnson_1964]: https://doi.org/10.1007/978-3-7091-4687-3_22
[research_gryglaszewski_1963]: https://doi.org/10.1109/tim.1963.4313348
[research_guier_1963]: https://doi.org/10.1038/200124a0
[research_guier_1965]: https://doi.org/10.21236/ad0464349
[research_hagan_1960]: https://doi.org/10.1109/tcom.1960.1097633
[research_hallett_1960]: https://doi.org/10.1007/978-1-4684-3099-8_3
[research_handelsman_1959]: https://doi.org/10.1109/tcom.1959.1097536
[research_harding_lawson_1968]: https://doi.org/10.2514/3.4494
[research_hauser_1972]: https://ntrs.nasa.gov/citations/19730010894
[research_haviland_1963]: https://doi.org/10.1016/b978-1-4831-9963-4.50008-7
[research_heath_1965]: https://ntrs.nasa.gov/citations/19650017798
[research_heath_1967]: https://ntrs.nasa.gov/citations/19670020099
[research_heitz_1971]: https://doi.org/10.1007/bf02522008
[research_hirvonen_1954]: https://doi.org/10.1111/j.2153-3490.1954.tb01095.x
[research_hix_1968]: https://doi.org/10.21236/ad0393899
[research_hoff_1967]: https://doi.org/10.2172/4228957
[research_horvath_blum_1966]: https://doi.org/10.1016/b978-1-4832-2716-0.50026-8
[research_hudson_1971]: https://doi.org/10.2514/6.1971-845
[research_humphrey_1961]: https://doi.org/10.1007/978-1-4757-0534-8_29
[research_hwang_2019]: https://doi.org/10.21914/anziamj.v60i0.14067
[research_ingber_1965]: https://ntrs.nasa.gov/citations/19660010157
[research_ingram_2026]: https://doi.org/10.59332/jbis-079-07-0262
[research_izotov_1959]: https://doi.org/10.1007/bf02526703
[research_jacobs_1964]: https://doi.org/10.1063/1.1746806
[research_jakes_1961]: https://doi.org/10.1038/190709a0
[research_jaroudi_mcdonald_1964]: https://doi.org/10.2514/3.2730
[research_jastrow_pearse_1957]: https://doi.org/10.1029/jz062i003p00413
[research_jo_2021]: https://doi.org/10.5139/jksas.2021.49.2.155
[research_jo_ahn_2021]: https://doi.org/10.1016/j.ast.2020.106431
[research_jo_ahn_2022]: https://doi.org/10.1016/j.ast.2022.107703
[research_johannessen_1964]: https://doi.org/10.21236/ad0353247
[research_johnson_mosely_1964]: https://doi.org/10.21236/ad0350496
[research_johnston_1966]: https://doi.org/10.2514/6.1966-63
[research_jordan_1972_2]: https://doi.org/10.1029/jb077i020p03660
[research_juarez_1961]: https://doi.org/10.21236/ad0607874
[research_kaplan_1961]: https://doi.org/10.2514/8.5635
[research_karrenberg_lueders_1963]: https://doi.org/10.2514/6.1963-397
[research_kelly_1959]: https://doi.org/10.2514/8.4794
[research_king_hele_1958]: https://doi.org/10.1098/rspa.1958.0169
[research_king_hele_1962]: https://doi.org/10.1007/978-3-7091-5470-0_5
[research_king_hele_1963]: https://doi.org/10.1038/197785a0
[research_king_hele_1964]: https://doi.org/10.1038/202996a0
[research_king_hele_1965]: https://doi.org/10.1038/207575a0
[research_king_hele_1965_2]: https://doi.org/10.1016/0032-0633(65)90056-5
[research_king_hele_1966]: https://doi.org/10.1038/212271b0
[research_king_hele_1966_2]: https://doi.org/10.1016/0032-0633(66)90058-4
[research_king_hele_cook_1965]: https://doi.org/10.1111/j.1365-246x.1965.tb03047.x
[research_kingsley_1967]: https://doi.org/10.1016/b978-1-4831-9967-2.50010-3
[research_kouba_mason_1962]: https://doi.org/10.2514/8.6197
[research_kozai_1964]: https://ntrs.nasa.gov/citations/19650010255
[research_kozai_1964_2]: https://doi.org/10.1093/pasj/16.4.263
[research_kravitsky_2007]: https://doi.org/10.21236/ada471939
[research_kumar_2023]: https://doi.org/10.61653/joast.v74i4.2022.45
[research_lall_1965]: https://ntrs.nasa.gov/citations/19660001031
[research_lange_parkinson_1965]: https://doi.org/10.2514/6.1965-691
[research_larson_1965]: https://doi.org/10.2514/6.1965-306
[research_liu_1974]: https://doi.org/10.2514/6.1974-166
[research_lortie_1966]: https://doi.org/10.21236/ad0630781
[research_lowrey_1962]: https://doi.org/10.4271/620368
[research_lubowe_1965]: https://doi.org/10.2514/3.28135
[research_lubowe_1969]: https://doi.org/10.2514/3.5313
[research_maas_1962]: https://doi.org/10.21236/ad0408258
[research_macpherson_1963]: https://doi.org/10.21236/ad0403872
[research_magrini_1967]: https://ntrs.nasa.gov/citations/19670027973
[research_maresca_1960]: https://doi.org/10.21236/ad0341205
[research_martin_1973]: https://doi.org/10.2514/3.50460
[research_mather_1971]: https://doi.org/10.1111/j.1365-246x.1971.tb03583.x
[research_mather_fryer_1970]: https://doi.org/10.1080/00050326.1970.10440195
[research_matson_1963]: https://doi.org/10.21236/ad0438031
[research_mattson_1965]: https://ntrs.nasa.gov/citations/19660010223
[research_maxwell_dorfman_1963]: https://doi.org/10.2514/6.1963-155
[research_mermagen_1964]: https://doi.org/10.21236/ad0444246
[research_message_1960]: https://doi.org/10.1111/j.1365-246x.1960.tb01722.x
[research_message_1960_2]: https://doi.org/10.1093/mnras/121.1.1
[research_miao_2022]: https://doi.org/10.1109/taes.2021.3133310
[research_miller_1967]: https://doi.org/10.2514/6.1967-44
[research_morey_koshar_1961]: https://doi.org/10.1016/b978-0-12-395682-8.50010-8
[research_moriarty_1966]: https://doi.org/10.21236/ad0633034
[research_moritz_1966]: https://doi.org/10.21236/ad0653193
[research_mottley_1960]: https://doi.org/10.1109/iret-mil.1960.5008220
[research_murphy_1961]: https://doi.org/10.1016/0032-0633(61)90141-6
[research_naca_1960]: https://ntrs.nasa.gov/citations/19690071283
[research_naca_1966]: https://ntrs.nasa.gov/citations/19660022936
[research_naca_1967]: https://ntrs.nasa.gov/citations/19670031002
[research_naca_1968]: https://ntrs.nasa.gov/citations/19680014866
[research_naca_1968_2]: https://ntrs.nasa.gov/citations/19690000964
[research_naca_1969_2]: https://ntrs.nasa.gov/citations/19690028458
[research_nash_1972]: https://doi.org/10.2514/6.1972-848
[research_nein_head_1962]: https://doi.org/10.1007/978-1-4757-0531-7_30
[research_nichols_1974]: https://doi.org/10.21236/ada002625
[research_o_rourke_2010]: https://doi.org/10.21236/ada536934
[research_ostner_1962]: https://doi.org/10.21236/ad0414825
[research_pamadi_2016]: https://ntrs.nasa.gov/citations/20160010566
[research_parkyn_1958]: https://doi.org/10.1038/182787b0
[research_parkyn_1958_2]: https://doi.org/10.2307/3610466
[research_peters_hall_1963]: https://doi.org/10.21236/ad0403115
[research_pijoan_1970]: https://doi.org/10.2514/6.1970-1011
[research_platt_hanner_1965]: https://doi.org/10.2172/1068247
[research_platus_1967]: https://doi.org/10.21236/ad0810587
[research_poehler_1961]: https://doi.org/10.1109/iret-set.1961.5008780
[research_polk_1962]: https://doi.org/10.21236/ad0296952
[research_powers_1960]: https://doi.org/10.1016/b978-0-12-395519-7.50008-2
[research_punga_campbell_1962]: https://doi.org/10.2514/8.9711
[research_rainey_1964]: https://doi.org/10.2514/6.1964-1016
[research_randall_1970]: https://doi.org/10.2514/3.29945
[research_rapp_1967]: https://doi.org/10.1029/jz072i002p00589
[research_rapp_1973]: https://doi.org/10.1029/jb078i032p07589
[research_rapp_1974]: https://ntrs.nasa.gov/citations/19760013482
[research_remmer_1974]: https://doi.org/10.1007/bf02521923
[research_richards_1960]: https://doi.org/10.21236/ad0419890
[research_richards_1961]: https://doi.org/10.2514/8.5903
[research_ringland_stubblefield_1965]: https://ntrs.nasa.gov/citations/19660013606
[research_roberts_1960]: https://ntrs.nasa.gov/citations/19980232223
[research_rockefeller_alfred_1960]: https://doi.org/10.21236/ada637368
[research_rodean_1959]: https://doi.org/10.2514/8.4786
[research_rowson_1962]: https://doi.org/10.1093/mnras/125.2.177
[research_russell_1964]: https://doi.org/10.2514/6.1964-242
[research_ryle_1952]: https://doi.org/10.1007/978-94-009-7752-5_12
[research_rynaski_1967]: https://doi.org/10.2514/6.1967-592
[research_sabaghzadeh_khansari_2022]: https://doi.org/10.5267/j.esm.2022.3.003
[research_sarychev_1962]: https://doi.org/10.2514/8.6110
[research_satterfield_akens_1958]: https://doi.org/10.21236/ada434326
[research_saunders_1965]: https://doi.org/10.21236/ad0620194
[research_scherberg_rubin_1953]: https://doi.org/10.21236/ad0012619
[research_schlegel_1966]: https://doi.org/10.2514/3.3857
[research_schurmann_1957]: https://doi.org/10.2514/8.12965
[research_schweppe_1964]: https://doi.org/10.21236/ad0609524
[research_scott_1963]: https://doi.org/10.21236/ad0410255
[research_sharenson_1966]: https://doi.org/10.21236/ad0634390
[research_shelton_1966]: https://ntrs.nasa.gov/citations/19660007993
[research_siry_1960]: https://doi.org/10.1016/b978-1-4832-2736-8.50006-8
[research_slifka_1960]: https://doi.org/10.1109/jrproc.1960.287405
[research_smalley_1961]: https://doi.org/10.21236/ad0264245
[research_stancil_1963]: https://doi.org/10.2514/6.1963-223
[research_stephens_1965]: https://doi.org/10.2514/6.1965-1114
[research_stetson_1964]: https://doi.org/10.2514/6.1964-433
[research_strauss_1964]: https://doi.org/10.21236/ad0609492
[research_su_2026]: https://doi.org/10.1080/23307706.2025.2556335
[research_sundstrom_brown_1969]: https://www.osti.gov/biblio/4721501
[research_taylor_price_1974]: https://doi.org/10.21236/ad0783098
[research_thomas_perlbachs_1967]: https://doi.org/10.21236/ad0655383
[research_townsend_1966]: https://doi.org/10.21236/ad0633628
[research_trushlyakov_2024]: https://doi.org/10.1016/j.cja.2023.09.018
[research_tsuboi_hayatu_1954]: https://doi.org/10.4294/jpe1952.2.45
[research_veis_1968]: https://doi.org/10.1007/bf02525700
[research_vickers_dyer_1971]: https://doi.org/10.1029/rs006i012p01021
[research_wareham_1972]: https://doi.org/10.21236/ad0754070
[research_westerman_1963]: https://doi.org/10.1086/108986
[research_whelan_1968]: https://doi.org/10.2514/6.1968-417
[research_whitcombe_1961]: https://doi.org/10.21236/ad0259865
[research_whitcombe_1961_2]: https://doi.org/10.21236/ad0266445
[research_widnall_1974]: https://doi.org/10.2514/6.1974-867
[research_wildhack_1958]: https://doi.org/10.1126/science.128.3319.309
[research_wilkinson_1971]: https://doi.org/10.2514/3.30286
[research_wilner_1960]: https://doi.org/10.1109/jrproc.1960.287484
[research_wolf_1954]: https://doi.org/10.1007/bf02526780
[research_wolfe_1966]: https://doi.org/10.21236/ad0486484
[research_wood_1961]: https://doi.org/10.21236/ad0421632
[research_wright_ruscus_1959]: https://doi.org/10.1109/iret-set.1959.5008660
[research_xu_2020]: https://doi.org/10.5755/j01.mech.26.5.27874
[research_yan_2025]: https://doi.org/10.1088/1742-6596/3004/1/012078
[research_zhang_2022]: https://doi.org/10.3390/act11120366

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
