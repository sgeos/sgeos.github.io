---
layout: post
mathjax: true
comments: true
title:  "Stability, Control, and Configuration for Fixed-Wing UAVs"
date:   2026-06-05 09:00:00 +0000
categories: aerospace engineering uav
series: fixed_wing_uav
series_title: Fixed-Wing UAV
series_index: 7
---
<!-- A122 -->
<script>console.log("A122");</script>

The airframe article in this series placed the center of gravity and named
the control surfaces, then declared a full treatment of stability and control
out of scope.
This article takes up that treatment.
Where the earlier articles managed speed, distance, and energy, this one
manages moments, the turning effects about the center of gravity that hold an
aircraft steady and that point it where the operator wants.
One quantity organizes the subject, namely the balance of those moments,
and a single proxy captures most of it, the static margin, the distance from
the center of gravity to the point where the aircraft is neutrally stable.
A large static margin makes an aircraft that holds its attitude and resists
the controls, and a small one makes an aircraft that changes attitude
readily and demands attention,
so the whole design is a choice on the line between stability and
maneuverability.
This piece builds on the [airframe companion][related_post_lwpla] for the
center of gravity, the [runway companion][related_post_runway] for the
planform, and the [propulsion companion][related_post_propulsion] for the
lift-to-drag ratio that the wing choices here trade against.

## The Moment Balance and the Static Margin

An aircraft is trimmed when the moments about its
[center of gravity][ref_cg] sum to zero, and it is stable when a small
disturbance creates a moment that pushes it back toward trim.
Whether it does so depends on where the center of gravity sits relative to
the neutral point, the position at which the whole aircraft's lift acts when
every surface is counted.
The [longitudinal stability][ref_long_stability] is measured by the static
margin,

$$ K_n = \frac{x_{np} - x_{cg}}{\bar c}, $$

the distance from the center of gravity to the neutral point as a fraction of
the [mean aerodynamic chord][ref_chord].
A positive static margin, with the center of gravity ahead of the neutral
point, gives a restoring moment and a stable aircraft,
and a negative one gives a divergent moment and an aircraft that cannot be
flown without constant correction.
The size of the margin is the master trade of the whole article.
A trainer carries ten to fifteen percent for docile behavior, a sport design
carries a few percent for liveliness, an aerobatic design sits near zero so
that it responds equally in any attitude, and a design that goes negative
buys [maneuverability][ref_flight_dynamics] at the price of needing active
control to stay pointed at all.
The center of gravity is not a fixed point either, since it shifts with the
payload and the placement of the battery or the fuel,
so the real requirement is that the loaded center of gravity stay ahead of
the neutral point across the whole loading envelope,
and a design that balances at the limit when full can become unstable as it
empties, which is why the allowable center-of-gravity range is fixed early
and the heavy items are placed to keep the aircraft inside it.

## Lateral and Directional Static Stability

Pitch is only one of three axes, and the other two have their own static
stability set by configuration rather than by control.
[Directional stability][ref_directional_stability] is the weathercock
tendency that swings the nose back into the relative wind after a sideslip,
and it comes from the vertical fin, which acts aft of the center of gravity
just as the horizontal tail does in pitch,
so it is sized by a vertical tail volume coefficient of the same form,
the fin area and its arm over the wing area and span.
The rudder is the yaw control, but the fin is the yaw stability,
and the distinction is the same one drawn for the elevator and the
horizontal tail.
Lateral stability is the roll response to a sideslip, and its main source is
[dihedral][ref_dihedral], the upward angle of the wings,
which makes the lower wing in a sideslip meet the air at a higher angle and
lift more, rolling the aircraft back to level.
Wing sweep and a high wing position add to the same effect, and too little
of it leaves an aircraft that will not pick up a dropped wing,
while too much makes it roll uncomfortably in response to every yaw.
The balance between the dihedral effect and the weathercock stability is what
sets the dynamic spiral and Dutch-roll behavior,
which belongs to the dynamic treatment left out of scope below.

## Airfoils, Camber, and Invertibility

The wing's own moment is set by its [airfoil][ref_airfoil], and specifically
by its [camber][ref_camber].
A cambered, lifting airfoil makes lift efficiently but carries a nose-down
[pitching moment][ref_pitching_moment] that something else must trim,
usually a tail surface pushing down, which is why a conventional aircraft
flies with a small download on the tail.
A symmetric airfoil makes less lift for its size but carries almost no
pitching moment and behaves the same upright or inverted,
which is why it is chosen for tail surfaces and for the wings of
[aerobatic][ref_aerobatics] and invertible aircraft that must fly as well on
their backs as upright.
The choice of airfoil is therefore not only a lift decision but a moment
decision, because the camber that buys lift also buys a trimming burden,
and the symmetry that buys invertibility gives some of that lift back.

