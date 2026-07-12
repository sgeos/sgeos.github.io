---
layout: post
mathjax: true
comments: true
title:  "Dynamic Stability and Control for Fixed-Wing UAVs"
date:   2026-06-06 09:00:00 +0000
categories: aerospace engineering uav
series: fixed_wing_uav
series_title: Fixed-Wing UAV
series_index: 8
---
<!-- A123 -->
<script>console.log("A123");</script>

The stability and control article in this series treated the static question,
whether a disturbance produces a moment that pushes the aircraft back toward
trim, and deferred the dynamic question to a sequel.
This article is that sequel.
Static stability gives the sign of the restoring moment, but it does not say
how the aircraft actually moves once it is disturbed,
and a statically stable aircraft can still oscillate unacceptably if those
oscillations do not die away.
One quantity organizes the dynamic question, the damping of the aircraft's
natural motions, because what matters is not only that a disturbance is
opposed but that the resulting motion settles in acceptable time.
The aircraft behaves as a set of springs with mass and friction,
and each of its characteristic motions has a frequency and a rate of decay,
so the subject is the management of those two numbers across the handful of
modes the aircraft owns.
This piece builds directly on the
[static stability companion][related_post_static] for the restoring moments,
the [airframe companion][related_post_lwpla] for the inertia, and the
[runway companion][related_post_runway] for the planform whose sweep shapes
some of these motions.

## The Spring, the Mass, and the Damping

A single disturbed motion of an aircraft behaves like a
[damped harmonic oscillator][ref_harmonic_oscillator],

$$ \ddot x + 2\zeta\,\omega_n\,\dot x + \omega_n^2\,x = 0, $$

where $\omega_n$ is the [natural frequency][ref_natural_frequency] and
$\zeta$ is the [damping ratio][ref_damping_ratio].
The pieces map onto the aircraft directly.
The static stability of the previous article is the spring that sets the
frequency, the mass and the moments of inertia are the mass, and the
aerodynamic forces that grow with the rate of motion, the same surfaces and
flow that resist a pitch rate or a yaw rate, are the damping.
The damping ratio decides the character of the response.
Below one the motion oscillates while it decays, at one it returns without
overshoot, and above one it crawls back slowly,
and a value somewhere between about a third and one is usually what a
designer wants, fast enough to settle and smooth enough not to overshoot
badly.
The full [flight dynamics][ref_flight_dynamics] are a set of coupled
equations whose solutions are several such modes at once,
and the rest of this article is a tour of those
[modes][ref_dynamic_modes] and of what is done when their damping is poor.
These modes are a small-disturbance description taken about one trim
condition, so their frequencies and damping shift with speed and altitude,
which is why a controller schedules its gains against the flight condition
rather than trusting a single setting everywhere.

## The Longitudinal Modes

The pitch motion splits into two modes with very different speeds.
The [short-period mode][ref_dynamic_modes] is a fast, usually well-damped
oscillation in angle of attack and pitch that settles within a second or
two, with a damping ratio that good design keeps between about a third and
two, and it is the one the operator feels as the immediate response to a
pitch input.
The [phugoid][ref_phugoid] is its slow opposite, a gentle exchange of speed
for altitude and back over a period of many seconds,
lightly damped with a ratio often only a few hundredths,
so the aircraft wallows slowly through shallow climbs and descents after a
disturbance.
The phugoid is mild enough that a pilot or an autopilot corrects it without
trouble, which is why it is allowed to be so lightly damped,
while the short-period mode must be well damped because it is fast enough to
matter on every input.

## The Lateral-Directional Modes

