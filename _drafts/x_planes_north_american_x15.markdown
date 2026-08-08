---
layout: post
mathjax: true
comments: true
title: "X-Planes: North American X-15"
date: 2025-10-21 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 16
---

<!-- A312 -->
<script>console.log("A312");</script>

The [North American X-15][ref_x15] is the most heavily documented aircraft in this series and that is the problem with writing about it. Two hundred flights, nine years, three airframes, twelve pilots, and a literature large enough that any account can be assembled from primary sources without ever deciding what the aircraft was for. **Every previous article in this series found its keystone by looking for the one binding unknown. Here the unknown is not scarce but abundant**, and the keystone has to be chosen and defended rather than discovered. This article is the sixteenth in the [X-Planes series][related_post_a297_xplanes_framing], following the [X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], the [X-4][related_post_a301_northrop_x4], the [X-5][related_post_a302_bell_x5], the [X-6][related_post_a303_convair_x6], the [X-7][related_post_a304_lockheed_x7], the [X-8][related_post_a305_aerojet_x8], the [X-9][related_post_a306_bell_x9], the [X-10][related_post_a307_north_american_x10], the [X-11][related_post_a308_convair_x11], the [X-12][related_post_a309_convair_x12], the [X-13][related_post_a310_ryan_x13], and the [X-14][related_post_a311_bell_x14].

The choice made here is **energy**, and specifically one fact about it. At the speed the X-15 reached, **the kinetic energy of every kilogramme of the aircraft was more than twice the energy needed to melt that kilogramme**. Flight at that speed is therefore not fast flight with heating added. It is the problem of carrying an amount of energy that would destroy the vehicle if it went to the wrong place, and then disposing of all of it before landing. The standard inventory entry remains [Jenkins Landis and Miller 2003 American X-Vehicles, An Inventory X-1 to X-50][book_jenkins_landis_miller_2003], the vehicle compilation is [Miller 2001 The X-Planes, X-1 to X-45][book_miller_2001], and the programme's own conference record is [NACA 1958][research_naca_1958] and [Beeler 1961][research_beeler_1961].

## The Research Question

The X-15 was designed to fly at Mach 6 and to reach the edge of the atmosphere, and both of those are usually offered as its purpose. Neither is a research question. They are places.

### Choosing the Keystone, and Saying Why

Four candidate keystones are all well supported by the record, and it is worth naming them before choosing, because an article that picks one silently is hiding a decision.

**Aerodynamic heating** is the conventional answer and it is not wrong. The X-15 was the first aircraft whose structure was designed by temperature rather than by load.

**Hypersonic stability and control** is defensible. Nobody knew whether an aeroplane could be controlled at Mach 6, and the wedge tail exists because of that doubt.

**Flight outside the atmosphere** is defensible. The X-15 was the first winged vehicle to leave the sensible atmosphere under its own power and return.

**Structures at temperature** is defensible. Inconel X was chosen, formed, and welded for this aircraft, and the manufacturing problem was severe.

The trouble with all four is that they are consequences of a single quantity, and treating any one as primary makes the other three look like separate subjects when they are the same subject. **The quantity is energy.**

### The Statement of the Keystone

An aircraft at Mach 6.7 carries a kinetic energy per unit mass of

$$e_{k} = \tfrac{1}{2} V^{2} = \tfrac{1}{2} \times 2{,}020.6^{2} = 2.041 \times 10^{6} \text{ J/kg}$$

The energy required to take a kilogramme of the nickel alloy the aircraft was built from up to its melting point and melt it is the sensible heat plus the latent heat,

$$h_{\text{melt}} = c_{p}\left(T_{m} - T_{0}\right) + L_{f}$$

which at a specific heat near 440 joules per kilogramme kelvin, a melting point near 1,393 degrees Celsius, and a latent heat near 300 kilojoules per kilogramme is

$$h_{\text{melt}} = 440 \times 1{,}373 + 300{,}000 = 0.904 \times 10^{6} \text{ J/kg}$$

The ratio is the number this article is built on.

$$\frac{e_{k}}{h_{\text{melt}}} = \frac{2.041}{0.904} = 2.26$$

**The X-15 at its record speed carried, in every kilogramme of itself, more than twice the energy needed to melt that kilogramme.** Against the temperature the structure was actually designed to tolerate, 1,200 degrees Fahrenheit, the margin is far wider still,

$$\frac{e_{k}}{c_{p}\left(T_{\text{design}} - T_{0}\right)} = \frac{2.041 \times 10^{6}}{0.277 \times 10^{6}} = 7.4$$

so the aircraft carried more than seven times the energy that would have taken its entire structure to the limit of its strength.

### Why That Is the Right Keystone

The research question follows immediately, and it dimensions everything.

> Can a piloted aircraft carry that much energy, dispose of all of it, and land?

**Disposal is the operative word.** A conventional aircraft sheds energy through drag and nobody thinks about where it goes, because there is not much of it. At hypersonic speed the drag work is the dominant term in a thermal balance, and the question is not whether the vehicle slows down but how much of the energy it sheds ends up inside its own structure rather than in the air behind it.

That question dimensions the airframe, because the structure must survive whatever fraction arrives. It dimensions the trajectory, because heating rate depends on density and speed and the heat load is an integral along the path, so **trajectory shape is a thermal design variable rather than a matter of taste**. It dimensions the propulsion, because burn time fixes how much energy is put in. And it dimensions the control system, because energy must be shed across a range of dynamic pressures spanning four orders of magnitude, and aerodynamic surfaces work at one end of that range and not the other.

### The Series Thread, Which Arrives From an Unexpected Direction

That last point connects this aircraft to the two before it in a way that is worth stating early.

The [X-13][related_post_a310_ryan_x13] and the [X-14][related_post_a311_bell_x14] lost their aerodynamic control authority because the vehicle was not moving. The X-15 loses it because there is no air. **The relation is identical and the cause is opposite**, and so, remarkably, is the answer. Both aircraft carry reaction jets and both must hand over between them and the aerodynamic surfaces. The previous article's central relation,

$$M_{\text{aero}} = q \, S \, \bar{c} \, \Delta C_{m}, \qquad q = \tfrac{1}{2}\rho V^{2}$$

holds here unchanged, and the X-15 drives $q$ to zero by making $\rho$ vanish rather than by making $V$ vanish.

## Programme Origin

The X-15 originates in a request rather than in a proposal. In 1954 the NACA Committee on Aerodynamics recommended a research aircraft for flight at very high speed and altitude, the Air Force and Navy agreed to fund it jointly with the NACA directing the research, and North American Aviation won the airframe contract in 1955 against competing designs.

### The Institutional Arrangement Was the Unusual Part

The X-15 was a genuinely tripartite programme. The NACA, and from 1958 NASA, specified the research and analysed the results. The Air Force and Navy paid. North American built the aircraft and Reaction Motors built the engine. The flight programme was run from Edwards with government and contractor pilots.

**This is the arrangement the [X-1][related_post_a298_bell_x1] established, scaled up by an order of magnitude in cost and duration**, and the X-15 is the last research aircraft for which it worked at this scale. The conference reports, of which [NACA 1958][research_naca_1958] and [Beeler 1961][research_beeler_1961] are two, are the visible product of it, and they are unusual documents because they record a programme reporting on itself to its sponsors while it was still running.

### What Was Known and What Was Not

By 1954 the theory of hypersonic heating existed. The blunt-body insight, that a blunt shape pushes most of its energy into the air rather than into itself, was already established, and the stagnation-point heat transfer problem was being solved analytically, as in [Eggers et al 1958][research_eggers_1958]. What did not exist was any flight data at all above Mach 3, and the [X-2][related_post_a299_bell_x2] had reached Mach 3.2 and been lost immediately afterward.

The materials position was worse. [Steinbacher and Young 1955][research_steinbacher_young_1955] surveys the problems of designing aircraft subjected to high temperature, and the alloy the X-15 would use was still being developed as sheet, in work reported later in [Greenewald and Riley 1963][research_greenewald_riley_1963] and [Duff and Watson 1964][research_duff_watson_1964]. **The aircraft was ordered before the material it is made of was a settled product.**

## Sizing From First Principles

The keystone relation is an accounting identity and it is worth writing before anything else, because every subsystem argument below is a term in it.

### The Energy Budget

The specific energy of the aircraft at any instant is the sum of its potential and kinetic terms,

$$e = g h + \tfrac{1}{2} V^{2}$$

The engine adds energy, gravity and drag remove it, and the flight ends when $e$ has been reduced to the value corresponding to a landing.

$$\frac{de}{dt} = \frac{T V}{m} - \frac{D V}{m}$$

**Everything the X-15 did is contained in the difference between those two terms.** The first acts for eighty to a hundred and fifty seconds. The second acts for the remaining eight to twelve minutes.

It is worth establishing how much of the budget the carrier aircraft supplies, because the launch from a B-52 is often described as though it were a substantial head start. Dropping near 13.7 kilometres at about Mach 0.8 gives

$$e_{\text{launch}} = 9.807 \times 13{,}716 + \tfrac{1}{2} \times 236^{2} = 0.135 + 0.028 = 0.162 \text{ MJ/kg}$$

against the 2.347 megajoules per kilogramme the speed record reached.

