---
layout: post
mathjax: true
comments: true
title: "X-Planes: Bell X-14"
date: 2025-10-20 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 15
---

<!-- A311 -->
<script>console.log("A311");</script>

The previous article in this series used two numbers it could not justify. Discussing the [Ryan X-13 Vertijet][related_post_a310_ryan_x13], it asked whether the aircraft's control surfaces were adequate, and to answer that it needed a standard of adequacy. It used half a radian per second squared in pitch and one radian per second squared in roll, flagged both in its own epistemic state as figures the field settled on after the X-13 had finished flying, and named the aircraft that produced them. **This article is about that aircraft.** The [Bell X-14][ref_x14] is the machine that turned the question of how much control a hovering aeroplane needs from a matter of opinion into a number in a specification, and it is the fifteenth article in the [X-Planes series][related_post_a297_xplanes_framing], following the [X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], the [X-4][related_post_a301_northrop_x4], the [X-5][related_post_a302_bell_x5], the [X-6][related_post_a303_convair_x6], the [X-7][related_post_a304_lockheed_x7], the [X-8][related_post_a305_aerojet_x8], the [X-9][related_post_a306_bell_x9], the [X-10][related_post_a307_north_american_x10], the [X-11][related_post_a308_convair_x11], the [X-12][related_post_a309_convair_x12], and the [X-13][related_post_a310_ryan_x13].

It is also the strangest aircraft the series has met so far, and the strangeness is not in how it looks. **The X-14 was built to be a bad aeroplane on demand.** Its wings, ailerons, and landing gear came from a [Beechcraft Bonanza][ref_bonanza] and its tail from a [T-34 Mentor][ref_t34]. It had an open cockpit and fixed gear. Its maximum speed was under 180 miles per hour. None of that was carelessness, because none of it was the point. The point was a control system whose authority and whose damping could be dialled to arbitrary values in flight, so that a pilot could be handed a deliberately deficient aircraft and asked how bad it was. The standard inventory entry remains [Jenkins Landis and Miller 2003 American X-Vehicles, An Inventory X-1 to X-50][book_jenkins_landis_miller_2003], the vehicle compilation is [Miller 2001 The X-Planes, X-1 to X-45][book_miller_2001], and the vertical take-off context is [Rogers 1989 VTOL, Military Research Aircraft][book_rogers_1989].

One more thing separates it from everything before it in this series. **It flew for twenty-four years on one airframe**, from February 1957 to May 1981, and the research it did in its last decade would have been unintelligible to the people who built it.

## The Research Question

Every article in this series so far has been about an aircraft built to go somewhere. The [X-1][related_post_a298_bell_x1] went faster than sound, the [X-2][related_post_a299_bell_x2] faster still, the [X-13][related_post_a310_ryan_x13] went from a hover to wingborne flight and back. **The X-14 was built to go nowhere in particular.** Its research question is not about a region of the flight envelope at all. It is this.

> How much attitude control authority does a hovering aircraft need?

### Why This Could Not Be Calculated

A designer in 1955 laying out a vertical take-off aeroplane had to choose the size of its attitude control system, and there was nothing to choose it from. The physics gives an inequality but not a threshold. The aircraft must be able to arrest any disturbance it will meet, which sets a floor, and it must not spend so much of its propulsion on control that it cannot lift anything, which sets a ceiling. Writing the control power as CP, the worst disturbance the vehicle must overpower as $\ddot{\theta}_{d}$, and the thrust the control system may consume as a fraction $\beta$ of the whole,

$$\ddot{\theta}_{d} \;<\; \text{CP} \;<\; \text{CP}\big(\beta_{\max}\big), \qquad \beta_{\max} = \frac{T - W}{T}$$

where the upper bound is whatever control power the remaining thrust margin can buy. **Between those two bounds, over more than an order of magnitude, the answer depends on whether a human being can fly it.**

That is not a rhetorical difficulty. It is a structural one. The quantity being sought is a property of a closed loop containing a person, and the person's transfer characteristics are not derivable from the airframe. [Anderson 1960][research_anderson_1960] surveys the state of handling-qualities criteria for vertical take-off aircraft at exactly this moment and finds the criteria absent rather than merely uncertain. [Tapscott 1960, Criteria for primary handling qual][research_tapscott_1960_2] attempts to state them and is explicit that the supporting data are thin.

**The absence persisted long enough to generate a literature about the absence.** [Clark 1964][research_clark_1964] and [Westbrook 1964][research_westbrook_1964] both report research on vertical take-off handling-qualities criteria rather than the criteria themselves. [Curry et al 1965][research_curry_1965] offers suggested requirements, the qualifier doing real work. [Goldberger 1966][research_goldberger_1966] asks, four years after the X-14A's first results, about the relative importance of the low-speed control requirement, which is not a question a settled field asks. [Carpenter and Jenny 1964][research_carpenter_jenny_1964] proposes a statistical approach to low-speed control criteria, which is an admission that the deterministic approach had not produced one. The same problem was recognised for spacecraft attitude control at the same time in [Besco 1964][research_besco_1964], where the aerodynamic term is absent for a different reason and the human term is identical.

### Why the Question Forces an Instrument

If the answer is a threshold in a human response, then locating it requires crossing it. A pilot flying an aircraft with adequate control power reports that the aircraft is adequate, which establishes an upper bound on the requirement and nothing else. **To find where adequacy ends, the aircraft must be made inadequate while the pilot is flying it**, and then made adequate again, and the pilot must be asked about both.

No ordinary aeroplane can do this. Its control power is a fixed consequence of its nozzle sizes, its bleed capacity, and its inertias. Changing it means rebuilding it, and rebuilding it changes twenty other things at the same time, so that a difference in pilot opinion cannot be attributed to the variable of interest.

**What is required is an aircraft in which control power is an adjustable parameter and everything else is held constant**, which is the definition of a variable-stability aircraft. [Key et al 1965][research_key_1965] states the case for the type directly, treating variable-stability aeroplanes as research instruments rather than as aircraft. The X-14 is the first one built for the vertical take-off problem.

The technique itself was not new. [Harper 1955][research_harper_p_1955] reports flight evaluations of longitudinal handling qualities in a variable-stability jet fighter two years before the X-14 first hovered, so the method existed and had been applied to conventional flight. What had not been done was applying it where the aerodynamic terms vanish, and the parallel attempt on a rotorcraft is [Garren and Kelly 1965][research_garren_kelly_1965], which applied a model-following technique to a variable-stability helicopter for the same purpose. [Mcgregor and Smith 1965][research_mcgregor_smith_1965] describes the same programme pursued independently in Canada with airborne simulators.

### The Inversion This Represents

It is worth being precise about how unusual this is, because it inverts the relationship between a research aircraft and its research question that the rest of this series has taken for granted.

In the ordinary case the aircraft is dimensioned so that it can reach the condition of interest. The [X-1][related_post_a298_bell_x1] carries the propellant and the structure it needs to exceed the speed of sound, and every subsystem is sized against that. The aircraft is the means and the flight condition is the end.

In the X-14 the flight condition is trivial. Hovering ten feet above a ramp at Moffett Field is not a frontier. **The aircraft is not the means of reaching a condition. It is the apparatus in which a variable is swept**, and the frontier it approaches is not aerodynamic but experimental. What it must do well is not fly, but change, repeatably, on command, while a pilot who knows what is being changed forms an opinion about it.

This has a consequence that runs through the whole article. **A research aircraft built as an instrument has no mission to fail at.** The flight-test record of the X-1 is a record of speeds reached. The flight-test record of the X-14 is a record of experiments run, and the interesting question about it is not whether it flew well but whether the numbers it produced were right.

## Programme Origin

In July 1955 Bell Aircraft received an Air Force contract for research into vertical take-off and landing, and construction of the Bell Model 68 began about three months later. The aircraft was assigned the designation X-14 and the serial 56-4022, and only one was built.

### The Cheapest Possible Airframe

The design decisions read as parsimony and are better read as focus. Bell took the wings, ailerons, and landing gear from a Beechcraft Bonanza and the tail surfaces from a T-34 Mentor, and built a new fuselage of duralumin around two turbojets mounted side by side at the centre of mass. The cockpit was open. The undercarriage was fixed.

Every one of those choices removes a variable that the experiment does not care about and would have had to pay for. **A retractable undercarriage would have added weight to an aircraft whose whole research programme was bounded by its thrust margin**, and would have bought speed the programme had no use for. Borrowed wings from a light aircraft in production removed a design and stress-analysis task whose outcome the experiment was indifferent to.

The contrast with the [X-13][related_post_a310_ryan_x13] is instructive. Ryan built a purpose-designed delta airframe to demonstrate a manoeuvre, and the airframe was the demonstration. Bell built a parts-bin airframe to carry a control system, and the control system was the point. **Both are correct engineering, and the difference between them is entirely a difference in what was being asked.**

### The Two Institutions

The programme has a clean division. The Air Force paid for an aircraft that could hover and transition, and Bell delivered one. What the aircraft then did for twenty-two years was decided elsewhere.

The aircraft was assigned to the NASA Ames Research Center at Moffett Field on 2 October 1959 and stayed there until it was destroyed. **Ames was not interested in the X-14 as a vertical take-off aeroplane.** It was interested in it as a flying laboratory for handling qualities, which is a subject Ames had already been pursuing with fixed-wing aircraft. [Creer et al 1959][research_creer_1959] is a pilot-opinion study of lateral control requirements for fighters published the same year the X-14 arrived, and it is the methodological ancestor of everything the X-14 subsequently did. The method was established. What was missing was a vehicle that could apply it to hovering.

### The Aircraft Was Not Alone

The X-14 is the first variable-stability aircraft applied to the hovering problem and it was not the last, and the family it belongs to is worth naming because it establishes that the method rather than the aircraft was the durable contribution.

[Key et al 1965][research_key_1965] surveys the flight research use of variable-stability aeroplanes for vertical take-off flying qualities. [Eney 1967][research_eney_1967] reports Navy variable-stability studies of longitudinal handling qualities, and [Rhoads 1967][research_rhoads_1967] an in-flight simulation and pilot evaluation of landing approach handling qualities, extended in [Rhoads 1970][research_rhoads_1970] to cockpit controller configurations. [Newell et al 1963][research_newell_1963] describes a variable-drag device fitted to a variable-stability aircraft, which indicates how far the technique was pushed beyond attitude dynamics.

The type spread to large aircraft as well as small. [Person and Robbins 1965][research_person_robbins_1965] and [Baska and Robbins 1966][research_baska_robbins_1966] describe the variable-stability simulation system fitted to a Boeing 367-80, first for a supersonic transport programme and then for a large transport programme, and [Condit et al 1966][research_condit_1966] compares in-flight against ground-based simulation of the handling qualities of very large aeroplanes in landing approach. [Motyka 1975][research_motyka_1975] assesses a T-2 as a high-angle-of-attack in-flight simulator, which is the technique applied to a third regime where the aerodynamics misbehave.

The control law itself became a subject. [Merrick 1977][research_merrick_1977] studies an implicit model-following controller applied to lift-fan vertical take-off aircraft, [Deets 1978][research_deets_1978] compares optimal-regulator and conventional setup techniques for a model-following simulator control system, and [Takahashi et al 1994][research_takahashi_1994] develops a model-following law for in-flight simulation two decades later. **The X-14B's digital system sits in the middle of that development rather than at the end of it.**

The direct successor for the vertical take-off problem was the X-22A, a tilting-ducted-propeller research aircraft described in [Marchese 1963][research_marchese_1963] and whose variable-stability capabilities for flying-qualities work are reported in [Aiken et al 1977][research_aiken_1977]. [Smith et al 1973][research_smith_1973] reports a flight investigation of longitudinal short-term dynamics for short take-off landing approaches using it, and [Smith 1974][research_smith_1974] summarises the flying-qualities research the aircraft supported. **The X-22A could do what the X-14 did with more authority and more endurance**, and its existence from the late 1960s onward is part of why the X-14B's later work moved toward control-law concepts rather than toward refining the original criteria.

The helicopter branch of the same family is reviewed in [Hindson 1982][research_hindson_1982], which considers past applications and future potential of variable-stability research helicopters, and continues in [Watson and Hindson 1988][research_watson_hindson_1988] on rotorcraft pitch-roll cross coupling. A helicopter has aerodynamic damping a jet-lift aircraft lacks, so the two branches are not interchangeable, but the method is identical.

### What the Field Already Knew in 1955

It is worth recording what was and was not available when Bell began, because the X-14's contribution is easy to overstate.

The configuration question had been worked over thoroughly. [Div 1956][research_div_1956] and [Irvin and Swan 1956][research_irvin_swan_1956] compare types and estimate weights for competing vertical take-off transport layouts, and [McCormick and Mallen 1956][research_mccormick_mallen_1956] treats tilt-wing design considerations. The field had a textbook within a few years in [Campbell 1962][research_campbell_1962], a conference series of which [NACA 1960][research_naca_1960] is one volume, and survey treatments in [Kirby 1961][research_kirby_1961] on propeller-driven configurations and [Brown 1965][research_brown_1965] on low-disc-loading designs. The tilt-wing branch alone supported [Nichols 1963][research_nichols_1963], [Martin 1963][research_martin_1963], [Tosti 1961][research_tosti_1961], and [Longhurst 1966][research_longhurst_1966]. **Everyone knew how to lay out a vertical take-off aircraft. Nobody knew how to size its control system.**

The hovering-stability problem had also been posed cleanly, though for rotorcraft rather than for jets. [Miller 1948][research_miller_1948] treats helicopter control and stability in hovering flight, and the subject was worked over through [Payne 1955][research_payne_1955] and [Bramwell 1956][research_bramwell_1956]. The flying-platform experiments of [Albachten 1956][research_albachten_1956] and [Sissingh 1956][research_sissingh_1956] address hovering stability for a vehicle with no wing at all. **What none of these could supply is the jet-lift case, in which there is no rotor to provide damping and no propeller slipstream to provide control.**

The specific problem of attitude control on a jet-lift aircraft was recognised and named. [Baxter and Finvold 1958][research_baxter_finvold_1958] addresses jet engine control and attitude control in vertical-attitude aircraft, which is the same problem in the tail-sitting configuration the [X-13][related_post_a310_ryan_x13] used. Scale-model work was underway, including the free-flight tests of a one-fifth-scale Ryan X-13 model reported in [Smith 1958, Hovering and Transition Flight Tes][research_smith_1958_2].

What was missing is exactly what the X-14 supplied, and [Anderson 1960][research_anderson_1960] and [Tapscott 1960][research_tapscott_1960] both say so in the same year, the first by examining the criteria and finding them inadequate and the second by proposing criteria and being explicit about the thinness of the supporting data.

## Sizing From First Principles

The keystone relationship is short enough to write in one line and it is worth writing carefully, because almost everything that follows is a consequence of it.

### Control Power Is an Acceleration

The moment a control system can produce is a force multiplied by a distance. What matters to the pilot is not that moment but the angular acceleration it produces, because the pilot is closing a loop on attitude. So the quantity of interest is

$$\text{CP} = \frac{M_{\text{control}}}{I}$$

where $M_{\text{control}}$ is the maximum moment the control system can generate about an axis and $I$ is the moment of inertia about that axis. The units are radians per second squared. [Greif et al 1972][research_greif_1972] defines it in exactly these terms, as control moment divided by moment of inertia.

The inertias and derivatives that populate this relation were themselves a measurement problem. [Rampy 1966][research_rampy_1966] identifies which stability derivatives actually matter in hover and transition, and the techniques for obtaining them are treated in [Barzda 1966][research_barzda_1966] on low-frequency oscillation methods, [Owen and Cox 1966][research_owen_cox_1966] on measuring oscillatory derivatives on jet-blowing models, and [Williams and Butler 1964][research_williams_butler_1964] on the wind-tunnel techniques the whole field depended on.

For a pair of nozzles acting differentially at a distance $\ell$ either side of the centre of mass, the moment is

$$M_{\text{control}} = 2 F \ell$$

so the control power delivered by a given nozzle thrust is

