---
layout: post
mathjax: true
comments: true
title:  "Aerobatics as Costed Trajectories for Fixed-Wing UAVs"
date:   2026-06-11 09:00:00 +0000
categories: aerospace engineering uav
series: fixed_wing_uav
series_title: Fixed-Wing UAV
series_index: 13
---
<!-- A128 -->
<script>console.log("A128");</script>

The structures article drew the flight envelope, the boundary an aircraft is
promised to hold together inside.
This article is about the paths flown within it.
It is written for the people who command unmanned aircraft and the autonomy
that flies them, and not at all for the human pilot, because a maneuver is a
different object once no one is aboard.
For a human a maneuver is a learned skill bounded by the tolerance of the body,
while for an unmanned aircraft it is a commanded spatiotemporal trajectory the
guidance and control loops fly to a tolerance, bounded by the airframe and the
energy state rather than the occupant.
One quantity organizes the subject, the energy state of the aircraft and the
[specific excess power][ref_em_theory] that changes it, because every maneuver
is a transaction in the potential, kinetic, and propulsive energy the series
has tracked throughout,
and every maneuver carries three costs, an energetic one, a structural one,
and a thermal one, whose relative size migrates with the speed regime until,
at the limit of reentry, all three bind at once.
This article treats the maneuver as a path and prices it, and it deliberately
discards the human pedagogy and physiology that the structures article already
set aside.

## A Maneuver as a Trajectory

A maneuver is a path through space and time, a [trajectory][ref_trajectory]
the aircraft is commanded to follow, described by its position, its velocity,
and its attitude as functions of time.
For the unmanned case the maneuver is issued as an intent the autopilot
realizes, the outer loops of the guidance article steering the aircraft along
the path while the inner loops of the dynamics article hold the attitude,
flown to a tolerance rather than felt by a body.
Two consequences follow from treating the maneuver as a trajectory rather than
a feeling.
The first is that it occupies a measurable volume of airspace for a measurable
time, the spatiotemporal effect, which is what matters to the mission and to
deconfliction.
The second is that its cost is the integral of expenditure along the path, so
two maneuvers that reach the same end state can cost very different amounts
depending on the route taken there.

## The Energy State and Specific Excess Power

The spine of the whole subject is the energy of the aircraft expressed as a
height.
The [specific energy][ref_specific_energy], the energy per unit weight, is the
energy height

$$ h_e = h + \frac{V^2}{2g}, $$

the altitude the aircraft would reach if it traded all of its speed for height,
the same energy height the boosted-propulsion article used.
The rate at which the aircraft can add to it is the specific excess power,

$$ P_s = \frac{V(T - D)}{W} = \frac{dh_e}{dt}, $$

the heart of [energy-maneuverability theory][ref_em_theory], the surplus of
thrust over drag carried at the current speed.
A maneuver is then a path traced in the plane of speed and energy height, and
the specific excess power says which way the path can go.
A climb or an acceleration spends excess power to raise the energy height, a
dive or a zoom trades kinetic for potential energy along a line of nearly
constant energy height, and a hard turn raises the drag so far that the excess
power goes negative and the energy height falls whatever the throttle does.
This is the difference between an instantaneous maneuver, which spends stored
energy and can be violent for a moment, and a sustained maneuver, which can be
held only where the excess power is zero or positive.

## The Three Costs

Every maneuver is priced along its path in three currencies.
The energetic cost is the change in energy height and the power spent against
drag to fly the path, the [induced drag][ref_induced_drag] of the lift that
bends the trajectory plus the profile and wave drag of pushing through the air.
The structural cost is the load factor the path demands, the lift as a multiple
of weight, which the structures article showed is bounded by the corners of the
load-versus-speed diagram, and for a turn of radius $R$ at speed $V$ it is

$$ n = \frac{V^2}{gR}, $$

so a tighter or faster path costs more structure.
The thermal cost is the heat the path deposits in the structure, negligible at
low speed and dominant at high speed, set by the
[stagnation temperature][ref_stagnation_temperature] that rises with the square
of the [Mach number][ref_mach].
The art of pricing a maneuver is that these three are not independent, because a
tighter turn raises the load factor and the induced drag together, and at high
speed it raises the heating too, so the costs are paid in concert and the
cheapest path is rarely the most direct one.
Beyond the three costs there is a gate that does not price the maneuver but
decides whether it can be flown at all, the control authority and the bandwidth
of the loops that must command it.
A trajectory is only flyable if the surfaces can generate the moment to bend it
and the actuators can move fast enough to track it, the control authority that
falls with dynamic pressure as the stability-and-control article described and
the actuator bandwidth that the dynamics article bounded,
so a figure can be impossible not because it overstresses the airframe or drains
its energy but because the loop cannot command it quickly or strongly enough.