$$\frac{0.162}{2.347} = 0.069$$

**The carrier supplies under seven percent of the energy.** The X-15 makes the other ninety-three percent itself, and the B-52 exists to save propellant and to put the launch point where the trajectory needs it rather than to provide a meaningful fraction of the budget.

### The Two Records Are Two Projections of One Budget

The X-15 holds two records and they are usually reported as separate achievements. They are the same quantity, differently partitioned.

The speed record, Flight 188 flown by Knight on 3 October 1967, reached 4,520 miles per hour at 102,100 feet. In specific energy that is

$$e = 9.807 \times 31{,}120 + \tfrac{1}{2} \times 2{,}020.6^{2} = 0.305 + 2.041 = 2.347 \text{ MJ/kg}$$

The altitude record, Flight 91 flown by Walker on 22 August 1963, reached 354,200 feet, but the informative instant is burnout, at about 176,000 feet and 3,794 miles per hour.

$$e = 9.807 \times 53{,}645 + \tfrac{1}{2} \times 1{,}696.1^{2} = 0.526 + 1.438 = 1.964 \text{ MJ/kg}$$

The comparison is cleanest in the units of altitude, because specific energy divided by gravity is a height. The energy height is what the vehicle would reach if it converted everything,

$$h_{e} = h + \frac{V^{2}}{2g}$$

which gives 239.3 kilometres for Flight 188 and 200.3 for Flight 91 at burnout.

$$h_{e,188} = 31.12 + 208.17 = 239.29 \text{ km}$$

and for the altitude flight at the instant its engine stopped,

$$h_{e,91} = 53.64 + 146.67 = 200.31 \text{ km}$$

**Energy height also provides a check on the ballistic coast.** If the arc above burnout is genuinely drag free, energy height is conserved along it, and evaluating at Flight 91's apogee with the horizontal speed derived below gives

$$h_{e,\text{apogee}} = 107.96 + 92.36 = 200.32 \text{ km}$$

which agrees with the burnout value to ten metres in two hundred kilometres. **The coast above 53 kilometres is drag free to within the precision of the input data**, which retrospectively justifies treating it that way.

**The two flights are eighty-seven percent alike in the quantity that matters and utterly different in how it is arranged.** One put 87 percent of its energy into speed, the other 73 percent.

$$\frac{2.347}{1.964} = 1.195$$

The speed flight carried 19.5 percent more, and the reason is not piloting. **Flight 188 was flown by the X-15A-2 with external tanks that raised the propellant load by about 75 percent.** The extra energy was bought rather than flown for.

### What the Altitude Record Cost

The energy budget makes a comparison available that neither record alone suggests. Convert the speed record's kinetic energy entirely into height,

$$h = \frac{V^{2}}{2g} = \frac{2{,}020.6^{2}}{2 \times 9.807} = 208.2 \text{ km}$$

which added to the 31.1 kilometres it was already at gives 239.3 kilometres, against an actual altitude record of 108.0. **A little over half the available energy did not reach apogee**, and the difference is what the atmosphere took on the way up, plus the fact that the altitude flights were flown with less propellant.

This is the first appearance of the article's recurring point. **The atmosphere is simultaneously the thing that makes the aircraft possible and the thing that takes its energy**, and every design decision below is a negotiation about how much of it to be in.

### Checking the Budget Against the Rocket Equation

The engine's contribution can be checked independently. At a vacuum specific impulse of 276 seconds the effective exhaust velocity is

$$v_{e} = I_{sp} \, g_{0} = 276 \times 9.807 = 2{,}706.6 \text{ m/s}$$

and with a gross mass of 15,195 kilogrammes over an empty mass of 6,622 the mass ratio and ideal velocity increment are

$$\frac{m_{0}}{m_{f}} = 2.294, \qquad \Delta V = v_{e} \ln 2.294 = 2{,}248 \text{ m/s}$$

The speed record was 2,020.6 metres per second, which is

$$\frac{2{,}020.6}{2{,}248} = 0.899$$

**Ninety percent of the ideal.** For a vehicle that climbs through the atmosphere under a gravity field, losing energy to drag and to lifting itself, that is a remarkably small loss, and it is a consequence of a thrust-to-weight ratio of

$$\frac{T}{W} = \frac{253{,}500}{15{,}195 \times 9.807} = 1.70$$

which gets the aircraft out of the dense air quickly.

### Where the Energy Goes, and What Reaches the Structure

### The Temperature the Air Arrives At

Before any heat-transfer relation, there is a temperature difference driving it, and at hypersonic speed that difference is set almost entirely by the vehicle's own speed.

Air brought to rest against the vehicle converts its kinetic energy into enthalpy, so the stagnation temperature is

$$\frac{T_{0}}{T_{\infty}} = 1 + \frac{\gamma - 1}{2} M^{2}$$

At Mach 6.7 that factor is 9.978, and the standard atmosphere gives an ambient temperature of 227.6 kelvin at the record altitude, so

$$T_{0} = 227.6 \times 9.978 = 2{,}271 \text{ K} = 3{,}628\ ^{\circ}\text{F}$$

**The air the aircraft is flying into is 2.46 times hotter than the metal is permitted to become.** The structure's problem is not that it is going fast. It is that it is immersed in a gas at two thousand degrees Celsius.

A boundary layer does not quite reach the stagnation temperature, because some enthalpy is carried away rather than recovered. Writing the recovery factor $r$,

$$T_{aw} = T_{\infty}\left(1 + r\,\frac{\gamma - 1}{2} M^{2}\right)$$

which for a turbulent layer at $r = 0.89$ gives 2,046 kelvin, and for a laminar layer at $r = 0.85$ gives 1,965. **The adiabatic wall temperature is the temperature the surface would reach if it could not lose heat at all**, and every heat-transfer calculation below is really a calculation of how far below it the surface actually sits.

The scale of the effect is worth writing as an enthalpy. The total enthalpy of the oncoming stream is

$$h_{0} = c_{p} T_{\infty} + \tfrac{1}{2} V^{2} = 0.229 + 2.041 = 2.270 \text{ MJ/kg}$$

of which the kinetic term is **89.9 percent**. The atmosphere at that altitude contributes almost nothing. **The heat is the aircraft's own energy arriving back at it.**

### Where the Energy Goes

The disposal problem is not the total energy but the rate at which it arrives at the surface. The stagnation-point convective heating rate follows a correlation of the form

$$\dot{q} = k \sqrt{\frac{\rho}{R_{n}}}\, V^{3}$$

with $k = 1.7415 \times 10^{-4}$ in SI units, $\rho$ the free-stream density, and $R_{n}$ the nose radius. **Two features of that relation govern the entire design.**

The first is the cube on velocity. Doubling speed multiplies the heating rate by eight, which is why the difference between Mach 3 and Mach 6 is a difference in kind rather than in degree.

The second is the square root on density, and the inverse square root on nose radius. **A blunt nose reduces heating**, which is the insight that made re-entry possible and which [Eggers et al 1958][research_eggers_1958] treats analytically. The X-15's nose is blunt for this reason and for no aerodynamic one, and the trade can be written down. Heating falls as the inverse square root of the nose radius while the nose's own pressure drag rises with its frontal area,

$$\dot{q} \propto R_{n}^{-1/2}, \qquad D_{\text{nose}} \propto R_{n}^{2}$$

so eliminating the radius between them gives

$$D_{\text{nose}} \propto \dot{q}^{-4}$$

**Halving the heating costs sixteen times the nose drag.** That fourth-power exchange rate is why a re-entry capsule, which does not have to fly anywhere afterwards, is as blunt as it can be made, and why an aeroplane that must also glide several hundred kilometres to a runway is not.

A third feature is absent from the relation and dominates the real problem. **A turbulent boundary layer transfers heat several times faster than a laminar one**, so where transition occurs matters more than most of the terms that are written down. The subject was under active investigation throughout the X-15's life and was not settled by it, in [Deem and Murphy 1965][research_deem_murphy_1965] on flat plates, [Sheetz 1965][research_sheetz_1965] on free flight, [Bueche 1966][research_bueche_1966] on the effect of surface roughness, [Henderson 1967][research_henderson_1967] and [Softley 1969][research_softley_1969] on cones, [Larson 1968][research_larson_1968] on results that did not fit, and [Masaki and Yakura 1968][research_masaki_yakura_1968] on how to carry a transitional layer through a heating analysis at all. [Berry 1967][research_berry_1967] flew an experiment for the purpose.

**Every number computed in this section assumes a boundary-layer state it does not derive**, and that assumption is the largest uncertainty in the analysis.

Evaluating at the speed record, with a 1976 standard atmosphere giving a density of 0.0155 kilogrammes per cubic metre at 31,120 metres and an assumed effective nose radius of 0.0762 metres,

$$\dot{q} = 1.7415 \times 10^{-4} \sqrt{\frac{0.0155}{0.0762}} \times 2{,}020.6^{3} = 6.48 \times 10^{5} \text{ W/m}^{2}$$

which is 64.8 watts per square centimetre.

### The Number That Explains the Whole Airframe

A structure that cannot conduct heat away fast enough must radiate it, and a radiating surface in equilibrium sits at the temperature where its emission matches its input,

