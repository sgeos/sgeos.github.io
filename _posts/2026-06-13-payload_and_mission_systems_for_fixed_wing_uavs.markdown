---
layout: post
mathjax: true
comments: true
title:  "Payload and Mission Systems for Fixed-Wing UAVs"
date:   2026-06-13 09:00:00 +0000
categories: aerospace engineering uav
series: fixed_wing_uav
series_title: Fixed-Wing UAV
series_index: 15
---
<!-- A130 -->
<script>console.log("A130");</script>

Every article in this series so far has been about the aircraft, the airframe
and the propulsion and the energy and the control that get a vehicle into the
air and bring it back.
This article is about the reason the vehicle flies at all, the
[payload][ref_payload] it carries and the mission system that uses it.
One idea organizes the subject, that the payload is the point and everything
else is overhead, so the design question is how much of the mass, the volume,
the power, the data, and the energy budget the whole series has tracked actually
reaches the payload rather than being spent to carry it.
An unmanned aircraft is a bus, and the mission is the payload's, so the platform
exists to deliver the payload to the right place at the right time in the right
condition, whether that condition is a steady stare at a point on the ground or
a release at the top of a climb to space.
This article catalogs what the payload can be, how it couples to the platform,
and, at its far end, the case the human pilot was never part of, a suborbital
carrier that delivers a payload to the edge of orbit and leaves the
circularization to the payload itself.

## The Payload Fraction

The first measure of a mission aircraft is how much of it is payload.
The payload fraction is

$$
 f_{pl} = \frac{m_{payload}}{m_{takeoff}}, 
\tag{1}
$$

and it competes directly against the structure fraction the
[structures article][related_post_structures] budgeted and the fuel or battery
fraction the energy articles budgeted, since
the three together with everything else must sum to one.
The fuller accounting is the size, weight, power, and cost of the payload, the
figure of merit a mission designer carries, because a payload claims not only
mass but volume in the airframe, electrical power from the generation the
[energy article][related_post_electric] sized, a share of the data link the
[communications article][related_post_comms] sized, and a budget of money.
A heavier or hungrier payload is paid for in the range and endurance and cost of
the platform, so the central trade of a mission aircraft is the same balance the
series has drawn throughout, now with the payload on one side and the entire
rest of the aircraft on the other.

## A Taxonomy of Payloads

Payloads divide by what they do.
The sensing payloads gather information and dominate the unmanned world, the
electro-optical and [infrared][ref_flir] cameras that see by day and by heat,
the [synthetic-aperture radar][ref_sar] that images through cloud and darkness,
the [signals-intelligence][ref_sigint] receivers that listen, the
[lidar][ref_lidar] that ranges, and the
[multispectral][ref_multispectral] and [hyperspectral][ref_hyperspectral]
imagers that separate materials by their spectra, the whole set serving the
[surveillance][ref_istar] and [reconnaissance][ref_aerial_recon] mission that is
the most common reason a UAV exists.
The relay payloads carry the communications of the data-link article outward,
turning the aircraft into the airborne repeater that extends a network beyond
the horizon.
The delivery payloads carry mass to a place, the parcel of the
[delivery drone][ref_delivery_drone], the chemicals of the
[agricultural drone][ref_agricultural_drone], and the medical or logistic
resupply that an aircraft can place where a vehicle cannot reach.
The effector payloads act on the world rather than observe it, the warhead of
the [loitering munition][ref_loitering_munition] whose terminal maneuver the
[aerobatics article][related_post_aerobatics] priced, where the payload and the
aircraft become one
expendable object.
And the scientific payloads sample the atmosphere and the field, the instruments
that make the aircraft a flying laboratory.

## Integrating the Payload with the Platform