## The Kinematic Primitives

Most of the catalogue is built from three primitives priced by the relations
above.
The turn bends the path in a plane, and in a level [banked turn][ref_banked_turn]
the load factor is $n = 1/\cos\phi$ for bank angle $\phi$, the radius is
$R = V^2/(g\sqrt{n^2-1})$, and the rate is $\dot\psi = g\sqrt{n^2-1}/V$, so the
tightest and fastest turn sits at the corner speed of the structures article
where the stall and the structural limit meet.
The loop bends the path in the vertical plane, a trade of kinetic for potential
energy in which the aircraft is slowest and the load factor lowest at the top
and fastest and most loaded at the bottom, so the loop is the energy-height
oscillation of the spine made visible.
The roll rotates the aircraft about its path with little change of trajectory,
limited by the control power of the ailerons rather than by energy, and freed
in the unmanned case from the roll-rate a human could tolerate.
A high roll rate is not free of dynamics, since rolling couples the pitch and
yaw axes through the [inertia coupling][ref_inertia_coupling] that troubled the
first aircraft to roll fast at speed, and a spinning propeller adds a
gyroscopic [precession][ref_precession] that biases a vertical pivot, both of
them effects the dynamics article would size and both more pronounced the faster
the figure is flown.
The vertical lines and the partial rolls and turns combine these primitives,
the zoom converting speed to height along a constant energy height and the
[hammerhead][ref_hammerhead] carrying the aircraft up until the speed bleeds
nearly to zero before it pivots and falls.
The turning bounds are usually drawn together as the
[maneuverability][ref_maneuverability] diagram, the turn rate against the
airspeed, closed by three walls, the lift limit where the wing stalls, the
structural limit where the load factor reaches the corner of the
load-versus-speed diagram, and the sustained limit where the specific excess
power falls to zero and the turn can no longer be held without shedding energy
height.
The instantaneous turn may sit anywhere inside the first two walls for as long
as the stored energy lasts, the sustained turn only on or inside the third, and
the corner speed is the point where the lift and structural walls meet, the
tightest and fastest turn the airframe can hold for a moment.

## A Catalogue of Maneuvers

The following maneuvers are scored on their spatiotemporal character, their
peak structural cost, and the highest regime in which they remain meaningful.
The energetic cost is read from whether the maneuver conserves, spends, or
trades energy height, and the thermal cost is inert for all of them in the
subsonic regime where they are flown.

| Maneuver | Path | Peak load | Energy height | Highest regime |
|---|---|---|---|---|
| Level turn | Horizontal arc | Moderate to high | Spent against drag | Supersonic, large radius |
| [Aileron roll][ref_aileron_roll] | Roll about the path | Near one | Nearly conserved | Supersonic |
| Loop | Vertical circle | High at the bottom | Traded then restored | Transonic at best |
| [Immelmann][ref_immelmann] | Half loop then half roll | High | Speed traded for height | Transonic |
| [Split S][ref_split_s] | Half roll then half loop | High | Height traded for speed | Transonic |
| [Hammerhead][ref_hammerhead] | Vertical up, pivot, down | Low at the pivot | Spent then recovered | Subsonic |
| [Cuban eight][ref_cuban_eight] | Linked inverted loops | High | Oscillated | Subsonic |
| [Barrel roll][ref_barrel_roll] | Helix about the path | Moderate | Nearly conserved | Transonic |
| [Spin][ref_spin] | Autorotating descent | Low but unsteady | Lost to drag | Subsonic, post-stall |
| [Cobra][ref_cobra] | High-alpha deceleration | High and unsteady | Dumped rapidly | Subsonic, post-stall |

The last two are post-stall figures in separated and unsteady flow, where no
closed-form pricing of the kind used above exists, a gap the article flags
rather than fills, in the same spirit the structures article left flutter to a
stiffness analysis.

