---
layout: post
mathjax: true
comments: true
title:  "Launch and Recovery Systems for Fixed-Wing UAVs"
date:   2026-06-01 09:00:00 +0000
categories: aerospace engineering uav
series: fixed_wing_uav
series_title: Fixed-Wing UAV
series_index: 3
---
<!-- A116 -->
<script>console.log("A116");</script>

A fixed-wing unmanned aerial vehicle can reach flying speed and return to
the ground without a runway, and the methods that make this possible are
the subject of this article.
A companion piece sized [the runway itself][related_post_runway],
and the recurring theme there was that many aircraft use a strip for only
one phase, or for neither, because a catapult, a net, a parachute, or a
ramp does the work instead.
This article takes up those methods directly.
One quantity dominates the analysis, namely the energy that must be added
to launch and removed to recover, because that energy is fixed by the
flying speed and the mass, and the only free choices are the distance and
the time over which it is delivered.
A second companion article covers [building the airframe][related_post_lwpla]
that these systems must accelerate and catch.

## The Energy and Stroke Master Variable

A launch must raise the aircraft from rest to a safe flying speed,
and the [kinetic energy][ref_kinetic_energy] it must acquire is

$$ E = \tfrac{1}{2} m V_e^2, $$

where $m$ is the mass and $V_e$ is the speed at the end of the launch,
a little above the stall speed and close to the liftoff speed of the
runway analysis.
By the work-energy theorem this same energy is the average force times the
stroke length, so over a launch stroke $L$ the average acceleration is

$$ \bar a = \frac{V_e^2}{2L}, \qquad
   n = \frac{\bar a}{g} = \frac{V_e^2}{2\,g\,L}, $$

where $n$ is the acceleration expressed in multiples of gravity.
Recovery is the same statement run backward.
The system must remove $\tfrac{1}{2} m V_c^2$ of energy from an aircraft
arriving at capture speed $V_c$, and if it does so over a stopping stroke
$d$ the deceleration is $V_c^2 / 2d$ with the same $g$-load form.
This is the spine of the whole subject.
The energy is set by mass and speed and is not negotiable,
the speed traces back through the stall speed to wing loading exactly as
in the runway analysis, and the single lever the designer holds is the
stroke.
A long stroke spreads the same energy over more distance and keeps the
$g$-load low, while a short stroke raises the load in inverse proportion.
Every method below is a way of providing or absorbing that energy,
and each is judged by the stroke it affords and the load it imposes.

## Launch by Catapult

A catapult stores energy and releases it along a track to accelerate the
aircraft on a shuttle.
The [aircraft catapult][ref_aircraft_catapult] of a carrier is the
large-scale ancestor, and the UAV versions differ mainly in how the energy
is stored.
A bungee catapult holds the energy in stretched elastic and is the
simplest and lightest, suited to aircraft of a few kilograms up to roughly
ten.
A pneumatic catapult drives the shuttle with compressed air and a
hydraulic one with oil pressurized against a gas spring,
both of which pack more energy into a transportable unit and reach the
larger tactical sizes.
A rail launcher constrains the aircraft to a straight track for a
repeatable attitude at release.
Whatever the store, the design trade is the one the master variable makes
explicit.
For a fixed exit speed the product of acceleration and stroke is fixed,
so a launcher that must fit on a trailer or a deck pays for its short rail
in a high $g$-load, and lengthening the rail is the direct way to be gentle
on the airframe and the payload.

A related family pulls rather than throws.
A [winch or a tow launch][ref_gliding], borrowed from sailplane practice,
accelerates the aircraft along a cable wound in by a ground winch or paid
out behind a tow vehicle, which delivers the launch energy over a long and
gentle stroke and suits an unpowered or lightly powered glider-like UAV.
The energy bookkeeping is unchanged, since the same $\tfrac{1}{2} m V_e^2$
must be supplied, but the long stroke keeps the acceleration low.

## Launch by Booster and Zero-Length Launch