The roll and yaw motions give three more modes, and they couple.
Roll subsidence is not an oscillation at all but a simple exponential decay
of roll rate, the natural damping of a wing that resists being rolled,
and it is normally fast and untroublesome.
The spiral mode is a slow divergence or convergence in which a small bank
leads to a gradual tightening or loosening spiral,
and its sign is set by the balance the static companion drew between the
dihedral effect and the weathercock stability,
so a design strong in the fin and weak in dihedral tends to spiral in slowly.
The [Dutch roll][ref_dutch_roll] is the troublesome one,
a coupled oscillation in which the aircraft yaws one way while rolling the
other, and it is often poorly damped,
arising when the dihedral effect is large relative to the directional
stability, which is exactly the opposite balance from the spiral.
The two are traded against each other, since fixing one by adjusting the
fin or the dihedral tends to worsen the other,
and the Dutch roll is the mode that most often needs help it cannot get from
the airframe alone.

## Damping, Frequency, and Handling Qualities

How much damping is enough is not a matter of taste but of measured
acceptability.
A motion's [settling time][ref_settling_time] is roughly

$$ t_s \approx \frac{4}{\zeta\,\omega_n}, $$

so the product of the damping ratio and the frequency, not either alone,
sets how quickly a mode dies away.
Decades of flight test condensed this into handling-qualities standards,
which specify minimum damping ratios and frequency ranges for each mode and
each flight phase,
and into the [Cooper-Harper rating scale][ref_cooper_harper] by which test
pilots grade the result from one to ten.
The standards are the reason the short-period mode is required to be well
damped while the phugoid is allowed to be loose,
and they translate directly to a UAV even with no pilot aboard,
because an autopilot tracking a poorly damped mode faces the same difficulty
a pilot would and benefits from the same minimum damping.

## Gusts and Ride Quality

A disturbance need not come from the controls.
The atmosphere is rarely still, and [turbulence][ref_turbulence] drives the
aircraft continuously, exciting the same modes over and over rather than
once, so the damping that decides how a mode settles after a single nudge
also decides how roughly the aircraft rides through rough air.
A well-damped mode absorbs a gust and forgets it,
while a lightly damped one is rung again and again and never settles.
Size makes this acute for a small UAV.
A gust is a change in the wind, but its effect is a change in angle of attack
that scales with the gust speed over the flight speed,
so a slow, lightly wing-loaded UAV of the kind the runway and static
companions favored feels a given gust far more than a fast, heavy aircraft
does.
The same low wing loading that shortens the runway and eases the launch
worsens the ride, which is a trade rather than a fault,
and it is one more reason a small UAV leans on the augmentation of the next
section to fly steadily in air that a larger aircraft would shrug off.

## Stability Augmentation

When the airframe cannot supply enough damping, electronics can.
A [yaw damper][ref_yaw_damper] is the classic case, a feedback loop that
senses the yaw rate with a gyroscope in the
[inertial measurement unit][ref_imu], multiplies it by a gain, and commands
the rudder to oppose it, which adds artificial damping to the Dutch roll
without changing how the aircraft is flown.
A pitch damper does the same for the short-period mode,
and both are low-authority loops that only damp, leaving the trim and the
commanded maneuver to the operator.
This is the inner loop of a
[flight control system][ref_fcs], and on a UAV it is a few
[feedback gains][ref_pid] on the rate signals the autopilot already
measures, so stability augmentation costs little once the sensors are
present.
The lesson the static companion anticipated is realized here,
that a moment source plus a rate measurement plus a gain can manufacture the
damping the airframe lacks.
The gain cannot be raised without bound, though.
Sensor noise sets a ceiling on how hard the loop can feed back before it
amplifies that noise into the controls, the actuator's rate and bandwidth
limit how quickly it can answer, and any delay around the loop turns added
gain into added lag,
so too much authority or too much delay drives the very oscillation it was
meant to damp, the [pilot-induced oscillation][ref_pio] and actuator
saturation that haunt an overdriven loop.
A loop that only damps is a stability augmentation system,
while one that also shapes the commanded response, so that a stick or an
autopilot command asks for a chosen rate rather than a raw surface
deflection, is a control augmentation system,
and the two are layered on the same sensors and actuators.

## Fly-by-Wire and Relaxed Stability

