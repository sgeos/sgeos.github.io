---
layout: post
mathjax: true
comments: true
title: "X-Planes: X-41 Common Aero Vehicle"
date: 2025-11-16 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 42
---
<!-- A338 -->
<script>console.log("A338");</script>

**No specifications for this vehicle have ever been released, and it is not certain that the designation in
the title belongs to it.** What is public is a mission requirement, and a mission requirement is a physics
problem. This article derives what the vehicle had to be from what it had to do, and then checks the
derivation against the one thing that did fly.
This is the forty-second article in the [X-Planes series][related_post_a297_framing], following the [X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], the [X-4][related_post_a301_northrop_x4], the [X-5][related_post_a302_bell_x5], the [X-6][related_post_a303_convair_x6], the [X-7][related_post_a304_lockheed_x7], the [X-8][related_post_a305_aerojet_x8], the [X-9][related_post_a306_bell_x9], the [X-10][related_post_a307_north_american_x10], the [X-11][related_post_a308_convair_x11], the [X-12][related_post_a309_convair_x12], the [X-13][related_post_a310_ryan_x13], the [X-14][related_post_a311_bell_x14], the [X-15][related_post_a312_north_american_x15], the [X-16][related_post_a313_bell_x16], the [X-17][related_post_a314_lockheed_x17], the [X-18][related_post_a315_hiller_x18], the [X-19][related_post_a316_curtiss_wright_x19], the [X-20][related_post_a317_boeing_x20], the [X-21][related_post_a318_northrop_x21], the [X-22][related_post_a319_bell_x22], the [X-23][related_post_a320_martin_marietta_x23], the [X-24][related_post_a321_martin_marietta_x24], the [X-25][related_post_a322_bensen_x25], the [X-26][related_post_a323_schweizer_x26], the [X-27][related_post_a324_lockheed_x27], the [X-28][related_post_a325_osprey_x28], the [X-29][related_post_a326_grumman_x29], the [X-30][related_post_a327_rockwell_x30], the [X-31][related_post_a328_rockwell_mbb_x31], the [X-32][related_post_a329_boeing_x32], the [X-33][related_post_a330_lockheed_martin_x33], the [X-34][related_post_a331_orbital_sciences_x34], the [X-35][related_post_a332_lockheed_martin_x35], the [X-36][related_post_a333_mcdonnell_douglas_x36], the [X-37][related_post_a334_boeing_x37], the [X-38][related_post_a335_scaled_composites_x38], the [X-39][related_post_a336_x39_reserved_never_assigned], and the [X-40][related_post_a337_boeing_x40].

**This is the first article in the series to take the documentation-poor class**, which the genre reserves
for a vehicle whose record will not support the full treatment. The section order is the same as for a
documented aircraft and the sections are shorter, **with the statement of what is unknown carrying weight
that a specification table would otherwise carry.**

**The finding is that classification hides the design and not the physics.** A published range, a published
mass and a published lift to drag ratio bound the problem tightly enough to show where it becomes
impossible, and **the place it becomes impossible is the leading edge.** When the vehicle finally flew,
twice, it failed at the leading edge both times, and the official failure report says so.

## The Research Question

**The binding unknown was whether a body could glide most of the way around the world and still be
pointed at something when it arrived.**

The Common Aero Vehicle was defined as a manoeuvrable hypersonic reentry vehicle able to dispense a
variety of payloads inside the atmosphere [[X-41 CAV][ref_x41_parsch]]. **The word Aero stood for
aeroshell rather than aerospace**, because the vehicle was conceived as a common thermal shell that
different payloads could sit inside [[X-41 CAV][ref_x41_parsch]]. That naming is the clearest statement of
the design intent available, and it says the shell was the product.

**The requirement that sets everything else is range.** The programme it belonged to sought to strike
targets **9,000 nautical miles from a launch site in the continental United States**
[[DARPA Falcon Project][ref_falcon]], carrying about **1,000 pounds** of payload
[[X-41 Common Aero Vehicle][ref_x41_wiki]].

**Those two numbers plus the laws of motion are enough to bound the design**, and the sizing section does
it. The chain runs from range to the required lift to drag ratio, from there to the speed the vehicle must
be boosted to, from there to the air density it must fly in to hold itself up, and from there to the
temperature of its leading edge. **The last number in that chain is the one that decides whether the
vehicle exists**, and it does not depend on anything classified.

## Programme Origin

**The vehicle began as an Air Force programme, was merged into a joint one, lost its weapon, and changed
its name.**

In December 2002 the Air Force's Common Aero Vehicle work was merged with a Defense Advanced Research
Projects Agency effort into a joint programme named **Force Application and Launch from the Continental
United States**, which carried two tasks, being a small launch vehicle and the aero vehicle itself
[[X-41 CAV][ref_x41_parsch]]. **The launch vehicle existed to make the glider cheap to use**, since an
intercontinental ballistic missile is an expensive way to deliver a thousand pounds.

**By 2004 the offensive strike element had been cancelled and the vehicle was renamed.** The Common Aero
Vehicle became the **Hypersonic Technology Vehicle**, and research on weaponisation ended
[[X-41 CAV][ref_x41_parsch]]. **Congress had restricted funding for the strike mission across several
years** [[DARPA Falcon Project][ref_falcon]] [[Prompt Global Strike][ref_pgs]], which is the proximate reason a vehicle designed to deliver
munitions across the Pacific became a vehicle designed to demonstrate that the glide was possible.

**The designation is the least certain thing in this section.** The X-41A was allocated in late 1997 or
early 1998, **years before the Common Aero Vehicle programme existed**, and the authoritative survey of
these designations records that it was never used again in any official announcement and that
**it is not clear the designation was ever actually applicable to the vehicle discussed here**
[[X-41 CAV][ref_x41_parsch]].

**The article immediately before last concerned a number reserved and never assigned.** This one concerns
a number that was assigned, went unused, and was later attached by the public record to a vehicle it may
have nothing to do with. **Both are failures of the same register**, and the
[X-39][related_post_a336_x39_reserved_never_assigned] article describes the mechanism.

## Sizing From First Principles

### The Range Requirement Fixes the Lift to Drag Ratio

**A hypersonic glider is held up by lift and by the curvature of its own path, and the second term is not
small.** Let $V$ be the vehicle's speed, $R_{e}$ the radius of the Earth and $g$ the acceleration due to
gravity. The speed at which a body would orbit at the surface is

$$V_{c} = \sqrt{g R_{e}} = \sqrt{(9.80665)(6.371 \times 10^{6})} = 7{,}904 \ \text{m/s}$$

**At a fraction of that speed the vehicle is partly in orbit already.** The lift a steady glide requires is
the weight less the centrifugal relief, which is the equilibrium glide condition.

$$L = W \left( 1 - \frac{V^{2}}{V_{c}^{2}} \right)$$

Integrating the resulting equation of motion over a glide that decelerates from an initial speed $V$ gives
the classical equilibrium glide range, in which the entire vehicle enters only through its lift to drag
ratio.

$$R = \left(\frac{L}{D}\right) \frac{R_{e}}{2} \ln \left( \frac{1}{1 - V^{2}/V_{c}^{2}} \right)$$

**That relation is the whole argument of this article.** It says that range is bought with two things only,
being the aerodynamic efficiency of the shape and the speed it is launched at, **and that neither can be
classified away.**

**Range is strictly linear in the ratio and strongly non-linear in speed**, which sets where the design
effort goes.

$$\frac{\partial R}{R} = \frac{\partial (L/D)}{L/D}$$

**A ten percent loss of aerodynamic efficiency is a ten percent loss of range**, so anything that blunts
the shape is paid for directly, and the sizing below ends by blunting the shape.

**Inverting it for the stated requirement gives the design space.** Solving the range relation for the
ratio gives the demand placed on the shape by a fixed distance.

$$\frac{L}{D} = \frac{R}{\dfrac{R_{e}}{2} \ln\left(\dfrac{1}{1 - V^{2}/V_{c}^{2}}\right)}$$

Entry speeds are quoted here as Mach numbers at 40 kilometres, where the speed of sound is about 295
metres per second, so the conversion is

$$V = M a \qquad a \approx 295 \ \text{m/s}$$

For a range of 9,000 nautical miles, being 16,668 kilometres, the required ratio at each entry speed is

| entry Mach at 40 km | $V$ (m/s) | $V/V_{c}$ | required $L/D$ |
|---|---|---|---|
| 15 | 4,425 | 0.560 | 13.92 |
| 20 | 5,900 | 0.746 | 6.42 |
| 22 | 6,490 | 0.821 | 4.67 |
| 24 | 7,080 | 0.896 | 3.23 |
| 26 | 7,670 | 0.970 | 1.84 |

### The Hypersonic Barrier Says Most of That Table Is Impossible

**There is an empirical ceiling on hypersonic aerodynamic efficiency and it is low.** The correlation
usually attributed to Küchemann bounds the attainable maximum for a hypersonic configuration as a function
of Mach number.

$$\left(\frac{L}{D}\right)_{\max} \approx \frac{4(M + 3)}{M}$$

**At Mach 20 that ceiling is 4.60 and the table demands 6.42**, so a 9,000 nautical mile glide entered at
Mach 20 is not merely hard but unavailable to any shape. **The mission becomes available at the Mach
number where demand and ceiling meet**, which is the root of

$$\frac{R}{\dfrac{R_{e}}{2} \ln\left(\dfrac{1}{1 - (M a / V_{c})^{2}}\right)} = \frac{4(M + 3)}{M}$$

and solving it numerically gives

$$M_{\min} = 22.2 \qquad V_{\min} = 6{,}537 \ \text{m/s} = 0.83 \ V_{c}$$

**The vehicle must therefore be boosted to at least 83 percent of orbital speed**, which is a statement
about the launch vehicle rather than about the glider, and it explains why the programme carried a launch
vehicle task at all.

### The Real Vehicle Confirms the Model

**One figure of merit for the vehicle that flew has been published, and it lets the model be checked.** The
lift to drag ratio of the Hypersonic Technology Vehicle 2 was estimated at **2.6**
[[Hypersonic Technology Vehicle 2][ref_htv2]]. Putting that into the range relation at the vehicle's stated
Mach 20 gives

$$R = 2.6 \times \frac{6.371 \times 10^{6}}{2} \times \ln\left(\frac{1}{1 - 0.746^{2}}\right) = 6{,}746 \ \text{km}$$

against a planned flight of **7,700 kilometres** [[Hypersonic Technology Vehicle 2][ref_htv2]].
**The model recovers 88 percent of the planned distance from two published numbers and nothing else**,
which is close enough to trust it for the argument that follows and not close enough to trust it for
design.

**Asking what the demonstrated ratio would need for the original mission closes the loop.**

$$\frac{V}{V_{c}} = \sqrt{1 - \exp\left(-\frac{16{,}668}{2.6 \times 3{,}185.5}\right)} = 0.931$$

$$V = 7{,}357 \ \text{m/s} = \text{Mach } 24.9 \ \text{at } 40 \ \text{km}$$

**The vehicle that flew would have needed boosting to 93 percent of orbital speed to make the nine
thousand mile requirement.** That is very nearly a launch to orbit, and it is the quantitative version of
the observation that boost-glide weapons and space launch are the same problem wearing different labels.

**The same model predicts how long the glide should take, and no source connects those two figures.** The
deceleration along the path is the drag divided by the mass, and drag is the lift divided by the ratio.

$$\frac{dV}{dt} = -\frac{g\left(1 - V^{2}/V_{c}^{2}\right)}{L/D}$$

**That is a gentle deceleration and it explains the flight time.** At Mach 20 it is 1.67 metres per second
squared, or 0.17 of a gravity, rising to 0.36 of a gravity as the vehicle slows and the centrifugal relief
disappears. Separating and integrating gives the time to decelerate from an entry speed to a final one.

$$t = \left(\frac{L}{D}\right) \frac{V_{c}}{g} \left[ \operatorname{artanh}\left(\frac{V_{i}}{V_{c}}\right) - \operatorname{artanh}\left(\frac{V_{f}}{V_{c}}\right) \right]$$

**Evaluating it at the published ratio and entry speed recovers the planned flight time.**

$$t = 2.6 \times \frac{7{,}904}{9.80665} \left[ \operatorname{artanh}(0.746) - \operatorname{artanh}(0.127) \right] = 1{,}755 \ \text{s} = 29.3 \ \text{min}$$

against a planned glide of **thirty minutes** [[Hypersonic Technology Vehicle 2][ref_htv2]].
**Two published numbers now reproduce both the distance and the duration of the intended flight**, which is
the strongest check available that the model describes the vehicle rather than something else.

### The Corridor Is Where the Vehicle Actually Lives

**A glider at this speed is squeezed between two conditions.** It must fly low enough for the air to hold
it up and high enough for the air not to destroy it, and the gap between those is the corridor.

The lift condition fixes the density. Let $S$ be the reference area, $C_{L}$ the lift coefficient and $W$
the weight, taking the published mass of about **900 kilograms**
[[X-41 CAV][ref_x41_parsch]].

$$\rho = \frac{2 W \left(1 - V^{2}/V_{c}^{2}\right)}{V^{2} S C_{L}}$$

At 7,000 metres per second and an assumed $S C_{L}$ of 0.45 square metres this gives

where the weight follows from the published mass.

$$W = m g = (900)(9.80665) = 8{,}826 \ \text{N}$$

$$\rho = \frac{2 (8{,}826)(0.2157)}{(7{,}000)^{2}(0.45)} = 1.73 \times 10^{-4} \ \text{kg/m}^{3}$$

**Converting a density to an altitude needs a model of the atmosphere**, and an exponential fit with a
scale height $H$ of about 6.9 kilometres is adequate at these heights.

$$\rho = \rho_{0} \exp\left(-\frac{h}{H}\right) \qquad h = -H \ln\left(\frac{\rho}{\rho_{0}}\right)$$

$$h = -6{,}900 \ln\left(\frac{1.73 \times 10^{-4}}{1.225}\right) = 61.2 \ \text{km}$$

**which is the corridor altitude used below.** The lift coefficient implied is small, as it must be at this
speed, and depends on a reference area the record does not give.

$$C_{L} = \frac{2 W \left(1 - V^{2}/V_{c}^{2}\right)}{\rho V^{2} S} = 0.225 \ \text{at} \ S = 2 \ \text{m}^{2}$$

The heating condition then follows from the stagnation-point
correlation, in which $R_{n}$ is the leading-edge radius and $k$ is $1.7415 \times 10^{-4}$ in units of
watts per square metre.

$$\dot{q} = k \sqrt{\frac{\rho}{R_{n}}} \, V^{3}$$

A surface that rejects that heat by radiation alone reaches an equilibrium temperature, where $\varepsilon$
is the emissivity and $\sigma$ the Stefan-Boltzmann constant.

$$T = \left(\frac{\dot{q}}{\varepsilon \sigma}\right)^{1/4}$$

**For a sharp edge of 50 millimetres radius at the corridor point that gives**

$$\dot{q} = 3.51 \ \text{MW/m}^{2} \qquad T = 2{,}921 \ \text{K}$$

against a published design surface temperature for the vehicle of **1,930 degrees Celsius**, or 2,203
kelvin [[Hypersonic Technology Vehicle 2][ref_htv2]].

### The Two Requirements Contradict Each Other

**Holding the published design temperature at the corridor point requires a leading-edge radius of**

$$R_{n} = \rho \left(\frac{k V^{3}}{\varepsilon \sigma T^{4}}\right)^{2} = 0.48 \ \text{m}$$

**on a vehicle 3.5 to 4.5 metres long** [[X-41 CAV][ref_x41_parsch]]. A nose radius of nearly half a metre
is more than a tenth of the vehicle's length, and blunting a hypersonic shape that much collapses its lift
to drag ratio far below the 2.6 that was measured.

**The design therefore wants a sharp edge for range and a blunt edge for survival, and cannot have both.**
Sweeping the two quantities the public record does not give, being the effective $S C_{L}$ and the
leading-edge radius, shows how narrow the escape is.

| $S C_{L}$ (m²) | $R_{n}$ = 0.05 m | $R_{n}$ = 0.20 m | $R_{n}$ = 0.48 m |
|---|---|---|---|
| 0.45 | 2,921 K | 2,457 K | 2,202 K |
| 0.90 | 2,679 K | 2,253 K | 2,019 K |
| 1.80 | 2,457 K | 2,066 K | 1,852 K |

**Five of those nine combinations exceed the published design temperature**, and every combination that
does not requires an edge blunt enough to cost the range. **That is the vehicle's central problem, and it
was derived here without a single classified number.**

## Dependent Systems

### The Aeroshell

**The aeroshell is the vehicle, which is what the programme's own name said.** The flight article was built
by Lockheed Martin from carbon composite in an arrowhead planform
[[Hypersonic Technology Vehicle 2][ref_htv2]]. **A carbon composite skin is a choice about mass rather than
about temperature**, and the sizing section shows why that choice was under pressure.

### Guidance and Control

**A glider with a lift to drag ratio near 2.6 has real manoeuvre authority and very little margin.** The
cross-range available scales with the same ratio that buys down-range, so the manoeuvrability that made the
concept attractive is bought from the same account as the range. **The public record gives no guidance
architecture**, and this article does not infer one.

### The Launch Vehicle

**The boost requirement derived above is severe and the programme's launch task reflects it.** Flight
articles were launched on a **Minotaur IV Lite** from Vandenberg Air Force Base to about **160 kilometres**
before release [[Hypersonic Technology Vehicle 2][ref_htv2]]. **A vehicle that must reach 83 to 93 percent
of orbital speed needs most of a space launcher**, and the phrase can be made exact. Specific kinetic
energy goes as the square of speed, so the fraction of orbital energy required is

$$\frac{E/m}{(E/m)_{\text{orbital}}} = \frac{V^{2}}{V_{c}^{2}}$$

$$\left(0.83\right)^{2} = 0.69 \qquad \left(0.931\right)^{2} = 0.87$$

**Between 69 and 87 percent of the energy of reaching orbit**, spent on a vehicle that then throws all of
it away in the atmosphere.

**The mass consequence follows from the rocket equation**, where $I_{sp}$ is the specific impulse of the
booster and $m_{0}/m_{f}$ the ratio of stack mass to delivered mass.

$$\frac{m_{0}}{m_{f}} = \exp\left(\frac{\Delta V}{g I_{sp}}\right)$$

At a solid-propellant specific impulse of 280 seconds and the lower of the two speeds this gives

$$\frac{m_{0}}{m_{f}} = \exp\left(\frac{6{,}537}{(9.80665)(280)}\right) = 10.8$$

**so a 900 kilogram glider needs something near ten tonnes of stack before losses**, and the vehicle
actually used was considerably larger than that. **The cheap alternative to an intercontinental ballistic
missile turns out to need most of one.**

### Payload Dispensing

**The one system that would have distinguished a weapon from a demonstrator was removed before flight.**
The Common Aero Vehicle was to dispense payloads inside the atmosphere [[X-41 CAV][ref_x41_parsch]], and
that function ended with the 2004 cancellation. **Nothing about it was ever flown**, so this article has
nothing to dimension.

## The Flight Test Record

**Two vehicles flew, both failed in the ninth minute, and the two failures were not the same.**

**Flight one was on 22 April 2010.** The vehicle was launched from Vandenberg toward Kwajalein on a planned
**7,700 kilometre, thirty minute** glide. Contact was lost after **nine minutes** when the vehicle began to
roll violently and the autopilot commanded flight termination
[[Hypersonic Technology Vehicle 2][ref_htv2]].

**Flight two was on 11 August 2011**, again planned as a thirty minute glide at Mach 20. It again ended at
about **nine minutes**, having controlled itself for roughly three minutes of degrading behaviour before
impacting the Pacific as a safety measure [[Hypersonic Technology Vehicle 2][ref_htv2]].

**Neither flight completed a third of its planned glide.** The vehicle reached Mach 20 and a surface
temperature near 1,930 degrees Celsius, which are the two headline figures the programme produced
[[Hypersonic Technology Vehicle 2][ref_htv2]].

**There was no third flight.** The agency judged that substantial data had been collected and that another
attempt was unlikely to be worth its cost [[Hypersonic Technology Vehicle 2][ref_htv2]].

## What the Data Changed

**The failure report is the programme's most valuable output and it confirms the sizing section
exactly.**

An independent engineering review board spent seven months on the second flight and concluded that
**the most probable cause was unexpected aeroshell degradation**, which created a series of upsets of
increasing severity until the flight safety system activated
[[Engineering review board concludes review of the second test flight][ref_erb]]. Some wearing of the skin
had been expected. **Larger portions than anticipated peeled away from the structure**, and the shocks
generated where the skin lifted were reported as far beyond what the vehicle was designed to take, rolling
it until the aerodynamic moments exceeded its control authority
[[Engineering review board concludes review of the second test flight][ref_erb]].

**The board's two conclusions are the ones this article's derivation predicts.** It found that
**the aerodynamic design was validated** and that what the flight actually taught concerned
**the thermal material properties** [[Engineering review board concludes review of the second test
flight][ref_erb]]. The shape worked. The edge did not.

**The board's third conclusion is the general one and it is the most important.** It found that
extrapolating from known flight regimes, relying on thermal modelling and ground testing alone, **could not
predict the realities of Mach 20 atmospheric flight**
[[Engineering review board concludes review of the second test flight][ref_erb]].

**That is a statement about the limits of ground test at the top of the speed range**, and it is the same
finding that this series has recorded for the [X-15][related_post_a312_north_american_x15] at a third of
the speed and for the [X-43][ref_x43] at a similar one. **The corridor derived above is where ground
facilities run out**, and the programme paid two vehicles to establish it.

## Where the Framing Breaks Down

**Deriving a classified vehicle from its mission is a method with three specific weaknesses, and this
article exhibits all of them.**

**First, the requirement may not be the requirement.** The 9,000 nautical mile figure is attached in the
public record to a hypersonic weapons system carrying several of these vehicles rather than to the glider
alone [[DARPA Falcon Project][ref_falcon]]. **If the glider was only ever meant to fly a fraction of that
range, the entire chain above is answering the wrong question**, and the article cannot exclude it.

**Second, equilibrium glide is an idealisation and real trajectories are not equilibrium glides.** A real
vehicle skips, phugoids and banks, and a banked turn spends lift on turning rather than on range.
**Every deviation from the idealisation reduces range for a given ratio**, so the required ratios in the
table are lower bounds and the argument is if anything understated.

**Third, the two quantities the corridor calculation needs are exactly the two the record withholds.** The
effective $S C_{L}$ and the leading-edge radius are swept rather than known, and **a reader who prefers
different values will get different temperatures.** The table is offered so that the sweep is visible
rather than hidden inside a single number.

## The Contemporary Literature

**The survey below holds 4,326 records** across 8 clusters, retrieved from the scholarly registry. **None of them is cited as evidence for any claim about the X-40A** and none was read. They map the fields the vehicle sits in, and the twelve curated sources remain the only ones the argument rests on.

### Boost-Glide Trajectories and Gliding Range

**This is the article's keystone and it is an old subject.** The equilibrium glide relation, the skip trajectory and the range available to a lifting entry body have been studied continuously since the 1950s, and the recurring result is the one derived here, that range is bought with aerodynamic efficiency and with entry speed and with nothing else.

**The harvest returned 1,018 records here, and the 25 most recent are listed. The remainder appear in the references.**

- [Liu and others, 2026, A Skip Trajectory Optimization Method for High-Speed Boost-Glide Flight Test Vehicles Based on IAPSO-NLP][research_liu_liu_2026]
- [Miao and others, 2026, A trajectory optimization method of hypersonic gliding vehicle based on differential flatness][research_miao_wang_2026]
- [Joseph and others, 2026, Aerodynamic Characterization and Flight Trajectory Reconstruction Using Pressure Measurements for a Spent Stage Re-entry with Inflatable Aerodynamic Decelerator][research_joseph_sinha_2026]
- [Matheny and Smith, 2026, Aerothermodynamic Analysis and High-Speed Schlieren Imaging of an Undergraduate-Designed Hypersonic Glide Vehicle][research_matheny_smith_2026]
- [Tong and others, 2026, An Improved Convex Optimization Method for Power-Augmented Reentry Trajectory Optimization][research_tong_wu_2026]
- [He and others, 2026, An Intelligent Trajectory Prediction Algorithm for Reentry Glide Vehicles Based on Physics-Informed Constraints and Prediction Error Compensation][research_he_li_2026_b]
- [Yu and others, 2026, Analytical solution for three-dimensional skip re-entry trajectory][research_yu_chen_2026]
- [Liu and others, 2026, Cascaded Model Predictive Control for Coordinated Formation of Hypersonic Glide Vehicle Swarms][research_liu_liang_2026]
- [Savelsberg and others, 2026, Chapter 4. The Threat of Hypersonic Glide Vehicles in A2/AD Scenarios][research_savelsberg_kampert_2026]
- [Knight and others, 2026, Characterisation of Wake-Region Optical Emissions From an Ablative Hypersonic Glide Vehicle][research_knight_kildare_2026]
- [Autenrieb and Gruhn, 2026, Control Allocation Algorithm for Hypersonic Glide Vehicles with Input Limitations][research_autenrieb_gruhn_2026]
- [Nguyen and others, 2026, Convexity of intercept time in short-range re-entry vehicle defence how to optimally intercept a fast re-entry vehicle travelling in a lofted trajectory][research_nguyen_urquhart_2026]
- [Gao and others, 2026, Coupled Heat Transfer Analysis of Hypersonic Wide-Speed-Range Cruise Aircraft][research_gao_ai_2026]
- [Hall and others, 2026, Coupling Fidelity and Stability in a Trajectory-Resolved Aerothermoelastic Analysis of a Maneuvering Hypersonic Vehicle][research_hall_schemmel_2026]
- [Wang and others, 2026, Current status and prospects of guidance techniques for intercepting hypersonic glide vehicles A review][research_wang_qu_2026]
- [Dendy and others, 2026, Design and Performance Analysis of Tachyon A Low-Altitude Hypersonic Glide Vehicle][research_dendy_hayes_2026]
- [Xue and others, 2026, Design and thermomechanical performance study of active-passive coupled thermal protection structures for hypersonic glide vehicles][research_xue_li_2026]
- [Brown and Chou, 2026, Design and Trajectory Optimization of a Shape-Morphing Aeroshell for Skip-Entry Orbital Inclination Change][research_brown_chou_2026]
- [Bonavita and others, 2026, Direct Collocation Methods for Boost-Glide Vehicle Trajectory Optimization with Newtonian Aerodynamic Model][research_bonavita_zollars_2026]
- [Cavesmith and others, 2026, Efficient Long-Range Lunar Descent Trajectory Generation with Continuous-Time Sequential Convex Programming][research_cavesmith_bhatt_2026]
- [Yin and others, 2026, Efficient long-range ship trajectory forecasting via selective state space modeling and hybrid AIS fusion][research_yin_yu_2026]
- [Wang and others, 2026, Embedded Online Trajectory Optimization Method for Hypersonic Entry][research_wang_zhang_2026]
- [Taheri and Ahmadi, 2026, Fast Cooperative Close-Range Satellite Formation Trajectory Optimization Using Finite Fourier Series Method][research_taheri_ahmadi_2026]
- [Zope and others, 2026, Generalized 5-DoF Model for Hypersonic Boost-Glide Vehicle Trajectory Predictions][research_zope_bhushan_2026]
- [Zhao and others, 2026, Glide Trajectory Optimization of Guided Projectiles Using an Improved Grey Wolf Optimizer and hp-Adaptive Radau Pseudospectral Method][research_zhao_wu_2026]

### Hypersonic Aerodynamics and the Lift to Drag Barrier

**The largest cluster covers the constraint that makes the mission hard.** Waverider design, hypersonic configuration optimisation and the empirical ceiling on lift to drag are the literature of trying to beat a limit that this article uses as a bound.

**The harvest returned 2,060 records here, and the 25 most recent are listed. The remainder appear in the references.**

- [Dodge and others, 2026, A Comparative Evaluation of Engineering-Level and RANS-Based Aerodynamic Models on the Flight Dynamics of a Generic Hypersonic Vehicle][research_dodge_lindorfer_2026]
- [Brindha and others, 2026, A comprehensive review of waverider configurations Advances in design, performance, and applications across wide-speed ranges][research_brindha_das_2026]
- [Türkoğlu and others, 2026, A locally validated surrogate-assisted design strategy for a hypersonic waverider under coupled aerodynamic and aerothermal constraints][research_turkoglu_donmez_2026]
- [Perlini and others, 2026, A Multi-Fidelity Bayesian Optimization Framework for Hypersonic Vehicle Design][research_perlini_bertolini_2026]
- [Liu and others, 2026, A novel bump/sawtooth-lip integrated hypersonic inlet Design and comprehensive aerodynamic-stealth performance analysis][research_liu_ren_2026]
- [Wexler and Idan, 2026, A Pointwise Minimum Norm Control Scheme for a Generic Air-Breathing Hypersonic Vehicle with State Constraints][research_wexler_idan_2026]
- [XU and others, 2026, A self-learning refined model and tracking for near space hypersonic vehicle by space-based radar][research_xu_pan_2026]
- [Fusco and others, 2026, A Sub Orbital Hypersonic Vehicle Preliminary Structural Sizing][research_fusco_trinchese_2026]
- [Li and others, 2026, Adaptive mechanism-data fusion modeling for control-oriented integrated air-breathing hypersonic vehicle/scramjet with multistage fuel injection][research_li_song_2026]
- [de Moura and Ribeiro, 2026, Aerodynamic and Dynamic Analysis of a Hypersonic Waverider with a Coupled Dynamic-Thermodynamic Model][research_demoura_ribeiro_2026_b]
- [Jo, 2026, Aerodynamic Heating from Compression Corner Interactions in Hypersonic Flow][research_jo_2026]
- [Ma and others, 2026, Aerodynamic Load Characterisation of Hypersonic Rudders][research_ma_wan_2026]
- [CHEN and others, 2026, Aerodynamic shape optimization of hypersonic aircraft using data-driven generative nonlinear parameterization][research_chen_li_2026]
- [Wiseman and Lopez, 2026, AI-Enhanced Control and Aerodynamic Optimization for Hypersonic Flight][research_wiseman_lopez_2026]
- [Duran and Zeng, 2026, An Automated Design-to-CFD Workflow for Hypersonic Waverider Analysis][research_duran_zeng_2026]
- [Hu and others, 2026, An enhanced radiative cooling structure based on phase change hydrogel for hypersonic vehicle][research_hu_wang_2026_b]
- [Letkemann and others, 2026, Analysis of Refractive Index Changes Near Ablative Surface of Hypersonic Vehicle][research_letkemann_tropina_2026]
- [Wang and others, 2026, Bi-directional Flying Wing with Orthogonal Coupling of Waverider and Flying Wing for Full-Speed Domain Applications Aerodynamic Configuration Design and Performance][research_wang_liu_2026]
- [Shekhawat and Sinha, 2026, Bifurcation-Based Analysis of the Longitudinal Flight Dynamics of an Air-Breathing Hypersonic Vehicle][research_shekhawat_sinha_2026]
- [Giampetro, 2026, Characterization of Hypersonic Waverider Wake at Zero Angle of Attack][research_giampetro_2026]
- [Giampetro and others, 2026, Characterization of Hypersonic Waverider Wake With Spectral Proper Orthogonal Decomposition][research_giampetro_lindau_2026]
- [Wang and others, 2026, COC-DAT a contrastive learning-based dilated attention temporal network for hypersonic flight vehicle fault diagnosis][research_wang_deng_2026]
- [Song and Tong, 2026, Collaborative Guidance and Decision Integration for Hypersonic Reentry Vehicles A Review][research_song_tong_2026]
- [Onozeki and others, 2026, Combined Aerodynamic and Structural Study on Hypersonic Aircraft With Lightweight Morphing Wing From Takeoff to Cruise][research_onozeki_shimizu_2026]
- [Rao and others, 2026, Comparing Aerothermodynamic Models With Emission Spectroscopy Data From the Atmospheric Reentry of the W-2 Hypersonic Testbed Vehicle][research_rao_crespo_2026]

### Entry Aerothermodynamics and Stagnation Heating

**The heating correlation used in the sizing section comes from this literature.** Stagnation-point heat transfer, shock-layer radiation and aerodynamic heating prediction are what turn a trajectory into a temperature, and the temperature is what decided this vehicle.

**The harvest returned 401 records here, and the 25 most recent are listed. The remainder appear in the references.**

- [Maione and others, 2026, Aerothermodynamic Analysis of a Blended Wing Body Re-entry Vehicle][research_maione_aprovitola_2026]
- [Hoter and others, 2026, Aerothermodynamic Analysis of a Flexible Thermal Protection System Under Reentry Loads][research_hoter_nastac_2026]
- [Al-Damook and others, 2026, Aerothermodynamic Parametric Analysis of Hypersonic Re-entry Capsules with Passive Decelerators][research_aldamook_shaban_2026]
- [De Prisco and others, 2026, Aerothermodynamic response of ZrB2-based compositionally complex ultra-high-temperature ceramics in hypersonic and supersonic flow conditions][research_deprisco_mungiguerra_2026]
- [Cas and others, 2026, Conservative Numerical Modeling of an Ablative Charring Heat Shield Under Deformations Validated Through Arc-Jet Tests][research_cas_baranger_2026]
- [Sabapathy, 2026, Effect of Static Fin on the Stability and Aerothermodynamic Characteristics of the Re-entry Vehicle][research_sabapathy_2026]
- [Lei and others, 2026, Fast estimation of aerodynamics-heat transfer-ablation-dynamics coupled process for reentry vehicles][research_lei_wang_2026]
- [Elmnefi, 2026, Heat Flux Measurements in Stagnation-Point Methane Flames Using LED-Based Thermographic Phosphor Thermometry][research_elmnefi_2026]
- [Joseph and others, 2026, HIFiRE-1 Flight Assessment Using MARSHAL Multiphysics Architecture for Real-time Simulation of High-speed Aerothermodynamic Loads][research_joseph_whitside_2026]
- [Gu, 2026, Isolating the specific contribution of boundary-layer edge chemical nonequilibrium to stagnation-point heating][research_gu_2026]
- [Tater and Holman, 2026, Matrix-Free LU-SGS Solver for Hypersonic Laminar Diatomic Gas Flows with Decoupled Vibrational Energy Mode Mesh Effects on Shock Waves and Separation Bubble in Double-Cone Flow][research_tater_holman_2026]
- [Riabov, 2026, Modelling Heat Transfer at Low-Density Hypersonic Spacecraft Flight Regimes][research_riabov_2026]
- [Sforza, 2026, Normal Shock Wave Approximations for Flight at Hypersonic Mach Numbers][research_sforza_2026]
- [Cabrera and West, 2026, Pioneer Venus Large Probe Stagnation Point Entry Heating with Coupled Ablation][research_cabrera_west_2026]
- [WANG and others, 2026, Prediction of separation length for hypersonic shock wave/turbulent boundary layer interactions][research_wang_zhu_2026]
- [Wang and Zuo, 2026, Separation Criterion in Hypersonic Swept Shock Wave/Turbulent Boundary Layer Interaction][research_wang_zuo_2026]
- [Menssen, 2026, Trajectory Analysis for Manned Spaceflight Aerodynamic Heating of a Two-Person Lunar-Return Vehicle][research_menssen_2026]
- [Chen and Fan, 2025, A Machine Learning Rapid Prediction of the Aerothermodynamic Environment for Near-Space Hypersonic Unmanned Aircraft][research_chen_fan_2025]
- [Hirschel and others, 2025, Aerothermodynamic Features of the External Flow Path][research_hirschel_staudacher_2025_b]
- [Ravi and others, 2025, Computational Investigation of Aerothermodynamic Characteristics of Spherical and Flat Disc Spiked Blunt Body at Hypersonic Flow][research_ravi_oda_2025]
- [Hermann, 2025, Correlation for wall-temperature oscillations in unsteady stagnation point convective heating][research_hermann_2025]
- [Hossein and others, 2025, Evaluating the influence of double curvature BOLT-2 versus conventional geometries on hypersonic aerothermodynamic effects][research_hossein_rabiee_2025]
- [Ohkage and others, 2025, Heat Shield Properties of Lightweight Ablator Series for Transfer Vehicle Systems with Different Laminated Structures Under High Enthalpy Flow Environments][research_ohkage_okuyama_2025]
- [Islam and Dutta, 2025, Machine learning assisted inverse heat transfer problem to find heat flux in ablative materials][research_islam_dutta_2025]
- [Dabas and others, 2025, Multi-Objective Optimization of Reentry Vehicle Design Aerodynamics, Heat Transfer, and Structural Durability][research_dabas_sheikh_2025]

### Thermal Protection and Leading-Edge Materials

**The binding constraint has its own field.** Ultra-high temperature ceramics, carbon composites and sharp leading-edge cooling are the technologies that would have to advance for the sizing section's contradiction to be resolved, and the failure report says they had not.

**The harvest returned 332 records here, and the 25 most recent are listed. The remainder appear in the references.**

- [Chen and others, 2026, Ablation resistance and high-temperature bending properties of free-standing ultra-high-temperature ceramics ZrB2-SiC-ZrC coating][research_chen_zhou_2026]
- [Hoffert and Wen, 2026, Approaching Experimental Conditions for Molecular Simulations of Phenol-Based Thermal Protection Materials][research_hoffert_wen_2026]
- [Monroe and Boyd, 2026, Cooling of a Hypersonic Leading Edge via Electron Emission and Absorption][research_monroe_boyd_2026]
- [Ehsan and others, 2026, Data-Driven Design of Single-Phase High-Entropy Ultra-High-Temperature Ceramics][research_ehsan_castellanos_2026]
- [Kavoosi and others, 2026, Effect of Si3N4 addition on erosion and oxidation resistance of ZrB2-SiC-ZrC ultra-high temperature ceramic composite Experimental and numerical investigation][research_kavoosi_mashhadi_2026]
- [Xin and others, 2026, Enhanced thermal protection performance of a near-space vehicle rudder system enabled by a micro-arc oxidation coating][research_xin_xu_2026]
- [Li and others, 2026, Expanding the members of ultra-high temperature ceramics and their maximum service temperature exceeding 3000 °C][research_li_zhang_2026]
- [Nykiel and others, 2026, Exploration of hexagonal, layered carbides and nitrides as ultra-high temperature ceramics][research_nykiel_wyatt_2026]
- [Rahimi and others, 2026, Functionally graded ultra-high temperature ceramics for hypersonic applications A numerical study of fracture under high-temperature extremes][research_rahimi_svolos_2026]
- [CECERE, 2026, Heat Transfer Analysis of Ultra-High-Temperature Ceramics in Plasma Wind Tunnel Experiments][research_cecere_2026]
- [Bano and others, 2026, High-Temperature Guided Wave Sensing for Thermal Protection System Structural Health Monitoring in Hypersonic Flight][research_bano_fraser_2026]
- [Lan and others, 2026, In-situ reactive spark plasma sintering and oxidation resistance of ZrB2-SiC-ZrC ultra-high temperature ceramics][research_lan_huiping_2026]
- [Susic and others, 2026, K-ADEPT Modeling the Hypersonic Reentry of an Innovative Thermal Protection System][research_susic_davuluri_2026]
- [Poudel and Shoele, 2026, Multi-Fidelity Fluid-Thermal-Structural Assessment of Heat-Pipe-Cooled Hypersonic Leading Edges][research_poudel_shoele_2026]
- [Orlandini and others, 2026, Numerical Assessment of a Multilayer Thermal Protection System of Inflatable Shields for Aerocapture and Reentry Missions][research_orlandini_paciorri_2026]
- [Connolly, 2026, Numerical Investigations of Active Cooling Architectures for Hypersonic Leading Edges][research_connolly_2026]
- [Chen and others, 2026, Recent advances in high-entropy carbide ultra-high temperature ceramics Synthesis, properties, and applications][research_chen_han_2026]
- [Zhang and others, 2026, Research Progress on Supercritical CO2 Brayton Cycle System and Compressor for Thermal Protection of Hypersonic Aircraft][research_zhang_yu_2026]
- [Zhao and others, 2026, Tailoring layer architecture to enhance the toughness of ZrB2-ZrC-SiC/C laminated ultra-high temperature ceramics][research_zhao_bai_2026]
- [Kashyap and Mitra, 2026, Thermophysical and electrical properties of spark plasma sintered ZrB2-SiC-LaB6 ultra-high temperature ceramic composites][research_kashyap_mitra_2026]
- [Aljbour, 2026, WITHDRAWAL Investigation of Roughness Induced Transition and Heating Amplification on Hypersonic Reusable Leading Edges][research_aljbour_2026]
- [Aljbour, 2026, WITHDRAWN Investigation of Roughness Induced Transition and Heating Amplification on Hypersonic Reusable Leading Edges][research_aljbour_2026_b]
- [Pang and others, 2025, Aerospace Vehicle Engine Nozzle External Thermal Protection System Design Factor Analysis][research_pang_du_2025]
- [Monroe and Boyd, 2025, Circuit Analysis of an Electron Transpiration Cooling System for Hypersonic Leading Edges][research_monroe_boyd_2025]
- [Carpman and others, 2025, Corrosion of Ultra-High Temperature Ceramics in Molten Chloride Salt][research_carpman_kelly_2025]

### Entry Guidance and Maneuvering Reentry

**A glider that cannot be steered is a ballistic reentry vehicle.** Entry guidance, trajectory planning and manoeuvring reentry are the literature of the capability that distinguished the concept from the missile it was meant to replace.

**The harvest returned 337 records here, and the 25 most recent are listed. The remainder appear in the references.**

- [Thien, 2026, Adaptive Guidance and Optimal Trajectory Generation for Highly Maneuvering UAVs][research_thien_2026]
- [Hu and others, 2026, Attitude control of multirotor with image-aided terminal guidance for precision target strike][research_hu_wang_2026]
- [Arai and Matsumoto, 2026, Convexification of Aerodynamic-Constraints for Reusable-Rockets Reentry-Burn Guidance][research_arai_matsumoto_2026]
- [Chadalavada and others, 2026, Desensitized Aerocapture Terminal Guidance][research_chadalavada_deshmukh_2026]
- [Chen and others, 2026, Explicit Trajectory Dispersion Control for Precision Landing Guidance of Reusable Rockets][research_chen_zhang_2026]
- [Tuzlukov, 2026, Guidance on Aircraft and Missile. Trajectory Control Algorithms][research_tuzlukov_2026]
- [Cui and others, 2026, Low-Order Integrated Guidance and Control Scheme for Reentry Vehicle Based on Dual-Loop Controller][research_cui_li_2026]
- [Ouyang and others, 2026, Terminal Guidance Methods for FPV Drone Precision Strike under Seeker Field-of-View Constraints][research_ouyang_wang_2026]
- [Pan and others, 2025, A Novel Attack Missile Guidance Method Considering the Terminal Angle Constraint of the Attack Missile-Target-Defense Missile Game][research_pan_ma_2025]
- [Cheng and others, 2025, A Parameter Optimization Method for Non-singular Terminal Sliding Mode Guidance Law with Falling Angle Constraint][research_cheng_shen_2025]
- [Dai and others, 2025, An Adaptive Terminal Guidance Law Based on Deep Reinforcement Learning][research_dai_yang_2025]
- [Mceowen and others, 2025, Auto-Tuned Primal-Dual Successive Convexification for Hypersonic Reentry Guidance][research_mceowen_calderone_2025_b]
- [Mceowen and others, 2025, Autotuned Primal-Dual Successive Convexification for Reentry Guidance][research_mceowen_calderone_2025]
- [Li and others, 2025, Cooperative Guidance of Glide Bombs Based on Gaussian Pseudo-spectral Method][research_li_mao_2025]
- [Wang and others, 2025, Desired Impact Angle Identification for An Incoming Aerial Vehicle Using the Trajectory Shaping Guidance Law][research_wang_wang_2025]
- [Li and others, 2025, Energy-Optimal Guidance Law Design With Terminal Impact Angle Constraints][research_li_zhang_2025]
- [Cheng and others, 2025, Geometric Approach to Lateral Guidance for Reentry Vehicle][research_cheng_song_2025]
- [Yan and Hexi, 2025, Guidance and Control Based on Nonsingular Terminal Sliding Mode Control for Asteroid Landing with a Flexible Lander][research_yan_hexi_2025]
- [Saito and others, 2025, Guidance strategies for controlled Earth reentry of small spacecraft in low Earth orbit][research_saito_kuwahara_2025]
- [Merkulov and others, 2025, Integrated Midcourse-Terminal Guidance with Delayed Target Selection][research_merkulov_shalumov_2025]
- [Jiang and others, 2025, Obstacle Avoidance Terminal Guidance Law Design Considering Terminal Angle][research_jiang_zhou_2025]
- [Chen and others, 2025, Optimal Guidance for Reusable Launch Vehicle in Reentry Phase Based on Adaptive Dynamic Programming with Experience Replay][research_chen_zhu_2025]
- [Yang and others, 2025, Optimal Midcourse Guidance Law and Cooperative Encirclement Hunting of Hypersonic Missile Group on Radau Pseudo-spectral Method][research_yang_song_2025]
- [Wei and others, 2025, Parameter Analysis and Design for Coupled-Proportional Guidance-Based Glide Slope Capture of Commercial Aircraft][research_wei_kang_2025]
- [Cui and others, 2025, Prescribed-Time Cooperative Integrated Guidance and Control for Reentry Vehicle Based on Hybrid Control Strategy][research_cui_zhen_2025]

### Launch Vehicles and Separation

**The boost requirement derived here is most of a space launch.** Small and responsive launch vehicles and the separation problem are the other half of the programme, and the smaller cluster.

**The harvest returned 86 records here, and the 25 most recent are listed. The remainder appear in the references.**

- [Long and others, 2026, Multidisciplinary modeling and dynamic Kriging assisted optimization for suborbital reusable launch vehicle][research_long_li_2026]
- [Tatsuta and others, 2025, Aerothermal Environment Prediction of Reentry Capsule With Deployable Aeroshell in Suborbital Reentry Flight Test][research_tatsuta_nagata_2025]
- [Gee and others, 2025, Examining the launch pad noise environment for a small-lift launch vehicle][research_gee_kellison_2025]
- [Kim and others, 2025, System-Level Optimization and Validation of a Small Suborbital Launch Vehicle with Rocket and Jet Propulsion][research_kim_park_2025]
- [Nguyen and Aleti, 2025, Utilizing Small Satellite Launch Vehicle - A Cross-Border Collaboration for Space Mission Australia India Technology Research and Innovation Space MAITRI by Space Machines Company and New Space India Limited][research_nguyen_aleti_2025]
- [Kaushal, 2024, Aerodynamic Optimization of Small Launch Vehicles Challenges, Design Considerations, and Future Trends][research_kaushal_2024]
- [Gomez Fernandez, 2024, Conceptual Design of a Small Launch Vehicle for CubeSats The Creative Process of Engineering Design][research_gomezfernandez_2024]
- [Li and others, 2024, Configuration Design and Application of Lm-2d Launch Vehicle Small Satellite Rideshare Mission][research_li_zhao_2024]
- [Kim and others, 2024, Fuel Efficiency Analysis of the Jet Engine and Solid-Propellant Based Small Reusable Sub-Orbital Launch Vehicle Candidates][research_kim_woldeyohannis_2024]
- [Abolghasemi Najafabadi and Kazemi, 2024, Systemic design of the very-high-resolution imaging payload of an optical remote sensing satellite for launch into the VLEO using an small launch vehicle][research_abolghaseminajafabadi_kazemi_2024]
- [Wang and Wang, 2024, Unsteady interaction and dynamic stability analysis of a two-stage-to-orbit vehicle during transverse stage separation][research_wang_wang_2024_b]
- [Shaju and others, 2023, Design and Additive Manufacturing of a Mechanical Chassis for Small Satellite Launch Vehicle Inertial Navigation Package][research_shaju_syamdas_2023]
- [He and others, 2023, Integrated design of sun-synchronous orbit and launch vehicle trajectory for operationally responsive space][research_he_gu_2023]
- [Bowden and Brown, 2023, Numerical Modeling and GNSS Observations of Ionospheric Depletions Due To a Small-Lift Launch Vehicle][research_bowden_brown_2023]
- [Haws and Bowman, 2022, Comparing Large versus Small Launch Vehicle in an Exploration Campaign][research_haws_bowman_2022]
- [Choi and others, 2022, Design of Deep Space Missions Using a Dedicated Small Launch Vehicle][research_choi_loucks_2022]
- [Gong and others, 2022, Performance Analysis on the Small-Scale Reusable Launch Vehicle][research_gong_wang_2022]
- [Villanueva, 2022, Small Modular Launch Vehicle Multidisciplinary Design Optimization][research_villanueva_2022_b]
- [Seo and others, 2022, Staging and Mission Design of a Two-Staged Small Launch Vehicle Based on the Liquid Rocket Engine Technology][research_seo_lee_2022]
- [Niederstrasser, 2022, The small launch vehicle survey a 2021 update The rockets are flying][research_niederstrasser_2022]
- [ZHANG and others, 2021, Launch Vehicle Classification for Decision-Making of Small Satellite Launch Options][research_zhang_xu_2021]
- [Jo and others, 2021, Staging and Injection Performance Analysis of Small Launch Vehicle Based on KSLV-II][research_jo_kim_2021]
- [Zheng and others, 2020, Ascent trajectory design of small-lift launch vehicle using hierarchical optimization][research_zheng_fu_2020]
- [Bailey, 2020, Frequent and Reliable Launch for Small Satellites Rocket Lab's Electron Launch Vehicle and Photon Spacecraft][research_bailey_2020]
- [Pelton and Madry, 2020, Global Launch Vehicle Systems for Potential Small Satellite Deployment][research_pelton_madry_2020]

### Detection and Tracking of Gliding Vehicles

**Whether such a vehicle can be seen is a separate question from whether it can fly.** This cluster is surveyed and not analysed, since the article makes no claim about it.

**The harvest returned 53 records here, and the 25 most recent are listed. The remainder appear in the references.**

- [Walenczykowska and others, 2024, Ballistic Missile Threat Modeling and VHF Radar Detection Performance Analysis for Tactical-Level Air Defense Simulator][research_walenczykowska_buzantowicz_2024]
- [Molchanov, 2024, Fast Radar for the Detection of Hypersonic Missiles and UASs][research_molchanov_2024]
- [Lonari and others, 2024, VISION Vehicle Infrared Signature Aware Off-Road Navigation][research_lonari_naber_2024]
- [Qu and others, 2023, Adaptive Fixed-Time Attitude Tracking Control in Reentry Phase for Reusable Launch Vehicle][research_qu_zhang_2023]
- [Wei and others, 2023, Detection of hypersonic weak targets by high pulse repetition frequency radar based on multi-hypothesis fuzzy-matching radon transform][research_wei_dandan_2023]
- [Choi and others, 2023, Effectiveness of water spray in infrared signature suppression of engine plumes][research_choi_moon_2023]
- [Luo and others, 2022, Adaptive finite-time prescribed performance attitude tracking control for reusable launch vehicle during reentry phase An event-triggered case][research_luo_wu_2022]
- [Zheng and Selezneva, 2022, Asymptotic Adaptive Roll Tracking Control for Single Moving-mass Controlled Reentry Vehicle][research_zheng_selezneva_2022]
- [Tang and others, 2022, Profile Tracking Control of Reentry Vehicle With Input-constrained Backstepping Sliding Mode Controller][research_tang_luo_2022]
- [Zewge and Bang, 2022, Reentry-phase Tracking of a Ballistic Missile in the Presence of Radar Glint Noise][research_zewge_bang_2022]
- [Guo and Fan, 2022, Research on midcourse target tracking method of ballistic missile][research_guo_fan_2022]
- [Starshak and Laurence, 2021, Computer-Graphics-Based Optical Tracking for Hypersonic Free-Flight Experiments][research_starshak_laurence_2021]
- [Kim and others, 2021, Infrared signature of NEPE, HTPB rocket plume under varying flight conditions and motor size][research_kim_kim_2021]
- [Zhang and others, 2020, LSTM-Based Boost-Phase Ballistic Missile Tracking][research_zhang_ji_2020]
- [O'Connor, 2019, Early Days of Phased Array Radars for Ballistic Missile Detection and Tracking][research_oconnor_2019]
- [Running and others, 2019, Hypersonic boundary-layer separation detection with pressure-sensitive paint for a cone at high angle of attack][research_running_sakaue_2019]
- [Gustafsson and Glendor, 2019, Infrared signature simulations of a mobile camouflage for a heavy military vehicle][research_gustafsson_glendor_2019]
- [Sun and others, 2017, Drag tracking sliding mode control for mars atmospheric reentry][research_sun_huang_2017]
- [Wang and others, 2017, Finite-time attitude tracking control design for reusable launch vehicle in reentry phase based on disturbance observer][research_wang_zou_2017]
- [Kim and others, 2017, Infrared Signature Analysis on Armored Vehicle Applied with Emissivity Controlled Structure][research_kim_kim_2017]
- [Gu and others, 2017, Infrared signature characteristic of a microturbine engine exhaust plume][research_gu_baek_2017]
- [Battistini and Menegaz, 2017, Interacting multiple model unscented filter for tracking a ballistic missile during its boost phase][research_battistini_menegaz_2017]
- [Wang and Li, 2016, A novel tracking algorithm of hypersonic target][research_wang_li_2016_c]
- [Cheng and others, 2016, Improved nonsingular terminal sliding mode attitude tracking control for reentry vehicle][research_cheng_sheng_2016]
- [Liang and others, 2015, New Design of Small Cardinality Model Set for Tracking Controllable-Structure Semiballistic Reentry Vehicle][research_liang_han_2015]

### Programme and Policy

**The smallest cluster, and small for a reason.** Open scholarship on prompt global strike as a policy question is thin next to the engineering literature, which is itself a fact about how this vehicle was discussed.

**The harvest returned 39 records here, and the 25 most recent are listed. The remainder appear in the references.**

- [Singh, 2026, Technological Innovation and Future Security-Impact of Supersonic and Hypersonic Weapon Systems on Air and Missile Defence][research_singh_2026]
- [Zhang and others, 2025, Enhanced Control System for Morphing Hypersonic Aircraft Based on an Improved Proximal Policy Optimization Algorithm][research_zhang_tang_2025]
- [Barrett, 2025, HYPERSONIC, SUPPRESSOR-COMPATIBLE SMALL ARMS AND HYPERSONIC FLIGHT-SAFE AERIAL GUNNERY AMMUNITION][research_barrett_2025]
- [Kong and others, 2024, Operational Application of Russian Hypersonic Weapon][research_kong_sun_2024]
- [Tarjáni, 2023, Hypersonic Weapon Systems as an Indicator of Changes in Concepts and Theories][research_tarjani_2023]
- [Raza and Mehmood, 2023, HYPERSONIC WEAPON SYSTEMS A NEW WAVE OF ARMS RACE IN THE INDIAN OCEAN REGION][research_raza_mehmood_2023]
- [Kong and others, 2023, Research on Hypersonic Weapon Development][research_kong_ren_2023]
- [Melville and Helmich, 2021, Hypersonic Weapons Summit Promoting Leadership in Hypersonic Development Among Research Institutions][research_melville_helmich_2021_b]
- [Malinowski, 2020, Hypersonic Weapon as a New Challenge for the Anti-aircraft Defense Command and Control System][research_malinowski_2020]
- [Thornton, 2019, Countering Prompt Global Strike The Russian Military Presence in Syria and the Eastern Mediterranean and Its Strategic Deterrence Role][research_thornton_2019]
- [Bahman Zohuri and others, 2019, New Weapon of Tomorrow's Battlefield Driven by Hypersonic Velocity][research_bahmanzohuri_patrickmcdaniel_2019]
- [O.S. KUPACH, 2018, Analyzing the US Conventional Prompt Global Strike Program][research_oskupach_2018]
- [Grego, 2018, US Ground-based midcourse missile defense Expensive and unreliable][research_grego_2018]
- [Lewis, 2017, Global strike hypersonic weapons][research_lewis_2017]
- [Peter Korzun, 2017, U.S. PROMPT GLOBAL STRIKE CONCEPT FAILS TO MAKE RUSSIA KNEEL][research_peterkorzun_2017]
- [Zvedre, 2016, Does the US program of Conventional Prompt Global Strike threaten Russian national security?][research_zvedre_2016]
- [Gormley, 2015, US Advanced Conventional Systems and Conventional Prompt Global Strike Ambitions][research_gormley_2015]
- [Marshall, 2013, A Midcourse Correction For U.S. Missile Defense System][research_marshall_2013]
- [Scheber and Guthe, 2013, Conventional Prompt Global Strike A Fresh Perspective][research_scheber_guthe_2013]
- [West, 2012, Minority Report Potential Challenges in Employing Global Strike Against Violent Non-State Actors in 2035][research_west_2012]
- [Anin, 2011, PROMPT GLOBAL STRIKE WEAPONS AND STRATEGIC INSTABILITY][research_anin_2011]
- [Hopkins and others, 2010, The analysis of conventional Prompt Global Strike alternatives][research_hopkins_raymond_2010]
- [Pollack, 2009, Evaluating Conventional Prompt Global Strike][research_pollack_2009]
- [Spinardi, 2008, Ballistic missile defence and the politics of testing the case of the US ground-based midcourse defence][research_spinardi_2008]
- [Chen and others, 2008, Terminal and Boost Phase Intercept of Ballistic Missile Defense][research_chen_speyer_2008]

## The Source Base

**Twelve curated sources carry the argument and 4,326 harvested records map the field, and
the article keeps them apart.**

**The curated set is small because the vehicle is small.** Two of the twelve are the manufacturer's own
press release and the space agency's programme page, two are designation references, one is a
contemporaneous report of the second free flight, one is the successor vehicle's specification, and the
remainder define terms. **Every quantitative claim in this article traces to the published dimensions,
masses and flight figures in that set**, and every derived number is computed here rather than quoted.

**The harvested set was never read.** 15,209 records were retrieved and 4,470
passed the subject gate, of which 4,326 reach the reference list after 47
duplicate registrations were removed. **Not one is cited in support of a claim about the X-40A.**

**The gate was audited by reading random samples of both sides, which is the return protocol rather than
a recommendation.** Reading found two families in the first pass, being the **underwater glider**, which
shares glide, trajectory, range and vehicle with a hypersonic glider and shares nothing else, and the
**block-glide landslide**, which also collects the phrase front range.

**A third family survived the samples and was found by checking an out-of-place publisher prefix.** A
condensed-matter physics identifier in the reference list led to the **nanofluid stagnation-point flow**
literature, a large applied-mathematical field concerning flow over stretching sheets and spinning spheres
that shares the terms stagnation point and heat transfer with reentry aerothermodynamics and shares no
physics of interest. **Ninety-seven records had reached the corpus and were removed**, which is 2.2 percent
of it, and the entry aerothermodynamics cluster fell from 489 records to 401 as a result.

**That is the third consecutive article on which a publisher-prefix check has beaten the random sample**,
and it is now part of the routine rather than a lucky catch. Reading found two homonym families that no count would have shown. **The runway is a
piece of apparatus in animal behaviour research**, a straight alley a rat runs down for reinforcement, and
one such record had been admitted. **Disaster risk reduction shares both words with flight risk reduction
and nothing else.** Both are now excluded, and the article claims a clean corpus nowhere.

**One inherited defect is absent here because A336 paid for it.** The qualifier helper wraps each part in
a non-capturing group, so an alternation cannot escape its lookahead and turn a conjunction into a
disjunction of bare words. **That defect made the previous article's gate simultaneously too permissive
and too narrow**, and it was invisible in every statistic.

## Epistemic State

### Historical Fact

The Common Aero Vehicle was a manoeuvrable hypersonic reentry vehicle intended to dispense payloads inside
the atmosphere, with Aero standing for aeroshell. In December 2002 the Air Force programme was merged with
a Defense Advanced Research Projects Agency effort into the Force Application and Launch from the
Continental United States programme, carrying a small launch vehicle task and an aero vehicle task. By 2004
the offensive strike element was cancelled, the vehicle was renamed the Hypersonic Technology Vehicle, and
weaponisation research ended. Congress had restricted funding for the strike mission across several years.
The programme sought to strike targets 9,000 nautical miles from the continental United States with about
1,000 pounds of payload. Vehicles were about 3.5 to 4.5 metres long and about 900 kilograms. The second
Hypersonic Technology Vehicle was built by Lockheed Martin from carbon composite in an arrowhead planform,
had an estimated lift to drag ratio of 2.6, was designed for a surface temperature near 1,930 degrees
Celsius, and was launched on a Minotaur IV Lite from Vandenberg Air Force Base to about 160 kilometres. It
flew on 22 April 2010 and 11 August 2011, each time ending near the ninth minute of a planned thirty minute
glide. No third flight was conducted.

### Engineering Analysis

**Every quantitative result here is computed from published figures using standard relations, and each was
recomputed independently before use.** The circular speed, the equilibrium glide condition and the range
relation are textbook results carrying no vehicle property. The Küchemann correlation is empirical and is
used as a bound rather than as a prediction. The lift condition, the stagnation-point heating correlation
and the radiative equilibrium temperature are standard.

**The model was validated against the one published performance figure before it was used to argue.**
Feeding the estimated lift to drag ratio of 2.6 and the stated Mach 20 into the range relation recovers 88
percent of the planned flight distance. **That is good agreement for a two-parameter model and it is not
good enough to size hardware.**

### Inference

**That the leading edge is the binding constraint is an inference**, though a well-supported one. It
follows from the corridor calculation and is corroborated by the failure report, which attributes the loss
to aeroshell degradation and states that the aerodynamic design was validated. **No source frames the
vehicle's central problem this way.**

**That the vehicle would have needed boosting to 93 percent of orbital speed is an inference** conditional
on the 9,000 nautical mile figure applying to the glider, which the record does not establish.

### What the Record Does Not Settle

**Whether the X-41 designation belongs to this vehicle at all is not settled**, and the authoritative
survey says so. The designation was allocated in late 1997 or early 1998, years before the programme, was
never used again officially, and its applicability to the Common Aero Vehicle is explicitly doubted
[[X-41 CAV][ref_x41_parsch]]. **This article uses the pairing because the public record does, and records
that the pairing may be wrong.**

**No specifications or photographs of the Common Aero Vehicle have been released**, so every dimension used
here belongs to the Hypersonic Technology Vehicle that succeeded it, **and there is arithmetic showing the
two cannot be the same vehicle.** The payload figure attached to the Common Aero Vehicle is 1,000 pounds
[[X-41 Common Aero Vehicle][ref_x41_wiki]], against a Hypersonic Technology Vehicle mass of about 900
kilograms [[X-41 CAV][ref_x41_parsch]].

$$\frac{1{,}000 \ \text{lb}}{900 \ \text{kg}} = \frac{454}{900} = 0.50$$

**A payload half the mass of the whole vehicle is not credible for a hypersonic glider**, so either the
payload figure belongs to a larger design than the one that flew, or the mass figure belongs to a stripped
demonstrator carrying nothing. **The record does not say which**, and this article uses each figure only
where it is safe to.

**The reference area, the lift coefficient and the leading-edge radius are not published.** They are swept
across a plausible range rather than assumed, and the conclusion is stated as holding across the sweep
rather than at a point.

**Whether the 9,000 nautical mile requirement applied to the glider or to the larger system that would
carry several of them is not settled**, and the framing section says what that does to the argument.

**The cause of the first flight's failure is described only as a violent roll leading to commanded flight
termination**, and no engineering review board conclusion for that flight is quoted here.

**The relationship between this vehicle and later hypersonic glide programmes is outside what the record
supports**, and this article does not trace it.

## Out of Scope

The Small Launch Vehicle task of the same programme, which deserves separate treatment. The air-breathing
hypersonic cruise vehicle studied under the same name, which is a different vehicle with a different
problem. Prompt global strike as a policy question, and the arms-control literature on distinguishing
conventional from nuclear boost-glide payloads. The later Hypersonic Technology Vehicle 3 concept. Scramjet
propulsion, which this vehicle did not use. Ablative thermal protection design, which is surveyed here and
not analysed. The detection and tracking of hypersonic glide vehicles, which is surveyed and not analysed.

## Conclusion

**A vehicle with no published specifications can still be bounded, because its mission is a physics
problem.** A range of 9,000 nautical miles and the equilibrium glide relation demand a lift to drag ratio
that the Küchemann barrier refuses below **Mach 22.2**, so the glider had to be boosted to at least
**83 percent of orbital speed**, and at the ratio of **2.6** that was actually measured, to **93 percent**.

**The corridor that follows is where the vehicle breaks.** Flying low enough to be held up by the air puts
a 50 millimetre leading edge at about **2,921 kelvin**, against a published design value of **2,203**.
Holding the design value needs an edge radius of **0.48 metres** on a vehicle four metres long, and that
much bluntness costs the range the sharpness was for. **Five of the nine plausible combinations swept here
exceed the design temperature.**

**Both flights ended in the ninth minute of a thirty minute glide**, and the failure board found unexpected
aeroshell degradation, larger than expected skin loss, and roll upsets beyond the vehicle's control
authority. **It also found that the aerodynamic design was validated and that the surprise was thermal.**

**The shape was never the problem. The edge was**, and the arithmetic said so before the vehicle flew.

The next article returns to a vehicle whose designation is not in doubt.

## References

### Reference

- [DARPA Falcon Project][ref_falcon]
- [Engineering review board concludes review of the second test flight][ref_erb]
- [Hypersonic Technology Vehicle 2][ref_htv2]
- [Minotaur IV][ref_minotaur]
- [NASA X-43][ref_x43]
- [Prompt Global Strike][ref_pgs]
- [X-41 CAV][ref_x41_parsch]
- [X-41 Common Aero Vehicle][ref_x41_wiki]

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
- [X-Planes: Boeing X-32][related_post_a329_boeing_x32]
- [X-Planes: Boeing X-37][related_post_a334_boeing_x37]
- [X-Planes: Boeing X-40][related_post_a337_boeing_x40]
- [X-Planes: Convair X-11][related_post_a308_convair_x11]
- [X-Planes: Convair X-12][related_post_a309_convair_x12]
- [X-Planes: Convair X-6][related_post_a303_convair_x6]
- [X-Planes: Curtiss-Wright X-19][related_post_a316_curtiss_wright_x19]
- [X-Planes: Douglas X-3 Stiletto][related_post_a300_douglas_x3]
- [X-Planes: Framing and the Research Aircraft Model][related_post_a297_framing]
- [X-Planes: Grumman X-29][related_post_a326_grumman_x29]
- [X-Planes: Hiller X-18][related_post_a315_hiller_x18]
- [X-Planes: Lockheed Martin X-33][related_post_a330_lockheed_martin_x33]
- [X-Planes: Lockheed Martin X-35][related_post_a332_lockheed_martin_x35]
- [X-Planes: Lockheed X-17][related_post_a314_lockheed_x17]
- [X-Planes: Lockheed X-27][related_post_a324_lockheed_x27]
- [X-Planes: Lockheed X-7][related_post_a304_lockheed_x7]
- [X-Planes: Martin Marietta X-23 PRIME and a Contested Assignment][related_post_a320_martin_marietta_x23]
- [X-Planes: Martin Marietta X-24][related_post_a321_martin_marietta_x24]
- [X-Planes: McDonnell Douglas X-36][related_post_a333_mcdonnell_douglas_x36]
- [X-Planes: North American X-10][related_post_a307_north_american_x10]
- [X-Planes: North American X-15][related_post_a312_north_american_x15]
- [X-Planes: Northrop X-21][related_post_a318_northrop_x21]
- [X-Planes: Northrop X-4 Bantam][related_post_a301_northrop_x4]
- [X-Planes: Orbital Sciences X-34][related_post_a331_orbital_sciences_x34]
- [X-Planes: Osprey X-28 Sea Skimmer][related_post_a325_osprey_x28]
- [X-Planes: Rockwell X-30 and the National Aero-Space Plane][related_post_a327_rockwell_x30]
- [X-Planes: Rockwell-MBB X-31][related_post_a328_rockwell_mbb_x31]
- [X-Planes: Ryan X-13 Vertijet][related_post_a310_ryan_x13]
- [X-Planes: Scaled Composites X-38][related_post_a335_scaled_composites_x38]
- [X-Planes: Schweizer X-26 Frigate][related_post_a323_schweizer_x26]
- [X-Planes: X-39, Reserved but Never Assigned][related_post_a336_x39_reserved_never_assigned]

### Research

- [1962, Automatic Re-Entry Guidance At Escape Velocity][research_automatic_re_entry_1962]
- [1962, Shock Layer Structure and Entropy Layers in Hypersonic Conical Flows][research_shock_layer_1962]
- [1962, Terminal Guidance System For Soft Lunar Landing][research_terminal_guidance_1962]
- [1963, Design Considerations for a Re-Entry Vehicle Thermal Protection System][research_design_considerations_1963]
- [1963, Supercircular Re-Entry Guidance for a Fixed L/D Vehicle Employing a Skip for Extreme Ranges][research_supercircular_re_entry_1963]
- [1963, Thermal Protection System for Extravehicular Space Suits][research_thermal_protection_1963]
- [1964, A Simple Re-Entry Guidance System][research_a_simple_1964]
- [1964, Boost Vehicle Trajectories for Ranger and Mariner Programs][research_boost_vehicle_1964]
- [1969, A Rapid Technique for Estimating Ablative Heat Shield Weights from Plasma Jet Test Data][research_a_rapid_1969]
- [1975, Nonequilibrium Stagnation Region Aerodynamic Heating of Hypersonic Glide Vehicles][research_nonequilibrium_stagnation_1975]
- [1975, Performance of Ablative Materials in Ramjet Environments][research_performance_of_1975]
- [1977, External Flows Drag Reduction of a Sharp Flat Plate in a Rarefied Hypersonic Flow][research_external_flows_1977_b]
- [1977, External Flows Flat Plate Skin Friction in the Range Between Hypersonic Continuum and Free Molecular Flow][research_external_flows_1977]
- [1978, Aerothermodynamic Base Heating][research_aerothermodynamic_base_1978]
- [1979, Aerodynamic Heating to the X-24C Hypersonic Research Configuration][research_aerodynamic_heating_1979]
- [1979, Aerothermodynamic Assessment of Corrugated Panel Thermal Protection Systems][research_aerothermodynamic_assessment_1979]
- [1979, Aerothermodynamic Environment for Jovian Entry with Silica Heat Shield][research_aerothermodynamic_environment_1979]
- [1980, Thermal protection system for filament wound pressure vessels][research_thermal_protection_1980]
- [1981, Optimal Glide of Reentry Vehicles][research_optimal_glide_1981]
- [1981, Thermal Protection System for the Galileo Mission Atmospheric Entry Probe][research_thermal_protection_1981]
- [1982, Aerothermodynamic Design Feasibility of a Generic Planetary Aerocapture/Aeromaneuver Vehicle][research_aerothermodynamic_design_1982]
- [1982, Analysis of Aerothermodynamic Environment of a Titan Aerocapture Vehicle][research_analysis_of_1982]
- [1982, The Hypersonic Flowfield over a Re-entry Vehicle Indented-Nose Configuration][research_the_hypersonic_1982]
- [1983, Aerothermodynamic Entry Environment of the Space Shuttle Orbiter][research_aerothermodynamic_entry_1983]
- [1983, Assessment of Alternate Thermal Protection Systems for the Space Shuttle Orbiter][research_assessment_of_1983]
- [1983, Preliminary Design of the Thermal Protection System for Solar Probe][research_preliminary_design_1983]
- [1983, Space Shuttle Orbiter Leading Edge Thermal Performance][research_space_shuttle_1983]
- [1983, Tile-Gap Flow in the Shuttle Orbiter Thermal Protection System][research_tile_gap_flow_1983]
- [1983, Viscous Shock-Layer Predictions for Hypersonic Laminar or Turbulent Flows in Chemical Equilibrium over the Windward Surface of a Shuttle-Like Vehicle][research_viscous_shock_layer_1983]
- [1985, Aerothermodynamic Heating Analysis of Aerobraking and Aeromaneuvering Orbital Transfer Vehicles][research_aerothermodynamic_heating_1985]
- [1985, Analytical Characterization of AOTV Perigee Aerothermodynamic Regime][research_analytical_characterization_1985]
- [1985, Thermal Protection Requirements for Near-Earth Aeroassisted Orbital Transfer Vehicle Missions][research_thermal_protection_1985]
- [1986, Approximate analysis of the motion and heating of hypersonic/transatmospheric vehicles][research_approximate_analysis_1986]
- [1986, Drag of Bodies in Rarefied Hypersonic Flow][research_drag_of_1986]
- [1986, Effects of Surface Discontinuities on Convective Heat Transfer in Hypersonic Flow][research_effects_of_1986]
- [1986, Heat Transfer on a Flat Plate in Continuum to Rarefied Hypersonic Flows at Mach 19.2 and 25.4][research_heat_transfer_1986]
- [1986, Numerical Simulation of Hypersonic Viscous Fore- and Afterbody Flows over Capsule-Type Vehicles at Angles of Attack][research_numerical_simulation_1986]
- [1986, Waverider Aerodynamics][research_waverider_aerodynamics_1986]
- [1988, Computation of skin friction and heat transfer with inclusion of stagnation heating of roughness elements for turbulent boundary layer flows][research_computation_of_1988]
- [1988, Hypersonic Aerodynamics][research_hypersonic_aerodynamics_1988]
- [1989, Monte Carlo Simulation of Flow into Channel with Sharp Leading Edge][research_monte_carlo_1989]
- [1990, Computational Fluid Dynamics Design Applications at Supersonic/Hypersonic Speeds][research_computational_fluid_1990]
- [1990, Supersonic/Hypersonic Euler Flowfield Prediction Method for Aircraft Configurations][research_supersonic_hypersonic_euler_1990]
- [1992, Light High-Temperature Aluminum Alloys for Supersonic and Hypersonic Vehicles][research_light_high_temperature_1992]
- [1993, Aerothermodynamic design of a hypersonic lifting body including GPS navigation capability][research_aerothermodynamic_design_1993]
- [1993, Aircraft design at the Naval Postgraduate School - Tactical waverider/long-range cargo aircraft][research_aircraft_design_1993]
- [1993, Design of a hypersonic waverider-derived airplane][research_design_of_1993]
- [1994, 188 Nonlinear control approach to reentry guidance of a spacecraft][research_188_nonlinear_1994]
- [1994, 212 Problems in control system design for hypersonic vehicles][research_212_problems_1994]
- [1994, 264 Guidance and trajectory optimization under state constraints Applied to a Sänger-type vehicle][research_264_guidance_1994]
- [1994, 266 On ascent guidance of hypersonic vehicle][research_266_on_1994]
- [1994, Aerodynamic Optimization for Hypersonic Flight at Very High Altitudes][research_aerodynamic_optimization_1994]
- [1994, CFD optimization and test validation of 2D ramjet nozzle for hypersonic vehicle][research_cfd_optimization_1994]
- [1994, Manned Mars Entry Vehicle Aerothermodynamic Analysis][research_manned_mars_1994]
- [1994, Numerical Analysis of Aerothermodynamic Environment of HITEN Spacecraft Aerobrake Experiment][research_numerical_analysis_1994]
- [1994, Rarefied Hypersonic Flow over a Flat Plate with Truncated Leading Edge][research_rarefied_hypersonic_1994]
- [1994, Slender Lifting Body Axial Force Prediction in Hypersonic Rarefied Flow][research_slender_lifting_1994]
- [1996, Optimal Aerodynamic Shapes Of A Hypersonic Vehicle With An Airbreathing Engine][research_optimal_aerodynamic_1996]
- [2001, Rudiments and Methodology for Design and Analysis of Hypersonic Airbreathing Vehicles][research_rudiments_and_2001]
- [2002, 3-Dimensional Trajectory Optimization and Explicit Guidance for a Satellite Launch Vehicle with Yaw Maneuver][research_3_dimensional_trajectory_2002]
- [2002, Aerothermodynamics Research in the DLR High Enthalpy Shock Tunnel HEG][research_aerothermodynamics_research_2002]
- [2002, Arc-Heated Facilities as a Tool to Study Aerothermodynamic Problems of Reentry Vehicles][research_arc_heated_facilities_2002]
- [2002, Characteristics of the HIEST and its Applicability for Hypersonic Aerothermodynamic and Scramjet Research][research_characteristics_of_2002]
- [2004, Aerothermodynamic Predictions for Hypersonic Reentry Vehicles][research_aerothermodynamic_predictions_2004]
- [2004, Development and Prospect of Air Launch Vehicle][research_development_and_2004]
- [2004, The FALCON Small Satellite Launch Vehicle Development and First Flight][research_the_falcon_2004]
- [2006, Viscous Flow Basic Aspects, Boundary Layer Results, and Aerodynamic Heating][research_viscous_flow_2006]
- [2008, Design/Construction and Performance Test of Hypersonic Shock Tunnel Part Ⅰ Design Method of Hypersonic Shock Tunnel][research_design_construction_and_2008]
- [2008, Numerical Research of Three-Dimensional Section Controllable Internal Waverider Hypersonic Inlet][research_numerical_research_2008]
- [2011, DSC attracts funding to boost long-range 3D facial recognition][research_dsc_attracts_2011]
- [2011, DSM acquires Vitatene to boost carotenoid colorants range][research_dsm_acquires_2011]
- [2011, Optimization Using Entropy-Generation Minimization for Maximum Performance of Hypersonic Vehicles][research_optimization_using_2011]
- [2012, Waverider Aircraft][research_waverider_aircraft_2012]
- [2013, Chapter 13 Numerical Modeling of Hypersonic Heat Transfer on the Windward Side of the Buran Reentry Vehicle][research_chapter_13_2013]
- [2013, Chapter 14 Mathematical Modeling of Heat and Mass Transfer during Aerothermochemical Destruction of Thermal Protection Materials][research_chapter_14_2013]
- [2013, Chapter 6 Modeling of Catalytic Properties of Thermal Protection Coatings of Space Vehicles][research_chapter_6_2013]
- [2013, Thermal Protection System Conception][research_thermal_protection_2013]
- [2014, A new guidance method for reentry warhead against a stationary target][research_a_new_2014]
- [2014, aerothermodynamic border][research_aerothermodynamic_border_2014]
- [2014, Thermal Protection System][research_thermal_protection_2014]
- [2015, Thermal Protection for a Re-Entry Vehicle Using Heat Ablation Process][research_thermal_protection_2015]
- [2016, Hypersonic Aerodynamics][research_hypersonic_aerodynamics_2016]
- [2017, Clutter suppression for hypersonic vehicle-borne radar with frequency diverse array][research_clutter_suppression_2017]
- [2017, Multi-objective reentry trajectory optimization method via GVD for hypersonic vehicles][research_multi_objective_reentry_2017]
- [2018, Coupled dynamic model of state estimation for hypersonic glide vehicle][research_coupled_dynamic_2018]
- [2018, Hypersonic Thin Viscous Shock Layer][research_hypersonic_thin_2018]
- [2018, Radiative Heat Transfer In Hypersonic Inviscid Flow][research_radiative_heat_2018]
- [2019, Viscous Flow Basic Aspects, Boundary Layer Results, and Aerodynamic Heating][research_viscous_flow_2019]
- [2020, Review 1 of "Use of the federal guidelines while maneuvering to achieve 'justice' A non-participant observational study of judicial sentencing discretion in illegal reentry cases in a U.S. District Court"][research_review_1_2020]
- [2020, Review 2 of "Use of the federal guidelines while maneuvering to achieve 'justice' A non-participant observational study of judicial sentencing discretion in illegal reentry cases in a U.S. District Court"][research_review_2_2020]
- [2020, Review 3 of "Use of the federal guidelines while maneuvering to achieve 'justice' A non-participant observational study of judicial sentencing discretion in illegal reentry cases in a U.S. District Court"][research_review_3_2020]
- [2022, Waverider Buoy][research_waverider_buoy_2022]
- [2023, Aerothermodynamic Testing and Hypersonic Physics][research_aerothermodynamic_testing_2023]
- [2023, Direct numerical simulations of hypersonic boundary layer transition over a hypersonic transition research vehicle model lifting body at different angles of attack][research_direct_numerical_2023]
- [2023, Hypersonic Materials for Thermal Protection][research_hypersonic_materials_2023]
- [2023, Shock-Wave Relations and Aerothermodynamic States][research_shock_wave_relations_2023]
- [2023, Terminal Phase Guidance Design for an Anti-Ship Bank-To-Turn BTT Cruise Missile][research_terminal_phase_2023]
- [2023, Unsteady interaction mechanism of transverse stage separation in hypersonic flow for a two-stage-to-orbit vehicle][research_unsteady_interaction_2023]
- [2024, Reentry Trajectory Estimation][research_reentry_trajectory_2024]
- [2025, Aero-heating prediction model for hypersonic vehicles][research_aero_heating_prediction_2025]
- [2025, APPLICATION OF HYPERSONIC VEHICLE RE-ENTRY PLASMA FORMATION AND RF BLACKOUT NUMERICAL MODELING BY "HYPERSMS AEROTHERMODYNAMIC"][research_application_of_2025]
- [2025, Reentry Maneuvering Vehicle Ascent Phase Trajectory Design][research_reentry_maneuvering_2025]
- [2025, Research Progress in Carbide Ultra-high Temperature Ceramics for Equipment Thermal Protection][research_research_progress_2025]
- [2025, Trajectory Shaping Guidance for Vertical Landing of Launch Vehicle Stage][research_trajectory_shaping_2025]
- [Abbasi and Mortazavi, 2013, A New Concept for Atmospheric Reentry Optimal Guidance An Inverse Problem Inspired Approach][research_abbasi_mortazavi_2013]
- [Abolghasemi Najafabadi and Kazemi, 2024, Systemic design of the very-high-resolution imaging payload of an optical remote sensing satellite for launch into the VLEO using an small launch vehicle][research_abolghaseminajafabadi_kazemi_2024]
- [ABU-ROMIA, 1971, Measurement of stagnation-point heat transfer from plasma torch by using heat pipe calorimetry][research_aburomia_1971]
- [Achambath and others, 2019, Surface Properties on Thermal Protection System Microstructure during Hypersonic Ablation][research_achambath_ramjatan_2019]
- [Acton, 2015, Hypersonic Boost-Glide Weapons][research_acton_2015]
- [Adami and Nosratolahi, 2009, Optimizing 3-D PN Guidance Law for Accelerated Reentry Vehicles][research_adami_nosratolahi_2009]
- [Adami and others, 2011, Multidisciplinary design optimization of a manned reentry mission considering trajectory and aerodynamic configuration][research_adami_nosratollahi_2011]
- [Adami and others, 2017, A New Approach to Multidisciplinary Design Optimization of Solid Propulsion System Including Heat Transfer and Ablative Cooling][research_adami_mortazavi_2017]
- [Adami and Zhu, 2007, Control of a Flexible, Hypersonic Scramjet Vehicle Using a Differential Algebraic Approach][research_adami_zhu_2007]
- [Adami and Zhu, 2008, Control of a Flexible, Hypersonic Scramjet Vehicle Using a Differential Algebraic Approach][research_adami_zhu_2008]
- [Adamo and others, 1978, A GOES--Reporting Waverider Buoy][research_adamo_steele_1978]
- [Adamov and others, 2014, Damping characteristics of a reentry vehicle at hypersonic velocities][research_adamov_puzyrev_2014]
- [Adams and others, 1973, Hypersonic Lifting Body Windward Surface Flow-Field Analysis for High Angles of Incidence][research_adams_johnc_1973]
- [Adsit and others, 1972, Mechanical Behavior of Three-Dimensional Composite Ablative Materials][research_adsit_carnahan_1972]
- [Afzal and others, 2009, An Explicit Guidance Method for a Lifting Interplanetary Re-Entry Vehicle][research_afzal_roeser_2009]
- [Agarwal and Nisar, 2025, Understanding rheology and sedimentation of ultra-high temperature ceramics for digital light processing based additive manufacturing][research_agarwal_nisar_2025]
- [Agarwal, 2011, Selected aerothermodynamic design problems of hypersonic flight vehicles][research_agarwal_2011]
- [Aggarwal and Moore, 1996, A terminal guidance algorithm for ramjet-powered missiles][research_aggarwal_moore_1996]
- [Aggarwal and Moore, 1998, Terminal Guidance Algorithm for Ramjet-Powered Missiles][research_aggarwal_moore_1998]
- [AGNONE and others, 1985, HYPERSONIC FLOW OVER A SI X FINNED CONFIGURATION][research_agnone_zakkay_1985]
- [Agnone and others, 1988, Hypersonic flow over a six-finned configuration][research_agnone_zakkay_1988]
- [Agostinelli and others, 2019, Aerothermodynamic analyses and redesign of GHIBLI Plasma Wind Tunnel hypersonic diffuser][research_agostinelli_trifoni_2019]
- [Agustin and others, 1998, Robust failure detection for reentry vehicle attitude control systems][research_agustin_mangoubi_1998]
- [Agustin and others, 1999, Robust Failure Detection for Reentry Vehicle Attitude Control Systems][research_agustin_mangoubi_1999]
- [Ahmad and others, 2022, Determination of extreme responses of USFG's equilibrium glide path hovering in ocean current][research_ahmad_xing_2022]
- [Ahmed and Qin, 2009, Comparison of Response Surface and Kriging Surrogates in Aerodynamic Design Optimization of Hypersonic Spiked Blunt Bodies][research_ahmed_qin_2009]
- [Ahmed and Qin, 2010, Metamodels for aerothermodynamic design optimization of hypersonic spiked blunt bodies][research_ahmed_qin_2010]
- [Ahmed and Qin, 2011, Surrogate-Based Multi-Objective Aerothermodynamic Design Optimization of Hypersonic Spiked Bodies][research_ahmed_qin_2011]
- [Ahmed and Qin, 2012, Surrogate-Based Multi-objective Aerothermodynamic Design Optimization of Hypersonic Spiked Bodies][research_ahmed_qin_2012]
- [Ahuja and Hartfield, 2009, Optimization of Air-breathing Hypersonic Aircraft Design for Maximum Cruise Speeds using Genetic Algorithms][research_ahuja_hartfield_2009]
- [AIR FORCE TEST PILOT SCHOOL EDWARDS AFB CA, 1987, Volume 1. Aircraft Performance. Chapter 10. Hypersonic Aerodynamics][research_airforcetestpilotschooledwardsafbca_1987]
- [Akinbo and Olajuwon, 2021, Impact of radiation and chemical reaction on stagnation-point flow of Hydromagnetic Walters' B fluid with Newtonian heating][research_akinbo_olajuwon_2021]
- [Al-Damook and others, 2026, Aerothermodynamic Parametric Analysis of Hypersonic Re-entry Capsules with Passive Decelerators][research_aldamook_shaban_2026]
- [Alavi and others, 2015, Numerical solutions of the stagnation-point flow and heat transfer towards an exponentially stretching/ shrinking sheet with constant heat flux][research_alavi_rosli_2015]
- [Albano and others, 2013, Electromagnetic shielding of thermal protection system for hypersonic vehicles][research_albano_micheli_2013]
- [Alber, 2012, Estimating the Orbiter reentry trajectory and the associated peak heating rates][research_alber_2012]
- [Albert and Braun, 2020, Conceptual Development of AeroDrop Aerocapture and Direct Entry for Two Spacecraft on a Common Approach Trajectory][research_albert_braun_2020]
- [Alexander and T. M, 1978, Explicit Guidance Equations for a Variable Trim Reentry Vehicle][research_alexander_tm_1978]
- [Alexander, 1970, A Transducer for Controlling Simulated Aerodynamic Heating][research_alexander_1970]
- [Alferov and Marchenko, 2012, Erbium oxide aerodynamic models in the hypersonic flow][research_alferov_marchenko_2012]
- [Aljbour, 2026, WITHDRAWAL Investigation of Roughness Induced Transition and Heating Amplification on Hypersonic Reusable Leading Edges][research_aljbour_2026]
- [Aljbour, 2026, WITHDRAWN Investigation of Roughness Induced Transition and Heating Amplification on Hypersonic Reusable Leading Edges][research_aljbour_2026_b]
- [Alkandry and others, 2014, Comparison of Transport Properties Models for Flowfield Simulations of Ablative Heat Shields][research_alkandry_boyd_2014]
- [Alkaya and others, 2018, Conceptual Advanced Transport Aircraft Design Configuration for Sustained Hypersonic Flight][research_alkaya_alexsam_2018]
- [Allegre and others, 1992, TEST CASE VTI-5 Aerodynamic Forces Applied to a Delta Wing Located in Rarefied Hypersonic Flows][research_allegre_heriarddubreuilh_1992]
- [Allouche and others, 2011, Study of Thermo-Chemical Non-Equilibrium Phenomena behind Strong Shock Waves at Atmospheric Reentry][research_allouche_haoui_2011]
- [Allouche and others, 2020, Prediction of the optimal speed of an aerospace vehicle by aerothermochemical analysis of hypersonic flow during atmospheric re-entry][research_allouche_renane_2020]
- [Almeida, 2021, Model Predictive Control and Constrained Dynamic Compensation for a Hypersonic Flight Vehicle][research_almeida_2021]
- [Alshibani and others, 2022, The Job Satisfaction Trajectory During Entrepreneurship Entry and Beyond][research_alshibani_volery_2022]
- [Amaratunga and others, 1996, Numerical predictions of hypersonic flow past a body/body-flap configuration][research_amaratunga_tutty_1996]
- [Amati and others, 2008, Exergy analysis of hypersonic propulsion systems Performance comparison of two different scramjet configurations at cruise conditions][research_amati_bruno_2008]
- [Amato and others, 2026, HyperCODA Validation for Hypersonic Flight Flow Simulations of a Reentry Vehicle][research_amato_giannino_2026]
- [AMIRKABIRIAN and others, 1986, The aerothermodynamic environment for hypersonic flow past a simulated wing leading-edge][research_amirkabirian_bertin_1986]
- [Ammendola and others, 2025, Mechanical properties of ultra-high temperature ceramic matrix composites UHTCMCs A review][research_ammendola_kedir_2025]
- [Amrutha and Hari Kumar, 2018, PID Tracking Controller for Air-Breathing Hypersonic Vehicle][research_amrutha_harikumar_2018]
- [An and others, 2017, Barrier Lyapunov function-based adaptive control for hypersonic flight vehicles][research_an_xia_2017]
- [An and others, 2017, Sliding mode disturbance observer-enhanced adaptive control for the air-breathing hypersonic flight vehicle][research_an_wang_2017]
- [An and others, 2020, A framework of trajectory design and optimization for the hypersonic gliding vehicle][research_an_guo_2020]
- [An and others, 2021, Compound control of an uncertain hypersonic vehicle model][research_an_wang_2021]
- [AN and others, 2021, Key issues in hypersonic vehicle aerodynamic design][research_an_li_2021]
- [An and others, 2023, A Guidance and Control Scheme Based on NDO for Flexible Hypersonic Vehicle][research_an_yuan_2023]
- [An and others, 2025, Antinoise Aerodynamic Parameter Estimation Approach for Hypersonic Vehicle Using Dynamic Equation and Flight Data][research_an_wang_2025]
- [An and others, 2025, Six-Degree-of-Freedom Intelligent Control of Hypersonic Flight Vehicle][research_an_wang_2025_b]
- [An and others, 2026, Hybrid multi-constraint reentry trajectory planning Insights from convex optimization and predictor-corrector][research_an_huang_2026]
- [Anbuselvan and Reddy, 2017, Experimental Investigation of Magneto-Aerodynamic Interaction Studies in Hypersonic Flows][research_anbuselvan_reddy_2017]
- [Anderson and John D, 1991, Hypersonic Aerodynamics Fellowships][research_anderson_johnd_1991]
- [Anderson and Jr, 1988, Fellowships in Hypersonic Aerodynamics][research_anderson_jr_1988]
- [Anderson and Kinzel, 2023, Numerical Evaluation of Entry System Trajectory Control via Active Porosity Control of Transpiration Cooled Thermal Protection System][research_anderson_kinzel_2023]
- [ANDERSON and others, 1967, A simple guidance scheme for lifting body reentry vehicles][research_anderson_schultz_1967]
- [Anderson and others, 2021, Preliminary Design of the Sensor Pod of a Hypersonic Reentry Flight Testbed][research_anderson_loewenson_2021]
- [ANDERSON, 1968, A simplified analysis for re-entry stagnation point heat transfer from a viscous nongray radiating shock layer][research_andersonjr_1968]
- [ANDERSON, 1968, An equation for stagnation-point radiative heat transfer][research_anderson_1968_b]
- [ANDERSON, 1968, Nongray radiative stagnation point heat transfer][research_anderson_1968]
- [Anin, 2011, PROMPT GLOBAL STRIKE WEAPONS AND STRATEGIC INSTABILITY][research_anin_2011]
- [Antipova and others, 2012, Range finder and Doppler method for measuring flight parameters and aircraft position at glide path][research_antipova_chezganov_2012]
- [Appar and Kumar, 2021, Effect of Thermal Ablation at the Fluid-Solid Interface of a Hypersonic Reentry Vehicle in Rarefied Flow Regime][research_appar_kumar_2021]
- [Appar and Kumar, 2025, Reentry aerothermodynamic analysis of a high-speed vehicle with coupled ablating surface interface effects at rarefied conditions][research_appar_kumar_2025]
- [Appar and others, 2022, Conjugate flow-thermal analysis of a hypersonic reentry vehicle in the rarefied flow regime][research_appar_kumar_2022]
- [Appartaim and others, 2001, Turbulence in plasma-induced hypersonic drag reduction][research_appartaim_mezonlin_2001]
- [APPLEBY and ADAMS, 1991, Robust estimator design applied to the lateral dynamics of a hypersonic vehicle][research_appleby_adams_1991]
- [APPLETON, 1964, Aerodynamic pitching derivatives of a wedge in hypersonic flow][research_appleton_1964]
- [Aprovitola and others, 2019, Parametric Integral Soft Objects-based Procedure for Thermal Protection System Modeling of Reusable Launch Vehicle][research_aprovitola_iuspa_2019]
- [Arabshahi, 2021, Computational Simulations of the Aerothermal Environment of Hypersonic Flight Vehicles][research_arabshahi_2021]
- [Arai and Matsumoto, 2026, Convexification of Aerodynamic-Constraints for Reusable-Rockets Reentry-Burn Guidance][research_arai_matsumoto_2026]
- [Arai and others, 2008, The Rationale for a Hypersonic Air-breathing Vehicle Technology Maturization][research_arai_taguchi_2008]
- [Arai and others, 2019, Carbon fiber reinforced ultra-high temperature ceramic matrix composites A review][research_arai_inoue_2019]
- [Araujo Oliveira and others, 2023, Low-order Hypersonic Vehicle Trajectory Simulator][research_araujooliveira_barbosa_2023]
- [Archer and Sworder, 1977, A class of robust guidance laws for reentry guidance][research_archer_sworder_1977]
- [Archer and Sworder, 1979, Selection of the Guidance Variable for a Re-entry Vehicle][research_archer_sworder_1979]
- [ARDEMA, 1972, Minimum Weight Passive Insulation Requirements for Hypersonic Cruise Vehicles][research_ardema_1972]
- [Arjun, 2010, Analysis of Unconventional Wing Structures of a Hyper-X Hypersonic Flight Research Vehicle for the Mach 7 Mission][research_arjun_2010]
- [Aronov and Klyagin, 2021, On thermal protection system optimization criteria selection of high-speed aerial vehicle][research_aronov_klyagin_2021]
- [Arora and Ananthasayanam, 2003, Trajectory Design for a Reusable Launch Vehicle Demonstrator During Re-entry Phase][research_arora_ananthasayanam_2003]
- [Arora and others, 2024, Design Optimization and Aerothermodynamic Analysis Over a Supersonic Vehicle][research_arora_balaji_2024]
- [Arora, 2002, Reentry Trajectory Optimization Evolutionary Approach][research_arora_2002]
- [Ashford, 1965, Boost-Glide Vehicles for Long Range Transport][research_ashford_1965]
- [Ashwin Ganesh and John, 2018, Concentrated energy addition for active drag reduction in hypersonic flow regime][research_ashwinganesh_john_2018]
- [Asma and Van der Haegen, 2010, Footprint Analysis of the EXPERT Vehicle Winglet at Hypersonic Conditions][research_asma_vanderhaegen_2010]
- [Aso and others, 1992, Aerodynamic heating phenomenon in three dimensional shock wave/turbulent boundary layer interaction induced by sweptback fins in hypersonic flows][research_aso_nakao_1992]
- [Atesmen, 2023, Use of Ablation Materials As Heat Shield to Protect Spacecrafts Entering Earth's Atmosphere From Incoming Excessive Heat Loads][research_atesmen_2023]
- [Atkins, 2026, Configuration Aerodynamics Methodology for Conceptual Design of Hypersonic Vehicles][research_atkins_2026]
- [Au and others, 1969, Structural Synthesis of Composite Materials for Ablative Nozzle Extensions][research_au_scheyhing_1969]
- [Auman and Wilks, 2003, Supersonic and Hypersonic Minimum Drag for Bodies of Revolution][research_auman_wilks_2003]
- [Austin and Jacobs, 2003, Can trained monkeys design flight controllers for hypersonic vehicles?][research_austin_jacobs_2003]
- [Autenrieb and Fezans, 2024, Flight control design for a hypersonic waverider configuration A non-linear model following control approach][research_autenrieb_fezans_2024]
- [Autenrieb and Gruhn, 2025, An Iterative Control Allocation Algorithm for Hypersonic Glide Vehicles with Asymmetric Magnitude and Rate Limits][research_autenrieb_gruhn_2025]
- [Autenrieb and Gruhn, 2026, Control Allocation Algorithm for Hypersonic Glide Vehicles with Input Limitations][research_autenrieb_gruhn_2026]
- [Autenrieb and others, 2025, A Quasi-LPV Approach for Gain Scheduling Cascaded NDI-Based Controllers for Hypersonic Glide Vehicles][research_autenrieb_fezans_2025]
- [Autenrieb, 2023, Data fusion-based Incremental Nonlinear Model Following Control Design for a Hypersonic Waverider Configuration][research_autenrieb_2023]
- [Avallone and others, 2013, Image resection and heat transfer measurements by IR thermography in hypersonic flows][research_avallone_greco_2013]
- [AVALOS and CASTELLANOS, 2022, DAMAGE AND FAILURE ANALYSIS OF ULTRA-HIGH TEMPERATURE CERAMICS UHTCS SUBJECTED TO THERMAL SHOCK][research_avalos_castellanos_2022]
- [Azad, 2008, Security Guidance for Operating Systems and Terminal Services][research_azad_2008]
- [B, 2011, Aerodynamic Heating at Hypersonic Speed][research_b_2011]
- [BABINEAUX, 1966, Experimental assessment of the effect of large amounts of argon in aplanetary atmosphere on stagnation-point convective heating][research_babineaux_1966]
- [Bachman and others, 2021, Rotational Axisymmetric Method of Characteristics for the Development of Novel Waverider Geometries][research_bachman_hyde_2021]
- [Backman and others, 2024, Analysis of Test Specimen Temperature Gradients Incurred in Resistive Heating System Oxidation Studies of Ultra-High Temperature Ceramics][research_backman_graham_2024]
- [Backman and others, 2024, Composition dependence of oxidation resistance in high entropy ultra-high temperature ceramics][research_backman_gild_2024]
- [Bade, 1962, Stagnation-Point Heat Transfer in a High-Temperature Inert Gas][research_bade_1962]
- [Bade, 1975, Stagnation-point heat transfer correlation for ionized gases][research_bade_1975]
- [Bahambari and Khankalantary, 2023, An Improved Nonlinear Observer-Based Integrated Guidance and Control for Hypersonic Flight Vehicle with Angle Constraints][research_bahambari_khankalantary_2023]
- [Bahlman and others, 2013, Glide performance and aerodynamics of non-equilibrium glides in northern flying squirrels Glaucomys sabrinus][research_bahlman_swartz_2013]
- [Bahman Zohuri and others, 2019, New Weapon of Tomorrow's Battlefield Driven by Hypersonic Velocity][research_bahmanzohuri_patrickmcdaniel_2019]
- [Bai and others, 2011, Application of high temperature heat pipe in hypersonic vehicles thermal protection][research_bai_zhang_2011]
- [Bai and others, 2013, Adaptive Tracking Control of Hypersonic Re-entry Vehicle with Uncertain Parameters][research_bai_lian_2013]
- [Bai and others, 2014, Decoupling control of a hypersonic gliding vehicle based on NESO][research_bai_ren_2014]
- [Bai and others, 2015, Robust Skip earth entry guidance for a low L/D spacecraft][research_bai_guo_2015]
- [Bai and others, 2024, An Improved PSO Algorithm for Hypersonic Vehicle Cruise Trajectory Planning][research_bai_hu_2024]
- [Bai and others, 2025, Analytical 3D Trajectory Solution and Simulation Analysis for Reentry Glide Vehicles Based on the Perturbation Method][research_bai_huo_2025]
- [Bai Weijie and others, 2019, Design of a Novel Fractional Order Sliding Mode Controller for Hypersonic Vehicle Attitude Control][research_baiweijie_shengyongzhi_2019]
- [Baidya and others, 2018, Ramjet Nozzle Analysis for Transport Aircraft Configuration for Sustained Hypersonic Flight][research_baidya_pesyridis_2018]
- [Bailet and others, 2021, Passive Method to Measure Reentry Radiation in the Presence of Ablative Products][research_bailet_denis_2021]
- [Bailey, 1966, SPHERE DRAG MEASUREMENTS IN AN AEROBALLISTICS RANGE AT HIGH VELOCITIES AND LOW REYNOLDS NUMBERS][research_bailey_1966]
- [Bailey, 2020, Frequent and Reliable Launch for Small Satellites Rocket Lab's Electron Launch Vehicle and Photon Spacecraft][research_bailey_2020]
- [Bairstow and Barton, 2007, Orion Reentry Guidance with Extended Range Capability Using PredGuid][research_bairstow_barton_2007]
- [Bajpai and Jagadeesh, 2023, Investigation of Natural Transition on a Sharp Leading Edge Flat Plate in a Hypersonic Shock Tunnel][research_bajpai_jagadeesh_2023]
- [BAKER and KRAMER, 1979, Reentry vehicle nosetip design for minimum total heat transfer][research_baker_kramer_1979]
- [Baker and Kramer, 1982, Reentry Vehicle Nosetip Design for Minimum Total Heat Transfer][research_baker_kramer_1982]
- [Baker and others, 2004, Weapon System Optimization in the Integrated Hypersonic Aeromechanics Tool IHAT][research_baker_munson_2004]
- [Balakrishnan and Kurian, 2014, Material Thermal Degradation Under Reentry Aerodynamic Heating][research_balakrishnan_kurian_2014]
- [Balakrishnan and others, 1997, Hypersonic vehicle trajectory optimization and control][research_balakrishnan_shen_1997]
- [BALBIRNIE and others, 1975, Merging conventional and optimal control techniques for practical missile terminal guidance][research_balbirnie_sheporaitis_1975]
- [Balbo and Sciti, 2008, Spark plasma sintering and hot pressing of ZrB2-MoSi2 ultra-high-temperature ceramics][research_balbo_sciti_2008]
- [Balland and others, 2015, Thermal and Energy Management for Hypersonic Cruise Vehicles - Cycle Analysis][research_balland_fernandezvillace_2015]
- [Baluragi and others, 2011, Development of Functionally Graded Coating Material for Metallic Thermal Protection System of Reusable Launch Vehicle][research_baluragi_gupta_2011]
- [Banerjee and Nabi, 2017, Re-entry trajectory optimization for space shuttle using Sine-Cosine Algorithm][research_banerjee_nabi_2017]
- [Banerjee and Padhi, 2017, An Optimal Explicit Guidance Algorithm for Terminal Descent Phase of Lunar Soft Landing][research_banerjee_padhi_2017]
- [Banerjee, 2019, Flight Parameter Analysis of an L1 Adaptive Controller of a Hypersonic Glider][research_banerjee_2019]
- [Bano and others, 2026, High-Temperature Guided Wave Sensing for Thermal Protection System Structural Health Monitoring in Hypersonic Flight][research_bano_fraser_2026]
- [Bansal and others, 2012, Simulation of Hypersonic Flow and Radiation over a Mars Reentry Vehicle Using OpenFOAM][research_bansal_feldick_2012]
- [Bao and others, 2019, Reliability Increase of Base Heating Prediction and Thermal Protection Methodology for Launch Vehicle Upper-Stage][research_bao_ding_2019]
- [Bao and others, 2020, A Fast Calculation and Rendering Method for Infrared Characteristics of Hypersonic Vehicle][research_bao_li_2020]
- [BAO and others, 2021, Integrated method of guidance, control and morphing for hypersonic morphing vehicle in glide phase][research_bao_wang_2021]
- [Bao and others, 2023, Adaptive Optimal Control Method for Hypersonic Variable Sweep Vehicle][research_bao_zhang_2023]
- [Bao and others, 2023, Observer-based optimal control method combination with event-triggered strategy for hypersonic morphing vehicle][research_bao_wang_2023]
- [Bao and others, 2024, Research on Backstepping Linear Active Disturbance Rejection Control of Hypersonic Vehicle][research_bao_zhu_2024]
- [BARADELL and MCLELLAN, 1963, LATERAL-RANGE AND HYPERSONIC LIFT-DRAG-RATIO REQUIREMENTS FOR EFFICIENT FERRY SERVICE FROM A NEAR-EARTH MANNED SPACE STATION][research_baradell_mclellan_1963]
- [BARBER and COX, 1988, Hypersonic vehicle propulsion - A CFD application case study][research_barber_coxjr_1988]
- [Baron and Efrat, 1979, An Off Design Shock Capturing Finite Difference Approach for Caret Waverider Configurations][research_baron_efrat_1979]
- [Barr and others, 2026, Hypersonic Glide Vehicle Trajectory Forecasting via Transformer and Physics-Informed GBDT Models][research_barr_figueroa_2026]
- [Barrett, 2025, HYPERSONIC, SUPPRESSOR-COMPATIBLE SMALL ARMS AND HYPERSONIC FLIGHT-SAFE AERIAL GUNNERY AMMUNITION][research_barrett_2025]
- [Bartusiak and others, 2022, A Stochastic Grammar Approach to Predict Flight Phases of a Hypersonic Glide Vehicle][research_bartusiak_hao_2022]
- [Bartusiak and others, 2023, Transfer Learning for Hypersonic Vehicle Trajectory Prediction][research_bartusiak_jacobs_2023]
- [Bartusiak and others, 2024, Predicting Hypersonic Glide Vehicle Behavior With Stochastic Grammars][research_bartusiak_jacobs_2024]
- [Barz, 2026, Multifidelity Fluid-Structure Coupled Shape Optimization of a Hypersonic Glide Vehicle][research_barz_2026]
- [Bastos Jr, 2019, A stable reentry trajectory for flexible manipulators][research_bastosjr_2019]
- [Battistini and Menegaz, 2017, Interacting multiple model unscented filter for tracking a ballistic missile during its boost phase][research_battistini_menegaz_2017]
- [BAUER and KUMMER, 1965, DEVELOPMENT AND PERFORMANCE OF THE GEMlNI ABLATIVE HEAT SHIELD][research_bauer_kummer_1965]
- [BAUER and KUMMER, 1966, Development and performance of the Gemini ablative heat shield][research_bauer_kummer_1966]
- [Baxter and Arthur, 1965, Generalised Single Component Insulation Requirement for the Hypersonic Glide][research_baxter_arthur_1965]
- [Bayramov and Gasanov, 2020, COMPUTER MODELLING OF A VERY HEAT RESISTANT Hf6C3N2 FOR COVER OF HYPERSONIC FLIGHT VEHICLES][research_bayramov_gasanov_2020]
- [Baysal and Luo, 1999, Dynamic Unstructured Method for Relative Motion of Multibody Configuration at Hypersonic Speeds][research_baysal_luo_1999]
- [Beall and others, 2017, Rapid prototyping of GNC algorithms for gliding reentry vehicles][research_beall_henderson_2017]
- [Beauthier and others, 2014, Hypersonic cryogenic tank design using mixed-variable surrogate-based optimization][research_beauthier_mahajan_2014]
- [Bebyakov, 2013, Optimal control of the angle of attack of a hypersonic flight vehicle][research_bebyakov_2013]
- [Becker and others, 1962, Aerodynamics of Trajectory Control for Re-Entry at Escape Speed][research_becker_baradell_1962]
- [BECKER and others, 1973, Velocity distribution in hypersonic helium flow near the leading edge of a flat plate][research_becker_robben_1973]
- [BECKER, 1964, STUDIES OF HIGH LIFT/DRAG RATIO HYPERSONIC CONFIGURATIONS][research_becker_1964]
- [Bedarev and Fedorova, 2001, Numerical Simulation of Axisymmetric Super- and Hypersonic Separated Flows in Vicinity of Cylinder-Flare Configuration][research_bedarev_fedorova_2001]
- [Bedrov and others, 1966, Certain Nonlinear Laws in the Control of a Winged Glide Vehicle in Transition from a Circular Orbit to a Takeoff and Landing Strip][research_bedrov_vadichin_1966]
- [Beers and others, 2013, Small Launch Vehicle Concept Development for Affordable Multi-Stage Inline Configurations][research_beers_waters_2013]
- [Bell and Hung, 1962, Implications of Re-Entry Trajectory Control on Vehicle Design Criteria at Superorbital Speeds][research_bell_hung_1962]
- [Bell, 1965, A CLOSED-FORM SOLUTION TO LIFTING REENTRY][research_bell_1965]
- [Belov and others, 1999, An experience in the investigation of a radio communications system for a reentry vehicle on the plasma flight trajectory portion][research_belov_borovoy_1999]
- [Benay, 2003, Shock Wave Transitional Boundary Layer Interaction in Hypersonic Flow][research_benay_2003]
- [BENDOR, 1963, RAREFIED VISCOUS FLOW NEAR A SHARP LEADING EDGE][research_bendor_1963]
- [Benson and others, 2025, CubeSat with VSWIR Imager for Detection and Tracking of Hypersonic Vehicles][research_benson_wells_2025]
- [BENTON, 1990, Design synthesis of Shuttle-class hypersonic SSTO vehicle][research_benton_1990]
- [Berens and Bissinger, 1998, Forebody precompression performance of hypersonic flight test vehicles][research_berens_bissinger_1998]
- [Beresh, 2022, Ground Testing of Unsteady Aerodynamic Environments in Hypersonic Flight][research_beresh_2022]
- [Bergen and others, 2024, Simulations of Slender Hypersonic Geometries with Blunt Leading Edges Using rhoCentralFoam][research_bergen_chan_2024]
- [Berger and others, 2008, Aerothermodynamic Testing and Boundary-Layer Trip Sizing of the HIFiRE Flight 1 Vehicle][research_berger_greene_2008]
- [Berger and others, 2009, Erratum on "Aerothermodynamic Testing and Boundary-Layer Trip Sizing of the HIFire Flight 1 Vehicle"][research_berger_greene_2009]
- [Berger, 2009, Aerothermodynamic Testing of the Crew Exploration Vehicle at Mach 6 and Mach 10][research_berger_2009]
- [Berlin and others, 1989, Analysis of the expansion-fan flowfield for holes in a hypersonic configuration][research_berlin_tedeschi_1989]
- [BERNHART, 1995, Materials requirements for the thermal protection system of Hermes and related testing requirements][research_bernhart_1995]
- [Berry and Berger, 2015, NASA Langley Experimental Aerothermodynamic Contributions to Slender and Winged Hypersonic Vehicles][research_berry_berger_2015]
- [BERRY and others, 1993, Experiences in fabrication of a waverider model for wind tunnel testing][research_berry_kammeyer_1993]
- [BERTELRUD and others, 1992, Plans for in-flight measurement of hypersonic crossflow transition on the Pegasus launch vehicle][research_bertelrud_kolodziej_1992]
- [Berthelot and others, 2026, Material Selection and Structural Analysis of an Undergraduate-Designed Unpowered Hypersonic Glide Vehicle][research_berthelot_craft_2026]
- [Bertin and Cummings, 2006, CRITICAL HYPERSONIC AEROTHERMODYNAMIC PHENOMENA][research_bertin_cummings_2006]
- [Bettis and Hosder, 2010, Quantification of Uncertainty in Aerodynamic Heating of a Reentry Vehicle due to Uncertain Wall and Freestream Conditions][research_bettis_hosder_2010]
- [Bhagwandin and Martin, 2023, Wall-Resolved LES of Mach 6 BoLT-2 Hypersonic Vehicle][research_bhagwandin_martin_2023]
- [Bhat and Lind, 2009, Control-oriented analysis of thermal gradients for a hypersonic vehicle][research_bhat_lind_2009]
- [Bhatta and Leonard, 2004, A Lyapunov function for vehicles with lift and drag stability of gliding][research_bhatta_leonard_2004]
- [Bhungalia and others, 2000, Integrated Aerodynamic and Geometric Modeling for Hypersonic Vehicle Design][research_bhungalia_zweber_2000]
- [BHUTTA and LEWIS, 1992, Low-to-high altitude predictions of three-dimensional ablative reentry flowfields][research_bhutta_lewis_1992]
- [Bianchi and others, 2011, Aerothermodynamic Analysis of Reentry Flows with Coupled Ablation][research_bianchi_nasuti_2011]
- [Bibeau and Rubinstein, 2000, Trajectory optimization for a fixed-trim reentry vehicle using direct collocation and nonlinear programming][research_bibeau_rubinstein_2000]
- [Bibin and Vinayak, 2013, Investigation of Energy Deposition Technique for Drag Reduction at Hypersonic Speeds][research_bibin_vinayak_2013]
- [Bikdash and others, 1999, Fuzzy guidance of the shuttle orbiter during atmospheric reentry][research_bikdash_sartor_1999]
- [Bilchenko and Bilchenko, 2017, On the bijectivity of controls pairs and pairs of heat and mass transfer local parameters in the hypersonic flow stagnation point][research_bilchenko_bilchenko_2017]
- [Bille and Lorenz, 2001, Requirements for a Conventional Prompt Global Strike Capability][research_bille_lorenz_2001]
- [Bin and Hongxin, 2006, Adaptive Control Based on Characteristic Model for a Hypersonic Flight Vehicle][research_bin_hongxin_2006]
- [Bin Jiang and Qi, 2017, Fault-tolerant guidance for hypersonic vehicle based on predictor-corrector strategy][research_binjiang_qi_2017]
- [BIRD, 1966, Aerodynamic properties of some simple bodies in the hypersonic transition regime][research_bird_1966]
- [BISHOP and DICRISTINA, 1967, A PREDICTION TECHNIQUE FOR ABLATIVE MATERIAL PERFORMANCE UNDER HIGH SHEAR REENTRY CONDITIONS][research_bishop_dicristina_1967]
- [Bishop, 2013, Bayesian Estimation for Tracking of Spiraling Reentry Vehicles][research_bishop_2013]
- [Bissinger and others, 1998, Improvement of forebody/inlet integration for hypersonic vehicle][research_bissinger_blagoveshchensky_1998]
- [Bissinger and Schmitz, 1996, Design and testing of 2-D hypersonic intakes][research_bissinger_schmitz_1996]
- [BLANKSON and HAGSETH, 1993, Propulsion/airframe integration issues for waverider aircraft][research_blankson_hagseth_1993]
- [Blankson and others, 1998, Subsonic experiments using the LoFlyte hypersonic waverider vehicle][research_blankson_lewis_1998]
- [Blankson, 1992, Air-Breathing Hypersonic Cruise Prospects for Mach 4-7 Waverider Aircraft][research_blankson_1992]
- [Blankson, 1994, Air-Breathing Hypersonic Cruise Prospects for Mach 4-7 Waverider Aircraft][research_blankson_1994]
- [Blaschke and Hummel, 1999, Experimental and numerical investigations on a waverider configuration in incompressible flow][research_blaschke_hummel_1999]
- [Blevins and others, 1993, Thermoacoustic loads and fatigue of hypersonic vehicle skin panels][research_blevins_holehouse_1993]
- [Bliamis and others, 2023, Implementation of various-fidelity methods for viscous effects modeling on the design of a waverider][research_bliamis_menelaou_2023]
- [BLOCK and others, 1990, The challenges of hypersonic-vehicle guidance, navigation, and control][research_block_gesslerjr_1990]
- [BLORE and MUSAL, 1965, Radar absorption effect in hypersonic ballistic ranges][research_blore_musal_1965]
- [Blosser and others, 1994, Wing leading-edge design concepts for airbreathing hypersonic waveriders][research_blosser_blankson_1994]
- [Blosser and others, 1995, Wing leading-edge design concepts for airbreathing hypersonic waveriders][research_blosser_blankson_1995]
- [Blum, 1969, LONG RANGE TRAJECTORY PREDICTION ERRORS FOR LEAST SQUARES SMOOTHING][research_blum_1969]
- [Blum, 1971, Long-Range Trajectory Prediction Errors for Least-Squares Smoothing][research_blum_1971]
- [Blum, 2006, Low Temperature Reactivities of Ultra-High Temperature Ceramics Hf-X System][research_blum_2006]
- [Bo and others, 2025, Aerodynamic design of sink nozzle providing supersonic toroidal cooling film for hypersonic optical window][research_bo_xiaoge_2025]
- [Boehrk and others, 2012, Thermal Testing of the Sharp Leading Edge of SHEFEX II][research_boehrk_dittert_2012]
- [BOEING SCIENTIFIC RESEARCH LABS SEATTLE WA, 1963, SLENDER, AXISYMMETRIC POWER BODIES HAVING MINIMUM ZERO-LIFT DRAG IN HYPERSONIC FLOW][research_boeingscientificresearchlabsseattlewa_1963]
- [BOENSCH and others, 1968, Structural design considerations for cryogenic fueled hypersonic cruise vehicles][research_boensch_goesch_1968]
- [Bogart and others, 1981, Thermal Protection of Commercial Dry Suit Diving Systems][research_bogart_breckenridge_1981]
- [BOGDONOFF, 1968, Studies of the leading edge effect on the rarefied hypersonic flow over a flat plate][research_bogdonoff_1968]
- [Bogdonoff, 1999, Hypersonic Flight Vehicles Perspective and Prognosis][research_bogdonoff_1999]
- [BOGUCZ and others, 1988, Unsteady stagnation-point heat transfer due to the motion of freestream vortices][research_bogucz_dirik_1988]
- [Bohn, 1967, Hybrid, six-degree-of-freedom, man-and-the-loop, simulation of a lifting reentry vehicle][research_bohn_1967]
- [Boland and others, 2023, Dust Erosion Correlation for Mars Entry Vehicles and Hypersonic Cruise Vehicle Leading-Edges][research_boland_hinkle_2023]
- [Bolender and Doman, 2005, A Non-Linear Model for the Longitudinal Dynamics of a Hypersonic Air-breathing Vehicle][research_bolender_doman_2005]
- [Bolender and Doman, 2005, Flight Path Angle Dynamics of Air-Breathing Hypersonic Vehicles][research_bolender_doman_2005_b]
- [Bolender and Doman, 2006, Modeling Unsteady Heating Effects on the Structural Dynamics of a Hypersonic Vehicle][research_bolender_doman_2006]
- [Bolender and others, 2009, Flight Dynamics of a Hypersonic Vehicle During Inlet Un-start][research_bolender_wilkin_2009]
- [Bollino and others, 2006, Optimal Guidance Command Generation and Tracking for Reusable Launch Vehicle Reentry][research_bollino_oppenheimer_2006]
- [Bollino and others, 2006, Optimal Nonlinear Feedback Guidance for Reentry Vehicles][research_bollino_ross_2006]
- [Bollino and Ross, 2007, A pseudospectral feedback method for real-time optimal guidance of reentry vehicles][research_bollino_ross_2007]
- [BOMAN and ELIAS, 1990, Tests on a sodium/Hastelloy X wing leading edge heat pipe for hypersonic vehicles][research_boman_elias_1990]
- [Bonavita and others, 2026, Direct Collocation Methods for Boost-Glide Vehicle Trajectory Optimization with Newtonian Aerodynamic Model][research_bonavita_zollars_2026]
- [Bond and others, 2000, Ground Effect Characteristics of a Two-Dimensional Hypersonic Configuration][research_bond_morris_2000]
- [Bond and others, 2001, Exhaust Ducting Effects on Takeoff Lift Loss of Two-Dimensional Hypersonic Configuration][research_bond_morris_2001]
- [Bond and others, 2006, Ground Effect Characteristics and Centerline Pressure Distributions for a Hypersonic Configuration][research_bond_morris_2006]
- [Bonelli and others, 2011, Preliminary design of a hypersonic air-breathing vehicle][research_bonelli_cutrone_2011]
- [Bonifacio and others, 2006, SPREAD a Scramjet PREliminary Aerothermodynamic Design Code][research_bonifacio_borreca_2006]
- [Bonin and others, 2017, Simulations of stagnation point radiative heating rates and spectral analysis of entry vehicles][research_bonin_kliche_2017]
- [Boppe and Davis, 1989, Hypersonic Forebody Lift-Induced Drag *][research_boppe_davis_1989]
- [Borg and others, 2025, HIFLIER Hypersonic Flight Experiment Design, Analysis, and Ground Test][research_borg_adamczak_2025]
- [Borovoj and Kubyshina, 1993, Hypersonic heat transfer on the upper wing surface fins][research_borovoj_kubyshina_1993]
- [Borovoy and others, 2015, Influence of leading edge bluntness on hypersonic flow in a generic internal-compression inlet][research_borovoy_egorov_2015]
- [Borrelli and others, 1998, Aerodynamic devices efficiency for the FESTIP hypersonic vehicle concepts][research_borrelli_marini_1998]
- [Bouchez and others, 1998, Hydrocarbon fueled scramjets for hypersonic vehicles][research_bouchez_montazel_1998]
- [Boudali and others, 2019, Unified dynamic and geometrical vehicle guidance strategy to cope with the discontinuous reference trajectory][research_boudali_orjuela_2019]
- [Bowcutt and Haney, 1995, Scramjet flight testing to support hypersonic research vehicle aeropropulsion performance][research_bowcutt_haney_1995]
- [BOWCUTT, 1992, Hypersonic aircraft optimization including aerodynamic, propulsion, and trim effects][research_bowcutt_1992]
- [Bowcutt, 2018, Physics Drivers of Hypersonic Vehicle Design][research_bowcutt_2018]
- [Bowden and Brown, 2023, Numerical Modeling and GNSS Observations of Ionospheric Depletions Due To a Small-Lift Launch Vehicle][research_bowden_brown_2023]
- [Bowersox and Fan, 2000, Investigation of Combined Low-Angled Jets and Variable Wall Geometry for Hypersonic Aerodynamic Control][research_bowersox_fan_2000]
- [Bowles and others, 1998, Optimizing hypersonic sharp body concepts from a thermal protection system perspective][research_bowles_roberts_1998]
- [Boyd and Padilla, 2003, Simulation of Sharp Leading Edge Aerothermodynamics][research_boyd_padilla_2003]
- [Boyer, 1965, DESIGN, INSTRUMENTATION AND PERFORMANCE OF THE UTIAS 4-IN.X 7-IN. HYPERSONIC SHOCK TUBE][research_boyer_1965]
- [Boylan, 1965, LIFT, DRAG, AND STATIC STABILITY OF A BLUNT CONICAL MODEL IN HYPERSONIC RAREFIED FLOW][research_boylan_1965]
- [BRADLEY and others, 1981, Comparison of forward fuselage to Space Shuttle Orbiter flight pressure data to wind tunnel and analytical results in the hypersonic Machnumber range][research_bradley_siemersiii_1981]
- [BRADY and LEVENSTEINS, 1964, Hypersonic drag, stability, and wake data for cones and spheres][research_brady_levensteins_1964]
- [Brandis and Johnston, 2014, Characterization of Stagnation-Point Heat Flux for Earth Entry][research_brandis_johnston_2014]
- [BRAUCKMANN, 1986, Hypersonic aerodynamic characteristics of a candidate entry researchvehicle][research_brauckmann_1986]
- [Brazhko and others, 2020, EXPERIMENTAL INVESTIGATION OF AEROTHERMODYNAMIC CHARACTERISTICS OF THE EXOMARS PROJECT LANDER AT HYPERSONIC VELOCITIES][research_brazhko_davletkildeev_2020]
- [Breeza Paulose and others, 2016, Linear Control of Air-Breathing Hypersonic Vehicle][research_breezapaulose_jisjose_2016]
- [Breitner and Pesch, 1994, Reentry Trajectory Optimization under Atmospheric Uncertainty as a Differential Game][research_breitner_pesch_1994]
- [Breitsamter and others, 2001, Wind tunnel tests for separation dynamics modeling of a two-stage hypersonic vehicle][research_breitsamter_laschka_2001]
- [Brinda and others, 2006, Trajectory Optimization and Guidance of an Air Breathing Hypersonic Vehicle][research_brinda_dasgupta_2006]
- [Brindha and others, 2026, A comprehensive review of waverider configurations Advances in design, performance, and applications across wide-speed ranges][research_brindha_das_2026]
- [Britcher and Landman, 2024, Hypersonic wind tunnel design][research_britcher_landman_2024]
- [BROADAWAY, 1984, Aerodynamics of a simple cone-derived waverider][research_broadaway_1984]
- [Brociek and others, 2023, Reconstruction of aerothermal heating for the thermal protection system of a reusable launch vehicle][research_brociek_hetmaniok_2023]
- [BROGLIO, 1961, ON GUIDANCE AND LANDING ACCURACY REQUIREMENTS IN RE-ENTRY TRAJECTORIES][research_broglio_1961]
- [Broglio, 1962, On Guidance and Landing Accuracy Requirements in Re-Entry Trajectories][research_broglio_1962]
- [Brown and Chou, 2026, Design and Trajectory Optimization of a Shape-Morphing Aeroshell for Skip-Entry Orbital Inclination Change][research_brown_chou_2026]
- [Brown and others, 2009, Ku-band retrodirective radar for ballistic projectile detection and tracking][research_brown_brown_2009]
- [BROWNING, 1993, A responsive launch vehicle should trade weight for cost and operability][research_browning_1993]
- [Brune and others, 2015, Uncertainty Analysis of Fluid-Structure Interaction of a Deformable Hypersonic Inflatable Aerodynamic Decelerator][research_brune_hosder_2015]
- [Brune and others, 2016, Uncertainty Analysis of Thermal Protection System Response of a Hypersonic Inflatable Aerodynamic Decelerator][research_brune_hosder_2016]
- [Brune and others, 2017, A Review of Uncertainty Analysis for Hypersonic Inflatable Aerodynamic Decelerator Design][research_brune_west_2017]
- [Brune and others, 2017, Thermal Protection System Response Uncertainty of a Hypersonic Inflatable Aerodynamic Decelerator][research_brune_hosder_2017]
- [Brunner and Lu, 2007, Skip Entry Trajectory Planning and Guidance][research_brunner_lu_2007]
- [Brunner and Lu, 2008, Skip Entry Trajectory Planning and Guidance][research_brunner_lu_2008]
- [Brunner and Lu, 2010, Comparison of Numerical Predictor-Corrector and Apollo Skip Entry Guidance Algorithms][research_brunner_lu_2010]
- [BRYSON and DENHAM, 1962, Guidance Scheme for Supercircular Re-Entry of a Lifting Vehicle][research_bryson_denham_1962]
- [Bryson and others, 2018, Approach for Understanding Range Extension of Gliding Indirect Fire Munitions][research_bryson_vasile_2018]
- [Bu and Bao, 2008, Mechanical Properties Evaluation of Ultra-High Temperature Ceramics][research_bu_bao_2008]
- [Bu and Jiang, 2023, Fragility-Free Prescribed Performance Control Without Approximation Applied to Waverider Aerocraft][research_bu_jiang_2023]
- [Bu and Ma, 2023, Adaptive critic design for enhanced control of waverider vehicles with nonaffine nonlinearities][research_bu_ma_2023]
- [Bu and others, 2015, Nonsingular direct neural control of air-breathing hypersonic vehicle via back-stepping][research_bu_wu_2015]
- [Bu and others, 2019, Robust tracking control of hypersonic flight vehicles A continuous model-free control approach][research_bu_lei_2019]
- [Bu and others, 2022, A Simplified Finite-Time Fuzzy Neural Controller With Prescribed Performance Applied to Waverider Aircraft][research_bu_qi_2022]
- [Bu and others, 2022, Non-fragile tracking control of constrained Waverider Vehicles with readjusting prescribed performance][research_bu_jiang_2022]
- [Bu and others, 2022, Nonfragile Quantitative Prescribed Performance Control of Waverider Vehicles With Actuator Saturation][research_bu_jiang_2022_b]
- [Bu and others, 2023, Flight Control of Waverider Vehicles with Fragility-avoidance Prescribed Performance][research_bu_hua_2023]
- [Bu and others, 2023, Fuzzy Neural Pseudo Control With Prescribed Performance for Waverider Vehicles A Fragility-Avoidance Approach][research_bu_lv_2023]
- [Bu and others, 2023, Low-Complexity Fuzzy Neural Control of Constrained Waverider Vehicles via Fragility-Free Prescribed Performance Approach][research_bu_jiang_2023_b]
- [Bu and others, 2023, Performance Guaranteed Finite-Time Non-Affine Control of Waverider Vehicles Without Function-Approximation][research_bu_jiang_2023_c]
- [Buchanan and Crosby, 1983, Captive Trajectory System Test Planning Information for AEDC Supersonic Wind Tunnel A and Hypersonic Wind Tunnels B and C][research_buchanan_crosby_1983]
- [Bukva and others, 2020, Towards Modelling of Thermal Protection Systems with Transpiration Cooling][research_bukva_christopher_2020]
- [Bulirsch and Chudej, 1992, Guidance and Trajectory Optimization Under State Constraints - Applied to a Sanger-Type Vehicle][research_bulirsch_chudej_1992]
- [Bulirsch and Chudej, 1993, GUIDANCE AND TRAJECTORY OPTIMIZATION UNDER STATE CONSTRAINTS - APPLIED TO A SANGER - TYPE VEHICLE][research_bulirsch_chudej_1993]
- [Burchfield and Bontrager, 1966, PRESSURE AND HEAT-TRANSFER MEASUREMENTS ON A SLOTTED LEADING EDGE IN HYPERSONIC FLOW][research_burchfield_bontrager_1966]
- [Burdun and Parfentyev, 1998, Analysis and optimization of hypersonic maneuvering of a transatmospheric vehicle under uncertainty using fuzzy trees][research_burdun_parfentyev_1998]
- [Burke and Rumpfkeil, 2025, Multi-Fidelity Surrogate Modeling of a Generic Hypersonic Vehicle][research_burke_rumpfkeil_2025]
- [BURNETT and LEWIS, 1993, A re-evaluation of the waverider design process][research_burnett_lewis_1993]
- [Burnett, 1993, An innovative aerothermodynamic research vehicle][research_burnett_1993]
- [Burns, 2020, Progress at Sandia for the DoD Common Hypersonic Boost Glide Vehicle and Autonomy for Hypersonics][research_burns_2020]
- [Burt and others, 2012, Automated Aerodynamic Optimization for Lifting Hypersonic Vehicles at High Altitude][research_burt_josyula_2012]
- [Buschek and Calise, 1997, Uncertainty Modeling and Fixed-Order Controller Design for a Hypersonic Vehicle Model][research_buschek_calise_1997]
- [BUSING, 1964, THE EFFECT OF SURFACE CATALYTIC EFFICIENCY ON STAGNATION POINT HEAT TRANSFER][research_busing_1964]
- [BUTLER and others, 1991, Ballistic range tests of store separation at supersonic to hypersonic speeds][research_butler_king_1991]
- [Butler and others, 2016, Characterization of Candidate Materials for Remote Recession Measurements of Ablative Heat Shield Materials][research_butler_winter_2016]
- [Butler and others, 2022, Pre- and Post-Flight Hypersonic Glide Vehicle Surface Roughness Measurements][research_butler_benitez_2022]
- [Butler and others, 2023, Pre- and Post-Flight Surface Roughness Measurements on the X-23 Hypersonic Glide Vehicle][research_butler_benitez_2023]
- [BUTSKO, 1966, Prediction of the subsonic base drag of hypersonic re-entry vehicles][research_butsko_1966]
- [Butt and others, 2010, Robust adaptive Dynamic Surface Control of a hypersonic flight vehicle][research_butt_yan_2010]
- [Butt and others, 2011, Adaptive dynamic surface control of a hypersonic flight vehicle with improved tracking][research_butt_yan_2011]
- [Butt and others, 2011, Adaptive Dynamic Surface Control of a Hypersonic Flight Vehicle with Magnitude, Rate and Bandwidth Constraints][research_butt_yan_2011_b]
- [Butt and others, 2013, Adaptive integral dynamic surface control of a hypersonic flight vehicle][research_butt_yan_2013]
- [Butt, 2013, Observer Based Dynamic Surface Control of A Hypersonic Flight Vehicle][research_butt_2013]
- [Buyanbaatar and others, 2022, Aerodynamic Study of Cone-Derived Waverider as Supersonic Transport][research_buyanbaatar_ishikawa_2022]
- [Byczkowski and Rao, 2023, Correction Reusable Entry Vehicle Trajectory Optimization Using Multiple-Domain Radau Collocation][research_byczkowski_rao_2023_b]
- [Byczkowski and Rao, 2023, Reusable Entry Vehicle Trajectory Optimization Using Multiple-Domain Radau Collocation][research_byczkowski_rao_2023]
- [Byczkowski and Rao, 2024, Constrained Hypersonic Reentry Trajectory Optimization Using A Multiple-Domain Direct Collocation Method][research_byczkowski_rao_2024]
- [Byczkowski and Rao, 2026, Numerical Optimization Study of a Constrained Hypersonic Reentry Vehicle][research_byczkowski_rao_2026]
- [Bykerk and others, 2020, Low speed lateral-directional aerodynamic and static stability analysis of a hypersonic waverider][research_bykerk_verstraete_2020]
- [Bykerk and others, 2020, Low speed lateral-directional dynamic stability analysis of a hypersonic waverider using unsteady Reynolds averaged Navier Stokes forced oscillation simulations][research_bykerk_verstraete_2020_d]
- [Bykerk and others, 2020, Low speed longitudinal aerodynamic, static stability and performance analysis of a hypersonic waverider][research_bykerk_verstraete_2020_b]
- [Bykerk and others, 2020, Low speed longitudinal dynamic stability analysis of a hypersonic waverider using unsteady Reynolds averaged Navier Stokes forced oscillation simulations][research_bykerk_verstraete_2020_c]
- [Byrne and others, 1996, A moving mass trim control system for reentry vehicle guidance][research_byrne_sturgis_1996]
- [Byrom and Allen, 1994, THERMOVISCOPLASTIC RESPONSE OF HYPERSONIC LEADING EDGE STRUCTURES SUBJECTED TO INTENSE LOCAL HEATING][research_byrom_allen_1994]
- [Böhrk and others, 2014, Sharp Leading Edge at Hypersonic Flight Modeling and Flight Measurement][research_bohrk_dittert_2014]
- [Błachowicz, 2003, The scattering of light on sound waves in the hypersonic range of frequencies the directional sensitivity of Brillouin light scattering][research_blachowicz_2003]
- [Cabrera and West, 2026, Pioneer Venus Large Probe Stagnation Point Entry Heating with Coupled Ablation][research_cabrera_west_2026]
- [Cai and others, 2010, Tracking control for air-breathing hypersonic cruise vehicle based on tangent linearization approach][research_cai_duan_2010]
- [Cai and others, 2013, Controller Design Based on Linear Matrix Inequalities for Hypersonic Reentry Vehicle Driven by Reaction Control System][research_cai_jianmei_2013]
- [Cai and others, 2013, Flight control system design for hypersonic reentry vehicle based on LFT-LPV method][research_cai_song_2013]
- [Cai and others, 2014, Control system design for hypersonic reentry vehicle driven by aerosurfaces and reaction control system][research_cai_song_2014]
- [CAI and others, 2024, Research Progress of High-entropy Carbide Ultra-high Temperature Ceramics][research_cai_ni_2024]
- [Cai and others, 2026, Improved two-phase sequential convex programming for reentry trajectory optimization][research_cai_wei_2026]
- [Cai and Wu, 2011, Multiobjective fault detection and isolation for flexible air-breathing hypersonic vehicle][research_cai_wu_2011]
- [Cai and Zhuang, 2025, Hypersonic glide vehicle trajectory prediction based on frequency enhanced channel attention and light sampling-oriented MLP network][research_cai_zhuang_2025]
- [Caledonia and Krech, 1994, Ultraviolet Emissions Occurring About Hypersonic Vehicles in Rarefied Flows][research_caledonia_krech_1994]
- [CALISE and BAE, 1987, Optimal heading change with minimum energy loss for a hypersonic gliding vehicle][research_calise_bae_1987]
- [Calise and Bae, 1988, Optimal Reentry Guidance for Aeroassisted Orbit Transfer Vehicles][research_calise_bae_1988]
- [Calise and Bae, 1990, Optimal heading change with minimum energy loss for a hypersonic gliding vehicle][research_calise_bae_1990]
- [Callsen and others, 2024, Analysis of sonic boom propagation and population disturbance of hypersonic vehicle trajectories][research_callsen_wilken_2024]
- [Campbell and others, 1996, Aerothermodynamic environment definition for an X-23/X-24A derived assured crew return vehicle][research_campbell_caram_1996]
- [Candler and Leyva, 2022, Computational Fluid Dynamics Analysis of the Infrared Emission From a Generic Hypersonic Glide Vehicle][research_candler_leyva_2022]
- [Candler and others, 2015, CFD Methods for Hypersonic Flows and Aerothermodynamics][research_candler_subbareddy_2015]
- [Cangelosi and others, 2024, Simultaneous Design and Trajectory Optimization for Boosted Hypersonic Glide Vehicles][research_cangelosi_heinkenschloss_2024]
- [Cantó and others, 2011, Gravitational drag on a point mass in hypersonic motion through a gaseous medium][research_canto_raga_2011]
- [Cao and others, 2007, Conceptual Design and Numerical Simulations of Hypersonic Waverider Vehicle][research_cao_zhang_2007]
- [CAO and others, 2026, Flow structure evolution and aerodynamic scaling of supersonic retropropulsion during hypersonic reentry][research_cao_dong_2026]
- [Cao and Zhang, 2015, Aerodynamic configuration optimization for hypersonic gliding vehicle based on improved hybrid multi-objective PSO algorithm][research_cao_zhang_2015]
- [Caogen and others, 2008, A study on metallic thermal protection system panel for Reusable Launch Vehicle][research_caogen_hongjun_2008]
- [CAPRIOTTI, 1987, Viscous optimized hypersonic waveriders][research_capriotti_1987]
- [Carbonaro, 1993, Aerodynamic Force Measurements in the VKI Longshot Hypersonic Facility][research_carbonaro_1993]
- [Cardone, 2007, IR heat transfer measurements in hypersonic plasma flows][research_cardone_2007]
- [Carlomagno and others, 1993, Hypersonic Aerodynamics Research with an Infrared Imaging System][research_carlomagno_luca_1993]
- [Carlson, 1999, Aerothermodynamic Analyses of Hypersonic, Blunt-Body Flows][research_carlson_1999]
- [Carman and J. B, 1966, INSULATIVE PERFORMANCE OF SELECTED ABLATIVE MATERIALS IN A LOW ENTHALPY HYPERSONIC AIRSTREAM][research_carman_jb_1966]
- [Carney, 2018, 5.10 Ultra-High Temperature Ceramic-Based Composites][research_carney_2018]
- [Carpman and others, 2025, Corrosion of Ultra-High Temperature Ceramics in Molten Chloride Salt][research_carpman_kelly_2025]
- [Carr and Lagimoniere, 2013, A Range Safety Footprint Analysis for the Dream Chaser Engineering Test Article Using Trajectory Optimization][research_carr_lagimoniere_2013]
- [Carr and others, 2012, Trajectory Analysis Program for Determining Range Safety Considerations for a Reusable Launch Vehicle Using Multiple-Phase Pseudospectral Optimization][research_carr_rexius_2012]
- [CARR, 1966, Design and operation of a high Mach number high Reynolds number hypersonic facility][research_carr_1966]
- [Carroll and Brandis, 2023, Stagnation Point Convective Heating Correlations for Entry into H 2 /He Atmospheres][research_carroll_brandis_2023]
- [Carson and others, 2006, Optimal nonlinear guidance with inner-loop feedback for hypersonic re-entry][research_carson_epstein_2006]
- [Carter and others, 2005, Hypersonic Engineering Aerothermodynamic Trajectory Tool Kit HEAT-TK . Delivery Order 0009 Software User's Manual][research_carter_kuruvila_2005]
- [CARTER, 1965, Reference trajectory re-entry guidance without pre-launch data storage][research_carter_1965]
- [Cas and others, 2026, Conservative Numerical Modeling of an Ablative Charring Heat Shield Under Deformations Validated Through Arc-Jet Tests][research_cas_baranger_2026]
- [Cassabaum and others, 2000, Application of local discriminant bases discrimination algorithm for theater missile defense][research_cassabaum_schmitt_2000]
- [Cassanto and others, 1977, Flight Experiment Demonstrating Existence of Re-entry Vehicle Nosetip Transient Shock Waves][research_cassanto_monfort_1977]
- [CASSANTO, 1966, Angle-of-attack measurements of a hypersonic reentry vehicle derivedfrom flight test pressure data][research_cassanto_1966]
- [Cassell and others, 2011, Hayabusa Re-entry Trajectory Analysis and Observation Mission Design][research_cassell_allen_2011]
- [Cavallo and others, 1996, A trajectory and attitude control strategy for the CRV/CRT atmospheric reentry][research_cavallo_demaria_1996]
- [Cavesmith and others, 2026, Efficient Long-Range Lunar Descent Trajectory Generation with Continuous-Time Sequential Convex Programming][research_cavesmith_bhatt_2026]
- [CECERE, 2026, Heat Transfer Analysis of Ultra-High-Temperature Ceramics in Plasma Wind Tunnel Experiments][research_cecere_2026]
- [CENTER and others, 1991, Interactive design of hypersonic waverider geometries][research_center_sobieczky_1991]
- [Chadalavada and others, 2026, Desensitized Aerocapture Terminal Guidance][research_chadalavada_deshmukh_2026]
- [Chadwick, 2000, Hypersonic shock tunnel measurements and simulations with a generic re-entry vehicle configuration][research_chadwick_2000]
- [Chai and others, 2015, Boost-skipping trajectory optimization for air-breathing hypersonic missile][research_chai_fang_2015]
- [Chai and others, 2020, Trajectory planning for hypersonic reentry vehicle satisfying deterministic and probabilistic constraints][research_chai_tsourdos_2020]
- [Chander and Krishna, 2013, Atmospheric Reentry Dispersion Correction Ascent Phase Guidance for a Generic Reentry Vehicle][research_chander_krishna_2013]
- [Chander and Krishna, 2013, Real Time Mid-course Maneuver and Guidance of a Generic Reentry Vehicle][research_chander_krishna_2013_b]
- [Chandler, 2019, Design and Testing of a Small Launch Vehicle with Lessons Learned][research_chandler_2019]
- [Chang and others, 2022, Thermal Protection Mechanism of a Novel Adjustable Non-Ablative Thermal Protection System for Hypersonic Vehicles][research_chang_huang_2022]
- [Chang and others, 2023, Numerical study on hypersonic aerodynamic characteristics of the high-pressure capturing wing configuration with wing dihedral][research_chang_xiao_2023]
- [Changbao and others, 2020, Performance Simulation Analysis of Composite Thermal Management System for Hypersonic Vehicle][research_changbao_hui_2020]
- [Changsheng and others, 2006, Optimal Guidance Law Design for Reentry Vehicle Using Virtual Displacement Concept][research_changsheng_wuxing_2006]
- [Chao and Jeng, 1965, Unsteady Stagnation Point Heat Transfer][research_chao_jeng_1965]
- [Chao and others, 2010, Maximum crossrange guidance under multiple constraints for lifting body reentry vehicle][research_chao_wang_2010]
- [Chao and others, 2014, Disturbance observer based constrained multi-model predictive control for Mars entry trajectory tracking][research_chao_shihua_2014]
- [Chao and others, 2015, Six-DOF Modeling and Simulation for Generic Hypersonic Vehicle in Reentry Phase][research_chao_xinyu_2015]
- [Chao and others, 2022, Adaptive fault-tolerant attitude control for hypersonic reentry vehicle subject to complex uncertainties][research_chao_qi_2022]
- [Chao and others, 2022, Adaptive fault-tolerant control for the ascent phase of hypersonic vehicle with time-varying full state constraints][research_chao_qi_2022_b]
- [Chao and others, 2026, RDRL-Augmented Free α SCP for Real-Time Glide-Reentry Trajectory Optimization of Hypersonic Vehicles][research_chao_cheng_2026]
- [Chao Song and others, 2011, Boost phase trajectory optimization for hypersonic vehicle based on GPM][research_chaosong_guorongzhao_2011]
- [Chase and McKinney, 2005, A Least Cost Reusable Operationally Responsive Space Launch Vehicle Demonstrator][research_chase_mckinney_2005]
- [Chauffour and Lewis, 2003, Corrected Shock-Based Design for Waverider Geometries][research_chauffour_lewis_2003]
- [Chauffour and Lewis, 2004, Corrected Waverider Design for Inlet Applications][research_chauffour_lewis_2004]
- [Chaumette and Cretenet, 1987, Hermes thermal protection system overview][research_chaumette_cretenet_1987]
- [Chauvet and Brouquet, 2005, Surface Recession Simulations with ESATAN/ABLAT During a Re-Entry Trajectory][research_chauvet_brouquet_2005]
- [Chavez and Schmidt, 1994, Analytical aeropropulsive-aeroelastic hypersonic-vehicle model with dynamic analysis][research_chavez_schmidt_1994]
- [Chaw-Bing Chang and others, 1977, On the state and parameter estimation for maneuvering reentry vehicles][research_chawbingchang_athans_1977]
- [Chawla and others, 2010, Suboptimal reentry guidance of a reusable launch vehicle using pitch plane maneuver][research_chawla_sarmah_2010]
- [Che and Tang, 2008, Research on integrated optimization design of hypersonic cruise vehicle][research_che_tang_2008]
- [Cheah and others, 2025, Control Synthesis for Hypersonic Vehicle Flight Testing with Input-Output-Sampled Nonlinearities][research_cheah_bhattacharjee_2025]
- [Chen and Chen, 2014, Thermal Design and Dynamic Analysis of Metallic Thermal Protection System][research_chen_chen_2014]
- [Chen and Fan, 2025, A Machine Learning Rapid Prediction of the Aerothermodynamic Environment for Near-Space Hypersonic Unmanned Aircraft][research_chen_fan_2025]
- [Chen and Fu, 2019, Long-Range AFM Imaging with Modified Cycloid Trajectory][research_chen_fu_2019]
- [Chen and He, 2025, An engineering method of aerodynamic heating prediction for hypersonic blunt body vehicles][research_chen_he_2025]
- [Chen and Liu, 2013, Flight Trajectory Visual Simulation Technology of Space-based Reentry Vehicles][research_chen_liu_2013]
- [Chen and Milos, 1996, Solution strategy for thermal response of nonablating thermal protection systems at hypersonic speeds][research_chen_milos_1996]
- [Chen and others, 1995, Three-dimensional hypersonic flowfields and heating analysis over DC-3 vehicle][research_cheninewd_olynick_1995]
- [Chen and others, 2005, Genetic Algorithm Optimization of RLV Reentry Trajectory][research_chen_wan_2005]
- [Chen and others, 2005, Multidisciplinary Design Optimization of RLV Reentry Trajectory][research_chen_xu_2005]
- [Chen and others, 2006, Aerothermodynamic Optimization of Hypersonic Vehicle TPS Design by POD/RSM-Based Approach][research_chen_liu_2006]
- [Chen and others, 2006, Optimization and Implementation of Periodic Cruise for a Hypersonic Vehicle][research_chen_williamson_2006]
- [Chen and others, 2008, Terminal and Boost Phase Intercept of Ballistic Missile Defense][research_chen_speyer_2008]
- [Chen and others, 2009, Integrated Aero-Servo-Thermo-Propulso-Elasticity ASTPE for Hypersonic Scramjet Vehicle Design/Analysis][research_chen_starkey_2009]
- [Chen and others, 2011, Bluntness impact on performance of waverider][research_chen_hou_2011]
- [Chen and others, 2014, An online predictive reentry guidance law for reusable launch vehicles][research_chen_fu_2014]
- [Chen and others, 2014, THE APPLICATION OF HIGH TEMPERATURE HEAT PIPE TECHNIQUE ON HYPERSONIC VEHICLE THERMAL PROTECTION][research_chen_ai_2014]
- [Chen and others, 2015, A reduced order aerothermodynamic modeling framework for hypersonic vehicles based on surrogate and POD][research_chen_liu_2015]
- [Chen and others, 2015, Coupled Analysis of Aerodynamic Heating, Radiative Heat Transfer and Heat Conduction for Hypersonic Vehicles][research_chen_liu_2015_b]
- [Chen and others, 2015, Integrated Guidance and Control Method for the Interception of Maneuvering Hypersonic Vehicle Based on High Order Sliding Mode Approach][research_chen_fu_2015]
- [Chen and others, 2016, Adaptive backstepping control for reentry attitude of near space hypersonic vehicle with input saturation][research_chen_zhu_2016]
- [CHEN and others, 2016, Effect of atmosphere parameter oscillation at high altitude in the northern hemisphere for near space hypersonic flight aerothermodynamic prediction][research_chen_du_2016]
- [Chen and others, 2016, Evaluation of hypersonic vehicle SINS navigation solution in the hardware-in-the-loop simulation][research_chen_chen_2016_b]
- [Chen and others, 2016, L 1 adaptive controller design for hypersonic formation flight][research_chen_wan_2016]
- [Chen and others, 2016, The Effects of Chemical Nonequilibrium and Surface Catalyticity on Aerothermodynamic Characteristics of Hypersonic Vehicles][research_chen_chen_2016]
- [Chen and others, 2016, Virtual displacement guidance for hypersonic glide vehicle][research_chen_gao_2016]
- [Chen and others, 2017, Nonlinear region of attraction analysis for hypersonic flight vehicles' flight control verification][research_chen_ma_2017]
- [Chen and others, 2017, Numerical Investigation of Laminar Separation Induced by Body Flap of Hypersonic Vehicle][research_chen_ni_2017]
- [Chen and others, 2018, An Adaptive Control Approach for a Flexible Hypersonic Glide Vehicle][research_chen_jing_2018]
- [Chen and others, 2018, Extended state observer-based back-stepping control for hypersonic reentry vehicle with input constraints][research_chen_ma_2018]
- [Chen and others, 2018, Hypersonic Vehicles Profile-Following Based on LQR Design Using Time-Varying Weighting Matrices][research_chen_xiong_2018]
- [Chen and others, 2018, Modeling and Analysis of Fluid-Thermal-Structure Coupling Problems for Hypersonic Vehicles][research_chen_zhang_2018]
- [Chen and others, 2018, Nonlinear Fault-Tolerant Control for Hypersonic Flight Vehicle With Multi-Sensor Faults][research_chen_niu_2018]
- [Chen and others, 2019, Adaptive diagnosis and compensation for hypersonic flight vehicle with multisensor faults][research_chen_gong_2019]
- [Chen and others, 2019, Nussbaum gain adaptive control scheme for moving mass reentry hypersonic vehicle with actuator saturation][research_chen_zhou_2019]
- [Chen and others, 2019, Waverider Configuration Design With Variable Shock Angle][research_chen_guo_2019]
- [Chen and others, 2020, 3-D Reentry Guidance with Real-Time Planning of Reference using New Analytical Solutions Based on Spectral Decomposition Method][research_chen_zhou_2020_m]
- [Chen and others, 2020, Analytical predictor-corrector entry guidance for hypersonic gliding vehicles][research_chen_zhao_2020]
- [Chen and others, 2020, Analytical Solutions of Steady Glide Reentry Trajectory in Three Dimensions and Their Application to Trajectory Planning][research_chen_zhou_2020_d]
- [Chen and others, 2020, Concept of Steady Glide Reentry Trajectory and Stability of Its Regular Perturbation Solutions][research_chen_zhou_2020_f]
- [Chen and others, 2020, Decoupling Attitude Control of a Hypersonic Glide Vehicle Based on a Nonlinear Extended State Observer][research_chen_du_2020]
- [Chen and others, 2020, Direct Method for Gliding Trajectory Optimization Problem][research_chen_zhou_2020_g]
- [Chen and others, 2020, Hypersonic boost-glide vehicle strapdown inertial navigation system / global positioning system algorithm in a launch-centered earth-fixed frame][research_chen_zhou_2020_n]
- [Chen and others, 2020, Indirect Approach to the Optimal Glide Trajectory Problem][research_chen_zhou_2020_c]
- [Chen and others, 2020, Linear Pseudospectral Reentry Guidance with Adaptive Flight Phase Segmentation and Eliminating General Nominal Effort Miss Distance][research_chen_zhou_2020_l]
- [Chen and others, 2020, Mathematical Description of Glide-Trajectory Optimization Problem][research_chen_zhou_2020_b]
- [Chen and others, 2020, Mathematical Modeling for Hypersonic Glide Problem][research_chen_zhou_2020_h]
- [Chen and others, 2020, Omnidirectional Autonomous Reentry Guidance Based on 3-D Analytical Glide Formulae Considering Influence of Earth's Rotation][research_chen_zhou_2020_k]
- [Chen and others, 2020, Robust finite time tracking control of flexible hypersonic vehicle with uncertainties][research_chen_wei_2020]
- [Chen and others, 2020, Robust Guidance Algorithm against Hypersonic Targets][research_chen_han_2020]
- [Chen and others, 2020, Simulation Platform for SINS/GPS Integrated Navigation System of Hypersonic Vehicles Based on Flight Mechanics][research_chen_shen_2020_b]
- [Chen and others, 2020, Singular Perturbation Guidance of Hypersonic Glide Reentry][research_chen_zhou_2020_i]
- [Chen and others, 2020, SINS/BDS Integrated Navigation for Hypersonic Boost-Glide Vehicles in the Launch-Centered Inertial Frame][research_chen_shen_2020]
- [Chen and others, 2020, Steady Glide Dynamic Modeling and Trajectory Optimization for High Lift-To-Drag Ratio Reentry Vehicle][research_chen_zhou_2020_e]
- [Chen and others, 2020, Trajectory Damping Control Technique for Hypersonic Glide Reentry][research_chen_zhou_2020]
- [Chen and others, 2020, Trajectory-shaping Guidance with Final Speed and Load Factor Constraints][research_chen_zhou_2020_j]
- [Chen and others, 2021, A novel lightweight aerodynamic design for the wings of hypersonic vehicles cruising in the upper atmosphere][research_chen_huang_2021]
- [Chen and others, 2021, Adding-Point Strategy for Surrogate-Based Reduced-Order Hypersonic Aerothermodynamic Modeling Based on Fuzzy Clustering][research_chen_cao_2021]
- [Chen and others, 2021, Guidance Algorithm for Reentry Vehicle Considering Target Maneuvering and No-fly Zone Constraints][research_chen_wang_2021]
- [Chen and others, 2021, Prediction-Correction Guidance Algorithm for High Velocity Reentry Capsules][research_chen_wang_2021_b]
- [Chen and others, 2021, Tightly Coupled Integrated Navigation Algorithm for Hypersonic Boost-Glide Vehicles in the LCEF Frame][research_chen_pei_2021]
- [Chen and others, 2022, Hierarchical Sliding Mode Control for Elastic Hypersonic Glide Vehicles Based on Moving Horizon Estimation][research_chen_zhu_2022]
- [Chen and others, 2022, Normal gravity model for inertial navigation of a hypersonic boost-glide vehicle][research_chen_zeng_2022]
- [Chen and others, 2022, SINS/BDS tightly coupled integrated navigation algorithm for hypersonic vehicle][research_chen_pei_2022]
- [Chen and others, 2023, Fixed-Time Dynamic Surface Control for Hypersonic Morphing Vehicle with Uncertainties Based on Fixed-Time Disturbance Observers][research_chen_wang_2023_b]
- [Chen and others, 2023, Nonsingular Fast Terminal Sliding Mode Based Impact Angle Guidance Law][research_chen_lin_2023]
- [Chen and others, 2023, On Predictor-Corrector Guidance of Hypersonic Vehicle in Glide Segment][research_chen_sun_2023]
- [Chen and others, 2023, Position Biased Terminal Guidance Based on Geometric Tangent][research_chen_guo_2023]
- [Chen and others, 2023, Trajectory Generator for Hypersonic Vehicle Based on Flight Dynamics][research_chen_wang_2023]
- [Chen and others, 2025, A hybrid discretization strategy for successive convex programming in skip entry trajectory optimization][research_chen_zhang_2025]
- [Chen and others, 2025, Effect of Thermal Protection System on Aerodynamics and Pressure of Reusable Launch Vehicle][research_chen_yang_2025]
- [Chen and others, 2025, Effects and mechanisms of multiple lateral jets on aerodynamic characteristics of a hypersonic vehicle][research_chen_huang_2025]
- [Chen and others, 2025, Optimal Guidance for Reusable Launch Vehicle in Reentry Phase Based on Adaptive Dynamic Programming with Experience Replay][research_chen_zhu_2025]
- [Chen and others, 2025, Research on Trajectory Optimization and Generation Methods for Hypersonic Glide Vehicles Targeting Moving Targets][research_chen_lu_2025]
- [Chen and others, 2026, Ablation resistance and high-temperature bending properties of free-standing ultra-high-temperature ceramics ZrB2-SiC-ZrC coating][research_chen_zhou_2026]
- [CHEN and others, 2026, Aerodynamic shape optimization of hypersonic aircraft using data-driven generative nonlinear parameterization][research_chen_li_2026]
- [Chen and others, 2026, Explicit Trajectory Dispersion Control for Precision Landing Guidance of Reusable Rockets][research_chen_zhang_2026]
- [Chen and others, 2026, Large eddy simulation of hypersonic boundary layer transition on the hypersonic transition research vehicle model lifting body at high angles of attack][research_chen_mao_2026]
- [Chen and others, 2026, Recent advances in high-entropy carbide ultra-high temperature ceramics Synthesis, properties, and applications][research_chen_han_2026]
- [Chen and Tseng, 2011, A robust fuzzy trajectory estimation design of high speed reentry vehicles][research_chen_tseng_2011]
- [Chen and Wu, 2018, Development of a Small Launch Vehicle with Hybrid Rocket Propulsion][research_chen_wu_2018]
- [Chen and Xia, 2022, Study on the Leading Edge of a Hypersonic Vehicle Using the Aero-Thermoelastic Coupling Method][research_chen_xia_2022]
- [Chen Chen and others, 2015, The analysis on infrared radiant properties of hypersonic vehicle][research_chenchen_cunfenggu_2015]
- [Chen, 1958, Closure to "Discussion of 'Transient Temperature and Thermal Stresses in Skin of Hypersonic Vehicle With Variable Boundary Conditions'" 1958, Trans. ASME, 80, p. 1394][research_chen_1958_b]
- [Chen, 1958, Transient Temperature and Thermal Stresses in Skin of Hypersonic Vehicle With Variable Boundary Conditions][research_chen_1958]
- [Chen, 2016, Numerical analyses of ablative behavior of C/C composite materials][research_chen_2016]
- [Chen, 2016, Robust terminal guidance law design for missiles against maneuvering targets][research_chen_2016_b]
- [Chen, 2017, Integrated flight/propulsion control for unknown hypersonic flight vehicles systems][research_chen_2017_b]
- [Chen, 2017, Strapdown Inertial Navigation Algorithm for Hypersonic Boost-Glide Vehicle][research_chen_2017]
- [Chen, 2019, Development of Hapith Small Launch Vehicle based on Hybrid Rocket Propulsion][research_chen_2019]
- [Chen, 2021, One hypersonic unmanned aerial vehicle sensor failure controller design][research_chen_2021]
- [Chen, 2023, ULTRA-HIGH-TEMPERATURE CERAMIC MATERIALS MODIFIED BY GRAPHENE AN OVERVIEW][research_chen_2023]
- [Cheng and others, 2011, Thermoelastic Analysis of an Heterogeneous Orthotropic Nose Cap for a Hypersonic Vehicle][research_cheng_yang_2011]
- [Cheng and others, 2013, Thermal Shock Resistance of Ultra-High-Temperature Ceramics Under Aerodynamic Thermal Environments][research_cheng_li_2013]
- [Cheng and others, 2014, Heat Transfer and Failure Mode Analyses of Ultrahigh-Temperature Ceramic Thermal Protection System of Hypersonic Vehicles][research_cheng_li_2014]
- [Cheng and others, 2016, Improved nonsingular terminal sliding mode attitude tracking control for reentry vehicle][research_cheng_sheng_2016]
- [Cheng and others, 2017, Advanced reentry guidance based on on-board reference trajectory reconstruction][research_cheng_zhang_2017]
- [Cheng and others, 2018, Flexibility suppression for aeroelastic hypersonic vehicle][research_cheng_wang_2018]
- [Cheng and others, 2019, Cross-cycle iterative unmanned aerial vehicle reentry guidance based on reinforcement learning][research_cheng_shui_2019]
- [Cheng and others, 2019, Fuzzy-reconstruction-based robust tracking control of an air-breathing hypersonic vehicle][research_cheng_wang_2019]
- [Cheng and others, 2019, Trajectory Estimation of Hypersonic Glide Vehicle Based on Analysis of Aerodynamic Performance][research_cheng_yan_2019]
- [Cheng and others, 2020, Self-repairing control of air-breathing hypersonic vehicle with actuator fault and backlash][research_cheng_chen_2020]
- [Cheng and others, 2021, Aerothermodynamic study of Two-Stage-To-Orbit system composed of wide-speed-range vehicle and rocket][research_cheng_chen_2021]
- [Cheng and others, 2021, An adaptive non-zero mean damping model for trajectory tracking of hypersonic glide vehicles][research_cheng_yan_2021]
- [Cheng and others, 2023, Ascent Phase Trajectory Optimization for Hypersonic Vehicle Using hp-Adaptive Pseudo-spectral Method][research_cheng_wei_2023]
- [Cheng and others, 2023, Trajectory Tracking of Maneuvering Reentry Vehicle Using Nonlinear Estimate Model][research_cheng_li_2023]
- [Cheng and others, 2024, A model predictive solution to cooperative guidance of hypersonic reentry vehicle with impact angle and distance coordination][research_cheng_song_2024]
- [Cheng and others, 2024, Drag reduction and aero heating prevention of a combined configuration of opposing jet and backward jet for hypersonic vehicles at different angles of attack][research_cheng_fang_2024]
- [Cheng and others, 2025, A Parameter Optimization Method for Non-singular Terminal Sliding Mode Guidance Law with Falling Angle Constraint][research_cheng_shen_2025]
- [Cheng and others, 2025, Geometric Approach to Lateral Guidance for Reentry Vehicle][research_cheng_song_2025]
- [Cheng and others, 2025, Midcourse Trajectory Modification Approach Based on Predictive-Control for Hypersonic Vehicle][research_cheng_yi_2025]
- [Cheng and others, 2025, The hydrodynamic characteristics and continuous skipping control strategy of skipping flight vehicle shaped by waverider configuration][research_cheng_wang_2025]
- [Cheng and Williams III, 1974, CURVATURE EFFECTS ON HEAT TRANSFER NEAR A FORWARD STAGNATION POINT][research_cheng_williamsiii_1974]
- [Cheng, 1965, Surveyor Terminal Guidance][research_cheng_1965]
- [Cheng, 1966, Surveyor Terminal Guidance][research_cheng_1966]
- [Chengbin Lian and others, 2012, Reference Command Tracking and Simulation Research of Hypersonic Cruise Vehicle][research_chengbinlian_zhangren_2012]
- [Chenhao and others, 2019, Engineering Calculation Method of Aerodynamic Coefficients for Air-breathing Hypersonic Vehicle][research_chenhao_naigang_2019]
- [Chernyi and Gonor, 1973, Lifting Body Configurations for Sustained Hypersonic Flight][research_chernyi_gonor_1973]
- [CHERNYI, 1961, EFFECT OF SLIGHT LEADING EDGE BLUNTING ON HYPERSONIC FLOWS PAST BODIES][research_chernyi_1961]
- [CHERNYI, 1961, HYPERSONIC FLOWS PAST SLENDER BODIES WITH SHARP LEADING EDGES][research_chernyi_1961_b]
- [Chetverushkin and others, 2006, Numerical Simulation of 2D Radiation Heat Transfer for Reentry Vehicles][research_chetverushkin_polyakov_2006]
- [Chevalier and others, 1996, French-Russian partnership on hypersonic wide range ramjets][research_chevalier_bouchez_1996]
- [Chi and others, 2021, Disturbance Compensation Based Backstepping Control for Hypersonic Vehicle][research_chi_wang_2021]
- [Chi and Zhou, 2021, Trajectory Planning for Hypersonic Vehicles with Reinforcement Learning][research_chi_zhou_2021]
- [Chiesa and others, 2005, A Small-Scale Low-Cost Technology Demonstrator of a Reusable Launch Vehicle][research_chiesa_grassi_2005]
- [CHIN and others, 1964, REENTRY HEATING AND THERMAL PROTECTION OF A MARS-MISSION EARTH-REENTRY MODULE][research_chin_hearne_1964]
- [Ching and others, 2024, Reduced Order Models of Hypersonic Aerodynamics for Aerothermal Heating Analysis][research_ching_blonigan_2024]
- [Chinnaraj and others, 2023, Arc-Jet Tests of Carbon-Phenolic-Based Ablative Materials for Spacecraft Heat Shield Applications][research_chinnaraj_kim_2023]
- [Chirayath and Bindu, 2014, Longitudinal guidance and control of reentry vehicle in the approach and landing phase][research_chirayath_bindu_2014]
- [Cho and others, 2017, Trajectory Shaping Guidance Law Based on Downrange-to-Go Polynomial][research_cho_kim_2017]
- [Cho and others, 2021, Integrated Framework for Staging and Trajectory Optimization of a Launch Vehicle Considering Range Safety Operations][research_cho_jo_2021]
- [Choi and Gamba, 2026, Thermal Protection Systems Model for a JP-7 Fueled Hypersonic Vehicle][research_choi_gamba_2026]
- [Choi and others, 2022, Design of Deep Space Missions Using a Dedicated Small Launch Vehicle][research_choi_loucks_2022]
- [Choi and others, 2023, Effectiveness of water spray in infrared signature suppression of engine plumes][research_choi_moon_2023]
- [Chou and others, 1996, Flight simulation of hypersonic waverider with finlets under various angles-of-attack][research_chou_shen_1996]
- [CHOW and EL-ASSAR, 1970, A kinetic study of the hypersonic flow past the leading edge of a flat plate][research_chow_elassar_1970]
- [CHOW, 1966, Hypersonic Slip Flow past the Leading Edge of a Flat Plate][research_chow_1966]
- [CHOW, 1967, Hypersonic rarefied flow past the sharp leading edge of a flat plate][research_chow_1967]
- [Chpoun, 1990, Hypersonic Transitional Flow in a Compression Corner in 2D Configuration][research_chpoun_1990]
- [Chu and Li, 2017, Multi-Objective Re-entry Trajectory Optimization based on the Physical Programming Method for Hypersonic Gliding Vehicle][research_chu_li_2017_b]
- [Chu and others, 2008, A Feasibility Study to the Application of Interval Analysis to Re-Entry Trajectory Optimization][research_chu_mooij_2008]
- [Chu and others, 2017, Improved MPSP Method-based Cooperative Re-entry Guidance for Hypersonic Gliding Vehicles][research_chu_li_2017]
- [Chu and others, 2023, Aerodynamic Parameter Identification of Hypersonic Vehicles Based on Improved Harris Hawks Optimization][research_chu_chunwang_2023]
- [Chuang and Morimoto, 1996, Optimal periodic cruise for a hypersonic vehicle with constraints][research_chuang_morimoto_1996]
- [Chuang and Morimoto, 1997, Periodic Optimal Cruise for a Hypersonic Vehicle with Constraints][research_chuang_morimoto_1997]
- [Chuanzhen and others, 2022, Design and Analysis of Double-Swept Waverider with Wing Dihedral][research_chuanzhen_xufei_2022_b]
- [Chuanzhen and others, 2022, Experimental and numerical investigation for hypersonic performance of double swept waverider][research_chuanzhen_xufei_2022]
- [Chuanzhen and Peng, 2021, Mathematical Expression of Geometric Relationship in Osculating-Cone Waverider Design][research_chuanzhen_peng_2021]
- [Chudej and Bulirsch, 1993, Numerical solution of a simultaneous staging and trajectory optimization problem of a hypersonic space vehicle][research_chudej_bulirsch_1993]
- [Chudej and others, 2009, Instationary Heat-Constrained Trajectory Optimization of a Hypersonic Space Vehicle by ODE-PDE-Constrained Optimal Control][research_chudej_pesch_2009]
- [Chudej, 1993, Optimal Ascent of a Hypersonic Space Vehicle][research_chudej_1993]
- [Chudoba and others, 2015, Strategic forecasting in uncertain environments hypersonic cruise vehicle research and development case study][research_chudoba_haney_2015]
- [Chue and others, 2009, Design and analysis of a rectangular cross-section hypersonic nozzle][research_chue_cresci_2009]
- [Chun, 1991, Experiments on the Heat Transfer and on the Aerodynamic Coefficients of a Delta Wing in Rarefied Hypersonic Flows][research_chun_1991]
- [Chung and Lee, 2006, Trajectory Simulation of the Small Atmospheric Re-entry Module][research_chung_lee_2006]
- [Cinquegrana and others, 2015, Aerodynamic and Aerothermodynamic Design of the USV3 Re-Entry Vehicle][research_cinquegrana_pezzella_2015]
- [Clapp and others, 2015, Structural Response of Hypersonic Inflatable Aerodynamic Decelerator Braided Tube Components and Elements][research_clapp_young_2015]
- [CLAPP, 1965, A small "state-of-the-art" maneuverable lifting reentry vehicle][research_clapp_1965]
- [Clark and others, 1993, Experimental evaluation of low-catalysis coatings for hypersonic vehicle applications][research_clark_cunnington_1993]
- [Clark and others, 2006, An Aero-Propulsion Integrated Elastic Model of a Generic Airbreathing Hypersonic Vehicle][research_clark_mirmirani_2006]
- [CLARK, 1969, Aerodynamic characteristics of the hemisphere at supersonic and hypersonic Mach numbers][research_clark_1969]
- [Clarke, 2008, New Thermal Protection Concepts for the Next Generation Gas Turbines and Hypersonic Vehicles][research_clarke_2008]
- [Clegg and others, 2019, Validation of a Crossflow Velocity Model Between Waverider Flowfield Planes][research_clegg_rodi_2019]
- [Clegg and others, 2020, Waverider Crossflow Model Validation for Radial and Length Variations Between Osculating Planes][research_clegg_rodi_2020]
- [CLIFF and others, 1992, Flight-test guidance for airbreathing hypersonic vehicles][research_cliff_well_1992]
- [Cockrell and others, 1995, Aerodynamic performance and flow-field characteristics of two waverider-derived hypersonic cruise configurations][research_cockrellsejr_huebner_1995]
- [COCKRELL, 1993, Interpretation of waverider performance data using computational fluid dynamics][research_cockrelljr_1993]
- [Cockrell, 1994, Interpretation of waverider performance data using computational fluid dynamics][research_cockrell_1994]
- [COLE and AROESTY, 1965, Optimum hypersonic lifting surfaces close to flat plates][research_cole_aroesty_1965]
- [Colgren and others, 2009, Nonlinear Ten-Degree-of-Freedom Dynamics Model of a Generic Hypersonic Vehicle][research_colgren_keshmiri_2009]
- [COLOSIMO, 1968, Techniques for aerothermodynamic testing of ablating models in the wave superheater hypersonic tunnel][research_colosimo_1968]
- [Colville and Lewis, 2003, Inverse Design of Hypersonic Star Inlets][research_colville_lewis_2003]
- [Colwell, 2023, COOLING HYPERSONIC VEHICLE STRUCTURES][research_colwell_2023]
- [COMPTON and others, 1979, Shuttle entry trajectory reconstruction using inflight accelerometer and gyro measurements][research_compton_blanchard_1979]
- [COMPTON and others, 1981, Shuttle /STS-1/ entry trajectory reconstruction][research_compton_findlay_1981]
- [Cong and Kunfeng, 2017, Control surface optimization of hypersonic vehicle based on adaptive backstepping method][research_cong_kunfeng_2017]
- [Connolly, 2026, Numerical Investigations of Active Cooling Architectures for Hypersonic Leading Edges][research_connolly_2026]
- [Copeland and others, 2014, Adjoint-Based Aerothermodynamic Shape Design of Hypersonic Vehicles in Non-Equilibrium Flows][research_copeland_palacios_2014]
- [Coras and Paull, 2006, Experiments on External Combustion with Leading Edge Fuel-Injection in Hypersonic Flow][research_coras_paull_2006]
- [CORDA and ANDERSON, 1988, Viscous optimized hypersonic waveriders designed from axisymmetric flow fields][research_corda_andersonjr_1988]
- [Cornick and others, 2023, Parameterization and Design Space Exploration of a Hypersonic Inflatable Aerodynamic Decelerator][research_cornick_robertson_2023]
- [Coulter and others, 2021, Hypersonic Trajectory Optimization with High-Fidelity Aerothermodynamic Models][research_coulter_wang_2021]
- [Coulter and others, 2023, Geometric Design of Hypersonic Vehicles for Optimal Mission Performance with High-Fidelity Aerodynamic Models][research_coulter_huang_2023]
- [COUSIN, 1967, Leading edge bluntness effects and their importance in hypersonic inlet design][research_cousin_1967]
- [Couture and others, 2008, Comparison of Scramjet and Shcramjet Propulsion for an Hypersonic Waverider Configuration][research_couture_dechamplain_2008]
- [COVELL and others, 1988, Configuration trade and code validation study on a conical hypersonic vehicle][research_covell_wood_1988]
- [Covington and others, 2004, Performance of a Low Density Ablative Heat Shield Material][research_covington_balboni_2004]
- [Covington and others, 2008, Erratum on "Erratum on 'Performance of a Low Density Ablative Heat Shield Material'"][research_covington_heinemann_2008_c]
- [Covington and others, 2008, Erratum on "Performance of a Low Density Ablative Heat Shield Material"][research_covington_heinemann_2008_b]
- [Covington and others, 2008, Performance of a Low Density Ablative Heat Shield Material][research_covington_heinemann_2008]
- [CRAMER and others, 1988, NLP reentry guidance - Developing a strategy for low L/D vehicles][research_cramer_bradt_1988]
- [Cremaschi, 2012, Trajectory Optimization for Launchers and Re-entry Vehicles][research_cremaschi_2012]
- [Cristillo and others, 2019, Structural and Thermal Loads for Hypersonic HEXAFLY-INT Vehicle][research_cristillo_scigliano_2019]
- [Cui and Hu, 2013, Aerothermal Shape Optimization of Hypersonic Vehicle Leading Edge by Using Genetic Algorithm][research_cui_hu_2013_b]
- [Cui and others, 2007, Waverider configurations derived from general conical flowfields][research_cui_zhao_2007]
- [Cui and others, 2010, Optimal Sliding-Mode Terminal Guidance Law Design of Airborne Boost-Phase Ballistic Missile Interception][research_cui_fu_2010]
- [Cui and others, 2013, A novel tracking control method for a flexible air-breathing hypersonic vehicle][research_cui_zhang_2013]
- [Cui and others, 2013, Conceptual design and aerodynamic evaluation of hypersonic airplane with double flanking air inlets][research_cui_hu_2013]
- [CUI and others, 2022, Competing effects of surface catalysis and ablation in hypersonic reentry aerothermodynamic environment][research_cui_zhao_2022]
- [Cui and others, 2022, Cooperative Trajectory Optimization for Long-range Interception with Terminal Handover Constraints][research_cui_wei_2022]
- [Cui and others, 2022, Terminal Multi-Constrained Finite Time Sliding Mode Guidance Law Based on Truncation Function for Hypersonic Vehicle][research_cui_hu_2022]
- [Cui and others, 2024, Prescribed-time integrated guidance and control for bank to turn reentry vehicle][research_cui_zhen_2024]
- [Cui and others, 2025, Prescribed-Time Cooperative Integrated Guidance and Control for Reentry Vehicle Based on Hybrid Control Strategy][research_cui_zhen_2025]
- [Cui and others, 2026, Low-Order Integrated Guidance and Control Scheme for Reentry Vehicle Based on Dual-Loop Controller][research_cui_li_2026]
- [Cui and others, 2026, Reinforcement learning-based morphing decision and prescribed-time control for hypersonic morphing vehicle with prescribed performance][research_cui_han_2026]
- [Cui and Yang, 2009, Conceptual Design of Hypersonic Vehicles with Large Capacity and High Aerodynamic Performance][research_cui_yang_2009]
- [Culler and others, 2007, Aerothermal Modeling and Dynamic Analysis of a Hypersonic Vehicle][research_culler_williams_2007]
- [Cummings, 2022, Summary of Progress for the DoD HPCMP Hypersonic Vehicle Simulation Institute][research_cummings_2022]
- [Cunningham, 1987, Hypersonic aerodynamics for an entry research vehicle][research_cunningham_1987]
- [Cutrone and Schettino, 2024, Rans Transition Model Predictions on Hypersonic Three-Dimensional Forebody Configuration][research_cutrone_schettino_2024]
- [Cutrone, 2023, RANS transition model predictions on hypersonic three-dimensional forebody configuration][research_cutrone_2023]
- [Cvrlje, 1999, Unsteady separation of a two-stage hypersonic vehicle][research_cvrlje_1999]
- [Cygan and others, 2025, Densification, mechanical and electrical properties of ultra-high temperature ceramics from ZrB2-SiC/graphene systems][research_cygan_wozniak_2025]
- [Czysz and others, 1997, A concept for an international project to develop a hypersonic flight test vehicle][research_czysz_froning_1997]
- [Căruntu and others, 2008, Optimal control in trajectory planning for a re-entry vehicle][research_caruntu_negrea_2008]
- [D'Amato and others, 2022, Trajectory Planning and Tracking for a Re-Entry Capsule with a Deployable Aero-Brake][research_damato_notaro_2022]
- [D'Amico and others, 2004, A Perspective for Hypersonic Vehicle Flight Instrumentation][research_damico_simon_2004]
- [D'Oriano and others, 2018, Aerothermodynamic study of a small hypersonic plane][research_doriano_savino_2018]
- [D'Souza and others, 2008, Development and Simulation of an Analytic Skip Earth Re-Entry Guidance Algorithm][research_dsouza_sarigulklijn_2008_b]
- [D'Souza and others, 2014, Potential for Integrating Entry Guidance into the Multi-Disciplinary Entry Vehicle Optimization Environment][research_dsouza_kinney_2014]
- [D'Souza and others, 2019, Potential for Integrating Entry Guidance into the Multi-Disciplinary Entry Vehicle Optimization Environment][research_dsouza_kinney_2019]
- [D'Souza and Sarigul-Klijn, 2008, An Analytical Approach to Skip Earth Entry Guidance of a Low L/D Vehicle][research_dsouza_sarigulklijn_2008]
- [D'Souza and Sarigul-Klijn, 2012, Investigation of Trajectory Generation for a Mission Adaptive Planetary Entry Guidance Algorithm][research_dsouza_sarigulklijn_2012]
- [da Costa and others, 2016, AERODYNAMIC HEATING OF THE BRAZILIAN 14-X HYPERSONIC WAVERIDER SCRAMJET VEHICLE AT MACH NUMBERS 7 AND 10][research_dacosta_rolim_2016]
- [da Costa and Sachs, 2005, Reentry Trajectory Optimization for Preventing Overheating of Damaged Thermal Protection System][research_dacosta_sachs_2005]
- [Da-wei, 2011, Reentry guidance based on feedback linearization][research_dawei_2011]
- [Dabas and others, 2025, Multi-Objective Optimization of Reentry Vehicle Design Aerodynamics, Heat Transfer, and Structural Durability][research_dabas_sheikh_2025]
- [Dai and others, 2020, Design and aerodynamic performance analysis of a variable-sweep-wing morphing waverider][research_dai_yan_2020]
- [Dai and others, 2024, Longitudinal Trajectory Planning and Attitude Control of Hypersonic Morphing Vehicle][research_dai_fang_2024]
- [Dai and others, 2025, An Adaptive Terminal Guidance Law Based on Deep Reinforcement Learning][research_dai_yang_2025]
- [Dai and others, 2026, Reentry Trajectory Optimization of Hypersonic Vehicle Based on Multi-Strategy Improved WOA Optimized Attention-LSTM Network][research_dai_cai_2026]
- [Dai and Wang, 2016, Recognition of warheads based on features of range profiles in ballistic missile defense][research_dai_wang_2016]
- [Dai and Xia, 2016, Sliding mode trajectory tracking for mars atmospheric entry based on extended state observer][research_dai_xia_2016]
- [Dai and Xia, 2016, Trajectory Tracking for Mars Atmospheric Entry Based on High-Order Sliding Mode Control][research_dai_xia_2016_b]
- [Dajun and others, 2006, Aeroheating Wind Tunnel Test And Thermal Protection System Design For Hypersonic Vehicle][research_dajun_guobiao_2006]
- [Dalle and Driscoll, 2012, Continuous Differentiation of Complex Systems Applied to a Hypersonic Vehicle][research_dalle_driscoll_2012]
- [Dalle and others, 2010, Hypersonic Vehicle Flight Dynamics with Coupled Aerodynamic and Reduced-Order Propulsive Models][research_dalle_frendreis_2010]
- [Dalle and others, 2011, Flight Envelope Calculation of a Hypersonic Vehicle Using a First Principles-Derived Model][research_dalle_torrez_2011]
- [Dalle and others, 2011, Turn Performance of an Air-Breathing Hypersonic Vehicle][research_dalle_torrez_2011_b]
- [Dalle and others, 2014, Minimum-Fuel Ascent of a Hypersonic Vehicle Using Surrogate Optimization][research_dalle_torrez_2014]
- [Dan and others, 2022, A Real-time Adaptive Filtering Algorithm for Reentry Maneuvering][research_dan_xi_2022]
- [Dang and others, 2021, Aerodynamic design optimization of a hypersonic rocket sled deflector using the free-form deformation technique][research_dang_li_2021]
- [DANIEL and MILTON, 1980, A drag and stability analysis of hypersonic spin stabilized projectiles][research_daniel_milton_1980]
- [Danush Datthathireyan and others, 2025, CFD Analysis of Re-Entry Vehicle at Hypersonic Speed Using Ansys Fluent][research_danushdatthathireyan_balaji_2025]
- [Daoguang Tang and others, 2016, Comparative analysis of the classic ground attack terminal guidance laws][research_daoguangtang_huiwang_2016]
- [Das and others, 2009, Robust Partial Integrated Guidance and Control of Interceptors in Terminal Phase][research_das_chawla_2009]
- [Das and others, 2023, Reentry trajectory design of a hypersonic vehicle based on reinforcement learning][research_das_pei_2023]
- [Das and others, 2024, Hypersonic vehicle reentry trajectory design based on reinforcement learning][research_das_wang_2024]
- [David O. Sigthorsson, 2006, Tracking with Steady-State Optimization an Application to Air-Breathing Hypersonic Vehicle Control][research_davidosigthorsson_2006]
- [DAVIES and others, 1984, Aerothermodynamic heating analysis of aerobraking and aeromaneuvering orbital-transfer vehicles][research_davies_wilson_1984]
- [DAVIS, 1966, Radiative vs ablative heat shield concepts for manned lifting entry vehicles][research_davis_1966]
- [DAVIS, 1969, Thermal protection system optimization][research_davis_1969]
- [De Filippis and others, 2005, Numerical-Experimental Correlation of Stagnation Point Heat Flux in High Enthalpy Hypersonic Wind Tunnel][research_defilippis_savino_2005]
- [De Filippis and others, 2016, Terminal Entry Phase Trajectory Generator for Reusable Launch Vehicles][research_defilippis_kerr_2016]
- [De Geyter and others, 1974, INFLUENCE OF LEADING EDGE GEOMETRY ON UPSTREAM DENSITY DISTURBANCES IN HYPERSONIC FLOW][research_degeyter_smolderen_1974]
- [De Geyter, 1973, A Modulation Technique for Measuring Small Disturbances in the Upstream Flow Field of a Sharp Leading Edge in a Rarefied Hypersonic Flow][research_degeyter_1973]
- [de Moura and Ribeiro, 2026, Aerodynamic and Dynamic Analysis of a Hypersonic Waverider with a Coupled Dynamic-Thermodynamic Model][research_demoura_ribeiro_2026_b]
- [de Moura and Ribeiro, 2026, Thermodynamic-Dynamic coupling and exergy analysis during transient maneuvers of a hypersonic vehicle][research_demoura_ribeiro_2026_c]
- [de Moura and Ribeiro, 2026, Transient thermodynamic-dynamic modeling and exergy analysis of a waverider hypersonic vehicle][research_demoura_ribeiro_2026]
- [de Pasquale and others, 2009, ATV Jules Verne reentry observation Mission design and trajectory analysis][research_depasquale_francillout_2009]
- [de Pena and others, 1986, Application of Trajectory Analysis to the Assessment of Local and Long-Range Contributions to Acidic Deposition][research_depena_rolph_1986]
- [De Prisco and others, 2026, Aerothermodynamic response of ZrB2-based compositionally complex ultra-high-temperature ceramics in hypersonic and supersonic flow conditions][research_deprisco_mungiguerra_2026]
- [De Vanna and others, 2022, Multi-Objective RANS Aerodynamic Optimization of a Hypersonic Intake Ramp at Mach 5][research_devanna_bof_2022]
- [DE VIRGILIO and others, 1973, Optimal guidance for aerodynamically controlled reentry vehicles][research_devirgilio_wells_1973]
- [De Vita and others, 2015, Assessment of Hypersonic Flights Operation Scenarios Analysis of Launch and Reentry Trajectories, and Derived Top Level Vehicle System and Support Infrastructure Concepts and Requirements][research_devita_viola_2015]
- [De Zaiacomo and others, 2009, Robust Skip Entry Guidance and Control for a Capsule Returning from Lunar Orbit][research_dezaiacomo_kerr_2009]
- [De-qing and others, 2019, Research on Integrated Design of Guidance and Control for Hypersonic Vehicle Based on Trajectory Linearization Control Method][research_deqing_yiyin_2019]
- [De-qing and others, 2021, Research on Sensor Layout Optimization Design of Elastic Hypersonic Vehicle Based on Phase Stability Criteria][research_deqing_yiyin_2021]
- [Dean and others, 2023, Multidisciplinary Design Analysis and Optimization of a Hypersonic Inflatable Aerodynamic Decelerator][research_dean_robertson_2023]
- [DeBardelaben and others, 2022, Creation of a Powered Trimmed Aerodynamic Database for a Generic Hypersonic Vehicle][research_debardelaben_dehay_2022]
- [Dec and Mitcheltree, 2002, Probabilistic design of a Mars Sample Return Earth entry vehicle thermal protection system][research_dec_mitcheltree_2002]
- [DeChant and Wagnild, 2020, Local Laminar Flow Shear and Heat Transfer Solutions for Reduced Order Reentry Simulation][research_dechant_wagnild_2020]
- [Decker and Laschka, 2001, Unsteady aerodynamics of a hypersonic vehicle during a separation phase][research_decker_laschka_2001]
- [Decker, 2010, Unstructured Adaptive Grid Techniques Applied to a Hypersonic Re-Entry Vehicle][research_decker_2010]
- [Deep and Jagadeesh, 2018, Aerothermodynamic effects of controlled heat release within the hypersonic shock layer around a large angle blunt cone][research_deep_jagadeesh_2018]
- [Deepak and others, 2006, Nose Cone Design Optimization for a Hypersonic Flight Experiment Trajectory][research_deepak_ray_2006]
- [Deepak and others, 2008, Evolutionary Algorithm Shape Optimization of a Hypersonic Flight Experiment Nose Cone][research_deepak_ray_2008]
- [DEGELSMITH and others, 1993, Cost methodology for a responsive launch vehicle system][research_degelsmith_freaner_1993]
- [DeGregoria, 2015, Creep and Oxidation of Hafnium Diboride Based Ultra High Temperature Ceramics at 1500C][research_degregoria_2015]
- [DeJarnette and others, 2008, New Method for Computing Convective Heating in Stagnation Region of Hypersonic Vehicles][research_dejarnette_hamilton_2008]
- [DeJarnette, 1992, Approximate Two Layer Inviscid/Viscous Methods to Model Aerothermodynamic Environments][research_dejarnette_1992]
- [Dendy and others, 2026, Design and Performance Analysis of Tachyon A Low-Altitude Hypersonic Glide Vehicle][research_dendy_hayes_2026]
- [Deng and others, 2016, Analysis and design of terminal guidance with large angular on a saucer-shaped UAV][research_deng_wu_2016]
- [Deng and others, 2017, Overall Performance Analysis-Oriented Aerodynamic Configuration Optimization Design for Hypersonic Vehicles][research_deng_jiao_2017]
- [Deng and others, 2025, Aerodynamic configuration parametrization and optimization of high-speed gliding vehicle][research_deng_xu_2025]
- [Deng and others, 2025, Hypersonic Vehicle Trajectory Planning Method Based on Sequential Convex Programming][research_deng_zhao_2025]
- [Deng and Zhao, 2026, High-precision trajectory planning method for hypersonic glide vehicles based on sequential convex optimization][research_deng_zhao_2026]
- [Deng, 2026, Hypersonic glide trajectory planning with sequential convex optimization and hp pseudospectral discretization][research_deng_2026]
- [DERIENZO and PALLONE, 1967, Addendum Wonvective Stagnation-Point Heating for Re-Entry Speeds up to 70,000 fps Including Effects of Large Blowing Rates"][research_derienzo_pallone_1967_b]
- [DERIENZO and PALLONE, 1967, Convective stagnation-point heating for re- entry speeds up to 70,000 fps including effects of large blowing rates][research_derienzo_pallone_1967]
- [Derollez and others, 2021, Robust Entry Vehicle Guidance with Sampling-Based Invariant Funnels][research_derollez_cleach_2021]
- [Desai and Knocke, 2004, Mars Exploration Rovers Entry, Descent, and Landing Trajectory Analysis][research_desai_knocke_2004]
- [Desai and others, 2019, Probing Real Gas and Leading-Edge Bluntness Effects on Shock Wave Boundary-Layer Interaction at Hypersonic Speeds][research_desai_brahmachary_2019]
- [DEWELL and SPEYER, 1993, An investigation of the fuel-optimal periodic trajectories of a hypersonic vehicle][research_dewell_speyer_1993]
- [Deyang and Kun, 2016, Numerical Simulation and Analysis of Hypersonic Vehicle Plasma Sheath][research_deyang_kun_2016]
- [DEYST and others, 1971, Optimal lateral guidance for low L/D shuttle vehicle entry][research_deyst_gustafson_1971]
- [DEYST and others, 1972, Optimal lateral guidance for low L/D shuttle vehicle entry][research_deyst_gustafson_1972]
- [Di Clemente and Marini, 2011, Aerothermodynamic Design of the Expert Open Flap Assembly Plasma Test][research_diclemente_marini_2011]
- [Di Clemente and others, 2006, Numerical prediction of aerothermodynamic effects on a reentry vehicle body flap configuration][research_diclemente_marini_2006]
- [Di Clemente and others, 2009, Numerical prediction of aerothermodynamic effects on a re-entry vehicle body flap configuration][research_diclemente_marini_2009]
- [Di Giorgio and others, 2019, An aerothermodynamic design optimization framework for hypersonic vehicles][research_digiorgio_quagliarella_2019]
- [Diao and others, 2022, Research on Guidance Method of Hypersonic Vehicle Based on Reinforcement Learning and Dynamic Surface Control][research_diao_lu_2022]
- [Dickeson and others, 2009, Decentralized Control of an Airbreathing Scramjet-Powered Hypersonic Vehicle][research_dickeson_rodriguez_2009]
- [Dicristina, 1979, Hypersonic Heat Transfer Test Program in the VKI Longshot Facility][research_dicristina_1979]
- [Diebold and Scahill, 1985, Ablative Pyrolysis of Biomass in Solid-Convective Heat Transfer Environments][research_diebold_scahill_1985]
- [Dijkstra and others, 2013, Trajectory Optimization to Support the Study of Hypersonic Aerothermodynamic Phenomena][research_dijkstra_mooij_2013]
- [DILLEY and NEREM, 1969, An analysis of reentry flight measurements of shock layer microwave radiation][research_dilley_nerem_1969]
- [Ding and Jiang, 2016, Simulation of data-link networks used in cooperative terminal guidance][research_ding_jiang_2016]
- [Ding and others, 2015, Comparison between novel waverider generated from flow past a pointed von Karman ogive and conventional cone-derived waverider][research_ding_shen_2015_b]
- [Ding and others, 2015, Influence of surface pressure distribution of basic flow field on shape and performance of waverider][research_ding_shen_2015]
- [Ding and others, 2015, Novel inlet-airframe integration methodology for hypersonic waverider vehicles][research_ding_liu_2015]
- [Ding and others, 2015, Simplified Osculating Cone Method for Design of a Waverider][research_ding_liu_2015_b]
- [Ding and others, 2016, Multi-objective optimization of reentry trajectory for Hypersonic Gliding Vehicle][research_ding_guo_2016]
- [Ding and others, 2018, An overview of waverider design concept in airframe/inlet integration methodology for air-breathing hypersonic vehicles][research_ding_liu_2018]
- [Ding and others, 2019, Global smooth sliding mode controller for flexible air-breathing hypersonic vehicle with actuator faults][research_ding_wang_2019]
- [Ding and others, 2020, The Application of CI-CSCKF Fusion in Tracking the Mid-Course of Boost-Glide Vehicles][research_ding_wu_2020]
- [DING and others, 2022, Review of control and guidance technology on hypersonic vehicle][research_ding_yue_2022]
- [Ding and others, 2023, Anti-Disturbance Continuous Fixed-Time Controller Design for Air-breathing Hypersonic Vehicle][research_ding_li_2023]
- [Ding and others, 2023, Hypersonic Vehicle Trajectory Prediction Algorithm Incorporating Multiple Attention and Coding-Decoding Structures][research_ding_zhou_2023]
- [Ding and others, 2025, A Robust Control Method for the Trajectory Tracking of Hypersonic Unmanned Flight Vehicles Based on Model Predictive Control][research_ding_xu_2025]
- [Dinkelmann and others, 2002, Modelling of Heat Transfer and Vehicle Dynamics for Thermal Load Reduction by Hypersonic Flight Optimization][research_dinkelmann_wchter_2002]
- [Dix and others, 1967, LIFTING REENTRY COMMUNICATIONS. VOLUME 3 PLANE WAVE ATTENUATION TABLES][research_dix_golden_1967]
- [Djanal-Mann and Murugan, 2025, Application of PID Control to Hypersonic Vehicle Control Surfaces][research_djanalmann_murugan_2025]
- [Dobrov and others, 2023, Simulation of high-temperature flowfield around hypersonic waverider using graphics processor units][research_dobrov_karpenko_2023]
- [Dodge and others, 2026, A Comparative Evaluation of Engineering-Level and RANS-Based Aerodynamic Models on the Flight Dynamics of a Generic Hypersonic Vehicle][research_dodge_lindorfer_2026]
- [DOLAN and others, 1966, Elastomeric thermal shield systems for lifting reentry vehicles][research_dolan_edighoffer_1966]
- [DOLAN, 1970, Refurbishable ablative thermal protection system concepts for a multi-mission lifting entry vehicle][research_dolan_1970]
- [Donaldson and Ireland, 2017, A Panel Method Aerodynamic Preprocessor for Planetary Entry Trajectory Simulations][research_donaldson_ireland_2017]
- [Dong and Cai, 2017, Reentry Trajectory Optimization for Hypersonic Glide Vehicle with Flexible Initial Conditions][research_dong_cai_2017]
- [Dong and others, 2012, Rapid Constrained Trajectory Planning for Entry Vehicles][research_dong_chao_2012_b]
- [Dong and others, 2012, Rapid Three-Dimensional Constrained Trajectory Generation for Near Space Hypersonic Vehicles][research_dong_chao_2012]
- [Dong and others, 2014, Finite-time stabilization-based trajectory tracking under disturbances for entry vehicles][research_dong_wang_2014]
- [Dong and others, 2020, Barrier Lyapunov function based adaptive finite-time control for hypersonic flight vehicles with state constraints][research_dong_liu_2020]
- [Dong and others, 2021, Robust Trajectory Planning for Hypersonic Glide Vehicle with Parametric Uncertainties][research_dong_guo_2021]
- [Dong and others, 2022, Constrained Integrated Guidance and Control Scheme for Strap-Down Hypersonic Flight Vehicles with Partial Measurement and Unmatched Uncertainties][research_dong_xu_2022]
- [Dong and others, 2023, Adaptive nonsingular fixed-time control for hypersonic flight vehicle considering angle of attack constraints][research_dong_li_2023]
- [Dong and others, 2023, Constrained Reentry Trajectory Design using Whale Optimization Algorithm for Hypersonic Glide Vehicle][research_dong_huang_2023]
- [Dong and others, 2023, Digital twin-assisted multiscale residual-self-attention feature fusion network for hypersonic flight vehicle fault diagnosis][research_dong_jiang_2023]
- [Dong and others, 2024, Global wavelet-integrated residual frequency attention regularized network for hypersonic flight vehicle fault diagnosis with imbalanced data][research_dong_jiang_2024]
- [Dong and others, 2024, Sequential convex programming without penalty function for reentry trajectory optimization problem][research_dong_xie_2024]
- [Dong and others, 2025, Hypersonic flight vehicle intelligent fault diagnosis with imbalance data][research_dong_jiang_2025]
- [Dong and others, 2025, Integrated Trajectory Optimization for Deorbit-Reentry of Re-Entry Spacecraft][research_dong_wu_2025]
- [Dong and others, 2025, Observer Based Fixed-Time Tracking Control for Hypersonic Gliding Vehicle][research_dong_zhao_2025]
- [Dongdong and others, 2026, Predictor-Corrector Guidance for Hypersonic Morphing Vehicle][research_dongdong_xun_2026]
- [Doolan, 2006, An Air-Launched Hypersonic Vehicle Performance Study][research_doolan_2006]
- [Doronzo, 2026, Trajectory Optimisation and Manoeuvrability Trade-Offs for Hypersonic Glide Vehicles in Contested Atmospheric Re-Entry][research_doronzo_2026]
- [Dou and others, 2013, Simulation Analysis of Viscous Effects on Dynamic Performance of Hypersonic Vehicle][research_dou_shen_2013]
- [Dou and others, 2017, Modeling and nonlinear control for air-breathing hypersonic vehicle with variable geometry inlet][research_dou_su_2017]
- [Douglas and Lindgren, 1999, Hypersonic Weapons Technology for the Time Critical Mobile Ground Threat A State-of-the-Art Review][research_douglas_lindgren_1999]
- [Doustdar and others, 2018, Aero-heating modelling on the ablative noses during flight trajectory][research_doustdar_mardani_2018]
- [DRAPER and others, 1977, A flight research vehicle to bridge shuttle and hypersonic aircraft technology][research_draper_lanejr_1977]
- [DRAWIN, 1993, ChemInform Abstract Atmospheric Reentry Degradation of Thermal Protection Shield Materials][research_drawin_1993]
- [Dreyer and others, 2021, Rapid Steady-State Hypersonic Aerothermodynamic Loads Prediction Using Reduced Fidelity Models][research_dreyer_grier_2021]
- [DROUGGE, 1965, NOTE ON THE FLOW OF A VISCOUS INCOMPRESSIBLE FLUID AROUND A SHARP LEADING EDGE][research_drougge_1965]
- [DSOUZA and MOLDER, 1971, A time-dependent method for blunt leading edge hypersonic internal flow][research_dsouza_molder_1971]
- [Du and others, 2017, Robust Aeroelastic Design Optimization of Hypersonic Vehicle with Uncertainties in Aerodynamic Loads, Heat Flux, and Structure][research_du_wan_2017]
- [Du and others, 2023, Finite-Time Dynamic Sliding Mode Control for Non-Minimum Phase Hypersonic Vehicle][research_du_wang_2023]
- [Du and others, 2024, Research on Aerodynamic Shape Design of Wings of Hypersonic Aircrafts][research_du_qi_2024]
- [Du and others, 2026, Trajectory prediction of hypersonic glide vehicles based on dual-branch attention-TCN-GRU network][research_du_li_2026]
- [Duan and Li, 2012, Progress in control approaches for hypersonic vehicle][research_duan_li_2012]
- [Duan and Li, 2015, Artificial bee colony-based direct collocation for reentry trajectory optimization of hypersonic vehicle][research_duan_li_2015]
- [Duan and others, 2010, Aerodynamic Coefficients Models of Hypersonic Vehicle Based on Aero Database][research_duan_sun_2010]
- [Duan and others, 2011, Obstacle avoidance trajectory optimization of hypersonic vehicle][research_duan_sun_2011]
- [Duan and others, 2016, Trajectory Tracking and Online Replanning for Mars Entry][research_duan_roviranavarro_2016]
- [Duan and others, 2024, Study on the hypersonic separation of the parallel configuration of the combined cycle two-stage orbit vehicle][research_duan_xu_2024]
- [Duan and others, 2026, Multifidelity Data Fusion Method for Aerodynamic Heating Prediction of Hypersonic Vehicles][research_duan_zhao_2026]
- [Duan and Zhang, 2016, Direct parametric control-oriented model transformations for a hypersonic vehicle][research_duan_zhang_2016]
- [Duan and Zhong, 2010, Parametric autopilot design for an air-breathing hypersonic vehicle][research_duan_zhong_2010]
- [Dubey and others, 2020, Design, Prototyping, and Performance Qualification of Thermal Protection Systems for Hypersonic Space Vehicles][research_dubey_mukhopadhyay_2020]
- [Dubois-Matra and Bishop, 2003, Tracking and Identification of a Maneuvering Reentry Vehicle][research_duboismatra_bishop_2003]
- [Dudar and Timoshenko, 2025, Air-Space and Hypersonic Aircraft Design][research_dudar_timoshenko_2025]
- [Dudin and Ledovskiy, 2013, Hypersonic boundary layer in the vicinity of a point of inflection of leading edge on a flat wing in the regime of strong viscous interaction][research_dudin_ledovskiy_2013]
- [Dudin and Ledovskiy, 2020, ASYMPTOTIC SOLUTIONS TO HYPERSONIC BOUNDARY LAYER EQUATIONS ON A FLAT WING WITH A POINT OF INFLECTION ON THE LEADING EDGE][research_dudin_ledovskiy_2020]
- [Dudin and Neiland, 1980, Heat transfer in the neighborhood of a point of inflection in the leading edge of a plate in hypersonic flight][research_dudin_neiland_1980]
- [DULIKRAVICH and LEE, 1990, Aerodynamic shape optimization of hypersonic missiles][research_dulikravich_lee_1990]
- [DULIKRAVICH and SHEFFER, 1992, Aerodynamic shape optimization of hypersonic configurations including viscous effects][research_dulikravich_sheffer_1992]
- [Duncan, 1968, Guidance and Control for Atmospheric Entry][research_duncan_1968]
- [Dunning, 2016, Washington Public Ports Association Marine Terminal AKART and ISGP Corrective Action Guidance Manual][research_dunning_2016]
- [Duran and Zeng, 2026, An Automated Design-to-CFD Workflow for Hypersonic Waverider Analysis][research_duran_zeng_2026]
- [Duret and Fabrizi, 1999, VEGA, a small launch vehicle][research_duret_fabrizi_1999]
- [Dusinberre, 1958, Discussion "Transient Temperature and Thermal Stresses in Skin of Hypersonic Vehicle With Variable Boundary Conditions" Chen, Shih-Yuan, 1958, Trans. ASME, 80, pp. 1389-1394][research_dusinberre_1958]
- [Duston and others, 2004, Strength Enhancement and Application Development of Carbon Foam for Thermal Protection Systems][research_duston_seghi_2004]
- [Dutta and Braun, 2010, Mars Entry, Descent, and Landing Trajectory and Atmosphere Reconstruction][research_dutta_braun_2010]
- [Dyakonov and others, 2012, Hypersonic and Supersonic Static Aerodynamics of Mars Science Laboratory Entry Vehicle][research_dyakonov_schoenenberger_2012]
- [Eakins and others, 2010, Toward Oxidation-Resistant ZrB2-SiC Ultra High Temperature Ceramics][research_eakins_jayaseelan_2010]
- [Ebrahimi and others, 2011, Multidisciplinary Design Optimization Approach for a Small Solid Propellant Launch Vehicle Conceptual Design Using Hybrid Simulated Annealing][research_ebrahimi_roshanian_2011]
- [EDQUIST and LEWIS, 1993, Waverider-based hypersonic projectiles][research_edquist_lewis_1993]
- [Edquist, 2006, Computations of Viking Lander Capsule Hypersonic Aerodynamics with Comparisons to Ground and Flight Data][research_edquist_2006]
- [EDWARDS and BABIKIAN, 1987, Volume interchange factors for hypersonic vehicle wake radiation][research_edwards_babikian_1987]
- [Eggers and others, 1995, Aerodynamic off-design behavior of integrated waveriders from take-off up to hypersonic flight][research_eggersohmeyerd_nickel_1995]
- [Eggers and others, 2009, Aerodynamic Design of Hypersonic Re-Entry Flight HIFiRE 7][research_eggers_silvester_2009]
- [Ehsan and others, 2026, Data-Driven Design of Single-Phase High-Entropy Ultra-High-Temperature Ceramics][research_ehsan_castellanos_2026]
- [Eickmans, 2015, Re-Entry Trajectory Analysis Prediction of Uncontrolled Atmospheric Re-entry of Orbital Objects under Operational Aspects][research_eickmans_2015]
- [Eisler and Hull, 1993, Guidance law for planar hypersonic descent to a point][research_eisler_hull_1993]
- [Eisler and Hull, 1994, Guidance law for hypersonic descent to a point][research_eisler_hull_1994]
- [Eklund, 2004, Quicksat A Two Stage to Orbit Reusable Launch Vehicle Utilizing Air Breathing Propulsion for Responsive Space Access][research_eklund_2004]
- [El-Kebir and Ornik, 2020, In-Flight Air Density Estimation and Prediction for Hypersonic Flight Vehicles][research_elkebir_ornik_2020]
- [ELLINWOOD, 1970, Streamlining vehicles for high-altitude hypersonic flight][research_ellinwood_1970]
- [ELLIOTT and HANKEY, 1968, Hypersonic lifting body optimization][research_elliott_hankey_1968]
- [Elmnefi, 2026, Heat Flux Measurements in Stagnation-Point Methane Flames Using LED-Based Thermographic Phosphor Thermometry][research_elmnefi_2026]
- [Elsen and others, 2008, Large calculation of the flow over a hypersonic vehicle using a GPU][research_elsen_legresley_2008]
- [Emery and Devos, 2006, Acoustic attenuation measurements in transparent materials in the hypersonic range by picosecond ultrasonics][research_emery_devos_2006]
- [Engel and others, 2021, Configuration Options for Hypersonic Flaps for Mars Entry Systems][research_engel_skolnik_2021]
- [Engel and others, 2024, Assessment of Control Algorithms for Mars Entry Vehicles with Flap-Based Trajectory Control][research_engel_putnam_2024]
- [Engel and Putnam, 2025, Optimal Range Capabilities for Low-Lift-to-Drag Ratio Mars Entry Vehicles][research_engel_putnam_2025]
- [Enmi and others, 2018, Accurate predictor-corrector skip entry guidance for low lift-to-drag ratio spacecraft][research_enmi_qian_2018]
- [Erdem and others, 2009, Drag Reduction by Energy Deposition in Hypersonic Flows][research_erdem_yang_2009]
- [ERICSSON, 1970, α-EFFECTS ARE NEGLIGIBLE IN HYPERSONIC UNSTEADY AERODYNAMICS-FACT OR FICTION?][research_ericsson_1970]
- [ERICSSON, 1978, Nonlinear hypersonic viscous crossflow effects on slender vehicle dynamics][research_ericsson_1978]
- [Ericsson, 1979, Nonlinear Hypersonic Viscous Crossflow Effects on Slender Vehicle Dynamics][research_ericsson_1979]
- [Ermakov and Kryukov, 2017, Supercomputer modeling of flow past hypersonic flight vehicles][research_ermakov_kryukov_2017]
- [Erwin and Bernstein, 2005, Spacecraft Trajectory Estimation Using a Sampled-Data Extended Kalman Filter with Range-Only Measurements][research_erwin_bernstein_2005]
- [ERWIN, 1990, Personnel launch system PLS lifting body and low lift-to-drag L/D][research_erwin_1990]
- [Escher and Ehrlic, 2000, An early TSTO fully reusable vehicle design used to 'calibrate' Stage 1 combined-cycle hypersonic propulsion systems][research_escher_ehrlic_2000]
- [Evans and Walton, 2017, Aerodynamic optimisation of a hypersonic reentry vehicle based on solution of the Boltzmann-BGK equation and evolutionary optimisation][research_evans_walton_2017]
- [Ewans and Collins, 2024, A Comparison of Wave Directional Spreading Measurements Made With a Spotter Buoy and a Directional Waverider Buoy in Parallel][research_ewans_collins_2024]
- [Ewenz Rocher and others, 2022, Correlation for Species Concentration on a Hypersonic Stagnation Point with Mass Injection][research_ewenzrocher_hermann_2022]
- [Eyi and others, 2018, Aerothermodynamic Design Optimization of Hypersonic Vehicles][research_eyi_hanquist_2018]
- [Eyi and others, 2019, Aerothermodynamic Design Optimization of Hypersonic Vehicles][research_eyi_hanquist_2019]
- [Eyi and Yumusak, 2012, Design Optimization in Hypersonic Flows][research_eyi_yumusak_2012]
- [Eyi and Yumuşak, 2014, Aerothermodynamic shape optimization of hypersonic blunt bodies][research_eyi_yumusak_2014]
- [Eyi, 2013, Aerothermodynamic Design Optimization in Hypersonic Flows][research_eyi_2013]
- [Fahrenholtz and Hilmas, 2017, Ultra-high temperature ceramics Materials for extreme environments][research_fahrenholtz_hilmas_2017]
- [Fahrenholtz and others, 2009, Design of Ultra-High Temperature Ceramics for Improved Performance][research_fahrenholtz_hilmas_2009]
- [Fahy and others, 2019, Development of Nanocomposite Thermoset Ablative for High Heat Flux Applications][research_fahy_koo_2019]
- [Fain and others, 2026, VORTEX, an Operational Spaceplane and Hypersonic Vehicle Program][research_fain_lambert_2026]
- [Fairfax and others, 2020, Trajectory Shaping for Quasi-Equilibrium Glide in Guided Munitions][research_fairfax_vasile_2020]
- [Falempin and others, 1995, Reference and generic vehicle for the French Hypersonic Technology Program][research_falempin_lacaze_1995]
- [Falkiewicz and others, 2009, Thermoelastic Formulation of a Hypersonic Vehicle Control Surface for Control-Oriented Simulation][research_falkiewicz_cesnik_2009]
- [Falkiewicz and others, 2010, Reduced-Order Aerothermoelastic Framework for Hypersonic Vehicle Control Simulation][research_falkiewicz_cesnik_2010]
- [Falkiewicz and others, 2011, Effect of Control Surface-Fuselage Inertial Coupling on Hypersonic Vehicle Flight Dynamics][research_falkiewicz_frendreis_2011]
- [Falkiewicz and others, 2011, Reduced-Order Aerothermoelastic Framework for Hypersonic Vehicle Control Simulation][research_falkiewicz_cesnik_2011]
- [Famularo and others, 2016, Enforcing State Constraints on a Model of a Hypersonic Vehicle][research_famularo_valasek_2016]
- [Fan and others, 2009, Experimental Investigation of Aerodynamic Characteristics of Hypersonic Airframe-Engine Integrated Vehicle][research_fan_liu_2009]
- [Fan and others, 2016, A Cost-Effective Tracking Algorithm for Hypersonic Glide Vehicle Maneuver Based on Modified Aerodynamic Model][research_fan_zhu_2016]
- [Fan and others, 2017, A Hybrid Model Algorithm for Hypersonic Glide Vehicle Maneuver Tracking Based on the Aerodynamic Model][research_fan_lu_2017]
- [Fan and others, 2017, Design of Lateral Control System for a Hypersonic Cruise missile][research_fan_wu_2017]
- [Fan and others, 2021, Design and Verification of Attitude Control System for a Boost-Glide Rocket][research_fan_bai_2021]
- [Fan and others, 2021, Hypersonic Vehicle Trajectory Prediction Algorithm Based on Hough Transform][research_fan_jiajun_2021]
- [Fan and others, 2022, Dynamic Performance Test and System Identification of Air Rudder for Boost-Glide Aircraft][research_fan_bai_2022]
- [Fan and others, 2023, Hardware-in-the-Loop Simulation Test Method for the Inertial Navigation System of a Boost-Glide Rocket][research_fan_bai_2023]
- [Fan and others, 2024, An Optimization Method of Attitude Control Parameters Based on Genetic Algorithm for the Boost-Glide Rocket][research_fan_bai_2024]
- [Fan and others, 2024, Research progress and prospect of the hypersonic flight vehicle fault-tolerant control methods][research_fan_qi_2024]
- [Fang and others, 2024, Dynamic Modeling and Observer-Based Fixed-Time Backstepping Control for a Hypersonic Morphing Waverider][research_fang_li_2024]
- [Fang and others, 2024, TimeVAE-based Hypersonic Glide Vehicle Trajectory Generation Method and Evaluation][research_fang_jiang_2024]
- [Farajollahi and Markazi, 2010, PDC controller design for aircraft glide-slope trajectory tracking][research_farajollahi_markazi_2010]
- [Farmakovsky and others, 2005, Development of the Materials For Power-Generating Unit, Active Thermal Protection System and Hypersonic Flight Vehicle HFV Protecting Systems Against Electromagnetic, Radioactive and X-radiation][research_farmakovsky_vinogradova_2005]
- [Fatemi and others, 2005, Re-Entry Vehicle Design Optimization with Integrated Trajectory Uncertainties][research_fatemi_mooij_2005]
- [Fattahi and others, 2020, On the simulation of spark plasma sintered TiB2 ultra high temperature ceramics A numerical approach][research_fattahi_najafiershadi_2020]
- [Fay and Kemp, 1963, THEORY OF STAGNATION-POINT HEAT TRANSFER IN A PARTIALLY IONIZED DIATOMIC GAS][research_fay_kemp_1963]
- [Fedele and others, 2014, Online parameters estimation for reentry vehicle in the hypersonic regime][research_fedele_romagnoli_2014]
- [Fedele and others, 2020, Aerothermodynamics and thermal design for on-ground and in-flight testing of a deployable heat shield capsule][research_fedele_gardi_2020]
- [Fedioun and Orlik, 2012, Boundary Layer Transition on the LEA Hypersonic Vehicle Forebody][research_fedioun_orlik_2012]
- [Feie and Kretz, 2008, High Temperature Thermocouple Installation Methods for Hypersonic Vehicles][research_feie_kretz_2008]
- [Feilden and others, 2019, High temperature strength of an ultra high temperature ceramic produced by additive manufacturing][research_feilden_glymond_2019]
- [Fenfen and others, 2020, An Improved Auto-Disturbance Rejection Control Method for Hypersonic vehicle control system][research_fenfen_xubo_2020]
- [Feng and others, 2014, Aerodynamic configuration optimization by the integration of aerodynamics, aerothermodynamics and trajectory for hypersonic vehicles][research_feng_tang_2014]
- [Feng and others, 2017, Aerodynamic configuration design and optimization for hypersonic vehicles][research_feng_liu_2017]
- [Feng and others, 2017, Trajectory tracking for hypersonic glide vehicles based on improved sine-AIMM][research_feng_tan_2017]
- [Feng and others, 2019, Adaptive Fuzzy Sliding Mode Control for a Flexible Air-breathing Hypersonic Vehicle Based on Tracking Differentiator][research_feng_wang_2019]
- [Feng and others, 2020, Adaptive Radau pseudo-spectral optimization for descending trajectory of a hypersonic cruise vehicle][research_feng_lv_2020]
- [Feng and others, 2022, Event-Triggered Neural Adaptive Control for a Switched Model of Hypersonic Flight Vehicle][research_feng_wang_2022]
- [Feng and others, 2025, A Modeling Approach for the Balanced Gliding Trajectory of a Hypersonic Vehicle with Pneumatic Iteration][research_feng_bai_2025]
- [Feng and others, 2025, Aerodynamic-infrared integrated stealth design method of hypersonic glide vehicles][research_feng_long_2025]
- [Feng and others, 2025, Fast Entry Trajectory Planning Method for Wide-Speed Range UASs][research_feng_feng_2025]
- [Feng and others, 2026, Unsteady Aerodynamic Modeling and Longitudinal Adaptive Tracking Control for Hypersonic Vehicles with Sweep Variation][research_feng_wu_2026]
- [Feng and Zhang, 2016, Analysis of Near Space Hypersonic Glide Vehicle Trajectory Characteristics and Defense Difficulties][research_feng_zhang_2016]
- [Feng Li and others, 2016, Coupling characterization analysis and control system design of XK-2 waverider hypersonic vehicle][research_fengli_chaowang_2016]
- [Feng, 2011, Robust Adaptive Control Based on Specified Region Pole Assignment for Flexible Hypersonic Vehicle][research_feng_2011]
- [Feng, 2022, Switched Control of Hypersonic Vehicle based on Threshold Event-triggered Mechanism][research_feng_2022]
- [Fengyuan and Huang, 2017, A Preliminary Overview analysis on the Internal Waverider Inlets for Ramjet][research_fengyuan_huang_2017]
- [FERGUSON and ANDERSON, 1993, Expanding the waverider design space using general supersonic and hypersonic generating flows][research_ferguson_andersonjr_1993]
- [Ferguson and others, 2015, A Coupled Aerodynamic and Propulsive Performance Analysis of the Generic Hypersonic Vehicle][research_ferguson_dasque_2015_b]
- [Ferguson and others, 2015, The Design, Analysis and Performance Evaluation of Waverider Configurations for Hypersonic Vehicle Applications][research_ferguson_dasque_2015]
- [Ferguson and others, 2015, Waverider Design and Analysis][research_ferguson_dhanasar_2015]
- [Ferguson and others, 2016, Waverider Design, Analysis and Performance Evaluation][research_ferguson_dasque_2016]
- [Ferguson and others, 2018, An Aerodynamic Analysis of the Generic Hypersonic Vehicle][research_ferguson_dasque_2018]
- [Ferlemann and others, 2000, Developing conceptual hypersonic airbreathing engines using Design of Experiments methods][research_ferlemann_robinson_2000]
- [Ferraiuolo and Manc, 2011, A New Methodology to Preliminary Design Structural Components of Re-Entry and Hypersonic Vehicles][research_ferraiuolo_manc_2011]
- [Ferraiuolo and Manca, 2012, Heat transfer in a multi-layered thermal protection system under aerodynamic heating][research_ferraiuolo_manca_2012]
- [Ferretto and others, 2026, Optimization of Fuel Depletion Sequence for Trim Drag Minimization of a Commercial Hypersonic Aircraft Powered by Liquid Hydrogen][research_ferretto_gori_2026]
- [Ferrier and others, 2006, Boundary Layer Transition Prediction on a Hypersonic Vehicle Forebody][research_ferrier_fedioun_2006]
- [Ferrier and others, 2008, Transition Prediction of the 3D Boundary Layer Under an Hypersonic Vehicle Forebody][research_ferrier_orlik_2008]
- [Filatov, 1972, Optimum shape of lifting bodies for hypersonic velocities][research_filatov_1972]
- [Filipkovskyi, 2026, DEPENDENCE OF AERODYNAMIC DRAG AND HEAT FLUX ON THE BLUNTNESS DEGREE OF HYPERSONIC MISSILE FAIRINGS][research_filipkovskyi_2026]
- [FINK, 1966, Hypersonic minimum-drag slender bodies of revolution][research_fink_1966]
- [Finley and Cockrell, 1995, Control effectiveness and lateral-directional stability for two waverider-derived hypersonic cruise configurations][research_finley_cockrell_1995]
- [Finzi and others, 2003, Atmospheric Re-entry Trajectory Tracking and Control for an Unmanned Space Vehicle with a Lyapunov Approach][research_finzi_lavagna_2003]
- [Fiorentini and others, 2007, Nonlinear Robust/Adaptive Controller Design for an Air-Breathing Hypersonic Vehicle Model][research_fiorentini_serrani_2007]
- [Fiorentini and others, 2009, Nonlinear control of non-minimum phase hypersonic vehicle models][research_fiorentini_serrani_2009]
- [Fiorentini and Serrani, 2012, Adaptive restricted trajectory tracking for a non-minimum phase hypersonic vehicle model][research_fiorentini_serrani_2012]
- [Fischer and others, 2023, Determination of Kriging Model Parameters for Modeling of Computational Aerodynamic Euler Responses for a Generic Hypersonic Vehicle][research_fischer_johanik_2023]
- [Fitzgerald, 1974, On reentry vehicle tracking in various coordinate systems][research_fitzgerald_1974]
- [FLORENCE and HILTZ, 1968, Thermal protection systems for a Mars-entry vehicle][research_florence_hiltz_1968]
- [FLORENCE and others, 1978, Selection, development, characterization and flight test of a thermal protection system for an earth entry satellite vehicle][research_florence_thibault_1978]
- [FLORENCE, 1979, Selection of hypersonic L/D to minimize thermal protection system weight and meet cross range requirements Lift-Drag ratio][research_florence_1979]
- [FLORENCE, 1981, Aerothermodynamic design feasibility of a generic planetary aerocapture/aeromaneuver vehicle][research_florence_1981]
- [FLORENCE, 1981, Aerothermodynamic design feasibility of a Mars aerocapture/aeromaneuver vehicle][research_florence_1981_b]
- [Florence, 1985, Aerothermodynamic design feasibility of a Mars aerocapture vehicle][research_florence_1985]
- [Fogarty, 1967, R67-28 A General-Purpose Analog Translational Trajectory Program for Orbiting and Reentry Vehicles][research_fogarty_1967]
- [Folk and Ho, 2001, Micro-actuators for control of delta wing with sharp leading edge][research_folk_ho_2001]
- [Fomin and others, 2010, Skip trajectory flight of a ramjet-powered hypersonic vehicle][research_fomin_aulchenko_2010]
- [Fong and others, 1970, Propulsion Effects on Aerodynamic Characteristics of Lifting Reentry Vehicles][research_fong_ehrlich_1970]
- [Forbes-Spyratos and others, 2014, Inverse Simulation for Hypersonic Vehicle Analysis][research_forbesspyratos_jahn_2014]
- [Forsythe and others, 1961, HYPERSONIC UTILITY GLIDER THERMODYNAMIC ANALYSIS][research_forsythe_melfi_1961]
- [Foust and Smith, 2004, Small Launch Vehicle Services Supply and Demand Through 2010][research_foust_smith_2004]
- [Franze and Barz, 2025, Comparison of models for aerothermal load prediction using coupled trajectory simulations of a high lift reentry vehicle][research_franze_barz_2025]
- [Fratantoni, 2001, Adaptive Oceanographic Sampling in a Coastal Environment Using Autonomous Gliding Vehicles][research_fratantoni_2001_b]
- [Fratantoni, 2001, Autonomous Oceanographic Sampling Using Environmentally-Powered Gliding Vehicles][research_fratantoni_2001]
- [Fratantoni, 2002, Adaptive Oceanographic Sampling in a Coastal Environment Using Autonomous Gliding Vehicles][research_fratantoni_2002_b]
- [Fratantoni, 2002, Development of Oceanographic Sampling Networks Using Autonomous Gliding Vehicles][research_fratantoni_2002]
- [Fratantoni, 2003, Adaptive Oceanographic Sampling in a Coastal Environment Using Autonomous Gliding Vehicles][research_fratantoni_2003_b]
- [Fratantoni, 2003, Development of Oceanographic Sampling Networks Using Autonomous Gliding Vehicles][research_fratantoni_2003]
- [Frayssinet, 2019, Roll torque modeling of a hypersonic reentry vehicle Numerical analysis of cross-hatching phenomenon][research_frayssinet_2019]
- [Freeborn and others, 2005, The ROCKOT launch vehicle-the competitive launch solution for small Earth observation satellites into low Earth orbits][research_freeborn_kinnersley_2005]
- [Friz and Samareh, 2020, Parametric Cost Modeling of a Mid-Lift-to-Drag Ratio Vehicle for Human Mars Entry, Descent, and Landing][research_friz_samareh_2020]
- [Froning and others, 1996, Aerospace plane trajectory optimization for sub-orbital boost glide flight][research_froningjr_mckinney_1996]
- [Froning and Roach, 1999, Influence of EM discharges on hypersonic vehicle lift, drag, and airbreathing thrust][research_froningjr_roach_1999]
- [Froning and Roach, 2003, CFD Investigation of Hypersonic Drag Reduction and Thrust Increase by External Burning][research_froning_roach_2003_b]
- [Froning and Roach, 2003, Investigation of Hypersonic Drag Reduction and Thrust Increase by External Burning][research_froning_roach_2003]
- [Fruncillo and others, 2026, Navigation Algorithms of a Hypersonic Launch Vehicle][research_fruncillo_morani_2026]
- [Fu and others, 2017, An improved predictor-corrector entry guidance method for hypersonic flight vehicle][research_fu_liu_2017]
- [Fu and others, 2019, Ascent Trajectory Optimization for Hypersonic Vehicle Based on Improved Chicken Swarm Optimization][research_fu_wang_2019]
- [Fu and others, 2020, Thermal Expansion for Charring Ablative Materials][research_fu_weng_2020]
- [Fu and others, 2022, Multi-objective aerodynamic optimization of two-dimensional hypersonic forebody-inlet based on the heuristic algorithm][research_fu_qu_2022]
- [Fu and others, 2024, Adaptive Variable Structure Interacting Multiple Model Tracking Algorithm for Hypersonic Glide Vehicle][research_fu_wan_2024]
- [Fu and others, 2024, Flight trajectory optimization study of a variable-cycle turbine-based combined cycle engine hypersonic vehicle based on airframe/engine integration][research_fu_song_2024]
- [Fu and others, 2026, Integrated design method of the waverider forebody and inward-turning inlet based on genetic/gradient hybrid strategy][research_fu_gong_2026]
- [Fuhry, 1999, Adaptive atmospheric reentry guidance for the Kistler K-1 orbital vehicle][research_fuhry_1999]
- [Fujii and Inoue, 1998, Aerodynamic Heating Measurement on Afterbody of Hypersonic Flight Experiment][research_fujii_inoue_1998]
- [Fujii and Inoue, 1998, Aerodynamic heating measurement on ceramic tile region of Hypersonic Flight Experiment HYFLEX][research_fujii_inoue_1998_b]
- [Fujii and others, 2000, Aerodynamic heating measurements on nose and elevon of Hypersonic Flight Experiment vehicle][research_fujii_watanabe_2000]
- [Fujii and others, 2001, Aerodynamic Heating Measurements on Nose and Elevon of Hypersonic Flight Experiment Vehicle][research_fujii_watanabe_2001]
- [Fujio and Taguchi, 2026, Design exploration of hypersonic air-breathing vehicle including airframe and air inlet using deep-learning flowfield prediction][research_fujio_taguchi_2026]
- [Fujiwara and Funase, 2022, Autonomous Trajectory Guidance under Uncertain Dynamical Environment Using State Transition Tensors][research_fujiwara_funase_2022]
- [FUKUDA and others, 2017, Experimental Study to Estimate Heat Flux and Thermal Response Analysis on Rear Heat Shield of Super Orbital Reentry Calsule][research_fukuda_araya_2017]
- [Fukuzawa and others, 2025, Hypersonic Air-Breathing and Combined Cycle Propulsion, and Hypersonic Vehicle][research_fukuzawa_iguchi_2025]
- [Fuller and others, 2008, Topical Issue on Ultra-High-Temperature Ceramics][research_fuller_blum_2008]
- [Fuller and Sacks, 2004, Guest Editorial Ultra-high temperature ceramics][research_fuller_sacks_2004]
- [Fung, 1953, On the Behavior of a Sharp Leading Edge][research_fung_1953]
- [FUREY, 1970, Minimum energy hypersonic nose and leading edge shapes][research_furey_1970]
- [FUREY, 1972, Minimum-Energy Hypersonic Nose and Leading-Edge Shapes][research_furey_1972]
- [Furfaro and Wibben, 2012, Mars Atmospheric Entry Guidance via Multiple Sliding Surface Guidance for Reference Trajectory Tracking][research_furfaro_wibben_2012]
- [Fusaro and others, 2019, A methodology for preliminary sizing of a Thermal and Energy Management System for a hypersonic vehicle][research_fusaro_ferretto_2019]
- [Fusaro and others, 2022, Flight Control System Design and Sizing Methodology for hypersonic cruiser][research_fusaro_ferretto_2022_b]
- [Fusaro and others, 2022, Liquid Metals Heat-Pipe solution for hypersonic air-intake leading edge Conceptual design, numerical analysis and verification][research_fusaro_ferretto_2022]
- [Fusaro and Viola, 2020, Design and integration of a cryogenic propellant subsystem for the hypersonic STRATOFLY MR3 Vehicle][research_fusaro_viola_2020]
- [Fusco and others, 2026, A Sub Orbital Hypersonic Vehicle Preliminary Structural Sizing][research_fusco_trinchese_2026]
- [Gabaldo and others, 2016, Aerothermodynamic simulation model for new hypersonic propulsion Rocket Ignited Supersonic Combustion Ram Jet][research_gabaldo_barros_2016]
- [GAI and others, 1985, Stagnation point heat transfer in hypersonic high enthalpy flow][research_gai_baird_1985]
- [Gaillard and others, 1999, Smooth leading edge transition in hypersonic flow][research_gaillard_benard_1999]
- [Galaktionov and others, 2006, Aerodynamic features of the hypersonic re-entry leg of Kliper type vehicle][research_galaktionov_lapygin_2006]
- [Gally and Campbell, 2002, Constrained Aerothermodynamic Design of Hypersonic Vehicles][research_gally_campbell_2002]
- [GAMBLE and YOUNG, 1982, The development and application of aerodynamic uncertainties in the design of the entry trajectory and flight control system of the SpaceShuttle Orbiter][research_gamble_young_1982]
- [Gang and others, 2005, RLV Reentry Trajectory Multi-Objective Optimization Design Based on NSGA2 Algorithm][research_gang_min_2005]
- [Gangireddy and others, 2010, Liquid Oxide Flow during Oxidation of Zirconium Diboride-Silicon Carbide Ultra High Temperature Ceramics][research_gangireddy_karlsdottir_2010]
- [Gao and Jiang, 2015, A matching approach to communicate through the plasma sheath surrounding a hypersonic vehicle][research_gao_jiang_2015]
- [Gao and others, 1997, The attitude stabilization and trajectory tracking of reentry vehicle via variable-structure based control method][research_gao_chen_1997]
- [Gao and others, 2011, Trajectory Optimization in Reentry Phase for Hypersonic Gliding Vehicles Using Swarm Intelligence Algorithms][research_gao_wu_2011]
- [Gao and others, 2012, Aerodynamic optimization and evaluation for the three-dimensional afterbody/nozzle integrated configuration of hypersonic vehicles][research_gao_cui_2012]
- [Gao and others, 2012, Passive Fault-Tolerant Control Design for Near-Space Hypersonic Vehicle Dynamical System][research_gao_jiang_2012]
- [Gao and others, 2013, Adaptive neural control design for hypersonic aircraft using time scale separation][research_gao_wang_2013_d]
- [Gao and others, 2013, Robust tracking control for an air-breathing hypersonic vehicle with input constraints][research_gao_wang_2013_c]
- [Gao and others, 2014, Observer-based attitude control for hypersonic gliding vehicle][research_gao_li_2014]
- [Gao and others, 2014, Observer-based H-infinity tracking control design for a linearized hypersonic vehicle model with external disturbance][research_gao_cao_2014]
- [GAO and others, 2018, Gauss Pseudospectral Method Based Trajectory Optimization for Hypersonic Glide Vehicles][research_gao_chen_2018]
- [Gao and others, 2018, Offset-free trajectory tracking control for hypersonic vehicle under external disturbance and parametric uncertainty][research_gao_zhang_2018]
- [Gao and others, 2019, Hypersonic Periodic Cruise Trajectory Optimization Based on Flexible Use of Pseudo-spectral Method][research_gao_sun_2019]
- [Gao and others, 2019, Improved Tentacle-Based Guidance for Reentry Gliding Hypersonic Vehicle With No-Fly Zone Constraint][research_gao_cai_2019]
- [Gao and others, 2019, Reentry trajectory optimization based on Deep Reinforcement Learning][research_gao_shi_2019]
- [Gao and others, 2020, An efficient fast altitude control for hypersonic vehicle][research_gao_chen_2020_b]
- [Gao and others, 2020, General Periodic Cruise Guidance Optimization for Hypersonic Vehicles][research_gao_chen_2020]
- [Gao and others, 2021, A novel mechanical-thermal-electrical thermal protection system concept and its multi-scale performance evaluation for hypersonic launch vehicles][research_gao_gou_2021]
- [Gao and others, 2024, Numerical Simulation of Aerodynamic Pressure and Aerodynamic Heat on Stagnation Point and Wall of Hypersonic Double Cone Aircraft][research_gao_li_2024]
- [Gao and others, 2024, Trajectory tracking control of a flexible air-breathing hypersonic vehicle using Lyapunov-based model predictive control][research_gao_chen_2024]
- [Gao and others, 2026, Coupled Heat Transfer Analysis of Hypersonic Wide-Speed-Range Cruise Aircraft][research_gao_ai_2026]
- [Gao and others, 2026, Resilient Prescribed Performance Control for Hypersonic Morphing Flight Vehicle with Measurement Uncertainty][research_gao_liu_2026]
- [Gao and others, 2026, Shock Angle Characteristics and Test Analysis of Hypersonic Wide-Speed-Range Cruise Aircraft][research_gao_jia_2026]
- [Gao and Wang, 2013, Observer-based fault-tolerant control for an air-breathing hypersonic vehicle model][research_gao_wang_2013]
- [Gao and Wang, 2013, Reference command tracking control for an air-breathing hypersonic vehicle with parametric uncertainties][research_gao_wang_2013_b]
- [Gao, 2000, Long March Launch Vehicles Responsive to both Domestic and International Market][research_gao_2000]
- [Gao, 2023, A design review on hypersonic aerodynamics configurations and applicability to hypersonic transports][research_gao_2023]
- [Gaohua and others, 2014, Robust LPV autopilot design for hypersonic reentry vehicle][research_gaohua_jianmei_2014]
- [Garcia-Llama, 2007, Analytic Guidance for the First Entry in a Skip Atmospheric Entry][research_garciallama_2007]
- [Garcia-Llama, 2011, Analytic Development of a Reference Trajectory for Skip Entry][research_garciallama_2011]
- [Gardi and others, 2015, In-Flight Test of Ultra High Temperature Ceramic Materials on Scramspace][research_gardi_delvecchio_2015]
- [Garino and others, 2024, Scratch-Induced Wear Behavior of Multi-Component Ultra-High-Temperature Ceramics][research_garino_nisar_2024]
- [Garrard, 2015, Hypersonic Test Capabilities at AEDC's Aerodynamic and Propulsion Test Unit][research_garrard_2015]
- [Garvey and others, 2003, The Incremental Development of a Cost-Effective Small Launch Vehicle for Nanosat Payloads][research_garvey_besnard_2003]
- [GARVINE, 1964, Hypersonic viscous flow near a sharp leading edge][research_garvine_1964]
- [GARVINE, 1966, Shock wave transport effects on hypersonic leading edge flow][research_garvine_1966]
- [Garzon and Matisheck, 2012, Supersonic Testing of Natural Laminar Flow on Sharp Leading Edge Airfoils. Recent Experiments by Aerion Corporation][research_garzon_matisheck_2012]
- [Garzon, 2024, Survey of Aerospike and Aerodisk Technologies for Drag Reduction at Hypersonic Speeds][research_garzon_2024]
- [GASNER and others, 1992, Evaluation of thermal management for a Mach 5.5 hypersonic vehicle][research_gasner_foster_1992]
- [Gazzaniga and Palafox, 2001, Substernal thoracoscopic guidance during sternal reentry][research_gazzaniga_palafox_2001]
- [Ge and others, 2017, Segmented optimal design of ballistic trajectory of gliding extended range projectile subjected to multiple constraints][research_ge_wang_2017]
- [Gee and others, 2025, Examining the launch pad noise environment for a small-lift launch vehicle][research_gee_kellison_2025]
- [Geshele and others, 2013, Ways to increase the flight velocity of a hypersonic vehicle][research_geshele_polezhaev_2013]
- [Ghaffari and others, 1991, Transonic Navier-Stokes solutions about a generic hypersonic configuration][research_ghaffari_luckring_1991]
- [Ghori and others, 2023, Thermo-Structural Response Prediction of UHTCC Control Surface for Hypersonic Cruise Vehicle][research_ghori_narendar_2023]
- [Ghosh and Ogawa, 2022, Correction Design and Numerical Investigation of a Hypersonic Waverider based Entry, Descent, and Landing Architecture Assisted by Supersonic Retro-Propulsion][research_ghosh_ogawa_2022_b]
- [Ghosh and Ogawa, 2022, Design and Numerical Investigation of a Hypersonic Waverider based Entry, Descent, and Landing Architecture Assisted by Supersonic Retro-Propulsion][research_ghosh_ogawa_2022]
- [Ghosh and others, 2009, Room-temperature dislocation activity during mechanical deformation of polycrystalline ultra-high-temperature ceramics][research_ghosh_subhash_2009]
- [Ghosh and others, 2023, Effect of Leading Edge Bluntness on Aerothermal Characteristics of Osculating Cone Waveriders][research_ghosh_rao_2023]
- [Ghosh and others, 2025, Effect of Tip Curvature on the Aerodynamic Performance of an Osculating Cone Waverider][research_ghosh_rao_2025]
- [Giampetro and others, 2026, Characterization of Hypersonic Waverider Wake With Spectral Proper Orthogonal Decomposition][research_giampetro_lindau_2026]
- [Giampetro, 2026, Characterization of Hypersonic Waverider Wake at Zero Angle of Attack][research_giampetro_2026]
- [Gibbons and others, 2021, Flight Regime Limits of a Hypersonic Vehicle using Electron Transpiration Cooling][research_gibbons_damm_2021]
- [Gibson and others, 2002, Development and Flight Test of the X-43A-LS Hypersonic Configuration UAV][research_gibson_neidhoefer_2002]
- [Gillum and Lewis, 1996, Analysis of experimental results on a Mach 14 waverider with blunt leading edges][research_gillum_lewis_1996]
- [Gillum and others, 1994, Details of a Mach 14 waverider wind tunnel test][research_gillum_kammeyer_1994_b]
- [Gillum and others, 1994, Wind tunnel results for a Mach 14 waverider][research_gillum_kammeyer_1994]
- [Girerd and Barton, 2000, Next generation entry guidance - Onboard trajectory generation for unpowered drop tests][research_girerd_barton_2000]
- [Giri and Ghose, 2010, Differential Evolution Based Ascent Phase Trajectory Optimization for a Hypersonic Vehicle][research_giri_ghose_2010]
- [Gislason and Prahm, 1983, Sensitivity study of air trajectory long-range transport modelling][research_gislason_prahm_1983]
- [Gladden and Melis, 1994, Hypersonic Engine Leading Edge Experiments in a High Heat Flux, Supersonic Flow Environment][research_gladden_melis_1994]
- [GLADDEN and others, 1990, Thermal/structural analyses of several hydrogen-cooled leading-edge concepts for hypersonic flight vehicles][research_gladden_melis_1990]
- [Glass and Moss, 2001, Aerothermodynamic characteristics in the hypersonic continuum-rarefied transitional regime][research_glass_moss_2001]
- [Glass, 2008, Ceramic Matrix Composite CMC Thermal Protection Systems TPS and Hot Structures for Hypersonic Vehicles][research_glass_2008]
- [Glass, 2018, Thermal Protection Systems and Hot Structures for Hypersonic Vehicles][research_glass_2018]
- [Gnoffo and others, 1997, Computational aerothermodynamic design issues for hypersonic vehicles][research_gnoffo_weilmuenster_1997]
- [Gnoffo and others, 1999, Computational Aerothermodynamic Design Issues for Hypersonic Vehicles][research_gnoffo_weilmuenster_1999]
- [Goates and others, 2026, Hypersonic Impact Method for Aerodynamics and Convective Heating HI-Mach with Sensitivities][research_goates_freeman_2026]
- [Gockel, 1993, Angular control of a reentry vehicle in hypersonic flight regime][research_gockel_1993]
- [Gogu and others, 2008, Aero-assisted orbital transfer vehicle trajectory optimization considering thermal protection system weight][research_gogu_matsumura_2008]
- [GOLDBERG and Scala, 1965, MASS TRANSFER IN THE LOW REYNOLDS NUMBER VISCOUS LAYER AROUND THE FORWARD REGION OF A HYPERSONIC VEHICLE][research_goldberg_scala_1965]
- [GOLDBERG, 1966, Forces and moments on the front face of a blunt lifting reentry vehicle][research_goldberg_1966]
- [GOLDMAN and OBREMSKI, 1973, Experimental Investigation of Hypersonic Buzz on a Delta Configuration][research_goldman_obremski_1973]
- [Golenko and Sychev, 2020, Maneuvering Reentry Target Tracking by Means of Passive Radar][research_golenko_sychev_2020]
- [Golomazov and Ivankov, 2013, On the boundary conditions on a shock wave for hypersonic flow around a descent vehicle][research_golomazov_ivankov_2013]
- [Golubkin and Negoda, 1992, Improving the aerodynamic performance of small-aspect-ratio wings at hypersonic speeds][research_golubkin_negoda_1992]
- [Golubkin, 1995, Lifting wings of optimum shape in a viscous hypersonic stream][research_golubkin_1995]
- [Gomez Fernandez, 2024, Conceptual Design of a Small Launch Vehicle for CubeSats The Creative Process of Engineering Design][research_gomezfernandez_2024]
- [Gong and others, 2006, A Rapid Aerodynamics/Propulsion Analysis Method for Hypersonic Flight Vehicle MDO][research_gong_yuan_2006]
- [Gong and others, 2014, Aerodynamic Optimization of the Expansion Section in a Hypersonic Quiet Nozzle Based on Favorable Pressure Effect][research_gong_yao_2014]
- [Gong and others, 2014, Design and Optimization of RBCC Powered Suborbital Reusable Launch Vehicle][research_gong_chen_2014]
- [Gong and others, 2015, Comparison Study of RBCC Powered Suborbital Reusable Launch Vehicle Concepts][research_gong_bing_2015]
- [Gong and others, 2020, Mars entry guidance for mid-lift-to-drag ratio vehicle with control constraints][research_gong_guo_2020]
- [Gong and others, 2022, Performance Analysis on the Small-Scale Reusable Launch Vehicle][research_gong_wang_2022]
- [Gong and others, 2024, Recent development of integrated design and improving methods of waverider and inlet][research_gong_long_2024]
- [Gong Weijie and Tang Shuo, 2010, Aerodynamic heating numerical simulation method research for quasi-waverider hypersonic vehicle][research_gongweijie_tangshuo_2010_b]
- [Gong Weijie and Tang shuo, 2010, Hypersonic vehicle wing-body joint location design optimization basing on Hybrid Genetic Algorithm][research_gongweijie_tangshuo_2010]
- [Goodwin and Maxwell, 2017, Performance analysis of a hypersonic scramjet engine with a morphable waverider inlet][research_goodwin_maxwell_2017]
- [GOPINATH and others, 2015, Experimental Investigation on Metal Sandwich Panel for Hypersonic Cruise Vehicle Airframe with Active Cooling][research_gopinath_vignesh_2015]
- [Gopinath and others, 2017, Thermomechanical Deformation Behavior of a Hypersonic Waverider Using Finite Element Method][research_gopinath_vignesh_2017]
- [Gorelov and Nguyen, 2020, Rotation body of minimal aerodynamic drag in hypersonic rarefied gas flow][research_gorelov_nguyen_2020]
- [Gorenbukh and Nikolaev, 1988, Effect of viscosity on the lift-drag ratio of a thin blunt wing at hypersonic rates of flow round it][research_gorenbukh_nikolaev_1988]
- [Gormley, 2005, Conventional Force Integration in Global Strike][research_gormley_2005]
- [Gormley, 2015, US Advanced Conventional Systems and Conventional Prompt Global Strike Ambitions][research_gormley_2015]
- [Gottlieb and others, 2024, Coupled Vehicle and Trajectory Design Optimization for Boost-Glide Hypersonic Systems][research_gottlieb_mines_2024]
- [Gottmann, 1996, Methodology for aerothermodynamic design assessment and comparison of different reuseable launch vehicles in FESTIP][research_gottmann_1996]
- [Goulard, 1961, A Comment on "Radiation From Hot Air and Its Effect on Stagnation-Point Heating"][research_goulard_1961]
- [Govinda and others, 2017, Design of Optimized Two-Dimensional Scramjet Nozzle Contour for Hypersonic Vehicle Using Evolutionary Algorithms][research_govinda_devaraj_2017]
- [Goyal and others, 2023, Aerodynamic Shape Optimization of a Hypersonic Missile Geometry][research_goyal_prasad_2023]
- [Goyal and others, 2023, Correction Aerodynamic Shape Optimization of a Hypersonic Missile Geometry][research_goyal_prasad_2023_c]
- [Goyal and others, 2023, Withdrawal Aerodynamic Shape Optimization of a Hypersonic Missile Geometry][research_goyal_prasad_2023_b]
- [Goyer and Tallon, 2023, Exploring new solvent mixtures for near-net shaping of Ultra-High Temperature Ceramics via colloidal processing][research_goyer_tallon_2023]
- [Goz and Theodoulis, 2025, Robust Multi-Objective H∞ Control of GHAME Hypersonic Vehicle in Subsonic Flight][research_goz_theodoulis_2025]
- [Gracey and others, 1982, Fixed-trim re-entry guidance analysis][research_gracey_cliff_1982]
- [Graham and Mavris, 2000, Implementation of parametric analysis to the aerodynamic design of a hypersonic strike fighter][research_graham_mavris_2000]
- [Graham and others, 1978, COMPARISON OF SHIPBORNE WAVE RECORDER AND WAVERIDER BUOY DATA USED TO GENERATE DESIGN AND OPERATIONAL PLANNING CRITERIA][research_graham_verboom_1978]
- [Grail and others, 1993, Nonlinear Control Approach to Reentry Guidance of a Spacecraft][research_grail_joly_1993]
- [Grallert and Keller, 1991, Metallic thermal protection concept for hypersonic vehicles][research_grallert_keller_1991]
- [Grallert and others, 1987, A model test vehicle for hypersonic aerospace systems development][research_grallert_cucinelli_1987]
- [Gramola and others, 2022, Hypersonic foldable Aeroshell for THermal protection using ORigami HATHOR aerothermal analysis][research_gramola_bruce_2022]
- [Grant and Antony, 2016, Rapid Indirect Trajectory Optimization of a Hypothetical Long Range Weapon System][research_grant_antony_2016]
- [Grant and Bolender, 2015, Minimum Terminal Energy Optimizations of Hypersonic Vehicles Using Indirect Methods][research_grant_bolender_2015]
- [Grant and others, 2010, Rapid Entry Corridor Trajectory Optimization for Conceptual Design][research_grant_clark_2010]
- [Grant and others, 2011, Rapid Simultaneous Hypersonic Aerodynamic and Trajectory Optimization Using Variational Methods][research_grant_clark_2011]
- [Grant, 2013, Hybrid Exact-Approximate Analytic Hypersonic Aerodynamic Relations for General Vehicle Shapes][research_grant_2013]
- [GRANTZ and others, 1993, The effects of hypersonic flight test requirements on research vehicle design][research_grantz_cervisi_1993]
- [Grantz, 1994, Calibration of aerodynamic engineering methods for waverider design][research_grantz_1994]
- [Graves and Argrow, 2001, Aerodynamic performance of an osculating-cones waverider at high altitudes][research_graves_argrow_2001]
- [Graves and Emanuel, 1996, Parametric investigation of idealized hypersonic cruise configurations][research_graves_emanuel_1996]
- [GREEN and others, 1984, Aerothermodynamic environment and thermal protection for a Titan aerocapture vehicle][research_green_moss_1984]
- [Green and others, 2013, Morphing Hypersonic Inflatable Aerodynamic Decelerator][research_green_dunn_2013]
- [Green and others, 2018, Parallelization of a Six Degree of Freedom Entry Vehicle Trajectory Simulation Using OpenMP and OpenACC][research_green_williams_2018]
- [GREENE and WILLIAMSON, 1981, Variable node drag parameterization for reentry trajectory estimation][research_greene_williamsonjr_1981]
- [Grego, 2018, US Ground-based midcourse missile defense Expensive and unreliable][research_grego_2018]
- [GREGOREK and LEE, 1962, DESIGN PERFORMANCE AND OPERATIONAL CHARACTERISTICS OF THE ARL TWENTY-INCH HYPERSONIC WIND TUNNEL][research_gregorek_lee_1962]
- [GRENLESKI and BILLIG, 1968, Investigation of an actively cooled leading edge for hypersonic ramjet engines][research_grenleski_billig_1968]
- [Griffin and others, 2022, Aerothermodynamic Modeling for a "Mission Code" Approach to Hypersonic Flight][research_griffin_takahashi_2022]
- [Grimm, 1992, On Ascent Guidance of a Hypersonic Vehicle][research_grimm_1992]
- [Grimm, 1993, ON ASCENT GUIDANCE OF A HYPERSONIC VEHICLE][research_grimm_1993]
- [Gronlund and others, 2002, An assessment of the intercept test program of the ground-based midcourse national missile defense system][research_gronlund_wright_2002]
- [Gros, 1963, AERODYNAMIC HEATING AND OTHER PARAMETERS AFFECTING SPACE VEHICLE OPERATIONS AN ANNOTATED BIBLIOGRAPHY][research_gros_1963]
- [Groves and others, 2005, Anti-Windup Control for an Air-Breathing Hypersonic Vehicle Model][research_groves_serrani_2005]
- [Groves and others, 2005, Reference Command Tracking for a Linearized Model of an Air-Breathing Hypersonic Vehicle][research_groves_sigthorsson_2005]
- [Groves and others, 2006, Anti-Windup Control for an Air-Breathing Hypersonic Vehicle Model][research_groves_serrani_2006]
- [Gruber and others, 2023, Determining Predicted Trajectory Accuracy Requirements to Reduce the Aviation Impact of Space Launch and Reentry Operations][research_gruber_weitz_2023]
- [GRUBIN, 1963, ON GUIDANCE DYNAMICS FOR THE TERMINAL PHASE OF RENDEZVOUS][research_grubin_1963]
- [Grubin, 1964, GUIDANCE DYNAMICS FOR THE TERMINAL PHASE OF RENDEZVOUS][research_grubin_1964]
- [Gruhn and Gülhan, 2018, Aerodynamic Measurements of an Air-Breathing Hypersonic Vehicle at Mach 3.5 to 8][research_gruhn_gulhan_2018]
- [Grunlan and others, 2010, Performance Characterization of Polyimide-Carbon Fiber Composites for Future Hypersonic Vehicles][research_grunlan_rajagopal_2010]
- [Gräßlin and others, 2004, Ascent and reentry guidance concept based on NLP-methods][research_grasslin_telaar_2004]
- [Gu and others, 2017, Infrared signature characteristic of a microturbine engine exhaust plume][research_gu_baek_2017]
- [Gu and others, 2018, Sliding Mode Tracking Control and GA-based Optimization for Reentry Guidance Subject to Multi-Constraints][research_gu_qi_2018]
- [Gu and others, 2023, Anti-Windup Trajectory Optimization for High-Mass Mars Entry Vehicles][research_gu_dai_2023]
- [Gu, 2026, Isolating the specific contribution of boundary-layer edge chemical nonequilibrium to stagnation-point heating][research_gu_2026]
- [Guan and others, 2013, The indirect adaptive fuzzy predictive control of hypersonic vehicle][research_guan_wang_2013]
- [Guan and others, 2023, MAPPO-Based Cooperative UAV Trajectory Design with Long-Range Emergency Communications in Disaster Areas][research_guan_zou_2023]
- [Guan Ping and others, 2012, The adaptive fuzzy control of hypersonic vehicle][research_guanping_xueli_2012]
- [Guangjun and others, 2013, Hypersonic Vehicle Tracking Based on Improved Current Statistical Model][research_guangjun_hang_2013]
- [Guangren and others, 2015, Parametric approach for longitudinal attitude control of a hypersonic vehicle][research_guangren_yanmei_2015]
- [Gui and others, 1999, The numerical simulation of coupled unsteady ablation and heat transfer in the porthole region during reentry][research_gui_chen_1999]
- [GUI, 2019, Combined thermal phenomena of hypersonic vehicle][research_gui_2019]
- [Gulli and others, 2012, Integrated Analysis for the Design of Reusable TPS Based on Variable Transpiration Cooling for Hypersonic Cruise Vehicles][research_gulli_maddalena_2012]
- [GUNCKEL, 1966, Guidance and Control of Reentry and Aerospace Vehicles][research_gunckel_1966]
- [Guo and Chen, 2022, Influence analysis of Waverider wake on the deflection rate of light][research_guo_chen_2022_b]
- [Guo and Fan, 2022, Research on midcourse target tracking method of ballistic missile][research_guo_fan_2022]
- [Guo and Fang, 2022, Study on heat reduction and lift-to-drag ratio increase of two-dimensional wedge-shaped waverider blunt leading edges and high pressure capture wing 1 combined configuration][research_guo_fang_2022]
- [GUO and LIU, 2024, Robust control for hypersonic flight vehicle overload tracking under dynamics uncertainties][research_guo_liu_2024_b]
- [Guo and Lu, 2021, Improved Adaptive Integral-Sliding-Mode Fault-Tolerant Control for Hypersonic Vehicle With Actuator Fault][research_guo_lu_2021]
- [Guo and others, 2017, Penetration Trajectory Programming for Air-Breathing Hypersonic Vehicles in Cruise Duration with Control Constraints and Flight Dynamics Uncertainties][research_guo_wenxing_2017]
- [Guo and others, 2017, Predictor-corrector guidance for reentry hypersonic vehicle based on feedback linearization][research_guo_qi_2017]
- [Guo and others, 2017, Robust Adaptive Neural Fault-Tolerant Control of Hypersonic Flight Vehicle][research_guo_wang_2017]
- [Guo and others, 2018, A Piecewise Control Synthesis Approach for Nonlinear Systems with application to Hypersonic Vehicle][research_guo_liu_2018]
- [Guo and others, 2018, Adaptive twisting sliding mode algorithm for hypersonic reentry vehicle attitude control based on finite-time observer][research_guo_chang_2018]
- [Guo and others, 2018, Two controller designs of hypersonic flight vehicle under actuator dynamics and AOA constraint][research_guo_xu_2018]
- [Guo and others, 2019, Fault-Tolerant Controller Based on Integral Sliding Mode With Prescribed Performance for Hypersonic Re-entry Vehicle][research_guo_liu_2019]
- [Guo and others, 2019, Thermal flutter prediction at trajectory points of a hypersonic vehicle based on aerothermal synchronization algorithm][research_guo_shen_2019]
- [Guo and others, 2020, Entry Guidance With Terminal Time Control Based on Quasi-Equilibrium Glide Condition][research_guo_li_2020]
- [Guo and others, 2020, Robust adaptive control of hypersonic flight vehicle with asymmetric AOA constraint][research_guo_xu_2020]
- [Guo and others, 2021, Attitude/Parameter Coupling Modeling and Sliding Mode Control System Design for Hyper-Glide Vehicle][research_guo_gong_2021]
- [Guo and others, 2021, Reentry trajectory analysis of single-skinned parawing used in the hypersonic rarefied flow][research_guo_fang_2021]
- [Guo and others, 2021, Reentry trajectory planning and guidance method with no-fly zone constraints][research_guo_huang_2021]
- [Guo and others, 2022, A Review of the Development of Sealing Materials and Measurement and Control Simulation Technology for Typical Hypersonic Vehicle Positions][research_guo_chen_2022]
- [Guo and others, 2022, Optimization of Power and Thermal Management System of Hypersonic Vehicle with Finite Heat Sink of Fuel][research_guo_pang_2022]
- [GUO and others, 2023, A power and thermal management system for long endurance hypersonic vehicle][research_guo_pang_2023]
- [Guo and others, 2023, Active adaptive continuous nonsingular terminal sliding mode controller for hypersonic vehicle][research_guo_ding_2023]
- [Guo and others, 2023, Overload Tracking Control for Hypersonic Flight Vehicle with Coupling Coordination][research_guo_yang_2023]
- [Guo and others, 2024, Aerodynamic optimization of hypersonic blunted waveriders based on symbolic regression][research_guo_liu_2024]
- [Guo and others, 2024, An Intelligent Penetration Guidance Law Based on DDPG for Hypersonic Vehicle][research_guo_ding_2024]
- [Guo and others, 2024, Fault-Tolerant Tracking Control of Hypersonic Vehicle Based on a Universal Prescribe Time Architecture][research_guo_zhang_2024]
- [Guo and others, 2024, Rapid prediction model of terahertz transmission in hypersonic plasma sheath under different flight speeds for different vehicle types][research_guo_cen_2024]
- [Guo and others, 2025, Adaptive mollified prescribed performance controller for waverider vehicle subjected to mismatched disturbances][research_guo_ding_2025]
- [Guo and others, 2025, Drag reduction and lift enhancement mechanism induced by a novel combinational spike and high-pressure capturing wing concept in hypersonic flows][research_guo_lei_2025]
- [Guo and others, 2025, Numerical Investigation of Stage Separation Control of Tandem Hypersonic Vehicles Based on Lateral Jet][research_guo_fu_2025]
- [Guo and others, 2026, Meta-SAC based No-Fly Zone Avoidance Guidance Law for Hypersonic Glide Vehicles][research_guo_li_2026]
- [Guo and others, 2026, State-dependent extensible prescribed performance controller for waverider vehicle with actuator saturation][research_guo_ding_2026]
- [Guo and Xu, 2022, Finite-Time Deterministic Learning Command Filtered Control for Hypersonic Flight Vehicle][research_guo_xu_2022]
- [Guoning Bao and others, 2016, Optimal terminal guidance law design based on target weaving maneuver compensation][research_guoningbao_yangxu_2016]
- [GUPTA and Ramkumar, 2015, Titanium Aluminides for Metallic Thermal Protection System of Reusable Space Transportation Vehicle A Review][research_gupta_ramkumar_2015]
- [Gupta and Voelker, 2012, Aeroelastic Simulation of Hypersonic Flight Vehicles][research_gupta_voelker_2012]
- [GUSEV, 1990, The investigation of the hypersonic vehicle aerothermodynamics][research_gusev_1990]
- [Gustafsson and Glendor, 2019, Infrared signature simulations of a mobile camouflage for a heavy military vehicle][research_gustafsson_glendor_2019]
- [Guzmán-Bohórquez and others, 2024, EVALUATION AND VERIFICATION OF THE IMPACT OF VARIOUS MESH CONFIGURATIONS ON THE CFD SIMULATION OUTCOMES FOR AN OPTIMIZED HYPERSONIC WAVERIDER][research_guzmanbohorquez_greco_2024]
- [Guzmán-Bohórquez and others, 2025, AERODYNAMIC ANALYSIS APPLIED TO A HYPERSONIC VEHICLE TYPE WAVERIDER THROUGH CFD][research_guzmanbohorquez_greco_2025]
- [Gülhan and others, 2001, Experimental Investigation of Reentry Vehicle Aerothermodynamic Problems in Arc-Heated Facilities][research_gulhan_esser_2001]
- [HACKETT, 1993, Aerothermodynamic heating due to shock wave/laminar boundary-layer interactions in high-enthalpy hypersonic flow][research_hackett_1993]
- [HAGSETH and BLANKSON, 1993, Current technologies for waverider aircraft][research_hagseth_blankson_1993]
- [Haiqing and others, 2025, Hypersonic Vehicle Reentry Trajectory Optimization Based on Particle Swarm Algorithm][research_haiqing_junfeng_2025]
- [Hakima and Bazzocchi, 2021, Low-Thrust Trajectory Design for Controlled Deorbiting and Reentry of Space Debris][research_hakima_bazzocchi_2021]
- [Halbe and others, 2010, Energy Based Suboptimal Reentry Guidance of a Reusable Launch Vehicle Using Model Predictive Static Programming][research_halbe_mathavaraj_2010]
- [Halbe and others, 2014, Robust Reentry Guidance of a Reusable Launch Vehicle Using Model Predictive Static Programming][research_halbe_raja_2014]
- [Haley and Chudoba, 2018, Hypersonic Vehicle Solution Space Screening][research_haley_chudoba_2018]
- [Haley and others, 2018, Generic Hypersonic Vehicle Design Configuration Verification][research_haley_gonzalez_2018]
- [Hall and others, 2026, Coupling Fidelity and Stability in a Trajectory-Resolved Aerothermoelastic Analysis of a Maneuvering Hypersonic Vehicle][research_hall_schemmel_2026]
- [HALTER and CLIFF, 1991, Optimal energy-heading transients for an airbreathing hypersonic vehicle][research_halter_cliff_1991]
- [Hamed and Kumar, 1992, Hypersonic Flow Separation in Shock Wave Boundary Layer Interactions][research_hamed_kumar_1992]
- [Hamid and others, 2016, Stagnation point flow, heat transfer and species transfer over a shrinking sheet with coupled Stefan blowing effects from species transfer][research_hamid_nazar_2016]
- [Hamilton and others, 1991, Flight stagnation-point heating calculations on Aeroassist Flight Experiment vehicle][research_hamilton_gupta_1991]
- [Hamilton and others, 2007, Responsive Small Satellite and Launch Vehicle Conceptual Design Trade/Cost Modeling][research_hamilton_carsten_2007]
- [HAMMITT and BOGDONOFF, 1956, Hypersonic Studies of the Leading Edge Effect on the Flow Over a Flat Plate][research_hammitt_bogdonoff_1956]
- [Hammitt, 1959, The hypersonic viscous effect on a flat plate with finite leading edge][research_hammitt_1959]
- [Han and Jia, 2023, Propagated error correction of the gauss pseudospectral method for skip reentry trajectory planning][research_han_jia_2023]
- [Han and others, 2020, Thermal protection of a hypersonic vehicle by modulating stagnation-point heat flux][research_han_sun_2020]
- [Han and others, 2022, Investigation of energy accommodation coefficient at gas-solid interface of a hypersonic flying vehicle][research_han_liu_2022]
- [Han and others, 2024, Adaptive-critic-design based tracking controller for boost complement glide vehicle with performance constraint and input saturation][research_han_wang_2024]
- [Han and others, 2024, Learning-based Adaptive Disturbance Rejection Control for Hypersonic Vehicle][research_han_wang_2024_b]
- [Han and others, 2024, Terminal Soft Landing Guidance Law Using Analytic Gravity Turn Trajectory][research_han_jo_2024]
- [Han and others, 2025, Sliding Mode Based Line-of-Sight Tracking for Hypersonic Gliding Vehicle][research_han_wang_2025]
- [Han and Shan, 2011, RLV's re-entry trajectory optimization based on B-spline theory][research_han_shan_2011]
- [Han and Su, 2025, Leading-edge shape effects on traveling crossflow mode excitation in hypersonic swept flat plate boundary layers][research_han_su_2025]
- [Han and Xiong, 2016, Method of trajectory prediction for unpowered gliding hypersonic vehicle in gliding phase][research_han_xiong_2016]
- [Hanai and others, 2007, Two-Stage-To-Orbit Booster Configuration for Reducing Aerodynamic Heating at Hypersonic Speed][research_hanai_ozawa_2007]
- [Handley and others, 2017, Euler Elastica Terminal Parafoil Guidance][research_handley_streetman_2017]
- [Haney and Beaulieu, 1994, Waverider inlet integration issues][research_haney_beaulieu_1994]
- [Haney and Bradley, 1995, Waverider nozzle integration issues][research_haney_bradley_1995]
- [HANEY and others, 1993, A hypersonic waverider research vehicle][research_haney_cervisi_1993]
- [Haney, 1995, A waverider derived hypersonic X-vehicle][research_haney_1995]
- [Hanquist and Boyd, 2016, Limits for Thermionic Emission from Leading Edges of Hypersonic Vehicles][research_hanquist_boyd_2016]
- [Hanquist and Boyd, 2018, Effectiveness of Thermionic Emission for Cooling Hypersonic Vehicle Surfaces][research_hanquist_boyd_2018]
- [Hanson and Jones, 2004, Test Results for Entry Guidance Methods for Space Vehicles][research_hanson_jones_2004]
- [Hanson and others, 1998, Ascent, transition, entry, and abort guidance algorithm design for the X-33 vehicle][research_hanson_coughlin_1998]
- [Hanumpatla and Knight, 2026, Exploring Multivariable Design Trade-offs in Hypersonic Expansion Tunnels Using Multi-Objective Optimization][research_hanumpatla_knight_2026]
- [Hao and others, 2017, Fluid-Thermal-Structure Coupled Analysis of Radome for Hypersonic Flight Vehicle][research_hao_longbin_2017]
- [Hao and others, 2017, United Trajectory Design Method for Return to Launch Site of Suborbital Reusable Launch Vehicle][research_hao_peng_2017]
- [Hao and others, 2019, Bluntness for Quasi-waverider and Its Effect on Performance][research_hao_dengcheng_2019]
- [Hao and others, 2019, General Reentry Trajectory Planning Method Based on Improved Maneuver Coefficient][research_hao_peng_2019]
- [HAO and others, 2025, Parameterized evasion strategy for hypersonic glide vehicles against two missiles based on reinforcement learning][research_hao_zhang_2025]
- [Hao and Yongqi, 2024, Tracking Hypersonic Glide Vehicle Based on the MaRV Model with Multiple-model Approach][research_hao_yongqi_2024]
- [Hao, 2026, Study on the Current Status and Development Direction of Hypersonic Vehicle Research][research_hao_2026]
- [Haoliang and others, 2015, Constrained predictor corrector entry guidance for common aero vehicle][research_haoliang_yongzhao_2015]
- [Haque and others, 2026, Multi-Fidelity Surrogate-Based Trajectory-Aware Shape Optimization of Hypersonic Vehicles][research_haque_meo_2026]
- [Harl and Balakrishnan, 2010, Reentry Terminal Guidance Through Sliding Mode Control][research_harl_balakrishnan_2010]
- [Harl, 2008, Reentry Terminal Guidance Through Sliding Mode Control][research_harl_2008]
- [HARLOFF and PETRIE, 1987, Preliminary aerothermodynamic design method for hypersonic vehicles][research_harloff_petrie_1987]
- [Harper and Braun, 2014, Asymmetrically Stacked Tori Hypersonic Inflatable Aerodynamic Decelerator Design Study for Mars Entry][research_harper_braun_2014]
- [Harpold and Gavert, 1983, Space Shuttle entry guidance performance results][research_harpold_gavert_1983]
- [HARRIS and others, 1980, Aerodynamic prediction methodology for maneuvering reentry vehicles][research_harris_hall_1980]
- [HARTOFILIS, 1965, An investigation of flow separation and aerodynamic controls at hypersonic speeds][research_hartofilis_1965]
- [HARTUNG and others, 1991, Stagnation point nonequilibrium radiative heating and the influence of energy exchange models][research_hartung_mitcheltree_1991]
- [Hartung and others, 1992, Stagnation point nonequilibrium radiative heating and the influence of energy exchange models][research_hartung_mitcheltree_1992]
- [HARTUNIAN and THOMPSON, 1963, NONEQUILIBRIUM STAGNATION POINT HEAT TRANSFER INCLUDING SURFACE CATALYSIS][research_hartunian_thompson_1963]
- [Harvey, 2011, Shock Wave???Boundary-Layer Interactions Occurring in Hypersonic Flows in the Upper Atmosphere][research_harvey_2011]
- [Hasegawa, 2025, Comparison of Numerical Results With Wind Tunnel Aerodynamic Data of Flight Vehicle for Hypersonic Flight][research_hasegawa_2025]
- [HASSAN and others, 1991, Effect of nose shape on three-dimensional stagnation region streamlines and heating rates][research_hassan_dejarnette_1991]
- [Hassan and others, 2001, A coupled fluid/thermal/flight dynamics approach for predicting hypersonic vehicle performance][research_hassan_kuntz_2001]
- [Hassan and others, 2024, SiC addition to a dual phase high entropy ultra-high temperature ceramic][research_hassan_fahrenholtz_2024]
- [HATTIS and MALCHOW, 1992, Evaluation of some significant issues affecting trajectory and control management for air-breathing hypersonic vehicles][research_hattis_malchow_1992]
- [HATTIS and others, 1991, Integrated trajectory and control analysis for generic hypersonic vehicles][research_hattis_malchow_1991]
- [Hattis and Smolskis, 1989, Optimal Trajectory Generation and Design Trades for Hypersonic Vehicles][research_hattis_smolskis_1989]
- [Hattis, 1990, Hypersonic Vehicle Air Data Collection Assessing the Relationship Between the Sensor and Guidance and Control System Requirements][research_hattis_1990]
- [Havstad and Ferencz, 2002, Comparison of Surface Chemical Kinetic Models for Ablative Reentry of Graphite][research_havstad_ferencz_2002]
- [Hawkins and others, 2010, Terminal-Phase Guidance and Control Analysis of Asteroid Interceptors][research_hawkins_pitz_2010]
- [HAWKINS and RICHARDSON, 1991, Design and off-design performance analysis of a maximum compression/minimum drag hypersonic forebody][research_hawkins_richardson_1991]
- [Haws and Bowman, 2022, Comparing Large versus Small Launch Vehicle in an Exploration Campaign][research_haws_bowman_2022]
- [Haya Ramos and others, 2009, High Lift-to-Drag Re-entry Concepts For Space Transportation Missions][research_hayaramos_bonetti_2009]
- [Hayat and others, 2014, Newtonian heating in stagnation point flow of Burgers fluid][research_hayat_ali_2014]
- [Hayes and others, 2020, Dynamic Stability Analysis of a Hypersonic Entry Vehicle with a Non-Linear Aerodynamic Model][research_hayes_nompelis_2020]
- [Hayward and Urdiales, 2018, Small Satellite Launch Vehicle from a Balloon Platform][research_hayward_urdiales_2018]
- [He and Le, 2017, Design and Performances Analysis of the Integrated Curved Cone Waverider-Inlet][research_he_le_2017_b]
- [He and others, 2001, Numerical simulation of integrative flow field for hypersonic vehicle][research_he_le_2001]
- [He and others, 2009, Design of a Curved Cone Derived Waverider Forebody][research_he_le_2009]
- [He and others, 2012, Aqueous gelcasting of ZrB2-SiC ultra high temperature ceramics][research_he_zhang_2012]
- [He and others, 2015, Research on Special Vehicle Crew Thermal Protection Equipment Cooling Effect Trial][research_he_huang_2015]
- [He and others, 2016, Rapid generation of multi-target entry trajectory for hypersonic glide vehicles][research_he_liu_2016]
- [He and others, 2017, Design and analysis osculating general curved cone waverider][research_he_le_2017]
- [He and others, 2017, Fault-tolerant control with mixed aerodynamic surfaces and RCS jets for hypersonic reentry vehicles][research_he_qi_2017]
- [He and others, 2017, Maneuver trajectory design for hypersonic glide vehicles in dive phase][research_he_liu_2017]
- [He and others, 2018, PSO based Ascent Trajectory Optimization for Air-breathing Hypersonic Vehicle][research_he_li_2018]
- [He and others, 2022, Surrogate-based entire trajectory optimization for full space mission from launch to reentry][research_he_zuo_2022]
- [He and others, 2023, Integrated design of sun-synchronous orbit and launch vehicle trajectory for operationally responsive space][research_he_gu_2023]
- [He and others, 2023, Non-equilibrium modeling on the aerothermodynamic characteristics of hypersonic inflatable reentry vehicle][research_he_sun_2023]
- [He and others, 2024, Processing of Hypersonic Glide Vehicle-Borne SAR Data With Spiral Trajectory][research_he_tang_2024]
- [He and others, 2025, A Trajectory Prediction Method for Reentry Glide Vehicles via Adaptive Cost Function][research_he_li_2025]
- [He and others, 2025, Analysis of Aerodynamic Heating Modes in Thermochemical Nonequilibrium Flow for Hypersonic Reentry][research_he_zhao_2025]
- [He and others, 2026, An Intelligent Trajectory Prediction Algorithm for Reentry Glide Vehicles Based on Physics-Informed Constraints and Prediction Error Compensation][research_he_li_2026_b]
- [He and others, 2026, Intelligent Trajectory Prediction Algorithm for Reentry Glide Vehicle via Physics-Informed Constraints and State Predictive Control][research_he_li_2026]
- [He and others, 2026, Reentry Glide Vehicle Intent Inference Method via Multidimensional Intention Fusion][research_he_li_2026_c]
- [He and Yan, 2018, Adaptive Terminal Guidance Law for Spiral-Diving Maneuver Based on Virtual Sliding Targets][research_he_yan_2018]
- [He and Yan, 2020, Correction Adaptive Terminal Guidance Law for Spiral-Diving Maneuver Based on Virtual Sliding Targets][research_he_yan_2020]
- [He, 2015, Progress in Waverider Inlet Integration Study][research_he_2015_b]
- [He, 2015, Target Tracking Algorithm of Ballistic Missile in Boost Phase Based on Ground-based Radar Systems][research_he_2015]
- [HEATHMAN and KELLY, 1966, HYDROGEN TANKAGE FOR HYPERSONIC CRUISE VEHICLES][research_heathman_kelly_1966]
- [HEFFNER and others, 1991, Leading edge effect on rarefied hypersonic flow over a flat plate][research_heffner_gottesdiener_1991]
- [Hegarty and others, 2017, Lagrangian waverider and wave filtering system for use in ROV control][research_hegarty_omerdic_2017]
- [Heidrich and Braun, 2020, Aerocapture Trajectory Design in Uncertain Entry Environments][research_heidrich_braun_2020]
- [Heinze and Bardenhagen, 1998, Waverider Aerodynamics and Preliminary Design for Two-Stage-to-Orbit Missions, Part 2][research_heinze_bardenhagen_1998]
- [Heller and others, 1998, Flight dynamics and robust control of a hypersonic test vehicle with ramjet propulsion][research_heller_sachs_1998]
- [Heller and Widnall, 1968, Dynamics of an Acoustic Probe for Measuring Pressure Fluctuations on a Hypersonic Re-Entry Vehicle][research_heller_widnall_1968]
- [Heller, 1967, Wind Tunnel Study of Probes for Measuring Pressure Fluctuations on an Ablative Hypersonic Reentry Vehicle][research_heller_1967]
- [Hellman and others, 2011, Advancing Reusable Booster System RBS Technologies and Capabilities with a Space Tourist Suborbital Vehicle][research_hellman_remillard_2011]
- [Hellman, 2014, Trajectory Approaches for Launching Hypersonic Flight Tests][research_hellman_2014]
- [Hemanth and others, 2009, Shock tunnel testing of a Mach 6 hypersonic waverider][research_hemanth_jagadeesh_2009]
- [Hemdan, 1990, Waverider configurations according to thin shock-layer theory][research_hemdan_1990]
- [Henline and others, 1995, Aerothermodynamic heating analysis and heatshield design of an SSTO rocket vehicle for Access-to-Space][research_henline_palmer_1995]
- [HENLINE, 1991, Aerothermodynamic heating environment and thermal protection materials comparison for manned Mars-earth return vehicles][research_henline_1991]
- [Herman and Melnik, 1962, AERODYNAMIC AND HEAT TRANSFER STUDIES WITH EVAPORATIVE FILM COOLING AT HYPERSONIC MACH NUMBERS][research_herman_melnik_1962]
- [Hermann and Schmidt, 1995, Fuel-optimal SSTO mission analysis of a generic hypersonic vehicle][research_hermann_schmidt_1995]
- [Hermann, 1959, Problems of Hypersonic Flight at the Re-Entry of Satellite Vehicles][research_hermann_1959]
- [Hermann, 1961, EVAPORATIVE FILM COOLING AT HYPERSONIC VELOCITIES FOR RE-ENTRY VEHICLES][research_hermann_1961]
- [Hermann, 1961, Evaporative Film Cooling of Blunt Bodies in Hypersonic Flow and its Application to Re-entry Vehicles][research_hermann_1961_b]
- [Hermann, 2025, Correlation for wall-temperature oscillations in unsteady stagnation point convective heating][research_hermann_2025]
- [Hernandez and others, 2020, Global and Local Models for the Structural Analysis of the Hypersonic STRATOFLY Vehicle][research_hernandez_rodriguezsegade_2020]
- [HERRLIN and GELDERLOOS, 1988, Vehicle management system for a manned hypersonic vehicle][research_herrlin_gelderloos_1988]
- [Herrmann and others, 2025, Multidisciplinary Design and Analysis of a Hypersonic Glide Vehicle With Trimmed Aerodynamics][research_herrmann_cox_2025]
- [HILL, 1967, MATERIALS FOR SMALL RADIUS LEADING EDGES FOR HYPERSONIC VEHICLES][research_hill_1967]
- [Hillig, 1986, Prospects for Ultra-High-Temperature Ceramic Composites][research_hillig_1986]
- [Hills, 1985, Design Sounding Rocket Payload System to Study Vehicle Charging Phenomena][research_hills_1985]
- [Hinman and others, 2015, Computational Fluid Dynamics Study of Optimized Hypersonic Leading Edge Geometries][research_hinman_schmitt_2015]
- [Hinman and others, 2017, Optimization and analysis of hypersonic leading edge geometries][research_hinman_johansen_2017]
- [Hirose and others, 2015, Preliminary Experiment of the Drag Force Measurement by Using Strain Gauge in the Hypersonic Flow][research_hirose_udagawa_2015]
- [Hirschel and Meier, 2004, Aerodynamics from Near-Sonic to Hypersonic Flight][research_hirschel_meier_2004]
- [Hirschel and others, 2025, Aerothermodynamic Features of the External Flow Path][research_hirschel_staudacher_2025_b]
- [Hirschel and others, 2025, Basic Considerations of Hypersonic Airbreather Design][research_hirschel_staudacher_2025]
- [Hirschel and Weiland, 2009, Aerothermodynamic Design Problems of Non-Winged Re-Entry Vehicles][research_hirschel_weiland_2009_d]
- [Hirschel and Weiland, 2009, Aerothermodynamic Design Problems of Winged Airbreathing Vehicles][research_hirschel_weiland_2009_b]
- [Hirschel and Weiland, 2009, Aerothermodynamic Design Problems of Winged Re-Entry Vehicles][research_hirschel_weiland_2009_c]
- [Hirschel and Weiland, 2009, Short Introduction to Flight Trajectories for Aerothermodynamicists][research_hirschel_weiland_2009_f]
- [Hirschel and Weiland, 2009, The Thermal State of a Hypersonic Vehicle Surface][research_hirschel_weiland_2009]
- [Hirschel and Weiland, 2009, The γeff Approach and Approximate Relations for the Determination of Aerothermodynamic Parameters][research_hirschel_weiland_2009_e]
- [Hirschel and Weiland, 2010, Design of hypersonic flight vehicles some lessons from the past and future challenges][research_hirschel_weiland_2010]
- [HIRSCHEL, 1991, Aerothermodynamics and propulsion integration in the Saenger technology programme][research_hirschel_1991]
- [Hirschel, 1992, Aerothermodynamic Phenomena and the Design of Atmospheric Hypersonic Airplanes][research_hirschel_1992]
- [Hirschel, 2015, Inviscid Aerothermodynamic Phenomena][research_hirschel_2015]
- [Hirschel, 2015, Real-Gas Aerothermodynamic Phenomena][research_hirschel_2015_b]
- [Hiruma and others, 2020, Integrated Design of Trajectory and Robust Control for Hypersonic Experimental Aircraft][research_hiruma_takase_2020]
- [HODGE and others, 1981, Flight testing a manned lifting reentry vehicle /Space Shuttle/ for aerothermodynamic performance][research_hodge_phillips_1981]
- [Hodgson and Lee, 2003, Terminal Guidance Using a Doppler Beam Sharpening Radar][research_hodgson_lee_2003]
- [Hoffert and Wen, 2026, Approaching Experimental Conditions for Molecular Simulations of Phenol-Based Thermal Protection Materials][research_hoffert_wen_2026]
- [Hoffman and others, 2003, Near Net-Shape Ultra-High Melting Recession-Resistant Rocket Nozzles II Low Cost Carbon-Carbon Technology for Use in Ultra-High Temperature Oxidative Environments][research_hoffman_wapner_2003]
- [HOFFMANN and others, 1989, Aerothermodynamic analysis of projectiles at hypersonic speeds][research_hoffmann_wilson_1989]
- [Hohn and Gülhan, 2017, Impact of Retrorocket Plumes on Upper-Stage Aerothermodynamics During Stage Separation][research_hohn_gulhan_2017]
- [Holden and others, 2008, Experimental Studies in the LENS Supersonic and Hypersonic Tunnels for Hypervelocity Vehicle Performance and Code Validation][research_holden_wadhams_2008]
- [HOLDEN, 1978, A study of flow separation in regions of shock wave-boundary layer interaction in hypersonic flow][research_holden_1978]
- [Holden, 1986, Aerothermal Problems Associated with Viscous/Inviscid Interaction over Hypersonic Flight Vehicles][research_holden_1986]
- [HOLDSWORTH and LEONDES, 1990, Computational Methods for Decoy Discrimination and Optimal Targeting in Ballistic Missile Defense][research_holdsworth_leondes_1990]
- [HOLGUIN and LABBEE, 1988, Launch vehicle to payload interface standardization - The quest for a low cost launch system][research_holguin_labbee_1988]
- [Holifield and Tufts, 2024, Correction Uncertainty Quantification of Hypersonic Aerodynamic Heating][research_holifield_tufts_2024_b]
- [Holifield and Tufts, 2024, Uncertainty Quantification of Hypersonic Aerodynamic Heating][research_holifield_tufts_2024]
- [HOLLANDERS and others, 1992, Some aspects of the aerodynamic methodology in hypersonic vehicle concept studies][research_hollanders_laval_1992]
- [Hollis and Hollingsworth, 2012, Laminar, Transitional, and Turbulent Heating on Mid Lift-to-Drag Ratio Entry Vehicles][research_hollis_hollingsworth_2012]
- [Hollis and Hollingsworth, 2013, Laminar, Transitional, and Turbulent Heating on Mid Lift-to-Drag Ratio Entry Vehicles][research_hollis_hollingsworth_2013]
- [Hollis, 2017, Aerothermodynamics of a Hypersonic Inflatable Aerodynamic Decelerator HIAD with Flexible TPS][research_hollis_2017]
- [Holm-Hansen and others, 2010, Neuro-Fuzzy Dynamic Inversion Control for a Hypersonic Cruise Vehicle][research_holmhansen_lee_2010]
- [Holmquist and others, 1997, Development of Ultra High Temperature Ceramic Composites for Gas Turbine Combustors][research_holmquist_lundberg_1997]
- [Holthouse and others, 2026, Low-Speed Aerodynamic Performance of Hypersonic Airfoils][research_holthouse_subin_2026]
- [HONG and NEUENSCHWANDER, 1991, Internal convective heat transfer mechanism in reentry space vehicles][research_hong_neuenschwander_1991]
- [Hong and others, 2014, Reaction control system of hypersonic vehicle and its moment parameter identification][research_hong_xiong_2014]
- [Hong Qian. Lu and others, 2011, Aerodynamics/propulsion integrated modeling for control of hypersonic vehicle][research_hongqianlu_dongmingge_2011]
- [Hong-jun and Qing, 2015, Experimental Investigation of Leading Edge Bluntness Effects on Hypersonic Tow-dimensional Inlet][research_hongjun_qing_2015]
- [Hongbo and Yongyuan, 2016, Trajectory optimisation and analysis for hypersonic vehicle][research_hongbo_yongyuan_2016]
- [Hongpeng and Weiqiang, 2016, Thermal-structural analysis of the platelet heat-pipe-cooled leading edge of hypersonic vehicle][research_hongpeng_weiqiang_2016]
- [Hopkins and others, 2010, The analysis of conventional Prompt Global Strike alternatives][research_hopkins_raymond_2010]
- [Horing and others, 2025, Aerothermodynamic Sensitivity Analysis and Optimization of a Hypersonic Re-Entry Vehicle][research_horing_maute_2025_b]
- [Horing and others, 2025, Aerothermodynamic Sensitivity Analysis and Optimization of Hypersonic Reentry Vehicle][research_horing_maute_2025]
- [Horlock, 1964, Maximum Range of Hypersonic Ramjets][research_horlock_1964]
- [Horneman and others, 2010, Launch Vehicle Guidance for Low Energy Re-entry][research_horneman_neal_2010]
- [Hornung, 2021, Shock detachment and drag in hypersonic flow over wedges and circular cylinders][research_hornung_2021]
- [HORSTMAN, 1969, Cone drag in rarefied hypersonic flow][research_horstman_1969]
- [HORTON and BABINEAUX, 1967, Influence of atmospheric composition on hypersonic stagnation-point convective heating][research_horton_babineaux_1967]
- [Hoschke and others, 2013, Self-Organizing Sensing of Structures Monitoring a Space Vehicle Thermal Protection System][research_hoschke_price_2013]
- [Hoschke and others, 2013, Structural Health Monitoring of Space Vehicle Thermal Protection Systems][research_hoschke_price_2013_b]
- [Hoskin and others, 2024, Leading Edge Effects on Hypersonic Boundary Layer Receptivity and Transition][research_hoskin_nguyen_2024]
- [Hossein and others, 2025, Evaluating the influence of double curvature BOLT-2 versus conventional geometries on hypersonic aerothermodynamic effects][research_hossein_rabiee_2025]
- [Hoter and others, 2026, Aerothermodynamic Analysis of a Flexible Thermal Protection System Under Reentry Loads][research_hoter_nastac_2026]
- [Hou and others, 2015, Output feedback dynamic surface controller design for airbreathing hypersonic flight vehicle][research_hou_wang_2015]
- [Hou and others, 2023, An Intelligent Autonomous Morphing Decision Approach for Hypersonic Boost-Glide Vehicles Based on DNNs][research_hou_liu_2023]
- [Hou and others, 2025, Enhanced SCP with DNN for Reentry Trajectory Planning][research_hou_li_2025]
- [Hoult and others, 2003, DSMC of Power-Law Leading Edge Ionization for Hypersonic Telemetry Applications][research_hoult_starkey_2003]
- [HOVE and SHIH, 1977, Reentry vehicle stagnation region heat transfer in particle environments][research_hove_shih_1977]
- [HOVEY, 1964, Cork thermal protection design data for aerospace vehicle ascent flight][research_hovey_1964]
- [HOVEY, 1965, Cork thermal protection design data for aerospace vehicle ascent flight][research_hovey_1965]
- [Hsu and others, 1990, Complete footprint of lifting reentry vehicles][research_hsu_kuo_1990]
- [Hsu and others, 2000, Joint position during anterior-posterior glide mobilization Its effect on glenohumeral abduction range of motion][research_hsu_ho_2000]
- [Hu and Liu, 2013, Adaptive fuzzy DSC control based on ISpS for hypersonic vehicle][research_hu_liu_2013]
- [Hu and Mahadevan, 2019, Reliability Analysis of a Hypersonic Vehicle Panel with Spatio-Temporal Variability][research_hu_mahadevan_2019]
- [Hu and Meng, 2017, Adaptive backstepping control for air-breathing hypersonic vehicle with actuator dynamics][research_hu_meng_2017]
- [Hu and others, 1997, Linear stability of hypersonic flow over a parabolic leading edge][research_hu_hu_1997]
- [Hu and others, 2008, Microstructure and Mechanical Properties of SiC Whisker-Reinforced ZrB 2 Ultra-High Temperature Ceramic][research_hu_zhang_2008]
- [Hu and others, 2008, Towards Real-Time Simulation of Aeroservoelastic Dynamics for a Flight Vehicle from Subsonic to Hypersonic Regime][research_hu_bodson_2008]
- [Hu and others, 2012, Adaptive sliding mode tracking control for a flexible air-breathing hypersonic vehicle][research_hu_wu_2012_b]
- [Hu and others, 2012, Fuzzy guaranteed cost tracking control for a flexible air-breathing hypersonic vehicle][research_hu_wu_2012]
- [Hu and others, 2015, Design of Air-Breathing Hypersonic Vehicle Control System][research_hu_deng_2015]
- [Hu and others, 2015, Design of Periodic Cruise Vehicle Based on the Passive Waverider Method][research_hu_jiang_2015]
- [Hu and others, 2015, Output Tracking Control for Nonminimum Phase Flexible Air-Breathing Hypersonic Vehicle Models][research_hu_hu_2015]
- [Hu and others, 2016, Adaptive trajectory linearization control for hypersonic reentry vehicle][research_hu_wang_2016]
- [Hu and others, 2018, Neuro-adaptive tracking control of a hypersonic flight vehicle with uncertainties using reinforcement synthesis][research_hu_li_2018]
- [Hu and others, 2021, Fuzzy Adaptive Hybrid Compensation for Compound Faults of Hypersonic Flight Vehicle][research_hu_chen_2021]
- [Hu and others, 2021, Hybrid Adaptive Fault-Tolerant Control for Compound Faults of Hypersonic Vehicle][research_hu_li_2021]
- [Hu and others, 2021, Maneuver mode analysis and parametric modeling for hypersonic glide vehicles][research_hu_gao_2021]
- [Hu and others, 2022, Adaptive Sliding Mode Fault Compensation for Sensor Faults of Variable Structure Hypersonic Vehicle][research_hu_yang_2022]
- [Hu and others, 2022, Bionic adaptive fault-tolerant control of non-Gaussian stochastic attitude hypersonic vehicle][research_hu_zhu_2022]
- [Hu and others, 2022, Joint State and Parameter Estimation for Hypersonic Glide Vehicles Based on Moving Horizon Estimation via Carleman Linearization][research_hu_gao_2022]
- [Hu and others, 2022, Reinforcement Learning based Optimal Tracking Control for Hypersonic Flight Vehicle A Model Free Approach][research_hu_dong_2022]
- [Hu and others, 2022, Sliding mode learning control for T-S fuzzy system and an application to hypersonic flight vehicle][research_hu_guo_2022]
- [Hu and others, 2022, Sliding Mode Observer-Based Stuck Fault and Partial Loss-of-Effectiveness PLOE Fault Detection of Hypersonic Flight Vehicle][research_hu_liu_2022]
- [Hu and others, 2023, Guidance Method for Re-Entry Glide Vehicle Considering No-Fly Zone Avoidance][research_hu_sun_2023]
- [Hu and others, 2024, Meta-learning-based fault-tolerant attitude control of hypersonic flight vehicle with input constraints][research_hu_dong_2024]
- [Hu and others, 2024, Unmeasurable flexible dynamics monitoring and tracking controller design for guidance and control system of hypersonic flight vehicle][research_hu_xiao_2024]
- [Hu and others, 2025, Maneuver mode parametric modeling based on trajectory curve evolution laws for hypersonic glide vehicles][research_hu_liu_2025]
- [Hu and others, 2026, An enhanced radiative cooling structure based on phase change hydrogel for hypersonic vehicle][research_hu_wang_2026_b]
- [Hu and others, 2026, Attitude control of multirotor with image-aided terminal guidance for precision target strike][research_hu_wang_2026]
- [Hu and others, 2026, Numerical Study on Heat-Drag Reduction for Hypersonic Vehicles via Integrated Aerospike-Jet Configuration][research_hu_huang_2026]
- [Hu and Xin, 2014, Reentry trajectory optimization for hypersonic vehicles using fuzzy satisfactory goal programming method][research_hu_xin_2014]
- [Hu and Zhou, 2010, Design of Quick Parameter Optimization Guidance Method for Suborbital Vehicle in Reentry Phase][research_hu_zhou_2010]
- [Huang and Hartley, 1969, Kinetic Theory of the Sharp Leading Edge Problem in Supersonic Flow][research_huang_hartley_1969]
- [HUANG and HWANG, 1970, KINETIC THEORY OF THE SHARP LEADING EDGE PROBLEM II. HYPERSONIC FLOW][research_huang_hwang_1970]
- [Huang and Li, 2016, Receding Horizon Optimal controller for reference trajectory tracking in Mars entry guidance][research_huang_li_2016]
- [Huang and others, 2011, A parametric study on the aerodynamic characteristics of a hypersonic waverider vehicle][research_huang_ma_2011]
- [Huang and others, 2013, Non-fragile switching tracking control for a flexible air-breathing hypersonic vehicle based on polytopic LPV model][research_huang_sun_2013]
- [Huang and others, 2016, Terminal guidance and control for kinetic kill vehicle adopting side window detection][research_huang_zhang_2016]
- [Huang and others, 2017, Design Method of Internal Waverider Inlet with Bump Compression Surface][research_huang_fengyuan_2017]
- [Huang and others, 2017, Radar tracking for hypersonic glide vehicle based on aerodynamic model][research_huang_zhang_2017]
- [Huang and others, 2018, Cooperative control for the hypersonic vehicle lateral attitude tracking][research_huang_yang_2018]
- [Huang and others, 2018, Research on State Estimation of Hypersonic Glide Vehicle][research_huang_zhang_2018]
- [Huang and others, 2020, An Interacting-Multiple-Model Method for Tracking a Hypersonic Glide Target][research_huang_zhang_2020]
- [Huang and others, 2021, Research on Real-Time Reentry Trajectory Reconstruction Base on Multiple Model][research_huang_zhang_2021_b]
- [Huang and others, 2021, Robust UKF-based filtering for tracking a maneuvering hypersonic glide vehicle][research_huang_zhang_2021]
- [Huang and others, 2023, An adaptive state estimation for tracking hypersonic glide targets with model uncertainties][research_huang_li_2023]
- [Huang and others, 2023, Ascent Trajectory Design Method for Air-Breathing Combined Power Hypersonic Vehicle][research_huang_sun_2023]
- [Huang and others, 2024, Multitask-constrained reentry trajectory planning for hypersonic gliding vehicle][research_huang_yu_2024]
- [Huang and others, 2025, A heat flux distribution prediction method for hypersonic flight vehicle along trajectory based on POD and TSCN][research_huang_li_2025]
- [Huang and others, 2025, Thermal Control Investigation on Combined Thermal Protection System of Hypersonic Wings][research_huang_li_2025_b]
- [Huang and others, 2026, Trajectory Optimization for Hypersonic Vehicles Under Aerodynamic Uncertainty via Risk-Neutral Sequential Convex Programming][research_huang_zhang_2026]
- [Huang and Wu, 2018, Ultrahigh-Temperature Ceramics UHTCs Systems][research_huang_wu_2018]
- [Huang and Yao, 2020, Heat reduction mechanism and aerodynamic optimization of combined non-ablative thermal protection system concept][research_huang_yao_2020_b]
- [Huang and Yao, 2020, Hypersonic drag reduction mechanism of a novel combinational spike and multi-opposing jets aerodynamic configuration][research_huang_yao_2020]
- [Huang and Zhang, 2014, Characteristic model-based H 2/H ∞ robust adaptive control during the re-entry of hypersonic cruise vehicles][research_huang_zhang_2014]
- [Huang, 1968, Variational approach to conical bodies having maximum lift-to-drag ratio at hypersonic speeds][research_huang_1968]
- [HUBER, 1966, Probes for measuring mass flux, stagnation point heating, and total enthalpy of high temperature hypersonic gas flows][research_huber_1966]
- [Hufgard and others, 2023, Novel heat flux controlled surface cooling for hypersonic flight][research_hufgard_duernhofer_2023]
- [Hughes and Wu, 2010, H-Infinity LPV State Feedback Control for Flexible Hypersonic Vehicle Longitudinal Dynamics][research_hughes_wu_2010]
- [Hughes and Wu, 2012, LPV H∞ Control for Flexible Hypersonic Vehicle][research_hughes_wu_2012]
- [Hugo and Lago, 2022, Experimental Analysis of Waverider Lift-to-Drag Ratio Measurements in Rarefied and Supersonic Regime][research_hugo_lago_2022]
- [Hui and others, 2021, High-Speed Reentry Vehicle Trajectory Optimization and Guidance with Lateral Maneuver][research_hui_chi_2021]
- [Hui-Sheng and Bei-Jing, 2021, Skeletal Kinetic Modeling for the Combustion of Endothermic Hydrocarbon Fuel in Hypersonic Vehicle][research_huisheng_beijing_2021]
- [Huihui and others, 2016, Research on a Novel Internal waverider TBCC Inlet for Ramjet Mode][research_huihui_huang_2016]
- [Huihui and others, 2017, CFD Simulation of TBCC Inlet Based on Internal WaveRider Concept][research_huihui_huang_2017]
- [HULL and others, 1981, Reentry vehicle trim resulting from ablation coupled with motion][research_hull_french_1981]
- [Hull and Seguin, 1994, Guidance law for hypersonic gliders based on piecewise constant control][research_hull_seguin_1994]
- [Hunt and Eiswirth, 1996, NASA's dual-fuel airbreathing hypersonic vehicle study][research_hunt_eiswirth_1996]
- [Hunt and others, 1979, Performance Potential and Research Needs of a Hypersonic, Airbreathing, Lifting Missile Concept][research_hunt_lawing_1979]
- [Hunt and others, 1997, Hypersonic airbreathing vehicle visions and enhancing technologies][research_hunt_lockwood_1997]
- [Hunt, 1989, Hypersonic Airbreathing Vehicle Design Focus on Aero-Space Plane][research_hunt_1989]
- [Huo and others, 2006, Altitude and Velocity Tracking Control for an Airbreathing Hypersonic Cruise Vehicle][research_huo_mirmirani_2006]
- [Huo and others, 2014, Reentry Trajectory Optimization and Simulation of Hypersonic Vehicle with Maximum Cross Range Based on GPM][research_huo_liu_2014]
- [Huo and others, 2016, Thermal Flutter Analysis of Panel on Hypersonic Vehicle][research_huo_yang_2016]
- [Huo and Yang, 2015, The Rapid Engineering Aero-Heating Calculation Method for Hypersonic Vehicles][research_huo_yang_2015]
- [Huo and Yang, 2017, Aeroelastic Analysis for Response Prediction of Hypersonic Vehicle Rudder][research_huo_yang_2017]
- [Hutchins and San Jose, 1998, IMM tracking of a theater ballistic missile during boost phase][research_hutchins_sanjose_1998]
- [Hutt, 1987, Hypersonic vehicle pitch stability measurement in a ground based facility][research_hutt_1987]
- [Huynh and Kriz, 2009, Final Environmental Assessment for Hypersonic Technology Vehicle 2 Flight Tests][research_huynh_kriz_2009]
- [Hwang and Huh, 2020, Research and Development Trends of a Hypersonic Glide Vehicle HGV][research_hwang_huh_2020]
- [Hwang, 2019, Three-dimensional trajectory optimization for multi-stage launch vehicle mission using a full-space quasi-Lagrange-Newton method][research_hwang_2019]
- [IDE and others, 1989, Hypersonic vehicle forebody design studies and aerodynamic trends][research_ide_armstrong_1989]
- [Igra, 2018, Extension of the Simple Analytical Model for Waverider Design][research_igra_2018]
- [Igra, 2019, Nonslender Waverider Design Implementation into Simple Analytical Model for Waverider Design][research_igra_2019]
- [IKAWA, 1983, A methodology for aerodecelerating entry trajectory analysis][research_ikawa_1983]
- [IKAWA, 1989, Rapid methodology for design and performance prediction of integrated scramjet/hypersonic vehicle][research_ikawa_1989]
- [Ikenson, 2025, Keeping Cool System shows promise for better thermal protection of hypersonic vehicles][research_ikenson_2025]
- [Ingenito, 2021, Design of Supersonic/Hypersonic Vehicles][research_ingenito_2021]
- [INGER, 1991, Nonequilibrium effects on the aerodynamic heating of lifting hypersonic vehicles][research_inger_1991]
- [Inger, 1995, Non-equilibrium boundary layer effects on the aerodynamic heating of hypersonic vehicles][research_inger_1995_b]
- [Inger, 1995, Nonequilibrium boundary-layer effects on the aerodynamic heating of hypersonic waverider vehicles][research_inger_1995]
- [INOUE and PAGE, 1977, Aerothermodynamic base heating][research_inoue_page_1977]
- [Ionescu and others, 2021, Polymer-Derived Ultra-High Temperature Ceramics UHTCs and Related Materials][research_ionescu_bernard_2021]
- [ISAAC and MILES, 1990, Navier Stokes simulation of waverider flowfields][research_isaac_miles_1990]
- [ISHIKAWA and YAMAZAKI, 2021, Aerodynamic Shape Optimization of Waverider Fuselage by Response Surface Methodology][research_ishikawa_yamazaki_2021]
- [Ishimoto and others, 1996, Flight control system of Hypersonic Flight Experiment vehicle][research_ishimoto_takizawa_1996]
- [Ishimoto, 1995, Guidance algorithm for suborbital flight experiment of unmanned lifting entry vehicle][research_ishimoto_1995]
- [Ishimoto, 1999, Nonlinear trajectory control using drag-to-altitude transformation for entry guidance][research_ishimoto_1999]
- [Islam and Dutta, 2025, Machine learning assisted inverse heat transfer problem to find heat flux in ablative materials][research_islam_dutta_2025]
- [Ismail and others, 2016, Stagnation-point flow and heat transfer over an exponentially shrinking sheet A stability analysis][research_ismail_arifin_2016]
- [Ispir and others, 2019, Analysis of a combined cycle propulsion system for STRATOFLY hypersonic vehicle over an extended trajectory][research_ispir_goncalves_2019]
- [Istratie and Istratie, 1997, Three-dimensional optimal skip entry with terminal maximum velocity][research_istratie_istratie_1997]
- [Istratie and others, 2007, Optimal Skip Entry with Heat Constraints into Atmosphere][research_istratie_simos_2007]
- [Istratie and others, 2009, Optimal Skip Entry into Atmosphere with Constraints in Minimum Time][research_istratie_maroulis_2009]
- [Istratie, 1998, Optimal skip entry with terminal maximum velocity and heat constraint][research_istratie_1998]
- [Istratie, 1999, Optimal skip entry into atmosphere][research_istratie_1999]
- [Istratie, 2000, Optimal skip entry into atmosphere with minimum heat and constraints][research_istratie_2000]
- [Istratie, 2003, Optimal Skip Entry into Atmosphere with Minimum Heat][research_istratie_2003]
- [Ito and others, 1999, Plasma electron density measurement around hypersonic flight experiment vehicle][research_ito_takaki_1999]
- [Itoh and others, 1999, Hypervelocity aerothermodynamic and propulsion research using a high enthalpy shock tunnel HIEST][research_itoh_ueda_1999]
- [Itoh and others, 2002, Hypersonic aerothermodynamic and scramjet research using high enthalpy shock tunnel][research_itoh_ueda_2002]
- [Ivanov and others, 2007, Numerical Investigation of the EXPERT Reentry Vehicle Aerothermodynamics Along the Descent Trajectory][research_ivanov_vashchenkov_2007]
- [J and others, 2022, Real Time Trajectory Generation of Mars Entry using Legendre Pseudo-Spectral Method][research_j_swaminathan_2022]
- [Jackson and Anderson, 1967, A Carbon Dioxide Purge and Thermal Protection System for Liquid Hydrogen Tanks of Hypersonic Airplanes][research_jackson_anderson_1967]
- [Jackson, 2006, CFD Analysis of a Generic Waverider][research_jackson_2006]
- [Jaeger and Hemati, 2025, Hypersonic Glide Vehicle Trajectory Design using Constrained Energy Maneuverability][research_jaeger_hemati_2025]
- [JAENSCH and MARKL, 1991, Trajectory optimization and guidance for a Hermes-type reentry vehicle][research_jaensch_markl_1991]
- [Janardanan and Jayakumar, 2006, Robust Longitudinal Flight Controller Design for a Hypersonic Re-entry Vehicle][research_janardanan_jayakumar_2006]
- [Jangir and others, 2023, Comparative Performance of Radar, Laser, and Waverider Buoy Measurements of Ocean Waves. Part I Frequency Domain Analysis][research_jangir_ewans_2023]
- [Janovsky and others, 1999, The aerothermodynamic measurement system of the X-38][research_janovsky_romberg_1999]
- [Javaid and Serghides, 2003, Thrust Matching Requirements for the Conceptual Design of Hypersonic Waverider Vehicles][research_javaid_serghides_2003]
- [Javaid and Serghides, 2004, Airframe-Propulsion Integration Methodology for Waverider-Derived Hypersonic Cruise Aircraft Design Concepts][research_javaid_serghides_2004]
- [Javaid and Serghides, 2005, Airframe-Propulsion Integration Methodology for Waverider-Derived Hypersonic Cruise Aircraft Design Concepts][research_javaid_serghides_2005]
- [Javaid and Serghides, 2005, Thrust-Matching Requirements for the Conceptual Design of Hypersonic Waverider Vehicles][research_javaid_serghides_2005_b]
- [Jayan, 2023, Recent Advances in Ultra-High-Temperature Ceramic Coatings for Various Applications][research_jayan_2023]
- [JAYANTHI and JAIN, 2019, Flexibility Analysis of Cylindrical Panels of a Hypersonic Launch Vehicle in a Ballistic Trajectory for Separation Loads][research_jayanthi_jain_2019]
- [JEDLICKA and PARKER, 1970, Thermal performance of spherical models subjected to stagnation heating in a plasma arc facility][research_jedlicka_parkerjr_1970]
- [Jeon and others, 2020, Connections Between Proportional Navigation and Terminal Velocity Maximization Guidance][research_jeon_karpenko_2020]
- [Jeong and others, 2025, Re-Entry Trajectory Prediction Considering Skip Maneuver Characteristics][research_jeong_kang_2025]
- [Jeyakumar and others, 2005, Stage separation dynamic analysis of upper stage of a multistage launch vehicle using retro rockets][research_jeyakumar_biswas_2005]
- [Ji and others, 2014, Investigation on thermal performance of high temperature multilayer insulations for hypersonic vehicles under aerodynamic heating condition][research_ji_zhang_2014]
- [Ji and others, 2017, Trajectory tracking based on time-varying sliding mode controller for hypersonic vehicle with aileron stuck][research_ji_wang_2017]
- [Ji and others, 2018, Approximate output regulation of non-minimum phase hypersonic flight vehicle][research_ji_zhou_2018]
- [Ji and others, 2019, Trajectory Tracking Control for a generic Hypersonic Flight Vehicle Under Event-triggered Mechanism][research_ji_zhou_2019]
- [Ji and others, 2023, Distributed-Observer-Based on Longitudinal Flight Control for Hypersonic Vehicle][research_ji_zhao_2023]
- [Ji and others, 2025, Hypersonic vehicle trajectory tracking based on moving horizon estimation][research_ji_chen_2025]
- [Ji and Zhou, 2017, Nonlinear tracking control of hypersonic flight vehicle subjected to hyperbolic zero dynamics via output regulation theorem][research_ji_zhou_2017]
- [Ji and Zhou, 2018, Pseudo-spectral-enhanced Output Regulation for Hypersonic Flight Vehicle][research_ji_zhou_2018_b]
- [Ji, 2017, Thermo-mechanical Analysis and Optimization of Lightweight Corrugated-core Sandwich Integrated Thermal Protection System for Hypersonic Vehicles][research_ji_2017]
- [Jia and others, 2004, Forebody compressibility research of hypersonic vehicle][research_jia_wenxiu_2004]
- [Jia and others, 2018, Fast optimization of glide vehicle reentry trajectory based on genetic algorithm][research_jia_dong_2018]
- [Jia and others, 2020, Hypersonic aerodynamic interference investigation for a two-stage-to-orbit model][research_jia_fu_2020]
- [Jia-Ming and others, 2024, Analysis of Event-Based Camera's Potential for In-Flight Measurement on Hypersonic Test Vehicles][research_jiaming_kyle_2024]
- [Jian-bo and others, 2017, Initial descent phase guidance for hypersonic glide vehicle][research_jianbo_xinghua_2017]
- [Jianan and others, 2025, Investigation on Intelligent Dynamic Inverse Control Method for Hypersonic Vehicle][research_jianan_weidong_2025]
- [Jiang and Bu, 2022, Adaptive fuzzy finite-time control with prescribed performance for waverider vehicles][research_jiang_bu_2022]
- [Jiang and Luo, 2019, A Multi-space Interrelation Theory for Correlating Aerodynamic Data from Hypersonic Ground Testing][research_jiang_luo_2019]
- [Jiang and others, 2009, Experimental demonstration of a new concept of drag reduction and thermal protection for hypersonic vehicles][research_jiang_liu_2009]
- [Jiang and others, 2017, Aerodynamic Force and Moment Measurement Under Duplicated Hypersonic Flight Conditions in the JF12 Shock Tunnel][research_jiang_wang_2017]
- [Jiang and others, 2018, Sensor Composite Faults Estimation and Control for Hypersonic Flight Vehicle][research_jiang_chen_2018]
- [Jiang and others, 2018, Three-Channel Independent Integrated Guidance and Control for Reentry Vehicle Actuated by Two Moving Masses][research_jiang_lv_2018]
- [Jiang and others, 2020, Stochastic precision analysis of hypersonic flight vehicle attitude control system in the presence of uncertainties][research_jiang_zhou_2020]
- [Jiang and others, 2021, Fast Trajectory Optimization for Gliding Reentry Vehicle Based on Improved Sparrow Search Algorithm][research_jiang_ge_2021]
- [Jiang and others, 2022, Anti-Interception Guidance for Hypersonic Glide Vehicle A Deep Reinforcement Learning Approach][research_jiang_nan_2022]
- [Jiang and others, 2023, Intelligent Reentry Guidance with Dynamic No-Fly Zones Based on Deep Reinforcement Learning][research_jiang_wang_2023]
- [Jiang and others, 2024, Finite-time tracking control with prescribed performance for hypersonic flight vehicle][research_jiang_liu_2024]
- [Jiang and others, 2025, Obstacle Avoidance Terminal Guidance Law Design Considering Terminal Angle][research_jiang_zhou_2025]
- [Jiang and others, 2026, Long-range masked autoencoder for pre-extraction of trajectory features in within-visual-range maneuver recognition][research_jiang_cui_2026]
- [Jiang and Yu, 2019, Aerodynamic Testing at Duplicating Hypersonic Flight Conditions with Hyper-Dragon][research_jiang_yu_2019]
- [Jiang, 2018, Correction Robust Optimization of Mars Entry Trajectory under Uncertainty][research_jiang_2018_b]
- [Jiang, 2018, Robust Optimization of Mars Entry Trajectory under Uncertainty][research_jiang_2018]
- [Jianguo and others, 2018, Finite time control for generic hypersonic vehicle][research_jianguo_yifei_2018]
- [Jianjun Luo, 2003, An Integrated Optimization of RLV Reentry Trajectory][research_jianjunluo_2003]
- [Jiao and Jiang, 2014, Multi-objective optimization of reentry trajectory planning for hypersonic aircraft based on ant colony algorithm][research_jiao_jiang_2014]
- [Jiao and others, 2025, Trajectory Optimization Method of Hypersonic Vehicle Based on PSO-GPM][research_jiao_zhang_2025]
- [Jiayuan and others, 2018, A Comparison of Flight Control Strategies for Hypersonic Reentry Vehicles with Lateral-Directional Coupling Dynamics][research_jiayuan_peng_2018]
- [Jie Gu and others, 2016, Trajectory oscillation suppression control for lifting reentry vehicles with predictor-corrector guidance][research_jiegu_shuguangzhang_2016]
- [Jie, 2017, Numerical Study of Hypersonic Shock-Wave/Laminar Boundary-Layer Interactions of a Typical Lifting Vehicle][research_jie_2017]
- [Jin and others, 2008, Research on the thermal corridor of a hypersonic vehicle][research_jin_wang_2008]
- [Jin and others, 2018, Quenching crack patterns of the ultra-high temperature ceramic in shapes of leading edge or alike][research_jin_wang_2018]
- [Jin and others, 2019, Oxidation behaviors of ZrB2 based ultra-high temperature ceramics under compressive stress][research_jin_li_2019]
- [Jin and others, 2024, Parametric Design Method and Lift/Drag Characteristics Analysis for a Wide-Range, Wing-Morphing Glide Vehicle][research_jin_yu_2024]
- [Jin and others, 2026, Numerical investigations on aerodynamic characteristics in a longitudinal V-shaped hypersonic vehicle formation][research_jin_wang_2026]
- [Jinchuan Hu and others, 2015, Longitudinal characteristics of steady glide trajectory for hypersonic vehicle][research_jinchuanhu_jinglinli_2015]
- [Jing and others, 2007, Airframe/Scramjet Integrated Design of Hypersonic Cruise Vehicle][research_jing_shuo_2007]
- [Jing and others, 2018, Observer-based integrated guidance and control under terminal impact angle constraint][research_jing_zhao_2018]
- [Jing and others, 2026, Performance and optimization of thermal protection system integrated with phase change material for hypersonic vehicles][research_jing_song_2026]
- [Jing and Shuo, 2008, Integrated Optimization Design of Hypersonic Cruise Vehicle][research_jing_shuo_2008]
- [Jing and Yuan-pei, 2015, Concurrent Subspace Optimization Design of Hypersonic Cruise Vehicle][research_jing_yuanpei_2015]
- [Jing-guang and Shen-min, 2017, Tracking control of hypersonic vehicle with input saturation based on adaptive back-stepping method][research_jingguang_shenmin_2017]
- [Jingang and others, 2026, Prescribe performance sliding mode control for hypersonic flight vehicle][research_jingang_haotian_2026]
- [Jingqing Xu and others, 2011, Study of engineering design and application of glide range-extended trajectory][research_jingqingxu_xinglinqi_2011]
- [Jiying and others, 2010, Trajectory Estimation with Multi-range-rate System Based on Sparse Representation and Spline Model Optimization][research_jiying_jubo_2010]
- [Jo and others, 2019, Prediction of Stagnation-Point Radiative Heating for FIRE II][research_jo_park_2019]
- [Jo and others, 2020, Stagnation-point heating of Fire II with a non-Boltzmann radiation model][research_jo_kwon_2020]
- [Jo and others, 2021, Staging and Injection Performance Analysis of Small Launch Vehicle Based on KSLV-II][research_jo_kim_2021]
- [Jo, 2026, Aerodynamic Heating from Compression Corner Interactions in Hypersonic Flow][research_jo_2026]
- [John and Kulkarni, 2014, Effect of leading edge bluntness on the interaction of ramp induced shock wave with laminar boundary layer at hypersonic speed][research_john_kulkarni_2014]
- [JOHNSON and others, 1986, Space Shuttle Orbiter - Leading edge structural design/analysis and material allowables][research_johnson_curry_1986]
- [Johnson and others, 1996, Damage Accumulation in Titanium Matrix Composites Under Generic Hypersonic Vehicle Flight Simulation and Sustained Loads][research_johnson_mirdamadi_1996]
- [Johnson and others, 2001, Configuration development for a hydrocarbon fueled hypersonic cruise vehicle][research_johnson_bogar_2001]
- [Johnson and others, 2006, Adaptive Guidance and Control for Autonomous Hypersonic Vehicles][research_johnson_calise_2006]
- [Johnson and others, 2006, Aerothermodynamic Optimization of Re-Entry Heat Shield Shapes for a Crew Exploration Vehicle][research_johnson_starkey_2006]
- [Johnson and others, 2007, Aerothermodynamic Optimization of Reentry Heat Shield Shapes for a Crew Exploration Vehicle][research_johnson_starkey_2007]
- [Johnson and others, 2008, Analysis of Optimal Earth Entry Heat Shield/Trajectory Configurations][research_johnson_lewis_2008_b]
- [Johnson and others, 2008, Coupled Entry Heat Shield/Trajectory Optimization for Lunar Return][research_johnson_lewis_2008]
- [Johnson and others, 2009, Recent Developments in Ultra High Temperature Ceramics at NASA Ames][research_johnson_gasch_2009]
- [Johnson and others, 2018, Mid-Lift-to-Drag Ratio Rigid Vehicle Control System Design and Simulation for Human Mars Entry][research_johnson_cerimele_2018]
- [Johnson and others, 2020, Mid Lift-to-Drag Rigid Vehicle 6-DoF Performance for Human Mars Entry, Descent, and Landing A Fractional Polynomial Powered Descent Guidance Approach][research_johnson_lu_2020]
- [Johnson, 1967, A THERMAL PROTECTION SYSTEM FOR LIQUID HYDROGEN FUEL TANKAGE IN HYPERSONIC VEHICLES][research_johnson_1967]
- [Johnson, 2002, Screening Process for Boosters for Hypersonic Vehicles][research_johnson_2002]
- [Jones and Center, 2002, Waverider Design Methods for Non-Conical Shock Geometries][research_jones_center_2002]
- [Jones and Cesnik, 2024, Quantifying the Impact of Coupled Aero-Thermo-Elastic Modeling on Load Estimation of Hypersonic Vehicles During Trajectory Simulation][research_jones_cesnik_2024]
- [JONES and DOUGHERTY, 1990, Computational simulation of flows about hypersonic geometries with sharp leading edges][research_jones_dougherty_1990]
- [JONES and others, 1993, Waverider design for generalized shock geometries][research_jones_dougherty_1993]
- [Jones and others, 1995, Waverider design for generalized shock geometries][research_jones_sobieczky_1995]
- [JONES, 1972, Development and performance analysis of a trajectory estimator for an entry through the Martian atmosphere][research_jones_1972]
- [Joseph and others, 2026, Aerodynamic Characterization and Flight Trajectory Reconstruction Using Pressure Measurements for a Spent Stage Re-entry with Inflatable Aerodynamic Decelerator][research_joseph_sinha_2026]
- [Joseph and others, 2026, HIFiRE-1 Flight Assessment Using MARSHAL Multiphysics Architecture for Real-time Simulation of High-speed Aerothermodynamic Loads][research_joseph_whitside_2026]
- [Joshi and Lu, 2015, Unsteady Drag Measurements for Hypersonic Shock Tunnel][research_joshi_lu_2015]
- [Joshi and others, 2007, Predictor-Corrector Reentry Guidance Algorithm with Path Constraints for Atmospheric Entry Vehicles][research_joshi_sivan_2007]
- [Joshi and Sivan, 2005, Reentry Guidance for Generic RLV Using Optimal Perturbations and Error Weights][research_joshi_sivan_2005]
- [Josselyn and Ross, 2003, Rapid Verification Method for the Trajectory Optimization of Reentry Vehicles][research_josselyn_ross_2003]
- [Jouhaud and others, 2007, GUIDANCE AND ATTITUDE CONTROL LAW FOR THE FINAL PART OF A REENTRY VEHICLE TRAJECTORY - ALTERNATE LAWS FOR THE EXPERIMENTAL VEHICLE HSFD II][research_jouhaud_ferreres_2007]
- [Jouhaud, 1992, Closed loop reentry guidance law of a space plane Application to Hermes][research_jouhaud_1992]
- [Jun-hui and others, 2014, Guidance precision factors of terminal correction mortar projectile using pulse jets][research_junhui_jiayuan_2014]
- [Juneau and others, 1970, Ablative Materials for High Heat Loads. Part 1. Environmental Simulation and Materials Characterization][research_juneau_pw_1970]
- [Jutty K and others, 2000, Performance of Parallel Shooting Method for Closed Loop Guidance of an Optimal Launch Vehicle Trajectory][research_juttyk_bhat_2000]
- [Jänsch and others, 1994, Multi-Phase Trajectory Optimization Methods with Applications to Hypersonic Vehicles][research_jansch_schnepper_1994]
- [KABELITZ, 1970, Comparison of hypersonic aerodynamic deceleration systems based on gun tunnel investigations][research_kabelitz_1970]
- [Kadam and Hablani, 2014, Trajectory Optimization of Reentry Capsule][research_kadam_hablani_2014]
- [Kadish and Goldberger, 1995, Ablative therapy for atrioventricular nodal reentry arrhythmias][research_kadish_goldberger_1995]
- [KAGEYAMA and HIRAOKA, 2004, Analyses of Lift to Drag Ratio for Various Waverider Geometry][research_kageyama_hiraoka_2004]
- [Kahl and others, 1989, Intercomparison of Long-Range Trajectory Models Applied to Arctic Haze][research_kahl_harris_1989]
- [Kai and Ohtake, 1996, Thermal Protection System evaluation of the HYFLEX vehicle][research_kai_ohtake_1996]
- [Kalaiarassan and others, 2018, One-Dimension Force Balance System for Hypersonic Vehicle an experimental and Fuzzy Prediction Approach][research_kalaiarassan_krishan_2018]
- [Kalimuthu and Rathakrishnan, 2008, Aerospike for Drag Reduction in Hypersonic Flow][research_kalimuthu_rathakrishnan_2008]
- [Kalirajan and Joshi, 2016, Optimal Gliding Guidance for Long Range Hypersonic vehicles with Impact angle Constraints using Pseudospectral Method][research_kalirajan_joshi_2016]
- [Kalirajan and Joshi, 2018, Near Optimal Explicit Guidance Law with Impact Angle Constraints for a Hypersonic Re-entry Vehicle][research_kalirajan_joshi_2018]
- [Kameda and others, 2000, Target tracking for maneuvering reentry vehicles using multiple maneuvering models][research_kameda_tsujimichi_2000]
- [KAMIMOTO and UENAKA, 1969, Hypersonic Aerodynamic Characteristics for Lifting Bodies][research_kamimoto_uenaka_1969]
- [KAMINSKY and JOHNSON, 1964, Structural and thermal considerations of ablative-covered nonmetallic protective shells Ablative-covered nonmetallic shells of lifting body shape for thermal protection during superorbital reentry][research_kaminsky_johnsonjr_1964]
- [Kanda and Hiraiwa, 2007, Evaluation of Effectiveness of Periodic Flight by a Hypersonic Vehicle][research_kanda_hiraiwa_2007]
- [Kanderpalli and others, 2014, Heat Transfer Measurements On Waverider at Hypersonic Mach Numbers][research_kanderpalli_selvaraj_2014]
- [Kang and others, 2008, Optimal Trajectories of Hypersonic Vehicle for Global Reach][research_kang_tang_2008]
- [Kang and others, 2026, Ramp-backward-facing-step for flow control and heating reduction on a hypersonic V-shaped blunt leading edge][research_kang_yan_2026]
- [Karlgaard and others, 2018, Reconstruction of the Advanced Supersonic Parachute Inflation Research Experiment Sounding Rocket Flight Test][research_karlgaard_tynis_2018]
- [Karlgaard and others, 2020, Mars InSight Entry, Descent, and Landing Trajectory and Atmosphere Reconstruction][research_karlgaard_korzun_2020]
- [Karlgaard and others, 2022, Data Fusion of In-Flight Aerothermodynamic Heating Measurements Using Kalman Filtering][research_karlgaard_stoffel_2022]
- [Karlgaard and others, 2022, Mars Entry, Descent, and Landing Instrumentation 2 Trajectory, Aerodynamics, and Atmosphere Reconstruction][research_karlgaard_schoenenberger_2022]
- [Karlsdottir and Halloran, 2007, Rapid Oxidation Characterization of Ultra-High Temperature Ceramics][research_karlsdottir_halloran_2007]
- [Karp and others, 2026, Flow Unsteadiness in Model Hypersonic Vehicle Forebodies Using Inviscid Continuum and Viscous Kinetic Computations][research_karp_senkardesler_2026]
- [Karthick and Sriram, 2019, Computational Studies on the Unsteadiness in Hypersonic Shock Induced Leading Edge Separation][research_karthick_sriram_2019]
- [Kasahara and Matsuo, 2018, The Effect of Shape on the Aerodynamic and Thermal Performance of Hypersonic Projectiles Launched by a Ground-based Railgun][research_kasahara_matsuo_2018]
- [Kasen and others, 2008, A Heat Plate Leading Edge for Hypersonic Vehicles][research_kasen_queheillalt_2008]
- [Kasen and Wadley, 2019, Heat Pipe Thermal Management at Hypersonic Vehicle Leading Edges A Low-Temperature Model Study][research_kasen_wadley_2019]
- [Kashkovsky, 2014, DSMC investigations of reentry vehicle aerothermodynamics on GPU][research_kashkovsky_2014]
- [Kashyap and Mitra, 2020, Densification behavior involving creep during spark plasma sintering of ZrB2-SiC based ultra-high temperature ceramic composites][research_kashyap_mitra_2020]
- [Kashyap and Mitra, 2026, Thermophysical and electrical properties of spark plasma sintered ZrB2-SiC-LaB6 ultra-high temperature ceramic composites][research_kashyap_mitra_2026]
- [Kastantin and others, 2010, Sharp Leading Edge Delta-Wing Flow Control at Low Reynolds Numbers][research_kastantin_vey_2010]
- [Katiyar and Balasubramanian, 2014, Thermal modelling of hybrid composites of nano cenosphere and polycarbonate for a thermal protection system][research_katiyar_balasubramanian_2014]
- [Katzir and others, 1988, Best-Range Study for a Boost-Sustain Missile][research_katzir_cliff_1988]
- [Katzir and others, 1989, Best-Range Study for a Boost-Coast-Sustain Missile][research_katzir_cliff_1989]
- [KAUFFMAN and others, 1991, Optimum transitions in climb/cruise/descent for hypersonic cruise vehicles][research_kauffman_grandhi_1991]
- [Kauffman and others, 1992, Control strategy for maximizing reconnaissance range of hypersonic cruise vehicles][research_kauffman_grandhi_1992_b]
- [KAUFFMAN and others, 1992, OPTIMUM DESIGN OF TRANSITIONS IN CLIMB/CRUISE/DESCENT FOR HYPERSONIC CRUISE VEHICLES][research_kauffman_grandhi_1992]
- [Kaufman and Louis G, 1964, PRESSURE AND HEAT TRANSFER MEASUREMENTS FOR MACH 21 FLOWS OVER A BLUNT PYRAMIDAL CONFIGURATION WITH AERODYNAMIC CONTROLS. PART OF AN INVESTIGATION OF HYPERSONIC FLOW SEPARATION AND CONTROL CHARACTERISTICS][research_kaufman_louisg_1964]
- [KAUFMAN and others, 1966, An investigation of flow separation and aerodynamic controls at hypersonic speeds][research_kaufman_meckler_1966]
- [Kaufman, 1963, PRESSURE AND HEAT TRANSFER MEASUREMENTS FOR HYPERSONIC FLOWS OVER EXPANSION CORNERS AND AHEAD OF RAMPS. PART II MACH 5 PRESSURE DATA FOR FLOWS AHEAD OF RAMPS PART OF AN INVESTIGATION OF HYPERSONIC FLOW SEPARATION AND CONTROL CHARACTERISTICS][research_kaufman_1963]
- [KAUFMAN, 1970, Boride composites - A new generation of nose cap and leading edge materials for reusable lifting reentry systems][research_kaufman_1970]
- [Kaushal, 2024, Aerodynamic Optimization of Small Launch Vehicles Challenges, Design Considerations, and Future Trends][research_kaushal_2024]
- [Kavoosi and others, 2026, Effect of Si3N4 addition on erosion and oxidation resistance of ZrB2-SiC-ZrC ultra-high temperature ceramic composite Experimental and numerical investigation][research_kavoosi_mashhadi_2026]
- [Ke and others, 2025, Research on the performance of active-passive combined thermal control for external thermal protection structure of hypersonic aircraft][research_ke_wang_2025]
- [KEEL and others, 1971, Hypersonic low density cone drag][research_keeljr_kraige_1971]
- [Keely and others, 2026, Correction Development of a Computational Tool for Generating Hypersonic Waverider Geometries Using an Approximate Solution to the Taylor-Maccoll Equation][research_keely_thombs_2026]
- [Keely and others, 2026, Development of a Computational Tool for Generating Hypersonic Waverider Geometries Using an Approximate Solution to the Taylor-Maccoll Equation][research_keely_thombs_2026_b]
- [Kelkar and others, 2009, Modeling and Analysis Framework for Early Stage Trade-off Studies for Scramjet-Powered Hypersonic Vehicles][research_kelkar_vogel_2009]
- [KELLEY and others, 1981, Boost-glide range-optimal guidance][research_kelley_cliff_1981]
- [Kelley and others, 1982, Boost-glide range-optimal guidance][research_kelley_cliff_1982]
- [Kemp, 1960, Hydromagnetic Effects on Heating and Shear at a Three-Dimensional Stagnation Point in Hypersonic Flow][research_kemp_1960]
- [Kennell and others, 2015, Measurement of Vehicle Stability Coefficients in Hypersonic Wind Tunnels][research_kennell_neely_2015]
- [Keren and Marom, 2016, Long-range synchrony and emergence of neural reentry][research_keren_marom_2016]
- [Keshmiri and others, 2005, Development of an Aerodynamic Database for a Generic Hypersonic Air Vehicle][research_keshmiri_colgren_2005]
- [Keshmiri and others, 2006, Modeling and Simulation of a Generic Hypersonic Vehicle using Merged Aerodynamic Models][research_keshmiri_colgren_2006_b]
- [Keshmiri and others, 2006, Ramjet and Scramjet Engine Cycle Analysis for a Generic Hypersonic Vehicle][research_keshmiri_colgren_2006_c]
- [Keshmiri and others, 2006, Trajectory Optimization for a Generic Hypersonic Vehicle][research_keshmiri_colgren_2006]
- [Keshmiri, 2008, Nonlinear and Linear Longitudinal and Lateral-Directional Dynamical Model of Air-Breathing Hypersonic Vehicle][research_keshmiri_2008]
- [Kessler, 2022, Russian Hypersonic Glide Vehicles What to Know and What to Fear][research_kessler_2022]
- [Keyes, 1923, VOCATIONAL GUIDANCE IN THE CONTINUATION SCHOOL ENTRY OR RESERVOIR CLASS][research_keyes_1923]
- [Khalil and others, 2023, Flight Simulation and Drag Prediction for a Pitching-Accelerating Hypersonic Reentry Vehicle][research_khalil_abdelgawad_2023]
- [Khan and others, 2023, Direct Collocation Methods for Hypersonic Trajectory Optimization by the Process of Continuation][research_khan_zollars_2023]
- [Khatuntseva, 2011, Analysis of the reasons for an aerodynamic hysteresis in flight tests of the Soyuz reentry capsule at the hypersonic segment of its descent][research_khatuntseva_2011]
- [Khlopkov and others, 2014, Computer Modelling of Aerothermodynamic Characteristics for Hypersonic Vehicles][research_khlopkov_khlopkov_2014]
- [khraibut and others, 2015, Numerical Investigation of Bluntness Effects on Hypersonic Leading Edge Separation][research_khraibut_gai_2015]
- [Khraibut and others, 2017, Laminar hypersonic leading edge separation a numerical study][research_khraibut_gai_2017]
- [Khraibut and others, 2019, Numerical study of bluntness effects on laminar leading edge separation in hypersonic flow][research_khraibut_gai_2019]
- [Khraibut and others, 2019, Real Gas Effects on Hypersonic Leading Edge Separation with Bluntness][research_khraibut_gai_2019_b]
- [Khrapko, 2018, The Concept of the Combined Thermal Protection System for Leading Edges of Hypersonic Vehicles with Use of Thermionic Emission][research_khrapko_2018]
- [Khurana and Suzuki, 2013, Assessment of Aerodynamic Effectiveness for Aerospike Application on Hypothesized Lifting Body Configuration in Hypersonic Flow][research_khurana_suzuki_2013]
- [Kianvashrad and Knight, 2018, The Effect of Thermochemistry on Prediction of Aerothermodynamic Loading over a Double Cone in a Laminar Hypersonic Flow][research_kianvashrad_knight_2018]
- [Kianvashrad and Knight, 2019, Nonequilibrium Effects on Prediction of Aerothermodynamic Loading for a Double Cone][research_kianvashrad_knight_2019]
- [Kienappel and others, 1974, FORCE AND HEAT TRANSFER MEASUREMENTS ON INCLINED CONES IN THE HYPERSONIC RANGE FROM CONTINUUM TO FREE MOLECULAR FLOW][research_kienappel_koppenwallner_1974]
- [Kim and Kim, 2015, Missile Guidance Law Considering Constraints on Impact Angle and Terminal Angle of Attack][research_kim_kim_2015]
- [Kim and Lee, 2013, A study on structural safety of mechanical ground support equipment during the launch operation of a Korea small launch vehicle KSLV-1][research_kim_lee_2013]
- [KIM and others, 1982, Optimization of waverider configurations generated from axisymmetricconical flows][research_kim_rasmussen_1982]
- [Kim and others, 1996, Terminal guidance algorithms of missiles maneuvering in the vertical plane][research_kim_cho_1996]
- [Kim and others, 2009, Optimization of Glide Performance using Wind Estimator for Unpowerd Air Vehicle without Pitot-Tube][research_kim_jin_2009]
- [Kim and others, 2015, Lyapunov-Based Three-Dimensional Terminal Angle Constrained Guidance Laws][research_kim_lee_2015]
- [Kim and others, 2015, Sub-Orbital Hypersonic Flight Test Programs using Sounding Rockets and Small Launch Vehicles][research_kim_yang_2015]
- [Kim and others, 2016, Finite Horizon Integrated Guidance and Control for Terminal Homing in Vertical Plane][research_kim_whang_2016]
- [Kim and others, 2017, Infrared Signature Analysis on Armored Vehicle Applied with Emissivity Controlled Structure][research_kim_kim_2017]
- [Kim and others, 2021, Infrared signature of NEPE, HTPB rocket plume under varying flight conditions and motor size][research_kim_kim_2021]
- [Kim and others, 2023, A Study on Flow and Aerodynamic Characteristics During Separation Stage of Hypersonic Launch Vehicle on Level Flight][research_kim_kim_2023]
- [Kim and others, 2024, Fuel Efficiency Analysis of the Jet Engine and Solid-Propellant Based Small Reusable Sub-Orbital Launch Vehicle Candidates][research_kim_woldeyohannis_2024]
- [Kim and others, 2025, Infra-Red Scene Simulation Framework for Space-Based Hypersonic Vehicle Observation][research_kim_chang_2025]
- [Kim and others, 2025, Study on the Performance Characteristics of Osculating Cone Waverider According to Shock Wave Angle][research_kim_kim_2025]
- [Kim and others, 2025, System-Level Optimization and Validation of a Small Suborbital Launch Vehicle with Rocket and Jet Propulsion][research_kim_park_2025]
- [Kim, 2017, Thermal Analysis of Thermal Protection System of Test Launch Vehicle][research_kim_2017]
- [Kimmel and others, 2011, Ground Test and Computation of Boundary Layer Transition on the Hypersonic International Flight Research and Experimentation HIFiRE -5 Vehicle][research_kimmel_adamczak_2011]
- [King and others, 2019, Selective laser melting for the preparation of an ultra-high temperature ceramic coating][research_king_middendorf_2019]
- [Kinnersley and others, 2002, ROCKOT a Competitive and Reliable Launch Vehicle for Small Satellites][research_kinnersley_viertel_2002]
- [Kinney, 2006, Aerodynamic Shape Optimization of Hypersonic Vehicles][research_kinney_2006]
- [KINUGAWA and MATSUNO, 2021, Numerical Analysis of Lift Enhancement for Supersonic Waverider][research_kinugawa_matsuno_2021]
- [Kishi and others, 2014, CFD Optimization and Test Validation of 2D Ramjet Nozzle for Hypersonic Vehicle][research_kishi_joubert_2014]
- [KIVEL, 1961, Radiation From Hot Air and Its Effect on Stagnation-Point Heating][research_kivel_1961]
- [Klimin and Yaroshevski, 1970, Space Vehicle Trajectory Control for Entry into the Atmosphere at Hypersolic Speed][research_klimin_yaroshevski_1970]
- [Klock and Cesnik, 2015, Aerothermoelastic Reduced-Order Model of a Hypersonic Vehicle][research_klock_cesnik_2015]
- [Klock and Cesnik, 2016, Nonlinear Thermal and Thermoelastic Reduced Order Models of a Hypersonic Vehicle][research_klock_cesnik_2016]
- [Klothakis and Nikolos, 2024, Design and Evaluation of a Hypersonic Waverider Vehicle Using DSMC][research_klothakis_nikolos_2024]
- [Klothakis and others, 2026, DSMC Simulation of a Non-axisymmetric Hypersonic Vehicle at 90 km Altitude][research_klothakis_nikolos_2026]
- [Kluever, 2007, Terminal Guidance for an Unpowered Reusable Launch Vehicle with Bank Constraints][research_kluever_2007]
- [Kluever, 2008, Entry Guidance Performance for Mars Precision Landing][research_kluever_2008]
- [Kluever, 2008, Entry Guidance Using Analytical Atmospheric Skip Trajectories][research_kluever_2008_b]
- [Kluever, 2022, Simple Analytical Terminal Area Guidance for an Unpowered Reusable Launch Vehicle][research_kluever_2022]
- [Klumpp, 1986, Trajectory Shaping Rendezvous Guidance][research_klumpp_1986]
- [Knight and Kianvashrad, 2023, Experiments-hypersonic shock wave turbulent boundary layer interactions][research_knight_kianvashrad_2023]
- [Knight and others, 2026, Characterisation of Wake-Region Optical Emissions From an Ablative Hypersonic Glide Vehicle][research_knight_kildare_2026]
- [KNIGHT and QUINN, 1971, Graphite heat shield ablation during the low velocity-low altitude portion of reentry trajectories][research_knight_quinn_1971]
- [Knight and Schmisseur, 2012, Special issue of Progress in Aerospace Sciences on assessment of aerothermodynamic flight prediction tools][research_knight_schmisseur_2012]
- [Knight, 2015, Assessment of CFD Modeling Capability for Hypersonic Shock Wave Boundary Layer Interactions][research_knight_2015]
- [Knisely and others, 2019, Impact of Hypersonic Boundary Layer Transition on Skin Drag and Surface Heating on Blunt Cones][research_knisely_haley_2019]
- [Knittel and Lewis, 2012, Multidisciplinary Optimization of StarBody Waverider Shapes for Lifting Aerocapture with Orbital Plane Change][research_knittel_lewis_2012]
- [Knox, 2013, Forensic Engineering Analysis Methods Employed for the Purpose of Determining the Location of a Long-Range Shooter Based on Terminal Bullet Trajectory][research_knox_2013]
- [KO and others, 1981, Preflight reentry heat transfer analysis of Space Shuttle][research_ko_quinn_1981]
- [KOBAYASHI and SAPERSTEIN, 1981, Low-temperature ablator tests for shape stable nosetip applications on maneuvering reentry vehicles][research_kobayashi_saperstein_1981]
- [Kobayashi and Suzuki, 2006, Simultaneous Optimal Design of Hypersonic Turbojet Engine and Trajectory with SEAT][research_kobayashi_suzuki_2006]
- [Koch and others, 2025, Uncertainty quantification data model for the probabilistic design of the thermal protection system of a reusable launch vehicle stage][research_koch_wilken_2025]
- [Koike and others, 2018, Aerodynamic Heating Prediction of Flare-type Membrane Inflatable Reentry Vehicle from Low Earth Orbit][research_koike_takahashi_2018]
- [Kojima and others, 2012, Aerodynamic Heating Rate Evaluation of Mach 5 Hypersonic Airplanes][research_kojima_taguchi_2012]
- [Kokan and others, 2014, Low Cost Small LOX/HC Launch Vehicle Enabled by Affordable Propulsion][research_kokan_levack_2014]
- [Kominek and Black, 2006, The Blizzard Challenge 2006 CMU Entry introducing hybrid trajectory-selection synthesis][research_kominek_black_2006]
- [Kong and others, 2023, Research on Hypersonic Weapon Development][research_kong_ren_2023]
- [Kong and others, 2024, Operational Application of Russian Hypersonic Weapon][research_kong_sun_2024]
- [Kong and Zhang, 2025, Impact Speed Constrained Guidance Law Under Drag Uncertainty for Gliding Vehicle][research_kong_zhang_2025]
- [Kontinos and others, 2001, Temperature constraints at the sharp leading edge of a Crew Transfer Vehicle][research_kontinos_gee_2001]
- [Kontis and others, 2000, Hypersonic Performance of a Lifting Elliptic Cone with and Without Strakes][research_kontis_qin_2000]
- [Kontogiannis and others, 2015, On the Conceptual Design of Waverider Forebody Geometries][research_kontogiannis_sobester_2015]
- [Kontogiannis and others, 2015, Parametric Geometry Models for Hypersonic Aircraft Components Blunt Leading Edges][research_kontogiannis_cerminara_2015]
- [Kontogiannis and others, 2017, Efficient Parameterization of Waverider Geometries][research_kontogiannis_sobester_2017]
- [Kopp and Garbers, 2014, Investigation of Structure, Thermal Protection System, and Passenger Stage Integration for the Hypersonic Transport System SpaceLiner][research_kopp_garbers_2014]
- [KOPPENWALLNER, 1985, The drag of simple shaped bodies in the rarefied hypersonic flow regime][research_koppenwallner_1985]
- [Korabelnikov and Kuranov, 2002, Thermal protection of hypersonic flight vehicle using chemical heat regeneration][research_korabelnikov_kuranov_2002]
- [Korchagin, 2019, Modification of Guidance at the End of the First Entry for Skip Trajectory after Return from the Moon][research_korchagin_2019]
- [Kordulla and others, 1991, Attempt to Evaluate the Computations for Test Case 6.1 - Cold Hypersonic Flow Past Ellipsoidal Shapes][research_kordulla_periaux_1991]
- [KORNREICH, 1963, APPROXIMATE ANALYTIC SOLUTIONS FOR THE RANGE OF A NONLIFTING RE-ENTRY TRAJECTORY][research_kornreich_1963]
- [KORTE and others, 1992, CAN-DO, CFD-based Aerodynamic Nozzle Design and Optimization programfor supersonic/hypersonic wind tunnels][research_korte_kumar_1992]
- [Korte, 1992, Aerodynamic design of axisymmetric hypersonic wind-tunnel nozzles using a least-squares/parabolized Navier-Stokes procedure][research_korte_1992]
- [KORTE, 1992, Aerodynamic design of axisymmetric hypersonic wind-tunnel nozzles using least-squares/parabolized Navier-Stokes procedure][research_korte_1992_b]
- [Kothari and others, 2011, Rocket Based Combined Cycle Hypersonic Vehicle Design for Orbital Access][research_kothari_livingston_2011]
- [Kourtides and others, 1988, High-Temperature Properties of Ceramic Fibers and Insulations for Thermal Protection of Atmospheric Entry and Hypersonic Cruise Vehicles][research_kourtides_pitts_1988]
- [Kozlov, 1969, Discussion "Transient Temperature and Thermal Stresses in Skin of Hypersonic Vehicle With Variable Boundary Conditions" Chen, Shih-Yuan, 1958, Trans. ASME, 80, pp. 1389-1394][research_kozlov_1969]
- [Kraft and Chapman, 1993, A critical review of the integration of computations, ground tests, and flight test for the development of hypersonic vehicles][research_kraft_chapman_1993]
- [Krause and others, 1991, Thermal Control for Hypersonic Vehicle Propulsion][research_krause_hartmann_1991]
- [Kremeyer, 2004, Lines of Pulsed Energy for Supersonic/Hypersonic Drag Reduction Generation and Implementation][research_kremeyer_2004]
- [Krouse and Ellis, 1966, LONGITUDINAL AERODYNAMIC CHARACTERISTICS OF SEVERAL HYPERSONIC AIRCRAFT CONFIGURATIONS AT A MACH NUMBER OF 9.45][research_krouse_ellis_1966]
- [Krozel and others, 1997, Terminal area guidance incorporating heavy weather][research_krozel_weidner_1997]
- [Kubota and Uchida, 1999, Thermal Protection System with Use of Porous Media for a Hypersonic Reentry Vehicle][research_kubota_uchida_1999]
- [Kuipers and others, 2007, Adaptive Control of an Aeroelastic Airbreathing Hypersonic Cruise Vehicle][research_kuipers_mirmirani_2007]
- [Kuipers and others, 2008, Robust Adaptive Multiple Model Controller Design for an Airbreathing Hypersonic Vehicle Model][research_kuipers_ioannou_2008]
- [Kuipers and others, 2009, Analysis of an adaptive mixing control scheme for an airbreathing hypersonic vehicle model][research_kuipers_ioannou_2009]
- [Kulathunga and others, 2020, Real-Time Long Range Trajectory Replanning for MAVs in the Presence of Dynamic Obstacles][research_kulathunga_fedorenko_2020]
- [Kulkarni and others, 2024, UDE Based Robust Flight Control For Air-Breathing Hypersonic Vehicle Using Two-Loop Structure][research_kulkarni_shrekhar_2024]
- [Kulkarni and Phan, 2003, Optimal Feedback Control of the Magneto-Hydrodynamic Generator for a Hypersonic Vehicle][research_kulkarni_phan_2003]
- [Kumar and De, 2021, Modes of unsteadiness in shock wave and separation region interaction in hypersonic flow over a double wedge geometry][research_kumar_de_2021]
- [Kumar and Mahulikar, 2016, Aerothermal Analysis for Configuration Design of Swept Leading Edge Hypersonic Vehicle][research_kumar_mahulikar_2016]
- [Kumar and Mahulikar, 2017, Design of Thermal Protection System for Reusable Hypersonic Vehicle Using Inverse Approach][research_kumar_mahulikar_2017]
- [Kumar and others, 2012, Sliding-Mode Guidance and Control for All-Aspect Interceptors with Terminal Angle Constraints][research_kumar_rao_2012]
- [Kumar and others, 2014, Nonsingular Terminal Sliding Mode Guidance with Impact Angle Constraints][research_kumar_rao_2014]
- [Kumar and others, 2018, Dynamic pressure based mid-course guidance scheme for hypersonic boost-glide vehicle][research_kumar_sarkar_2018]
- [Kumar and others, 2018, Hypersonic Boost Glide Vehicle Trajectory Optimization Using Genetic Algorithm][research_kumar_penchalaiah_2018]
- [Kumar and others, 2018, Reentry Trajectory Optimization using Gradient Free Algorithms][research_kumar_ahmed_2018]
- [Kumar and others, 2020, Aerothermodynamic Assessment of Spiked Configuration for Drag Reduction at Hypersonic Speeds][research_kumar_kulkarni_2020]
- [Kumar and Singh, 2024, Synthesis, processing and wear characterization of ultra high temperature ceramics composite UHTC][research_kumar_singh_2024]
- [Kundu, 2013, Modeling of Ultrasonic and Terahertz Radiations in Defective Tiles for Condition Monitoring of Thermal Protection Systems][research_kundu_2013]
- [KUNHIKRISHNAN and others, 2012, Sensitivity in the trajectory of long-range α-particle][research_kunhikrishnan_nambiar_2012]
- [KUO, 1976, SOME CONSIDERATIONS OF THE DYNAMICS OF SPACE SHUTTLE VEHICLE THERMAL PROTECTION SYSTEM][research_kuo_1976]
- [Kuranov and Korabelnikov, 2008, Atmospheric Cruise Flight Challenges for Hypersonic Vehicles Under the Ajax Concept][research_kuranov_korabelnikov_2008]
- [Kuranov and others, 2012, Thermal protection and hydrogen production on board of the hypersonic vehicle][research_kuranov_korabelnikov_2012]
- [Kuranov and others, 2016, Conversion of hydrocarbon fuel in elements of thermal protection of a hypersonic flight vehicle][research_kuranov_korabelnikov_2016]
- [Kurilova and Li, 2026, Time-Frequency Wavelet Transformer Forecasting for Hypersonic Glide Vehicle Trajectory Prediction][research_kurilova_li_2026]
- [KURODA and IMADO, 1990, Improved advanced missile guidance system against a hypersonic target with short maneuvering time][research_kuroda_imado_1990]
- [Kushner and others, 2013, Photogrammetry of a Hypersonic Inflatable Aerodynamic Decelerator][research_kushner_littell_2013]
- [KUSSOY and HORSTMAN, 1970, Cone drag in rarefied hypersonic flow][research_kussoy_horstman_1970]
- [Kutkan and Eyi, 2018, Aerothermodynamic Shape Optimization of Reentry Capsule][research_kutkan_eyi_2018]
- [Kwon and others, 2021, Mid-course Trajectory Optimization for Boost-Glide Missiles Based on Convex Programming][research_kwon_hong_2021]
- [Küchemann, 1965, Hypersonic aircraft and their aerodynamic problems][research_kuchemann_1965]
- [L and others, 2025, Design of a Slot-Loaded Microstrip Antenna for Telemetry in Hypersonic Boost Systems][research_l_rao_2025]
- [La Sorsa and others, 2025, Thermal Analysis of Inconel-718 in Hypersonic Leading Edge Configurations][research_lasorsa_sprunger_2025]
- [LACOMBE and ROUGES, 1990, Ceramic matrix composites - Forerunners of technological breakthrough in space vehicle hot structures and thermal protection system][research_lacombe_rouges_1990]
- [Lafleur, 2009, Trading Robustness Requirements in Mars Entry Trajectory Design][research_lafleur_2009]
- [Lago and others, 2012, Shock Waves in Hypersonic Rarefied Flows][research_lago_chpoun_2012]
- [Lakin and others, 2025, Experimental Investigation on Heat Streaks Behind a Swept, Second-Order Continuous Leading Edge in Hypersonic Flow][research_lakin_smotzer_2025]
- [Lakshman and others, 2017, Shock-Induced Large Separation Bubbles Near the Leading Edge of a Flat Plate at Hypersonic Mach Numbers][research_lakshman_sriram_2017]
- [Lam, 2008, Circular Guidance Laws With and Without Terminal Velocity Direction Constraints][research_lam_2008]
- [Lan and others, 2014, H based decoupling tracking control of hypersonic vehicle][research_lan_wang_2014]
- [Lan and others, 2026, In-situ reactive spark plasma sintering and oxidation resistance of ZrB2-SiC-ZrC ultra-high temperature ceramics][research_lan_huiping_2026]
- [Landon and others, 1994, Automatic supersonic/hypersonic aerodynamic shape optimization][research_landon_hall_1994]
- [LANE and KIRLIN, 1978, Development of bond-on thermal protection systems for hypersonic research vehicle][research_lanejr_kirlin_1978]
- [LANE and SALMASSY, 1993, An evaluation of ablative materials for a lunar transfer vehicle aerobrake][research_lane_salmassy_1993]
- [Lang and Jacobs, 1997, Flow visualization and application of Particle-Image Velocimetry to the hypersonic configuration ELAC 1][research_lang_jacobs_1997]
- [Lanzano, 1961, Application of the Jacobi Integral of Celestial Mechanics to the Terminal Guidance of Space Probes][research_lanzano_1961]
- [Lapygin and Yakunina, 2009, The shapes of bodies with maximum lift-to-drag ratio in supersonic flow][research_lapygin_yakunina_2009]
- [Large, 1962, Nose Shape for Minimum Drag in Hypersonic Flow][research_large_1962]
- [Laster and others, 2006, Remarks on the Design of Hypersonic High Reynolds Number Nozzles with Energy Addition][research_laster_jordan_2006]
- [Lau, 1979, A midcourse thinning decision model for an exoatmospheric missile defence system][research_lau_1979]
- [Lau, 2008, Hypersonic Boundary-Layer Transition Application to High-Speed Vehicle Design][research_lau_2008]
- [LAURMANN, 1964, Structure of the boundary layer at the leading edge of a flat plate in hypersonic slip flow][research_laurmann_1964]
- [Law and others, 2023, Detecting and tracking hypersonic glide vehicles A cybersecurity-engineering analysis of academic literature][research_law_gliponeo_2023]
- [Lawson and others, 2011, Lattice thermal conductivity of ultra high temperature ceramics ZrB2 and HfB2 from atomistic simulations][research_lawson_daw_2011]
- [Lazarev, 1999, Structure of reusable hypersonic vehicles - Problems of weight, cost and operating effectiveness][research_lazarev_1999]
- [Lazur and others, 1999, Hypersonic vehicle control surface development][research_lazur_sawyer_1999]
- [Le and others, 2023, Attitude Control of a Hypersonic Glide Vehicle Based on Reduced-Order Modeling and NESO-Assisted Backstepping Variable Structure Control][research_le_liu_2023]
- [Leavitt and Mease, 2007, Feasible Trajectory Generation for Atmospheric Entry Guidance][research_leavitt_mease_2007]
- [Lecerf and others, 2014, New concept of small antennas for telemetry and tracking trajectory on space reentry vehicles][research_lecerf_villers_2014]
- [Lee and Cho, 2002, Reference trajectory analysis and trajectory control by bank angle for re-entry vehicle][research_lee_cho_2002]
- [Lee and Cho, 2006, ANALYSIS OF OPTIMAL TRAJECTORY FOR RE-ENTRY VEHICLE][research_lee_cho_2006]
- [Lee and James T, 1963, INVISCID HYPERSONIC FLOW FOR POWER-LAW SHOCK WAVES][research_lee_jamest_1963]
- [Lee and Kim, 2021, Stagnation-point heating and ablation analysis of orbital re-entry experiment][research_lee_kim_2021]
- [Lee and Kim, 2022, Stagnation-Point Ablation Analysis of Orbital Re-Entry Experiment][research_lee_kim_2022]
- [Lee and Lee, 2022, Optimal Trajectory Generation for Mars Atmospheric Entry Guidance using Parameter Optimization][research_lee_lee_2022_b]
- [Lee and Liu, 1999, Trajectory Estimation of Reentry Vehicles by Use of On-Line Input Estimator][research_lee_liu_1999]
- [Lee and others, 1999, Numerical computation of hypersonic flows over complex configuration][research_lee_zheng_1999]
- [Lee and others, 2003, Hypersonic Aerodynamic Heating Prediction Using Weighted Essentially Nonoscillatory Schemes][research_lee_zhong_2003]
- [Lee and others, 2007, Robust Nonlinear Dynamic Inversion Control for a Hypersonic Cruise Vehicle][research_lee_reiman_2007]
- [Lee and others, 2022, Pseudospectral Convex Optimization for Reentry Vehicle Guidance with No-Fly Zone Constraints][research_lee_lee_2022]
- [Lee and others, 2026, Effect of Thermochemical Models for Aerodynamic Heating Characteristics of Reentry Spaceplane in Hypersonic Simulations][research_lee_kim_2026]
- [Lee and Seo, 2018, New Insights into Guidance Laws with Terminal Angle Constraints][research_lee_seo_2018]
- [Lee, 2006, Optimization analysis of trajectory for re-entry vehicle using global orthogonal polynomial][research_lee_2006]
- [Lee, 2013, Shaping Guidance Law with Impact Angle Constraint for Alleviating Guidance Command at Terminal Phase][research_lee_2013]
- [Lee, 2023, Impact Speed Control Guidance for Glider Vehicle Using Optimal Output Trajectory Shaping Algorithm][research_lee_2023]
- [LEES, 1956, Influence of the Leading-Edge Shock Wave on the Laminar Boundary Layer at Hypersonic Speeds][research_lees_1956]
- [LEES, 1956, Laminar Heat Transfer Over Blunt-Nosed Bodies at Hypersonic Flight Speeds][research_lees_1956_b]
- [Lehr and others, 2003, Wind Uncertainty in Long Range Trajectory Forecasts][research_lehr_simecekbeatty_2003]
- [Lei and others, 2017, High-altitude and Low-speed Reentry Guidance for Suborbital Reusable Launch Vehicle Returning to Launch Site][research_lei_yan_2017]
- [Lei and others, 2026, Fast estimation of aerodynamics-heat transfer-ablation-dynamics coupled process for reentry vehicles][research_lei_wang_2026]
- [Leite and others, 2022, Aerodynamic Shape Optimization of a Symmetric Airfoil from Subsonic to Hypersonic Flight Regimes][research_leite_afonso_2022]
- [Leng and others, 2024, Design and investigation on the combined two-stage waverider equipped with rocket and scramjet engine][research_leng_wang_2024]
- [Leng and others, 2025, Investigation on factors influencing the range of boost-glide-cruise combined trajectories for scramjet-powered vehicles][research_leng_shen_2025]
- [Leng and others, 2025, Multidisciplinary design optimization of the first-stage waverider based on boost-glide flight trajectory][research_leng_xie_2025]
- [Leng and Qian, 2017, Sonic boom signature analysis for a type of hypersonic long-range civil vehicle][research_leng_qian_2017]
- [Leonardi and Pontani, 2024, Trajectory Optimization and Multiple-Sliding-Surface Terminal Guidance in the Lifting Atmospheric Reentry][research_leonardi_pontani_2024]
- [Leonardi, 2023, Trajectory optimization and multiple-sliding-surface terminal guidance in the lifting atmospheric reentry][research_leonardi_2023]
- [Lepore, 2006, AirLaunch's QuickReach� Small Launch Vehicle Development Status of Phase 2B][research_lepore_2006]
- [Lesin, 1976, Laminar heat transfer near an asymmetric stagnation point][research_lesin_1976]
- [LESSING and COATE, 1965, ATMOSPHERE REENTRY GUIDANCE - RETURN FROM THE MANNED MARS MISSION][research_lessing_coate_1965]
- [LESSING and others, 1963, LUNAR LANDING AND LONG-RANGE EARTH REENTRY GUIDANCE BY APPLICATION OF PERTURBATION THEORY][research_lessing_tunnell_1963]
- [Letkemann and others, 2024, Analysis of Refractive Index Changes Near the Ablative Surface of Hypersonic Vehicle][research_letkemann_tropina_2024]
- [Letkemann and others, 2026, Analysis of Refractive Index Changes Near Ablative Surface of Hypersonic Vehicle][research_letkemann_tropina_2026]
- [LETTS and CASTLE, 1981, Entry trajectory shaping for Shuttle-deployed experiments][research_lettsjr_castle_1981]
- [LEVENSTEINS and KRUMINS, 1967, Aerodynamic characteristics of hypersonic wakes][research_levensteins_krumins_1967]
- [Levin and DeLaurentis, 2024, Neighboring Optimal Maximum Range Glide Phugoid-Damping Guidance Law][research_levin_delaurentis_2024]
- [Levin and others, 2008, Adaptive Mode Suppression Scheme for an Aeroelastic Airbreathing Hypersonic Cruise Vehicle][research_levin_ioannou_2008]
- [LEWELLEN and MIRELS, 1966, Optimum lifting bodies in hypersonic viscous flow][research_lewellen_mirels_1966]
- [Lewis and Chauffour, 2005, Shock-Based Waverider Design with Pressure Gradient Corrections and Computational Simulations][research_lewis_chauffour_2005]
- [LEWIS and TAKASHIMA, 1993, Engine/airframe integration for waverider cruise vehicles][research_lewis_takashima_1993]
- [LEWIS, 1991, Application of waverider-based configurations to hypersonic vehicle design][research_lewis_1991]
- [Lewis, 1999, Sharp Leading Edge Hypersonic Vehicles in the Air and Beyond][research_lewis_1999]
- [Lewis, 2001, Significance of Fuel Selection for Hypersonic Vehicle Range][research_lewis_2001]
- [Lewis, 2017, Global strike hypersonic weapons][research_lewis_2017]
- [Li and Chen, 2011, An Adaptive Surrogate Model Applied to the Design Optimizations of Waverider-Based Hypersonic Vehicle][research_li_chen_2011]
- [Li and Cui, 2009, Optimal attack trajectory for Hypersonic Boost-Glide Missile in maximum reachable domain][research_li_cui_2009_b]
- [LI and FANG, 2008, EFFECTS OF THERMAL ENVIRONMENTS ON THE THERMAL SHOCK RESISTANCE OF ULTRA-HIGH TEMPERATURE CERAMICS][research_li_fang_2008_b]
- [Li and Fang, 2008, Thermal Shock Resistance of Ultra-High Temperature Ceramics][research_li_fang_2008]
- [Li and Fu, 2010, Exploring aerodynamic characteristics and control methods of hypersonic flight vehicle][research_li_fu_2010]
- [Li and Gao, 2014, An Engineering Method of Aerothermodynamic Environments Prediction for Complex Reentry Configurations][research_li_gao_2014]
- [Li and Jia, 2017, Output feedback sliding mode control with finite time trajectory tracking performance for the hypersonic vehicles][research_li_jia_2017]
- [Li and Lv, 2016, Fuzzy Control Design for Hypersonic Vehicle][research_li_lv_2016]
- [Li and others, 2006, Molecular Modeling of Oxidation of Ultra-High Temperature Ceramics][research_li_foerst_2006]
- [Li and others, 2008, A design on moving-mass actuated reentry vehicle with predictive guidance law][research_li_jing_2008]
- [Li and others, 2008, Properties and Microstructure of an HfB 2 -HfC-SiC Ultra High Temperature Ceramics][research_li_meng_2008]
- [Li and others, 2009, The temperature-dependent fracture strength model for ultra-high temperature ceramics][research_li_yang_2009]
- [Li and others, 2009, Thermal shock modeling of Ultra-High Temperature Ceramics under active cooling][research_li_yang_2009_b]
- [Li and others, 2009, Trajectory optimization for hypersonic boost-glide missile considering aeroheating][research_li_cui_2009]
- [Li and others, 2010, Fault-tolerant output tracking control for a flexible air-breathing hypersonic vehicle][research_li_si_2010]
- [Li and others, 2010, Research on Programming Algorithm of Trajectory for Hypersonic Vehicles Based on Particle Swarm Optimization][research_li_wang_2010]
- [Li and others, 2010, Trajectory Optimization and Reentry Tracking Research for Lifting Reentry Vehicle][research_li_shen_2010]
- [Li and others, 2011, A Control Method of Hypersonic Vehicle Based on the Structured Singular Value Theory][research_li_xu_2011]
- [LI and others, 2011, Control-oriented Modeling for Air-breathing Hypersonic Vehicle Using Parameterized Configuration Approach][research_li_lin_2011]
- [Li and others, 2011, Reference output tracking control for a flexible air-breathing hypersonic vehicle via output feedback][research_li_wu_2011]
- [Li and others, 2011, Reference tracking control for flexible air-breathing hypersonic vehicle with actuator delay and uncertainty][research_li_cheng_2011]
- [Li and others, 2012, A Temperature-Damage-Dependent Fracture Strength Model for Ultra-High Temperature Ceramics][research_li_yang_2012]
- [Li and others, 2012, Effective thermal conductivity of ultra-high temperature ceramics with thermal contact resistance][research_li_li_2012_c]
- [LI and others, 2012, Footprint Problem with Angle of Attack Optimization for High Lifting Reentry Vehicle][research_li_zhang_2012]
- [Li and others, 2012, Modelling the effect of temperature and damage on the fracture strength of ultra-high temperature ceramics][research_li_li_2012_b]
- [Li and others, 2012, Range Prediction and Trajectory Correction of Long Range Rocket with Attitude Stabilization][research_li_xiong_2012]
- [Li and others, 2012, Temperature-damage-dependent thermal shock resistance model for ultra-high temperature ceramics][research_li_li_2012]
- [Li and others, 2013, Catalytic Properties of ZrB 2 -Based Ultra-High Temperature Ceramics Based on the Wall Temperature Response Method][research_li_hu_2013]
- [Li and others, 2013, Influence of the connection section on the aerodynamic performance of the tandem waverider in a wide-speed range][research_li_luo_2013]
- [Li and others, 2014, Aerodynamic Design of the Bleed Slot in a Hypersonic Quiet Nozzle][research_li_shen_2014]
- [Li and others, 2014, Incipient Fault Detection for a Hypersonic Scramjet Vehicle][research_li_wang_2014]
- [Li and others, 2014, Integration methodology for waverider-derived hypersonic inlet and vehicle forebody][research_li_an_2014]
- [Li and others, 2014, Maneuver modes analysis for hypersonic glide vehicles][research_li_zhang_2014]
- [Li and others, 2015, Development of Aerodynamic Design of Hypersonic Quiet Nozzles][research_li_shen_2015]
- [Li and others, 2015, Maneuver characteristics analysis for hypersonic glide vehicles][research_li_zhang_2015]
- [Li and others, 2016, Research on the drag reduction performance induced by the counterflowing jet for waverider with variable blunt radii][research_li_wang_2016]
- [Li and others, 2016, Robust adaptive multivariable higher-order sliding mode flight control for air-breathing hypersonic vehicle with actuator failures][research_li_ma_2016]
- [Li and others, 2016, Rolling Guidance Law for single moving-mass reentry vehicle considering the influence of gravity][research_li_chao_2016]
- [Li and others, 2016, Steady glide reentry trajectory optimization with waypoint and no-fly zone constraints][research_li_chen_2016]
- [Li and others, 2016, The Multiobjective Trajectory Optimization for Hypersonic Glide Vehicle Based on Normal Boundary Intersection Method][research_li_yang_2016]
- [Li and others, 2017, Aerodynamic performance investigation on waverider with variable blunt radius in hypersonic flows][research_li_wang_2017]
- [Li and others, 2017, Analysis of longitudinal dynamic characteristics for air-breathing hypersonic flight vehicle][research_li_wu_2017]
- [Li and others, 2017, Flight-Corridor Analysis for Hypersonic Glide Vehicles][research_li_zhang_2017]
- [Li and others, 2017, Normal Acceleration Reduce Guidance and Control for Sub-orbit Vehicle Re-entry][research_li_xiao_2017]
- [Li and others, 2017, Performance analysis of hypersonic vehicle based on aerodynamic derivatives][research_li_chen_2017]
- [Li and others, 2017, Preparation of Ultra-High Temperature Ceramics-Based Materials by Sol-Gel Routes][research_li_huang_2017]
- [Li and others, 2018, Analysis on thermal control approach for a bare shaft of rudder in a hypersonic vehicle][research_li_yang_2018]
- [Li and others, 2018, Compound Guidance Law for Single Moving Mass Controlled Reentry Vehicle][research_li_chao_2018]
- [Li and others, 2018, Drag and Heat Reduction Mechanism of the Porous Opposing Jet for Variable Blunt Hypersonic Vehicles][research_li_huang_2018]
- [Li and others, 2018, Stochastic gradient particle swarm optimization based entry trajectory rapid planning for hypersonic glide vehicles][research_li_hu_2018]
- [Li and others, 2019, Adaptive back-stepping tracking control of the hypersonic vehicle with input saturation][research_li_sun_2019]
- [Li and others, 2019, Computer Simulation of Infrared Characteristics of Hypersonic Vehicle X43A][research_li_tian_2019]
- [Li and others, 2019, Time-coordinated reentry guidance law for reusable launch vehicle][research_li_peng_2019]
- [Li and others, 2019, Time-coordination entry guidance for multi-hypersonic vehicles][research_li_he_2019]
- [Li and others, 2020, A segmented and weighted adaptive predictor-corrector guidance method for the ascent phase of hypersonic vehicle][research_li_hu_2020]
- [Li and others, 2020, Design and investigation of equal cone-variable Mach number waverider in hypersonic flow][research_li_li_2020]
- [LI and others, 2020, Disturbance Rejection Control Based on Linear Quadratic for Nonminimum-phase Hypersonic Flight Vehicle System][research_li_chen_2020]
- [Li and others, 2020, Experimental investigation of a hypersonic I-shaped configuration with a waverider compression surface][research_li_cui_2020]
- [Li and others, 2020, Sol-gel derived porous ultra-high temperature ceramics][research_li_huang_2020]
- [Li and others, 2021, A Cooperative Reentry Trajectory Optimization Method for Hypersonic Glide vehicles][research_li_jiang_2021_b]
- [Li and others, 2021, A Two-Level Optimization Method for Hypersonic Periodic Cruise Trajectory][research_li_wang_2021]
- [Li and others, 2021, Analysis of main damage accumulative surfaces of the Hypersonic Flight Vehicle][research_li_ma_2021]
- [Li and others, 2021, Kinetic comparative study on aerodynamic characteristics of hypersonic reentry vehicle from near-continuous flow to free molecular flow][research_li_jiang_2021]
- [Li and others, 2021, Lateral Guidance for Hypersonic Vehicle Based on Linear Crossrange Prediction][research_li_liu_2021]
- [Li and others, 2021, Optimal Cruise Characteristic Analysis and Parameter Optimization Method for Air-Breathing Hypersonic Vehicle][research_li_zhou_2021]
- [Li and others, 2021, Optimization and Analysis for Hypersonic Steady-State Cruise Trajectory][research_li_wang_2021_b]
- [Li and others, 2022, Aerothermodynamic Shape Optimization of a Hypersonic Lifting Body][research_li_li_2022]
- [Li and others, 2022, An Improved Predictor-Corrector Guidance Algorithm for Reentry Glide Vehicle Based on Intelligent Flight Range Prediction and Adaptive Crossrange Corridor][research_li_zhou_2022_c]
- [Li and others, 2022, An Intelligent Trajectory Prediction Algorithm for Hypersonic Glide Targets Based on Maneuver Mode Identification][research_li_zhou_2022]
- [Li and others, 2022, Flight-Propulsion Integration Dynamic Analysis and Adaptive Control of the Hypersonic Vehicle at Wide-Range Mach Numbers][research_li_li_2022_b]
- [Li and others, 2022, Intelligent Trajectory Prediction Algorithm for Reentry Glide Target Based on Intention Inference][research_li_zhou_2022_b]
- [LI and others, 2022, Modified rolling guidance law for single moving mass controlled reentry vehicle against maneuvering target with impact angle constraints][research_li_yang_2022]
- [Li and others, 2022, Near Space Hypersonic Vehicle Target Tracking Adaptive Non-Zero Mean Model][research_li_xiong_2022]
- [Li and others, 2022, Segmented guidance law for single moving mass controlled reentry vehicle with multiple constraints][research_li_chao_2022]
- [Li and others, 2023, A Trajectory Generation Algorithm for a Re-Entry Gliding Vehicle Based on Convex Optimization in the Flight Range Domain and Distributed Grid Points Adjustment][research_li_zhou_2023_b]
- [Li and others, 2023, Detectability of onboard infrared detection system to hypersonic vehicles][research_li_qi_2023]
- [Li and others, 2023, Feasibility Analysis of Hypersonic Vehicles Trajectory Under Multiple Constraints][research_li_xu_2023]
- [Li and others, 2023, Online Trajectory Planning Method for Midcourse Guidance Phase Based on Deep Reinforcement Learning][research_li_li_2023]
- [Li and others, 2023, Research on Integrated Modeling and Control Method of the Air-Breathing Hypersonic Vehicle][research_li_zhou_2023]
- [Li and others, 2023, Three-Dimensional Optimal Homing Guidance Without Terminal Maneuverability Advantage][research_li_tao_2023]
- [LI and others, 2024, A novel evasion guidance for hypersonic morphing vehicle via intelligent maneuver strategy][research_li_wang_2024_b]
- [Li and others, 2024, A segmented trajectory planning and guidance method for hypersonic glide vehicles considering target detection performance][research_li_ma_2024]
- [Li and others, 2024, Computational Guidance Method for Mars Entry][research_li_liu_2024_g]
- [Li and others, 2024, Configuration Design and Application of Lm-2d Launch Vehicle Small Satellite Rideshare Mission][research_li_zhao_2024]
- [Li and others, 2024, Direct Model Reference Adaptive Tracking Guidance for Mars Entry][research_li_liu_2024_h]
- [Li and others, 2024, Improved Gauss Pseudospectral Method for Mars Entry Trajectory Planning][research_li_liu_2024_d]
- [Li and others, 2024, Improved Sequential Convex Optimization for Mars Entry Trajectory Planning][research_li_liu_2024_c]
- [Li and others, 2024, Indirect Sequential Convex Programming for Mars Entry Trajectory Planning][research_li_liu_2024_e]
- [Li and others, 2024, Mars Entry Trajectory Optimization with Desensitized Optimal Control][research_li_liu_2024_b]
- [Li and others, 2024, Observer based Online Identification of Aerodynamic Parameters for Hypersonic Gliding Vehicle][research_li_chang_2024]
- [Li and others, 2024, Performance analysis of hypersonic vehicle with integrated thermal protection and propulsion based on liquid ammonia-aviation kerosene][research_li_wang_2024]
- [Li and others, 2024, Preliminary Design of a Novel Multi-Stage Nose Cone for Hypersonic Aircraft Forebody][research_li_yu_2024]
- [Li and others, 2024, Pseudospectral Model Predictive Convex Programming for Mars Entry Trajectory Planning][research_li_liu_2024_f]
- [Li and others, 2024, Robust Trajectory Optimization for Mars Entry][research_li_liu_2024]
- [Li and others, 2024, The aerodynamic optimization of hypersonic vehicles with the proper-orthogonal-decomposition-based CST method][research_li_zhang_2024]
- [Li and others, 2024, Three-Dimensional Cooperative Guidance Against Aerial Target for Unpowered Glide Vehicle][research_li_li_2024]
- [Li and others, 2024, Tightly-Coupled LiDAR-Inertial-Range Odometry for Reducing Trajectory Drift][research_li_long_2024]
- [Li and others, 2025, Aerodynamic-Trajectory Integrated Optimization of a Lifting Body Based on Aerodynamic Fusion Modeling via MFNN with Redundant Feature Elimination][research_li_sun_2025]
- [Li and others, 2025, Collaborative Trajectory Planning for Hypersonic Vehicles Considering Angle Constraints][research_li_liu_2025_b]
- [Li and others, 2025, Cooperative Guidance of Glide Bombs Based on Gaussian Pseudo-spectral Method][research_li_mao_2025]
- [Li and others, 2025, Disintegration and separation of the bilobate-shaped meteoric fragment during hypersonic atmospheric entry][research_li_yu_2025]
- [Li and others, 2025, Energy-Based Range Augmentation Analysis for Maneuver-Assisted Jumping-Glide Trajectory Design][research_li_wang_2025]
- [Li and others, 2025, Energy-Optimal Guidance Law Design With Terminal Impact Angle Constraints][research_li_zhang_2025]
- [Li and others, 2025, Guidance Law with Terminal Velocity Constraint for Hypersonic Morphing Vehicle][research_li_liu_2025]
- [Li and others, 2025, Intelligent model correction and trajectory planning for air-breathing hypersonic vehicle considering inlet unstart][research_li_wu_2025]
- [Li and others, 2025, Longitudinal optimal analytical midcourse guidance for cruise-glide integrated hypersonic vehicles][research_li_cai_2025]
- [Li and others, 2025, Performance assessment of pressurized SOFC power generation system for hypersonic vehicles Thermodynamic analysis, system configuration optimization][research_li_cheng_2025]
- [Li and others, 2025, Reconfigurable fault-tolerant attitude control for over-actuated hypersonic flight vehicle with actuator failures][research_li_hu_2025]
- [Li and others, 2025, Reentry glide vehicle trajectory prediction method via multidimensional intention fusion][research_li_he_2025]
- [Li and others, 2025, Research development of ultra-high temperature ceramics][research_li_chen_2025]
- [LI and others, 2025, Variable leading-edge cone method for waverider design][research_li_jiang_2025]
- [Li and others, 2026, Adaptive mechanism-data fusion modeling for control-oriented integrated air-breathing hypersonic vehicle/scramjet with multistage fuel injection][research_li_song_2026]
- [Li and others, 2026, Expanding the members of ultra-high temperature ceramics and their maximum service temperature exceeding 3000 °C][research_li_zhang_2026]
- [Li and others, 2026, Mechanism model and protective control for an air-breathing hypersonic vehicle considering the combustion mode transition][research_li_feng_2026]
- [Li and others, 2026, Modeling and Control of Rigid-Elastic Coupled Hypersonic Flight Vehicles A Review][research_li_xu_2026]
- [Li and others, 2026, Sequential convex optimization for a hypersonic glide vehicle based on SOCP][research_li_zhao_2026]
- [LI and WEY, 1988, Numerical simulation of hypersonic flow over an aeroassist flight experiment vehicle][research_li_wey_1988]
- [Li and Xin, 2017, A three-dimensional anti-saturation terminal guidance law with finite-time convergence][research_li_xin_2017]
- [Li and Zhang, 2017, A Bézier Curve Based Ship Trajectory Optimization for Close-Range Maritime Operations][research_li_zhang_2017_b]
- [Li and Zhang, 2021, Computational Study on Radiative Aerothermodynamics of a Reentry Space Vehicle][research_li_zhang_2021]
- [Li and Zhao, 2014, Hypersonic Vehicle Leading Thermal Protection Technology][research_li_zhao_2014]
- [Li Zhi-huai and others, 2011, Research on detection of hypersonic weak target][research_lizhihuai_tanxiansi_2011]
- [Li, 2013, Reentry Guidance Based on Parametric Optimization][research_li_2013]
- [Li, 2021, Exact tracking control of hypersonic flight vehicles with full state constraints][research_li_2021_b]
- [Li, 2021, Skip Trajectory Characteristics Analysis for Hypersonic Glide Vehicles][research_li_2021]
- [Lian and others, 2012, Fuzzy Sliding Mode Variable Structure Controller for Hypersonic Cruise Vehicle][research_lian_shi_2012]
- [Lian and others, 2013, Hypersonic Cruise Vehicle Attitude Control Based on NESO][research_lian_bai_2013]
- [Lian and others, 2013, The Design of Nonlinear Flight Control System of Hypersonic Cruise Vehicle Based on Nonlinear Disturbance Observer][research_lian_bai_2013_b]
- [Liang and Han, 2008, Tracking of Semi-ballistic Reentry Vehicle][research_liang_han_2008]
- [Liang and Liu, 2009, An Optimal Control Method for Reentry Maneuvering Warhead][research_liang_liu_2009]
- [Liang and Mease, 2019, Precision Guidance for Mars Entry with a Supersonic Inflatable Aerodynamic Decelerator][research_liang_mease_2019]
- [LIANG and others, 2010, Controllable-structure Semi-ballistic Reentry Vehicle Tracking and Space-filling Model-set Design][research_liang_han_2010]
- [Liang and others, 2015, Decoupling trajectory tracking for gliding reentry vehicles][research_liang_ren_2015]
- [Liang and others, 2015, New Design of Small Cardinality Model Set for Tracking Controllable-Structure Semiballistic Reentry Vehicle][research_liang_han_2015]
- [Liang and others, 2016, Interceptor trajectory and guidance for hypersonic gliding targets][research_liang_yi_2016]
- [Liang and others, 2016, Modified shuffled frog leaping algorithm optimized control for air-breathing hypersonic flight vehicle][research_liang_zhen_2016]
- [Liang and others, 2017, Trajectory Planning for Cooperative Flight of Two Hypersonic Entry Vehicles][research_liang_yu_2017]
- [Liang and others, 2021, Kalman-filter-based robust control for hypersonic flight vehicle with measurement noises][research_liang_xu_2021]
- [Liang and others, 2023, A Robust Variational Bayesian Student-T CKF Algorithm for Hypersonic Vehicle Tracking][research_liang_hu_2023]
- [Liang and others, 2023, Robust Self-Learning Fault-Tolerant Control for Hypersonic Flight Vehicle Based on ADHDP][research_liang_xu_2023]
- [Liang and others, 2024, A Reentry Trajectory Planning Algorithm via Pseudo-Spectral Convexification and Method of Multipliers][research_liang_luo_2024]
- [Liang and others, 2025, Dynamic-Command-Limiting-Based AOA Constraint Control of Hypersonic Flight Vehicle][research_liang_xu_2025]
- [Liang and others, 2025, Fixed-Time Attitude Control of Hypersonic Flight Vehicle Based on Neural Disturbance Observer][research_liang_wen_2025]
- [Liao and Li, 2013, Trajectory optimization for terminal phase flight of hypersonic reentry vehicles with multi-constraints][research_liao_li_2013]
- [Liao and others, 1992, Navier-Stokes simulation for cone-derived waverider][research_liao_isaac_1992]
- [Liao and others, 2026, Conceptual exploration of two-dimensional hypersonic configuration based on aerodynamic topology][research_liao_luo_2026]
- [Liaoni Wu and others, 2008, Reusable Launch Vehicle lateral control design on suborbital reentry][research_liaoniwu_yiminhuang_2008]
- [LICATA, 1977, Reentry vehicle tracking problem][research_licata_1977]
- [Licheri and others, 2009, Spark plasma sintering of ZrB2- and HfB2-based Ultra High Temperature Ceramics prepared by SHS][research_licheri_orru_2009]
- [Licheri and others, 2010, Erratum to "Spark Plasma Sintering of ZrB2- and HfB2-Based Ultra High Temperature Ceramics Prepared by SHS"][research_licheri_orru_2010]
- [Licheri and others, 2010, Processing and Characterization of Zr-, Hf- and Ta-Based Ultra High Temperature Ceramics][research_licheri_orru_2010_b]
- [Lichodziejewski and others, 2013, Ground and Flight Testing of a Stacked Torus Hypersonic Inflatable Aerodynamic Decelerator Configuration][research_lichodziejewski_dillman_2013]
- [Liechty, 2008, Aerothermodynamic Testing of Protuberances and Penetrations on the NASA Crew Exploration Vehicle Heat Shield][research_liechty_2008]
- [Liguore and Tzong, 2011, Identification of Knowledge Gaps in the Predictive Capability for Response and Life Prediction of Hypersonic Vehicle Structures][research_liguore_tzong_2011]
- [Lin and Luo, 1995, Optimization of waverider generated from conical flow with combined transverse and longitudinal curvature][research_lin_luo_1995]
- [Lin and others, 2000, A novel approach for trajectory shaping reentry vehicle designs][research_lin_mckeel_2000]
- [Lin and others, 2003, Novel Approach for Maneuvering Reentry Vehicle Design][research_lin_sproul_2003]
- [Lin and others, 2006, Hypersonic Reentry Vehicle Wake Flow Fields at Angle of Attack][research_lin_sproul_2006]
- [Lin and others, 2014, Characterization of hot-pressed short ZrO 2 fiber toughened ZrB 2 -based ultra-high temperature ceramics][research_lin_huang_2014]
- [Lin and others, 2015, Spark plasma sintering of ZrO2 fiber toughened ZrB2-based ultra-high temperature ceramics][research_lin_huang_2015]
- [Lin and others, 2020, Reentry Trajectory Optimization of Powered Hypersonic Vehicle for Improving Range based on Discontinuous Ignition][research_lin_he_2020]
- [Lin and others, 2025, Expansion tube capabilities for studying boost-glide re-entry conditions][research_lin_wallington_2025]
- [Lin and others, 2025, Hypersonic Vehicle Maneuver Trajectory Multi-label Classification Based on Seq2Seq Model][research_lin_chen_2025]
- [Lin and others, 2025, Hypersonic Vehicle Missing Trajectory Imputation Prediction Based on Machine Learning][research_lin_zhuang_2025]
- [Lin and Shen, 1996, Navier-Stokes simulation of a cone-derived waverider with multidirectional curvature][research_lin_shen_1996_b]
- [Lin and Shen, 1996, Numerical study of multidirectional-curvature waverider with finlets][research_lin_shen_1996]
- [Lin and Shen, 1997, Flight simulation of a waverider-based hypersonic vehicle][research_lin_shen_1997]
- [Lin and Tsai, 1987, Analytical solution of optimal trajectory-shaping guidance][research_lin_tsai_1987]
- [LIN, 1983, Classical vs. modern control system design for terminal guidance of bank-to-turn intercept missiles][research_lin_1983]
- [Lin-lin and others, 2015, Single moving-mass asymmetrical reentry vehicle guidance law design][research_linlin_jianqiao_2015]
- [Lind and others, 1999, Multi-loop aeroservoelastic control of a hypersonic vehicle][research_lind_buffington_1999]
- [Ling and others, 2025, Vibration Control of Hypersonic Waverider Under Shock Wave Interference][research_ling_wang_2025]
- [Linqi and others, 2015, Adaptive control for a non-minimum phase hypersonic vehicle model][research_linqi_qun_2015]
- [Lippitt and others, 1983, Development of Passive Diver Thermal Protection System][research_lippitt_jr_1983]
- [Liquan and others, 2020, Tracking and application of IMM algorithm in mid-course of Booster-glide vehicle][research_liquan_nan_2020]
- [Liqun and others, 2017, Interception of hypersonic vehicle based on integrated guidance and control][research_liqun_chaoyang_2017]
- [Liu and Bai, 2021, Effect of curvature distribution on customized-planform waverider][research_liu_bai_2021]
- [Liu and Bai, 2024, Waverider Design Using Osculating Method][research_liu_bai_2024]
- [Liu and Duan, 2018, Direct parametric attitude tracking control for generic hypersonic vehicle][research_liu_duan_2018]
- [Liu and He, 2017, Study of reentry guidance based on analytical predictor-corrector for aerospace vehicle][research_liu_he_2017]
- [Liu and Jiang, 2013, Concept of Non-Ablative Thermal Protection System for Hypersonic Vehicles][research_liu_jiang_2013]
- [Liu and Liang, 2025, A systematic multiple-model estimator for tracking hypersonic gliding vehicle][research_liu_liang_2025]
- [Liu and Liu, 2016, A numerical model for the platelet heat-pipe-cooled leading edge of hypersonic vehicle][research_liu_liu_2016]
- [Liu and Lu, 2011, Conceptual research on modelling and control integrative design methods for hypersonic waverider][research_liu_lu_2011]
- [Liu and Lu, 2015, Collaborative Deformation Design Using Control Integrated Analysis Methods for Hypersonic Waverider][research_liu_lu_2015]
- [Liu and others, 2002, Integrated Hypersonic Aerothermoelastic Methodology for Transatmospheric Vehicle TAV /Thermal Protection System TPS Structural Design and Optimization][research_liu_chen_2002]
- [Liu and others, 2005, Input Estimation Algorithms for Reentry Vehicle Trajectory Estimation][research_liu_wang_2005]
- [Liu and others, 2007, Aerodynamic performance of waverider forebody Integrated with Inlet and Isolator][research_liu_xiao_2007]
- [Liu and others, 2010, Research on thermal control system of Hypersonic Glide Vehicle][research_liu_hou_2010]
- [Liu and others, 2011, Research of equilibrium-glide guidance method based on the generalized reference-trajectory][research_liu_chen_2011]
- [Liu and others, 2012, Consecutive tracking for ballistic missile based on bearings-only during boost phase][research_liu_yu_2012]
- [Liu and others, 2013, Preliminary research on optimal design based on control demands for hypersonic morphing vehicle][research_liu_deng_2013]
- [Liu and others, 2014, Applications of multi-block CST method for quasi-waverider design][research_liu_duan_2014]
- [Liu and others, 2014, Multidisciplinary parameterization study-based control-centric idea for hypersonic morphing vehicle][research_liu_chen_2014]
- [Liu and others, 2014, Novel approach for designing a hypersonic gliding-cruising dual waverider vehicle][research_liu_ding_2014]
- [Liu and others, 2014, Optimization on steady-state cruise for a hypersonic vehicle][research_liu_wang_2014]
- [Liu and others, 2015, Design, Modeling and Analysis of a Sharp-edge Hypersonic Stealthy Re-entry Vehicle][research_liu_li_2015]
- [Liu and others, 2016, Navier-Stokes predictions of dynamic stability derivatives for air-breathing hypersonic vehicle][research_liu_liu_2016_b]
- [Liu and others, 2016, Partial integrated guidance and control for hypersonic vehicle in initial reentry phase][research_liu_wang_2016]
- [Liu and others, 2016, Predictor-corrector guidance for entry with terminal altitude constraint][research_liu_liang_2016]
- [Liu and others, 2016, Rapid Design and Optimization of Waverider from 3D Flow][research_liu_peng_2016]
- [Liu and others, 2016, The Effect of Thermochemical Non-Equilibrium on the Aerodynamics of Osculating-Cone Waverider][research_liu_jun_2016]
- [Liu and others, 2017, Experiments to determine surface catalytic recombination coefficients of ultra high temperature ceramics in high temperature dissociated flows][research_liu_wang_2017]
- [Liu and others, 2017, Partial Integrated Guidance and Control Design for Hypersonic Vehicle in Dive Phase][research_liu_chen_2017]
- [Liu and others, 2017, Research on the design of double swept waverider][research_liu_bai_2017]
- [Liu and others, 2017, The fast-optimization for configuration of hypersonic vehicle][research_liu_tang_2017]
- [Liu and others, 2018, Control variable parameterisation with penalty approach for hypersonic vehicle reentry optimisation][research_liu_liu_2018_b]
- [LIU and others, 2018, Design method of a new hypersonic waverider configuration][research_liu_zhang_2018]
- [Liu and others, 2018, Novel Osculating Flowfield Methodology for Hypersonic Waverider Vehicles Based on Variable Shock Angle][research_liu_liu_2018]
- [Liu and others, 2018, RESEARCH ON THE CROSS-SCALE THERMAL CHARACTERISTICS PREDICTION METHOD OF INTEGRATED THERMAL PROTECTION MATERIALS FOR HYPERSONIC VEHICLE][research_liu_shi_2018]
- [Liu and others, 2019, A new design of a support force measuring system for hypersonic vehicle aerodynamic measurement][research_liu_gao_2019]
- [Liu and others, 2019, Drag Reduction Effect for Hypersonic Lifting-body Vehicle with Counterflowing Jet][research_liu_dong_2019]
- [Liu and others, 2019, Numerical Investigation of RCS Jet Interaction on a Hypersonic Vehicle][research_liu_chen_2019]
- [Liu and others, 2019, Planform-customized waverider design integrating with vortex effect][research_liu_liu_2019]
- [Liu and others, 2019, Surrogate-based aerodynamic shape optimization of hypersonic flows considering transonic performance][research_liu_han_2019]
- [Liu and others, 2019, Trim and Flight Elastic Coupling Characteristics of a Flexible Air-breathing Hypersonic Vehicle][research_liu_chen_2019_b]
- [Liu and others, 2020, An Adaptive Infrared Tracking Method for Spacebased Surveillance to a Hypersonic Cruise Vehicle][research_liu_luo_2020_b]
- [Liu and others, 2020, Barrier Lyapunov function based reinforcement learning control for air-breathing hypersonic vehicle with variable geometry inlet][research_liu_dong_2020]
- [Liu and others, 2020, Design and Optimization Method for Hypersonic Quasi-Waverider][research_liu_zhang_2020]
- [Liu and others, 2020, Effect of Bulging Upper Surface on Waverider Performances][research_liu_bai_2020]
- [Liu and others, 2020, Reentry Attitude Tracking Control for Hypersonic Vehicle with Reaction Control Systems Via Improved Model Predictive Control Approach][research_liu_hou_2020]
- [Liu and others, 2020, Space infrared tracking of a hypersonic cruise vehicle using an adaptive scaling UKF][research_liu_luo_2020]
- [Liu and others, 2021, Parametric Study on Lateral-Directional Stability of Hypersonic Waverider][research_liu_zhang_2021]
- [LIU and others, 2021, Phase plane design based fast altitude tracking control for hypersonic flight vehicle with angle of attack constraint][research_liu_dong_2021]
- [Liu and others, 2021, Real-time Trajectory prediction for Hypersonic Glide Vehicle Based on 3-D Flight Corridor][research_liu_xie_2021]
- [Liu and others, 2022, Adaptive control arc length-based time grid refinement control parameterisation method for unmanned hypersonic vehicle reentry trajectory optimisation][research_liu_liu_2022]
- [Liu and others, 2022, Carbon nanotube reinforced pyrocarbon matrix composites with high coefficient of thermal expansion for self-adapting ultra-high-temperature ceramic coatings][research_liu_guo_2022]
- [Liu and others, 2022, Colloidal Processing of Complex-Shaped ZrB2-Based Ultra-High-Temperature Ceramics Progress and Prospects][research_liu_yan_2022]
- [Liu and others, 2022, Design and calibration test of a support force measuring system for hypersonic vehicle aerodynamic measurement][research_liu_pang_2022]
- [Liu and others, 2022, Mars Entry Trajectory Planning with Range Discretization and Successive Convexification][research_liu_li_2022]
- [Liu and others, 2022, Research on Improved Cooperative Terminal Guidance Law of Multi-hypersonic Cruise Missiles][research_liu_chen_2022]
- [Liu and others, 2022, Three-dimensional coverage-based cooperative guidance law with overload constraints to intercept a hypersonic vehicle][research_liu_yan_2022_b]
- [Liu and others, 2023, Actuator Fault Detection for Hypersonic Flight Vehicle Model A Sliding Mode Observer Approach][research_liu_hu_2023]
- [Liu and others, 2023, Drag Reduction and Thermal Protection of the Combination of Aero Disk, Lateral Jet, and Rear Jet for Hypersonic Vehicle][research_liu_fang_2023]
- [Liu and others, 2023, Experimental Investigation on Off-Design Performances of Double-Swept Waverider][research_liu_liu_2023_b]
- [Liu and others, 2023, Gaussian Distribution-Based Control Vector Parameterization Method for Constrained Hypersonic Vehicle Reentry Trajectory Optimization][research_liu_liu_2023]
- [Liu and others, 2023, Huber-Based Robust Tracking Method of Hypersonic Cruise Vehicle][research_liu_mu_2023]
- [Liu and others, 2023, Radau Pseudospectral Method-Based Cooperative Re-entry Trajectory Optimization for Hypersonic Reentry Vehicle][research_liu_zhou_2023]
- [Liu and others, 2023, Reentry Guidance for Hypersonic Vehicle based on Reinforcement Learning][research_liu_cui_2023]
- [Liu and others, 2024, Fast finite-time extended state observer based fast nonsingular integral terminal sliding mode control for hypersonic glide vehicles][research_liu_xing_2024]
- [Liu and others, 2024, Intelligent Trajectory Prediction Algorithm for Hypersonic Vehicle Based on Sparse Associative Structure Model][research_liu_lu_2024]
- [Liu and others, 2024, Predictor-corrector reentry guidance for hypersonic glide vehicles based on high-precision analytical solutions][research_liu_zheng_2024]
- [Liu and others, 2024, Predictor-Corrector Reentry Guidance of Hypersonic Gliding Vehicle Satisfying No-Fly Zone Constraints with High Terminal State Accuracy][research_liu_zhang_2024]
- [Liu and others, 2024, Sequential Convex Programming for Reentry Trajectory Optimization Utilizing Modified hp-Adaptive Mesh Refinement and Variable Quadratic Penalty][research_liu_cui_2024]
- [Liu and others, 2024, Trajectory Optimization and Characteristic Analysis for Translunar Direct Abort Considering Reentry Constraints][research_liu_wang_2024]
- [Liu and others, 2025, An improved adaptive IMM-CKF method for tracking hypersonic glide vehicles via space-based radars][research_liu_deng_2025]
- [Liu and others, 2025, Bayesian intent inference of Reentry Glide Vehicle under no-fly zone constraints][research_liu_zhou_2025]
- [Liu and others, 2025, Data-Driven Online Modeling and Tracking of Hypersonic Glide Vehicles][research_liu_hu_2025]
- [Liu and others, 2025, Design of Morphing Mechanism for a Hypersonic Vehicle Model in Wind Tunnel Test][research_liu_jiang_2025]
- [Liu and others, 2025, Entry Guidance for Hypersonic Glide Vehicles via Two-Phase hp-Adaptive Sequential Convex Programming][research_liu_li_2025]
- [Liu and others, 2025, Key materials for extreme high-temperature environments Ultra-high-temperature ceramics and their composites][research_liu_wang_2025]
- [Liu and others, 2025, Mamba-Based Prediction Method for Trajectory Control Parameters of Hypersonic Glide Vehicles][research_liu_zhang_2025]
- [Liu and others, 2025, Preview Model Predictive Control for Hypersonic Flight Vehicles][research_liu_tang_2025]
- [Liu and others, 2025, Time-Cooperative Reentry Trajectory Optimization Based on LSTM and Sequential Convex Programming][research_liu_shao_2025]
- [Liu and others, 2026, A novel bump/sawtooth-lip integrated hypersonic inlet Design and comprehensive aerodynamic-stealth performance analysis][research_liu_ren_2026]
- [Liu and others, 2026, A Skip Trajectory Optimization Method for High-Speed Boost-Glide Flight Test Vehicles Based on IAPSO-NLP][research_liu_liu_2026]
- [Liu and others, 2026, Cascaded Model Predictive Control for Coordinated Formation of Hypersonic Glide Vehicle Swarms][research_liu_liang_2026]
- [Liu and others, 2026, Parametric modeling and optimization of hypersonic glide vehicles under stringent loading constraints][research_liu_xu_2026]
- [Liu and others, 2026, Time control entry guidance method for hypersonic glide vehicles based on deep reinforcement learning][research_liu_lei_2026]
- [Liu and others, 2026, Trajectory Tracking of Reentry Vehicle Based on KalmanNet with Time-Varying Observation Matrix][research_liu_chen_2026]
- [Liu and others, 2026, Traversability-Enhanced Long-Range Trajectory Recovery with Motion-Variation Modeling][research_liu_wu_2026]
- [Liu and others, 2026, Waverider Design Given Leading Edge from Axisymmetric Flow][research_liu_wu_2026_b]
- [Liu and Qiang, 2012, Numerical Simulation of the Aerodynamics and Aerothermal Heating for a Hypersonic Vehicle][research_liu_qiang_2012]
- [Liu and Shen, 2015, Rapid Smooth Entry Trajectory Planning for High Lift/Drag Hypersonic Glide Vehicles][research_liu_shen_2015]
- [Liu and Tang, 2013, Optimization of glide trajectory design Proportion derivative controller simulation][research_liu_tang_2013]
- [Liu Yuan and others, 2015, Sine tracking model of hypersonic target in near space based on radar detecting][research_liuyuan_zhangxiangyu_2015]
- [LIU, 1967, Skin-friction drag at supersonic-hypersonic speeds with transition][research_liu_1967]
- [Liu, 2009, Tracking the Warhead Among Objects Separation from the Reentry Vehicle in a Clear Environment][research_liu_2009]
- [Liu, 2017, Optimal guidance law of reentry vehicle with terminal interception and impact angle constraints][research_liu_2017]
- [Liu, 2020, Application of intelligent algorithm in trajectory optimization of hypersonic vehicle][research_liu_2020]
- [Liu, 2025, Thermal-Mechanical Coupling Analysis of Thermal Protection System Based on Finite Element Model][research_liu_2025]
- [Lloyd and Brown, 1979, Instability of Spinning Projectiles During Terminal Guidance][research_lloyd_brown_1979]
- [Lobanovsky, 2014, INTERFERENCE CONCEPT OF AERODYNAMIC DESIGN OF EFFECTIVE HYPERSONIC CONFIGURATIONS][research_lobanovsky_2014]
- [Lobbia and Suzuki, 2001, Design and analysis of payload-optimized waveriders][research_lobbia_suzuki_2001]
- [Lobbia and Suzuki, 2003, Numerical Investigation of Waverider-Derived Hypersonic Transport Configurations][research_lobbia_suzuki_2003]
- [Lobbia and Suzuki, 2014, Multidisciplinary Design Optimization of Hypersonic Transport Configurations using Waveriders][research_lobbia_suzuki_2014]
- [Lobbia, 2015, Optimization of Waverider-Derived Crew Reentry Vehicles using a Rapid Aerodynamics Analysis Approach][research_lobbia_2015]
- [Lobbia, 2017, Multidisciplinary Design Optimization of Waverider-Derived Crew Reentry Vehicles][research_lobbia_2017]
- [Lock and others, 2025, Hypersonic Glide Vehicle Shape and Trajectory Co-Design][research_lock_oberman_2025]
- [Lohsoonthorn and others, 2001, Eigenstructure vs Constrained H Design for Hypersonic Winged Cone][research_lohsoonthorn_jonckheere_2001]
- [Lonari and others, 2024, VISION Vehicle Infrared Signature Aware Off-Road Navigation][research_lonari_naber_2024]
- [LONG and HANUS, 1989, Aerodynamic design and analysis of a dual throat hypersonic nozzle][research_long_hanus_1989]
- [Long and others, 2020, Barrier Lyapunov function based sliding mode control for Mars atmospheric entry trajectory tracking with input saturation constraint][research_long_zhu_2020]
- [Long and others, 2026, Multidisciplinary modeling and dynamic Kriging assisted optimization for suborbital reusable launch vehicle][research_long_li_2026]
- [Longo, 2008, Aerothermodynamics Issues of the DLR Hypersonic Flight Experiment SHEFEX-I Invited][research_longo_2008]
- [Lorenz and Putnam, 2017, Optimal Hypersonic Trajectory Strategies for Supersonic Retropropulsion at Mars][research_lorenz_putnam_2017]
- [Lu and Hanson, 1998, Entry Guidance for the X-33 Vehicle][research_lu_hanson_1998]
- [Lu and others, 1997, Entry trajectory design for the X-33 vehicle][research_lu_hanson_1997]
- [Lu and others, 2000, Entry guidance by trajectory regulation][research_lu_shen_2000]
- [Lu and others, 2005, Adaptive Terminal Guidance for Hypervelocity Impact in Specified Direction][research_lu_doman_2005]
- [Lu and others, 2006, Adaptive Terminal Guidance for Hypervelocity Impact in Specified Direction][research_lu_doman_2006]
- [Lu and others, 2016, Adaptive Control with Pseudo-Control Hedging for a Hypersonic Air Vehicle][research_lu_zhang_2016_b]
- [Lu and others, 2016, Analytical solution on transient aerodynamic heating of hypersonic vehicle hot structure][research_lu_zhang_2016]
- [Lu and others, 2022, Research on Cooperative Target Assignment and Guidance Method of Hypersonic Glide Vehicle][research_lu_zheng_2022]
- [Lu and others, 2025, A Control Method for Thermal Structural Tests of Hypersonic Missile Aerodynamic Heating][research_lu_zhang_2025]
- [Lu and others, 2025, Two-Stage Differential Game Guidance Law with Terminal Angle and Hard Acceleration Constraints][research_lu_guo_2025]
- [Lu and Qian, 2024, Enhanced Trajectory Forecasting for Hypersonic Glide Vehicle via Physics-Embedded Neural ODE][research_lu_qian_2024]
- [Lu and Zhou, 2017, LQR tracking guidance law for hypersonic vehicle][research_lu_zhou_2017_b]
- [Lu and Zhou, 2017, Re-entry guidance for hypersonic vehicle satisfying no-fly zone constraints][research_lu_zhou_2017]
- [LU, 1991, Trajectory optimization and guidance for a hypersonic vehicle][research_lu_1991]
- [Lu, 1996, Entry guidance and trajectory control for reusable launch vehicles][research_lu_1996_b]
- [Lu, 1996, Nonlinear trajectory tracking guidance with application to a launch vehicle][research_lu_1996]
- [Lu, 1997, Entry Guidance and Trajectory Control for Reusable Launch Vehicle][research_lu_1997]
- [Lu, 1999, Regulation About Time-Varying Trajectories Precision Entry Guidance Illustrated][research_lu_1999]
- [Lu, 2005, Asymptotic Analysis of Quasi-Equilibrium Glide in Lifting Entry Flight][research_lu_2005]
- [Lu, 2006, Asymptotic Analysis of Quasi-Equilibrium Glide in Lifting Entry Flight][research_lu_2006]
- [Lu, 2008, Entry Trajectory Optimization with Analytical Feedback Bank Angle Law][research_lu_2008_b]
- [Lu, 2008, Predictor-Corrector Entry Guidance for Low-Lifting Vehicles][research_lu_2008]
- [Lu, 2014, Entry Guidance A Unified Method][research_lu_2014]
- [Lu, 2021, Disturbance observer-based backstepping control for hypersonic flight vehicles without use of measured flight path angle][research_lu_2021]
- [Lubing and others, 2020, DOB Identification and Anti-Disturbance Control for Hypersonic Flight Vehicle Systems][research_lubing_yangfei_2020]
- [Lukacs and Yakimenko, 2007, Trajectory-Shape-Varying Missile Guidance for Interception of Ballistic Missiles During the Boost Phase][research_lukacs_yakimenko_2007]
- [Lukacs and Yakimenko, 2008, Trajectory-Shaping Guidance for Interception of Ballistic Missiles During the Boost Phase][research_lukacs_yakimenko_2008]
- [Lunan, 1990, Waverider][research_lunan_1990]
- [Lunan, 2015, Waverider, A Revised Chronology][research_lunan_2015]
- [Luo and Baysal, 1999, Computational simulation of hypersonic vehicle separation from its booster][research_luo_baysal_1999]
- [Luo and Gao, 2015, Computer simulation on aerodynamic design of waverider vehicle][research_luo_gao_2015]
- [Luo and Li, 2011, Fuzzy dynamic characteristic model based attitude control of hypersonic vehicle in gliding phase][research_luo_li_2011]
- [Luo and others, 2003, Application of Taguchi Design Methods and Uniform Design Methods to Scramjet Propulsion System Optimization for Hypersonic Cruise Vehicle][research_luo_luo_2003]
- [Luo and others, 2014, Patched Corridor A Novel Lateral Logic for Skip Entry Guidance][research_luo_zhang_2014]
- [Luo and others, 2015, Skip entry guidance using numerical predictor-corrector and patched corridor][research_luo_zhang_2015]
- [Luo and others, 2019, Performance Evaluation of Symbolic Regression Methods on Hypersonic Aerodynamic Data Modeling][research_luo_chen_2019]
- [Luo and others, 2021, Effects of Coolants of Double Layer Transpiration Cooling System in the Leading Edge of a Hypersonic Vehicle][research_luo_miao_2021]
- [Luo and others, 2022, Adaptive finite-time prescribed performance attitude tracking control for reusable launch vehicle during reentry phase An event-triggered case][research_luo_wu_2022]
- [Luo and others, 2022, Performance analysis of the hypersonic vehicle with dorsal and ventral intake][research_luo_sun_2022]
- [Luo and others, 2023, Rapid reentry trajectory planning based on geometric-dynamic method][research_luo_lei_2023]
- [Luo and others, 2024, Picard-Chebyshev-Based Improved Sequential Convexification Method for Reentry Trajectory Planning][research_luo_li_2024]
- [Luo and others, 2025, Air-breathing wide-range vehicle configuration concepts with double-sided inlet based on the waverider theory][research_luo_sun_2025]
- [Luo and others, 2025, Fragility Analysis of Prescribed Performance Control for Waverider Vehicles][research_luo_he_2025]
- [LUO and SU, 2016, Hypersonic entry guidance design based on three-dimensional equilibrium glide space][research_luo_su_2016]
- [LUSTY and MIELE, 1966, Bodies of maximum lift-to-drag ratio in hypersonic flow][research_lusty_miele_1966]
- [Lv and others, 2014, Passive Waverider Method and Its Validation][research_lv_jiang_2014]
- [Lv and others, 2015, The Direct Measurement of Base Drag for Hypersonic Vehicles][research_lv_li_2015]
- [LV and others, 2019, Trajectory optimization for Long-Range Air-Defense Missile with a Constraint on Capability of Error Correction][research_lv_cai_2019]
- [Lv and others, 2023, Adaptive fixed-time quantized fault-tolerant attitude control for hypersonic reentry vehicle][research_lv_wang_2023]
- [Lv and others, 2024, Hypersonic vehicle terminal velocity improvement considering ramjet safety boundary constraint][research_lv_lan_2024]
- [Lv and others, 2026, Deep Reinforcement Learning-Driven Parameter Tuning for Adaptive Control Systems in Hypersonic Flight Vehicle][research_lv_zhang_2026]
- [Lv and Zhou, 2023, Adaptive Performance-Constrained Synchronization Control for Hypersonic Flight Vehicle Swarms A Novel Finite-Time Convergence Protocol Methodology][research_lv_zhou_2023]
- [Lyons, 1977, Cadmium telluride detector development and use in reentry vehicle applications][research_lyons_1977]
- [Lyu and others, 2018, Improved Design of Waverider Based on Mach Line Cutting of Compression Surfaces][research_lyu_jiang_2018]
- [Löhle and others, 2017, Experimental assessment of the performance of ablative heat shield materials from plasma wind tunnel testing][research_lohle_hermann_2017]
- [Ma and others, 2012, Modeling and Simulation Methodology of Multifield Coupling for Hypersonic Vehicle][research_ma_chao_2012]
- [Ma and others, 2014, Hypersonic lifting body aerodynamic shape optimization based on the multiobjective evolutionary algorithm based on decomposition][research_ma_yang_2014]
- [Ma and others, 2017, Aerodynamic Performance Analysis of A New Conception Hypersonic Aircraft][research_ma_zhong_2017]
- [Ma and others, 2019, Rapid Altitude Tracking for Air-Breathing Hypersonic Vehicle With Limited Angle of Attack][research_ma_du_2019]
- [Ma and others, 2021, Evaluation on Two Thermodynamic Systems Integrated Thermal Protection and Power Generation for a Hypersonic Vehicle Engine][research_ma_xie_2021]
- [Ma and others, 2022, Review of Research Methods for Hypersonic Vehicle Reentry Trajectory Planning][research_ma_yin_2022]
- [Ma and others, 2023, Hypersonic Vehicle Control Based on Deep Reinforcement Learning][research_ma_hu_2023]
- [Ma and others, 2024, Extended state observer-based fixed-time fault-tolerant attitude control for hypersonic reentry vehicle][research_ma_liu_2024]
- [MA and others, 2024, High-precision analytical solutions for Earth coverage of constellation equipped with reentry glide vehicles][research_ma_sun_2024]
- [Ma and others, 2024, Learning-Based Optimal Guidance for Hypersonic Reentry Using a Barrier Function][research_ma_chen_2024]
- [Ma and others, 2024, Trajectory optimization of hypersonic vehicle considering the quasi-static assumption of pitch motion][research_ma_yang_2024]
- [Ma and others, 2025, An efficient and high-precision aerodynamic modeling method for hypersonic vehicle optimization design][research_ma_xue_2025]
- [Ma and others, 2026, Aerodynamic Load Characterisation of Hypersonic Rudders][research_ma_wan_2026]
- [Ma and others, 2026, Research on Online Trajectory Optimization and Tracking Guidance Methods for Formation Phase of Reentry Vehicles][research_ma_li_2026]
- [Ma and She, 2011, Time-varying control via nominal trajectory linearization for an air-breathing hypersonic vehicle][research_ma_she_2011]
- [Machado, 2018, Evaluation of Reentry Dynamics of SARA platform Considering the Effects of Ablation in the Thermal Shield][research_machado_2018]
- [Mackle and Jahn, 2024, Efficient and Flexible Methodology for the Aerodynamic Shape Optimization of Hypersonic Vehicle Concepts in a High-Dimensional Design Space][research_mackle_jahn_2024]
- [Mackle and others, 2024, Developing a Co-Design Framework for Hypersonic Vehicle Aerodynamics and Trajectory][research_mackle_lock_2024]
- [Magister, 2012, Long Range Aircraft Trajectory Prediction][research_magister_2012]
- [Mahato and others, 2023, Aerodynamic Characterization of Hypersonic Launch Vehicle laden with exposed Scramjet based Cruise Vehicle][research_mahato_sarikonda_2023]
- [Mahmood and others, 2023, Flow across moving plate at separated stagnation point Features of corcione's correlation with Thompson and Troian slip and melting heat][research_mahmood_duraihem_2023]
- [Mahmoud and others, 2017, Ascent and Glide Trajectory Optimization for Hypersonic Vehicle][research_mahmoud_hao_2017]
- [Mahulikar and others, 2008, Transient aero-thermal mapping of passive Thermal Protection system for nose-cap of Reusable Hypersonic Vehicle][research_mahulikar_khurana_2008]
- [Mahulikar, 2005, Theoretical aerothermal concepts for configuration design of hypersonic vehicles][research_mahulikar_2005]
- [Mai and others, 2026, Intelligent Real-Time Trajectory Optimization Framework for Multiple Time-Coordinated Hypersonic Glide Vehicles With No-Fly Zone Avoidance][research_mai_li_2026]
- [Maigler and others, 2024, Predicting lift and drag coefficients during hypersonic Mars reentry using hyStrath][research_maigler_pessina_2024]
- [Maikapar, 1967, Optimum form of lifting bodies at hypersonic speeds][research_maikapar_1967]
- [Maikapar, 1993, Lift-to-drag ratio at supersonic speeds][research_maikapar_1993]
- [Maikapar, 1996, Comments on the choice of waverider shape][research_maikapar_1996]
- [Maione and others, 2026, Aerothermodynamic Analysis of a Blended Wing Body Re-entry Vehicle][research_maione_aprovitola_2026]
- [Maisaia, 2023, Optionally Piloted Hypersonic Aerospace Vehicle With Inflight Hydrogen Generation Propulsion system][research_maisaia_2023]
- [Maity and others, 2012, MPSP Guidance of a Solid Motor Propelled Launch Vehicle for a Hypersonic Mission][research_maity_padhi_2012]
- [Majumder and Kumar, 2023, Prescribed Performance Terminal Sliding Mode based Guidance with Impact Angle Constraints][research_majumder_kumar_2023]
- [Malinowski, 2020, Hypersonic Weapon as a New Challenge for the Anti-aircraft Defense Command and Control System][research_malinowski_2020]
- [Mall and others, 2024, Human-Class Mars Entry, Descent, and Landing Trajectory Optimization Using Indirect Methods][research_mall_levin_2024]
- [Mall and Taheri, 2020, Entry Trajectory Optimization for Mars Science Laboratory Class Missions Using Indirect Uniform Trigonometrization Method][research_mall_taheri_2020]
- [Mani and Haney, 1994, 3D CFD analysis of a SR71-waverider launch configuration][research_mani_haney_1994]
- [Manickavasagam and others, 2015, Trajectory Optimisation of Long Range and Air-to-Air Tactical Flight Vehicles][research_manickavasagam_sarkar_2015]
- [Manor and others, 2002, Aerothermodynamics Environments and Thermal Protection System Design for a Wave-Rider TSTO Second Stage][research_manor_lau_2002]
- [Mao and others, 2016, Reentry trajectory optimization for hypersonic vehicle based on improved Gauss pseudospectral method][research_mao_zhang_2016]
- [Mao and Yang, 2024, Trajectory tracking control of hypersonic flight vehicles with composite perturbations An ANN compensator approach][research_mao_yang_2024]
- [Maomao and others, 2021, A Multi-constrained Adaptive Predictor-Corrector Guidance Method for Ascent Phase of Hypersonic Vehicle][research_maomao_jun_2021]
- [Maorui Zhang and others, 2010, Reentry trajectory optimization of hypersonic vehicle with enhancing parametrization method][research_maoruizhang_yongsun_2010_b]
- [Maorui Zhang and others, 2010, Reentry trajectory optimization of hypersonic vehicle with minimum heat][research_maoruizhang_yongsun_2010]
- [Maples, 1979, Aerodynamic Heating of Conventional Weapons][research_maples_1979]
- [Marchetti and Minisci, 2021, Genetic Programming Guidance Control System for a Reentry Vehicle under Uncertainties][research_marchetti_minisci_2021]
- [Marchetti and others, 2024, Genetic Programming Guidance for the Reentry Trajectory of the ReFEx Vehicle][research_marchetti_redondogutierrez_2024]
- [Marcum, 2001, Computational Simulation of Unsteady, Viscous, Hypersonic Flow about Flight Vehicles with Store Separation][research_marcum_2001]
- [Marinescu and others, 1997, Minimum heat input optimal skip entry into Venus atmosphere][research_marinescu_ilin_1997]
- [Marini, 2001, Analysis of hypersonic compression ramp laminar flows under sharp leading edge conditions][research_marini_2001]
- [Markusic and others, 2018, Firefly A New Generation of Low Cost, Small Satellite Launch Vehicles Designed to Serve the Rapidly Growing Small Satellite Market][research_markusic_sabripour_2018]
- [Marley and Driscoll, 2017, Modeling an Active and Passive Thermal Protection System for a Hypersonic Vehicle][research_marley_driscoll_2017]
- [Marley and Driscoll, 2018, Optimization of an Active and Passive Thermal Protection System for a Scramjet-Powered Hypersonic Vehicle][research_marley_driscoll_2018]
- [Marley and Driscoll, 2022, Optimization of Active and Passive Thermal Protection Systems for a Hypersonic Vehicle][research_marley_driscoll_2022]
- [Marraffa and Smith, 1998, Aerothermodynamic Aspects of Entry Probe Heat Shield Design][research_marraffa_smith_1998]
- [Marrison and Stengel, 1998, Design of Robust Control Systems for a Hypersonic Aircraft][research_marrison_stengel_1998]
- [Marschall and Fletcher, 2010, High-enthalpy test environments, flow modeling and in situ diagnostics for characterizing ultra-high temperature ceramics][research_marschall_fletcher_2010]
- [Marschall, 2011, Testing and Modeling Ultra-High Temperature Ceramic UHTC Materials for Hypersonic Flight][research_marschall_2011]
- [Marshall, 2013, A Midcourse Correction For U.S. Missile Defense System][research_marshall_2013]
- [Martin and Boyd, 2015, Modeling of Heat Transfer Attenuation by Ablative Gases During the Stardust Reentry][research_martin_boyd_2015]
- [Marwaha and others, 2009, Integrated Guidance and Fault Tolerant Adaptive Control for Mars Entry Vehicle][research_marwaha_singh_2009]
- [MASAKI and YAKURA, 1968, Transitional boundary layer considerations for the heating analyses of lifting reentry vehicles][research_masaki_yakura_1968]
- [Masarath Jabeen, 2024, Combined Convection Stagnation-Point and Transfer of Heat of a Jeffery Fluid][research_masarathjabeen_2024]
- [Matheny and Smith, 2026, Aerothermodynamic Analysis and High-Speed Schlieren Imaging of an Undergraduate-Designed Hypersonic Glide Vehicle][research_matheny_smith_2026]
- [Matienzo and others, 1985, Thermal Protection System for the Space Shuttle External Tank Applications of Instrumental Methods of Analysis][research_matienzo_shah_1985]
- [Matsuda and others, 2013, Numerical Study of Thermochemical Nonequilibrium Flow Around Reentry Capsule and Estimation of Aerodynamic Heating][research_matsuda_kihara_2013]
- [Matsumoto and others, 2013, Accurate Real-Time Prediction Guidance Using Numerical Integration for Reentry Spacecraft][research_matsumoto_kondoh_2013]
- [Matsumoto and others, 2015, IMU-DM Integrated Navigation and Terminal Reentry Guidance for Accurate Guided Reentry Flight][research_matsumoto_kondoh_2015]
- [Matsunaga and others, 2017, Aerodynamic Heating Prediction of an Inflatable Reentry Vehicle in a Hypersonic Wind Tunnel][research_matsunaga_takahashi_2017]
- [MATSUNO and others, 2014, Multidisciplinary Design Optimization of Long or Short Range Hypersonic Aircraft][research_matsuno_tsuchiya_2014]
- [Matsuyama and others, 2003, Trajectory-Based Heating Analysis of Galileo Probe Entry Flowfield with Radiation and Ablation][research_matsuyama_ohnishi_2003]
- [Matthews and Jones, 2005, Design and Test of a Modular Waverider Hypersonic Intake][research_matthews_jones_2005]
- [Matthews and Jones, 2006, Design and Test of a Modular Waverider Hypersonic Intake][research_matthews_jones_2006]
- [Matthews and others, 2003, Design and Test of a Low Drag Hypersonic Intake][research_matthews_jones_2003]
- [Matthews, 1993, Aerothermal Test Methodology and Techniques for the Development of Hypersonic Vehicles][research_matthews_1993]
- [Maughmer and others, 1993, Validation of engineering methods for predicting hypersonic vehicle control forces and moments][research_maughmer_ozoroski_1993]
- [Mauriello and others, 2024, Multidisciplinary Design Assessment of Promising Aerodynamic Shapes for Hypersonic Passenger Transport][research_mauriello_wilken_2024]
- [Mavris and Graham, 2000, Implementation of Parametric Anaylsis to the Aerodynamic Design of a Hypersonic Strike Fighter][research_mavris_graham_2000]
- [Maxwell and Hoang, 2016, Two Phase Thermal Protection of the Hypersonic Leading Edge][research_maxwell_hoang_2016]
- [Maxwell and Phoenix, 2017, Morphable Hypersonic Waverider and Trajectory Optimized for Atmospheric Entry][research_maxwell_phoenix_2017]
- [Maxwell, 2016, Hypersonic Waverider Stream Surface Actuation for Variable Design Point Operation][research_maxwell_2016]
- [Maxwell, 2017, Efficient Design of Viscous Waveriders with CFD Verification and Off-Design Performance Analysis][research_maxwell_2017_b]
- [Maxwell, 2017, Shapeable Hypersonic Waverider Entry Vehicles][research_maxwell_2017]
- [Mayanna and others, 2006, Adaptive Guidance for Terminal Area Energy Management TAEM of Reentry Vehicles][research_mayanna_grimm_2006]
- [Maynard and others, 2025, Hypersonic Point-to-Point Transportation Benchmark Study Boost-Glide Versus Cruise Methodology][research_maynard_patel_2025]
- [Mayrhofer and Sachs, 1999, A contribution to mission safety for a two-stage hypersonic vehicle][research_mayrhofer_sachs_1999]
- [Mazaheri, 2013, High-Energy Atmospheric Reentry Test Aerothermodynamic Analysis][research_mazaheri_2013]
- [Mazzaracchio and Marchetti, 2010, A probabilistic sizing tool and Monte Carlo analysis for entry vehicle ablative thermal protection systems][research_mazzaracchio_marchetti_2010]
- [Mbagwu and Driscoll, 2018, An Examination of Vehicle Design Tradeoffs and Trajectory Optimization for Trimmed Scramjet-Powered Hypersonic Vehicles On Ascent][research_mbagwu_driscoll_2018]
- [Mbagwu and others, 2023, Maximizing Lift-to-Drag and Thrust-to-Drag Ratios for Trimmed Hypersonic Vehicles][research_mbagwu_dalle_2023]
- [MCANALLY and ENGEL, 1979, Reentry aerodynamic heating methods for sounding rocket payloads][research_mcanally_engel_1979]
- [McClary and Putnam, 2021, Assessment of Hypersonic Separation Dynamics For Drag Modulation Systems at Mars][research_mcclary_putnam_2021]
- [McCormick and others, 2010, Uncertainty Quantification and Propagation Methods for Hypersonic Airbreathing Launch Vehicle System Analysis][research_mccormick_wakayama_2010]
- [McCOWN and DAVI, 1967, Radiative vs ablative heat shield concepts for manned lifting entry vehicles][research_mccown_davi_1967]
- [McCOWN and others, 1966, Design and testing of a hot redundant structure concept for a hypersonic flight vehicle][research_mccown_barrett_1966]
- [Mccurry, 1996, Lockheed Martin launch vehicle application to small planetary missions][research_mccurry_1996]
- [McDonald and Mavris, 2000, Formulation, realization, and demonstration of a process to generate aerodynamic metamodels for hypersonic cruise vehicle design][research_mcdonald_mavris_2000]
- [Mceowen and Acikmese, 2022, Hypersonic Entry Trajectory Optimization via Successive Convexification with Abstracted Control][research_mceowen_acikmese_2022]
- [Mceowen and others, 2023, High-Accuracy 3-DoF Hypersonic Reentry Guidance via Sequential Convex Programming][research_mceowen_kamath_2023]
- [Mceowen and others, 2025, Auto-Tuned Primal-Dual Successive Convexification for Hypersonic Reentry Guidance][research_mceowen_calderone_2025_b]
- [Mceowen and others, 2025, Autotuned Primal-Dual Successive Convexification for Reentry Guidance][research_mceowen_calderone_2025]
- [McFarland, 2001, Hybridizing contemporary glide slopes to provide vertical guidance for GPS approaches][research_mcfarland_2001]
- [McGrory, 2001, Hypersonic Maneuvering Vehicle Simulations Using Real-Gas, Unstructured Navier-Stokes Software][research_mcgrory_2001]
- [McINTOSH, 1973, Effect of Hypersonic Nonlinear Aerodynamic Loading on Panel Flutter][research_mcintosh_1973]
- [McNamara, 2012, Entry Atmospheric Flight Control Authority Impacts on GNandC and Trajectory Performance for Orion Exploration Flight Test 1][research_mcnamara_2012]
- [McQuaid and Brehm, 2024, Simulating the BOLT Hypersonic Vehicle using an Overset Near Body Cartesian Solver][research_mcquaid_brehm_2024]
- [McQuellin and Buttsworth, 2024, Free-Flight of a Propelled Axisymmetric Vehicle in a Hypersonic Ground-Test Facility][research_mcquellin_buttsworth_2024]
- [Mease and Kremer, 1994, Shuttle entry guidance revisited using nonlinear geometric methods][research_mease_kremer_1994]
- [Mease and others, 1999, Re-entry trajectory planning for a reusable launch vehicle][research_mease_teufel_1999]
- [Meckler, 1964, HEAT TRANSFER MEASUREMENTS AT MACH 8 ON AN AERODYNAMICALLY CONTROLLABLE WINGED RE-ENTRY CONFIGURATION. PART OF AN INVESTIGATION OF HYPERSONIC FLOW SEPARATION AND CONTROL CHARACTERISTICS][research_meckler_1964]
- [Meckler, 1965, PRESSURE MEASUREMENTS AT MACH 8 ON AN AERODYNAMICALLY CONTROLLABLE WINGED REENTRY CONFIGURATION. PART OF AN INVESTIGATION OF HYPERSONIC FLOW SEPARATION AND CONTROL CHARACTERISTICS][research_meckler_1965]
- [Medri and others, 2013, Production of UHTC Complex Shapes and Architectures][research_medri_sciti_2013]
- [Medyanik and Vlahopoulos, 2016, Atomistic Simulation Studies of the Effects of Defects on Thermal Properties of Ultra High Temperature Ceramics][research_medyanik_vlahopoulos_2016]
- [Mehra, 1971, A comparison of several nonlinear filters for reentry vehicle tracking][research_mehra_1971]
- [Mehta, 2023, Numerical Computation of Heat Transfer on Reentry Capsules at Mach 5][research_mehta_2023]
- [Mei and others, 2020, Coupled simulation for reentry ablative behavior of hypersonic vehicles][research_mei_shi_2020]
- [Melville and Helmich, 2021, Common Hypersonic Boost Glide RandD][research_melville_helmich_2021]
- [Melville and Helmich, 2021, Hypersonic Weapons Summit Promoting Leadership in Hypersonic Development Among Research Institutions][research_melville_helmich_2021_b]
- [MENEES and others, 1985, Aerothermodynamic heating and performance analysis of a high-lift aeromaneuvering AOTV concept][research_menees_brown_1985]
- [Menees and others, 1987, Aerothermodynamic heating and performance analysis of a high-lift aeromaneuvering AOTV concept][research_menees_brown_1987]
- [Menezes and others, 2005, Drag reduction by controlled base flow separation for missile shaped bodies flying at hypersonic Mach number][research_menezes_sun_2005]
- [Meng and others, 2016, Fault-tolerant predictive control for Hypersonic Vehicle in reentry phase based on SMDO][research_meng_jiang_2016]
- [Meng and others, 2019, Adaptive fault-tolerant attitude tracking control of hypersonic vehicle subject to unexpected centroid-shift and state constraints][research_meng_jiang_2019]
- [Meng and others, 2021, Distributed Target Assignment Method of Phased-Array Radar Network for Detecting Hypersonic-Glide Vehicle][research_meng_tian_2021]
- [Meng and others, 2023, Adaptive attitude angle constrained fault-tolerant control of hypersonic vehicle with unknown centroid shift][research_meng_liu_2023]
- [Meng and others, 2025, Low-Speed Performance Analysis of Double Swept Waverider with Wing Dihedral][research_meng_bai_2025_b]
- [Meng and others, 2025, Planform-customized waverider design using flows with variable mach numbers][research_meng_bai_2025]
- [Meng and Tian, 2020, Phased-Array Radar Task Scheduling Method for Hypersonic-Glide Vehicles][research_meng_tian_2020]
- [Menk and others, 2025, Computational and Experimental Evaluation of Sonic Boom From a HTV-2 Type Hypersonic Boost Gliding Vehicle with High-Enthalpy Inlet Conditions][research_menk_candler_2025]
- [Menssen, 2026, Trajectory Analysis for Manned Spaceflight Aerodynamic Heating of a Two-Person Lunar-Return Vehicle][research_menssen_2026]
- [Mercatelli and others, 2011, Intrinsic spectral selectivity in ultra-high temperature ceramics for solar applications][research_mercatelli_sani_2011]
- [Merkin and others, 2011, The development of forced convection heat transfer near a forward stagnation point with Newtonian heating][research_merkin_nazar_2011]
- [Merkulov and others, 2025, Integrated Midcourse-Terminal Guidance with Delayed Target Selection][research_merkulov_shalumov_2025]
- [Merrill and Bleck, 1986, Isentropic trajectory analysis of long range transport over the Pacific][research_merrill_bleck_1986]
- [Merrill, 1989, Modeling Long-Range Transport Using Trajectory Techniques][research_merrill_1989]
- [Merritt and Kramer, 1997, Field test of active tracking of a ballistic missile in the boost phase][research_merritt_kramer_1997]
- [Merritt and others, 1996, Active tracking of a ballistic missile in the boost phase][research_merritt_cusumano_1996]
- [Mesalles Ripoll and others, 2021, Aerothermodynamic Uncertainty in Lifting and Boost-Glide Entry Trajectories][research_mesallesripoll_campbell_2021]
- [Meyer and others, 1999, Hypersonic drag and heat transfer reduction using a forward facing jet][research_meyer_nelson_1999]
- [Mhapsekar and Maurya, 2025, Redefining Hypersonic Nose Cones A Machine Learning Approach to Wave Drag Minimization][research_mhapsekar_maurya_2025]
- [Mi and others, 2022, Hypersonic Vehicle Tube-MPC Fault-Tolerant Control Method Based on Multi-objective Trajectory Optimization][research_mi_hu_2022]
- [Miao and others, 2026, A trajectory optimization method of hypersonic gliding vehicle based on differential flatness][research_miao_wang_2026]
- [MICOL, 1991, Aerothermodynamic measurement and prediction for a modified orbiter at Mach 6 and 10 in air][research_micol_1991]
- [Micol, 1995, Aerothermodynamic measurement and prediction for modified orbiter at Mach 6 and 10][research_micol_1995]
- [Micol, 1995, Hypersonic aerodynamic/aerothermodynamic testing capabilities at Langley Research Center - Aerothermodynamic Facilities Complex][research_micol_1995_b]
- [MIELE and DAMOULAKIS, 1969, Maximum lift-to-drag ratio airfoils at moderate supersonic speeds][research_miele_damoulakis_1969]
- [Miele and Hull, 1963, SLENDER BODIES OF REVOLUTION HAVING MINIMUM TOTAL DRAG AT HYPERSONIC SPEEDS][research_miele_hull_1963]
- [Miele and Pritchard, 1963, SLENDER, TWO DIMENSIONAL BODIES HAVING MINIMUM TOTAL DRAG AT HYPERSONIC SPEEDS][research_miele_pritchard_1963]
- [Mifsud and others, 2012, A case study on the aerodynamic heating of a hypersonic vehicle][research_mifsud_estruchsamper_2012]
- [Mihalea and Florea, 2024, Vehicle Ego-Trajectory Segmentation Using Guidance Cues][research_mihalea_florea_2024]
- [Miller and others, 1997, Subsonic aerodynamics of an osculating cones waverider][research_miller_argrow_1997]
- [Miller, 1985, Refinement of an 'alternate' method for measuring heating rates in hypersonic wind tunnels][research_miller_1985]
- [MILLER, 1990, Langley hypersonic aerodynamic/aerothermodynamic testing capabilities - Present and future][research_miller_1990]
- [MILLER, 1992, Hypersonic aerodynamic/aerothermodynamic testing capabilities at Langley Research Center][research_milleriii_1992]
- [Miller, 1993, Aerothermodynamic Measurement Techniques Employed in NASA Langley Hypersonic Facilities][research_miller_1993]
- [MILLER, 2004, GLOBAL STRIKE CAPABILITIES THE BALLISTIC MISSILE OPTION][research_miller_2004]
- [Miller, 2005, Computational Aerothermodynamic Datasets for Hypersonic Heat Transfer on Reentry Vehicles][research_miller_2005]
- [Miller-Oana and Corral, 2015, High-Temperature Isothermal Oxidation of Ultra-High Temperature Ceramics Using Thermal Gravimetric Analysis][research_milleroana_corral_2015]
- [Minami and Tsukamoto, 2006, A Subscale Flight Experiment for the Approach and Landing of a Lifting Body Re-entry Vehicle][research_minami_tsukamoto_2006]
- [Ming and others, 2017, Research on the GFSINS/GPS/CNS integrated navigation technology for hypersonic vehicle][research_ming_ming_2017_b]
- [Ming and others, 2017, The Fast-optimization for Configuration of Hypersonic Vehicle Based on Flight Performance][research_ming_ming_2017]
- [Ming-Guang and others, 2006, Fast Optimization of Constrained Reentry Trajectory][research_mingguang_qiong_2006]
- [MingLin, 2022, Skip reentry trajectory planning based on multi-phase Gauss pseudospectral method][research_minglin_2022]
- [Minwen and Dayi, 2014, Guidance law for low-lift skip reentry subject to control saturation based on nonlinear predictive control][research_minwen_dayi_2014]
- [MIRELS and ELLINWOOD, 1970, Slender bodies of minimum drag in hypersonic viscous flow][research_mirels_ellinwood_1970]
- [MIRELS and MULLEN, 1965, Aerodynamic blast simulation in hypersonic tunnels][research_mirels_mullen_1965]
- [MIRELS and MULLEN, 1966, Errata "Aerodynamic Blast Simulation in Hypersonic Tunnels"][research_mirels_mullen_1966]
- [Mirmirani and others, 2005, Modeling for Control of a Generic Airbreathing Hypersonic Vehicle][research_mirmirani_wu_2005]
- [Mishra and Sushnigdha, 2025, Comparison of Nonlinear Control Techniques Utilized for Re-Entry Trajectory Tracking][research_mishra_sushnigdha_2025]
- [Misko, 1999, Design of the optimal nozzle of a hypersonic flight vehicle for given overall dimensions and moment][research_misko_1999]
- [Mitanchey and others, 2024, Influence of the Atmospheric Plasma Sheath on the RCS of a Hypersonic Reentry Vehicle][research_mitanchey_pagani_2024]
- [MITCHEL, 1967, Evaluation of ablative composites containing high-reflectance fillers in simulated superorbital reentry][research_mitchel_1967]
- [Mitroshin and others, 1983, SYNTHESIS OF TERMINAL CONTROL SEQUENCE ALGORITHMS WITH THE USE OF MOVING-POINT GUIDANCE][research_mitroshin_glinsky_1983]
- [MIYAZAWA and others, 1993, Guidance and control law for automatic landing flight experiment of reentry space vehicle][research_miyazawa_ishikawa_1993]
- [Mizener and others, 2017, Preliminary Installed Performance of Rotating Detonation Engines onto Waverider Configurations][research_mizener_lu_2017]
- [Mizener and others, 2019, Performance Sensitivities of Rotating Detonation Engines Installed onto Waverider Forebodies][research_mizener_lu_2019]
- [Mo and others, 2022, Numerical investigations of the slot blowing technique on the hypersonic vehicle for drag reduction][research_mo_su_2022]
- [Mo and others, 2022, The Robust Adaptive Controller for Hypersonic Flight Vehicle Based on ADRC and PSMC][research_mo_liu_2022]
- [Mo and others, 2023, Adaptive Sliding Mode Control with RBF Approximation for Hypersonic Flight Vehicle][research_mo_lu_2023]
- [Mocio, 2001, Demonstrating low cost access to space for small satellites - The DoD Space Test Program Medium Launch Vehicle 2005 Mission][research_mocio_2001]
- [Mohamed and others, 2017, Buoyancy effect on stagnation point flow past a stretching vertical surface with Newtonian heating][research_mohamed_salleh_2017]
- [Mohring and others, 2021, Antenna In-Situ Performance Analysis for the Hypersonic Flight Vehicle HEXAFLY Employing measurement data in a simulation model][research_mohring_gabler_2021]
- [Molchanov, 2024, Fast Radar for the Detection of Hypersonic Missiles and UASs][research_molchanov_2024]
- [Molina and others, 1996, Pre-flight aerothermodynamic analysis of the Atmospheric Reentry Demonstrator][research_molina_simeonides_1996]
- [Molvik and others, 1993, A hypersonic waverider research vehicle with hydrocarbon scramjet propulsion - Design and analysis][research_molvik_bowles_1993]
- [MOLVIK and others, 1993, Analysis of a hypersonic waverider research vehicle with a hydrocarbon scramjet engine][research_molvik_bowles_1993_b]
- [Mondal and Padhi, 2018, Angle-Constrained Terminal Guidance Using Quasi-Spectral Model Predictive Static Programming][research_mondal_padhi_2018]
- [Mondal and Padhi, 2020, Correction Angle-Constrained Terminal Guidance Using Quasi-Spectral Model Predictive Static Programming][research_mondal_padhi_2020]
- [Mongibello and de Luca, 2008, Critical Discharge in Actively Cooled Wing Leading Edge of a Reentry Vehicle][research_mongibello_deluca_2008]
- [MONNOYER, 1993, Hypersonic configuration optimization with an Euler/boundary layer coupling technique][research_monnoyer_1993]
- [Monroe and Boyd, 2025, Circuit Analysis of an Electron Transpiration Cooling System for Hypersonic Leading Edges][research_monroe_boyd_2025]
- [Monroe and Boyd, 2026, Cooling of a Hypersonic Leading Edge via Electron Emission and Absorption][research_monroe_boyd_2026]
- [Monteiro dos Santos Rodrigues da Silva and others, 2022, Preliminary design of an aerospace vehicle using airbreathing propulsion system for hypersonic speed][research_monteirodossantosrodriguesdasilva_delimacostasalazar_2022]
- [Monteverde and others, 2008, Processing and properties of ultra-high temperature ceramics for space applications][research_monteverde_bellosi_2008]
- [Monteverde and others, 2013, Effects of LaB6 addition on arc-jet convectively heated SiC-containing ZrB2-based ultra-high temperature ceramics in high enthalpy supersonic airflows][research_monteverde_alfano_2013]
- [MOODY and others, 1982, Coupled reentry vehicle heatshield/antenna window ablation][research_moody_groener_1982]
- [Mooij and Barkana, 2005, Stability Analysis of an Adaptive Guidance and Control System applied to a Winged Re-Entry Vehicle][research_mooij_barkana_2005]
- [Mooij and Hanninen, 2009, Distributed Global Trajectory Optimization of a Moderate Lift-to-Drag Re-Entry Vehicle][research_mooij_hanninen_2009]
- [Mooij and others, 2006, Entry Trajectory Simulation Using ESA Mars Climate Database Version 4.1][research_mooij_huot_2006]
- [Mooij, 2004, Model Reference Adaptive Guidance for Re-entry Trajectory Tracking][research_mooij_2004]
- [Mooij, 2004, Parametric Control-Variable Analysis in Support of Re-entry Trajectory Optimisation][research_mooij_2004_b]
- [Moorhouse and Suchomel, 2001, Exergy methods applied to the hypersonic vehicle challenge][research_moorhouse_suchomel_2001]
- [Moosavi and others, 2009, Aerothermodynamics Optimization of a Re-Entry Vehicle on a Specified Trajectory Using Parallel Genetic Algorithms][research_moosavi_mirzaei_2009]
- [Mor and Livne, 2006, Multidisciplinary Design Optimization of Reentry Vehicles Trajectory Optimization and Sensitivities][research_mor_livne_2006]
- [Mor and Livne, 2007, Coupled Aeroelastic / Trajectory Optimization of Reentry Vehicles][research_mor_livne_2007]
- [Mor and others, 2025, Production and characterization of conical shaped ultra-high temperature ceramics matrix composites by slip casting and pressure-less sintering][research_mor_taraborelli_2025]
- [Moran and others, 2021, Numerical tool for quantifying energy deposition effects on representative hypersonic vehicle structures][research_moran_capra_2021]
- [Moran and others, 2023, Wind-Tunnel based Free-Flight Testing of a Viscous Optimised Hypersonic Waverider][research_moran_mcquellin_2023]
- [Morani and others, 2026, Guidance and Control Algorithms of a Hypersonic Launch Vehicle][research_morani_fruncillo_2026]
- [Moravszki and others, 2018, Tunnel/Predictor Display for Trajectory Control in Hypersonic Flight][research_moravszki_rohacs_2018]
- [Moreira and others, 2021, Thermal analysis of hypersonic reactive flows on the SARA Brazilian satellite reentry trajectory][research_moreira_wolf_2021]
- [Moreira and others, 2022, Convective Heat Transfer in Hypersonic Non-Equilibrium Reactive Flows Over the Fire II Reentry Capsule][research_moreira_wolf_2022_b]
- [Moreira and others, 2022, Numerical Simulation of Non-Equilibrium Hypersonic Flows for the Reentry Trajectory of a Reusable Satellite][research_moreira_wolf_2022]
- [Morelli, 2008, Flight Test Experiment Design for Characterizing Stability and Control of Hypersonic Vechicles][research_morelli_2008]
- [Morelli, 2009, Flight-Test Experiment Design for Characterizing Stability and Control of Hypersonic Vehicles][research_morelli_2009]
- [Morgan, 1961, LEADING EDGE AND NOSE CAP MATERIALS-PYROLYTIC GRAPHITE][research_morgan_1961]
- [MORGAN, 1971, Advanced techniques in the testing and evaluation of terminal guidance subsystems][research_morgan_1971]
- [Morgan, 2016, Midcourse guidance with terminal handover constraint][research_morgan_2016]
- [Mori and others, 2002, Glide-back Flying Test Bed Concept for Hypersonic Flight Test][research_mori_tsuchiya_2002]
- [Morimoto and Chuang, 1998, Minimum-fuel trajectory along entire flight profile for a hypersonic vehicle with constraint][research_morimoto_chuang_1998]
- [Morimoto and Kinefuchi, 2025, Effect of the vehicle nose radius on radio wave-plasma interference in hypersonic flight][research_morimoto_kinefuchi_2025]
- [Morio and others, 2009, Flatness-based hypersonic reentry guidance of a lifting-body vehicle][research_morio_cazaurang_2009]
- [Morita and others, 2020, MDO of Hypersonic Waverider with Trajectory-Aero-Structure Coupling][research_morita_tsuchiya_2020]
- [Morreale and Wagnild, 2021, Direct Numerical Simulations of the Conventional Prompt Strike Vehicle?s Ogive at Hypersonic Flight Conditions][research_morreale_wagnild_2021]
- [Morrell and others, 2014, Development of a Hypersonic Aircraft Design Optimization Tool][research_morrell_munk_2014]
- [Morris and others, 2022, Investigation of Oxidation Effects in Porous Ultra-High Temperature Ceramics][research_morris_povolny_2022]
- [Morris and others, 2023, Effects of oxidation on the effective thermomechanical properties of porous ultra-high temperature ceramics in compression via computational micromechanics and MPM][research_morris_povolny_2023]
- [MORRISON and others, 1981, The hypersonic flow field over a reentry vehicle indented nose configuration][research_morrison_yanta_1981]
- [MORTH and SPEYER, 1961, Divergence From Equilibrium Glide Path at Supersatellite Velocities][research_morth_speyer_1961]
- [MORTH, 1972, An explicit automatic terminal energy management guidance technique for space shuttle][research_morth_1972]
- [Moshman and Proulx, 2014, Range Improvements in Gliding Reentry Vehicles from Thrust Capability][research_moshman_proulx_2014]
- [Mostafa and Nooraliei, 2009, Modeling of Boost-Phase Ground Based Interception against Long and Mid Range Attacking Ballistic Misiles][research_mostafa_nooraliei_2009]
- [Mosunov and others, 2010, Paralympic swimmer`s hydrodynamic quality in "entry into the water glide" phase on pedestal starts accomplishment][research_mosunov_mosunova_2010]
- [Moszee and Moszee, 1997, In-flight H2O production for hypersonic vehicle active cooling and auxiliary propulsion][research_moszee_moszee_1997]
- [Motoyama and others, 2001, Thermal protection and drag reduction with use of spike in hypersonic flow][research_motoyama_mihara_2001]
- [Moura and Borges Ribeiro, 2025, Flight Control Longitudinal Law for a Hypersonic Waverider Vehicle][research_moura_borgesribeiro_2025_b]
- [Moura and Borges Ribeiro, 2025, Hypersonic Waverider Vehicle Flight Control Autopilot System Design and Implementation][research_moura_borgesribeiro_2025]
- [Moura and Borges Ribeiro, 2025, Hypersonic waverider vehicle flight control latero-directional law implementation][research_moura_borgesribeiro_2025_c]
- [Moura and Borges Ribeiro, 2025, Scramjet Engine Control Law for a Hypersonic Waverider Vehicle][research_moura_borgesribeiro_2025_d]
- [Moura and Borges Ribeiro, 2025, Total Energy Control System for a Hypersonic Waverider Vehicle][research_moura_borgesribeiro_2025_e]
- [Moura and Borges Ribeiro, 2026, COOLING SYSTEM MODEL INTEGRATED INTO THE COMPLETE SIMULATION FRAMEWORK OF A HYPERSONIC VEHICLE][research_moura_borgesribeiro_2026]
- [Moura and Ribeiro, 2024, Dynamic-thermodynamic coupling of a hypersonic vehicle][research_moura_ribeiro_2024]
- [Mowry and Grasso, 2020, The Evolution of Medium-/Heavy-lift and Reusable Launch Vehicles and Its Implications for Smallsat Access to Space][research_mowry_grasso_2020]
- [Moylan and others, 2013, Investigation of the Physical Phenomena Associated with Rain Impacts on Supersonic and Hypersonic Flight Vehicles][research_moylan_landrum_2013]
- [Mu and Wang, 2025, Analysis of Near-Field Electromagnetic Scattering Characteristics of the Hypersonic Vehicle][research_mu_wang_2025]
- [Mudrik and Oshman, 2023, Terminal-Set-Based Optimal Stochastic Guidance][research_mudrik_oshman_2023]
- [Mukhopadhyay and others, 2013, Ultra High Temperature Ceramics][research_mukhopadhyay_raju_2013]
- [Mungiguerra and others, 2024, Test and Simulation in High-Enthalpy Atmospheric Re-Entry Conditions of Multi-Phase Ultra-High-Temperature Ceramics][research_mungiguerra_silvestroni_2024]
- [Munipalli and others, 2005, Automated Design Optimization for Hypersonic Plasma-Aerodynamics][research_munipalli_subbarao_2005]
- [Murayama and others, 1992, Chemical and thermal processes on hypersonic shock layer][research_murayama_sasoh_1992]
- [MURBACH, 1993, A hypersonic vehicle approach to planetary exploration][research_murbach_1993]
- [Murillo and Lu, 2010, Fast Ascent Trajectory Optimization for Hypersonic Air-Breathing Vehicles][research_murillo_lu_2010]
- [Murphy and others, 2004, Overview of Transonic to Hypersonic Stage Separation Tool Development for Multi-Stage-To-Orbit Concepts][research_murphy_buning_2004]
- [Murray and Steelant, 2009, Methodologies involved in the Design of LAPCAT-MR1 a Hypersonic Cruise Passenger Vehicle][research_murray_steelant_2009]
- [Murray and Tartabini, 2001, Development of a Mars airplane entry, descent, and flight trajectory][research_murray_tartabini_2001]
- [Musa and others, 2022, Assessment of new pressure-corrected design method for hypersonic internal waverider intake][research_musa_huang_2022]
- [Musa and others, 2024, Isolator shape transition impact on hypersonic internal waverider intake flow distortion][research_musa_huang_2024]
- [Musa and others, 2024, Startability analysis of hypersonic overboard spillage internal waverider intake based on new basic flowfield][research_musa_huang_2024_b]
- [Musa and others, 2025, Withdrawn Effect of Isolator Shape Transition on Hypersonic Internal Waverider Intake Performance][research_musa_huang_2025]
- [MUSAL, 1962, PLASMA FREQUENCY AND ELECTRON COLLISION FREQUENCY CHARTS FOR HYPERSONIC VEHICLE EQUILIBRIUM FLOW FIELDS IN AIR][research_musal_1962]
- [Müller and Petervari, 2025, Tracking of Hypersonic Glide Vehicles Radar Resource Load Reduction by using a Non-Ballistic Reentry Process Model][research_muller_petervari_2025]
- [Nagai and others, 2011, Experimental Study of Heat Transfer Measurement using Temperature-Sensitive Paint for High-Temperature Application in Hypersonic Flow][research_nagai_swamura_2011]
- [Nagai and others, 2013, Color Signal Integration for Color Discrimination along a Long-range Apparent Motion Trajectory][research_nagai_kimura_2013]
- [Nagamatsu and Li, 1960, Hypersonic Flow Near the Leading Edge of a Flat Plate][research_nagamatsu_li_1960]
- [Nagamatsu and others, 1961, DESIGN FEATURES OF THE GENERAL ELECTRIC RESEARCH LABORATORY HYPERSONIC SHOCK TUNNEL][research_nagamatsu_sheer_1961]
- [NAGAMATSU and SHEER, 1960, Hypersonic Shock Wave-Boundary Layer Interaction and Leading Edge Slip][research_nagamatsu_sheer_1960]
- [Nagashetty and others, 2017, Tomographic Visualization of the Hypersonic Flow Field over a Waverider][research_nagashetty_medhi_2017]
- [Nagdewe and Shevare, 2006, Hypersonic Flow Past a Vehicle by Using Relaxation Method with Turbulence][research_nagdewe_shevare_2006]
- [Nagpal and others, 2023, Hypersonic Aerodynamic Characterization of a Winged Body Re-entry Configuration Using Chemical Non-Equilibrium CFD Simulations][research_nagpal_g_2023]
- [Nair and others, 2003, Reynolds Averaged Navier-Stokes Based Aerodynamic Analysis of Inlet for a Hypersonic Research Vehicle][research_nair_kumar_2003]
- [Naitoh and others, 2011, A Wide-range single engine operated from startup to hypersonic condition][research_naitoh_nakamura_2011]
- [Najafiyazdi, 2005, An Engineering Method for Aerodynamic Heating Prediction of Biconic Configurations in 3-D Hypersonic Flow][research_najafiyazdi_2005]
- [Najam, 2014, Basic PARTS of the Suborbital Reusable Launch Vehicle Research Market "Game"][research_najam_2014]
- [Najib and others, 2014, Stagnation point flow over a stretching/shrinking cylinder with prescribed surface heat flux][research_najib_bachok_2014]
- [Najson and Mease, 2006, Computationally Inexpensive Guidance Algorithm for Fuel-Efficient Terminal Descent][research_najson_mease_2006]
- [Nakatani and others, 2009, An Experimental Study on Aerodynamic Design of Hypersonic Airplane][research_nakatani_taguchi_2009]
- [Nakatani and others, 2011, Evaluation of Aerodynamic Performance of a Hypersonic Experimental Aircraft][research_nakatani_taguchi_2011]
- [Nakayama and others, 2018, A Dual-Mode Scramjet Combustor employing a Jet Fuel for Hypersonic Flight Vehicle][research_nakayama_edanaga_2018]
- [Nakayama and others, 2018, Apparent shift in long-range motion trajectory by local pattern orientation][research_nakayama_harada_2018]
- [Nam and others, 2025, Attack Intent Inference of Hypersonic Glide Vehicle Based on a Unified Dynamics and Decision-Making Model][research_nam_lee_2025]
- [NARAIN, 1991, High angle of attack aerodynamics of a glide vehicle][research_narain_1991]
- [Nardo and others, 1961, EXPERIMENTAL PRESSURE, TEMPERATURE, AND STRAIN MEASUREMENTS ON ABLATING HEMISPHERICAL NOSE CONES IN HYPERSONIC FLOW. TEST SERIES 2][research_nardo_erickson_1961]
- [Nardo and Sadler, 1962, HEAT TRANSFER AND TEMPERATURE DISTRIBUTION IN A HEMISPHERICAL NOSE CONE IN HYPERSONIC FLOW][research_nardo_sadler_1962]
- [NARDO, 1972, Aerodynamic Characteristics of Two-Dimensional Waverider Configurations][research_nardo_1972]
- [Naresh Kumar and others, 2017, Hypersonic flight vehicle trajectory optimization using pattern search algorithm][research_nareshkumar_ikram_2017]
- [Nassif and others, 2026, Multi-point surrogate-based aerodynamic optimisation of a generic hypersonic waverider][research_nassif_hoste_2026]
- [Natali and others, 2013, An Armadillo-Like Flexible Thermal Protection System for Inflatable Decelerators A Novel Paradigm][research_natali_rallini_2013]
- [Nathan and Bindu, 2005, Low Temperature Ablative Heat Shield for Re-Entry Vehicles][research_nathan_bindu_2005]
- [Nawaz and others, 2012, Dufour and Soret Effects in an Axisymmetric Stagnation Point Flow of Second Grade Fluid with Newtonian Heating][research_nawaz_alsaedi_2012]
- [Needels and Alonso, 2023, Efficient Global Optimization for Multidisciplinary Conceptual Design of Hypersonic Vehicles][research_needels_alonso_2023]
- [NEEDHAM, 1965, A heat-transfer criterion for the detection of incipient separation in hypersonic flow][research_needham_1965]
- [Neely and others, 2015, Re-entry Trajectory Modelling for the Microgravity Experiment Recoverable Satellite][research_neely_woodward_2015]
- [NEFF, 1972, Ablative nose shape change effects on re-entry vehicle aerodynamic performance][research_neff_1972]
- [Nelson, 1996, An airfield take-off concept for large and small payload reusable launch vehicles][research_nelson_1996]
- [Nelson, 2000, Carryover for hypersonic '+' and 'x' configuration delta fin missiles][research_nelson_2000]
- [Nenarokomov and others, 2016, Research and development of heat flux sensor for ablative thermal protection of spacecrafts][research_nenarokomov_alifanov_2016]
- [Neubacher and others, 2002, Experimental Investigation of a Hypersonic Inlet for the TSTO-Configuration ELAC][research_neubacher_henckels_2002]
- [Neumann, 1989, Defining the Aerothermodynamic Methodology][research_neumann_1989]
- [Neuwerth and others, 1999, Reynolds Number Effects on Low-Speed Aerodynamics of a Hypersonic Configuration][research_neuwerth_peiter_1999]
- [Nevrekar and others, 2012, Maximum Range Glide of a Supersonic Aircraft in the Presence of Wind][research_nevrekar_striz_2012]
- [Newberry, 1995, The conceptual design of deck-launched waverider configured aircraft][research_newberry_1995]
- [Newberry, 1998, The conceptual design of deck-launched waverider-configured aircraft][research_newberry_1998]
- [Newell and Zakharov, 2007, Communication with Hypersonic Vehicles via Nonlinear Plasma Processes][research_newell_zakharov_2007]
- [NEWMAN and others, 1992, On the aerodynamics/dynamics of store separation from hypersonic aircraft][research_newman_fulcher_1992]
- [Ng and others, 2011, Thermomechanical behaviour of a damaged thermal protection system experimental correlation and influence of hypersonic flow][research_ng_friedmann_2011]
- [NGO and others, 1993, Hypersonic vehicle structural weight prediction using parametric modeling, finite element modeling, and structural optimization][research_ngo_koshiba_1993]
- [Ngo and others, 2017, Inverse Force Determination on a Small Scale Launch Vehicle Model using a Dynamic Balance][research_ngo_powell_2017]
- [Nguyen and Aleti, 2025, Utilizing Small Satellite Launch Vehicle - A Cross-Border Collaboration for Space Mission Australia India Technology Research and Innovation Space MAITRI by Space Machines Company and New Space India Limited][research_nguyen_aleti_2025]
- [Nguyen and others, 2026, Convexity of intercept time in short-range re-entry vehicle defence how to optimally intercept a fast re-entry vehicle travelling in a lofted trajectory][research_nguyen_urquhart_2026]
- [Ni and others, 2025, Adaptive Active Defense Guidance for Hypersonic Vehicle with Incomplete Information Based on Reinforcement Learning][research_ni_qiu_2025]
- [Nie and Liu, 2013, CFD Turbulent Model and Grid Dependency of Hypersonic Aerodynamic Heating Calculation Accuracy][research_nie_liu_2013]
- [Nie and others, 2023, Reinforcement Learning Control for Hypersonic Morphing Flight Vehicle with Identification of Dynamic Parameter][research_nie_zhang_2023]
- [Niederstrasser, 2022, The small launch vehicle survey a 2021 update The rockets are flying][research_niederstrasser_2022]
- [Nikolaevich Blinov and others, 2016, Exploring the Possibilities for Improving the Performance of the Adapters used for Launching Multiple Small Space Vehicles on a Single Launch Vehicle][research_nikolaevichblinov_vladimirovichshalay_2016]
- [NING and others, 2007, Integrated Entry Guidance for Reusable Launch Vehicle][research_ning_zhang_2007]
- [Nisar and others, 2017, Establishing microstructure-mechanical property correlation in ZrB2-based ultra-high temperature ceramic composites][research_nisar_ariharan_2017]
- [Nisar and others, 2020, A perspective on challenges and opportunities in developing high entropy-ultra high temperature ceramics][research_nisar_zhang_2020]
- [Nisar and others, 2022, Ultra-high temperature ceramics Aspiration to overcome challenges in thermal protection systems][research_nisar_hassan_2022]
- [Nisar and others, 2023, Synthesis of Hf6Ta2O17 superstructure via spark plasma sintering for improved oxidation resistance of multi-component ultra-high temperature ceramics][research_nisar_zhang_2023]
- [Nishio and Hagiwara, 1998, Investigation of wake behind hypersonic vehicle by electric discharge method][research_nishio_hagiwara_1998]
- [Nishio and others, 2001, Experimental study of wake behind hypersonic vehicle utilizing the electric discharge method][research_nishio_nakamura_2001]
- [Nithin Chandran and others, 2019, Synthesis of Zirconium diboride based ultra high temperature ceramics via preceramic route][research_nithinchandran_devapal_2019]
- [Niu and others, 2017, WITHDRAWN Effects of angle of attack on IR radiation for a hypersonic boost-glide vehicle][research_niu_yuan_2017]
- [Niu and others, 2018, Nonlinear fuzzy fault-tolerant control of hypersonic flight vehicle with parametric uncertainty and actuator fault][research_niu_chen_2018]
- [NIU and others, 2019, Infrared radiation characteristics of a hypersonic vehicle under time-varying angles of attack][research_niu_yuan_2019]
- [Niu and others, 2019, Target Detection Algorithm for Hypersonic Vehicle Based on Wideband Radar Echo Model][research_niu_su_2019]
- [Noftz and others, 2023, Performance Evaluation of an Internal Osculating Waverider Inlet][research_noftz_shuck_2023]
- [NOMURA and YAMAMOTO, 1996, Aerothermodynamic Studies on Hypersonic Vehicle][research_nomura_yamamoto_1996]
- [Nomura, 1983, Correlation of hypersonic stagnation point heat transfer at low Reynolds numbers][research_nomura_1983]
- [Norris, 2006, Mach 8 High Reynolds Number Static Stability Capability Extension Using a Hypersonic Waverider at AEDC Tunnel 9][research_norris_2006]
- [Norsell, 2005, Multistage Trajectory Optimization with Radar Range Constraints][research_norsell_2005]
- [Novotny and others, 2024, Aerodynamic Exergy-Based Analysis and Optimization of the Generic Hypersonic Vehicle Using FUN3D][research_novotny_rumpfkeil_2024]
- [Novotny and others, 2024, Thermal Exergy-Based Analysis of the Generic Hypersonic Vehicle][research_novotny_neiferd_2024]
- [Nowak and others, 2021, High temperature interaction between molten Ni50Al50 alloy and ZrB2 ultra-high temperature ceramics][research_nowak_bruzda_2021]
- [NOZHNITSKY and SMIRNOV, 1995, Ceramic, carbon-carbon and other composite materials tests at high temperature][research_nozhnitsky_smirnov_1995]
- [NUSCA, 1993, AEROTHERMODYNAMIC ANALYSIS FOR AXISYMMETRIC PROJECTILES AT SUPERSONIC/HYPERSONIC SPEEDS][research_nusca_1993]
- [Nykiel and others, 2026, Exploration of hexagonal, layered carbides and nitrides as ultra-high temperature ceramics][research_nykiel_wyatt_2026]
- [O'Brien and Lewis, 2000, RBCC engine-airframe integration on an osculating cone waverider vehicle][research_obrien_lewis_2000]
- [O'Brien and Lewis, 2001, Transonic through hypersonic performance of an RBCC engine-airframe integrated vehicle][research_obrien_lewis_2001]
- [O'Brien and Lewis, 2002, Rapid Transonic Aerodynamic Prediction for Hypersonic Lifting Bodies][research_obrien_lewis_2002]
- [O'Connor, 2019, Early Days of Phased Array Radars for Ballistic Missile Detection and Tracking][research_oconnor_2019]
- [O'Driscoll and others, 2021, Hypersonic foldable Aeroshell for THermal protection using ORigami HATHOR evaluation of deployable structural rigidity during descent][research_odriscoll_bruce_2021]
- [O'HARE and ANDERSON, 1993, Maneuvering a reentry body via magnetogasdynamic forces][research_ohare_andersonjr_1993]
- [O'Neal and others, 2026, Hypersonic Aerodynamic Stability Study of a KRUPS Re-Entry Vehicle][research_oneal_desilva_2026]
- [O'Neill and Lewis, 1992, Optimized Scramjet Integration on a Waverider][research_oneill_lewis_1992]
- [O'Neill and Lewis, 1993, Design tradeoffs on scramjet engine integrated hypersonic waverider vehicles][research_oneill_lewis_1993]
- [O.S. KUPACH, 2018, Analyzing the US Conventional Prompt Global Strike Program][research_oskupach_2018]
- [Oberkampf and Aeschliman, 1992, Joint computational/experimental aerodynamics research on a hypersonic vehicle. I - Experimental results][research_oberkampf_aeschliman_1992]
- [Ochi, 2004, DESIGN OF A FLIGHT CONTROLLER FOR HYPERSONIC FLIGHT EXPERIMENT VEHICLE][research_ochi_2004]
- [ODABAS and SARIGUL-KLIJN, 1992, On the coupled thermomechanical analysis of hypersonic flight vehicle structures][research_odabas_sarigulklijn_1992]
- [Odion Iyinomen, 2022, Plasma Preheating Technology for Ablation Studies of Hypersonic Reentry Vehicles][research_odioniyinomen_2022]
- [OHASHI and others, 2018, Aerodynamic instability of flare-type membrane inflatable vehicle in suborbital reentry demonstration][research_ohashi_takahashi_2018]
- [Ohkage and others, 2025, Heat Shield Properties of Lightweight Ablator Series for Transfer Vehicle Systems with Different Laminated Structures Under High Enthalpy Flow Environments][research_ohkage_okuyama_2025]
- [Ohlmeyer and others, 2010, Tracking of Spiraling Reentry Vehicles with Varying Frequency using the Unscented Kalman Filter][research_ohlmeyer_menon_2010]
- [Ohtake, 1998, Thermal analysis of the thermal protection system for the re-entry vehicle][research_ohtake_1998]
- [Okamoto and others, 2002, Low-Speed Aerodynamic Characteristics and Stage Separation Simulation of TSTO Vehicles][research_okamoto_yamamoto_2002]
- [OKUNO and WATANABE, 1992, Optimal launch trajectory of a hypersonic research vehicle][research_okuno_watanabe_1992]
- [Oliveira Júnior and others, 2021, AERODYNAMIC HEATING OF AN HYPERSONIC AIRBREATHING VEHICLE AT MACH NUMBER 5.8][research_oliveirajunior_marinho_2021]
- [Olivier, 1995, Influence of the velocity gradient on the stagnation point heating in hypersonic flow][research_olivier_1995]
- [Olsen, 1965, LOCAL AERODYNAMIC PARAMETERS FOR SUPERSONIC AND HYPERSONIC FLUTTER ANALYSES][research_olsen_1965]
- [OLSTAD, 1969, Correlations for stagnation-point radiative heat transfer][research_olstad_1969]
- [OLSZEWSKI, 1990, Automated terminal guidance for a Shuttle rendezvous to Space Station Freedom][research_olszewski_1990]
- [Olynick, 1998, Trajectory-Based Thermal Protection System Sizing for an X-33 Winged Vehicle Concept][research_olynick_1998]
- [Onozeki and others, 2026, Combined Aerodynamic and Structural Study on Hypersonic Aircraft With Lightweight Morphing Wing From Takeoff to Cruise][research_onozeki_shimizu_2026]
- [Opila and others, 2006, Columbia tragedy High-temperature materials chemistry and thermodynamic considerations of the breached wing leading edge][research_opila_jacobson_2006]
- [Oppenheimer and Doman, 2006, A Hypersonic Vehicle Model Developed With Piston Theory][research_oppenheimer_doman_2006]
- [Oppenheimer and others, 2008, Canard-Elevon Interactions on a Hypersonic Vehicle][research_oppenheimer_skujins_2008]
- [Oppenheimer and others, 2008, Viscous Effects for a Hypersonic Vehicle Model][research_oppenheimer_doman_2008]
- [Orlandini and others, 2026, Numerical Assessment of a Multilayer Thermal Protection System of Inflatable Shields for Aerocapture and Reentry Missions][research_orlandini_paciorri_2026]
- [Orrù and Cao, 2013, Comparison of Reactive and Non-Reactive Spark Plasma Sintering Routes for the Fabrication of Monolithic and Composite Ultra High Temperature Ceramics UHTC Materials][research_orru_cao_2013_b]
- [Orrù and Cao, 2013, Self-Propagating High-Temperature Synthesis SHS and Spark Plasma Sintering SPS of Zr-, Hf-, and Ta-Based Ultra-High Temperature Ceramics][research_orru_cao_2013]
- [Orrù and Cao, 2019, Ultra-high temperature ceramics by spark plasma sintering][research_orru_cao_2019]
- [Ortloff, 1968, LOW DENSITY TRANSITIONAL REGIME DRAG COEFFICIENTS FOR SLENDER COLD WALL CONICAL VEHICLES IN HYPERSONIC FLOW][research_ortloff_1968]
- [OSSIN and ARONIN, 1975, Refractory metal air vane leading edge for an advanced ballistic missile defense /BMD/ interceptor][research_ossin_aronin_1975]
- [Ostapenko, 1983, Bodies of minimal wave drag in a swirling hypersonic flow][research_ostapenko_1983]
- [Otsu and others, 1999, Effect of ablative gas on the radiative environment around the MUSES-C reentry capsule][research_otsu_suzuki_1999]
- [Otsu and others, 2011, Impact of Lift Force by Electromagnetic Flow Control on the Reentry Trajectory][research_otsu_katsurayama_2011]
- [Otsu and others, 2015, Effect of New Electron Impact Ionization on the Aerodynamic Heating Environment for Super-Orbital Reentry Vehicles][research_otsu_yamada_2015]
- [OTSU, 2016, Control of Aerodynamic Characteristics of Lifting Reentry Vehicle with Applied Magnetic Field][research_otsu_2016]
- [OTSU, 2018, New Magnetic Field Setup for Electromagnetic Flow Control of Lifting Reentry Vehicle][research_otsu_2018]
- [Ouyang and others, 2026, Terminal Guidance Methods for FPV Drone Precision Strike under Seeker Field-of-View Constraints][research_ouyang_wang_2026]
- [Ouzts and others, 2009, The Role of Guidance, Navigation, and Control in Hypersonic Vehicle Multidisciplinary Design and Optimization][research_ouzts_soloway_2009]
- [Ouzts, 2008, Mode Transition Design Considerations for an Airbreathing Combined-Cycle Hypersonic Vehicle][research_ouzts_2008]
- [Owotunse and others, 2023, Lateral Control of Air-breathing Hypersonic Vehicle Using Model Predictive Control][research_owotunse_ogwumike_2023]
- [Page and Rogers, 1977, Guidance and control of maneuvering reentry vehicles][research_page_rogers_1977]
- [Pai and others, 2019, 2D analysis of waverider in hypersonic flow][research_pai_chandy_2019]
- [Paiva, 1998, Navy theater ballistic missile defense boost multispectral discrimination requirements for low-resolution detection, classification, and high-resolution aimpoint selection][research_paiva_1998]
- [Palmer and others, 1995, A heating analysis and thermal protection system sizing of a lifting body single-stage-to-orbit vehicle][research_palmer_henline_1995]
- [Palmer and others, 1997, High-Fidelity Thermal Protection System Sizing of Reusable Launch Vehicle][research_palmer_henline_1997]
- [Palmer and others, 1997, Stagnation point heat transfer in superorbital expansion tubes][research_palmer_morgan_1997]
- [Palmer and Rao, 2022, Mars Entry Optimal Trajectory Generation, Guidance, and Control][research_palmer_rao_2022]
- [Palmer, 2020, Hypersonic Vehicle for Space Access Using Hydrocarbon Fuel][research_palmer_2020]
- [Palumbo and others, 2017, Reentry Trajectory Optimization for Mission Analysis][research_palumbo_morani_2017]
- [Pan and others, 2009, Computation and Analysis of Aeroheating on Hypersonic Inlet Leading Edge][research_pan_tian_2009]
- [Pan and others, 2014, Numerical investigation of rarefaction effects in the vicinity of a sharp leading edge][research_pan_gao_2014]
- [Pan and others, 2020, 3D guidance for hypersonic reentry gliders based on analytical prediction][research_pan_peng_2020]
- [Pan and others, 2025, A Novel Attack Missile Guidance Method Considering the Terminal Angle Constraint of the Attack Missile-Target-Defense Missile Game][research_pan_ma_2025]
- [Panagiotopoulos and others, 2005, Entry Trajectory Aerothermodynamics of Space Vehicles in Planetary Atmospheres][research_panagiotopoulos_margaris_2005]
- [Panagiotopoulos and others, 2006, Aerothermodynamic Analysis and Real Gas Flow Properties of Spacecraft Hypersonic Entry Flight][research_panagiotopoulos_margaris_2006]
- [Panerai and others, 2009, Testing of the EXPERT Thermal Protection System Junction in a Plasma Wind Tunnel][research_panerai_olivier_2009]
- [Panesi and Martin, 2020, Radiative transmission and absorption within the ablative heat shield of hypersonic vehicles][research_panesi_martin_2020]
- [Pang and others, 2021, A calculation approach for shock layer radiation and transmittance towards hypersonic infrared homing vehicle][research_pang_shi_2021]
- [Pang and others, 2025, Aerospace Vehicle Engine Nozzle External Thermal Protection System Design Factor Analysis][research_pang_du_2025]
- [Papadopoulos and Subrahmanyam, 2006, Trajectory Coupled Aerothermodynamics Modeling for Atmospheric Entry Probes at Hypersonic Velocities][research_papadopoulos_subrahmanyam_2006]
- [Park and Ahn, 1998, Stagnation-point heat transfer rates for Pioneer-Venus probes][research_park_ahn_1998]
- [Park and Park, 2017, Reentry trajectory and survivability estimation of small space debris with catalytic recombination][research_park_park_2017]
- [Park and Shin, 2024, Thermal-Structural Coupled Analysis and Design of a Reentry Capsule with Ablative Thermal Protection Systems][research_park_shin_2024]
- [Park, 2005, Calculation of Stagnation-Point Heating Rates Associated with Stardust Vehicle][research_park_2005]
- [Park, 2007, Calculation of Stagnation-Point Heating Rates Associated with Stardust Vehicle][research_park_2007]
- [Park, 2011, Viscous Shock Layer Calculation of Stagnation-Region Heating Environment in Neptune Aerocapture][research_park_2011]
- [Parker and others, 2006, Approximate Feedback Linearization of an Air-Breathing Hypersonic Vehicle][research_parker_serrani_2006]
- [Parker and others, 2007, Control-Oriented Modeling of an Air-Breathing Hypersonic Vehicle][research_parker_serrani_2007]
- [PARSONS ENGINEERING SCIENCES INC PASADENA CA, 1991, Environmental Impact Analysis Process. Environmental Assessment Air Force Small Launch Vehicle, Vandenberg Air Force Base, Edwards Air Force Base, and San Nicolas Island, CA][research_parsonsengineeringsciencesincpasadenaca_1991]
- [Pasagada and others, 2022, Electron beam sintering EBS process for Ultra-High Temperature Ceramics UHTCs and the comparison with traditional UHTC sintering and metal Electron Beam Melting EBM processes][research_pasagada_yang_2022]
- [Paschal and others, 2001, Integrated terminal guidance and automatic pilot using subspace-stabilization][research_paschal_tournes_2001]
- [Passera, 1960, Conditional-Switching Terminal Guidance A Terminal Guidance Technique for Satellite Rendezvous][research_passera_1960]
- [Paus and Well, 1996, Optimal ascent guidance for a hypersonic vehicle][research_paus_well_1996]
- [Paydayesh and Kokabi, 2015, Highly filled organoclay/phenolic resin nanocomposite as an ablative heat shield material][research_paydayesh_kokabi_2015]
- [Payne and Edwards, 1997, Impartiality in pre-entry guidance for adults in further education colleges][research_payne_edwards_1997]
- [PAYNTER, 1988, CFD TECHNOLOGY FOR HYPERSONIC VEHICLE DESIGN][research_paynter_1988]
- [Pegg and others, 1995, Low-speed wind tunnel tests of two waverider configuration models][research_pegg_hahne_1995]
- [Pei and others, 2018, Global fast terminal sliding mode guidance law for maneuvering target interception][research_pei_lin_2018]
- [Pei and others, 2021, Online Reentry Trajectory Optimization Using Modified Sequential Convex Programming for Hypersonic Vehicle][research_pei_fan_2021]
- [Peigin and Désidéri, 2001, Parallel implementation of genetic algorithms to the solution for the space vehicle reentry trajectory problem][research_peigin_desideri_2001]
- [Peipei and others, 2017, Hypersonic aerodynamic characteristics of lifting bodies having variations in body shape][research_peipei_junbo_2017]
- [Pelton and Madry, 2019, Global Launch Vehicle Systems for Potential Small Satellite Deployment][research_pelton_madry_2019]
- [Pelton and Madry, 2020, Global Launch Vehicle Systems for Potential Small Satellite Deployment][research_pelton_madry_2020]
- [Peng and others, 2014, A new dynamic calibration method for IMU deterministic errors of the INS on the Hypersonic Cruise Vehicles][research_peng_zhi_2014]
- [Peng and others, 2014, Backstepping control for longitudinal dynamics of hypersonic flight vehicle][research_peng_peng_2014]
- [Peng and others, 2015, RETRACTED Thermal protection mechanism of heat pipe in leading edge under hypersonic conditions][research_peng_he_2015]
- [Peng and others, 2019, Adaptive Fault Tolerant Control of Hypersonic Flight Vehicle with State Constraints using Barrier Lyapunov Function][research_peng_qi_2019]
- [Peng and others, 2019, Rapid Aerodynamic Shape Optimization With Payload Size Constraints for Hypersonic Vehicle][research_peng_feng_2019]
- [Peng and others, 2020, Adaptive fault tolerant control for hypersonic flight vehicle system with state constraints][research_peng_qi_2020]
- [Peng and Qi, 2019, Adaptive Fault-tolerant Controller for Hypersonic Flight Vehicle with State Constraints Using Integral Barrier Lyapunov Function][research_peng_qi_2019_b]
- [Peng and Wang, 2012, Estimating of Aerodynamic and Analysis of Aeroelasticity for Hypersonic Projectile][research_peng_wang_2012]
- [Peng Peng and others, 2013, Dynamic RCS feature of ballistic missile for detection and classification in the boost phase][research_pengpeng_tongchuangming_2013]
- [Pengxin and others, 2015, A kind of engineering trajectory oscillation eliminated control method for suborbital reentry vehicle][research_pengxin_feng_2015]
- [Penty Geraets and McGilvray, 2019, Stagnation Point Heat Flux Measurements in a Plasma Wind Tunnel Using a Diamond Heat Transfer Gauge][research_pentygeraets_mcgilvray_2019]
- [Pereira Lara and others, 2018, HEAT FLUX AND THERMODYNAMIC PROPERTIES ANALYSIS AT THE STAGNATION POINT AND THE BLUNT REGION OF THE 14-X S SCRAMJET ENGINE][research_pereiralara_toro_2018]
- [Perini, 1975, Compilation and correlation of stagnation convective heating rates on spherical bodies][research_perini_1975]
- [PERKINS and TANNAS, 1967, Simulation evaluation of closed form reentry guidance][research_perkins_tannasjr_1967]
- [Perlini and others, 2026, A Multi-Fidelity Bayesian Optimization Framework for Hypersonic Vehicle Design][research_perlini_bertolini_2026]
- [Perminov, 1969, Wing of given volume with maximum lift/drag ratio in hypersonic flow][research_perminov_1969]
- [Perrier, 1989, Industrial Methodologies for the Design of Hypersonic Vehicles][research_perrier_1989]
- [Persoons and others, 2011, A general correlation for the stagnation point Nusselt number of an axisymmetric impinging synthetic jet][research_persoons_mcguinn_2011]
- [Peter Korzun, 2017, U.S. PROMPT GLOBAL STRIKE CONCEPT FAILS TO MAKE RUSSIA KNEEL][research_peterkorzun_2017]
- [PETLEY and DZIEDZIC, 1993, Water cooling system for an air-breathing hypersonic test vehicle][research_petley_dziedzic_1993]
- [Pettinari and others, 2012, Detection of scramjet unstart in a hypersonic vehicle model][research_pettinari_corradini_2012]
- [Pezzella and others, 2014, Aerodynamic Characterization of HEXAFLY Scramjet Propelled Hypersonic Vehicle][research_pezzella_marini_2014]
- [Pezzella and Viviani, 2016, Aerodynamic performance analysis of a winged re-entry vehicle from hypersonic down to subsonic speed][research_pezzella_viviani_2016]
- [Pezzella, 2011, Aerodynamic and aerothermodynamic trade-off analysis of a small hypersonic flying test bed][research_pezzella_2011]
- [Pezzella, 2013, Hypersonic environment assessment of the CIRA FTB-X re-entry vehicle][research_pezzella_2013]
- [Pezzella, 2015, Assessment of the aerodynamic and aerothermodynamic performance of a high-lift reentry vehicle][research_pezzella_2015]
- [Pfaff, 1968, LIFT-TO-DRAG RATIOS OF SEMISPAN DELTA WING CONFIGURATIONS AT SUPERSONIC AND HYPERSONIC MACH NUMBERS][research_pfaff_1968]
- [Pham and Nguyen, 2025, Optimization of variable-direction long-range trajectory for the unpowered flight vehicle][research_pham_nguyen_2025]
- [Pham and others, 2020, OPTIMIZATION OF LONG-RANGE TRAJECTORY FOR AN UNPOWERED FLIGHT VEHICLE][research_pham_nguyen_2020]
- [PHILLIPS and CRUZ, 1991, Super/hypersonic aerodynamic characteristics for a transatmospheric vehicle concept having a minimum drag forebody][research_phillips_cruz_1991]
- [Phoenix and Maxwell, 2018, The Mach 5 to 3.5 Morphing Waverider Optimal Actuation Location Selection][research_phoenix_maxwell_2018]
- [Phoenix and others, 2017, Morphing High-Temperature Surfaces for Shapeable Hypersonic Waverider Vehicles][research_phoenix_maxwell_2017]
- [Phoenix and others, 2019, Mach 5-3.5 Morphing Waverider Accuracy and Aerodynamic Performance Evaluation][research_phoenix_maxwell_2019]
- [Piao and others, 2018, Synthesis of attitude control for statically unstable hypersonic vehicle with low-frequency aero-servo-elastic effect][research_piao_yang_2018]
- [Piccirillo and others, 2023, Noise Prediction for Mach 8 Waverider vehicle during Take-Off and Landing][research_piccirillo_viola_2023]
- [Pichon and Barreteau, 2012, Thermal Protection Systems Heritage - Development Status - Perspectives][research_pichon_barreteau_2012]
- [Pichon and others, 2006, Thermal Protection Systems Technologies For Re-Entry Vehicles][research_pichon_soyris_2006]
- [Piet-Lahanier and Serre, 2017, Trajectory and guidance scheme design for free flight test of hypersonic vehicle][research_pietlahanier_serre_2017]
- [Pike, 2006, Minimum forebody drag in hypersonic continuum and rarefied flows][research_pike_2006]
- [Pike, 2013, Hypersonic minimum drag forebodies with blunt leading edges][research_pike_2013]
- [Ping and others, 2017, The nonlinear anti-windup control of hypersonic glide vehicles with input saturation and uncertainties][research_ping_yanli_2017]
- [Ping Li and others, 2010, Quasi-equilibrium glide trajectory design of waverider-based hypersonic vehicle][research_pingli_wanchunchen_2010]
- [Pinto and others, 2023, Representation of hypersonic glide vehicles as fluctuating radar targets][research_pinto_whyman_2023_b]
- [Pinto and others, 2023, Statistical analysis of hypersonic glide vehicle radar cross section][research_pinto_whyman_2023]
- [Pionessa and Kinzel, 2024, Correction Understanding Heat Transfer Effects on Hypersonic Flow Implications for Aerodynamic Design][research_pionessa_kinzel_2024_b]
- [Pionessa and Kinzel, 2024, Understanding Heat Transfer Effects on Hypersonic Flow Implications for Aerodynamic Design][research_pionessa_kinzel_2024]
- [Pisano and Whitfield, 2024, Characterization of a Hypersonic Waverider in Low-Speed Flight][research_pisano_whitfield_2024]
- [Pittman and Dillon, 1977, Vortex lattice prediction of subsonic aerodynamics of hypersonic vehicle concepts][research_pittman_dillon_1977]
- [PLATUS, 1983, Angular motion influence on reentry vehicle ablation or erosion asymmetry formation][research_platus_1983]
- [Platus, 1985, Angular motion influence on re-entry vehicle ablation or erosion asymmetry formation][research_platus_1985]
- [Pokiya and others, 2022, High-precision computational guidance in terminal phase with impact angle, lead angle and lateral acceleration constraints][research_pokiya_sharma_2022]
- [Polisano and others, 2024, Signal Processing Methods for Long-Range UAV-SAR Focusing with Partially Unknown Trajectory][research_polisano_grassi_2024]
- [Pollack, 2009, Evaluating Conventional Prompt Global Strike][research_pollack_2009]
- [Pollack, 2015, Boost-glide Weapons and US-China Strategic Stability][research_pollack_2015]
- [Pollock and others, 2023, Effects of Aerothermal Shape Distortion on Hypersonic Vehicle Performance in Cruise][research_pollock_moran_2023]
- [Pollock and Wild, 2024, Preliminary Design of a Thermally Morphing Hypersonic Vehicle Flap][research_pollock_wild_2024]
- [Polsgrove and others, 2017, Mission and design sensitivities for human Mars landers using Hypersonic Inflatable Aerodynamic Decelerators][research_polsgrove_thomas_2017]
- [Polyanskii, 1967, Aerodynamic characteristics of a slender wedge in a nonequilibrium hypersonic flow][research_polyanskii_1967]
- [POPE, 1968, Stagnation-point convective heat transfer in frozen boundary layers][research_pope_1968]
- [Poplavskaya, 2002, Viscous Shock Layer on a Cone in Hypersonic Flow][research_poplavskaya_2002]
- [Portis and others, 2024, Evaluating Reduced-Order Methods for Hypersonic Vehicle Aerodynamics][research_portis_dambrosio_2024]
- [Poteet, 1998, Computational study of hypervelocity impacts on metallic thermal protection systems][research_poteet_1998]
- [Potsawat and others, 2019, Multipoint Shape Optimization of Supersonic Waverider][research_potsawat_palar_2019]
- [POTTSEPP and SHI, 1968, Optimal lift control of a hypersonic glider][research_pottsepp_shi_1968]
- [Poudel and Shoele, 2026, Multi-Fidelity Fluid-Thermal-Structural Assessment of Heat-Pipe-Cooled Hypersonic Leading Edges][research_poudel_shoele_2026]
- [Poulain and others, 2009, Nonlinear Control of a Airbreathing Hypersonic Vehicle][research_poulain_pietlahanie_2009]
- [Povolny and others, 2022, Numerical investigation of thermomechanical response of multiscale porous Ultra-High Temperature Ceramics][research_povolny_seidel_2022]
- [POWELL and CRUZ, 1991, Guidance and control analysis of the entry of a lifting body personnel launch vehicle][research_powell_cruz_1991]
- [POZEFSKY, 1989, Identifying sonic fatigue prone structures on a hypersonic Transatmospheric Vehicle TAV][research_pozefsky_1989]
- [Prakash and Singh, 2021, Flight Dynamics Analysis using High Altitude and Mach Number for Generic Air-Breathing Hypersonic Vehicle][research_prakash_singh_2021]
- [Prakash and Zhong, 2008, Numerical Simulation of Planetary Reentry Aeroheating Over Blunt Bodies with Non-equilibrium Reacting Flow][research_prakash_zhong_2008]
- [Prakash and Zhong, 2009, Numerical Simulation of Planetary Reentry Aeroheating Over Blunt Bodies with Non-Equilibrium Reacting Flow and Surface Reactions][research_prakash_zhong_2009]
- [Prasanna and others, 2005, Ascent Phase Trajectory Optimization for a Hypersonic Vehicle Using Nonlinear Programming][research_prasanna_ghose_2005]
- [Prasanna and others, 2005, Interpolation-Aware Trajectory Optimization for a Hypersonic Vehicle Using Nonlinear Programming][research_prasanna_ghose_2005_b]
- [Preller and Smart, 2012, Design of a Minimum Trim Hypersonic Airbreathing Accelerator Vehicle][research_preller_smart_2012]
- [Pressman and others, 1986, Trajectory Models of the Long-Range Air Pollutant Transmission][research_pressman_galperin_1986]
- [Pritchard, 1969, Base drag effects on maximum lift-to-drag ratio airfoils at moderate supersonic speeds][research_pritchard_1969]
- [Priyamvada and others, 2015, Analytical Modeling and Design for an Air-Breathing Hypersonic Cruise Vehicle Using an Integrated Approach][research_priyamvada_singh_2015]
- [PROBSTEIN, 1961, Shock Wave and Flow Field Development in Hypersonic Re-Entry][research_probstein_1961]
- [Pu and others, 2012, Design of entry trajectory tracking law for a hypersonic vehicle via inversion control][research_pu_tan_2012]
- [Pu and others, 2013, Robust trajectory linearization control of a flexible hypersonic vehicle in the presence of uncertainties][research_pu_tan_2013]
- [Pu and others, 2013, Robust Trajectory Linearization Control of Hypersonic Entry Flight Using Extended State Observer and Time-varying Bandwidth][research_pu_fan_2013]
- [Pu and others, 2014, Uncertainty analysis and robust trajectory linearization control of a flexible air-breathing hypersonic vehicle][research_pu_tan_2014]
- [Pu and others, 2016, Time-varying spectrum based active disturbance rejection control for hypersonic reentry vehicle][research_pu_zhang_2016]
- [Pudsey and others, 2012, Hypersonic Viscous Drag Reduction Via Multi-Porthole Injector Arrays][research_pudsey_boyce_2012]
- [Pulimidi and others, 2018, Mid-Tier Defense Against Hypersonic Glide Vehicles During Cruise][research_pulimidi_peace_2018]
- [Pulok and Chakravarty, 2020, Aerodynamic and Vibration Analysis of the Morphing Wings of a Hypersonic Vehicle][research_pulok_chakravarty_2020]
- [Purcell, 1980, New components boost range of microwave systems][research_purcell_1980]
- [Purpura and others, 2012, Comparison between Probe Stagnation Point Heat Flux Measurements and Correlation Formulas in SCIROCCO Plasma Wind Tunnel Tests][research_purpura_f_2012]
- [Purwar and Basu, 2017, Thermo-structural design of ZrB 2 SiC-based thermal protection system for hypersonic space vehicles][research_purwar_basu_2017]
- [Purwar, 2019, Thermo-structural Design of Hypersonic Vehicle Sharp Leading Edges for Thermo-erosive Stability Using Finite Element Modelling][research_purwar_2019]
- [Putnam and Braun, 2016, Review and Assessment of the Steep Lifting Entry Closed-Form Trajectory Solution][research_putnam_braun_2016]
- [Putnam and others, 2006, Improving Lunar Return Entry Footprints Using Enhanced Skip Trajectory Guidance][research_putnam_braun_2006]
- [Putnam and others, 2008, Improving Lunar Return Entry Range Capability Using Enhanced Skip Trajectory Guidance][research_putnam_bairstow_2008]
- [Putnam and others, 2009, An Entry Trajectory Design Methodology for Lunar Return][research_putnam_barton_2009]
- [Qi and Jianliang, 2017, NDI-Based L1 Adaptive Control Design for a Generic Hypersonic Vehicle Model][research_qi_jianliang_2017]
- [Qi and others, 2021, Lateral Reentry Guidance Based on Coverage Zone Profile][research_qi_zhang_2021]
- [Qi and others, 2023, Robust Ascent Trajectory Optimization for Hypersonic Vehicles Based on IGS-UMPSP][research_qi_wang_2023]
- [Qian and others, 2014, Fault-tolerant guidance and control design for reentry hypersonic flight vehicles based on control-allocation approach][research_qian_qi_2014]
- [Qian and Xinguo, 2011, Adaptive Inverse Control of a Generic Hypersonic Vehicle Based on Improved EMRAN][research_qian_xinguo_2011]
- [Qiang and others, 2000, Waverider design with parametric flow quality control by inverse method of characteristics][research_qiang_sobieczky_2000]
- [Qiang and others, 2017, Study on BTT Coordinated Turn Autopilot Design for Reentry Gliding Vehicle][research_qiang_yongtao_2017]
- [Qiang and others, 2019, The Research of Terminal Optimal Guidance Law of MANEUVERING vehicle with Multiple Constrains][research_qiang_jun_2019]
- [Qiao and Chen, 2011, Dynamic Inversion Guidance Law for a Hypersonic Vehicle][research_qiao_chen_2011]
- [Qiao and others, 2019, Adaptive control for hypersonic vehicle with input saturation and state constraints][research_qiao_meng_2019]
- [Qiao and others, 2024, Design and decoupling analysis of Thermal-Electric energy comprehensive utilization scheme based on "diamond" active cooling thermal protection system for hypersonic vehicle][research_qiao_liu_2024]
- [Qiao Yongjie and others, 2011, Detection probability of early warning radar against hypersonic cruise missile][research_qiaoyongjie_liujinrong_2011]
- [Qilun and others, 2015, Coordinated guidance strategy for heterogeneous missiles intercepting hypersonic weapon][research_qilun_xiwang_2015]
- [Qin and others, 2008, Thermal Management System Performance Analysis of Hypersonic Vehicle Based on Closed Brayton Cycle][research_qin_bao_2008]
- [Qin Changmao and others, 2010, Fractional PID controller design of hypersonic flight vehicle][research_qinchangmao_qinaiming_2010]
- [Qing Gao and others, 2014, Study on Lateral Aerodynamic Characteristics of Hypersonic Lifting-Configuration][research_qinggao_jianhuali_2014]
- [Qiu and others, 2016, Maximum range trajectory optimization for a boost-glide vehicle using adaptive mesh refinement pseudospectral methods][research_qiu_jia_2016]
- [Qiu and others, 2017, Numerical Investigation of Geometric Parameters Effects on Vortexes and Aerodynamic Heating Environment in Transverse Gaps on Hypersonic Vehicle][research_qiu_zhang_2017]
- [Qu and others, 2015, On aero glide downwards beam guidance control system][research_qu_pingyuan_2015]
- [Qu and others, 2015, Pre-oxidation temperature optimization of ultra-high temperature ceramic components Flexural strength testing and residual stress analysis][research_qu_he_2015]
- [Qu and others, 2016, An effective TLBO-based memetic algorithm for hypersonic reentry trajectory optimization][research_qu_li_2016]
- [Qu and others, 2017, Investigation into the influences of the low speed's accuracy on the hypersonic heating predictions for the Reusable Manned Space Vehicle][research_qu_sun_2017]
- [Qu and others, 2018, A study of upwind schemes on the laminar hypersonic heating predictions for the reusable space vehicle][research_qu_sun_2018]
- [Qu and others, 2019, Ultra-high temperature ceramics melting temperature prediction via machine learning][research_qu_liu_2019]
- [Qu and others, 2023, Adaptive Fixed-Time Attitude Tracking Control in Reentry Phase for Reusable Launch Vehicle][research_qu_zhang_2023]
- [Qu and others, 2023, Influence of Non-Uniform Bluntness on Aerodynamic Performance and Aerothermal Characteristics of Waverider][research_qu_wang_2023]
- [Qu and others, 2024, Aerodynamic design optimization of the hypersonic inward turning inlet in wide-speed range][research_qu_wang_2024]
- [Quan and others, 2026, Efficient Hypersonic Heating Rate Prediction for Three-Dimensional Vehicles Using Radial Basis Interpolation][research_quan_ma_2026]
- [Quinlan and others, 2021, Leveraging Multi-Fidelity Aerodynamic Databasing to Efficiently Represent a Hypersonic Design Space][research_quinlan_movva_2021]
- [R and others, 2022, Study of Drag Reduction on a Hypersonic Vehicle Using Aerospike][research_r_s_2022]
- [R C and others, 2023, Assessment of Modified 𝛾-model for Hypersonic Boundary Layer Transition Prediction Considering Leading Edge Bluntness][research_rc_k_2023]
- [Rademakers, 1993, Waverider-wavestaff comparison][research_rademakers_1993]
- [Rafique and LinShu, 2009, Effect of Aerodynamic Enhancements on Flight Performance of Air Launched Satellite Launch Vehicle][research_rafique_linshu_2009]
- [Rafla, 2019, Aerodynamic Heating Coupled with Structural Temperature Response Analysis for Hypersonic Flight Vehicles][research_rafla_2019]
- [Rafla, 2019, Correction Aerodynamic Heating Coupled with Structural Temperature Response Analysis for Hypersonic Flight Vehicles][research_rafla_2019_b]
- [Ragnoli and others, 2024, Hypersonic boost-glide systems Flight mechanics and plasma parameters evaluation through aero-thermo-chemical computational fluid dynamics][research_ragnoli_savino_2024]
- [Rahimi and others, 2013, Particle Swarm Optimization Applied to Spacecraft Reentry Trajectory][research_rahimi_devkumar_2013]
- [Rahimi and others, 2026, Functionally graded ultra-high temperature ceramics for hypersonic applications A numerical study of fracture under high-temperature extremes][research_rahimi_svolos_2026]
- [Rahman and others, 2013, Bézier approximation based inverse dynamic guidance for entry glide trajectory][research_rahman_hao_2013]
- [Raible and Jacob, 2003, Sensitivity-Based Optimization of Two-Stage-To-Orbit Space Planes with Lifting Body and Waverider Lower Stages][research_raible_jacob_2003]
- [Raja and others, 2021, Effectiveness of Hot Pack with Caudal Glide and Antero-Posterior Glide Mobilisation to Improve Shoulder Abduction Range in Adhesive Capsulitis][research_raja_shekadar_2021]
- [Rajasekhar and John, 2021, Computational Study of the Unsteady Wave Drag Reduction at Hypersonic Mach Number][research_rajasekhar_john_2021]
- [Rakdham and others, 2007, Boost Phase Ballistic Missile Defense Using Multiple Hypothesis Tracking][research_rakdham_tummala_2007]
- [Ramunno and others, 2021, Integrated Hypersonic Aero-Propulsion Model for Multidisciplinary Vehicle Analysis and Optimization][research_ramunno_boyd_2021]
- [Ran and others, 2023, Diving Guidance for Hypersonic Vehicles with Terminal Velocity Constraint][research_ran_huang_2023]
- [Rana and Chudoba, 2016, Design Evolution and AHP-based Historiography of Lifting Reentry Vehicle Space Programs][research_rana_chudoba_2016]
- [Rana and others, 2025, In Silico Evaluation of Sonic Ring Standoff and Trailing Edge Expansion on Hypersonic Waverider Performance][research_rana_khan_2025]
- [Rand, 1963, THE AERODYNAMIC HEATING OF A COMPOSITE FLAT PLATE][research_rand_1963]
- [Randolph, 2005, A Waverider Application of an Advanced Nuclear Power Source][research_randolph_2005]
- [Raney and others, 1995, Impact of aeroelastic-propulsive interactions on flight dynamics of a hypersonic vehicle][research_raney_mcminn_1995]
- [Rangaraj and others, 2013, Processing of Ultra-High Temperature Ceramics for Hostile Environments][research_rangaraj_divakar_2013]
- [Rao and others, 2026, Comparing Aerothermodynamic Models With Emission Spectroscopy Data From the Atmospheric Reentry of the W-2 Hypersonic Testbed Vehicle][research_rao_crespo_2026]
- [Rao, 1989, Analytical solution of optimal trajectory-shaping guidance][research_rao_1989]
- [Rao, 2011, Infrared Signature Modeling and Analysis of Aircraft Plume][research_rao_2011]
- [Rao, 2019, Sliding mode guidance with terminal angle and latax constraints][research_rao_2019]
- [RASMUSSEN and STEVENS, 1987, On waverider shapes applied to aero-space plane forebody configurations][research_rasmussen_stevens_1987]
- [Rasmussen, 1980, Waverider Configurations Derived from Inclined Circular and Elliptic Cones][research_rasmussen_1980]
- [RASMUSSEN, 1983, Viscous effects on the performance of cone-derived waveriders][research_rasmussen_1983]
- [RASMUSSEN, 1989, Integration of scramjets with waverider configurations][research_rasmussen_1989]
- [Rataczak and others, 2023, Reachability Analysis of a Hypersonic Glide Vehicle using Particle Swarm Optimization][research_rataczak_mcmahon_2023]
- [Rataczak and others, 2024, Investigation of Surface-Catalycity Effects on Hypersonic Glide Vehicle Trajectory Optimization][research_rataczak_chaudhry_2024]
- [Rathod and Sushnigdha, 2025, Space Shuttle Re-Entry Trajectory Tracking Using Estimator Based Control][research_rathod_sushnigdha_2025]
- [Ratnoo, 2017, Nonswitching Guidance Law for Trajectory Shaping Control][research_ratnoo_2017]
- [Rauh and others, 2026, The Panel Interface Measurement Experiment on the CMC Forebody of the ATHEAt Hypersonic Vehicle][research_rauh_reimer_2026]
- [RAULT, 1992, Aerodynamic characteristics of a hypersonic viscous optimized waverider at high altitudes][research_rault_1992_b]
- [Rault, 1992, Aerodynamic Performance of Delta Wings in The Hypersonic Rarefied Flow Regime. Comparison of 3D Dsmc Simulation With Wind Tunnel Data][research_rault_1992]
- [Rault, 1994, Aerodynamic characteristics of a hypersonic viscous optimized waverider at high altitudes][research_rault_1994]
- [Ravi and others, 2025, Computational Investigation of Aerothermodynamic Characteristics of Spherical and Flat Disc Spiked Blunt Body at Hypersonic Flow][research_ravi_oda_2025]
- [Ravichandran and others, 2023, Aerodynamic Effects and Heat Flux Augmentation of a Transpiration Cooled Hypersonic Sharp Leading Edge][research_ravichandran_doherty_2023]
- [Ravichandran and others, 2023, Boundary Layer Transition Studies on a Winged Body Reentry Vehicle through Heat Flux Measurements in Shock Tunnel][research_ravichandran_ahmed_2023]
- [Ravichandran and others, 2023, Correction Aerodynamic Effects and Heat Flux Augmentation of a Transpiration Cooled Hypersonic Sharp Leading Edge][research_ravichandran_doherty_2023_b]
- [Ray and De, 2022, Video Leading edge bluntness effects on double-wedge configuration in low enthalpy hypersonic flow][research_ray_de_2022]
- [Ray and De, 2025, Role of Gas Models on Aerothermodynamic Heating Over Double-Wedge in Hypersonic Stream][research_ray_de_2025]
- [Ray, 2021, Mars Entry, Descent, and Landing Spacecraft Design to Trajectory Simulation][research_ray_2021]
- [Raza and Mehmood, 2023, HYPERSONIC WEAPON SYSTEMS A NEW WAVE OF ARMS RACE IN THE INDIAN OCEAN REGION][research_raza_mehmood_2023]
- [Rea and Putnam, 2007, A Comparison of Two Orion Skip Entry Guidance Algorithms][research_rea_putnam_2007]
- [Reaser, 1997, Aerodynamic development of a lifting body launch vehicle][research_reaser_1997]
- [Reda and others, 2004, Aerothermodynamic Testing of Ablative Reentry Vehicle Nosetip Materials in Hypersonic Ballistic-Range Environments][research_reda_wilder_2004]
- [Reddy and Nagaraja, 2024, Drag and heat reduction on hypersonic re-entry vehicle using combination of spike and counter jet][research_reddy_nagaraja_2024]
- [Reddy and Sinha, 2009, Hypersonic Turbulent Flow Simulation of Fire II Reentry Vehicle Afterbody][research_reddy_sinha_2009]
- [Reddy and Sinha, 2012, Analysis of High-enthalpy Air-chemistry and its Effect on Stagnation Point Heat Flux][research_reddy_sinha_2012]
- [REGGIORI, 1971, Lift and drag of a wing-cone configuration in hypersonic flow][research_reggiori_1971]
- [REHDER, 1973, Correlation of hypersonic zero-lift drag data][research_rehder_1973]
- [Rehman and others, 2009, Minimax LQR Control Design for a Hypersonic Flight Vehicle][research_rehman_fidan_2009]
- [Reich and others, 1990, Thermal Protection Systems for Hypersonic Transport Vehicles][research_reich_hinger_1990]
- [Reilly, 1964, Stagnation-Point Heating in Ionized Monatomic Gases][research_reilly_1964]
- [Reimer and others, 2023, Design, Manufacturing and Assembly of the STORT Hypersonic Flight Experiment Thermal Protection System][research_reimer_dimartino_2023]
- [Reinartz and others, 2003, Aerodynamic Performance Analysis of a Hypersonic Inlet Isolator Using Computation and Experiment][research_reinartz_herrmann_2003]
- [Ren and others, 2014, Ultra-high temperature ceramic TaB2-TaC-SiC coating for oxidation protection of SiC-coated carbon/carbon composites][research_ren_li_2014]
- [Ren and others, 2017, Discrete reconfigurable back-stepping attitude control of reentry hypersonic flight vehicle][research_ren_fu_2017]
- [Ren and others, 2019, Hybrid guidance for Common Aero Vehicle equilibrium glide reentry with multi-constraints][research_ren_yang_2019]
- [Ren and others, 2022, Appointed-Time Prescribed Performance Control for Hypersonic Reentry Vehicles][research_ren_wang_2022]
- [Ren and others, 2023, Long-Term Trajectory Prediction of Hypersonic Glide Vehicle Based on Physics-Informed Transformer][research_ren_wu_2023]
- [Ren and others, 2025, Contextual DRL-empowered integrated guidance and evasion approach for hypersonic glide vehicles][research_ren_wang_2025]
- [Ren and others, 2025, Ultra-high temperature ceramics composites Synthesis, microstructure, and properties][research_ren_chen_2025]
- [Ren and Yang, 2017, Disturbance observer-based control of flexible hypersonic flight vehicle][research_ren_yang_2017]
- [Ren, 2009, Hypersonic Vehicle Multidisciplinary Design Optimization Based on Approximate Technology][research_ren_2009]
- [Reubush and Omar, 1990, Pressure and heat-transfer investigation of a hypersonic configuration][research_reubush_omar_1990]
- [Rhoads and others, 2023, Trajectory Modeling and Property Analysis of Atmospheric Entry Vehicles][research_rhoads_duplessis_2023]
- [RHUDY, 1970, Effect of uncooled leading edge on cooled-wall hypersonic flat-plateboundary-layer transition][research_rhudy_1970]
- [Riabov and Fedoseyev, 2015, The Analysis of Underexpanded Jet Flows for Hypersonic Aerodynamic Experiments in Vacuum Chambers][research_riabov_fedoseyev_2015]
- [Riabov, 1994, Aerodynamic applications of underexpanded hypersonic viscous jets][research_riabov_1994]
- [Riabov, 1995, Aerodynamic applications of underexpanded hypersonic viscous jets][research_riabov_1995]
- [Riabov, 2020, Applications of Underexpanded Jets in Hypersonic Rarefied-Gas Aerodynamic Research][research_riabov_2020]
- [Riabov, 2026, Modelling Heat Transfer at Low-Density Hypersonic Spacecraft Flight Regimes][research_riabov_2026]
- [Ribe, 1982, Calibration accuracy and data correction for Waverider buoys deployed during ARSLOE][research_ribe_1982]
- [Ribe, 1983, Accuracy characteristics of the electronics of waverider buoys used in the ARSLOE][research_ribe_1983]
- [Richards and others, 1971, Heat Transfer and Pressure Distributions on Re-Entry Nose Shapes in the VKI Longshot Hypersonic Tunnel][research_richards_culotta_1971]
- [Richmond, 2022, Optimizing Trajectories for Unpowered Hypersonic Waveriders during Atmospheric Reentry][research_richmond_2022]
- [Riedelbauch and Hirschel, 1993, Aerothermodynamic properties of hypersonic flow over radiation-adiabatic surfaces][research_riedelbauch_hirschel_1993]
- [RIGBY and RAE, 1989, Unsteady stagnation-point heat transfer during passage of a concentrated vortex][research_rigby_rae_1989]
- [Riggins and Camberos, 2020, Drag and Heat Transfer Effects on Hypersonic Vehicles in Close-Proximity Flight][research_riggins_camberos_2020]
- [Riggins and others, 2003, Drag Reduction and Heat Transfer Mitigation Techniques for Blunt Bodies in Hypersonic Flight][research_riggins_taylor_2003]
- [Rijbin and Lin, 1972, A numerical method for three-dimensional viscous flow Application to the hypersonic leading edge][research_rijbin_lin_1972]
- [Riley and DeJarnette, 1992, Engineering aerodynamic heating method for hypersonic flow][research_riley_dejarnette_1992]
- [Rishad and others, 2025, Innovative fabrication pathways for ultra-high temperature ceramic matrix composites Progress, properties enhancements and future perspectives][research_rishad_islam_2025]
- [Rizvi and others, 2012, Trajectory optimization study of a lifting body re-entry vehicle for medium to intermediate range applications][research_rizvi_linshu_2012]
- [Rizvi and others, 2015, Optimal trajectory and heat load analysis of different shape lifting reentry vehicles for medium range application][research_rizvi_he_2015]
- [Rizvi and others, 2017, Trajectory optimisation for a rocket-assisted hypersonic boost-glide vehicle][research_rizvi_linshu_2017]
- [Robinson and others, 1995, Meteoroid/orbital debris implications to a reusable launch vehicle thermal protection system][research_robinson_nolen_1995]
- [Rodi and Bennett, 2012, High Lift-to-Drag Ratio Waveriders for Missions in the Martian Atmosphere][research_rodi_bennett_2012]
- [Rodi, 2005, The Osculating Flowfield Method of Waverider Geometry Generation][research_rodi_2005]
- [Rodi, 2012, Non-Symmetric Waverider Star Bodies for Aerodynamic Moment Generation][research_rodi_2012]
- [Rodi, 2012, Preliminary Ramjet/Scramjet Integration with Vehicles Using Osculating Flowfield Waverider Forebodies][research_rodi_2012_c]
- [Rodi, 2012, Vortex Lift Waverider Configurations][research_rodi_2012_b]
- [Rodi, 2015, Integration of Optimized Leading Edge Geometries Onto Waverider Configurations][research_rodi_2015]
- [Rodi, 2018, An Examination of Crossflow Between Waverider Flowfield Planes][research_rodi_2018_e]
- [Rodi, 2018, Expanding the Osculating Flowfield Waverider Method Beyond Power Law Body Induced Flowfields][research_rodi_2018_b]
- [Rodi, 2018, On Using Upper Surface Shaping to Improve Waverider Performance][research_rodi_2018]
- [Rodi, 2018, Waverider Vehicle Optimization with Volumetric Constraints for Sonic Boom][research_rodi_2018_d]
- [Rodi, 2018, Waverider Vehicle Optimization with Volumetric Constraints for Wave Drag Minimization][research_rodi_2018_c]
- [Rodi, 2020, Combined Capsule/Waverider Configurations For Boost Glide Missions][research_rodi_2020]
- [Rodi, 2021, Effects of Viscosity on Capsule/Waverider Shape Optimization for Boost-Glide Missions][research_rodi_2021]
- [Rodi, 2021, Evaluation of the Capsule/Waverider Concept for Mars Entry, Descent, and Landing][research_rodi_2021_b]
- [Rodi, 2022, Effects of Finite Radius Leading Edges on the Performance of Capsule/Waveriders for Boost-Glide Missions][research_rodi_2022]
- [Rodi, 2023, Improved Waverider Vehicle Optimization with Volumetric and Lift Constraints for Shaped Sonic Booms][research_rodi_2023]
- [Rodríguez-Segade and others, 2022, Multi-bubble scheme and structural analysis of a hypersonic stratospheric flight vehicle][research_rodriguezsegade_hernandez_2022]
- [Rodríguez-Segade and others, 2024, Multi-level and multi-objective structural optimization for hypersonic vehicle design][research_rodriguezsegade_hernandez_2024]
- [ROENNEKE and CORNWELL, 1992, Trajectory control for a low-lift maneuverable reentry vehicle][research_roenneke_cornwell_1992]
- [Roenneke and Cornwell, 1993, Trajectory control for a low-lift re-entry vehicle][research_roenneke_cornwell_1993]
- [Roenneke and Well, 1996, Nonlinear drag-tracking control applied to optimal low-lift reentry guidance][research_roenneke_well_1996]
- [Roeser and others, 2010, Implementation of a Predictive Guidance Scheme for a Lunar Reentry Using Lift Force][research_roeser_graesslin_2010]
- [Rogers and others, 2022, Analysis of Ablation on Boundary Layer Stability of the Reentry F Flight Vehicle][research_rogers_schroeder_2022]
- [Rogers and Slegers, 2013, Robust Parafoil Terminal Guidance Using Massively Parallel Processing][research_rogers_slegers_2013]
- [Rolim and others, 2009, Experimental Results of a Mach 10 Conical-Flow Derived Waverider][research_rolim_minucci_2009]
- [Rolim and others, 2011, Experimental results of a Mach 10 conical-flow derived waverider to 14-X hypersonic airspace vehicle][research_rolim_toro_2011]
- [Rollins and others, 2013, Nonlinear Adaptive Dynamic Inversion Applied to a Generic Hypersonic Vehicle][research_rollins_valasek_2013]
- [ROLLSTIN, 1973, A rocket system for hypersonic, high Reynolds number aerothermodynamic research][research_rollstin_1973]
- [Rona and Zavalan, 2022, Contur A Computer Program for the Aerodynamic Design of Axisymmetric and Planar Supersonic and Hypersonic Nozzles][research_rona_zavalan_2022]
- [Rong and others, 2016, Heat-balance Thermal Protection with Heat Pipes for Hypersonic Vehicle][research_rong_wei_2016]
- [Rong and others, 2017, Self-evolving fuzzy model-based controller with online structure and parameter learning for hypersonic vehicle][research_rong_yang_2017]
- [Rong and Yang, 2024, Self-evolving Fuzzy Model-Based Controller for Hypersonic Vehicle][research_rong_yang_2024]
- [Rong Huang and others, 2015, Study of on-board trajectory generation of powered glide vehicle based on footprint analysis][research_ronghuang_yingziguan_2015]
- [Rong, 2017, Heat-balance Thermal Protection with High Thermal Conductivity Materials for Hypersonic Vehicle][research_rong_2017]
- [Ronquillo and Williams, 1984, Thermal Protection System for the Space Shuttle External Tank][research_ronquillo_williams_1984]
- [Rosa and others, 1991, CESA-1 project capabilities for high temperature material testing Application to the HERMES wing leading edge tests][research_rosa_valverde_1991]
- [Rose and Stankevics, 1963, STAGNATION POINT HEAT TRANSFER MEASUREMENTS IN PARTIALLY IONIZED AIR][research_rose_stankevics_1963]
- [ROSNER and CIBRIAN, 1974, Non-equilibrium stagnation region aerodynamic heating of hypersonic glide vehicles][research_rosner_cibrian_1974]
- [ROUNDS, 1987, Terminal guidance with low update rates][research_rounds_1987]
- [Rowden and others, 2022, WaveRider Immersive Visualization of Indoor Signal Propagation][research_rowden_aslan_2022]
- [Roy and Priyadarshi, 2020, Multi-objective Aerodynamic Optimization of a Hypersonic Scramjet Inlet][research_roy_priyadarshi_2020]
- [Rubin and Shepps, 1966, A general-purpose analog translational trajectory program for orbiting and reentry vehicles][research_rubin_shepps_1966]
- [RUBIN, 1968, Hypersonic viscous flow over slender bodies with sharp leading edges][research_rubin_1968]
- [Rubio and others, 2018, Ultra-high temperature ceramic composite][research_rubio_ramanujam_2018]
- [RUBLE, 1964, Variable geometry hypersonic entry vehicle][research_ruble_1964]
- [Rucker and Grandle, 1973, Thermoacoustic Fatigue Testing Facility for Space Shuttle Thermal Protection System][research_rucker_grandle_1973]
- [RUGER, 1964, Skip-impact criteria of a re-entry trajectory with negative lift][research_ruger_1964]
- [Rugescu, 2013, Reentry Design Solution for a Hypersonic Small Capsule][research_rugescu_2013]
- [Ruggles and Tichenor, 2025, Laser Ablation for Hypersonic Aerodynamic Control][research_ruggles_tichenor_2025]
- [Ruimin and Jianguo, 2018, Statistical performance analysis of hypersonic vehicle attitude control system][research_ruimin_jianguo_2018]
- [Ruisong Huang and Wei Li, 2015, Optimal sliding mode guidance law with height deviation and terminal impact angle constraints][research_ruisonghuang_weili_2015]
- [Running and others, 2019, Hypersonic boundary-layer separation detection with pressure-sensitive paint for a cone at high angle of attack][research_running_sakaue_2019]
- [RUPERTI and others, 2004, Engineering Analysis of Ablative Thermal Protection for Atmospheric Reentry Improved Lumped Formulations and Symbolic Numerical Computation][research_ruperti_cotta_2004]
- [Rusnak, 2000, Multiple Model-Based Terminal Guidance Law][research_rusnak_2000]
- [Rusnak, 2015, Bounds on the Miss of Multiple-Model-Based Terminal Guidance Laws][research_rusnak_2015]
- [Russo and others, 2026, Integrated CFD Modelling and Thermal Management Strategies for the Scramjet Hypersonic Demonstrator Vehicle][research_russo_roncioni_2026]
- [Ryan and Lewis, 2012, Trajectory Optimization Studies of Long Range Morphing Projectiles][research_ryan_lewis_2012]
- [Ryan and others, 2013, Comparison of Robust Optimization Methods Applied to Hypersonic Vehicle Design][research_ryan_lewis_2013]
- [Ryoo and others, 2005, Optimal Guidance Laws with Terminal Impact Angle Constraint][research_ryoo_cho_2005]
- [S and Padhi, 2017, Explicit Constrained Terminal Acceleration Optimal Guidance for Three Dimensional Lunar Landing][research_s_padhi_2017]
- [Sabapathy, 2026, Effect of Static Fin on the Stability and Aerothermodynamic Characteristics of the Re-entry Vehicle][research_sabapathy_2026]
- [Sacchetti and Anfossi, 1993, Forecasting of precipitation occurrence in long-range trajectory climatology][research_sacchetti_anfossi_1993]
- [Sachan and Padhi, 2018, State-constrained Robust Adaptive Cruise Control Design for Air-breathing Hypersonic Vehicles][research_sachan_padhi_2018]
- [Sachan and Padhi, 2020, Nonlinear robust neuro-adaptive flight control for hypersonic vehicles with state constraints][research_sachan_padhi_2020]
- [Sacher and Zellner, 1995, Flight testing objectives for small hypersonic flight test vehicles featuring a ramjet engine][research_sacher_zellner_1995]
- [Sacher, 1993, Hypersonic Technology Experimental Vehicles The Need for Flight Testing at Hypersonic Speed][research_sacher_1993]
- [Sachs and Dinkelmann, 1996, Heat input reduction in hypersonic flight by optimal trajectory control][research_sachs_dinkelmann_1996_b]
- [Sachs and Dinkelmann, 1996, Reduction of coolant fuel losses in hypersonic flight by optimal trajectory control][research_sachs_dinkelmann_1996]
- [Sachs and Moravszki, 2002, Simulation Experiments for Hypersonic Trajectory Control Using a Predictive Flight Path Display][research_sachs_moravszki_2002]
- [Sachs and others, 1996, Robust control of a hypersonic experimental vehicle with ramjet engines][research_sachs_heller_1996]
- [Sachs and others, 2009, Trajectory Optimization for Maximizing the Range of Powered Sailplanes with Retractable Propeller][research_sachs_lenz_2009]
- [SACHS and SCHODER, 1991, Optimal separation of lifting vehicles in hypersonic flight][research_sachs_schoder_1991]
- [SACHS and SCHODER, 1992, Robust control of the separation of hypersonic lifting vehicles][research_sachs_schoder_1992]
- [Sadagopan and others, 2020, Impact of High-Temperature Effects on the Aerothermoelastic Behavior of Composite Skin Panels in Hypersonic Flow][research_sadagopan_huang_2020]
- [Sager, 1995, Aerodynamic investigation of a SSTO vehicle lifting body design][research_sager_1995]
- [Sagliano and others, 2016, Onboard Trajectory Generation for Entry Vehicles via Adaptive Multivariate Pseudospectral Interpolation][research_sagliano_mooij_2016]
- [Sagliano and others, 2017, Adaptive Disturbance-Based High-Order Sliding-Mode Control for Hypersonic-Entry Vehicles][research_sagliano_mooij_2017]
- [Sagliano and others, 2024, Six-Degrees-of-Freedom Aero-Propulsive Entry Trajectory Optimization][research_sagliano_lu_2024]
- [Saha, 2023, New Frontiers in Characterising ZrB2-MoSi2 Ultra-High Temperature Ceramics][research_saha_2023]
- [Sahai and others, 2014, Effect of Fineness Ratio on Minimum-Drag Shapes in Hypersonic Flows][research_sahai_john_2014]
- [Saheby and others, 2017, Design of hypersonic forebody by the combination of bump and waverider surfaces][research_saheby_huang_2017]
- [Sahu and others, 2024, Hypersonic Flow Predictions on a Generic Canonical Flight Vehicle][research_sahu_vasile_2024]
- [Sai Naga Bharghava and others, 2024, Implementation of concavity over heat shield of a reentry vehicle in reducing aerodynamic heating][research_sainagabharghava_krishnatmali_2024]
- [Saito and others, 2025, Guidance strategies for controlled Earth reentry of small spacecraft in low Earth orbit][research_saito_kuwahara_2025]
- [Sakai and others, 2017, In Situ Ablation Measurement for an Ablative Heat Shield Using an Embedded Sensor][research_sakai_nakazawa_2017]
- [Sakurai and others, 1997, Development of the hypersonic flight experimental vehicle][research_sakurai_kobayasi_1997]
- [SALAH, 1969, Hypersonic sphere drag from radar measurements][research_salah_1969]
- [Saldivar Massimi and others, 2015, Numerical analysis of hypersonic flows around blunt-nosed models and a space vehicle][research_saldivarmassimi_shen_2015]
- [Salleh and others, 2009, FORCED CONVECTION BOUNDARY LAYER FLOW AT A FORWARD STAGNATION POINT WITH NEWTONIAN HEATING][research_salleh_nazar_2009]
- [Saltzman and others, 2007, In-Flight Subsonic Lift and Drag Characteristics Unique to Blunt-Based Lifting Reentry Vehicles][research_saltzman_wang_2007]
- [Samotokhin, 2021, Review of space vehicle control and guidance methods at atmosphere reentry][research_samotokhin_2021]
- [Sana and Hu, 2020, Reentry guidance by accelerated fractional-order particle swarm optimization method][research_sana_hu_2020]
- [Sandeep, 2023, Design and Performance of Hypersonic Intake for Scramjet Engine][research_sandeep_2023]
- [Sani and others, 2012, Ultra-High Temperature Ceramics for solar receivers spectral and high-temperature emittance characterization][research_sani_mercatelli_2012]
- [Sani and others, 2013, Porous and dense hafnium and zirconium ultra-high temperature ceramics for solar receivers][research_sani_mercatelli_2013]
- [Sankowski, 2011, Continuous-discrete estimation for tracking ballistic missiles in air-surveillance radar][research_sankowski_2011]
- [Sano, 1981, Unsteady Stagnation Point Heat Transfer with Blowing or Suction][research_sano_1981]
- [Santos and Lewis, 2002, Power law shaped leading edges in rarefied hypersonic flow][research_santos_lewis_2002]
- [Santos and Lewis, 2003, Aerodynamic Heating Performance of Power Law Leading Edges in Rarefied Hypersonic Flow][research_santos_lewis_2003]
- [Santos and Lewis, 2005, Aerothermodynamic Performance Analysis of Hypersonic Flow on Power Law Leading Edges][research_santos_lewis_2005]
- [Santos and others, 2008, Thermal Modeling of In-Depth Thermocouple Response in Ablative Heat Shield Materials][research_santos_beck_2008]
- [Santos and others, 2020, Multi-Fidelity Turbulent Heating Prediction of Hypersonic Inflatable Aerodynamic Decelerators with Surface Scalloping][research_santos_hosder_2020]
- [Santos and others, 2021, Multifidelity Turbulent Heating Prediction of Hypersonic Inflatable Aerodynamic Decelerators with Surface Scalloping][research_santos_hosder_2021]
- [Santos, 1993, An efficient numerical method for the aerothermodynamic design of hypersonic vehicles][research_santos_1993]
- [Santos, 2004, Aerothermodynamic Characteristics of Flat-Nose Power-Law Bodies in Low-Density Hypersonic Flow][research_santos_2004]
- [Santos, 2005, Power law shapes for leading-edge blunting with minimal standoff distance in low-density hypersonic flow][research_santos_2005]
- [Santos, 2006, Influence of Gas-Surface Interaction on Hypersonic Aerothermodynamic Performance of Flat-Nose Power-Law Bodies][research_santos_2006]
- [Santos, 2007, Leading Edge Thickness Impact on Drag and Lift in Hypersonic Wedge Flow][research_santos_2007_b]
- [Santos, 2007, Simulation of blunt leading edge aerothermodynamics in rarefied hypersonic flow][research_santos_2007]
- [Santos, 2008, Flowfield Characteristics of Sharp/Blunt Leading Edges for Hypersonic Waverider Configurations][research_santos_2008]
- [Santos, 2009, Bluntness Impact on Lift-to-Drag Ratio of Hypersonic Wedge Flow][research_santos_2009]
- [Santos, 2011, Bluntness Effects on Lift-to-Drag Ratio of Leading Edges for Hypersonic Waverider Configurations][research_santos_2011]
- [Santos, 2012, Aerothermodynamic Analysis of a Reentry Brazilian Satellite][research_santos_2012]
- [Santos, 2012, Bluntness Effects on Lift-to-Drag Ratio of Leading Edges for Hypersonic Waverider Configurations][research_santos_2012_b]
- [Saqib and Linshu, 2007, Towards Developing a WaveRider Based Low Hypersonic Research Vehicle][research_saqib_linshu_2007]
- [Saranathan and Grant, 2016, Incorporation of Ablative Shape Change into Conceptual Hypersonic Mission Design][research_saranathan_grant_2016_b]
- [Saranathan and Grant, 2016, Incorporation of Effects of Control Surfaces into Hypersonic Trajectory Optimization Framework][research_saranathan_grant_2016]
- [Saranathan and others, 2015, Rapid Modeling of Ablative Shape Change for Conceptual Hypersonic Mission Design][research_saranathan_geldermans_2015]
- [Saranya and others, 2018, Mars Entry Phase Trajectory Tracking Controller using Dynamic Inversion][research_saranya_chinnaponnu_2018]
- [Saravanan and others, 2009, Aerodynamic Characteristics of Hypersonic Vehicle with Variable Sweep back Wing Configuration][research_saravanan_pillai_2009]
- [Saravanan and others, 2009, Measurement of aerodynamic forces for missile shaped body in hypersonic shock tunnel using 6-component accelerometer based balance system][research_saravanan_jagadeesh_2009]
- [Sardar, 2024, Way-points Based Trajectory Simulation Using Web Technology for Range Environment][research_sardar_2024]
- [Sargunaraj and others, 2022, Use of Supercritical CO 2 Impingement Cooling for a Hypersonic Leading Edge][research_sargunaraj_otto_2022]
- [Sargunaraj and others, 2023, Aerodynamics and Heat Transfer Investigation of Supercritical Carbon Dioxide Multi Jet Impingement Cooling for a Leading Edge at Hypersonic Speeds][research_sargunaraj_otto_2023]
- [Sarkar and others, 2011, Range Extension Of An Air-to-air Engagement By Offline Trajectory Optimization][research_sarkar_kar_2011]
- [Sarkar and others, 2021, Re-entry trajectory tracking of reusable launch vehicle using artificial delay based robust guidance law][research_sarkar_mukherjee_2021]
- [SARMA and SWAMY, 1989, MAMS An approach to optimal terminal homing guidance for aerial engagements][research_sarma_swamy_1989]
- [Sarma, 1996, Relevance of Aerothermochemistry for Hypersonic Technology][research_sarma_1996]
- [Sarosh and others, 2013, A TIPSO algorithm assessment for aerothermodynamic optimization of hypersonic compression systems][research_sarosh_di_2013]
- [Sarosh, 2021, An Inverse Aerothermal Design IAD Methodology for Scramjet Integrated Waverider Configuration][research_sarosh_2021]
- [Sarwar and others, 2024, A Study of Different Techniques for Reducing Drag and Heating Problems on a Blunt Body at Supersonic and Hypersonic Speed][research_sarwar_rao_2024]
- [Sarzi-Amade and others, 2016, Sprite, a Very Low-Cost Launch Vehicle for Small Satellites][research_sarziamade_bauer_2016]
- [SASOH and FUJIWARA, 1990, Equilibrium and nonequilibrium radiation heat transfer over a reentry blunt body][research_sasoh_fujiwara_1990]
- [Satheesh and Jagadeesh, 2009, Effect of electric arc discharge on hypersonic blunt body drag][research_satheesh_jagadeesh_2009]
- [Satheesh and others, 2005, Hypersonic wave drag reduction in re-entry capsules using concentrated energy deposition][research_satheesh_jagadeesh_2005]
- [Satheesh Chandran and others, 2021, Low Density Syntactic Foam Composites as Ablative TPS Material for High Heat Flux Conditions for Reentry Missions][research_satheeshchandran_sunitha_2021]
- [Savage and others, 2000, Fuzzy classification algorithm as applied to signal discrimination for navy theater-wide missile defense][research_savage_chen_2000]
- [SAVAGE, 1965, TERMINAL PREDICTION GUIDANCE][research_savage_1965]
- [Savelsberg and others, 2026, Chapter 4. The Threat of Hypersonic Glide Vehicles in A2/AD Scenarios][research_savelsberg_kampert_2026]
- [Savino and others, 2018, Testing ultra-high-temperature ceramics for thermal protection and rocket applications][research_savino_mungiguerra_2018]
- [Savino, 2010, Editorial Ultra High Temperature Ceramics for Aerospace Applications][research_savino_2010]
- [Savu and Trifu, 1993, The global aerodynamic optimization of a hypersonic transport aircraft][research_savu_trifu_1993]
- [Sawada and Dendou, 2001, Validation of hypersonic chemical equilibrium flow calculations using ballistic-range data][research_sawada_dendou_2001]
- [Scala and Nolan, 1960, AEROTHERMODYNAMIC FEASIBILITY OF GRAPHITE FOR HYPERSONIC GLIDE VEHICLES][research_scala_nolan_1960]
- [Scala, 1958, Estimating Aerodynamic Characteristic Times in Hypersonic Flow][research_scala_1958]
- [SCALA, 1962, THE HYPERSONIC ENVIRONMENT HEAT TRANSFER IN MULTICOMPONENT GASES][research_scala_1962]
- [Scatteia and others, 2005, PRORA-USV SHS Ultra High Temperature Ceramic Materials for Sharp Hot Structures][research_scatteia_riccio_2005]
- [Scatteia and others, 2006, Surface Properties and Oxidation Behaviour of Ultra High Temperature Ceramics for Sharp Leading Edges][research_scatteia_pichelin_2006]
- [Schafer, 2002, Small Satellites in a Large Launch Vehicle Marketplace NASA's Strategic Effort to Provide Space Transportation][research_schafer_2002]
- [Scheber and Guthe, 2013, Conventional Prompt Global Strike A Fresh Perspective][research_scheber_guthe_2013]
- [Schettino and Borrelli, 1998, Applicability of Scirocco Plasma Wind Tunnel for testing the thermal protection system of FESTIP concept vehicles][research_schettino_borrelli_1998]
- [Schiavazzi and Juliano, 2020, Bayesian Network Inference of Thermal Protection System Failure in Hypersonic Vehicles][research_schiavazzi_juliano_2020]
- [Schierman and Hull, 2005, In-Flight Entry Trajectory Optimization for Reusable Launch Vehicles][research_schierman_hull_2005]
- [Schierman and others, 2001, Adaptive Guidance Systems for Hypersonic Reusable Launch Vehicles][research_schierman_ward_2001]
- [Schmidt and Hermann, 1998, Use of Energy-State Analysis on a Generic Air-Breathing Hypersonic Vehicle][research_schmidt_hermann_1998]
- [Schmidt and others, 1993, Using trajectory optimization to determine design sensitivities for single-stage-to-orbit hypersonic vehicles][research_schmidt_lovell_1993]
- [Schmidt and others, 2022, Kentucky Re-Entry Universal Payload System KRUPS Design and Testing for Hypersonic Re-Entry Flight][research_schmidt_nichols_2022]
- [Schmidt and Velapoldi, 1996, Optimum mission performance and guidance for hypersonic single stage to orbit][research_schmidt_velapoldi_1996]
- [Schmidt, 1993, PROBLEMS IN CONTROL SYSTEM DESIGN FOR HYPERSONIC VEHICLES][research_schmidt_1993]
- [Schmidt-Wimmer and others, 2012, Evaluation of Ultra High Temperature Ceramics and Coating-Systems for their Application in Orbital and Air-Breathing Propulsion][research_schmidtwimmer_beyer_2012]
- [Schmisseur and Erbland, 2012, Introduction Assessment of aerothermodynamic flight prediction tools through ground and flight experimentation][research_schmisseur_erbland_2012]
- [Schoeler, 1987, Kinetic Energy Finned Projectile Aerodynamic Heating Measurements][research_schoeler_1987]
- [Schoenenberger and others, 2005, Ballistic Range Testing of the Mars Exploration Rover Entry Capsule][research_schoenenberger_hathaway_2005]
- [Scholtz and Weisman, 1985, A Multi-Layered, Long-Range Transport, Lagrangian Trajectory Model Comparison with Fully Mixed Single Layer Models][research_scholtz_weisman_1985]
- [Schoneman and others, 2000, Orbital Suborbital Program OSP 'Minotaur' space launch vehicle - Low cost space lift for small satellites using surplus Minuteman motors][research_schoneman_buckley_2000]
- [Schoneman and others, 2005, OSP-2 Minotaur Family of Space Launch Vehicles for Near Term, Low Risk Responsive Spacelift][research_schoneman_amorosi_2005]
- [Schoneman and others, 2007, Minotaur-Family Launch Vehicles Responsive Launch Demonstration for the TacSat-2 Mission][research_schoneman_amorosi_2007]
- [Schouler and others, 2021, IXV post-flight reconstruction and analysis of the aerothermodynamic measurements along the rarefied portion of the reentry trajectory][research_schouler_prevereaud_2021]
- [Schouler and others, 2023, Machine Learning based reduced models for the aerothermodynamic and aerodynamic wall quantities in hypersonic rarefied conditions][research_schouler_prevereaud_2023]
- [Schumacher and others, 2003, COMMERCIAL OPERATIONS OF THE ROCKOT LAUNCH VEHICLE FOR SMALL AND MEDIUM PAYLOADS INTO LOW EARTH ORBIT][research_schumacher_kinnersley_2003]
- [Schwanekamp, 2014, System Studies on Active Thermal Protection of a Hypersonic Suborbital Passenger Transport Vehicle][research_schwanekamp_2014]
- [Schwartz and others, 2025, Unscented Hypersonic Trajectory Optimization With a Heating-Rate Chance Constraint][research_schwartz_karpenko_2025]
- [Scigliano and others, 2020, Preliminary Finite Element Thermal Analysis of STRATOFLY Hypersonic Vehicle][research_scigliano_desimone_2020]
- [Sciti and others, 2014, Are short Hi-Nicalon SiC fibers a secondary or a toughening phase for ultra-high temperature ceramics?][research_sciti_guicciardi_2014]
- [Scott, 1989, Effects of Thermochemistry, Nonequilibrium, and Surface Catalysis on the Design of Hypersonic Vehicles][research_scott_1989]
- [Seager and Agarwal, 2015, Shape Optimization of Axisymmetric Bodies in Hypersonic Flow for Reducing Drag and Heat Transfer][research_seager_agarwal_2015]
- [Sebastian and Schreyer, 2024, Design considerations for efficient spanwise-inclined air-jet vortex generators for separation control in supersonic and hypersonic flows][research_sebastian_schreyer_2024]
- [Sedláček, 1995, A Model of Long-Range Internal Stresses and Glide Dislocation Shapes in Dislocation Wall Structures][research_sedlacek_1995]
- [Sedláček, 1995, Glide dislocation shapes and long-range internal stresses in dislocation wall structures][research_sedlacek_1995_b]
- [Selim and Ozkol, 2023, Safe and Adaptive Trajectory Reshaping of Constrained Re-entry Flight Recovery Ensemble Control][research_selim_ozkol_2023_b]
- [Selim and Özkol, 2023, Robust Trajectory Optimization of Constrained Re-entry Flight][research_selim_ozkol_2023]
- [Sen and others, 2018, A Scramjet Compression System for Hypersonic Air Transportation Vehicle Combined Cycle Engines][research_sen_pesyridis_2018]
- [Seo and others, 2022, Staging and Mission Design of a Two-Staged Small Launch Vehicle Based on the Liquid Rocket Engine Technology][research_seo_lee_2022]
- [Serrani, 2010, Nonlinear Flight Control Systems Design for Hypersonic Vehicles Results and Open Problems][research_serrani_2010]
- [Sforza, 2020, Bluntness Effects on the Lift to Drag Ratio of Slender Bodies in Hypersonic Flight][research_sforza_2020]
- [Sforza, 2020, Correction Bluntness Effects on the Lift to Drag Ratio of Slender Bodies in Hypersonic Flight][research_sforza_2020_b]
- [Sforza, 2026, Normal Shock Wave Approximations for Flight at Hypersonic Mach Numbers][research_sforza_2026]
- [Shachar and others, 2025, Optimal Trajectory for a Hypersonic Cruise Missile with a Nonconvex Control Set][research_shachar_benasher_2025]
- [Shaferman and Shima, 2008, Linear Quadratic Guidance Laws for Imposing a Terminal Intercept Angle][research_shaferman_shima_2008]
- [Shahzad and Weiduo, 2014, Boundary conditions for skip entry trajectory][research_shahzad_weiduo_2014]
- [Shahzad and Weiduo, 2019, Design and Simulation of Range Enhancement of Reentry Vehicle][research_shahzad_weiduo_2019]
- [Shaju and others, 2023, Design and Additive Manufacturing of a Mechanical Chassis for Small Satellite Launch Vehicle Inertial Navigation Package][research_shaju_syamdas_2023]
- [Shakiba and Serrani, 2011, Control Oriented Modeling of 6-DOF Hypersonic Vehicle Dynamics][research_shakiba_serrani_2011]
- [Shams and others, 2020, Capability Analysis of Global Hypersonic Wind Tunnel Facilities for Aerothermodynamic Investigations][research_shams_shah_2020]
- [Shan and others, 2018, Hypersonic Gliding Reentry Vehicle Tracking with Process Noise Variance Adaptive Approach][research_shan_liang_2018]
- [Shang and others, 2018, Dynamic Surface Fuzzy Adaptive Terminal Guidance Law with Impact Angle Constraints and Autopilot Lag][research_shang_weige_2018]
- [Shang and Surzhikov, 2010, Simulating Nonequlibrium Flow for Ablative Earth Reentry][research_shang_surzhikov_2010]
- [Shang and Surzhikov, 2011, Nonequilibrium Radiation Heat Transfer in Hypersonic Flow][research_shang_surzhikov_2011]
- [Shang, 2002, Plasma Injection for Hypersonic Blunt-Body Drag Reduction][research_shang_2002]
- [Shang, 2008, Electrostatic-Aerodynamic Compression in Hypersonic Cylindrical Inlet][research_shang_2008]
- [Shao and others, 2014, The air-breathing hypersonic vehicle adaptive backstepping control design based on the dynamic surface][research_shao_lian_2014]
- [Shao and others, 2015, Enhanced trajectory linearization control based advanced guidance and control for hypersonic reentry vehicle with multiple disturbances][research_shao_wang_2015_b]
- [Shao and others, 2016, Analysis of weakly ionized ablation plasma flows for a hypersonic vehicle][research_shao_nie_2016]
- [Shao and others, 2018, A Sliding Mode Variable-structure Guidance Law with Terminal Impact Angle Constraint][research_shao_xu_2018]
- [Shao and others, 2025, A Hierarchical Adaptive Moment Matching Multiple Model Tracking Method for Hypersonic Glide Target Under Measurement Uncertainty][research_shao_zheng_2025]
- [Shao and others, 2025, Hypersonic Flight Vehicle Rigid/Flexible State Estimation Using INS and FADS][research_shao_zhao_2025]
- [Shao and Wang, 2015, Active disturbance rejection based trajectory linearization control for hypersonic reentry vehicle with bounded uncertainties][research_shao_wang_2015]
- [Shao and Wang, 2016, Back-stepping robust trajectory linearization control for hypersonic reentry vehicle via novel tracking differentiator][research_shao_wang_2016]
- [Shapiro and Akin, 2005, Survivability of Emergency Escape from a Simulated Shuttle Entry Trajectory][research_shapiro_akin_2005]
- [Sharifzadeh and others, 2015, Cryogenic hydrogen fuel tanks for large hypersonic cruise vehicles][research_sharifzadeh_verstraete_2015]
- [Sharma and others, 2020, Toward an Uncertain Modeling of Hypersonic Aerodynamic Forces][research_sharma_wang_2020]
- [Sharma and others, 2023, Pseudo-Spectral MPSP-Based Unified Midcourse and Terminal Guidance for Reentry Targets][research_sharma_kumar_2023]
- [SHARPE, 1969, Experimental cylinder drag data for hypersonic, rarefied flow][research_sharpe_1969]
- [Shaw and Porter, 2006, Process for Optimizing the Aerodynamic Design of Hypersonic Vehicles][research_shaw_porter_2006]
- [Sheetz, 1969, Ballistics Range Boundary-Layer Transition Measurements on Cones at Hypersonic Speeds][research_sheetz_1969]
- [SHEFFER and DULIKRAVICH, 1993, Constrained optimization of three-dimensional hypersonic vehicle configurations][research_sheffer_dulikravich_1993]
- [Shekhawat and Sinha, 2025, Longitudinal Dynamics of a Nonlinear Model of Air-Breathing Hypersonic Vehicle][research_shekhawat_sinha_2025]
- [Shekhawat and Sinha, 2026, Bifurcation-Based Analysis of the Longitudinal Flight Dynamics of an Air-Breathing Hypersonic Vehicle][research_shekhawat_sinha_2026]
- [Shen and Li, 2009, Design of Range Correction Fuze Trajectory Calculation and Control Device][research_shen_li_2009]
- [Shen and Li, 2015, Optimal feedback gains determination method for nominal reentry guidance][research_shen_li_2015]
- [Shen and Lu, 2003, On-Board Entry Trajectory Planning Expanded to Sub-Orbital Flight][research_shen_lu_2003]
- [Shen and Lu, 2004, Dynamic Lateral Entry Guidance Logic][research_shen_lu_2004]
- [Shen and others, 2014, Robust Gain-Scheduling Controller for Airbreathing Hypersonic Flight Vehicle][research_shen_yu_2014]
- [Shen and others, 2019, Parametric modeling and aerodynamic optimization of EXPERT configuration at hypersonic speeds][research_shen_huang_2019]
- [Shen and others, 2020, Constraint-based parameterization using FFD and multi-objective design optimization of a hypersonic vehicle][research_shen_huang_2020]
- [Shen and others, 2022, Penetration trajectory optimization for the hypersonic gliding vehicle encountering two interceptors][research_shen_yu_2022]
- [Shen and others, 2023, Adaptive super-twisting sliding mode altitude trajectory tracking control for reentry vehicle][research_shen_xia_2023]
- [Shengzheng and others, 2023, Study on Gliding Extended Range Ballistics of Long-Range Guided Mortar Projectiles][research_shengzheng_yuhang_2023]
- [Shenming and others, 2019, Improved Optimal Terminal Guidance Law Based on Virtual Expected Terminal Impact Angle][research_shenming_tao_2019]
- [SHEPORAITIS and others, 1976, Practical optimal steering for missile terminal guidance][research_sheporaitis_balbirnie_1976]
- [Sheta and others, 2015, Development and Performance Assessment of Hypersonic Inflatable Aerodynamic Decelerator][research_sheta_venugopalan_2015]
- [Sheu and others, 1998, Optimal glide for maximum range][research_sheu_chen_1998]
- [Shevelev, 2018, Numerical Modeling of Hypersonic Aerodynamics and Heat Transfer Problems of the Martian Descent Modules][research_shevelev_2018]
- [Shevyrin and others, 2016, Investigation of an ionized shock layer in a rarefied gas flow around a reentry vehicle][research_shevyrin_wu_2016]
- [Shi and Deng, 2024, Reentry Trajectory Planning Based on Proximal Policy Optimization][research_shi_deng_2024]
- [Shi and others, 1997, Computational Fluid Dynamics Simulation of Turbulent Waverider Flowfield with Sideslip][research_shi_miles_1997]
- [Shi and others, 2010, Study on the Probability of Successful Handoff of Missile Trajectory from Midcourse Guidance to Terminal Guidance][research_shi_wang_2010]
- [Shi and others, 2012, Simulation of Skip-Glide Trajectory for Hypersonic Vehicle in Near Space][research_shi_zhou_2012]
- [Shi and others, 2013, A pseudospectral approach to ascent trajectory optimization for hypersonic air-breathing vehicles][research_shi_jing_2013_b]
- [Shi and others, 2013, Ascent trajectory optimisation for hypersonic vehicles via Gauss pseudospectral method][research_shi_jing_2013]
- [Shi and others, 2014, Adaptive robust control for maneuvering reentry vehicle basing on backstepping][research_shi_zhang_2014]
- [Shi and others, 2015, Design and optimization of an integrated thermal protection system for space vehicles][research_shi_dai_2015]
- [Shi and others, 2017, Sliding mode disturbance observer-based adaptive tracking control for hypersonic reentry vehicle][research_shi_he_2017]
- [Shi and others, 2019, Uniform Aero-Heating Flux Design for a Hypersonic Blunt Body][research_shi_shi_2019]
- [Shi and others, 2020, Algorithm of Reentry Guidance for Hypersonic Vehicle Based on Lateral Maneuverability Prediction][research_shi_zhang_2020]
- [Shi and others, 2020, Quantized learning control for flexible air-breathing hypersonic vehicle with limited actuator bandwidth and prescribed performance][research_shi_shao_2020]
- [Shi and others, 2021, Thermal performance and ablation characteristics of C/C-SiC for thermal protection of hypersonic vehicle][research_shi_zha_2021]
- [Shi and others, 2023, A Full-trajectory Design Method for a Waverider Hypersonic Vehicle with Boost-glide-attack Process][research_shi_niu_2023]
- [Shi and others, 2025, Trajectory Optimization for Hypersonic Gliding Vehicle Using Lossless Convexification][research_shi_li_2025]
- [Shichao and others, 2021, Integrated Guidance and Control Design for Homing Missile with Terminal Angular Constraint][research_shichao_aijun_2021]
- [SHIH and others, 1988, Thermal protection system optimization for a hypersonic aerospace vehicle][research_shih_zwan_1988]
- [Shimada and Ohwada, 2020, ILES of an array of three subsonic counter-flow jets issuing from a wing leading edge exposed to hypersonic aerodynamic heating][research_shimada_ohwada_2020]
- [Shinar, 2004, On the Optimal Estimator of Randomly Maneuvering Targets for Terminal Guidance][research_shinar_2004]
- [Shivank and others, 2023, Aerothermodynamic design optimization of planetary vehicle][research_shivank_harshul_2023]
- [Shoemaker and others, 2012, Trajectory reconstruction of Hayabusa's atmospheric reentry][research_shoemaker_vanderha_2012]
- [Shojaie-bahaabad and others, 2024, Ultra high temperature ceramic coatings in thermal protection systems TPS][research_shojaiebahaabad_bozorg_2024]
- [SHOPE and SPINETTI, 1993, Aerodynamic design of a hypersonic body with a constant favorable pressure gradient][research_shope_spinetti_1993]
- [SHOPE, 1991, Aerodynamic design of a hypersonic body with a constant adverse pressure gradient][research_shope_1991]
- [Shorenstein, 1971, The Hypersonic Leading Edge Problem. 2. Wedges and Cones][research_shorenstein_1971]
- [SHORENSTEIN, 1972, Hypersonic Leading Edge Problem Wedges and Cones][research_shorenstein_1972]
- [SHOU and HAN, 2024, Channel coupling coordinated robust adaptive control algorithm for hypersonic flight vehicles][research_shou_han_2024]
- [Shou and others, 2021, Aerodynamic/reaction-jet compound control of hypersonic reentry vehicle using sliding mode control and neural learning][research_shou_xu_2021]
- [Shou and others, 2022, Coordinated adaptive control of hypersonic reentry vehicle considering channel coupling][research_shou_xu_2022]
- [Shou and others, 2025, Finite-Time Adaptive Control of Flexible Hypersonic Flight Vehicle Under Measurement Noise][research_shou_zhan_2025]
- [Shruster and Carpas, 1983, Approximation to the optimization of a coast-glide trajectory][research_shruster_carpas_1983]
- [Shu and others, 2007, The Full Flowpath Analysis of a Hypersonic Vehicle][research_shu_hongying_2007]
- [Shuai and others, 2022, Adaptive Tracking Control for Hypersonic Flight Vehicle Using ADHDP][research_shuai_daqian_2022]
- [Shuck and others, 2023, Computational Study of an Internal Osculating Waverider Intake][research_shuck_noftz_2023]
- [Shukurov, 2021, Backward-trajectory analysis of a link between the meteorological optical range and long-range air transport][research_shukurov_2021]
- [Shuping Tan and Zhibin Li, 2010, Switching control design for a hypersonic flight vehicle][research_shupingtan_zhibinli_2010]
- [Shuvayan Brahmachary and others, 2016, A Hybrid Aerodynamic Shape Optimization Approach for Axisymmetric Body in Hypersonic Flow][research_shuvayanbrahmachary_ganeshnatarajan_2016]
- [Shvets and others, 2005, On Waverider Performance with Hypersonic Flight Speed and High Altitudes][research_shvets_voronin_2005]
- [Si-Yuan and others, 2018, Design of Adaptive Inversion Control for a Hypersonic Vehicle][research_siyuan_xiaobing_2018]
- [Sidor and others, 2020, Numerical Methodology for the Conceptual Design of Conformal Ablative Heat Shields][research_sidor_kennedy_2020]
- [Siebenhaar and Bogar, 2006, The Impact of Round Combustors on TBCC Propulsion and Hypersonic Cruise Vehicles][research_siebenhaar_bogar_2006]
- [Sigthorsson and others, 2006, Tracking Control for an Overactuated Hypersonic Air-Breathing Vehicle with Steady State Constraints][research_sigthorsson_serrani_2006]
- [Sigthorsson and others, 2008, Robust Linear Output Feedback Control of an Airbreathing Hypersonic Vehicle][research_sigthorsson_jankovsky_2008]
- [Sills, 2000, Prompt Global Strikes Through Space What Military Value][research_sills_2000]
- [Sills, 2001, Space-Based Global Strike Understanding Strategic and Military Implications][research_sills_2001]
- [Silvester and Morgan, 2004, Computational Hypervelocity Aerodynamics of a Caret Waverider][research_silvester_morgan_2004]
- [Silvester and others, 2007, Superorbital expansion tube tests of a caret waverider][research_silvester_mcintyre_2007]
- [Silvestroni and Sciti, 2013, Effect of Transition Metal Silicides on Microstructure and Mechanical Properties of Ultra-High Temperature Ceramics][research_silvestroni_sciti_2013]
- [Simeonides, 2003, Correlation of laminar-turbulent transition data over flat plates in supersonic/hypersonic flow including leading edge bluntness effects][research_simeonides_2003]
- [Simeonides, 2006, Extrapolation-to-flight of aerodynamic heating measurements and determination of in-flight radiation-equilibrium surface temperature in hypersonic/high enthalpy flow conditions][research_simeonides_2006]
- [Simmons and Meritt, 2022, Hypersonic Instrumentation Testing for Thermal Protection Systems][research_simmons_meritt_2022]
- [Simon and others, 2021, Development of a Hypersonic Vehicle Configuration Compendium][research_simon_atchison_2021]
- [Simons, 1975, Advanced Reentry Aeromechanics. Volume II. Aerodynamic Shattering of Ice Crystals in Hypersonic Flight][research_simons_1975]
- [Simons, 1976, Aerodynamic shattering of ice crystals in hypersonic flight][research_simons_1976]
- [Sims and Hahn, 1964, AERODYNAMIC DRAG ON SPIKED BLUNT BODIES IN LOW-DENSITY HYPERSONIC FLOW][research_sims_hahn_1964]
- [Simsek and others, 2016, Aerodynamic Heating Prediction Tool for a Supersonic Vehicle for Conceptual Design Phase][research_simsek_kuran_2016]
- [Singh and others, 2017, Optimization of Hypersonic Power Law Derived Waverider Using TLBO][research_singh_devaraj_2017]
- [Singh and others, 2022, Bifurcation Analysis of Longitudinal Dynamics of Generic Air-Breathing Hypersonic Vehicle for Different Operating Flight Conditions][research_singh_prakash_2022]
- [Singh and others, 2022, Development of 3DOF Longitudinal Dynamic Model of Generic Air-breathing Hypersonic Vehicle][research_singh_prakash_2022_b]
- [Singh and others, 2022, Linear Controller Design for Generic Air-Breathing Hypersonic Vehicle for different Control Inputs][research_singh_prakash_2022_c]
- [SINGH and others, 2023, Numerical Analysis of an integrated Scramjet vehicle at Hypersonic Speed][research_singh_g_2023]
- [Singh and Sinha, 2023, Shock Induced Flow-Separation in Hypersonic Intakes at Off-Design Conditions][research_singh_sinha_2023]
- [Singh, 2026, Technological Innovation and Future Security-Impact of Supersonic and Hypersonic Weapon Systems on Air and Missile Defence][research_singh_2026]
- [Sinha and others, 2021, Three-Dimensional Guidance with Terminal Time Constraints for Wide Launch Envelops][research_sinha_kumar_2021]
- [Sinha and Reddy, 2007, Hypersonic Turbulent Reacting Flow Simulation of Fire II Re-entry Vehicle][research_sinha_reddy_2007]
- [Sippel and Klevanski, 2006, Preliminary Definition of Supersonic and Hypersonic Airliner Configurations][research_sippel_klevanski_2006]
- [SIVELLS, 1963, AERODYNAMIC DESIGN AND CALIBRATION OF THE VKF 50-INCH HYPERSONIC WIND TUNNELS][research_sivells_1963]
- [SIVELLS, 1969, Aerodynamic design of axisymmetric hypersonic wind tunnel nozzles][research_sivells_1969]
- [SIVELLS, 1970, Aerodynamic design of axisymmetric hypersonic wind-tunnel nozzles][research_sivells_1970]
- [Sivolella, 2014, The Orbiter's skin the thermal protection system][research_sivolella_2014]
- [Skolnik and others, 2017, Design of a Novel Hypersonic Inflatable Aerodynamic Decelerator for Mars Entry, Descent, and Landing][research_skolnik_kamezawa_2017]
- [Skripnyak and others, 2017, Fracture mechanisms of zirconium diboride ultra-high temperature ceramics under pulse loading][research_skripnyak_bragov_2017]
- [Skripnyak and Skripnyak, 2017, Predicting the mechanical properties of ultra-high temperature ceramics][research_skripnyak_skripnyak_2017]
- [Skujins and Cesnik, 2010, Reduced-Order Modeling of Hypersonic Vehicle Unsteady Aerodynamics][research_skujins_cesnik_2010]
- [Slapikas and others, 2022, Molecular Dynamics Analysis and Optimization of Ultra-High-Temperature Ceramic UHTC Compositions for Propulsion][research_slapikas_ghoshal_2022]
- [Smiley and Camberos, 2024, Importance of Control and Stability Analysis on Hypersonic Vehicle Design][research_smiley_camberos_2024]
- [Smith and others, 2021, Modeling Hypersonic Vehicle Interdependencies at the Subsystem Level][research_smith_sitchin_2021]
- [Smith, 2008, Proportional Navigation with Adaptive Terminal Guidance for Aircraft Rendezvous][research_smith_2008]
- [Smith, 2021, Aerodynamic heating in hypersonic flows][research_smith_2021]
- [Sobieczky, 2026, Generic Configurations for Hypersonic Design and Analysis][research_sobieczky_2026]
- [Socha and others, 2015, How animals glide from trajectory to morphology][research_socha_jafari_2015]
- [Sockalingam and Tabiei, 2009, Fluid/thermal/chemical non-equilibrium simulation of hypersonic reentry vehicles][research_sockalingam_tabiei_2009]
- [Sogin, 1991, An Improved Correlation of Stagnation Point Mass Transfer From Naphthalene Circular Disks Facing Uniform Airstreams][research_sogin_1991]
- [Son and others, 2022, A Novel Direct Optimization Framework for Hypersonic Waverider Inverse Design Methods][research_son_son_2022]
- [Sonber and others, 2013, Processing Methods for Ultra High Temperature Ceramics][research_sonber_chmurthy_2013]
- [Song and Bian, 2019, An Improvement of PWPF in Reaction Control System of Hypersonic Vehicle][research_song_bian_2019]
- [Song and Choi, 2020, Hybrid Control Trajectory Optimization for Air-breathing Hypersonic Vehicle][research_song_choi_2020]
- [Song and others, 2018, Control Allocation-Based Command Tracking-Control System for Hypersonic Re-entry Vehicle Driven by Hybrid Effecters][research_song_cai_2018]
- [Song and others, 2019, Double-Loop Sliding Mode Control of Reentry Hypersonic Vehicle with RCS][research_song_hao_2019]
- [Song and others, 2021, Effect of Time-Varying Plasma Sheath on Hypersonic Vehicle-Borne Radar Target Detection][research_song_li_2021]
- [Song and others, 2022, A Real-Time Reentry Guidance Method for Hypersonic Vehicles Based on a Time2vec and Transformer Network][research_song_tong_2022]
- [Song and others, 2022, Fault-Tolerant Integrated Guidance and Control Design for Hypersonic Vehicle Based on PPO][research_song_luo_2022]
- [Song and others, 2024, 3D Guidance for Maneuvering Targets with Terminal Angle Constraints An Incremental Nonsingular Terminal Sliding Mode Approach][research_song_zhu_2024]
- [Song and others, 2024, Online Reentry Trajectory Optimization for Hypersonic Vehicles Using Radau Pseudospectral Sequential Convex Programming][research_song_liu_2024]
- [Song and others, 2026, Surrogate-Assisted Optimization of Hypersonic Gliding Vehicle for Range Extension in Re-entry Flight][research_song_shi_2026]
- [Song and Tong, 2026, Collaborative Guidance and Decision Integration for Hypersonic Reentry Vehicles A Review][research_song_tong_2026]
- [Sostaric and others, 2017, A Rigid Mid Lift-to-Drag Ratio Approach to Human Mars Entry, Descent, and Landing][research_sostaric_cerimele_2017]
- [Sostaric and others, 2019, Aeroballistic Range Testing of the CobraMRV Mid Lift-to-Drag Entry Vehicle][research_sostaric_garcia_2019]
- [SPEARMAN, 1984, Aerodynamic characteristics of some lifting reentry concepts applicable to transatmospheric vehicle design studies][research_spearman_1984]
- [Spearman, 2003, Some NASA Wind-Tunnel Studies Related to the Aerodynamics of Hypersonic Vehicles][research_spearman_2003]
- [SPEYER and others, 1980, Periodic optimal cruise of a hypersonic vehicle][research_speyer_dannemiller_1980]
- [Spinardi, 2008, Ballistic missile defence and the politics of testing the case of the US ground-based midcourse defence][research_spinardi_2008]
- [Spravka and Jorris, 2015, Current Hypersonic and Space Vehicle Flight Test and Instrumentation][research_spravka_jorris_2015_b]
- [Spravka and Jorris, 2015, Current Hypersonic and Space Vehicle Flight Test Instrumentation Challenges][research_spravka_jorris_2015]
- [Sprinks, 2011, Range of training opportunities to boost health visitor workforce][research_sprinks_2011]
- [Sridharan and Rodriguez, 2013, Impact of Control Specifications on Vehicle Design for Scramjet-Powered Hypersonic Vehicles][research_sridharan_rodriguez_2013]
- [Srinath and Reddy, 2010, Experimental Investigation of the Effects of Aerospike Geometry on Aerodynamic Drag and Heat Transfer Rates for a Blunt Body Configuration at Hypersonic Mach Numbers][research_srinath_reddy_2010]
- [Srivastava and others, 2022, Fourier series and Search Space Reduction based Control profiles for Reentry Trajectory Optimization][research_srivastava_mishra_2022]
- [STALONY-DOBRZANSKI, 1966, Effect of trajectory control scheme on the performance of lifting entry vehicles][research_stalonydobrzanski_1966]
- [Stanley and others, 1999, A collaborative analysis tool for integrating hypersonic aerodynamics, thermal protection systems, and RBCC engine performance for single stage to orbit launch vehicles][research_stanley_alexander_1999]
- [Starkey and Lewis, 1999, Aerodynamics of a box constrained waverider missile using multiple scramjets][research_starkey_lewis_1999_b]
- [Starkey and Lewis, 1999, Performance of hypersonic waverider missiles using multiple scram jets][research_starkey_lewis_1999]
- [Starkey and Lewis, 2000, Analytical Off-Design Lift-to-Drag-Ratio Analysis for Hypersonic Waveriders][research_starkey_lewis_2000]
- [Starkey and Lewis, 2001, Critical Design Issues for Airbreathing Hypersonic Waverider Missiles][research_starkey_lewis_2001]
- [Starkey and others, 2005, Coupled Waverider/Trajectory Optimization for Hypersonic Cruise][research_starkey_rankins_2005]
- [Starkey and others, 2006, Effects of Hypersonic Cruise Trajectory Optimization Coupled with Airbreathing Vehicle Design][research_starkey_rankins_2006]
- [Starkey, 2014, MDO for Hypersonic Scramjet Vehicle Development Invited][research_starkey_2014]
- [Starkey, 2015, Hypersonic Vehicle Telemetry Blackout Analysis][research_starkey_2015]
- [Starshak and Laurence, 2021, Computer-Graphics-Based Optical Tracking for Hypersonic Free-Flight Experiments][research_starshak_laurence_2021]
- [STECKLEIN and others, 1993, Numerical solution of inviscid hypersonic flow around a conically-derived waverider][research_stecklein_hasen_1993]
- [Steelant and van Duijn, 2011, Structural Analysis of the LAPCAT-MR2 Waverider Based Vehicle][research_steelant_vanduijn_2011]
- [Steele, 2009, Evolved Expendable Launch Vehicles EELV for Operationally Responsive Space][research_steele_2009]
- [STEFFAN, 1961, Satellite Rendezvous Terminal Guidance System][research_steffan_1961]
- [Stein and Raghavan, 2024, High Energy X-ray Investigation of Ultra-High Temperature Ceramics under Thermal Cycling][research_stein_raghavan_2024]
- [Steinfeldt and others, 2013, Rapid Robust Design of a Deployable System for Boost-Glide Vehicles][research_steinfeldt_rossman_2013]
- [Stender and Loghry, 2017, Utilizing small launch vehicles for multiple small payload missions][research_stender_loghry_2017]
- [Stephan and Obermeier, 1974, CORRELATION OF HEAT TRANSFER COEFFICIENTS IN HYPERSONIC STAGNATION POINT FLOW][research_stephan_obermeier_1974]
- [Stern and Chu, 1963, LANDING SITE COVERAGE FOR ORBITAL LIFTING REENTRY VEHICLES][research_stern_chu_1963]
- [Stevens and others, 1995, Taurus - Small launch vehicle technologies development][research_stevens_lockwood_1995]
- [STEVENS, 1992, Practical considerations in waverider applications][research_stevens_1992]
- [Stewart and Leiser, 2006, Lightweight TUFROC TPS for Hypersonic Vehicles][research_stewart_leiser_2006]
- [STEWART and others, 1985, Effect of variable surface catalysis on heating near the stagnation point of a blunt body][research_stewart_leiser_1985]
- [STEWART and others, 1992, Computational fluid dynamics application to hypersonic flow over a Martian entry vehicle MEV - A correlation with experiment][research_stewart_smith_1992]
- [Stiles, 1970, Predictive Entry Guidance for an Apollo-Type Vehicle][research_stiles_1970]
- [Stoffel and others, 2024, Fusion of In-Flight Aerothermodynamic Heating Sensor Measurements Using Kalman Filtering][research_stoffel_karlgaard_2024]
- [Stokes and Lombaerts, 2023, Control System Design for a Hypersonic Re-entry Vehicle][research_stokes_lombaerts_2023]
- [Stoll, 1961, THERMAL PROTECTION CAPACITY OF AVIATOR'S TEXTILES][research_stoll_1961]
- [Stollery, 1992, Some Viscous Interactions Affecting the Design of Hypersonic Intakes and Nozzles][research_stollery_1992]
- [Stollery, 2010, Selected Aerothermodynamic Design Problems of Hypersonic Flight Vehicles E. H. Hirschel and C. Weiland Springer-Verlag, Tiergartenstrasse 17, D-69121 Heidelberg, Germany. 2009. 518pp. Illustrated. £81.50. ISBN 978-3-540-89973-0][research_stollery_2010]
- [STONER, 1972, Spiral descent terminal guidance][research_stoner_1972]
- [Strauss, 1966, New Ablative Heat Shield Materials for Mars Landers][research_strauss_1966]
- [Strippoli and others, 2013, Mission analysis and guidance, navigation, and control design for rendezvous and docking phase of advanced reentry vehicle mission][research_strippoli_colmenarejo_2013]
- [Strohm, 2011, A Terminal Guidance Model for Smart Projectiles Employing a Semi-Active Laser Seeker][research_strohm_2011]
- [Strohmeyer and Eggers, 1997, Impact of Planform Geometry on Waverider Aerodynamics][research_strohmeyer_eggers_1997]
- [Su and Liu, 2025, Constraint-handling techniques for reusable launch vehicle reentry trajectory optimization using marine predator whale optimizer][research_su_liu_2025]
- [Su and Liu, 2025, Reentry trajectory optimization for reusable launch vehicle using marine predator whale optimizer and smoothing technique][research_su_liu_2025_b]
- [Su and others, 2013, Modeling and robust decoupling control for hypersonic scramjet vehicle][research_su_jiang_2013]
- [Su and others, 2013, Moving Mass Actuated Reentry Vehicle Control Based on Trajectory Linearization][research_su_yu_2013]
- [Su and others, 2021, A hybrid hyper-heuristic whale optimization algorithm for reusable launch vehicle reentry trajectory optimization][research_su_dai_2021]
- [Su and others, 2023, A Real-Time and Optimal Hypersonic Entry Guidance Method Using Inverse Reinforcement Learning][research_su_wang_2023]
- [Su and others, 2024, Reentry trajectory optimization of hypersonic glide vehicle based on improved particle swarm algorithm][research_su_zhao_2024]
- [Su and others, 2025, Reentry initial descent stage guidance method for lift-type reentry vehicle][research_su_hong_2025]
- [Su, 2017, Compartmental Tank Propellant Management System Design and Operation for Hypersonic Vehicle][research_su_2017]
- [Subrahmanyam, 2008, Development of an Interactive Hypersonic Flow Solver Framework for Aerothermodynamic Analysis][research_subrahmanyam_2008]
- [Sudalagunta and others, 2018, Aeroelastic Control-Oriented Modeling of an Airbreathing Hypersonic Vehicle][research_sudalagunta_sultan_2018]
- [Sudhir and Tewari, 2007, Adaptive maneuvering entry guidance with ground-track control][research_sudhir_tewari_2007]
- [Sui and others, 2023, Influence of vehicle length on the aerothermodynamic environment of the Hyperloop][research_sui_niu_2023]
- [Sun and Duan, 2012, Optimal feedback reentry guidance of hypersonic vehicle based on improved Gauss pseudospectral method][research_sun_duan_2012]
- [Sun and others, 2009, Configuration Optimization of Hypersonic Vehicles under Transitional Flow Conditions][research_sun_fan_2009]
- [Sun and others, 2013, New Tracking-Control Strategy for Airbreathing Hypersonic Vehicles][research_sun_yang_2013]
- [Sun and others, 2014, Tracking control of a class of non-linear systems with applications to cruise control of air-breathing hypersonic vehicles][research_sun_yang_2014]
- [SUN and others, 2015, The ablation antenna design and verification of circumlunar free return and reentry flight vehicle][research_sun_yang_2015]
- [Sun and others, 2017, Drag tracking sliding mode control for mars atmospheric reentry][research_sun_huang_2017]
- [Sun and others, 2017, Finite-time tracking control of hypersonic vehicle with input saturation][research_sun_xu_2017]
- [Sun and others, 2017, Tracking Control of Hypersonic Vehicle Considering Input Constraint][research_sun_song_2017]
- [Sun and others, 2018, An effective flux scheme for hypersonic heating prediction of re-entry vehicles][research_sun_qu_2018]
- [SUN and others, 2020, Numerical Prediction of Flow Field and Aerodynamic Heating in the Gap of Hypersonic Vehicle][research_sun_yang_2020]
- [Sun and others, 2020, Thermo-Structural Behaviour Prediction of the Nose Cap of a Hypersonic Vehicle Based on Multifield Coupling][research_sun_yang_2020_b]
- [Sun and others, 2022, Guidance for hypersonic re-entry using receding horizon control with finite terminal weighting matrix][research_sun_xu_2022]
- [Sun and others, 2022, Numerical simulation of hypersonic vehicle plasma sheath and the attenuation effects on electromagnetic wave transmission][research_sun_xia_2022]
- [Sun and others, 2022, Skip re-entry trajectory detection in aero-assisted orbit transfer][research_sun_tang_2022]
- [Sun and others, 2023, Aerodynamic Thermal Simulation and Heat Flux Distribution Study of Mechanical Expansion Reentry Vehicle][research_sun_zhu_2023]
- [Sun and others, 2024, Analytical Solutions for Hypersonic Glide Trajectory Based on Altitude-Velocity Profile][research_sun_ma_2024]
- [Sun and others, 2024, Stream-Surface Iteration-Based Flowfield Calculation Method for Pressure-Controllable Waverider Design][research_sun_zheng_2024]
- [Sun and others, 2024, Study on the aerodynamic characteristics of reentry capsule with obtuse head inverted cone under hypersonic chemical nonequilibrium flow][research_sun_chen_2024]
- [Sun and others, 2024, Transient Numerical Study on Drag Reduction and Thermal Protection Characteristics of Porous Reverse Jet in Deployable Reentry Vehicles][research_sun_han_2024]
- [Sun and others, 2025, Discontinuous Trajectory Tracking of Hypersonic Glide Reentry Vehicle An Intention Inference Approach][research_sun_ran_2025]
- [Sun and others, 2025, Optimization of mechanical deployable reentry vehicle based on multi-fidelity aerodynamic-trajectory coupling model][research_sun_zhu_2025]
- [Sun and others, 2025, Planetary Entry Trajectory Optimization under Temporal Logic and Environmental Constraints][research_sun_liu_2025]
- [Sun and others, 2025, Prediction Method for Discontinuous Hypersonic Gliding Reentry Vehicle Trajectory][research_sun_huang_2025]
- [Sun and others, 2026, Leader-Follower Formation Trajectory Planning for Unmanned Reentry Vehicles Based on Quasi-Equilibrium Glide][research_sun_li_2026_c]
- [Sun and others, 2026, Online Trajectory Planning for Hypersonic Glide Vehicle Under Multiple No-Fly Zones An Attention Mechanism-Based BiGRU Framework][research_sun_li_2026]
- [Sun and others, 2026, QEGC-based time-coordinated analytical entry guidance for reentry glide vehicles with irregular no-fly zones][research_sun_li_2026_d]
- [Sun and others, 2026, Transient Dynamics of Multi-Port Lateral Jet Interactions on a Hypersonic Vehicle][research_sun_cao_2026]
- [Sun and others, 2026, Two-stage cooperative trajectory planning for hypersonic glide vehicles A bio-inspired optimization approach][research_sun_li_2026_b]
- [Sun and Sun, 2014, Thermal-Structural Analysis of Ni-Based Alloy Panel with Active Cooling Thermal Protection System][research_sun_sun_2014]
- [Sun and Xin, 2014, Hypersonic Entry Vehicle State Estimation Using High-degree Cubature Kalman Filter][research_sun_xin_2014]
- [Sun and Xin, 2017, Hypersonic entry vehicle state estimation using nonlinearity-based adaptive cubature Kalman filters][research_sun_xin_2017]
- [Sun and Zhang, 2011, Optimal reentry range trajectory of hypersonic vehicle by Gauss Pseudospectral Method][research_sun_zhang_2011]
- [Sun and Zhang, 2020, Skip Re-Entry Trajectory Detection and Guidance for Maneuvering Vehicles][research_sun_zhang_2020]
- [Sun and Zhao, 2013, Phase Plane Control for Small Launch Vehicle][research_sun_zhao_2013]
- [Sun and Zhu, 2019, A physical model for solving the dredging thermal protection system of hypersonic vehicle leading edge][research_sun_zhu_2019]
- [Sun Jian and Liu Wei-Qiang, 2013, Investigation on integral model of heat-pipe-cooled leading edge of hypersonic vehicle][research_sunjian_liuweiqiang_2013]
- [Sun Jian and Liu Wei-Qiang, 2014, Experimental investigation of dredging thermal protection system of hypersonic vehicle leading edge][research_sunjian_liuweiqiang_2014]
- [Sushnigdha and Joshi, 2016, Evolutionary Method Based Hybrid Entry Guidance Strategy for Reentry Vehicles][research_sushnigdha_joshi_2016]
- [Sushnigdha and Joshi, 2017, Re-entry Trajectory Design using Pigeon Inspired Optimization][research_sushnigdha_joshi_2017]
- [Sushnigdha and Joshi, 2018, Evolutionary method based integrated guidance strategy for reentry vehicles][research_sushnigdha_joshi_2018_b]
- [Sushnigdha and Joshi, 2018, Reentry Trajectory Design with Pigeon Inspired Optimization Using Derived Angle of Attack Profile][research_sushnigdha_joshi_2018]
- [Sushnigdha, 2022, Spacecraft Reentry Trajectory Optimization using Search Space Reduction Technique][research_sushnigdha_2022]
- [Susic and others, 2026, K-ADEPT Modeling the Hypersonic Reentry of an Innovative Thermal Protection System][research_susic_davuluri_2026]
- [Sutheesh and Chollackal, 2020, Numerical Simulation and Performance Analysis of MLI During Reentry of Hypersonic Vehicles][research_sutheesh_chollackal_2020]
- [Suvorova and others, 2023, Fabrication and investigation of novel hafnium-zirconium carbonitride ultra-high temperature ceramics][research_suvorova_khadyrova_2023]
- [Suwantong and others, 2012, Space debris trajectory estimation during atmospheric reentry using moving horizon estimator][research_suwantong_bertrand_2012]
- [SUZUKI and others, 1997, Navigation, Guidance and Control of Hypersonic Flight Experiment Vehicle HYFLEX and Actual Reentry Flight Trajectory][research_suzuki_ishimoto_1997]
- [Suzuki and others, 2001, Unified calculation of hypersonic flowfield for a reentry vehicle][research_suzuki_furudate_2001]
- [SUZUKI and others, 2002, Trajectory-Based Heating Analysis and In-Depth Response of Ablative Heatshield for Reentry Capsule][research_suzuki_sawada_2002]
- [Suzuki and others, 2002, Unified Calculation of Hypersonic Flowfield for a Reentry Vehicle][research_suzuki_furudate_2002]
- [Suzuki, 2001, The Effect of the Small Damping Sloshing to the Flexible Launch Vehicle Stability][research_suzuki_2001]
- [SUZUKI, 2016, Aerodynamic Shape Design of Hypersonic Booster with RBCC Engine for TSTO Vehicle][research_suzuki_2016]
- [SUZUKI, 2018, Aerothermodynamic Studies on Low-Ballistic-Coefficient Mars Aerocapture Vehicle with Drag Modulation and Electric Propulsion][research_suzuki_2018]
- [Swain and others, 2025, Auto Object Detection and Tracking Using Trajectory Matching in Test Range Scenarios][research_swain_chauhan_2025]
- [Swain and Sushnigdha, 2025, Mars Entry Trajectory Optimization Using Search Space Reduction and Sequential Quadratic Programming][research_swain_sushnigdha_2025]
- [SWAIN, 1975, The effect of particle/shock layer interaction on reentry vehicle performance][research_swain_1975]
- [Swann, 1960, AN ENGINEERING ANALYSIS OF THE WEIGHTS OF ABLATING SYSTEMS FOR MANNED ° REENTRY VEHICLES][research_swann_1960]
- [Swanson and others, 2007, Hypersonic Vehicle Thermal Structure Test Challenges][research_swanson_caghlan_2007]
- [SWORDER and ARCHER, 1977, Selection of the independent guidance variable for an aerodynamically controlled re-entry vehicle][research_sworder_archer_1977]
- [Sziroczak and Smith, 2016, A review of design issues specific to hypersonic flight vehicles][research_sziroczak_smith_2016]
- [T and CM, 2017, Drag Reduction Optimization for Hypersonic Blunt Body with Aerospikes][research_t_cm_2017]
- [Tabiei and Sockalingam, 2012, Multiphysics Coupled Fluid/Thermal/Structural Simulation for Hypersonic Reentry Vehicles][research_tabiei_sockalingam_2012]
- [Tablole and Banavar, 1998, Predictive Control-Based Optimal Nonliear Reentry Guidance Law][research_tablole_banavar_1998]
- [Tacchi and others, 2023, Inverse estimation of the Kentucky Re-entry Universal Payload System KRUPS flight trajectory][research_tacchi_martin_2023]
- [Tacchi and others, 2024, Reconstruction of the Kentucky Re-Entry Universal Payload System Hypersonic Flight Trajectory][research_tacchi_stoffel_2024]
- [Tachinina and others, 2018, Algorithm for Operational Optimization of Two-Stage Hypersonic Unmanned Aerial Vehicle Branching Path][research_tachinina_lysenko_2018]
- [TAGUCHI and others, 2009, Conceptual Study on Hypersonic Turbojet Experimental Vehicle HYTEX][research_taguchi_murakami_2009]
- [Taguchi and others, 2009, Firing Test of a Hypersonic Turbojet Engine Installed on a Flight Test Vehicle][research_taguchi_harada_2009]
- [Taheri and Ahmadi, 2026, Fast Cooperative Close-Range Satellite Formation Trajectory Optimization Using Finite Fourier Series Method][research_taheri_ahmadi_2026]
- [Tahmasbi and Noori, 2018, Thermal Analysis of Honeycomb Sandwich Panels as Substrate of Ablative Heat Shield][research_tahmasbi_noori_2018]
- [Tahsini and Mousavi, 2014, Ablative Heat Shield Design for Reentry Vehicle Using Numerical Analysis][research_tahsini_mousavi_2014]
- [Taihua and others, 2011, The Mechanics Analysis of Desquamation for Thermal Protection System TPS Tiles of Spacecraft][research_taihua_xianhong_2011]
- [Takahashi and Griffin, 2023, Hypersonic Aircraft Performance Limitations Arising from Aerodynamic Control Limits][research_takahashi_griffin_2023]
- [Takahashi and others, 2013, Aerodynamic Heating around an Inflatable Vehicle during a Reentry Demonstration Flight by a Sounding Rocket][research_takahashi_yamada_2013]
- [Takahashi and others, 2015, Aerodynamic Heating Around Flare-Type Membrane Inflatable Vehicle in Suborbital Reentry Demonstration Flight][research_takahashi_yamada_2015]
- [Takahashi and others, 2025, Flush Air-Data Sensing System for Hypersonic Flight Experimental Vehicle With Ogive-Shaped Nose][research_takahashi_hirotani_2025]
- [Takahashi and others, 2026, Flush Air-Data Sensing System for a Hypersonic Flight Experimental Vehicle][research_takahashi_hirotani_2026]
- [Takahashi and Yamada, 2018, Aerodynamic heating of inflatable aeroshell in orbital reentry][research_takahashi_yamada_2018]
- [Takama, 2011, Practical waverider with outer wings for the improvement of low-speed aerodynamic performance][research_takama_2011]
- [TAKASHIMA and LEWIS, 1992, Navier-Stokes computations of a viscous optimized waverider][research_takashima_lewis_1992]
- [Takashima and Lewis, 1994, Navier-Stokes computation of a viscous optimized waverider][research_takashima_lewis_1994]
- [Takashima and Lewis, 1995, Powered hypersonic waverider vehicles for optimization with mission-oriented constraints][research_takashima_lewis_1995_b]
- [Takashima and Lewis, 1995, Wedge-cone waverider configuration for engine-airframe interaction][research_takashima_lewis_1995]
- [Takashima and Lewis, 1996, Engine-airframe integration on osculating cone waverider-based vehicle designs][research_takashima_lewis_1996_c]
- [Takashima and Lewis, 1996, Optimized mission-oriented waverider vehicles with base closure][research_takashima_lewis_1996_b]
- [Takashima and Lewis, 1999, Optimization of Waverider-Based Hypersonic Cruise Vehicles with Off-Design Considerations][research_takashima_lewis_1999]
- [Takashima and others, 1996, Waverider configuration development for the dual fuel vehicle][research_takashima_lewis_1996]
- [Takehira and others, 1997, Analytical solution of missile terminal guidance][research_takehira_vinh_1997]
- [Takehira and others, 1998, Analytical Solution of Missile Terminal Guidance][research_takehira_vinh_1998]
- [TALBOT, 1963, CRITERION FOR SLIP NEAR THE LEADING EDGE OF A FLAT PLATE IN HYPERSONIC FLOW][research_talbot_1963]
- [Tan and others, 2019, Optimal Maneuver Trajectory for Hypersonic Missiles in Dive Phase Using Inverted Flight][research_tan_lei_2019]
- [TAN and YAN, 2012, Linear quadratic control based on stochastic robustness design for hypersonic vehicles][research_tan_yan_2012]
- [Tang and others, 2011, Reentry trajectory planning based on genetic optimization of terminal matching][research_tang_chen_2011]
- [Tang and others, 2018, A Novel Robust Flight Controller Design for an Air-Breathing Hypersonic Vehicle][research_tang_long_2018]
- [Tang and others, 2020, Adaptive fault-tolerance control based finite-time backstepping for hypersonic flight vehicle with full state constrains][research_tang_zhai_2020]
- [Tang and others, 2020, Reentry Trajectory Optimization Based on Second Order Cone Programming][research_tang_he_2020]
- [Tang and others, 2021, Aerothermodynamic characteristics of hypersonic curved compression ramp flows with bistable states][research_tang_wang_2021]
- [Tang and others, 2021, The Discrete Sliding Mode Control for a Hypersonic Vehicle][research_tang_gao_2021]
- [Tang and others, 2022, Fuzzy Adaptive Finite-Time Tracking for Hypersonic Flight Vehicles Using Switching Event-Triggered Methodology][research_tang_di_2022]
- [Tang and others, 2022, Profile Tracking Control of Reentry Vehicle With Input-constrained Backstepping Sliding Mode Controller][research_tang_luo_2022]
- [Tang and others, 2023, A preliminary experimental study of the supercritical CO2 U-shaped compact heat exchanger for the hypersonic vehicle][research_tang_chen_2023]
- [Tang and others, 2023, Preshaping Trajectory Optimization and Control of Flexible Hypersonic Vehicle for Vibration Suppression][research_tang_hu_2023]
- [Tang and others, 2025, Coupling effects of flow separation and aerodynamic heating in hypersonic shock wave and turbulent boundary layer interaction][research_tang_li_2025]
- [Tang and others, 2025, Design concept of compression wave and opposite cowl shock configuration for hypersonic inlet with inward deflecting cowl][research_tang_cai_2025]
- [Tang and others, 2025, Modeling and Control Methods for Hypersonic Vehicle Considering Inlet Unstart][research_tang_zhang_2025]
- [Tangermann and others, 2012, Detached Eddy Simulation Compared with Wind Tunnel Results of a Delta Wing with Sharp Leading Edge and Vortex Breakdown][research_tangermann_furman_2012]
- [TANNAS, 1966, ENTRY GUIDANCE THROUGH CLOSED FORM RANGE EQUATIONS][research_tannas_1966]
- [Tannehill and Eisler, 1976, Numerical computation of the hypersonic leading edge problem using the Burnett equations][research_tannehill_eisler_1976]
- [TANNEHILL and others, 1974, Numerical Computation of Hypersonic Viscous Flow over a Sharp Leading Edge][research_tannehill_mohling_1974]
- [Tanriverdi and Cavdaroglu, 2017, Utilization of INS Measurements into Fixed-Point Smoothing Approach to Mitigate the Disturbance Effect of Missile Initial Heading Errors on Missile Terminal Guidance Performance][research_tanriverdi_cavdaroglu_2017]
- [Tao and others, 2016, Multiple model predictive control for large envelope flight of hypersonic vehicle systems][research_tao_li_2016]
- [Tao and others, 2017, A nonlinear control approach for a hypersonic vehicle][research_tao_wan_2017]
- [Tao and others, 2025, Game Penetration Trajectory Planning Method for Hypersonic Vehicle Based on Hp-adaptive Gaussian Pseudospectral Method][research_tao_zhou_2025]
- [Tao Guo and others, 2010, Novel aeroassisted orbital transfer optimal guidance algorithm for reentry vehicle][research_taoguo_daweiliu_2010]
- [Tao Xu and others, 2011, Research on algorithm of counter target lost for Maneuvering Reentry Vehicle using Infrared imaging terminal guidance][research_taoxu_xiaopingzhu_2011]
- [Tarjáni, 2023, Hypersonic Weapon Systems as an Indicator of Changes in Concepts and Theories][research_tarjani_2023]
- [Tarpley and Lewis, 1995, Optimization of an engine-integrated waverider with steady state flight constraints][research_tarpley_lewis_1995_c]
- [Tarpley and Lewis, 1995, Sensitivity of engine-integrated waverider performance to static margin constraint][research_tarpley_lewis_1995_b]
- [Tarpley and Lewis, 1995, Stability derivatives for a hypersonic caret-wing waverider][research_tarpley_lewis_1995]
- [Tarpley and others, 1996, Low-speed stability analysis of the dual fuel waverider configuration][research_tarpley_pines_1996]
- [Tartabini and others, 2011, Ares I-X Separation and Reentry Trajectory Analyses][research_tartabini_starr_2011]
- [TATE, 1964, TECHNIQUES FOR AERODYNAMIC TESTING IN THE WAVE SUPERHEATER HYPERSONIC TUNNEL][research_tate_1964]
- [Tater and Holman, 2026, Matrix-Free LU-SGS Solver for Hypersonic Laminar Diatomic Gas Flows with Decoupled Vibrational Energy Mode Mesh Effects on Shock Waves and Separation Bubble in Double-Cone Flow][research_tater_holman_2026]
- [Tatsuta and others, 2025, Aerothermal Environment Prediction of Reentry Capsule With Deployable Aeroshell in Suborbital Reentry Flight Test][research_tatsuta_nagata_2025]
- [TAUB, 1968, Hypersonic, low-density sphere and cone drag correlations][research_taub_1968]
- [Tauber and Sutton, 1991, Stagnation-point radiative heating relations for earth and Mars entries][research_tauber_sutton_1991]
- [Taur, 2013, Anti-Missile RF Homing Guidance and Navigation with Terminal Side Jet][research_taur_2013]
- [Tava and Suzuki, 2001, Multidisciplinary design optimization of a re-entry vehicle shape and trajectory][research_tava_suzuki_2001]
- [Tava and Suzuki, 2002, Multidisciplinary Design Optimization of the Shape and Trajectory of a Reentry Vehicle][research_tava_suzuki_2002]
- [Tawfiqur and others, 2011, Trajectory Optimization of Hypersonic Vehicle Using Gauss Pseudospectral Method][research_tawfiqur_zhou_2011]
- [TAYLOR and JACKSON, 1980, Thermostructural analyses of structural concepts for hypersonic cruise vehicles][research_taylor_jackson_1980]
- [Taylor, 2004, Drag Reduction and Control Using Energetics and Electrostatic Force-Fields for Hypersonic Applications][research_taylor_2004]
- [Tejtel and others, 2011, Computational Prediction of Aerothermodynamic Characteristics of a Reentry Vehicle at High Angles of Attack][research_tejtel_rothnie_2011]
- [Teng and others, 2016, Tracking performance and global stability guaranteed neural control of uncertain hypersonic flight vehicle][research_teng_yang_2016]
- [Teng and others, 2023, Time-Cooperative Trajectory Optimization Method for Hypersonic Vehicle based on Improved Grey Wolf Artificial Potential Field Method][research_teng_xu_2023]
- [Teng and Yuan, 2013, Design Methodology and Unsteady Aerodynamic Characteristics of a Rectangular Variable Geometry Hypersonic Inlet][research_teng_yuan_2013]
- [Tengli and others, 2025, Design and Computational Analysis of Hypersonic Flight Vehicle][research_tengli_shetty_2025]
- [TERASAKI, 1963, A GUIDANCE SCHEME FOR LIFTING REENTRY][research_terasaki_1963]
- [Theisinger and others, 2010, Aerothermodynamic Shape Optimization of Hypersonic Entry Aeroshells][research_theisinger_braun_2010]
- [THEOBALD, 1966, Comments on "Motion of Re-Entry Vehicles During Constant-Altitude Glide"][research_theobald_1966]
- [Theofilis and Hermanns, 2013, On Global Linear Instability Analysis of Hypersonic Flow Around a Model Re-Entry Vehicle][research_theofilis_hermanns_2013]
- [Thiagarajan and Sharma, 2023, Experimental Evaluation of Isolated Intake for Hypersonic Air- Breathing Vehicle][research_thiagarajan_sharma_2023]
- [Thibodeaux, 2002, Hypersonic Vehicle Electric Power System Technology][research_thibodeaux_2002]
- [Thien, 2026, Adaptive Guidance and Optimal Trajectory Generation for Highly Maneuvering UAVs][research_thien_2026]
- [Thivet and Pélissier, 2003, Reduction of the Hypersonic Heat Flux Behavior on Catalytic Walls][research_thivet_pelissier_2003]
- [Thoemel and others, 2009, In-Flight Testing of Critical Technologies and Experimentation of Aerothermodynamic Phenomena][research_thoemel_muylaert_2009]
- [Thomas and others, 1982, Importance of phase corrections to waverider data][research_thomas_stickels_1982]
- [Thomas and others, 2022, Heat Transfer Study of a Conically Shaped Hypersonic Vehicle in Glide][research_thomas_marayikkottuvijayan_2022]
- [Thome and others, 2018, Direct numerical simulation of BOLT hypersonic flight vehicle][research_thome_dwivedi_2018]
- [Thompson and Hull, 1970, Hypersonic airfoils of maximum lift-to-drag ratio][research_thompson_hull_1970]
- [Thompson and Riley, 1994, Engineering code for hypersonic vehicle optimization][research_thompson_riley_1994]
- [Thornton, 2019, Countering Prompt Global Strike The Russian Military Presence in Syria and the Eastern Mediterranean and Its Strategic Deterrence Role][research_thornton_2019]
- [Tian and others, 2013, A parameterized geometry design method for inward turning inlet compatible waverider][research_tian_li_2013]
- [Tian and others, 2013, Flight Dynamics Modeling and Analysis of Flexible Hypersonic Flight Vehicles][research_tian_tang_2013]
- [Tian and others, 2015, Integrated guidance and control for reusable launch vehicle in reentry phase][research_tian_fan_2015]
- [Tian and others, 2023, Numerical Investigation on the Thermal Protection Characteristics of a New Active Jet Design Parameter for Hypersonic Flight Vehicle][research_tian_duan_2023]
- [Tian and Shen, 2022, Air-breathing hypersonic vehicle trajectory optimization with uncertain no-fly zones][research_tian_shen_2022]
- [Tian and Zhang, 2013, Multi-target tracking algorithm of boost-phase ballistic missile defense][research_tian_zhang_2013]
- [Tian and Zong, 2011, Optimal guidance for reentry vehicles based on indirect Legendre pseudospectral method][research_tian_zong_2011]
- [Tian Muyin and Shen Zuojun, 2019, A Rapid Hybrid Method for Powered Reentry Trajectory Planning with Uncertain No-Fly Zone Constraints][research_tianmuyin_shenzuojun_2019]
- [Tianyang and others, 2024, Research on aerodynamic optimization of hypersonic missiles][research_tianyang_jiahao_2024]
- [Tieshan and others, 2021, Application of Adaptive Fuzzy ADRC for Hypersonic Flight Vehicle][research_tieshan_zhiyao_2021]
- [Timchenko and others, 2004, aMultiobjective asynchrone parallel genetic algorithm for reentry trajectory optimization][research_timchenko_bimatov_2004]
- [TINCHER and BURNETT, 1992, A hypersonic waverider test vehicle - The logical next step][research_tincher_burnett_1992]
- [Tincher and Burnett, 1994, Hypersonic waverider test vehicle - A logical next step][research_tincher_burnett_1994]
- [Tirres and others, 2002, A Flow Quality Analysis for Future Hypersonic Vehicle Testing Invited][research_tirres_bradley_2002]
- [Tittmann and Bömmel, 1968, Simple Scheme for Hypersonic Measurements over Broad Frequency Range][research_tittmann_bommel_1968]
- [TIWARI and others, 1981, Analysis of aerothermodynamic environment of a Titan aerocapture vehicle][research_tiwari_chow_1981]
- [Tiwari and others, 1994, Computation of nonequilibrium hypersonic viscous flow about a Martian Entry Vehicle MEV][research_tiwari_thomas_1994]
- [Tobe and Grandhi, 2013, Hypersonic vehicle thermal protection system model optimization and validation with vibration tests][research_tobe_grandhi_2013]
- [Tobin and Dec, 2015, Probabilistic Design Demonstration of a Flexible Thermal Protection System for a Hypersonic Inflatable Aerodynamic Decelerator][research_tobin_dec_2015]
- [TOKARCIK and others, 1991, Computational flow predictions for hypersonic drag devices][research_tokarcik_venkatapathy_1991]
- [Tokuda and Yang, 2019, UNSTEADY STAGNATION POINT HEAT TRANSFER DUE TO ARBITRARY TIMEWISE-VARIANT FREE STREAM VELOCITY][research_tokuda_yang_2019]
- [Tokunaga and others, 2019, Stochastic re-entry trajectory analysis with uncertain initial conditions for safety assessment][research_tokunaga_sotoguchi_2019]
- [Tomar, 2014, First Principles Calculations of Interfaces in Ultra High Temperature Ceramics][research_tomar_2014]
- [Tong and Giedt, 1963, SUPERSONIC STAGNATION PNT HEAT TRANSFER TO HEMISPHERE CYLINDERS AT LOW REYNOLDS NUMBERS][research_tong_giedt_1963]
- [Tong and others, 2026, An Improved Convex Optimization Method for Power-Augmented Reentry Trajectory Optimization][research_tong_wu_2026]
- [TONG, 1965, Stagnation point nonequilibrium heat transfer][research_tong_1965]
- [Tormo and Serghides, 2007, Initial Sizing and Reentry Trajectory Design Methodologies for Dual-Mode-Propulsion Reusable Aerospace Vehicles][research_tormo_serghides_2007]
- [Tournes and Johnson, 1999, Direct-lift design strategy for longitudinal control of hypersonic aircraft using subspace stabilization][research_tournes_johnson_1999]
- [Tournes, 2013, Compendium of Flight Mechanics Formulae Applied to Hypersonic Gliders][research_tournes_2013]
- [Toussaint and others, 2023, Numerical investigation of the influence of the rarefaction degree on a waverider aerodynamic performances in super-/hypersonic regimes][research_toussaint_braeunig_2023]
- [Townend, 1979, Research and design for lifting reentry][research_townend_1979]
- [Toyama and Shimbo, 1996, Evaluation of the trajectory of vowel glide based on vector analysis][research_toyama_shimbo_1996]
- [TRACI and WILCOX, 1974, An analytical study of freestream turbulence effects on stagnation point flow and heat transfer][research_traci_wilcox_1974]
- [Tracy and Wright, 2020, Modeling the Performance of Hypersonic Boost-Glide Missiles][research_tracy_wright_2020]
- [Tracy and Wright, 2023, "Computational Fluid Dynamics Analysis of the Infrared Emission from a Generic Hypersonic Glide Vehicle" A Response][research_tracy_wright_2023]
- [Trent and others, 2007, Trajectory Planning For A Reentry Vehicle Under Failure Conditions][research_trent_doman_2007]
- [Trettel and Ezekoye, 2015, Theoretical Range and Trajectory of a Water Jet][research_trettel_ezekoye_2015]
- [Trivedi and Menezes, 2012, Measurement of yaw, pitch and side-force on a lifting model in a hypersonic shock tunnel][research_trivedi_menezes_2012]
- [TSAI and others, 1992, Computation of turbulent flow about cone-derived waverider][research_tsai_miles_1992]
- [Tsuchiya and others, 2007, Multidisciplinary Design Optimization for Hypersonic Experimental Vehicle][research_tsuchiya_takenaka_2007]
- [TSUCHIYA and others, 2007, Trajectory Optimization and Conceptual Study of Small Test Vehicles for a Hypersonic Engine Using a High-Altitude Balloon][research_tsuchiya_takenaka_2007_b]
- [TSUDA and others, 2024, Reentry Terminal Guidance Operation of Hayabusa2][research_tsuda_kikuchi_2024]
- [Tsukahara and others, 2001, Advanced thermal protection systems for reusable launch vehicles][research_tsukahara_yamao_2001]
- [Tu and others, 2006, Reentry Skipping Trajectory Optimization Using Direct Parameter Optimization Method][research_tu_yuan_2006_b]
- [Tu and Yuan, 2006, Reentry trajectory optimization using direct collocation method and nonlinear programming][research_tu_yuan_2006]
- [Tului and others, 2006, Plasma spray deposition of ultra high temperature ceramics][research_tului_marino_2006]
- [Turner and others, 2006, SHEFEX - Hypersonic Re-entry Flight Experiment Vehicle and Subsystem Design, Flight Performance and Prospects][research_turner_hoerschgen_2006]
- [TURNER, 1965, FREE-FLIGHT MODEL TECHNIQUES FOR AERODYNAMIC RESEARCH AT SUPERSONIC AND HYPERSONIC SPEEDS][research_turner_1965]
- [Turri and others, 2011, Development of a Hypersonic Aerodynamic Database for a High Angle of Attack Reentry Configuration][research_turri_klaput_2011]
- [Tuttle and others, 1994, Lift, drag and thrust measurement in a hypersonic impulse facility][research_tuttle_mee_1994]
- [Tuzlukov, 2026, Guidance on Aircraft and Missile. Trajectory Control Algorithms][research_tuzlukov_2026]
- [Türkoğlu and others, 2026, A locally validated surrogate-assisted design strategy for a hypersonic waverider under coupled aerodynamic and aerothermal constraints][research_turkoglu_donmez_2026]
- [Ueda and others, 2011, Trajectory of HAYABUSA Reentry Determined from Multisite TV Observations][research_ueda_shiba_2011]
- [Ueno and others, 2011, Experimental and Numerical Study on Aerodynamic Design of Hypersonic Vehicle][research_ueno_imamura_2011]
- [Ueno and Suzuki, 2008, CFD-Based Shape Optimization of Hypersonic Vehicles Considering Transonic Aerodynamic Performance][research_ueno_suzuki_2008]
- [UENO and SUZUKI, 2009, Two-Dimensional Shape Optimization of Hypersonic Vehicles Considering Transonic Aerodynamic Performance][research_ueno_suzuki_2009]
- [ul Islam Rizvi and others, 2015, Optimal trajectory analysis of hypersonic boost-glide waverider with heat load constraint][research_ulislamrizvi_linshu_2015]
- [Ulybyshev, 2005, Terminal Guidance Law Based on Proportional Navigation][research_ulybyshev_2005]
- [Upadhyay and others, 2019, AERODYNAMICS, STRUCTURAL CONFIGURATION AND MATERIALS OF HYPERSONIC AIRCRAFTS][research_upadhyay_kumar_2019]
- [UZAKI and others, 2017, Numerical Simulations and Wind Tunnel Experiments of Aerodynamic Characteristics on Waverider with Orbiter][research_uzaki_muta_2017]
- [V K Bhuvaneswar and others, 2025, Impact of Sustained Natural Apophyseal Gliding Technique on Neck Pain and Cervical Range of Motion in Subjects with Cervicogenic Headache][research_vkbhuvaneswar_sharifshaik_2025]
- [Vaganov and others, 2016, Methodology of investigation of ultra high temperature ceramics thermochemical stability and catalycity][research_vaganov_zhestkov_2016]
- [Vaganov and others, 2017, Laminar-turbulent transition in the vicinity of blunt leading edge of flat delta wing in hypersonic flow][research_vaganov_grachikov_2017]
- [VAHL and EDWARDS, 1978, Study of heat sink thermal protection systems for hypersonic research aircraft][research_vahl_edwards_1978]
- [Vaknin and Idan, 2026, Control Lyapunov and Barrier Function Based Analytic Controller for Air-Breathing Hypersonic Vehicles][research_vaknin_idan_2026]
- [Vala and others, 2023, Computational Analysis of Re-entry Space Vehicle at Supersonic and Hypersonic Speed][research_vala_rana_2023]
- [Valente and others, 2000, Plasma Sprayed Ultra High Temperature Ceramics for Thermal Protection Systems][research_valente_bartuli_2000]
- [Vali and Abbasi, 2022, Hypersonic drag and heat reduction mechanism of a new hybrid method of spike, multi-row discs and opposing jets aerodynamic configuration][research_vali_abbasi_2022]
- [van Brummen and others, 2015, Aerodynamic Design Analysis of the Hexafly-INT Hypersonic Glider][research_vanbrummen_pezzella_2015]
- [van den Abeelen, 2016, Staying Cool The Thermal Protection System][research_vandenabeelen_2016]
- [van der Heide and others, 2025, Multi-Mission Codesign of a Hypersonic Vehicle Leading Edge With Heat Flux Constraints][research_vanderheide_lock_2025]
- [van der Heide and others, 2026, Hypersonic Vehicle Co-Design for Multi-Stage Mission Planning][research_vanderheide_bone_2026]
- [VANMOL and ANDERSON, 1992, Heat transfer characteristics of hypersonic waveriders with an emphasis on leading edge effects][research_vanmol_andersonjr_1992]
- [Vaughn and others, 2012, Hypersonic Ground Testing Combustion Air Heater Ignition Optimization via Design of Experiments][research_vaughn_garrard_2012]
- [Vedula, 1989, Ultra High Temperature Ceramic-Ceramic Composites][research_vedula_1989]
- [Veeran and others, 2018, Ramjet Compression System for a Hypersonic Air Transportation Vehicle Combined Cycle Engine][research_veeran_pesyridis_2018]
- [Vemuri, 1982, Optimal Alpha-Beta Filtering for Tracking Reentry Vehicles from Shipboard Radars][research_vemuri_1982]
- [Vendemia and R. J, 1965, AN ENGINEERING METHOD FOR RAPID CALCULATION OF SUPERSONIC-HYPERSONIC PRESSURE DISTRIBUTIONS ON LIFTING AND NON-LIFTING POINTED BODIES OF REVOLUTION AND SEVERAL SPECIAL CASES OF BLUNT-NOSED BODIES OF REVOLUTION][research_vendemia_rj_1965]
- [Venkates and others, 2020, Parametric analysis of waverider in hypersonic flow][research_venkates_pillai_2020]
- [Vennik and others, 2017, Reproducing Non-Uniform Surface Temperature Profiles on Hypersonic Cruise Vehicles in Impulsive Wind Tunnels][research_vennik_neely_2017]
- [Venugopal and others, 1991, Automated trajectory synthesis for hypersonic vehicles using energy management and variational calculus techniques][research_venugopal_grandhi_1991]
- [Veraar, 2009, On-Ground Test Conditions to Duplicate Hypersonic Vehicle In-Flight Local Heat Flux Levels][research_veraar_2009]
- [Verma and others, 2007, Neural Dynamic Trajectory Design for Reentry Vehicles][research_verma_xu_2007]
- [Vernis and others, 2011, Accurate Skip-Entry Guidance for low to medium L/D spacecrafts return missions requiring high range capabilities][research_vernis_spreng_2011]
- [Vijayakumar and others, 2020, Thermal Design and Testing of External Protuberance of Hypersonic Carrier Vehicle Airframe][research_vijayakumar_narendar_2020]
- [Villanueva and others, 2013, Multidisciplinary Design Optimization of Small Canister-Launched Space Launch Vehicle Using Genetic Algorithm][research_villanueva_he_2013]
- [Villanueva and others, 2014, Small Solid Propellant Launch Vehicle Mixed Design Optimization Approach][research_villanueva_linshu_2014]
- [Villanueva, 2022, Maneuverable Reentry Vehicle Trajectory Optimization using Pseudospectral Method][research_villanueva_2022]
- [Villanueva, 2022, Small Modular Launch Vehicle Multidisciplinary Design Optimization][research_villanueva_2022_b]
- [Vinh and Medepalli, 1994, Optimal Thrust and Aerodynamic Controls in Hypersonic Flight][research_vinh_medepalli_1994]
- [Viotto and others, 2012, Advanced Thermal Protection and Locking System for atmospheric Re-Entry applications][research_viotto_francesconi_2012]
- [Vitiello and others, 2023, Multiple-Sliding-Surface Guidance and Control for Terminal Atmospheric Reentry and Precise Landing][research_vitiello_leonardi_2023]
- [Viviand, 1991, Similitude in Hypersonic Aerodynamics][research_viviand_1991]
- [Viviani and others, 2006, Aerothermodynamic Analysis of an Apollo-Like Reentry Vehicle][research_viviani_pezzella_2006]
- [Viviani and others, 2008, EFFECTS OF SURFACE CATALYTICITY ON COMPUTED HEAT TRANSFER OVER A REENTRY VEHICLE][research_viviani_pezzella_2008]
- [Viviani and Pezzella, 2007, Catalytic Effects on Non-Equilibrium Aerothermodynamics of a Reentry Vehicle][research_viviani_pezzella_2007]
- [Viviani and Pezzella, 2007, Influence of Surface Catalyticity on Reentry Aerothermodynamics and Heat Shield][research_viviani_pezzella_2007_b]
- [Viviani and Pezzella, 2015, Basics of Hypersonic Aerodynamics and Aerothermodynamics][research_viviani_pezzella_2015]
- [Viviani and Pezzella, 2019, Introductory Chapter Hypersonic Vehicles - Past, Present, and Future Insights][research_viviani_pezzella_2019]
- [Vlahopoulos and He, 2009, Designing the Thermal Protection System of an Apollo Type Vehicle under Uncertainty][research_vlahopoulos_he_2009]
- [Voevodenko, 1995, Calculation method for supersonic/hypersonic flows over configurations with blunt leading edges][research_voevodenko_1995]
- [Vogel and others, 2009, Hypersonic Vehicle Control Augmentation and Health Monitoring using Fads Technology][research_vogel_kelkar_2009]
- [Voland and others, 2006, X-43A Hypersonic vehicle technology development][research_voland_huebner_2006]
- [Volokhov and others, 2016, Supercomputer Simulation of Physicochemical Processes in Solid Fuel Ramjet Design Components for Hypersonic Flying Vehicle][research_volokhov_toktaliev_2016]
- [von Eggers Rudd and others, 2000, Long-Range Performance of Suboptimal Periodic Hypersonic Cruise Trajectories][research_voneggersrudd_pines_2000]
- [vonEgger and others, 1998, Improved performance of sub-optimal periodic hypersonic cruise trajectories for long range][research_vonegger_pines_1998]
- [vonEgger and Pines, 1999, Dynamic control of mission-oriented hypersonic waveriders][research_vonegger_pines_1999]
- [Vorst and Zell, 2010, Fully autonomous trajectory estimation with long-range passive RFID][research_vorst_zell_2010]
- [Votta and others, 2009, Hypersonic Low Density Aerothermodynamic of ORION Crew Exploration Vehicle CEV][research_votta_schettino_2009]
- [Votta and others, 2013, Hypersonic high altitude aerothermodynamics of a space re-entry vehicle][research_votta_schettino_2013]
- [Vu and Biezad, 1994, Direct-lift design strategy for longitudinal control of hypersonic aircraft][research_vu_biezad_1994]
- [Waechter and others, 2005, Optimizing Fuel Consumption and Reducing Thermal Load for a Hypersonic Vehicle][research_waechter_tan_2005]
- [Wagner and Dale, 1985, The Design and Testing of Pneumatic Systems for Measuring Low Pressures in Hypersonic Wind Tunnels][research_wagner_dale_1985]
- [Walberg and Birge, 2000, Terminal guidance techniques for a Mars Precision Lander][research_walberg_birge_2000]
- [WALDMAN and REINECKE, 1971, Particle trajectories, heating, and breakup in hypersonic shock layers][research_waldman_reinecke_1971]
- [Walenczykowska and others, 2024, Ballistic Missile Threat Modeling and VHF Radar Detection Performance Analysis for Tactical-Level Air Defense Simulator][research_walenczykowska_buzantowicz_2024]
- [Walker and others, 2008, The DARPA/AF Falcon Program The Hypersonic Technology Vehicle #2 HTV-2 Flight Demonstration Phase][research_walker_sherk_2008]
- [Walker and Sullivan, 2003, Sharp Refractory Composite Leading Edges on Hypersonic Vehicles][research_walker_sullivan_2003]
- [WALL, 1983, Terminal guidance][research_wall_1983]
- [Walmsley and Mailhot, 1983, On a Method of Evaluation of Performance of a Trajectory Model for Long-Range Transport of Atmospheric Pollutants][research_walmsley_mailhot_1983]
- [Wan and Chen, 2022, Prescribed Performance Control of Air-breathing Hypersonic Vehicle with Propulsion System Constraint][research_wan_chen_2022]
- [Wan and others, 2012, Dynamic Inversion-Based Control System of a Hypersonic Vehicle with Model Uncertainty][research_wan_wang_2012]
- [Wang and Bair, 2021, Operational Considerations on the American Academy of Pediatrics Guidance for K-12 School Reentry][research_wang_bair_2021]
- [Wang and Cai, 2016, Multistage Optimization Applied to the Hypersonic Inward Turning Inlet Design][research_wang_cai_2016]
- [Wang and Dong, 2013, Coevolutionary Algorithm Applied to Skip Reentry Trajectory Optimization Design][research_wang_dong_2013]
- [Wang and Gao, 2013, Numerical Study on Aerodynamic Design of Hypersonic Vehicle Forebody][research_wang_gao_2013]
- [Wang and Grant, 2016, Constrained Trajectory Optimization for Planetary Entry via Sequential Convex Programming][research_wang_grant_2016]
- [Wang and Grant, 2017, Hypersonic Trajectory Optimization by Sequential Semidefinite Programming][research_wang_grant_2017]
- [Wang and Grant, 2018, Autonomous Entry Guidance for Hypersonic Vehicles by Convex Optimization][research_wang_grant_2018]
- [Wang and Grant, 2018, Correction Near-Optimal Entry Guidance for Reference Trajectory Tracking via Convex Optimization][research_wang_grant_2018_c]
- [Wang and Grant, 2018, Near-Optimal Entry Guidance for Reference Trajectory Tracking via Convex Optimization][research_wang_grant_2018_b]
- [Wang and Grant, 2019, Improved Sequential Convex Programming Algorithms for Entry Trajectory Optimization][research_wang_grant_2019]
- [Wang and Li, 2015, A Model for Determining Strength for Embedded Elliptical Crack in Ultra-high-temperature Ceramics][research_wang_li_2015]
- [Wang and Li, 2016, A novel tracking algorithm of hypersonic target][research_wang_li_2016_c]
- [Wang and Li, 2016, Temperature Dependent Residual Stress Models for Ultra-High-Temperature Ceramics on High Temperature Oxidation][research_wang_li_2016]
- [Wang and Lin, 2016, Investigation on Aerodynamic Measurement of Hypersonic Wind Tunnel with Cable Driven Parallel Suspension System][research_wang_lin_2016]
- [Wang and Liu, 2016, Terminal sliding mode attitude controller design for a near-space hypersonic vehicle][research_wang_liu_2016]
- [Wang and Luo, 2022, Uncertainty-Based Comprehensive Optimization Design for the Thermal Protection System of Hypersonic Wing Structure][research_wang_luo_2022]
- [Wang and Meng, 2014, Skip entry trajectory tracking with consideration of the rotation of the Earth][research_wang_meng_2014]
- [Wang and Ning, 2011, Hypersonic Vehicle Attitude Single-Channel Controller Design Based on Spatially Optimal Rotation Vector][research_wang_ning_2011]
- [Wang and others, 2009, Aerodynamic characteristics research on wide-speed range waverider configuration][research_wang_ding_2009]
- [Wang and others, 2011, Influence of Blunting Manner of the Lip Highlight of Hypersonic Inlet on the Aerothermodynamic Performance][research_wang_xie_2011]
- [Wang and others, 2012, Disturbance-observer-based dynamic inversion tracking control for a hypersonic vehicle][research_wang_yang_2012]
- [Wang and others, 2012, Nonlinear Hierarchy-Structured Predictive Control System Design for Hypersonic Flight Vehicle][research_wang_liu_2012]
- [Wang and others, 2012, Peaking Free HGO Based Neural Hypersonic Flight Vehicle Control][research_wang_xu_2012]
- [Wang and others, 2012, Sizing Optimization of Lightweight Multilayer Thermal Protection Structures for Hypersonic Aircraft][research_wang_xie_2012]
- [Wang and others, 2013, A New Evolved Acceleration Reentry Guidance for Reusable Launch Vehicles][research_wang_pan_2013]
- [WANG and others, 2013, A THERMO-DAMAGE STRENGTH MODEL FOR THE SiC -DEPLETED LAYER OF ULTRA-HIGH-TEMPERATURE CERAMICS ON HIGH TEMPERATURE OXIDATION][research_wang_li_2013]
- [Wang and others, 2013, Aerodynamic and Aerothermal Performance of Power-law Shaped Leading Edge of Hypersonic Waveriders][research_wang_han_2013]
- [Wang and others, 2013, Flight control for a flexible air-breathing hypersonic vehicle based on quasi-continuous high-order sliding mode][research_wang_zong_2013]
- [Wang and others, 2013, Research of Reentry Corridor and Guidance Technology for Hypersonic Vehicle][research_wang_zhang_2013]
- [WANG and others, 2013, Tracking control for a hypersonic air-breathing vehicle with thrust vectoring nozzles][research_wang_liu_2013]
- [Wang and others, 2014, A Novel Switching Control Method for Hypersonic Flying Vehicle][research_wang_liu_2014]
- [Wang and others, 2014, Adaptive Huber-Based Filter for Hypersonic Cruise Vehicle Navigation][research_wang_xiong_2014]
- [Wang and others, 2014, Continuous high order sliding mode controller design for a flexible air-breathing hypersonic vehicle][research_wang_zong_2014]
- [Wang and others, 2014, Modeling method for gliding reentry vehicle via model migration][research_wang_li_2014]
- [Wang and others, 2014, Research on Parameter Optimization Method of an Air Vehicle Gliding Trajectory][research_wang_xu_2014]
- [Wang and others, 2014, Sliding mode controller design based on reaching law for hypersonic flight vehicle][research_wang_wu_2014]
- [Wang and others, 2014, Sliding mode decoupling control of a generic hypersonic vehicle based on parametric commands][research_wang_tang_2014]
- [Wang and others, 2015, Design and Verification for Hypersonic Aerodynamic Model with Duct of Internal and External Flow Decoupling][research_wang_song_2015]
- [Wang and others, 2015, Diving integrated guidance and control for hypersonic vehicle with impact angle constraints][research_wang_liu_2015]
- [Wang and others, 2015, Recursive terminal sliding mode control for hypersonic flight vehicle with sliding mode disturbance observer][research_wang_wu_2015]
- [Wang and others, 2015, Reentry trajectory rapid optimization for hypersonic vehicle satisfying waypoint and no-fly zone constraints][research_wang_xing_2015]
- [Wang and others, 2015, The optimal design and analysis of the IRDT system based on two-dimensional ballistic trajectory in atmosphere reentry][research_wang_hou_2015]
- [Wang and others, 2016, A new integration method based on the coupling of mutistage osculating cones waverider and Busemann inlet for hypersonic airbreathing vehicles][research_wang_wang_2016]
- [Wang and others, 2016, Adding a power integrator technique based terminal guidance law][research_wang_sun_2016]
- [Wang and others, 2016, An improved reentry trajectory planning method for Common Aero Vehicle][research_wang_zhou_2016]
- [Wang and others, 2016, Involute guidance laws with terminal impact angle constraints][research_wang_zhong_2016]
- [Wang and others, 2016, Predictor-corrector entry guidance for high-lifting hypersonic vehicles][research_wang_li_2016_b]
- [WANG and others, 2017, Aerodynamic configuration integration design of hypersonic cruise aircraft with inward-turning inlets][research_wang_cai_2017]
- [Wang and others, 2017, An Improved Online Reentry Trajectory Planning and Tracking Algorithm for Common Aero Vehicles][research_wang_zhou_2017]
- [Wang and others, 2017, Clutter suppression and moving target imaging approach for multichannel hypersonic vehicle borne radar][research_wang_cao_2017]
- [Wang and others, 2017, Control-oriented credibility assessment of air-breathing hypersonic vehicle model][research_wang_li_2017]
- [Wang and others, 2017, Finite-time attitude tracking control design for reusable launch vehicle in reentry phase based on disturbance observer][research_wang_zou_2017]
- [Wang and others, 2017, Multiobjective optimization of steady-state cruise trajectory for a hypersonic vehicle][research_wang_zhang_2017]
- [Wang and others, 2017, Numerical Investigation on Unsteady Flows with an Air-breathing Hypersonic Vehicle During its Shroud Separation][research_wang_li_2017_b]
- [Wang and others, 2017, Variable horizon reentry guidance based on predictive control and pseudospectral method for hypersonic vehicle][research_wang_feng_2017]
- [Wang and others, 2018, A Two-Stage Rapid Trajectory Optimization Algorithm for Hypersonic Entry][research_wang_cui_2018]
- [Wang and others, 2018, Design methodology of the waverider with a controllable planar shape][research_wang_liu_2018]
- [Wang and others, 2018, Fuzzy adaptive non-affine attitude tracking control for a generic hypersonic flight vehicle][research_wang_chen_2018]
- [Wang and others, 2018, Influence of the Earth Rotation on Trajectory of a Returnable Hypersonic Cruise Vehicle][research_wang_hou_2018]
- [Wang and others, 2018, Neural Extended State Observer Based Intelligent Integrated Guidance and Control for Hypersonic Flight][research_wang_peng_2018]
- [Wang and others, 2018, Self-Healing Control for Attitude System of Hypersonic Flight Vehicle With Body Flap Faults][research_wang_chen_2018_b]
- [Wang and others, 2019, Comparison of Strategies for Coupled Flow-Thermal Analysis of Thermal Protection System at Hypersonic Flight Condition][research_wang_wang_2019]
- [Wang and others, 2019, Entry Trajectory Optimization via hp Pseudospectral Convex Programming][research_wang_wang_2019_b]
- [Wang and others, 2019, Hypersonic vehicle aerodynamic design using modified sequential approximate optimization][research_wang_wu_2019]
- [Wang and others, 2019, Lowest-Technical-Merit Design Methodology of Hypersonic Cruise Vehicle][research_wang_hou_2019_b]
- [Wang and others, 2019, Mapped Chebyshev pseudospectral methods for optimal trajectory planning of differentially flat hypersonic vehicle systems][research_wang_liang_2019]
- [Wang and others, 2019, Optimal Periodic Control of Hypersonic Cruise Vehicle Trajectory Features][research_wang_hou_2019]
- [Wang and others, 2019, Short-Range Reentry Guidance With Impact Angle and Impact Velocity Constraints for Hypersonic Gliding Reentry Vehicle][research_wang_tang_2019]
- [Wang and others, 2019, The Role of Three-Dimensional Shock Wave Interaction in the Complex Hypersonic Heating][research_wang_xiang_2019]
- [Wang and others, 2019, Trajectory tracking control of hypersonic vehicle considering modeling uncertainty][research_wang_chao_2019]
- [WANG and others, 2020, Adaptive parameter estimation control of nonminimum phase hypersonic flight vehicle][research_wang_xu_2020]
- [Wang and others, 2020, Fault estimation and compensation for hypersonic flight vehicle via type-2 fuzzy technique and cuckoo search algorithm][research_wang_gong_2020]
- [Wang and others, 2021, Adaptive Attitude Estimation and Control of Hypersonic Re-Entry Vehicle with Unknown Process Noise][research_wang_wu_2021]
- [Wang and others, 2021, Aerodynamic Coefficients Modeling and Attitude Controller Design for an Air-breathing Generic Hypersonic Vehicle][research_wang_yun_2021]
- [Wang and others, 2021, Hypersonic Vehicle Aerodynamic Optimization Using Field Metamodel-Enhanced Sequential Approximate Optimization][research_wang_wu_2021_b]
- [Wang and others, 2021, Ultraviolet radiation characteristics of NO in shock layer of hypersonic vehicle][research_wang_bai_2021]
- [Wang and others, 2022, Entry Guidance Command Generation for Hypersonic Glide Vehicles Under Threats and Multiple Constraints][research_wang_tang_2022]
- [Wang and others, 2022, Integrated Thermal Protection System Design for Hypersonic Vehicle Based on New Thermal-Mechanical Method][research_wang_zhang_2022]
- [Wang and others, 2022, Linear Pseudospectral Entry Guidance Algorithm Using Differential Flat Output for High Lift-to-Drag Ratio Entry Vehicle][research_wang_yang_2022]
- [Wang and others, 2022, Pseudo-optimal discharge pressure analysis of transcritical CO2 electric vehicle heat pumps due to temperature glide][research_wang_cao_2022]
- [Wang and others, 2022, Trajectory Tracking Control for Hypersonic Vehicle Based on Differential Flatness and ADRC][research_wang_feng_2022]
- [Wang and others, 2023, A Joint Longitudinal and Lateral Guidance Scheme for Reentry Gliding Phase of Hypersonic Vehicles][research_wang_wu_2023]
- [Wang and others, 2023, Integrated Guidance and Control Design of Wide-Area Hypersonic Vehicle Based on Dynamic Inversion][research_wang_li_2023]
- [Wang and others, 2023, Numerical studies on the thermal-fluid-structure coupling analysis method of hypersonic flight vehicle][research_wang_qian_2023]
- [Wang and others, 2023, Reentry blackout reachable set footprint prediction using multi-phase trajectory optimization][research_wang_sun_2023]
- [Wang and others, 2023, Research Status of Hypersonic Flight Vehicle Control Technology Based on Composite Fault][research_wang_zhang_2023]
- [Wang and others, 2024, Autonomous Cooling Design and Temperature Control Mechanism of Hypersonic Vehicle][research_wang_ma_2024]
- [WANG and others, 2024, Collision avoidance and formation control of hypersonic glide vehicles within predefined time][research_wang_wang_2024]
- [Wang and others, 2024, Design of Time-Varying Compound Control System for Hypersonic Vehicle][research_wang_zhou_2024]
- [Wang and others, 2024, Guidance Strategy for Hypersonic Glide Vehicle with Additional Angular Error Approach][research_wang_li_2024]
- [Wang and others, 2024, Research on the cooling performance of the discontinuous transpiration surface structure for the leading edge of a hypersonic vehicle][research_wang_pan_2024]
- [Wang and others, 2024, Tube-MPC-Based Robust Control Method of Elastic Hypersonic Vehicle with Input Delay][research_wang_mi_2024]
- [Wang and others, 2025, Adaptive high order super-twisting control of hypersonic vehicle in climbing phase][research_wang_liu_2025_c]
- [Wang and others, 2025, Desired Impact Angle Identification for An Incoming Aerial Vehicle Using the Trajectory Shaping Guidance Law][research_wang_wang_2025]
- [Wang and others, 2025, Efficient initialization and optimization of translunar direct-abort trajectory under reentry constraints][research_wang_liu_2025]
- [Wang and others, 2025, Hybrid Trajectory Planning for Energy-Augmented Skip-Glide Vehicles via Hierarchical Bayesian Optimization][research_wang_li_2025]
- [Wang and others, 2025, Intention Inference Method for Reentry Glide Vehicle Based on Double-Layer BPA Fusion][research_wang_he_2025]
- [Wang and others, 2025, Learning Observer-Based Fault-Tolerant Tracking Control for Hypersonic Vehicle][research_wang_cao_2025]
- [Wang and others, 2025, Prescribed Performance Control for Hypersonic Morphing Vehicle][research_wang_li_2025_b]
- [Wang and others, 2025, Reentry Trajectory Online Planning and Guidance Method Based on TD3][research_wang_an_2025]
- [Wang and others, 2025, Robust attitude control for hypersonic reentry vehicle via composite fixed-time stable control method][research_wang_yang_2025]
- [Wang and others, 2025, Robust Incremental Learning of Approximate Dynamic Programming for Nonlinear Terminal Guidance][research_wang_cheng_2025]
- [Wang and others, 2025, Study on Trajectory Optimization Design of Multi-pulse Long-range Guided Rocket Based on Particle Swarm Optimization][research_wang_ma_2025]
- [Wang and others, 2025, Thermodynamic analysis of helium-xenon closed Brayton cycle combined with Rankine cycle power generation system for hypersonic vehicle][research_wang_liu_2025_b]
- [Wang and others, 2025, Trajectory Optimization Method for Flexible Hypersonic Vehicle Based on Pigeon-Inspired Optimization][research_wang_tang_2025]
- [Wang and others, 2025, Working medium selection for Hypersonic Vehicle Closed Brayton Cycle Energy Systems][research_wang_xue_2025]
- [Wang and others, 2026, Bi-directional Flying Wing with Orthogonal Coupling of Waverider and Flying Wing for Full-Speed Domain Applications Aerodynamic Configuration Design and Performance][research_wang_liu_2026]
- [Wang and others, 2026, COC-DAT a contrastive learning-based dilated attention temporal network for hypersonic flight vehicle fault diagnosis][research_wang_deng_2026]
- [Wang and others, 2026, Current status and prospects of guidance techniques for intercepting hypersonic glide vehicles A review][research_wang_qu_2026]
- [Wang and others, 2026, Embedded Online Trajectory Optimization Method for Hypersonic Entry][research_wang_zhang_2026]
- [Wang and others, 2026, Hypersonic Vehicle State Time-Series Prediction Based on PG-DGNet][research_wang_li_2026]
- [Wang and others, 2026, Integrated aerodynamic-trajectory optimization method considering stability constraints of air-breathing hypersonic vehicle][research_wang_cheng_2026]
- [WANG and others, 2026, Prediction of separation length for hypersonic shock wave/turbulent boundary layer interactions][research_wang_zhu_2026]
- [Wang and others, 2026, Trajectory Tracking of Glide-Phase Hypersonic Vehicles Via Nonsingular Fast Terminal Sliding Mode Control with HSMO-DO Under Multi-Source Disturbances][research_wang_liu_2026_b]
- [Wang and Ren, 2011, A new piecewise predictive guidance for the long-range reentry vehicles][research_wang_ren_2011]
- [WANG and SHIH, 1991, Numerical studies on inflatable ballute as an aerodynamic decelerator for a solid rocket motor hypersonic reentry][research_wang_shih_1991]
- [WANG and SKULSKY, 1963, Characteristics of lateral range during constant-altitude glide][research_wang_skulsky_1963]
- [Wang and Wang, 2024, Unsteady interaction and dynamic stability analysis of a two-stage-to-orbit vehicle during transverse stage separation][research_wang_wang_2024_b]
- [Wang and Wu, 2017, Adaptive non-affine control for the short-period model of a generic hypersonic flight vehicle][research_wang_wu_2017]
- [Wang and Xia, 2022, Composite Learning Control for Hypersonic Flight Vehicle Using Historical Stack][research_wang_xia_2022]
- [Wang and Xu, 2023, Robust Adaptive Control of Hypersonic Flight Vehicle With Aero-Servo-Elastic Effect][research_wang_xu_2023]
- [Wang and Yan, 2013, Research on High Accuracy Guidance Law for Reentry Vehicles][research_wang_yan_2013]
- [Wang and Yao, 2017, Optimal Skip Entry Trajectory for Lunar Return Vehicle with Trim-Flaps][research_wang_yao_2017]
- [Wang and Zhang, 2018, Terminal Guidance for a Hypersonic Vehicle with Impact Time Control][research_wang_zhang_2018]
- [Wang and Zhang, 2021, Bilevel Trajectory Optimization for Hypersonic Cruise Vehicle Using Bilevel Directed Search Domain][research_wang_zhang_2021]
- [Wang and Zuo, 2026, Separation Criterion in Hypersonic Swept Shock Wave/Turbulent Boundary Layer Interaction][research_wang_zuo_2026]
- [Wang, 1963, APPROXIMATE SOLUTIONS OF THE LATERAL MOTION OF RE-ENTRY VEHICLES DURING CONSTANT ALTITUDE GLIDE][research_wang_1963]
- [WANG, 1965, Mass injection contours for a hypersonic leading edge at an angle of attack][research_wang_1965]
- [WANG, 1965, Motion of re-entry vehicles during constant- altitude glide][research_wang_1965_b]
- [Wang, 2019, Maximum-Normal-Load Entry Trajectory Optimization for Hypersonic Glide Vehicles][research_wang_2019_b]
- [Wang, 2019, Optimal trajectories and normal load analysis of hypersonic glide vehicles via convex optimization][research_wang_2019]
- [Wang, 2022, Hypersonic vehicle attitude-tracking control using model-free deep reinforcement learning][research_wang_2022]
- [Wang, 2023, Low-Complexity Neural Back-Stepping Control with Improved Prescribed Performance for Waverider Vehicles][research_wang_2023]
- [Wanli Zhang and others, 2010, Trajectory optimization and closed-Loop guidance law design of Aero-assisted Orbital Transfer problem][research_wanlizhang_changhongwang_2010]
- [Ward and Smart, 2026, The DART Hypersonic Vehicle From Concept to Launch][research_ward_smart_2026]
- [Waszkowski and Pisani, 2025, A Review of Hypersonic Vehicle Engine Optimization][research_waszkowski_pisani_2025]
- [Watanabe and others, 1996, Aerodynamic characteristics evaluation of the Hypersonic Flight Experiment HYFLEX vehicle based on flight data][research_watanabe_ishimoto_1996]
- [Watanabe and others, 1997, Aerodynamic Characteristics Evaluation of Hypersonic Flight Experiment Vehicle Based on Flight Data][research_watanabe_ishimoto_1997]
- [Watanabe and others, 2011, Control parameter design for robot vehicle based on numerical simulation and heuristic optimization - Feed-back controller design for trajectory tracking under strict physical constraints in wide speed range][research_watanabe_ohya_2011]
- [Watanabe and others, 2016, Aerodynamic characteristics of breathing blunt nose configuration at hypersonic speeds][research_watanabe_suzuki_2016]
- [Watts, 2005, Control of a High Performance Maneuvering Reentry Vehicle Using Dynamic Inversion][research_watts_2005]
- [Way and others, 2024, Hypernetwork Based Surrogate Modeling of Hypersonic Glide Vehicle Aerothermodynamics][research_way_sescu_2024]
- [Weaver and Hunsaker, 2025, Investigating Stability of Hypersonic Conically-Derived Waverider Vehicles][research_weaver_hunsaker_2025]
- [Webb and Bettinger, 2024, Max Range Reentry Optimization in Pseudo 5DOF for Lifting Bodies with Heating and Survivability Constraints][research_webb_bettinger_2024]
- [Webb and Lu, 2016, Entry Guidance by Onboard Trajectory Planning and Tracking][research_webb_lu_2016]
- [Webb, 1999, Small Business Technology Transfer STTR Program, Phase 2, an Autonomous Gliding Vehicle for the Distributed Observation of the Littoral Environment][research_webb_1999]
- [Webb, 2000, An Autonomous Gliding Vehicle for the Distributed Observation of the Littoral Environment][research_webb_2000]
- [Wei and others, 2015, Optimization and Analysis on Trajectory with Multiple Constraints for Hypersonic Air-vehicle][research_wei_huang_2015]
- [Wei and others, 2016, A Hypersonic Cruise Flight Vehicle High-precision Control Method Using Compound Rudder Surface][research_wei_wang_2016]
- [Wei and others, 2018, Reentry Trajectory Optimization for a Hypersonic Vehicle Based on an Improved Adaptive Fireworks Algorithm][research_wei_liu_2018]
- [Wei and others, 2019, Fault-tolerant Control for Disturbed Hypersonic Vehicle Based on Tube-MPC][research_wei_hu_2019]
- [Wei and others, 2023, Detection of hypersonic weak targets by high pulse repetition frequency radar based on multi-hypothesis fuzzy-matching radon transform][research_wei_dandan_2023]
- [Wei and others, 2024, Research on the Zooming Method for Determining the Flow, Heat Transfer, and Infrared Radiation of an Air-Breathing Hypersonic Vehicle Powered by a Scramjet][research_wei_shi_2024]
- [Wei and others, 2024, WITHDRAWN Reentry vehicle fixed-time terminal guidance and attitude control with impact angle constraints][research_wei_li_2024]
- [Wei and others, 2025, Aerodynamic shape optimization for a hypersonic vehicle flying over a range of speeds][research_wei_li_2025]
- [Wei and others, 2025, Composite Actuation and Adaptive Control for Hypersonic Reentry Vehicles Mitigating Aerodynamic Ablation via Moving Mass-Aileron Integration][research_wei_cui_2025]
- [Wei and others, 2025, Parameter Analysis and Design for Coupled-Proportional Guidance-Based Glide Slope Capture of Commercial Aircraft][research_wei_kang_2025]
- [Wei and others, 2026, Online Trajectory Optimization Based on Pseudospectra Convex Optimization for Morphing Gliding Reentry Vehicles][research_wei_huang_2026]
- [Wei-feng and others, 2015, An asynchronous tracking systems modeling and its application in tracking performance analysis for hypersonic aircraft vehicle][research_weifeng_chenglin_2015]
- [Wei-wei and others, 2013, Robust optimal guidance for hypersonic glide vehicle with hinge moment constraint][research_weiwei_leping_2013]
- [WEIDNER, 1978, The application of dual fuel /JP-LH2/ for hypersonic cruise vehicles][research_weidner_1978_b]
- [Weidner, 1978, The Application of Dual Fuel JP-LH, for Hypersonic Cruise Vehicles][research_weidner_1978]
- [WEIDNER, 1980, Propulsion/airframe integration considerations for high altitude hypersonic cruise vehicles][research_weidner_1980]
- [Weidong and others, 2015, Multi-objective longitudinal trajectory optimization for hypersonic reentry glide vehicle based on PSO algorithm][research_weidong_xianlin_2015]
- [Weijie and others, 2016, Adaptive higher order sliding mode attitude control for hypersonic glide vehicles][research_weijie_hao_2016]
- [Weiland, 2014, Aerothermodynamic Data of Cruise and Acceleration Vehicles CAV][research_weiland_2014]
- [Weiland, 2014, Aerothermodynamic Data of Winged Re-entry Vehicles RV-W][research_weiland_2014_b]
- [Weilmuenster and others, 1995, Hypersonic aerodynamic characteristics of a proposed single-stage-to-orbit vehicle][research_weilmuenster_gnoffo_1995]
- [Weilmuenster and others, 1996, Hypersonic aerodynamic characteristics of a proposed single-stage-to-orbit vehicle][research_weilmuenster_gnoffo_1996]
- [Weilmuenster and others, 1996, Thermal environment of a proposed single-stage-to-orbit vehicle at hypersonic speeds][research_weilmuenster_gnoffo_1996_b]
- [Weilmuenster and others, 1997, Hypersonic Thermal Environment of a Proposed Single-Stage-to-Orbit Vehicle][research_weilmuenster_gnoffo_1997]
- [Weiwei and others, 2022, Sensitivity Analysis of Maximum Range Trajectories for Hypersonic Reentry Vehicle][research_weiwei_runde_2022]
- [Wen and others, 2014, The analysis and design of control system for unpowered skipping-glide air vehicle in near space][research_wen_wu_2014]
- [Wen and others, 2017, Hypersonic vehicle system models and adaptive turbulence compensation][research_wen_tao_2017]
- [Wenbiao and others, 2014, Method of velocity controller design for an airbreathing hypersonic cruise vehicle][research_wenbiao_dong_2014]
- [Wenbo and Qiang, 2012, The Hardware-in-the-loop Simulation on the Control System of a Small Launch Vehicle][research_wenbo_qiang_2012]
- [Wenfeng and others, 2017, Adaptive control for hypersonic vehicle based on error characteristic model][research_wenfeng_peng_2017]
- [Wenkai and others, 2017, Heat-augmented Trajectory Optimization of Hypersonic Cruise Vehicle][research_wenkai_hou_2017]
- [Wenkai and others, 2017, Optimal periodic control of hypersonic cruise vehicle][research_wenkai_zhongxi_2017]
- [Wenkai and others, 2017, Range Extension of Hypersonic Cruise Vehicle with Lowest Technical Merit][research_wenkai_hou_2017_b]
- [West and Brandis, 2018, Correction Updated Stagnation Point Aeroheating Correlations for Mars Entry][research_west_brandis_2018_b]
- [West and Brandis, 2018, Updated Stagnation Point Aeroheating Correlations for Mars Entry][research_west_brandis_2018]
- [West, 2012, Minority Report Potential Challenges in Employing Global Strike Against Violent Non-State Actors in 2035][research_west_2012]
- [Westin and others, 2003, Active control of infrared signature system implementation in a ground vehicle][research_westin_olsson_2003]
- [Weston and Cesnik, 2024, Hybrid-Fidelity Global-Local Aerothermoelastic Modeling for Path-Dependent Hypersonic Flight][research_weston_cesnik_2024]
- [Wexler and Idan, 2026, A Pointwise Minimum Norm Control Scheme for a Generic Air-Breathing Hypersonic Vehicle with State Constraints][research_wexler_idan_2026]
- [WHITE and RHIE, 1987, Numerical analysis of peak heat transfer rates for hypersonic flow over a cowl leading edge][research_white_rhie_1987]
- [WHITE, 1993, Supersonic/hypersonic flight vehicle forebody wave drag determination using an Euler-based CFD approach][research_white_1993]
- [White, 1996, Expansion corner effects on hypersonic shock wave/turbulent boundary layer interactions][research_white_1996]
- [WHITFIELD and GRIFFITH, 1963, HYPERSONIC VISCOUS DRAG EFFECTS ON BLUNT SLENDER CONES][research_whitfield_griffith_1963]
- [WHITFIELD and GRIFFITH, 1964, Hypersonic viscous drag effects on blunt slender cones][research_whitfield_griffith_1964]
- [Wibben and Furfaro, 2016, Terminal Guidance for Lunar Landing and Retargeting Using a Hybrid Control Strategy][research_wibben_furfaro_2016]
- [Wiese and others, 2013, Adaptive Control of a Generic Hypersonic Vehicle][research_wiese_annaswamy_2013]
- [Wiese and others, 2016, Sequential Loop Closure Based Adaptive Autopilot Design for a Hypersonic Vehicle][research_wiese_annaswamy_2016]
- [Wilder and Prabhu, 2019, Rough-Wall Turbulent Heat Transfer Experiments in Hypersonic Free Flight][research_wilder_prabhu_2019]
- [Wilke and others, 2000, Whole-Spacecraft Vibration Isolation on Small Launch Vehicles][research_wilke_johnson_2000]
- [Willard, 2022, Low-Density Resin-Based Ablative Heat Protection Materials][research_willard_2022]
- [Williams and others, 2024, Shape Optimization for a Parametrically-Defined Hypersonic Glide Vehicle][research_williams_bartkowicz_2024]
- [Williams and others, 2025, Integrated Guidance and Control of Generic Hypersonic Glide Vehicles Using Computational Fluid Dynamics][research_williams_bhattacharjee_2025]
- [Williams, 2019, Asymmetric arms control and strategic stability Scenarios for limiting hypersonic glide vehicles][research_williams_2019]
- [Williams, 2021, Asymmetric arms control and strategic stability Scenarios for limiting hypersonic glide vehicles][research_williams_2021]
- [Williamson and others, 2026, Simultaneous Vehicle Design and Trajectory Optimisation of a Multi-Stage Hypersonic Boost-Glide System][research_williamson_pascoe_2026]
- [Willis and others, 2009, Energetically Optimal Flight Trajectories for Short Range Gliding Animals][research_willis_bahlman_2009]
- [Willis and others, 2011, Energetically Optimal Short-Range Gliding Trajectories for Gliding Animals][research_willis_bahlman_2011]
- [Wilsdorf and Schmitz, 1962, The Observation and Interpretation of Dislocation Tangles in the Easy Glide Range of Aluminum][research_wilsdorf_schmitz_1962]
- [Wilson and Taylor, 1983, Experiences With Waverider Buoys In The Canadian Wave Climate Study][research_wilson_taylor_1983]
- [Wilson-Heid and others, 2022, Towards Laser-Based Additive Manufacturing of Ultra-High Temperature Ceramics Laser-Material Interactions of Zirconium Carbide][research_wilsonheid_griffiths_2022]
- [Windhorst and others, 1997, Minimum heating reentry trajectories for advanced hypersonic launch vehicles][research_windhorst_ardema_1997]
- [Wing and others, 2012, Non-Contact Tabletop Mechanical Testing of Ultra-High Temperature Ceramics][research_wing_gangireddy_2012]
- [WINGROVE, 1964, TRAJECTORY CONTROL PROBLEMS IN THE PLANETARY ENTRY OF MANNED VEHICLES][research_wingrove_1964]
- [Wingrove, 1966, Guidance and Control in Supercircular Atmosphere Entry][research_wingrove_1966]
- [Winn, 1993, A Large Aspect Ratio Waverider][research_winn_1993]
- [Winter and others, 2014, Remote Recession Sensing of Ablative Heat Shield Materials][research_winter_stackpoole_2014]
- [Wiseman and Lopez, 2026, AI-Enhanced Control and Aerodynamic Optimization for Hypersonic Flight][research_wiseman_lopez_2026]
- [WITTLIFF and others, 1992, A hypersonic shock tunnel test of the Aeroassist Flight Experiment AFE vehicle at high altitude test conditions][research_wittliff_oconnor_1992]
- [Wittliff and Wilson, 1961, LOW-DENSITY STAGNATION-POINT HEAT TRANSFER IN HYPERSONIC AIR FLOW][research_wittliff_wilson_1961]
- [WITTLIFF, 1983, Hypersonic shock tunnel heat transfer tests of the Space Shuttle SILTS pod configuration][research_wittliff_1983]
- [Witzeman, 2003, Magneto-Aerodynamic Hypersonics][research_witzeman_2003]
- [Wood and others, 1996, Aerothermodynamic analysis of Commercial Experiment Transporter COMET reentry capsule][research_wood_gnoffo_1996]
- [Wood and others, 2008, Allowable Trajectory Variations for Space Shuttle Orbiter Entry-Aeroheating CFD][research_wood_alter_2008]
- [WORTMAN, 1970, Three-dimensional stagnation-point heat transfer in equilibrium air flows][research_wortman_1970]
- [Wright, 2015, Research Note to Hypersonic Boost-Glide Weapons by James M. Acton Analysis of the Boost Phase of the HTV-2 Hypersonic Glider Tests][research_wright_2015]
- [Wu and Chen, 2011, Trajectory Estimation of Hypersonic Vehicle Based on Observations from Infrared Sensor on LEO Satellite][research_wu_chen_2011]
- [Wu and Guo, 2018, Neural Back-Stepping Control of Hypersonic Flight Vehicle with Actuator Fault][research_wu_guo_2018]
- [Wu and Meng, 2016, Nonlinear disturbance observer based robust backstepping control for a flexible air-breathing hypersonic vehicle][research_wu_meng_2016]
- [Wu and others, 2009, An Analytic Solution of Entry Trajectory Based on Dynamic Pressure Planning][research_wu_huang_2009]
- [Wu and others, 2009, FCMAC Based Guidance Law for Lifting Reentry Vehicles][research_wu_li_2009]
- [Wu and others, 2009, The Design of Guidance on Suborbital Reentry][research_wu_huang_2009_b]
- [Wu and others, 2012, Coupled Shape and Reentry Trajectory Optimization of Entry Vehicle for Lunar Return][research_wu_tang_2012]
- [Wu and others, 2012, Modeling and Improved Switching Control of Hypersonic Vehicle with Uncertainties][research_wu_wang_2012]
- [Wu and others, 2014, Mars entry trajectory tracking via constrained multi-model predictive control][research_wu_li_2014]
- [Wu and others, 2015, Ascent trajectory optimization of hypersonic vehicle based on improved Particle Swarm algorithm][research_wu_liu_2015]
- [Wu and others, 2015, Effect of Thrust Vectoring Technology on Taking-Off Performance of Hypersonic Vehicle][research_wu_jiang_2015]
- [Wu and others, 2018, An adaptive reentry guidance method considering the influence of blackout zone][research_wu_yao_2018]
- [Wu and others, 2018, Design and computational study of practical waverider configuration with high performance][research_wu_zhao_2018]
- [Wu and others, 2018, Fixed-Time Disturbance Observer Based Nonsingular Fast Terminal Sliding Mode Guidance with Impact Angle Constraint][research_wu_guan_2018]
- [Wu and others, 2018, Improved Chicken Swarm Optimization Method for Reentry Trajectory Optimization][research_wu_yan_2018]
- [Wu and others, 2018, Improved nonlinear dynamic inversion control for a flexible air-breathing hypersonic vehicle][research_wu_meng_2018]
- [Wu and others, 2018, Multi-disciplinary Design Optimization of Air-Breathing Hypersonic Vehicle Using Pareto Games and Evolutionary Algorithms][research_wu_tang_2018]
- [Wu and others, 2020, Full-stage Reentry Trajectory Optimization for Reusable Launch Vehicle][research_wu_tian_2020]
- [Wu and others, 2021, A hybrid particle swarm optimization-gauss pseudo method for reentry trajectory optimization of hypersonic vehicle with navigation information model][research_wu_deng_2021]
- [Wu and others, 2021, Thermal Aeroelastic Characteristics of Inflatable Reentry Vehicle Experiment IRVE in Hypersonic Flow][research_wu_zhang_2021]
- [Wu and others, 2022, Learning-Based Predictive-Corrector Reentry Guidance for Hypersonic Vehicles][research_wu_wang_2022]
- [Wu and others, 2023, Learning-based interfered fluid avoidance guidance for hypersonic reentry vehicles with multiple constraints][research_wu_wang_2023]
- [Wu and others, 2023, Prescribed Performance Control with Finite-time Convergence for Air-breathing Hypersonic Vehicle Based on Extended State Observer][research_wu_li_2023]
- [Wu and others, 2025, A switched dynamic system approach for hypersonic vehicle optimal flight control][research_wu_yuan_2025]
- [Wu and Wang, 2015, Continuous Recursive Sliding Mode Control for Hypersonic Flight Vehicle with Extended Disturbance Observer][research_wu_wang_2015]
- [Wu and Xiao, 2009, Aerodynamics Simulation of Hypersonic Waverider Vehicle][research_wu_xiao_2009]
- [Wu and Xiong, 2020, Predictor-Corrector Guidance Law Considering Multiple Terminal Constraints][research_wu_xiong_2020]
- [Wu and Yu, 2018, Robust Controller Design of Hypersonic Vehicle in Uncertainty Models][research_wu_yu_2018]
- [Wu Yanan and others, 2016, Terminal guidance with impact angle constraint based on a practical flight strategy][research_wuyanan_zhangran_2016]
- [WU, 2018, Optimization Design of High Lift to Drag Ratio Waverider Vehicle Based on Viscosity Simulation][research_wu_2018]
- [Wunderlin and others, 2018, Design Options for a South African Small-Satellite Launch Vehicle][research_wunderlin_martin_2018]
- [WURSTER, 1980, Mass reduction for advanced winged entry vehicles through integratedthermostructural-trajectory design][research_wurster_1980]
- [WURSTER, 1981, An assessment of the impact of transition on advanced winged entry vehicle thermal protection system mass][research_wurster_1981]
- [Wuxing and others, 2015, Optimization of projectile state and trajectory of reentry body based on Hp-adaptive pseudospectral method][research_wuxing_chunwang_2015]
- [Wächter and Sachs, 2006, CONSTRAINING HEAT INPUT BY TRAJECTORY OPTIMIZATION FOR MINIMUM-FUEL HYPERSONIC CRUISE][research_wachter_sachs_2006]
- [Xi and Meng, 2019, Adaptive actuator failure compensation control for hypersonic vehicle with full state constraints][research_xi_meng_2019]
- [Xia and Chen, 2015, Gradient-based Aerothermodynamic Optimization of a Hypersonic Wing Profile][research_xia_chen_2015]
- [Xia and others, 2023, Finite-horizon optimal trajectory control of near space hypersonic vehicle with multi-constraints][research_xia_bu_2023]
- [Xia and others, 2024, Research on Parallel Computation and Memory Optimization of Multi-Core Embedded DSP Technology in High Precision Missile Terminal Guidance Image Tracking Algorithm][research_xia_jing_2024]
- [Xia and others, 2025, Fractional-Order Sliding Mode Guidance Law for Hypersonic Vehicle Interception][research_xia_gao_2025]
- [Xiang and Deng, 2023, Control Parameter Design for Hypersonic Vehicle via Improved Comprehensive Learning Pigeon-Inspired Optimization][research_xiang_deng_2023]
- [Xiang and Kun, 2017, A design method for constellation of lifting reentry vehicles][research_xiang_kun_2017]
- [Xiang and others, 2022, Cross-flow transition model predictions of hypersonic transition research vehicle][research_xiang_chen_2022]
- [XIANG and others, 2025, THE THERMAL PROTECTION AND TEST VERIFICATION FOR HYPERSONIC FLIGHT VEHICLES BY FILM COOLING][research_xiang_zhang_2025]
- [Xianhong and others, 2017, Investigation of a Wide Range Adaptable Hypersonic Dual-Waverider Integrative Design Method Based on Two Different Types of 3D Inward-Turning Inlets][research_xianhong_yuan_2017]
- [XIAO and others, 1991, Numerical analysis on ablation mechanism of carbon-carbon material during reentry][research_xiao_he_1991]
- [Xiao and others, 2006, Simulation and Experiment of Hypersonic Waverider Forebody Integrated with Inlet][research_xiao_liu_2006]
- [Xiao and others, 2014, Detection Performance Analysis of Space-Based Radar to near Space Hypersonic Target][research_xiao_tan_2014]
- [Xiao and others, 2018, Hypersonic Shock Wave Interactions on a V-Shaped Blunt Leading Edge][research_xiao_li_2018]
- [Xiao and others, 2020, Low-Cost and Aerodynamics-Aim Hypersonic Flight Experiment MF-1][research_xiao_ou_2020]
- [Xiao and others, 2025, Integrated Trajectory Optimization and Morphing Control for Hypersonic Morphing Vehicles Based on Proximal Policy Optimization][research_xiao_xie_2025]
- [Xiao and Shen, 2016, Stability analysis of Trajectory Tracking Entry Guidance based on singular perturbation theory][research_xiao_shen_2016]
- [Xiao, 2009, Large Eddy Simulation and Experiment of a Hypersonic Configuration][research_xiao_2009]
- [Xiao-Qing and others, 2011, Modification impact on aerodynamic performance of hypersonic waverider][research_xiaoqing_zhongxi_2011]
- [Xiao-tian and others, 2022, Trajectory Design and Guidance Method of Multi-constraint Reentry and Glide section Based on H-V Planning and Gaussian Pseudo-Spectral Method][research_xiaotian_wei_2022]
- [Xiaoqing and others, 2010, The Hypersonic Dynamic Characteristics of Waverider][research_xiaoqing_zhongxi_2010]
- [Xiaowei and others, 2023, Real-Time Trajectory Planning for Hypersonic Vehicle with Dynamic No-Fly Zone Constraints][research_xiaowei_jia_2023]
- [Xiaoxuan and others, 2018, Model reduction of aerothermodynamic for hypersonic aerothermoelasticity based on POD and Chebyshev method][research_xiaoxuan_jinglong_2018]
- [Xie and others, 2011, A reentry trajectory planning approach satisfying waypoint and no-fly zone constraints][research_xie_liu_2011]
- [Xie and others, 2012, A Novel Migrant PSO Algorithm for Vehicle Reentry Trajectory Optimization][research_xie_wang_2012]
- [Xie and others, 2013, A New Strategy of Guidance Command Generation for Re-entry Vehicle][research_xie_wang_2013_b]
- [Xie and others, 2013, Thermomechanical optimization of lightweight thermal protection system under aerodynamic heating][research_xie_wang_2013]
- [Xie and others, 2015, Trajectory Planning for Reentry Maneuverable Ballistic Missiles][research_xie_pan_2015]
- [Xie and others, 2017, The Computing of Dynamic Derivatives of Hypersonic Lift Body Based on Time Spectral Method][research_xie_yang_2017]
- [Xie and others, 2020, Effect of thermal protection system size on aerothermoelastic stability of the hypersonic panel][research_xie_dong_2020]
- [Xie and others, 2021, Sequential Convex Programming using Hybrid Trust Region Method for Reentry Trajectory Planning][research_xie_lin_2021]
- [Xie and others, 2023, Rapid Adaptive Planning of Glide Trajectory Based on Inverse Dynamics][research_xie_peng_2023]
- [Xie and others, 2023, Sequential Convex Programming for Reentry Trajectory with Piecewise Constant Bank Angle Profile Constraint][research_xie_zhang_2023]
- [Xie and others, 2024, Aerodynamic Analysis of Hypersonic Gliding Vehicles with Wide-Speed Range Based on the Cuspidal Waverider][research_xie_zhao_2024]
- [Xie and others, 2024, An Analytical Reentry Solution Based Online Time-Coordinated A* Path Planning Method for Hypersonic Gliding Vehicles Considering No-Fly-Zone Constraint][research_xie_wei_2024]
- [Xie and others, 2025, Rapid Trajectory Planning Considering Uncertainties for Hypersonic Glide Vehicles][research_xie_zhang_2025]
- [Xie and Wang, 2012, Adaptive proportional guidance law for reentry vehicles with impact angle and terminal velocity constraints][research_xie_wang_2012_c]
- [Xie and Wang, 2012, Optimal Guidance Law Design for Reentry Vehicles with Terminal Velocity and Angle Constraints][research_xie_wang_2012_b]
- [Xin and others, 2026, Enhanced thermal protection performance of a near-space vehicle rudder system enabled by a micro-arc oxidation coating][research_xin_xu_2026]
- [Xin Wang and others, 2008, Attitude Control of Unmanned Hypersonic Test Vehicle][research_xinwang_dongzhufeng_2008]
- [Xin Wang and Shijie Sun, 2010, Uncertainty disturbance modeling and effect on hypersonic test vehicle][research_xinwang_shijiesun_2010]
- [Xingling and Honglun, 2014, Sliding mode based trajectory linearization control for hypersonic reentry vehicle via extended disturbance observer][research_xingling_honglun_2014]
- [Xinguo and others, 2024, Re-entry Trajectory Planning Algorithm for Reusable Launch Vehicle Based on RRT *][research_xinguo_ting_2024]
- [Xinyu and others, 2025, Reentry Guidance Method for Reusable Launch Vehicles Based on GRU-DDPG][research_xinyu_kelong_2025]
- [Xiong and Lele, 2003, Simulation and Analysis of Stagnation Point Heat Transfer Under Free-Stream Turbulence][research_xiong_lele_2003]
- [Xiong and Lele, 2004, Stagnation Point Flow and Heat Transfer Under Free-Stream Turbulence][research_xiong_lele_2004]
- [Xiong and others, 2014, Improved reference trajectory generation method in reentry guidance][research_xiong_chen_2014]
- [Xiong and others, 2021, Design and evaluation of a conical hypersonic vehicle with an overturned aerodynamic layout][research_xiong_fan_2021]
- [Xiong Luo and others, 2008, Virtual simulation framework of intelligent autonomous control for hypersonic vehicle][research_xiongluo_zengqisun_2008]
- [Xu and Cai, 2011, High altitude aero-optic imaging deviation prediction for a hypersonic flying vehicle][research_xu_cai_2011]
- [Xu and Cui, 2015, Robust Trajectory Design Scheme under Uncertainties and Perturbations for Mars Entry Vehicle][research_xu_cui_2015]
- [Xu and Fang, 2022, Numerical Investigation of Drag and Heat Flux Reduction in Hypersonic Vehicle with Aerospike][research_xu_fang_2022_b]
- [XU and HUANG, 2018, Attitude Stabilization of Hypersonic Vehicle under Actuator Faults and Saturation][research_xu_huang_2018]
- [Xu and Lan, 2018, Entry Trajectory Reconstruction for an Unpowered Reusable Launch Vehicle Under the Change of Landing Field][research_xu_lan_2018]
- [Xu and others, 2004, Adaptive Sliding Mode Control Design for a Hypersonic Flight Vehicle][research_xu_mirmirani_2004]
- [Xu and others, 2011, Infrared imaging Maneuvering Reentry Vehicle counter target lost algorithm using Modified Gain Extended Kalman Filter][research_xu_zhu_2011]
- [Xu and others, 2011, Notice of Retraction Applied Study on Consequence Assessment of Hypothetical Radioactive Releases Using Long-Range Trajectory and Dispersion Models][research_xu_yao_2011]
- [Xu and others, 2011, Quasi-equilibrium glide auto-adaptive entry guidance based on ideology of predictor-corrector][research_xu_liu_2011]
- [Xu and others, 2012, Adaptive Kriging controller design for hypersonic flight vehicle via back-stepping][research_xu_sun_2012]
- [Xu and others, 2012, Direct neural discrete control of hypersonic flight vehicle][research_xu_wang_2012]
- [Xu and others, 2012, Quasi-equilibrium glide adaptive guidance for hypersonic vehicles][research_xu_chen_2012]
- [Xu and others, 2012, The Applications of Improved Genetic Algorithm on Hypersonic Vehicle Trajectory Optimization][research_xu_li_2012]
- [Xu and others, 2013, A hypersonic lift mechanism with decoupled lift and drag surfaces][research_xu_xu_2013]
- [Xu and others, 2013, Direct neural control of hypersonic flight vehicles with prediction model in discrete time][research_xu_wang_2013]
- [Xu and others, 2013, Neural control of hypersonic flight vehicle model via time-scale decomposition with throttle setting constraint][research_xu_shi_2013]
- [Xu and others, 2015, Research on motion model for the hypersonic boost-glide aircraft][research_xu_wu_2015]
- [Xu and others, 2017, DOB-Based Neural Control of Flexible Hypersonic Flight Vehicle Considering Wind Effects][research_xu_wang_2017]
- [Xu and others, 2017, Four-Loop Feedback Control System with Integrator Design for Hypersonic Cruise Missile][research_xu_yu_2017]
- [Xu and others, 2018, Preparation of carbon/carbon-ultra high temperature ceramics composites with ultra high temperature ceramics coating][research_xu_cheng_2018]
- [Xu and others, 2019, Barrier Lyapunov Function Based Learning Control of Hypersonic Flight Vehicle With AOA Constraint and Actuator Faults][research_xu_shi_2019]
- [Xu and others, 2020, Application and effect analysis of plasma stealth technology in hypersonic vehicle][research_xu_zhang_2020]
- [xu and others, 2021, Constrained reentry trajectory optimization based on improved particle swarm optimization algorithm][research_xu_zhou_2021]
- [Xu and others, 2021, Study on the Influence of Angle of Attack on the Aerodynamic Performance of Aerospike Structure of Hypersonic Vehicle][research_xu_fang_2021]
- [Xu and others, 2022, An Adaptive Kalman Filter for Near Space Hypersonic Vehicle Tracking][research_xu_wang_2022]
- [Xu and others, 2022, Numerical Study on Aerodynamic Performance of Hypersonic Vehicle with Aerospikes][research_xu_fang_2022]
- [Xu and others, 2022, Reentry Attitude Control of Hypersonic Vehicle based on Sliding Mode Active Disturbance Rejection][research_xu_dong_2022]
- [Xu and others, 2023, Analytic Time Reentry Cooperative Guidance for Multi-Hypersonic Glide Vehicles][research_xu_cai_2023]
- [Xu and others, 2023, Hypersonic Vehicle Tracking Algorithm Based on Virtual Radar Constructed by Artificial Intelligence][research_xu_zhu_2023]
- [Xu and others, 2023, Predefined-Time Hierarchical Coordinated Neural Control for Hypersonic Reentry Vehicle][research_xu_shou_2023]
- [Xu and others, 2025, Design and Analysis of Bump Configuration in a Hypersonic Inlet][research_xu_peng_2025]
- [Xu and others, 2025, Error shaping strategy-based multi-constrained integrated guidance and control for hypersonic vehicle in dive phase][research_xu_liao_2025]
- [Xu and others, 2025, Imitation-Reinforcement Learning Penetration Strategy for Hypersonic Vehicle in Gliding Phase][research_xu_guan_2025]
- [XU and others, 2026, A self-learning refined model and tracking for near space hypersonic vehicle by space-based radar][research_xu_pan_2026]
- [Xu and others, 2026, Intelligent Online Identification of Aerodynamic Parameters for Hypersonic Glide Vehicle][research_xu_ma_2026]
- [Xu and Zhang, 2015, Neural discrete back-stepping control of hypersonic flight vehicle with equivalent prediction model][research_xu_zhang_2015]
- [Xu Mingliang and others, 2010, Study on guidance approaches of hypersonic glide-cruise vehicle during cruise and attack phases][research_xumingliang_liuluhua_2010]
- [Xu, 2015, Robust adaptive neural control of flexible hypersonic flight vehicle with dead-zone input nonlinearity][research_xu_2015]
- [Xu, 2022, Research On Parallel Calculation Technology of Multiple Independently Targeted Reentry Vehicle's Ballistic Trajectory][research_xu_2022]
- [Xu, 2023, Active Disturbance Rejection Attitude Control of Underactuated Hypersonic Vehicle][research_xu_2023]
- [Xudong Liu and others, 2016, Entry trajectory optimization for hypersonic vehicle based on time-scales separation guidance with waterweeds algorithm][research_xudongliu_lincheng_2016]
- [Xue and Haibin, 2017, Aerodynamic parameter identification of hypersonic vehicle via Pigeon-inspired optimization][research_xue_haibin_2017]
- [Xue and Lu, 2010, Constrained Predictor-Corrector Entry Guidance][research_xue_lu_2010]
- [Xue and others, 2017, Numerical Investigation of Drag Increase due to Roughness Elements in Hypersonic Boundary Layers][research_xue_wang_2017]
- [Xue and others, 2018, A maneuvering penetration strategy via integrated flight/propulsion guidance and control method for air-breathing hypersonic vehicle][research_xue_guodong_2018]
- [Xue and others, 2021, A study on the RR-to-MR transition of shock wave reflections near the leading edge in hypersonic flows][research_xue_wang_2021]
- [Xue and others, 2023, A Distributed Formation Guidance Law for Lifting Body Vehicle][research_xue_xin_2023]
- [Xue and others, 2023, An adaptive multivariate Student's t-process recursive method for hypersonic glide vehicle trajectory prediction][research_xue_huang_2023]
- [Xue and others, 2025, Research on the performance of an integrated active cooling and propulsion system for hypersonic glide vehicles][research_xue_wang_2025]
- [Xue and others, 2026, Design and thermomechanical performance study of active-passive coupled thermal protection structures for hypersonic glide vehicles][research_xue_li_2026]
- [Xuebao and others, 2023, Online Fast Sliding Mode Controller for Air-Breathing Hypersonic Vehicle with Inlet Constraint][research_xuebao_xiaokui_2023]
- [Xuguo and others, 2017, Research on Aeroheating of Hypersonic Reentry Vehicle Base Flow Fields][research_xuguo_yongtao_2017]
- [Xuzhao and others, 2012, Osculating Inward turning Cone Waverider/Inlet OICWI Design Methods and Experimental Study][research_xuzhao_jialing_2012]
- [Yadhukulakrishnan and others, 2013, Spark plasma sintering of graphene reinforced zirconium diboride ultra-high temperature ceramic composites][research_yadhukulakrishnan_karumuri_2013]
- [Yakubayev and others, 2026, Towards Selection of a Hypersonic Glide Vehicle Aerothermal Common Research Model Configuration][research_yakubayev_gschwend_2026]
- [Yamada, 2022, Best Estimated Trajectory and Attitude Motion of Hayabusa2 SRC Reentry Flight][research_yamada_2022]
- [Yamada, 2022, Correction Best Estimated Trajectory and Attitude Motion of Hayabusa2 SRC Reentry Flight][research_yamada_2022_b]
- [YAMAMOTO and others, 1989, Numerical simulation of hypersonic viscous perfect gas flow for the aerothermodynamic design of space planes at low angles of attack][research_yamamoto_arakawa_1989]
- [Yamamoto and others, 1995, Hypersonic CFD analysis for the aerothermodynamic design of HOPE][research_yamamoto_wada_1995]
- [Yamasaki and Balakrishnan, 2012, Terminal intercept guidance and autopilot for aircraft defense against an attacking missile via 3D sliding mode approach][research_yamasaki_balakrishnan_2012]
- [Yan and Hexi, 2025, Guidance and Control Based on Nonsingular Terminal Sliding Mode Control for Asteroid Landing with a Flexible Lander][research_yan_hexi_2025]
- [Yan and others, 2008, Estimation the Mission Effectiveness of Hypersonic Cruise Missile in Conceptual Design][research_yan_pan_2008]
- [Yan and others, 2014, Analysis of optimal initial glide conditions for hypersonic glide vehicles][research_yan_lyu_2014]
- [Yan and others, 2017, A small-gain method for integrated guidance and control in terminal phase of reentry][research_yan_tan_2017]
- [Yan and others, 2017, The dual decoupling fusion control design for the lateral motion of hypersonic glide vehicle][research_yan_fan_2017]
- [YAN and others, 2023, Robust convex optimization for reentry glide trajectory using polynomial chaos][research_yan_wang_2023]
- [Yan and others, 2024, Fault-Tolerant Integrated Guidance and Control Design for Hypersonic Vehicle Based on ADRC][research_yan_wang_2024]
- [Yan and Wang, 2012, Three-dimensional Trajectory Planning Method for Hypersonic Glide Vehicle][research_yan_wang_2012]
- [Yan and Zhang, 2023, Active Disturbance Rejection Control of Hypersonic Vehicle Based on Q-Learning Algorithm][research_yan_zhang_2023]
- [Yan Binbin and others, 2009, Fuzzy CMAC control design for an airbreathing hypersonic cruise vehicle][research_yanbinbin_lucunkan_2009]
- [Yan, 2014, Adaptive Pole Assignment Control for Generic Elastic Hypersonic Vehicle][research_yan_2014]
- [Yang and Li, 2023, Nonlinearly Parametrized Modeling and Adaptive Control for a Generic Hypersonic Vehicle][research_yang_li_2023]
- [Yang and Liu, 2017, A wall grid scale criterion for hypersonic aerodynamic heating calculation][research_yang_liu_2017]
- [Yang and Meng, 2012, The Reentry Trajectory Optimization for Lifting Vehicle by Using Gauss Pseudospectral Method][research_yang_meng_2012]
- [YANG and others, 1987, Aerodynamic design modification of a hypersonic wind tunnel nozzle by CSCM with high order accuracy][research_yang_lombard_1987]
- [Yang and others, 2008, Research progress on thermal protection materials and structures of hypersonic vehicles][research_yang_yang_2008]
- [Yang and others, 2013, Backstepping Based Type-2 Adaptive Fuzzy Control for a Generic Hypersonic Flight Vehicle][research_yang_yuan_2013]
- [Yang and others, 2014, Approximate Prediction for Aerodynamic Heating and Design for Leading-edge Bluntness on Hypersonic Vehicles][research_yang_duan_2014]
- [Yang and others, 2014, Flight Dynamic Characteristic Analysis of a Generic Airbreathing Hypersonic Vehicle][research_yang_yu_2014]
- [Yang and others, 2014, Research on SINS in application of reentry navigation for lifting reentry vehicles][research_yang_kong_2014]
- [Yang and others, 2016, Steady Glide Dynamic Modeling and Trajectory Optimization for High Lift-to-Drag Ratio Reentry Vehicle][research_yang_chen_2016]
- [Yang and others, 2017, Active disturbance rejection attitude control for a hypersonic reentry vehicle with actuator saturation][research_yang_yu_2017]
- [Yang and others, 2017, Practical Guidance Design for the Boost Phase of Hypersonic Vehicle Subject to Terminal Scramjet Transition Constraints][research_yang_zhu_2017]
- [Yang and others, 2017, Predictor-corrector reentry guidance based on online model identification][research_yang_lin_2017]
- [Yang and others, 2017, The application of SRCQMMSPF in ballistic reentry target trajectory tracking][research_yang_zheng_2017]
- [Yang and others, 2018, The Application of Improved Particle Filtering in Ballistic Reentry Target Trajectory Tracking][research_yang_hu_2018]
- [Yang and others, 2019, Fault-Tolerant Control Based on LPV-Robust Model Predictive Control for Hypersonic Vehicle][research_yang_lv_2019]
- [Yang and others, 2022, Fault-Tolerant Control for Hypersonic Reentry Vehicles with RCS][research_yang_wang_2022]
- [Yang and others, 2022, Investigation into The Influences of Turbulence Models on Heating Prediction of Hypersonic Inflatable Aerodynamic Decelerator][research_yang_ji_2022]
- [Yang and others, 2023, Cooperative Trajectory Shaping Guidance Law for Multiple Missiles][research_yang_fang_2023]
- [Yang and others, 2023, Design Consideration on High-power Generation Technology for Hypersonic Vehicle][research_yang_wang_2023]
- [Yang and others, 2023, Robust Multiobjective Trajectory Optimization for Hypersonic Telescopic Wing Morphing Aircraft][research_yang_chao_2023]
- [Yang and others, 2024, Analytical time-coordinated entry guidance for multi-hypersonic vehicles within three-dimensional corridor][research_yang_liang_2024]
- [Yang and others, 2024, Development of combined hypersonic test facility for aerothermodynamic testing][research_yang_choi_2024]
- [Yang and others, 2025, Application of Rapid Calculation for Infrared Radiation Characteristics in Hypersonic Vehicle][research_yang_yang_2025]
- [Yang and others, 2025, Landing Footprint Prediction for Hypersonic Morphing Vehicle A Generative Adversarial Network-Based Method][research_yang_liu_2025]
- [Yang and others, 2025, Optimal Midcourse Guidance Law and Cooperative Encirclement Hunting of Hypersonic Missile Group on Radau Pseudo-spectral Method][research_yang_song_2025]
- [Yang and others, 2026, Reentry Vehicle Intelligent Trajectory Convex Optimization Method Based on Terminal Time Prediction][research_yang_tian_2026]
- [Yang and others, 2026, Trajectory optimization for auxiliary power unit operation of an extender range electric vehicle][research_yang_tian_2026_b]
- [Yang and Qi, 2016, Reentry trajectory optimization for hypersonic vehicle based on improved mesh refinement techniques][research_yang_qi_2016]
- [Yang and Sun, 2011, Reentry Trajectory Optimization of Airbreathing Hypersonic Vehicles Based on Gauss Pseudospectral Method][research_yang_sun_2011]
- [Yang and Wang, 2012, Trajectory Tracking Control of Hypersonic Reentry Vehicle Based on Adaptive Fuzzy System][research_yang_wang_2012]
- [Yang and Wang, 2015, Reentry Trajectory Optimization Based on Time-Domain Improved Particle Swarm Optimization][research_yang_wang_2015]
- [Yang and Wang, 2021, High-Order Disturbance Observer-Based Attitude Control with Prescribed Performance for Hypersonic Vehicle][research_yang_wang_2021]
- [Yang and Zhang, 2024, Aero-optical effects of a hypersonic vehicle based on the refractive index step ray tracing method][research_yang_zhang_2024]
- [YANG Hong and others, 2016, Detectability of airship infrared detection system to hypersonic vehicle][research_yanghong_zhangyasheng_2016]
- [Yang, 2025, Comprehensive Review of Aerodynamic Optimization for Wide-Speed-Range Hypersonic Vehicles][research_yang_2025]
- [Yankui and others, 2005, The Design of Waverider Configuration with High Lift-Drag Ratio][research_yankui_dongjun_2005]
- [Yankui and others, 2007, Design of Waverider Configuration with High Lift-Drag Ratio][research_yankui_shuifeng_2007]
- [Yanli and others, 2016, Self-organizing functional-link-network-based control for hypersonic glide vehicles][research_yanli_dongyang_2016]
- [Yanli Du and others, 2008, Attitude tracking of a near-space hypersonic vehicle using robust predictive control][research_yanlidu_qingxianwu_2008]
- [Yao and others, 2013, A Kind of Adaptive Backstepping Sliding Model Controller Design for Hypersonic Reentry Vehicle][research_yao_wang_2013]
- [Yao and others, 2017, Preliminary Study of Aerodynamic Performance for Waverider-based Hypersonic Vehicles with Dorsal Mounted Engines][research_yao_cui_2017]
- [Yao and others, 2023, High-precision reconstruction of the heat flux field by a scanning electron beam for thermal assessment of a hypersonic vehicle][research_yao_wang_2023]
- [Yao and others, 2023, Sliding Mode Formation Control for Multiple Hypersonic Glide Vehicles][research_yao_hu_2023]
- [Yao and others, 2025, Distributed integrated design for optimity and safety of hypersonic flight vehicle swarm][research_yao_liang_2025]
- [Yao and Wang, 2013, Adaptive backstepping sliding model control of hypersonic vehicle based on CMAC and dynamic surface][research_yao_wang_2013_b]
- [Yao and Xia, 2023, Predictor-Corrector Guidance for a Hypersonic Morphing Vehicle][research_yao_xia_2023]
- [Yao and Xia, 2024, Finite-Time Convergence Guidance Law for Hypersonic Morphing Vehicle][research_yao_xia_2024]
- [Yaosheng, 2018, Sliding Mode Variable Structure Controller for PSO-RBF Hypersonic Vehicle][research_yaosheng_2018]
- [Yassin and others, 2025, On the Impact of Surface Thermal Conditions on Aero-heating to Hypersonic Vehicle][research_yassin_ahmed_2025]
- [Yates, 1967, An Experimental and Analytical Evaluation of the Thermal Behavior of Liquid Hydrogen in a Tank Designed and Insulated for Use in a Hypersonic Vehicle][research_yates_1967]
- [Yatsukhno, 2017, Numerical simulation of the flow over a hypersonic waverider using the method for splitting into physical processes][research_yatsukhno_2017]
- [Yatsukhno, 2021, Waverider Surface Heating Estimationby Effective Length Technique][research_yatsukhno_2021]
- [Ye and Jiang, 2020, Adaptive switching control for hypersonic vehicle with uncertain control direction][research_ye_jiang_2020]
- [Ye and others, 2000, Effect of sidewall leading edge sweep direction on performance of a hypersonic 3-D inlet][research_ye_huque_2000]
- [Ye and others, 2016, Aerodynamic optimization for hypersonic airfoil design based on local piston theory][research_ye_zhang_2016]
- [Ye and others, 2017, Control-oriented modeling and adaptive backstepping control for a nonminimum phase hypersonic vehicle][research_ye_zong_2017]
- [Ye and others, 2017, Reentry guidance method based on predictive control for hypersonic vehicle][research_ye_chaofang_2017]
- [Ye and others, 2022, Hypersonic Glide Target Tracking Based on Improved Square Root UKF][research_ye_tu_2022]
- [Ye and others, 2022, Initial value selection strategy of glide trajectory based on Legendre pseudospectral method][research_ye_liu_2022]
- [Ye and others, 2024, Multiscale coupling simulation of surface catalytic effect on hypersonic aerothermodynamic environment][research_ye_zhao_2024]
- [Ye and others, 2025, A Novel Approach for Optimizing the Trajectory of Glide-Guided Projectiles Using the GWO-hpRPM Algorithm][research_ye_guan_2025]
- [Ye, 2015, Wide input voltage range boost/inverting/SEPIC controller works down to an input voltage of 1.6V][research_ye_2015]
- [Yee and Koo, 2021, Withdrawal Review of Ablative Polymer Nanocomposites and Ultra High Temperature Ceramics for Hypersonic Applications][research_yee_koo_2021_b]
- [Yee and Koo, 2021, Withdrawn Review of Ablative Polymer Nanocomposites and Ultra High Temperature Ceramics for Hypersonic Applications][research_yee_koo_2021]
- [Yen, 1986, Thermal nonequilibrium hypersonic shock layer near the stagnation point][research_yen_1986]
- [Yeo and Sng, 1980, Numerical Solution of the Constrained Re-entry Vehicle Trajectory Problem via Quasilinearization][research_yeo_sng_1980]
- [Yi and others, 2021, Adaptive Terminal Sliding Mode Guidance Law with Impact Angle Constraint][research_yi_li_2021]
- [Yihan Li and others, 2020, Radiative transmission property of infrared window in hypersonic vehicle][research_yihanli_haiyanghu_2020]
- [Yin and others, 2017, Numerical and Experimental Studies of the Support Interference in the Force Prediction of an Airbreathing Hypersonic Flight Vehicle][research_yin_qin_2017]
- [Yin and others, 2025, Aerodynamic shape optimization of hypersonic vehicle based on improved class-shape-transformation method][research_yin_he_2025]
- [Yin and others, 2026, Efficient long-range ship trajectory forecasting via selective state space modeling and hybrid AIS fusion][research_yin_yu_2026]
- [Ying and others, 2018, Damage-mitigating control of hypersonic flight vehicle based on prescribed performance][research_ying_wang_2018]
- [Yiyin Wei and others, 2016, Reference command tracking of a hypersonic vehicle with elastic effects][research_yiyinwei_yaochen_2016]
- [Yizhen Meng and others, 2016, Fault diagnosis and fault-tolerant predictive control for Hypersonic Vehicle IEEE CGNCC][research_yizhenmeng_binjiang_2016]
- [Yong and others, 2017, An Improved Predictor-corrector Reentry Guidance for Low L/D Spacecraft][research_yong_li_2017]
- [Yongfeng Xie and Shuo Tang, 2010, Rapid prototyping of reentry vehicle navigation and guidance systems][research_yongfengxie_shuotang_2010]
- [Yoon and Ahn, 2016, Trajectory Optimization of a Launch Vehicle with Explicit Instantaneous Impact Point Constraints for Various Range Safety Requirements][research_yoon_ahn_2016]
- [Yoon and Rasmussen, 1996, Aerodynamic forces of elliptic-cone derived waveriders at hypersonic velocities][research_yoon_rasmussen_1996]
- [Yoon and Suzuki, 2024, Effect of Mass Flow Rate on Drag Reduction with Counter-Flow Jet in Laminar Hypersonic Flow at High Reynolds Number][research_yoon_suzuki_2024]
- [YORK and PASTRICK, 1976, Optimal terminal guidance with constraints at final time][research_york_pastrick_1976]
- [Yost and others, 2019, Performance of a Generic X-51 Waverider Thrust, Drag, and Trim Computed Using the MASIV Reduced Order Model][research_yost_choi_2019]
- [You and Liang, 2009, Design concept of three-dimensional section controllable internal waverider hypersonic inlet][research_you_liang_2009]
- [You and Liang, 2009, Low Mach Number Wind Tunnel Tests of Internal Waverider Hypersonic Inlet][research_you_liang_2009_c]
- [You and Liang, 2009, Numerical Research of Internal Waverider Hypersonic Inlet in Non-Design Statuses][research_you_liang_2009_b]
- [You and others, 2009, Dual Waverider Concept for the Integration of Hypersonic Inward-Turning Inlet and Airframe Forebody][research_you_zhu_2009]
- [You and others, 2009, High Enthalpy Wind Tunnel Tests of Three-Dimensional Section Controllable Internal Waverider Hypersonic Inlet][research_you_liang_2009_d]
- [YOUNG and others, 1972, Hypersonic Transitional and Turbulent Flow Studies on a Lifting Entry Vehicle][research_young_reda_1972]
- [YOUNG, 1966, Aerodynamics of Hypersonic Flight][research_young_1966]
- [YOUNG, 1969, Electronic Terminal Guidance for All-Weather VTOL Operations][research_young_1969]
- [Youssef and Chowdhry, 2004, Hypersonic Global Reach Trajectory Optimization][research_youssef_chowdhry_2004]
- [Youssef and others, 2003, Hypersonic Skipping Trajectory][research_youssef_chowdhry_2003]
- [Youssef and others, 2008, Adaptive Reconfigurable Dynamic Inversion Control for a Hypersonic Cruise Vehicle][research_youssef_reiman_2008]
- [Youssef and others, 2009, Robust Adaptive Reconfigurable Control for a Hypersonic Cruise Vehicle][research_youssef_reiman_2009]
- [Yu and Chen, 2011, Guidance Scheme for Glide Range Maximization of a Hypersonic Vehicle][research_yu_chen_2011]
- [Yu and others, 2013, Dynamic Modeling and Numerical Simulation of Acoustic-Thermal-Fluid Coupling for Hypersonic Vehicle Fatigue Test][research_yu_zhong_2013]
- [Yu and others, 2014, Numerical Studies of Acoustic and Thermal Coupling in Sonic Fatigue Tests for Hypersonic Vehicle][research_yu_zhong_2014]
- [Yu and others, 2014, Robust tracking control for the hypersonic flight vehicle via backstepping method][research_yu_zhang_2014]
- [Yu and others, 2015, An Improved Internal-Waverider-Inlet with High External-Compression for Ramjet Engine][research_yu_huang_2015]
- [Yu and others, 2015, Research on SINS/CNS Gaussian Particle Filter Integrated Navigation Algorithm for Hypersonic Vehicle][research_yu_xu_2015]
- [Yu and others, 2016, An Observability-Based Trajectory Optimization Considering Disturbance for Atmospheric Entry][research_yu_zhao_2016]
- [Yu and others, 2016, Omnidirectional autonomous entry guidance based on 3-D analytical glide formulas][research_yu_chen_2016]
- [Yu and others, 2017, Finite-time decoupling direct control for hypersonic reentry vehicle with multiple disturbances via second-order ADRC][research_yu_wang_2017]
- [Yu and others, 2019, Configuration optimization of the tandem cooling-compression system for a novel precooled hypersonic airbreathing engine][research_yu_wang_2019]
- [Yu and others, 2019, Fault-tolerant control for over-actuated hypersonic reentry vehicle subject to multiple disturbances and actuator faults][research_yu_wang_2019_b]
- [Yu and others, 2019, Marginal tracking algorithm for hypersonic reentry gliding vehicle][research_yu_tan_2019]
- [Yu and others, 2020, Adaptive backstepping control for air-breathing hypersonic vehicle subject to mismatched uncertainties][research_yu_jiang_2020]
- [Yu and others, 2021, Intelligent Control of a Hypersonic Flight Vehicle Based on Active Disturbance Rejection Control][research_yu_ao_2021]
- [Yu and others, 2022, Aerodynamic Characteristics of Supersonic Rocket-Sled Involving Waverider Geometry][research_yu_wang_2022]
- [Yu and others, 2022, Numerical simulation of thermochemical non-equilibrium flow-field characteristics around a hypersonic atmospheric reentry vehicle][research_yu_qiu_2022]
- [Yu and others, 2022, Real-time dynamic optimized band detection method for hypersonic glide vehicle][research_yu_ni_2022]
- [Yu and others, 2025, Design and adaptability study of a novel internal waverider inlet for random hypersonic non-uniform inflow][research_yu_hao_2025]
- [Yu and others, 2025, Numerical analysis on the active cooling characteristics for a hypersonic vehicle leading edge and coolant distribution strategy][research_yu_guo_2025]
- [Yu and others, 2025, Reliability analysis of hypersonic vehicles under aerodynamic heating][research_yu_wang_2025]
- [Yu and others, 2025, Trajectory Prediction and Cooperative Interception Strategy for Maneuverable Hypersonic Target][research_yu_li_2025]
- [Yu and others, 2026, Analytical solution for three-dimensional skip re-entry trajectory][research_yu_chen_2026]
- [Yu and others, 2026, Interfered fluid-based integrated avoidance guidance and control for hypersonic reentry vehicle][research_yu_wang_2026]
- [Yu Li and Nai-gang Cui, 2008, Maximum crossrange for hypersonic boost-glide missile][research_yuli_naigangcui_2008]
- [Yuan and others, 2026, Piecewise Nonsingular Practical Prescribed-Time Control for Three-Dimensional Skip-Trajectory Tracking of Hypersonic Glide Vehicles][research_yuan_gao_2026]
- [Yuanjie and others, 2023, Intelligent Trajectory Predicting of Hypersonic Vehicle Using LSTM][research_yuanjie_chunqiao_2023]
- [Yuhang Yun and others, 2016, Adaptive sliding-mode guidance with terminal angle constraints based on explicit space engagement model][research_yuhangyun_shengjingtang_2016]
- [Yujie and Yanhua, 2025, Fuel-Optimal Control and Robustness Optimization Methods of Hypersonic Vehicles in the Ascending Stage][research_yujie_yanhua_2025]
- [Yulian and Bin, 2014, On the feedback linearization control for hypersonic flight vehicle analogy X20][research_yulian_bin_2014]
- [Yumusak and Eyi, 2013, Aerothermodynamic Shape Optimization of Hypersonic Blunt Bodies][research_yumusak_eyi_2013]
- [Zadonsky and others, 2013, NUMERICAL AND EXPERIMENTAL INVESTIGATION OF AERODYNAMIC CHARACTERISTICS OF THE HYPERSONIC AIRCRAFT MODEL OF INTEGRATED CONFIGURATION][research_zadonsky_kosykh_2013]
- [Zaehringer and others, 2003, Lateral Separation Dynamics and Stability of a Two-Stage Hypersonic Vehicle][research_zaehringer_heller_2003]
- [Zamora and others, 2012, Spark-plasma sintering of ZrB2 ultra-high-temperature ceramics at lower temperature via nanoscale crystal refinement][research_zamora_ortiz_2012]
- [Zamora and others, 2014, Effect of graphite addition on the spark-plasma sinterability of ZrB2 and ZrB2-SiC ultra-high-temperature ceramics][research_zamora_nygren_2014]
- [Zampa and others, 2025, Optimization of Hypersonic Re-Entry Vehicle Aerodynamics for Communication Blackout Mitigation][research_zampa_difabbio_2025]
- [Zapata-Solvas and others, 2015, Effect of oxidation on room temperature strength of ZrB 2 - and HfB 2 - based ultra-high temperature ceramics][research_zapatasolvas_jayaseelan_2015]
- [Zemlyanskii, 1966, Hypersonic nonuniform gas flow past a beveled blunt leading edge][research_zemlyanskii_1966]
- [Zeng and others, 2008, Fracture Strength of Ultra-High Temperature Ceramics][research_zeng_fang_2008]
- [Zeng and others, 2019, Positioning and Tracking Performance Analysis of Hypersonic Vehicle based on Aerodynamic Model][research_zeng_gao_2019]
- [Zeng and others, 2021, Hypersonic Vehicle Trajectory Classification Using Improved CNN-LSTM Model][research_zeng_zhuang_2021]
- [Zewge and Bang, 2022, Reentry-phase Tracking of a Ballistic Missile in the Presence of Radar Glint Noise][research_zewge_bang_2022]
- [Zhai and others, 2016, Fault-tolerant control for reentry hypersonic vehicle with blended aerodynamic surfaces and RCS][research_zhai_qi_2016]
- [Zhai and others, 2018, Robust Adaptive Optimized Tracking Control for a Hypersonic Vehicle with Varying Uncertainties][research_zhai_yang_2018]
- [Zhai and others, 2019, Compound fault-tolerant attitude control for hypersonic vehicle with reaction control systems in reentry phase][research_zhai_qi_2019]
- [Zhai and others, 2020, Alleviation of lateral spillage of two-dimensional hypersonic inlet using waverider-configuration chines][research_zhai_zhang_2020]
- [Zhai and others, 2026, Nonlinear dynamic inversion-based robust adaptive learning control for boost-glide two-stage-to-orbit aerospace vehicles][research_zhai_li_2026]
- [Zhai and Yang, 2020, Piecewise analytic optimized ascent trajectory design and robust adaptive finite-time tracking control for hypersonic boost-glide vehicle][research_zhai_yang_2020]
- [Zhai and Zhou, 2009, Adjustable Range Trajectory Design with Multiple Constraints][research_zhai_zhou_2009]
- [Zhan and others, 2017, Gaussian mixture approximation smoother for hypersonic glide reentry vehicles tracking][research_zhan_liang_2017]
- [Zhang and Bai, 2021, Analysis of ultraviolet spectral parameters of NO molecules in the shock layer of RAM-CII hypersonic vehicle][research_zhang_bai_2021]
- [Zhang and Cao, 2019, Flight Control of Air-Breathing Hypersonic Vehicles Based on Disturbance Rejection Scheme][research_zhang_cao_2019]
- [Zhang and Chen, 2011, Reentry Vehicle Constrained Trajectory Optimization][research_zhang_chen_2011_b]
- [Zhang and Chen, 2011, Trajectory Optimization for Hypersonic Vehicle Satisfying Maneuvering Penetration][research_zhang_chen_2011]
- [Zhang and Ding, 2023, Numerical algorithm for hypersonic vehicle optimal flight control][research_zhang_ding_2023_b]
- [Zhang and Du, 2017, The robust maneuver flight control of hypersonic glide vehicles with input saturation using disturbance observer][research_zhang_du_2017]
- [Zhang and Gao, 2018, Infrared measurement and composite tracking algorithm for air-breathing hypersonic vehicles][research_zhang_gao_2018]
- [Zhang and Han, 2024, Extended Observer-Based Fault-Tolerant Attitude Control of Hypersonic Reentry Vehicle Considering Actuator and Sensor Faults][research_zhang_han_2024]
- [Zhang and Han, 2025, Control Allocation Based Fault-Tolerant Attitude Control of Hypersonic Reentry Vehicle][research_zhang_han_2025]
- [Zhang and Hu, 2011, Prediction-based guidance algorithm for high-lift reentry vehicles][research_zhang_hu_2011]
- [Zhang and Liu, 2011, RLV Reentry Trajectory Optimization through Hybridization of an Improved GA and a SQP Algorithm][research_zhang_liu_2011]
- [Zhang and others, 2007, Ultra-High Temperature Ceramics UHTCs via Reactive Sintering][research_zhang_wu_2007]
- [Zhang and others, 2008, Preparation and Characterization of Stable ZrB 2 -Based Ultra-High Temperature Ceramics Slurry by Aqueous Gelcasting][research_zhang_yan_2008]
- [Zhang and others, 2010, Multidisciplinary Design under Uncertainty for a Hypersonic Vehicle][research_zhang_he_2010]
- [Zhang and others, 2012, A New Robust Controller for Flight Control System of Hypersonic Flying Vehicle][research_zhang_fan_2012]
- [Zhang and others, 2012, Research on Influence of Aerodynamic Force on the Aerodynamic Heat for the Hypersonic Vehicle][research_zhang_xu_2012]
- [Zhang and others, 2013, Adaptive Backstepping Controller Design for Reentry Attitude of Near Space Hypersonic Vehicle][research_zhang_sun_2013]
- [Zhang and others, 2013, Robust Continuous Terminal Sliding Mode Control Design for a Near-Space Hypersonic Vehicle][research_zhang_sun_2013_b]
- [Zhang and others, 2013, Second-order terminal sliding mode control for hypersonic vehicle in cruising flight with sliding mode disturbance observer][research_zhang_sun_2013_c]
- [Zhang and others, 2014, Robust tracking control design for a flexible air-breathing hypersonic vehicle][research_zhang_xian_2014]
- [Zhang and others, 2014, Study of Proportional Navigation Guidance of Reentry Vehicle Considering Wind Disturbance][research_zhang_huang_2014]
- [Zhang and others, 2015, Fast Computation of Hypersonic Gliding Lifting Body Aerodynamic Based on Configuration Parameters][research_zhang_yang_2015]
- [Zhang and others, 2015, On-line reentry guidance algorithm with both path and no-fly zone constraints][research_zhang_liu_2015]
- [Zhang and others, 2016, Aerodynamic Optimization for Hypersonic Wing Design Based on Local Piston Theory][research_zhang_ye_2016]
- [Zhang and others, 2016, Parameterization and optimization of hypersonic-gliding vehicle configurations during conceptual design][research_zhang_wang_2016]
- [Zhang and others, 2017, Analytical decoupling control of a generic hypersonic vehicle based on internal model control][research_zhang_xia_2017]
- [Zhang and others, 2017, Estimation of aerodynamic parameter for maneuvering reentry vehicle tracking][research_zhang_fu_2017]
- [Zhang and others, 2017, Global Sliding Mode Control for the Bank-to-Turn of Hypersonic Glide Vehicle][research_zhang_yu_2017]
- [Zhang and others, 2017, Linear near-equilibrium glide model for unpowered entry trajectory control][research_zhang_li_2017]
- [Zhang and others, 2017, Rapid generation of boost trajectory for boost-glide missile][research_zhang_he_2017]
- [Zhang and others, 2017, Under no-fly zone constraints accuracy hypersonic vehicle trajectory optimization][research_zhang_liu_2017]
- [Zhang and others, 2018, Entry guidance for high-L/D hypersonic vehicle based on drag-vs-energy profile][research_zhang_chen_2018]
- [Zhang and others, 2018, Reduced-order Linear Extended State Observer Based Trajectory Linearization Control for Hypersonic Reentry Vehicle under High Maneuver Flight with Multiple Disturbances][research_zhang_yu_2018]
- [Zhang and others, 2018, Time-optimal memetic whale optimization algorithm for hypersonic vehicle reentry trajectory optimization with no-fly zones][research_zhang_wang_2018]
- [Zhang and others, 2018, Ultra-high temperature ceramic coating for carbon/carbon composites against ablation above 2000 K][research_zhang_wang_2018_b]
- [Zhang and others, 2019, Clutter modelling and simulation for hypersonic vehicle-borne radar][research_zhang_liao_2019]
- [Zhang and others, 2019, Damage-Mitigating Predictive Control of Airfoil Flutter for a General Hypersonic Flight Vehicle][research_zhang_wang_2019_b]
- [Zhang and others, 2019, Dynamic damage analysis of airfoil flutter for a generic hypersonic flight vehicle][research_zhang_wang_2019_c]
- [Zhang and others, 2019, Efficient Aerodynamic Shape Optimization of the Hypersonic Lifting Body Based on Free Form Deformation Technique][research_zhang_feng_2019]
- [Zhang and others, 2019, Free Form Deformation Method Applied to Modeling and Design of Hypersonic Glide Vehicles][research_zhang_feng_2019_b]
- [Zhang and others, 2019, Performance comparison between waverider and wide-speed-range gliding vehicle based on CFD approaches][research_zhang_wang_2019]
- [Zhang and others, 2019, Switched linear parameter-varying modeling and tracking control for flexible hypersonic vehicle][research_zhang_nie_2019]
- [Zhang and others, 2020, LSTM-Based Boost-Phase Ballistic Missile Tracking][research_zhang_ji_2020]
- [ZHANG and others, 2020, Modeling and Analysis of a 6-DOF Flexible Hypersonic Flight Vehicle][research_zhang_zhang_2020]
- [Zhang and others, 2021, Fuzzy Active Disturbance Rejection Control for Hypersonic Vehicle][research_zhang_feng_2021]
- [Zhang and others, 2021, Impact-Angle and Terminal-Maneuvering-Acceleration Constrained Guidance against Maneuvering Target][research_zhang_chen_2021]
- [ZHANG and others, 2021, Launch Vehicle Classification for Decision-Making of Small Satellite Launch Options][research_zhang_xu_2021]
- [Zhang and others, 2021, Whole-Channel Decoupling Control of Hypersonic Vehicle Based on ESO][research_zhang_du_2021]
- [Zhang and others, 2022, A search method for a hypersonic gliding vehicle based on early warning information guidance][research_zhang_xiong_2022]
- [Zhang and others, 2022, A Sinking Trajectory Planning Method For Reentry Vehicle Under Strict Constraints][research_zhang_yang_2022]
- [Zhang and others, 2022, Analysis of electromagnetic wave radiation of hypersonic vehicle covered by plasma sheath][research_zhang_jin_2022]
- [Zhang and others, 2022, Angular-Accelerometer-Based Flexible-State Estimation and Tracking Controller Design for Hypersonic Flight Vehicle][research_zhang_zheng_2022]
- [Zhang and others, 2022, Control Contraction Metrics Based Robust Tracking Guidance for Hypersonic Glide Vehicle in Terminal Phase][research_zhang_zhang_2022]
- [Zhang and others, 2022, Finite-time Control for the Hypersonic Morphing Flight Vehicle With FTESO][research_zhang_huang_2022]
- [Zhang and others, 2022, hp-Adaptive RPD based sequential convex programming for reentry trajectory optimization][research_zhang_su_2022]
- [Zhang and others, 2022, Sliding mode based fault-tolerant control of hypersonic reentry vehicle using composite learning][research_zhang_shou_2022]
- [Zhang and others, 2022, Trajectory Optimization with Polygonal No-Fly Zone Constraints for Hypersonic Glide Vehicle][research_zhang_sun_2022]
- [Zhang and others, 2023, Event-Trigger-Based Global Sliding Mode Control for a Hypersonic Morphing Vehicle][research_zhang_wang_2023]
- [Zhang and others, 2023, Mixed-integer trajectory optimization with no-fly zone constraints for a hypersonic vehicle][research_zhang_zhang_2023]
- [Zhang and others, 2023, Neural Adaptive Finite-Time Sliding Mode Controller for Air-Breathing Hypersonic Vehicle][research_zhang_ding_2023]
- [Zhang and others, 2023, Optical performance evaluation of an infrared system of a hypersonic vehicle in an aero-thermal environment][research_zhang_ju_2023]
- [Zhang and others, 2023, Policy Iteration Adaptive Dynamic Programming Based Control for Hypersonic Flight Vehicles][research_zhang_fu_2023]
- [Zhang and others, 2023, Reentry Trajectory Planning and Tracking Law of Hypersonic Glide Vehicle Under the Influence of Environmental Uncertainty][research_zhang_chen_2023]
- [Zhang and others, 2023, The Progress and Intelligent Control/Decision Technical Discussion on Hypersonic Morphing Flight Vehicle][research_zhang_bai_2023]
- [Zhang and others, 2024, Internet of Things Based Digital Twin Model Construction and Online Fault-Tolerant Control of Hypersonic Flight Vehicle][research_zhang_li_2024]
- [Zhang and others, 2024, Multi-Objective Optimization of Real-Time Parameters for Thermal Management System of Hypersonic Vehicle Actuating System][research_zhang_wang_2024]
- [Zhang and others, 2024, Trajectory Control of Midcourse Guidance for Air-to-Air Missile Based on Feedback Linearization and Sliding Mode Control][research_zhang_tong_2024]
- [Zhang and others, 2025, Adaptive Target Tracking Method for Hypersonic Gliding Vehicle's Glide Phase][research_zhang_li_2025_b]
- [Zhang and others, 2025, Aerodynamic and stealth integrated design of hypersonic vehicle based on discrete adjoint method][research_zhang_xia_2025]
- [Zhang and others, 2025, Anti-Disturbance Control of Air-Breathing Hypersonic Vehicle A Zero-Sum Differential Game Approach][research_zhang_wang_2025_b]
- [Zhang and others, 2025, Ascent Trajectory Optimization for Boost-Glide Vehicle Using Homotopy Approximation Function Sequential Convex Programming][research_zhang_li_2025]
- [Zhang and others, 2025, Configuration optimization and optical transmission simulation of a conformal fairing under a hypersonic thermal environment][research_zhang_song_2025]
- [Zhang and others, 2025, Coordinated Design of Intelligent Morphing Decision and Entry Guidance for Morphing Hypersonic Glide Vehicles][research_zhang_guo_2025]
- [Zhang and others, 2025, Enhanced Control System for Morphing Hypersonic Aircraft Based on an Improved Proximal Policy Optimization Algorithm][research_zhang_tang_2025]
- [Zhang and others, 2025, Finite-time fault-tolerant attitude control for hypersonic reentry vehicle based composite learning observer][research_zhang_han_2025_b]
- [Zhang and others, 2025, Infrared imaging performance evaluation and perspective optimization strategy for hypersonic vehicles in different flight attitudes][research_zhang_xu_2025]
- [Zhang and others, 2025, Reentry Trajectory Planning of Hypersonic Gliding Vehicle Based on IFDS Algorithm][research_zhang_wang_2025]
- [Zhang and others, 2025, Research on Aerodynamic Force/Thrust Vector Combined Trajectory Optimization Method for Hypersonic Drones Based on Deep Reinforcement Learning][research_zhang_zhou_2025]
- [Zhang and others, 2025, Simulation of integrated infrared radiation characteristics of hypersonic cruise vehicles][research_zhang_bian_2025]
- [Zhang and others, 2026, Effects of Wavy Wall on Hypersonic Boundary-Layer Instability of Hypersonic Transition Research Vehicle Lifting Body][research_zhang_hu_2026]
- [Zhang and others, 2026, Novel Predefined-Time Sliding Mode Fault-Tolerant Control for Hypersonic Vehicle Attitude Tracking][research_zhang_li_2026]
- [Zhang and others, 2026, Predefined-time Control for Boost-glide Missile System under the ACE Hardware-in-the-loop Environment][research_zhang_yan_2026]
- [Zhang and others, 2026, Research Progress on Supercritical CO2 Brayton Cycle System and Compressor for Thermal Protection of Hypersonic Aircraft][research_zhang_yu_2026]
- [Zhang and others, 2026, Suboptimal Stochastic Differential Game Control for Sequential Evasive Maneuvers of a Hypersonic Glide Vehicle][research_zhang_chen_2026]
- [Zhang and others, 2026, Thermal model test and multi-scale simulation method for the lattice-structured air rudder of hypersonic flight vehicle][research_zhang_liao_2026]
- [Zhang and SHE, 2015, Elliptical Trajectory Guidance Law with Terminal Impact Angle Constraint][research_zhang_she_2015]
- [Zhang and Tang, 2008, Rapid terminal area trajectory planning for reentry vehicles][research_zhang_tang_2008]
- [Zhang and Tang, 2015, Co-evolutionary multiobjective multidisciplinary design optimization for the airframe/propulsion integration of hypersonic vehicles][research_zhang_tang_2015]
- [Zhang and Yang, 2018, Fast Convergent Nonsingular Terminal Sliding Mode Guidance Law with Impact Angle Constraint][research_zhang_yang_2018]
- [Zhang and Zong, 2014, Modeling and Analysis of an Air-Breathing Flexible Hypersonic Vehicle][research_zhang_zong_2014]
- [Zhang Qingzhen and others, 2007, Reentry trajectory planning optimization based on ant colony algorithm][research_zhangqingzhen_liucunjia_2007]
- [Zhang Qingzhen and others, 2008, Reentry trajectory planning optimization based on sequential quadratic programming][research_zhangqingzhen_gaochen_2008]
- [Zhang Zhikai and others, 2015, Longitudinal attitude control of a hypersonic vehicle with angle of attack constraints][research_zhangzhikai_duanguangren_2015]
- [Zhang, 2011, Effects of hypersonic vehicle's optical dome on infrared imaging][research_zhang_2011]
- [Zhang, 2015, On-board three-dimensional trajectory planning for reentry vehicle][research_zhang_2015]
- [Zhang, 2015, Research Progress of Hypersonic Inlet Inverse Design Based on Curved Shock Compression System][research_zhang_2015_b]
- [Zhang, 2017, A composite guidance law through reference trajectory tracking for Mars entry guidance][research_zhang_2017]
- [Zhang, 2020, Features and Drag Reduction Analysis of Drag in Hypersonic Inlet][research_zhang_2020]
- [Zhang, 2020, Inverse Design and Experiment of Hypersonic Curved Shock Wave Compression Inlet][research_zhang_2020_b]
- [Zhang, 2026, PERFORMANCE OPTIMIZATION OF TRAJECTORY DEVIATION CORRECTION IN LONG-RANGE BALLISTIC MISSILES AN ADAPTIVE PID CONTROL APPROACH][research_zhang_2026]
- [Zhao and Chen, 2021, Predictive sliding mode tracking control of hypersonic vehicle based on disturbance observer][research_zhao_chen_2021]
- [Zhao and Li, 2019, Prescribed Performance Fault Tolerant Control for Hypersonic Flight Vehicles With Actuator Failures][research_zhao_li_2019]
- [Zhao and others, 2012, Reentry Trajectory Planning Based on the Secondary Reversal Dynamics for the Second Generation Reusable Launch Vehicles][research_zhao_cui_2012_b]
- [Zhao and others, 2012, Trajectory Planning and Prediction Guidance Based on the Moon-Earth Return Reentry Dynamics][research_zhao_cui_2012]
- [Zhao and others, 2013, A New Support Structure in Waverider Force Measurement][research_zhao_guo_2013]
- [Zhao and others, 2014, Progress in reentry trajectory planning for hypersonic vehicle][research_zhao_zhou_2014]
- [Zhao and others, 2014, Reentry Trajectory Optimization Based on a Multistage Pseudospectral Method][research_zhao_zhou_2014_b]
- [Zhao and others, 2016, Integrated Guidance and Control for a Hypersonic Vehicle with Recursive H8 Method][research_zhao_wang_2016]
- [Zhao and others, 2018, Design and high speed aerodynamic performance analysis of vortex lift waverider with a wide-speed range][research_zhao_huang_2018_b]
- [Zhao and others, 2018, Design of the Nonlinear Cruise Controllers for Hypersonic Vehicle][research_zhao_huang_2018]
- [Zhao and others, 2018, Joint Design of Guidance and Control System for a Hypersonic Gliding Vehicle on Lie Groups][research_zhao_he_2018]
- [Zhao and others, 2018, LPV model reference control method for hypersonic vehicle control system][research_zhao_cai_2018]
- [Zhao and others, 2019, Analytical solutions for longitudinal-plane motion of hypersonic skip-glide trajectory][research_zhao_chen_2019]
- [Zhao and others, 2020, A Combined Guidance Law for Intercepting Hypersonic Large Maneuvering Targets][research_zhao_dong_2020]
- [Zhao and others, 2020, An overview of research on wide-speed range waverider configuration][research_zhao_huang_2020]
- [Zhao and others, 2021, Control separation based fault accommodation for flexible hypersonic vehicles][research_zhao_jiang_2021]
- [zhao and others, 2021, Design of LPV sliding mode controller for hypersonic vehicle based on the upper bound of uncertainty][research_zhao_yao_2021]
- [Zhao and others, 2022, Aerodisk Effect on Hypersonic Boundary Layer Transition and Heat Transfer of HIFiRE-5 Vehicle][research_zhao_shao_2022]
- [Zhao and others, 2022, Analytical trajectory prediction for skip re-entry of lifting vehicle][research_zhao_meng_2022]
- [Zhao and others, 2022, Improved Fractional-Order Extended State Observer-Based Hypersonic Vehicle Active Disturbance Rejection Control][research_zhao_hu_2022]
- [Zhao and others, 2023, Simulation analysis of space-based infrared remote sensing characteristics of hypersonic vehicles][research_zhao_hong_2023]
- [Zhao and others, 2024, Study on the effect of the canard on wide-speed range aerodynamic performance of the cuspidal waverider][research_zhao_xie_2024]
- [Zhao and others, 2025, Optimization of Midcourse Guidance Trajectory for Hypersonic Vehicle Swarms Using the Radau Pseudospectral Method][research_zhao_quan_2025]
- [Zhao and others, 2025, Research on integrated design method of wide-range hypersonic vehicle/engine based on dynamic multi-objective optimization][research_zhao_ma_2025]
- [Zhao and others, 2026, Glide Trajectory Optimization of Guided Projectiles Using an Improved Grey Wolf Optimizer and hp-Adaptive Radau Pseudospectral Method][research_zhao_wu_2026]
- [Zhao and others, 2026, Tailoring layer architecture to enhance the toughness of ZrB2-ZrC-SiC/C laminated ultra-high temperature ceramics][research_zhao_bai_2026]
- [Zhao and Pan, 2026, Reentry trajectory optimization for cross-domain morphing vehicles based on functional connections theory][research_zhao_pan_2026]
- [Zhao and Song, 2017, Reentry trajectory optimization with waypoint and no-fly zone constraints using multiphase convex programming][research_zhao_song_2017]
- [Zhao and Tang, 2015, Dynamic Inverse Based Controller for a Hypersonic Flight Vehicle][research_zhao_tang_2015]
- [Zhao and Yang, 2021, Global adaptive neural backstepping control of a flexible hypersonic vehicle with disturbance estimation][research_zhao_yang_2021]
- [Zhao and Zhou, 2013, Reentry trajectory optimization for hypersonic vehicle satisfying complex constraints][research_zhao_zhou_2013]
- [Zhao, 2011, Some Applications of WCNS-E-5 on Shock-Wave/Boundary-Layer Interactions and Aerodynamic Heating Prediction in Hypersonic Flows][research_zhao_2011]
- [Zhao, 2021, A Functional Based Prediction Method for Hypersonic Aerodynamic Force and Heat][research_zhao_2021_c]
- [Zhao, 2021, An Overview of Ground-Flying Calibration Technologies for Hypersonic Vehicle][research_zhao_2021]
- [Zhao, 2021, Development of Hypersonic Aerothermodynamic Technologies][research_zhao_2021_b]
- [Zheleznyakova and Surzhikov, 2014, Calculation of a hypersonic flow over bodies of complex configuration on unstructured tetrahedral meshes using the AUSM scheme][research_zheleznyakova_surzhikov_2014]
- [Zhen and Fei, 2012, Study on dynamic inversion control of hypersonic vehicle][research_zhen_fei_2012]
- [Zheng and others, 2020, Ascent trajectory design of small-lift launch vehicle using hierarchical optimization][research_zheng_fu_2020]
- [Zheng and others, 2020, Local-Turning Osculating Cones Method for Waverider Design][research_zheng_hu_2020]
- [Zheng and others, 2020, Multiple Osculating Cones' Waverider Design Method for Ruled Shock Surfaces][research_zheng_li_2020]
- [Zheng and others, 2022, Entry Guidance with No-Fly Zone Avoidance for Hypersonic Glide Vehicle][research_zheng_wang_2022]
- [Zheng and Selezneva, 2022, Asymptotic Adaptive Roll Tracking Control for Single Moving-mass Controlled Reentry Vehicle][research_zheng_selezneva_2022]
- [Zheng, 2021, Aerodynamic Shape Design of Hypersonic Vehicles via Interval-Robust Optimization Method Including Geometric Tolerances and Multiple Flight Conditions][research_zheng_2021]
- [Zhengchun, 2018, A New Reentry Trajectory Design Approach for Lift-control Flight Vehicle Based on Cruising Design Concept][research_zhengchun_2018]
- [Zhengdong and others, 2013, Nonlinear Robust Control of a Hypersonic Flight Vehicle Using Fuzzy Disturbance Observer][research_zhengdong_man_2013]
- [Zhi and others, 2015, Detached Eddy Simulation on Hypersonic Base Flow Structure of Reentry-F Vehicle][research_zhi_liang_2015]
- [Zhi and others, 2015, Hybrid Re-entry Guidance for Reusable Launch Vehicle][research_zhi_ran_2015]
- [Zhijian and others, 2018, A novel tightly coupled algorithm for the air data estimation of a hypersonic vehicle][research_zhijian_huan_2018]
- [Zhiqiang Zhao and Zhengdong Hu, 2010, A rapid reentry trajectory planning method for CAV][research_zhiqiangzhao_zhengdonghu_2010]
- [Zhivotov and Nikolaev, 2011, METHOD OF CALCULATING AERODYNAMIC CHARACTERISTICS OF HYPERSONIC FLYING VEHICLE ELEMENTS WITH ALLOWANCE FOR VISCOSITY, ENTROPY EFFECTS, AND VORTEX INTERACTION][research_zhivotov_nikolaev_2011]
- [Zhong and others, 2017, Fabrication of modified ultra high-temperature ceramic hybrid powders using in situ grown SiC nanowires][research_zhong_yan_2017]
- [Zhong and others, 2022, A Switching-Based Control Method for the Fairing Separation Control of Axisymmetric Hypersonic Vehicles][research_zhong_fan_2022]
- [Zhong and Wu, 2021, A Switching-Based Interference Control for Booster Separation of Hypersonic Vehicle][research_zhong_wu_2021]
- [Zhongjie Meng and others, 2008, Trajectory Planning for Hypersonic Vehicle Using Improved Sparse A* Algorithm][research_zhongjiemeng_panfenghuang_2008]
- [Zhongjie Meng and others, 2010, Multi-constrained fast trajectory optimization of glide phase for hypersonic vehicle][research_zhongjiemeng_jianzhongdong_2010]
- [Zhou and Fei, 2013, Adaptive dynamic surface control for air-breathing hypersonic vehicle][research_zhou_fei_2013]
- [Zhou and others, 2006, Hypersonic vehicle trajectory design based on optimal control theory][research_zhou_chen_2006]
- [Zhou and others, 2008, Preparation and Properties of 2D Carbon Cloth Reinforced Ultra-High Temperature Ceramic Matrix Composites][research_zhou_hu_2008]
- [Zhou and others, 2010, Mechanical Behaviors of Ultra-High Temperature Ceramics][research_zhou_zeng_2010]
- [Zhou and others, 2012, A Simple Reentry Trajectory Generation and Tracking Scheme for Common Aero Vehicle][research_zhou_tan_2012]
- [Zhou and others, 2015, Research of Infrared Electro Optical System's Operating Range on Hypersonic Vehicle][research_zhou_shi_2015]
- [Zhou and others, 2016, Boosting trajectory planning for hypersonic vehicle][research_zhou_pan_2016]
- [Zhou and others, 2017, A Preliminary Research on a Two-Stage-To-Orbit Vehicle with Airbreathing Pre-cooled Hypersonic Engines][research_zhou_lu_2017]
- [Zhou and others, 2017, Fast Computation Scheme for Gravity Anomaly along Glide Trajectory Based on Extension Approximation][research_zhou_ding_2017]
- [Zhou and others, 2017, Online optimal midcourse trajectory modification algorithm for hypersonic vehicle interceptions][research_zhou_lei_2017]
- [Zhou and others, 2018, Multichannel High Resolution Wide Swath SAR Imaging for Hypersonic Air Vehicle with Curved Trajectory][research_zhou_sun_2018]
- [Zhou and others, 2018, Reconstruction Model Optimization for Gravity Anomaly along Glide Trajectory][research_zhou_ding_2018]
- [Zhou and others, 2019, Glide trajectory optimization for hypersonic vehicles via dynamic pressure control][research_zhou_wang_2019]
- [Zhou and others, 2022, Application of a Gas-Kinetic BGK Scheme in Thermal Protection System Analysis for Hypersonic Vehicles][research_zhou_du_2022]
- [Zhou and others, 2023, A Real-Time Trajectory Planning and Guidance Algorithm for Terminal Area Energy Management][research_zhou_zheng_2023]
- [Zhou and others, 2023, Aerothermal Heating Correlations at Stagnation Point/Line in Low-Enthalpy Hypersonic Flow][research_zhou_yi_2023]
- [Zhou and others, 2023, An Improved Predictor-Corrector Guidance Algorithm for Reentry Glide Vehicle Based on Fast Landing Points Position Prediction][research_zhou_li_2023]
- [Zhou and others, 2023, Optimal guidance for hypersonic vehicle using analytical solutions and an intelligent reversal strategy][research_zhou_li_2023_b]
- [Zhou and others, 2023, Upgraded design methodology for airframe/engine integrated full-waverider vehicle considering thrust chamber design][research_zhou_xia_2023]
- [Zhou and others, 2024, Study on coupled heat transfer of pyrolytic kerosene and supercritical CO2 in zigzag-type PCHE used for hypersonic vehicle power generation system][research_zhou_zhang_2024]
- [Zhou and others, 2025, Hypersonic Vehicle Cooperative Guidance Law Identification and Trajectory Prediction][research_zhou_xu_2025]
- [Zhou and others, 2026, Integrated Propulsion-Aerodynamics-Trajectory-Cost Design Optimization for High-Speed, Long-Range Rocket-Boosted Vehicles][research_zhou_zhou_2026]
- [Zhou and others, 2026, Physics-Informed Ensemble Informerstack for Hypersonic Glide Vehicle Trajectory Prediction][research_zhou_wang_2026]
- [Zhou and Qi, 2024, Design of hypersonic vehicle tracking controller based on high-order fully actuated system theory][research_zhou_qi_2024]
- [Zhou Jinwei and others, 2015, Research of Infrared Detectability of Hypersonic Vehicle][research_zhoujinwei_lijicheng_2015]
- [Zhou Wenya and others, 2008, Entry guidance for Common Aero Vehicle][research_zhouwenya_chenhongbo_2008]
- [Zhou, 2009, On-Board Reentry Flight Trajectory Generation and Guidance for Common Aero Vehicle][research_zhou_2009]
- [Zhou, 2018, Porous Ceramic Matrix Phase Change Composites for Thermal Control Purposes of Hypersonic Vehicle][research_zhou_2018]
- [Zhou, 2023, Design of Hypersonic Vehicle Time-Delay Compensation Controller based on Dynamic Surface Control][research_zhou_2023]
- [Zhu and Liu, 2015, Adaptive dynamic surface control for hypersonic vehicle with input nonlinearity][research_zhu_liu_2015]
- [Zhu and Liu, 2015, Robust flight control for hypersonic flight vehicle using nonlinear disturbance observer][research_zhu_liu_2015_b]
- [Zhu and others, 2014, Optimal diving maneuver strategy considering guidance accuracy for hypersonic vehicle][research_zhu_liu_2014]
- [Zhu and others, 2014, Three-dimensional nonlinear coupling guidance for hypersonic vehicle in dive phase][research_zhu_liu_2014_b]
- [Zhu and others, 2016, Characteristic model-based robust predictive control for reentry hypersonic vehicle with constraints][research_zhu_li_2016]
- [Zhu and others, 2016, Impact of cabin environment on thermal protection system of crew hypersonic vehicle][research_zhu_zhao_2016]
- [Zhu and others, 2016, Optimal control and analysis for aero-elastic model of hypersonic vehicle][research_zhu_shen_2016]
- [Zhu and others, 2016, Three-dimensional robust diving guidance for hypersonic vehicle][research_zhu_liu_2016]
- [Zhu and others, 2017, Simulation research on hypersonic vehicle based on fuzzy adaptive control][research_zhu_chen_2017]
- [Zhu and others, 2018, Pendulum maneuvering strategy for hypersonic glide vehicles][research_zhu_he_2018]
- [Zhu and others, 2023, An Adaptive Sliding Mode Terminal Guidance Method][research_zhu_yao_2023]
- [Zhu and Shen, 2015, Three Dimensional Trajectory Linearization Control for Flight of Air-breathing Hypersonic Vehicle][research_zhu_shen_2015]
- [Zhu, 2013, Robust Control for Air-Breathing Hypersonic Cruise Vehicles][research_zhu_2013]
- [Zhuang and Ridley, 2024, The Development of Thermal Protection Systems for Aerospace Vehicle Reentry A Review][research_zhuang_ridley_2024]
- [Zhuo and others, 2011, A Reentry Trajectory Planning Based on the Optimization of Angle of Attack][research_zhuo_qingzhen_2011]
- [Zhuo and others, 2023, Integrated Guidance and Control System Design for Hypersonic Vehicle Based on Backstepping High-Order Sliding Mode Approach][research_zhuo_zhang_2023]
- [Zien, 1998, Effects of melt layer on steady aerodynamic ablation in hypersonic flow][research_zien_1998]
- [Zien, 2006, Modeling of Hypersonic Melting Ablation Near Stagnation Point and Extension to Waveriders][research_zien_2006]
- [Zimmermann and others, 1996, Comparison of guidance concepts for a semi-ballistic reentry capsule][research_zimmermann_burkhardt_1996]
- [Zishka and Agarwal, 2015, Shape Optimization of a Blunt Body in Reacting Hypersonic flow in Thermal Non-Equilibrium for Reducing Both Drag and Heat Transfer][research_zishka_agarwal_2015]
- [Ziyang and others, 2025, Optimizing trajectory tracking control for hypersonic flight vehicles via ADDHP][research_ziyang_xiaohui_2025]
- [Zoby and others, 1993, Hypervelocity stagnation-point heating rate discrepancies][research_zoby_gupta_1993]
- [Zoli and others, 2021, Ultra-High Temperature Ceramic Matrix Composites][research_zoli_sciti_2021]
- [Zong and others, 2012, Output feedback back-stepping control for a generic Hypersonic Vehicle via small-gain theorem][research_zong_ji_2012]
- [Zong and others, 2013, Adaptive high-order dynamic sliding mode control for a flexible air-breathing hypersonic vehicle][research_zong_wang_2013]
- [Zong and others, 2013, Quasi-continuous high-order sliding mode controller and observer design for flexible hypersonic vehicle][research_zong_wang_2013_b]
- [Zope and others, 2026, Generalized 5-DoF Model for Hypersonic Boost-Glide Vehicle Trajectory Predictions][research_zope_bhushan_2026]
- [Zou and others, 2013, Entry trajectory planning using quasi-equilibrium glide assumption][research_zou_xie_2013]
- [Zou and others, 2015, Nonlinear Constrained Adaptive Backstepping Tracking Control for a Hypersonic Vehicle with Uncertainty][research_zou_wang_2015]
- [Zou and others, 2023, Rapid hypersonic sonic boom prediction using line-distributed energy impulse formulations with and without lift effect][research_zou_johnston_2023]
- [Zou and others, 2024, Computational and experimental investigation of near-field sonic boom of a HTV-2 type hypersonic boost gliding vehicle][research_zou_candler_2024]
- [Zuber and Bertin, 1998, Hypersonic aerodynamic research at the USAF Academy][research_zuber_bertin_1998]
- [Zubin and others, 1997, Lift-Drag Ratio of a Hypersonic Waverider of Delta Planform][research_zubin_ostapenko_1997]
- [Zuchowski, 2013, Structural Response and Service Life Prediction Concerns in the Design of Hypersonic Flight Vehicle Hot-Structure][research_zuchowski_2013]
- [Zuo and Hu, 2021, Thermochemical non-equilibrium effects on aerothermodynamic prediction of laminar double-cone flow][research_zuo_hu_2021]
- [Zuppardi and others, 2006, Evaluation of Rarefaction Effects on a Winged, Hypersonic Re-Entry Vehicle][research_zuppardi_costagliola_2006]
- [Zvedre, 2016, Does the US program of Conventional Prompt Global Strike threaten Russian national security?][research_zvedre_2016]
- [Zweber and others, 2002, Towards an Integrated Design Environment for Hypersonic Vehicle Design and Synthesis][research_zweber_kabis_2002]
- [Ösün and others, 2026, Conjugate Heat Transfer Modeling of a Hypersonic Vehicle Forebody][research_osun_james_2026]
- [Баринов and Просунцов, 2016, Modeling of Heat Transfer in Decomposable Materials of Thermal Protection Coating of Reentry Vehicle][research_modeling_of_heat_2016]
- [안미치코, 2013, Aerodynamics Calculation of Reentry Body in Hypersonic Flowfield][research_aerodynamics_calculation_of_2013]

[ref_erb]: https://spacenews.com/darpa-engineering-review-board-concludes-review-of-htv-2-second-test-flight/
[ref_falcon]: https://en.wikipedia.org/wiki/DARPA_Falcon_Project
[ref_htv2]: https://en.wikipedia.org/wiki/HTV-2_Falcon
[ref_minotaur]: https://en.wikipedia.org/wiki/Minotaur_IV
[ref_pgs]: https://en.wikipedia.org/wiki/Prompt_Global_Strike
[ref_x41_parsch]: https://www.designation-systems.net/dusrm/app4/x-41.html
[ref_x41_wiki]: https://en.wikipedia.org/wiki/X-41_Common_Aero_Vehicle
[ref_x43]: https://en.wikipedia.org/wiki/NASA_X-43

[related_post_a297_framing]: {% post_url 2025-10-06-x_planes_framing %}
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
[related_post_a327_rockwell_x30]: {% post_url 2025-11-05-x_planes_rockwell_x30 %}
[related_post_a328_rockwell_mbb_x31]: {% post_url 2025-11-06-x_planes_rockwell_mbb_x31 %}
[related_post_a329_boeing_x32]: {% post_url 2025-11-07-x_planes_boeing_x32 %}
[related_post_a330_lockheed_martin_x33]: {% post_url 2025-11-08-x_planes_lockheed_martin_x33 %}
[related_post_a331_orbital_sciences_x34]: {% post_url 2025-11-09-x_planes_orbital_sciences_x34 %}
[related_post_a332_lockheed_martin_x35]: {% post_url 2025-11-10-x_planes_lockheed_martin_x35 %}
[related_post_a333_mcdonnell_douglas_x36]: {% post_url 2025-11-11-x_planes_mcdonnell_douglas_x36 %}
[related_post_a334_boeing_x37]: {% post_url 2025-11-12-x_planes_boeing_x37 %}
[related_post_a335_scaled_composites_x38]: {% post_url 2025-11-13-x_planes_scaled_composites_x38 %}
[related_post_a336_x39_reserved_never_assigned]: {% post_url 2025-11-14-x_planes_x39_reserved_never_assigned %}
[related_post_a337_boeing_x40]: {% post_url 2025-11-15-x_planes_boeing_x40 %}

[research_188_nonlinear_1994]: https://doi.org/10.1016/0967-0661(94)90540-1
[research_212_problems_1994]: https://doi.org/10.1016/0967-0661(94)91001-4
[research_264_guidance_1994]: https://doi.org/10.1016/0967-0661(94)91055-3
[research_266_on_1994]: https://doi.org/10.1016/0967-0661(94)91057-x
[research_3_dimensional_trajectory_2002]: https://doi.org/10.5302/j.icros.2002.8.7.613
[research_a_new_2014]: https://doi.org/10.1201/b17735-84
[research_a_rapid_1969]: https://doi.org/10.2514/5.9781600864957.0203.0223
[research_a_simple_1964]: https://doi.org/10.2514/5.9781600864872.0931.0964
[research_abbasi_mortazavi_2013]: https://doi.org/10.1155/2013/419409
[research_abolghaseminajafabadi_kazemi_2024]: https://doi.org/10.1016/j.heliyon.2024.e27404
[research_aburomia_1971]: https://doi.org/10.2514/6.1971-81
[research_achambath_ramjatan_2019]: https://doi.org/10.2514/6.2019-1283
[research_acton_2015]: https://doi.org/10.1080/08929882.2015.1087242
[research_adami_mortazavi_2017]: https://doi.org/10.5028/jatm.v9i1.717
[research_adami_nosratolahi_2009]: https://doi.org/10.2514/6.2009-6092
[research_adami_nosratollahi_2011]: https://doi.org/10.1109/rast.2011.5966908
[research_adami_zhu_2007]: https://doi.org/10.2514/6.2007-6328
[research_adami_zhu_2008]: https://doi.org/10.2514/6.2008-7464
[research_adamo_steele_1978]: https://doi.org/10.1109/oceans.1978.1151064
[research_adamov_puzyrev_2014]: https://doi.org/10.1134/s0021894414050162
[research_adams_johnc_1973]: https://doi.org/10.21236/ad0756499
[research_adsit_carnahan_1972]: https://doi.org/10.1520/stp27743s
[research_aero_heating_prediction_2025]: https://doi.org/10.37285/bsp.sacad2025.05
[research_aerodynamic_heating_1979]: https://doi.org/10.2514/5.9781600865398.0192.0214
[research_aerodynamic_optimization_1994]: https://doi.org/10.2514/5.9781600866326.0296.0307
[research_aerodynamics_calculation_of_2013]: https://doi.org/10.17958/ksmt.15.6.201312.819
[research_aerothermodynamic_assessment_1979]: https://doi.org/10.2514/5.9781600865381.0387.0403
[research_aerothermodynamic_base_1978]: https://doi.org/10.2514/5.9781600865336.0049.0065
[research_aerothermodynamic_border_2014]: https://doi.org/10.1007/978-3-642-41714-6_10872
[research_aerothermodynamic_design_1982]: https://doi.org/10.2514/5.9781600865565.0477.0519
[research_aerothermodynamic_design_1993]: https://doi.org/10.2514/6.1993-4013
[research_aerothermodynamic_entry_1983]: https://doi.org/10.2514/5.9781600865626.0003.0020
[research_aerothermodynamic_environment_1979]: https://doi.org/10.2514/5.9781600865381.0108.0128
[research_aerothermodynamic_heating_1985]: https://doi.org/10.2514/5.9781600865718.0338.0360
[research_aerothermodynamic_predictions_2004]: https://doi.org/10.1201/9781482264715-22
[research_aerothermodynamic_testing_2023]: https://doi.org/10.1017/9781009030991.009
[research_aerothermodynamics_research_2002]: https://doi.org/10.2514/5.9781600866678.0205.0237
[research_afzal_roeser_2009]: https://doi.org/10.2514/6.2009-6108
[research_agarwal_2011]: https://doi.org/10.1080/10618562.2011.633490
[research_agarwal_nisar_2025]: https://doi.org/10.1016/j.ceramint.2025.09.427
[research_aggarwal_moore_1996]: https://doi.org/10.2514/6.1996-3738
[research_aggarwal_moore_1998]: https://doi.org/10.2514/2.4349
[research_agnone_zakkay_1985]: https://doi.org/10.2514/6.1985-453
[research_agnone_zakkay_1988]: https://doi.org/10.1007/bf00187363
[research_agostinelli_trifoni_2019]: https://doi.org/10.1016/j.ast.2019.02.023
[research_agustin_mangoubi_1998]: https://doi.org/10.2514/6.1998-4499
[research_agustin_mangoubi_1999]: https://doi.org/10.2514/2.4461
[research_ahmad_xing_2022]: https://doi.org/10.1016/j.oceaneng.2022.112343
[research_ahmed_qin_2009]: https://doi.org/10.21608/asat.2009.23443
[research_ahmed_qin_2010]: https://doi.org/10.1016/j.ast.2010.03.003
[research_ahmed_qin_2011]: https://doi.org/10.21608/asat.2011.23409
[research_ahmed_qin_2012]: https://doi.org/10.1007/978-3-642-25688-2_110
[research_ahuja_hartfield_2009]: https://doi.org/10.2514/6.2009-7323
[research_aircraft_design_1993]: https://doi.org/10.2514/6.1993-4007
[research_airforcetestpilotschooledwardsafbca_1987]: https://doi.org/10.21236/ada320212
[research_akinbo_olajuwon_2021]: https://doi.org/10.1016/j.icheatmasstransfer.2021.105115
[research_alavi_rosli_2015]: https://doi.org/10.1063/1.4907492
[research_albano_micheli_2013]: https://doi.org/10.1016/j.actaastro.2013.02.003
[research_alber_2012]: https://doi.org/10.1007/978-3-642-22537-6_5
[research_albert_braun_2020]: https://doi.org/10.2514/6.2020-1737
[research_aldamook_shaban_2026]: https://doi.org/10.47176/jafm.19.5.3813
[research_alexander_1970]: https://doi.org/10.21236/ad0875525
[research_alexander_tm_1978]: https://doi.org/10.21236/ada063655
[research_alferov_marchenko_2012]: https://doi.org/10.1134/s0018151x12040013
[research_aljbour_2026]: https://doi.org/10.2514/6.2026-5070.c1
[research_aljbour_2026_b]: https://doi.org/10.2514/6.2026-5070
[research_alkandry_boyd_2014]: https://doi.org/10.2514/1.t4233
[research_alkaya_alexsam_2018]: https://doi.org/10.3390/aerospace5030091
[research_allegre_heriarddubreuilh_1992]: https://doi.org/10.1007/978-3-642-77922-0_61
[research_allouche_haoui_2011]: https://doi.org/10.4028/www.scientific.net/amr.274.13
[research_allouche_renane_2020]: https://doi.org/10.1051/meca/2020006
[research_almeida_2021]: https://doi.org/10.2514/6.2021-1566
[research_alshibani_volery_2022]: https://doi.org/10.1007/978-981-16-7341-2_2
[research_amaratunga_tutty_1996]: https://doi.org/10.2514/6.1996-4587
[research_amati_bruno_2008]: https://doi.org/10.1016/j.energy.2007.08.012
[research_amato_giannino_2026]: https://doi.org/10.2514/6.2026-5098
[research_amirkabirian_bertin_1986]: https://doi.org/10.2514/6.1986-389
[research_ammendola_kedir_2025]: https://doi.org/10.1016/j.ceramint.2025.04.293
[research_amrutha_harikumar_2018]: https://doi.org/10.1109/icetietr.2018.8529093
[research_an_guo_2020]: https://doi.org/10.1016/j.ast.2020.106110
[research_an_huang_2026]: https://doi.org/10.1016/j.ast.2025.111564
[research_an_li_2021]: https://doi.org/10.1360/sspma-2021-0135
[research_an_wang_2017]: https://doi.org/10.1016/j.actaastro.2017.06.026
[research_an_wang_2021]: https://doi.org/10.1080/00207179.2021.1980824
[research_an_wang_2025]: https://doi.org/10.1061/jaeeez.aseng-6056
[research_an_wang_2025_b]: https://doi.org/10.1109/taes.2025.3548555
[research_an_xia_2017]: https://doi.org/10.1007/s11071-017-3347-y
[research_an_yuan_2023]: https://doi.org/10.1007/978-981-19-6613-2_80
[research_analysis_of_1982]: https://doi.org/10.2514/5.9781600865565.0430.0454
[research_analytical_characterization_1985]: https://doi.org/10.2514/5.9781600865718.0230.0253
[research_anbuselvan_reddy_2017]: https://doi.org/10.1007/978-3-319-44866-4_1
[research_anderson_1968]: https://doi.org/10.2514/3.4593
[research_anderson_1968_b]: https://doi.org/10.2514/3.4970
[research_anderson_johnd_1991]: https://doi.org/10.21236/ada233584
[research_anderson_jr_1988]: https://doi.org/10.21236/ada194265
[research_anderson_kinzel_2023]: https://doi.org/10.2514/6.2023-0391
[research_anderson_loewenson_2021]: https://doi.org/10.2514/6.2021-2798
[research_anderson_schultz_1967]: https://doi.org/10.2514/6.1967-136
[research_andersonjr_1968]: https://doi.org/10.2514/6.1968-164
[research_anin_2011]: https://doi.org/10.1080/19934270.2011.578452
[research_antipova_chezganov_2012]: https://doi.org/10.7463/1112.0499873
[research_appar_kumar_2021]: https://doi.org/10.1080/10618562.2021.2017900
[research_appar_kumar_2022]: https://doi.org/10.1063/5.0082783
[research_appar_kumar_2025]: https://doi.org/10.1016/j.compfluid.2025.106637
[research_appartaim_mezonlin_2001]: https://doi.org/10.2514/6.2001-1799
[research_appleby_adams_1991]: https://doi.org/10.2514/6.1991-2689
[research_appleton_1964]: https://doi.org/10.2514/3.2729
[research_application_of_2025]: https://doi.org/10.61552/jibi.2025.03.002
[research_approximate_analysis_1986]: https://doi.org/10.2514/6.1986-2132
[research_aprovitola_iuspa_2019]: https://doi.org/10.5772/intechopen.85603
[research_arabshahi_2021]: https://doi.org/10.2514/6.2021-1075
[research_arai_inoue_2019]: https://doi.org/10.1016/j.ceramint.2019.05.065
[research_arai_matsumoto_2026]: https://doi.org/10.2514/6.2026-2538
[research_arai_taguchi_2008]: https://doi.org/10.2514/6.2008-2579
[research_araujooliveira_barbosa_2023]: https://doi.org/10.26678/abcm.diname2023.din2023-0072
[research_arc_heated_facilities_2002]: https://doi.org/10.2514/5.9781600866678.0375.0403
[research_archer_sworder_1977]: https://doi.org/10.1109/cdc.1977.271657
[research_archer_sworder_1979]: https://doi.org/10.2514/3.55848
[research_ardema_1972]: https://doi.org/10.2514/3.50272
[research_arjun_2010]: https://doi.org/10.14741/ijcet/spl.2.2014.85
[research_aronov_klyagin_2021]: https://doi.org/10.34759/tpt-2021-13-10-456-466
[research_arora_2002]: https://doi.org/10.2514/6.2002-5466
[research_arora_ananthasayanam_2003]: https://doi.org/10.2514/6.2003-5547
[research_arora_balaji_2024]: https://doi.org/10.1007/978-981-97-6732-8_11
[research_ashford_1965]: https://doi.org/10.1017/s000192400005908x
[research_ashwinganesh_john_2018]: https://doi.org/10.1016/j.actaastro.2017.11.003
[research_asma_vanderhaegen_2010]: https://doi.org/10.2514/6.2010-4963
[research_aso_nakao_1992]: https://doi.org/10.1007/978-3-642-77648-9_104
[research_assessment_of_1983]: https://doi.org/10.2514/5.9781600865626.0300.0324
[research_atesmen_2023]: https://doi.org/10.1115/1.886786_ch4
[research_atkins_2026]: https://doi.org/10.2514/6.2026-115362
[research_au_scheyhing_1969]: https://doi.org/10.1520/stp49834s
[research_auman_wilks_2003]: https://doi.org/10.2514/6.2003-3417
[research_austin_jacobs_2003]: https://doi.org/10.21914/anziamj.v44i0.671
[research_autenrieb_2023]: https://doi.org/10.2514/6.2023-1997
[research_autenrieb_fezans_2024]: https://doi.org/10.1007/s12567-024-00544-0
[research_autenrieb_fezans_2025]: https://doi.org/10.2514/6.2025-1908
[research_autenrieb_gruhn_2025]: https://doi.org/10.2514/6.2025-2265
[research_autenrieb_gruhn_2026]: https://doi.org/10.2514/1.g009588
[research_automatic_re_entry_1962]: https://doi.org/10.2514/5.9781600864827.0271.0308
[research_avallone_greco_2013]: https://doi.org/10.1080/17686733.2013.800697
[research_avalos_castellanos_2022]: https://doi.org/10.12783/asc37/36429
[research_azad_2008]: https://doi.org/10.1016/b978-1-59749-281-2.00002-0
[research_b_2011]: https://doi.org/10.5772/13890
[research_babineaux_1966]: https://doi.org/10.2514/6.1966-29
[research_bachman_hyde_2021]: https://doi.org/10.2514/6.2021-0838
[research_backman_gild_2024]: https://doi.org/10.1016/j.oceram.2024.100563
[research_backman_graham_2024]: https://doi.org/10.1007/s11085-024-10247-w
[research_bade_1962]: https://doi.org/10.1063/1.1706589
[research_bade_1975]: https://doi.org/10.1063/1.861259
[research_bahambari_khankalantary_2023]: https://doi.org/10.1109/icee59167.2023.10334860
[research_bahlman_swartz_2013]: https://doi.org/10.1098/rsif.2012.0794
[research_bahmanzohuri_patrickmcdaniel_2019]: https://doi.org/10.17265/1934-8975/2019.05.002
[research_bai_guo_2015]: https://doi.org/10.1109/icma.2015.7237733
[research_bai_hu_2024]: https://doi.org/10.1007/978-981-97-2116-0_22
[research_bai_huo_2025]: https://doi.org/10.1007/978-981-95-4472-1_20
[research_bai_lian_2013]: https://doi.org/10.1109/imccc.2013.354
[research_bai_ren_2014]: https://doi.org/10.1109/chicc.2014.6896993
[research_bai_zhang_2011]: https://doi.org/10.1007/s11771-011-0833-0
[research_baidya_pesyridis_2018]: https://doi.org/10.3390/app8040574
[research_bailet_denis_2021]: https://doi.org/10.2514/1.a34969
[research_bailey_1966]: https://doi.org/10.21236/ad0633278
[research_bailey_2020]: https://doi.org/10.1007/978-3-030-20707-6_91-1
[research_bairstow_barton_2007]: https://doi.org/10.2514/6.2007-6427
[research_baiweijie_shengyongzhi_2019]: https://doi.org/10.3233/faia190278
[research_bajpai_jagadeesh_2023]: https://doi.org/10.2514/6.2023-3096
[research_baker_kramer_1979]: https://doi.org/10.2514/6.1979-201
[research_baker_kramer_1982]: https://doi.org/10.21236/ada114013
[research_baker_munson_2004]: https://doi.org/10.2514/6.2004-4316
[research_balakrishnan_kurian_2014]: https://doi.org/10.2514/1.a32712
[research_balakrishnan_shen_1997]: https://doi.org/10.2514/6.1997-3531
[research_balbirnie_sheporaitis_1975]: https://doi.org/10.2514/6.1975-1127
[research_balbo_sciti_2008]: https://doi.org/10.1016/j.msea.2007.01.164
[research_balland_fernandezvillace_2015]: https://doi.org/10.2514/6.2015-3557
[research_baluragi_gupta_2011]: https://doi.org/10.1007/s12666-011-0073-x
[research_banerjee_2019]: https://doi.org/10.2514/1.c034888
[research_banerjee_nabi_2017]: https://doi.org/10.1109/rast.2017.8002982
[research_banerjee_padhi_2017]: https://doi.org/10.2514/6.2017-1266
[research_bano_fraser_2026]: https://doi.org/10.2514/6.2026-5113
[research_bansal_feldick_2012]: https://doi.org/10.2514/6.2012-650
[research_bao_ding_2019]: https://doi.org/10.23940/ijpe.19.02.p4.387396
[research_bao_li_2020]: https://doi.org/10.1088/1742-6596/1584/1/012067
[research_bao_wang_2021]: https://doi.org/10.1016/j.cja.2020.11.009
[research_bao_wang_2023]: https://doi.org/10.1016/j.ast.2023.108219
[research_bao_zhang_2023]: https://doi.org/10.1007/978-981-19-6613-2_231
[research_bao_zhu_2024]: https://doi.org/10.3390/app14135367
[research_baradell_mclellan_1963]: https://doi.org/10.2514/6.1963-1424
[research_barber_coxjr_1988]: https://doi.org/10.2514/6.1988-475
[research_baron_efrat_1979]: https://doi.org/10.21236/ada068819
[research_barr_figueroa_2026]: https://doi.org/10.2514/6.2026-1691
[research_barrett_2025]: https://doi.org/10.12783/ballistics25/37108
[research_bartusiak_hao_2022]: https://doi.org/10.1109/aero53065.2022.9843362
[research_bartusiak_jacobs_2023]: https://doi.org/10.1109/aero55745.2023.10115826
[research_bartusiak_jacobs_2024]: https://doi.org/10.1109/taes.2023.3335895
[research_barz_2026]: https://doi.org/10.2514/6.2026-5022
[research_bastosjr_2019]: https://doi.org/10.1080/00207179.2019.1644538
[research_battistini_menegaz_2017]: https://doi.org/10.1109/aero.2017.7943795
[research_bauer_kummer_1965]: https://doi.org/10.2514/6.1965-1527
[research_bauer_kummer_1966]: https://doi.org/10.2514/3.28683
[research_baxter_arthur_1965]: https://doi.org/10.1017/s000192400006070x
[research_bayramov_gasanov_2020]: https://doi.org/10.20998/2522-9052.2020.4.03
[research_baysal_luo_1999]: https://doi.org/10.2514/2.2499
[research_beall_henderson_2017]: https://doi.org/10.1109/aero.2017.7943643
[research_beauthier_mahajan_2014]: https://doi.org/10.1201/b17488-98
[research_bebyakov_2013]: https://doi.org/10.18287/1998-6629-2013-0-1(39)-26-38
[research_becker_1964]: https://doi.org/10.2514/6.1964-551
[research_becker_baradell_1962]: https://doi.org/10.1007/978-3-7091-5470-0_2
[research_becker_robben_1973]: https://doi.org/10.2514/6.1973-691
[research_bedarev_fedorova_2001]: https://doi.org/10.1007/978-3-642-56535-9_130
[research_bedrov_vadichin_1966]: https://doi.org/10.1007/978-1-4899-6411-3_37
[research_beers_waters_2013]: https://doi.org/10.2514/6.2013-5529
[research_bell_1965]: https://doi.org/10.21236/ad0631590
[research_bell_hung_1962]: https://doi.org/10.4271/620320
[research_belov_borovoy_1999]: https://doi.org/10.2514/6.1999-3739
[research_benay_2003]: https://doi.org/10.2514/6.2003-6966
[research_bendor_1963]: https://doi.org/10.2514/3.1700
[research_benson_wells_2025]: https://doi.org/10.2514/6.2025-97548
[research_benton_1990]: https://doi.org/10.2514/6.1990-297
[research_berens_bissinger_1998]: https://doi.org/10.2514/6.1998-1574
[research_beresh_2022]: https://doi.org/10.2172/2006213
[research_bergen_chan_2024]: https://doi.org/10.2514/6.2024-0669
[research_berger_2009]: https://doi.org/10.2514/1.39247
[research_berger_greene_2008]: https://doi.org/10.2514/1.38722
[research_berger_greene_2009]: https://doi.org/10.2514/1.43927
[research_berlin_tedeschi_1989]: https://doi.org/10.2514/3.10251
[research_bernhart_1995]: https://doi.org/10.1533/9780857093219.7
[research_berry_berger_2015]: https://doi.org/10.2514/6.2015-0213
[research_berry_kammeyer_1993]: https://doi.org/10.2514/6.1993-510
[research_bertelrud_kolodziej_1992]: https://doi.org/10.2514/6.1992-4104
[research_berthelot_craft_2026]: https://doi.org/10.2514/6.2026-112174
[research_bertin_cummings_2006]: https://doi.org/10.1146/annurev.fluid.38.050304.092041
[research_bettis_hosder_2010]: https://doi.org/10.2514/6.2010-4642
[research_bhagwandin_martin_2023]: https://doi.org/10.2514/6.2023-3848
[research_bhat_lind_2009]: https://doi.org/10.1109/acc.2009.5160180
[research_bhatta_leonard_2004]: https://doi.org/10.1109/cdc.2004.1429394
[research_bhungalia_zweber_2000]: https://doi.org/10.1115/detc2000/dac-14267
[research_bhutta_lewis_1992]: https://doi.org/10.2514/6.1992-366
[research_bianchi_nasuti_2011]: https://doi.org/10.2514/6.2011-2273
[research_bibeau_rubinstein_2000]: https://doi.org/10.2514/6.2000-4262
[research_bibin_vinayak_2013]: https://doi.org/10.4028/www.scientific.net/amm.367.222
[research_bikdash_sartor_1999]: https://doi.org/10.1016/s0967-0661(98)00188-9
[research_bilchenko_bilchenko_2017]: https://doi.org/10.1109/cnsa.2017.7973941
[research_bille_lorenz_2001]: https://doi.org/10.21236/ada385939
[research_bin_hongxin_2006]: https://doi.org/10.1109/chicc.2006.4346800
[research_binjiang_qi_2017]: https://doi.org/10.1016/j.ifacol.2017.08.464
[research_bird_1966]: https://doi.org/10.2514/3.3384
[research_bishop_2013]: https://doi.org/10.2514/6.2013-5126
[research_bishop_dicristina_1967]: https://doi.org/10.2514/6.1967-1126
[research_bissinger_blagoveshchensky_1998]: https://doi.org/10.1016/s1270-9638(99)80009-1
[research_bissinger_schmitz_1996]: https://doi.org/10.2514/6.1996-4532
[research_blachowicz_2003]: https://doi.org/10.2478/bf02475559
[research_blankson_1992]: https://doi.org/10.1115/92-gt-437
[research_blankson_1994]: https://doi.org/10.1115/1.2906779
[research_blankson_hagseth_1993]: https://doi.org/10.2514/6.1993-506
[research_blankson_lewis_1998]: https://doi.org/10.2514/6.1998-1550
[research_blaschke_hummel_1999]: https://doi.org/10.1007/978-3-663-10901-3_8
[research_blevins_holehouse_1993]: https://doi.org/10.2514/3.46441
[research_bliamis_menelaou_2023]: https://doi.org/10.1016/j.ast.2023.108141
[research_block_gesslerjr_1990]: https://doi.org/10.2514/6.1990-3832
[research_blore_musal_1965]: https://doi.org/10.2514/3.3086
[research_blosser_blankson_1994]: https://doi.org/10.2514/6.1994-379
[research_blosser_blankson_1995]: https://doi.org/10.2514/3.46717
[research_blum_1969]: https://doi.org/10.21236/ad0701801
[research_blum_1971]: https://doi.org/10.1109/taes.1971.310363
[research_blum_2006]: https://doi.org/10.21236/ada448163
[research_bo_xiaoge_2025]: https://doi.org/10.1016/j.applthermaleng.2025.128575
[research_boehrk_dittert_2012]: https://doi.org/10.2514/6.2012-5919
[research_boeingscientificresearchlabsseattlewa_1963]: https://doi.org/10.21236/ad0414555
[research_boensch_goesch_1968]: https://doi.org/10.2514/6.1968-1088
[research_bogart_breckenridge_1981]: https://doi.org/10.21236/ada106728
[research_bogdonoff_1968]: https://doi.org/10.2514/6.1968-5
[research_bogdonoff_1999]: https://doi.org/10.21236/ada370547
[research_bogucz_dirik_1988]: https://doi.org/10.2514/6.1988-3771
[research_bohn_1967]: https://doi.org/10.1145/1465611.1465628
[research_bohrk_dittert_2014]: https://doi.org/10.2514/1.a32892
[research_boland_hinkle_2023]: https://doi.org/10.2514/6.2023-3694
[research_bolender_doman_2005]: https://doi.org/10.2514/6.2005-6255
[research_bolender_doman_2005_b]: https://doi.org/10.21236/ada444974
[research_bolender_doman_2006]: https://doi.org/10.2514/6.2006-6646
[research_bolender_wilkin_2009]: https://doi.org/10.2514/6.2009-7292
[research_bollino_oppenheimer_2006]: https://doi.org/10.2514/6.2006-6691
[research_bollino_ross_2006]: https://doi.org/10.2514/6.2006-6074
[research_bollino_ross_2007]: https://doi.org/10.1109/acc.2007.4282500
[research_boman_elias_1990]: https://doi.org/10.2514/6.1990-1759
[research_bonavita_zollars_2026]: https://doi.org/10.2514/1.c038065
[research_bond_morris_2000]: https://doi.org/10.2514/2.2616
[research_bond_morris_2001]: https://doi.org/10.2514/2.2759
[research_bond_morris_2006]: https://doi.org/10.2514/1.428
[research_bonelli_cutrone_2011]: https://doi.org/10.2514/6.2011-2319
[research_bonifacio_borreca_2006]: https://doi.org/10.2514/6.2006-7910
[research_bonin_kliche_2017]: https://doi.org/10.2514/6.2017-1611
[research_boost_vehicle_1964]: https://doi.org/10.2514/5.9781600864889.0523.0544
[research_boppe_davis_1989]: https://doi.org/10.4271/892345
[research_borg_adamczak_2025]: https://doi.org/10.2514/6.2025-0733
[research_borovoj_kubyshina_1993]: https://doi.org/10.2514/6.1993-5050
[research_borovoy_egorov_2015]: https://doi.org/10.1051/eucass/201507419
[research_borrelli_marini_1998]: https://doi.org/10.2514/6.1998-1577
[research_bouchez_montazel_1998]: https://doi.org/10.2514/6.1998-1589
[research_boudali_orjuela_2019]: https://doi.org/10.1080/00423114.2019.1638516
[research_bowcutt_1992]: https://doi.org/10.2514/6.1992-5055
[research_bowcutt_2018]: https://doi.org/10.2514/6.2018-5373
[research_bowcutt_haney_1995]: https://doi.org/10.2514/6.1995-850
[research_bowden_brown_2023]: https://doi.org/10.1029/2023sw003563
[research_bowersox_fan_2000]: https://doi.org/10.21236/ada384726
[research_bowles_roberts_1998]: https://doi.org/10.2514/6.1998-1610
[research_boyd_padilla_2003]: https://doi.org/10.2514/6.2003-7062
[research_boyer_1965]: https://doi.org/10.21236/ad0621447
[research_boylan_1965]: https://doi.org/10.21236/ad0460154
[research_bradley_siemersiii_1981]: https://doi.org/10.2514/6.1981-2477
[research_brady_levensteins_1964]: https://doi.org/10.2514/6.1964-44
[research_brandis_johnston_2014]: https://doi.org/10.2514/6.2014-2374
[research_brauckmann_1986]: https://doi.org/10.2514/6.1986-271
[research_brazhko_davletkildeev_2020]: https://doi.org/10.1615/tsagiscij.2020034055
[research_breezapaulose_jisjose_2016]: https://doi.org/10.17577/ijertv5is040928
[research_breitner_pesch_1994]: https://doi.org/10.1007/978-1-4612-0245-5_4
[research_breitsamter_laschka_2001]: https://doi.org/10.2514/6.2001-1811
[research_brinda_dasgupta_2006]: https://doi.org/10.2514/6.2006-7997
[research_brindha_das_2026]: https://doi.org/10.1063/5.0340438
[research_britcher_landman_2024]: https://doi.org/10.1016/b978-0-12-818099-0.00009-4
[research_broadaway_1984]: https://doi.org/10.2514/6.1984-85
[research_brociek_hetmaniok_2023]: https://doi.org/10.1016/j.applthermaleng.2022.119405
[research_broglio_1961]: https://doi.org/10.21236/ad0294976
[research_broglio_1962]: https://doi.org/10.1007/978-3-7091-5470-0_15
[research_brown_brown_2009]: https://doi.org/10.1109/radar.2009.4977123
[research_brown_chou_2026]: https://doi.org/10.2514/6.2026-5049
[research_browning_1993]: https://doi.org/10.2514/6.1993-1994
[research_brune_hosder_2015]: https://doi.org/10.2514/6.2015-3581
[research_brune_hosder_2016]: https://doi.org/10.2514/6.2016-3535
[research_brune_hosder_2017]: https://doi.org/10.2514/1.a33732
[research_brune_west_2017]: https://doi.org/10.2514/6.2017-2373
[research_brunner_lu_2007]: https://doi.org/10.2514/6.2007-6777
[research_brunner_lu_2008]: https://doi.org/10.2514/1.35055
[research_brunner_lu_2010]: https://doi.org/10.2514/6.2010-8307
[research_bryson_denham_1962]: https://doi.org/10.2514/8.6166
[research_bryson_vasile_2018]: https://doi.org/10.2514/6.2018-3158
[research_bu_bao_2008]: https://doi.org/10.4028/0-87849-473-1.1791
[research_bu_hua_2023]: https://doi.org/10.1109/taes.2023.3251314
[research_bu_jiang_2022]: https://doi.org/10.1007/s11071-022-07430-6
[research_bu_jiang_2022_b]: https://doi.org/10.1109/taes.2022.3153429
[research_bu_jiang_2023]: https://doi.org/10.1109/jmass.2023.3242304
[research_bu_jiang_2023_b]: https://doi.org/10.1109/tfuzz.2022.3217378
[research_bu_jiang_2023_c]: https://doi.org/10.1109/tits.2022.3224424
[research_bu_lei_2019]: https://doi.org/10.1016/j.actaastro.2019.05.039
[research_bu_lv_2023]: https://doi.org/10.1109/tcyb.2023.3255925
[research_bu_ma_2023]: https://doi.org/10.1007/s11071-023-09085-3
[research_bu_qi_2022]: https://doi.org/10.1109/tfuzz.2021.3089031
[research_bu_wu_2015]: https://doi.org/10.1016/j.neucom.2014.11.040
[research_buchanan_crosby_1983]: https://doi.org/10.21236/ada136439
[research_bukva_christopher_2020]: https://doi.org/10.2514/6.2020-2456
[research_bulirsch_chudej_1992]: https://doi.org/10.1016/s1474-6670(17)49692-3
[research_bulirsch_chudej_1993]: https://doi.org/10.1016/b978-0-08-041715-8.50070-5
[research_burchfield_bontrager_1966]: https://doi.org/10.21236/ad0481634
[research_burdun_parfentyev_1998]: https://doi.org/10.2514/6.1998-4976
[research_burke_rumpfkeil_2025]: https://doi.org/10.2514/6.2025-0480
[research_burnett_1993]: https://doi.org/10.2514/6.1993-4190
[research_burnett_lewis_1993]: https://doi.org/10.2514/6.1993-404
[research_burns_2020]: https://doi.org/10.2172/1829235
[research_burt_josyula_2012]: https://doi.org/10.2514/6.2012-224
[research_buschek_calise_1997]: https://doi.org/10.2514/2.4031
[research_busing_1964]: https://doi.org/10.1016/b978-0-08-011007-3.50012-3
[research_butler_benitez_2022]: https://doi.org/10.2514/6.2022-1905
[research_butler_benitez_2023]: https://doi.org/10.2514/6.2023-1539
[research_butler_king_1991]: https://doi.org/10.2514/6.1991-199
[research_butler_winter_2016]: https://doi.org/10.2514/6.2016-1516
[research_butsko_1966]: https://doi.org/10.2514/6.1966-991
[research_butt_2013]: https://doi.org/10.21307/ijssis-2017-560
[research_butt_yan_2010]: https://doi.org/10.1109/cdc.2010.5717701
[research_butt_yan_2011]: https://doi.org/10.1002/asjc.450
[research_butt_yan_2011_b]: https://doi.org/10.3182/20110828-6-it-1002.00534
[research_butt_yan_2013]: https://doi.org/10.1080/00207721.2013.828798
[research_buyanbaatar_ishikawa_2022]: https://doi.org/10.1007/978-981-19-2689-1_55
[research_byczkowski_rao_2023]: https://doi.org/10.2514/6.2023-1168
[research_byczkowski_rao_2023_b]: https://doi.org/10.2514/6.2023-1168.c1
[research_byczkowski_rao_2024]: https://doi.org/10.2514/6.2024-1457
[research_byczkowski_rao_2026]: https://doi.org/10.1007/s40295-026-00589-9
[research_bykerk_verstraete_2020]: https://doi.org/10.1016/j.ast.2020.105709
[research_bykerk_verstraete_2020_b]: https://doi.org/10.1016/j.ast.2019.105531
[research_bykerk_verstraete_2020_c]: https://doi.org/10.1016/j.ast.2020.105883
[research_bykerk_verstraete_2020_d]: https://doi.org/10.1016/j.ast.2020.106228
[research_byrne_sturgis_1996]: https://doi.org/10.2514/6.1996-3438
[research_byrom_allen_1994]: https://doi.org/10.1080/01495739408946270
[research_cabrera_west_2026]: https://doi.org/10.2514/1.a36431
[research_cai_duan_2010]: https://doi.org/10.3969/j.issn.1004-4132.2010.03.018
[research_cai_jianmei_2013]: https://doi.org/10.2514/6.2013-4525
[research_cai_ni_2024]: https://doi.org/10.15541/jim20230562
[research_cai_song_2013]: https://doi.org/10.1177/0954410013486239
[research_cai_song_2014]: https://doi.org/10.1177/0954410014555894
[research_cai_wei_2026]: https://doi.org/10.1007/s42064-026-0316-6
[research_cai_wu_2011]: https://doi.org/10.3969/j.issn.1004-4132.2011.01.006
[research_cai_zhuang_2025]: https://doi.org/10.1016/j.dt.2024.11.001
[research_caledonia_krech_1994]: https://doi.org/10.21236/ada281452
[research_calise_bae_1987]: https://doi.org/10.2514/6.1987-2568
[research_calise_bae_1988]: https://doi.org/10.23919/acc.1988.4789866
[research_calise_bae_1990]: https://doi.org/10.2514/3.25377
[research_callsen_wilken_2024]: https://doi.org/10.1007/s12567-024-00583-7
[research_campbell_caram_1996]: https://doi.org/10.2514/6.1996-1862
[research_candler_leyva_2022]: https://doi.org/10.1080/08929882.2022.2145777
[research_candler_subbareddy_2015]: https://doi.org/10.2514/5.9781624103292.0203.0238
[research_cangelosi_heinkenschloss_2024]: https://doi.org/10.2514/6.2024-0375
[research_canto_raga_2011]: https://doi.org/10.1111/j.1365-2966.2011.19574.x
[research_cao_dong_2026]: https://doi.org/10.1016/j.cja.2026.104143
[research_cao_zhang_2007]: https://doi.org/10.1007/978-3-540-75995-9_86
[research_cao_zhang_2015]: https://doi.org/10.1109/icspcc.2015.7338798
[research_caogen_hongjun_2008]: https://doi.org/10.1016/j.actaastro.2007.12.059
[research_capriotti_1987]: https://doi.org/10.2514/6.1987-272
[research_carbonaro_1993]: https://doi.org/10.1007/978-94-011-1828-6_29
[research_cardone_2007]: https://doi.org/10.3166/qirt.4.233-251
[research_carlomagno_luca_1993]: https://doi.org/10.1007/978-94-011-1828-6_44
[research_carlson_1999]: https://doi.org/10.2514/2.3511
[research_carman_jb_1966]: https://doi.org/10.21236/ad0632514
[research_carney_2018]: https://doi.org/10.1016/b978-0-12-803581-8.09996-3
[research_carpman_kelly_2025]: https://doi.org/10.5006/ed2025-00057
[research_carr_1966]: https://doi.org/10.2514/6.1966-758
[research_carr_lagimoniere_2013]: https://doi.org/10.2514/6.2013-4647
[research_carr_rexius_2012]: https://doi.org/10.2514/6.2012-3081
[research_carroll_brandis_2023]: https://doi.org/10.2514/6.2023-0208
[research_carson_epstein_2006]: https://doi.org/10.1109/acc.2006.1657647
[research_carter_1965]: https://doi.org/10.2514/6.1965-48
[research_carter_kuruvila_2005]: https://doi.org/10.21236/ada455794
[research_caruntu_negrea_2008]: https://doi.org/10.2298/jac0801001c
[research_cas_baranger_2026]: https://doi.org/10.2514/6.2026-4756
[research_cassabaum_schmitt_2000]: https://doi.org/10.1117/12.408572
[research_cassanto_1966]: https://doi.org/10.2514/3.28728
[research_cassanto_monfort_1977]: https://doi.org/10.2514/3.57210
[research_cassell_allen_2011]: https://doi.org/10.2514/6.2011-3330
[research_cavallo_demaria_1996]: https://doi.org/10.2514/6.1996-3703
[research_cavesmith_bhatt_2026]: https://doi.org/10.2514/6.2026-1165
[research_cecere_2026]: https://doi.org/10.21741/9781644904299-2
[research_center_sobieczky_1991]: https://doi.org/10.2514/6.1991-1697
[research_cfd_optimization_1994]: https://doi.org/10.2514/6.1994-2951
[research_chadalavada_deshmukh_2026]: https://doi.org/10.2514/6.2026-1376
[research_chadwick_2000]: https://doi.org/10.2514/6.2000-2441
[research_chai_fang_2015]: https://doi.org/10.1016/j.ast.2015.09.004
[research_chai_tsourdos_2020]: https://doi.org/10.1016/j.actaastro.2020.06.051
[research_chander_krishna_2013]: https://doi.org/10.14429/dsj.63.3733
[research_chander_krishna_2013_b]: https://doi.org/10.14429/dsj.63.4207
[research_chandler_2019]: https://doi.org/10.2514/6.2019-4148
[research_chang_huang_2022]: https://doi.org/10.3390/aerospace10010001
[research_chang_xiao_2023]: https://doi.org/10.1016/j.ast.2023.108699
[research_changbao_hui_2020]: https://doi.org/10.1088/1757-899x/751/1/012078
[research_changsheng_wuxing_2006]: https://doi.org/10.1109/chicc.2006.4347462
[research_chao_cheng_2026]: https://doi.org/10.1109/taes.2026.3716640
[research_chao_jeng_1965]: https://doi.org/10.1115/1.3689076
[research_chao_qi_2022]: https://doi.org/10.1016/j.jfranklin.2022.05.011
[research_chao_qi_2022_b]: https://doi.org/10.1016/j.ast.2022.108006
[research_chao_shihua_2014]: https://doi.org/10.1109/cgncc.2014.7007534
[research_chao_wang_2010]: https://doi.org/10.1109/isscaa.2010.5633153
[research_chao_xinyu_2015]: https://doi.org/10.1016/j.proeng.2014.12.577
[research_chaosong_guorongzhao_2011]: https://doi.org/10.1109/iccrd.2011.5763877
[research_chapter_13_2013]: https://doi.org/10.1615/978-1-56700-309-3.236
[research_chapter_14_2013]: https://doi.org/10.1615/978-1-56700-309-3.261
[research_chapter_6_2013]: https://doi.org/10.1615/978-1-56700-309-3.153
[research_characteristics_of_2002]: https://doi.org/10.2514/5.9781600866678.0239.0253
[research_chase_mckinney_2005]: https://doi.org/10.2514/6.2005-6745
[research_chauffour_lewis_2003]: https://doi.org/10.2514/6.2003-7060
[research_chauffour_lewis_2004]: https://doi.org/10.2514/6.2004-3405
[research_chaumette_cretenet_1987]: https://doi.org/10.1016/0094-5765(87)90127-5
[research_chauvet_brouquet_2005]: https://doi.org/10.4271/2005-01-2856
[research_chavez_schmidt_1994]: https://doi.org/10.2514/3.21349
[research_chawbingchang_athans_1977]: https://doi.org/10.1109/tac.1977.1101412
[research_chawla_sarmah_2010]: https://doi.org/10.1016/j.ast.2010.04.001
[research_che_tang_2008]: https://doi.org/10.1016/j.ast.2008.01.008
[research_cheah_bhattacharjee_2025]: https://doi.org/10.2514/1.g008331
[research_chen_1958]: https://doi.org/10.1115/1.4012730
[research_chen_1958_b]: https://doi.org/10.1115/1.4012732
[research_chen_2016]: https://doi.org/10.1016/j.ijheatmasstransfer.2015.12.031
[research_chen_2016_b]: https://doi.org/10.1016/j.ast.2016.03.028
[research_chen_2017]: https://doi.org/10.2514/6.2017-2174
[research_chen_2017_b]: https://doi.org/10.1109/iccss.2017.8091423
[research_chen_2019]: https://doi.org/10.2514/6.2019-3837
[research_chen_2021]: https://doi.org/10.1117/12.2611407
[research_chen_2023]: https://doi.org/10.13168/cs.2023.0026
[research_chen_ai_2014]: https://doi.org/10.1615/heatpipescietech.v5.i1-4.590
[research_chen_cao_2021]: https://doi.org/10.2514/1.a34813
[research_chen_chen_2014]: https://doi.org/10.4028/www.scientific.net/amr.912-914.427
[research_chen_chen_2016]: https://doi.org/10.2514/6.2016-1252
[research_chen_chen_2016_b]: https://doi.org/10.1109/cgncc.2016.7829058
[research_chen_du_2016]: https://doi.org/10.1360/n972016-00194
[research_chen_du_2020]: https://doi.org/10.1155/2020/4905698
[research_chen_fan_2025]: https://doi.org/10.26599/tst.2024.9010018
[research_chen_fu_2014]: https://doi.org/10.1109/cgncc.2014.7007264
[research_chen_fu_2015]: https://doi.org/10.1155/2015/648231
[research_chen_fu_2019]: https://doi.org/10.1109/smc.2019.8914599
[research_chen_gao_2016]: https://doi.org/10.1109/chicc.2016.7554180
[research_chen_gong_2019]: https://doi.org/10.1002/rnc.4711
[research_chen_guo_2019]: https://doi.org/10.1109/access.2019.2907806
[research_chen_guo_2023]: https://doi.org/10.1007/978-981-19-6613-2_538
[research_chen_han_2020]: https://doi.org/10.5772/intechopen.84655
[research_chen_han_2026]: https://doi.org/10.1063/5.0306269
[research_chen_he_2025]: https://doi.org/10.1177/16878132251348391
[research_chen_hou_2011]: https://doi.org/10.1016/j.compfluid.2011.03.011
[research_chen_huang_2021]: https://doi.org/10.1016/j.ast.2020.106418
[research_chen_huang_2025]: https://doi.org/10.1088/1402-4896/ae26e2
[research_chen_jing_2018]: https://doi.org/10.1109/icmae.2018.8467711
[research_chen_li_2026]: https://doi.org/10.1016/j.cja.2025.103924
[research_chen_lin_2023]: https://doi.org/10.1007/978-981-19-6613-2_346
[research_chen_liu_2006]: https://doi.org/10.2514/6.2006-777
[research_chen_liu_2013]: https://doi.org/10.1016/j.proeng.2013.12.015
[research_chen_liu_2015]: https://doi.org/10.1016/j.cja.2015.06.024
[research_chen_liu_2015_b]: https://doi.org/10.2514/6.2015-3670
[research_chen_lu_2025]: https://doi.org/10.1109/cac67268.2025.11487931
[research_chen_ma_2017]: https://doi.org/10.1177/1729881417705674
[research_chen_ma_2018]: https://doi.org/10.1093/imamci/dny012
[research_chen_mao_2026]: https://doi.org/10.1063/5.0335632
[research_chen_milos_1996]: https://doi.org/10.2514/6.1996-615
[research_chen_ni_2017]: https://doi.org/10.2514/6.2017-2338
[research_chen_niu_2018]: https://doi.org/10.1109/access.2018.2820008
[research_chen_pei_2021]: https://doi.org/10.3390/aerospace8050124
[research_chen_pei_2022]: https://doi.org/10.1038/s41598-022-10063-9
[research_chen_shen_2020]: https://doi.org/10.1155/2020/7503272
[research_chen_shen_2020_b]: https://doi.org/10.3390/s20185418
[research_chen_speyer_2008]: https://doi.org/10.2514/6.2008-6492
[research_chen_starkey_2009]: https://doi.org/10.21236/ada590178
[research_chen_sun_2023]: https://doi.org/10.1007/978-981-19-6613-2_84
[research_chen_tseng_2011]: https://doi.org/10.1109/fuzzy.2011.6007437
[research_chen_wan_2005]: https://doi.org/10.2514/6.2005-3269
[research_chen_wan_2016]: https://doi.org/10.1007/s11431-016-0009-9
[research_chen_wang_2021]: https://doi.org/10.23919/ccc52363.2021.9550242
[research_chen_wang_2021_b]: https://doi.org/10.23919/ccc52363.2021.9550729
[research_chen_wang_2023]: https://doi.org/10.1007/978-981-19-6613-2_114
[research_chen_wang_2023_b]: https://doi.org/10.1007/978-981-19-6613-2_710
[research_chen_wei_2020]: https://doi.org/10.1109/itnec48623.2020.9084777
[research_chen_williamson_2006]: https://doi.org/10.2514/1.19361
[research_chen_wu_2018]: https://doi.org/10.2514/6.2018-4835
[research_chen_xia_2022]: https://doi.org/10.3390/aerospace9120835
[research_chen_xiong_2018]: https://doi.org/10.5772/intechopen.70659
[research_chen_xu_2005]: https://doi.org/10.2514/6.2005-3270
[research_chen_yang_2025]: https://doi.org/10.34133/space.0260
[research_chen_zeng_2022]: https://doi.org/10.1631/jzus.a2100133
[research_chen_zhang_2018]: https://doi.org/10.5772/intechopen.70658
[research_chen_zhang_2025]: https://doi.org/10.1016/j.ast.2025.110056
[research_chen_zhang_2026]: https://doi.org/10.2514/1.g009289
[research_chen_zhao_2020]: https://doi.org/10.1515/ijnsns-2019-0290
[research_chen_zhou_2019]: https://doi.org/10.1016/j.ast.2019.05.041
[research_chen_zhou_2020]: https://doi.org/10.1007/978-981-15-8901-0_9
[research_chen_zhou_2020_b]: https://doi.org/10.1007/978-981-15-8901-0_4
[research_chen_zhou_2020_c]: https://doi.org/10.1007/978-981-15-8901-0_5
[research_chen_zhou_2020_d]: https://doi.org/10.1007/978-981-15-8901-0_8
[research_chen_zhou_2020_e]: https://doi.org/10.1007/978-981-15-8901-0_10
[research_chen_zhou_2020_f]: https://doi.org/10.1007/978-981-15-8901-0_7
[research_chen_zhou_2020_g]: https://doi.org/10.1007/978-981-15-8901-0_6
[research_chen_zhou_2020_h]: https://doi.org/10.1007/978-981-15-8901-0_3
[research_chen_zhou_2020_i]: https://doi.org/10.1007/978-981-15-8901-0_11
[research_chen_zhou_2020_j]: https://doi.org/10.1007/978-981-15-8901-0_17
[research_chen_zhou_2020_k]: https://doi.org/10.1007/978-981-15-8901-0_13
[research_chen_zhou_2020_l]: https://doi.org/10.1007/978-981-15-8901-0_16
[research_chen_zhou_2020_m]: https://doi.org/10.1007/978-981-15-8901-0_12
[research_chen_zhou_2020_n]: https://doi.org/10.1016/j.ast.2020.105679
[research_chen_zhou_2026]: https://doi.org/10.1016/j.ceramint.2026.06.382
[research_chen_zhu_2016]: https://doi.org/10.1109/chicc.2016.7555061
[research_chen_zhu_2022]: https://doi.org/10.1109/icus55513.2022.9987017
[research_chen_zhu_2025]: https://doi.org/10.23919/ccc64809.2025.11179204
[research_chenchen_cunfenggu_2015]: https://doi.org/10.1049/cp.2015.1003
[research_cheng_1965]: https://doi.org/10.1016/s1474-6670(17)69125-0
[research_cheng_1966]: https://doi.org/10.1007/978-1-4899-6411-3_38
[research_cheng_chen_2020]: https://doi.org/10.1016/j.ast.2019.105608
[research_cheng_chen_2021]: https://doi.org/10.1016/j.actaastro.2020.11.034
[research_cheng_fang_2024]: https://doi.org/10.1117/12.3024624
[research_cheng_li_2013]: https://doi.org/10.2514/1.j051750
[research_cheng_li_2014]: https://doi.org/10.1155/2014/412718
[research_cheng_li_2023]: https://doi.org/10.1007/978-981-19-6613-2_652
[research_cheng_shen_2025]: https://doi.org/10.1007/978-981-96-2204-7_22
[research_cheng_sheng_2016]: https://doi.org/10.1109/chicc.2016.7555053
[research_cheng_shui_2019]: https://doi.org/10.1109/icus48101.2019.8996086
[research_cheng_song_2024]: https://doi.org/10.1016/j.ast.2023.108855
[research_cheng_song_2025]: https://doi.org/10.1109/taes.2024.3449247
[research_cheng_wang_2018]: https://doi.org/10.1109/ccdc.2018.8407688
[research_cheng_wang_2019]: https://doi.org/10.1016/j.ast.2019.01.041
[research_cheng_wang_2025]: https://doi.org/10.1063/5.0308839
[research_cheng_wei_2023]: https://doi.org/10.1007/978-981-99-0479-2_223
[research_cheng_williamsiii_1974]: https://doi.org/10.1615/ihtc5.1740
[research_cheng_yan_2019]: https://doi.org/10.1051/jnwpu/20193761102
[research_cheng_yan_2021]: https://doi.org/10.1016/j.ast.2021.106529
[research_cheng_yang_2011]: https://doi.org/10.4028/www.scientific.net/amr.338.325
[research_cheng_yi_2025]: https://doi.org/10.1007/978-981-96-2240-5_58
[research_cheng_zhang_2017]: https://doi.org/10.1109/ccdc.2017.7978467
[research_chengbinlian_zhangren_2012]: https://doi.org/10.1049/cp.2012.1300
[research_chenhao_naigang_2019]: https://doi.org/10.1109/icsidp47821.2019.9173491
[research_cheninewd_olynick_1995]: https://doi.org/10.2514/6.1995-2081
[research_chernyi_1961]: https://doi.org/10.1016/b978-1-4832-3197-6.50011-3
[research_chernyi_1961_b]: https://doi.org/10.1016/b978-1-4832-3197-6.50008-3
[research_chernyi_gonor_1973]: https://doi.org/10.1007/978-94-010-2559-1_11
[research_chetverushkin_polyakov_2006]: https://doi.org/10.1016/b978-044452206-1/50035-5
[research_chevalier_bouchez_1996]: https://doi.org/10.2514/6.1996-4554
[research_chi_wang_2021]: https://doi.org/10.23919/ccc52363.2021.9550037
[research_chi_zhou_2021]: https://doi.org/10.23919/ccc52363.2021.9549361
[research_chiesa_grassi_2005]: https://doi.org/10.2514/6.2005-3346
[research_chin_hearne_1964]: https://doi.org/10.2514/6.1964-1311
[research_ching_blonigan_2024]: https://doi.org/10.2514/6.2024-1293
[research_chinnaraj_kim_2023]: https://doi.org/10.3390/ma16103717
[research_chirayath_bindu_2014]: https://doi.org/10.1109/epscicon.2014.6887480
[research_cho_jo_2021]: https://doi.org/10.1007/s42405-020-00348-6
[research_cho_kim_2017]: https://doi.org/10.1007/978-3-319-65283-2_30
[research_choi_gamba_2026]: https://doi.org/10.2514/6.2026-5096
[research_choi_loucks_2022]: https://doi.org/10.5139/jksas.2022.50.12.877
[research_choi_moon_2023]: https://doi.org/10.1016/j.infrared.2023.104959
[research_chou_shen_1996]: https://doi.org/10.2514/6.1996-2892
[research_chow_1966]: https://doi.org/10.2514/3.55299
[research_chow_1967]: https://doi.org/10.2514/3.4250
[research_chow_elassar_1970]: https://doi.org/10.2514/6.1970-181
[research_chpoun_1990]: https://doi.org/10.1007/978-3-642-84103-3_48
[research_chu_chunwang_2023]: https://doi.org/10.1007/978-981-19-6613-2_398
[research_chu_li_2017]: https://doi.org/10.1051/matecconf/201711401002
[research_chu_li_2017_b]: https://doi.org/10.2991/icmeit-17.2017.130
[research_chu_mooij_2008]: https://doi.org/10.2514/6.2008-6212
[research_chuang_morimoto_1996]: https://doi.org/10.2514/6.1996-3876
[research_chuang_morimoto_1997]: https://doi.org/10.2514/2.3205
[research_chuanzhen_peng_2021]: https://doi.org/10.2514/1.c036122
[research_chuanzhen_xufei_2022]: https://doi.org/10.1016/j.actaastro.2022.08.004
[research_chuanzhen_xufei_2022_b]: https://doi.org/10.2514/1.j060706
[research_chudej_1993]: https://doi.org/10.1007/978-3-0348-7539-4_23
[research_chudej_bulirsch_1993]: https://doi.org/10.2514/6.1993-5130
[research_chudej_pesch_2009]: https://doi.org/10.1007/978-0-387-95857-6_8
[research_chudoba_haney_2015]: https://doi.org/10.1017/s0001924000010241
[research_chue_cresci_2009]: https://doi.org/10.1007/978-3-540-85181-3_25
[research_chun_1991]: https://doi.org/10.1007/978-3-642-76527-8_67
[research_chung_lee_2006]: https://doi.org/10.1109/sice.2006.314762
[research_cinquegrana_pezzella_2015]: https://doi.org/10.1007/bf03404698
[research_clapp_1965]: https://doi.org/10.2514/6.1965-492
[research_clapp_young_2015]: https://doi.org/10.2514/6.2015-2165
[research_clark_1969]: https://doi.org/10.2514/3.5359
[research_clark_cunnington_1993]: https://doi.org/10.1016/0894-1777(93)90228-b
[research_clark_mirmirani_2006]: https://doi.org/10.2514/6.2006-6560
[research_clarke_2008]: https://doi.org/10.21236/ada500739
[research_clegg_rodi_2019]: https://doi.org/10.2514/6.2019-2813
[research_clegg_rodi_2020]: https://doi.org/10.2514/6.2020-2405
[research_cliff_well_1992]: https://doi.org/10.2514/6.1992-4301
[research_clutter_suppression_2017]: https://doi.org/10.21629/jsee.2017.03.08
[research_cockrell_1994]: https://doi.org/10.2514/3.46616
[research_cockrelljr_1993]: https://doi.org/10.2514/6.1993-2921
[research_cockrellsejr_huebner_1995]: https://doi.org/10.2514/6.1995-736
[research_cole_aroesty_1965]: https://doi.org/10.2514/3.3185
[research_colgren_keshmiri_2009]: https://doi.org/10.2514/1.35644
[research_colosimo_1968]: https://doi.org/10.2514/6.1968-380
[research_colville_lewis_2003]: https://doi.org/10.2514/6.2003-7040
[research_colwell_2023]: https://doi.org/10.1615/ihpc1990v1.500
[research_compton_blanchard_1979]: https://doi.org/10.2514/6.1979-257
[research_compton_findlay_1981]: https://doi.org/10.2514/6.1981-2459
[research_computation_of_1988]: https://doi.org/10.2514/6.1988-175
[research_computational_fluid_1990]: https://doi.org/10.2514/5.9781600865985.0817.0838
[research_cong_kunfeng_2017]: https://doi.org/10.23919/chicc.2017.8027876
[research_connolly_2026]: https://doi.org/10.2514/6.2026-5112
[research_copeland_palacios_2014]: https://doi.org/10.2514/6.2014-0513
[research_coras_paull_2006]: https://doi.org/10.2514/6.2006-7981
[research_corda_andersonjr_1988]: https://doi.org/10.2514/6.1988-369
[research_cornick_robertson_2023]: https://doi.org/10.2514/6.2023-1786
[research_coulter_huang_2023]: https://doi.org/10.2514/1.c036980
[research_coulter_wang_2021]: https://doi.org/10.2514/6.2021-0715
[research_coupled_dynamic_2018]: https://doi.org/10.21629/jsee.2018.06.15
[research_cousin_1967]: https://doi.org/10.2514/6.1967-451
[research_couture_dechamplain_2008]: https://doi.org/10.2514/6.2008-5171
[research_covell_wood_1988]: https://doi.org/10.2514/6.1988-4505
[research_covington_balboni_2004]: https://doi.org/10.2514/6.2004-2273
[research_covington_heinemann_2008]: https://doi.org/10.2514/1.12403
[research_covington_heinemann_2008_b]: https://doi.org/10.2514/1.38249
[research_covington_heinemann_2008_c]: https://doi.org/10.2514/1.40598
[research_cramer_bradt_1988]: https://doi.org/10.2514/6.1988-4123
[research_cremaschi_2012]: https://doi.org/10.1007/978-1-4614-4469-5_7
[research_cristillo_scigliano_2019]: https://doi.org/10.1115/imece2019-10577
[research_cui_fu_2010]: https://doi.org/10.4028/www.scientific.net/amm.40-41.15
[research_cui_han_2026]: https://doi.org/10.1016/j.ast.2026.112009
[research_cui_hu_2013]: https://doi.org/10.1007/s11431-013-5288-0
[research_cui_hu_2013_b]: https://doi.org/10.2514/6.2013-233
[research_cui_hu_2022]: https://doi.org/10.1007/978-981-16-6640-7_2
[research_cui_li_2026]: https://doi.org/10.1002/acs.70086
[research_cui_wei_2022]: https://doi.org/10.5220/0011917200003612
[research_cui_yang_2009]: https://doi.org/10.2514/6.2009-7400
[research_cui_zhang_2013]: https://doi.org/10.1109/tencon.2013.6718477
[research_cui_zhao_2007]: https://doi.org/10.1007/s10409-007-0069-2
[research_cui_zhao_2022]: https://doi.org/10.1016/j.cja.2021.11.025
[research_cui_zhen_2024]: https://doi.org/10.1016/j.ast.2024.109218
[research_cui_zhen_2025]: https://doi.org/10.1002/rnc.8012
[research_culler_williams_2007]: https://doi.org/10.2514/6.2007-6395
[research_cummings_2022]: https://doi.org/10.2514/6.2022-0023
[research_cunningham_1987]: https://doi.org/10.2514/3.25879
[research_cutrone_2023]: https://doi.org/10.21741/9781644902813-36
[research_cutrone_schettino_2024]: https://doi.org/10.1007/s42496-024-00201-z
[research_cvrlje_1999]: https://doi.org/10.2514/6.1999-3412
[research_cygan_wozniak_2025]: https://doi.org/10.1016/j.ceramint.2025.11.108
[research_czysz_froning_1997]: https://doi.org/10.2514/6.1997-3394
[research_dabas_sheikh_2025]: https://doi.org/10.52202/083092-0073
[research_dacosta_rolim_2016]: https://doi.org/10.26678/abcm.encit2016.cit2016-0657
[research_dacosta_sachs_2005]: https://doi.org/10.2514/6.2005-3272
[research_dai_cai_2026]: https://doi.org/10.3390/aerospace13030283
[research_dai_fang_2024]: https://doi.org/10.1109/cac63892.2024.10864489
[research_dai_wang_2016]: https://doi.org/10.1109/radar.2016.8059177
[research_dai_xia_2016]: https://doi.org/10.1109/icit.2016.7475036
[research_dai_xia_2016_b]: https://doi.org/10.1109/ispdc.2016.67
[research_dai_yan_2020]: https://doi.org/10.1016/j.ast.2020.105703
[research_dai_yang_2025]: https://doi.org/10.1007/978-981-96-2208-5_39
[research_dajun_guobiao_2006]: https://doi.org/10.2514/6.iac-06-c2.p.2.05
[research_dalle_driscoll_2012]: https://doi.org/10.2514/6.2012-4958
[research_dalle_frendreis_2010]: https://doi.org/10.2514/6.2010-7930
[research_dalle_torrez_2011]: https://doi.org/10.2514/6.2011-2368
[research_dalle_torrez_2011_b]: https://doi.org/10.2514/6.2011-6300
[research_dalle_torrez_2014]: https://doi.org/10.2514/1.c032617
[research_damato_notaro_2022]: https://doi.org/10.3390/aerospace9120841
[research_damico_simon_2004]: https://doi.org/10.2514/6.2004-2294
[research_dan_xi_2022]: https://doi.org/10.1109/cac57257.2022.10055988
[research_dang_li_2021]: https://doi.org/10.1177/0954410021994984
[research_daniel_milton_1980]: https://doi.org/10.2514/6.1980-1587
[research_danushdatthathireyan_balaji_2025]: https://doi.org/10.1007/978-3-031-73816-6_56
[research_daoguangtang_huiwang_2016]: https://doi.org/10.1109/cgncc.2016.7828999
[research_das_chawla_2009]: https://doi.org/10.2514/6.2009-6275
[research_das_pei_2023]: https://doi.org/10.1088/1742-6596/2633/1/012005
[research_das_wang_2024]: https://doi.org/10.1049/icp.2024.0657
[research_davidosigthorsson_2006]: https://doi.org/10.1109/med.2006.235983
[research_davies_wilson_1984]: https://doi.org/10.2514/6.1984-1711
[research_davis_1966]: https://doi.org/10.2514/6.1966-990
[research_davis_1969]: https://doi.org/10.2514/6.1969-27
[research_dawei_2011]: https://doi.org/10.1109/icecc.2011.6066635
[research_dean_robertson_2023]: https://doi.org/10.2514/6.2023-2364
[research_debardelaben_dehay_2022]: https://doi.org/10.2514/6.2022-0368
[research_dec_mitcheltree_2002]: https://doi.org/10.2514/6.2002-910
[research_dechant_wagnild_2020]: https://doi.org/10.2514/6.2020-1807
[research_decker_2010]: https://doi.org/10.2514/6.2010-5071
[research_decker_laschka_2001]: https://doi.org/10.2514/6.2001-1852
[research_deep_jagadeesh_2018]: https://doi.org/10.1063/1.5046191
[research_deepak_ray_2006]: https://doi.org/10.2514/6.2006-7998
[research_deepak_ray_2008]: https://doi.org/10.2514/1.33826
[research_defilippis_kerr_2016]: https://doi.org/10.1007/978-3-319-23986-6_7
[research_defilippis_savino_2005]: https://doi.org/10.2514/6.2005-3277
[research_degelsmith_freaner_1993]: https://doi.org/10.2514/6.1993-2419
[research_degeyter_1973]: https://doi.org/10.1007/978-94-010-2559-1_38
[research_degeyter_smolderen_1974]: https://doi.org/10.1016/b978-0-12-398150-9.50038-9
[research_degregoria_2015]: https://doi.org/10.21236/ad1003573
[research_dejarnette_1992]: https://doi.org/10.1007/978-1-4612-0375-9_1
[research_dejarnette_hamilton_2008]: https://doi.org/10.2514/6.2008-1261
[research_demoura_ribeiro_2026]: https://doi.org/10.1007/s42401-026-00510-0
[research_demoura_ribeiro_2026_b]: https://doi.org/10.1016/j.ast.2026.112481
[research_demoura_ribeiro_2026_c]: https://doi.org/10.1016/j.ast.2025.110869
[research_dendy_hayes_2026]: https://doi.org/10.2514/6.2026-112635
[research_deng_2026]: https://doi.org/10.1088/1742-6596/3240/1/012025
[research_deng_jiao_2017]: https://doi.org/10.2514/1.a33729
[research_deng_wu_2016]: https://doi.org/10.1109/cgncc.2016.7829007
[research_deng_xu_2025]: https://doi.org/10.1088/1742-6596/2977/1/012007
[research_deng_zhao_2025]: https://doi.org/10.1109/icmtae66890.2025.11428105
[research_deng_zhao_2026]: https://doi.org/10.1088/1742-6596/3207/1/012079
[research_depasquale_francillout_2009]: https://doi.org/10.1109/aero.2009.4839703
[research_depena_rolph_1986]: https://doi.org/10.1007/978-94-009-3385-9_92
[research_deprisco_mungiguerra_2026]: https://doi.org/10.1016/j.jeurceramsoc.2026.118184
[research_deqing_yiyin_2019]: https://doi.org/10.1109/icus48101.2019.8996033
[research_deqing_yiyin_2021]: https://doi.org/10.1007/978-981-15-8155-7_41
[research_derienzo_pallone_1967]: https://doi.org/10.2514/3.3942
[research_derienzo_pallone_1967_b]: https://doi.org/10.2514/3.55354
[research_derollez_cleach_2021]: https://doi.org/10.1109/aero50100.2021.9438259
[research_desai_brahmachary_2019]: https://doi.org/10.1061/(asce)as.1943-5525.0001085
[research_desai_knocke_2004]: https://doi.org/10.2514/6.2004-5092
[research_design_considerations_1963]: https://doi.org/10.2514/5.9781600864834.0761.0782
[research_design_construction_and_2008]: https://doi.org/10.5139/jksas.2008.36.4.321
[research_design_of_1993]: https://doi.org/10.2514/6.1993-401
[research_devanna_bof_2022]: https://doi.org/10.3390/en15082811
[research_development_and_2004]: https://doi.org/10.5139/jksas.2004.32.3.124
[research_devirgilio_wells_1973]: https://doi.org/10.2514/6.1973-891
[research_devita_viola_2015]: https://doi.org/10.2514/6.2015-3540
[research_dewell_speyer_1993]: https://doi.org/10.2514/6.1993-3753
[research_deyang_kun_2016]: https://doi.org/10.2514/6.2016-3229
[research_deyst_gustafson_1971]: https://doi.org/10.2514/6.1971-914
[research_deyst_gustafson_1972]: https://doi.org/10.2514/3.30394
[research_dezaiacomo_kerr_2009]: https://doi.org/10.2514/6.2009-5771
[research_diao_lu_2022]: https://doi.org/10.5220/0012010400003612
[research_dickeson_rodriguez_2009]: https://doi.org/10.2514/6.2009-6281
[research_diclemente_marini_2006]: https://doi.org/10.2514/6.iac-06-d2.6.08
[research_diclemente_marini_2009]: https://doi.org/10.1016/j.actaastro.2009.01.069
[research_diclemente_marini_2011]: https://doi.org/10.2514/6.2011-2259
[research_dicristina_1979]: https://doi.org/10.21236/ada065645
[research_diebold_scahill_1985]: https://doi.org/10.1007/978-94-009-4932-4_30
[research_digiorgio_quagliarella_2019]: https://doi.org/10.1016/j.ast.2018.09.042
[research_dijkstra_mooij_2013]: https://doi.org/10.2514/6.2013-4501
[research_dilley_nerem_1969]: https://doi.org/10.2514/6.1969-183
[research_ding_guo_2016]: https://doi.org/10.1109/cgncc.2016.7829000
[research_ding_jiang_2016]: https://doi.org/10.1142/9789814740135_0052
[research_ding_li_2023]: https://doi.org/10.2174/9789815050028123040003
[research_ding_liu_2015]: https://doi.org/10.1016/j.actaastro.2015.02.016
[research_ding_liu_2015_b]: https://doi.org/10.1115/gt2015-43934
[research_ding_liu_2018]: https://doi.org/10.1016/j.actaastro.2018.09.002
[research_ding_shen_2015]: https://doi.org/10.1016/j.actaastro.2014.11.038
[research_ding_shen_2015_b]: https://doi.org/10.1177/0954410015581404
[research_ding_wang_2019]: https://doi.org/10.1016/j.ast.2019.06.032
[research_ding_wu_2020]: https://doi.org/10.1109/iciba50161.2020.9276902
[research_ding_xu_2025]: https://doi.org/10.3390/drones9030223
[research_ding_yue_2022]: https://doi.org/10.1016/j.cja.2021.10.037
[research_ding_zhou_2023]: https://doi.org/10.1109/icmee59781.2023.10525275
[research_dinkelmann_wchter_2002]: https://doi.org/10.1076/mcmd.8.3.237.14098
[research_direct_numerical_2023]: https://doi.org/10.1063/5.0146651
[research_dix_golden_1967]: https://doi.org/10.21236/ad0813708
[research_djanalmann_murugan_2025]: https://doi.org/10.2514/6.2025-2632
[research_dobrov_karpenko_2023]: https://doi.org/10.1016/j.actaastro.2022.09.044
[research_dodge_lindorfer_2026]: https://doi.org/10.2514/6.2026-4428
[research_dolan_1970]: https://doi.org/10.2514/6.1970-277
[research_dolan_edighoffer_1966]: https://doi.org/10.2514/3.28551
[research_donaldson_ireland_2017]: https://doi.org/10.2514/6.2017-2379
[research_dong_cai_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000727
[research_dong_chao_2012]: https://doi.org/10.2514/6.2012-5896
[research_dong_chao_2012_b]: https://doi.org/10.2514/6.2012-5881
[research_dong_guo_2021]: https://doi.org/10.1155/2021/3676810
[research_dong_huang_2023]: https://doi.org/10.23919/ccc58697.2023.10239805
[research_dong_jiang_2023]: https://doi.org/10.1016/j.ress.2023.109253
[research_dong_jiang_2024]: https://doi.org/10.1016/j.engappai.2024.107968
[research_dong_jiang_2025]: https://doi.org/10.1109/icphm65385.2025.11061823
[research_dong_li_2023]: https://doi.org/10.1002/rnc.6722
[research_dong_liu_2020]: https://doi.org/10.1016/j.isatra.2019.06.011
[research_dong_wang_2014]: https://doi.org/10.1109/cgncc.2014.7007476
[research_dong_wu_2025]: https://doi.org/10.1016/j.ifacol.2025.11.391
[research_dong_xie_2024]: https://doi.org/10.1016/j.actaastro.2024.08.057
[research_dong_xu_2022]: https://doi.org/10.3390/aerospace9120840
[research_dong_zhao_2025]: https://doi.org/10.1007/978-981-96-2244-3_24
[research_dongdong_xun_2026]: https://doi.org/10.1007/978-981-96-4652-4_74
[research_doolan_2006]: https://doi.org/10.2514/6.2006-222
[research_doriano_savino_2018]: https://doi.org/10.1108/aeat-06-2015-0151
[research_doronzo_2026]: https://doi.org/10.4236/aast.2026.113005
[research_dou_shen_2013]: https://doi.org/10.4028/www.scientific.net/amm.433-435.1979
[research_dou_su_2017]: https://doi.org/10.1016/j.ast.2017.04.024
[research_douglas_lindgren_1999]: https://doi.org/10.21236/ada361137
[research_doustdar_mardani_2018]: https://doi.org/10.1108/aeat-07-2016-0108
[research_drag_of_1986]: https://doi.org/10.2514/5.9781600865770.0044.0059
[research_draper_lanejr_1977]: https://doi.org/10.2514/6.1977-1165
[research_drawin_1993]: https://doi.org/10.1002/chin.199320293
[research_dreyer_grier_2021]: https://doi.org/10.2514/1.c035969
[research_drougge_1965]: https://doi.org/10.1016/b978-0-08-011860-4.50042-2
[research_dsc_attracts_2011]: https://doi.org/10.1016/s0969-4765(11)70098-4
[research_dsm_acquires_2011]: https://doi.org/10.1016/s0969-6210(11)70157-6
[research_dsouza_kinney_2014]: https://doi.org/10.2514/6.2014-0387
[research_dsouza_kinney_2019]: https://doi.org/10.2514/6.2019-0015
[research_dsouza_molder_1971]: https://doi.org/10.2514/6.1971-85
[research_dsouza_sarigulklijn_2008]: https://doi.org/10.2514/6.2008-230
[research_dsouza_sarigulklijn_2008_b]: https://doi.org/10.2514/6.2008-7804
[research_dsouza_sarigulklijn_2012]: https://doi.org/10.2514/6.2012-4508
[research_du_li_2026]: https://doi.org/10.1088/1742-6596/3207/1/012059
[research_du_qi_2024]: https://doi.org/10.2991/978-94-6463-518-8_9
[research_du_wan_2017]: https://doi.org/10.2514/6.2017-1938
[research_du_wang_2023]: https://doi.org/10.23919/ccc58697.2023.10240184
[research_duan_li_2012]: https://doi.org/10.1007/s11431-012-5036-x
[research_duan_li_2015]: https://doi.org/10.1109/taes.2014.120654
[research_duan_roviranavarro_2016]: https://doi.org/10.2514/6.2016-5444
[research_duan_sun_2010]: https://doi.org/10.1109/pcspa.2010.247
[research_duan_sun_2011]: https://doi.org/10.1109/ccdc.2011.5968400
[research_duan_xu_2024]: https://doi.org/10.1088/1742-6596/2820/1/012040
[research_duan_zhang_2016]: https://doi.org/10.1109/wcica.2016.7578837
[research_duan_zhao_2026]: https://doi.org/10.2514/1.j066092
[research_duan_zhong_2010]: https://doi.org/10.1109/icca.2010.5524360
[research_dubey_mukhopadhyay_2020]: https://doi.org/10.1201/9780429319631-16
[research_duboismatra_bishop_2003]: https://doi.org/10.2514/6.2003-5446
[research_dudar_timoshenko_2025]: https://doi.org/10.1007/978-981-96-4599-2_13
[research_dudin_ledovskiy_2013]: https://doi.org/10.1051/eucass/201305379
[research_dudin_ledovskiy_2020]: https://doi.org/10.1615/tsagiscij.2021037829
[research_dudin_neiland_1980]: https://doi.org/10.1007/bf01089967
[research_dulikravich_lee_1990]: https://doi.org/10.2514/6.1990-3073
[research_dulikravich_sheffer_1992]: https://doi.org/10.2514/6.1992-2635
[research_duncan_1968]: https://doi.org/10.1007/978-3-642-50082-4_6
[research_dunning_2016]: https://doi.org/10.1061/9780784479919.036
[research_duran_zeng_2026]: https://doi.org/10.2514/6.2026-109216
[research_duret_fabrizi_1999]: https://doi.org/10.1016/s0094-5765(99)00090-9
[research_dusinberre_1958]: https://doi.org/10.1115/1.4012731
[research_duston_seghi_2004]: https://doi.org/10.21236/ada461309
[research_dutta_braun_2010]: https://doi.org/10.2514/6.2010-1210
[research_dyakonov_schoenenberger_2012]: https://doi.org/10.2514/6.2012-2999
[research_eakins_jayaseelan_2010]: https://doi.org/10.1007/s11661-010-0540-8
[research_ebrahimi_roshanian_2011]: https://doi.org/10.4028/www.scientific.net/amm.110-116.4765
[research_edquist_2006]: https://doi.org/10.2514/6.2006-6137
[research_edquist_lewis_1993]: https://doi.org/10.2514/6.1993-403
[research_edwards_babikian_1987]: https://doi.org/10.2514/6.1987-1520
[research_effects_of_1986]: https://doi.org/10.2514/5.9781600865770.0416.0442
[research_eggers_silvester_2009]: https://doi.org/10.2514/6.2009-7256
[research_eggersohmeyerd_nickel_1995]: https://doi.org/10.2514/6.1995-6091
[research_ehsan_castellanos_2026]: https://doi.org/10.2514/6.2026-4714
[research_eickmans_2015]: https://doi.org/10.1007/978-3-319-15982-9_51
[research_eisler_hull_1993]: https://doi.org/10.2514/3.21020
[research_eisler_hull_1994]: https://doi.org/10.2514/3.21251
[research_eklund_2004]: https://doi.org/10.2514/6.2004-5950
[research_elkebir_ornik_2020]: https://doi.org/10.2514/6.2020-2412
[research_ellinwood_1970]: https://doi.org/10.2514/3.29870
[research_elliott_hankey_1968]: https://doi.org/10.2514/3.29503
[research_elmnefi_2026]: https://doi.org/10.2339/politeknik.1856487
[research_elsen_legresley_2008]: https://doi.org/10.1016/j.jcp.2008.08.023
[research_emery_devos_2006]: https://doi.org/10.1063/1.2372745
[research_engel_putnam_2024]: https://doi.org/10.2514/6.2024-1173
[research_engel_putnam_2025]: https://doi.org/10.2514/1.a35925
[research_engel_skolnik_2021]: https://doi.org/10.2514/6.2021-0933
[research_enmi_qian_2018]: https://doi.org/10.1051/eucass/201810105
[research_erdem_yang_2009]: https://doi.org/10.2514/6.2009-7347
[research_ericsson_1970]: https://doi.org/10.1016/b978-0-08-006931-9.50031-3
[research_ericsson_1978]: https://doi.org/10.2514/6.1978-1181
[research_ericsson_1979]: https://doi.org/10.2514/3.61181
[research_ermakov_kryukov_2017]: https://doi.org/10.1088/1742-6596/815/1/012016
[research_erwin_1990]: https://doi.org/10.2514/6.1990-3815
[research_erwin_bernstein_2005]: https://doi.org/10.21236/ada439012
[research_escher_ehrlic_2000]: https://doi.org/10.2514/6.2000-5602
[research_evans_walton_2017]: https://doi.org/10.1016/j.apm.2017.07.024
[research_ewans_collins_2024]: https://doi.org/10.1115/omae2024-126998
[research_ewenzrocher_hermann_2022]: https://doi.org/10.2514/1.j061159
[research_external_flows_1977]: https://doi.org/10.2514/5.9781600865251.0349.0359
[research_external_flows_1977_b]: https://doi.org/10.2514/5.9781600865251.0361.0377
[research_eyi_2013]: https://doi.org/10.2514/6.2013-3977
[research_eyi_hanquist_2018]: https://doi.org/10.2514/6.2018-3108
[research_eyi_hanquist_2019]: https://doi.org/10.2514/1.t5523
[research_eyi_yumusak_2012]: https://doi.org/10.2514/6.2012-5827
[research_eyi_yumusak_2014]: https://doi.org/10.1080/0305215x.2014.933822
[research_fahrenholtz_hilmas_2009]: https://doi.org/10.21236/ada495056
[research_fahrenholtz_hilmas_2017]: https://doi.org/10.1016/j.scriptamat.2016.10.018
[research_fahy_koo_2019]: https://doi.org/10.33599/nasampe/c.19.0775
[research_fain_lambert_2026]: https://doi.org/10.2514/6.2026-5087
[research_fairfax_vasile_2020]: https://doi.org/10.2514/6.2020-0021
[research_falempin_lacaze_1995]: https://doi.org/10.2514/6.1995-6008
[research_falkiewicz_cesnik_2009]: https://doi.org/10.2514/6.2009-6284
[research_falkiewicz_cesnik_2010]: https://doi.org/10.2514/6.2010-7928
[research_falkiewicz_cesnik_2011]: https://doi.org/10.2514/1.j050802
[research_falkiewicz_frendreis_2011]: https://doi.org/10.2514/6.2011-6378
[research_famularo_valasek_2016]: https://doi.org/10.2514/6.2016-1865
[research_fan_bai_2021]: https://doi.org/10.1109/access.2021.3117704
[research_fan_bai_2022]: https://doi.org/10.1007/978-981-16-6640-7_3
[research_fan_bai_2023]: https://doi.org/10.1109/icmae59650.2023.10424679
[research_fan_bai_2024]: https://doi.org/10.1109/taes.2024.3374712
[research_fan_jiajun_2021]: https://doi.org/10.1049/cje.2021.07.003
[research_fan_liu_2009]: https://doi.org/10.2514/6.2009-7334
[research_fan_lu_2017]: https://doi.org/10.3390/app7020159
[research_fan_qi_2024]: https://doi.org/10.1049/icp.2024.0651
[research_fan_wu_2017]: https://doi.org/10.2514/6.2017-2111
[research_fan_zhu_2016]: https://doi.org/10.3390/app6100312
[research_fang_jiang_2024]: https://doi.org/10.1109/ccssta62096.2024.10691869
[research_fang_li_2024]: https://doi.org/10.3390/app14135924
[research_farajollahi_markazi_2010]: https://doi.org/10.1109/iccet.2010.5486075
[research_farmakovsky_vinogradova_2005]: https://doi.org/10.2514/6.2005-920
[research_fatemi_mooij_2005]: https://doi.org/10.2514/6.2005-3386
[research_fattahi_najafiershadi_2020]: https://doi.org/10.1016/j.ceramint.2020.03.003
[research_fay_kemp_1963]: https://doi.org/10.21236/ad0405723
[research_fedele_gardi_2020]: https://doi.org/10.1007/s12567-020-00312-w
[research_fedele_romagnoli_2014]: https://doi.org/10.1109/chicc.2014.6896120
[research_fedioun_orlik_2012]: https://doi.org/10.2514/6.2012-5864
[research_feie_kretz_2008]: https://doi.org/10.21236/ada488092
[research_feilden_glymond_2019]: https://doi.org/10.1016/j.ceramint.2019.05.032
[research_fenfen_xubo_2020]: https://doi.org/10.1109/ccdc49329.2020.9164687
[research_feng_2011]: https://doi.org/10.4028/www.scientific.net/amm.128-129.270
[research_feng_2022]: https://doi.org/10.1109/ccdc55256.2022.10033500
[research_feng_bai_2025]: https://doi.org/10.3390/aerospace12110956
[research_feng_feng_2025]: https://doi.org/10.3390/drones9030210
[research_feng_liu_2017]: https://doi.org/10.2514/6.2017-2173
[research_feng_long_2025]: https://doi.org/10.1063/5.0284681
[research_feng_lv_2020]: https://doi.org/10.1007/s42401-020-00069-4
[research_feng_tan_2017]: https://doi.org/10.23919/chicc.2017.8028225
[research_feng_tang_2014]: https://doi.org/10.1007/s11434-014-0534-9
[research_feng_wang_2019]: https://doi.org/10.1109/safeprocess45799.2019.9213331
[research_feng_wang_2022]: https://doi.org/10.1109/ccdc55256.2022.10034211
[research_feng_wu_2026]: https://doi.org/10.65904/3083-3450.2026.02.04
[research_feng_zhang_2016]: https://doi.org/10.2991/icamcs-16.2016.138
[research_fengli_chaowang_2016]: https://doi.org/10.1109/cgncc.2016.7829056
[research_fengyuan_huang_2017]: https://doi.org/10.2514/6.2017-2420
[research_ferguson_andersonjr_1993]: https://doi.org/10.2514/6.1993-505
[research_ferguson_dasque_2015]: https://doi.org/10.2514/6.2015-1008
[research_ferguson_dasque_2015_b]: https://doi.org/10.2514/6.2015-3839
[research_ferguson_dasque_2016]: https://doi.org/10.2514/6.2016-1663
[research_ferguson_dasque_2018]: https://doi.org/10.2514/6.2018-0637
[research_ferguson_dhanasar_2015]: https://doi.org/10.2514/6.2015-3508
[research_ferlemann_robinson_2000]: https://doi.org/10.2514/6.2000-2694
[research_ferraiuolo_manc_2011]: https://doi.org/10.5772/17141
[research_ferraiuolo_manca_2012]: https://doi.org/10.1016/j.ijthermalsci.2011.10.019
[research_ferretto_gori_2026]: https://doi.org/10.2514/6.2026-5145
[research_ferrier_fedioun_2006]: https://doi.org/10.2514/6.2006-8092
[research_ferrier_orlik_2008]: https://doi.org/10.2514/6.2008-2599
[research_filatov_1972]: https://doi.org/10.1007/bf01205371
[research_filipkovskyi_2026]: https://doi.org/10.15421/472606
[research_fink_1966]: https://doi.org/10.2514/3.3768
[research_finley_cockrell_1995]: https://doi.org/10.2514/6.1995-1831
[research_finzi_lavagna_2003]: https://doi.org/10.2514/6.2003-5441
[research_fiorentini_serrani_2007]: https://doi.org/10.2514/6.2007-6329
[research_fiorentini_serrani_2009]: https://doi.org/10.1109/acc.2009.5160211
[research_fiorentini_serrani_2012]: https://doi.org/10.1016/j.automatica.2012.04.006
[research_fischer_johanik_2023]: https://doi.org/10.2514/6.2023-0331
[research_fitzgerald_1974]: https://doi.org/10.1109/tac.1974.1100653
[research_florence_1979]: https://doi.org/10.2514/6.1979-1627
[research_florence_1981]: https://doi.org/10.2514/6.1981-1127
[research_florence_1981_b]: https://doi.org/10.2514/6.1981-350
[research_florence_1985]: https://doi.org/10.2514/3.25712
[research_florence_hiltz_1968]: https://doi.org/10.2514/6.1968-304
[research_florence_thibault_1978]: https://doi.org/10.2514/6.1978-861
[research_fogarty_1967]: https://doi.org/10.1109/pgec.1967.264609
[research_folk_ho_2001]: https://doi.org/10.2514/6.2001-121
[research_fomin_aulchenko_2010]: https://doi.org/10.1007/s10808-010-0068-0
[research_fong_ehrlich_1970]: https://doi.org/10.21236/ad0866735
[research_forbesspyratos_jahn_2014]: https://doi.org/10.2514/6.2014-2954
[research_forsythe_melfi_1961]: https://doi.org/10.21236/ad0672194
[research_foust_smith_2004]: https://doi.org/10.2514/6.2004-6000
[research_franze_barz_2025]: https://doi.org/10.1007/s12567-024-00588-2
[research_fratantoni_2001]: https://doi.org/10.21236/ada625213
[research_fratantoni_2001_b]: https://doi.org/10.21236/ada625172
[research_fratantoni_2002]: https://doi.org/10.21236/ada629092
[research_fratantoni_2002_b]: https://doi.org/10.21236/ada629088
[research_fratantoni_2003]: https://doi.org/10.21236/ada629472
[research_fratantoni_2003_b]: https://doi.org/10.21236/ada629474
[research_frayssinet_2019]: https://doi.org/10.2514/6.2019-3224
[research_freeborn_kinnersley_2005]: https://doi.org/10.1016/j.actaastro.2004.09.020
[research_friz_samareh_2020]: https://doi.org/10.2514/6.2020-4120
[research_froning_roach_2003]: https://doi.org/10.2514/6.2003-6906
[research_froning_roach_2003_b]: https://doi.org/10.2514/6.2003-205
[research_froningjr_mckinney_1996]: https://doi.org/10.2514/6.1996-4519
[research_froningjr_roach_1999]: https://doi.org/10.2514/6.1999-4878
[research_fruncillo_morani_2026]: https://doi.org/10.2514/6.2026-5047
[research_fu_gong_2026]: https://doi.org/10.1063/5.0323065
[research_fu_liu_2017]: https://doi.org/10.1177/1687814017726291
[research_fu_qu_2022]: https://doi.org/10.1016/j.ast.2022.107470
[research_fu_song_2024]: https://doi.org/10.1515/tjj-2024-0085
[research_fu_wan_2024]: https://doi.org/10.1590/jatm.v16.1355
[research_fu_wang_2019]: https://doi.org/10.1109/access.2019.2947297
[research_fu_weng_2020]: https://doi.org/10.2514/1.t5718
[research_fuhry_1999]: https://doi.org/10.2514/6.1999-4211
[research_fujii_inoue_1998]: https://doi.org/10.2514/2.3409
[research_fujii_inoue_1998_b]: https://doi.org/10.2514/6.1998-605
[research_fujii_watanabe_2000]: https://doi.org/10.2514/6.2000-267
[research_fujii_watanabe_2001]: https://doi.org/10.2514/2.3665
[research_fujio_taguchi_2026]: https://doi.org/10.1007/s12567-026-00722-2
[research_fujiwara_funase_2022]: https://doi.org/10.1109/aero53065.2022.9843229
[research_fukuda_araya_2017]: https://doi.org/10.1299/jsmemecj.2017.s1910103
[research_fukuzawa_iguchi_2025]: https://doi.org/10.52202/083090-0142
[research_fuller_blum_2008]: https://doi.org/10.1111/j.1551-2916.2008.02481.x
[research_fuller_sacks_2004]: https://doi.org/10.1023/b:jmsc.0000041685.85043.34
[research_fung_1953]: https://doi.org/10.2514/8.2773
[research_furey_1970]: https://doi.org/10.2514/6.1970-825
[research_furey_1972]: https://doi.org/10.2514/3.61637
[research_furfaro_wibben_2012]: https://doi.org/10.2514/6.2012-4435
[research_fusaro_ferretto_2019]: https://doi.org/10.1017/aer.2019.109
[research_fusaro_ferretto_2022]: https://doi.org/10.1016/j.actaastro.2022.05.034
[research_fusaro_ferretto_2022_b]: https://doi.org/10.2514/6.2022-3588
[research_fusaro_viola_2020]: https://doi.org/10.2514/6.2020-1106
[research_fusco_trinchese_2026]: https://doi.org/10.2514/6.2026-5024
[research_gabaldo_barros_2016]: https://doi.org/10.2514/6.2016-5323
[research_gai_baird_1985]: https://doi.org/10.2514/6.1985-973
[research_gaillard_benard_1999]: https://doi.org/10.1007/s003480050276
[research_galaktionov_lapygin_2006]: https://doi.org/10.2514/6.iac-06-d2.3.07
[research_gally_campbell_2002]: https://doi.org/10.2514/6.2002-3139
[research_gamble_young_1982]: https://doi.org/10.2514/6.1982-1335
[research_gang_min_2005]: https://doi.org/10.2514/6.2005-6131
[research_gangireddy_karlsdottir_2010]: https://doi.org/10.4028/www.scientific.net/kem.434-435.144
[research_gao_2000]: https://doi.org/10.1007/978-94-010-0894-5_8
[research_gao_2023]: https://doi.org/10.54254/2753-8818/11/20230391
[research_gao_ai_2026]: https://doi.org/10.3390/aerospace13050459
[research_gao_cai_2019]: https://doi.org/10.1109/access.2019.2936974
[research_gao_cao_2014]: https://doi.org/10.1109/cgncc.2014.7007436
[research_gao_chen_1997]: https://doi.org/10.2514/6.1997-3534
[research_gao_chen_2018]: https://doi.org/10.12783/dtcse/pcmm2018/23663
[research_gao_chen_2020]: https://doi.org/10.3390/app10082898
[research_gao_chen_2020_b]: https://doi.org/10.1016/j.conengprac.2020.104426
[research_gao_chen_2024]: https://doi.org/10.1080/21642583.2024.2364035
[research_gao_cui_2012]: https://doi.org/10.1007/s11434-011-4948-3
[research_gao_gou_2021]: https://doi.org/10.1016/j.compstruct.2021.113962
[research_gao_jia_2026]: https://doi.org/10.3390/aerospace13020170
[research_gao_jiang_2012]: https://doi.org/10.1007/s00034-011-9385-7
[research_gao_jiang_2015]: https://doi.org/10.1063/1.4921751
[research_gao_li_2014]: https://doi.org/10.1109/cgncc.2014.7007365
[research_gao_li_2024]: https://doi.org/10.1109/aaac63570.2024.11027380
[research_gao_liu_2026]: https://doi.org/10.2514/1.g009823
[research_gao_shi_2019]: https://doi.org/10.1109/ccdc.2019.8832559
[research_gao_sun_2019]: https://doi.org/10.1007/978-981-32-9686-2_14
[research_gao_wang_2013]: https://doi.org/10.1007/s11071-013-1135-x
[research_gao_wang_2013_b]: https://doi.org/10.1016/j.jfranklin.2013.02.012
[research_gao_wang_2013_c]: https://doi.org/10.1080/00207721.2013.771758
[research_gao_wang_2013_d]: https://doi.org/10.1109/icuas.2013.6564792
[research_gao_wu_2011]: https://doi.org/10.1007/978-3-642-25658-5_45
[research_gao_zhang_2018]: https://doi.org/10.1016/j.jfranklin.2017.12.007
[research_gaohua_jianmei_2014]: https://doi.org/10.1108/aeat-10-2012-0198
[research_garciallama_2007]: https://doi.org/10.2514/6.2007-6897
[research_garciallama_2011]: https://doi.org/10.2514/1.50798
[research_gardi_delvecchio_2015]: https://doi.org/10.2514/6.2015-3640
[research_garino_nisar_2024]: https://doi.org/10.3390/ceramics7040106
[research_garrard_2015]: https://doi.org/10.2514/6.2015-1784
[research_garvey_besnard_2003]: https://doi.org/10.2514/6.2003-6390
[research_garvine_1964]: https://doi.org/10.2514/3.2644
[research_garvine_1966]: https://doi.org/10.2514/3.3798
[research_garzon_2024]: https://doi.org/10.2514/6.2024-84586
[research_garzon_matisheck_2012]: https://doi.org/10.2514/6.2012-3258
[research_gasner_foster_1992]: https://doi.org/10.2514/6.1992-3721
[research_gazzaniga_palafox_2001]: https://doi.org/10.1016/s0003-4975(01)02582-6
[research_ge_wang_2017]: https://doi.org/10.1109/icras.2017.8071926
[research_gee_kellison_2025]: https://doi.org/10.1121/10.0040740
[research_geshele_polezhaev_2013]: https://doi.org/10.1134/s0018151x13050076
[research_ghaffari_luckring_1991]: https://doi.org/10.2514/3.46038
[research_ghori_narendar_2023]: https://doi.org/10.4028/p-oah3jt
[research_ghosh_ogawa_2022]: https://doi.org/10.2514/6.2022-2734
[research_ghosh_ogawa_2022_b]: https://doi.org/10.2514/6.2022-2734.c1
[research_ghosh_rao_2023]: https://doi.org/10.2514/6.2023-3051
[research_ghosh_rao_2025]: https://doi.org/10.1007/978-981-96-4771-2_44
[research_ghosh_subhash_2009]: https://doi.org/10.1016/j.scriptamat.2009.08.038
[research_giampetro_2026]: https://doi.org/10.2514/6.2026-110256
[research_giampetro_lindau_2026]: https://doi.org/10.2514/6.2026-4398
[research_gibbons_damm_2021]: https://doi.org/10.2514/6.2021-4141
[research_gibson_neidhoefer_2002]: https://doi.org/10.2514/6.2002-3462
[research_gillum_kammeyer_1994]: https://doi.org/10.2514/6.1994-384
[research_gillum_kammeyer_1994_b]: https://doi.org/10.2514/6.1994-2476
[research_gillum_lewis_1996]: https://doi.org/10.2514/6.1996-812
[research_girerd_barton_2000]: https://doi.org/10.2514/6.2000-3960
[research_giri_ghose_2010]: https://doi.org/10.1007/978-3-642-17563-3_2
[research_gislason_prahm_1983]: https://doi.org/10.1016/0004-6981(83)90070-7
[research_gladden_melis_1990]: https://doi.org/10.2514/6.1990-53
[research_gladden_melis_1994]: https://doi.org/10.1115/imece1994-1617
[research_glass_2008]: https://doi.org/10.2514/6.2008-2682
[research_glass_2018]: https://doi.org/10.2514/5.9781624104893.0531.0578
[research_glass_moss_2001]: https://doi.org/10.2514/6.2001-2962
[research_gnoffo_weilmuenster_1997]: https://doi.org/10.2514/6.1997-2473
[research_gnoffo_weilmuenster_1999]: https://doi.org/10.2514/2.3430
[research_goates_freeman_2026]: https://doi.org/10.3390/aerospace13040373
[research_gockel_1993]: https://doi.org/10.2514/6.1993-5090
[research_gogu_matsumura_2008]: https://doi.org/10.2514/6.2008-898
[research_goldberg_1966]: https://doi.org/10.2514/6.1966-464
[research_goldberg_scala_1965]: https://doi.org/10.21236/ad0623553
[research_goldman_obremski_1973]: https://doi.org/10.2514/3.50589
[research_golenko_sychev_2020]: https://doi.org/10.1109/ieeeconf48371.2020.9078641
[research_golomazov_ivankov_2013]: https://doi.org/10.1134/s003809461307006x
[research_golubkin_1995]: https://doi.org/10.1007/bf02078211
[research_golubkin_negoda_1992]: https://doi.org/10.1016/0021-8928(92)90022-z
[research_gomezfernandez_2024]: https://doi.org/10.52202/078373-0057
[research_gong_bing_2015]: https://doi.org/10.2514/6.2015-3606
[research_gong_chen_2014]: https://doi.org/10.2514/6.2014-2361
[research_gong_guo_2020]: https://doi.org/10.1016/j.ast.2020.106361
[research_gong_long_2024]: https://doi.org/10.1186/s42774-024-00181-5
[research_gong_wang_2022]: https://doi.org/10.3390/sym14091862
[research_gong_yao_2014]: https://doi.org/10.4236/jamp.2014.26054
[research_gong_yuan_2006]: https://doi.org/10.2514/6.2006-7994
[research_gongweijie_tangshuo_2010]: https://doi.org/10.1109/icent.2010.5532163
[research_gongweijie_tangshuo_2010_b]: https://doi.org/10.1109/iccda.2010.5541259
[research_goodwin_maxwell_2017]: https://doi.org/10.2514/6.2017-4651
[research_gopinath_vignesh_2015]: https://doi.org/10.2514/6.2015-3558
[research_gopinath_vignesh_2017]: https://doi.org/10.1007/978-3-319-46213-4_41
[research_gorelov_nguyen_2020]: https://doi.org/10.34759/trd-2020-113-4
[research_gorenbukh_nikolaev_1988]: https://doi.org/10.1007/bf01051831
[research_gormley_2005]: https://doi.org/10.1007/978-1-137-07838-4_5
[research_gormley_2015]: https://doi.org/10.1080/10736700.2015.1117735
[research_gottlieb_mines_2024]: https://doi.org/10.2514/6.2024-0373
[research_gottmann_1996]: https://doi.org/10.2514/6.1996-4500
[research_goulard_1961]: https://doi.org/10.2514/8.8893
[research_govinda_devaraj_2017]: https://doi.org/10.1007/978-3-319-46213-4_19
[research_goyal_prasad_2023]: https://doi.org/10.2514/6.2023-3022
[research_goyal_prasad_2023_b]: https://doi.org/10.2514/6.2023-3022.c2
[research_goyal_prasad_2023_c]: https://doi.org/10.2514/6.2023-3022.c1
[research_goyer_tallon_2023]: https://doi.org/10.1016/j.ceramint.2023.04.055
[research_goz_theodoulis_2025]: https://doi.org/10.2514/6.2025-2266
[research_gracey_cliff_1982]: https://doi.org/10.2514/3.19789
[research_graham_mavris_2000]: https://doi.org/10.2514/6.2000-5561
[research_graham_verboom_1978]: https://doi.org/10.9753/icce.v16.4
[research_grail_joly_1993]: https://doi.org/10.1016/s1474-6670(17)48857-4
[research_grallert_cucinelli_1987]: https://doi.org/10.1016/0094-5765(87)90101-9
[research_grallert_keller_1991]: https://doi.org/10.2514/3.46042
[research_gramola_bruce_2022]: https://doi.org/10.2514/6.2022-2288
[research_grant_2013]: https://doi.org/10.2514/6.2013-4503
[research_grant_antony_2016]: https://doi.org/10.2514/6.2016-0276
[research_grant_bolender_2015]: https://doi.org/10.2514/6.2015-2402
[research_grant_clark_2010]: https://doi.org/10.2514/6.2010-7810
[research_grant_clark_2011]: https://doi.org/10.2514/6.2011-6640
[research_grantz_1994]: https://doi.org/10.2514/6.1994-382
[research_grantz_cervisi_1993]: https://doi.org/10.2514/6.1993-511
[research_grasslin_telaar_2004]: https://doi.org/10.1016/j.actaastro.2004.05.004
[research_graves_argrow_2001]: https://doi.org/10.2514/6.2001-2960
[research_graves_emanuel_1996]: https://doi.org/10.2514/6.1996-3401
[research_green_dunn_2013]: https://doi.org/10.2514/6.2013-1256
[research_green_moss_1984]: https://doi.org/10.2514/6.1984-1714
[research_green_williams_2018]: https://doi.org/10.2514/6.2018-3432
[research_greene_williamsonjr_1981]: https://doi.org/10.2514/6.1981-168
[research_grego_2018]: https://doi.org/10.1080/00963402.2018.1486592
[research_gregorek_lee_1962]: https://doi.org/10.21236/ad0288297
[research_grenleski_billig_1968]: https://doi.org/10.2514/3.43951
[research_griffin_takahashi_2022]: https://doi.org/10.2514/6.2022-3657
[research_grimm_1992]: https://doi.org/10.1016/s1474-6670(17)49694-7
[research_grimm_1993]: https://doi.org/10.1016/b978-0-08-041715-8.50072-9
[research_gronlund_wright_2002]: https://doi.org/10.1080/14751790220002343
[research_gros_1963]: https://doi.org/10.21236/ad0436090
[research_groves_serrani_2005]: https://doi.org/10.21236/ada444973
[research_groves_serrani_2006]: https://doi.org/10.2514/6.2006-6557
[research_groves_sigthorsson_2005]: https://doi.org/10.2514/6.2005-6144
[research_gruber_weitz_2023]: https://doi.org/10.2514/6.2023-4632
[research_grubin_1963]: https://doi.org/10.2514/6.1963-364
[research_grubin_1964]: https://doi.org/10.1016/b978-0-12-395587-6.50037-5
[research_gruhn_gulhan_2018]: https://doi.org/10.2514/1.j056522
[research_grunlan_rajagopal_2010]: https://doi.org/10.21236/ada546978
[research_gu_2026]: https://doi.org/10.1016/j.ijheatfluidflow.2025.110206
[research_gu_baek_2017]: https://doi.org/10.1016/j.infrared.2017.08.014
[research_gu_dai_2023]: https://doi.org/10.23919/ccc58697.2023.10241136
[research_gu_qi_2018]: https://doi.org/10.1109/gncc42960.2018.9018867
[research_guan_wang_2013]: https://doi.org/10.1109/ccdc.2013.6560923
[research_guan_zou_2023]: https://doi.org/10.1109/wowmom57956.2023.00067
[research_guangjun_hang_2013]: https://doi.org/10.11591/telkomnika.v11i11.2786
[research_guangren_yanmei_2015]: https://doi.org/10.1109/chicc.2015.7260541
[research_guanping_xueli_2012]: https://doi.org/10.1109/ccdc.2012.6243059
[research_gui_2019]: https://doi.org/10.1360/sspma2019-0060
[research_gui_chen_1999]: https://doi.org/10.1002/(sici)1523-149x(1999)28:7<597::aid-htj5>3.3.co;2-7
[research_gulhan_esser_2001]: https://doi.org/10.2514/2.3729
[research_gulli_maddalena_2012]: https://doi.org/10.2514/6.2012-4161
[research_gunckel_1966]: https://doi.org/10.1016/b978-1-4831-6716-9.50006-0
[research_guo_cen_2024]: https://doi.org/10.1088/1361-6463/ad9dfb
[research_guo_chang_2018]: https://doi.org/10.1016/j.isatra.2018.04.001
[research_guo_chen_2022]: https://doi.org/10.3233/atde220826
[research_guo_chen_2022_b]: https://doi.org/10.1007/s42401-022-00137-x
[research_guo_ding_2023]: https://doi.org/10.1016/j.ast.2023.108279
[research_guo_ding_2024]: https://doi.org/10.1007/978-3-031-44947-5_101
[research_guo_ding_2025]: https://doi.org/10.1016/j.apm.2025.116122
[research_guo_ding_2026]: https://doi.org/10.1016/j.cnsns.2026.110335
[research_guo_fan_2022]: https://doi.org/10.1117/12.2643552
[research_guo_fang_2021]: https://doi.org/10.1109/icmeas54189.2021.00049
[research_guo_fang_2022]: https://doi.org/10.1088/1742-6596/2383/1/012127
[research_guo_fu_2025]: https://doi.org/10.3390/aerospace12040286
[research_guo_gong_2021]: https://doi.org/10.1007/978-981-15-8155-7_430
[research_guo_huang_2021]: https://doi.org/10.1109/cac53003.2021.9728281
[research_guo_lei_2025]: https://doi.org/10.1063/5.0256471
[research_guo_li_2020]: https://doi.org/10.1109/taes.2019.2921213
[research_guo_li_2026]: https://doi.org/10.1109/jmass.2026.3714464
[research_guo_liu_2018]: https://doi.org/10.1109/gncc42960.2018.9019110
[research_guo_liu_2019]: https://doi.org/10.23919/chicc.2019.8865758
[research_guo_liu_2024]: https://doi.org/10.1016/j.ast.2023.108801
[research_guo_liu_2024_b]: https://doi.org/10.1360/ssi-2023-0285
[research_guo_lu_2021]: https://doi.org/10.1109/access.2021.3067038
[research_guo_pang_2022]: https://doi.org/10.3390/en15155332
[research_guo_pang_2023]: https://doi.org/10.1016/j.cja.2022.07.012
[research_guo_qi_2017]: https://doi.org/10.1109/ccdc.2017.7978346
[research_guo_shen_2019]: https://doi.org/10.1016/j.ast.2019.105381
[research_guo_wang_2017]: https://doi.org/10.1007/978-981-10-5230-9_5
[research_guo_wenxing_2017]: https://doi.org/10.2514/6.2017-2142
[research_guo_xu_2018]: https://doi.org/10.1016/j.ast.2018.06.025
[research_guo_xu_2020]: https://doi.org/10.1007/s11432-019-2682-y
[research_guo_xu_2022]: https://doi.org/10.1109/taes.2022.3160687
[research_guo_yang_2023]: https://doi.org/10.23919/ccc58697.2023.10240784
[research_guo_zhang_2024]: https://doi.org/10.3390/drones8070295
[research_guoningbao_yangxu_2016]: https://doi.org/10.1109/cgncc.2016.7828810
[research_gupta_ramkumar_2015]: https://doi.org/10.12783/fae.2015.0401.02
[research_gupta_voelker_2012]: https://doi.org/10.2514/1.j051386
[research_gusev_1990]: https://doi.org/10.2514/6.1990-5271
[research_gustafsson_glendor_2019]: https://doi.org/10.1117/12.2533452
[research_guzmanbohorquez_greco_2024]: https://doi.org/10.26678/abcm.encit2024.cit24-0927
[research_guzmanbohorquez_greco_2025]: https://doi.org/10.26678/abcm.cobem2023.cob2023-2028
[research_hackett_1993]: https://doi.org/10.2514/6.1993-3135
[research_hagseth_blankson_1993]: https://doi.org/10.2514/6.1993-400
[research_haiqing_junfeng_2025]: https://doi.org/10.1007/978-981-96-3592-4_25
[research_hakima_bazzocchi_2021]: https://doi.org/10.1109/aero50100.2021.9438278
[research_halbe_mathavaraj_2010]: https://doi.org/10.2514/6.2010-8311
[research_halbe_raja_2014]: https://doi.org/10.2514/1.61615
[research_haley_chudoba_2018]: https://doi.org/10.2514/6.2018-5316
[research_haley_gonzalez_2018]: https://doi.org/10.2514/6.2018-5258
[research_hall_schemmel_2026]: https://doi.org/10.2514/6.2026-4402
[research_halter_cliff_1991]: https://doi.org/10.2514/6.1991-2713
[research_hamed_kumar_1992]: https://doi.org/10.1115/92-gt-205
[research_hamid_nazar_2016]: https://doi.org/10.1063/1.4966824
[research_hamilton_carsten_2007]: https://doi.org/10.2514/6.2007-6003
[research_hamilton_gupta_1991]: https://doi.org/10.2514/3.26219
[research_hammitt_1959]: https://doi.org/10.1017/s0022112059000179
[research_hammitt_bogdonoff_1956]: https://doi.org/10.2514/8.6969
[research_han_jia_2023]: https://doi.org/10.1109/ccdc58219.2023.10327401
[research_han_jo_2024]: https://doi.org/10.2514/1.g007903
[research_han_liu_2022]: https://doi.org/10.1016/j.ast.2022.107585
[research_han_shan_2011]: https://doi.org/10.1109/iceceng.2011.6057715
[research_han_su_2025]: https://doi.org/10.1063/5.0274656
[research_han_sun_2020]: https://doi.org/10.1016/j.ast.2019.105673
[research_han_wang_2024]: https://doi.org/10.1016/j.ast.2023.108839
[research_han_wang_2024_b]: https://doi.org/10.23919/ccc63176.2024.10661992
[research_han_wang_2025]: https://doi.org/10.1007/978-981-96-2260-3_26
[research_han_xiong_2016]: https://doi.org/10.1109/imcec.2016.7867213
[research_hanai_ozawa_2007]: https://doi.org/10.2514/6.2007-4220
[research_handley_streetman_2017]: https://doi.org/10.2514/6.2017-3877
[research_haney_1995]: https://doi.org/10.2514/6.1995-6162
[research_haney_beaulieu_1994]: https://doi.org/10.2514/6.1994-383
[research_haney_bradley_1995]: https://doi.org/10.2514/6.1995-847
[research_haney_cervisi_1993]: https://doi.org/10.2514/6.1993-402
[research_hanquist_boyd_2016]: https://doi.org/10.2514/6.2016-0507
[research_hanquist_boyd_2018]: https://doi.org/10.2514/6.2018-1714
[research_hanson_coughlin_1998]: https://doi.org/10.2514/6.1998-4409
[research_hanson_jones_2004]: https://doi.org/10.2514/1.10886
[research_hanumpatla_knight_2026]: https://doi.org/10.2514/6.2026-2298
[research_hao_2026]: https://doi.org/10.2991/978-94-6239-701-9_34
[research_hao_dengcheng_2019]: https://doi.org/10.1109/iicspi48186.2019.9095890
[research_hao_longbin_2017]: https://doi.org/10.2991/icmmcce-17.2017.225
[research_hao_peng_2017]: https://doi.org/10.2514/6.2017-2108
[research_hao_peng_2019]: https://doi.org/10.1109/access.2018.2889926
[research_hao_yongqi_2024]: https://doi.org/10.23919/ccc63176.2024.10662106
[research_hao_zhang_2025]: https://doi.org/10.1016/j.cja.2024.08.004
[research_haoliang_yongzhao_2015]: https://doi.org/10.1109/chicc.2015.7260428
[research_haque_meo_2026]: https://doi.org/10.2514/6.2026-2301
[research_harl_2008]: https://doi.org/10.2514/6.2008-6215
[research_harl_balakrishnan_2010]: https://doi.org/10.2514/1.42654
[research_harloff_petrie_1987]: https://doi.org/10.2514/6.1987-2545
[research_harper_braun_2014]: https://doi.org/10.2514/6.2014-1095
[research_harpold_gavert_1983]: https://doi.org/10.2514/3.8523
[research_harris_hall_1980]: https://doi.org/10.2514/6.1980-1609
[research_hartofilis_1965]: https://doi.org/10.2514/6.1965-753
[research_hartung_mitcheltree_1991]: https://doi.org/10.2514/6.1991-571
[research_hartung_mitcheltree_1992]: https://doi.org/10.2514/3.376
[research_hartunian_thompson_1963]: https://doi.org/10.2514/6.1963-464
[research_harvey_2011]: https://doi.org/10.1017/cbo9780511842757.008
[research_hasegawa_2025]: https://doi.org/10.2514/6.2025-1335
[research_hassan_dejarnette_1991]: https://doi.org/10.2514/6.1991-5032
[research_hassan_fahrenholtz_2024]: https://doi.org/10.1016/j.ceramint.2024.10.430
[research_hassan_kuntz_2001]: https://doi.org/10.2514/6.2001-2903
[research_hattis_1990]: https://doi.org/10.23919/acc.1990.4791043
[research_hattis_malchow_1991]: https://doi.org/10.2514/6.1991-5052
[research_hattis_malchow_1992]: https://doi.org/10.2514/6.1992-5011
[research_hattis_smolskis_1989]: https://doi.org/10.23919/acc.1989.4790358
[research_havstad_ferencz_2002]: https://doi.org/10.2514/2.6725
[research_hawkins_pitz_2010]: https://doi.org/10.2514/6.2010-8348
[research_hawkins_richardson_1991]: https://doi.org/10.2514/6.1991-3179
[research_haws_bowman_2022]: https://doi.org/10.2514/6.2022-4212
[research_hayaramos_bonetti_2009]: https://doi.org/10.2514/6.2009-7412
[research_hayat_ali_2014]: https://doi.org/10.1007/s10483-015-1895-9
[research_hayes_nompelis_2020]: https://doi.org/10.2514/6.2020-3201
[research_hayward_urdiales_2018]: https://doi.org/10.1007/978-3-319-32817-1_17
[research_he_2015]: https://doi.org/10.12733/jics20105682
[research_he_2015_b]: https://doi.org/10.2514/6.2015-3685
[research_he_gu_2023]: https://doi.org/10.1088/1742-6596/2658/1/012011
[research_he_huang_2015]: https://doi.org/10.1007/978-3-662-48224-7_69
[research_he_le_2001]: https://doi.org/10.1007/s11630-001-0049-y
[research_he_le_2009]: https://doi.org/10.2514/6.2009-7423
[research_he_le_2017]: https://doi.org/10.1108/aeat-12-2014-0214
[research_he_le_2017_b]: https://doi.org/10.2514/6.2017-2145
[research_he_li_2018]: https://doi.org/10.1109/gncc42960.2018.9018857
[research_he_li_2025]: https://doi.org/10.3390/aerospace12010062
[research_he_li_2026]: https://doi.org/10.3390/electronics15143132
[research_he_li_2026_b]: https://doi.org/10.1155/ijae/3161844
[research_he_li_2026_c]: https://doi.org/10.23919/jsee.2026.000096
[research_he_liu_2016]: https://doi.org/10.1109/chicc.2016.7554181
[research_he_liu_2017]: https://doi.org/10.1109/ccdc.2017.7978630
[research_he_qi_2017]: https://doi.org/10.1016/j.cja.2017.01.003
[research_he_sun_2023]: https://doi.org/10.1016/j.ast.2023.108524
[research_he_tang_2024]: https://doi.org/10.1109/tgrs.2024.3459951
[research_he_yan_2018]: https://doi.org/10.2514/1.g003424
[research_he_yan_2020]: https://doi.org/10.2514/1.g003424.c1
[research_he_zhang_2012]: https://doi.org/10.1016/j.ceramint.2012.03.051
[research_he_zhao_2025]: https://doi.org/10.3390/en18133417
[research_he_zuo_2022]: https://doi.org/10.1016/j.actaastro.2021.09.030
[research_heat_transfer_1986]: https://doi.org/10.2514/5.9781600865770.0060.0078
[research_heathman_kelly_1966]: https://doi.org/10.2514/6.1966-1740
[research_heffner_gottesdiener_1991]: https://doi.org/10.2514/6.1991-1749
[research_hegarty_omerdic_2017]: https://doi.org/10.1109/oceanse.2017.8084650
[research_heidrich_braun_2020]: https://doi.org/10.2514/6.2020-1741
[research_heinze_bardenhagen_1998]: https://doi.org/10.2514/2.3376
[research_heller_1967]: https://doi.org/10.1121/1.2144251
[research_heller_sachs_1998]: https://doi.org/10.2514/6.1998-1521
[research_heller_widnall_1968]: https://doi.org/10.1121/1.1911226
[research_hellman_2014]: https://doi.org/10.2514/6.2014-4206
[research_hellman_remillard_2011]: https://doi.org/10.21236/ada554045
[research_hemanth_jagadeesh_2009]: https://doi.org/10.1007/978-3-540-85168-4_113
[research_hemdan_1990]: https://doi.org/10.1016/0094-5765(90)90084-x
[research_henline_1991]: https://doi.org/10.2514/6.1991-697
[research_henline_palmer_1995]: https://doi.org/10.2514/6.1995-2079
[research_herman_melnik_1962]: https://doi.org/10.21236/ad0404197
[research_hermann_1959]: https://doi.org/10.1007/978-3-7091-4745-0_19
[research_hermann_1961]: https://doi.org/10.1016/b978-0-12-395690-3.50011-9
[research_hermann_1961_b]: https://doi.org/10.1007/978-94-015-6337-6_23
[research_hermann_2025]: https://doi.org/10.1016/j.ijheatmasstransfer.2025.126907
[research_hermann_schmidt_1995]: https://doi.org/10.2514/6.1995-3372
[research_hernandez_rodriguezsegade_2020]: https://doi.org/10.2514/6.2020-2420
[research_herrlin_gelderloos_1988]: https://doi.org/10.2514/6.1988-3877
[research_herrmann_cox_2025]: https://doi.org/10.2514/6.2025-1338
[research_hill_1967]: https://doi.org/10.2514/6.1967-1127
[research_hillig_1986]: https://doi.org/10.1007/978-1-4613-2233-7_55
[research_hills_1985]: https://doi.org/10.21236/ada162149
[research_hinman_johansen_2017]: https://doi.org/10.1016/j.ast.2017.08.034
[research_hinman_schmitt_2015]: https://doi.org/10.2514/6.2015-3509
[research_hirose_udagawa_2015]: https://doi.org/10.1007/978-3-319-16835-7_54
[research_hirschel_1991]: https://doi.org/10.2514/6.1991-5041
[research_hirschel_1992]: https://doi.org/10.1007/978-1-4612-0379-7_1
[research_hirschel_2015]: https://doi.org/10.1007/978-3-319-14373-6_6
[research_hirschel_2015_b]: https://doi.org/10.1007/978-3-319-14373-6_5
[research_hirschel_meier_2004]: https://doi.org/10.1007/978-3-642-18484-0_16
[research_hirschel_staudacher_2025]: https://doi.org/10.1007/978-3-031-94219-8_2
[research_hirschel_staudacher_2025_b]: https://doi.org/10.1007/978-3-031-94219-8_3
[research_hirschel_weiland_2009]: https://doi.org/10.1007/978-3-540-89974-7_9
[research_hirschel_weiland_2009_b]: https://doi.org/10.1007/978-3-540-89974-7_4
[research_hirschel_weiland_2009_c]: https://doi.org/10.1007/978-3-540-89974-7_3
[research_hirschel_weiland_2009_d]: https://doi.org/10.1007/978-3-540-89974-7_5
[research_hirschel_weiland_2009_e]: https://doi.org/10.1007/978-3-540-89974-7_10
[research_hirschel_weiland_2009_f]: https://doi.org/10.1007/978-3-540-89974-7_2
[research_hirschel_weiland_2010]: https://doi.org/10.1007/s12567-010-0004-4
[research_hiruma_takase_2020]: https://doi.org/10.2514/6.2020-2413
[research_hodge_phillips_1981]: https://doi.org/10.2514/6.1981-2421
[research_hodgson_lee_2003]: https://doi.org/10.2514/6.2003-5796
[research_hoffert_wen_2026]: https://doi.org/10.2514/6.2026-5025
[research_hoffman_wapner_2003]: https://doi.org/10.21236/ada419385
[research_hoffmann_wilson_1989]: https://doi.org/10.2514/6.1989-2185
[research_hohn_gulhan_2017]: https://doi.org/10.2514/1.a33728
[research_holden_1978]: https://doi.org/10.2514/6.1978-1169
[research_holden_1986]: https://doi.org/10.1007/978-3-642-82770-9_26
[research_holden_wadhams_2008]: https://doi.org/10.2514/6.2008-2505
[research_holdsworth_leondes_1990]: https://doi.org/10.1016/b978-0-12-012732-0.50014-8
[research_holguin_labbee_1988]: https://doi.org/10.2514/6.1988-165
[research_holifield_tufts_2024]: https://doi.org/10.2514/6.2024-0672
[research_holifield_tufts_2024_b]: https://doi.org/10.2514/6.2024-0672.c1
[research_hollanders_laval_1992]: https://doi.org/10.2514/6.1992-5027
[research_hollis_2017]: https://doi.org/10.2514/6.2017-3122
[research_hollis_hollingsworth_2012]: https://doi.org/10.2514/6.2012-3063
[research_hollis_hollingsworth_2013]: https://doi.org/10.2514/1.a32458
[research_holmhansen_lee_2010]: https://doi.org/10.2514/6.2010-7868
[research_holmquist_lundberg_1997]: https://doi.org/10.1115/97-gt-413
[research_holthouse_subin_2026]: https://doi.org/10.2514/6.2026-116415
[research_hong_neuenschwander_1991]: https://doi.org/10.2514/6.1991-1440
[research_hong_xiong_2014]: https://doi.org/10.1109/chicc.2014.6896100
[research_hongbo_yongyuan_2016]: https://doi.org/10.1504/ijscom.2016.076405
[research_hongjun_qing_2015]: https://doi.org/10.1016/j.proeng.2014.12.710
[research_hongpeng_weiqiang_2016]: https://doi.org/10.1016/j.actaastro.2016.05.014
[research_hongqianlu_dongmingge_2011]: https://doi.org/10.1109/icacc.2011.6016487
[research_hopkins_raymond_2010]: https://doi.org/10.1109/sieds.2010.5469661
[research_horing_maute_2025]: https://doi.org/10.2514/1.t7165
[research_horing_maute_2025_b]: https://doi.org/10.2514/6.2025-1560
[research_horlock_1964]: https://doi.org/10.1017/s0368393100080688
[research_horneman_neal_2010]: https://doi.org/10.2514/6.2010-8309
[research_hornung_2021]: https://doi.org/10.1017/jfm.2021.187
[research_horstman_1969]: https://doi.org/10.2514/6.1969-140
[research_horton_babineaux_1967]: https://doi.org/10.2514/3.3904
[research_hoschke_price_2013]: https://doi.org/10.1007/978-1-4471-5113-5_4
[research_hoschke_price_2013_b]: https://doi.org/10.4028/www.scientific.net/kem.558.268
[research_hoskin_nguyen_2024]: https://doi.org/10.2514/6.2024-2857
[research_hossein_rabiee_2025]: https://doi.org/10.1063/5.0243457
[research_hoter_nastac_2026]: https://doi.org/10.2514/6.2026-5115
[research_hou_li_2025]: https://doi.org/10.1007/978-981-95-3007-6_12
[research_hou_liu_2023]: https://doi.org/10.3390/aerospace10121008
[research_hou_wang_2015]: https://doi.org/10.1109/jas.2015.7081658
[research_hoult_starkey_2003]: https://doi.org/10.2514/6.2003-6964
[research_hove_shih_1977]: https://doi.org/10.2514/6.1977-93
[research_hovey_1964]: https://doi.org/10.2514/6.1964-356
[research_hovey_1965]: https://doi.org/10.2514/3.28175
[research_hsu_ho_2000]: https://doi.org/10.1053/apmr.2000.0810210
[research_hsu_kuo_1990]: https://doi.org/10.1016/0094-5765(90)90114-z
[research_hu_bodson_2008]: https://doi.org/10.2514/6.2008-6375
[research_hu_chen_2021]: https://doi.org/10.1007/s12555-019-0474-x
[research_hu_deng_2015]: https://doi.org/10.4028/www.scientific.net/amm.719-720.324
[research_hu_dong_2022]: https://doi.org/10.1109/indin51773.2022.9976071
[research_hu_dong_2024]: https://doi.org/10.1007/s11071-024-10209-6
[research_hu_gao_2021]: https://doi.org/10.1016/j.ast.2021.107166
[research_hu_gao_2022]: https://doi.org/10.3390/aerospace9040217
[research_hu_guo_2022]: https://doi.org/10.1002/asjc.2822
[research_hu_hu_1997]: https://doi.org/10.2514/6.1997-2015
[research_hu_hu_2015]: https://doi.org/10.1061/(asce)as.1943-5525.0000383
[research_hu_huang_2026]: https://doi.org/10.2514/1.a36734
[research_hu_jiang_2015]: https://doi.org/10.2514/6.2015-4546
[research_hu_li_2018]: https://doi.org/10.1016/j.neucom.2018.01.031
[research_hu_li_2021]: https://doi.org/10.1109/access.2021.3066501
[research_hu_liu_2013]: https://doi.org/10.1109/ccdc.2013.6560962
[research_hu_liu_2022]: https://doi.org/10.3390/electronics11193059
[research_hu_liu_2025]: https://doi.org/10.1016/j.ast.2024.109856
[research_hu_mahadevan_2019]: https://doi.org/10.2514/1.j057865
[research_hu_meng_2017]: https://doi.org/10.1016/j.ast.2017.04.022
[research_hu_sun_2023]: https://doi.org/10.23919/ccc58697.2023.10240299
[research_hu_wang_2016]: https://doi.org/10.1007/s11771-016-3351-2
[research_hu_wang_2026]: https://doi.org/10.1016/j.dt.2025.10.033
[research_hu_wang_2026_b]: https://doi.org/10.1016/j.ast.2025.110931
[research_hu_wu_2012]: https://doi.org/10.1049/iet-cta.2011.0065
[research_hu_wu_2012_b]: https://doi.org/10.1016/j.jfranklin.2011.08.007
[research_hu_xiao_2024]: https://doi.org/10.1016/j.jfranklin.2023.12.038
[research_hu_xin_2014]: https://doi.org/10.1007/s11633-014-0823-4
[research_hu_yang_2022]: https://doi.org/10.3390/s22041523
[research_hu_zhang_2008]: https://doi.org/10.4028/0-87849-473-1.1730
[research_hu_zhou_2010]: https://doi.org/10.1109/icmtma.2010.427
[research_hu_zhu_2022]: https://doi.org/10.1038/s41598-022-24138-0
[research_huang_1968]: https://doi.org/10.1007/bf00928758
[research_huang_fengyuan_2017]: https://doi.org/10.2514/6.2017-4654
[research_huang_hartley_1969]: https://doi.org/10.1063/1.1692299
[research_huang_hwang_1970]: https://doi.org/10.1016/b978-0-08-006931-9.50030-1
[research_huang_li_2016]: https://doi.org/10.1109/cgncc.2016.7829176
[research_huang_li_2023]: https://doi.org/10.1016/j.ast.2023.108235
[research_huang_li_2025]: https://doi.org/10.1016/j.ast.2025.110283
[research_huang_li_2025_b]: https://doi.org/10.2514/1.a36290
[research_huang_ma_2011]: https://doi.org/10.1016/j.actaastro.2011.02.016
[research_huang_sun_2013]: https://doi.org/10.1016/j.cja.2013.04.036
[research_huang_sun_2023]: https://doi.org/10.1007/978-981-19-6613-2_387
[research_huang_wu_2018]: https://doi.org/10.1007/978-981-13-0463-7_4
[research_huang_yang_2018]: https://doi.org/10.1109/ccdc.2018.8407432
[research_huang_yao_2020]: https://doi.org/10.1016/j.actaastro.2020.03.009
[research_huang_yao_2020_b]: https://doi.org/10.1016/j.ijheatmasstransfer.2020.119549
[research_huang_yu_2024]: https://doi.org/10.1016/j.ast.2024.109636
[research_huang_zhang_2014]: https://doi.org/10.1007/s11432-014-5179-4
[research_huang_zhang_2016]: https://doi.org/10.1109/cgncc.2016.7828812
[research_huang_zhang_2017]: https://doi.org/10.1109/ccdc.2017.7978679
[research_huang_zhang_2018]: https://doi.org/10.1088/1742-6596/1060/1/012088
[research_huang_zhang_2020]: https://doi.org/10.1109/ccdc49329.2020.9164342
[research_huang_zhang_2021]: https://doi.org/10.1177/09544100211051106
[research_huang_zhang_2021_b]: https://doi.org/10.23919/ccc52363.2021.9550353
[research_huang_zhang_2026]: https://doi.org/10.1007/978-981-92-1599-7_17
[research_huber_1966]: https://doi.org/10.2514/6.1966-750
[research_hufgard_duernhofer_2023]: https://doi.org/10.1038/s41598-023-40281-8
[research_hughes_wu_2010]: https://doi.org/10.2514/6.2010-8281
[research_hughes_wu_2012]: https://doi.org/10.1007/978-1-4614-1833-7_16
[research_hugo_lago_2022]: https://doi.org/10.5772/intechopen.100328
[research_hui_chi_2021]: https://doi.org/10.1007/978-981-15-8155-7_346
[research_huihui_huang_2016]: https://doi.org/10.2514/6.2016-4575
[research_huihui_huang_2017]: https://doi.org/10.2514/6.2017-2354
[research_huisheng_beijing_2021]: https://doi.org/10.1115/1.4053068
[research_hull_french_1981]: https://doi.org/10.2514/6.1981-1862
[research_hull_seguin_1994]: https://doi.org/10.2514/3.21288
[research_hunt_1989]: https://doi.org/10.1007/978-1-4684-9187-6_5
[research_hunt_eiswirth_1996]: https://doi.org/10.2514/6.1996-4591
[research_hunt_lawing_1979]: https://doi.org/10.2514/3.58587
[research_hunt_lockwood_1997]: https://doi.org/10.1063/1.51938
[research_huo_liu_2014]: https://doi.org/10.4028/www.scientific.net/amm.635-637.1431
[research_huo_mirmirani_2006]: https://doi.org/10.2514/6.2006-6695
[research_huo_yang_2015]: https://doi.org/10.4028/www.scientific.net/amm.775.59
[research_huo_yang_2016]: https://doi.org/10.1109/ihmsc.2016.255
[research_huo_yang_2017]: https://doi.org/10.2514/6.2017-2106
[research_hutchins_sanjose_1998]: https://doi.org/10.1117/12.324646
[research_hutt_1987]: https://doi.org/10.1177/014233128700900404
[research_huynh_kriz_2009]: https://doi.org/10.21236/ada640309
[research_hwang_2019]: https://doi.org/10.21914/anziamj.v60i0.14067
[research_hwang_huh_2020]: https://doi.org/10.5139/jksas.2020.48.9.731
[research_hypersonic_aerodynamics_1988]: https://doi.org/10.2514/5.9781600862342.0051.0080
[research_hypersonic_aerodynamics_2016]: https://doi.org/10.1016/b978-0-12-804425-4.00023-4
[research_hypersonic_materials_2023]: https://doi.org/10.12968/s1478-2774(24)50016-3
[research_hypersonic_thin_2018]: https://doi.org/10.1201/9780203737972-3
[research_ide_armstrong_1989]: https://doi.org/10.2514/6.1989-2182
[research_igra_2018]: https://doi.org/10.2514/1.a34089
[research_igra_2019]: https://doi.org/10.2514/1.a34415
[research_ikawa_1983]: https://doi.org/10.2514/6.1983-2096
[research_ikawa_1989]: https://doi.org/10.2514/6.1989-2682
[research_ikenson_2025]: https://doi.org/10.1063/10.0039841
[research_ingenito_2021]: https://doi.org/10.1007/978-3-030-66881-5_3
[research_inger_1991]: https://doi.org/10.2514/6.1991-3324
[research_inger_1995]: https://doi.org/10.2514/3.713
[research_inger_1995_b]: https://doi.org/10.1016/0094-5765(95)00101-5
[research_inoue_page_1977]: https://doi.org/10.2514/6.1977-755
[research_ionescu_bernard_2021]: https://doi.org/10.1007/978-3-030-85776-9_9
[research_isaac_miles_1990]: https://doi.org/10.2514/6.1990-3066
[research_ishikawa_yamazaki_2021]: https://doi.org/10.1299/jsmecmd.2021.34.113
[research_ishimoto_1995]: https://doi.org/10.2514/6.1995-3286
[research_ishimoto_1999]: https://doi.org/10.2514/6.1999-4169
[research_ishimoto_takizawa_1996]: https://doi.org/10.2514/6.1996-3403
[research_islam_dutta_2025]: https://doi.org/10.1016/j.mtcomm.2025.112337
[research_ismail_arifin_2016]: https://doi.org/10.1063/1.4952503
[research_ispir_goncalves_2019]: https://doi.org/10.1051/matecconf/201930403001
[research_istratie_1998]: https://doi.org/10.2514/6.1998-2457
[research_istratie_1999]: https://doi.org/10.2514/6.1999-4170
[research_istratie_2000]: https://doi.org/10.2514/6.2000-3993
[research_istratie_2003]: https://doi.org/10.2514/6.2003-5395
[research_istratie_istratie_1997]: https://doi.org/10.2514/6.1997-3483
[research_istratie_maroulis_2009]: https://doi.org/10.1063/1.3225444
[research_istratie_simos_2007]: https://doi.org/10.1063/1.2790127
[research_ito_takaki_1999]: https://doi.org/10.2514/3.27202
[research_itoh_ueda_1999]: https://doi.org/10.2514/6.1999-4960
[research_itoh_ueda_2002]: https://doi.org/10.1007/s00193-002-0147-0
[research_ivanov_vashchenkov_2007]: https://doi.org/10.2514/6.2007-4145
[research_j_swaminathan_2022]: https://doi.org/10.23919/ascc56756.2022.9828063
[research_jackson_2006]: https://doi.org/10.2514/6.2006-2817
[research_jackson_anderson_1967]: https://doi.org/10.1007/978-1-4757-0489-1_15
[research_jaeger_hemati_2025]: https://doi.org/10.2514/6.2025-97945
[research_jaensch_markl_1991]: https://doi.org/10.2514/6.1991-2659
[research_janardanan_jayakumar_2006]: https://doi.org/10.2514/6.2006-8076
[research_jangir_ewans_2023]: https://doi.org/10.1175/jtech-d-22-0108.1
[research_janovsky_romberg_1999]: https://doi.org/10.2514/6.1999-4817
[research_jansch_schnepper_1994]: https://doi.org/10.1007/978-1-4757-9259-1_8
[research_javaid_serghides_2003]: https://doi.org/10.2514/6.2003-6953
[research_javaid_serghides_2004]: https://doi.org/10.2514/6.2004-1201
[research_javaid_serghides_2005]: https://doi.org/10.2514/1.8782
[research_javaid_serghides_2005_b]: https://doi.org/10.2514/1.8729
[research_jayan_2023]: https://doi.org/10.1007/978-3-031-40809-0_13
[research_jayanthi_jain_2019]: https://doi.org/10.12783/ballistics2019/33142
[research_jedlicka_parkerjr_1970]: https://doi.org/10.2514/6.1970-200
[research_jeon_karpenko_2020]: https://doi.org/10.2514/1.g004672
[research_jeong_kang_2025]: https://doi.org/10.5370/kiee.2025.74.4.666
[research_jeyakumar_biswas_2005]: https://doi.org/10.1016/j.mcm.2005.02.001
[research_ji_2017]: https://doi.org/10.2514/6.2017-2184
[research_ji_chen_2025]: https://doi.org/10.1016/j.ifacol.2025.11.477
[research_ji_wang_2017]: https://doi.org/10.23919/chicc.2017.8027473
[research_ji_zhang_2014]: https://doi.org/10.1016/j.applthermaleng.2014.06.014
[research_ji_zhao_2023]: https://doi.org/10.23919/ccc58697.2023.10240358
[research_ji_zhou_2017]: https://doi.org/10.23919/chicc.2017.8028356
[research_ji_zhou_2018]: https://doi.org/10.1007/s11071-017-4041-9
[research_ji_zhou_2018_b]: https://doi.org/10.1109/gncc42960.2018.9019124
[research_ji_zhou_2019]: https://doi.org/10.23919/chicc.2019.8865421
[research_jia_dong_2018]: https://doi.org/10.1117/12.2309292
[research_jia_fu_2020]: https://doi.org/10.1016/j.actaastro.2019.11.038
[research_jia_wenxiu_2004]: https://doi.org/10.1007/bf02437297
[research_jiaming_kyle_2024]: https://doi.org/10.2514/6.2024-2659
[research_jianan_weidong_2025]: https://doi.org/10.1007/978-981-96-2236-8_37
[research_jianbo_xinghua_2017]: https://doi.org/10.23919/chicc.2017.8028297
[research_jiang_2018]: https://doi.org/10.2514/6.2018-0721
[research_jiang_2018_b]: https://doi.org/10.2514/6.2018-0721.c1
[research_jiang_bu_2022]: https://doi.org/10.1177/00202940221114893
[research_jiang_chen_2018]: https://doi.org/10.1109/gncc42960.2018.9018655
[research_jiang_cui_2026]: https://doi.org/10.1016/j.dt.2025.07.020
[research_jiang_ge_2021]: https://doi.org/10.1088/1742-6596/1986/1/012114
[research_jiang_liu_2009]: https://doi.org/10.1007/s10409-009-0252-8
[research_jiang_liu_2024]: https://doi.org/10.23919/ccc63176.2024.10661464
[research_jiang_luo_2019]: https://doi.org/10.1007/978-3-319-91020-8_59
[research_jiang_lv_2018]: https://doi.org/10.1109/gncc42960.2018.9019042
[research_jiang_nan_2022]: https://doi.org/10.3390/aerospace9080424
[research_jiang_wang_2017]: https://doi.org/10.1007/978-3-319-46213-4_29
[research_jiang_wang_2023]: https://doi.org/10.1007/978-3-031-42515-8_20
[research_jiang_yu_2019]: https://doi.org/10.1007/978-3-319-91020-8_1
[research_jiang_zhou_2020]: https://doi.org/10.1080/21642583.2020.1747567
[research_jiang_zhou_2025]: https://doi.org/10.23919/ccc64809.2025.11178345
[research_jianguo_yifei_2018]: https://doi.org/10.1109/ccdc.2018.8407770
[research_jianjunluo_2003]: https://doi.org/10.2514/6.iac-03-a.7.05
[research_jiao_jiang_2014]: https://doi.org/10.1109/cgncc.2014.7007373
[research_jiao_zhang_2025]: https://doi.org/10.1007/978-981-96-3568-9_28
[research_jiayuan_peng_2018]: https://doi.org/10.1109/gncc42960.2018.9018894
[research_jie_2017]: https://doi.org/10.2514/6.2017-2280
[research_jiegu_shuguangzhang_2016]: https://doi.org/10.1109/imcec.2016.7867528
[research_jin_li_2019]: https://doi.org/10.1016/j.ceramint.2019.01.009
[research_jin_wang_2008]: https://doi.org/10.1002/htj.20203
[research_jin_wang_2018]: https://doi.org/10.1016/j.engfailanal.2017.10.001
[research_jin_wang_2026]: https://doi.org/10.1016/j.ast.2025.111249
[research_jin_yu_2024]: https://doi.org/10.3390/aerospace11040257
[research_jinchuanhu_jinglinli_2015]: https://doi.org/10.1109/iccais.2015.7338676
[research_jing_shuo_2007]: https://doi.org/10.2514/6.2007-642
[research_jing_shuo_2008]: https://doi.org/10.2514/6.2008-142
[research_jing_song_2026]: https://doi.org/10.1016/j.applthermaleng.2026.130617
[research_jing_yuanpei_2015]: https://doi.org/10.2514/6.2015-3242
[research_jing_zhao_2018]: https://doi.org/10.1109/cac.2018.8623527
[research_jingang_haotian_2026]: https://doi.org/10.23919/jsee.2026.000076
[research_jingguang_shenmin_2017]: https://doi.org/10.23919/chicc.2017.8027411
[research_jingqingxu_xinglinqi_2011]: https://doi.org/10.1109/csss.2011.5974822
[research_jiying_jubo_2010]: https://doi.org/10.1016/s1000-9361(09)60191-6
[research_jo_2026]: https://doi.org/10.2514/6.2026-115448
[research_jo_kim_2021]: https://doi.org/10.5139/jksas.2021.49.2.155
[research_jo_kwon_2020]: https://doi.org/10.1016/j.ijheatmasstransfer.2020.119566
[research_jo_park_2019]: https://doi.org/10.1007/978-3-319-91017-8_120
[research_john_kulkarni_2014]: https://doi.org/10.1016/j.compfluid.2014.03.004
[research_johnson_1967]: https://doi.org/10.1016/b978-0-12-395737-5.50048-2
[research_johnson_2002]: https://doi.org/10.2514/6.2002-5218
[research_johnson_bogar_2001]: https://doi.org/10.2514/6.2001-1926
[research_johnson_calise_2006]: https://doi.org/10.2514/1.14767
[research_johnson_cerimele_2018]: https://doi.org/10.2514/6.2018-0615
[research_johnson_curry_1986]: https://doi.org/10.2514/6.1986-949
[research_johnson_gasch_2009]: https://doi.org/10.2514/6.2009-7219
[research_johnson_lewis_2008]: https://doi.org/10.2514/6.2008-6557
[research_johnson_lewis_2008_b]: https://doi.org/10.2514/6.2008-2594
[research_johnson_lu_2020]: https://doi.org/10.2514/6.2020-1513
[research_johnson_mirdamadi_1996]: https://doi.org/10.1520/stp16457s
[research_johnson_starkey_2006]: https://doi.org/10.2514/6.2006-6273
[research_johnson_starkey_2007]: https://doi.org/10.2514/1.27219
[research_jones_1972]: https://doi.org/10.2514/6.1972-953
[research_jones_center_2002]: https://doi.org/10.2514/6.2002-3204
[research_jones_cesnik_2024]: https://doi.org/10.2514/6.2024-1048
[research_jones_dougherty_1990]: https://doi.org/10.2514/6.1990-3065
[research_jones_dougherty_1993]: https://doi.org/10.2514/6.1993-774
[research_jones_sobieczky_1995]: https://doi.org/10.2514/3.26715
[research_joseph_sinha_2026]: https://doi.org/10.1007/978-981-95-1723-7_49
[research_joseph_whitside_2026]: https://doi.org/10.2514/6.2026-5069
[research_joshi_lu_2015]: https://doi.org/10.1007/978-3-319-16835-7_56
[research_joshi_sivan_2005]: https://doi.org/10.2514/6.2005-6438
[research_joshi_sivan_2007]: https://doi.org/10.2514/1.26306
[research_josselyn_ross_2003]: https://doi.org/10.2514/2.5074
[research_jouhaud_1992]: https://doi.org/10.1016/0094-5765(92)90148-c
[research_jouhaud_ferreres_2007]: https://doi.org/10.3182/20070625-5-fr-2916.00054
[research_juneau_pw_1970]: https://doi.org/10.21236/ad0871961
[research_junhui_jiayuan_2014]: https://doi.org/10.1109/cgncc.2014.7007343
[research_juttyk_bhat_2000]: https://doi.org/10.1023/a:1011536324041
[research_kabelitz_1970]: https://doi.org/10.2514/6.1970-1174
[research_kadam_hablani_2014]: https://doi.org/10.3182/20140313-3-in-3024.00133
[research_kadish_goldberger_1995]: https://doi.org/10.1016/s0033-0620(05)80015-5
[research_kageyama_hiraoka_2004]: https://doi.org/10.1299/jsmecmd.2004.17.681
[research_kahl_harris_1989]: https://doi.org/10.1007/978-1-4615-6409-6_14
[research_kai_ohtake_1996]: https://doi.org/10.2514/6.1996-4526
[research_kalaiarassan_krishan_2018]: https://doi.org/10.1016/j.matpr.2018.02.350
[research_kalimuthu_rathakrishnan_2008]: https://doi.org/10.2514/6.2008-4707
[research_kalirajan_joshi_2016]: https://doi.org/10.2514/6.2016-3236
[research_kalirajan_joshi_2018]: https://doi.org/10.13111/2066-8201.2018.10.2.5
[research_kameda_tsujimichi_2000]: https://doi.org/10.1002/1520-6424(200012)83:12<84::aid-ecja8>3.0.co;2-6
[research_kamimoto_uenaka_1969]: https://doi.org/10.2322/jjsass1969.17.142
[research_kaminsky_johnsonjr_1964]: https://doi.org/10.2514/6.1964-1037
[research_kanda_hiraiwa_2007]: https://doi.org/10.2514/1.31143
[research_kanderpalli_selvaraj_2014]: https://doi.org/10.2514/6.2014-2507
[research_kang_tang_2008]: https://doi.org/10.2514/6.2008-2595
[research_kang_yan_2026]: https://doi.org/10.1016/j.ast.2026.112141
[research_karlgaard_korzun_2020]: https://doi.org/10.2514/6.2020-1271
[research_karlgaard_schoenenberger_2022]: https://doi.org/10.2514/6.2022-0423
[research_karlgaard_stoffel_2022]: https://doi.org/10.2514/6.2022-3794
[research_karlgaard_tynis_2018]: https://doi.org/10.2514/6.2018-3624
[research_karlsdottir_halloran_2007]: https://doi.org/10.1111/j.1551-2916.2007.01861.x
[research_karp_senkardesler_2026]: https://doi.org/10.2514/6.2026-5102
[research_karthick_sriram_2019]: https://doi.org/10.3850/978-981-11-2730-4_0297-cd
[research_kasahara_matsuo_2018]: https://doi.org/10.2514/6.2018-0048
[research_kasen_queheillalt_2008]: https://doi.org/10.1115/imece2008-68823
[research_kasen_wadley_2019]: https://doi.org/10.1115/1.4042988
[research_kashkovsky_2014]: https://doi.org/10.1063/1.4902593
[research_kashyap_mitra_2020]: https://doi.org/10.1016/j.ceramint.2019.10.246
[research_kashyap_mitra_2026]: https://doi.org/10.1016/j.ceramint.2025.12.256
[research_kastantin_vey_2010]: https://doi.org/10.2514/6.2010-4864
[research_katiyar_balasubramanian_2014]: https://doi.org/10.1039/c4ra07973f
[research_katzir_cliff_1988]: https://doi.org/10.23919/acc.1988.4789708
[research_katzir_cliff_1989]: https://doi.org/10.23919/acc.1989.4790437
[research_kauffman_grandhi_1991]: https://doi.org/10.2514/6.1991-472
[research_kauffman_grandhi_1992]: https://doi.org/10.1080/03052159208941226
[research_kauffman_grandhi_1992_b]: https://doi.org/10.2514/3.46170
[research_kaufman_1963]: https://doi.org/10.21236/ad0421859
[research_kaufman_1970]: https://doi.org/10.2514/6.1970-278
[research_kaufman_louisg_1964]: https://doi.org/10.21236/ad0609559
[research_kaufman_meckler_1966]: https://doi.org/10.2514/3.43776
[research_kaushal_2024]: https://doi.org/10.61359/11.2106-2436
[research_kavoosi_mashhadi_2026]: https://doi.org/10.1016/j.ceramint.2026.07.429
[research_ke_wang_2025]: https://doi.org/10.1016/j.applthermaleng.2025.126835
[research_keeljr_kraige_1971]: https://doi.org/10.2514/6.1971-133
[research_keely_thombs_2026]: https://doi.org/10.2514/6.2026-1092.c1
[research_keely_thombs_2026_b]: https://doi.org/10.2514/6.2026-1092
[research_kelkar_vogel_2009]: https://doi.org/10.2514/6.2009-7325
[research_kelley_cliff_1981]: https://doi.org/10.2514/6.1981-1781
[research_kelley_cliff_1982]: https://doi.org/10.1002/oca.4660030307
[research_kemp_1960]: https://doi.org/10.2514/8.8637
[research_kennell_neely_2015]: https://doi.org/10.2514/6.2015-3690
[research_keren_marom_2016]: https://doi.org/10.1038/srep36837
[research_keshmiri_2008]: https://doi.org/10.2514/6.2008-2531
[research_keshmiri_colgren_2005]: https://doi.org/10.2514/6.2005-6257
[research_keshmiri_colgren_2006]: https://doi.org/10.2514/6.2006-8157
[research_keshmiri_colgren_2006_b]: https://doi.org/10.2514/6.2006-8087
[research_keshmiri_colgren_2006_c]: https://doi.org/10.2514/6.2006-8158
[research_kessler_2022]: https://doi.org/10.1016/j.orbis.2022.02.009
[research_keyes_1923]: https://doi.org/10.1002/j.2164-5876.1923.tb00056.x
[research_khalil_abdelgawad_2023]: https://doi.org/10.2514/1.a35441
[research_khan_zollars_2023]: https://doi.org/10.1109/aero55745.2023.10115683
[research_khatuntseva_2011]: https://doi.org/10.1134/s0021894411040067
[research_khlopkov_khlopkov_2014]: https://doi.org/10.4236/jamp.2014.25015
[research_khraibut_gai_2015]: https://doi.org/10.2514/6.2015-0984
[research_khraibut_gai_2017]: https://doi.org/10.1017/jfm.2017.204
[research_khraibut_gai_2019]: https://doi.org/10.1017/jfm.2019.614
[research_khraibut_gai_2019_b]: https://doi.org/10.3850/978-981-11-2730-4_0319-cd
[research_khrapko_2018]: https://doi.org/10.18502/keg.v3i3.1647
[research_khurana_suzuki_2013]: https://doi.org/10.2514/6.2013-2513
[research_kianvashrad_knight_2018]: https://doi.org/10.2514/6.2018-1812
[research_kianvashrad_knight_2019]: https://doi.org/10.2514/1.j057883
[research_kienappel_koppenwallner_1974]: https://doi.org/10.1016/b978-0-12-398150-9.50036-5
[research_kim_2017]: https://doi.org/10.1007/s10765-017-2285-8
[research_kim_chang_2025]: https://doi.org/10.2514/6.2025-1159
[research_kim_cho_1996]: https://doi.org/10.2514/6.1996-3883
[research_kim_jin_2009]: https://doi.org/10.5302/j.icros.2009.15.1.001
[research_kim_kim_2015]: https://doi.org/10.2514/6.2015-0861
[research_kim_kim_2017]: https://doi.org/10.7734/coseik.2017.30.2.179
[research_kim_kim_2021]: https://doi.org/10.1016/j.infrared.2020.103590
[research_kim_kim_2023]: https://doi.org/10.5139/jksas.2023.51.10.661
[research_kim_kim_2025]: https://doi.org/10.1007/s42405-025-01106-2
[research_kim_lee_2013]: https://doi.org/10.1007/s12206-013-0713-7
[research_kim_lee_2015]: https://doi.org/10.1007/978-3-319-17518-8_3
[research_kim_park_2025]: https://doi.org/10.52202/083092-0048
[research_kim_rasmussen_1982]: https://doi.org/10.2514/6.1982-1299
[research_kim_whang_2016]: https://doi.org/10.2514/1.g001699
[research_kim_woldeyohannis_2024]: https://doi.org/10.52202/078373-0082
[research_kim_yang_2015]: https://doi.org/10.5139/jksas.2015.43.3.243
[research_kimmel_adamczak_2011]: https://doi.org/10.21236/ada548272
[research_king_middendorf_2019]: https://doi.org/10.1016/j.ceramint.2018.10.173
[research_kinnersley_viertel_2002]: https://doi.org/10.1007/978-94-017-3008-2_53
[research_kinney_2006]: https://doi.org/10.2514/6.2006-239
[research_kinugawa_matsuno_2021]: https://doi.org/10.1299/jsmecs.2021.59.07b3
[research_kishi_joubert_2014]: https://doi.org/10.38036/jgpp.6.1_1
[research_kivel_1961]: https://doi.org/10.2514/8.8883
[research_klimin_yaroshevski_1970]: https://doi.org/10.1016/s1474-6670(17)68823-2
[research_klock_cesnik_2015]: https://doi.org/10.2514/6.2015-2711
[research_klock_cesnik_2016]: https://doi.org/10.2514/6.2016-1322
[research_klothakis_nikolos_2024]: https://doi.org/10.3390/computation12070140
[research_klothakis_nikolos_2026]: https://doi.org/10.1007/978-3-032-00094-1_18
[research_kluever_2007]: https://doi.org/10.2514/1.24864
[research_kluever_2008]: https://doi.org/10.2514/1.36950
[research_kluever_2008_b]: https://doi.org/10.2514/1.32314
[research_kluever_2022]: https://doi.org/10.2514/1.g006338
[research_klumpp_1986]: https://doi.org/10.23919/acc.1986.4789171
[research_knight_2015]: https://doi.org/10.21236/ada627597
[research_knight_kianvashrad_2023]: https://doi.org/10.1088/978-0-7503-5002-0ch5
[research_knight_kildare_2026]: https://doi.org/10.2514/6.2026-2509
[research_knight_quinn_1971]: https://doi.org/10.2514/6.1971-415
[research_knight_schmisseur_2012]: https://doi.org/10.1016/j.paerosci.2011.09.002
[research_knisely_haley_2019]: https://doi.org/10.2514/6.2019-1134
[research_knittel_lewis_2012]: https://doi.org/10.2514/6.2012-5809
[research_knox_2013]: https://doi.org/10.1115/imece2013-62517
[research_ko_quinn_1981]: https://doi.org/10.2514/6.1981-2382
[research_kobayashi_saperstein_1981]: https://doi.org/10.2514/6.1981-1061
[research_kobayashi_suzuki_2006]: https://doi.org/10.2514/6.2006-8051
[research_koch_wilken_2025]: https://doi.org/10.1007/s12567-025-00597-9
[research_koike_takahashi_2018]: https://doi.org/10.2514/6.2018-0289
[research_kojima_taguchi_2012]: https://doi.org/10.2514/6.2012-5973
[research_kokan_levack_2014]: https://doi.org/10.2514/6.2014-4342
[research_kominek_black_2006]: https://doi.org/10.21437/blizzard.2006-4
[research_kong_ren_2023]: https://doi.org/10.1007/978-981-99-4882-6_93
[research_kong_sun_2024]: https://doi.org/10.1007/978-981-97-7139-4_34
[research_kong_zhang_2025]: https://doi.org/10.1007/978-981-96-2232-0_52
[research_kontinos_gee_2001]: https://doi.org/10.2514/6.2001-2886
[research_kontis_qin_2000]: https://doi.org/10.2514/2.3545
[research_kontogiannis_cerminara_2015]: https://doi.org/10.2514/6.2015-3580
[research_kontogiannis_sobester_2015]: https://doi.org/10.2514/6.2015-1009
[research_kontogiannis_sobester_2017]: https://doi.org/10.2514/1.c033902
[research_kopp_garbers_2014]: https://doi.org/10.2514/6.2014-2531
[research_koppenwallner_1985]: https://doi.org/10.2514/6.1985-998
[research_korabelnikov_kuranov_2002]: https://doi.org/10.2514/6.2002-913
[research_korchagin_2019]: https://doi.org/10.20948/prepr-2019-55
[research_kordulla_periaux_1991]: https://doi.org/10.1007/978-3-642-76527-8_46
[research_kornreich_1963]: https://doi.org/10.2514/3.1960
[research_korte_1992]: https://doi.org/10.2514/3.11511
[research_korte_1992_b]: https://doi.org/10.2514/6.1992-332
[research_korte_kumar_1992]: https://doi.org/10.2514/6.1992-4009
[research_kothari_livingston_2011]: https://doi.org/10.2514/6.2011-2338
[research_kourtides_pitts_1988]: https://doi.org/10.1177/073490418800600501
[research_kozlov_1969]: https://doi.org/10.1115/1.3580227
[research_kraft_chapman_1993]: https://doi.org/10.2514/6.1993-5101
[research_krause_hartmann_1991]: https://doi.org/10.23919/acc.1991.4791945
[research_kremeyer_2004]: https://doi.org/10.2514/6.2004-984
[research_krouse_ellis_1966]: https://doi.org/10.21236/ad0628160
[research_krozel_weidner_1997]: https://doi.org/10.2514/6.1997-3541
[research_kubota_uchida_1999]: https://doi.org/10.1615/jpormedia.v2.i1.50
[research_kuchemann_1965]: https://doi.org/10.1016/0376-0421(65)90006-0
[research_kuipers_ioannou_2008]: https://doi.org/10.2514/6.2008-7142
[research_kuipers_ioannou_2009]: https://doi.org/10.1109/acc.2009.5160574
[research_kuipers_mirmirani_2007]: https://doi.org/10.2514/6.2007-6326
[research_kulathunga_fedorenko_2020]: https://doi.org/10.1109/acirs49895.2020.9162605
[research_kulkarni_phan_2003]: https://doi.org/10.2514/6.2003-5497
[research_kulkarni_shrekhar_2024]: https://doi.org/10.2514/6.2024-1591
[research_kumar_ahmed_2018]: https://doi.org/10.1016/j.ifacol.2018.05.109
[research_kumar_de_2021]: https://doi.org/10.1063/5.0053949
[research_kumar_kulkarni_2020]: https://doi.org/10.1061/(asce)as.1943-5525.0001180
[research_kumar_mahulikar_2016]: https://doi.org/10.1061/(asce)as.1943-5525.0000651
[research_kumar_mahulikar_2017]: https://doi.org/10.2514/1.a33688
[research_kumar_penchalaiah_2018]: https://doi.org/10.1016/j.ifacol.2018.05.020
[research_kumar_rao_2012]: https://doi.org/10.2514/1.55242
[research_kumar_rao_2014]: https://doi.org/10.2514/1.62737
[research_kumar_sarkar_2018]: https://doi.org/10.1177/0954410018795265
[research_kumar_singh_2024]: https://doi.org/10.1201/9781032713229-109
[research_kundu_2013]: https://doi.org/10.21236/ada582581
[research_kunhikrishnan_nambiar_2012]: https://doi.org/10.1007/s12043-012-0332-3
[research_kuo_1976]: https://doi.org/10.2514/6.1976-1531
[research_kuranov_korabelnikov_2008]: https://doi.org/10.2514/1.24684
[research_kuranov_korabelnikov_2012]: https://doi.org/10.2514/6.2012-5879
[research_kuranov_korabelnikov_2016]: https://doi.org/10.1134/s0018151x16030093
[research_kurilova_li_2026]: https://doi.org/10.1109/aero66936.2026.11519972
[research_kuroda_imado_1990]: https://doi.org/10.2514/6.1990-3379
[research_kushner_littell_2013]: https://doi.org/10.2514/6.2013-1284
[research_kussoy_horstman_1970]: https://doi.org/10.2514/3.5662
[research_kutkan_eyi_2018]: https://doi.org/10.2514/6.2018-4071
[research_kwon_hong_2021]: https://doi.org/10.5139/jksas.2021.49.1.21
[research_l_rao_2025]: https://doi.org/10.1109/mapcon65020.2025.11426436
[research_lacombe_rouges_1990]: https://doi.org/10.2514/6.1990-3837
[research_lafleur_2009]: https://doi.org/10.2514/6.2009-5612
[research_lago_chpoun_2012]: https://doi.org/10.1007/978-3-642-25119-1_8
[research_lakin_smotzer_2025]: https://doi.org/10.2514/6.2025-3530
[research_lakshman_sriram_2017]: https://doi.org/10.1007/978-3-319-44866-4_69
[research_lam_2008]: https://doi.org/10.2514/6.2008-7304
[research_lan_huiping_2026]: https://doi.org/10.1016/j.ceramint.2026.03.021
[research_lan_wang_2014]: https://doi.org/10.3182/20140824-6-za-1003.01209
[research_landon_hall_1994]: https://doi.org/10.2514/6.1994-1898
[research_lane_salmassy_1993]: https://doi.org/10.2514/6.1993-2791
[research_lanejr_kirlin_1978]: https://doi.org/10.2514/6.1978-478
[research_lang_jacobs_1997]: https://doi.org/10.1007/978-3-322-86573-1_27
[research_lanzano_1961]: https://doi.org/10.1007/978-94-015-6337-6_15
[research_lapygin_yakunina_2009]: https://doi.org/10.1016/j.jappmathmech.2009.11.004
[research_large_1962]: https://doi.org/10.2514/8.9308
[research_lasorsa_sprunger_2025]: https://doi.org/10.2514/6.2025-1327
[research_laster_jordan_2006]: https://doi.org/10.2514/6.2006-2957
[research_lau_1979]: https://doi.org/10.1016/s0307-904x(79)80062-1
[research_lau_2008]: https://doi.org/10.2514/1.31134
[research_laurmann_1964]: https://doi.org/10.2514/3.2641
[research_law_gliponeo_2023]: https://doi.org/10.34190/iccws.18.1.950
[research_lawson_daw_2011]: https://doi.org/10.1063/1.3647754
[research_lazarev_1999]: https://doi.org/10.2514/6.1999-4865
[research_lazur_sawyer_1999]: https://doi.org/10.2514/6.1999-4864
[research_le_liu_2023]: https://doi.org/10.3390/drones7020119
[research_leavitt_mease_2007]: https://doi.org/10.2514/1.23034
[research_lecerf_villers_2014]: https://doi.org/10.1109/eucap.2014.6902215
[research_lee_2006]: https://doi.org/10.1007/bf02916260
[research_lee_2013]: https://doi.org/10.2514/6.2013-4951
[research_lee_2023]: https://doi.org/10.5139/jksas.2023.51.3.183
[research_lee_cho_2002]: https://doi.org/10.1007/bf02939333
[research_lee_cho_2006]: https://doi.org/10.3182/20060517-3-fr-2903.00177
[research_lee_jamest_1963]: https://doi.org/10.21236/ad0406459
[research_lee_kim_2021]: https://doi.org/10.1063/5.0057473
[research_lee_kim_2022]: https://doi.org/10.2514/6.2022-1500
[research_lee_kim_2026]: https://doi.org/10.2514/6.2026-5074
[research_lee_lee_2022]: https://doi.org/10.1007/978-981-19-2635-8_14
[research_lee_lee_2022_b]: https://doi.org/10.2514/6.2022-0957
[research_lee_liu_1999]: https://doi.org/10.2514/2.4482
[research_lee_reiman_2007]: https://doi.org/10.2514/6.2007-6685
[research_lee_seo_2018]: https://doi.org/10.2514/1.g002817
[research_lee_zheng_1999]: https://doi.org/10.2514/6.1999-3687
[research_lee_zhong_2003]: https://doi.org/10.2514/2.3946
[research_lees_1956]: https://doi.org/10.2514/8.3614
[research_lees_1956_b]: https://doi.org/10.2514/8.6977
[research_lehr_simecekbeatty_2003]: https://doi.org/10.7901/2169-3358-2003-1-435
[research_lei_wang_2026]: https://doi.org/10.1016/j.icheatmasstransfer.2026.111415
[research_lei_yan_2017]: https://doi.org/10.2514/6.2017-2256
[research_leite_afonso_2022]: https://doi.org/10.3390/fluids7110353
[research_leng_qian_2017]: https://doi.org/10.2514/6.2017-2244
[research_leng_shen_2025]: https://doi.org/10.1016/j.energy.2025.134730
[research_leng_wang_2024]: https://doi.org/10.1016/j.energy.2024.132076
[research_leng_xie_2025]: https://doi.org/10.1016/j.ast.2025.110033
[research_leonardi_2023]: https://doi.org/10.21741/9781644902813-134
[research_leonardi_pontani_2024]: https://doi.org/10.1007/s42496-024-00210-y
[research_lepore_2006]: https://doi.org/10.2514/6.iac-06-d2.1.09
[research_lesin_1976]: https://doi.org/10.1007/bf01026419
[research_lessing_coate_1965]: https://doi.org/10.2514/6.1965-1241
[research_lessing_tunnell_1963]: https://doi.org/10.2514/6.1963-1422
[research_letkemann_tropina_2024]: https://doi.org/10.2514/6.2024-3983
[research_letkemann_tropina_2026]: https://doi.org/10.2514/1.t7167
[research_lettsjr_castle_1981]: https://doi.org/10.2514/6.1981-1860
[research_levensteins_krumins_1967]: https://doi.org/10.2514/3.4256
[research_levin_delaurentis_2024]: https://doi.org/10.1109/aero58975.2024.10521344
[research_levin_ioannou_2008]: https://doi.org/10.2514/6.2008-7137
[research_lewellen_mirels_1966]: https://doi.org/10.2514/3.3803
[research_lewis_1991]: https://doi.org/10.2514/6.1991-3304
[research_lewis_1999]: https://doi.org/10.4271/1999-01-5514
[research_lewis_2001]: https://doi.org/10.2514/2.5866
[research_lewis_2017]: https://doi.org/10.1063/1.5009210
[research_lewis_chauffour_2005]: https://doi.org/10.2514/1.13027
[research_lewis_takashima_1993]: https://doi.org/10.2514/6.1993-507
[research_li_2013]: https://doi.org/10.4028/www.scientific.net/amm.278-280.1496
[research_li_2021]: https://doi.org/10.23919/ccc52363.2021.9549545
[research_li_2021_b]: https://doi.org/10.23919/ccc52363.2021.9550532
[research_li_an_2014]: https://doi.org/10.2514/6.2014-3229
[research_li_cai_2025]: https://doi.org/10.1016/j.dt.2025.04.020
[research_li_chang_2024]: https://doi.org/10.1109/ccdc62350.2024.10587813
[research_li_chao_2016]: https://doi.org/10.1109/chicc.2016.7555065
[research_li_chao_2018]: https://doi.org/10.23919/chicc.2018.8482793
[research_li_chao_2022]: https://doi.org/10.1016/j.ast.2022.107364
[research_li_chen_2011]: https://doi.org/10.4028/www.scientific.net/amm.110-116.5118
[research_li_chen_2016]: https://doi.org/10.1109/icma.2016.7558761
[research_li_chen_2017]: https://doi.org/10.23919/chicc.2017.8029006
[research_li_chen_2020]: https://doi.org/10.12783/dtetr/amee2019/33499
[research_li_chen_2025]: https://doi.org/10.1063/5.0290941
[research_li_cheng_2011]: https://doi.org/10.3969/j.issn.1004-4132.2011.01.018
[research_li_cheng_2025]: https://doi.org/10.1016/j.energy.2025.134377
[research_li_cui_2009]: https://doi.org/10.1108/00022660910926854
[research_li_cui_2009_b]: https://doi.org/10.1109/icma.2009.5246695
[research_li_cui_2020]: https://doi.org/10.1007/s11433-019-1487-7
[research_li_fang_2008]: https://doi.org/10.4028/0-87849-473-1.1782
[research_li_fang_2008_b]: https://doi.org/10.1142/s021798490801608x
[research_li_feng_2026]: https://doi.org/10.1016/j.ast.2025.111490
[research_li_foerst_2006]: https://doi.org/10.1149/ma2006-02/18/961
[research_li_fu_2010]: https://doi.org/10.1109/car.2010.5456775
[research_li_gao_2014]: https://doi.org/10.2514/6.2014-4414
[research_li_he_2019]: https://doi.org/10.1016/j.ast.2019.03.056
[research_li_he_2025]: https://doi.org/10.1016/j.ast.2025.109960
[research_li_hu_2013]: https://doi.org/10.4028/www.scientific.net/msf.745-746.636
[research_li_hu_2018]: https://doi.org/10.1016/j.ast.2018.01.033
[research_li_hu_2020]: https://doi.org/10.1016/j.ast.2020.106231
[research_li_hu_2025]: https://doi.org/10.1016/j.aej.2024.11.090
[research_li_huang_2017]: https://doi.org/10.5772/67783
[research_li_huang_2018]: https://doi.org/10.1115/gt2018-75151
[research_li_huang_2020]: https://doi.org/10.1007/s40145-019-0332-6
[research_li_jia_2017]: https://doi.org/10.23919/chicc.2017.8028866
[research_li_jiang_2021]: https://doi.org/10.1186/s42774-021-00063-0
[research_li_jiang_2021_b]: https://doi.org/10.1109/iaecst54258.2021.9695560
[research_li_jiang_2025]: https://doi.org/10.1016/j.cja.2024.09.001
[research_li_jing_2008]: https://doi.org/10.1109/isscaa.2008.4776294
[research_li_li_2012]: https://doi.org/10.1016/j.engfracmech.2011.11.016
[research_li_li_2012_b]: https://doi.org/10.1007/s10704-012-9743-x
[research_li_li_2012_c]: https://doi.org/10.1088/0031-8949/86/05/055402
[research_li_li_2020]: https://doi.org/10.1016/j.ast.2019.105540
[research_li_li_2022]: https://doi.org/10.1007/978-981-19-2689-1_37
[research_li_li_2022_b]: https://doi.org/10.1109/access.2021.3136612
[research_li_li_2023]: https://doi.org/10.3390/aerospace10050441
[research_li_li_2024]: https://doi.org/10.1109/cac63892.2024.10864770
[research_li_lin_2011]: https://doi.org/10.1016/s1000-9361(11)60010-1
[research_li_liu_2021]: https://doi.org/10.1007/978-981-15-8155-7_288
[research_li_liu_2024]: https://doi.org/10.1007/978-981-99-6282-2_10
[research_li_liu_2024_b]: https://doi.org/10.1007/978-981-99-6282-2_8
[research_li_liu_2024_c]: https://doi.org/10.1007/978-981-99-6282-2_4
[research_li_liu_2024_d]: https://doi.org/10.1007/978-981-99-6282-2_3
[research_li_liu_2024_e]: https://doi.org/10.1007/978-981-99-6282-2_6
[research_li_liu_2024_f]: https://doi.org/10.1007/978-981-99-6282-2_5
[research_li_liu_2024_g]: https://doi.org/10.1007/978-981-99-6282-2_12
[research_li_liu_2024_h]: https://doi.org/10.1007/978-981-99-6282-2_11
[research_li_liu_2025]: https://doi.org/10.1007/978-981-96-2232-0_33
[research_li_liu_2025_b]: https://doi.org/10.1007/978-981-96-2216-0_20
[research_li_long_2024]: https://doi.org/10.1109/robio64047.2024.10907649
[research_li_luo_2013]: https://doi.org/10.1016/j.ast.2013.07.003
[research_li_lv_2016]: https://doi.org/10.2991/icmmct-16.2016.268
[research_li_ma_2016]: https://doi.org/10.1177/1729881416663376
[research_li_ma_2021]: https://doi.org/10.1109/yac53711.2021.9486509
[research_li_ma_2024]: https://doi.org/10.1016/j.ast.2024.109461
[research_li_mao_2025]: https://doi.org/10.1007/978-981-96-2216-0_19
[research_li_meng_2008]: https://doi.org/10.4028/0-87849-473-1.1761
[research_li_peng_2019]: https://doi.org/10.1109/icus48101.2019.8996088
[research_li_qi_2023]: https://doi.org/10.1117/12.2661622
[research_li_shen_2010]: https://doi.org/10.1061/41096(366)178
[research_li_shen_2014]: https://doi.org/10.4236/jamp.2014.26053
[research_li_shen_2015]: https://doi.org/10.1016/j.proeng.2014.12.716
[research_li_si_2010]: https://doi.org/10.1109/isscaa.2010.5634035
[research_li_song_2026]: https://doi.org/10.1016/j.ast.2026.113052
[research_li_sun_2019]: https://doi.org/10.1109/iaeac47372.2019.8997697
[research_li_sun_2025]: https://doi.org/10.1007/978-981-95-3010-6_37
[research_li_tao_2023]: https://doi.org/10.2514/1.g007483
[research_li_tian_2019]: https://doi.org/10.1088/1742-6596/1168/5/052034
[research_li_wang_2010]: https://doi.org/10.4304/jcp.5.7.1003-1010
[research_li_wang_2014]: https://doi.org/10.1007/978-3-642-54236-7_4
[research_li_wang_2016]: https://doi.org/10.1016/j.actaastro.2016.05.031
[research_li_wang_2017]: https://doi.org/10.1016/j.actaastro.2017.05.001
[research_li_wang_2021]: https://doi.org/10.1155/2021/9975007
[research_li_wang_2021_b]: https://doi.org/10.1109/ccdc52312.2021.9601982
[research_li_wang_2024]: https://doi.org/10.1016/j.energy.2024.134084
[research_li_wang_2024_b]: https://doi.org/10.1016/j.cja.2024.02.024
[research_li_wang_2025]: https://doi.org/10.1007/978-981-96-2224-5_41
[research_li_wey_1988]: https://doi.org/10.2514/6.1988-2675
[research_li_wu_2011]: https://doi.org/10.1002/oca.1008
[research_li_wu_2017]: https://doi.org/10.2514/6.2017-2344
[research_li_wu_2025]: https://doi.org/10.1016/j.ast.2025.110401
[research_li_xiao_2017]: https://doi.org/10.2514/6.2017-2254
[research_li_xin_2017]: https://doi.org/10.23919/acc.2017.7963286
[research_li_xiong_2012]: https://doi.org/10.4028/www.scientific.net/amm.232.299
[research_li_xiong_2022]: https://doi.org/10.1109/access.2021.3139434
[research_li_xu_2011]: https://doi.org/10.4028/www.scientific.net/amm.128-129.761
[research_li_xu_2023]: https://doi.org/10.1007/978-981-19-6613-2_548
[research_li_xu_2026]: https://doi.org/10.3390/vibration9010008
[research_li_yang_2009]: https://doi.org/10.1007/s10409-009-0326-7
[research_li_yang_2009_b]: https://doi.org/10.1016/j.camwa.2009.03.080
[research_li_yang_2012]: https://doi.org/10.1166/asl.2012.1989
[research_li_yang_2016]: https://doi.org/10.1155/2016/9407238
[research_li_yang_2018]: https://doi.org/10.1016/j.applthermaleng.2018.03.084
[research_li_yang_2022]: https://doi.org/10.1016/j.cja.2021.08.026
[research_li_yu_2024]: https://doi.org/10.1109/meae62008.2024.11026517
[research_li_yu_2025]: https://doi.org/10.1016/j.icarus.2025.116537
[research_li_zhang_2012]: https://doi.org/10.1016/s1000-9361(11)60384-1
[research_li_zhang_2014]: https://doi.org/10.1109/cgncc.2014.7007281
[research_li_zhang_2015]: https://doi.org/10.1016/j.ast.2015.03.016
[research_li_zhang_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000667
[research_li_zhang_2017_b]: https://doi.org/10.1115/omae2017-61171
[research_li_zhang_2021]: https://doi.org/10.1115/fedsm2021-61455
[research_li_zhang_2024]: https://doi.org/10.1016/j.ast.2024.109295
[research_li_zhang_2025]: https://doi.org/10.23919/ccc64809.2025.11178324
[research_li_zhang_2026]: https://doi.org/10.26599/jac.2025.9221231
[research_li_zhao_2014]: https://doi.org/10.2514/6.2014-2818
[research_li_zhao_2024]: https://doi.org/10.52202/078365-0049
[research_li_zhao_2026]: https://doi.org/10.1088/1742-6596/3207/1/012072
[research_li_zhou_2021]: https://doi.org/10.3390/app11209565
[research_li_zhou_2022]: https://doi.org/10.1155/2022/4625001
[research_li_zhou_2022_b]: https://doi.org/10.3390/app122110796
[research_li_zhou_2022_c]: https://doi.org/10.1155/2022/7313586
[research_li_zhou_2023]: https://doi.org/10.1007/978-981-19-6613-2_517
[research_li_zhou_2023_b]: https://doi.org/10.3390/app13031988
[research_lian_bai_2013]: https://doi.org/10.4028/www.scientific.net/amm.427-429.913
[research_lian_bai_2013_b]: https://doi.org/10.1109/imccc.2013.328
[research_lian_shi_2012]: https://doi.org/10.1007/978-3-642-34381-0_16
[research_liang_han_2008]: https://doi.org/10.1109/isic.2008.4635959
[research_liang_han_2010]: https://doi.org/10.3724/sp.j.1004.2010.01534
[research_liang_han_2015]: https://doi.org/10.1061/(asce)as.1943-5525.0000426
[research_liang_hu_2023]: https://doi.org/10.23919/ccc58697.2023.10239908
[research_liang_liu_2009]: https://doi.org/10.1109/itcs.2009.95
[research_liang_luo_2024]: https://doi.org/10.3390/math12091306
[research_liang_mease_2019]: https://doi.org/10.2514/1.g004027
[research_liang_ren_2015]: https://doi.org/10.1109/jas.2015.7032913
[research_liang_wen_2025]: https://doi.org/10.23919/ccc64809.2025.11178558
[research_liang_xu_2021]: https://doi.org/10.1016/j.ast.2021.106566
[research_liang_xu_2023]: https://doi.org/10.1109/tsmc.2023.3264552
[research_liang_xu_2025]: https://doi.org/10.1109/taes.2024.3452051
[research_liang_yi_2016]: https://doi.org/10.1109/chicc.2016.7554240
[research_liang_yu_2017]: https://doi.org/10.2514/6.2017-2251
[research_liang_zhen_2016]: https://doi.org/10.1177/1729881416678136
[research_liao_isaac_1992]: https://doi.org/10.2514/3.11096
[research_liao_li_2013]: https://doi.org/10.1109/ccdc.2013.6560989
[research_liao_luo_2026]: https://doi.org/10.1016/j.ast.2025.110944
[research_liaoniwu_yiminhuang_2008]: https://doi.org/10.1109/isscaa.2008.4776287
[research_licata_1977]: https://doi.org/10.2514/6.1977-1089
[research_licheri_orru_2009]: https://doi.org/10.3103/s106138620901004x
[research_licheri_orru_2010]: https://doi.org/10.3103/s1061386210040096
[research_licheri_orru_2010_b]: https://doi.org/10.4028/www.scientific.net/ast.65.118
[research_lichodziejewski_dillman_2013]: https://doi.org/10.2514/6.2013-1864
[research_liechty_2008]: https://doi.org/10.2514/6.2008-1240
[research_light_high_temperature_1992]: https://doi.org/10.2514/5.9781600866128.0141.0160
[research_liguore_tzong_2011]: https://doi.org/10.2514/6.2011-1961
[research_lin_1983]: https://doi.org/10.2514/6.1983-2203
[research_lin_chen_2025]: https://doi.org/10.1007/978-981-96-2232-0_6
[research_lin_he_2020]: https://doi.org/10.1109/cac51589.2020.9326663
[research_lin_huang_2014]: https://doi.org/10.1016/j.matchar.2014.07.002
[research_lin_huang_2015]: https://doi.org/10.1016/j.ceramint.2015.04.148
[research_lin_luo_1995]: https://doi.org/10.2514/6.1995-1849
[research_lin_mckeel_2000]: https://doi.org/10.2514/6.2000-636
[research_lin_shen_1996]: https://doi.org/10.2514/3.26807
[research_lin_shen_1996_b]: https://doi.org/10.2514/3.13298
[research_lin_shen_1997]: https://doi.org/10.1016/s0045-7930(96)00026-6
[research_lin_sproul_2003]: https://doi.org/10.2514/2.6891
[research_lin_sproul_2006]: https://doi.org/10.2514/6.2006-582
[research_lin_tsai_1987]: https://doi.org/10.2514/3.20181
[research_lin_wallington_2025]: https://doi.org/10.1007/s12567-025-00606-x
[research_lin_zhuang_2025]: https://doi.org/10.1007/978-981-96-3564-1_19
[research_lind_buffington_1999]: https://doi.org/10.2514/6.1999-4123
[research_ling_wang_2025]: https://doi.org/10.1109/rcae66389.2025.11355185
[research_linlin_jianqiao_2015]: https://doi.org/10.1109/chicc.2015.7260426
[research_linqi_qun_2015]: https://doi.org/10.1109/chicc.2015.7259769
[research_lippitt_jr_1983]: https://doi.org/10.21236/ada130685
[research_liquan_nan_2020]: https://doi.org/10.1109/icise51755.2020.00046
[research_liqun_chaoyang_2017]: https://doi.org/10.1109/ccdc.2017.7979401
[research_liu_1967]: https://doi.org/10.2514/3.43830
[research_liu_2009]: https://doi.org/10.14429/dsj.59.1498
[research_liu_2017]: https://doi.org/10.23919/chicc.2017.8028308
[research_liu_2020]: https://doi.org/10.1088/1742-6596/1509/1/012006
[research_liu_2025]: https://doi.org/10.1007/978-981-96-2440-9_2
[research_liu_bai_2017]: https://doi.org/10.2514/6.2017-2140
[research_liu_bai_2020]: https://doi.org/10.2514/6.2020-2424
[research_liu_bai_2021]: https://doi.org/10.1016/j.ast.2020.106422
[research_liu_bai_2024]: https://doi.org/10.2514/1.j063558
[research_liu_chen_2002]: https://doi.org/10.21236/ada403577
[research_liu_chen_2011]: https://doi.org/10.1109/rast.2011.5966841
[research_liu_chen_2014]: https://doi.org/10.1177/0142331213516034
[research_liu_chen_2017]: https://doi.org/10.2991/icmeit-17.2017.16
[research_liu_chen_2019]: https://doi.org/10.1007/978-981-13-3305-7_40
[research_liu_chen_2019_b]: https://doi.org/10.2514/6.2019-1595
[research_liu_chen_2022]: https://doi.org/10.1007/978-981-16-9492-9_54
[research_liu_chen_2026]: https://doi.org/10.3390/act15070379
[research_liu_cui_2023]: https://doi.org/10.1109/icfeict59519.2023.00076
[research_liu_cui_2024]: https://doi.org/10.3390/aerospace11090785
[research_liu_deng_2013]: https://doi.org/10.1109/maes.2013.6516146
[research_liu_deng_2025]: https://doi.org/10.1088/1742-6596/3069/1/012001
[research_liu_ding_2014]: https://doi.org/10.1016/j.actaastro.2014.04.024
[research_liu_dong_2019]: https://doi.org/10.3850/978-981-11-2730-4_0126-cd
[research_liu_dong_2020]: https://doi.org/10.1016/j.ast.2019.105537
[research_liu_dong_2021]: https://doi.org/10.1016/j.cja.2020.04.026
[research_liu_duan_2014]: https://doi.org/10.2514/6.2014-0189
[research_liu_duan_2018]: https://doi.org/10.1080/00207721.2018.1457732
[research_liu_fang_2023]: https://doi.org/10.1088/1742-6596/2636/1/012047
[research_liu_gao_2019]: https://doi.org/10.1016/j.flowmeasinst.2019.101646
[research_liu_guo_2022]: https://doi.org/10.1016/j.ceramint.2022.02.101
[research_liu_han_2019]: https://doi.org/10.1016/j.ast.2019.105345
[research_liu_he_2017]: https://doi.org/10.23919/chicc.2017.8028281
[research_liu_hou_2010]: https://doi.org/10.1109/isscaa.2010.5633608
[research_liu_hou_2020]: https://doi.org/10.32604/cmes.2020.08124
[research_liu_hu_2023]: https://doi.org/10.1007/978-981-19-6613-2_440
[research_liu_hu_2025]: https://doi.org/10.1016/j.ifacol.2025.11.182
[research_liu_jiang_2013]: https://doi.org/10.2514/1.j051875
[research_liu_jiang_2025]: https://doi.org/10.3233/atde250043
[research_liu_jun_2016]: https://doi.org/10.1115/gt2016-56929
[research_liu_lei_2026]: https://doi.org/10.1631/jzus.a2500144
[research_liu_li_2015]: https://doi.org/10.1016/j.proeng.2014.12.521
[research_liu_li_2022]: https://doi.org/10.2514/1.g006237
[research_liu_li_2025]: https://doi.org/10.3390/aerospace12060539
[research_liu_liang_2016]: https://doi.org/10.1109/chicc.2016.7554222
[research_liu_liang_2025]: https://doi.org/10.1016/j.ast.2025.110448
[research_liu_liang_2026]: https://doi.org/10.1007/978-981-95-8435-2_9
[research_liu_liu_2016]: https://doi.org/10.1016/j.actaastro.2015.10.011
[research_liu_liu_2016_b]: https://doi.org/10.1016/j.actaastro.2015.10.015
[research_liu_liu_2018]: https://doi.org/10.1061/(asce)as.1943-5525.0000864
[research_liu_liu_2018_b]: https://doi.org/10.1080/00207179.2018.1426882
[research_liu_liu_2019]: https://doi.org/10.1016/j.ast.2019.01.029
[research_liu_liu_2022]: https://doi.org/10.1080/00207179.2022.2106891
[research_liu_liu_2023]: https://doi.org/10.1061/jaeeez.aseng-4711
[research_liu_liu_2023_b]: https://doi.org/10.2514/1.j062254
[research_liu_liu_2026]: https://doi.org/10.1007/s42405-026-01147-1
[research_liu_lu_2011]: https://doi.org/10.1177/0954410011406629
[research_liu_lu_2015]: https://doi.org/10.1155/2015/510414
[research_liu_lu_2024]: https://doi.org/10.3390/drones8090505
[research_liu_luo_2020]: https://doi.org/10.1007/s42401-020-00061-y
[research_liu_luo_2020_b]: https://doi.org/10.1109/cac51589.2020.9327809
[research_liu_mu_2023]: https://doi.org/10.1007/978-981-99-8861-7_49
[research_liu_pang_2022]: https://doi.org/10.1016/j.flowmeasinst.2022.102264
[research_liu_peng_2016]: https://doi.org/10.2514/6.2016-3288
[research_liu_qiang_2012]: https://doi.org/10.4028/www.scientific.net/amr.429.147
[research_liu_ren_2026]: https://doi.org/10.1016/j.ast.2026.112327
[research_liu_shao_2025]: https://doi.org/10.1109/ccdc65474.2025.11091261
[research_liu_shen_2015]: https://doi.org/10.1007/s10957-015-0831-8
[research_liu_shi_2018]: https://doi.org/10.1615/ihtc16.tpm.022494
[research_liu_tang_2013]: https://doi.org/10.1109/icnc.2013.6817988
[research_liu_tang_2017]: https://doi.org/10.1109/ccdc.2017.7979467
[research_liu_tang_2025]: https://doi.org/10.65904/3083-3450.2025.01.07
[research_liu_wang_2005]: https://doi.org/10.14429/dsj.55.1999
[research_liu_wang_2014]: https://doi.org/10.1109/chicc.2014.6896504
[research_liu_wang_2016]: https://doi.org/10.1109/chicc.2016.7555029
[research_liu_wang_2017]: https://doi.org/10.2514/6.2017-2153
[research_liu_wang_2024]: https://doi.org/10.52202/078373-0095
[research_liu_wang_2025]: https://doi.org/10.1016/j.exm.2025.01.001
[research_liu_wu_2026]: https://doi.org/10.1007/978-981-92-0375-8_21
[research_liu_wu_2026_b]: https://doi.org/10.2514/1.c039065
[research_liu_xiao_2007]: https://doi.org/10.2514/6.2007-5413
[research_liu_xie_2021]: https://doi.org/10.1109/cacre52464.2021.9501317
[research_liu_xing_2024]: https://doi.org/10.23919/ccc63176.2024.10662442
[research_liu_xu_2026]: https://doi.org/10.1063/5.0339067
[research_liu_yan_2022]: https://doi.org/10.3390/ma15082886
[research_liu_yan_2022_b]: https://doi.org/10.1016/j.ast.2022.107908
[research_liu_yu_2012]: https://doi.org/10.1109/jsee.2012.00086
[research_liu_zhang_2018]: https://doi.org/10.1360/n092017-00373
[research_liu_zhang_2020]: https://doi.org/10.2514/1.j059087
[research_liu_zhang_2021]: https://doi.org/10.2514/1.j059904
[research_liu_zhang_2024]: https://doi.org/10.1007/978-981-97-1107-9_37
[research_liu_zhang_2025]: https://doi.org/10.1109/cac67268.2025.11487632
[research_liu_zheng_2024]: https://doi.org/10.1016/j.ast.2024.109545
[research_liu_zhou_2023]: https://doi.org/10.1007/978-981-19-6613-2_26
[research_liu_zhou_2025]: https://doi.org/10.1109/cac67268.2025.11487274
[research_liuyuan_zhangxiangyu_2015]: https://doi.org/10.1049/cp.2015.0971
[research_lizhihuai_tanxiansi_2011]: https://doi.org/10.1109/cie-radar.2011.6159801
[research_lloyd_brown_1979]: https://doi.org/10.2514/3.55833
[research_lobanovsky_2014]: https://doi.org/10.1615/tsagiscij.2014012528
[research_lobbia_2015]: https://doi.org/10.2514/6.2015-0757
[research_lobbia_2017]: https://doi.org/10.2514/1.a33253
[research_lobbia_suzuki_2001]: https://doi.org/10.2514/6.2001-1849
[research_lobbia_suzuki_2003]: https://doi.org/10.2514/6.2003-3804
[research_lobbia_suzuki_2014]: https://doi.org/10.2514/6.2014-2359
[research_lock_oberman_2025]: https://doi.org/10.2514/6.2025-1337
[research_lohle_hermann_2017]: https://doi.org/10.1007/s12567-017-0186-0
[research_lohsoonthorn_jonckheere_2001]: https://doi.org/10.2514/2.4781
[research_lonari_naber_2024]: https://doi.org/10.4271/2024-01-2661
[research_long_hanus_1989]: https://doi.org/10.2514/6.1989-44
[research_long_li_2026]: https://doi.org/10.1016/j.asr.2026.03.053
[research_long_zhu_2020]: https://doi.org/10.1016/j.ast.2020.106213
[research_longo_2008]: https://doi.org/10.2514/6.2008-4038
[research_lorenz_putnam_2017]: https://doi.org/10.2514/6.2017-0247
[research_lu_1991]: https://doi.org/10.2514/6.1991-5068
[research_lu_1996]: https://doi.org/10.2514/3.21585
[research_lu_1996_b]: https://doi.org/10.2514/6.1996-3700
[research_lu_1997]: https://doi.org/10.2514/2.4008
[research_lu_1999]: https://doi.org/10.2514/2.4479
[research_lu_2005]: https://doi.org/10.2514/6.2005-6128
[research_lu_2006]: https://doi.org/10.2514/1.15789
[research_lu_2008]: https://doi.org/10.2514/1.32055
[research_lu_2008_b]: https://doi.org/10.2514/6.2008-7268
[research_lu_2014]: https://doi.org/10.2514/1.62605
[research_lu_2021]: https://doi.org/10.1016/j.cja.2020.09.053
[research_lu_doman_2005]: https://doi.org/10.2514/6.2005-6059
[research_lu_doman_2006]: https://doi.org/10.2514/1.14367
[research_lu_guo_2025]: https://doi.org/10.1007/978-981-96-2268-9_3
[research_lu_hanson_1997]: https://doi.org/10.2514/6.1997-3580
[research_lu_hanson_1998]: https://doi.org/10.2514/2.3332
[research_lu_qian_2024]: https://doi.org/10.3390/drones8080377
[research_lu_shen_2000]: https://doi.org/10.2514/6.2000-3958
[research_lu_zhang_2016]: https://doi.org/10.2991/imst-16.2016.15
[research_lu_zhang_2016_b]: https://doi.org/10.1109/cgncc.2016.7828815
[research_lu_zhang_2025]: https://doi.org/10.3390/math13030380
[research_lu_zheng_2022]: https://doi.org/10.1007/978-981-16-9492-9_258
[research_lu_zhou_2017]: https://doi.org/10.1177/0142331217735050
[research_lu_zhou_2017_b]: https://doi.org/10.1109/ccdc.2017.7978461
[research_lubing_yangfei_2020]: https://doi.org/10.23919/ccc50068.2020.9189249
[research_lukacs_yakimenko_2007]: https://doi.org/10.2514/6.2007-6538
[research_lukacs_yakimenko_2008]: https://doi.org/10.2514/1.32262
[research_lunan_1990]: https://doi.org/10.1016/0265-9646(90)90090-k
[research_lunan_2015]: https://doi.org/10.2514/6.2015-3529
[research_luo_baysal_1999]: https://doi.org/10.2514/6.1999-4807
[research_luo_chen_2019]: https://doi.org/10.3850/978-981-11-2730-4_0138-cd
[research_luo_gao_2015]: https://doi.org/10.1201/b19362-36
[research_luo_he_2025]: https://doi.org/10.1007/978-981-96-2228-3_6
[research_luo_lei_2023]: https://doi.org/10.1016/j.jer.2023.100074
[research_luo_li_2011]: https://doi.org/10.1007/s11432-011-4193-z
[research_luo_li_2024]: https://doi.org/10.1109/meae62008.2024.11026303
[research_luo_luo_2003]: https://doi.org/10.2514/6.2003-5193
[research_luo_miao_2021]: https://doi.org/10.3389/fenrg.2021.756820
[research_luo_su_2016]: https://doi.org/10.1360/n112015-00172
[research_luo_sun_2022]: https://doi.org/10.1016/j.ast.2022.107964
[research_luo_sun_2025]: https://doi.org/10.1016/j.ast.2025.110259
[research_luo_wu_2022]: https://doi.org/10.1016/j.asr.2022.02.049
[research_luo_zhang_2014]: https://doi.org/10.2514/1.g000441
[research_luo_zhang_2015]: https://doi.org/10.1016/j.actaastro.2015.07.028
[research_lusty_miele_1966]: https://doi.org/10.2514/3.3866
[research_lv_cai_2019]: https://doi.org/10.23919/chicc.2019.8866423
[research_lv_jiang_2014]: https://doi.org/10.2514/6.2014-4346
[research_lv_lan_2024]: https://doi.org/10.1016/j.ast.2023.108804
[research_lv_li_2015]: https://doi.org/10.1007/978-3-319-16835-7_103
[research_lv_wang_2023]: https://doi.org/10.1016/j.neucom.2022.11.057
[research_lv_zhang_2026]: https://doi.org/10.1109/tase.2025.3641526
[research_lv_zhou_2023]: https://doi.org/10.1142/s2737480723500115
[research_lyons_1977]: https://doi.org/10.1051/rphysap:01977001202038500
[research_lyu_jiang_2018]: https://doi.org/10.2514/6.2018-0279
[research_ma_chao_2012]: https://doi.org/10.1007/978-3-642-34390-2_21
[research_ma_chen_2024]: https://doi.org/10.1109/icca62789.2024.10591915
[research_ma_du_2019]: https://doi.org/10.1109/access.2019.2936086
[research_ma_hu_2023]: https://doi.org/10.1007/978-981-19-7652-0_6
[research_ma_li_2026]: https://doi.org/10.1109/ccdc69976.2026.11560308
[research_ma_liu_2024]: https://doi.org/10.23919/ccc63176.2024.10661212
[research_ma_she_2011]: https://doi.org/10.1007/s11768-011-0012-8
[research_ma_sun_2024]: https://doi.org/10.1016/j.cja.2024.05.033
[research_ma_wan_2026]: https://doi.org/10.1007/978-981-95-3037-3_20
[research_ma_xie_2021]: https://doi.org/10.2139/ssrn.3983112
[research_ma_xue_2025]: https://doi.org/10.1016/j.ast.2025.110382
[research_ma_yang_2014]: https://doi.org/10.1177/0954410014548699
[research_ma_yang_2024]: https://doi.org/10.1016/j.ast.2024.108969
[research_ma_yin_2022]: https://doi.org/10.54097/fcis.v2i1.3343
[research_ma_zhong_2017]: https://doi.org/10.2514/6.2017-2171
[research_machado_2018]: https://doi.org/10.26678/abcm.encit2018.cit18-0011
[research_mackle_jahn_2024]: https://doi.org/10.2514/6.2024-2838
[research_mackle_lock_2024]: https://doi.org/10.2514/6.2024-0238
[research_magister_2012]: https://doi.org/10.7307/ptt.v21i5.246
[research_mahato_sarikonda_2023]: https://doi.org/10.2514/6.2023-3035
[research_mahmood_duraihem_2023]: https://doi.org/10.1080/10407790.2023.2270155
[research_mahmoud_hao_2017]: https://doi.org/10.1109/iccairo.2017.35
[research_mahulikar_2005]: https://doi.org/10.1016/j.ast.2005.08.006
[research_mahulikar_khurana_2008]: https://doi.org/10.1007/bf03256567
[research_mai_li_2026]: https://doi.org/10.1109/taes.2026.3670077
[research_maigler_pessina_2024]: https://doi.org/10.1063/5.0202173
[research_maikapar_1967]: https://doi.org/10.1007/bf01015134
[research_maikapar_1993]: https://doi.org/10.1007/bf01050055
[research_maikapar_1996]: https://doi.org/10.1007/bf02030228
[research_maione_aprovitola_2026]: https://doi.org/10.2514/6.2026-5093
[research_maisaia_2023]: https://doi.org/10.2514/6.2023-3234
[research_maity_padhi_2012]: https://doi.org/10.2514/6.2012-4474
[research_majumder_kumar_2023]: https://doi.org/10.2514/6.2023-2158
[research_malinowski_2020]: https://doi.org/10.37105/sd.87
[research_mall_levin_2024]: https://doi.org/10.1109/aero58975.2024.10521265
[research_mall_taheri_2020]: https://doi.org/10.23919/acc45564.2020.9147275
[research_mani_haney_1994]: https://doi.org/10.2514/6.1994-156
[research_manickavasagam_sarkar_2015]: https://doi.org/10.14429/dsj.65.8238
[research_manned_mars_1994]: https://doi.org/10.2514/5.9781600866326.0025.0034
[research_manor_lau_2002]: https://doi.org/10.2514/6.2002-5160
[research_mao_yang_2024]: https://doi.org/10.23919/ccc63176.2024.10662627
[research_mao_zhang_2016]: https://doi.org/10.1007/s00500-016-2201-3
[research_maomao_jun_2021]: https://doi.org/10.1007/978-981-15-8155-7_14
[research_maoruizhang_yongsun_2010]: https://doi.org/10.1109/wcica.2010.5554588
[research_maoruizhang_yongsun_2010_b]: https://doi.org/10.1109/isscaa.2010.5633024
[research_maples_1979]: https://doi.org/10.21236/ada069807
[research_marchetti_minisci_2021]: https://doi.org/10.3390/math9161868
[research_marchetti_redondogutierrez_2024]: https://doi.org/10.52202/078373-0041
[research_marcum_2001]: https://doi.org/10.21236/ada387492
[research_marinescu_ilin_1997]: https://doi.org/10.2514/6.1997-3664
[research_marini_2001]: https://doi.org/10.1016/s1270-9638(01)01109-9
[research_markusic_sabripour_2018]: https://doi.org/10.1007/978-3-319-32817-1_5
[research_marley_driscoll_2017]: https://doi.org/10.2514/6.2017-0118
[research_marley_driscoll_2018]: https://doi.org/10.2514/6.2018-0280
[research_marley_driscoll_2022]: https://doi.org/10.2514/1.c036411
[research_marraffa_smith_1998]: https://doi.org/10.1023/a:1001874903881
[research_marrison_stengel_1998]: https://doi.org/10.2514/2.4197
[research_marschall_2011]: https://doi.org/10.21236/ada553782
[research_marschall_fletcher_2010]: https://doi.org/10.1016/j.jeurceramsoc.2010.01.010
[research_marshall_2013]: https://doi.org/10.1126/science.339.6127.1508
[research_martin_boyd_2015]: https://doi.org/10.2514/1.t4202
[research_marwaha_singh_2009]: https://doi.org/10.2514/6.2009-5668
[research_masaki_yakura_1968]: https://doi.org/10.2514/6.1968-1155
[research_masarathjabeen_2024]: https://doi.org/10.52783/cana.v32.1742
[research_matheny_smith_2026]: https://doi.org/10.2514/6.2026-112162
[research_matienzo_shah_1985]: https://doi.org/10.1177/109719638500900104
[research_matsuda_kihara_2013]: https://doi.org/10.1016/j.proeng.2013.12.025
[research_matsumoto_kondoh_2013]: https://doi.org/10.2514/6.2013-4646
[research_matsumoto_kondoh_2015]: https://doi.org/10.2514/6.2015-1772
[research_matsunaga_takahashi_2017]: https://doi.org/10.2514/6.2017-0263
[research_matsuno_tsuchiya_2014]: https://doi.org/10.2322/tjsass.57.143
[research_matsuyama_ohnishi_2003]: https://doi.org/10.2514/6.2003-3768
[research_matthews_1993]: https://doi.org/10.1007/978-94-011-1828-6_41
[research_matthews_jones_2003]: https://doi.org/10.2514/6.2003-7045
[research_matthews_jones_2005]: https://doi.org/10.2514/6.2005-3379
[research_matthews_jones_2006]: https://doi.org/10.2514/1.17874
[research_maughmer_ozoroski_1993]: https://doi.org/10.2514/3.21078
[research_mauriello_wilken_2024]: https://doi.org/10.52202/078373-0031
[research_mavris_graham_2000]: https://doi.org/10.4271/2000-01-5561
[research_maxwell_2016]: https://doi.org/10.2514/6.2016-4706
[research_maxwell_2017]: https://doi.org/10.2514/6.2017-4880
[research_maxwell_2017_b]: https://doi.org/10.2514/6.2017-4879
[research_maxwell_hoang_2016]: https://doi.org/10.2514/6.2016-4149
[research_maxwell_phoenix_2017]: https://doi.org/10.2514/6.2017-5357
[research_mayanna_grimm_2006]: https://doi.org/10.2514/6.2006-6037
[research_maynard_patel_2025]: https://doi.org/10.2514/1.a36296
[research_mayrhofer_sachs_1999]: https://doi.org/10.2514/6.1999-4886
[research_mazaheri_2013]: https://doi.org/10.2514/1.a32407
[research_mazzaracchio_marchetti_2010]: https://doi.org/10.1016/j.actaastro.2009.08.033
[research_mbagwu_dalle_2023]: https://doi.org/10.2514/1.c037186
[research_mbagwu_driscoll_2018]: https://doi.org/10.2514/6.2018-0417
[research_mcanally_engel_1979]: https://doi.org/10.2514/6.1979-508
[research_mcclary_putnam_2021]: https://doi.org/10.2514/6.2021-1063
[research_mccormick_wakayama_2010]: https://doi.org/10.2514/6.2010-8906
[research_mccown_barrett_1966]: https://doi.org/10.2514/3.28514
[research_mccown_davi_1967]: https://doi.org/10.2514/3.28943
[research_mccurry_1996]: https://doi.org/10.1016/s0094-5765(96)00142-7
[research_mcdonald_mavris_2000]: https://doi.org/10.2514/6.2000-5559
[research_mceowen_acikmese_2022]: https://doi.org/10.2514/6.2022-0950
[research_mceowen_calderone_2025]: https://doi.org/10.2514/1.g008692
[research_mceowen_calderone_2025_b]: https://doi.org/10.2514/6.2025-1317
[research_mceowen_kamath_2023]: https://doi.org/10.2514/6.2023-0300
[research_mcfarland_2001]: https://doi.org/10.1109/62.894172
[research_mcgrory_2001]: https://doi.org/10.21236/ada399497
[research_mcintosh_1973]: https://doi.org/10.2514/3.50432
[research_mcnamara_2012]: https://doi.org/10.2514/6.2012-4994
[research_mcquaid_brehm_2024]: https://doi.org/10.2514/6.2024-2185
[research_mcquellin_buttsworth_2024]: https://doi.org/10.2514/6.2024-2889
[research_mease_kremer_1994]: https://doi.org/10.2514/3.21355
[research_mease_teufel_1999]: https://doi.org/10.2514/6.1999-4160
[research_meckler_1964]: https://doi.org/10.21236/ad0608830
[research_meckler_1965]: https://doi.org/10.21236/ad0620959
[research_medri_sciti_2013]: https://doi.org/10.4018/978-1-4666-4066-5.ch008
[research_medyanik_vlahopoulos_2016]: https://doi.org/10.1115/imece2016-65389
[research_mehra_1971]: https://doi.org/10.1109/tac.1971.1099744
[research_mehta_2023]: https://doi.org/10.61653/joast.v58i3.2006.643
[research_mei_shi_2020]: https://doi.org/10.1088/1757-899x/892/1/012028
[research_melville_helmich_2021]: https://doi.org/10.2172/1892153
[research_melville_helmich_2021_b]: https://doi.org/10.2172/1890378
[research_menees_brown_1985]: https://doi.org/10.2514/6.1985-1060
[research_menees_brown_1987]: https://doi.org/10.2514/3.25899
[research_menezes_sun_2005]: https://doi.org/10.1007/978-3-540-27009-6_14
[research_meng_bai_2025]: https://doi.org/10.1016/j.ast.2025.110654
[research_meng_bai_2025_b]: https://doi.org/10.1061/jaeeez.aseng-5603
[research_meng_jiang_2016]: https://doi.org/10.1109/chicc.2016.7554371
[research_meng_jiang_2019]: https://doi.org/10.1016/j.ast.2019.105515
[research_meng_liu_2023]: https://doi.org/10.1016/j.ast.2023.108475
[research_meng_tian_2020]: https://doi.org/10.1109/access.2020.3043338
[research_meng_tian_2021]: https://doi.org/10.1109/icras52289.2021.9476537
[research_menk_candler_2025]: https://doi.org/10.2514/6.2025-3082
[research_menssen_2026]: https://doi.org/10.2514/6.2026-111626
[research_mercatelli_sani_2011]: https://doi.org/10.1109/cleoe.2011.5942843
[research_merkin_nazar_2011]: https://doi.org/10.1007/s10665-011-9487-z
[research_merkulov_shalumov_2025]: https://doi.org/10.2514/1.g009009
[research_merrill_1989]: https://doi.org/10.1007/978-94-009-0995-3_8
[research_merrill_bleck_1986]: https://doi.org/10.1016/0004-6981(86)90366-5
[research_merritt_cusumano_1996]: https://doi.org/10.1117/12.241917
[research_merritt_kramer_1997]: https://doi.org/10.1117/12.277173
[research_mesallesripoll_campbell_2021]: https://doi.org/10.2514/6.2021-0934
[research_meyer_nelson_1999]: https://doi.org/10.2514/6.1999-4880
[research_mhapsekar_maurya_2025]: https://doi.org/10.1109/indiscon66021.2025.11252266
[research_mi_hu_2022]: https://doi.org/10.1007/978-981-19-6203-5_44
[research_miao_wang_2026]: https://doi.org/10.1016/j.ast.2026.113155
[research_micol_1991]: https://doi.org/10.2514/6.1991-1436
[research_micol_1995]: https://doi.org/10.2514/3.26678
[research_micol_1995_b]: https://doi.org/10.2514/6.1995-2107
[research_miele_damoulakis_1969]: https://doi.org/10.2514/3.5131
[research_miele_hull_1963]: https://doi.org/10.21236/ad0404858
[research_miele_pritchard_1963]: https://doi.org/10.21236/ad0403460
[research_mifsud_estruchsamper_2012]: https://doi.org/10.1017/s0001924000007338
[research_mihalea_florea_2024]: https://doi.org/10.3390/app14177776
[research_miller_1985]: https://doi.org/10.2514/3.8989
[research_miller_1990]: https://doi.org/10.2514/6.1990-1376
[research_miller_1993]: https://doi.org/10.1007/978-94-011-1828-6_40
[research_miller_2004]: https://doi.org/10.1080/14777620490444722
[research_miller_2005]: https://doi.org/10.2514/6.2005-5911
[research_miller_argrow_1997]: https://doi.org/10.2514/6.1997-189
[research_milleriii_1992]: https://doi.org/10.2514/6.1992-3937
[research_milleroana_corral_2015]: https://doi.org/10.1111/jace.14001
[research_minami_tsukamoto_2006]: https://doi.org/10.2514/6.2006-8120
[research_ming_ming_2017]: https://doi.org/10.2514/6.2017-2408
[research_ming_ming_2017_b]: https://doi.org/10.2514/6.2017-2321
[research_mingguang_qiong_2006]: https://doi.org/10.2514/6.iac-06-c1.4.07
[research_minglin_2022]: https://doi.org/10.1109/ccdc55256.2022.10033793
[research_minwen_dayi_2014]: https://doi.org/10.1016/j.ast.2014.05.004
[research_mirels_ellinwood_1970]: https://doi.org/10.2514/3.6002
[research_mirels_mullen_1965]: https://doi.org/10.2514/3.3321
[research_mirels_mullen_1966]: https://doi.org/10.2514/3.55254
[research_mirmirani_wu_2005]: https://doi.org/10.2514/6.2005-6256
[research_mishra_sushnigdha_2025]: https://doi.org/10.1109/spert67079.2025.11469624
[research_misko_1999]: https://doi.org/10.1007/bf02698757
[research_mitanchey_pagani_2024]: https://doi.org/10.23919/eucap60739.2024.10501224
[research_mitchel_1967]: https://doi.org/10.2514/6.1967-154
[research_mitroshin_glinsky_1983]: https://doi.org/10.1016/b978-0-08-029328-8.50019-0
[research_miyazawa_ishikawa_1993]: https://doi.org/10.2514/6.1993-3818
[research_mizener_lu_2017]: https://doi.org/10.2514/6.2017-4740
[research_mizener_lu_2019]: https://doi.org/10.2514/1.b37033
[research_mo_liu_2022]: https://doi.org/10.1109/cac57257.2022.10055944
[research_mo_lu_2023]: https://doi.org/10.1007/978-981-99-0479-2_167
[research_mo_su_2022]: https://doi.org/10.1016/j.ast.2022.107372
[research_mocio_2001]: https://doi.org/10.2514/6.2001-4582
[research_modeling_of_heat_2016]: https://doi.org/10.18698/0236-3941-2016-6-22-32
[research_mohamed_salleh_2017]: https://doi.org/10.1063/1.4972149
[research_mohring_gabler_2021]: https://doi.org/10.1109/map.2020.3003226
[research_molchanov_2024]: https://doi.org/10.1201/9781003476559-8
[research_molina_simeonides_1996]: https://doi.org/10.2514/6.1996-2468
[research_molvik_bowles_1993]: https://doi.org/10.2514/6.1993-5097
[research_molvik_bowles_1993_b]: https://doi.org/10.2514/6.1993-509
[research_mondal_padhi_2018]: https://doi.org/10.2514/1.g002893
[research_mondal_padhi_2020]: https://doi.org/10.2514/1.g002893.c1
[research_mongibello_deluca_2008]: https://doi.org/10.2514/1.33824
[research_monnoyer_1993]: https://doi.org/10.2514/6.1993-3116
[research_monroe_boyd_2025]: https://doi.org/10.2514/6.2025-0556
[research_monroe_boyd_2026]: https://doi.org/10.2514/6.2026-2645
[research_monte_carlo_1989]: https://doi.org/10.2514/5.9781600865923.0582.0596
[research_monteirodossantosrodriguesdasilva_delimacostasalazar_2022]: https://doi.org/10.26678/abcm.encit2022.cit22-0340
[research_monteverde_alfano_2013]: https://doi.org/10.1016/j.corsci.2013.06.029
[research_monteverde_bellosi_2008]: https://doi.org/10.1016/j.msea.2007.08.054
[research_moody_groener_1982]: https://doi.org/10.2514/6.1982-579
[research_mooij_2004]: https://doi.org/10.2514/6.2004-4775
[research_mooij_2004_b]: https://doi.org/10.2514/6.2004-5186
[research_mooij_barkana_2005]: https://doi.org/10.2514/6.2005-6290
[research_mooij_hanninen_2009]: https://doi.org/10.2514/6.2009-5770
[research_mooij_huot_2006]: https://doi.org/10.2514/6.2006-6023
[research_moorhouse_suchomel_2001]: https://doi.org/10.2514/6.2001-3063
[research_moosavi_mirzaei_2009]: https://doi.org/10.2514/6.2009-7247
[research_mor_livne_2006]: https://doi.org/10.2514/6.2006-1718
[research_mor_livne_2007]: https://doi.org/10.2514/6.2007-1859
[research_mor_taraborelli_2025]: https://doi.org/10.1016/j.oceram.2025.100766
[research_moran_capra_2021]: https://doi.org/10.1016/j.ast.2021.106862
[research_moran_mcquellin_2023]: https://doi.org/10.2514/6.2023-1385
[research_morani_fruncillo_2026]: https://doi.org/10.2514/6.2026-5046
[research_moravszki_rohacs_2018]: https://doi.org/10.3311/pptr.10342
[research_moreira_wolf_2021]: https://doi.org/10.1007/s40430-021-03336-3
[research_moreira_wolf_2022]: https://doi.org/10.2514/6.2022-3278
[research_moreira_wolf_2022_b]: https://doi.org/10.2514/6.2022-0344
[research_morelli_2008]: https://doi.org/10.2514/6.2008-1682
[research_morelli_2009]: https://doi.org/10.2514/1.37092
[research_morgan_1961]: https://doi.org/10.21236/ad0600907
[research_morgan_1971]: https://doi.org/10.2514/6.1971-969
[research_morgan_2016]: https://doi.org/10.1109/acc.2016.7526612
[research_mori_tsuchiya_2002]: https://doi.org/10.2514/6.2002-5221
[research_morimoto_chuang_1998]: https://doi.org/10.2514/6.1998-4122
[research_morimoto_kinefuchi_2025]: https://doi.org/10.1063/5.0242370
[research_morio_cazaurang_2009]: https://doi.org/10.1016/j.conengprac.2008.10.018
[research_morita_tsuchiya_2020]: https://doi.org/10.2514/6.2020-2402
[research_morreale_wagnild_2021]: https://doi.org/10.2172/1894999
[research_morrell_munk_2014]: https://doi.org/10.4028/www.scientific.net/amm.553.847
[research_morris_povolny_2022]: https://doi.org/10.2514/6.2022-1860
[research_morris_povolny_2023]: https://doi.org/10.1016/j.oceram.2023.100382
[research_morrison_yanta_1981]: https://doi.org/10.2514/6.1981-1060
[research_morth_1972]: https://doi.org/10.2514/6.1972-833
[research_morth_speyer_1961]: https://doi.org/10.2514/8.5507
[research_moshman_proulx_2014]: https://doi.org/10.2514/1.a32764
[research_mostafa_nooraliei_2009]: https://doi.org/10.1115/1.802977.paper97
[research_mosunov_mosunova_2010]: https://doi.org/10.5930/issn.1994-4683.2010.10.68.p73-76
[research_moszee_moszee_1997]: https://doi.org/10.2514/6.1997-3395
[research_motoyama_mihara_2001]: https://doi.org/10.2514/6.2001-1828
[research_moura_borgesribeiro_2025]: https://doi.org/10.26678/abcm.cobem2025.cob2025-1507
[research_moura_borgesribeiro_2025_b]: https://doi.org/10.26678/abcm.cobem2025.cob2025-0300
[research_moura_borgesribeiro_2025_c]: https://doi.org/10.26678/abcm.cobem2025.cob2025-0360
[research_moura_borgesribeiro_2025_d]: https://doi.org/10.26678/abcm.cobem2025.cob2025-1480
[research_moura_borgesribeiro_2025_e]: https://doi.org/10.26678/abcm.cobem2025.cob2025-1499
[research_moura_borgesribeiro_2026]: https://doi.org/10.26678/abcm.evr2026.evr26-0014
[research_moura_ribeiro_2024]: https://doi.org/10.26678/abcm.encit2024.cit24-0501
[research_mowry_grasso_2020]: https://doi.org/10.1007/978-3-030-20707-6_92-1
[research_moylan_landrum_2013]: https://doi.org/10.1016/j.proeng.2013.05.026
[research_mu_wang_2025]: https://doi.org/10.1109/itoec63606.2025.10968931
[research_mudrik_oshman_2023]: https://doi.org/10.1109/med59994.2023.10185736
[research_mukhopadhyay_raju_2013]: https://doi.org/10.4018/978-1-4666-4066-5.ch003
[research_muller_petervari_2025]: https://doi.org/10.1109/maes.2025.3637666
[research_multi_objective_reentry_2017]: https://doi.org/10.21629/jsee.2017.04.13
[research_mungiguerra_silvestroni_2024]: https://doi.org/10.52202/078369-0117
[research_munipalli_subbarao_2005]: https://doi.org/10.21236/ada435356
[research_murayama_sasoh_1992]: https://doi.org/10.1007/978-3-642-77648-9_108
[research_murbach_1993]: https://doi.org/10.2514/6.1993-313
[research_murillo_lu_2010]: https://doi.org/10.2514/6.2010-8173
[research_murphy_buning_2004]: https://doi.org/10.2514/6.2004-2595
[research_murray_steelant_2009]: https://doi.org/10.2514/6.2009-7399
[research_murray_tartabini_2001]: https://doi.org/10.2514/6.2001-839
[research_musa_huang_2022]: https://doi.org/10.1016/j.actaastro.2022.09.001
[research_musa_huang_2024]: https://doi.org/10.1063/5.0239660
[research_musa_huang_2024_b]: https://doi.org/10.1063/5.0205193
[research_musa_huang_2025]: https://doi.org/10.2514/6.2025-0753
[research_musal_1962]: https://doi.org/10.21236/ad0294472
[research_nagai_kimura_2013]: https://doi.org/10.1163/22134808-00002415
[research_nagai_swamura_2011]: https://doi.org/10.2514/6.2011-850
[research_nagamatsu_li_1960]: https://doi.org/10.1063/1.1705993
[research_nagamatsu_sheer_1960]: https://doi.org/10.2514/8.5118
[research_nagamatsu_sheer_1961]: https://doi.org/10.21236/ad0600345
[research_nagashetty_medhi_2017]: https://doi.org/10.1007/978-3-319-44866-4_112
[research_nagdewe_shevare_2006]: https://doi.org/10.2514/6.2006-8088
[research_nagpal_g_2023]: https://doi.org/10.2514/6.2023-3083
[research_nair_kumar_2003]: https://doi.org/10.2514/6.2003-7067
[research_naitoh_nakamura_2011]: https://doi.org/10.2514/6.2011-2316
[research_najafiyazdi_2005]: https://doi.org/10.2514/6.2005-4827
[research_najam_2014]: https://doi.org/10.1089/space.2013.0027
[research_najib_bachok_2014]: https://doi.org/10.1063/1.4882515
[research_najson_mease_2006]: https://doi.org/10.2514/1.17715
[research_nakatani_taguchi_2009]: https://doi.org/10.2514/6.2009-7434
[research_nakatani_taguchi_2011]: https://doi.org/10.2514/6.2011-2339
[research_nakayama_edanaga_2018]: https://doi.org/10.2514/6.2018-4452
[research_nakayama_harada_2018]: https://doi.org/10.1038/s41598-017-19005-2
[research_nam_lee_2025]: https://doi.org/10.1109/taes.2025.3575052
[research_narain_1991]: https://doi.org/10.2514/6.1991-1813
[research_nardo_1972]: https://doi.org/10.2514/3.50367
[research_nardo_erickson_1961]: https://doi.org/10.21236/ad0264410
[research_nardo_sadler_1962]: https://doi.org/10.21236/ad0273837
[research_nareshkumar_ikram_2017]: https://doi.org/10.1007/s11081-017-9367-0
[research_nassif_hoste_2026]: https://doi.org/10.1016/j.ast.2026.111978
[research_natali_rallini_2013]: https://doi.org/10.1002/mame.201300267
[research_nathan_bindu_2005]: https://doi.org/10.2514/6.2005-5063
[research_nawaz_alsaedi_2012]: https://doi.org/10.1017/jmech.2012.142
[research_needels_alonso_2023]: https://doi.org/10.2514/6.2023-3718
[research_needham_1965]: https://doi.org/10.2514/3.2986
[research_neely_woodward_2015]: https://doi.org/10.2514/6.2015-3642
[research_neff_1972]: https://doi.org/10.2514/6.1972-974
[research_nelson_1996]: https://doi.org/10.2514/6.1996-904
[research_nelson_2000]: https://doi.org/10.2514/6.2000-388
[research_nenarokomov_alifanov_2016]: https://doi.org/10.1016/j.ijheatmasstransfer.2016.02.045
[research_neubacher_henckels_2002]: https://doi.org/10.1007/978-3-540-45466-3_16
[research_neumann_1989]: https://doi.org/10.1007/978-1-4684-9187-6_4
[research_neuwerth_peiter_1999]: https://doi.org/10.2514/2.3441
[research_nevrekar_striz_2012]: https://doi.org/10.2514/6.2012-5633
[research_newberry_1995]: https://doi.org/10.2514/6.1995-6155
[research_newberry_1998]: https://doi.org/10.1016/s1369-8869(98)00015-9
[research_newell_zakharov_2007]: https://doi.org/10.21236/ada479049
[research_newman_fulcher_1992]: https://doi.org/10.2514/6.1992-2722
[research_ng_friedmann_2011]: https://doi.org/10.1017/s0001924000005467
[research_ngo_koshiba_1993]: https://doi.org/10.2514/6.1993-1397
[research_ngo_powell_2017]: https://doi.org/10.2514/6.2017-1405
[research_nguyen_aleti_2025]: https://doi.org/10.52202/083084-0038
[research_nguyen_urquhart_2026]: https://doi.org/10.1108/jdal-06-2025-0015
[research_ni_qiu_2025]: https://doi.org/10.1007/978-981-96-2204-7_10
[research_nie_liu_2013]: https://doi.org/10.4028/www.scientific.net/amm.291-294.1636
[research_nie_zhang_2023]: https://doi.org/10.1007/978-981-19-6613-2_250
[research_niederstrasser_2022]: https://doi.org/10.1016/j.jsse.2022.07.003
[research_nikolaevichblinov_vladimirovichshalay_2016]: https://doi.org/10.17485/ijst/2016/v9i27/97681
[research_ning_zhang_2007]: https://doi.org/10.1016/s1000-9361(07)60001-6
[research_nisar_ariharan_2017]: https://doi.org/10.1016/j.ceramint.2017.07.053
[research_nisar_hassan_2022]: https://doi.org/10.1016/j.ceramint.2021.12.199
[research_nisar_zhang_2020]: https://doi.org/10.1016/j.ceramint.2020.07.066
[research_nisar_zhang_2023]: https://doi.org/10.1016/j.ceramint.2022.09.050
[research_nishio_hagiwara_1998]: https://doi.org/10.2514/6.1998-1620
[research_nishio_nakamura_2001]: https://doi.org/10.2514/6.2001-1810
[research_nithinchandran_devapal_2019]: https://doi.org/10.1016/j.ceramint.2019.05.253
[research_niu_chen_2018]: https://doi.org/10.1007/s11071-018-4127-z
[research_niu_su_2019]: https://doi.org/10.1109/access.2018.2886243
[research_niu_yuan_2017]: https://doi.org/10.1016/j.ast.2017.10.026
[research_niu_yuan_2019]: https://doi.org/10.1016/j.cja.2019.01.003
[research_noftz_shuck_2023]: https://doi.org/10.2514/6.2023-2352
[research_nomura_1983]: https://doi.org/10.2514/3.8296
[research_nomura_yamamoto_1996]: https://doi.org/10.2322/jjsass1969.44.265
[research_nonequilibrium_stagnation_1975]: https://doi.org/10.2514/5.9781600865138.0415.0435
[research_norris_2006]: https://doi.org/10.2514/6.2006-2815
[research_norsell_2005]: https://doi.org/10.2514/1.8544
[research_novotny_neiferd_2024]: https://doi.org/10.2514/6.2024-1800
[research_novotny_rumpfkeil_2024]: https://doi.org/10.2514/1.c037547
[research_nowak_bruzda_2021]: https://doi.org/10.1016/j.matlet.2021.129447
[research_nozhnitsky_smirnov_1995]: https://doi.org/10.1533/9780857093219.184
[research_numerical_analysis_1994]: https://doi.org/10.2514/5.9781600866326.0012.0024
[research_numerical_research_2008]: https://doi.org/10.2514/6.2008-4708
[research_numerical_simulation_1986]: https://doi.org/10.2514/5.9781600865770.0571.0595
[research_nusca_1993]: https://doi.org/10.1108/eb023918
[research_nykiel_wyatt_2026]: https://doi.org/10.1007/s43939-026-00787-0
[research_oberkampf_aeschliman_1992]: https://doi.org/10.2514/3.11172
[research_obrien_lewis_2000]: https://doi.org/10.2514/6.2000-3823
[research_obrien_lewis_2001]: https://doi.org/10.2514/6.2001-1919
[research_obrien_lewis_2002]: https://doi.org/10.2514/2.3028
[research_ochi_2004]: https://doi.org/10.1111/j.1934-6093.2004.tb00211.x
[research_oconnor_2019]: https://doi.org/10.1109/radar41533.2019.171388
[research_odabas_sarigulklijn_1992]: https://doi.org/10.2514/6.1992-5018
[research_odioniyinomen_2022]: https://doi.org/10.5772/intechopen.100129
[research_odriscoll_bruce_2021]: https://doi.org/10.2514/6.2021-1031
[research_ohare_andersonjr_1993]: https://doi.org/10.2514/6.1993-3202
[research_ohashi_takahashi_2018]: https://doi.org/10.1299/jfst.2018jfst0020
[research_ohkage_okuyama_2025]: https://doi.org/10.3390/aerospace12040281
[research_ohlmeyer_menon_2010]: https://doi.org/10.2514/6.2010-8319
[research_ohtake_1998]: https://doi.org/10.1016/s0045-7825(97)00153-9
[research_okamoto_yamamoto_2002]: https://doi.org/10.2514/6.2002-5193
[research_okuno_watanabe_1992]: https://doi.org/10.2514/6.1992-4302
[research_oliveirajunior_marinho_2021]: https://doi.org/10.26678/abcm.cobem2021.cob2021-0818
[research_olivier_1995]: https://doi.org/10.1007/bf01419002
[research_olsen_1965]: https://doi.org/10.21236/ad0626928
[research_olstad_1969]: https://doi.org/10.2514/3.5062
[research_olszewski_1990]: https://doi.org/10.2514/6.1990-3356
[research_olynick_1998]: https://doi.org/10.2514/2.3338
[research_oneal_desilva_2026]: https://doi.org/10.2514/6.2026-4592
[research_oneill_lewis_1992]: https://doi.org/10.2514/3.56866
[research_oneill_lewis_1993]: https://doi.org/10.2514/3.46438
[research_onozeki_shimizu_2026]: https://doi.org/10.2514/6.2026-2468
[research_opila_jacobson_2006]: https://doi.org/10.1361/154770206x86590
[research_oppenheimer_doman_2006]: https://doi.org/10.2514/6.2006-6637
[research_oppenheimer_doman_2008]: https://doi.org/10.2514/6.2008-6382
[research_oppenheimer_skujins_2008]: https://doi.org/10.2514/6.2008-6383
[research_optimal_aerodynamic_1996]: https://doi.org/10.2514/5.9781600866401.0017.0049
[research_optimal_glide_1981]: https://doi.org/10.1016/b978-0-444-41961-3.50023-1
[research_optimization_using_2011]: https://doi.org/10.2514/5.9781600868405.0229.0273
[research_orlandini_paciorri_2026]: https://doi.org/10.2514/6.2026-5116
[research_orru_cao_2013]: https://doi.org/10.4018/978-1-4666-4066-5.ch009
[research_orru_cao_2013_b]: https://doi.org/10.3390/ma6051566
[research_orru_cao_2019]: https://doi.org/10.1016/b978-0-12-817744-0.00002-7
[research_ortloff_1968]: https://doi.org/10.21236/ad0830727
[research_oskupach_2018]: https://doi.org/10.21557/mth.52771229
[research_ossin_aronin_1975]: https://doi.org/10.2514/6.1975-819
[research_ostapenko_1983]: https://doi.org/10.1007/bf01090514
[research_osun_james_2026]: https://doi.org/10.2514/6.2026-5040
[research_otsu_2016]: https://doi.org/10.2322/tastj.14.pe_7
[research_otsu_2018]: https://doi.org/10.2322/tastj.16.588
[research_otsu_katsurayama_2011]: https://doi.org/10.2514/6.2011-3466
[research_otsu_suzuki_1999]: https://doi.org/10.2514/6.1999-3463
[research_otsu_yamada_2015]: https://doi.org/10.2514/6.2015-2808
[research_ouyang_wang_2026]: https://doi.org/10.1109/icetac70565.2026.11636040
[research_ouzts_2008]: https://doi.org/10.2514/6.2008-2621
[research_ouzts_soloway_2009]: https://doi.org/10.2514/6.2009-7329
[research_owotunse_ogwumike_2023]: https://doi.org/10.1109/swc57546.2023.10448888
[research_page_rogers_1977]: https://doi.org/10.1109/cdc.1977.271654
[research_pai_chandy_2019]: https://doi.org/10.1063/1.5141217
[research_paiva_1998]: https://doi.org/10.1117/12.304845
[research_palmer_2020]: https://doi.org/10.2514/6.2020-0116
[research_palmer_henline_1995]: https://doi.org/10.2514/6.1995-2080
[research_palmer_henline_1997]: https://doi.org/10.2514/2.3261
[research_palmer_morgan_1997]: https://doi.org/10.2514/6.1997-280
[research_palmer_rao_2022]: https://doi.org/10.2514/6.2022-2390
[research_palumbo_morani_2017]: https://doi.org/10.2514/1.a33465
[research_pan_gao_2014]: https://doi.org/10.1063/1.4902591
[research_pan_ma_2025]: https://doi.org/10.1007/978-981-96-2204-7_23
[research_pan_peng_2020]: https://doi.org/10.1016/j.actaastro.2019.07.039
[research_pan_tian_2009]: https://doi.org/10.2514/6.2009-7370
[research_panagiotopoulos_margaris_2005]: https://doi.org/10.2514/6.2005-3209
[research_panagiotopoulos_margaris_2006]: https://doi.org/10.2514/6.2006-3250
[research_panerai_olivier_2009]: https://doi.org/10.2514/6.2009-7243
[research_panesi_martin_2020]: https://doi.org/10.2514/6.2020-3276
[research_pang_du_2025]: https://doi.org/10.1007/978-981-95-2632-1_6
[research_pang_shi_2021]: https://doi.org/10.1117/12.2606307
[research_papadopoulos_subrahmanyam_2006]: https://doi.org/10.2514/6.2006-1034
[research_park_2005]: https://doi.org/10.2514/6.2005-190
[research_park_2007]: https://doi.org/10.2514/1.15745
[research_park_2011]: https://doi.org/10.2514/6.2011-248
[research_park_ahn_1998]: https://doi.org/10.2514/6.1998-832
[research_park_park_2017]: https://doi.org/10.1016/j.asr.2017.05.004
[research_park_shin_2024]: https://doi.org/10.1007/s42405-024-00789-3
[research_parker_serrani_2006]: https://doi.org/10.2514/6.2006-6556
[research_parker_serrani_2007]: https://doi.org/10.2514/1.27830
[research_parsonsengineeringsciencesincpasadenaca_1991]: https://doi.org/10.21236/ada413142
[research_pasagada_yang_2022]: https://doi.org/10.1016/j.ceramint.2021.12.229
[research_paschal_tournes_2001]: https://doi.org/10.2514/6.2001-4275
[research_passera_1960]: https://doi.org/10.1109/tane3.1960.4201755
[research_paus_well_1996]: https://doi.org/10.2514/6.1996-3901
[research_paydayesh_kokabi_2015]: https://doi.org/10.1007/s13726-015-0331-6
[research_payne_edwards_1997]: https://doi.org/10.1080/03069889708253814
[research_paynter_1988]: https://doi.org/10.1016/b978-0-08-037197-9.50009-7
[research_pegg_hahne_1995]: https://doi.org/10.2514/6.1995-6093
[research_pei_fan_2021]: https://doi.org/10.1109/access.2021.3056517
[research_pei_lin_2018]: https://doi.org/10.1109/gncc42960.2018.9018941
[research_peigin_desideri_2001]: https://doi.org/10.1016/b978-044450673-3/50112-3
[research_peipei_junbo_2017]: https://doi.org/10.2514/6.2017-2227
[research_pelton_madry_2019]: https://doi.org/10.1007/978-3-030-20707-6_82-1
[research_pelton_madry_2020]: https://doi.org/10.1007/978-3-030-36308-6_82
[research_peng_feng_2019]: https://doi.org/10.1109/access.2019.2923014
[research_peng_he_2015]: https://doi.org/10.1016/j.cja.2014.12.018
[research_peng_peng_2014]: https://doi.org/10.1109/cgncc.2014.7007351
[research_peng_qi_2019]: https://doi.org/10.1109/ccdc.2019.8832538
[research_peng_qi_2019_b]: https://doi.org/10.1109/safeprocess45799.2019.9213337
[research_peng_qi_2020]: https://doi.org/10.1016/j.jfranklin.2020.07.014
[research_peng_wang_2012]: https://doi.org/10.4028/www.scientific.net/amm.215-216.978
[research_peng_zhi_2014]: https://doi.org/10.1016/j.ast.2013.11.005
[research_pengpeng_tongchuangming_2013]: https://doi.org/10.1109/csqrwc.2013.6657446
[research_pengxin_feng_2015]: https://doi.org/10.1109/ccdc.2015.7162512
[research_pentygeraets_mcgilvray_2019]: https://doi.org/10.2514/6.2019-0535
[research_pereiralara_toro_2018]: https://doi.org/10.26678/abcm.encit2018.cit18-0462
[research_performance_of_1975]: https://doi.org/10.2514/5.9781600865138.0457.0489
[research_perini_1975]: https://doi.org/10.2514/3.27829
[research_perkins_tannasjr_1967]: https://doi.org/10.2514/6.1967-597
[research_perlini_bertolini_2026]: https://doi.org/10.2514/6.2026-5058
[research_perminov_1969]: https://doi.org/10.1007/bf01015966
[research_perrier_1989]: https://doi.org/10.1007/978-1-4684-9187-6_3
[research_persoons_mcguinn_2011]: https://doi.org/10.1016/j.ijheatmasstransfer.2011.04.037
[research_peterkorzun_2017]: https://doi.org/10.21557/dsp.49928613
[research_petley_dziedzic_1993]: https://doi.org/10.2514/6.1993-1984
[research_pettinari_corradini_2012]: https://doi.org/10.1109/acc.2012.6315223
[research_pezzella_2011]: https://doi.org/10.1016/j.actaastro.2011.03.004
[research_pezzella_2013]: https://doi.org/10.1016/j.ast.2012.01.007
[research_pezzella_2015]: https://doi.org/10.12989/aas.2015.2.2.109
[research_pezzella_marini_2014]: https://doi.org/10.2514/6.2014-2844
[research_pezzella_viviani_2016]: https://doi.org/10.1016/j.ast.2016.02.030
[research_pfaff_1968]: https://doi.org/10.21236/ad0832104
[research_pham_nguyen_2020]: https://doi.org/10.15625/2525-2518/57/6a/14012
[research_pham_nguyen_2025]: https://doi.org/10.15625/2525-2518/18306
[research_phillips_cruz_1991]: https://doi.org/10.2514/6.1991-1694
[research_phoenix_maxwell_2017]: https://doi.org/10.1115/smasis2017-3766
[research_phoenix_maxwell_2018]: https://doi.org/10.2514/6.2018-1285
[research_phoenix_maxwell_2019]: https://doi.org/10.2514/1.c035317
[research_piao_yang_2018]: https://doi.org/10.1016/j.ast.2018.06.029
[research_piccirillo_viola_2023]: https://doi.org/10.2514/6.2023-3098
[research_pichon_barreteau_2012]: https://doi.org/10.2514/6.2012-5846
[research_pichon_soyris_2006]: https://doi.org/10.2514/6.2006-7950
[research_pietlahanier_serre_2017]: https://doi.org/10.2514/6.2017-2197
[research_pike_2006]: https://doi.org/10.1017/s0001924000001287
[research_pike_2013]: https://doi.org/10.1017/s0001924000008186
[research_ping_yanli_2017]: https://doi.org/10.1109/ccdc.2017.7979315
[research_pingli_wanchunchen_2010]: https://doi.org/10.1109/icmet.2010.5598391
[research_pinto_whyman_2023]: https://doi.org/10.1049/rsn2.12432
[research_pinto_whyman_2023_b]: https://doi.org/10.1049/icp.2023.1256
[research_pionessa_kinzel_2024]: https://doi.org/10.2514/6.2024-1971
[research_pionessa_kinzel_2024_b]: https://doi.org/10.2514/6.2024-1971.c1
[research_pisano_whitfield_2024]: https://doi.org/10.2514/6.2024-2330
[research_pittman_dillon_1977]: https://doi.org/10.2514/3.44633
[research_platus_1983]: https://doi.org/10.2514/6.1983-2111
[research_platus_1985]: https://doi.org/10.2514/3.19974
[research_pokiya_sharma_2022]: https://doi.org/10.1016/j.jfranklin.2022.09.064
[research_polisano_grassi_2024]: https://doi.org/10.1109/igarss53475.2024.10640451
[research_pollack_2009]: https://doi.org/10.2968/065001003
[research_pollack_2015]: https://doi.org/10.1080/10736700.2015.1119422
[research_pollock_moran_2023]: https://doi.org/10.2514/6.2023-3033
[research_pollock_wild_2024]: https://doi.org/10.2514/6.2024-4139
[research_polsgrove_thomas_2017]: https://doi.org/10.1109/aero.2017.7943887
[research_polyanskii_1967]: https://doi.org/10.1007/bf01013723
[research_pope_1968]: https://doi.org/10.2514/6.1968-15
[research_poplavskaya_2002]: https://doi.org/10.1023/a:1015203206949
[research_portis_dambrosio_2024]: https://doi.org/10.52202/078369-0104
[research_poteet_1998]: https://doi.org/10.2514/6.1998-1611
[research_potsawat_palar_2019]: https://doi.org/10.1299/jsmedsd.2019.29.1206
[research_pottsepp_shi_1968]: https://doi.org/10.2514/3.4699
[research_poudel_shoele_2026]: https://doi.org/10.2514/6.2026-4661
[research_poulain_pietlahanie_2009]: https://doi.org/10.2514/6.2009-7290
[research_povolny_seidel_2022]: https://doi.org/10.1016/j.ceramint.2022.01.006
[research_powell_cruz_1991]: https://doi.org/10.2514/6.1991-55
[research_pozefsky_1989]: https://doi.org/10.2514/6.1989-1103
[research_prakash_singh_2021]: https://doi.org/10.2514/6.2021-3271
[research_prakash_zhong_2008]: https://doi.org/10.2514/6.2008-744
[research_prakash_zhong_2009]: https://doi.org/10.2514/6.2009-1542
[research_prasanna_ghose_2005]: https://doi.org/10.1007/11424925_58
[research_prasanna_ghose_2005_b]: https://doi.org/10.2514/6.2005-6063
[research_preliminary_design_1983]: https://doi.org/10.2514/5.9781600865626.0385.0415
[research_preller_smart_2012]: https://doi.org/10.2514/6.2012-5825
[research_pressman_galperin_1986]: https://doi.org/10.1016/s0166-1116(08)70889-6
[research_pritchard_1969]: https://doi.org/10.1007/bf00932462
[research_priyamvada_singh_2015]: https://doi.org/10.2514/6.2015-3678
[research_probstein_1961]: https://doi.org/10.2514/8.5423
[research_pu_fan_2013]: https://doi.org/10.3182/20130902-3-cn-3020.00158
[research_pu_tan_2012]: https://doi.org/10.1109/wcica.2012.6358043
[research_pu_tan_2013]: https://doi.org/10.1109/icma.2013.6617946
[research_pu_tan_2014]: https://doi.org/10.1016/j.actaastro.2014.01.025
[research_pu_zhang_2016]: https://doi.org/10.1109/icma.2016.7558787
[research_pudsey_boyce_2012]: https://doi.org/10.2514/6.2012-5934
[research_pulimidi_peace_2018]: https://doi.org/10.2514/6.2018-5254
[research_pulok_chakravarty_2020]: https://doi.org/10.1115/imece2020-23663
[research_purcell_1980]: https://doi.org/10.1049/ep.1980.0006
[research_purpura_f_2012]: https://doi.org/10.2514/6.2012-5968
[research_purwar_2019]: https://doi.org/10.1007/978-3-319-91017-8_128
[research_purwar_basu_2017]: https://doi.org/10.1111/jace.14750
[research_putnam_bairstow_2008]: https://doi.org/10.2514/1.27616
[research_putnam_barton_2009]: https://doi.org/10.2514/6.2009-5773
[research_putnam_braun_2006]: https://doi.org/10.2514/6.2006-7438
[research_putnam_braun_2016]: https://doi.org/10.2514/6.2016-0278
[research_qi_jianliang_2017]: https://doi.org/10.2514/6.2017-1248
[research_qi_wang_2023]: https://doi.org/10.1007/978-981-99-6187-0_81
[research_qi_zhang_2021]: https://doi.org/10.1007/978-981-15-8155-7_38
[research_qian_qi_2014]: https://doi.org/10.1109/cgncc.2014.7007434
[research_qian_xinguo_2011]: https://doi.org/10.1016/j.proeng.2011.08.054
[research_qiang_jun_2019]: https://doi.org/10.1109/icmae.2019.8880990
[research_qiang_sobieczky_2000]: https://doi.org/10.1016/b978-008043693-7/50113-6
[research_qiang_yongtao_2017]: https://doi.org/10.1088/1757-899x/234/1/012012
[research_qiao_chen_2011]: https://doi.org/10.4028/www.scientific.net/amr.383-390.4451
[research_qiao_liu_2024]: https://doi.org/10.1016/j.energy.2024.130906
[research_qiao_meng_2019]: https://doi.org/10.1016/j.ast.2018.10.018
[research_qiaoyongjie_liujinrong_2011]: https://doi.org/10.1109/cie-radar.2011.6159904
[research_qilun_xiwang_2015]: https://doi.org/10.1109/chicc.2015.7260445
[research_qin_bao_2008]: https://doi.org/10.2514/6.2008-5178
[research_qinchangmao_qinaiming_2010]: https://doi.org/10.1109/cmce.2010.5610285
[research_qinggao_jianhuali_2014]: https://doi.org/10.17265/1934-8975/2014.12.009
[research_qiu_jia_2016]: https://doi.org/10.1177/0954410016649208
[research_qiu_zhang_2017]: https://doi.org/10.2514/6.2017-2381
[research_qu_he_2015]: https://doi.org/10.1016/j.ceramint.2014.12.079
[research_qu_li_2016]: https://doi.org/10.1109/cec.2016.7744191
[research_qu_liu_2019]: https://doi.org/10.1016/j.ceramint.2019.06.076
[research_qu_pingyuan_2015]: https://doi.org/10.1109/chicc.2015.7261023
[research_qu_sun_2017]: https://doi.org/10.2514/6.2017-2445
[research_qu_sun_2018]: https://doi.org/10.1016/j.actaastro.2018.03.046
[research_qu_wang_2023]: https://doi.org/10.3390/aerospace10030205
[research_qu_wang_2024]: https://doi.org/10.1063/5.0234961
[research_qu_zhang_2023]: https://doi.org/10.1109/icma57826.2023.10215607
[research_quan_ma_2026]: https://doi.org/10.2514/1.t7148
[research_quinlan_movva_2021]: https://doi.org/10.2514/6.2021-4245
[research_r_s_2022]: https://doi.org/10.4018/978-1-6684-4230-2.ch013
[research_rademakers_1993]: https://doi.org/10.1016/0029-8018(93)90034-f
[research_radiative_heat_2018]: https://doi.org/10.1201/9780203737972-15
[research_rafique_linshu_2009]: https://doi.org/10.2514/6.2009-7246
[research_rafla_2019]: https://doi.org/10.2514/6.2019-3132
[research_rafla_2019_b]: https://doi.org/10.2514/6.2019-3132.c1
[research_ragnoli_savino_2024]: https://doi.org/10.1016/j.ast.2024.109092
[research_rahimi_devkumar_2013]: https://doi.org/10.2514/1.56387
[research_rahimi_svolos_2026]: https://doi.org/10.1016/j.engfracmech.2025.111794
[research_rahman_hao_2013]: https://doi.org/10.1109/ascc.2013.6606111
[research_raible_jacob_2003]: https://doi.org/10.2514/6.2003-6955
[research_raja_shekadar_2021]: https://doi.org/10.7860/jcdr/2021/47097.14728
[research_rajasekhar_john_2021]: https://doi.org/10.1007/978-981-16-0698-4_19
[research_rakdham_tummala_2007]: https://doi.org/10.1109/sysose.2007.4304314
[research_ramunno_boyd_2021]: https://doi.org/10.2514/6.2021-2440
[research_ran_huang_2023]: https://doi.org/10.1007/978-981-19-6613-2_229
[research_rana_chudoba_2016]: https://doi.org/10.2514/6.2016-5319
[research_rana_khan_2025]: https://doi.org/10.2514/6.2025-3528
[research_rand_1963]: https://doi.org/10.21236/ad0419249
[research_randolph_2005]: https://doi.org/10.1063/1.1867142
[research_raney_mcminn_1995]: https://doi.org/10.2514/3.46723
[research_rangaraj_divakar_2013]: https://doi.org/10.4018/978-1-4666-4066-5.ch004
[research_rao_1989]: https://doi.org/10.2514/3.20451
[research_rao_2011]: https://doi.org/10.1515/tjj.2011.023
[research_rao_2019]: https://doi.org/10.1109/icc47138.2019.9123236
[research_rao_crespo_2026]: https://doi.org/10.2514/6.2026-0307
[research_rarefied_hypersonic_1994]: https://doi.org/10.2514/5.9781600866326.0285.0295
[research_rasmussen_1980]: https://doi.org/10.2514/3.57771
[research_rasmussen_1983]: https://doi.org/10.2514/6.1983-2084
[research_rasmussen_1989]: https://doi.org/10.2514/6.1989-2675
[research_rasmussen_stevens_1987]: https://doi.org/10.2514/6.1987-2550
[research_rataczak_chaudhry_2024]: https://doi.org/10.2514/1.a35764
[research_rataczak_mcmahon_2023]: https://doi.org/10.2514/6.2023-1172
[research_rathod_sushnigdha_2025]: https://doi.org/10.1109/spert67079.2025.11469196
[research_ratnoo_2017]: https://doi.org/10.2514/1.g002459
[research_rauh_reimer_2026]: https://doi.org/10.2514/6.2026-5085
[research_rault_1992]: https://doi.org/10.1007/978-3-642-77922-0_72
[research_rault_1992_b]: https://doi.org/10.2514/6.1992-306
[research_rault_1994]: https://doi.org/10.2514/3.26504
[research_ravi_oda_2025]: https://doi.org/10.1007/s42405-025-00953-3
[research_ravichandran_ahmed_2023]: https://doi.org/10.2514/6.2023-3060
[research_ravichandran_doherty_2023]: https://doi.org/10.2514/6.2023-0437
[research_ravichandran_doherty_2023_b]: https://doi.org/10.2514/6.2023-0437.c1
[research_ray_2021]: https://doi.org/10.2514/6.2021-1159
[research_ray_de_2022]: https://doi.org/10.1103/aps.dfd.2022.gfm.v0051
[research_ray_de_2025]: https://doi.org/10.1007/978-981-97-6783-0_25
[research_raza_mehmood_2023]: https://doi.org/10.54690/margallapapers.27.1.149
[research_rc_k_2023]: https://doi.org/10.2514/6.2023-3017
[research_rea_putnam_2007]: https://doi.org/10.2514/6.2007-6424
[research_reaser_1997]: https://doi.org/10.1063/1.51928
[research_reda_wilder_2004]: https://doi.org/10.2514/6.2004-6829
[research_reddy_nagaraja_2024]: https://doi.org/10.1201/9781032713229-90
[research_reddy_sinha_2009]: https://doi.org/10.2514/1.41380
[research_reddy_sinha_2012]: https://doi.org/10.2514/6.2012-3002
[research_reentry_maneuvering_2025]: https://doi.org/10.37285/bsp.sacad2025.03
[research_reentry_trajectory_2024]: https://doi.org/10.2514/5.9781624107092.0207.0250
[research_reggiori_1971]: https://doi.org/10.2514/3.6262
[research_rehder_1973]: https://doi.org/10.2514/3.27783
[research_rehman_fidan_2009]: https://doi.org/10.2514/6.2009-7291
[research_reich_hinger_1990]: https://doi.org/10.4271/901306
[research_reilly_1964]: https://doi.org/10.1063/1.1711099
[research_reimer_dimartino_2023]: https://doi.org/10.2514/6.2023-3089
[research_reinartz_herrmann_2003]: https://doi.org/10.2514/2.6177
[research_ren_2009]: https://doi.org/10.2514/6.2009-7321
[research_ren_chen_2025]: https://doi.org/10.1016/b978-0-443-18598-4.00023-5
[research_ren_fu_2017]: https://doi.org/10.1177/1687814017703900
[research_ren_li_2014]: https://doi.org/10.1016/j.ceramint.2014.02.013
[research_ren_wang_2022]: https://doi.org/10.1007/978-981-16-9492-9_103
[research_ren_wang_2025]: https://doi.org/10.1007/s11071-025-11899-2
[research_ren_wu_2023]: https://doi.org/10.1109/taes.2023.3322977
[research_ren_yang_2017]: https://doi.org/10.1177/1729881416686953
[research_ren_yang_2019]: https://doi.org/10.1109/icusai47366.2019.9124790
[research_research_progress_2025]: https://doi.org/10.3901/jme.2025.10.001
[research_reubush_omar_1990]: https://doi.org/10.2514/3.25292
[research_review_1_2020]: https://doi.org/10.21428/cb6ab371.ae054b46
[research_review_2_2020]: https://doi.org/10.21428/cb6ab371.53f10aae
[research_review_3_2020]: https://doi.org/10.21428/cb6ab371.a2f3db67
[research_rhoads_duplessis_2023]: https://doi.org/10.2514/6.2023-71833
[research_rhudy_1970]: https://doi.org/10.2514/3.5713
[research_riabov_1994]: https://doi.org/10.2514/6.1994-2634
[research_riabov_1995]: https://doi.org/10.2514/3.46744
[research_riabov_2020]: https://doi.org/10.2514/6.2020-2450
[research_riabov_2026]: https://doi.org/10.1007/978-3-032-00094-1_17
[research_riabov_fedoseyev_2015]: https://doi.org/10.1007/978-3-319-16838-8_124
[research_ribe_1982]: https://doi.org/10.1109/oceans.1982.1151922
[research_ribe_1983]: https://doi.org/10.1109/joe.1983.1145584
[research_richards_culotta_1971]: https://doi.org/10.21236/ad0743836
[research_richmond_2022]: https://doi.org/10.2514/6.2022-2608
[research_riedelbauch_hirschel_1993]: https://doi.org/10.2514/3.46425
[research_rigby_rae_1989]: https://doi.org/10.2514/6.1989-1690
[research_riggins_camberos_2020]: https://doi.org/10.2514/1.c035659
[research_riggins_taylor_2003]: https://doi.org/10.2514/6.2003-6968
[research_rijbin_lin_1972]: https://doi.org/10.1016/0021-9991(72)90027-7
[research_riley_dejarnette_1992]: https://doi.org/10.2514/3.26355
[research_rishad_islam_2025]: https://doi.org/10.1016/j.oceram.2025.100817
[research_rizvi_he_2015]: https://doi.org/10.1016/j.dt.2015.06.003
[research_rizvi_linshu_2012]: https://doi.org/10.1063/1.4765577
[research_rizvi_linshu_2017]: https://doi.org/10.1017/aer.2017.11
[research_robinson_nolen_1995]: https://doi.org/10.2514/6.1995-3606
[research_rodi_2005]: https://doi.org/10.2514/6.2005-511
[research_rodi_2012]: https://doi.org/10.2514/6.2012-3222
[research_rodi_2012_b]: https://doi.org/10.2514/6.2012-1238
[research_rodi_2012_c]: https://doi.org/10.2514/6.2012-3223
[research_rodi_2015]: https://doi.org/10.2514/6.2015-1700
[research_rodi_2018]: https://doi.org/10.2514/6.2018-0554
[research_rodi_2018_b]: https://doi.org/10.2514/6.2018-3817
[research_rodi_2018_c]: https://doi.org/10.2514/6.2018-1048
[research_rodi_2018_d]: https://doi.org/10.2514/6.2018-0551
[research_rodi_2018_e]: https://doi.org/10.2514/6.2018-5196
[research_rodi_2020]: https://doi.org/10.2514/6.2020-2423
[research_rodi_2021]: https://doi.org/10.2514/6.2021-2542
[research_rodi_2021_b]: https://doi.org/10.2514/6.2021-2508
[research_rodi_2022]: https://doi.org/10.2514/6.2022-4050
[research_rodi_2023]: https://doi.org/10.2514/6.2023-2100
[research_rodi_bennett_2012]: https://doi.org/10.2514/6.2012-3221
[research_rodriguezsegade_hernandez_2022]: https://doi.org/10.1016/j.ast.2022.107514
[research_rodriguezsegade_hernandez_2024]: https://doi.org/10.1016/j.ast.2024.109346
[research_roenneke_cornwell_1992]: https://doi.org/10.2514/6.1992-1146
[research_roenneke_cornwell_1993]: https://doi.org/10.2514/3.21103
[research_roenneke_well_1996]: https://doi.org/10.2514/6.1996-3698
[research_roeser_graesslin_2010]: https://doi.org/10.2514/6.2010-8030
[research_rogers_schroeder_2022]: https://doi.org/10.2514/6.2022-3775
[research_rogers_slegers_2013]: https://doi.org/10.2514/1.59782
[research_rolim_minucci_2009]: https://doi.org/10.2514/6.2009-7433
[research_rolim_toro_2011]: https://doi.org/10.5028/jatm.2011.03027510
[research_rollins_valasek_2013]: https://doi.org/10.2514/6.2013-5234
[research_rollstin_1973]: https://doi.org/10.2514/6.1973-304
[research_rona_zavalan_2022]: https://doi.org/10.2139/ssrn.4061508
[research_rong_2017]: https://doi.org/10.12783/dtetr/apetc2017/11122
[research_rong_wei_2016]: https://doi.org/10.1051/matecconf/20166104008
[research_rong_yang_2017]: https://doi.org/10.1016/j.ast.2017.01.008
[research_rong_yang_2024]: https://doi.org/10.1007/978-981-97-1541-1_10
[research_ronghuang_yingziguan_2015]: https://doi.org/10.1109/aero.2015.7119000
[research_ronquillo_williams_1984]: https://doi.org/10.1177/109719638400700307
[research_rosa_valverde_1991]: https://doi.org/10.1016/0038-092x(91)90091-a
[research_rose_stankevics_1963]: https://doi.org/10.21236/ad0406269
[research_rosner_cibrian_1974]: https://doi.org/10.2514/6.1974-755
[research_rounds_1987]: https://doi.org/10.2514/6.1987-2592
[research_rowden_aslan_2022]: https://doi.org/10.1145/3565970.3567689
[research_roy_priyadarshi_2020]: https://doi.org/10.1007/978-981-15-5432-2_5
[research_rubin_1968]: https://doi.org/10.2514/6.1968-3
[research_rubin_shepps_1966]: https://doi.org/10.1145/1464291.1464375
[research_rubio_ramanujam_2018]: https://doi.org/10.1080/17436753.2018.1475140
[research_ruble_1964]: https://doi.org/10.2514/6.1964-291
[research_rucker_grandle_1973]: https://doi.org/10.1520/stp38844s
[research_rudiments_and_2001]: https://doi.org/10.2514/5.9781600866609.0939.0978
[research_ruger_1964]: https://doi.org/10.2514/3.2375
[research_rugescu_2013]: https://doi.org/10.4028/www.scientific.net/amm.332.33
[research_ruggles_tichenor_2025]: https://doi.org/10.2514/6.2025-0259
[research_ruimin_jianguo_2018]: https://doi.org/10.1109/iccre.2018.8376433
[research_ruisonghuang_weili_2015]: https://doi.org/10.1109/aero.2015.7118983
[research_running_sakaue_2019]: https://doi.org/10.1007/s00348-018-2665-2
[research_ruperti_cotta_2004]: https://doi.org/10.1080/01457630490486319
[research_rusnak_2000]: https://doi.org/10.2514/2.4593
[research_rusnak_2015]: https://doi.org/10.2514/1.g000267
[research_russo_roncioni_2026]: https://doi.org/10.2514/6.2026-5037
[research_ryan_lewis_2012]: https://doi.org/10.2514/6.2012-4862
[research_ryan_lewis_2013]: https://doi.org/10.2514/6.2013-4680
[research_ryoo_cho_2005]: https://doi.org/10.2514/1.8392
[research_s_padhi_2017]: https://doi.org/10.2514/6.2017-1267
[research_sabapathy_2026]: https://doi.org/10.4271/01-19-01-0003
[research_sacchetti_anfossi_1993]: https://doi.org/10.1007/bf02509214
[research_sachan_padhi_2018]: https://doi.org/10.2514/6.2018-0847
[research_sachan_padhi_2020]: https://doi.org/10.1016/j.conengprac.2020.104526
[research_sacher_1993]: https://doi.org/10.1007/978-3-642-45720-3_6
[research_sacher_zellner_1995]: https://doi.org/10.2514/6.1995-6014
[research_sachs_dinkelmann_1996]: https://doi.org/10.2514/3.21783
[research_sachs_dinkelmann_1996_b]: https://doi.org/10.2514/6.1996-3905
[research_sachs_heller_1996]: https://doi.org/10.2514/6.1996-3728
[research_sachs_lenz_2009]: https://doi.org/10.2514/6.2009-5626
[research_sachs_moravszki_2002]: https://doi.org/10.2514/6.2002-4696
[research_sachs_schoder_1991]: https://doi.org/10.2514/6.1991-2657
[research_sachs_schoder_1992]: https://doi.org/10.2514/6.1992-5013
[research_sadagopan_huang_2020]: https://doi.org/10.2514/6.2020-0937
[research_sager_1995]: https://doi.org/10.2514/6.1995-3859
[research_sagliano_lu_2024]: https://doi.org/10.2514/6.2024-1171
[research_sagliano_mooij_2016]: https://doi.org/10.2514/6.2016-2115
[research_sagliano_mooij_2017]: https://doi.org/10.2514/1.g000675
[research_saha_2023]: https://doi.org/10.2139/ssrn.4383402
[research_sahai_john_2014]: https://doi.org/10.2514/1.a32583
[research_saheby_huang_2017]: https://doi.org/10.2514/6.2017-2177
[research_sahu_vasile_2024]: https://doi.org/10.2514/6.2024-4338
[research_sainagabharghava_krishnatmali_2024]: https://doi.org/10.1016/j.ijheatfluidflow.2024.109413
[research_saito_kuwahara_2025]: https://doi.org/10.1016/j.actaastro.2024.12.054
[research_sakai_nakazawa_2017]: https://doi.org/10.1007/978-3-319-44866-4_7
[research_sakurai_kobayasi_1997]: https://doi.org/10.1016/s0094-5765(97)00149-5
[research_salah_1969]: https://doi.org/10.2514/3.5347
[research_saldivarmassimi_shen_2015]: https://doi.org/10.1016/j.ast.2015.03.017
[research_salleh_nazar_2009]: https://doi.org/10.1080/00986440902797840
[research_saltzman_wang_2007]: https://doi.org/10.2514/1.18365
[research_samotokhin_2021]: https://doi.org/10.20948/prepr-2021-5
[research_sana_hu_2020]: https://doi.org/10.1108/aeat-11-2019-0221
[research_sandeep_2023]: https://doi.org/10.5772/intechopen.107840
[research_sani_mercatelli_2012]: https://doi.org/10.2971/jeos.2012.12052
[research_sani_mercatelli_2013]: https://doi.org/10.1016/j.optmat.2013.08.020
[research_sankowski_2011]: https://doi.org/10.1049/iet-rsn.2011.0144
[research_sano_1981]: https://doi.org/10.1115/1.3244484
[research_santos_1993]: https://doi.org/10.2514/6.1993-5066
[research_santos_2004]: https://doi.org/10.2514/6.2004-5381
[research_santos_2005]: https://doi.org/10.1007/978-3-540-27009-6_26
[research_santos_2006]: https://doi.org/10.2514/6.2006-1194
[research_santos_2007]: https://doi.org/10.1590/s1678-58782007000200001
[research_santos_2007_b]: https://doi.org/10.2514/6.2007-615
[research_santos_2008]: https://doi.org/10.2514/6.2008-1183
[research_santos_2009]: https://doi.org/10.2514/1.41387
[research_santos_2011]: https://doi.org/10.2514/6.2011-2321
[research_santos_2012]: https://doi.org/10.1007/s13538-012-0100-3
[research_santos_2012_b]: https://doi.org/10.2514/6.2012-5802
[research_santos_beck_2008]: https://doi.org/10.2514/6.2008-4134
[research_santos_hosder_2020]: https://doi.org/10.2514/6.2020-2724
[research_santos_hosder_2021]: https://doi.org/10.2514/1.a34936
[research_santos_lewis_2002]: https://doi.org/10.2514/6.2002-645
[research_santos_lewis_2003]: https://doi.org/10.2514/6.2003-3894
[research_santos_lewis_2005]: https://doi.org/10.2514/1.9550
[research_saqib_linshu_2007]: https://doi.org/10.2514/6.2007-853
[research_saranathan_geldermans_2015]: https://doi.org/10.2514/6.2015-0014
[research_saranathan_grant_2016]: https://doi.org/10.2514/6.2016-3245
[research_saranathan_grant_2016_b]: https://doi.org/10.2514/6.2016-0020
[research_saranya_chinnaponnu_2018]: https://doi.org/10.1109/icctct.2018.8551059
[research_saravanan_jagadeesh_2009]: https://doi.org/10.1007/978-3-540-85168-4_102
[research_saravanan_pillai_2009]: https://doi.org/10.26634/jfet.5.1.1018
[research_sardar_2024]: https://doi.org/10.1109/space63117.2024.10668080
[research_sargunaraj_otto_2022]: https://doi.org/10.2514/6.2022-0266
[research_sargunaraj_otto_2023]: https://doi.org/10.2514/6.2023-0389
[research_sarkar_kar_2011]: https://doi.org/10.2514/6.2011-6339
[research_sarkar_mukherjee_2021]: https://doi.org/10.1016/j.asr.2020.10.006
[research_sarma_1996]: https://doi.org/10.1007/978-94-009-0267-1_1
[research_sarma_swamy_1989]: https://doi.org/10.2514/6.1989-3588
[research_sarosh_2021]: https://doi.org/10.20935/al2998
[research_sarosh_di_2013]: https://doi.org/10.1080/0305215x.2012.690758
[research_sarwar_rao_2024]: https://doi.org/10.1201/9788770046299-5
[research_sarziamade_bauer_2016]: https://doi.org/10.1007/978-3-319-34024-1_13
[research_sasoh_fujiwara_1990]: https://doi.org/10.2514/6.1990-2113
[research_satheesh_jagadeesh_2005]: https://doi.org/10.1007/978-3-540-27009-6_10
[research_satheesh_jagadeesh_2009]: https://doi.org/10.1007/978-3-540-85168-4_92
[research_satheeshchandran_sunitha_2021]: https://doi.org/10.1007/s41403-021-00217-y
[research_savage_1965]: https://doi.org/10.2514/6.1965-1242
[research_savage_chen_2000]: https://doi.org/10.1117/12.403619
[research_savelsberg_kampert_2026]: https://doi.org/10.24415/9789400605626-009
[research_savino_2010]: https://doi.org/10.2174/1874146001003010009
[research_savino_mungiguerra_2018]: https://doi.org/10.1080/17436753.2018.1509175
[research_savu_trifu_1993]: https://doi.org/10.2514/6.1993-5139
[research_sawada_dendou_2001]: https://doi.org/10.1007/pl00004059
[research_scala_1958]: https://doi.org/10.2514/8.7530
[research_scala_1962]: https://doi.org/10.21236/ad0294982
[research_scala_nolan_1960]: https://doi.org/10.1016/b978-1-4832-2885-3.50007-6
[research_scatteia_pichelin_2006]: https://doi.org/10.2514/6.iac-06-c2.4.04
[research_scatteia_riccio_2005]: https://doi.org/10.2514/6.2005-3266
[research_schafer_2002]: https://doi.org/10.1007/978-94-017-3008-2_27
[research_scheber_guthe_2013]: https://doi.org/10.1080/01495933.2013.754151
[research_schettino_borrelli_1998]: https://doi.org/10.2514/6.1998-1509
[research_schiavazzi_juliano_2020]: https://doi.org/10.2514/6.2020-1652
[research_schierman_hull_2005]: https://doi.org/10.2514/6.2005-6434
[research_schierman_ward_2001]: https://doi.org/10.21236/ada436268
[research_schmidt_1993]: https://doi.org/10.1016/b978-0-08-041715-8.50016-x
[research_schmidt_hermann_1998]: https://doi.org/10.2514/2.4199
[research_schmidt_lovell_1993]: https://doi.org/10.2514/6.1993-4009
[research_schmidt_nichols_2022]: https://doi.org/10.2514/6.2022-1576
[research_schmidt_velapoldi_1996]: https://doi.org/10.2514/6.1996-3904
[research_schmidtwimmer_beyer_2012]: https://doi.org/10.2514/6.2012-5908
[research_schmisseur_erbland_2012]: https://doi.org/10.1016/j.paerosci.2011.09.004
[research_schoeler_1987]: https://doi.org/10.21236/ada195832
[research_schoenenberger_hathaway_2005]: https://doi.org/10.2514/6.2005-55
[research_scholtz_weisman_1985]: https://doi.org/10.1007/978-1-4613-2455-3_3
[research_schoneman_amorosi_2005]: https://doi.org/10.2514/6.2005-6640
[research_schoneman_amorosi_2007]: https://doi.org/10.2514/6.2007-6145
[research_schoneman_buckley_2000]: https://doi.org/10.2514/6.2000-5068
[research_schouler_prevereaud_2021]: https://doi.org/10.1016/j.ijheatmasstransfer.2021.121582
[research_schouler_prevereaud_2023]: https://doi.org/10.1016/j.actaastro.2022.12.039
[research_schumacher_kinnersley_2003]: https://doi.org/10.1016/s0094-5765(03)00074-2
[research_schwanekamp_2014]: https://doi.org/10.2514/6.2014-2372
[research_schwartz_karpenko_2025]: https://doi.org/10.2514/6.2025-2267
[research_scigliano_desimone_2020]: https://doi.org/10.2514/6.2020-2422
[research_sciti_guicciardi_2014]: https://doi.org/10.1016/j.matdes.2013.10.019
[research_scott_1989]: https://doi.org/10.1007/978-1-4684-9187-6_8
[research_seager_agarwal_2015]: https://doi.org/10.2514/6.2015-1704
[research_sebastian_schreyer_2024]: https://doi.org/10.1016/j.ast.2024.109033
[research_sedlacek_1995]: https://doi.org/10.4028/www.scientific.net/kem.97-98.497
[research_sedlacek_1995_b]: https://doi.org/10.1002/pssa.2211490106
[research_selim_ozkol_2023]: https://doi.org/10.1109/rast57548.2023.10197982
[research_selim_ozkol_2023_b]: https://doi.org/10.2514/6.2023-3001
[research_sen_pesyridis_2018]: https://doi.org/10.3390/en11061568
[research_seo_lee_2022]: https://doi.org/10.5139/jksas.2022.50.4.277
[research_serrani_2010]: https://doi.org/10.3182/20100901-3-it-2016.00307
[research_sforza_2020]: https://doi.org/10.2514/6.2020-0281
[research_sforza_2020_b]: https://doi.org/10.2514/6.2020-0281.c1
[research_sforza_2026]: https://doi.org/10.3390/aerospace13020115
[research_shachar_benasher_2025]: https://doi.org/10.2514/1.g008439
[research_shaferman_shima_2008]: https://doi.org/10.2514/1.32836
[research_shahzad_weiduo_2014]: https://doi.org/10.1109/ibcast.2014.6778140
[research_shahzad_weiduo_2019]: https://doi.org/10.1109/ibcast.2019.8667154
[research_shaju_syamdas_2023]: https://doi.org/10.1007/978-981-19-7474-8_18
[research_shakiba_serrani_2011]: https://doi.org/10.2514/6.2011-6227
[research_shams_shah_2020]: https://doi.org/10.1109/ibcast47879.2020.9044523
[research_shan_liang_2018]: https://doi.org/10.1109/cac.2018.8623709
[research_shang_2002]: https://doi.org/10.2514/2.1769
[research_shang_2008]: https://doi.org/10.4208/cicp.2008.v4.p838
[research_shang_surzhikov_2010]: https://doi.org/10.2514/1.49923
[research_shang_surzhikov_2011]: https://doi.org/10.2514/6.2011-2258
[research_shang_weige_2018]: https://doi.org/10.1109/gncc42960.2018.9018995
[research_shao_lian_2014]: https://doi.org/10.3182/20140824-6-za-1003.00026
[research_shao_nie_2016]: https://doi.org/10.1016/j.ast.2016.02.005
[research_shao_wang_2015]: https://doi.org/10.1016/j.isatra.2014.06.010
[research_shao_wang_2015_b]: https://doi.org/10.1016/j.ast.2015.09.003
[research_shao_wang_2016]: https://doi.org/10.1016/j.jfranklin.2016.03.007
[research_shao_xu_2018]: https://doi.org/10.1109/gncc42960.2018.9018699
[research_shao_zhao_2025]: https://doi.org/10.1007/978-981-96-2232-0_36
[research_shao_zheng_2025]: https://doi.org/10.3390/s25216621
[research_shapiro_akin_2005]: https://doi.org/10.2514/6.2005-823
[research_sharifzadeh_verstraete_2015]: https://doi.org/10.1016/j.ijhydene.2015.07.120
[research_sharma_kumar_2023]: https://doi.org/10.1109/taes.2023.3237796
[research_sharma_wang_2020]: https://doi.org/10.2514/6.2020-1878
[research_sharpe_1969]: https://doi.org/10.2514/3.5444
[research_shaw_porter_2006]: https://doi.org/10.2514/6.2006-7991
[research_sheetz_1969]: https://doi.org/10.1007/978-1-4899-5579-1_3
[research_sheffer_dulikravich_1993]: https://doi.org/10.2514/6.1993-39
[research_shekhawat_sinha_2025]: https://doi.org/10.2514/6.2025-2268
[research_shekhawat_sinha_2026]: https://doi.org/10.1007/s42405-026-01263-y
[research_shen_huang_2019]: https://doi.org/10.1016/j.ast.2018.11.007
[research_shen_huang_2020]: https://doi.org/10.1016/j.ast.2020.105788
[research_shen_li_2009]: https://doi.org/10.1109/icacc.2009.72
[research_shen_li_2015]: https://doi.org/10.1002/oca.2172
[research_shen_lu_2003]: https://doi.org/10.2514/6.2003-5736
[research_shen_lu_2004]: https://doi.org/10.2514/1.8008
[research_shen_xia_2023]: https://doi.org/10.1016/j.isatra.2022.06.023
[research_shen_yu_2014]: https://doi.org/10.4028/www.scientific.net/amm.716-717.1624
[research_shen_yu_2022]: https://doi.org/10.1016/j.ast.2022.107363
[research_shengzheng_yuhang_2023]: https://doi.org/10.1088/1742-6596/2460/1/012033
[research_shenming_tao_2019]: https://doi.org/10.1109/crc.2019.00012
[research_sheporaitis_balbirnie_1976]: https://doi.org/10.2514/6.1976-1917
[research_sheta_venugopalan_2015]: https://doi.org/10.2514/6.2015-2166
[research_sheu_chen_1998]: https://doi.org/10.2514/6.1998-4462
[research_shevelev_2018]: https://doi.org/10.5772/intechopen.71666
[research_shevyrin_wu_2016]: https://doi.org/10.1063/1.4964080
[research_shi_dai_2015]: https://doi.org/10.2514/6.2015-3553
[research_shi_deng_2024]: https://doi.org/10.1007/978-981-97-1107-9_13
[research_shi_he_2017]: https://doi.org/10.1177/1687814017732894
[research_shi_jing_2013]: https://doi.org/10.1504/ijspacese.2013.051769
[research_shi_jing_2013_b]: https://doi.org/10.1109/ascc.2013.6606246
[research_shi_li_2025]: https://doi.org/10.1007/978-981-96-2264-1_43
[research_shi_miles_1997]: https://doi.org/10.2514/2.3175
[research_shi_niu_2023]: https://doi.org/10.1109/yac59482.2023.10401454
[research_shi_shao_2020]: https://doi.org/10.1016/j.ast.2019.105629
[research_shi_shi_2019]: https://doi.org/10.1007/978-981-13-3305-7_27
[research_shi_wang_2010]: https://doi.org/10.1109/iccis.2010.248
[research_shi_zha_2021]: https://doi.org/10.1016/j.jeurceramsoc.2021.03.015
[research_shi_zhang_2014]: https://doi.org/10.1109/chicc.2014.6896948
[research_shi_zhang_2020]: https://doi.org/10.1051/jnwpu/20203830523
[research_shi_zhou_2012]: https://doi.org/10.1007/978-3-642-34381-0_29
[research_shichao_aijun_2021]: https://doi.org/10.1007/978-981-15-8155-7_186
[research_shih_zwan_1988]: https://doi.org/10.2514/6.1988-2739
[research_shimada_ohwada_2020]: https://doi.org/10.1186/s42774-020-00037-8
[research_shinar_2004]: https://doi.org/10.1016/s1474-6670(17)32236-x
[research_shivank_harshul_2023]: https://doi.org/10.1134/s0869864323030046
[research_shock_layer_1962]: https://doi.org/10.2514/5.9781600864810.0379.0420
[research_shock_wave_relations_2023]: https://doi.org/10.1017/9781009030991.003
[research_shoemaker_vanderha_2012]: https://doi.org/10.1016/j.actaastro.2011.08.006
[research_shojaiebahaabad_bozorg_2024]: https://doi.org/10.1016/j.ceramint.2023.12.372
[research_shope_1991]: https://doi.org/10.2514/6.1991-3319
[research_shope_spinetti_1993]: https://doi.org/10.2514/6.1993-3444
[research_shorenstein_1971]: https://doi.org/10.21236/ad0731696
[research_shorenstein_1972]: https://doi.org/10.2514/3.50345
[research_shou_han_2024]: https://doi.org/10.1360/ssi-2024-0023
[research_shou_xu_2021]: https://doi.org/10.1016/j.ast.2021.106564
[research_shou_xu_2022]: https://doi.org/10.1002/mma.8071
[research_shou_zhan_2025]: https://doi.org/10.1109/taes.2024.3523460
[research_shruster_carpas_1983]: https://doi.org/10.2514/3.44962
[research_shu_hongying_2007]: https://doi.org/10.1016/s1000-9361(07)60059-4
[research_shuai_daqian_2022]: https://doi.org/10.1109/docs55193.2022.9967480
[research_shuck_noftz_2023]: https://doi.org/10.2514/6.2023-3895
[research_shukurov_2021]: https://doi.org/10.1117/12.2601736
[research_shupingtan_zhibinli_2010]: https://doi.org/10.1109/ccdc.2010.5498526
[research_shuvayanbrahmachary_ganeshnatarajan_2016]: https://doi.org/10.1007/978-81-322-2743-4_29
[research_shvets_voronin_2005]: https://doi.org/10.2514/6.2005-512
[research_sidor_kennedy_2020]: https://doi.org/10.2514/1.a34442
[research_siebenhaar_bogar_2006]: https://doi.org/10.2514/6.2006-7986
[research_sigthorsson_jankovsky_2008]: https://doi.org/10.2514/1.32300
[research_sigthorsson_serrani_2006]: https://doi.org/10.2514/6.2006-6558
[research_sills_2000]: https://doi.org/10.21236/ada388404
[research_sills_2001]: https://doi.org/10.21236/ada407068
[research_silvester_mcintyre_2007]: https://doi.org/10.1007/s00193-007-0100-3
[research_silvester_morgan_2004]: https://doi.org/10.2514/6.2004-3848
[research_silvestroni_sciti_2013]: https://doi.org/10.4018/978-1-4666-4066-5.ch005
[research_simeonides_2003]: https://doi.org/10.1007/s00193-003-0184-3
[research_simeonides_2006]: https://doi.org/10.1007/s00193-006-0040-3
[research_simmons_meritt_2022]: https://doi.org/10.2514/6.2022-3582
[research_simon_atchison_2021]: https://doi.org/10.2514/6.2021-2791
[research_simons_1975]: https://doi.org/10.21236/ada019517
[research_simons_1976]: https://doi.org/10.2514/3.7252
[research_sims_hahn_1964]: https://doi.org/10.21236/ad0603567
[research_simsek_kuran_2016]: https://doi.org/10.2514/6.2016-4428
[research_singh_2026]: https://doi.org/10.1109/icads69450.2026.11545481
[research_singh_devaraj_2017]: https://doi.org/10.1007/978-3-319-46213-4_26
[research_singh_g_2023]: https://doi.org/10.2514/6.2023-3012
[research_singh_prakash_2022]: https://doi.org/10.1007/978-3-030-99792-2_97
[research_singh_prakash_2022_b]: https://doi.org/10.1109/iconat53423.2022.9725896
[research_singh_prakash_2022_c]: https://doi.org/10.1109/iconat53423.2022.9725951
[research_singh_sinha_2023]: https://doi.org/10.61653/joast.v71i2.2019.142
[research_sinha_kumar_2021]: https://doi.org/10.2514/1.g005180
[research_sinha_reddy_2007]: https://doi.org/10.2514/6.2007-805
[research_sippel_klevanski_2006]: https://doi.org/10.2514/6.2006-7984
[research_sivells_1963]: https://doi.org/10.21236/ad0299774
[research_sivells_1969]: https://doi.org/10.2514/6.1969-337
[research_sivells_1970]: https://doi.org/10.2514/3.30160
[research_sivolella_2014]: https://doi.org/10.1007/978-1-4614-0983-0_8
[research_siyuan_xiaobing_2018]: https://doi.org/10.1109/iaeac.2018.8577900
[research_skolnik_kamezawa_2017]: https://doi.org/10.2514/6.2017-0469
[research_skripnyak_bragov_2017]: https://doi.org/10.1063/1.4971628
[research_skripnyak_skripnyak_2017]: https://doi.org/10.22226/2410-3535-2017-4-407-411
[research_skujins_cesnik_2010]: https://doi.org/10.2514/6.2010-8127
[research_slapikas_ghoshal_2022]: https://doi.org/10.21236/ad1171344
[research_slender_lifting_1994]: https://doi.org/10.2514/5.9781600866326.0261.0275
[research_smiley_camberos_2024]: https://doi.org/10.2514/6.2024-0167
[research_smith_2008]: https://doi.org/10.2514/1.33535
[research_smith_2021]: https://doi.org/10.1063/pt.3.4888
[research_smith_sitchin_2021]: https://doi.org/10.2514/6.2021-2456
[research_sobieczky_2026]: https://doi.org/10.1201/9781003760528-10
[research_socha_jafari_2015]: https://doi.org/10.1139/cjz-2014-0013
[research_sockalingam_tabiei_2009]: https://doi.org/10.1260/175095409788922284
[research_sogin_1991]: https://doi.org/10.1115/1.2910632
[research_son_son_2022]: https://doi.org/10.3390/aerospace9070348
[research_sonber_chmurthy_2013]: https://doi.org/10.4018/978-1-4666-4066-5.ch006
[research_song_bian_2019]: https://doi.org/10.1007/978-981-32-9698-5_20
[research_song_cai_2018]: https://doi.org/10.1061/(asce)as.1943-5525.0000855
[research_song_choi_2020]: https://doi.org/10.1016/j.ifacol.2020.12.1900
[research_song_hao_2019]: https://doi.org/10.1109/icca.2019.8899548
[research_song_li_2021]: https://doi.org/10.1109/jsen.2021.3077727
[research_song_liu_2024]: https://doi.org/10.23919/ccc63176.2024.10661581
[research_song_luo_2022]: https://doi.org/10.3390/math10183401
[research_song_shi_2026]: https://doi.org/10.1007/978-981-95-7342-4_35
[research_song_tong_2022]: https://doi.org/10.3390/aerospace9080427
[research_song_tong_2026]: https://doi.org/10.1007/s42423-026-00205-w
[research_song_zhu_2024]: https://doi.org/10.1109/cac63892.2024.10865083
[research_sostaric_cerimele_2017]: https://doi.org/10.2514/6.2017-1898
[research_sostaric_garcia_2019]: https://doi.org/10.2514/6.2019-0664
[research_space_shuttle_1983]: https://doi.org/10.2514/5.9781600865626.0206.0233
[research_spearman_1984]: https://doi.org/10.2514/6.1984-2146
[research_spearman_2003]: https://doi.org/10.2514/6.2003-7061
[research_speyer_dannemiller_1980]: https://doi.org/10.2514/6.1980-1777
[research_spinardi_2008]: https://doi.org/10.3152/030234208x394688
[research_spravka_jorris_2015]: https://doi.org/10.2514/6.2015-3224
[research_spravka_jorris_2015_b]: https://doi.org/10.21236/ada619521
[research_sprinks_2011]: https://doi.org/10.7748/paed.23.2.4.s2
[research_sridharan_rodriguez_2013]: https://doi.org/10.2514/6.2013-5166
[research_srinath_reddy_2010]: https://doi.org/10.1260/1759-3107.1.2.93
[research_srivastava_mishra_2022]: https://doi.org/10.1016/j.ifacol.2023.03.053
[research_stalonydobrzanski_1966]: https://doi.org/10.2514/6.1966-407
[research_stanley_alexander_1999]: https://doi.org/10.2514/6.1999-4808
[research_starkey_2014]: https://doi.org/10.2514/6.2014-3111
[research_starkey_2015]: https://doi.org/10.2514/1.a32051
[research_starkey_lewis_1999]: https://doi.org/10.2514/6.1999-4953
[research_starkey_lewis_1999_b]: https://doi.org/10.2514/6.1999-2378
[research_starkey_lewis_2000]: https://doi.org/10.2514/2.3618
[research_starkey_lewis_2001]: https://doi.org/10.2514/2.3734
[research_starkey_rankins_2005]: https://doi.org/10.2514/6.2005-530
[research_starkey_rankins_2006]: https://doi.org/10.2514/6.2006-337
[research_starshak_laurence_2021]: https://doi.org/10.2514/1.j060017
[research_stecklein_hasen_1993]: https://doi.org/10.2514/6.1993-320
[research_steelant_vanduijn_2011]: https://doi.org/10.2514/6.2011-2336
[research_steele_2009]: https://doi.org/10.21236/ada540092
[research_steffan_1961]: https://doi.org/10.2514/8.5842
[research_stein_raghavan_2024]: https://doi.org/10.2514/6.2024-0366
[research_steinfeldt_rossman_2013]: https://doi.org/10.2514/6.2013-31
[research_stender_loghry_2017]: https://doi.org/10.1109/aero.2017.7943818
[research_stephan_obermeier_1974]: https://doi.org/10.1615/ihtc5.2210
[research_stern_chu_1963]: https://doi.org/10.21236/ad0405109
[research_stevens_1992]: https://doi.org/10.2514/6.1992-4247
[research_stevens_lockwood_1995]: https://doi.org/10.2514/6.1995-3623
[research_stewart_leiser_1985]: https://doi.org/10.2514/6.1985-248
[research_stewart_leiser_2006]: https://doi.org/10.2514/6.2006-7945
[research_stewart_smith_1992]: https://doi.org/10.2514/6.1992-836
[research_stiles_1970]: https://doi.org/10.1016/s1474-6670(17)68824-4
[research_stoffel_karlgaard_2024]: https://doi.org/10.2514/1.a35641
[research_stokes_lombaerts_2023]: https://doi.org/10.2514/6.2023-1638
[research_stoll_1961]: https://doi.org/10.21236/ad0259076
[research_stollery_1992]: https://doi.org/10.1007/978-3-642-77922-0_14
[research_stollery_2010]: https://doi.org/10.1017/s0001924000088163
[research_stoner_1972]: https://doi.org/10.2514/6.1972-834
[research_strauss_1966]: https://doi.org/10.4271/660654
[research_strippoli_colmenarejo_2013]: https://doi.org/10.1051/eucass/201306123
[research_strohm_2011]: https://doi.org/10.21236/ada553607
[research_strohmeyer_eggers_1997]: https://doi.org/10.1007/978-3-322-86573-1_42
[research_su_2017]: https://doi.org/10.2514/6.2017-2297
[research_su_dai_2021]: https://doi.org/10.1016/j.ast.2021.107200
[research_su_hong_2025]: https://doi.org/10.1080/23307706.2025.2556335
[research_su_jiang_2013]: https://doi.org/10.1007/s10015-013-0099-8
[research_su_liu_2025]: https://doi.org/10.1016/j.asoc.2024.112637
[research_su_liu_2025_b]: https://doi.org/10.1016/j.ast.2024.109839
[research_su_wang_2023]: https://doi.org/10.3390/aerospace10110948
[research_su_yu_2013]: https://doi.org/10.5139/ijass.2013.14.3.247
[research_su_zhao_2024]: https://doi.org/10.1088/1742-6596/2764/1/012069
[research_subrahmanyam_2008]: https://doi.org/10.1080/19942060.2008.11015243
[research_sudalagunta_sultan_2018]: https://doi.org/10.2514/1.g002777
[research_sudhir_tewari_2007]: https://doi.org/10.1016/j.ast.2007.02.005
[research_sui_niu_2023]: https://doi.org/10.1016/j.tust.2023.105126
[research_sun_cao_2026]: https://doi.org/10.3390/aerospace13070608
[research_sun_chen_2024]: https://doi.org/10.1088/1742-6596/2882/1/012085
[research_sun_duan_2012]: https://doi.org/10.1109/wcica.2012.6358286
[research_sun_fan_2009]: https://doi.org/10.2514/6.2009-7229
[research_sun_han_2024]: https://doi.org/10.1109/aaac63570.2024.11027404
[research_sun_huang_2017]: https://doi.org/10.23919/chicc.2017.8028353
[research_sun_huang_2025]: https://doi.org/10.1109/ccdc65474.2025.11090502
[research_sun_li_2026]: https://doi.org/10.1109/taes.2026.3687820
[research_sun_li_2026_b]: https://doi.org/10.1016/j.ast.2026.111909
[research_sun_li_2026_c]: https://doi.org/10.1002/rnc.70621
[research_sun_li_2026_d]: https://doi.org/10.1016/j.ast.2026.112696
[research_sun_liu_2025]: https://doi.org/10.1109/cac67268.2025.11486810
[research_sun_ma_2024]: https://doi.org/10.1109/taes.2024.3417425
[research_sun_qu_2018]: https://doi.org/10.1016/j.compfluid.2018.05.028
[research_sun_ran_2025]: https://doi.org/10.1109/jsen.2025.3598737
[research_sun_song_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000775
[research_sun_sun_2014]: https://doi.org/10.4028/www.scientific.net/amm.644-650.4718
[research_sun_tang_2022]: https://doi.org/10.2514/6.2022-0762
[research_sun_xia_2022]: https://doi.org/10.1117/12.2638787
[research_sun_xin_2014]: https://doi.org/10.2514/6.2014-2383
[research_sun_xin_2017]: https://doi.org/10.1016/j.actaastro.2017.01.036
[research_sun_xu_2017]: https://doi.org/10.1016/j.ast.2017.09.036
[research_sun_xu_2022]: https://doi.org/10.1002/oca.2891
[research_sun_yang_2013]: https://doi.org/10.2514/1.57739
[research_sun_yang_2014]: https://doi.org/10.1080/00207179.2014.983169
[research_sun_yang_2015]: https://doi.org/10.1360/n092014-00463
[research_sun_yang_2020]: https://doi.org/10.12783/dtcse/cmso2019/33628
[research_sun_yang_2020_b]: https://doi.org/10.1155/2020/3850283
[research_sun_zhang_2011]: https://doi.org/10.1109/icicip.2011.6008304
[research_sun_zhang_2020]: https://doi.org/10.3390/s20102976
[research_sun_zhao_2013]: https://doi.org/10.1166/asl.2013.4551
[research_sun_zheng_2024]: https://doi.org/10.2514/1.j063430
[research_sun_zhu_2019]: https://doi.org/10.1063/1.5083820
[research_sun_zhu_2023]: https://doi.org/10.3390/aerospace10030310
[research_sun_zhu_2025]: https://doi.org/10.1016/j.ast.2024.109777
[research_sunjian_liuweiqiang_2013]: https://doi.org/10.7498/aps.62.074401
[research_sunjian_liuweiqiang_2014]: https://doi.org/10.7498/aps.63.094401
[research_supercircular_re_entry_1963]: https://doi.org/10.2514/5.9781600864834.0703.0733
[research_supersonic_hypersonic_euler_1990]: https://doi.org/10.2514/5.9781600865985.0839.0861
[research_sushnigdha_2022]: https://doi.org/10.1016/j.ifacol.2022.04.008
[research_sushnigdha_joshi_2016]: https://doi.org/10.1016/j.ifacol.2016.07.136
[research_sushnigdha_joshi_2017]: https://doi.org/10.2514/6.2017-4209
[research_sushnigdha_joshi_2018]: https://doi.org/10.1061/(asce)as.1943-5525.0000929
[research_sushnigdha_joshi_2018_b]: https://doi.org/10.1016/j.engappai.2017.11.010
[research_susic_davuluri_2026]: https://doi.org/10.2514/6.2026-2939
[research_sutheesh_chollackal_2020]: https://doi.org/10.1007/978-981-15-1063-2_38
[research_suvorova_khadyrova_2023]: https://doi.org/10.1016/j.ceramint.2023.04.222
[research_suwantong_bertrand_2012]: https://doi.org/10.1109/cdc.2012.6426215
[research_suzuki_2001]: https://doi.org/10.1016/s1474-6670(17)40725-7
[research_suzuki_2016]: https://doi.org/10.2322/tastj.14.pe_71
[research_suzuki_2018]: https://doi.org/10.2322/tastj.16.412
[research_suzuki_furudate_2001]: https://doi.org/10.2514/6.2001-980
[research_suzuki_furudate_2002]: https://doi.org/10.2514/2.6656
[research_suzuki_ishimoto_1997]: https://doi.org/10.2322/jjsass1969.45.635
[research_suzuki_sawada_2002]: https://doi.org/10.1299/jsmemecjo.2002.1.0_301
[research_swain_1975]: https://doi.org/10.2514/6.1975-734
[research_swain_chauhan_2025]: https://doi.org/10.1109/icort64008.2025.11115327
[research_swain_sushnigdha_2025]: https://doi.org/10.1109/spert67079.2025.11469284
[research_swann_1960]: https://doi.org/10.1016/b978-1-4832-2885-3.50008-8
[research_swanson_caghlan_2007]: https://doi.org/10.2514/6.2007-1670
[research_sworder_archer_1977]: https://doi.org/10.2514/6.1977-1053
[research_sziroczak_smith_2016]: https://doi.org/10.1016/j.paerosci.2016.04.001
[research_t_cm_2017]: https://doi.org/10.4172/2168-9792.1000202
[research_tabiei_sockalingam_2012]: https://doi.org/10.1061/(asce)as.1943-5525.0000113
[research_tablole_banavar_1998]: https://doi.org/10.14429/dsj.48.4043
[research_tacchi_martin_2023]: https://doi.org/10.2514/6.2023-3733
[research_tacchi_stoffel_2024]: https://doi.org/10.2514/1.a35826
[research_tachinina_lysenko_2018]: https://doi.org/10.1109/msnmc.2018.8576319
[research_taguchi_harada_2009]: https://doi.org/10.2514/6.2009-7311
[research_taguchi_murakami_2009]: https://doi.org/10.2322/tstj.7.pa_27
[research_taheri_ahmadi_2026]: https://doi.org/10.2514/6.2026-1665
[research_tahmasbi_noori_2018]: https://doi.org/10.2514/1.t5051
[research_tahsini_mousavi_2014]: https://doi.org/10.4028/www.scientific.net/amm.598.298
[research_taihua_xianhong_2011]: https://doi.org/10.5772/13604
[research_takahashi_griffin_2023]: https://doi.org/10.2514/6.2023-2248
[research_takahashi_hirotani_2025]: https://doi.org/10.2514/6.2025-1340
[research_takahashi_hirotani_2026]: https://doi.org/10.2514/1.j065479
[research_takahashi_yamada_2013]: https://doi.org/10.2514/6.2013-1303
[research_takahashi_yamada_2015]: https://doi.org/10.2514/1.a33170
[research_takahashi_yamada_2018]: https://doi.org/10.1016/j.actaastro.2018.08.003
[research_takama_2011]: https://doi.org/10.2514/6.2011-2300
[research_takashima_lewis_1992]: https://doi.org/10.2514/6.1992-305
[research_takashima_lewis_1994]: https://doi.org/10.2514/3.26450
[research_takashima_lewis_1995]: https://doi.org/10.2514/3.46848
[research_takashima_lewis_1995_b]: https://doi.org/10.2514/6.1995-846
[research_takashima_lewis_1996]: https://doi.org/10.2514/6.1996-4593
[research_takashima_lewis_1996_b]: https://doi.org/10.2514/6.1996-810
[research_takashima_lewis_1996_c]: https://doi.org/10.2514/6.1996-2551
[research_takashima_lewis_1999]: https://doi.org/10.2514/2.2430
[research_takehira_vinh_1997]: https://doi.org/10.2514/6.1997-3472
[research_takehira_vinh_1998]: https://doi.org/10.2514/2.4241
[research_talbot_1963]: https://doi.org/10.2514/3.1742
[research_tan_lei_2019]: https://doi.org/10.1109/access.2019.2916464
[research_tan_yan_2012]: https://doi.org/10.3724/sp.j.1087.2011.01723
[research_tang_cai_2025]: https://doi.org/10.1063/5.0297492
[research_tang_chen_2011]: https://doi.org/10.1109/emeit.2011.6022991
[research_tang_chen_2023]: https://doi.org/10.33737/gpps23-tc-254
[research_tang_di_2022]: https://doi.org/10.1109/access.2022.3187712
[research_tang_gao_2021]: https://doi.org/10.1109/cac53003.2021.9728007
[research_tang_he_2020]: https://doi.org/10.1109/ccdc49329.2020.9164575
[research_tang_hu_2023]: https://doi.org/10.23919/ccc58697.2023.10240416
[research_tang_li_2025]: https://doi.org/10.1063/5.0256817
[research_tang_long_2018]: https://doi.org/10.3103/s0146411618030100
[research_tang_luo_2022]: https://doi.org/10.1109/iai55780.2022.9976736
[research_tang_wang_2021]: https://doi.org/10.1063/5.0069666
[research_tang_zhai_2020]: https://doi.org/10.1016/j.ins.2019.08.012
[research_tang_zhang_2025]: https://doi.org/10.1007/978-981-96-2240-5_40
[research_tangermann_furman_2012]: https://doi.org/10.2514/6.2012-3329
[research_tannas_1966]: https://doi.org/10.2514/6.1966-1831
[research_tannehill_eisler_1976]: https://doi.org/10.1063/1.861304
[research_tannehill_mohling_1974]: https://doi.org/10.2514/3.49181
[research_tanriverdi_cavdaroglu_2017]: https://doi.org/10.2514/6.2017-1033
[research_tao_li_2016]: https://doi.org/10.1016/j.ins.2015.08.033
[research_tao_wan_2017]: https://doi.org/10.1108/aeat-06-2013-0119
[research_tao_zhou_2025]: https://doi.org/10.1109/icus66297.2025.11294812
[research_taoguo_daweiliu_2010]: https://doi.org/10.1109/icacte.2010.5578951
[research_taoxu_xiaopingzhu_2011]: https://doi.org/10.1109/icinfa.2011.5949079
[research_tarjani_2023]: https://doi.org/10.32565/aarms.2023.1.7
[research_tarpley_lewis_1995]: https://doi.org/10.2514/3.46793
[research_tarpley_lewis_1995_b]: https://doi.org/10.2514/6.1995-6142
[research_tarpley_lewis_1995_c]: https://doi.org/10.2514/6.1995-848
[research_tarpley_pines_1996]: https://doi.org/10.2514/6.1996-4596
[research_tartabini_starr_2011]: https://doi.org/10.2514/6.2011-6462
[research_tate_1964]: https://doi.org/10.2514/6.1964-1114
[research_tater_holman_2026]: https://doi.org/10.14311/tpfm.2026.031
[research_tatsuta_nagata_2025]: https://doi.org/10.2514/6.2025-0644
[research_taub_1968]: https://doi.org/10.2514/3.4812
[research_tauber_sutton_1991]: https://doi.org/10.2514/3.26206
[research_taur_2013]: https://doi.org/10.2514/6.2013-5245
[research_tava_suzuki_2001]: https://doi.org/10.2514/6.2001-1920
[research_tava_suzuki_2002]: https://doi.org/10.2322/tjsass.45.10
[research_tawfiqur_zhou_2011]: https://doi.org/10.4028/www.scientific.net/amm.110-116.5232
[research_taylor_2004]: https://doi.org/10.2514/6.2004-131
[research_taylor_jackson_1980]: https://doi.org/10.2514/6.1980-407
[research_tejtel_rothnie_2011]: https://doi.org/10.2514/6.2011-2240
[research_teng_xu_2023]: https://doi.org/10.1109/cac59555.2023.10450668
[research_teng_yang_2016]: https://doi.org/10.1177/1729881416678140
[research_teng_yuan_2013]: https://doi.org/10.4028/www.scientific.net/amm.275-277.433
[research_tengli_shetty_2025]: https://doi.org/10.1007/978-3-031-76937-5_5
[research_terasaki_1963]: https://doi.org/10.2514/6.1963-320
[research_terminal_guidance_1962]: https://doi.org/10.2514/5.9781600864827.0217.0239
[research_terminal_phase_2023]: https://doi.org/10.37285/bsp.sasat2023.09
[research_the_falcon_2004]: https://doi.org/10.2514/6.iac-04-iaa.4.11.5.03
[research_the_hypersonic_1982]: https://doi.org/10.2514/5.9781600865565.0177.0200
[research_theisinger_braun_2010]: https://doi.org/10.2514/6.2010-9200
[research_theobald_1966]: https://doi.org/10.2514/3.55255
[research_theofilis_hermanns_2013]: https://doi.org/10.2514/6.2013-2980
[research_thermal_protection_1963]: https://doi.org/10.2514/5.9781600864834.0433.0447
[research_thermal_protection_1980]: https://doi.org/10.1016/0010-4361(80)90072-5
[research_thermal_protection_1981]: https://doi.org/10.2514/5.9781600865510.0309.0334
[research_thermal_protection_1985]: https://doi.org/10.2514/5.9781600865718.0257.0285
[research_thermal_protection_2013]: https://doi.org/10.2514/5.9781624101717.0001.0030
[research_thermal_protection_2014]: https://doi.org/10.1007/978-94-007-2739-7_100677
[research_thermal_protection_2015]: https://doi.org/10.21275/v4i11.nov151618
[research_thiagarajan_sharma_2023]: https://doi.org/10.61653/joast.v67i2.2015.301
[research_thibodeaux_2002]: https://doi.org/10.2514/6.2002-2109
[research_thien_2026]: https://doi.org/10.63680/ijsate0726045.44
[research_thivet_pelissier_2003]: https://doi.org/10.2514/6.2003-7013
[research_thoemel_muylaert_2009]: https://doi.org/10.2514/6.2009-7232
[research_thomas_marayikkottuvijayan_2022]: https://doi.org/10.2514/6.2022-1499
[research_thomas_stickels_1982]: https://doi.org/10.1109/oceans.1982.1151920
[research_thome_dwivedi_2018]: https://doi.org/10.2514/6.2018-2894
[research_thompson_hull_1970]: https://doi.org/10.1007/bf00927442
[research_thompson_riley_1994]: https://doi.org/10.2514/3.26415
[research_thornton_2019]: https://doi.org/10.1080/13518046.2019.1552655
[research_tian_duan_2023]: https://doi.org/10.1155/2023/1920270
[research_tian_fan_2015]: https://doi.org/10.1007/s11071-014-1877-0
[research_tian_li_2013]: https://doi.org/10.1016/j.cja.2013.07.003
[research_tian_shen_2022]: https://doi.org/10.1177/16878132221111208
[research_tian_tang_2013]: https://doi.org/10.4028/www.scientific.net/amm.275-277.513
[research_tian_zhang_2013]: https://doi.org/10.1109/jsee.2013.00012
[research_tian_zong_2011]: https://doi.org/10.1016/j.actaastro.2010.10.010
[research_tianmuyin_shenzuojun_2019]: https://doi.org/10.3233/faia190185
[research_tianyang_jiahao_2024]: https://doi.org/10.1088/1742-6596/2891/11/112026
[research_tieshan_zhiyao_2021]: https://doi.org/10.1109/ccdc52312.2021.9601884
[research_tile_gap_flow_1983]: https://doi.org/10.2514/5.9781600865626.0271.0299
[research_timchenko_bimatov_2004]: https://doi.org/10.1016/b978-044451612-1/50057-3
[research_tincher_burnett_1992]: https://doi.org/10.2514/6.1992-308
[research_tincher_burnett_1994]: https://doi.org/10.2514/3.26451
[research_tirres_bradley_2002]: https://doi.org/10.2514/6.2002-2706
[research_tittmann_bommel_1968]: https://doi.org/10.1063/1.1683458
[research_tiwari_chow_1981]: https://doi.org/10.2514/6.1981-1128
[research_tiwari_thomas_1994]: https://doi.org/10.2514/6.1994-767
[research_tobe_grandhi_2013]: https://doi.org/10.1016/j.ast.2012.11.001
[research_tobin_dec_2015]: https://doi.org/10.2514/6.2015-1895
[research_tokarcik_venkatapathy_1991]: https://doi.org/10.2514/6.1991-3303
[research_tokuda_yang_2019]: https://doi.org/10.1615/ihtc3.1840
[research_tokunaga_sotoguchi_2019]: https://doi.org/10.2514/6.2019-2235
[research_tomar_2014]: https://doi.org/10.4028/www.scientific.net/ast.89.100
[research_tong_1965]: https://doi.org/10.2514/3.2979
[research_tong_giedt_1963]: https://doi.org/10.21236/ad0403711
[research_tong_wu_2026]: https://doi.org/10.1109/icaace69793.2026.11509033
[research_tormo_serghides_2007]: https://doi.org/10.2514/1.30613
[research_tournes_2013]: https://doi.org/10.2514/6.2013-4609
[research_tournes_johnson_1999]: https://doi.org/10.2514/6.1999-3979
[research_toussaint_braeunig_2023]: https://doi.org/10.2514/6.2023-3849
[research_townend_1979]: https://doi.org/10.1016/0376-0421(79)90001-0
[research_toyama_shimbo_1996]: https://doi.org/10.1121/1.417020
[research_traci_wilcox_1974]: https://doi.org/10.2514/6.1974-515
[research_tracy_wright_2020]: https://doi.org/10.1080/08929882.2020.1864945
[research_tracy_wright_2023]: https://doi.org/10.1080/08929882.2023.2215587
[research_trajectory_shaping_2025]: https://doi.org/10.37285/bsp.sacad2025.24
[research_trent_doman_2007]: https://doi.org/10.1109/acc.2007.4282306
[research_trettel_ezekoye_2015]: https://doi.org/10.1115/imece2015-52103
[research_trivedi_menezes_2012]: https://doi.org/10.1016/j.measurement.2012.04.008
[research_tsai_miles_1992]: https://doi.org/10.2514/6.1992-2726
[research_tsuchiya_takenaka_2007]: https://doi.org/10.2514/1.26668
[research_tsuchiya_takenaka_2007_b]: https://doi.org/10.2322/tjsass.50.141
[research_tsuda_kikuchi_2024]: https://doi.org/10.2322/tjsass.67.340
[research_tsukahara_yamao_2001]: https://doi.org/10.2514/6.2001-1909
[research_tu_yuan_2006]: https://doi.org/10.2514/6.iac-06-c1.4.06
[research_tu_yuan_2006_b]: https://doi.org/10.2514/6.2006-7993
[research_tului_marino_2006]: https://doi.org/10.1016/j.surfcoat.2006.04.053
[research_turkoglu_donmez_2026]: https://doi.org/10.1016/j.ast.2026.113022
[research_turner_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50015-4
[research_turner_hoerschgen_2006]: https://doi.org/10.2514/6.2006-8115
[research_turri_klaput_2011]: https://doi.org/10.2514/6.2011-2239
[research_tuttle_mee_1994]: https://doi.org/10.2514/6.1994-2596
[research_tuzlukov_2026]: https://doi.org/10.1201/9781003408802-6
[research_ueda_shiba_2011]: https://doi.org/10.1093/pasj/63.5.947
[research_ueno_imamura_2011]: https://doi.org/10.2514/6.2011-2340
[research_ueno_suzuki_2008]: https://doi.org/10.2514/6.2008-288
[research_ueno_suzuki_2009]: https://doi.org/10.2322/tjsass.52.65
[research_ulislamrizvi_linshu_2015]: https://doi.org/10.1108/aeat-04-2013-0079
[research_ulybyshev_2005]: https://doi.org/10.2514/1.12545
[research_unsteady_interaction_2023]: https://doi.org/10.1063/5.0151663
[research_upadhyay_kumar_2019]: https://doi.org/10.33564/ijeast.2019.v04i07.025
[research_uzaki_muta_2017]: https://doi.org/10.1299/jsmekyushu.2017.70.502
[research_vaganov_grachikov_2017]: https://doi.org/10.1063/1.5007528
[research_vaganov_zhestkov_2016]: https://doi.org/10.1063/1.4964039
[research_vahl_edwards_1978]: https://doi.org/10.2514/6.1978-38
[research_vaknin_idan_2026]: https://doi.org/10.2514/6.2026-1745
[research_vala_rana_2023]: https://doi.org/10.1007/978-3-031-38446-2_41
[research_valente_bartuli_2000]: https://doi.org/10.31399/asm.cp.itsc2000p0837
[research_vali_abbasi_2022]: https://doi.org/10.1016/j.ijheatmasstransfer.2022.123034
[research_vanbrummen_pezzella_2015]: https://doi.org/10.2514/6.2015-3644
[research_vandenabeelen_2016]: https://doi.org/10.1007/978-3-319-44472-7_20
[research_vanderheide_bone_2026]: https://doi.org/10.2514/6.2026-0369
[research_vanderheide_lock_2025]: https://doi.org/10.2514/6.2025-0955
[research_vanmol_andersonjr_1992]: https://doi.org/10.2514/6.1992-2920
[research_vaughn_garrard_2012]: https://doi.org/10.2514/6.2012-2729
[research_vedula_1989]: https://doi.org/10.21236/ada230593
[research_veeran_pesyridis_2018]: https://doi.org/10.3390/en11102558
[research_vemuri_1982]: https://doi.org/10.21236/ada113076
[research_vendemia_rj_1965]: https://doi.org/10.21236/ad0630342
[research_venkates_pillai_2020]: https://doi.org/10.1063/5.0024230
[research_vennik_neely_2017]: https://doi.org/10.2514/6.2017-2194
[research_venugopal_grandhi_1991]: https://doi.org/10.1016/0094-5765(91)90043-5
[research_veraar_2009]: https://doi.org/10.2514/6.2009-7379
[research_verma_xu_2007]: https://doi.org/10.2514/6.2007-6537
[research_vernis_spreng_2011]: https://doi.org/10.2514/6.2011-6649
[research_vijayakumar_narendar_2020]: https://doi.org/10.1007/978-981-15-1201-8_33
[research_villanueva_2022]: https://doi.org/10.1109/eircon56026.2022.9934090
[research_villanueva_2022_b]: https://doi.org/10.1109/aero53065.2022.9843685
[research_villanueva_he_2013]: https://doi.org/10.4028/www.scientific.net/amm.302.583
[research_villanueva_linshu_2014]: https://doi.org/10.5028/jatm.v6i3.333
[research_vinh_medepalli_1994]: https://doi.org/10.1007/978-1-4615-2425-0_14
[research_viotto_francesconi_2012]: https://doi.org/10.2514/6.2012-5847
[research_viscous_flow_2006]: https://doi.org/10.2514/5.9781600861956.0261.0374
[research_viscous_flow_2019]: https://doi.org/10.2514/5.9781624105142.0267.0388
[research_viscous_shock_layer_1983]: https://doi.org/10.2514/5.9781600865626.0054.0077
[research_vitiello_leonardi_2023]: https://doi.org/10.2514/1.a35438
[research_viviand_1991]: https://doi.org/10.1007/978-3-642-84580-2_7
[research_viviani_pezzella_2006]: https://doi.org/10.2514/6.2006-8082
[research_viviani_pezzella_2007]: https://doi.org/10.2514/6.2007-1211
[research_viviani_pezzella_2007_b]: https://doi.org/10.2514/6.2007-4047
[research_viviani_pezzella_2008]: https://doi.org/10.1615/ichmt.2008.cht.1790
[research_viviani_pezzella_2015]: https://doi.org/10.1007/978-3-319-13927-2_1
[research_viviani_pezzella_2019]: https://doi.org/10.5772/intechopen.87988
[research_vkbhuvaneswar_sharifshaik_2025]: https://doi.org/10.21275/sr251101104047
[research_vlahopoulos_he_2009]: https://doi.org/10.4271/2009-01-0564
[research_voevodenko_1995]: https://doi.org/10.2514/6.1995-3924
[research_vogel_kelkar_2009]: https://doi.org/10.2514/6.2009-7383
[research_voland_huebner_2006]: https://doi.org/10.1016/j.actaastro.2006.02.021
[research_volokhov_toktaliev_2016]: https://doi.org/10.1007/978-3-319-55669-7_19
[research_vonegger_pines_1998]: https://doi.org/10.2514/6.1998-1585
[research_vonegger_pines_1999]: https://doi.org/10.2514/6.1999-4951
[research_voneggersrudd_pines_2000]: https://doi.org/10.2514/2.4598
[research_vorst_zell_2010]: https://doi.org/10.1109/robot.2010.5509810
[research_votta_schettino_2009]: https://doi.org/10.2514/6.2009-6610
[research_votta_schettino_2013]: https://doi.org/10.1016/j.ast.2012.02.001
[research_vu_biezad_1994]: https://doi.org/10.2514/3.21342
[research_wachter_sachs_2006]: https://doi.org/10.1111/j.1934-6093.2006.tb00282.x
[research_waechter_tan_2005]: https://doi.org/10.2514/6.2005-3273
[research_wagner_dale_1985]: https://doi.org/10.21236/ada379715
[research_walberg_birge_2000]: https://doi.org/10.2514/6.2000-5342
[research_waldman_reinecke_1971]: https://doi.org/10.2514/3.6328
[research_walenczykowska_buzantowicz_2024]: https://doi.org/10.1109/techdefense63521.2024.10863732
[research_walker_sherk_2008]: https://doi.org/10.2514/6.2008-2539
[research_walker_sullivan_2003]: https://doi.org/10.2514/6.2003-6915
[research_wall_1983]: https://doi.org/10.1038/306220c0
[research_walmsley_mailhot_1983]: https://doi.org/10.1007/978-1-4684-7941-6_14
[research_wan_chen_2022]: https://doi.org/10.1109/isas55863.2022.9757294
[research_wan_wang_2012]: https://doi.org/10.2514/6.2012-5965
[research_wang_1963]: https://doi.org/10.21236/ad0402079
[research_wang_1965]: https://doi.org/10.2514/3.2829
[research_wang_1965_b]: https://doi.org/10.2514/3.3142
[research_wang_2019]: https://doi.org/10.1016/j.ast.2019.03.002
[research_wang_2019_b]: https://doi.org/10.2514/6.2019-0262
[research_wang_2022]: https://doi.org/10.1088/1742-6596/2383/1/012068
[research_wang_2023]: https://doi.org/10.1007/978-981-99-8867-9_21
[research_wang_an_2025]: https://doi.org/10.3390/aerospace12080747
[research_wang_bai_2021]: https://doi.org/10.1117/12.2601819
[research_wang_bair_2021]: https://doi.org/10.1001/jamapediatrics.2020.3871
[research_wang_cai_2016]: https://doi.org/10.2514/6.2016-1019
[research_wang_cai_2017]: https://doi.org/10.1016/j.cja.2017.05.002
[research_wang_cao_2017]: https://doi.org/10.1016/j.dsp.2017.05.010
[research_wang_cao_2022]: https://doi.org/10.1016/j.applthermaleng.2022.118856
[research_wang_cao_2025]: https://doi.org/10.1007/978-981-96-2236-8_38
[research_wang_chao_2019]: https://doi.org/10.1177/0954410019830811
[research_wang_chen_2018]: https://doi.org/10.1016/j.ast.2018.06.033
[research_wang_chen_2018_b]: https://doi.org/10.1109/access.2018.2809515
[research_wang_cheng_2025]: https://doi.org/10.1007/978-981-96-2260-3_43
[research_wang_cheng_2026]: https://doi.org/10.1016/j.ast.2026.112326
[research_wang_cui_2018]: https://doi.org/10.1109/gncc42960.2018.9018689
[research_wang_deng_2026]: https://doi.org/10.1088/2631-8695/ae32de
[research_wang_ding_2009]: https://doi.org/10.1007/s11431-009-0258-2
[research_wang_dong_2013]: https://doi.org/10.4028/www.scientific.net/amm.427-429.1424
[research_wang_feng_2017]: https://doi.org/10.23919/chicc.2017.8028295
[research_wang_feng_2022]: https://doi.org/10.23919/ccc55666.2022.9902115
[research_wang_gao_2013]: https://doi.org/10.4028/www.scientific.net/amr.756-759.4626
[research_wang_gong_2020]: https://doi.org/10.1177/1729881419891605
[research_wang_grant_2016]: https://doi.org/10.2514/6.2016-3241
[research_wang_grant_2017]: https://doi.org/10.2514/6.2017-0248
[research_wang_grant_2018]: https://doi.org/10.2514/1.a34102
[research_wang_grant_2018_b]: https://doi.org/10.2514/6.2018-0013
[research_wang_grant_2018_c]: https://doi.org/10.2514/6.2018-0013.c1
[research_wang_grant_2019]: https://doi.org/10.2514/6.2019-0667
[research_wang_han_2013]: https://doi.org/10.1016/j.proeng.2013.12.020
[research_wang_he_2025]: https://doi.org/10.1109/ieeeconf65522.2025.11137177
[research_wang_hou_2015]: https://doi.org/10.2514/6.2015-3672
[research_wang_hou_2018]: https://doi.org/10.1088/1757-899x/449/1/012006
[research_wang_hou_2019]: https://doi.org/10.1109/access.2018.2885597
[research_wang_hou_2019_b]: https://doi.org/10.1109/access.2019.2913989
[research_wang_li_2013]: https://doi.org/10.1142/s1758825113500269
[research_wang_li_2014]: https://doi.org/10.1109/cgncc.2014.7007445
[research_wang_li_2015]: https://doi.org/10.3390/ma8085018
[research_wang_li_2016]: https://doi.org/10.1007/s10443-016-9548-6
[research_wang_li_2016_b]: https://doi.org/10.1109/chicc.2016.7554235
[research_wang_li_2016_c]: https://doi.org/10.1109/radar.2016.8059267
[research_wang_li_2017]: https://doi.org/10.1109/ccdc.2017.7979050
[research_wang_li_2017_b]: https://doi.org/10.2514/6.2017-2335
[research_wang_li_2023]: https://doi.org/10.1007/978-981-99-8861-7_38
[research_wang_li_2024]: https://doi.org/10.1007/978-981-97-3340-8_50
[research_wang_li_2025]: https://doi.org/10.3390/sym17091430
[research_wang_li_2025_b]: https://doi.org/10.1109/cac67268.2025.11487377
[research_wang_li_2026]: https://doi.org/10.1007/978-981-95-6736-2_13
[research_wang_liang_2019]: https://doi.org/10.1016/j.ast.2019.04.017
[research_wang_lin_2016]: https://doi.org/10.2514/6.2016-3821
[research_wang_liu_2012]: https://doi.org/10.4028/www.scientific.net/amm.232.194
[research_wang_liu_2013]: https://doi.org/10.1360/132012-724
[research_wang_liu_2014]: https://doi.org/10.4028/www.scientific.net/amm.668-669.419
[research_wang_liu_2015]: https://doi.org/10.1109/chicc.2015.7259715
[research_wang_liu_2016]: https://doi.org/10.1109/cgncc.2016.7828993
[research_wang_liu_2018]: https://doi.org/10.1016/j.actaastro.2018.06.048
[research_wang_liu_2025]: https://doi.org/10.1016/j.actaastro.2025.07.070
[research_wang_liu_2025_b]: https://doi.org/10.1016/j.tsep.2025.103659
[research_wang_liu_2025_c]: https://doi.org/10.1108/aeat-03-2024-0061
[research_wang_liu_2026]: https://doi.org/10.1007/978-981-95-3013-7_4
[research_wang_liu_2026_b]: https://doi.org/10.1109/fasta70174.2026.11549484
[research_wang_luo_2022]: https://doi.org/10.3390/app122110734
[research_wang_ma_2024]: https://doi.org/10.1080/01457632.2024.2437893
[research_wang_ma_2025]: https://doi.org/10.1109/aaac66612.2025.11427723
[research_wang_meng_2014]: https://doi.org/10.1109/chicc.2014.6896747
[research_wang_mi_2024]: https://doi.org/10.1007/978-981-97-8658-9_34
[research_wang_ning_2011]: https://doi.org/10.1007/978-3-642-25992-0_43
[research_wang_pan_2013]: https://doi.org/10.4028/www.scientific.net/amm.380-384.576
[research_wang_pan_2024]: https://doi.org/10.1016/j.applthermaleng.2023.122324
[research_wang_peng_2018]: https://doi.org/10.3390/en11102605
[research_wang_qian_2023]: https://doi.org/10.1016/j.tsep.2023.101792
[research_wang_qu_2026]: https://doi.org/10.1016/j.dt.2025.10.009
[research_wang_ren_2011]: https://doi.org/10.1109/iceceng.2011.6057721
[research_wang_shih_1991]: https://doi.org/10.2514/6.1991-841
[research_wang_skulsky_1963]: https://doi.org/10.2514/3.1621
[research_wang_song_2015]: https://doi.org/10.5539/mas.v9n12p202
[research_wang_sun_2016]: https://doi.org/10.1109/cgncc.2016.7829107
[research_wang_sun_2023]: https://doi.org/10.1016/j.asr.2023.05.034
[research_wang_tang_2014]: https://doi.org/10.1007/s11432-014-5122-8
[research_wang_tang_2019]: https://doi.org/10.1109/access.2019.2909589
[research_wang_tang_2022]: https://doi.org/10.1109/access.2021.3137641
[research_wang_tang_2025]: https://doi.org/10.23919/ccc64809.2025.11179003
[research_wang_wang_2016]: https://doi.org/10.1016/j.actaastro.2016.06.022
[research_wang_wang_2019]: https://doi.org/10.1007/s42405-019-00217-x
[research_wang_wang_2019_b]: https://doi.org/10.5220/0007909800610069
[research_wang_wang_2024]: https://doi.org/10.1360/ssi-2024-0128
[research_wang_wang_2024_b]: https://doi.org/10.1016/j.actaastro.2024.01.002
[research_wang_wang_2025]: https://doi.org/10.23919/ecc65951.2025.11186845
[research_wang_wu_2014]: https://doi.org/10.1142/s1793962314500147
[research_wang_wu_2015]: https://doi.org/10.1007/s11071-015-2083-4
[research_wang_wu_2017]: https://doi.org/10.1016/j.ast.2017.03.005
[research_wang_wu_2019]: https://doi.org/10.1016/j.asr.2019.02.010
[research_wang_wu_2021]: https://doi.org/10.1007/978-981-15-8155-7_75
[research_wang_wu_2021_b]: https://doi.org/10.1155/2021/8889593
[research_wang_wu_2023]: https://doi.org/10.1007/978-981-19-6613-2_221
[research_wang_xia_2022]: https://doi.org/10.1109/oncon56984.2022.10126719
[research_wang_xiang_2019]: https://doi.org/10.1007/978-3-319-91017-8_113
[research_wang_xie_2011]: https://doi.org/10.2514/6.2011-2306
[research_wang_xie_2012]: https://doi.org/10.1115/imece2012-93052
[research_wang_xing_2015]: https://doi.org/10.1109/jsee.2015.00140
[research_wang_xiong_2014]: https://doi.org/10.1260/1748-3018.8.3.319
[research_wang_xu_2012]: https://doi.org/10.1109/isdea.2012.641
[research_wang_xu_2014]: https://doi.org/10.4028/www.scientific.net/amr.945-949.662
[research_wang_xu_2020]: https://doi.org/10.1360/sst-2020-0211
[research_wang_xu_2023]: https://doi.org/10.1109/taes.2022.3210153
[research_wang_xue_2025]: https://doi.org/10.1016/j.applthermaleng.2025.126704
[research_wang_yan_2013]: https://doi.org/10.4028/www.scientific.net/amm.427-429.81
[research_wang_yang_2012]: https://doi.org/10.1109/wcica.2012.6358266
[research_wang_yang_2022]: https://doi.org/10.1007/s42405-022-00506-y
[research_wang_yang_2025]: https://doi.org/10.1016/j.jfranklin.2024.107426
[research_wang_yao_2017]: https://doi.org/10.1155/2017/3498350
[research_wang_yun_2021]: https://doi.org/10.1109/ccdc52312.2021.9601514
[research_wang_zhang_2013]: https://doi.org/10.4028/www.scientific.net/amr.823.62
[research_wang_zhang_2017]: https://doi.org/10.1109/ccsse.2017.8087909
[research_wang_zhang_2018]: https://doi.org/10.2514/1.g003540
[research_wang_zhang_2021]: https://doi.org/10.2514/1.a34728
[research_wang_zhang_2022]: https://doi.org/10.1061/(asce)as.1943-5525.0001374
[research_wang_zhang_2023]: https://doi.org/10.1109/yac59482.2023.10401618
[research_wang_zhang_2026]: https://doi.org/10.2514/1.g009011
[research_wang_zhong_2016]: https://doi.org/10.1109/cgncc.2016.7828782
[research_wang_zhou_2016]: https://doi.org/10.1109/cgncc.2016.7828813
[research_wang_zhou_2017]: https://doi.org/10.2514/6.2017-1242
[research_wang_zhou_2024]: https://doi.org/10.1109/cac63892.2024.10865062
[research_wang_zhu_2026]: https://doi.org/10.1016/j.cja.2026.104153
[research_wang_zong_2013]: https://doi.org/10.1109/jsee.2013.00036
[research_wang_zong_2014]: https://doi.org/10.1016/j.isatra.2014.01.002
[research_wang_zou_2017]: https://doi.org/10.1177/1687814017744077
[research_wang_zuo_2026]: https://doi.org/10.2514/1.j065924
[research_wanlizhang_changhongwang_2010]: https://doi.org/10.1109/isscaa.2010.5633299
[research_ward_smart_2026]: https://doi.org/10.2514/6.2026-5107
[research_waszkowski_pisani_2025]: https://doi.org/10.2514/6.2025-99583
[research_watanabe_ishimoto_1996]: https://doi.org/10.2514/6.1996-4527
[research_watanabe_ishimoto_1997]: https://doi.org/10.2514/2.3259
[research_watanabe_ohya_2011]: https://doi.org/10.1109/cica.2011.5945752
[research_watanabe_suzuki_2016]: https://doi.org/10.1177/0954410016643979
[research_watts_2005]: https://doi.org/10.2514/6.2005-6375
[research_waverider_aerodynamics_1986]: https://doi.org/10.2514/5.9781600861871.0399.0414
[research_waverider_aircraft_2012]: https://doi.org/10.2514/5.9781600869228.0448.0510
[research_waverider_buoy_2022]: https://doi.org/10.1007/978-981-10-6946-8_300920
[research_way_sescu_2024]: https://doi.org/10.2514/6.2024-4107
[research_weaver_hunsaker_2025]: https://doi.org/10.2514/6.2025-0224
[research_webb_1999]: https://doi.org/10.21236/ada636796
[research_webb_2000]: https://doi.org/10.21236/ada380432
[research_webb_bettinger_2024]: https://doi.org/10.2514/6.2024-1915
[research_webb_lu_2016]: https://doi.org/10.2514/6.2016-0279
[research_wei_cui_2025]: https://doi.org/10.3390/aerospace12090773
[research_wei_dandan_2023]: https://doi.org/10.1049/rsn2.12487
[research_wei_hu_2019]: https://doi.org/10.23919/chicc.2019.8866177
[research_wei_huang_2015]: https://doi.org/10.1051/matecconf/20152203016
[research_wei_huang_2026]: https://doi.org/10.3390/aerospace13070600
[research_wei_kang_2025]: https://doi.org/10.1007/978-981-96-2248-1_16
[research_wei_li_2024]: https://doi.org/10.1016/j.asr.2024.10.035
[research_wei_li_2025]: https://doi.org/10.1088/1742-6596/3006/1/012043
[research_wei_liu_2018]: https://doi.org/10.1155/2018/8793908
[research_wei_shi_2024]: https://doi.org/10.3390/aerospace11030212
[research_wei_wang_2016]: https://doi.org/10.2316/p.2016.830-040
[research_weidner_1978]: https://doi.org/10.2514/3.58429
[research_weidner_1978_b]: https://doi.org/10.2514/6.1978-149
[research_weidner_1980]: https://doi.org/10.2514/6.1980-111
[research_weidong_xianlin_2015]: https://doi.org/10.1109/chicc.2015.7260001
[research_weifeng_chenglin_2015]: https://doi.org/10.1109/chicc.2015.7259963
[research_weijie_hao_2016]: https://doi.org/10.1109/chicc.2016.7553885
[research_weiland_2014]: https://doi.org/10.1007/978-3-642-54168-1_7
[research_weiland_2014_b]: https://doi.org/10.1007/978-3-642-54168-1_6
[research_weilmuenster_gnoffo_1995]: https://doi.org/10.2514/6.1995-1850
[research_weilmuenster_gnoffo_1996]: https://doi.org/10.2514/3.26786
[research_weilmuenster_gnoffo_1996_b]: https://doi.org/10.2514/6.1996-609
[research_weilmuenster_gnoffo_1997]: https://doi.org/10.2514/2.3282
[research_weiwei_leping_2013]: https://doi.org/10.1109/ccdc.2013.6560984
[research_weiwei_runde_2022]: https://doi.org/10.1109/cac57257.2022.10055554
[research_wen_tao_2017]: https://doi.org/10.1109/ascc.2017.8287334
[research_wen_wu_2014]: https://doi.org/10.1109/chicc.2014.6895555
[research_wenbiao_dong_2014]: https://doi.org/10.1109/cgncc.2014.7007458
[research_wenbo_qiang_2012]: https://doi.org/10.1016/j.proeng.2012.01.228
[research_wenfeng_peng_2017]: https://doi.org/10.23919/chicc.2017.8027899
[research_wenkai_hou_2017]: https://doi.org/10.2514/6.2017-2156
[research_wenkai_hou_2017_b]: https://doi.org/10.2514/6.2017-4004
[research_wenkai_zhongxi_2017]: https://doi.org/10.23919/chicc.2017.8027732
[research_west_2012]: https://doi.org/10.21236/ada568300
[research_west_brandis_2018]: https://doi.org/10.2514/6.2018-3767
[research_west_brandis_2018_b]: https://doi.org/10.2514/6.2018-3767.c1
[research_westin_olsson_2003]: https://doi.org/10.1117/12.487079
[research_weston_cesnik_2024]: https://doi.org/10.2514/6.2024-1045
[research_wexler_idan_2026]: https://doi.org/10.2514/6.2026-5048
[research_white_1993]: https://doi.org/10.2514/6.1993-971
[research_white_1996]: https://doi.org/10.2514/6.1996-4542
[research_white_rhie_1987]: https://doi.org/10.2514/6.1987-1895
[research_whitfield_griffith_1963]: https://doi.org/10.2514/6.1963-434
[research_whitfield_griffith_1964]: https://doi.org/10.2514/3.2658
[research_wibben_furfaro_2016]: https://doi.org/10.2514/1.g001411
[research_wiese_annaswamy_2013]: https://doi.org/10.2514/6.2013-4514
[research_wiese_annaswamy_2016]: https://doi.org/10.2514/6.2016-1379
[research_wilder_prabhu_2019]: https://doi.org/10.2514/6.2019-3009
[research_wilke_johnson_2000]: https://doi.org/10.21236/ada476252
[research_willard_2022]: https://doi.org/10.15354/si.22.re063
[research_williams_2019]: https://doi.org/10.1080/01402390.2019.1627521
[research_williams_2021]: https://doi.org/10.4324/9781003179917-8
[research_williams_bartkowicz_2024]: https://doi.org/10.2514/6.2024-0562
[research_williams_bhattacharjee_2025]: https://doi.org/10.2514/6.2025-0264
[research_williamson_pascoe_2026]: https://doi.org/10.2514/6.2026-5003
[research_willis_bahlman_2009]: https://doi.org/10.2514/6.2009-3764
[research_willis_bahlman_2011]: https://doi.org/10.2514/1.j051070
[research_wilsdorf_schmitz_1962]: https://doi.org/10.1063/1.1728823
[research_wilson_taylor_1983]: https://doi.org/10.1109/oceans.1983.1151998
[research_wilsonheid_griffiths_2022]: https://doi.org/10.13182/nets22-38752
[research_windhorst_ardema_1997]: https://doi.org/10.2514/6.1997-3535
[research_wing_gangireddy_2012]: https://doi.org/10.21236/ada565619
[research_wingrove_1964]: https://doi.org/10.2514/6.1964-1303
[research_wingrove_1966]: https://doi.org/10.1007/978-1-4899-6411-3_35
[research_winn_1993]: https://doi.org/10.1007/978-94-011-1743-2_22
[research_winter_stackpoole_2014]: https://doi.org/10.2514/6.2014-1151
[research_wiseman_lopez_2026]: https://doi.org/10.2514/6.2026-112080
[research_wittliff_1983]: https://doi.org/10.2514/6.1983-1535
[research_wittliff_oconnor_1992]: https://doi.org/10.2514/6.1992-3906
[research_wittliff_wilson_1961]: https://doi.org/10.21236/ad0266413
[research_witzeman_2003]: https://doi.org/10.21236/ada419720
[research_wood_alter_2008]: https://doi.org/10.2514/6.2008-6559
[research_wood_gnoffo_1996]: https://doi.org/10.2514/6.1996-316
[research_wortman_1970]: https://doi.org/10.2514/6.1970-809
[research_wright_2015]: https://doi.org/10.1080/08929882.2015.1088734
[research_wu_2018]: https://doi.org/10.12783/dtetr/pmsms2018/24866
[research_wu_chen_2011]: https://doi.org/10.1007/978-3-642-25899-2_85
[research_wu_deng_2021]: https://doi.org/10.1016/j.ast.2021.107046
[research_wu_guan_2018]: https://doi.org/10.1109/gncc42960.2018.9018640
[research_wu_guo_2018]: https://doi.org/10.1155/2018/2198423
[research_wu_huang_2009]: https://doi.org/10.1109/icect.2009.36
[research_wu_huang_2009_b]: https://doi.org/10.1109/car.2009.63
[research_wu_jiang_2015]: https://doi.org/10.1051/matecconf/20153102004
[research_wu_li_2009]: https://doi.org/10.1007/978-3-642-01513-7_27
[research_wu_li_2014]: https://doi.org/10.1109/chicc.2014.6896303
[research_wu_li_2023]: https://doi.org/10.1109/ecnct59757.2023.10281034
[research_wu_liu_2015]: https://doi.org/10.1109/cac.2015.7382480
[research_wu_meng_2016]: https://doi.org/10.1016/j.ast.2016.04.018
[research_wu_meng_2018]: https://doi.org/10.1016/j.ast.2018.04.036
[research_wu_tang_2012]: https://doi.org/10.4028/www.scientific.net/amr.591-593.2624
[research_wu_tang_2018]: https://doi.org/10.1007/978-3-319-89988-6_19
[research_wu_tian_2020]: https://doi.org/10.23919/ccc50068.2020.9188640
[research_wu_wang_2012]: https://doi.org/10.4028/www.scientific.net/amm.220-223.973
[research_wu_wang_2015]: https://doi.org/10.1155/2015/506906
[research_wu_wang_2022]: https://doi.org/10.1007/978-981-16-9492-9_248
[research_wu_wang_2023]: https://doi.org/10.1016/j.isatra.2023.04.004
[research_wu_xiao_2009]: https://doi.org/10.5539/mas.v3n2p117
[research_wu_xiong_2020]: https://doi.org/10.23919/ccc50068.2020.9189569
[research_wu_yan_2018]: https://doi.org/10.1155/2018/8135274
[research_wu_yao_2018]: https://doi.org/10.1016/j.actaastro.2017.10.041
[research_wu_yu_2018]: https://doi.org/10.5220/0006969302880293
[research_wu_yuan_2025]: https://doi.org/10.3934/jimo.2025010
[research_wu_zhang_2021]: https://doi.org/10.1155/2021/6673818
[research_wu_zhao_2018]: https://doi.org/10.1088/1742-6596/1053/1/012055
[research_wunderlin_martin_2018]: https://doi.org/10.2514/6.2018-4462
[research_wurster_1980]: https://doi.org/10.2514/6.1980-363
[research_wurster_1981]: https://doi.org/10.2514/6.1981-1090
[research_wuxing_chunwang_2015]: https://doi.org/10.1109/chicc.2015.7260440
[research_wuyanan_zhangran_2016]: https://doi.org/10.1109/cgncc.2016.7828799
[research_xi_meng_2019]: https://doi.org/10.1016/j.ast.2018.12.032
[research_xia_bu_2023]: https://doi.org/10.1002/oca.3058
[research_xia_chen_2015]: https://doi.org/10.1016/j.proeng.2015.11.214
[research_xia_gao_2025]: https://doi.org/10.1109/cac67268.2025.11487314
[research_xia_jing_2024]: https://doi.org/10.1109/icpics62053.2024.10796544
[research_xiang_chen_2022]: https://doi.org/10.1016/j.ast.2022.107327
[research_xiang_deng_2023]: https://doi.org/10.1007/978-981-19-6613-2_392
[research_xiang_kun_2017]: https://doi.org/10.1063/1.4977357
[research_xiang_zhang_2025]: https://doi.org/10.25144/24744
[research_xianhong_yuan_2017]: https://doi.org/10.2514/6.2017-2110
[research_xiao_2009]: https://doi.org/10.2514/6.2009-7435
[research_xiao_he_1991]: https://doi.org/10.2514/6.1991-2306
[research_xiao_li_2018]: https://doi.org/10.2514/1.j055915
[research_xiao_liu_2006]: https://doi.org/10.2514/6.2006-8090
[research_xiao_ou_2020]: https://doi.org/10.1051/matecconf/202031604006
[research_xiao_shen_2016]: https://doi.org/10.1109/chicc.2016.7553323
[research_xiao_tan_2014]: https://doi.org/10.4028/www.scientific.net/amr.981.730
[research_xiao_xie_2025]: https://doi.org/10.1109/acait67930.2025.11522005
[research_xiaoqing_zhongxi_2010]: https://doi.org/10.2514/6.2010-7931
[research_xiaoqing_zhongxi_2011]: https://doi.org/10.1017/s0001924000005844
[research_xiaotian_wei_2022]: https://doi.org/10.1109/ccdc55256.2022.10033608
[research_xiaowei_jia_2023]: https://doi.org/10.1007/978-981-19-6613-2_322
[research_xiaoxuan_jinglong_2018]: https://doi.org/10.1177/0954410018808634
[research_xie_dong_2020]: https://doi.org/10.1016/j.ast.2020.106170
[research_xie_lin_2021]: https://doi.org/10.1109/cac53003.2021.9728449
[research_xie_liu_2011]: https://doi.org/10.1109/rast.2011.5966833
[research_xie_pan_2015]: https://doi.org/10.2991/icmse-15.2015.2
[research_xie_peng_2023]: https://doi.org/10.1109/cac59555.2023.10450773
[research_xie_wang_2012]: https://doi.org/10.1166/jctn.2012.2022
[research_xie_wang_2012_b]: https://doi.org/10.4028/www.scientific.net/amr.459.505
[research_xie_wang_2012_c]: https://doi.org/10.1109/wcica.2012.6357859
[research_xie_wang_2013]: https://doi.org/10.1016/j.applthermaleng.2013.06.002
[research_xie_wang_2013_b]: https://doi.org/10.14429/dsj.63.2360
[research_xie_wei_2024]: https://doi.org/10.3390/aerospace11060499
[research_xie_yang_2017]: https://doi.org/10.2514/6.2017-2347
[research_xie_zhang_2023]: https://doi.org/10.1109/cac59555.2023.10450328
[research_xie_zhang_2025]: https://doi.org/10.1007/978-981-96-2252-8_52
[research_xie_zhao_2024]: https://doi.org/10.1134/s0015462823603285
[research_xin_xu_2026]: https://doi.org/10.1016/j.applthermaleng.2026.130208
[research_xingling_honglun_2014]: https://doi.org/10.1016/j.isatra.2014.09.021
[research_xinguo_ting_2024]: https://doi.org/10.1109/ccdc62350.2024.10587450
[research_xinwang_dongzhufeng_2008]: https://doi.org/10.1109/isscaa.2008.4776354
[research_xinwang_shijiesun_2010]: https://doi.org/10.1109/ccdc.2010.5498090
[research_xinyu_kelong_2025]: https://doi.org/10.1016/j.ifacol.2025.11.202
[research_xiong_chen_2014]: https://doi.org/10.1109/cgncc.2014.7007438
[research_xiong_fan_2021]: https://doi.org/10.1016/j.ast.2021.106979
[research_xiong_lele_2003]: https://doi.org/10.2514/6.2003-1259
[research_xiong_lele_2004]: https://doi.org/10.21236/ada422883
[research_xiongluo_zengqisun_2008]: https://doi.org/10.1109/wcica.2008.4593311
[research_xu_2015]: https://doi.org/10.1007/s11071-015-1958-8
[research_xu_2022]: https://doi.org/10.1109/itaic54216.2022.9836763
[research_xu_2023]: https://doi.org/10.1007/978-981-19-6613-2_595
[research_xu_cai_2011]: https://doi.org/10.1109/ist.2011.5962219
[research_xu_cai_2023]: https://doi.org/10.3390/app13084987
[research_xu_chen_2012]: https://doi.org/10.1007/s11431-011-4727-z
[research_xu_cheng_2018]: https://doi.org/10.1111/jace.15565
[research_xu_cui_2015]: https://doi.org/10.1109/cict.2015.132
[research_xu_dong_2022]: https://doi.org/10.1109/cac57257.2022.10055577
[research_xu_fang_2021]: https://doi.org/10.1109/icmeas54189.2021.00034
[research_xu_fang_2022]: https://doi.org/10.1007/978-981-16-6640-7_1
[research_xu_fang_2022_b]: https://doi.org/10.1145/3547578.3547593
[research_xu_guan_2025]: https://doi.org/10.3390/aerospace12050438
[research_xu_huang_2018]: https://doi.org/10.12783/dtetr/ecame2017/18365
[research_xu_lan_2018]: https://doi.org/10.1109/icmic.2018.8529840
[research_xu_li_2012]: https://doi.org/10.4028/www.scientific.net/amr.466-467.1095
[research_xu_liao_2025]: https://doi.org/10.1007/s11071-025-10900-2
[research_xu_liu_2011]: https://doi.org/10.1109/rast.2011.5966837
[research_xu_ma_2026]: https://doi.org/10.1007/978-981-95-3034-2_36
[research_xu_mirmirani_2004]: https://doi.org/10.2514/1.12596
[research_xu_pan_2026]: https://doi.org/10.1016/j.cja.2025.103840
[research_xu_peng_2025]: https://doi.org/10.1007/978-3-032-09862-7_3
[research_xu_shi_2013]: https://doi.org/10.1007/s11071-013-0908-6
[research_xu_shi_2019]: https://doi.org/10.1109/tcyb.2018.2794972
[research_xu_shou_2023]: https://doi.org/10.1109/tnnls.2022.3151198
[research_xu_sun_2012]: https://doi.org/10.1049/iet-cta.2011.0026
[research_xu_wang_2012]: https://doi.org/10.1007/s11071-012-0451-x
[research_xu_wang_2013]: https://doi.org/10.1016/j.neucom.2012.12.028
[research_xu_wang_2017]: https://doi.org/10.1109/tie.2017.2703678
[research_xu_wang_2022]: https://doi.org/10.1109/iccsi55536.2022.9970639
[research_xu_wu_2015]: https://doi.org/10.1117/12.2216033
[research_xu_xu_2013]: https://doi.org/10.1007/s11433-013-5078-5
[research_xu_yao_2011]: https://doi.org/10.1109/icbbe.2011.5781576
[research_xu_yu_2017]: https://doi.org/10.2514/6.2017-2112
[research_xu_zhang_2015]: https://doi.org/10.1016/j.neucom.2014.11.059
[research_xu_zhang_2020]: https://doi.org/10.1117/12.2563810
[research_xu_zhou_2021]: https://doi.org/10.1117/12.2586769
[research_xu_zhu_2011]: https://doi.org/10.1109/icecc.2011.6067823
[research_xu_zhu_2023]: https://doi.org/10.1007/978-981-19-6613-2_678
[research_xudongliu_lincheng_2016]: https://doi.org/10.1109/cgncc.2016.7828785
[research_xue_guodong_2018]: https://doi.org/10.1109/gncc42960.2018.9018943
[research_xue_haibin_2017]: https://doi.org/10.1108/aeat-01-2015-0007
[research_xue_huang_2023]: https://doi.org/10.1049/rsn2.12400
[research_xue_li_2026]: https://doi.org/10.1016/j.applthermaleng.2026.130619
[research_xue_lu_2010]: https://doi.org/10.2514/1.49557
[research_xue_wang_2017]: https://doi.org/10.2514/6.2017-2309
[research_xue_wang_2021]: https://doi.org/10.1017/jfm.2021.421
[research_xue_wang_2025]: https://doi.org/10.1016/j.energy.2025.138363
[research_xue_xin_2023]: https://doi.org/10.1007/978-981-19-6613-2_691
[research_xuebao_xiaokui_2023]: https://doi.org/10.1007/978-3-031-42515-8_83
[research_xuguo_yongtao_2017]: https://doi.org/10.1088/1757-899x/234/1/012011
[research_xumingliang_liuluhua_2010]: https://doi.org/10.1109/isscaa.2010.5633205
[research_xuzhao_jialing_2012]: https://doi.org/10.2514/6.2012-5810
[research_yadhukulakrishnan_karumuri_2013]: https://doi.org/10.1016/j.ceramint.2013.01.101
[research_yakubayev_gschwend_2026]: https://doi.org/10.2514/6.2026-1095
[research_yamada_2022]: https://doi.org/10.2514/6.2022-3801
[research_yamada_2022_b]: https://doi.org/10.2514/6.2022-3801.c1
[research_yamamoto_arakawa_1989]: https://doi.org/10.2514/6.1989-1699
[research_yamamoto_wada_1995]: https://doi.org/10.2514/6.1995-1770
[research_yamasaki_balakrishnan_2012]: https://doi.org/10.1109/acc.2012.6315051
[research_yan_2014]: https://doi.org/10.12720/joace.2.3.294-301
[research_yan_fan_2017]: https://doi.org/10.23919/chicc.2017.8027935
[research_yan_hexi_2025]: https://doi.org/10.1007/978-981-96-2232-0_23
[research_yan_lyu_2014]: https://doi.org/10.1016/j.cja.2014.02.019
[research_yan_pan_2008]: https://doi.org/10.2514/6.2008-176
[research_yan_tan_2017]: https://doi.org/10.1016/j.actaastro.2016.12.027
[research_yan_wang_2012]: https://doi.org/10.2514/6.2012-5897
[research_yan_wang_2023]: https://doi.org/10.1051/jnwpu/20234150850
[research_yan_wang_2024]: https://doi.org/10.1007/978-981-97-1107-9_48
[research_yan_zhang_2023]: https://doi.org/10.1007/978-3-031-42987-3_7
[research_yanbinbin_lucunkan_2009]: https://doi.org/10.1109/iciea.2009.5138209
[research_yang_2025]: https://doi.org/10.5220/0014376100004918
[research_yang_chao_2023]: https://doi.org/10.1007/978-981-99-0479-2_232
[research_yang_chen_2016]: https://doi.org/10.1155/2016/3527460
[research_yang_choi_2024]: https://doi.org/10.1371/journal.pone.0298113
[research_yang_duan_2014]: https://doi.org/10.2514/6.2014-1393
[research_yang_fang_2023]: https://doi.org/10.1007/978-981-19-6613-2_458
[research_yang_hu_2018]: https://doi.org/10.1109/cac.2018.8623766
[research_yang_ji_2022]: https://doi.org/10.1088/1742-6596/2235/1/012015
[research_yang_kong_2014]: https://doi.org/10.1109/cgncc.2014.7007413
[research_yang_li_2023]: https://doi.org/10.3390/pr11010263
[research_yang_liang_2024]: https://doi.org/10.1016/j.ast.2024.109639
[research_yang_lin_2017]: https://doi.org/10.23919/chicc.2017.8028327
[research_yang_liu_2017]: https://doi.org/10.1016/j.actaastro.2016.11.043
[research_yang_liu_2025]: https://doi.org/10.1109/taes.2025.3597279
[research_yang_lombard_1987]: https://doi.org/10.2514/6.1987-1896
[research_yang_lv_2019]: https://doi.org/10.1007/978-981-32-9698-5_19
[research_yang_meng_2012]: https://doi.org/10.1007/978-3-642-34390-2_26
[research_yang_qi_2016]: https://doi.org/10.1109/chicc.2016.7554207
[research_yang_song_2025]: https://doi.org/10.1016/j.ifacol.2025.11.346
[research_yang_sun_2011]: https://doi.org/10.4028/www.scientific.net/amr.383-390.7375
[research_yang_tian_2026]: https://doi.org/10.3390/aerospace13060498
[research_yang_tian_2026_b]: https://doi.org/10.1038/s41598-026-48203-0
[research_yang_wang_2012]: https://doi.org/10.4028/www.scientific.net/amm.236-237.378
[research_yang_wang_2015]: https://doi.org/10.4028/www.scientific.net/amm.734.482
[research_yang_wang_2021]: https://doi.org/10.23919/ccc52363.2021.9549492
[research_yang_wang_2022]: https://doi.org/10.1007/978-981-16-9492-9_249
[research_yang_wang_2023]: https://doi.org/10.1109/asemd59061.2023.10369201
[research_yang_yang_2008]: https://doi.org/10.1007/s10483-008-0107-1
[research_yang_yang_2025]: https://doi.org/10.3233/atde241397
[research_yang_yu_2014]: https://doi.org/10.4028/www.scientific.net/amm.716-717.724
[research_yang_yu_2017]: https://doi.org/10.1177/1729881417703567
[research_yang_yuan_2013]: https://doi.org/10.1007/978-3-642-38524-7_18
[research_yang_zhang_2024]: https://doi.org/10.1364/ao.535256
[research_yang_zheng_2017]: https://doi.org/10.1109/iccais.2017.8217600
[research_yang_zhu_2017]: https://doi.org/10.2514/6.2017-2139
[research_yanghong_zhangyasheng_2016]: https://doi.org/10.3788/co.20160905.0596
[research_yankui_dongjun_2005]: https://doi.org/10.2514/6.2005-6040
[research_yankui_shuifeng_2007]: https://doi.org/10.2514/1.22669
[research_yanli_dongyang_2016]: https://doi.org/10.1109/ccdc.2016.7531399
[research_yanlidu_qingxianwu_2008]: https://doi.org/10.1109/isscaa.2008.4776353
[research_yao_cui_2017]: https://doi.org/10.2514/6.2017-2315
[research_yao_hu_2023]: https://doi.org/10.5220/0012150900003562
[research_yao_liang_2025]: https://doi.org/10.1007/s43684-025-00115-y
[research_yao_wang_2013]: https://doi.org/10.1007/978-3-319-01273-5_73
[research_yao_wang_2013_b]: https://doi.org/10.1504/ijcat.2013.052796
[research_yao_wang_2023]: https://doi.org/10.1016/j.ijthermalsci.2022.107967
[research_yao_xia_2023]: https://doi.org/10.3390/aerospace10090795
[research_yao_xia_2024]: https://doi.org/10.3390/aerospace11080680
[research_yaosheng_2018]: https://doi.org/10.1109/icomssc45026.2018.8941700
[research_yassin_ahmed_2025]: https://doi.org/10.1088/1742-6596/3070/1/012006
[research_yates_1967]: https://doi.org/10.1007/978-1-4757-0489-1_14
[research_yatsukhno_2017]: https://doi.org/10.1088/1742-6596/815/1/012022
[research_yatsukhno_2021]: https://doi.org/10.33257/phchgd.22.6.975
[research_ye_2015]: https://doi.org/10.1016/b978-0-12-800001-4.00151-4
[research_ye_chaofang_2017]: https://doi.org/10.1109/ccdc.2017.7978401
[research_ye_guan_2025]: https://doi.org/10.23919/ccc64809.2025.11179028
[research_ye_huque_2000]: https://doi.org/10.2514/6.2000-3600
[research_ye_jiang_2020]: https://doi.org/10.1016/j.jfranklin.2020.06.014
[research_ye_liu_2022]: https://doi.org/10.1109/cyber55403.2022.9907718
[research_ye_tu_2022]: https://doi.org/10.1109/icfeict57213.2022.00012
[research_ye_zhang_2016]: https://doi.org/10.1109/ibcast.2016.7429922
[research_ye_zhao_2024]: https://doi.org/10.1016/j.ijheatmasstransfer.2023.125152
[research_ye_zong_2017]: https://doi.org/10.1016/j.isatra.2017.07.019
[research_yee_koo_2021]: https://doi.org/10.2514/6.2021-1586
[research_yee_koo_2021_b]: https://doi.org/10.2514/6.2021-1586.c1
[research_yen_1986]: https://doi.org/10.1063/1.865958
[research_yeo_sng_1980]: https://doi.org/10.2514/3.56012
[research_yi_li_2021]: https://doi.org/10.1109/cac53003.2021.9728169
[research_yihanli_haiyanghu_2020]: https://doi.org/10.3788/irla202049.0404002
[research_yin_he_2025]: https://doi.org/10.1016/j.asr.2025.08.015
[research_yin_qin_2017]: https://doi.org/10.2514/6.2017-2304
[research_yin_yu_2026]: https://doi.org/10.1016/j.oceaneng.2025.124075
[research_ying_wang_2018]: https://doi.org/10.1177/1056789518793492
[research_yiyinwei_yaochen_2016]: https://doi.org/10.1109/cgncc.2016.7828747
[research_yizhenmeng_binjiang_2016]: https://doi.org/10.1109/cgncc.2016.7829087
[research_yong_li_2017]: https://doi.org/10.2514/6.2017-2109
[research_yongfengxie_shuotang_2010]: https://doi.org/10.1109/iccda.2010.5540835
[research_yoon_ahn_2016]: https://doi.org/10.1061/(asce)as.1943-5525.0000567
[research_yoon_rasmussen_1996]: https://doi.org/10.1007/bf02942643
[research_yoon_suzuki_2024]: https://doi.org/10.1007/978-981-97-3998-1_130
[research_york_pastrick_1976]: https://doi.org/10.2514/6.1976-1916
[research_yost_choi_2019]: https://doi.org/10.2514/6.2019-3841
[research_you_liang_2009]: https://doi.org/10.1007/s11431-009-0125-1
[research_you_liang_2009_b]: https://doi.org/10.2514/6.2009-4215
[research_you_liang_2009_c]: https://doi.org/10.2514/6.2009-4214
[research_you_liang_2009_d]: https://doi.org/10.2514/6.2009-31
[research_you_zhu_2009]: https://doi.org/10.2514/6.2009-7421
[research_young_1966]: https://doi.org/10.1038/2091163b0
[research_young_1969]: https://doi.org/10.1002/j.2161-4296.1969.tb01655.x
[research_young_reda_1972]: https://doi.org/10.2514/3.61815
[research_youssef_chowdhry_2003]: https://doi.org/10.2514/6.2003-5498
[research_youssef_chowdhry_2004]: https://doi.org/10.2514/6.2004-5167
[research_youssef_reiman_2008]: https://doi.org/10.2514/6.2008-7466
[research_youssef_reiman_2009]: https://doi.org/10.2514/6.2009-6185
[research_yu_ao_2021]: https://doi.org/10.1109/icceic54227.2021.00034
[research_yu_chen_2011]: https://doi.org/10.2514/6.2011-6714
[research_yu_chen_2016]: https://doi.org/10.1016/j.isatra.2016.09.002
[research_yu_chen_2026]: https://doi.org/10.1016/j.asr.2025.10.046
[research_yu_guo_2025]: https://doi.org/10.1016/j.ijthermalsci.2025.109703
[research_yu_hao_2025]: https://doi.org/10.1016/j.ast.2025.110339
[research_yu_huang_2015]: https://doi.org/10.2514/6.2015-3612
[research_yu_jiang_2020]: https://doi.org/10.1016/j.ast.2020.106244
[research_yu_li_2025]: https://doi.org/10.1007/978-981-96-2264-1_47
[research_yu_ni_2022]: https://doi.org/10.1016/j.infrared.2022.104020
[research_yu_qiu_2022]: https://doi.org/10.1063/5.0131460
[research_yu_tan_2019]: https://doi.org/10.1049/iet-rsn.2018.5192
[research_yu_wang_2017]: https://doi.org/10.1109/robio.2017.8324831
[research_yu_wang_2019]: https://doi.org/10.1016/j.enconman.2019.111827
[research_yu_wang_2019_b]: https://doi.org/10.1016/j.ast.2019.02.024
[research_yu_wang_2022]: https://doi.org/10.3390/app12157861
[research_yu_wang_2025]: https://doi.org/10.1007/s12567-025-00672-1
[research_yu_wang_2026]: https://doi.org/10.1016/j.ast.2026.112132
[research_yu_xu_2015]: https://doi.org/10.2514/6.2015-1754
[research_yu_zhang_2014]: https://doi.org/10.1109/chicc.2014.6895661
[research_yu_zhao_2016]: https://doi.org/10.2514/6.2016-1373
[research_yu_zhong_2013]: https://doi.org/10.2514/6.2013-2130
[research_yu_zhong_2014]: https://doi.org/10.2514/6.2014-2656
[research_yuan_gao_2026]: https://doi.org/10.3390/aerospace13080705
[research_yuanjie_chunqiao_2023]: https://doi.org/10.1007/978-981-99-0479-2_45
[research_yuhangyun_shengjingtang_2016]: https://doi.org/10.1109/cgncc.2016.7828949
[research_yujie_yanhua_2025]: https://doi.org/10.1007/978-981-96-2228-3_26
[research_yuli_naigangcui_2008]: https://doi.org/10.1109/isscaa.2008.4776361
[research_yulian_bin_2014]: https://doi.org/10.1109/ccdc.2014.6852297
[research_yumusak_eyi_2013]: https://doi.org/10.2514/6.2013-2693
[research_zadonsky_kosykh_2013]: https://doi.org/10.1615/tsagiscij.2013007838
[research_zaehringer_heller_2003]: https://doi.org/10.2514/6.2003-7080
[research_zamora_nygren_2014]: https://doi.org/10.1016/j.ceramint.2014.03.130
[research_zamora_ortiz_2012]: https://doi.org/10.1016/j.jeurceramsoc.2012.02.023
[research_zampa_difabbio_2025]: https://doi.org/10.23919/eumc65286.2025.11235288
[research_zapatasolvas_jayaseelan_2015]: https://doi.org/10.1179/1743676115y.0000000012
[research_zemlyanskii_1966]: https://doi.org/10.1007/bf01022285
[research_zeng_fang_2008]: https://doi.org/10.4028/0-87849-473-1.1785
[research_zeng_gao_2019]: https://doi.org/10.1109/icaica.2019.8873439
[research_zeng_zhuang_2021]: https://doi.org/10.1109/icus52573.2021.9641452
[research_zewge_bang_2022]: https://doi.org/10.23919/iccas55662.2022.10003874
[research_zhai_li_2026]: https://doi.org/10.1016/j.actaastro.2026.05.011
[research_zhai_qi_2016]: https://doi.org/10.1109/chicc.2016.7554394
[research_zhai_qi_2019]: https://doi.org/10.1016/j.isatra.2019.01.005
[research_zhai_yang_2018]: https://doi.org/10.23919/chicc.2018.8483797
[research_zhai_yang_2020]: https://doi.org/10.1016/j.jfranklin.2020.03.002
[research_zhai_zhang_2020]: https://doi.org/10.1142/s0217979220400743
[research_zhai_zhou_2009]: https://doi.org/10.2514/6.2009-1607
[research_zhan_liang_2017]: https://doi.org/10.23919/icif.2017.8009775
[research_zhang_2011]: https://doi.org/10.1117/1.3617453
[research_zhang_2015]: https://doi.org/10.2514/6.2015-3500
[research_zhang_2015_b]: https://doi.org/10.2514/6.2015-3647
[research_zhang_2017]: https://doi.org/10.1109/cac.2017.8242972
[research_zhang_2020]: https://doi.org/10.1007/978-981-15-0727-4_9
[research_zhang_2020_b]: https://doi.org/10.1007/978-981-15-0727-4_7
[research_zhang_2026]: https://doi.org/10.61784/wjer3082
[research_zhang_bai_2021]: https://doi.org/10.1117/12.2586892
[research_zhang_bai_2023]: https://doi.org/10.1007/978-981-19-6613-2_137
[research_zhang_bian_2025]: https://doi.org/10.1117/12.3082918
[research_zhang_cao_2019]: https://doi.org/10.1109/access.2019.2936232
[research_zhang_chen_2011]: https://doi.org/10.4028/www.scientific.net/amm.110-116.5223
[research_zhang_chen_2011_b]: https://doi.org/10.2514/6.2011-2231
[research_zhang_chen_2018]: https://doi.org/10.1016/j.isatra.2018.08.012
[research_zhang_chen_2021]: https://doi.org/10.3390/aerospace9010022
[research_zhang_chen_2023]: https://doi.org/10.1007/978-981-19-6613-2_436
[research_zhang_chen_2026]: https://doi.org/10.1007/s42401-026-00511-z
[research_zhang_ding_2023]: https://doi.org/10.1007/978-3-031-42515-8_66
[research_zhang_ding_2023_b]: https://doi.org/10.1177/00202940231154856
[research_zhang_du_2017]: https://doi.org/10.1109/iecon.2017.8217148
[research_zhang_du_2021]: https://doi.org/10.1007/978-981-15-8155-7_199
[research_zhang_fan_2012]: https://doi.org/10.4028/www.scientific.net/amr.562-564.1682
[research_zhang_feng_2019]: https://doi.org/10.1109/access.2019.2945082
[research_zhang_feng_2019_b]: https://doi.org/10.1109/access.2019.2915516
[research_zhang_feng_2021]: https://doi.org/10.1007/978-981-15-8155-7_210
[research_zhang_fu_2017]: https://doi.org/10.23919/chicc.2017.8027650
[research_zhang_fu_2023]: https://doi.org/10.1109/cac59555.2023.10450781
[research_zhang_gao_2018]: https://doi.org/10.1117/1.jei.27.2.023023
[research_zhang_guo_2025]: https://doi.org/10.1061/jaeeez.aseng-6129
[research_zhang_han_2024]: https://doi.org/10.1109/eei63073.2024.10696792
[research_zhang_han_2025]: https://doi.org/10.1007/978-981-96-7352-0_11
[research_zhang_han_2025_b]: https://doi.org/10.1002/asjc.3839
[research_zhang_he_2010]: https://doi.org/10.2514/6.2010-9189
[research_zhang_he_2017]: https://doi.org/10.23919/chicc.2017.8028140
[research_zhang_hu_2011]: https://doi.org/10.1007/s11432-011-4187-x
[research_zhang_hu_2026]: https://doi.org/10.2514/1.j066725
[research_zhang_huang_2014]: https://doi.org/10.4028/www.scientific.net/amm.490-491.368
[research_zhang_huang_2022]: https://doi.org/10.1109/yac57282.2022.10023597
[research_zhang_ji_2020]: https://doi.org/10.1109/itaic49862.2020.9338796
[research_zhang_jin_2022]: https://doi.org/10.1109/csrswtc56224.2022.10098326
[research_zhang_ju_2023]: https://doi.org/10.1364/oe.496783
[research_zhang_li_2017]: https://doi.org/10.1016/j.ast.2017.08.017
[research_zhang_li_2024]: https://doi.org/10.3390/drones8090460
[research_zhang_li_2025]: https://doi.org/10.1109/taes.2025.3539639
[research_zhang_li_2025_b]: https://doi.org/10.1016/j.ifacol.2025.11.497
[research_zhang_li_2026]: https://doi.org/10.3390/aerospace13020199
[research_zhang_liao_2019]: https://doi.org/10.1049/joe.2019.0502
[research_zhang_liao_2026]: https://doi.org/10.1016/j.ast.2026.111885
[research_zhang_liu_2011]: https://doi.org/10.2514/6.2011-6658
[research_zhang_liu_2015]: https://doi.org/10.1016/j.actaastro.2015.08.006
[research_zhang_liu_2017]: https://doi.org/10.23919/chicc.2017.8027759
[research_zhang_nie_2019]: https://doi.org/10.1016/j.ast.2019.105445
[research_zhang_she_2015]: https://doi.org/10.2514/6.2015-1021
[research_zhang_shou_2022]: https://doi.org/10.1016/j.neucom.2021.10.084
[research_zhang_song_2025]: https://doi.org/10.1364/ao.558916
[research_zhang_su_2022]: https://doi.org/10.1016/j.ast.2022.107887
[research_zhang_sun_2013]: https://doi.org/10.1007/978-3-642-42057-3_81
[research_zhang_sun_2013_b]: https://doi.org/10.1007/978-3-642-42057-3_87
[research_zhang_sun_2013_c]: https://doi.org/10.1007/s11768-013-1164-5
[research_zhang_sun_2022]: https://doi.org/10.1109/icus55513.2022.9986788
[research_zhang_tang_2008]: https://doi.org/10.3182/20080706-5-kr-1001.02202
[research_zhang_tang_2015]: https://doi.org/10.2514/6.2015-3667
[research_zhang_tang_2025]: https://doi.org/10.1109/ddcls66240.2025.11065632
[research_zhang_tong_2024]: https://doi.org/10.1109/icus61736.2024.10840132
[research_zhang_wang_2016]: https://doi.org/10.1016/j.ast.2016.08.020
[research_zhang_wang_2018]: https://doi.org/10.1007/s00521-018-3764-y
[research_zhang_wang_2018_b]: https://doi.org/10.1016/j.ceramint.2017.11.066
[research_zhang_wang_2019]: https://doi.org/10.1007/s11431-018-9378-3
[research_zhang_wang_2019_b]: https://doi.org/10.1115/1.4043511
[research_zhang_wang_2019_c]: https://doi.org/10.1177/1077546319856142
[research_zhang_wang_2023]: https://doi.org/10.1007/978-981-19-6613-2_709
[research_zhang_wang_2024]: https://doi.org/10.1109/aim55361.2024.10637004
[research_zhang_wang_2025]: https://doi.org/10.1007/978-981-96-3552-8_23
[research_zhang_wang_2025_b]: https://doi.org/10.1007/978-981-96-2212-2_27
[research_zhang_wu_2007]: https://doi.org/10.4028/0-87849-410-3.1159
[research_zhang_xia_2017]: https://doi.org/10.23919/chicc.2017.8028337
[research_zhang_xia_2025]: https://doi.org/10.1016/j.ast.2025.110222
[research_zhang_xian_2014]: https://doi.org/10.1007/s11771-014-1924-5
[research_zhang_xiong_2022]: https://doi.org/10.1049/rsn2.12251
[research_zhang_xu_2012]: https://doi.org/10.4028/www.scientific.net/amm.198-199.207
[research_zhang_xu_2021]: https://doi.org/10.2322/tjsass.64.234
[research_zhang_xu_2025]: https://doi.org/10.1117/1.oe.64.10.103102
[research_zhang_yan_2008]: https://doi.org/10.4028/0-87849-473-1.1756
[research_zhang_yan_2026]: https://doi.org/10.1007/s42405-026-01193-9
[research_zhang_yang_2015]: https://doi.org/10.1109/ihmsc.2015.175
[research_zhang_yang_2018]: https://doi.org/10.23919/chicc.2018.8483369
[research_zhang_yang_2022]: https://doi.org/10.1109/cac57257.2022.10055737
[research_zhang_ye_2016]: https://doi.org/10.2514/1.c033381
[research_zhang_yu_2017]: https://doi.org/10.1088/1757-899x/187/1/012004
[research_zhang_yu_2018]: https://doi.org/10.1109/gncc42960.2018.9018888
[research_zhang_yu_2026]: https://doi.org/10.1007/978-981-95-6366-1_30
[research_zhang_zhang_2020]: https://doi.org/10.2322/tjsass.63.151
[research_zhang_zhang_2022]: https://doi.org/10.23919/ccc55666.2022.9901754
[research_zhang_zhang_2023]: https://doi.org/10.1016/j.actaastro.2023.03.031
[research_zhang_zheng_2022]: https://doi.org/10.3390/aerospace9040206
[research_zhang_zhou_2025]: https://doi.org/10.3390/act14090461
[research_zhang_zong_2014]: https://doi.org/10.1155/2014/264247
[research_zhangqingzhen_gaochen_2008]: https://doi.org/10.1109/isscaa.2008.4776316
[research_zhangqingzhen_liucunjia_2007]: https://doi.org/10.1109/robio.2007.4522311
[research_zhangzhikai_duanguangren_2015]: https://doi.org/10.1109/ascc.2015.7244862
[research_zhao_2011]: https://doi.org/10.2514/6.2011-3858
[research_zhao_2021]: https://doi.org/10.1007/978-981-33-6526-1_2
[research_zhao_2021_b]: https://doi.org/10.1007/978-981-33-6526-1_1
[research_zhao_2021_c]: https://doi.org/10.1007/978-981-33-6526-1_4
[research_zhao_bai_2026]: https://doi.org/10.1016/j.ceramint.2026.02.119
[research_zhao_cai_2018]: https://doi.org/10.1109/ccdc.2018.8407903
[research_zhao_chen_2019]: https://doi.org/10.1007/s11071-019-04897-8
[research_zhao_chen_2021]: https://doi.org/10.1049/icp.2021.1426
[research_zhao_cui_2012]: https://doi.org/10.4028/www.scientific.net/amr.625.100
[research_zhao_cui_2012_b]: https://doi.org/10.4028/www.scientific.net/amr.625.109
[research_zhao_dong_2020]: https://doi.org/10.1109/cac51589.2020.9327117
[research_zhao_guo_2013]: https://doi.org/10.4028/www.scientific.net/amm.318.96
[research_zhao_he_2018]: https://doi.org/10.1109/gncc42960.2018.9019043
[research_zhao_hong_2023]: https://doi.org/10.1117/12.2651380
[research_zhao_hu_2022]: https://doi.org/10.3390/math10234414
[research_zhao_huang_2018]: https://doi.org/10.1051/jnwpu/20183630403
[research_zhao_huang_2018_b]: https://doi.org/10.1016/j.actaastro.2018.07.034
[research_zhao_huang_2020]: https://doi.org/10.1016/j.paerosci.2020.100606
[research_zhao_jiang_2021]: https://doi.org/10.1080/00207721.2021.1876274
[research_zhao_li_2019]: https://doi.org/10.1109/access.2019.2930658
[research_zhao_ma_2025]: https://doi.org/10.1016/j.ast.2025.110031
[research_zhao_meng_2022]: https://doi.org/10.1177/09544100221145990
[research_zhao_pan_2026]: https://doi.org/10.1016/j.ast.2026.112447
[research_zhao_quan_2025]: https://doi.org/10.1007/978-981-96-3568-9_21
[research_zhao_shao_2022]: https://doi.org/10.3390/aerospace9120742
[research_zhao_song_2017]: https://doi.org/10.1016/j.actaastro.2017.04.013
[research_zhao_tang_2015]: https://doi.org/10.2991/icismme-15.2015.71
[research_zhao_wang_2016]: https://doi.org/10.1109/icisce.2016.215
[research_zhao_wu_2026]: https://doi.org/10.3390/aerospace13070644
[research_zhao_xie_2024]: https://doi.org/10.1016/j.euromechflu.2023.10.013
[research_zhao_yang_2021]: https://doi.org/10.1108/aeat-08-2020-0178
[research_zhao_yao_2021]: https://doi.org/10.1117/12.2586492
[research_zhao_zhou_2013]: https://doi.org/10.1016/j.cja.2013.10.009
[research_zhao_zhou_2014]: https://doi.org/10.1109/jsee.2014.00073
[research_zhao_zhou_2014_b]: https://doi.org/10.1155/2014/878193
[research_zheleznyakova_surzhikov_2014]: https://doi.org/10.1134/s0018151x14020217
[research_zhen_fei_2012]: https://doi.org/10.1109/iccsnt.2012.6526105
[research_zheng_2021]: https://doi.org/10.1061/(asce)as.1943-5525.0001257
[research_zheng_fu_2020]: https://doi.org/10.1016/j.ast.2020.106285
[research_zheng_hu_2020]: https://doi.org/10.2514/1.j059139
[research_zheng_li_2020]: https://doi.org/10.2514/1.j058640
[research_zheng_selezneva_2022]: https://doi.org/10.1109/rusautocon54946.2022.9896297
[research_zheng_wang_2022]: https://doi.org/10.1007/978-981-16-9492-9_136
[research_zhengchun_2018]: https://doi.org/10.1109/gncc42960.2018.9018936
[research_zhengdong_man_2013]: https://doi.org/10.1155/2013/369092
[research_zhi_liang_2015]: https://doi.org/10.1016/j.proeng.2014.12.559
[research_zhi_ran_2015]: https://doi.org/10.1016/j.proeng.2014.12.633
[research_zhijian_huan_2018]: https://doi.org/10.1109/gncc42960.2018.9018903
[research_zhiqiangzhao_zhengdonghu_2010]: https://doi.org/10.1109/isscaa.2010.5633320
[research_zhivotov_nikolaev_2011]: https://doi.org/10.1615/tsagiscij.v42.i3.50
[research_zhong_fan_2022]: https://doi.org/10.3390/aerospace9030132
[research_zhong_wu_2021]: https://doi.org/10.1155/2021/2115641
[research_zhong_yan_2017]: https://doi.org/10.1016/j.ceramint.2016.11.171
[research_zhongjiemeng_jianzhongdong_2010]: https://doi.org/10.1109/wcica.2010.5554861
[research_zhongjiemeng_panfenghuang_2008]: https://doi.org/10.1109/aim.2008.4601825
[research_zhou_2009]: https://doi.org/10.2514/6.2009-7384
[research_zhou_2018]: https://doi.org/10.5772/intechopen.70863
[research_zhou_2023]: https://doi.org/10.4273/ijvss.15.2.22
[research_zhou_chen_2006]: https://doi.org/10.1117/12.717986
[research_zhou_ding_2017]: https://doi.org/10.2514/6.2017-2218
[research_zhou_ding_2018]: https://doi.org/10.23919/chicc.2018.8483610
[research_zhou_du_2022]: https://doi.org/10.3390/e24101325
[research_zhou_fei_2013]: https://doi.org/10.1109/jsee.2013.00055
[research_zhou_hu_2008]: https://doi.org/10.4028/0-87849-473-1.1050
[research_zhou_lei_2017]: https://doi.org/10.1016/j.ast.2016.12.022
[research_zhou_li_2023]: https://doi.org/10.1007/978-981-19-6613-2_64
[research_zhou_li_2023_b]: https://doi.org/10.1016/j.ast.2022.108053
[research_zhou_lu_2017]: https://doi.org/10.2514/6.2017-2343
[research_zhou_pan_2016]: https://doi.org/10.1109/fskd.2016.7603508
[research_zhou_qi_2024]: https://doi.org/10.1109/fasta61401.2024.10595101
[research_zhou_shi_2015]: https://doi.org/10.4028/www.scientific.net/amm.742.234
[research_zhou_sun_2018]: https://doi.org/10.3390/s18020411
[research_zhou_tan_2012]: https://doi.org/10.2514/6.2012-4709
[research_zhou_wang_2019]: https://doi.org/10.1016/j.actaastro.2019.08.012
[research_zhou_wang_2026]: https://doi.org/10.1109/taes.2026.3705024
[research_zhou_xia_2023]: https://doi.org/10.1016/j.actaastro.2023.05.036
[research_zhou_xu_2025]: https://doi.org/10.1088/1742-6596/3109/1/012005
[research_zhou_yi_2023]: https://doi.org/10.2514/1.j062455
[research_zhou_zeng_2010]: https://doi.org/10.4028/www.scientific.net/amr.105-106.210
[research_zhou_zhang_2024]: https://doi.org/10.1016/j.applthermaleng.2024.123101
[research_zhou_zheng_2023]: https://doi.org/10.1007/978-981-19-6613-2_9
[research_zhou_zhou_2026]: https://doi.org/10.3390/aerospace13080711
[research_zhoujinwei_lijicheng_2015]: https://doi.org/10.3788/aos201535.0504001
[research_zhouwenya_chenhongbo_2008]: https://doi.org/10.1109/isscaa.2008.4776298
[research_zhu_2013]: https://doi.org/10.1007/978-3-642-38460-8_22
[research_zhu_chen_2017]: https://doi.org/10.2991/iccia-17.2017.28
[research_zhu_he_2018]: https://doi.org/10.1016/j.ast.2018.03.038
[research_zhu_li_2016]: https://doi.org/10.1109/cgncc.2016.7828860
[research_zhu_liu_2014]: https://doi.org/10.1016/j.actaastro.2014.07.026
[research_zhu_liu_2014_b]: https://doi.org/10.1007/s11431-014-5615-0
[research_zhu_liu_2015]: https://doi.org/10.1109/ccdc.2015.7162436
[research_zhu_liu_2015_b]: https://doi.org/10.1109/ccdc.2015.7162611
[research_zhu_liu_2016]: https://doi.org/10.1016/j.asr.2015.10.037
[research_zhu_shen_2015]: https://doi.org/10.1016/j.proeng.2014.12.535
[research_zhu_shen_2016]: https://doi.org/10.1109/cgncc.2016.7829081
[research_zhu_yao_2023]: https://doi.org/10.1109/cac59555.2023.10450493
[research_zhu_zhao_2016]: https://doi.org/10.1016/j.actaastro.2016.01.028
[research_zhuang_ridley_2024]: https://doi.org/10.47611/jsrhs.v13i4.7581
[research_zhuo_qingzhen_2011]: https://doi.org/10.1109/imccc.2011.236
[research_zhuo_zhang_2023]: https://doi.org/10.23919/ccc58697.2023.10240010
[research_zien_1998]: https://doi.org/10.2514/6.1998-1580
[research_zien_2006]: https://doi.org/10.2514/6.2006-7932
[research_zimmermann_burkhardt_1996]: https://doi.org/10.2514/6.1996-3708
[research_zishka_agarwal_2015]: https://doi.org/10.2514/6.2015-2967
[research_ziyang_xiaohui_2025]: https://doi.org/10.1016/j.isatra.2025.08.017
[research_zoby_gupta_1993]: https://doi.org/10.2514/3.26388
[research_zoli_sciti_2021]: https://doi.org/10.1016/b978-0-12-818542-1.00023-0
[research_zong_ji_2012]: https://doi.org/10.1016/j.ast.2011.09.012
[research_zong_wang_2013]: https://doi.org/10.1002/rnc.3040
[research_zong_wang_2013_b]: https://doi.org/10.1016/j.ast.2012.07.004
[research_zope_bhushan_2026]: https://doi.org/10.2514/6.2026-1143
[research_zou_candler_2024]: https://doi.org/10.2514/6.2024-0671
[research_zou_johnston_2023]: https://doi.org/10.2514/6.2023-0816
[research_zou_wang_2015]: https://doi.org/10.1155/2015/237453
[research_zou_xie_2013]: https://doi.org/10.1109/rast.2013.6581228
[research_zuber_bertin_1998]: https://doi.org/10.2514/6.1998-1633
[research_zubin_ostapenko_1997]: https://doi.org/10.1007/bf03374538
[research_zuchowski_2013]: https://doi.org/10.2514/6.2013-1457
[research_zuo_hu_2021]: https://doi.org/10.1016/j.actaastro.2021.01.058
[research_zuppardi_costagliola_2006]: https://doi.org/10.2514/6.2006-8032
[research_zvedre_2016]: https://doi.org/10.46272/2587-8476-2016-0-1-52-61
[research_zweber_kabis_2002]: https://doi.org/10.2514/6.2002-5172