When even a rail is unwanted, a rocket booster can supply the launch energy.
[Rocket-assisted takeoff][ref_jato], long used to lift overloaded crewed
aircraft from short fields, scales down to a solid motor that burns for a
few seconds and is then jettisoned or retained.
The booster adds thrust rather than reacting against a track,
so the stroke is the distance the aircraft travels while the motor burns
rather than the length of a rail.
Carried to its limit the technique becomes [zero-length launch][ref_zero_length],
in which the aircraft leaves a simple stand or canister under booster
thrust alone with no ground run at all.
Boosters buy the smallest ground footprint of any launch method and tolerate
heavy aircraft, at the cost of carrying pyrotechnics, accepting a high and
brief acceleration, and managing the spent motor.
The same energy bookkeeping applies, since the impulse of the motor must
supply $\tfrac{1}{2} m V_e^2$ plus the work against drag and gravity during
the burn.

## Recovery by Net and Cable

A net strung on a frame is the most direct way to stop an aircraft in a
small space.
The aircraft flies into the net and the net yields, and the stopping stroke
is whatever travel the net and its energy absorbers allow.
Because the master variable ties load inversely to stroke,
a net that is rigidly anchored stops the aircraft fast and harshly,
while a net backed by a brake or a compliant mount lengthens the stroke and
softens the capture.
A cable system replaces the net with a single vertical line.
The [Skyhook][ref_scaneagle] used by the ScanEagle is the clearest example,
in which a hook on the wingtip catches a suspended rope and the aircraft
swings around it as the line pays out under tension,
so the long arc and the controlled tension are what hold the $g$-load down.
The [RQ-21 Blackjack][ref_rq21] uses the same launcher-and-cable pairing,
which is why both aircraft can work from a small deck or a clearing with no
strip at all.
A [broad review of runway-free recovery][research_mdpi_recovery] catalogs
these alongside rope and barrier variants, and the common engineering
problem in all of them is to make the capture compliant enough that the
deceleration stays within the airframe limit.

## Recovery by Arrested Landing

An arrested landing keeps a short ground roll but shortens it drastically
with [arresting gear][ref_arresting_gear].
The aircraft touches down on a prepared surface, a hook engages a wire,
and the wire pays out against a brake that absorbs the energy over a few
tens of meters.
The [RQ-7 Shadow][ref_rq7] recovers this way, catapult-launched at one end
of its mission and caught by a hook and tailored arresting gear at the other.
This method is the bridge to the runway analysis,
because it still needs a strip, only a far shorter one than an unaided
landing roll would require,
and the strip is therefore sized by the arresting stroke rather than by the
braking friction of the surface.
The energy the gear must dissipate is the same $\tfrac{1}{2} m V_c^2$,
and the stroke of the wire is the lever that sets the load.

## Recovery by Parachute and Airbag

A parachute removes the horizontal flight entirely and lowers the aircraft
under a canopy.
The descent settles at the terminal velocity where canopy drag balances
weight, and from the [drag equation][ref_drag_equation] that velocity is

$$ V_d = \sqrt{\frac{2\,m\,g}{\rho\,C_D\,S}}, $$

where $C_D$ is the canopy drag coefficient, near $1.5$ for a round canopy,
and $S$ is the canopy area.
Solving for the area needed to hit a target descent rate is the core
[sizing step for a parachute recovery system][research_fruity_chutes],
and the [terminal-velocity balance][research_nasa_descent] is the same one
used to size recovery canopies for rockets and capsules.
A parachute alone does not finish the job,
because the aircraft still strikes the ground at the descent rate,
so a [qualified recovery system][research_butler_parachute] usually pairs
the [canopy][ref_parachute] with an airbag or a crushable structure that
takes the residual energy over a short final stroke.
The appeal is that a parachute needs almost no ground infrastructure and
works for an aircraft that cannot be flown to a precise spot,
and the cost is the descent footprint, the wind drift under canopy,
and the mass and volume of the stowed system.

## Recovery by Belly Skid

