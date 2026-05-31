---
layout: post
mathjax: true
comments: true
title:  "Runway Sizing for Fixed-Wing UAVs"
date:   2026-05-31 09:00:00 +0000
categories: aerospace engineering uav
---

<!-- A114 -->
<script>console.log("A114");</script>

A fixed-wing unmanned aerial vehicle needs ground to accelerate to flying
speed and ground to slow back down, and the question of how much ground
has a surprisingly structured answer.
One variable dominates, namely the speed the aircraft must reach,
because the distance to reach a speed grows with the square of that speed.
Everything else, the runway slope, the surface, the wind,
the air density, and the aircraft's own planform,
acts by changing either that speed or the acceleration available to reach it.
This article works through runway sizing for small and medium fixed-wing
UAVs in that order, from the master variable outward,
and gives formulae meant to be plugged with a particular aircraft's numbers.
A companion article covers
[building the airframe itself][related_post_lwpla].

## The Master Variable

A wing flies when it can carry the aircraft's weight,
and the slowest speed at which it can do so is the stall speed,

$$ V_{\text{stall}} = \sqrt{\frac{2W}{\rho\,S\,C_{L,\max}}}, $$

where $W$ is weight, $\rho$ is air density, $S$ is wing area,
and $C_{L,\max}$ is the maximum [lift coefficient][ref_lift_coefficient].
An aircraft lifts off a little above this, at roughly

$$ V_{LO} \approx 1.1\,V_{\text{stall}}, $$

and lands a little above it as well.
Because a ground roll is the distance to accelerate to a speed,
and that distance scales with the square of the speed,
the runway length scales as

$$ s \;\propto\; V_{LO}^2 \;\propto\; \frac{W/S}{\rho\,C_{L,\max}}. $$

This single proportionality is the spine of the whole subject.
Runway length rises with [wing loading][ref_wing_loading] $W/S$,
falls with air density $\rho$, and falls with the maximum lift coefficient.
Every later section is a refinement of it.
The proxy worth carrying in your head is wing loading,
because for a given airfoil and air it sets the stall speed,
and the stall speed squared sets the runway.

This is also how raw size enters, by way of the
[square-cube law][ref_square_cube].
If a design is scaled up while keeping its shape and construction,
its wing area grows with the square of the length
and its weight grows with the cube,
so wing loading rises in direct proportion to the linear scale.
A geometrically [doubled model carries roughly double the wing loading][research_rcsd_scaling]
if it is built the same way,
which raises the stall speed by about forty percent
and the runway by about double.
Larger aircraft therefore want longer runways not as a separate rule
but as a consequence of the same proportionality,
and the lever a designer has against it is to break the scaling,
by building lighter in proportion or by adding wing area faster than length,
so that wing loading does not climb as fast as raw size would dictate.

## Level Runways and the Ground Roll

On level ground the takeoff roll is the distance to accelerate
from rest to $V_{LO}$ under the net of thrust, drag, and rolling friction.
A useful first cut neglects aerodynamic drag and lift during the roll,
which partly cancel, and treats the acceleration as constant,

$$ s_g \approx \frac{V_{LO}^2}{2\,\bar a}, \qquad
   \bar a = g\left(\frac{T}{W} - \mu_r\right), $$

where $T/W$ is the thrust-to-weight ratio and $\mu_r$ is the
rolling-friction coefficient.
Substituting the liftoff speed gives the form to plug numbers into,

$$ s_g \approx \frac{1.21\,(W/S)}{\rho\,C_{L,\max}\,g\,\left(\dfrac{T}{W} - \mu_r\right)}. $$

The [parameters that matter][research_erau_to] are exactly the three
in that expression, wing loading, thrust-to-weight, and maximum lift
coefficient, plus the friction of the surface.
A more exact figure requires integrating the speed-dependent forces,
because there is [no closed-form solution to the full equations][research_vt_to],
but the constant-acceleration estimate is close enough to size a runway
and to compare designs.