$$\varepsilon \sigma T^{4} = \dot{q} \quad \Longrightarrow \quad T = \left(\frac{\dot{q}}{\varepsilon \sigma}\right)^{1/4}$$

At an emissivity of 0.8 the design temperature of 1,200 degrees Fahrenheit, or 922 kelvin, corresponds to a sustainable heating rate of

$$\varepsilon \sigma T^{4} = 0.8 \times 5.670 \times 10^{-8} \times 922^{4} = 3.28 \times 10^{4} \text{ W/m}^{2}$$

or 3.28 watts per square centimetre. The speed record demanded 64.8.

$$\frac{64.8}{3.28} = 19.8$$

**The record flight asked the structure to reject nearly twenty times the heat its design temperature could radiate.** That single ratio is why the X-15A-2 was covered in an ablative coating, why the flight was the fastest ever made, and why nothing like it was attempted again.

The model can be checked. The radiative equilibrium temperature at that heating rate is

$$T = \left(\frac{6.48 \times 10^{5}}{0.8 \times 5.670 \times 10^{-8}}\right)^{1/4} = 1{,}944 \text{ K} = 3{,}040\ ^{\circ}\text{F}$$

against leading-edge temperatures reported near 2,700 degrees Fahrenheit on that flight. **The correlation overshoots the measurement by 12.7 percent**, which is close agreement for a relation carrying one assumed length scale, and the conclusion is insensitive to that scale because doubling the assumed nose radius changes the equilibrium temperature by only 8.3 percent.

### How Much of It Actually Reaches the Structure

The keystone was stated as a question about where the energy goes, and it has not yet been answered. It can be, approximately, and the answer contains something the framing did not anticipate.

Energy leaves the vehicle by drag, and drag has two parts that dispose of it in different places. **Pressure drag dissipates into the shock layer and the wake, where the vehicle never sees it again. Skin friction dissipates at the wall, which is where the structure is.** So the fraction of the vehicle's energy that threatens it is bounded by the fraction of its drag that is friction.

Of the friction dissipation, only part crosses into the surface. The Reynolds analogy relates the heat-transfer coefficient to the skin friction for a gas of Prandtl number near unity,

$$St = \frac{C_{H}}{\rho V c_{p}} \approx \frac{C_{f}}{2}$$

The heat entering the wall and the friction work done at it are then

$$\dot{q}_{w} = St\, \rho V c_{p} \left(T_{aw} - T_{w}\right), \qquad \tau V = \frac{C_{f}}{2}\, \rho V^{3}$$

and their ratio collapses to something remarkably simple,

$$\frac{\dot{q}_{w}}{\tau V} = \frac{c_{p}\left(T_{aw} - T_{w}\right)}{V^{2}}$$

**The velocity has cancelled out of the numerator entirely**, so the fraction depends only on how far the wall sits below the adiabatic wall temperature, measured against the vehicle's kinetic energy.

### The Result, Which Explains Why a Hot Structure Runs Hot

Evaluating at the record condition, with an adiabatic wall temperature of 2,046 kelvin,

$$\frac{c_{p}\left(T_{aw} - T_{w}\right)}{V^{2}} = \frac{1004.5 \times \left(2046 - T_{w}\right)}{2020.6^{2}}$$

gives

| Wall temperature | Fraction of friction work entering the wall |
|------------------|---------------------------------------------|
| 300 K, cold | 43.0 percent |
| 922 K, the design limit | 27.7 percent |
| 1,755 K, Knight's leading edges | 7.2 percent |

**A hot wall absorbs a smaller fraction than a cold one, and it is not a small difference.** Going from cold metal to the design limit cuts the fraction by more than a third, and at the temperature Knight's leading edges actually reached the wall was taking barely a seventh of what a cold wall would have taken.

This is the part the keystone framing did not anticipate. **A hot structure is not merely a structure that tolerates being hot. Running hot is part of the mechanism by which it protects itself**, because the driving temperature difference is what pushes heat into it, and a hot wall has less of one. The design is self-limiting in a way that an insulated cold structure is not.

### How Much of the Drag Is Friction

The remaining factor is the drag split, and it can be estimated rather than assumed. At the record condition the Reynolds number on the fuselage length is

$$Re_{L} = \frac{\rho V L}{\mu} = \frac{0.0155 \times 2020.6 \times 14.99}{1.48 \times 10^{-5}} = 3.2 \times 10^{7}$$

and a turbulent flat-plate correlation gives a skin friction coefficient of

$$C_{f} = \frac{0.0592}{Re_{L}^{0.2}} = 0.00187$$

Over a wetted area of order 113 square metres against a reference area of 18.58, the friction drag and the total drag are

$$D_{f} = C_{f}\, q\, A_{\text{wet}} = 6.7 \text{ kN}, \qquad D = C_{D}\, q\, S = 47 \text{ kN}$$

at a drag coefficient of 0.08, so friction is about 14 percent of the total. Sweeping the two uncertain inputs, wetted area from 90 to 130 square metres and drag coefficient from 0.05 to 0.12, gives a range of **8 to 26 percent, centring near 15**.

$$f_{\text{structure}} = 0.15 \times 0.277 = 0.042$$

**About four percent of the vehicle's kinetic energy ends up in its own structure.** That is the answer to the question the keystone asked.

### Four Percent Turns Out to Be Survivable, and the Reason Matters

The empty aircraft masses 6,622 kilogrammes, so its kinetic energy at the record is

$$E = m\, \tfrac{1}{2} V^{2} = 6{,}622 \times 2.041 \times 10^{6} = 13.52 \text{ GJ}$$

of which four percent is 0.56 gigajoules. Against that, a structure comprising perhaps 60 percent of the empty mass can absorb, in reaching its design temperature from ambient,

$$Q_{\text{capacity}} = m_{s} c_{p} \left(T_{\text{design}} - T_{0}\right) = 3{,}973 \times 440 \times 629 = 1.10 \text{ GJ}$$

so the ratio is

$$\frac{0.56}{1.10} = 0.51$$

and across the whole range of friction fractions it runs from 0.27 to 0.68. **The total heat load is comfortably within what the structure can hold, with roughly a factor of two in hand.**

That is worth sitting with, because it says the X-15's thermal problem is not a global energy problem at all. **The aircraft could absorb its entire heat load in its own thermal mass and still be below its design temperature.** Radiation, which over a five-minute descent from a hundred square metres at the design temperature rejects

$$\varepsilon \sigma T^{4} A\, \Delta t = 0.8 \times 5.670 \times 10^{-8} \times 922^{4} \times 100 \times 300 = 0.98 \text{ GJ}$$

is not required to close the budget. It is required to keep the surface at a temperature the metal survives while the budget is being spent.

### Which Confirms That the Constraint Is Rate, Not Load

The two halves of the analysis now agree, and they did not have to.

The heating-rate calculation found that the record condition demanded 19.8 times what the design temperature could radiate. The heat-load calculation finds that the total is only half of what the structure could absorb. **Those are consistent statements about a rate-limited structure**, and they are the quantitative form of the claim made earlier that a hot structure fails by exceeding a temperature rather than by filling up.

**The X-15 was never in danger of running out of thermal capacity. It was in continuous danger of exceeding a temperature at a point**, which is exactly the failure that took the pylon off the ventral on the fastest flight ever made. A vehicle whose margin is global has room for local surprises. A vehicle whose margin is local has none.

### Trajectory Is a Thermal Design Variable

Because the heating rate goes as the square root of density, and density falls roughly exponentially with height, flying higher at the same speed reduces the rate. The scale height that governs the fall is

$$H = \frac{R T}{g} \quad \Longrightarrow \quad \rho(h) \approx \rho_{0} e^{-h/H}$$

which for air at the temperatures of the middle atmosphere is between about 6.2 and 8.0 kilometres, so density falls by a factor of $e$ every seven kilometres or so. One scale height buys a factor of

$$\sqrt{e^{-1}} = e^{-1/2} = 0.607$$

and from the record altitude, climbing five kilometres cuts the density to 0.460 of its value and the heating rate to 0.678.

But the quantity that damages a structure is not the rate. It is the load,

$$Q = \int \dot{q} \, dt$$

and a trajectory flown higher takes longer, so the integral does not fall as fast as the rate. The distinction can be made concrete. Suppose a vehicle sheds a fixed energy $\Delta e$ at roughly constant speed. The time taken is set by the drag,

$$\Delta t \approx \frac{\Delta e \, m}{q S C_{D} V} \propto \frac{1}{\rho}$$

so the load is the rate multiplied by that time,

$$Q = \dot{q}\, \Delta t \propto \sqrt{\rho}\, V^{3} \times \frac{1}{\rho} = \frac{V^{3}}{\sqrt{\rho}}$$

**The rate falls with thinner air and the load rises.** They move in opposite directions, which is the sharpest statement of the trade this article can make.

Putting a number on the load is worth doing because it is the quantity an ablator is sized against. At the record heating rate, the integrated load per unit area over exposures of one, two, and five minutes is

$$Q = \dot{q}\,\Delta t = 6.48 \times 10^{5} \times \left\{60,\ 120,\ 300\right\} = \left\{38.9,\ 77.8,\ 194\right\} \text{ MJ/m}^{2}$$

**Tens to hundreds of megajoules per square metre** is the scale of the problem, and it is the number that decides how thick a coating has to be.