The simplest recovery uses the airframe itself.
A belly landing on a reinforced underside trades wheels and brakes for a
skid on grass or dirt, accepting wear in exchange for mechanical simplicity,
and it is common on small aircraft that can absorb the touchdown in soft
structure.
It reduces the recovery to the landing analysis of the companion article
with a steeper approach and a higher rolling resistance,
and its limit is the same energy that governs every other method,
since a heavier or faster aircraft delivers more energy to the skid than a
light structure can absorb without damage.

## Recovery by High-Alpha Braking

The aircraft can also brake itself, by pitching to a very high angle of
attack so that pressure drag does the work a net or a parachute would
otherwise do.
Three related procedures sit on this spectrum.
A [deep stall][research_deepstall] holds the aircraft in a steady
high-angle, drag-dominated descent, trading lift for a steep path and a low
forward speed with no external hardware at all.
A [perched landing][research_perching] instead sheds the horizontal speed
mainly with lift during a rapid flare, so that in the ideal case the
aircraft arrives at a chosen point with almost no horizontal or vertical
speed, the way a bird settles onto a branch.
Between the two is the [cobra][ref_cobra], a rapid pitch-up past sixty and
toward ninety degrees of angle of attack along a nearly level path, which
dumps a large fraction of the kinetic energy into drag within a few aircraft
lengths and then either returns to normal flight or continues into a
capture or a settle.

Used deliberately, cobra braking can be a routine recovery procedure rather
than an air-show flourish.
The value follows straight from the master variable, because the recovery
energy scales as the square of the capture speed,
so a cobra that sheds even a third of the approach speed before the aircraft
meets a net, a cable, or a perch removes more than half of the energy the
capture device must absorb.
A small UAV with sufficient pitch authority, a full-flying tail or a large
elevator, and enough thrust to arrest the pitch can perform the maneuver
repeatably, and [the same procedure has been flown autonomously on
tail-sitter UAVs][research_cobra_tailsitter].
The practical effect is to turn a fast, energetic arrival into a slow one,
which shrinks every downstream number, the net stroke, the cable load, and
the perch structure alike.

The procedure is not free, and its costs are the ones the
[recovery review][research_mdpi_recovery] flags for the high-angle methods.
It demands control authority and post-stall stability, because the
deep-stall regime is a narrow one from which an underpowered or weakly
controlled aircraft cannot recover, and it loads the structure and the
attitude control during the pitch-up.
It is most fragile to gusts at the moment of lowest speed,
and making it routine rather than heroic depends on a validated controller
and a planned trajectory rather than open-loop piloting.
Stated plainly, cobra braking lowers the capture speed and therefore the
whole recovery energy budget, at the price of demanding that the airframe
and the autopilot be good enough to enter and leave a very high angle of
attack on command.

## Wind and Environment

Wind helps launch and recovery for the reason it helps a runway.
The aircraft flies relative to the air, so a headwind reduces the ground
speed that the catapult must impart at release to $V_e - V_w$,
and it reduces the closing speed into a net or a cable to $V_c - V_w$,
which cuts the energy the system must handle by the square factor familiar
from the [runway wind analysis][related_post_runway].
A crosswind is the harder case, because a net, a cable, and a parachute
all want the aircraft arriving straight,
and a steady wind from one quarter argues for orienting the recovery
equipment into it just as it argues for runway alignment.
Operation from a moving ship adds the deck motion to the closing geometry,
which is one reason cable and net systems, with their forgiving capture
volume, dominate at sea.

## The Acceleration Limit

The binding constraint across all of these methods is the acceleration the
aircraft and its payload can survive.
The airframe has a structural limit, and a gimbaled camera or a sensitive
sensor often has a lower one, so the most fragile component sets the ceiling.
Because the master variable fixes the product of load and stroke for a
given energy, respecting that ceiling is a demand for stroke.
A launcher or a capture device that is too compact forces a high load,
and the only honest fixes are to lengthen the stroke, to reduce the capture
speed by recovering into more wind or at a lower wing loading,
or to accept a heavier and stronger structure that raises the limit at a
cost in useful load.
Stating the acceleration limit up front, and sizing the stroke to meet it,
is the discipline that keeps a clever compact system from quietly destroying
the payload it exists to carry.