$$\text{CP} = \frac{2 F \ell}{I}$$

**This normalisation is the reason the X-14's results transfer to other aircraft at all.** A moment expressed in newton metres is a fact about one airframe. The same moment divided by that airframe's inertia is a statement about how quickly attitude responds, and a pilot flying two different aircraft with the same control power and the same damping is, to a first approximation, flying the same aircraft. The criterion is stated in radians per second squared precisely so that it can be carried from the vehicle that measured it to vehicles that did not.

The claim being made is that the pair of numbers is sufficient. Two aircraft whose attitude dynamics satisfy

$$\ddot{\theta}_{1} = \text{CP} \, u - \frac{D}{I}\dot{\theta}_{1}, \qquad \ddot{\theta}_{2} = \text{CP} \, u - \frac{D}{I}\dot{\theta}_{2}$$

with the same CP and the same $D/I$ produce identical attitude histories for identical inputs, whatever their masses, spans, or nozzle arrangements. **The whole transferability of the criterion rests on that statement and on nothing else**, and the places where it fails are the subject of a later section.

### The Second Variable Is Damping

Control power alone does not determine the response. An aircraft whose attitude rate is opposed by a restoring effect behaves differently from one whose attitude rate is opposed by nothing. In hovering flight there is no aerodynamic damping worth the name, because damping in pitch and roll comes from the change in local incidence produced by rotation, and at zero airspeed there is no incidence to change. So the damping present in a hover is whatever the control system synthesises.

Writing the attitude dynamics about one axis with a rate-proportional term,

$$I \ddot{\theta} = M_{\text{control}} - D \dot{\theta}$$

and dividing by the inertia,

$$\ddot{\theta} = \text{CP} \, u - \frac{D}{I} \dot{\theta}$$

where $u$ is the normalised control input between minus one and one and $D/I$ has units of inverse seconds. **The pair of numbers CP and $D/I$ specifies the attitude response**, and the X-14A's experimental programme was a sweep over that pair.

Transforming gives the attitude response to control as

$$\frac{\theta(s)}{u(s)} = \frac{\text{CP}}{s\left(s + \dfrac{D}{I}\right)}$$

which has a pole at the origin and a second at the damping value, so the system carries a characteristic time

$$\tau = \frac{I}{D} = \left(\frac{D}{I}\right)^{-1}$$

The two dampings the X-14A actually flew, 0.45 and 0.59 per second, correspond to

$$\tau = \frac{1}{0.45} = 2.22 \text{ s}, \qquad \tau = \frac{1}{0.59} = 1.69 \text{ s}$$

The angular rate following a step of full control approaches its limit exponentially,

$$\dot{\theta}(t) = \frac{\text{CP}}{D/I}\left(1 - e^{-t/\tau}\right)$$

and the steady rate reached at full control is the ratio of the two,

$$\dot{\theta}_{\text{max}} = \frac{\text{CP}}{D/I}$$

which is worth noting because it means the two parameters cannot be varied entirely independently in their effect on what the pilot sees. Raising the damping at fixed control power lowers the achievable rate. At the maximum control power the two flown dampings give

$$\frac{2.0}{0.45} = 4.44 \text{ rad/s}, \qquad \frac{2.0}{0.59} = 3.39 \text{ rad/s}$$

or 255 and 194 degrees per second, both far beyond anything a hovering pilot would use, which is the first hint that the damping mattered through the transient rather than through the steady state.

**With no damping at all the attitude is a pure double integrator**,

$$\ddot{\theta} = \text{CP} \, u \quad \Longrightarrow \quad \theta(t) = \tfrac{1}{2}\,\text{CP}\, t^{2}$$

so a second of full control at 2.0 radians per second squared banks the aircraft through

$$\tfrac{1}{2} \times 2.0 \times 1^{2} = 1.0 \text{ rad} = 57.3 \text{ degrees}$$

**This is the condition a hovering jet-lift aircraft is in unless something synthesises damping for it**, and it is worth holding on to, because it decides the order of the loop the pilot is closing.

### What the Control Power Was Bought With

On the X-14 the attitude control moments came from compressed air bled from the compressors of the turbojets and ejected through nozzles at the wingtips and the tail. [Drinkwater et al 1965][research_drinkwater_1965] describes the arrangement, and [Keller 1969][research_keller_1969] and [Friend 1964][research_friend_1964] treat reaction controls for jet-lift aircraft as a design problem in their own right. **[Patierno and Asdurian 1965][research_patierno_asdurian_1965] states the trade in its title**, addressing the impact of control provisions on the mission performance of jet vertical take-off aircraft using reaction control systems, which is the subject of the next several pages here. The effectiveness of such jets was still being measured in the wind tunnel a quarter of a century later in [Riley et al 1989][research_riley_1989], for the hover and transition of a short take-off vertical landing fighter concept.

One property of a reaction control system that this article does not otherwise treat deserves naming, because it bears on the fan result below. A nozzle valve that is effectively on or off rather than proportional makes the closed loop a relay system, and relay systems limit-cycle. [Dahl et al 1962][research_dahl_1962] analyses limit cycles in reaction-jet attitude control subject to external torques, which is the failure mode a bang-bang attitude control invites.

The thrust of a reaction nozzle follows from the mass flow through it and the velocity at which that mass leaves,

$$F = \dot{m} \, v_{e}$$

and for a choked convergent nozzle supplied at total temperature $T_{0}$ the exit velocity is set by the temperature and the gas properties,

$$v_{e} = \sqrt{\frac{2 \gamma}{\gamma + 1} R T_{0}}$$

so that hotter bleed gives more thrust per unit of mass flow. The mass flow itself, for a choked convergent nozzle of throat area $A$ supplied at total pressure $p_{0}$, is

$$\dot{m} = A \, p_{0} \sqrt{\frac{\gamma}{R T_{0}}} \left(\frac{2}{\gamma + 1}\right)^{\frac{\gamma + 1}{2(\gamma - 1)}}$$

and the thrust per unit mass flow, which is the figure of merit for the whole arrangement, is just the exit velocity,

$$\frac{F}{\dot{m}} = v_{e}$$

That is the whole design freedom, and it is not much of one, because the bleed temperature is whatever the compressor stage delivers. At a representative compressor delivery temperature of 500 kelvin the exit velocity is

$$v_{e} = \sqrt{\frac{2 \times 1.4}{2.4} \times 287 \times 500} = 409 \text{ m/s}$$

so producing the 150 pounds of thrust the wingtip station needed requires

$$\dot{m} = \frac{667}{409} = 1.63 \text{ kg/s}$$

**A J85 passes roughly twenty kilogrammes per second, so one wingtip station at full deflection is asking for something like four percent of one engine's entire airflow.** That is an order-of-magnitude figure rather than a measurement, and it is offered only because it lands in the same region as the bleed penalty measured below, which is the point of computing it.

**The important point is not how the nozzle works but where the mass flow comes from.** It comes out of the engine, and the engine was going to use it to make lift.

### The Price of Control, Fixed by an Experiment

The cost of bleed is usually estimated rather than measured, because separating it from every other installation effect requires running the same engine in the same aircraft with two different bleed schedules. The X-14A programme did exactly that, for a different reason, and the result fixes the price.

[Gerdes and Rolls 1969][research_gerdes_rolls_1969] reports flight tests of tip-turbine-driven fans fitted at the wingtips as an alternative lateral control effector. The fans were rejected, for reasons taken up later in this article, but the report states that they required about half the bleed air of the reaction controls for the same thrust, and that this permitted the engines to produce four percent more thrust.

That single sentence can be inverted. The thrust delivered when a fraction $\beta$ of the flow is diverted is

$$T = T_{0}\,(1 - \beta)$$

If the thrust with full bleed is $T_{0}(1 - \beta)$ and the thrust with half the bleed is $T_{0}(1 - \beta/2)$, then the fractional gain observed is

$$\frac{\beta / 2}{1 - \beta} = 0.04$$

For a general observed gain $\delta$ on halving the bleed this rearranges to

$$\beta = \frac{2\delta}{1 + 2\delta}$$

and substituting the reported four percent,

$$\beta = \frac{2 \times 0.04}{1 + 2 \times 0.04} = 0.0741$$

**So the reaction control system on the X-14A consumed about 7.4 percent of the thrust the engines would otherwise have produced.** Call it seven to eight percent. This is a measured figure rather than an estimate, and it is the number that makes the rest of the analysis in this article concrete.

### What Seven Percent Costs a Hovering Aircraft

Seven percent of thrust sounds small. For a hovering aircraft it is not, and the reason is that a hovering aircraft's useful output is not its thrust but the difference between its thrust and its weight,

$$\Delta T = T - W$$

which for a machine with a thrust-to-weight ratio near unity is a small difference of two large numbers and is therefore extremely sensitive to any deduction from either.

During the lateral control experiments the X-14A weighed 3,700 pounds and had a thrust-to-weight ratio available of 1.1 to 1.2, which [Drinkwater et al 1965][research_drinkwater_1965] states directly. Its two General Electric J85-GE-5 engines were rated at 2,680 pounds of thrust each, or 5,360 pounds together, so the uninstalled thrust-to-weight ratio was

$$\frac{T_{\text{uninstalled}}}{W} = \frac{5{,}360}{3{,}700} = 1.449$$

against an available 1.1 to 1.2. Defining the installation efficiency as the ratio of what the aircraft got to what the engines were rated at,

$$\eta_{\text{inst}} = \frac{T_{\text{available}}}{T_{\text{uninstalled}}}$$

the two reported bounds give

$$\eta_{\text{inst}} = \frac{1.1 \times 3{,}700}{5{,}360} = 0.759, \qquad \frac{1.2 \times 3{,}700}{5{,}360} = 0.828$$

**The installation therefore lost between 17.2 and 24.1 percent of the engines' rated thrust**, and the bleed for the attitude controls is one part of that loss.

Now take the margin. At a thrust-to-weight ratio of 1.2 the aircraft can lift 740 pounds beyond its own weight. The bleed costs

$$0.0741 \times 5{,}360 = 397 \text{ pounds of thrust}$$

so without it the margin would have been 1,137 pounds. **The attitude control system consumed 34.9 percent of the aircraft's hover margin.** At a thrust-to-weight ratio of 1.1 the margin after bleed is 370 pounds, the margin before bleed would have been 767, and the control system consumed 51.8 percent of it.

$$\frac{397}{767} = 0.518, \qquad \frac{397}{1{,}137} = 0.349$$

The general form is worth having, because it is the relation a designer would use rather than the two numbers. If the control system takes a fraction $\beta$ of the uninstalled thrust and the aircraft is left with a thrust-to-weight ratio $r$, the share of the pre-bleed margin that the control system consumed is

$$\Phi = \frac{\beta \, T_{0}}{(r - 1) W + \beta \, T_{0}}$$

**The denominator contains $r - 1$, and that is the whole problem.** As the thrust-to-weight ratio approaches unity the margin vanishes while the bleed does not, so $\Phi$ approaches one and the control system consumes everything.

This is the central result of the article's sizing analysis and it deserves stating plainly. **Between a third and a half of everything the X-14A could lift beyond its own weight was spent on being controllable.** Not on payload, not on fuel, not on range. On the ability to point.

[Hoffman 1971][research_hoffman_1971] treats this cost as a subject in itself under the title of control power costs, which indicates that by 1971 the field understood the trade as central rather than incidental.

### The Floor, Which Disturbances Set

The analysis so far gives the price of control power. It does not say how much is needed, and the lower bound comes from a different place, which is that the aircraft must be able to overpower whatever is trying to upset it.

A hovering aircraft in a wind experiences a moment it did not ask for. The control system must be able to cancel that moment and still have authority left over for the pilot to manoeuvre with, so the requirement is not that control power exceed the disturbance but that it exceed it by enough.

It is worth asking how large that moment actually was, because the answer is not what the framing suggests. A steady wind of speed $V_{w}$ acting on a side area $S_{s}$ produces a force

$$F_{w} = \tfrac{1}{2}\rho V_{w}^{2} S_{s} C_{D}$$

and at ten metres per second on a representative eight square metres at a drag coefficient of 0.8 that is

$$F_{w} = \tfrac{1}{2} \times 1.225 \times 100 \times 8 \times 0.8 = 392 \text{ N}$$

As an attitude disturbance this is trivial. Acting through an offset of a metre it produces

$$\frac{392 \times 1.0}{3{,}333} = 0.118 \text{ rad/s}^{2}$$

which is 5.9 percent of the maximum control power. As a translational disturbance it is not trivial at all. The same force accelerates the aircraft at

$$a_{w} = \frac{392}{1{,}678} = 0.234 \text{ m/s}^{2}$$

and holding station against it requires a permanent tilt into wind of

$$\theta_{\text{trim}} = \arctan\frac{a_{w}}{g} = \arctan\frac{0.234}{9.807} = 1.36^{\circ}$$

while leaving it uncorrected for ten seconds costs

$$\tfrac{1}{2} \times 0.234 \times 100 = 11.7 \text{ m}$$

**The wind is a position problem and not an attitude problem**, which is the same conclusion the previous article reached for the [X-13][related_post_a310_ryan_x13] by a different route and on a differently shaped aircraft. The disturbance that sizes the control power is therefore the gust and the manoeuvre rather than the steady wind, which is what the experimental ratio below actually encodes.

The field settled on a working ratio and it can be read off the experimental design. [Greif et al 1972][research_greif_1972] held peak disturbance strength at 0.32 radians per second squared against a maximum roll control power of 0.8, and states the ratio explicitly as four tenths of the maximum. Writing the disturbance as a fraction $\sigma$ of the available control power,

$$\ddot{\theta}_{\text{disturbance}} = \sigma \, \text{CP}, \qquad \sigma = 0.4$$

the authority actually available to the pilot is what remains,

$$\text{CP}_{\text{pilot}} = (1 - \sigma) \, \text{CP}$$

**Sixty percent of the control power reaches the pilot and forty percent is spent standing still.** At the X-14A's maximum of 2.0 radians per second squared this leaves 1.2, and at its minimum of 0.8 it leaves 0.48.

$$0.6 \times 2.0 = 1.2, \qquad 0.6 \times 0.8 = 0.48$$

This compounds with the bleed cost in an unpleasant way. The aircraft surrenders a third to a half of its hover margin to buy control power, and then surrenders two fifths of the control power it bought to the disturbance. The two fractions multiply,

$$\Phi \times (1 - \sigma)$$

giving, at the two reported thrust-to-weight ratios,

$$0.518 \times 0.6 = 0.311, \qquad 0.349 \times 0.6 = 0.210$$

**So between 21 and 31 percent of the aircraft's entire hover margin ends up as manoeuvring authority in the pilot's hands, and the rest is overhead.** It is small through two independent multiplications rather than one.

### The Roll Inertia, Recovered From Two Reports

The article needs the aircraft's roll inertia to say anything quantitative about what the tested control powers meant in terms of force. No source consulted states it. It can be recovered, because two independent reports state quantities that together determine it.

[Drinkwater et al 1965][research_drinkwater_1965] states that the maximum lateral control power tested was 2.0 radians per second squared. [Gerdes and Rolls 1969][research_gerdes_rolls_1969] states that the replacement wingtip fans were designed for 150 pounds of thrust each. Taking the fans as sized to reproduce the existing maximum authority, and placing them at the wingtips with a moment arm slightly inboard of the semi-span,

$$\ell = 0.97 \times \frac{b}{2} = 0.97 \times \frac{10.300}{2} = 4.995 \text{ m}$$

two fans operating differentially give a rolling moment of

$$M = 2 F \ell = 2 \times 667.2 \times 4.995 = 6{,}666 \text{ N m}$$

and at 2.0 radians per second squared the inertia must be

$$I_{x} = \frac{M}{\text{CP}} = \frac{6{,}666}{2.0} = 3{,}333 \text{ kg m}^{2}$$

The corresponding radius of gyration, at a test mass of 1,678 kilogrammes, is

$$k_{x} = \sqrt{\frac{I_{x}}{m}} = \sqrt{\frac{3{,}333}{1{,}678}} = 1.409 \text{ m}$$