A payload is not carried for free, and several budgets bind its integration.
The mass and its placement set the center of gravity the stability article
required to stay within a range, so a heavy gimbal in the nose or a store on a
wing pylon must be balanced, and a payload that moves or is released shifts the
center of gravity in flight.
The electrical power the payload draws is part of the hotel load the
energy-systems article budgeted, a continuous demand that competes with
propulsion for the same generation and storage, and some payloads, a radar or a
laser or a transmitter, draw a peak power far above their average that the
supply must meet even though the energy budget is set by the average.
The data the payload produces is the fat downlink stream of the communications
article, often the largest flow the aircraft carries, which sets whether the
information is sent down live or recorded to onboard storage and
[compressed][ref_data_compression] to fit, the compression buying link capacity
at the cost of the latency the communications article described.
The heat the payload makes must be carried away, and the volume it occupies must
be found in the airframe, on a [hardpoint][ref_hardpoint] under a wing, in an
internal bay, or in a gimbal beneath the fuselage.
The vibration of the engine and the airframe reaches the payload too, blurring a
sensor and loosening a mounting, so a sensitive payload rides on
[vibration isolation][ref_vibration_isolation] that the integration must find
room and mass for.
The mass, the power, the data, the heat, the volume, and the vibration are the
currency in which the platform pays for what the payload does.

## Pointing and Stabilization

A sensing payload is only as good as its ability to hold its aim.
A camera or a radar on a maneuvering aircraft sees a line of sight that the
motion of the airframe is constantly disturbing, so the payload is carried on a
[gimbal][ref_gimbal] that isolates it from the attitude motion of the dynamics
article and holds its aim on a point while the aircraft moves.
The [stabilization][ref_image_stabilization] rejects the airframe rates measured
by the same inertial sensors the guidance article used for navigation, and the
residual jitter sets the sharpness of the image and the accuracy of the
geolocation.
The product the payload actually delivers is often not the image but the
coordinate, the [georeferenced][ref_georeferencing] location of what it sees,
and that location is no better than the chain that produces it, the navigation
solution of the guidance article, the measured gimbal angles, and the terrain
model together setting a target-location error that is the real figure of merit
for a sensing mission.
The geometry the payload sees follows from the platform, since the altitude sets
the footprint and the standoff range, the speed sets how long a point stays in
view, and the steadiness of the aircraft sets how hard the gimbal must work, so
the pointing problem couples the payload back to the flight the rest of the
series designed.

## The Mission System

The payload is the sensor, and the mission system is everything that turns its
output into a result.
The mission system tasks the payload, pointing it at what matters and managing
its modes, and it takes in what the payload produces and decides what to do with
it.
The central choice is where the processing happens, aboard the aircraft at the
[edge][ref_edge_computing] or on the ground after the downlink, a trade between
the latency the communications article described and the limited power and mass
a payload computer may have.
An aircraft that processes aboard can detect and track and classify on its own,
fusing several sensors into one picture through the
[sensor fusion][ref_sensor_fusion] that combines what each sensor sees best, and
it can act on the result within the autonomy spectrum the
[guidance article][related_post_gnc] drew, from reporting a detection to closing
a loop on it.
The mission system is therefore the bridge between the payload and the autonomy,
the part that makes the aircraft useful rather than merely present.

## The Payload Sizes the Aircraft

The deepest coupling runs the other way, from the payload back to the platform.
A surveillance mission that must stare at a point for hours demands the
endurance the energy article budgeted, a mission that must see a wide area
demands the altitude that sets the footprint, a mission that must arrive quickly
demands the dash speed the propulsion article sized, and a mission that must
hold a steady aim demands the calm airframe the stability article tuned.
The sharpest instance of the coupling is physical, since the
[angular resolution][ref_angular_resolution] of a sensor is set by the ratio of
its wavelength to its aperture, so a larger aperture is needed to resolve a given
detail at a given range, and the
[ground resolution][ref_ground_sample_distance] at the standoff distance
therefore drives the aperture, hence the size and mass of the payload, hence the
aircraft.
This is why a small UAV with a small aperture cannot simply stand off as far as
a large one and see the same detail, the diffraction limit tying the mission
geometry to the payload size and the payload size to the platform.
The payload writes the requirement and the rest of the aircraft is sized to meet
it, which is why a long-endurance surveillance UAV and a fast strike UAV look
nothing alike though both are fixed-wing aircraft, the difference set by the
payload each was built to carry.
The whole of this series, read backward from here, is the set of budgets a
payload spends.

## Releasing and Dropping Payloads

