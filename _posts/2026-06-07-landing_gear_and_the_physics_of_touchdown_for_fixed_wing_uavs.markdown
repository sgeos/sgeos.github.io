---
layout: post
mathjax: true
comments: true
title:  "Landing Gear and the Physics of Touchdown for Fixed-Wing UAVs"
date:   2026-06-07 09:00:00 +0000
categories: aerospace engineering uav
---

<!-- A124 -->
<script>console.log("A124");</script>

The runway article in this series sized the ground roll, and the launch and
recovery article catalogued the devices that catch an aircraft out of the
air.
This article takes up what happens at the surface itself,
the landing gear and the other interfaces that meet the ground or the water,
and the way the last of the aircraft's energy is absorbed there.
One quantity organizes it, the energy the aircraft still carries at
touchdown, because a landing is the act of dissipating that energy into the
structure and the surface over whatever distance the interface provides.
The deceleration, and therefore the load the airframe and the payload must
survive, is that energy divided by the stroke,
the same relation the recovery article used to size a catapult or a net,
now applied to the wheel, the skid, the hull, the canopy, and the crushable
nose.
A second quantity sits upstream, the energy bled away before touchdown,
which decides how much arrives at the interface in the first place.
This piece builds on the [runway companion][related_post_runway] for the
ground roll, the [launch and recovery companion][related_post_launch] for
the recovery devices it complements rather than repeats, and the
[control companion][related_post_static] for the surfaces that bleed energy
on the approach.

## The Touchdown Energy and the Stroke

At the moment of touchdown the aircraft carries kinetic energy in two
directions, a horizontal part from its forward speed and a vertical part
from its rate of descent,
and the landing must remove both.
For the vertical part, a sink rate $v$ arrested over a stroke $d$ gives a
deceleration

$$ a = \frac{v^2}{2\,d}, \qquad n = \frac{a}{g_0} = \frac{v^2}{2\,g_0\,d}, $$

so the load in multiples of gravity falls as the stroke lengthens,
exactly as it did for the catapult and the net.
The horizontal part is taken by friction, by braking, or by the recovery
device of the companion article, over its own stroke.
This single relation is the spine of the whole subject.
Every interface below, the oleo strut, the skid, the water, the parachute
and its airbag, and the crushable structure, is a way of providing the
stroke $d$,
and the design problem is always to make that stroke long enough that the
deceleration stays within what the airframe and the payload can bear.
A short stroke is a hard landing and a long one is a soft one,
and the rest of the article is the catalogue of strokes.

## Wheels and Landing Gear

The most familiar interface is the wheel, and the first decision is whether
to retract it.
Fixed [landing gear][ref_landing_gear] is simple, light, and reliable but
hangs in the airstream for the whole flight, and that permanent drag costs
range and endurance against the budgets the propulsion and energy articles
tracked.
Retractable gear removes the cruise drag at the price of weight, a mechanism,
and a new way to fail, so it pays off only when the cruise is long enough
for the saved drag to matter, and when the mechanism does fail to extend the
fallback is the belly landing of the next section.
The layout is the [tricycle][ref_tricycle] or the
[conventional][ref_conventional] arrangement of the runway article,
chosen for ground stability and crosswind behavior.
The shock is absorbed by the gear itself, usually an
[oleo strut][ref_oleo], a telescoping leg in which a trapped gas acts as a
spring and oil forced through an orifice provides the damping,
so the strut converts the sink-rate energy into heat over its stroke and
sets the touchdown load directly,
and the oil's recoil damping also checks the rebound that would otherwise
bounce the aircraft back into the air, a tendency a rigid leg or a skid shows
more readily.
Where a hard arrival is possible, the gear can be made frangible or
sacrificial, designed to break or crush in a controlled way so that it,
rather than the airframe, absorbs an overload.
The vertical sink is not the only load the leg must carry.
A wheel touches down stationary and must be spun up to ground speed in an
instant, a rearward drag load and a burst of tire wear,
and a touchdown still drifting or crabbed in a crosswind adds a side load,
so the leg is sized by these combined loads rather than by the sink alone,
while the directional behavior of the rollout, the ground loop and the
crosswind handling, is the subject of the runway and control companions.

