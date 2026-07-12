---
layout: post
mathjax: true
comments: true
title:  "Guidance, Navigation, and Automatic Landing for Fixed-Wing UAVs"
date:   2026-06-08 09:00:00 +0000
categories: aerospace engineering uav
series: fixed_wing_uav
series_title: Fixed-Wing UAV
series_index: 10
---
<!-- A125 -->
<script>console.log("A125");</script>

The dynamic stability article in this series sized the inner loop, the fast
feedback that holds an attitude and damps the aircraft's natural motions.
This article takes up the outer loop that sits on top of it,
the [guidance, navigation, and control][ref_gnc] that decides where the
aircraft should go, works out where it actually is, and closes the gap
between the two, all the way down to an automatic landing.
One idea organizes the whole subject.
Every loop drives an error to zero, the error between the state the aircraft
is commanded to hold and the state it is estimated to be in,
so navigation supplies the estimate, guidance supplies the command, and
control nulls the difference.
The loops are stacked by speed, a fast inner loop inside a slower outer loop
inside a slower mission loop,
and the automatic landing is simply the tightest of them, the case where the
tolerated error shrinks toward zero just as the ground arrives.
This piece is the capstone of the series, the layer that flies the aircraft
the [airframe][related_post_runway] gave shape to, that the
[dynamics article][related_post_dynamics] stabilized, and that the
[landing article][related_post_landing] receives at the surface.

## The Nested Loops

A capable [autopilot][ref_autopilot] is not one controller but a stack of
them.
The innermost loop, the subject of the dynamics article, holds pitch, roll,
and yaw and runs fastest.
Around it a guidance loop holds heading, altitude, and speed by commanding
attitudes to the inner loop, and around that a mission loop follows a route
of waypoints by commanding heading and altitude to the guidance loop.
The loops are separated in speed on purpose,
each outer loop running several times slower than the loop inside it,
so that the inner loop has settled before the outer one asks for anything
new and the two do not fight.
Each is usually a [proportional-integral-derivative controller][ref_pid] or a
small variant, closing its own error,
and the discipline of the whole design is to keep the separation wide enough
that the stack stays stable.
The loops are also digital, sampled at finite rates rather than run
continuously, the attitude loop at a few hundred hertz and the navigation and
guidance loops at tens,
and the sensor, processing, and actuator latency around each loop caps the
bandwidth it can reach, the same delay-limits-gain lesson the dynamics
article drew, now in the outer loops.
This nesting is why the dynamics article had to come first,
because no outer loop can fly well around an inner loop that is not already
well damped.

## Navigation, or Where Am I

Guidance is useless without an answer to where the aircraft is, and that
answer is an estimate, never a direct measurement.
A [satellite navigation][ref_gnss] receiver gives an absolute position whose
error is bounded but which can drop out, lag, or be denied,
while an [inertial navigation system][ref_ins] built on an
[inertial measurement unit][ref_imu] gives a smooth, high-rate position by
[dead reckoning][ref_dead_reckoning] from accelerations and rotation rates,
at the cost of a drift that grows without bound over time.
The two are complementary, so a [Kalman filter][ref_kalman]
[fuses][ref_sensor_fusion] them, leaning on the inertial solution between
satellite fixes and on the satellite fix to bound the inertial drift,
weighting each by its uncertainty and carrying that uncertainty forward as
part of the estimate.
The [pitot-static system][ref_pitot] adds airspeed and a barometric altitude,
and where centimeter accuracy is needed a
[real-time-kinematic correction][ref_rtk] sharpens the satellite fix.
The estimate is only as good as its start, so the inertial solution must be
aligned and the magnetometer calibrated before flight,
since a poor initialization biases everything the filter does afterward.
When the satellites are jammed or [spoofed][ref_spoofing] the estimate must
fall back on the drifting inertial solution or on
[vision and terrain-relative navigation][ref_visual_odometry],
which is the hardest open problem of the three letters.

## Guidance, or Where To Go

Guidance turns a route into commands the inner loops can fly.
The route is usually a list of waypoints joined by straight legs,
and the quantity that matters is the cross-track error, the perpendicular
distance from the aircraft to the leg it is meant to be on.
A [path-following guidance law][research_waypoint] commands a heading that
drives that error to zero, steering toward a point a fixed distance ahead on
the path,