or, as the ratio that makes it checkable,

$$\frac{k_{x}}{b} = \frac{1.409}{10.300} = 0.137$$

which is 13.7 percent of the span. The recovery in general form is

$$I_{x} = \frac{2 F \ell}{\text{CP}_{\max}}, \qquad \frac{k_{x}}{b} = \frac{1}{b}\sqrt{\frac{2 F \ell}{m \, \text{CP}_{\max}}}$$

**That number is the check.** A roll radius of gyration between roughly ten and sixteen percent of span is what an aircraft with its heavy items on the centreline and light wings should have, and the X-14 had two engines side by side at the centre of mass and borrowed light-aircraft wings. The recovered value lands in the middle of the expected band. The recovery is therefore consistent, and the more interesting inference is the one that follows from the fan sizing rather than from the inertia.

**The fans were specified at exactly the aircraft's maximum tested control power and not above it.** Whoever wrote the specification was not trying to give the X-14A more authority. They were trying to give it the same authority for less bleed, which confirms that bleed, and not control power, was understood as the binding constraint.

### Why Control Power Gets Harder as Aircraft Get Bigger

The relation for control power can be pushed through a scaling argument, and the result explains a great deal about why jet-lift vertical take-off never grew.

With reaction nozzles at the wingtips the control moment is the differential force multiplied by the span,

$$M = F b$$

and the inertia is the mass multiplied by the square of a radius of gyration that is itself proportional to span,

$$I_{x} = m k_{x}^{2}, \qquad k_{x} \propto b$$

so the control power is

$$\text{CP} = \frac{M}{I_{x}} \propto \frac{F b}{m b^{2}} = \frac{F}{m b}$$

A hovering aircraft has thrust proportional to weight and therefore to mass,

$$T \approx W = m g \quad \Longrightarrow \quad T \propto m$$

and at a fixed bleed fraction the reaction force is proportional to thrust,

$$F = \beta \, T \propto \beta \, m g$$

so $F \propto m$ and

$$\text{CP} \propto \frac{1}{b}$$

**Control power at a fixed bleed fraction is inversely proportional to span.** Doubling the linear size of a jet-lift aircraft halves its control power, and holding the control power fixed requires doubling the bleed fraction.

The consequences are severe and they are arithmetic. The X-14A bought 2.0 radians per second squared for 7.4 percent bleed at a span of 10.3 metres. The same control power at twice the span costs 14.8 percent, at three times 22.2 percent, and at four times 29.6 percent.

$$\beta(b) = 0.0741 \times \frac{b}{10.3}$$

Set that against the thrust margin available. A generous jet-lift aircraft has twenty percent of thrust to spare over its weight. The bleed consumes the whole of it at

$$b = 10.3 \times \frac{0.20}{0.0741} = 27.8 \text{ m}$$

**A jet-lift aircraft with reaction controls at the wingtips runs out of aircraft at somewhere around twenty-eight metres of span.** The Dornier Do 31, the largest jet-lift vertical take-off aircraft ever flown, spanned about eighteen metres, at which the relation demands 12.9 percent bleed. It is not a coincidence that the type stopped there.

This conclusion was reached independently and contemporaneously, and by more than one group. [Johnston and Friend 1965][research_johnston_friend_1965] is titled for the effect of size on hover and low-speed handling qualities, and [Johnston et al 1965][research_johnston_1965] reports a study of size effects on vertical take-off handling-qualities criteria in the same year. **Two papers on the size dependence within three years of the X-14A's first results is not a coincidence**, and it indicates the field had recognised the scaling problem as soon as it had a criterion to scale.

The reappraisals that followed carry the same concern. [Smith 1966, Vtol control power requirements re][research_smith_1966_2] revisits the requirements four years after they were determined, [Hoffman 1971][research_hoffman_1971] treats the cost of control power as a subject in itself, and [Stevens and Roskam 1985][research_stevens_roskam_1985] is still investigating vertical-axis control power requirements for shipboard landing two decades later.

### What the Criterion Costs an Arbitrary Aircraft

The scaling relation can be turned into the calculation a designer would actually have performed, which is the calculation the X-14A's number existed to enable.

Take an aircraft of mass $m$ and span $b$ whose roll radius of gyration is a fraction $\kappa_{r}$ of its span, with reaction nozzles at the wingtips. Meeting a control power CP requires a tip force of

$$F_{\text{tip}} = \frac{\text{CP} \, m \, \kappa_{r}^{2} b^{2}}{2 \times 0.97 \times b/2} = \frac{\text{CP} \, m \, \kappa_{r}^{2} b}{0.97}$$

**The force grows with the product of mass and span**, which is the scaling result in the form a designer meets it. Using the value of $\kappa_{r}$ recovered above, 0.1368, this reproduces the X-14A's 150 pounds per tip exactly, which is a consistency check rather than a new result because the constant was calibrated on that aircraft.

Applied to larger aircraft the numbers become difficult very quickly. A vehicle of fifteen metres span weighing 12,000 pounds needs 708 pounds of thrust at each wingtip to reach 2.0 radians per second squared. A vehicle of eighteen metres span weighing 50,000 pounds, which is roughly the scale of the largest jet-lift aircraft flown, needs

$$F_{\text{tip}} = 3{,}542 \text{ pounds of thrust at each wingtip}$$

**That is a small jet engine at the end of each wing, provided as bleed from engines in the fuselage, purely to point the aircraft.** The conclusion drawn earlier from the bleed fraction is the same conclusion reached from the force, and reaching it twice by different routes is the reason this article treats the scaling result as the most durable thing the X-14's numbers imply.

### What the Bleed Actually Bought

One ratio is worth recording because it states the efficiency of the whole arrangement. The X-14A surrendered 397 pounds of engine thrust to obtain, at the wingtips, a peak differential roll force of about 300 pounds.

$$\frac{300}{397} = 0.756$$

**Roughly three quarters of a pound of control force for every pound of thrust given up**, and the same bleed also fed the pitch and yaw nozzles, so the figure understates the total return and overstates the cost attributable to any single axis. It is nonetheless a poor exchange rate, and it is the quantity the tip-turbine fans were built to improve.

## Dependent Systems

Each subsystem was dimensioned against the keystone, and the ordering below is by dependency rather than by convention. The propulsion determines the control authority available, the control authority determines what the variable-stability system can synthesise, and what it can synthesise determines the experiment.

### Propulsion and the Diverter

The aircraft was re-engined twice, and neither change was about performance in the ordinary sense.

The original X-14 flew on two Armstrong Siddeley Viper 8 turbojets. **Sources disagree on their rating.** Several give 1,750 pounds of thrust each and at least one gives 1,560. The disagreement matters, and this article does not resolve it, because both figures produce the same conclusion.

At 1,750 pounds each the pair gives 3,500 pounds. At 1,560 each the pair gives 3,120. Against the 3,700 pound weight at which the aircraft later did its research, those are thrust-to-weight ratios of

$$\frac{3{,}500}{3{,}700} = 0.946, \qquad \frac{3{,}120}{3{,}700} = 0.843$$

**Both are below one.** The original X-14 could not have hovered at the weight the X-14A hovered at, on either reading of its engine rating, and that is before any allowance for bleed or for the losses in turning the exhaust. Whatever the aircraft did in 1957 and 1958, it did light, and the margin was not a margin in any useful sense.

Replacing the Vipers with two General Electric J85-GE-5 engines at 2,680 pounds each raised the uninstalled ratio to 1.449, and the later J85-GE-19 installation at 3,015 pounds each raised it to 1.630. **The re-engining was not an upgrade to an aircraft that already worked. It was the precondition for the research programme existing at all**, because a variable-stability aircraft must be able to give away control power to the experiment and still fly, and an aircraft with no thrust margin has nothing to give away.

The exhaust was turned by cascade-type diverters at the centre of mass, which the pilot could set for vertical or horizontal thrust. The device had a research literature of its own, including [Erwin et al 1964][research_erwin_1964] on a tandem cascade thrust-vectoring programme and [Davis and Spicer 1965][research_davis_spicer_1965] on determining the thrust vector of a fixed-nozzle engine on a six-component stand, which is the measurement problem that turning the exhaust creates. The wider principle of an engine that supplies both lift and thrust is set out in [Denning 1962][research_denning_1962], and the control of engines used this way in [Sellers and Szuch 1973][research_sellers_szuch_1973]. The propulsion requirements of the configuration as a class are surveyed in [Kohn 1972][research_kohn_1972] and [Ciepluch et al 1979][research_ciepluch_1979].

Turning a jet through ninety degrees is not free. Writing the turning efficiency as $\eta$, the vertical thrust available is

$$T_{v} = \eta \, T$$

and combining that with the bleed gives the thrust actually available for lifting,

$$T_{\text{lift}} = \eta \, (1 - \beta) \, T$$

During the transition the diverter sits at intermediate angles, and the thrust splits into components. At a deflection $\delta$ measured from the vertical,

$$T_{v} = \eta \, T \cos\delta, \qquad T_{h} = \eta \, T \sin\delta$$

so the vertical component the aircraft still needs to support itself and the horizontal component that accelerates it are not independent,

$$\left(\frac{T_{v}}{\eta T}\right)^{2} + \left(\frac{T_{h}}{\eta T}\right)^{2} = 1$$

**The aircraft cannot accelerate forward without giving up lift**, which is why the transition has to be flown as a trajectory rather than as a switch, and why a thrust-to-weight ratio comfortably above one is needed to fly it at all.

At a turning efficiency of 0.95 and the measured bleed fraction, the J85-GE-5 installation yields

$$\frac{T_{\text{lift}}}{W} = 0.95 \times 0.9259 \times \frac{5{,}360}{3{,}700} = 1.274$$

against a reported available ratio of 1.1 to 1.2. **The two agree to within about six to fifteen percent**, and the residual is what one would expect from inlet losses, ambient conditions, and the accessory loads not accounted for here. That the simple product of two efficiencies lands this close to the reported figure is a check that the bleed fraction inverted from the fan report is of the right size.

The same arithmetic applied to the later engines shows what the second re-engining bought. The J85-GE-19 installation gives an uninstalled ratio of

$$\frac{6{,}030}{3{,}700} = 1.630$$

and after the same two deductions

$$0.95 \times 0.9259 \times \frac{6{,}030}{3{,}700} = 1.434$$

**The X-14B could therefore afford roughly 0.16 more in thrust-to-weight ratio than the X-14A**, which at a constant weight is about 590 pounds of additional lift, and it is that margin rather than the digital computer that set how much authority the later experiments could give away.

[Rolls 1965, Jet Vtol power plant experience du][research_rolls_1965_4] reports the powerplant experience from the X-14A flight test programme directly, and is the primary source on how the installation actually behaved.

There is a further loss that this article accounts for only qualitatively. A jet directed downward beneath a wing entrains air, lowers the pressure on the surfaces above it, and produces a download that subtracts from the thrust. [Gentry and Margason 1966][research_gentry_margason_1966] measured jet-induced lift losses on vertical take-off configurations hovering both in and out of ground effect, and the effect is a few percent of thrust for a configuration like the X-14's.

**This matters for the argument only in that it makes the accounting worse rather than better.** The bleed for the attitude controls is the largest identifiable single deduction from the hover thrust budget, and the induced loss, the cascade turning loss, and the inlet loss are additional. Every one of them competes with payload, and the article's conclusion that control consumed a third to a half of the margin is a lower bound on the total burden rather than an upper one.

Operating close to the ground adds effects that were treated as disqualifying for the configuration generally. [Dent 1966][research_dent_1966] addresses ground erosion in the operation of jet lift aircraft, which is the practical objection that a jet-lift aircraft requires a prepared surface.

### The Reaction Control System

The reaction controls were the aircraft's only means of attitude control in a hover and they were the experimental variable. Nozzles at the wingtips supplied roll, and nozzles at the tail supplied pitch and yaw.

The moment arms differ substantially between axes, which means the axes are not equally cheap. Roll acts through the semi-span, about 5.0 metres. Pitch and yaw act through the distance from the centre of mass to the tail, which on an aircraft 7.92 metres long is roughly 3.6 metres,

$$\frac{\ell_{\text{roll}}}{\ell_{\text{pitch}}} = \frac{4.995}{3.564} = 1.40$$

For a given nozzle thrust the roll moment is therefore the larger, but the roll inertia is also the larger, and which axis is cheapest in control power depends on the product of the two ratios,

$$\frac{F_{\text{pitch}}}{F_{\text{roll}}} = \frac{I_{y}}{I_{x}} \times \frac{\ell_{\text{roll}}}{\ell_{\text{pitch}}}$$

At equal inertias this is 1.40, so **the pitch nozzle must be about forty percent stronger than the roll nozzle for the same control power**, which is a consequence of the aircraft being wider than it is long.

Taking the recovered roll inertia and assuming pitch inertia of similar magnitude, since the aircraft's length and span are comparable, the tip force required to produce each of the tested control powers follows from

$$F_{\text{tip}} = \frac{\text{CP} \times I_{x}}{2 \ell}$$

giving 60.0 pounds per tip at 0.8 radians per second squared, 105.0 pounds at 1.4, and 150.0 pounds at 2.0. **These are small forces**, and that is the point worth taking away. The X-14A's entire lateral control authority at its most generous setting was three hundred pounds of thrust split between two wingtips, and buying it cost four hundred pounds of engine thrust. The efficiency of the conversion from engine thrust to control force is poor, and improving it is what the fan experiment was about.

### The Variable Stability System and Its Budget

The system that made the aircraft an instrument was installed by Ames after the aircraft arrived, in analogue form on the X-14A and in digital form on the X-14B, the latter described by [Gallagher et al 1972][research_gallagher_1972] as a model-following system.

**The analogue system has its own paper and it is easy to miss, because its title names the configuration rather than the aircraft.** [Hegarty et al 1965][research_hegarty_1965] describes a system for varying the stability and control of a deflected-jet fixed-wing vertical take-off aircraft, which is the X-14A and no other machine. It is the primary description of the apparatus that produced every number in this article.

The principle is feedback to the same effectors the pilot commands. To synthesise a damping derivative that the airframe does not possess, the system measures the angular rate and commands a control moment opposing it. To synthesise a different control power, it scales the pilot's command before passing it on.

**The two are not independent, and the reason is that they share an authority budget.** The nozzles can produce a bounded moment. Every newton metre the feedback loop spends opposing rate is a newton metre the pilot cannot have. Writing the synthesised damping as $D/I$ and the roll rate as $p$, the control power remaining to the pilot is

$$\text{CP}_{\text{pilot}} = \text{CP}_{\text{total}} - \frac{D}{I} \, p$$

At the total control power of 2.0 radians per second squared and a synthesised damping of 0.59 per second, a roll rate of 30 degrees per second consumes

$$0.59 \times 0.5236 = 0.309 \text{ rad/s}^{2}$$

leaving 1.691, or 84.6 percent. At a damping of 1.5 per second the same rate leaves 60.7 percent. And the rate at which the damping loop exhausts the entire budget on its own is

$$p_{\text{exhaust}} = \frac{\text{CP}_{\text{total}}}{D/I}$$

which is 194 degrees per second at the lower damping and 76 degrees per second at the higher.

The fraction left is more useful than the difference,

$$\frac{\text{CP}_{\text{pilot}}}{\text{CP}_{\text{total}}} = 1 - \frac{(D/I)\,p}{\text{CP}_{\text{total}}}$$

and inverting it gives the constraint the experimenter actually faced. Reserving a fraction $\lambda$ of the authority for the pilot caps the damping that can be synthesised at a working roll rate,

$$\left(\frac{D}{I}\right)_{\max} = \frac{(1 - \lambda)\,\text{CP}_{\text{total}}}{p}$$

Reserving half the authority at thirty degrees per second caps it at

$$\frac{0.5 \times 2.0}{0.5236} = 1.91 \text{ per second}$$

**The instrument could not simultaneously offer high damping and high control power, and the ceiling on the product is set by the nozzles rather than by the electronics.**