## Skids

The simplest interface is no wheel at all.
A skid trades the wheel and the strut for a reinforced surface that slides,
accepting wear and a longer ground scar in exchange for the least possible
mass and complexity, which is why the recovery article's belly landing is
common on small aircraft.
A skid takes the vertical energy in the give of the structure and the
horizontal energy in friction, so its stroke is short and its decelerations
are higher than a sprung wheel's,
which a light, slow airframe can tolerate where a heavy one cannot.
A sacrificial skid carries this further, a cheap replaceable wear part bolted
under the fuselage that is expected to be ground away and renewed,
protecting the primary structure at the cost of a part that is meant to be
consumed.
The surface matters as much as the skid, since the firm, smooth ground the
runway article preferred gives a predictable slide while soft or rough ground
shortens it unpredictably.
The interface is also matched to the surface itself,
with skis spreading the load to land on snow and oversized low-pressure
[tundra tires][ref_tundra] letting a wheeled aircraft work the rough,
unprepared ground the runway article warned about,
each a gear chosen for a surface that a plain wheel would dig into.

## Water Landings

Water is a surface too, and a [water landing][ref_water_landing] is either a
designed capability or an emergency.
A [floatplane][ref_floatplane] carries the load on pontoons and a
[flying boat][ref_flying_boat] on a boat-shaped hull,
and both rise onto the [step and plane][ref_planing] across the surface as
speed builds, the same on the water as a boat.
A land aircraft instead ditches, an emergency arrival on a surface it was not
built for.
Water changes the physics in two ways.
It is far denser than air, so it decelerates the aircraft sharply and loads
the underside heavily, and because it is effectively incompressible it
punishes a poor attitude,
the rhythmic porpoising in which a nose-low touch bounces the aircraft into a
growing pitch oscillation that can end in a capsize.
A water interface therefore rewards a clean attitude and a hull or float
shaped to enter the surface smoothly,
and a [seaplane operations reference][research_seaplane] documents the narrow
band of attitudes within which the landing stays controlled.

## Drogue and Main Parachutes

A parachute makes the surface almost irrelevant by lowering the aircraft
slowly, and the recovery article treated it as a recovery device,
so this article adds only the staging and the touchdown.
A descent often uses two canopies in sequence.
A small [drogue parachute][ref_drogue] deploys first at high speed,
where it stabilizes the vehicle and bleeds enough speed that the main can
open without bursting, reducing the dynamic pressure before the main inflates.
The [main canopy][ref_parachute] then handles the final descent.
The key point for this article is that the canopy still delivers the aircraft
to the ground at its descent rate,
so the touchdown energy of the first section is not removed but only reduced,
and a parachute recovery almost always ends on an airbag or a crushable nose
that provides the final stroke,
which is why the parachute and the impact interface are designed together
rather than separately.

## Deliberate Impact

For an expendable vehicle the cheapest interface is the ground itself,
taken on purpose.
An intentional intersection with the land or the water, a controlled descent
into terrain or sea as a terminal recovery, dispenses with gear, skid, and
canopy and lets the structure absorb the arrival by destroying itself.
The tool is [crashworthiness][ref_crashworthiness], a crushable structure of
tubes, honeycomb, or foam whose mean crushing force is set by the mass, the
impact speed, and the crushable length,
so even a high-speed arrival can be bounded to a survivable load for a
ruggedized payload if the crush stroke is long enough.
A [study of crushable energy absorbers][research_crashworthiness] shows
acceleration peaks cut by half when the structure is designed to fold
progressively rather than to shatter.
This is a deliberate, bounded crash rather than an accident,
and it suits a vehicle that is not meant to be flown again,
where the value is in the payload's data or the mission rather than in the
airframe's survival.

## Energy Bleeding Before Touchdown