## The Footprint in Space and Time

A maneuver is not only a cost but a volume of airspace held for a span of time,
and that footprint is read from the same quantities that priced it.
The vertical extent of a figure is its energy-height excursion, the height the
aircraft gains as it trades away its speed, and the horizontal extent is its
turn radius, so a loop flown fast needs a tall box and a hard turn needs a wide
one, while the time the figure takes is its arc length divided by the speed
along it.
This footprint is what the mission cares about, the box a sequence must fit
within and the airspace that must be held clear of other traffic, the
[separation][ref_separation] problem an autonomous aircraft solves by knowing in
advance the volume each commanded figure will sweep.
A maneuver flown in a moving airmass also drifts over the ground, so a figure
that must end at a ground point, such as the terminal maneuver of a guided
munition, is planned against the wind the guidance article treated, the air path
and the ground path differing by the drift accumulated over the time of the
figure.

## The Subsonic Regime

The subsonic regime is the home of figure flying, where the energetic and
structural costs dominate and the thermal cost is inert.
Energy is cheap to trade because the drag is low, so the figures are tight, and
control is by the aerodynamic surfaces throughout.
The unmanned aircraft has one decisive advantage here, that with no body to
protect it may be flown to the structural corner of the envelope rather than to
a human limit, so the full positive and negative load range of the structures
article is available, and the post-stall figures such as the
[cobra][ref_cobra] that punish a human become ordinary commands.
The negative side of the envelope opens here too, the outside loop and the
sustained inverted flight that load the structure downward throughout, which the
structures article showed only the symmetric aerobatic category is built to
take, the structurally most expensive figures in the catalogue.
The cost of a subsonic maneuver is therefore read almost entirely from the
load-versus-speed diagram and the energy-height trade, and the catalogue above
is flown in full.

## The Transonic and Supersonic Regimes

As the aircraft approaches and passes the speed of sound the character of
maneuvering changes.
[Wave drag][ref_wave_drag] appears and grows, so the specific excess power
collapses and a turn bleeds energy height fast, which makes every hard maneuver
an energy decision rather than a free choice.
Compressibility shifts the aerodynamic center rearward and can reduce control
effectiveness, the [Mach tuck][ref_mach_tuck] and the stiffening of the
controls that the [transonic][ref_transonic] region is known for, and the
enormous dynamic pressure of [supersonic][ref_supersonic] flight binds the
high-speed corner of the load-versus-speed diagram hard.
The figures that survive are the gentle ones, the rolls and the large-radius
turns and pulls, because a tight loop cannot be closed without bleeding to
subsonic speed partway through.
The thermal cost is no longer zero, the leading edges warming as the Mach
number climbs, and the maneuver set has begun to shrink from a catalogue toward
a few energy-managed curves.

## The Hypersonic Regime

In the [hypersonic][ref_hypersonic] regime the thermal cost dominates
everything.
The [stagnation temperature][ref_stagnation_temperature] rises with the square
of the Mach number, so the thermal wall of the boosted-propulsion article is
the binding constraint, and any maneuver that raises the
[angle of attack][ref_angle_of_attack] or the load factor raises the heating
and can exceed what the structure can survive.
Energetically the vehicle is on a glide or a ballistic arc with no thrust to
spare, a [boost-glide][ref_boost_glide] body or a
[hypersonic glide vehicle][ref_hgv] living on the energy height it was given,
so maneuvering cannot add energy and can only spend it.
The catalogue has by now collapsed almost to nothing.
What remains is bank-angle modulation and roll reversals that turn the lift
vector to buy cross-range, and shallow weaving that bleeds energy in a
controlled way, the same energy bleeding the landing-gear article treated as
the alternative to a structural and thermal overload.
A loop or a tight figure is impossible, so the word maneuver here means the
shaping of a descent and not the flying of a figure.

## Spaceplane Maneuvering During Reentry