A payload that leaves the aircraft introduces its own dynamics.
The release shifts the center of gravity at once, a change the control system
must absorb, and the separating store must clear the aircraft cleanly without
striking it, the safe-separation problem the structures article's loads feed
into.
A dropped payload may fall ballistically, descend under a parachute like the
recovery systems the launch-and-recovery article described, or glide away under
its own wings as a released vehicle of its own.
The aircraft becomes a launch platform, and the accuracy of the delivery depends
on the state at release, the position and velocity and attitude the guidance
article holds, since everything the payload does afterward begins from the
condition in which it was let go.
That principle, that the carrier owes the payload a correct release state and
little more, is the whole of the next case.

## Suborbital Spaceplane Payload Delivery

The limiting case of payload delivery is the one that leaves the atmosphere.
A reusable suborbital [spaceplane][ref_spaceplane] is a carrier that boosts on
the energy budget of the [staged-propulsion article][related_post_staged] along
a steep [suborbital][ref_suborbital] arc, the kind of arc the
[sounding rocket][ref_sounding_rocket] has long flown for atmospheric science,
climbing toward an apogee at the edge of space on the zoom the aerobatics
article described, releasing its payload near that apogee, and then returning
through the thermal wall to land like the aircraft of the landing-gear and
guidance articles.
The division of labor is the point.
The carrier delivers the payload to a release state, an altitude and a velocity
vector and an attitude at a chosen time, and the orbital insertion is the
payload's own responsibility, since the payload carries an
[apogee kick][ref_apogee_kick] stage and is in effect the
[upper stage][ref_multistage] of the system.
At the apogee of a suborbital arc the vertical velocity is by definition zero,
so the velocity there is purely horizontal, and it is less than the
[orbital speed][ref_orbital_speed] of a [circular orbit][ref_circular_orbit] at
that altitude,

$$
 v_{circ} = \sqrt{\frac{\mu}{R + h}}, 
\tag{2}
$$

so the payload must supply the difference as a horizontal burn at the
[apogee][ref_apsis],

$$
 \Delta v_{payload} \approx v_{circ} - v_h, 
\tag{3}
$$

the [delta-v][ref_delta_v] that raises the suborbital path into a closed orbit,
the [circularization][ref_orbital_maneuver] the carrier never performs.
This division is what makes the carrier reusable, because it never carries the
propellant of orbit and so is spared the mass penalty that propellant would
impose, while the payload bears the [delta-v budget][ref_delta_v_budget] of its
own insertion and is sized accordingly.
What the carrier owes is not merely a release state but an accurate one, since
an error in the release velocity or attitude or timing propagates into the orbit
the payload reaches, a small error at release becoming a large one in the final
orbit, so the guidance accuracy of the guidance article is itself part of the
handoff and the carrier is judged on how precisely it arrives at the release
point.
The concept is the [air-launch-to-orbit][ref_atlo] idea taken to its clean
edge, the carrier a winged first stage in the lineage of the
[Pegasus][ref_pegasus] and [LauncherOne][ref_launcherone] air-launched systems
and of the [horizontal-launch][research_horizontal_launch] and
[air-launch performance][research_air_launch] studies, except that here the
responsibility is
drawn sharply, the carrier owning the suborbital ascent and the release and the
payload owning everything above it.
What the carrier gives the payload is altitude and a head start, lifting it
above the dense air that costs drag and steering loss and granting it whatever
horizontal velocity the boost imparted, so the payload's burn is smaller than a
launch from the ground would be by exactly the velocity the carrier delivered.

## Scale and the UAV Case

The small unmanned aircraft carries a scaled version of this whole story.
Its payload is a gimballed camera the size of a fist rather than a
reconnaissance suite, its relay is a small radio, its delivery is a parcel, and
its effector, in the loitering-munition case, is the aircraft itself, but the
budgets are the same, the payload fraction squeezed harder at small scale where
the structure and the battery take a larger share.
The modern small UAV increasingly carries a modular bay so one airframe serves
many missions by swapping the payload, which is the payload-fraction logic made
into a product, the bus standardized and the payload changed to suit the day.
That swapping rests on a standardized interface, the mechanical mounting, the
electrical power, and the data and control protocol agreed in advance, the
interoperability that standards such as [STANAG 4586][ref_stanag] codify so a
payload and a platform built by different hands still fit.
The suborbital case steps up in scale to a dedicated carrier far larger than the
twenty-five-kilogram aircraft the series has used as its running example, since
reaching the edge of space is a large-vehicle undertaking, but the principle is
identical, that the carrier is a reusable bus and the payload owns what happens
after release.