## Paved Versus Dirt

The surface enters through the friction coefficient $\mu_r$ and through firmness.
On [dry pavement the rolling coefficient is about 0.02 to 0.04][research_erau_to].
Firm grass or packed dirt runs higher, roughly 0.05 to 0.10,
and soft or wet ground higher still, which lengthens the roll
by enlarging the friction term that opposes acceleration.
A [soft surface also costs energy that never returns][ref_slope_surface],
unlike a slope, so it penalizes both takeoff and landing.
Two non-numerical concerns ride along with the surface.
Loose dirt and gravel raise foreign-object risk to the propeller and airframe,
and an unpaved strip's bearing strength limits how heavy a UAV it can carry
without rutting, which couples back to wing loading and tire choice.
Pavement removes both worries at the cost of preparation,
so the practical rule is that an unpaved strip must be longer than the
formula's paved figure, by a margin that grows with how soft it is.

## Inclined Runways

A sloped runway adds a component of gravity along the direction of travel.
For a slope angle $\gamma$ the effective acceleration becomes

$$ \bar a_{\text{eff}} = g\left(\frac{T}{W} - \mu_r\right) \mp g\sin\gamma, $$

with the minus sign for an uphill takeoff and the plus for a downhill one.
The practical consequences are firm.
[Take off downhill and land uphill][ref_slope_surface] when the slope is
appreciable and the wind does not forbid it,
because the downhill grade adds to acceleration on takeoff
and the uphill grade adds to deceleration on landing.
A common field rule of thumb is that
[one percent of slope changes takeoff distance by about five percent
and landing distance by about ten percent][ref_slope_surface].
On a one-way sloped strip the slope can override the wind,
so a downhill-into-a-tailwind departure is sometimes the right choice,
and the two effects can be weighed in the same acceleration balance.

## Ski-Jump Runways

A ski jump trades runway length for an upward launch.
At the ramp exit the aircraft gains a vertical velocity of about

$$ v_z \approx V_e \sin\theta, $$

where $V_e$ is the speed leaving the ramp and $\theta$ is the ramp angle.
That vertical velocity buys
[ballistic airborne time of roughly $2 v_z / g$][ref_ski_jump]
during which the aircraft keeps accelerating toward flying speed
rather than needing to have reached it on the ground.
The result is that liftoff can occur at a lower horizontal speed,
which for [carrier jets is thirty to fifty percent below a flat run][ref_ski_jump].
For a thrust-limited UAV the gain is smaller, because the benefit
depends on continuing to accelerate while airborne,
but a ramp is a genuine way to launch from a short strip.
The costs are mechanical.
The ramp imposes a pitch rate and a landing-gear load,
which is why carrier ramps curve gradually over tens of meters,
and a UAV ramp must respect the same limits at its own scale.

## Wind

Wind is the cheapest runway length there is.
An aircraft flies relative to the air, so a headwind $V_w$ means it only
has to accelerate over the ground to $V_{LO} - V_w$,
and the ground roll shrinks roughly as

$$ s_g(V_w) \approx s_g(0)\left(1 - \frac{V_w}{V_{LO}}\right)^2. $$

A tailwind does the reverse and lengthens the roll sharply,
which is why operations face into the wind whenever possible.
Wind also constrains placement, not only length.
A runway should be aligned with the prevailing wind
so that the usual condition is a headwind rather than a crosswind,
and the [crosswind component][ref_crosswind] is

$$ V_{\text{cross}} = V\sin\psi, \qquad V_{\text{head}} = V\cos\psi, $$

where $\psi$ is the angle between the wind and the runway.
The crosswind component, not the total wind, is what bounds a safe launch,
so a site with a steady wind from one quarter wants its runway pointed there,
and a site with variable wind may want more than one orientation
or a wider tolerance built into the airframe and the autopilot.