Carried far enough, the same idea lets an aircraft fly that could not fly
on its own.
A design with [relaxed or negative static stability][ref_relaxed_stability]
has little or no natural restoring moment, which the static companion noted
buys maneuverability at the price of constant correction,
and a [fly-by-wire][ref_fly_by_wire] system supplies that correction
continuously, sensing the motion and driving the surfaces many times a
second to hold an attitude the airframe would otherwise diverge from.
The control system becomes the spring and the damper that the airframe no
longer provides,
which is how a modern agile aircraft is both unstable and flyable at once.
For a small UAV the same architecture is ordinary rather than exotic,
because the autopilot is already in the loop,
and a relaxed-stability UAV simply leans harder on a controller it was going
to carry regardless.

## Scale and the UAV Case

Size changes the numbers in a way that matters for a small UAV.
The natural frequencies of these modes rise as the aircraft shrinks,
so a two-meter UAV oscillates faster than a full-scale aircraft and its
modes come and go in a fraction of the time,
which demands an autopilot loop and servo actuators with enough bandwidth to
keep up.
A control that is fast enough for a transport aircraft can be too slow for a
small UAV whose short-period mode rings several times a second.
The remedy is the same augmentation already described, scheduled for the
faster dynamics, and it is one reason small fixed-wing UAVs lean on their
autopilots for routine stability rather than treating the controller as a
convenience.
The differential-propulsion and surface authority of the static companion
are the actuators these loops command, now driven by rate feedback rather
than by the operator alone.

## Putting Numbers to It

A worked example shows what augmentation buys.
Take a Dutch roll with a natural frequency of about three radians per second
and a bare damping ratio of $0.05$.
Its settling time is $4 / (0.05 \times 3) \approx 27$ seconds,
and since its damped period is near $2\pi / 3 \approx 2.1$ seconds it
oscillates a dozen times before it quiets, which an operator would find
miserable and an autopilot would fight.
Add a yaw damper that raises the damping ratio to $0.4$,
and the settling time falls to $4 / (0.4 \times 3) \approx 3.3$ seconds,
under two cycles, which is comfortable.
The frequency barely changed, because the yaw damper added damping rather
than stiffness, and that is the point,
the airframe set the frequency and the electronics set the decay.
A phugoid on the same aircraft might have a period near ten seconds at a
cruise of twenty-five meters per second and a damping ratio of a few
hundredths, slow and loose enough to leave to the autopilot's outer loop.
None of these is a final design, but together they show the single lever,
the damping of each mode, that turns a statically sound aircraft into a
dynamically pleasant one.

## Out of Scope

Several neighboring subjects are deliberately excluded.
The estimation of the stability derivatives and the assembly and solution of
the full equations of motion are a quantitative discipline of their own,
and this article uses their results, the modes and their damping, rather
than deriving them.
The synthesis of the control laws, the selection of the gains, and the
proof of their robustness are named but not carried out,
as are the sensors and the state estimation, the filtering that turns noisy
rate signals into the clean feedback the loops assume.
The structural and aeroelastic dynamics, including the flutter the airframe
companion flagged, and the nonlinear behavior of departure and spin, are
beyond this scope.
And the outer loop, the guidance and navigation that decide where the
aircraft should go and the automatic landing that brings it down,
is the subject of a separate treatment that builds on the inner loop sized
here.

## Conclusion

Dynamic stability and control are the management of how the aircraft's
motions decay.
Each mode is a damped oscillation whose frequency the static stability and
the inertia set and whose damping the aerodynamic rate forces provide,
and the design goal is a damping ratio high enough that every mode settles in
acceptable time.
The short-period mode and the roll subsidence are usually well behaved,
the phugoid is loose but harmless, and the Dutch roll is the one that most
often needs a yaw damper to make it pleasant,
while a relaxed-stability aircraft hands the whole job of the spring and the
damper to a fly-by-wire loop.
Size the damping of each mode, augment the modes the airframe leaves poorly
damped, and the statically sound aircraft of the previous article becomes one
that flies as steadily as the mission demands.