The reentry of a [spaceplane][ref_lifting_body] is the limiting case in which
the energetic, structural, and thermal costs all bind at once inside a narrow
corridor.
The corridor is bounded above by the speed at which the air is too thin to turn
the vehicle and it skips back out, and below by the speed at which the
deceleration and the heating grow beyond what the structure and the thermal
protection can take, and the whole of [atmospheric entry][ref_atmospheric_entry]
is the management of the trajectory between those walls.
Inside the corridor the available maneuvering is small, and it is honest to say
that figure flying does not survive into this regime, so the word aerobatics is
extended here to mean deliberate commanded maneuvering rather than the flying of
figures.
What the vehicle can do is hold a high angle of attack to manage drag and
heating and modulate its bank angle in a series of roll reversals to steer
cross-range, the technique the Space Shuttle flew at about forty degrees of
angle of attack for more than a thousand nautical miles of cross-range.
The control authority migrates across the descent exactly as the
stability-and-control article described, the
[reaction control][ref_rcs] thrusters doing the work at the top where the air
is too thin for the surfaces to bite and handing over to the aerodynamic
surfaces as the dynamic pressure builds.
The orbital mechanics that placed the vehicle on the entry trajectory, the
deorbit, and the derivation of the entry guidance law are out of scope here, as
they were when the stability-and-control article drew the same boundary.

## Spaceplane Maneuvering After the Thermal Wall

Once the orbital and hypersonic energy has been spent and the vehicle has slowed
through the thermal wall into the lower atmosphere, conventional aerodynamic
maneuvering returns, but with a hard constraint.
The vehicle is now an unpowered glider with one attempt at the runway, so the
maneuvering is energy management, the terminal-area energy management the
[Space Shuttle][ref_space_shuttle] flew through a descending spiral and a
heading-alignment turn that spent exactly the surplus energy height needed to
arrive at the threshold on speed.
This is the energy bleeding of the landing-gear article and the total energy
management of the guidance article applied to a vehicle that began the day in
orbit, and a powered spaceplane that kept some propulsive energy in reserve
reopens more of the catalogue.
The progression of the whole article closes here, from the rich figure flying
of the slow and light regime, through the energy-expensive curves of the
supersonic regime, to the thermally bounded trajectory shaping of reentry, and
back at last to a single energy-managed approach.

## Scale and the UAV Case

The small unmanned aircraft inherits this entire range without the human ceiling
that bounds the crewed one.
The favorable structural scaling of the previous article lets a small airframe
pull a high load factor cheaply, so a small UAV can fly the subsonic catalogue
to the structural corner and use the post-stall figures a human could not
tolerate, whether flown first-person by an operator over the data link or as a
programmed trajectory by the autopilot.
The terminal maneuver of a loitering munition is exactly such a commanded
figure, a costed trajectory chosen to arrive at a point with a required angle
and speed.
What bounds the small aircraft is not the occupant but the energy budget of the
electric-systems article and the thermal limits of its powertrain, since a
sustained high-power maneuver drains the battery and heats the motor and its
controller, so the same three costs reappear at small scale in the form the
electric aircraft pays them.
Through all of it the theme of the structures article holds, that with no human
aboard the structure and the energy and the heat, and not a person, decide
which trajectories may be flown.

## Putting Numbers to It

A worked example prices a few maneuvers for the twenty-five-kilogram aircraft
the series has carried, with a wing loading near two hundred forty-five newtons
per square meter and a stall speed near eighteen meters per second.
A level turn at a load factor of two is a sixty-degree bank, and at a speed of
twenty-eight meters per second its radius is
$28^2/(9.81\sqrt{2^2-1}) \approx 46$ meters and its rate about thirty-five
degrees per second.
Pulling instead to the utility-category corner near a load factor of four and
four tenths at the corner speed of about thirty-eight meters per second tightens
the radius to about thirty-four meters and raises the rate to about sixty-three
degrees per second, the tightest turn the structure allows, though the specific
excess power there is deeply negative so the turn can be held only for a moment
before the energy height falls away.
A loop is sized by the energy-height trade, since with the throttle unable to
cover the drag the entry speed must carry the climb, so a loop fifty meters
across needs about $\sqrt{18^2 + 4(9.81)(25)} \approx 36$ meters per second at
the bottom merely to keep flying over the top.
At the other end of the range a Mach-five pass sits against the thermal wall the
boosted-propulsion article computed, where even a small increase in angle of
attack to turn raises the stagnation heating sharply, which is the concrete form
of the claim that a hypersonic maneuver is priced in heat before it is priced in
anything else.
The post-stall figures have no honest closed form at this level and are left, as
the spin and the cobra were in the catalogue, to a treatment in unsteady
aerodynamics.

## Out of Scope