How much crosswind the aircraft can use on the ground depends on its
landing-gear layout, which is part of the airframe rather than the field.
A [tricycle arrangement][ref_tricycle_gear], with the main wheels behind
the center of gravity and a nose wheel ahead of it,
is directionally stable on the roll and forgiving in a crosswind,
because a small yaw tends to correct itself.
A taildragger, with its center of gravity behind the mains,
is the opposite, since a yaw tends to grow,
and a crosswind can start a [ground loop][ref_ground_loop] in which the
aircraft pivots about a main wheel and departs the runway.
A UAV that must operate from a crosswind-prone strip therefore favors
tricycle gear and a wider track,
and the crosswind limit that gear sets feeds back into how forgiving the
runway orientation has to be.

## Orientation

Orientation follows from wind, and the cardinal labels are a proxy for it.
A north-south versus east-west choice is really a choice to align
with the prevailing wind, so the right axis is whichever one most often
puts the wind on the nose.
Full-scale [runways are even named for their magnetic heading][ref_runway],
a runway pointing 090 degrees being Runway 9,
and they are renumbered as the magnetic field drifts,
which is a reminder that the orientation that matters is set by the air,
not by the map.

The rotation of the Earth deserves a brief, dismissive note,
because it is a real effect in a neighboring field and a non-effect here.
At the speeds and length scales of a UAV runway
the Coriolis acceleration is negligible,
and the eastward velocity that the rotating Earth confers,
which makes equatorial east-facing sites valuable for orbital launch,
does nothing for an aircraft that climbs away under its own power
and is referenced to the moving air around it.
That argument belongs to astronautics and is out of scope here.

## Density Altitude and Ambient Conditions

Air density is in the denominator of every distance in this article,
so the conditions that thin the air lengthen the runway.
[Density altitude is pressure altitude corrected for temperature][ref_density_altitude],
and it rises with field elevation, with heat, and slightly with humidity.
Thin air lengthens the roll twice over.
It raises the true speed needed for liftoff,
since $V_{\text{stall}}$ grows as $1/\sqrt{\rho}$,
and it cuts the thrust a propeller or a small turbine can make,
which shrinks the acceleration.
To first order the ground roll scales as

$$ s_g \;\propto\; \frac{1}{\rho}, $$

and the thrust loss makes the real penalty worse.
The effect is large enough to plan around.
A [hot, high field can add tens of percent to the takeoff roll][research_faa_da]
relative to a cool day at sea level,
so a runway sized only for standard conditions
can become too short on a summer afternoon at altitude.

## Obstacle Clearance and Margins

A runway is not only the ground roll.
The aircraft must also clear whatever sits beyond the end,
and the figure that governs sizing is the distance to lift off
and climb to a screen height, conventionally fifty feet or about fifteen meters.
The total takeoff distance is the ground roll plus an airborne segment,

$$ s_{\text{total}} = s_g + \frac{h}{\tan\gamma_{\text{climb}}}, $$

where $h$ is the screen height and $\gamma_{\text{climb}}$ is the
initial climb angle, itself set by excess thrust.
A weak climb angle can make the obstacle distance,
not the ground roll, the binding constraint.
Real practice then multiplies by a safety factor,
since engines underperform, pilots and autopilots are imperfect,
and surfaces vary, and a margin of twenty to fifty percent over the
computed distance is ordinary rather than cautious.
The honest runway length is the obstacle-clearing distance with the margin,
not the bare ground roll the first formula gives.
One margin is worth naming on its own.
If the design must be able to abort a takeoff and stop on the remaining
runway, the field has to hold the distance to accelerate to a decision
speed and then brake to a halt, which is generally longer than either the
plain ground roll or the landing roll.
Sizing for that stopping case is a deliberate choice rather than a default,
since many small UAVs simply accept that past a certain point the takeoff
is committed.
The formal version of this trade, the
[balanced field length][ref_balanced_field] that equates the
continue-and-climb distance with the accelerate-and-stop distance,
is a certified-transport method left out of scope below,
but the underlying idea, that rejecting a launch needs runway reserved for it,
belongs in the margin a UAV builder picks.

