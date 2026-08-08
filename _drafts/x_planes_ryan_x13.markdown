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

where $\ell$ is the distance from the nozzle to the centre of mass and $\theta$ is the deflection. **One term is quadratic in speed and the other is constant, so they cross exactly once**, and the airframe must be adequately controlled on both sides of the crossing and at it.

That is the X-13's research question, and it is not a question the previous five articles could have asked. The [X-11][related_post_a308_convair_x11] was a mass-fraction problem and the [X-12][related_post_a309_convair_x12] a terminal-velocity problem. **Neither vehicle was ever required to be controllable at zero airspeed, because neither was ever at zero airspeed while airborne.** The general statement of the problem for this class of aircraft is [Campbell 1962][research_campbell_1962], which is the period's standard treatment, with the conference record in [NACA 1960][research_naca_1960] and [NACA 1960, NASA Conference on V/stol Aircraft][research_naca_1960_2].

### What Adequate Means

Control authority is judged against an angular acceleration the pilot can use, and the period settled on figures near half a radian per second squared in pitch and one in roll for a hovering aircraft. Taking the X-13's mass at its gross weight of 6,730 pounds, or

$$m = 3053 \, \text{kg}$$

and a pitch radius of gyration of 0.30 of the 7.14 metre length gives

$$I_{yy} = m \, (0.30 L)^{2} = 3053 \times 2.14^{2} = 1.40 \times 10^{4} \, \text{kg m}^{2}$$

so the required pitching moment is

$$M_{\text{req}} = I_{yy} \, \dot{q}_{\text{req}} = 1.40 \times 10^{4} \times 0.50 = 6998 \, \text{N m}$$

The radius of gyration and the criterion are both estimates and are identified as such in the Epistemic State. The criteria themselves were being established experimentally at exactly this moment, and the aircraft that established them was the next one in this series, in [Drinkwater and Rolls 1962][research_drinkwater_rolls_1962] using the variable-stability X-14A, with the visual-flight investigation in [Garren et al 1965][research_garren_1965].

### Three Axes, Three Different Answers

The crossing is not a single event, because the three axes are controlled by different things and hand over at different speeds.

**Pitch** is deflected thrust against elevons, and both act about the same axis with comparable arms. **Yaw** is deflected thrust against a rudder, and on a tail-sitter the rudder is on a fin that is short because the fuselage is short. **Roll cannot use deflected thrust at all**, because rolling the aircraft about the thrust line produces no moment however the nozzle is aimed, so it needs a separate device that a conventional aeroplane does not carry.

That asymmetry is the reason a tail-sitting jet looks the way it does. **The roll axis is the one that forces a design decision**, and everything outboard on the X-13, the endplates and the jets beyond them, exists to serve it. The systematic study of what a jet vertical take-off aircraft actually needs by way of reaction control is [Friend 1964][research_friend_1964], and the cost of providing it is quantified in [Hoffman 1971][research_hoffman_1971].

### Where They Cross

With a wing area of 191 square feet, a mean chord taken as area over span,

$$\bar{c} = \frac{S}{b} = \frac{17.74}{6.40} = 2.77 \, \text{m}$$

and an elevon pitching-moment increment of 0.10 at full deflection, the aerodynamic moment is

$$M_{\text{aero}} = \tfrac{1}{2} \times 1.225 \times 17.74 \times 2.77 \times 0.10 \, V^{2} = 3.013 \, V^{2}$$

Setting that equal to the requirement gives the speed below which the control surfaces cannot do the job,

$$V_{\text{cross}} = \sqrt{\frac{6998}{3.013}} = 48.2 \, \text{m/s} = 94 \, \text{knots}$$

The vectored thrust, meanwhile, is ample everywhere. A ten degree deflection of 10,000 pounds of thrust at an assumed 3.5 metre arm gives

$$M_{\text{thrust}} = 44{,}482 \times 3.50 \times \sin 10^{\circ} = 27{,}035 \, \text{N m}$$

which is

$$\frac{M_{\text{thrust}}}{M_{\text{req}}} = 3.86$$

**Nearly four times what is needed.** The criteria this is measured against were assembled over the following decade, in [Tapscott 1960][research_tapscott_1960] on primary handling qualities for hovering and transition, [Anderson 1960][research_anderson_1960] examining the criteria themselves, [Clark 1964][research_clark_1964], and later by moving-base simulation in [McCormick 1969][research_mccormick_1969] and by task performance measurement in [Harper and Sardanowsky 1969][research_harper_sardanowsky_1969]. So the handover is not a struggle between two marginal systems. The thrust vectoring is comfortable from zero airspeed upward, and the aerodynamic surfaces become comfortable at 48 metres per second. The interesting question is what that speed is compared with.

### The Answer, and Why It Is Not Obvious

The wing begins carrying the aircraft at its stall speed. At a gross weight of 29,935 newtons over 17.74 square metres, with a maximum lift coefficient of 1.0 for a thin delta without high-lift devices,

$$V_{\text{stall}} = \sqrt{\frac{2W}{\rho S C_{L\max}}} = \sqrt{\frac{2 \times 29{,}935}{1.225 \times 17.74 \times 1.0}} = 52.5 \, \text{m/s}$$

so

$$\frac{V_{\text{cross}}}{V_{\text{stall}}} = \frac{48.2}{52.5} = 0.918$$

**The control surfaces become adequate at ninety-two percent of the speed at which the wing starts flying.** The two events coincide, and the coincidence is the whole reason a tail-sitting jet is possible at all. Had the crossover come at twice the stall speed the aircraft would have had a band of speeds in which it was flying on its wing and could not be pointed, which is not a survivable condition.

The coincidence is not luck, and it is worth seeing why. Both quantities scale with $W/S$ and with the same dynamic pressure, so their ratio depends on the ratio of the control-moment coefficient to the lift coefficient and on the geometry, and not on the size or weight of the aircraft. **A tail-sitting jet works because the same air that lifts a wing also works its controls, and both start at once.** The low-speed characteristics that set the wing side of it are [Aoyagi and Tolhurst 1964][research_aoyagi_tolhurst_1964] and [Spencer 1962][research_spencer_1962]. What would break it is not weight but a control surface too small, and this is the design margin the article's later sections keep returning to.

Writing the ratio out makes the independence explicit. Both speeds come from setting a moment equal to a requirement,

$$V_{\text{cross}}^{2} = \frac{I_{yy} \dot{q}_{\text{req}}}{\tfrac{1}{2} \rho S \bar{c} \, \Delta C_{m}}, \qquad V_{\text{stall}}^{2} = \frac{2W}{\rho S C_{L\max}}$$

so their ratio is

$$\left( \frac{V_{\text{cross}}}{V_{\text{stall}}} \right)^{2} = \frac{I_{yy} \, \dot{q}_{\text{req}} \, C_{L\max}}{W \bar{c} \, \Delta C_{m}}$$

The wing area has cancelled and the air density has cancelled. What remains is the pitch inertia divided by the weight, which for a given shape scales as a length, divided by the mean chord, which is also a length. **The ratio is therefore a function of proportions and of the required angular acceleration, and not of scale**, which is why a one-fifth-scale model of this aircraft can demonstrate the same handover. It is also why the requirement itself became the interesting variable, and whether the control power a hovering aircraft needs depends on its size was studied directly in [Johnston and Friend 1965][research_johnston_friend_1965] and [Johnston et al 1965][research_johnston_1965].

## Programme Origin

### A Navy Question From 1947

The line begins with the Bureau of Aeronautics, which in 1947 asked Ryan whether a jet fighter could be launched vertically, under a designation of F3R. The motivation was that a vertically launched fighter needs no runway, and therefore could operate from a small ship, from a clearing, or from a submarine. Ryan's own starting point was the FR-1 Fireball, a mixed-power fighter the company had already built.

**The Navy pursued the same idea with propellers and got there first.** The Convair XFY-1 and the Lockheed XFV-1 were turboprop tail-sitters flown from 1954, and their development generated the research literature this article rests on, in [Lovell et al 1953][research_lovell_1953], [Lovell 1954][research_lovell_1954], [Queijo et al 1953][research_queijo_1953], [Johnson 1954][research_johnson_1954], [Smith and Lovell 1954][research_smith_lovell_1954], [Schade et al 1954][research_schade_1954], [Kelly and Smaus 1952][research_kelly_smaus_1952], [Sutton and Buell 1952][research_sutton_buell_1952], and [Kirby 1954][research_kirby_1954]. **The X-13 exists because the Air Force wanted the same demonstration on pure jet thrust**, and contracted Ryan for it in 1953. A stand-on configuration had already been flown as a model in [Mckinney 1954][research_mckinney_p_1954], and rocket-boosted and windmilling-propeller variants of the XFY-1 case are [Hastings and Mitcham 1954][research_hastings_mitcham_1954] and [Hollinger and Mitcham 1955][research_hollinger_mitcham_1955].