**This explains a sentence in the source that would otherwise read as modesty.** [Drinkwater et al 1965][research_drinkwater_1965] says the tested conditions covered, to the ability of the X-14A, a high, medium, and low control power for each of a high, medium, and low damping. The qualifier is not politeness. The high-damping and high-control-power corner of the experimental grid is the corner where the two demands on the nozzles add, and the aircraft could not reach all of it. **The instrument's own authority limit truncated its experimental space**, and it truncated it precisely in the region where a designer most wanted an answer.

### The Position Loop the Pilot Actually Closed

The variable being measured was attitude authority, and the task the pilots were rated on was holding a position. Those are not the same thing, and the relation between them is what makes hovering hard.

The previous article established the structure for the [X-13][related_post_a310_ryan_x13], and writing it as a transfer function rather than as a chain of integrals shows it needs one correction and gains a result the X-14 is uniquely placed to supply.

A hovering aircraft has no aerodynamic restoring moment, so with the damping set to zero attitude is a double integrator driven by control,

$$\ddot{\theta} = \text{CP} \, u$$

and horizontal position is driven by attitude,

$$\ddot{x} = g \tan\theta \approx g \theta$$

Composing the two,

$$\frac{x(s)}{u(s)} = \frac{g \, \text{CP}}{s^{4}}$$

**Position is the fourth integral of the pilot's control input, not the third.** The previous article described this as a third-order loop, on the reasoning that attitude is the integral of what the control does. That is the step to check. A reaction nozzle produces a moment, and a moment produces angular acceleration, so attitude is the double integral of control rather than the single integral, and the loop from stick to position is fourth order.

**The reconciliation is that the earlier description holds at low frequency and only there**, and the parameter that decides where the boundary falls is the damping. Restoring the rate term,

$$\frac{x(s)}{u(s)} = \frac{g \, \text{CP}}{s^{3}\left(s + \dfrac{D}{I}\right)}$$

Below the break frequency $D/I$ the bracket is dominated by the constant, and the loop behaves as

$$\frac{x(s)}{u(s)} \approx \frac{g \, \text{CP}}{(D/I)\, s^{3}} \qquad \text{for} \quad \omega \ll \frac{D}{I}$$

which is third order and is the case the previous article described. Above it the bracket is dominated by $s$ and the loop is fourth order. **So hovering is a third-order problem or a fourth-order one depending on how much damping the aircraft has, and an aircraft with no aerodynamic damping and no artificial damping is in the harder case.**

This is not a quibble about counting. The two cases differ in what the pilot must supply. A fourth-order plant requires the pilot to generate two derivatives of lead to stabilise it rather than one, and a human being generating lead is a human being working hard. **It is the clearest available explanation of why [Greif et al 1972][research_greif_1972] found that attitude stabilisation gives the best handling qualities for the least control power**, because attitude stabilisation does not merely help the pilot, it removes two orders from the plant they are closing around.

The X-14A is the only aircraft in this series that could have demonstrated the distinction, because it is the only one whose damping was a dial.

The loop closure was observed rather than merely postulated. [Lollar and Matous 1963][research_lollar_matous_1963] reports observed pilot-vehicle loop-closure characteristics for hovering aircraft control, which is the measurement that the analysis above predicts the shape of. The engineering response was to stop asking the pilot to close it unaided, and that response has a continuous literature: [Elliott and Schreiber 1964][research_elliott_schreiber_1964] on improving the stability of hovering aircraft, [Dukes 1970][research_dukes_1970] on feedback control of vertical take-off aircraft, [Kelly et al 1977][research_kelly_1977] on a vertical-velocity command system, and [Stapleford 1980][research_stapleford_1980] on velocity command with position hold, which by then had become the recommended concept for hovering. [Merrick 1982][research_merrick_1982] is the same idea reported from the X-14B itself. **The whole sequence is a retreat from the raw fourth-order plant toward something a person can fly**, and every step buys that with control authority.

Two consequences follow, and both bear on how the criterion should be read.

The first is that attitude errors do not merely make the aircraft look untidy. They integrate twice into position. Holding a mean tilt of one degree for ten seconds moves the aircraft

$$\tfrac{1}{2} \times 9.807 \times 0.01745 \times 100 = 8.6 \text{ m}$$

which is a substantial distance for a machine meant to land on a marked spot.

The second is that the pilot's control power requirement is not set by the size of the attitude excursions but by how quickly they must be reversed. **This is why control power and not control sensitivity dominated the ratings.** Sensitivity determines how much attitude a given stick displacement commands. Control power determines how fast the aircraft can stop doing something. In a loop where errors integrate twice before the pilot sees them as position, the ability to stop is worth more than the ability to start.

### The Visual Task, Which Was the Other Half

The pilot closing that loop needs to see the position error, and this turns out to be the operational problem the programme actually struggled with.

[Rolls 1965][research_rolls_1965] divides five and a half years of operating problems into two categories, and one of them is restrictions imposed on the pilot by reduced visual reference. **The aircraft's difficulties were not the ones its experiments were measuring.** [Garren et al 1965][research_garren_1965] conducted a visual flight investigation of hovering and low-speed control requirements precisely because the visual environment turns out to be a variable in its own right.

It became a research subject with a literature of its own. [Lemons and Dukes 1975][research_lemons_dukes_1975] studied the information requirements for precision hovering directly, asking not how much control the pilot needs but how much information, and [Fry et al 1969][research_fry_1969] used a six-degrees-of-freedom motion simulator for hovering tasks to separate the motion cues from the visual ones. **The two questions are the same question approached from opposite ends of the loop**, and the X-14A's criterion answers only one of them.

The engineering answer was to supply the information artificially. [Schwartz and Shearer 1964][research_schwartz_shearer_1964] sets out control and display subsystem requirements for high-performance vertical take-off aircraft, [Gold and Walchli 1974][research_gold_walchli_1974] reports a head-up display for all-weather approach and landing, and [Moen and Yenni 1975][research_moen_yenni_1975] an approach profile indicator. **A display is cheaper than control power and it addresses a different half of the same loop**, which is a trade the control-power criterion cannot express. The line runs on through [Merrick 1981][research_merrick_1981] and [Merrick 1984][research_merrick_1984] on control and display systems for instrument approach and shipboard landing, [Farris et al 1983][research_farris_1983] on shipboard operations, [Foster et al 1987][research_foster_1987] and [Foster et al 1988][research_foster_1988] on integrated control and display for transition and vertical flight, and [Dorr et al 1992][research_dorr_1992] and [Dorr et al 1994][research_dorr_1994] on head-up display guidance for Harrier approach transitions. Earlier display work that framed the problem includes [Behan and Siciliani 1965][research_behan_siciliani_1965], [Vallerie 1967][research_vallerie_1967], and [Roscoe et al 1975][research_roscoe_1975].

**What happens when the cues are removed rather than supplied is the controlled experiment**, and it was run. [Howard 1976][research_howard_1976] measures the influence of losing visual cues on pilot performance in the final approach and landing, [Haines 1980][research_haines_1980] observes head-up transition behaviour in low visibility, and [Hoh 1985][research_hoh_1985] investigates which outside visual cues are actually required for low-speed flight and hover. How much of the cue can be supplied by a simulator at all is the question of [Sinacori 1986][research_sinacori_1986] and [Parrish and Bowles 1983][research_parrish_bowles_1983].

The difficulty is structural rather than incidental. Position error is not directly sensed. It is inferred from the apparent motion of the ground, and the precision of that inference depends on texture, on lighting, on height, and on where the pilot is sitting. **A criterion measured with good visual cues is not a criterion for flying with poor ones**, and an aircraft that meets it on a marked ramp in daylight at Moffett Field may not meet it elsewhere. This limitation is inherited by every number the programme produced and is taken up again below.

### The Airframe, Which Was Deliberately Uninteresting

The borrowed Bonanza wing gave a span of 10.300 metres over an area of 16.678 square metres, an aspect ratio of 6.36, and at the 3,700 pound test weight a wing loading of 987 newtons per square metre. These are light-aircraft numbers and they were chosen to be.

In a hover the wing does nothing except add inertia and catch the exhaust. In the transition it does what a light-aircraft wing does. The X-14 was not asked to fly fast, and its recorded maximum of around 172 to 180 miles per hour is a consequence of not caring rather than a limit that was pushed against.

There is one respect in which the airframe was not neutral, and it belongs here rather than in the epistemic state because it is quantitative. **The inertia the wing contributes is the denominator of every control-power figure the aircraft produced.** An aircraft with the same nozzles and heavier wings would have measured lower control powers for the same hardware. The criterion the X-14A produced is expressed in radians per second squared precisely to remove this dependence, and the removal is exact only to the extent that pilot opinion depends on angular acceleration alone.

### The Ground, Which the Aircraft Had to Stand On

This article treats ground effects only where they bear on control, and one point belongs here because it constrained where the experiments could be run.

A jet-lift aircraft hovering close to a surface directs its entire exhaust at that surface. The downwash impingement problem was studied contemporaneously and at length, in [White et al 1960][research_white_1960], [Morse and Newhouse 1960][research_morse_newhouse_1960], and [Morse and Newhouse 1961][research_morse_newhouse_1961], the last extending to duct adapter testing, and it had hardened into stated design criteria by [George et al 1964][research_george_1964]. The efflux itself is reviewed in [Garner 1967][research_garner_1967] and [Skifstad 1970][research_skifstad_1970], and the outflows of competing configurations are compared in [Michaelsen 1971][research_michaelsen_1971], which finds the jet-lift case the most severe of the three. The underlying fluid mechanics were pursued in parallel, in [Donaldson et al 1966][research_donaldson_1966] on the structure of an impinging free jet, [Strand 1967][research_strand_1967] on the inviscid theory of a round jet striking the ground, [Binion 1970][research_binion_w_1970] on the recirculation region a jet in ground effect creates with crossflow, and [Lissaman 1967][research_lissaman_1967] on the related jet-flap case. Ground-effect machines supplied a neighbouring body of measurements in [Foltz 1962][research_foltz_1962] and [Walker et al 1965][research_walker_1965], and the ingestion hazard was characterised as a dust problem as early as [Hafer and Skinner 1960][research_hafer_skinner_1960]. Estimating the loss from a single jet remained a live problem into [Christiansen et al 1985][research_christiansen_1985].

The aircraft also loses lift to its own jet before it ever reaches the ground. [Mc Lemore 1966][research_mc_lemore_1966] measures jet-induced lift loss in the hovering condition and [Margason 1966][research_margason_1966] the induced effects in transition, with the theoretical treatment in [Levinsky et al 1968][research_levinsky_1968]. The operational consequences run from prepared surfaces in [Butler and Thomas 1964][research_butler_thomas_1964] through spray in [Kuhn 1979][research_kuhn_1979] and deck temperatures in [Fluk 1981][research_fluk_1981] to shipboard operation in [Kamman and Hall 1978][research_kamman_hall_1978], with the flow field itself modelled in [Kotansky 1982][research_kotansky_1982] and still being visualised in [Mourtos et al 1995][research_mourtos_1995]. Hot gas returning to the inlet is the related hazard, treated in [Johns et al 1989][research_johns_1989] and [Johns et al 1990][research_johns_1990].

**The consequence for the X-14 programme is that out-of-ground-effect experiments and in-ground-effect experiments are different experiments**, and [Drinkwater et al 1965][research_drinkwater_1965] is explicit that its hovering evaluations were conducted out of ground effect. That is the correct choice for isolating the control variable, and it means the criterion was established in the condition least like a landing.

### Instrumentation, Which Was a Rating Scale

The measuring instrument in this aircraft was not a transducer. It was a numbered scale of pilot opinion, and the aircraft's output was an integer.

[Drinkwater et al 1965][research_drinkwater_1965] reproduces the rating schedule it used, running from excellent through satisfactory with mildly unpleasant characteristics, then to acceptable but with unpleasant characteristics, then to unacceptable for normal operation and acceptable only for emergency conditions. This is the Cooper scale in the form current before the revision that produced the [Cooper-Harper scale][ref_cooper_harper].

Two properties of this instrument shape everything the programme could conclude.

**It is ordinal rather than interval.** The distance between ratings three and four is not known to equal the distance between four and five, so averaging ratings is not obviously meaningful, and fitting a curve through them to find where it crosses a boundary imports an assumption the scale does not support. The scale's own authors returned to this two decades later in [Harper and Cooper 1984][research_harper_cooper_1984], and the methodological difficulties of evaluation at hover specifically are the subject of [Harper and Sardanowsky 1969][research_harper_sardanowsky_1969].

**Its dependence on how the evaluation is run was known and measured.** [Kidd and Bull 1963][research_kidd_bull_1963] examines how handling-qualities requirements are influenced by pilot evaluation time and sample size, which is precisely the objection this article raises below about two pilots, published two years before the lateral control experiments. The ambition to predict the rating rather than collect it runs from [Adams and Hatch 1970][research_adams_hatch_1970] and [Adams 1972][research_adams_1972] through [Levison 1982][research_levison_1982] to [Hess 1981][research_hess_1981] and [Hess 1984][research_hess_1984], the last proposing a unifying theory. **None of them removed the pilot from the procedure.**

**Its resolution is set by the sampling, not by the scale.** The X-14A tested three control powers, 0.8, 1.4, and 2.0 radians per second squared, spaced 0.6 apart. A threshold lying between two of them is located only to within that spacing. If the satisfactory boundary sits near 1.4, the experiment locates it to within 42.9 percent of its own value. If it sits near 2.0, to within 30.0 percent.

$$\frac{0.6}{1.4} = 0.429, \qquad \frac{0.6}{2.0} = 0.300$$

**This is the article's least comfortable number and it is not a criticism of the programme.** Three points was what an aircraft with a finite authority budget and a finite flight-test programme could deliver, and three points across a factor of two and a half in the variable is a respectable experiment. But a criterion later written into a specification to two significant figures rests, at its origin, on a grid whose spacing was thirty to forty percent of the answer.

### The Other Way of Measuring the Same Pilot

The rating scale treats the pilot as an oracle who returns a number. A parallel literature, running through exactly the same years and the same institutions, treats the pilot as a dynamic system to be identified.

[Elkind and Forgie 1959][research_elkind_forgie_1959] characterises the human operator in simple manual control systems, and the subject was developed continuously through a long conference series, of which [NACA 1966, Second Annual NASA-University Conf][research_naca_1966_2], [NACA 1967][research_naca_1967], [NACA 1969][research_naca_1969], [NACA 1970][research_naca_1970], and [NACA 1972][research_naca_1972] are successive proceedings. [Mitchell 1964][research_mitchell_1964] surveys the operator models available, [Young et al 1964][research_young_1964] treats the operator's adaptive response, and [Costello 1968][research_costello_1968] proposes a specific model form.

**The most directly relevant of these is [Smith 1966][research_smith_1966], which measured human describing functions in flight and on simulators**, because that is the comparison the X-14A's whole justification rested on. [Mooij 1973][research_mooij_1973] measured the pitch-axis describing function and remnant in flight.

**The hovering case was singled out for this treatment**, which matters because the loop structure derived above says hovering should be the hardest case for an adaptive operator. [Vinje 1968][research_vinje_1968] analyses pilot adaptation in a simulated multiloop vertical take-off hovering task, and [Andrisani 1982][research_andrisani_1982] determines pilot models experimentally from hovering flight data rather than from a simulator. The identification methods themselves developed through [Washizu et al 1978][research_washizu_1978] on the effect of forcing-function characteristics, [Tomizuka and Whitney 1976][research_tomizuka_whitney_1976] on preview tracking, [Dey 1972][research_dey_1972] on prediction displays, and [Biezad and Schmidt 1984][research_biezad_schmidt_1984] on time-series modelling, with the field's proceedings continuing through [NACA 1975][research_naca_1975], [NACA 1977][research_naca_1977], and [NACA 1981][research_naca_1981].

The two literatures met in [Hess 1977][research_hess_1977], which predicts pilot opinion ratings using an optimal pilot model. **If that programme had fully succeeded, the variable-stability aircraft would have become unnecessary**, because a rating could be computed from the dynamics rather than obtained from a person. It did not fully succeed, and the reason it did not is the reason a Cooper-Harper rating is still collected by asking someone.