## Landing

Landing reverses the problem and is often the longer of the two.
The approach is flown near $1.3\,V_{\text{stall}}$ and the aircraft touches
down a little slower, after which the landing roll is the distance to stop,

$$ s_{\text{land}} \approx \frac{V_{TD}^2}{2\,\mu_b\,g}, $$

where $V_{TD}$ is the touchdown speed and $\mu_b$ is the braking
coefficient, around 0.3 to 0.5 on dry pavement and less on grass or when wet.
Because the touchdown speed is tied to the same stall speed as takeoff,
the same proportionality to wing loading and density and lift coefficient holds,
and the same obstacle and margin logic applies on the approach end.
Slope and wind enter exactly as before, with the signs that favor
landing uphill and into the wind.
A UAV that brakes poorly, or that has no brakes and relies on aerodynamic
and rolling drag alone, needs the landing case computed with its real
deceleration, because that case will frequently size the field.

Near the ground the wing also enters [ground effect][ref_ground_effect],
where the surface squashes the trailing vortices and cuts induced drag.
The reduction is slight when the wing is more than a span above the surface
but reaches tens of percent within a fraction of a span,
so on landing the aircraft tends to float and bleed speed slowly,
which lengthens the roll if the approach is even slightly fast,
and on takeoff it gives a brief assist that fades as the aircraft climbs.
It is a second-order effect that the margin normally absorbs,
but it is worth naming because it acts on the landing flare,
the phase most likely to size the field.

## Width and the Lateral Dimension

Length is the headline number, but a runway also has a width,
and width is set by different drivers than length.
The first is the crosswind already discussed,
since an aircraft that touches down crabbing or drifting needs lateral room,
and the [crosswind component][ref_crosswind] that the airframe can hold
translates into how far off the centerline a gust can push it.
The second is the landing gear, because a wider main-wheel track is more
stable against the yaw that starts a ground loop,
and a wider track wants a wider prepared surface.
The third driver is specific to an unmanned aircraft, namely the lateral
accuracy of its guidance.
An autopilot tracking a runway has a finite lateral navigation error,
and the touchdown point scatters around the aim point from approach to approach,
so the width must cover that [touchdown dispersion][research_uav_landing]
the way the length covers the stopping distance.
A precise guidance mode, differential satellite positioning or a vision
system locked to the runway edges, shrinks the dispersion and allows a
narrower strip, while a coarse mode demands either a wider strip or a
tighter crosswind limit.
The detailed runway-width design standards used in civil airport
engineering are out of scope here, but the sizing logic is the same,
in that the lateral dimension must hold the worst expected sum of drift,
gear track, and guidance error with a margin.

## Takeoff and Landing, or Only One Phase

A runway that must serve both takeoff and landing is sized by the longer
of the two distances, with margins, at the worst expected density altitude
and wind.
Many UAVs, however, use the runway for only one phase.
An aircraft launched by catapult, by a booster, by a vertical-lift mode,
or off a ramp may need the runway only to land,
and an aircraft that recovers into a net, by parachute, or on a belly skid
may need the runway only to take off.
In those cases the field is sized for the phase that uses it,
which is the lever that makes short-strip and runway-independent operation possible.
Fielded systems span the whole range.
The [ScanEagle][ref_scaneagle] uses no runway at all,
launching from a pneumatic catapult and recovering by snagging a
suspended cable, so its ground requirement is the footprint of the
launcher and the recovery mast rather than a strip.
The [RQ-7 Shadow][ref_rq7] launches from a catapult as well
but lands on a short prepared strip with arresting gear,
so the runway it needs is sized by the recovery phase alone.
At the other end the [MQ-9 Reaper][ref_mq9] takes off and lands
conventionally on its own wheels and is quoted as needing a runway of
roughly five thousand feet when flown manually and about three thousand
when takeoff and landing are automated,
which shows how directly the ground-roll and margin logic of this article
sizes a real aircraft.
The design question is therefore not only how long a runway must be,
but whether the aircraft should depend on one for a given phase at all,
and the formulae above size whichever phases remain on the ground.
A diverting or alternate field is just a runway sized by this same logic
for the heaviest, hottest, least favorable case the mission allows.

