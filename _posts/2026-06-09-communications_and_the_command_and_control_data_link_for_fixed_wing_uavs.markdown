---
layout: post
mathjax: true
comments: true
title:  "Communications and the Command-and-Control Data Link for Fixed-Wing UAVs"
date:   2026-06-09 09:00:00 +0000
categories: aerospace engineering uav
series: fixed_wing_uav
series_title: Fixed-Wing UAV
series_index: 11
---
<!-- A126 -->
<script>console.log("A126");</script>

The guidance and automatic-landing article put the autopilot aboard the
aircraft, able to fly a mission on its own.
This article is about the link that connects that aircraft to the people on
the ground, the command-and-control data link that carries the operator's
intent up and the aircraft's state and its sensors down.
One quantity organizes the subject, the link budget, the accounting of how
much signal power leaves the transmitter, how much is lost on the way, and
how much reaches the receiver above the noise,
because the margin that accounting leaves is what sets the range, the data
rate, and the reliability of every link the aircraft carries.
A second quantity rides alongside, the latency, the time a message takes to
make the trip, which decides what can be controlled over the link at all.
This article is the first extension beyond the flight-physics arc of the
series, the nervous system that connects the operator to the
[autonomous aircraft][related_post_gnc] the previous articles built and flew.

## The Link Budget

A radio link is an exercise in spending a power budget against loss.
The [link budget][ref_link_budget] adds the transmitter power and the antenna
gains and subtracts the path loss to find the power that reaches the
receiver,

$$
 P_{rx} = P_{tx} + G_{tx} + G_{rx} - \text{FSPL}, 
\tag{1}
$$

where the dominant term over a clear path is the
[free-space path loss][ref_fspl] from the
[Friis transmission equation][ref_friis],

$$
 \text{FSPL(dB)} = 20\log_{10} d + 20\log_{10} f + 32.44, 
\tag{2}
$$

with the distance in kilometers and the frequency in megahertz.
The received power must clear the noise by a margin, and the
[signal-to-noise ratio][ref_snr] that remains bounds how fast the link can
carry data through the [Shannon-Hartley limit][ref_shannon],
$C = B\log_2(1 + \text{SNR})$.
The frequency is the central trade.
A lower frequency travels farther and bends around obstacles but carries
less data, and a higher one carries more but demands a clear line of sight
and loses signal faster,
which is why a small UAV often runs a low band for control and a high band
for video.
The path must also stay clear through most of its [Fresnel zone][ref_fresnel]
to behave as free space, and the unlicensed [ISM bands][ref_ism] are where
most small-UAV links live.
That budget describes a clean path, and near the ground it is optimistic,
because the signal also arrives by reflection, so the
[two-ray ground reflection][ref_ground_reflection] of a low pass can fall off
much faster than free space while [multipath][ref_multipath] fading comes and
goes as the geometry shifts,
which is why a sound link holds extra margin against the fades rather than
trusting the free-space figure.
The transmitter power and the antenna gain are not free to raise, either,
because the regulator caps the [effective radiated power][ref_eirp] on the
unlicensed bands,
so reaching farther within the law means a more sensitive receiver and a
better antenna rather than brute power, or moving to protected
command-and-control spectrum.

## The Radio Horizon

Even a generous link budget cannot see past the horizon.
For frequencies that travel in straight lines, the
[line-of-sight][ref_los] range is bounded by the curve of the Earth,
and the radio horizon is roughly

$$
 d \approx 4.12\left(\sqrt{h_t} + \sqrt{h_r}\right), 
\tag{3}
$$

with the distance in kilometers and the antenna heights in meters,
the constant slightly larger than the geometric one because the atmosphere
bends the waves a little downward.
An aircraft a hundred meters up and a ground antenna a few meters up can see
each other to tens of kilometers,
so for a small UAV the link budget usually binds before the horizon does,
and raising the transmit power or the antenna gain buys range up to the point
where the horizon takes over.
Beyond that line the curve of the Earth, not the power budget, is the wall,
and reaching past it needs a relay or a satellite.

## The Moving Aircraft

