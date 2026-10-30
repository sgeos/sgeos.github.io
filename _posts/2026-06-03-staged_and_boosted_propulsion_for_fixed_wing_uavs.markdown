---
layout: post
mathjax: true
comments: true
title:  "Staged and Boosted Propulsion for Small Fixed-Wing UAVs"
date:   2026-06-03 09:00:00 +0000
categories: aerospace engineering uav
series: fixed_wing_uav
series_title: Fixed-Wing UAV
series_index: 5
---
<!-- A120 -->
<script>console.log("A120");</script>

The propulsion article in this series sized a single sustained powerplant
and named the high-speed families, the ramjet, the scramjet, and the
rocket, as lying outside the regime of a small subsonic UAV.
A boost stage is what reopens them, and the cleanest way to think about a
boosted vehicle is as an energy budget.
When the boost burns out, the vehicle owns a fixed total of energy,
the sum of its potential energy from the altitude the boost reached,
its kinetic energy from the speed the boost gave it,
and the propulsive energy still stored aboard as fuel, battery, or unspent
propellant.
The mission, whatever it is, is paid out of that post-boost budget.
This article takes up staged and boosted propulsion for a small airframe on
the order of two meters in span, framed throughout as the management of that
budget.
How the boost deposits the energy, how the airframe holds it, and how the
mission spends it are the three questions,
and the configurations divide naturally into airframes that bank the budget
as altitude, airframes that spend it in a maneuvering descent, and airframes
that hold it level and top it up with propulsion.
A second constraint rides alongside, because the kinetic part of the budget
is a speed, and speed sets the stagnation temperature and therefore the
material the airframe must be built from.
The earlier articles on [the airframe][related_post_lwpla],
[the launch and recovery][related_post_launch], and
[the sustained propulsion][related_post_propulsion] supply the pieces this
one stages together.

## The Mission Energy Budget

When the boost burns out the vehicle holds a total mechanical energy of

$$
 E = \underbrace{m g h}_{\text{potential}} + \underbrace{\tfrac{1}{2} m V^2}_{\text{kinetic}}, 
\tag{1}
$$

to which is added the propulsive energy still stored aboard, the chemical or
electrical energy of any fuel, battery, or unspent propellant.
That sum is the mission budget, and every later choice is a way of filling
it and spending it.
It is convenient to carry the budget as an energy height,
$h_e = h + V^2 / 2g$, the altitude the vehicle would reach if all of its
[kinetic energy][ref_kinetic_energy] were traded for
[potential energy][ref_potential_energy],
which is the [energy-state idea][ref_em_theory] borrowed from fighter
performance.
The boost fills this account.
The [Tsiolkovsky rocket equation][ref_rocket_equation],

$$
 \Delta V = g_0\, I_{sp}\, \ln\!\frac{m_0}{m_f}, 
\tag{2}
$$

gives the velocity the boost delivers, and the angle of the boost decides
how that velocity is banked,
a near-vertical boost converting most of it into altitude and a flat boost
keeping most of it as speed.
Spending the budget is then the mission.
An unpowered glide spends potential and kinetic energy against drag,
a sustainer replenishes the account with propulsive energy as it goes,
and in every case drag is the tax that draws the account down at a rate of
drag times speed.
A single constraint rides on top of the budget.
The kinetic share is a speed, and that speed sets the
[stagnation temperature][ref_stagnation_temp] and the
[aerodynamic heating][ref_aero_heating] through
$T_0 / T_\infty = 1 + 0.2\,M^2$,
so the faster the vehicle holds its budget at low altitude the hotter its
skin runs and the more capable a material it demands.
The two-meter scale forbids none of this, because scale is not what fails at
high Mach number.
Material is what fails, and material is the thread this article follows.

## The Boost Stage

The boost is almost always a [solid-propellant rocket][ref_solid_rocket],
chosen for its simplicity, its storability, and its high thrust for a short
time, with a [specific impulse][ref_specific_impulse] around two hundred
fifty seconds.
Reading the rocket equation backward gives the propellant fraction needed to
reach a given speed.
To reach roughly Mach two at low altitude, near six hundred eighty meters
per second, a single solid stage spends about a quarter of the boosted mass
on propellant, and to reach Mach five it spends about half, before drag and
gravity losses are even counted.
Those losses are why a single stage runs out of margin and why a
[second stage][ref_multistage] earns its place.
A [multistage rocket][ref_multistage] sheds the dead mass of the first
motor before lighting the second, which raises the effective mass ratio and
reaches a takeover speed a single stage cannot.
The cost is the staging event itself, a separation that must be clean and
reliable, and a second set of structure and ignition that can fail.
For a two-meter vehicle the practical rule is that one stage suffices to
reach the ramjet regime and a second stage is what reaches the scramjet
regime.