**The mid-1950s were also the moment the whole configuration space was surveyed at once.** Comparative studies weighed tail-sitters against tilt-wings, deflected slipstream, and lift engines, in [Irvin and Swan 1956][research_irvin_swan_1956] on performance and weight estimates for six vertical take-off aircraft, [Div 1956][research_div_1956], and [McCormick 1956][research_mccormick_w_1956], the last of which is a transition analysis and is therefore the nearest thing in the accessible literature to a general treatment of this article's keystone. The propeller side of the same survey is [Kirby 1961][research_kirby_1961] and [Kuhn and Grunwald 1960][research_kuhn_grunwald_1960].

### Why the Propeller Version Was Easier, in a Sentence That Needs Numbers

A turboprop tail-sitter hovers inside its own slipstream. The propeller pushes air over the wing and tail even at zero forward speed, so the control surfaces work in the hover. A turbojet tail-sitter exhausts aft of everything and its wing sees nothing at all.

Quantifying it settles the design difference completely. A propeller disc supporting a weight $W$ over area $A$ produces a slipstream of

$$v_{s} = \sqrt{\frac{2 (W/A)}{\rho}}$$

and for a disc loading of roughly 1,500 pascals, which is the class the XFY-1 sat in,

$$v_{s} = \sqrt{\frac{2 \times 1500}{1.225}} = 49.5 \, \text{m/s}$$

That is a dynamic pressure of 1,500 pascals over the inboard wing, against 1,687 pascals at the X-13's stall. **A turboprop tail-sitter hovers with something close to stall-speed dynamic pressure already on its control surfaces, and a turbojet tail-sitter hovers with none.** The propeller side of that statement is measured in [Sutton and Buell 1952][research_sutton_buell_1952] and surveyed in [Kirby 1961][research_kirby_1961]. The propeller aircraft therefore needed no reaction control system and the jet aircraft could not do without one, and that single ratio explains why the two configurations look so different despite answering the same question.

## Sizing From First Principles

### The First Condition, Which Is Necessary and Not Sufficient

A hovering aircraft must produce more thrust than it weighs. The Rolls-Royce Avon RA.28 gave 10,000 pounds against a gross weight of 6,730, so

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

The useful load at gross weight is the difference between 6,730 and the 5,334 pound empty weight, which is 1,396 pounds. Allowing 250 pounds for the pilot and his equipment leaves about 1,146 pounds of fuel, giving

$$t_{\text{hover}} = \frac{1146}{104.3} = 11.0 \, \text{min}$$

**The entire fuel load is about eleven minutes of hovering.** That is the number the whole article turns on, and it is worth restating in the harshest form available. One minute of hovering at each end of a flight spends nearly a fifth of the fuel before the machine has gone anywhere.

The relation generalises and the generalisation is unkind. Hover endurance is

$$t_{\text{hover}} = \frac{m_{f}}{c \, W} = \frac{1}{c} \cdot \frac{m_{f}}{W}$$

so it depends only on the fuel fraction and the specific fuel consumption, and **not at all on the size of the aircraft or the thrust of its engine.** A larger tail-sitter with a larger engine hovers for exactly as long as a smaller one at the same fuel fraction. There is no scale at which the problem improves, which is the difference between this constraint and most aircraft design constraints, and it is why the comparative studies of the period kept returning verdicts against the configuration for transport work, in [Div 1956][research_div_1956] and [McCormick 1956][research_mccormick_w_1956]. The weight bookkeeping behind those verdicts is [Irvin and Swan 1956][research_irvin_swan_1956].

A rotorcraft escapes the same arithmetic because it does not produce its lift as thrust from a jet. Hovering efficiency is measured by the power needed per unit of lift, which for an actuator disc is

$$\frac{P}{T} = \sqrt{\frac{T/A}{2 \rho}}$$

and therefore improves as the disc grows. **A jet has the smallest possible disc and pays the largest possible price**, and the disc-loading comparison computed later in this article is the same fact seen from the ground rather than from the fuel gauge.

### Roll, Which Is the Harder Axis

Pitch and yaw were handled by deflecting the engine exhaust. Roll could not be, because rolling the aircraft about the thrust line produces no moment however the nozzle is aimed. **A tail-sitting jet therefore needs a separate roll control that works at zero airspeed**, and the X-13 carried compressed-air jets at the wingtips, outboard of the endplates.

Sizing them is a short calculation. A roll radius of gyration of 0.20 of the 6.40 metre span gives

$$I_{xx} = m (0.20 b)^{2} = 3053 \times 1.28^{2} = 5003 \, \text{kg m}^{2}$$

and at a criterion of one radian per second squared the couple required is 5,003 newton metres. Delivered by a pair of opposed jets at the tips, the force each must produce is

$$F = \frac{M}{b} = \frac{5003}{6.40} = 782 \, \text{N} = 176 \, \text{lbf}$$

which is 3.5 percent of the engine's thrust taken as a couple. At an assumed bleed velocity of 500 metres per second that is a mass flow of

$$\dot{m} = \frac{2F}{v} = \frac{1564}{500} = 3.13 \, \text{kg/s}$$

or about 4.5 percent of an Avon's air. **A roll control that costs four percent of the engine is affordable and not negligible**, and it is a cost the propeller tail-sitters did not pay at all. The design problem of arranging engine control and attitude control together in a vertical-attitude aircraft is [Baxter and Finvold 1958][research_baxter_finvold_1958], which is the closest thing in the accessible literature to a statement of this vehicle's control philosophy, with the reaction control criteria worked systematically in [Friend 1964][research_friend_1964].

The ailerons take over earlier than the elevons do. At a rolling-moment coefficient of 0.05 the aerodynamic couple reaches the same criterion at

$$V = \sqrt{\frac{M}{\tfrac{1}{2} \rho S b \, \Delta C_{l}}} = 37.9 \, \text{m/s}$$

which is 0.72 of the stall speed, so **roll hands over from the puffers to the ailerons well before pitch hands over from the nozzle to the elevons.** The two axes do not cross at the same moment, and a pilot flying the transition is therefore managing a control system whose character changes progressively rather than all at once.

### Yaw, Which Is the Easy Axis, and the Sequence That Results

Yaw has been mentioned and not sized, and sizing it completes the picture. Taking the yaw inertia five percent above the pitch inertia, which is what a configuration with most of its mass along the body axis and its wing short gives,

$$I_{zz} \approx 1.05 \, I_{yy} = 1.47 \times 10^{4} \, \text{kg m}^{2}$$

and a criterion of 0.3 radians per second squared, the required moment is 4,412 newton metres. The nozzle supplies that at a deflection of

$$\theta = \arcsin \frac{M}{T \ell} = \arcsin \frac{4412}{44{,}482 \times 3.50} = 1.62^{\circ}$$

**Under two degrees.** Yaw is the axis nobody had to think about, because the same nozzle that handles pitch handles yaw with a fraction of the deflection and the criterion is lower.

The rudder takes over early as well. At a yawing-moment increment of 0.06 the aerodynamic moment reaches the criterion at

$$V = \sqrt{\frac{M}{\tfrac{1}{2} \rho S b \, \Delta C_{n}}} = 32.5 \, \text{m/s}$$

which is 0.62 of the stall speed. Collecting the three axes gives the article's structural result about the transition.

| Axis | Reaction or vectored device | Aerodynamic device takes over at | As a fraction of stall speed |
|---|---|---|---|
| Yaw | nozzle, 1.6 degrees | 32.5 m/s | 0.62 |
| Roll | wingtip jets, 782 N each | 37.9 m/s | 0.72 |
| Pitch | nozzle, 10 degrees | 48.2 m/s | 0.92 |

**The three axes do not hand over together. They hand over in sequence, and the sequence runs from the cheapest axis to the dearest.** The derivatives that would settle the aerodynamic side of each were measured for this configuration class in [Queijo et al 1953, Wind-Tunnel Investigation at Low S][research_queijo_1953_2], [Queijo et al 1953, Wind-Tunnel Investigation at Low S][research_queijo_1953_3], and [Queijo et al 1953, Wind-Tunnel Investigation at Low S][research_queijo_1953_4], and for the jet-powered vertical-attitude model in [Shanks and Smith 1959][research_shanks_smith_1959] and [Shanks and Smith 1960][research_shanks_smith_1960]. A pilot accelerating through the transition therefore feels the aircraft become a conventional aeroplane one axis at a time, first in yaw, then in roll, and last in pitch, and for a band of about sixteen metres per second he is flying a machine that is aerodynamic in two axes and reactive in the third. That is a more interesting statement than a single crossover speed, and it is the kind of thing an article gets only by computing all three.

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

Reaction control is not free and its price is paid in the same currency as everything else. A puffer system sized to the criterion above bleeds about 4.5 percent of the engine's air, and bleeding air from a turbojet costs thrust roughly in proportion, so holding the roll criterion in a hover costs

$$\Delta T \approx 0.045 \, T = 2002 \, \text{N} = 450 \, \text{lbf}$$

against a hover margin of 3,270 pounds. **Roll control alone consumes about fourteen percent of the thrust margin**, before pitch and yaw are considered and before any allowance for gusts. That figure is an estimate resting on the assumed bleed velocity, and the general accounting of what control power costs a vertical take-off aircraft is [Hoffman 1971][research_hoffman_1971].

