---
layout: post
mathjax: true
comments: true
title: "X-Planes: Rockwell X-30 and the National Aero-Space Plane"
date: 2025-11-05 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 31
---
<!-- A327 -->
<script>console.log("A327");</script>

The [X-30][ref_x30] was to take off from a runway, accelerate to orbital velocity on air-breathing engines,
and land on a runway.
**It was never built, and this article is about why that sentence is harder than it sounds for a reason that has nothing to do with ambition.**
The article before this one treated the [X-29][related_post_a326_grumman_x29], which was built, flew for
seven years and left a flight record. **The X-30 left a technology record and no aeroplane**, and the two
together make a useful pair, because the X-29 could measure the thing it existed to measure and the X-30's
central quantity could not be measured by anything on the ground at all. This is the thirty-first article in
the [X-Planes series][related_post_a297_xplanes_framing], following the [X-1][related_post_a298_bell_x1],
the [X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], the
[X-4][related_post_a301_northrop_x4], the [X-5][related_post_a302_bell_x5], the
[X-6][related_post_a303_convair_x6], the [X-7][related_post_a304_lockheed_x7], the
[X-8][related_post_a305_aerojet_x8], the [X-9][related_post_a306_bell_x9], the
[X-10][related_post_a307_north_american_x10], the [X-11][related_post_a308_convair_x11], the
[X-12][related_post_a309_convair_x12], the [X-13][related_post_a310_ryan_x13], the
[X-14][related_post_a311_bell_x14], the [X-15][related_post_a312_north_american_x15], the
[X-16][related_post_a313_bell_x16], the [X-17][related_post_a314_lockheed_x17], the
[X-18][related_post_a315_hiller_x18], the [X-19][related_post_a316_curtiss_wright_x19], the
[X-20][related_post_a317_boeing_x20], the [X-21][related_post_a318_northrop_x21], the
[X-22][related_post_a319_bell_x22], the [X-23][related_post_a320_martin_marietta_x23], the
[X-24][related_post_a321_martin_marietta_x24], the [X-25][related_post_a322_bensen_x25], the
[X-26][related_post_a323_schweizer_x26], the [X-27][related_post_a324_lockheed_x27], the
[X-28][related_post_a325_osprey_x28], and the [X-29][related_post_a326_grumman_x29].

**The easy misreading is that the X-30 failed because supersonic combustion is hard.** It is hard, and that
is not the reason. Burning fuel in a supersonic stream was demonstrated in ground tests in the 1950s and
1960s and has been demonstrated repeatedly since \[[Scramjet][ref_scramjet]\]. The programme did not
founder on whether a [scramjet][ref_scramjet] would light.

**It foundered on a subtraction.** What accelerates an air-breathing vehicle is not the thrust its engine
makes but what is left after the drag of swallowing the air is taken away, and at orbital speeds those two
quantities are nearly equal. The useful output is a small difference between two large numbers, and
**no facility on Earth could measure either of them at the conditions that mattered.**

* Contents
{:toc}

## The Research Question

**The keystone has two halves, and the way they meet is unusual.**

**The first half is the thrust margin.** An air-breathing engine takes in air moving at flight speed and
expels it faster. The momentum it gains is the gross thrust. The momentum the incoming air already carried
is the [ram drag][ref_ram_drag]. The difference is what pushes. As flight speed rises, the incoming momentum
rises with it, while the fuel can only add so much.
**The margin shrinks toward zero not because the engine gets worse but because the arithmetic it is embedded in gets worse.**

**The second half is that it could not be measured.** A true Mach 25 condition carries a stagnation enthalpy
that no continuous facility could produce at useful scale, and the facilities that reach the enthalpy hold
it for a few milliseconds, the same order as the time the flow needs merely to establish itself
inside the engine duct.

**Put together, those two halves are the purest statement of the research-aircraft rationale in the series.**
The programme's contractors concluded that only a near full-scale vehicle flying above Mach 20 could take the
measurement with confidence \[[Peebles 2007][research_peeblescurtis_2007_b]\].
**The same argument killed it**, because a programme whose central number cannot be known
until the vehicle flies is a programme asking for several billion dollars against an unquantified risk.

### Why This Is the Right Keystone

The obvious alternative is to make the keystone the materials, since a 1985 review by the Defense Advanced
Research Projects Agency concluded that the vehicle's key materials exceeded the state of the art. That
difficulty is treated at length below. It is genuine, but it is a difficulty of degree. Hot structures
existed, were improving, and could be tested on the ground one panel at a time, as the programme's large
titanium aluminide panels and its leading edges were
\[[Schweikart and Hallion 1998][research_schwelkart_hallion_1997]\].

**The thrust margin is different in kind, because no component has one.** It emerges only when
forebody, inlet, combustor, nozzle and aftbody are assembled and flown together, and
**it is defined as a subtraction between two quantities that are each larger than it is.** Measuring it
required an aeroplane.

## Programme Origin

**The programme began in secret and was announced in a speech.**

### Copper Canyon

The [Defense Advanced Research Projects Agency][ref_darpa] ran a classified study called **Copper Canyon**
from the early 1980s to 1985, a feasibility study for a single-stage vehicle that would take off and land
horizontally. [Jenkins, Landis and Miller][ref_xvehicles] date its start to 1982 and the programme history by
[Schweikart][research_schwelkart_hallion_1997] to 1983. Its reviewers concluded that hypersonic flight was
feasible and that a spaceplane was worth pursuing, and many of its supporters held that computational fluid
dynamics was the most promising of the technologies the vehicle would need
\[[Schweikart and Hallion 1998][research_schwelkart_hallion_1997]\].

**That conclusion rested heavily on computation**, for the reason named above. Many doubted that
data from small engine modules run for a few seconds in wind tunnels could be scaled to a full-size engine,
so the case for the vehicle was made in software \[[Peebles 2007][research_peeblescurtis_2007_b]\].

### The Announcement

President Reagan described the vehicle in the **1986 State of the Union address** as a new Orient Express
that could take off from Dulles and reach Tokyo within two hours \[[Jenkins, Landis and Miller][ref_xvehicles]\].
**The hypersonic transport was never the programme's real objective**, which was military and orbital
access, but the phrase attached itself to the X-30 permanently and shaped how it was reported
\[[Schweikart and Hallion 1998][research_schwelkart_hallion_1997]\].

### The Industrial Arrangement

After the 1987 downselection the airframe contracts were held by [Rockwell International][ref_rockwell],
[McDonnell Douglas][ref_mcdonnell] and [General Dynamics][ref_gd], and the propulsion work was divided
between [Pratt and Whitney][ref_pw] and [Rocketdyne][ref_rocketdyne]. In 1990 the five companies formed a
single National Contractor Team, reporting to the government's Joint Program Office, rather than a prime
contractor with subcontractors, and its leader came from Rockwell's Rocketdyne division
\[[Schweikart and Hallion 1998][research_schwelkart_hallion_1997]\].

**The programme ended without a vehicle.**
With defence funding declining after the Cold War, Congress directed that the effort be closed out by the end
of fiscal year 1994, and NASA's history of the X-43A records that it was cancelled in October 1994, after
some 2.4 billion dollars had been spent and eight years of work had produced no workable
design\[[Peebles 2007][research_peeblescurtis_2007_b]\].
The same history dates the end of the programme to June 1995 in another passage, so the record places the
close-out somewhere between late 1994 and mid 1995 and fixes no single day.

## The Vehicle

**This section is short because there is very little to put in it, and that scarcity is the finding. It does not reflect a gap in the research.**

**No X-30 configuration was ever frozen.** The design evolved continuously for the whole life of the
programme, and estimates of gross weight differed between years and between contractors, from 50,000 pounds
for the original government baseline to nearly 200,000 for Rockwell's 1988 design, nearly 350,000 for
Lockheed's and about 500,000 for the team's design in 1992. The programme was still planning to freeze the
design as soon as possible in the early 1990s \[[Schweikart and Hallion 1998][research_schwelkart_hallion_1997]\],
and the vehicle that appears in illustrations is a design study rather than a specification.
**An article that presented a table of X-30 dimensions would be presenting one snapshot of a moving target as though it were the aeroplane.**

What can be stated is the intent, which was stable.

| Quantity | Intent |
|---|---|
| Take-off and landing | Horizontal, from a conventional runway |
| Propulsion | Air-breathing to high Mach, rocket for final insertion |
| Fuel | Hydrogen, with [slush hydrogen][ref_slush] to raise density |
| Staging | Single stage to orbit |
| Target speed | Orbital velocity, usually quoted as Mach 25 |
| Structure | Actively cooled, with titanium aluminide and carbon-carbon |
| Crew | Two, in most configurations |

**Even the target speed is a loose statement**, and the looseness is instructive. Mach number is a ratio to
the local speed of sound, which varies with altitude, so **Mach 25 is not a fixed velocity at all.** At
forty-eight kilometres it corresponds to about 8,245 metres per second, above orbital velocity. The
physically meaningful target is the orbital velocity itself.

$$ V_{\mathrm{orbit}} = \sqrt{\frac{\mu}{R_\oplus + h}} = \sqrt{\frac{3.986 \times 10^{14}}{6.371 \times 10^6 + 2 \times 10^5}} = 7{,}789\ \mathrm{m/s} $$

Mach number is the ratio of flight speed to the local speed of sound, and the speed of sound depends only on
temperature.

$$ a = \sqrt{\gamma R T}, \qquad M = \frac{V}{a} $$

At forty-eight kilometres the atmosphere is warm enough that

$$ a = \sqrt{1.4 \times 287.05 \times 270.65} = 329.8\ \mathrm{m/s} $$

so orbital velocity there corresponds to

$$ M_{\mathrm{orbit}} = \frac{7{,}789}{329.8} = 23.62 $$

**Mach 25 at that altitude is 8,245 metres per second, which overshoots orbital velocity by six percent.**
The programme's headline number was never a velocity target at all.

**Every result in this article is computed against that number rather than against a Mach number**, because a
Mach number at these speeds is a statement about the atmosphere and not about the vehicle.

## Sizing From First Principles

The inventory of record for the series, and the source for this vehicle's place in it, is
[Jenkins, Landis and Miller][ref_xvehicles].

The relations used throughout follow [Anderson][book_anderson_hyp] on hypersonic and high-temperature gas
dynamics, [Heiser and Pratt][book_heiser_pratt] on hypersonic air-breathing propulsion,
[Curran and Murthy][book_curran] on scramjet propulsion, and [Bertin][book_bertin] on hypersonic
aerothermodynamics, with the compressible-flow relations in [Shapiro][book_shapiro] and the vehicle sizing
in [Hill and Peterson][book_hill_peterson].

### The Subtraction That Decides Everything

Consider a stream tube of air entering the engine at flight speed $V_0$ and leaving at $V_e$, with a
fuel-air ratio $f$ by mass. Momentum conservation gives the gross thrust and the ram drag directly.

$$ F_{\mathrm{gross}} = \dot{m}_0\left(1 + f\right)V_e, \qquad D_{\mathrm{ram}} = \dot{m}_0 V_0 $$

$$ F_{\mathrm{net}} = \dot{m}_0\left[\left(1 + f\right)V_e - V_0\right] $$

The exit velocity follows from an energy balance across the engine. The stream arrives carrying kinetic
energy $V_0^2/2$ per unit mass of air, combustion adds $f\,\eta_c\,h_{\mathrm{fuel}}$ per unit mass of air,
and the nozzle expands the combined flow.

$$ \left(1 + f\right)\frac{V_e^2}{2} = \eta_n\left[\frac{V_0^2}{2} + f\,\eta_c\,h_{\mathrm{fuel}}\right] $$

$$ V_e = \sqrt{\frac{2\eta_n\left(\tfrac{1}{2}V_0^2 + f\,\eta_c\,h_{\mathrm{fuel}}\right)}{1 + f}} $$

**That pair of relations carries the argument.** The fuel's contribution is a fixed quantity. The stream's
kinetic energy grows as the square of flight speed.
**So the fuel becomes a smaller and smaller perturbation on a larger and larger number**, and the difference
that pushes the vehicle is squeezed between them.

### Why the Air-Breather's Specific Impulse Looks So Large

Specific impulse is thrust divided by the weight flow of propellant, and
**the propellant an air-breather is charged for is the fuel alone**, because it does not carry its oxidiser.

$$ I_{sp} = \frac{F_{\mathrm{net}}}{\dot{m}_{\mathrm{fuel}}\,g_0} = \frac{F_{\mathrm{net}}/\dot{m}_0}{f\,g_0} $$

**That single difference in convention is why figures above a thousand seconds appear below**, against about
450 for a hydrogen rocket \[[RS-25][ref_rs25]\]. It is not that the engine is four times better. It is
that three quarters of what a rocket carries is free.

### What That Looks Like in Numbers

Taking hydrogen at a lower heating value of 119.96 megajoules per kilogram
\[[Heat of combustion][ref_heat_combustion]\], a stoichiometric fuel-air ratio of 0.0291, and **assumed**
efficiencies of 0.90 for combustion and 0.95 for the nozzle, the subtraction runs as follows. All thrusts are specific, meaning per unit mass flow of captured air, so they carry units of
metres per second.

| $V_0$, m/s | Gross | Ram drag | Net | Net/gross | Amplification | $I_{sp}$, s | Fuel energy over stream energy |
|---|---|---|---|---|---|---|---|
| 1,000 | 2,668.5 | 1,000.0 | 1,668.5 | 0.6253 | 1.60 | 5,846.6 | 6.2835 |
| 2,000 | 3,170.7 | 2,000.0 | 1,170.7 | 0.3692 | 2.71 | 4,102.5 | 1.5709 |
| 3,000 | 3,865.5 | 3,000.0 | 865.5 | 0.2239 | 4.47 | 3,032.8 | 0.6982 |
| 4,000 | 4,667.5 | 4,000.0 | 667.5 | 0.1430 | 6.99 | 2,339.0 | 0.3927 |
| 5,000 | 5,530.3 | 5,000.0 | 530.3 | 0.0959 | 10.43 | 1,858.2 | 0.2513 |
| 6,000 | 6,429.5 | 6,000.0 | 429.5 | 0.0668 | 14.97 | 1,505.0 | 0.1745 |
| 7,000 | 7,351.7 | 7,000.0 | 351.7 | 0.0478 | 20.90 | 1,232.5 | 0.1282 |
| 7,500 | 7,818.9 | 7,500.0 | 318.9 | 0.0408 | 24.52 | 1,117.6 | 0.1117 |

Taking the row at seven thousand metres per second and substituting,

$$ V_e = \sqrt{\frac{2 \times 0.95\left(\tfrac{1}{2}\left(7000\right)^2 + 0.0291 \times 0.90 \times 119.96 \times 10^6\right)}{1.0291}} = 7{,}143.8\ \mathrm{m/s} $$

$$ \frac{F_{\mathrm{gross}}}{\dot{m}_0} = 1.0291 \times 7143.8 = 7{,}351.7\ \mathrm{m/s} $$

$$ \frac{F_{\mathrm{net}}}{\dot{m}_0} = 7351.7 - 7000 = 351.7\ \mathrm{m/s} $$

$$ I_{sp} = \frac{351.7}{0.0291 \times 9.80665} = 1{,}232.5\ \mathrm{s} $$

$$ \frac{f\,\eta_c\,h_{\mathrm{fuel}}}{\tfrac{1}{2}V_0^2} = \frac{3.142 \times 10^6}{2.45 \times 10^7} = 0.1282 $$

**The exhaust leaves 143.8 metres per second faster than the air arrived**, on a flight speed of seven
thousand. That increment is all the engine contributes, and the rest of the table follows from it.

**Read the last column first.** At a thousand metres per second the fuel supplies more than six times the
kinetic energy the stream already has, and the engine is doing something close to what a jet engine does.
**At seven thousand it supplies about an eighth of it.** The engine has become a device that adds a modest
amount of energy to an enormous flow, and takes its living from the difference.

### From Specific Thrust to a Vehicle

The figures above are per unit mass flow of captured air. Converting them into forces requires the capture
area, and the conversion deserves its own line because the result is startling.

$$ \dot{m}_0 = \rho\,V_0\,A_{\mathrm{capture}} $$

At Mach 20 and forty-two kilometres, where the density is 2.878 × 10⁻³ kilograms per cubic metre and the
flight speed 6,423 metres per second, a ten square metre capture area gives

$$ \dot{m}_0 = 2.878 \times 10^{-3} \times 6423 \times 10 = 184.9\ \mathrm{kg/s} $$

$$ F_{\mathrm{gross}} = 184.9 \times 6{,}816 = 1{,}260\ \mathrm{kN}, \qquad F_{\mathrm{net}} = 184.9 \times 394 = 72.9\ \mathrm{kN} $$

**An engine developing 1,260 kilonewtons of gross thrust pushes the vehicle with 73.** The other 1,187
kilonewtons are spent getting the air up to the speed it was already travelling at.

### Amplification of Error

The column headed amplification is the ratio of gross thrust to net thrust. It is also the factor by which a
relative error in the gross figure appears in the net one.

$$ \frac{\delta F_{\mathrm{net}}}{F_{\mathrm{net}}} = \frac{F_{\mathrm{gross}}}{F_{\mathrm{net}}} \cdot \frac{\delta F_{\mathrm{gross}}}{F_{\mathrm{gross}}} $$

**At seven thousand metres per second a one percent error in gross thrust is a twenty-one percent error in net thrust.**
At seven and a half thousand it is nearly twenty-five percent.

**This is why the programme needed a flight vehicle and why it could not justify one.** To predict the
acceleration to within ten percent at that speed, the gross thrust must be known to within half of one
percent, and the ram drag to a similar precision, and there was no way to establish either.

### The Loss Budget

The same ratio read the other way is more useful still, because net thrust is what remains after everything
else has taken its share.

$$ \frac{F_{\mathrm{net}}}{F_{\mathrm{gross}}} = \text{the fraction of gross thrust that everything else may consume} $$

Inlet spillage, total-pressure loss through the shock system, incomplete combustion, nozzle underexpansion,
the drag of the cooling system and the external drag of the vehicle must together fit inside that fraction,
or the vehicle stops accelerating.

| $V_0$, m/s | Loss budget |
|---|---|
| 3,000 | 22.39 percent |
| 5,000 | 9.59 percent |
| 6,000 | 6.68 percent |
| 7,000 | 4.78 percent |
| 7,500 | 4.08 percent |

**Four and three quarter percent, for everything, at seven kilometres per second.** That is the engineering
problem stated as a single number. No component test can confirm it, because it exists only for the
assembled vehicle in flight.

### The Speed at Which Net Thrust Vanishes

A natural question is the flight speed at which net thrust falls to zero. With the assumed efficiencies the
crossing falls at 16,577 metres per second, a figure easily mistaken for a ceiling set by chemistry.

**It is nothing of the kind.** In an ideal engine net thrust never reaches zero at all. For small fuel
fractions the specific net thrust tends to

$$ F_{\mathrm{net}}/\dot{m}_0 \;\approx\; \frac{f\,\eta_c\,h_{\mathrm{fuel}}}{V_0} $$

which shrinks without ever changing sign. The crossing was produced entirely by the assumed nozzle
efficiency, and it moves as follows.

| Assumed nozzle efficiency | Speed at which net thrust vanishes |
|---|---|
| 1.00 | No crossing at any speed |
| 0.98 | No crossing at any speed |
| 0.95 | 16,577 m/s |
| 0.92 | 10,572 m/s |
| 0.90 | 8,880 m/s |

### Buying Thrust by Running Rich

The fuel-air ratio is not fixed at stoichiometric, and running rich is the obvious lever. The equivalence
ratio scales it.

$$ \phi = \frac{f}{f_{\mathrm{stoich}}} $$

At six and a half thousand metres per second,

| $\phi$ | Net specific thrust | $I_{sp}$ | Amplification |
|---|---|---|---|
| 0.6 | 169.5 m/s | 990.0 s | 39.34 |
| 1.0 | 388.3 m/s | 1,360.6 s | 17.74 |
| 2.0 | 923.4 m/s | 1,617.9 s | 8.04 |
| 3.0 | 1,444.4 m/s | 1,687.1 s | 5.50 |

**Running at three times stoichiometric nearly quadruples the net thrust and cuts the amplification from eighteen to five and a half**,
which makes the vehicle both more capable and far easier to predict.
**It also burns three times the fuel for a twenty-four percent gain in specific impulse**, and the extra
hydrogen is the same hydrogen the cooling system needs. That trade, between thrust, fuel and coolant, ran
through the design, since the path the hydrogen took as coolant also set how well it burned
\[[Schweikart and Hallion 1998][research_schwelkart_hallion_1997]\].

**A number that moves by a factor of two when one assumed efficiency moves by five percent is not a finding about propulsion.**
It is a finding about the assumption. The loss budget above says the same thing honestly, because it makes
no efficiency assumption at all.

Equivalence ratio and the behaviour of a hydrogen flame run rich are covered by two clusters under The Contemporary Literature, on ignition, kinetics and hydrogen-air chemistry and on dual-mode combustion and thermal choking.

## Dependent Systems

### The Ground Test Gap

**This is the other half of the keystone, and it decided the programme.**

A facility that simulates flight must reproduce the total enthalpy of the free stream, because the total enthalpy
sets the temperature the engine sees and therefore the chemistry inside it.

$$ h_0 = c_p T + \frac{V^2}{2} $$

At hypersonic speed the second term swamps the first entirely, so facility capability is quoted as
an enthalpy rather than as a Mach number.

| Flight condition | Free-stream speed | Stagnation enthalpy | Ideal stagnation temperature |
|---|---|---|---|
| Mach 8 at 27 km | 2,398 m/s | 3.10 MJ/kg | 3,086 K |
| Mach 12 at 33 km | 3,660 m/s | 6.93 MJ/kg | 6,897 K |
| Mach 16 at 38 km | 5,025 m/s | 12.87 MJ/kg | 12,812 K |
| Mach 20 at 42 km | 6,423 m/s | 20.89 MJ/kg | 20,789 K |
| Mach 25 at 48 km | 8,245 m/s | 34.26 MJ/kg | 34,102 K |

**The last column is deliberately wrong and the size of the error is the point.** Air does not reach
thirty-four thousand kelvin. It dissociates and then ionises, and both processes absorb energy, so the true
stagnation temperature is far lower.
**A model that returns a number that absurd is announcing that the model has failed**, and the
ideal-gas assumption on which most engineering compressible-flow relations rest fails somewhere around the
third row of that table.

**The difficulty is not only that the facilities were inadequate. The equations were inadequate too**,
and the computational methods that were meant to substitute for the facilities had to model chemistry that
the facilities could not produce cleanly enough to validate against.

### The Other Quantity That Explodes

Temperature is the difficulty a facility is usually judged on. **Pressure grows faster.**

$$ \frac{p_0}{p} = \left(1 + \frac{\gamma - 1}{2}M^2\right)^{\frac{\gamma}{\gamma - 1}} $$

| Flight Mach | Total to static pressure ratio |
|---|---|
| 4 | 1.518 × 10² |
| 8 | 9.763 × 10³ |
| 12 | 1.445 × 10⁵ |
| 20 | 4.783 × 10⁶ |
| 25 | 2.245 × 10⁷ |

**Twenty-two million at Mach 25.** A facility must contain that, an engine must be built to hold it, and the
ideal-gas relation that produced the number has already failed for the same reason the temperature relation
did. **The structural problem grows faster than the thermal one and is discussed far less.**

The facilities built to contain these pressures are surveyed in the cluster on impulse and high-enthalpy ground test facilities under The Contemporary Literature.

### Why Milliseconds Are Not Enough

Facilities capable of the required enthalpy store energy and release it quickly, and their run
times are short compared with the time the flow needs to establish itself in an engine duct.

$$ t_{\mathrm{flow}} = \frac{L}{V_{\mathrm{duct}}} = \frac{5\ \mathrm{m}}{2{,}500\ \mathrm{m/s}} = 2.0\ \mathrm{ms} $$

The count of flow-through times a run provides is the ratio.

$$ N = \frac{t_{\mathrm{run}}}{t_{\mathrm{flow}}} = \frac{5 \times 10^{-3}}{2.0 \times 10^{-3}} = 2.50 \quad \text{for a reflected shock tunnel} $$

$$ N = \frac{2 \times 10^{-4}}{2.0 \times 10^{-3}} = 0.10 \quad \text{for an expansion tube} $$

Steady flow is not established until several of these have passed, because the starting shock system must
sweep out of the duct and the boundary layers must grow to their equilibrium thickness. Taking eight
flow-through times as the requirement gives the following comparison.

| Facility type | Run time | Flow-through times available | Verdict |
|---|---|---|---|
| Blowdown, combustion heated | 30 s | 15,000 | Ample, at low enthalpy |
| Arc heated | 1 s | 500 | Ample, at small scale |
| Reflected shock tunnel | 5 ms | 2.5 | Short by a factor of 3.2 |
| Expansion tube | 0.2 ms | 0.1 | Short by a factor of 80 |

**The facilities that reach the enthalpy cannot hold it long enough to establish the flow, and the facilities that can hold it cannot reach the enthalpy.**
That is the gap, stated as a table, and no amount of money would have closed it, because the two
requirements pull in opposite directions.

**The combustion-heated facilities carry a further problem the table does not show.** They reach their
enthalpy by burning fuel in the test gas, which leaves the flow contaminated with water vapour, and with
carbon dioxide when the fuel is a hydrocarbon \[[Arad and Michaels 2021][research_arad_michaels_2021]\].
A scramjet burning hydrogen in that gas is not burning in air, and the difference matters precisely where
the margins are thinnest.

Short-duration facilities, their test times and the contamination of their test gas are taken up again in the clusters on impulse and high-enthalpy ground test facilities and on vitiation and test gas contamination.

### Why the Flow Is Kept Supersonic Through the Burner

**The reason for a scramjet is a temperature argument, not a choking argument, and getting that backwards is easy.**

A ramjet slows the incoming flow to subsonic speed before burning. That conversion is governed by total
enthalpy being conserved through the inlet, so whatever kinetic energy is removed reappears as static
temperature.

$$ T_{\mathrm{entry}} = \frac{T_0}{1 + \frac{\gamma - 1}{2}M_c^2} $$

For subsonic combustion at $M_c \approx 0.3$ the denominator is barely above one, so the burner inherits
almost the whole stagnation temperature. Keeping the flow at $M_c \approx 2.5$ divides it by 2.25.

| Flight Mach | $T_0$ | Burner entry, subsonic | Burner entry, supersonic | Normal shock total pressure recovery |
|---|---|---|---|---|
| 4 | 910 K | 894 K | 404 K | 13.9 percent |
| 6 | 1,809 K | 1,777 K | 804 K | 2.97 percent |
| 8 | 3,086 K | 3,032 K | 1,372 K | 0.849 percent |
| 12 | 6,897 K | 6,775 K | 3,065 K | 0.129 percent |
| 16 | 12,812 K | 12,586 K | 5,694 K | 0.0321 percent |
| 20 | 20,789 K | 20,421 K | 9,239 K | 0.0108 percent |

The total pressure recovery in the last column is the normal shock relation.

$$ \frac{p_{0,2}}{p_{0,1}} = \left[\frac{\left(\gamma + 1\right)M^2}{2 + \left(\gamma - 1\right)M^2}\right]^{\frac{\gamma}{\gamma - 1}}\left[\frac{\gamma + 1}{2\gamma M^2 - \left(\gamma - 1\right)}\right]^{\frac{1}{\gamma - 1}} $$

Substituting the Mach 8 condition,

$$ T_0 = 223.7\left(1 + 0.2 \times 64\right) = 3{,}086\ \mathrm{K} $$

$$ T_{\mathrm{entry}}\big|_{M_c = 2.5} = \frac{3086}{1 + 0.2 \times 6.25} = 1{,}372\ \mathrm{K}, \qquad T_{\mathrm{entry}}\big|_{M_c = 0.3} = \frac{3086}{1.018} = 3{,}032\ \mathrm{K} $$

**Combustion products begin to dissociate around three thousand kelvin**, and above it the energy released
by burning hydrogen goes into breaking molecules apart rather than into raising pressure. Reading down the
subsonic column, that threshold is crossed **between Mach 6 and Mach 8**, a little above the Mach 5 to 6
at which scramjets are usually said to overtake ramjets \[[Scramjet][ref_scramjet]\].
**The model was not fitted to that transition and lands near it anyway**, which supports the argument without
proving it.

**The total pressure column says the same thing by a second route.** A normal shock at Mach 20 returns about
one part in ten thousand of the incoming total pressure, so a ramjet at that speed would have nothing left
to expand through its nozzle.

**Thermal choking is the third constraint and the least binding of the three.** At Mach 8 flight with
a Mach 2.5 burner entry the duct can accept about forty percent of the heat the fuel supplies before
choking. That limit is real and forces the burner to be lean or long, but it is not the reason the flow
is kept supersonic.

The [Rayleigh relation][ref_rayleigh] that sets it is displayed here because its behaviour is easy to
misremember, and it follows [Shapiro][book_shapiro] and [Zucrow and Hoffman][book_zucrow].

$$ \frac{T_{0}^{*}}{T_0} = \frac{\left(1 + \gamma M^2\right)^2}{\left(\gamma + 1\right)M^2\left(2 + \left(\gamma - 1\right)M^2\right)} $$

**It equals exactly one at Mach one and grows as the flow moves away from sonic in either direction**,
because a duct further from choking has more room to accept heat. That identity is also a useful check,
since a slip in the denominator shows at once as a value other than one at Mach one.

### Time to Burn

Residence time in the burner is short but not the binding constraint.

$$ t_{\mathrm{res}} = \frac{L}{M_c\sqrt{\gamma R T}} = \frac{5\ \mathrm{m}}{2.5\sqrt{1.4 \times 287 \times 1500}} = 2.58\ \mathrm{ms} $$

$$ N_{\mathrm{ignition}} = \frac{t_{\mathrm{res}}}{t_{\mathrm{ignition}}} $$

| Assumed ignition delay | Delays available within the residence time |
|---|---|
| 10 μs | 258 |
| 50 μs | 52 |
| 100 μs | 26 |

**If hydrogen ignition delay at these pressures and temperatures is of order tens of microseconds**, as the
table assumes, there is ample time to ignite. **What there is not time for is mixing.** Fuel injected into a
stream moving at two and a half kilometres per second must penetrate, mix and burn within a couple of
milliseconds \[[Scramjet][ref_scramjet]\], and mixing is the slow step, which is why so much of the
scramjet literature concerns injector geometry rather than chemistry.

The ignition and mixing work this estimate draws on is reviewed below in the clusters on ignition, kinetics and hydrogen-air chemistry, on fuel injection, mixing and flameholding and on turbulent combustion modelling and simulation.

### The Airframe as the Engine

**On an airframe-integrated vehicle the forebody is the first compression surface and the aftbody is the last expansion surface**,
so the engine is not a component bolted beneath the aircraft. It is the underside of the aircraft.

**This integration makes the thrust margin unmeasurable by parts.** A component test of the combustor requires
the inlet's exit conditions, which depend on the forebody boundary layer, which depends on transition, which
depends on the flight environment. A test of the nozzle requires the combustor exit conditions.
**Each piece can be tested only against an assumption about the piece before it**, and the assumptions are
what the flight vehicle was meant to check.

### Why Unstart Cannot Be Undone at Speed

**Unstart is catastrophic because it is irreversible, and its irreversibility comes from a pair of area ratios that do not overlap.**

A fixed-geometry inlet must swallow its starting shock. The largest internal contraction at which it can
do so is the Kantrowitz limit, being the contraction at which the flow behind a normal shock at the entry
reaches sonic conditions at the throat.

$$ \left(\frac{A_{\mathrm{entry}}}{A_{\mathrm{throat}}}\right)_{\mathrm{start}} = \frac{1}{M_2}\left[\frac{2}{\gamma + 1}\left(1 + \frac{\gamma - 1}{2}M_2^2\right)\right]^{\frac{\gamma + 1}{2\left(\gamma - 1\right)}} $$

where $M_2$ is the Mach number behind that shock. Once started, the same duct can hold far more, because the
flow through it is supersonic and the limit becomes the isentropic area ratio.

$$ \left(\frac{A}{A^{*}}\right)_{\mathrm{run}} = \frac{1}{M}\left[\frac{2}{\gamma + 1}\left(1 + \frac{\gamma - 1}{2}M^2\right)\right]^{\frac{\gamma + 1}{2\left(\gamma - 1\right)}} $$

| Flight Mach | Mach behind the shock | Contraction that will start | Contraction that will run | Ratio |
|---|---|---|---|---|
| 3 | 0.4752 | 1.390 | 4.235 | 3.05 |
| 5 | 0.4152 | 1.543 | 25.00 | 16.2 |
| 8 | 0.3929 | 1.614 | 190.1 | 117.8 |
| 12 | 0.3847 | 1.642 | 1,276 | 777 |
| 20 | 0.3804 | 1.657 | 15,377 | 9,279 |

**At Mach 20 an inlet can run at a contraction nine thousand times what it could start at.** The starting
limit barely moves with Mach number, sitting between 1.4 and 1.7 across the whole range, while the running
limit grows without bound.

**So a hypersonic inlet is started at low speed and must never let go.** If it unstarts at Mach 20 it cannot
restart there, and the vehicle must decelerate a long way before it can try again.
**Unstart is therefore a loss-of-vehicle event rather than a transient**, and the clearest single
reason the flowpath cannot be treated as a component.

For inlets, their starting limits and the isolators behind them, see the clusters on inlets, forebody compression and mass capture, on inlet starting and unstart and on isolators and shock trains.

**Inlet unstart is the failure mode this arrangement creates.** If the shock system in the isolator is
driven forward by too much heat release, it disgorges from the inlet, mass capture collapses, thrust
disappears and the vehicle pitches. The isolator exists to absorb that pressure rise, and sizing it is a
trade between length, weight and cooling area.

### Whether Hydrogen Can Carry the Heat Away

Stagnation-point heat flux on a blunt leading edge follows the Sutton and Graves correlation.

$$ \dot{q}_s = 1.7415 \times 10^{-4}\sqrt{\frac{\rho}{R_n}}\,V^3 $$

The cube on velocity is what makes this brutal. Taking an **assumed** leading-edge radius of five
centimetres,

| Condition | Stagnation heat flux | Radiation equilibrium temperature |
|---|---|---|
| Mach 10 at 30 km | 287 W/cm² | 2,779 K |
| Mach 15 at 36 km | 660 W/cm² | 3,420 K |
| Mach 20 at 42 km | 1,107 W/cm² | 3,893 K |
| Mach 25 at 48 km | 1,548 W/cm² | 4,234 K |

Substituting the Mach 20 condition at forty-two kilometres,

$$ \dot{q}_s = 1.7415 \times 10^{-4}\sqrt{\frac{2.878 \times 10^{-3}}{0.05}}\left(6{,}423\right)^3 = 1.107 \times 10^{7}\ \mathrm{W/m^2} = 1{,}107\ \mathrm{W/cm^2} $$

$$ T_w = \left(\frac{1.107 \times 10^{7}}{0.85 \times 5.670 \times 10^{-8}}\right)^{1/4} = 3{,}893\ \mathrm{K} $$

where the radiation equilibrium temperature is the wall temperature at which re-radiation alone balances the
incoming flux, with an **assumed** emissivity of 0.85. The aerothermodynamic relations here follow
[Bertin][book_bertin] and [Hirschel][book_hirschel].

$$ \dot{q} = \varepsilon\sigma T_w^4 \quad \Longrightarrow \quad T_w = \left(\frac{\dot{q}}{\varepsilon\sigma}\right)^{1/4} $$

**Nothing structural survives four thousand kelvin.** Carbon-carbon retains its properties to about two
thousand degrees Celsius, and beyond that only when coated against oxidation
\[[Reinforced carbon-carbon][ref_rcc]\], and the best titanium aluminides keep their strength only to about a
thousand \[[Titanium aluminide][ref_tial]\]. **So the leading edges must be actively cooled**, and the only
coolant aboard is the fuel, which the design pumped through the airframe for that purpose
\[[Schweikart and Hallion 1998][research_schwelkart_hallion_1997]\].

Each kilogram of hydrogen can absorb a computable amount of heat before it is too hot to burn well.

$$ Q_{\mathrm{sink}} = c_{p,H_2}\,\Delta T = 14{,}300 \times 800 = 11.44\ \mathrm{MJ/kg} $$

The balance is between the heat arriving on the wetted area and the heat the fuel flow can take up.

$$ \frac{\dot{Q}_{\mathrm{capacity}}}{\dot{Q}_{\mathrm{load}}} = \frac{f\,\dot{m}_0\,c_{p,H_2}\,\Delta T}{\kappa\,\dot{q}_s\,A_{\mathrm{wetted}}} $$

where $\kappa$ is the ratio of average surface flux to the stagnation-point value.

Whether that is enough depends on $\kappa$, which is **assumed** for want of a measurement, so it is swept
rather than asserted. Taking Mach 20 at forty-two
kilometres, eight hundred square metres of wetted area and four hundred kilograms per second of captured
air,

| Assumed average flux as a fraction of stagnation | Heat load | Fuel cooling capacity | Margin |
|---|---|---|---|
| 0.01 | 88.6 MW | 133.2 MW | 1.50 |
| 0.02 | 177.1 MW | 133.2 MW | 0.75 |
| 0.05 | 442.9 MW | 133.2 MW | 0.30 |
| 0.10 | 885.7 MW | 133.2 MW | 0.15 |

**The answer turns entirely on a ratio nobody could measure**, the same difficulty in a different
currency. If the average flux is one percent of the stagnation value the fuel carries the load with fifty
percent to spare. If it is two percent the fuel cannot carry it, and the vehicle needs either more fuel flow
than combustion wants or a heavier structure than the mass budget allows.

**Running the engine rich to buy cooling capacity is the trade this arithmetic forces**,
because extra fuel is extra coolant, and it also costs specific impulse.

Heating and cooling each have a cluster under The Contemporary Literature, stagnation-point, leading-edge and aerodynamic heating for the first and active, regenerative and transpiration cooling for the second.

### Materials That Were Necessary but Not Sufficient

**The materials programme is the part of the X-30 most often counted a success**, and its history records
that it cut the development time of new materials from about fifteen years to about five, although not every
material proved worthy \[[Schweikart and Hallion 1998][research_schwelkart_hallion_1997]\].

Titanium aluminide intermetallics, metal matrix composites and coated carbon-carbon all advanced
substantially, and many of the programme's materials passed to the private sector
\[[Schweikart and Hallion 1998][research_schwelkart_hallion_1997]\].
**None of that addressed the keystone**, because a panel that survives an arc-jet test tells you nothing
about the thrust margin of an assembled vehicle.

**A programme can succeed at every subsystem and fail**, and the X-30 is the clearest case of it in this
series.

Three clusters below hold the materials literature, those on titanium aluminides, intermetallics and titanium matrix composites, on carbon-carbon, ceramic matrix composites and oxidation protection and on thermal protection, hot structures and aerothermoelasticity.

### Fuel and Tankage

Hydrogen was not a choice so much as a consequence. Its heating value per unit mass is about 2.8 times that
of kerosene \[[Heat of combustion][ref_heat_combustion]\], and at these speeds specific impulse dominates the design.
**What it costs is volume**, because liquid hydrogen has a density of about seventy-one kilograms per cubic
metre \[[Liquid hydrogen][ref_lh2]\], roughly an eleventh that of kerosene \[[Kerosene][ref_kerosene]\].

**Slush hydrogen was the programme's answer**, being a mixture of solid and liquid at the triple point
\[[Slush hydrogen][ref_slush]\].

$$ \frac{\rho_{\mathrm{slush}}}{\rho_{\mathrm{liquid}}} - 1 = \frac{81.5}{70.8} - 1 = 15.1\ \mathrm{percent} $$

$$ \frac{\mathcal{V}_{\mathrm{slush}}}{\mathcal{V}_{\mathrm{liquid}}} = \frac{70.8}{81.5} = 0.869 $$

**A thirteen percent reduction in tank volume is worth a great deal on a vehicle whose tanks dominate its size**,
and slush carries additional heat capacity through the latent heat of fusion. It also requires production,
storage and pumping of a two-phase cryogen at the triple point, a substantial industrial
undertaking for a fuel, and the programme counted its demonstration a major accomplishment
\[[Schweikart and Hallion 1998][research_schwelkart_hallion_1997]\].

The cluster on hydrogen fuel, slush hydrogen and tankage, under The Contemporary Literature, collects the work on slush and on cryogenic tanks.

### Getting to Orbit Is Not the Problem

**The result here is the article's least expected, and it reframes the programme.**

The usual objection to single stage to orbit is the mass fraction, and the rocket relations follow
[Sutton][book_sutton]. Taking an all-rocket single stage with a specific impulse of 450 seconds and a
velocity budget of about 9,300 metres per second including losses,

$$ \frac{m_0}{m_f} = \exp\left(\frac{\Delta V}{g_0 I_{sp}}\right), \qquad \text{propellant fraction} = 1 - \frac{m_f}{m_0} $$

$$ \text{propellant fraction} = 87.81\ \mathrm{percent}, \qquad \text{dry fraction} = 12.19\ \mathrm{percent} $$

**Twelve percent for structure, engines, tanks, thermal protection, systems and payload together** is why
rocket-powered single stage to orbit is so unforgiving.

The air-breather's case must be made with the specific impulse allowed to decay, because that decay is this
article's central finding and assuming it away would beg the question. Integrating instead,

$$ \ln\frac{m_0}{m_f} = \int_{V_1}^{V_2}\frac{dV}{g_0\,I_{sp}(V)} + \frac{V_{\mathrm{orbit}} - V_2}{g_0\,I_{sp,\mathrm{rocket}}} $$

with $I_{sp}(V)$ taken from the same energy balance as the thrust model, air-breathing from 900 metres per
second to a transition speed and then rocketing to orbital velocity.

| Transition speed | Propellant fraction | Dry fraction | Structure permitted at 2 percent payload |
|---|---|---|---|
| 3,000 m/s | 67.92 percent | 32.08 percent | 30.08 percent |
| 4,000 m/s | 61.28 percent | 38.72 percent | 36.72 percent |
| 5,000 m/s | 53.76 percent | 46.24 percent | 44.24 percent |
| 6,000 m/s | 45.44 percent | 54.56 percent | 52.56 percent |
| 7,000 m/s | 36.52 percent | 63.48 percent | 61.48 percent |

Taking the six thousand metre per second row and showing the integration,

$$ \ln\frac{m_0}{m_f} = 0.60594 \quad \Longrightarrow \quad \frac{m_0}{m_f} = 1.8330 $$

$$ \text{propellant fraction} = 1 - \frac{1}{1.8330} = 45.44\ \mathrm{percent} $$

### A Bound That Owes Nothing to Any Engine

**The integrated result deserves a check that does not depend on the thrust model, and thermodynamics supplies one.**

Reaching orbit requires a definite energy per unit mass of vehicle, being the kinetic energy of orbital
velocity plus the potential energy of the altitude.

$$ e_{\mathrm{orbit}} = \frac{V_{\mathrm{orbit}}^2}{2} + \mu\left(\frac{1}{R_\oplus} - \frac{1}{R_\oplus + h}\right) = 30.33 + 1.90 = 32.24\ \mathrm{MJ/kg} $$

Hydrogen carries 119.96 megajoules per kilogram \[[Heat of combustion][ref_heat_combustion]\].
**If every joule went into the vehicle and none into the exhaust, the atmosphere or the structure**, the
fuel fraction could not fall below

$$ \left(\frac{m_{\mathrm{fuel}}}{m_0}\right)_{\min} = \frac{32.24}{119.96} = 26.9\ \mathrm{percent} $$

**The integrated ascent gives 45.44 percent, which is 1.69 times the bound.** A perfect engine could do no
better than a factor of 1.69 improvement on the answer above, and
**the bound is the strongest evidence available here that the integration is not producing a fantasy**, because a
result below the bound would have been proof of an error.

**Air-breathing to six kilometres per second moves the permitted structural fraction from twelve percent to fifty-two.**
The improvement is not marginal. It separates a vehicle that cannot be built from one with
room to spare.

The result survives a heavy drag penalty.

| Drag as a share of thrust | Propellant fraction | Structure permitted | Closes |
|---|---|---|---|
| 0.0 | 45.44 percent | 52.56 percent | Yes |
| 0.2 | 48.11 percent | 49.89 percent | Yes |
| 0.4 | 52.28 percent | 45.72 percent | Yes |
| 0.6 | 59.62 percent | 38.38 percent | Yes |

**So the rocket equation was never the X-30's problem.** On mass fraction the concept closes comfortably,
and it keeps closing even when drag consumes sixty percent of thrust throughout the air-breathing phase.

**What does not close is the loss budget.** The vehicle needs everything else to consume less than about
five percent of gross thrust at the top of the air-breathing phase, and nothing on the ground could
establish whether it would.

Work on single-stage and staged vehicles to orbit appears in the cluster on single-stage and two-stage to orbit.

### The Corridor

An air-breather must fly where there is enough air to breathe and not so much that it burns. That confines
it to a narrow band of dynamic pressure, and therefore to a specific altitude at each speed.

$$ q = \tfrac{1}{2}\rho V^2 $$

| Flight Mach | Altitude at 47.9 kPa | Altitude at 95.8 kPa |
|---|---|---|
| 6 | 26.82 km | 22.33 km |
| 10 | 33.61 km | 28.98 km |
| 15 | 39.33 km | 34.42 km |
| 20 | 43.63 km | 38.48 km |
| 25 | 47.11 km | 41.76 km |

Working the Mach 25 case,

$$ q = \tfrac{1}{2}\left(1.409 \times 10^{-3}\right)\left(8{,}245\right)^2 = 47{,}880\ \mathrm{Pa} \quad \text{at}\ 47.11\ \mathrm{km} $$

**The corridor is a line, not a region.** The vehicle must climb along it as it accelerates, and the heat
load, the structural load and the engine's operating point are all set by where on that line it sits.

What it does along that line is set by the acceleration equation, in which the net thrust this article has
computed appears once and is then reduced again by the vehicle's own drag.

$$ m\frac{dV}{dt} = F_{\mathrm{net}} - D - m g \sin\gamma, \qquad D = q\,S_{\mathrm{ref}}\,C_D $$

**Every term on the right is smaller than the gross thrust, and the first of them is the smallest.** A
trajectory that strays high loses the air it needs, and one that strays low melts.

Ascent trajectories and the dynamic pressure corridor are the subject of the cluster on trajectory, guidance and control of hypersonic vehicles, and transition along the corridor that of the cluster on boundary-layer transition and instability.

### Computation as a Substitute for the Facility

**The Copper Canyon conclusion rested on computational fluid dynamics being ready**, and the X-30's
feasibility case was made primarily in software \[[Schweikart and Hallion 1998][research_schwelkart_hallion_1997]\].

The Reynolds number that sets where transition occurs is modest, which is part of the difficulty,
since these flows sit in the range where transition is most sensitive rather than safely laminar or safely
turbulent.

$$ \frac{Re}{L} = \frac{\rho V}{\mu}, \qquad \mu = \frac{1.458 \times 10^{-6}\,T^{3/2}}{T + 110.4} $$

| Condition | Unit Reynolds number |
|---|---|
| Mach 8 at 27 km | 4.73 × 10⁶ per metre |
| Mach 20 at 42 km | 1.13 × 10⁶ per metre |

That was a reasonable bet in 1985 and it was only partly vindicated, for the methods advanced faster than
expected \[[Schweikart and Hallion 1998][research_schwelkart_hallion_1997]\]. Hypersonic flows combine turbulence,
finite-rate chemistry, boundary layer transition and shock interactions, and each of those was, and
substantially still is, an open problem.
**The codes could not be validated at the conditions that mattered for the same reason the engine could not be tested there**,
so the computational case and the experimental case failed together rather than backing one another up
\[[Peebles 2007][research_peeblescurtis_2007_b]\].

The computational work is divided among the clusters on computation, validation and uncertainty, on real-gas, nonequilibrium and rarefied hypersonic flow and on turbulent combustion modelling and simulation.

## The Flight Test Record

**There is none, and the shape of the absence can be stated precisely.**

**No X-30 was built.** No airframe was completed, no integrated engine flew, and the vehicle never
progressed beyond design studies, component tests and ground demonstrations. The programme was cancelled in
October 1994 \[[Peebles 2007][research_peeblescurtis_2007_b]\] \[[Schweikart and Hallion 1998][research_schwelkart_hallion_1997]\].

**What did exist was substantial and was not an aeroplane.** Engine modules were run in ground facilities,
small scramjets to Mach 18 and large ones to Mach 16, short of the speeds the vehicle needed. Structural
panels and an integrated fuel tank were tested. Materials were developed and characterised. Computational
methods were written, validated against the test data and used to make predictions
\[[Schweikart and Hallion 1998][research_schwelkart_hallion_1997]\].

**The gap between that inventory and a flight vehicle is the subject of this article.** Every item
on the list is a component tested against an assumed environment, and the environment was the unknown.

## Comparison With Ground Prediction

**Every article in this series has this section. Here it inverts, and the inversion is the most useful thing about it.**

For every other vehicle in this series the section compares what the ground predicted against what the
aircraft measured. **The X-30 flew nothing, so there is no flight column.** What can be compared instead is
the ground prediction against itself, and against what has been learned since.

### The Predictions Disagreed With One Another

**The programme's technical history records that different groups, using different codes and different assumptions, reached materially different conclusions about the same propulsion question.**
One laboratory reported confirming the original design's claim to reach orbit, which none of the other
contractors could reproduce \[[Schweikart and Hallion 1998][research_schwelkart_hallion_1997]\]. Such disagreement
is to be expected when the quantity of interest is a small difference between two large numbers, as the
arithmetic above shows.
**At an amplification of twenty, two teams differing by three percent on gross thrust differ by sixty percent on the thing that decides whether the vehicle reaches orbit.**

### What Flight Data Since Has Shown

**Two later programmes did fly scramjets and both are relevant.** The [X-43A][ref_x43] flew powered at about
Mach 7 and Mach 10 in 2004, and the [X-51A][ref_x51] sustained powered flight for several minutes at about
Mach 5 in 2013. **Both demonstrated positive net thrust in flight**, the X-43A accelerating at Mach 7 and
holding its thrust equal to its drag at Mach 10 \[[Peebles 2007][research_peeblescurtis_2007_b]\], and the X-51A
accelerating to about Mach 5.1 \[[Boeing X-51 Waverider][ref_x51]\]. That is the qualitative result the X-30
needed, and neither approached the speeds at which the loss budget becomes as tight as the table above shows.

**So the concept was vindicated in the regime where it was never really in doubt**, and the regime the X-30
was built to settle remains unvisited.

The flight programmes are surveyed in the cluster on scramjet flight experiments since the X-30 under The Contemporary Literature.

## What the Data Changed

**The X-30 produced no flight data and changed a great deal, an unusual combination in this series.**

- **The materials transferred.** Titanium aluminides, metal matrix composites and coated carbon-carbon
  advanced under the programme, and many of its materials passed to the private sector
  \[[Schweikart and Hallion 1998][research_schwelkart_hallion_1997]\]. It is the most commonly cited
  return on the expenditure, and a real one.
- **The computational methods transferred.** Hypersonic computational fluid dynamics was pushed hard
  by the programme, which trained a new generation of scramjet researchers, and the X-43A project began
  within it \[[Peebles 2007][research_peeblescurtis_2007_b]\].
- **The flight programmes that followed were shaped by it.** The X-43A was scoped as a small, expendable
  vehicle with a limited goal, an approach the programme's managers had long rejected
  \[[Peebles 2007][research_peeblescurtis_2007_b]\], and the X-51A was another
  single-purpose demonstrator \[[Boeing X-51 Waverider][ref_x51]\]. Each answered one question, which is
  the opposite of the X-30's approach.

**What did not change is the answer to the question the programme asked.** Whether an air-breathing vehicle
can accelerate to orbital velocity is still unknown, because the margin is still small, the uncertainty
large, and the ground unable to settle it.

The clusters on the National Aero-Space Plane and its programme record, on titanium aluminides, intermetallics and titanium matrix composites and on carbon-carbon, ceramic matrix composites and oxidation protection, under The Contemporary Literature, collect the programme's record and the materials and methods it passed on.

## The Designation Went to Something That Was Never Built, Again

**The X-27 was a manufacturer's private-venture fighter that was never built. The X-30 was a government programme's flagship that was never built. Those are different failures and the difference matters.**

The X-27 was never built because nobody bought it. The design existed, the manufacturer was ready, and no
customer appeared \[[X-Planes: Lockheed X-27][related_post_a324_lockheed_x27]\].
**Its non-existence is a procurement fact.**

**The X-30 was never built because the thing it was meant to demonstrate could not be shown to be achievable before building it.**
Some 2.4 billion dollars and eight years of work produced materials, methods and modules, and no aeroplane
\[[Peebles 2007][research_peeblescurtis_2007_b]\], because the central quantity stayed out of reach of every
instrument that could be brought to bear on it short of the vehicle itself.

**This is a different category of X-plane and deserves a name**, because the series contains
several vehicles bought off the shelf, several built to answer a question, and several that were never built
at all, among them the [X-6][related_post_a303_convair_x6], the [X-20][related_post_a317_boeing_x20], the X-27
and now the X-30, the last two for opposite reasons. That distinction is part of the evidence the closing
article of this series assembles.

## The Contemporary Literature

| Cluster | Records |
|---|---|
| Fuel injection, mixing and flameholding | 314 |
| Impulse and high-enthalpy ground test facilities | 287 |
| Inlets, forebody compression and mass capture | 236 |
| Hypersonic aerodynamics, boundary layers and configurations | 228 |
| Scramjet flight experiments since the X-30 | 221 |
| Active, regenerative and transpiration cooling | 173 |
| Combined-cycle and precooled engines | 169 |
| Carbon-carbon, ceramic matrix composites and oxidation protection | 147 |
| Stagnation-point, leading-edge and aerodynamic heating | 145 |
| The National Aero-Space Plane and its programme record | 141 |
| Boundary-layer transition and instability | 137 |
| Single-stage and two-stage to orbit | 119 |
| Thermal protection, hot structures and aerothermoelasticity | 120 |
| Titanium aluminides, intermetallics and titanium matrix composites | 110 |
| Scramjet cycle analysis and engine performance | 107 |
| Trajectory, guidance and control of hypersonic vehicles | 105 |
| Detonation engines | 98 |
| Hydrogen fuel, slush hydrogen and tankage | 98 |
| Real-gas, nonequilibrium and rarefied hypersonic flow | 96 |
| Computation, validation and uncertainty | 92 |
| Turbulent combustion modelling and simulation | 88 |
| Nozzles, afterbodies and exhaust flows | 86 |
| Inlet starting and unstart | 84 |
| Ignition, kinetics and hydrogen-air chemistry | 78 |
| Net thrust, thrust and drag accounting, and force measurement | 77 |
| Dual-mode combustion and thermal choking | 76 |
| Reusable launch vehicles and the cost of access | 61 |
| Isolators and shock trains | 57 |
| Vitiation and test gas contamination | 52 |
| Additive manufacture of aerospace structures | 14 |
| **Total** | **3,816** |

The table gathers every research record this article cites into the literatures the argument draws on.
**The subsections that follow review what has happened to those subjects since the programme ended**, and the
cluster subsections after them set out each literature in turn.

**The short version is that the field became modest, and being modest made it succeed.**

### Scramjets flew, in small pieces

**The X-30 tried to answer every question with one vehicle. What followed answered one question per vehicle and the vehicles were cheap by comparison.**
The X-43A was planned at about 200 million dollars over four years
\[[Peebles 2007][research_peeblescurtis_2007_b]\]. The X-43A and X-51A were expendable, air-launched and
single-purpose, and between them they established that an airframe-integrated scramjet produces positive net
thrust in flight.

**That is a smaller claim than the X-30's, and it was settled**, which is the
methodological lesson the programme paid some 2.4 billion dollars to teach.

The flight results are reported in \[[Ferlemann et al 2005][research_ferlemann_mcclinton_2005]\] for the Mach 7 flight and in \[[Marshall et al 2005][research_marshall_bahm_2005]\] for the Mach 10 flight, the X-51A programme is described in \[[Hank et al 2008][research_hank_murphy_2008]\], and the wider literature makes up the cluster on scramjet flight experiments since the X-30 below.

### The isolator became its own subject

**Inlet unstart was a known risk in 1990 and is a quantified one now.** The isolator, the length of duct
whose shock train absorbs the back pressure of combustion, has a modern literature covering its sizing, its
dynamics, its response to throttling and the detection of impending unstart.

Its sizing is optimised in \[[Deng et al 2017][research_deng_jin_2017]\], the shock train's response to unsteady back pressure is studied in \[[Cai et al 2017][research_cai_zhou_2017]\], and metrics for detecting impending unstart are set out in \[[Acharya 2025][research_acharya_2025]\] and \[[Ratchford et al 2025][research_ratchford_redding_2025]\]. Further work on isolators and shock trains appears in that cluster below.

### Ground testing improved and the gap did not close

**The facilities are better and the fundamental tension is unchanged.** Higher-enthalpy shock tunnels and
expansion tubes reach further, run times are still measured in milliseconds, and the trade between enthalpy
and duration is set by how energy is stored, which more engineering effort does not change.

**What has changed is how much is said about it.** Vitiation has been studied since the 1960s, and
34 of the 52 records in the cluster on vitiation and test gas contamination date from 2000 or later,
alongside a facility literature that states what a given facility can and cannot establish.

Vitiation is reviewed in \[[Pellett et al 2002][research_pellett_bruno_2002]\] and its effect on ground tests analysed in \[[Arad and Michaels 2021][research_arad_michaels_2021]\], and the work on extending test time includes \[[Yu 2015][research_yu_2015]\]. Facility work follows in the cluster on impulse and high-enthalpy ground test facilities below, and contamination in the one on vitiation and test gas contamination.

### Computation grew up, and learned to state its uncertainty

**The X-30's computational case was presented as a prediction. The modern equivalent is presented as a prediction with a distribution attached.**
Uncertainty quantification, validation hierarchies and sensitivity analysis are now standard in hypersonic
simulation, and the shift matters for the reason the amplification factor above gives.

**A twenty-fold amplification from input uncertainty to output uncertainty is not a reason to stop computing. It is a reason to compute the amplification.**

An isolator flowfield is computed with its uncertainty quantified in \[[Baurle and Axdahl 2017][research_baurlera_axdahlel_2017]\], and the standards for verification and validation are set out in \[[Freitas 2020][research_freitas_2020]\]. Further work is listed under computation, validation and uncertainty below.

### Transition remains the hardest open problem

**Boundary layer transition sets the heat load, the drag and the inlet's incoming profile**, and first principles
still cannot predict it at these conditions. The contemporary literature is large and honest
about this.

The state of the question is summarised in \[[Chou and Marineau 2023][research_amandachou_ericcmarineau_2024]\], and the cluster on boundary-layer transition and instability below carries the rest.

### Aerothermodynamics is computed, and still not settled

**Heating prediction has moved from correlations to computation and the uncertainty has not closed.**
Real-gas chemistry, surface catalysis and radiative transport are all better represented than they were, and
the spread between codes at the conditions that matter remains substantial.

The capability of the codes for shock and boundary-layer interaction is assessed in \[[Knight 2015][research_knight_2015]\], and the heating work appears below under stagnation-point, leading-edge and aerodynamic heating, with high-temperature gas effects under real-gas, nonequilibrium and rarefied hypersonic flow.

### Trajectory and guidance became a control problem

**The corridor the X-30 had to fly along is now treated as a constrained optimal control problem**, with the
dynamic pressure limit, the heating limit and the engine's operating box entering as path constraints rather
than as lines on a chart.

Ascent with a dynamic pressure limit is solved as an optimal control problem in \[[Chudej 1996][research_chudej_1996]\], and path constraints of a later kind appear in \[[Tian and Shen 2022][research_tian_shen_2022]\]. Both sit in the cluster on trajectory, guidance and control of hypersonic vehicles below.

### Combustion modelling and the fuel-air question

**Ignition delay and equivalence ratio are now computed with detailed kinetics rather than correlated.** The
trade the X-30 faced, between thrust, fuel and coolant, has not changed, but it is now posed with
a chemistry model attached.

Flamelet methods for supersonic combustion are assessed in \[[Baumgart et al 2025][research_baumgart_yao_2025]\], and three clusters below share the subject, those on turbulent combustion modelling and simulation, on ignition, kinetics and hydrogen-air chemistry and on fuel injection, mixing and flameholding.

### Inlet starting is a design variable now

**Variable geometry, bleed and controlled unstart recovery have turned the starting problem from a constraint into a subject.**

Bleed is used to improve self-starting in \[[Fengyuan et al 2016][research_fengyuan_guoping_2016]\], restart by an active jet is assessed in \[[Jin and Yao 2023][research_jin_yao_2023]\], and adaptive geometry is proposed in \[[Zhang 2020][research_zhang_2020_c]\]. The cluster on inlet starting and unstart below covers the rest.

### Materials and structures moved on

**Ceramic matrix composites, ultra-high-temperature ceramics and modern thermal protection have advanced well past what the X-30 had available**,
and additive manufacture has changed what cooled structures can be made.

Ceramic matrix composites for hypersonic systems are reviewed in \[[De Stefano Fumo et al 2025][research_destefanofumo_sciti_2025]\], and the subject continues in the clusters on carbon-carbon, ceramic matrix composites and oxidation protection, on thermal protection, hot structures and aerothermoelasticity and on titanium aluminides, intermetallics and titanium matrix composites below.

### Six Subjects That Were Small or Absent in 1994

**The subsections above track what happened to the subjects the X-30 worked on.** The six that follow
were small or absent when the programme was cancelled, and between them they have changed both the technical and
the economic case.

### Detonation replaced deflagration as the interesting question

**The X-30 assumed its fuel would burn as a deflagration, a flame that moves subsonically through the mixture.** A
detonation burns through the mixture at supersonic speed and approaches constant-volume rather than
constant-pressure heat release, which raises the theoretical cycle efficiency.

**Rotating and pulse detonation engines are now a substantial literature**, and the relevance here is
direct. The X-30's difficulty was that its fuel added a small perturbation to a very large stream.
**A cycle that extracts more work from the same chemical energy attacks that difficulty directly.**

Standing oblique detonation for hypersonic propulsion is reviewed in \[[Jiang 2023][research_jiang_2023]\], and the remaining work forms the cluster on detonation engines below.

### Precooling attacks the problem from the other end

**If the difficulty is that the incoming air is too hot and too fast, one answer is to cool it before the engine sees it.**
A precooled engine passes the intake air through a heat exchanger fed by the cryogenic fuel, which lowers
the compressor inlet temperature enough to let turbomachinery work far beyond its usual limit.

**This is a different bet from the X-30's**, and its central difficulty is the heat exchanger rather than
the combustor.

The thermodynamics of precooled engines is set out in \[[Yu et al 2017][research_yu_pan_2017]\]. Precooled engines share a cluster with combined cycles below.

### Machine learning entered where the codes could not be validated

**The X-30's computational case could not be checked against experiment at flight conditions.**
Contemporary practice inserts learned models at the same points, for turbulence closure, for chemistry
reduction and for surrogate models that make an optimisation affordable.

**The obvious objection comes from the X-30's history.** A model trained on data that does not
reach the flight condition extrapolates there, and extrapolation is what the programme was punished for.

Turbulence models are calibrated against the HIFiRE-1 flight experiment with machine-learned models in \[[Chowdhary et al 2022][research_chowdhary_hoang_2022]\], and that work is counted with computation, validation and uncertainty below.

### Uncertainty is quantified rather than covered

**This bears directly on the arithmetic above.** With gross-thrust error amplified twenty-fold
into net-thrust error,
**the remedy is to compute the amplification and state the distribution**, now standard
practice under the names uncertainty quantification and validation hierarchy.

Uncertainty quantification for an air-breathing launch vehicle is set out in \[[McCormick et al 2010][research_mccormick_wakayama_2010]\], and it too falls within the cluster on computation, validation and uncertainty.

### Manufacture changed what a cooled structure can be

**The X-30's actively cooled panels were made by conventional fabrication, with brazing among the steps of its manufacturing plan**
\[[Schweikart and Hallion 1998][research_schwelkart_hallion_1997]\]. Additive manufacture
allows internal cooling geometries that cannot be fabricated any other way, and design for additive
manufacture has become a literature of its own since 2016.

A printed hypersonic combustor is reported in \[[Orbital ATK tests 3D printed hypersonic engine combustor][research_orbital_atk_2016]\], and the cluster on additive manufacture of aerospace structures below holds the rest.

### Aerothermoelasticity became a coupled subject

**Heating softens structure, softened structure deflects, deflection changes the flow, and the flow changes the heating.**
Coupled analysis began within the programme, in its aeroservothermoelasticity studies \[[Doggett et al 1991][research_doggettrobertvjr_rickettsrodneyh_1991]\] and the aerothermoelastic analysis of a demonstrator model \[[Heeg et al 1993][research_heegjennifer_zeilerthomasa_1993]\], and the modern treatment couples the disciplines as a matter of course.

The cluster on thermal protection, hot structures and aerothermoelasticity below includes this work.

### The economic case was removed by something else entirely

**The development that matters most is not aerodynamic.**

**Reusable rocket first stages have been credited with lowering the cost of access to space, without air-breathing.**
One of the X-30's justifications was that air-breathing was the route to cheap access
\[[Schweikart and Hallion 1998][research_schwelkart_hallion_1997]\]. That argument has been
answered by a different technology, and
**the physics the X-30 could not settle remains unsettled.**

The development of reusable launch vehicles is reviewed in \[[Wu and Zhang 2023][research_wu_zhang_2023]\], and reusable launch vehicles and the cost of access form a cluster below.

### Combined cycles and the reusable launch question

**The question the X-30 asked has not gone away and is now usually posed with staging.** Two-stage concepts
with air-breathing first stages, rocket-based and turbine-based combined cycles, and the practical success
of reusable rocket first stages have all changed what the competition looks like.

**Here again the most important development is economic.** Reusable rockets made access to space dramatically
cheaper without air-breathing, which removes much of the economic argument the X-30 was built on while
leaving the physics where it was \[[Wu and Zhang 2023][research_wu_zhang_2023]\].

The history of rocket-based combined cycles is set out in \[[Escher 1999][research_escher_1999]\], and the clusters on combined-cycle and precooled engines and on single-stage and two-stage to orbit carry the subject from there.

### Fuel injection, mixing and flameholding

**How fuel is put into a supersonic stream and kept burning.** Injectors, struts, ramps and cavities, flameholding, combustion efficiency and the combustor experiments and computations that measure them.

**314 records.** \[[95/01686 Cavity-actuated supersonic mixing and combustion...][research_95_01686_cavity_actuated_1995]\] \[[98/01484 Effects of mixing schemes on kerosene combustion in...][research_98_01484_effects_1998]\] \[[Fuhs 1966][research_fuhs_1966]\] \[[Rogers 1979][research_rogersrc_1979]\] \[[Qin et al 2019][research_qin_agarwal_2019]\] \[[Krishamurthy 1993][research_krishamurthyramesh_1993]\] \[[Weidner 1996][research_weidnerjohnp_1996]\] \[[Trudgian et al 2025][research_trudgian_vanyai_2025]\] \[[Ghenai et al 2005][research_ghenai_philippidis_2005]\] \[[Swartzbaugh 1997][research_swartzbaugh_1997]\] \[[Tedder 2010][research_teddersarahaugustaumberger_2010]\] \[[Walton 1992][research_waltonjamest_1992]\] \[[Agnone 1972][research_agnone_1972]\] \[[Ali et al 2004][research_ali_sadrulislam_2004]\] \[[Alspach et al 2018][research_alspach_webb_2018]\] \[[Ambe Verma et al 2021][research_ambeverma_muraripandey_2021]\] \[[Ferri and Fox 1969][research_ferri_fox_1969]\] \[[yang and culick 1986][research_yang_culick_1986]\] \[[Bonanni et al 2024][research_bonanni_norris_2024]\] \[[Schetz et al 1991][research_schetz_billig_1991]\] \[[Andreadis et al 2002][research_andreadis_drake_2002]\] \[[Li et al 2023][research_li_wang_2023]\] \[[Viaud and Mestre 1966][research_viaud_mestre_1966]\] \[[Yang et al 1993][research_yang_kubota_1993]\] \[[Peschke 1995][research_peschke_1995]\] \[[Bakos 2024][research_bakos_2024]\] \[[Barth 2014][research_barth_2014]\] \[[Barth et al 2014][research_barth_wheatley_2014]\] \[[Billig 1967][research_billig_1967]\] \[[Brescianini 2023][research_brescianini_2023]\] \[[Burnett and Czysz 1963][research_burnett_czysz_1963]\] \[[Bush et al 1996][research_bush_tiwari_1996]\] \[[Hornbeck 1975][research_hornbeck_1975]\] \[[Clauss et al 1994][research_clauss_sontgen_1994]\] \[[Liu et al 2019][research_liu_baccarella_2019]\] \[[Roga 2019][research_roga_2019]\] \[[Roga 2019][research_roga_2019_b]\] \[[Urso et al 2022][research_urso_kinney_2022]\] \[[Choubey and Tiwari 2022][research_choubey_tiwari_2022_c]\] \[[Choubey and Tiwari 2022][research_choubey_tiwari_2022_b]\] \[[van Staden et al 2020][research_vanstaden_lorrain_2020]\] \[[Cui et al 2015][research_cui_wang_2015]\] \[[Jeong and Choi 2020][research_jeong_choi_2020]\] \[[Yamaguchi et al 2020][research_yamaguchi_hizawa_2020]\] \[[Segal et al 1991][research_segalcorin_mcdanieljamesc_1991]\] \[[Yasunaga et al 2024][research_yasunaga_nakaya_2024]\] \[[Wang et al 2020][research_wang_li_2020]\] \[[van der Lee et al 2026][research_vanderlee_kaner_2026]\] \[[Yang et al 2020][research_yang_lee_2020]\] \[[Combustion Scaling in an 2012][research_combustion_scaling_2012]\] \[[Shajahan et al 2025][research_shajahan_gugulothu_2025]\] \[[Wu and Wei 2022][research_wu_wei_2022]\] \[[Xue et al 2025][research_xue_he_2025]\] \[[Verma et al 2021][research_verma_pandey_2021]\] \[[Dash et al 1986][research_dashsm_sinhan_1986]\] \[[Roux and Tiruveedula 2016][research_roux_tiruveedula_2016]\] \[[Roux and Tiruveedula 2017][research_roux_tiruveedula_2017]\] \[[Rodríguez Fuentes and Parent 2023][research_rodriguezfuentes_parent_2023]\] \[[Coras and Paull 2006][research_coras_paull_2006]\] \[[Waltrup et al 1981][research_waltrup_billig_1981]\] \[[Curran 2017][research_curran_2017]\] \[[Current State-of-the-Art for Airbreathing 1974][research_current_state_of_the_art_1974]\] \[[Cutler 1998][research_cutler_1998]\] \[[Degregori and Ferlauto 2018][research_degregori_ferlauto_2018_b]\] \[[Denman 2018][research_denman_2018]\] \[[Rayle and Koch 1954][research_raylewarrend_kochrichardg_1954]\] \[[Baccarella et al 2016][research_baccarella_liu_2016]\] \[[Dewangan and Parwani 2026][research_dewangan_parwani_2026]\] \[[Capriotti][research_diegopcapriotti]\] \[[Diskin et al 1987][research_diskin_jachimowski_1987]\] \[[Drummond 1979][research_drummond_1979]\] \[[MacLeod et al 2025][research_macleod_gibson_2025]\] \[[Liu et al 2017][research_liu_zhao_2017]\] \[[Fletcher 1967][research_fletcher_1967]\] \[[Choubey and Pandey 2017][research_choubey_pandey_2017]\] \[[Choubey et al 2023][research_choubey_solanki_2023]\] \[[Choubey and Pandey 2018][research_choubey_pandey_2018]\] \[[Zong et al 2015][research_zong_bao_2015]\] \[[Ma et al 2021][research_ma_sun_2021]\] \[[Kummitha 2022][research_kummitha_2022]\] \[[Li et al 2023][research_li_leng_2023]\] \[[Peng et al 2024][research_peng_zhou_2024]\] \[[Yan et al 2026][research_yan_le_2026]\] \[[Nair et al 2023][research_nair_suryan_2023]\] \[[Mahto et al 2016][research_mahto_choubey_2016]\] \[[Kummitha and Pandey 2020][research_kummitha_pandey_2020]\] \[[Kummitha and Kandula 2024][research_kummitha_kandula_2024]\] \[[Takahashi et al 1998][research_takahashi_wakai_1998]\] \[[Effects of compression and 1993][research_effects_of_1993]\] \[[Oamjee and Sadanandan 2020][research_oamjee_sadanandan_2020]\] \[[Oamjee and Sadanandan 2020][research_oamjee_sadanandan_2020_b]\] \[[Diskin and Northam 1987][research_diskinglenns_northamgburton_1987]\] \[[Baş 2026][research_bas_2026]\] \[[Nishiguchi et al 2025][research_nishiguchi_kodera_2025]\] \[[Eggers et al 1978][research_eggers_reagon_1978]\] \[[Engblom et al 2005][research_engblom_frate_2005]\] \[[Pulsonetti et al 1991][research_pulsonetti_erdos_1991]\] \[[Singh and Mukhopadhyay 2025][research_singh_mukhopadhyay_2025]\] \[[Drummond 1997][research_drummondjphilip_1997]\] \[[Liu et al 2024][research_liu_pan_2024]\] \[[McClinton and Anderson 1980][research_mcclintoncr_andersongy_1980]\] \[[Swain et al 2020][research_swain_p_2020]\] \[[Economos 1966][research_economosc_1966]\] \[[Landsberg et al 2022][research_landsberg_curran_2022]\] \[[Cohen-Zur and Natan 1998][research_cohenzur_natan_1998]\] \[[Anderson et al 1977][research_andersongy_reagonpg_1977]\] \[[Nakaya et al 2021][research_nakaya_yamana_2021]\] \[[Hirayama et al 2026][research_hirayama_hamaji_2026]\] \[[Zhang et al 2023][research_zhang_lin_2023]\] \[[Golui et al 2025][research_golui_ranjith_2025]\] \[[Li et al 2018][research_li_jiao_2018]\] \[[Li et al 2025][research_li_li_2025]\] \[[Tian et al 2018][research_tian_zeng_2018]\] \[[Rogers et al 1998][research_rogersrclayton_capriottidiegop_1998]\] \[[Yan and Yang 2025][research_yan_yang_2025]\] \[[Ju and Niioka 1994][research_ju_niioka_1994_b]\] \[[Vanamamalai and Panneerselvam 2024][research_vanamamalai_panneerselvam_2024]\] \[[Cao et al 2021][research_cao_brod_2021]\] \[[Schetz et al 1982][research_schetz_billig_1982]\] \[[Chun et al 1994][research_chunks_lockerj_1994]\] \[[Schetz et al 1969][research_schetz_gilreath_1969]\] \[[Oamjee and Sadanandan 2019][research_oamjee_sadanandan_2019]\] \[[Wang et al 2025][research_wang_an_2025]\] \[[Drummond et al 2006][research_drummondjphilip_diskinglenns_2006]\] \[[Swithenbank and Jaques 1970][research_swithenbank_jaques_1970]\] \[[Hawk and Nelson 1998][research_hawk_nelson_1998]\] \[[He et al 2026][research_he_zhou_2026]\] \[[Sabelkin et al 2017][research_sabelkin_zawada_2017]\] \[[Hunt 2015][research_hunt_2015]\] \[[Kummitha and Pandey 2021][research_kummitha_pandey_2021]\] \[[Ben Hamida et al 2025][research_benhamida_basem_2025]\] \[[Beach 1976][research_beachhljr_1976]\] \[[Thompson and Hoffman 1992][research_thompsonhdoyle_hoffmanjoed_1992]\] \[[Chakravarthy et al 2021][research_chakravarthy_randive_2021]\] \[[Lakka et al 2021][research_lakka_randive_2021]\] \[[Suneetha et al 2021][research_suneetha_randive_2021]\] \[[Bulman et al 1997][research_bulmanmj_stoutpw_1997]\] \[[Atci et al 2024][research_atci_jeyakumar_2024]\] \[[Zhang et al 2025][research_zhang_liang_2025]\] \[[Barre et al 1997][research_barre_braud_1997]\] \[[Aziz et al 2022][research_aziz_chowdhury_2022]\] \[[Vasil'ev and Petrov 1977][research_vasilev_petrov_1977]\] \[[Xiong et al 2020][research_xiong_qin_2020]\] \[[M․V․V․ and Rajagopal 2026][research_mvv_rajagopal_2026]\] \[[Chakravarthy and Randive 2022][research_chakravarthy_randive_2022]\] \[[Yan et al 2025][research_yan_tian_2025]\] \[[Du et al 2025][research_du_chen_2025]\] \[[Ma et al 2025][research_ma_zhao_2025]\] \[[Investigation of mixing characteristics of gaseous kerosene...][research_investigation_of_2023]\] \[[Tang et al 2024][research_tang_wang_2024]\] \[[Soni and De 2017][research_soni_de_2017]\] \[[Zhang et al 2019][research_zhang_cao_2019]\] \[[Jacobs et al 1990][research_jacobs_rogers_1990]\] \[[Jo et al 2026][research_jo_sung_2026]\] \[[Kamath and McClinton 1992][research_kamath_mcclinton_1992]\] \[[Kamath et al 1991][research_kamath_mao_1991]\] \[[Kim and Kwon 2017][research_kim_kwon_2017]\] \[[Kimmerly 2024][research_kimmerly_2024]\] \[[Kishida 2006][research_kishida_2006]\] \[[Kishore N et al 2023][research_kishoren_gugulothu_2023]\] \[[Ladeinde 2021][research_ladeinde_2021]\] \[[Khali and Yao 2018][research_khali_yao_2018]\] \[[Li and Luo 2012][research_li_luo_2012]\] \[[Li et al 2009][research_li_yu_2009]\] \[[Dupont et al 1999][research_dupont_muscat_1999]\] \[[Ma et al 2017][research_ma_yin_2017]\] \[[Macheret et al 2005][research_macheret_shneider_2005]\] \[[Opacich and Ombrello 2026][research_opacich_ombrello_2026]\] \[[Chang and Tiernan 1986][research_chang_tiernan_1986]\] \[[McClinton 1976][research_mcclinton_1976]\] \[[McClinton 1978][research_mcclinton_1978]\] \[[McClinton and Gooderum 1977][research_mcclinton_gooderum_1977]\] \[[McDaniel 1998][research_mcdanieljr_1998]\] \[[Luo et al 2025][research_luo_sun_2025]\] \[[O'Byrne et al 1999][research_obyrne_doolan_1999]\] \[[Measurement Techniques for Supersonic 1974][research_measurement_techniques_1974]\] \[[Busa et al 2013][research_busakristin_ellisonerikn_2013]\] \[[Menees et al 1989][research_menees_bowles_1989]\] \[[Michalski et al 2018][research_michalski_boust_2018]\] \[[Mitani and Kouchi 2005][research_mitani_kouchi_2005]\] \[[Liu et al 2023][research_liu_sun_2023]\] \[[Shen et al 2021][research_shen_huang_2021]\] \[[Drummond et al 1989][research_drummondjphilip_carpentermarkh_1989]\] \[[Drummond 1991][research_drummondjp_1991]\] \[[Maikap and Rajagopal 2024][research_maikap_rajagopal_2024]\] \[[Ferri 1973][research_ferri_1973]\] \[[Kim and Kwon 2018][research_kim_kwon_2018]\] \[[Neill and Pesyridis 2017][research_neill_pesyridis_2017]\] \[[Moon and Chung 1996][research_moon_chung_1996]\] \[[Mu et al 2022][research_mu_wang_2022]\] \[[Ngo 2017][research_ngo_2017]\] \[[niu and wang 2023][research_niu_wang_2023]\] \[[Jensen et al 1972][research_jensenrm_bryceca_1972]\] \[[McClinton et al 1975][research_mcclintoncr_torrencemg_1975]\] \[[Candon and Ogawa 2018][research_candon_ogawa_2018]\] \[[Kummitha 2017][research_kummitha_2017]\] \[[Kummitha et al 2017][research_kummitha_suneetha_2017]\] \[[Kandula and Kummitha 2025][research_kandula_kummitha_2025]\] \[[Numerical Comparative Analysis of the Influence of Fuel...][research_numerical_comparative_2024]\] \[[Dharavath et al 2015][research_dharavath_manna_2015]\] \[[Soumyajit Saha and Debasis Chakraborty 2023][research_soumyajitsaha_debasischakraborty_2023]\] \[[Zhang et al 2016][research_zhang_li_2016]\] \[[Roos et al 2020][research_roos_pudsey_2020]\] \[[Jeong et al 2023][research_jeong_lee_2023]\] \[[Choubey et al 2027][research_choubey_panging_2027]\] \[[Venkateshwaran and Padmanathan 2026][research_venkateshwaran_padmanathan_2026]\] \[[Choubey et al 2022][research_choubey_gaud_2022]\] \[[Abdelhameed and Watanabe 2025][research_abdelhameed_watanabe_2025]\] \[[Kireeti et al 2022][research_kireeti_ravikiransastry_2022]\] \[[Athithan and Jeyakumar 2022][research_athithan_jeyakumar_2022]\] \[[Behera and Chakraborty 2023][research_behera_chakraborty_2023]\] \[[Dudebout et al 1998][research_dudebout_sislian_1998]\] \[[Ullman et al 2025][research_ullman_sharma_2025]\] \[[Gerlinger et al 1994][research_gerlinger_bruggemann_1994]\] \[[He et al 2024][research_he_tian_2024]\] \[[Numerical Simulation on Hypersonic Combustion of...][research_numerical_simulation_2015]\] \[[Numerical Study of Mixing in an Air-Breathing Rocket Engine][research_numerical_study_2015]\] \[[Lu et al 2015][research_lu_zhansen_2015]\] \[[Li et al 2023][research_li_li_2023]\] \[[Li et al 2024][research_li_zhao_2024]\] \[[Barbi et al 1989][research_barbie_mahanjr_1989]\] \[[Kummitha and Kandula 2025][research_kummitha_kandula_2025]\] \[[Kummitha et al 2018][research_kummitha_pandey_2018]\] \[[da Silva et al 2026][research_dasilva_decastrodasilva_2026]\] \[[Cao and Yu 2021][research_cao_yu_2021]\] \[[Satyanarayan et al 2026][research_satyanarayan_raj_2026]\] \[[Das et al 2025][research_das_debnath_2025]\] \[[Manna et al 2023][research_manna_dharavath_2023]\] \[[Pinckney and Walton 1994][research_pinckney_walton_1994]\] \[[Niu and Chen 2026][research_niu_chen_2026]\] \[[Debnath and Roy 2023][research_debnath_roy_2023]\] \[[Liu et al 2026][research_liu_zhang_2026]\] \[[Pudsey 2014][research_pudsey_2014]\] \[[Cheng et al 1994][research_cheng_wehrmeyer_1994]\] \[[Hojnacki 1972][research_hojnacki_1972]\] \[[Ikawa 1991][research_ikawa_1991]\] \[[McGann et al 2026][research_mcgann_carter_2026]\] \[[Özbek and Karyeyen 2023][research_ozbek_karyeyen_2023]\] \[[Ispir et al 2023][research_ispir_zdybal_2023]\] \[[Zhang et al 2023][research_zhang_feng_2023]\] \[[Qiu et al 2021][research_qiu_zhang_2021]\] \[[Quan et al 2024][research_quan_chang_2024]\] \[[Zhou et al 2025][research_zhou_tian_2025]\] \[[Research Progress in Active 2026][research_research_progress_2026]\] \[[Liu et al 2020][research_liu_baccarella_2020]\] \[[Rubins and Bauer 1994][research_rubins_bauer_1994]\] \[[Riggins et al 1992][research_riggins_mcclinton_1992]\] \[[Rodríguez Fuentes and Parent 2022][research_rodriguezfuentes_parent_2022]\] \[[Rogers and Weidner 1991][research_rogers_weidner_1991]\] \[[Rogers et al 1994][research_rogers_weidner_1994]\] \[[Li et al 2019][research_li_chen_2019]\] \[[Rose and Sridhar 2022][research_rose_sridhar_2022]\] \[[Rouzbar and Eyi 2015][research_rouzbar_eyi_2015]\] \[[Rowan 2024][research_rowan_2024]\] \[[Ruan et al 2020][research_ruan_domingo_2020]\] \[[Russin 1974][research_russin_1974]\] \[[Schultz et al 2012][research_schultz_goldenstein_2012]\] \[[Scramjet Combustion 2022][research_scramjet_combustion_2022]\] \[[Scramjet Combustor 2022][research_scramjet_combustor_2022]\] \[[Willbanks 1970][research_willbanks_1970]\] \[[Diskin and Northam 1988][research_diskinglenns_northamgburton_1988]\] \[[Shenoy et al 2019][research_shenoy_drozda_2019]\] \[[Niu and Chen 2025][research_niu_chen_2025]\] \[[Niu and Chen 2024][research_niu_chen_2024]\] \[[Sihvola 2018][research_sihvola_2018]\] \[[Smart 2024][research_smart_2024]\] \[[Smith 1979][research_smith_1979]\] \[[Spatially Resolved Temperature and Water Vapor Concentration...][research_busakm_mcdanieljc_2012]\] \[[Species measurements in a 1996][research_species_measurements_1996]\] \[[Steffen et al 2002][research_steffen_bond_2002]\] \[[Street 2024][research_street_2024]\] \[[Dou et al 2022][research_dou_yang_2022]\] \[[Peng et al 2025][research_peng_yin_2025]\] \[[Kirkby 1964][research_kirkby_1964]\] \[[Kydd and Mullaney 1961][research_kydd_mullaney_1961]\] \[[Urzay 2018][research_urzay_2018]\] \[[Slutsky et al 1965][research_slutsky_tamagno_1965]\] \[[Niu and Chen 2026][research_niu_chen_2026_b]\] \[[Meng et al 2022][research_meng_sun_2022]\] \[[Gruenig and Mayinger 1999][research_gruenig_mayinger_1999]\] \[[Supersonic Combustion Processes 2009][research_supersonic_combustion_2009]\] \[[Billig 1995][research_billig_1995]\] \[[Carter 2012][research_carter_2012]\] \[[Supersonic Flow Combustors 2001][research_supersonic_flow_2001]\] \[[Stalker and Morgan 1984][research_stalker_morgan_1984]\] \[[Huang et al 2019][research_huang_du_2019]\] \[[Du et al 2025][research_du_chen_2025_b]\] \[[Suraweera 2024][research_suraweera_2024]\] \[[Boles and Milligan 2013][research_boles_milligan_2013]\] \[[Zheng and Bray 1994][research_zheng_bray_1994]\] \[[Russin 1975][research_russinwr_1975]\] \[[Kummitha 2024][research_kummitha_2024]\] \[[Relangi et al 2022][research_relangi_ingenito_2022]\] \[[Wei et al 2024][research_wei_jiao_2024]\] \[[Libby 1962][research_libby_1962]\] \[[Chen and Wang 2026][research_chen_wang_2026]\] \[[Luo et al 2024][research_luo_qu_2024]\] \[[Thompson and Friedman 1991][research_thompson_friedman_1991]\] \[[DeSpirito 2015][research_despirito_2015]\] \[[Patrick 2021][research_patrick_2021]\] \[[Feng and Wang 2025][research_feng_wang_2025]\] \[[Barpande et al 2021][research_barpande_singh_2021]\] \[[Lu et al 2025][research_lu_sheng_2025]\] \[[Venkatapathy et al 1995][research_venkatapathy_tokarcikpolsky_1995]\] \[[Swithebank and Chigier 1969][research_swithebank_chigier_1969]\] \[[Waidmann et al 2024][research_waidmann_brummund_2024]\] \[[Wang 2023][research_wang_2023]\] \[[Wang et al 2023][research_wang_xu_2023_b]\] \[[Webb and Samimy 2016][research_webb_samimy_2016]\] \[[Yip et al 1990][research_yip_strawa_1990]\] \[[Yongsheng 2014][research_yongsheng_2014]\] \[[Yu et al 2005][research_yu_kim_2005]\] \[[Yungster 1992][research_yungster_1992]\] \[[Zhou et al 2025][research_zhou_cao_2025]\]

### Impulse and high-enthalpy ground test facilities

**The ground facilities that reach the enthalpy and the instruments used in them.** Shock tunnels, expansion tubes, arc-heated and combustion-heated tunnels, their calibration, their test time and the measurements made in milliseconds.

**287 records.** \[[Brune et al 2020][research_brune_2020]\] \[[Hildebrand et al 2022][research_hildebrand_2022]\] \[[Huebner et al 1996][research_huebner_1996]\] \[[Matsuda 2015][research_matsuda_2015]\] \[[1985, Prediction and Verification of Aerodynamic Drag, Part II Wind-Tunnel/Flight][research_prediction_and_1985_b]\] \[[Gildfind and Morgan 2015][research_gildfind_morgan_2015]\] \[[Lubbock et al 2018][research_lubbock_luque_2018]\] \[[Lee et al 2015][research_lee_kang_2015]\] \[[Gildfind 2024][research_gildfind_2024]\] \[[Torre et al 2023][research_torre_merli_2023]\] \[[Penland and Romeo 1971][research_penland_romeo_1971]\] \[[Lominac and Boytos 1998][research_lominac_boytos_1998]\] \[[Aerothermodynamics Research in the 2002][research_aerothermodynamics_research_2002]\] \[[Ahmed et al 2023][research_ahmed_ameenk_2023]\] \[[Ahmed et al 2024][research_ahmed_saenz_2024]\] \[[Aircraft Engine Test Facility][research_aircraft_engine_1992]\] \[[Albertson and Emami 2001][research_albertson_emami_2001]\] \[[Shadow 1987][research_shadow_1987]\] \[[Petervari et al 2026][research_petervari_wagner_2026]\] \[[Nanda et al 2019][research_nanda_kulkarni_2019]\] \[[Anbuselvan et al 2010][research_anbuselvan_menezes_2010]\] \[[Andrews 1978][research_andrews_1978]\] \[[Andrianatos 2020][research_andrianatos_2020]\] \[[Thomas and Perlbachs 1967][research_thomas_perlbachs_1967]\] \[[Kim et al 2022][research_kim_jang_2022]\] \[[Bajpai and Jagadeesh 2023][research_bajpai_jagadeesh_2023]\] \[[Bakos et al 1995][research_bakos_chinitz_1995]\] \[[Balboni and Atler 1993][research_balboni_atler_1993]\] \[[Bathel et al 2019][research_bathel_jones_2019]\] \[[Beck et al 1998][research_beck_eitelberg_1998]\] \[[Bhagwandin and Sahu 2023][research_bhagwandin_sahu_2023]\] \[[Bogdanoff and Edwards 1995][research_bogdanoff_edwards_1995]\] \[[Bogdanoff et al 1996][research_bogdanoff_wilson_1996]\] \[[Bogdanoff et al 1997][research_bogdanoff_wilson_1997]\] \[[Boyer 1965][research_boyer_1965]\] \[[Brescianini and Morgan 1992][research_brescianini_morgan_1992]\] \[[Bui 2025][research_bui_2025]\] \[[Burton et al 1990][research_burton_witherspoon_1990]\] \[[Surzhikov 2021][research_surzhikov_2021]\] \[[Surzhikov 2021][research_surzhikov_2021_b]\] \[[California Inst Of Tech Pasadena 1990][research_californiainstoftechpasadena_1990]\] \[[Calspan Ub Research Center Buffalo Ny 1990][research_calspanubresearchcenterbuffalony_1990]\] \[[Candler and Nompelis 2006][research_candler_nompelis_2006]\] \[[Capra et al 2004][research_capra_leyland_2004]\] \[[Carpenter et al 1967][research_carpenter_graves_1967]\] \[[Purpura et al 2018][research_purpura_trifoni_2018]\] \[[Cruden et al 2021][research_cruden_tang_2021]\] \[[Liu et al 2025][research_liu_li_2025]\] \[[Baccarella and Samuels 2025][research_baccarella_samuels_2025]\] \[[Chazot and Panerai 2015][research_chazot_panerai_2015]\] \[[McClure and Sirbaugh 1991][research_mcclure_sirbaugh_1991]\] \[[Brune et al 2019][research_brune_bruce_2019]\] \[[Brune et al 2017][research_bruneaj_bruceweiii_2017]\] \[[Fang et al 2026][research_fang_zeng_2026]\] \[[Dougherty 1975][research_dougherty_1975]\] \[[Kumar et al 2017][research_kumar_rakesh_2017]\] \[[Czysz 1963][research_czysz_1963]\] \[[Czysz 1963][research_czysz_1963_b]\] \[[Patterson 2010][research_patterson_2010]\] \[[Deangelis and Anderson 1992][research_deangelis_anderson_1992]\] \[[Deiwert et al 1994][research_deiwert_cavalowsky_1994]\] \[[Midden and Miller 1985][research_middenraymonde_millercharlesgiii_1985]\] \[[Bouchard and Chambers 1966][research_bouchard_chambers_1966]\] \[[Lynch et al 2023][research_lynch_grasser_2023]\] \[[Saenz et al 2025][research_saenz_frankel_2025]\] \[[Nagamatsu et al 1961][research_nagamatsu_sheer_1961]\] \[[Kamal 2025][research_kamal_2025]\] \[[Design/Construction and Performance Test 2008][research_design_construction_and_2008]\] \[[Stanley et al 2013][research_stanley_lopp_2013]\] \[[Ji et al 2019][research_ji_li_2019]\] \[[Beckwith 1975][research_beckwith_1975]\] \[[Yang et al 2024][research_yang_choi_2024]\] \[[Development of the Shock 1962][research_development_of_1962]\] \[[Direct measurements of skin 1994][research_direct_measurements_1994]\] \[[Yang et al 2021][research_yang_xia_2021]\] \[[Dufrene 2015][research_dufrene_2015]\] \[[Turchi et al 2021][research_turchi_matesanzsaiz_2021]\] \[[Andrews et al 1985][research_earlhandrewsjr_marvingtorrence_1985]\] \[[Chang et al 2020][research_chang_chan_2020]\] \[[Shi et al 2020][research_shi_zhu_2020]\] \[[Shen et al 2025][research_shen_yao_2025]\] \[[Erdos and Erdos 1997][research_erdos_erdos_1997]\] \[[Kim et al 2025][research_kim_shim_2025]\] \[[Sudhiesh Kumar and Reddy 2015][research_sudhieshkumar_reddy_2015]\] \[[Paull et al 1995][research_paull_stalker_1995]\] \[[Chinitz et al 1994][research_chinitz_erdos_1994]\] \[[Fasoulas 1996][research_fasoulas_1996]\] \[[Fasoulas and Messerschmid 1996][research_fasoulas_messerschmid_1996]\] \[[McTaggart 1973][research_mctaggart_1973]\] \[[Flow Calibration and Test Facility][research_flow_calibration_1982]\] \[[Abul-Huda and Gamba 2017][research_abulhuda_gamba_2017]\] \[[Foelsche et al 2001][research_foelsche_rogers_2001]\] \[[Smart and Ruf 2006][research_smartmichaelk_rufedwardg_2006]\] \[[Shekhtman et al 2021][research_shekhtman_yu_2021]\] \[[Fuehrer 1969][research_fuehrer_1969]\] \[[Garberoglio 1969][research_garberoglio_1969]\] \[[Deep and Jagadeesh 2021][research_deep_jagadeesh_2021]\] \[[Geiger 1963][research_geiger_1963]\] \[[Gildfind et al 2012][research_gildfind_morgan_2012]\] \[[Gildfind et al 2014][research_gildfind_morgan_2014]\] \[[Gildfind et al 2015][research_gildfind_sancho_2015]\] \[[Gildfind et al 2017][research_gildfind_jacobs_2017]\] \[[Gion 1968][research_gion_1968]\] \[[Goodrich et al 1983][research_goodrich_derry_1983]\] \[[Grabau et al 1964][research_grabau_smithson_1964]\] \[[Gregorek and Lee 1962][research_gregorek_lee_1962]\] \[[Ground Testing and Evaluation 2022][research_ground_testing_2022]\] \[[Ground Testing Facility for Hypersonic Materials][research_ground_testing_2023]\] \[[Anderson et al 1987][research_andersongriffiny_benczedanielp_1987]\] \[[Guy et al 1976][research_guy_mueller_1976]\] \[[Guy et al 1981][research_guy_torrence_1981]\] \[[Haas 1963][research_haas_1963]\] \[[Hagenmaier et al 2011][research_hagenmaier_eklund_2011]\] \[[Kumar and Reddy 2018][research_kumar_reddy_2018]\] \[[Hass et al 2005][research_hass_shih_2005]\] \[[Hatzl et al 2010][research_hatzl_sander_2010]\] \[[Haun and Ball 1966][research_haun_ball_1966]\] \[[Richards et al 1971][research_richards_culotta_1971]\] \[[Connor et al 1971][research_connorle_sparksvw_1971]\] \[[Hertzberg et al 1961][research_hertzberg_wittliff_1961]\] \[[Martinez Schramm et al 2024][research_martinezschramm_wagner_2024]\] \[[Hollis and Perkins 1996][research_hollis_perkins_1996]\] \[[Hypersonic flight regime and 2017][research_hypersonic_flight_2017]\] \[[Dicristina 1979][research_dicristina_1979]\] \[[Igra 2026][research_igra_2026]\] \[[Selcan et al 2021][research_selcan_sander_2021]\] \[[Guy and Mackley 1979][research_guyrw_mackleyea_1979]\] \[[Lee et al 2022][research_lee_duan_2022]\] \[[Itoh 2007][research_itoh_2007]\] \[[Itoh et al 2002][research_itoh_ueda_2002]\] \[[Jackson and Blanchard 1964][research_jackson_blanchard_1964]\] \[[Jewell et al 2013][research_jewell_shepherd_2013]\] \[[Jiang et al 2017][research_jiang_wang_2017]\] \[[Micol][research_johnrmicol]\] \[[Rodriguez et al][research_josemrodriguez_brettfbathel]\] \[[Kidd et al 2014][research_kidd_narayanaswamy_2014]\] \[[Samuels et al][research_killiansamuels_talschwartz]\] \[[Kim and Park 2020][research_kim_park_2020]\] \[[Kim et al 2019][research_kim_park_2019]\] \[[Kim et al 2024][research_kim_shim_2024]\] \[[Micol 1998][research_micoljr_1998]\] \[[Boatright et al 1976][research_boatrightwb_sabolap_1976]\] \[[Laurence et al 2012][research_laurence_martinezschramm_2012]\] \[[Lee and Lewis 1991][research_lee_lewis_1991]\] \[[Lee et al 2012][research_lee_kang_2012]\] \[[Li and Yang 2017][research_li_yang_2017]\] \[[Li et al 2018][research_li_huang_2018]\] \[[Altenhöfer et al 2018][research_altenhofer_sander_2018]\] \[[Livingston 1965][research_livingston_1965]\] \[[Lobb et al 1955][research_lobb_winkler_1955]\] \[[Loehle 2016][research_loehle_2016]\] \[[Loney 1994][research_loney_1994]\] \[[Lord et al 1960][research_lord_boersen_1960]\] \[[Carson and Midden 1976][research_carsongtjr_middenre_1976]\] \[[Lee et al 2022][research_lee_yang_2022_b]\] \[[Lee et al 2022][research_lee_yang_2022]\] \[[MacKinnon et al 2004][research_mackinnon_beitel_2004]\] \[[Spencer 1962][research_spencer_1962]\] \[[Matsui et al 2008][research_matsui_shinmi_2008]\] \[[Matthew McGilvray 2024][research_matthewmcgilvray_2024]\] \[[McGilvray et al 2006][research_mcgilvray_jacobs_2006]\] \[[McGilvray et al 2010][research_mcgilvray_kirchhartz_2010]\] \[[McIntyre et al 1998][research_mcintyre_bishop_1998]\] \[[McRae and Zikry 1999][research_mcrae_zikry_1999]\] \[[Fletcher 2000][research_fletcherdouglasg_2000]\] \[[Melis and Gladden 1990][research_melis_gladden_1990]\] \[[Meritt and Schetz 2014][research_meritt_schetz_2014]\] \[[Purpura 2021][research_purpura_2021]\] \[[Kurosaka and Shimamura 2024][research_kurosaka_shimamura_2024]\] \[[Kelly and Wieting 1984][research_kellyhn_wietingar_1984]\] \[[Reubush et al 1987][research_reubushde_pusterrl_1987]\] \[[Modroukas et al 1998][research_modroukas_betti_1998]\] \[[Morgan and Stalker 1985][research_morgan_stalker_1985]\] \[[Morgan et al 1985][research_morgan_paull_1985]\] \[[Morgan et al 1986][research_morgan_paull_1986]\] \[[NASA's HYPULSE Facility at 2002][research_nasa_s_hypulse_2002]\] \[[Hass and Cabell][research_nealehass_karenfcabell]\] \[[Neely 2022][research_neely_2022]\] \[[Neely and Morgan 1995][research_neely_morgan_1995]\] \[[Gilbert et al 2009][research_gilbertmichael_rajuivatury_2009]\] \[[Neumann 1990][research_neumann_1990]\] \[[Inman et al 2011][research_inmanjennifera_bathelbrettf_2011]\] \[[Inman et al 2013][research_inmanjennifera_bathelbrettf_2013]\] \[[Chan et al 2021][research_chan_whitside_2021]\] \[[Watt and Aronson 1964][research_watt_aronson_1964]\] \[[Norman et al 1966][research_norman_walker_1966]\] \[[Thiele et al 2018][research_thiele_gampe_2018]\] \[[Tang et al 2019][research_tang_wang_2019]\] \[[Yu et al 2022][research_yu_li_2022]\] \[[Ishihara et al 2015][research_ishihara_ogino_2015]\] \[[Jiao et al 2017][research_jiao_chang_2017]\] \[[Ishihara et al 2016][research_ishihara_ogino_2016]\] \[[Oerley et al 2012][research_oerley_gamba_2012]\] \[[Oertel 1970][research_oertel_1970]\] \[[Oertel and Fritz H. 1972][research_oertel_fritzh_1972]\] \[[Olejniczak et al 1996][research_olejniczak_candler_1996]\] \[[Osgerby et al 1969][research_osgerby_smithson_1969]\] \[[Slater et al 2005][research_slaterjohnw_davisdavido_2005]\] \[[Park 1996][research_park_1996]\] \[[Parsons and Richmond 1969][research_parsons_richmond_1969]\] \[[Paull 1999][research_paull_1999]\] \[[Paull and Stalker 1998][research_paull_stalker_1998]\] \[[Paull et al 1988][research_paull_stalker_1988]\] \[[Paull et al 1995][research_paull_stalker_1995_b]\] \[[Irimpan et al 2015][research_irimpan_mannil_2015]\] \[[Wang et al 2018][research_wang_li_2018_b]\] \[[Porter 2022][research_porter_2022]\] \[[Wolfle 1969][research_wolfle_1969]\] \[[Raj et al 2019][research_raj_sandhu_2019]\] \[[Ramanah and Mee 2006][research_ramanah_mee_2006]\] \[[Yang et al 2020][research_yang_gui_2020]\] \[[Elder 1975][research_elderdj_1975]\] \[[Rich et al 2007][research_rich_lempert_2007]\] \[[Rizkalla et al 1989][research_rizkalla_bakos_1989]\] \[[Rogers et al 2001][research_rogers_shih_2001]\] \[[Sandborn and Heron 1963][research_sandborn_heron_1963]\] \[[Sauerwein et al 2015][research_sauerwein_hruschka_2015]\] \[[Scaggs et al 1963][research_scaggs_burggraf_1963]\] \[[Scramjet Testing in the 2001][research_scramjet_testing_2001]\] \[[Sekar et al 1990][research_sekar_thomas_1990]\] \[[Serre 2011][research_serre_2011]\] \[[Sharma 1992][research_sharma_1992]\] \[[Shen et al 2019][research_shen_zhang_2019]\] \[[Sriram et al 2015][research_sriram_ram_2015]\] \[[Stalker 1996][research_stalkerrj_1996]\] \[[Stalker et al 1995][research_stalkerrj_bakosrj_1995]\] \[[Casey et al 1990][research_caseyr_stalkerrj_1990]\] \[[Wendt et al 1993][research_wendtm_nettletonm_1993]\] \[[Bakos et al 1993][research_bakosrj_morganrg_1993]\] \[[Stalker et al 1993][research_stalkerrj_hollisp_1993]\] \[[Loomis 1994][research_loomismarkp_1994]\] \[[Shumskii and Yaroslavtsev 2012][research_shumskii_yaroslavtsev_2012]\] \[[Simeonides 2006][research_simeonides_2006]\] \[[Skinner and Stalker 1995][research_skinner_stalker_1995]\] \[[Stalker and Morgan 1987][research_stalker_morgan_1987]\] \[[Stalker et al 1994][research_stalker_simmons_1994]\] \[[Stalker et al 1995][research_stalker_simmons_1995]\] \[[Stalker et al 1996][research_stalker_morgan_1996]\] \[[Stallings et al 2003][research_stallings_williams_2003]\] \[[Star et al 2005][research_star_edwards_2005]\] \[[Star et al 2006][research_star_edwards_2006]\] \[[Stennett 2020][research_stennett_2020]\] \[[Stennett et al 2019][research_stennett_gildfind_2019]\] \[[Stewar et al 2003][research_stewar_morgan_2003]\] \[[Stewart 2024][research_stewart_2024]\] \[[Stewart et al 2000][research_stewart_morgan_2000]\] \[[Xie et al 2026][research_xie_zhao_2026]\] \[[Osgerby et al 1970][research_osgerby_smithson_1970]\] \[[Suraweera and Smart 2008][research_suraweera_smart_2008]\] \[[Survey of Shock Tube 1962][research_survey_of_1962]\] \[[Tamagno et al 1990][research_tamagno_bakos_1990]\] \[[Hodge and Harvin 2000][research_hodgejeffreys_harvinstephenf_2000]\] \[[Harvin et al 2006][research_harvinsf_cabellkf_2006]\] \[[Varwig 1963][research_varwig_1963]\] \[[Hertzberg 1956][research_hertzberg_1956]\] \[[Wagner and Dale 1985][research_wagner_dale_1985]\] \[[Hannemann et al 2018][research_hannemann_martinezschramm_2018]\] \[[Denenberg 1986][research_denenberg_1986]\] \[[TokarcikPolsky et al 1995][research_tokarcikpolskys_papadopoulosp_1995]\] \[[Stapp 1995][research_stapp_1995]\] \[[Lee et al 2020][research_lee_kim_2020]\] \[[Thomas and Guy 1982][research_thomas_guy_1982]\] \[[Thomas and Guy 1983][research_thomas_guy_1983]\] \[[Thomas et al 1987][research_thomas_voland_1987]\] \[[Thomas et al 2010][research_thomas_lee_2010]\] \[[Thompson and Pandolfini 1995][research_thompson_pandolfini_1995]\] \[[Tomioka et al 2007][research_tomioka_ueda_2007]\] \[[Toniato 2019][research_toniato_2019]\] \[[Toniato et al 2018][research_toniato_gildfind_2018]\] \[[Malekipour et al 2021][research_malekipour_mohammadiamin_2021]\] \[[Knight and Naiman 2009][research_knight_naiman_2009]\] \[[Trivedi and Menezes 2012][research_trivedi_menezes_2012]\] \[[Trolier and Krawczyk 1996][research_trolier_krawczyk_1996]\] \[[Mohsen et al 2017][research_mohsen_yusoff_2017]\] \[[Ueda et al 2004][research_ueda_weiland_2004]\] \[[Liu et al 2024][research_liu_wang_2024]\] \[[Val et al 2020][research_val_chazot_2020]\] \[[Verant and Sagnier 1996][research_verant_sagnier_1996]\] \[[Wang et al 2017][research_wang_liu_2017]\] \[[Wilson 1992][research_wilson_1992]\] \[[Holland et al 1991][research_hollandscottd_hodgejeffreys_1991]\] \[[Lilley and Pengelly 1993][research_lilley_pengelly_1993]\] \[[Winkler 1952][research_winkler_1952]\] \[[Wittliff and Wilson 1961][research_wittliff_wilson_1961]\] \[[Yu 2015][research_yu_2015]\] \[[Zhou et al 2017][research_zhou_jiang_2017]\] \[[Zvegintsev 1993][research_zvegintsev_1993]\]

### Inlets, forebody compression and mass capture

**The first compression surface and what it delivers.** Forebodies, inlets and diffusers, pressure recovery, spillage and mass capture, from the supersonic inlets of the 1950s to the inward-turning inlets of the present.

**236 records.** \[[Yu et al 2020][research_yu_huang_2020]\] \[[Holland 1991][research_hollandscottdouglas_1991]\] \[[Chun and Burr 1969][research_chun_burr_1969]\] \[[Pordal et al 1990][research_pordalhs_khoslapk_1990]\] \[[Gao et al 2015][research_gao_li_2015]\] \[[Wang et al 2016][research_wang_wang_2016]\] \[[Kline and Alonso 2017][research_kline_alonso_2017]\] \[[Sorensen et al 1973][research_sorensen_smeltzer_1973]\] \[[Dillon et al 1980][research_dillonjl_marcumdcjr_1980]\] \[[Wang et al 2017][research_wang_cai_2017]\] \[[Chang and Hsu 1960][research_chang_hsu_1960]\] \[[Tang et al 2021][research_tang_wang_2021]\] \[[Akihisa et al 2000][research_akihisa_masuya_2000]\] \[[Barry 1971][research_barry_1971]\] \[[Agnone 1987][research_agnoneanthonym_1987]\] \[[Lehtinen and Zeller 1972][research_lehtinen_zeller_1972]\] \[[Lawrence 1992][research_lawrencescottl_1992]\] \[[Mann and Garner 1977][research_mann_garner_1977]\] \[[Başkaya and Hickel 2025][research_baskaya_hickel_2025]\] \[[Berens and Bissinger 1996][research_berens_bissinger_1996]\] \[[Benson and Maslowe 1966][research_benson_maslowe_1966]\] \[[Mayer and Paynter 1994][research_mayer_paynter_1994]\] \[[Ruban et al 2018][research_ruban_menezes_2018]\] \[[Ding et al 2021][research_ding_liu_2021]\] \[[Brenneis and Wanie 1991][research_brenneis_wanie_1991]\] \[[Bretherton 2021][research_bretherton_2021]\] \[[Molder and Szpiro 1966][research_molder_szpiro_1966]\] \[[Lai et al 1993][research_laiht_kimsc_1993]\] \[[Marvin 1991][research_marvinjg_1991]\] \[[Zhong et al 2025][research_zhong_qu_2025]\] \[[Cockrell and Huebner 1991][research_cockrelljr_huebner_1991]\] \[[Reyhner and Hickcox 1972][research_reyhner_hickcox_1972]\] \[[Pike 1996][research_pike_1996]\] \[[Huebner and Tatum 1993][research_huebner_tatum_1993]\] \[[Holland 1993][research_hollandscottd_1993]\] \[[Weidner 1979][research_weidnerjp_1979]\] \[[Hartsell 1961][research_hartsell_1961]\] \[[Holland and Perkins 1991][research_hollandscottd_perkinsjohnn_1991]\] \[[Control system design using frequency domain models and...][research_control_system_1976]\] \[[Corpening et al 1991][research_corpening_vanwie_1991]\] \[[Chima et al 2009][research_chimarodrickv_connerstimothyr_2009]\] \[[Chima et al 2010][research_chimarodrickv_connerstimothyr_2010]\] \[[Cousin 1967][research_cousin_1967]\] \[[Kaltreider 1951][research_kaltreider_1951]\] \[[Karl and Steelant 2018][research_karl_steelant_2018]\] \[[Hawkins and Richardson 1991][research_hawkinsrichardw_richardsonpamelaf_1991]\] \[[Fujio and Taguchi 2026][research_fujio_taguchi_2026]\] \[[Lee and Kang 2020][research_lee_kang_2020]\] \[[Smart 1999][research_smart_1999]\] \[[Brahmachary et al 2022][research_brahmachary_fujio_2022]\] \[[Lewis 1993][research_lewis_1993]\] \[[Seebaugh et al 1971][research_seebaughwr_doranrw_1971]\] \[[Ravi Teja et al 2022][research_raviteja_bharanichandra_2022]\] \[[Batterton et al 1974][research_battertonpg_arpasidj_1974]\] \[[Luo et al 2025][research_luo_li_2025]\] \[[Surber and Sedlock 1979][research_surber_sedlock_1979]\] \[[Zhou et al 2022][research_zhou_xu_2022]\] \[[Ye et al 2019][research_ye_ye_2019_b]\] \[[Bangert et al 1980][research_bangertlh_santmandm_1980]\] \[[Herrmann and Gülhan 2015][research_herrmann_gulhan_2015]\] \[[Ball and Ross 1972][research_ball_ross_1972]\] \[[McVey et al 1969][research_mcvey_rejeske_1969]\] \[[Leamer and Kennon 1978][research_leamerpc_kennonig_1978]\] \[[Flaherty and Stitt 1959][research_flahertyrj_stittle_1959]\] \[[Jones et al 1992][research_jones_myrabo_1992]\] \[[Hong-jun and Qing 2015][research_hongjun_qing_2015]\] \[[Hwang et al 1995][research_hwangkyuc_tiwarisurrendran_1995]\] \[[Wasserbauer et al 1996][research_wasserbauerjf_meleasonet_1996]\] \[[Simeonides et al 1994][research_simeonides_haase_1994]\] \[[Flock and Guelhan 2015][research_flock_guelhan_2015]\] \[[Flock and Gülhan 2015][research_flock_gulhan_2015]\] \[[Li et al 2023][research_li_sun_2023]\] \[[Babinsky 2014][research_babinsky_2014]\] \[[Kim et al 2011][research_kimhyoungjin_kumanotakayasu_2011]\] \[[Allen and Beke 1953][research_allenjl_bekeandrew_1953]\] \[[Berens and Bissinger 1998][research_berens_bissinger_1998]\] \[[White and Rhie 1992][research_white_rhie_1992]\] \[[Hsia 1993][research_hsia_1993]\] \[[Gallo et al 1966][research_gallo_gnos_1966]\] \[[Goldfeld and Nestoulia 2003][research_goldfeld_nestoulia_2003]\] \[[Gollan et al 2011][research_gollan_gollan_2011]\] \[[Goodwin and Maxwell 2017][research_goodwin_maxwell_2017]\] \[[Gopal and Wilson 2016][research_gopal_wilson_2016]\] \[[Hohn and Guelhan 2012][research_hohn_guelhan_2012]\] \[[Horing et al 2025][research_horing_maute_2025_b]\] \[[Hsia 1992][research_hsia_1992]\] \[[Hsia et al 1991][research_hsia_daso_1991]\] \[[Hemdan 1990][research_hemdan_1990]\] \[[Seebaugh 1973][research_seebaugh_1973]\] \[[Stroud and Miller 1966][research_stroud_miller_1966]\] \[[Inger 1990][research_inger_1990]\] \[[Reddy 2019][research_reddy_2019]\] \[[Zuo 2023][research_zuo_2023]\] \[[Jiao et al 2016][research_jiao_chang_2016_b]\] \[[Idris et al 2019][research_idris_saad_2019]\] \[[Pathak et al 2024][research_pathak_khare_2024]\] \[[Bissinger et al 1998][research_bissinger_blagoveshchensky_1998]\] \[[Povinelli 1996][research_povinellilouisa_1996]\] \[[Lawing and Johnson 1978][research_lawingpl_johnsoncb_1978]\] \[[Frey 2014][research_frey_2014]\] \[[Jules and Barnhart 1998][research_juleskenol_barnhartpaulj_1998]\] \[[Trexler 1975][research_trexlerca_1975]\] \[[Hawkins et al 1976][research_hawkinsje_kirklandfp_1976]\] \[[Kutschenreuter 1992][research_kutschenreuterpaul_1992]\] \[[Instrumentation for In-Flight Determination 1974][research_instrumentation_for_1974_b]\] \[[Holland and Perkins 1992][research_hollandscottd_perkinsjohnn_1992]\] \[[Latham et al 1972][research_lathamea_sorensonne_1972]\] \[[Investigation of Hypersonic Inlet Shock-wave Boundary Layer...][research_kutschenreuter_paulh_1966]\] \[[Martin 1977][research_martinaw_1977]\] \[[Gokul and Malaikannan 2025][research_g_g_2025]\] \[[Pagilla 2019][research_pagilla_2019]\] \[[Jacobsen et al 2006][research_jacobsen_tam_2006]\] \[[Jiao et al 2017][research_jiao_wang_2017]\] \[[Kanda et al 1989][research_kanda_komuro_1989]\] \[[Kanda et al 2003][research_kanda_hiraiwa_2003]\] \[[Kanda et al 2004][research_kanda_hiraiwa_2004]\] \[[Kumar 1981][research_kumar_1981]\] \[[Li et al 2022][research_li_yue_2022]\] \[[Libby et al 1963][research_libby_fox_1963]\] \[[Li et al 2014][research_li_hong_2014]\] \[[Libby et al 1963][research_libby_fox_1963_b]\] \[[Smart and Trexler 2003][research_smartmichaelk_trexlercarla_2003]\] \[[Henderson 1964][research_henderson_1964]\] \[[Maxwell and Goodwin 2017][research_maxwell_goodwin_2017]\] \[[Tabakoff and McDONEL 1966][research_tabakoff_mcdonel_1966]\] \[[Schneider and Reed 2003][research_schneider_reed_2003]\] \[[Medina et al 2021][research_medina_patel_2021]\] \[[Allard 2024][research_allard_2024]\] \[[Min et al 2026][research_min_son_2026]\] \[[Brahmachary and Ogawa 2021][research_brahmachary_ogawa_2021]\] \[[Nagamatsu 1989][research_nagamatsu_1989]\] \[[Nair et al 2003][research_nair_kumar_2003]\] \[[Inger 1995][research_inger_1995]\] \[[Ding et al 2015][research_ding_liu_2015]\] \[[Chung et al 1995][research_chung_kim_1995]\] \[[Vinogradov et al 1992][research_vinogradov_stepanov_1992]\] \[[Nurfathin Zahrolayali et al 2022][research_nurfathinzahrolayali_mohdrashdansaad_2022]\] \[[Lawrence 1991][research_lawrencescottl_1991]\] \[[Yan and Wang 2022][research_yan_wang_2022]\] \[[Varner et al 1987][research_varnermo_martindalewr_1987]\] \[[Yu et al 1988][research_yushengtao_hsiehkwangchung_1988]\] \[[Pan et al 2024][research_pan_wang_2024]\] \[[Korte et al 1993][research_kortejohnj_singhdj_1993]\] \[[O'Byrne et al 2011][research_obyrne_wittig_2011]\] \[[Oberg 2015][research_oberg_2015]\] \[[Hudgens and Trexler 1992][research_hudgensjuliea_trexlercarla_1992]\] \[[Ortwerth and Goldman 1996][research_ortwerth_goldman_1996]\] \[[Debarber 1999][research_debarber_1999]\] \[[Xiong et al 2019][research_xiong_fan_2019]\] \[[Chen et al 2020][research_chen_fan_2020]\] \[[Thomas et al 1988][research_thomasjl_rudydh_1988]\] \[[Luo et al 2022][research_luo_sun_2022]\] \[[Dryer and Beke 1952][research_dryermurray_bekeandrew_1952]\] \[[Sorensen and Smeltzer 1972][research_sorensen_smeltzer_1972]\] \[[Obery and Stitt 1958][research_oberylj_stittle_1958]\] \[[Trexler 1974][research_trexler_1974]\] \[[Phillips and Cruz 1991][research_phillips_cruz_1991]\] \[[Pollock and Wild 2021][research_pollock_wild_2021]\] \[[Pollock and Wild 2024][research_pollock_wild_2024]\] \[[Sorensen and Bencze 1973][research_sorensenne_benczedp_1973]\] \[[Azevedo et al 1990][research_azevedo_liu_1990]\] \[[Vander Schaaf et al 2025][research_vanderschaaf_acharya_2025]\] \[[Ferri and Nucci 1946][research_ferriantonio_nuccilouism_1946]\] \[[Ferri and Nucci 1951][research_ferriantonio_nuccilouism_1951]\] \[[Johnson III and Wu 1974][research_johnsoniii_wu_1974]\] \[[Amatucci et al 1982][research_amatucci_addy_1982]\] \[[Merkli 1975][research_merkli_1975]\] \[[Merkli 1976][research_merkli_1976]\] \[[Johnson and Wu 1975][research_johnson_wu_1975]\] \[[Pressure Recovery Performance of Straight-Channel...][research_runstadler_peterw_1969]\] \[[Zhang et al 2015][research_zhang_hong_2015]\] \[[Wilder 1949][research_wilder_jr_1949]\] \[[Liu et al 2024][research_liu_peng_2024]\] \[[Clauser 1954][research_clauser_1954]\] \[[Scribben and Withrow 2006][research_scribben_withrow_2006]\] \[[Ng et al 1986][research_ng_benson_1986]\] \[[Reddy et al 1989][research_reddy_smith_1989]\] \[[Zhang et al 2025][research_zhang_su_2025]\] \[[Meng et al 2024][research_meng_jin_2024]\] \[[Zhang et al 2023][research_zhang_li_2023]\] \[[Holland 1992][research_hollandscottd_1992]\] \[[Liu et al 2022][research_liu_chen_2022]\] \[[Di Giovanni and Stemmer 2019][research_digiovanni_stemmer_2019]\] \[[Lefieux et al 2021][research_lefieux_garnier_2021]\] \[[Rozario and Zouaoui 2007][research_rozario_zouaoui_2007]\] \[[Schuelein et al 2017][research_schuelein_schenk_2017]\] \[[Schulte-Roedding and Olivier 1998][research_schulteroedding_olivier_1998]\] \[[Scramjet Inlets 2001][research_scramjet_inlets_2001]\] \[[Shang and Chang 2007][research_shang_chang_2007]\] \[[Sheikin and Kuranov 2004][research_sheikin_kuranov_2004]\] \[[Sheikin and Kuranov 2005][research_sheikin_kuranov_2005]\] \[[Ruban et al 2020][research_ruban_menezes_2020]\] \[[Liu et al 1995][research_liu_sheng_1995]\] \[[Shukla and Verma 2020][research_shukla_verma_2020]\] \[[Penanhoat and Darracq 1996][research_penanhoat_darracq_1996]\] \[[Singh et al 1990][research_singh_tiwari_1990]\] \[[Bangert et al 1980][research_bangertlh_santmandm_1980_b]\] \[[Shulman et al 1966][research_shulman_parry_1966]\] \[[Kurtz et al 2016][research_kurtz_aizengendler_2016]\] \[[Sorensen and Latham 1975][research_sorensen_latham_1975]\] \[[Fraiser 1960][research_fraiser_1960]\] \[[Samimy et al 2011][research_samimy_webb_2011]\] \[[Cole and Richard 1991][research_colegaryl_richardjacquesc_1991]\] \[[Carlin et al 2003][research_carlincm_frischi_2003]\] \[[Harloff and Smith 1996][research_harloff_smith_1996]\] \[[Slater 2016][research_slaterjohnw_2016]\] \[[Park and Park 2022][research_park_park_2022]\] \[[Tam and Hagenmaier 1999][research_tam_hagenmaier_1999]\] \[[Tang et al 2015][research_tang_gao_2015]\] \[[Schwendemann and Sanders 1982][research_schwendemannmf_sandersbw_1982]\] \[[Hube 1968][research_hube_1968]\] \[[Kumar 1982][research_kumar_1982_b]\] \[[McRae and Neaves 1998][research_mcrae_neaves_1998]\] \[[Zhang et al 2025][research_zhang_pan_2025]\] \[[Gelder 1957][research_gelderthomasf_1957]\] \[[Ng et al 1989][research_ng_ajmani_1989]\] \[[Kumar 1982][research_kumar_1982]\] \[[Liu et al 2018][research_liu_yan_2018]\] \[[Rodi et al 1996][research_rodi_emami_1996]\] \[[van Keuk et al 1998][research_vankeuk_ballmann_1998]\] \[[Van Wie 1992][research_vanwie_1992]\] \[[Teng and Yuan 2015][research_teng_yuan_2015]\] \[[Baydar et al 2017][research_baydarezgihan_lufrankk_2017]\] \[[Baydar et al 2016][research_baydarezgihan_lufrankk_2016]\] \[[Pike 1996][research_pike_1996_b]\] \[[Wang and Guo 2013][research_wang_guo_2013]\] \[[Weissman 1990][research_weissman_1990]\] \[[White 1993][research_white_1993]\] \[[Xiao et al 2006][research_xiao_liu_2006]\] \[[Xiao et al 2008][research_xiao_yue_2008]\] \[[Xiao et al 2012][research_xiao_yue_2012]\] \[[Zhang 2015][research_zhang_2015]\] \[[Zhang 2020][research_zhang_2020_c]\] \[[Zhang 2020][research_zhang_2020_b]\] \[[Zhang 2020][research_zhang_2020_d]\] \[[Zhang et al 2026][research_zhang_zhou_2026]\]

### Hypersonic aerodynamics, boundary layers and configurations

**The external flow over the vehicle.** Hypersonic aerodynamics, viscous interaction and the turbulent boundary layer, shock interactions, waveriders and the configurations proposed for air-breathing vehicles.

**228 records.** \[[1985, Prediction and Verification of Aerodynamic Drag, Part I Prediction][research_prediction_and_1985]\] \[[98/03244 Thermodynamics analysis of inverse cycle engine for...][research_98_03244_thermodynamics_1998]\] \[[Gao 2023][research_gao_2023]\] \[[Flight Sciences Lab Inc Buffalo Ny 1964][research_flightscienceslabincbuffalony_1964]\] \[[Fuchs 2019][research_aaronwfuchs_2019]\] \[[Accelerating Hypersonic Innovation][research_accelerating_hypersonic_2022]\] \[[Lantz 1992][research_lantz_1992]\] \[[Adams et al 1973][research_adams_johnc_1973]\] \[[Advisory Group for Aerospace Research and Development 1997][research_advisorygroupforaerospaceresearchanddevelopment_1997]\] \[[Zhu et al 2021][research_zhu_shi_2021]\] \[[Levensteins and Krumins 1967][research_levensteins_krumins_1967]\] \[[Rodkiewicz and Chattopadhyay 1971][research_rodkiewicz_chattopadhyay_1971]\] \[[Clark 1969][research_clark_1969]\] \[[Pezzella and Viviani 2016][research_pezzella_viviani_2016]\] \[[Eyi et al 2019][research_eyi_hanquist_2019]\] \[[Horing et al 2025][research_horing_maute_2025]\] \[[Air Force Test Pilot School Edwards Afb Ca 1987][research_airforcetestpilotschooledwardsafbca_1987]\] \[[Airbreathing Hypersonic Aircraft and 1997][research_airbreathing_hypersonic_1997]\] \[[Jones and Huber 1978][research_jonesra_huberpw_1978]\] \[[Jayaraman and Lewis 1997][research_jayaraman_lewis_1997]\] \[[Anderson 1987][research_anderson_1987]\] \[[Andrews and Mackley 1993][research_andrews_mackley_1993]\] \[[Andrews and Mackley 1994][research_andrews_mackley_1994]\] \[[Lewis and Hastings 1989][research_lewis_hastings_1989]\] \[[Arrington and Woods 1972][research_arrington_woods_1972]\] \[[Auslender et al 2009][research_auslender_suder_2009]\] \[[Baron and Efrat 1979][research_baron_efrat_1979]\] \[[Lusty and Miele 1966][research_lusty_miele_1966]\] \[[Boeing Scientific Research Labs Seattle Wa 1963][research_boeingscientificresearchlabsseattlewa_1963]\] \[[Bogdonoff 1970][research_bogdonoff_1970]\] \[[Bogdonoff 1999][research_bogdonoff_1999]\] \[[Bolender and Doman 2005][research_bolender_doman_2005]\] \[[Bowcutt 2001][research_bowcutt_2001]\] \[[Boyd 2008][research_boyd_2008]\] \[[Bruno 2023][research_bruno_2023_c]\] \[[Bruno 2023][research_bruno_2023_d]\] \[[Bruno 2023][research_bruno_2023]\] \[[Calloway 1983][research_calloway_1983]\] \[[Campbell and Gerstenmaier 2014][research_campbell_gerstenmaier_2014]\] \[[Anderson and Eckbreth 1991][research_anderson_eckbreth_1991]\] \[[Cikanek et al 2007][research_cikanek_bartolotta_2007]\] \[[Colladay 1987][research_colladay_1987]\] \[[Matarrese et al 1991][research_matarrese_messiter_1991]\] \[[Couture et al 2008][research_couture_dechamplain_2008]\] \[[Creating Hypersonic Flow in 2019][research_creating_hypersonic_2019]\] \[[Cresci 1966][research_cresci_1966]\] \[[Jiang et al 2021][research_jiang_zhang_2021]\] \[[Batterton et al 1976][research_battertonpg_arpasidj_1976]\] \[[Pegg et al 1993][research_peggrobertj_huntjamesl_1993]\] \[[O'Neill and Lewis 1992][research_oneillmarykael_lewismarkj_1992]\] \[[Zaludin 2025][research_zaludin_2025]\] \[[Brown and Donbar 2013][research_brown_donbar_2013]\] \[[Brown and Donbar 2015][research_brown_donbar_2015]\] \[[Dickeson et al 2009][research_dickeson_rodriguez_2009]\] \[[Dietrick 2013][research_dietrick_2013]\] \[[Burgers 2017][research_burgers_2017]\] \[[Flandro et al 1992][research_flandroga_roachrl_1992]\] \[[El-Kebir and Ornik 2020][research_elkebir_ornik_2020]\] \[[Chu 1967][research_chu_1967]\] \[[Cox et al 1966][research_cox_crabtree_1966]\] \[[Curran and Beach 1988][research_curranet_beachhljr_1988]\] \[[Goradia et al 1991][research_goradiasuresh_torresabelo_1991]\] \[[Espinosa 2003][research_espinosa_2003]\] \[[Scala 1958][research_scala_1958]\] \[[Evans et al 2011][research_evans_zok_2011]\] \[[Vert and Bouchard 2024][research_vert_bouchard_2024]\] \[[White and Ault 1996][research_white_ault_1996]\] \[[Hastings et al 1957][research_hastings_persh_1957]\] \[[Cappuccio 1999][research_cappucciogelsomina_1999]\] \[[Holden et al 2001][research_holden_wadhams_2001]\] \[[Falempin and Serre 2006][research_falempin_serre_2006]\] \[[Feie and Kretz 2008][research_feie_kretz_2008]\] \[[Ferlemann et al 2000][research_ferlemann_robinson_2000]\] \[[Johnston et al 1987][research_johnstonpatrickj_whiteheadallenhjr_1987]\] \[[Foreman 1963][research_foreman_1963]\] \[[Forsythe et al 1961][research_forsythe_melfi_1961]\] \[[Froning and Roach 2003][research_froning_roach_2003]\] \[[Froning and Roach 1999][research_froningjr_roach_1999]\] \[[Fuels for Hypersonic Air-Breathing 2022][research_fuels_for_2022]\] \[[Glass and Glass 2002][research_glass_glass_2002]\] \[[Gregorek and Reuss 1990][research_gregorek_reuss_1990]\] \[[Griffith et al 1983][research_griffith_maus_1983]\] \[[Grunlan et al 2010][research_grunlan_rajagopal_2010]\] \[[Guizzo 2004][research_guizzo_2004]\] \[[Hao et al 2014][research_hao_chang_2014]\] \[[Heitmeier and Bissinger 1995][research_heitmeier_bissinger_1995]\] \[[Heitmeir et al 1992][research_heitmeir_lederer_1992]\] \[[Harloff 1988][research_harloff_1988]\] \[[Smits 2007][research_smits_2007]\] \[[Smits 2009][research_smits_2009]\] \[[Dewey 1961][research_dewey_1961]\] \[[Hunt and Rausch 1998][research_hunt_rausch_1998]\] \[[Allen 1962][research_hjulianallen_1962]\] \[[Cunningham 1987][research_cunningham_1987]\] \[[Agnone and Prakasam 1987][research_agnone_prakasam_1987]\] \[[Swithenbank 1967][research_swithenbank_1967]\] \[[Townend 1995][research_townend_1995]\] \[[Weidner 1992][research_weidnerjohnp_1992]\] \[[Thompson and Hull 1970][research_thompson_hull_1970]\] \[[Zuo 2023][research_zuo_2023_b]\] \[[Hypersonic flight 2015][research_hypersonic_flight_2015]\] \[[Allen 1957][research_allen_1957]\] \[[Hayes et al 1960][research_hayes_probstein_1960]\] \[[Cheng 1989][research_cheng_1989]\] \[[Guy 1990][research_rwayneguy_1990]\] \[[Janiszewski and Woźniak 2022][research_janiszewski_wozniak_2022]\] \[[Chung and Lu 1995][research_chung_lu_1995]\] \[[Hypersonic Viscous Interactions 2006][research_hypersonic_viscous_2006]\] \[[Gupta et al 1990][research_gupta_lee_1990]\] \[[Lee et al 1990][research_lee_gupta_1990]\] \[[Chen et al 2009][research_chen_starkey_2009]\] \[[Ramunno et al 2022][research_ramunno_boyd_2022]\] \[[Johnston et al 1978][research_johnston_pittman_1978_b]\] \[[Introduction to Hypersonic Air-Breathing 2022][research_introduction_to_2022]\] \[[Marsh and Sears 1954][research_marsh_sears_1954]\] \[[Bowersox and Fan 2000][research_bowersox_fan_2000]\] \[[Jackson and Wang 1974][research_jackson_wang_1974]\] \[[Jenkins 2000][research_jenkins_2000]\] \[[Jiang and Yu 2019][research_jiang_yu_2019]\] \[[Jing et al 2007][research_jing_shuo_2007]\] \[[Kaufman and Louis G. 1963][research_kaufman_louisg_1963]\] \[[Kaul 1991][research_kaul_1991]\] \[[Kazmar 2002][research_kazmar_2002]\] \[[Kazmar 2005][research_kazmar_2005]\] \[[Keshmiri et al 2006][research_keshmiri_colgren_2006]\] \[[Khambaswadkar 2024][research_khambaswadkar_2024]\] \[[Kim et al 1982][research_kim_rasmussen_1982]\] \[[Kopp et al 1999][research_kopp_hollmeier_1999]\] \[[Koschel 1996][research_koschel_1996]\] \[[Kremeyer and Pakhomov 2008][research_kremeyer_pakhomov_2008]\] \[[Ladyzhenskij 1963][research_ladyzhenskij_1963]\] \[[Lees and Kubota 1972][research_lees_kubota_1972]\] \[[Levermore and Brio 1994][research_levermore_brio_1994]\] \[[Zubin et al 1997][research_zubin_ostapenko_1997]\] \[[Pfaff 1968][research_pfaff_1968]\] \[[Liu et al 2019][research_liu_dong_2019]\] \[[Lockwood et al 1996][research_lockwood_petley_1996]\] \[[Krouse and Ellis 1966][research_krouse_ellis_1966]\] \[[Adams 1975][research_adams_1975]\] \[[Lukasiewicz 1961][research_lukasiewicz_1961]\] \[[Goldberg and Scala 1965][research_goldberg_scala_1965]\] \[[Wright 1993][research_wrightgeorgefjr_1993]\] \[[McClinton et al 2002][research_mcclinton_ferlemann_2002]\] \[[McGilvray et al 2019][research_mcgilvray_neely_2019]\] \[[Meuwly 2014][research_meuwly_2014]\] \[[Miele and Hull 1963][research_miele_hull_1963]\] \[[Miele and Pritchard 1963][research_miele_pritchard_1963]\] \[[Mogavero and Brown 2018][research_mogavero_brown_2018]\] \[[Molvik et al 1993][research_molvik_bowles_1993_b]\] \[[Molvik et al 1993][research_molvik_bowles_1993]\] \[[Stewart et al 2002][research_stewartmem_suresha_2002]\] \[[Nagel and Becker 1973][research_nagel_becker_1973]\] \[[Nance 2013][research_nance_2013]\] \[[Hunt and Eiswirth 1996][research_huntjamesl_eiswirthedwarda_1996]\] \[[Marshall et al 2014][research_marshall_cox_2014]\] \[[Sforza 2026][research_sforza_2026]\] \[[Novelli and Koschel 2001][research_novelli_koschel_2001]\] \[[O'Neill and Lewis 1992][research_oneill_lewis_1992]\] \[[O'Neill and Lewis 1993][research_oneill_lewis_1993]\] \[[Owen and Horstman 1972][research_owenfk_horstmancc_1972]\] \[[Adams and Probstein 1958][research_adams_probstein_1958]\] \[[Optimal Aerodynamic Shapes Of 1996][research_optimal_aerodynamic_1996]\] \[[Zheng et al 2023][research_zheng_wu_2023]\] \[[Hao et al 2025][research_hao_yu_2025]\] \[[Palmer 2021][research_palmer_2021]\] \[[Parker 2022][research_parker_2022]\] \[[Sahbon et al 2023][research_sahbon_jacewicz_2023]\] \[[Pisano and Whitfield 2024][research_pisano_whitfield_2024]\] \[[Preller 2018][research_preller_2018]\] \[[Preller and Smart 2012][research_preller_smart_2012]\] \[[Sastry 1963][research_sastry_1963]\] \[[Ormsbee 1962][research_ormsbee_1962]\] \[[Monaghan 1959][research_monaghan_1959]\] \[[Rizzi et al 2026][research_rizzi_parish_2026]\] \[[Blankson and Hagseth 1993][research_blanksonisaiahm_hagsethpaul_1993]\] \[[Smarslok 2015][research_smarslok_2015]\] \[[Walker 1952][research_walker_1952]\] \[[Curran and Swithenbank 1966][research_curran_swithenbank_1966]\] \[[Lees 1957][research_lees_1957]\] \[[Reed 1997][research_reed_1997]\] \[[Zhao et al 2025][research_zhao_ma_2025]\] \[[Reshotko 1987][research_reshotko_1987]\] \[[Bandyopadhyay and Gad-el-Hak 1994][research_bandyopadhyay_gadelhak_1994]\] \[[Neuwerth et al 1999][research_neuwerth_peiter_1999]\] \[[Bushnell et al 1993][research_bushnelldennism_yiplongp_1993]\] \[[Rickman 2010][research_rickman_2010]\] \[[Rodi 2012][research_rodi_2012]\] \[[Rodriguez et al 2009][research_rodriguez_dickeson_2009]\] \[[Rudiments and Methodology for 2001][research_rudiments_and_2001]\] \[[Russian Aerospace Literature This month Hypersonic...][research_russian_aerospace_1996]\] \[[Sakata 1992][research_sakata_1992]\] \[[Weidner et al 1976][research_weidnerjp_smallwj_1976]\] \[[Scramjet Investigations Within the 2001][research_scramjet_investigations_2001]\] \[[Yao et al 2025][research_yao_wu_2025]\] \[[Zhikharev 1993][research_zhikharev_1993]\] \[[Sharenson 1966][research_sharenson_1966]\] \[[Shvets et al 2005][research_shvets_voronin_2005]\] \[[Bruno and Ingenito 2021][research_bruno_ingenito_2021]\] \[[Compton et al 1983][research_comptonhr_schiessjr_1983]\] \[[Batdor 1957][research_batdor_1957]\] \[[Johnston et al 1971][research_johnston_cubbage_1971]\] \[[Edwards et al 1975][research_edwardsclw_smallwj_1975]\] \[[Hartill et al 1978][research_hartillwr_goebeltp_1978]\] \[[Trujillo 1970][research_trujillo_1970]\] \[[Davis et al 1970][research_davisgw_plankpp_1970]\] \[[Torres 1992][research_torresabelo_1992]\] \[[Tarpley and Lewis 1995][research_tarpley_lewis_1995]\] \[[Tumuklu and Hanquist 2023][research_tumuklu_hanquist_2023]\] \[[The Free Flight Range 1962][research_the_free_1962]\] \[[The Quest For Hypersonic 2011][research_the_quest_2011]\] \[[Brasseur 1994][research_brasseur_1994]\] \[[Curran and Craig 1973][research_curran_craig_1973]\] \[[Torrez et al 2009][research_torrez_driscoll_2009]\] \[[Tournes 2013][research_tournes_2013]\] \[[de Moura and Ribeiro 2026][research_demoura_ribeiro_2026]\] \[[Van 1963][research_van_1963]\] \[[Wei et al 2015][research_wei_tian_2015]\] \[[Varner 1976][research_varner_1976]\] \[[Cockrell 1994][research_cockrellcharlesedwardjr_1994]\] \[[Walchner 1974][research_walchner_1974]\] \[[Ward and Hewitt 1988][research_ward_hewitt_1988]\] \[[Dukes 1962][research_wilfredhdukes_1962]\] \[[Williams and Lewis 1975][research_williams_lewis_1975]\] \[[Wu et al 2015][research_wu_jiang_2015]\] \[[Xiaoqing et al 2010][research_xiaoqing_zhongxi_2010]\] \[[Yankui et al 2005][research_yankui_dongjun_2005]\] \[[Zarlingo 1988][research_zarlingo_1988]\] \[[Zhou et al 2023][research_zhou_xia_2023]\]

### Scramjet flight experiments since the X-30

**The vehicles that flew scramjets or hypersonic experiments after the X-30.** The X-43A and Hyper-X, HyShot, HIFiRE, the CIAM and NASA flight tests and the free-flight techniques that put an engine in flight.

**82 of these titles name the X-43A or Hyper-X, 39 name HyShot and 44 name HIFiRE.** The X-51A is far less visible, as Thin Subjects records.

**221 records.** \[[Ren et al 2022][research_ren_wang_2022]\] \[[Adamczak and Bolender 2015][research_adamczak_bolender_2015]\] \[[Zhao et al 2022][research_zhao_shao_2022]\] \[[Watanabe et al 1997][research_watanabe_ishimoto_1997]\] \[[Tanno and Tanno 2021][research_tanno_tanno_2021]\] \[[Fujii and Inoue 1998][research_fujii_inoue_1998]\] \[[Amundsen et al 2004][research_amundsen_leonard_2004]\] \[[Ratnayake 2010][research_ratnayakenalina_2010]\] \[[Arjun 2010][research_arjun_2010]\] \[[Marek 2011][research_mareklindsayc_2011]\] \[[Bahm et al 2005][research_bahm_baumann_2005]\] \[[Baumann 2006][research_baumann_2006]\] \[[Baumann 2007][research_baumann_2007]\] \[[Baumann et al 2008][research_baumann_pahle_2008]\] \[[Baumann et al 2008][research_baumann_bahm_2008]\] \[[Bermudez and Gladden 2003][research_bermudez_gladden_2003]\] \[[Berry et al 2000][research_berry_auslender_2000]\] \[[Berry et al 2008][research_berry_daryabeigi_2008]\] \[[Boeing to use X-43A 2005][research_boeing_to_2005]\] \[[Spanos 2009][research_spanostheodorosa_2009]\] \[[Boyce and Paull 2001][research_boyce_paull_2001]\] \[[Boyce et al 2003][research_boyce_gerard_2003]\] \[[Wheaton et al][research_bradleymwheaton_ivettaleyva]\] \[[Buning et al 2000][research_buning_wong_2000]\] \[[Burrows et al 2024][research_burrows_rana_2024]\] \[[McClinton et al 2001][research_crmcclinton_vlrausch_2001]\] \[[Cain and Walton 2003][research_cain_walton_2003]\] \[[Chowdhary et al 2022][research_chowdhary_hoang_2022]\] \[[Cavolowsky and Newfield 1992][research_cavolowsky_newfield_1992]\] \[[Paredes and Theofilis 2015][research_paredes_theofilis_2015]\] \[[Chan et al 2018][research_chan_razzaqi_2018]\] \[[Chen and Zhao 2017][research_chen_zhao_2017]\] \[[Choi and Driscoll 2024][research_choi_driscoll_2024]\] \[[Cockrell et al 2000][research_cockrell_engelund_2000]\] \[[Sellers 1965][research_sellers_1965]\] \[[Seleznev 2021][research_seleznev_2021]\] \[[Edquist 2006][research_edquistkarlt_2006]\] \[[Constantine et al 2011][research_constantine_wang_2011]\] \[[Cheah et al 2025][research_cheah_bhattacharjee_2025]\] \[[Corpening 2004][research_corpening_2004]\] \[[Jewell et al 2017][research_jewell_miller_2017]\] \[[Crow et al 2012][research_crow_boyd_2012]\] \[[Cuda and Hass 2010][research_cuda_hass_2010]\] \[[Davidson et al 1999][research_davidson_lallman_1999]\] \[[Davis 1995][research_davis_1995]\] \[[Davis 2007][research_davis_2007]\] \[[Davis and White 2006][research_davis_white_2006]\] \[[Davis and White 2008][research_davis_white_2008]\] \[[Davis et al 2006][research_davis_sim_2006]\] \[[Doherty 2022][research_doherty_2022]\] \[[Dolvin 2009][research_dolvin_2009]\] \[[Ellsworth 2010][research_ellsworth_2010]\] \[[Emory et al 2011][research_emory_terrapon_2011]\] \[[Engelund 2001][research_engelund_2001]\] \[[Engelund and Neal 2013][research_engelund_neal_2013]\] \[[Engelund et al 2000][research_engelund_holland_2000]\] \[[Eshtairy et al 2025][research_eshtairy_millot_2025]\] \[[Parikh et al 2004][research_parikhparesh_engelundwalter_2004]\] \[[Falempin et al 1992][research_falempin_forrat_1992]\] \[[Falempin et al 1995][research_falempin_thevenot_1995]\] \[[Ferlemann 2005][research_ferlemann_2005]\] \[[Ferlemann et al 2005][research_ferlemann_mcclinton_2005]\] \[[Berry et al 2016][research_berryscotta_bergerkarent_2016]\] \[[Foelsche et al 2006][research_foelsche_beckel_2006]\] \[[Ferlemann 2008][research_ferlemannpaulg_2008]\] \[[Fratini et al 2025][research_fratini_dellaposta_2025]\] \[[Sheetz 1965][research_sheetznwjr_1965]\] \[[Freeman et al 1997][research_freeman_reubush_1997]\] \[[Frost 2020][research_frost_2020]\] \[[Furudate et al 2005][research_furudate_lee_2005]\] \[[Gardner 2024][research_gardner_2024]\] \[[Gardner et al 2004][research_gardner_steelant_2004]\] \[[Geraci et al 2019][research_geraci_menhorn_2019]\] \[[Gibson et al 2002][research_gibson_neidhoefer_2002]\] \[[Gibson et al 2003][research_gibson_cancienne_2003]\] \[[Glaessgen et al 2005][research_glaessgen_dawicke_2005]\] \[[Glass et al 2013][research_glass_capriotti_2013]\] \[[Glass et al 2014][research_glass_capriotti_2014]\] \[[Gong 2005][research_gong_2005]\] \[[Grindle 2011][research_grindle_2011]\] \[[Grindle 2012][research_grindle_2012]\] \[[Grindle and Bahm 2006][research_grindle_bahm_2006]\] \[[Kimmel et al 2011][research_kimmel_adamczak_2011]\] \[[Hank et al 2008][research_hank_murphy_2008]\] \[[Hass et al 2005][research_hass_smart_2005]\] \[[Gai et al 1992][research_gaisl_mudfordnr_1992]\] \[[Hegedus and Mendenhall 2003][research_hegedus_mendenhall_2003]\] \[[Hass et al 2010][research_hassneale_cabellkarenf_2010]\] \[[Cabell et al 2011][research_cabellkaren_hassneal_2011]\] \[[Kimmel et al 2015][research_kimmel_borg_2015]\] \[[Juliano et al 2015][research_juliano_adamczak_2015]\] \[[Holland et al 2000][research_holland_woods_2000]\] \[[Holland et al 2001][research_holland_woods_2001]\] \[[Howard 2024][research_howard_2024]\] \[[Huebner et al 2000][research_huebner_rock_2000]\] \[[Huebner et al 2001][research_huebner_rock_2001]\] \[[Hyper-X Model Testing with 1996][research_hyper_x_model_1996]\] \[[Hypersonic Air-Breathing Flight Testing 2022][research_hypersonic_air_breathing_2022]\] \[[West and Bynum 2024][research_west_bynum_2024]\] \[[Iaccarino et al 2010][research_iaccarino_pecnik_2010]\] \[[Berry et al 2008][research_berryscotta_horvaththomasjjr_2008]\] \[[Ingenito et al 2010][research_ingenito_bruno_2010]\] \[[Ishimoto et al 1996][research_ishimoto_takizawa_1996]\] \[[Jackson et al 2011][research_jackson_gruber_2011]\] \[[Lux-Baumann and Burkes 2005][research_jessicaluxbaumann_darrylaburkes_2005]\] \[[Jones 2006][research_jones_2006]\] \[[Jorris 2014][research_jorris_2014]\] \[[Joyce et al 2005][research_joyce_pomroy_2005]\] \[[Kardas 2023][research_kardas_2023]\] \[[Karl et al 2006][research_karl_hannemann_2006]\] \[[Karl et al 2008][research_karl_hannemann_2008]\] \[[Karl et al 2012][research_karl_laurence_2012]\] \[[Karlgaard et al 2004][research_karlgaard_tartabini_2004]\] \[[Karlgaard et al 2005][research_karlgaard_martin_2005]\] \[[Kimmel 2008][research_kimmel_2008]\] \[[Kimmel 2008][research_kimmel_2008_b]\] \[[Kimmel et al 2014][research_kimmel_adamczak_2014]\] \[[Kindler et al 2008][research_kindler_blacha_2008]\] \[[Ko and Gong 2000][research_ko_gong_2000]\] \[[Ko and Gong 2001][research_ko_gong_2001]\] \[[Kodera et al 2005][research_kodera_sunami_2005]\] \[[Kurtz et al 2015][research_kurtz_aizengendler_2015]\] \[[Labbe et al 2009][research_labbe_gilbert_2009]\] \[[Lacaze et al 2017][research_lacaze_vane_2017]\] \[[Ladeinde 2019][research_ladeinde_2019]\] \[[Lam and Stollenwerk 1966][research_lam_stollenwerk_1966]\] \[[Larsson 2012][research_larsson_2012]\] \[[Laurence et al 2015][research_laurence_karl_2015]\] \[[Leonard et al 2005][research_leonard_amundsen_2005]\] \[[Li and Wey 1988][research_li_wey_1988]\] \[[Lin et al 2008][research_lin_baumann_2008]\] \[[Lux-Baumann and Burkes 2006][research_luxbaumann_burkes_2006]\] \[[Lux-Baumann et al 2006][research_luxbaumann_dees_2006]\] \[[Jackson et al 2015][research_jackson_gruber_2015]\] \[[Mack et al 2009][research_mack_steelant_2009]\] \[[Marie et al 2019][research_marie_hideyuki_2019]\] \[[Marshall et al 2005][research_marshall_corpening_2005]\] \[[Marshall et al 2005][research_marshall_bahm_2005]\] \[[Martinez Schramm et al 2008][research_martinezschramm_karl_2008]\] \[[McClinton et al 1991][research_mcclinton_rondakov_1991]\] \[[McClinton et al 1998][research_mcclinton_holland_1998]\] \[[McClinton et al 1998][research_mcclinton_voland_1998]\] \[[Choudhari et al 2021][research_meelanchoudhari_feili_2021]\] \[[Mehta and Kutler 1994][research_mehta_kutler_1994]\] \[[Morelli 2008][research_morelli_2008]\] \[[Morelli et al 2005][research_morelli_derry_2005]\] \[[Moses 2003][research_moses_2003]\] \[[Moses 2003][research_moses_2003_b]\] \[[Rieken et al 2020][research_elizabethfrieken_scottaberry_2020]\] \[[Navó and Bergada 2020][research_navo_bergada_2020]\] \[[Neuenhahn et al 2006][research_neuenhahn_olivier_2006]\] \[[Takahashi et al 2021][research_takahashi_tomioka_2021]\] \[[Ohlhorst et al 2005][research_ohlhorst_glass_2005]\] \[[Pak 2008][research_pak_2008]\] \[[Tufts et al 2018][research_tufts_gosse_2018]\] \[[Paull et al 2000][research_paull_frost_2000]\] \[[Paull et al 2005][research_paull_alesi_2005]\] \[[Peebles 2008][research_peebles_2008]\] \[[Peebles 2009][research_peebles_2009]\] \[[Peebles 2007][research_peeblescurtis_2007_b]\] \[[Pellett et al 2008][research_pellett_vaden_2008]\] \[[Pellett et al 2009][research_pellett_dawson_2009]\] \[[Perry 2026][research_perry_2026]\] \[[Engelund et al 1999][research_engelundwalterc_hollandscottd_1999]\] \[[Purifoy and Neal 2017][research_purifoy_neal_2017]\] \[[Rana et al 2009][research_rana_thornber_2009]\] \[[Rana et al 2011][research_rana_thornber_2011]\] \[[Rausch et al 1997][research_rausch_mcclinton_1997]\] \[[Rausch et al 2000][research_rausch_mcclinton_2000]\] \[[Roudakov et al 1998][research_roudakovalexanders_semenovvyacheslavl_1998]\] \[[Berry et al 2011][research_berryscotta_kimmelroger_2011]\] \[[Redifer et al 2007][research_redifer_lin_2007]\] \[[Reubush 1999][research_reubush_1999]\] \[[Reubush et al 2004][research_reubush_nguyen_2004]\] \[[Robinson and Martin 2006][research_robinson_martin_2006]\] \[[Rogers et al 2005][research_rogers_shih_2005]\] \[[Roudakov et al 1996][research_roudakov_semenov_1996]\] \[[Saghafian et al 2015][research_saghafian_shunn_2015]\] \[[Sappey et al 2009][research_sappey_sutherland_2009]\] \[[Seleznev 2022][research_seleznev_2022]\] \[[Shimada et al 1999][research_shimada_yamamoto_1999]\] \[[Silvestrov and Surzhikov 2020][research_silvestrov_surzhikov_2020]\] \[[Smart and Suraweera 2009][research_smart_suraweera_2009]\] \[[Smart et al 2006][research_smart_hass_2006]\] \[[Smith et al 2002][research_smith_schetz_2002]\] \[[Smith et al 2002][research_smith_walker_2002]\] \[[Spravka and Jorris 2015][research_spravka_jorris_2015]\] \[[Storch et al 2011][research_storch_bynum_2011]\] \[[Sunami et al 2006][research_sunami_itoh_2006]\] \[[Peebles 2007][research_peeblescurtis_2007]\] \[[Tirtey and Boyce 2009][research_tirtey_boyce_2009]\] \[[Xing-hao et al 2021][research_xinghao_haijie_2021]\] \[[Georgiadis et al 2014][research_georgiadisnicholasj_mankbadiminar_2014]\] \[[Turner 1965][research_turner_1965]\] \[[Turner et al 2006][research_turner_hoerschgen_2006]\] \[[Tyll et al 2000][research_tyll_bakos_2000]\] \[[Nordin-Bates et al 2017][research_nordinbates_fureby_2017]\] \[[Vachon et al 2005][research_vachon_grindle_2005]\] \[[Vaden et al 2009][research_vaden_debes_2009]\] \[[Voland et al 1998][research_voland_rock_1998]\] \[[Voland et al 1999][research_voland_auslender_1999]\] \[[Voland et al 2005][research_voland_huebner_2005]\] \[[Voland et al 2006][research_voland_huebner_2006]\] \[[Wadhams et al 2008][research_wadhams_maclean_2008]\] \[[Watanabe et al 1996][research_watanabe_ishimoto_1996]\] \[[Wen et al 2011][research_wen_chen_2011]\] \[[West and Bynum 2021][research_west_bynum_2021]\] \[[Williamson 1992][research_williamson_1992]\] \[[Wilson Chan et al 2014][research_wilsonchan_razzaqi_2014]\] \[[Wittliff et al 1992][research_wittliff_oconnor_1992]\] \[[Won et al 2006][research_won_jeung_2006]\] \[[Won et al 2007][research_won_jeung_2007]\] \[[Woods et al 2000][research_woods_holland_2000]\] \[[X-43A Research Vehicle Design 2011][research_x_43a_research_2011]\] \[[Xing et al 2012][research_xing_zhang_2012]\] \[[Xing et al 2017][research_xing_cai_2017]\] \[[Yentsch and Gaitonde 2012][research_yentsch_gaitonde_2012]\] \[[Yentsch and Gaitonde 2013][research_yentsch_gaitonde_2013]\] \[[Yentsch and Gaitonde 2013][research_yentsch_gaitonde_2013_b]\] \[[Cenkci 1991][research_cenkci_1991]\] \[[Zheng et al 2020][research_zheng_yan_2020]\]

### Active, regenerative and transpiration cooling

**Using the fuel, or something else, to carry the heat away.** Regenerative cooling with hydrogen and with endothermic hydrocarbon fuels, transpiration and film cooling, heat pipes, and the thermal management cycles built on the fuel's heat sink.

**140 of these 173 records date from 2015 or later**, so the cooled-structure problem the X-30 posed is mainly a literature of the last decade.

**173 records.** \[[Skamniotis and Cocks 2021][research_skamniotis_cocks_2021]\] \[[Kamath et al 1990][research_kamathpradeeps_bakernr_1990]\] \[[Jin et al 2024][research_jin_zhao_2024]\] \[[Wang et al 2020][research_wang_yang_2020]\] \[[Al-Garni et al 1996][research_algarni_sahin_1996]\] \[[Nowak and Kelly 1976][research_nowakrj_kellyhn_1976]\] \[[Herman and Melnik 1962][research_herman_melnik_1962]\] \[[Aleemuddin et al 2026][research_aleemuddin_hossain_2026]\] \[[Lei et al 2023][research_lei_zhang_2023]\] \[[Sreekireddy et al 2019][research_sreekireddy_reddy_2019]\] \[[Gao et al 2020][research_gao_zhang_2020_c]\] \[[Li et al 2018][research_li_liu_2018]\] \[[Anthony et al 1975][research_anthony_dukes_1975]\] \[[Diao et al 2025][research_diao_liu_2025]\] \[[Wang et al 2026][research_wang_du_2026]\] \[[Camarda and Masek 1979][research_camarda_masek_1979]\] \[[Cao et al 2026][research_cao_zhou_2026]\] \[[Sahu et al 2022][research_sahu_tropina_2022]\] \[[Colwell 2023][research_colwell_2023]\] \[[Li et al 2024][research_li_wang_2024]\] \[[Zhou et al 2025][research_zhou_zhang_2025]\] \[[Ma et al 2019][research_ma_chang_2019]\] \[[Zhang et al 2025][research_zhang_xie_2025]\] \[[Wang et al 2022][research_wang_jin_2022]\] \[[Youn and Mills 1995][research_youn_mills_1995]\] \[[Hu et al 2026][research_hu_li_2026]\] \[[Bejan 2013][research_bejan_2013]\] \[[Daly 2025][research_daly_2025]\] \[[Smith 1978][research_smithlm_1978]\] \[[Qiao et al 2024][research_qiao_liu_2024]\] \[[Qiao et al 2023][research_qiao_liu_2023]\] \[[Zhang et al 2022][research_zhang_zhang_2022]\] \[[Hanquist et al 2017][research_hanquist_hara_2017]\] \[[Kerth et al 2024][research_kerth_lepage_2024]\] \[[Dunavant and Mulligan 1969][research_dunavant_mulligan_1969]\] \[[Xu et al 2024][research_xu_lin_2024]\] \[[Yin et al 2022][research_yin_e_2022]\] \[[Tian et al 2023][research_tian_yang_2023]\] \[[Kanda et al 1994][research_kanda_masuya_1994]\] \[[Li et al 2021][research_li_wang_2021]\] \[[Anderson and Brooks 1960][research_anderson_brooks_1960]\] \[[Luo et al 2021][research_luo_miao_2021]\] \[[Sun et al 2019][research_sun_li_2019]\] \[[Tsujikawa 1996][research_tsujikawa_1996]\] \[[Nakaya et al 2015][research_nakaya_tsue_2015]\] \[[Wang et al 2023][research_wang_liu_2023]\] \[[dos Santos et al 2025][research_dossantos_passaro_2025]\] \[[Xu et al 2021][research_xu_lin_2021]\] \[[Helenbrook et al 1971][research_helenbrookrg_mcconartywa_1971]\] \[[Li and Wang 2017][research_li_wang_2017_b]\] \[[Wang et al 2018][research_wang_pan_2018]\] \[[Lu et al 2026][research_lu_gang_2026]\] \[[Wang et al 2019][research_wang_nie_2019]\] \[[Huang et al 2022][research_huang_liu_2022]\] \[[Guo et al 2017][research_guo_bi_2017]\] \[[Pan et al 2018][research_pan_bi_2018]\] \[[Deng et al 2025][research_deng_wang_2025]\] \[[Liu et al 2023][research_liu_yang_2023]\] \[[Zhong and Peng 2018][research_zhong_peng_2018]\] \[[Guo et al 2023][research_guo_gao_2023]\] \[[Cary and Hefner 1970][research_cary_hefner_1970]\] \[[Liang et al 2016][research_liang_liu_2016]\] \[[Gibbons et al 2026][research_gibbons_damm_2026]\] \[[Li et al 2020][research_li_xie_2020]\] \[[Gopinath et al 2022][research_gopinath_govindarajan_2022]\] \[[Gibbons et al 2021][research_gibbons_damm_2021]\] \[[Gopinath et al 2015][research_gopinath_vignesh_2015]\] \[[Grenleski and Billig 1968][research_grenleski_billig_1968]\] \[[Hanquist and Boyd 2018][research_hanquist_boyd_2018]\] \[[Colwell and Modlin 1992][research_colwell_modlin_1992]\] \[[Yue et al 2016][research_yue_wu_2016]\] \[[Jiang et al 2025][research_jiang_zhan_2025]\] \[[Hu et al 2026][research_hu_zheng_2026]\] \[[Woodruff and Lorenz 1966][research_woodruff_lorenz_1966]\] \[[Li et al 2018][research_li_sun_2018]\] \[[Zhao et al 2023][research_zhao_zhang_2023]\] \[[Wartemann et al 2019][research_wartemann_ponchiocamillo_2019]\] \[[Jiang et al 2023][research_jiang_wang_2023]\] \[[Sun et al 2021][research_sun_li_2021]\] \[[Cui et al 2018][research_cui_mei_2018]\] \[[Karabacak and Turan 2023][research_karabacak_turan_2023]\] \[[Zan et al 2018][research_zan_li_2018]\] \[[Richards and Stollery 1979][research_richards_stollery_1979]\] \[[Ifti et al 2022][research_ifti_hermann_2022]\] \[[Li and Wang 2019][research_li_z_2019]\] \[[Li et al 2019][research_li_qin_2019]\] \[[Liu and Liu 2016][research_liu_liu_2016_b]\] \[[Luo et al 2026][research_luo_chen_2026]\] \[[Materials, Structures, and Thermal 2022][research_materials_structures_2022]\] \[[Melis and Wang 1999][research_melis_wang_1999]\] \[[Peng and Zhong 2022][research_peng_zhong_2022]\] \[[Ravindran et al 2019][research_ravindran_bricalli_2019]\] \[[Gao et al 2020][research_gao_zhang_2020]\] \[[Monroe and Boyd 2026][research_monroe_boyd_2026]\] \[[Moszee and Moszee 1997][research_moszee_moszee_1997]\] \[[Ma et al 2019][research_ma_chang_2019_b]\] \[[Hoseinzade and Kim 2024][research_hoseinzade_kim_2024]\] \[[Hoseinzade and Kim 2024][research_hoseinzade_kim_2024_b]\] \[[Mannion et al 2026][research_mannion_ko_2026]\] \[[Lv et al 2020][research_lv_chang_2020]\] \[[Musielak and Musielak 1997][research_musielak_musielak_1997]\] \[[Hufgard et al 2023][research_hufgard_duernhofer_2023]\] \[[Zhao et al 2023][research_zhao_gao_2023]\] \[[Numerical Analysis of Heat Flux Reduction by Transpiration...][research_numerical_analysis_2026]\] \[[Elmouazen et al 2026][research_elmouazen_zhang_2026]\] \[[Gao et al 2026][research_gao_he_2026]\] \[[Geng et al 2026][research_geng_liu_2026]\] \[[Gerlinger and Simsont 2019][research_gerlinger_simsont_2019]\] \[[He et al 2020][research_he_wu_2020]\] \[[Su et al 2019][research_su_wang_2019]\] \[[Hoseinzade et al 2025][research_hoseinzade_lakzian_2025]\] \[[Naved et al 2021][research_naved_hermann_2021]\] \[[Ifti et al 2022][research_ifti_hermann_2022_b]\] \[[Pan et al 2024][research_pan_zhou_2024]\] \[[Guo and Lei 2025][research_guo_lei_2025]\] \[[Tian et al 2024][research_tian_yang_2024]\] \[[Ma et al 2025][research_ma_shu_2025]\] \[[Jiang et al 2023][research_jiang_wang_2023_b]\] \[[Jiang et al 2023][research_jiang_wang_2023_c]\] \[[Gao et al 2020][research_gao_zhang_2020_b]\] \[[Guo et al 2022][research_guo_pang_2022]\] \[[Li et al 2022][research_li_lin_2022]\] \[[Zhang et al 2016][research_zhang_feng_2016]\] \[[Kanda et al 1991][research_kanda_masuya_1991]\] \[[Ko et al 2025][research_ko_mannion_2025]\] \[[Ma et al 2025][research_ma_guo_2025]\] \[[Luo et al 2025][research_luo_luo_2025]\] \[[Miao et al 2020][research_miao_wang_2020]\] \[[Cheng et al 2022][research_cheng_xu_2022]\] \[[Zuo et al 2018][research_zuo_zhang_2018]\] \[[Mannion et al 2026][research_mannion_ko_2026_b]\] \[[Changbao et al 2020][research_changbao_hui_2020]\] \[[Wang et al 2019][research_wang_hou_2019]\] \[[Petley and Dziedzic 1993][research_petley_dziedzic_1993]\] \[[Pichler 2023][research_pichler_2023]\] \[[Poudel and Shoele 2026][research_poudel_shoele_2026]\] \[[Zhang et al 2024][research_zhang_yu_2024]\] \[[He et al 2023][research_he_liu_2023]\] \[[Jin et al 2017][research_jin_jing_2017]\] \[[Li et al 2021][research_li_jin_2021]\] \[[Qin et al 2009][research_qin_bao_2009]\] \[[Qin et al 2010][research_qin_zhou_2010]\] \[[Qin et al 2012][research_qin_bao_2012]\] \[[Xiong et al 2022][research_xiong_qin_2022]\] \[[Zhang et al 2016][research_zhang_feng_2016_b]\] \[[Li et al 2026][research_li_yang_2026]\] \[[Ravichandran et al 2023][research_ravichandran_doherty_2023]\] \[[Sun et al 2026][research_sun_ding_2026]\] \[[Wang et al 2024][research_wang_pan_2024]\] \[[Ferrari et al 2016][research_ferrari_barbato_2016]\] \[[Shanmugam et al 2025][research_shanmugam_silvi_2025]\] \[[Kaufman 1988][research_kaufmanalbert_1988]\] \[[Brewer and Morris 1975][research_brewergd_morrisre_1975]\] \[[Vahl and Edwards 1978][research_vahlwa_edwardsclw_1978]\] \[[Sreekanth and Reddy 1995][research_sreekanth_reddy_1995]\] \[[Zhou et al 2024][research_zhou_zhang_2024]\] \[[Sun Jian and Liu Wei-Qiang 2013][research_sunjian_liuweiqiang_2013]\] \[[Chen et al 2020][research_chen_li_2020]\] \[[Khrapko 2018][research_khrapko_2018]\] \[[Li et al 2018][research_li_li_2018]\] \[[Liu et al 2023][research_liu_han_2023]\] \[[Wu et al 2025][research_wu_he_2025]\] \[[Hongpeng and Weiqiang 2016][research_hongpeng_weiqiang_2016]\] \[[Li et al 2025][research_li_wang_2025_b]\] \[[Luo et al 2024][research_luo_qi_2024]\] \[[Jingqi and Yulong 2024][research_jingqi_yulong_2024]\] \[[WlMBERLY et al 1970][research_wlmberly_mcginnis_1970]\] \[[Cerminara et al 2025][research_cerminara_nayak_2025]\] \[[Cerminara 2023][research_cerminara_2023]\] \[[Brune et al 2015][research_brune_hosder_2015]\] \[[Wu et al 2015][research_wu_yang_2015]\] \[[Xinchun et al 2021][research_xinchun_zhongwei_2021]\] \[[Xinchun Li et al 2020][research_xinchunli_zhongweiwang_2020]\]

### Combined-cycle and precooled engines

**Engines that change mode on the way to orbit.** Rocket-based and turbine-based combined cycles, ejectors and precooled engines.

**169 records.** \[[Han 1998][research_hansamuels_1998]\] \[[Stanley et al 2000][research_stanleythomastroy_alexanderreginald_2000]\] \[[Stanley and Alexander 1999][research_stanleythomastroy_alexanderreginald_1999]\] \[[Thomas 2011][research_thomas_2011]\] \[[Zou et al 2026][research_zou_liu_2026]\] \[[Gu et al 2021][research_gu_sun_2021]\] \[[Zou et al 2022][research_zou_wang_2022_b]\] \[[He et al 2026][research_he_nie_2026]\] \[[Shi et al 2016][research_shi_he_2016]\] \[[Sen et al 2018][research_sen_pesyridis_2018]\] \[[Wei et al 2024][research_wei_shi_2024]\] \[[Xianhong et al 2015][research_xianhong_yuan_2015]\] \[[Li et al 2018][research_li_zhang_2018]\] \[[Moses et al 1999][research_mosespl_bouchardka_1999]\] \[[Zhang et al 2020][research_zhang_wang_2020]\] \[[Xie et al 2025][research_xie_liu_2025]\] \[[Wang et al 2018][research_wang_he_2018]\] \[[Zheng et al 2020][research_zheng_chang_2020]\] \[[Sanjay and Kuzhiveli 2025][research_sanjay_kuzhiveli_2025]\] \[[Wang et al 2023][research_wang_huang_2023]\] \[[An et al 2024][research_an_sun_2024]\] \[[Fusaro et al 2025][research_fusaro_borgna_2025]\] \[[Liu et al 2026][research_liu_zheng_2026]\] \[[Hu et al 2025][research_hu_guo_2025]\] \[[Bulman and Siebenhaar 1995][research_bulman_siebenhaar_1995]\] \[[an et al 2020][research_an_sun_2020]\] \[[Jia et al 2019][research_jia_ye_2019]\] \[[Fu et al 2026][research_fu_song_2026]\] \[[Kors 1988][research_kors_1988]\] \[[Steffen and Yungster 2001][research_steffenchristopherjjr_yungstershaye_2001]\] \[[Computational Fluid Dynamics Analysis Method Developed for...][research_computational_fluid_1997]\] \[[Zhang et al 2017][research_zhang_zhang_2017]\] \[[Yu et al 2019][research_yu_wang_2019_c]\] \[[Zhang et al 2023][research_zhang_chen_2023_b]\] \[[Zhu et al 2025][research_zhu_zhang_2025]\] \[[Kim and Lee 2024][research_kim_lee_2024]\] \[[Liu et al 2026][research_liu_tian_2026]\] \[[Dynamic Testing of the NASA Hypersonic Project Combined Cycle...][research_dynamic_testing_2011]\] \[[Yan et al 2022][research_yan_liu_2022_b]\] \[[Hu et al 2022][research_hu_liu_2022]\] \[[Yan et al 2018][research_yan_he_2018_b]\] \[[Wang et al 2017][research_wang_yang_2017]\] \[[Guo et al 2020][research_guo_luo_2020]\] \[[Yan et al 2022][research_yan_liu_2022]\] \[[Escher 1992][research_escher_1992]\] \[[Escher 1999][research_escher_1999]\] \[[Escher 2001][research_escher_2001]\] \[[Escher et al 1986][research_escher_doughty_1986]\] \[[Takashima and Kothari 1998][research_takashiman_kothariap_1998]\] \[[Thomas et al 1997][research_thomasscottr_perkinshdouglas_1997]\] \[[Nelson and Hawk 1997][research_knelson_clarkwhawk_1997]\] \[[Liu et al 2017][research_liu_yuan_2017]\] \[[Lv et al 2020][research_lv_xu_2020]\] \[[Nie et al 2024][research_nie_he_2024]\] \[[Li et al 2021][research_li_liu_2021]\] \[[Qin et al 2026][research_qin_yuan_2026]\] \[[Yao et al 2023][research_yao_sun_2023]\] \[[Clemens 2010][research_clemens_2010]\] \[[Yu et al 2025][research_yu_yang_2025]\] \[[Fu et al 2024][research_fu_song_2024]\] \[[Wang et al 2023][research_wang_eri_2023]\] \[[Wang et al 2026][research_wang_hong_2026]\] \[[Han et al 2000][research_han_bai_2000]\] \[[Zuo and Mölder 2019][research_zuo_molder_2019]\] \[[An et al 2021][research_an_wang_2021]\] \[[Ingenito et al 2009][research_ingenito_bruno_2009]\] \[[Ingenito et al 2009][research_ingenito_bruno_2009_b]\] \[[Wang et al 2024][research_wang_zou_2024]\] \[[Huang et al 2025][research_huang_ning_2025]\] \[[Chen et al 2024][research_chen_zhang_2024]\] \[[Liu et al 2021][research_liu_yuan_2021]\] \[[Nie et al 2023][research_nie_ye_2023]\] \[[Nie et al 2025][research_nie_qin_2025]\] \[[Gao et al 2025][research_gao_ge_2025]\] \[[Isono and Fujikawa 2025][research_isono_fujikawa_2025]\] \[[Kloesel et al 2011][research_kloesel_ratnayake_2011]\] \[[Kojima et al 2015][research_kojima_taguchi_2015]\] \[[Yang et al 2015][research_yang_shi_2015]\] \[[Meng et al 2021][research_meng_wan_2021]\] \[[Yu et al 2020][research_yu_wang_2020]\] \[[Lv et al 2022][research_lv_xu_2022]\] \[[Lv et al 2023][research_lv_huang_2023]\] \[[Zheng et al 2019][research_zheng_chang_2019]\] \[[Zheng et al 2021][research_zheng_chang_2021]\] \[[Gao et al 2020][research_gao_xi_2020]\] \[[Ma et al 2023][research_ma_jiang_2023]\] \[[Moss and Perrell 2005][research_moss_perrell_2005]\] \[[Liu et al 2024][research_liu_zhang_2024]\] \[[Yu et al 2017][research_yu_jones_2017]\] \[[Fujikawa et al 2017][research_fujikawa_tsuchiya_2017]\] \[[Nelson and McArthur 2001][research_nelson_mcarthur_2001]\] \[[An et al 2023][research_an_sun_2023]\] \[[Wang et al 2023][research_wang_eri_2023_b]\] \[[Shi et al 2016][research_shi_liu_2016]\] \[[Zhang et al 2018][research_zhang_liu_2018]\] \[[Cui et al 2018][research_cui_xu_2018]\] \[[Lee and Bae 2023][research_lee_bae_2023]\] \[[Wang et al 2022][research_wang_li_2022]\] \[[Ruf et al 2001][research_rufjosephh_holtjamesb_2001]\] \[[Ruf et al 1999][research_rufjoseph_holtjamesb_1999]\] \[[Jee and Etele 2020][research_jee_etele_2020]\] \[[Ouzts 2008][research_ouzts_2008]\] \[[Fernandez et al 2001][research_fernandezrene_trefnycharlesj_2001]\] \[[Han et al 2026][research_han_xu_2026]\] \[[Shi 2022][research_shi_2022]\] \[[Yungster et al 2015][research_yungstershaye_paxsondaniele_2015]\] \[[Ma et al 2022][research_ma_jiang_2022]\] \[[Pan et al 2022][research_pan_xiong_2022]\] \[[Cai et al 2023][research_cai_zheng_2023]\] \[[Wang et al 2022][research_wang_cheng_2022]\] \[[Xu et al 2025][research_xu_leng_2025]\] \[[Lee et al 2015][research_lee_yang_2015]\] \[[Zheng et al 2018][research_zheng_chang_2018]\] \[[Yu et al 2019][research_yu_wang_2019_b]\] \[[Cai et al 2024][research_cai_zheng_2024]\] \[[Qi et al 1998][research_qi_wang_1998]\] \[[Hillion et al 2023][research_hillion_parisse_2023]\] \[[Hueter and Turner 1998][research_hueteruwe_turnerjames_1998]\] \[[Park et al 2026][research_park_lee_2026]\] \[[Veeran et al 2018][research_veeran_pesyridis_2018]\] \[[Yan et al 2023][research_yan_wang_2023]\] \[[Wang et al 2026][research_wang_fang_2026]\] \[[Polev et al 2022][research_polev_grunin_2022]\] \[[Wang et al 2025][research_wang_xu_2025]\] \[[Wei et al 2017][research_wei_xue_2017]\] \[[Rice 2002][research_rice_2002]\] \[[DeBonis and Yungster 1996][research_debonisjr_yungsters_1996]\] \[[Kolimi Abdul Ahad 2021][research_kolimiabdulahad_2021]\] \[[Sabre Space Engine Gets £26.5M Boost][research_sabre_space_2018]\] \[[Saunders et al 2007][research_saunders_slater_2007]\] \[[Scramjets and Combined Cycle 2022][research_scramjets_and_2022]\] \[[Tomioka et al 2021][research_tomioka_takegoshi_2021]\] \[[Dai and Huang 2021][research_dai_huang_2021]\] \[[Shi 2016][research_shi_2016]\] \[[Siebenhaar and Bulman 1998][research_siebenhaar_bulman_1998]\] \[[Siebenhaar et al 1999][research_siebenhaar_bulman_1999]\] \[[Liu et al 2024][research_liu_kuang_2024]\] \[[Slater and Saunders 2009][research_slater_saunders_2009]\] \[[Yang et al 2023][research_yang_yang_2023]\] \[[Yang et al 2024][research_yang_tian_2024]\] \[[Strutjet Rocket-Based Combined-Cycle Engine 2001][research_strutjet_rocket_based_2001]\] \[[Lyu et al 2021][research_lyu_gao_2021]\] \[[Zhao et al 2023][research_zhao_fan_2023]\] \[[Dong et al 2018][research_dong_tang_2018]\] \[[Wen 2023][research_wen_2023]\] \[[Dong et al 2019][research_dong_sun_2019]\] \[[Saunders et al 2012][research_saundersjd_stuebertj_2012]\] \[[Liu et al 2017][research_liu_yuan_2017_b]\] \[[Yan et al 2018][research_yan_he_2018]\] \[[Zou et al 2022][research_zou_wang_2022]\] \[[Wang et al 2021][research_wang_dang_2021]\] \[[Cai et al 2023][research_cai_chen_2023]\] \[[Wang et al 2021][research_wang_ha_2021]\] \[[Yu et al 2019][research_yu_yu_2019]\] \[[Yu et al 2019][research_yu_wang_2019]\] \[[Li et al 2025][research_li_zhang_2025]\] \[[Cai et al 2024][research_cai_chen_2024]\] \[[Zhang et al 2017][research_zhang_wang_2017]\] \[[Wang et al 2022][research_wang_yu_2022_b]\] \[[Wang et al 2024][research_wang_liu_2024]\] \[[Yu et al 2017][research_yu_pan_2017]\] \[[Thomas et al 2001][research_thomas_palac_2001]\] \[[Thomas et al 2009][research_thomas_walker_2009]\] \[[Song et al 2026][research_song_xu_2026]\] \[[Yao et al 2023][research_yao_gu_2023]\] \[[Liu et al 2015][research_liu_yuan_2015]\] \[[Lepsch et al 1991][research_lepsch_stanley_1991]\] \[[Chen et al 2022][research_chen_zou_2022]\] \[[Zhou et al 2017][research_zhou_lu_2017]\]

### Carbon-carbon, ceramic matrix composites and oxidation protection

**The structural materials that survive the highest temperatures.** Carbon-carbon and its oxidation protection, ceramic matrix composites and ultra-high-temperature ceramics.

**147 records.** \[[Kimura et al 1976][research_kimura_shibusa_1976]\] \[[Strangman and Keiser 1988][research_strangman_keiser_1988]\] \[[95/05986 Oxidation and ablation of 3D carbon-carbon composite...][research_95_05986_oxidation_1995]\] \[[95/06441 Studies on solution-derived ceramic coatings for...][research_95_06441_studies_1995]\] \[[Vlassak 2008][research_vlassak_2008]\] \[[Li 2021][research_li_2021]\] \[[Otsuka et al 1999][research_otsuka_sakamoto_1999]\] \[[Deng et al 2026][research_deng_ying_2026]\] \[[Ju et al 2022][research_ju_liu_2022]\] \[[Wang et al 2021][research_wang_gao_2021]\] \[[Huo et al 2015][research_huo_cheng_2015]\] \[[Battelle Memorial Inst Columbus Oh 1947][research_battellememorialinstcolumbusoh_1947]\] \[[An Investigation on the Effect of TiC Additive on the...][research_an_investigation_2024]\] \[[Whitcomb 2010][research_whitcomb_2010]\] \[[Wang et al 2026][research_wang_huang_2026]\] \[[Barrier coating and penetrant providing oxidation protection...][research_barrier_coating_1990]\] \[[Daghigh and Daghigh 2025][research_daghigh_daghigh_2025]\] \[[Carbon fiber composites effect of fiber oxidation on...][research_carbon_fiber_1971]\] \[[Bacos 1993][research_bacos_1993]\] \[[Ibadi et al 2026][research_ibadi_supriadi_2026]\] \[[Chu et al 2026][research_chu_tu_2026]\] \[[Wu 1992][research_wu_1992]\] \[[Stewart 1973][research_stewart_1973]\] \[[Cunnington et al 1990][research_cunnington_robinson_1990]\] \[[Saha 2022][research_saha_2022]\] \[[Li et al 2020][research_li_yang_2020]\] \[[Baier et al 2024][research_baier_friess_2024]\] \[[Adam Khan 2024][research_adamkhan_2024]\] \[[Zhao et al 1985][research_zhao_bradt_1985]\] \[[Kowbel et al 1993][research_kowbel_huang_1993]\] \[[Longbiao 2019][research_longbiao_2019_b]\] \[[Kavoosi et al 2026][research_kavoosi_mashhadi_2026]\] \[[Li 2020][research_li_2020]\] \[[Echeverria Aparicio et al 2022][research_echeverriaaparicio_fishpool_2022]\] \[[Chen and Wang 2020][research_chen_wang_2020]\] \[[Zou et al 2016][research_zou_li_2016]\] \[[Patra and Lee 2018][research_patra_lee_2018]\] \[[Wilkinson and Ruggles-Wrenn 2016][research_wilkinson_ruggleswrenn_2016]\] \[[Flexible ceramic matrix composite seal][research_flexible_ceramic_2015]\] \[[Zhu et al 1999][research_zhu_ohtani_1999]\] \[[Delage et al 2022][research_delage_saiz_2022]\] \[[Rahimi et al 2026][research_rahimi_svolos_2026]\] \[[Glass 2008][research_glass_2008]\] \[[De Stefano Fumo et al 2025][research_destefanofumo_sciti_2025]\] \[[Stewart et al 2010][research_stewartdavida_leiserdanielb_2010]\] \[[High Power Water Jet Guided Laser Cutting of SiC/SiC Ceramic...][research_high_power_2022]\] \[[Keer et al 1994][research_keer_faber_1994]\] \[[Raj 1987][research_raj_1987]\] \[[Huang et al 2023][research_huang_xia_2023]\] \[[Li et al 1993][research_li_yang_1993]\] \[[Kim et al 2021][research_kim_choi_2021]\] \[[Jiang et al 2025][research_jiang_xu_2025]\] \[[Wang et al 2022][research_wang_gao_2022]\] \[[Lehmusto et al 2024][research_lehmusto_ievlev_2024]\] \[[Presby 2021][research_presby_2021]\] \[[Choudhary et al 2021][research_choudhary_daschakladar_2021]\] \[[Bertrand et al 2025][research_bertrand_huchette_2025]\] \[[Du et al 2026][research_du_chong_2026]\] \[[Ehrburger et al 1986][research_ehrburger_baranne_1986]\] \[[Insulative Performance of Selected Ablative Materials in a...][research_carman_jb_1966]\] \[[Interstitially protected oxidation resistant carbon-carbon...][research_interstitially_protected_1988]\] \[[Investigation of the Effect of Temperature on the...][research_investigation_of_2024]\] \[[Saccone et al 2016][research_saccone_gardi_2016]\] \[[Liu et al 2021][research_liu_liu_2021]\] \[[Huang et al 2026][research_huang_lu_2026]\] \[[Zhang et al 2022][research_zhang_wang_2022]\] \[[Maahs 1989][research_maahs_1989]\] \[[Upsadhya 2001][research_upsadhya_2001]\] \[[Pandey et al 2022][research_pandey_soni_2022]\] \[[Cho et al 1996][research_cho_ha_1996]\] \[[Li et al 2024][research_li_huang_2024]\] \[[Li 2020][research_li_2020_b]\] \[[Alghamdi and Al-Ghamdi 2016][research_alghamdi_alghamdi_2016]\] \[[Ahearn and Rand 1996][research_ahearn_rand_1996]\] \[[Hamza and Chattopadhyay 2024][research_hamza_chattopadhyay_2024]\] \[[Skinner and Chattopadhyay 2021][research_skinner_chattopadhyay_2021]\] \[[El Yagoubi et al 2015][research_elyagoubi_lamon_2015]\] \[[Nardo et al 1961][research_nardo_erickson_1961]\] \[[Hyers 2009][research_hyers_2009]\] \[[Ohlhorst et al 1992][research_ohlhorst_vaughn_1992]\] \[[Rodríguez-Mirasol et al 1995][research_rodriguezmirasol_thrower_1995]\] \[[Gorskii and Olenicheva 2018][research_gorskii_olenicheva_2018]\] \[[Han et al 1995][research_han_he_1995]\] \[[Crocker and McEnaney 1991][research_crocker_mcenaney_1991]\] \[[Yamada and Fujii 1999][research_yamada_fujii_1999]\] \[[McKee 1987][research_mckee_1987]\] \[[Gee and Little 1991][research_gee_little_1991]\] \[[Opila 2003][research_opilaelizabethj_2003]\] \[[Wei and Tsung-Ming 1994][research_wei_tsungming_1994]\] \[[Sheehan 1989][research_sheehan_1989]\] \[[Oxidation protection for carbon fibre composites][research_oxidation_protection_1990]\] \[[Jawed and Nagle 1986][research_jawed_nagle_1986]\] \[[Wang et al 1995][research_wang_zhou_1995]\] \[[Buchanan and Little 1993][research_buchanan_little_1993]\] \[[Zhao et al 2022][research_zhao_sun_2022]\] \[[Triantou et al 2017][research_triantou_perez_2017]\] \[[Chen et al 2018][research_chen_zhang_2018]\] \[[Yang et al 2026][research_yang_li_2026]\] \[[Zhang et al 2024][research_zhang_shi_2024]\] \[[Xu et al 2018][research_xu_cheng_2018]\] \[[Gupta et al 2009][research_gupta_sun_2009]\] \[[Tanabe et al 1987][research_tanabe_yasuda_1987]\] \[[Murthy et al 2021][research_murthy_patel_2021]\] \[[Venkatachalam et al 2024][research_venkatachalam_esser_2024]\] \[[Mendiratta and Choudhury 1978][research_mendiratta_choudhury_1978]\] \[[Magnus et al 2020][research_magnus_sharp_2020]\] \[[Ransone et al 1992][research_ransonephilipo_yamakiyrobert_1992]\] \[[Generale and Kalidindi 2021][research_generale_kalidindi_2021]\] \[[Zhou et al 2023][research_zhou_tan_2023]\] \[[Zhang et al 2022][research_zhang_sun_2022]\] \[[Bilsborough et al 2025][research_bilsborough_neilsenburke_2025]\] \[[Sankar and Kelkar 1995][research_sankar_kelkar_1995]\] \[[Makurunje et al 2021][research_makurunje_sigalas_2021]\] \[[Scanning and Transmission Electron Microscopy of High...][research_scanning_and_1994]\] \[[Gopinath et al 2019][research_gopinath_jagadeesh_2019]\] \[[Martin and Boyd 2015][research_martin_boyd_2015]\] \[[Kulkarni et al 2026][research_kulkarni_gujar_2026]\] \[[Manocha and Manocha 1995][research_manocha_manocha_1995]\] \[[Doozandeh et al 2025][research_doozandeh_jindal_2025]\] \[[Longbiao 2018][research_longbiao_2018]\] \[[Longbiao 2016][research_longbiao_2016]\] \[[Longbiao 2019][research_longbiao_2019]\] \[[Kong et al 2023][research_kong_lee_2023]\] \[[Jieyan and Yuan 2022][research_jieyan_yuan_2022]\] \[[Wang and Li 2016][research_wang_li_2016]\] \[[Ruggles-Wrenn and Schmidt 2024][research_ruggleswrenn_schmidt_2024]\] \[[Marschall 2011][research_marschall_2011]\] \[[Hoffman et al 1995][research_hoffman_phan_1995]\] \[[Goldstein et al 1966][research_goldstein_carter_1966]\] \[[Deng et al 2016][research_deng_li_2016]\] \[[Li et al 2021][research_li_reynaud_2021]\] \[[Chang et al 2022][research_chang_huang_2022]\] \[[Wang et al 2019][research_wang_wei_2019]\] \[[Triantou et al 2017][research_triantou_mergia_2017]\] \[[Yang et al 2026][research_yang_hayat_2026]\] \[[Wu et al 2020][research_wu_lin_2020]\] \[[Ghori et al 2023][research_ghori_narendar_2023]\] \[[Xu et al 2024][research_xu_he_2024]\] \[[Purwar and Basu 2017][research_purwar_basu_2017]\] \[[Shimojima et al 2017][research_shimojima_hosokawa_2017]\] \[[Malakhov 2025][research_malakhov_2025]\] \[[Longbiao 2020][research_longbiao_2019_c]\] \[[Rubio et al 2018][research_rubio_ramanujam_2018]\] \[[Chen 2023][research_chen_2023]\] \[[Nieto et al 2021][research_nieto_samayoa_2021]\] \[[White 2004][research_white_2004]\] \[[Zaldivar et al 1998][research_zaldivar_rellick_1998]\]

### Stagnation-point, leading-edge and aerodynamic heating

**How much heat arrives and where.** Stagnation-point and leading-edge heating, its correlations and computation, radiative heating and the engineering methods used in design.

**145 records.** \[[Lu et al 2025][research_lu_zhang_2025]\] \[[Huang et al 2025][research_huang_li_2025_b]\] \[[Türkoğlu et al 2026][research_turkoglu_donmez_2026]\] \[[Hawkins et al 1999][research_hawkins_kidd_1999]\] \[[Grasso and Gnoffo 1990][research_grassofrancesco_gnoffopetera_1990]\] \[[Sun and Zhu 2019][research_sun_zhu_2019]\] \[[Wang et al 2026][research_wang_song_2026]\] \[[Stalder 1957][research_stalder_1957]\] \[[Persh 1955][research_persh_1955]\] \[[Yang and Liu 2017][research_yang_liu_2017]\] \[[Abtahi and Dean 1990][research_abtahi_dean_1990]\] \[[Abu-Romia 1971][research_aburomia_1971]\] \[[Mori 1965][research_mori_1965]\] \[[Wurster and Stone 1993][research_wursterke_stonehw_1993]\] \[[Aso and Hayashi 1990][research_aso_hayashi_1990]\] \[[Smith 2021][research_smith_2021]\] \[[Tang et al 2024][research_tang_xu_2024]\] \[[Unterberg 1957][research_unterberg_1957]\] \[[Chen and He 2025][research_chen_he_2025_b]\] \[[Qiao et al 2022][research_qiao_liu_2022]\] \[[Brunner 1959][research_brunner_1959]\] \[[Armstrong and Nicholls 1967][research_armstrong_nicholls_1967]\] \[[Yang et al 2022][research_yang_wang_2022]\] \[[Bade 1975][research_bade_1975]\] \[[Yang et al 2021][research_yang_li_2021]\] \[[Bogdonoff 1968][research_bogdonoff_1968]\] \[[Bolz 1979][research_bolz_1979]\] \[[Boyd and Padilla 2003][research_boyd_padilla_2003]\] \[[Burchfield and Bontrager 1966][research_burchfield_bontrager_1966]\] \[[Butler 1967][research_butler_1967]\] \[[Byrom and Allen 1994][research_byrom_allen_1994]\] \[[Candler and Park 1988][research_candler_park_1988]\] \[[Yu et al 2021][research_yu_ni_2021]\] \[[Chang et al 1993][research_chang_bass_1993]\] \[[Chao and Jeng 1965][research_chao_jeng_1965]\] \[[Cheng 1960][research_cheng_1960]\] \[[Chernyi 1961][research_chernyi_1961]\] \[[Schneider 1970][research_schneider_1970]\] \[[Miyashita et al 2025][research_miyashita_sugihara_2025]\] \[[Ashok et al 2023][research_ashok_joseph_2023]\] \[[Tang et al 2025][research_tang_li_2025]\] \[[Davis 1964][research_davis_1964]\] \[[Golewski and Sadowski 2019][research_golewski_sadowski_2019]\] \[[Donohue et al 1992][research_donohue_marinelli_1992]\] \[[Dsouza and Molder 1971][research_dsouza_molder_1971]\] \[[Han and Han 2024][research_han_han_2024]\] \[[Riley and DeJarnette 1992][research_riley_dejarnette_1992]\] \[[Wurster et al 1998][research_wursterkathryne_rileychristopherj_1998]\] \[[Evaluation of Various Flow Control Methods in Reducing Drag...][research_evaluation_of_2024]\] \[[Rufer et al 2009][research_rufershannj_nowakrobertj_2009]\] \[[Fay and Kemp 1963][research_fay_kemp_1963]\] \[[Zoby and Thompson 1990][research_zoby_thompson_1990]\] \[[Furey 1970][research_furey_1970]\] \[[Gai and Cao 2025][research_gai_cao_2025]\] \[[Reba and Christian 1963][research_reba_christian_1963]\] \[[Gilmore 1967][research_gilmore_1967]\] \[[Ginter and Cerreta 1962][research_ginter_cerreta_1962]\] \[[Gladden et al 1990][research_gladden_melis_1990]\] \[[Gupta 1987][research_gupta_1987]\] \[[Gupta et al 1992][research_gupta_jones_1992]\] \[[Guy][research_guy]\] \[[Ding et al 2022][research_ding_chen_2022]\] \[[Richards 1978][research_richards_1978]\] \[[Nardo and Sadler 1962][research_nardo_sadler_1962]\] \[[Tewfik and Giedt 1960][research_tewfik_giedt_1960]\] \[[Hinman et al 2015][research_hinman_schmitt_2015]\] \[[Hossain 2025][research_hossain_2025]\] \[[Hoult et al 2003][research_hoult_starkey_2003]\] \[[Si et al 2019][research_si_huang_2019]\] \[[Inoue and Yamamoto 1990][research_inoue_yamamoto_1990]\] \[[Dai et al 2025][research_dai_shao_2025]\] \[[Bein et al 1993][research_beint_friedmannp_1993]\] \[[Hammitt and Bogdonoff 1956][research_hammitt_bogdonoff_1956]\] \[[Yushchenkova et al 1967][research_yushchenkova_pomerantsev_1967]\] \[[Zhluktov and Tirskii 1990][research_zhluktov_tirskii_1990]\] \[[Barone et al 2022][research_barone_nicholson_2022]\] \[[Kang et al 2026][research_kang_yan_2026]\] \[[Kaufman and Louis G. 1964][research_kaufman_louisg_1964]\] \[[Levin 2015][research_levin_2015]\] \[[Lewis et al 1963][research_lewis_burgess_1963]\] \[[Dai et al 2023][research_dai_zhao_2023]\] \[[Chen 1969][research_chen_1969]\] \[[Meyer 1959][research_meyer_1959]\] \[[Maxwell and Hoang 2016][research_maxwell_hoang_2016]\] \[[Tirskii 1993][research_tirskii_1993]\] \[[Mohling 2018][research_mohling_2018]\] \[[Boyd 2002][research_boyd_2002]\] \[[Morgan 1961][research_morgan_1961]\] \[[Duan et al 2026][research_duan_zhao_2026]\] \[[Nomura 1983][research_nomura_1983]\] \[[Inger 1995][research_inger_1995_b]\] \[[Inger 1995][research_inger_1995_c]\] \[[Ingeri 1966][research_ingeri_1966]\] \[[Surzhikov 2018][research_surzhikov_2018]\] \[[Sun et al 2020][research_sun_yang_2020_b]\] \[[Vargas Venegas and Huang 2023][research_vargasvenegas_huang_2023]\] \[[Pope 1968][research_pope_1968]\] \[[Huang et al 2022][research_huang_he_2022]\] \[[Kaufman 1963][research_kaufman_1963]\] \[[Desai et al 2019][research_desai_brahmachary_2019]\] \[[Probstein 1968][research_probstein_1968]\] \[[Radiation at Hypersonic Speeds 1962][research_radiation_at_1962]\] \[[Liu and Sogame 1969][research_liu_sogame_1969]\] \[[Quinn and Gong 1990][research_quinnrobertd_gongleslie_1990]\] \[[Kumar and Mahulikar 2016][research_kumar_mahulikar_2016]\] \[[Brociek et al 2023][research_brociek_hetmaniok_2023]\] \[[Baker and Kramer 1982][research_baker_kramer_1982]\] \[[Reid 2025][research_reid_2025]\] \[[Yu et al 2025][research_yu_wang_2025]\] \[[Zhu et al 2018][research_zhu_peng_2018]\] \[[Rodrigues 2026][research_rodrigues_2026]\] \[[Rose and Stankevics 1963][research_rose_stankevics_1963]\] \[[Rosner and Cibrian 1974][research_rosner_cibrian_1974]\] \[[Ru-ren Chow 1963][research_rurenchow_1963]\] \[[Sano 1981][research_sano_1981]\] \[[Santos 2005][research_santos_2005]\] \[[Santos 2007][research_santos_2007]\] \[[Santos and Lewis 2003][research_santos_lewis_2003]\] \[[Sarosh 2021][research_sarosh_2021]\] \[[Arguchintseva 1999][research_arguchintseva_1999]\] \[[Shimada and Ohwada 2020][research_shimada_ohwada_2020]\] \[[Qin et al 1991][research_qin_scriba_1991]\] \[[Shorenstein 1971][research_shorenstein_1971]\] \[[Simoneau et al 1988][research_simoneau_hendricks_1988]\] \[[Stephan and Obermeier 1974][research_stephan_obermeier_1974]\] \[[Udhayakumar et al 2016][research_s_ad_2016]\] \[[Trimmer 1968][research_trimmer_1968]\] \[[Test Method for Calculation 2008][research_test_method_2008]\] \[[Allen 1966][research_allenhj_1966]\] \[[Liu 1967][research_liu_1967]\] \[[Huo and Yang 2015][research_huo_yang_2015]\] \[[Wang et al 2024][research_wang_wang_2024]\] \[[Thornton et al 1990][research_thornton_oden_1990]\] \[[Tokuda and Yang 2019][research_tokuda_yang_2019]\] \[[Tong and Giedt 1963][research_tong_giedt_1963]\] \[[Tirsky 1993][research_tirsky_1993]\] \[[Vanmol and Anderson 1992][research_vanmol_andersonjr_1992]\] \[[Schubert 1978][research_schubert_1978]\] \[[Tong et al 2023][research_tong_duan_2023]\] \[[Weilmuenster and Gnoffo 1992][research_weilmuenster_gnoffo_1992]\] \[[Wieting 1990][research_wieting_1990]\] \[[Wittliff and Wilson 1961][research_wittliff_wilson_1961_b]\] \[[Wortman 1970][research_wortman_1970]\] \[[Xu and Fang 2022][research_xu_fang_2022]\] \[[Yang et al 2014][research_yang_duan_2014]\]

### The National Aero-Space Plane and its programme record

**The programme's own record.** Technology reviews, status reports, the Defense Science Board's assessments, cost and environmental studies, and the programme's technical papers on the X-30 and its derivatives, together with the aerospace plane studies of other countries.

**134 of these 141 records date from 1985 to 1995**, the years of the programme and its close-out, and 71 of them are report primaries. What the record lacks is the decision record, as The Source Base explains.

**141 records.** \[[McNelis et al 1995][research_mcnelisnancyb_hardyterryl_1995]\] \[[Kelly and Blosser 1992][research_kellyhneale_blossermaxl_1992]\] \[[Kelly and Blosser 1994][research_kellyhneale_blossermaxl_1994]\] \[[Aero-Space Plane Flexible Access 1991][research_aero_space_plane_1991]\] \[[Heeg et al 1993][research_heegjennifer_zeilerthomasa_1993]\] \[[Mehta 1994][research_mehtaunmeelb_1994]\] \[[Brown et al 1992][research_brown_wierzbanowski_1992]\] \[[Ricketts et al 1993][research_rickettsrodneyh_nollthomase_1993]\] \[[Anfimov 1993][research_anfimov_1993]\] \[[Autonomous space processor for 1988][research_autonomous_space_1988]\] \[[Barthelemy 1989][research_barthelemy_1989_b]\] \[[Barthelemy 1991][research_barthelemy_1991]\] \[[Baumann and Bisbee 2003][research_baumann_bisbee_2003]\] \[[Bert 1989][research_bert_1989]\] \[[Bogue and Erbland 1993][research_bogue_erbland_1993]\] \[[Butler and Moore 1992][research_butler_moore_1992]\] \[[Calise et al 1988][research_calise_flandro_1988]\] \[[Camarda and Murrow 1990][research_camarda_murrow_1990]\] \[[Chakravarthy and the Computational Fluid Dynamics Department 1990][research_chakravarthy_thecomputationalfluiddynamicsdepartment_1990]\] \[[Chaput 1989][research_chaput_1989]\] \[[Chase 1991][research_chase_1991_b]\] \[[Chase 1991][research_chase_1991]\] \[[Chase and Tang 1995][research_chase_tang_1995]\] \[[Cole et al 1993][research_cole_florance_1993]\] \[[Sullivan 1991][research_williamsullivan_1991]\] \[[Seebass 1989][research_seebass_1989]\] \[[Dayton 1993][research_dayton_1993]\] \[[Defense Science Board Washington Dc 1988][research_defensescienceboardwashingtondc_1988]\] \[[Defense Science Board Washington Dc 1992][research_defensescienceboardwashingtondc_1992]\] \[[DeNardo 1994][research_denardo_1994]\] \[[Dewitt et al 1989][research_dewitt_hardy_1989]\] \[[Dress et al 1994][research_dress_boyden_1994]\] \[[Dube et al 1991][research_dube_slifka_1991]\] \[[Ellis 1989][research_ellis_1989]\] \[[Emanuel 1989][research_emanuel_1989_b]\] \[[Erbland 1990][research_erbland_1990]\] \[[Froning et al 1990][research_froning_gaubatz_1990]\] \[[Hannum and Berkopec 1989][research_hannumnedp_berkopecfrankd_1989]\] \[[Anderson 1993][research_andersoncharlesw_1993]\] \[[Hanaoka 1997][research_hanaoka_1997]\] \[[Hannigan and Webb 1991][research_hannigan_webb_1991]\] \[[Harris 1993][research_harris_1993]\] \[[Harsha and Waldman 1989][research_harsha_waldman_1989]\] \[[Hickman and Adams 1991][research_hickman_adams_1991]\] \[[Steinetz et al 1991][research_steinetzbrucem_melismatthewe_1991]\] \[[Hinkley et al 1995][research_hinkley_prasad_1995]\] \[[Hunt and Martin 1992][research_hunt_martin_1992]\] \[[Hunt and Martin 1989][research_huntjamesl_martinjohng_1989]\] \[[Richardson et al 1989][research_richardsonpamelaf_mcclintoncharlesr_1989]\] \[[Mehta 1995][research_mehtau_1995]\] \[[Maglieri et al 1990][research_maglieridomenicj_sothcottvictore_1990]\] \[[Jackman et al 1992][research_jackman_douglas_1992]\] \[[Johnson 1991][research_johnson_1991]\] \[[Kahre 1987][research_kahre_1987]\] \[[Kasten 1991][research_kasten_1991]\] \[[Kussoy et al 1992][research_kussoy_menter_1992]\] \[[Lanshin 1993][research_lanshin_1993]\] \[[Lehrach 1987][research_lehrach_1987]\] \[[Longstaff 1995][research_longstaff_1995]\] \[[Wierzbanowski and Kasten 1990][research_wierzbanowskitheodore_kastenterryd_1990]\] \[[Mattern 1992][research_mattern_1992]\] \[[McCandless and Cruz 1985][research_mccandless_cruz_1985]\] \[[McClinton et al 1990][research_mcclinton_bittner_1990]\] \[[Mease 1993][research_mease_1993]\] \[[Mease and Van Buren 1994][research_mease_vanburen_1994]\] \[[Mehta 1990][research_mehta_1990]\] \[[Mehta 1992][research_mehta_1992]\] \[[Mehta 1993][research_mehta_1993]\] \[[Miele 1990][research_miele_1990]\] \[[Morris 1992][research_morris_1992]\] \[[Morris 1995][research_morrisjr_1995]\] \[[Moszee and Snyder 1989][research_moszee_snyder_1989]\] \[[Dixon 1985][research_dixonsc_1985]\] \[[Whitehead 1989][research_whiteheadallenhjr_1989]\] \[[Doggett et al 1991][research_doggettrobertvjr_rickettsrodneyh_1991]\] \[[NASP tests composites 1991][research_nasp_tests_1991]\] \[[Piland 1987][research_pilandwilliamm_1987]\] \[[National Aero-Space Plane NASP 1990][research_national_aero_space_1990]\] \[[Wright 1989][research_wrighthowardt_1989]\] \[[Berry 1991][research_berry_1991]\] \[[Johnson et al 1993][research_johnsondl_hillck_1993]\] \[[Natural environment requirements definition 1993][research_natural_environment_1993]\] \[[Nebylov and Tomita 1998][research_nebylov_tomita_1998]\] \[[Neyland 1993][research_neyland_1993]\] \[[Ohlhorst et al 1990][research_ohlhorst_vaughn_1990]\] \[[Parker et al 1991][research_parker_spain_1991]\] \[[Pelloux 1994][research_pelloux_1994]\] \[[Performance and Technological Feasibility 2018][research_performance_and_2018]\] \[[Piland 1987][research_piland_1987]\] \[[Pototzky et al 1988][research_pototzky_spain_1988]\] \[[Povinelli et al 1990][research_povinelli_dwoyer_1990]\] \[[Powell 1992][research_powell_1992]\] \[[Hicks 1991][research_hicksjohnw_1991]\] \[[Anderson et al 1990][research_cwanderson_charlesrmcclinton_1990]\] \[[Psiaki and Park 1991][research_psiaki_park_1991]\] \[[Pukhov 1993][research_pukhov_1993]\] \[[Corban et al 1991][research_corbanje_caliseaj_1991]\] \[[Rasmussen and Stevens 1987][research_rasmussen_stevens_1987]\] \[[Barthelemy 1989][research_barthelemy_1989]\] \[[Reda 1991][research_reda_1991]\] \[[Abell 1989][research_abell_1989]\] \[[Cavolowsky et al 1995][research_cavolowskyjohna_loomismarkp_1995]\] \[[Rodgers 1992][research_rodgers_1992]\] \[[Ronald 1989][research_ronald_1989]\] \[[Ronald 1989][research_ronald_1989_b]\] \[[Ronald 1991][research_ronald_1991]\] \[[Ronald 1993][research_ronald_1993]\] \[[Ronald 1995][research_ronald_1995]\] \[[Ruffin et al 1989][research_ruffin_venkatapathy_1989]\] \[[Sams 1989][research_sams_1989]\] \[[Sasmal et al 1991][research_sasmal_hochstein_1991]\] \[[Scramjet Engine Research athe 2001][research_scramjet_engine_2001]\] \[[Spain et al 1993][research_spain_zeiler_1993_b]\] \[[Spain et al 1993][research_spain_zeiler_1993]\] \[[Steinetz 1991][research_steinetz_1991]\] \[[Little 1992][research_littlete_1992]\] \[[Sypniewski 1989][research_sypniewski_1989]\] \[[Tank 1991][research_tank_1991]\] \[[Rausch and Morris 1992][research_rauschvincentl_morrischarlesekjr_1992]\] \[[Hannum 1988][research_hannumnedp_1988]\] \[[Christol 1993][research_christol_1993]\] \[[Song and Su 2015][research_song_su_2015]\] \[[Wierzbanowski and Armstrong 1991][research_wierzbanowskitheodore_armstrongjohnnyg_1991]\] \[[Schweikart and Hallion 1998][research_schwelkart_hallion_1997]\] \[[Hallion et al 1995][research_hallion_becker_1995]\] \[[Woodcock 1988][research_woodcock_1988]\] \[[Thomas and Powell 1992][research_thomas_powell_1992]\] \[[Throckmorton 1989][research_throckmorton_1989]\] \[[Toten et al 1991][research_toten_fong_1991]\] \[[Mease and Vanburen 1989][research_measekennethd_vanburenmarka_1989]\] \[[Lu 1993][research_luping_1993]\] \[[Vaicaitis 1991][research_vaicaitis_1991]\] \[[Van Buren and Mease 1991][research_vanburen_mease_1991]\] \[[Waldman and Harsha 1992][research_waldman_harsha_1992]\] \[[West and Mitchell 1994][research_west_mitchell_1994]\] \[[Wierzbanowski and McCorry 1990][research_wierzbanowski_mccorry_1990]\] \[[Winkler and Bush 1992][research_winkler_bush_1992]\] \[[Wolf and Daum 1993][research_wolf_daum_1993]\] \[[Yamanaka 1992][research_yamanaka_1992]\] \[[Yaros 1991][research_yaros_1991]\] \[[Zagainov and Plokhikh 1991][research_zagainov_plokhikh_1991]\]

### Boundary-layer transition and instability

**Where the boundary layer becomes turbulent and why it matters for heating, drag and the inlet.** Instability, receptivity, roughness and the prediction of transition at hypersonic speed.

**137 records.** \[[Zhou et al 2018][research_zhou_zhao_2018]\] \[[Hodge 1976][research_hodge_1976]\] \[[Meng et al 2022][research_meng_shi_2022]\] \[[Griffith and Lewis 1963][research_griffith_lewis_1963]\] \[[Chou and Marineau 2023][research_amandachou_ericcmarineau_2024]\] \[[Zhou et al 2015][research_zhou_yan_2015]\] \[[Adams and John C. 1970][research_adams_johnc_1970]\] \[[Zhu et al 2018][research_zhu_chen_2018]\] \[[Tetervin 1961][research_tetervin_1961]\] \[[Menon et al 2025][research_menon_ck_2025]\] \[[Nie et al 2022][research_nie_song_2022]\] \[[Rouhi Youssefi and Knight 2017][research_rouhiyoussefi_knight_2017]\] \[[Bertelrud et al 1992][research_bertelrud_kolodziej_1992]\] \[[Qiu et al 2024][research_qiu_shi_2024]\] \[[Chen 1993][research_chen_1993]\] \[[Choudhari et al 2012][research_choudhari_tokugawa_2012]\] \[[Cohen and Reshotko 1956][research_cohen_reshotko_1956]\] \[[Ustinov and Kachanov 2021][research_ustinov_kachanov_2021]\] \[[Nagel 1967][research_nagel_1967]\] \[[Chen et al 2023][research_chen_guo_2023]\] \[[Oz and Kara 2024][research_oz_kara_2024]\] \[[Siddiqui et al 2023][research_siddiqui_ledbetter_2023]\] \[[Guo and Cao 2026][research_guo_cao_2026]\] \[[Craig and Saric 2016][research_craig_saric_2016]\] \[[Li and Su 2025][research_li_su_2025]\] \[[White and Sreenivasan 1998][research_white_sreenivasan_1998]\] \[[Tian et al 2022][research_tian_liu_2022]\] \[[Dunlap and Kuethe 1961][research_dunlap_kuethe_1961]\] \[[Yu 2024][research_yu_2024]\] \[[Zhang et al 2023][research_zhang_yi_2023]\] \[[Stainback 1969][research_stainbackpc_1969]\] \[[Maddalon 1969][research_maddalon_1969]\] \[[Fu and Hall 1993][research_fu_hall_1993]\] \[[Stilla 1994][research_stilla_1994]\] \[[Zhang 2020][research_zhang_2020]\] \[[Zhu 2019][research_zhu_2019]\] \[[Webber et al 2026][research_webber_reeves_2026]\] \[[Sha et al 2026][research_sha_long_2026]\] \[[Xu et al 2026][research_xu_zhu_2026]\] \[[Park et al 2026][research_park_kim_2026]\] \[[Zhang et al 2024][research_zhang_wu_2024]\] \[[Han and Cao 2019][research_han_cao_2019]\] \[[Ginoux 1966][research_ginoux_1966]\] \[[Loiseau et al 2015][research_loiseau_robinet_2015]\] \[[Ren et al 2019][research_ren_yuan_2019]\] \[[Zhao et al 2019][research_zhao_dong_2019]\] \[[Baughn et al 1987][research_baughn_hoffman_1987]\] \[[Jeffs et al 2026][research_jeffs_newton_2026]\] \[[Zhong 1998][research_zhong_1998]\] \[[Hoskin et al 2024][research_hoskin_nguyen_2024]\] \[[Gong et al 2026][research_gong_dong_2026]\] \[[Chen et al 2022][research_chen_chen_2022]\] \[[Gui et al 2022][research_gui_wang_2022]\] \[[He and Zhong 2021][research_he_zhong_2021]\] \[[Stetson 1986][research_stetson_1986]\] \[[Wood 1968][research_wood_1968]\] \[[Zhou et al 2016][research_zhou_yan_2016]\] \[[Zhou et al 2017][research_zhou_li_2017]\] \[[Hao et al 2017][research_hao_yan_2017]\] \[[Zhang et al 2023][research_zhang_chen_2023]\] \[[Li et al 2025][research_li_ji_2025]\] \[[Zhang et al 2020][research_zhang_li_2020]\] \[[Benard et al 1997][research_benard_gaillard_1997]\] \[[Kharitonov and Chernykh 1974][research_kharitonov_chernykh_1974]\] \[[Liu et al 2021][research_liu_wang_2021]\] \[[Tian and Liu 2026][research_tian_liu_2026]\] \[[Riley and McNamara 2017][research_riley_mcnamara_2017]\] \[[Huang 2021][research_huang_2021]\] \[[Chen et al 2017][research_chen_zhu_2017]\] \[[Yang et al 2024][research_yang_qiu_2024]\] \[[Kauffman et al 1990][research_kauffman_grandhi_1990]\] \[[Lees 1956][research_lees_1956]\] \[[Ge et al 2026][research_ge_zhu_2026]\] \[[Huang et al 2026][research_huang_chen_2026]\] \[[Reed 1990][research_reed_1990]\] \[[Moss et al 1987][research_mossjamesn_simmondsannl_1987]\] \[[Zhu 2022][research_zhu_2022]\] \[[Dong et al 2019][research_dong_liu_2019]\] \[[Liu et al 2023][research_liu_luo_2023]\] \[[Zhou et al 2016][research_zhou_zhao_2016]\] \[[Surzhikov 2019][research_surzhikov_2019]\] \[[Zhong 2009][research_zhong_2009]\] \[[Surzhikov 2022][research_surzhikov_2022]\] \[[Fasel et al 2011][research_fasel_gross_2011]\] \[[Holman 2023][research_holman_2023]\] \[[Johnson et al 1998][research_johnson_seipp_1998]\] \[[Zhao et al 2019][research_zhao_liu_2019]\] \[[Fu et al 1993][research_fu_hall_1993_b]\] \[[Masad 1995][research_masad_1995]\] \[[Ortloff 1968][research_ortloff_1968]\] \[[Schreck et al 1998][research_schreck_faller_1998]\] \[[Liu et al 2025][research_liu_yang_2025]\] \[[Peng and Wang 2026][research_peng_wang_2026]\] \[[Pisharoti and Brizzolara 2025][research_pisharoti_brizzolara_2025]\] \[[Kaul 1989][research_kaulupenderk_1989]\] \[[Potter and Whitfield 1957][research_potter_whitfield_1957]\] \[[Liu et al 2021][research_liu_xu_2021]\] \[[Zhao et al 2020][research_zhao_liu_2020]\] \[[Adams et al 1976][research_adamsjcjr_martindalewr_1976]\] \[[Niu and Su 2023][research_niu_su_2023]\] \[[Rhudy 1970][research_rhudy_1970]\] \[[Campbell et al 2010][research_campbellcharlesh_kingrudolpha_2010]\] \[[Haley and Zhong 2023][research_haley_zhong_2023]\] \[[Suryanarayanan et al 2019][research_suryanarayanan_goldstein_2019]\] \[[Nagamatsu et al 1964][research_nagamatsu_graber_1964]\] \[[Di Giovanni and Stemmer 2019][research_digiovanni_stemmer_2019_b]\] \[[Berger and White 2024][research_berger_white_2024]\] \[[Balakumar and Kegerise 2016][research_balakumar_kegerise_2016]\] \[[Li et al 2022][research_li_choudhari_2022]\] \[[Xu et al 2020][research_xu_liu_2020]\] \[[Song et al 2020][research_song_zhao_2020]\] \[[Wang et al 2018][research_wang_li_2018]\] \[[Schmidt and Patankar 1991][research_schmidt_patankar_1991]\] \[[Ghannadian et al 2024][research_ghannadian_gosse_2024]\] \[[Boscagli et al 2026][research_boscagli_rigas_2026]\] \[[Liu et al 2023][research_liu_dong_2023]\] \[[Uy et al 2023][research_uy_hao_2023]\] \[[Yang et al 2026][research_yang_gao_2026]\] \[[Stetson 1990][research_stetson_1990]\] \[[Willaime et al 1998][research_willaime_belin_1998]\] \[[Park and Park 2016][research_park_park_2016]\] \[[Surface Roughness Effects on 1973][research_surface_roughness_1973]\] \[[Yu and Yuan 2016][research_yu_yuan_2016]\] \[[Yin et al 2023][research_yin_jiang_2023]\] \[[Liu and Zhang 2019][research_liu_zhang_2019]\] \[[Preston 1958][research_preston_1958]\] \[[Whitfield and Potter 1959][research_whitfield_potter_1959]\] \[[Chen et al 2023][research_chen_chen_2023]\] \[[Zuo and Hu 2021][research_zuo_hu_2021]\] \[[Patrick 2019][research_patrick_2019]\] \[[Paredes et al 2020][research_paredes_venkatachari_2020]\] \[[Nance et al 1997][research_nancerobertp_horvaththomasj_1997]\] \[[Balakumar and Chou 2018][research_balakumar_chou_2018]\] \[[Hopkins and Keener 1968][research_hopkins_keener_1968]\] \[[Lange et al 1953][research_lange_gieseler_1953]\] \[[Isaac et al 1959][research_isaac_williams_1959]\] \[[Reed et al 2015][research_reed_perez_2015]\]

### Single-stage and two-stage to orbit

**Getting a single vehicle, or two, to orbit.** Single-stage and two-stage concepts, air-breathing launch vehicles, their sizing, mass budgets and ascent performance.

**119 records.** \[[Lovell and Schmidt 1994][research_lovelltalan_schmidtdk_1994]\] \[[Adams and Landrum 2001][research_adams_landrum_2001]\] \[[Wilhite et al 1991][research_wilhite_bush_1991]\] \[[Phillips and Engelund 1997][research_phillips_engelund_1997]\] \[[Landiech et al 1990][research_landiech_aumasson_1990]\] \[[Hunt 1995][research_huntjamesl_1995]\] \[[Allen et al 1994][research_allen_maughan_1994]\] \[[Shirasu et al 1996][research_shirasu_south_1996]\] \[[Beichel and Obrien 1978][research_beichel_obrien_1978]\] \[[Bekey 1994][research_bekey_1994]\] \[[Park et al 1996][research_park_menees_1996]\] \[[Bentley 2009][research_bentley_2009]\] \[[Biltgen et al 2004][research_biltgen_lafleur_2004]\] \[[Bonnefond et al 1996][research_bonnefond_falempin_1996]\] \[[Butrica 2003][research_butrica_2003]\] \[[Cazin 1989][research_cazin_1989]\] \[[Chase 1990][research_chase_1990]\] \[[Chase 1992][research_chase_1992]\] \[[Christophe 1992][research_christophe_1992]\] \[[Clapp and Hunter 1993][research_clapp_hunter_1993]\] \[[Conchie 1989][research_conchie_1989]\] \[[Labib and King 2015][research_labib_king_2015_b]\] \[[Dissel et al 2006][research_dissel_kothari_2006]\] \[[Dorrington 1999][research_dorrington_1999]\] \[[Limerick 1991][research_limerick_1991]\] \[[Beaurain et al 2003][research_beaurainandre_souchieralain_2003]\] \[[Edwards et al 2015][research_edwards_steffens_2015]\] \[[Huang et al 1998][research_huang_wang_1998]\] \[[Escher 2002][research_escher_2002]\] \[[Escher et al 1986][research_escher_teeter_1986]\] \[[Manski and Martin 1991][research_manski_martin_1991]\] \[[Walker 2025][research_walker_2025]\] \[[Future Perspectives of Airbreathing 2004][research_future_perspectives_2004]\] \[[Gregory and Wilcox 1970][research_gregory_wilcox_1970]\] \[[Gregory et al 1971][research_gregory_williams_1971]\] \[[Gregory et al 1994][research_gregory_bowles_1994]\] \[[Hamaker 1996][research_hamaker_1996]\] \[[Hames 1992][research_hames_1992]\] \[[Health monitoring and controls 1994][research_health_monitoring_1994]\] \[[Heiser 2010][research_heiser_2010]\] \[[Hermann and Schmidt 1995][research_hermann_schmidt_1995]\] \[[Martin 1995][research_martin_1995]\] \[[Hoegenauer and Koelle 1989][research_hoegenauer_koelle_1989]\] \[[Kramer and Buhler 1980][research_kramer_buhler_1980]\] \[[Weilmuenster et al 1996][research_weilmuenster_gnoffo_1996]\] \[[Jia et al 2020][research_jia_fu_2020_b]\] \[[Weilmuenster et al 1997][research_weilmuenster_gnoffo_1997]\] \[[Freeman and Powell 1980][research_freeman_powell_1980]\] \[[Labib and King 2015][research_labib_king_2015]\] \[[Froning 1988][research_froning_1988]\] \[[Jazra and Smart 2011][research_jazra_smart_2011]\] \[[Kauffman et al 1991][research_kauffman_grandhi_1991]\] \[[Krieger 1990][research_krieger_1990]\] \[[Landis and Denis 2003][research_landis_denis_2003]\] \[[Lederer et al 1991][research_lederer_schwab_1991]\] \[[Leng et al 2024][research_leng_wang_2024]\] \[[Lewis 2003][research_lewis_2003]\] \[[Lidke et al 1987][research_lidke_poulin_1987]\] \[[Limerick 1994][research_limerick_1994]\] \[[Maita et al 1990][research_maita_ohkami_1990]\] \[[Martin 1992][research_martin_1992]\] \[[Martin et al 1991][research_martin_kabis_1991]\] \[[Matsushima et al 1987][research_matsushima_takanashi_1987]\] \[[Mayhew and Norden 1995][research_mayhew_norden_1995]\] \[[McClure and Andrews 1998][research_mcclure_andrews_1998]\] \[[McCormick et al 2010][research_mccormick_wakayama_2010]\] \[[Mehta and Bowles 2001][research_mehta_bowles_2001]\] \[[Mendham 2003][research_mendham_2003]\] \[[Nadell et al 1992][research_nadellsharibeth_baumgartenwilliamj_1992_b]\] \[[Nadell et al 1992][research_nadellsharibeth_baumgartenwilliamj_1992]\] \[[Nguyen 1987][research_nguyen_1987]\] \[[Nguyen 1991][research_nguyen_1991]\] \[[Wang et al 2022][research_wang_wang_2022]\] \[[Wang et al 2023][research_wang_wang_2023]\] \[[Olds 1988][research_olds_1988]\] \[[Manski et al 1997][research_manski_hagemann_1997]\] \[[Wilhite 1983][research_wilhite_1983]\] \[[Plencner 1991][research_plencnerrobertm_1991]\] \[[Pamadi 1989][research_pamadi_1989]\] \[[Parsley 1989][research_parsley_1989]\] \[[Dorrington 1990][research_dorrington_1990]\] \[[Powell et al 1991][research_powell_shaughnessy_1991]\] \[[Powering the Future of 2022][research_powering_the_2022]\] \[[Brevault et al 2017][research_brevault_balesdent_2017]\] \[[Martin 1978][research_martin_1978]\] \[[Calise et al 1990][research_caliseaj_flandroga_1990]\] \[[Ricciardi 1991][research_ricciardi_1991]\] \[[Richard and Christophe 1995][research_richard_christophe_1995]\] \[[Andrews et al 1992][research_andrews_davis_1992]\] \[[Rothmund et al 1996][research_rothmund_scherrer_1996]\] \[[Schmidt and Schmidt 1997][research_schmidt_schmidt_1997]\] \[[Schmidt and Velapoldi 1996][research_schmidt_velapoldi_1996]\] \[[Schoettle and Hillesheimer 1991][research_schoettle_hillesheimer_1991]\] \[[Schoettle and Rahn 1993][research_schoettle_rahn_1993]\] \[[Shirasu et al 1996][research_shirasu_south_1996_b]\] \[[Pamadi 1995][research_pamadi_1995]\] \[[Single stage to orbit 1994][research_single_stage_1994]\] \[[Marchetti et al 2021][research_marchetti_minisci_2021]\] \[[Freeman et al 1995][research_freeman_stanley_1995]\] \[[Freeman et al 1996][research_freeman_talay_1996]\] \[[Kibbey 2019][research_kibbeytim_2019]\] \[[Smart and Tetlow 2006][research_smart_tetlow_2006]\] \[[Sponable 1995][research_sponable_1995]\] \[[Stanley et al 1991][research_stanley_wilhite_1991]\] \[[Stanley et al 1992][research_stanley_wilhite_1992]\] \[[Stephan and Schneider 1991][research_stephan_schneider_1991]\] \[[Tanatsugu and Carrick 2003][research_tanatsugu_carrick_2003]\] \[[MacLeod 2026][research_macleod_2026]\] \[[Yoon and Ahn 2016][research_yoon_ahn_2016]\] \[[Trefny 1999][research_trefny_1999]\] \[[Shaughnessy and Gregory 1991][research_shaughnessyjohnd_gregoryirenem_1991]\] \[[Goracke et al 1997][research_goracke_levack_1997]\] \[[Tsuchiya and Mori 2005][research_tsuchiya_mori_2005]\] \[[Wang and Wang 2024][research_wang_wang_2024_b]\] \[[Unsteady interaction mechanism of transverse stage separation...][research_unsteady_interaction_2023]\] \[[Whitehead 1996][research_whitehead_1996]\] \[[Wilhite 1991][research_wilhite_1991]\] \[[Wu 2026][research_wu_2026]\] \[[Yamanaka 1989][research_yamanaka_1989]\]

### Thermal protection, hot structures and aerothermoelasticity

**Keeping the airframe intact.** Thermal protection systems, hot and cooled structures, seals, thermal-structural testing and aerothermoelasticity.

**120 records.** \[[Hoter et al 2026][research_hoter_2026]\] \[[Munk et al 2016][research_munk_vio_2016]\] \[[Gao et al 2021][research_gao_gou_2021]\] \[[Luo et al 2026][research_luo_tang_2026]\] \[[Wang et al 2023][research_wang_xu_2023]\] \[[Huang and Yao 2020][research_huang_yao_2020]\] \[[DelCorso et al 2011][research_delcorsojosepha_cheatwoodfmcneil_2011]\] \[[Ardema 1995][research_ardemamarkd_1995]\] \[[Sudalagunta et al 2018][research_sudalagunta_sultan_2018]\] \[[Chen and Zhao 2019][research_chen_zhao_2019]\] \[[Chen et al 2018][research_chen_xu_2018]\] \[[Wan et al 2025][research_wan_ma_2025]\] \[[Huang et al 2019][research_huang_friedmann_2019]\] \[[Yi and Xie 2024][research_yi_xie_2024]\] \[[Huang and Friedmann 2020][research_huang_friedmann_2020]\] \[[Demange et al 2014][research_demangejeffreyj_taylorshawnc_2014]\] \[[Quan et al 2021][research_quan_xu_2021]\] \[[Ardema 1972][research_ardema_1972]\] \[[Lv et al 2015][research_lv_wang_2015]\] \[[Collier 1992][research_collier_1992]\] \[[Nasir et al 2026][research_nasir_xie_2026]\] \[[Wang et al 2019][research_wang_wang_2019]\] \[[Fasel et al 2020][research_fasel_keidel_2020]\] \[[Scotti 1992][research_scottistephenj_1992]\] \[[Glass et al][research_davideglass_bryanakubitschek]\] \[[Davis and Murrow 1989][research_davis_murrow_1989]\] \[[Thawait et al 2023][research_thawait_tandaiya_2023]\] \[[Xu et al 2019][research_xu_xu_2019]\] \[[Xue et al 2026][research_xue_li_2026]\] \[[Kumar and Mahulikar 2017][research_kumar_mahulikar_2017]\] \[[Kang et al 2018][research_kang_kim_2018]\] \[[Khan and Chakraborty 2023][research_khan_chakraborty_2023]\] \[[Daryabeigi et al 2006][research_daryabeigikamran_blossermaxl_2006]\] \[[Kim and Choi 2026][research_kim_choi_2026]\] \[[Raney et al 1993][research_raneydavidl_mcminnjohnd_1993]\] \[[McINTOSH 1973][research_mcintosh_1973]\] \[[Chen et al 2025][research_chen_yang_2025]\] \[[Xie et al 2020][research_xie_dong_2020]\] \[[Chinnaraj et al 2024][research_chinnaraj_kim_2024]\] \[[Daub et al 2022][research_daub_willems_2022]\] \[[Fields et al 2004][research_fields_richards_2004]\] \[[Freydin and Dowell 2021][research_freydin_dowell_2021]\] \[[Hunter et al 2002][research_hunterje_mccurdydr_2002]\] \[[Rong 2017][research_rong_2017]\] \[[Yang et al 2019][research_yang_li_2019]\] \[[Lemcoe 1992][research_lemcoemm_1992]\] \[[Holguin et al 2018][research_holguin_hudson_2018]\] \[[Hunt and Bohon 1974][research_hunt_bohon_1974]\] \[[Hypersonic Materials for Thermal Protection][research_hypersonic_materials_2023]\] \[[Resende 1993][research_resendehugob_1993]\] \[[Plank and Penning 1973][research_plankpp_penningfa_1973]\] \[[Zhu et al 2016][research_zhu_zhao_2016]\] \[[Liu et al 2002][research_liu_chen_2002]\] \[[Wang et al 2022][research_wang_zhang_2022]\] \[[Cui et al 2017][research_cui_zhao_2017]\] \[[Cerro and Shore 1990][research_jeffreyacerro_cpshore_1990]\] \[[Ikenson 2025][research_ikenson_2025]\] \[[Kehoe and Ricketts 1992][research_kehoe_ricketts_1992]\] \[[Kourtides 1993][research_kourtides_1993]\] \[[Kuranov et al 2012][research_kuranov_korabelnikov_2012]\] \[[Lear et al 2008][research_lear_mcgrath_2008]\] \[[Lei 1992][research_lei_1992]\] \[[Stewart and Leiser 2007][research_stewartdavid_leiserdaniel_2007]\] \[[Lisagor 1990][research_lisagor_1990]\] \[[Tenney et al 1989][research_darrelrtenney_wbarrylisagor_1989]\] \[[Tenney et al 1988][research_drtenney_wblisagor_1988]\] \[[Miller et al 1993][research_miller_steinetz_1993]\] \[[Xiaoxuan et al 2018][research_xiaoxuan_jinglong_2018]\] \[[Rodríguez-Segade et al 2024][research_rodriguezsegade_hernandez_2024]\] \[[Huang and Friedmann 2020][research_huang_friedmann_2020_b]\] \[[Resende 1991][research_resendehugob_1991]\] \[[Thawait et al 2023][research_thawait_tandaiya_2023_b]\] \[[Ye et al 2019][research_ye_ye_2019]\] \[[Xu and Wu 2018][research_xu_wu_2018]\] \[[Maiorova et al 2016][research_maiorova_prosuntsov_2016]\] \[[Yue et al 2018][research_yue_nie_2018]\] \[[Langston et al 2016][research_langstonsarahl_langchristapherg_2016]\] \[[Marley and Driscoll 2022][research_marley_driscoll_2022]\] \[[Swanson et al 2014][research_swansongreg_kazembacole_2014]\] \[[Swanson et al 2014][research_swansongregorytodd_cassellalanm_2014]\] \[[Li et al 2024][research_li_wang_2024_b]\] \[[Jing et al 2026][research_jing_song_2026]\] \[[Venegas et al 2026][research_venegas_huang_2026]\] \[[Wieting and Guy 1975][research_wietingar_guyrw_1975]\] \[[Feltrin et al 2025][research_feltrin_debona_2025]\] \[[Rasky 1993][research_rasky_1993]\] \[[Recent Advances in Structures for Hypersonic Flight, Part 1][research_recent_advances_1978]\] \[[Ji and Xie 2022][research_ji_xie_2022]\] \[[Hu and Mahadevan 2019][research_hu_mahadevan_2019]\] \[[Kerrebrock and Poferl 1984][research_kerrebrockjackl_poferldavidj_1984]\] \[[Ke et al 2025][research_ke_wang_2025]\] \[[Shore 1986][research_shorecharlesp_1986]\] \[[Barnett 1963][research_barnett_1963]\] \[[Rivers and Glass 2006][research_rivers_glass_2006]\] \[[Buschek and Calise 1993][research_buschekharald_caliseanthonyj_1993]\] \[[Scott 1993][research_scott_1993]\] \[[Scott and Pototzky 1993][research_scott_pototzky_1993]\] \[[Steinetz 2008][research_steinetzbrucem_2008]\] \[[Li et al 2024][research_li_wan_2024]\] \[[Vinson and Shore 1967][research_vinson_shore_1967]\] \[[Roche and Kosareo 2001][research_rochejosephm_kosareodanieln_2001]\] \[[Swanson et al 2015][research_swansongt_kazembacd_2015]\] \[[Yount et al 2012][research_yountbryanc_arnoldjameso_2012]\] \[[Camarda and Murrow 1990][research_camardacharlesj_murrowharoldn_1990]\] \[[Yang et al 2018][research_yang_gui_2018]\] \[[Taylor and Jackson 1980][research_taylor_jackson_1980]\] \[[McIntosh 1972][research_mcintoshscjr_1972]\] \[[Lerner and McIntosh 1968][research_lernerji_mcintoshscjr_1968]\] \[[Huang et al 2025][research_huang_li_2025]\] \[[Rajput et al 2026][research_rajput_soni_2026]\] \[[Aprovitola et al 2019][research_aprovitola_iuspa_2019]\] \[[Brune et al 2017][research_brune_hosder_2017]\] \[[Sun et al 2020][research_sun_yang_2020]\] \[[Feldman et al 2019][research_feldmanjay_stewartdavid_2019]\] \[[Tuttle and Rogacki 1991][research_tuttle_rogacki_1991]\] \[[Koch et al 2025][research_koch_wilken_2025]\] \[[Wang and Luo 2022][research_wang_luo_2022]\] \[[August and Joshi 1996][research_augustjamesa_joshishiv_1996]\] \[[Wieting and Guy 1976][research_wieting_guy_1976]\] \[[Williams et al 1996][research_williams_lei_1996]\]

### Titanium aluminides, intermetallics and titanium matrix composites

**The intermetallic and metal-matrix materials the programme developed.** Titanium aluminides, titanium matrix composites and related high-temperature alloys, their processing, fatigue and behaviour in hydrogen.

**110 records.** \[[Nicolaou and Semiatin 1997][research_nicolaou_semiatin_1997]\] \[[Lombard et al 1999][research_lombard_ghosh_1999]\] \[[Appel and Oehring 2003][research_appel_oehring_2003]\] \[[Nelson 1974][research_nelsonhg_1974]\] \[[Ball and Chan 1999][research_ball_chan_1999]\] \[[Beddoes 2018][research_beddoes_2018]\] \[[Bartolotta and Krause 2000][research_bartolottapaula_krausedavidl_2000]\] \[[Berton et al 1995][research_berton_surdon_1995]\] \[[Chaudhury and Zhao 1992][research_chaudhury_zhao_1992]\] \[[Clark et al 1992][research_clark_wallace_1992]\] \[[Clark et al 1994][research_clark_wallace_1994]\] \[[Jha et al 1991][research_jha_forster_1991]\] \[[Thompson et al 1996][research_thompson_chu_1996]\] \[[Compressive deformation of PM titanium aluminide at high...][research_compressive_deformation_1996]\] \[[Morris 1991][research_morris_1991]\] \[[Herrouin et al 1996][research_herrouin_bowen_1996]\] \[[Crystallographic and fracture behaviour 2009][research_crystallographic_and_2009]\] \[[Das 2000][research_das_2000]\] \[[Davidson 1996][research_davidson_1996]\] \[[Deformation of titanium aluminide 1998][research_deformation_of_1998]\] \[[Chan 1992][research_chan_1992]\] \[[Wallace et al 2003][research_wallaceta_birdrk_2003]\] \[[Dudzinski 2018][research_dudzinski_2018]\] \[[Dwivedi and Bradley 2010][research_dwivedi_bradley_2010]\] \[[Dary and Pollock 1996][research_dary_mpollock_1996]\] \[[Bird and Hoffman 1998][research_birdrkeith_hoffmanerick_1998]\] \[[Hoffmann et al 1989][research_hoffmannek_birdrk_1989]\] \[[Fabrication of titanium alloy 1992][research_fabrication_of_1992]\] \[[Fabrication of titanium matrix 2000][research_fabrication_of_2000]\] \[[Fogarty 1992][research_fogarty_1992]\] \[[Chan 1990][research_chan_1990]\] \[[Gabb and Gayda 1994][research_gabb_gayda_1994]\] \[[Gabb and Gayda 1996][research_gabb_gayda_1996]\] \[[Gao et al 1994][research_gao_zhao_1994]\] \[[Gaspar and Hackman 1991][research_gaspar_hackman_1991]\] \[[Ghonem 2000][research_ghonem_2000]\] \[[Ghonem and Osborne 1996][research_ghonem_osborne_1996]\] \[[Gooder and Mall 1995][research_gooder_mall_1995]\] \[[Griffin 2018][research_griffin_2018]\] \[[Harmon et al 1996][research_harmon_finefield_1996]\] \[[Herrmann and Hillberry 1997][research_herrmann_hillberry_1997]\] \[[High temperature compressive strength of titanium reinforced...][research_high_temperature_1993]\] \[[Subrahmanyam and Annapurna 1986][research_subrahmanyam_annapurna_1986]\] \[[Chung and Kim 1994][research_chung_kim_1994]\] \[[Mishra et al 1996][research_mishra_mukherjee_1996]\] \[[Masahashi et al 1991][research_masahashi_mizuhara_1991]\] \[[High temperature deformation properties of HIP processed...][research_high_temperature_1999]\] \[[High temperature hardness and oxidation resistance of...][research_high_temperature_1996]\] \[[Recina and Karlsson 1999][research_recina_karlsson_1999]\] \[[High temperature strength of nickel alloy reinforced with...][research_high_temperature_1996_b]\] \[[Nicolaou and Semiatin 1996][research_nicolaou_semiatin_1996]\] \[[Sabinash et al 1995][research_sabinash_sastry_1995]\] \[[Malakondaiah and Nicholas 1996][research_malakondaiah_nicholas_1996]\] \[[Hordon 1973][research_hordon_1973]\] \[[Holmquist et al 1998][research_holmquist_recina_1998]\] \[[Chu et al 1992][research_chu_thompson_1992]\] \[[Kobayashi et al 1990][research_kobayashi_yoshihara_1990]\] \[[Seetharaman and Semiatin 1996][research_seetharaman_semiatin_1996]\] \[[Johnson and Mirdamadi 1993][research_johnson_mirdamadi_1993]\] \[[Johnson and Mirdamadi 1994][research_johnson_mirdamadi_1994]\] \[[Johnson and Weeks 2005][research_johnson_weeks_2005]\] \[[Johnson et al 1996][research_johnson_mirdamadi_1996]\] \[[Kong et al 2024][research_kong_wang_2024]\] \[[Fritzemeier and Jacinto 1990][research_lgfritzemeier_majacinto_1990]\] \[[Laumakis and Bonacuse 2001][research_laumakis_bonacuse_2001]\] \[[Lisiecki 2015][research_lisiecki_2015]\] \[[Lissenden et al 2019][research_lissenden_yalcin_2019]\] \[[Liu and Liu 2015][research_liu_liu_2015]\] \[[Low cycle fatigue of 2000][research_low_cycle_2000]\] \[[Mall and Cunningham 2007][research_mall_cunningham_2007]\] \[[Marshall et al 1996][research_marshall_morris_1996]\] \[[Matikas 2008][research_matikas_2008]\] \[[Mechanical and oxidation properties 1995][research_mechanical_and_1995]\] \[[Method and titanium aluminide 1993][research_method_and_1993]\] \[[Method for forming titanium aluminide-ductile titanium...][research_method_for_1991]\] \[[Method for making a 1997][research_method_for_1997]\] \[[Method of fabricating titanium 1978][research_method_of_1978]\] \[[Method to fabricate titanium 1994][research_method_to_1994]\] \[[Method to produce metal 1990][research_method_to_1990]\] \[[Microstructural control of a titanium aluminide alloy][research_microstructural_control_1997]\] \[[Mirdamadi and Johnson 1994][research_mirdamadi_johnson_1994]\] \[[Dempers et al 1999][research_dempers_nikbin_1999]\] \[[Yao and Marck 1995][research_yao_marck_1995]\] \[[Osborne and Ghonem 2005][research_osborne_ghonem_2005]\] \[[Petukhov et al 2023][research_petukhov_kolchin_2023]\] \[[PM titanium technology for 2002][research_pm_titanium_2002]\] \[[Process for stabilisation of 1992][research_process_for_1992]\] \[[Rattray and Mall 1994][research_rattray_mall_1994]\] \[[Reisgen et al 2014][research_reisgen_olschok_2014]\] \[[Sawatzky 2018][research_sawatzky_2018]\] \[[Stickler and Keller 1998][research_stickler_keller_1998]\] \[[Structure and high temperature deformation behaviour of...][research_structure_and_1992]\] \[[Structure and properties of 1997][research_structure_and_1997]\] \[[Wisbey et al 1994][research_wisbey_kearns_1994]\] \[[Jobart et al 1994][research_jobart_blandin_1994]\] \[[Tsunekawa et al 1992][research_tsunekawa_gotoh_1992]\] \[[Kimura 1993][research_kimura_1993]\] \[[Synthesis of titanium aluminide-titanium 1994][research_synthesis_of_1994]\] \[[Holmquist et al 1999][research_holmquist_recina_1999]\] \[[Titanium Aluminide Intermetallics 2012][research_titanium_aluminide_2012]\] \[[Titanium aluminide made by sintering powder prepared by self...][research_titanium_aluminide_1992]\] \[[Gupta and Ramkumar 2015][research_gupta_ramkumar_2015]\] \[[Jones 2011][research_jones_2011]\] \[[Utilization of gas atomized 2001][research_utilization_of_2001]\] \[[Wadley et al 1990][research_wadley_elzey_1990]\] \[[Wisbey and Ward-Close 1997][research_wisbey_wardclose_1997]\] \[[Werner et al 2014][research_werner_smarsly_2014]\] \[[Wiezorek and Mills 1998][research_wiezorek_mills_1998]\] \[[Wright 1996][research_wright_1996]\] \[[Zhang et al 2019][research_zhang_niu_2019]\]

### Scramjet cycle analysis and engine performance

**The engine considered as a whole.** Scramjet and ramjet cycle analysis, engine performance, airframe and engine integration and the programmes that developed engines.

**107 records.** \[[99/00179 Performance analysis of hydrocarbon-fueled scramjet][research_99_00179_performance_1999]\] \[[Andrews and Mackley 1976][research_andrews_mackley_1976]\] \[[Das et al 2021][research_das_pandey_2021]\] \[[Sullins and Waltrup 1985][research_sullins_waltrup_1985]\] \[[A conceptual design of an unmanned test vehicle using an...][research_a_conceptual_1992]\] \[[Morris et al 1976][research_morrissjjr_nelmswpjr_1976]\] \[[Streby et al 1999][research_streby_mathur_1999]\] \[[Sandhu 2005][research_sandhu_2005]\] \[[Thelander 1966][research_thelander_1966]\] \[[Aerothermodynamics of Vehicle-Integrated Scramjet 2022][research_aerothermodynamics_of_2022]\] \[[Lloyd 1959][research_lloyd_1959]\] \[[Henderson 1991][research_henderson_1991]\] \[[Akpolat et al 2014][research_akpolat_toker_2014]\] \[[All a Matter of 2019][research_all_a_2019]\] \[[Walton 1990][research_waltonjt_1990]\] \[[Wang et al 2020][research_wang_cheng_2020]\] \[[Aslan et al 1990][research_aslan_bisard_1990]\] \[[Bao et al 2009][research_bao_qin_2009]\] \[[Bradford and Olds 1999][research_bradford_olds_1999]\] \[[Builder 1964][research_builder_1964]\] \[[Cavolowsky et al 1995][research_cavolowsky_loomis_1995]\] \[[Choi and Driscoll 2021][research_choi_driscoll_2021]\] \[[Choubey and Tiwari 2022][research_choubey_tiwari_2022]\] \[[Daines and Segal 1998][research_daines_segal_1998]\] \[[Anderson 1986][research_anderson_1986]\] \[[Yang et al 2015][research_yang_chang_2015]\] \[[Roundy 1979][research_roundy_1979]\] \[[Buchmann 1978][research_buchmannoa_1978]\] \[[Henry and Anderson 1973][research_henryjr_andersongy_1973]\] \[[Ford 1993][research_ford_1993]\] \[[Dhanasar et al 2019][research_dhanasar_ferguson_2019]\] \[[Diskin and Northam 1986][research_diskin_northam_1986]\] \[[Doherty 2015][research_doherty_2015]\] \[[Doherty et al 2012][research_doherty_smart_2012]\] \[[Doherty et al 2014][research_doherty_smart_2014]\] \[[Doherty et al 2015][research_doherty_smart_2015_b]\] \[[Doherty et al 2015][research_doherty_smart_2015]\] \[[Drummond et al 2006][research_drummond_bouchez_2006]\] \[[Edmonds et al 1964][research_edmonds_omoth_1964]\] \[[Emanuel 1989][research_emanuel_1989]\] \[[Davis and Harvey 1981][research_davis_harvey_1981]\] \[[Glassman and Nosek 1971][research_glassman_nosek_1971]\] \[[Glickstein and Powell 1987][research_glickstein_powell_1987]\] \[[Goel et al 2015][research_goel_xie_2015]\] \[[Hagenmaier et al 2013][research_hagenmaier_boles_2013]\] \[[Haiman and Karp 2026][research_haiman_karp_2026]\] \[[Koubek 1963][research_koubek_1963]\] \[[Chaney 1999][research_chaneysteve_1999]\] \[[Hutt et al 2001][research_hutt_mcarthur_2001]\] \[[Schrötter et al 2026][research_schrotter_kavas_2026]\] \[[Instrumentation for Airbreathing Propulsion 1974][research_instrumentation_for_1974]\] \[[Hunter and McCurdy 2003][research_hunterjamese_mccurdydavidr_2003]\] \[[Jalbert and Hiers 1993][research_jalbert_hiers_1993]\] \[[Kanda 2000][research_kanda_2000]\] \[[Leingang 1992][research_leingang_1992]\] \[[Liming and Bing 2006][research_liming_bing_2006]\] \[[Molvik et al 1992][research_molvik_bowles_1992]\] \[[Monteiro dos Santos Rodrigues da Silva and Leite 2025][research_monteirodossantosrodriguesdasilva_leite_2025]\] \[[Myrabo et al 1986][research_myrabo_powers_1986]\] \[[Ahuja and Hartfield 2015][research_ahuja_hartfield_2015]\] \[[Tsujikawa 1995][research_tsujikawa_1995]\] \[[Palaszewski 1998][research_palaszewski_1998]\] \[[Tsujikawa et al 1991][research_tsujikawa_tsukamoto_1991]\] \[[Lu et al 2024][research_lu_zhang_2024]\] \[[Pinckney 1978][research_pinckney_1978]\] \[[Aarnes and White 1975][research_aarnes_white_1975]\] \[[Mitani 1996][research_mitani_1996]\] \[[Quinn 1978][research_quinn_1978]\] \[[Guy et al 1996][research_rwguy_rcrogers_1996]\] \[[Besserer 1952][research_besserer_1952]\] \[[Wolf et al 1951][research_wolf_mullen_1951]\] \[[Longwell and Weiss 1952][research_longwell_weiss_1952]\] \[[Universal Technology Corp Dayton Oh 2014][research_universaltechnologycorpdaytonoh_2014]\] \[[Lv et al 2022][research_lv_chang_2022]\] \[[Chang and Yuan 2022][research_chang_yuan_2022]\] \[[Rom and Avital 1992][research_rom_avital_1992]\] \[[Roux 2011][research_roux_2011]\] \[[Roux et al 2013][research_roux_shakya_2013_b]\] \[[Roux et al 2014][research_roux_choi_2014]\] \[[Ryken and Davis 2004][research_ryken_davis_2004]\] \[[Sancho Ponce 2016][research_sanchoponce_2016]\] \[[Sato et al 1997][research_sato_izumikawa_1997]\] \[[Schunk and Chung 2000][research_schunk_chung_2000]\] \[[Scramjet 2015][research_scramjet_2015]\] \[[Leingang and Stull 1992][research_leingangjl_stullfd_1992]\] \[[Scramjet Developments in France 2001][research_scramjet_developments_2001]\] \[[Hunt and McClinton 1997][research_huntjamesl_mcclintoncharlesr_1997]\] \[[Scramjet Flowpath Integration 2001][research_scramjet_flowpath_2001]\] \[[Scramjet Performance 2001][research_scramjet_performance_2001]\] \[[Scramjet Research and Development 2001][research_scramjet_research_2001]\] \[[Thomas and Guy 1990][research_thomasscottr_guyrwayne_1990]\] \[[Universal Energy Systems Inc Dayton Oh 1995][research_universalenergysystemsincdaytonoh_1995]\] \[[Kerrebrock 1992][research_kerrebrock_1992]\] \[[Buehler and Lo 1981][research_buehlerrd_lore_1981]\] \[[Hite 1991][research_hitedale_1991]\] \[[Stull 1989][research_stull_1989]\] \[[Tanno et al 2001][research_tanno_komuro_2001]\] \[[Naval Ordnance Test Station China Lake Ca 1956][research_navalordnanceteststationchinalakeca_1957]\] \[[Zhang et al 2015][research_zhang_yang_2015]\] \[[Vanyai 2018][research_vanyai_2018]\] \[[Walton 1991][research_walton_1991]\] \[[Walton and Pinckney 1994][research_walton_pinckney_1994]\] \[[Waltrup et al 1996][research_waltrup_white_1996]\] \[[Whitehead 2007][research_whitehead_2007]\] \[[Whitside 2021][research_whitside_2021]\] \[[Xiao et al 2004][research_xiao_edwards_2004]\] \[[Zhang et al 2020][research_zhang_wang_2020_b]\]

### Trajectory, guidance and control of hypersonic vehicles

**Flying the corridor.** Trajectory optimisation, guidance and control of air-breathing and other hypersonic vehicles, including control in the presence of elastic and propulsive coupling.

**105 records.** \[[266 On ascent guidance of hypersonic vehicle][research_266_on_1994]\] \[[Ma and Cai 2018][research_ma_cai_2018]\] \[[Wu et al 2021][research_wu_deng_2021]\] \[[Wang et al 2020][research_wang_cheng_2020_b]\] \[[Zhang et al 2024][research_zhang_nie_2024]\] \[[Wu et al 2025][research_wu_yuan_2025]\] \[[Miao et al 2026][research_miao_wang_2026]\] \[[Tian and Shen 2022][research_tian_shen_2022]\] \[[Liu 2020][research_liu_2020]\] \[[Duan and Li 2015][research_duan_li_2015]\] \[[Fu et al 2019][research_fu_wang_2019]\] \[[Le et al 2023][research_le_liu_2023]\] \[[Austin 2024][research_austin_2024]\] \[[Wang and Zhang 2021][research_wang_zhang_2021]\] \[[Bulirsch and Chudej 1991][research_bulirsch_chudej_1991]\] \[[Chen et al 2020][research_chen_zhou_2020]\] \[[Chudej 1996][research_chudej_1996]\] \[[Zhang and Xian 2015][research_zhang_xian_2015]\] \[[Singh et al 2023][research_singh_prakash_2023]\] \[[Liu et al 2019][research_liu_tong_2019]\] \[[Bao et al 2023][research_bao_wang_2023]\] \[[Li et al 2015][research_li_song_2015]\] \[[Hu et al 2015][research_hu_deng_2015]\] \[[Zhou 2023][research_zhou_2023]\] \[[Dewell and Speyer 1993][research_dewell_speyer_1993]\] \[[Wang et al 2019][research_wang_guo_2019]\] \[[Disturbance Rejection For Airbreathing 2016][research_disturbance_rejection_2016]\] \[[Kumar et al 2018][research_kumar_sarkar_2018]\] \[[Shao et al 2015][research_shao_wang_2015]\] \[[Explicit Guidance Equations for a Variable Trim Reentry...][research_alexander_tm_1978]\] \[[Zhou et al 2024][research_zhou_fu_2024]\] \[[Song et al 2022][research_song_luo_2022]\] \[[Ferreira de Moura and Borges Ribeiro 2025][research_ferreirademoura_borgesribeiro_2025_d]\] \[[Ferreira de Moura and Borges Ribeiro 2025][research_ferreirademoura_borgesribeiro_2025_b]\] \[[Ferreira de Moura and Borges Ribeiro 2025][research_ferreirademoura_borgesribeiro_2025_c]\] \[[Ferreira de Moura and Borges Ribeiro 2025][research_ferreirademoura_borgesribeiro_2025]\] \[[Yao and Xia 2024][research_yao_xia_2024]\] \[[Zhang et al 2025][research_zhang_han_2025]\] \[[Li et al 2022][research_li_li_2022]\] \[[Liu et al 2023][research_liu_liu_2023]\] \[[Groves et al 2005][research_groves_serrani_2005]\] \[[Gupta 2022][research_gupta_2022]\] \[[Hattis and Malchow 1992][research_hattis_malchow_1992]\] \[[Song and Choi 2020][research_song_choi_2020]\] \[[Kumar et al 2018][research_kumar_penchalaiah_2018]\] \[[Naresh Kumar et al 2017][research_nareshkumar_ikram_2017]\] \[[Gregory et al 1992][research_gregoryirenem_chowdhryrajivs_1992]\] \[[Gregory et al 1993][research_gregoryirenem_mcminnjohnd_1993]\] \[[Gregory et al 1994][research_gregoryirenem_chowdhryrajivs_1994]\] \[[Chen et al 2017][research_chen_hu_2017]\] \[[Wang et al 2018][research_wang_hou_2018]\] \[[Wang et al 2026][research_wang_cheng_2026]\] \[[Shou et al 2023][research_shou_yan_2023]\] \[[Bao et al 2021][research_bao_wang_2021]\] \[[Liu et al 2024][research_liu_lu_2024]\] \[[Yu et al 2026][research_yu_wang_2026]\] \[[Rataczak et al 2024][research_rataczak_chaudhry_2024]\] \[[Maisaia 2023][research_maisaia_2023]\] \[[Mease and Vinh 1988][research_mease_vinh_1988]\] \[[Zhang et al 2023][research_zhang_zhang_2023]\] \[[Tsentis et al 2021][research_tsentis_gkoutzamanis_2021]\] \[[Murillo 2018][research_murillo_2018]\] \[[Murillo and Lu 2010][research_murillo_lu_2010]\] \[[Xia et al 2020][research_xia_chen_2020]\] \[[Zhang and Ding 2023][research_zhang_ding_2023]\] \[[Olds and Budianto 1998][research_olds_budianto_1998]\] \[[Grimm 1992][research_grimm_1992]\] \[[Pei et al 2021][research_pei_fan_2021]\] \[[ul Islam Rizvi et al 2015][research_ulislamrizvi_linshu_2015]\] \[[Ouzts et al 2009][research_ouzts_soloway_2009]\] \[[Dongre 2024][research_dongre_2024]\] \[[Zhai and Yang 2020][research_zhai_yang_2020]\] \[[Sheng et al 2023][research_sheng_gan_2023]\] \[[Yao and Xia 2023][research_yao_xia_2023]\] \[[Cui et al 2025][research_cui_zhen_2025]\] \[[Xu et al 2025][research_xu_liao_2025]\] \[[Lu and Zhou 2017][research_lu_zhou_2017]\] \[[Wei et al 2018][research_wei_liu_2018]\] \[[Dong and Cai 2017][research_dong_cai_2017]\] \[[Mao et al 2016][research_mao_zhang_2016]\] \[[Su et al 2024][research_su_zhao_2024]\] \[[Dai et al 2026][research_dai_cai_2026]\] \[[Ding et al 2022][research_ding_yue_2022]\] \[[Zong et al 2015][research_zong_wang_2015]\] \[[Fu et al 2015][research_fu_wang_2015]\] \[[Wang et al 2025][research_wang_yang_2025]\] \[[Gao et al 2015][research_gao_lin_2015]\] \[[Sun et al 2024][research_sun_jing_2024]\] \[[Ma and Cai 2018][research_ma_cai_2018_b]\] \[[Starkey et al 2006][research_starkey_rankins_2006]\] \[[Cai and Huang 2022][research_cai_huang_2022]\] \[[Supersonic and Hypersonic Flight Dynamics Realization for the...][research_supersonic_and_2019]\] \[[Li et al 2022][research_li_wang_2022]\] \[[Wang and Zhang 2018][research_wang_zhang_2018]\] \[[Li et al 2016][research_li_yang_2016]\] \[[Zhang et al 2018][research_zhang_wang_2018]\] \[[Hongbo and Yongyuan 2016][research_hongbo_yongyuan_2016]\] \[[Rizvi et al 2017][research_rizvi_linshu_2017]\] \[[Ma et al 2024][research_ma_yang_2024]\] \[[Li et al 2024][research_li_zeng_2024]\] \[[Wang et al 2026][research_wang_guo_2026]\] \[[Williams et al 2017][research_williams_mall_2017]\] \[[Karasopoulos and Langan 1992][research_karasopoulos_langan_1992]\] \[[Yang and Sun 2011][research_yang_sun_2011]\] \[[Zhang et al 2018][research_zhang_chen_2018]\]

### Detonation engines

**Combustion in a detonation wave rather than a flame.** Rotating, pulse and oblique detonation engines and their performance.

**93 of these 98 records date from 2015 or later.** **3 of these 98 records date from before 2000**, so the subject barely existed while the programme ran.

**98 records.** \[[3D Problems of Rotating Detonation Wave in a Ramjet Engine...][research_3d_problems_2018]\] \[[Lv et al 2026][research_lv_li_2026]\] \[[Veeramanikandan 2023][research_veeramanikandan_2023]\] \[[Eidelman et al 2000][research_eidelman_sharov_2000]\] \[[Perkowski et al 2024][research_perkowski_bilar_2024]\] \[[Analysis of Rotating Detonation Wave Engine][research_analysis_of_2023]\] \[[Kanda and Inagaki 2024][research_kanda_inagaki_2024]\] \[[Bedick et al 2019][research_bedick_ferguson_2019]\] \[[Debnath and Pandey 2015][research_debnath_pandey_2015]\] \[[Coupling study of supersonic turbine stage and...][research_coupling_study_2023]\] \[[Sato and Raman 2020][research_sato_raman_2020]\] \[[Jo and Choi 2026][research_jo_choi_2026]\] \[[Kawalec et al 2023][research_kawalec_wolanski_2023]\] \[[Ramanujachari and Amrutha Preethi 2023][research_ramanujachari_amruthapreethi_2023]\] \[[Chen et al 2021][research_chen_fan_2021]\] \[[Effects of different physical properties of anthracite powder...][research_effects_of_2023]\] \[[Han et al 2026][research_han_tian_2026]\] \[[Koo et al 2023][research_koo_lee_2023]\] \[[Yan et al 2021][research_yan_teng_2021]\] \[[Silva and Brójo 2026][research_silva_brojo_2026]\] \[[Effects of Various Compositions of the Fuel-Air Mixture on...][research_effects_of_2019]\] \[[Xiao et al 2024][research_xiao_lu_2024]\] \[[Cuppoletti et al 2019][research_cuppoletti_ombrello_2019]\] \[[Paudel and McFarland 2025][research_paudel_mcfarland_2025]\] \[[Dunn et al 2021][research_dunn_malik_2021]\] \[[Han et al 2021][research_han_lee_2021]\] \[[Md Salleh 2026][research_mdsalleh_2026]\] \[[Yang et al 2023][research_yang_song_2023]\] \[[Fotia et al 2016][research_fotia_schauer_2016]\] \[[Li et al 2024][research_li_li_2024]\] \[[Assad et al 2026][research_assad_pisarev_2026]\] \[[Tobias and Agrawal 2023][research_tobias_agrawal_2023]\] \[[Flow Dynamics and Design Optimization of Rotating Detonation...][research_flow_dynamics_2025]\] \[[Joshi and Lu 2017][research_joshi_lu_2017]\] \[[Flow-field reconstruction in rotating detonation combustor...][research_flow_field_reconstruction_2023]\] \[[Murray et al 2021][research_murray_smith_2021]\] \[[Tsuboi et al 2017][research_tsuboi_eto_2017]\] \[[Gray et al 2024][research_gray_mcloughlin_2024]\] \[[Grady and Madzsar 1998][research_grady_madzsar_1998]\] \[[Cuppoletti et al 2020][research_cuppoletti_ombrello_2020]\] \[[Wang et al 2016][research_wang_zhang_2016]\] \[[Yoshida et al 2019][research_yoshida_micci_2019]\] \[[Lu et al 2025][research_lu_zhu_2025]\] \[[Rong et al 2023][research_rong_cheng_2023]\] \[[Tharakan and Sukesh 2025][research_tharakan_sukesh_2025]\] \[[Jiang 2014][research_jiang_2014]\] \[[Jiang and Yu 2015][research_jiang_yu_2015]\] \[[Van Beck and Raman 2024][research_vanbeck_raman_2024]\] \[[Johnson May et al 2024][research_johnsonmay_weber_2024]\] \[[Mizener and Lu 2017][research_mizener_lu_2017]\] \[[Luo et al 2019][research_luo_wang_2019]\] \[[Wu et al 2026][research_wu_gao_2026]\] \[[Smirnov et al 2023][research_smirnov_nikitin_2023]\] \[[Voronin 2020][research_voronin_2020]\] \[[Carrier et al 1995][research_carrier_fendell_1995]\] \[[Subramanian and Meadows 2020][research_subramanian_meadows_2020]\] \[[Li et al 2022][research_li_xu_2022]\] \[[Pallela and Thakur 2025][research_pallela_thakur_2025]\] \[[Han et al 2024][research_han_bian_2024]\] \[[Alam et al 2019][research_alam_sharma_2019]\] \[[Gwak et al 2016][research_gwak_lee_2016]\] \[[Chen et al 2023][research_chen_si_2023]\] \[[Xu et al 2025][research_xu_han_2025]\] \[[Kocaaslan 2024][research_kocaaslan_2024]\] \[[Luo et al 2020][research_luo_wang_2020]\] \[[Gidaspov and Kononov 2019][research_gidaspov_kononov_2019]\] \[[Banagiri et al 2025][research_banagiri_raj_2025]\] \[[Yi et al 2020][research_yi_lou_2020]\] \[[Shi et al 2023][research_shi_fan_2023]\] \[[Yao et al 2017][research_yao_tang_2017]\] \[[Hayashi et al 2020][research_hayashi_tsuboi_2020]\] \[[Li et al 2026][research_li_pang_2026]\] \[[Ji et al 2019][research_ji_zhang_2019]\] \[[Sun et al 2018][research_sun_zhou_2018]\] \[[Burke and Rezzag 2026][research_burke_rezzag_2026]\] \[[Kanda et al 2020][research_kanda_katano_2020]\] \[[Yokoo et al 2020][research_yokoo_goto_2020]\] \[[Sharma and Saluti 2025][research_sharma_saluti_2025]\] \[[Research on the Combustion Mode and Thrust Performance of...][research_research_on_2024]\] \[[Gupta and Schwer 2018][research_gupta_schwer_2018]\] \[[Stechmann et al 2019][research_stechmann_heister_2019]\] \[[Driscoll et al 2015][research_driscoll_stoddard_2015]\] \[[Shen et al 2022][research_shen_ma_2022]\] \[[Jiang 2023][research_jiang_2023]\] \[[Fievisohn and Yu 2017][research_fievisohn_yu_2017]\] \[[Zhang et al 2020][research_zhang_qiao_2020]\] \[[James and Agrawal 2026][research_james_agrawal_2026]\] \[[Mohamad et al 2024][research_mohamad_ivan_2024]\] \[[Adelman et al 1996][research_adelmanhenryg_meneesgenep_1996]\] \[[Qin et al 2026][research_qin_zhang_2026]\] \[[Kaemming et al 2017][research_kaemming_fotia_2017]\] \[[Alam et al 2019][research_alam_sharma_2019_b]\] \[[Zangiev et al 2016][research_zangiev_ivanov_2016]\] \[[Amrutha Preethi and Ramanujachari 2020][research_amruthapreethi_ramanujachari_2020]\] \[[Joshi and Lu 2016][research_joshi_lu_2016]\] \[[Zheng and Wang 2018][research_zheng_wang_2018]\] \[[Ayers et al 2023][research_ayers_athmanathan_2023]\] \[[Allen 2021][research_allen_2021]\]

### Hydrogen fuel, slush hydrogen and tankage

**The fuel and where it is kept.** Slush and liquid hydrogen, their production, transfer and instrumentation, cryogenic tankage and the effect of hydrogen on structural materials.

**98 records.** \[[Fesmire et al 2021][research_fesmire_2021]\] \[[Pirrello et al 1976][research_pirrellocj_bakerah_1976]\] \[[Stone 1975][research_stoneje_1975]\] \[[A study of hydrogen 1967][research_a_study_1967]\] \[[Sindt 1970][research_sindt_1970]\] \[[Akyurtlu and Akyurtlu 1991][research_akyurtlu_akyurtlu_1991]\] \[[Vigilante et al 1997][research_vigilante_cote_1997]\] \[[Ohira et al 1994][research_ohira_matsuo_1994]\] \[[Alipour Bonab and Yazdani-Asrami 2025][research_alipourbonab_yazdaniasrami_2025]\] \[[Atanacio 2000][research_atanacio_2000]\] \[[Birnbaum 1989][research_birnbaum_1989]\] \[[Brunnhofer et al 2006][research_brunnhofer_sirbiparagina_2006]\] \[[Cady and Kendle 1971][research_cady_kendle_1971]\] \[[Cady and Kendle 1972][research_cady_kendle_1972]\] \[[Carney 1964][research_carney_1964]\] \[[Casali et al 2001][research_casali_gamma_2001]\] \[[Rivers 1999][research_rivershkevin_1999]\] \[[Cook and Dwyer 1966][research_cook_dwyer_1966]\] \[[Crivellari et al 1999][research_crivellari_de_1999]\] \[[Gu and Timmerhaus 1992][research_gu_timmerhaus_1992]\] \[[Daney 1968][research_daney_1968]\] \[[Daney et al 1968][research_daney_sindt_1968]\] \[[Bhat et al 1993][research_bhatbn_mcphersonwb_1993]\] \[[Elrod 1965][research_elrod_1965]\] \[[Ferretto et al 2022][research_ferretto_fusaro_2022]\] \[[Fischer and Hausrath 1966][research_fischer_hausrath_1966]\] \[[Fujiwara 1998][research_fujiwara_1998]\] \[[Singh et al 1992][research_singh_shen_1992]\] \[[Goff et al 2026][research_goff_wray_2026]\] \[[Gursu et al 1994][research_gursu_sheriff_1994]\] \[[Hall et al 1964][research_hall_hildebrand_1964]\] \[[Handbook of physical and 1967][research_handbook_of_1967]\] \[[Hardy and Whalen 1991][research_hardy_whalen_1991]\] \[[Hardy and Whalen 1992][research_hardy_whalen_1992]\] \[[Hartwig et al 2016][research_hartwig_rame_2016]\] \[[Helenbrook and Colt 1977][research_helenbrook_colt_1977]\] \[[Ho and Rahman 2005][research_ho_rahman_2005]\] \[[Horsley et al 1990][research_horsley_kroenke_1990]\] \[[Nelson 1988][research_nelsonhowardg_1988]\] \[[Rez 2021][research_rez_2021]\] \[[Mandel et al 1977][research_mandelg_carpenterjljr_1977]\] \[[Carpenter and Stuhrke 1976][research_carpenterjljr_stuhrkewf_1976]\] \[[Gopalasingam et al 2025][research_gopalasingam_rakhshani_2025]\] \[[Hydrogen Slush 2007][research_hydrogen_slush_2007]\] \[[Izenson 1991][research_izenson_1991]\] \[[Johnson 1967][research_johnson_1967]\] \[[Kocher and Keller 1969][research_kocher_keller_1969]\] \[[Lee et al 2021][research_lee_ryu_2021]\] \[[Hammond 1966][research_hammondmbjr_1966]\] \[[MacDermott et al 1965][research_macdermott_dix_1965]\] \[[Marshall 1969][research_marshall_1969]\] \[[Matveev and Leachman 2023][research_matveev_leachman_2023]\] \[[Matveev and Leachman 2023][research_matveev_leachman_2023_b]\] \[[NBS Probes Hydrogen Slush 1965][research_nbs_probes_1965]\] \[[Ohira 2002][research_ohira_2002]\] \[[Ohira 2004][research_ohira_2004]\] \[[Ohira 2016][research_ohira_2016]\] \[[Park 2010][research_park_2010]\] \[[Park et al 2022][research_park_lee_2022]\] \[[Payne 1968][research_payne_1968]\] \[[Sharpe and Jackson 1975][research_sharpeel_jacksonlr_1975]\] \[[Gray et al 1975][research_grayhr_nelsonhg_1975]\] \[[Rapial 1969][research_rapial_1969]\] \[[Bodan-Sanders and Bouvier 1998][research_bodansanderspatricia_bouviercarl_1998]\] \[[Roder 1977][research_roder_1977]\] \[[Rokaw and Getchell 1996][research_rokaw_getchell_1996]\] \[[Stephens 1974][research_stephensjr_1974]\] \[[Schalla 1967][research_schalla_1967]\] \[[Sindt 1969][research_sindt_1969]\] \[[Sindt 1972][research_sindt_1972_c]\] \[[Sindt 1972][research_sindt_1972]\] \[[Sindt 1972][research_sindt_1972_b]\] \[[Sindt 1995][research_sindt_1995]\] \[[Sindt and Ludtke 1973][research_sindt_ludtke_1973]\] \[[Sindt and Ludtke 1995][research_sindt_ludtke_1995]\] \[[Kumakawa 1989][research_kumakawa_1989]\] \[[Smith 1989][research_smith_1989]\] \[[Slush hydrogen production, storage 1966][research_slush_hydrogen_1966]\] \[[Slush Hydrogen Storage 2014][research_slush_hydrogen_2014]\] \[[Corrington et al 1956][research_corringtonlc_henningsg_1956]\] \[[Stewart 2017][research_stewart_2017]\] \[[Ruscigno 1965][research_ruscignoh_1965]\] \[[Ohira 1999][research_ohira_1999]\] \[[Su 2017][research_su_2017]\] \[[Superconducting liquid-level sensor for slush hydrogen use][research_superconducting_liquid_level_1967]\] \[[Gray 1978][research_grayhr_1978]\] \[[Cowgill and Johnson 1971][research_cowgillgr_johnsonwr_1971]\] \[[Wang et al 2007][research_wangxiaoyen_harpstergeorge_2007]\] \[[Johnson et al 1998][research_johnsontheodoref_natividadroderick_1998]\] \[[Johnson et al 2005][research_johnsontheodoref_natividadroderick_2005]\] \[[Voth and Ludtke 1979][research_voth_ludtke_1979]\] \[[Wang et al 2025][research_wang_jordan_2025]\] \[[Whalen and Hardy 1992][research_whalen_hardy_1992]\] \[[Whalen et al 1993][research_whalen_hardy_1993]\] \[[Xia et al 2023][research_xia_li_2023]\] \[[Xia et al 2023][research_xia_li_2023_b]\] \[[Yates 1967][research_yates_1967]\] \[[Yin and He 2023][research_yin_he_2023]\]

### Real-gas, nonequilibrium and rarefied hypersonic flow

**Air that no longer behaves as an ideal gas.** Dissociation, nonequilibrium, ionisation and rarefied flow at the conditions the X-30 was meant to reach.

**96 records.** \[[Lumpkin and Chapman 1992][research_lumpkin_chapman_1992]\] \[[Polyanskii 1967][research_polyanskii_1967]\] \[[Tolstykh 1969][research_tolstykh_1969]\] \[[Ladyzhenskii and Lipin 1966][research_ladyzhenskii_lipin_1966]\] \[[Zhang et al 2025][research_zhang_zhang_2025]\] \[[Kim 2018][research_kim_2018]\] \[[Lebedev et al 1969][research_lebedev_minostsev_1969]\] \[[Archer 1963][research_archer_1963]\] \[[Boyd 1990][research_boydiaind_1990]\] \[[Behrenbrinker et al 2025][research_behrenbrinker_guo_2025]\] \[[Borrelli and Pandolfi 1991][research_borrelli_pandolfi_1991]\] \[[Boylan 1965][research_boylan_1965]\] \[[Chambers Jr 2007][research_chambersjr_2007]\] \[[Pearson 1967][research_pearsonwe_1967]\] \[[Chapter 9 Model of 2013][research_chapter_9_2013]\] \[[Chinnappan and Kim 2026][research_chinnappan_kim_2026]\] \[[Clarey and Greendyke 2018][research_clarey_greendyke_2018]\] \[[Klothakis and Nikolos 2024][research_klothakis_nikolos_2024_b]\] \[[Danberg 1961][research_danberg_1961]\] \[[De Marchi Poltronieri et al 2025][research_demarchipoltronieri_moreira_2025]\] \[[Klothakis and Nikolos 2024][research_klothakis_nikolos_2024]\] \[[Epstein 1961][research_epstein_1961]\] \[[Edwards 1992][research_edwards_1992]\] \[[Golubkin 1978][research_golubkin_1978]\] \[[Erdman 2004][research_erdman_2004]\] \[[Sai Prakash et al 2026][research_saiprakash_raghav_2026]\] \[[Savel'ev and Stepanov 1988][research_savelev_stepanov_1988]\] \[[Fratini and Bernardini 2026][research_fratini_bernardini_2026]\] \[[Froning 2002][research_froning_2002]\] \[[Gaitonde and Lindsey 2006][research_gaitonde_lindsey_2006]\] \[[Haas et al 1994][research_haas_milos_1994]\] \[[Ivanov et al 1998][research_ivanov_markelov_1998]\] \[[Horstman 1969][research_horstman_1969]\] \[[Montagne et al 1988][research_montagnejl_yeehc_1988]\] \[[Ragnoli et al 2024][research_ragnoli_savino_2024]\] \[[Goldman 1958][research_goldman_1958]\] \[[Hermann and Thoenes 1965][research_hermannr_thoenesj_1965]\] \[[Maus et al 1984][research_maus_griffith_1984]\] \[[McGrory 2001][research_mcgrory_2001]\] \[[Hermann 1965][research_hermannr_1965]\] \[[Sugavanam and Sastry 1975][research_sugavanam_sastry_1975]\] \[[Gnoffo 1993][research_gnoffopetera_1993]\] \[[Han et al 2024][research_han_ma_2024]\] \[[Inviscid High-Temperature Equilibrium Flows 2006][research_inviscid_high_temperature_2006]\] \[[Karpenko et al 2023][research_karpenko_tolstoguzov_2023]\] \[[Kumar and Rana 2024][research_kumar_rana_2024]\] \[[Kumar and Ranjan 2026][research_kumar_ranjan_2026_b]\] \[[Kumar and Ranjan 2026][research_kumar_ranjan_2026_c]\] \[[Kumar and Ranjan 2026][research_kumar_ranjan_2026]\] \[[Lenard et al 1962][research_lenard_long_1962]\] \[[Kaskan and Reuther 1977][research_kaskan_reuther_1977]\] \[[Schouler et al 2023][research_schouler_prevereaud_2023]\] \[[Mehta et al 2001][research_mehtaunmeelb_bogdanoffdavidw_2001]\] \[[Miró Miró and Pinna 2017][research_miromiro_pinna_2017]\] \[[Nidharia et al 2024][research_nidharia_mane_2024]\] \[[Non-empirical analytical model of 2019][research_non_empirical_analytical_2019]\] \[[He et al 2023][research_he_sun_2023]\] \[[Han et al 2026][research_han_cheng_2026]\] \[[Ball and Lyon 1966][research_ballwh_lyonfj_1966]\] \[[Kianvashrad and Knight 2019][research_kianvashrad_knight_2019]\] \[[Park 1989][research_parkchul_1989]\] \[[Melnik and Perini 1968][research_melnikwl_perinill_1968]\] \[[Pu et al 2026][research_pu_xu_2026]\] \[[Kang 1970][research_kang_1970]\] \[[Zhivotov 1996][research_zhivotov_1996]\] \[[Han et al 2020][research_han_lee_2020]\] \[[Mei et al 2020][research_mei_shi_2020]\] \[[Gokul and Malaikannan 2025][research_gokul_malaikannan_2025]\] \[[Prabhu and Tannehill 1984][research_prabhudk_tannehilljc_1984]\] \[[Rahmani and Hejranfar 2021][research_rahmani_hejranfar_2021]\] \[[Park et al 2000][research_park_mehta_2000]\] \[[Park et al 2000][research_park_bogdanoff_2000]\] \[[Li et al 2022][research_li_cao_2022]\] \[[Perrel and Lafon 1992][research_perrel_lafon_1992]\] \[[Tong et al 2025][research_tong_li_2025]\] \[[Bond 1958][research_bond_1958]\] \[[Problem of Hypersonic Flow 2001][research_problem_of_2001]\] \[[Nagamatsu et al 1960][research_nagamatsu_geiger_1960]\] \[[Subramanian and Dwarakanath 1969][research_subramanian_dwarakanath_1969]\] \[[Malik and Anderson 1991][research_malik_anderson_1991]\] \[[Griffith 1958][research_griffith_1958]\] \[[Riggins 2002][research_riggins_2002]\] \[[Boyd 1989][research_boydiaind_1989]\] \[[Ding et al 2025][research_ding_liu_2025]\] \[[Sharma 1987][research_sharma_1987]\] \[[Sims and Hahn 1964][research_sims_hahn_1964]\] \[[Suresh and Liou 1992][research_suresh_liou_1992]\] \[[Stolzenburg 1965][research_stolzenburg_1965]\] \[[Lillard et al 2011][research_lillardrandolphp_oliverabrandon_2011]\] \[[Fomichev and Yadrenkin 2017][research_fomichev_yadrenkin_2017]\] \[[Jiang et al 2022][research_jiang_liu_2022]\] \[[Litchford et al 2000][research_litchfordrj_colejw_2000]\] \[[Litchford et al 1999][research_litchfordronj_bityurinvalentinea_1999]\] \[[Kim et al 2025][research_kim_park_2025]\] \[[Wada 2026][research_wada_2026]\] \[[Woods et al 1983][research_woods_arrington_1983]\]

### Computation, validation and uncertainty

**Computation as a substitute for the facility.** Computational fluid dynamics for hypersonic flow, its validation, its uncertainty and the surrogate and learned models that have joined it.

**92 records.** \[[Baurle and White 2022][research_baurle_white_2022]\] \[[Bu and Lei 2018][research_bu_lei_2018]\] \[[Chen and Fan 2025][research_chen_fan_2025]\] \[[Ispir et al 2023][research_ispir_saracoglu_2023]\] \[[Liu et al 2022][research_liu_yuan_2022]\] \[[Maccormack and Candler 1988][research_maccormackrobertw_candlergrahamv_1988]\] \[[Narayan and Kumar 1989][research_narayanjr_kumara_1989]\] \[[Ghioldi and Piscaglia 2023][research_ghioldi_piscaglia_2023]\] \[[Hu et al 2023][research_hu_cheng_2023]\] \[[Yang 2026][research_yang_2026]\] \[[Zheng et al 2025][research_zheng_huang_2025]\] \[[Povinelli 1989][research_povinellilouisa_1989]\] \[[Harish and Shabaz 2016][research_harish_shabaz_2016]\] \[[Mohring et al 2021][research_mohring_gabler_2021]\] \[[Povinelli 1991][research_povinellilouisa_1991]\] \[[Pavlov and Istomin 2023][research_pavlov_istomin_2023]\] \[[Li et al 2025][research_li_wang_2025]\] \[[Knight 2015][research_knight_2015]\] \[[Roche et al 2026][research_roche_breil_2026]\] \[[Baganoff 1990][research_baganoff_1990]\] \[[Li et al 2022][research_li_chen_2022]\] \[[Bruno 2023][research_bruno_2023_b]\] \[[Duncan 1991][research_duncanbeverly_1991]\] \[[Gupta and Venuprasad 2018][research_gupta_venuprasad_2018]\] \[[Edwards 1992][research_edwardsta_1992]\] \[[Povinelli 1990][research_povinellilouisa_1990]\] \[[Gupta et al 2022][research_gupta_ashokkumar_2022]\] \[[Paynter 1988][research_paynter_1988]\] \[[Davis 2015][research_davisdavido_2015]\] \[[Jun et al 2026][research_jun_yang_2026]\] \[[Jung et al 2017][research_jung_han_2017]\] \[[Chitsomboon 1992][research_chitsomboon_1992]\] \[[Kirsch et al 2025][research_kirsch_krueger_2025]\] \[[Arora et al 2025][research_arora_srivastava_2025]\] \[[Watkins 1990][research_watkinswilliamb_1990]\] \[[Mathur and Singh 2024][research_mathur_singh_2024]\] \[[Hsu and Liou 1991][research_hsu_liou_1991]\] \[[Candler and Leyva 2022][research_candler_leyva_2022]\] \[[Dwoyer 1987][research_dwoyerdouglasl_1987]\] \[[Yatsukhno 2018][research_yatsukhno_2018]\] \[[Covell et al 1988][research_covellpeterf_woodrichardm_1988]\] \[[Lan et al 2025][research_lan_wang_2025]\] \[[Deiwert 1997][research_deiwertgeorges_1997]\] \[[Naveen Kumar 2020][research_g_2020]\] \[[Ou et al 2019][research_ou_yan_2019]\] \[[Jones 1994][research_joneskennethm_1994]\] \[[Reisenthel et al 2010][research_reisenthel_allen_2010]\] \[[Sanghi and Sane 1999][research_sanghi_sane_1999]\] \[[Drummond and Weidner 1981][research_drummond_weidner_1981]\] \[[Bhattrai et al 2018][research_bhattrai_debaar_2018]\] \[[Beachy et al 2021][research_beachy_bae_2021]\] \[[Chen et al 2022][research_chen_li_2022]\] \[[Marvin et al 2013][research_marvinjosephg_brownjamesl_2013]\] \[[Froning and Roach 2003][research_froning_roach_2003_b]\] \[[Gaitonde 2003][research_gaitonde_2003]\] \[[Helgeson and Chinitz 1995][research_helgeson_chinitz_1995]\] \[[Barber and Cox 1989][research_barber_cox_1989]\] \[[Cockrell 1994][research_cockrellcharlesejr_1994]\] \[[Li et al 2022][research_li_zeng_2022]\] \[[Isaac and Miles 1990][research_isaac_miles_1990]\] \[[Thornton et al][research_jmthornton_jbemeurisse]\] \[[Kanda 1998][research_kanda_1998]\] \[[Zhang et al 2026][research_zhang_li_2026]\] \[[Lin and Shen 1997][research_lin_shen_1997]\] \[[Lockman et al 1990][research_lockman_lawrence_1990]\] \[[Marcum 2001][research_marcum_2001]\] \[[McRae and Edwards 2001][research_mcrae_edwards_2001]\] \[[Peng and Panesar 2024][research_peng_panesar_2024]\] \[[Ma et al 2024][research_ma_yang_2024_b]\] \[[Nagawkar and Leifsson 2022][research_nagawkar_leifsson_2022]\] \[[Liu et al 2016][research_liu_liu_2016]\] \[[Hung and MacCormack 1977][research_hung_maccormack_1977]\] \[[Numerical Simulation of the Interaction of a Transverse Jet...][research_numerical_simulation_2015_b]\] \[[Volkov et al 2015][research_volkov_emelyanov_2015]\] \[[Wang et al 2023][research_wang_qian_2023]\] \[[Perrier and Rostand 1994][research_perrier_rostand_1994]\] \[[Yan et al 2026][research_yan_wang_2026]\] \[[Chen and He 2025][research_chen_he_2025_c]\] \[[Hollmeier et al 1999][research_hollmeier_kopp_1999]\] \[[Su et al 2023][research_su_wu_2023]\] \[[Gao et al 2026][research_gao_liu_2026]\] \[[Richardson 1989][research_richardson_1989]\] \[[Simpson 2026][research_simpson_2026]\] \[[Shilnikov and Elizarova 2018][research_shilnikov_elizarova_2018]\] \[[Rathi and Sinha 2024][research_rathi_sinha_2024]\] \[[Freitas 2020][research_freitas_2020]\] \[[Liu et al 2025][research_liu_zhang_2025]\] \[[El Khoury and Hickey 2026][research_elkhoury_hickey_2026]\] \[[Sun et al 2023][research_sun_wu_2023]\] \[[West and Hosder 2015][research_west_hosder_2015]\] \[[Davidson 2026][research_davidson_2026]\] \[[Venkatapathy 1994][research_venkatapathy_1994]\]

### Turbulent combustion modelling and simulation

**Supersonic combustion computed.** Large eddy and direct numerical simulation, flamelet and other turbulent combustion models applied to scramjet combustors.

**88 records.** \[[Klein et al 2017][research_klein_chakraborty_2017]\] \[[Koeplinger et al 2026][research_koeplinger_2026]\] \[[Zhong et al 2025][research_zhong_xu_2025]\] \[[Cerminara et al 2020][research_cerminara_deiterding_2020]\] \[[Wang et al 2016][research_wang_xiao_2016]\] \[[Casseau et al 2016][research_casseau_espinoza_2016]\] \[[Casseau et al 2016][research_casseau_palharini_2016]\] \[[Shan et al 2021][research_shan_zhang_2021]\] \[[Baumgart et al 2025][research_baumgart_yao_2025]\] \[[Baurle 2004][research_baurle_2004]\] \[[Berglund and Fureby 2007][research_berglund_fureby_2007]\] \[[Chitsomboon et al 1988][research_chitsomboont_northamgb_1988]\] \[[Sharma et al 2020][research_sharma_eswaran_2020]\] \[[Chitsomboon and Northam 1991][research_chitsomboon_northam_1991]\] \[[Chen et al 2017][research_chen_xiao_2017]\] \[[Zhong 2007][research_zhong_2007]\] \[[Bellan 2017][research_bellan_2017]\] \[[Direct Numerical Simulation of a Supersonic Flow in the Base...][research_direct_numerical_2018]\] \[[Jin et al 2015][research_jin_luo_2015]\] \[[Wang and Xu 2024][research_wang_xu_2024_b]\] \[[Wu et al 2019][research_wu_liang_2019]\] \[[Wang et al 2025][research_wang_liu_2025_b]\] \[[Sun et al 2019][research_sun_guo_2019]\] \[[Chen et al 2024][research_chen_yang_2024]\] \[[Qi et al 2021][research_qi_li_2021]\] \[[Liu and Wang 2025][research_liu_wang_2025]\] \[[Zhang et al 2018][research_zhang_liu_2018_b]\] \[[Koo et al 2015][research_koo_raman_2015]\] \[[Wu et al 2026][research_wu_zhao_2026]\] \[[Lipanov and Karskanov 2024][research_lipanov_karskanov_2024]\] \[[Ni et al 2016][research_ni_lu_2016]\] \[[Xiao et al 2025][research_xiao_wu_2025]\] \[[Zhang et al 2021][research_zhang_tong_2021]\] \[[Direct Numerical Simulation of the Transition to Turbulence...][research_direct_numerical_2017]\] \[[Tian et al 2025][research_tian_bai_2025]\] \[[Direct numerical simulations of hypersonic boundary layer...][research_direct_numerical_2023]\] \[[Drummond and Mukunda 1988][research_drummond_mukunda_1988]\] \[[Drummond et al 1989][research_drummond_carpenter_1989]\] \[[Drummond et al 1991][research_drummond_carpenter_1991]\] \[[Li and Wang 2017][research_li_wang_2017]\] \[[Zhao et al 2025][research_zhao_wu_2025_b]\] \[[Eugênio Ribeiro 2026][research_eugenioribeiro_2026]\] \[[Tang et al 2022][research_tang_wang_2022]\] \[[Fontan Moura 2019][research_fontanmoura_2019]\] \[[Advisory Group for Aerospace Research and Development 1993][research_advisorygroupforaerospaceresearchanddevelopment_1993]\] \[[Eugênio Ribeiro et al 2020][research_eugenioribeiro_boukharfane_2020]\] \[[Wang et al 2015][research_wang_shan_2015]\] \[[Zhang et al 2023][research_zhang_yao_2023]\] \[[Ladeinde and Lou 2018][research_ladeinde_lou_2018]\] \[[Cheng et al 2023][research_cheng_chen_2023]\] \[[Wang et al 2015][research_wang_wang_2015]\] \[[Wei et al 2024][research_wei_zhang_2024]\] \[[Li et al 2025][research_li_pan_2025]\] \[[Chen et al 2026][research_chen_mao_2026]\] \[[Wei et al 2023][research_wei_zhang_2023]\] \[[Almeida and Navarro-Martinez 2019][research_almeida_navarromartinez_2019]\] \[[Moin and Lele 1998][research_moin_lele_1998]\] \[[Wang et al 2016][research_wang_cai_2016]\] \[[Cai et al 2016][research_cai_liu_2016]\] \[[Fureby et al 2025][research_fureby_nilsson_2025]\] \[[Menon and Jou 1991][research_menon_jou_1991]\] \[[Shan et al 2017][research_shan_hou_2017]\] \[[Narayan 1994][research_narayan_1994]\] \[[Yao 2022][research_yao_2022]\] \[[Zheng et al 2022][research_zheng_jiang_2022]\] \[[Kamel et al 2015][research_kamel_owis_2015]\] \[[Nikonov 2025][research_nikonov_2025]\] \[[Volpiani 2021][research_volpiani_2021]\] \[[Park 1992][research_park_1992]\] \[[Yao et al 2021][research_yao_liu_2021]\] \[[Kumar and Thornber 2016][research_kumar_thornber_2016]\] \[[Sanaka et al 2023][research_sanaka_kandula_2023]\] \[[Gao et al 2017][research_gao_jiang_2017]\] \[[Sun et al 2025][research_sun_xue_2025]\] \[[Parish and Barone 2025][research_parish_barone_2025]\] \[[Peterson 2023][research_peterson_2023]\] \[[Lian et al 2023][research_lian_tang_2023]\] \[[Huang et al 2025][research_huang_zhao_2025]\] \[[Ladeinde et al 2019][research_ladeinde_lou_2019]\] \[[Wu et al 2016][research_wu_wang_2016]\] \[[Zhao et al 2025][research_zhao_wu_2025]\] \[[Tsai 1991][research_tsai_1991]\] \[[Xiang et al 2020][research_xiang_yang_2020]\] \[[Balakrishnan and Williams 1994][research_balakrishnan_williams_1994]\] \[[Bowman et al 1990][research_bowman_hanson_1990]\] \[[Bowman et al 1991][research_bowman_hanson_1991]\] \[[Bowman et al 1992][research_bowman_hanson_1992]\] \[[Shin and Sung 2018][research_shin_sung_2018]\]

### Nozzles, afterbodies and exhaust flows

**The last expansion surface.** Scramjet nozzles, afterbodies, single expansion ramp nozzles and exhaust plumes, and their effect on installed performance.

**86 records.** \[[Huang et al 2024][research_huang_wang_2024]\] \[[Payne et al 1980][research_payne_hartley_1980]\] \[[Payne 1980][research_payne_1980]\] \[[Deere and Asbury 1996][research_deerekarena_asburyscottc_1996]\] \[[Robinson et al 1980][research_robinsonjc_smithdm_1980]\] \[[Golliard and Mihaescu 2025][research_golliard_mihaescu_2025]\] \[[Rizkalla et al 1990][research_rizkalla_chinitz_1990]\] \[[Candon et al 2015][research_candon_ogawa_2015]\] \[[Chen et al 2021][research_chen_xu_2021]\] \[[Huebner 1995][research_huebner_1995]\] \[[Cubbage and Monta 1991][research_cubbage_monta_1991]\] \[[Degregori and Ferlauto 2018][research_degregori_ferlauto_2018]\] \[[Dunn 1969][research_dunn_1969]\] \[[Edwards 1991][research_edwards_1991]\] \[[Schindel 1999][research_schindel_1999]\] \[[Zhang et al 2016][research_zhang_xu_2016]\] \[[Anders 1975][research_andersjbjr_1975]\] \[[Huebner et al 2004][research_huebnerlawrenced_wittedavidw_2004]\] \[[Chou et al 1995][research_choulynnchen_machkervynd_1995]\] \[[Deere and Asbury 1999][research_deerekarena_asburyscottc_1999]\] \[[Heinemann et al 1992][research_heinemannk_bogdanoffdavidw_1992]\] \[[Zukoski and Auerbach 1976][research_zukoski_auerbach_1976]\] \[[Baysal 1992][research_baysalo_1992]\] \[[Shieh et al 2024][research_shieh_lin_2024]\] \[[Gamble et al 2005][research_gamble_defrancesco_2005]\] \[[Griffith 1989][research_griffith_1989]\] \[[Gronland et al 1997][research_gronland_cambier_1997]\] \[[Hartill 1977][research_hartill_1977]\] \[[Hirschen et al 2009][research_hirschen_gulhan_2009]\] \[[Hopkins et al 1979][research_hopkins_konopka_1979]\] \[[Huebner and Tatum 1991][research_huebner_tatum_1991]\] \[[Back et al 1972][research_back_cuffel_1972]\] \[[Taylor 1968][research_taylor_1968]\] \[[Malone and Peavey 1999][research_malonemichaelb_peaveycharlesc_1999]\] \[[Sadunas 1976][research_sadunas_1976]\] \[[Korte 2000][research_kortejj_2000]\] \[[James 2024][research_james_2024]\] \[[Jiang et al 2025][research_jiang_liu_2025]\] \[[Keener 1992][research_keener_1992]\] \[[Keener et al 1994][research_keener_spaid_1994]\] \[[Kohl 1993][research_kohl_1993]\] \[[Koschel and Rick 1991][research_koschel_rick_1991]\] \[[Lee and Mitani 1999][research_lee_mitani_1999]\] \[[Lee et al 2013][research_lee_yang_2013]\] \[[Kinslow et al 1973][research_kinslow_busby_1973]\] \[[Meiss et al 2011][research_meiss_schroder_2011]\] \[[Meyers et al 1974][research_meyers_feller_1974]\] \[[Ridgway et al 2018][research_ridgway_sam_2018]\] \[[Mulard and Moules 1992][research_mulard_moules_1992]\] \[[Matthews and Trimmer 1969][research_matthews_trimmer_1969]\] \[[Schirmer and Capone 1989][research_schirmeralbertow_caponefrancisj_1989]\] \[[Ward and Smart 2021][research_ward_smart_2021]\] \[[Azhar et al 2022][research_azhar_habeeb_2022]\] \[[Pittman 1989][research_pittman_1989]\] \[[Carlson and Abdol-Hamid 1993][research_carlsonjohnr_abdolhamidkhaleds_1993]\] \[[Pruitt and Bates 1992][research_pruitt_bates_1992]\] \[[Streiff 1953][research_streiff_1953]\] \[[Metghalchi 2009][research_metghalchi_2009]\] \[[Ray et al 1988][research_ray_niggemeier_1988]\] \[[Ellison and Johnson 1964][research_ellisonjc_johnsoncb_1964]\] \[[Ren et al 2017][research_ren_zhang_2017]\] \[[Sangiovanni et al 1993][research_sangiovanni_barber_1993]\] \[[Ruffin et al 1989][research_ruffin_venkatapathy_1989_b]\] \[[Scaggs 1966][research_scaggs_1966]\] \[[Small et al 1974][research_smallwj_weidnerjp_1974]\] \[[Small et al 1976][research_smallwj_weidnerjp_1976]\] \[[Watanabe 1993][research_watanabe_1993]\] \[[Scramjet Nozzle/Aftbody 2022][research_scramjet_nozzle_aftbody_2022]\] \[[Sforza 2017][research_sforza_2017]\] \[[Dash and Delguidice 1978][research_dashs_delguidicep_1978]\] \[[Spaid et al 1995][research_spaid_keener_1995]\] \[[Capone and Schirmer 1993][research_caponefrancisj_schirmeralbertow_1993]\] \[[Re and Berrier 1982][research_rerj_berrierbl_1982]\] \[[Brodsky 1970][research_brodsky_1970]\] \[[Crown 1950][research_crown_1950]\] \[[Takahashi et al 2018][research_takahashi_munakata_2018]\] \[[Edwards 1988][research_edwardsthomasalan_1988]\] \[[Kelly 1973][research_kelly_1973]\] \[[Bhadouriya 2024][research_bhadouriya_2024]\] \[[Reddy and Harloff 1991][research_reddy_harloff_1991]\] \[[Phillips et al 1968][research_phillips_fiedler_1968]\] \[[Eames and Mason 1988][research_eamesdjh_masonml_1988]\] \[[Watanabe 1992][research_watanabe_1992]\] \[[Yu et al 2020][research_yu_chen_2020]\] \[[Yu et al 2020][research_yu_chen_2020_b]\] \[[Yue et al 2009][research_yue_xiao_2009]\]

### Inlet starting and unstart

**Whether the inlet starts and what happens when it unstarts.** The Kantrowitz limit and its modifications, self-starting, unstart, restart and buzz.

**66 of these 84 records date from 2015 or later**, so starting became a design variable rather than a fixed limit within the last decade.

**84 records.** \[[Balaji and Venkatasubbaiah 2025][research_balaji_venkatasubbaiah_2025]\] \[[Wang et al 2022][research_wang_zhao_2022]\] \[[Kim et al 2022][research_kim_seo_2022]\] \[[Zeng et al 2026][research_zeng_wang_2026]\] \[[Wang et al 2025][research_wang_tang_2025]\] \[[Peng et al 2024][research_peng_xu_2024_b]\] \[[Carbajosa et al 2025][research_carbajosa_sanzandres_2025]\] \[[Baccarella et al 2021][research_baccarella_liu_2021]\] \[[Barber et al 2006][research_barber_heitt_2006]\] \[[Borovoy et al 2017][research_borovoy_mosharov_2017]\] \[[Deng and Kim 2017][research_deng_kim_2017]\] \[[Wang et al 2026][research_wang_zhang_2026]\] \[[Qi et al 2015][research_qi_bao_2015]\] \[[An et al 2018][research_an_wu_2018]\] \[[Ratchford et al 2025][research_ratchford_redding_2025]\] \[[Luo et al 2024][research_luo_liu_2024]\] \[[Xu et al 2022][research_xu_wang_2022]\] \[[Flock and Gülhan 2017][research_flock_gulhan_2017]\] \[[Liu et al 2019][research_liu_fan_2019]\] \[[Experimental Study of the Unstart/Restart Process of a...][research_experimental_study_2022]\] \[[Fengyuan et al 2016][research_fengyuan_guoping_2016]\] \[[Flock and Gülhan 2019][research_flock_gulhan_2019]\] \[[Li et al 2020][research_li_huang_2020]\] \[[Grainger et al 2014][research_grainger_brieschenk_2014]\] \[[Guo et al 2017][research_guo_gao_2017]\] \[[Hall and Poggie 2019][research_hall_poggie_2019]\] \[[Johnson and Narayanaswamy 2024][research_johnson_narayanaswamy_2024]\] \[[Humphrey et al 1993][research_humphrey_brueckner_1993]\] \[[Mondal and Jagtap 2026][research_mondal_jagtap_2026]\] \[[Acharya 2025][research_acharya_2025]\] \[[Lian et al 2025][research_lian_xiong_2025]\] \[[Tang et al 2026][research_tang_fan_2026]\] \[[Trexler 1988][research_trexlercarla_1988]\] \[[Jiao et al 2016][research_jiao_chang_2016]\] \[[Redding et al 2025][research_redding_cavanaugh_2025]\] \[[Riley et al 2018][research_riley_gaitonde_2018]\] \[[Jin and Yao 2023][research_jin_yao_2023]\] \[[Johnson et al 2022][research_johnson_jenquin_2022]\] \[[Kai-li and Kun-yuan 2010][research_kaili_kunyuan_2010]\] \[[Kurade and Suryanarayana 2023][research_kurade_suryanarayana_2023]\] \[[Grainger et al 2012][research_l_r_2012]\] \[[Li et al 2024][research_li_sun_2024]\] \[[Liu et al 2022][research_liu_kang_2022]\] \[[Jiao et al 2015][research_jiao_chang_2015]\] \[[Millerd 2025][research_millerd_2025]\] \[[Moradian and Timofeev 2012][research_moradian_timofeev_2012]\] \[[Neiner et al 1978][research_neinergh_colegl_1978]\] \[[Wang et al 2019][research_wang_xue_2019]\] \[[Huang et al 2026][research_huang_wang_2026]\] \[[Deng et al 2017][research_deng_jin_2017_b]\] \[[Sivasubramanian et al 2026][research_sivasubramanian_v_2026]\] \[[Sun et al 2025][research_sun_yu_2025]\] \[[Lee and Kang 2019][research_lee_kang_2019]\] \[[Ogawa et al 2009][research_ogawa_grainger_2009]\] \[[Adams et al 1984][research_adamsjcjr_martindalewr_1984]\] \[[Lehtinen et al 1978][research_lehtinenb_zellerjr_1978]\] \[[Mayer and Paynter 1995][research_mayer_paynter_1995]\] \[[Wang et al 2023][research_wang_fan_2023]\] \[[Chang et al 2017][research_chang_li_2017]\] \[[Li 2022][research_li_2022_b]\] \[[Goel et al 2018][research_goel_duraisamy_2018]\] \[[Wang et al 2022][research_wang_fan_2022]\] \[[Sato and Kaji 1992][research_sato_kaji_1992]\] \[[Sato and Kaji 1993][research_sato_kaji_1993]\] \[[Tang et al 2023][research_tang_xiong_2023]\] \[[Self-starting Simulation of a Hypersonic Inlet with Variable...][research_self_starting_simulation_2020]\] \[[Cao et al 2015][research_cao_chang_2015]\] \[[Tahir 2021][research_tahir_2021]\] \[[Baumbick 1974][research_baumbickrj_1974]\] \[[Anderson and Weir 2014][research_andersonbernhardh_weirlois_2014]\] \[[Sun et al 2026][research_sun_yu_2026]\] \[[Timofeev et al 2001][research_timofeev_voinovich_2001]\] \[[Sprunger et al 2025][research_sprunger_lasorsa_2025]\] \[[Qin et al 2026][research_qin_huang_2026]\] \[[Schram and Narayanaswamy 2026][research_schram_narayanaswamy_2026]\] \[[Qin et al 2015][research_qin_chang_2015]\] \[[Im and Do 2018][research_im_do_2018]\] \[[Parmar et al 2026][research_parmar_jp_2026]\] \[[Wang et al 2014][research_wang_wang_2014]\] \[[Wang et al 2024][research_wang_wang_2024_c]\] \[[Wang et al 2026][research_wang_yuan_2026]\] \[[Xiong et al 2019][research_xiong_bai_2019]\] \[[Yang et al 2025][research_yang_xie_2025]\] \[[Zuo et al 2015][research_zuo_huang_2015]\]

### Ignition, kinetics and hydrogen-air chemistry

**The chemistry of ignition.** Ignition delay, reaction mechanisms and the kinetics of hydrogen and hydrocarbon fuels with air at scramjet conditions.

**78 records.** \[[95/01778 Reduced kinetic mechanism of ignition for...][research_95_01778_reduced_1995]\] \[[95/01780 The role of kinetic versus thermal feedback in...][research_95_01780_the_1995]\] \[[95/06326 Ignition simulation of methane/hydrogen mixtures in...][research_95_06326_ignition_1995]\] \[[96/05298 Relationships between bifurcation and numerical...][research_96_05298_relationships_1996]\] \[[97/03061 A numerical study of ignition in the supersonic...][research_97_03061_a_1997]\] \[[97/04270 Ignition of hydrogen-enriched methane by heated air][research_97_04270_ignition_1997]\] \[[Jachimowski and McLain 1983][research_jachimowskicj_mclainag_1983]\] \[[Nishioka and Law 1997][research_nishioka_law_1997]\] \[[Radhi et al 2019][research_radhi_iacobellis_2019]\] \[[Carson 1974][research_carsongtjr_1974]\] \[[Erickson and Klick 1970][research_ericksonwd_klickgf_1970]\] \[[Zhou et al 2022][research_zhou_du_2022]\] \[[Benoit 1967][research_benoit_1967]\] \[[Yu et al 2022][research_yu_zhou_2022]\] \[[Li et al 2018][research_li_liu_2018_b]\] \[[Harney 1963][research_harney_1963]\] \[[Law 2004][research_law_2004]\] \[[Ludwig and Sulzmann 1961][research_ludwig_sulzmann_1961]\] \[[Fujimoto 1963][research_fujimoto_1963]\] \[[Bray 1963][research_bray_1963]\] \[[Neek et al 2025][research_neek_najarmansour_2025]\] \[[Zhong and Peng 2019][research_zhong_peng_2019]\] \[[Drozda et al 2016][research_drozda_baurle_2016]\] \[[Li et al 2025][research_li_xu_2025]\] \[[Rabadan Santana and Weigand 2021][research_rabadansantana_weigand_2021]\] \[[Zhao et al 2026][research_zhao_bai_2026]\] \[[Wan et al 2026][research_wan_wang_2026]\] \[[Strokin and Khailov 1974][research_strokin_khailov_1974]\] \[[Li et al 2017][research_li_liu_2017]\] \[[Yin et al 2026][research_yin_li_2026]\] \[[Zheng et al 2021][research_zheng_xiong_2021]\] \[[Gao et al 2025][research_gao_ji_2025]\] \[[Gimelshein and Wysong 2019][research_gimelshein_wysong_2019]\] \[[Riva et al 1997][research_riva_daminelli_1997]\] \[[Buzukov 1999][research_buzukov_1999]\] \[[Zander et al 2021][research_zander_vinkeloe_2021]\] \[[Baranyshyn et al 2024][research_baranyshyn_kuzmitski_2024]\] \[[Krivosheyev et al 2024][research_krivosheyev_kisel_2024]\] \[[Ignition Delay Time for Silane/Hydrogen/Air Mixtures at Low...][research_ignition_delay_2018]\] \[[Morinaga 1969][research_morinaga_1969]\] \[[Im et al 1998][research_im_chen_1998]\] \[[Kreutz and Law 1996][research_kreutz_law_1996]\] \[[Bryan 1955][research_bryan_1955]\] \[[Mitani 1995][research_mitani_1995]\] \[[Ju and Niioka 1995][research_ju_niioka_1995]\] \[[Li and Zhang 2026][research_li_zhang_2026]\] \[[McGann et al 2019][research_mcgann_lee_2019]\] \[[Peng 2023][research_peng_2023]\] \[[Jachimowski 1974][research_jachimowskicj_1974]\] \[[Dong et al 2020][research_dong_cui_2020]\] \[[Medvedev et al 2016][research_medvedev_agafonov_2016]\] \[[Ogawa 2024][research_ogawa_2024]\] \[[Treviño 1995][research_trevino_1995]\] \[[Bracco et al 1978][research_bracco_homan_1978]\] \[[Norris 2017][research_norris_2017]\] \[[Molchanov et al 2021][research_molchanov_gribinenko_2021]\] \[[Goulard 1958][research_goulard_1958]\] \[[Whitehurst et al 1992][research_whitehurstrb_kraussrh_1992]\] \[[Ma et al 2026][research_ma_fu_2026]\] \[[Boiocchi et al 2018][research_boiocchi_galfetti_2018]\] \[[Law et al 1989][research_law_metghalchi_1989]\] \[[Meshcheryakov and Sabel'nikov 1988][research_meshcheryakov_sabelnikov_1988]\] \[[Ju and Niioka 1994][research_ju_niioka_1994]\] \[[Wang and Zhang 2022][research_wang_zhang_2022_c]\] \[[Pellett 2005][research_pellettgerald_2005]\] \[[Pavlov et al 2023][research_pavlov_gerasimov_2023]\] \[[Hu et al 2016][research_hu_pan_2016]\] \[[Hui-Sheng and Bei-Jing 2021][research_huisheng_beijing_2021]\] \[[Yang and Yuh-Yih Wu 1994][research_yang_yuhyihwu_1994]\] \[[Yin et al 2024][research_yin_li_2024]\] \[[Reynier 2016][research_reynier_2016]\] \[[Chang et al 2022][research_chang_bai_2022]\] \[[Rhodes 1964][research_rhodes_1964]\] \[[Vuillermoz et al 1992][research_vuillermoz_oran_1992]\] \[[da Silva and Deshaies 1994][research_dasilva_deshaies_1994]\] \[[Yang et al 2024][research_yang_che_2024]\] \[[Ma et al 2026][research_ma_zhao_2026]\] \[[Xu et al 2008][research_xu_he_2008]\]

### Net thrust, thrust and drag accounting, and force measurement

**The keystone quantity and how it is measured.** Net thrust and ram drag, thrust and drag accounting, specific impulse and specific thrust, and the force balances that measure thrust and drag in impulse facilities.

The titles that name the keystone quantity itself are few, and Thin Subjects counts them.

**77 records.** \[[Bowman and Foy 1961][research_bowman_foy_1961]\] \[[Kshetrimayum et al 2021][research_kshetrimayum_menezes_2021]\] \[[Allen 1991][research_allenjr_1991]\] \[[Balakalyani and Jagadeesh 2019][research_balakalyani_jagadeesh_2019]\] \[[Bakos and Morgan 1994][research_bakos_morgan_1994]\] \[[Chang et al 2005][research_chang_gu_2005]\] \[[Goulos et al 2021][research_goulos_otter_2021]\] \[[Covert 1984][research_covert_1984]\] \[[Cui et al 2024][research_cui_zhang_2024]\] \[[Curran 2021][research_curran_2021]\] \[[Davison 1963][research_davison_1963]\] \[[Yang et al 2024][research_yang_choi_2024_b]\] \[[Zhang et al 2015][research_zhang_chen_2015]\] \[[Experimental Hypersonic Scramjet Sets Thrust Record][research_experimental_hypersonic_2019]\] \[[Daniel and Mee 1995][research_daniel_mee_1995]\] \[[Wang et al 2016][research_wang_liu_2016]\] \[[Nie et al 2023][research_nie_wang_2023]\] \[[Kutschenreuter 1962][research_kutschenreuter_1962]\] \[[Park et al 2016][research_park_chang_2016]\] \[[Gao et al 2013][research_gao_wang_2013]\] \[[Hall and Ibasitas 2023][research_hall_ibasitas_2023]\] \[[Han et al 2025][research_han_wei_2025]\] \[[Hannemann et al 2017][research_hannemann_martinezschramm_2017]\] \[[Hiers 2018][research_hiers_2018]\] \[[Huang et al 2017][research_huang_tan_2017]\] \[[Kutschenreuter and Balent 1965][research_kutschenreuter_balent_1965]\] \[[Wang and Jiang 2020][research_wang_jiang_2020]\] \[[Isono 2026][research_isono_2026]\] \[[Javaid and Serghides 2003][research_javaid_serghides_2003]\] \[[Jeong et al 2024][research_jeong_kim_2024]\] \[[Jeong et al 2025][research_jeong_kim_2025]\] \[[Jessen and Grönig 1995][research_jessen_gronig_1995]\] \[[Kim et al 2020][research_kim_jang_2020]\] \[[Kunze 2020][research_kunze_2020]\] \[[Langener et al 2009][research_langener_myrabo_2009]\] \[[Liu et al 2019][research_liu_wang_2019]\] \[[Mbagwu et al 2023][research_mbagwu_dalle_2023]\] \[[Mee et al 1995][research_mee_daniel_1995]\] \[[Migdal and Greathouse 1968][research_migdal_greathouse_1968]\] \[[Naumann et al 1991][research_naumann_ende_1991]\] \[[Naumann et al 1992][research_naumann_ende_1992]\] \[[Odam and Paull 2003][research_odam_paull_2003]\] \[[Cassetti 1978][research_cassetti_1978]\] \[[Kalaiarassan et al 2018][research_kalaiarassan_krishan_2018]\] \[[Paull 1993][research_paull_1993]\] \[[Paull et al 1995][research_paull_stalker_1995_c]\] \[[Li et al 2023][research_li_xia_2023]\] \[[Smithey and Fuhs 1977][research_smithey_fuhs_1977]\] \[[Dunlap 1969][research_dunlap_1969]\] \[[Robinson 2024][research_robinson_2024]\] \[[Robinson et al 2004][research_robinson_mee_2004]\] \[[Roux et al 2013][research_roux_shakya_2013]\] \[[Sahoo et al 2007][research_sahoo_mahapatra_2007]\] \[[Saravanan et al 2008][research_saravanan_jagadeesh_2008]\] \[[Choi and Driscoll 2023][research_choi_driscoll_2023]\] \[[Cardullo 1965][research_cardullo_1965]\] \[[Allen and Byrne 1965][research_allen_byrne_1965]\] \[[Stauffer and Takahashi 2023][research_stauffer_takahashi_2023]\] \[[Takahashi et al 1999][research_takahashi_ueda_1999]\] \[[Telectro-Mek Inc Fort Wayne In 1965][research_telectromekincfortwaynein_1965]\] \[[Throttle-Dependent Forces 1985][research_throttle_dependent_forces_1985]\] \[[Thrust and Drag Modeling 2021][research_thrust_and_2021]\] \[[Riggins et al 1997][research_riggins_mcclinton_1997]\] \[[Riggins 1997][research_riggins_1997]\] \[[Tuttle 1995][research_tuttlesean_1995]\] \[[Paull et al 1995][research_paulla_stalkerrj_1995]\] \[[Thrust-Drag Accounting Methodology 1985][research_thrust_drag_accounting_1985]\] \[[Tuttle 2021][research_tuttle_2021]\] \[[Tuttle et al 1995][research_tuttle_mee_1995]\] \[[Voland 1990][research_voland_1990]\] \[[Wang et al 2016][research_wang_liu_2016_b]\] \[[Wang et al 2019][research_wang_liu_2019]\] \[[Stalker et al 1988][research_stalker_morgan_1988]\] \[[Xu et al 2025][research_xu_yu_2025]\] \[[Yang et al 2014][research_yang_chang_2014]\] \[[Zhang et al 2014][research_zhang_chen_2014]\] \[[Zimont and Muhin 2009][research_zimont_muhin_2009]\]

### Dual-mode combustion and thermal choking

**The duct that can be either a ramjet or a scramjet.** Dual-mode combustion, the transition between modes and thermal choking.

**76 records.** \[[Bathel et al 2024][research_bathel_2024]\] \[[Hao et al 2016][research_hao_chang_2016]\] \[[Bussing and Murman 1983][research_bussingtra_murmanem_1983]\] \[[Quinlan et al 2014][research_quinlanjesser_mcdanieljamesc_2014]\] \[[Suneetha et al 2019][research_suneetha_randive_2019]\] \[[Kirik et al 2018][research_kirik_goyne_2018]\] \[[Aerothermodynamics of the Dual-Mode 2001][research_aerothermodynamics_of_2001]\] \[[An et al 2019][research_an_xia_2019]\] \[[Li et al 2017][research_li_jin_2017]\] \[[Arad et al 2020][research_arad_yokev_2020]\] \[[Baccarella et al 2020][research_baccarella_liu_2020]\] \[[Shen et al 2020][research_shen_huang_2020]\] \[[Zhou et al 2023][research_zhou_li_2023]\] \[[Wang et al 2025][research_wang_yao_2025]\] \[[van der Lee et al 2022][research_vanderlee_yokev_2022]\] \[[Zhao et al 2023][research_zhao_tian_2023]\] \[[Computational analysis of scramjet dual mode operation][research_computational_analysis_1985]\] \[[Li et al 2026][research_li_jiao_2026]\] \[[Goyne and McDaniel 2002][research_goynechristopherp_mcdanieljamesc_2002]\] \[[Dual-Mode Combustion Scramjet 2022][research_dual_mode_combustion_2022]\] \[[Trefny et al 2017][research_trefnycharlesj_dippoldvancefiii_2017]\] \[[Elkowitz et al 2024][research_elkowitz_wanchek_2024]\] \[[Donohue 2012][research_donohuejamesm_2012]\] \[[Zhang et al 2018][research_zhang_chang_2018]\] \[[Ha et al 2018][research_ha_yoon_2018]\] \[[Wang et al 2018][research_wang_wang_2018]\] \[[Li et al 2019][research_li_jiao_2019]\] \[[Karanian and Kepler 1965][research_karanianaj_keplerce_1965]\] \[[Byun and Kim 2026][research_byun_kim_2026]\] \[[Meng et al 2024][research_meng_sun_2024]\] \[[Zhu and Xu 2017][research_zhu_xu_2017]\] \[[Li et al 2019][research_li_wang_2019]\] \[[Shaohua and Xu 2017][research_shaohua_xu_2017]\] \[[Zhu et al 2017][research_zhu_xu_2017_b]\] \[[Kouchi et al 2015][research_kouchi_goyne_2015]\] \[[Guha 1994][research_guha_1994]\] \[[Hsia et al 1989][research_hsia_gross_1989]\] \[[Nielsen et al 2021][research_nielsen_edwards_2021]\] \[[Yan et al 2016][research_yan_shaohua_2016]\] \[[Li et al 2025][research_li_ren_2025]\] \[[Ko et al 2024][research_ko_son_2024]\] \[[Li and Ladeinde 2019][research_li_ladeinde_2019]\] \[[McDaniel 2005][research_mcdaniel_2005]\] \[[McDaniel and Edwards 1999][research_mcdaniel_edwards_1999]\] \[[McDaniel and Edwards 2001][research_mcdaniel_edwards_2001]\] \[[Fotia 2015][research_fotia_2015]\] \[[Li et al 2026][research_li_feng_2026]\] \[[Xia et al 2026][research_xia_han_2026]\] \[[Moon et al 2000][research_moon_jeung_2000]\] \[[Cantu et al 2015][research_cantulucaml_galloemanuelaca_2015]\] \[[Zhang et al 2019][research_zhang_yue_2019]\] \[[Huang and Yan 2016][research_huang_yan_2016]\] \[[Fedorova 2023][research_fedorova_2023]\] \[[Tian et al 2016][research_tian_yang_2016]\] \[[O'Byrne et al 1998][research_obyrne_doolan_1998]\] \[[Wang et al 2021][research_wang_he_2021]\] \[[Ko et al 2026][research_ko_son_2026]\] \[[Kim et al 2025][research_kim_seo_2025]\] \[[Yun et al 2026][research_yun_kim_2026]\] \[[Pouring 1965][research_pouring_1965]\] \[[Son et al 2024][research_son_ko_2024]\] \[[Kanapathipillai and Yu 2024][research_kanapathipillai_yu_2024]\] \[[Wang et al 2021][research_wang_hou_2021]\] \[[Aguilera and Yu 2017][research_aguilera_yu_2017]\] \[[Xie et al 2025][research_xie_xia_2025]\] \[[Smayda 2017][research_smayda_2017]\] \[[Zhao et al 2022][research_zhao_xia_2022]\] \[[Cao et al 2020][research_cao_lu_2020]\] \[[Wang et al 2026][research_wang_chen_2026]\] \[[Cockrell et al 2002][research_cockrellcharlesejr_auslenderaaronh_2002]\] \[[Li et al 2019][research_li_liao_2019]\] \[[Riggins 1998][research_rigginsdavid_1998]\] \[[Meshcheryakov and Yashina 2015][research_meshcheryakov_yashina_2015]\] \[[Riggins et al 2006][research_rigginsdavid_tacketregan_2006]\] \[[Xing et al 2016][research_xing_xiao_2016]\] \[[Yen 1963][research_yen_1963]\]

### Reusable launch vehicles and the cost of access

**The development that changed the economic case.** Reusable launch vehicles, their recovery, landing and costs.

**46 of these 61 records date from 2015 or later**, after the programme's economic case had been answered by reusable rockets.

**61 records.** \[[Su and Wang 2015][research_su_wang_2015]\] \[[Zhang et al 2019][research_zhang_wei_2019]\] \[[Schierman et al 2001][research_schierman_ward_2001]\] \[[Nag et al 2023][research_nag_senthil_2023]\] \[[Jia et al 2020][research_jia_fu_2020]\] \[[Liao et al 2023][research_liao_song_2023]\] \[[Maurice et al 1996][research_maurice_leingang_1996]\] \[[Zhao et al 2021][research_zhao_he_2021]\] \[[Nastac and Frendi 2022][research_nastac_frendi_2022]\] \[[Sivan and Pandian 2018][research_sivan_pandian_2018]\] \[[Yue et al 2022][research_yue_titurus_2022]\] \[[Kim et al 2021][research_kim_lee_2021]\] \[[Wu and Zhang 2023][research_wu_zhang_2023]\] \[[Lee et al 2026][research_lee_jo_2026]\] \[[Prasad 2022][research_prasad_2022]\] \[[Su and Liu 2025][research_su_liu_2025]\] \[[Calvignac et al 2003][research_calvignacjacky_danglisa_2003]\] \[[Tariq et al 2026][research_tariq_wasim_2026]\] \[[Botelho et al 2022][research_botelho_martinez_2022]\] \[[Perlo 2026][research_perlo_2026]\] \[[Xu et al 2025][research_xu_guo_2025]\] \[[Fletcher 1988][research_fletcher_1988]\] \[[Holloway and Limerick 1993][research_holloway_limerick_1993]\] \[[Zhi et al 2015][research_zhi_ran_2015]\] \[[ISRO Releases the Special Issue on ‘Reusable Launch...][research_anon_2018]\] \[[Lepsch and Naftel 1992][research_lepsch_naftel_1992]\] \[[Qi et al 2022][research_qi_cheng_2022]\] \[[Du et al 2025][research_du_qin_2025]\] \[[Khamlak 2026][research_khamlak_2026]\] \[[Miller 2000][research_miller_2000]\] \[[Guadagnini et al 2023][research_guadagnini_dezaiacomo_2023]\] \[[Junaid R and Beebi M 2015][research_junaidr_beebim_2015]\] \[[Fusaro et al 2024][research_fusaro_saccone_2024]\] \[[Wang et al 2024][research_wang_xu_2024]\] \[[Wan et al 2026][research_wan_shi_2026]\] \[[Numerical Optimization on Approach and Landing for Reusable...][research_numerical_optimization_2016]\] \[[Çelik and Demirezen 2024][research_celik_demirezen_2024]\] \[[Mathavaraj and Padhi 2020][research_mathavaraj_padhi_2020]\] \[[Pamadi et al 2004][research_pamadi_tartabini_2004]\] \[[Wang et al 2020][research_wang_chen_2020]\] \[[Gong et al 2022][research_gong_wang_2022]\] \[[Wang et al 2022][research_wang_wei_2022]\] \[[Stanley et al 1994][research_stanley_engelund_1994]\] \[[Abrahamm and Valsa 2018][research_abrahamm_valsa_2018]\] \[[Liang et al 2022][research_liang_xu_2022]\] \[[Cheng et al 2021][research_cheng_jing_2021]\] \[[Saboktakin and Monjezi 2024][research_saboktakin_monjezi_2024]\] \[[Li et al 2026][research_li_ji_2026]\] \[[Reusable launch vehicle Technology development and test...][research_reusable_launch_1995]\] \[[Single segment approach and landing guidance and control for...][research_shameed_gr_2021]\] \[[Kiehn 2020][research_kiehn_2020]\] \[[Dixon et al 1985][research_dixonsc_tenneydr_1985]\] \[[Sun 2018][research_sun_2018]\] \[[Swiss Students Achieve Europe’s First Reusable Rocket Hopper][research_swiss_students_2025]\] \[[Takahashi et al 1997][research_takahashi_mizobata_1997]\] \[[Mukundan et al 2022][research_mukundan_maity_2022]\] \[[Duparcq et al 1993][research_duparcq_hermant_1993]\] \[[Zhao et al 2020][research_zhao_li_2020]\] \[[Liao et al 2023][research_liao_chu_2023]\] \[[Lepsch and Naftel 1993][research_lepsch_naftel_1993]\] \[[Wright et al 2003][research_wright_achary_2003]\]

### Isolators and shock trains

**The length of duct that absorbs the back pressure of combustion.** Isolators, shock trains and their unsteady behaviour.

**52 of these 57 records date from 2015 or later**, which is the sense in which the isolator became a subject of its own.

**57 records.** \[[Edelman 2024][research_edelman_2024]\] \[[Edelman et al 2022][research_edelman_2022]\] \[[Gugulothu 2020][research_gugulothu_2020]\] \[[Ngoc Long 2016][research_ngoclong_2016]\] \[[Ullman and Raman 2023][research_ullman_raman_2023]\] \[[Brown et al 2010][research_brown_williams_2010]\] \[[Su et al 2018][research_su_chen_2018]\] \[[Li and Zheng 2023][research_li_zheng_2023]\] \[[Zhao et al 2026][research_zhao_chen_2026]\] \[[Stefaniya et al 2025][research_stefaniya_pushpalatha_2025]\] \[[Srinivasan et al 2020][research_srinivasan_mahapatra_2020]\] \[[Liu et al 2022][research_liu_wu_2022]\] \[[Zhang et al 2017][research_zhang_chang_2017]\] \[[Chen et al 2025][research_chen_sethuraman_2025]\] \[[Yuan et al 2026][research_yuan_liu_2026]\] \[[Cai et al 2017][research_cai_zhou_2017]\] \[[Emami et al 1995][research_emami_trexler_1995]\] \[[Wang et al 2021][research_wang_chang_2021]\] \[[Fu et al 2023][research_fu_song_2023]\] \[[Kong et al 2020][research_kong_chang_2020]\] \[[Juluru Sandeep and AVSS Kumara Swami Gupta 2023][research_julurusandeep_avsskumaraswamigupta_2023]\] \[[Huang et al 2021][research_huang_zhang_2021]\] \[[Li et al 2025][research_li_liu_2025]\] \[[Larsson et al 2015][research_larsson_laurence_2015]\] \[[Sharma et al 2022][research_sharma_eswaran_2022]\] \[[Influence of the rising rate of backpressure on the upstream...][research_influence_of_2023]\] \[[Wang et al 2025][research_wang_liu_2025]\] \[[Meng et al 2020][research_meng_ye_2020]\] \[[Petha Sethuraman et al 2023][research_pethasethuraman_yang_2023]\] \[[Middleton et al 2011][research_middletontroyf_ballarobertjeffrey_2011]\] \[[Hunt and Hunt 2021][research_hunt_hunt_2021]\] \[[Wang et al 2022][research_wang_xin_2022]\] \[[Chen et al 2025][research_chen_he_2025]\] \[[Lonkar and Panda 2026][research_lonkar_panda_2026]\] \[[Wang et al 2025][research_wang_he_2025]\] \[[Huang et al 2025][research_huang_wang_2025]\] \[[Xing et al 2017][research_xing_ruan_2017]\] \[[Fang et al 2020][research_fang_xianyao_2020]\] \[[Deng et al 2015][research_deng_kim_2015]\] \[[Ji et al 2024][research_ji_he_2024]\] \[[Peng et al 2024][research_peng_xu_2024]\] \[[Deng et al 2017][research_deng_jin_2017]\] \[[Jiao et al 2018][research_jiao_chang_2018]\] \[[Liang et al 2024][research_liang_guo_2024]\] \[[Li 2022][research_li_2022]\] \[[Baurle et al 2012][research_baurleroberta_middletontroyf_2012]\] \[[Scramjet Inlet/Forebody and Isolator 2022][research_scramjet_inlet_forebody_2022]\] \[[Hu et al 2015][research_hu_chang_2015]\] \[[Shang 2008][research_shang_2008]\] \[[Petha Sethuraman et al 2020][research_pethasethuraman_kim_2020]\] \[[Liang et al 2022][research_liang_huang_2022]\] \[[Yan et al 2022][research_yan_fan_2022]\] \[[Chen et al 2026][research_chen_sethuraman_2026]\] \[[Geerts and Yu 2017][research_geerts_yu_2017]\] \[[Seleznev 2019][research_seleznev_2019]\] \[[Yang et al 2017][research_yang_bao_2017]\] \[[Baurle and Axdahl 2017][research_baurlera_axdahlel_2017]\]

### Vitiation and test gas contamination

**What the test gas is made of.** Vitiation by combustion heating, contamination by nitric oxide and water, and their effect on what a ground test of a scramjet shows.

**52 records.** \[[Lee et al 2023][research_lee_lee_2023]\] \[[Agresta et al 2013][research_agresta_andriani_2013]\] \[[Davis 1970][research_davis_1970]\] \[[Arad and Michaels 2021][research_arad_michaels_2021]\] \[[Bryce and Reese 1969][research_bryce_reese_1969]\] \[[Burrows and Kurkov 1971][research_burrows_kurkov_1971]\] \[[Cabell and Rock 2003][research_cabell_rock_2003]\] \[[Chang and Cao 2014][research_chang_cao_2014]\] \[[Chelliah et al 1994][research_chelliah_krauss_1994]\] \[[Cheng and Gong 2017][research_cheng_gong_2017]\] \[[Cuda and Gaffney 2008][research_cuda_gaffney_2008]\] \[[Cutler 1998][research_cutler_1998_b]\] \[[Edelman and Spadaccini 1969][research_edelman_spadaccini_1969_b]\] \[[Edelman and Spadaccini 1969][research_edelman_spadaccini_1969]\] \[[Fischer and Rock 1995][research_fischer_rock_1995]\] \[[Giusti et al 2016][research_giusti_sidey_2016]\] \[[Goyne et al 2007][research_goyne_mcdaniel_2007]\] \[[Han et al 2002][research_han_sung_2002]\] \[[Hashimoto 1997][research_hashimoto_1997]\] \[[Hashimoto and Yoshida 1991][research_hashimoto_yoshida_1991]\] \[[Haw et al 2011][research_haw_goyne_2011]\] \[[Hiraiwa et al 1997][research_hiraiwa_sato_1997]\] \[[Brabbs et al 1987][research_brabbstheodorea_lezbergerwina_1987]\] \[[Jeong et al 2024][research_jeong_kim_2024_b]\] \[[Kang et al 2010][research_kang_lee_2010]\] \[[Le et al 2009][research_le_liu_2009]\] \[[Lee et al 2018][research_lee_na_2018]\] \[[Li et al 2012][research_li_song_2012]\] \[[Li et al 2014][research_li_song_2014]\] \[[Luo et al 2012][research_luo_song_2012]\] \[[McDaniel 2003][research_mcdaniel_2003]\] \[[Mitani et al 1996][research_mitani_hiraiwa_1996]\] \[[Mitani et al 1997][research_mitani_hiraiwa_1997]\] \[[Vyas et al 2010][research_vyasmanana_engblomwilliama_2010]\] \[[Ogawa 2025][research_ogawa_2025]\] \[[Pellett et al 2002][research_pellett_bruno_2002]\] \[[Perkins 2010][research_perkins_2010]\] \[[Powell 1985][research_powell_1985]\] \[[Rockwell et al 2010][research_rockwell_goyne_2010]\] \[[Rockwell et al 2011][research_rockwell_goyne_2011]\] \[[Schmalhofer et al 2017][research_schmalhofer_griebel_2017]\] \[[Sprinkle and Davis 1999][research_sprinkle_davis_1999]\] \[[Srinivasan and Erickson 1995][research_srinivasan_erickson_1995]\] \[[Stallings and Burt 1984][research_stallings_burt_1984]\] \[[Sung et al 2024][research_sung_jeong_2024]\] \[[Sung et al 2026][research_sung_kim_2026]\] \[[Tatman 2017][research_tatman_2017]\] \[[Ingenito 2015][research_ingenito_2015]\] \[[Tomioka et al 2007][research_tomioka_hiraiwa_2007]\] \[[Tomioka et al 2009][research_tomioka_hiraiwa_2009]\] \[[Walsh et al 2024][research_walsh_zhan_2024]\] \[[Wu et al 2021][research_wu_song_2021]\]

### Additive manufacture of aerospace structures

**Making structures that could not be made before.** Additive manufacture and design for it, applied to aerospace components, lattices and hot-section parts.

**14 records.** \[[Bozkurt et al 2025][research_bozkurt_avsar_2025]\] \[[Lomo et al 2023][research_lomo_patel_2023]\] \[[Khan and Riccio 2024][research_khan_riccio_2024]\] \[[Dagkolu et al 2021][research_dagkolu_gokdag_2021]\] \[[Gamma Titanium-Aluminide Powder for 2021][research_gamma_titanium_aluminide_2021]\] \[[Feilden et al 2019][research_feilden_glymond_2019]\] \[[Di Caprio et al 2019][research_dicaprio_acanfora_2019]\] \[[Ellis 2025][research_ellis_2025]\] \[[Chen et al 2026][research_pschen_chsu_2026]\] \[[Next-Generation Aerospace Components Via Additive...][research_next_generation_aerospace_2026]\] \[[Orbital ATK tests 3D printed hypersonic engine combustor][research_orbital_atk_2016]\] \[[William-Sobers et al 2025][research_williamsobers_agwu_2025]\] \[[Venkatesan and Vasanth 2024][research_venkatesan_s_2024]\] \[[Zhang et al 2026][research_zhang_liao_2026]\]

## Where the Framing Breaks Down

**The thrust model is a one-dimensional energy and momentum balance and nothing more.** It has no pressure
terms, no losses other than two assumed efficiencies, no chemistry, no dissociation and no spatial
structure. It captures the shape of the problem but makes no performance prediction.
**Every absolute thrust number in this article inherits that.**

**The amplification factor is the most robust thing here and even it is model-dependent.** It follows from
net thrust being a difference, a fact about bookkeeping rather than about any particular engine,
but its numerical value moves with the assumed efficiencies.

**The dissociation threshold of about three thousand kelvin is a rule of thumb**, not a sharp line, and the
ideal-gas stagnation temperatures in the same table are known to be wrong. The argument they support is
qualitative, which is why it is stated as a crossing between Mach 6 and Mach 8 rather than at a specific
Mach number.

**The mass fraction result is the most favourable calculation in the article and deserves the most suspicion.**
It ignores the mass of the propulsion system itself, which for an air-breather grows with capture area and
is far heavier than a rocket engine of equivalent thrust. It ignores the mass of the thermal protection and
of the cooling system. And it assumes the air-breathing phase can be flown at all.
**It says the rocket equation does not forbid the concept. It does not say the vehicle closes.**

**The cooling balance turns on a flux ratio that is assumed rather than known**, and its answer changes from
comfortable to impossible across the plausible range of that one parameter.

**The largest limitation is that this article analyses a vehicle that does not exist.** There is no
configuration to check the physics against, no measured drag, no measured capture area and no flown
trajectory. Every number here describes a class of vehicle rather than the X-30.

## The Source Base

**The vehicle record is nearly empty and the technology record is enormous, which is the opposite of the usual difficulty and creates its own.**

**No frozen configuration was ever published**, so the vehicle's dimensions, weights and even crew
complement vary between sources and between years. The article therefore describes intent rather than
specification, and states that it is doing so.

**The technology record is very large.** The National Aeronautics and Space Administration's Technical
Reports Server returns a substantial body of work on the programme's materials, structures, computational
methods and ground testing, and the propulsion and aerothermodynamics literature that surrounds it is larger
still.

**Much of the programme was classified and some remains so**, particularly the Copper Canyon study and the
military mission analysis. What is publicly available is mostly the technology base rather than the
programme's own decision record, and the decision record that is public comes chiefly through the Air Force
history of the programme, which traces its budget turmoil, the 1989 attempt to cancel it and the
congressional direction to end it by fiscal year 1994
\[[Schweikart and Hallion 1998][research_schwelkart_hallion_1997]\].

**The physics is not in doubt and is drawn from primary literature that long predates the programme.**
Supersonic combustion, hypersonic aerothermodynamics, Rayleigh flow and the mass-fraction arithmetic are all
standard, and the article is built on those rather than on programme documents.

**The research survey holds 3,816 research records drawn from Crossref, the NASA Technical Reports Server and the Defense Technical Information Center**, of which 1,013 are report primaries, being 26.5 percent, by the identifier rule set out under The Definition of Primary. **The median publication year is 2011.** Of the 3,807 dated records, 1,493 were published before 2000, the period of the programme and the decade around it, being 39.2 percent, and 1,776 were published in 2015 or later, being 46.7 percent.

### The Definition of Primary

**Primacy is a property of the document, and this survey derives it from the identifier.** A record is a report primary when its address is on the NASA Technical Reports Server or it carries a digital object identifier under the 10.21236 prefix, which Crossref registers for Defense Technical Information Center reports. By that rule 749 records are report-server records and 264 are Defense Technical Information Center reports. **The programme's own record is largely of this kind**, and 71 of the 141 records in the cluster on the National Aero-Space Plane are report primaries. **The rule does not reach the journal and conference papers that carry much of the period's propulsion work**, so 26.5 percent is a lower bound on how much of the survey is first-hand.

### Thin Subjects

**Eight subjects that this article's derivations depend on have thin literatures.** Each count below is the number of research records in this survey whose title carries at least one of the listed terms, with a hyphen read as a space.

| Subject | Title terms counted | Records |
|---|---|---|
| net thrust and ram drag | net thrust, ram drag | 4 |
| thrust and drag accounting | bookkeeping, thrust drag accounting, thrust/drag accounting, drag accounting | 8 |
| mass capture of an inlet | mass capture, capture ratio, capture area | 3 |
| test time and flow establishment in impulse facilities | test time, test times, flow establishment, establishment time, establishment times, starting time | 16 |
| the radiation equilibrium temperature | radiation equilibrium, radiative equilibrium | 1 |
| the Kantrowitz starting limit | Kantrowitz | 2 |
| mass fraction and the energy needed to reach orbit | mass fraction, mass budget, mass budgets, propellant fraction, energy to orbit | 1 |
| the X-51A | X-51, X-51A, X51 | 2 |

**The keystone quantity has almost no literature under its own name.** Four titles name net thrust or ram drag, and of the 8 that name thrust and drag accounting, one, \[[Lehrach 1987][research_lehrach_1987]\], concerns an aerospace plane. The rest of the accounting literature concerns aircraft in general, civil transports and rockets, so the subtraction this article is built on is measured in the force-balance literature of impulse facilities rather than studied as a subject of its own.

**Mass capture is discussed inside the inlet literature rather than under a heading of its own.** Three titles name mass capture or a capture ratio, against 371 that carry the word inlet or intake, although the conversion from specific thrust to force depends on it.

**The test-time argument rests on a small literature.** Sixteen titles name test time or flow establishment, and 7 of them concern extending the test time of a facility, which is the trade between enthalpy and duration that the facility comparison describes.

**The Kantrowitz limit is named in few titles.** Two titles name it, the earlier from 2019, while the cluster on inlet starting and unstart holds 84 records.

**The radiation equilibrium temperature and the mass fraction to orbit are standard rather than studied.** One title names the radiation equilibrium temperature and one names a mass fraction, mass budget or the energy needed to reach orbit, so the article's heating balance and its bound on the fuel fraction rest on the relations derived above rather than on a literature that tests them.

**The X-51A is almost absent.** Two titles name the X-51, and the flight demonstration programme is described in \[[Hank et al 2008][research_hank_murphy_2008]\], so the X-51A appears here mainly through its place in the article's account rather than through a published literature of its own.

### What the Survey Admits

**A record is admitted only when a person reading its title finds it on this article's subject.** Many words this subject depends on also name something else, and a record that shares only such a word is excluded. Inlet also names the inlets of mass spectrometers, pipes and engine particle separators and the tidal inlets of a coastline. Hydrogen also names civil hydrogen aviation, fuel cells and the road vehicles that carry hydrogen tanks. NASP also names the National Association of School Psychologists, a histone chaperone and a specialty pharmacy association, and vitiation is also a doctrine of contract law. The vocabulary of the energy needed to reach orbit also names **oceanographic and meteorological energy budgets**, and cooling also names the cooling towers of civil engineering. **The combustion of the gas turbine, the piston engine and the power station is excluded**, although it shares the vocabulary of equivalence ratio, ignition delay and flame structure, and so are the tracking, interception and terminal guidance of hypersonic weapons, which this article sets out of scope, and conventional rocket launch vehicles that carry no air-breathing stage. Correction, erratum and withdrawal notices, meeting proceedings, advertisements and trade news of weapons programmes are excluded as well, because a survey counts research works, and a document deposited twice under one title is counted once. A review of a book, a reference or definition entry and a notice such as an editorial, a special-issue introduction or a news item are not admitted either, since none of them is a research work in its own right.

**Some records of doubtful relevance are kept.** General reviews of hydrogen as an aviation fuel are kept because the fuel is the X-30's. Reentry and planetary-entry aerothermodynamics is kept where it shares the heating relations and the facilities, titanium aluminide metallurgy that names no vehicle is kept because the alloys are the programme's, and nuclear and antimatter air-breathing concepts for single stage to orbit are kept because they pose the same question with another heat source. A reader may weigh each accordingly.

**Every research title has been read for relevance, so the off-topic share that remains is a matter of reading judgement.** A reading of titles cannot show that a work is relevant in substance, so this is a statement about titles only.

## Epistemic State

**Historical fact, well attested.**

- The Defense Advanced Research Projects Agency ran a study called Copper Canyon from the early 1980s
  to 1985 which led to the programme, its start dated to 1982 by one source and to 1983 by another.
- The National Aero-Space Plane programme was announced publicly in the 1986 State of the Union
  address, and the vehicle was designated X-30.
- Airframe work involved Rockwell International, McDonnell Douglas and General Dynamics, with
  propulsion work at Pratt and Whitney and Rocketdyne.
- The vehicle was to take off horizontally, use air-breathing propulsion to high Mach number, and
  reach orbit in a single stage.
- Hydrogen was the fuel, with slush hydrogen intended to raise its density.
- Congress directed close-out by the end of fiscal year 1994, and NASA's X-43A history records cancellation
  in October 1994, after some 2.4 billion dollars, without a vehicle being built.

**Reported and not independently corroborated here.**

- That no X-30 configuration was ever frozen, which is consistent with the programme history's record
  of weight estimates rising from 50,000 pounds to about 500,000 and of a design still to be frozen in
  the early 1990s.

**Engineering analysis, computed here and reproducible from the stated inputs.**

- The orbital velocity of 7,789 metres per second at two hundred kilometres.
- The thrust breakdown against flight speed, and that at seven thousand metres per second net thrust
  is 4.78 percent of gross thrust.
- The amplification of 20.90 at that speed, meaning a one percent error in gross thrust becomes a
  twenty-one percent error in net thrust.
- That the fuel's chemical energy is 12.82 percent of the stream's kinetic energy at that speed.
- That the speed at which net thrust vanishes is an artefact of the assumed nozzle efficiency, moving
  from 16,577 metres per second to 8,880 when that efficiency moves from 0.95 to 0.90, and vanishing
  entirely at 1.00.
- The stagnation enthalpies, and the ideal stagnation temperatures which are deliberately reported as
  wrong.
- The flow-through time of 2.0 milliseconds and the resulting facility comparison.
- The burner entry temperatures for subsonic and supersonic combustion, and that the dissociation
  threshold is crossed between Mach 6 and Mach 8 in the subsonic case.
- The normal shock total pressure recovery falling to 0.0108 percent at Mach 20.
- The stagnation heat fluxes and radiation equilibrium temperatures.
- The hydrogen heat sink of 11.44 megajoules per kilogram and the cooling balance against an assumed
  flux ratio.
- The all-rocket dry fraction of 12.19 percent against 52.56 percent permitted for structure when
  air-breathing to six thousand metres per second.
- The slush hydrogen density gain of 15.1 percent.
- The dynamic pressure corridor.

**Inference, labelled as such.**

- **The verification gap, rather than any single technology, is what killed the programme.**
  The physics supports it, while the published histories attribute the cancellation chiefly to budgets
  and to the early commitment to a full-scale orbital vehicle \[[Schweikart and Hallion 1998][research_schwelkart_hallion_1997]\]
  \[[Peebles 2007][research_peeblescurtis_2007_b]\].
- **The small single-purpose scramjet programmes that followed were a reaction to this one.**
  The pattern is clear, and NASA's X-43A history records that the project began within the programme
  as the subscale approach its managers had long rejected \[[Peebles 2007][research_peeblescurtis_2007_b]\].

**Not established.**

- What the X-30's drag, capture area or net thrust would actually have been.
- Whether the vehicle would have closed once propulsion system mass and thermal protection were
  included.
- Whether the concept can reach orbital velocity at all, which remains the open question.

## Out of Scope

- **The [X-43A][ref_x43] and [X-51A][ref_x51]** in detail, treated here only as what came after.
- **The [Space Shuttle][ref_shuttle]**, whose thermal protection experience informed the programme.
- **[Skylon][ref_skylon] and the precooled engine approach**, which attacks the same problem from a
  different direction.
- **Hypersonic weapons**, which are a different mission at different speeds.
- **Chemical kinetics of hydrogen combustion in detail**, surveyed here rather than derived.
- **The classified military mission analysis**, which is not available.

## Conclusion

**The X-30 was cancelled because the number that decided everything could not be measured, and could not be computed either.**

**What accelerates an air-breathing vehicle is a subtraction.** Gross thrust minus ram drag, and at seven
kilometres per second the remainder is under five percent of the gross. Everything the vehicle loses to
spillage, to shock losses, to incomplete combustion, to cooling and to its own external drag has to fit
inside that five percent.
**A one percent error in the larger number is a twenty-one percent error in the answer.**

**No facility could supply the conditions.** Mach 25 carries thirty-four megajoules per kilogram of
stagnation enthalpy, the facilities able to produce it sustain it for milliseconds, and the flow inside the engine
needs milliseconds merely to establish.
**The facilities that reach the enthalpy cannot hold it, and the ones that can hold it cannot reach it**,
a consequence of how energy is stored, and more money would not have changed it.

**And the computation could not close the gap**, because the codes needed validation at conditions the
facilities could not produce, so the computational case and the experimental case failed together instead of
supporting one another.

**The most surprising result here is what was not the problem.** The rocket equation, which is the usual
objection to single stage to orbit, is comfortably satisfied. An all-rocket single stage permits about
twelve percent of its mass to be structure.
**Air-breathing to six kilometres per second permits fifty-two percent, and keeps closing even when drag takes sixty percent of thrust throughout.**
The concept is not forbidden by mass fraction. It is forbidden, or at least indefinitely deferred, by
uncertainty.

**Many of the materials worked, the computational methods advanced, and the programme trained the researchers who went on to fly scramjets on cheaper vehicles.**
A programme can succeed at every subsystem and fail, and this one did.

**The X-30 is the second designation in four articles to go to an aircraft that was never built, after the X-27, and the two failures are opposites.**
The X-27 was not built because nobody bought it.
**The X-30 was not built because the thing it was meant to prove could not be shown to be provable in advance.**

The next article treats the [X-31][ref_x31], the Rockwell and Messerschmitt-Bolkow-Blohm post-stall
manoeuvrability demonstrator, which was built, flew, and answered its question in the most direct way
available.

## References

### Books

- [Ascher H. Shapiro 1953, The dynamics and thermodynamics of compressible...][book_shapiro]
- [E. T. Curran 2000, Scramjet propulsion][book_curran]
- [Ernst Heinrich Hirschel 2004, Basics Of Aerothermodynamics][book_hirschel]
- [George Paul Sutton 1949, Rocket propulsion elements][book_sutton]
- [John Anderson 1989, Hypersonic and high-temperature gas dynamics][book_anderson_hyp]
- [John J. Bertin 1994, Hypersonic aerothermodynamics][book_bertin]
- [Maurice J. Zucrow 1900, Gas dynamics][book_zucrow]
- [Philip G. Hill 1965, Mechanics and thermodynamics of propulsion by...][book_hill_peterson]
- [William H. Heiser 1994, Hypersonic airbreathing propulsion][book_heiser_pratt]

[book_anderson_hyp]: https://openlibrary.org/works/OL1993330W
[book_bertin]: https://openlibrary.org/works/OL3287053W
[book_curran]: https://openlibrary.org/works/OL23791670W
[book_heiser_pratt]: https://openlibrary.org/works/OL3932490W
[book_hill_peterson]: https://openlibrary.org/works/OL8229940W
[book_hirschel]: https://openlibrary.org/works/OL8874089W
[book_shapiro]: https://openlibrary.org/works/OL5908243W
[book_sutton]: https://openlibrary.org/works/OL4095814W
[book_zucrow]: https://openlibrary.org/works/OL122419W

### Reference

- [Boeing X-51 Waverider][ref_x51]
- [Defense Advanced Research Projects Agency][ref_darpa]
- [General Dynamics][ref_gd]
- [Heat of combustion][ref_heat_combustion]
- [Jenkins, Landis and Miller, American X-Vehicles][ref_xvehicles]
- [Kerosene][ref_kerosene]
- [Liquid hydrogen][ref_lh2]
- [McDonnell Douglas][ref_mcdonnell]
- [NASA X-43][ref_x43]
- [Pratt and Whitney][ref_pw]
- [Ram drag and net thrust][ref_ram_drag]
- [Rayleigh flow][ref_rayleigh]
- [Reinforced carbon-carbon][ref_rcc]
- [Rocketdyne][ref_rocketdyne]
- [Rockwell International][ref_rockwell]
- [Rockwell X-30][ref_x30]
- [Rockwell-MBB X-31][ref_x31]
- [RS-25][ref_rs25]
- [Scramjet][ref_scramjet]
- [Skylon and the SABRE precooled engine][ref_skylon]
- [Slush hydrogen][ref_slush]
- [Space Shuttle][ref_shuttle]
- [Titanium aluminide][ref_tial]

[ref_darpa]: https://en.wikipedia.org/wiki/DARPA
[ref_gd]: https://en.wikipedia.org/wiki/General_Dynamics
[ref_heat_combustion]: https://en.wikipedia.org/wiki/Heat_of_combustion
[ref_kerosene]: https://en.wikipedia.org/wiki/Kerosene
[ref_lh2]: https://en.wikipedia.org/wiki/Liquid_hydrogen
[ref_mcdonnell]: https://en.wikipedia.org/wiki/McDonnell_Douglas
[ref_pw]: https://en.wikipedia.org/wiki/Pratt_%26_Whitney
[ref_ram_drag]: https://ntrs.nasa.gov/citations/19930091053
[ref_rayleigh]: https://en.wikipedia.org/wiki/Rayleigh_flow
[ref_rcc]: https://en.wikipedia.org/wiki/Reinforced_carbon%E2%80%93carbon
[ref_rocketdyne]: https://en.wikipedia.org/wiki/Rocketdyne
[ref_rockwell]: https://en.wikipedia.org/wiki/Rockwell_International
[ref_rs25]: https://en.wikipedia.org/wiki/RS-25
[ref_scramjet]: https://en.wikipedia.org/wiki/Scramjet
[ref_shuttle]: https://en.wikipedia.org/wiki/Space_Shuttle
[ref_skylon]: https://en.wikipedia.org/wiki/Skylon_(spacecraft)
[ref_slush]: https://en.wikipedia.org/wiki/Slush_hydrogen
[ref_tial]: https://en.wikipedia.org/wiki/Titanium_aluminide
[ref_x30]: https://en.wikipedia.org/wiki/Rockwell_X-30
[ref_x31]: https://en.wikipedia.org/wiki/Rockwell-MBB_X-31
[ref_x43]: https://en.wikipedia.org/wiki/NASA_X-43
[ref_x51]: https://en.wikipedia.org/wiki/Boeing_X-51_Waverider
[ref_xvehicles]: https://ntrs.nasa.gov/citations/20030067480

### Related Post

- [X-Planes: Aerojet X-8 Aerobee][related_post_a305_aerojet_x8]
- [X-Planes: Bell X-1][related_post_a298_bell_x1]
- [X-Planes: Bell X-14][related_post_a311_bell_x14]
- [X-Planes: Bell X-16][related_post_a313_bell_x16]
- [X-Planes: Bell X-2][related_post_a299_bell_x2]
- [X-Planes: Bell X-22][related_post_a319_bell_x22]
- [X-Planes: Bell X-5][related_post_a302_bell_x5]
- [X-Planes: Bell X-9 Shrike][related_post_a306_bell_x9]
- [X-Planes: Bensen X-25][related_post_a322_bensen_x25]
- [X-Planes: Boeing X-20 Dyna-Soar][related_post_a317_boeing_x20]
- [X-Planes: Convair X-11][related_post_a308_convair_x11]
- [X-Planes: Convair X-12][related_post_a309_convair_x12]
- [X-Planes: Convair X-6][related_post_a303_convair_x6]
- [X-Planes: Curtiss-Wright X-19][related_post_a316_curtiss_wright_x19]
- [X-Planes: Douglas X-3 Stiletto][related_post_a300_douglas_x3]
- [X-Planes: Framing and the Research Aircraft Model][related_post_a297_xplanes_framing]
- [X-Planes: Grumman X-29][related_post_a326_grumman_x29]
- [X-Planes: Hiller X-18][related_post_a315_hiller_x18]
- [X-Planes: Lockheed X-17][related_post_a314_lockheed_x17]
- [X-Planes: Lockheed X-27][related_post_a324_lockheed_x27]
- [X-Planes: Lockheed X-7][related_post_a304_lockheed_x7]
- [X-Planes: Martin Marietta X-23 PRIME][related_post_a320_martin_marietta_x23]
- [X-Planes: Martin Marietta X-24][related_post_a321_martin_marietta_x24]
- [X-Planes: North American X-10][related_post_a307_north_american_x10]
- [X-Planes: North American X-15][related_post_a312_north_american_x15]
- [X-Planes: Northrop X-21][related_post_a318_northrop_x21]
- [X-Planes: Northrop X-4 Bantam][related_post_a301_northrop_x4]
- [X-Planes: Osprey X-28 Sea Skimmer][related_post_a325_osprey_x28]
- [X-Planes: Ryan X-13 Vertijet][related_post_a310_ryan_x13]
- [X-Planes: Schweizer X-26 Frigate][related_post_a323_schweizer_x26]

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
[related_post_a317_boeing_x20]: {% post_url 2025-10-26-x_planes_boeing_x20 %}
[related_post_a318_northrop_x21]: {% post_url 2025-10-27-x_planes_northrop_x21 %}
[related_post_a319_bell_x22]: {% post_url 2025-10-28-x_planes_bell_x22 %}
[related_post_a320_martin_marietta_x23]: {% post_url 2025-10-29-x_planes_martin_marietta_x23 %}
[related_post_a321_martin_marietta_x24]: {% post_url 2025-10-30-x_planes_martin_marietta_x24 %}
[related_post_a322_bensen_x25]: {% post_url 2025-10-31-x_planes_bensen_x25 %}
[related_post_a323_schweizer_x26]: {% post_url 2025-11-01-x_planes_schweizer_x26 %}
[related_post_a324_lockheed_x27]: {% post_url 2025-11-02-x_planes_lockheed_x27 %}
[related_post_a325_osprey_x28]: {% post_url 2025-11-03-x_planes_osprey_x28 %}
[related_post_a326_grumman_x29]: {% post_url 2025-11-04-x_planes_grumman_x29 %}

### Research

- [1985, Prediction and Verification of Aerodynamic Drag, Part I Prediction][research_prediction_and_1985]
- [1985, Prediction and Verification of Aerodynamic Drag, Part II Wind-Tunnel/Flight][research_prediction_and_1985_b]
- [2018][research_anon_2018]
- [266 On ascent guidance of hypersonic vehicle 1994][research_266_on_1994]
- [3D Problems of Rotating Detonation Wave in a Ramjet Engine Modeled on a Supercomputer 2018][research_3d_problems_2018]
- [95/01686 Cavity-actuated supersonic mixing and combustion control 1995][research_95_01686_cavity_actuated_1995]
- [95/01778 Reduced kinetic mechanism of ignition for non-premixed hydrogen/air in a supersonic mixing layer 1995][research_95_01778_reduced_1995]
- [95/01780 The role of kinetic versus thermal feedback in non-premixed ignition of hydrogen versus heated air 1995][research_95_01780_the_1995]
- [95/05986 Oxidation and ablation of 3D carbon-carbon composite at up to 3000°C 1995][research_95_05986_oxidation_1995]
- [95/06326 Ignition simulation of methane/hydrogen mixtures in a supersonic mixing layer 1995][research_95_06326_ignition_1995]
- [95/06441 Studies on solution-derived ceramic coatings for oxidation protection of carbon-carbon composites 1995][research_95_06441_studies_1995]
- [96/05298 Relationships between bifurcation and numerical analyses for ignition of hydrogen-air diffusion flames 1996][research_96_05298_relationships_1996]
- [97/03061 A numerical study of ignition in the supersonic hydrogen/air laminar mixing layer 1997][research_97_03061_a_1997]
- [97/04270 Ignition of hydrogen-enriched methane by heated air 1997][research_97_04270_ignition_1997]
- [98/01484 Effects of mixing schemes on kerosene combustion in a supersonic airstream 1998][research_98_01484_effects_1998]
- [98/03244 Thermodynamics analysis of inverse cycle engine for hypersonic propulsion 1998][research_98_03244_thermodynamics_1998]
- [99/00179 Performance analysis of hydrocarbon-fueled scramjet 1999][research_99_00179_performance_1999]
- [A conceptual design of 1992][research_a_conceptual_1992]
- [A study of hydrogen 1967][research_a_study_1967]
- [Aarnes and White 1975][research_aarnes_white_1975]
- [Abdelhameed and Watanabe 2025][research_abdelhameed_watanabe_2025]
- [Abell 1989][research_abell_1989]
- [Abrahamm and Valsa 2018][research_abrahamm_valsa_2018]
- [Abtahi and Dean 1990][research_abtahi_dean_1990]
- [Abu-Romia 1971][research_aburomia_1971]
- [Abul-Huda and Gamba 2017][research_abulhuda_gamba_2017]
- [Accelerating Hypersonic Innovation 2022][research_accelerating_hypersonic_2022]
- [Acharya 2025][research_acharya_2025]
- [Adam Khan 2024][research_adamkhan_2024]
- [Adamczak and Bolender 2015][research_adamczak_bolender_2015]
- [Adams 1975][research_adams_1975]
- [Adams and John C. 1970][research_adams_johnc_1970]
- [Adams and Landrum 2001][research_adams_landrum_2001]
- [Adams and Probstein 1958][research_adams_probstein_1958]
- [Adams et al 1973][research_adams_johnc_1973]
- [Adams et al 1976][research_adamsjcjr_martindalewr_1976]
- [Adams et al 1984][research_adamsjcjr_martindalewr_1984]
- [Adelman et al 1996][research_adelmanhenryg_meneesgenep_1996]
- [Advisory Group for Aerospace Research and Development 1993][research_advisorygroupforaerospaceresearchanddevelopment_1993]
- [Advisory Group for Aerospace Research and Development 1997][research_advisorygroupforaerospaceresearchanddevelopment_1997]
- [Aero-Space Plane Flexible Access 1991][research_aero_space_plane_1991]
- [Aerothermodynamics of the Dual-Mode 2001][research_aerothermodynamics_of_2001]
- [Aerothermodynamics of Vehicle-Integrated Scramjet 2022][research_aerothermodynamics_of_2022]
- [Aerothermodynamics Research in the 2002][research_aerothermodynamics_research_2002]
- [Agnone 1972][research_agnone_1972]
- [Agnone 1987][research_agnoneanthonym_1987]
- [Agnone and Prakasam 1987][research_agnone_prakasam_1987]
- [Agresta et al 2013][research_agresta_andriani_2013]
- [Aguilera and Yu 2017][research_aguilera_yu_2017]
- [Ahearn and Rand 1996][research_ahearn_rand_1996]
- [Ahmed et al 2023][research_ahmed_ameenk_2023]
- [Ahmed et al 2024][research_ahmed_saenz_2024]
- [Ahuja and Hartfield 2015][research_ahuja_hartfield_2015]
- [Air Force Test Pilot School Edwards Afb Ca 1987][research_airforcetestpilotschooledwardsafbca_1987]
- [Airbreathing Hypersonic Aircraft and 1997][research_airbreathing_hypersonic_1997]
- [Aircraft Engine Test Facility 1992][research_aircraft_engine_1992]
- [Akihisa et al 2000][research_akihisa_masuya_2000]
- [Akpolat et al 2014][research_akpolat_toker_2014]
- [Akyurtlu and Akyurtlu 1991][research_akyurtlu_akyurtlu_1991]
- [Al-Garni et al 1996][research_algarni_sahin_1996]
- [Alam et al 2019][research_alam_sharma_2019]
- [Alam et al 2019][research_alam_sharma_2019_b]
- [Albertson and Emami 2001][research_albertson_emami_2001]
- [Aleemuddin et al 2026][research_aleemuddin_hossain_2026]
- [Alexander 1978][research_alexander_tm_1978]
- [Alghamdi and Al-Ghamdi 2016][research_alghamdi_alghamdi_2016]
- [Ali et al 2004][research_ali_sadrulislam_2004]
- [Alipour Bonab and Yazdani-Asrami 2025][research_alipourbonab_yazdaniasrami_2025]
- [All a Matter of 2019][research_all_a_2019]
- [Allard 2024][research_allard_2024]
- [Allen 1957][research_allen_1957]
- [Allen 1962][research_hjulianallen_1962]
- [Allen 1966][research_allenhj_1966]
- [Allen 1991][research_allenjr_1991]
- [Allen 2021][research_allen_2021]
- [Allen and Beke 1953][research_allenjl_bekeandrew_1953]
- [Allen and Byrne 1965][research_allen_byrne_1965]
- [Allen et al 1994][research_allen_maughan_1994]
- [Almeida and Navarro-Martinez 2019][research_almeida_navarromartinez_2019]
- [Alspach et al 2018][research_alspach_webb_2018]
- [Altenhöfer et al 2018][research_altenhofer_sander_2018]
- [Amatucci et al 1982][research_amatucci_addy_1982]
- [Ambe Verma et al 2021][research_ambeverma_muraripandey_2021]
- [Amrutha Preethi and Ramanujachari 2020][research_amruthapreethi_ramanujachari_2020]
- [Amundsen et al 2004][research_amundsen_leonard_2004]
- [An et al 2018][research_an_wu_2018]
- [An et al 2019][research_an_xia_2019]
- [An et al 2020][research_an_sun_2020]
- [An et al 2021][research_an_wang_2021]
- [An et al 2023][research_an_sun_2023]
- [An et al 2024][research_an_sun_2024]
- [An Investigation on the Effect of TiC Additive on the Microstructural and Mechanical Properties of Ultra-High Temperature ZrB2-SiC-Based Ceramic Composite by Multi-Step Spark Plasma Sintering Method 2024][research_an_investigation_2024]
- [Analysis of Rotating Detonation Wave Engine 2023][research_analysis_of_2023]
- [Anbuselvan et al 2010][research_anbuselvan_menezes_2010]
- [Anders 1975][research_andersjbjr_1975]
- [Anderson 1986][research_anderson_1986]
- [Anderson 1987][research_anderson_1987]
- [Anderson 1993][research_andersoncharlesw_1993]
- [Anderson and Brooks 1960][research_anderson_brooks_1960]
- [Anderson and Eckbreth 1991][research_anderson_eckbreth_1991]
- [Anderson and Weir 2014][research_andersonbernhardh_weirlois_2014]
- [Anderson et al 1977][research_andersongy_reagonpg_1977]
- [Anderson et al 1987][research_andersongriffiny_benczedanielp_1987]
- [Anderson et al 1990][research_cwanderson_charlesrmcclinton_1990]
- [Andreadis et al 2002][research_andreadis_drake_2002]
- [Andrews 1978][research_andrews_1978]
- [Andrews and Mackley 1976][research_andrews_mackley_1976]
- [Andrews and Mackley 1993][research_andrews_mackley_1993]
- [Andrews and Mackley 1994][research_andrews_mackley_1994]
- [Andrews et al 1985][research_earlhandrewsjr_marvingtorrence_1985]
- [Andrews et al 1992][research_andrews_davis_1992]
- [Andrianatos 2020][research_andrianatos_2020]
- [Anfimov 1993][research_anfimov_1993]
- [Anthony et al 1975][research_anthony_dukes_1975]
- [Appel and Oehring 2003][research_appel_oehring_2003]
- [Aprovitola et al 2019][research_aprovitola_iuspa_2019]
- [Arad and Michaels 2021][research_arad_michaels_2021]
- [Arad et al 2020][research_arad_yokev_2020]
- [Archer 1963][research_archer_1963]
- [Ardema 1972][research_ardema_1972]
- [Ardema 1995][research_ardemamarkd_1995]
- [Arguchintseva 1999][research_arguchintseva_1999]
- [Arjun 2010][research_arjun_2010]
- [Armstrong and Nicholls 1967][research_armstrong_nicholls_1967]
- [Arora et al 2025][research_arora_srivastava_2025]
- [Arrington and Woods 1972][research_arrington_woods_1972]
- [Ashok et al 2023][research_ashok_joseph_2023]
- [Aslan et al 1990][research_aslan_bisard_1990]
- [Aso and Hayashi 1990][research_aso_hayashi_1990]
- [Assad et al 2026][research_assad_pisarev_2026]
- [Atanacio 2000][research_atanacio_2000]
- [Atci et al 2024][research_atci_jeyakumar_2024]
- [Athithan and Jeyakumar 2022][research_athithan_jeyakumar_2022]
- [August and Joshi 1996][research_augustjamesa_joshishiv_1996]
- [Auslender et al 2009][research_auslender_suder_2009]
- [Austin 2024][research_austin_2024]
- [Autonomous space processor for 1988][research_autonomous_space_1988]
- [Ayers et al 2023][research_ayers_athmanathan_2023]
- [Azevedo et al 1990][research_azevedo_liu_1990]
- [Azhar et al 2022][research_azhar_habeeb_2022]
- [Aziz et al 2022][research_aziz_chowdhury_2022]
- [Babinsky 2014][research_babinsky_2014]
- [Baccarella and Samuels 2025][research_baccarella_samuels_2025]
- [Baccarella et al 2016][research_baccarella_liu_2016]
- [Baccarella et al 2020][research_baccarella_liu_2020]
- [Baccarella et al 2021][research_baccarella_liu_2021]
- [Back et al 1972][research_back_cuffel_1972]
- [Bacos 1993][research_bacos_1993]
- [Bade 1975][research_bade_1975]
- [Baganoff 1990][research_baganoff_1990]
- [Bahm et al 2005][research_bahm_baumann_2005]
- [Baier et al 2024][research_baier_friess_2024]
- [Bajpai and Jagadeesh 2023][research_bajpai_jagadeesh_2023]
- [Baker and Kramer 1982][research_baker_kramer_1982]
- [Bakos 2024][research_bakos_2024]
- [Bakos and Morgan 1994][research_bakos_morgan_1994]
- [Bakos et al 1993][research_bakosrj_morganrg_1993]
- [Bakos et al 1995][research_bakos_chinitz_1995]
- [Balaji and Venkatasubbaiah 2025][research_balaji_venkatasubbaiah_2025]
- [Balakalyani and Jagadeesh 2019][research_balakalyani_jagadeesh_2019]
- [Balakrishnan and Williams 1994][research_balakrishnan_williams_1994]
- [Balakumar and Chou 2018][research_balakumar_chou_2018]
- [Balakumar and Kegerise 2016][research_balakumar_kegerise_2016]
- [Balboni and Atler 1993][research_balboni_atler_1993]
- [Ball and Chan 1999][research_ball_chan_1999]
- [Ball and Lyon 1966][research_ballwh_lyonfj_1966]
- [Ball and Ross 1972][research_ball_ross_1972]
- [Banagiri et al 2025][research_banagiri_raj_2025]
- [Bandyopadhyay and Gad-el-Hak 1994][research_bandyopadhyay_gadelhak_1994]
- [Bangert et al 1980][research_bangertlh_santmandm_1980]
- [Bangert et al 1980][research_bangertlh_santmandm_1980_b]
- [Bao et al 2009][research_bao_qin_2009]
- [Bao et al 2021][research_bao_wang_2021]
- [Bao et al 2023][research_bao_wang_2023]
- [Baranyshyn et al 2024][research_baranyshyn_kuzmitski_2024]
- [Barber and Cox 1989][research_barber_cox_1989]
- [Barber et al 2006][research_barber_heitt_2006]
- [Barbi et al 1989][research_barbie_mahanjr_1989]
- [Barnett 1963][research_barnett_1963]
- [Baron and Efrat 1979][research_baron_efrat_1979]
- [Barone et al 2022][research_barone_nicholson_2022]
- [Barpande et al 2021][research_barpande_singh_2021]
- [Barre et al 1997][research_barre_braud_1997]
- [Barrier coating and penetrant providing oxidation protection for carbon-carbon materials 1990][research_barrier_coating_1990]
- [Barry 1971][research_barry_1971]
- [Barth 2014][research_barth_2014]
- [Barth et al 2014][research_barth_wheatley_2014]
- [Barthelemy 1989][research_barthelemy_1989]
- [Barthelemy 1989][research_barthelemy_1989_b]
- [Barthelemy 1991][research_barthelemy_1991]
- [Bartolotta and Krause 2000][research_bartolottapaula_krausedavidl_2000]
- [Batdor 1957][research_batdor_1957]
- [Bathel et al 2019][research_bathel_jones_2019]
- [Bathel et al 2024][research_bathel_2024]
- [Battelle Memorial Inst Columbus Oh 1947][research_battellememorialinstcolumbusoh_1947]
- [Batterton et al 1974][research_battertonpg_arpasidj_1974]
- [Batterton et al 1976][research_battertonpg_arpasidj_1976]
- [Baughn et al 1987][research_baughn_hoffman_1987]
- [Baumann 2006][research_baumann_2006]
- [Baumann 2007][research_baumann_2007]
- [Baumann and Bisbee 2003][research_baumann_bisbee_2003]
- [Baumann et al 2008][research_baumann_bahm_2008]
- [Baumann et al 2008][research_baumann_pahle_2008]
- [Baumbick 1974][research_baumbickrj_1974]
- [Baumgart et al 2025][research_baumgart_yao_2025]
- [Baurle 2004][research_baurle_2004]
- [Baurle and Axdahl 2017][research_baurlera_axdahlel_2017]
- [Baurle and White 2022][research_baurle_white_2022]
- [Baurle et al 2012][research_baurleroberta_middletontroyf_2012]
- [Baydar et al 2016][research_baydarezgihan_lufrankk_2016]
- [Baydar et al 2017][research_baydarezgihan_lufrankk_2017]
- [Baysal 1992][research_baysalo_1992]
- [Baş 2026][research_bas_2026]
- [Başkaya and Hickel 2025][research_baskaya_hickel_2025]
- [Beach 1976][research_beachhljr_1976]
- [Beachy et al 2021][research_beachy_bae_2021]
- [Beaurain et al 2003][research_beaurainandre_souchieralain_2003]
- [Beck et al 1998][research_beck_eitelberg_1998]
- [Beckwith 1975][research_beckwith_1975]
- [Beddoes 2018][research_beddoes_2018]
- [Bedick et al 2019][research_bedick_ferguson_2019]
- [Behera and Chakraborty 2023][research_behera_chakraborty_2023]
- [Behrenbrinker et al 2025][research_behrenbrinker_guo_2025]
- [Beichel and Obrien 1978][research_beichel_obrien_1978]
- [Bein et al 1993][research_beint_friedmannp_1993]
- [Bejan 2013][research_bejan_2013]
- [Bekey 1994][research_bekey_1994]
- [Bellan 2017][research_bellan_2017]
- [Ben Hamida et al 2025][research_benhamida_basem_2025]
- [Benard et al 1997][research_benard_gaillard_1997]
- [Benoit 1967][research_benoit_1967]
- [Benson and Maslowe 1966][research_benson_maslowe_1966]
- [Bentley 2009][research_bentley_2009]
- [Berens and Bissinger 1996][research_berens_bissinger_1996]
- [Berens and Bissinger 1998][research_berens_bissinger_1998]
- [Berger and White 2024][research_berger_white_2024]
- [Berglund and Fureby 2007][research_berglund_fureby_2007]
- [Bermudez and Gladden 2003][research_bermudez_gladden_2003]
- [Berry 1991][research_berry_1991]
- [Berry et al 2000][research_berry_auslender_2000]
- [Berry et al 2008][research_berry_daryabeigi_2008]
- [Berry et al 2008][research_berryscotta_horvaththomasjjr_2008]
- [Berry et al 2011][research_berryscotta_kimmelroger_2011]
- [Berry et al 2016][research_berryscotta_bergerkarent_2016]
- [Bert 1989][research_bert_1989]
- [Bertelrud et al 1992][research_bertelrud_kolodziej_1992]
- [Berton et al 1995][research_berton_surdon_1995]
- [Bertrand et al 2025][research_bertrand_huchette_2025]
- [Besserer 1952][research_besserer_1952]
- [Bhadouriya 2024][research_bhadouriya_2024]
- [Bhagwandin and Sahu 2023][research_bhagwandin_sahu_2023]
- [Bhat et al 1993][research_bhatbn_mcphersonwb_1993]
- [Bhattrai et al 2018][research_bhattrai_debaar_2018]
- [Billig 1967][research_billig_1967]
- [Billig 1995][research_billig_1995]
- [Bilsborough et al 2025][research_bilsborough_neilsenburke_2025]
- [Biltgen et al 2004][research_biltgen_lafleur_2004]
- [Bird and Hoffman 1998][research_birdrkeith_hoffmanerick_1998]
- [Birnbaum 1989][research_birnbaum_1989]
- [Bissinger et al 1998][research_bissinger_blagoveshchensky_1998]
- [Blankson and Hagseth 1993][research_blanksonisaiahm_hagsethpaul_1993]
- [Boatright et al 1976][research_boatrightwb_sabolap_1976]
- [Bodan-Sanders and Bouvier 1998][research_bodansanderspatricia_bouviercarl_1998]
- [Boeing Scientific Research Labs Seattle Wa 1963][research_boeingscientificresearchlabsseattlewa_1963]
- [Boeing to use X-43A 2005][research_boeing_to_2005]
- [Bogdanoff and Edwards 1995][research_bogdanoff_edwards_1995]
- [Bogdanoff et al 1996][research_bogdanoff_wilson_1996]
- [Bogdanoff et al 1997][research_bogdanoff_wilson_1997]
- [Bogdonoff 1968][research_bogdonoff_1968]
- [Bogdonoff 1970][research_bogdonoff_1970]
- [Bogdonoff 1999][research_bogdonoff_1999]
- [Bogue and Erbland 1993][research_bogue_erbland_1993]
- [Boiocchi et al 2018][research_boiocchi_galfetti_2018]
- [Bolender and Doman 2005][research_bolender_doman_2005]
- [Boles and Milligan 2013][research_boles_milligan_2013]
- [Bolz 1979][research_bolz_1979]
- [Bonanni et al 2024][research_bonanni_norris_2024]
- [Bond 1958][research_bond_1958]
- [Bonnefond et al 1996][research_bonnefond_falempin_1996]
- [Borovoy et al 2017][research_borovoy_mosharov_2017]
- [Borrelli and Pandolfi 1991][research_borrelli_pandolfi_1991]
- [Boscagli et al 2026][research_boscagli_rigas_2026]
- [Botelho et al 2022][research_botelho_martinez_2022]
- [Bouchard and Chambers 1966][research_bouchard_chambers_1966]
- [Bowcutt 2001][research_bowcutt_2001]
- [Bowersox and Fan 2000][research_bowersox_fan_2000]
- [Bowman and Foy 1961][research_bowman_foy_1961]
- [Bowman et al 1990][research_bowman_hanson_1990]
- [Bowman et al 1991][research_bowman_hanson_1991]
- [Bowman et al 1992][research_bowman_hanson_1992]
- [Boyce and Paull 2001][research_boyce_paull_2001]
- [Boyce et al 2003][research_boyce_gerard_2003]
- [Boyd 1989][research_boydiaind_1989]
- [Boyd 1990][research_boydiaind_1990]
- [Boyd 2002][research_boyd_2002]
- [Boyd 2008][research_boyd_2008]
- [Boyd and Padilla 2003][research_boyd_padilla_2003]
- [Boyer 1965][research_boyer_1965]
- [Boylan 1965][research_boylan_1965]
- [Bozkurt et al 2025][research_bozkurt_avsar_2025]
- [Brabbs et al 1987][research_brabbstheodorea_lezbergerwina_1987]
- [Bracco et al 1978][research_bracco_homan_1978]
- [Bradford and Olds 1999][research_bradford_olds_1999]
- [Brahmachary and Ogawa 2021][research_brahmachary_ogawa_2021]
- [Brahmachary et al 2022][research_brahmachary_fujio_2022]
- [Brasseur 1994][research_brasseur_1994]
- [Bray 1963][research_bray_1963]
- [Brenneis and Wanie 1991][research_brenneis_wanie_1991]
- [Brescianini 2023][research_brescianini_2023]
- [Brescianini and Morgan 1992][research_brescianini_morgan_1992]
- [Bretherton 2021][research_bretherton_2021]
- [Brevault et al 2017][research_brevault_balesdent_2017]
- [Brewer and Morris 1975][research_brewergd_morrisre_1975]
- [Brociek et al 2023][research_brociek_hetmaniok_2023]
- [Brodsky 1970][research_brodsky_1970]
- [Brown and Donbar 2013][research_brown_donbar_2013]
- [Brown and Donbar 2015][research_brown_donbar_2015]
- [Brown et al 1992][research_brown_wierzbanowski_1992]
- [Brown et al 2010][research_brown_williams_2010]
- [Brune et al 2015][research_brune_hosder_2015]
- [Brune et al 2017][research_brune_hosder_2017]
- [Brune et al 2017][research_bruneaj_bruceweiii_2017]
- [Brune et al 2019][research_brune_bruce_2019]
- [Brune et al 2020][research_brune_2020]
- [Brunner 1959][research_brunner_1959]
- [Brunnhofer et al 2006][research_brunnhofer_sirbiparagina_2006]
- [Bruno 2023][research_bruno_2023]
- [Bruno 2023][research_bruno_2023_b]
- [Bruno 2023][research_bruno_2023_c]
- [Bruno 2023][research_bruno_2023_d]
- [Bruno and Ingenito 2021][research_bruno_ingenito_2021]
- [Bryan 1955][research_bryan_1955]
- [Bryce and Reese 1969][research_bryce_reese_1969]
- [Bu and Lei 2018][research_bu_lei_2018]
- [Buchanan and Little 1993][research_buchanan_little_1993]
- [Buchmann 1978][research_buchmannoa_1978]
- [Buehler and Lo 1981][research_buehlerrd_lore_1981]
- [Bui 2025][research_bui_2025]
- [Builder 1964][research_builder_1964]
- [Bulirsch and Chudej 1991][research_bulirsch_chudej_1991]
- [Bulman and Siebenhaar 1995][research_bulman_siebenhaar_1995]
- [Bulman et al 1997][research_bulmanmj_stoutpw_1997]
- [Buning et al 2000][research_buning_wong_2000]
- [Burchfield and Bontrager 1966][research_burchfield_bontrager_1966]
- [Burgers 2017][research_burgers_2017]
- [Burke and Rezzag 2026][research_burke_rezzag_2026]
- [Burnett and Czysz 1963][research_burnett_czysz_1963]
- [Burrows and Kurkov 1971][research_burrows_kurkov_1971]
- [Burrows et al 2024][research_burrows_rana_2024]
- [Burton et al 1990][research_burton_witherspoon_1990]
- [Busa et al 2013][research_busakristin_ellisonerikn_2013]
- [Busa, K. M. et al 2012][research_busakm_mcdanieljc_2012]
- [Buschek and Calise 1993][research_buschekharald_caliseanthonyj_1993]
- [Bush et al 1996][research_bush_tiwari_1996]
- [Bushnell et al 1993][research_bushnelldennism_yiplongp_1993]
- [Bussing and Murman 1983][research_bussingtra_murmanem_1983]
- [Butler 1967][research_butler_1967]
- [Butler and Moore 1992][research_butler_moore_1992]
- [Butrica 2003][research_butrica_2003]
- [Buzukov 1999][research_buzukov_1999]
- [Byrom and Allen 1994][research_byrom_allen_1994]
- [Byun and Kim 2026][research_byun_kim_2026]
- [Cabell and Rock 2003][research_cabell_rock_2003]
- [Cabell et al 2011][research_cabellkaren_hassneal_2011]
- [Cady and Kendle 1971][research_cady_kendle_1971]
- [Cady and Kendle 1972][research_cady_kendle_1972]
- [Cai and Huang 2022][research_cai_huang_2022]
- [Cai et al 2016][research_cai_liu_2016]
- [Cai et al 2017][research_cai_zhou_2017]
- [Cai et al 2023][research_cai_chen_2023]
- [Cai et al 2023][research_cai_zheng_2023]
- [Cai et al 2024][research_cai_chen_2024]
- [Cai et al 2024][research_cai_zheng_2024]
- [Cain and Walton 2003][research_cain_walton_2003]
- [California Inst Of Tech Pasadena 1990][research_californiainstoftechpasadena_1990]
- [Calise et al 1988][research_calise_flandro_1988]
- [Calise et al 1990][research_caliseaj_flandroga_1990]
- [Calloway 1983][research_calloway_1983]
- [Calspan Ub Research Center Buffalo Ny 1990][research_calspanubresearchcenterbuffalony_1990]
- [Calvignac et al 2003][research_calvignacjacky_danglisa_2003]
- [Camarda and Masek 1979][research_camarda_masek_1979]
- [Camarda and Murrow 1990][research_camarda_murrow_1990]
- [Camarda and Murrow 1990][research_camardacharlesj_murrowharoldn_1990]
- [Campbell and Gerstenmaier 2014][research_campbell_gerstenmaier_2014]
- [Campbell et al 2010][research_campbellcharlesh_kingrudolpha_2010]
- [Candler and Leyva 2022][research_candler_leyva_2022]
- [Candler and Nompelis 2006][research_candler_nompelis_2006]
- [Candler and Park 1988][research_candler_park_1988]
- [Candon and Ogawa 2018][research_candon_ogawa_2018]
- [Candon et al 2015][research_candon_ogawa_2015]
- [Cantu et al 2015][research_cantulucaml_galloemanuelaca_2015]
- [Cao and Yu 2021][research_cao_yu_2021]
- [Cao et al 2015][research_cao_chang_2015]
- [Cao et al 2020][research_cao_lu_2020]
- [Cao et al 2021][research_cao_brod_2021]
- [Cao et al 2026][research_cao_zhou_2026]
- [Capone and Schirmer 1993][research_caponefrancisj_schirmeralbertow_1993]
- [Cappuccio 1999][research_cappucciogelsomina_1999]
- [Capra et al 2004][research_capra_leyland_2004]
- [Capriotti][research_diegopcapriotti]
- [Carbajosa et al 2025][research_carbajosa_sanzandres_2025]
- [Carbon fiber composites effect 1971][research_carbon_fiber_1971]
- [Cardullo 1965][research_cardullo_1965]
- [Carlin et al 2003][research_carlincm_frischi_2003]
- [Carlson and Abdol-Hamid 1993][research_carlsonjohnr_abdolhamidkhaleds_1993]
- [Carman 1966][research_carman_jb_1966]
- [Carney 1964][research_carney_1964]
- [Carpenter and Stuhrke 1976][research_carpenterjljr_stuhrkewf_1976]
- [Carpenter et al 1967][research_carpenter_graves_1967]
- [Carrier et al 1995][research_carrier_fendell_1995]
- [Carson 1974][research_carsongtjr_1974]
- [Carson and Midden 1976][research_carsongtjr_middenre_1976]
- [Carter 2012][research_carter_2012]
- [Cary and Hefner 1970][research_cary_hefner_1970]
- [Casali et al 2001][research_casali_gamma_2001]
- [Casey et al 1990][research_caseyr_stalkerrj_1990]
- [Casseau et al 2016][research_casseau_espinoza_2016]
- [Casseau et al 2016][research_casseau_palharini_2016]
- [Cassetti 1978][research_cassetti_1978]
- [Cavolowsky and Newfield 1992][research_cavolowsky_newfield_1992]
- [Cavolowsky et al 1995][research_cavolowsky_loomis_1995]
- [Cavolowsky et al 1995][research_cavolowskyjohna_loomismarkp_1995]
- [Cazin 1989][research_cazin_1989]
- [Cenkci 1991][research_cenkci_1991]
- [Cerminara 2023][research_cerminara_2023]
- [Cerminara et al 2020][research_cerminara_deiterding_2020]
- [Cerminara et al 2025][research_cerminara_nayak_2025]
- [Cerro and Shore 1990][research_jeffreyacerro_cpshore_1990]
- [Chakravarthy and Randive 2022][research_chakravarthy_randive_2022]
- [Chakravarthy and the Computational Fluid Dynamics Department 1990][research_chakravarthy_thecomputationalfluiddynamicsdepartment_1990]
- [Chakravarthy et al 2021][research_chakravarthy_randive_2021]
- [Chambers Jr 2007][research_chambersjr_2007]
- [Chan 1990][research_chan_1990]
- [Chan 1992][research_chan_1992]
- [Chan et al 2018][research_chan_razzaqi_2018]
- [Chan et al 2021][research_chan_whitside_2021]
- [Chaney 1999][research_chaneysteve_1999]
- [Chang and Cao 2014][research_chang_cao_2014]
- [Chang and Hsu 1960][research_chang_hsu_1960]
- [Chang and Tiernan 1986][research_chang_tiernan_1986]
- [Chang and Yuan 2022][research_chang_yuan_2022]
- [Chang et al 1993][research_chang_bass_1993]
- [Chang et al 2005][research_chang_gu_2005]
- [Chang et al 2017][research_chang_li_2017]
- [Chang et al 2020][research_chang_chan_2020]
- [Chang et al 2022][research_chang_bai_2022]
- [Chang et al 2022][research_chang_huang_2022]
- [Changbao et al 2020][research_changbao_hui_2020]
- [Chao and Jeng 1965][research_chao_jeng_1965]
- [Chapter 9 Model of 2013][research_chapter_9_2013]
- [Chaput 1989][research_chaput_1989]
- [Chase 1990][research_chase_1990]
- [Chase 1991][research_chase_1991]
- [Chase 1991][research_chase_1991_b]
- [Chase 1992][research_chase_1992]
- [Chase and Tang 1995][research_chase_tang_1995]
- [Chaudhury and Zhao 1992][research_chaudhury_zhao_1992]
- [Chazot and Panerai 2015][research_chazot_panerai_2015]
- [Cheah et al 2025][research_cheah_bhattacharjee_2025]
- [Chelliah et al 1994][research_chelliah_krauss_1994]
- [Chen 1969][research_chen_1969]
- [Chen 1993][research_chen_1993]
- [Chen 2023][research_chen_2023]
- [Chen and Fan 2025][research_chen_fan_2025]
- [Chen and He 2025][research_chen_he_2025_b]
- [Chen and He 2025][research_chen_he_2025_c]
- [Chen and Wang 2020][research_chen_wang_2020]
- [Chen and Wang 2026][research_chen_wang_2026]
- [Chen and Zhao 2017][research_chen_zhao_2017]
- [Chen and Zhao 2019][research_chen_zhao_2019]
- [Chen et al 2009][research_chen_starkey_2009]
- [Chen et al 2017][research_chen_hu_2017]
- [Chen et al 2017][research_chen_xiao_2017]
- [Chen et al 2017][research_chen_zhu_2017]
- [Chen et al 2018][research_chen_xu_2018]
- [Chen et al 2018][research_chen_zhang_2018]
- [Chen et al 2020][research_chen_fan_2020]
- [Chen et al 2020][research_chen_li_2020]
- [Chen et al 2020][research_chen_zhou_2020]
- [Chen et al 2021][research_chen_fan_2021]
- [Chen et al 2021][research_chen_xu_2021]
- [Chen et al 2022][research_chen_chen_2022]
- [Chen et al 2022][research_chen_li_2022]
- [Chen et al 2022][research_chen_zou_2022]
- [Chen et al 2023][research_chen_chen_2023]
- [Chen et al 2023][research_chen_guo_2023]
- [Chen et al 2023][research_chen_si_2023]
- [Chen et al 2024][research_chen_yang_2024]
- [Chen et al 2024][research_chen_zhang_2024]
- [Chen et al 2025][research_chen_he_2025]
- [Chen et al 2025][research_chen_sethuraman_2025]
- [Chen et al 2025][research_chen_yang_2025]
- [Chen et al 2026][research_chen_mao_2026]
- [Chen et al 2026][research_chen_sethuraman_2026]
- [Chen et al 2026][research_pschen_chsu_2026]
- [Cheng 1960][research_cheng_1960]
- [Cheng 1989][research_cheng_1989]
- [Cheng and Gong 2017][research_cheng_gong_2017]
- [Cheng et al 1994][research_cheng_wehrmeyer_1994]
- [Cheng et al 2021][research_cheng_jing_2021]
- [Cheng et al 2022][research_cheng_xu_2022]
- [Cheng et al 2023][research_cheng_chen_2023]
- [Chernyi 1961][research_chernyi_1961]
- [Chima et al 2009][research_chimarodrickv_connerstimothyr_2009]
- [Chima et al 2010][research_chimarodrickv_connerstimothyr_2010]
- [Chinitz et al 1994][research_chinitz_erdos_1994]
- [Chinnappan and Kim 2026][research_chinnappan_kim_2026]
- [Chinnaraj et al 2024][research_chinnaraj_kim_2024]
- [Chitsomboon 1992][research_chitsomboon_1992]
- [Chitsomboon and Northam 1991][research_chitsomboon_northam_1991]
- [Chitsomboon et al 1988][research_chitsomboont_northamgb_1988]
- [Cho et al 1996][research_cho_ha_1996]
- [Choi and Driscoll 2021][research_choi_driscoll_2021]
- [Choi and Driscoll 2023][research_choi_driscoll_2023]
- [Choi and Driscoll 2024][research_choi_driscoll_2024]
- [Chou and Marineau 2024][research_amandachou_ericcmarineau_2024]
- [Chou et al 1995][research_choulynnchen_machkervynd_1995]
- [Choubey and Pandey 2017][research_choubey_pandey_2017]
- [Choubey and Pandey 2018][research_choubey_pandey_2018]
- [Choubey and Tiwari 2022][research_choubey_tiwari_2022]
- [Choubey and Tiwari 2022][research_choubey_tiwari_2022_b]
- [Choubey and Tiwari 2022][research_choubey_tiwari_2022_c]
- [Choubey et al 2022][research_choubey_gaud_2022]
- [Choubey et al 2023][research_choubey_solanki_2023]
- [Choubey et al 2027][research_choubey_panging_2027]
- [Choudhari et al 2012][research_choudhari_tokugawa_2012]
- [Choudhari et al 2021][research_meelanchoudhari_feili_2021]
- [Choudhary et al 2021][research_choudhary_daschakladar_2021]
- [Chowdhary et al 2022][research_chowdhary_hoang_2022]
- [Christol 1993][research_christol_1993]
- [Christophe 1992][research_christophe_1992]
- [Chu 1967][research_chu_1967]
- [Chu et al 1992][research_chu_thompson_1992]
- [Chu et al 2026][research_chu_tu_2026]
- [Chudej 1996][research_chudej_1996]
- [Chun and Burr 1969][research_chun_burr_1969]
- [Chun et al 1994][research_chunks_lockerj_1994]
- [Chung and Kim 1994][research_chung_kim_1994]
- [Chung and Lu 1995][research_chung_lu_1995]
- [Chung et al 1995][research_chung_kim_1995]
- [Cikanek et al 2007][research_cikanek_bartolotta_2007]
- [Clapp and Hunter 1993][research_clapp_hunter_1993]
- [Clarey and Greendyke 2018][research_clarey_greendyke_2018]
- [Clark 1969][research_clark_1969]
- [Clark et al 1992][research_clark_wallace_1992]
- [Clark et al 1994][research_clark_wallace_1994]
- [Clauser 1954][research_clauser_1954]
- [Clauss et al 1994][research_clauss_sontgen_1994]
- [Clemens 2010][research_clemens_2010]
- [Cockrell 1994][research_cockrellcharlesedwardjr_1994]
- [Cockrell 1994][research_cockrellcharlesejr_1994]
- [Cockrell and Huebner 1991][research_cockrelljr_huebner_1991]
- [Cockrell et al 2000][research_cockrell_engelund_2000]
- [Cockrell et al 2002][research_cockrellcharlesejr_auslenderaaronh_2002]
- [Cohen and Reshotko 1956][research_cohen_reshotko_1956]
- [Cohen-Zur and Natan 1998][research_cohenzur_natan_1998]
- [Cole and Richard 1991][research_colegaryl_richardjacquesc_1991]
- [Cole et al 1993][research_cole_florance_1993]
- [Colladay 1987][research_colladay_1987]
- [Collier 1992][research_collier_1992]
- [Colwell 2023][research_colwell_2023]
- [Colwell and Modlin 1992][research_colwell_modlin_1992]
- [Combustion Scaling in an 2012][research_combustion_scaling_2012]
- [Compressive deformation of PM titanium aluminide at high temperatures 1996][research_compressive_deformation_1996]
- [Compton et al 1983][research_comptonhr_schiessjr_1983]
- [Computational analysis of scramjet 1985][research_computational_analysis_1985]
- [Computational Fluid Dynamics Analysis 1997][research_computational_fluid_1997]
- [Conchie 1989][research_conchie_1989]
- [Connor et al 1971][research_connorle_sparksvw_1971]
- [Constantine et al 2011][research_constantine_wang_2011]
- [Control system design using frequency domain models and parameter optimization with application to supersonic inlet controls 1976][research_control_system_1976]
- [Cook and Dwyer 1966][research_cook_dwyer_1966]
- [Coras and Paull 2006][research_coras_paull_2006]
- [Corban et al 1991][research_corbanje_caliseaj_1991]
- [Corpening 2004][research_corpening_2004]
- [Corpening et al 1991][research_corpening_vanwie_1991]
- [Corrington et al 1956][research_corringtonlc_henningsg_1956]
- [Coupling study of supersonic turbine stage and two-dimensional hydrogen/air rotating detonation combustor 2023][research_coupling_study_2023]
- [Cousin 1967][research_cousin_1967]
- [Couture et al 2008][research_couture_dechamplain_2008]
- [Covell et al 1988][research_covellpeterf_woodrichardm_1988]
- [Covert 1984][research_covert_1984]
- [Cowgill and Johnson 1971][research_cowgillgr_johnsonwr_1971]
- [Cox et al 1966][research_cox_crabtree_1966]
- [Craig and Saric 2016][research_craig_saric_2016]
- [Creating Hypersonic Flow in 2019][research_creating_hypersonic_2019]
- [Cresci 1966][research_cresci_1966]
- [Crivellari et al 1999][research_crivellari_de_1999]
- [Crocker and McEnaney 1991][research_crocker_mcenaney_1991]
- [Crow et al 2012][research_crow_boyd_2012]
- [Crown 1950][research_crown_1950]
- [Cruden et al 2021][research_cruden_tang_2021]
- [Crystallographic and fracture behaviour 2009][research_crystallographic_and_2009]
- [Cubbage and Monta 1991][research_cubbage_monta_1991]
- [Cuda and Gaffney 2008][research_cuda_gaffney_2008]
- [Cuda and Hass 2010][research_cuda_hass_2010]
- [Cui et al 2015][research_cui_wang_2015]
- [Cui et al 2017][research_cui_zhao_2017]
- [Cui et al 2018][research_cui_mei_2018]
- [Cui et al 2018][research_cui_xu_2018]
- [Cui et al 2024][research_cui_zhang_2024]
- [Cui et al 2025][research_cui_zhen_2025]
- [Cunningham 1987][research_cunningham_1987]
- [Cunnington et al 1990][research_cunnington_robinson_1990]
- [Cuppoletti et al 2019][research_cuppoletti_ombrello_2019]
- [Cuppoletti et al 2020][research_cuppoletti_ombrello_2020]
- [Curran 2017][research_curran_2017]
- [Curran 2021][research_curran_2021]
- [Curran and Beach 1988][research_curranet_beachhljr_1988]
- [Curran and Craig 1973][research_curran_craig_1973]
- [Curran and Swithenbank 1966][research_curran_swithenbank_1966]
- [Current State-of-the-Art for Airbreathing 1974][research_current_state_of_the_art_1974]
- [Cutler 1998][research_cutler_1998]
- [Cutler 1998][research_cutler_1998_b]
- [Czysz 1963][research_czysz_1963]
- [Czysz 1963][research_czysz_1963_b]
- [da Silva and Deshaies 1994][research_dasilva_deshaies_1994]
- [da Silva et al 2026][research_dasilva_decastrodasilva_2026]
- [Daghigh and Daghigh 2025][research_daghigh_daghigh_2025]
- [Dagkolu et al 2021][research_dagkolu_gokdag_2021]
- [Dai and Huang 2021][research_dai_huang_2021]
- [Dai et al 2023][research_dai_zhao_2023]
- [Dai et al 2025][research_dai_shao_2025]
- [Dai et al 2026][research_dai_cai_2026]
- [Daines and Segal 1998][research_daines_segal_1998]
- [Daly 2025][research_daly_2025]
- [Danberg 1961][research_danberg_1961]
- [Daney 1968][research_daney_1968]
- [Daney et al 1968][research_daney_sindt_1968]
- [Daniel and Mee 1995][research_daniel_mee_1995]
- [Dary and Pollock 1996][research_dary_mpollock_1996]
- [Daryabeigi et al 2006][research_daryabeigikamran_blossermaxl_2006]
- [Das 2000][research_das_2000]
- [Das et al 2021][research_das_pandey_2021]
- [Das et al 2025][research_das_debnath_2025]
- [Dash and Delguidice 1978][research_dashs_delguidicep_1978]
- [Dash et al 1986][research_dashsm_sinhan_1986]
- [Daub et al 2022][research_daub_willems_2022]
- [Davidson 1996][research_davidson_1996]
- [Davidson 2026][research_davidson_2026]
- [Davidson et al 1999][research_davidson_lallman_1999]
- [Davis 1964][research_davis_1964]
- [Davis 1970][research_davis_1970]
- [Davis 1995][research_davis_1995]
- [Davis 2007][research_davis_2007]
- [Davis 2015][research_davisdavido_2015]
- [Davis and Harvey 1981][research_davis_harvey_1981]
- [Davis and Murrow 1989][research_davis_murrow_1989]
- [Davis and White 2006][research_davis_white_2006]
- [Davis and White 2008][research_davis_white_2008]
- [Davis et al 1970][research_davisgw_plankpp_1970]
- [Davis et al 2006][research_davis_sim_2006]
- [Davison 1963][research_davison_1963]
- [Dayton 1993][research_dayton_1993]
- [De Marchi Poltronieri et al 2025][research_demarchipoltronieri_moreira_2025]
- [de Moura and Ribeiro 2026][research_demoura_ribeiro_2026]
- [De Stefano Fumo et al 2025][research_destefanofumo_sciti_2025]
- [Deangelis and Anderson 1992][research_deangelis_anderson_1992]
- [Debarber 1999][research_debarber_1999]
- [Debnath and Pandey 2015][research_debnath_pandey_2015]
- [Debnath and Roy 2023][research_debnath_roy_2023]
- [DeBonis and Yungster 1996][research_debonisjr_yungsters_1996]
- [Deep and Jagadeesh 2021][research_deep_jagadeesh_2021]
- [Deere and Asbury 1996][research_deerekarena_asburyscottc_1996]
- [Deere and Asbury 1999][research_deerekarena_asburyscottc_1999]
- [Defense Science Board Washington Dc 1988][research_defensescienceboardwashingtondc_1988]
- [Defense Science Board Washington Dc 1992][research_defensescienceboardwashingtondc_1992]
- [Deformation of titanium aluminide 1998][research_deformation_of_1998]
- [Degregori and Ferlauto 2018][research_degregori_ferlauto_2018]
- [Degregori and Ferlauto 2018][research_degregori_ferlauto_2018_b]
- [Deiwert 1997][research_deiwertgeorges_1997]
- [Deiwert et al 1994][research_deiwert_cavalowsky_1994]
- [Delage et al 2022][research_delage_saiz_2022]
- [DelCorso et al 2011][research_delcorsojosepha_cheatwoodfmcneil_2011]
- [Demange et al 2014][research_demangejeffreyj_taylorshawnc_2014]
- [Dempers et al 1999][research_dempers_nikbin_1999]
- [DeNardo 1994][research_denardo_1994]
- [Denenberg 1986][research_denenberg_1986]
- [Deng and Kim 2017][research_deng_kim_2017]
- [Deng et al 2015][research_deng_kim_2015]
- [Deng et al 2016][research_deng_li_2016]
- [Deng et al 2017][research_deng_jin_2017]
- [Deng et al 2017][research_deng_jin_2017_b]
- [Deng et al 2025][research_deng_wang_2025]
- [Deng et al 2026][research_deng_ying_2026]
- [Denman 2018][research_denman_2018]
- [Desai et al 2019][research_desai_brahmachary_2019]
- [Design/Construction and Performance Test 2008][research_design_construction_and_2008]
- [DeSpirito 2015][research_despirito_2015]
- [Development of the Shock 1962][research_development_of_1962]
- [Dewangan and Parwani 2026][research_dewangan_parwani_2026]
- [Dewell and Speyer 1993][research_dewell_speyer_1993]
- [Dewey 1961][research_dewey_1961]
- [Dewitt et al 1989][research_dewitt_hardy_1989]
- [Dhanasar et al 2019][research_dhanasar_ferguson_2019]
- [Dharavath et al 2015][research_dharavath_manna_2015]
- [Di Caprio et al 2019][research_dicaprio_acanfora_2019]
- [Di Giovanni and Stemmer 2019][research_digiovanni_stemmer_2019]
- [Di Giovanni and Stemmer 2019][research_digiovanni_stemmer_2019_b]
- [Diao et al 2025][research_diao_liu_2025]
- [Dickeson et al 2009][research_dickeson_rodriguez_2009]
- [Dicristina 1979][research_dicristina_1979]
- [Dietrick 2013][research_dietrick_2013]
- [Dillon et al 1980][research_dillonjl_marcumdcjr_1980]
- [Ding et al 2015][research_ding_liu_2015]
- [Ding et al 2021][research_ding_liu_2021]
- [Ding et al 2022][research_ding_chen_2022]
- [Ding et al 2022][research_ding_yue_2022]
- [Ding et al 2025][research_ding_liu_2025]
- [Direct measurements of skin 1994][research_direct_measurements_1994]
- [Direct Numerical Simulation of a Supersonic Flow in the Base Region of a Circular Cylinder 2018][research_direct_numerical_2018]
- [Direct Numerical Simulation of the Transition to Turbulence in a Supersonic Boundary Layer on Smooth and Rough Surfaces 2017][research_direct_numerical_2017]
- [Direct numerical simulations of hypersonic boundary layer transition over a hypersonic transition research vehicle model lifting body at different angles of attack 2023][research_direct_numerical_2023]
- [Diskin and Northam 1986][research_diskin_northam_1986]
- [Diskin and Northam 1987][research_diskinglenns_northamgburton_1987]
- [Diskin and Northam 1988][research_diskinglenns_northamgburton_1988]
- [Diskin et al 1987][research_diskin_jachimowski_1987]
- [Dissel et al 2006][research_dissel_kothari_2006]
- [Disturbance Rejection For Airbreathing 2016][research_disturbance_rejection_2016]
- [Dixon 1985][research_dixonsc_1985]
- [Dixon et al 1985][research_dixonsc_tenneydr_1985]
- [Doggett et al 1991][research_doggettrobertvjr_rickettsrodneyh_1991]
- [Doherty 2015][research_doherty_2015]
- [Doherty 2022][research_doherty_2022]
- [Doherty et al 2012][research_doherty_smart_2012]
- [Doherty et al 2014][research_doherty_smart_2014]
- [Doherty et al 2015][research_doherty_smart_2015]
- [Doherty et al 2015][research_doherty_smart_2015_b]
- [Dolvin 2009][research_dolvin_2009]
- [Dong and Cai 2017][research_dong_cai_2017]
- [Dong et al 2018][research_dong_tang_2018]
- [Dong et al 2019][research_dong_liu_2019]
- [Dong et al 2019][research_dong_sun_2019]
- [Dong et al 2020][research_dong_cui_2020]
- [Dongre 2024][research_dongre_2024]
- [Donohue 2012][research_donohuejamesm_2012]
- [Donohue et al 1992][research_donohue_marinelli_1992]
- [Doozandeh et al 2025][research_doozandeh_jindal_2025]
- [Dorrington 1990][research_dorrington_1990]
- [Dorrington 1999][research_dorrington_1999]
- [dos Santos et al 2025][research_dossantos_passaro_2025]
- [Dou et al 2022][research_dou_yang_2022]
- [Dougherty 1975][research_dougherty_1975]
- [Dress et al 1994][research_dress_boyden_1994]
- [Driscoll et al 2015][research_driscoll_stoddard_2015]
- [Drozda et al 2016][research_drozda_baurle_2016]
- [Drummond 1979][research_drummond_1979]
- [Drummond 1991][research_drummondjp_1991]
- [Drummond 1997][research_drummondjphilip_1997]
- [Drummond and Mukunda 1988][research_drummond_mukunda_1988]
- [Drummond and Weidner 1981][research_drummond_weidner_1981]
- [Drummond et al 1989][research_drummond_carpenter_1989]
- [Drummond et al 1989][research_drummondjphilip_carpentermarkh_1989]
- [Drummond et al 1991][research_drummond_carpenter_1991]
- [Drummond et al 2006][research_drummond_bouchez_2006]
- [Drummond et al 2006][research_drummondjphilip_diskinglenns_2006]
- [Dryer and Beke 1952][research_dryermurray_bekeandrew_1952]
- [Dsouza and Molder 1971][research_dsouza_molder_1971]
- [Du et al 2025][research_du_chen_2025]
- [Du et al 2025][research_du_chen_2025_b]
- [Du et al 2025][research_du_qin_2025]
- [Du et al 2026][research_du_chong_2026]
- [Dual-Mode Combustion Scramjet 2022][research_dual_mode_combustion_2022]
- [Duan and Li 2015][research_duan_li_2015]
- [Duan et al 2026][research_duan_zhao_2026]
- [Dube et al 1991][research_dube_slifka_1991]
- [Dudebout et al 1998][research_dudebout_sislian_1998]
- [Dudzinski 2018][research_dudzinski_2018]
- [Dufrene 2015][research_dufrene_2015]
- [Dukes 1962][research_wilfredhdukes_1962]
- [Dunavant and Mulligan 1969][research_dunavant_mulligan_1969]
- [Duncan 1991][research_duncanbeverly_1991]
- [Dunlap 1969][research_dunlap_1969]
- [Dunlap and Kuethe 1961][research_dunlap_kuethe_1961]
- [Dunn 1969][research_dunn_1969]
- [Dunn et al 2021][research_dunn_malik_2021]
- [Duparcq et al 1993][research_duparcq_hermant_1993]
- [Dupont et al 1999][research_dupont_muscat_1999]
- [Dwivedi and Bradley 2010][research_dwivedi_bradley_2010]
- [Dwoyer 1987][research_dwoyerdouglasl_1987]
- [Dynamic Testing of the 2011][research_dynamic_testing_2011]
- [Eames and Mason 1988][research_eamesdjh_masonml_1988]
- [Echeverria Aparicio et al 2022][research_echeverriaaparicio_fishpool_2022]
- [Economos 1966][research_economosc_1966]
- [Edelman 2024][research_edelman_2024]
- [Edelman and Spadaccini 1969][research_edelman_spadaccini_1969]
- [Edelman and Spadaccini 1969][research_edelman_spadaccini_1969_b]
- [Edelman et al 2022][research_edelman_2022]
- [Edmonds et al 1964][research_edmonds_omoth_1964]
- [Edquist 2006][research_edquistkarlt_2006]
- [Edwards 1988][research_edwardsthomasalan_1988]
- [Edwards 1991][research_edwards_1991]
- [Edwards 1992][research_edwards_1992]
- [Edwards 1992][research_edwardsta_1992]
- [Edwards et al 1975][research_edwardsclw_smallwj_1975]
- [Edwards et al 2015][research_edwards_steffens_2015]
- [Effects of compression and 1993][research_effects_of_1993]
- [Effects of different physical properties of anthracite powder fuel on detonation characteristics of a rotating detonation engine 2023][research_effects_of_2023]
- [Effects of Various Compositions of the Fuel-Air Mixture on the Pulse Detonation Engine Performance 2019][research_effects_of_2019]
- [Eggers et al 1978][research_eggers_reagon_1978]
- [Ehrburger et al 1986][research_ehrburger_baranne_1986]
- [Eidelman et al 2000][research_eidelman_sharov_2000]
- [El Khoury and Hickey 2026][research_elkhoury_hickey_2026]
- [El Yagoubi et al 2015][research_elyagoubi_lamon_2015]
- [El-Kebir and Ornik 2020][research_elkebir_ornik_2020]
- [Elder 1975][research_elderdj_1975]
- [Elkowitz et al 2024][research_elkowitz_wanchek_2024]
- [Ellis 1989][research_ellis_1989]
- [Ellis 2025][research_ellis_2025]
- [Ellison and Johnson 1964][research_ellisonjc_johnsoncb_1964]
- [Ellsworth 2010][research_ellsworth_2010]
- [Elmouazen et al 2026][research_elmouazen_zhang_2026]
- [Elrod 1965][research_elrod_1965]
- [Emami et al 1995][research_emami_trexler_1995]
- [Emanuel 1989][research_emanuel_1989]
- [Emanuel 1989][research_emanuel_1989_b]
- [Emory et al 2011][research_emory_terrapon_2011]
- [Engblom et al 2005][research_engblom_frate_2005]
- [Engelund 2001][research_engelund_2001]
- [Engelund and Neal 2013][research_engelund_neal_2013]
- [Engelund et al 1999][research_engelundwalterc_hollandscottd_1999]
- [Engelund et al 2000][research_engelund_holland_2000]
- [Epstein 1961][research_epstein_1961]
- [Erbland 1990][research_erbland_1990]
- [Erdman 2004][research_erdman_2004]
- [Erdos and Erdos 1997][research_erdos_erdos_1997]
- [Erickson and Klick 1970][research_ericksonwd_klickgf_1970]
- [Escher 1992][research_escher_1992]
- [Escher 1999][research_escher_1999]
- [Escher 2001][research_escher_2001]
- [Escher 2002][research_escher_2002]
- [Escher et al 1986][research_escher_doughty_1986]
- [Escher et al 1986][research_escher_teeter_1986]
- [Eshtairy et al 2025][research_eshtairy_millot_2025]
- [Espinosa 2003][research_espinosa_2003]
- [Eugênio Ribeiro 2026][research_eugenioribeiro_2026]
- [Eugênio Ribeiro et al 2020][research_eugenioribeiro_boukharfane_2020]
- [Evaluation of Various Flow Control Methods in Reducing Drag and Aerodynamic Heating on the Nose of Hypersonic Flying Objects 2024][research_evaluation_of_2024]
- [Evans et al 2011][research_evans_zok_2011]
- [Experimental Hypersonic Scramjet Sets Thrust Record 2019][research_experimental_hypersonic_2019]
- [Experimental Study of the Unstart/Restart Process of a Two-Dimensional Supersonic Inlet Induced by Backpressure 2022][research_experimental_study_2022]
- [Eyi et al 2019][research_eyi_hanquist_2019]
- [Fabrication of titanium alloy 1992][research_fabrication_of_1992]
- [Fabrication of titanium matrix 2000][research_fabrication_of_2000]
- [Falempin and Serre 2006][research_falempin_serre_2006]
- [Falempin et al 1992][research_falempin_forrat_1992]
- [Falempin et al 1995][research_falempin_thevenot_1995]
- [Fang et al 2020][research_fang_xianyao_2020]
- [Fang et al 2026][research_fang_zeng_2026]
- [Fasel et al 2011][research_fasel_gross_2011]
- [Fasel et al 2020][research_fasel_keidel_2020]
- [Fasoulas 1996][research_fasoulas_1996]
- [Fasoulas and Messerschmid 1996][research_fasoulas_messerschmid_1996]
- [Fay and Kemp 1963][research_fay_kemp_1963]
- [Fedorova 2023][research_fedorova_2023]
- [Feie and Kretz 2008][research_feie_kretz_2008]
- [Feilden et al 2019][research_feilden_glymond_2019]
- [Feldman et al 2019][research_feldmanjay_stewartdavid_2019]
- [Feltrin et al 2025][research_feltrin_debona_2025]
- [Feng and Wang 2025][research_feng_wang_2025]
- [Fengyuan et al 2016][research_fengyuan_guoping_2016]
- [Ferlemann 2005][research_ferlemann_2005]
- [Ferlemann 2008][research_ferlemannpaulg_2008]
- [Ferlemann et al 2000][research_ferlemann_robinson_2000]
- [Ferlemann et al 2005][research_ferlemann_mcclinton_2005]
- [Fernandez et al 2001][research_fernandezrene_trefnycharlesj_2001]
- [Ferrari et al 2016][research_ferrari_barbato_2016]
- [Ferreira de Moura and Borges Ribeiro 2025][research_ferreirademoura_borgesribeiro_2025]
- [Ferreira de Moura and Borges Ribeiro 2025][research_ferreirademoura_borgesribeiro_2025_b]
- [Ferreira de Moura and Borges Ribeiro 2025][research_ferreirademoura_borgesribeiro_2025_c]
- [Ferreira de Moura and Borges Ribeiro 2025][research_ferreirademoura_borgesribeiro_2025_d]
- [Ferretto et al 2022][research_ferretto_fusaro_2022]
- [Ferri 1973][research_ferri_1973]
- [Ferri and Fox 1969][research_ferri_fox_1969]
- [Ferri and Nucci 1946][research_ferriantonio_nuccilouism_1946]
- [Ferri and Nucci 1951][research_ferriantonio_nuccilouism_1951]
- [Fesmire et al 2021][research_fesmire_2021]
- [Fields et al 2004][research_fields_richards_2004]
- [Fievisohn and Yu 2017][research_fievisohn_yu_2017]
- [Fischer and Hausrath 1966][research_fischer_hausrath_1966]
- [Fischer and Rock 1995][research_fischer_rock_1995]
- [Flaherty and Stitt 1959][research_flahertyrj_stittle_1959]
- [Flandro et al 1992][research_flandroga_roachrl_1992]
- [Fletcher 1967][research_fletcher_1967]
- [Fletcher 1988][research_fletcher_1988]
- [Fletcher 2000][research_fletcherdouglasg_2000]
- [Flexible ceramic matrix composite seal 2015][research_flexible_ceramic_2015]
- [Flight Sciences Lab Inc Buffalo Ny 1964][research_flightscienceslabincbuffalony_1964]
- [Flock and Guelhan 2015][research_flock_guelhan_2015]
- [Flock and Gülhan 2015][research_flock_gulhan_2015]
- [Flock and Gülhan 2017][research_flock_gulhan_2017]
- [Flock and Gülhan 2019][research_flock_gulhan_2019]
- [Flow Calibration and Test Facility 1982][research_flow_calibration_1982]
- [Flow Dynamics and Design Optimization of Rotating Detonation Engine 2025][research_flow_dynamics_2025]
- [Flow-field reconstruction in rotating detonation combustor based on physics-informed neural network 2023][research_flow_field_reconstruction_2023]
- [Foelsche et al 2001][research_foelsche_rogers_2001]
- [Foelsche et al 2006][research_foelsche_beckel_2006]
- [Fogarty 1992][research_fogarty_1992]
- [Fomichev and Yadrenkin 2017][research_fomichev_yadrenkin_2017]
- [Fontan Moura 2019][research_fontanmoura_2019]
- [Ford 1993][research_ford_1993]
- [Foreman 1963][research_foreman_1963]
- [Forsythe et al 1961][research_forsythe_melfi_1961]
- [Fotia 2015][research_fotia_2015]
- [Fotia et al 2016][research_fotia_schauer_2016]
- [Fraiser 1960][research_fraiser_1960]
- [Fratini and Bernardini 2026][research_fratini_bernardini_2026]
- [Fratini et al 2025][research_fratini_dellaposta_2025]
- [Freeman and Powell 1980][research_freeman_powell_1980]
- [Freeman et al 1995][research_freeman_stanley_1995]
- [Freeman et al 1996][research_freeman_talay_1996]
- [Freeman et al 1997][research_freeman_reubush_1997]
- [Freitas 2020][research_freitas_2020]
- [Frey 2014][research_frey_2014]
- [Freydin and Dowell 2021][research_freydin_dowell_2021]
- [Fritzemeier and Jacinto 1990][research_lgfritzemeier_majacinto_1990]
- [Froning 1988][research_froning_1988]
- [Froning 2002][research_froning_2002]
- [Froning and Roach 1999][research_froningjr_roach_1999]
- [Froning and Roach 2003][research_froning_roach_2003]
- [Froning and Roach 2003][research_froning_roach_2003_b]
- [Froning et al 1990][research_froning_gaubatz_1990]
- [Frost 2020][research_frost_2020]
- [Fu and Hall 1993][research_fu_hall_1993]
- [Fu et al 1993][research_fu_hall_1993_b]
- [Fu et al 2015][research_fu_wang_2015]
- [Fu et al 2019][research_fu_wang_2019]
- [Fu et al 2023][research_fu_song_2023]
- [Fu et al 2024][research_fu_song_2024]
- [Fu et al 2026][research_fu_song_2026]
- [Fuchs 2019][research_aaronwfuchs_2019]
- [Fuehrer 1969][research_fuehrer_1969]
- [Fuels for Hypersonic Air-Breathing 2022][research_fuels_for_2022]
- [Fuhs 1966][research_fuhs_1966]
- [Fujii and Inoue 1998][research_fujii_inoue_1998]
- [Fujikawa et al 2017][research_fujikawa_tsuchiya_2017]
- [Fujimoto 1963][research_fujimoto_1963]
- [Fujio and Taguchi 2026][research_fujio_taguchi_2026]
- [Fujiwara 1998][research_fujiwara_1998]
- [Fureby et al 2025][research_fureby_nilsson_2025]
- [Furey 1970][research_furey_1970]
- [Furudate et al 2005][research_furudate_lee_2005]
- [Fusaro et al 2024][research_fusaro_saccone_2024]
- [Fusaro et al 2025][research_fusaro_borgna_2025]
- [Future Perspectives of Airbreathing 2004][research_future_perspectives_2004]
- [Gabb and Gayda 1994][research_gabb_gayda_1994]
- [Gabb and Gayda 1996][research_gabb_gayda_1996]
- [Gai and Cao 2025][research_gai_cao_2025]
- [Gai et al 1992][research_gaisl_mudfordnr_1992]
- [Gaitonde 2003][research_gaitonde_2003]
- [Gaitonde and Lindsey 2006][research_gaitonde_lindsey_2006]
- [Gallo et al 1966][research_gallo_gnos_1966]
- [Gamble et al 2005][research_gamble_defrancesco_2005]
- [Gamma Titanium-Aluminide Powder for 2021][research_gamma_titanium_aluminide_2021]
- [Gao 2023][research_gao_2023]
- [Gao et al 1994][research_gao_zhao_1994]
- [Gao et al 2013][research_gao_wang_2013]
- [Gao et al 2015][research_gao_li_2015]
- [Gao et al 2015][research_gao_lin_2015]
- [Gao et al 2017][research_gao_jiang_2017]
- [Gao et al 2020][research_gao_xi_2020]
- [Gao et al 2020][research_gao_zhang_2020]
- [Gao et al 2020][research_gao_zhang_2020_b]
- [Gao et al 2020][research_gao_zhang_2020_c]
- [Gao et al 2021][research_gao_gou_2021]
- [Gao et al 2025][research_gao_ge_2025]
- [Gao et al 2025][research_gao_ji_2025]
- [Gao et al 2026][research_gao_he_2026]
- [Gao et al 2026][research_gao_liu_2026]
- [Garberoglio 1969][research_garberoglio_1969]
- [Gardner 2024][research_gardner_2024]
- [Gardner et al 2004][research_gardner_steelant_2004]
- [Gaspar and Hackman 1991][research_gaspar_hackman_1991]
- [Ge et al 2026][research_ge_zhu_2026]
- [Gee and Little 1991][research_gee_little_1991]
- [Geerts and Yu 2017][research_geerts_yu_2017]
- [Geiger 1963][research_geiger_1963]
- [Gelder 1957][research_gelderthomasf_1957]
- [Generale and Kalidindi 2021][research_generale_kalidindi_2021]
- [Geng et al 2026][research_geng_liu_2026]
- [Georgiadis et al 2014][research_georgiadisnicholasj_mankbadiminar_2014]
- [Geraci et al 2019][research_geraci_menhorn_2019]
- [Gerlinger and Simsont 2019][research_gerlinger_simsont_2019]
- [Gerlinger et al 1994][research_gerlinger_bruggemann_1994]
- [Ghannadian et al 2024][research_ghannadian_gosse_2024]
- [Ghenai et al 2005][research_ghenai_philippidis_2005]
- [Ghioldi and Piscaglia 2023][research_ghioldi_piscaglia_2023]
- [Ghonem 2000][research_ghonem_2000]
- [Ghonem and Osborne 1996][research_ghonem_osborne_1996]
- [Ghori et al 2023][research_ghori_narendar_2023]
- [Gibbons et al 2021][research_gibbons_damm_2021]
- [Gibbons et al 2026][research_gibbons_damm_2026]
- [Gibson et al 2002][research_gibson_neidhoefer_2002]
- [Gibson et al 2003][research_gibson_cancienne_2003]
- [Gidaspov and Kononov 2019][research_gidaspov_kononov_2019]
- [Gilbert et al 2009][research_gilbertmichael_rajuivatury_2009]
- [Gildfind 2024][research_gildfind_2024]
- [Gildfind and Morgan 2015][research_gildfind_morgan_2015]
- [Gildfind et al 2012][research_gildfind_morgan_2012]
- [Gildfind et al 2014][research_gildfind_morgan_2014]
- [Gildfind et al 2015][research_gildfind_sancho_2015]
- [Gildfind et al 2017][research_gildfind_jacobs_2017]
- [Gilmore 1967][research_gilmore_1967]
- [Gimelshein and Wysong 2019][research_gimelshein_wysong_2019]
- [Ginoux 1966][research_ginoux_1966]
- [Ginter and Cerreta 1962][research_ginter_cerreta_1962]
- [Gion 1968][research_gion_1968]
- [Giusti et al 2016][research_giusti_sidey_2016]
- [Gladden et al 1990][research_gladden_melis_1990]
- [Glaessgen et al 2005][research_glaessgen_dawicke_2005]
- [Glass 2008][research_glass_2008]
- [Glass and Glass 2002][research_glass_glass_2002]
- [Glass et al][research_davideglass_bryanakubitschek]
- [Glass et al 2013][research_glass_capriotti_2013]
- [Glass et al 2014][research_glass_capriotti_2014]
- [Glassman and Nosek 1971][research_glassman_nosek_1971]
- [Glickstein and Powell 1987][research_glickstein_powell_1987]
- [Gnoffo 1993][research_gnoffopetera_1993]
- [Goel et al 2015][research_goel_xie_2015]
- [Goel et al 2018][research_goel_duraisamy_2018]
- [Goff et al 2026][research_goff_wray_2026]
- [Gokul and Malaikannan 2025][research_g_g_2025]
- [Gokul and Malaikannan 2025][research_gokul_malaikannan_2025]
- [Goldberg and Scala 1965][research_goldberg_scala_1965]
- [Goldfeld and Nestoulia 2003][research_goldfeld_nestoulia_2003]
- [Goldman 1958][research_goldman_1958]
- [Goldstein et al 1966][research_goldstein_carter_1966]
- [Golewski and Sadowski 2019][research_golewski_sadowski_2019]
- [Gollan et al 2011][research_gollan_gollan_2011]
- [Golliard and Mihaescu 2025][research_golliard_mihaescu_2025]
- [Golubkin 1978][research_golubkin_1978]
- [Golui et al 2025][research_golui_ranjith_2025]
- [Gong 2005][research_gong_2005]
- [Gong et al 2022][research_gong_wang_2022]
- [Gong et al 2026][research_gong_dong_2026]
- [Gooder and Mall 1995][research_gooder_mall_1995]
- [Goodrich et al 1983][research_goodrich_derry_1983]
- [Goodwin and Maxwell 2017][research_goodwin_maxwell_2017]
- [Gopal and Wilson 2016][research_gopal_wilson_2016]
- [Gopalasingam et al 2025][research_gopalasingam_rakhshani_2025]
- [Gopinath et al 2015][research_gopinath_vignesh_2015]
- [Gopinath et al 2019][research_gopinath_jagadeesh_2019]
- [Gopinath et al 2022][research_gopinath_govindarajan_2022]
- [Goracke et al 1997][research_goracke_levack_1997]
- [Goradia et al 1991][research_goradiasuresh_torresabelo_1991]
- [Gorskii and Olenicheva 2018][research_gorskii_olenicheva_2018]
- [Goulard 1958][research_goulard_1958]
- [Goulos et al 2021][research_goulos_otter_2021]
- [Goyne and McDaniel 2002][research_goynechristopherp_mcdanieljamesc_2002]
- [Goyne et al 2007][research_goyne_mcdaniel_2007]
- [Grabau et al 1964][research_grabau_smithson_1964]
- [Grady and Madzsar 1998][research_grady_madzsar_1998]
- [Grainger et al 2012][research_l_r_2012]
- [Grainger et al 2014][research_grainger_brieschenk_2014]
- [Grasso and Gnoffo 1990][research_grassofrancesco_gnoffopetera_1990]
- [Gray 1978][research_grayhr_1978]
- [Gray et al 1975][research_grayhr_nelsonhg_1975]
- [Gray et al 2024][research_gray_mcloughlin_2024]
- [Gregorek and Lee 1962][research_gregorek_lee_1962]
- [Gregorek and Reuss 1990][research_gregorek_reuss_1990]
- [Gregory and Wilcox 1970][research_gregory_wilcox_1970]
- [Gregory et al 1971][research_gregory_williams_1971]
- [Gregory et al 1992][research_gregoryirenem_chowdhryrajivs_1992]
- [Gregory et al 1993][research_gregoryirenem_mcminnjohnd_1993]
- [Gregory et al 1994][research_gregory_bowles_1994]
- [Gregory et al 1994][research_gregoryirenem_chowdhryrajivs_1994]
- [Grenleski and Billig 1968][research_grenleski_billig_1968]
- [Griffin 2018][research_griffin_2018]
- [Griffith 1958][research_griffith_1958]
- [Griffith 1989][research_griffith_1989]
- [Griffith and Lewis 1963][research_griffith_lewis_1963]
- [Griffith et al 1983][research_griffith_maus_1983]
- [Grimm 1992][research_grimm_1992]
- [Grindle 2011][research_grindle_2011]
- [Grindle 2012][research_grindle_2012]
- [Grindle and Bahm 2006][research_grindle_bahm_2006]
- [Gronland et al 1997][research_gronland_cambier_1997]
- [Ground Testing and Evaluation 2022][research_ground_testing_2022]
- [Ground Testing Facility for Hypersonic Materials 2023][research_ground_testing_2023]
- [Groves et al 2005][research_groves_serrani_2005]
- [Gruenig and Mayinger 1999][research_gruenig_mayinger_1999]
- [Grunlan et al 2010][research_grunlan_rajagopal_2010]
- [Gu and Timmerhaus 1992][research_gu_timmerhaus_1992]
- [Gu et al 2021][research_gu_sun_2021]
- [Guadagnini et al 2023][research_guadagnini_dezaiacomo_2023]
- [Gugulothu 2020][research_gugulothu_2020]
- [Guha 1994][research_guha_1994]
- [Gui et al 2022][research_gui_wang_2022]
- [Guizzo 2004][research_guizzo_2004]
- [Guo and Cao 2026][research_guo_cao_2026]
- [Guo and Lei 2025][research_guo_lei_2025]
- [Guo et al 2017][research_guo_bi_2017]
- [Guo et al 2017][research_guo_gao_2017]
- [Guo et al 2020][research_guo_luo_2020]
- [Guo et al 2022][research_guo_pang_2022]
- [Guo et al 2023][research_guo_gao_2023]
- [Gupta 1987][research_gupta_1987]
- [Gupta 2022][research_gupta_2022]
- [Gupta and Ramkumar 2015][research_gupta_ramkumar_2015]
- [Gupta and Schwer 2018][research_gupta_schwer_2018]
- [Gupta and Venuprasad 2018][research_gupta_venuprasad_2018]
- [Gupta et al 1990][research_gupta_lee_1990]
- [Gupta et al 1992][research_gupta_jones_1992]
- [Gupta et al 2009][research_gupta_sun_2009]
- [Gupta et al 2022][research_gupta_ashokkumar_2022]
- [Gursu et al 1994][research_gursu_sheriff_1994]
- [Guy][research_guy]
- [Guy 1990][research_rwayneguy_1990]
- [Guy and Mackley 1979][research_guyrw_mackleyea_1979]
- [Guy et al 1976][research_guy_mueller_1976]
- [Guy et al 1981][research_guy_torrence_1981]
- [Guy et al 1996][research_rwguy_rcrogers_1996]
- [Gwak et al 2016][research_gwak_lee_2016]
- [Ha et al 2018][research_ha_yoon_2018]
- [Haas 1963][research_haas_1963]
- [Haas et al 1994][research_haas_milos_1994]
- [Hagenmaier et al 2011][research_hagenmaier_eklund_2011]
- [Hagenmaier et al 2013][research_hagenmaier_boles_2013]
- [Haiman and Karp 2026][research_haiman_karp_2026]
- [Haley and Zhong 2023][research_haley_zhong_2023]
- [Hall and Ibasitas 2023][research_hall_ibasitas_2023]
- [Hall and Poggie 2019][research_hall_poggie_2019]
- [Hall et al 1964][research_hall_hildebrand_1964]
- [Hallion et al 1995][research_hallion_becker_1995]
- [Hamaker 1996][research_hamaker_1996]
- [Hames 1992][research_hames_1992]
- [Hammitt and Bogdonoff 1956][research_hammitt_bogdonoff_1956]
- [Hammond 1966][research_hammondmbjr_1966]
- [Hamza and Chattopadhyay 2024][research_hamza_chattopadhyay_2024]
- [Han 1998][research_hansamuels_1998]
- [Han and Cao 2019][research_han_cao_2019]
- [Han and Han 2024][research_han_han_2024]
- [Han et al 1995][research_han_he_1995]
- [Han et al 2000][research_han_bai_2000]
- [Han et al 2002][research_han_sung_2002]
- [Han et al 2020][research_han_lee_2020]
- [Han et al 2021][research_han_lee_2021]
- [Han et al 2024][research_han_bian_2024]
- [Han et al 2024][research_han_ma_2024]
- [Han et al 2025][research_han_wei_2025]
- [Han et al 2026][research_han_cheng_2026]
- [Han et al 2026][research_han_tian_2026]
- [Han et al 2026][research_han_xu_2026]
- [Hanaoka 1997][research_hanaoka_1997]
- [Handbook of physical and 1967][research_handbook_of_1967]
- [Hank et al 2008][research_hank_murphy_2008]
- [Hannemann et al 2017][research_hannemann_martinezschramm_2017]
- [Hannemann et al 2018][research_hannemann_martinezschramm_2018]
- [Hannigan and Webb 1991][research_hannigan_webb_1991]
- [Hannum 1988][research_hannumnedp_1988]
- [Hannum and Berkopec 1989][research_hannumnedp_berkopecfrankd_1989]
- [Hanquist and Boyd 2018][research_hanquist_boyd_2018]
- [Hanquist et al 2017][research_hanquist_hara_2017]
- [Hao et al 2014][research_hao_chang_2014]
- [Hao et al 2016][research_hao_chang_2016]
- [Hao et al 2017][research_hao_yan_2017]
- [Hao et al 2025][research_hao_yu_2025]
- [Hardy and Whalen 1991][research_hardy_whalen_1991]
- [Hardy and Whalen 1992][research_hardy_whalen_1992]
- [Harish and Shabaz 2016][research_harish_shabaz_2016]
- [Harloff 1988][research_harloff_1988]
- [Harloff and Smith 1996][research_harloff_smith_1996]
- [Harmon et al 1996][research_harmon_finefield_1996]
- [Harney 1963][research_harney_1963]
- [Harris 1993][research_harris_1993]
- [Harsha and Waldman 1989][research_harsha_waldman_1989]
- [Hartill 1977][research_hartill_1977]
- [Hartill et al 1978][research_hartillwr_goebeltp_1978]
- [Hartsell 1961][research_hartsell_1961]
- [Hartwig et al 2016][research_hartwig_rame_2016]
- [Harvin et al 2006][research_harvinsf_cabellkf_2006]
- [Hashimoto 1997][research_hashimoto_1997]
- [Hashimoto and Yoshida 1991][research_hashimoto_yoshida_1991]
- [Hass and Cabell][research_nealehass_karenfcabell]
- [Hass et al 2005][research_hass_shih_2005]
- [Hass et al 2005][research_hass_smart_2005]
- [Hass et al 2010][research_hassneale_cabellkarenf_2010]
- [Hastings et al 1957][research_hastings_persh_1957]
- [Hattis and Malchow 1992][research_hattis_malchow_1992]
- [Hatzl et al 2010][research_hatzl_sander_2010]
- [Haun and Ball 1966][research_haun_ball_1966]
- [Haw et al 2011][research_haw_goyne_2011]
- [Hawk and Nelson 1998][research_hawk_nelson_1998]
- [Hawkins and Richardson 1991][research_hawkinsrichardw_richardsonpamelaf_1991]
- [Hawkins et al 1976][research_hawkinsje_kirklandfp_1976]
- [Hawkins et al 1999][research_hawkins_kidd_1999]
- [Hayashi et al 2020][research_hayashi_tsuboi_2020]
- [Hayes et al 1960][research_hayes_probstein_1960]
- [He and Zhong 2021][research_he_zhong_2021]
- [He et al 2020][research_he_wu_2020]
- [He et al 2023][research_he_liu_2023]
- [He et al 2023][research_he_sun_2023]
- [He et al 2024][research_he_tian_2024]
- [He et al 2026][research_he_nie_2026]
- [He et al 2026][research_he_zhou_2026]
- [Health monitoring and controls 1994][research_health_monitoring_1994]
- [Heeg et al 1993][research_heegjennifer_zeilerthomasa_1993]
- [Hegedus and Mendenhall 2003][research_hegedus_mendenhall_2003]
- [Heinemann et al 1992][research_heinemannk_bogdanoffdavidw_1992]
- [Heiser 2010][research_heiser_2010]
- [Heitmeier and Bissinger 1995][research_heitmeier_bissinger_1995]
- [Heitmeir et al 1992][research_heitmeir_lederer_1992]
- [Helenbrook and Colt 1977][research_helenbrook_colt_1977]
- [Helenbrook et al 1971][research_helenbrookrg_mcconartywa_1971]
- [Helgeson and Chinitz 1995][research_helgeson_chinitz_1995]
- [Hemdan 1990][research_hemdan_1990]
- [Henderson 1964][research_henderson_1964]
- [Henderson 1991][research_henderson_1991]
- [Henry and Anderson 1973][research_henryjr_andersongy_1973]
- [Herman and Melnik 1962][research_herman_melnik_1962]
- [Hermann 1965][research_hermannr_1965]
- [Hermann and Schmidt 1995][research_hermann_schmidt_1995]
- [Hermann and Thoenes 1965][research_hermannr_thoenesj_1965]
- [Herrmann and Gülhan 2015][research_herrmann_gulhan_2015]
- [Herrmann and Hillberry 1997][research_herrmann_hillberry_1997]
- [Herrouin et al 1996][research_herrouin_bowen_1996]
- [Hertzberg 1956][research_hertzberg_1956]
- [Hertzberg et al 1961][research_hertzberg_wittliff_1961]
- [Hickman and Adams 1991][research_hickman_adams_1991]
- [Hicks 1991][research_hicksjohnw_1991]
- [Hiers 2018][research_hiers_2018]
- [High Power Water Jet Guided Laser Cutting of SiC/SiC Ceramic Matrix Composite 2022][research_high_power_2022]
- [High temperature compressive strength of titanium reinforced nickel alloy 1993][research_high_temperature_1993]
- [High temperature deformation properties of HIP processed titanium boride-titanium aluminide 1999][research_high_temperature_1999]
- [High temperature hardness and oxidation resistance of sinter-HIP titanium aluminide 1996][research_high_temperature_1996]
- [High temperature strength of nickel alloy reinforced with titanium carbide particles 1996][research_high_temperature_1996_b]
- [Hildebrand et al 2022][research_hildebrand_2022]
- [Hillion et al 2023][research_hillion_parisse_2023]
- [Hinkley et al 1995][research_hinkley_prasad_1995]
- [Hinman et al 2015][research_hinman_schmitt_2015]
- [Hiraiwa et al 1997][research_hiraiwa_sato_1997]
- [Hirayama et al 2026][research_hirayama_hamaji_2026]
- [Hirschen et al 2009][research_hirschen_gulhan_2009]
- [Hite 1991][research_hitedale_1991]
- [Ho and Rahman 2005][research_ho_rahman_2005]
- [Hodge 1976][research_hodge_1976]
- [Hodge and Harvin 2000][research_hodgejeffreys_harvinstephenf_2000]
- [Hoegenauer and Koelle 1989][research_hoegenauer_koelle_1989]
- [Hoffman et al 1995][research_hoffman_phan_1995]
- [Hoffmann et al 1989][research_hoffmannek_birdrk_1989]
- [Hohn and Guelhan 2012][research_hohn_guelhan_2012]
- [Hojnacki 1972][research_hojnacki_1972]
- [Holden et al 2001][research_holden_wadhams_2001]
- [Holguin et al 2018][research_holguin_hudson_2018]
- [Holland 1991][research_hollandscottdouglas_1991]
- [Holland 1992][research_hollandscottd_1992]
- [Holland 1993][research_hollandscottd_1993]
- [Holland and Perkins 1991][research_hollandscottd_perkinsjohnn_1991]
- [Holland and Perkins 1992][research_hollandscottd_perkinsjohnn_1992]
- [Holland et al 1991][research_hollandscottd_hodgejeffreys_1991]
- [Holland et al 2000][research_holland_woods_2000]
- [Holland et al 2001][research_holland_woods_2001]
- [Hollis and Perkins 1996][research_hollis_perkins_1996]
- [Hollmeier et al 1999][research_hollmeier_kopp_1999]
- [Holloway and Limerick 1993][research_holloway_limerick_1993]
- [Holman 2023][research_holman_2023]
- [Holmquist et al 1998][research_holmquist_recina_1998]
- [Holmquist et al 1999][research_holmquist_recina_1999]
- [Hong-jun and Qing 2015][research_hongjun_qing_2015]
- [Hongbo and Yongyuan 2016][research_hongbo_yongyuan_2016]
- [Hongpeng and Weiqiang 2016][research_hongpeng_weiqiang_2016]
- [Hopkins and Keener 1968][research_hopkins_keener_1968]
- [Hopkins et al 1979][research_hopkins_konopka_1979]
- [Hordon 1973][research_hordon_1973]
- [Horing et al 2025][research_horing_maute_2025]
- [Horing et al 2025][research_horing_maute_2025_b]
- [Hornbeck 1975][research_hornbeck_1975]
- [Horsley et al 1990][research_horsley_kroenke_1990]
- [Horstman 1969][research_horstman_1969]
- [Hoseinzade and Kim 2024][research_hoseinzade_kim_2024]
- [Hoseinzade and Kim 2024][research_hoseinzade_kim_2024_b]
- [Hoseinzade et al 2025][research_hoseinzade_lakzian_2025]
- [Hoskin et al 2024][research_hoskin_nguyen_2024]
- [Hossain 2025][research_hossain_2025]
- [Hoter et al 2026][research_hoter_2026]
- [Hoult et al 2003][research_hoult_starkey_2003]
- [Howard 2024][research_howard_2024]
- [Hsia 1992][research_hsia_1992]
- [Hsia 1993][research_hsia_1993]
- [Hsia et al 1989][research_hsia_gross_1989]
- [Hsia et al 1991][research_hsia_daso_1991]
- [Hsu and Liou 1991][research_hsu_liou_1991]
- [Hu and Mahadevan 2019][research_hu_mahadevan_2019]
- [Hu et al 2015][research_hu_chang_2015]
- [Hu et al 2015][research_hu_deng_2015]
- [Hu et al 2016][research_hu_pan_2016]
- [Hu et al 2022][research_hu_liu_2022]
- [Hu et al 2023][research_hu_cheng_2023]
- [Hu et al 2025][research_hu_guo_2025]
- [Hu et al 2026][research_hu_li_2026]
- [Hu et al 2026][research_hu_zheng_2026]
- [Huang 2021][research_huang_2021]
- [Huang and Friedmann 2020][research_huang_friedmann_2020]
- [Huang and Friedmann 2020][research_huang_friedmann_2020_b]
- [Huang and Yan 2016][research_huang_yan_2016]
- [Huang and Yao 2020][research_huang_yao_2020]
- [Huang et al 1998][research_huang_wang_1998]
- [Huang et al 2017][research_huang_tan_2017]
- [Huang et al 2019][research_huang_du_2019]
- [Huang et al 2019][research_huang_friedmann_2019]
- [Huang et al 2021][research_huang_zhang_2021]
- [Huang et al 2022][research_huang_he_2022]
- [Huang et al 2022][research_huang_liu_2022]
- [Huang et al 2023][research_huang_xia_2023]
- [Huang et al 2024][research_huang_wang_2024]
- [Huang et al 2025][research_huang_li_2025]
- [Huang et al 2025][research_huang_li_2025_b]
- [Huang et al 2025][research_huang_ning_2025]
- [Huang et al 2025][research_huang_wang_2025]
- [Huang et al 2025][research_huang_zhao_2025]
- [Huang et al 2026][research_huang_chen_2026]
- [Huang et al 2026][research_huang_lu_2026]
- [Huang et al 2026][research_huang_wang_2026]
- [Hube 1968][research_hube_1968]
- [Hudgens and Trexler 1992][research_hudgensjuliea_trexlercarla_1992]
- [Huebner 1995][research_huebner_1995]
- [Huebner and Tatum 1991][research_huebner_tatum_1991]
- [Huebner and Tatum 1993][research_huebner_tatum_1993]
- [Huebner et al 1996][research_huebner_1996]
- [Huebner et al 2000][research_huebner_rock_2000]
- [Huebner et al 2001][research_huebner_rock_2001]
- [Huebner et al 2004][research_huebnerlawrenced_wittedavidw_2004]
- [Hueter and Turner 1998][research_hueteruwe_turnerjames_1998]
- [Hufgard et al 2023][research_hufgard_duernhofer_2023]
- [Hui-Sheng and Bei-Jing 2021][research_huisheng_beijing_2021]
- [Humphrey et al 1993][research_humphrey_brueckner_1993]
- [Hung and MacCormack 1977][research_hung_maccormack_1977]
- [Hunt 1995][research_huntjamesl_1995]
- [Hunt 2015][research_hunt_2015]
- [Hunt and Bohon 1974][research_hunt_bohon_1974]
- [Hunt and Eiswirth 1996][research_huntjamesl_eiswirthedwarda_1996]
- [Hunt and Hunt 2021][research_hunt_hunt_2021]
- [Hunt and Martin 1989][research_huntjamesl_martinjohng_1989]
- [Hunt and Martin 1992][research_hunt_martin_1992]
- [Hunt and McClinton 1997][research_huntjamesl_mcclintoncharlesr_1997]
- [Hunt and Rausch 1998][research_hunt_rausch_1998]
- [Hunter and McCurdy 2003][research_hunterjamese_mccurdydavidr_2003]
- [Hunter et al 2002][research_hunterje_mccurdydr_2002]
- [Huo and Yang 2015][research_huo_yang_2015]
- [Huo et al 2015][research_huo_cheng_2015]
- [Hutt et al 2001][research_hutt_mcarthur_2001]
- [Hwang et al 1995][research_hwangkyuc_tiwarisurrendran_1995]
- [Hydrogen Slush 2007][research_hydrogen_slush_2007]
- [Hyers 2009][research_hyers_2009]
- [Hyper-X Model Testing with 1996][research_hyper_x_model_1996]
- [Hypersonic Air-Breathing Flight Testing 2022][research_hypersonic_air_breathing_2022]
- [Hypersonic flight 2015][research_hypersonic_flight_2015]
- [Hypersonic flight regime and 2017][research_hypersonic_flight_2017]
- [Hypersonic Materials for Thermal Protection 2023][research_hypersonic_materials_2023]
- [Hypersonic Viscous Interactions 2006][research_hypersonic_viscous_2006]
- [Iaccarino et al 2010][research_iaccarino_pecnik_2010]
- [Ibadi et al 2026][research_ibadi_supriadi_2026]
- [Idris et al 2019][research_idris_saad_2019]
- [Ifti et al 2022][research_ifti_hermann_2022]
- [Ifti et al 2022][research_ifti_hermann_2022_b]
- [Ignition Delay Time for Silane/Hydrogen/Air Mixtures at Low Temperatures 2018][research_ignition_delay_2018]
- [Igra 2026][research_igra_2026]
- [Ikawa 1991][research_ikawa_1991]
- [Ikenson 2025][research_ikenson_2025]
- [Im and Do 2018][research_im_do_2018]
- [Im et al 1998][research_im_chen_1998]
- [Influence of the rising rate of backpressure on the upstream motion characteristics of the shock train in a scramjet isolator 2023][research_influence_of_2023]
- [Ingenito 2015][research_ingenito_2015]
- [Ingenito et al 2009][research_ingenito_bruno_2009]
- [Ingenito et al 2009][research_ingenito_bruno_2009_b]
- [Ingenito et al 2010][research_ingenito_bruno_2010]
- [Inger 1990][research_inger_1990]
- [Inger 1995][research_inger_1995]
- [Inger 1995][research_inger_1995_b]
- [Inger 1995][research_inger_1995_c]
- [Ingeri 1966][research_ingeri_1966]
- [Inman et al 2011][research_inmanjennifera_bathelbrettf_2011]
- [Inman et al 2013][research_inmanjennifera_bathelbrettf_2013]
- [Inoue and Yamamoto 1990][research_inoue_yamamoto_1990]
- [Instrumentation for Airbreathing Propulsion 1974][research_instrumentation_for_1974]
- [Instrumentation for In-Flight Determination 1974][research_instrumentation_for_1974_b]
- [Interstitially protected oxidation resistant carbon-carbon composite 1988][research_interstitially_protected_1988]
- [Introduction to Hypersonic Air-Breathing 2022][research_introduction_to_2022]
- [Investigation of mixing characteristics of gaseous kerosene scramjet combustor with an oxygen-supplemented strut 2023][research_investigation_of_2023]
- [Investigation of the Effect of Temperature on the Microstructural and Mechanical Properties of the Ultra-High Temperature Ceramic Composite ZrB2-SiC-TiC Using the Multi-Step Spark Plasma Sintering Method 2024][research_investigation_of_2024]
- [Inviscid High-Temperature Equilibrium Flows 2006][research_inviscid_high_temperature_2006]
- [Irimpan et al 2015][research_irimpan_mannil_2015]
- [Isaac and Miles 1990][research_isaac_miles_1990]
- [Isaac et al 1959][research_isaac_williams_1959]
- [Ishihara et al 2015][research_ishihara_ogino_2015]
- [Ishihara et al 2016][research_ishihara_ogino_2016]
- [Ishimoto et al 1996][research_ishimoto_takizawa_1996]
- [Isono 2026][research_isono_2026]
- [Isono and Fujikawa 2025][research_isono_fujikawa_2025]
- [Ispir et al 2023][research_ispir_saracoglu_2023]
- [Ispir et al 2023][research_ispir_zdybal_2023]
- [Itoh 2007][research_itoh_2007]
- [Itoh et al 2002][research_itoh_ueda_2002]
- [Ivanov et al 1998][research_ivanov_markelov_1998]
- [Izenson 1991][research_izenson_1991]
- [Jachimowski 1974][research_jachimowskicj_1974]
- [Jachimowski and McLain 1983][research_jachimowskicj_mclainag_1983]
- [Jackman et al 1992][research_jackman_douglas_1992]
- [Jackson and Blanchard 1964][research_jackson_blanchard_1964]
- [Jackson and Wang 1974][research_jackson_wang_1974]
- [Jackson et al 2011][research_jackson_gruber_2011]
- [Jackson et al 2015][research_jackson_gruber_2015]
- [Jacobs et al 1990][research_jacobs_rogers_1990]
- [Jacobsen et al 2006][research_jacobsen_tam_2006]
- [Jalbert and Hiers 1993][research_jalbert_hiers_1993]
- [James 2024][research_james_2024]
- [James and Agrawal 2026][research_james_agrawal_2026]
- [Janiszewski and Woźniak 2022][research_janiszewski_wozniak_2022]
- [Javaid and Serghides 2003][research_javaid_serghides_2003]
- [Jawed and Nagle 1986][research_jawed_nagle_1986]
- [Jayaraman and Lewis 1997][research_jayaraman_lewis_1997]
- [Jazra and Smart 2011][research_jazra_smart_2011]
- [Jee and Etele 2020][research_jee_etele_2020]
- [Jeffs et al 2026][research_jeffs_newton_2026]
- [Jenkins 2000][research_jenkins_2000]
- [Jensen et al 1972][research_jensenrm_bryceca_1972]
- [Jeong and Choi 2020][research_jeong_choi_2020]
- [Jeong et al 2023][research_jeong_lee_2023]
- [Jeong et al 2024][research_jeong_kim_2024]
- [Jeong et al 2024][research_jeong_kim_2024_b]
- [Jeong et al 2025][research_jeong_kim_2025]
- [Jessen and Grönig 1995][research_jessen_gronig_1995]
- [Jewell et al 2013][research_jewell_shepherd_2013]
- [Jewell et al 2017][research_jewell_miller_2017]
- [Jha et al 1991][research_jha_forster_1991]
- [Ji and Xie 2022][research_ji_xie_2022]
- [Ji et al 2019][research_ji_li_2019]
- [Ji et al 2019][research_ji_zhang_2019]
- [Ji et al 2024][research_ji_he_2024]
- [Jia et al 2019][research_jia_ye_2019]
- [Jia et al 2020][research_jia_fu_2020]
- [Jia et al 2020][research_jia_fu_2020_b]
- [Jiang 2014][research_jiang_2014]
- [Jiang 2023][research_jiang_2023]
- [Jiang and Yu 2015][research_jiang_yu_2015]
- [Jiang and Yu 2019][research_jiang_yu_2019]
- [Jiang et al 2017][research_jiang_wang_2017]
- [Jiang et al 2021][research_jiang_zhang_2021]
- [Jiang et al 2022][research_jiang_liu_2022]
- [Jiang et al 2023][research_jiang_wang_2023]
- [Jiang et al 2023][research_jiang_wang_2023_b]
- [Jiang et al 2023][research_jiang_wang_2023_c]
- [Jiang et al 2025][research_jiang_liu_2025]
- [Jiang et al 2025][research_jiang_xu_2025]
- [Jiang et al 2025][research_jiang_zhan_2025]
- [Jiao et al 2015][research_jiao_chang_2015]
- [Jiao et al 2016][research_jiao_chang_2016]
- [Jiao et al 2016][research_jiao_chang_2016_b]
- [Jiao et al 2017][research_jiao_chang_2017]
- [Jiao et al 2017][research_jiao_wang_2017]
- [Jiao et al 2018][research_jiao_chang_2018]
- [Jieyan and Yuan 2022][research_jieyan_yuan_2022]
- [Jin and Yao 2023][research_jin_yao_2023]
- [Jin et al 2015][research_jin_luo_2015]
- [Jin et al 2017][research_jin_jing_2017]
- [Jin et al 2024][research_jin_zhao_2024]
- [Jing et al 2007][research_jing_shuo_2007]
- [Jing et al 2026][research_jing_song_2026]
- [Jingqi and Yulong 2024][research_jingqi_yulong_2024]
- [Jo and Choi 2026][research_jo_choi_2026]
- [Jo et al 2026][research_jo_sung_2026]
- [Jobart et al 1994][research_jobart_blandin_1994]
- [Johnson 1967][research_johnson_1967]
- [Johnson 1991][research_johnson_1991]
- [Johnson and Mirdamadi 1993][research_johnson_mirdamadi_1993]
- [Johnson and Mirdamadi 1994][research_johnson_mirdamadi_1994]
- [Johnson and Narayanaswamy 2024][research_johnson_narayanaswamy_2024]
- [Johnson and Weeks 2005][research_johnson_weeks_2005]
- [Johnson and Wu 1975][research_johnson_wu_1975]
- [Johnson et al 1993][research_johnsondl_hillck_1993]
- [Johnson et al 1996][research_johnson_mirdamadi_1996]
- [Johnson et al 1998][research_johnson_seipp_1998]
- [Johnson et al 1998][research_johnsontheodoref_natividadroderick_1998]
- [Johnson et al 2005][research_johnsontheodoref_natividadroderick_2005]
- [Johnson et al 2022][research_johnson_jenquin_2022]
- [Johnson III and Wu 1974][research_johnsoniii_wu_1974]
- [Johnson May et al 2024][research_johnsonmay_weber_2024]
- [Johnston et al 1971][research_johnston_cubbage_1971]
- [Johnston et al 1978][research_johnston_pittman_1978_b]
- [Johnston et al 1987][research_johnstonpatrickj_whiteheadallenhjr_1987]
- [Jones 1994][research_joneskennethm_1994]
- [Jones 2006][research_jones_2006]
- [Jones 2011][research_jones_2011]
- [Jones and Huber 1978][research_jonesra_huberpw_1978]
- [Jones et al 1992][research_jones_myrabo_1992]
- [Jorris 2014][research_jorris_2014]
- [Joshi and Lu 2016][research_joshi_lu_2016]
- [Joshi and Lu 2017][research_joshi_lu_2017]
- [Joyce et al 2005][research_joyce_pomroy_2005]
- [Ju and Niioka 1994][research_ju_niioka_1994]
- [Ju and Niioka 1994][research_ju_niioka_1994_b]
- [Ju and Niioka 1995][research_ju_niioka_1995]
- [Ju et al 2022][research_ju_liu_2022]
- [Jules and Barnhart 1998][research_juleskenol_barnhartpaulj_1998]
- [Juliano et al 2015][research_juliano_adamczak_2015]
- [Juluru Sandeep and Avss Kumara Swami Gupta 2023][research_julurusandeep_avsskumaraswamigupta_2023]
- [Jun et al 2026][research_jun_yang_2026]
- [Junaid R and Beebi M 2015][research_junaidr_beebim_2015]
- [Jung et al 2017][research_jung_han_2017]
- [Kaemming et al 2017][research_kaemming_fotia_2017]
- [Kahre 1987][research_kahre_1987]
- [Kai-li and Kun-yuan 2010][research_kaili_kunyuan_2010]
- [Kalaiarassan et al 2018][research_kalaiarassan_krishan_2018]
- [Kaltreider 1951][research_kaltreider_1951]
- [Kamal 2025][research_kamal_2025]
- [Kamath and McClinton 1992][research_kamath_mcclinton_1992]
- [Kamath et al 1990][research_kamathpradeeps_bakernr_1990]
- [Kamath et al 1991][research_kamath_mao_1991]
- [Kamel et al 2015][research_kamel_owis_2015]
- [Kanapathipillai and Yu 2024][research_kanapathipillai_yu_2024]
- [Kanda 1998][research_kanda_1998]
- [Kanda 2000][research_kanda_2000]
- [Kanda and Inagaki 2024][research_kanda_inagaki_2024]
- [Kanda et al 1989][research_kanda_komuro_1989]
- [Kanda et al 1991][research_kanda_masuya_1991]
- [Kanda et al 1994][research_kanda_masuya_1994]
- [Kanda et al 2003][research_kanda_hiraiwa_2003]
- [Kanda et al 2004][research_kanda_hiraiwa_2004]
- [Kanda et al 2020][research_kanda_katano_2020]
- [Kandula and Kummitha 2025][research_kandula_kummitha_2025]
- [Kang 1970][research_kang_1970]
- [Kang et al 2010][research_kang_lee_2010]
- [Kang et al 2018][research_kang_kim_2018]
- [Kang et al 2026][research_kang_yan_2026]
- [Karabacak and Turan 2023][research_karabacak_turan_2023]
- [Karanian and Kepler 1965][research_karanianaj_keplerce_1965]
- [Karasopoulos and Langan 1992][research_karasopoulos_langan_1992]
- [Kardas 2023][research_kardas_2023]
- [Karl and Steelant 2018][research_karl_steelant_2018]
- [Karl et al 2006][research_karl_hannemann_2006]
- [Karl et al 2008][research_karl_hannemann_2008]
- [Karl et al 2012][research_karl_laurence_2012]
- [Karlgaard et al 2004][research_karlgaard_tartabini_2004]
- [Karlgaard et al 2005][research_karlgaard_martin_2005]
- [Karpenko et al 2023][research_karpenko_tolstoguzov_2023]
- [Kaskan and Reuther 1977][research_kaskan_reuther_1977]
- [Kasten 1991][research_kasten_1991]
- [Kauffman et al 1990][research_kauffman_grandhi_1990]
- [Kauffman et al 1991][research_kauffman_grandhi_1991]
- [Kaufman 1963][research_kaufman_1963]
- [Kaufman 1988][research_kaufmanalbert_1988]
- [Kaufman and Louis G. 1963][research_kaufman_louisg_1963]
- [Kaufman and Louis G. 1964][research_kaufman_louisg_1964]
- [Kaul 1989][research_kaulupenderk_1989]
- [Kaul 1991][research_kaul_1991]
- [Kavoosi et al 2026][research_kavoosi_mashhadi_2026]
- [Kawalec et al 2023][research_kawalec_wolanski_2023]
- [Kazmar 2002][research_kazmar_2002]
- [Kazmar 2005][research_kazmar_2005]
- [Ke et al 2025][research_ke_wang_2025]
- [Keener 1992][research_keener_1992]
- [Keener et al 1994][research_keener_spaid_1994]
- [Keer et al 1994][research_keer_faber_1994]
- [Kehoe and Ricketts 1992][research_kehoe_ricketts_1992]
- [Kelly 1973][research_kelly_1973]
- [Kelly and Blosser 1992][research_kellyhneale_blossermaxl_1992]
- [Kelly and Blosser 1994][research_kellyhneale_blossermaxl_1994]
- [Kelly and Wieting 1984][research_kellyhn_wietingar_1984]
- [Kerrebrock 1992][research_kerrebrock_1992]
- [Kerrebrock and Poferl 1984][research_kerrebrockjackl_poferldavidj_1984]
- [Kerth et al 2024][research_kerth_lepage_2024]
- [Keshmiri et al 2006][research_keshmiri_colgren_2006]
- [Khali and Yao 2018][research_khali_yao_2018]
- [Khambaswadkar 2024][research_khambaswadkar_2024]
- [Khamlak 2026][research_khamlak_2026]
- [Khan and Chakraborty 2023][research_khan_chakraborty_2023]
- [Khan and Riccio 2024][research_khan_riccio_2024]
- [Kharitonov and Chernykh 1974][research_kharitonov_chernykh_1974]
- [Khrapko 2018][research_khrapko_2018]
- [Kianvashrad and Knight 2019][research_kianvashrad_knight_2019]
- [Kibbey 2019][research_kibbeytim_2019]
- [Kidd et al 2014][research_kidd_narayanaswamy_2014]
- [Kiehn 2020][research_kiehn_2020]
- [Kim 2018][research_kim_2018]
- [Kim and Choi 2026][research_kim_choi_2026]
- [Kim and Kwon 2017][research_kim_kwon_2017]
- [Kim and Kwon 2018][research_kim_kwon_2018]
- [Kim and Lee 2024][research_kim_lee_2024]
- [Kim and Park 2020][research_kim_park_2020]
- [Kim et al 1982][research_kim_rasmussen_1982]
- [Kim et al 2011][research_kimhyoungjin_kumanotakayasu_2011]
- [Kim et al 2019][research_kim_park_2019]
- [Kim et al 2020][research_kim_jang_2020]
- [Kim et al 2021][research_kim_choi_2021]
- [Kim et al 2021][research_kim_lee_2021]
- [Kim et al 2022][research_kim_jang_2022]
- [Kim et al 2022][research_kim_seo_2022]
- [Kim et al 2024][research_kim_shim_2024]
- [Kim et al 2025][research_kim_park_2025]
- [Kim et al 2025][research_kim_seo_2025]
- [Kim et al 2025][research_kim_shim_2025]
- [Kimmel 2008][research_kimmel_2008]
- [Kimmel 2008][research_kimmel_2008_b]
- [Kimmel et al 2011][research_kimmel_adamczak_2011]
- [Kimmel et al 2014][research_kimmel_adamczak_2014]
- [Kimmel et al 2015][research_kimmel_borg_2015]
- [Kimmerly 2024][research_kimmerly_2024]
- [Kimura 1993][research_kimura_1993]
- [Kimura et al 1976][research_kimura_shibusa_1976]
- [Kindler et al 2008][research_kindler_blacha_2008]
- [Kinslow et al 1973][research_kinslow_busby_1973]
- [Kireeti et al 2022][research_kireeti_ravikiransastry_2022]
- [Kirik et al 2018][research_kirik_goyne_2018]
- [Kirkby 1964][research_kirkby_1964]
- [Kirsch et al 2025][research_kirsch_krueger_2025]
- [Kishida 2006][research_kishida_2006]
- [Kishore N et al 2023][research_kishoren_gugulothu_2023]
- [Klein et al 2017][research_klein_chakraborty_2017]
- [Kline and Alonso 2017][research_kline_alonso_2017]
- [Kloesel et al 2011][research_kloesel_ratnayake_2011]
- [Klothakis and Nikolos 2024][research_klothakis_nikolos_2024]
- [Klothakis and Nikolos 2024][research_klothakis_nikolos_2024_b]
- [Knight 2015][research_knight_2015]
- [Knight and Naiman 2009][research_knight_naiman_2009]
- [Ko and Gong 2000][research_ko_gong_2000]
- [Ko and Gong 2001][research_ko_gong_2001]
- [Ko et al 2024][research_ko_son_2024]
- [Ko et al 2025][research_ko_mannion_2025]
- [Ko et al 2026][research_ko_son_2026]
- [Kobayashi et al 1990][research_kobayashi_yoshihara_1990]
- [Kocaaslan 2024][research_kocaaslan_2024]
- [Koch et al 2025][research_koch_wilken_2025]
- [Kocher and Keller 1969][research_kocher_keller_1969]
- [Kodera et al 2005][research_kodera_sunami_2005]
- [Koeplinger et al 2026][research_koeplinger_2026]
- [Kohl 1993][research_kohl_1993]
- [Kojima et al 2015][research_kojima_taguchi_2015]
- [Kolimi Abdul Ahad 2021][research_kolimiabdulahad_2021]
- [Kong et al 2020][research_kong_chang_2020]
- [Kong et al 2023][research_kong_lee_2023]
- [Kong et al 2024][research_kong_wang_2024]
- [Koo et al 2015][research_koo_raman_2015]
- [Koo et al 2023][research_koo_lee_2023]
- [Kopp et al 1999][research_kopp_hollmeier_1999]
- [Kors 1988][research_kors_1988]
- [Korte 2000][research_kortejj_2000]
- [Korte et al 1993][research_kortejohnj_singhdj_1993]
- [Koschel 1996][research_koschel_1996]
- [Koschel and Rick 1991][research_koschel_rick_1991]
- [Koubek 1963][research_koubek_1963]
- [Kouchi et al 2015][research_kouchi_goyne_2015]
- [Kourtides 1993][research_kourtides_1993]
- [Kowbel et al 1993][research_kowbel_huang_1993]
- [Kramer and Buhler 1980][research_kramer_buhler_1980]
- [Kremeyer and Pakhomov 2008][research_kremeyer_pakhomov_2008]
- [Kreutz and Law 1996][research_kreutz_law_1996]
- [Krieger 1990][research_krieger_1990]
- [Krishamurthy 1993][research_krishamurthyramesh_1993]
- [Krivosheyev et al 2024][research_krivosheyev_kisel_2024]
- [Krouse and Ellis 1966][research_krouse_ellis_1966]
- [Kshetrimayum et al 2021][research_kshetrimayum_menezes_2021]
- [Kulkarni et al 2026][research_kulkarni_gujar_2026]
- [Kumakawa 1989][research_kumakawa_1989]
- [Kumar 1981][research_kumar_1981]
- [Kumar 1982][research_kumar_1982]
- [Kumar 1982][research_kumar_1982_b]
- [Kumar and Mahulikar 2016][research_kumar_mahulikar_2016]
- [Kumar and Mahulikar 2017][research_kumar_mahulikar_2017]
- [Kumar and Rana 2024][research_kumar_rana_2024]
- [Kumar and Ranjan 2026][research_kumar_ranjan_2026]
- [Kumar and Ranjan 2026][research_kumar_ranjan_2026_b]
- [Kumar and Ranjan 2026][research_kumar_ranjan_2026_c]
- [Kumar and Reddy 2018][research_kumar_reddy_2018]
- [Kumar and Thornber 2016][research_kumar_thornber_2016]
- [Kumar et al 2017][research_kumar_rakesh_2017]
- [Kumar et al 2018][research_kumar_penchalaiah_2018]
- [Kumar et al 2018][research_kumar_sarkar_2018]
- [Kummitha 2017][research_kummitha_2017]
- [Kummitha 2022][research_kummitha_2022]
- [Kummitha 2024][research_kummitha_2024]
- [Kummitha and Kandula 2024][research_kummitha_kandula_2024]
- [Kummitha and Kandula 2025][research_kummitha_kandula_2025]
- [Kummitha and Pandey 2020][research_kummitha_pandey_2020]
- [Kummitha and Pandey 2021][research_kummitha_pandey_2021]
- [Kummitha et al 2017][research_kummitha_suneetha_2017]
- [Kummitha et al 2018][research_kummitha_pandey_2018]
- [Kunze 2020][research_kunze_2020]
- [Kurade and Suryanarayana 2023][research_kurade_suryanarayana_2023]
- [Kuranov et al 2012][research_kuranov_korabelnikov_2012]
- [Kurosaka and Shimamura 2024][research_kurosaka_shimamura_2024]
- [Kurtz et al 2015][research_kurtz_aizengendler_2015]
- [Kurtz et al 2016][research_kurtz_aizengendler_2016]
- [Kussoy et al 1992][research_kussoy_menter_1992]
- [Kutschenreuter 1962][research_kutschenreuter_1962]
- [Kutschenreuter 1992][research_kutschenreuterpaul_1992]
- [Kutschenreuter and Balent 1965][research_kutschenreuter_balent_1965]
- [Kutschenreuter et al 1966][research_kutschenreuter_paulh_1966]
- [Kydd and Mullaney 1961][research_kydd_mullaney_1961]
- [Labbe et al 2009][research_labbe_gilbert_2009]
- [Labib and King 2015][research_labib_king_2015]
- [Labib and King 2015][research_labib_king_2015_b]
- [Lacaze et al 2017][research_lacaze_vane_2017]
- [Ladeinde 2019][research_ladeinde_2019]
- [Ladeinde 2021][research_ladeinde_2021]
- [Ladeinde and Lou 2018][research_ladeinde_lou_2018]
- [Ladeinde et al 2019][research_ladeinde_lou_2019]
- [Ladyzhenskii and Lipin 1966][research_ladyzhenskii_lipin_1966]
- [Ladyzhenskij 1963][research_ladyzhenskij_1963]
- [Lai et al 1993][research_laiht_kimsc_1993]
- [Lakka et al 2021][research_lakka_randive_2021]
- [Lam and Stollenwerk 1966][research_lam_stollenwerk_1966]
- [Lan et al 2025][research_lan_wang_2025]
- [Landiech et al 1990][research_landiech_aumasson_1990]
- [Landis and Denis 2003][research_landis_denis_2003]
- [Landsberg et al 2022][research_landsberg_curran_2022]
- [Lange et al 1953][research_lange_gieseler_1953]
- [Langener et al 2009][research_langener_myrabo_2009]
- [Langston et al 2016][research_langstonsarahl_langchristapherg_2016]
- [Lanshin 1993][research_lanshin_1993]
- [Lantz 1992][research_lantz_1992]
- [Larsson 2012][research_larsson_2012]
- [Larsson et al 2015][research_larsson_laurence_2015]
- [Latham et al 1972][research_lathamea_sorensonne_1972]
- [Laumakis and Bonacuse 2001][research_laumakis_bonacuse_2001]
- [Laurence et al 2012][research_laurence_martinezschramm_2012]
- [Laurence et al 2015][research_laurence_karl_2015]
- [Law 2004][research_law_2004]
- [Law et al 1989][research_law_metghalchi_1989]
- [Lawing and Johnson 1978][research_lawingpl_johnsoncb_1978]
- [Lawrence 1991][research_lawrencescottl_1991]
- [Lawrence 1992][research_lawrencescottl_1992]
- [Le et al 2009][research_le_liu_2009]
- [Le et al 2023][research_le_liu_2023]
- [Leamer and Kennon 1978][research_leamerpc_kennonig_1978]
- [Lear et al 2008][research_lear_mcgrath_2008]
- [Lebedev et al 1969][research_lebedev_minostsev_1969]
- [Lederer et al 1991][research_lederer_schwab_1991]
- [Lee and Bae 2023][research_lee_bae_2023]
- [Lee and Kang 2019][research_lee_kang_2019]
- [Lee and Kang 2020][research_lee_kang_2020]
- [Lee and Lewis 1991][research_lee_lewis_1991]
- [Lee and Mitani 1999][research_lee_mitani_1999]
- [Lee et al 1990][research_lee_gupta_1990]
- [Lee et al 2012][research_lee_kang_2012]
- [Lee et al 2013][research_lee_yang_2013]
- [Lee et al 2015][research_lee_kang_2015]
- [Lee et al 2015][research_lee_yang_2015]
- [Lee et al 2018][research_lee_na_2018]
- [Lee et al 2020][research_lee_kim_2020]
- [Lee et al 2021][research_lee_ryu_2021]
- [Lee et al 2022][research_lee_duan_2022]
- [Lee et al 2022][research_lee_yang_2022]
- [Lee et al 2022][research_lee_yang_2022_b]
- [Lee et al 2023][research_lee_lee_2023]
- [Lee et al 2026][research_lee_jo_2026]
- [Lees 1956][research_lees_1956]
- [Lees 1957][research_lees_1957]
- [Lees and Kubota 1972][research_lees_kubota_1972]
- [Lefieux et al 2021][research_lefieux_garnier_2021]
- [Lehmusto et al 2024][research_lehmusto_ievlev_2024]
- [Lehrach 1987][research_lehrach_1987]
- [Lehtinen and Zeller 1972][research_lehtinen_zeller_1972]
- [Lehtinen et al 1978][research_lehtinenb_zellerjr_1978]
- [Lei 1992][research_lei_1992]
- [Lei et al 2023][research_lei_zhang_2023]
- [Leingang 1992][research_leingang_1992]
- [Leingang and Stull 1992][research_leingangjl_stullfd_1992]
- [Lemcoe 1992][research_lemcoemm_1992]
- [Lenard et al 1962][research_lenard_long_1962]
- [Leng et al 2024][research_leng_wang_2024]
- [Leonard et al 2005][research_leonard_amundsen_2005]
- [Lepsch and Naftel 1992][research_lepsch_naftel_1992]
- [Lepsch and Naftel 1993][research_lepsch_naftel_1993]
- [Lepsch et al 1991][research_lepsch_stanley_1991]
- [Lerner and McIntosh 1968][research_lernerji_mcintoshscjr_1968]
- [Levensteins and Krumins 1967][research_levensteins_krumins_1967]
- [Levermore and Brio 1994][research_levermore_brio_1994]
- [Levin 2015][research_levin_2015]
- [Lewis 1993][research_lewis_1993]
- [Lewis 2003][research_lewis_2003]
- [Lewis and Hastings 1989][research_lewis_hastings_1989]
- [Lewis et al 1963][research_lewis_burgess_1963]
- [Li 2020][research_li_2020]
- [Li 2020][research_li_2020_b]
- [Li 2021][research_li_2021]
- [Li 2022][research_li_2022]
- [Li 2022][research_li_2022_b]
- [Li and Ladeinde 2019][research_li_ladeinde_2019]
- [Li and Luo 2012][research_li_luo_2012]
- [Li and Su 2025][research_li_su_2025]
- [Li and Wang 2017][research_li_wang_2017]
- [Li and Wang 2017][research_li_wang_2017_b]
- [Li and Wang 2019][research_li_z_2019]
- [Li and Wey 1988][research_li_wey_1988]
- [Li and Yang 2017][research_li_yang_2017]
- [Li and Zhang 2026][research_li_zhang_2026]
- [Li and Zheng 2023][research_li_zheng_2023]
- [Li et al 1993][research_li_yang_1993]
- [Li et al 2009][research_li_yu_2009]
- [Li et al 2012][research_li_song_2012]
- [Li et al 2014][research_li_hong_2014]
- [Li et al 2014][research_li_song_2014]
- [Li et al 2015][research_li_song_2015]
- [Li et al 2016][research_li_yang_2016]
- [Li et al 2017][research_li_jin_2017]
- [Li et al 2017][research_li_liu_2017]
- [Li et al 2018][research_li_huang_2018]
- [Li et al 2018][research_li_jiao_2018]
- [Li et al 2018][research_li_li_2018]
- [Li et al 2018][research_li_liu_2018]
- [Li et al 2018][research_li_liu_2018_b]
- [Li et al 2018][research_li_sun_2018]
- [Li et al 2018][research_li_zhang_2018]
- [Li et al 2019][research_li_chen_2019]
- [Li et al 2019][research_li_jiao_2019]
- [Li et al 2019][research_li_liao_2019]
- [Li et al 2019][research_li_qin_2019]
- [Li et al 2019][research_li_wang_2019]
- [Li et al 2020][research_li_huang_2020]
- [Li et al 2020][research_li_xie_2020]
- [Li et al 2020][research_li_yang_2020]
- [Li et al 2021][research_li_jin_2021]
- [Li et al 2021][research_li_liu_2021]
- [Li et al 2021][research_li_reynaud_2021]
- [Li et al 2021][research_li_wang_2021]
- [Li et al 2022][research_li_cao_2022]
- [Li et al 2022][research_li_chen_2022]
- [Li et al 2022][research_li_choudhari_2022]
- [Li et al 2022][research_li_li_2022]
- [Li et al 2022][research_li_lin_2022]
- [Li et al 2022][research_li_wang_2022]
- [Li et al 2022][research_li_xu_2022]
- [Li et al 2022][research_li_yue_2022]
- [Li et al 2022][research_li_zeng_2022]
- [Li et al 2023][research_li_leng_2023]
- [Li et al 2023][research_li_li_2023]
- [Li et al 2023][research_li_sun_2023]
- [Li et al 2023][research_li_wang_2023]
- [Li et al 2023][research_li_xia_2023]
- [Li et al 2024][research_li_huang_2024]
- [Li et al 2024][research_li_li_2024]
- [Li et al 2024][research_li_sun_2024]
- [Li et al 2024][research_li_wan_2024]
- [Li et al 2024][research_li_wang_2024]
- [Li et al 2024][research_li_wang_2024_b]
- [Li et al 2024][research_li_zeng_2024]
- [Li et al 2024][research_li_zhao_2024]
- [Li et al 2025][research_li_ji_2025]
- [Li et al 2025][research_li_li_2025]
- [Li et al 2025][research_li_liu_2025]
- [Li et al 2025][research_li_pan_2025]
- [Li et al 2025][research_li_ren_2025]
- [Li et al 2025][research_li_wang_2025]
- [Li et al 2025][research_li_wang_2025_b]
- [Li et al 2025][research_li_xu_2025]
- [Li et al 2025][research_li_zhang_2025]
- [Li et al 2026][research_li_feng_2026]
- [Li et al 2026][research_li_ji_2026]
- [Li et al 2026][research_li_jiao_2026]
- [Li et al 2026][research_li_pang_2026]
- [Li et al 2026][research_li_yang_2026]
- [Lian et al 2023][research_lian_tang_2023]
- [Lian et al 2025][research_lian_xiong_2025]
- [Liang et al 2016][research_liang_liu_2016]
- [Liang et al 2022][research_liang_huang_2022]
- [Liang et al 2022][research_liang_xu_2022]
- [Liang et al 2024][research_liang_guo_2024]
- [Liao et al 2023][research_liao_chu_2023]
- [Liao et al 2023][research_liao_song_2023]
- [Libby 1962][research_libby_1962]
- [Libby et al 1963][research_libby_fox_1963]
- [Libby et al 1963][research_libby_fox_1963_b]
- [Lidke et al 1987][research_lidke_poulin_1987]
- [Lillard et al 2011][research_lillardrandolphp_oliverabrandon_2011]
- [Lilley and Pengelly 1993][research_lilley_pengelly_1993]
- [Limerick 1991][research_limerick_1991]
- [Limerick 1994][research_limerick_1994]
- [Liming and Bing 2006][research_liming_bing_2006]
- [Lin and Shen 1997][research_lin_shen_1997]
- [Lin et al 2008][research_lin_baumann_2008]
- [Lipanov and Karskanov 2024][research_lipanov_karskanov_2024]
- [Lisagor 1990][research_lisagor_1990]
- [Lisiecki 2015][research_lisiecki_2015]
- [Lissenden et al 2019][research_lissenden_yalcin_2019]
- [Litchford et al 1999][research_litchfordronj_bityurinvalentinea_1999]
- [Litchford et al 2000][research_litchfordrj_colejw_2000]
- [Little 1992][research_littlete_1992]
- [Liu 1967][research_liu_1967]
- [Liu 2020][research_liu_2020]
- [Liu and Liu 2015][research_liu_liu_2015]
- [Liu and Liu 2016][research_liu_liu_2016_b]
- [Liu and Sogame 1969][research_liu_sogame_1969]
- [Liu and Wang 2025][research_liu_wang_2025]
- [Liu and Zhang 2019][research_liu_zhang_2019]
- [Liu et al 1995][research_liu_sheng_1995]
- [Liu et al 2002][research_liu_chen_2002]
- [Liu et al 2015][research_liu_yuan_2015]
- [Liu et al 2016][research_liu_liu_2016]
- [Liu et al 2017][research_liu_yuan_2017]
- [Liu et al 2017][research_liu_yuan_2017_b]
- [Liu et al 2017][research_liu_zhao_2017]
- [Liu et al 2018][research_liu_yan_2018]
- [Liu et al 2019][research_liu_baccarella_2019]
- [Liu et al 2019][research_liu_dong_2019]
- [Liu et al 2019][research_liu_fan_2019]
- [Liu et al 2019][research_liu_tong_2019]
- [Liu et al 2019][research_liu_wang_2019]
- [Liu et al 2020][research_liu_baccarella_2020]
- [Liu et al 2021][research_liu_liu_2021]
- [Liu et al 2021][research_liu_wang_2021]
- [Liu et al 2021][research_liu_xu_2021]
- [Liu et al 2021][research_liu_yuan_2021]
- [Liu et al 2022][research_liu_chen_2022]
- [Liu et al 2022][research_liu_kang_2022]
- [Liu et al 2022][research_liu_wu_2022]
- [Liu et al 2022][research_liu_yuan_2022]
- [Liu et al 2023][research_liu_dong_2023]
- [Liu et al 2023][research_liu_han_2023]
- [Liu et al 2023][research_liu_liu_2023]
- [Liu et al 2023][research_liu_luo_2023]
- [Liu et al 2023][research_liu_sun_2023]
- [Liu et al 2023][research_liu_yang_2023]
- [Liu et al 2024][research_liu_kuang_2024]
- [Liu et al 2024][research_liu_lu_2024]
- [Liu et al 2024][research_liu_pan_2024]
- [Liu et al 2024][research_liu_peng_2024]
- [Liu et al 2024][research_liu_wang_2024]
- [Liu et al 2024][research_liu_zhang_2024]
- [Liu et al 2025][research_liu_li_2025]
- [Liu et al 2025][research_liu_yang_2025]
- [Liu et al 2025][research_liu_zhang_2025]
- [Liu et al 2026][research_liu_tian_2026]
- [Liu et al 2026][research_liu_zhang_2026]
- [Liu et al 2026][research_liu_zheng_2026]
- [Livingston 1965][research_livingston_1965]
- [Lloyd 1959][research_lloyd_1959]
- [Lobb et al 1955][research_lobb_winkler_1955]
- [Lockman et al 1990][research_lockman_lawrence_1990]
- [Lockwood et al 1996][research_lockwood_petley_1996]
- [Loehle 2016][research_loehle_2016]
- [Loiseau et al 2015][research_loiseau_robinet_2015]
- [Lombard et al 1999][research_lombard_ghosh_1999]
- [Lominac and Boytos 1998][research_lominac_boytos_1998]
- [Lomo et al 2023][research_lomo_patel_2023]
- [Loney 1994][research_loney_1994]
- [Longbiao 2016][research_longbiao_2016]
- [Longbiao 2018][research_longbiao_2018]
- [Longbiao 2019][research_longbiao_2019]
- [Longbiao 2019][research_longbiao_2019_b]
- [Longbiao 2019][research_longbiao_2019_c]
- [Longstaff 1995][research_longstaff_1995]
- [Longwell and Weiss 1952][research_longwell_weiss_1952]
- [Lonkar and Panda 2026][research_lonkar_panda_2026]
- [Loomis 1994][research_loomismarkp_1994]
- [Lord et al 1960][research_lord_boersen_1960]
- [Lovell and Schmidt 1994][research_lovelltalan_schmidtdk_1994]
- [Low cycle fatigue of 2000][research_low_cycle_2000]
- [Lu 1993][research_luping_1993]
- [Lu and Zhou 2017][research_lu_zhou_2017]
- [Lu et al 2015][research_lu_zhansen_2015]
- [Lu et al 2024][research_lu_zhang_2024]
- [Lu et al 2025][research_lu_sheng_2025]
- [Lu et al 2025][research_lu_zhang_2025]
- [Lu et al 2025][research_lu_zhu_2025]
- [Lu et al 2026][research_lu_gang_2026]
- [Lubbock et al 2018][research_lubbock_luque_2018]
- [Ludwig and Sulzmann 1961][research_ludwig_sulzmann_1961]
- [Lukasiewicz 1961][research_lukasiewicz_1961]
- [Lumpkin and Chapman 1992][research_lumpkin_chapman_1992]
- [Luo et al 2012][research_luo_song_2012]
- [Luo et al 2019][research_luo_wang_2019]
- [Luo et al 2020][research_luo_wang_2020]
- [Luo et al 2021][research_luo_miao_2021]
- [Luo et al 2022][research_luo_sun_2022]
- [Luo et al 2024][research_luo_liu_2024]
- [Luo et al 2024][research_luo_qi_2024]
- [Luo et al 2024][research_luo_qu_2024]
- [Luo et al 2025][research_luo_li_2025]
- [Luo et al 2025][research_luo_luo_2025]
- [Luo et al 2025][research_luo_sun_2025]
- [Luo et al 2026][research_luo_chen_2026]
- [Luo et al 2026][research_luo_tang_2026]
- [Lusty and Miele 1966][research_lusty_miele_1966]
- [Lux-Baumann and Burkes 2005][research_jessicaluxbaumann_darrylaburkes_2005]
- [Lux-Baumann and Burkes 2006][research_luxbaumann_burkes_2006]
- [Lux-Baumann et al 2006][research_luxbaumann_dees_2006]
- [Lv et al 2015][research_lv_wang_2015]
- [Lv et al 2020][research_lv_chang_2020]
- [Lv et al 2020][research_lv_xu_2020]
- [Lv et al 2022][research_lv_chang_2022]
- [Lv et al 2022][research_lv_xu_2022]
- [Lv et al 2023][research_lv_huang_2023]
- [Lv et al 2026][research_lv_li_2026]
- [Lynch et al 2023][research_lynch_grasser_2023]
- [Lyu et al 2021][research_lyu_gao_2021]
- [Ma and Cai 2018][research_ma_cai_2018]
- [Ma and Cai 2018][research_ma_cai_2018_b]
- [Ma et al 2017][research_ma_yin_2017]
- [Ma et al 2019][research_ma_chang_2019]
- [Ma et al 2019][research_ma_chang_2019_b]
- [Ma et al 2021][research_ma_sun_2021]
- [Ma et al 2022][research_ma_jiang_2022]
- [Ma et al 2023][research_ma_jiang_2023]
- [Ma et al 2024][research_ma_yang_2024]
- [Ma et al 2024][research_ma_yang_2024_b]
- [Ma et al 2025][research_ma_guo_2025]
- [Ma et al 2025][research_ma_shu_2025]
- [Ma et al 2025][research_ma_zhao_2025]
- [Ma et al 2026][research_ma_fu_2026]
- [Ma et al 2026][research_ma_zhao_2026]
- [Maahs 1989][research_maahs_1989]
- [Maccormack and Candler 1988][research_maccormackrobertw_candlergrahamv_1988]
- [MacDermott et al 1965][research_macdermott_dix_1965]
- [Macheret et al 2005][research_macheret_shneider_2005]
- [Mack et al 2009][research_mack_steelant_2009]
- [MacKinnon et al 2004][research_mackinnon_beitel_2004]
- [MacLeod 2026][research_macleod_2026]
- [MacLeod et al 2025][research_macleod_gibson_2025]
- [Maddalon 1969][research_maddalon_1969]
- [Maglieri et al 1990][research_maglieridomenicj_sothcottvictore_1990]
- [Magnus et al 2020][research_magnus_sharp_2020]
- [Mahto et al 2016][research_mahto_choubey_2016]
- [Maikap and Rajagopal 2024][research_maikap_rajagopal_2024]
- [Maiorova et al 2016][research_maiorova_prosuntsov_2016]
- [Maisaia 2023][research_maisaia_2023]
- [Maita et al 1990][research_maita_ohkami_1990]
- [Makurunje et al 2021][research_makurunje_sigalas_2021]
- [Malakhov 2025][research_malakhov_2025]
- [Malakondaiah and Nicholas 1996][research_malakondaiah_nicholas_1996]
- [Malekipour et al 2021][research_malekipour_mohammadiamin_2021]
- [Malik and Anderson 1991][research_malik_anderson_1991]
- [Mall and Cunningham 2007][research_mall_cunningham_2007]
- [Malone and Peavey 1999][research_malonemichaelb_peaveycharlesc_1999]
- [Mandel et al 1977][research_mandelg_carpenterjljr_1977]
- [Mann and Garner 1977][research_mann_garner_1977]
- [Manna et al 2023][research_manna_dharavath_2023]
- [Mannion et al 2026][research_mannion_ko_2026]
- [Mannion et al 2026][research_mannion_ko_2026_b]
- [Manocha and Manocha 1995][research_manocha_manocha_1995]
- [Manski and Martin 1991][research_manski_martin_1991]
- [Manski et al 1997][research_manski_hagemann_1997]
- [Mao et al 2016][research_mao_zhang_2016]
- [Marchetti et al 2021][research_marchetti_minisci_2021]
- [Marcum 2001][research_marcum_2001]
- [Marek 2011][research_mareklindsayc_2011]
- [Marie et al 2019][research_marie_hideyuki_2019]
- [Marley and Driscoll 2022][research_marley_driscoll_2022]
- [Marschall 2011][research_marschall_2011]
- [Marsh and Sears 1954][research_marsh_sears_1954]
- [Marshall 1969][research_marshall_1969]
- [Marshall et al 1996][research_marshall_morris_1996]
- [Marshall et al 2005][research_marshall_bahm_2005]
- [Marshall et al 2005][research_marshall_corpening_2005]
- [Marshall et al 2014][research_marshall_cox_2014]
- [Martin 1977][research_martinaw_1977]
- [Martin 1978][research_martin_1978]
- [Martin 1992][research_martin_1992]
- [Martin 1995][research_martin_1995]
- [Martin and Boyd 2015][research_martin_boyd_2015]
- [Martin et al 1991][research_martin_kabis_1991]
- [Martinez Schramm et al 2008][research_martinezschramm_karl_2008]
- [Martinez Schramm et al 2024][research_martinezschramm_wagner_2024]
- [Marvin 1991][research_marvinjg_1991]
- [Marvin et al 2013][research_marvinjosephg_brownjamesl_2013]
- [Masad 1995][research_masad_1995]
- [Masahashi et al 1991][research_masahashi_mizuhara_1991]
- [Matarrese et al 1991][research_matarrese_messiter_1991]
- [Materials, Structures, and Thermal 2022][research_materials_structures_2022]
- [Mathavaraj and Padhi 2020][research_mathavaraj_padhi_2020]
- [Mathur and Singh 2024][research_mathur_singh_2024]
- [Matikas 2008][research_matikas_2008]
- [Matsuda 2015][research_matsuda_2015]
- [Matsui et al 2008][research_matsui_shinmi_2008]
- [Matsushima et al 1987][research_matsushima_takanashi_1987]
- [Mattern 1992][research_mattern_1992]
- [Matthew McGilvray 2024][research_matthewmcgilvray_2024]
- [Matthews and Trimmer 1969][research_matthews_trimmer_1969]
- [Matveev and Leachman 2023][research_matveev_leachman_2023]
- [Matveev and Leachman 2023][research_matveev_leachman_2023_b]
- [Maurice et al 1996][research_maurice_leingang_1996]
- [Maus et al 1984][research_maus_griffith_1984]
- [Maxwell and Goodwin 2017][research_maxwell_goodwin_2017]
- [Maxwell and Hoang 2016][research_maxwell_hoang_2016]
- [Mayer and Paynter 1994][research_mayer_paynter_1994]
- [Mayer and Paynter 1995][research_mayer_paynter_1995]
- [Mayhew and Norden 1995][research_mayhew_norden_1995]
- [Mbagwu et al 2023][research_mbagwu_dalle_2023]
- [McCandless and Cruz 1985][research_mccandless_cruz_1985]
- [McClinton 1976][research_mcclinton_1976]
- [McClinton 1978][research_mcclinton_1978]
- [McClinton and Anderson 1980][research_mcclintoncr_andersongy_1980]
- [McClinton and Gooderum 1977][research_mcclinton_gooderum_1977]
- [McClinton et al 1975][research_mcclintoncr_torrencemg_1975]
- [McClinton et al 1990][research_mcclinton_bittner_1990]
- [McClinton et al 1991][research_mcclinton_rondakov_1991]
- [McClinton et al 1998][research_mcclinton_holland_1998]
- [McClinton et al 1998][research_mcclinton_voland_1998]
- [McClinton et al 2001][research_crmcclinton_vlrausch_2001]
- [McClinton et al 2002][research_mcclinton_ferlemann_2002]
- [McClure and Andrews 1998][research_mcclure_andrews_1998]
- [McClure and Sirbaugh 1991][research_mcclure_sirbaugh_1991]
- [McCormick et al 2010][research_mccormick_wakayama_2010]
- [McDaniel 1998][research_mcdanieljr_1998]
- [McDaniel 2003][research_mcdaniel_2003]
- [McDaniel 2005][research_mcdaniel_2005]
- [McDaniel and Edwards 1999][research_mcdaniel_edwards_1999]
- [McDaniel and Edwards 2001][research_mcdaniel_edwards_2001]
- [McGann et al 2019][research_mcgann_lee_2019]
- [McGann et al 2026][research_mcgann_carter_2026]
- [McGilvray et al 2006][research_mcgilvray_jacobs_2006]
- [McGilvray et al 2010][research_mcgilvray_kirchhartz_2010]
- [McGilvray et al 2019][research_mcgilvray_neely_2019]
- [McGrory 2001][research_mcgrory_2001]
- [McIntosh 1972][research_mcintoshscjr_1972]
- [McINTOSH 1973][research_mcintosh_1973]
- [McIntyre et al 1998][research_mcintyre_bishop_1998]
- [McKee 1987][research_mckee_1987]
- [McNelis et al 1995][research_mcnelisnancyb_hardyterryl_1995]
- [McRae and Edwards 2001][research_mcrae_edwards_2001]
- [McRae and Neaves 1998][research_mcrae_neaves_1998]
- [McRae and Zikry 1999][research_mcrae_zikry_1999]
- [McTaggart 1973][research_mctaggart_1973]
- [McVey et al 1969][research_mcvey_rejeske_1969]
- [Md Salleh 2026][research_mdsalleh_2026]
- [Mease 1993][research_mease_1993]
- [Mease and Van Buren 1994][research_mease_vanburen_1994]
- [Mease and Vanburen 1989][research_measekennethd_vanburenmarka_1989]
- [Mease and Vinh 1988][research_mease_vinh_1988]
- [Measurement Techniques for Supersonic 1974][research_measurement_techniques_1974]
- [Mechanical and oxidation properties 1995][research_mechanical_and_1995]
- [Medina et al 2021][research_medina_patel_2021]
- [Medvedev et al 2016][research_medvedev_agafonov_2016]
- [Mee et al 1995][research_mee_daniel_1995]
- [Mehta 1990][research_mehta_1990]
- [Mehta 1992][research_mehta_1992]
- [Mehta 1993][research_mehta_1993]
- [Mehta 1994][research_mehtaunmeelb_1994]
- [Mehta 1995][research_mehtau_1995]
- [Mehta and Bowles 2001][research_mehta_bowles_2001]
- [Mehta and Kutler 1994][research_mehta_kutler_1994]
- [Mehta et al 2001][research_mehtaunmeelb_bogdanoffdavidw_2001]
- [Mei et al 2020][research_mei_shi_2020]
- [Meiss et al 2011][research_meiss_schroder_2011]
- [Melis and Gladden 1990][research_melis_gladden_1990]
- [Melis and Wang 1999][research_melis_wang_1999]
- [Melnik and Perini 1968][research_melnikwl_perinill_1968]
- [Mendham 2003][research_mendham_2003]
- [Mendiratta and Choudhury 1978][research_mendiratta_choudhury_1978]
- [Menees et al 1989][research_menees_bowles_1989]
- [Meng et al 2020][research_meng_ye_2020]
- [Meng et al 2021][research_meng_wan_2021]
- [Meng et al 2022][research_meng_shi_2022]
- [Meng et al 2022][research_meng_sun_2022]
- [Meng et al 2024][research_meng_jin_2024]
- [Meng et al 2024][research_meng_sun_2024]
- [Menon and Jou 1991][research_menon_jou_1991]
- [Menon et al 2025][research_menon_ck_2025]
- [Meritt and Schetz 2014][research_meritt_schetz_2014]
- [Merkli 1975][research_merkli_1975]
- [Merkli 1976][research_merkli_1976]
- [Meshcheryakov and Sabel'nikov 1988][research_meshcheryakov_sabelnikov_1988]
- [Meshcheryakov and Yashina 2015][research_meshcheryakov_yashina_2015]
- [Metghalchi 2009][research_metghalchi_2009]
- [Method and titanium aluminide 1993][research_method_and_1993]
- [Method for forming titanium aluminide-ductile titanium aluminium alloy matrix alloy composites 1991][research_method_for_1991]
- [Method for making a 1997][research_method_for_1997]
- [Method of fabricating titanium 1978][research_method_of_1978]
- [Method to fabricate titanium 1994][research_method_to_1994]
- [Method to produce metal 1990][research_method_to_1990]
- [Meuwly 2014][research_meuwly_2014]
- [Meyer 1959][research_meyer_1959]
- [Meyers et al 1974][research_meyers_feller_1974]
- [Miao et al 2020][research_miao_wang_2020]
- [Miao et al 2026][research_miao_wang_2026]
- [Michalski et al 2018][research_michalski_boust_2018]
- [Micol][research_johnrmicol]
- [Micol 1998][research_micoljr_1998]
- [Microstructural control of a titanium aluminide alloy 1997][research_microstructural_control_1997]
- [Midden and Miller 1985][research_middenraymonde_millercharlesgiii_1985]
- [Middleton et al 2011][research_middletontroyf_ballarobertjeffrey_2011]
- [Miele 1990][research_miele_1990]
- [Miele and Hull 1963][research_miele_hull_1963]
- [Miele and Pritchard 1963][research_miele_pritchard_1963]
- [Migdal and Greathouse 1968][research_migdal_greathouse_1968]
- [Miller 2000][research_miller_2000]
- [Miller et al 1993][research_miller_steinetz_1993]
- [Millerd 2025][research_millerd_2025]
- [Min et al 2026][research_min_son_2026]
- [Mirdamadi and Johnson 1994][research_mirdamadi_johnson_1994]
- [Miró Miró and Pinna 2017][research_miromiro_pinna_2017]
- [Mishra et al 1996][research_mishra_mukherjee_1996]
- [Mitani 1995][research_mitani_1995]
- [Mitani 1996][research_mitani_1996]
- [Mitani and Kouchi 2005][research_mitani_kouchi_2005]
- [Mitani et al 1996][research_mitani_hiraiwa_1996]
- [Mitani et al 1997][research_mitani_hiraiwa_1997]
- [Miyashita et al 2025][research_miyashita_sugihara_2025]
- [Mizener and Lu 2017][research_mizener_lu_2017]
- [Modroukas et al 1998][research_modroukas_betti_1998]
- [Mogavero and Brown 2018][research_mogavero_brown_2018]
- [Mohamad et al 2024][research_mohamad_ivan_2024]
- [Mohling 2018][research_mohling_2018]
- [Mohring et al 2021][research_mohring_gabler_2021]
- [Mohsen et al 2017][research_mohsen_yusoff_2017]
- [Moin and Lele 1998][research_moin_lele_1998]
- [Molchanov et al 2021][research_molchanov_gribinenko_2021]
- [Molder and Szpiro 1966][research_molder_szpiro_1966]
- [Molvik et al 1992][research_molvik_bowles_1992]
- [Molvik et al 1993][research_molvik_bowles_1993]
- [Molvik et al 1993][research_molvik_bowles_1993_b]
- [Monaghan 1959][research_monaghan_1959]
- [Mondal and Jagtap 2026][research_mondal_jagtap_2026]
- [Monroe and Boyd 2026][research_monroe_boyd_2026]
- [Montagne et al 1988][research_montagnejl_yeehc_1988]
- [Monteiro dos Santos Rodrigues da Silva and Leite 2025][research_monteirodossantosrodriguesdasilva_leite_2025]
- [Moon and Chung 1996][research_moon_chung_1996]
- [Moon et al 2000][research_moon_jeung_2000]
- [Moradian and Timofeev 2012][research_moradian_timofeev_2012]
- [Morelli 2008][research_morelli_2008]
- [Morelli et al 2005][research_morelli_derry_2005]
- [Morgan 1961][research_morgan_1961]
- [Morgan and Stalker 1985][research_morgan_stalker_1985]
- [Morgan et al 1985][research_morgan_paull_1985]
- [Morgan et al 1986][research_morgan_paull_1986]
- [Mori 1965][research_mori_1965]
- [Morinaga 1969][research_morinaga_1969]
- [Morris 1991][research_morris_1991]
- [Morris 1992][research_morris_1992]
- [Morris 1995][research_morrisjr_1995]
- [Morris et al 1976][research_morrissjjr_nelmswpjr_1976]
- [Moses 2003][research_moses_2003]
- [Moses 2003][research_moses_2003_b]
- [Moses et al 1999][research_mosespl_bouchardka_1999]
- [Moss and Perrell 2005][research_moss_perrell_2005]
- [Moss et al 1987][research_mossjamesn_simmondsannl_1987]
- [Moszee and Moszee 1997][research_moszee_moszee_1997]
- [Moszee and Snyder 1989][research_moszee_snyder_1989]
- [Mu et al 2022][research_mu_wang_2022]
- [Mukundan et al 2022][research_mukundan_maity_2022]
- [Mulard and Moules 1992][research_mulard_moules_1992]
- [Munk et al 2016][research_munk_vio_2016]
- [Murillo 2018][research_murillo_2018]
- [Murillo and Lu 2010][research_murillo_lu_2010]
- [Murray et al 2021][research_murray_smith_2021]
- [Murthy et al 2021][research_murthy_patel_2021]
- [Musielak and Musielak 1997][research_musielak_musielak_1997]
- [Myrabo et al 1986][research_myrabo_powers_1986]
- [M․V․V․ and Rajagopal 2026][research_mvv_rajagopal_2026]
- [Nadell et al 1992][research_nadellsharibeth_baumgartenwilliamj_1992]
- [Nadell et al 1992][research_nadellsharibeth_baumgartenwilliamj_1992_b]
- [Nag et al 2023][research_nag_senthil_2023]
- [Nagamatsu 1989][research_nagamatsu_1989]
- [Nagamatsu et al 1960][research_nagamatsu_geiger_1960]
- [Nagamatsu et al 1961][research_nagamatsu_sheer_1961]
- [Nagamatsu et al 1964][research_nagamatsu_graber_1964]
- [Nagawkar and Leifsson 2022][research_nagawkar_leifsson_2022]
- [Nagel 1967][research_nagel_1967]
- [Nagel and Becker 1973][research_nagel_becker_1973]
- [Nair et al 2003][research_nair_kumar_2003]
- [Nair et al 2023][research_nair_suryan_2023]
- [Nakaya et al 2015][research_nakaya_tsue_2015]
- [Nakaya et al 2021][research_nakaya_yamana_2021]
- [Nance 2013][research_nance_2013]
- [Nance et al 1997][research_nancerobertp_horvaththomasj_1997]
- [Nanda et al 2019][research_nanda_kulkarni_2019]
- [Narayan 1994][research_narayan_1994]
- [Narayan and Kumar 1989][research_narayanjr_kumara_1989]
- [Nardo and Sadler 1962][research_nardo_sadler_1962]
- [Nardo et al 1961][research_nardo_erickson_1961]
- [Naresh Kumar et al 2017][research_nareshkumar_ikram_2017]
- [NASA's HYPULSE Facility at 2002][research_nasa_s_hypulse_2002]
- [Nasir et al 2026][research_nasir_xie_2026]
- [NASP tests composites 1991][research_nasp_tests_1991]
- [Nastac and Frendi 2022][research_nastac_frendi_2022]
- [National Aero-Space Plane NASP 1990][research_national_aero_space_1990]
- [Natural environment requirements definition 1993][research_natural_environment_1993]
- [Naumann et al 1991][research_naumann_ende_1991]
- [Naumann et al 1992][research_naumann_ende_1992]
- [Naval Ordnance Test Station China Lake Ca 1957][research_navalordnanceteststationchinalakeca_1957]
- [Naved et al 2021][research_naved_hermann_2021]
- [Naveen Kumar 2020][research_g_2020]
- [Navó and Bergada 2020][research_navo_bergada_2020]
- [NBS Probes Hydrogen Slush 1965][research_nbs_probes_1965]
- [Nebylov and Tomita 1998][research_nebylov_tomita_1998]
- [Neek et al 2025][research_neek_najarmansour_2025]
- [Neely 2022][research_neely_2022]
- [Neely and Morgan 1995][research_neely_morgan_1995]
- [Neill and Pesyridis 2017][research_neill_pesyridis_2017]
- [Neiner et al 1978][research_neinergh_colegl_1978]
- [Nelson 1974][research_nelsonhg_1974]
- [Nelson 1988][research_nelsonhowardg_1988]
- [Nelson and Hawk 1997][research_knelson_clarkwhawk_1997]
- [Nelson and McArthur 2001][research_nelson_mcarthur_2001]
- [Neuenhahn et al 2006][research_neuenhahn_olivier_2006]
- [Neumann 1990][research_neumann_1990]
- [Neuwerth et al 1999][research_neuwerth_peiter_1999]
- [Next-Generation Aerospace Components Via Additive Manufacturing and Structural Optimization 2026][research_next_generation_aerospace_2026]
- [Neyland 1993][research_neyland_1993]
- [Ng et al 1986][research_ng_benson_1986]
- [Ng et al 1989][research_ng_ajmani_1989]
- [Ngo 2017][research_ngo_2017]
- [Ngoc Long 2016][research_ngoclong_2016]
- [Nguyen 1987][research_nguyen_1987]
- [Nguyen 1991][research_nguyen_1991]
- [Ni et al 2016][research_ni_lu_2016]
- [Nicolaou and Semiatin 1996][research_nicolaou_semiatin_1996]
- [Nicolaou and Semiatin 1997][research_nicolaou_semiatin_1997]
- [Nidharia et al 2024][research_nidharia_mane_2024]
- [Nie et al 2022][research_nie_song_2022]
- [Nie et al 2023][research_nie_wang_2023]
- [Nie et al 2023][research_nie_ye_2023]
- [Nie et al 2024][research_nie_he_2024]
- [Nie et al 2025][research_nie_qin_2025]
- [Nielsen et al 2021][research_nielsen_edwards_2021]
- [Nieto et al 2021][research_nieto_samayoa_2021]
- [Nikonov 2025][research_nikonov_2025]
- [Nishiguchi et al 2025][research_nishiguchi_kodera_2025]
- [Nishioka and Law 1997][research_nishioka_law_1997]
- [Niu and Chen 2024][research_niu_chen_2024]
- [Niu and Chen 2025][research_niu_chen_2025]
- [Niu and Chen 2026][research_niu_chen_2026]
- [Niu and Chen 2026][research_niu_chen_2026_b]
- [Niu and Su 2023][research_niu_su_2023]
- [niu and wang 2023][research_niu_wang_2023]
- [Nomura 1983][research_nomura_1983]
- [Non-empirical analytical model of 2019][research_non_empirical_analytical_2019]
- [Nordin-Bates et al 2017][research_nordinbates_fureby_2017]
- [Norman et al 1966][research_norman_walker_1966]
- [Norris 2017][research_norris_2017]
- [Novelli and Koschel 2001][research_novelli_koschel_2001]
- [Nowak and Kelly 1976][research_nowakrj_kellyhn_1976]
- [Numerical Analysis of Heat Flux Reduction by Transpiration Cooling in Laminar Hypersonic Flow 2026][research_numerical_analysis_2026]
- [Numerical Comparative Analysis of the Influence of Fuel Micro-Hole Geometry on the Combustion Characteristics of Hydrogen Micro-Mixing Combustor 2024][research_numerical_comparative_2024]
- [Numerical Optimization on Approach and Landing for Reusable Launch Vehicle 2016][research_numerical_optimization_2016]
- [Numerical Simulation of the Interaction of a Transverse Jet with Supersonic Flow Using Different Turbulence Models 2015][research_numerical_simulation_2015_b]
- [Numerical Simulation on Hypersonic Combustion of Hydrogen-Fueled Scramjet Combustor with Parallel Strut Fuel Injection at a Flight Mach Number of 7 2015][research_numerical_simulation_2015]
- [Numerical Study of Mixing in an Air-Breathing Rocket Engine 2015][research_numerical_study_2015]
- [Nurfathin Zahrolayali et al 2022][research_nurfathinzahrolayali_mohdrashdansaad_2022]
- [O'Byrne et al 1998][research_obyrne_doolan_1998]
- [O'Byrne et al 1999][research_obyrne_doolan_1999]
- [O'Byrne et al 2011][research_obyrne_wittig_2011]
- [O'Neill and Lewis 1992][research_oneill_lewis_1992]
- [O'Neill and Lewis 1992][research_oneillmarykael_lewismarkj_1992]
- [O'Neill and Lewis 1993][research_oneill_lewis_1993]
- [Oamjee and Sadanandan 2019][research_oamjee_sadanandan_2019]
- [Oamjee and Sadanandan 2020][research_oamjee_sadanandan_2020]
- [Oamjee and Sadanandan 2020][research_oamjee_sadanandan_2020_b]
- [Oberg 2015][research_oberg_2015]
- [Obery and Stitt 1958][research_oberylj_stittle_1958]
- [Odam and Paull 2003][research_odam_paull_2003]
- [Oerley et al 2012][research_oerley_gamba_2012]
- [Oertel 1970][research_oertel_1970]
- [Oertel and Fritz H. 1972][research_oertel_fritzh_1972]
- [Ogawa 2024][research_ogawa_2024]
- [Ogawa 2025][research_ogawa_2025]
- [Ogawa et al 2009][research_ogawa_grainger_2009]
- [Ohira 1999][research_ohira_1999]
- [Ohira 2002][research_ohira_2002]
- [Ohira 2004][research_ohira_2004]
- [Ohira 2016][research_ohira_2016]
- [Ohira et al 1994][research_ohira_matsuo_1994]
- [Ohlhorst et al 1990][research_ohlhorst_vaughn_1990]
- [Ohlhorst et al 1992][research_ohlhorst_vaughn_1992]
- [Ohlhorst et al 2005][research_ohlhorst_glass_2005]
- [Olds 1988][research_olds_1988]
- [Olds and Budianto 1998][research_olds_budianto_1998]
- [Olejniczak et al 1996][research_olejniczak_candler_1996]
- [Opacich and Ombrello 2026][research_opacich_ombrello_2026]
- [Opila 2003][research_opilaelizabethj_2003]
- [Optimal Aerodynamic Shapes Of 1996][research_optimal_aerodynamic_1996]
- [Orbital ATK tests 3D printed hypersonic engine combustor 2016][research_orbital_atk_2016]
- [Ormsbee 1962][research_ormsbee_1962]
- [Ortloff 1968][research_ortloff_1968]
- [Ortwerth and Goldman 1996][research_ortwerth_goldman_1996]
- [Osborne and Ghonem 2005][research_osborne_ghonem_2005]
- [Osgerby et al 1969][research_osgerby_smithson_1969]
- [Osgerby et al 1970][research_osgerby_smithson_1970]
- [Otsuka et al 1999][research_otsuka_sakamoto_1999]
- [Ou et al 2019][research_ou_yan_2019]
- [Ouzts 2008][research_ouzts_2008]
- [Ouzts et al 2009][research_ouzts_soloway_2009]
- [Owen and Horstman 1972][research_owenfk_horstmancc_1972]
- [Oxidation protection for carbon fibre composites 1990][research_oxidation_protection_1990]
- [Oz and Kara 2024][research_oz_kara_2024]
- [Pagilla 2019][research_pagilla_2019]
- [Pak 2008][research_pak_2008]
- [Palaszewski 1998][research_palaszewski_1998]
- [Pallela and Thakur 2025][research_pallela_thakur_2025]
- [Palmer 2021][research_palmer_2021]
- [Pamadi 1989][research_pamadi_1989]
- [Pamadi 1995][research_pamadi_1995]
- [Pamadi et al 2004][research_pamadi_tartabini_2004]
- [Pan et al 2018][research_pan_bi_2018]
- [Pan et al 2022][research_pan_xiong_2022]
- [Pan et al 2024][research_pan_wang_2024]
- [Pan et al 2024][research_pan_zhou_2024]
- [Pandey et al 2022][research_pandey_soni_2022]
- [Paredes and Theofilis 2015][research_paredes_theofilis_2015]
- [Paredes et al 2020][research_paredes_venkatachari_2020]
- [Parikh et al 2004][research_parikhparesh_engelundwalter_2004]
- [Parish and Barone 2025][research_parish_barone_2025]
- [Park 1989][research_parkchul_1989]
- [Park 1992][research_park_1992]
- [Park 1996][research_park_1996]
- [Park 2010][research_park_2010]
- [Park and Park 2016][research_park_park_2016]
- [Park and Park 2022][research_park_park_2022]
- [Park et al 1996][research_park_menees_1996]
- [Park et al 2000][research_park_bogdanoff_2000]
- [Park et al 2000][research_park_mehta_2000]
- [Park et al 2016][research_park_chang_2016]
- [Park et al 2022][research_park_lee_2022]
- [Park et al 2026][research_park_kim_2026]
- [Park et al 2026][research_park_lee_2026]
- [Parker 2022][research_parker_2022]
- [Parker et al 1991][research_parker_spain_1991]
- [Parmar et al 2026][research_parmar_jp_2026]
- [Parsley 1989][research_parsley_1989]
- [Parsons and Richmond 1969][research_parsons_richmond_1969]
- [Pathak et al 2024][research_pathak_khare_2024]
- [Patra and Lee 2018][research_patra_lee_2018]
- [Patrick 2019][research_patrick_2019]
- [Patrick 2021][research_patrick_2021]
- [Patterson 2010][research_patterson_2010]
- [Paudel and McFarland 2025][research_paudel_mcfarland_2025]
- [Paull 1993][research_paull_1993]
- [Paull 1999][research_paull_1999]
- [Paull and Stalker 1998][research_paull_stalker_1998]
- [Paull et al 1988][research_paull_stalker_1988]
- [Paull et al 1995][research_paull_stalker_1995]
- [Paull et al 1995][research_paull_stalker_1995_b]
- [Paull et al 1995][research_paull_stalker_1995_c]
- [Paull et al 1995][research_paulla_stalkerrj_1995]
- [Paull et al 2000][research_paull_frost_2000]
- [Paull et al 2005][research_paull_alesi_2005]
- [Pavlov and Istomin 2023][research_pavlov_istomin_2023]
- [Pavlov et al 2023][research_pavlov_gerasimov_2023]
- [Payne 1968][research_payne_1968]
- [Payne 1980][research_payne_1980]
- [Payne et al 1980][research_payne_hartley_1980]
- [Paynter 1988][research_paynter_1988]
- [Pearson 1967][research_pearsonwe_1967]
- [Peebles 2007][research_peeblescurtis_2007]
- [Peebles 2007][research_peeblescurtis_2007_b]
- [Peebles 2008][research_peebles_2008]
- [Peebles 2009][research_peebles_2009]
- [Pegg et al 1993][research_peggrobertj_huntjamesl_1993]
- [Pei et al 2021][research_pei_fan_2021]
- [Pellett 2005][research_pellettgerald_2005]
- [Pellett et al 2002][research_pellett_bruno_2002]
- [Pellett et al 2008][research_pellett_vaden_2008]
- [Pellett et al 2009][research_pellett_dawson_2009]
- [Pelloux 1994][research_pelloux_1994]
- [Penanhoat and Darracq 1996][research_penanhoat_darracq_1996]
- [Peng 2023][research_peng_2023]
- [Peng and Panesar 2024][research_peng_panesar_2024]
- [Peng and Wang 2026][research_peng_wang_2026]
- [Peng and Zhong 2022][research_peng_zhong_2022]
- [Peng et al 2024][research_peng_xu_2024]
- [Peng et al 2024][research_peng_xu_2024_b]
- [Peng et al 2024][research_peng_zhou_2024]
- [Peng et al 2025][research_peng_yin_2025]
- [Penland and Romeo 1971][research_penland_romeo_1971]
- [Performance and Technological Feasibility 2018][research_performance_and_2018]
- [Perkins 2010][research_perkins_2010]
- [Perkowski et al 2024][research_perkowski_bilar_2024]
- [Perlo 2026][research_perlo_2026]
- [Perrel and Lafon 1992][research_perrel_lafon_1992]
- [Perrier and Rostand 1994][research_perrier_rostand_1994]
- [Perry 2026][research_perry_2026]
- [Persh 1955][research_persh_1955]
- [Peschke 1995][research_peschke_1995]
- [Peterson 2023][research_peterson_2023]
- [Petervari et al 2026][research_petervari_wagner_2026]
- [Petha Sethuraman et al 2020][research_pethasethuraman_kim_2020]
- [Petha Sethuraman et al 2023][research_pethasethuraman_yang_2023]
- [Petley and Dziedzic 1993][research_petley_dziedzic_1993]
- [Petukhov et al 2023][research_petukhov_kolchin_2023]
- [Pezzella and Viviani 2016][research_pezzella_viviani_2016]
- [Pfaff 1968][research_pfaff_1968]
- [Phillips and Cruz 1991][research_phillips_cruz_1991]
- [Phillips and Engelund 1997][research_phillips_engelund_1997]
- [Phillips et al 1968][research_phillips_fiedler_1968]
- [Pichler 2023][research_pichler_2023]
- [Pike 1996][research_pike_1996]
- [Pike 1996][research_pike_1996_b]
- [Piland 1987][research_piland_1987]
- [Piland 1987][research_pilandwilliamm_1987]
- [Pinckney 1978][research_pinckney_1978]
- [Pinckney and Walton 1994][research_pinckney_walton_1994]
- [Pirrello et al 1976][research_pirrellocj_bakerah_1976]
- [Pisano and Whitfield 2024][research_pisano_whitfield_2024]
- [Pisharoti and Brizzolara 2025][research_pisharoti_brizzolara_2025]
- [Pittman 1989][research_pittman_1989]
- [Plank and Penning 1973][research_plankpp_penningfa_1973]
- [Plencner 1991][research_plencnerrobertm_1991]
- [PM titanium technology for 2002][research_pm_titanium_2002]
- [Polev et al 2022][research_polev_grunin_2022]
- [Pollock and Wild 2021][research_pollock_wild_2021]
- [Pollock and Wild 2024][research_pollock_wild_2024]
- [Polyanskii 1967][research_polyanskii_1967]
- [Pope 1968][research_pope_1968]
- [Pordal et al 1990][research_pordalhs_khoslapk_1990]
- [Porter 2022][research_porter_2022]
- [Pototzky et al 1988][research_pototzky_spain_1988]
- [Potter and Whitfield 1957][research_potter_whitfield_1957]
- [Poudel and Shoele 2026][research_poudel_shoele_2026]
- [Pouring 1965][research_pouring_1965]
- [Povinelli 1989][research_povinellilouisa_1989]
- [Povinelli 1990][research_povinellilouisa_1990]
- [Povinelli 1991][research_povinellilouisa_1991]
- [Povinelli 1996][research_povinellilouisa_1996]
- [Povinelli et al 1990][research_povinelli_dwoyer_1990]
- [Powell 1985][research_powell_1985]
- [Powell 1992][research_powell_1992]
- [Powell et al 1991][research_powell_shaughnessy_1991]
- [Powering the Future of 2022][research_powering_the_2022]
- [Prabhu and Tannehill 1984][research_prabhudk_tannehilljc_1984]
- [Prasad 2022][research_prasad_2022]
- [Preller 2018][research_preller_2018]
- [Preller and Smart 2012][research_preller_smart_2012]
- [Presby 2021][research_presby_2021]
- [Preston 1958][research_preston_1958]
- [Problem of Hypersonic Flow 2001][research_problem_of_2001]
- [Probstein 1968][research_probstein_1968]
- [Process for stabilisation of 1992][research_process_for_1992]
- [Pruitt and Bates 1992][research_pruitt_bates_1992]
- [Psiaki and Park 1991][research_psiaki_park_1991]
- [Pu et al 2026][research_pu_xu_2026]
- [Pudsey 2014][research_pudsey_2014]
- [Pukhov 1993][research_pukhov_1993]
- [Pulsonetti et al 1991][research_pulsonetti_erdos_1991]
- [Purifoy and Neal 2017][research_purifoy_neal_2017]
- [Purpura 2021][research_purpura_2021]
- [Purpura et al 2018][research_purpura_trifoni_2018]
- [Purwar and Basu 2017][research_purwar_basu_2017]
- [Qi et al 1998][research_qi_wang_1998]
- [Qi et al 2015][research_qi_bao_2015]
- [Qi et al 2021][research_qi_li_2021]
- [Qi et al 2022][research_qi_cheng_2022]
- [Qiao et al 2022][research_qiao_liu_2022]
- [Qiao et al 2023][research_qiao_liu_2023]
- [Qiao et al 2024][research_qiao_liu_2024]
- [Qin et al 1991][research_qin_scriba_1991]
- [Qin et al 2009][research_qin_bao_2009]
- [Qin et al 2010][research_qin_zhou_2010]
- [Qin et al 2012][research_qin_bao_2012]
- [Qin et al 2015][research_qin_chang_2015]
- [Qin et al 2019][research_qin_agarwal_2019]
- [Qin et al 2026][research_qin_huang_2026]
- [Qin et al 2026][research_qin_yuan_2026]
- [Qin et al 2026][research_qin_zhang_2026]
- [Qiu et al 2021][research_qiu_zhang_2021]
- [Qiu et al 2024][research_qiu_shi_2024]
- [Quan et al 2021][research_quan_xu_2021]
- [Quan et al 2024][research_quan_chang_2024]
- [Quinlan et al 2014][research_quinlanjesser_mcdanieljamesc_2014]
- [Quinn 1978][research_quinn_1978]
- [Quinn and Gong 1990][research_quinnrobertd_gongleslie_1990]
- [Rabadan Santana and Weigand 2021][research_rabadansantana_weigand_2021]
- [Radhi et al 2019][research_radhi_iacobellis_2019]
- [Radiation at Hypersonic Speeds 1962][research_radiation_at_1962]
- [Ragnoli et al 2024][research_ragnoli_savino_2024]
- [Rahimi et al 2026][research_rahimi_svolos_2026]
- [Rahmani and Hejranfar 2021][research_rahmani_hejranfar_2021]
- [Raj 1987][research_raj_1987]
- [Raj et al 2019][research_raj_sandhu_2019]
- [Rajput et al 2026][research_rajput_soni_2026]
- [Ramanah and Mee 2006][research_ramanah_mee_2006]
- [Ramanujachari and Amrutha Preethi 2023][research_ramanujachari_amruthapreethi_2023]
- [Ramunno et al 2022][research_ramunno_boyd_2022]
- [Rana et al 2009][research_rana_thornber_2009]
- [Rana et al 2011][research_rana_thornber_2011]
- [Raney et al 1993][research_raneydavidl_mcminnjohnd_1993]
- [Ransone et al 1992][research_ransonephilipo_yamakiyrobert_1992]
- [Rapial 1969][research_rapial_1969]
- [Rasky 1993][research_rasky_1993]
- [Rasmussen and Stevens 1987][research_rasmussen_stevens_1987]
- [Rataczak et al 2024][research_rataczak_chaudhry_2024]
- [Ratchford et al 2025][research_ratchford_redding_2025]
- [Rathi and Sinha 2024][research_rathi_sinha_2024]
- [Ratnayake 2010][research_ratnayakenalina_2010]
- [Rattray and Mall 1994][research_rattray_mall_1994]
- [Rausch and Morris 1992][research_rauschvincentl_morrischarlesekjr_1992]
- [Rausch et al 1997][research_rausch_mcclinton_1997]
- [Rausch et al 2000][research_rausch_mcclinton_2000]
- [Ravi Teja et al 2022][research_raviteja_bharanichandra_2022]
- [Ravichandran et al 2023][research_ravichandran_doherty_2023]
- [Ravindran et al 2019][research_ravindran_bricalli_2019]
- [Ray et al 1988][research_ray_niggemeier_1988]
- [Rayle and Koch 1954][research_raylewarrend_kochrichardg_1954]
- [Re and Berrier 1982][research_rerj_berrierbl_1982]
- [Reba and Christian 1963][research_reba_christian_1963]
- [Recent Advances in Structures 1978][research_recent_advances_1978]
- [Recina and Karlsson 1999][research_recina_karlsson_1999]
- [Reda 1991][research_reda_1991]
- [Redding et al 2025][research_redding_cavanaugh_2025]
- [Reddy 2019][research_reddy_2019]
- [Reddy and Harloff 1991][research_reddy_harloff_1991]
- [Reddy et al 1989][research_reddy_smith_1989]
- [Redifer et al 2007][research_redifer_lin_2007]
- [Reed 1990][research_reed_1990]
- [Reed 1997][research_reed_1997]
- [Reed et al 2015][research_reed_perez_2015]
- [Reid 2025][research_reid_2025]
- [Reisenthel et al 2010][research_reisenthel_allen_2010]
- [Reisgen et al 2014][research_reisgen_olschok_2014]
- [Relangi et al 2022][research_relangi_ingenito_2022]
- [Ren et al 2017][research_ren_zhang_2017]
- [Ren et al 2019][research_ren_yuan_2019]
- [Ren et al 2022][research_ren_wang_2022]
- [Research on the Combustion Mode and Thrust Performance of Rotating Detonation Scrarmjet Engines 2024][research_research_on_2024]
- [Research Progress in Active 2026][research_research_progress_2026]
- [Resende 1991][research_resendehugob_1991]
- [Resende 1993][research_resendehugob_1993]
- [Reshotko 1987][research_reshotko_1987]
- [Reubush 1999][research_reubush_1999]
- [Reubush et al 1987][research_reubushde_pusterrl_1987]
- [Reubush et al 2004][research_reubush_nguyen_2004]
- [Reusable launch vehicle Technology 1995][research_reusable_launch_1995]
- [Reyhner and Hickcox 1972][research_reyhner_hickcox_1972]
- [Reynier 2016][research_reynier_2016]
- [Rez 2021][research_rez_2021]
- [Rhodes 1964][research_rhodes_1964]
- [Rhudy 1970][research_rhudy_1970]
- [Ricciardi 1991][research_ricciardi_1991]
- [Rice 2002][research_rice_2002]
- [Rich et al 2007][research_rich_lempert_2007]
- [Richard and Christophe 1995][research_richard_christophe_1995]
- [Richards 1978][research_richards_1978]
- [Richards and Stollery 1979][research_richards_stollery_1979]
- [Richards et al 1971][research_richards_culotta_1971]
- [Richardson 1989][research_richardson_1989]
- [Richardson et al 1989][research_richardsonpamelaf_mcclintoncharlesr_1989]
- [Ricketts et al 1993][research_rickettsrodneyh_nollthomase_1993]
- [Rickman 2010][research_rickman_2010]
- [Ridgway et al 2018][research_ridgway_sam_2018]
- [Rieken et al 2020][research_elizabethfrieken_scottaberry_2020]
- [Riggins 1997][research_riggins_1997]
- [Riggins 1998][research_rigginsdavid_1998]
- [Riggins 2002][research_riggins_2002]
- [Riggins et al 1992][research_riggins_mcclinton_1992]
- [Riggins et al 1997][research_riggins_mcclinton_1997]
- [Riggins et al 2006][research_rigginsdavid_tacketregan_2006]
- [Riley and DeJarnette 1992][research_riley_dejarnette_1992]
- [Riley and McNamara 2017][research_riley_mcnamara_2017]
- [Riley et al 2018][research_riley_gaitonde_2018]
- [Riva et al 1997][research_riva_daminelli_1997]
- [Rivers 1999][research_rivershkevin_1999]
- [Rivers and Glass 2006][research_rivers_glass_2006]
- [Rizkalla et al 1989][research_rizkalla_bakos_1989]
- [Rizkalla et al 1990][research_rizkalla_chinitz_1990]
- [Rizvi et al 2017][research_rizvi_linshu_2017]
- [Rizzi et al 2026][research_rizzi_parish_2026]
- [Robinson 2024][research_robinson_2024]
- [Robinson and Martin 2006][research_robinson_martin_2006]
- [Robinson et al 1980][research_robinsonjc_smithdm_1980]
- [Robinson et al 2004][research_robinson_mee_2004]
- [Roche and Kosareo 2001][research_rochejosephm_kosareodanieln_2001]
- [Roche et al 2026][research_roche_breil_2026]
- [Rockwell et al 2010][research_rockwell_goyne_2010]
- [Rockwell et al 2011][research_rockwell_goyne_2011]
- [Roder 1977][research_roder_1977]
- [Rodgers 1992][research_rodgers_1992]
- [Rodi 2012][research_rodi_2012]
- [Rodi et al 1996][research_rodi_emami_1996]
- [Rodkiewicz and Chattopadhyay 1971][research_rodkiewicz_chattopadhyay_1971]
- [Rodrigues 2026][research_rodrigues_2026]
- [Rodriguez et al][research_josemrodriguez_brettfbathel]
- [Rodriguez et al 2009][research_rodriguez_dickeson_2009]
- [Rodríguez Fuentes and Parent 2022][research_rodriguezfuentes_parent_2022]
- [Rodríguez Fuentes and Parent 2023][research_rodriguezfuentes_parent_2023]
- [Rodríguez-Mirasol et al 1995][research_rodriguezmirasol_thrower_1995]
- [Rodríguez-Segade et al 2024][research_rodriguezsegade_hernandez_2024]
- [Roga 2019][research_roga_2019]
- [Roga 2019][research_roga_2019_b]
- [Rogers 1979][research_rogersrc_1979]
- [Rogers and Weidner 1991][research_rogers_weidner_1991]
- [Rogers et al 1994][research_rogers_weidner_1994]
- [Rogers et al 1998][research_rogersrclayton_capriottidiegop_1998]
- [Rogers et al 2001][research_rogers_shih_2001]
- [Rogers et al 2005][research_rogers_shih_2005]
- [Rokaw and Getchell 1996][research_rokaw_getchell_1996]
- [Rom and Avital 1992][research_rom_avital_1992]
- [Ronald 1989][research_ronald_1989]
- [Ronald 1989][research_ronald_1989_b]
- [Ronald 1991][research_ronald_1991]
- [Ronald 1993][research_ronald_1993]
- [Ronald 1995][research_ronald_1995]
- [Rong 2017][research_rong_2017]
- [Rong et al 2023][research_rong_cheng_2023]
- [Roos et al 2020][research_roos_pudsey_2020]
- [Rose and Sridhar 2022][research_rose_sridhar_2022]
- [Rose and Stankevics 1963][research_rose_stankevics_1963]
- [Rosner and Cibrian 1974][research_rosner_cibrian_1974]
- [Rothmund et al 1996][research_rothmund_scherrer_1996]
- [Roudakov et al 1996][research_roudakov_semenov_1996]
- [Roudakov et al 1998][research_roudakovalexanders_semenovvyacheslavl_1998]
- [Rouhi Youssefi and Knight 2017][research_rouhiyoussefi_knight_2017]
- [Roundy 1979][research_roundy_1979]
- [Roux 2011][research_roux_2011]
- [Roux and Tiruveedula 2016][research_roux_tiruveedula_2016]
- [Roux and Tiruveedula 2017][research_roux_tiruveedula_2017]
- [Roux et al 2013][research_roux_shakya_2013]
- [Roux et al 2013][research_roux_shakya_2013_b]
- [Roux et al 2014][research_roux_choi_2014]
- [Rouzbar and Eyi 2015][research_rouzbar_eyi_2015]
- [Rowan 2024][research_rowan_2024]
- [Rozario and Zouaoui 2007][research_rozario_zouaoui_2007]
- [Ru-ren Chow 1963][research_rurenchow_1963]
- [Ruan et al 2020][research_ruan_domingo_2020]
- [Ruban et al 2018][research_ruban_menezes_2018]
- [Ruban et al 2020][research_ruban_menezes_2020]
- [Rubins and Bauer 1994][research_rubins_bauer_1994]
- [Rubio et al 2018][research_rubio_ramanujam_2018]
- [Rudiments and Methodology for 2001][research_rudiments_and_2001]
- [Ruf et al 1999][research_rufjoseph_holtjamesb_1999]
- [Ruf et al 2001][research_rufjosephh_holtjamesb_2001]
- [Rufer et al 2009][research_rufershannj_nowakrobertj_2009]
- [Ruffin et al 1989][research_ruffin_venkatapathy_1989]
- [Ruffin et al 1989][research_ruffin_venkatapathy_1989_b]
- [Ruggles-Wrenn and Schmidt 2024][research_ruggleswrenn_schmidt_2024]
- [Runstadler and Peter W. 1969][research_runstadler_peterw_1969]
- [Ruscigno 1965][research_ruscignoh_1965]
- [Russian Aerospace Literature This month: Hypersonic Aerodynamics 1996][research_russian_aerospace_1996]
- [Russin 1974][research_russin_1974]
- [Russin 1975][research_russinwr_1975]
- [Ryken and Davis 2004][research_ryken_davis_2004]
- [S. Hameed and G. R 2021][research_shameed_gr_2021]
- [Sabelkin et al 2017][research_sabelkin_zawada_2017]
- [Sabinash et al 1995][research_sabinash_sastry_1995]
- [Saboktakin and Monjezi 2024][research_saboktakin_monjezi_2024]
- [Sabre Space Engine Gets £26.5M Boost 2018][research_sabre_space_2018]
- [Saccone et al 2016][research_saccone_gardi_2016]
- [Sadunas 1976][research_sadunas_1976]
- [Saenz et al 2025][research_saenz_frankel_2025]
- [Saghafian et al 2015][research_saghafian_shunn_2015]
- [Saha 2022][research_saha_2022]
- [Sahbon et al 2023][research_sahbon_jacewicz_2023]
- [Sahoo et al 2007][research_sahoo_mahapatra_2007]
- [Sahu et al 2022][research_sahu_tropina_2022]
- [Sai Prakash et al 2026][research_saiprakash_raghav_2026]
- [Sakata 1992][research_sakata_1992]
- [Samimy et al 2011][research_samimy_webb_2011]
- [Sams 1989][research_sams_1989]
- [Samuels et al][research_killiansamuels_talschwartz]
- [Sanaka et al 2023][research_sanaka_kandula_2023]
- [Sancho Ponce 2016][research_sanchoponce_2016]
- [Sandborn and Heron 1963][research_sandborn_heron_1963]
- [Sandhu 2005][research_sandhu_2005]
- [Sanghi and Sane 1999][research_sanghi_sane_1999]
- [Sangiovanni et al 1993][research_sangiovanni_barber_1993]
- [Sanjay and Kuzhiveli 2025][research_sanjay_kuzhiveli_2025]
- [Sankar and Kelkar 1995][research_sankar_kelkar_1995]
- [Sano 1981][research_sano_1981]
- [Santos 2005][research_santos_2005]
- [Santos 2007][research_santos_2007]
- [Santos and Lewis 2003][research_santos_lewis_2003]
- [Sappey et al 2009][research_sappey_sutherland_2009]
- [Saravanan et al 2008][research_saravanan_jagadeesh_2008]
- [Sarosh 2021][research_sarosh_2021]
- [Sasmal et al 1991][research_sasmal_hochstein_1991]
- [Sastry 1963][research_sastry_1963]
- [Sato and Kaji 1992][research_sato_kaji_1992]
- [Sato and Kaji 1993][research_sato_kaji_1993]
- [Sato and Raman 2020][research_sato_raman_2020]
- [Sato et al 1997][research_sato_izumikawa_1997]
- [Satyanarayan et al 2026][research_satyanarayan_raj_2026]
- [Sauerwein et al 2015][research_sauerwein_hruschka_2015]
- [Saunders et al 2007][research_saunders_slater_2007]
- [Saunders et al 2012][research_saundersjd_stuebertj_2012]
- [Savel'ev and Stepanov 1988][research_savelev_stepanov_1988]
- [Sawatzky 2018][research_sawatzky_2018]
- [Scaggs 1966][research_scaggs_1966]
- [Scaggs et al 1963][research_scaggs_burggraf_1963]
- [Scala 1958][research_scala_1958]
- [Scanning and Transmission Electron 1994][research_scanning_and_1994]
- [Schalla 1967][research_schalla_1967]
- [Schetz et al 1969][research_schetz_gilreath_1969]
- [Schetz et al 1982][research_schetz_billig_1982]
- [Schetz et al 1991][research_schetz_billig_1991]
- [Schierman et al 2001][research_schierman_ward_2001]
- [Schindel 1999][research_schindel_1999]
- [Schirmer and Capone 1989][research_schirmeralbertow_caponefrancisj_1989]
- [Schmalhofer et al 2017][research_schmalhofer_griebel_2017]
- [Schmidt and Patankar 1991][research_schmidt_patankar_1991]
- [Schmidt and Schmidt 1997][research_schmidt_schmidt_1997]
- [Schmidt and Velapoldi 1996][research_schmidt_velapoldi_1996]
- [Schneider 1970][research_schneider_1970]
- [Schneider and Reed 2003][research_schneider_reed_2003]
- [Schoettle and Hillesheimer 1991][research_schoettle_hillesheimer_1991]
- [Schoettle and Rahn 1993][research_schoettle_rahn_1993]
- [Schouler et al 2023][research_schouler_prevereaud_2023]
- [Schram and Narayanaswamy 2026][research_schram_narayanaswamy_2026]
- [Schreck et al 1998][research_schreck_faller_1998]
- [Schrötter et al 2026][research_schrotter_kavas_2026]
- [Schubert 1978][research_schubert_1978]
- [Schuelein et al 2017][research_schuelein_schenk_2017]
- [Schulte-Roedding and Olivier 1998][research_schulteroedding_olivier_1998]
- [Schultz et al 2012][research_schultz_goldenstein_2012]
- [Schunk and Chung 2000][research_schunk_chung_2000]
- [Schweikart and Hallion 1998][research_schwelkart_hallion_1997]
- [Schwendemann and Sanders 1982][research_schwendemannmf_sandersbw_1982]
- [Scott 1993][research_scott_1993]
- [Scott and Pototzky 1993][research_scott_pototzky_1993]
- [Scotti 1992][research_scottistephenj_1992]
- [Scramjet 2015][research_scramjet_2015]
- [Scramjet Combustion 2022][research_scramjet_combustion_2022]
- [Scramjet Combustor 2022][research_scramjet_combustor_2022]
- [Scramjet Developments in France 2001][research_scramjet_developments_2001]
- [Scramjet Engine Research athe 2001][research_scramjet_engine_2001]
- [Scramjet Flowpath Integration 2001][research_scramjet_flowpath_2001]
- [Scramjet Inlet/Forebody and Isolator 2022][research_scramjet_inlet_forebody_2022]
- [Scramjet Inlets 2001][research_scramjet_inlets_2001]
- [Scramjet Investigations Within the 2001][research_scramjet_investigations_2001]
- [Scramjet Nozzle/Aftbody 2022][research_scramjet_nozzle_aftbody_2022]
- [Scramjet Performance 2001][research_scramjet_performance_2001]
- [Scramjet Research and Development 2001][research_scramjet_research_2001]
- [Scramjet Testing in the 2001][research_scramjet_testing_2001]
- [Scramjets and Combined Cycle 2022][research_scramjets_and_2022]
- [Scribben and Withrow 2006][research_scribben_withrow_2006]
- [Seebass 1989][research_seebass_1989]
- [Seebaugh 1973][research_seebaugh_1973]
- [Seebaugh et al 1971][research_seebaughwr_doranrw_1971]
- [Seetharaman and Semiatin 1996][research_seetharaman_semiatin_1996]
- [Segal et al 1991][research_segalcorin_mcdanieljamesc_1991]
- [Sekar et al 1990][research_sekar_thomas_1990]
- [Selcan et al 2021][research_selcan_sander_2021]
- [Seleznev 2019][research_seleznev_2019]
- [Seleznev 2021][research_seleznev_2021]
- [Seleznev 2022][research_seleznev_2022]
- [Self-starting Simulation of a Hypersonic Inlet with Variable Free Stream Condition 2020][research_self_starting_simulation_2020]
- [Sellers 1965][research_sellers_1965]
- [Sen et al 2018][research_sen_pesyridis_2018]
- [Serre 2011][research_serre_2011]
- [Sforza 2017][research_sforza_2017]
- [Sforza 2026][research_sforza_2026]
- [Sha et al 2026][research_sha_long_2026]
- [Shadow 1987][research_shadow_1987]
- [Shajahan et al 2025][research_shajahan_gugulothu_2025]
- [Shan et al 2017][research_shan_hou_2017]
- [Shan et al 2021][research_shan_zhang_2021]
- [Shang 2008][research_shang_2008]
- [Shang and Chang 2007][research_shang_chang_2007]
- [Shanmugam et al 2025][research_shanmugam_silvi_2025]
- [Shao et al 2015][research_shao_wang_2015]
- [Shaohua and Xu 2017][research_shaohua_xu_2017]
- [Sharenson 1966][research_sharenson_1966]
- [Sharma 1987][research_sharma_1987]
- [Sharma 1992][research_sharma_1992]
- [Sharma and Saluti 2025][research_sharma_saluti_2025]
- [Sharma et al 2020][research_sharma_eswaran_2020]
- [Sharma et al 2022][research_sharma_eswaran_2022]
- [Sharpe and Jackson 1975][research_sharpeel_jacksonlr_1975]
- [Shaughnessy and Gregory 1991][research_shaughnessyjohnd_gregoryirenem_1991]
- [Sheehan 1989][research_sheehan_1989]
- [Sheetz 1965][research_sheetznwjr_1965]
- [Sheikin and Kuranov 2004][research_sheikin_kuranov_2004]
- [Sheikin and Kuranov 2005][research_sheikin_kuranov_2005]
- [Shekhtman et al 2021][research_shekhtman_yu_2021]
- [Shen et al 2019][research_shen_zhang_2019]
- [Shen et al 2020][research_shen_huang_2020]
- [Shen et al 2021][research_shen_huang_2021]
- [Shen et al 2022][research_shen_ma_2022]
- [Shen et al 2025][research_shen_yao_2025]
- [Sheng et al 2023][research_sheng_gan_2023]
- [Shenoy et al 2019][research_shenoy_drozda_2019]
- [Shi 2016][research_shi_2016]
- [Shi 2022][research_shi_2022]
- [Shi et al 2016][research_shi_he_2016]
- [Shi et al 2016][research_shi_liu_2016]
- [Shi et al 2020][research_shi_zhu_2020]
- [Shi et al 2023][research_shi_fan_2023]
- [Shieh et al 2024][research_shieh_lin_2024]
- [Shilnikov and Elizarova 2018][research_shilnikov_elizarova_2018]
- [Shimada and Ohwada 2020][research_shimada_ohwada_2020]
- [Shimada et al 1999][research_shimada_yamamoto_1999]
- [Shimojima et al 2017][research_shimojima_hosokawa_2017]
- [Shin and Sung 2018][research_shin_sung_2018]
- [Shirasu et al 1996][research_shirasu_south_1996]
- [Shirasu et al 1996][research_shirasu_south_1996_b]
- [Shore 1986][research_shorecharlesp_1986]
- [Shorenstein 1971][research_shorenstein_1971]
- [Shou et al 2023][research_shou_yan_2023]
- [Shukla and Verma 2020][research_shukla_verma_2020]
- [Shulman et al 1966][research_shulman_parry_1966]
- [Shumskii and Yaroslavtsev 2012][research_shumskii_yaroslavtsev_2012]
- [Shvets et al 2005][research_shvets_voronin_2005]
- [Si et al 2019][research_si_huang_2019]
- [Siddiqui et al 2023][research_siddiqui_ledbetter_2023]
- [Siebenhaar and Bulman 1998][research_siebenhaar_bulman_1998]
- [Siebenhaar et al 1999][research_siebenhaar_bulman_1999]
- [Sihvola 2018][research_sihvola_2018]
- [Silva and Brójo 2026][research_silva_brojo_2026]
- [Silvestrov and Surzhikov 2020][research_silvestrov_surzhikov_2020]
- [Simeonides 2006][research_simeonides_2006]
- [Simeonides et al 1994][research_simeonides_haase_1994]
- [Simoneau et al 1988][research_simoneau_hendricks_1988]
- [Simpson 2026][research_simpson_2026]
- [Sims and Hahn 1964][research_sims_hahn_1964]
- [Sindt 1969][research_sindt_1969]
- [Sindt 1970][research_sindt_1970]
- [Sindt 1972][research_sindt_1972]
- [Sindt 1972][research_sindt_1972_b]
- [Sindt 1972][research_sindt_1972_c]
- [Sindt 1995][research_sindt_1995]
- [Sindt and Ludtke 1973][research_sindt_ludtke_1973]
- [Sindt and Ludtke 1995][research_sindt_ludtke_1995]
- [Singh and Mukhopadhyay 2025][research_singh_mukhopadhyay_2025]
- [Singh et al 1990][research_singh_tiwari_1990]
- [Singh et al 1992][research_singh_shen_1992]
- [Singh et al 2023][research_singh_prakash_2023]
- [Single stage to orbit 1994][research_single_stage_1994]
- [Sivan and Pandian 2018][research_sivan_pandian_2018]
- [Sivasubramanian et al 2026][research_sivasubramanian_v_2026]
- [Skamniotis and Cocks 2021][research_skamniotis_cocks_2021]
- [Skinner and Chattopadhyay 2021][research_skinner_chattopadhyay_2021]
- [Skinner and Stalker 1995][research_skinner_stalker_1995]
- [Slater 2016][research_slaterjohnw_2016]
- [Slater and Saunders 2009][research_slater_saunders_2009]
- [Slater et al 2005][research_slaterjohnw_davisdavido_2005]
- [Slush hydrogen production, storage 1966][research_slush_hydrogen_1966]
- [Slush Hydrogen Storage 2014][research_slush_hydrogen_2014]
- [Slutsky et al 1965][research_slutsky_tamagno_1965]
- [Small et al 1974][research_smallwj_weidnerjp_1974]
- [Small et al 1976][research_smallwj_weidnerjp_1976]
- [Smarslok 2015][research_smarslok_2015]
- [Smart 1999][research_smart_1999]
- [Smart 2024][research_smart_2024]
- [Smart and Ruf 2006][research_smartmichaelk_rufedwardg_2006]
- [Smart and Suraweera 2009][research_smart_suraweera_2009]
- [Smart and Tetlow 2006][research_smart_tetlow_2006]
- [Smart and Trexler 2003][research_smartmichaelk_trexlercarla_2003]
- [Smart et al 2006][research_smart_hass_2006]
- [Smayda 2017][research_smayda_2017]
- [Smirnov et al 2023][research_smirnov_nikitin_2023]
- [Smith 1978][research_smithlm_1978]
- [Smith 1979][research_smith_1979]
- [Smith 1989][research_smith_1989]
- [Smith 2021][research_smith_2021]
- [Smith et al 2002][research_smith_schetz_2002]
- [Smith et al 2002][research_smith_walker_2002]
- [Smithey and Fuhs 1977][research_smithey_fuhs_1977]
- [Smits 2007][research_smits_2007]
- [Smits 2009][research_smits_2009]
- [Son et al 2024][research_son_ko_2024]
- [Song and Choi 2020][research_song_choi_2020]
- [Song and Su 2015][research_song_su_2015]
- [Song et al 2020][research_song_zhao_2020]
- [Song et al 2022][research_song_luo_2022]
- [Song et al 2026][research_song_xu_2026]
- [Soni and De 2017][research_soni_de_2017]
- [Sorensen and Bencze 1973][research_sorensenne_benczedp_1973]
- [Sorensen and Latham 1975][research_sorensen_latham_1975]
- [Sorensen and Smeltzer 1972][research_sorensen_smeltzer_1972]
- [Sorensen et al 1973][research_sorensen_smeltzer_1973]
- [Soumyajit Saha and Debasis Chakraborty 2023][research_soumyajitsaha_debasischakraborty_2023]
- [Spaid et al 1995][research_spaid_keener_1995]
- [Spain et al 1993][research_spain_zeiler_1993]
- [Spain et al 1993][research_spain_zeiler_1993_b]
- [Spanos 2009][research_spanostheodorosa_2009]
- [Species measurements in a 1996][research_species_measurements_1996]
- [Spencer 1962][research_spencer_1962]
- [Sponable 1995][research_sponable_1995]
- [Spravka and Jorris 2015][research_spravka_jorris_2015]
- [Sprinkle and Davis 1999][research_sprinkle_davis_1999]
- [Sprunger et al 2025][research_sprunger_lasorsa_2025]
- [Sreekanth and Reddy 1995][research_sreekanth_reddy_1995]
- [Sreekireddy et al 2019][research_sreekireddy_reddy_2019]
- [Srinivasan and Erickson 1995][research_srinivasan_erickson_1995]
- [Srinivasan et al 2020][research_srinivasan_mahapatra_2020]
- [Sriram et al 2015][research_sriram_ram_2015]
- [Stainback 1969][research_stainbackpc_1969]
- [Stalder 1957][research_stalder_1957]
- [Stalker 1996][research_stalkerrj_1996]
- [Stalker and Morgan 1984][research_stalker_morgan_1984]
- [Stalker and Morgan 1987][research_stalker_morgan_1987]
- [Stalker et al 1988][research_stalker_morgan_1988]
- [Stalker et al 1993][research_stalkerrj_hollisp_1993]
- [Stalker et al 1994][research_stalker_simmons_1994]
- [Stalker et al 1995][research_stalker_simmons_1995]
- [Stalker et al 1995][research_stalkerrj_bakosrj_1995]
- [Stalker et al 1996][research_stalker_morgan_1996]
- [Stallings and Burt 1984][research_stallings_burt_1984]
- [Stallings et al 2003][research_stallings_williams_2003]
- [Stanley and Alexander 1999][research_stanleythomastroy_alexanderreginald_1999]
- [Stanley et al 1991][research_stanley_wilhite_1991]
- [Stanley et al 1992][research_stanley_wilhite_1992]
- [Stanley et al 1994][research_stanley_engelund_1994]
- [Stanley et al 2000][research_stanleythomastroy_alexanderreginald_2000]
- [Stanley et al 2013][research_stanley_lopp_2013]
- [Stapp 1995][research_stapp_1995]
- [Star et al 2005][research_star_edwards_2005]
- [Star et al 2006][research_star_edwards_2006]
- [Starkey et al 2006][research_starkey_rankins_2006]
- [Stauffer and Takahashi 2023][research_stauffer_takahashi_2023]
- [Stechmann et al 2019][research_stechmann_heister_2019]
- [Stefaniya et al 2025][research_stefaniya_pushpalatha_2025]
- [Steffen and Yungster 2001][research_steffenchristopherjjr_yungstershaye_2001]
- [Steffen et al 2002][research_steffen_bond_2002]
- [Steinetz 1991][research_steinetz_1991]
- [Steinetz 2008][research_steinetzbrucem_2008]
- [Steinetz et al 1991][research_steinetzbrucem_melismatthewe_1991]
- [Stennett 2020][research_stennett_2020]
- [Stennett et al 2019][research_stennett_gildfind_2019]
- [Stephan and Obermeier 1974][research_stephan_obermeier_1974]
- [Stephan and Schneider 1991][research_stephan_schneider_1991]
- [Stephens 1974][research_stephensjr_1974]
- [Stetson 1986][research_stetson_1986]
- [Stetson 1990][research_stetson_1990]
- [Stewar et al 2003][research_stewar_morgan_2003]
- [Stewart 1973][research_stewart_1973]
- [Stewart 2017][research_stewart_2017]
- [Stewart 2024][research_stewart_2024]
- [Stewart and Leiser 2007][research_stewartdavid_leiserdaniel_2007]
- [Stewart et al 2000][research_stewart_morgan_2000]
- [Stewart et al 2002][research_stewartmem_suresha_2002]
- [Stewart et al 2010][research_stewartdavida_leiserdanielb_2010]
- [Stickler and Keller 1998][research_stickler_keller_1998]
- [Stilla 1994][research_stilla_1994]
- [Stolzenburg 1965][research_stolzenburg_1965]
- [Stone 1975][research_stoneje_1975]
- [Storch et al 2011][research_storch_bynum_2011]
- [Strangman and Keiser 1988][research_strangman_keiser_1988]
- [Streby et al 1999][research_streby_mathur_1999]
- [Street 2024][research_street_2024]
- [Streiff 1953][research_streiff_1953]
- [Strokin and Khailov 1974][research_strokin_khailov_1974]
- [Stroud and Miller 1966][research_stroud_miller_1966]
- [Structure and high temperature deformation behaviour of titanium-rich titanium aluminide 1992][research_structure_and_1992]
- [Structure and properties of 1997][research_structure_and_1997]
- [Strutjet Rocket-Based Combined-Cycle Engine 2001][research_strutjet_rocket_based_2001]
- [Stull 1989][research_stull_1989]
- [Su 2017][research_su_2017]
- [Su and Liu 2025][research_su_liu_2025]
- [Su and Wang 2015][research_su_wang_2015]
- [Su et al 2018][research_su_chen_2018]
- [Su et al 2019][research_su_wang_2019]
- [Su et al 2023][research_su_wu_2023]
- [Su et al 2024][research_su_zhao_2024]
- [Subrahmanyam and Annapurna 1986][research_subrahmanyam_annapurna_1986]
- [Subramanian and Dwarakanath 1969][research_subramanian_dwarakanath_1969]
- [Subramanian and Meadows 2020][research_subramanian_meadows_2020]
- [Sudalagunta et al 2018][research_sudalagunta_sultan_2018]
- [Sudhiesh Kumar and Reddy 2015][research_sudhieshkumar_reddy_2015]
- [Sugavanam and Sastry 1975][research_sugavanam_sastry_1975]
- [Sullins and Waltrup 1985][research_sullins_waltrup_1985]
- [Sullivan 1991][research_williamsullivan_1991]
- [Sun 2018][research_sun_2018]
- [Sun and Zhu 2019][research_sun_zhu_2019]
- [Sun et al 2018][research_sun_zhou_2018]
- [Sun et al 2019][research_sun_guo_2019]
- [Sun et al 2019][research_sun_li_2019]
- [Sun et al 2020][research_sun_yang_2020]
- [Sun et al 2020][research_sun_yang_2020_b]
- [Sun et al 2021][research_sun_li_2021]
- [Sun et al 2023][research_sun_wu_2023]
- [Sun et al 2024][research_sun_jing_2024]
- [Sun et al 2025][research_sun_xue_2025]
- [Sun et al 2025][research_sun_yu_2025]
- [Sun et al 2026][research_sun_ding_2026]
- [Sun et al 2026][research_sun_yu_2026]
- [Sun Jian and Liu Wei-Qiang 2013][research_sunjian_liuweiqiang_2013]
- [Sunami et al 2006][research_sunami_itoh_2006]
- [Suneetha et al 2019][research_suneetha_randive_2019]
- [Suneetha et al 2021][research_suneetha_randive_2021]
- [Sung et al 2024][research_sung_jeong_2024]
- [Sung et al 2026][research_sung_kim_2026]
- [Superconducting liquid-level sensor for slush hydrogen use 1967][research_superconducting_liquid_level_1967]
- [Supersonic and Hypersonic Flight Dynamics Realization for the Spaceliner Real-Time Human-In-the-Loop Space Flight Simulator 2019][research_supersonic_and_2019]
- [Supersonic Combustion Processes 2009][research_supersonic_combustion_2009]
- [Supersonic Flow Combustors 2001][research_supersonic_flow_2001]
- [Suraweera 2024][research_suraweera_2024]
- [Suraweera and Smart 2008][research_suraweera_smart_2008]
- [Surber and Sedlock 1979][research_surber_sedlock_1979]
- [Suresh and Liou 1992][research_suresh_liou_1992]
- [Surface Roughness Effects on 1973][research_surface_roughness_1973]
- [Survey of Shock Tube 1962][research_survey_of_1962]
- [Suryanarayanan et al 2019][research_suryanarayanan_goldstein_2019]
- [Surzhikov 2018][research_surzhikov_2018]
- [Surzhikov 2019][research_surzhikov_2019]
- [Surzhikov 2021][research_surzhikov_2021]
- [Surzhikov 2021][research_surzhikov_2021_b]
- [Surzhikov 2022][research_surzhikov_2022]
- [Swain et al 2020][research_swain_p_2020]
- [Swanson et al 2014][research_swansongreg_kazembacole_2014]
- [Swanson et al 2014][research_swansongregorytodd_cassellalanm_2014]
- [Swanson et al 2015][research_swansongt_kazembacd_2015]
- [Swartzbaugh 1997][research_swartzbaugh_1997]
- [Swiss Students Achieve Europe’s First Reusable Rocket Hopper 2025][research_swiss_students_2025]
- [Swithebank and Chigier 1969][research_swithebank_chigier_1969]
- [Swithenbank 1967][research_swithenbank_1967]
- [Swithenbank and Jaques 1970][research_swithenbank_jaques_1970]
- [Synthesis of titanium aluminide-titanium 1994][research_synthesis_of_1994]
- [Sypniewski 1989][research_sypniewski_1989]
- [Tabakoff and McDONEL 1966][research_tabakoff_mcdonel_1966]
- [Tahir 2021][research_tahir_2021]
- [Takahashi et al 1997][research_takahashi_mizobata_1997]
- [Takahashi et al 1998][research_takahashi_wakai_1998]
- [Takahashi et al 1999][research_takahashi_ueda_1999]
- [Takahashi et al 2018][research_takahashi_munakata_2018]
- [Takahashi et al 2021][research_takahashi_tomioka_2021]
- [Takashima and Kothari 1998][research_takashiman_kothariap_1998]
- [Tam and Hagenmaier 1999][research_tam_hagenmaier_1999]
- [Tamagno et al 1990][research_tamagno_bakos_1990]
- [Tanabe et al 1987][research_tanabe_yasuda_1987]
- [Tanatsugu and Carrick 2003][research_tanatsugu_carrick_2003]
- [Tang et al 2015][research_tang_gao_2015]
- [Tang et al 2019][research_tang_wang_2019]
- [Tang et al 2021][research_tang_wang_2021]
- [Tang et al 2022][research_tang_wang_2022]
- [Tang et al 2023][research_tang_xiong_2023]
- [Tang et al 2024][research_tang_wang_2024]
- [Tang et al 2024][research_tang_xu_2024]
- [Tang et al 2025][research_tang_li_2025]
- [Tang et al 2026][research_tang_fan_2026]
- [Tank 1991][research_tank_1991]
- [Tanno and Tanno 2021][research_tanno_tanno_2021]
- [Tanno et al 2001][research_tanno_komuro_2001]
- [Tariq et al 2026][research_tariq_wasim_2026]
- [Tarpley and Lewis 1995][research_tarpley_lewis_1995]
- [Tatman 2017][research_tatman_2017]
- [Taylor 1968][research_taylor_1968]
- [Taylor and Jackson 1980][research_taylor_jackson_1980]
- [Tedder 2010][research_teddersarahaugustaumberger_2010]
- [Telectro-Mek Inc Fort Wayne In 1965][research_telectromekincfortwaynein_1965]
- [Teng and Yuan 2015][research_teng_yuan_2015]
- [Tenney et al 1988][research_drtenney_wblisagor_1988]
- [Tenney et al 1989][research_darrelrtenney_wbarrylisagor_1989]
- [Test Method for Calculation 2008][research_test_method_2008]
- [Tetervin 1961][research_tetervin_1961]
- [Tewfik and Giedt 1960][research_tewfik_giedt_1960]
- [Tharakan and Sukesh 2025][research_tharakan_sukesh_2025]
- [Thawait et al 2023][research_thawait_tandaiya_2023]
- [Thawait et al 2023][research_thawait_tandaiya_2023_b]
- [The Free Flight Range 1962][research_the_free_1962]
- [The Quest For Hypersonic 2011][research_the_quest_2011]
- [Thelander 1966][research_thelander_1966]
- [Thiele et al 2018][research_thiele_gampe_2018]
- [Thomas 2011][research_thomas_2011]
- [Thomas and Guy 1982][research_thomas_guy_1982]
- [Thomas and Guy 1983][research_thomas_guy_1983]
- [Thomas and Guy 1990][research_thomasscottr_guyrwayne_1990]
- [Thomas and Perlbachs 1967][research_thomas_perlbachs_1967]
- [Thomas and Powell 1992][research_thomas_powell_1992]
- [Thomas et al 1987][research_thomas_voland_1987]
- [Thomas et al 1988][research_thomasjl_rudydh_1988]
- [Thomas et al 1997][research_thomasscottr_perkinshdouglas_1997]
- [Thomas et al 2001][research_thomas_palac_2001]
- [Thomas et al 2009][research_thomas_walker_2009]
- [Thomas et al 2010][research_thomas_lee_2010]
- [Thompson and Friedman 1991][research_thompson_friedman_1991]
- [Thompson and Hoffman 1992][research_thompsonhdoyle_hoffmanjoed_1992]
- [Thompson and Hull 1970][research_thompson_hull_1970]
- [Thompson and Pandolfini 1995][research_thompson_pandolfini_1995]
- [Thompson et al 1996][research_thompson_chu_1996]
- [Thornton et al][research_jmthornton_jbemeurisse]
- [Thornton et al 1990][research_thornton_oden_1990]
- [Throckmorton 1989][research_throckmorton_1989]
- [Throttle-Dependent Forces 1985][research_throttle_dependent_forces_1985]
- [Thrust and Drag Modeling 2021][research_thrust_and_2021]
- [Thrust-Drag Accounting Methodology 1985][research_thrust_drag_accounting_1985]
- [Tian and Liu 2026][research_tian_liu_2026]
- [Tian and Shen 2022][research_tian_shen_2022]
- [Tian et al 2016][research_tian_yang_2016]
- [Tian et al 2018][research_tian_zeng_2018]
- [Tian et al 2022][research_tian_liu_2022]
- [Tian et al 2023][research_tian_yang_2023]
- [Tian et al 2024][research_tian_yang_2024]
- [Tian et al 2025][research_tian_bai_2025]
- [Timofeev et al 2001][research_timofeev_voinovich_2001]
- [Tirskii 1993][research_tirskii_1993]
- [Tirsky 1993][research_tirsky_1993]
- [Tirtey and Boyce 2009][research_tirtey_boyce_2009]
- [Titanium Aluminide Intermetallics 2012][research_titanium_aluminide_2012]
- [Titanium aluminide made by sintering powder prepared by self propagating high temperature synthesis (SPHTS) 1992][research_titanium_aluminide_1992]
- [Tobias and Agrawal 2023][research_tobias_agrawal_2023]
- [TokarcikPolsky et al 1995][research_tokarcikpolskys_papadopoulosp_1995]
- [Tokuda and Yang 2019][research_tokuda_yang_2019]
- [Tolstykh 1969][research_tolstykh_1969]
- [Tomioka et al 2007][research_tomioka_hiraiwa_2007]
- [Tomioka et al 2007][research_tomioka_ueda_2007]
- [Tomioka et al 2009][research_tomioka_hiraiwa_2009]
- [Tomioka et al 2021][research_tomioka_takegoshi_2021]
- [Tong and Giedt 1963][research_tong_giedt_1963]
- [Tong et al 2023][research_tong_duan_2023]
- [Tong et al 2025][research_tong_li_2025]
- [Toniato 2019][research_toniato_2019]
- [Toniato et al 2018][research_toniato_gildfind_2018]
- [Torre et al 2023][research_torre_merli_2023]
- [Torres 1992][research_torresabelo_1992]
- [Torrez et al 2009][research_torrez_driscoll_2009]
- [Toten et al 1991][research_toten_fong_1991]
- [Tournes 2013][research_tournes_2013]
- [Townend 1995][research_townend_1995]
- [Trefny 1999][research_trefny_1999]
- [Trefny et al 2017][research_trefnycharlesj_dippoldvancefiii_2017]
- [Treviño 1995][research_trevino_1995]
- [Trexler 1974][research_trexler_1974]
- [Trexler 1975][research_trexlerca_1975]
- [Trexler 1988][research_trexlercarla_1988]
- [Triantou et al 2017][research_triantou_mergia_2017]
- [Triantou et al 2017][research_triantou_perez_2017]
- [Trimmer 1968][research_trimmer_1968]
- [Trivedi and Menezes 2012][research_trivedi_menezes_2012]
- [Trolier and Krawczyk 1996][research_trolier_krawczyk_1996]
- [Trudgian et al 2025][research_trudgian_vanyai_2025]
- [Trujillo 1970][research_trujillo_1970]
- [Tsai 1991][research_tsai_1991]
- [Tsentis et al 2021][research_tsentis_gkoutzamanis_2021]
- [Tsuboi et al 2017][research_tsuboi_eto_2017]
- [Tsuchiya and Mori 2005][research_tsuchiya_mori_2005]
- [Tsujikawa 1995][research_tsujikawa_1995]
- [Tsujikawa 1996][research_tsujikawa_1996]
- [Tsujikawa et al 1991][research_tsujikawa_tsukamoto_1991]
- [Tsunekawa et al 1992][research_tsunekawa_gotoh_1992]
- [Tufts et al 2018][research_tufts_gosse_2018]
- [Tumuklu and Hanquist 2023][research_tumuklu_hanquist_2023]
- [Turchi et al 2021][research_turchi_matesanzsaiz_2021]
- [Turner 1965][research_turner_1965]
- [Turner et al 2006][research_turner_hoerschgen_2006]
- [Tuttle 1995][research_tuttlesean_1995]
- [Tuttle 2021][research_tuttle_2021]
- [Tuttle and Rogacki 1991][research_tuttle_rogacki_1991]
- [Tuttle et al 1995][research_tuttle_mee_1995]
- [Tyll et al 2000][research_tyll_bakos_2000]
- [Türkoğlu et al 2026][research_turkoglu_donmez_2026]
- [Udhayakumar et al 2016][research_s_ad_2016]
- [Ueda et al 2004][research_ueda_weiland_2004]
- [ul Islam Rizvi et al 2015][research_ulislamrizvi_linshu_2015]
- [Ullman and Raman 2023][research_ullman_raman_2023]
- [Ullman et al 2025][research_ullman_sharma_2025]
- [Universal Energy Systems Inc Dayton Oh 1995][research_universalenergysystemsincdaytonoh_1995]
- [Universal Technology Corp Dayton Oh 2014][research_universaltechnologycorpdaytonoh_2014]
- [Unsteady interaction mechanism of transverse stage separation in hypersonic flow for a two-stage-to-orbit vehicle 2023][research_unsteady_interaction_2023]
- [Unterberg 1957][research_unterberg_1957]
- [Upsadhya 2001][research_upsadhya_2001]
- [Urso et al 2022][research_urso_kinney_2022]
- [Urzay 2018][research_urzay_2018]
- [Ustinov and Kachanov 2021][research_ustinov_kachanov_2021]
- [Utilization of gas atomized 2001][research_utilization_of_2001]
- [Uy et al 2023][research_uy_hao_2023]
- [Vachon et al 2005][research_vachon_grindle_2005]
- [Vaden et al 2009][research_vaden_debes_2009]
- [Vahl and Edwards 1978][research_vahlwa_edwardsclw_1978]
- [Vaicaitis 1991][research_vaicaitis_1991]
- [Val et al 2020][research_val_chazot_2020]
- [Van 1963][research_van_1963]
- [Van Beck and Raman 2024][research_vanbeck_raman_2024]
- [Van Buren and Mease 1991][research_vanburen_mease_1991]
- [van der Lee et al 2022][research_vanderlee_yokev_2022]
- [van der Lee et al 2026][research_vanderlee_kaner_2026]
- [van Keuk et al 1998][research_vankeuk_ballmann_1998]
- [van Staden et al 2020][research_vanstaden_lorrain_2020]
- [Van Wie 1992][research_vanwie_1992]
- [Vanamamalai and Panneerselvam 2024][research_vanamamalai_panneerselvam_2024]
- [Vander Schaaf et al 2025][research_vanderschaaf_acharya_2025]
- [Vanmol and Anderson 1992][research_vanmol_andersonjr_1992]
- [Vanyai 2018][research_vanyai_2018]
- [Vargas Venegas and Huang 2023][research_vargasvenegas_huang_2023]
- [Varner 1976][research_varner_1976]
- [Varner et al 1987][research_varnermo_martindalewr_1987]
- [Varwig 1963][research_varwig_1963]
- [Vasil'ev and Petrov 1977][research_vasilev_petrov_1977]
- [Veeramanikandan 2023][research_veeramanikandan_2023]
- [Veeran et al 2018][research_veeran_pesyridis_2018]
- [Venegas et al 2026][research_venegas_huang_2026]
- [Venkatachalam et al 2024][research_venkatachalam_esser_2024]
- [Venkatapathy 1994][research_venkatapathy_1994]
- [Venkatapathy et al 1995][research_venkatapathy_tokarcikpolsky_1995]
- [Venkatesan and Vasanth 2024][research_venkatesan_s_2024]
- [Venkateshwaran and Padmanathan 2026][research_venkateshwaran_padmanathan_2026]
- [Verant and Sagnier 1996][research_verant_sagnier_1996]
- [Verma et al 2021][research_verma_pandey_2021]
- [Vert and Bouchard 2024][research_vert_bouchard_2024]
- [Viaud and Mestre 1966][research_viaud_mestre_1966]
- [Vigilante et al 1997][research_vigilante_cote_1997]
- [Vinogradov et al 1992][research_vinogradov_stepanov_1992]
- [Vinson and Shore 1967][research_vinson_shore_1967]
- [Vlassak 2008][research_vlassak_2008]
- [Voland 1990][research_voland_1990]
- [Voland et al 1998][research_voland_rock_1998]
- [Voland et al 1999][research_voland_auslender_1999]
- [Voland et al 2005][research_voland_huebner_2005]
- [Voland et al 2006][research_voland_huebner_2006]
- [Volkov et al 2015][research_volkov_emelyanov_2015]
- [Volpiani 2021][research_volpiani_2021]
- [Voronin 2020][research_voronin_2020]
- [Voth and Ludtke 1979][research_voth_ludtke_1979]
- [Vuillermoz et al 1992][research_vuillermoz_oran_1992]
- [Vyas et al 2010][research_vyasmanana_engblomwilliama_2010]
- [Wada 2026][research_wada_2026]
- [Wadhams et al 2008][research_wadhams_maclean_2008]
- [Wadley et al 1990][research_wadley_elzey_1990]
- [Wagner and Dale 1985][research_wagner_dale_1985]
- [Waidmann et al 2024][research_waidmann_brummund_2024]
- [Walchner 1974][research_walchner_1974]
- [Waldman and Harsha 1992][research_waldman_harsha_1992]
- [Walker 1952][research_walker_1952]
- [Walker 2025][research_walker_2025]
- [Wallace et al 2003][research_wallaceta_birdrk_2003]
- [Walsh et al 2024][research_walsh_zhan_2024]
- [Walton 1990][research_waltonjt_1990]
- [Walton 1991][research_walton_1991]
- [Walton 1992][research_waltonjamest_1992]
- [Walton and Pinckney 1994][research_walton_pinckney_1994]
- [Waltrup et al 1981][research_waltrup_billig_1981]
- [Waltrup et al 1996][research_waltrup_white_1996]
- [Wan et al 2025][research_wan_ma_2025]
- [Wan et al 2026][research_wan_shi_2026]
- [Wan et al 2026][research_wan_wang_2026]
- [Wang 2023][research_wang_2023]
- [Wang and Guo 2013][research_wang_guo_2013]
- [Wang and Jiang 2020][research_wang_jiang_2020]
- [Wang and Li 2016][research_wang_li_2016]
- [Wang and Luo 2022][research_wang_luo_2022]
- [Wang and Wang 2024][research_wang_wang_2024_b]
- [Wang and Xu 2024][research_wang_xu_2024_b]
- [Wang and Zhang 2018][research_wang_zhang_2018]
- [Wang and Zhang 2021][research_wang_zhang_2021]
- [Wang and Zhang 2022][research_wang_zhang_2022_c]
- [Wang et al 1995][research_wang_zhou_1995]
- [Wang et al 2007][research_wangxiaoyen_harpstergeorge_2007]
- [Wang et al 2014][research_wang_wang_2014]
- [Wang et al 2015][research_wang_shan_2015]
- [Wang et al 2015][research_wang_wang_2015]
- [Wang et al 2016][research_wang_cai_2016]
- [Wang et al 2016][research_wang_liu_2016]
- [Wang et al 2016][research_wang_liu_2016_b]
- [Wang et al 2016][research_wang_wang_2016]
- [Wang et al 2016][research_wang_xiao_2016]
- [Wang et al 2016][research_wang_zhang_2016]
- [Wang et al 2017][research_wang_cai_2017]
- [Wang et al 2017][research_wang_liu_2017]
- [Wang et al 2017][research_wang_yang_2017]
- [Wang et al 2018][research_wang_he_2018]
- [Wang et al 2018][research_wang_hou_2018]
- [Wang et al 2018][research_wang_li_2018]
- [Wang et al 2018][research_wang_li_2018_b]
- [Wang et al 2018][research_wang_pan_2018]
- [Wang et al 2018][research_wang_wang_2018]
- [Wang et al 2019][research_wang_guo_2019]
- [Wang et al 2019][research_wang_hou_2019]
- [Wang et al 2019][research_wang_liu_2019]
- [Wang et al 2019][research_wang_nie_2019]
- [Wang et al 2019][research_wang_wang_2019]
- [Wang et al 2019][research_wang_wei_2019]
- [Wang et al 2019][research_wang_xue_2019]
- [Wang et al 2020][research_wang_chen_2020]
- [Wang et al 2020][research_wang_cheng_2020]
- [Wang et al 2020][research_wang_cheng_2020_b]
- [Wang et al 2020][research_wang_li_2020]
- [Wang et al 2020][research_wang_yang_2020]
- [Wang et al 2021][research_wang_chang_2021]
- [Wang et al 2021][research_wang_dang_2021]
- [Wang et al 2021][research_wang_gao_2021]
- [Wang et al 2021][research_wang_ha_2021]
- [Wang et al 2021][research_wang_he_2021]
- [Wang et al 2021][research_wang_hou_2021]
- [Wang et al 2022][research_wang_cheng_2022]
- [Wang et al 2022][research_wang_fan_2022]
- [Wang et al 2022][research_wang_gao_2022]
- [Wang et al 2022][research_wang_jin_2022]
- [Wang et al 2022][research_wang_li_2022]
- [Wang et al 2022][research_wang_wang_2022]
- [Wang et al 2022][research_wang_wei_2022]
- [Wang et al 2022][research_wang_xin_2022]
- [Wang et al 2022][research_wang_yu_2022_b]
- [Wang et al 2022][research_wang_zhang_2022]
- [Wang et al 2022][research_wang_zhao_2022]
- [Wang et al 2023][research_wang_eri_2023]
- [Wang et al 2023][research_wang_eri_2023_b]
- [Wang et al 2023][research_wang_fan_2023]
- [Wang et al 2023][research_wang_huang_2023]
- [Wang et al 2023][research_wang_liu_2023]
- [Wang et al 2023][research_wang_qian_2023]
- [Wang et al 2023][research_wang_wang_2023]
- [Wang et al 2023][research_wang_xu_2023]
- [Wang et al 2023][research_wang_xu_2023_b]
- [Wang et al 2024][research_wang_liu_2024]
- [Wang et al 2024][research_wang_pan_2024]
- [Wang et al 2024][research_wang_wang_2024]
- [Wang et al 2024][research_wang_wang_2024_c]
- [Wang et al 2024][research_wang_xu_2024]
- [Wang et al 2024][research_wang_zou_2024]
- [Wang et al 2025][research_wang_an_2025]
- [Wang et al 2025][research_wang_he_2025]
- [Wang et al 2025][research_wang_jordan_2025]
- [Wang et al 2025][research_wang_liu_2025]
- [Wang et al 2025][research_wang_liu_2025_b]
- [Wang et al 2025][research_wang_tang_2025]
- [Wang et al 2025][research_wang_xu_2025]
- [Wang et al 2025][research_wang_yang_2025]
- [Wang et al 2025][research_wang_yao_2025]
- [Wang et al 2026][research_wang_chen_2026]
- [Wang et al 2026][research_wang_cheng_2026]
- [Wang et al 2026][research_wang_du_2026]
- [Wang et al 2026][research_wang_fang_2026]
- [Wang et al 2026][research_wang_guo_2026]
- [Wang et al 2026][research_wang_hong_2026]
- [Wang et al 2026][research_wang_huang_2026]
- [Wang et al 2026][research_wang_song_2026]
- [Wang et al 2026][research_wang_yuan_2026]
- [Wang et al 2026][research_wang_zhang_2026]
- [Ward and Hewitt 1988][research_ward_hewitt_1988]
- [Ward and Smart 2021][research_ward_smart_2021]
- [Wartemann et al 2019][research_wartemann_ponchiocamillo_2019]
- [Wasserbauer et al 1996][research_wasserbauerjf_meleasonet_1996]
- [Watanabe 1992][research_watanabe_1992]
- [Watanabe 1993][research_watanabe_1993]
- [Watanabe et al 1996][research_watanabe_ishimoto_1996]
- [Watanabe et al 1997][research_watanabe_ishimoto_1997]
- [Watkins 1990][research_watkinswilliamb_1990]
- [Watt and Aronson 1964][research_watt_aronson_1964]
- [Webb and Samimy 2016][research_webb_samimy_2016]
- [Webber et al 2026][research_webber_reeves_2026]
- [Wei and Tsung-Ming 1994][research_wei_tsungming_1994]
- [Wei et al 2015][research_wei_tian_2015]
- [Wei et al 2017][research_wei_xue_2017]
- [Wei et al 2018][research_wei_liu_2018]
- [Wei et al 2023][research_wei_zhang_2023]
- [Wei et al 2024][research_wei_jiao_2024]
- [Wei et al 2024][research_wei_shi_2024]
- [Wei et al 2024][research_wei_zhang_2024]
- [Weidner 1979][research_weidnerjp_1979]
- [Weidner 1992][research_weidnerjohnp_1992]
- [Weidner 1996][research_weidnerjohnp_1996]
- [Weidner et al 1976][research_weidnerjp_smallwj_1976]
- [Weilmuenster and Gnoffo 1992][research_weilmuenster_gnoffo_1992]
- [Weilmuenster et al 1996][research_weilmuenster_gnoffo_1996]
- [Weilmuenster et al 1997][research_weilmuenster_gnoffo_1997]
- [Weissman 1990][research_weissman_1990]
- [Wen 2023][research_wen_2023]
- [Wen et al 2011][research_wen_chen_2011]
- [Wendt et al 1993][research_wendtm_nettletonm_1993]
- [Werner et al 2014][research_werner_smarsly_2014]
- [West and Bynum 2021][research_west_bynum_2021]
- [West and Bynum 2024][research_west_bynum_2024]
- [West and Hosder 2015][research_west_hosder_2015]
- [West and Mitchell 1994][research_west_mitchell_1994]
- [Whalen and Hardy 1992][research_whalen_hardy_1992]
- [Whalen et al 1993][research_whalen_hardy_1993]
- [Wheaton et al][research_bradleymwheaton_ivettaleyva]
- [Whitcomb 2010][research_whitcomb_2010]
- [White 1993][research_white_1993]
- [White 2004][research_white_2004]
- [White and Ault 1996][research_white_ault_1996]
- [White and Rhie 1992][research_white_rhie_1992]
- [White and Sreenivasan 1998][research_white_sreenivasan_1998]
- [Whitehead 1989][research_whiteheadallenhjr_1989]
- [Whitehead 1996][research_whitehead_1996]
- [Whitehead 2007][research_whitehead_2007]
- [Whitehurst et al 1992][research_whitehurstrb_kraussrh_1992]
- [Whitfield and Potter 1959][research_whitfield_potter_1959]
- [Whitside 2021][research_whitside_2021]
- [Wierzbanowski and Armstrong 1991][research_wierzbanowskitheodore_armstrongjohnnyg_1991]
- [Wierzbanowski and Kasten 1990][research_wierzbanowskitheodore_kastenterryd_1990]
- [Wierzbanowski and McCorry 1990][research_wierzbanowski_mccorry_1990]
- [Wieting 1990][research_wieting_1990]
- [Wieting and Guy 1975][research_wietingar_guyrw_1975]
- [Wieting and Guy 1976][research_wieting_guy_1976]
- [Wiezorek and Mills 1998][research_wiezorek_mills_1998]
- [Wilder 1949][research_wilder_jr_1949]
- [Wilhite 1983][research_wilhite_1983]
- [Wilhite 1991][research_wilhite_1991]
- [Wilhite et al 1991][research_wilhite_bush_1991]
- [Wilkinson and Ruggles-Wrenn 2016][research_wilkinson_ruggleswrenn_2016]
- [Willaime et al 1998][research_willaime_belin_1998]
- [Willbanks 1970][research_willbanks_1970]
- [William-Sobers et al 2025][research_williamsobers_agwu_2025]
- [Williams and Lewis 1975][research_williams_lewis_1975]
- [Williams et al 1996][research_williams_lei_1996]
- [Williams et al 2017][research_williams_mall_2017]
- [Williamson 1992][research_williamson_1992]
- [Wilson 1992][research_wilson_1992]
- [Wilson Chan et al 2014][research_wilsonchan_razzaqi_2014]
- [Winkler 1952][research_winkler_1952]
- [Winkler and Bush 1992][research_winkler_bush_1992]
- [Wisbey and Ward-Close 1997][research_wisbey_wardclose_1997]
- [Wisbey et al 1994][research_wisbey_kearns_1994]
- [Wittliff and Wilson 1961][research_wittliff_wilson_1961]
- [Wittliff and Wilson 1961][research_wittliff_wilson_1961_b]
- [Wittliff et al 1992][research_wittliff_oconnor_1992]
- [WlMBERLY et al 1970][research_wlmberly_mcginnis_1970]
- [Wolf and Daum 1993][research_wolf_daum_1993]
- [Wolf et al 1951][research_wolf_mullen_1951]
- [Wolfle 1969][research_wolfle_1969]
- [Won et al 2006][research_won_jeung_2006]
- [Won et al 2007][research_won_jeung_2007]
- [Wood 1968][research_wood_1968]
- [Woodcock 1988][research_woodcock_1988]
- [Woodruff and Lorenz 1966][research_woodruff_lorenz_1966]
- [Woods et al 1983][research_woods_arrington_1983]
- [Woods et al 2000][research_woods_holland_2000]
- [Wortman 1970][research_wortman_1970]
- [Wright 1989][research_wrighthowardt_1989]
- [Wright 1993][research_wrightgeorgefjr_1993]
- [Wright 1996][research_wright_1996]
- [Wright et al 2003][research_wright_achary_2003]
- [Wu 1992][research_wu_1992]
- [Wu 2026][research_wu_2026]
- [Wu and Wei 2022][research_wu_wei_2022]
- [Wu and Zhang 2023][research_wu_zhang_2023]
- [Wu et al 2015][research_wu_jiang_2015]
- [Wu et al 2015][research_wu_yang_2015]
- [Wu et al 2016][research_wu_wang_2016]
- [Wu et al 2019][research_wu_liang_2019]
- [Wu et al 2020][research_wu_lin_2020]
- [Wu et al 2021][research_wu_deng_2021]
- [Wu et al 2021][research_wu_song_2021]
- [Wu et al 2025][research_wu_he_2025]
- [Wu et al 2025][research_wu_yuan_2025]
- [Wu et al 2026][research_wu_gao_2026]
- [Wu et al 2026][research_wu_zhao_2026]
- [Wurster and Stone 1993][research_wursterke_stonehw_1993]
- [Wurster et al 1998][research_wursterkathryne_rileychristopherj_1998]
- [X-43A Research Vehicle Design 2011][research_x_43a_research_2011]
- [Xia et al 2020][research_xia_chen_2020]
- [Xia et al 2023][research_xia_li_2023]
- [Xia et al 2023][research_xia_li_2023_b]
- [Xia et al 2026][research_xia_han_2026]
- [Xiang et al 2020][research_xiang_yang_2020]
- [Xianhong et al 2015][research_xianhong_yuan_2015]
- [Xiao et al 2004][research_xiao_edwards_2004]
- [Xiao et al 2006][research_xiao_liu_2006]
- [Xiao et al 2008][research_xiao_yue_2008]
- [Xiao et al 2012][research_xiao_yue_2012]
- [Xiao et al 2024][research_xiao_lu_2024]
- [Xiao et al 2025][research_xiao_wu_2025]
- [Xiaoqing et al 2010][research_xiaoqing_zhongxi_2010]
- [Xiaoxuan et al 2018][research_xiaoxuan_jinglong_2018]
- [Xie et al 2020][research_xie_dong_2020]
- [Xie et al 2025][research_xie_liu_2025]
- [Xie et al 2025][research_xie_xia_2025]
- [Xie et al 2026][research_xie_zhao_2026]
- [Xinchun et al 2021][research_xinchun_zhongwei_2021]
- [Xinchun Li et al 2020][research_xinchunli_zhongweiwang_2020]
- [Xing et al 2012][research_xing_zhang_2012]
- [Xing et al 2016][research_xing_xiao_2016]
- [Xing et al 2017][research_xing_cai_2017]
- [Xing et al 2017][research_xing_ruan_2017]
- [Xing-hao et al 2021][research_xinghao_haijie_2021]
- [Xiong et al 2019][research_xiong_bai_2019]
- [Xiong et al 2019][research_xiong_fan_2019]
- [Xiong et al 2020][research_xiong_qin_2020]
- [Xiong et al 2022][research_xiong_qin_2022]
- [Xu and Fang 2022][research_xu_fang_2022]
- [Xu and Wu 2018][research_xu_wu_2018]
- [Xu et al 2008][research_xu_he_2008]
- [Xu et al 2018][research_xu_cheng_2018]
- [Xu et al 2019][research_xu_xu_2019]
- [Xu et al 2020][research_xu_liu_2020]
- [Xu et al 2021][research_xu_lin_2021]
- [Xu et al 2022][research_xu_wang_2022]
- [Xu et al 2024][research_xu_he_2024]
- [Xu et al 2024][research_xu_lin_2024]
- [Xu et al 2025][research_xu_guo_2025]
- [Xu et al 2025][research_xu_han_2025]
- [Xu et al 2025][research_xu_leng_2025]
- [Xu et al 2025][research_xu_liao_2025]
- [Xu et al 2025][research_xu_yu_2025]
- [Xu et al 2026][research_xu_zhu_2026]
- [Xue et al 2025][research_xue_he_2025]
- [Xue et al 2026][research_xue_li_2026]
- [Yamada and Fujii 1999][research_yamada_fujii_1999]
- [Yamaguchi et al 2020][research_yamaguchi_hizawa_2020]
- [Yamanaka 1989][research_yamanaka_1989]
- [Yamanaka 1992][research_yamanaka_1992]
- [Yan and Wang 2022][research_yan_wang_2022]
- [Yan and Yang 2025][research_yan_yang_2025]
- [Yan et al 2016][research_yan_shaohua_2016]
- [Yan et al 2018][research_yan_he_2018]
- [Yan et al 2018][research_yan_he_2018_b]
- [Yan et al 2021][research_yan_teng_2021]
- [Yan et al 2022][research_yan_fan_2022]
- [Yan et al 2022][research_yan_liu_2022]
- [Yan et al 2022][research_yan_liu_2022_b]
- [Yan et al 2023][research_yan_wang_2023]
- [Yan et al 2025][research_yan_tian_2025]
- [Yan et al 2026][research_yan_le_2026]
- [Yan et al 2026][research_yan_wang_2026]
- [Yang 2026][research_yang_2026]
- [yang and culick 1986][research_yang_culick_1986]
- [Yang and Liu 2017][research_yang_liu_2017]
- [Yang and Sun 2011][research_yang_sun_2011]
- [Yang and Yuh-Yih Wu 1994][research_yang_yuhyihwu_1994]
- [Yang et al 1993][research_yang_kubota_1993]
- [Yang et al 2014][research_yang_chang_2014]
- [Yang et al 2014][research_yang_duan_2014]
- [Yang et al 2015][research_yang_chang_2015]
- [Yang et al 2015][research_yang_shi_2015]
- [Yang et al 2017][research_yang_bao_2017]
- [Yang et al 2018][research_yang_gui_2018]
- [Yang et al 2019][research_yang_li_2019]
- [Yang et al 2020][research_yang_gui_2020]
- [Yang et al 2020][research_yang_lee_2020]
- [Yang et al 2021][research_yang_li_2021]
- [Yang et al 2021][research_yang_xia_2021]
- [Yang et al 2022][research_yang_wang_2022]
- [Yang et al 2023][research_yang_song_2023]
- [Yang et al 2023][research_yang_yang_2023]
- [Yang et al 2024][research_yang_che_2024]
- [Yang et al 2024][research_yang_choi_2024]
- [Yang et al 2024][research_yang_choi_2024_b]
- [Yang et al 2024][research_yang_qiu_2024]
- [Yang et al 2024][research_yang_tian_2024]
- [Yang et al 2025][research_yang_xie_2025]
- [Yang et al 2026][research_yang_gao_2026]
- [Yang et al 2026][research_yang_hayat_2026]
- [Yang et al 2026][research_yang_li_2026]
- [Yankui et al 2005][research_yankui_dongjun_2005]
- [Yao 2022][research_yao_2022]
- [Yao and Marck 1995][research_yao_marck_1995]
- [Yao and Xia 2023][research_yao_xia_2023]
- [Yao and Xia 2024][research_yao_xia_2024]
- [Yao et al 2017][research_yao_tang_2017]
- [Yao et al 2021][research_yao_liu_2021]
- [Yao et al 2023][research_yao_gu_2023]
- [Yao et al 2023][research_yao_sun_2023]
- [Yao et al 2025][research_yao_wu_2025]
- [Yaros 1991][research_yaros_1991]
- [Yasunaga et al 2024][research_yasunaga_nakaya_2024]
- [Yates 1967][research_yates_1967]
- [Yatsukhno 2018][research_yatsukhno_2018]
- [Ye et al 2019][research_ye_ye_2019]
- [Ye et al 2019][research_ye_ye_2019_b]
- [Yen 1963][research_yen_1963]
- [Yentsch and Gaitonde 2012][research_yentsch_gaitonde_2012]
- [Yentsch and Gaitonde 2013][research_yentsch_gaitonde_2013]
- [Yentsch and Gaitonde 2013][research_yentsch_gaitonde_2013_b]
- [Yi and Xie 2024][research_yi_xie_2024]
- [Yi et al 2020][research_yi_lou_2020]
- [Yin and He 2023][research_yin_he_2023]
- [Yin et al 2022][research_yin_e_2022]
- [Yin et al 2023][research_yin_jiang_2023]
- [Yin et al 2024][research_yin_li_2024]
- [Yin et al 2026][research_yin_li_2026]
- [Yip et al 1990][research_yip_strawa_1990]
- [Yokoo et al 2020][research_yokoo_goto_2020]
- [Yongsheng 2014][research_yongsheng_2014]
- [Yoon and Ahn 2016][research_yoon_ahn_2016]
- [Yoshida et al 2019][research_yoshida_micci_2019]
- [Youn and Mills 1995][research_youn_mills_1995]
- [Yount et al 2012][research_yountbryanc_arnoldjameso_2012]
- [Yu 2015][research_yu_2015]
- [Yu 2024][research_yu_2024]
- [Yu and Yuan 2016][research_yu_yuan_2016]
- [Yu et al 1988][research_yushengtao_hsiehkwangchung_1988]
- [Yu et al 2005][research_yu_kim_2005]
- [Yu et al 2017][research_yu_jones_2017]
- [Yu et al 2017][research_yu_pan_2017]
- [Yu et al 2019][research_yu_wang_2019]
- [Yu et al 2019][research_yu_wang_2019_b]
- [Yu et al 2019][research_yu_wang_2019_c]
- [Yu et al 2019][research_yu_yu_2019]
- [Yu et al 2020][research_yu_chen_2020]
- [Yu et al 2020][research_yu_chen_2020_b]
- [Yu et al 2020][research_yu_huang_2020]
- [Yu et al 2020][research_yu_wang_2020]
- [Yu et al 2021][research_yu_ni_2021]
- [Yu et al 2022][research_yu_li_2022]
- [Yu et al 2022][research_yu_zhou_2022]
- [Yu et al 2025][research_yu_wang_2025]
- [Yu et al 2025][research_yu_yang_2025]
- [Yu et al 2026][research_yu_wang_2026]
- [Yuan et al 2026][research_yuan_liu_2026]
- [Yue et al 2009][research_yue_xiao_2009]
- [Yue et al 2016][research_yue_wu_2016]
- [Yue et al 2018][research_yue_nie_2018]
- [Yue et al 2022][research_yue_titurus_2022]
- [Yun et al 2026][research_yun_kim_2026]
- [Yungster 1992][research_yungster_1992]
- [Yungster et al 2015][research_yungstershaye_paxsondaniele_2015]
- [Yushchenkova et al 1967][research_yushchenkova_pomerantsev_1967]
- [Zagainov and Plokhikh 1991][research_zagainov_plokhikh_1991]
- [Zaldivar et al 1998][research_zaldivar_rellick_1998]
- [Zaludin 2025][research_zaludin_2025]
- [Zan et al 2018][research_zan_li_2018]
- [Zander et al 2021][research_zander_vinkeloe_2021]
- [Zangiev et al 2016][research_zangiev_ivanov_2016]
- [Zarlingo 1988][research_zarlingo_1988]
- [Zeng et al 2026][research_zeng_wang_2026]
- [Zhai and Yang 2020][research_zhai_yang_2020]
- [Zhang 2015][research_zhang_2015]
- [Zhang 2020][research_zhang_2020]
- [Zhang 2020][research_zhang_2020_b]
- [Zhang 2020][research_zhang_2020_c]
- [Zhang 2020][research_zhang_2020_d]
- [Zhang and Ding 2023][research_zhang_ding_2023]
- [Zhang and Xian 2015][research_zhang_xian_2015]
- [Zhang et al 2014][research_zhang_chen_2014]
- [Zhang et al 2015][research_zhang_chen_2015]
- [Zhang et al 2015][research_zhang_hong_2015]
- [Zhang et al 2015][research_zhang_yang_2015]
- [Zhang et al 2016][research_zhang_feng_2016]
- [Zhang et al 2016][research_zhang_feng_2016_b]
- [Zhang et al 2016][research_zhang_li_2016]
- [Zhang et al 2016][research_zhang_xu_2016]
- [Zhang et al 2017][research_zhang_chang_2017]
- [Zhang et al 2017][research_zhang_wang_2017]
- [Zhang et al 2017][research_zhang_zhang_2017]
- [Zhang et al 2018][research_zhang_chang_2018]
- [Zhang et al 2018][research_zhang_chen_2018]
- [Zhang et al 2018][research_zhang_liu_2018]
- [Zhang et al 2018][research_zhang_liu_2018_b]
- [Zhang et al 2018][research_zhang_wang_2018]
- [Zhang et al 2019][research_zhang_cao_2019]
- [Zhang et al 2019][research_zhang_niu_2019]
- [Zhang et al 2019][research_zhang_wei_2019]
- [Zhang et al 2019][research_zhang_yue_2019]
- [Zhang et al 2020][research_zhang_li_2020]
- [Zhang et al 2020][research_zhang_qiao_2020]
- [Zhang et al 2020][research_zhang_wang_2020]
- [Zhang et al 2020][research_zhang_wang_2020_b]
- [Zhang et al 2021][research_zhang_tong_2021]
- [Zhang et al 2022][research_zhang_sun_2022]
- [Zhang et al 2022][research_zhang_wang_2022]
- [Zhang et al 2022][research_zhang_zhang_2022]
- [Zhang et al 2023][research_zhang_chen_2023]
- [Zhang et al 2023][research_zhang_chen_2023_b]
- [Zhang et al 2023][research_zhang_feng_2023]
- [Zhang et al 2023][research_zhang_li_2023]
- [Zhang et al 2023][research_zhang_lin_2023]
- [Zhang et al 2023][research_zhang_yao_2023]
- [Zhang et al 2023][research_zhang_yi_2023]
- [Zhang et al 2023][research_zhang_zhang_2023]
- [Zhang et al 2024][research_zhang_nie_2024]
- [Zhang et al 2024][research_zhang_shi_2024]
- [Zhang et al 2024][research_zhang_wu_2024]
- [Zhang et al 2024][research_zhang_yu_2024]
- [Zhang et al 2025][research_zhang_han_2025]
- [Zhang et al 2025][research_zhang_liang_2025]
- [Zhang et al 2025][research_zhang_pan_2025]
- [Zhang et al 2025][research_zhang_su_2025]
- [Zhang et al 2025][research_zhang_xie_2025]
- [Zhang et al 2025][research_zhang_zhang_2025]
- [Zhang et al 2026][research_zhang_li_2026]
- [Zhang et al 2026][research_zhang_liao_2026]
- [Zhang et al 2026][research_zhang_zhou_2026]
- [Zhao et al 1985][research_zhao_bradt_1985]
- [Zhao et al 2019][research_zhao_dong_2019]
- [Zhao et al 2019][research_zhao_liu_2019]
- [Zhao et al 2020][research_zhao_li_2020]
- [Zhao et al 2020][research_zhao_liu_2020]
- [Zhao et al 2021][research_zhao_he_2021]
- [Zhao et al 2022][research_zhao_shao_2022]
- [Zhao et al 2022][research_zhao_sun_2022]
- [Zhao et al 2022][research_zhao_xia_2022]
- [Zhao et al 2023][research_zhao_fan_2023]
- [Zhao et al 2023][research_zhao_gao_2023]
- [Zhao et al 2023][research_zhao_tian_2023]
- [Zhao et al 2023][research_zhao_zhang_2023]
- [Zhao et al 2025][research_zhao_ma_2025]
- [Zhao et al 2025][research_zhao_wu_2025]
- [Zhao et al 2025][research_zhao_wu_2025_b]
- [Zhao et al 2026][research_zhao_bai_2026]
- [Zhao et al 2026][research_zhao_chen_2026]
- [Zheng and Bray 1994][research_zheng_bray_1994]
- [Zheng and Wang 2018][research_zheng_wang_2018]
- [Zheng et al 2018][research_zheng_chang_2018]
- [Zheng et al 2019][research_zheng_chang_2019]
- [Zheng et al 2020][research_zheng_chang_2020]
- [Zheng et al 2020][research_zheng_yan_2020]
- [Zheng et al 2021][research_zheng_chang_2021]
- [Zheng et al 2021][research_zheng_xiong_2021]
- [Zheng et al 2022][research_zheng_jiang_2022]
- [Zheng et al 2023][research_zheng_wu_2023]
- [Zheng et al 2025][research_zheng_huang_2025]
- [Zhi et al 2015][research_zhi_ran_2015]
- [Zhikharev 1993][research_zhikharev_1993]
- [Zhivotov 1996][research_zhivotov_1996]
- [Zhluktov and Tirskii 1990][research_zhluktov_tirskii_1990]
- [Zhong 1998][research_zhong_1998]
- [Zhong 2007][research_zhong_2007]
- [Zhong 2009][research_zhong_2009]
- [Zhong and Peng 2018][research_zhong_peng_2018]
- [Zhong and Peng 2019][research_zhong_peng_2019]
- [Zhong et al 2025][research_zhong_qu_2025]
- [Zhong et al 2025][research_zhong_xu_2025]
- [Zhou 2023][research_zhou_2023]
- [Zhou et al 2015][research_zhou_yan_2015]
- [Zhou et al 2016][research_zhou_yan_2016]
- [Zhou et al 2016][research_zhou_zhao_2016]
- [Zhou et al 2017][research_zhou_jiang_2017]
- [Zhou et al 2017][research_zhou_li_2017]
- [Zhou et al 2017][research_zhou_lu_2017]
- [Zhou et al 2018][research_zhou_zhao_2018]
- [Zhou et al 2022][research_zhou_du_2022]
- [Zhou et al 2022][research_zhou_xu_2022]
- [Zhou et al 2023][research_zhou_li_2023]
- [Zhou et al 2023][research_zhou_tan_2023]
- [Zhou et al 2023][research_zhou_xia_2023]
- [Zhou et al 2024][research_zhou_fu_2024]
- [Zhou et al 2024][research_zhou_zhang_2024]
- [Zhou et al 2025][research_zhou_cao_2025]
- [Zhou et al 2025][research_zhou_tian_2025]
- [Zhou et al 2025][research_zhou_zhang_2025]
- [Zhu 2019][research_zhu_2019]
- [Zhu 2022][research_zhu_2022]
- [Zhu and Xu 2017][research_zhu_xu_2017]
- [Zhu et al 1999][research_zhu_ohtani_1999]
- [Zhu et al 2016][research_zhu_zhao_2016]
- [Zhu et al 2017][research_zhu_xu_2017_b]
- [Zhu et al 2018][research_zhu_chen_2018]
- [Zhu et al 2018][research_zhu_peng_2018]
- [Zhu et al 2021][research_zhu_shi_2021]
- [Zhu et al 2025][research_zhu_zhang_2025]
- [Zimont and Muhin 2009][research_zimont_muhin_2009]
- [Zoby and Thompson 1990][research_zoby_thompson_1990]
- [Zong et al 2015][research_zong_bao_2015]
- [Zong et al 2015][research_zong_wang_2015]
- [Zou et al 2016][research_zou_li_2016]
- [Zou et al 2022][research_zou_wang_2022]
- [Zou et al 2022][research_zou_wang_2022_b]
- [Zou et al 2026][research_zou_liu_2026]
- [Zubin et al 1997][research_zubin_ostapenko_1997]
- [Zukoski and Auerbach 1976][research_zukoski_auerbach_1976]
- [Zuo 2023][research_zuo_2023]
- [Zuo 2023][research_zuo_2023_b]
- [Zuo and Hu 2021][research_zuo_hu_2021]
- [Zuo and Mölder 2019][research_zuo_molder_2019]
- [Zuo et al 2015][research_zuo_huang_2015]
- [Zuo et al 2018][research_zuo_zhang_2018]
- [Zvegintsev 1993][research_zvegintsev_1993]
- [Çelik and Demirezen 2024][research_celik_demirezen_2024]
- [Özbek and Karyeyen 2023][research_ozbek_karyeyen_2023]

[research_266_on_1994]: https://doi.org/10.1016/0967-0661(94)91057-x
[research_3d_problems_2018]: https://doi.org/10.14529/jsfi180207
[research_95_01686_cavity_actuated_1995]: https://doi.org/10.1016/0140-6701(95)93351-4
[research_95_01778_reduced_1995]: https://doi.org/10.1016/0140-6701(95)93443-x
[research_95_01780_the_1995]: https://doi.org/10.1016/0140-6701(95)93445-6
[research_95_05986_oxidation_1995]: https://doi.org/10.1016/0140-6701(95)97624-s
[research_95_06326_ignition_1995]: https://doi.org/10.1016/0140-6701(95)97915-7
[research_95_06441_studies_1995]: https://doi.org/10.1016/0140-6701(95)98013-h
[research_96_05298_relationships_1996]: https://doi.org/10.1016/0140-6701(96)89992-9
[research_97_03061_a_1997]: https://doi.org/10.1016/s0140-6701(97)84932-6
[research_97_04270_ignition_1997]: https://doi.org/10.1016/s0140-6701(97)81565-2
[research_98_01484_effects_1998]: https://doi.org/10.1016/s0140-6701(98)97626-3
[research_98_03244_thermodynamics_1998]: https://doi.org/10.1016/s0140-6701(98)96769-8
[research_99_00179_performance_1999]: https://doi.org/10.1016/s0140-6701(99)92452-9
[research_a_conceptual_1992]: https://ntrs.nasa.gov/citations/19940020603
[research_a_study_1967]: https://ntrs.nasa.gov/citations/19670022001
[research_aarnes_white_1975]: https://doi.org/10.2514/3.44438
[research_aaronwfuchs_2019]: https://ntrs.nasa.gov/citations/20200005407
[research_abdelhameed_watanabe_2025]: https://doi.org/10.1016/j.ijhydene.2025.152035
[research_abell_1989]: https://doi.org/10.1126/science.246.4936.1375.a
[research_abrahamm_valsa_2018]: https://doi.org/10.18520/cs/v114/i01/144-147
[research_abtahi_dean_1990]: https://ntrs.nasa.gov/citations/19920007788
[research_abulhuda_gamba_2017]: https://doi.org/10.2514/1.b36543
[research_aburomia_1971]: https://doi.org/10.2514/6.1971-81
[research_accelerating_hypersonic_2022]: https://doi.org/10.12968/s1478-2774(23)50146-0
[research_acharya_2025]: https://doi.org/10.3390/aerospace12060503
[research_adamczak_bolender_2015]: https://doi.org/10.2514/6.2015-0528
[research_adamkhan_2024]: https://doi.org/10.1007/s11085-024-10239-w
[research_adams_1975]: https://doi.org/10.2514/3.27820
[research_adams_johnc_1970]: https://doi.org/10.21236/ad0714058
[research_adams_johnc_1973]: https://doi.org/10.21236/ad0756499
[research_adams_landrum_2001]: https://doi.org/10.2514/6.2001-3205
[research_adams_probstein_1958]: https://doi.org/10.2514/8.7237
[research_adamsjcjr_martindalewr_1976]: https://ntrs.nasa.gov/citations/19760054044
[research_adamsjcjr_martindalewr_1984]: https://ntrs.nasa.gov/citations/19840035307
[research_adelmanhenryg_meneesgenep_1996]: https://ntrs.nasa.gov/citations/19960021078
[research_advisorygroupforaerospaceresearchanddevelopment_1993]: https://ntrs.nasa.gov/citations/19940024743
[research_advisorygroupforaerospaceresearchanddevelopment_1997]: https://ntrs.nasa.gov/citations/19980018672
[research_aero_space_plane_1991]: https://ntrs.nasa.gov/citations/19950004141
[research_aerothermodynamics_of_2001]: https://doi.org/10.2514/5.9781600866609.0569.0595
[research_aerothermodynamics_of_2022]: https://doi.org/10.1002/9781119640646.ch3
[research_aerothermodynamics_research_2002]: https://doi.org/10.2514/5.9781600866678.0205.0237
[research_agnone_1972]: https://ntrs.nasa.gov/citations/19730012102
[research_agnone_prakasam_1987]: https://doi.org/10.2514/3.25894
[research_agnoneanthonym_1987]: https://ntrs.nasa.gov/citations/19870037657
[research_agresta_andriani_2013]: https://doi.org/10.2514/6.2013-3701
[research_aguilera_yu_2017]: https://doi.org/10.1016/j.proci.2016.06.113
[research_ahearn_rand_1996]: https://doi.org/10.1016/0008-6223(96)00164-9
[research_ahmed_ameenk_2023]: https://doi.org/10.2514/6.2023-3078
[research_ahmed_saenz_2024]: https://doi.org/10.2514/6.2024-0067
[research_ahuja_hartfield_2015]: https://doi.org/10.2514/1.b35212
[research_airbreathing_hypersonic_1997]: https://doi.org/10.2514/5.9781600866449.0297.0371
[research_aircraft_engine_1992]: https://doi.org/10.1108/eb037251
[research_airforcetestpilotschooledwardsafbca_1987]: https://doi.org/10.21236/ada320212
[research_akihisa_masuya_2000]: https://doi.org/10.2514/6.2000-619
[research_akpolat_toker_2014]: https://doi.org/10.2514/6.2014-2788
[research_akyurtlu_akyurtlu_1991]: https://ntrs.nasa.gov/citations/19910012808
[research_alam_sharma_2019]: https://doi.org/10.2139/ssrn.3351634
[research_alam_sharma_2019_b]: https://doi.org/10.2139/ssrn.3355295
[research_albertson_emami_2001]: https://ntrs.nasa.gov/citations/20010061808
[research_aleemuddin_hossain_2026]: https://doi.org/10.3390/aerospace13070573
[research_alexander_tm_1978]: https://doi.org/10.21236/ada063655
[research_algarni_sahin_1996]: https://doi.org/10.1243/pime_proc_1996_210_340_02
[research_alghamdi_alghamdi_2016]: https://doi.org/10.1615/computthermalscien.2016016226
[research_ali_sadrulislam_2004]: https://doi.org/10.1016/j.icheatmasstransfer.2004.08.016
[research_alipourbonab_yazdaniasrami_2025]: https://doi.org/10.1016/j.fuel.2024.133323
[research_all_a_2019]: https://doi.org/10.12968/s0013-7758(23)90658-6
[research_allard_2024]: https://doi.org/10.1038/s41578-024-00748-0
[research_allen_1957]: https://doi.org/10.2514/8.12486
[research_allen_2021]: https://doi.org/10.1088/2058-7058/34/07/06
[research_allen_byrne_1965]: https://doi.org/10.2514/3.3041
[research_allen_maughan_1994]: https://doi.org/10.2514/6.1994-3145
[research_allenhj_1966]: https://ntrs.nasa.gov/citations/19660045863
[research_allenjl_bekeandrew_1953]: https://ntrs.nasa.gov/citations/19930087574
[research_allenjr_1991]: https://doi.org/10.2514/6.1991-227
[research_almeida_navarromartinez_2019]: https://doi.org/10.1007/s10494-019-00055-7
[research_alspach_webb_2018]: https://doi.org/10.2514/6.2018-4025
[research_altenhofer_sander_2018]: https://doi.org/10.1007/s00193-018-0808-2
[research_amandachou_ericcmarineau_2024]: https://ntrs.nasa.gov/citations/20240005810
[research_amatucci_addy_1982]: https://doi.org/10.2514/3.7977
[research_ambeverma_muraripandey_2021]: https://doi.org/10.1016/j.energy.2020.119511
[research_amruthapreethi_ramanujachari_2020]: https://doi.org/10.4273/ijvss.11.5.05
[research_amundsen_leonard_2004]: https://ntrs.nasa.gov/citations/20040111308
[research_an_investigation_2024]: https://doi.org/10.47176/jame.43.2.1063
[research_an_sun_2020]: https://doi.org/10.1016/j.ast.2020.106180
[research_an_sun_2023]: https://doi.org/10.2514/1.j062504
[research_an_sun_2024]: https://doi.org/10.1063/5.0185024
[research_an_wang_2021]: https://doi.org/10.1016/j.ast.2021.106951
[research_an_wu_2018]: https://doi.org/10.1016/j.jfranklin.2018.04.035
[research_an_xia_2019]: https://doi.org/10.1016/j.isatra.2019.05.023
[research_analysis_of_2023]: https://doi.org/10.56042/ijems.v30i2.1461
[research_anbuselvan_menezes_2010]: https://doi.org/10.1260/1759-3107.1.1.59
[research_andersjbjr_1975]: https://ntrs.nasa.gov/citations/19750006919
[research_anderson_1986]: https://doi.org/10.2514/3.48409
[research_anderson_1987]: https://ntrs.nasa.gov/citations/19870058118
[research_anderson_brooks_1960]: https://doi.org/10.2514/8.8371
[research_anderson_eckbreth_1991]: https://doi.org/10.1016/s0082-0784(06)80470-4
[research_andersonbernhardh_weirlois_2014]: https://ntrs.nasa.gov/citations/20140016538
[research_andersoncharlesw_1993]: https://ntrs.nasa.gov/citations/19930065836
[research_andersongriffiny_benczedanielp_1987]: https://ntrs.nasa.gov/citations/19880023142
[research_andersongy_reagonpg_1977]: https://ntrs.nasa.gov/citations/19770021180
[research_andreadis_drake_2002]: https://ntrs.nasa.gov/citations/20030068741
[research_andrews_1978]: https://ntrs.nasa.gov/citations/19780048423
[research_andrews_davis_1992]: https://doi.org/10.1016/0094-5765(92)90153-a
[research_andrews_mackley_1976]: https://ntrs.nasa.gov/citations/19760016176
[research_andrews_mackley_1993]: https://ntrs.nasa.gov/citations/19930066106
[research_andrews_mackley_1994]: https://ntrs.nasa.gov/citations/19950006447
[research_andrianatos_2020]: https://doi.org/10.14264/uql.2020.628
[research_anfimov_1993]: https://doi.org/10.2514/6.1993-5000
[research_anon_2018]: https://doi.org/10.18520/cs/v114/i08/1596-1596
[research_anthony_dukes_1975]: https://ntrs.nasa.gov/citations/19750008479
[research_appel_oehring_2003]: https://doi.org/10.1002/3527602119.ch4
[research_aprovitola_iuspa_2019]: https://doi.org/10.1155/2019/6069528
[research_arad_michaels_2021]: https://doi.org/10.2514/6.2021-4177
[research_arad_yokev_2020]: https://doi.org/10.2514/6.2020-2966
[research_archer_1963]: https://doi.org/10.21236/ad0431737
[research_ardema_1972]: https://ntrs.nasa.gov/citations/19720011261
[research_ardemamarkd_1995]: https://ntrs.nasa.gov/citations/19960000793
[research_arguchintseva_1999]: https://doi.org/10.1016/s1474-6670(17)57385-1
[research_arjun_2010]: https://doi.org/10.14741/ijcet/spl.2.2014.85
[research_armstrong_nicholls_1967]: https://doi.org/10.21236/ad0654055
[research_arora_srivastava_2025]: https://doi.org/10.1007/s42401-025-00405-6
[research_arrington_woods_1972]: https://ntrs.nasa.gov/citations/19720015257
[research_ashok_joseph_2023]: https://doi.org/10.61653/joast.v65i2.2013.722
[research_aslan_bisard_1990]: https://ntrs.nasa.gov/citations/19910000728
[research_aso_hayashi_1990]: https://doi.org/10.2322/jjsass1969.38.178
[research_assad_pisarev_2026]: https://doi.org/10.1016/j.ast.2025.110889
[research_atanacio_2000]: https://doi.org/10.21236/ada377656
[research_atci_jeyakumar_2024]: https://doi.org/10.1177/14680874241295358
[research_athithan_jeyakumar_2022]: https://doi.org/10.1177/14680874221107137
[research_augustjamesa_joshishiv_1996]: https://ntrs.nasa.gov/citations/19960047659
[research_auslender_suder_2009]: https://ntrs.nasa.gov/citations/20090037583
[research_austin_2024]: https://doi.org/10.14264/105958
[research_autonomous_space_1988]: https://ntrs.nasa.gov/citations/19930074538
[research_ayers_athmanathan_2023]: https://doi.org/10.2514/1.b38868
[research_azevedo_liu_1990]: https://doi.org/10.2514/3.10486
[research_azhar_habeeb_2022]: https://doi.org/10.4273/ijvss.14.7.21
[research_aziz_chowdhury_2022]: https://doi.org/10.1177/14680874221100499
[research_babinsky_2014]: https://doi.org/10.21236/ada602774
[research_baccarella_liu_2016]: https://doi.org/10.1088/0957-0233/27/4/045902
[research_baccarella_liu_2020]: https://doi.org/10.2514/6.2020-1611
[research_baccarella_liu_2021]: https://doi.org/10.1017/jfm.2021.238
[research_baccarella_samuels_2025]: https://doi.org/10.2514/1.t7019
[research_back_cuffel_1972]: https://doi.org/10.2514/3.61705
[research_bacos_1993]: https://doi.org/10.1051/jp4:19937303
[research_bade_1975]: https://ntrs.nasa.gov/citations/19750057648
[research_baganoff_1990]: https://doi.org/10.21236/ada222704
[research_bahm_baumann_2005]: https://ntrs.nasa.gov/citations/20050182778
[research_baier_friess_2024]: https://doi.org/10.1007/s12567-024-00562-y
[research_bajpai_jagadeesh_2023]: https://doi.org/10.2514/6.2023-3096
[research_baker_kramer_1982]: https://doi.org/10.21236/ada114013
[research_bakos_2024]: https://doi.org/10.14264/366376
[research_bakos_chinitz_1995]: https://doi.org/10.2514/6.1995-6148
[research_bakos_morgan_1994]: https://doi.org/10.2514/6.1994-2520
[research_bakosrj_morganrg_1993]: https://ntrs.nasa.gov/citations/19940019040
[research_balaji_venkatasubbaiah_2025]: https://doi.org/10.1016/j.euromechflu.2025.204290
[research_balakalyani_jagadeesh_2019]: https://doi.org/10.1016/j.measurement.2018.12.099
[research_balakrishnan_williams_1994]: https://doi.org/10.2514/3.23754
[research_balakumar_chou_2018]: https://doi.org/10.2514/1.j056040
[research_balakumar_kegerise_2016]: https://doi.org/10.2514/1.j054632
[research_balboni_atler_1993]: https://doi.org/10.2514/6.1993-2786
[research_ball_chan_1999]: https://doi.org/10.1115/imece1999-0518
[research_ball_ross_1972]: https://doi.org/10.2514/3.59042
[research_ballwh_lyonfj_1966]: https://ntrs.nasa.gov/citations/19660053460
[research_banagiri_raj_2025]: https://doi.org/10.1115/1.4069506
[research_bandyopadhyay_gadelhak_1994]: https://doi.org/10.21236/ada637054
[research_bangertlh_santmandm_1980]: https://ntrs.nasa.gov/citations/19810009475
[research_bangertlh_santmandm_1980_b]: https://ntrs.nasa.gov/citations/19800061564
[research_bao_qin_2009]: https://doi.org/10.1016/j.ijhydene.2009.06.006
[research_bao_wang_2021]: https://doi.org/10.1016/j.cja.2020.11.009
[research_bao_wang_2023]: https://doi.org/10.1109/taes.2022.3230633
[research_baranyshyn_kuzmitski_2024]: https://doi.org/10.3390/fire7020043
[research_barber_cox_1989]: https://doi.org/10.2514/3.23181
[research_barber_heitt_2006]: https://doi.org/10.2514/6.2006-123
[research_barbie_mahanjr_1989]: https://ntrs.nasa.gov/citations/19890040959
[research_barnett_1963]: https://doi.org/10.21236/ad0410262
[research_baron_efrat_1979]: https://doi.org/10.21236/ada068819
[research_barone_nicholson_2022]: https://doi.org/10.1103/physrevfluids.7.084604
[research_barpande_singh_2021]: https://doi.org/10.1016/j.matpr.2020.09.703
[research_barre_braud_1997]: https://doi.org/10.1016/s0894-1777(96)00102-1
[research_barrier_coating_1990]: https://doi.org/10.1016/0010-4361(90)90306-h
[research_barry_1971]: https://doi.org/10.2514/3.44269
[research_barth_2014]: https://doi.org/10.14264/uql.2014.614
[research_barth_wheatley_2014]: https://doi.org/10.2514/6.2014-1159
[research_barthelemy_1989]: https://doi.org/10.1109/62.31806
[research_barthelemy_1989_b]: https://doi.org/10.2514/6.1989-5053
[research_barthelemy_1991]: https://doi.org/10.4271/911969
[research_bartolottapaula_krausedavidl_2000]: https://ntrs.nasa.gov/citations/20050192387
[research_bas_2026]: https://doi.org/10.54287/gujsa.1810054
[research_baskaya_hickel_2025]: https://doi.org/10.1063/5.0281627
[research_batdor_1957]: https://doi.org/10.2514/8.12490
[research_bathel_2024]: https://ntrs.nasa.gov/citations/20240008140
[research_bathel_jones_2019]: https://ntrs.nasa.gov/citations/20200002424
[research_battellememorialinstcolumbusoh_1947]: https://doi.org/10.21236/ad0210300
[research_battertonpg_arpasidj_1974]: https://ntrs.nasa.gov/citations/19740025659
[research_battertonpg_arpasidj_1976]: https://ntrs.nasa.gov/citations/19760024067
[research_baughn_hoffman_1987]: https://doi.org/10.1115/1.3248064
[research_baumann_2006]: https://ntrs.nasa.gov/citations/20060047627
[research_baumann_2007]: https://ntrs.nasa.gov/citations/20070003597
[research_baumann_bahm_2008]: https://ntrs.nasa.gov/citations/20080006640
[research_baumann_bisbee_2003]: https://doi.org/10.1109/naecon.1988.195203
[research_baumann_pahle_2008]: https://ntrs.nasa.gov/citations/20080033978
[research_baumbickrj_1974]: https://ntrs.nasa.gov/citations/19740008381
[research_baumgart_yao_2025]: https://doi.org/10.1016/j.proci.2025.105798
[research_baurle_2004]: https://ntrs.nasa.gov/citations/20040035566
[research_baurle_white_2022]: https://ntrs.nasa.gov/citations/20220004274
[research_baurlera_axdahlel_2017]: https://ntrs.nasa.gov/citations/20180000520
[research_baurleroberta_middletontroyf_2012]: https://ntrs.nasa.gov/citations/20130000726
[research_baydarezgihan_lufrankk_2016]: https://ntrs.nasa.gov/citations/20170000948
[research_baydarezgihan_lufrankk_2017]: https://ntrs.nasa.gov/citations/20170001419
[research_baysalo_1992]: https://ntrs.nasa.gov/citations/19930065534
[research_beachhljr_1976]: https://ntrs.nasa.gov/citations/19770003430
[research_beachy_bae_2021]: https://doi.org/10.1007/s00158-021-03005-y
[research_beaurainandre_souchieralain_2003]: https://ntrs.nasa.gov/citations/20030066115
[research_beck_eitelberg_1998]: https://doi.org/10.2514/6.1998-2770
[research_beckwith_1975]: https://doi.org/10.2514/3.49695
[research_beddoes_2018]: https://doi.org/10.22215/etd/1993-02393
[research_bedick_ferguson_2019]: https://doi.org/10.2514/1.b37309
[research_behera_chakraborty_2023]: https://doi.org/10.61653/joast.v58i2.2006.701
[research_behrenbrinker_guo_2025]: https://doi.org/10.2514/6.2025-3478
[research_beichel_obrien_1978]: https://doi.org/10.2514/6.1978-974
[research_beint_friedmannp_1993]: https://ntrs.nasa.gov/citations/19930053431
[research_bejan_2013]: https://doi.org/10.21236/ada590232
[research_bekey_1994]: https://ntrs.nasa.gov/citations/19950036755
[research_bellan_2017]: https://doi.org/10.1016/j.combustflame.2016.09.026
[research_benard_gaillard_1997]: https://doi.org/10.1007/s003480050050
[research_benhamida_basem_2025]: https://doi.org/10.1063/5.0272099
[research_benoit_1967]: https://doi.org/10.21236/ad0652194
[research_benson_maslowe_1966]: https://doi.org/10.2514/3.28665
[research_bentley_2009]: https://doi.org/10.1007/978-0-387-76510-5_9
[research_berens_bissinger_1996]: https://doi.org/10.2514/6.1996-4531
[research_berens_bissinger_1998]: https://doi.org/10.2514/3.26994
[research_berger_white_2024]: https://doi.org/10.1007/s00348-024-03909-7
[research_berglund_fureby_2007]: https://doi.org/10.1016/j.proci.2006.07.074
[research_bermudez_gladden_2003]: https://doi.org/10.2514/6.2003-7074
[research_berry_1991]: https://doi.org/10.2514/3.20623
[research_berry_auslender_2000]: https://ntrs.nasa.gov/citations/20000080347
[research_berry_daryabeigi_2008]: https://ntrs.nasa.gov/citations/20080023459
[research_berryscotta_bergerkarent_2016]: https://ntrs.nasa.gov/citations/20160010109
[research_berryscotta_horvaththomasjjr_2008]: https://ntrs.nasa.gov/citations/20080023461
[research_berryscotta_kimmelroger_2011]: https://ntrs.nasa.gov/citations/20110013235
[research_bert_1989]: https://doi.org/10.2514/3.45772
[research_bertelrud_kolodziej_1992]: https://ntrs.nasa.gov/citations/19930029263
[research_berton_surdon_1995]: https://doi.org/10.2514/6.1995-6132
[research_bertrand_huchette_2025]: https://doi.org/10.1016/j.engfracmech.2025.111570
[research_besserer_1952]: https://doi.org/10.21236/ad0036272
[research_bhadouriya_2024]: https://doi.org/10.22214/ijraset.2024.58089
[research_bhagwandin_sahu_2023]: https://doi.org/10.21236/ad1216596
[research_bhatbn_mcphersonwb_1993]: https://ntrs.nasa.gov/citations/19930066322
[research_bhattrai_debaar_2018]: https://doi.org/10.1016/j.ast.2018.06.036
[research_billig_1967]: https://ntrs.nasa.gov/citations/19670024055
[research_billig_1995]: https://doi.org/10.2514/3.23952
[research_bilsborough_neilsenburke_2025]: https://doi.org/10.1016/j.compositesb.2025.112906
[research_biltgen_lafleur_2004]: https://doi.org/10.2514/6.2004-3729
[research_birdrkeith_hoffmanerick_1998]: https://ntrs.nasa.gov/citations/19980201176
[research_birnbaum_1989]: https://doi.org/10.21236/ada208210
[research_bissinger_blagoveshchensky_1998]: https://doi.org/10.1016/s1270-9638(99)80009-1
[research_blanksonisaiahm_hagsethpaul_1993]: https://ntrs.nasa.gov/citations/19930041536
[research_boatrightwb_sabolap_1976]: https://ntrs.nasa.gov/citations/19760035766
[research_bodansanderspatricia_bouviercarl_1998]: https://ntrs.nasa.gov/citations/19980069722
[research_boeing_to_2005]: https://doi.org/10.1108/aeat.2005.12777baf.006
[research_boeingscientificresearchlabsseattlewa_1963]: https://doi.org/10.21236/ad0414555
[research_bogdanoff_edwards_1995]: https://ntrs.nasa.gov/citations/20020034914
[research_bogdanoff_wilson_1996]: https://ntrs.nasa.gov/citations/20020034854
[research_bogdanoff_wilson_1997]: https://doi.org/10.2514/2.193
[research_bogdonoff_1968]: https://doi.org/10.2514/6.1968-5
[research_bogdonoff_1970]: https://doi.org/10.21236/ad0708757
[research_bogdonoff_1999]: https://doi.org/10.21236/ada370547
[research_bogue_erbland_1993]: https://ntrs.nasa.gov/citations/19940008783
[research_boiocchi_galfetti_2018]: https://doi.org/10.2514/1.b36307
[research_bolender_doman_2005]: https://doi.org/10.21236/ada444974
[research_boles_milligan_2013]: https://doi.org/10.21236/ada586382
[research_bolz_1979]: https://ntrs.nasa.gov/citations/19790016131
[research_bonanni_norris_2024]: https://doi.org/10.1016/j.proci.2024.105690
[research_bond_1958]: https://doi.org/10.2514/8.7284
[research_bonnefond_falempin_1996]: https://doi.org/10.2514/6.1996-4490
[research_borovoy_mosharov_2017]: https://doi.org/10.1051/eucass/201609025
[research_borrelli_pandolfi_1991]: https://doi.org/10.1007/978-3-642-76527-8_50
[research_boscagli_rigas_2026]: https://doi.org/10.1017/jfm.2026.11548
[research_botelho_martinez_2022]: https://doi.org/10.1007/s12567-022-00423-6
[research_bouchard_chambers_1966]: https://doi.org/10.21236/ad0632234
[research_bowcutt_2001]: https://doi.org/10.2514/2.5893
[research_bowersox_fan_2000]: https://doi.org/10.21236/ada384726
[research_bowman_foy_1961]: https://doi.org/10.21236/ad0267505
[research_bowman_hanson_1990]: https://doi.org/10.21236/ada221793
[research_bowman_hanson_1991]: https://doi.org/10.21236/ada236759
[research_bowman_hanson_1992]: https://doi.org/10.21236/ada251065
[research_boyce_gerard_2003]: https://doi.org/10.2514/6.2003-7029
[research_boyce_paull_2001]: https://doi.org/10.2514/6.2001-1891
[research_boyd_2002]: https://doi.org/10.21236/ada414031
[research_boyd_2008]: https://doi.org/10.21236/ada573606
[research_boyd_padilla_2003]: https://doi.org/10.2514/6.2003-7062
[research_boydiaind_1989]: https://ntrs.nasa.gov/citations/19900003182
[research_boydiaind_1990]: https://ntrs.nasa.gov/citations/19900032651
[research_boyer_1965]: https://doi.org/10.21236/ad0621447
[research_boylan_1965]: https://doi.org/10.21236/ad0460154
[research_bozkurt_avsar_2025]: https://doi.org/10.1007/s40964-025-01160-y
[research_brabbstheodorea_lezbergerwina_1987]: https://ntrs.nasa.gov/citations/19870019195
[research_bracco_homan_1978]: https://doi.org/10.21236/ada064560
[research_bradford_olds_1999]: https://doi.org/10.2514/6.1999-2104
[research_bradleymwheaton_ivettaleyva]: https://ntrs.nasa.gov/citations/20250010917
[research_brahmachary_fujio_2022]: https://doi.org/10.1063/5.0080272
[research_brahmachary_ogawa_2021]: https://doi.org/10.2514/1.b38383
[research_brasseur_1994]: https://doi.org/10.21236/ada278392
[research_bray_1963]: https://doi.org/10.1016/s0082-0784(63)80085-5
[research_brenneis_wanie_1991]: https://doi.org/10.2514/6.1991-2472
[research_brescianini_2023]: https://doi.org/10.14264/3a9190d
[research_brescianini_morgan_1992]: https://doi.org/10.2514/6.1992-3965
[research_bretherton_2021]: https://doi.org/10.14264/64f3ccb
[research_brevault_balesdent_2017]: https://doi.org/10.1177/1063293x17737131
[research_brewergd_morrisre_1975]: https://ntrs.nasa.gov/citations/19750009264
[research_brociek_hetmaniok_2023]: https://doi.org/10.1016/j.applthermaleng.2022.119405
[research_brodsky_1970]: https://doi.org/10.21236/ad0716026
[research_brown_donbar_2013]: https://doi.org/10.21236/ada578570
[research_brown_donbar_2015]: https://doi.org/10.21236/ada613800
[research_brown_wierzbanowski_1992]: https://doi.org/10.21236/ada266071
[research_brown_williams_2010]: https://doi.org/10.21236/ada522512
[research_brune_2020]: https://ntrs.nasa.gov/citations/20200002798
[research_brune_bruce_2019]: https://doi.org/10.2514/1.t5490
[research_brune_hosder_2015]: https://doi.org/10.2514/1.j053053
[research_brune_hosder_2017]: https://doi.org/10.2514/1.a33732
[research_bruneaj_bruceweiii_2017]: https://ntrs.nasa.gov/citations/20180000701
[research_brunner_1959]: https://doi.org/10.1115/1.4008191
[research_brunnhofer_sirbiparagina_2006]: https://doi.org/10.2514/6.2006-4563
[research_bruno_2023]: https://doi.org/10.1007/978-981-19-7927-9_1
[research_bruno_2023_b]: https://doi.org/10.1007/978-981-19-7927-9_7
[research_bruno_2023_c]: https://doi.org/10.1007/978-981-19-7927-9
[research_bruno_2023_d]: https://doi.org/10.1007/978-981-19-7927-9_4
[research_bruno_ingenito_2021]: https://doi.org/10.3390/en14123690
[research_bryan_1955]: https://doi.org/10.21236/ad0079996
[research_bryce_reese_1969]: https://doi.org/10.2514/6.1969-457
[research_bu_lei_2018]: https://doi.org/10.1007/s11071-018-4447-z
[research_buchanan_little_1993]: https://doi.org/10.1016/0010-938x(93)90344-g
[research_buchmannoa_1978]: https://ntrs.nasa.gov/citations/19790013255
[research_buehlerrd_lore_1981]: https://ntrs.nasa.gov/citations/19810018656
[research_bui_2025]: https://doi.org/10.14264/3d7b8ad
[research_builder_1964]: https://doi.org/10.2514/6.1964-243
[research_bulirsch_chudej_1991]: https://doi.org/10.2514/6.1991-2656
[research_bulman_siebenhaar_1995]: https://doi.org/10.2514/6.1995-2475
[research_bulmanmj_stoutpw_1997]: https://ntrs.nasa.gov/citations/19990080047
[research_buning_wong_2000]: https://ntrs.nasa.gov/citations/20000091005
[research_burchfield_bontrager_1966]: https://doi.org/10.21236/ad0481634
[research_burgers_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000689
[research_burke_rezzag_2026]: https://doi.org/10.1007/s00193-026-01263-7
[research_burnett_czysz_1963]: https://doi.org/10.21236/ad0408988
[research_burrows_kurkov_1971]: https://doi.org/10.2514/6.1971-721
[research_burrows_rana_2024]: https://doi.org/10.2514/6.2024-2861
[research_burton_witherspoon_1990]: https://ntrs.nasa.gov/citations/19910014975
[research_busakm_mcdanieljc_2012]: https://ntrs.nasa.gov/citations/20130001729
[research_busakristin_ellisonerikn_2013]: https://ntrs.nasa.gov/citations/20130004498
[research_buschekharald_caliseanthonyj_1993]: https://ntrs.nasa.gov/citations/19930067360
[research_bush_tiwari_1996]: https://doi.org/10.2514/6.1996-2279
[research_bushnelldennism_yiplongp_1993]: https://ntrs.nasa.gov/citations/19930022543
[research_bussingtra_murmanem_1983]: https://ntrs.nasa.gov/citations/19830035487
[research_butler_1967]: https://doi.org/10.1063/1.1762264
[research_butler_moore_1992]: https://doi.org/10.2514/6.1992-5068
[research_butrica_2003]: https://doi.org/10.1353/book.20644
[research_buzukov_1999]: https://doi.org/10.1007/bf02674532
[research_byrom_allen_1994]: https://doi.org/10.1080/01495739408946270
[research_byun_kim_2026]: https://doi.org/10.1016/j.ast.2026.112144
[research_cabell_rock_2003]: https://ntrs.nasa.gov/citations/20030057128
[research_cabellkaren_hassneal_2011]: https://ntrs.nasa.gov/citations/20110011173
[research_cady_kendle_1971]: https://doi.org/10.2514/6.1971-645
[research_cady_kendle_1972]: https://doi.org/10.2514/6.1972-1133
[research_cai_chen_2023]: https://doi.org/10.1016/j.energy.2023.128161
[research_cai_chen_2024]: https://doi.org/10.1016/j.energy.2024.130358
[research_cai_huang_2022]: https://doi.org/10.3389/fenrg.2022.884624
[research_cai_liu_2016]: https://doi.org/10.1016/j.actaastro.2016.05.010
[research_cai_zheng_2023]: https://doi.org/10.1016/j.applthermaleng.2023.120227
[research_cai_zheng_2024]: https://doi.org/10.1016/j.energy.2024.131748
[research_cai_zhou_2017]: https://doi.org/10.1016/j.actaastro.2017.10.013
[research_cain_walton_2003]: https://doi.org/10.2514/6.2003-7030
[research_californiainstoftechpasadena_1990]: https://doi.org/10.21236/ada229217
[research_calise_flandro_1988]: https://ntrs.nasa.gov/citations/19890003167
[research_caliseaj_flandroga_1990]: https://ntrs.nasa.gov/citations/19900009959
[research_calloway_1983]: https://ntrs.nasa.gov/citations/19840002070
[research_calspanubresearchcenterbuffalony_1990]: https://doi.org/10.21236/ada338839
[research_calvignacjacky_danglisa_2003]: https://ntrs.nasa.gov/citations/20030067582
[research_camarda_masek_1979]: https://ntrs.nasa.gov/citations/19800031074
[research_camarda_murrow_1990]: https://doi.org/10.4271/902008
[research_camardacharlesj_murrowharoldn_1990]: https://ntrs.nasa.gov/citations/19910035185
[research_campbell_gerstenmaier_2014]: https://ntrs.nasa.gov/citations/20140005659
[research_campbellcharlesh_kingrudolpha_2010]: https://ntrs.nasa.gov/citations/20100003360
[research_candler_leyva_2022]: https://doi.org/10.1080/08929882.2022.2145777
[research_candler_nompelis_2006]: https://doi.org/10.21236/ada470282
[research_candler_park_1988]: https://ntrs.nasa.gov/citations/19880057368
[research_candon_ogawa_2015]: https://doi.org/10.2514/6.2015-1106
[research_candon_ogawa_2018]: https://doi.org/10.1016/j.actaastro.2018.04.012
[research_cantulucaml_galloemanuelaca_2015]: https://ntrs.nasa.gov/citations/20160005909
[research_cao_brod_2021]: https://doi.org/10.1016/j.combustflame.2021.111562
[research_cao_chang_2015]: https://doi.org/10.1016/j.ast.2014.11.001
[research_cao_lu_2020]: https://doi.org/10.1016/j.ast.2019.105590
[research_cao_yu_2021]: https://doi.org/10.1134/s0869864321040120
[research_cao_zhou_2026]: https://doi.org/10.1016/j.energy.2026.142437
[research_caponefrancisj_schirmeralbertow_1993]: https://ntrs.nasa.gov/citations/19940006220
[research_cappucciogelsomina_1999]: https://ntrs.nasa.gov/citations/20000044623
[research_capra_leyland_2004]: https://doi.org/10.2514/6.2004-1298
[research_carbajosa_sanzandres_2025]: https://doi.org/10.1016/j.actaastro.2025.05.006
[research_carbon_fiber_1971]: https://doi.org/10.1016/0010-4361(71)90969-4
[research_cardullo_1965]: https://doi.org/10.2514/3.28134
[research_carlincm_frischi_2003]: https://ntrs.nasa.gov/citations/20030065839
[research_carlsonjohnr_abdolhamidkhaleds_1993]: https://ntrs.nasa.gov/citations/19930057050
[research_carman_jb_1966]: https://doi.org/10.21236/ad0632514
[research_carney_1964]: https://doi.org/10.1007/978-1-4757-0525-6_64
[research_carpenter_graves_1967]: https://doi.org/10.2514/6.1967-182
[research_carpenterjljr_stuhrkewf_1976]: https://ntrs.nasa.gov/citations/19760018287
[research_carrier_fendell_1995]: https://doi.org/10.1016/0010-2180(95)00099-2
[research_carsongtjr_1974]: https://ntrs.nasa.gov/citations/19750002123
[research_carsongtjr_middenre_1976]: https://ntrs.nasa.gov/citations/19770004126
[research_carter_2012]: https://doi.org/10.21236/ada563331
[research_cary_hefner_1970]: https://doi.org/10.2514/3.6062
[research_casali_gamma_2001]: https://doi.org/10.2514/6.2001-826
[research_caseyr_stalkerrj_1990]: https://ntrs.nasa.gov/citations/19910004338
[research_casseau_espinoza_2016]: https://doi.org/10.3390/aerospace3040045
[research_casseau_palharini_2016]: https://doi.org/10.3390/aerospace3040034
[research_cassetti_1978]: https://doi.org/10.1108/eb035480
[research_cavolowsky_loomis_1995]: https://ntrs.nasa.gov/citations/20020038413
[research_cavolowsky_newfield_1992]: https://ntrs.nasa.gov/citations/19930038361
[research_cavolowskyjohna_loomismarkp_1995]: https://ntrs.nasa.gov/citations/20020038030
[research_cazin_1989]: https://doi.org/10.2514/6.1989-5020
[research_celik_demirezen_2024]: https://doi.org/10.1109/access.2024.3359417
[research_cenkci_1991]: https://doi.org/10.21236/ada241143
[research_cerminara_2023]: https://doi.org/10.1007/s10494-023-00403-8
[research_cerminara_deiterding_2020]: https://doi.org/10.1016/j.ijheatfluidflow.2020.108732
[research_cerminara_nayak_2025]: https://doi.org/10.1063/5.0253164
[research_chakravarthy_randive_2021]: https://doi.org/10.1016/j.actaastro.2021.07.022
[research_chakravarthy_randive_2022]: https://doi.org/10.1016/j.actaastro.2022.04.036
[research_chakravarthy_thecomputationalfluiddynamicsdepartment_1990]: https://doi.org/10.1016/0956-0521(90)90027-i
[research_chambersjr_2007]: https://doi.org/10.21236/ada463441
[research_chan_1990]: https://doi.org/10.1007/bf02646064
[research_chan_1992]: https://doi.org/10.1007/bf02801167
[research_chan_razzaqi_2018]: https://doi.org/10.2514/1.b36652
[research_chan_whitside_2021]: https://doi.org/10.1007/s00193-021-01002-0
[research_chaneysteve_1999]: https://ntrs.nasa.gov/citations/20000044624
[research_chang_bai_2022]: https://doi.org/10.1016/j.ijhydene.2022.01.026
[research_chang_bass_1993]: https://ntrs.nasa.gov/citations/19930008904
[research_chang_cao_2014]: https://doi.org/10.4172/2168-9792.1000130
[research_chang_chan_2020]: https://doi.org/10.1016/j.ast.2020.105856
[research_chang_gu_2005]: https://doi.org/10.2514/6.2005-3315
[research_chang_hsu_1960]: https://doi.org/10.2514/8.5121
[research_chang_huang_2022]: https://doi.org/10.3390/aerospace10010001
[research_chang_li_2017]: https://doi.org/10.1016/j.paerosci.2016.12.001
[research_chang_tiernan_1986]: https://doi.org/10.21236/ada187197
[research_chang_yuan_2022]: https://doi.org/10.1080/00102202.2022.2086000
[research_changbao_hui_2020]: https://doi.org/10.1088/1757-899x/751/1/012078
[research_chao_jeng_1965]: https://doi.org/10.1115/1.3689076
[research_chapter_9_2013]: https://doi.org/10.1615/978-1-56700-309-3.183
[research_chaput_1989]: https://doi.org/10.2514/6.1989-5018
[research_chase_1990]: https://doi.org/10.2514/6.1990-2706
[research_chase_1991]: https://doi.org/10.2514/6.1991-2389
[research_chase_1991_b]: https://doi.org/10.2514/6.1991-2388
[research_chase_1992]: https://doi.org/10.2514/6.1992-3141
[research_chase_tang_1995]: https://doi.org/10.2514/6.1995-6031
[research_chaudhury_zhao_1992]: https://doi.org/10.21236/ada268321
[research_chazot_panerai_2015]: https://doi.org/10.2514/5.9781624103292.0329.0342
[research_cheah_bhattacharjee_2025]: https://doi.org/10.2514/1.g008331
[research_chelliah_krauss_1994]: https://doi.org/10.2514/6.1994-2577
[research_chen_1969]: https://doi.org/10.2514/3.29720
[research_chen_1993]: https://ntrs.nasa.gov/citations/19930041520
[research_chen_2023]: https://doi.org/10.13168/cs.2023.0026
[research_chen_chen_2022]: https://doi.org/10.1063/5.0113570
[research_chen_chen_2023]: https://doi.org/10.1063/5.0146348
[research_chen_fan_2020]: https://doi.org/10.1016/j.actaastro.2019.10.047
[research_chen_fan_2021]: https://doi.org/10.1016/j.jppr.2021.11.002
[research_chen_fan_2025]: https://doi.org/10.26599/tst.2024.9010018
[research_chen_guo_2023]: https://doi.org/10.1063/5.0176245
[research_chen_he_2025]: https://doi.org/10.1016/j.ast.2025.110086
[research_chen_he_2025_b]: https://doi.org/10.1177/16878132251348391
[research_chen_he_2025_c]: https://doi.org/10.4236/jilsa.2025.171003
[research_chen_hu_2017]: https://doi.org/10.1002/rnc.3923
[research_chen_li_2020]: https://doi.org/10.1016/j.applthermaleng.2019.114637
[research_chen_li_2022]: https://doi.org/10.1016/j.eswa.2022.116609
[research_chen_mao_2026]: https://doi.org/10.1063/5.0335632
[research_chen_sethuraman_2025]: https://doi.org/10.1016/j.ast.2025.110262
[research_chen_sethuraman_2026]: https://doi.org/10.1016/j.ast.2025.111260
[research_chen_si_2023]: https://doi.org/10.1016/j.ijhydene.2023.03.190
[research_chen_starkey_2009]: https://doi.org/10.21236/ada590178
[research_chen_wang_2020]: https://doi.org/10.1016/j.ceramint.2020.06.180
[research_chen_wang_2026]: https://doi.org/10.1016/j.applthermaleng.2025.129525
[research_chen_xiao_2017]: https://doi.org/10.1080/14685248.2017.1333615
[research_chen_xu_2018]: https://doi.org/10.1155/2018/6051924
[research_chen_xu_2021]: https://doi.org/10.2514/1.j059846
[research_chen_yang_2024]: https://doi.org/10.1063/5.0221364
[research_chen_yang_2025]: https://doi.org/10.34133/space.0260
[research_chen_zhang_2018]: https://doi.org/10.1016/j.compstruct.2018.04.004
[research_chen_zhang_2024]: https://doi.org/10.1063/5.0218003
[research_chen_zhao_2017]: https://doi.org/10.2514/6.2017-2271
[research_chen_zhao_2019]: https://doi.org/10.1155/2019/8384639
[research_chen_zhou_2020]: https://doi.org/10.1007/978-981-15-8901-0_10
[research_chen_zhu_2017]: https://doi.org/10.1017/jfm.2017.233
[research_chen_zou_2022]: https://doi.org/10.1016/j.applthermaleng.2021.117742
[research_cheng_1960]: https://doi.org/10.21236/ad0243140
[research_cheng_1989]: https://doi.org/10.1016/0360-1285(89)90008-7
[research_cheng_chen_2023]: https://doi.org/10.3390/aerospace10100857
[research_cheng_gong_2017]: https://doi.org/10.2514/6.2017-2366
[research_cheng_jing_2021]: https://doi.org/10.1016/j.ast.2021.106965
[research_cheng_wehrmeyer_1994]: https://doi.org/10.1016/0010-2180(94)90087-6
[research_cheng_xu_2022]: https://doi.org/10.2139/ssrn.4019929
[research_chernyi_1961]: https://doi.org/10.1016/b978-1-4832-3197-6.50011-3
[research_chimarodrickv_connerstimothyr_2009]: https://ntrs.nasa.gov/citations/20100041304
[research_chimarodrickv_connerstimothyr_2010]: https://ntrs.nasa.gov/citations/20100024366
[research_chinitz_erdos_1994]: https://doi.org/10.2514/3.23705
[research_chinnappan_kim_2026]: https://doi.org/10.1007/s00162-026-00786-0
[research_chinnaraj_kim_2024]: https://doi.org/10.3390/ma17215229
[research_chitsomboon_1992]: https://ntrs.nasa.gov/citations/19920016579
[research_chitsomboon_northam_1991]: https://doi.org/10.2514/3.23292
[research_chitsomboont_northamgb_1988]: https://ntrs.nasa.gov/citations/19880065924
[research_cho_ha_1996]: https://doi.org/10.1016/0008-6223(96)00016-4
[research_choi_driscoll_2021]: https://doi.org/10.2514/6.2021-4097
[research_choi_driscoll_2023]: https://doi.org/10.2514/1.b38931
[research_choi_driscoll_2024]: https://doi.org/10.2514/1.b39553
[research_choubey_gaud_2022]: https://doi.org/10.1016/j.fuel.2021.122847
[research_choubey_pandey_2017]: https://doi.org/10.1016/j.ijhydene.2017.04.024
[research_choubey_pandey_2018]: https://doi.org/10.1016/j.actaastro.2018.01.034
[research_choubey_panging_2027]: https://doi.org/10.1016/j.fuel.2026.140782
[research_choubey_solanki_2023]: https://doi.org/10.1016/j.fuel.2023.128972
[research_choubey_tiwari_2022]: https://doi.org/10.1016/b978-0-323-99565-8.00002-1
[research_choubey_tiwari_2022_b]: https://doi.org/10.1016/b978-0-323-99565-8.00006-9
[research_choubey_tiwari_2022_c]: https://doi.org/10.1016/b978-0-323-99565-8.00005-7
[research_choudhari_tokugawa_2012]: https://ntrs.nasa.gov/citations/20120012434
[research_choudhary_daschakladar_2021]: https://doi.org/10.1016/j.compstruct.2020.113274
[research_choulynnchen_machkervynd_1995]: https://ntrs.nasa.gov/citations/19960047303
[research_chowdhary_hoang_2022]: https://doi.org/10.1016/j.cma.2022.115396
[research_christol_1993]: https://doi.org/10.1016/0265-9646(93)90007-v
[research_christophe_1992]: https://doi.org/10.2514/6.1992-5007
[research_chu_1967]: https://doi.org/10.1016/0016-0032(67)90237-2
[research_chu_thompson_1992]: https://doi.org/10.1016/0956-7151(92)90393-s
[research_chu_tu_2026]: https://doi.org/10.3390/pr14081315
[research_chudej_1996]: https://doi.org/10.1007/978-3-322-82967-2_4
[research_chun_burr_1969]: https://doi.org/10.2514/3.44056
[research_chung_kim_1994]: https://doi.org/10.1007/bf02944707
[research_chung_kim_1995]: https://doi.org/10.2514/3.26575
[research_chung_lu_1995]: https://doi.org/10.2514/3.23863
[research_chunks_lockerj_1994]: https://ntrs.nasa.gov/citations/19940022070
[research_cikanek_bartolotta_2007]: https://ntrs.nasa.gov/citations/20070032055
[research_clapp_hunter_1993]: https://doi.org/10.2514/6.1993-2285
[research_clarey_greendyke_2018]: https://doi.org/10.2514/6.2018-0744
[research_clark_1969]: https://doi.org/10.2514/3.5359
[research_clark_wallace_1992]: https://ntrs.nasa.gov/citations/19930003269
[research_clark_wallace_1994]: https://ntrs.nasa.gov/citations/19940000148
[research_clauser_1954]: https://doi.org/10.2514/8.6460
[research_clauss_sontgen_1994]: https://doi.org/10.1615/intjenergeticmaterialschemprop.v3.i1-6.140
[research_clemens_2010]: https://doi.org/10.21236/ada525600
[research_cockrell_engelund_2000]: https://ntrs.nasa.gov/citations/20000091003
[research_cockrellcharlesedwardjr_1994]: https://ntrs.nasa.gov/citations/19940029612
[research_cockrellcharlesejr_1994]: https://ntrs.nasa.gov/citations/19950037643
[research_cockrellcharlesejr_auslenderaaronh_2002]: https://ntrs.nasa.gov/citations/20030000444
[research_cockrelljr_huebner_1991]: https://doi.org/10.2514/6.1991-3209
[research_cohen_reshotko_1956]: https://ntrs.nasa.gov/citations/19930091005
[research_cohenzur_natan_1998]: https://doi.org/10.2514/2.5379
[research_cole_florance_1993]: https://ntrs.nasa.gov/citations/19930049938
[research_colegaryl_richardjacquesc_1991]: https://ntrs.nasa.gov/citations/19920006775
[research_colladay_1987]: https://ntrs.nasa.gov/citations/19870063099
[research_collier_1992]: https://doi.org/10.2514/6.1992-5015
[research_colwell_2023]: https://doi.org/10.1615/ihpc1990v1.500
[research_colwell_modlin_1992]: https://doi.org/10.2514/3.387
[research_combustion_scaling_2012]: https://doi.org/10.2514/6.2012-5811
[research_compressive_deformation_1996]: https://doi.org/10.1016/s0026-0657(96)93028-3
[research_comptonhr_schiessjr_1983]: https://ntrs.nasa.gov/citations/19840002068
[research_computational_analysis_1985]: https://ntrs.nasa.gov/citations/19850007751
[research_computational_fluid_1997]: https://ntrs.nasa.gov/citations/20050177084
[research_conchie_1989]: https://doi.org/10.2514/6.1989-5021
[research_connorle_sparksvw_1971]: https://ntrs.nasa.gov/citations/19730013103
[research_constantine_wang_2011]: https://doi.org/10.2514/6.2011-2037
[research_control_system_1976]: https://doi.org/10.1016/0010-4485(76)90126-3
[research_cook_dwyer_1966]: https://doi.org/10.1007/978-1-4757-0522-5_22
[research_coras_paull_2006]: https://doi.org/10.2514/6.2006-7981
[research_corbanje_caliseaj_1991]: https://ntrs.nasa.gov/citations/19920035988
[research_corpening_2004]: https://ntrs.nasa.gov/citations/20060046909
[research_corpening_vanwie_1991]: https://doi.org/10.2514/6.1991-551
[research_corringtonlc_henningsg_1956]: https://ntrs.nasa.gov/citations/19650003106
[research_coupling_study_2023]: https://doi.org/10.1063/5.0154900
[research_cousin_1967]: https://doi.org/10.2514/6.1967-451
[research_couture_dechamplain_2008]: https://doi.org/10.2514/6.2008-5171
[research_covellpeterf_woodrichardm_1988]: https://ntrs.nasa.gov/citations/19880064748
[research_covert_1984]: https://doi.org/10.2514/6.1984-611
[research_cowgillgr_johnsonwr_1971]: https://ntrs.nasa.gov/citations/19710012082
[research_cox_crabtree_1966]: https://doi.org/10.1063/1.3048343
[research_craig_saric_2016]: https://doi.org/10.1017/jfm.2016.643
[research_creating_hypersonic_2019]: https://doi.org/10.2514/5.9781624105142.0829.0836
[research_cresci_1966]: https://doi.org/10.21236/ad0633949
[research_crivellari_de_1999]: https://doi.org/10.2514/6.1999-2243
[research_crmcclinton_vlrausch_2001]: https://ntrs.nasa.gov/citations/20010021138
[research_crocker_mcenaney_1991]: https://doi.org/10.1016/0008-6223(91)90163-d
[research_crow_boyd_2012]: https://doi.org/10.2514/6.2012-2751
[research_crown_1950]: https://doi.org/10.21236/ad0062509
[research_cruden_tang_2021]: https://doi.org/10.1007/s00348-021-03227-2
[research_crystallographic_and_2009]: https://doi.org/10.1201/noe1439801482.ch11
[research_cubbage_monta_1991]: https://ntrs.nasa.gov/citations/19910007677
[research_cuda_gaffney_2008]: https://ntrs.nasa.gov/citations/20080020459
[research_cuda_hass_2010]: https://ntrs.nasa.gov/citations/20100002217
[research_cui_mei_2018]: https://doi.org/10.1016/j.applthermaleng.2018.02.038
[research_cui_wang_2015]: https://doi.org/10.2514/1.j053378
[research_cui_xu_2018]: https://doi.org/10.1016/j.actaastro.2017.10.034
[research_cui_zhang_2024]: https://doi.org/10.1088/1742-6596/2707/1/012112
[research_cui_zhao_2017]: https://doi.org/10.1016/j.applthermaleng.2017.06.113
[research_cui_zhen_2025]: https://doi.org/10.1002/rnc.8012
[research_cunningham_1987]: https://doi.org/10.2514/3.25879
[research_cunnington_robinson_1990]: https://ntrs.nasa.gov/citations/19900051383
[research_cuppoletti_ombrello_2019]: https://doi.org/10.1016/j.proci.2018.08.005
[research_cuppoletti_ombrello_2020]: https://doi.org/10.1016/j.combustflame.2020.01.030
[research_curran_2017]: https://doi.org/10.14264/uql.2017.184
[research_curran_2021]: https://doi.org/10.14264/91e395c
[research_curran_craig_1973]: https://doi.org/10.21236/ad0769481
[research_curran_swithenbank_1966]: https://doi.org/10.1108/eb034117
[research_curranet_beachhljr_1988]: https://ntrs.nasa.gov/citations/19890026132
[research_current_state_of_the_art_1974]: https://doi.org/10.2514/5.9781600865077.0227.0247
[research_cutler_1998]: https://doi.org/10.2514/6.1998-710
[research_cutler_1998_b]: https://doi.org/10.2514/2.500
[research_cwanderson_charlesrmcclinton_1990]: https://ntrs.nasa.gov/citations/19910064039
[research_czysz_1963]: https://doi.org/10.21236/ad0410539
[research_czysz_1963_b]: https://doi.org/10.21236/ad0408922
[research_daghigh_daghigh_2025]: https://doi.org/10.1111/ijac.70085
[research_dagkolu_gokdag_2021]: https://doi.org/10.1016/j.promfg.2021.07.037
[research_dai_cai_2026]: https://doi.org/10.3390/aerospace13030283
[research_dai_huang_2021]: https://doi.org/10.1016/j.actaastro.2020.09.028
[research_dai_shao_2025]: https://doi.org/10.1063/5.0305837
[research_dai_zhao_2023]: https://doi.org/10.2514/1.t6675
[research_daines_segal_1998]: https://doi.org/10.2514/2.5352
[research_daly_2025]: https://doi.org/10.14264/62de2c0
[research_danberg_1961]: https://doi.org/10.21236/ad0439624
[research_daney_1968]: https://doi.org/10.6028/nbs.tn.364
[research_daney_sindt_1968]: https://ntrs.nasa.gov/citations/19680054072
[research_daniel_mee_1995]: https://doi.org/10.1016/0045-7949(94)00309-q
[research_darrelrtenney_wbarrylisagor_1989]: https://ntrs.nasa.gov/citations/19900025960
[research_dary_mpollock_1996]: https://doi.org/10.1016/0921-5093(95)10049-0
[research_daryabeigikamran_blossermaxl_2006]: https://ntrs.nasa.gov/citations/20060022542
[research_das_2000]: https://ntrs.nasa.gov/citations/20000116208
[research_das_debnath_2025]: https://doi.org/10.1007/s40997-025-00895-x
[research_das_pandey_2021]: https://doi.org/10.1016/j.matpr.2020.12.1035
[research_dashs_delguidicep_1978]: https://ntrs.nasa.gov/citations/19780017412
[research_dashsm_sinhan_1986]: https://ntrs.nasa.gov/citations/19860057999
[research_dasilva_decastrodasilva_2026]: https://doi.org/10.1016/j.actaastro.2026.01.059
[research_dasilva_deshaies_1994]: https://doi.org/10.1016/s0082-0784(06)80624-7
[research_daub_willems_2022]: https://doi.org/10.1016/j.jsv.2021.116714
[research_davideglass_bryanakubitschek]: https://ntrs.nasa.gov/citations/20230012520
[research_davidson_1996]: https://doi.org/10.7449/1996/superalloys_1996_545_553
[research_davidson_2026]: https://doi.org/10.1080/14685248.2026.2665148
[research_davidson_lallman_1999]: https://ntrs.nasa.gov/citations/20040086945
[research_davis_1964]: https://doi.org/10.21236/ad0601998
[research_davis_1970]: https://doi.org/10.21236/ad0705129
[research_davis_1995]: https://doi.org/10.2514/6.1995-2716
[research_davis_2007]: https://ntrs.nasa.gov/citations/20070039002
[research_davis_harvey_1981]: https://doi.org/10.21236/ada101185
[research_davis_murrow_1989]: https://ntrs.nasa.gov/citations/19890063965
[research_davis_sim_2006]: https://ntrs.nasa.gov/citations/20060022150
[research_davis_white_2006]: https://ntrs.nasa.gov/citations/20090009773
[research_davis_white_2008]: https://ntrs.nasa.gov/citations/20080021260
[research_davisdavido_2015]: https://ntrs.nasa.gov/citations/20150022184
[research_davisgw_plankpp_1970]: https://ntrs.nasa.gov/citations/19700017938
[research_davison_1963]: https://doi.org/10.2514/6.1963-1802
[research_dayton_1993]: https://doi.org/10.2514/6.1993-2564
[research_deangelis_anderson_1992]: https://ntrs.nasa.gov/citations/19920024958
[research_debarber_1999]: https://doi.org/10.21236/ada388803
[research_debnath_pandey_2015]: https://doi.org/10.4028/www.scientific.net/amm.772.136
[research_debnath_roy_2023]: https://doi.org/10.1007/s42979-023-02020-8
[research_debonisjr_yungsters_1996]: https://ntrs.nasa.gov/citations/19960033187
[research_deep_jagadeesh_2021]: https://doi.org/10.2514/1.t6016
[research_deerekarena_asburyscottc_1996]: https://ntrs.nasa.gov/citations/19960020543
[research_deerekarena_asburyscottc_1999]: https://ntrs.nasa.gov/citations/19990052644
[research_defensescienceboardwashingtondc_1988]: https://doi.org/10.21236/ada201124
[research_defensescienceboardwashingtondc_1992]: https://doi.org/10.21236/ada274530
[research_deformation_of_1998]: https://doi.org/10.1016/s0026-0657(99)80118-0
[research_degregori_ferlauto_2018]: https://doi.org/10.1063/1.5048596
[research_degregori_ferlauto_2018_b]: https://doi.org/10.2514/6.2018-1143
[research_deiwert_cavalowsky_1994]: https://doi.org/10.2514/6.1994-2519
[research_deiwertgeorges_1997]: https://ntrs.nasa.gov/citations/19970026372
[research_delage_saiz_2022]: https://doi.org/10.1016/j.jeurceramsoc.2022.01.060
[research_delcorsojosepha_cheatwoodfmcneil_2011]: https://ntrs.nasa.gov/citations/20110012051
[research_demangejeffreyj_taylorshawnc_2014]: https://ntrs.nasa.gov/citations/20150000141
[research_demarchipoltronieri_moreira_2025]: https://doi.org/10.26678/abcm.cobem2023.cob2023-0144
[research_demoura_ribeiro_2026]: https://doi.org/10.1007/s42401-026-00510-0
[research_dempers_nikbin_1999]: https://doi.org/10.4028/www.scientific.net/kem.171-174.153
[research_denardo_1994]: https://doi.org/10.4271/941200
[research_denenberg_1986]: https://doi.org/10.1108/eb047633
[research_deng_jin_2017]: https://doi.org/10.1007/s12206-017-0121-5
[research_deng_jin_2017_b]: https://doi.org/10.1016/j.ijheatmasstransfer.2016.10.004
[research_deng_kim_2015]: https://doi.org/10.6108/kspe.2015.19.5.031
[research_deng_kim_2017]: https://doi.org/10.1007/s12206-017-1025-0
[research_deng_li_2016]: https://doi.org/10.1016/j.compstruct.2016.01.020
[research_deng_wang_2025]: https://doi.org/10.1016/j.tsep.2025.104290
[research_deng_ying_2026]: https://doi.org/10.1016/j.jeurceramsoc.2026.118587
[research_denman_2018]: https://doi.org/10.14264/uql.2018.8
[research_desai_brahmachary_2019]: https://doi.org/10.1061/(asce)as.1943-5525.0001085
[research_design_construction_and_2008]: https://doi.org/10.5139/jksas.2008.36.4.328
[research_despirito_2015]: https://doi.org/10.2514/1.a32974
[research_destefanofumo_sciti_2025]: https://doi.org/10.14339/sto-avt-384-2
[research_development_of_1962]: https://doi.org/10.2514/5.9781600864810.0701.0758
[research_dewangan_parwani_2026]: https://doi.org/10.1080/01457632.2026.2642431
[research_dewell_speyer_1993]: https://doi.org/10.2514/6.1993-3753
[research_dewey_1961]: https://doi.org/10.2514/8.5900
[research_dewitt_hardy_1989]: https://ntrs.nasa.gov/citations/19900004952
[research_dhanasar_ferguson_2019]: https://doi.org/10.5772/intechopen.85697
[research_dharavath_manna_2015]: https://doi.org/10.1016/j.actaastro.2015.08.014
[research_diao_liu_2025]: https://doi.org/10.1016/j.ijthermalsci.2024.109457
[research_dicaprio_acanfora_2019]: https://doi.org/10.3390/aerospace6060071
[research_dickeson_rodriguez_2009]: https://doi.org/10.2514/6.2009-6281
[research_dicristina_1979]: https://doi.org/10.21236/ada065645
[research_diegopcapriotti]: https://ntrs.nasa.gov/citations/20205010450
[research_dietrick_2013]: https://doi.org/10.21236/ad1018856
[research_digiovanni_stemmer_2019]: https://doi.org/10.2514/1.a34488
[research_digiovanni_stemmer_2019_b]: https://doi.org/10.2514/1.a34404
[research_dillonjl_marcumdcjr_1980]: https://ntrs.nasa.gov/citations/19800034112
[research_ding_chen_2022]: https://doi.org/10.1063/5.0108757
[research_ding_liu_2015]: https://doi.org/10.1016/j.actaastro.2015.02.016
[research_ding_liu_2021]: https://doi.org/10.1016/j.actaastro.2021.09.018
[research_ding_liu_2025]: https://doi.org/10.1016/j.actaastro.2024.09.070
[research_ding_yue_2022]: https://doi.org/10.1016/j.cja.2021.10.037
[research_direct_measurements_1994]: https://doi.org/10.2514/6.1994-585
[research_direct_numerical_2017]: https://doi.org/10.15372/pmtf20170508
[research_direct_numerical_2018]: https://doi.org/10.15372/pmtf20180103
[research_direct_numerical_2023]: https://doi.org/10.1063/5.0146651
[research_diskin_jachimowski_1987]: https://ntrs.nasa.gov/citations/19880016184
[research_diskin_northam_1986]: https://ntrs.nasa.gov/citations/19860037959
[research_diskinglenns_northamgburton_1987]: https://ntrs.nasa.gov/citations/19870058170
[research_diskinglenns_northamgburton_1988]: https://ntrs.nasa.gov/citations/19890026140
[research_dissel_kothari_2006]: https://doi.org/10.2514/1.17916
[research_disturbance_rejection_2016]: https://doi.org/10.1201/b16570-28
[research_dixonsc_1985]: https://ntrs.nasa.gov/citations/19850017057
[research_dixonsc_tenneydr_1985]: https://ntrs.nasa.gov/citations/19860003881
[research_doggettrobertvjr_rickettsrodneyh_1991]: https://ntrs.nasa.gov/citations/19910017813
[research_doherty_2015]: https://doi.org/10.14264/uql.2014.382
[research_doherty_2022]: https://doi.org/10.14264/30640a6
[research_doherty_smart_2012]: https://doi.org/10.2514/6.2012-5910
[research_doherty_smart_2014]: https://doi.org/10.2514/6.2014-2930
[research_doherty_smart_2015]: https://doi.org/10.2514/6.2015-3523
[research_doherty_smart_2015_b]: https://doi.org/10.2514/1.j053785
[research_dolvin_2009]: https://doi.org/10.2514/6.2009-7228
[research_dong_cai_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000727
[research_dong_cui_2020]: https://doi.org/10.1016/j.energy.2020.117463
[research_dong_liu_2019]: https://doi.org/10.1016/j.cja.2018.12.004
[research_dong_sun_2019]: https://doi.org/10.1016/j.actaastro.2019.07.016
[research_dong_tang_2018]: https://doi.org/10.1016/j.applthermaleng.2017.12.002
[research_dongre_2024]: https://doi.org/10.53555/e2ha7809
[research_donohue_marinelli_1992]: https://doi.org/10.2514/6.1992-2869
[research_donohuejamesm_2012]: https://ntrs.nasa.gov/citations/20140005746
[research_doozandeh_jindal_2025]: https://doi.org/10.3390/ma18133196
[research_dorrington_1990]: https://doi.org/10.1016/0094-5765(90)90004-5
[research_dorrington_1999]: https://doi.org/10.2514/6.1999-2625
[research_dossantos_passaro_2025]: https://doi.org/10.1016/j.tsep.2024.103172
[research_dou_yang_2022]: https://doi.org/10.1016/j.actaastro.2022.07.016
[research_dougherty_1975]: https://doi.org/10.2514/3.7045
[research_dress_boyden_1994]: https://doi.org/10.2514/3.46536
[research_driscoll_stoddard_2015]: https://doi.org/10.2514/1.j053027
[research_drozda_baurle_2016]: https://ntrs.nasa.gov/citations/20160009131
[research_drtenney_wblisagor_1988]: https://ntrs.nasa.gov/citations/19890026171
[research_drummond_1979]: https://doi.org/10.2514/6.1979-1482
[research_drummond_bouchez_2006]: https://ntrs.nasa.gov/citations/20060020216
[research_drummond_carpenter_1989]: https://ntrs.nasa.gov/citations/19900057355
[research_drummond_carpenter_1991]: https://ntrs.nasa.gov/citations/19920063809
[research_drummond_mukunda_1988]: https://ntrs.nasa.gov/citations/19880063557
[research_drummond_weidner_1981]: https://doi.org/10.2514/6.1981-186
[research_drummondjp_1991]: https://ntrs.nasa.gov/citations/19910059432
[research_drummondjphilip_1997]: https://ntrs.nasa.gov/citations/20040110377
[research_drummondjphilip_carpentermarkh_1989]: https://ntrs.nasa.gov/citations/19890059717
[research_drummondjphilip_diskinglenns_2006]: https://ntrs.nasa.gov/citations/20060020221
[research_dryermurray_bekeandrew_1952]: https://ntrs.nasa.gov/citations/19930087106
[research_dsouza_molder_1971]: https://doi.org/10.2514/6.1971-85
[research_du_chen_2025]: https://doi.org/10.1016/j.combustflame.2025.114142
[research_du_chen_2025_b]: https://doi.org/10.1016/j.actaastro.2025.08.033
[research_du_chong_2026]: https://doi.org/10.1016/j.ast.2026.113143
[research_du_qin_2025]: https://doi.org/10.1007/s42423-025-00187-1
[research_dual_mode_combustion_2022]: https://doi.org/10.1002/9781119640646.ch7
[research_duan_li_2015]: https://doi.org/10.1109/taes.2014.120654
[research_duan_zhao_2026]: https://doi.org/10.2514/1.j066092
[research_dube_slifka_1991]: https://ntrs.nasa.gov/citations/19930064593
[research_dudebout_sislian_1998]: https://doi.org/10.2514/2.5368
[research_dudzinski_2018]: https://doi.org/10.22215/etd/1997-03772
[research_dufrene_2015]: https://doi.org/10.2514/6.2015-2017
[research_dunavant_mulligan_1969]: https://ntrs.nasa.gov/citations/19690065599
[research_duncanbeverly_1991]: https://ntrs.nasa.gov/citations/19910057030
[research_dunlap_1969]: https://doi.org/10.2514/3.44103
[research_dunlap_kuethe_1961]: https://doi.org/10.21236/ad0256234
[research_dunn_1969]: https://doi.org/10.2514/3.5431
[research_dunn_malik_2021]: https://doi.org/10.1016/j.fuel.2021.121128
[research_duparcq_hermant_1993]: https://doi.org/10.1016/0094-5765(93)90068-8
[research_dupont_muscat_1999]: https://doi.org/10.1023/a:1009979903970
[research_dwivedi_bradley_2010]: https://doi.org/10.21236/ada544560
[research_dwoyerdouglasl_1987]: https://ntrs.nasa.gov/citations/19890029132
[research_dynamic_testing_2011]: https://ntrs.nasa.gov/citations/20110023756
[research_eamesdjh_masonml_1988]: https://ntrs.nasa.gov/citations/19880057494
[research_earlhandrewsjr_marvingtorrence_1985]: https://ntrs.nasa.gov/citations/19850008574
[research_echeverriaaparicio_fishpool_2022]: https://doi.org/10.1016/j.jeurceramsoc.2021.12.059
[research_economosc_1966]: https://ntrs.nasa.gov/citations/19660037118
[research_edelman_2022]: https://ntrs.nasa.gov/citations/20210024275
[research_edelman_2024]: https://ntrs.nasa.gov/citations/20240008352
[research_edelman_spadaccini_1969]: https://doi.org/10.2514/6.1969-456
[research_edelman_spadaccini_1969_b]: https://doi.org/10.2514/6.1969-338
[research_edmonds_omoth_1964]: https://doi.org/10.2514/6.1964-1233
[research_edquistkarlt_2006]: https://ntrs.nasa.gov/citations/20060047743
[research_edwards_1991]: https://doi.org/10.2514/3.46000
[research_edwards_1992]: https://ntrs.nasa.gov/citations/19930030123
[research_edwards_steffens_2015]: https://doi.org/10.2514/6.2015-4678
[research_edwardsclw_smallwj_1975]: https://ntrs.nasa.gov/citations/19750034212
[research_edwardsta_1992]: https://ntrs.nasa.gov/citations/19930038304
[research_edwardsthomasalan_1988]: https://ntrs.nasa.gov/citations/19890008229
[research_effects_of_1993]: https://doi.org/10.2514/6.1993-609
[research_effects_of_2019]: https://doi.org/10.15372/fgv20190612
[research_effects_of_2023]: https://doi.org/10.1063/5.0149813
[research_eggers_reagon_1978]: https://ntrs.nasa.gov/citations/19780015150
[research_ehrburger_baranne_1986]: https://doi.org/10.1016/0008-6223(86)90274-5
[research_eidelman_sharov_2000]: https://doi.org/10.21236/ada405510
[research_elderdj_1975]: https://ntrs.nasa.gov/citations/19760009061
[research_elizabethfrieken_scottaberry_2020]: https://ntrs.nasa.gov/citations/20200003493
[research_elkebir_ornik_2020]: https://doi.org/10.2514/6.2020-2412
[research_elkhoury_hickey_2026]: https://doi.org/10.1016/j.ast.2026.113130
[research_elkowitz_wanchek_2024]: https://doi.org/10.1364/ao.507587
[research_ellis_1989]: https://doi.org/10.2514/6.1989-1406
[research_ellis_2025]: https://doi.org/10.2139/ssrn.5181173
[research_ellisonjc_johnsoncb_1964]: https://ntrs.nasa.gov/citations/19650001351
[research_ellsworth_2010]: https://ntrs.nasa.gov/citations/20100037123
[research_elmouazen_zhang_2026]: https://doi.org/10.1063/5.0312618
[research_elrod_1965]: https://doi.org/10.4271/650309
[research_elyagoubi_lamon_2015]: https://doi.org/10.1007/s11340-014-9976-x
[research_emami_trexler_1995]: https://ntrs.nasa.gov/citations/19950021922
[research_emanuel_1989]: https://ntrs.nasa.gov/citations/19890010775
[research_emanuel_1989_b]: https://doi.org/10.2514/6.1989-1878
[research_emory_terrapon_2011]: https://doi.org/10.2514/6.2011-2282
[research_engblom_frate_2005]: https://ntrs.nasa.gov/citations/20050182663
[research_engelund_2001]: https://doi.org/10.2514/2.3757
[research_engelund_holland_2000]: https://ntrs.nasa.gov/citations/20000092515
[research_engelund_neal_2013]: https://ntrs.nasa.gov/citations/20140008538
[research_engelundwalterc_hollandscottd_1999]: https://ntrs.nasa.gov/citations/20040086964
[research_epstein_1961]: https://doi.org/10.2514/8.9128
[research_erbland_1990]: https://doi.org/10.1117/12.24831
[research_erdman_2004]: https://doi.org/10.21236/ada422969
[research_erdos_erdos_1997]: https://doi.org/10.2514/6.1997-3014
[research_ericksonwd_klickgf_1970]: https://ntrs.nasa.gov/citations/19700014243
[research_escher_1992]: https://ntrs.nasa.gov/citations/19920071509
[research_escher_1999]: https://ntrs.nasa.gov/citations/19990062726
[research_escher_2001]: https://doi.org/10.2514/6.2001-3240
[research_escher_2002]: https://doi.org/10.2514/6.2002-3551
[research_escher_doughty_1986]: https://doi.org/10.2514/6.1986-1388
[research_escher_teeter_1986]: https://doi.org/10.2514/6.1986-1680
[research_eshtairy_millot_2025]: https://doi.org/10.1109/aero63441.2025.11068578
[research_espinosa_2003]: https://doi.org/10.2514/6.2003-4408
[research_eugenioribeiro_2026]: https://doi.org/10.70675/71fb3bbazace2z4d12z9c65z6f46972309c9
[research_eugenioribeiro_boukharfane_2020]: https://doi.org/10.1016/j.compfluid.2019.104344
[research_evaluation_of_2024]: https://doi.org/10.47176/jafm.17.3.2150
[research_evans_zok_2011]: https://doi.org/10.21236/ada552599
[research_experimental_hypersonic_2019]: https://doi.org/10.12968/s0261-2097(22)60721-4
[research_experimental_study_2022]: https://doi.org/10.47176/jafm.15.02.33220
[research_eyi_hanquist_2019]: https://doi.org/10.2514/1.t5523
[research_fabrication_of_1992]: https://doi.org/10.1016/0026-0657(92)91479-4
[research_fabrication_of_2000]: https://doi.org/10.1016/0026-0657(00)93426-x
[research_falempin_forrat_1992]: https://doi.org/10.2514/6.1992-5052
[research_falempin_serre_2006]: https://doi.org/10.2514/6.2006-5190
[research_falempin_thevenot_1995]: https://doi.org/10.2514/6.1995-6013
[research_fang_xianyao_2020]: https://doi.org/10.1088/1757-899x/887/1/012031
[research_fang_zeng_2026]: https://doi.org/10.1016/j.ast.2026.113019
[research_fasel_gross_2011]: https://doi.org/10.21236/ada563832
[research_fasel_keidel_2020]: https://doi.org/10.1016/j.mfglet.2019.12.004
[research_fasoulas_1996]: https://doi.org/10.2514/6.1996-2213
[research_fasoulas_messerschmid_1996]: https://doi.org/10.2514/6.1996-2275
[research_fay_kemp_1963]: https://doi.org/10.21236/ad0405723
[research_fedorova_2023]: https://doi.org/10.1134/s0010508223040020
[research_feie_kretz_2008]: https://doi.org/10.21236/ada488092
[research_feilden_glymond_2019]: https://doi.org/10.1016/j.ceramint.2019.05.032
[research_feldmanjay_stewartdavid_2019]: https://ntrs.nasa.gov/citations/20190030273
[research_feltrin_debona_2025]: https://doi.org/10.1016/j.jeurceramsoc.2024.117132
[research_feng_wang_2025]: https://doi.org/10.1016/j.ast.2025.110423
[research_fengyuan_guoping_2016]: https://doi.org/10.1515/tjj-2016-0063
[research_ferlemann_2005]: https://doi.org/10.2514/6.2005-3352
[research_ferlemann_mcclinton_2005]: https://ntrs.nasa.gov/citations/20050215122
[research_ferlemann_robinson_2000]: https://ntrs.nasa.gov/citations/20000061968
[research_ferlemannpaulg_2008]: https://ntrs.nasa.gov/citations/20080020517
[research_fernandezrene_trefnycharlesj_2001]: https://ntrs.nasa.gov/citations/20020006304
[research_ferrari_barbato_2016]: https://doi.org/10.1016/j.compstruct.2016.07.043
[research_ferreirademoura_borgesribeiro_2025]: https://doi.org/10.26678/abcm.cobem2025.cob2025-1480
[research_ferreirademoura_borgesribeiro_2025_b]: https://doi.org/10.26678/abcm.cobem2025.cob2025-0360
[research_ferreirademoura_borgesribeiro_2025_c]: https://doi.org/10.26678/abcm.cobem2025.cob2025-1507
[research_ferreirademoura_borgesribeiro_2025_d]: https://doi.org/10.26678/abcm.cobem2025.cob2025-0300
[research_ferretto_fusaro_2022]: https://doi.org/10.2514/6.2022-3381
[research_ferri_1973]: https://doi.org/10.1146/annurev.fl.05.010173.001505
[research_ferri_fox_1969]: https://doi.org/10.1016/s0082-0784(69)80488-1
[research_ferriantonio_nuccilouism_1946]: https://ntrs.nasa.gov/citations/19930093800
[research_ferriantonio_nuccilouism_1951]: https://ntrs.nasa.gov/citations/19930083137
[research_fesmire_2021]: https://ntrs.nasa.gov/citations/20210018293
[research_fields_richards_2004]: https://ntrs.nasa.gov/citations/20040031531
[research_fievisohn_yu_2017]: https://doi.org/10.2514/1.b36103
[research_fischer_hausrath_1966]: https://doi.org/10.4271/660679
[research_fischer_rock_1995]: https://ntrs.nasa.gov/citations/20040111299
[research_flahertyrj_stittle_1959]: https://ntrs.nasa.gov/citations/19650003082
[research_flandroga_roachrl_1992]: https://ntrs.nasa.gov/citations/19920024060
[research_fletcher_1967]: https://doi.org/10.1016/s0082-0784(67)80198-x
[research_fletcher_1988]: https://ntrs.nasa.gov/citations/19880045249
[research_fletcherdouglasg_2000]: https://ntrs.nasa.gov/citations/20000039706
[research_flexible_ceramic_2015]: https://doi.org/10.1016/s1350-4789(15)30250-6
[research_flightscienceslabincbuffalony_1964]: https://doi.org/10.21236/ad0442900
[research_flock_guelhan_2015]: https://doi.org/10.2514/6.2015-0108
[research_flock_gulhan_2015]: https://doi.org/10.2514/1.j053786
[research_flock_gulhan_2017]: https://doi.org/10.2514/1.b36602
[research_flock_gulhan_2019]: https://doi.org/10.2514/1.j057283
[research_flow_calibration_1982]: https://doi.org/10.1177/002029408201500401
[research_flow_dynamics_2025]: https://doi.org/10.46632/aae/3/2/2
[research_flow_field_reconstruction_2023]: https://doi.org/10.1063/5.0154979
[research_foelsche_beckel_2006]: https://doi.org/10.2514/6.2006-8119
[research_foelsche_rogers_2001]: https://ntrs.nasa.gov/citations/20010059583
[research_fogarty_1992]: https://doi.org/10.1177/002199839202600703
[research_fomichev_yadrenkin_2017]: https://doi.org/10.1134/s1063785017120057
[research_fontanmoura_2019]: https://doi.org/10.14264/uql.2019.413
[research_ford_1993]: https://doi.org/10.1108/eb037329
[research_foreman_1963]: https://doi.org/10.2514/6.1963-110
[research_forsythe_melfi_1961]: https://doi.org/10.21236/ad0672194
[research_fotia_2015]: https://doi.org/10.2514/1.b35171
[research_fotia_schauer_2016]: https://doi.org/10.2514/1.b35913
[research_fraiser_1960]: https://doi.org/10.2514/8.8575
[research_fratini_bernardini_2026]: https://doi.org/10.1017/jfm.2026.11973
[research_fratini_dellaposta_2025]: https://doi.org/10.1615/thmt-25.330
[research_freeman_powell_1980]: https://doi.org/10.2514/3.57743
[research_freeman_reubush_1997]: https://ntrs.nasa.gov/citations/19980018480
[research_freeman_stanley_1995]: https://doi.org/10.1016/0094-5765(95)00087-g
[research_freeman_talay_1996]: https://doi.org/10.1016/0094-5765(96)00051-3
[research_freitas_2020]: https://doi.org/10.1115/1.4047274
[research_frey_2014]: https://doi.org/10.21236/ada622072
[research_freydin_dowell_2021]: https://doi.org/10.2514/1.j060085
[research_froning_1988]: https://doi.org/10.1016/0094-5765(88)90168-3
[research_froning_2002]: https://doi.org/10.2514/6.2002-2252
[research_froning_gaubatz_1990]: https://ntrs.nasa.gov/citations/19910038263
[research_froning_roach_2003]: https://doi.org/10.2514/6.2003-6906
[research_froning_roach_2003_b]: https://doi.org/10.2514/6.2003-205
[research_froningjr_roach_1999]: https://doi.org/10.2514/6.1999-4878
[research_frost_2020]: https://doi.org/10.14264/uql.2020.593
[research_fu_hall_1993]: https://doi.org/10.1017/s0022112093000540
[research_fu_hall_1993_b]: https://doi.org/10.1098/rsta.1993.0025
[research_fu_song_2023]: https://doi.org/10.1016/j.energy.2022.126438
[research_fu_song_2024]: https://doi.org/10.1515/tjj-2024-0085
[research_fu_song_2026]: https://doi.org/10.3390/en19040993
[research_fu_wang_2015]: https://doi.org/10.1155/2015/293480
[research_fu_wang_2019]: https://doi.org/10.1109/access.2019.2947297
[research_fuehrer_1969]: https://doi.org/10.21236/ad0695562
[research_fuels_for_2022]: https://doi.org/10.1002/9781119640646.ch6
[research_fuhs_1966]: https://doi.org/10.2514/3.28433
[research_fujii_inoue_1998]: https://doi.org/10.2514/2.3409
[research_fujikawa_tsuchiya_2017]: https://doi.org/10.2322/tjsass.60.265
[research_fujimoto_1963]: https://doi.org/10.1246/bcsj.36.1233
[research_fujio_taguchi_2026]: https://doi.org/10.1007/s12567-026-00722-2
[research_fujiwara_1998]: https://doi.org/10.1016/s0360-3199(97)00082-7
[research_fureby_nilsson_2025]: https://doi.org/10.2514/1.j064432
[research_furey_1970]: https://doi.org/10.2514/6.1970-825
[research_furudate_lee_2005]: https://doi.org/10.2514/6.2005-3353
[research_fusaro_borgna_2025]: https://doi.org/10.1016/j.actaastro.2024.11.061
[research_fusaro_saccone_2024]: https://doi.org/10.1016/j.actaastro.2023.12.060
[research_future_perspectives_2004]: https://doi.org/10.2514/6.iac-04-v.4.09
[research_g_2020]: https://doi.org/10.22214/ijraset.2020.30549
[research_g_g_2025]: https://doi.org/10.1063/5.0262265
[research_gabb_gayda_1994]: https://ntrs.nasa.gov/citations/19940020704
[research_gabb_gayda_1996]: https://doi.org/10.1520/stp18233s
[research_gai_cao_2025]: https://doi.org/10.1063/5.0274336
[research_gaisl_mudfordnr_1992]: https://ntrs.nasa.gov/citations/19920074118
[research_gaitonde_2003]: https://doi.org/10.2514/6.2003-172
[research_gaitonde_lindsey_2006]: https://doi.org/10.1109/hpcmp-ugc.2006.18
[research_gallo_gnos_1966]: https://doi.org/10.2514/6.1966-606
[research_gamble_defrancesco_2005]: https://doi.org/10.2514/6.2005-3501
[research_gamma_titanium_aluminide_2021]: https://doi.org/10.4271/ams7023
[research_gao_2023]: https://doi.org/10.54254/2753-8818/11/20230391
[research_gao_ge_2025]: https://doi.org/10.1007/s44270-025-00015-9
[research_gao_gou_2021]: https://doi.org/10.1016/j.compstruct.2021.113962
[research_gao_he_2026]: https://doi.org/10.1063/5.0322431
[research_gao_ji_2025]: https://doi.org/10.1063/5.0297202
[research_gao_jiang_2017]: https://doi.org/10.1016/j.proci.2016.06.184
[research_gao_li_2015]: https://doi.org/10.1007/s11433-015-5710-7
[research_gao_lin_2015]: https://doi.org/10.1007/s12555-014-0169-2
[research_gao_liu_2026]: https://doi.org/10.2514/1.g009823
[research_gao_wang_2013]: https://doi.org/10.4028/www.scientific.net/amm.427-429.271
[research_gao_xi_2020]: https://doi.org/10.1515/tjj-2020-0038
[research_gao_zhang_2020]: https://doi.org/10.1051/matecconf/202031603002
[research_gao_zhang_2020_b]: https://doi.org/10.1088/1742-6596/1634/1/012157
[research_gao_zhang_2020_c]: https://doi.org/10.1088/1742-6596/1634/1/012159
[research_gao_zhao_1994]: https://doi.org/10.1115/imece1994-1300
[research_garberoglio_1969]: https://doi.org/10.2514/6.1969-330
[research_gardner_2024]: https://doi.org/10.14264/158612
[research_gardner_steelant_2004]: https://doi.org/10.2514/6.2004-3345
[research_gaspar_hackman_1991]: https://doi.org/10.21236/ada231906
[research_ge_zhu_2026]: https://doi.org/10.2514/1.j066541
[research_gee_little_1991]: https://doi.org/10.1007/bf00576792
[research_geerts_yu_2017]: https://doi.org/10.2514/1.j054991
[research_geiger_1963]: https://doi.org/10.21236/ad0409517
[research_gelderthomasf_1957]: https://ntrs.nasa.gov/citations/19930093764
[research_generale_kalidindi_2021]: https://doi.org/10.1016/j.compstruct.2021.114399
[research_geng_liu_2026]: https://doi.org/10.1016/j.ijthermalsci.2025.110577
[research_georgiadisnicholasj_mankbadiminar_2014]: https://ntrs.nasa.gov/citations/20150006760
[research_geraci_menhorn_2019]: https://doi.org/10.2514/6.2019-0725
[research_gerlinger_bruggemann_1994]: https://doi.org/10.1016/s0082-0784(06)80623-5
[research_gerlinger_simsont_2019]: https://doi.org/10.1016/j.actaastro.2019.04.042
[research_ghannadian_gosse_2024]: https://doi.org/10.1063/5.0226443
[research_ghenai_philippidis_2005]: https://doi.org/10.21236/ada443378
[research_ghioldi_piscaglia_2023]: https://doi.org/10.1016/j.compfluid.2023.106041
[research_ghonem_2000]: https://doi.org/10.21236/ada382904
[research_ghonem_osborne_1996]: https://doi.org/10.21236/ada326145
[research_ghori_narendar_2023]: https://doi.org/10.4028/p-oah3jt
[research_gibbons_damm_2021]: https://doi.org/10.2514/6.2021-4141
[research_gibbons_damm_2026]: https://doi.org/10.2514/1.t7072
[research_gibson_cancienne_2003]: https://doi.org/10.2514/6.2003-7086
[research_gibson_neidhoefer_2002]: https://doi.org/10.2514/6.2002-3462
[research_gidaspov_kononov_2019]: https://doi.org/10.34759/trd-2019-109-6
[research_gilbertmichael_rajuivatury_2009]: https://ntrs.nasa.gov/citations/20090015238
[research_gildfind_2024]: https://doi.org/10.1016/j.ast.2024.109621
[research_gildfind_jacobs_2017]: https://doi.org/10.1007/s00193-017-0786-9
[research_gildfind_morgan_2012]: https://doi.org/10.2514/6.2012-5954
[research_gildfind_morgan_2014]: https://doi.org/10.2514/1.j052383
[research_gildfind_morgan_2015]: https://doi.org/10.1007/s00193-015-0609-9
[research_gildfind_sancho_2015]: https://doi.org/10.1007/978-3-319-16835-7_58
[research_gilmore_1967]: https://doi.org/10.21236/ad0654054
[research_gimelshein_wysong_2019]: https://doi.org/10.2514/1.t5556
[research_ginoux_1966]: https://doi.org/10.21236/ad0647819
[research_ginter_cerreta_1962]: https://doi.org/10.4271/620331
[research_gion_1968]: https://doi.org/10.2514/6.1968-371
[research_giusti_sidey_2016]: https://doi.org/10.2514/6.2016-1681
[research_gladden_melis_1990]: https://ntrs.nasa.gov/citations/19900005195
[research_glaessgen_dawicke_2005]: https://ntrs.nasa.gov/citations/20050136675
[research_glass_2008]: https://doi.org/10.2514/6.2008-2682
[research_glass_capriotti_2013]: https://ntrs.nasa.gov/citations/20140001395
[research_glass_capriotti_2014]: https://ntrs.nasa.gov/citations/20150000555
[research_glass_glass_2002]: https://doi.org/10.2514/6.2002-5137
[research_glassman_nosek_1971]: https://doi.org/10.2514/6.1971-662
[research_glickstein_powell_1987]: https://doi.org/10.2514/6.1987-2003
[research_gnoffopetera_1993]: https://ntrs.nasa.gov/citations/19940008099
[research_goel_duraisamy_2018]: https://doi.org/10.2514/1.j055812
[research_goel_xie_2015]: https://doi.org/10.1109/acc.2015.7172208
[research_goff_wray_2026]: https://doi.org/10.58895/hysafe.46
[research_gokul_malaikannan_2025]: https://doi.org/10.1017/aer.2025.10023
[research_goldberg_scala_1965]: https://doi.org/10.21236/ad0623553
[research_goldfeld_nestoulia_2003]: https://doi.org/10.2514/6.2003-14
[research_goldman_1958]: https://doi.org/10.2514/8.7864
[research_goldstein_carter_1966]: https://doi.org/10.1016/0008-6223(66)90089-3
[research_golewski_sadowski_2019]: https://doi.org/10.1016/j.compstruct.2019.111489
[research_gollan_gollan_2011]: https://doi.org/10.2514/6.2011-2254
[research_golliard_mihaescu_2025]: https://doi.org/10.1007/s10494-025-00700-4
[research_golubkin_1978]: https://doi.org/10.1007/bf01091689
[research_golui_ranjith_2025]: https://doi.org/10.1016/j.applthermaleng.2025.127584
[research_gong_2005]: https://ntrs.nasa.gov/citations/20110014692
[research_gong_dong_2026]: https://doi.org/10.1016/j.ast.2025.111162
[research_gong_wang_2022]: https://doi.org/10.3390/sym14091862
[research_gooder_mall_1995]: https://doi.org/10.1016/0263-8223(95)00094-1
[research_goodrich_derry_1983]: https://ntrs.nasa.gov/citations/19840002082
[research_goodwin_maxwell_2017]: https://doi.org/10.2514/6.2017-4651
[research_gopal_wilson_2016]: https://doi.org/10.2514/6.2016-1166
[research_gopalasingam_rakhshani_2025]: https://doi.org/10.3390/hydrogen6040092
[research_gopinath_govindarajan_2022]: https://doi.org/10.1016/j.ijheatmasstransfer.2022.123060
[research_gopinath_jagadeesh_2019]: https://doi.org/10.1111/jace.16548
[research_gopinath_vignesh_2015]: https://doi.org/10.2514/6.2015-3558
[research_goracke_levack_1997]: https://doi.org/10.2514/2.3281
[research_goradiasuresh_torresabelo_1991]: https://ntrs.nasa.gov/citations/19920049066
[research_gorskii_olenicheva_2018]: https://doi.org/10.1134/s0018151x18020104
[research_goulard_1958]: https://doi.org/10.2514/8.7444
[research_goulos_otter_2021]: https://doi.org/10.1016/j.ast.2021.106533
[research_goyne_mcdaniel_2007]: https://doi.org/10.2514/1.24663
[research_goynechristopherp_mcdanieljamesc_2002]: https://ntrs.nasa.gov/citations/20030007792
[research_grabau_smithson_1964]: https://doi.org/10.21236/ad0601070
[research_grady_madzsar_1998]: https://doi.org/10.2514/6.1998-3773
[research_grainger_brieschenk_2014]: https://doi.org/10.2514/6.2014-3230
[research_grassofrancesco_gnoffopetera_1990]: https://ntrs.nasa.gov/citations/19910049570
[research_gray_mcloughlin_2024]: https://doi.org/10.1016/j.combustflame.2023.113250
[research_grayhr_1978]: https://ntrs.nasa.gov/citations/19780053166
[research_grayhr_nelsonhg_1975]: https://ntrs.nasa.gov/citations/19750018428
[research_gregorek_lee_1962]: https://doi.org/10.21236/ad0288297
[research_gregorek_reuss_1990]: https://ntrs.nasa.gov/citations/19910008854
[research_gregory_bowles_1994]: https://doi.org/10.4271/941168
[research_gregory_wilcox_1970]: https://doi.org/10.2514/6.1970-270
[research_gregory_williams_1971]: https://doi.org/10.2514/3.59163
[research_gregoryirenem_chowdhryrajivs_1992]: https://ntrs.nasa.gov/citations/19930003880
[research_gregoryirenem_chowdhryrajivs_1994]: https://ntrs.nasa.gov/citations/19950006425
[research_gregoryirenem_mcminnjohnd_1993]: https://ntrs.nasa.gov/citations/19940020622
[research_grenleski_billig_1968]: https://doi.org/10.2514/3.43951
[research_griffin_2018]: https://doi.org/10.22215/etd/1998-03924
[research_griffith_1958]: https://doi.org/10.2514/8.7258
[research_griffith_1989]: https://ntrs.nasa.gov/citations/19900005761
[research_griffith_lewis_1963]: https://doi.org/10.21236/ad0408568
[research_griffith_maus_1983]: https://ntrs.nasa.gov/citations/19840002063
[research_grimm_1992]: https://doi.org/10.1016/s1474-6670(17)49694-7
[research_grindle_2011]: https://ntrs.nasa.gov/citations/20110014424
[research_grindle_2012]: https://ntrs.nasa.gov/citations/20120016867
[research_grindle_bahm_2006]: https://ntrs.nasa.gov/citations/20060056098
[research_gronland_cambier_1997]: https://doi.org/10.2514/6.1997-3166
[research_ground_testing_2022]: https://doi.org/10.1002/9781119640646.ch11
[research_ground_testing_2023]: https://doi.org/10.12968/s1478-2774(23)50337-9
[research_groves_serrani_2005]: https://doi.org/10.21236/ada444973
[research_gruenig_mayinger_1999]: https://doi.org/10.1080/00102209908924205
[research_grunlan_rajagopal_2010]: https://doi.org/10.21236/ada546978
[research_gu_sun_2021]: https://doi.org/10.1016/j.applthermaleng.2021.117245
[research_gu_timmerhaus_1992]: https://doi.org/10.1016/0011-2275(92)90266-d
[research_guadagnini_dezaiacomo_2023]: https://doi.org/10.3390/aerospace11010035
[research_gugulothu_2020]: https://doi.org/10.1002/htj.21856
[research_guha_1994]: https://doi.org/10.1115/1.2910319
[research_gui_wang_2022]: https://doi.org/10.2514/1.j060930
[research_guizzo_2004]: https://doi.org/10.1109/mspec.2004.1317885
[research_guo_bi_2017]: https://doi.org/10.1016/j.applthermaleng.2017.05.038
[research_guo_cao_2026]: https://doi.org/10.1063/5.0340255
[research_guo_gao_2017]: https://doi.org/10.1007/978-3-319-46213-4_25
[research_guo_gao_2023]: https://doi.org/10.1021/acsomega.2c07582
[research_guo_lei_2025]: https://doi.org/10.1061/jaeeez.aseng-5809
[research_guo_luo_2020]: https://doi.org/10.3390/en13112911
[research_guo_pang_2022]: https://doi.org/10.3390/en15155332
[research_gupta_1987]: https://ntrs.nasa.gov/citations/19870055811
[research_gupta_2022]: https://doi.org/10.14264/923d57d
[research_gupta_ashokkumar_2022]: https://doi.org/10.1108/aeat-04-2020-0069
[research_gupta_jones_1992]: https://ntrs.nasa.gov/citations/19920022037
[research_gupta_lee_1990]: https://doi.org/10.2514/3.26122
[research_gupta_ramkumar_2015]: https://doi.org/10.12783/fae.2015.0401.02
[research_gupta_schwer_2018]: https://doi.org/10.2514/1.b36545
[research_gupta_sun_2009]: https://doi.org/10.21236/ada583075
[research_gupta_venuprasad_2018]: https://doi.org/10.1088/1757-899x/455/1/012027
[research_gursu_sheriff_1994]: https://doi.org/10.1016/0360-3199(94)90002-7
[research_guy]: https://doi.org/10.70675/dd4f8fdaz0c7bz420az9b17z69553809f0b0
[research_guy_mueller_1976]: https://ntrs.nasa.gov/citations/19770008102
[research_guy_torrence_1981]: https://ntrs.nasa.gov/citations/19810011555
[research_guyrw_mackleyea_1979]: https://ntrs.nasa.gov/citations/19790045400
[research_gwak_lee_2016]: https://doi.org/10.2514/1.b36020
[research_ha_yoon_2018]: https://doi.org/10.6108/kspe.2018.22.1.045
[research_haas_1963]: https://doi.org/10.21236/ad0404619
[research_haas_milos_1994]: https://ntrs.nasa.gov/citations/20010047000
[research_hagenmaier_boles_2013]: https://doi.org/10.21236/ada589252
[research_hagenmaier_eklund_2011]: https://doi.org/10.21236/ada543745
[research_haiman_karp_2026]: https://doi.org/10.2514/6.2026-2146
[research_haley_zhong_2023]: https://doi.org/10.1063/5.0137902
[research_hall_hildebrand_1964]: https://doi.org/10.21236/ada953011
[research_hall_ibasitas_2023]: https://doi.org/10.2514/6.2023-3464
[research_hall_poggie_2019]: https://doi.org/10.2514/6.2019-0946
[research_hallion_becker_1995]: https://doi.org/10.21236/ada302634
[research_hamaker_1996]: https://doi.org/10.1063/1.49962
[research_hames_1992]: https://doi.org/10.2514/6.1992-5056
[research_hammitt_bogdonoff_1956]: https://doi.org/10.2514/8.6969
[research_hammondmbjr_1966]: https://ntrs.nasa.gov/citations/19660060602
[research_hamza_chattopadhyay_2024]: https://doi.org/10.1016/j.compstruct.2024.118360
[research_han_bai_2000]: https://ntrs.nasa.gov/citations/20000036568
[research_han_bian_2024]: https://doi.org/10.1063/5.0179228
[research_han_cao_2019]: https://doi.org/10.1007/s10483-019-2480-6
[research_han_cheng_2026]: https://doi.org/10.1088/1674-1056/ae40d7
[research_han_han_2024]: https://doi.org/10.1063/5.0196415
[research_han_he_1995]: https://doi.org/10.1016/0008-6223(94)00172-v
[research_han_lee_2020]: https://doi.org/10.3390/en13030606
[research_han_lee_2021]: https://doi.org/10.3390/en14051381
[research_han_ma_2024]: https://doi.org/10.1016/j.apsusc.2024.159812
[research_han_sung_2002]: https://doi.org/10.2514/6.2002-332
[research_han_tian_2026]: https://doi.org/10.1016/j.applthermaleng.2026.132248
[research_han_wei_2025]: https://doi.org/10.2139/ssrn.5933060
[research_han_xu_2026]: https://doi.org/10.1063/5.0313065
[research_hanaoka_1997]: https://doi.org/10.1016/s1474-6670(17)43847-x
[research_handbook_of_1967]: https://ntrs.nasa.gov/citations/19670025583
[research_hank_murphy_2008]: https://doi.org/10.2514/6.2008-2540
[research_hannemann_martinezschramm_2017]: https://doi.org/10.2514/6.2017-2235
[research_hannemann_martinezschramm_2018]: https://doi.org/10.17815/jlsrf-4-168
[research_hannigan_webb_1991]: https://doi.org/10.2514/6.1991-5089
[research_hannumnedp_1988]: https://ntrs.nasa.gov/citations/19890000752
[research_hannumnedp_berkopecfrankd_1989]: https://ntrs.nasa.gov/citations/19890063968
[research_hanquist_boyd_2018]: https://doi.org/10.2514/6.2018-1714
[research_hanquist_hara_2017]: https://doi.org/10.1063/1.4974961
[research_hansamuels_1998]: https://ntrs.nasa.gov/citations/19990010016
[research_hao_chang_2014]: https://doi.org/10.1109/chicc.2014.6896749
[research_hao_chang_2016]: https://doi.org/10.1016/j.ast.2015.12.001
[research_hao_yan_2017]: https://doi.org/10.1016/j.ijheatmasstransfer.2016.11.052
[research_hao_yu_2025]: https://doi.org/10.1016/j.applthermaleng.2025.127490
[research_hardy_whalen_1991]: https://doi.org/10.2514/6.1991-3550
[research_hardy_whalen_1992]: https://doi.org/10.2514/6.1992-3384
[research_harish_shabaz_2016]: https://doi.org/10.9790/1684-130503134137
[research_harloff_1988]: https://doi.org/10.2514/3.26010
[research_harloff_smith_1996]: https://doi.org/10.2514/3.13140
[research_harmon_finefield_1996]: https://doi.org/10.1520/stp18239s
[research_harney_1963]: https://doi.org/10.21236/ad0295147
[research_harris_1993]: https://doi.org/10.2514/6.1993-5012
[research_harsha_waldman_1989]: https://doi.org/10.2514/6.1989-5005
[research_hartill_1977]: https://ntrs.nasa.gov/citations/19770018138
[research_hartillwr_goebeltp_1978]: https://ntrs.nasa.gov/citations/19780011153
[research_hartsell_1961]: https://doi.org/10.2514/8.8946
[research_hartwig_rame_2016]: https://doi.org/10.2514/6.2016-2186
[research_harvinsf_cabellkf_2006]: https://ntrs.nasa.gov/citations/20070003589
[research_hashimoto_1997]: https://doi.org/10.1016/s0196-8904(96)00138-0
[research_hashimoto_yoshida_1991]: https://doi.org/10.2514/6.1991-2501
[research_hass_shih_2005]: https://doi.org/10.2514/6.2005-690
[research_hass_smart_2005]: https://ntrs.nasa.gov/citations/20050215040
[research_hassneale_cabellkarenf_2010]: https://ntrs.nasa.gov/citations/20100002215
[research_hastings_persh_1957]: https://doi.org/10.21236/ad0156190
[research_hattis_malchow_1992]: https://ntrs.nasa.gov/citations/19930038290
[research_hatzl_sander_2010]: https://doi.org/10.2514/6.2010-4809
[research_haun_ball_1966]: https://doi.org/10.21236/ad0632816
[research_haw_goyne_2011]: https://doi.org/10.2514/1.49090
[research_hawk_nelson_1998]: https://ntrs.nasa.gov/citations/19980237004
[research_hawkins_kidd_1999]: https://doi.org/10.21236/ada370988
[research_hawkinsje_kirklandfp_1976]: https://ntrs.nasa.gov/citations/19760017152
[research_hawkinsrichardw_richardsonpamelaf_1991]: https://ntrs.nasa.gov/citations/19910069464
[research_hayashi_tsuboi_2020]: https://doi.org/10.2514/1.j058167
[research_hayes_probstein_1960]: https://doi.org/10.1115/1.3644007
[research_he_liu_2023]: https://doi.org/10.3390/en16031025
[research_he_nie_2026]: https://doi.org/10.1016/j.paerosci.2026.101230
[research_he_sun_2023]: https://doi.org/10.1016/j.ast.2023.108524
[research_he_tian_2024]: https://doi.org/10.1063/5.0234223
[research_he_wu_2020]: https://doi.org/10.1016/j.ast.2020.106152
[research_he_zhong_2021]: https://doi.org/10.2514/1.j059697
[research_he_zhou_2026]: https://doi.org/10.2139/ssrn.6926147
[research_health_monitoring_1994]: https://doi.org/10.2514/6.1994-3225
[research_heegjennifer_zeilerthomasa_1993]: https://ntrs.nasa.gov/citations/19930049936
[research_hegedus_mendenhall_2003]: https://doi.org/10.2514/6.2003-1104
[research_heinemannk_bogdanoffdavidw_1992]: https://ntrs.nasa.gov/citations/19930008896
[research_heiser_2010]: https://doi.org/10.2514/1.46631
[research_heitmeier_bissinger_1995]: https://doi.org/10.2514/6.1995-6027
[research_heitmeir_lederer_1992]: https://doi.org/10.2514/6.1992-5057
[research_helenbrook_colt_1977]: https://ntrs.nasa.gov/citations/19770018511
[research_helenbrookrg_mcconartywa_1971]: https://ntrs.nasa.gov/citations/19720014374
[research_helgeson_chinitz_1995]: https://doi.org/10.2514/6.1995-2768
[research_hemdan_1990]: https://doi.org/10.1016/0094-5765(90)90072-s
[research_henderson_1964]: https://doi.org/10.2514/3.2502
[research_henderson_1991]: https://doi.org/10.1115/1.2906530
[research_henryjr_andersongy_1973]: https://ntrs.nasa.gov/citations/19740004335
[research_herman_melnik_1962]: https://doi.org/10.21236/ad0404197
[research_hermann_schmidt_1995]: https://doi.org/10.2514/6.1995-3372
[research_hermannr_1965]: https://ntrs.nasa.gov/citations/19660012369
[research_hermannr_thoenesj_1965]: https://ntrs.nasa.gov/citations/19660042085
[research_herrmann_gulhan_2015]: https://doi.org/10.2514/1.b35339
[research_herrmann_hillberry_1997]: https://doi.org/10.1520/stp19924s
[research_herrouin_bowen_1996]: https://doi.org/10.1557/proc-460-287
[research_hertzberg_1956]: https://doi.org/10.2514/8.7091
[research_hertzberg_wittliff_1961]: https://doi.org/10.21236/ad0260731
[research_hickman_adams_1991]: https://ntrs.nasa.gov/citations/19920035227
[research_hicksjohnw_1991]: https://ntrs.nasa.gov/citations/19910063201
[research_hiers_2018]: https://doi.org/10.2514/6.2018-4863
[research_high_power_2022]: https://doi.org/10.2961/jlmn.2022.03.2006
[research_high_temperature_1993]: https://doi.org/10.1016/0026-0657(93)91719-e
[research_high_temperature_1996]: https://doi.org/10.1016/s0026-0657(96)92827-1
[research_high_temperature_1996_b]: https://doi.org/10.1016/s0026-0657(96)93213-0
[research_high_temperature_1999]: https://doi.org/10.1016/s0026-0657(99)80184-2
[research_hildebrand_2022]: https://ntrs.nasa.gov/citations/20220006154
[research_hillion_parisse_2023]: https://doi.org/10.3389/frspt.2023.1103981
[research_hinkley_prasad_1995]: https://doi.org/10.2514/6.1995-3915
[research_hinman_schmitt_2015]: https://doi.org/10.2514/6.2015-3509
[research_hiraiwa_sato_1997]: https://doi.org/10.2514/6.1997-292
[research_hirayama_hamaji_2026]: https://doi.org/10.1016/j.proci.2026.106200
[research_hirschen_gulhan_2009]: https://doi.org/10.2514/1.37957
[research_hitedale_1991]: https://ntrs.nasa.gov/citations/19910018895
[research_hjulianallen_1962]: https://ntrs.nasa.gov/citations/19620000713
[research_ho_rahman_2005]: https://doi.org/10.2514/6.2005-5712
[research_hodge_1976]: https://doi.org/10.21236/ada029544
[research_hodgejeffreys_harvinstephenf_2000]: https://ntrs.nasa.gov/citations/20000058170
[research_hoegenauer_koelle_1989]: https://doi.org/10.2514/6.1989-5007
[research_hoffman_phan_1995]: https://doi.org/10.1016/0008-6223(94)00176-z
[research_hoffmannek_birdrk_1989]: https://ntrs.nasa.gov/citations/19900057153
[research_hohn_guelhan_2012]: https://doi.org/10.2514/6.2012-5975
[research_hojnacki_1972]: https://doi.org/10.21236/ad0754852
[research_holden_wadhams_2001]: https://doi.org/10.21236/ada400749
[research_holguin_hudson_2018]: https://ntrs.nasa.gov/citations/20180006671
[research_holland_woods_2000]: https://ntrs.nasa.gov/citations/20000085906
[research_holland_woods_2001]: https://doi.org/10.2514/2.3772
[research_hollandscottd_1992]: https://ntrs.nasa.gov/citations/19920074224
[research_hollandscottd_1993]: https://ntrs.nasa.gov/citations/19930011110
[research_hollandscottd_hodgejeffreys_1991]: https://ntrs.nasa.gov/citations/19910036821
[research_hollandscottd_perkinsjohnn_1991]: https://ntrs.nasa.gov/citations/19910058982
[research_hollandscottd_perkinsjohnn_1992]: https://ntrs.nasa.gov/citations/19920066117
[research_hollandscottdouglas_1991]: https://ntrs.nasa.gov/citations/19910021769
[research_hollis_perkins_1996]: https://doi.org/10.2514/6.1996-2240
[research_hollmeier_kopp_1999]: https://doi.org/10.1515/tjj.1999.16.4.207
[research_holloway_limerick_1993]: https://doi.org/10.2514/6.1993-966
[research_holman_2023]: https://doi.org/10.3390/math11173684
[research_holmquist_recina_1998]: https://doi.org/10.1016/s1359-6462(98)00274-7
[research_holmquist_recina_1999]: https://doi.org/10.1016/s1359-6454(99)00051-8
[research_hongbo_yongyuan_2016]: https://doi.org/10.1504/ijscom.2016.076405
[research_hongjun_qing_2015]: https://doi.org/10.1016/j.proeng.2014.12.710
[research_hongpeng_weiqiang_2016]: https://doi.org/10.1016/j.actaastro.2016.05.014
[research_hopkins_keener_1968]: https://doi.org/10.2514/3.4644
[research_hopkins_konopka_1979]: https://ntrs.nasa.gov/citations/19790011933
[research_hordon_1973]: https://doi.org/10.1177/002199837300700409
[research_horing_maute_2025]: https://doi.org/10.2514/1.t7165
[research_horing_maute_2025_b]: https://doi.org/10.2514/6.2025-1720
[research_hornbeck_1975]: https://doi.org/10.21236/ada023471
[research_horsley_kroenke_1990]: https://doi.org/10.2514/6.1990-5235
[research_horstman_1969]: https://doi.org/10.2514/6.1969-140
[research_hoseinzade_kim_2024]: https://doi.org/10.1063/5.0215973
[research_hoseinzade_kim_2024_b]: https://doi.org/10.1016/j.ast.2024.109414
[research_hoseinzade_lakzian_2025]: https://doi.org/10.1016/j.applthermaleng.2025.125827
[research_hoskin_nguyen_2024]: https://doi.org/10.2514/6.2024-2857
[research_hossain_2025]: https://doi.org/10.31224/5900
[research_hoter_2026]: https://ntrs.nasa.gov/citations/20260004751
[research_hoult_starkey_2003]: https://doi.org/10.2514/6.2003-6964
[research_howard_2024]: https://doi.org/10.14264/345537
[research_hsia_1992]: https://doi.org/10.2514/6.1992-3100
[research_hsia_1993]: https://doi.org/10.2514/3.23696
[research_hsia_daso_1991]: https://doi.org/10.2514/6.1991-129
[research_hsia_gross_1989]: https://doi.org/10.2514/6.1989-2681
[research_hsu_liou_1991]: https://doi.org/10.2514/3.23324
[research_hu_chang_2015]: https://doi.org/10.1061/(asce)as.1943-5525.0000389
[research_hu_cheng_2023]: https://doi.org/10.1109/access.2023.3321892
[research_hu_deng_2015]: https://doi.org/10.4028/www.scientific.net/amm.719-720.324
[research_hu_guo_2025]: https://doi.org/10.1109/taes.2025.3591385
[research_hu_li_2026]: https://doi.org/10.1016/j.ijheatmasstransfer.2026.129036
[research_hu_liu_2022]: https://doi.org/10.2139/ssrn.4231148
[research_hu_mahadevan_2019]: https://doi.org/10.2514/1.j057865
[research_hu_pan_2016]: https://doi.org/10.1016/j.ijhydene.2016.05.118
[research_hu_zheng_2026]: https://doi.org/10.2514/1.a36423
[research_huang_2021]: https://doi.org/10.1063/5.0073053
[research_huang_chen_2026]: https://doi.org/10.1063/5.0314000
[research_huang_du_2019]: https://doi.org/10.1016/j.paerosci.2019.05.005
[research_huang_friedmann_2019]: https://doi.org/10.2514/1.j057499
[research_huang_friedmann_2020]: https://doi.org/10.1016/j.jfluidstructs.2020.102927
[research_huang_friedmann_2020_b]: https://doi.org/10.2514/1.j059308
[research_huang_he_2022]: https://doi.org/10.4236/aast.2022.73008
[research_huang_li_2025]: https://doi.org/10.2514/1.a36290
[research_huang_li_2025_b]: https://doi.org/10.1016/j.ast.2025.110283
[research_huang_liu_2022]: https://doi.org/10.1016/j.fpc.2022.03.001
[research_huang_lu_2026]: https://doi.org/10.1016/j.jmst.2025.09.024
[research_huang_ning_2025]: https://doi.org/10.1016/j.energy.2025.135014
[research_huang_tan_2017]: https://doi.org/10.2514/6.2017-2166
[research_huang_wang_1998]: https://doi.org/10.2514/3.27009
[research_huang_wang_2024]: https://doi.org/10.1063/5.0223963
[research_huang_wang_2025]: https://doi.org/10.1063/5.0282133
[research_huang_wang_2026]: https://doi.org/10.1016/j.ast.2026.112309
[research_huang_xia_2023]: https://doi.org/10.3390/coatings13010173
[research_huang_yan_2016]: https://doi.org/10.1016/j.ijhydene.2016.01.062
[research_huang_yao_2020]: https://doi.org/10.1016/j.actaastro.2020.01.033
[research_huang_zhang_2021]: https://doi.org/10.2514/1.j060051
[research_huang_zhao_2025]: https://doi.org/10.1063/5.0282619
[research_hube_1968]: https://doi.org/10.21236/ad0388036
[research_hudgensjuliea_trexlercarla_1992]: https://ntrs.nasa.gov/citations/19920066119
[research_huebner_1995]: https://doi.org/10.2514/3.46870
[research_huebner_1996]: https://ntrs.nasa.gov/citations/20040110860
[research_huebner_rock_2000]: https://ntrs.nasa.gov/citations/20000068996
[research_huebner_rock_2001]: https://ntrs.nasa.gov/citations/20010047675
[research_huebner_tatum_1991]: https://doi.org/10.2514/6.1991-1709
[research_huebner_tatum_1993]: https://doi.org/10.2514/3.46384
[research_huebnerlawrenced_wittedavidw_2004]: https://ntrs.nasa.gov/citations/20040012860
[research_hueteruwe_turnerjames_1998]: https://ntrs.nasa.gov/citations/19990099681
[research_hufgard_duernhofer_2023]: https://doi.org/10.1038/s41598-023-40281-8
[research_huisheng_beijing_2021]: https://doi.org/10.1115/1.4053068
[research_humphrey_brueckner_1993]: https://doi.org/10.2514/6.1993-746
[research_hung_maccormack_1977]: https://doi.org/10.2514/3.60633
[research_hunt_2015]: https://doi.org/10.14264/uql.2014.194
[research_hunt_bohon_1974]: https://ntrs.nasa.gov/citations/19740015359
[research_hunt_hunt_2021]: https://doi.org/10.2514/1.b38334
[research_hunt_martin_1992]: https://doi.org/10.2514/6.1992-5058
[research_hunt_rausch_1998]: https://doi.org/10.2514/6.1998-1641
[research_hunterjamese_mccurdydavidr_2003]: https://ntrs.nasa.gov/citations/20050215095
[research_hunterje_mccurdydr_2002]: https://ntrs.nasa.gov/citations/20020073117
[research_huntjamesl_1995]: https://ntrs.nasa.gov/citations/19970005131
[research_huntjamesl_eiswirthedwarda_1996]: https://ntrs.nasa.gov/citations/20040110965
[research_huntjamesl_martinjohng_1989]: https://ntrs.nasa.gov/citations/19890015839
[research_huntjamesl_mcclintoncharlesr_1997]: https://ntrs.nasa.gov/citations/19980018699
[research_huo_cheng_2015]: https://doi.org/10.1016/j.asr.2015.02.008
[research_huo_yang_2015]: https://doi.org/10.4028/www.scientific.net/amm.775.59
[research_hutt_mcarthur_2001]: https://ntrs.nasa.gov/citations/20020022506
[research_hwangkyuc_tiwarisurrendran_1995]: https://ntrs.nasa.gov/citations/19960002555
[research_hydrogen_slush_2007]: https://doi.org/10.1002/9780470114735.hawley08646
[research_hyers_2009]: https://doi.org/10.21236/ada524249
[research_hyper_x_model_1996]: https://ntrs.nasa.gov/citations/20000033438
[research_hypersonic_air_breathing_2022]: https://doi.org/10.1002/9781119640646.ch13
[research_hypersonic_flight_2015]: https://doi.org/10.1036/1097-8542.333400
[research_hypersonic_flight_2017]: https://doi.org/10.1036/1097-8542.yb160013
[research_hypersonic_materials_2023]: https://doi.org/10.12968/s1478-2774(24)50016-3
[research_hypersonic_viscous_2006]: https://doi.org/10.2514/5.9781600861956.0375.0414
[research_iaccarino_pecnik_2010]: https://doi.org/10.1115/imece2010-40186
[research_ibadi_supriadi_2026]: https://doi.org/10.2298/sos250116014i
[research_idris_saad_2019]: https://doi.org/10.1051/eucass/201911747
[research_ifti_hermann_2022]: https://doi.org/10.1007/s00348-022-03446-1
[research_ifti_hermann_2022_b]: https://doi.org/10.2514/1.a35325
[research_ignition_delay_2018]: https://doi.org/10.15372/fgv20180404
[research_igra_2026]: https://doi.org/10.2514/6.2026-4172
[research_ikawa_1991]: https://doi.org/10.2514/3.23345
[research_ikenson_2025]: https://doi.org/10.1063/10.0039841
[research_im_chen_1998]: https://doi.org/10.1016/s0082-0784(98)80505-5
[research_im_do_2018]: https://doi.org/10.1016/j.paerosci.2017.12.001
[research_influence_of_2023]: https://doi.org/10.1063/5.0150253
[research_ingenito_2015]: https://doi.org/10.1016/j.ijhydene.2014.12.014
[research_ingenito_bruno_2009]: https://doi.org/10.2514/6.2009-5186
[research_ingenito_bruno_2009_b]: https://doi.org/10.2514/6.2009-7419
[research_ingenito_bruno_2010]: https://doi.org/10.2514/6.2010-758
[research_inger_1990]: https://doi.org/10.1515/tjj.1990.7.3-4.309
[research_inger_1995]: https://doi.org/10.2514/3.12950
[research_inger_1995_b]: https://doi.org/10.1016/0094-5765(95)00101-5
[research_inger_1995_c]: https://doi.org/10.2514/3.713
[research_ingeri_1966]: https://doi.org/10.1016/0017-9310(66)90004-4
[research_inmanjennifera_bathelbrettf_2011]: https://ntrs.nasa.gov/citations/20110004025
[research_inmanjennifera_bathelbrettf_2013]: https://ntrs.nasa.gov/citations/20150018912
[research_inoue_yamamoto_1990]: https://doi.org/10.2322/jjsass1969.38.204
[research_instrumentation_for_1974]: https://doi.org/10.2514/4.865077
[research_instrumentation_for_1974_b]: https://doi.org/10.2514/5.9781600865077.0041.0058
[research_interstitially_protected_1988]: https://doi.org/10.1016/0010-4361(88)90336-9
[research_introduction_to_2022]: https://doi.org/10.1002/9781119640646.ch1
[research_investigation_of_2023]: https://doi.org/10.1063/5.0148331
[research_investigation_of_2024]: https://doi.org/10.47176/jame.43.4.1064
[research_inviscid_high_temperature_2006]: https://doi.org/10.2514/5.9781600861956.0599.0646
[research_irimpan_mannil_2015]: https://doi.org/10.1016/j.measurement.2014.10.056
[research_isaac_miles_1990]: https://doi.org/10.2514/6.1990-3066
[research_isaac_williams_1959]: https://doi.org/10.1038/183531a0
[research_ishihara_ogino_2015]: https://doi.org/10.2322/tjsass.58.319
[research_ishihara_ogino_2016]: https://doi.org/10.1016/j.ast.2015.12.015
[research_ishimoto_takizawa_1996]: https://doi.org/10.2514/6.1996-3403
[research_isono_2026]: https://doi.org/10.1007/s10494-026-00731-5
[research_isono_fujikawa_2025]: https://doi.org/10.2514/6.2025-0957
[research_ispir_saracoglu_2023]: https://doi.org/10.1016/j.ast.2023.108501
[research_ispir_zdybal_2023]: https://doi.org/10.1016/j.actaastro.2022.11.013
[research_itoh_2007]: https://doi.org/10.2514/6.2007-1041
[research_itoh_ueda_2002]: https://doi.org/10.1007/s00193-002-0147-0
[research_ivanov_markelov_1998]: https://doi.org/10.2514/3.26992
[research_izenson_1991]: https://doi.org/10.2514/6.1991-4098
[research_jachimowskicj_1974]: https://ntrs.nasa.gov/citations/19750026376
[research_jachimowskicj_mclainag_1983]: https://ntrs.nasa.gov/citations/19830011554
[research_jackman_douglas_1992]: https://doi.org/10.2514/6.1992-5073
[research_jackson_blanchard_1964]: https://doi.org/10.21236/ad0451306
[research_jackson_gruber_2011]: https://ntrs.nasa.gov/citations/20110011187
[research_jackson_gruber_2015]: https://doi.org/10.2514/1.b35350
[research_jackson_wang_1974]: https://ntrs.nasa.gov/citations/19740021101
[research_jacobs_rogers_1990]: https://ntrs.nasa.gov/citations/19900055674
[research_jacobsen_tam_2006]: https://doi.org/10.2514/6.2006-4508
[research_jalbert_hiers_1993]: https://doi.org/10.4271/932551
[research_james_2024]: https://doi.org/10.14264/329671
[research_james_agrawal_2026]: https://doi.org/10.1016/j.proci.2026.106110
[research_janiszewski_wozniak_2022]: https://doi.org/10.5604/01.3001.0016.1105
[research_javaid_serghides_2003]: https://doi.org/10.2514/6.2003-6953
[research_jawed_nagle_1986]: https://doi.org/10.1016/0025-5408(86)90075-9
[research_jayaraman_lewis_1997]: https://doi.org/10.2514/2.5141
[research_jazra_smart_2011]: https://doi.org/10.2514/6.2011-2377
[research_jee_etele_2020]: https://doi.org/10.2514/1.a34616
[research_jeffreyacerro_cpshore_1990]: https://ntrs.nasa.gov/citations/20080021318
[research_jeffs_newton_2026]: https://doi.org/10.1016/j.jeurceramsoc.2025.117811
[research_jenkins_2000]: https://ntrs.nasa.gov/citations/20000068530
[research_jensenrm_bryceca_1972]: https://ntrs.nasa.gov/citations/19730003242
[research_jeong_choi_2020]: https://doi.org/10.3390/en13154029
[research_jeong_kim_2024]: https://doi.org/10.6108/kspe.2024.28.5.078
[research_jeong_kim_2024_b]: https://doi.org/10.2514/6.2024-1418
[research_jeong_kim_2025]: https://doi.org/10.1007/s12206-024-1227-1
[research_jeong_lee_2023]: https://doi.org/10.1016/j.proci.2022.07.245
[research_jessen_gronig_1995]: https://doi.org/10.1007/978-3-642-78829-1_46
[research_jessicaluxbaumann_darrylaburkes_2005]: https://ntrs.nasa.gov/citations/20050237906
[research_jewell_miller_2017]: https://doi.org/10.2514/1.a33725
[research_jewell_shepherd_2013]: https://doi.org/10.21236/ada595841
[research_jha_forster_1991]: https://doi.org/10.2355/isijinternational.31.1267
[research_ji_he_2024]: https://doi.org/10.1063/5.0234187
[research_ji_li_2019]: https://doi.org/10.2514/1.j056165
[research_ji_xie_2022]: https://doi.org/10.32604/icces.2022.08737
[research_ji_zhang_2019]: https://doi.org/10.1016/j.ast.2019.07.011
[research_jia_fu_2020]: https://doi.org/10.1016/j.actaastro.2020.07.022
[research_jia_fu_2020_b]: https://doi.org/10.1016/j.actaastro.2019.11.038
[research_jia_ye_2019]: https://doi.org/10.1016/j.actaastro.2019.05.034
[research_jiang_2014]: https://doi.org/10.2514/6.2014-1012
[research_jiang_2023]: https://doi.org/10.1016/j.paerosci.2023.100955
[research_jiang_liu_2022]: https://doi.org/10.1016/j.actaastro.2021.12.010
[research_jiang_liu_2025]: https://doi.org/10.1063/5.0287673
[research_jiang_wang_2017]: https://doi.org/10.1007/978-3-319-46213-4_29
[research_jiang_wang_2023]: https://doi.org/10.1080/10407782.2023.2174627
[research_jiang_wang_2023_b]: https://doi.org/10.1016/j.fuel.2023.127462
[research_jiang_wang_2023_c]: https://doi.org/10.1016/j.applthermaleng.2022.119757
[research_jiang_xu_2025]: https://doi.org/10.1016/j.ceramint.2024.11.502
[research_jiang_yu_2015]: https://doi.org/10.1007/978-3-319-16835-7_7
[research_jiang_yu_2019]: https://doi.org/10.1007/978-3-319-91020-8_1
[research_jiang_zhan_2025]: https://doi.org/10.1016/j.energy.2025.138187
[research_jiang_zhang_2021]: https://doi.org/10.1016/j.cja.2020.11.001
[research_jiao_chang_2015]: https://doi.org/10.2514/1.j053913
[research_jiao_chang_2016]: https://doi.org/10.1016/j.ast.2016.09.008
[research_jiao_chang_2016_b]: https://doi.org/10.1016/j.actaastro.2016.08.025
[research_jiao_chang_2017]: https://doi.org/10.1016/j.actaastro.2016.10.027
[research_jiao_chang_2018]: https://doi.org/10.1016/j.actaastro.2017.12.005
[research_jiao_wang_2017]: https://doi.org/10.2514/1.j055831
[research_jieyan_yuan_2022]: https://doi.org/10.2139/ssrn.4088134
[research_jin_jing_2017]: https://doi.org/10.1016/j.jaap.2017.04.010
[research_jin_luo_2015]: https://doi.org/10.1016/j.actaastro.2014.12.012
[research_jin_yao_2023]: https://doi.org/10.2514/6.2023-4444
[research_jin_zhao_2024]: https://doi.org/10.1186/s42774-024-00173-5
[research_jing_shuo_2007]: https://doi.org/10.2514/6.2007-642
[research_jing_song_2026]: https://doi.org/10.1016/j.applthermaleng.2026.130617
[research_jingqi_yulong_2024]: https://doi.org/10.1016/j.energy.2024.132763
[research_jmthornton_jbemeurisse]: https://ntrs.nasa.gov/citations/20220007678
[research_jo_choi_2026]: https://doi.org/10.1016/j.ijhydene.2026.156139
[research_jo_sung_2026]: https://doi.org/10.2514/6.2026-2738
[research_jobart_blandin_1994]: https://doi.org/10.4028/www.scientific.net/msf.170-172.465
[research_johnrmicol]: https://ntrs.nasa.gov/citations/20200005591
[research_johnson_1967]: https://doi.org/10.2514/6.1967-297
[research_johnson_1991]: https://ntrs.nasa.gov/citations/19920035226
[research_johnson_jenquin_2022]: https://doi.org/10.2514/6.2022-3478
[research_johnson_mirdamadi_1993]: https://ntrs.nasa.gov/citations/19940018145
[research_johnson_mirdamadi_1994]: https://ntrs.nasa.gov/citations/19940032159
[research_johnson_mirdamadi_1996]: https://doi.org/10.1520/stp16457s
[research_johnson_narayanaswamy_2024]: https://doi.org/10.2514/1.j064324
[research_johnson_seipp_1998]: https://doi.org/10.1063/1.869781
[research_johnson_weeks_2005]: https://ntrs.nasa.gov/citations/20050162057
[research_johnson_wu_1975]: https://doi.org/10.1115/1.3447318
[research_johnsondl_hillck_1993]: https://ntrs.nasa.gov/citations/19930040918
[research_johnsoniii_wu_1974]: https://doi.org/10.21236/ada017631
[research_johnsonmay_weber_2024]: https://doi.org/10.2514/1.b39271
[research_johnsontheodoref_natividadroderick_1998]: https://ntrs.nasa.gov/citations/19980107885
[research_johnsontheodoref_natividadroderick_2005]: https://ntrs.nasa.gov/citations/20050217094
[research_johnston_cubbage_1971]: https://doi.org/10.2514/3.59129
[research_johnston_pittman_1978_b]: https://doi.org/10.2514/3.58365
[research_johnstonpatrickj_whiteheadallenhjr_1987]: https://ntrs.nasa.gov/citations/19880023141
[research_jones_2006]: https://ntrs.nasa.gov/citations/20060056094
[research_jones_2011]: https://doi.org/10.21236/ada552062
[research_jones_myrabo_1992]: https://doi.org/10.2514/3.11467
[research_joneskennethm_1994]: https://ntrs.nasa.gov/citations/19950012573
[research_jonesra_huberpw_1978]: https://ntrs.nasa.gov/citations/19790036073
[research_jorris_2014]: https://doi.org/10.2514/6.2014-2579
[research_josemrodriguez_brettfbathel]: https://ntrs.nasa.gov/citations/20205002606
[research_joshi_lu_2016]: https://doi.org/10.2514/1.b35520
[research_joshi_lu_2017]: https://doi.org/10.2514/1.b36170
[research_joyce_pomroy_2005]: https://doi.org/10.2514/6.2005-3333
[research_ju_liu_2022]: https://doi.org/10.15541/jim20210182
[research_ju_niioka_1994]: https://doi.org/10.1016/0010-2180(94)90127-9
[research_ju_niioka_1994_b]: https://doi.org/10.1016/0010-2180(94)90032-9
[research_ju_niioka_1995]: https://doi.org/10.1016/0010-2180(95)00047-a
[research_juleskenol_barnhartpaulj_1998]: https://ntrs.nasa.gov/citations/20050177169
[research_juliano_adamczak_2015]: https://doi.org/10.2514/1.a33142
[research_julurusandeep_avsskumaraswamigupta_2023]: https://doi.org/10.37934/arfmts.101.1.7389
[research_jun_yang_2026]: https://doi.org/10.5139/jksas.2026.54.1.15
[research_junaidr_beebim_2015]: https://doi.org/10.70729/ijser15399
[research_jung_han_2017]: https://doi.org/10.5139/jksas.2017.45.3.259
[research_kaemming_fotia_2017]: https://doi.org/10.2514/1.b36237
[research_kahre_1987]: https://doi.org/10.4271/872529
[research_kaili_kunyuan_2010]: https://doi.org/10.2514/6.2010-7034
[research_kalaiarassan_krishan_2018]: https://doi.org/10.1016/j.matpr.2018.02.350
[research_kaltreider_1951]: https://doi.org/10.1016/0002-9378(51)91159-3
[research_kamal_2025]: https://doi.org/10.55041/ijsrem42315
[research_kamath_mao_1991]: https://ntrs.nasa.gov/citations/19910058851
[research_kamath_mcclinton_1992]: https://ntrs.nasa.gov/citations/19930030246
[research_kamathpradeeps_bakernr_1990]: https://ntrs.nasa.gov/citations/19900032909
[research_kamel_owis_2015]: https://doi.org/10.1504/ijesms.2015.066132
[research_kanapathipillai_yu_2024]: https://doi.org/10.1016/j.proci.2024.105414
[research_kanda_1998]: https://doi.org/10.2514/6.1998-3427
[research_kanda_2000]: https://doi.org/10.2514/6.2000-3705
[research_kanda_hiraiwa_2003]: https://doi.org/10.2514/6.2003-11
[research_kanda_hiraiwa_2004]: https://doi.org/10.2514/1.2189
[research_kanda_inagaki_2024]: https://doi.org/10.1063/5.0234035
[research_kanda_katano_2020]: https://doi.org/10.1299/jsmemecj.2020.j19108
[research_kanda_komuro_1989]: https://doi.org/10.2514/6.1989-2680
[research_kanda_masuya_1991]: https://doi.org/10.2514/3.23344
[research_kanda_masuya_1994]: https://doi.org/10.2514/3.23741
[research_kandula_kummitha_2025]: https://doi.org/10.1080/00102202.2025.2580323
[research_kang_1970]: https://doi.org/10.2514/3.5883
[research_kang_kim_2018]: https://doi.org/10.5139/jksas.2018.46.11.892
[research_kang_lee_2010]: https://doi.org/10.2514/6.2010-7123
[research_kang_yan_2026]: https://doi.org/10.1016/j.ast.2026.112141
[research_karabacak_turan_2023]: https://doi.org/10.18038/estubtda.1270986
[research_karanianaj_keplerce_1965]: https://ntrs.nasa.gov/citations/19650044095
[research_karasopoulos_langan_1992]: https://doi.org/10.21236/ada259761
[research_kardas_2023]: https://doi.org/10.2514/6.2023-4252
[research_karl_hannemann_2006]: https://doi.org/10.2514/6.2006-8041
[research_karl_hannemann_2008]: https://doi.org/10.2514/6.2008-2548
[research_karl_laurence_2012]: https://doi.org/10.2514/6.2012-5912
[research_karl_steelant_2018]: https://doi.org/10.2514/1.b36637
[research_karlgaard_martin_2005]: https://ntrs.nasa.gov/citations/20050232845
[research_karlgaard_tartabini_2004]: https://ntrs.nasa.gov/citations/20040111310
[research_karpenko_tolstoguzov_2023]: https://doi.org/10.20944/preprints202308.2030.v1
[research_kaskan_reuther_1977]: https://doi.org/10.1016/s0082-0784(77)80398-6
[research_kasten_1991]: https://doi.org/10.4271/911170
[research_kauffman_grandhi_1990]: https://doi.org/10.2514/6.1990-2471
[research_kauffman_grandhi_1991]: https://doi.org/10.2514/3.26226
[research_kaufman_1963]: https://doi.org/10.21236/ad0421859
[research_kaufman_louisg_1963]: https://doi.org/10.21236/ad0431280
[research_kaufman_louisg_1964]: https://doi.org/10.21236/ad0601804
[research_kaufmanalbert_1988]: https://ntrs.nasa.gov/citations/19880013021
[research_kaul_1991]: https://ntrs.nasa.gov/citations/19910000538
[research_kaulupenderk_1989]: https://ntrs.nasa.gov/citations/19910036572
[research_kavoosi_mashhadi_2026]: https://doi.org/10.1016/j.ceramint.2026.07.429
[research_kawalec_wolanski_2023]: https://doi.org/10.2514/1.b38771
[research_kazmar_2002]: https://ntrs.nasa.gov/citations/20020092084
[research_kazmar_2005]: https://doi.org/10.2514/6.2005-3256
[research_ke_wang_2025]: https://doi.org/10.1016/j.applthermaleng.2025.126835
[research_keener_1992]: https://ntrs.nasa.gov/citations/19920005830
[research_keener_spaid_1994]: https://ntrs.nasa.gov/citations/20010046977
[research_keer_faber_1994]: https://doi.org/10.21236/ada329853
[research_kehoe_ricketts_1992]: https://ntrs.nasa.gov/citations/19920072503
[research_kelly_1973]: https://doi.org/10.21236/ad0771157
[research_kellyhn_wietingar_1984]: https://ntrs.nasa.gov/citations/19840017665
[research_kellyhneale_blossermaxl_1992]: https://ntrs.nasa.gov/citations/19930003270
[research_kellyhneale_blossermaxl_1994]: https://ntrs.nasa.gov/citations/19940033030
[research_kerrebrock_1992]: https://doi.org/10.2514/3.23600
[research_kerrebrockjackl_poferldavidj_1984]: https://ntrs.nasa.gov/citations/19970030198
[research_kerth_lepage_2024]: https://doi.org/10.1063/5.0189321
[research_keshmiri_colgren_2006]: https://doi.org/10.2514/6.2006-8158
[research_khali_yao_2018]: https://doi.org/10.1504/ijtamm.2018.096429
[research_khambaswadkar_2024]: https://doi.org/10.58445/rars.2094
[research_khamlak_2026]: https://doi.org/10.37547/tajet/book-26-01
[research_khan_chakraborty_2023]: https://doi.org/10.2514/1.j063120
[research_khan_riccio_2024]: https://doi.org/10.1016/j.paerosci.2024.101021
[research_kharitonov_chernykh_1974]: https://doi.org/10.1007/bf01031324
[research_khrapko_2018]: https://doi.org/10.18502/keg.v3i3.1647
[research_kianvashrad_knight_2019]: https://doi.org/10.2514/1.j057883
[research_kibbeytim_2019]: https://ntrs.nasa.gov/citations/20190027424
[research_kidd_narayanaswamy_2014]: https://ntrs.nasa.gov/citations/20150001233
[research_kiehn_2020]: https://doi.org/10.1007/s12567-020-00319-3
[research_killiansamuels_talschwartz]: https://ntrs.nasa.gov/citations/20250010496
[research_kim_2018]: https://doi.org/10.1063/1.5078623
[research_kim_choi_2021]: https://doi.org/10.32908/hthp.v50.1079
[research_kim_choi_2026]: https://doi.org/10.3390/ma19020303
[research_kim_jang_2020]: https://doi.org/10.2514/6.2020-2443
[research_kim_jang_2022]: https://doi.org/10.1371/journal.pone.0270743
[research_kim_kwon_2017]: https://doi.org/10.2514/6.2017-0558
[research_kim_kwon_2018]: https://doi.org/10.1016/j.ast.2018.04.044
[research_kim_lee_2021]: https://doi.org/10.3390/en14113210
[research_kim_lee_2024]: https://doi.org/10.6108/kspe.2024.28.5.027
[research_kim_park_2019]: https://doi.org/10.1016/j.actaastro.2019.02.022
[research_kim_park_2020]: https://doi.org/10.6108/jpne.2020.1.1.011
[research_kim_park_2025]: https://doi.org/10.1007/s42405-025-01021-6
[research_kim_rasmussen_1982]: https://doi.org/10.2514/6.1982-1299
[research_kim_seo_2022]: https://doi.org/10.5139/jksas.2022.50.1.21
[research_kim_seo_2025]: https://doi.org/10.1016/j.ast.2025.109978
[research_kim_shim_2024]: https://doi.org/10.2139/ssrn.5031710
[research_kim_shim_2025]: https://doi.org/10.1007/s00348-025-04117-7
[research_kimhyoungjin_kumanotakayasu_2011]: https://ntrs.nasa.gov/citations/20110011992
[research_kimmel_2008]: https://doi.org/10.2514/6.2008-4034
[research_kimmel_2008_b]: https://doi.org/10.2514/6.2008-4293
[research_kimmel_adamczak_2011]: https://doi.org/10.21236/ada548272
[research_kimmel_adamczak_2014]: https://doi.org/10.21236/ada605731
[research_kimmel_borg_2015]: https://doi.org/10.21236/ada623564
[research_kimmerly_2024]: https://doi.org/10.14264/345542
[research_kimura_1993]: https://doi.org/10.1051/jp4:1993765
[research_kimura_shibusa_1976]: https://doi.org/10.1016/0008-6223(76)90264-5
[research_kindler_blacha_2008]: https://doi.org/10.2514/6.2008-5167
[research_kinslow_busby_1973]: https://doi.org/10.21236/ad0754276
[research_kireeti_ravikiransastry_2022]: https://doi.org/10.1016/j.fuel.2022.124528
[research_kirik_goyne_2018]: https://doi.org/10.2514/1.b36605
[research_kirkby_1964]: https://doi.org/10.1016/0010-2180(64)90103-8
[research_kirsch_krueger_2025]: https://doi.org/10.1115/1.4070187
[research_kishida_2006]: https://doi.org/10.1063/1.2204542
[research_kishoren_gugulothu_2023]: https://doi.org/10.1016/j.ijhydene.2022.09.135
[research_klein_chakraborty_2017]: https://doi.org/10.1007/s10494-017-9843-9
[research_kline_alonso_2017]: https://doi.org/10.2514/1.j055863
[research_kloesel_ratnayake_2011]: https://ntrs.nasa.gov/citations/20110013567
[research_klothakis_nikolos_2024]: https://doi.org/10.3390/computation12070140
[research_klothakis_nikolos_2024_b]: https://doi.org/10.3390/computation12100200
[research_knelson_clarkwhawk_1997]: https://ntrs.nasa.gov/citations/19990064401
[research_knight_2015]: https://doi.org/10.21236/ada627597
[research_knight_naiman_2009]: https://doi.org/10.21236/ada498212
[research_ko_gong_2000]: https://ntrs.nasa.gov/citations/20000095550
[research_ko_gong_2001]: https://ntrs.nasa.gov/citations/20010098879
[research_ko_mannion_2025]: https://doi.org/10.2514/1.t6991
[research_ko_son_2024]: https://doi.org/10.5139/jksas.2024.52.8.655
[research_ko_son_2026]: https://doi.org/10.1016/j.ast.2026.112444
[research_kobayashi_yoshihara_1990]: https://doi.org/10.1080/02619180.1990.11753477
[research_kocaaslan_2024]: https://doi.org/10.46793/adeletters.2024.3.1.1
[research_koch_wilken_2025]: https://doi.org/10.1007/s12567-025-00597-9
[research_kocher_keller_1969]: https://doi.org/10.1007/978-1-4757-0549-2_38
[research_kodera_sunami_2005]: https://doi.org/10.2514/6.2005-3355
[research_koeplinger_2026]: https://ntrs.nasa.gov/citations/20260004838
[research_kohl_1993]: https://doi.org/10.1007/978-94-011-1828-6_15
[research_kojima_taguchi_2015]: https://doi.org/10.2514/6.2015-3595
[research_kolimiabdulahad_2021]: https://doi.org/10.21275/sr21926223440
[research_kong_chang_2020]: https://doi.org/10.2514/1.j059302
[research_kong_lee_2023]: https://doi.org/10.1016/j.jeurceramsoc.2023.02.048
[research_kong_wang_2024]: https://doi.org/10.2139/ssrn.4705683
[research_koo_lee_2023]: https://doi.org/10.3390/aerospace10110949
[research_koo_raman_2015]: https://doi.org/10.1016/j.proci.2014.08.005
[research_kopp_hollmeier_1999]: https://doi.org/10.2514/6.1999-4813
[research_kors_1988]: https://doi.org/10.1016/0094-5765(88)90099-9
[research_kortejj_2000]: https://ntrs.nasa.gov/citations/19990116372
[research_kortejohnj_singhdj_1993]: https://ntrs.nasa.gov/citations/19930065724
[research_koschel_1996]: https://doi.org/10.2514/6.1996-4579
[research_koschel_rick_1991]: https://doi.org/10.2514/6.1991-5019
[research_koubek_1963]: https://doi.org/10.21236/ad0408362
[research_kouchi_goyne_2015]: https://doi.org/10.1007/s00348-015-2081-9
[research_kourtides_1993]: https://ntrs.nasa.gov/citations/19930012922
[research_kowbel_huang_1993]: https://doi.org/10.1016/0008-6223(93)90040-h
[research_kramer_buhler_1980]: https://doi.org/10.2514/3.57746
[research_kremeyer_pakhomov_2008]: https://doi.org/10.1063/1.2931905
[research_kreutz_law_1996]: https://doi.org/10.1016/0140-6701(96)88878-3
[research_krieger_1990]: https://doi.org/10.2514/6.1990-1932
[research_krishamurthyramesh_1993]: https://ntrs.nasa.gov/citations/19940023408
[research_krivosheyev_kisel_2024]: https://doi.org/10.1016/j.ijhydene.2024.03.363
[research_krouse_ellis_1966]: https://doi.org/10.21236/ad0634562
[research_kshetrimayum_menezes_2021]: https://doi.org/10.1088/1361-6501/abe161
[research_kulkarni_gujar_2026]: https://doi.org/10.1615/hightempmatproc.2025058747
[research_kumakawa_1989]: https://doi.org/10.3775/jie.68.107
[research_kumar_1981]: https://doi.org/10.2514/6.1981-185
[research_kumar_1982]: https://doi.org/10.2514/3.51052
[research_kumar_1982_b]: https://doi.org/10.2514/3.61571
[research_kumar_mahulikar_2016]: https://doi.org/10.1016/j.applthermaleng.2016.04.100
[research_kumar_mahulikar_2017]: https://doi.org/10.2514/1.a33688
[research_kumar_penchalaiah_2018]: https://doi.org/10.1016/j.ifacol.2018.05.020
[research_kumar_rakesh_2017]: https://doi.org/10.17654/fm020030375
[research_kumar_rana_2024]: https://doi.org/10.1063/5.0227257
[research_kumar_ranjan_2026]: https://doi.org/10.2139/ssrn.6962147
[research_kumar_ranjan_2026_b]: https://doi.org/10.2514/6.2026-4090
[research_kumar_ranjan_2026_c]: https://doi.org/10.1016/j.ast.2026.113469
[research_kumar_reddy_2018]: https://doi.org/10.15406/fmrij.2018.02.00031
[research_kumar_sarkar_2018]: https://doi.org/10.1177/0954410018795265
[research_kumar_thornber_2016]: https://doi.org/10.4028/www.scientific.net/amm.846.61
[research_kummitha_2017]: https://doi.org/10.1016/j.ijhydene.2017.01.148
[research_kummitha_2022]: https://doi.org/10.1016/j.ijhydene.2022.06.263
[research_kummitha_2024]: https://doi.org/10.1016/j.ijhydene.2024.06.133
[research_kummitha_kandula_2024]: https://doi.org/10.1016/j.ijhydene.2024.10.304
[research_kummitha_kandula_2025]: https://doi.org/10.1017/aer.2025.10117
[research_kummitha_pandey_2018]: https://doi.org/10.1016/j.actaastro.2018.09.026
[research_kummitha_pandey_2020]: https://doi.org/10.1093/jcde/qwaa084
[research_kummitha_pandey_2021]: https://doi.org/10.1016/j.fuel.2021.121425
[research_kummitha_suneetha_2017]: https://doi.org/10.1016/j.ijhydene.2017.01.213
[research_kunze_2020]: https://doi.org/10.14264/uql.2020.182
[research_kurade_suryanarayana_2023]: https://doi.org/10.1016/j.ast.2023.108560
[research_kuranov_korabelnikov_2012]: https://doi.org/10.2514/6.2012-5879
[research_kurosaka_shimamura_2024]: https://doi.org/10.1007/s00193-024-01194-1
[research_kurtz_aizengendler_2015]: https://doi.org/10.2514/6.2015-0110
[research_kurtz_aizengendler_2016]: https://doi.org/10.2514/1.j054207
[research_kussoy_menter_1992]: https://ntrs.nasa.gov/citations/19930009189
[research_kutschenreuter_1962]: https://doi.org/10.2514/8.9827
[research_kutschenreuter_balent_1965]: https://doi.org/10.2514/3.28150
[research_kutschenreuter_paulh_1966]: https://doi.org/10.21236/ad0636981
[research_kutschenreuterpaul_1992]: https://ntrs.nasa.gov/citations/19920012285
[research_kydd_mullaney_1961]: https://doi.org/10.1016/0010-2180(61)90112-2
[research_l_r_2012]: https://doi.org/10.2514/6.2012-5937
[research_labbe_gilbert_2009]: https://ntrs.nasa.gov/citations/20090033116
[research_labib_king_2015]: https://doi.org/10.1016/j.nucengdes.2015.02.004
[research_labib_king_2015_b]: https://doi.org/10.1016/j.nucengdes.2015.02.006
[research_lacaze_vane_2017]: https://doi.org/10.2514/6.2017-0142
[research_ladeinde_2019]: https://doi.org/10.2514/6.2019-4419
[research_ladeinde_2021]: https://doi.org/10.2514/6.2021-3534
[research_ladeinde_lou_2018]: https://doi.org/10.2514/1.b36779
[research_ladeinde_lou_2019]: https://doi.org/10.1016/j.combustflame.2019.03.030
[research_ladyzhenskii_lipin_1966]: https://doi.org/10.1007/bf01016282
[research_ladyzhenskij_1963]: https://doi.org/10.21236/ad0295787
[research_laiht_kimsc_1993]: https://ntrs.nasa.gov/citations/19930065723
[research_lakka_randive_2021]: https://doi.org/10.1016/j.actaastro.2020.08.040
[research_lam_stollenwerk_1966]: https://doi.org/10.2514/6.1966-771
[research_lan_wang_2025]: https://doi.org/10.1016/j.ifacol.2025.11.420
[research_landiech_aumasson_1990]: https://doi.org/10.1016/0094-5765(90)90019-h
[research_landis_denis_2003]: https://ntrs.nasa.gov/citations/20150012328
[research_landsberg_curran_2022]: https://doi.org/10.1016/j.ast.2022.107622
[research_lange_gieseler_1953]: https://doi.org/10.2514/8.2804
[research_langener_myrabo_2009]: https://doi.org/10.2514/6.2009-4806
[research_langstonsarahl_langchristapherg_2016]: https://ntrs.nasa.gov/citations/20160011574
[research_lanshin_1993]: https://doi.org/10.2514/6.1993-5103
[research_lantz_1992]: https://doi.org/10.2514/3.23510
[research_larsson_2012]: https://doi.org/10.2514/6.2012-4261
[research_larsson_laurence_2015]: https://doi.org/10.1016/j.combustflame.2014.09.017
[research_lathamea_sorensonne_1972]: https://ntrs.nasa.gov/citations/19720007338
[research_laumakis_bonacuse_2001]: https://doi.org/10.1106/tvcd-wlk9-0kcn-kmxe
[research_laurence_karl_2015]: https://doi.org/10.1007/978-3-319-16835-7_47
[research_laurence_martinezschramm_2012]: https://doi.org/10.2514/6.2012-2861
[research_law_2004]: https://doi.org/10.21236/ada429385
[research_law_metghalchi_1989]: https://doi.org/10.1016/s0082-0784(89)80183-3
[research_lawingpl_johnsoncb_1978]: https://ntrs.nasa.gov/citations/19780034729
[research_lawrencescottl_1991]: https://ntrs.nasa.gov/citations/19910058972
[research_lawrencescottl_1992]: https://ntrs.nasa.gov/citations/19930038308
[research_le_liu_2009]: https://doi.org/10.2514/6.2009-7344
[research_le_liu_2023]: https://doi.org/10.3390/drones7020119
[research_leamerpc_kennonig_1978]: https://ntrs.nasa.gov/citations/19790003843
[research_lear_mcgrath_2008]: https://ntrs.nasa.gov/citations/20080017199
[research_lebedev_minostsev_1969]: https://doi.org/10.1007/bf01014976
[research_lederer_schwab_1991]: https://doi.org/10.2514/6.1991-5040
[research_lee_bae_2023]: https://doi.org/10.6108/kspe.2023.27.4.015
[research_lee_duan_2022]: https://doi.org/10.1016/j.actaastro.2022.09.029
[research_lee_gupta_1990]: https://doi.org/10.2514/3.26123
[research_lee_jo_2026]: https://doi.org/10.3390/aerospace13010079
[research_lee_kang_2012]: https://doi.org/10.1115/imece2012-87193
[research_lee_kang_2015]: https://doi.org/10.6108/kspe.2015.19.6.081
[research_lee_kang_2019]: https://doi.org/10.1371/journal.pone.0224994
[research_lee_kang_2020]: https://doi.org/10.6108/kspe.2020.24.6.016
[research_lee_kim_2020]: https://doi.org/10.1371/journal.pone.0240300
[research_lee_lee_2023]: https://doi.org/10.3390/aerospace10050415
[research_lee_lewis_1991]: https://ntrs.nasa.gov/citations/19910058981
[research_lee_mitani_1999]: https://doi.org/10.2514/6.1999-616
[research_lee_na_2018]: https://doi.org/10.6108/kspe.2018.22.4.068
[research_lee_ryu_2021]: https://doi.org/10.7316/khnes.2021.32.6.565
[research_lee_yang_2013]: https://doi.org/10.6108/kspe.2013.17.4.063
[research_lee_yang_2015]: https://doi.org/10.6108/kspe.2015.19.6.010
[research_lee_yang_2022]: https://doi.org/10.6108/kspe.2022.26.1.077
[research_lee_yang_2022_b]: https://doi.org/10.6108/kspe.2022.26.4.010
[research_lees_1956]: https://doi.org/10.2514/8.6977
[research_lees_1957]: https://doi.org/10.2514/8.12491
[research_lees_kubota_1972]: https://doi.org/10.21236/ad0755276
[research_lefieux_garnier_2021]: https://doi.org/10.2514/1.j059972
[research_lehmusto_ievlev_2024]: https://doi.org/10.1007/s11085-024-10323-1
[research_lehrach_1987]: https://doi.org/10.2514/6.1987-1966
[research_lehtinen_zeller_1972]: https://doi.org/10.1016/0005-1098(72)90027-1
[research_lehtinenb_zellerjr_1978]: https://ntrs.nasa.gov/citations/19780015081
[research_lei_1992]: https://ntrs.nasa.gov/citations/19930038316
[research_lei_zhang_2023]: https://doi.org/10.1016/j.tsep.2023.102255
[research_leingang_1992]: https://ntrs.nasa.gov/citations/19920012277
[research_leingangjl_stullfd_1992]: https://ntrs.nasa.gov/citations/19920012289
[research_lemcoemm_1992]: https://ntrs.nasa.gov/citations/19930004481
[research_lenard_long_1962]: https://doi.org/10.21236/ad0294819
[research_leng_wang_2024]: https://doi.org/10.1016/j.energy.2024.132076
[research_leonard_amundsen_2005]: https://doi.org/10.2514/6.2005-3438
[research_lepsch_naftel_1992]: https://ntrs.nasa.gov/citations/19920066411
[research_lepsch_naftel_1993]: https://doi.org/10.2514/3.26368
[research_lepsch_stanley_1991]: https://doi.org/10.2514/3.26281
[research_lernerji_mcintoshscjr_1968]: https://ntrs.nasa.gov/citations/19710005866
[research_levensteins_krumins_1967]: https://doi.org/10.2514/3.4256
[research_levermore_brio_1994]: https://doi.org/10.21236/ada295493
[research_levin_2015]: https://doi.org/10.2514/5.9781624103292.0159.0202
[research_lewis_1993]: https://doi.org/10.2514/3.23624
[research_lewis_2003]: https://doi.org/10.2514/6.2003-7020
[research_lewis_burgess_1963]: https://doi.org/10.21236/ad0409870
[research_lewis_hastings_1989]: https://doi.org/10.2514/3.23200
[research_lgfritzemeier_majacinto_1990]: https://ntrs.nasa.gov/citations/19910044166
[research_li_2020]: https://doi.org/10.1515/htmp-2020-0044
[research_li_2020_b]: https://doi.org/10.1080/09276440.2020.1775016
[research_li_2021]: https://doi.org/10.1016/j.compstruct.2020.113297
[research_li_2022]: https://doi.org/10.1016/j.actaastro.2021.10.019
[research_li_2022_b]: https://doi.org/10.1063/5.0074757
[research_li_cao_2022]: https://doi.org/10.1016/j.ast.2022.107737
[research_li_chen_2019]: https://doi.org/10.1016/j.ijhydene.2019.09.023
[research_li_chen_2022]: https://doi.org/10.1016/j.cja.2021.07.039
[research_li_choudhari_2022]: https://doi.org/10.1007/s00162-021-00599-3
[research_li_feng_2026]: https://doi.org/10.1016/j.ast.2025.111490
[research_li_hong_2014]: https://doi.org/10.4028/www.scientific.net/amm.644-650.1470
[research_li_huang_2018]: https://doi.org/10.2514/1.j056723
[research_li_huang_2020]: https://doi.org/10.1016/j.energy.2020.116920
[research_li_huang_2024]: https://doi.org/10.3390/aerospace11110886
[research_li_ji_2025]: https://doi.org/10.1063/5.0292927
[research_li_ji_2026]: https://doi.org/10.1109/access.2026.3667479
[research_li_jiao_2018]: https://doi.org/10.1080/00102202.2018.1472086
[research_li_jiao_2019]: https://doi.org/10.1016/j.actaastro.2018.11.035
[research_li_jiao_2026]: https://doi.org/10.1016/j.ast.2025.111255
[research_li_jin_2017]: https://doi.org/10.1080/00102202.2017.1376190
[research_li_jin_2021]: https://doi.org/10.1016/j.jaap.2021.105084
[research_li_ladeinde_2019]: https://doi.org/10.2514/6.2019-4272
[research_li_leng_2023]: https://doi.org/10.1016/j.icheatmasstransfer.2022.106514
[research_li_li_2018]: https://doi.org/10.1021/acs.energyfuels.8b00531
[research_li_li_2022]: https://doi.org/10.1109/access.2021.3136612
[research_li_li_2023]: https://doi.org/10.1016/j.ast.2023.108362
[research_li_li_2024]: https://doi.org/10.1016/j.actaastro.2023.12.001
[research_li_li_2025]: https://doi.org/10.1063/5.0293232
[research_li_liao_2019]: https://doi.org/10.1016/j.energy.2019.116017
[research_li_lin_2022]: https://doi.org/10.3390/app12136590
[research_li_liu_2017]: https://doi.org/10.1016/j.actaastro.2017.05.036
[research_li_liu_2018]: https://doi.org/10.3724/sp.j.1123.2018.02030
[research_li_liu_2018_b]: https://doi.org/10.1016/j.actaastro.2017.12.018
[research_li_liu_2021]: https://doi.org/10.1016/j.applthermaleng.2020.116108
[research_li_liu_2025]: https://doi.org/10.1063/5.0298885
[research_li_luo_2012]: https://doi.org/10.4028/www.scientific.net/amr.601.294
[research_li_pan_2025]: https://doi.org/10.1016/j.compfluid.2025.106781
[research_li_pang_2026]: https://doi.org/10.1016/j.ast.2025.110815
[research_li_qin_2019]: https://doi.org/10.1016/j.actaastro.2018.11.021
[research_li_ren_2025]: https://doi.org/10.1016/j.ast.2024.109436
[research_li_reynaud_2021]: https://doi.org/10.1080/09276440.2021.1960678
[research_li_song_2012]: https://doi.org/10.5539/mas.v6n5p73
[research_li_song_2014]: https://doi.org/10.1016/j.actaastro.2013.11.016
[research_li_song_2015]: https://doi.org/10.1007/s12046-014-0310-1
[research_li_su_2025]: https://doi.org/10.2514/1.j064262
[research_li_sun_2018]: https://doi.org/10.1016/j.applthermaleng.2018.07.055
[research_li_sun_2023]: https://doi.org/10.3390/aerospace10060506
[research_li_sun_2024]: https://doi.org/10.3390/aerospace11070553
[research_li_wan_2024]: https://doi.org/10.3390/aerospace11070572
[research_li_wang_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000747
[research_li_wang_2017_b]: https://doi.org/10.1016/j.ast.2017.02.021
[research_li_wang_2019]: https://doi.org/10.1080/00102202.2019.1594800
[research_li_wang_2021]: https://doi.org/10.1016/j.ces.2021.116806
[research_li_wang_2022]: https://doi.org/10.3390/aerospace9060300
[research_li_wang_2023]: https://doi.org/10.1016/j.fuel.2023.128659
[research_li_wang_2024]: https://doi.org/10.2298/tsci231223114l
[research_li_wang_2024_b]: https://doi.org/10.1016/j.energy.2024.134084
[research_li_wang_2025]: https://doi.org/10.2514/1.j065602
[research_li_wang_2025_b]: https://doi.org/10.1016/j.energy.2025.137326
[research_li_wey_1988]: https://ntrs.nasa.gov/citations/19880057367
[research_li_xia_2023]: https://doi.org/10.1016/j.energy.2022.126400
[research_li_xie_2020]: https://doi.org/10.1016/j.applthermaleng.2020.115695
[research_li_xu_2022]: https://doi.org/10.2514/1.b38539
[research_li_xu_2025]: https://doi.org/10.3390/aerospace12040280
[research_li_yang_1993]: https://doi.org/10.1016/0008-6223(93)90102-g
[research_li_yang_2016]: https://doi.org/10.1155/2016/9407238
[research_li_yang_2017]: https://doi.org/10.2514/6.2017-2328
[research_li_yang_2020]: https://doi.org/10.1016/j.corsci.2019.108231
[research_li_yang_2026]: https://doi.org/10.1016/j.ast.2025.111088
[research_li_yu_2009]: https://doi.org/10.2514/6.2009-7300
[research_li_yue_2022]: https://doi.org/10.3390/aerospace9100625
[research_li_z_2019]: https://doi.org/10.19070/2470-4415-1900023
[research_li_zeng_2022]: https://doi.org/10.2514/1.j061355
[research_li_zeng_2024]: https://doi.org/10.1088/1742-6596/2882/1/012089
[research_li_zhang_2018]: https://doi.org/10.1515/tjj-2016-0052
[research_li_zhang_2025]: https://doi.org/10.1007/s42405-025-00941-7
[research_li_zhang_2026]: https://doi.org/10.1016/j.ast.2025.111328
[research_li_zhao_2024]: https://doi.org/10.1016/j.combustflame.2024.113725
[research_li_zheng_2023]: https://doi.org/10.1061/jaeeez.aseng-4966
[research_lian_tang_2023]: https://doi.org/10.1063/5.0171442
[research_lian_xiong_2025]: https://doi.org/10.1088/1742-6596/3085/1/012011
[research_liang_guo_2024]: https://doi.org/10.1063/5.0187459
[research_liang_huang_2022]: https://doi.org/10.1063/5.0120400
[research_liang_liu_2016]: https://doi.org/10.2514/1.t4704
[research_liang_xu_2022]: https://doi.org/10.1016/j.ast.2022.107855
[research_liao_chu_2023]: https://doi.org/10.1016/j.cja.2023.11.020
[research_liao_song_2023]: https://doi.org/10.1061/jaeeez.aseng-4668
[research_libby_1962]: https://doi.org/10.2514/8.6033
[research_libby_fox_1963]: https://doi.org/10.2514/3.2167
[research_libby_fox_1963_b]: https://doi.org/10.2514/6.1963-115
[research_lidke_poulin_1987]: https://doi.org/10.2514/6.1987-1815
[research_lillardrandolphp_oliverabrandon_2011]: https://ntrs.nasa.gov/citations/20110024207
[research_lilley_pengelly_1993]: https://doi.org/10.2514/3.23700
[research_limerick_1991]: https://doi.org/10.2514/3.23290
[research_limerick_1994]: https://doi.org/10.2514/6.1994-3161
[research_liming_bing_2006]: https://doi.org/10.2514/6.iac-06-c2.p.2.06
[research_lin_baumann_2008]: https://ntrs.nasa.gov/citations/20090005180
[research_lin_shen_1997]: https://doi.org/10.1016/s0045-7930(96)00026-6
[research_lipanov_karskanov_2024]: https://doi.org/10.20537/nd240803
[research_lisagor_1990]: https://ntrs.nasa.gov/citations/19910031409
[research_lisiecki_2015]: https://doi.org/10.3390/met5010054
[research_lissenden_yalcin_2019]: https://doi.org/10.1201/9780367812720-33
[research_litchfordrj_colejw_2000]: https://ntrs.nasa.gov/citations/20000095934
[research_litchfordronj_bityurinvalentinea_1999]: https://ntrs.nasa.gov/citations/20000032786
[research_littlete_1992]: https://ntrs.nasa.gov/citations/19920016677
[research_liu_1967]: https://doi.org/10.1016/0017-9310(67)90184-6
[research_liu_2020]: https://doi.org/10.1088/1742-6596/1509/1/012006
[research_liu_baccarella_2019]: https://doi.org/10.1016/j.proci.2018.08.037
[research_liu_baccarella_2020]: https://doi.org/10.1016/j.paerosci.2020.100636
[research_liu_chen_2002]: https://doi.org/10.21236/ada403577
[research_liu_chen_2022]: https://doi.org/10.3390/aerospace9120811
[research_liu_dong_2019]: https://doi.org/10.3850/978-981-11-2730-4_0126-cd
[research_liu_dong_2023]: https://doi.org/10.1063/5.0165938
[research_liu_fan_2019]: https://doi.org/10.1016/j.actaastro.2019.04.041
[research_liu_han_2023]: https://doi.org/10.1016/j.energy.2023.129003
[research_liu_kang_2022]: https://doi.org/10.1016/j.actaastro.2022.01.030
[research_liu_kuang_2024]: https://doi.org/10.1515/tjj-2024-0047
[research_liu_li_2025]: https://doi.org/10.1007/s00348-025-03967-5
[research_liu_liu_2015]: https://doi.org/10.1016/b978-0-12-800054-0.00027-7
[research_liu_liu_2016]: https://doi.org/10.1016/j.actaastro.2015.10.015
[research_liu_liu_2016_b]: https://doi.org/10.1016/j.actaastro.2015.10.011
[research_liu_liu_2021]: https://doi.org/10.1016/j.ceramint.2021.05.080
[research_liu_liu_2023]: https://doi.org/10.1061/jaeeez.aseng-4711
[research_liu_lu_2024]: https://doi.org/10.3390/drones8090505
[research_liu_luo_2023]: https://doi.org/10.3390/aerospace10090766
[research_liu_pan_2024]: https://doi.org/10.1016/j.fuel.2023.129466
[research_liu_peng_2024]: https://doi.org/10.1063/5.0227619
[research_liu_sheng_1995]: https://doi.org/10.1007/bf01416034
[research_liu_sogame_1969]: https://doi.org/10.2514/3.5334
[research_liu_sun_2023]: https://doi.org/10.1016/j.cja.2023.04.013
[research_liu_tian_2026]: https://doi.org/10.1016/j.cja.2026.104327
[research_liu_tong_2019]: https://doi.org/10.1177/1461348419835131
[research_liu_wang_2019]: https://doi.org/10.1007/978-3-319-91017-8_22
[research_liu_wang_2021]: https://doi.org/10.1142/s021798492150500x
[research_liu_wang_2024]: https://doi.org/10.1063/5.0234745
[research_liu_wang_2025]: https://doi.org/10.1063/5.0295650
[research_liu_wu_2022]: https://doi.org/10.1063/5.0123724
[research_liu_xu_2021]: https://doi.org/10.1063/5.0033183
[research_liu_yan_2018]: https://doi.org/10.1016/j.actaastro.2018.07.011
[research_liu_yang_2023]: https://doi.org/10.1016/j.cja.2022.09.024
[research_liu_yang_2025]: https://doi.org/10.2514/1.j063776
[research_liu_yuan_2015]: https://doi.org/10.1016/j.jppr.2015.07.006
[research_liu_yuan_2017]: https://doi.org/10.1016/j.ast.2016.11.005
[research_liu_yuan_2017_b]: https://doi.org/10.1016/j.ast.2017.07.020
[research_liu_yuan_2021]: https://doi.org/10.1016/j.ast.2021.106894
[research_liu_yuan_2022]: https://doi.org/10.3390/aerospace9110685
[research_liu_zhang_2019]: https://doi.org/10.4208/aamm.2018.s01
[research_liu_zhang_2024]: https://doi.org/10.1016/j.ast.2024.109710
[research_liu_zhang_2025]: https://doi.org/10.1063/5.0282257
[research_liu_zhang_2026]: https://doi.org/10.1016/j.applthermaleng.2026.130674
[research_liu_zhao_2017]: https://doi.org/10.1016/j.actaastro.2017.03.010
[research_liu_zheng_2026]: https://doi.org/10.1142/s2301385028500276
[research_livingston_1965]: https://ntrs.nasa.gov/citations/19650009668
[research_lloyd_1959]: https://doi.org/10.1016/0010-2180(59)90027-6
[research_lobb_winkler_1955]: https://doi.org/10.21236/ad0068499
[research_lockman_lawrence_1990]: https://ntrs.nasa.gov/citations/19930073133
[research_lockwood_petley_1996]: https://ntrs.nasa.gov/citations/19960016113
[research_loehle_2016]: https://doi.org/10.2514/6.2016-3205
[research_loiseau_robinet_2015]: https://doi.org/10.1016/j.piutam.2015.03.039
[research_lombard_ghosh_1999]: https://doi.org/10.1557/proc-601-73
[research_lominac_boytos_1998]: https://doi.org/10.21236/ada370970
[research_lomo_patel_2023]: https://doi.org/10.1016/j.addma.2023.103891
[research_loney_1994]: https://ntrs.nasa.gov/citations/19950016889
[research_longbiao_2016]: https://doi.org/10.1007/s10443-016-9535-y
[research_longbiao_2018]: https://doi.org/10.1080/09276440.2018.1488490
[research_longbiao_2019]: https://doi.org/10.1080/09276440.2019.1637196
[research_longbiao_2019_b]: https://doi.org/10.1080/09276440.2019.1685281
[research_longbiao_2019_c]: https://doi.org/10.1080/09276440.2019.1667194
[research_longstaff_1995]: https://doi.org/10.2514/6.1995-6074
[research_longwell_weiss_1952]: https://doi.org/10.21236/ad0041743
[research_lonkar_panda_2026]: https://doi.org/10.1016/j.ast.2026.112194
[research_loomismarkp_1994]: https://ntrs.nasa.gov/citations/19950005525
[research_lord_boersen_1960]: https://doi.org/10.21236/ada952043
[research_lovelltalan_schmidtdk_1994]: https://ntrs.nasa.gov/citations/19940023286
[research_low_cycle_2000]: https://doi.org/10.1016/0026-0657(00)93555-0
[research_lu_gang_2026]: https://doi.org/10.1016/j.ast.2026.111837
[research_lu_sheng_2025]: https://doi.org/10.1016/j.fuel.2024.134216
[research_lu_zhang_2024]: https://doi.org/10.1016/j.enconman.2023.117913
[research_lu_zhang_2025]: https://doi.org/10.3390/math13030380
[research_lu_zhansen_2015]: https://doi.org/10.1016/j.proeng.2014.12.540
[research_lu_zhou_2017]: https://doi.org/10.1177/0142331217735050
[research_lu_zhu_2025]: https://doi.org/10.1016/j.applthermaleng.2025.126811
[research_lubbock_luque_2018]: https://doi.org/10.1115/1.4038339
[research_ludwig_sulzmann_1961]: https://doi.org/10.21236/ad0257971
[research_lukasiewicz_1961]: https://doi.org/10.21236/ad0259455
[research_lumpkin_chapman_1992]: https://doi.org/10.2514/3.377
[research_luo_chen_2026]: https://doi.org/10.1016/j.applthermaleng.2026.133184
[research_luo_li_2025]: https://doi.org/10.1016/j.applthermaleng.2025.127298
[research_luo_liu_2024]: https://doi.org/10.1360/sspma-2023-0126
[research_luo_luo_2025]: https://doi.org/10.1016/j.renene.2025.123606
[research_luo_miao_2021]: https://doi.org/10.3389/fenrg.2021.756820
[research_luo_qi_2024]: https://doi.org/10.3390/en17236003
[research_luo_qu_2024]: https://doi.org/10.1016/j.tsep.2024.102775
[research_luo_song_2012]: https://doi.org/10.1016/s1000-9361(11)60375-0
[research_luo_sun_2022]: https://doi.org/10.1016/j.ast.2022.107964
[research_luo_sun_2025]: https://doi.org/10.1016/j.combustflame.2025.113999
[research_luo_tang_2026]: https://doi.org/10.1016/j.icheatmasstransfer.2026.111984
[research_luo_wang_2019]: https://doi.org/10.3850/978-981-11-2730-4_0240-cd
[research_luo_wang_2020]: https://doi.org/10.1016/j.ast.2020.105958
[research_luping_1993]: https://ntrs.nasa.gov/citations/19940012025
[research_lusty_miele_1966]: https://doi.org/10.2514/3.3866
[research_luxbaumann_burkes_2006]: https://ntrs.nasa.gov/citations/20090007796
[research_luxbaumann_dees_2006]: https://ntrs.nasa.gov/citations/20060027798
[research_lv_chang_2020]: https://doi.org/10.1016/j.rineng.2020.100161
[research_lv_chang_2022]: https://doi.org/10.1016/j.jppr.2022.02.003
[research_lv_huang_2023]: https://doi.org/10.1016/j.energy.2023.126718
[research_lv_li_2026]: https://doi.org/10.1016/j.ast.2026.112379
[research_lv_wang_2015]: https://doi.org/10.1016/j.proeng.2015.11.192
[research_lv_xu_2020]: https://doi.org/10.1016/j.ast.2020.106265
[research_lv_xu_2022]: https://doi.org/10.1016/j.energy.2022.125324
[research_lynch_grasser_2023]: https://doi.org/10.1007/s00193-023-01127-4
[research_lyu_gao_2021]: https://doi.org/10.1016/j.ast.2021.106546
[research_ma_cai_2018]: https://doi.org/10.1109/access.2017.2780118
[research_ma_cai_2018_b]: https://doi.org/10.1061/(asce)as.1943-5525.0000856
[research_ma_chang_2019]: https://doi.org/10.1016/j.ast.2018.12.012
[research_ma_chang_2019_b]: https://doi.org/10.1016/j.ast.2019.04.027
[research_ma_fu_2026]: https://doi.org/10.3390/aerospace13080663
[research_ma_guo_2025]: https://doi.org/10.1016/j.apenergy.2025.125362
[research_ma_jiang_2022]: https://doi.org/10.1016/j.applthermaleng.2022.118867
[research_ma_jiang_2023]: https://doi.org/10.1016/j.energy.2023.128540
[research_ma_shu_2025]: https://doi.org/10.1016/j.energy.2025.139462
[research_ma_sun_2021]: https://doi.org/10.1016/j.actaastro.2021.02.020
[research_ma_yang_2024]: https://doi.org/10.1016/j.ast.2024.108969
[research_ma_yang_2024_b]: https://doi.org/10.1155/2024/5557153
[research_ma_yin_2017]: https://doi.org/10.2514/6.2017-2151
[research_ma_zhao_2025]: https://doi.org/10.2514/1.j065087
[research_ma_zhao_2026]: https://doi.org/10.1016/j.combustflame.2025.114721
[research_maahs_1989]: https://ntrs.nasa.gov/citations/19900016764
[research_maccormackrobertw_candlergrahamv_1988]: https://ntrs.nasa.gov/citations/19890026829
[research_macdermott_dix_1965]: https://doi.org/10.21236/ad0467446
[research_macheret_shneider_2005]: https://doi.org/10.2514/6.2005-5371
[research_mack_steelant_2009]: https://doi.org/10.1007/978-3-540-85168-4_99
[research_mackinnon_beitel_2004]: https://doi.org/10.2514/6.2004-2594
[research_macleod_2026]: https://doi.org/10.59332/jbis-079-01-0017
[research_macleod_gibson_2025]: https://doi.org/10.59332/jbis-078-09-0308
[research_maddalon_1969]: https://doi.org/10.2514/3.5549
[research_maglieridomenicj_sothcottvictore_1990]: https://ntrs.nasa.gov/citations/19910029827
[research_magnus_sharp_2020]: https://doi.org/10.1016/j.ceramint.2020.05.151
[research_mahto_choubey_2016]: https://doi.org/10.1016/j.actaastro.2016.08.010
[research_maikap_rajagopal_2024]: https://doi.org/10.1063/5.0185787
[research_maiorova_prosuntsov_2016]: https://doi.org/10.1007/s10891-016-1406-8
[research_maisaia_2023]: https://doi.org/10.2514/6.2023-3234
[research_maita_ohkami_1990]: https://doi.org/10.2514/6.1990-5225
[research_makurunje_sigalas_2021]: https://doi.org/10.1016/j.jeurceramsoc.2020.08.048
[research_malakhov_2025]: https://doi.org/10.1007/s11085-025-10355-1
[research_malakondaiah_nicholas_1996]: https://doi.org/10.1007/bf02651878
[research_malekipour_mohammadiamin_2021]: https://doi.org/10.1061/(asce)as.1943-5525.0001296
[research_malik_anderson_1991]: https://doi.org/10.1063/1.858012
[research_mall_cunningham_2007]: https://doi.org/10.1016/j.compstruct.2006.02.032
[research_malonemichaelb_peaveycharlesc_1999]: https://ntrs.nasa.gov/citations/20000044629
[research_mandelg_carpenterjljr_1977]: https://ntrs.nasa.gov/citations/19770000080
[research_mann_garner_1977]: https://doi.org/10.21236/ada040707
[research_manna_dharavath_2023]: https://doi.org/10.61653/joast.v61i4.2009.589
[research_mannion_ko_2026]: https://doi.org/10.2514/1.t7258
[research_mannion_ko_2026_b]: https://doi.org/10.2514/1.t7150
[research_manocha_manocha_1995]: https://doi.org/10.1016/0008-6223(94)00168-y
[research_manski_hagemann_1997]: https://doi.org/10.1016/s0094-5765(97)00119-7
[research_manski_martin_1991]: https://doi.org/10.2514/3.23411
[research_mao_zhang_2016]: https://doi.org/10.1007/s00500-016-2201-3
[research_marchetti_minisci_2021]: https://doi.org/10.1007/s11081-021-09698-w
[research_marcum_2001]: https://doi.org/10.21236/ada387492
[research_mareklindsayc_2011]: https://ntrs.nasa.gov/citations/20110024073
[research_marie_hideyuki_2019]: https://doi.org/10.3850/978-981-11-2730-4_0276-cd
[research_marley_driscoll_2022]: https://doi.org/10.2514/1.c036411
[research_marschall_2011]: https://doi.org/10.21236/ada553782
[research_marsh_sears_1954]: https://doi.org/10.2514/8.6480
[research_marshall_1969]: https://ntrs.nasa.gov/citations/19700042333
[research_marshall_bahm_2005]: https://ntrs.nasa.gov/citations/20050175679
[research_marshall_corpening_2005]: https://ntrs.nasa.gov/citations/20050175770
[research_marshall_cox_2014]: https://doi.org/10.21236/ada609952
[research_marshall_morris_1996]: https://doi.org/10.1520/stp18218s
[research_martin_1978]: https://doi.org/10.2514/3.57314
[research_martin_1992]: https://doi.org/10.2514/3.55636
[research_martin_1995]: https://doi.org/10.2514/3.23845
[research_martin_boyd_2015]: https://doi.org/10.2514/1.a32847
[research_martin_kabis_1991]: https://doi.org/10.2514/6.1991-5016
[research_martinaw_1977]: https://ntrs.nasa.gov/citations/19770008083
[research_martinezschramm_karl_2008]: https://doi.org/10.2514/6.2008-2547
[research_martinezschramm_wagner_2024]: https://doi.org/10.17815/jlsrf-9-188
[research_marvinjg_1991]: https://ntrs.nasa.gov/citations/19910016035
[research_marvinjosephg_brownjamesl_2013]: https://ntrs.nasa.gov/citations/20140010683
[research_masad_1995]: https://doi.org/10.1115/1.2817329
[research_masahashi_mizuhara_1991]: https://doi.org/10.2355/isijinternational.31.728
[research_matarrese_messiter_1991]: https://doi.org/10.2514/3.10846
[research_materials_structures_2022]: https://doi.org/10.1002/9781119640646.ch9
[research_mathavaraj_padhi_2020]: https://doi.org/10.1142/s230138502050003x
[research_mathur_singh_2024]: https://doi.org/10.22214/ijraset.2024.65672
[research_matikas_2008]: https://doi.org/10.1163/156855408784514757
[research_matsuda_2015]: https://doi.org/10.1299/jsmefed.2015._0809-1_
[research_matsui_shinmi_2008]: https://doi.org/10.2514/6.2008-4133
[research_matsushima_takanashi_1987]: https://ntrs.nasa.gov/citations/19880016248
[research_mattern_1992]: https://ntrs.nasa.gov/citations/19930038343
[research_matthewmcgilvray_2024]: https://doi.org/10.14264/155369
[research_matthews_trimmer_1969]: https://doi.org/10.21236/ad0854309
[research_matveev_leachman_2023]: https://doi.org/10.3390/hydrogen4010010
[research_matveev_leachman_2023_b]: https://doi.org/10.3390/hydrogen4030030
[research_maurice_leingang_1996]: https://doi.org/10.2514/3.24030
[research_maus_griffith_1984]: https://doi.org/10.2514/3.8624
[research_maxwell_goodwin_2017]: https://doi.org/10.2514/6.2017-1385
[research_maxwell_hoang_2016]: https://doi.org/10.2514/6.2016-4149
[research_mayer_paynter_1994]: https://doi.org/10.2514/3.12120
[research_mayer_paynter_1995]: https://doi.org/10.2514/3.12418
[research_mayhew_norden_1995]: https://doi.org/10.2514/6.1995-2748
[research_mbagwu_dalle_2023]: https://doi.org/10.2514/1.c037186
[research_mccandless_cruz_1985]: https://doi.org/10.2514/6.1985-346
[research_mcclinton_1976]: https://ntrs.nasa.gov/citations/19760035792
[research_mcclinton_1978]: https://ntrs.nasa.gov/citations/19780015151
[research_mcclinton_bittner_1990]: https://ntrs.nasa.gov/citations/19910029849
[research_mcclinton_ferlemann_2002]: https://ntrs.nasa.gov/citations/20020023450
[research_mcclinton_gooderum_1977]: https://ntrs.nasa.gov/citations/19780030345
[research_mcclinton_holland_1998]: https://ntrs.nasa.gov/citations/19980047114
[research_mcclinton_rondakov_1991]: https://ntrs.nasa.gov/citations/20040110897
[research_mcclinton_voland_1998]: https://doi.org/10.2514/6.1998-2866
[research_mcclintoncr_andersongy_1980]: https://ntrs.nasa.gov/citations/19810004547
[research_mcclintoncr_torrencemg_1975]: https://ntrs.nasa.gov/citations/19760006009
[research_mcclure_andrews_1998]: https://doi.org/10.2514/6.1998-5180
[research_mcclure_sirbaugh_1991]: https://doi.org/10.21236/ada232101
[research_mccormick_wakayama_2010]: https://doi.org/10.2514/6.2010-8906
[research_mcdaniel_2003]: https://doi.org/10.2514/6.2003-6960
[research_mcdaniel_2005]: https://doi.org/10.1063/1.1941709
[research_mcdaniel_edwards_1999]: https://doi.org/10.2514/6.1999-3411
[research_mcdaniel_edwards_2001]: https://doi.org/10.2514/6.2001-382
[research_mcdanieljr_1998]: https://doi.org/10.2514/6.1998-1646
[research_mcgann_carter_2026]: https://doi.org/10.1016/j.proci.2026.106148
[research_mcgann_lee_2019]: https://doi.org/10.2514/1.b37204
[research_mcgilvray_jacobs_2006]: https://doi.org/10.2514/6.2006-8143
[research_mcgilvray_kirchhartz_2010]: https://doi.org/10.2514/1.j050025
[research_mcgilvray_neely_2019]: https://doi.org/10.2514/6.2019-1680
[research_mcgrory_2001]: https://doi.org/10.21236/ada399497
[research_mcintosh_1973]: https://doi.org/10.2514/3.50432
[research_mcintoshscjr_1972]: https://ntrs.nasa.gov/citations/19720041708
[research_mcintyre_bishop_1998]: https://doi.org/10.2514/6.1998-2772
[research_mckee_1987]: https://doi.org/10.1016/0008-6223(87)90197-7
[research_mcnelisnancyb_hardyterryl_1995]: https://ntrs.nasa.gov/citations/19950017766
[research_mcrae_edwards_2001]: https://doi.org/10.21236/ada399718
[research_mcrae_neaves_1998]: https://doi.org/10.21236/ada336232
[research_mcrae_zikry_1999]: https://doi.org/10.21236/ada378084
[research_mctaggart_1973]: https://doi.org/10.21236/ad0769043
[research_mcvey_rejeske_1969]: https://doi.org/10.21236/ad0861763
[research_mdsalleh_2026]: https://doi.org/10.24191/jmeche.v23i1.6123
[research_mease_1993]: https://doi.org/10.1016/b978-0-08-041715-8.50071-7
[research_mease_vanburen_1994]: https://doi.org/10.1016/0005-1098(94)90046-9
[research_mease_vinh_1988]: https://doi.org/10.2514/6.1988-4341
[research_measekennethd_vanburenmarka_1989]: https://ntrs.nasa.gov/citations/19900004053
[research_measurement_techniques_1974]: https://doi.org/10.2514/5.9781600865077.0263.0282
[research_mechanical_and_1995]: https://doi.org/10.1016/s0026-0657(99)80945-x
[research_medina_patel_2021]: https://doi.org/10.2514/6.2021-4096
[research_medvedev_agafonov_2016]: https://doi.org/10.1016/j.actaastro.2016.04.019
[research_mee_daniel_1995]: https://ntrs.nasa.gov/citations/19950018980
[research_meelanchoudhari_feili_2021]: https://ntrs.nasa.gov/citations/20205010368
[research_mehta_1990]: https://doi.org/10.2514/6.1990-5248
[research_mehta_1992]: https://ntrs.nasa.gov/citations/20000024793
[research_mehta_1993]: https://doi.org/10.2514/3.46374
[research_mehta_bowles_2001]: https://ntrs.nasa.gov/citations/20010041080
[research_mehta_kutler_1994]: https://ntrs.nasa.gov/citations/20020010588
[research_mehtau_1995]: https://ntrs.nasa.gov/citations/19950058869
[research_mehtaunmeelb_1994]: https://ntrs.nasa.gov/citations/19950008507
[research_mehtaunmeelb_bogdanoffdavidw_2001]: https://ntrs.nasa.gov/citations/20010048659
[research_mei_shi_2020]: https://doi.org/10.1016/j.mtcomm.2019.100773
[research_meiss_schroder_2011]: https://doi.org/10.2514/6.2011-2346
[research_melis_gladden_1990]: https://ntrs.nasa.gov/citations/19910029831
[research_melis_wang_1999]: https://ntrs.nasa.gov/citations/19990116904
[research_melnikwl_perinill_1968]: https://ntrs.nasa.gov/citations/19680040420
[research_mendham_2003]: https://doi.org/10.2514/6.iac-03-v.p.11
[research_mendiratta_choudhury_1978]: https://doi.org/10.21236/ada060386
[research_menees_bowles_1989]: https://ntrs.nasa.gov/citations/19900030386
[research_meng_jin_2024]: https://doi.org/10.3390/aerospace11110941
[research_meng_shi_2022]: https://doi.org/10.1063/5.0077734
[research_meng_sun_2022]: https://doi.org/10.3390/aerospace9120826
[research_meng_sun_2024]: https://doi.org/10.1063/5.0193282
[research_meng_wan_2021]: https://doi.org/10.1016/j.cja.2020.03.028
[research_meng_ye_2020]: https://doi.org/10.1016/j.actaastro.2019.09.035
[research_menon_ck_2025]: https://doi.org/10.1007/s11038-025-09574-y
[research_menon_jou_1991]: https://doi.org/10.1080/00102209108924078
[research_meritt_schetz_2014]: https://doi.org/10.2514/6.2014-2800
[research_merkli_1975]: https://doi.org/10.21236/ada033630
[research_merkli_1976]: https://doi.org/10.2514/3.61352
[research_meshcheryakov_sabelnikov_1988]: https://doi.org/10.1007/bf00755488
[research_meshcheryakov_yashina_2015]: https://doi.org/10.1615/tsagiscij.v46.i5.40
[research_metghalchi_2009]: https://doi.org/10.21236/ada516408
[research_method_and_1993]: https://doi.org/10.1016/0010-4361(93)90323-z
[research_method_for_1991]: https://doi.org/10.1016/0010-4361(91)90657-3
[research_method_for_1997]: https://doi.org/10.1016/s1359-4311(97)88055-6
[research_method_of_1978]: https://doi.org/10.1016/0010-4361(78)90578-5
[research_method_to_1990]: https://doi.org/10.1016/0010-4361(90)90212-f
[research_method_to_1994]: https://doi.org/10.1016/0010-4361(94)90055-8
[research_meuwly_2014]: https://doi.org/10.21236/ada611797
[research_meyer_1959]: https://doi.org/10.2514/8.4717
[research_meyers_feller_1974]: https://ntrs.nasa.gov/citations/19760027473
[research_miao_wang_2020]: https://doi.org/10.1016/j.applthermaleng.2019.114774
[research_miao_wang_2026]: https://doi.org/10.1016/j.ast.2026.113155
[research_michalski_boust_2018]: https://doi.org/10.2514/6.2018-4478
[research_micoljr_1998]: https://ntrs.nasa.gov/citations/20040088542
[research_microstructural_control_1997]: https://doi.org/10.1016/s0026-0657(97)87116-0
[research_middenraymonde_millercharlesgiii_1985]: https://ntrs.nasa.gov/citations/19870020345
[research_middletontroyf_ballarobertjeffrey_2011]: https://ntrs.nasa.gov/citations/20110011132
[research_miele_1990]: https://ntrs.nasa.gov/citations/19910006697
[research_miele_hull_1963]: https://doi.org/10.21236/ad0404858
[research_miele_pritchard_1963]: https://doi.org/10.21236/ad0403460
[research_migdal_greathouse_1968]: https://doi.org/10.4271/680294
[research_miller_2000]: https://ntrs.nasa.gov/citations/20000061448
[research_miller_steinetz_1993]: https://ntrs.nasa.gov/citations/19930049919
[research_millerd_2025]: https://doi.org/10.14264/fc09cc4
[research_min_son_2026]: https://doi.org/10.2139/ssrn.7042880
[research_mirdamadi_johnson_1994]: https://ntrs.nasa.gov/citations/19950005502
[research_miromiro_pinna_2017]: https://doi.org/10.2514/6.2017-4518
[research_mishra_mukherjee_1996]: https://doi.org/10.1016/1359-6462(96)00047-4
[research_mitani_1995]: https://doi.org/10.1016/0010-2180(94)00218-h
[research_mitani_1996]: https://doi.org/10.1016/s0082-0784(96)80133-0
[research_mitani_hiraiwa_1996]: https://doi.org/10.2514/6.1996-4555
[research_mitani_hiraiwa_1997]: https://doi.org/10.2514/2.5228
[research_mitani_kouchi_2005]: https://doi.org/10.1016/j.combustflame.2004.10.004
[research_miyashita_sugihara_2025]: https://doi.org/10.1063/5.0250348
[research_mizener_lu_2017]: https://doi.org/10.2514/1.b36432
[research_modroukas_betti_1998]: https://doi.org/10.2514/6.1998-2496
[research_mogavero_brown_2018]: https://doi.org/10.2514/1.a33676
[research_mohamad_ivan_2024]: https://doi.org/10.1016/j.fuel.2024.132227
[research_mohling_2018]: https://doi.org/10.31274/rtd-180814-3937
[research_mohring_gabler_2021]: https://doi.org/10.1109/map.2020.3003226
[research_mohsen_yusoff_2017]: https://doi.org/10.1007/s00193-017-0758-0
[research_moin_lele_1998]: https://doi.org/10.21236/ada343835
[research_molchanov_gribinenko_2021]: https://doi.org/10.34759/tpt-2021-13-4-148-154
[research_molder_szpiro_1966]: https://doi.org/10.2514/3.28649
[research_molvik_bowles_1992]: https://ntrs.nasa.gov/citations/19920066360
[research_molvik_bowles_1993]: https://ntrs.nasa.gov/citations/19930039259
[research_molvik_bowles_1993_b]: https://doi.org/10.2514/6.1993-5097
[research_monaghan_1959]: https://doi.org/10.1017/s0368393100071595
[research_mondal_jagtap_2026]: https://doi.org/10.1063/5.0324870
[research_monroe_boyd_2026]: https://doi.org/10.2514/6.2026-2645
[research_montagnejl_yeehc_1988]: https://ntrs.nasa.gov/citations/19880008960
[research_monteirodossantosrodriguesdasilva_leite_2025]: https://doi.org/10.26678/abcm.cobem2023.cob2023-1036
[research_moon_chung_1996]: https://doi.org/10.2514/6.1996-2921
[research_moon_jeung_2000]: https://doi.org/10.2514/6.2000-3706
[research_moradian_timofeev_2012]: https://doi.org/10.1007/978-3-642-25685-1_47
[research_morelli_2008]: https://ntrs.nasa.gov/citations/20080012502
[research_morelli_derry_2005]: https://ntrs.nasa.gov/citations/20050209958
[research_morgan_1961]: https://doi.org/10.21236/ad0600907
[research_morgan_paull_1985]: https://ntrs.nasa.gov/citations/19860005867
[research_morgan_paull_1986]: https://ntrs.nasa.gov/citations/19870003109
[research_morgan_stalker_1985]: https://doi.org/10.2514/6.1985-908
[research_mori_1965]: https://doi.org/10.1299/jsmemag.68.562_1587
[research_morinaga_1969]: https://doi.org/10.1246/bcsj.42.2106
[research_morris_1991]: https://doi.org/10.1016/0921-5093(91)90863-i
[research_morris_1992]: https://ntrs.nasa.gov/citations/19930021524
[research_morrisjr_1995]: https://doi.org/10.2514/6.1995-6052
[research_morrissjjr_nelmswpjr_1976]: https://ntrs.nasa.gov/citations/19770009073
[research_moses_2003]: https://ntrs.nasa.gov/citations/20040042495
[research_moses_2003_b]: https://ntrs.nasa.gov/citations/20040014996
[research_mosespl_bouchardka_1999]: https://ntrs.nasa.gov/citations/19990115467
[research_moss_perrell_2005]: https://doi.org/10.2514/6.2005-4426
[research_mossjamesn_simmondsannl_1987]: https://ntrs.nasa.gov/citations/19870035337
[research_moszee_moszee_1997]: https://doi.org/10.2514/6.1997-3395
[research_moszee_snyder_1989]: https://doi.org/10.2514/6.1989-2751
[research_mu_wang_2022]: https://doi.org/10.2514/6.2022-0203
[research_mukundan_maity_2022]: https://doi.org/10.1016/j.ifacol.2023.03.007
[research_mulard_moules_1992]: https://doi.org/10.1007/978-3-642-77922-0_81
[research_munk_vio_2016]: https://doi.org/10.4028/www.scientific.net/amm.846.494
[research_murillo_2018]: https://doi.org/10.31274/etd-180810-1331
[research_murillo_lu_2010]: https://doi.org/10.2514/6.2010-8173
[research_murray_smith_2021]: https://doi.org/10.2514/1.b38049
[research_murthy_patel_2021]: https://doi.org/10.1016/j.ceramint.2021.08.145
[research_musielak_musielak_1997]: https://doi.org/10.2514/6.1997-3268
[research_mvv_rajagopal_2026]: https://doi.org/10.1016/j.ast.2026.112894
[research_myrabo_powers_1986]: https://ntrs.nasa.gov/citations/19870034251
[research_nadellsharibeth_baumgartenwilliamj_1992]: https://ntrs.nasa.gov/citations/19920053244
[research_nadellsharibeth_baumgartenwilliamj_1992_b]: https://ntrs.nasa.gov/citations/19920012304
[research_nag_senthil_2023]: https://doi.org/10.61653/joast.v65i2.2013.721
[research_nagamatsu_1989]: https://doi.org/10.2514/6.1989-3
[research_nagamatsu_geiger_1960]: https://doi.org/10.2514/8.8494
[research_nagamatsu_graber_1964]: https://doi.org/10.21236/ad0615601
[research_nagamatsu_sheer_1961]: https://doi.org/10.21236/ad0600345
[research_nagawkar_leifsson_2022]: https://doi.org/10.1016/j.ast.2022.107449
[research_nagel_1967]: https://doi.org/10.21236/ad0661318
[research_nagel_becker_1973]: https://doi.org/10.2514/6.1973-58
[research_nair_kumar_2003]: https://doi.org/10.2514/6.2003-7067
[research_nair_suryan_2023]: https://doi.org/10.1063/5.0151676
[research_nakaya_tsue_2015]: https://doi.org/10.1016/j.combustflame.2015.07.021
[research_nakaya_yamana_2021]: https://doi.org/10.1016/j.proci.2020.07.129
[research_nance_2013]: https://doi.org/10.21236/ada571259
[research_nancerobertp_horvaththomasj_1997]: https://ntrs.nasa.gov/citations/20040105593
[research_nanda_kulkarni_2019]: https://doi.org/10.1016/j.measurement.2018.11.007
[research_narayan_1994]: https://doi.org/10.2514/6.1994-2948
[research_narayanjr_kumara_1989]: https://ntrs.nasa.gov/citations/19890037655
[research_nardo_erickson_1961]: https://doi.org/10.21236/ad0264410
[research_nardo_sadler_1962]: https://doi.org/10.21236/ad0273837
[research_nareshkumar_ikram_2017]: https://doi.org/10.1007/s11081-017-9367-0
[research_nasa_s_hypulse_2002]: https://doi.org/10.2514/5.9781600866678.0029.0071
[research_nasir_xie_2026]: https://doi.org/10.1016/j.ast.2026.111792
[research_nasp_tests_1991]: https://doi.org/10.1016/0261-3069(91)90015-v
[research_nastac_frendi_2022]: https://doi.org/10.3390/fluids7120362
[research_national_aero_space_1990]: https://ntrs.nasa.gov/citations/19940029244
[research_natural_environment_1993]: https://doi.org/10.2514/6.1993-5074
[research_naumann_ende_1991]: https://doi.org/10.1007/bf01413797
[research_naumann_ende_1992]: https://doi.org/10.2514/6.1992-3963
[research_navalordnanceteststationchinalakeca_1957]: https://doi.org/10.21236/ad0128000
[research_naved_hermann_2021]: https://doi.org/10.2514/1.j059771
[research_navo_bergada_2020]: https://doi.org/10.3390/app10228211
[research_nbs_probes_1965]: https://doi.org/10.1021/cen-v043n036.p041
[research_nealehass_karenfcabell]: https://ntrs.nasa.gov/citations/20205003306
[research_nebylov_tomita_1998]: https://doi.org/10.2514/6.1998-305
[research_neek_najarmansour_2025]: https://doi.org/10.1016/j.ijhydene.2025.152129
[research_neely_2022]: https://doi.org/10.14264/f72c588
[research_neely_morgan_1995]: https://ntrs.nasa.gov/citations/19950018979
[research_neill_pesyridis_2017]: https://doi.org/10.3390/en10111900
[research_neinergh_colegl_1978]: https://ntrs.nasa.gov/citations/19780015080
[research_nelson_mcarthur_2001]: https://ntrs.nasa.gov/citations/20010021214
[research_nelsonhg_1974]: https://ntrs.nasa.gov/citations/19740057320
[research_nelsonhowardg_1988]: https://ntrs.nasa.gov/citations/19890029406
[research_neuenhahn_olivier_2006]: https://doi.org/10.2514/6.2006-2960
[research_neumann_1990]: https://doi.org/10.2514/6.1990-1401
[research_neuwerth_peiter_1999]: https://doi.org/10.2514/2.3441
[research_next_generation_aerospace_2026]: https://doi.org/10.64643/ijirtv12i11-207245-459
[research_neyland_1993]: https://doi.org/10.2514/3.46378
[research_ng_ajmani_1989]: https://doi.org/10.2514/3.10271
[research_ng_benson_1986]: https://doi.org/10.2514/3.22900
[research_ngo_2017]: https://doi.org/10.14264/uql.2017.193
[research_ngoclong_2016]: https://doi.org/10.11648/j.ijmea.20160405.14
[research_nguyen_1987]: https://doi.org/10.2514/6.1987-448
[research_nguyen_1991]: https://doi.org/10.2514/6.1991-2740
[research_ni_lu_2016]: https://doi.org/10.3390/en9030154
[research_nicolaou_semiatin_1996]: https://doi.org/10.1007/bf02595459
[research_nicolaou_semiatin_1997]: https://doi.org/10.1007/s11661-997-1017-2
[research_nidharia_mane_2024]: https://doi.org/10.1063/5.0237684
[research_nie_he_2024]: https://doi.org/10.1016/j.ast.2024.109442
[research_nie_qin_2025]: https://doi.org/10.1016/j.actaastro.2025.01.004
[research_nie_song_2022]: https://doi.org/10.1186/s42774-022-00120-2
[research_nie_wang_2023]: https://doi.org/10.1016/j.cja.2023.05.009
[research_nie_ye_2023]: https://doi.org/10.1016/j.actaastro.2023.04.034
[research_nielsen_edwards_2021]: https://doi.org/10.2514/1.j059343
[research_nieto_samayoa_2021]: https://doi.org/10.1016/j.mtla.2021.101265
[research_nikonov_2025]: https://doi.org/10.7868/s3034612625040087
[research_nishiguchi_kodera_2025]: https://doi.org/10.3390/aerospace12010066
[research_nishioka_law_1997]: https://doi.org/10.1016/s0010-2180(96)00099-5
[research_niu_chen_2024]: https://doi.org/10.1016/j.actaastro.2024.09.001
[research_niu_chen_2025]: https://doi.org/10.1007/s44270-025-00024-8
[research_niu_chen_2026]: https://doi.org/10.1016/j.ast.2026.111969
[research_niu_chen_2026_b]: https://doi.org/10.1016/j.ijhydene.2026.155962
[research_niu_su_2023]: https://doi.org/10.1063/5.0141000
[research_niu_wang_2023]: https://doi.org/10.21203/rs.3.rs-2333969/v1
[research_nomura_1983]: https://doi.org/10.2514/3.8296
[research_non_empirical_analytical_2019]: https://doi.org/10.1088/2053-2563/aae894ch17
[research_nordinbates_fureby_2017]: https://doi.org/10.1016/j.proci.2016.07.118
[research_norman_walker_1966]: https://doi.org/10.21236/ad0482453
[research_norris_2017]: https://ntrs.nasa.gov/citations/20180000521
[research_novelli_koschel_2001]: https://doi.org/10.2514/6.2001-1870
[research_nowakrj_kellyhn_1976]: https://ntrs.nasa.gov/citations/19760047061
[research_numerical_analysis_2026]: https://doi.org/10.56726/irjmets88340
[research_numerical_comparative_2024]: https://doi.org/10.23977/mpcr.2024.040113
[research_numerical_optimization_2016]: https://doi.org/10.21275/v5i6.nov164465
[research_numerical_simulation_2015]: https://doi.org/10.4028/www.scientific.net/amm.766-767.1044
[research_numerical_simulation_2015_b]: https://doi.org/10.15372/pmtf20150505
[research_numerical_study_2015]: https://doi.org/10.15372/fgv20150305
[research_nurfathinzahrolayali_mohdrashdansaad_2022]: https://doi.org/10.37934/cfdl.14.10.7986
[research_oamjee_sadanandan_2019]: https://doi.org/10.1016/j.ast.2019.07.021
[research_oamjee_sadanandan_2020]: https://doi.org/10.1063/5.0026125
[research_oamjee_sadanandan_2020_b]: https://doi.org/10.1017/aer.2020.27
[research_oberg_2015]: https://doi.org/10.14264/uql.2015.505
[research_oberylj_stittle_1958]: https://ntrs.nasa.gov/citations/19630008168
[research_obyrne_doolan_1998]: https://doi.org/10.2514/6.1998-965
[research_obyrne_doolan_1999]: https://doi.org/10.1007/s001930050159
[research_obyrne_wittig_2011]: https://doi.org/10.21236/ada544361
[research_odam_paull_2003]: https://doi.org/10.2514/6.2003-6961
[research_oerley_gamba_2012]: https://doi.org/10.2514/6.2012-3264
[research_oertel_1970]: https://doi.org/10.3138/9781487595876-008
[research_oertel_fritzh_1972]: https://doi.org/10.21236/ad0757150
[research_ogawa_2024]: https://doi.org/10.1063/5.0228287
[research_ogawa_2025]: https://doi.org/10.1115/1.4068663
[research_ogawa_grainger_2009]: https://doi.org/10.2514/6.2009-7401
[research_ohira_1999]: https://doi.org/10.1299/kikaib.65.4055
[research_ohira_2002]: https://doi.org/10.1002/htj.10068
[research_ohira_2004]: https://doi.org/10.1063/1.1774667
[research_ohira_2016]: https://doi.org/10.1016/b978-1-78242-362-1.00003-1
[research_ohira_matsuo_1994]: https://doi.org/10.1016/s0011-2275(05)80090-6
[research_ohlhorst_glass_2005]: https://ntrs.nasa.gov/citations/20050240163
[research_ohlhorst_vaughn_1990]: https://ntrs.nasa.gov/citations/19900019225
[research_ohlhorst_vaughn_1992]: https://ntrs.nasa.gov/citations/19930003268
[research_olds_1988]: https://doi.org/10.2514/6.1988-89
[research_olds_budianto_1998]: https://doi.org/10.2514/6.1998-302
[research_olejniczak_candler_1996]: https://doi.org/10.2514/6.1996-2238
[research_oneill_lewis_1992]: https://doi.org/10.2514/3.56866
[research_oneill_lewis_1993]: https://doi.org/10.2514/3.46438
[research_oneillmarykael_lewismarkj_1992]: https://ntrs.nasa.gov/citations/19920050689
[research_opacich_ombrello_2026]: https://doi.org/10.1016/j.proci.2026.106191
[research_opilaelizabethj_2003]: https://ntrs.nasa.gov/citations/20050214581
[research_optimal_aerodynamic_1996]: https://doi.org/10.2514/5.9781600866401.0017.0049
[research_orbital_atk_2016]: https://doi.org/10.1016/j.mprp.2016.04.028
[research_ormsbee_1962]: https://doi.org/10.21236/ad0295993
[research_ortloff_1968]: https://doi.org/10.21236/ad0830727
[research_ortwerth_goldman_1996]: https://doi.org/10.2514/6.1996-3039
[research_osborne_ghonem_2005]: https://doi.org/10.21236/ada438848
[research_osgerby_smithson_1969]: https://doi.org/10.21236/ad0692466
[research_osgerby_smithson_1970]: https://doi.org/10.2514/3.5970
[research_otsuka_sakamoto_1999]: https://doi.org/10.2472/jsms.48.9appendix_163
[research_ou_yan_2019]: https://doi.org/10.1016/j.actaastro.2018.12.012
[research_ouzts_2008]: https://doi.org/10.2514/6.2008-2621
[research_ouzts_soloway_2009]: https://ntrs.nasa.gov/citations/20100021410
[research_owenfk_horstmancc_1972]: https://ntrs.nasa.gov/citations/19720051522
[research_oxidation_protection_1990]: https://doi.org/10.1016/0010-4361(90)90250-z
[research_oz_kara_2024]: https://doi.org/10.1038/s41598-024-66867-4
[research_ozbek_karyeyen_2023]: https://doi.org/10.58559/ijes.1218754
[research_pagilla_2019]: https://doi.org/10.22214/ijraset.2019.8032
[research_pak_2008]: https://ntrs.nasa.gov/citations/20080017221
[research_palaszewski_1998]: https://ntrs.nasa.gov/citations/20050177876
[research_pallela_thakur_2025]: https://doi.org/10.1007/s42401-025-00425-2
[research_palmer_2021]: https://doi.org/10.14264/bd53932
[research_pamadi_1989]: https://doi.org/10.2514/6.1989-3443
[research_pamadi_1995]: https://doi.org/10.2514/3.21563
[research_pamadi_tartabini_2004]: https://doi.org/10.2514/6.2004-876
[research_pan_bi_2018]: https://doi.org/10.1016/j.expthermflusci.2018.03.017
[research_pan_wang_2024]: https://doi.org/10.1088/1742-6596/2820/1/012076
[research_pan_xiong_2022]: https://doi.org/10.1016/j.energy.2022.123582
[research_pan_zhou_2024]: https://doi.org/10.1016/j.applthermaleng.2024.122916
[research_pandey_soni_2022]: https://doi.org/10.1016/j.msea.2022.144378
[research_paredes_theofilis_2015]: https://doi.org/10.1016/j.jfluidstructs.2014.11.002
[research_paredes_venkatachari_2020]: https://doi.org/10.2514/1.j059407
[research_parikhparesh_engelundwalter_2004]: https://ntrs.nasa.gov/citations/20040110351
[research_parish_barone_2025]: https://doi.org/10.1103/qqxr-ly55
[research_park_1992]: https://ntrs.nasa.gov/citations/19940034108
[research_park_1996]: https://doi.org/10.2514/6.1996-2234
[research_park_2010]: https://doi.org/10.1016/j.ijhydene.2010.04.074
[research_park_bogdanoff_2000]: https://ntrs.nasa.gov/citations/20010066491
[research_park_chang_2016]: https://doi.org/10.5139/jksas.2016.44.6.463
[research_park_kim_2026]: https://doi.org/10.1007/s42405-026-01190-y
[research_park_lee_2022]: https://doi.org/10.7316/khnes.2022.33.3.247
[research_park_lee_2026]: https://doi.org/10.3390/aerospace13040380
[research_park_mehta_2000]: https://ntrs.nasa.gov/citations/20010087676
[research_park_menees_1996]: https://doi.org/10.2514/3.26787
[research_park_park_2016]: https://doi.org/10.1007/s00162-016-0396-7
[research_park_park_2022]: https://doi.org/10.1016/j.ast.2022.107902
[research_parkchul_1989]: https://ntrs.nasa.gov/citations/19910029860
[research_parker_2022]: https://doi.org/10.21236/ad1180064
[research_parker_spain_1991]: https://doi.org/10.2514/6.1991-936
[research_parmar_jp_2026]: https://doi.org/10.1016/j.ast.2026.112964
[research_parsley_1989]: https://doi.org/10.2514/6.1989-2280
[research_parsons_richmond_1969]: https://doi.org/10.2514/6.1969-84
[research_pathak_khare_2024]: https://doi.org/10.1016/j.actaastro.2024.08.023
[research_patra_lee_2018]: https://doi.org/10.1021/acsanm.8b00781
[research_patrick_2019]: https://doi.org/10.1063/10.0000281
[research_patrick_2021]: https://doi.org/10.1063/10.0005106
[research_patterson_2010]: https://doi.org/10.21236/ada514616
[research_paudel_mcfarland_2025]: https://doi.org/10.1016/j.fuel.2024.133587
[research_paull_1993]: https://ntrs.nasa.gov/citations/19930066199
[research_paull_1999]: https://doi.org/10.2514/6.1999-2450
[research_paull_alesi_2005]: https://doi.org/10.1007/978-3-540-27009-6_4
[research_paull_frost_2000]: https://ntrs.nasa.gov/citations/20000037781
[research_paull_stalker_1988]: https://doi.org/10.2514/6.1988-2018
[research_paull_stalker_1995]: https://doi.org/10.1017/s0022112095002096
[research_paull_stalker_1995_b]: https://ntrs.nasa.gov/citations/19960001680
[research_paull_stalker_1995_c]: https://ntrs.nasa.gov/citations/19950018976
[research_paull_stalker_1998]: https://doi.org/10.2514/6.1998-1533
[research_paulla_stalkerrj_1995]: https://ntrs.nasa.gov/citations/19950018975
[research_pavlov_gerasimov_2023]: https://doi.org/10.3390/fire6110435
[research_pavlov_istomin_2023]: https://doi.org/10.3103/s002713492307024x
[research_payne_1968]: https://ntrs.nasa.gov/citations/19680021154
[research_payne_1980]: https://doi.org/10.21236/ada087515
[research_payne_hartley_1980]: https://doi.org/10.21236/ada087514
[research_paynter_1988]: https://doi.org/10.1016/0045-7949(88)90212-x
[research_pearsonwe_1967]: https://ntrs.nasa.gov/citations/19680034465
[research_peebles_2008]: https://doi.org/10.2514/4.479328
[research_peebles_2009]: https://ntrs.nasa.gov/citations/20090009758
[research_peeblescurtis_2007]: https://ntrs.nasa.gov/citations/20070038172
[research_peeblescurtis_2007_b]: https://ntrs.nasa.gov/citations/20070021686
[research_peggrobertj_huntjamesl_1993]: https://ntrs.nasa.gov/citations/19930037111
[research_pei_fan_2021]: https://doi.org/10.1109/access.2021.3056517
[research_pellett_bruno_2002]: https://ntrs.nasa.gov/citations/20030010281
[research_pellett_dawson_2009]: https://ntrs.nasa.gov/citations/20100002799
[research_pellett_vaden_2008]: https://ntrs.nasa.gov/citations/20080020388
[research_pellettgerald_2005]: https://ntrs.nasa.gov/citations/20050041971
[research_pelloux_1994]: https://ntrs.nasa.gov/citations/19950012056
[research_penanhoat_darracq_1996]: https://doi.org/10.2514/3.24059
[research_peng_2023]: https://doi.org/10.1016/j.csite.2023.103620
[research_peng_panesar_2024]: https://doi.org/10.1016/j.addma.2024.104498
[research_peng_wang_2026]: https://doi.org/10.1088/1742-6596/3256/1/012063
[research_peng_xu_2024]: https://doi.org/10.1063/5.0235591
[research_peng_xu_2024_b]: https://doi.org/10.1088/1742-6596/2882/1/012097
[research_peng_yin_2025]: https://doi.org/10.1016/j.ast.2024.109881
[research_peng_zhong_2022]: https://doi.org/10.1016/j.fuel.2022.125547
[research_peng_zhou_2024]: https://doi.org/10.1021/acsomega.4c00622
[research_penland_romeo_1971]: https://doi.org/10.2514/3.59185
[research_performance_and_2018]: https://doi.org/10.33140/atcp.01.02.07
[research_perkins_2010]: https://ntrs.nasa.gov/citations/20100040415
[research_perkowski_bilar_2024]: https://doi.org/10.1007/s00193-024-01185-2
[research_perlo_2026]: https://doi.org/10.63620/mkjaeast.2026.1012
[research_perrel_lafon_1992]: https://doi.org/10.1007/978-3-642-77922-0_47
[research_perrier_rostand_1994]: https://doi.org/10.2514/6.1994-3090
[research_perry_2026]: https://doi.org/10.14264/69be79f
[research_persh_1955]: https://doi.org/10.21236/ad0075320
[research_peschke_1995]: https://doi.org/10.2514/3.23921
[research_peterson_2023]: https://doi.org/10.1016/j.proci.2022.08.120
[research_petervari_wagner_2026]: https://doi.org/10.1016/j.ast.2026.113377
[research_pethasethuraman_kim_2020]: https://doi.org/10.1177/0954410020967537
[research_pethasethuraman_yang_2023]: https://doi.org/10.1063/5.0137481
[research_petley_dziedzic_1993]: https://ntrs.nasa.gov/citations/19930065834
[research_petukhov_kolchin_2023]: https://doi.org/10.36236/1999-7590-2023-15-3-205-214
[research_pezzella_viviani_2016]: https://doi.org/10.1016/j.ast.2016.02.030
[research_pfaff_1968]: https://doi.org/10.21236/ad0832104
[research_phillips_cruz_1991]: https://doi.org/10.2514/6.1991-1694
[research_phillips_engelund_1997]: https://doi.org/10.2514/2.3190
[research_phillips_fiedler_1968]: https://doi.org/10.21236/ad0683763
[research_pichler_2023]: https://doi.org/10.31224/3206
[research_pike_1996]: https://doi.org/10.2514/3.13268
[research_pike_1996_b]: https://doi.org/10.2514/3.13267
[research_piland_1987]: https://ntrs.nasa.gov/citations/19880028711
[research_pilandwilliamm_1987]: https://ntrs.nasa.gov/citations/19880054061
[research_pinckney_1978]: https://ntrs.nasa.gov/citations/19780009114
[research_pinckney_walton_1994]: https://ntrs.nasa.gov/citations/19940000264
[research_pirrellocj_bakerah_1976]: https://ntrs.nasa.gov/citations/19760011448
[research_pisano_whitfield_2024]: https://doi.org/10.2514/6.2024-2330
[research_pisharoti_brizzolara_2025]: https://doi.org/10.51560/ofj.v5.130
[research_pittman_1989]: https://ntrs.nasa.gov/citations/19900058422
[research_plankpp_penningfa_1973]: https://ntrs.nasa.gov/citations/19730025150
[research_plencnerrobertm_1991]: https://ntrs.nasa.gov/citations/19920001816
[research_pm_titanium_2002]: https://doi.org/10.1016/s0026-0657(02)80588-4
[research_polev_grunin_2022]: https://doi.org/10.54349/26586061_2022_3_15
[research_pollock_wild_2021]: https://doi.org/10.2514/6.2021-4084
[research_pollock_wild_2024]: https://doi.org/10.31224/3817
[research_polyanskii_1967]: https://doi.org/10.1007/bf01013723
[research_pope_1968]: https://doi.org/10.2514/6.1968-15
[research_pordalhs_khoslapk_1990]: https://ntrs.nasa.gov/citations/19900039912
[research_porter_2022]: https://doi.org/10.14264/1304176
[research_pototzky_spain_1988]: https://ntrs.nasa.gov/citations/19890002362
[research_potter_whitfield_1957]: https://doi.org/10.21236/ad0135338
[research_poudel_shoele_2026]: https://doi.org/10.2514/6.2026-4661
[research_pouring_1965]: https://doi.org/10.1063/1.1761112
[research_povinelli_dwoyer_1990]: https://ntrs.nasa.gov/citations/19900054108
[research_povinellilouisa_1989]: https://ntrs.nasa.gov/citations/19890014438
[research_povinellilouisa_1990]: https://ntrs.nasa.gov/citations/19910012134
[research_povinellilouisa_1991]: https://ntrs.nasa.gov/citations/19910012145
[research_povinellilouisa_1996]: https://ntrs.nasa.gov/citations/19970009255
[research_powell_1985]: https://doi.org/10.2514/6.1985-913
[research_powell_1992]: https://ntrs.nasa.gov/citations/19920012291
[research_powell_shaughnessy_1991]: https://ntrs.nasa.gov/citations/19910060519
[research_powering_the_2022]: https://doi.org/10.1002/9781119640646.oth1
[research_prabhudk_tannehilljc_1984]: https://ntrs.nasa.gov/citations/19840056580
[research_prasad_2022]: https://doi.org/10.13111/2066-8201.2022.14.1.10
[research_prediction_and_1985]: https://doi.org/10.2514/5.9781600865732.0121.0171
[research_prediction_and_1985_b]: https://doi.org/10.2514/5.9781600865732.0173.0206
[research_preller_2018]: https://doi.org/10.14264/uql.2018.437
[research_preller_smart_2012]: https://doi.org/10.2514/6.2012-5825
[research_presby_2021]: https://doi.org/10.1115/1.4051969
[research_preston_1958]: https://doi.org/10.1017/s0022112058000057
[research_problem_of_2001]: https://doi.org/10.2514/5.9781600866609.0891.0938
[research_probstein_1968]: https://doi.org/10.2514/6.1968-4
[research_process_for_1992]: https://doi.org/10.1016/0010-4361(92)90502-l
[research_pruitt_bates_1992]: https://doi.org/10.2514/6.1992-5091
[research_pschen_chsu_2026]: https://ntrs.nasa.gov/citations/20260002311
[research_psiaki_park_1991]: https://ntrs.nasa.gov/citations/19920035222
[research_pu_xu_2026]: https://doi.org/10.1063/5.0336053
[research_pudsey_2014]: https://doi.org/10.14264/uql.2014.242
[research_pukhov_1993]: https://doi.org/10.2514/6.1993-5055
[research_pulsonetti_erdos_1991]: https://doi.org/10.2514/3.23427
[research_purifoy_neal_2017]: https://ntrs.nasa.gov/citations/20170003419
[research_purpura_2021]: https://doi.org/10.1109/jmass.2020.3023968
[research_purpura_trifoni_2018]: https://doi.org/10.1007/bf03406051
[research_purwar_basu_2017]: https://doi.org/10.1111/jace.14750
[research_qi_bao_2015]: https://doi.org/10.1016/j.jfranklin.2015.08.020
[research_qi_cheng_2022]: https://doi.org/10.3390/aerospace9120788
[research_qi_li_2021]: https://doi.org/10.1186/s42774-021-00082-x
[research_qi_wang_1998]: https://doi.org/10.2514/2.5353
[research_qiao_liu_2022]: https://doi.org/10.1016/j.csite.2022.102476
[research_qiao_liu_2023]: https://doi.org/10.1016/j.applthermaleng.2023.120526
[research_qiao_liu_2024]: https://doi.org/10.1016/j.energy.2024.130906
[research_qin_agarwal_2019]: https://doi.org/10.1016/j.combustflame.2019.08.038
[research_qin_bao_2009]: https://doi.org/10.1243/09544100jaero552
[research_qin_bao_2012]: https://doi.org/10.1061/(asce)as.1943-5525.0000137
[research_qin_chang_2015]: https://doi.org/10.2514/1.j053547
[research_qin_huang_2026]: https://doi.org/10.1016/j.ast.2025.111044
[research_qin_scriba_1991]: https://doi.org/10.1017/s0001924000023800
[research_qin_yuan_2026]: https://doi.org/10.1063/5.0336363
[research_qin_zhang_2026]: https://doi.org/10.1063/5.0303107
[research_qin_zhou_2010]: https://doi.org/10.1016/j.ijhydene.2009.09.025
[research_qiu_shi_2024]: https://doi.org/10.1017/jfm.2024.42
[research_qiu_zhang_2021]: https://doi.org/10.1016/j.ast.2020.106376
[research_quan_chang_2024]: https://doi.org/10.1016/j.applthermaleng.2023.121527
[research_quan_xu_2021]: https://doi.org/10.1016/j.ast.2021.107076
[research_quinlanjesser_mcdanieljamesc_2014]: https://ntrs.nasa.gov/citations/20150001235
[research_quinn_1978]: https://doi.org/10.2514/6.1978-44
[research_quinnrobertd_gongleslie_1990]: https://ntrs.nasa.gov/citations/19900019499
[research_rabadansantana_weigand_2021]: https://doi.org/10.1016/j.ast.2021.106595
[research_radhi_iacobellis_2019]: https://doi.org/10.1016/j.compositesb.2019.107129
[research_radiation_at_1962]: https://doi.org/10.2514/5.9781600864810.0255.0280
[research_ragnoli_savino_2024]: https://doi.org/10.1016/j.ast.2024.109092
[research_rahimi_svolos_2026]: https://doi.org/10.1016/j.engfracmech.2025.111794
[research_rahmani_hejranfar_2021]: https://doi.org/10.1016/j.compfluid.2021.105079
[research_raj_1987]: https://doi.org/10.21236/ada182904
[research_raj_sandhu_2019]: https://doi.org/10.12783/ballistics2019/33290
[research_rajput_soni_2026]: https://doi.org/10.37868/dss.v7.id324
[research_ramanah_mee_2006]: https://doi.org/10.2514/6.2006-8004
[research_ramanujachari_amruthapreethi_2023]: https://doi.org/10.61653/joast.v74i1.2022.5
[research_ramunno_boyd_2022]: https://doi.org/10.2514/1.b38573
[research_rana_thornber_2009]: https://doi.org/10.2514/6.2009-4844
[research_rana_thornber_2011]: https://doi.org/10.2514/6.2011-506
[research_raneydavidl_mcminnjohnd_1993]: https://ntrs.nasa.gov/citations/19940020631
[research_ransonephilipo_yamakiyrobert_1992]: https://ntrs.nasa.gov/citations/19930003267
[research_rapial_1969]: https://doi.org/10.6028/nbs.tn.378
[research_rasky_1993]: https://ntrs.nasa.gov/citations/19930012925
[research_rasmussen_stevens_1987]: https://doi.org/10.2514/6.1987-2550
[research_rataczak_chaudhry_2024]: https://doi.org/10.2514/1.a35764
[research_ratchford_redding_2025]: https://doi.org/10.1063/5.0299691
[research_rathi_sinha_2024]: https://doi.org/10.2514/1.j064053
[research_ratnayakenalina_2010]: https://ntrs.nasa.gov/citations/20100001729
[research_rattray_mall_1994]: https://doi.org/10.1016/0263-8223(94)90127-9
[research_rausch_mcclinton_1997]: https://ntrs.nasa.gov/citations/20040110669
[research_rausch_mcclinton_2000]: https://ntrs.nasa.gov/citations/20010075170
[research_rauschvincentl_morrischarlesekjr_1992]: https://ntrs.nasa.gov/citations/19920074635
[research_ravichandran_doherty_2023]: https://doi.org/10.2514/6.2023-0437
[research_ravindran_bricalli_2019]: https://doi.org/10.1016/j.actaastro.2019.06.010
[research_raviteja_bharanichandra_2022]: https://doi.org/10.1016/j.ifacol.2022.04.033
[research_ray_niggemeier_1988]: https://doi.org/10.2514/6.1988-3262
[research_raylewarrend_kochrichardg_1954]: https://ntrs.nasa.gov/citations/19930088026
[research_reba_christian_1963]: https://doi.org/10.21236/ad0297092
[research_recent_advances_1978]: https://ntrs.nasa.gov/citations/19790013251
[research_recina_karlsson_1999]: https://doi.org/10.1016/s0921-5093(98)01008-9
[research_reda_1991]: https://doi.org/10.2514/6.1991-5051
[research_redding_cavanaugh_2025]: https://doi.org/10.1063/5.0271076
[research_reddy_2019]: https://doi.org/10.22214/ijraset.2019.6273
[research_reddy_harloff_1991]: https://doi.org/10.2514/3.23297
[research_reddy_smith_1989]: https://ntrs.nasa.gov/citations/19890007388
[research_redifer_lin_2007]: https://ntrs.nasa.gov/citations/20070021457
[research_reed_1990]: https://doi.org/10.21236/ada226351
[research_reed_1997]: https://doi.org/10.21236/ada329724
[research_reed_perez_2015]: https://doi.org/10.2514/1.a32825
[research_reid_2025]: https://doi.org/10.14264/dcf3434
[research_reisenthel_allen_2010]: https://doi.org/10.21236/ada517077
[research_reisgen_olschok_2014]: https://doi.org/10.1002/9781118998489.ch15
[research_relangi_ingenito_2022]: https://doi.org/10.1177/14680874221085059
[research_ren_wang_2022]: https://doi.org/10.1063/5.0093438
[research_ren_yuan_2019]: https://doi.org/10.1017/jfm.2019.756
[research_ren_zhang_2017]: https://doi.org/10.2514/6.2017-2113
[research_rerj_berrierbl_1982]: https://ntrs.nasa.gov/citations/19820012282
[research_research_on_2024]: https://doi.org/10.33140/eoa.02.03.04
[research_research_progress_2026]: https://doi.org/10.3901/jme.260073
[research_resendehugob_1991]: https://ntrs.nasa.gov/citations/19910047406
[research_resendehugob_1993]: https://ntrs.nasa.gov/citations/19930017895
[research_reshotko_1987]: https://doi.org/10.21236/ada185764
[research_reubush_1999]: https://ntrs.nasa.gov/citations/20040087154
[research_reubush_nguyen_2004]: https://ntrs.nasa.gov/citations/20040040296
[research_reubushde_pusterrl_1987]: https://ntrs.nasa.gov/citations/19870018524
[research_reusable_launch_1995]: https://ntrs.nasa.gov/citations/19960013899
[research_reyhner_hickcox_1972]: https://doi.org/10.2514/3.59041
[research_reynier_2016]: https://doi.org/10.1016/j.paerosci.2016.04.002
[research_rez_2021]: https://doi.org/10.1063/pt.3.4826
[research_rhodes_1964]: https://doi.org/10.21236/ad0608566
[research_rhudy_1970]: https://doi.org/10.2514/3.5713
[research_ricciardi_1991]: https://doi.org/10.2514/6.1991-1920
[research_rice_2002]: https://ntrs.nasa.gov/citations/20020087574
[research_rich_lempert_2007]: https://doi.org/10.21236/ada478735
[research_richard_christophe_1995]: https://doi.org/10.1016/0094-5765(94)00154-e
[research_richards_1978]: https://doi.org/10.21236/ada069883
[research_richards_culotta_1971]: https://doi.org/10.21236/ad0743836
[research_richards_stollery_1979]: https://doi.org/10.2514/3.58502
[research_richardson_1989]: https://ntrs.nasa.gov/citations/19910001561
[research_richardsonpamelaf_mcclintoncharlesr_1989]: https://ntrs.nasa.gov/citations/19900058418
[research_rickettsrodneyh_nollthomase_1993]: https://ntrs.nasa.gov/citations/19930049892
[research_rickman_2010]: https://doi.org/10.1002/9780470686652.eae486
[research_ridgway_sam_2018]: https://doi.org/10.3390/en11123449
[research_riggins_1997]: https://doi.org/10.2514/2.5161
[research_riggins_2002]: https://ntrs.nasa.gov/citations/20020073109
[research_riggins_mcclinton_1992]: https://doi.org/10.2514/6.1992-5097
[research_riggins_mcclinton_1997]: https://doi.org/10.2514/2.5160
[research_rigginsdavid_1998]: https://ntrs.nasa.gov/citations/20000034104
[research_rigginsdavid_tacketregan_2006]: https://ntrs.nasa.gov/citations/20070000536
[research_riley_dejarnette_1992]: https://doi.org/10.2514/3.26355
[research_riley_gaitonde_2018]: https://doi.org/10.2514/1.b36888
[research_riley_mcnamara_2017]: https://doi.org/10.2514/1.j055521
[research_riva_daminelli_1997]: https://doi.org/10.2514/2.5199
[research_rivers_glass_2006]: https://ntrs.nasa.gov/citations/20060020757
[research_rivershkevin_1999]: https://ntrs.nasa.gov/citations/20040086813
[research_rizkalla_bakos_1989]: https://ntrs.nasa.gov/citations/19890059536
[research_rizkalla_chinitz_1990]: https://doi.org/10.2514/3.23222
[research_rizvi_linshu_2017]: https://doi.org/10.1017/aer.2017.11
[research_rizzi_parish_2026]: https://doi.org/10.1007/s00158-026-04300-2
[research_robinson_2024]: https://doi.org/10.14264/158040
[research_robinson_martin_2006]: https://ntrs.nasa.gov/citations/20060050110
[research_robinson_mee_2004]: https://doi.org/10.2514/1.10699
[research_robinsonjc_smithdm_1980]: https://ntrs.nasa.gov/citations/19810030592
[research_roche_breil_2026]: https://doi.org/10.1016/j.cma.2026.119209
[research_rochejosephm_kosareodanieln_2001]: https://ntrs.nasa.gov/citations/20010016865
[research_rockwell_goyne_2010]: https://doi.org/10.2514/6.2010-1126
[research_rockwell_goyne_2011]: https://doi.org/10.2514/1.b34270
[research_roder_1977]: https://doi.org/10.6028/nbs.ir.77-859
[research_rodgers_1992]: https://ntrs.nasa.gov/citations/20080032814
[research_rodi_2012]: https://doi.org/10.2514/6.2012-3223
[research_rodi_emami_1996]: https://doi.org/10.2514/3.24061
[research_rodkiewicz_chattopadhyay_1971]: https://doi.org/10.2514/3.6505
[research_rodrigues_2026]: https://doi.org/10.2514/1.t7458
[research_rodriguez_dickeson_2009]: https://ntrs.nasa.gov/citations/20100024153
[research_rodriguezfuentes_parent_2022]: https://doi.org/10.2514/6.2022-3442
[research_rodriguezfuentes_parent_2023]: https://doi.org/10.2514/1.j062166
[research_rodriguezmirasol_thrower_1995]: https://doi.org/10.1016/0008-6223(94)00180-8
[research_rodriguezsegade_hernandez_2024]: https://doi.org/10.1016/j.ast.2024.109346
[research_roga_2019]: https://doi.org/10.1088/1742-6596/1276/1/012041
[research_roga_2019_b]: https://doi.org/10.1088/1742-6596/1276/1/012038
[research_rogers_shih_2001]: https://ntrs.nasa.gov/citations/20010083962
[research_rogers_shih_2005]: https://ntrs.nasa.gov/citations/20050234608
[research_rogers_weidner_1991]: https://ntrs.nasa.gov/citations/19910034570
[research_rogers_weidner_1994]: https://doi.org/10.2514/6.1994-2518
[research_rogersrc_1979]: https://ntrs.nasa.gov/citations/19790035675
[research_rogersrclayton_capriottidiegop_1998]: https://ntrs.nasa.gov/citations/20040090464
[research_rokaw_getchell_1996]: https://doi.org/10.21236/ada366929
[research_rom_avital_1992]: https://doi.org/10.2514/6.1992-3717
[research_ronald_1989]: https://doi.org/10.2514/6.1989-5010
[research_ronald_1989_b]: https://doi.org/10.1007/978-1-4613-0817-1_1
[research_ronald_1991]: https://doi.org/10.2514/6.1991-5101
[research_ronald_1993]: https://ntrs.nasa.gov/citations/19940033671
[research_ronald_1995]: https://doi.org/10.2514/6.1995-6131
[research_rong_2017]: https://doi.org/10.12783/dtetr/apetc2017/11122
[research_rong_cheng_2023]: https://doi.org/10.1063/5.0154599
[research_roos_pudsey_2020]: https://doi.org/10.1016/j.actaastro.2020.08.022
[research_rose_sridhar_2022]: https://doi.org/10.1016/j.actaastro.2022.01.041
[research_rose_stankevics_1963]: https://doi.org/10.21236/ad0406269
[research_rosner_cibrian_1974]: https://ntrs.nasa.gov/citations/19740053212
[research_rothmund_scherrer_1996]: https://doi.org/10.2514/6.1996-4498
[research_roudakov_semenov_1996]: https://doi.org/10.2514/6.1996-4572
[research_roudakovalexanders_semenovvyacheslavl_1998]: https://ntrs.nasa.gov/citations/19980137604
[research_rouhiyoussefi_knight_2017]: https://doi.org/10.3390/aerospace4020025
[research_roundy_1979]: https://doi.org/10.21236/ada078529
[research_roux_2011]: https://doi.org/10.2514/1.t3758
[research_roux_choi_2014]: https://doi.org/10.2514/1.t4217
[research_roux_shakya_2013]: https://doi.org/10.2514/1.t4045
[research_roux_shakya_2013_b]: https://doi.org/10.2514/1.t3961
[research_roux_tiruveedula_2016]: https://doi.org/10.2514/1.t4792
[research_roux_tiruveedula_2017]: https://doi.org/10.1016/j.tsep.2017.03.003
[research_rouzbar_eyi_2015]: https://doi.org/10.2514/6.2015-3212
[research_rowan_2024]: https://doi.org/10.14264/106385
[research_rozario_zouaoui_2007]: https://doi.org/10.2514/6.2007-30
[research_ruan_domingo_2020]: https://doi.org/10.1016/j.combustflame.2020.01.034
[research_ruban_menezes_2018]: https://doi.org/10.2514/1.b37066
[research_ruban_menezes_2020]: https://doi.org/10.1115/1.4048141
[research_rubins_bauer_1994]: https://doi.org/10.2514/3.23768
[research_rubio_ramanujam_2018]: https://doi.org/10.1080/17436753.2018.1475140
[research_rudiments_and_2001]: https://doi.org/10.2514/5.9781600866609.0939.0978
[research_rufershannj_nowakrobertj_2009]: https://ntrs.nasa.gov/citations/20090024224
[research_ruffin_venkatapathy_1989]: https://ntrs.nasa.gov/citations/19890037993
[research_ruffin_venkatapathy_1989_b]: https://ntrs.nasa.gov/citations/19910001559
[research_rufjoseph_holtjamesb_1999]: https://ntrs.nasa.gov/citations/19990105699
[research_rufjosephh_holtjamesb_2001]: https://ntrs.nasa.gov/citations/20020050408
[research_ruggleswrenn_schmidt_2024]: https://doi.org/10.3390/jcs8080291
[research_runstadler_peterw_1969]: https://doi.org/10.21236/ad0865300
[research_rurenchow_1963]: https://doi.org/10.21236/ad0412486
[research_ruscignoh_1965]: https://ntrs.nasa.gov/citations/19660009178
[research_russian_aerospace_1996]: https://doi.org/10.2514/3.48384
[research_russin_1974]: https://ntrs.nasa.gov/citations/19740009392
[research_russinwr_1975]: https://ntrs.nasa.gov/citations/19750018240
[research_rwayneguy_1990]: https://ntrs.nasa.gov/citations/19910013840
[research_rwguy_rcrogers_1996]: https://ntrs.nasa.gov/citations/19960044656
[research_ryken_davis_2004]: https://doi.org/10.2514/6.2004-2741
[research_s_ad_2016]: https://doi.org/10.1016/j.ijheatfluidflow.2016.06.011
[research_sabelkin_zawada_2017]: https://doi.org/10.1177/0021998317722836
[research_sabinash_sastry_1995]: https://doi.org/10.1016/0921-5093(95)03333-5
[research_saboktakin_monjezi_2024]: https://doi.org/10.3897/arb.v36.e14
[research_sabre_space_2018]: https://doi.org/10.12968/s0261-2097(23)60247-3
[research_saccone_gardi_2016]: https://doi.org/10.1016/j.ast.2016.09.004
[research_sadunas_1976]: https://doi.org/10.2514/3.58724
[research_saenz_frankel_2025]: https://doi.org/10.1007/s00193-025-01226-4
[research_saghafian_shunn_2015]: https://doi.org/10.1016/j.proci.2014.10.004
[research_saha_2022]: https://doi.org/10.2139/ssrn.4084066
[research_sahbon_jacewicz_2023]: https://doi.org/10.3390/en16052501
[research_sahoo_mahapatra_2007]: https://doi.org/10.1016/j.measurement.2006.03.016
[research_sahu_tropina_2022]: https://doi.org/10.1088/1361-6595/ac4ecc
[research_saiprakash_raghav_2026]: https://doi.org/10.1063/5.0309330
[research_sakata_1992]: https://doi.org/10.1299/jsmemag.95.887_880
[research_samimy_webb_2011]: https://doi.org/10.21236/ada564713
[research_sams_1989]: https://doi.org/10.2514/6.1989-5006
[research_sanaka_kandula_2023]: https://doi.org/10.1515/tjeng-2023-0029
[research_sanchoponce_2016]: https://doi.org/10.14264/uql.2016.71
[research_sandborn_heron_1963]: https://doi.org/10.21236/ad0407472
[research_sandhu_2005]: https://doi.org/10.21236/ada436943
[research_sanghi_sane_1999]: https://doi.org/10.1515/tjj.1999.16.1.27
[research_sangiovanni_barber_1993]: https://doi.org/10.2514/3.11495
[research_sanjay_kuzhiveli_2025]: https://doi.org/10.1088/1757-899x/1327/1/012167
[research_sankar_kelkar_1995]: https://doi.org/10.21236/ada319913
[research_sano_1981]: https://doi.org/10.1115/1.3244484
[research_santos_2005]: https://doi.org/10.1590/s1678-58782005000300004
[research_santos_2007]: https://doi.org/10.2514/6.2007-615
[research_santos_lewis_2003]: https://doi.org/10.2514/6.2003-3894
[research_sappey_sutherland_2009]: https://doi.org/10.21236/ada544557
[research_saravanan_jagadeesh_2008]: https://doi.org/10.1007/s00193-008-0172-8
[research_sarosh_2021]: https://doi.org/10.20935/al2998
[research_sasmal_hochstein_1991]: https://doi.org/10.2514/6.1991-2407
[research_sastry_1963]: https://doi.org/10.2514/3.2079
[research_sato_izumikawa_1997]: https://doi.org/10.2514/6.1997-3021
[research_sato_kaji_1992]: https://doi.org/10.2514/6.1992-5102
[research_sato_kaji_1993]: https://doi.org/10.2322/jjsass1969.41.524
[research_sato_raman_2020]: https://doi.org/10.2514/1.b37664
[research_satyanarayan_raj_2026]: https://doi.org/10.1016/j.fuel.2025.137977
[research_sauerwein_hruschka_2015]: https://doi.org/10.1007/978-3-319-16835-7_61
[research_saunders_slater_2007]: https://ntrs.nasa.gov/citations/20080006598
[research_saundersjd_stuebertj_2012]: https://ntrs.nasa.gov/citations/20120002930
[research_savelev_stepanov_1988]: https://doi.org/10.1007/bf01051832
[research_sawatzky_2018]: https://doi.org/10.22215/etd/2017-11756
[research_scaggs_1966]: https://doi.org/10.21236/ad0648906
[research_scaggs_burggraf_1963]: https://doi.org/10.21236/ad0427751
[research_scala_1958]: https://doi.org/10.2514/8.7530
[research_scanning_and_1994]: https://ntrs.nasa.gov/citations/19960022935
[research_schalla_1967]: https://doi.org/10.1007/978-1-4757-0489-1_27
[research_schetz_billig_1982]: https://doi.org/10.2514/3.51187
[research_schetz_billig_1991]: https://doi.org/10.2514/3.23301
[research_schetz_gilreath_1969]: https://doi.org/10.1016/s0082-0784(69)80491-1
[research_schierman_ward_2001]: https://doi.org/10.21236/ada436268
[research_schindel_1999]: https://doi.org/10.2514/2.5435
[research_schirmeralbertow_caponefrancisj_1989]: https://ntrs.nasa.gov/citations/19890059727
[research_schmalhofer_griebel_2017]: https://doi.org/10.1115/gt2017-63249
[research_schmidt_patankar_1991]: https://doi.org/10.1115/1.2927728
[research_schmidt_schmidt_1997]: https://doi.org/10.2514/6.1997-458
[research_schmidt_velapoldi_1996]: https://doi.org/10.2514/6.1996-3904
[research_schneider_1970]: https://doi.org/10.2514/3.49827
[research_schneider_reed_2003]: https://doi.org/10.21236/ada413763
[research_schoettle_hillesheimer_1991]: https://doi.org/10.2514/6.1991-2655
[research_schoettle_rahn_1993]: https://doi.org/10.2514/6.1993-5009
[research_schouler_prevereaud_2023]: https://doi.org/10.1016/j.actaastro.2022.12.039
[research_schram_narayanaswamy_2026]: https://doi.org/10.1007/s00348-026-04215-0
[research_schreck_faller_1998]: https://doi.org/10.2514/2.2258
[research_schrotter_kavas_2026]: https://doi.org/10.13044/j.sdewes.d13.0659
[research_schubert_1978]: https://doi.org/10.1016/0017-9310(78)90102-3
[research_schuelein_schenk_2017]: https://doi.org/10.2514/6.2017-3121
[research_schulteroedding_olivier_1998]: https://doi.org/10.2514/6.1998-1528
[research_schultz_goldenstein_2012]: https://doi.org/10.2514/6.2012-2654
[research_schunk_chung_2000]: https://doi.org/10.2514/6.2000-3467
[research_schwelkart_hallion_1997]: https://doi.org/10.21236/ada441126
[research_schwendemannmf_sandersbw_1982]: https://ntrs.nasa.gov/citations/19820054149
[research_scott_1993]: https://ntrs.nasa.gov/citations/19940023417
[research_scott_pototzky_1993]: https://ntrs.nasa.gov/citations/19930049934
[research_scottistephenj_1992]: https://ntrs.nasa.gov/citations/19930003259
[research_scramjet_2015]: https://doi.org/10.1036/1097-8542.802420
[research_scramjet_combustion_2022]: https://doi.org/10.1016/c2021-0-02204-5
[research_scramjet_combustor_2022]: https://doi.org/10.1002/9781119640646.ch5
[research_scramjet_developments_2001]: https://doi.org/10.2514/5.9781600866609.0047.0117
[research_scramjet_engine_2001]: https://doi.org/10.2514/5.9781600866609.0159.0222
[research_scramjet_flowpath_2001]: https://doi.org/10.2514/5.9781600866609.1105.1293
[research_scramjet_inlet_forebody_2022]: https://doi.org/10.1002/9781119640646.ch4
[research_scramjet_inlets_2001]: https://doi.org/10.2514/5.9781600866609.0447.0511
[research_scramjet_investigations_2001]: https://doi.org/10.2514/5.9781600866609.0119.0158
[research_scramjet_nozzle_aftbody_2022]: https://doi.org/10.1002/9781119640646.ch8
[research_scramjet_performance_2001]: https://doi.org/10.2514/5.9781600866609.0369.0446
[research_scramjet_research_2001]: https://doi.org/10.2514/5.9781600866609.0223.0367
[research_scramjet_testing_2001]: https://doi.org/10.2514/5.9781600866609.0001.0046
[research_scramjets_and_2022]: https://doi.org/10.1002/9781119640646.ch10
[research_scribben_withrow_2006]: https://doi.org/10.21236/ada463634
[research_seebass_1989]: https://doi.org/10.1126/science.246.4936.1374-e
[research_seebaugh_1973]: https://doi.org/10.2514/3.44348
[research_seebaughwr_doranrw_1971]: https://ntrs.nasa.gov/citations/19720004553
[research_seetharaman_semiatin_1996]: https://doi.org/10.1007/bf02651948
[research_segalcorin_mcdanieljamesc_1991]: https://ntrs.nasa.gov/citations/19910036713
[research_sekar_thomas_1990]: https://doi.org/10.2514/6.1990-531
[research_selcan_sander_2021]: https://doi.org/10.1007/s00193-020-00982-9
[research_seleznev_2019]: https://doi.org/10.33257/phchgd.20.3.853
[research_seleznev_2021]: https://doi.org/10.33257/phchgd.22.4.945
[research_seleznev_2022]: https://doi.org/10.1134/s0015462822601164
[research_self_starting_simulation_2020]: https://doi.org/10.36884/jafm.13.06.31389
[research_sellers_1965]: https://doi.org/10.2514/3.59477
[research_sen_pesyridis_2018]: https://doi.org/10.3390/en11061568
[research_serre_2011]: https://doi.org/10.2514/6.2011-2265
[research_sforza_2017]: https://doi.org/10.1016/b978-0-12-809326-9.00005-1
[research_sforza_2026]: https://doi.org/10.3390/aerospace13020115
[research_sha_long_2026]: https://doi.org/10.1063/5.0320179
[research_shadow_1987]: https://doi.org/10.21236/ada531361
[research_shajahan_gugulothu_2025]: https://doi.org/10.1016/j.ijhydene.2025.150342
[research_shameed_gr_2021]: https://doi.org/10.1016/j.ast.2021.106777
[research_shan_hou_2017]: https://doi.org/10.1016/j.ijhydene.2017.02.100
[research_shan_zhang_2021]: https://doi.org/10.1016/j.ijhydene.2020.10.225
[research_shang_2008]: https://doi.org/10.2514/6.2008-722
[research_shang_chang_2007]: https://doi.org/10.2514/6.2007-3885
[research_shanmugam_silvi_2025]: https://doi.org/10.1016/j.icheatmasstransfer.2025.109519
[research_shao_wang_2015]: https://doi.org/10.1016/j.ast.2015.09.003
[research_shaohua_xu_2017]: https://doi.org/10.1177/0954410017708213
[research_sharenson_1966]: https://doi.org/10.21236/ad0634390
[research_sharma_1987]: https://ntrs.nasa.gov/citations/19870011532
[research_sharma_1992]: https://ntrs.nasa.gov/citations/19950058960
[research_sharma_eswaran_2020]: https://doi.org/10.1115/1.4045985
[research_sharma_eswaran_2022]: https://doi.org/10.1016/j.ast.2022.107900
[research_sharma_saluti_2025]: https://doi.org/10.11648/j.ajae.20251102.14
[research_sharpeel_jacksonlr_1975]: https://ntrs.nasa.gov/citations/19750010039
[research_shaughnessyjohnd_gregoryirenem_1991]: https://ntrs.nasa.gov/citations/19920005858
[research_sheehan_1989]: https://doi.org/10.1016/0008-6223(89)90204-2
[research_sheetznwjr_1965]: https://ntrs.nasa.gov/citations/19650033898
[research_sheikin_kuranov_2004]: https://doi.org/10.2514/6.2004-1195
[research_sheikin_kuranov_2005]: https://doi.org/10.2514/6.2005-3223
[research_shekhtman_yu_2021]: https://doi.org/10.1007/s00348-021-03207-6
[research_shen_huang_2020]: https://doi.org/10.1016/j.ast.2020.105779
[research_shen_huang_2021]: https://doi.org/10.1016/j.csite.2021.101104
[research_shen_ma_2022]: https://doi.org/10.1016/j.ast.2022.107661
[research_shen_yao_2025]: https://doi.org/10.1016/j.ast.2025.110520
[research_shen_zhang_2019]: https://doi.org/10.1007/978-3-319-91017-8_27
[research_sheng_gan_2023]: https://doi.org/10.1007/s11071-023-08602-8
[research_shenoy_drozda_2019]: https://ntrs.nasa.gov/citations/20200002676
[research_shi_2016]: https://doi.org/10.2514/6.2016-4874
[research_shi_2022]: https://doi.org/10.3390/aerospace9070346
[research_shi_fan_2023]: https://doi.org/10.3390/aerospace10100879
[research_shi_he_2016]: https://doi.org/10.1016/j.actaastro.2016.07.017
[research_shi_liu_2016]: https://doi.org/10.1016/j.actaastro.2016.05.033
[research_shi_zhu_2020]: https://doi.org/10.2514/1.j059054
[research_shieh_lin_2024]: https://doi.org/10.3390/sym16081044
[research_shilnikov_elizarova_2018]: https://doi.org/10.1615/hightempmatproc.2018024713
[research_shimada_ohwada_2020]: https://doi.org/10.1186/s42774-020-00037-8
[research_shimada_yamamoto_1999]: https://doi.org/10.2514/6.1999-3493
[research_shimojima_hosokawa_2017]: https://doi.org/10.1016/j.mprp.2016.06.004
[research_shin_sung_2018]: https://doi.org/10.2514/1.j056707
[research_shirasu_south_1996]: https://doi.org/10.2514/3.26805
[research_shirasu_south_1996_b]: https://doi.org/10.2514/6.1996-3109
[research_shorecharlesp_1986]: https://ntrs.nasa.gov/citations/19880014433
[research_shorenstein_1971]: https://doi.org/10.21236/ad0731696
[research_shou_yan_2023]: https://doi.org/10.1002/rnc.6607
[research_shukla_verma_2020]: https://doi.org/10.2514/6.2020-2965
[research_shulman_parry_1966]: https://doi.org/10.1121/1.1942873
[research_shumskii_yaroslavtsev_2012]: https://doi.org/10.1134/s0010508212010042
[research_shvets_voronin_2005]: https://doi.org/10.2514/6.2005-512
[research_si_huang_2019]: https://doi.org/10.1063/1.5098543
[research_siddiqui_ledbetter_2023]: https://doi.org/10.1007/s00348-023-03716-6
[research_siebenhaar_bulman_1998]: https://ntrs.nasa.gov/citations/19990009075
[research_siebenhaar_bulman_1999]: https://ntrs.nasa.gov/citations/19990064624
[research_sihvola_2018]: https://doi.org/10.14264/uql.2018.323
[research_silva_brojo_2026]: https://doi.org/10.1016/j.ast.2025.111159
[research_silvestrov_surzhikov_2020]: https://doi.org/10.18698/0236-3941-2020-3-29-46
[research_simeonides_2006]: https://doi.org/10.1007/s00193-006-0040-3
[research_simeonides_haase_1994]: https://doi.org/10.2514/3.11985
[research_simoneau_hendricks_1988]: https://ntrs.nasa.gov/citations/19890065911
[research_simpson_2026]: https://doi.org/10.14264/29e2e8e
[research_sims_hahn_1964]: https://doi.org/10.21236/ad0603567
[research_sindt_1969]: https://doi.org/10.6028/nbs.tn.377
[research_sindt_1970]: https://doi.org/10.1016/0011-2275(70)90003-2
[research_sindt_1972]: https://ntrs.nasa.gov/citations/19730009186
[research_sindt_1972_b]: https://ntrs.nasa.gov/citations/19730009187
[research_sindt_1972_c]: https://ntrs.nasa.gov/citations/19730009185
[research_sindt_1995]: https://doi.org/10.1007/978-1-4613-9847-9_52
[research_sindt_ludtke_1973]: https://doi.org/10.6028/nbs.ir.73-344
[research_sindt_ludtke_1995]: https://doi.org/10.1007/978-1-4757-0513-3_47
[research_singh_mukhopadhyay_2025]: https://doi.org/10.1016/j.ast.2025.109928
[research_singh_prakash_2023]: https://doi.org/10.5937/fme2302221s
[research_singh_shen_1992]: https://doi.org/10.1016/0883-2889(92)90057-l
[research_singh_tiwari_1990]: https://doi.org/10.2514/6.1990-529
[research_single_stage_1994]: https://doi.org/10.2514/6.1994-4497
[research_sivan_pandian_2018]: https://doi.org/10.18520/cs/v114/i01/38-47
[research_sivasubramanian_v_2026]: https://doi.org/10.36948/ijfmr.2026.v08i02.74866
[research_skamniotis_cocks_2021]: https://doi.org/10.1016/j.ast.2021.106610
[research_skinner_chattopadhyay_2021]: https://doi.org/10.1016/j.compstruct.2021.114006
[research_skinner_stalker_1995]: https://ntrs.nasa.gov/citations/19960001683
[research_slater_saunders_2009]: https://doi.org/10.2514/6.2009-7349
[research_slaterjohnw_2016]: https://ntrs.nasa.gov/citations/20160010068
[research_slaterjohnw_davisdavido_2005]: https://ntrs.nasa.gov/citations/20050217469
[research_slush_hydrogen_1966]: https://ntrs.nasa.gov/citations/19670006126
[research_slush_hydrogen_2014]: https://doi.org/10.1201/b17226-30
[research_slutsky_tamagno_1965]: https://doi.org/10.2514/3.3215
[research_smallwj_weidnerjp_1974]: https://ntrs.nasa.gov/citations/19750005793
[research_smallwj_weidnerjp_1976]: https://ntrs.nasa.gov/citations/19770005051
[research_smarslok_2015]: https://doi.org/10.21236/ada615850
[research_smart_1999]: https://doi.org/10.2514/2.5459
[research_smart_2024]: https://doi.org/10.14264/282547
[research_smart_hass_2006]: https://doi.org/10.2514/1.20661
[research_smart_suraweera_2009]: https://doi.org/10.2514/6.2009-7259
[research_smart_tetlow_2006]: https://doi.org/10.2514/6.2006-8019
[research_smartmichaelk_rufedwardg_2006]: https://ntrs.nasa.gov/citations/20060020177
[research_smartmichaelk_trexlercarla_2003]: https://ntrs.nasa.gov/citations/20030012601
[research_smayda_2017]: https://doi.org/10.18130/v3dr44
[research_smirnov_nikitin_2023]: https://doi.org/10.3390/fire6090335
[research_smith_1979]: https://doi.org/10.21236/ada067968
[research_smith_1989]: https://doi.org/10.1016/0360-3199(89)90054-2
[research_smith_2021]: https://doi.org/10.1063/pt.3.4888
[research_smith_schetz_2002]: https://doi.org/10.2514/6.2002-3134
[research_smith_walker_2002]: https://doi.org/10.2514/6.2002-3133
[research_smithey_fuhs_1977]: https://doi.org/10.2514/3.58886
[research_smithlm_1978]: https://ntrs.nasa.gov/citations/19790013260
[research_smits_2007]: https://doi.org/10.21236/ada465164
[research_smits_2009]: https://doi.org/10.21236/ada499452
[research_son_ko_2024]: https://doi.org/10.1016/j.ast.2024.109366
[research_song_choi_2020]: https://doi.org/10.1016/j.ifacol.2020.12.1900
[research_song_luo_2022]: https://doi.org/10.3390/math10183401
[research_song_su_2015]: https://doi.org/10.1016/j.proeng.2014.12.639
[research_song_xu_2026]: https://doi.org/10.1016/j.ast.2025.110949
[research_song_zhao_2020]: https://doi.org/10.1063/1.5140222
[research_soni_de_2017]: https://doi.org/10.1007/s12206-017-0215-0
[research_sorensen_latham_1975]: https://doi.org/10.2514/3.44491
[research_sorensen_smeltzer_1972]: https://doi.org/10.2514/3.59067
[research_sorensen_smeltzer_1973]: https://doi.org/10.2514/3.44367
[research_sorensenne_benczedp_1973]: https://ntrs.nasa.gov/citations/19740028534
[research_soumyajitsaha_debasischakraborty_2023]: https://doi.org/10.61653/joast.v63i4.2011.594
[research_spaid_keener_1995]: https://ntrs.nasa.gov/citations/19950016830
[research_spain_zeiler_1993]: https://ntrs.nasa.gov/citations/19930049893
[research_spain_zeiler_1993_b]: https://ntrs.nasa.gov/citations/19930053430
[research_spanostheodorosa_2009]: https://ntrs.nasa.gov/citations/20110008506
[research_species_measurements_1996]: https://doi.org/10.1016/s0140-6701(97)83795-2
[research_spencer_1962]: https://doi.org/10.21236/ad0408919
[research_sponable_1995]: https://doi.org/10.2514/6.1995-3004
[research_spravka_jorris_2015]: https://doi.org/10.21236/ada619521
[research_sprinkle_davis_1999]: https://ntrs.nasa.gov/citations/20000005107
[research_sprunger_lasorsa_2025]: https://doi.org/10.1016/j.combustflame.2025.114044
[research_sreekanth_reddy_1995]: https://doi.org/10.2514/3.701
[research_sreekireddy_reddy_2019]: https://doi.org/10.1016/j.applthermaleng.2018.10.078
[research_srinivasan_erickson_1995]: https://doi.org/10.2514/6.1995-2719
[research_srinivasan_mahapatra_2020]: https://doi.org/10.1080/14685248.2019.1710517
[research_sriram_ram_2015]: https://doi.org/10.1088/0957-0233/26/9/095301
[research_stainbackpc_1969]: https://ntrs.nasa.gov/citations/19690005540
[research_stalder_1957]: https://doi.org/10.2514/8.12492
[research_stalker_morgan_1984]: https://doi.org/10.1016/0010-2180(84)90137-8
[research_stalker_morgan_1987]: https://ntrs.nasa.gov/citations/19870058909
[research_stalker_morgan_1988]: https://doi.org/10.1016/0010-2180(88)90106-x
[research_stalker_morgan_1996]: https://doi.org/10.2514/6.1996-4534
[research_stalker_simmons_1994]: https://doi.org/10.2514/6.1994-2516
[research_stalker_simmons_1995]: https://ntrs.nasa.gov/citations/19960001679
[research_stalkerrj_1996]: https://ntrs.nasa.gov/citations/19970026342
[research_stalkerrj_bakosrj_1995]: https://ntrs.nasa.gov/citations/19950018974
[research_stalkerrj_hollisp_1993]: https://ntrs.nasa.gov/citations/19940019059
[research_stallings_burt_1984]: https://doi.org/10.2514/6.1984-605
[research_stallings_williams_2003]: https://doi.org/10.21236/ada412642
[research_stanley_engelund_1994]: https://doi.org/10.2514/3.26454
[research_stanley_lopp_2013]: https://doi.org/10.21236/ada591565
[research_stanley_wilhite_1991]: https://ntrs.nasa.gov/citations/19920035188
[research_stanley_wilhite_1992]: https://doi.org/10.2514/3.11518
[research_stanleythomastroy_alexanderreginald_1999]: https://ntrs.nasa.gov/citations/19990102866
[research_stanleythomastroy_alexanderreginald_2000]: https://ntrs.nasa.gov/citations/20000021504
[research_stapp_1995]: https://doi.org/10.1117/12.194195
[research_star_edwards_2005]: https://doi.org/10.2514/6.2005-428
[research_star_edwards_2006]: https://doi.org/10.2514/6.2006-3040
[research_starkey_rankins_2006]: https://doi.org/10.2514/6.2006-337
[research_stauffer_takahashi_2023]: https://doi.org/10.2514/6.2023-1553
[research_stechmann_heister_2019]: https://doi.org/10.2514/1.a34313
[research_stefaniya_pushpalatha_2025]: https://doi.org/10.1134/s001546282560227x
[research_steffen_bond_2002]: https://ntrs.nasa.gov/citations/20020061704
[research_steffenchristopherjjr_yungstershaye_2001]: https://ntrs.nasa.gov/citations/20010050137
[research_steinetz_1991]: https://ntrs.nasa.gov/citations/19920005885
[research_steinetzbrucem_2008]: https://ntrs.nasa.gov/citations/20080047343
[research_steinetzbrucem_melismatthewe_1991]: https://ntrs.nasa.gov/citations/19910010128
[research_stennett_2020]: https://doi.org/10.14264/uql.2020.925
[research_stennett_gildfind_2019]: https://doi.org/10.1007/978-3-319-91017-8_23
[research_stephan_obermeier_1974]: https://doi.org/10.1615/ihtc5.2210
[research_stephan_schneider_1991]: https://doi.org/10.2514/6.1991-5047
[research_stephensjr_1974]: https://ntrs.nasa.gov/citations/19740057316
[research_stetson_1986]: https://doi.org/10.21236/ada178877
[research_stetson_1990]: https://doi.org/10.21236/ada227242
[research_stewar_morgan_2003]: https://doi.org/10.2514/2.6085
[research_stewart_1973]: https://doi.org/10.21236/ad0525631
[research_stewart_2017]: https://doi.org/10.2514/6.2017-4916
[research_stewart_2024]: https://doi.org/10.14264/267592
[research_stewart_morgan_2000]: https://doi.org/10.2514/6.2000-2595
[research_stewartdavid_leiserdaniel_2007]: https://ntrs.nasa.gov/citations/20100011117
[research_stewartdavida_leiserdanielb_2010]: https://ntrs.nasa.gov/citations/20100042283
[research_stewartmem_suresha_2002]: https://ntrs.nasa.gov/citations/20020090948
[research_stickler_keller_1998]: https://doi.org/10.1063/1.54717
[research_stilla_1994]: https://doi.org/10.2514/3.46659
[research_stolzenburg_1965]: https://doi.org/10.5594/j06018
[research_stoneje_1975]: https://ntrs.nasa.gov/citations/19750018926
[research_storch_bynum_2011]: https://ntrs.nasa.gov/citations/20110010976
[research_strangman_keiser_1988]: https://doi.org/10.1016/0008-6223(88)90240-0
[research_streby_mathur_1999]: https://doi.org/10.21236/ada372847
[research_street_2024]: https://doi.org/10.14264/340dbcb
[research_streiff_1953]: https://doi.org/10.21236/ad0041742
[research_strokin_khailov_1974]: https://doi.org/10.1007/bf01464177
[research_stroud_miller_1966]: https://doi.org/10.2514/3.43775
[research_structure_and_1992]: https://doi.org/10.1016/0026-0657(92)91224-8
[research_structure_and_1997]: https://doi.org/10.1016/s0026-0657(97)86936-6
[research_strutjet_rocket_based_2001]: https://doi.org/10.2514/5.9781600866609.0697.0755
[research_stull_1989]: https://doi.org/10.2514/6.1989-5012
[research_su_2017]: https://doi.org/10.2514/6.2017-2297
[research_su_chen_2018]: https://doi.org/10.1016/j.actaastro.2017.10.040
[research_su_liu_2025]: https://doi.org/10.1016/j.asoc.2024.112637
[research_su_wang_2015]: https://doi.org/10.1016/j.neucom.2015.03.063
[research_su_wang_2019]: https://doi.org/10.1016/j.ijheatmasstransfer.2018.09.123
[research_su_wu_2023]: https://doi.org/10.1049/icp.2022.2978
[research_su_zhao_2024]: https://doi.org/10.1088/1742-6596/2764/1/012069
[research_subrahmanyam_annapurna_1986]: https://doi.org/10.1007/bf00659189
[research_subramanian_dwarakanath_1969]: https://doi.org/10.1007/bf00411620
[research_subramanian_meadows_2020]: https://doi.org/10.2514/1.b37719
[research_sudalagunta_sultan_2018]: https://doi.org/10.2514/1.g002777
[research_sudhieshkumar_reddy_2015]: https://doi.org/10.1007/s00193-015-0608-x
[research_sugavanam_sastry_1975]: https://doi.org/10.2514/3.49665
[research_sullins_waltrup_1985]: https://doi.org/10.2514/3.22774
[research_sun_2018]: https://doi.org/10.31274/rtd-180813-14281
[research_sun_ding_2026]: https://doi.org/10.2514/1.j067279
[research_sun_guo_2019]: https://doi.org/10.1063/1.5123453
[research_sun_jing_2024]: https://doi.org/10.2514/1.g008075
[research_sun_li_2019]: https://doi.org/10.1016/j.fuel.2018.11.003
[research_sun_li_2021]: https://doi.org/10.1016/j.ast.2021.106901
[research_sun_wu_2023]: https://doi.org/10.1049/icp.2022.3063
[research_sun_xue_2025]: https://doi.org/10.1016/j.ast.2025.110525
[research_sun_yang_2020]: https://doi.org/10.1155/2020/3850283
[research_sun_yang_2020_b]: https://doi.org/10.12783/dtcse/cmso2019/33628
[research_sun_yu_2025]: https://doi.org/10.1063/5.0257367
[research_sun_yu_2026]: https://doi.org/10.1016/j.ast.2026.112248
[research_sun_zhou_2018]: https://doi.org/10.1016/j.ast.2018.08.024
[research_sun_zhu_2019]: https://doi.org/10.1063/1.5083820
[research_sunami_itoh_2006]: https://doi.org/10.2514/6.2006-8062
[research_suneetha_randive_2019]: https://doi.org/10.1016/j.matpr.2019.06.282
[research_suneetha_randive_2021]: https://doi.org/10.1016/j.actaastro.2021.05.032
[research_sung_jeong_2024]: https://doi.org/10.2514/6.2024-1416
[research_sung_kim_2026]: https://doi.org/10.1016/j.ast.2025.111001
[research_sunjian_liuweiqiang_2013]: https://doi.org/10.7498/aps.62.074401
[research_superconducting_liquid_level_1967]: https://doi.org/10.1016/0042-207x(67)91396-6
[research_supersonic_and_2019]: https://doi.org/10.35940/ijrte.b1590.0982s1119
[research_supersonic_combustion_2009]: https://doi.org/10.1017/cbo9780511627019.007
[research_supersonic_flow_2001]: https://doi.org/10.2514/5.9781600866609.0513.0568
[research_suraweera_2024]: https://doi.org/10.14264/158241
[research_suraweera_smart_2008]: https://doi.org/10.2514/6.2008-100
[research_surber_sedlock_1979]: https://doi.org/10.2514/3.58575
[research_suresh_liou_1992]: https://ntrs.nasa.gov/citations/19920016574
[research_surface_roughness_1973]: https://doi.org/10.2514/5.9781600865053.0435.0453
[research_survey_of_1962]: https://doi.org/10.2514/5.9781600864810.0651.0662
[research_suryanarayanan_goldstein_2019]: https://doi.org/10.1063/1.5075635
[research_surzhikov_2018]: https://doi.org/10.1134/s1028335818020039
[research_surzhikov_2019]: https://doi.org/10.33257/phchgd.20.4.892
[research_surzhikov_2021]: https://doi.org/10.33257/phchgd.22.1.931
[research_surzhikov_2021_b]: https://doi.org/10.33257/phchgd.22.1.930
[research_surzhikov_2022]: https://doi.org/10.1134/s001546282260122x
[research_swain_p_2020]: https://doi.org/10.1080/00102202.2020.1791838
[research_swansongreg_kazembacole_2014]: https://ntrs.nasa.gov/citations/20150000181
[research_swansongregorytodd_cassellalanm_2014]: https://ntrs.nasa.gov/citations/20190001057
[research_swansongt_kazembacd_2015]: https://ntrs.nasa.gov/citations/20150011064
[research_swartzbaugh_1997]: https://doi.org/10.21236/ada344488
[research_swiss_students_2025]: https://doi.org/10.12968/s1478-2774(25)50079-0
[research_swithebank_chigier_1969]: https://doi.org/10.1016/s0082-0784(69)80492-3
[research_swithenbank_1967]: https://doi.org/10.1016/0376-0421(67)90005-x
[research_swithenbank_jaques_1970]: https://doi.org/10.21236/ad0709222
[research_synthesis_of_1994]: https://doi.org/10.1016/0026-0657(94)91919-4
[research_sypniewski_1989]: https://doi.org/10.2514/6.1989-5017
[research_tabakoff_mcdonel_1966]: https://doi.org/10.2514/3.3399
[research_tahir_2021]: https://doi.org/10.32920/ryerson.14644473.v1
[research_takahashi_mizobata_1997]: https://doi.org/10.2514/6.1997-192
[research_takahashi_munakata_2018]: https://doi.org/10.3390/aerospace5010019
[research_takahashi_tomioka_2021]: https://doi.org/10.2322/tastj.19.415
[research_takahashi_ueda_1999]: https://doi.org/10.2514/6.1999-4961
[research_takahashi_wakai_1998]: https://doi.org/10.1016/s0082-0784(98)80062-3
[research_takashiman_kothariap_1998]: https://ntrs.nasa.gov/citations/19990079881
[research_tam_hagenmaier_1999]: https://doi.org/10.2514/6.1999-613
[research_tamagno_bakos_1990]: https://doi.org/10.2514/6.1990-1390
[research_tanabe_yasuda_1987]: https://doi.org/10.7209/tanso.1987.181
[research_tanatsugu_carrick_2003]: https://doi.org/10.2514/6.2003-2586
[research_tang_fan_2026]: https://doi.org/10.1016/j.ast.2026.111869
[research_tang_gao_2015]: https://doi.org/10.2514/6.2015-4681
[research_tang_li_2025]: https://doi.org/10.1063/5.0256817
[research_tang_wang_2019]: https://doi.org/10.1360/sspma2018-00414
[research_tang_wang_2021]: https://doi.org/10.1063/5.0069666
[research_tang_wang_2022]: https://doi.org/10.1016/j.ast.2022.107633
[research_tang_wang_2024]: https://doi.org/10.1016/j.combustflame.2024.113431
[research_tang_xiong_2023]: https://doi.org/10.3390/app13179752
[research_tang_xu_2024]: https://doi.org/10.1017/jfm.2024.641
[research_tank_1991]: https://ntrs.nasa.gov/citations/19910018900
[research_tanno_komuro_2001]: https://doi.org/10.2514/6.2001-1889
[research_tanno_tanno_2021]: https://doi.org/10.1007/s00348-021-03229-0
[research_tariq_wasim_2026]: https://doi.org/10.3390/pr14152458
[research_tarpley_lewis_1995]: https://doi.org/10.2514/6.1995-848
[research_tatman_2017]: https://doi.org/10.18130/v3g36z
[research_taylor_1968]: https://doi.org/10.1017/s0001924000084347
[research_taylor_jackson_1980]: https://ntrs.nasa.gov/citations/19800039780
[research_teddersarahaugustaumberger_2010]: https://ntrs.nasa.gov/citations/20100026458
[research_telectromekincfortwaynein_1965]: https://doi.org/10.21236/ad0654210
[research_teng_yuan_2015]: https://doi.org/10.1016/j.ast.2015.01.011
[research_test_method_2008]: https://doi.org/10.1520/e0637-98
[research_tetervin_1961]: https://doi.org/10.2514/8.8896
[research_tewfik_giedt_1960]: https://doi.org/10.2514/8.8737
[research_tharakan_sukesh_2025]: https://doi.org/10.1615/intjenergeticmaterialschemprop.2025058828
[research_thawait_tandaiya_2023]: https://doi.org/10.1063/5.0165168
[research_thawait_tandaiya_2023_b]: https://doi.org/10.1007/s00707-023-03495-5
[research_the_free_1962]: https://doi.org/10.2514/5.9781600864810.0627.0650
[research_the_quest_2011]: https://doi.org/10.2514/5.9781600867774.0001.0014
[research_thelander_1966]: https://doi.org/10.2514/3.28449
[research_thiele_gampe_2018]: https://doi.org/10.1115/1.4041129
[research_thomas_2011]: https://ntrs.nasa.gov/citations/20110011395
[research_thomas_guy_1982]: https://ntrs.nasa.gov/citations/19820051545
[research_thomas_guy_1983]: https://ntrs.nasa.gov/citations/19830027768
[research_thomas_lee_2010]: https://ntrs.nasa.gov/citations/20110004251
[research_thomas_palac_2001]: https://ntrs.nasa.gov/citations/20010092480
[research_thomas_perlbachs_1967]: https://doi.org/10.21236/ad0655383
[research_thomas_powell_1992]: https://ntrs.nasa.gov/citations/19920055945
[research_thomas_voland_1987]: https://ntrs.nasa.gov/citations/19870058171
[research_thomas_walker_2009]: https://ntrs.nasa.gov/citations/20110012002
[research_thomasjl_rudydh_1988]: https://ntrs.nasa.gov/citations/19890047357
[research_thomasscottr_guyrwayne_1990]: https://ntrs.nasa.gov/citations/19900051430
[research_thomasscottr_perkinshdouglas_1997]: https://ntrs.nasa.gov/citations/19970017381
[research_thompson_chu_1996]: https://doi.org/10.1016/1359-6462(96)00282-5
[research_thompson_friedman_1991]: https://doi.org/10.2514/6.1991-5104
[research_thompson_hull_1970]: https://doi.org/10.1007/bf00927442
[research_thompson_pandolfini_1995]: https://doi.org/10.2514/6.1995-6130
[research_thompsonhdoyle_hoffmanjoed_1992]: https://ntrs.nasa.gov/citations/19930003026
[research_thornton_oden_1990]: https://doi.org/10.2514/3.45943
[research_throckmorton_1989]: https://doi.org/10.2514/6.1989-5009
[research_throttle_dependent_forces_1985]: https://doi.org/10.2514/5.9781600865732.0207.0280
[research_thrust_and_2021]: https://doi.org/10.2514/5.9781624105920.0289.0354
[research_thrust_drag_accounting_1985]: https://doi.org/10.2514/5.9781600865732.0029.0045
[research_tian_bai_2025]: https://doi.org/10.1063/5.0247229
[research_tian_liu_2022]: https://doi.org/10.1063/5.0096772
[research_tian_liu_2026]: https://doi.org/10.2514/1.j066483
[research_tian_shen_2022]: https://doi.org/10.1177/16878132221111208
[research_tian_yang_2016]: https://doi.org/10.1016/j.ast.2016.02.027
[research_tian_yang_2023]: https://doi.org/10.1016/j.ast.2023.108357
[research_tian_yang_2024]: https://doi.org/10.1016/j.jclepro.2024.143247
[research_tian_zeng_2018]: https://doi.org/10.1016/j.ast.2018.08.026
[research_timofeev_voinovich_2001]: https://doi.org/10.2514/6.2001-1896
[research_tirskii_1993]: https://doi.org/10.1007/bf00570739
[research_tirsky_1993]: https://doi.org/10.1146/annurev.fl.25.010193.001055
[research_tirtey_boyce_2009]: https://doi.org/10.2514/6.2009-7295
[research_titanium_aluminide_1992]: https://doi.org/10.1016/0026-0657(92)91460-2
[research_titanium_aluminide_2012]: https://doi.org/10.31399/asm.tb.lmub.t53550299
[research_tobias_agrawal_2023]: https://doi.org/10.2514/1.b38874
[research_tokarcikpolskys_papadopoulosp_1995]: https://ntrs.nasa.gov/citations/20020038862
[research_tokuda_yang_2019]: https://doi.org/10.1615/ihtc3.1840
[research_tolstykh_1969]: https://doi.org/10.1007/bf01032489
[research_tomioka_hiraiwa_2007]: https://doi.org/10.2514/1.28149
[research_tomioka_hiraiwa_2009]: https://doi.org/10.2322/tstj.7.pa_47
[research_tomioka_takegoshi_2021]: https://doi.org/10.2514/1.b37683
[research_tomioka_ueda_2007]: https://doi.org/10.2514/6.2007-1040
[research_tong_duan_2023]: https://doi.org/10.1080/14685248.2023.2260777
[research_tong_giedt_1963]: https://doi.org/10.21236/ad0403711
[research_tong_li_2025]: https://doi.org/10.1109/jsen.2025.3538625
[research_toniato_2019]: https://doi.org/10.14264/uql.2019.342
[research_toniato_gildfind_2018]: https://doi.org/10.2514/6.2018-3818
[research_torre_merli_2023]: https://doi.org/10.1115/1.4064067
[research_torresabelo_1992]: https://ntrs.nasa.gov/citations/19930062819
[research_torrez_driscoll_2009]: https://doi.org/10.2514/6.2009-6152
[research_toten_fong_1991]: https://doi.org/10.2514/6.1991-5080
[research_tournes_2013]: https://doi.org/10.2514/6.2013-4609
[research_townend_1995]: https://doi.org/10.1017/s0001924000049666
[research_trefny_1999]: https://doi.org/10.2514/6.1999-2730
[research_trefnycharlesj_dippoldvancefiii_2017]: https://ntrs.nasa.gov/citations/20170008733
[research_trevino_1995]: https://doi.org/10.1016/0010-2180(95)00052-8
[research_trexler_1974]: https://doi.org/10.2514/3.60393
[research_trexlerca_1975]: https://ntrs.nasa.gov/citations/19750061560
[research_trexlercarla_1988]: https://ntrs.nasa.gov/citations/19880057583
[research_triantou_mergia_2017]: https://doi.org/10.1016/j.compositesb.2016.12.020
[research_triantou_perez_2017]: https://doi.org/10.1016/j.compositesb.2016.09.104
[research_trimmer_1968]: https://doi.org/10.21236/ad0669378
[research_trivedi_menezes_2012]: https://doi.org/10.1016/j.measurement.2012.04.008
[research_trolier_krawczyk_1996]: https://doi.org/10.2514/6.1996-2235
[research_trudgian_vanyai_2025]: https://doi.org/10.1016/j.ast.2025.110310
[research_trujillo_1970]: https://doi.org/10.2514/3.30096
[research_tsai_1991]: https://ntrs.nasa.gov/citations/19910011781
[research_tsentis_gkoutzamanis_2021]: https://doi.org/10.1017/aer.2021.3
[research_tsuboi_eto_2017]: https://doi.org/10.2514/1.b36095
[research_tsuchiya_mori_2005]: https://doi.org/10.2514/1.8012
[research_tsujikawa_1995]: https://doi.org/10.1016/0360-3199(94)00098-k
[research_tsujikawa_1996]: https://doi.org/10.1016/0360-3199(95)00077-1
[research_tsujikawa_tsukamoto_1991]: https://doi.org/10.1016/0360-3199(91)90040-p
[research_tsunekawa_gotoh_1992]: https://doi.org/10.1007/bf02646777
[research_tufts_gosse_2018]: https://doi.org/10.2514/1.a34149
[research_tumuklu_hanquist_2023]: https://doi.org/10.1063/5.0169648
[research_turchi_matesanzsaiz_2021]: https://doi.org/10.1007/s00348-021-03320-6
[research_turkoglu_donmez_2026]: https://doi.org/10.1016/j.ast.2026.113022
[research_turner_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50015-4
[research_turner_hoerschgen_2006]: https://doi.org/10.2514/6.2006-8115
[research_tuttle_2021]: https://doi.org/10.14264/545af79
[research_tuttle_mee_1995]: https://ntrs.nasa.gov/citations/19960001678
[research_tuttle_rogacki_1991]: https://ntrs.nasa.gov/citations/19920002173
[research_tuttlesean_1995]: https://ntrs.nasa.gov/citations/19950018977
[research_tyll_bakos_2000]: https://doi.org/10.2514/6.2000-2442
[research_ueda_weiland_2004]: https://doi.org/10.2514/6.2004-2397
[research_ulislamrizvi_linshu_2015]: https://doi.org/10.1108/aeat-04-2013-0079
[research_ullman_raman_2023]: https://doi.org/10.1080/00102202.2023.2239447
[research_ullman_sharma_2025]: https://doi.org/10.1016/j.jaecs.2025.100353
[research_universalenergysystemsincdaytonoh_1995]: https://doi.org/10.21236/ada302115
[research_universaltechnologycorpdaytonoh_2014]: https://doi.org/10.21236/ada618909
[research_unsteady_interaction_2023]: https://doi.org/10.1063/5.0151663
[research_unterberg_1957]: https://doi.org/10.2514/8.12848
[research_upsadhya_2001]: https://doi.org/10.21236/ada388213
[research_urso_kinney_2022]: https://doi.org/10.1063/5.0084047
[research_urzay_2018]: https://doi.org/10.1146/annurev-fluid-122316-045217
[research_ustinov_kachanov_2021]: https://doi.org/10.1063/5.0057853
[research_utilization_of_2001]: https://doi.org/10.1016/s0026-0657(01)80813-4
[research_uy_hao_2023]: https://doi.org/10.1016/j.ast.2023.108520
[research_vachon_grindle_2005]: https://ntrs.nasa.gov/citations/20050182779
[research_vaden_debes_2009]: https://ntrs.nasa.gov/citations/20090033784
[research_vahlwa_edwardsclw_1978]: https://ntrs.nasa.gov/citations/19780036739
[research_vaicaitis_1991]: https://doi.org/10.2514/6.1991-1177
[research_val_chazot_2020]: https://doi.org/10.1007/978-3-030-60166-9_16
[research_van_1963]: https://doi.org/10.21236/ad0408349
[research_vanamamalai_panneerselvam_2024]: https://doi.org/10.24425/ather.2024.151227
[research_vanbeck_raman_2024]: https://doi.org/10.1016/j.proci.2024.105606
[research_vanburen_mease_1991]: https://doi.org/10.2514/6.1991-5054
[research_vanderlee_kaner_2026]: https://doi.org/10.2514/1.b40338
[research_vanderlee_yokev_2022]: https://doi.org/10.2514/1.b38683
[research_vanderschaaf_acharya_2025]: https://doi.org/10.1063/5.0281488
[research_vankeuk_ballmann_1998]: https://doi.org/10.2514/6.1998-1526
[research_vanmol_andersonjr_1992]: https://doi.org/10.2514/6.1992-2920
[research_vanstaden_lorrain_2020]: https://doi.org/10.2514/1.j059177
[research_vanwie_1992]: https://doi.org/10.2514/6.1992-5104
[research_vanyai_2018]: https://doi.org/10.14264/uql.2018.247
[research_vargasvenegas_huang_2023]: https://doi.org/10.2514/1.j062214
[research_varner_1976]: https://doi.org/10.21236/ada032725
[research_varnermo_martindalewr_1987]: https://ntrs.nasa.gov/citations/19870000547
[research_varwig_1963]: https://doi.org/10.21236/ad0403052
[research_vasilev_petrov_1977]: https://doi.org/10.1007/bf01050476
[research_veeramanikandan_2023]: https://doi.org/10.61359/11.2106-2310
[research_veeran_pesyridis_2018]: https://doi.org/10.3390/en11102558
[research_venegas_huang_2026]: https://doi.org/10.1007/s00158-026-04258-1
[research_venkatachalam_esser_2024]: https://doi.org/10.1016/j.compositesa.2024.108358
[research_venkatapathy_1994]: https://ntrs.nasa.gov/citations/19940030992
[research_venkatapathy_tokarcikpolsky_1995]: https://ntrs.nasa.gov/citations/20010122932
[research_venkatesan_s_2024]: https://doi.org/10.61359/11.2106-2412
[research_venkateshwaran_padmanathan_2026]: https://doi.org/10.1016/j.rineng.2026.110667
[research_verant_sagnier_1996]: https://doi.org/10.2514/6.1996-2239
[research_verma_pandey_2021]: https://doi.org/10.1016/j.matpr.2020.07.388
[research_vert_bouchard_2024]: https://doi.org/10.12968/s1478-2774(25)50011-x
[research_viaud_mestre_1966]: https://doi.org/10.1108/eb034121
[research_vigilante_cote_1997]: https://doi.org/10.21236/ada324040
[research_vinogradov_stepanov_1992]: https://doi.org/10.2514/3.23455
[research_vinson_shore_1967]: https://doi.org/10.21236/ad0656056
[research_vlassak_2008]: https://doi.org/10.21236/ada588148
[research_voland_1990]: https://doi.org/10.2514/6.1990-2340
[research_voland_auslender_1999]: https://ntrs.nasa.gov/citations/20040087160
[research_voland_huebner_2005]: https://ntrs.nasa.gov/citations/20050239566
[research_voland_huebner_2006]: https://doi.org/10.1016/j.actaastro.2006.02.021
[research_voland_rock_1998]: https://ntrs.nasa.gov/citations/20040088578
[research_volkov_emelyanov_2015]: https://doi.org/10.1134/s0021894415050053
[research_volpiani_2021]: https://doi.org/10.1007/s00193-021-01018-6
[research_voronin_2020]: https://doi.org/10.37394/232012.2020.15.17
[research_voth_ludtke_1979]: https://doi.org/10.6028/nbs.ir.79-1607
[research_vuillermoz_oran_1992]: https://doi.org/10.1016/s0082-0784(06)80051-2
[research_vyasmanana_engblomwilliama_2010]: https://ntrs.nasa.gov/citations/20100029603
[research_wada_2026]: https://doi.org/10.1201/9781003760528-11
[research_wadhams_maclean_2008]: https://doi.org/10.21236/ada481623
[research_wadley_elzey_1990]: https://ntrs.nasa.gov/citations/19910031422
[research_wagner_dale_1985]: https://doi.org/10.21236/ada379715
[research_waidmann_brummund_2024]: https://doi.org/10.1201/9780203735138-143
[research_walchner_1974]: https://doi.org/10.21236/ada007045
[research_waldman_harsha_1992]: https://ntrs.nasa.gov/citations/19930038281
[research_walker_1952]: https://doi.org/10.21236/ad0041745
[research_walker_2025]: https://doi.org/10.18278/sesa.5.4.5
[research_wallaceta_birdrk_2003]: https://ntrs.nasa.gov/citations/20040012943
[research_walsh_zhan_2024]: https://doi.org/10.2514/6.2024-2427
[research_walton_1991]: https://ntrs.nasa.gov/citations/19910000096
[research_walton_pinckney_1994]: https://ntrs.nasa.gov/citations/19940000062
[research_waltonjamest_1992]: https://ntrs.nasa.gov/citations/19930006339
[research_waltonjt_1990]: https://ntrs.nasa.gov/citations/19900000647
[research_waltrup_billig_1981]: https://doi.org/10.2514/3.28060
[research_waltrup_white_1996]: https://doi.org/10.2514/6.1996-3152
[research_wan_ma_2025]: https://doi.org/10.1016/j.actaastro.2025.06.055
[research_wan_shi_2026]: https://doi.org/10.1016/j.actaastro.2026.02.024
[research_wan_wang_2026]: https://doi.org/10.1016/j.ast.2026.112088
[research_wang_2023]: https://doi.org/10.54254/2753-8818/5/20230403
[research_wang_an_2025]: https://doi.org/10.1063/5.0295712
[research_wang_cai_2016]: https://doi.org/10.1016/j.ijhydene.2016.09.012
[research_wang_cai_2017]: https://doi.org/10.1016/j.cja.2017.05.002
[research_wang_chang_2021]: https://doi.org/10.1063/5.0047665
[research_wang_chen_2020]: https://doi.org/10.3390/sym12091572
[research_wang_chen_2026]: https://doi.org/10.1016/j.ast.2026.111727
[research_wang_cheng_2020]: https://doi.org/10.1016/j.ast.2019.105594
[research_wang_cheng_2020_b]: https://doi.org/10.1016/j.ast.2020.106115
[research_wang_cheng_2022]: https://doi.org/10.1016/j.energy.2022.123606
[research_wang_cheng_2026]: https://doi.org/10.1016/j.ast.2026.112326
[research_wang_dang_2021]: https://doi.org/10.2139/ssrn.3980387
[research_wang_du_2026]: https://doi.org/10.1016/j.ast.2025.111542
[research_wang_eri_2023]: https://doi.org/10.1016/j.applthermaleng.2023.120596
[research_wang_eri_2023_b]: https://doi.org/10.1016/j.applthermaleng.2023.120827
[research_wang_fan_2022]: https://doi.org/10.23919/jsee.2022.000019
[research_wang_fan_2023]: https://doi.org/10.1016/j.actaastro.2023.06.043
[research_wang_fang_2026]: https://doi.org/10.1016/j.energy.2026.142138
[research_wang_gao_2021]: https://doi.org/10.1016/j.jeurceramsoc.2021.03.051
[research_wang_gao_2022]: https://doi.org/10.3390/ma15248860
[research_wang_guo_2013]: https://doi.org/10.1016/j.cja.2013.04.018
[research_wang_guo_2019]: https://doi.org/10.1049/iet-cta.2018.5482
[research_wang_guo_2026]: https://doi.org/10.2139/ssrn.7359964
[research_wang_ha_2021]: https://doi.org/10.1016/j.enconman.2021.114184
[research_wang_he_2018]: https://doi.org/10.1016/j.actaastro.2018.06.028
[research_wang_he_2021]: https://doi.org/10.1016/j.actaastro.2021.06.050
[research_wang_he_2025]: https://doi.org/10.1371/journal.pone.0328630
[research_wang_hong_2026]: https://doi.org/10.1063/5.0307799
[research_wang_hou_2018]: https://doi.org/10.1088/1757-899x/449/1/012006
[research_wang_hou_2019]: https://doi.org/10.1109/access.2019.2918848
[research_wang_hou_2021]: https://doi.org/10.1016/j.energy.2020.119271
[research_wang_huang_2023]: https://doi.org/10.1016/j.fuel.2022.126619
[research_wang_huang_2026]: https://doi.org/10.1016/j.jeurceramsoc.2025.118061
[research_wang_jiang_2020]: https://doi.org/10.3390/s20216179
[research_wang_jin_2022]: https://doi.org/10.1016/j.applthermaleng.2021.117661
[research_wang_jordan_2025]: https://doi.org/10.58895/hysafe.35
[research_wang_li_2016]: https://doi.org/10.1007/s10443-016-9548-6
[research_wang_li_2018]: https://doi.org/10.1016/j.ijheatmasstransfer.2018.03.092
[research_wang_li_2018_b]: https://doi.org/10.1007/s11630-018-1020-5
[research_wang_li_2020]: https://doi.org/10.1016/j.ijhydene.2019.11.118
[research_wang_li_2022]: https://doi.org/10.1016/j.egyr.2022.05.019
[research_wang_liu_2016]: https://doi.org/10.1063/1.4950781
[research_wang_liu_2016_b]: https://doi.org/10.1007/s00193-015-0616-x
[research_wang_liu_2017]: https://doi.org/10.2514/6.2017-0486
[research_wang_liu_2019]: https://doi.org/10.1007/978-3-319-91017-8_20
[research_wang_liu_2023]: https://doi.org/10.1016/j.fuel.2022.125732
[research_wang_liu_2024]: https://doi.org/10.33737/jgpps/187745
[research_wang_liu_2025]: https://doi.org/10.1080/01457632.2025.2571269
[research_wang_liu_2025_b]: https://doi.org/10.3390/aerospace12030242
[research_wang_luo_2022]: https://doi.org/10.3390/app122110734
[research_wang_nie_2019]: https://doi.org/10.1177/1687814019830283
[research_wang_pan_2018]: https://doi.org/10.1088/1742-6596/1064/1/012001
[research_wang_pan_2024]: https://doi.org/10.1016/j.applthermaleng.2023.122324
[research_wang_qian_2023]: https://doi.org/10.1016/j.tsep.2023.101792
[research_wang_shan_2015]: https://doi.org/10.1016/j.ijhydene.2014.10.124
[research_wang_song_2026]: https://doi.org/10.1016/j.cja.2026.104219
[research_wang_tang_2025]: https://doi.org/10.1088/1742-6596/3041/1/012024
[research_wang_wang_2014]: https://doi.org/10.2514/1.b35289
[research_wang_wang_2015]: https://doi.org/10.1016/j.actaastro.2014.12.008
[research_wang_wang_2016]: https://doi.org/10.1016/j.actaastro.2016.06.022
[research_wang_wang_2018]: https://doi.org/10.1016/j.actaastro.2018.10.013
[research_wang_wang_2019]: https://doi.org/10.1007/s42405-019-00217-x
[research_wang_wang_2022]: https://doi.org/10.1016/j.ast.2022.107995
[research_wang_wang_2023]: https://doi.org/10.2514/1.a35390
[research_wang_wang_2024]: https://doi.org/10.1038/s41598-024-61900-y
[research_wang_wang_2024_b]: https://doi.org/10.1016/j.actaastro.2024.01.002
[research_wang_wang_2024_c]: https://doi.org/10.1109/cac63892.2024.10865158
[research_wang_wei_2019]: https://doi.org/10.1016/j.compstruct.2018.11.004
[research_wang_wei_2022]: https://doi.org/10.3390/app121910153
[research_wang_xiao_2016]: https://doi.org/10.1016/j.ast.2016.07.004
[research_wang_xin_2022]: https://doi.org/10.1016/j.actaastro.2022.07.057
[research_wang_xu_2023]: https://doi.org/10.1007/s00158-023-03635-4
[research_wang_xu_2023_b]: https://doi.org/10.2139/ssrn.4435085
[research_wang_xu_2024]: https://doi.org/10.1016/j.ijthermalsci.2023.108857
[research_wang_xu_2024_b]: https://doi.org/10.1017/jfm.2024.595
[research_wang_xu_2025]: https://doi.org/10.1016/j.fuel.2024.133201
[research_wang_xue_2019]: https://doi.org/10.2514/1.j057352
[research_wang_yang_2017]: https://doi.org/10.1016/j.applthermaleng.2017.01.059
[research_wang_yang_2020]: https://doi.org/10.1016/j.fuproc.2019.106229
[research_wang_yang_2025]: https://doi.org/10.1016/j.jfranklin.2024.107426
[research_wang_yao_2025]: https://doi.org/10.2514/1.j064599
[research_wang_yu_2022_b]: https://doi.org/10.1016/j.energy.2021.121769
[research_wang_yuan_2026]: https://doi.org/10.3390/aerospace13030252
[research_wang_zhang_2016]: https://doi.org/10.1016/j.applthermaleng.2015.09.064
[research_wang_zhang_2018]: https://doi.org/10.2514/1.g003540
[research_wang_zhang_2021]: https://doi.org/10.2514/1.a34728
[research_wang_zhang_2022]: https://doi.org/10.1061/(asce)as.1943-5525.0001374
[research_wang_zhang_2022_c]: https://doi.org/10.2139/ssrn.4201874
[research_wang_zhang_2026]: https://doi.org/10.1016/j.ast.2026.111678
[research_wang_zhao_2022]: https://doi.org/10.1016/j.ast.2022.107883
[research_wang_zhou_1995]: https://doi.org/10.1016/0008-6223(94)00167-x
[research_wang_zou_2024]: https://doi.org/10.1016/j.cja.2024.03.042
[research_wangxiaoyen_harpstergeorge_2007]: https://ntrs.nasa.gov/citations/20070010027
[research_ward_hewitt_1988]: https://doi.org/10.2514/6.1988-3069
[research_ward_smart_2021]: https://doi.org/10.2514/1.a34983
[research_wartemann_ponchiocamillo_2019]: https://doi.org/10.1007/s12567-019-00249-9
[research_wasserbauerjf_meleasonet_1996]: https://ntrs.nasa.gov/citations/19960026650
[research_watanabe_1992]: https://doi.org/10.2514/6.1992-3289
[research_watanabe_1993]: https://doi.org/10.2514/3.23654
[research_watanabe_ishimoto_1996]: https://doi.org/10.2514/6.1996-4527
[research_watanabe_ishimoto_1997]: https://doi.org/10.2514/2.3259
[research_watkinswilliamb_1990]: https://ntrs.nasa.gov/citations/20080029274
[research_watt_aronson_1964]: https://doi.org/10.21236/ad0447153
[research_webb_samimy_2016]: https://doi.org/10.2514/6.2016-3173
[research_webber_reeves_2026]: https://doi.org/10.1063/5.0325241
[research_wei_jiao_2024]: https://doi.org/10.1016/j.energy.2024.131679
[research_wei_liu_2018]: https://doi.org/10.1155/2018/8793908
[research_wei_shi_2024]: https://doi.org/10.1016/j.applthermaleng.2024.123709
[research_wei_tian_2015]: https://doi.org/10.17706/ijapm.2015.5.2.144-152
[research_wei_tsungming_1994]: https://doi.org/10.1016/0008-6223(94)90079-5
[research_wei_xue_2017]: https://doi.org/10.1016/j.actaastro.2017.08.013
[research_wei_zhang_2023]: https://doi.org/10.1016/j.ast.2023.108683
[research_wei_zhang_2024]: https://doi.org/10.1016/j.cja.2024.04.023
[research_weidnerjohnp_1992]: https://ntrs.nasa.gov/citations/19920012279
[research_weidnerjohnp_1996]: https://ntrs.nasa.gov/citations/19960021079
[research_weidnerjp_1979]: https://ntrs.nasa.gov/citations/19790023044
[research_weidnerjp_smallwj_1976]: https://ntrs.nasa.gov/citations/19760055284
[research_weilmuenster_gnoffo_1992]: https://ntrs.nasa.gov/citations/19920065269
[research_weilmuenster_gnoffo_1996]: https://doi.org/10.2514/3.26786
[research_weilmuenster_gnoffo_1997]: https://doi.org/10.2514/2.3282
[research_weissman_1990]: https://doi.org/10.2514/6.1990-527
[research_wen_2023]: https://doi.org/10.54254/2753-8818/5/20230341
[research_wen_chen_2011]: https://doi.org/10.2514/6.2011-2382
[research_wendtm_nettletonm_1993]: https://ntrs.nasa.gov/citations/19930013628
[research_werner_smarsly_2014]: https://doi.org/10.1002/9781118998489.ch17
[research_west_bynum_2021]: https://doi.org/10.2514/6.2021-4139
[research_west_bynum_2024]: https://doi.org/10.2514/1.b39108
[research_west_hosder_2015]: https://doi.org/10.2514/1.a32947
[research_west_mitchell_1994]: https://doi.org/10.4271/941196
[research_whalen_hardy_1992]: https://ntrs.nasa.gov/citations/19920016888
[research_whalen_hardy_1993]: https://ntrs.nasa.gov/citations/19930000740
[research_whitcomb_2010]: https://doi.org/10.21236/ada547461
[research_white_1993]: https://doi.org/10.2514/6.1993-971
[research_white_2004]: https://doi.org/10.21236/ada430835
[research_white_ault_1996]: https://doi.org/10.2514/3.24157
[research_white_rhie_1992]: https://doi.org/10.2514/3.23471
[research_white_sreenivasan_1998]: https://doi.org/10.1016/s0375-9601(97)00765-2
[research_whitehead_1996]: https://doi.org/10.2514/6.1996-3108
[research_whitehead_2007]: https://doi.org/10.2514/6.2007-5837
[research_whiteheadallenhjr_1989]: https://ntrs.nasa.gov/citations/19890063967
[research_whitehurstrb_kraussrh_1992]: https://ntrs.nasa.gov/citations/19920066359
[research_whitfield_potter_1959]: https://doi.org/10.2514/8.7992
[research_whitside_2021]: https://doi.org/10.14264/1e68f80
[research_wierzbanowski_mccorry_1990]: https://ntrs.nasa.gov/citations/19920033435
[research_wierzbanowskitheodore_armstrongjohnnyg_1991]: https://ntrs.nasa.gov/citations/19930052226
[research_wierzbanowskitheodore_kastenterryd_1990]: https://ntrs.nasa.gov/citations/19910038265
[research_wieting_1990]: https://ntrs.nasa.gov/citations/19910029841
[research_wieting_guy_1976]: https://doi.org/10.2514/3.58649
[research_wietingar_guyrw_1975]: https://ntrs.nasa.gov/citations/19750034263
[research_wiezorek_mills_1998]: https://doi.org/10.21236/ada351754
[research_wilder_jr_1949]: https://doi.org/10.21236/ada952917
[research_wilfredhdukes_1962]: https://ntrs.nasa.gov/citations/19620004480
[research_wilhite_1983]: https://doi.org/10.2514/3.28366
[research_wilhite_1991]: https://ntrs.nasa.gov/citations/19910069462
[research_wilhite_bush_1991]: https://doi.org/10.2514/3.26294
[research_wilkinson_ruggleswrenn_2016]: https://doi.org/10.1016/j.polymertesting.2016.07.010
[research_willaime_belin_1998]: https://doi.org/10.1016/s0997-7546(98)80006-x
[research_willbanks_1970]: https://doi.org/10.2514/3.5614
[research_williams_lei_1996]: https://ntrs.nasa.gov/citations/19970022593
[research_williams_lewis_1975]: https://doi.org/10.21236/ada012877
[research_williams_mall_2017]: https://doi.org/10.2514/6.2017-1384
[research_williamsobers_agwu_2025]: https://doi.org/10.1089/3dp.2023.0168
[research_williamson_1992]: https://doi.org/10.2514/6.1992-3989
[research_williamsullivan_1991]: https://ntrs.nasa.gov/citations/19920035196
[research_wilson_1992]: https://ntrs.nasa.gov/citations/19930038369
[research_wilsonchan_razzaqi_2014]: https://doi.org/10.2514/6.2014-2931
[research_winkler_1952]: https://doi.org/10.21236/ad0001030
[research_winkler_bush_1992]: https://ntrs.nasa.gov/citations/19930004490
[research_wisbey_kearns_1994]: https://doi.org/10.1016/0167-577x(94)90120-1
[research_wisbey_wardclose_1997]: https://doi.org/10.1179/026708397790302313
[research_wittliff_oconnor_1992]: https://doi.org/10.2514/6.1992-3906
[research_wittliff_wilson_1961]: https://doi.org/10.21236/ad0258436
[research_wittliff_wilson_1961_b]: https://doi.org/10.21236/ad0266413
[research_wlmberly_mcginnis_1970]: https://doi.org/10.2514/3.5827
[research_wolf_daum_1993]: https://doi.org/10.2514/6.1993-5100
[research_wolf_mullen_1951]: https://doi.org/10.21236/ad0036130
[research_wolfle_1969]: https://doi.org/10.1126/science.165.3897.969
[research_won_jeung_2006]: https://doi.org/10.2514/6.2006-8039
[research_won_jeung_2007]: https://doi.org/10.2514/6.2007-5427
[research_wood_1968]: https://doi.org/10.1017/s0001925900004704
[research_woodcock_1988]: https://doi.org/10.1126/science.518-c
[research_woodruff_lorenz_1966]: https://doi.org/10.2514/3.3589
[research_woods_arrington_1983]: https://ntrs.nasa.gov/citations/19840002062
[research_woods_holland_2000]: https://ntrs.nasa.gov/citations/20000081743
[research_wortman_1970]: https://doi.org/10.2514/6.1970-809
[research_wright_1996]: https://doi.org/10.1520/stp18237s
[research_wright_achary_2003]: https://ntrs.nasa.gov/citations/20030066328
[research_wrightgeorgefjr_1993]: https://ntrs.nasa.gov/citations/19930012927
[research_wrighthowardt_1989]: https://ntrs.nasa.gov/citations/19890063957
[research_wu_1992]: https://doi.org/10.1007/bf00729908
[research_wu_2026]: https://doi.org/10.2514/6.2026-114962
[research_wu_deng_2021]: https://doi.org/10.1016/j.ast.2021.107046
[research_wu_gao_2026]: https://doi.org/10.1063/5.0341670
[research_wu_he_2025]: https://doi.org/10.1016/j.applthermaleng.2024.125054
[research_wu_jiang_2015]: https://doi.org/10.1051/matecconf/20153102004
[research_wu_liang_2019]: https://doi.org/10.1103/physrevfluids.4.044602
[research_wu_lin_2020]: https://doi.org/10.1016/j.ceramint.2020.02.241
[research_wu_song_2021]: https://doi.org/10.1016/j.actaastro.2021.04.015
[research_wu_wang_2016]: https://doi.org/10.1016/j.actaastro.2016.06.021
[research_wu_wei_2022]: https://doi.org/10.3390/app13010480
[research_wu_yang_2015]: https://doi.org/10.1007/s11630-015-0794-y
[research_wu_yuan_2025]: https://doi.org/10.3934/jimo.2025010
[research_wu_zhang_2023]: https://doi.org/10.54254/2755-2721/11/20230209
[research_wu_zhao_2026]: https://doi.org/10.2514/1.j066934
[research_wursterkathryne_rileychristopherj_1998]: https://ntrs.nasa.gov/citations/19980025468
[research_wursterke_stonehw_1993]: https://ntrs.nasa.gov/citations/19930069742
[research_x_43a_research_2011]: https://doi.org/10.2514/5.9781600867774.0199.0219
[research_xia_chen_2020]: https://doi.org/10.1016/j.neucom.2019.10.038
[research_xia_han_2026]: https://doi.org/10.1063/5.0332049
[research_xia_li_2023]: https://doi.org/10.1016/j.ijhydene.2023.05.241
[research_xia_li_2023_b]: https://doi.org/10.1016/j.ijhydene.2023.01.046
[research_xiang_yang_2020]: https://doi.org/10.1080/19942060.2020.1842248
[research_xianhong_yuan_2015]: https://doi.org/10.1016/j.proeng.2014.12.516
[research_xiao_edwards_2004]: https://ntrs.nasa.gov/citations/20040111370
[research_xiao_liu_2006]: https://doi.org/10.2514/6.2006-8090
[research_xiao_lu_2024]: https://doi.org/10.1016/j.csite.2024.105426
[research_xiao_wu_2025]: https://doi.org/10.1063/5.0251986
[research_xiao_yue_2008]: https://doi.org/10.2514/6.2008-2634
[research_xiao_yue_2012]: https://doi.org/10.2514/6.2012-5978
[research_xiaoqing_zhongxi_2010]: https://doi.org/10.2514/6.2010-7931
[research_xiaoxuan_jinglong_2018]: https://doi.org/10.1177/0954410018808634
[research_xie_dong_2020]: https://doi.org/10.1016/j.ast.2020.106170
[research_xie_liu_2025]: https://doi.org/10.1016/j.applthermaleng.2025.127458
[research_xie_xia_2025]: https://doi.org/10.1016/j.ast.2025.110228
[research_xie_zhao_2026]: https://doi.org/10.1016/j.ast.2026.112895
[research_xinchun_zhongwei_2021]: https://doi.org/10.35840/2631-5009/7553
[research_xinchunli_zhongweiwang_2020]: https://doi.org/10.30574/ijsra.2020.1.2.0032
[research_xing_cai_2017]: https://doi.org/10.2514/6.2017-2121
[research_xing_ruan_2017]: https://doi.org/10.1016/j.ast.2016.11.007
[research_xing_xiao_2016]: https://doi.org/10.1061/(asce)as.1943-5525.0000624
[research_xing_zhang_2012]: https://doi.org/10.2514/6.2012-945
[research_xinghao_haijie_2021]: https://doi.org/10.1088/1742-6596/1786/1/012051
[research_xiong_bai_2019]: https://doi.org/10.1007/978-3-319-91017-8_133
[research_xiong_fan_2019]: https://doi.org/10.1016/j.actaastro.2019.07.004
[research_xiong_qin_2020]: https://doi.org/10.1016/j.energy.2020.117477
[research_xiong_qin_2022]: https://doi.org/10.1155/2022/9931498
[research_xu_cheng_2018]: https://doi.org/10.1111/jace.15565
[research_xu_fang_2022]: https://doi.org/10.1145/3547578.3547593
[research_xu_guo_2025]: https://doi.org/10.3390/act14110565
[research_xu_han_2025]: https://doi.org/10.3390/aerospace12010068
[research_xu_he_2008]: https://doi.org/10.1016/j.jcp.2008.03.035
[research_xu_he_2024]: https://doi.org/10.1016/j.addma.2024.103981
[research_xu_leng_2025]: https://doi.org/10.1016/j.energy.2025.137846
[research_xu_liao_2025]: https://doi.org/10.1002/rnc.7804
[research_xu_lin_2021]: https://doi.org/10.1016/j.applthermaleng.2021.117616
[research_xu_lin_2024]: https://doi.org/10.3390/app14062508
[research_xu_liu_2020]: https://doi.org/10.1063/5.0001914
[research_xu_wang_2022]: https://doi.org/10.1631/jzus.a2200155
[research_xu_wu_2018]: https://doi.org/10.12783/dtetr/pmsms2018/24889
[research_xu_xu_2019]: https://doi.org/10.1088/1757-899x/531/1/012059
[research_xu_yu_2025]: https://doi.org/10.1063/5.0256333
[research_xu_zhu_2026]: https://doi.org/10.1016/j.cja.2025.103631
[research_xue_he_2025]: https://doi.org/10.1016/j.ast.2025.110705
[research_xue_li_2026]: https://doi.org/10.1016/j.applthermaleng.2026.130619
[research_yamada_fujii_1999]: https://doi.org/10.4028/www.scientific.net/msf.308-311.902
[research_yamaguchi_hizawa_2020]: https://doi.org/10.2322/tjsass.63.160
[research_yamanaka_1989]: https://doi.org/10.2514/6.1989-5008
[research_yamanaka_1992]: https://doi.org/10.2514/6.1992-5005
[research_yan_fan_2022]: https://doi.org/10.3390/aerospace10010002
[research_yan_he_2018]: https://doi.org/10.1016/j.actaastro.2018.04.038
[research_yan_he_2018_b]: https://doi.org/10.1016/j.actaastro.2018.04.051
[research_yan_le_2026]: https://doi.org/10.1016/j.applthermaleng.2026.132218
[research_yan_liu_2022]: https://doi.org/10.1016/j.ast.2022.107637
[research_yan_liu_2022_b]: https://doi.org/10.1016/j.ast.2022.107617
[research_yan_shaohua_2016]: https://doi.org/10.1016/j.actaastro.2016.07.025
[research_yan_teng_2021]: https://doi.org/10.1016/j.actaastro.2021.02.010
[research_yan_tian_2025]: https://doi.org/10.1016/j.combustflame.2025.114485
[research_yan_wang_2022]: https://doi.org/10.3390/aerospace9120773
[research_yan_wang_2023]: https://doi.org/10.1051/jnwpu/20234161064
[research_yan_wang_2026]: https://doi.org/10.1016/j.ast.2026.113181
[research_yan_yang_2025]: https://doi.org/10.2478/amns-2025-0394
[research_yang_2026]: https://ntrs.nasa.gov/citations/20260000294
[research_yang_bao_2017]: https://doi.org/10.1016/j.cja.2017.02.013
[research_yang_chang_2014]: https://doi.org/10.1016/j.energy.2014.08.052
[research_yang_chang_2015]: https://doi.org/10.2514/1.t4379
[research_yang_che_2024]: https://doi.org/10.1016/j.ijhydene.2024.06.329
[research_yang_choi_2024]: https://doi.org/10.1371/journal.pone.0298113
[research_yang_choi_2024_b]: https://doi.org/10.1007/s12206-024-0224-8
[research_yang_culick_1986]: https://doi.org/10.1080/00102208608923839
[research_yang_duan_2014]: https://doi.org/10.2514/6.2014-1393
[research_yang_gao_2026]: https://doi.org/10.1017/jfm.2025.11062
[research_yang_gui_2018]: https://doi.org/10.1016/j.actaastro.2018.03.055
[research_yang_gui_2020]: https://doi.org/10.1016/j.ijheatmasstransfer.2019.118869
[research_yang_hayat_2026]: https://doi.org/10.1177/00219983261456074
[research_yang_kubota_1993]: https://doi.org/10.2514/3.11696
[research_yang_lee_2020]: https://doi.org/10.6108/kspe.2020.24.5.013
[research_yang_li_2019]: https://doi.org/10.1016/j.jeurceramsoc.2018.09.007
[research_yang_li_2021]: https://doi.org/10.1061/(asce)as.1943-5525.0001306
[research_yang_li_2026]: https://doi.org/10.3390/ma19153296
[research_yang_liu_2017]: https://doi.org/10.1016/j.actaastro.2016.11.043
[research_yang_qiu_2024]: https://doi.org/10.1063/5.0226284
[research_yang_shi_2015]: https://doi.org/10.1016/j.ijhydene.2015.01.033
[research_yang_song_2023]: https://doi.org/10.1063/5.0160146
[research_yang_sun_2011]: https://doi.org/10.4028/www.scientific.net/amr.383-390.7375
[research_yang_tian_2024]: https://doi.org/10.1063/5.0212881
[research_yang_wang_2022]: https://doi.org/10.3390/aerospace9040219
[research_yang_xia_2021]: https://doi.org/10.3390/en14175589
[research_yang_xie_2025]: https://doi.org/10.2139/ssrn.5148232
[research_yang_yang_2023]: https://doi.org/10.1063/5.0171301
[research_yang_yuhyihwu_1994]: https://doi.org/10.1016/s0082-0784(06)80806-4
[research_yankui_dongjun_2005]: https://doi.org/10.2514/6.2005-6040
[research_yao_2022]: https://doi.org/10.2514/1.b38617
[research_yao_gu_2023]: https://doi.org/10.1063/5.0145047
[research_yao_liu_2021]: https://doi.org/10.1016/j.ast.2021.106941
[research_yao_marck_1995]: https://doi.org/10.1016/0921-5093(95)03345-9
[research_yao_sun_2023]: https://doi.org/10.1016/j.ast.2023.108308
[research_yao_tang_2017]: https://doi.org/10.1515/tjj-2015-0052
[research_yao_wu_2025]: https://doi.org/10.1049/icp.2025.3470
[research_yao_xia_2023]: https://doi.org/10.3390/aerospace10090795
[research_yao_xia_2024]: https://doi.org/10.3390/aerospace11080680
[research_yaros_1991]: https://doi.org/10.2514/6.1991-2154
[research_yasunaga_nakaya_2024]: https://doi.org/10.1016/j.proci.2024.105302
[research_yates_1967]: https://doi.org/10.1007/978-1-4757-0489-1_14
[research_yatsukhno_2018]: https://doi.org/10.1088/1742-6596/1009/1/012002
[research_ye_ye_2019]: https://doi.org/10.1016/j.actaastro.2019.04.028
[research_ye_ye_2019_b]: https://doi.org/10.1016/j.ast.2018.11.015
[research_yen_1963]: https://doi.org/10.2514/3.2026
[research_yentsch_gaitonde_2012]: https://doi.org/10.2514/6.2012-3772
[research_yentsch_gaitonde_2013]: https://doi.org/10.2514/6.2013-119
[research_yentsch_gaitonde_2013_b]: https://doi.org/10.2514/6.2013-3753
[research_yi_lou_2020]: https://doi.org/10.2478/tar-2020-0015
[research_yi_xie_2024]: https://doi.org/10.32604/icces.2024.012704
[research_yin_e_2022]: https://doi.org/10.1155/2022/3471421
[research_yin_he_2023]: https://doi.org/10.2139/ssrn.4574049
[research_yin_jiang_2023]: https://doi.org/10.3390/app132413302
[research_yin_li_2024]: https://doi.org/10.1007/s40430-024-05361-4
[research_yin_li_2026]: https://doi.org/10.1016/j.combustflame.2026.115044
[research_yip_strawa_1990]: https://doi.org/10.2514/6.1990-2339
[research_yokoo_goto_2020]: https://doi.org/10.2514/1.j058322
[research_yongsheng_2014]: https://doi.org/10.2514/6.2014-3666
[research_yoon_ahn_2016]: https://doi.org/10.1061/(asce)as.1943-5525.0000567
[research_yoshida_micci_2019]: https://doi.org/10.2514/1.a34341
[research_youn_mills_1995]: https://doi.org/10.2514/3.639
[research_yountbryanc_arnoldjameso_2012]: https://ntrs.nasa.gov/citations/20120018068
[research_yu_2015]: https://doi.org/10.1360/sspma2015-00260
[research_yu_2024]: https://doi.org/10.1063/5.0209635
[research_yu_chen_2020]: https://doi.org/10.1016/j.actaastro.2019.10.024
[research_yu_chen_2020_b]: https://doi.org/10.1016/j.ast.2020.105948
[research_yu_huang_2020]: https://doi.org/10.1016/j.actaastro.2019.09.015
[research_yu_jones_2017]: https://doi.org/10.2514/1.t4921
[research_yu_kim_2005]: https://doi.org/10.21236/ada439707
[research_yu_li_2022]: https://doi.org/10.3390/app12062845
[research_yu_ni_2021]: https://doi.org/10.1155/2021/8885074
[research_yu_pan_2017]: https://doi.org/10.1016/j.energy.2017.06.158
[research_yu_wang_2019]: https://doi.org/10.1016/j.energy.2019.07.102
[research_yu_wang_2019_b]: https://doi.org/10.1016/j.energy.2018.12.192
[research_yu_wang_2019_c]: https://doi.org/10.1016/j.enconman.2019.111827
[research_yu_wang_2020]: https://doi.org/10.1016/j.enconman.2020.112548
[research_yu_wang_2025]: https://doi.org/10.1007/s12567-025-00672-1
[research_yu_wang_2026]: https://doi.org/10.1016/j.ast.2026.112132
[research_yu_yang_2025]: https://doi.org/10.1177/01423312241300745
[research_yu_yu_2019]: https://doi.org/10.1016/j.enconman.2019.06.049
[research_yu_yuan_2016]: https://doi.org/10.1016/j.taml.2016.02.003
[research_yu_zhou_2022]: https://doi.org/10.1016/j.actaastro.2022.02.025
[research_yuan_liu_2026]: https://doi.org/10.1063/5.0338458
[research_yue_nie_2018]: https://doi.org/10.1061/(asce)as.1943-5525.0000825
[research_yue_titurus_2022]: https://doi.org/10.1007/s11071-022-07944-z
[research_yue_wu_2016]: https://doi.org/10.1016/j.fuproc.2016.04.017
[research_yue_xiao_2009]: https://doi.org/10.2514/6.2009-7422
[research_yun_kim_2026]: https://doi.org/10.1016/j.ast.2026.111990
[research_yungster_1992]: https://ntrs.nasa.gov/citations/19920016573
[research_yungstershaye_paxsondaniele_2015]: https://ntrs.nasa.gov/citations/20150022172
[research_yushchenkova_pomerantsev_1967]: https://doi.org/10.1016/0017-9310(67)90179-2
[research_yushengtao_hsiehkwangchung_1988]: https://ntrs.nasa.gov/citations/19880040490
[research_zagainov_plokhikh_1991]: https://doi.org/10.2514/6.1991-5103
[research_zaldivar_rellick_1998]: https://doi.org/10.21236/ada349058
[research_zaludin_2025]: https://doi.org/10.70112/arme-2025.14.1.4286
[research_zan_li_2018]: https://doi.org/10.1016/j.actaastro.2018.03.015
[research_zander_vinkeloe_2021]: https://doi.org/10.1002/kin.21469
[research_zangiev_ivanov_2016]: https://doi.org/10.1134/s1990793116020135
[research_zarlingo_1988]: https://doi.org/10.2514/6.1988-3070
[research_zeng_wang_2026]: https://doi.org/10.1016/j.ast.2026.113306
[research_zhai_yang_2020]: https://doi.org/10.1016/j.jfranklin.2020.03.002
[research_zhang_2015]: https://doi.org/10.2514/6.2015-3647
[research_zhang_2020]: https://doi.org/10.1063/5.0036004
[research_zhang_2020_b]: https://doi.org/10.1007/978-981-15-0727-4_9
[research_zhang_2020_c]: https://doi.org/10.1007/978-981-15-0727-4_8
[research_zhang_2020_d]: https://doi.org/10.1007/978-981-15-0727-4_7
[research_zhang_cao_2019]: https://doi.org/10.1016/j.ijhydene.2019.09.063
[research_zhang_chang_2017]: https://doi.org/10.1016/j.actaastro.2017.01.031
[research_zhang_chang_2018]: https://doi.org/10.1016/j.ast.2018.02.027
[research_zhang_chen_2014]: https://doi.org/10.2514/6.2014-3686
[research_zhang_chen_2015]: https://doi.org/10.1016/j.cja.2015.06.015
[research_zhang_chen_2018]: https://doi.org/10.1016/j.isatra.2018.08.012
[research_zhang_chen_2023]: https://doi.org/10.1063/5.0137819
[research_zhang_chen_2023_b]: https://doi.org/10.1016/j.energy.2022.126110
[research_zhang_ding_2023]: https://doi.org/10.1177/00202940231154856
[research_zhang_feng_2016]: https://doi.org/10.1016/j.ijhydene.2016.03.176
[research_zhang_feng_2016_b]: https://doi.org/10.2514/1.b35887
[research_zhang_feng_2023]: https://doi.org/10.1016/j.jppr.2023.02.006
[research_zhang_han_2025]: https://doi.org/10.1002/asjc.3839
[research_zhang_hong_2015]: https://doi.org/10.4028/www.scientific.net/amm.730.311
[research_zhang_li_2016]: https://doi.org/10.1016/j.actaastro.2016.09.028
[research_zhang_li_2020]: https://doi.org/10.1063/5.0011299
[research_zhang_li_2023]: https://doi.org/10.1049/icp.2022.2954
[research_zhang_li_2026]: https://doi.org/10.1088/1742-6596/3256/1/012066
[research_zhang_liang_2025]: https://doi.org/10.1038/s41598-025-88987-1
[research_zhang_liao_2026]: https://doi.org/10.1016/j.ast.2026.111885
[research_zhang_lin_2023]: https://doi.org/10.1016/j.actaastro.2022.10.008
[research_zhang_liu_2018]: https://doi.org/10.1016/j.actaastro.2018.05.017
[research_zhang_liu_2018_b]: https://doi.org/10.1016/j.actaastro.2018.10.004
[research_zhang_nie_2024]: https://doi.org/10.1016/j.cja.2023.09.007
[research_zhang_niu_2019]: https://doi.org/10.1080/09276440.2019.1701321
[research_zhang_pan_2025]: https://doi.org/10.2514/1.j064706
[research_zhang_qiao_2020]: https://doi.org/10.1016/j.applthermaleng.2020.115661
[research_zhang_shi_2024]: https://doi.org/10.1016/j.jeurceramsoc.2023.11.007
[research_zhang_su_2025]: https://doi.org/10.2514/1.a36194
[research_zhang_sun_2022]: https://doi.org/10.3390/app12125996
[research_zhang_tong_2021]: https://doi.org/10.1063/5.0064741
[research_zhang_wang_2017]: https://doi.org/10.1016/j.actaastro.2017.06.011
[research_zhang_wang_2018]: https://doi.org/10.1007/s00521-018-3764-y
[research_zhang_wang_2020]: https://doi.org/10.1016/j.energy.2019.116709
[research_zhang_wang_2020_b]: https://doi.org/10.1016/j.ast.2020.106145
[research_zhang_wang_2022]: https://doi.org/10.1016/j.jeurceramsoc.2022.02.021
[research_zhang_wei_2019]: https://doi.org/10.1016/j.actaastro.2019.03.078
[research_zhang_wu_2024]: https://doi.org/10.1360/sspma-2024-0182
[research_zhang_xian_2015]: https://doi.org/10.1007/s11071-015-2373-x
[research_zhang_xie_2025]: https://doi.org/10.1016/j.icheatmasstransfer.2025.109733
[research_zhang_xu_2016]: https://doi.org/10.1016/j.actaastro.2016.09.021
[research_zhang_yang_2015]: https://doi.org/10.1016/j.energy.2015.08.017
[research_zhang_yao_2023]: https://doi.org/10.1016/j.fuel.2023.128502
[research_zhang_yi_2023]: https://doi.org/10.1016/j.expthermflusci.2022.110786
[research_zhang_yu_2024]: https://doi.org/10.1016/j.renene.2024.120541
[research_zhang_yue_2019]: https://doi.org/10.1016/j.ast.2019.105420
[research_zhang_zhang_2017]: https://doi.org/10.1177/0954410017703148
[research_zhang_zhang_2022]: https://doi.org/10.1186/s42774-022-00123-z
[research_zhang_zhang_2023]: https://doi.org/10.1016/j.actaastro.2023.03.031
[research_zhang_zhang_2025]: https://doi.org/10.3390/aerospace12040308
[research_zhang_zhou_2026]: https://doi.org/10.2139/ssrn.7193352
[research_zhao_bai_2026]: https://doi.org/10.1016/j.energy.2026.141972
[research_zhao_bradt_1985]: https://doi.org/10.1016/0008-6223(85)90189-7
[research_zhao_chen_2026]: https://doi.org/10.1016/j.combustflame.2025.114588
[research_zhao_dong_2019]: https://doi.org/10.1063/1.5086912
[research_zhao_fan_2023]: https://doi.org/10.1016/j.applthermaleng.2022.119582
[research_zhao_gao_2023]: https://doi.org/10.1088/1742-6596/2633/1/012011
[research_zhao_he_2021]: https://doi.org/10.1016/j.actaastro.2021.02.036
[research_zhao_li_2020]: https://doi.org/10.1155/2020/4313758
[research_zhao_liu_2019]: https://doi.org/10.1063/1.5125116
[research_zhao_liu_2020]: https://doi.org/10.1016/j.ast.2019.105553
[research_zhao_ma_2025]: https://doi.org/10.1016/j.ast.2025.110031
[research_zhao_shao_2022]: https://doi.org/10.3390/aerospace9120742
[research_zhao_sun_2022]: https://doi.org/10.1155/2022/7169123
[research_zhao_tian_2023]: https://doi.org/10.1016/j.ast.2023.108529
[research_zhao_wu_2025]: https://doi.org/10.1063/5.0245154
[research_zhao_wu_2025_b]: https://doi.org/10.1063/5.0285061
[research_zhao_xia_2022]: https://doi.org/10.1088/1742-6596/2364/1/012066
[research_zhao_zhang_2023]: https://doi.org/10.1016/j.applthermaleng.2023.120987
[research_zheng_bray_1994]: https://doi.org/10.1016/0010-2180(94)90151-1
[research_zheng_chang_2018]: https://doi.org/10.1016/j.actaastro.2018.10.009
[research_zheng_chang_2019]: https://doi.org/10.1016/j.ast.2019.105462
[research_zheng_chang_2020]: https://doi.org/10.1016/j.ast.2020.105773
[research_zheng_chang_2021]: https://doi.org/10.1016/j.ast.2020.106423
[research_zheng_huang_2025]: https://doi.org/10.1016/j.tsep.2025.104408
[research_zheng_jiang_2022]: https://doi.org/10.32604/fdmp.2022.019048
[research_zheng_wang_2018]: https://doi.org/10.2514/1.b36591
[research_zheng_wu_2023]: https://doi.org/10.1049/icp.2022.3035
[research_zheng_xiong_2021]: https://doi.org/10.1002/er.6856
[research_zheng_yan_2020]: https://doi.org/10.1016/j.actaastro.2019.12.020
[research_zhi_ran_2015]: https://doi.org/10.1016/j.proeng.2014.12.633
[research_zhikharev_1993]: https://doi.org/10.1007/bf00417928
[research_zhivotov_1996]: https://doi.org/10.1007/bf02230761
[research_zhluktov_tirskii_1990]: https://doi.org/10.1007/bf01049829
[research_zhong_1998]: https://doi.org/10.1006/jcph.1998.6010
[research_zhong_2007]: https://doi.org/10.21236/ada467163
[research_zhong_2009]: https://doi.org/10.21236/ada517055
[research_zhong_peng_2018]: https://doi.org/10.1080/00102202.2018.1559838
[research_zhong_peng_2019]: https://doi.org/10.2514/1.b37421
[research_zhong_qu_2025]: https://doi.org/10.1063/5.0255571
[research_zhong_xu_2025]: https://doi.org/10.1016/j.combustflame.2024.113864
[research_zhou_2023]: https://doi.org/10.4273/ijvss.15.2.22
[research_zhou_cao_2025]: https://doi.org/10.1016/j.measurement.2025.118169
[research_zhou_du_2022]: https://doi.org/10.3390/e24101325
[research_zhou_fu_2024]: https://doi.org/10.1360/ssi-2023-0322
[research_zhou_jiang_2017]: https://doi.org/10.1007/978-3-319-44866-4_66
[research_zhou_li_2017]: https://doi.org/10.1016/j.ijheatmasstransfer.2017.08.013
[research_zhou_li_2023]: https://doi.org/10.1063/5.0136170
[research_zhou_lu_2017]: https://doi.org/10.2514/6.2017-2343
[research_zhou_tan_2023]: https://doi.org/10.21595/vp.2023.23198
[research_zhou_tian_2025]: https://doi.org/10.1016/j.applthermaleng.2025.127851
[research_zhou_xia_2023]: https://doi.org/10.1016/j.actaastro.2023.05.036
[research_zhou_xu_2022]: https://doi.org/10.3390/app12147127
[research_zhou_yan_2015]: https://doi.org/10.4028/www.scientific.net/amm.798.627
[research_zhou_yan_2016]: https://doi.org/10.1016/j.ijheatmasstransfer.2015.11.048
[research_zhou_zhang_2024]: https://doi.org/10.1016/j.energy.2024.133502
[research_zhou_zhang_2025]: https://doi.org/10.1016/j.energy.2025.138569
[research_zhou_zhao_2016]: https://doi.org/10.1016/j.actaastro.2016.05.027
[research_zhou_zhao_2018]: https://doi.org/10.1016/j.ast.2017.12.002
[research_zhu_2019]: https://doi.org/10.1007/s10483-019-2430-9
[research_zhu_2022]: https://doi.org/10.1186/s42774-022-00117-x
[research_zhu_chen_2018]: https://doi.org/10.1063/1.5005529
[research_zhu_ohtani_1999]: https://doi.org/10.1016/s0008-6223(99)00003-2
[research_zhu_peng_2018]: https://doi.org/10.1016/j.cja.2018.06.011
[research_zhu_shi_2021]: https://doi.org/10.1063/5.0033779
[research_zhu_xu_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000740
[research_zhu_xu_2017_b]: https://doi.org/10.2514/1.j054974
[research_zhu_zhang_2025]: https://doi.org/10.1016/j.ast.2025.110081
[research_zhu_zhao_2016]: https://doi.org/10.1016/j.actaastro.2016.01.028
[research_zimont_muhin_2009]: https://doi.org/10.2514/6.2009-7283
[research_zoby_thompson_1990]: https://doi.org/10.2514/3.26151
[research_zong_bao_2015]: https://doi.org/10.1061/(asce)as.1943-5525.0000374
[research_zong_wang_2015]: https://doi.org/10.1061/(asce)as.1943-5525.0000438
[research_zou_li_2016]: https://doi.org/10.1016/j.matdes.2015.12.048
[research_zou_liu_2026]: https://doi.org/10.1016/j.energy.2026.139991
[research_zou_wang_2022]: https://doi.org/10.1080/08916152.2022.2086323
[research_zou_wang_2022_b]: https://doi.org/10.1016/j.enconman.2022.115472
[research_zubin_ostapenko_1997]: https://doi.org/10.1007/bf03374538
[research_zukoski_auerbach_1976]: https://doi.org/10.1115/1.3446114
[research_zuo_2023]: https://doi.org/10.2514/1.j062521
[research_zuo_2023_b]: https://doi.org/10.2514/1.j062953
[research_zuo_hu_2021]: https://doi.org/10.1016/j.actaastro.2021.01.058
[research_zuo_huang_2015]: https://doi.org/10.2514/6.2015-3748
[research_zuo_molder_2019]: https://doi.org/10.1016/j.paerosci.2019.03.001
[research_zuo_zhang_2018]: https://doi.org/10.1016/j.actaastro.2018.04.037
[research_zvegintsev_1993]: https://doi.org/10.2514/6.1993-2446