## Putting Numbers to It

A worked example sizes both ends of the range.
On the twenty-five-kilogram aircraft a five-kilogram payload is a payload
fraction of about twenty percent, a few hundred watts of its power is a
continuous draw on the hotel load, and its imagery at several megabits per
second is the largest stream on the data link, numbers that read straight out of
the budgets the energy and communications articles built.
At the other end, a payload released near an apogee of two hundred kilometers
faces a circular orbital speed of
$\sqrt{398600/(6371 + 200)} \approx 7.8$ kilometers per second, and since its
horizontal velocity at apogee is whatever the carrier delivered, its
circularization burn is that figure less the delivered velocity.
A carrier that imparts two kilometers per second of horizontal velocity leaves
the payload to supply nearly six, which is the delta-v of a substantial rocket
stage, so the honest conclusion is that the carrier's gift is mostly altitude
and a modest head start while the payload remains most of a launch vehicle in
its own right.
The number sharpens the division of responsibility rather than softening it,
since it shows precisely how much orbit the payload must buy for itself.

## Out of Scope

Several neighboring subjects are deliberately excluded.
The internal design and the signal processing of the sensors, the optics and the
radar waveforms and the receiver chains, are disciplines of their own and are
named rather than derived.
The orbital mechanics of the payload after release, the transfer and the
rendezvous and the station-keeping, are the payload's own concern and beyond
this article except for the handoff delta-v that defines the division of labor,
the same boundary the stability article drew around the orbital problem.
The targeting doctrine and the rules that govern an effector payload are a legal
and operational matter rather than an engineering one.
And the mission-planning and exploitation software, and the specific fielded
systems and their classified capabilities, are outside the scope of a treatment
concerned with how a payload couples to an airframe.

## Conclusion

The payload is the reason the aircraft exists, and every budget the series has
tracked is, read from here, a budget the payload spends, the mass and the volume
and the power and the data and the energy that the platform devotes to carrying
something useful and pointing it where it must look or placing it where it must
go.
The mission system turns the payload's output into a result, and the coupling
runs both ways, the platform constraining the payload and the payload sizing the
platform.
At the far edge the division of labor becomes a clean handoff, a suborbital
carrier that owes its payload only a correct release state at the top of its arc
and a payload that owns its own circularization, the bus and its cargo each
responsible for its own half of the journey to orbit.
It is the fitting last budget of the series, the one in which the aircraft,
having been designed from the airframe outward through every system, finally
exists only to deliver the thing it was built to carry.

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 3 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 3, 3 are established and 0 are bespoke.
The payload fraction is a dimensionless ratio of masses, and the orbital relations use SI units, with the gravitational parameter in cubic metres per second squared and the radius and altitude in metres, so that the speeds are in metres per second.

**Equation 1, Payload Fraction.**
The payload fraction is the payload mass as a fraction of the takeoff mass.

$$
 f_{pl} = \frac{m_{payload}}{m_{takeoff}}, 
\tag{1}
$$

**Equation 2, Circular Orbital Speed.**
The speed of a circular orbit at a given altitude is the square root of the gravitational parameter divided by the orbital radius.
[orbital speed][ref_orbital_speed]
[circular orbit][ref_circular_orbit]

$$
 v_{circ} = \sqrt{\frac{\mu}{R + h}}, 
\tag{2}
$$

**Equation 3, Circularisation Delta-V at Apogee.**
At apogee the velocity is purely horizontal, so the burn that closes the orbit supplies the difference between the circular speed and the horizontal speed.
[delta-v][ref_delta_v]
[circularization][ref_orbital_maneuver]

$$
 \Delta v_{payload} \approx v_{circ} - v_h, 
\tag{3}
$$

### Notation

- $f_{pl}$, the payload fraction
- $m_{payload}$, the payload mass
- $m_{takeoff}$, the takeoff mass
- $v_{circ}$, the circular orbital speed at the apogee altitude
- $\mu$, the gravitational parameter of the Earth
- $R$, the radius of the Earth
- $h$, the altitude
- $v_h$, the horizontal velocity at apogee

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Non-Peer-Reviewed