The consequence is a design spiral of the ordinary kind. More control power needs more bleed, which needs more thrust, which needs a larger engine, which needs a larger airframe, which has more inertia and therefore needs more of it. **The spiral converges only because the requirement is an angular acceleration and inertia grows faster than the moment arms do**, so the aircraft that closes is a small one, and the X-13 is small. Whether the requirement itself should depend on size is [Johnston et al 1965][research_johnston_1965] and [Johnston and Friend 1965][research_johnston_friend_1965].

### What an Operational Version Would Have Cost

The programme was a demonstration and never carried a weapon, but the arithmetic of what it would have meant operationally is short and is the reason the idea stopped. The fuel fraction is

$$\zeta = \frac{1146}{6730} = 0.170$$

and the Breguet range for a jet is

$$R = \frac{V}{c} \frac{L}{D} \ln \frac{1}{1 - \zeta}$$

with $c$ the thrust specific fuel consumption expressed as a reciprocal time, which for 0.93 pounds per pound-hour is $2.583 \times 10^{-4}$ per second. At a cruise speed of 200 metres per second and a lift-to-drag ratio of six,

$$R = \frac{200}{2.583 \times 10^{-4}} \times 6 \times \ln \frac{1}{0.830} = 867 \, \text{km}$$

giving a radius of 434 kilometres if every pound of fuel went to cruising. It does not.

| Total hover time | Fuel spent hovering | Radius | Radius forgone |
|---|---|---|---|
| 60 s | 104.3 lb | 391 km | 43 km, 9.9 percent |
| 120 s | 208.6 lb | 348 km | 85 km, 19.7 percent |
| 180 s | 312.9 lb | 307 km | 127 km, 29.2 percent |

**One minute of hovering at each end of the flight costs a fifth of the radius.** The period's own weight and performance bookkeeping for this class is [Irvin and Swan 1956][research_irvin_swan_1956], with the configuration comparison in [Div 1956][research_div_1956] and [Campbell 1962][research_campbell_1962]. And one minute is optimistic for a vertical landing onto a hook, for the reasons the preceding sections quantify.

| Hover discipline | Take-off and landing | Fuel spent | Fraction of fuel |
|---|---|---|---|
| Brisk | 0.5 and 1.0 minutes | 156 lb | 13.7 percent |
| Realistic | 1.0 and 2.0 minutes | 313 lb | 27.3 percent |
| Cautious | 2.0 and 4.0 minutes | 626 lb | 54.6 percent |

**A cautious pilot spends more than half the fuel without leaving the airfield.** And the preceding analysis says the pilot has every reason to be cautious, since he is flying a third-order loop by proxy through a man on the ground toward a hook he cannot see. The vertical take-off and landing capability is therefore not free and not cheap. It is paid for in the currency the aircraft has least of, and the payment is made twice on every sortie.

## Dependent Systems

### The Engine, Which Is Most of the Aeroplane

The Avon RA.28 is a single-shaft axial turbojet with a fifteen-stage compressor, rated at 10,000 pounds of thrust. In an airframe with an empty weight of 5,334 pounds the engine is a large fraction of the whole, and it is better understood as an engine with a wing attached than as an aeroplane with an engine in it. **Every dimension of the X-13 follows from wrapping the smallest possible airframe around an Avon**, which is why the span is 21 feet, the length 23 feet 5 inches, and the aspect ratio

$$AR = \frac{b^{2}}{S} = \frac{6.40^{2}}{17.74} = 2.31$$

A wing of aspect ratio 2.31 is a poor lifting device and a good structural one, and on an aircraft that spends its critical moments not using the wing at all, that is the correct trade.

### The Nozzle

Pitch and yaw came from deflecting the exhaust. The relation derived above puts the required deflection in context, since a ten degree deflection delivers nearly four times the pitching moment the criterion asks for, so the nozzle need not be large-angle and the deflection can be modest. The penalty is a loss of axial thrust,

$$\frac{T_{\text{axial}}}{T} = \cos \theta = \cos 10^{\circ} = 0.985$$

so **a ten degree deflection costs 1.5 percent of the thrust**, which against a thrust-to-weight ratio of 1.486 is affordable. At thirty degrees it would cost 13.4 percent, which is not, and this is the quantitative reason a vectoring system for attitude control is a small-angle device while one for propulsion is not.

| Deflection | Axial thrust retained | Moment produced | Angular acceleration |
|---|---|---|---|
| 5 degrees | 99.6 percent | 13,569 N m | 0.969 rad/s² |
| 10 degrees | 98.5 percent | 27,035 N m | 1.932 rad/s² |
| 15 degrees | 96.6 percent | 40,295 N m | 2.879 rad/s² |

The mechanisms available for turning a jet were an active subject and remained one, in [Erwin et al 1964][research_erwin_1964] on tandem cascade vectoring, [Eatough 1971][research_eatough_1971] on jet tabs, and [Shandor and Walker 1962][research_shandor_walker_1962] on fluid injection, with the measurement problem of establishing where a nozzle's thrust vector actually points in [Davis and Spicer 1965][research_davis_spicer_1965] and [Holdhusen and Perusse 1965][research_holdhusen_perusse_1965].

### The Puffer Jets

The wingtip jets sized above are the aircraft's only roll control below 38 metres per second. Their placement outboard of the wingtip endplates is a moment-arm decision and the arithmetic is direct, since the required force varies inversely with the arm,

$$F = \frac{I_{xx} \dot{p}}{b}$$

so halving the span would double the force and therefore double the bleed. **A tail-sitting jet wants a wide span for roll control and a small span for everything else**, and that tension is visible in the aircraft's proportions.

### The Wing, Which Spends the Critical Moments Doing Nothing

A wing of aspect ratio 2.31 with a sharp leading edge is a poor subsonic lifting surface and its low-speed behaviour is dominated by leading-edge vortices rather than by attached flow. The adopted maximum lift coefficient of 1.0 reflects that, and the sensitivity is worth showing because the article's central ratio depends on it.

| Maximum lift coefficient | Stall speed | Ratio of crossover to stall |
|---|---|---|
| 0.8 | 58.7 m/s | 0.821 |
| 1.0 | 52.5 m/s | 0.918 |
| 1.2 | 47.9 m/s | 1.006 |

**At a lift coefficient of 1.2 the crossover moves above the stall speed and the coincidence the article rests on becomes an inequality in the wrong direction.** The qualitative conclusion survives, since the two speeds remain within a few percent of each other, but the comfortable reading that the controls come alive before the wing does depends on a coefficient that has been assumed rather than measured. The low-speed aerodynamics of slender deltas at high incidence are [Clark and Spurlin 1962][research_clark_spurlin_1962], [Spencer 1962][research_spencer_1962], and [Wentz 1972][research_wentz_1972], and what a tailless delta fighter is actually like to fly slowly is [White and Innis 1959][research_white_innis_1959].

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

**Holding position to within a metre over five seconds requires holding the mean tilt below half a degree.** That is the actual task, and it is why hovering is difficult in a way that the control-power criteria do not capture. Measuring task performance rather than control power is what [Harper and Sardanowsky 1969][research_harper_sardanowsky_1969] set out to do, with the visual side in [Garren et al 1965][research_garren_1965]. The criteria say the pilot can command an angular acceleration. They do not say he can hold an attitude to half a degree while looking sideways.

### The Wind Is a Position Problem, Not an Attitude Problem

Standing vertically, the airframe presents its whole length to a crosswind. Taking a side area of ten square metres and a drag coefficient of 0.8, both estimates,

$$F = \tfrac{1}{2} \rho V^{2} A C_{d}$$

| Crosswind | Side force | Acceleration | Uncorrected drift in 30 s |
|---|---|---|---|
| 5 m/s | 122 N | 0.040 m/s² | 18 m |
| 10 m/s | 490 N | 0.160 m/s² | 72 m |
| 15 m/s | 1102 N | 0.361 m/s² | 163 m |

The moment such a wind produces is small, at 7.0 percent of the pitch requirement in a ten metre per second wind with the side-area centroid a metre from the centre of mass. **So the wind does not threaten control and it does threaten station-keeping**, and the pilot must hold a steady tilt into it, which is a steady attitude error he is also using to correct position. The two tasks are the same actuator and they conflict, which is the coupling [Tapscott 1960][research_tapscott_1960] and [Anderson 1960][research_anderson_1960] were trying to write criteria around.

### Height, and an Asymmetry

Vertical control is a throttle problem and it is asymmetric. A vertical acceleration $a$ requires a thrust change of $m a$, so

| Vertical acceleration | Thrust change | As a fraction of thrust |
|---|---|---|
| 0.5 m/s² | 1,526 N | 3.4 percent |
| 1.0 m/s² | 3,053 N | 6.9 percent |
| 2.0 m/s² | 6,106 N | 13.7 percent |

The upward margin is bounded by the thrust available, at 4.76 metres per second squared. **The downward authority is unbounded, because the pilot can always close the throttle and let the aircraft fall.** A descent is therefore easier to start than to stop, and stopping it costs engine response time. At an assumed one second spool a one metre per second sink costs a metre of height before the thrust arrives, which against a hook is the whole tolerance.