$$ \chi_{\text{cmd}} = \chi_{\text{path}} - \tan^{-1}\!\frac{e_y}{L_1}, $$

where $e_y$ is the cross-track error and $L_1$ is the look-ahead distance
that sets how aggressively the aircraft cuts back to the line.
A short look-ahead corrects hard and risks oscillation, a long one corrects
gently and accepts a wider track,
which is the same damping-versus-response trade the dynamics article drew,
now one loop further out.
Loitering, holding, and the approach are all the same machinery with
different paths.

## Wind and the Ground Track

Guidance is complicated by the fact that the aircraft flies relative to the
air but is asked to follow a path over the ground.
The wind is the difference between the two, so the heading the nose points
and the course the aircraft actually tracks diverge by a crab angle,
and the [wind triangle][ref_wind_triangle] relates the airspeed and heading
to the wind and the resulting ground speed and course.
Guidance must therefore crab into the wind to hold a ground track,
and the integral term of the cross-track law does this on its own for a
steady wind, settling the aircraft at whatever crab cancels the drift.
Scale makes this acute, the same way it did for the runway and recovery
articles.
On a slow, small UAV the wind can be a large fraction of the airspeed,
so a strong enough wind leaves little ground speed into it and can stop the
aircraft from making a waypoint upwind at all,
and a gust is a fast disturbance the inner loop and its damping must reject
before the guidance even sees it.
The wind that sized the runway and shaped the recovery is thus the same wind
the guidance loop spends its authority against.

## Closing the Loop with Energy

The longitudinal half of the guidance loop is best understood as energy,
which ties this article to the rest of the series.
A [total energy control system][research_tecs] uses the throttle to set the
aircraft's total energy, the sum of its kinetic and potential energy,
and the elevator to distribute that energy between speed and height,
rather than the older scheme of throttle for speed and elevator for altitude
that fights itself on a climb or a descent.
This is exactly the energy budget the propulsion and the staged-propulsion
articles tracked, now regulated continuously in flight,
the autopilot deciding moment by moment how much energy to add and whether to
spend it as speed or as altitude.
Seeing the outer loop as energy management rather than as two independent
channels is what makes a coordinated climb, descent, and approach possible,
and it is the same accounting the whole series has kept.

## The Approach and the Automatic Landing

The automatic landing is the tightest loop, because the tolerated error
shrinks to a few meters and then to zero exactly as the margin for correction
runs out.
The [autoland][ref_autoland] sequence captures an approach course, tracks a
descending glideslope much as the
[instrument landing system][ref_ils] of crewed aviation does,
[flares][ref_flare] to arrest the sink rate in the last moment, and then
manages the rollout onto the interfaces the landing article described.
The height in the flare is too critical for a barometer, so a precise source
is needed, a [real-time-kinematic fix][ref_rtk], a
[radar altimeter][ref_radar_altimeter], or a vision system locked to the
runway,
and a fielded [automatic-landing system][research_ardupilot_autoland] of this
kind recovers a UAV onto a small strip with a success rate above ninety-nine
percent.
The lateral accuracy of the approach is what sets the runway width the runway
article sized, since the cross-track error at the threshold is the dispersion
the strip must contain,
so the guidance precision of this article and the physical sizing of the
earlier ones meet at the moment of touchdown.
The takeoff is the same machinery run forward and is the easier bookend.
An [automatic takeoff][research_ardupilot_takeoff] holds the runway heading
with the rudder, advances the throttle, rotates at a commanded speed, and
captures the climb-out, or for the launch devices of the recovery article
simply takes over from release at the first waypoint,
so the autopilot flies the whole profile from the start of the roll or the
end of the catapult to the touchdown the approach delivers.

## When the Loop Breaks

Autonomy is only as good as its behavior when a sensor or a link fails,
so a sound design plans the degraded modes before they are needed.
A loss of satellite navigation hands the estimate to the inertial solution
for as long as its drift allows, or to a vision-based return,
a loss of the command link triggers a return-to-launch or a loiter rather
than a runaway, and a [geofence][ref_geofencing] bounds where the aircraft is
permitted to be at all.
Sensor redundancy, several inertial units and more than one satellite
receiver, lets the fusion drop a faulty input rather than believe it,
and a flight-termination option of the kind the recovery article described
remains the last resort when nothing else will keep the aircraft safe.
The lesson the recovery and stability articles anticipated holds here too,
that the system must fail into a safe state rather than into an arbitrary one,
and for an autonomous aircraft that safe state is written into the guidance
itself.