## Planform and Airframe Implications

The aircraft's planform sets the lift coefficient and the geometry of
rotation, and both feed the master variable.
A conventional configuration with flaps reaches the highest
maximum lift coefficient, often well above two with flaps deployed,
which lowers the stall speed and shortens the runway directly.
A [pure delta][ref_delta] behaves differently.
It makes much of its lift from a [leading-edge vortex][ref_vortex_lift]
rather than attached flow, so its lift keeps rising to a very high
angle of attack, on the order of thirty-five degrees,
but it reaches a usable maximum lift coefficient only by rotating to a
steep attitude that demands long landing gear and risks a tail strike,
and at moderate ground attitudes its lift coefficient is modest,
so it tends to take off and land fast and long.
A [tailless flying wing][ref_flying_wing] is more constrained still,
because it carries no flaps and trims with reflex or washout that costs
lift, and it has limited pitch authority to rotate,
so its maximum usable lift coefficient is low and its runway is long
for its size.

The variables that matter reduce to a short list,
and each has a convenient proxy.
The maximum lift coefficient and the wing loading together set the stall
speed, and the stall speed squared sets the runway,
so wing loading is the single best proxy for runway length within a
configuration.
The thrust-to-weight ratio sets the acceleration and so the ground roll
at a given liftoff speed.
The ground attitude limit, how far the aircraft can rotate before the
tail or the propeller strikes, caps the lift coefficient that the
planform's potential can actually be used at.
An exotic configuration is then read through these same variables.
Whatever it does to lift coefficient, wing loading, thrust-to-weight,
and rotation geometry is what it does to the runway,
and a design that scores poorly on lift coefficient or rotation,
as deltas and flying wings tend to,
pays for it in field length unless it also lowers its wing loading
or raises its thrust to compensate.

## Putting Numbers to It

A worked example threads the formulae together.
Take a UAV of mass $25$ kilograms, so $W \approx 245$ newtons,
with a wing area of $1.0$ square meter, a maximum lift coefficient of $1.4$,
a thrust-to-weight ratio of $0.35$, and tires on firm grass at $\mu_r = 0.06$,
at a sea-level density of $1.225$ kilograms per cubic meter.
The stall speed is
$\sqrt{2 \times 245 / (1.225 \times 1.0 \times 1.4)} \approx 16.9$ meters per second,
the liftoff speed is about $18.6$ meters per second,
and the level ground roll is
$1.21 \times 245 / (1.225 \times 1.4 \times 9.81 \times (0.35 - 0.06)) \approx 61$ meters.
Add the climb to a fifteen-meter obstacle at a six-degree initial climb,
about $15 / \tan 6^\circ \approx 143$ meters of air distance,
and a forty percent margin, and the takeoff field is on the order of
$1.4 \times (61 + 143) \approx 290$ meters.
Now move the same aircraft to a two-thousand-meter-elevation field
on a hot day, where the density might be near $0.95$ kilograms per cubic meter.
The ground roll scales by about $1.225 / 0.95 \approx 1.3$ before the
thrust loss is even counted, so the field grows accordingly.
Give it a five-meter-per-second headwind instead,
and the roll shrinks by $(1 - 5/18.6)^2 \approx 0.54$, almost halving it.
None of these numbers is the final word,
but together they place the design and show which lever,
density, wind, surface, or planform, is the one worth pulling.

## Lighting, Reflectors, and Markings