**The heating rate and the heat load are therefore optimised by different trajectories**, and which one binds depends on whether the structure fails by exceeding a temperature or by absorbing too much total energy. The X-15's hot structure, which has no insulation and reaches equilibrium quickly, is rate-limited. An ablative or insulated structure is load-limited. **The X-15A-2 changed from one regime to the other when it was coated**, which is a more interesting statement than the usual observation that the coating let it fly faster.

An ablator works by a different mechanism from a hot structure. It absorbs energy as latent heat of decomposition and carries it away in the mass that leaves, so its capacity is a total rather than a rate,

$$Q_{\text{ablator}} = \dot{m}_{\text{loss}}\, h_{\text{eff}}$$

where $h_{\text{eff}}$ is an effective heat of ablation and the mass loss is permanent. Rearranged, the mass consumed follows directly from the heating,

$$\dot{m}_{\text{loss}} = \frac{\dot{q} A}{h_{\text{eff}}}$$

and at the record heating rate over a representative five square metres, with an effective heat of ablation of 2.5 megajoules per kilogramme, this is 1.30 kilogrammes per second, or 156 kilogrammes over a two-minute exposure.

The reason so thin a coating can do what a thick structure cannot is a ratio of capacities,

$$\frac{h_{\text{eff}}}{c_{p}\left(T_{\text{design}} - T_{0}\right)} = \frac{2.5 \times 10^{6}}{440 \times 629} = 9.0$$

**A kilogramme of ablator absorbs nine times what a kilogramme of structure absorbs reaching its limit**, and it does so at whatever surface temperature the chemistry sets rather than at one the metallurgy permits. **A hot structure is reusable and rate-limited. An ablator is expendable and load-limited.** The material options of the period are surveyed in [Diaconis et al 1959][research_diaconis_1959], the alternative of evaporative film cooling in [Hermann 1962][research_hermann_1962], the aerodynamic consequences of a shape that changes as it ablates in [Chang 1966][research_chang_1966], and the testing problem in [Colosimo 1968][research_colosimo_1968].

### The Disposal Problem, Which Is the Other Half

The sizing so far has been about acquiring the energy. The keystone says the aircraft must also get rid of it, and that half is where the X-15 is least like a rocket and most like an aeroplane.

The quantity to be disposed of is nearly all of what the vehicle has. Landing occurs at about 200 miles per hour, which is a specific kinetic energy of

$$e_{\text{land}} = \tfrac{1}{2} \times 89.4^{2} = 4.00 \times 10^{3} \text{ J/kg}$$

against 2.041 million at the record. As a fraction,

$$\frac{e_{\text{land}}}{e_{k}} = \frac{4.00 \times 10^{3}}{2.041 \times 10^{6}} = 0.00196$$

**The flight is the disposal of 99.8 percent of the energy the vehicle possesses at its fastest.** Every design feature discussed below exists to make that disposal survivable.

### Disposal Has Only One Mechanism

There is no other way to shed the energy than to do work against drag. Writing the rate,

$$\frac{de}{dt} = -\frac{D V}{m} = -\frac{q S C_{D} V}{m}$$

and noting that the heating rate goes as $\sqrt{\rho}\,V^{3}$ while the disposal rate goes as $\rho V^{3}$, the two have different powers of density. Their ratio is

$$\frac{\dot{q}}{|de/dt|} \propto \frac{\sqrt{\rho}\,V^{3}}{\rho V^{3}} = \frac{1}{\sqrt{\rho}}$$

**Heating per unit of energy shed is worse in thin air than in thick.** That is the fact that shapes every re-entry trajectory ever flown, and it points the opposite way from intuition. A vehicle that lingers high to stay cool sheds energy slowly and accumulates heat load doing it, while a vehicle that descends into denser air heats harder but finishes sooner.

The X-15 is on the mild end of this because it never enters from orbit, but the structure of the trade is identical, and it is why the article treats trajectory as a thermal variable rather than a performance one.

### The Aircraft Cannot Dispose of Its Energy Where It Acquires It

One relation closes the keystone, and it is the one that explains why the flight has the shape it does.

Deceleration by drag at constant altitude obeys

$$\frac{dV}{dt} = -\frac{\rho S C_{D}}{2m} V^{2}$$

which integrates to a time to fall from one speed to another,

$$t = \frac{2m}{\rho S C_{D}}\left(\frac{1}{V_{f}} - \frac{1}{V_{0}}\right)$$

The group in front is the ballistic coefficient in disguise,

$$\beta = \frac{m}{C_{D} S} = \frac{6{,}622}{0.08 \times 18.58} = 4{,}455 \text{ kg/m}^{2}$$

and a vehicle with a large ballistic coefficient is one that does not want to slow down. Evaluating from the record speed to a landing speed at several altitudes gives times that settle the question.

| Altitude | Time to shed the energy |
|----------|--------------------------|
| 31 km, the record altitude | 102 minutes |
| 25 km | 40 minutes |
| 20 km | 18 minutes |
| 15 km | 8 minutes |
| 10 km | 4 minutes |

**An X-15 flight lasts eight to twelve minutes in total.** At the altitude where it sets its speed record the aircraft would need an hour and a half to slow down, which it does not have and could not survive.

$$\frac{102\ \text{min}}{10\ \text{min}} \approx 10$$

**So the aircraft cannot dispose of its energy where it acquires it. It must descend into denser air to do so**, and descending into denser air is precisely what raises the heating rate, since $\dot{q}$ goes as the square root of density.

That is the keystone stated as a single trap. **The vehicle must go where the heating is in order to get rid of the energy that causes the heating**, and the entire descent trajectory is the negotiation of that requirement. Every earlier result in this section is a term in it.

### The Glide, Which Is a Range Problem With a Fixed Budget

From engine shutdown the X-15 is a glider, and a glider's range is set by its lift-to-drag ratio,

$$R = \frac{L}{D} \, h$$

From the burnout altitude of Flight 91 at 53.6 kilometres, a lift-to-drag ratio of 4 gives 214.6 kilometres of range and a ratio of 2.5 gives 134.1. Expressing the whole energy budget as an equivalent range by converting the kinetic term at the same ratio,

$$R_{\text{equiv}} = \frac{L}{D} \, \frac{e}{g}$$

gives 801 kilometres at a ratio of 4 and 501 at 2.5, from the 1.964 megajoules per kilogramme available at burnout.

The other end of the glide is worth a number too. At the empty mass the wing loading is

$$\frac{W}{S} = \frac{6{,}622 \times 9.807}{18.58} = 3{,}495 \text{ N/m}^{2} = 73 \text{ lb/ft}^{2}$$

and touching down at 200 miles per hour at sea level requires

$$C_{L} = \frac{W}{\tfrac{1}{2}\rho_{0} V^{2} S} = \frac{64{,}950}{\tfrac{1}{2} \times 1.225 \times 89.4^{2} \times 18.58} = 0.71$$

**That is an unremarkable landing lift coefficient on a wing of aspect ratio 2.5**, which is the point. The aircraft that had just been at Mach 6.7 lands like a heavy delta-winged fighter, and the same wing does both jobs because at neither end is it being asked for very much.

**Those distances are the reason the X-15 was launched from a B-52 over Nevada and landed in California.** The flight plan is not a route. It is an energy budget with a lake bed at the end of it, and the launch point was chosen so that the budget closes.

### Why a Person Could Fly It

An energy-management problem with a fixed budget and one landing site sounds like a task requiring precision. [Garringer and Saltzman 1966][research_garringer_saltzman_1966] reports the fact that made it tractable.

**Ninety-five percent of the maximum supersonic lift-to-drag ratio is available anywhere between about seven and twelve degrees of angle of attack.** The optimum is therefore flat, and a pilot holding anywhere in a five-degree band gets within five percent of the best available range.

$$\frac{\Delta (L/D)}{(L/D)_{\max}} = 0.05 \quad \text{over} \quad 7^{\circ} < \alpha < 12^{\circ}$$

That is a fortunate property of a low-aspect-ratio wing at supersonic speed rather than a design achievement, and it is worth naming because the alternative would have required an automatic system the era could not have built. **The X-15's energy management was hand-flown because the optimum was broad enough to hit by hand.**

### Speed Brakes, Which Dispose of the Surplus

A fixed budget with a flat optimum still leaves the problem of arriving with too much energy rather than too little, and the answer is drag on demand. The X-15's vertical surfaces split to form speed brakes, which raise $C_{D}$ without changing lift and so move the vehicle down its energy curve without moving it along the ground.

$$\frac{L}{D} \rightarrow \frac{L}{D + \Delta D}$$

**A speed brake is a device for making the aircraft worse in a controlled way**, which is exactly what a vehicle with a surplus of the one quantity it cannot store requires, and it is the same logic that put a variable-stability system in the [X-14][related_post_a311_bell_x14] for a different purpose.

## Dependent Systems

Each subsystem was dimensioned against the energy problem, and the ordering below follows the dependency rather than convention.

### Structure, Which Is the Skin

The X-15 has a hot structure. There is no thermal protection system in the later sense, no tiles and no insulation blanket. **The load-bearing skin is also the heat shield, and it is expected to get hot and keep working.**

