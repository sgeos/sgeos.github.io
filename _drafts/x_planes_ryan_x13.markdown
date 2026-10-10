---
layout: post
mathjax: true
comments: true
title: "X-Planes: Ryan X-13 Vertijet"
date: 2025-10-19 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 14
---

<!-- A310 -->
<script>console.log("A310");</script>

The [Ryan X-13 Vertijet][ref_x13] did everything it was asked to do and it changed nothing. On 11 April 1957 it rose vertically from a hook on the back of a lorry, tilted over into wingborne flight, flew, tilted back, hovered, and hung itself on the same hook. **Nothing before it had completed that cycle on jet thrust alone, and nothing crewed has been built to do it since.** This article is the fourteenth in the [X-Planes series][related_post_a297_xplanes_framing], following the [X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], the [X-4][related_post_a301_northrop_x4], the [X-5][related_post_a302_bell_x5], the [X-6][related_post_a303_convair_x6], the [X-7][related_post_a304_lockheed_x7], the [X-8][related_post_a305_aerojet_x8], the [X-9][related_post_a306_bell_x9], the [X-10][related_post_a307_north_american_x10], the [X-11][related_post_a308_convair_x11], and the [X-12][related_post_a309_convair_x12].

It also ends a run. The [X-8][related_post_a305_aerojet_x8], [X-9][related_post_a306_bell_x9], [X-10][related_post_a307_north_american_x10], [X-11][related_post_a308_convair_x11], and [X-12][related_post_a309_convair_x12] were sounding rockets, missiles, and ballistic weapon articles, none of them a research aircraft in the sense the [X-1][related_post_a298_bell_x1] established. **The X-13 is a research aircraft again**, built by one company in two examples to answer one question, and the question is a good one. The standard inventory entry remains [Jenkins Landis and Miller 2003 American X-Vehicles, An Inventory X-1 to X-50][book_jenkins_landis_miller_2003], the vehicle compilation is [Miller 2001 The X-Planes, X-1 to X-45][book_miller_2001], and the wider vertical take-off context is [Rogers 1989 VTOL, Military Research Aircraft][book_rogers_1989].

## The Research Question

An aeroplane is controlled by moving air over surfaces. At zero airspeed there is no air moving over anything, so a machine that intends to hover must be controlled by something else, and at some point in between the something else must hand over.

### Two Systems Whose Authority Scales Differently

The moment available from a control surface is proportional to dynamic pressure,

$$M_{\text{aero}} = q \, S \, \bar{c} \, \Delta C_{m}, \qquad q = \tfrac{1}{2} \rho V^{2}$$

so it vanishes as the square of the speed and is exactly zero in a hover. The moment available from deflecting the engine's own thrust does not depend on airspeed at all,

$$M_{\text{thrust}} = T \, \ell \sin \theta$$

where $\ell$ is the distance from the nozzle to the centre of mass and $\theta$ is the deflection. **One term is quadratic in speed and the other is constant, so they cross exactly once**, at

$$V_{\text{equal}} = \sqrt{\frac{T \ell \sin \theta}{\tfrac{1}{2} \rho S \bar{c} \, \Delta C_{m}}}$$

and the airframe must be adequately controlled on both sides of that crossing and at it.

**Two different crossings will appear below and it is worth separating them now.** One is the speed at which the aerodynamic surfaces produce as much moment as the deflected thrust does, which is where the two curves meet. The other is the speed at which the aerodynamic surfaces produce enough moment to meet the control-power criterion, which happens earlier because the criterion asks for less than the thrust can supply. **The second is the one that matters**, since a vehicle needs adequate control and not maximal control, and the first turns out to lie above the speed at which the aircraft is flying normally anyway.

That is the X-13's research question, and it is not a question the previous five articles could have asked. The [X-11][related_post_a308_convair_x11] was a mass-fraction problem and the [X-12][related_post_a309_convair_x12] a terminal-velocity problem. **Neither vehicle was ever required to be controllable at zero airspeed, because neither was ever at zero airspeed while airborne.** The general statement of the problem for this class of aircraft is [Campbell 1962][research_campbell_1962], which is the period's standard treatment, with the conference record in [NASA 1960][research_naca_1960] and [NASA 1960, NASA Conference on V/STOL Aircraft][research_naca_1960_2].

### What Adequate Means

Control authority is judged against an angular acceleration the pilot can use, and the period settled on figures near half a radian per second squared in pitch and one in roll for a hovering aircraft. The X-13's mass at its gross weight of 6,730 pounds is

$$m = 3053 \, \text{kg}$$

and its pitching moment of inertia need not be estimated. **The Langley spin-tunnel programme tabulated the airplane's full-scale mass characteristics**, and [Bowman 1957][research_bowman_1957] gives 4,042 slug square feet in pitch for the normal loading with full fuel and the landing hook, at 6,696 pounds. Converting at 1.3558 kilogramme square metres to the slug square foot,

$$I_{yy} = 4042 \times 1.3558 = 5480 \, \text{kg m}^{2}$$

which is a radius of gyration of $\sqrt{I_{yy}/m} = 1.34$ metres, or 0.19 of the 7.14 metre length, so the required pitching moment is

$$M_{\text{req}} = I_{yy} \, \dot{q}_{\text{req}} = 5480 \times 0.50 = 2740 \, \text{N m}$$

The criterion is an estimate and is identified as such in the Epistemic State. The criteria themselves were being established experimentally at exactly this moment, and the aircraft that established them was the next one in this series, in [Drinkwater and Rolls 1962][research_drinkwater_rolls_1962] using the variable-stability X-14A, with the visual-flight investigation in [Garren et al 1965][research_garren_1965].

### Three Axes, Three Different Answers

The crossing is not a single event, because the three axes are controlled by different things and hand over at different speeds.

**Pitch** is deflected thrust against elevons, and both act about the same axis with comparable arms. **Yaw** is deflected thrust against a rudder, and on a tail-sitter the rudder is on a fin that is short because the fuselage is short. **Roll cannot use deflected thrust at all**, and the reason is geometric rather than a matter of degree. The moment of a force applied at a position is

$$\mathbf{M} = \mathbf{r} \times \mathbf{F}$$

and for a nozzle on the longitudinal axis the position vector is parallel to that axis, so

$$\mathbf{M} \cdot \hat{\mathbf{x}} = (\mathbf{r} \times \mathbf{F}) \cdot \hat{\mathbf{x}} = 0$$

for any $\mathbf{F}$ whatever. **The rolling moment from the nozzle is identically zero and not merely small**, so a separate device is required that a conventional aeroplane does not carry.

That asymmetry is the reason a tail-sitting jet looks the way it does. **The roll axis is the one that forces a design decision**, and everything outboard on the X-13, the endplates and the jets beyond them, exists to serve it. The systematic study of what a jet vertical take-off aircraft actually needs by way of reaction control is [Friend 1964][research_friend_1964], and the cost of providing it is quantified in [Hoffman 1971][research_hoffman_1971].

### Where They Cross

With the wing area of 191 square feet and span of 21 feet that [Bowman 1957][research_bowman_1957] tabulates for the airplane, a mean chord taken as area over span,

$$\bar{c} = \frac{S}{b} = \frac{17.74}{6.40} = 2.77 \, \text{m}$$

and an elevon pitching-moment increment of 0.10 at full deflection, the aerodynamic moment is

$$M_{\text{aero}} = \tfrac{1}{2} \times 1.225 \times 17.74 \times 2.77 \times 0.10 \, V^{2} = 3.013 \, V^{2}$$

Setting that equal to the requirement gives the speed below which the control surfaces cannot do the job,

$$V_{\text{cross}} = \sqrt{\frac{2740}{3.013}} = 30.2 \, \text{m/s} = 59 \, \text{knots}$$

The vectored thrust, meanwhile, is ample everywhere. A ten degree deflection of 10,000 pounds of thrust at an assumed 3.5 metre arm gives

$$M_{\text{thrust}} = 44{,}482 \times 3.50 \times \sin 10^{\circ} = 27{,}035 \, \text{N m}$$

which is

$$\frac{M_{\text{thrust}}}{M_{\text{req}}} = \frac{27{,}035}{2740} = 9.87$$

Evaluating the equal-authority crossing introduced above gives

$$V_{\text{equal}} = \sqrt{\frac{27{,}035}{3.013}} = 94.7 \, \text{m/s}$$

so the two curves do not meet until well beyond the speed at which the aircraft is flying normally, and the elevons never dominate within the transition. The fraction of the available authority that is aerodynamic,

$$\lambda(V) = \frac{M_{\text{aero}}(V)}{M_{\text{aero}}(V) + M_{\text{thrust}}}$$

is therefore small throughout.

| Speed | Aerodynamic share of available authority |
|---|---|
| 0 m/s | 0.000 |
| 20 m/s | 0.043 |
| 30.2 m/s | 0.092 |
| 40 m/s | 0.151 |
| 60 m/s | 0.286 |

**At the speed where the elevons first become adequate they still supply only about a tenth of what is available**, and the nozzle is doing the rest. That is the honest picture of the handover and it is more gradual than a single crossover speed suggests.

**The vectored thrust supplies nearly ten times what is needed.** The criteria this is measured against were assembled over the following decade, in [Tapscott 1960][research_tapscott_1960] on primary handling qualities for hovering and transition, [Anderson 1960][research_anderson_1960] examining the criteria themselves, [Clark 1964][research_clark_1964], and later by moving-base simulation in [McCormick 1969][research_mccormick_1969] and by task performance measurement in [Harper and Sardanowsky 1969][research_harper_sardanowsky_1969]. So the handover is not a struggle between two marginal systems. The thrust vectoring is comfortable from zero airspeed upward, and the aerodynamic surfaces become comfortable at 30 metres per second. The interesting question is what that speed is compared with.

### The Answer, and Why It Is Not Obvious

The wing begins carrying the aircraft at its stall speed. At a gross weight of 29,935 newtons over 17.74 square metres, with a maximum lift coefficient of 1.0 for a thin delta without high-lift devices,

$$V_{\text{stall}} = \sqrt{\frac{2W}{\rho S C_{L\max}}} = \sqrt{\frac{2 \times 29{,}935}{1.225 \times 17.74 \times 1.0}} = 52.5 \, \text{m/s}$$

so

$$\frac{V_{\text{cross}}}{V_{\text{stall}}} = \frac{30.2}{52.5} = 0.575$$

**The control surfaces become adequate at well under three fifths of the speed at which the wing starts flying.** The controls come alive before the wing does, and that ordering is the whole reason a tail-sitting jet is possible at all. Had the crossover come at twice the stall speed the aircraft would have had a band of speeds in which it was flying on its wing and could not be pointed, which is not a survivable condition.

The ordering is not luck, and it is worth seeing why. Both quantities scale with $W/S$ and with the same dynamic pressure, so their ratio depends on the ratio of the control-moment coefficient to the lift coefficient and on the geometry, and not on the size or weight of the aircraft. **A tail-sitting jet works because the same air that lifts a wing also works its controls, and both start at once.** The low-speed characteristics that set the wing side of it are [Aoyagi and Tolhurst 1964][research_aoyagi_tolhurst_1964] and [Spencer 1962][research_spencer_1962]. What would break it is not weight but a control surface too small, and this is the design margin the article's later sections keep returning to.

Writing the ratio out makes the independence explicit. Both speeds come from setting a moment equal to a requirement,

$$V_{\text{cross}}^{2} = \frac{I_{yy} \dot{q}_{\text{req}}}{\tfrac{1}{2} \rho S \bar{c} \, \Delta C_{m}}, \qquad V_{\text{stall}}^{2} = \frac{2W}{\rho S C_{L\max}}$$

so their ratio is

$$\left( \frac{V_{\text{cross}}}{V_{\text{stall}}} \right)^{2} = \frac{I_{yy} \, \dot{q}_{\text{req}} \, C_{L\max}}{W \bar{c} \, \Delta C_{m}}$$

The wing area has cancelled and the air density has cancelled. What remains is the pitch inertia divided by the weight, which for a given shape scales as a length, divided by the mean chord, which is also a length. **The ratio is therefore a function of proportions and of the required angular acceleration, and not of scale**, which is why a one-fifth-scale model of this aircraft can demonstrate the same handover. It is also why the requirement itself became the interesting variable, and whether the control power a hovering aircraft needs depends on its size was studied directly in [Johnston and Friend 1965][research_johnston_friend_1965] and [Johnston et al 1965][research_johnston_1965].

## Programme Origin

### A Navy Question From 1947