## Configuration Archetypes

Where the trimming and stabilizing moments come from is the configuration
question.
A conventional layout places a horizontal stabilizer on an
[empennage][ref_empennage] aft of the wing, on a long moment arm, and trims
the cambered wing with a download while providing pitch control.
A [canard][ref_canard] places the small surface ahead of the wing instead,
and a [tandem wing][ref_tandem] splits the lift between two main surfaces.
A [tailless flying wing][ref_flying_wing], the most constrained case, has no
separate surface at all and must stabilize itself,
which the [tailless aircraft][ref_tailless] tradition does with a
[swept wing][ref_swept_wing] carrying [washout][ref_washout] toward the tips
or with a reflexed airfoil whose upturned trailing edge produces a nose-up
moment, so the center of gravity can still sit ahead of the neutral point.
Washout earns its place on conventional wings as well,
because twisting the tips to a lower incidence makes them stall after the
root, which keeps the ailerons biting into the stall when the operator most
needs roll control.
The price of the flying wing is a short moment arm and a small usable static
margin, which is why it tends to be a careful compromise rather than a
forgiving one.

## Control Surfaces by Placement and Name

The [flight control surfaces][ref_control_surfaces] take their names from
where they sit and what they do.
On a conventional aircraft the [elevator][ref_elevator] on the tail controls
pitch, the [ailerons][ref_aileron] near the wingtips control roll, and the
[rudder][ref_rudder] on the fin controls yaw.
Rolling with the ailerons also yaws the aircraft the wrong way,
because the down-going aileron adds drag as well as lift on its wing,
a coupling called [adverse yaw][ref_adverse_yaw] that the rudder coordinates
against and that differential and Frise ailerons are shaped to reduce,
which is the clearest reminder that the three axes are not independent.
When one surface does two jobs the name combines.
An [elevon][ref_elevon] on a flying wing is an elevator and an aileron at
once, moving together for pitch and differentially for roll.
A ruddervator on a [V-tail][ref_vtail] is a rudder and an elevator at once.
A [stabilator][ref_stabilator] is an all-moving tail that is the pitch
surface in its entirety, and a [flaperon][ref_flaperon] is an aileron that
also droops as a flap.
The lesson is that the names follow the placement and the combination of
functions, so an unfamiliar layout can always be read by asking which axis
each surface moves and whether it shares a second duty.

## High-Lift and Spoiler Devices

Not every movable surface trims or steers.
A [flap][ref_flap] on the trailing edge increases lift and drag together for
slow flight, which lowers the stall speed the runway companion cared about.
A [spoiler][ref_spoiler] does the opposite, a panel on the upper surface that
when raised dumps lift and adds drag, used to steepen a descent without
gaining speed, to put weight on the wheels at touchdown, and when raised on
one wing only, as a spoileron, to roll.
An [air brake][ref_airbrake] adds drag without disturbing the lift across the
span, for speed control alone.
These devices manage the lift and the drag rather than the moments,
and on a glider-like UAV the spoiler in particular is the tool that controls
the glide path on the way down.

## Control Authority and Dynamic Pressure

Control authority need not come from an aerodynamic surface, and which source
is available is set by the [dynamic pressure][ref_dynamic_pressure]
$q = \tfrac{1}{2}\rho V^2$, because a surface produces a moment only in
proportion to the air pushing on it.
At ordinary speed and density the surfaces dominate, but as the speed or the
air thins their authority fades, and another source must take over.
Differential thrust, throttling one side of a multi-engine aircraft harder
than the other, produces a yawing moment, and it is the standard backup when
a rudder is damaged or absent.
[Thrust vectoring][ref_thrust_vectoring] deflects the exhaust or the
propeller wake to produce pitch, roll, or yaw directly,
and a distributed set of electric motors can produce any of the three by
varying thrust across the span, the same distributed-propulsion idea the
electric-energy companion described.
These thrust methods work as long as the engines run, independent of the
dynamic pressure, which is why they matter on a tailless aircraft with little
room for a control arm, at very low speed where surfaces have little air to
bite, and in the post-stall regime named in the staged-propulsion companion.
At the limit, where there is essentially no air at all,
the only remaining source is reaction.
A [reaction control system][ref_rcs] expels mass through small thrusters to
produce a moment directly, needing neither air nor a running main engine but
only stored propellant,
which is how a [spaceplane][ref_spaceplane] holds its attitude above the
atmosphere and why such vehicles, from the X-15 to the Space Shuttle, blend
from reaction control to aerodynamic surfaces as the dynamic pressure builds
on reentry, near the point where $q$ grows enough for the surfaces to bite.
For the vehicles of this series the case arises at the top of a high
boost-glide arc, where the staged-propulsion companion's vehicle leaves the
aerodynamic regime, and at the two-meter scale the accessible form is a
[cold-gas thruster][ref_cold_gas] set of the kind used for small-satellite
attitude control.
A conventional low-altitude UAV needs none of this,
so reaction control is the control source for the regime where the air runs
out, not standard equipment, and its cost is the propellant it spends on
every correction, a budget as finite as the staged-propulsion stock.