The link budget treats the antenna as a fixed gain, but the aircraft is the
hard case because it maneuvers.
As it banks and turns, the airframe shadows the antenna, and the nulls in the
[radiation pattern][ref_radiation_pattern] and the polarization mismatch swing
across the ground station, so the link can drop at the very moment of a steep
turn when it is most needed.
The answers are at the system level rather than in the budget.
The aircraft carries more than one antenna and switches to whichever hears
best, the [antenna diversity][ref_antenna_diversity] that papers over the
nulls,
and the ground station often points a [directional antenna][ref_directional_antenna]
that tracks the aircraft so the gain follows it across the sky.
A link that closes on paper can still fail in a turn, so the moving geometry
is part of the design and not a detail.

## The Three Streams

A UAV link is really three flows with different demands.
The command uplink carries the operator's intent to the aircraft, a small
but critical and latency-sensitive stream, often only a few kilobits per
second.
The [telemetry][ref_telemetry] downlink reports the aircraft's state and
health, its position, attitude, battery, and faults, a modest stream that
the ground watches continuously.
The payload downlink carries the video or the sensor data, the fat pipe that
dwarfs the other two and drives the choice of a high band and a short range.
That video must be squeezed into the channel by a codec such as
[Advanced Video Coding][ref_avc], and the compression adds a latency of its
own, which is why an operator who flies on the video wants the
lowest-latency encoding the link can bear rather than the most efficient.
The streams are asymmetric, a thin trickle up and a flood down,
and the critical command stream is given priority and protection over the
others, since a lost video frame is a nuisance while a lost command is a
hazard.

## Radio Control with a Handheld Transmitter

The oldest and simplest link is a human holding a transmitter.
A consumer [radio-control][ref_radio_control] handset sends stick positions
to a small receiver in the aircraft on the 2.4 gigahertz band,
hopping pseudo-randomly across many channels with
[frequency-hopping spread spectrum][ref_fhss] so that interference on any one
channel is shrugged off, and binding the receiver to one transmitter so the
aircraft answers only to its own operator.
The receiver hands the channels to the autopilot or the servos over a serial
protocol, and an open long-range system such as
[ExpressLRS][ref_elrs] pushes a low-power handheld link to tens of kilometers
on the same principle.
The control link runs at a chosen packet rate, from tens to a thousand updates
a second, trading range against the responsiveness of the controls, the
link-layer echo of the loop rates the dynamics and guidance articles set.
A [first-person-view][ref_fpv] video downlink on a higher band often rides
along so the operator sees what the aircraft sees.
This is direct manual flight within line of sight, the
[radio-controlled aircraft][ref_rc_aircraft] tradition,
and on a UAV it remains the manual path and the backup, the way a person
takes the aircraft when the autonomy is not wanted or not trusted,
with a failsafe that drives the controls to a preset state if the link drops.

## Computer-Controlled Transmission

The same link can be driven by a computer instead of a hand.
Rather than stick positions, a ground station sends structured messages,
and the de facto standard for small UAVs is [MAVLink][ref_mavlink],
a lightweight protocol that carries commands, mission uploads, parameter
changes, and telemetry between a ground control station such as the common
open-source planners and the flight controller running the autopilot of the
previous article.
The link itself is a pair of telemetry radios, a low-power pair on the 433 or
915 megahertz band for modest range or a higher-power pair to reach farther,
and a companion computer aboard the aircraft can route the same messages over
a cellular modem.
The distinction from the handheld case is the level of the command.
The handheld sends raw control deflections that a human closes the loop on,
while the computer sends a waypoint or a mission that the onboard autopilot
then flies, so the data link carries intent rather than stick movement.
The two coexist on most serious aircraft, the autonomous data link for the
mission and the manual handheld link as the human's fallback,
and a well-built UAV listens to both.

## Beyond Line of Sight