## The Thermal Wall

The stagnation temperature climbs with the square of the Mach number,
so the thermal environment is mild in the subsonic regime and violent in
the hypersonic one.
At Mach two the stagnation temperature is a few hundred degrees Celsius,
at Mach three it is above five hundred,
and at Mach five it exceeds fourteen hundred at the stagnation point,
with the heat concentrated at the nose and the wing leading edges where the
shock stands closest to the surface.
Two facts soften the picture for a small boosted prototype.
The first is altitude, since the ambient temperature is lower high up and
the air is thinner, so a vehicle that flies its fast phase high sees a
gentler environment than the sea-level numbers suggest.
The second is duration, because a boosted dash lasts seconds to a minute
rather than hours, so a structure need only absorb a transient heat pulse
rather than reach thermal equilibrium,
which lets heat-sink mass and [ablative][ref_ablation] coatings carry a
short exposure that would defeat them in steady flight.
This is why the two-meter prototype is survivable where intuition says it
should melt.
It is not flying a sustained hypersonic cruise, it is surviving a brief
pulse, and the material need only be matched to that pulse.

## Airframe Materials by Regime

The material ladder follows the stagnation temperature directly.
In the subsonic regime the fiberglassed lightweight foaming PLA of the
airframe companion serves to about Mach zero point seven,
above which the heat and the loads exceed what the polymer and the resin
can bear.
In the transonic and low supersonic regime aluminum and elevated-temperature
carbon composites carry the structure.
In the supersonic ramjet regime, around Mach two to four,
the choice is aluminum for the briefest dashes,
[titanium][ref_titanium] and stainless steel for sustained flight, and a
ceramic or metallic leading edge,
the [SR-71][ref_sr71] being the standing example, a roughly ninety percent
titanium aircraft whose skin reached three hundred fifteen to four hundred
eighty degrees Celsius at Mach three above eighty thousand feet,
with its fuel circulated as a heat sink.
In the hypersonic scramjet regime, Mach five and beyond,
the structure turns to [nickel superalloys][ref_superalloy],
[refractory metals][ref_refractory],
[ceramic matrix composites][ref_cmc],
[reinforced carbon-carbon][ref_carbon_carbon] at the sharp leading edges,
[ultra-high-temperature ceramics][ref_uhtc] where the heating is worst,
and [regenerative or fuel cooling][ref_regen_cooling] of the most loaded
surfaces, with [ablative][ref_ablation] protection as the single-use
fallback.
The [X-43][ref_x43] and the [X-51][ref_x51] flew exactly this kind of
construction, carbon-carbon and refractory tiles over short scramjet bursts,
and a [survey of hypersonic materials][research_hypersonic_materials]
documents how thin the present margins still are.
A [thermal protection system][ref_thermal_protection] is therefore not an
accessory at these speeds but the primary structure's condition of survival.

## Airframe Archetypes for Spending the Budget

How an airframe holds and spends the energy budget sorts the designs into
three families.
The first banks the budget as altitude.
A vertical-fighter airframe boosts steeply, converting the boost velocity
into height in a [zoom climb][ref_zoom_climb] and holding the energy as
potential energy to be cashed later,
the historical instance being the [Bachem Natter][ref_ba349],
a vertical-takeoff rocket [interceptor][ref_interceptor] that reached twelve
kilometers in about a minute.
Such an airframe carries little wing and accepts high drag only briefly,
because its purpose is to arrive high with energy in hand rather than to
cruise, and at the small scale it is the shape of a boosted interceptor or a
vertically launched loitering munition.
The second family spends the budget in a controlled descent.
A maneuverable descending airframe trades its potential and kinetic energy
for range and maneuver on the way down, flying on lift rather than thrust,
and it wants a high lift-to-drag ratio to stretch the glide and enough
control authority to maneuver while it does.
The [lifting body][ref_lifting_body], the [waverider][ref_waverider] that
draws its lift from its own shock, the
[hypersonic glide vehicle][ref_hgv], and the
[maneuverable reentry vehicle][ref_marv] are all members of this family,
and a boosted two-meter glider is the accessible instance of it.
The third family is the conventional one.
It holds the budget roughly level at a chosen altitude and speed and tops it
up continuously with propulsive energy, replacing only what drag removes,
which is the cruise of a propeller, a turbine, or a ramjet and the regime
the propulsion companion sized in full.
The three families are not exclusive, because a single mission may boost
steeply, push over at altitude, and glide down,
but naming them makes the spending of the budget explicit rather than
incidental.