The material is Inconel X, a nickel-chromium alloy retaining useful strength to about 1,200 degrees Fahrenheit, which is the number that appears in the sizing above. The alloy's development as usable sheet is documented in [Greenewald and Riley 1963][research_greenewald_riley_1963] and [Duff and Watson 1964][research_duff_watson_1964], and the general design problem in [Wolfe 1964][research_wolfe_1964] and [Steinbacher and Young 1955][research_steinbacher_young_1955].

A hot structure buys simplicity and pays for it in thermal stress. A skin that is hot where it meets the airflow and cool where it meets internal structure expands differentially, and the resulting stress is

$$\sigma_{\text{thermal}} = E \, \alpha \, \Delta T$$

which for a nickel alloy with a Young's modulus near 214 gigapascals and an expansion coefficient near $1.3 \times 10^{-5}$ per kelvin reaches yield over a temperature difference of only a couple of hundred kelvin. Putting numbers to that, a temperature difference of 300 kelvin between skin and substructure gives

$$\sigma_{\text{thermal}} = 214 \times 10^{9} \times 1.3 \times 10^{-5} \times 300 = 8.3 \times 10^{8} \text{ Pa}$$

or 830 megapascals, which is of the same order as the alloy's yield strength at temperature. **A three hundred degree gradient is enough to yield the structure on its own, with no aerodynamic load applied at all.**

The design response is to remove the constraint rather than to strengthen against it. **The X-15's skin is corrugated along the wing leading edges and slotted elsewhere precisely to let it expand**, which is a structural feature that exists for no load reason at all. A corrugation is a spring in the direction it needs to be a spring in, and the thermal stress it carries is the product of the gradient and its own much lower effective stiffness rather than the full modulus of the material.

There is a second consequence that the sizing makes visible. The equilibrium temperature computed above is reached quickly, because a thin skin has little thermal mass. Writing the time constant for a skin of thickness $t$ and density $\rho_{s}$ heating toward equilibrium,

$$\tau_{\text{th}} \sim \frac{\rho_{s} t c_{p} T}{\dot{q}}$$

a 1.5 millimetre Inconel skin at 8,200 kilogrammes per cubic metre, reaching 900 kelvin under 64.8 watts per square centimetre, gives

$$\tau_{\text{th}} \sim \frac{8{,}200 \times 0.0015 \times 440 \times 900}{6.48 \times 10^{5}} = 7.5 \text{ s}$$

**The structure comes to equilibrium in under ten seconds**, which is short compared with the minutes the aircraft spends at speed. That is what makes the hot structure rate-limited rather than load-limited, and it is the quantitative form of the claim made earlier.

The same conclusion follows from the diffusion side. The thermal diffusivity of the alloy is

$$\alpha = \frac{k}{\rho_{s} c_{p}} = \frac{15}{8{,}200 \times 440} = 4.16 \times 10^{-6}\ \text{m}^{2}\text{/s}$$

and heat penetrates a distance of order $\sqrt{\alpha t}$, so a 1.5 millimetre skin is thermally through-soaked after

$$t = \frac{\left(1.5 \times 10^{-3}\right)^{2}}{4.16 \times 10^{-6}} = 0.5 \text{ s}$$

**The skin has no interior.** It is a single lumped temperature within half a second of anything happening to it, which is why the design can be reasoned about as a surface in radiative balance and why there is no thermal-lag margin to hide behind.

### Propulsion, Which Sets the Budget

The XLR99 delivered 57,000 pounds of thrust and burned anhydrous ammonia with liquid oxygen, with hydrogen peroxide driving the turbopump. It was throttleable between about 30 and 100 percent and it could be restarted, both of which were unusual and both of which exist because the energy delivered had to be controllable.

At a vacuum specific impulse of 276 seconds the mass flow at full thrust is

$$\dot{m} = \frac{T}{v_{e}} = \frac{253{,}500}{2{,}706.6} = 93.7 \text{ kg/s}$$

so the full internal load of 8,573 kilogrammes lasts

$$t_{b} = \frac{8{,}573}{93.7} = 91.5 \text{ s}$$

which reproduces the reported burn time of about ninety seconds. **The entire energy input to an X-15 flight happens in a minute and a half**, and everything else is disposal.

Because the mass falls by more than half while the thrust does not, the acceleration climbs throughout the burn. The thrust-to-weight ratio runs from

$$\frac{T}{W_{0}} = \frac{253{,}500}{15{,}195 \times 9.807} = 1.70 \quad \text{to} \quad \frac{T}{W_{f}} = \frac{253{,}500}{6{,}622 \times 9.807} = 3.90$$

so the net longitudinal acceleration, after subtracting the component the aircraft spends holding itself up, rises from about 0.7 g to about 2.9 g. **The pilot's workload is not constant during the boost and neither is his ability to reach the controls**, which is why the aircraft carried a side stick usable under acceleration in addition to the centre stick. Component development is reported in [Wiswell et al 1961][research_wiswell_1961].

### Control, Across Four Orders of Magnitude of Dynamic Pressure

This is where the aircraft is most unlike anything before it and most like the two articles before this one.

Aerodynamic control effectiveness is proportional to dynamic pressure, and dynamic pressure has a form that makes the altitude dependence explicit. Substituting the perfect-gas relation into its definition,

$$q = \tfrac{1}{2}\rho V^{2} = \frac{\gamma}{2}\, p\, M^{2}$$

**so at fixed Mach number the dynamic pressure follows the static pressure exactly**, and static pressure falls by roughly a factor of ten every sixteen kilometres. At the record condition this gives 31.8 kilopascals against 31.7 computed from density and velocity directly, which is the consistency check the substitution invites. Along a representative ballistic arc at 1,500 metres per second, the standard atmosphere gives

| Altitude | Density | Dynamic pressure |
|----------|---------|------------------|
| 30 km | 1.84 × 10⁻² kg/m³ | 433 lb/ft² |
| 50 km | 1.03 × 10⁻³ kg/m³ | 24.1 lb/ft² |
| 70 km | 8.28 × 10⁻⁵ kg/m³ | 1.95 lb/ft² |
| 84.9 km | 8.42 × 10⁻⁶ kg/m³ | 0.198 lb/ft² |

against a maximum recorded dynamic pressure of about 2,000 pounds per square foot. **The ratio between the highest and lowest dynamic pressures a single X-15 flight passes through is above four thousand.**

$$\frac{q_{\max}}{q_{80\,\text{km}}} = \frac{95{,}800}{20.8} = 4.6 \times 10^{3}$$

The crossover between the two systems is where their moments are equal,

$$q_{\times} S \bar{c}\, \Delta C_{m} = F \ell \quad \Longrightarrow \quad q_{\times} = \frac{F \ell}{S \bar{c}\, \Delta C_{m}}$$

and with the numbers above, a mean chord near 3 metres and a control-power coefficient near 0.1, this is

$$q_{\times} = \frac{500 \times 7}{18.58 \times 3 \times 0.1} = 628 \text{ Pa}$$

or about 13 pounds per square foot, which the standard atmosphere places near 55 kilometres at this speed. **The handover is not a point but a band, and the band sits high**, well above the altitudes at which the aircraft does most of its decelerating.

There is a coincidence in that number worth recording. Flight 91's engine burned out at about 53.6 kilometres, which is within a couple of kilometres of where this estimate puts the crossover. **On a high flight the engine stops at roughly the altitude where the aerodynamic surfaces stop working**, so the pilot loses thrust and aerodynamic control at nearly the same moment and flies the top of the arc on reaction jets alone. The coincidence is not designed. It falls out of a rocket aircraft whose boost ends where the air becomes thin enough to leave.

No set of aerodynamic surfaces works across the whole range. The aircraft therefore carries hydrogen peroxide reaction jets in the nose and wings, and the pilot flew with **three controllers**, a centre stick for aerodynamic control, a left-hand controller for the reaction jets, and a right-hand side stick for use under acceleration. Operating experience is [Adkins and Jarvis 1964][research_adkins_jarvis_1964].

The reaction system can be sized by the same relation the previous two articles used. Control power is moment over inertia,

$$\text{CP} = \frac{F \ell}{I}$$

and for a vehicle of 6,622 kilogrammes empty with a length of 15 metres, a plausible pitch radius of gyration of a quarter of the length gives

$$I_{y} \approx 6{,}622 \times \left(0.25 \times 15\right)^{2} = 9.3 \times 10^{4} \text{ kg m}^{2}$$

so a nose thruster pair of 500 newtons acting through 7 metres supplies

$$\text{CP} = \frac{500 \times 7}{9.3 \times 10^{4}} = 0.038 \text{ rad/s}^{2}$$

**That is a twentieth of the control power the X-14A's pilots called adequate for hovering**, and it was sufficient, because the tasks are not comparable. A hovering aircraft is closing a position loop through attitude against gravity. A ballistic aircraft outside the atmosphere is pointing itself, with no position consequence at all until it returns.

**The handover problem is nonetheless the X-14's problem with the sign of the cause reversed.** The X-14A's engineers asked how much control authority a pilot needs when there is no dynamic pressure because the aircraft is stationary, and the answer became a number in a specification. The X-15's pilots faced the same absence for the opposite reason and had the same answer available to them, which is one of the reasons the reaction controls worked as well as they did.

### Stability, and the Wedge