### The Ground Observer Was Part of the Control Loop

The reported arrangement, in which a man on the ground talked the pilot down because the pilot could not see the trailer, is usually recorded as an operational inconvenience. **It is better understood as a sensor with a transport delay inserted into a third-order loop that has no damping.**

The hook tolerance is of order a third of a metre. At a closure rate of one metre per second, a loop delay $\tau$ introduces a position uncertainty of

$$\delta x = V \tau$$

so a delay of 0.3 seconds consumes the entire tolerance, and 0.3 seconds is optimistic for a human observer speaking over a radio to a pilot who must then move a control. **The X-13 landed successfully many times, so the loop clearly closed**, and the arithmetic says it closed with very little margin and only because the closure rate was kept low. What a pilot can and cannot do with a delayed and partial view of a landing point is [Behan and Siciliani 1965][research_behan_siciliani_1965], [Behan and Siciliani 1967][research_behan_siciliani_1967], and [Rhoads 1967][research_rhoads_1967]. Keeping the closure rate low costs hover time, and hover time is the fuel.

### The Trailer, the Wire, and the Hook

The X-13 had no undercarriage in the ordinary sense. It hung from a wire strung on an A-frame at the top of a trailer bed, which raised to the vertical for launch and recovery and lowered to the horizontal to move the aircraft. A hook on the underside of the nose engaged the wire, and a short pole projecting from the airframe gave the pilot a distance reference.

The arrangement removes weight from the aircraft and puts it on the ground, which is the correct decision for a vehicle whose thrust margin is 3,270 pounds and whose undercarriage would have cost several hundred. **It also makes the aircraft dependent on a specific piece of ground equipment for every landing**, which is the opposite of the operational freedom the vertical take-off concept was supposed to buy, and the tension between those two facts is the deepest problem in the programme. The same tension appears from the other direction in [Butler and Thomas 1964][research_butler_thomas_1964], which is about preparing sites rather than about not needing them.

### The Undercarriage That Was Not Carried

The trailer looks like an eccentricity and it is a weight decision. A retractable undercarriage for a machine of this class costs something in the region of three to five percent of gross weight, so

| Gear weight as a fraction of gross | Weight | As a fraction of the fuel load |
|---|---|---|
| 3 percent | 202 lb | 17.6 percent |
| 4 percent | 269 lb | 23.5 percent |
| 5 percent | 336 lb | 29.4 percent |

**Deleting the undercarriage bought roughly a quarter more fuel**, which against an eleven minute hover endurance is two or three minutes of hovering and, by the radius table above, some tens of kilometres. Weight bookkeeping of this kind across the configuration options is [Irvin and Swan 1956][research_irvin_swan_1956]. On an aircraft this tightly bounded that is not a small saving, and it explains why a design that looks like a stunt is actually the obvious answer once the fuel arithmetic is admitted.

The structural side reinforces it. Hanging from a hook at the nose puts the entire weight into the airframe as a **tension**, while standing on a tail puts the same load in as a **compression** on a slender body. A tension member is lighter than a column of equal strength, so the hook arrangement is structurally as well as operationally cheaper than legs would have been.

The arrival itself is gentle. At a closure rate $v$ arrested over a stroke $d$ the mean deceleration is

$$a = \frac{v^{2}}{2d}$$

so a one metre per second arrival stopped in 0.3 metres is

$$a = \frac{1.0}{0.6} = 1.67 \, \text{m/s}^{2} = 0.17 g$$

**A vertical landing on a wire is a very soft landing**, softer than a conventional arrival on a runway, which is worth stating because the arrangement looks violent and is not. The difficulty of the landing was never the impact. It was arriving at the right place with the right speed while unable to see.

### The Cockpit, and a Pilot Who Cannot See

The pilot's seat pivoted forty-five degrees so that he was not lying flat on his back during vertical flight. Forty-five degrees is a compromise and it leaves the problem half-solved, because his line of sight remains

$$90^{\circ} - 45^{\circ} = 45^{\circ}$$

away from the direction the aircraft is travelling during a vertical descent. **The reported and decisive difficulty is that the underside of the fuselage sits between the pilot and the trailer he is trying to land on.** He approached the recovery point without being able to see it and depended on a ground observer to talk him down.

That is not a detail. The vertical landing is a closed-loop position-control task with a tolerance of a few centimetres on a hook, executed by a pilot who cannot see the target, in an aircraft with eleven minutes of fuel, in ground effect. The visual requirements for exactly this class of task were being measured at the time in [Garren et al 1965][research_garren_1965] and [Behan and Siciliani 1965][research_behan_siciliani_1965], and the general problem of a pilot's acceptance of a landing display is [Behan and Siciliani 1967][research_behan_siciliani_1967] and [Rhoads 1967][research_rhoads_1967].

### Spin and Tumble

A tail-sitter with a low aspect ratio and a large fuselage volume is a candidate for departure modes that a conventional aeroplane does not have, and the X-13 was tested for them in the Langley spin tunnel before it flew. **This is the one part of the programme with a complete surviving primary record**, in [Bowman 1955][research_bowman_1955] on free-spinning and recovery, [Bowman 1955, Emergency Spin-Recovery Device for][research_bowman_1955_2] on the emergency recovery device, and [Bowman 1957][research_bowman_1957] as the concluding report covering spinning, tumbling, and recovery together. The equivalent studies for the propeller tail-sitters are [Lee 1952][research_lee_1952] and [Lee 1953][research_lee_1953].

Tumbling is the mode peculiar to this configuration. An aircraft pointed vertically with no forward speed has no aerodynamic restoring moment in pitch, so a disturbance can start it rotating end over end, and once tumbling it has no airspeed with which to stop. The reaction controls are the only recovery, and their authority was computed above.

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

**A hovering jet loads the ground about a hundred times more heavily than a helicopter of the same span.** That is why a tail-sitting jet needs a prepared surface and a helicopter does not, and it is the second reason the operational freedom the concept promised was not actually available. The impingement problem and its design criteria are [George et al 1964][research_george_1964], with the dust-ingestion consequence in [Hafer and Skinner 1960][research_hafer_skinner_1960] and the analogous problem on another surface entirely in [Roberts 1964][research_roberts_1964]. **The operational answer was to prepare the ground**, and the fact that somebody wrote a document called rapid site preparation for turbojet vertical take-off aircraft, in [Butler and Thomas 1964][research_butler_thomas_1964], is the clearest possible statement that the runway had not actually been eliminated but relocated and renamed. Surface bearing capacity under aircraft loads is [Hay 1970][research_hay_1970], and the jet in ground effect as an aerodynamic problem is [Lissaman 1967][research_lissaman_1967], [Foltz 1962][research_foltz_1962], and [Carmichael and McNay 1961][research_carmichael_mcnay_1961].

## The Flight Test Record

Two aircraft were built, serial numbers 54-1619 and 54-1620, under the Ryan company designation Model 69. The programme ran without loss of an aircraft or injury to a pilot, which for a first-of-type vertical take-off aircraft is a notable result on its own.

| Date | Event | Aircraft |
|------|-------|----------|
| 1955-12-10 | First conventional flight, temporary landing gear | 54-1619 |
| 1956-05-28 | First vertical hovering flight | 54-1619 |
| 1957-04-11 | First complete cycle, vertical to horizontal to vertical | 54-1620 |
| 1957-07-28 | Demonstration across the Potomac, landing at the Pentagon | 54-1620 |