There is a tension here the X-14's programme never resolved and mostly did not need to. A rating is a scalar summary of a closed-loop interaction whose dynamics the same field was busy measuring in detail. **The criterion the X-14A produced is expressed in terms of the plant alone**, which is only defensible if the pilot's contribution is approximately constant across the configurations compared, and the adaptive-operator literature was simultaneously establishing that it is not.

## The Flight Test Record

The X-14's flight record divides into a short period in which it was an aeroplane and a long period in which it was an instrument, and the two have almost nothing to do with each other.

### The Aeroplane, 1957 and 1958

The aircraft first hovered in February 1957. **Sources give either the seventeenth or the nineteenth**, and this article does not choose between them. Whichever it was, the first hover was made on the Viper engines, at a thrust-to-weight ratio that the arithmetic above shows to have been marginal at any realistic weight.

A partial transition followed, and the first full transition from vertical to horizontal flight was made on 24 May 1958. That completed the demonstration the Air Force contract had asked for. **The X-14 had shown that a jet-lift aircraft with vectored thrust and reaction controls could take off vertically, fly, and land vertically**, which the [X-13][related_post_a310_ryan_x13] had also shown by a different means the previous year.

At that point the aircraft had discharged its stated purpose and there was no obvious reason to keep flying it.

### The Instrument, 1959 to 1981

The aircraft was assigned to NASA Ames on 2 October 1959 and re-engined with the J85-GE-5, becoming the X-14A. The variable-stability system followed. From that point the flight record is a record of experiments.

The two that matter most to this article are the ones already drawn on. [Drinkwater and Rolls 1962][research_drinkwater_rolls_1962] used the variable-stability and control X-14A to determine attitude control power and damping requirements for a visual hovering task, and is the origin of the criteria. [Drinkwater et al 1965][research_drinkwater_1965] extended the work by separating control power from control sensitivity, testing three total control powers at three stick travels, and reported a result that is easy to state and was not obvious in advance.

**Total control power dominated. Control sensitivity barely mattered.** Changing the control power per inch of stick travel had only a minor effect across the range investigated, while changing the maximum moment available had a predominant effect on the pilots' ratings during visual hovering out of ground effect. This matters because sensitivity is nearly free and control power is expensive. The experiment found that the expensive parameter was the one that counted.

[Rolls 1965][research_rolls_1965] reports the operational experience of five and a half years of flight research with the aircraft, grouping the problems into effects of the jet engine and its operation, and restrictions imposed on the pilot by reduced visual reference. **Those two categories are the ones the wider field also found**, and the operational literature that grew around them covers terminal-area operation in [Schade 1968][research_schade_1968], shipboard compatibility in [Daffer and Rogers 1973][research_daffer_rogers_1973] and guidance to a small ship in [Goka et al 1980][research_goka_1980], noise in [Cole and England 1967][research_cole_england_1967], the sensing problem a vehicle with no reliable airspeed has in [McElreath 1972][research_mcelreath_1972] and [Wachtell 1970][research_wachtell_1970], and the consequences of losing the pilot in [Harvey and Waugh 1976][research_harvey_waugh_1976]. Whether the configuration was worth its costs at all was assessed commercially in [Fry 1967][research_fry_1967], and against competing layouts in [Englar and Kirkpatrick 1969][research_englar_kirkpatrick_1969] and [Detore and Gaffey 1969][research_detore_gaffey_1969]. Low-speed control improvement generally is [Kesselyak 1974][research_kesselyak_1974], and visual acquisition under a hovering aircraft's own disturbance is [Hilgendorf et al 1975][research_hilgendorf_1975]. **Neither category is about control power**, which is a useful corrective. The thing the aircraft was measuring was not the thing that made it difficult to operate.

[Gerdes and Rolls 1969][research_gerdes_rolls_1969] reports the tip-turbine fan experiment. The fans worked thermodynamically and failed dynamically, and the failure is instructive enough to be taken up separately below.

The experiments were not confined to control power. [Gerdes 1964][research_gerdes_1964] investigated height-control requirements, which is the vertical axis of the same problem and has a different character because thrust responds through engine dynamics rather than through a nozzle valve. The aircraft's inability to change its own thrust quickly is a limitation the criterion for attitude does not address at all.

In 1970 or 1971 the aircraft was re-engined again with J85-GE-19 engines and fitted with a programmable digital computer and a fly-by-wire control system, becoming the X-14B. [Gallagher et al 1972][research_gallagher_1972] describes the model-following variable-stability system. The digital system did what the analogue system had done, but it could be reprogrammed between flights rather than rewired, which changed the economics of running an experiment. [Corliss et al 1977][research_corliss_1977] reports an in-flight simulation of hover control concepts, and [Merrick 1982][research_merrick_1982] a translational velocity command system, both of which are experiments the analogue aircraft could not have hosted.

Over the whole period around twenty-five test pilots flew the aircraft. In 1965 Neil Armstrong flew it to evaluate control characteristics in vertical flight representative of the Apollo lunar module during final descent.

### The Ending

The X-14B was damaged beyond repair on 29 May 1981 in a hard landing. The pilot was not seriously injured. Secondary accounts attribute the accident to a design flaw in the lateral control software that led to a pilot-induced oscillation, and this article reports that attribution without having been able to confirm it against a primary investigation report.

**If the attribution is correct, the ending is exact.** An aircraft whose entire purpose was to make itself deliberately deficient in the lateral axis so that pilots could report on the consequences was destroyed by an unintended deficiency in the lateral axis that a pilot could not fly out of. The instrument was consumed by the phenomenon it existed to measure. It had been flying for twenty-four years and it was not repaired.

## Comparison With Ground Prediction

The X-14A's results can be set against three kinds of prediction, and the comparison is unusually informative because in this case the ground-based method eventually replaced the aircraft rather than merely preceding it.

### Against Ground Simulators

Ames ran motion-base simulators on the same questions throughout the period. [Gerdes 1964][research_gerdes_1964] investigated height-control requirements on a piloted motion simulator, and [Garren et al 1965][research_garren_1965] conducted a visual flight investigation of hovering and low-speed control requirements. [Greif et al 1972][research_greif_1972] used a motion simulator to study the effect of stabilisation on control power requirements, comparing no stabilisation, rate stabilisation, and attitude stabilisation. The same approach was applied to other configurations in [Breul 1963][research_breul_1963] for tilt-wing handling qualities and in [McCormick 1969][research_mccormick_1969] through moving-base simulation, with the equations of motion that such simulations required set out in [McIntyre 1963][research_mcintyre_1963] and the attitude representation problem in [Greenwood 1960][research_greenwood_1960].

**The most useful evidence of agreement is that the 1972 simulator study swept the same range the 1965 aircraft had.** It reports results across control powers from 0.8 to 2.0 radians per second squared and states its disturbance correlation as valid at least within that range. A decade after the flight experiment, the simulator work was still anchored to the interval the aircraft had established. That is either strong corroboration or strong path dependence, and the two are not easy to separate from outside.

The 1972 study also reports a finding the aircraft could not have produced. **An attitude-stabilised system gives the best handling qualities for the least control power**, which is a statement about a trade between two things the X-14A could vary but could not vary cheaply enough to map densely. A simulator can run hundreds of configurations in a week. The aircraft ran twenty-seven at most, and could not reach all of those.

Whether the two agree in general is a question the field kept returning to and never closed. [Innis and Anderson 1972][research_innis_anderson_1972] compares simulator and flight results directly for an augmentor-wing research aircraft, [Condit et al 1966][research_condit_1966] does the same for large transports in landing approach, [Mitchell and Hart 1993][research_mitchell_hart_1993] examines how simulator motion and visual characteristics change rotorcraft handling-qualities evaluations, and [Brandon et al 1995][research_brandon_1995] compares ground and flight assessments for a high-performance aeroplane. **That the comparison was still being made in 1995 is the answer to whether the X-14A's premise had been superseded.**

### Against the Scaling Argument

The scaling relation derived above, that control power at fixed bleed fraction falls inversely with span, is a prediction this article makes from the X-14A's own numbers. It can be checked against the contemporary literature rather than against a wind tunnel.

[Johnston and Friend 1965][research_johnston_friend_1965] addresses the effect of size on hover and low-speed handling qualities directly. **The existence of that paper, in that year, is the corroboration.** The field asked the size question within three years of the X-14A's first control-power results, which is what one would expect if the practitioners had noticed the same inverse dependence the algebra gives.

The check that can be made numerically is the Dornier Do 31, which spanned about eighteen metres and is the largest jet-lift vertical take-off aircraft flown. The relation demands 12.9 percent bleed at that span for the X-14A's maximum control power. That is a substantial fraction of installed thrust and it is consistent with the type having been at the edge of practicality. **The prediction is not falsified by the one large data point available**, which is weaker than confirmation and is what the evidence supports.

### Against the Model That Replaced the Aircraft

The most consequential comparison is with what came after. [Smith 1966, Vtol control power requirements re][research_smith_1966_2] reappraises control power requirements only four years after the original determination, which indicates the numbers were contested almost immediately.

The eventual resolution was not a better number. It was a change of variable, taken up below.

## What the Data Changed

This section usually asks whether an aircraft's data mattered. In the X-14's case the answer is unusually definite, and it is definite because the data became a specification.

### It Became a Requirement Document

Military Specification MIL-F-83300, Flying Qualities of Piloted V/STOL Aircraft, was adopted in December 1970. It is the document that turned handling-qualities research on vertical take-off aircraft into a contractual obligation on manufacturers, and its hovering requirements descend from the flight and simulator work of the preceding decade, of which the X-14A's is the principal flight component.

**The generation of the specification has its own account.** [Key 1971][research_key_1971] describes how MIL-F-83300 was produced, published the year after adoption, and it is the primary source for the lineage this section claims. The conventional-aircraft counterpart is documented the same way in [Chalk et al 1969][research_chalk_1969], the background and user guide for MIL-F-8785B. The specification then attracted the work any specification attracts: [Vinje and Miller 1973][research_vinje_miller_1973] reports flight simulator experiments in support of its further development, [Hutchings 1977][research_hutchings_1977] reviews the Navy requirements against it, [Anderson 1979][research_anderson_1979] compares an actual aircraft's handling qualities against both it and the corresponding AGARD report, and [Goldstein 1982][research_goldstein_1982] gives an overview of where the specifications stood a decade on. The short take-off case followed in [Hoh and Mitchell 1983][research_hoh_mitchell_1983]. **A research aircraft whose output can be traced into a numbered document that contractors must satisfy has had an unusual kind of effect**, and among the fifteen aircraft this series has covered only this one has it.

**This is rare among X-planes.** The [X-1][related_post_a298_bell_x1] changed what engineers believed about transonic drag. The [X-5][related_post_a302_bell_x5] changed what they believed about variable sweep. Belief is the usual output. A number in a military specification that a contractor must demonstrate compliance with is a different kind of output, and among the fifteen aircraft this series has covered, only the X-14 produced one directly.

### It Set the Range Everyone Else Worked In

The interval from 0.8 to 2.0 radians per second squared appears in the X-14A flight reports of 1962 and 1965, in the Ames simulator work of 1972, and in the discussion of control power requirements throughout the period. **A research aircraft that fixes the axis limits of everyone else's plots has had an effect that is easy to miss because it does not look like a result.**

### It Fed the Lunar Programme, Partially

Armstrong's 1965 flights connect the X-14A to Apollo, and the connection is real but narrower than the popular account suggests. [Hewes 1967][research_hewes_1967] reports flight evaluations of lunar landing vehicle attitude control systems, and [Mccabe et al 1967][research_mccabe_1967] reports piloted lunar module landing simulation studies. The X-14A could contribute to the attitude problem. **It could not contribute to the whole problem, for a reason that is exactly quantifiable and is taken up in the next section.**

### It Established the Method More Firmly Than the Number

The number the X-14A produced was reappraised within four years by [Smith 1966, Vtol control power requirements re][research_smith_1966_2] and superseded within twenty by the shift to bandwidth criteria. The method outlived both.

**Every serious handling-qualities question since has been settled the same way**, by building a vehicle or a simulator whose dynamics are adjustable, sweeping the parameter of interest across a boundary, and asking a trained pilot for an ordinal judgement. [Aiken et al 1977][research_aiken_1977] on the X-22A, [Hindson 1982][research_hindson_1982] on research helicopters, and [Corliss et al 1977][research_corliss_1977] on the X-14B itself are all the same experiment with different plants.

That is a stronger legacy than a number, and it is the one the X-14 has the best claim to, because it was first to apply the method to a hovering vehicle.

### It Did Not Save Jet Lift

The X-14's data made jet-lift vertical take-off aircraft designable. It did not make them worth designing. The scaling relation above is the reason, and it was not something better criteria could fix. **Knowing precisely how much control power a hovering aircraft needs does not make that control power cheaper**, and the whole history of the configuration after 1970 is the history of an idea that worked and did not pay.

## The Contemporary Literature

The X-14's question is live, and it is live in a field that does not usually cite it. Everything below is recent scholarship rather than recent history, and the connection to a 1962 flight report is in the structure of the problem rather than in the citations.

### The Question Is Being Asked Again in Almost the Original Form

The clearest case is [Antonakis 2025][research_antonakis_2025], which sizes handling qualities for aerial vehicles using control moment polytopes. **This is the X-14's question with the geometry made explicit.** A polytope of achievable control moments is the modern statement of the authority budget the X-14A ran into when its high-damping and high-control-power corner proved unreachable, and the sizing problem is the same one Bell faced in 1955 with a different set of effectors.

[Favaro et al 2025][research_favaro_2025] addresses building credible vertical take-off flight models for handling-quality certification by simulation. **This closes a loop the X-14 opened.** The X-14A existed because ground simulation was not trusted for hovering handling qualities. Sixty years later the question is what would make simulation credible enough to certify against, which is the same question with the burden of proof reversed.

### The Vehicle Is Small Again and the Constraint Has Moved

The tail-sitter and the jet-lift aeroplane both returned as small electric vehicles. [Wang et al 2026, Modeling and hover control of a bi][research_wang_2026_4] treats hover control of a biplane quadrotor tail-sitter, and [Juhasz et al 2025][research_juhasz_2025] identifies the dynamics of a hovering quadrotor biplane tail-sitter with canted motors from flight data.

The scaling relation derived above explains why these vehicles are easy in a respect the X-14 was not. **Control power falls inversely with span, so a vehicle at one tenth the span has ten times the control power for the same fractional expenditure**, and a small multirotor is enormously overprovided with attitude authority by 1960s standards. The constraint that dominated the X-14's design has been dissolved by size rather than solved by cleverness. What binds a small electric vehicle instead is energy, which the previous article in this series treated at length for the [X-13][related_post_a310_ryan_x13].

### System Identification Replaced the Variable-Stability Aircraft, Partly

The X-14 was an instrument for imposing dynamics on an aircraft so that a pilot could rate them. A large modern literature does the inverse, extracting dynamics from an aircraft that already has them. [Grauer and Morelli 2023][research_grauer_morelli_2023] introduces a collection on advances in aircraft system identification from flight test data, [Simmons et al 2023, Flight-Test System Identification][research_simmons_2023_2] treats techniques for small low-cost fixed-wing aircraft, and [Perry et al 2023][research_perry_2023] identifies a subscale distributed-electric-propulsion aircraft.

**The relationship between the two techniques is not replacement but a division of labour.** Identification tells you what an aircraft does. It cannot tell you what a pilot would think of an aircraft that does something else, which is the question the X-14 was built to answer, and the only ways to answer it remain a simulator and a variable-stability aircraft.

### Identification Is Now Done on the Vehicle That Will Fly

The X-14's dynamics were imposed. A modern small vehicle's are measured, often from the vehicle itself in flight, and the tooling for that has become routine. [Juhasz et al 2025][research_juhasz_2025] identifies a hovering quadrotor biplane tail-sitter with canted motors, [Perry et al 2023][research_perry_2023] a subscale distributed-electric-propulsion aircraft, and [Simmons et al 2023, Flight-Test System Identification][research_simmons_2023_2] treats the techniques for small low-cost fixed-wing aircraft generally, with the state of the field reviewed in [Grauer and Morelli 2023][research_grauer_morelli_2023].