A strip also has to be seen, by an observer, by a safety pilot, or by an
optical sensor on the aircraft, and how it is marked is part of provisioning it.
In clear daylight a visual-line-of-sight flight from a known field may need
nothing beyond a recognizable surface.
Beyond that case the aids are at first optional and then, past a threshold,
required.
On the optional end, low-cost passive markers go a long way.
[Retroreflective edge and threshold markers][ref_retroreflective] need no
power and define the strip for landing lights or a camera at dusk,
and a [portable, battery-powered expeditionary lighting set][ref_eals]
defines an austere strip that has no installed infrastructure.
These are conveniences a daytime operation can choose or skip.
They stop being optional in two situations worth calling out.
First, a runway used at night or in low visibility is generally required to
carry [edge, threshold, and runway-end lighting][ref_runway_lighting]
that defines its extent, so a field intended for night recovery must be
sized and equipped for that lighting, not only for the ground roll.
Second, the requirement can attach to the aircraft rather than the field.
Under the United States small-UAV rule, for instance,
[night operation requires anti-collision lighting on the aircraft visible
for three statute miles][research_part107_29],
which is mandatory regardless of how the runway itself is marked.
The detailed photometric design, the color coding, and the spacing of
airfield lighting and markings are a specialty of their own and are out of
scope here, but whether lights and reflectors are present at all,
and whether they are optional or required, is a sizing-stage decision.

## Out of Scope

A few neighboring subjects are deliberately excluded.
Orbital and astronautical launch, including the Earth-rotation velocity
argument noted above, is a different problem with different physics.
The civil-engineering design of the runway itself, its pavement structure,
drainage, and bearing strength beyond the rolling-resistance effect,
is a specialty of its own.
Full certification methods, the balanced field length and
accelerate-stop analysis used for crewed transport aircraft,
are heavier than UAV sizing usually warrants and are only gestured at here.
And the detailed design of catapults, arrestor nets, parachutes, and
vertical-lift systems is named where it bears on which phase needs a runway
but is not engineered in this article.
The photometric and color-coding design of airfield lighting and markings,
and the civil-airport runway-width design standards,
are referenced for the sizing decisions they drive but are not specified here.
The guidance and navigation system that flies the approach,
whose lateral accuracy sets the touchdown dispersion the width must hold,
is likewise treated only as an input and not designed.

## Conclusion

Runway sizing for a fixed-wing UAV is the management of one squared speed.
The stall speed, set by wing loading, air density, and maximum lift
coefficient, fixes the liftoff and touchdown speeds,
and the runway grows with the square of those.
Slope, surface, wind, and density altitude each adjust the distance
through the acceleration or the speed in a way the formulae make explicit,
a ski jump and a downhill grade and a headwind all buying length,
a soft surface and thin air and a low-lift planform all spending it.
Size for the longer of takeoff and landing, at the worst conditions,
with a margin to clear the obstacle, and the result is a field length
a builder can defend with numbers rather than guess at.

## References

- [Reference, AAI RQ-7 Shadow][ref_rq7]
- [Reference, Balanced Field Takeoff][ref_balanced_field]
- [Reference, Boeing Insitu MQ-27 ScanEagle][ref_scaneagle]
- [Reference, Crosswind Component][ref_crosswind]
- [Reference, Delta Wing][ref_delta]
- [Reference, Density Altitude][ref_density_altitude]
- [Reference, Expeditionary Airfield Lighting System][ref_eals]
- [Reference, Flying Wing][ref_flying_wing]
- [Reference, General Atomics MQ-9 Reaper][ref_mq9]
- [Reference, Ground Effect][ref_ground_effect]
- [Reference, Ground Loop in Aviation][ref_ground_loop]
- [Reference, Lift Coefficient][ref_lift_coefficient]
- [Reference, Retroreflective Runway Markers][ref_retroreflective]
- [Reference, Runway][ref_runway]
- [Reference, Runway Lighting][ref_runway_lighting]
- [Reference, Runway Slope and Surface][ref_slope_surface]
- [Reference, Ski-Jump in Aviation][ref_ski_jump]
- [Reference, Square-Cube Law][ref_square_cube]
- [Reference, Tricycle Landing Gear][ref_tricycle_gear]
- [Reference, Vortex Lift][ref_vortex_lift]
- [Reference, Wing Loading][ref_wing_loading]
- [Related Post, Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass][related_post_lwpla]
- [Research, Accelerated Performance, Takeoff and Landing][research_vt_to]
- [Research, Density Altitude (FAA)][research_faa_da]
- [Research, Operation at Night (14 CFR 107.29)][research_part107_29]
- [Research, Precision Runway Landing for UAVs][research_uav_landing]
- [Research, Square-Cube Law and Scaling for RC Sailplanes][research_rcsd_scaling]
- [Research, Takeoff and Landing Performance][research_erau_to]