## Boost-Glide

The simplest staged configuration burns a booster and then flies no engine
at all.
A boost-glide vehicle trades all of its sustained propulsion for an
unpowered descent.
In budget terms its range is about the lift-to-drag ratio times the energy
height,

$$
 R \approx \frac{L}{D}\left(h + \frac{V^2}{2g}\right), 
\tag{3}
$$

so the glide turns the entire post-boost budget of potential and kinetic
energy into distance at a rate set by the airframe's efficiency,
which is exactly the lift-to-drag ratio the propulsion companion treated.
At modest speed this is the sounding-rocket glider, a booster lofting a
small airframe that then soars or glides home.
At high speed it becomes the [hypersonic glide vehicle][ref_hgv],
a body boosted to above Mach five that maneuvers through the upper
atmosphere on lift alone.
For a two-meter prototype the boost-glide profile is attractive because the
airframe carries no sustainer mass and the glide phase is unpowered,
so the entire propulsion budget is the booster,
and the thermal demand is set by the peak speed at the top of the boost
rather than by a sustained burn.

## Boost-Sustainer

A boost stage can hand off to one of the sustained powerplants of the
propulsion companion.
Boosting to flying speed and then cruising on a propeller or an electric
fan is simply rocket-assisted takeoff followed by ordinary cruise,
covered already in the launch and propulsion articles, and it keeps the
vehicle subsonic so the airframe companion's materials still serve.
Boosting and then sustaining on a turbojet is the classic
[cruise-missile][ref_cruise_missile] pattern, a jettisoned solid booster
that brings the vehicle to the speed where the turbine is efficient,
after which the turbine carries the cruise.
This pairing keeps the speed high subsonic to low supersonic,
so the airframe rises from foam and glass to aluminum or composite but does
not yet need the exotic materials of the faster regimes.

## Boost-Ramjet

The boost-ramjet is the configuration that most rewards staging,
because a [ramjet][ref_ramjet] makes no static thrust and cannot start from
rest, so it requires a boost to its working speed near Mach two before it
produces any thrust at all.
The standing example at a relatable scale is the
[GQM-163 Coyote][ref_gqm163], a supersonic target about five and a half
meters long that is launched by a solid booster and then sustained by a
ducted-rocket ramjet to about Mach two point eight at sea level.
A two-meter vehicle is a smaller instance of the same architecture,
a solid boost to the takeover speed followed by ramjet sustain,
and at Mach two to three its airframe is the titanium and steel of the
supersonic regime rather than foam and glass.
The integral arrangement, in which the spent booster case becomes the
ramjet combustion chamber, is the compact way to package this and is the
reason such vehicles look like a single tube rather than two stacked stages.
The boost-ramjet is buildable at two meters, demanding but conventional in
its materials, and it is the natural high-speed endpoint for a prototype
that must sustain rather than merely dash.

## Boost-Scramjet

The boost-scramjet pushes into the hypersonic regime,
where a [scramjet][ref_scramjet] burns its fuel in a supersonic internal
flow and only functions above roughly Mach five.
Reaching that takeover speed is itself a major rocket task,
which is why the flown examples were air-launched and rocket-boosted,
the [X-43][ref_x43] carried aloft and accelerated by a Pegasus-derived
booster to about Mach ten for a ten-second burn,
and the [X-51][ref_x51] boosted and then sustained for several minutes.
A two-meter scramjet vehicle is physically possible and has effectively been
flown at similar scales, but it is a research undertaking rather than a shop
build, because the boost to Mach five is large relative to the vehicle,
the inlet and supersonic combustor must be integrated and cooled,
and the airframe needs the [hypersonic][ref_hypersonic] material set,
carbon-carbon and ceramic matrix composites and active cooling,
with ablative protection where nothing else survives.
The honest summary is that the scale is not the obstacle and the materials
are known, but the budget, the instrumentation, and the boost stage are all
substantial, so this is the configuration that consumes a real program
rather than a hobby season.