Once the mission outruns the horizon, the link must be relayed.
A relay aircraft or a ground repeater extends the range by a hop,
a cellular network can carry the link wherever it has coverage,
and a [satellite link][ref_satcom] carries it anywhere at all,
a constellation such as [Iridium][ref_iridium] relaying the command and the
telemetry between the aircraft and a distant ground station.
The satellite path is the only truly global option, but it is narrow and it
is slow, a constrained data rate and a latency far above the line-of-sight
case,
so a beyond-line-of-sight aircraft typically carries the satellite link for
command and telemetry while leaving the fat payload stream for a moment of
line of sight or a cellular pass.
Many vehicles carry more than one path and fall back from the fastest to the
most available, the same defense-in-depth the recovery article applied to the
aircraft itself.

## Latency, and Why the Loops Are Aboard

The link budget sets whether a message arrives, and the latency sets what can
be done with it.
A line-of-sight link adds only microseconds of travel and a little
processing, but a satellite link in a high orbit adds a quarter of a second
each way, and even a low orbit adds tens of milliseconds.
This [latency][ref_latency] is the reason the fast loops of the dynamics
article run aboard the aircraft and not on the ground.
A pitch oscillation that must be caught many times a second cannot be flown
over a link that takes a quarter second to answer,
so the inner loop and the guidance loop live on the autopilot, and the link
carries only the slow layer, the waypoints, the mission changes, and the
supervision.
The architecture of the whole series follows from this single fact,
that autonomy is aboard because the speed of light and the radio link will
not let it be anywhere else.

## Security and Jamming

A link that carries control is an attack surface.
The simplest attack is [jamming][ref_jamming], drowning the receiver in noise
until the legitimate signal cannot be heard, measured by the
jamming-to-signal ratio at the aircraft,
and the spread-spectrum hopping that fends off accidental interference also
raises the bar for a jammer.
A subtler attack is spoofing, injecting a forged command, which is why a
serious link authenticates and [encrypts][ref_encryption] its traffic so the
aircraft acts only on messages it can verify,
the command-link counterpart to the navigation spoofing the previous article
treated.
A [directional antenna][ref_directional_antenna] that concentrates the link
toward the aircraft both extends the range and narrows the angle from which a
jammer can work,
so antenna choice is a security measure as much as a range one.

## Lost Link

The link will sometimes fail, and the aircraft's behavior when it does is
part of the design rather than an afterthought.
A sound autopilot treats a lost link as a defined event, waiting a set time
and then executing a preset response, a loiter to wait for the link to
return, a return to the launch point, or in the last resort a controlled
landing or termination,
the same [fail-safe][ref_failsafe] discipline the recovery article applied to
the aircraft and the guidance article applied to a lost navigation fix.
A geofence bounds where the aircraft may go even with no link at all.
The lost-link behavior is why a beyond-line-of-sight aircraft can be trusted
with an intermittent satellite link,
because a gap in the link becomes a known, safe holding behavior rather than
a runaway, and the reliability the link cannot guarantee is supplied by the
autonomy instead.

## Scale and the UAV Case

The small UAV carries this whole communications suite in a handful of cheap
modules.
A 2.4 gigahertz handheld link gives the manual path, a 915 or 433 megahertz
telemetry radio carries the MAVLink connection to the ground station, and a
5.8 gigahertz transmitter sends the video,
each a small board costing little and drawing little, though the radios are a
real part of the electrical load the energy article budgeted.
The same open hardware and software that made the autopilot ordinary made the
data link ordinary too,
so a hobbyist commands a small UAV with the same kinds of radios a large one
uses, scaled down in power and range.
The difference between a toy and a serious aircraft is less the radios than
the discipline applied to the link budget, the security, and the lost-link
behavior.

## Putting Numbers to It