At hypersonic speed a conventional thin vertical fin loses effectiveness, because the lift-curve slope of a thin surface falls as Mach number rises. The X-15's answer is a vertical tail of wedge section, blunt-based and thick, which retains directional stability where a thin one would not.

The reason is visible in the simplest hypersonic pressure relation there is. Newtonian impact theory treats the flow as particles that lose their normal momentum on striking a surface, giving

$$C_{p} = 2 \sin^{2}\theta$$

for a surface inclined at $\theta$ to the stream. **The pressure coefficient depends on the inclination and not on Mach number at all**, which is precisely the property a designer wants at a speed where everything else is falling away.

The same relation says something about the whole aircraft that the article has not yet said. Newtonian theory gives a lift coefficient of

$$C_{L} = 2 \sin^{2}\alpha \cos\alpha$$

and holding the aircraft up at the record condition requires

$$C_{L} = \frac{m g}{q S} = \frac{6{,}622 \times 9.807}{31{,}651 \times 18.58} = 0.110$$

which solves to an angle of attack of about **13.8 degrees**. **A hypersonic aeroplane does not fly nose-first.** It flies at an attitude that would be a stall on any subsonic aircraft, because at those dynamic pressures lift comes from inclining the underside to the stream rather than from circulation, and the wing is a flat plate that happens to have an aerofoil section.

That relation also states the wedge's advantage numerically. A thin surface deflected three degrees and a ten-degree wedge give

$$C_{p} = 2\sin^{2} 3^{\circ} = 0.0055, \qquad C_{p} = 2\sin^{2} 10^{\circ} = 0.0603$$

a ratio of 11. **A thick wedge is not a slightly better fin at hypersonic speed. It is an order of magnitude better**, and the cost is paid in base drag at every other speed the aircraft flies at. [Nonweiler 1959][research_nonweiler_1959] treats the general control and stability problem of hypersonic aircraft in the same period.

The wedge works and it costs drag. **The base drag of a blunt-based fin is a permanent penalty paid to retain stability at a condition occupying perhaps thirty seconds of an eleven-minute flight**, and [Saltzman 1961][research_saltzman_1961] measured the base pressures that quantify it.

The lower ventral had to be jettisoned before landing because it was too long for the landing gear, which means the aircraft's directional stability changed configuration between the hypersonic phase and the approach. That is a real cost of the arrangement and it is not usually counted.

### The Adaptive System, Which Solved a Problem the Envelope Created

A damper gain that suits one flight condition suits no other when dynamic pressure varies by a factor of four thousand. The conventional answer is gain scheduling, which requires knowing the condition, and the X-15's condition was precisely what its instruments were struggling to measure.

The answer fitted to X-15-3 was the MH-96, a self-adaptive system that inferred the right gain from the aircraft's own response rather than from a schedule. The principle is to drive the loop gain up until a limit cycle appears at the servo, and then hold it just below that, so that **the aircraft's closed-loop response is held constant while the plant underneath it changes by orders of magnitude**. [NACA 1971][research_naca_1971] reports the flight experience, and the contemporary argument about whether the approach was wise at all is [Adkins and Taylor 1964][research_adkins_taylor_1964], whose title concedes the dispute. [Montgomery 1973][research_montgomery_1973] places it in the wider adaptive-systems programme.

The system also blended the aerodynamic and reaction controls automatically, so that a pilot flying X-15-3 used one stick where a pilot flying the other two used three. **That is the [X-14][related_post_a311_bell_x14]'s handover performed by machine rather than by hand**, six years after the X-14A measured how much authority the hand needed.

It is worth stating plainly that this system was fitted to the aircraft that was lost. The relationship between the two facts is examined in [Dennehy et al 2014][research_dennehy_2014] and this article does not assert one.

### The Ball Nose, Which Exists Because Nothing Else Would Work

A conventional pitot-static boom cannot survive the stagnation heating computed above, and cannot measure flow direction at Mach 6 in any case. The X-15 carried a spherical, servo-driven, liquid-nitrogen-cooled nose that nulled itself into the flow and reported angle of attack and sideslip directly.

**It is worth pausing on this, because the aircraft's most basic instrument was a research project.** [Lipscomb and Dodgen 1958][research_lipscomb_dodgen_1958] describes the all-attitude flight-data system and [Christensen and Dodgen 1961][research_christensen_dodgen_1961] the inertial system that supplemented it. An aircraft that cannot measure its own angle of attack cannot be flown at the edge of its envelope, and the ball nose is the reason the X-15's data are worth anything.

### The Pilot, Who Is a Component of the Thermal System

The pilot wore a full pressure suit, which is a spacecraft in the sense that it must maintain pressure and remove heat independently of the cabin. The suit development literature is substantial, including [Games et al 1954][research_games_1954], [Rosenbaum 1957][research_rosenbaum_1957], [FurryY et al 1962][research_furryy_1962], and [Hendler et al 1964][research_hendler_1964], the last on the metabolic cost of working in one.

**The cabin is a pressure vessel inside a structure at several hundred degrees**, which makes cooling a design problem rather than a comfort one, and the physiological effects of the flight regime are treated in [Raeke 1958][research_raeke_1958].

## The Flight Test Record

The record is the largest of any aircraft in this series and this section does not attempt to recount it. What follows is the shape of it and the three flights that bear on the keystone.

### The Shape

The first glide flight was on 8 June 1959 with Crossfield, the first powered flight on 17 September 1959, and the first flight with the intended XLR99 engine on 15 November 1960. The interim engines were a pair of XLR11s of the type the [X-1][related_post_a298_bell_x1] had used, which is a neat illustration of how long that engine remained the only available article.

The programme ran to **199 flights and ended on 24 October 1968**, having been flown by twelve pilots, eight of whom qualified for astronaut wings. Early results are collected in [Finch and Matranga 1959][research_finch_matranga_1959], [McKay 1959][research_mckay_1959], and [NACA 1960][research_naca_1960], and the programme reviewed itself in [Weil 1962][research_weil_1962].

### Flight 91, Which Spent the Budget on Height

Walker took X-15-3 to 354,200 feet on 22 August 1963, with the engine at full thrust for 85.8 seconds and burnout near 176,000 feet. The aircraft then coasted 178,200 feet higher, which is a purely ballistic arc in which the controls that matter are the reaction jets.

Conserving the burnout energy through a drag-free coast leaves a horizontal speed at apogee of

$$V_{\text{apogee}} = \sqrt{2\left(e_{\text{burnout}} - g h_{\text{apogee}}\right)} = \sqrt{2\left(1.964 - 1.059\right) \times 10^{6}} = 1{,}346 \text{ m/s}$$

**so the aircraft was still moving at more than Mach 4 equivalent when it was at its highest and, in the ordinary sense, weightless.** The altitude record is not a hover at the top of a climb. It is the top of a very fast arc.

### Flight 188, Which Spent It on Speed and Nearly Lost the Aircraft

Knight took the X-15A-2 to Mach 6.70 on 3 October 1967 with external tanks and a full ablative coating, and with a dummy ramjet on the ventral pylon.

The flight is usually reported as a triumph and it was also very nearly a catastrophe. **The shock from the dummy ramjet impinged on the pylon and produced local heating far above anything the design contemplated**, burning through structure and causing the ramjet to separate. The aircraft landed and never flew again.

The sizing analysis above says why this was predictable in kind if not in detail. Shock impingement concentrates heating by focusing the flow, and the article's own heating relation shows that the rate is already twenty times what the structure could radiate at its design temperature **before any concentration is applied**. A vehicle operating at that margin has no tolerance for a local multiplier.

The phenomenon has a literature and it postdates the flight that met it. [Hung and Barnett 1973][research_hung_barnett_1973] analyses shockwave and boundary-layer interference heating directly, and [Kaufman and Johnson 1984][research_kaufman_johnson_1984] measures the heating distributions that trailing-edge controls induce, which is the same mechanism on a different protuberance. **The clean-body correlations the programme was designed around have nothing to say about any of it**, and this article's own use of one is subject to the same limitation.

[Graves 1969][research_graves_1969] reports the effect of the hypersonic research engine installation on the aircraft's aerodynamic characteristics, which is the nearest the primary record comes to treating the object that caused the damage as a design element rather than as a payload.

### Flight 3-65, Which Was Lost

On 15 November 1967, six weeks after the speed record, Michael Adams entered a hypersonic spin in X-15-3, recovered from it into an inverted dive, and broke up at about 60,000 feet under loads reported near 15 g normal and 8 g lateral. He was killed.

The accident is analysed at length in [Dennehy et al 2014][research_dennehy_2014], a modern reconstruction that had access to more analytical technique than the original investigation. **The proximate causes involve a control-system electrical disturbance, a display that showed sideslip on an instrument the pilot may have read as heading, and a drift in attitude that went uncorrected.** The article notes the finding and does not attempt to relitigate it.

What the accident says about the keystone is this. **The aircraft's energy had to be disposed of whatever attitude it was in**, and an attitude excursion at hypersonic speed converts a controlled deceleration into an uncontrolled one, with the loads and the heating arriving in the wrong places. The margin that a nominal trajectory maintains is not available off the nominal.

## Comparison With Ground Prediction