Several neighboring subjects are deliberately excluded.
The human pedagogy and physiology of aerobatics, the sight picture and the
tolerance of acceleration, are set aside by design, since the article is written
for the unmanned case from the start.
The orbital mechanics, the deorbit burn, and the derivation of the reentry
guidance law are named but not worked, the boundary the stability-and-control
article drew.
The unsteady and separated aerodynamics of the post-stall figures, the
control-law synthesis that the dynamics and guidance articles treated, and the
propulsion-cycle detail of the propulsion articles are referenced rather than
rederived.
And the competition formalism of judged aerobatics, the catalogues of figures
and their scoring, is left aside as a human-sport concern beside the point of a
costed trajectory.

## Conclusion

A maneuver is a path through the energy state, priced in energy, in structure,
and in heat.
The price is read from the specific excess power that says where the path may
go, the load-versus-speed diagram that says how hard it may be bent, and the
stagnation temperature that says how fast it may be flown, and the three are
paid together rather than apart.
The catalogue of figures is richest in the slow and light regime where energy is
cheap and heat is absent, thins through the transonic and supersonic regimes
where wave drag makes every turn an energy decision, and collapses in the
hypersonic regime to the shaping of a descent, until at reentry the only
maneuvering left is a bank reversal inside a corridor where all three costs bind
at once.
The unmanned aircraft inherits the whole of this range without the human ceiling,
so the binding edge is drawn by the airframe and the energy and the heat, and the
last question of the series is the same as the first, how much of what is
physically possible the budget will actually allow.

## References