## Failure and Abort Modes

Every launch and recovery method has a way of failing, and the consequence
of that failure is as much a part of the choice as the nominal performance.
On the launch side a catapult can release early or with too little stored
energy, leaving the aircraft below flying speed at the end of the stroke,
so a sound design carries margin in the exit speed or tolerates a low-energy
departure without loss of the aircraft.
A booster can [fail to fire or fire late][ref_hangfire],
which is why a pyrotechnic launch demands ordnance discipline,
a clear safe arc, and a defined state to fall back to if the motor does not
light.
On the recovery side a hook can skip the wire in a [bolter][ref_bolter],
so an arrested-landing aircraft must keep enough energy to climb away and
try again rather than arriving committed.
A net or a cable can fail to latch, a parachute can fail to deploy or fail
to open from its reefed stage, and a [deep stall][ref_deep_stall] or a
cobra entered without enough control authority can become a descent from
which the aircraft cannot recover.

The unifying principle is to design for [graceful failure][ref_fail_safe].
A launch wants a survivable low-energy abort, a parachute recovery wants a
reserve or a backup mode, a capture wants a go-around path,
and the aircraft wants a [flight-termination or controlled-ditch
option][ref_flight_termination] for the case where recovery is impossible,
so that a single failure costs the aircraft at worst rather than harming
people or property.
The energy view makes the stakes plain,
because the same kinetic energy that a successful recovery removes over a
controlled stroke is the energy loose in a failed one,
scaling with the same mass and speed,
so the heavier and faster the aircraft, the more its failure modes deserve
deliberate design rather than hope.

## Matching Launch to Recovery

Launch and recovery need not use the same principle, and the strongest
systems mix them.
A catapult launch pairs naturally with a cable or net recovery,
because both avoid a runway and both can work from a deck or a clearing,
and the [ScanEagle][ref_scaneagle] and the [RQ-21 Blackjack][ref_rq21]
are built exactly this way.
A catapult launch can instead pair with an arrested landing when a short
strip is available, as on the [RQ-7 Shadow][ref_rq7],
trading the recovery mast for a prepared surface.
A booster launch pairs with a parachute recovery for an aircraft that must
deploy from the smallest possible site and is content to be retrieved
wherever it comes down.
Any of the capture methods can be preceded by a high-alpha braking maneuver
to lower the closing speed, which is the cheapest way to shrink the capture
device, since it adds no ground hardware and spends only control authority.
The design question is therefore two questions,
namely how to add the launch energy and how to remove the recovery energy,
and the answers are chosen separately against the site, the mission, and the
acceleration limit.

## Airframe Implications

Each method reaches into the structure of the aircraft.
A catapult or a rail needs a hardpoint and a shuttle interface able to carry
the launch force into the airframe without local failure,
and a booster needs a mounting and a thermal margin for the motor.
A cable capture needs a wingtip hook and a wing strong enough to take the
asymmetric snatch, and an arrested landing needs a tailhook and the
structure to react it.
A parachute needs a stowage bay and an attachment that places the canopy
load near the center of gravity so the aircraft hangs in a controlled
attitude, which couples to the balance discussion of the
[airframe-building companion][related_post_lwpla].
A belly skid needs a reinforced and abrasion-tolerant underside.
None of this is free mass, so the recovery and launch choice is also an
airframe choice, made early because it shapes the primary structure.

## Putting Numbers to It