**The line begins with the Navy.** In 1947 the Bureau of Aeronautics awarded Ryan a contract to investigate a vertically launched jet fighter, as part of an evaluation of submarine-based aircraft, according to the [National Air and Space Museum's record of the aircraft][ref_nasm_x13], and a [compilation][ref_x13] gives the original designation as F3R. The motivation was that a vertically launched fighter needs no runway, and therefore could operate from a small ship, from a clearing, or from a submarine. Ryan's own starting point was the FR-1 Fireball, a mixed-power fighter the company had already built, whose thrust-to-weight ratio reached one at low fuel quantities.

**A jet test rig preceded the aeroplane.** The same record describes an unmanned demonstrator powered by an Allison J33 that first flew on 20 October 1950 and was controlled in the hover by a ball-mounted nozzle, and a manned conversion of it in which Peter Girard made the first manned hovering flight in a jet aircraft on 24 November 1953.

**The Navy pursued the same idea with propellers and got there first.** The Convair XFY-1 and the Lockheed XFV-1 were turboprop tail-sitters flown from 1954, and their development generated the research literature this article rests on, in [Lovell et al 1953][research_lovell_1953], [Lovell 1954][research_lovell_1954], [Queijo et al 1953][research_queijo_1953], [Johnson 1954][research_johnson_1954], [Smith and Lovell 1954][research_smith_lovell_1954], [Schade et al 1954][research_schade_1954], [Kelly and Smaus 1952][research_kelly_smaus_1952], [Sutton and Buell 1952][research_sutton_buell_1952], and [Kirby 1954][research_kirby_1954]. **The X-13 exists because the Air Force wanted the same demonstration on pure jet thrust**, and after the Navy's funding ran out it contracted Ryan in July 1954 for two demonstrators, according to the [Smithsonian record][ref_nasm_x13]. Compilations, among them the [standard reference entry][ref_x13], give 1953 instead. A stand-on configuration had already been flown as a model in [McKinney 1954][research_mckinney_p_1954], and rocket-boosted and windmilling-propeller variants of the XFY-1 case are [Hastings and Mitcham 1954][research_hastings_mitcham_1954] and [Hollinger and Mitcham 1955][research_hollinger_mitcham_1955].

**The mid-1950s were also the moment the whole configuration space was surveyed at once.** Comparative studies weighed tail-sitters against tilt-wings, deflected slipstream, and lift engines, in [Irvin and Swan 1956][research_irvin_swan_1956] on performance and weight estimates for six vertical take-off aircraft, [Boeing Co Morton Pa Vertol Div 1956][research_div_1956], and [McCormick 1956][research_mccormick_w_1956], the last of which is a transition analysis and is therefore the nearest thing in the accessible literature to a general treatment of this article's keystone. The propeller side of the same survey is [Kirby 1961][research_kirby_1961] and [Kuhn and Grunwald 1960][research_kuhn_grunwald_1960].

### Why the Propeller Version Was Easier, in a Sentence That Needs Numbers

A turboprop tail-sitter hovers inside its own slipstream. The propeller pushes air over the wing and tail even at zero forward speed, so the control surfaces work in the hover. A turbojet tail-sitter exhausts aft of everything and its wing sees nothing at all.

Quantifying it settles the design difference completely. A propeller disc supporting a weight $W$ over area $A$ produces a slipstream of

$$v_{s} = \sqrt{\frac{2 (W/A)}{\rho}}$$

and for a disc loading of roughly 1,500 pascals, which is the class the XFY-1 sat in,

$$v_{s} = \sqrt{\frac{2 \times 1500}{1.225}} = 49.5 \, \text{m/s}$$

That is a dynamic pressure of 1,500 pascals over the inboard wing, against 1,687 pascals at the X-13's stall. **A turboprop tail-sitter hovers with something close to stall-speed dynamic pressure already on its control surfaces, and a turbojet tail-sitter hovers with none.** The propeller side of that statement is measured in [Sutton and Buell 1952][research_sutton_buell_1952] and surveyed in [Kirby 1961][research_kirby_1961]. The propeller aircraft therefore needed no reaction control system and the jet aircraft could not do without one, and that single ratio explains why the two configurations look so different despite answering the same question.

## Sizing From First Principles

### The First Condition, Which Is Necessary and Not Sufficient

A hovering aircraft must produce more thrust than it weighs. The Rolls-Royce Avon gave 10,000 pounds of thrust, in the figures of the [National Museum of the United States Air Force][ref_nmusaf_x13] and of the [Smithsonian record][ref_nasm_x13], which identifies it as an RA.28-49, against a gross weight of 6,730 pounds in compilations. **The primary weights differ among themselves.** The spin-tunnel table of [Bowman 1957][research_bowman_1957] gives 6,696 pounds with full fuel and the landing hook and 6,958 pounds with full fuel and wheels, the Smithsonian record a gross of 7,313 pounds, and the Air Force museum a maximum of 7,200. The 6,730 pounds used throughout lies within about half a percent of the hook loading. **The condition is the one that defines the whole configuration class**, and the surrounding design space, from lift fans through lift-plus-thrust arrangements to low-disc-loading rotorcraft, is [Denning 1962][research_denning_1962], [Przedpelski 1965][research_przedpelski_1965], and [Brown 1965][research_brown_1965], with the conference records in [Division 1966][research_division_1966] and the period's standard book reviewed in [Titchener 1963][research_titchener_1963]. Taking the ratio,

$$\frac{T}{W} = \frac{44{,}482}{29{,}935} = 1.486$$

and at the maximum weight of 7,200 pounds it is still 1.389. The vertical acceleration available is

$$a = g \left( \frac{T}{W} - 1 \right) = 9.807 \times 0.486 = 4.76 \, \text{m/s}^{2}$$

so the aircraft leaves the trailer at about half a gravity and reaches thirty metres in

$$t = \sqrt{\frac{2h}{a}} = \sqrt{\frac{60}{4.76}} = 3.55 \, \text{s}$$

arriving at 16.9 metres per second. **This is the condition everyone thinks of first and it is the least interesting one**, because an Avon in a small airframe satisfied it with room to spare. The heaviest the aircraft could be and still hover is 10,000 pounds, which is 3,270 pounds above its gross weight, and no part of the programme was ever limited by thrust.

### Hovering Is the Expensive Part

The condition that did bind is fuel. A turbojet producing thrust at a specific fuel consumption $c$ burns

$$\dot{m}_{f} = c \, T$$

and to hover it must produce thrust equal to weight, so the fuel flow in a hover is fixed by the aircraft's weight and nothing else. At an assumed 0.93 pounds per pound of thrust per hour, which is the figure quoted for the Avon and is adopted here as an estimate,

$$\dot{m}_{f} = 0.93 \times 6730 = 6259 \, \text{lb/hr} = 104.3 \, \text{lb/min}$$

The fuel load follows from the spin-tunnel table of loadings in [Bowman 1957][research_bowman_1957], which gives the airplane with its hook at 6,696 pounds with full fuel, 5,646 pounds with a quarter of it, and 5,366 pounds with a twentieth. The differences are three quarters and nineteen twentieths of the full load, so

$$m_{f} = \frac{6696 - 5646}{0.75} = \frac{6696 - 5366}{0.95} = 1400 \, \text{lb}$$

and the wheeled loadings in the same table return the same 1,400 pounds. That gives

$$t_{\text{hover}} = \frac{1400}{104.3} = 13.4 \, \text{min}$$

**The entire fuel load is about thirteen minutes of hovering.** That is the number the whole article turns on, and it is worth restating in the harshest form available. One minute of hovering at each end of a flight spends about fifteen percent of the fuel before the machine has gone anywhere.

The same table checks the compilations' weights. Removing the fuel from the wheeled loading leaves

$$6958 - 1400 - 5334 = 224 \, \text{lb}$$

above the 5,334 pound empty weight that compilations quote, which is about what a pilot and his equipment weigh, so the published empty weight appears to describe the aircraft on wheels.

The relation generalises and the generalisation is unkind. Hover endurance is

$$t_{\text{hover}} = \frac{m_{f}}{c \, W} = \frac{1}{c} \cdot \frac{m_{f}}{W}$$

so it depends only on the fuel fraction and the specific fuel consumption, and **not at all on the size of the aircraft or the thrust of its engine.** A larger tail-sitter with a larger engine hovers for exactly as long as a smaller one at the same fuel fraction. There is no scale at which the problem improves, which is the difference between this constraint and most aircraft design constraints, and it is why the comparative studies of the period kept returning verdicts against the configuration for transport work, in [Boeing Co Morton Pa Vertol Div 1956][research_div_1956] and [McCormick 1956][research_mccormick_w_1956]. The weight bookkeeping behind those verdicts is [Irvin and Swan 1956][research_irvin_swan_1956].

A rotorcraft escapes the same arithmetic because it does not produce its lift as thrust from a jet. Hovering efficiency is measured by the power needed per unit of lift, which for an actuator disc is

$$\frac{P}{T} = \sqrt{\frac{T/A}{2 \rho}}$$

and therefore improves as the disc grows. **A jet has the smallest possible disc and pays the largest possible price**, and the disc-loading comparison computed later in this article is the same fact seen from the ground rather than from the fuel gauge. That comparison across the three configurations was eventually made by measurement in [Michaelsen 1971][research_michaelsen_1971], and the weight bookkeeping that follows from it is [Irvin and Swan 1956][research_irvin_swan_1956].

### Roll, Which Is the Harder Axis

Pitch and yaw were handled by deflecting the engine exhaust. Roll could not be, because rolling the aircraft about the thrust line produces no moment however the nozzle is aimed. **A tail-sitting jet therefore needs a separate roll control that works at zero airspeed**, and the X-13 carried compressed-air jets at the wingtips, outboard of the endplates.

Sizing them is a short calculation. The spin-tunnel table gives the rolling moment of inertia as 1,543 slug square feet, so

$$I_{xx} = 1543 \times 1.3558 = 2092 \, \text{kg m}^{2}$$

and at a criterion of one radian per second squared the couple required is 2,092 newton metres. The one-fifth-scale model of [Smith 1958, Hovering and Transition Flight Tes][research_smith_1958_2], whose roll nozzles use engine bleed air, places them 24.375 inches from the centreline, which is 10.16 feet or 3.10 metres at full scale, so the opposed jets act on an arm of $d = 6.19$ metres and the force each must produce is

$$F = \frac{M}{d} = \frac{2092}{6.19} = 338 \, \text{N} = 76 \, \text{lbf}$$

which is 1.5 percent of the engine's thrust taken as a couple. At an assumed bleed velocity of 500 metres per second that is a mass flow of

$$\dot{m} = \frac{2F}{v} = \frac{676}{500} = 1.35 \, \text{kg/s}$$

or about 1.9 percent of an Avon's air. **A roll control that costs two percent of the engine is affordable and not negligible**, and it is a cost the propeller tail-sitters did not pay at all. The design problem of arranging engine control and attitude control together in a vertical-attitude aircraft is [Baxter and Finvold 1958][research_baxter_finvold_1958], which is the closest thing in the accessible literature to a statement of this vehicle's control philosophy, with the reaction control criteria worked systematically in [Friend 1964][research_friend_1964].

**What lateral control actually needs to feel like in a hovering jet-lift aircraft was measured directly**, in [Drinkwater et al 1965, Effects of lateral control charact][research_drinkwater_1965_2], which is the nearest experiment in the literature to the X-13's roll problem and postdates it by eight years. The variable-stability apparatus that made such measurements possible is [Hegarty et al 1965][research_hegarty_1965] for a deflected-jet aircraft, and the eventual in-flight simulation of competing hover control concepts is [Corliss et al 1977][research_corliss_1977]. Cross-coupling between axes, which a reaction control system introduces and an aerodynamic one largely does not, is [Garren 1961][research_garren_1961], and the augmentation that later removed the problem from the pilot is [Clark et al 1963][research_clark_1963] and [Hartmann et al 1979][research_hartmann_1979].

The ailerons take over earlier than the elevons do. At a rolling-moment coefficient of 0.05 the aerodynamic couple reaches the same criterion at

$$V = \sqrt{\frac{M}{\tfrac{1}{2} \rho S b \, \Delta C_{l}}} = 24.5 \, \text{m/s}$$

which is 0.47 of the stall speed, so **roll hands over from the puffers to the ailerons well before pitch hands over from the nozzle to the elevons.** The two axes do not cross at the same moment, and a pilot flying the transition is therefore managing a control system whose character changes progressively rather than all at once.

### Yaw, Which Is the Easy Axis, and the Sequence That Results

Yaw has been mentioned and not sized, and sizing it completes the picture. The spin-tunnel table gives the yawing moment of inertia as 4,833 slug square feet, or

$$I_{zz} = 4833 \times 1.3558 = 6553 \, \text{kg m}^{2}$$

which is 1.20 times the pitch inertia, and at a criterion of 0.3 radians per second squared the required moment is 1,966 newton metres. The nozzle supplies that at a deflection of

$$\theta = \arcsin \frac{M}{T \ell} = \arcsin \frac{1966}{44{,}482 \times 3.50} = 0.72^{\circ}$$

**Under one degree.** Yaw is the axis nobody had to think about, because the same nozzle that handles pitch handles yaw with a fraction of the deflection and the criterion is lower.

The rudder takes over early as well. At a yawing-moment increment of 0.06 the aerodynamic moment reaches the criterion at

$$V = \sqrt{\frac{M}{\tfrac{1}{2} \rho S b \, \Delta C_{n}}} = 21.7 \, \text{m/s}$$

which is 0.41 of the stall speed. The same deflection relation puts the pitch criterion at $\arcsin (2740 / 155{,}687) = 1.01$ degrees of nozzle. Collecting the three axes gives the article's structural result about the transition.

| Axis | Reaction or vectored device | Aerodynamic device takes over at | As a fraction of stall speed |
|---|---|---|---|
| Yaw | nozzle, 0.7 degrees | 21.7 m/s | 0.41 |
| Roll | wingtip jets, 338 N each | 24.5 m/s | 0.47 |
| Pitch | nozzle, 1.0 degree | 30.2 m/s | 0.57 |

**The three axes do not hand over together. They hand over in sequence, and the sequence runs from the cheapest axis to the dearest.** The derivatives that would settle the aerodynamic side of each were measured for this configuration class in [Queijo et al 1953, Wind-Tunnel Investigation at Low S][research_queijo_1953_2], [Queijo et al 1953, Wind-Tunnel Investigation at Low S][research_queijo_1953_3], and [Queijo et al 1953, Wind-Tunnel Investigation at Low S][research_queijo_1953_4], and for the jet-powered vertical-attitude model in [Shanks and Smith 1959][research_shanks_smith_1959] and [Shanks and Smith 1960][research_shanks_smith_1960]. A pilot accelerating through the transition therefore feels the aircraft become a conventional aeroplane one axis at a time, first in yaw, then in roll, and last in pitch, and for a band of about six metres per second, between 24.5 and 30.2, he is flying a machine that is aerodynamic in two axes and reactive in the third. That is a more interesting statement than a single crossover speed, and it is the kind of thing an article gets only by computing all three.

### The Transition, Which Is Quick and Cheap

Set against the hover, the transition itself is almost free. In the manoeuvre the aircraft tilts by an angle $\phi$ from the vertical, and the thrust must still support the weight,

$$T \cos \phi \geq W$$

so the steepest available tilt is

$$\phi_{\max} = \arccos \frac{W}{T} = \arccos 0.6730 = 47.7^{\circ}$$

At that attitude the horizontal acceleration, neglecting drag, is

$$a_{h} = g \frac{T}{W} \sin \phi_{\max} = 9.807 \times 1.486 \times 0.7396 = 10.78 \, \text{m/s}^{2}$$

which is 1.10 gravities. Reaching the stall speed therefore takes

$$t = \frac{V_{\text{stall}}}{a_{h}} = \frac{52.5}{10.78} = 4.9 \, \text{s}$$

over a distance of

$$s = \tfrac{1}{2} a_{h} t^{2} = 128 \, \text{m}$$

and consumes, at full thrust,

$$m_{f} = \frac{10{,}000 \times 0.93 \times 4.9}{3600} = 12.6 \, \text{lb}$$

**Twelve pounds of fuel and five seconds.** The manoeuvre the entire programme existed to demonstrate costs about one percent of the fuel, and the hovering that brackets it costs everything else. Flying at a gentler tilt is slower and therefore more expensive.

| Tilt from vertical | Horizontal acceleration | Vertical acceleration | Time to stall speed |
|---|---|---|---|
| 20 degrees | 4.98 m/s² | +3.89 m/s² | 10.5 s |
| 30 degrees | 7.29 m/s² | +2.81 m/s² | 7.2 s |
| 40 degrees | 9.36 m/s² | +1.36 m/s² | 5.6 s |
| 47.7 degrees | 10.78 m/s² | 0.00 m/s² | 4.9 s |

The transition analysis for the configuration class is [McCormick 1956][research_mccormick_w_1956], and the model flight tests that flew the manoeuvre are [Smith 1958, Hovering and Transition Flight Tes][research_smith_1958_2] for the X-13 itself and [Smith 1958][research_smith_1958] and [Smith 1961][research_smith_1961] for the closely related jet-powered vertical-attitude model, whose lateral derivatives were measured in [Shanks and Smith 1959][research_shanks_smith_1959] and [Shanks and Smith 1960][research_shanks_smith_1960].

**The vertical column is the constraint that makes the table interesting.** At every tilt shallower than 47.7 degrees the aircraft is still climbing while it accelerates, which is comfortable but slow. At exactly 47.7 degrees it holds altitude and accelerates hardest. Beyond it the aircraft descends, and doing that near the ground with a wing not yet flying is the condition the transition exists to avoid.

### What Control Power Costs

Reaction control is not free and its price is paid in the same currency as everything else. A puffer system sized to the criterion above bleeds about 1.9 percent of the engine's air, and bleeding air from a turbojet costs thrust roughly in proportion, so holding the roll criterion in a hover costs

$$\Delta T \approx 0.0193 \, T = 859 \, \text{N} = 193 \, \text{lbf}$$

against a hover margin of 3,270 pounds. **Roll control alone consumes about six percent of the thrust margin**, before pitch and yaw are considered and before any allowance for gusts. That figure is an estimate resting on the assumed bleed velocity, and the general accounting of what control power costs a vertical take-off aircraft is [Hoffman 1971][research_hoffman_1971].

Whether the cost is worth paying against the alternatives is a question the field answered much later and in the opposite direction, since a lateral-directional control system built deliberately around thrust vectoring is [Lallman 1985][research_lallman_1985]. **What the X-13 treated as a penalty is now sometimes the point**, because an aircraft that can point its thrust can be flown at attitudes a conventional one cannot.

The consequence is a design spiral of the ordinary kind. More control power needs more bleed, which needs more thrust, which needs a larger engine, which needs a larger airframe, which has more inertia and therefore needs more of it. The spiral has a direction and it can be written down. The required moment scales with inertia,

$$M_{\text{req}} = I \dot{\omega} \propto m L^{2}$$

while the available moment scales with thrust times a moment arm, and at a fixed thrust-to-weight ratio the thrust scales with the mass,

$$M_{\text{av}} = T \ell \sin \theta \propto m L$$

so the ratio of what is needed to what is there grows linearly with size,

$$\frac{M_{\text{req}}}{M_{\text{av}}} \propto L$$

| Linear scale | Mass | Control power as a fraction of the engine |
|---|---|---|
| 1 | 1 | 1.9 percent |
| 2 | 8 | 3.9 percent |
| 3 | 27 | 5.8 percent |

**Doubling the length doubles the fraction of the engine that attitude control consumes.** The spiral therefore converges only for a small aircraft, and the X-13 is small. This is a different and stronger statement than the earlier one that the crossover ratio is independent of scale, and both are true. **The speed at which the controls become adequate does not care about size. The cost of making them adequate does.** Whether the requirement itself should depend on size is [Johnston et al 1965][research_johnston_1965] and [Johnston and Friend 1965][research_johnston_friend_1965].

### What an Operational Version Would Have Cost

The programme was a demonstration and never carried a weapon, but the arithmetic of what it would have meant operationally is short and is the reason the idea stopped. The fuel fraction is

$$\zeta = \frac{1400}{6730} = 0.208$$

and the Breguet range for a jet is

$$R = \frac{V}{c} \frac{L}{D} \ln \frac{1}{1 - \zeta}$$

with $c$ the thrust specific fuel consumption expressed as a reciprocal time, which for 0.93 pounds per pound-hour is $2.583 \times 10^{-4}$ per second. At a cruise speed of 200 metres per second and a lift-to-drag ratio of six,

$$R = \frac{200}{2.583 \times 10^{-4}} \times 6 \times \ln \frac{1}{0.792} = 1083 \, \text{km}$$

giving a radius of 542 kilometres if every pound of fuel went to cruising. It does not.

| Total hover time | Fuel spent hovering | Radius | Radius forgone |
|---|---|---|---|
| 60 s | 104.3 lb | 497 km | 45 km, 8.3 percent |
| 120 s | 208.6 lb | 453 km | 89 km, 16.5 percent |
| 180 s | 312.9 lb | 409 km | 133 km, 24.5 percent |

**One minute of hovering at each end of the flight costs a sixth of the radius.** The period's own weight and performance bookkeeping for this class is [Irvin and Swan 1956][research_irvin_swan_1956], with the configuration comparison in [Boeing Co Morton Pa Vertol Div 1956][research_div_1956] and [Campbell 1962][research_campbell_1962]. **The same arithmetic was run for civil operations and returned the same verdict**, in [Spillman 1965][research_spillman_1965] on short-range vertical take-off jet airliners, where a route short enough to suit the aircraft is also short enough that the hover fuel dominates the sortie. And one minute is optimistic for a vertical landing onto a hook, for the reasons the Dependent Systems section quantifies.

| Hover discipline | Take-off and landing | Fuel spent | Fraction of fuel |
|---|---|---|---|
| Brisk | 0.5 and 1.0 minutes | 156 lb | 11.2 percent |
| Realistic | 1.0 and 2.0 minutes | 313 lb | 22.4 percent |
| Cautious | 2.0 and 4.0 minutes | 626 lb | 44.7 percent |

**A cautious pilot spends nearly half the fuel without leaving the airfield.** And the Dependent Systems section shows that the pilot has every reason to be cautious, since he is flying a third-order loop by proxy through a man on the ground toward a hook he cannot see. The vertical take-off and landing capability is therefore not free and not cheap. It is paid for in the currency the aircraft has least of, and the payment is made twice on every sortie.

## Dependent Systems

### The Engine, Which Is Most of the Aeroplane

The [Smithsonian record][ref_nasm_x13] describes the engine as an Avon RA.28-49 axial-flow turbojet of 10,000 pounds of thrust, while the spin-tunnel tests of [Bowman 1957][research_bowman_1957] simulated the rotating parts of an Avon R.A. 14 at 8,000 revolutions per minute, and the documents available do not say whether the designation changed between the model tests and the flights. In an airframe with an empty weight of 5,334 pounds the engine is a large fraction of the whole, and it is better understood as an engine with a wing attached than as an aeroplane with an engine in it. **Every dimension of the X-13 follows from wrapping the smallest possible airframe around an Avon**, which is why the span is 21 feet, the length 23.445 feet, or 23 feet 5 inches, in the dimensional table of [Bowman 1957][research_bowman_1957], and the aspect ratio

$$AR = \frac{b^{2}}{S} = \frac{6.40^{2}}{17.74} = 2.31$$

A wing of aspect ratio 2.31 is a poor lifting device and a good structural one, and on an aircraft that spends its critical moments not using the wing at all, that is the correct trade.

**Installing a jet engine in an aircraft that must hover creates aerodynamic problems the engine does not have on a test stand**, and the survey of them is [Kuhn and McKinney 1965][research_kuhn_marion_0_mckinney_1965]. The inlet is the acute case, since in the transition it is asked to swallow air arriving from every direction in turn, which is [Grahame 1968][research_grahame_1968] and [Grahame 1969][research_grahame_1969]. What that does to the compressor is [Evans et al 1974][research_evans_1974], with the distortion statistics in [Jacocks and Kneile 1975][research_jacocks_kneile_1975] and the full-scale testing technique in [Palko 1973][research_palko_1973]. **The powerplant experience the period actually accumulated on a jet vertical take-off aircraft was written up for the next aircraft in this series**, in [Rolls 1965, Jet Vtol power plant experience du][research_rolls_1965_2].

### The Nozzle

Pitch and yaw came from deflecting the exhaust. The relation derived above puts the required deflection in context, since a ten degree deflection delivers nearly four times the pitching moment the criterion asks for, so the nozzle need not be large-angle and the deflection can be modest. The penalty is a loss of axial thrust,

$$\frac{T_{\text{axial}}}{T} = \cos \theta = \cos 10^{\circ} = 0.985$$

so **a ten degree deflection costs 1.5 percent of the thrust**, which against a thrust-to-weight ratio of 1.486 is affordable. At thirty degrees it would cost 13.4 percent, which is not, and this is the quantitative reason a vectoring system for attitude control is a small-angle device while one for propulsion is not.

| Deflection | Axial thrust retained | Moment produced | Angular acceleration |
|---|---|---|---|
| 5 degrees | 99.6 percent | 13,569 N m | 0.969 rad/s² |
| 10 degrees | 98.5 percent | 27,035 N m | 1.932 rad/s² |
| 15 degrees | 96.6 percent | 40,295 N m | 2.879 rad/s² |

The two quantities move in opposite directions with deflection, since

$$M(\theta) = T \ell \sin \theta, \qquad \frac{T_{\text{axial}}}{T} = \cos \theta$$

so the moment grows almost linearly at small angles while the thrust loss grows quadratically,

$$1 - \cos \theta \approx \frac{\theta^{2}}{2}$$

which is why small-angle vectoring is nearly free and large-angle vectoring is not.

The mechanisms available for turning a jet were an active subject and remained one, in [Erwin et al 1964][research_erwin_1964] on tandem cascade vectoring, [Eatough 1971][research_eatough_1971] on jet tabs, and [Shandor and Walker 1962][research_shandor_walker_1962] on fluid injection, with the measurement problem of establishing where a nozzle's thrust vector actually points in [Davis and Spicer 1965][research_davis_spicer_1965] and [Holdhusen and Perusse 1965][research_holdhusen_perusse_1965].

### The Puffer Jets

The wingtip jets sized above are the aircraft's only roll control below 25 metres per second. Their placement outboard of the wingtip endplates is a moment-arm decision and the arithmetic is direct, since the required force varies inversely with the arm,

$$F = \frac{I_{xx} \dot{p}}{d}$$

so halving the arm would double the force and therefore double the bleed. **A tail-sitting jet wants a wide span for roll control and a small span for everything else**, and that tension is visible in the aircraft's proportions.

### The Wing, Which Spends the Critical Moments Doing Nothing

A wing of aspect ratio 2.31 with a sharp leading edge is a poor subsonic lifting surface and its low-speed behaviour is dominated by leading-edge vortices rather than by attached flow. The adopted maximum lift coefficient of 1.0 reflects that, and the sensitivity is worth showing because the article's central ratio depends on it.

| Maximum lift coefficient | Stall speed | Ratio of crossover to stall |
|---|---|---|
| 0.8 | 58.7 m/s | 0.514 |
| 1.0 | 52.5 m/s | 0.575 |
| 1.2 | 47.9 m/s | 0.629 |

The relation behind the table is the ratio derived earlier,

$$\frac{V_{\text{cross}}}{V_{\text{stall}}} = \sqrt{\frac{I_{yy} \dot{q}_{\text{req}} \, C_{L\max}}{W \bar{c} \, \Delta C_{m}}}$$

which grows as the square root of the maximum lift coefficient, because a wing that stalls later gives the elevons less time to catch up.

**Even at a lift coefficient of 1.2 the crossover stays well below the stall speed**, at 0.63 of it, so the reading that the controls come alive before the wing does survives a large error in a coefficient that has been assumed rather than measured. The ratio reaches one only when the maximum lift coefficient exceeds $1.0 / 0.575^{2} = 3.0$, far beyond any figure considered here. The low-speed aerodynamics of slender deltas at high incidence are [Clark and Spurlin 1962][research_clark_spurlin_1962], [Spencer 1962][research_spencer_1962], and [Wentz 1972][research_wentz_1972], and what a tailless delta fighter is actually like to fly slowly is [White and Innis 1959][research_white_innis_1959] and [Huff 1949][research_huff_w_1949].

**The reason such a wing does not behave like a conventional one was explained only after the X-13 flew.** The lift of a sharp-edged delta at incidence comes largely from the vortex that forms along the leading edge rather than from attached flow, and the analogy that made it calculable is [Polhamus 1966][research_polhamus_1966], extended in [Polhamus 1968][research_polhamus_1968] and [Polhamus 1969][research_polhamus_1969]. The structure of the vortex itself is [Roy 1966][research_roy_1966] and [Li and Polak 1966][research_li_polak_1966], and the practical consequence, that a rounded planform behaves better at low speed, is [Rolls 1965][research_rolls_1965] and [Drinkwater and Rolls 1965][research_drinkwater_rolls_1965]. **A maximum lift coefficient of 1.0 assumed for this wing is therefore a vortex-lift number and not an attached-flow one**, which is worth knowing given how much of the article rests on it.

### Hovering Is a Position Loop With Nothing Holding It Still

The article has treated hovering as a control-power problem, which it is, and that understates it. **A hovering airframe has no aerodynamic restoring moment in any axis**, so an attitude disturbance does not decay, and attitude is what produces horizontal acceleration,

$$\ddot{x} = g \sin \theta$$

Position is therefore the double integral of attitude, and attitude is the integral of whatever the control does, so the pilot is closing a third-order loop by eye with no natural damping anywhere in it. Evaluating the first integral makes the tolerance visible.

| Tilt held | Horizontal acceleration | Drift in five seconds |
|---|---|---|
| 0.5 degrees | 0.086 m/s² | 1.07 m |
| 1.0 degrees | 0.171 m/s² | 2.14 m |
| 2.0 degrees | 0.342 m/s² | 4.28 m |
| 5.0 degrees | 0.855 m/s² | 10.68 m |

**Holding position to within a metre over five seconds requires holding the mean tilt below half a degree.** That is the actual task, and it is why hovering is difficult in a way that the control-power criteria do not capture. Measuring task performance rather than control power is what [Harper and Sardanowsky 1969][research_harper_sardanowsky_1969] set out to do, with the visual side in [Garren et al 1965][research_garren_1965] and the loop closure itself observed in [Lollar and Matous 1963][research_lollar_matous_1963]. **The instability is not a defect of the aircraft but of the flight condition**, and the same difficulty appears in every hovering machine, including the helicopter work of [McCaskill 1953][research_mccaskill_1953] and [Warsett 1953][research_warsett_1953] and, much later, the near-hover control of a helicopter carrying a swinging load in [Gupta and Bryson 1976][research_gupta_bryson_1976]. The criteria say the pilot can command an angular acceleration. They do not say he can hold an attitude to half a degree while looking sideways.

### The Wind Is a Position Problem, Not an Attitude Problem

Standing vertically, the airframe presents its whole length to a crosswind. Taking a side area of ten square metres and a drag coefficient of 0.8, both estimates,

$$F = \tfrac{1}{2} \rho V^{2} A C_{d}$$

| Crosswind | Side force | Acceleration | Uncorrected drift in 30 s |
|---|---|---|---|
| 5 m/s | 122 N | 0.040 m/s² | 18 m |
| 10 m/s | 490 N | 0.160 m/s² | 72 m |
| 15 m/s | 1102 N | 0.361 m/s² | 163 m |

The moment such a wind produces is small, at 17.9 percent of the pitch requirement in a ten metre per second wind with the side-area centroid a metre from the centre of mass. **So the wind does not threaten control and it does threaten station-keeping.**

The conflict can be made exact. To hold station the aircraft must tilt into the wind until the horizontal component of thrust balances the side force,

$$g \sin \theta_{w} = \frac{\tfrac{1}{2} \rho V^{2} A C_{d}}{m}$$

| Crosswind | Steady tilt needed to hold station | As a multiple of the drift budget |
|---|---|---|
| 5 m/s | 0.23 degrees | 0.50 |
| 10 m/s | 0.94 degrees | 2.00 |
| 15 m/s | 2.11 degrees | 4.49 |

The drift budget derived above was a mean tilt below 0.47 degrees. **In a ten metre per second wind the tilt required merely to stay still is twice that budget**, so the pilot is holding a steady attitude error of about a degree while trying to keep the fluctuating part below half of one. The two tasks use the same actuator and they conflict, which is the coupling [Tapscott 1960][research_tapscott_1960] and [Anderson 1960][research_anderson_1960] were trying to write criteria around. **The conflict was eventually measured rather than argued**, in [Whitaker et al 1977][research_whitaker_1977] on how hover stability affects the hover control task, and the loop the pilot is actually closing was characterised as early as [Lollar and Matous 1963][research_lollar_matous_1963], which observes the pilot-vehicle loop closure for hovering aircraft directly. **That paper is the single closest thing in the literature to the analysis this article has just performed**, and it postdates the X-13's last flight by six years.

### Height, and an Asymmetry

Vertical control is a throttle problem and it is asymmetric. A vertical acceleration $a$ requires a thrust change of $m a$, so

| Vertical acceleration | Thrust change | As a fraction of thrust |
|---|---|---|
| 0.5 m/s² | 1,526 N | 3.4 percent |
| 1.0 m/s² | 3,053 N | 6.9 percent |
| 2.0 m/s² | 6,106 N | 13.7 percent |

The relation is simply Newton's second law applied to the vertical axis,

$$\Delta T = m a$$

and the bounds are asymmetric. Upward,

$$a_{\max} = \frac{T - W}{m} = 4.76 \, \text{m/s}^{2}$$

and downward there is no bound at all, because the pilot can always close the throttle and let the aircraft fall. **A descent is easier to start than to stop.**

Stopping one costs engine response time and then stopping distance, so the height lost recovering from a sink rate $v$ with an engine lag $\tau$ is roughly

$$\Delta h \approx v \tau + \frac{v^{2}}{2 a_{\max}}$$

| Sink rate | Height lost at a one second lag |
|---|---|
| 0.5 m/s | 0.53 m |
| 1.0 m/s | 1.11 m |
| 2.0 m/s | 2.42 m |

**A one metre per second sink costs a metre before the aircraft is going up again**, and against a hook tolerance of a third of a metre that is the whole budget spent on a sink rate a pilot would barely notice.

The vertical axis turns out to be a distinct control problem with its own requirements rather than a trivial one, and the field eventually said so, in [Gerdes 1964][research_gerdes_1964] on a piloted simulator investigation of height-control requirements and, two decades later, [Stevens and Roskam 1985][research_stevens_roskam_1985] on the vertical axis control power a landing vertical take-off aircraft actually needs. Flight path control as a system problem is [Ostheimer and Giguere 1963][research_ostheimer_giguere_1963]. **The engine is the actuator, so the problem is a propulsion problem as much as a flight control one**, and controlling lift engines for exactly this purpose is [Sellers and Szuch 1973][research_sellers_szuch_1973]. A vertical velocity command system, which removes the pilot from the throttle loop altogether, is the obvious answer.

**Making the engine respond faster is the other half of the answer and it is a control problem in its own right.** Turbine engine control synthesis is [Ryan et al 1975][research_ryan_1975], [Stone et al 1975][research_stone_1975], and [Beale and Miller 1975][research_beale_miller_1975], the coordination problem when a hovering aircraft has more than one engine is [Swick and Skarvan 1967][research_swick_skarvan_1967], and the reliability of the fuel control that all of it depends on is [Burnell et al 1973][research_burnell_1973] and [Zagranski et al 1974][research_zagranski_1974]. Diagnosing what an engine is actually doing is [Douglass 1963][research_douglass_1963] and [Harris 1969][research_harris_1969]. **A 1957 hydromechanical fuel control was not a fast actuator**, and every one of those documents is part of the reason it later became one.

### The Ground Observer Was Part of the Control Loop

The arrangement the [Smithsonian record][ref_nasm_x13] describes, constant radio communication with a ground observer who talked the pilot into position because the pilot could not see the trailer, is usually recorded as an operational inconvenience. **It is better understood as a sensor with a transport delay inserted into a third-order loop that has no damping.**

The hook tolerance is of order a third of a metre. At a closure rate of one metre per second, a loop delay $\tau$ introduces a position uncertainty of

$$\delta x = V \tau$$

so a delay of 0.3 seconds consumes the entire tolerance, and 0.3 seconds is optimistic for a human observer speaking over a radio to a pilot who must then move a control. **The X-13 landed successfully many times, so the loop clearly closed**, and the arithmetic says it closed with very little margin and only because the closure rate was kept low. What a pilot can and cannot do with a delayed and partial view of a landing point is [Behan and Siciliani 1965][research_behan_siciliani_1965], [Behan and Siciliani 1967][research_behan_siciliani_1967], and [Rhoads 1967][research_rhoads_1967]. Keeping the closure rate low costs hover time, and hover time is the fuel.

### The Trailer, the Wire, and the Hook

In its vertical configuration the X-13 had no undercarriage in the ordinary sense, and flat bumpers replaced the main wheels of its fixed gear to protect the fuselage if it swung against the trailer bed. It hung from a cable suspended between two arms at the top of a trailer bed, which raised to the vertical for launch and recovery and lowered to the horizontal to move the aircraft. A partially retractable hook on the nose engaged the cable, and a folding pole about twenty feet long with marked gradations, attached to the top of the trailer, gave the pilot a distance reference. All of this is from the [Smithsonian record][ref_nasm_x13].

The arrangement removes weight from the aircraft and puts it on the ground. Written as a bookkeeping identity, the launch system's mass is simply moved out of the term that has to be lifted,

$$m_{\text{lifted}} = m_{\text{empty}} + m_{\text{fuel}} + m_{\text{payload}}, \qquad m_{\text{trailer}} \notin m_{\text{lifted}}$$

**Moving mass out of the lifted term is the oldest trick in vertical take-off design and it recurs in every generation**, from the flying platform of [Sissingh 1956][research_sissingh_1956] through the ground-effect machines of [Walker et al 1965][research_walker_1965] and [Davidson et al 1972][research_davidson_1972] to the air cushion landing systems of [Leland and Thompson 1975][research_leland_thompson_1975]. What distinguishes the X-13 is that the mass was moved onto a vehicle which then had to be present at the landing point.

Deleting the legs is the correct decision for an aircraft whose thrust margin is 3,270 pounds and whose undercarriage would have cost several hundred. **It also makes the aircraft dependent on a specific piece of ground equipment for every landing**, which is the opposite of the operational freedom the vertical take-off concept was supposed to buy, and the tension between those two facts is the deepest problem in the programme. The same tension appears from the other direction in [Butler and Thomas 1964][research_butler_thomas_1964], which is about preparing sites rather than about not needing them.

### The Undercarriage That Was Not Carried

The trailer looks like an eccentricity and it is a weight decision. A retractable undercarriage for a machine of this class costs something in the region of three to five percent of gross weight, so

| Gear weight as a fraction of gross | Weight | As a fraction of the fuel load |
|---|---|---|
| 3 percent | 202 lb | 14.4 percent |
| 4 percent | 269 lb | 19.2 percent |
| 5 percent | 336 lb | 24.0 percent |

Converting the saving into the currency the aircraft actually lacks gives

$$\Delta t_{\text{hover}} = \frac{w_{g}}{c \, W}$$

| Gear weight | Extra hover time | Endurance gained |
|---|---|---|
| 202 lb | 1.94 min | 14.4 percent |
| 269 lb | 2.58 min | 19.2 percent |
| 336 lb | 3.22 min | 24.0 percent |

**The spin-tunnel table measures the saving directly.** Its full-fuel loading is 6,958 pounds with wheels and 6,696 pounds with the hook in [Bowman 1957][research_bowman_1957], so the wheels cost

$$6958 - 6696 = 262 \, \text{lb}$$

net of the hook, which is 3.8 percent of the wheeled weight, inside the range assumed above, and worth $262 / 104.3 = 2.51$ minutes of hovering. **Deleting the undercarriage bought about two and a half minutes of hovering**, which against a thirteen and a half minute endurance is about a fifth more, and by the radius table above some tens of kilometres. Weight bookkeeping of this kind across the configuration options is [Irvin and Swan 1956][research_irvin_swan_1956]. On an aircraft this tightly bounded that is not a small saving, and it explains why a design that looks like a stunt is actually the obvious answer once the fuel arithmetic is admitted.

The structural side reinforces it. Hanging from a hook at the nose puts the entire weight into the airframe as a **tension**, while standing on a tail puts the same load in as a **compression** on a slender body. A tension member is lighter than a column of equal strength, so the hook arrangement is structurally as well as operationally cheaper than legs would have been. Estimating what airframe structure weighs, which is how such a trade is settled in practice, is [Chaloff et al 1974][research_chaloff_1974] and [Marchinski 1974][research_marchinski_1974], and a conventional gear's own control problems are [Yang 1970][research_yang_1970].

The arrival itself is gentle. At a closure rate $v$ arrested over a stroke $d$ the mean deceleration is

$$a = \frac{v^{2}}{2d}$$

so a one metre per second arrival stopped in 0.3 metres is

$$a = \frac{1.0}{0.6} = 1.67 \, \text{m/s}^{2} = 0.17 g$$

**A vertical landing on a wire is a very soft landing**, softer than a conventional arrival on a runway, which is worth stating because the arrangement looks violent and is not. Landing impact as a designed problem, in the form it takes when the undercarriage is unconventional, is [Leland and Thompson 1975][research_leland_thompson_1975]. **The difficulty of the landing was never the impact. It was arriving at the right place with the right speed while unable to see.**

### The Cockpit, and a Pilot Who Cannot See

The pilot's seat pivoted forty-five degrees toward the vertical for the landing, according to the [Smithsonian record][ref_nasm_x13], so that he was not lying flat on his back during vertical flight. Forty-five degrees is a compromise and it leaves the problem half-solved, because his line of sight remains

$$90^{\circ} - 45^{\circ} = 45^{\circ}$$

away from the direction the aircraft is travelling during a vertical descent. Writing the geometry down shows why the compromise cannot be improved. Let $\beta$ be the angle between the pilot's line of sight and the direction the aircraft is travelling during the descent. For a seat pivoted by $\sigma$ from the body axis,

$$\beta = 90^{\circ} - \sigma$$

| Seat pivot | Angle between sight line and direction of travel |
|---|---|
| 0 degrees | 90 degrees |
| 45 degrees | 45 degrees |
| 90 degrees | 0 degrees |

**Driving $\beta$ to zero means laying the pilot flat on his back facing the tail**, which is not a position from which to fly an aeroplane that is about to become horizontal. Forty-five degrees is the compromise, and it leaves the fuselage between the pilot and the target.

**The reported and decisive difficulty is that the underside of the fuselage sits between the pilot and the trailer he is trying to land on.** The [Smithsonian record][ref_nasm_x13] calls the obscured view the concept's greatest flaw. He approached the recovery point without being able to see it and depended on a ground observer to talk him down.

That is not a detail. The vertical landing is a closed-loop position-control task with a tolerance of about a third of a metre on a hook, executed by a pilot who cannot see the target, in an aircraft with thirteen minutes of fuel, in ground effect. The visual requirements for exactly this class of task were being measured at the time in [Garren et al 1965][research_garren_1965] and [Behan and Siciliani 1965][research_behan_siciliani_1965], and the general problem of a pilot's acceptance of a landing display is [Behan and Siciliani 1967][research_behan_siciliani_1967] and [Rhoads 1967][research_rhoads_1967].

**What happens to a pilot's performance when the visual cues are removed was eventually measured directly**, in [Howard 1976][research_howard_1976], with the related question of how much an imperfect instrument substitute costs in [Howard 1975][research_howard_1975]. The answers the field arrived at were all forms of giving the information back rather than improving the view. Peripheral vision displays are [Vallerie 1967][research_vallerie_1967], a head-up display for a tilt-wing vertical take-off aircraft is [Gold and Walchli 1974][research_gold_walchli_1974], and the mature control and display combinations for instrument approach and shipboard landing are [Merrick 1981][research_merrick_1981], [Merrick 1984][research_merrick_1984], and [Farris et al 1983][research_farris_1983]. **Every one of those is a way of telling the pilot what he cannot see, and the X-13 had none of them.** Windshield optics as a contributor to the same problem is [Grether 1973][research_grether_1973].

### Spin and Tumble

A tail-sitter with a low aspect ratio and a large fuselage volume is a candidate for departure modes that a conventional aeroplane does not have, and the X-13 was tested for them in the Langley spin tunnel before it flew. **This is the one part of the programme with a complete surviving primary record**, in [Bowman 1955][research_bowman_1955] on free-spinning and recovery, [Bowman 1955, Emergency Spin-Recovery Device for][research_bowman_1955_2] on the parachute needed for emergency recovery during demonstration spins, which it sets at a stable parachute 12.73 feet in diameter, and [Bowman 1957][research_bowman_1957] as the concluding report covering spinning, tumbling, and recovery together. The equivalent studies for the propeller tail-sitters are [Lee 1952][research_lee_1952] and [Lee 1953][research_lee_1953], with the spin tunnel applied to conventional fighters for comparison in [Lee and Libbey 1961][research_lee_libbey_1961] and the deep-stall descent, which is the nearest conventional analogue to a tumble, in [Blanchard 1981][research_blanchard_1981]. Earlier free-spinning investigations in the same facility are [Bennett 1947][research_bennett_1947] and [Healy 1958][research_healy_1958], and the rotational-flow aerodynamics that eventually explained what the tunnel had been measuring is [Bihrle and Bowman 1980][research_bihrle_bowman_1980].

Tumbling was the mode the Air Force asked about, because an aircraft pointed vertically with no forward speed has no aerodynamic restoring moment in pitch. **The model did not tumble.** [Bowman 1957][research_bowman_1957] reports that the airplane will not tumble end over end but may instead enter a wild gyrating motion, a roll with simultaneous yaw and pitch from which recovery is doubtful, and it attributes the motion primarily to the gyroscopic moment of a large engine in a small airframe.

Arresting a pitch rotation with the engine running is an angular momentum problem. A rotation at rate $\omega$ carries

$$H = I_{yy} \omega$$

and the nozzle removes it at a rate equal to the moment it produces, so the time to stop is

$$t = \frac{I_{yy} \omega}{T \ell \sin \theta}$$

| Pitch rate | Angular momentum | Time to stop | Arc swept |
|---|---|---|---|
| 0.5 rad/s | 2,740 kg m²/s | 0.10 s | 1.5 degrees |
| 1.0 rad/s | 5,480 kg m²/s | 0.20 s | 5.8 degrees |
| 2.0 rad/s | 10,960 kg m²/s | 0.41 s | 23.2 degrees |

**With the engine running a pitch rotation is stopped in under half a second.** The engine that makes this possible is also the source of the trouble, because its rotor carries angular momentum of its own. [Smith 1958, Hovering and Transition Flight Tes][research_smith_1958_2] represented it on the one-fifth model with a flywheel of 39,500 pound square inches per second, which it describes as approximately the correctly scaled value. Under Froude scaling angular momentum grows as the four and a half power of length, so the full-scale engine carries about

$$H_{e} = 39{,}500 \times 5^{4.5} \, \text{lb in}^{2}/\text{s} = 1.62 \times 10^{4} \, \text{kg m}^{2}/\text{s}$$

which is about three times the airframe's own angular momentum at one radian per second in pitch. Any pitch rate $\Omega$ then produces a yawing moment

$$M_{g} = H_{e} \, \Omega$$

and a pitch rate of only 0.1 radians per second produces 1,615 newton metres, which is 82 percent of the yaw criterion computed above. **This is why the model could not be hovered without dampers.** Smith reports that with the engine's gyroscopic effect represented the pilots found the model completely uncontrollable in the hover, that pitch and yaw dampers made it easy to fly, and that every transition was flown with them. The full-scale aircraft carried them too. The [Smithsonian record][ref_nasm_x13] states that dampers were installed after the conventional flights revealed oscillation problems and that a stability augmentation system blended the conventional and hovering controls.

**With the engine out there is no nozzle and no reaction control**, because both are powered by it. Bowman simulated a power failure in the hover by dropping the model from rest in a nose-up attitude. It fell tail first, nosed over at up to 130 degrees per second, and was yawed by the engine's gyroscopic moment into what appeared to be a right spin, from which the report expects recovery with rudder and aileron once the engine has run down. It puts the minimum altitude for a belly landing after a power failure in the hover at

$$h_{\min} = 900 + 800 + 2500 = 4200 \, \text{ft}$$

the sum of the fall before the spin, the spin recovery, and a pull-out distance assumed from a similar configuration. The report describes the first term as a free fall over the time to spin entry and gives that time as about 6.5 seconds, which in free fall is

$$h = \tfrac{1}{2} g t^{2} = \tfrac{1}{2} \times 32.17 \times 6.5^{2} = 680 \, \text{ft}$$

so its two figures are not mutually consistent, and 900 feet corresponds to about 7.5 seconds. **Either way every vertical take-off and landing was necessarily flown far below the height from which a flame-out could be survived**, and the parachute of [Bowman 1955, Emergency Spin-Recovery Device for][research_bowman_1955_2] was sized for demonstration spins at altitude rather than for that case. It is the sharpest illustration in the article of what it means to control an aircraft with its propulsion.

### Ground Effect and the Pad

The exhaust the aircraft sits on is a small, fast, hot jet. Taking an engine mass flow of 70 kilogrammes per second, the exit velocity implied by the thrust is

$$v_{e} = \frac{T}{\dot{m}} = \frac{44{,}482}{70} = 635 \, \text{m/s}$$

and at an assumed exhaust density of 0.35 kilogrammes per cubic metre the dynamic pressure in the jet is

$$q_{e} = \tfrac{1}{2} \rho_{e} v_{e}^{2} = 70.7 \, \text{kPa} = 10.2 \, \text{psi}$$

The implied nozzle area is 0.315 square metres, so the disc loading is

$$\frac{T}{A} = 141 \, \text{kPa}$$

against what a rotor of the same 6.40 metre span would need,

$$\frac{T}{A_{\text{rotor}}} = \frac{44{,}482}{\pi (3.20)^{2}} = 1382 \, \text{Pa}$$

a ratio of

$$\frac{141{,}000}{1382} = 102$$

**A hovering jet loads the ground about a hundred times more heavily than a helicopter of the same span.** That is why a tail-sitting jet needs a prepared surface and a helicopter does not, and it is the second reason the operational freedom the concept promised was not actually available. The impingement problem and its design criteria are [George et al 1964][research_george_1964], with the dust-ingestion consequence in [Hafer and Skinner 1960][research_hafer_skinner_1960] and the analogous problem on another surface entirely in [Roberts 1964][research_roberts_1964].

**The downwash impingement problem generated its own multi-year study programme**, in [White et al 1960][research_white_1960], [Morse and Newhouse 1960][research_morse_newhouse_1960], and [Morse and Newhouse 1961][research_morse_newhouse_1961], with erosion specifically for jet-lift aircraft in [Dent 1966][research_dent_1966] and the spray a vertical take-off aircraft throws in [Kuhn 1979][research_kuhn_1979]. The fluid mechanics underneath is [Strand 1967][research_strand_1967] on the impingement of a jet on a plane, [Donaldson et al 1966][research_donaldson_1966] and [Donaldson et al 1971][research_donaldson_1971] on the turbulent structure of a free jet meeting a surface, and [Binion 1970][research_binion_w_1970] on the recirculation region such a flow creates.

**The aerodynamic penalty is separate from the erosion and is called suckdown**, since the entrained flow between the jet and the ground reduces the lift the aircraft actually has. That is [Gentry and Margason 1966][research_gentry_margason_1966], with the later modelling in [Kotansky and Bower 1977][research_kotansky_bower_1977] and [Kotansky 1982][research_kotansky_1982] and a large-scale investigation in [Christiansen 1984][research_christiansen_1984].

**The comparison the article makes between a jet and a rotor was made directly and by measurement**, in [Michaelsen 1971][research_michaelsen_1971], which compares the outflows from a helicopter, a tilt-wing aircraft, and a jet-lift aircraft. That paper is the empirical form of the hundred-to-one disc loading ratio computed above. **The operational answer was to prepare the ground**, and the fact that somebody wrote a document called rapid site preparation for turbojet vertical take-off aircraft, in [Butler and Thomas 1964][research_butler_thomas_1964], is the clearest possible statement that the runway had not actually been eliminated but relocated and renamed. Surface bearing capacity under aircraft loads is [Hay 1970][research_hay_1970], and the jet in ground effect as an aerodynamic problem is [Lissaman 1967][research_lissaman_1967], [Foltz 1962][research_foltz_1962], and [Carmichael and McNay 1961][research_carmichael_mcnay_1961].

## The Flight Test Record

Two aircraft were built, serial numbers 54-1619 and 54-1620, under the Ryan company designation Model 69 that a [compilation][ref_x13] gives. Both survived the programme, as [NASA's inventory of X-vehicles][ref_american_x_vehicles] records, which for a first-of-type vertical take-off aircraft is a notable result on its own.

| Date | Event | Aircraft |
|------|-------|----------|
| 1955-12-10 | First conventional flight, temporary tricycle landing gear | 54-1619 |
| 1956-05-28 | First vertical take-off and landing, on a temporary tail rig, and first flight of the second aircraft | both |
| 1956-11-28 | First transition from horizontal to vertical flight and back | not stated |
| 1957-04-11 | First complete cycle, from the trailer to the trailer | 54-1620 |
| 1957-07-30 | Demonstration at the Pentagon | 54-1620 |
| 1957-09-30 | Last flight | not stated |

The dates are those of the [Smithsonian record][ref_nasm_x13]. The [Air Force museum][ref_nmusaf_x13] confirms the conventional first flight in December 1955, the first hovering in May 1956, and the full cycle by the second X-13, the aircraft it now displays, at Edwards Air Force Base in April 1957. **The sources disagree about the end.** [NASA's inventory][ref_american_x_vehicles] gives the last flight as 30 July 1957 and the number of flights as unknown, and a [compilation][ref_x13] dates the Washington demonstration 28 and 29 July.

The sequence is worth reading as a decomposition. **The programme separated the problem into the two halves that could be tested independently and only then joined them.** The value of doing so is that a joint first attempt confounds the failures. If the wing, the hover, and the join each work with probability $p$, a single all-up attempt returns an unambiguous result only with probability

$$p^{3}$$

which for $p = 0.8$ is 0.51, while testing in sequence identifies which of the three failed with certainty. The first aircraft flew conventionally on temporary undercarriage to establish that it was an aeroplane, then took off and landed vertically on a temporary steel-tube tail rig with castering wheels to establish that it was a hovering machine, while its pilots practised hooking onto a rope strung between two towers with a replaceable wooden nose fitted, according to the [Smithsonian record][ref_nasm_x13]. The two halves were joined in the air six months after the first hover, and brought down to the trailer four and a half months after that. That ordering is the same one the [X-5][related_post_a302_bell_x5] used for variable sweep and the X-13's own predecessors used for the propeller case, and it is what a research aircraft programme looks like when it is being run carefully.

The intervals are 170 days from first flight to first hover, 184 days from first hover to first transition, and 134 days from there to the full cycle,

$$170 + 184 + 134 = 488 \, \text{days}$$

or 1.34 years from first flight to full cycle. The pilots were Ryan's chief test pilot Peter Girard and Ryan test pilot Lou Everett, whom the [Smithsonian record][ref_nasm_x13] names as the two who practised the hook-on technique and spells Everrett.

**A programme of two aircraft and a handful of flights cannot support a statistical statement and should not be asked to.** What it can support is a statement about sequence, and the sequence is the finding.

Each phase settled a different one of the article's relations. **The conventional flight on temporary undercarriage settled the wing**, which is to say it demonstrated the stall speed and the low-speed handling that the crossover ratio is measured against. **The hovering flights settled the reaction and vectoring authority**, which the relations above put at 9.87 times the criterion in pitch, and they also settled the position-loop problem well enough for the pilot to hold station. **The full cycle settled only the joining of the two**, and it is the shortest of the three questions because the transition itself lasts about five seconds.

That ordering also explains the sixteen month interval. The transition was first flown 184 days after the first hover, at altitude in a [compilation's][ref_x13] account, and only 134 days later from the trailer, so the only untested thing on the day of the full cycle was flying the whole sequence near the ground. The variable-stability technique that would later let one aircraft stand in for many is [Harper 1955][research_harper_p_1955] and, for this problem specifically, [Drinkwater and Rolls 1962][research_drinkwater_rolls_1962]. Simulation as the alternative to flying every case arrives with [McIntyre 1963][research_mcintyre_1963] and [McCormick 1969][research_mccormick_1969].

### What the Full Cycle Actually Demonstrated

**It demonstrated the crossover.** Everything in the article's first section is a prediction that the two control systems hand over cleanly, and the transitions flown from 28 November 1956, completed from trailer to trailer on 11 April 1957, are the measurement. The aircraft went from a state in which its wing did nothing and its nozzle did everything to the reverse, and back, without an uncontrollable band in between.

**It did not demonstrate anything about the mission**, because there was no mission. The aircraft carried no armament, no radar, no operational fuel load, and no capability to land anywhere except on its own trailer.

### The Pentagon Flight

On 30 July 1957 the second X-13 was demonstrated at the Pentagon before more than 3,000 military officers and journalists, according to the [Smithsonian record][ref_nasm_x13], which presents it as an illustration of the dispersed operating site concept. A [compilation][ref_x13] dates the Washington flights 28 and 29 July and describes a crossing of the Potomac. It is the most photographed event of the programme and the least technical. **A demonstration flown for an audience of officials is a statement that the technical question has been answered and the remaining question is whether anyone wants the answer.** The answer turned out to be no, and the primary accounts give money and size rather than doctrine as the reason. The [Smithsonian record][ref_nasm_x13] says competing programmes reduced the funds available, the [Air Force museum][ref_nmusaf_x13] says the design had limited operational potential and that a lack of funding shut the programme down in 1958, and [NASA's inventory][ref_american_x_vehicles] attributes the absence of a production follow-on mainly to the aircraft's small size and limited payload and to the inability of existing turbojets to power a larger version. The statement that the Air Force found no operational requirement is a [compilation's][ref_x13].

## Comparison With Ground Prediction

### What the Models Got Right

The X-13 was preceded by an unusually complete model programme, and the single most directly relevant document is [Smith 1958, Hovering and Transition Flight Tes][research_smith_1958_2] on hovering and transition flight tests of a one-fifth-scale model of the aircraft. **A free-flight model at one-fifth scale can perform the entire manoeuvre the full-scale aircraft exists to perform**, which is unusual, and the reason it works is that the problem is dominated by gravity rather than by viscosity.

**The model confirmed the handover and exposed a lateral weakness.** Smith flew slow constant-altitude transitions in the Langley full-scale tunnel over full-scale speeds of 0 to 110 knots and angles of attack from about 20 to 90 degrees, and found the transition very easy, with the swivelling nozzle giving adequate pitch control throughout, so that the elevons were trimmed and not used. That is what the relations above predict, since the nozzle supplies nearly ten times the pitch criterion. Between about 25 and 45 degrees angle of attack, however, the model was directionally unstable and settled into a rolled and sideslipped attitude, and restoring zero bank took approximately the maximum roll control available on the airplane. **That is the one finding of the model programme that the authority arithmetic does not anticipate**, because it is a stability problem rather than a control-power one.

Dynamic similarity in a gravity-dominated problem requires the Froude number to match,

$$\frac{V^{2}}{gL} = \text{constant}$$

so at a length scale $\kappa$ the speeds and times scale as its square root and the angular rates as its inverse square root,

$$\frac{V_{m}}{V_{f}} = \sqrt{\kappa}, \qquad \frac{t_{m}}{t_{f}} = \sqrt{\kappa}, \qquad \frac{\omega_{m}}{\omega_{f}} = \frac{1}{\sqrt{\kappa}}, \qquad \frac{m_{m}}{m_{f}} = \kappa^{3}$$

For the one-fifth model that gives

| Quantity | Full scale | One-fifth model |
|---|---|---|
| Stall speed | 52.5 m/s | 23.5 m/s |
| Crossover speed | 30.2 m/s | 13.5 m/s |
| Transition time | 4.9 s | 2.19 s |
| Transition distance | 128 m | 25.6 m |
| Mass | 3053 kg | 24.4 kg |

**A twenty-four kilogramme model flying at twenty-three metres per second reproduces the manoeuvre, and does it twice as fast.** That last point is the practical difficulty, since everything the observer has to watch happens at 2.24 times the rate. The model actually flown was lighter than the scaled mass, at 39.3 pounds in its rocket-powered tests in Smith's table of mass characteristics, against

$$\frac{39.3}{6730 / 125} = \frac{39.3}{53.8} = 0.73$$

of the Froude-scaled weight.

**The technique was a Langley speciality and it has a literature of its own.** Its development for low-speed and vertical take-off configurations is [Williams and Butler 1964][research_williams_butler_1964], its application to a free-flying model of a vertical take-off configuration is [Paulson and Shanks 1961][research_paulson_shanks_1961], and the radio-controlled variant used for departure work is [Burk and Wilson 1975][research_burk_wilson_1975]. An earlier example of the same method applied to another aircraft in this series is [Hewes and Hassell 1960][research_hewes_hassell_1960] on a one-seventh model of a North American design. The wind-tunnel free-flight technique in its general form is [Platou 1968][research_platou_1968], with the powered-model balance problem in [Dougherty 1966][research_dougherty_1966] and the oscillatory derivative measurement that supports it in [Owen and Cox 1966][research_owen_cox_1966] and [Barzda 1966][research_barzda_1966].

What does not scale is the Reynolds number, which goes as speed times length,

$$\frac{Re_{m}}{Re_{f}} = \kappa^{3/2} = 0.089$$

**eleven times lower**, so the model's boundary layer is not the aircraft's. For a manoeuvre governed by inertia and thrust that is tolerable, and for the stall it is not, which is exactly the division between what the models settled and what they did not.

The spin tunnel work in [Bowman 1955][research_bowman_1955] and [Bowman 1957][research_bowman_1957] covered the departure modes, and the whole XFY-1 and XFV-1 literature covered the configuration class, in [Lovell et al 1953][research_lovell_1953], [Queijo et al 1953][research_queijo_1953], [Kirby 1956][research_kirby_1956], and [Lovell and Parlett 1957][research_lovell_parlett_1957], the last of which is a jet-powered vertically rising model and therefore the nearest aerodynamic relative of the X-13 in the model record.

### What the Models Could Not Show

**A free-flight model has no pilot in it.** The decisive difficulty of the X-13, that the man flying it cannot see where he is going during the landing, is invisible at model scale because the model is flown by someone standing outside it with an unobstructed view. **The programme's ground testing was excellent and it tested the wrong difficulty**, not through carelessness but because the difficulty was not aerodynamic.

**A model does not burn fuel in proportion.** The endurance relation

$$t = \frac{\zeta}{c}$$

contains no length at all, so it neither improves nor worsens with scale, and a tethered or externally powered model carries no fuel fraction whatever. **The constraint is not merely mis-scaled in a model. It is absent from it**, and a model that hovers for as long as its tether is connected gives no warning that the full-scale aircraft has thirteen minutes.

**A model does not load the ground.** For geometric scaling at a fixed thrust-to-weight ratio the thrust goes as the cube of length and the nozzle area as the square, so the disc loading goes as the first power,

$$\frac{T}{A} \propto L$$

and a one-fifth-scale model imposes one fifth of the pressure, not one twenty-fifth. That is still 28 kilopascals, which is enough to notice and not enough to reproduce the erosion, and the linear rather than quadratic scaling is the reason ground-effect results from small models transfer poorly.

**And a model is flown to a different standard.** A free-flight model is judged by whether it completes the manoeuvre, and a real aeroplane is judged by whether a pilot can complete it repeatably while doing other things. The gap between those two standards is what handling qualities research exists to measure, and the techniques for measuring it were being invented alongside these aircraft, in [Anderson 1960][research_anderson_1960], [Clark 1964][research_clark_1964], [Nettleton 1965][research_nettleton_1965], [McGregor and Smith 1965][research_mcgregor_smith_1965], [Ashkenas 1965][research_ashkenas_1965], and [Harper and Sardanowsky 1969][research_harper_sardanowsky_1969], with pilot-model analysis in [Adams 1972][research_adams_1972].

## What the Data Changed

### Into the Control Power Criteria

The most durable result is the least visible. The question of how much attitude control power a hovering aircraft actually needs was open when the X-13 flew and was closed shortly afterwards by systematic experiment, in [Drinkwater and Rolls 1962][research_drinkwater_rolls_1962] using the X-14A as a variable-stability testbed and [Garren et al 1965][research_garren_1965] in visual flight. **The X-13 is one of the data points that made the question worth asking**, and the criteria that emerged are the ones used above to size its own controls, which is a pleasing circularity and a real one.

### Into Nothing Operational

No tail-sitting jet fighter was built. The reasons this article can demonstrate are the fuel arithmetic, the pilot's inability to see the landing point, and the ground loading, and they are all present in the numbers rather than in hindsight.

### Into the Configuration That Actually Worked

The vertical take-off jet did enter service, and not in this form. The Hawker P.1127 kept the aircraft horizontal and turned the thrust instead of turning the aeroplane, which leaves the pilot facing forward, leaves the undercarriage useful, and removes the landing visibility problem entirely. Its model testing is [Smith 1961, Flight Tests of a 1/6-Scale Model][research_smith_1961_2], flown at Langley in the same facility and by the same group that flew the X-13 model.

**The comparison is the fairest verdict on the X-13 available.** Both configurations solve the control-authority problem, and the vectored-thrust layout solves it while also solving the two problems the X-13 could not, namely where the pilot looks and what the aircraft rests on.

The first of those is geometric and can be stated in one number. Measure the bearing of the landing point from the pilot's line of sight during the descent. On a tail-sitter the target lies along the negative body axis, at the tail, so with the seat pivoted forty-five degrees the bearing is

$$135^{\circ}$$

On a horizontal aircraft hovering on deflected thrust the target lies directly below while the pilot looks forward and down, giving a bearing of order

$$45^{\circ}$$

**The same task is a hundred and thirty-five degrees behind one pilot and forty-five degrees below the other**, and no amount of seat pivoting closes that gap, because the difference is which end of the aeroplane is pointed at the ground.

The vectored-thrust line also inherited a research literature the tail-sitter did not. Take-off performance for vectored-thrust aircraft is [Krenkel and Salzman 1968][research_krenkel_salzman_1968], the flight control technology that made them practical is [Crandall et al 1973][research_crandall_1973] and, later, [Hartmann et al 1979][research_hartmann_1979] on digital adaptive control. **The competing answers of the same period all kept the pilot upright**, whether by tilting the wing, in [McCormick and Mallen 1956][research_mccormick_mallen_1956], [McCormick and Mallen 1957][research_mccormick_mallen_1957], [Mazzitelli 1957][research_mazzitelli_1957], [Hargraves 1961][research_hargraves_1961], [Putman 1961][research_putman_1961], [Clark et al 1963][research_clark_1963], [Longhurst 1966][research_longhurst_1966], and [Magee and Taylor 1971][research_magee_taylor_1971], or by ducting the lift, in [Parlett 1961][research_parlett_1961] and [Marchese 1963][research_marchese_1963]. **The X-13 is the only one of them that asked the pilot to lie on his back**, and it is the only one that did not proceed. The tri-service programme that carried the ducted-fan answer forward is [Marchese 1963][research_marchese_1963], and the carrier air wake a shipboard version would have had to land into is [Cook 1964][research_cook_1964]. **The X-13 demonstrated that the tail-sitting answer works and thereby helped establish that it was not the answer to take**, which is a real contribution and not the one the programme set out to make. A flight evaluation of a jet vertical take-off transport under visual and instrument conditions, which is the mature form of the same question, is [Holzhauser et al 1972][research_holzhauser_1972].

### The Vertical Attitude Idea Returns Twice

It came back in the 1970s as a proposal for carrier-based fighters, in [Eilertson 1975][research_eilertson_1975] on a remotely piloted demonstration vehicle, [Gerhardt and Chen 1978][research_gerhardt_chen_1978] on the vertical attitude concept for a fighter or attack aircraft, and [Papadales 1979][research_papadales_s_1979] on the performance of a conceptual vertical-attitude fighter.

**And it came back using the same technique that had supported the X-13 twenty years earlier.** [Newsom and Anglin 1975][research_newsom_anglin_1975] and [Grafton and Anglin 1975][research_grafton_anglin_1975] are free-flight model investigations of a vertical-attitude vertical take-off fighter, flown in the same facility and reported in the same form as [Smith 1958, Hovering and Transition Flight Tes][research_smith_1958_2]. **Two decades of intervening work changed the proposed aircraft and did not change how the question was asked**, which is a fair measure of how completely the technique had settled the aerodynamic side of the problem and how little it could say about the rest. **The remotely piloted version is the interesting one, because removing the pilot removes the problem the X-13 could not solve**, and it took two decades for anyone to say so in a document.

## The Contemporary Literature

The X-13's configuration is not a historical curiosity. It is a standard layout for small uncrewed aircraft, and the reason is exactly the one the 1975 remotely piloted proposal identified, which is that the configuration's hard problem was the pilot.

### The Same Relations, Run Forward

The most useful way into the modern literature is to apply the article's own relations to a modern vehicle. Nothing in them has changed, so the comparison is direct.

| Vehicle | Mass | Disc loading | Wing loading | Ratio | Hover endurance |
|---|---|---|---|---|---|
| Small quadrotor tail-sitter | 25 kg | 488 Pa | 490 Pa | 0.99 | 22.8 min |
| Medium tail-sitter | 120 kg | 462 Pa | 588 Pa | 0.79 | 23.4 min |
| Large lift-plus-cruise | 2000 kg | 542 Pa | 981 Pa | 0.55 | 21.6 min |
| **Ryan X-13** | **3053 kg** | **141,000 Pa** | **1,687 Pa** | **84** | **13.4 min** |

Two things fall out, and the second corrects the first.

**The disc loading and the wing loading of a modern electric tail-sitter are the same quantity to within a factor of two.** This article derived, from the XFY-1 comparison, that a designer who wants stall-level dynamic pressure on the control surfaces in a hover should choose a disc loading equal to the wing loading. **A small electric tail-sitter satisfies that condition without anyone arranging it**, because both quantities are set by the same structural and aerodynamic scaling once the propulsor is a set of rotors rather than a jet. The X-13's ratio was 84 and the modern ratio is near one. **The design difference that separated the X-13 from the XFY-1 has been dissolved rather than solved.**

**The endurance advantage is not what it looks like.** Twenty-three minutes against thirteen suggests the energy problem has nearly halved, and it has not.

The two vehicles obey different relations. A jet in the hover burns fuel in proportion to the thrust it must produce, so

$$t = \frac{\zeta}{c}$$

while a rotor's power is set by how hard it works the air it passes through,

$$\frac{P}{T} = \frac{v_{i}}{\eta}, \qquad v_{i} = \sqrt{\frac{T/A}{2\rho}}$$

and its endurance is the stored energy divided by that power,

$$t = \frac{\zeta_{b} \, e \, \eta}{g \, v_{i}}$$

The modern figures in the table assume a battery at thirty percent of the mass while the X-13's fuel was twenty-one. Holding the energy mass fraction equal, with an induced velocity of 14.1 metres per second,

$$t = \frac{0.208 \times 9.0 \times 10^{5} \times 0.70}{9.807 \times 14.1} = 948 \, \text{s} = 15.8 \, \text{min}$$

against the X-13's 13.4. **Seventy years of propulsion and energy storage has improved hovering endurance at fixed energy mass fraction by about eighteen percent.**

The comparison is cleanest expressed as an effective specific consumption. A jet in the hover obeys $t = \zeta / c$ and a rotor obeys the relation above, so the rotor's equivalent $c$ is

$$c_{\text{eff}} = \frac{g \, v_{i}}{e \, \eta}$$

| Configuration | Effective specific consumption | Relative to the Avon |
|---|---|---|
| Ryan X-13, Avon RA.28 | $2.583 \times 10^{-4}$ s⁻¹ | 1.000 |
| Small electric tail-sitter, 250 Wh/kg | $2.197 \times 10^{-4}$ s⁻¹ | 0.850 |
| The same at 400 Wh/kg | $1.373 \times 10^{-4}$ s⁻¹ | 0.532 |

**A battery forty-eight times worse than kerosene per kilogramme, driving a rotor seventeen times better than a jet at converting power into thrust, comes out fifteen percent ahead.** The rest of the modern advantage is bought by carrying more energy, which a vehicle with no pilot and no weapon can afford to do. **The hover is still expensive and it is expensive for the same reason.**

### The Tail-Sitter Came Back Without a Pilot

The transition control problem this article derives is now an ordinary subject with a large literature, and the vehicle it is written about is usually a biplane quadrotor tail-sitter, which is the X-13's configuration with four rotors in place of one jet and a computer in place of the man.

**Disturbance rejection through the hover and the transition together**, which the X-13's pilot had to manage by hand, is [Mao et al 2026][research_mao_2026] and [Wang et al 2025, Modeling and Attitude Disturbances][research_wang_2025_3]. Hover attitude control for exactly that configuration is [Wang et al 2026, Modeling and hover control of a bi][research_wang_2026_4] and [Wang et al 2026, Cascaded finite-time hovering atti][research_wang_2026_5], its transition feedback design is [Gupta et al 2026][research_gupta_2026], and its aerodynamics and acoustics are [Jayasundara and Baeder 2026][research_jayasundara_baeder_2026]. **The stability derivatives that the 1953 wind-tunnel programme measured for the XFY-1 are now obtained from the vehicle itself in flight**, in [Juhasz et al 2025][research_juhasz_2025] on system identification of a hovering quadrotor biplane tail-sitter.

Transition strategies and corridors are [Rehan et al 2026][research_rehan_2026], [Lee et al 2026][research_lee_2026], [Pobikrowska and Goetzendorf-Grabowski 2025][research_pobikrowska_goetzendorf_grabowski_2025], [Burton et al 2026][research_burton_2026], [Panish and Bacic 2025][research_panish_bacic_2025], [Xi et al 2025][research_xi_2025], [Tellez-Belkotosky et al 2025][research_tellez_belkotosky_2025], and [Irmawan et al 2023][research_irmawan_2023]. Adaptive and fault-tolerant versions, which matter because a rotor can fail where a jet mostly could not, are [Zhou et al 2025][research_zhou_2025], [Cai and Lovera 2026][research_cai_lovera_2026], and [Wang et al 2026, Adaptive sliding mode fault-tolera][research_wang_2026_6]. Configuration studies are [Samarth Pathak 2025][research_pathak_2025], [Liang et al 2026][research_liang_2026], [Rajendran 2025][research_rajendran_2025], and [Fernandez et al 2026][research_fernandez_2026], the last of which optimises the design and the trajectory together under a controllability constraint, which is the modern form of the question this article opens with.

### The Handover Is Now a Least-Squares Problem

**The control-authority handover is solved as an allocation problem.** A modern over-actuated aircraft is given a desired moment and solves for the actuator commands that produce it at least cost,

$$\mathbf{M}_{\text{des}} = B \mathbf{u}, \qquad \mathbf{u} = W^{-1} B^{\mathsf{T}} \left( B W^{-1} B^{\mathsf{T}} \right)^{-1} \mathbf{M}_{\text{des}}$$

where the weighting $W$ prices each actuator and the effectiveness matrix $B$ varies with dynamic pressure. **The blend that the X-13's pilot had to perform by hand is now the solution of that problem, evaluated many times a second**, and the fraction $\lambda(V)$ tabulated earlier is what it converges to.

The formulation for a vectored-thrust vertical take-off aircraft specifically is [Enenakpogbe et al 2025][research_enenakpogbe_2025], and treating the transition as a multi-objective allocation is [Asghari and Tayefi 2026][research_asghari_tayefi_2026]. The control laws that sit above it are [Scordamaglia et al 2025][research_scordamaglia_2025], [Pfeifle and Fichter 2023][research_pfeifle_fichter_2023], [Saetti 2025, Dynamic Inversion Flight Control L][research_saetti_2025_2], and [McIntosh et al 2024][research_mcintosh_2024]. Incremental nonlinear dynamic inversion, which has become the default because it needs less of a model than the alternatives, is [Tamaskani et al 2026][research_tamaskani_2026], [Wang et al 2026, Adaptive Augmentation of Increment][research_wang_2026_3], [Athayde et al 2024][research_athayde_2024], and [Salahudden et al 2024][research_salahudden_2024]. Nonlinear model predictive control on a large multirotor is [Zwiener et al 2026][research_zwiener_2026], on a tiltwing [Doff-Sotta et al 2025][research_doff_sotta_2025], and reconfiguration after an actuator failure is [Li et al 2025, Reconfigurable fault-tolerant atti][research_li_2025_3] and [Cai et al 2026, Incremental Model Predictive Attit][research_cai_2026_2].

### The Position Loop Became Somebody Else's Problem

This article's sharpest human-factors result is that hovering is a third-order position loop with no restoring moment, requiring the mean tilt to be held below half a degree to keep station within a metre. **That loop is now closed by a computer with better sensors than eyes.**

Station-keeping against disturbance is [Stewart et al 2026][research_stewart_2026], hover system identification is [Matt and Altamirano 2026][research_matt_altamirano_2026], and rotor-level health monitoring in the hover, which no 1957 aircraft could contemplate, is [Lovas 2026][research_lovas_2026]. The rotor aerodynamics underneath are [Mihaila et al 2026][research_mihaila_2026], [Mortimer et al 2026][research_mortimer_2026], and [Makeev 2026][research_makeev_2026].

**Where a human remains in the loop the article's transport-delay analysis has become a research subject in its own right**, in [Liu et al 2026, Delay-Aware Shared Control for Tel][research_liu_2026_2] on teleoperation under delay and [Li et al 2026, Design and evaluation of Avatar][research_li_2026_4] on driving the latency of an immersive interface down. **The ground observer who talked Girard onto the hook was an early and unusually literal instance of shared control with a transport delay**, and the modern treatment of that arrangement says the delay is the thing to attack.

### The Visual Task, Solved by Deleting the Viewer

The X-13's decisive difficulty was that the pilot could not see the trailer. The modern answer is not a better window.

Vision-based autonomous landing is [Qian et al 2026][research_qian_2026], [González-Tejeda et al 2026][research_gonzalez_tejeda_2026], [Ryu et al 2025][research_ryu_2025], [Yang et al 2025, Robust Online Predictive Visual Se][research_yang_2025_2], and [Zhang et al 2025, Image-based fixed-time visual serv][research_zhang_2025_3]. **Landing on a moving platform, which is harder than landing on a trailer and is the same problem**, is [de Paula et al 2026][research_paula_2026], [Zhou et al 2026, Research on Autonomous Uav Shipboa][research_zhou_2026_2], [Yuan et al 2024][research_yuan_2024], and [Comeau et al 2024][research_comeau_2024].

Where a pilot is retained, the answer is to give the information back rather than to improve the view, which is what the 1970s displays literature concluded and what [Newton et al 2024][research_newton_2024] measures for a head-worn display on approach. Operator workload and situational awareness for small uncrewed aircraft are [Stephenson et al 2026][research_stephenson_2026], and the training question is [Gonzalo 2026][research_gonzalo_2026]. **Every one of these is a way of removing the geometry the X-13 could not remove.**

### Handling Qualities Became Certification

The control-power criteria this article borrows were a research subject in the 1960s and are now a regulatory one, because somebody has to certify vertical take-off aircraft carrying passengers.

**Sizing an aircraft's control power directly against handling-qualities requirements is [Antonakis 2025][research_antonakis_2025]**, using control moment polytopes, which is the formal version of the argument this article makes with a single criterion and a single moment arm. Testing those qualities with uncertainty modelled explicitly is [Antonakis 2025, Reinforcement-learning-based aircr][research_antonakis_2025_2] and [Saetti and Rogers 2024][research_saetti_rogers_2024], applying the Cooper-Harper scale to a small uncrewed aircraft is [Ioannis and Ioannis 2026][research_ioannis_ioannis_2026], and building flight models credible enough to certify by simulation is [Favaro et al 2025][research_favaro_2025]. Slung loads, which reproduce the X-13's coupled attitude and position problem in another form, are [Wang and Chen 2024][research_wang_chen_2024].

**The most direct descendant of the X-13's pilot problem is simplified vehicle operations**, in which the aircraft is made easy enough that a person who is not a pilot can fly it. [Janetzko et al 2026][research_janetzko_2026] measures whether novices actually can. **The X-13 asked an experienced test pilot to do something at the edge of what a person can do, and the field's eventual answer was to change the aircraft rather than to train the person.** Workload measurement itself has moved to physiological instrumentation, in [Procházková and Juračka 2026][research_prochazkova_juracka_2026], [Xu et al 2026][research_xu_2026], and [Chen et al 2025, Correlation analysis of physiologi][research_chen_2025_3].

### Ground Effect Became a Civil Planning Problem

The disc-loading ratio of about a hundred between a jet and a rotor of the same span is why vertical landing on unprepared ground remains a rotorcraft capability. **What has changed is who is asking.** The X-13's ground loading was a military basing question and it is now a question about where a vertiport may be placed in a city.

The aerodynamics is [Greene 2020][research_greene_2020], [Sagaga and Lee 2025][research_sagaga_lee_2025], [Lee et al 2026, Aerodynamic effects of rotor-rotor][research_lee_2026_2], [Shirbhate et al 2025][research_shirbhate_2025], and [Georgiev 2025][research_georgiev_2025], with the energy consequence measured in flight in [Su et al 2024][research_su_2024]. Ingestion persists even at rotorcraft disc loadings, in [Li et al 2025, Sand Ingestion Behavior of Helicop][research_li_2025_2], and brownout is now simulated for another planet entirely in [Caprace et al 2025][research_caprace_2025]. The shipboard case with deck motion is [Sharma et al 2021][research_sharma_2021].

**The planning literature is the part that would have surprised the X-13's engineers.** Vertiport siting and design are [Li et al 2026, Urban air mobility vertiports][research_li_2026_2], [Lyu and Feng 2026][research_lyu_feng_2026], [Maksoud et al 2025][research_maksoud_2025], [Mercan et al 2025][research_mercan_2025], [Guo et al 2025][research_guo_2025], [Zhou et al 2026][research_zhou_2026], [Jin and Ma 2025][research_jin_ma_2025], and [Mirković et al 2026][research_mirkovic_2026], with operations in [Lee et al 2025, Efficient Urban Air Mobility Verti][research_lee_2025_2] and the navigation requirement in [García Crespillo et al 2024][research_crespillo_2025]. **A tail-sitting jet needed a prepared surface and a particular trailer, which was held against it. A modern vertical take-off aircraft needs a prepared surface and a licensed site, and that is treated as infrastructure rather than as a defect.** The requirement did not go away. The expectation did.

### Sizing Now Carries the Hover Explicitly

The article's central arithmetic is that hover endurance depends only on the energy fraction and the effective consumption. **Every modern sizing method carries that term explicitly, because it dominates.**

Sizing methodologies are [Qiao and Zhou 2026][research_qiao_zhou_2026], [Lee et al 2022][research_lee_2022], [Chen et al 2026][research_chen_2026], [Paek 2025][research_paek_2025], and [Park et al 2025][research_park_2025]. Endurance relations rewritten for hybrid propulsion are [Batra et al 2024][research_batra_2024] and [Barufaldi and Morales 2023][research_barufaldi_morales_2023]. **The honest response, which is to carry a second energy source so the vehicle does not hover on its cruise powerplant, is now a design discipline**, in [Vegh 2025][research_vegh_2025], [Park 2026][research_park_2026], [Park and Park 2026][research_park_park_2026], [Li and Jiang 2026][research_li_jiang_2026], [Zhu et al 2022][research_zhu_2022], and [Radmanesh 2026][research_radmanesh_2026]. Energy-optimal trajectories exist because the hover is worth avoiding, in [Mathur and Atkins 2026][research_mathur_atkins_2026], [Cai et al 2026][research_cai_2026], and [Kang et al 2025][research_kang_2025], and the battery's own behaviour under that duty cycle is [Ayyaswamy et al 2023][research_ayyaswamy_2023], [Boggan and Clarke 2026][research_boggan_clarke_2026], and [Jiao and Yang 2026][research_jiao_yang_2026].

### The Slipstream Question, Now a Free Parameter

This article's explanation of why a turboprop tail-sitter needs no reaction control is that its slipstream gives the wing stall-level dynamic pressure in the hover. The relation is

$$q_{s} = \tfrac{1}{2} \rho v_{s}^{2} = \frac{T}{A}$$

so a designer who wants that condition simply chooses a disc loading equal to the wing loading, which the table at the head of this section shows a modern tail-sitter does automatically.

Shaping the interaction deliberately is [Xue and Zhou 2020][research_xue_zhou_2020], [Leng et al 2020][research_leng_2020], [Duivenvoorden et al 2026][research_duivenvoorden_2026], [Duivenvoorden et al 2025][research_duivenvoorden_2025], [Cao et al 2023][research_cao_2023], [Meng et al 2023][research_meng_2023], [Zhao et al 2024][research_zhao_2024], [Zhao et al 2026][research_zhao_2026], and [Ikami et al 2021][research_ikami_2021], with the propulsion-aerodynamics coupling modelled in [Li et al 2026][research_li_2026]. **The X-13's disadvantage against the XFY-1 is now a design choice that distributed electric propulsion makes freely available**, and it is the single largest change between the period and the present.

### High Angle of Attack, Which Is Where a Tail-Sitter Lives

A transitioning aircraft passes through every incidence from zero to ninety degrees. Modelling that is [Wang et al 2025][research_wang_2025] and [Golmirzaee and Wood 2026][research_golmirzaee_wood_2026], the unsteady interactions are [Koch 2026][research_koch_2026], [Acher et al 2021][research_acher_2021], and [Combey et al 2026][research_combey_2026], and the engine's own tolerance of incidence, which the X-13 needed and nobody measured, is [Mohankumar et al 2021][research_mohankumar_2021] and [Mohankumar et al 2022][research_mohankumar_2022].

### Subscale Free Flight Is Still How It Is Done

The Froude-scaled free-flight model that settled the X-13's transition is not a superseded technique. **It is how a transitioning aircraft is still tested before it carries anything.**

Scaled demonstrators and their development are [Pan et al 2026][research_pan_2026] and [Bianco and Simon 2023][research_bianco_simon_2023], flight testing a trajectory controller on a subscale transitioning aircraft is [Comer et al 2026][research_comer_2026], and the identification work that turns such a flight into a model is [Ahmed et al 2025][research_ahmed_2025], [Shen and Chen 2025][research_shen_chen_2025], [Abdul Rashid et al 2025][research_rashid_2025], and [Ide and Landman 2025][research_ide_landman_2025]. **The difference from 1958 is that the model now carries the flight computer it is testing**, so the thing being validated is the software rather than the shape, and the Reynolds number mismatch this article computes matters less than it did because the quantity of interest is a control law rather than a stall. Safety and certification lessons drawn from such vehicles are [Filippoli et al 2026][research_filippoli_2026] and [Kieß et al 2026][research_kie_2026], and the noise a full-scale one makes is [Pascioni et al 2026][research_pascioni_2026] and [Lee et al 2025][research_lee_2025].

### What Has Not Changed

Three of the article's findings have no modern remedy and appear unchanged in the current literature.

**Hovering is expensive**, and the effective specific consumption table above shows the improvement over seventy years is about fifteen percent at fixed energy fraction. **Ground loading scales with disc loading**, so any vehicle that hovers on a small actuator disc will damage what it hovers over. **And a hovering aircraft has no aerodynamic restoring moment**, so the position loop is third order and undamped whether a person or a computer is closing it.

**What changed is who closes the loop, how much energy the vehicle can afford to carry, and whether the ground is expected to be prepared.** None of those is an aerodynamic advance, and the X-13's aerodynamics were never the problem.

## Where the Framing Breaks Down

**The control-power criteria are borrowed from later work.** The half a radian per second squared in pitch and one in roll used throughout are figures the field settled on after the X-13 flew, and applying them to the X-13 is anachronistic. It is done here because they are the best available statement of what adequate means, and because the article's conclusion, that the crossover falls well below the stall speed, survives a large error in the criterion, since the ratio grows only as its square root and would reach one only if the criterion were three times larger.

**The control criteria fit the X-13 better in one respect than their date suggests**, since they were written for aircraft with automatic stabilisation and the X-13 had it. [Friend 1964][research_friend_1964] and [Hoffman 1971][research_hoffman_1971] both size reaction control against a stabilised airframe, and the X-13 flew with pitch and yaw dampers and a stability augmentation system, which the [Smithsonian record][ref_nasm_x13] records and the model tests of [Smith 1958, Hovering and Transition Flight Tes][research_smith_1958_2] show to have been necessary.

**The elevon and aileron effectiveness figures are assumed.** A pitching-moment increment of 0.10 and a rolling-moment increment of 0.05 are plausible for a tailless delta and are not measured values for this aircraft. They are referred to the geometric mean chord of 2.77 metres, while the mean aerodynamic chord that [Bowman 1957][research_bowman_1957] tabulates is 145.49 inches, or 3.70 metres, so what is assumed is the product of chord and coefficient. The crossover speed varies as the inverse square root of the assumed effectiveness,

$$V_{\text{cross}} \propto (\Delta C_{m})^{-1/2}$$

so the exposure is direct.

| Elevon effectiveness relative to the assumption | Crossover speed | Ratio to stall |
|---|---|---|
| half | 42.6 m/s | 0.813 |
| three quarters | 34.8 m/s | 0.663 |
| as assumed | 30.2 m/s | 0.575 |
| one and a half times | 24.6 m/s | 0.469 |
| twice | 21.3 m/s | 0.406 |

**If the elevons were half as effective as assumed the crossover would still sit nearly a fifth below the stall speed**, and the central claim would invert only if they were less than a third as effective as assumed, since the ratio grows as the inverse square root of the effectiveness and $0.575^{2} = 0.33$. That remains the single largest exposure in the analysis and it rests on a coefficient nobody measured for this aircraft.

**The fuel figure is derived from tabulated loadings, not reported as a capacity.** The 1,400 pound fuel load follows from the differences between the full, quarter and twentieth fuel loadings of the spin-tunnel table, which agree exactly, but those are loadings possible on the airplane rather than measured ones, and no document found states a tank capacity. The thirteen minute hover endurance moves in direct proportion.

**The control-power criteria have themselves been contested throughout.** Treating them as settled is a convenience. [Carpenter and Jenny 1964][research_carpenter_jenny_1964] approaches low-speed control criteria statistically, [Goldberger 1966][research_goldberger_1966] argues about the relative importance of the requirement at all, and the longitudinal criteria were still being evaluated and re-evaluated in [Gertsen and Shomber 1965][research_gertsen_shomber_1965], [Martin 1963, Investigation Of Longitudinal Hand][research_martin_1963_2], and [Eney 1967][research_eney_1967]. **A number this article uses as though it were a physical constant was an active dispute for two decades**, and the later synthesis in [Anderson 1979][research_anderson_1979] is measuring a real aircraft against requirements that had by then changed several times.

**The hover analysis assumes a rigid aircraft and a still atmosphere separately, and the real case is neither.** The drift table and the crosswind table are computed independently and then discussed together, which is not the same as solving them together. A pilot correcting a wind-induced drift is holding a tilt that is itself producing drift, and the coupled problem is what the handling-qualities literature actually measures.

**The side area and drag coefficient in the crosswind table are guesses.** Ten square metres and 0.8 are plausible for a vertical aircraft of this size and are not derived from its geometry, and the forces scale directly with both.

**Treating the programme as a failure of concept understates the demonstration.** The aircraft did what it was built to do, and both examples survived it. An article organised around why the idea did not proceed can read as though the vehicle did not work, and it worked.

## What the X-13 Was Worth

**It established that a pure jet can complete the cycle.** This was genuinely open when the Air Force contract was let and closed in 1957, and no aircraft since has needed to ask it again.

**It established that the control handover is clean for this configuration.** The crossover computed above is a prediction and the flight is the confirmation.

**It established the shape of the operational objection.** The fuel, the pilot's sight line, and the ground loading are all visible in the X-13's own numbers, and a programme that had gone to a prototype fighter would have discovered them more expensively.

**It established nothing about combat capability**, and the aircraft carried nothing.

**It did not establish that the configuration is a bad idea.** The idea returned as soon as the pilot could be removed from it, which is the correct reading of what the X-13 actually proved.

## The Designation, Which Returns to Normal

For five consecutive articles this series has recorded a designation attached to something that was not a research aircraft. **The X-13 ends that run.** It is a manufacturer's prototype built in two examples under a research contract, flown by company test pilots, with no operational intent and no production plan, which is the pattern the [X-1][related_post_a298_bell_x1] established and the [X-3][related_post_a300_douglas_x3] and [X-5][related_post_a302_bell_x5] continued.

That matters for the argument the closing article of this series will have to make. **The run of five was an interruption and not a redefinition.** Whatever mechanism attached X numbers to the [X-8][related_post_a305_aerojet_x8] through the [X-12][related_post_a309_convair_x12], it did not replace the original one, and the two coexisted. A closing article that describes the series as having drifted from research aircraft to weapons would be contradicted by its own next entry.

## The Source Base

**The X-13's own record is thin and its family's record is thick.** Querying the technical archive of the National Aeronautics and Space Administration, NASA, for the popular name returns nothing at all, and querying for the manufacturer and designation together returns a small set, of which the spin tunnel series and the one-fifth-scale hovering and transition tests are the substance. **The lesson is the same one the [X-10][related_post_a307_north_american_x10] taught in a different form**, which is that a vehicle is indexed under the name its engineers used and not the name the public learned.

Around that thin core sits an unusually complete literature on the configuration class, because the Navy's two propeller tail-sitters were studied exhaustively at Langley before either flew. **An article about the X-13 is therefore better supported than an article about the X-13 alone would be**, and most of the aerodynamic statements here rest on documents about the XFY-1 and the XFV-1. The exceptions are the airplane's own dimensions, loadings and moments of inertia, which come from the tables of [Bowman 1957][research_bowman_1957], and the roll-nozzle geometry, which comes from the one-fifth model of [Smith 1958, Hovering and Transition Flight Tes][research_smith_1958_2].

**The aircraft's own history rests on institutional records.** The [Smithsonian record][ref_nasm_x13], the [Air Force museum's fact sheet][ref_nmusaf_x13] and [NASA's inventory of X-vehicles][ref_american_x_vehicles] are the sources for the programme's dates, and they disagree about the Washington demonstration and the last flight, as the flight test record notes. The Smithsonian record lists a curatorial file and a 2002 magazine history among its sources, and neither is available here.

The contrast with the [X-11][related_post_a308_convair_x11] and [X-12][related_post_a309_convair_x12] is instructive. Those vehicles left a thick archive because they became launch vehicles and flew for sixty years. The X-13 left almost nothing because it stopped, and what survives is the research literature of the question rather than the engineering record of the article.

**A third asymmetry is worth naming because it runs the other way from the previous two articles.** The Atlas record is thick and classified, and the geodesy the Atlas depended on is thick and open. The X-13's record is thin and open, and there is no classified layer underneath it, because a two-aircraft demonstration programme with no weapon and no production intent generated nothing worth withholding. **The whole of what is knowable about this aircraft is knowable**, which is not true of any vehicle in the five that precede it, and it makes the X-13 the easiest article in this run to verify and the hardest to say anything new about.

The defence archive contributes little here and that absence is itself informative. Querying it returns work on vertical take-off as a concept, on site preparation, and on handling qualities criteria, in [Butler and Thomas 1964][research_butler_thomas_1964], [Irvin and Swan 1956][research_irvin_swan_1956], [Boeing Co Morton Pa Vertol Div 1956][research_div_1956], [Friend 1964][research_friend_1964], [Hoffman 1971][research_hoffman_1971], and [Johnston et al 1965][research_johnston_1965], and it returns nothing at all about this airframe. **The Air Force studied the idea and the Navy's laboratories studied the aerodynamics and Ryan built the aeroplane**, and only the middle of those three left a public record of the vehicle itself.

**The shape of the surviving literature is worth one more observation, because it inverts the usual complaint.** Almost nothing in this article rests on a document about the X-13. It rests on documents about the configuration, the flight condition, the test technique, and the pilot's task, written before and after the aircraft flew and mostly about other aircraft. **An article about a vehicle with almost no record of its own can still be dense, provided the question it asked was one other people were also asking.** That is true of the X-13 and it was not true of the [X-10][related_post_a307_north_american_x10], whose keystone was peculiar to a cancelled programme, and the difference is a property of the question rather than of the archive.

**The research survey admits a record only when a person reading its title finds it on this article's subject**, which here means the aircraft, its configuration class, the flight condition, the test technique or the pilot's task. Its 318 records come from NASA's Technical Reports Server, the Defense Technical Information Center and the journal literature indexed by Crossref, and every one of them is cited in a sentence of the body. Of these, 44.0 percent are report-server records, and their median year is 1975. Records that are not works are excluded, meaning figures, tables, supplementary files, peer-review reports, notices of erratum, correction, retraction or withdrawal, and journal front matter, because a survey counts research works and those are parts of works or editorial events.

**A few records of doubtful relevance are kept because each supports a specific claim.** Two studies of teleoperation under communication delay are cited for the transport-delay reading of the ground observer, a study of C-141A ground flotation on landing mats for the bearing capacity of a prepared surface, and a study of C-5A bogie pitching control for the control problems of a conventional undercarriage.

**Every research title has been read for relevance and none was found outside the subject**, so the off-topic share that remains is a matter of reading judgement, although a reading of titles alone cannot rule out a work whose title is on topic and whose content is not.

## Epistemic State

**Historical fact, well supported.** Two X-13 aircraft were built by Ryan, serials 54-1619 and 54-1620. The Navy Bureau of Aeronautics contracted Ryan in 1947 to study vertically launched jet fighters, and a jet test rig made the first manned jet hovering flight on 24 November 1953. The powerplant is a Rolls-Royce Avon of 10,000 pounds thrust. The first conventional flight was 10 December 1955, the first vertical take-off and landing 28 May 1956, the first transition 28 November 1956, and the first complete cycle from the trailer 11 April 1957. The second aircraft was demonstrated at the Pentagon in July 1957. Pitch and yaw control in hover came from vectored engine thrust and roll control from bleed-air jets at the wingtips, and the aircraft flew with pitch and yaw dampers and a stability augmentation system. The pilot's seat pivoted forty-five degrees. The aircraft launched from and recovered onto a cable on a tilting trailer using a nose hook, with a ground observer talking the pilot down and a graduated pole on the trailer as a distance reference. Both aircraft survive, 54-1619 with the San Diego Air and Space Museum on loan from the Smithsonian and 54-1620 at the National Museum of the United States Air Force. The airplane's span, length, wing area and mean aerodynamic chord, its tabulated loadings and its moments of inertia are those of the Langley spin-tunnel reports, which also find that it would not tumble end over end, that a power failure in the hover leads to a spin, and that about 4,200 feet are needed to recover. The one-fifth model needed pitch and yaw dampers to hover once the engine's gyroscopic effect was represented, and showed a rolled and sideslipped trim between about 25 and 45 degrees angle of attack.

**Reported, with sources in disagreement.** The Air Force contract year, July 1954 in the Smithsonian record and 1953 in compilations. The date of the Washington demonstration, 30 July 1957 in the Smithsonian record and 28 and 29 July in a compilation. The last flight, 30 September 1957 in the Smithsonian record and 30 July 1957 in NASA's inventory. The engine designation, RA.28-49 in the Smithsonian record and R.A. 14 in the spin-tunnel report. The reason the programme ended, which is funding and limited operational potential in the two museum records, size, payload and the lack of a larger engine in NASA's inventory, and the absence of an operational requirement in a compilation. The gross weight, 6,730 pounds in compilations against 6,696 and 6,958 pounds in the spin-tunnel loadings, 7,313 pounds in the Smithsonian record and a 7,200 pound maximum in the Air Force museum's.

**Reported in compilations and museum records but in no programme document found.** The company designation Model 69 and the F3R designation. The 15 feet 2 inches height. The 5,334 pound empty weight. The identification of the test pilots. The statement that the first transitions were flown at altitude.

**Assumed for the purpose of calculation and stated as such.** The specific fuel consumption of 0.93 pounds per pound of thrust per hour, which is a figure quoted for an Avon variant rather than for the RA.28. The maximum lift coefficient of 1.0. The elevon pitching-moment increment of 0.10, the aileron rolling-moment increment of 0.05, and the rudder yawing-moment increment of 0.06, all referred to the geometric mean chord or the span. The control power criteria of 0.5, 1.0, and 0.3 radians per second squared in pitch, roll, and yaw. The full-scale roll-nozzle arm of 10.16 feet, scaled from the one-fifth model. The battery specific energy of 250 watt-hours per kilogramme, the battery mass fraction of thirty percent assumed for the modern reference vehicles and of 0.208 chosen to match the X-13's fuel fraction in the equal-fraction comparison, and the rotor figure of merit of 0.70 used in the electric comparison. The independent success probability of 0.8 used to illustrate the value of testing in sequence. The 3.5 metre nozzle moment arm. The engine mass flow of 70 kilogrammes per second and exhaust density of 0.35 kilogrammes per cubic metre. The bleed velocity of 500 metres per second. The cruise speed of 200 metres per second and lift-to-drag ratio of six. The 1,500 pascal disc loading taken as representative of the XFY-1 class. The ten square metre side area and drag coefficient of 0.8 for the crosswind case. The one second engine spool time. The 0.3 metre hook tolerance and the closure rates used against it. The undercarriage weight fraction of three to five percent of gross used for the table, which the spin-tunnel loadings place at 3.8 percent. The 0.3 metre arresting stroke.

**Engineering analysis, derived here and independently checkable.** The fuel load of 1,400 pounds from the differences between the tabulated loadings, and the 224 pounds by which the wheeled zero-fuel weight exceeds the published empty weight. The pitch, roll and yaw inertias of 5,480, 2,092 and 6,553 kilogramme square metres converted from the tabulated values. The distinction between the equal-authority crossing at 94.7 metres per second and the adequacy crossing at 30.2, and the table of the aerodynamic share of available authority showing that at the adequacy crossing the elevons still supply only about a tenth of what is there. The vanishing of the nozzle's rolling moment as a cross-product identity rather than an approximation. The linear growth of required over available control moment with size, and the resulting bleed fractions of 1.9, 3.9, and 5.8 percent at one, two, and three times scale. The crossover sensitivity table showing that halving the assumed elevon effectiveness moves the ratio only to 0.813, and that the ratio reaches one only below a third of the assumed effectiveness. The pitch-rotation table, giving 0.20 seconds and 5.8 degrees of arc at one radian per second with the engine running. The full-scale engine angular momentum of about 16,200 kilogramme square metres per second scaled from the model flywheel, and the gyroscopic yawing moment of 1,615 newton metres at a pitch rate of 0.1 radians per second. The sum of 4,200 feet for recovery after a flame-out in the hover, and the 680 feet that free fall over the stated 6.5 seconds gives against the report's 900. The Froude scaling relations and the one-fifth model table, giving 23.5 metres per second, 2.19 seconds, 25.6 metres, and 24.4 kilogrammes, with a Reynolds number 11.2 times lower, and the model's weight at 0.73 of the scaled value. The undercarriage saving expressed as hover time, at 1.94 to 3.22 minutes across the assumed range and 2.51 minutes for the tabulated 262 pounds. The sight-line relation and the finding that the landing point bears 135 degrees from the tail-sitter pilot against about 45 for a horizontal jet-lift aircraft. The height-loss relation and its table. The steady tilt required to hold station in a crosswind, at 0.94 degrees in ten metres per second against a drift budget of 0.47. The observation that a disc loading equal to the wing loading of 1,687 pascals puts stall-level dynamic pressure on the controls in a hover. The 1,966 newton metre yaw requirement, the 0.72 degree nozzle deflection that meets it, the 21.7 metre per second rudder crossover, and the resulting table showing that the three axes hand over in sequence at 0.41, 0.47, and 0.57 of the stall speed. The hover drift table and the finding that holding position to a metre over five seconds requires holding the mean tilt below half a degree. The crosswind force table and the finding that a ten metre per second wind is 17.9 percent of the pitch requirement as a moment and 72 metres of drift in thirty seconds as a position error. The vertical acceleration and thrust-change table and the asymmetry between bounded upward and unbounded downward authority. The loop-delay relation and the finding that 0.3 seconds consumes the whole hook tolerance at one metre per second. The sortie fuel table showing a cautious profile spending 44.7 percent of the fuel. The undercarriage weight table and the 19.2 percent of fuel load a four percent gear would have cost. The arresting deceleration of 0.17 gravities at one metre per second over 0.3 metres. The scaling of disc loading as the first power of length. The control power cost of about 193 pounds of thrust and its six percent of the hover margin. The lift coefficient sensitivity table for the crossover ratio. The nozzle deflection table. The thrust-to-weight ratios at gross and maximum weight, the vertical acceleration, and the time and speed at thirty metres. The aspect ratio, mean chord, and wing loading. The hover fuel flow of 104.3 pounds per minute and the resulting endurance of 13.4 minutes. The stall speed of 52.5 metres per second and its sensitivity to the lift coefficient. The pitch requirement of 2,740 newton metres. The aerodynamic pitching moment relation and its coefficient of 3.013. The crossover speed of 30.2 metres per second, its ratio of 0.575 to the stall speed, and the argument that the ratio is independent of aircraft size. The vectored thrust moments and the margin of 9.87 over the criterion. The axial thrust loss with nozzle deflection. The puffer force of 338 newtons, its 1.5 percent of thrust, and the 1.9 percent bleed. The aileron crossover at 24.5 metres per second and its ratio of 0.47 to the stall speed. The maximum transition tilt of 47.7 degrees, the horizontal acceleration of 10.78 metres per second squared, the 4.9 second and 128 metre transition, the 12.6 pounds of fuel, and the tilt table. The propeller slipstream velocity of 49.5 metres per second and its comparison with the stall dynamic pressure. The Breguet range and radius, and the table charging hover time against radius. The exhaust velocity, dynamic pressure, nozzle area, and the disc loading ratio of 102 against a rotor of the same span. The intervals of 170, 184 and 134 days, which sum to the 488 days from first flight to full cycle.

**Inference, argued but not established.** That the near equality between the X-13's thirteen and a half minutes of hovering and the 15.8 minutes an electric rotorcraft manages at the same energy mass fraction reflects two large factors largely cancelling, a battery forty-eight times worse per kilogramme and a rotor seventeen times better at converting power into thrust, rather than anything deeper, which the arithmetic shows and which no source states. That the three-axis handover sequence would have been perceptible to the pilot as the aircraft becoming conventional one axis at a time, which the relations imply and which no pilot report found here describes. That deleting the undercarriage was a deliberate performance decision rather than only a consequence of the launch method. That the ground observer is best understood as a delayed sensor inside the control loop, which is this article's framing and not the period's. That the control crossover falling well below the stall speed is what makes the configuration workable rather than a fortunate accident. That the published empty weight of 5,334 pounds describes the aircraft on wheels. That the fuel arithmetic, the pilot's sight line, and the ground loading are the operative reasons the concept did not proceed, which the numbers support but which no document found here states in those terms. That the programme's ground testing addressed the wrong difficulty because the difficulty was not aerodynamic. That the return of the vertical-attitude concept as a remotely piloted vehicle is a recognition that the pilot was the binding constraint.

**Engineering analysis of the modern comparison, derived here and independently checkable.** The three modern reference vehicles and their disc loadings, wing loadings, ratios, and hover endurances. The finding that a small electric tail-sitter's disc loading and wing loading are the same quantity to within a factor of two, against the X-13's ratio of 84. The effective specific consumption relation for a rotor, its evaluation at 250 and 400 watt-hours per kilogramme, and the comparison with the Avon showing the modern vehicle fifteen percent ahead. The endurance of 15.8 minutes at the X-13's own energy mass fraction against its 13.4, an improvement of about eighteen percent. The decomposition into a battery forty-eight times worse per kilogramme and a rotor seventeen times better at converting power into thrust.

**A caution about the modern reference vehicles.** The three vehicles in the comparison table are representative rather than actual. Their masses, spans, wing areas, rotor counts, and rotor diameters were chosen as plausible for their classes and are not taken from any specific aircraft, and the battery specific energy of 250 watt-hours per kilogramme and figure of merit of 0.70 are likewise estimates. **The conclusions drawn from them are ratios and orders and are insensitive to reasonable variation, and the specific endurances are not.**

**Written from current knowledge.** This article is dated 2025-10-19 and draws on literature published after that date where the modern discussion continues the period problem.

## Out of Scope

The Convair XFY-1 and Lockheed XFV-1 as programmes in their own right, which are used here only as the configuration comparison. The Ryan FR-1 Fireball. The submarine-launched fighter concept the 1947 study addressed. The Rolls-Royce Avon as an engine programme. The later jet-lift aircraft, the Hawker P.1127 line, and the lift-fan configurations, which solved the same problem a different way and belong with the aircraft that carry those designations. The X-14, which is the next article and which established the control criteria used here. Carrier and shipboard operation. The aerodynamics of the delta wing at high angle of attack in any depth. The remotely piloted vertical-attitude proposals of the 1970s beyond noting that they exist.

## Conclusion

The X-13 was built to find out whether a jet could take off vertically, become an aeroplane, become a hovering machine again, and land on the spot it left. **It could, and both aircraft survived the programme.**

The reason it worked is an ordering that is not an accident. Aerodynamic control authority grows as the square of speed and vectored thrust does not depend on speed at all, so the two hand over exactly once, and for this aircraft the handover falls at 30 metres per second against a stall speed of 52. **The control surfaces start working at well under three fifths of the speed at which the wing starts working**, so there is no band in which the aircraft is flying and cannot be pointed. That ratio is a property of the configuration rather than of the size, which is why the layout has outlived the aeroplane.

The reason it led nowhere is arithmetic of a different kind. **The entire fuel load is thirteen minutes of hovering**, the transition that the programme existed to demonstrate costs twelve pounds of it, and the hovering at either end costs everything else. A minute at each end takes a sixth of the radius. The exhaust loads the ground a hundred times harder than a helicopter of the same span, so the aircraft needs a prepared surface and a particular trailer. And the pilot cannot see the hook he is aiming at.

**Each of those is a reason the concept did not become a fighter, and none of them is a reason the aircraft failed.** The X-13 answered its question completely and the answer was that the question had been the wrong one to ask about a manned aeroplane. Two decades later the same configuration came back with nobody in it, and it is now the ordinary way to build a small aircraft that has to take off from somewhere without a runway.

## References

### Books

- [Jenkins Landis and Miller 2003 American X-Vehicles, An Inventory X-1 to X-50][book_jenkins_landis_miller_2003]
- [Miller 2001 The X-Planes, X-1 to X-45][book_miller_2001]
- [Rogers 1989 VTOL, Military Research Aircraft][book_rogers_1989]

[book_jenkins_landis_miller_2003]: https://openlibrary.org/works/OL20394726W
[book_miller_2001]: https://openlibrary.org/works/OL7006680W
[book_rogers_1989]: https://openlibrary.org/works/OL4784139W

### Reference

- [American X-Vehicles, An Inventory X-1 to X-50, SP-2003-4531][ref_american_x_vehicles]
- [National Air and Space Museum, Ryan X-13 Vertijet, A19600018000][ref_nasm_x13]
- [National Museum of the United States Air Force, Ryan X-13 Vertijet][ref_nmusaf_x13]
- [Ryan X-13 Vertijet][ref_x13]

[ref_american_x_vehicles]: https://www.nasa.gov/wp-content/uploads/2023/04/sp-4531.pdf
[ref_nasm_x13]: https://airandspace.si.edu/collection-objects/ryan-x-13-vertijet/nasm_A19600018000
[ref_nmusaf_x13]: https://www.nationalmuseum.af.mil/Visit/Museum-Exhibits/Fact-Sheets/Display/Article/195753/ryan-x-13-vertijet/
[ref_x13]: https://en.wikipedia.org/wiki/Ryan_X-13_Vertijet

### Related Post

- [X-1][related_post_a298_bell_x1]
- [X-10][related_post_a307_north_american_x10]
- [X-11][related_post_a308_convair_x11]
- [X-12][related_post_a309_convair_x12]
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

### Research

- [Acher et al 2021][research_acher_2021]
- [Adams 1972][research_adams_1972]
- [Ahmed et al 2025][research_ahmed_2025]
- [Anderson 1960][research_anderson_1960]
- [Anderson 1979][research_anderson_1979]
- [Antonakis 2025][research_antonakis_2025]
- [Antonakis 2025, Reinforcement-learning-based aircr][research_antonakis_2025_2]
- [Aoyagi and Tolhurst 1964][research_aoyagi_tolhurst_1964]
- [Asghari and Tayefi 2026][research_asghari_tayefi_2026]
- [Ashkenas 1965][research_ashkenas_1965]
- [Athayde et al 2024][research_athayde_2024]
- [Ayyaswamy et al 2023][research_ayyaswamy_2023]
- [Barufaldi and Morales 2023][research_barufaldi_morales_2023]
- [Barzda 1966][research_barzda_1966]
- [Batra et al 2024][research_batra_2024]
- [Baxter and Finvold 1958][research_baxter_finvold_1958]
- [Beale and Miller 1975][research_beale_miller_1975]
- [Behan and Siciliani 1965][research_behan_siciliani_1965]
- [Behan and Siciliani 1967][research_behan_siciliani_1967]
- [Bennett 1947][research_bennett_1947]
- [Bianco and Simon 2023][research_bianco_simon_2023]
- [Bihrle and Bowman 1980][research_bihrle_bowman_1980]
- [Binion 1970][research_binion_w_1970]
- [Blanchard 1981][research_blanchard_1981]
- [Boggan and Clarke 2026][research_boggan_clarke_2026]
- [Bowman 1955][research_bowman_1955]
- [Bowman 1955, Emergency Spin-Recovery Device for][research_bowman_1955_2]
- [Bowman 1957][research_bowman_1957]
- [Brown 1965][research_brown_1965]
- [Burk and Wilson 1975][research_burk_wilson_1975]
- [Burnell et al 1973][research_burnell_1973]
- [Burton et al 2026][research_burton_2026]
- [Butler and Thomas 1964][research_butler_thomas_1964]
- [Cai and Lovera 2026][research_cai_lovera_2026]
- [Cai et al 2026][research_cai_2026]
- [Cai et al 2026, Incremental Model Predictive Attit][research_cai_2026_2]
- [Campbell 1962][research_campbell_1962]
- [Cao et al 2023][research_cao_2023]
- [Caprace et al 2025][research_caprace_2025]
- [Carmichael and McNay 1961][research_carmichael_mcnay_1961]
- [Carpenter and Jenny 1964][research_carpenter_jenny_1964]
- [Chaloff et al 1974][research_chaloff_1974]
- [Chen et al 2025, Correlation analysis of physiologi][research_chen_2025_3]
- [Chen et al 2026][research_chen_2026]
- [Christiansen 1984][research_christiansen_1984]
- [Clark 1964][research_clark_1964]
- [Clark and Spurlin 1962][research_clark_spurlin_1962]
- [Clark et al 1963][research_clark_1963]
- [Combey et al 2026][research_combey_2026]
- [Comeau et al 2024][research_comeau_2024]
- [Comer et al 2026][research_comer_2026]
- [Cook 1964][research_cook_1964]
- [Corliss et al 1977][research_corliss_1977]
- [Crandall et al 1973][research_crandall_1973]
- [García Crespillo et al 2024][research_crespillo_2025]
- [Davidson et al 1972][research_davidson_1972]
- [Davis and Spicer 1965][research_davis_spicer_1965]
- [Denning 1962][research_denning_1962]
- [Dent 1966][research_dent_1966]
- [Boeing Co Morton Pa Vertol Div 1956][research_div_1956]
- [Division 1966][research_division_1966]
- [Doff-Sotta et al 2025][research_doff_sotta_2025]
- [Donaldson et al 1966][research_donaldson_1966]
- [Donaldson et al 1971][research_donaldson_1971]
- [Dougherty 1966][research_dougherty_1966]
- [Douglass 1963][research_douglass_1963]
- [Drinkwater and Rolls 1962][research_drinkwater_rolls_1962]
- [Drinkwater and Rolls 1965][research_drinkwater_rolls_1965]
- [Drinkwater et al 1965, Effects of lateral control charact][research_drinkwater_1965_2]
- [Duivenvoorden et al 2025][research_duivenvoorden_2025]
- [Duivenvoorden et al 2026][research_duivenvoorden_2026]
- [Eatough 1971][research_eatough_1971]
- [Eilertson 1975][research_eilertson_1975]
- [Enenakpogbe et al 2025][research_enenakpogbe_2025]
- [Eney 1967][research_eney_1967]
- [Erwin et al 1964][research_erwin_1964]
- [Evans et al 1974][research_evans_1974]
- [Farris et al 1983][research_farris_1983]
- [Favaro et al 2025][research_favaro_2025]
- [Fernandez et al 2026][research_fernandez_2026]
- [Filippoli et al 2026][research_filippoli_2026]
- [Foltz 1962][research_foltz_1962]
- [Friend 1964][research_friend_1964]
- [Garren 1961][research_garren_1961]
- [Garren et al 1965][research_garren_1965]
- [Gentry and Margason 1966][research_gentry_margason_1966]
- [George et al 1964][research_george_1964]
- [Georgiev 2025][research_georgiev_2025]
- [Gerdes 1964][research_gerdes_1964]
- [Gerhardt and Chen 1978][research_gerhardt_chen_1978]
- [Gertsen and Shomber 1965][research_gertsen_shomber_1965]
- [Gold and Walchli 1974][research_gold_walchli_1974]
- [Goldberger 1966][research_goldberger_1966]
- [Golmirzaee and Wood 2026][research_golmirzaee_wood_2026]
- [Gonzalo 2026][research_gonzalo_2026]
- [González-Tejeda et al 2026][research_gonzalez_tejeda_2026]
- [Grafton and Anglin 1975][research_grafton_anglin_1975]
- [Grahame 1968][research_grahame_1968]
- [Grahame 1969][research_grahame_1969]
- [Greene 2020][research_greene_2020]
- [Grether 1973][research_grether_1973]
- [Guo et al 2025][research_guo_2025]
- [Gupta and Bryson 1976][research_gupta_bryson_1976]
- [Gupta et al 2026][research_gupta_2026]
- [Hafer and Skinner 1960][research_hafer_skinner_1960]
- [Hargraves 1961][research_hargraves_1961]
- [Harper 1955][research_harper_p_1955]
- [Harper and Sardanowsky 1969][research_harper_sardanowsky_1969]
- [Harris 1969][research_harris_1969]
- [Hartmann et al 1979][research_hartmann_1979]
- [Hastings and Mitcham 1954][research_hastings_mitcham_1954]
- [Hay 1970][research_hay_1970]
- [Healy 1958][research_healy_1958]
- [Hegarty et al 1965][research_hegarty_1965]
- [Hewes and Hassell 1960][research_hewes_hassell_1960]
- [Hoffman 1971][research_hoffman_1971]
- [Holdhusen and Perusse 1965][research_holdhusen_perusse_1965]
- [Hollinger and Mitcham 1955][research_hollinger_mitcham_1955]
- [Holzhauser et al 1972][research_holzhauser_1972]
- [Howard 1975][research_howard_1975]
- [Howard 1976][research_howard_1976]
- [Huff 1949][research_huff_w_1949]
- [Ide and Landman 2025][research_ide_landman_2025]
- [Ikami et al 2021][research_ikami_2021]
- [Ioannis and Ioannis 2026][research_ioannis_ioannis_2026]
- [Irmawan et al 2023][research_irmawan_2023]
- [Irvin and Swan 1956][research_irvin_swan_1956]
- [Jacocks and Kneile 1975][research_jacocks_kneile_1975]
- [Janetzko et al 2026][research_janetzko_2026]
- [Jayasundara and Baeder 2026][research_jayasundara_baeder_2026]
- [Jiao and Yang 2026][research_jiao_yang_2026]
- [Jin and Ma 2025][research_jin_ma_2025]
- [Johnson 1954][research_johnson_1954]
- [Johnston and Friend 1965][research_johnston_friend_1965]
- [Johnston et al 1965][research_johnston_1965]
- [Juhasz et al 2025][research_juhasz_2025]
- [Kang et al 2025][research_kang_2025]
- [Kelly and Smaus 1952][research_kelly_smaus_1952]
- [Kieß et al 2026][research_kie_2026]
- [Kirby 1954][research_kirby_1954]
- [Kirby 1956][research_kirby_1956]
- [Kirby 1961][research_kirby_1961]
- [Koch 2026][research_koch_2026]
- [Kotansky 1982][research_kotansky_1982]
- [Kotansky and Bower 1977][research_kotansky_bower_1977]
- [Krenkel and Salzman 1968][research_krenkel_salzman_1968]
- [Kuhn 1979][research_kuhn_1979]
- [Kuhn and Grunwald 1960][research_kuhn_grunwald_1960]
- [Kuhn and McKinney 1965][research_kuhn_marion_0_mckinney_1965]
- [Lallman 1985][research_lallman_1985]
- [Lee 1952][research_lee_1952]
- [Lee 1953][research_lee_1953]
- [Lee and Libbey 1961][research_lee_libbey_1961]
- [Lee et al 2022][research_lee_2022]
- [Lee et al 2025][research_lee_2025]
- [Lee et al 2025, Efficient Urban Air Mobility Verti][research_lee_2025_2]
- [Lee et al 2026][research_lee_2026]
- [Lee et al 2026, Aerodynamic effects of rotor-rotor][research_lee_2026_2]
- [Leland and Thompson 1975][research_leland_thompson_1975]
- [Leng et al 2020][research_leng_2020]
- [Li and Jiang 2026][research_li_jiang_2026]
- [Li and Polak 1966][research_li_polak_1966]
- [Li et al 2025, Reconfigurable fault-tolerant atti][research_li_2025_3]
- [Li et al 2025, Sand Ingestion Behavior of Helicop][research_li_2025_2]
- [Li et al 2026][research_li_2026]
- [Li et al 2026, Design and evaluation of Avatar][research_li_2026_4]
- [Li et al 2026, Urban air mobility vertiports][research_li_2026_2]
- [Liang et al 2026][research_liang_2026]
- [Lissaman 1967][research_lissaman_1967]
- [Liu et al 2026, Delay-Aware Shared Control for Tel][research_liu_2026_2]
- [Lollar and Matous 1963][research_lollar_matous_1963]
- [Longhurst 1966][research_longhurst_1966]
- [Lovas 2026][research_lovas_2026]
- [Lovell 1954][research_lovell_1954]
- [Lovell and Parlett 1957][research_lovell_parlett_1957]
- [Lovell et al 1953][research_lovell_1953]
- [Lyu and Feng 2026][research_lyu_feng_2026]
- [Magee and Taylor 1971][research_magee_taylor_1971]
- [Makeev 2026][research_makeev_2026]
- [Maksoud et al 2025][research_maksoud_2025]
- [Mao et al 2026][research_mao_2026]
- [Marchese 1963][research_marchese_1963]
- [Marchinski 1974][research_marchinski_1974]
- [Martin 1963, Investigation Of Longitudinal Hand][research_martin_1963_2]
- [Mathur and Atkins 2026][research_mathur_atkins_2026]
- [Matt and Altamirano 2026][research_matt_altamirano_2026]
- [Mazzitelli 1957][research_mazzitelli_1957]
- [McCaskill 1953][research_mccaskill_1953]
- [McCormick 1956][research_mccormick_w_1956]
- [McCormick 1969][research_mccormick_1969]
- [McCormick and Mallen 1956][research_mccormick_mallen_1956]
- [McCormick and Mallen 1957][research_mccormick_mallen_1957]
- [McGregor and Smith 1965][research_mcgregor_smith_1965]
- [McIntosh et al 2024][research_mcintosh_2024]
- [McIntyre 1963][research_mcintyre_1963]
- [McKinney 1954][research_mckinney_p_1954]
- [Meng et al 2023][research_meng_2023]
- [Mercan et al 2025][research_mercan_2025]
- [Merrick 1981][research_merrick_1981]
- [Merrick 1984][research_merrick_1984]
- [Michaelsen 1971][research_michaelsen_1971]
- [Mihaila et al 2026][research_mihaila_2026]
- [Mirković et al 2026][research_mirkovic_2026]
- [Mohankumar et al 2021][research_mohankumar_2021]
- [Mohankumar et al 2022][research_mohankumar_2022]
- [Morse and Newhouse 1960][research_morse_newhouse_1960]
- [Morse and Newhouse 1961][research_morse_newhouse_1961]
- [Mortimer et al 2026][research_mortimer_2026]
- [NASA 1960][research_naca_1960]
- [NASA 1960, NASA Conference on V/STOL Aircraft][research_naca_1960_2]
- [Nettleton 1965][research_nettleton_1965]
- [Newsom and Anglin 1975][research_newsom_anglin_1975]
- [Newton et al 2024][research_newton_2024]
- [Ostheimer and Giguere 1963][research_ostheimer_giguere_1963]
- [Owen and Cox 1966][research_owen_cox_1966]
- [Paek 2025][research_paek_2025]
- [Palko 1973][research_palko_1973]
- [Pan et al 2026][research_pan_2026]
- [Panish and Bacic 2025][research_panish_bacic_2025]
- [Papadales 1979][research_papadales_s_1979]
- [Park 2026][research_park_2026]
- [Park and Park 2026][research_park_park_2026]
- [Park et al 2025][research_park_2025]
- [Parlett 1961][research_parlett_1961]
- [Pascioni et al 2026][research_pascioni_2026]
- [Samarth Pathak 2025][research_pathak_2025]
- [de Paula et al 2026][research_paula_2026]
- [Paulson and Shanks 1961][research_paulson_shanks_1961]
- [Pfeifle and Fichter 2023][research_pfeifle_fichter_2023]
- [Platou 1968][research_platou_1968]
- [Pobikrowska and Goetzendorf-Grabowski 2025][research_pobikrowska_goetzendorf_grabowski_2025]
- [Polhamus 1966][research_polhamus_1966]
- [Polhamus 1968][research_polhamus_1968]
- [Polhamus 1969][research_polhamus_1969]
- [Procházková and Juračka 2026][research_prochazkova_juracka_2026]
- [Przedpelski 1965][research_przedpelski_1965]
- [Putman 1961][research_putman_1961]
- [Qian et al 2026][research_qian_2026]
- [Qiao and Zhou 2026][research_qiao_zhou_2026]
- [Queijo et al 1953][research_queijo_1953]
- [Queijo et al 1953, Wind-Tunnel Investigation at Low S][research_queijo_1953_2]
- [Queijo et al 1953, Wind-Tunnel Investigation at Low S][research_queijo_1953_3]
- [Queijo et al 1953, Wind-Tunnel Investigation at Low S][research_queijo_1953_4]
- [Radmanesh 2026][research_radmanesh_2026]
- [Rajendran 2025][research_rajendran_2025]
- [Abdul Rashid et al 2025][research_rashid_2025]
- [Rehan et al 2026][research_rehan_2026]
- [Rhoads 1967][research_rhoads_1967]
- [Roberts 1964][research_roberts_1964]
- [Rolls 1965][research_rolls_1965]
- [Rolls 1965, Jet Vtol power plant experience du][research_rolls_1965_2]
- [Roy 1966][research_roy_1966]
- [Ryan et al 1975][research_ryan_1975]
- [Ryu et al 2025][research_ryu_2025]
- [Saetti 2025, Dynamic Inversion Flight Control L][research_saetti_2025_2]
- [Saetti and Rogers 2024][research_saetti_rogers_2024]
- [Sagaga and Lee 2025][research_sagaga_lee_2025]
- [Salahudden et al 2024][research_salahudden_2024]
- [Schade et al 1954][research_schade_1954]
- [Scordamaglia et al 2025][research_scordamaglia_2025]
- [Sellers and Szuch 1973][research_sellers_szuch_1973]
- [Shandor and Walker 1962][research_shandor_walker_1962]
- [Shanks and Smith 1959][research_shanks_smith_1959]
- [Shanks and Smith 1960][research_shanks_smith_1960]
- [Sharma et al 2021][research_sharma_2021]
- [Shen and Chen 2025][research_shen_chen_2025]
- [Shirbhate et al 2025][research_shirbhate_2025]
- [Sissingh 1956][research_sissingh_1956]
- [Smith 1958][research_smith_1958]
- [Smith 1958, Hovering and Transition Flight Tes][research_smith_1958_2]
- [Smith 1961][research_smith_1961]
- [Smith 1961, Flight Tests of a 1/6-Scale Model][research_smith_1961_2]
- [Smith and Lovell 1954][research_smith_lovell_1954]
- [Spencer 1962][research_spencer_1962]
- [Spillman 1965][research_spillman_1965]
- [Stephenson et al 2026][research_stephenson_2026]
- [Stevens and Roskam 1985][research_stevens_roskam_1985]
- [Stewart et al 2026][research_stewart_2026]
- [Stone et al 1975][research_stone_1975]
- [Strand 1967][research_strand_1967]
- [Su et al 2024][research_su_2024]
- [Sutton and Buell 1952][research_sutton_buell_1952]
- [Swick and Skarvan 1967][research_swick_skarvan_1967]
- [Tamaskani et al 2026][research_tamaskani_2026]
- [Tapscott 1960][research_tapscott_1960]
- [Tellez-Belkotosky et al 2025][research_tellez_belkotosky_2025]
- [Titchener 1963][research_titchener_1963]
- [Vallerie 1967][research_vallerie_1967]
- [Vegh 2025][research_vegh_2025]
- [Walker et al 1965][research_walker_1965]
- [Wang and Chen 2024][research_wang_chen_2024]
- [Wang et al 2025][research_wang_2025]
- [Wang et al 2025, Modeling and Attitude Disturbances][research_wang_2025_3]
- [Wang et al 2026, Adaptive Augmentation of Increment][research_wang_2026_3]
- [Wang et al 2026, Adaptive sliding mode fault-tolera][research_wang_2026_6]
- [Wang et al 2026, Cascaded finite-time hovering atti][research_wang_2026_5]
- [Wang et al 2026, Modeling and hover control of a bi][research_wang_2026_4]
- [Warsett 1953][research_warsett_1953]
- [Wentz 1972][research_wentz_1972]
- [Whitaker et al 1977][research_whitaker_1977]
- [White and Innis 1959][research_white_innis_1959]
- [White et al 1960][research_white_1960]
- [Williams and Butler 1964][research_williams_butler_1964]
- [Xi et al 2025][research_xi_2025]
- [Xu et al 2026][research_xu_2026]
- [Xue and Zhou 2020][research_xue_zhou_2020]
- [Yang 1970][research_yang_1970]
- [Yang et al 2025, Robust Online Predictive Visual Se][research_yang_2025_2]
- [Yuan et al 2024][research_yuan_2024]
- [Zagranski et al 1974][research_zagranski_1974]
- [Zhang et al 2025, Image-based fixed-time visual serv][research_zhang_2025_3]
- [Zhao et al 2024][research_zhao_2024]
- [Zhao et al 2026][research_zhao_2026]
- [Zhou et al 2025][research_zhou_2025]
- [Zhou et al 2026][research_zhou_2026]
- [Zhou et al 2026, Research on Autonomous Uav Shipboa][research_zhou_2026_2]
- [Zhu et al 2022][research_zhu_2022]
- [Zwiener et al 2026][research_zwiener_2026]

[research_acher_2021]: https://doi.org/10.18409/ispiv.v1i1.51
[research_adams_1972]: https://doi.org/10.2514/6.1972-962
[research_ahmed_2025]: https://doi.org/10.1142/s230138502550027x
[research_anderson_1960]: https://ntrs.nasa.gov/citations/19980223619
[research_anderson_1979]: https://ntrs.nasa.gov/citations/19790019011
[research_antonakis_2025]: https://doi.org/10.1016/j.ast.2025.110020
[research_antonakis_2025_2]: https://doi.org/10.1007/s13272-025-00815-4
[research_aoyagi_tolhurst_1964]: https://ntrs.nasa.gov/citations/19670022812
[research_asghari_tayefi_2026]: https://doi.org/10.1109/access.2026.3679992
[research_ashkenas_1965]: https://doi.org/10.21236/ad0627659
[research_athayde_2024]: https://doi.org/10.3390/act13060225
[research_ayyaswamy_2023]: https://doi.org/10.1016/j.joule.2023.07.014
[research_barufaldi_morales_2023]: https://doi.org/10.2514/1.c036890
[research_barzda_1966]: https://doi.org/10.2514/6.1966-733
[research_batra_2024]: https://doi.org/10.3390/aerospace11090698
[research_baxter_finvold_1958]: https://doi.org/10.4271/580070
[research_beale_miller_1975]: https://doi.org/10.21236/ada014231
[research_behan_siciliani_1965]: https://doi.org/10.2514/6.1965-722
[research_behan_siciliani_1967]: https://doi.org/10.2514/3.43811
[research_bennett_1947]: https://ntrs.nasa.gov/citations/20050028507
[research_bianco_simon_2023]: https://ntrs.nasa.gov/citations/20230005325
[research_bihrle_bowman_1980]: https://ntrs.nasa.gov/citations/19800042785
[research_binion_w_1970]: https://doi.org/10.21236/ad0711665
[research_blanchard_1981]: https://ntrs.nasa.gov/citations/19810012555
[research_boggan_clarke_2026]: https://doi.org/10.1109/tte.2026.3681423
[research_bowman_1955]: https://ntrs.nasa.gov/citations/20050030035
[research_bowman_1955_2]: https://ntrs.nasa.gov/citations/20050029375
[research_bowman_1957]: https://ntrs.nasa.gov/citations/20050028487
[research_brown_1965]: https://doi.org/10.2514/6.1965-756
[research_burk_wilson_1975]: https://ntrs.nasa.gov/citations/19790022002
[research_burnell_1973]: https://doi.org/10.21236/ad0771030
[research_burton_2026]: https://doi.org/10.1115/1.4070771
[research_butler_thomas_1964]: https://doi.org/10.21236/ad0613342
[research_cai_2026]: https://doi.org/10.3390/drones10050325
[research_cai_2026_2]: https://doi.org/10.1061/jaeeez.aseng-6043
[research_cai_lovera_2026]: https://doi.org/10.1109/taes.2025.3622578
[research_campbell_1962]: https://ntrs.nasa.gov/citations/19630017020
[research_cao_2023]: https://doi.org/10.3390/drones7090566
[research_caprace_2025]: https://doi.org/10.2514/1.j065017
[research_carmichael_mcnay_1961]: https://doi.org/10.21236/ad0282125
[research_carpenter_jenny_1964]: https://doi.org/10.2514/6.1964-286
[research_chaloff_1974]: https://doi.org/10.21236/ada002858
[research_chen_2025_3]: https://doi.org/10.1016/j.bspc.2025.108024
[research_chen_2026]: https://doi.org/10.3389/arc.2026.16513
[research_christiansen_1984]: https://ntrs.nasa.gov/citations/19840035242
[research_clark_1963]: https://doi.org/10.21236/ad0419126
[research_clark_1964]: https://doi.org/10.2514/6.1964-618
[research_clark_spurlin_1962]: https://doi.org/10.21236/ad0329345
[research_combey_2026]: https://doi.org/10.2514/1.c038518
[research_comeau_2024]: https://doi.org/10.1177/15485129221118937
[research_comer_2026]: https://doi.org/10.2514/1.g009060
[research_cook_1964]: https://doi.org/10.21236/ada953004
[research_corliss_1977]: https://ntrs.nasa.gov/citations/19770052109
[research_crandall_1973]: https://doi.org/10.21236/ad0766642
[research_crespillo_2025]: https://doi.org/10.1007/s13272-024-00749-3
[research_davidson_1972]: https://doi.org/10.21236/ad0763365
[research_davis_spicer_1965]: https://doi.org/10.2514/6.1965-1425
[research_denning_1962]: https://doi.org/10.4271/620308
[research_dent_1966]: https://doi.org/10.1016/0022-460x(66)90128-3
[research_div_1956]: https://doi.org/10.21236/ad0141370
[research_division_1966]: https://ntrs.nasa.gov/citations/19660015317
[research_doff_sotta_2025]: https://doi.org/10.2514/1.g008315
[research_donaldson_1966]: https://doi.org/10.21236/ad0656592
[research_donaldson_1971]: https://doi.org/10.1017/s0022112071000156
[research_dougherty_1966]: https://doi.org/10.2514/6.1966-751
[research_douglass_1963]: https://doi.org/10.21236/ad0406348
[research_drinkwater_1965_2]: https://ntrs.nasa.gov/citations/19650009016
[research_drinkwater_rolls_1962]: https://ntrs.nasa.gov/citations/19620002530
[research_drinkwater_rolls_1965]: https://doi.org/10.2514/6.1965-782
[research_duivenvoorden_2025]: https://doi.org/10.2514/1.j064763
[research_duivenvoorden_2026]: https://doi.org/10.2514/1.c038435
[research_eatough_1971]: https://doi.org/10.2514/6.1971-752
[research_eilertson_1975]: https://doi.org/10.4271/751103
[research_enenakpogbe_2025]: https://doi.org/10.1016/j.ast.2025.110145
[research_eney_1967]: https://doi.org/10.2514/6.1967-576
[research_erwin_1964]: https://doi.org/10.21236/ad0609059
[research_evans_1974]: https://ntrs.nasa.gov/citations/19740020647
[research_farris_1983]: https://ntrs.nasa.gov/citations/19830060450
[research_favaro_2025]: https://doi.org/10.3390/aerospace12060559
[research_fernandez_2026]: https://doi.org/10.2514/1.c038553
[research_filippoli_2026]: https://doi.org/10.3390/safety12040096
[research_foltz_1962]: https://doi.org/10.21236/ad0414393
[research_friend_1964]: https://doi.org/10.2514/6.1964-787
[research_garren_1961]: https://ntrs.nasa.gov/citations/20040006489
[research_garren_1965]: https://ntrs.nasa.gov/citations/19650012141
[research_gentry_margason_1966]: https://ntrs.nasa.gov/citations/19660006875
[research_george_1964]: https://doi.org/10.21236/ad0608185
[research_georgiev_2025]: https://doi.org/10.3846/aviation.2025.23587
[research_gerdes_1964]: https://ntrs.nasa.gov/citations/19640018145
[research_gerhardt_chen_1978]: https://ntrs.nasa.gov/citations/19790001855
[research_gertsen_shomber_1965]: https://doi.org/10.2514/6.1965-780
[research_gold_walchli_1974]: https://doi.org/10.2514/6.1974-952
[research_goldberger_1966]: https://doi.org/10.21236/ad0644191
[research_golmirzaee_wood_2026]: https://doi.org/10.1186/s42774-025-00222-7
[research_gonzalez_tejeda_2026]: https://doi.org/10.1142/s2301385027410056
[research_gonzalo_2026]: https://doi.org/10.65150/ep-gjetr/v2e5/2026-04
[research_grafton_anglin_1975]: https://ntrs.nasa.gov/citations/19760003954
[research_grahame_1968]: https://doi.org/10.2514/6.1968-637
[research_grahame_1969]: https://doi.org/10.2514/3.44022
[research_greene_2020]: https://doi.org/10.4271/01-14-01-0001
[research_grether_1973]: https://doi.org/10.21236/ad0767203
[research_guo_2025]: https://doi.org/10.1016/j.urbmob.2025.100117
[research_gupta_2026]: https://doi.org/10.1016/j.ast.2026.112700
[research_gupta_bryson_1976]: https://ntrs.nasa.gov/citations/19760047895
[research_hafer_skinner_1960]: https://doi.org/10.21236/ad0472676
[research_hargraves_1961]: https://doi.org/10.21236/ad0268350
[research_harper_p_1955]: https://doi.org/10.21236/ad0092496
[research_harper_sardanowsky_1969]: https://doi.org/10.21236/ad0858184
[research_harris_1969]: https://doi.org/10.21236/ad0856377
[research_hartmann_1979]: https://ntrs.nasa.gov/citations/19800007805
[research_hastings_mitcham_1954]: https://ntrs.nasa.gov/citations/20050030055
[research_hay_1970]: https://doi.org/10.21236/ad0872113
[research_healy_1958]: https://ntrs.nasa.gov/citations/20050028462
[research_hegarty_1965]: https://ntrs.nasa.gov/citations/19650007734
[research_hewes_hassell_1960]: https://ntrs.nasa.gov/citations/19980223968
[research_hoffman_1971]: https://doi.org/10.2514/6.1971-768
[research_holdhusen_perusse_1965]: https://doi.org/10.21236/ada956154
[research_hollinger_mitcham_1955]: https://ntrs.nasa.gov/citations/20090023602
[research_holzhauser_1972]: https://ntrs.nasa.gov/citations/19720012362
[research_howard_1975]: https://ntrs.nasa.gov/citations/19750022974
[research_howard_1976]: https://ntrs.nasa.gov/citations/19990117220
[research_huff_w_1949]: https://doi.org/10.21236/ad0035641
[research_ide_landman_2025]: https://doi.org/10.1108/ijius-11-2024-0335
[research_ikami_2021]: https://doi.org/10.2514/1.c035880
[research_ioannis_ioannis_2026]: https://doi.org/10.70322/dav.2026.10005
[research_irmawan_2023]: https://doi.org/10.3390/drones7050330
[research_irvin_swan_1956]: https://doi.org/10.21236/ad0147927
[research_jacocks_kneile_1975]: https://doi.org/10.21236/ada004104
[research_janetzko_2026]: https://doi.org/10.1007/s10111-026-00883-4
[research_jayasundara_baeder_2026]: https://doi.org/10.4050/jahs.71.012001
[research_jiao_yang_2026]: https://doi.org/10.1007/s11581-026-07214-7
[research_jin_ma_2025]: https://doi.org/10.3390/smartcities8060202
[research_johnson_1954]: https://ntrs.nasa.gov/citations/20090023688
[research_johnston_1965]: https://doi.org/10.21236/ad0622578
[research_johnston_friend_1965]: https://doi.org/10.4050/sm_vstol_1965-2533
[research_juhasz_2025]: https://doi.org/10.1017/aer.2025.35
[research_kang_2025]: https://doi.org/10.2514/1.g008466
[research_kelly_smaus_1952]: https://ntrs.nasa.gov/citations/20050019245
[research_kie_2026]: https://doi.org/10.3390/aerospace13040343
[research_kirby_1954]: https://ntrs.nasa.gov/citations/20090023639
[research_kirby_1956]: https://ntrs.nasa.gov/citations/19930084609
[research_kirby_1961]: https://ntrs.nasa.gov/citations/20040047148
[research_koch_2026]: https://doi.org/10.2514/1.j066617
[research_kotansky_1982]: https://ntrs.nasa.gov/citations/19820015292
[research_kotansky_bower_1977]: https://doi.org/10.21236/ada043518
[research_krenkel_salzman_1968]: https://doi.org/10.2514/3.43962
[research_kuhn_1979]: https://doi.org/10.21236/ada073099
[research_kuhn_grunwald_1960]: https://ntrs.nasa.gov/citations/19980227804
[research_kuhn_marion_0_mckinney_1965]: https://ntrs.nasa.gov/citations/19650025397
[research_lallman_1985]: https://ntrs.nasa.gov/citations/19860001736
[research_lee_1952]: https://ntrs.nasa.gov/citations/20050029463
[research_lee_1953]: https://ntrs.nasa.gov/citations/20050029432
[research_lee_2022]: https://doi.org/10.2514/1.c036214
[research_lee_2025]: https://doi.org/10.1007/s12206-024-1204-8
[research_lee_2025_2]: https://doi.org/10.3390/su17115054
[research_lee_2026]: https://doi.org/10.1109/taes.2026.3714382
[research_lee_2026_2]: https://doi.org/10.1017/jfm.2026.11347
[research_lee_libbey_1961]: https://ntrs.nasa.gov/citations/19980227452
[research_leland_thompson_1975]: https://ntrs.nasa.gov/citations/19750009270
[research_leng_2020]: https://doi.org/10.1142/s2301385020500247
[research_li_2025_2]: https://doi.org/10.3390/aerospace12100927
[research_li_2025_3]: https://doi.org/10.1016/j.aej.2024.11.090
[research_li_2026]: https://doi.org/10.1016/j.ast.2025.111519
[research_li_2026_2]: https://doi.org/10.1016/j.urbmob.2026.100265
[research_li_2026_4]: https://doi.org/10.1016/j.displa.2025.103292
[research_li_jiang_2026]: https://doi.org/10.1016/j.energy.2026.140162
[research_li_polak_1966]: https://doi.org/10.2514/6.1966-492
[research_liang_2026]: https://doi.org/10.1109/lra.2025.3632111
[research_lissaman_1967]: https://doi.org/10.2514/6.1967-2
[research_liu_2026_2]: https://doi.org/10.1109/jiot.2026.3697060
[research_lollar_matous_1963]: https://doi.org/10.1109/thfe.1963.231288
[research_longhurst_1966]: https://doi.org/10.4271/660315
[research_lovas_2026]: https://doi.org/10.3390/drones10050395
[research_lovell_1953]: https://ntrs.nasa.gov/citations/20050029472
[research_lovell_1954]: https://ntrs.nasa.gov/citations/20050028502
[research_lovell_parlett_1957]: https://ntrs.nasa.gov/citations/19930084763
[research_lyu_feng_2026]: https://doi.org/10.1016/j.tranpol.2026.104345
[research_magee_taylor_1971]: https://doi.org/10.21236/ad0735733
[research_makeev_2026]: https://doi.org/10.26467/2079-0619-2026-29-2-121-132
[research_maksoud_2025]: https://doi.org/10.1016/j.rineng.2025.103968
[research_mao_2026]: https://doi.org/10.1016/j.ast.2026.112672
[research_marchese_1963]: https://doi.org/10.21236/ad0442887
[research_marchinski_1974]: https://doi.org/10.2514/6.1974-962
[research_martin_1963_2]: https://doi.org/10.2514/6.1963-1016
[research_mathur_atkins_2026]: https://doi.org/10.2514/1.g008907
[research_matt_altamirano_2026]: https://doi.org/10.2514/1.c038636
[research_mazzitelli_1957]: https://doi.org/10.4271/570357
[research_mccaskill_1953]: https://doi.org/10.21236/ad0015833
[research_mccormick_1969]: https://doi.org/10.21236/ad0863818
[research_mccormick_mallen_1956]: https://doi.org/10.4050/sm_wf_1956-2299
[research_mccormick_mallen_1957]: https://doi.org/10.4050/jahs.2.49
[research_mccormick_w_1956]: https://doi.org/10.21236/ad0159429
[research_mcgregor_smith_1965]: https://doi.org/10.2514/6.1965-705
[research_mcintosh_2024]: https://doi.org/10.2514/1.g008002
[research_mcintyre_1963]: https://doi.org/10.21236/ad0602427
[research_mckinney_p_1954]: https://ntrs.nasa.gov/citations/19930090534
[research_meng_2023]: https://doi.org/10.1016/j.cja.2023.06.022
[research_mercan_2025]: https://doi.org/10.1016/j.jairtraman.2025.102760
[research_merrick_1981]: https://ntrs.nasa.gov/citations/19810021598
[research_merrick_1984]: https://ntrs.nasa.gov/citations/19850006532
[research_michaelsen_1971]: https://doi.org/10.2514/6.1971-992
[research_mihaila_2026]: https://doi.org/10.3390/eng7070335
[research_mirkovic_2026]: https://doi.org/10.1016/j.urbmob.2025.100181
[research_mohankumar_2021]: https://doi.org/10.1115/1.4050606
[research_mohankumar_2022]: https://doi.org/10.1115/1.4054064
[research_morse_newhouse_1960]: https://doi.org/10.21236/ad0248356
[research_morse_newhouse_1961]: https://doi.org/10.21236/ad0264226
[research_mortimer_2026]: https://doi.org/10.4050/jahs.71.042007
[research_naca_1960]: https://ntrs.nasa.gov/citations/19630004807
[research_naca_1960_2]: https://ntrs.nasa.gov/citations/19740076580
[research_nettleton_1965]: https://doi.org/10.2514/6.1965-713
[research_newsom_anglin_1975]: https://ntrs.nasa.gov/citations/19750022036
[research_newton_2024]: https://doi.org/10.1177/10711813241280042
[research_ostheimer_giguere_1963]: https://doi.org/10.21236/ad0402379
[research_owen_cox_1966]: https://doi.org/10.1016/0022-460x(66)90141-6
[research_paek_2025]: https://doi.org/10.5139/jksas.2025.53.1.91
[research_palko_1973]: https://doi.org/10.21236/ad0769307
[research_pan_2026]: https://doi.org/10.1088/1742-6596/3207/1/012030
[research_panish_bacic_2025]: https://doi.org/10.2514/1.c037862
[research_papadales_s_1979]: https://doi.org/10.21236/ada073100
[research_park_2025]: https://doi.org/10.1016/j.apenergy.2024.124567
[research_park_2026]: https://doi.org/10.1016/j.enconman.2025.120868
[research_park_park_2026]: https://doi.org/10.1016/j.ast.2025.110745
[research_parlett_1961]: https://ntrs.nasa.gov/citations/19980227758
[research_pascioni_2026]: https://doi.org/10.2514/1.c038487
[research_pathak_2025]: https://doi.org/10.52783/jier.v5i2.3173
[research_paula_2026]: https://doi.org/10.2514/1.g009512
[research_paulson_shanks_1961]: https://ntrs.nasa.gov/citations/19980227997
[research_pfeifle_fichter_2023]: https://doi.org/10.2514/1.g006929
[research_platou_1968]: https://doi.org/10.2514/6.1968-388
[research_pobikrowska_goetzendorf_grabowski_2025]: https://doi.org/10.1108/aeat-01-2025-0001
[research_polhamus_1966]: https://ntrs.nasa.gov/citations/19670003842
[research_polhamus_1968]: https://ntrs.nasa.gov/citations/19680022518
[research_polhamus_1969]: https://ntrs.nasa.gov/citations/19700034491
[research_prochazkova_juracka_2026]: https://doi.org/10.1016/j.trpro.2026.01.012
[research_przedpelski_1965]: https://doi.org/10.2514/6.1965-708
[research_putman_1961]: https://doi.org/10.21236/ad0270217
[research_qian_2026]: https://doi.org/10.3390/drones10080610
[research_qiao_zhou_2026]: https://doi.org/10.1016/j.ast.2025.110825
[research_queijo_1953]: https://ntrs.nasa.gov/citations/20050080793
[research_queijo_1953_2]: https://ntrs.nasa.gov/citations/20050029407
[research_queijo_1953_3]: https://ntrs.nasa.gov/citations/20050029464
[research_queijo_1953_4]: https://ntrs.nasa.gov/citations/20050029471
[research_radmanesh_2026]: https://doi.org/10.1007/s12667-026-00785-4
[research_rajendran_2025]: https://doi.org/10.61359/11.2106-2557
[research_rashid_2025]: https://doi.org/10.15866/irease.v18i5.25896
[research_rehan_2026]: https://doi.org/10.1017/aer.2026.10130
[research_rhoads_1967]: https://doi.org/10.21236/ad0820790
[research_roberts_1964]: https://doi.org/10.1007/978-3-7091-4688-0_3
[research_rolls_1965]: https://ntrs.nasa.gov/citations/19660037515
[research_rolls_1965_2]: https://ntrs.nasa.gov/citations/19660013004
[research_roy_1966]: https://doi.org/10.1016/0376-0421(66)90003-0
[research_ryan_1975]: https://doi.org/10.21236/ada014229
[research_ryu_2025]: https://doi.org/10.1177/02783649241287229
[research_saetti_2025_2]: https://doi.org/10.4050/jahs.70.032005
[research_saetti_rogers_2024]: https://doi.org/10.4050/jahs.69.042007
[research_sagaga_lee_2025]: https://doi.org/10.4050/jahs.70.032004
[research_salahudden_2024]: https://doi.org/10.1016/j.ast.2024.109156
[research_schade_1954]: https://ntrs.nasa.gov/citations/20050028505
[research_scordamaglia_2025]: https://doi.org/10.1109/ojcsys.2025.3619810
[research_sellers_szuch_1973]: https://ntrs.nasa.gov/citations/19730007088
[research_shandor_walker_1962]: https://doi.org/10.21236/ad0406683
[research_shanks_smith_1959]: https://ntrs.nasa.gov/citations/19980235622
[research_shanks_smith_1960]: https://ntrs.nasa.gov/citations/19980230619
[research_sharma_2021]: https://doi.org/10.2514/1.c035973
[research_shen_chen_2025]: https://doi.org/10.3390/drones9090624
[research_shirbhate_2025]: https://doi.org/10.1007/s12046-025-02838-3
[research_sissingh_1956]: https://doi.org/10.21236/ad0116272
[research_smith_1958]: https://ntrs.nasa.gov/citations/19980227972
[research_smith_1958_2]: https://ntrs.nasa.gov/citations/19710082837
[research_smith_1961]: https://ntrs.nasa.gov/citations/19980230621
[research_smith_1961_2]: https://ntrs.nasa.gov/citations/19980227431
[research_smith_lovell_1954]: https://ntrs.nasa.gov/citations/20050030042
[research_spencer_1962]: https://ntrs.nasa.gov/citations/19630000325
[research_spillman_1965]: https://doi.org/10.2514/6.1965-797
[research_stephenson_2026]: https://doi.org/10.3390/systems14020167
[research_stevens_roskam_1985]: https://ntrs.nasa.gov/citations/19860003826
[research_stewart_2026]: https://doi.org/10.3390/aerospace13070616
[research_stone_1975]: https://doi.org/10.21236/ada014230
[research_strand_1967]: https://doi.org/10.2514/3.43869
[research_su_2024]: https://doi.org/10.3390/drones8110625
[research_sutton_buell_1952]: https://ntrs.nasa.gov/citations/20090026346
[research_swick_skarvan_1967]: https://doi.org/10.21236/ad0666796
[research_tamaskani_2026]: https://doi.org/10.1016/j.ast.2026.111656
[research_tapscott_1960]: https://ntrs.nasa.gov/citations/19630004822
[research_tellez_belkotosky_2025]: https://doi.org/10.1109/mcse.2025.3597193
[research_titchener_1963]: https://doi.org/10.1017/s0368393100078937
[research_vallerie_1967]: https://ntrs.nasa.gov/citations/19670020039
[research_vegh_2025]: https://doi.org/10.2514/1.c038393
[research_walker_1965]: https://doi.org/10.21236/ad0617129
[research_wang_2025]: https://doi.org/10.1016/j.ast.2024.109773
[research_wang_2025_3]: https://doi.org/10.1007/s13369-024-09910-w
[research_wang_2026_3]: https://doi.org/10.1109/taes.2026.3663140
[research_wang_2026_4]: https://doi.org/10.1016/j.cnsns.2026.110180
[research_wang_2026_5]: https://doi.org/10.1016/j.ast.2025.110780
[research_wang_2026_6]: https://doi.org/10.1016/j.isatra.2025.12.046
[research_wang_chen_2024]: https://doi.org/10.3390/aerospace11090711
[research_warsett_1953]: https://doi.org/10.21236/ad0015981
[research_wentz_1972]: https://ntrs.nasa.gov/citations/19720025346
[research_whitaker_1977]: https://ntrs.nasa.gov/citations/19780011159
[research_white_1960]: https://doi.org/10.21236/ad0251154
[research_white_innis_1959]: https://ntrs.nasa.gov/citations/19980232080
[research_williams_butler_1964]: https://doi.org/10.2514/6.1964-1103
[research_xi_2025]: https://doi.org/10.1088/1742-6596/3073/1/012019
[research_xu_2026]: https://doi.org/10.3390/s26123627
[research_xue_zhou_2020]: https://doi.org/10.1016/j.ast.2019.105556
[research_yang_1970]: https://doi.org/10.2514/6.1970-914
[research_yang_2025_2]: https://doi.org/10.1109/tiv.2024.3385283
[research_yuan_2024]: https://doi.org/10.1109/jas.2024.124254
[research_zagranski_1974]: https://doi.org/10.21236/ad0785580
[research_zhang_2025_3]: https://doi.org/10.1007/s11071-025-11229-6
[research_zhao_2024]: https://doi.org/10.3390/aerospace11110922
[research_zhao_2026]: https://doi.org/10.1016/j.ast.2025.110810
[research_zhou_2025]: https://doi.org/10.1016/j.ifacol.2025.11.200
[research_zhou_2026]: https://doi.org/10.1007/s42524-026-5302-4
[research_zhou_2026_2]: https://doi.org/10.3390/machines14060612
[research_zhu_2022]: https://doi.org/10.3390/aerospace9100547
[research_zwiener_2026]: https://doi.org/10.1109/tcst.2026.3672184