## The Wing Tradeoff

The planform that the configuration hangs on is itself a trade between speed
and gliding performance.
A high [aspect ratio][ref_aspect_ratio], a long slender wing, lowers the
induced drag and raises the lift-to-drag ratio that the propulsion and
electric-energy companions showed sets endurance and range,
which is why a glider or a long-endurance UAV carries a long thin wing.
A low aspect ratio and a high [wing loading][ref_wing_loading] give a smaller,
stiffer wing that is faster, less disturbed by gusts, and more maneuverable,
at the cost of a higher stall speed and a poorer glide.
Planform shape follows the speed regime as well,
a straight wing for low speed, a [swept wing][ref_swept_wing] for transonic
and high-speed flight, and a [delta wing][ref_delta] for the high-speed and
high-angle regimes the runway and staged-propulsion companions discussed.
The wing is therefore chosen for where on the speed-and-glide line the
mission sits, and that choice then constrains the stability and control that
the rest of the article sized.

## The Energy Cost of Control

Stability and control are not free, and their price is paid in drag against
the endurance budget the energy companions tracked.
Trimming a cambered wing with a tail download adds
[lift-induced drag][ref_induced_drag], the trim drag, because the tail must
make a downward force that the wing then has to overcome with extra lift.
Every control deflection adds drag while it is held, and a marginally stable
aircraft that is always correcting holds its surfaces deflected more of the
time than a stable one does.
A flying wing avoids the tail download and so avoids that share of the trim
drag, which is one of its genuine efficiencies,
and a relaxed-stability design that trims with little or no download spends
less on trim drag at the price of the active control it then requires.
The moment balance and the energy budget are therefore linked,
because the cheapest aircraft to hold steady is also, within limits, the
cheapest to fly.

## Putting Numbers to It

A worked example places the numbers on the conventional and the tailless
cases.
For a stable conventional UAV the center of gravity is set about twelve
percent of the mean aerodynamic chord ahead of the neutral point,
a static margin of $K_n \approx 0.12$,
and the horizontal tail is sized by its volume coefficient,

$$ V_H = \frac{l_t\, S_t}{\bar c\, S_w}, $$

the product of the tail arm and the tail area over the chord and the wing
area, with a value around one half being typical for a docile aircraft.
A larger tail or a longer arm raises the volume coefficient and the stability
together, and moving the center of gravity aft toward the neutral point
trades that stability for a lighter, more responsive feel until, near a
static margin of zero, the aircraft becomes an aerobatic one that holds no
attitude on its own.
A flying wing reaches the same positive margin with no tail at all,
by sweeping the wing and washing out the tips and setting the elevons to a
few degrees of reflex, so the center of gravity still leads the neutral point
but by a smaller distance and with less margin to spare.
None of these is a final design, but together they show the single lever,
the position of the center of gravity relative to the neutral point,
that sets where an aircraft sits between steady and agile.

## Out of Scope