A worked example sizes a modest link.
At 2.4 gigahertz over ten kilometers the free-space path loss is
$20\log_{10}(10) + 20\log_{10}(2400) + 32.44 \approx 120$ decibels.
A hundred-milliwatt transmitter at twenty decibel-milliwatts, with a couple
of decibels of antenna gain at each end, delivers about
$20 + 2 + 2 - 120 = -96$ decibel-milliwatts at the receiver,
and a sensitive long-range receiver hearing down to about minus one hundred
eight decibel-milliwatts leaves roughly a twelve-decibel margin,
so the small link closes ten kilometers with room to spare.
The radio horizon for an aircraft a hundred meters up and an antenna three
meters up is $4.12(\sqrt{100} + \sqrt{3}) \approx 48$ kilometers,
so the power budget binds first and more power would buy more range.
The command stream needs only kilobits per second while the video wants
megabits, which is why the video rides a wider, shorter-range band,
and the line-of-sight latency is well under a millisecond while a satellite
relay would add hundreds, which is why the fast loops stay aboard.

## Out of Scope

Several neighboring subjects are deliberately excluded.
The detailed design of the radio, the antenna, and the modulation and coding
that pack bits into the channel is a discipline of its own,
and this article uses the link budget rather than deriving the waveform.
The internals of the specific protocols, the cryptographic algorithms, and
the spectrum regulation that governs which bands and powers are permitted are
named but not specified.
The guidance and navigation that the link carries are the subject of the
previous article, and the satellite navigation it depends on is distinct from
the communications link treated here.
And the networking of many vehicles into a mesh or a swarm, and the
ground-station software and human-factors design, are beyond this scope.

## Conclusion

The command-and-control data link is the management of an information budget.
The link budget decides whether a message arrives, the frequency trades range
against data rate, the horizon bounds the line-of-sight reach, and the
latency decides what can be controlled over the link at all.
A handheld transmitter flies the aircraft manually within sight, a computer
link carries waypoints and missions to the autopilot, and a satellite relay
reaches beyond the horizon at the cost of speed,
while the fast loops stay aboard because no link is quick enough to hold them,
and a lost link falls into a safe, preset behavior rather than a runaway.
This is the link that makes the autonomous aircraft of the series
commandable and accountable from the ground,
the thin, defended thread of radio over which a person, or a planner,
tells the aircraft what to do and watches it do it.

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 3 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 3, 3 are established and 0 are bespoke.
The link budget is written in decibels, with powers in decibels relative to a reference and gains in decibels, and the free-space path loss constant of 32.44 holds only with distance in kilometres and frequency in megahertz, while the radio horizon takes antenna heights in metres and returns kilometres.

**Equation 1, Link Budget.**
The received power in decibels is the transmitter power plus both antenna gains less the path loss.
[link budget][ref_link_budget]

$$
 P_{rx} = P_{tx} + G_{tx} + G_{rx} - \text{FSPL}, 
\tag{1}
$$

**Equation 2, Free-Space Path Loss in Decibels.**
The free-space path loss from the Friis transmission equation grows by twenty decibels per decade of distance and of frequency.
[free-space path loss][ref_fspl]
[Friis transmission equation][ref_friis]

$$
 \text{FSPL(dB)} = 20\log_{10} d + 20\log_{10} f + 32.44, 
\tag{2}
$$

**Equation 3, Radio Horizon.**
The line-of-sight range between two antennas is the sum of their horizon distances, with a constant slightly larger than the geometric one to allow for atmospheric refraction.
[line-of-sight][ref_los]

$$
 d \approx 4.12\left(\sqrt{h_t} + \sqrt{h_r}\right), 
\tag{3}
$$

### Notation

- $P_{rx}$, the received power
- $P_{tx}$, the transmitter power
- $G_{tx}$, the transmitting antenna gain
- $G_{rx}$, the receiving antenna gain
- $\text{FSPL}$, the free-space path loss
- $d$, the distance in kilometres
- $f$, the frequency in megahertz
- $h_t$, the transmitting antenna height in metres
- $h_r$, the receiving antenna height in metres

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Non-Peer-Reviewed