## Boost-Throttleable Rocket

A boost stage can also hand off to a sustained rocket,
a [throttleable rocket engine][ref_rocket_engine] of liquid or hybrid type
that continues to thrust after the solid booster is spent.
Because a rocket carries its own oxidizer, this configuration reaches very
high speed and altitude at the cost of poor endurance,
so it suits a brief high-speed dash, a high-altitude zoom, or a
near-space sounding profile rather than sustained flight.
At the two-meter scale the hybrid rocket is the accessible form,
since student and amateur hybrid motors are well within reach,
which makes a boost-then-throttleable-hybrid prototype more buildable than a
scramjet even though it buys speed rather than range.
Its airframe demand follows the same thermal ladder, set by whatever peak
Mach number the rocket sustainer reaches.

## One Stage Versus Two

The choice between one stage and two is a choice of how much takeover speed
is needed.
A single boost stage reaches the ramjet regime comfortably and the lower
hypersonic edge with difficulty.
A second stage exists to reach beyond that, because shedding the first
motor's dead mass before igniting the second raises the effective mass ratio
and buys the extra velocity that a single stage cannot.
The same logic decides the boost for a scramjet,
which usually wants a second stage or a large first stage simply to arrive
at the speed where the engine lights.
The penalty is the staging event, a separation and a second ignition that
add two more ways to fail,
so the rule is to use one stage where one stage reaches the regime and to
accept the complexity of two only when the target speed demands it.

## Putting Numbers to It

A worked example threads the two master variables together for a two-meter
vehicle.
A single solid booster of specific impulse two hundred fifty seconds has an
effective exhaust velocity of about two thousand four hundred fifty meters
per second.
To reach Mach two near the ground, about six hundred eighty meters per
second, the rocket equation gives a mass ratio of
$\exp(680 / 2450) \approx 1.32$,
so about twenty-four percent of the boosted mass is propellant,
and the stagnation temperature at Mach two is about
$1.8 \times 288 \approx 518$ kelvin, near two hundred forty-five degrees
Celsius, which a titanium or even a brief aluminum structure can take.
To reach Mach five, about seventeen hundred meters per second, the mass
ratio is $\exp(1700 / 2450) \approx 2.0$,
so roughly half the boosted mass is propellant before losses,
and the stagnation temperature is about
$6 \times 288 \approx 1728$ kelvin, over fourteen hundred degrees Celsius,
which demands carbon-carbon, ceramic matrix composites, and active or
ablative cooling.
That Mach five speed is also a large energy budget in its own right,
since its kinetic energy corresponds to an energy height of
$V^2 / 2g \approx 147$ kilometers, the altitude the speed could in principle
be traded for, which is why a boosted hypersonic glider ranges so far on no
propulsion at all.
The contrast is the whole article in two numbers.
The same two-meter airframe can be boosted to Mach two on a quarter of its
mass in propellant and built of titanium,
or boosted to Mach five on half its mass in propellant and built of
ceramics and refractory metals,
and the leap between those two columns is paid in propellant fraction and in
material, not in size.

## Out of Scope

Several neighboring subjects are deliberately excluded.
The internal ballistics of the solid booster, the grain design, the nozzle,
and the propellant chemistry are a discipline of their own,
and this article treats a booster only through its specific impulse and
mass ratio.
The internal aerodynamics of the ramjet and the scramjet, the inlet, the
isolator, and the supersonic combustor, are named but not designed here.
The detailed design of the thermal protection system, the tile sizing, the
coating chemistry, and the active-cooling plumbing, is beyond this scope,
as is the structural analysis of a supersonic or hypersonic airframe.
The guidance, navigation, and control of a boosted vehicle through staging
and high-speed flight, the trajectory optimization that allocates the energy
budget across the mission, the recovery of the airframe afterward, and the
range-safety and regulatory approvals for supersonic and hypersonic flight
are each left to their own treatments.
And the sustained subsonic propulsion the boost hands off to is covered in
the propulsion companion and is not repeated.

## Conclusion