Every interface is easier if less energy arrives at it,
so the approach is partly an exercise in shedding energy on purpose.
The [spoiler][ref_spoiler] of the control article dumps lift and adds drag,
a [forward slip][ref_slip] hangs the fuselage sideways to the airflow to
steepen the descent without gaining speed, and S-turns and a holding pattern
spend altitude and time,
while the [flare][ref_flare] just before touchdown trades the last of the
forward speed for a gentle sink.
The high-energy edge needs care, and it is the place a common term misleads.
True [aerobraking][ref_aerobraking] is an orbital maneuver, a spacecraft
dipping repeatedly into the thin upper atmosphere to shed orbital energy,
and it has nothing to do with an air-breathing engine, which cannot even run
in that rarefied air.
What a boost-glide, ramjet, or scramjet vehicle actually does at the end of
its run is [atmospheric deceleration][ref_atmospheric_entry] by drag,
and that is thermally limited, because braking hard at high Mach turns the
kinetic energy straight into heat in a structure already near its limit,
as the staged-propulsion article's thermal wall described.
Such a vehicle therefore bleeds its energy gently and high rather than
quickly and low, the opposite of aerobraking aggressively,
and only once it is slow and cool does it meet one of the interfaces above.

## Scale and the UAV Case

Size makes the small UAV the easy case for landing.
A light, slow aircraft arrives with little energy, since the touchdown energy
falls with the mass and with the square of the speed,
so a skid, a belly, or a parachute and airbag often suffices and a wheeled
gear can be minimal or absent entirely.
Retractable gear rarely earns its weight at the two-meter scale,
because the cruise is short and the drag of a small fixed gear or a clean
belly is a minor part of the budget.
The same low wing loading that eased the runway and the launch lowers the
touchdown speed and the energy with it,
so the small UAV that is gust-sensitive in the air is forgiving at the
surface, which is the favorable side of the same trade.
The design question reduces to matching the simplest interface that keeps the
touchdown load within what the airframe and the payload can bear.

## Putting Numbers to It

A worked example places the strokes on the twenty-five-kilogram aircraft of
the series.
A gentle arrival at a three-meter-per-second sink rate, absorbed over a
fifteen-centimeter oleo stroke, gives
$3^2 / (2 \times 0.15) = 30$ meters per second squared, about three times
gravity, an easy landing.
A firmer five-meter-per-second sink onto a skid that gives only ten
centimeters yields $5^2 / (2 \times 0.10) = 125$ meters per second squared,
near thirteen times gravity, which a rugged light airframe takes but a
delicate payload would not.
A parachute recovery descending at five meters per second onto a
twenty-five-centimeter airbag gives
$5^2 / (2 \times 0.25) = 50$ meters per second squared, about five times
gravity.
And a deliberate impact at thirty meters per second into a half-meter
crushable nose gives $30^2 / (2 \times 0.5) = 900$ meters per second squared,
about ninety times gravity, destructive to the airframe but bounded enough
for a hardened payload to survive.
The four cases differ only in the stroke, from fifteen centimeters of strut
to half a meter of crush, and the load follows it inversely,
which is the whole physics of touchdown in one column of numbers.

## Out of Scope

Several neighboring subjects are deliberately excluded.
The detailed mechanical design of the oleo strut, the tire, and the brake
and anti-skid system is an engineering specialty of its own,
and the braking friction of the rollout is the subject of the runway article.
The canopy aerodynamics and the deployment and inflation dynamics of a
parachute are named but, as in the recovery article, not derived here.
The structural finite-element analysis of a crushable airframe, and the
certification of a ditching, are beyond this scope.
The thermal protection and the detailed reentry mechanics of the high-energy
deceleration, and aerobraking proper, belong to the staged-propulsion and
spacecraft domains and are only distinguished here, not engineered.
And the guidance and the automatic landing that fly the approach these
interfaces receive are the subject of a separate treatment of the outer loop.

## Conclusion

The landing is the management of the energy the aircraft still carries when
it meets the surface.
That energy, the forward speed and the sink rate, is absorbed over a stroke,
and the deceleration is the energy divided by the stroke,
so a wheel on a long oleo leg lands softly, a skid lands harder, water lands
sharply, a parachute and airbag land gently, and a crushable nose lands once.
Bleed what energy you can on the approach with spoilers and slips and the
flare, choose the interface whose stroke keeps the load within the airframe
and the payload, and let scale work in the small UAV's favor,
and the aircraft that the rest of the series got into the air comes back to
the ground in one reusable piece, or in the case of the expendable vehicle,
exactly as intended.