The sequence is worth reading as a decomposition. **The programme separated the problem into the two halves that could be tested independently and only then joined them.** The first aircraft flew conventionally on temporary undercarriage to establish that it was an aeroplane, then hovered on a tether and free to establish that it was a hovering machine, and the two halves were joined sixteen months later. That ordering is the same one the [X-5][related_post_a302_bell_x5] used for variable sweep and the [X-13's] own predecessors used for the propeller case, and it is what a research aircraft programme looks like when it is being run carefully.

The interval from first flight to full cycle is about 491 days, or 1.35 years. The pilots were Ryan's chief test pilot Peter Girard and Ryan test pilot Lou Everett.

**A programme of two aircraft and a handful of flights cannot support a statistical statement and should not be asked to.** What it can support is a statement about sequence, and the sequence is the finding.

Each phase settled a different one of the article's relations. **The conventional flight on temporary undercarriage settled the wing**, which is to say it demonstrated the stall speed and the low-speed handling that the crossover ratio is measured against. **The hovering flights settled the reaction and vectoring authority**, which the relations above put at 3.86 times the criterion in pitch, and they also settled the position-loop problem well enough for the pilot to hold station. **The full cycle settled only the joining of the two**, and it is the shortest of the three questions because the transition itself lasts about five seconds.

That ordering also explains the sixteen month interval. The two ends of the problem were tested for eleven months before anybody attempted the middle, which is a programme deliberately arranging that the only untested thing on the day of the full cycle was the handover itself. The variable-stability technique that would later let one aircraft stand in for many is [Harper 1955][research_harper_p_1955] and, for this problem specifically, [Drinkwater and Rolls 1962][research_drinkwater_rolls_1962]. Simulation as the alternative to flying every case arrives with [McIntyre 1963][research_mcintyre_1963] and [McCormick 1969][research_mccormick_1969].

### What the Full Cycle Actually Demonstrated

**It demonstrated the crossover.** Everything in the article's first section is a prediction that the two control systems hand over cleanly, and the 11 April 1957 flight is the measurement. The aircraft went from a state in which its wing did nothing and its nozzle did everything to the reverse, and back, without an uncontrollable band in between.

**It did not demonstrate anything about the mission**, because there was no mission. The aircraft carried no armament, no radar, no operational fuel load, and no capability to land anywhere except on its own trailer.

### The Pentagon Flight

On 28 and 29 July 1957 the X-13 was flown in Washington, crossing the Potomac and landing at the Pentagon. It is the most photographed event of the programme and the least technical. **A demonstration flown for an audience of officials is a statement that the technical question has been answered and the remaining question is whether anyone wants the answer.** The answer turned out to be no, and the Air Force declined to continue on the stated grounds that there was no operational requirement.

## Comparison With Ground Prediction

### What the Models Got Right

The X-13 was preceded by an unusually complete model programme, and the single most directly relevant document is [Smith 1958, Hovering and Transition Flight Tes][research_smith_1958_2] on hovering and transition flight tests of a one-fifth-scale model of the aircraft. **A free-flight model at one-fifth scale can perform the entire manoeuvre the full-scale aircraft exists to perform**, which is unusual, and it is possible because the transition is a low-speed manoeuvre in which compressibility does not enter and the model can be flown indoors.

The spin tunnel work in [Bowman 1955][research_bowman_1955] and [Bowman 1957][research_bowman_1957] covered the departure modes, and the whole XFY-1 and XFV-1 literature covered the configuration class, in [Lovell et al 1953][research_lovell_1953], [Queijo et al 1953][research_queijo_1953], [Kirby 1956][research_kirby_1956], and [Lovell and Parlett 1957][research_lovell_parlett_1957], the last of which is a jet-powered vertically rising model and therefore the nearest aerodynamic relative of the X-13 in the model record.

### What the Models Could Not Show

**A free-flight model has no pilot in it.** The decisive difficulty of the X-13, that the man flying it cannot see where he is going during the landing, is invisible at model scale because the model is flown by someone standing outside it with an unobstructed view. **The programme's ground testing was excellent and it tested the wrong difficulty**, not through carelessness but because the difficulty was not aerodynamic.

**A model does not burn fuel in proportion.** Hover endurance does not scale, so a model that hovers for as long as its tether is connected gives no warning that the full-scale aircraft has eleven minutes.

**A model does not load the ground.** For geometric scaling at a fixed thrust-to-weight ratio the thrust goes as the cube of length and the nozzle area as the square, so the disc loading goes as the first power,

$$\frac{T}{A} \propto L$$

and a one-fifth-scale model imposes one fifth of the pressure, not one twenty-fifth. That is still 28 kilopascals, which is enough to notice and not enough to reproduce the erosion, and the linear rather than quadratic scaling is the reason ground-effect results from small models transfer poorly.

**And a model is flown to a different standard.** A free-flight model is judged by whether it completes the manoeuvre, and a real aeroplane is judged by whether a pilot can complete it repeatably while doing other things. The gap between those two standards is what handling qualities research exists to measure, and the techniques for measuring it were being invented alongside these aircraft, in [Anderson 1960][research_anderson_1960], [Clark 1964][research_clark_1964], [Nettleton 1965][research_nettleton_1965], [Mcgregor and Smith 1965][research_mcgregor_smith_1965], [Ashkenas 1965][research_ashkenas_1965], and [Harper and Sardanowsky 1969][research_harper_sardanowsky_1969], with pilot-model analysis in [Adams 1972][research_adams_1972].

## What the Data Changed

### Into the Control Power Criteria

The most durable result is the least visible. The question of how much attitude control power a hovering aircraft actually needs was open when the X-13 flew and was closed shortly afterwards by systematic experiment, in [Drinkwater and Rolls 1962][research_drinkwater_rolls_1962] using the X-14A as a variable-stability testbed and [Garren et al 1965][research_garren_1965] in visual flight. **The X-13 is one of the data points that made the question worth asking**, and the criteria that emerged are the ones used above to size its own controls, which is a pleasing circularity and a real one.

### Into Nothing Operational

No tail-sitting jet fighter was built. The reasons this article can demonstrate are the fuel arithmetic, the pilot's inability to see the landing point, and the ground loading, and they are all present in the numbers rather than in hindsight.

### Into the Configuration That Actually Worked

The vertical take-off jet did enter service, and not in this form. The Hawker P.1127 kept the aircraft horizontal and turned the thrust instead of turning the aeroplane, which leaves the pilot facing forward, leaves the undercarriage useful, and removes the landing visibility problem entirely. Its model testing is [Smith 1961, Flight Tests of a 1/6-Scale Model][research_smith_1961_2], flown at Langley in the same facility and by the same group that flew the X-13 model.

**The comparison is the fairest verdict on the X-13 available.** Both configurations solve the control-authority problem, and the vectored-thrust layout solves it while also solving the two problems the X-13 could not, namely where the pilot looks and what the aircraft rests on. **The X-13 demonstrated that the tail-sitting answer works and thereby helped establish that it was not the answer to take**, which is a real contribution and not the one the programme set out to make. A flight evaluation of a jet vertical take-off transport under visual and instrument conditions, which is the mature form of the same question, is [Holzhauser et al 1972][research_holzhauser_1972].

### The Vertical Attitude Idea Returns Twice

It came back in the 1970s as a proposal for carrier-based fighters, in [Eilertson 1975][research_eilertson_1975] on a remotely piloted demonstration vehicle, [Gerhardt and Chen 1978][research_gerhardt_chen_1978] on the vertical attitude concept for a fighter or attack aircraft, and [Papadales 1979][research_papadales_s_1979] on the performance of a conceptual vertical-attitude fighter. **The remotely piloted version is the interesting one, because removing the pilot removes the problem the X-13 could not solve**, and it took two decades for anyone to say so in a document.

## The Contemporary Literature

The X-13's configuration is not a historical curiosity. It is a standard layout for small uncrewed aircraft, and the reason is exactly the one the 1975 remotely piloted proposal identified, which is that the configuration's hard problem was the pilot.

### The Tail-Sitter Came Back Without a Pilot

The transition control problem this article derives is now an ordinary subject with a large literature. **Disturbance rejection through the hover and the transition together**, which is the pairing the X-13's pilot had to manage by hand, is [Mao et al 2026][research_mao_2026]. Transition strategies and corridors are [Rehan et al 2026][research_rehan_2026], [Lee et al 2026][research_lee_2026] on corridor-based optimal transition, [Pobikrowska and Goetzendorf-Grabowski 2025][research_pobikrowska_goetzendorf_grabowski_2025], [Burton et al 2026][research_burton_2026], [Panish and Bacic 2025][research_panish_bacic_2025], and [Irmawan et al 2023][research_irmawan_2023]. **The quadrotor biplane tail-sitter of [Saetti et al 2025][research_saetti_2025] is the X-13's configuration with the pilot replaced by a flight control computer and the single jet replaced by four rotors**, and it works.

**The control-authority handover is now solved as an allocation problem.** Where the X-13's pilot moved from nozzle to elevons by feel, a modern over-actuated aircraft blends them continuously, in [Scordamaglia et al 2025][research_scordamaglia_2025], [Pfeifle and Fichter 2023][research_pfeifle_fichter_2023], [Saetti 2025, Dynamic Inversion Flight Control L][research_saetti_2025_2], and [McIntosh et al 2024][research_mcintosh_2024], the last of which explicitly architects the feedforward and feedback for a tail-sitter across hybrid flight regimes. Attitude control in the hover itself is [Comer et al 2025][research_comer_2025], [Ilyas et al 2025][research_ilyas_2025], [Athayde et al 2024][research_athayde_2024], and [Dagal and Erol 2025][research_dagal_erol_2025]. **The article's third-order position loop has not become easier. It has become somebody else's problem**, and the somebody is a computer that does not need to see the landing point.

### What Price Hover, Asked Again in 2025

The article's central arithmetic is that hover endurance depends only on the fuel fraction and the specific consumption, and is therefore independent of scale. **That relation binds electric vertical take-off aircraft in exactly the same form**, with energy in place of fuel, and the question has been asked in almost the article's own words in [Hart et al 2025][research_hart_2025].

The consequences are visible throughout the current design literature. Sizing methodologies must carry the hover segment explicitly, in [Qiao and Zhou 2026][research_qiao_zhou_2026], [Lee et al 2022][research_lee_2022], and [Chen et al 2026][research_chen_2026]. Endurance relations are rewritten for hybrid propulsion in [Batra et al 2024][research_batra_2024] and [Barufaldi and Morales 2023][research_barufaldi_morales_2023]. Energy-optimal trajectories exist because the hover is worth avoiding, in [Mathur and Atkins 2026][research_mathur_atkins_2026], [Cai et al 2026][research_cai_2026], and [Kang et al 2025][research_kang_2025]. And the honest response, which is to add a second energy source so the vehicle does not have to hover on its cruise powerplant, is [Vegh 2025][research_vegh_2025] on a hybrid-electric long-endurance tail-sitter, [Zhu et al 2022][research_zhu_2022], and [Radmanesh 2026][research_radmanesh_2026]. **Seventy years later the answer to the fuel problem is still to carry a different kind of fuel rather than to hover more cheaply.**

### Ground Effect Is Still Not Solved

The disc-loading ratio of about a hundred between a jet and a rotor of the same span is why vertical landing on unprepared ground remains a rotorcraft capability. Ground effect for this class of vehicle is [Greene 2020][research_greene_2020], the ingestion problem persists even at rotorcraft disc loadings in [Li et al 2025, Sand Ingestion Behavior of Helicop][research_li_2025_2], and the shipboard case with deck motion is [Sharma et al 2021][research_sharma_2021].

### The Slipstream Question the Propeller Tail-Sitters Answered

This article's explanation of why a turboprop tail-sitter needs no reaction control is that its slipstream gives the wing stall-level dynamic pressure in the hover. That interaction is now a design variable rather than an accident, and the modern literature is about shaping it deliberately, in [Xue and Zhou 2020][research_xue_zhou_2020] on coupled propeller and wing design, [Leng et al 2020][research_leng_2020] on slipstream deformation for a convertible aircraft in hover, [Duivenvoorden et al 2026][research_duivenvoorden_2026] and [Duivenvoorden et al 2025][research_duivenvoorden_2025], [Cao et al 2023][research_cao_2023], [Meng et al 2023][research_meng_2023], [Zhao et al 2024][research_zhao_2024] and [Zhao et al 2026][research_zhao_2026] on distributed propulsion wings, and [Ikami et al 2021][research_ikami_2021] on precisely the question of what a control surface does inside a slipstream. **The X-13's disadvantage against the XFY-1 is now a design choice that distributed electric propulsion makes freely available**, which is the single largest change between the period and the present.

### High Angle of Attack, Which Is Where a Tail-Sitter Lives

A transitioning aircraft passes through every incidence from zero to ninety degrees. Modelling that is [Wang et al 2025][research_wang_2025] and [Golmirzaee and Wood 2026][research_golmirzaee_wood_2026], the unsteady interactions are [Koch 2026][research_koch_2026], [Acher et al 2021][research_acher_2021], and [Combey et al 2026][research_combey_2026], and the engine's own tolerance of incidence, which the X-13 needed and nobody measured, is [Mohankumar et al 2021][research_mohankumar_2021] and [Mohankumar et al 2022][research_mohankumar_2022].

## Where the Framing Breaks Down

**The control-power criteria are borrowed from later work.** The half a radian per second squared in pitch and one in roll used throughout are figures the field settled on after the X-13 flew, and applying them to the X-13 is anachronistic. It is done here because they are the best available statement of what adequate means, and because the article's conclusion, that the crossover falls close to the stall speed, is a ratio and is insensitive to the criterion.

**The control criteria are anachronistic in a second way as well**, since they were written for aircraft with automatic stabilisation and the X-13 had none of consequence. [Friend 1964][research_friend_1964] and [Hoffman 1971][research_hoffman_1971] both size reaction control against a stabilised airframe, and an unaugmented aircraft asks more of the pilot for the same control power.

**The elevon and aileron effectiveness figures are assumed.** A pitching-moment increment of 0.10 and a rolling-moment increment of 0.05 are plausible for a tailless delta and are not measured values for this aircraft. The crossover speed varies as the inverse square root of the assumed effectiveness, so a factor of two error in it moves the crossover by a factor of 1.41 and would break the coincidence with the stall speed that the article makes much of.

**The fuel figure is derived, not reported.** The 1,146 pound fuel load is the useful load minus an assumed pilot weight, and no fuel capacity was found for this aircraft. The eleven minute hover endurance moves in direct proportion.

**The hover analysis assumes a rigid aircraft and a still atmosphere separately, and the real case is neither.** The drift table and the crosswind table are computed independently and then discussed together, which is not the same as solving them together. A pilot correcting a wind-induced drift is holding a tilt that is itself producing drift, and the coupled problem is what the handling-qualities literature actually measures.

**The side area and drag coefficient in the crosswind table are guesses.** Ten square metres and 0.8 are plausible for a vertical aircraft of this size and are not derived from its geometry, and the forces scale directly with both.

**Treating the programme as a failure of concept understates the demonstration.** The aircraft did what it was built to do on the first attempt at the full cycle and never lost an aircraft. An article organised around why the idea did not proceed can read as though the vehicle did not work, and it worked.

## What the X-13 Was Worth

**It established that a pure jet can complete the cycle.** This was genuinely open in 1953 and closed in 1957, and no aircraft since has needed to ask it again.

**It established that the control handover is clean for this configuration.** The crossover computed above is a prediction and the flight is the confirmation.

**It established the shape of the operational objection.** The fuel, the pilot's sight line, and the ground loading are all visible in the X-13's own numbers, and a programme that had gone to a prototype fighter would have discovered them more expensively.

**It established nothing about combat capability**, and the aircraft carried nothing.

**It did not establish that the configuration is a bad idea.** The idea returned as soon as the pilot could be removed from it, which is the correct reading of what the X-13 actually proved.

## The Designation, Which Returns to Normal

For five consecutive articles this series has recorded a designation attached to something that was not a research aircraft. **The X-13 ends that run.** It is a manufacturer's prototype built in two examples under a research contract, flown by company test pilots, with no operational intent and no production plan, which is the pattern the [X-1][related_post_a298_bell_x1] established and the [X-3][related_post_a300_douglas_x3] and [X-5][related_post_a302_bell_x5] continued.

That matters for the argument the closing article of this series will have to make. **The run of five was an interruption and not a redefinition.** Whatever mechanism attached X numbers to the [X-8][related_post_a305_aerojet_x8] through the [X-12][related_post_a309_convair_x12], it did not replace the original one, and the two coexisted. A closing article that describes the series as having drifted from research aircraft to weapons would be contradicted by its own next entry.

## The Source Base

**The X-13's own record is thin and its family's record is thick.** Querying the NASA technical archive for the popular name returns nothing at all, and querying for the manufacturer and designation together returns a small set, of which the spin tunnel series and the one-fifth-scale hovering and transition tests are the substance. **The lesson is the same one the [X-10][related_post_a307_north_american_x10] taught in a different form**, which is that a vehicle is indexed under the name its engineers used and not the name the public learned.

Around that thin core sits an unusually complete literature on the configuration class, because the Navy's two propeller tail-sitters were studied exhaustively at Langley before either flew. **An article about the X-13 is therefore better supported than an article about the X-13 alone would be**, and most of the aerodynamic statements here rest on documents about the XFY-1 and the XFV-1.

The contrast with the [X-11][related_post_a308_convair_x11] and [X-12][related_post_a309_convair_x12] is instructive. Those vehicles left a thick archive because they became launch vehicles and flew for sixty years. The X-13 left almost nothing because it stopped, and what survives is the research literature of the question rather than the engineering record of the article.

**A third asymmetry is worth naming because it runs the other way from the previous two articles.** The Atlas record is thick and classified, and the geodesy the Atlas depended on is thick and open. The X-13's record is thin and open, and there is no classified layer underneath it, because a two-aircraft demonstration programme with no weapon and no production intent generated nothing worth withholding. **The whole of what is knowable about this aircraft is knowable**, which is not true of any vehicle in the five that precede it, and it makes the X-13 the easiest article in this run to verify and the hardest to say anything new about.

The defence archive contributes little here and that absence is itself informative. Querying it returns work on vertical take-off as a concept, on site preparation, and on handling qualities criteria, in [Butler and Thomas 1964][research_butler_thomas_1964], [Irvin and Swan 1956][research_irvin_swan_1956], [Div 1956][research_div_1956], [Friend 1964][research_friend_1964], [Hoffman 1971][research_hoffman_1971], and [Johnston et al 1965][research_johnston_1965], and it returns nothing at all about this airframe. **The Air Force studied the idea and the Navy's laboratories studied the aerodynamics and Ryan built the aeroplane**, and only the middle of those three left a public record of the vehicle itself.

## Epistemic State

**Historical fact, well supported.** Two X-13 aircraft were built by Ryan Aeronautical, serials 54-1619 and 54-1620, under the company designation Model 69. The Navy Bureau of Aeronautics contracted Ryan in 1947 under the designation F3R to study vertically launched jet fighters, and the Air Force contracted the X-13 in 1953. The powerplant is a Rolls-Royce Avon RA.28 of 10,000 pounds thrust. The first conventional flight was 10 December 1955, the first vertical hovering flight 28 May 1956, and the first complete cycle 11 April 1957. The aircraft was demonstrated in Washington on 28 and 29 July 1957, landing at the Pentagon. Pitch and yaw control in hover came from vectored engine thrust and roll control from compressed-air jets outboard of the wingtip endplates. The pilot's seat pivoted forty-five degrees. The aircraft launched from and recovered onto a wire on a tilting trailer using a hook. The Air Force declined to continue for lack of an operational requirement. Both aircraft survive, 54-1619 with the San Diego Air and Space Museum on loan from the Smithsonian and 54-1620 at the National Museum of the United States Air Force.

**Reported but from compilations rather than programme documents.** The dimensions of 23 feet 5 inches length, 21 feet span, 15 feet 2 inches height, and 191 square feet of wing area. The weights of 5,334 pounds empty, 6,730 pounds gross, and 7,200 pounds maximum. The identification of the test pilots. The description of the pilot's sight line being obstructed by the fuselage during the landing approach and of his dependence on outside assistance.

**Assumed for the purpose of calculation and stated as such.** The specific fuel consumption of 0.93 pounds per pound of thrust per hour, which is a figure quoted for an Avon variant rather than for the RA.28. The 250 pound allowance for pilot and equipment, from which the fuel load is derived. The maximum lift coefficient of 1.0. The elevon pitching-moment increment of 0.10, the aileron rolling-moment increment of 0.05, and the rudder yawing-moment increment of 0.06. The pitch and roll radii of gyration at 0.30 of length and 0.20 of span, and the yaw inertia taken five percent above the pitch inertia. The control power criteria of 0.5, 1.0, and 0.3 radians per second squared in pitch, roll, and yaw. The 3.5 metre nozzle moment arm. The engine mass flow of 70 kilogrammes per second and exhaust density of 0.35 kilogrammes per cubic metre. The bleed velocity of 500 metres per second. The cruise speed of 200 metres per second and lift-to-drag ratio of six. The 1,500 pascal disc loading taken as representative of the XFY-1 class. The ten square metre side area and drag coefficient of 0.8 for the crosswind case. The one second engine spool time. The 0.3 metre hook tolerance and the closure rates used against it. The undercarriage weight fraction of three to five percent of gross. The 0.3 metre arresting stroke.

**Engineering analysis, derived here and independently checkable.** The yaw inertia, the 4,412 newton metre yaw requirement, the 1.62 degree nozzle deflection that meets it, the 32.5 metre per second rudder crossover, and the resulting table showing that the three axes hand over in sequence at 0.62, 0.72, and 0.92 of the stall speed. The hover drift table and the finding that holding position to a metre over five seconds requires holding the mean tilt below half a degree. The crosswind force table and the finding that a ten metre per second wind is 7.0 percent of the pitch requirement as a moment and 72 metres of drift in thirty seconds as a position error. The vertical acceleration and thrust-change table and the asymmetry between bounded upward and unbounded downward authority. The loop-delay relation and the finding that 0.3 seconds consumes the whole hook tolerance at one metre per second. The sortie fuel table showing a cautious profile spending 54.6 percent of the fuel. The undercarriage weight table and the 23.5 percent of fuel load a four percent gear would have cost. The arresting deceleration of 0.17 gravities at one metre per second over 0.3 metres. The scaling of disc loading as the first power of length. The control power cost of about 450 pounds of thrust and its 14 percent of the hover margin. The lift coefficient sensitivity table for the crossover ratio. The nozzle deflection table. The thrust-to-weight ratios at gross and maximum weight, the vertical acceleration, and the time and speed at thirty metres. The aspect ratio, mean chord, and wing loading. The hover fuel flow of 104.3 pounds per minute and the resulting eleven minute endurance. The stall speed of 52.5 metres per second and its sensitivity to the lift coefficient. The pitch and roll inertias. The aerodynamic pitching moment relation and its coefficient of 3.013. The crossover speed of 48.2 metres per second, its ratio of 0.918 to the stall speed, and the argument that the ratio is independent of aircraft size. The vectored thrust moments and the margin of 3.86 over the criterion. The axial thrust loss with nozzle deflection. The puffer force of 782 newtons, its 3.5 percent of thrust, and the 4.5 percent bleed. The aileron crossover at 37.9 metres per second and its ratio of 0.72 to the stall speed. The maximum transition tilt of 47.7 degrees, the horizontal acceleration of 10.78 metres per second squared, the 4.9 second and 128 metre transition, the 12.6 pounds of fuel, and the tilt table. The propeller slipstream velocity of 49.5 metres per second and its comparison with the stall dynamic pressure. The Breguet range and radius, and the table charging hover time against radius. The exhaust velocity, dynamic pressure, nozzle area, and the disc loading ratio of 102 against a rotor of the same span. The interval of 491 days from first flight to full cycle.

**Inference, argued but not established.** That the three-axis handover sequence would have been perceptible to the pilot as the aircraft becoming conventional one axis at a time, which the relations imply and which no pilot report found here describes. That deleting the undercarriage was a deliberate performance decision rather than only a consequence of the launch method. That the ground observer is best understood as a delayed sensor inside the control loop, which is this article's framing and not the period's. That the coincidence between the control crossover and the stall speed is what makes the configuration workable rather than a fortunate accident. That the fuel arithmetic, the pilot's sight line, and the ground loading are the operative reasons the concept did not proceed, which the numbers support but which no document found here states in those terms. That the programme's ground testing addressed the wrong difficulty because the difficulty was not aerodynamic. That the return of the vertical-attitude concept as a remotely piloted vehicle is a recognition that the pilot was the binding constraint.

**Written from current knowledge.** This article is dated 2025-10-19 and draws on literature published after that date where the modern discussion continues the period problem, in line with the series convention.

## Out of Scope

The Convair XFY-1 and Lockheed XFV-1 as programmes in their own right, which are used here only as the configuration comparison. The Ryan FR-1 Fireball. The submarine-launched fighter concept the 1947 study addressed. The Rolls-Royce Avon as an engine programme. The later jet-lift aircraft, the Hawker P.1127 line, and the lift-fan configurations, which solved the same problem a different way and belong with the aircraft that carry those designations. The X-14, which is the next article and which established the control criteria used here. Carrier and shipboard operation. The aerodynamics of the delta wing at high angle of attack in any depth. The remotely piloted vertical-attitude proposals of the 1970s beyond noting that they exist.

## Conclusion

The X-13 was built to find out whether a jet could take off vertically, become an aeroplane, become a hovering machine again, and land on the spot it left. **It could, and it did so on the first attempt at the complete cycle, and it never hurt anybody.**

The reason it worked is a coincidence that is not a coincidence. Aerodynamic control authority grows as the square of speed and vectored thrust does not depend on speed at all, so the two hand over exactly once, and for this aircraft the handover falls at 48 metres per second against a stall speed of 52. **The control surfaces start working at ninety-two percent of the speed at which the wing starts working**, so there is no band in which the aircraft is flying and cannot be pointed. That ratio is a property of the configuration rather than of the size, which is why the layout has outlived the aeroplane.

The reason it led nowhere is arithmetic of a different kind. **The entire fuel load is eleven minutes of hovering**, the transition that the programme existed to demonstrate costs twelve pounds of it, and the hovering at either end costs everything else. A minute at each end takes a fifth of the radius. The exhaust loads the ground a hundred times harder than a helicopter of the same span, so the aircraft needs a prepared surface and a particular trailer. And the pilot cannot see the hook he is aiming at.

**Each of those is a reason the concept did not become a fighter, and none of them is a reason the aircraft failed.** The X-13 answered its question completely and the answer was that the question had been the wrong one to ask about a manned aeroplane. Two decades later the same configuration came back with nobody in it, and it is now the ordinary way to build a small aircraft that has to take off from somewhere without a runway.

## References

### Books

[book_jenkins_landis_miller_2003]: https://openlibrary.org/search?q=Jenkins+Landis+Miller+American+X+Vehicles
[book_miller_2001]: https://openlibrary.org/search?q=Miller+The+X+Planes+X-1+to+X-45
[book_rogers_1989]: https://openlibrary.org/search?q=Rogers+VTOL+Military+Research+Aircraft

### Reference

[ref_x13]: https://en.wikipedia.org/wiki/Ryan_X-13_Vertijet

### Research

[research_acher_2021]: https://doi.org/10.18409/ispiv.v1i1.51
[research_adams_1972]: https://doi.org/10.2514/6.1972-962
[research_anderson_1960]: https://ntrs.nasa.gov/citations/19980223619
[research_aoyagi_tolhurst_1964]: https://ntrs.nasa.gov/citations/19670022812
[research_ashkenas_1965]: https://doi.org/10.21236/ad0627659
[research_athayde_2024]: https://doi.org/10.3390/act13060225
[research_barufaldi_morales_2023]: https://doi.org/10.2514/1.c036890
[research_batra_2024]: https://doi.org/10.3390/aerospace11090698
[research_baxter_finvold_1958]: https://doi.org/10.4271/580070
[research_behan_siciliani_1965]: https://doi.org/10.2514/6.1965-722
[research_behan_siciliani_1967]: https://doi.org/10.2514/3.43811
[research_bowman_1955]: https://ntrs.nasa.gov/citations/20050030035
[research_bowman_1955_2]: https://ntrs.nasa.gov/citations/20050029375
[research_bowman_1957]: https://ntrs.nasa.gov/citations/20050028487
[research_burton_2026]: https://doi.org/10.1115/1.4070771
[research_butler_thomas_1964]: https://doi.org/10.21236/ad0613342
[research_cai_2026]: https://doi.org/10.3390/drones10050325
[research_campbell_1962]: https://ntrs.nasa.gov/citations/19630017020
[research_cao_2023]: https://doi.org/10.3390/drones7090566
[research_carmichael_mcnay_1961]: https://doi.org/10.21236/ad0282125
[research_chen_2026]: https://doi.org/10.3389/arc.2026.16513
[research_clark_1964]: https://doi.org/10.2514/6.1964-618
[research_clark_spurlin_1962]: https://doi.org/10.21236/ad0329345
[research_combey_2026]: https://doi.org/10.2514/1.c038518
[research_comer_2025]: https://ntrs.nasa.gov/citations/20250000954
[research_dagal_erol_2025]: https://doi.org/10.1038/s41598-025-25903-7
[research_davis_spicer_1965]: https://doi.org/10.2514/6.1965-1425
[research_div_1956]: https://doi.org/10.21236/ad0141370
[research_drinkwater_rolls_1962]: https://ntrs.nasa.gov/citations/19620002530
[research_duivenvoorden_2025]: https://doi.org/10.2514/1.j064763
[research_duivenvoorden_2026]: https://doi.org/10.2514/1.c038435
[research_eatough_1971]: https://doi.org/10.2514/6.1971-752
[research_eilertson_1975]: https://doi.org/10.4271/751103
[research_erwin_1964]: https://doi.org/10.21236/ad0609059
[research_foltz_1962]: https://doi.org/10.21236/ad0414393
[research_friend_1964]: https://doi.org/10.2514/6.1964-787
[research_garren_1965]: https://ntrs.nasa.gov/citations/19650012141
[research_george_1964]: https://doi.org/10.21236/ad0608185
[research_gerhardt_chen_1978]: https://ntrs.nasa.gov/citations/19790001855
[research_golmirzaee_wood_2026]: https://doi.org/10.1186/s42774-025-00222-7
[research_greene_2020]: https://doi.org/10.4271/01-14-01-0001
[research_hafer_skinner_1960]: https://doi.org/10.21236/ad0472676
[research_harper_p_1955]: https://doi.org/10.21236/ad0092496
[research_harper_sardanowsky_1969]: https://doi.org/10.21236/ad0858184
[research_hart_2025]: https://doi.org/10.2514/1.c038680
[research_hastings_mitcham_1954]: https://ntrs.nasa.gov/citations/20050030055
[research_hay_1970]: https://doi.org/10.21236/ad0872113
[research_hoffman_1971]: https://doi.org/10.2514/6.1971-768
[research_holdhusen_perusse_1965]: https://doi.org/10.21236/ada956154
[research_hollinger_mitcham_1955]: https://ntrs.nasa.gov/citations/20090023602
[research_holzhauser_1972]: https://ntrs.nasa.gov/citations/19720012362
[research_ikami_2021]: https://doi.org/10.2514/1.c035880
[research_ilyas_2025]: https://doi.org/10.1109/access.2025.3544133
[research_irmawan_2023]: https://doi.org/10.3390/drones7050330
[research_irvin_swan_1956]: https://doi.org/10.21236/ad0147927
[research_johnson_1954]: https://ntrs.nasa.gov/citations/20090023688
[research_johnston_1965]: https://doi.org/10.21236/ad0622578
[research_johnston_friend_1965]: https://doi.org/10.4050/sm_vstol_1965-2533
[research_kang_2025]: https://doi.org/10.2514/1.g008466
[research_kelly_smaus_1952]: https://ntrs.nasa.gov/citations/20050019245
[research_kirby_1954]: https://ntrs.nasa.gov/citations/20090023639
[research_kirby_1956]: https://ntrs.nasa.gov/citations/19930084609
[research_kirby_1961]: https://ntrs.nasa.gov/citations/20040047148
[research_koch_2026]: https://doi.org/10.2514/1.j066617
[research_kuhn_grunwald_1960]: https://ntrs.nasa.gov/citations/19980227804
[research_lee_1952]: https://ntrs.nasa.gov/citations/20050029463
[research_lee_1953]: https://ntrs.nasa.gov/citations/20050029432
[research_lee_2022]: https://doi.org/10.2514/1.c036214
[research_lee_2026]: https://doi.org/10.1109/taes.2026.3714382
[research_leng_2020]: https://doi.org/10.1142/s2301385020500247
[research_li_2025_2]: https://doi.org/10.3390/aerospace12100927
[research_lissaman_1967]: https://doi.org/10.2514/6.1967-2
[research_lovell_1953]: https://ntrs.nasa.gov/citations/20050029472
[research_lovell_1954]: https://ntrs.nasa.gov/citations/20050028502
[research_lovell_parlett_1957]: https://ntrs.nasa.gov/citations/19930084763
[research_mao_2026]: https://doi.org/10.1016/j.ast.2026.112672
[research_mathur_atkins_2026]: https://doi.org/10.2514/1.g008907
[research_mccormick_1969]: https://doi.org/10.21236/ad0863818
[research_mccormick_w_1956]: https://doi.org/10.21236/ad0159429
[research_mcgregor_smith_1965]: https://doi.org/10.2514/6.1965-705
[research_mcintosh_2024]: https://doi.org/10.2514/1.g008002
[research_mcintyre_1963]: https://doi.org/10.21236/ad0602427
[research_mckinney_p_1954]: https://ntrs.nasa.gov/citations/19930090534
[research_meng_2023]: https://doi.org/10.1016/j.cja.2023.06.022
[research_mohankumar_2021]: https://doi.org/10.1115/1.4050606
[research_mohankumar_2022]: https://doi.org/10.1115/1.4054064
[research_naca_1960]: https://ntrs.nasa.gov/citations/19630004807
[research_naca_1960_2]: https://ntrs.nasa.gov/citations/19740076580
[research_nettleton_1965]: https://doi.org/10.2514/6.1965-713
[research_panish_bacic_2025]: https://doi.org/10.2514/1.c037862
[research_papadales_s_1979]: https://doi.org/10.21236/ada073100
[research_pfeifle_fichter_2023]: https://doi.org/10.2514/1.g006929
[research_pobikrowska_goetzendorf_grabowski_2025]: https://doi.org/10.1108/aeat-01-2025-0001
[research_qiao_zhou_2026]: https://doi.org/10.1016/j.ast.2025.110825
[research_queijo_1953]: https://ntrs.nasa.gov/citations/20050080793
[research_queijo_1953_2]: https://ntrs.nasa.gov/citations/20050029407
[research_queijo_1953_3]: https://ntrs.nasa.gov/citations/20050029464
[research_queijo_1953_4]: https://ntrs.nasa.gov/citations/20050029471
[research_radmanesh_2026]: https://doi.org/10.1007/s12667-026-00785-4
[research_rehan_2026]: https://doi.org/10.1017/aer.2026.10130
[research_rhoads_1967]: https://doi.org/10.21236/ad0820790
[research_roberts_1964]: https://doi.org/10.1007/978-3-7091-4688-0_3
[research_saetti_2025]: https://doi.org/10.4050/jahs.70.042002
[research_saetti_2025_2]: https://doi.org/10.4050/jahs.70.032005
[research_schade_1954]: https://ntrs.nasa.gov/citations/20050028505
[research_scordamaglia_2025]: https://doi.org/10.1109/ojcsys.2025.3619810
[research_shandor_walker_1962]: https://doi.org/10.21236/ad0406683
[research_shanks_smith_1959]: https://ntrs.nasa.gov/citations/19980235622
[research_shanks_smith_1960]: https://ntrs.nasa.gov/citations/19980230619
[research_sharma_2021]: https://doi.org/10.2514/1.c035973
[research_smith_1958]: https://ntrs.nasa.gov/citations/19980227972
[research_smith_1958_2]: https://ntrs.nasa.gov/citations/19710082837
[research_smith_1961]: https://ntrs.nasa.gov/citations/19980230621
[research_smith_1961_2]: https://ntrs.nasa.gov/citations/19980227431
[research_smith_lovell_1954]: https://ntrs.nasa.gov/citations/20050030042
[research_spencer_1962]: https://ntrs.nasa.gov/citations/19630000325
[research_sutton_buell_1952]: https://ntrs.nasa.gov/citations/20090026346
[research_tapscott_1960]: https://ntrs.nasa.gov/citations/19630004822
[research_vegh_2025]: https://doi.org/10.2514/1.c038393
[research_wang_2025]: https://doi.org/10.1016/j.ast.2024.109773
[research_wentz_1972]: https://ntrs.nasa.gov/citations/19720025346
[research_white_innis_1959]: https://ntrs.nasa.gov/citations/19980232080
[research_xue_zhou_2020]: https://doi.org/10.1016/j.ast.2019.105556
[research_zhao_2024]: https://doi.org/10.3390/aerospace11110922
[research_zhao_2026]: https://doi.org/10.1016/j.ast.2025.110810
[research_zhu_2022]: https://doi.org/10.3390/aerospace9100547

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