**The economic change is the one worth naming.** The X-14 cost an airframe, two engines, a control system, and twenty-four years of a flight-test organisation. A modern subscale vehicle that answers a narrower version of the same question costs a few thousand dollars and can be replaced when it crashes, which changes not only the price of an experiment but the acceptable probability of losing one.

### The Pilot Is Still in the Loop and the Loop Now Has a Computer in It

The X-14's hovering pilot closed a position loop through an attitude loop with no aerodynamic help. The modern version of that arrangement puts an autonomous system in the same loop, and the question becomes how authority is divided. [Xu et al 2025, Modeling Shared Control System Bet][research_xu_2025_3] models shared control between a human pilot and an autopilot for a carrier landing task, which is structurally the X-14's problem with a second controller added.

[Wang and Chen 2024][research_wang_chen_2024] assesses handling qualities for a helicopter with slung loads under various sling configurations, which is a case where the plant changes underneath a fixed criterion, and is the kind of problem a criterion stated as a single threshold in angular acceleration handles badly.

The most direct modern descendant of the X-14A's question is [Bahr et al 2022][research_bahr_2022], on the handling qualities of fixed-pitch variable-speed multicopters for urban air mobility. **A fixed-pitch multicopter changes its attitude moment by changing rotor speed**, which is the tip-turbine fan's failure mode reintroduced as the primary control mechanism, because a rotor with inertia cannot change speed instantly. That the configuration works anyway is a consequence of how small the vehicles are, which the scaling relation above explains, and of electric motors having far better torque response than a bleed-driven turbine.

The X-14A's 1969 finding therefore survives in an unexpected form. **Rotational inertia in the control effector is still the thing that decides whether a hovering aircraft is flyable**, and the modern answer is not to avoid it but to make the rotors small enough and the motors strong enough that the time constant falls below the pilot's, or the autopilot's, bandwidth.

### Certification Replaced Specification, and the Burden Moved

MIL-F-83300 obliged a military contractor to demonstrate compliance. The vehicles now being built to hover are civil, and the framework they must satisfy is a certification basis rather than a procurement specification. [Favaro et al 2025][research_favaro_2025] is written from inside that problem, and its subject is what makes a flight model credible enough to certify against by simulation rather than by flight.

**This is a reversal worth naming.** The X-14A existed because nobody trusted a simulator to answer a handling-qualities question about hovering. The modern question is what evidence would justify trusting one, because flying every configuration is no longer affordable and the number of configurations has grown enormously. The variable-stability aircraft solved the credibility problem by removing the simulation. The current approach is to solve it by validating the simulation, and the criterion for adequate validation is itself unsettled.

### The Authority Budget Became a Geometry Problem

The X-14A ran into its authority limit as a truncated corner of an experimental grid, described in its own report as the region beyond the ability of the aircraft. The modern statement of the same limit is explicit and geometric.

[Antonakis 2025][research_antonakis_2025] sizes handling qualities using control moment polytopes, which represent the set of moments a given effector arrangement can produce as a convex region in three-dimensional moment space. **The X-14A's problem is the statement that the polytope did not contain the required corner.** Casting it this way makes the multi-axis case tractable, which the scalar control-power criterion never was, because an aircraft demanding simultaneous roll and pitch authority is asking about a diagonal of the polytope rather than about either axis alone.

This is also where the X-14's three-axis arrangement shows its age. Its roll nozzles were at the wingtips and its pitch and yaw nozzles at the tail, so the axes drew on a shared bleed supply but acted through separate hardware. A modern multirotor produces all three axis moments from the same set of rotors, so the axes compete directly, and the polytope is the only honest way to state what is available.

### What Has Not Changed

Three of this article's findings have no modern remedy.

**Attitude control still costs lift on any vehicle that produces both from the same source.** An electric multirotor produces attitude moments by differential rotor thrust, which is thrust not being used to hold the vehicle up, and the accounting is the same as the X-14's even though the hardware is not.

**The threshold is still a property of the person.** No amount of modelling has removed the need to ask a human being whether an aircraft is acceptable, which is why the Cooper-Harper scale is still in use sixty years after the scale the X-14A used.

**And gravity is still not adjustable.** Every argument in this article about what the X-14 could not simulate applies unchanged to any Earth-based simulator for any other body, which is why lunar landing training vehicles remain a live engineering subject rather than a historical one.

## Where the Framing Breaks Down

Treating the X-14 through the keystone of control-power measurement is the right frame, and there are five places where it misleads.

### The Criterion Specified Magnitude and the Problem Was Bandwidth

This is the most important limitation and the aircraft's own programme demonstrated it.

The tip-turbine fans of [Gerdes and Rolls 1969][research_gerdes_rolls_1969] produced the required thrust for half the bleed, which by the criterion the aircraft itself had established should have been a straightforward improvement. **They were rejected because of their time constants.** A fan has rotational inertia and takes time to spin up, so the moment arrives late. The report is explicit that this resulted in pilot-induced oscillations and long lags between control initiation and the aircraft following.

So a control system meeting the control-power criterion exactly was unflyable. **The criterion was incomplete, and the experiment that revealed the incompleteness was run on the same aircraft that had produced the criterion.** What was missing was any statement about how quickly the moment must appear, which is a bandwidth requirement rather than an authority requirement.

The field's eventual answer was to change the variable. Modern handling-qualities criteria are stated in terms of attitude-response bandwidth and phase delay rather than in terms of maximum angular acceleration alone, and the experiments that established those criteria are a direct methodological descendant of the X-14A's. [Pausder and Blanken 1992][research_pausder_blanken_1992], [Pausder and Blanken 1993][research_pausder_blanken_1993], and [Blanken and Pausder 1994][research_blanken_pausder_1994] investigate the effects of bandwidth and time delay on roll-axis handling qualities, sweeping two parameters across a boundary and collecting pilot ratings, which is the X-14A's procedure with the independent variables replaced. The state of the subject at that point is collected in [Blanken and Whalley 1993][research_blanken_whalley_1993]. **The X-14's number survived as a floor and stopped being the criterion.**

The two framings can be connected, and connecting them shows why the older one was not simply wrong. Tracking an attitude oscillation of amplitude $A$ at frequency $\omega$ on a double integrator requires an angular acceleration of

$$\ddot{\theta} = A \omega^{2}$$

so saturation at the available control power caps the frequency at

$$\omega_{\text{max}} = \sqrt{\frac{\text{CP}}{A}}$$

**Authority and bandwidth are therefore the same statement at a specified amplitude and different statements otherwise.** At five degrees of amplitude the X-14A's lowest tested control power of 0.8 radians per second squared supports 3.03 radians per second and its highest supports 4.79.

$$\sqrt{\frac{0.8}{0.0873}} = 3.03, \qquad \sqrt{\frac{2.0}{0.0873}} = 4.79$$

Turning it the other way, a control power of 0.8 sustains a bandwidth of two radians per second up to an amplitude of 11.5 degrees, and 2.0 sustains it up to 28.6 degrees.

$$A_{\text{max}} = \frac{\text{CP}}{\omega^{2}} = \frac{0.8}{4} = 0.2 \text{ rad}$$

**So the magnitude criterion is a bandwidth criterion evaluated at large amplitude.** The X-14A's numbers are adequate for the large corrections and become uninformative for the small rapid ones, which is exactly the regime in which a laggy actuator ruins an aircraft while satisfying the magnitude requirement. The tip-turbine fans failed in the regime the criterion did not describe.

### Two Pilots

The lateral control results rest on the flight performance of two NASA research pilots, both experienced in helicopters and vertical take-off aircraft. That is the sample.

Nothing about this was unreasonable in 1965, and the alternative was no data at all. But a criterion that a contractor must design to, derived from two experienced test pilots' opinions, carries an assumption that the population of pilots who will fly production aircraft resembles those two. **Experienced test pilots are precisely the population least representative of the difficulty a task presents**, because they are selected for being able to fly things other people cannot.

### One Airframe's Inertias

Every control power the X-14A reported is a moment divided by the X-14A's inertia. The normalisation is intended to make the result transferable, and it does so exactly if pilot opinion depends on angular acceleration and nothing else.

It does not, quite. The pilot sees the aircraft's attitude and also its position, and the mapping from attitude to position depends on the aircraft's height above the ground, its visual surroundings, and the pilot's viewing position. **The X-14 had an open cockpit and the pilot sat forward of the wing**, which is an unusually good viewing position, and [Rolls 1965][research_rolls_1965] identifies reduced visual reference as one of the two principal operational problem categories. A criterion measured in one visual environment and applied in another is being extrapolated on a variable nobody recorded.

### Gravity Was Not Adjustable

The variable-stability system could synthesise any attitude dynamics within its authority budget. It could not synthesise gravity, and this bounds what the aircraft could simulate in a way that is exactly computable.

The attitude dynamics contain no gravitational term,

$$\ddot{\theta} = \frac{M}{I}$$

so the X-14A could reproduce a lunar module's attitude response exactly. The translational dynamics do contain one. A hovering vehicle holding height and tilted by $\theta$ accelerates horizontally at

$$\ddot{x} = g \tan\theta$$

so the same attitude produces different translation under different gravity. The ratio of terrestrial to lunar gravity is

$$\frac{g_{e}}{g_{m}} = \frac{9.807}{1.62} = 6.05$$

and since a distance covered under constant acceleration goes as the square of time, the lunar translation timescale is longer by

$$\sqrt{\frac{g_{e}}{g_{m}}} = 2.46$$

**The X-14A therefore simulated the inner loop exactly and the outer loop 2.46 times too fast.** Concretely, holding five degrees of tilt for five seconds moves an aircraft 10.7 metres on Earth and 1.8 metres on the Moon.

$$\tfrac{1}{2} \times 9.807 \times 0.0873 \times 25 = 10.7 \text{ m}$$

The same input on the Moon produces a translation the pilot would have to work to notice.

$$\tfrac{1}{2} \times 1.62 \times 0.0873 \times 25 = 1.8 \text{ m}$$

Two further consequences follow and both are quantitative. A vehicle hovering on the Moon needs

$$\frac{T_{\text{moon}}}{T_{\text{earth}}} = \frac{g_{m}}{g_{e}} = 0.165$$

of the thrust it would need on Earth, so the thrust margin is not the binding constraint there that it is here. And to obtain the same horizontal acceleration the lunar vehicle must tilt very much further, since

$$g_{m} \tan\theta_{m} = g_{e} \tan\theta_{e} \quad \Longrightarrow \quad \tan\theta_{m} = 6.05 \tan\theta_{e}$$

so that five degrees on Earth corresponds to

$$\theta_{m} = \arctan\left(6.05 \times \tan 5^{\circ}\right) = 27.9^{\circ}$$

**A lunar lander manoeuvres at attitudes that would be alarming in a terrestrial hover**, and no amount of adjustment to a terrestrial aircraft's control system reproduces that, because the aircraft would simply translate away.

This is not a small mismatch and it is not correctable by any adjustment of the control system, because it is a mismatch in the plant rather than in the controller. **It is the reason the [Lunar Landing Research Vehicle][ref_llrv] had to exist.**

The lineage is documented and it reads as a sequence of admissions that the previous simulator was insufficient. [Henderson 1963][research_henderson_1963] compares control systems for the final descent and landing manoeuvre, and [Markson et al 1963][research_markson_1963] reports simulation of the manned lunar landing. [Obryan 1966][research_obryan_1966] reports flight tests of a manned rocket-powered vehicle using the Langley lunar landing facility, which suspended the vehicle to cancel most of its weight. [Greene and Russo 1967][research_greene_russo_1967] and [Mccabe et al 1967][research_mccabe_1967] report piloted lunar module landing simulation studies, and [Hewes 1967][research_hewes_1967] reports flight evaluations of lunar landing vehicle attitude control systems.

**The document that states the problem most directly is [Kluever 1967][research_kluever_1967]**, which assesses ground and flight simulators for examining the manned lunar landing, because that is precisely the question of what each kind of simulator can and cannot represent. The training programme that resulted is described in [Armstrong and Nassiff 1968][research_armstrong_nassiff_1968] and the vehicle itself in [Bigham 1970][research_bigham_1970]. **[Jarvis 1967][research_jarvis_1967] is the most directly comparable document**, reporting fly-by-wire flight control experience with a free-flight lunar-landing research vehicle, which is the same class of report as the X-14B papers for a machine built because the X-14 could not do the job. The landing simulations themselves are [Pollack et al 1967][research_pollack_1967] and [Mccabe et al 1967, Results and analysis of piloted lu][research_mccabe_1967_2], the automatic alternative to a piloted landing is [Rimer and Sperling 1965][research_rimer_sperling_1965], and the surface interaction that made the final phase hazardous is [Roberts 1964][research_roberts_1964]. That vehicle cancelled most of its weight with a gimballed vertical jet so that the residual translational dynamics were lunar. The fraction it had to support is

$$1 - \frac{g_{m}}{g_{e}} = 1 - 0.165 = 0.835$$

**so the jet carried 83.5 percent of the vehicle and the remaining 16.5 percent was flown**, which is a far more expensive and dangerous way to build a simulator, and it was built because the cheaper way could not do the job.

The X-14's contribution to Apollo was therefore real and bounded. It could teach the attitude task. It could not teach the landing.

### Diminishing Returns, Which the Criterion Does Not Show

A last point that the framing obscures. The criterion is a threshold, which suggests that more control power is better until the threshold is met and irrelevant afterwards. The dynamics say something more graded.

Consider correcting a position error of three metres. The pilot tilts, waits, and tilts back. Establishing an attitude $\theta$ by a symmetric accelerate-and-arrest input at angular acceleration CP takes $2\sqrt{\theta/\text{CP}}$, and the tilt must be put in and taken out twice. Covering the distance at that tilt takes $2\sqrt{d/(g\tan\theta)}$. So the total is approximately

$$t(\theta) = 4\sqrt{\frac{\theta}{\text{CP}}} + 2\sqrt{\frac{d}{g \tan\theta}}$$

which has an interior minimum, because a larger tilt translates faster but takes longer to establish. In the small-angle form the stationarity condition is

$$\frac{dt}{d\theta} = \frac{2}{\sqrt{\text{CP}\,\theta}} - \sqrt{\frac{d}{g}}\;\theta^{-3/2} = 0$$

which solves to

$$\theta^{*} = \tfrac{1}{2}\sqrt{\frac{\text{CP}\, d}{g}}$$

and substituting that back has a pleasant consequence. The attitude term and the translation term become equal,

$$4\sqrt{\frac{\theta^{*}}{\text{CP}}} = 2\sqrt{\frac{d}{g\,\theta^{*}}}$$

**An optimally flown hover correction spends exactly half its time changing attitude and half translating**, whatever the control power and whatever the distance. The numerical optimum with the exact tangent runs a little above the small-angle value, at 24.6 degrees against 22.4 for a three metre correction at the maximum control power, and the split is 1.85 seconds against 1.63.

Minimising over $\theta$ for a three metre correction gives 4.42 seconds at a control power of 0.8 and 3.49 seconds at 2.0.

**Two and a half times the control power buys 21.2 percent less time.** The local exponent is

$$\frac{d \ln t}{d \ln \text{CP}} = -0.26$$

which is close to a quarter-power law. **Control power has sharply diminishing returns**, and this is a structural reason why the pilot ratings improved so much less than proportionally across the tested range, and why a threshold criterion is the right shape of answer even though the underlying physics is continuous.

## What the X-14 Was Worth

The X-14 is the first aircraft in this series whose value cannot be stated as a capability.

It did not fly fast, high, or far. It demonstrated a transition that another aircraft in the same series had already demonstrated by a different method a year earlier. **Its entire contribution is a set of numbers, and the numbers are about people.**