The X-15's most valuable output is arguably not any single measurement but the calibration of the ground facilities that produced its predictions.

### Heating

[Banner et al 1962][research_banner_1962] reports the first flight heating measurements, and the general finding across the programme was that **theory and tunnel over-predicted heating in some places and under-predicted it badly in others**, with the discrepancies concentrated where the flow was not what the simple correlations assume, which means at interference regions, at protuberances, and wherever boundary-layer transition occurred.

The article's own arithmetic reproduces this pattern in miniature. The Sutton and Graves correlation, applied to the clean stagnation point, lands within thirteen percent. **The same correlation says nothing whatever about a shock striking a pylon**, which is what nearly destroyed the aircraft.

### Aerodynamics

[Garringer and Saltzman 1966][research_garringer_saltzman_1966] summarises the full-scale lift and drag characteristics from Mach 0.63 to 6.0 and compares them with the wind-tunnel data that most nearly simulate flight. Its most directly useful result for the keystone is operational rather than aerodynamic. **Ninety-five percent of the maximum supersonic lift-to-drag ratio is available anywhere between about seven and twelve degrees of angle of attack**, so a pilot flying a near-optimum glide does not need to hold a precise attitude, only to stay inside a five-degree band.

That is the energy-management problem made tractable by a fact about the aerodynamics, and it is why the X-15 could be landed by a person rather than by a computer.

### Landing, Predicted on Another Aircraft

The unpowered approach was rehearsed before the X-15 flew. [Bray et al 1960][research_bray_1960] reports a flight study of a power-off landing technique applicable to re-entry vehicles, flown on a different aeroplane, and the technique it establishes is the one the X-15 used.

## What the Data Changed

### It Calibrated Hypersonic Prediction

The single most consequential output is a set of flight measurements against which every ground facility and every theory could be checked. **Before the X-15 there was no hypersonic flight data at all**, and after it there was a decade of it across a wide range of Mach number, altitude, and configuration.

### It Made the Hot Structure a Known Quantity, and Then Retired It

The X-15 demonstrated that a hot structure works. It also demonstrated the cost, which is that the structure is at its temperature limit at the design condition and has no margin for the local heating that real vehicles encounter. **The lesson taken forward was not the hot structure but the reason it was abandoned**, and the vehicle that followed used insulation and ablation instead.

### It Fed the Lifting Bodies and the Shuttle

The unpowered precision landing, the energy-management approach, and the pilot's ability to fly it are the X-15's most durable operational legacy. The lifting-body programme took the technique further and the Space Shuttle used it for thirty years.

### It Established That the Atmosphere Is the Instrument and the Adversary

The recurring result of the sizing analysis is that the atmosphere both enables and penalises, and the X-15 is the vehicle that measured the exchange rate.

Air is what the wings work against, what the control surfaces work against, and what the aircraft eventually stops in. Air is also what heats it, what takes half the energy of a zoom climb, and what destroyed the pylon on the fastest flight ever made. **The design problem is not to escape the atmosphere or to stay in it but to choose, at every instant, how much of it to be in**, and the choice is made by trajectory.

That is a framing the programme's own reports do not state in these words, and it is what the energy keystone is for.

### It Did Not Produce an Operational Aircraft

Nothing derived from the X-15 entered service. **That is not a failure and it is worth saying plainly**, because the aircraft was an instrument for producing data and it produced data, but a series that reports only what led somewhere would misrepresent what this aircraft was.

## The Contemporary Literature

The X-15's problem is live. Hypersonic flight is a subject of large current investment, and the questions are recognisably the same ones.

Modern work on hypersonic vehicle heating and thermal protection continues in [Zhai et al 2019][research_zhai_2019] on fault-tolerant attitude control with reaction control systems, [Liu et al 2020][research_liu_2020] on reentry attitude tracking with reaction control, and [Jiang et al 2020][research_jiang_2020] on precision analysis of hypersonic attitude control. **The reaction-control handover the X-15 flew by hand with a separate stick is now a control-allocation problem**, and the modern literature treats the blending as a solved matter of software.

[Ikeda and Takaku 2023][research_ikeda_takaku_2023] and [Ikeda and Takaku 2025][research_ikeda_takaku_2025] treat large-angle attitude manoeuvres by reaction control, and [Liu and Tan 2024][research_liu_tan_2024] incremental sliding-mode control for a fixed-wing vehicle, which is the same handover problem in another guise.

Thermal protection has moved decisively away from the hot structure the X-15 demonstrated. The state of the art at the end of the Shuttle era is surveyed in [Scotti 1992][research_scotti_1992] and [Goldstein 1993][research_goldstein_1993], and current work on reusable vehicles is [Aprovitola et al 2019][research_aprovitola_2019] on design integration, [Huang et al 2019][research_huang_2019] on coupled fluid and thermal analysis of non-ablative systems, [Huang and Yao 2019][research_huang_yao_2019] on adhesive failure, and [Chang et al 2022][research_chang_2022] on adjustable non-ablative concepts. **The direction of travel is toward systems that are neither purely rate-limited nor purely load-limited**, which is the trade this article's sizing analysis sets out and which the X-15 met at its two extremes.

Robust control for hypersonic vehicles, which is the modern form of the problem the MH-96 attacked by adaptation, is [Bu et al 2019][research_bu_2019] and [Chen et al 2019][research_chen_2019] on fault estimation with a degraded sensor set.

**What has not changed is the energy.** A hypersonic vehicle still carries kinetic energy comparable to the enthalpy that would destroy it, and the disposal of that energy is still the central design problem. The materials are better, the prediction is better, and the ratio is the same.

## Where the Framing Breaks Down

**The keystone was chosen and other choices were defensible.** An article organised around hypersonic stability and control would emphasise the wedge tail, the dampers, and the adaptive system, and would be a different and defensible article. The energy framing is offered as the one that makes the largest number of the aircraft's features follow from a single quantity, not as the only true account.

**The energy budget treats the aircraft as a point mass** and every real difficulty is a distribution problem. The heating that nearly destroyed Flight 188 was local, and no argument about total energy predicts where a shock will fall.

**The heating arithmetic uses one correlation and one assumed length scale.** It reproduces a reported temperature within thirteen percent, which is encouraging and is not a validation. Real hypersonic heating depends on boundary-layer state, and transition location is the largest single uncertainty in the whole subject.

**The comparison of the two records is not quite like with like.** Flight 188 was flown by a modified aircraft with external tanks, so the nineteen percent energy difference is a difference in vehicle as much as in trajectory.

**And the article says little about the pilots.** Twelve people flew this aircraft, one died, and the human account is a large part of what the X-15 was. This is a series about engineering and the omission is a choice rather than an oversight.

## What the X-15 Was Worth

The X-15 answered its question. A piloted aircraft could carry twice the energy needed to melt itself, dispose of all of it, and land, and it could do so 199 times.

**The more useful legacy is negative.** The programme established what a hot structure costs, that operating at a twenty-fold margin over the radiative capacity of the structure leaves no tolerance for local effects, and that the fastest flight ever made damaged the aircraft that made it. Those are the findings that shaped what came next, and they are findings a programme flying inside its margins would never have produced.

## The Designation, Which Is Ordinary and the Aircraft Which Is Not

The X-15 designation is unremarkable. It was assigned in sequence, to three aircraft of one type, and they kept it.

**What is remarkable is the discontinuity in the sequence.** The X-14 preceding it was a converted light aircraft hovering above a ramp at under 180 miles per hour. The X-15 following it flew at 4,520. Two consecutive designations span a factor of twenty-five in speed, and the designation system records no distinction between them at all.

## The Source Base

The X-15's primary record is unusually complete and unusually accessible. The programme's own conference reports, [NACA 1958][research_naca_1958] and [Beeler 1961][research_beeler_1961], are the closest thing to a contemporaneous synthesis, and [Weil 1962][research_weil_1962] is a mid-programme review.

The measurements this article relies on are [Garringer and Saltzman 1966][research_garringer_saltzman_1966] for lift and drag, [Banner et al 1962][research_banner_1962] for heating, [Saltzman 1961][research_saltzman_1961] for base pressures, and [Adkins and Jarvis 1964][research_adkins_jarvis_1964] for reaction-control operating experience.

One archive quirk is worth recording because a reader checking the citation will meet it. The lift and drag report's own cover reads "By Edwin J. Saltzman and Darwin J. Garringer", while the Technical Reports Server records the authors in the opposite order, and this article uses the archive's order because its citations are generated from archive metadata.

**Two limitations should be stated.** The article's heating numbers are computed rather than taken from the flight record, because the flight heating data are distributed across many reports and figures that did not survive text extraction. And the vehicle specifications come from secondary compilations, which agree with each other more than the sources for earlier articles in this series did, but are still secondary.

## Epistemic State

**Historical fact, from primary and secondary sources.** The 1954 origin, the tripartite arrangement, the three airframes, the XLR11 and XLR99 installations, the first glide flight on 8 June 1959, 199 flights ending 24 October 1968, twelve pilots, Flight 91 reaching 354,200 feet on 22 August 1963, Flight 188 reaching Mach 6.70 on 3 October 1967, and the loss of Adams on 15 November 1967.

