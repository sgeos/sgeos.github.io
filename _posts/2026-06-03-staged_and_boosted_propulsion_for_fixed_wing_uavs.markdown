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

$$ E = \underbrace{m g h}_{\text{potential}} + \underbrace{\tfrac{1}{2} m V^2}_{\text{kinetic}}, $$

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

$$ \Delta V = g_0\, I_{sp}\, \ln\!\frac{m_0}{m_f}, $$

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

$$ R \approx \frac{L}{D}\left(h + \frac{V^2}{2g}\right), $$

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

## References

- [Reference, Ablation][ref_ablation]
- [Reference, Aerodynamic Heating][ref_aero_heating]
- [Reference, Bachem Ba 349 Natter][ref_ba349]
- [Reference, Boost-Glide][ref_boost_glide]
- [Reference, Ceramic Matrix Composite][ref_cmc]
- [Reference, Cruise Missile][ref_cruise_missile]
- [Reference, Energy-Maneuverability Theory][ref_em_theory]
- [Reference, GQM-163 Coyote][ref_gqm163]
- [Reference, Hypersonic Glide Vehicle][ref_hgv]
- [Reference, Hypersonic Speed][ref_hypersonic]
- [Reference, Interceptor Aircraft][ref_interceptor]
- [Reference, Kinetic Energy][ref_kinetic_energy]
- [Reference, Lifting Body][ref_lifting_body]
- [Reference, Lockheed SR-71 Blackbird][ref_sr71]
- [Reference, Maneuverable Reentry Vehicle][ref_marv]
- [Reference, Multistage Rocket][ref_multistage]
- [Reference, NASA X-43][ref_x43]
- [Reference, Potential Energy][ref_potential_energy]
- [Reference, Ramjet][ref_ramjet]
- [Reference, Refractory Metals][ref_refractory]
- [Reference, Regenerative Cooling in Rockets][ref_regen_cooling]
- [Reference, Reinforced Carbon-Carbon][ref_carbon_carbon]
- [Reference, Rocket Engine][ref_rocket_engine]
- [Reference, Scramjet][ref_scramjet]
- [Reference, Solid-Propellant Rocket][ref_solid_rocket]
- [Reference, Specific Impulse][ref_specific_impulse]
- [Reference, Stagnation Temperature][ref_stagnation_temp]
- [Reference, Superalloy][ref_superalloy]
- [Reference, Thermal Protection System][ref_thermal_protection]
- [Reference, Titanium][ref_titanium]
- [Reference, Tsiolkovsky Rocket Equation][ref_rocket_equation]
- [Reference, Ultra-High-Temperature Ceramics][ref_uhtc]
- [Reference, Waverider][ref_waverider]
- [Reference, X-51 Waverider][ref_x51]
- [Reference, Zoom Climb][ref_zoom_climb]
- [Related Post, Launch and Recovery Systems for Fixed-Wing UAVs][related_post_launch]
- [Related Post, Propulsion and Power Sizing for Small Fixed-Wing UAVs][related_post_propulsion]
- [Related Post, Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass][related_post_lwpla]
- [Related Post, Runway Sizing for Fixed-Wing UAVs][related_post_runway]
- [Research, Materials Design for Hypersonics (Nature Communications)][research_hypersonic_materials]

[ref_ablation]: https://en.wikipedia.org/wiki/Ablation
[ref_aero_heating]: https://en.wikipedia.org/wiki/Aerodynamic_heating
[ref_ba349]: https://en.wikipedia.org/wiki/Bachem_Ba_349_Natter
[ref_boost_glide]: https://en.wikipedia.org/wiki/Boost-glide
[ref_carbon_carbon]: https://en.wikipedia.org/wiki/Reinforced_carbon%E2%80%93carbon
[ref_cmc]: https://en.wikipedia.org/wiki/Ceramic_matrix_composite
[ref_cruise_missile]: https://en.wikipedia.org/wiki/Cruise_missile
[ref_em_theory]: https://en.wikipedia.org/wiki/Energy%E2%80%93maneuverability_theory
[ref_gqm163]: https://en.wikipedia.org/wiki/GQM-163_Coyote
[ref_hgv]: https://en.wikipedia.org/wiki/Hypersonic_glide_vehicle
[ref_hypersonic]: https://en.wikipedia.org/wiki/Hypersonic_speed
[ref_interceptor]: https://en.wikipedia.org/wiki/Interceptor_aircraft
[ref_kinetic_energy]: https://en.wikipedia.org/wiki/Kinetic_energy
[ref_lifting_body]: https://en.wikipedia.org/wiki/Lifting_body
[ref_marv]: https://en.wikipedia.org/wiki/Maneuverable_reentry_vehicle
[ref_multistage]: https://en.wikipedia.org/wiki/Multistage_rocket
[ref_potential_energy]: https://en.wikipedia.org/wiki/Potential_energy
[ref_ramjet]: https://en.wikipedia.org/wiki/Ramjet
[ref_refractory]: https://en.wikipedia.org/wiki/Refractory_metals
[ref_regen_cooling]: https://en.wikipedia.org/wiki/Regenerative_cooling_(rocket)
[ref_rocket_engine]: https://en.wikipedia.org/wiki/Rocket_engine
[ref_rocket_equation]: https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation
[ref_scramjet]: https://en.wikipedia.org/wiki/Scramjet
[ref_solid_rocket]: https://en.wikipedia.org/wiki/Solid-propellant_rocket
[ref_specific_impulse]: https://en.wikipedia.org/wiki/Specific_impulse
[ref_sr71]: https://en.wikipedia.org/wiki/Lockheed_SR-71_Blackbird
[ref_stagnation_temp]: https://en.wikipedia.org/wiki/Stagnation_temperature
[ref_superalloy]: https://en.wikipedia.org/wiki/Superalloy
[ref_thermal_protection]: https://en.wikipedia.org/wiki/Thermal_protection_system
[ref_titanium]: https://en.wikipedia.org/wiki/Titanium
[ref_uhtc]: https://en.wikipedia.org/wiki/Ultra-high-temperature_ceramics
[ref_waverider]: https://en.wikipedia.org/wiki/Waverider
[ref_x43]: https://en.wikipedia.org/wiki/NASA_X-43
[ref_x51]: https://en.wikipedia.org/wiki/Boeing_X-51_Waverider
[ref_zoom_climb]: https://en.wikipedia.org/wiki/Zoom_climb
[related_post_launch]: {% post_url 2026-06-01-launch_and_recovery_systems_for_fixed_wing_uavs %}
[related_post_lwpla]: {% post_url 2026-05-30-prototyping_fixed_wing_aircraft_with_lightweight_pla_and_fiberglass %}
[related_post_propulsion]: {% post_url 2026-06-02-propulsion_and_power_sizing_for_fixed_wing_uavs %}
[related_post_runway]: {% post_url 2026-05-31-runway_sizing_for_fixed_wing_uavs %}
[research_hypersonic_materials]: https://www.nature.com/articles/s41467-024-46753-3