The case for it is that the numbers were not otherwise obtainable and that they were needed. Between 1955 and 1970 every serious vertical take-off design in the West had to choose an attitude control system size, and before the X-14A the choice was informed by opinion and afterwards by measurement. The measurement was coarse, resting on three sampled control powers and two pilots, and it was incomplete, specifying magnitude where bandwidth also mattered. **It was still better than what it replaced, which was nothing.**

The second part of the case is the twenty-four years. An aircraft built for a 1955 question was still producing publishable results in 1982, on subjects its designers had no concept of, because what had been built was reprogrammable. **The X-14 is the strongest argument in this series for building research aircraft as instruments rather than as demonstrations**, and the argument is economic rather than aesthetic. A demonstration is worth what it demonstrates, once. An instrument is worth whatever anyone subsequently thinks to measure with it.

## The Designation, Which Is Unremarkable

There is nothing anomalous about the X-14 designation. It was assigned in sequence, to one aircraft, which was built and flown and kept the designation with suffix changes through two major reconfigurations.

One asymmetry in the record is worth setting down, because the contrast says something about how each programme was run. The tail-sitting alternative is far better documented in the scale-model literature. The [X-13][related_post_a310_ryan_x13] was preceded by free-flight model work in [Smith 1958][research_smith_1958] and derivative measurements in [Shanks and Smith 1959][research_shanks_smith_1959] and [Shanks and Smith 1960][research_shanks_smith_1960], and the earlier Convair tail-sitter by [Lovell et al 1953][research_lovell_1953] and the four-part derivative series beginning at [Queijo et al 1953][research_queijo_1953]. **The X-14's control-power question could not be attacked that way at all**, because the quantity being sought is a property of a pilot and a model has no pilot in it.

The point that does deserve comment is the pairing. The X-13 and the X-14 are consecutive designations covering two solutions to the same problem, a jet aircraft that takes off vertically. The [X-13][related_post_a310_ryan_x13] solved it by standing the whole aircraft on its tail and the X-14 by turning the exhaust while the aircraft stayed level. **The second approach is the one that survived**, in the Harrier and everything descended from it, and the designation sequence records the comparison without comment. The subsequent literature is about how to fly the surviving configuration rather than whether to build it, running through [Huntley 1972][research_huntley_1972] on minimising landing transition distance, [Karemaa 1971][research_karemaa_1971] on hybrid jet-lift take-off and landing, [Nishimura 1980][research_nishimura_1980] on the fuel-minimal take-off path, and [Morello et al 1972][research_morello_1972] on a flight evaluation of a vectored-thrust aeroplane during simulated instrument approaches. The inlet problem the configuration creates for itself is [Grahame 1968][research_grahame_1968] and [Grahame 1969][research_grahame_1969], the configuration management the transition demands is [Johnson and Craig 1974][research_johnson_craig_1974], and the whole development is reviewed from a distance in [Anderson 1983][research_anderson_1983].

The criteria the X-14A produced were applied well beyond the aircraft that produced them. The lift-fan branch runs through [Przedpelski 1965][research_przedpelski_1965], [Hill and Waters 1974][research_hill_waters_1974], [Bland et al 1976][research_bland_1976], and [Sellers et al 1977][research_sellers_1977], and reaches an integrated flight and propulsion treatment in [Chung et al 1995, Simulation model of the integrated][research_chung_1995_2]. The tail-sitting configuration returned to simulation in [Hill 1981][research_hill_1981] and [Hill 1983][research_hill_1983], which is the [X-13][related_post_a310_ryan_x13]'s layout being re-examined a quarter of a century later with the criteria this aircraft supplied. Rotorcraft response requirements were settled the same way in [Mitchell et al 1987, A flight investigation of helicopt][research_mitchell_1987_2] and [Mitchell et al 1989][research_mitchell_1989], with hovering dynamics and pilot performance in [Aponso et al 1987][research_aponso_1987] and control and display dynamics for hover in [Eshow 1990][research_eshow_1990]. Even vehicles with no wing at all inherited the framework, in [Putman et al 1977][research_putman_1977] and [Curtiss and Sumantran 1985][research_curtiss_sumantran_1985] on hovering airships, and the rotor case in [Curtiss 1973][research_curtiss_1973].

## The Source Base

The primary record for this article is unusually concentrated and has one significant hole.

The keystone document is [Drinkwater and Rolls 1962][research_drinkwater_rolls_1962], which is the NASA Ames determination of attitude control power and damping requirements using the variable-stability and control X-14A. **The full text of the underlying technical note was not retrievable.** The NASA Technical Reports Server holds the record with an abstract but no downloadable document, and the archive's search endpoint does not return it for any phrasing of its own title, which is a retrieval defect in the archive rather than in the query. The document was located through its citation in a later report.

This article therefore relies on the successor rather than the origin for its numbers. [Drinkwater et al 1965][research_drinkwater_1965] is available in full, states the control powers tested and the test weight and thrust-to-weight ratio directly, and is the source for every quantitative claim about the experimental programme made above. **The specific pilot ratings against control power were not recoverable** from the copy obtained, because the relevant figure did not survive text extraction, and no rating values are asserted anywhere in this article.

The other primary documents are complete and were read. [Gerdes and Rolls 1969][research_gerdes_rolls_1969] supplies the bleed figure that the whole sizing analysis rests on. [Rolls 1965][research_rolls_1965] supplies the operational experience. [Rolls 1965, Jet Vtol power plant experience du][research_rolls_1965_4] supplies the powerplant experience. [Gallagher et al 1972][research_gallagher_1972], [Corliss et al 1977][research_corliss_1977], and [Merrick 1982][research_merrick_1982] cover the digital era.

The vehicle specifications come from secondary compilations and **they disagree with each other** on the Viper engine rating and on the date of the first hover. Both disagreements are reported in the text rather than resolved. The 1981 accident cause is given by secondary sources and was not confirmed against a primary investigation report.

## Epistemic State

**Historical fact, from primary sources.** The X-14A weighed 3,700 pounds during the lateral control experiments with a thrust-to-weight ratio available of 1.1 to 1.2. Lateral control power was tested at 0.8, 1.4, and 2.0 radians per second squared, at three stick travels, with damping also varied, and total control power dominated pilot ratings while control sensitivity had only a minor effect. Attitude control in hover was by reaction jets at the wingtips and tail supplied with compressor bleed. The exhaust was turned by cascade diverters. Tip-turbine fans of 150 pounds thrust were flown, used about half the bleed of the reaction controls for the same thrust, returned four percent more engine thrust, and were rejected for their time constants.

**Historical fact, from secondary sources.** The July 1955 Air Force contract, the Bell Model 68 designation and 56-4022 serial, the Bonanza and T-34 component origins, the assignment to Ames on 2 October 1959, the J85-GE-5 and J85-GE-19 ratings, the first transition on 24 May 1958, the roughly twenty-five pilots, Armstrong's 1965 flights, and the 29 May 1981 loss.

**Contested in the sources and left contested.** The Viper 8 rating, given as either 1,750 or 1,560 pounds of thrust each. The first hover date, given as either 17 or 19 February 1957. The 1981 accident cause, attributed by secondary sources to a lateral control software flaw producing a pilot-induced oscillation, unconfirmed here.

**Engineering analysis, derived in this article and reproducible from the stated inputs.** The bleed fraction of 7.41 percent, inverted from the four percent thrust recovery on halving the bleed. The consequent 397 pounds of thrust and the finding that this consumed 34.9 to 51.8 percent of the hover margin. The installation loss of 17.2 to 24.1 percent. The Viper thrust-to-weight ratios of 0.843 and 0.946, both below unity at the 3,700 pound test weight. The roll inertia of 3,333 kilogramme metres squared and radius of gyration of 13.7 percent of span. The scaling relation that control power falls inversely with span at fixed bleed fraction, and the resulting span limit near 28 metres. The repositioning time analysis and its exponent of minus 0.26. The lunar timescale mismatch of 2.46.

**A correction to the previous article, derived here.** The [X-13][related_post_a310_ryan_x13] article described hovering as a third-order position loop. Composing the transfer functions shows the loop from control input to position is fourth order when the damping is zero, and third only below the damping break frequency. Both articles are describing the same physics and the earlier phrasing is the low-frequency case. The distinction matters because a fourth-order plant demands two derivatives of lead from the pilot rather than one, and this article treats that as the explanation for why attitude stabilisation buys so much.

**Inference, stated as such.** That the re-engining was a precondition for the research programme rather than a performance upgrade follows from the Viper thrust-to-weight ratios but is not stated in any source consulted. That the tip fans were specified at the aircraft's existing maximum control power rather than above it, and that this indicates bleed rather than authority was the binding constraint, is an inference from two numbers in two reports. That the X-14A's tested range set the range used by later simulator studies is an inference from the coincidence of intervals and could equally be independent convergence. That the field recognised the size-scaling problem within three years is inferred from the existence and title of a 1965 paper rather than from its content, which was not read in full.

**Claims the record does not settle.** Whether MIL-F-83300's hovering requirements derive specifically from the X-14A's numbers rather than from the broader flight and simulator corpus of the 1960s. The article claims descent from that corpus, of which the X-14A is the principal flight component, and does not claim a direct numerical inheritance. Whether the 1981 accident was as described. Whether the X-14 is the longest-serving X-plane, which its 1957 to 1981 span suggests but which this article has not verified against all seventy-two designations in the series and therefore does not assert.

**Anachronism, flagged.** The bandwidth and phase-delay framing used in the discussion of what the criterion missed postdates the X-14A's principal results by decades. It is applied here because the tip-fan failure of 1969 is unintelligible without it, and the aircraft's own programme produced the evidence that the magnitude criterion was incomplete before the vocabulary existed to say so.

## Out of Scope

The transition aerodynamics of jet-lift aircraft, including induced lift loss and the ground vortex, are treated only where they bear on control. Hot gas ingestion and ground erosion, which the sources identify as significant operational problems, are noted and not analysed. The Cooper-Harper scale's development and its statistical properties are a subject in their own right and are treated only far enough to state why an ordinal scale limits what the experiment concluded. The Lunar Landing Research Vehicle and Lunar Landing Training Vehicle are discussed only as the answer to a limitation of the X-14 and not on their own terms. The Hawker P.1127 and the Harrier line are the obvious descendants of vectored-thrust jet lift and are out of scope here. The detailed thermodynamics of compressor bleed extraction, including the stage from which air is taken and the effect on surge margin, is not treated.

## Conclusion

The X-14 answered the question of how much attitude control a hovering aircraft needs, and the answer was a number between 0.8 and 2.0 radians per second squared with the boundary somewhere inside that interval.

The more durable results are the ones around the number. **Attitude control on a jet-lift aircraft is bought with lift, at a price this article fixes at about seven and a half percent of thrust, which consumed between a third and a half of everything the X-14A could lift beyond its own weight.** That price scales badly, growing linearly with span at fixed control power, and the scaling is sufficient on its own to explain why jet-lift vertical take-off aircraft never grew beyond about eighteen metres of span in practice.

The aircraft also demonstrated the limits of its own criterion. **The tip-turbine fan experiment produced a control system that met the control-power requirement exactly and was unflyable**, which showed that magnitude without bandwidth is not a specification, and the field eventually changed the variable rather than the number.

And it could not simulate gravity. That single unadjustable parameter bounds what any Earth-based hovering simulator can teach about landing anywhere else, by a factor of 2.46 in the translational timescale, and it is why a far more dangerous vehicle had to be built to finish the job.

**What the X-14 is worth is not what it did but what was done with it.** It was built as an instrument, kept for twenty-four years, reprogrammed twice, and used for experiments nobody had conceived when it was ordered. Among the fifteen aircraft this series has examined, it is the only one whose principal output was a number that a contractor was later obliged to meet.

The next article takes up the [North American X-15][ref_x15], which is the opposite of this aircraft in every respect that matters.

## References

### Books

[book_jenkins_landis_miller_2003]: https://openlibrary.org/search?q=Jenkins+Landis+Miller+American+X+Vehicles
[book_miller_2001]: https://openlibrary.org/search?q=Miller+The+X+Planes+X-1+to+X-45
[book_rogers_1989]: https://openlibrary.org/search?q=Rogers+VTOL+Military+Research+Aircraft

### Reference

[ref_bonanza]: https://en.wikipedia.org/wiki/Beechcraft_Bonanza
[ref_cooper_harper]: https://en.wikipedia.org/wiki/Cooper%E2%80%93Harper_rating_scale
[ref_llrv]: https://en.wikipedia.org/wiki/Bell_Aerosystems_Lunar_Landing_Research_Vehicle
[ref_t34]: https://en.wikipedia.org/wiki/Beechcraft_T-34_Mentor
[ref_x14]: https://en.wikipedia.org/wiki/Bell_X-14
[ref_x15]: https://en.wikipedia.org/wiki/North_American_X-15

### Research