A worked example reuses the aircraft of the runway analysis,
a UAV of mass $25$ kilograms with a liftoff speed near $18.6$ meters per
second.
The launch energy is $\tfrac{1}{2}\times 25 \times 18.6^2 \approx 4.3$
kilojoules, which is fixed.
On a five-meter catapult stroke the acceleration is
$18.6^2 / (2 \times 5) \approx 34.6$ meters per second squared,
about $3.5$ times gravity, for an average shuttle force near $865$ newtons.
Halve the stroke to two and a half meters and the load doubles to about
seven times gravity for the same energy, which is the compactness penalty
in plain numbers.
For recovery into a net at a capture speed of $20$ meters per second the
energy is $\tfrac{1}{2}\times 25 \times 20^2 = 5$ kilojoules,
and a three-meter compliant stroke gives
$20^2 / (2 \times 3) \approx 66.7$ meters per second squared,
near seven times gravity, which is why cable and net systems work hard to
extend the stroke.
Had the aircraft shed a third of that closing speed in a cobra first,
to about $13.3$ meters per second, the same net would face
$\tfrac{1}{2}\times 25 \times 13.3^2 \approx 2.2$ kilojoules instead of five,
less than half, for the same stroke and a correspondingly lower load.
For a parachute targeting a gentle five-meter-per-second descent with a
round canopy at $C_D \approx 1.5$,
the area is $2 \times 245 / (1.225 \times 1.5 \times 25) \approx 10.7$
square meters, a canopy about $3.7$ meters across,
and the residual $312$ joules at touchdown is what the airbag or crushable
nose must absorb over its short stroke.
None of these is a final design, but together they show that the energy is
the same story told three ways, and that the stroke is always the lever.

## Out of Scope

Several neighboring subjects are deliberately excluded.
The detailed mechanical design of catapults and rails, their seals,
brakes, and shuttle dynamics, is an engineering specialty of its own.
The internal ballistics and the propellant and safety handling of rocket
boosters are a separate discipline, and this article treats a booster only
as a source of impulse.
The canopy aerodynamics and the deployment and inflation dynamics of a
parachute, including reefing and the snatch load at line stretch, are named
but not derived here.
The guidance and control laws that fly an aircraft into a cable, a net, a
deep stall, a cobra, or a perch, and the automatic spot-landing problem,
are an autopilot topic deferred to a separate treatment,
since this article uses these maneuvers as procedures rather than deriving
the controllers and trajectories that make them repeatable.
The runway-based landing roll itself is covered in the
[companion article][related_post_runway] and is not repeated.
Vertical-takeoff and hybrid configurations, the tail-sitter, the tiltrotor,
and the lift-plus-cruise arrangement, achieve runway independence by
building launch and recovery into the airframe and its propulsion rather
than into an external system, and they are a configuration choice treated
elsewhere.
Aerial retrieval, in which one aircraft catches another in flight, is named
for completeness and is likewise out of scope.
And full structural analysis, certification, and the airworthiness of
recovery systems are beyond this scope.
The quantitative reliability analysis of the failure modes above,
the redundancy sizing, and the detailed design of a flight-termination
system are named in the failure discussion but are not carried out here.
The operational and procurement questions, the logistics and crew of a
launcher, its setup time, its reusability and cost per cycle,
and the power source that charges a pneumatic or hydraulic store,
are likewise out of scope, since they sit beside the sizing physics rather
than within it.

## Conclusion

Launch and recovery for a fixed-wing UAV are the management of one energy.
The launch must add and the recovery must remove a kinetic energy fixed by
the mass and the flying speed, and every method is a way of delivering that
energy over a chosen stroke, with the acceleration rising as the stroke
shrinks.
Catapults and boosters add the energy, nets and cables and hooks and
parachutes and skids remove it, a high-angle cobra can shed much of it
before capture, and wind lowers the speed that sets it.
Choose the launch method and the recovery method separately,
size the stroke of each to the acceleration the airframe and payload can
bear, and the result is a runway-independent system a builder can defend
with numbers rather than guess at.

## References