Several neighboring subjects are deliberately excluded.
The dynamic behavior of the aircraft, the oscillations named the phugoid, the
short period, the Dutch roll, and the spiral mode, and the stability
derivatives that govern them, is a quantitative subject of its own and is
treated here only through its static precursor.
The design of stability-augmentation and fly-by-wire control laws,
which is what lets a negative-static-margin aircraft fly at all, is named but
not derived.
Spin entry and recovery, and the aeroelastic flutter the airframe companion
already flagged, are beyond this scope,
as is the detailed shaping of an airfoil beyond its camber and its moment.
The detailed design of a reaction control system, its propellant, its
thruster sizing, and its plume, is treated here only as a moment source and
not engineered.
The translational problem of reaching, circularizing, and holding an orbit,
the province of [orbital mechanics][ref_orbital_mechanics], the
[orbital maneuver][ref_orbital_maneuver], and
[stationkeeping][ref_stationkeeping], is a separate and entirely legitimate
discipline for spacecraft that actually reach orbit,
and it is out of scope here because this article controls attitude rather
than trajectory, and its vehicles are atmospheric or at most suborbital,
so a reaction thruster appears only as a source of moments and never as a
means of changing the orbit the vehicle is in.
And the autopilot that schedules these surfaces through a mission is left to a
guidance and control treatment of its own.

## Conclusion

Stability and control for a fixed-wing UAV are the management of the moments
about the center of gravity.
The static margin, the distance from the center of gravity to the neutral
point, sets where the aircraft sits between steady and agile in pitch,
the fin and the dihedral hold the other two axes,
the airfoil's camber sets the moment that must be trimmed,
the configuration sets where the trimming and controlling moments come from,
and those moments are produced by surfaces where there is air, by thrust
where the engines run, and by reaction where there is neither.
The wing underneath is chosen for speed or for gliding, and every bit of
trim and control is paid for in drag against the endurance budget.
Place the center of gravity, size the tail or the reflex, name the surfaces
by what they move, and the aircraft can be made as steady or as sharp as the
mission wants, with the static margin as the number that says which.

## References

- [Reference, Adverse Yaw][ref_adverse_yaw]
- [Reference, Aerobatics][ref_aerobatics]
- [Reference, Aileron][ref_aileron]
- [Reference, Air Brake in Aeronautics][ref_airbrake]
- [Reference, Airfoil][ref_airfoil]
- [Reference, Aspect Ratio in Aeronautics][ref_aspect_ratio]
- [Reference, Camber in Aerodynamics][ref_camber]
- [Reference, Canard in Aeronautics][ref_canard]
- [Reference, Center of Gravity of an Aircraft][ref_cg]
- [Reference, Chord in Aeronautics][ref_chord]
- [Reference, Cold Gas Thruster][ref_cold_gas]
- [Reference, Delta Wing][ref_delta]
- [Reference, Dihedral in Aeronautics][ref_dihedral]
- [Reference, Directional Stability][ref_directional_stability]
- [Reference, Dynamic Pressure][ref_dynamic_pressure]
- [Reference, Elevator in Aeronautics][ref_elevator]
- [Reference, Elevon][ref_elevon]
- [Reference, Empennage][ref_empennage]
- [Reference, Flaperon][ref_flaperon]
- [Reference, Flap in Aeronautics][ref_flap]
- [Reference, Flight Control Surfaces][ref_control_surfaces]
- [Reference, Flight Dynamics][ref_flight_dynamics]
- [Reference, Flying Wing][ref_flying_wing]
- [Reference, Lift-Induced Drag][ref_induced_drag]
- [Reference, Longitudinal Stability][ref_long_stability]
- [Reference, Orbital Maneuver][ref_orbital_maneuver]
- [Reference, Orbital Mechanics][ref_orbital_mechanics]
- [Reference, Orbital Station-Keeping][ref_stationkeeping]
- [Reference, Pitching Moment][ref_pitching_moment]
- [Reference, Reaction Control System][ref_rcs]
- [Reference, Rudder][ref_rudder]
- [Reference, Spaceplane][ref_spaceplane]
- [Reference, Spoiler in Aeronautics][ref_spoiler]
- [Reference, Stabilator][ref_stabilator]
- [Reference, Swept Wing][ref_swept_wing]
- [Reference, Tailless Aircraft][ref_tailless]
- [Reference, Tandem Wing][ref_tandem]
- [Reference, Thrust Vectoring][ref_thrust_vectoring]
- [Reference, V-Tail][ref_vtail]
- [Reference, Washout in Aeronautics][ref_washout]
- [Reference, Wing Loading][ref_wing_loading]
- [Related Post, Propulsion and Power Sizing for Small Fixed-Wing UAVs][related_post_propulsion]
- [Related Post, Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass][related_post_lwpla]
- [Related Post, Runway Sizing for Fixed-Wing UAVs][related_post_runway]
- [Research, Aircraft Stability and Control (Embry-Riddle)][research_erau_stability]
- [Research, Review of Thrust Vectoring Technology Applications in UAVs (MDPI Drones)][research_mdpi_tvc]