- [Book, Flight Mechanics of High-Performance Aircraft, Vinh][book_vinh]
- [Reference, Aerobatic Maneuver][ref_aerobatic_maneuver]
- [Reference, Aerobatics][ref_aerobatics]
- [Reference, Aileron Roll][ref_aileron_roll]
- [Reference, Angle of Attack][ref_angle_of_attack]
- [Reference, Atmospheric Entry][ref_atmospheric_entry]
- [Reference, Banked Turn][ref_banked_turn]
- [Reference, Barrel Roll][ref_barrel_roll]
- [Reference, Boost-Glide][ref_boost_glide]
- [Reference, Cuban Eight][ref_cuban_eight]
- [Reference, Energy-Maneuverability Theory][ref_em_theory]
- [Reference, Hammerhead Turn][ref_hammerhead]
- [Reference, Hypersonic Glide Vehicle][ref_hgv]
- [Reference, Hypersonic Speed][ref_hypersonic]
- [Reference, Immelmann Turn][ref_immelmann]
- [Reference, Inertia Coupling][ref_inertia_coupling]
- [Reference, Lift-Induced Drag][ref_induced_drag]
- [Reference, Lifting Body][ref_lifting_body]
- [Reference, Mach Number][ref_mach]
- [Reference, Mach Tuck][ref_mach_tuck]
- [Reference, Maneuverability][ref_maneuverability]
- [Reference, Precession][ref_precession]
- [Reference, Pugachev's Cobra][ref_cobra]
- [Reference, Reaction Control System][ref_rcs]
- [Reference, Separation in Aeronautics][ref_separation]
- [Reference, Space Shuttle][ref_space_shuttle]
- [Reference, Specific Energy][ref_specific_energy]
- [Reference, Spin in Aerodynamics][ref_spin]
- [Reference, Split S][ref_split_s]
- [Reference, Stagnation Temperature][ref_stagnation_temperature]
- [Reference, Supersonic Speed][ref_supersonic]
- [Reference, Transonic][ref_transonic]
- [Reference, Trajectory][ref_trajectory]
- [Reference, Wave Drag][ref_wave_drag]
- [Related Post, Dynamic Stability and Control for Fixed-Wing UAVs][related_post_dynamic]
- [Related Post, Guidance, Navigation, and Automatic Landing for Fixed-Wing UAVs][related_post_gnc]
- [Related Post, Landing Gear and the Physics of Touchdown for Fixed-Wing UAVs][related_post_landing]
- [Related Post, Staged and Boosted Propulsion for Small Fixed-Wing UAVs][related_post_staged]
- [Related Post, Stability, Control, and Configuration for Fixed-Wing UAVs][related_post_stability]
- [Related Post, Structures and the Flight Envelope for Fixed-Wing UAVs][related_post_structures]
- [Research, Shuttle Entry Guidance Revisited (NASA)][research_entry_guidance]
- [Research, Space Shuttle Entry Terminal Area Energy Management (NASA TM 104744)][research_taem]

[book_vinh]: https://books.google.com/books/about/Flight_Mechanics_of_High_Performance_Air.html?id=ND9dDeOARkMC
[ref_aerobatic_maneuver]: https://en.wikipedia.org/wiki/Aerobatic_maneuver
[ref_aerobatics]: https://en.wikipedia.org/wiki/Aerobatics
[ref_aileron_roll]: https://en.wikipedia.org/wiki/Aileron_roll
[ref_angle_of_attack]: https://en.wikipedia.org/wiki/Angle_of_attack
[ref_atmospheric_entry]: https://en.wikipedia.org/wiki/Atmospheric_entry
[ref_banked_turn]: https://en.wikipedia.org/wiki/Banked_turn
[ref_barrel_roll]: https://en.wikipedia.org/wiki/Barrel_roll
[ref_boost_glide]: https://en.wikipedia.org/wiki/Boost-glide
[ref_cobra]: https://en.wikipedia.org/wiki/Pugachev%27s_Cobra
[ref_cuban_eight]: https://en.wikipedia.org/wiki/Cuban_Eight
[ref_em_theory]: https://en.wikipedia.org/wiki/Energy%E2%80%93maneuverability_theory
[ref_hammerhead]: https://en.wikipedia.org/wiki/Hammerhead_turn
[ref_hgv]: https://en.wikipedia.org/wiki/Hypersonic_glide_vehicle
[ref_hypersonic]: https://en.wikipedia.org/wiki/Hypersonic_speed
[ref_immelmann]: https://en.wikipedia.org/wiki/Immelmann_turn
[ref_induced_drag]: https://en.wikipedia.org/wiki/Lift-induced_drag
[ref_inertia_coupling]: https://en.wikipedia.org/wiki/Inertia_coupling
[ref_lifting_body]: https://en.wikipedia.org/wiki/Lifting_body
[ref_mach]: https://en.wikipedia.org/wiki/Mach_number
[ref_mach_tuck]: https://en.wikipedia.org/wiki/Mach_tuck
[ref_maneuverability]: https://en.wikipedia.org/wiki/Maneuverability
[ref_precession]: https://en.wikipedia.org/wiki/Precession
[ref_rcs]: https://en.wikipedia.org/wiki/Reaction_control_system
[ref_separation]: https://en.wikipedia.org/wiki/Separation_(aeronautics)
[ref_space_shuttle]: https://en.wikipedia.org/wiki/Space_Shuttle
[ref_specific_energy]: https://en.wikipedia.org/wiki/Specific_energy
[ref_spin]: https://en.wikipedia.org/wiki/Spin_(aerodynamics)
[ref_split_s]: https://en.wikipedia.org/wiki/Split_S
[ref_stagnation_temperature]: https://en.wikipedia.org/wiki/Stagnation_temperature
[ref_supersonic]: https://en.wikipedia.org/wiki/Supersonic_speed
[ref_transonic]: https://en.wikipedia.org/wiki/Transonic
[ref_trajectory]: https://en.wikipedia.org/wiki/Trajectory
[ref_wave_drag]: https://en.wikipedia.org/wiki/Wave_drag
[related_post_dynamic]: {% post_url 2026-06-06-dynamic_stability_and_control_for_fixed_wing_uavs %}
[related_post_gnc]: {% post_url 2026-06-08-guidance_navigation_and_automatic_landing_for_fixed_wing_uavs %}
[related_post_landing]: {% post_url 2026-06-07-landing_gear_and_the_physics_of_touchdown_for_fixed_wing_uavs %}
[related_post_staged]: {% post_url 2026-06-03-staged_and_boosted_propulsion_for_fixed_wing_uavs %}
[related_post_stability]: {% post_url 2026-06-05-stability_control_and_configuration_for_fixed_wing_uavs %}
[related_post_structures]: {% post_url 2026-06-10-structures_and_the_flight_envelope_for_fixed_wing_uavs %}
[research_entry_guidance]: https://ntrs.nasa.gov/citations/19930029282
[research_taem]: https://ntrs.nasa.gov/api/citations/19920010688/downloads/19920010688.pdf