## References

- [Reference, Aerobraking][ref_aerobraking]
- [Reference, Atmospheric Entry][ref_atmospheric_entry]
- [Reference, Conventional Landing Gear][ref_conventional]
- [Reference, Crashworthiness][ref_crashworthiness]
- [Reference, Drogue Parachute][ref_drogue]
- [Reference, Floatplane][ref_floatplane]
- [Reference, Flying Boat][ref_flying_boat]
- [Reference, Landing Flare][ref_flare]
- [Reference, Landing Gear][ref_landing_gear]
- [Reference, Oleo Strut][ref_oleo]
- [Reference, Parachute][ref_parachute]
- [Reference, Planing in Boats][ref_planing]
- [Reference, Slip in Aerodynamics][ref_slip]
- [Reference, Spoiler in Aeronautics][ref_spoiler]
- [Reference, Tricycle Landing Gear][ref_tricycle]
- [Reference, Tundra Tire][ref_tundra]
- [Reference, Water Landing][ref_water_landing]
- [Related Post, Launch and Recovery Systems for Fixed-Wing UAVs][related_post_launch]
- [Related Post, Runway Sizing for Fixed-Wing UAVs][related_post_runway]
- [Related Post, Staged and Boosted Propulsion for Small Fixed-Wing UAVs][related_post_staged]
- [Related Post, Stability, Control, and Configuration for Fixed-Wing UAVs][related_post_static]
- [Research, Crushable Energy-Absorbing Structure for Crashworthiness (MDPI Aerospace)][research_crashworthiness]
- [Research, Seaplane Operations (US Naval Academy)][research_seaplane]

[ref_aerobraking]: https://en.wikipedia.org/wiki/Aerobraking
[ref_atmospheric_entry]: https://en.wikipedia.org/wiki/Atmospheric_entry
[ref_conventional]: https://en.wikipedia.org/wiki/Conventional_landing_gear
[ref_crashworthiness]: https://en.wikipedia.org/wiki/Crashworthiness
[ref_drogue]: https://en.wikipedia.org/wiki/Drogue_parachute
[ref_flare]: https://en.wikipedia.org/wiki/Landing_flare
[ref_floatplane]: https://en.wikipedia.org/wiki/Floatplane
[ref_flying_boat]: https://en.wikipedia.org/wiki/Flying_boat
[ref_landing_gear]: https://en.wikipedia.org/wiki/Landing_gear
[ref_oleo]: https://en.wikipedia.org/wiki/Oleo_strut
[ref_parachute]: https://en.wikipedia.org/wiki/Parachute
[ref_planing]: https://en.wikipedia.org/wiki/Planing_(boat)
[ref_slip]: https://en.wikipedia.org/wiki/Slip_(aerodynamics)
[ref_spoiler]: https://en.wikipedia.org/wiki/Spoiler_(aeronautics)
[ref_tricycle]: https://en.wikipedia.org/wiki/Tricycle_landing_gear
[ref_tundra]: https://en.wikipedia.org/wiki/Tundra_tire
[ref_water_landing]: https://en.wikipedia.org/wiki/Water_landing
[related_post_launch]: {% post_url 2026-06-01-launch_and_recovery_systems_for_fixed_wing_uavs %}
[related_post_runway]: {% post_url 2026-05-31-runway_sizing_for_fixed_wing_uavs %}
[related_post_staged]: {% post_url 2026-06-03-staged_and_boosted_propulsion_for_fixed_wing_uavs %}
[related_post_static]: {% post_url 2026-06-05-stability_control_and_configuration_for_fixed_wing_uavs %}
[research_crashworthiness]: https://www.mdpi.com/2226-4310/12/4/332
[research_seaplane]: https://www.usna.edu/NAOE/_files/documents/Courses/EN486/20_-_Appendix_I_-_Seaplane_Operations.pdf