## Scale and the UAV Case

The remarkable thing about the small UAV is that this entire stack runs on a
cheap, open board.
A [Pixhawk][ref_pixhawk]-class flight controller carries a microelectro-
mechanical inertial unit, a barometer, and a satellite receiver,
and runs an open-source autopilot such as [ArduPilot][ref_ardupilot] or its
peers that implements every loop above, the navigation filter, the waypoint
guidance, the total-energy control, and the automatic landing.
The small aircraft's faster natural modes, which the dynamics article noted,
demand that these loops run at an adequate rate, but the processing to do so
costs almost nothing today.
This is why an autonomous fixed-wing UAV is now ordinary rather than exotic,
the same guidance, navigation, and control that once filled an avionics bay
reduced to a board smaller than a hand,
flying the aircraft the rest of this series designed from launch to touchdown
without a pilot in the loop.
Autonomy is a spectrum rather than a switch, though,
from manual through stabilized and assisted modes to waypoint and full
automatic flight, with an operator supervising on the loop and able to take a
level of control back whenever the mission or a fault demands it.

## Putting Numbers to It

A worked example shows the loops at their characteristic speeds.
If the inner attitude loop is tuned to a bandwidth of about five radians per
second, the guidance loop around it is set perhaps ten times slower, near
half a radian per second, so the attitude has settled long before the
guidance asks for a new one.
For the cross-track law, a look-ahead of fifty meters and a cross-track error
of ten meters command a heading correction of
$\tan^{-1}(10 / 50) \approx 11$ degrees back toward the path,
firm but not violent.
The navigation estimate might carry a few meters of error on a bare satellite
fix, a few centimeters with a real-time-kinematic correction, and a drift of
meters per minute on the inertial solution alone once the satellites are
gone.
At the landing, a three-degree glideslope turns a one-meter height error into
about nineteen meters along the runway, $1 / \tan 3^\circ$,
and the lateral cross-track error at the threshold is the dispersion the
runway width must hold.
None of these is a final design, but together they show the single thread,
an error driven toward zero by a loop fast enough to catch it,
repeated at every scale from the attitude to the mission to the last meter
of the flare.

## Out of Scope

Several neighboring subjects are deliberately excluded.
The detailed mathematics of the Kalman filter and the estimation theory
behind the navigation solution are a discipline of their own,
and this article uses the estimate rather than deriving it.
The synthesis of the control laws and the selection of the gains belong to
the dynamics article and to control theory, and are named but not carried
out.
The command-and-control data link, the radio, the ground control station,
and their security are a separate subsystem that the series has not yet
treated and that deserves its own article.
The detect-and-avoid problem of sharing the airspace with other traffic, the
coordination of multiple vehicles, and the regulatory approval of autonomous
flight are beyond this scope,
as are the physical landing interfaces themselves, which are the subject of
the landing article this one delivers the aircraft to.

## Conclusion

Guidance, navigation, and automatic landing are the management of one error,
the gap between where the aircraft is estimated to be and where it is
commanded to be, driven to zero by a stack of loops nested by speed.
Navigation builds the estimate by fusing a drifting inertial solution with a
bounded satellite fix, guidance turns a route into a commanded heading and a
total-energy target, and control flies it, while the automatic landing is the
same machinery wound to its tightest tolerance at the surface.
Run on an open board no larger than a hand, this layer flies the aircraft the
rest of the series built, powered, energized, stabilized, and brought to the
ground, and it closes the set,
the vehicle that the first article shaped from foam and glass now able to
launch, navigate its mission, and land itself, with the whole flight read as
one budget of energy and one error driven steadily toward zero.

## References