[ref_adverse_yaw]: https://en.wikipedia.org/wiki/Adverse_yaw
[ref_aerobatics]: https://en.wikipedia.org/wiki/Aerobatics
[ref_aileron]: https://en.wikipedia.org/wiki/Aileron
[ref_airbrake]: https://en.wikipedia.org/wiki/Air_brake_(aeronautics)
[ref_airfoil]: https://en.wikipedia.org/wiki/Airfoil
[ref_aspect_ratio]: https://en.wikipedia.org/wiki/Aspect_ratio_(aeronautics)
[ref_camber]: https://en.wikipedia.org/wiki/Camber_(aerodynamics)
[ref_canard]: https://en.wikipedia.org/wiki/Canard_(aeronautics)
[ref_cg]: https://en.wikipedia.org/wiki/Center_of_gravity_of_an_aircraft
[ref_chord]: https://en.wikipedia.org/wiki/Chord_(aeronautics)
[ref_cold_gas]: https://en.wikipedia.org/wiki/Cold_gas_thruster
[ref_control_surfaces]: https://en.wikipedia.org/wiki/Flight_control_surfaces
[ref_delta]: https://en.wikipedia.org/wiki/Delta_wing
[ref_dihedral]: https://en.wikipedia.org/wiki/Dihedral_(aeronautics)
[ref_directional_stability]: https://en.wikipedia.org/wiki/Directional_stability
[ref_dynamic_pressure]: https://en.wikipedia.org/wiki/Dynamic_pressure
[ref_elevator]: https://en.wikipedia.org/wiki/Elevator_(aeronautics)
[ref_elevon]: https://en.wikipedia.org/wiki/Elevon
[ref_empennage]: https://en.wikipedia.org/wiki/Empennage
[ref_flap]: https://en.wikipedia.org/wiki/Flap_(aeronautics)
[ref_flaperon]: https://en.wikipedia.org/wiki/Flaperon
[ref_flight_dynamics]: https://en.wikipedia.org/wiki/Flight_dynamics
[ref_flying_wing]: https://en.wikipedia.org/wiki/Flying_wing
[ref_induced_drag]: https://en.wikipedia.org/wiki/Lift-induced_drag
[ref_long_stability]: https://en.wikipedia.org/wiki/Longitudinal_stability
[ref_orbital_maneuver]: https://en.wikipedia.org/wiki/Orbital_maneuver
[ref_orbital_mechanics]: https://en.wikipedia.org/wiki/Orbital_mechanics
[ref_pitching_moment]: https://en.wikipedia.org/wiki/Pitching_moment
[ref_rcs]: https://en.wikipedia.org/wiki/Reaction_control_system
[ref_rudder]: https://en.wikipedia.org/wiki/Rudder
[ref_spaceplane]: https://en.wikipedia.org/wiki/Spaceplane
[ref_spoiler]: https://en.wikipedia.org/wiki/Spoiler_(aeronautics)
[ref_stabilator]: https://en.wikipedia.org/wiki/Stabilator
[ref_stationkeeping]: https://en.wikipedia.org/wiki/Orbital_station-keeping
[ref_swept_wing]: https://en.wikipedia.org/wiki/Swept_wing
[ref_tailless]: https://en.wikipedia.org/wiki/Tailless_aircraft
[ref_tandem]: https://en.wikipedia.org/wiki/Tandem_wing
[ref_thrust_vectoring]: https://en.wikipedia.org/wiki/Thrust_vectoring
[ref_vtail]: https://en.wikipedia.org/wiki/V-tail
[ref_washout]: https://en.wikipedia.org/wiki/Washout_(aeronautics)
[ref_wing_loading]: https://en.wikipedia.org/wiki/Wing_loading
[related_post_lwpla]: {% post_url 2026-05-30-prototyping_fixed_wing_aircraft_with_lightweight_pla_and_fiberglass %}
[related_post_propulsion]: {% post_url 2026-06-02-propulsion_and_power_sizing_for_fixed_wing_uavs %}
[related_post_runway]: {% post_url 2026-05-31-runway_sizing_for_fixed_wing_uavs %}
[research_erau_stability]: https://eaglepubs.erau.edu/introductiontoaerospaceflightvehicles/chapter/aircraft-stability-control/
[research_mdpi_tvc]: https://www.mdpi.com/2504-446X/9/10/689