- Bartolotta, Paul, Alan W. Wilhite, Mark Schaffer, Randall T. Voland, and Larry Huebner. 2011. *Horizontal Launch: A Versatile Concept for Assured Space Access*. NASA/SP-2011-215994. NASA. [https://ntrs.nasa.gov/citations/20120000791][research_horizontal_launch]
- Waters, Eric D., Dennis M. Creech, and Alan D. Philips. 2013. "Air Launch: Examining Performance Potential of Various Configurations and Growth Options." In *American Inst. of Aeronautics and Astronautics*. [https://ntrs.nasa.gov/citations/20140003206][research_air_launch]

### Tertiary Sources

- "Aerial Reconnaissance." 2026. Wikipedia. Last modified February 1, at 04:25 (UTC). [https://en.wikipedia.org/w/index.php?title=Aerial\_reconnaissance&oldid=1335962262][ref_aerial_recon]
- "Agricultural Drone." 2026. Wikipedia. Last modified January 24, at 20:01 (UTC). [https://en.wikipedia.org/w/index.php?title=Agricultural\_drone&oldid=1334638399][ref_agricultural_drone]
- "Air-Launch-to-Orbit." 2026. Wikipedia. Last modified May 11, at 16:58 (UTC). [https://en.wikipedia.org/w/index.php?title=Air-launch-to-orbit&oldid=1353664730][ref_atlo]
- "Angular Resolution." 2025. Wikipedia. Last modified July 9, at 20:46 (UTC). [https://en.wikipedia.org/w/index.php?title=Angular\_resolution&oldid=1299686603][ref_angular_resolution]
- "Apogee Kick Motor." 2025. Wikipedia. Last modified December 19, at 02:58 (UTC). [https://en.wikipedia.org/w/index.php?title=Apogee\_kick\_motor&oldid=1328310806][ref_apogee_kick]
- "Apsis." 2026. Wikipedia. Last modified April 18, at 03:53 (UTC). [https://en.wikipedia.org/w/index.php?title=Apsis&oldid=1349615937][ref_apsis]
- "Circular Orbit." 2024. Wikipedia. Last modified December 5, at 11:32 (UTC). [https://en.wikipedia.org/w/index.php?title=Circular\_orbit&oldid=1261305538][ref_circular_orbit]
- "Data Compression." 2026. Wikipedia. Last modified May 20, at 23:18 (UTC). [https://en.wikipedia.org/w/index.php?title=Data\_compression&oldid=1355277926][ref_data_compression]
- "Delivery Drone." 2026. Wikipedia. Last modified May 5, at 21:19 (UTC). [https://en.wikipedia.org/w/index.php?title=Delivery\_drone&oldid=1352717542][ref_delivery_drone]
- "Delta-v." 2026. Wikipedia. Last modified April 19, at 12:10 (UTC). [https://en.wikipedia.org/w/index.php?title=Delta-v&oldid=1349908295][ref_delta_v]
- "Delta-v Budget." 2026. Wikipedia. Last modified May 11, at 05:27 (UTC). [https://en.wikipedia.org/w/index.php?title=Delta-v\_budget&oldid=1353595717][ref_delta_v_budget]
- "Edge Computing." 2026. Wikipedia. Last modified May 11, at 04:12 (UTC). [https://en.wikipedia.org/w/index.php?title=Edge\_computing&oldid=1353587746][ref_edge_computing]
- "Forward-Looking Infrared." 2026. Wikipedia. Last modified April 13, at 02:07 (UTC). [https://en.wikipedia.org/w/index.php?title=Forward-looking\_infrared&oldid=1348506872][ref_flir]
- "Georeferencing." 2025. Wikipedia. Last modified August 5, at 12:16 (UTC). [https://en.wikipedia.org/w/index.php?title=Georeferencing&oldid=1304338473][ref_georeferencing]
- "Gimbal." 2026. Wikipedia. Last modified March 15, at 11:24 (UTC). [https://en.wikipedia.org/w/index.php?title=Gimbal&oldid=1343619302][ref_gimbal]
- "Ground Sample Distance." 2026. Wikipedia. Last modified February 7, at 20:39 (UTC). [https://en.wikipedia.org/w/index.php?title=Ground\_sample\_distance&oldid=1337157507][ref_ground_sample_distance]
- "Hardpoint." 2026. Wikipedia. Last modified February 19, at 21:19 (UTC). [https://en.wikipedia.org/w/index.php?title=Hardpoint&oldid=1339286279][ref_hardpoint]
- "Hyperspectral Imaging." 2026. Wikipedia. Last modified May 30, at 14:50 (UTC). [https://en.wikipedia.org/w/index.php?title=Hyperspectral\_imaging&oldid=1356901444][ref_hyperspectral]
- "Image Stabilization." 2026. Wikipedia. Last modified April 6, at 16:05 (UTC). [https://en.wikipedia.org/w/index.php?title=Image\_stabilization&oldid=1347418441][ref_image_stabilization]
- "Intelligence, Surveillance, Target Acquisition, and Reconnaissance." 2025. Wikipedia. Last modified December 6, at 06:49 (UTC). [https://en.wikipedia.org/w/index.php?title=Intelligence,\_surveillance,\_target\_acquisition,\_and\_reconnaissance&oldid=1325965536][ref_istar]
- "LauncherOne." 2026. Wikipedia. Last modified April 18, at 20:28 (UTC). [https://en.wikipedia.org/w/index.php?title=LauncherOne&oldid=1349758966][ref_launcherone]
- "Lidar." 2026. Wikipedia. Last modified May 12, at 18:32 (UTC). [https://en.wikipedia.org/w/index.php?title=Lidar&oldid=1353843491][ref_lidar]
- "Loitering Munition." 2026. Wikipedia. Last modified May 30, at 10:13 (UTC). [https://en.wikipedia.org/w/index.php?title=Loitering\_munition&oldid=1356871390][ref_loitering_munition]
- "Multispectral Imaging." 2026. Wikipedia. Last modified January 5, at 08:38 (UTC). [https://en.wikipedia.org/w/index.php?title=Multispectral\_imaging&oldid=1331237907][ref_multispectral]
- "Multistage Rocket." 2026. Wikipedia. Last modified May 17, at 17:22 (UTC). [https://en.wikipedia.org/w/index.php?title=Multistage\_rocket&oldid=1354660731][ref_multistage]
- "Northrop Grumman Pegasus." 2026. Wikipedia. Last modified April 30, at 22:42 (UTC). [https://en.wikipedia.org/w/index.php?title=Northrop\_Grumman\_Pegasus&oldid=1351916555][ref_pegasus]
- "Orbital Maneuver." 2026. Wikipedia. Last modified April 13, at 12:27 (UTC). [https://en.wikipedia.org/w/index.php?title=Orbital\_maneuver&oldid=1348598030][ref_orbital_maneuver]
- "Orbital Speed." 2026. Wikipedia. Last modified January 17, at 04:57 (UTC). [https://en.wikipedia.org/w/index.php?title=Orbital\_speed&oldid=1333342089][ref_orbital_speed]
- "Payload." 2026. Wikipedia. Last modified May 24, at 14:53 (UTC). [https://en.wikipedia.org/w/index.php?title=Payload&oldid=1355894409][ref_payload]
- "Sensor Fusion." 2026. Wikipedia. Last modified April 2, at 20:58 (UTC). [https://en.wikipedia.org/w/index.php?title=Sensor\_fusion&oldid=1346776065][ref_sensor_fusion]
- "Signals Intelligence." 2025. Wikipedia. Last modified November 9, at 13:48 (UTC). [https://en.wikipedia.org/w/index.php?title=Signals\_intelligence&oldid=1321239551][ref_sigint]
- "Sounding Rocket." 2026. Wikipedia. Last modified March 4, at 03:44 (UTC). [https://en.wikipedia.org/w/index.php?title=Sounding\_rocket&oldid=1341619707][ref_sounding_rocket]
- "Spaceplane." 2026. Wikipedia. Last modified May 21, at 07:07 (UTC). [https://en.wikipedia.org/w/index.php?title=Spaceplane&oldid=1355332811][ref_spaceplane]
- "STANAG 4586." 2025. Wikipedia. Last modified August 14, at 17:59 (UTC). [https://en.wikipedia.org/w/index.php?title=STANAG\_4586&oldid=1305891330][ref_stanag]
- "Sub-Orbital Spaceflight." 2026. Wikipedia. Last modified May 7, at 10:20 (UTC). [https://en.wikipedia.org/w/index.php?title=Sub-orbital\_spaceflight&oldid=1352970187][ref_suborbital]
- "Synthetic-Aperture Radar." 2026. Wikipedia. Last modified March 16, at 07:05 (UTC). [https://en.wikipedia.org/w/index.php?title=Synthetic-aperture\_radar&oldid=1343767791][ref_sar]
- "Vibration Isolation." 2026. Wikipedia. Last modified March 3, at 03:02 (UTC). [https://en.wikipedia.org/w/index.php?title=Vibration\_isolation&oldid=1341415069][ref_vibration_isolation]

### Related Posts

- Sechter, Brendan. 2026. "Staged and Boosted Propulsion for Small Fixed-Wing UAVs." *Brendan A R Sechter's Development Blog*, June 3. [https://sgeos.github.io/aerospace/engineering/uav/2026/06/03/staged\_and\_boosted\_propulsion\_for\_fixed\_wing\_uavs.html][related_post_staged]
- Sechter, Brendan. 2026. "Electric Energy Systems and the Endurance Budget for Fixed-Wing UAVs." *Brendan A R Sechter's Development Blog*, June 4. [https://sgeos.github.io/aerospace/engineering/uav/2026/06/04/electric\_energy\_systems\_and\_endurance\_budget\_for\_fixed\_wing\_uavs.html][related_post_electric]
- Sechter, Brendan. 2026. "Guidance, Navigation, and Automatic Landing for Fixed-Wing UAVs." *Brendan A R Sechter's Development Blog*, June 8. [https://sgeos.github.io/aerospace/engineering/uav/2026/06/08/guidance\_navigation\_and\_automatic\_landing\_for\_fixed\_wing\_uavs.html][related_post_gnc]
- Sechter, Brendan. 2026. "Communications and the Command-and-Control Data Link for Fixed-Wing UAVs." *Brendan A R Sechter's Development Blog*, June 9. [https://sgeos.github.io/aerospace/engineering/uav/2026/06/09/communications\_and\_the\_command\_and\_control\_data\_link\_for\_fixed\_wing\_uavs.html][related_post_comms]
- Sechter, Brendan. 2026. "Structures and the Flight Envelope for Fixed-Wing UAVs." *Brendan A R Sechter's Development Blog*, June 10. [https://sgeos.github.io/aerospace/engineering/uav/2026/06/10/structures\_and\_the\_flight\_envelope\_for\_fixed\_wing\_uavs.html][related_post_structures]
- Sechter, Brendan. 2026. "Aerobatics as Costed Trajectories for Fixed-Wing UAVs." *Brendan A R Sechter's Development Blog*, June 11. [https://sgeos.github.io/aerospace/engineering/uav/2026/06/11/aerobatics\_as\_costed\_trajectories\_for\_fixed\_wing\_uavs.html][related_post_aerobatics]

[ref_aerial_recon]: https://en.wikipedia.org/w/index.php?title=Aerial_reconnaissance&oldid=1335962262
[ref_agricultural_drone]: https://en.wikipedia.org/w/index.php?title=Agricultural_drone&oldid=1334638399
[ref_angular_resolution]: https://en.wikipedia.org/w/index.php?title=Angular_resolution&oldid=1299686603
[ref_apogee_kick]: https://en.wikipedia.org/w/index.php?title=Apogee_kick_motor&oldid=1328310806
[ref_apsis]: https://en.wikipedia.org/w/index.php?title=Apsis&oldid=1349615937
[ref_atlo]: https://en.wikipedia.org/w/index.php?title=Air-launch-to-orbit&oldid=1353664730
[ref_circular_orbit]: https://en.wikipedia.org/w/index.php?title=Circular_orbit&oldid=1261305538
[ref_data_compression]: https://en.wikipedia.org/w/index.php?title=Data_compression&oldid=1355277926
[ref_delivery_drone]: https://en.wikipedia.org/w/index.php?title=Delivery_drone&oldid=1352717542
[ref_delta_v]: https://en.wikipedia.org/w/index.php?title=Delta-v&oldid=1349908295
[ref_delta_v_budget]: https://en.wikipedia.org/w/index.php?title=Delta-v_budget&oldid=1353595717
[ref_edge_computing]: https://en.wikipedia.org/w/index.php?title=Edge_computing&oldid=1353587746
[ref_flir]: https://en.wikipedia.org/w/index.php?title=Forward-looking_infrared&oldid=1348506872
[ref_georeferencing]: https://en.wikipedia.org/w/index.php?title=Georeferencing&oldid=1304338473
[ref_gimbal]: https://en.wikipedia.org/w/index.php?title=Gimbal&oldid=1343619302
[ref_ground_sample_distance]: https://en.wikipedia.org/w/index.php?title=Ground_sample_distance&oldid=1337157507
[ref_hardpoint]: https://en.wikipedia.org/w/index.php?title=Hardpoint&oldid=1339286279
[ref_hyperspectral]: https://en.wikipedia.org/w/index.php?title=Hyperspectral_imaging&oldid=1356901444
[ref_image_stabilization]: https://en.wikipedia.org/w/index.php?title=Image_stabilization&oldid=1347418441
[ref_istar]: https://en.wikipedia.org/w/index.php?title=Intelligence,_surveillance,_target_acquisition,_and_reconnaissance&oldid=1325965536
[ref_launcherone]: https://en.wikipedia.org/w/index.php?title=LauncherOne&oldid=1349758966
[ref_lidar]: https://en.wikipedia.org/w/index.php?title=Lidar&oldid=1353843491
[ref_loitering_munition]: https://en.wikipedia.org/w/index.php?title=Loitering_munition&oldid=1356871390
[ref_multispectral]: https://en.wikipedia.org/w/index.php?title=Multispectral_imaging&oldid=1331237907
[ref_multistage]: https://en.wikipedia.org/w/index.php?title=Multistage_rocket&oldid=1354660731
[ref_orbital_maneuver]: https://en.wikipedia.org/w/index.php?title=Orbital_maneuver&oldid=1348598030
[ref_orbital_speed]: https://en.wikipedia.org/w/index.php?title=Orbital_speed&oldid=1333342089
[ref_payload]: https://en.wikipedia.org/w/index.php?title=Payload&oldid=1355894409
[ref_pegasus]: https://en.wikipedia.org/w/index.php?title=Northrop_Grumman_Pegasus&oldid=1351916555
[ref_sar]: https://en.wikipedia.org/w/index.php?title=Synthetic-aperture_radar&oldid=1343767791
[ref_sensor_fusion]: https://en.wikipedia.org/w/index.php?title=Sensor_fusion&oldid=1346776065
[ref_sigint]: https://en.wikipedia.org/w/index.php?title=Signals_intelligence&oldid=1321239551
[ref_sounding_rocket]: https://en.wikipedia.org/w/index.php?title=Sounding_rocket&oldid=1341619707
[ref_spaceplane]: https://en.wikipedia.org/w/index.php?title=Spaceplane&oldid=1355332811
[ref_stanag]: https://en.wikipedia.org/w/index.php?title=STANAG_4586&oldid=1305891330
[ref_suborbital]: https://en.wikipedia.org/w/index.php?title=Sub-orbital_spaceflight&oldid=1352970187
[ref_vibration_isolation]: https://en.wikipedia.org/w/index.php?title=Vibration_isolation&oldid=1341415069
[related_post_aerobatics]: {% post_url 2026-06-11-aerobatics_as_costed_trajectories_for_fixed_wing_uavs %}
[related_post_comms]: {% post_url 2026-06-09-communications_and_the_command_and_control_data_link_for_fixed_wing_uavs %}
[related_post_electric]: {% post_url 2026-06-04-electric_energy_systems_and_endurance_budget_for_fixed_wing_uavs %}
[related_post_gnc]: {% post_url 2026-06-08-guidance_navigation_and_automatic_landing_for_fixed_wing_uavs %}
[related_post_staged]: {% post_url 2026-06-03-staged_and_boosted_propulsion_for_fixed_wing_uavs %}
[related_post_structures]: {% post_url 2026-06-10-structures_and_the_flight_envelope_for_fixed_wing_uavs %}
[research_air_launch]: https://ntrs.nasa.gov/citations/20140003206
[research_horizontal_launch]: https://ntrs.nasa.gov/citations/20120000791