Staged and boosted propulsion turns one small airframe into many vehicles,
and the unifying idea is the post-boost energy budget.
A boost governed by the rocket equation deposits a total of potential and
kinetic energy, to which the stored propulsive energy is added,
and the mission is whatever that budget can buy.
An airframe banks the budget as altitude, spends it in a maneuvering
descent, or holds it level and tops it up with propulsion,
and the kinetic share sets the stagnation temperature, and therefore the
material, through the square of the Mach number.
Choose how to fill the budget and how to spend it, and the configuration
follows,
a boost-glide that carries no engine, a boost-sustainer that cruises on a
propeller or a turbine, a boost-ramjet that sustains at supersonic speed on
a titanium airframe, a boost-scramjet that dashes hypersonic on ceramics,
or a boost-rocket that trades endurance for speed.
The two-meter scale forbids none of these.
It is the budget and the material, not the size, that decide how far up the
speed ladder a given prototype can be carried,
and a builder who states the takeover speed can read off both the propellant
fraction and the airframe material with numbers rather than guesswork.

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 3 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 3, 2 are established and 1 are bespoke.
Quantities are in SI units, with energy in joules, altitude in metres and speed in metres per second, and the specific impulse is in seconds so that it is multiplied by standard gravity to give an exhaust velocity.

**Equation 1, Mechanical Energy at Burnout.**
The mechanical energy held at burnout is the sum of the gravitational potential energy and the kinetic energy of the vehicle.
[potential energy][ref_potential_energy]
[kinetic energy][ref_kinetic_energy]

$$
 E = \underbrace{m g h}_{\text{potential}} + \underbrace{\tfrac{1}{2} m V^2}_{\text{kinetic}}, 
\tag{1}
$$

**Equation 2, Tsiolkovsky Rocket Equation.**
The velocity a boost delivers is the effective exhaust velocity multiplied by the natural logarithm of the ratio of initial to final mass.
[Tsiolkovsky rocket equation][ref_rocket_equation]

$$
 \Delta V = g_0\, I_{sp}\, \ln\!\frac{m_0}{m_f}, 
\tag{2}
$$

*Equation 3, Bespoke Boost-Glide Range from Energy Height.*
The glide range is taken as the lift-to-drag ratio times the energy height, which assumes that the whole post-boost potential and kinetic energy is spent in a glide at one constant lift-to-drag ratio.

$$
 R \approx \frac{L}{D}\left(h + \frac{V^2}{2g}\right), 
\tag{3}
$$

### Notation