- [Reference, AAI RQ-7 Shadow][ref_rq7]
- [Reference, Aircraft Catapult][ref_aircraft_catapult]
- [Reference, Arresting Gear][ref_arresting_gear]
- [Reference, Boeing Insitu MQ-27 ScanEagle][ref_scaneagle]
- [Reference, Boeing Insitu RQ-21 Blackjack][ref_rq21]
- [Reference, Bolter in Aeronautics][ref_bolter]
- [Reference, Cobra Maneuver][ref_cobra]
- [Reference, Deep Stall][ref_deep_stall]
- [Reference, Drag Equation][ref_drag_equation]
- [Reference, Fail-Safe Design][ref_fail_safe]
- [Reference, Flight Termination System][ref_flight_termination]
- [Reference, Gliding, Winch and Aerotow Launch][ref_gliding]
- [Reference, Hang Fire][ref_hangfire]
- [Reference, JATO and Rocket-Assisted Takeoff][ref_jato]
- [Reference, Kinetic Energy][ref_kinetic_energy]
- [Reference, Parachute][ref_parachute]
- [Reference, Zero-Length Launch][ref_zero_length]
- [Related Post, Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass][related_post_lwpla]
- [Related Post, Runway Sizing for Fixed-Wing UAVs][related_post_runway]
- [Research, Cobra Maneuver Learning for Tail-Sitter UAVs][research_cobra_tailsitter]
- [Research, Parachute Recovery System Selection and Qualification (Butler Parachutes)][research_butler_parachute]
- [Research, Post-Stall Perching with a Fixed-Wing Glider (MIT)][research_perching]
- [Research, Precision Deep-Stall Landing of Fixed-Wing UAVs][research_deepstall]
- [Research, Runway-Free Recovery Methods for Fixed-Wing UAVs, A Comprehensive Review][research_mdpi_recovery]
- [Research, UAS Parachute Recovery Tutorial (Fruity Chutes)][research_fruity_chutes]
- [Research, Velocity During Recovery (NASA Glenn)][research_nasa_descent]

[ref_aircraft_catapult]: https://en.wikipedia.org/wiki/Aircraft_catapult
[ref_arresting_gear]: https://en.wikipedia.org/wiki/Arresting_gear
[ref_bolter]: https://en.wikipedia.org/wiki/Bolter_(aeronautics)
[ref_cobra]: https://en.wikipedia.org/wiki/Cobra_maneuver
[ref_deep_stall]: https://en.wikipedia.org/wiki/Deep_stall
[ref_drag_equation]: https://en.wikipedia.org/wiki/Drag_equation
[ref_fail_safe]: https://en.wikipedia.org/wiki/Fail-safe
[ref_flight_termination]: https://en.wikipedia.org/wiki/Flight_termination_system
[ref_gliding]: https://en.wikipedia.org/wiki/Gliding
[ref_hangfire]: https://en.wikipedia.org/wiki/Hang_fire
[ref_jato]: https://en.wikipedia.org/wiki/JATO
[ref_kinetic_energy]: https://en.wikipedia.org/wiki/Kinetic_energy
[ref_parachute]: https://en.wikipedia.org/wiki/Parachute
[ref_rq21]: https://en.wikipedia.org/wiki/Boeing_Insitu_RQ-21_Blackjack
[ref_rq7]: https://en.wikipedia.org/wiki/AAI_RQ-7_Shadow
[ref_scaneagle]: https://en.wikipedia.org/wiki/Boeing_Insitu_MQ-27_ScanEagle
[ref_zero_length]: https://en.wikipedia.org/wiki/Zero-length_launch
[related_post_lwpla]: {% post_url 2026-05-30-prototyping_fixed_wing_aircraft_with_lightweight_pla_and_fiberglass %}
[related_post_runway]: {% post_url 2026-05-31-runway_sizing_for_fixed_wing_uavs %}
[research_butler_parachute]: https://www.butlerparachutes.com/wp-content/uploads/BUPS-Recovery-System-Qualification.pdf
[research_cobra_tailsitter]: https://arxiv.org/abs/1906.02596
[research_deepstall]: https://link.springer.com/article/10.1007/s10846-020-01264-3
[research_fruity_chutes]: https://fruitychutes.com/uav_rpv_drone_recovery_parachutes/uas-parachute-recovery-tutorial
[research_mdpi_recovery]: https://www.mdpi.com/2504-446X/8/9/463
[research_nasa_descent]: https://www.grc.nasa.gov/www/k-12/VirtualAero/BottleRocket/airplane/rktvrecv.html
[research_perching]: https://groups.csail.mit.edu/robotics-center/public_papers/Moore14a.pdf