**Engineering analysis, derived here and reproducible from the stated inputs.** The specific kinetic energy of 2.041 MJ/kg and its ratio of 2.26 to the melting enthalpy of the structure and 7.4 to the design-temperature enthalpy. The specific energies of the two records, 2.347 and 1.964 MJ/kg, and their ratio of 1.195. The 239.3 kilometre ideal zoom. The 89.9 percent of ideal delta-v. The heating rate of 64.8 W/cm², the radiative capacity of 3.28 W/cm² at the design temperature, and their ratio of 19.8. The radiative equilibrium of 3,040 degrees Fahrenheit against a reported 2,700. The dynamic pressure ratio above 4,000. The apogee horizontal speed of 1,346 m/s.

**A result that changed during the equation review, recorded because the first version was wrong.** The fraction of the vehicle's energy reaching its structure was first written on an assumed friction fraction of 35 percent of total drag, which gave about ten percent to the structure and a heat load exceeding the structure's absorptive capacity. Estimating the friction drag directly, from a turbulent flat-plate coefficient at the record Reynolds number over a plausible wetted area, gives 8 to 26 percent and about 15 centrally. **The corrected figure is four percent to the structure and a heat load of about half the absorptive capacity**, so the conclusion inverts. The corrected version is also the one consistent with the rest of the article, since a hot structure that is rate-limited should have load margin in hand, and the erroneous version contradicted that.

**Assumptions carried by the analysis.** The melting enthalpy uses representative values for a nickel superalloy rather than measured Inconel X data. The heating uses one correlation and an assumed effective nose radius of 0.0762 metres. The sensitivity is stated in the text and the conclusion survives doubling that radius. The atmosphere model is the 1976 standard table implemented to 84.852 km and clamped above, so dynamic pressures quoted above that height are upper bounds and the control argument is strengthened rather than weakened by the clamp. The emissivity of 0.8 is representative. The energy-partition analysis assumes the Reynolds analogy with a Prandtl number near unity, a turbulent recovery factor of 0.89, a wetted area near 113 square metres, a drag coefficient near 0.08, and a structural mass fraction of 60 percent of empty mass. The friction fraction is quoted as a range because those inputs are uncertain, and the conclusion that load margin exists holds across the whole range. The Newtonian trim angle of 13.8 degrees uses impact theory alone and takes no account of the fuselage or of real-gas effects. The launch condition of 13.7 kilometres at Mach 0.8 is representative rather than taken from any particular flight.

**Inference, stated as such.** That the two records are one budget differently partitioned is the article's framing rather than a claim any source makes. That the X-15A-2's ablative coating moved the vehicle from a rate-limited to a load-limited thermal regime is an inference from the nature of the two structures. That the reaction-control experience of the [X-14][related_post_a311_bell_x14] was available to the X-15's designers is plausible from the dates and is not documented here as a transfer.

**Claims the record does not settle.** The precise causal chain of the Adams accident, which [Dennehy et al 2014][research_dennehy_2014] reconstructs and which this article reports rather than adjudicates.

## Out of Scope

The X-15's experiment programme, which carried dozens of unrelated payloads, is not treated. The hypersonic research engine and the scramjet work it was meant to support are noted and not analysed. The delta-wing X-15 proposals and other unbuilt variants are omitted. The individual flight histories of the three airframes, the biographies of the pilots, and the programme's budget history are all out of scope. Boundary-layer transition, which is the largest uncertainty in hypersonic heating, is named and not developed.

## Conclusion

The X-15 was built to find out whether an aircraft could survive its own kinetic energy.

**At its record speed it carried 2.26 times the energy per kilogramme needed to melt its own structure, and asked that structure to reject nearly twenty times the heat it could radiate at its design temperature.** It survived by being blunt where it mattered, by being made of a material that stayed strong when hot, by flying trajectories chosen for their thermal properties as much as their performance, and by shedding energy over eleven minutes rather than one.

Its two records are one energy budget spent two ways, differing by nineteen percent in magnitude and completely in arrangement. Its worst day and its best were six weeks apart.

The next article takes up the [Bell X-16][ref_x16], a reconnaissance aircraft that was cancelled before it flew, and the contrast in what a designation can mean could hardly be sharper.

## References

### Books

[book_jenkins_landis_miller_2003]: https://openlibrary.org/search?q=Jenkins+Landis+Miller+American+X+Vehicles
[book_miller_2001]: https://openlibrary.org/search?q=Miller+The+X+Planes+X-1+to+X-45

### Reference

[ref_x15]: https://en.wikipedia.org/wiki/North_American_X-15
[ref_x16]: https://en.wikipedia.org/wiki/Bell_X-16

### Research

[research_adkins_jarvis_1964]: https://ntrs.nasa.gov/citations/19640010769
[research_adkins_taylor_1964]: https://ntrs.nasa.gov/citations/19640017347
[research_aprovitola_2019]: https://doi.org/10.1155/2019/6069528
[research_banner_1962]: https://ntrs.nasa.gov/citations/19660020178
[research_beeler_1961]: https://ntrs.nasa.gov/citations/19710070129
[research_berry_1967]: https://ntrs.nasa.gov/citations/20250007312
[research_bray_1960]: https://ntrs.nasa.gov/citations/19980223952
[research_bu_2019]: https://doi.org/10.1016/j.actaastro.2019.05.039
[research_bueche_1966]: https://doi.org/10.2514/6.1966-26
[research_chang_1966]: https://doi.org/10.2514/6.1966-410
[research_chang_2022]: https://doi.org/10.3390/aerospace10010001
[research_chen_2019]: https://doi.org/10.1002/rnc.4544
[research_christensen_dodgen_1961]: https://ntrs.nasa.gov/citations/19710070144
[research_colosimo_1968]: https://doi.org/10.2514/6.1968-380
[research_deem_murphy_1965]: https://doi.org/10.2514/6.1965-128
[research_dennehy_2014]: https://ntrs.nasa.gov/citations/20140013264
[research_diaconis_1959]: https://www.osti.gov/biblio/4079406
[research_duff_watson_1964]: https://doi.org/10.21236/ad0600872
[research_eggers_1958]: https://ntrs.nasa.gov/citations/19930085175
[research_finch_matranga_1959]: https://ntrs.nasa.gov/citations/19980236840
[research_furryy_1962]: https://doi.org/10.21236/ad0290357
[research_games_1954]: https://doi.org/10.21236/ad0035127
[research_garringer_saltzman_1966]: https://ntrs.nasa.gov/citations/19660010056
[research_goldstein_1993]: https://ntrs.nasa.gov/citations/19930012924
[research_graves_1969]: https://ntrs.nasa.gov/citations/19690029227
[research_greenewald_riley_1963]: https://doi.org/10.21236/ad0406873
[research_henderson_1967]: https://doi.org/10.2514/6.1967-130
[research_hendler_1964]: https://doi.org/10.21236/ad0609937
[research_hermann_1962]: https://ntrs.nasa.gov/citations/19630006112
[research_huang_2019]: https://doi.org/10.2514/1.a34212
[research_huang_yao_2019]: https://doi.org/10.2514/1.a34363
[research_hung_barnett_1973]: https://ntrs.nasa.gov/citations/19730032160
[research_ikeda_takaku_2023]: https://doi.org/10.1016/j.ifacol.2023.10.229
[research_ikeda_takaku_2025]: https://doi.org/10.1016/j.ifacol.2025.12.232
[research_jiang_2020]: https://doi.org/10.1080/21642583.2020.1747567
[research_kaufman_johnson_1984]: https://ntrs.nasa.gov/citations/19850014059
[research_larson_1968]: https://doi.org/10.2514/6.1968-40
[research_lipscomb_dodgen_1958]: https://ntrs.nasa.gov/citations/19930092393
[research_liu_2020]: https://doi.org/10.32604/cmes.2020.08124
[research_liu_tan_2024]: https://doi.org/10.3390/act13090371
[research_masaki_yakura_1968]: https://doi.org/10.2514/6.1968-1155
[research_mckay_1959]: https://ntrs.nasa.gov/citations/19980227362
[research_montgomery_1973]: https://ntrs.nasa.gov/citations/19740037345
[research_naca_1958]: https://ntrs.nasa.gov/citations/19930092380
[research_naca_1960]: https://ntrs.nasa.gov/citations/19980228350
[research_naca_1971]: https://ntrs.nasa.gov/citations/19710008947
[research_nonweiler_1959]: https://doi.org/10.1108/eb033176
[research_raeke_1958]: https://doi.org/10.4271/580153
[research_rosenbaum_1957]: https://doi.org/10.21236/ad0142149
[research_saltzman_1961]: https://ntrs.nasa.gov/citations/19980227195
[research_scotti_1992]: https://ntrs.nasa.gov/citations/19930003259
[research_sheetz_1965]: https://doi.org/10.2514/6.1965-127
[research_softley_1969]: https://doi.org/10.2514/6.1969-705
[research_steinbacher_young_1955]: https://doi.org/10.1115/1.4014492
[research_weil_1962]: https://ntrs.nasa.gov/citations/19620003289
[research_wiswell_1961]: https://ntrs.nasa.gov/citations/19710070148
[research_wolfe_1964]: https://doi.org/10.1016/b978-0-08-010580-2.50018-9
[research_zhai_2019]: https://doi.org/10.1016/j.isatra.2019.01.005

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