- $E$, the mechanical energy at burnout
- $h$, the altitude
- $V$, the speed
- $I_{sp}$, the specific impulse in seconds
- $g_0$, standard gravity, 9.80665 metres per second squared
- $m_0$, the initial mass
- $m_f$, the final mass after the burn
- $R$, the glide range
- $\frac{L}{D}$, the lift-to-drag ratio

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- Peters, Adam B., Dajie Zhang, Samuel Chen, et al. 2024. "Materials Design for Hypersonics." *Nature Communications* 15 (1): 3328. [https://doi.org/10.1038/s41467-024-46753-3][research_hypersonic_materials]

### Tertiary Sources

- "Ablation." 2026. Wikipedia. Last modified May 1, at 23:15 (UTC). [https://en.wikipedia.org/w/index.php?title=Ablation&oldid=1352085846][ref_ablation]
- "Aerodynamic Heating." 2024. Wikipedia. Last modified November 4, at 21:55 (UTC). [https://en.wikipedia.org/w/index.php?title=Aerodynamic\_heating&oldid=1255423677][ref_aero_heating]
- "Atmospheric Entry." 2026. Wikipedia. Last modified May 22, at 07:25 (UTC). [https://en.wikipedia.org/w/index.php?title=Atmospheric\_entry&oldid=1355508904][ref_thermal_protection]
- "Bachem Ba 349 Natter." 2026. Wikipedia. Last modified May 12, at 23:47 (UTC). [https://en.wikipedia.org/w/index.php?title=Bachem\_Ba\_349\_Natter&oldid=1353882093][ref_ba349]
- "Boeing X-51 Waverider." 2025. Wikipedia. Last modified April 5, at 07:29 (UTC). [https://en.wikipedia.org/w/index.php?title=Boeing\_X-51\_Waverider&oldid=1284050871][ref_x51]
- "Boost-Glide." 2026. Wikipedia. Last modified May 4, at 07:19 (UTC). [https://en.wikipedia.org/w/index.php?title=Boost-glide&oldid=1352449733][ref_boost_glide]
- "Ceramic Matrix Composite." 2025. Wikipedia. Last modified November 26, at 17:40 (UTC). [https://en.wikipedia.org/w/index.php?title=Ceramic\_matrix\_composite&oldid=1324274145][ref_cmc]
- "Cruise Missile." 2026. Wikipedia. Last modified May 25, at 13:53 (UTC). [https://en.wikipedia.org/w/index.php?title=Cruise\_missile&oldid=1356057387][ref_cruise_missile]
- "Energy–maneuverability Theory." 2026. Wikipedia. Last modified February 10, at 13:02 (UTC). [https://en.wikipedia.org/w/index.php?title=Energy%E2%80%93maneuverability\_theory&oldid=1337603045][ref_em_theory]
- "GQM-163 Coyote." 2025. Wikipedia. Last modified October 27, at 04:39 (UTC). [https://en.wikipedia.org/w/index.php?title=GQM-163\_Coyote&oldid=1318991312][ref_gqm163]
- "Hypersonic Glide Vehicle." 2026. Wikipedia. Last modified May 31, at 01:11 (UTC). [https://en.wikipedia.org/w/index.php?title=Hypersonic\_glide\_vehicle&oldid=1356977266][ref_hgv]
- "Hypersonic Speed." 2026. Wikipedia. Last modified April 12, at 17:45 (UTC). [https://en.wikipedia.org/w/index.php?title=Hypersonic\_speed&oldid=1348438749][ref_hypersonic]
- "Interceptor Aircraft." 2026. Wikipedia. Last modified February 22, at 06:24 (UTC). [https://en.wikipedia.org/w/index.php?title=Interceptor\_aircraft&oldid=1339767826][ref_interceptor]
- "Kinetic Energy." 2026. Wikipedia. Last modified April 30, at 15:06 (UTC). [https://en.wikipedia.org/w/index.php?title=Kinetic\_energy&oldid=1351851317][ref_kinetic_energy]
- "Lifting Body." 2026. Wikipedia. Last modified May 23, at 23:31 (UTC). [https://en.wikipedia.org/w/index.php?title=Lifting\_body&oldid=1355792687][ref_lifting_body]
- "Lockheed SR-71 Blackbird." 2026. Wikipedia. Last modified May 28, at 18:01 (UTC). [https://en.wikipedia.org/w/index.php?title=Lockheed\_SR-71\_Blackbird&oldid=1356586918][ref_sr71]
- "Maneuverable Reentry Vehicle." 2026. Wikipedia. Last modified May 23, at 18:16 (UTC). [https://en.wikipedia.org/w/index.php?title=Maneuverable\_reentry\_vehicle&oldid=1355748110][ref_marv]
- "Multistage Rocket." 2026. Wikipedia. Last modified May 17, at 17:22 (UTC). [https://en.wikipedia.org/w/index.php?title=Multistage\_rocket&oldid=1354660731][ref_multistage]
- "NASA X-43." 2026. Wikipedia. Last modified May 14, at 16:31 (UTC). [https://en.wikipedia.org/w/index.php?title=NASA\_X-43&oldid=1354148087][ref_x43]
- "Potential Energy." 2026. Wikipedia. Last modified May 29, at 14:21 (UTC). [https://en.wikipedia.org/w/index.php?title=Potential\_energy&oldid=1356733354][ref_potential_energy]
- "Ramjet." 2026. Wikipedia. Last modified May 10, at 15:40 (UTC). [https://en.wikipedia.org/w/index.php?title=Ramjet&oldid=1353487326][ref_ramjet]
- "Refractory Metals." 2025. Wikipedia. Last modified December 26, at 18:06 (UTC). [https://en.wikipedia.org/w/index.php?title=Refractory\_metals&oldid=1329545026][ref_refractory]
- "Regenerative Cooling (Rocketry)." 2026. Wikipedia. Last modified April 12, at 17:38 (UTC). [https://en.wikipedia.org/w/index.php?title=Regenerative\_cooling\_(rocketry)&oldid=1348437664][ref_regen_cooling]
- "Reinforced Carbon–carbon." 2026. Wikipedia. Last modified May 27, at 16:54 (UTC). [https://en.wikipedia.org/w/index.php?title=Reinforced\_carbon%E2%80%93carbon&oldid=1356416786][ref_carbon_carbon]
- "Rocket Engine." 2026. Wikipedia. Last modified May 25, at 14:02 (UTC). [https://en.wikipedia.org/w/index.php?title=Rocket\_engine&oldid=1356058584][ref_rocket_engine]
- "Scramjet." 2026. Wikipedia. Last modified March 25, at 14:02 (UTC). [https://en.wikipedia.org/w/index.php?title=Scramjet&oldid=1345319324][ref_scramjet]
- "Solid-Propellant Rocket." 2026. Wikipedia. Last modified April 6, at 00:06 (UTC). [https://en.wikipedia.org/w/index.php?title=Solid-propellant\_rocket&oldid=1347314567][ref_solid_rocket]
- "Specific Impulse." 2026. Wikipedia. Last modified May 21, at 09:35 (UTC). [https://en.wikipedia.org/w/index.php?title=Specific\_impulse&oldid=1355346239][ref_specific_impulse]
- "Stagnation Temperature." 2025. Wikipedia. Last modified March 15, at 22:24 (UTC). [https://en.wikipedia.org/w/index.php?title=Stagnation\_temperature&oldid=1280690173][ref_stagnation_temp]
- "Superalloy." 2026. Wikipedia. Last modified May 8, at 01:16 (UTC). [https://en.wikipedia.org/w/index.php?title=Superalloy&oldid=1353077196][ref_superalloy]
- "Titanium." 2026. Wikipedia. Last modified May 28, at 12:11 (UTC). [https://en.wikipedia.org/w/index.php?title=Titanium&oldid=1356544924][ref_titanium]
- "Tsiolkovsky Rocket Equation." 2026. Wikipedia. Last modified May 17, at 01:07 (UTC). [https://en.wikipedia.org/w/index.php?title=Tsiolkovsky\_rocket\_equation&oldid=1354537333][ref_rocket_equation]
- "Ultra-High Temperature Ceramic." 2026. Wikipedia. Last modified May 27, at 20:51 (UTC). [https://en.wikipedia.org/w/index.php?title=Ultra-high\_temperature\_ceramic&oldid=1356450427][ref_uhtc]
- "Waverider." 2025. Wikipedia. Last modified September 16, at 02:42 (UTC). [https://en.wikipedia.org/w/index.php?title=Waverider&oldid=1311620728][ref_waverider]
- "Zoom Climb." 2026. Wikipedia. Last modified February 27, at 13:18 (UTC). [https://en.wikipedia.org/w/index.php?title=Zoom\_climb&oldid=1340755341][ref_zoom_climb]

### Related Posts

- Sechter, Brendan. 2026. "Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass." *Brendan A R Sechter's Development Blog*, May 30. [https://sgeos.github.io/aerospace/engineering/3d-printing/2026/05/30/prototyping\_fixed\_wing\_aircraft\_with\_lightweight\_pla\_and\_fiberglass.html][related_post_lwpla]
- Sechter, Brendan. 2026. "Runway Sizing for Fixed-Wing UAVs." *Brendan A R Sechter's Development Blog*, May 31. [https://sgeos.github.io/aerospace/engineering/uav/2026/05/31/runway\_sizing\_for\_fixed\_wing\_uavs.html][related_post_runway]
- Sechter, Brendan. 2026. "Launch and Recovery Systems for Fixed-Wing UAVs." *Brendan A R Sechter's Development Blog*, June 1. [https://sgeos.github.io/aerospace/engineering/uav/2026/06/01/launch\_and\_recovery\_systems\_for\_fixed\_wing\_uavs.html][related_post_launch]
- Sechter, Brendan. 2026. "Propulsion and Power Sizing for Small Fixed-Wing UAVs." *Brendan A R Sechter's Development Blog*, June 2. [https://sgeos.github.io/aerospace/engineering/uav/2026/06/02/propulsion\_and\_power\_sizing\_for\_fixed\_wing\_uavs.html][related_post_propulsion]

[ref_ablation]: https://en.wikipedia.org/w/index.php?title=Ablation&oldid=1352085846
[ref_aero_heating]: https://en.wikipedia.org/w/index.php?title=Aerodynamic_heating&oldid=1255423677
[ref_ba349]: https://en.wikipedia.org/w/index.php?title=Bachem_Ba_349_Natter&oldid=1353882093
[ref_boost_glide]: https://en.wikipedia.org/w/index.php?title=Boost-glide&oldid=1352449733
[ref_carbon_carbon]: https://en.wikipedia.org/w/index.php?title=Reinforced_carbon%E2%80%93carbon&oldid=1356416786
[ref_cmc]: https://en.wikipedia.org/w/index.php?title=Ceramic_matrix_composite&oldid=1324274145
[ref_cruise_missile]: https://en.wikipedia.org/w/index.php?title=Cruise_missile&oldid=1356057387
[ref_em_theory]: https://en.wikipedia.org/w/index.php?title=Energy%E2%80%93maneuverability_theory&oldid=1337603045
[ref_gqm163]: https://en.wikipedia.org/w/index.php?title=GQM-163_Coyote&oldid=1318991312
[ref_hgv]: https://en.wikipedia.org/w/index.php?title=Hypersonic_glide_vehicle&oldid=1356977266
[ref_hypersonic]: https://en.wikipedia.org/w/index.php?title=Hypersonic_speed&oldid=1348438749
[ref_interceptor]: https://en.wikipedia.org/w/index.php?title=Interceptor_aircraft&oldid=1339767826
[ref_kinetic_energy]: https://en.wikipedia.org/w/index.php?title=Kinetic_energy&oldid=1351851317
[ref_lifting_body]: https://en.wikipedia.org/w/index.php?title=Lifting_body&oldid=1355792687
[ref_marv]: https://en.wikipedia.org/w/index.php?title=Maneuverable_reentry_vehicle&oldid=1355748110
[ref_multistage]: https://en.wikipedia.org/w/index.php?title=Multistage_rocket&oldid=1354660731
[ref_potential_energy]: https://en.wikipedia.org/w/index.php?title=Potential_energy&oldid=1356733354
[ref_ramjet]: https://en.wikipedia.org/w/index.php?title=Ramjet&oldid=1353487326
[ref_refractory]: https://en.wikipedia.org/w/index.php?title=Refractory_metals&oldid=1329545026
[ref_regen_cooling]: https://en.wikipedia.org/w/index.php?title=Regenerative_cooling_(rocketry)&oldid=1348437664
[ref_rocket_engine]: https://en.wikipedia.org/w/index.php?title=Rocket_engine&oldid=1356058584
[ref_rocket_equation]: https://en.wikipedia.org/w/index.php?title=Tsiolkovsky_rocket_equation&oldid=1354537333
[ref_scramjet]: https://en.wikipedia.org/w/index.php?title=Scramjet&oldid=1345319324
[ref_solid_rocket]: https://en.wikipedia.org/w/index.php?title=Solid-propellant_rocket&oldid=1347314567
[ref_specific_impulse]: https://en.wikipedia.org/w/index.php?title=Specific_impulse&oldid=1355346239
[ref_sr71]: https://en.wikipedia.org/w/index.php?title=Lockheed_SR-71_Blackbird&oldid=1356586918
[ref_stagnation_temp]: https://en.wikipedia.org/w/index.php?title=Stagnation_temperature&oldid=1280690173
[ref_superalloy]: https://en.wikipedia.org/w/index.php?title=Superalloy&oldid=1353077196
[ref_thermal_protection]: https://en.wikipedia.org/w/index.php?title=Atmospheric_entry&oldid=1355508904
[ref_titanium]: https://en.wikipedia.org/w/index.php?title=Titanium&oldid=1356544924
[ref_uhtc]: https://en.wikipedia.org/w/index.php?title=Ultra-high_temperature_ceramic&oldid=1356450427
[ref_waverider]: https://en.wikipedia.org/w/index.php?title=Waverider&oldid=1311620728
[ref_x43]: https://en.wikipedia.org/w/index.php?title=NASA_X-43&oldid=1354148087
[ref_x51]: https://en.wikipedia.org/w/index.php?title=Boeing_X-51_Waverider&oldid=1284050871
[ref_zoom_climb]: https://en.wikipedia.org/w/index.php?title=Zoom_climb&oldid=1340755341
[related_post_launch]: {% post_url 2026-06-01-launch_and_recovery_systems_for_fixed_wing_uavs %}
[related_post_lwpla]: {% post_url 2026-05-30-prototyping_fixed_wing_aircraft_with_lightweight_pla_and_fiberglass %}
[related_post_propulsion]: {% post_url 2026-06-02-propulsion_and_power_sizing_for_fixed_wing_uavs %}
[related_post_runway]: {% post_url 2026-05-31-runway_sizing_for_fixed_wing_uavs %}
[research_hypersonic_materials]: https://doi.org/10.1038/s41467-024-46753-3