[research_adams_1972]: https://doi.org/10.2514/6.1972-962
[research_adams_hatch_1970]: https://doi.org/10.2514/6.1970-568
[research_aiken_1977]: https://ntrs.nasa.gov/citations/19780011162
[research_albachten_1956]: https://doi.org/10.21236/ad0116273
[research_anderson_1960]: https://ntrs.nasa.gov/citations/19980223619
[research_anderson_1979]: https://ntrs.nasa.gov/citations/19790019011
[research_anderson_1983]: https://ntrs.nasa.gov/citations/19830068366
[research_andrisani_1982]: https://doi.org/10.2514/6.1982-1294
[research_antonakis_2025]: https://doi.org/10.1016/j.ast.2025.110020
[research_aponso_1987]: https://ntrs.nasa.gov/citations/19870063261
[research_armstrong_nassiff_1968]: https://doi.org/10.2514/6.1968-254
[research_bahr_2022]: https://doi.org/10.1017/aer.2021.114
[research_barzda_1966]: https://doi.org/10.2514/6.1966-733
[research_baska_robbins_1966]: https://ntrs.nasa.gov/citations/19660023333
[research_baxter_finvold_1958]: https://doi.org/10.4271/580070
[research_behan_siciliani_1965]: https://doi.org/10.2514/6.1965-722
[research_besco_1964]: https://doi.org/10.2514/6.1964-1227
[research_biezad_schmidt_1984]: https://doi.org/10.2514/6.1984-1899
[research_bigham_1970]: https://doi.org/10.1177/003754977001500107
[research_binion_w_1970]: https://doi.org/10.21236/ad0711665
[research_bland_1976]: https://ntrs.nasa.gov/citations/19770007094
[research_blanken_pausder_1994]: https://ntrs.nasa.gov/citations/19950043496
[research_blanken_whalley_1993]: https://ntrs.nasa.gov/citations/19940008821
[research_bramwell_1956]: https://doi.org/10.1017/s0001924000126089
[research_brandon_1995]: https://ntrs.nasa.gov/citations/19970005147
[research_breul_1963]: https://doi.org/10.21236/ad0402774
[research_brown_1965]: https://doi.org/10.2514/6.1965-756
[research_butler_thomas_1964]: https://doi.org/10.21236/ad0613342
[research_campbell_1962]: https://ntrs.nasa.gov/citations/19630017020
[research_carpenter_jenny_1964]: https://doi.org/10.2514/6.1964-286
[research_chalk_1969]: https://doi.org/10.21236/ad0860856
[research_christiansen_1985]: https://ntrs.nasa.gov/citations/19860053601
[research_chung_1995_2]: https://ntrs.nasa.gov/citations/19950019992
[research_ciepluch_1979]: https://ntrs.nasa.gov/citations/19800001979
[research_clark_1964]: https://doi.org/10.2514/6.1964-618
[research_cole_england_1967]: https://doi.org/10.21236/ad0658448
[research_condit_1966]: https://ntrs.nasa.gov/citations/19660029515
[research_corliss_1977]: https://ntrs.nasa.gov/citations/19770052109
[research_costello_1968]: https://doi.org/10.1109/tmms.1968.300028
[research_creer_1959]: https://ntrs.nasa.gov/citations/19980228135
[research_curry_1965]: https://doi.org/10.21236/ad0617748
[research_curtiss_1973]: https://doi.org/10.2514/3.60228
[research_curtiss_sumantran_1985]: https://doi.org/10.2514/3.20051
[research_daffer_rogers_1973]: https://doi.org/10.21236/ad0764865
[research_dahl_1962]: https://doi.org/10.1016/b978-0-12-395586-9.50032-5
[research_davis_spicer_1965]: https://doi.org/10.2514/6.1965-1425
[research_deets_1978]: https://ntrs.nasa.gov/citations/19780015077
[research_denning_1962]: https://doi.org/10.4271/620308
[research_dent_1966]: https://doi.org/10.1016/0022-460x(66)90128-3
[research_detore_gaffey_1969]: https://doi.org/10.2514/6.1969-220
[research_dey_1972]: https://ntrs.nasa.gov/citations/19730001393
[research_div_1956]: https://doi.org/10.21236/ad0141370
[research_donaldson_1966]: https://doi.org/10.21236/ad0656592
[research_dorr_1992]: https://ntrs.nasa.gov/citations/19930029334
[research_dorr_1994]: https://ntrs.nasa.gov/citations/19950037642
[research_drinkwater_1965]: https://ntrs.nasa.gov/citations/19650009016
[research_drinkwater_rolls_1962]: https://ntrs.nasa.gov/citations/19620002530
[research_dukes_1970]: https://doi.org/10.21236/ad0871424
[research_elkind_forgie_1959]: https://doi.org/10.1109/tac.1959.6429402
[research_elliott_schreiber_1964]: https://doi.org/10.2514/6.1964-805
[research_eney_1967]: https://doi.org/10.2514/6.1967-576
[research_englar_kirkpatrick_1969]: https://doi.org/10.21236/ad0703669
[research_erwin_1964]: https://doi.org/10.21236/ad0609059
[research_eshow_1990]: https://ntrs.nasa.gov/citations/19900060676
[research_farris_1983]: https://ntrs.nasa.gov/citations/19830060450
[research_favaro_2025]: https://doi.org/10.3390/aerospace12060559
[research_fluk_1981]: https://doi.org/10.2514/6.1981-1623
[research_foltz_1962]: https://doi.org/10.21236/ad0414393
[research_foster_1987]: https://ntrs.nasa.gov/citations/19880003977
[research_foster_1988]: https://ntrs.nasa.gov/citations/19880049971
[research_friend_1964]: https://doi.org/10.2514/6.1964-787
[research_fry_1967]: https://doi.org/10.2514/6.1967-411
[research_fry_1969]: https://ntrs.nasa.gov/citations/19690025981
[research_gallagher_1972]: https://ntrs.nasa.gov/citations/19720033312
[research_garner_1967]: https://doi.org/10.21236/ad0658432
[research_garren_1965]: https://ntrs.nasa.gov/citations/19650012141
[research_garren_kelly_1965]: https://ntrs.nasa.gov/citations/19650025398
[research_gentry_margason_1966]: https://ntrs.nasa.gov/citations/19660006875
[research_george_1964]: https://doi.org/10.21236/ad0608185
[research_gerdes_1964]: https://ntrs.nasa.gov/citations/19640018145
[research_gerdes_rolls_1969]: https://ntrs.nasa.gov/citations/19690029422
[research_goka_1980]: https://ntrs.nasa.gov/citations/19800061737
[research_gold_walchli_1974]: https://doi.org/10.2514/6.1974-952
[research_goldberger_1966]: https://doi.org/10.21236/ad0644191
[research_goldstein_1982]: https://ntrs.nasa.gov/citations/19820015335
[research_grahame_1968]: https://doi.org/10.2514/6.1968-637
[research_grahame_1969]: https://doi.org/10.2514/3.44022
[research_grauer_morelli_2023]: https://doi.org/10.2514/1.c037583
[research_greene_russo_1967]: https://doi.org/10.2514/6.1967-249
[research_greenwood_1960]: https://doi.org/10.1037/e417302004-001
[research_greif_1972]: https://ntrs.nasa.gov/citations/19720020365
[research_hafer_skinner_1960]: https://doi.org/10.21236/ad0472676
[research_haines_1980]: https://ntrs.nasa.gov/citations/19800017541
[research_harper_cooper_1984]: https://doi.org/10.2514/6.1984-2442
[research_harper_p_1955]: https://doi.org/10.21236/ad0092496
[research_harper_sardanowsky_1969]: https://doi.org/10.21236/ad0858184
[research_harvey_waugh_1976]: https://doi.org/10.21236/ada023728
[research_hegarty_1965]: https://ntrs.nasa.gov/citations/19650007734
[research_henderson_1963]: https://doi.org/10.2514/6.1963-1010
[research_hess_1977]: https://ntrs.nasa.gov/citations/19780028540
[research_hess_1981]: https://doi.org/10.2514/6.1981-1771
[research_hess_1984]: https://doi.org/10.2514/6.1984-236
[research_hewes_1967]: https://doi.org/10.2514/6.1967-239
[research_hilgendorf_1975]: https://doi.org/10.21236/adb002554
[research_hill_1981]: https://ntrs.nasa.gov/citations/19820033375
[research_hill_1983]: https://ntrs.nasa.gov/citations/19830055846
[research_hill_waters_1974]: https://doi.org/10.2514/6.1974-969
[research_hindson_1982]: https://ntrs.nasa.gov/citations/19820015354
[research_hoffman_1971]: https://doi.org/10.2514/6.1971-768
[research_hoh_1985]: https://ntrs.nasa.gov/citations/19850061706
[research_hoh_mitchell_1983]: https://doi.org/10.21236/ada132857
[research_howard_1976]: https://ntrs.nasa.gov/citations/19990117220
[research_huntley_1972]: https://doi.org/10.1017/s0001924000043104
[research_hutchings_1977]: https://ntrs.nasa.gov/citations/19780011161
[research_innis_anderson_1972]: https://ntrs.nasa.gov/citations/19730024222
[research_irvin_swan_1956]: https://doi.org/10.21236/ad0147927
[research_jarvis_1967]: https://doi.org/10.2514/6.1967-273
[research_johns_1989]: https://ntrs.nasa.gov/citations/19900037988
[research_johns_1990]: https://ntrs.nasa.gov/citations/19900016693
[research_johnson_craig_1974]: https://doi.org/10.2514/6.1974-836
[research_johnston_1965]: https://doi.org/10.21236/ad0622578
[research_johnston_friend_1965]: https://doi.org/10.4050/sm_vstol_1965-2533
[research_juhasz_2025]: https://doi.org/10.1017/aer.2025.35
[research_kamman_hall_1978]: https://doi.org/10.21236/ada062097
[research_karemaa_1971]: https://doi.org/10.2514/6.1971-767
[research_keller_1969]: https://doi.org/10.2514/6.1969-545
[research_kelly_1977]: https://ntrs.nasa.gov/citations/19770021193
[research_kesselyak_1974]: https://doi.org/10.2514/6.1974-1039
[research_key_1965]: https://doi.org/10.2514/6.1965-706
[research_key_1971]: https://doi.org/10.21236/ad0725746
[research_kidd_bull_1963]: https://doi.org/10.21236/ad0400265
[research_kirby_1961]: https://ntrs.nasa.gov/citations/20040047148
[research_kluever_1967]: https://doi.org/10.2514/6.1967-238
[research_kohn_1972]: https://doi.org/10.1115/72-gt-73
[research_kotansky_1982]: https://ntrs.nasa.gov/citations/19820015292
[research_kuhn_1979]: https://doi.org/10.21236/ada073099
[research_lemons_dukes_1975]: https://ntrs.nasa.gov/citations/19750025623
[research_levinsky_1968]: https://doi.org/10.21236/ad0680969
[research_levison_1982]: https://ntrs.nasa.gov/citations/19820026174
[research_lissaman_1967]: https://doi.org/10.2514/6.1967-2
[research_lollar_matous_1963]: https://doi.org/10.1109/thfe.1963.231288
[research_longhurst_1966]: https://doi.org/10.4271/660315
[research_lovell_1953]: https://ntrs.nasa.gov/citations/20050029472
[research_marchese_1963]: https://doi.org/10.21236/ad0442887
[research_margason_1966]: https://ntrs.nasa.gov/citations/19660015330
[research_markson_1963]: https://doi.org/10.1016/b978-0-12-395707-8.50027-9
[research_martin_1963]: https://doi.org/10.2514/6.1963-484
[research_mc_lemore_1966]: https://ntrs.nasa.gov/citations/19660018439
[research_mccabe_1967]: https://ntrs.nasa.gov/citations/19670061371
[research_mccabe_1967_2]: https://ntrs.nasa.gov/citations/19670041333
[research_mccormick_1969]: https://doi.org/10.21236/ad0863818
[research_mccormick_mallen_1956]: https://doi.org/10.4050/sm_wf_1956-2299
[research_mcelreath_1972]: https://doi.org/10.21236/ad0755374
[research_mcgregor_smith_1965]: https://doi.org/10.2514/6.1965-705
[research_mcintyre_1963]: https://doi.org/10.21236/ad0602427
[research_merrick_1977]: https://ntrs.nasa.gov/citations/19780008120
[research_merrick_1981]: https://ntrs.nasa.gov/citations/19810021598
[research_merrick_1982]: https://ntrs.nasa.gov/citations/19820012312
[research_merrick_1984]: https://ntrs.nasa.gov/citations/19850006532
[research_michaelsen_1971]: https://doi.org/10.2514/6.1971-992
[research_miller_1948]: https://doi.org/10.2514/8.11623
[research_mitchell_1964]: https://doi.org/10.21236/ad0449587
[research_mitchell_1987_2]: https://ntrs.nasa.gov/citations/19870062304
[research_mitchell_1989]: https://ntrs.nasa.gov/citations/19890064331
[research_mitchell_hart_1993]: https://ntrs.nasa.gov/citations/19940008844
[research_moen_yenni_1975]: https://ntrs.nasa.gov/citations/19760004969
[research_mooij_1973]: https://ntrs.nasa.gov/citations/19750011079
[research_morello_1972]: https://ntrs.nasa.gov/citations/19720016362
[research_morse_newhouse_1960]: https://doi.org/10.21236/ad0248356
[research_morse_newhouse_1961]: https://doi.org/10.21236/ad0264226
[research_motyka_1975]: https://doi.org/10.21236/ada025359
[research_mourtos_1995]: https://ntrs.nasa.gov/citations/19950016249
[research_naca_1960]: https://ntrs.nasa.gov/citations/19630004807
[research_naca_1966_2]: https://ntrs.nasa.gov/citations/19670006521
[research_naca_1967]: https://ntrs.nasa.gov/citations/19680006432
[research_naca_1969]: https://ntrs.nasa.gov/citations/19700005572
[research_naca_1970]: https://ntrs.nasa.gov/citations/19700021566
[research_naca_1972]: https://ntrs.nasa.gov/citations/19730001377
[research_naca_1975]: https://ntrs.nasa.gov/citations/19750025602
[research_naca_1977]: https://ntrs.nasa.gov/citations/19790009304
[research_naca_1981]: https://ntrs.nasa.gov/citations/19820005792
[research_newell_1963]: https://doi.org/10.21236/ad0425705
[research_nichols_1963]: https://doi.org/10.1017/s0001924000062783
[research_nishimura_1980]: https://doi.org/10.2514/3.57903
[research_obryan_1966]: https://ntrs.nasa.gov/citations/19660059610
[research_owen_cox_1966]: https://doi.org/10.1016/0022-460x(66)90141-6
[research_parrish_bowles_1983]: https://ntrs.nasa.gov/citations/19830013921
[research_patierno_asdurian_1965]: https://doi.org/10.4050/sm_vstol_1965-3112
[research_pausder_blanken_1992]: https://ntrs.nasa.gov/citations/19940035438
[research_pausder_blanken_1993]: https://ntrs.nasa.gov/citations/19940008827
[research_payne_1955]: https://doi.org/10.1017/s0368393100116955
[research_perry_2023]: https://doi.org/10.2514/1.c036616
[research_person_robbins_1965]: https://ntrs.nasa.gov/citations/19660022563
[research_pollack_1967]: https://doi.org/10.2514/6.1967-241
[research_przedpelski_1965]: https://doi.org/10.2514/6.1965-708
[research_putman_1977]: https://doi.org/10.21236/ada045315
[research_queijo_1953]: https://ntrs.nasa.gov/citations/20050080793
[research_rampy_1966]: https://doi.org/10.21236/ad0641371
[research_rhoads_1967]: https://doi.org/10.21236/ad0820790
[research_rhoads_1970]: https://doi.org/10.21236/ad0876589
[research_riley_1989]: https://ntrs.nasa.gov/citations/19900002435
[research_rimer_sperling_1965]: https://doi.org/10.2514/6.1965-1437
[research_roberts_1964]: https://doi.org/10.1007/978-3-7091-4688-0_3
[research_rolls_1965]: https://ntrs.nasa.gov/citations/19650021531
[research_rolls_1965_4]: https://ntrs.nasa.gov/citations/19660013004
[research_roscoe_1975]: https://doi.org/10.21236/ada022459
[research_schade_1968]: https://ntrs.nasa.gov/citations/19680064091
[research_schwartz_shearer_1964]: https://doi.org/10.2514/6.1964-773
[research_sellers_1977]: https://ntrs.nasa.gov/citations/19770052110
[research_sellers_szuch_1973]: https://ntrs.nasa.gov/citations/19730007088
[research_shanks_smith_1959]: https://ntrs.nasa.gov/citations/19980235622
[research_shanks_smith_1960]: https://ntrs.nasa.gov/citations/19980230619
[research_simmons_2023_2]: https://doi.org/10.2514/1.c037260
[research_sinacori_1986]: https://doi.org/10.21236/ada359459
[research_sissingh_1956]: https://doi.org/10.21236/ad0116272
[research_skifstad_1970]: https://doi.org/10.2514/3.44146
[research_smith_1958]: https://ntrs.nasa.gov/citations/19980227972
[research_smith_1958_2]: https://ntrs.nasa.gov/citations/19710082837
[research_smith_1966]: https://ntrs.nasa.gov/citations/19670006542
[research_smith_1966_2]: https://doi.org/10.2514/3.43700
[research_smith_1973]: https://doi.org/10.21236/ad0754840
[research_smith_1974]: https://ntrs.nasa.gov/citations/19740048075
[research_stapleford_1980]: https://doi.org/10.4271/801206
[research_stevens_roskam_1985]: https://ntrs.nasa.gov/citations/19860003826
[research_strand_1967]: https://doi.org/10.2514/3.43869
[research_takahashi_1994]: https://ntrs.nasa.gov/citations/20020014293
[research_tapscott_1960]: https://ntrs.nasa.gov/citations/19630004822
[research_tapscott_1960_2]: https://ntrs.nasa.gov/citations/19740076595
[research_tomizuka_whitney_1976]: https://doi.org/10.1115/1.3427058
[research_tosti_1961]: https://ntrs.nasa.gov/citations/19980227992
[research_vallerie_1967]: https://ntrs.nasa.gov/citations/19670020039
[research_vinje_1968]: https://doi.org/10.1109/tmms.1968.300015
[research_vinje_miller_1973]: https://doi.org/10.21236/ad0769868
[research_wachtell_1970]: https://doi.org/10.21236/ad0874029
[research_walker_1965]: https://doi.org/10.21236/ad0617129
[research_wang_2026_4]: https://doi.org/10.1016/j.cnsns.2026.110180
[research_wang_chen_2024]: https://doi.org/10.3390/aerospace11090711
[research_washizu_1978]: https://ntrs.nasa.gov/citations/19790007419
[research_watson_hindson_1988]: https://ntrs.nasa.gov/citations/19890005747
[research_westbrook_1964]: https://doi.org/10.2514/6.1964-777
[research_white_1960]: https://doi.org/10.21236/ad0251154
[research_williams_butler_1964]: https://doi.org/10.2514/6.1964-1103
[research_xu_2025_3]: https://doi.org/10.1109/thms.2024.3502178
[research_young_1964]: https://doi.org/10.1109/thfe.1964.231648

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