## References

- [Reference, Aircraft Dynamic Modes][ref_dynamic_modes]
- [Reference, Aircraft Flight Control System][ref_fcs]
- [Reference, Cooper-Harper Rating Scale][ref_cooper_harper]
- [Reference, Damping Ratio][ref_damping_ratio]
- [Reference, Dryden Wind Turbulence Model][ref_turbulence]
- [Reference, Dutch Roll][ref_dutch_roll]
- [Reference, Flight Dynamics][ref_flight_dynamics]
- [Reference, Fly-by-Wire][ref_fly_by_wire]
- [Reference, Harmonic Oscillator][ref_harmonic_oscillator]
- [Reference, Inertial Measurement Unit][ref_imu]
- [Reference, Natural Frequency][ref_natural_frequency]
- [Reference, Phugoid][ref_phugoid]
- [Reference, PID Controller][ref_pid]
- [Reference, Pilot-Induced Oscillation][ref_pio]
- [Reference, Relaxed Stability][ref_relaxed_stability]
- [Reference, Settling Time][ref_settling_time]
- [Reference, Yaw Damper][ref_yaw_damper]
- [Related Post, Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass][related_post_lwpla]
- [Related Post, Runway Sizing for Fixed-Wing UAVs][related_post_runway]
- [Related Post, Stability, Control, and Configuration for Fixed-Wing UAVs][related_post_static]
- [Research, Dynamic Stability (Cornell MAE 5070)][research_cornell_dynamic]
- [Research, Flying Qualities Criteria (Princeton MAE 331)][research_princeton_fq]

[ref_cooper_harper]: https://en.wikipedia.org/wiki/Cooper%E2%80%93Harper_rating_scale
[ref_damping_ratio]: https://en.wikipedia.org/wiki/Damping_ratio
[ref_dutch_roll]: https://en.wikipedia.org/wiki/Dutch_roll
[ref_dynamic_modes]: https://en.wikipedia.org/wiki/Aircraft_dynamic_modes
[ref_fcs]: https://en.wikipedia.org/wiki/Aircraft_flight_control_system
[ref_flight_dynamics]: https://en.wikipedia.org/wiki/Flight_dynamics
[ref_fly_by_wire]: https://en.wikipedia.org/wiki/Fly-by-wire
[ref_harmonic_oscillator]: https://en.wikipedia.org/wiki/Harmonic_oscillator
[ref_imu]: https://en.wikipedia.org/wiki/Inertial_measurement_unit
[ref_natural_frequency]: https://en.wikipedia.org/wiki/Natural_frequency
[ref_phugoid]: https://en.wikipedia.org/wiki/Phugoid
[ref_pid]: https://en.wikipedia.org/wiki/PID_controller
[ref_pio]: https://en.wikipedia.org/wiki/Pilot-induced_oscillation
[ref_relaxed_stability]: https://en.wikipedia.org/wiki/Relaxed_stability
[ref_settling_time]: https://en.wikipedia.org/wiki/Settling_time
[ref_turbulence]: https://en.wikipedia.org/wiki/Dryden_Wind_Turbulence_Model
[ref_yaw_damper]: https://en.wikipedia.org/wiki/Yaw_damper
[related_post_lwpla]: {% post_url 2026-05-30-prototyping_fixed_wing_aircraft_with_lightweight_pla_and_fiberglass %}
[related_post_runway]: {% post_url 2026-05-31-runway_sizing_for_fixed_wing_uavs %}
[related_post_static]: {% post_url 2026-06-05-stability_control_and_configuration_for_fixed_wing_uavs %}
[research_cornell_dynamic]: https://courses.cit.cornell.edu/mae5070/DynamicStability.pdf
[research_princeton_fq]: https://stengel.mycpanel.princeton.edu/MAE331Lecture21.pdf