- Data Links Functions. n.d. *Attributes, and Latency (Kansas State University)*. [https://kstatelibraries.pressbooks.pub/unmannedaircraftsystems/chapter/chapter-13-data-links-functions-attributes-and-latency/][research_kstate_datalink]
- Kerczewski, Robert J., Jeffrey D. Wilson, and William D. Bishop. 2016. "Satellite Communications for Unmanned Aircraft C2 Links: C-Band, Ku-Band and Ka-Band." In *American Inst. of Aeronautics and Astronautics*. [https://ntrs.nasa.gov/citations/20170005641][research_nasa_satcom]
- *Secure Communication in Drone Networks (MDPI Drones)*. n.d. [https://www.mdpi.com/2504-446X/9/8/583][research_mdpi_security]

### Tertiary Sources

- "Advanced Video Coding." 2026. Wikipedia. Last modified May 30, at 23:25 (UTC). [https://en.wikipedia.org/w/index.php?title=Advanced\_Video\_Coding&oldid=1356965470][ref_avc]
- "Antenna Diversity." 2026. Wikipedia. Last modified May 14, at 06:11 (UTC). [https://en.wikipedia.org/w/index.php?title=Antenna\_diversity&oldid=1354087734][ref_antenna_diversity]
- "Communications Satellite." 2026. Wikipedia. Last modified April 27, at 18:54 (UTC). [https://en.wikipedia.org/w/index.php?title=Communications\_satellite&oldid=1351404367][ref_satcom]
- "Directional Antenna." 2025. Wikipedia. Last modified September 24, at 13:45 (UTC). [https://en.wikipedia.org/w/index.php?title=Directional\_antenna&oldid=1313135297][ref_directional_antenna]
- "Effective Radiated Power." 2026. Wikipedia. Last modified January 23, at 13:48 (UTC). [https://en.wikipedia.org/w/index.php?title=Effective\_radiated\_power&oldid=1334428095][ref_eirp]
- "Encryption." 2026. Wikipedia. Last modified May 29, at 12:03 (UTC). [https://en.wikipedia.org/w/index.php?title=Encryption&oldid=1356718435][ref_encryption]
- "ExpressLRS." 2026. Wikipedia. Last modified May 22, at 17:08 (UTC). [https://en.wikipedia.org/w/index.php?title=ExpressLRS&oldid=1355571152][ref_elrs]
- "Fail-Safe." 2026. Wikipedia. Last modified May 22, at 20:55 (UTC). [https://en.wikipedia.org/w/index.php?title=Fail-safe&oldid=1355604792][ref_failsafe]
- "First-Person View (Remote Control)." 2026. Wikipedia. Last modified May 13, at 19:19 (UTC). [https://en.wikipedia.org/w/index.php?title=First-person\_view\_(remote\_control)&oldid=1354011853][ref_fpv]
- "Free-Space Path Loss." 2026. Wikipedia. Last modified May 14, at 23:51 (UTC). [https://en.wikipedia.org/w/index.php?title=Free-space\_path\_loss&oldid=1354206088][ref_fspl]
- "Frequency-Hopping Spread Spectrum." 2025. Wikipedia. Last modified September 4, at 06:48 (UTC). [https://en.wikipedia.org/w/index.php?title=Frequency-hopping\_spread\_spectrum&oldid=1309467218][ref_fhss]
- "Fresnel Zone." 2026. Wikipedia. Last modified February 19, at 04:04 (UTC). [https://en.wikipedia.org/w/index.php?title=Fresnel\_zone&oldid=1339145953][ref_fresnel]
- "Friis Transmission Equation." 2025. Wikipedia. Last modified April 16, at 11:54 (UTC). [https://en.wikipedia.org/w/index.php?title=Friis\_transmission\_equation&oldid=1285892231][ref_friis]
- "Iridium Satellite Constellation." 2026. Wikipedia. Last modified May 9, at 14:24 (UTC). [https://en.wikipedia.org/w/index.php?title=Iridium\_satellite\_constellation&oldid=1353311359][ref_iridium]
- "ISM Radio Band." 2026. Wikipedia. Last modified May 20, at 20:39 (UTC). [https://en.wikipedia.org/w/index.php?title=ISM\_radio\_band&oldid=1355256467][ref_ism]
- "Latency (Engineering)." 2026. Wikipedia. Last modified March 24, at 16:41 (UTC). [https://en.wikipedia.org/w/index.php?title=Latency\_(engineering)&oldid=1345160690][ref_latency]
- "Line-of-Sight Propagation." 2026. Wikipedia. Last modified February 19, at 11:14 (UTC). [https://en.wikipedia.org/w/index.php?title=Line-of-sight\_propagation&oldid=1339192660][ref_los]
- "Link Budget." 2025. Wikipedia. Last modified June 6, at 10:34 (UTC). [https://en.wikipedia.org/w/index.php?title=Link\_budget&oldid=1294217373][ref_link_budget]
- "MAVLink." 2026. Wikipedia. Last modified May 21, at 01:43 (UTC). [https://en.wikipedia.org/w/index.php?title=MAVLink&oldid=1355297070][ref_mavlink]
- "Multipath Propagation." 2025. Wikipedia. Last modified August 20, at 21:11 (UTC). [https://en.wikipedia.org/w/index.php?title=Multipath\_propagation&oldid=1306985169][ref_multipath]
- "Radiation Pattern." 2026. Wikipedia. Last modified March 14, at 03:32 (UTC). [https://en.wikipedia.org/w/index.php?title=Radiation\_pattern&oldid=1343410001][ref_radiation_pattern]
- "Radio Control." 2026. Wikipedia. Last modified May 20, at 17:52 (UTC). [https://en.wikipedia.org/w/index.php?title=Radio\_control&oldid=1355232766][ref_radio_control]
- "Radio Jamming." 2026. Wikipedia. Last modified May 16, at 02:07 (UTC). [https://en.wikipedia.org/w/index.php?title=Radio\_jamming&oldid=1354382325][ref_jamming]
- "Radio-Controlled Aircraft." 2026. Wikipedia. Last modified May 6, at 00:20 (UTC). [https://en.wikipedia.org/w/index.php?title=Radio-controlled\_aircraft&oldid=1352738353][ref_rc_aircraft]
- "Shannon–Hartley Theorem." 2026. Wikipedia. Last modified April 25, at 13:07 (UTC). [https://en.wikipedia.org/w/index.php?title=Shannon%E2%80%93Hartley\_theorem&oldid=1351019133][ref_shannon]
- "Signal-to-Noise Ratio." 2026. Wikipedia. Last modified May 10, at 15:56 (UTC). [https://en.wikipedia.org/w/index.php?title=Signal-to-noise\_ratio&oldid=1353489938][ref_snr]
- "Telemetry." 2026. Wikipedia. Last modified March 31, at 08:16 (UTC). [https://en.wikipedia.org/w/index.php?title=Telemetry&oldid=1346337145][ref_telemetry]
- "Two-Ray Ground-Reflection Model." 2026. Wikipedia. Last modified March 30, at 02:14 (UTC). [https://en.wikipedia.org/w/index.php?title=Two-ray\_ground-reflection\_model&oldid=1346124943][ref_ground_reflection]

### Related Posts

- Sechter, Brendan. 2026. "Launch and Recovery Systems for Fixed-Wing UAVs." *Brendan A R Sechter's Development Blog*, June 1. [https://sgeos.github.io/aerospace/engineering/uav/2026/06/01/launch\_and\_recovery\_systems\_for\_fixed\_wing\_uavs.html][related_post_recovery]
- Sechter, Brendan. 2026. "Electric Energy Systems and the Endurance Budget for Fixed-Wing UAVs." *Brendan A R Sechter's Development Blog*, June 4. [https://sgeos.github.io/aerospace/engineering/uav/2026/06/04/electric\_energy\_systems\_and\_endurance\_budget\_for\_fixed\_wing\_uavs.html][related_post_electric]
- Sechter, Brendan. 2026. "Guidance, Navigation, and Automatic Landing for Fixed-Wing UAVs." *Brendan A R Sechter's Development Blog*, June 8. [https://sgeos.github.io/aerospace/engineering/uav/2026/06/08/guidance\_navigation\_and\_automatic\_landing\_for\_fixed\_wing\_uavs.html][related_post_gnc]

[ref_antenna_diversity]: https://en.wikipedia.org/w/index.php?title=Antenna_diversity&oldid=1354087734
[ref_avc]: https://en.wikipedia.org/w/index.php?title=Advanced_Video_Coding&oldid=1356965470
[ref_directional_antenna]: https://en.wikipedia.org/w/index.php?title=Directional_antenna&oldid=1313135297
[ref_eirp]: https://en.wikipedia.org/w/index.php?title=Effective_radiated_power&oldid=1334428095
[ref_elrs]: https://en.wikipedia.org/w/index.php?title=ExpressLRS&oldid=1355571152
[ref_encryption]: https://en.wikipedia.org/w/index.php?title=Encryption&oldid=1356718435
[ref_failsafe]: https://en.wikipedia.org/w/index.php?title=Fail-safe&oldid=1355604792
[ref_fhss]: https://en.wikipedia.org/w/index.php?title=Frequency-hopping_spread_spectrum&oldid=1309467218
[ref_fpv]: https://en.wikipedia.org/w/index.php?title=First-person_view_(remote_control)&oldid=1354011853
[ref_fresnel]: https://en.wikipedia.org/w/index.php?title=Fresnel_zone&oldid=1339145953
[ref_friis]: https://en.wikipedia.org/w/index.php?title=Friis_transmission_equation&oldid=1285892231
[ref_fspl]: https://en.wikipedia.org/w/index.php?title=Free-space_path_loss&oldid=1354206088
[ref_ground_reflection]: https://en.wikipedia.org/w/index.php?title=Two-ray_ground-reflection_model&oldid=1346124943
[ref_iridium]: https://en.wikipedia.org/w/index.php?title=Iridium_satellite_constellation&oldid=1353311359
[ref_ism]: https://en.wikipedia.org/w/index.php?title=ISM_radio_band&oldid=1355256467
[ref_jamming]: https://en.wikipedia.org/w/index.php?title=Radio_jamming&oldid=1354382325
[ref_latency]: https://en.wikipedia.org/w/index.php?title=Latency_(engineering)&oldid=1345160690
[ref_link_budget]: https://en.wikipedia.org/w/index.php?title=Link_budget&oldid=1294217373
[ref_los]: https://en.wikipedia.org/w/index.php?title=Line-of-sight_propagation&oldid=1339192660
[ref_mavlink]: https://en.wikipedia.org/w/index.php?title=MAVLink&oldid=1355297070
[ref_multipath]: https://en.wikipedia.org/w/index.php?title=Multipath_propagation&oldid=1306985169
[ref_radiation_pattern]: https://en.wikipedia.org/w/index.php?title=Radiation_pattern&oldid=1343410001
[ref_radio_control]: https://en.wikipedia.org/w/index.php?title=Radio_control&oldid=1355232766
[ref_rc_aircraft]: https://en.wikipedia.org/w/index.php?title=Radio-controlled_aircraft&oldid=1352738353
[ref_satcom]: https://en.wikipedia.org/w/index.php?title=Communications_satellite&oldid=1351404367
[ref_shannon]: https://en.wikipedia.org/w/index.php?title=Shannon%E2%80%93Hartley_theorem&oldid=1351019133
[ref_snr]: https://en.wikipedia.org/w/index.php?title=Signal-to-noise_ratio&oldid=1353489938
[ref_telemetry]: https://en.wikipedia.org/w/index.php?title=Telemetry&oldid=1346337145
[related_post_electric]: {% post_url 2026-06-04-electric_energy_systems_and_endurance_budget_for_fixed_wing_uavs %}
[related_post_gnc]: {% post_url 2026-06-08-guidance_navigation_and_automatic_landing_for_fixed_wing_uavs %}
[related_post_recovery]: {% post_url 2026-06-01-launch_and_recovery_systems_for_fixed_wing_uavs %}
[research_kstate_datalink]: https://kstatelibraries.pressbooks.pub/unmannedaircraftsystems/chapter/chapter-13-data-links-functions-attributes-and-latency/
[research_mdpi_security]: https://www.mdpi.com/2504-446X/9/8/583
[research_nasa_satcom]: https://ntrs.nasa.gov/citations/20170005641