- [Reference, ArduPilot][ref_ardupilot]
- [Reference, Autoland][ref_autoland]
- [Reference, Autopilot][ref_autopilot]
- [Reference, Dead Reckoning][ref_dead_reckoning]
- [Reference, Geofencing][ref_geofencing]
- [Reference, GPS Spoofing][ref_spoofing]
- [Reference, Guidance, Navigation, and Control][ref_gnc]
- [Reference, Inertial Measurement Unit][ref_imu]
- [Reference, Inertial Navigation System][ref_ins]
- [Reference, Instrument Landing System][ref_ils]
- [Reference, Kalman Filter][ref_kalman]
- [Reference, Landing Flare][ref_flare]
- [Reference, PID Controller][ref_pid]
- [Reference, Pitot-Static System][ref_pitot]
- [Reference, Pixhawk][ref_pixhawk]
- [Reference, Radar Altimeter][ref_radar_altimeter]
- [Reference, Real-Time Kinematic Positioning][ref_rtk]
- [Reference, Satellite Navigation][ref_gnss]
- [Reference, Sensor Fusion][ref_sensor_fusion]
- [Reference, Visual Odometry][ref_visual_odometry]
- [Reference, Wind Triangle][ref_wind_triangle]
- [Related Post, Dynamic Stability and Control for Fixed-Wing UAVs][related_post_dynamics]
- [Related Post, Landing Gear and the Physics of Touchdown for Fixed-Wing UAVs][related_post_landing]
- [Related Post, Launch and Recovery Systems for Fixed-Wing UAVs][related_post_recovery]
- [Related Post, Runway Sizing for Fixed-Wing UAVs][related_post_runway]
- [Research, Automatic Landing (ArduPilot Plane Documentation)][research_ardupilot_autoland]
- [Research, Automatic Takeoff (ArduPilot Plane Documentation)][research_ardupilot_takeoff]
- [Research, Total Energy Control System Flight Test (NASA)][research_tecs]
- [Research, Waypoint Guidance for Small UAVs (University of Washington)][research_waypoint]

[ref_ardupilot]: https://en.wikipedia.org/wiki/ArduPilot
[ref_autoland]: https://en.wikipedia.org/wiki/Autoland
[ref_autopilot]: https://en.wikipedia.org/wiki/Autopilot
[ref_dead_reckoning]: https://en.wikipedia.org/wiki/Dead_reckoning
[ref_geofencing]: https://en.wikipedia.org/wiki/Geofencing
[ref_spoofing]: https://en.wikipedia.org/wiki/GPS_spoofing
[ref_gnc]: https://en.wikipedia.org/wiki/Guidance,_navigation,_and_control
[ref_imu]: https://en.wikipedia.org/wiki/Inertial_measurement_unit
[ref_ins]: https://en.wikipedia.org/wiki/Inertial_navigation_system
[ref_ils]: https://en.wikipedia.org/wiki/Instrument_landing_system
[ref_kalman]: https://en.wikipedia.org/wiki/Kalman_filter
[ref_flare]: https://en.wikipedia.org/wiki/Landing_flare
[ref_pid]: https://en.wikipedia.org/wiki/PID_controller
[ref_pitot]: https://en.wikipedia.org/wiki/Pitot-static_system
[ref_pixhawk]: https://en.wikipedia.org/wiki/Pixhawk
[ref_radar_altimeter]: https://en.wikipedia.org/wiki/Radar_altimeter
[ref_rtk]: https://en.wikipedia.org/wiki/Real-time_kinematic_positioning
[ref_gnss]: https://en.wikipedia.org/wiki/Satellite_navigation
[ref_sensor_fusion]: https://en.wikipedia.org/wiki/Sensor_fusion
[ref_visual_odometry]: https://en.wikipedia.org/wiki/Visual_odometry
[ref_wind_triangle]: https://en.wikipedia.org/wiki/Wind_triangle
[related_post_dynamics]: {% post_url 2026-06-06-dynamic_stability_and_control_for_fixed_wing_uavs %}
[related_post_landing]: {% post_url 2026-06-07-landing_gear_and_the_physics_of_touchdown_for_fixed_wing_uavs %}
[related_post_recovery]: {% post_url 2026-06-01-launch_and_recovery_systems_for_fixed_wing_uavs %}
[related_post_runway]: {% post_url 2026-05-31-runway_sizing_for_fixed_wing_uavs %}
[research_ardupilot_autoland]: https://ardupilot.org/plane/docs/automatic-landing.html
[research_ardupilot_takeoff]: https://ardupilot.org/plane/docs/automatic-takeoff.html
[research_tecs]: https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19870017485.pdf
[research_waypoint]: https://www.aa.washington.edu/sites/aa/files/research/afsl/publications/osborne2005waypoint.pdf