[ref_balanced_field]: https://en.wikipedia.org/wiki/Balanced_field_takeoff
[ref_crosswind]: https://aerotoolbox.com/crosswind/
[ref_delta]: https://en.wikipedia.org/wiki/Delta_wing
[ref_density_altitude]: https://en.wikipedia.org/wiki/Density_altitude
[ref_eals]: https://www.avlite.com/product/expeditionary-airfield-lighting-system-eals/
[ref_flying_wing]: https://en.wikipedia.org/wiki/Flying_wing
[ref_ground_effect]: https://en.wikipedia.org/wiki/Ground_effect_(aerodynamics)
[ref_ground_loop]: https://en.wikipedia.org/wiki/Ground_loop_(aviation)
[ref_lift_coefficient]: https://en.wikipedia.org/wiki/Lift_coefficient
[ref_mq9]: https://en.wikipedia.org/wiki/General_Atomics_MQ-9_Reaper
[ref_retroreflective]: https://flightlight.com/products/runway-taxiway-retroreflective-markers-faa-l-853/
[ref_rq7]: https://en.wikipedia.org/wiki/AAI_RQ-7_Shadow
[ref_runway]: https://en.wikipedia.org/wiki/Runway
[ref_runway_lighting]: https://skybrary.aero/articles/runway-lighting
[ref_scaneagle]: https://en.wikipedia.org/wiki/Boeing_Insitu_MQ-27_ScanEagle
[ref_slope_surface]: https://www.boldmethod.com/learn-to-fly/performance/runway-surface-and-slope/
[ref_ski_jump]: https://en.wikipedia.org/wiki/Ski-jump_(aviation)
[ref_square_cube]: https://en.wikipedia.org/wiki/Square%E2%80%93cube_law
[ref_tricycle_gear]: https://en.wikipedia.org/wiki/Tricycle_landing_gear
[ref_vortex_lift]: https://en.wikipedia.org/wiki/Vortex_lift
[ref_wing_loading]: https://en.wikipedia.org/wiki/Wing_loading
[related_post_lwpla]: {% post_url 2026-05-30-prototyping_fixed_wing_aircraft_with_lightweight_pla_and_fiberglass %}
[research_vt_to]: https://pressbooks.lib.vt.edu/aerodynamics/chapter/chapter-7-accelerated-performance-takeoff-and-landing/
[research_faa_da]: https://www.faasafety.gov/files/events/NM/NM07/2023/NM07120280/FAA-P-8740-02-DensityAltitude.pdf
[research_part107_29]: https://www.ecfr.gov/current/title-14/chapter-I/subchapter-F/part-107/subpart-B/section-107.29
[research_uav_landing]: https://www.uavnavigation.com/company/blog/uav-navigation-depth-precision-runway-landing-without-dgpsrtk
[research_rcsd_scaling]: https://www.rcsoaringdigest.com/SquareCube.html
[research_erau_to]: https://eaglepubs.erau.edu/introductiontoaerospaceflightvehicles/chapter/takeoff-landing-performance/
