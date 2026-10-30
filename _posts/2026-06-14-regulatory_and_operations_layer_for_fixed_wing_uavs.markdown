---
layout: post
mathjax: true
comments: true
title:  "The Regulatory and Operations Layer for Fixed-Wing UAVs"
date:   2026-06-14 09:00:00 +0000
categories: aerospace engineering uav
series: fixed_wing_uav
series_title: Fixed-Wing UAV
series_index: 16
---
<!-- A131 -->
<script>console.log("A131");</script>

The series has now designed and equipped the aircraft, from the foam-and-glass
airframe through the propulsion, the energy, the control, the link, the
structure, and the payload.
This final article is about the permission to fly it and the discipline of
operating it, the layer that sits above the engineering and decides whether the
aircraft may leave the ground at all.
One principle organizes the subject, that the authorization to operate is
granted in proportion to the risk the operation poses and the control the
operator can demonstrate over that risk, so the regulatory burden and the
operational discipline both scale with the harm a flight could do.
A caution belongs at the front of this article more than any other in the
series, that regulation is jurisdictional and not everyone is in the same
country, so the specific thresholds and categories named here are patterns and
not the law of any one place, they differ between states, and they change from
year to year, so an operator must read the rules of the authority that governs
where the aircraft will actually fly.
What follows is the shape of the layer, not its current text.

## Regulation Is Jurisdictional

There is no single rulebook for the world.
The [International Civil Aviation Organization][ref_icao] frames the
international system under the [Chicago Convention][ref_chicago], setting
[standards and recommended practices][research_icao] that member states agree to
implement, but
it is each state that writes and enforces its own law, so the
[regulation of unmanned aircraft][ref_uav_regulation] is a patchwork of national
regimes that rhyme without being identical.
The [Federal Aviation Administration][ref_faa] governs the United States, the
[European Union Aviation Safety Agency][ref_easa] the European Union, the
[Civil Aviation Authority][ref_caa_uk] the United Kingdom, the
[Civil Aviation Safety Authority][ref_casa] Australia,
[Transport Canada][ref_transport_canada] Canada, the
[Civil Aviation Administration of China][ref_caac] China, and every other state
its own authority, and an operator obeys the one whose airspace it is in.
The Chicago Convention also sets aside state aircraft, those in military,
customs, and police service, from the civil rules, so a state operator follows a
separate regime, which is why this article describes the civil layer and notes
the military exemption rather than treating it.
The lesson of this section governs all the rest, that the principles travel but
the numbers do not.

## Authorization Proportionate to Risk

The principle that unifies the modern regimes is that the burden tracks the risk.
A common pattern, clearest in the [European framework][research_easa] but echoed
in others, sorts
operations into three bands, an open or low-risk band flown under fixed
conditions with no individual approval, a specific or medium-risk band that
requires a risk assessment and an operating authorization, and a certified or
high-risk band regulated like crewed aviation with a type-certified aircraft and
a licensed operator.
The risk that sets the band has two components, the ground risk of harm to
people and property beneath the flight, and the air risk of collision with
other aircraft, and an operation is placed by the larger of the two.
A structured method such as the specific operations risk assessment promoted by
the [international rulemaking bodies][research_jarus] works through these risks
and the mitigations
that reduce them, granting the authorization when the residual risk is low
enough.
The shape is the same everywhere even where the labels differ, the freedom to
fly without asking at the low end, a reasoned case made to the authority in the
middle, and the full apparatus of certified aviation at the top.

## Kinetic Energy as the Measure of Harm

Underneath the categories is a physical quantity the whole series has tracked.
The severity of a ground impact scales with the
[kinetic energy][ref_kinetic_energy] the aircraft carries,

$$
 E_k = \tfrac{1}{2} m v^2, 
\tag{1}
$$

so the mass of the structures article and the speed of the envelope and
aerobatics articles are exactly the variables that set how much harm a falling
aircraft can do.
This is why the regulatory axes are mass and speed, and why a small slow
aircraft is treated lightly while a large fast one is treated as a hazard, since
the energy rises with the mass once and with the speed squared.
The common low-risk thresholds near a quarter of a kilogram and the limits on
speed and height are, read physically, lines drawn on the kinetic energy a
member of the public might receive, and the same energy that the recovery and
landing articles had to absorb deliberately is the energy the regulator is
trying to keep away from people.
The categories are a budget of harm, written in the same currency of mass and
speed the engineering used.

## The Axes of Risk

The regulations cut along a small set of axes that together place an operation.
The mass class sorts aircraft into bands, with common breakpoints that vary by
jurisdiction but always rise with the kinetic energy at stake.
Whether the operation is within visual line of sight or
[beyond it][ref_bvlos] is decisive, since a beyond-line-of-sight flight cannot
be seen and avoided by its own operator and so carries far more air risk and
demands far more capability.
Flight over people, and especially over crowds, raises the ground risk sharply,
as does flight near an aerodrome or in controlled
[airspace][ref_airspace_class], while flight at night, beyond a height limit, or
near other traffic each adds its own restriction.
The common numbers, a height limit often near a hundred and twenty meters, a
small-aircraft threshold often near a quarter of a kilogram, a separation from
aerodromes, are patterns repeated across many regimes, but the exact values are
set by each authority and must be checked, the principle being that every axis
is a proxy for ground risk or air risk.

## Registration, Identification, and Competency

Above a threshold the aircraft and its operator must be known to the authority.
Registration records who is responsible for a given aircraft, and
[remote identification][ref_remote_id], the broadcast of an electronic identity
and position, is increasingly required so that an aircraft in flight can be
attributed to its operator from the ground, the aviation counterpart to a
license plate.
The remote pilot must demonstrate competency, through a test or a certificate
scaled to the risk of the operation, from a short online examination for the
low-risk band to a full licence for the certified one.
Through all of it the operator, the legal person who conducts the flight, holds
the responsibility, so registration and identification and competency are the
means by which the authority binds a flight to an accountable party.
The growing [automation][ref_automation] the guidance and payload articles built
strains this model, since when the aircraft decides for itself the question of
who is accountable sharpens, and the regulator answers it so far by anchoring the
responsibility to a human operator however much the aircraft does on its own, an
arrangement the frontier of the regime is still testing.

## Airworthiness and the Certified End

At the high-risk end the aircraft itself must be shown to be sound.
A [type certificate][ref_type_cert] attests that a design meets an
[airworthiness][ref_airworthiness] standard, established by the kind of static,
fatigue, and flutter testing the [structures article][related_post_structures]
described, and a certificate
of airworthiness attests that a particular aircraft conforms to that design and
remains fit to fly.
Continuing airworthiness then keeps it so through its life, by the maintenance
and inspection that catch the fatigue and damage the structures article
treated.
This is the apparatus of crewed aviation applied to the unmanned aircraft, and
it is required only where the risk earns it, the certified band, so most small
unmanned aircraft never meet it while a large one flown over people or in shared
airspace must.

## Integrating with Other Traffic

The hardest problem of the layer is sharing the sky.
Airspace may be segregated, set aside so that the unmanned aircraft flies where
crewed aircraft do not, which is simple but limiting, or integrated, so that the
two share the same air, which is the goal and the difficulty.
Integration at scale is the work of unmanned traffic management, the
[traffic-management][ref_utm] systems and the European
[U-space][ref_uspace] that provide the registration, the flight authorization,
and the deconfliction the data-link article touched on, a layer of digital
services parallel to the air traffic control of crewed aviation.
For a flight beyond visual line of sight the aircraft must be able to
[detect and avoid][ref_daa] other traffic on its own, the capability that
substitutes for the eyes of a pilot, and it must hold a command-and-control link
reliable enough that the regulator trusts the operator to remain in charge, the
reliability the [communications article][related_post_comms] framed and the
autonomy the [guidance article][related_post_gnc] supplied.
Until detect-and-avoid and link reliability are proven, the beyond-line-of-sight
operation is the boundary the whole regime is pushing against.

## The Operations Layer

Below the regulation sits the discipline of actually operating, which the
authority requires and inspects.
The concept of operations states what the aircraft will do and where and how,
the document against which an authorization is granted.
The crew has defined roles, a remote pilot in command who is responsible for the
flight, with observers and a payload operator as the operation needs, and they
work to written procedures and checklists rather than from memory.
Before each sortie the crew plans the flight, secures any airspace
authorization, checks the weather against its limits, and reads the notices that
warn of hazards and restrictions, the routine discipline that precedes every
launch.
The aircraft is maintained on a schedule that keeps it airworthy, the crew is
trained and kept current, and a mature operator runs a
[safety management system][ref_sms], a standing process that identifies hazards,
tracks them, and learns from occurrences, supported by the
[just culture][ref_just_culture] that lets people report a mistake without fear
so the system can improve, while a serious occurrence is examined by an
authority independent of the regulator so the lesson is drawn for
[air safety][ref_air_safety] rather than for blame.
The operations layer is where the engineering of the whole series meets the
daily reality of flying, the place the aircraft is either operated well or not.

## Contingency and Containment

The heart of the safety case an authority examines is what happens when things
go wrong.
An authorization rests on defined contingency procedures, a known response to a
lost command link, a lost navigation fix, or a failed component, the failsafe
behavior the launch-and-recovery and guidance articles built now read as a
regulatory requirement rather than a design choice.
Containment is the central idea, the aircraft kept inside an approved
operational volume by a [geofence][ref_geofence] with a buffer of ground and air
risk around it, so that a failure stays within a region cleared for it, and in
the last resort a [flight termination][ref_flight_termination] brings the
aircraft down deliberately inside that region rather than letting it wander.
The security of the command link is part of the same case, since the jamming and
spoofing the communications article treated are not only engineering problems
but regulatory ones, a link that can be hijacked making the aircraft a hazard,
so the authority weighs the integrity of the command as it weighs the integrity
of the structure.

## Adjacent Regimes

Aviation law is not the only law a flight must obey.
The radio link of the communications article uses spectrum that is licensed, the
international allocations of the [telecommunication union][ref_itu] implemented
by each national regulator, so the very frequencies the aircraft transmits on
are permitted rather than free.
The aircraft and its components may be controlled exports, the dual-use and
military technology governed by regimes such as the
[arms-traffic regulations][ref_itar] and the
[export administration regulations][ref_ear] of the United States and the
multilateral [Wassenaar Arrangement][ref_wassenaar], so moving an aircraft or
its sensors across a border can require a licence.
The payload of the mission-systems article gathers data about people and places,
which engages privacy and data-protection law such as the European
[data-protection regulation][ref_gdpr], varying widely between states.
The flight may also cross the [property rights][ref_air_rights] of those it
passes over, the contested question of who owns the air just above private land
and of trespass and nuisance, which differs sharply between states.
And insurance and liability, and noise and environmental rules, each add their
own constraint, so the permission to fly is the intersection of several bodies
of law and not aviation regulation alone.

## The Boundary with Space

The suborbital carrier of the [payload article][related_post_payload] crosses a
boundary that the rest of the series never reaches, the one between air law and
[space law][ref_space_law].
Aviation regulation governs flight in the airspace of a state, but a vehicle
that climbs toward orbit passes into a regime governed by the
[Outer Space Treaty][ref_ost] and its principle that states bear international
responsibility for the activities they launch, implemented through national
launch licensing rather than through the airworthiness and operating
authorizations of aviation.
Where exactly one regime ends and the other begins is itself unsettled, since
the [Kármán line][ref_karman] near a hundred kilometers is a convention rather
than a treaty boundary, and a vehicle that takes off as an aircraft and releases
a payload toward orbit may pass through both regimes in one flight.
The clean division of labor the payload article drew has a regulatory twin, the
carrier licensed and operated as an aircraft up to release and the payload and
its insertion falling under the law of space, the handoff in responsibility
mirrored by a handoff in jurisdiction.

## Scale and the UAV Case

For the small unmanned aircraft the whole layer collapses to something light.
A sub-kilogram aircraft flown in daylight within sight and away from people and
aerodromes sits in the low-risk band of almost every regime, needing at most a
registration, a remote identity, and a short competency test, which is why the
hobby and the light commercial use of small UAVs is widespread.
As the aircraft grows heavier, flies beyond sight, ventures over people, or
shares controlled airspace, it climbs through the specific band into the
certified one, and the burden rises with it toward the full apparatus of
aviation.
The recurring lesson of the series holds here in its final form, that the
burden tracks the risk and the risk tracks the kinetic energy and the airspace,
and that with no one aboard the responsibility falls not on a pilot in the
aircraft but on the operator on the ground, who is the accountable party the
whole layer is built to identify and bind.

## Out of Scope

Several subjects are deliberately excluded.
The specific current rules of any one jurisdiction are not given, because they
differ between states and change from year to year, and the only safe source is
the authority that governs the flight.
The detailed legal and contractual matter, the enforcement and the penalties,
and the full methodology of a formal risk assessment are named rather than
worked.
The detailed treatment of space law and launch licensing belongs to a study of
its own, and is touched here only at the boundary the suborbital case crosses.
And the policy questions, whether a given rule is wise or a given burden
proportionate, are left aside in favor of the engineering shape of the layer.

## Conclusion

The right to fly is granted against demonstrated control of risk, and the whole
of this series has been the building of an aircraft that can demonstrate it.
The structure that holds together, the link that stays in command, the autonomy
that flies the path, and the payload that does the work are also the evidence an
operator brings to an authority to earn an authorization, so the engineering and
the regulation are two views of the same thing, the case that a flight is safe
enough to permit.
The layer is jurisdictional and it moves, so the operator must read the rules of
the place and the year, but the principle is stable, that the burden tracks the
risk and the risk is measured in the mass and the speed and the airspace the
series has worked in throughout.
This completes the arc, from a
[foam-and-glass airframe][related_post_prototyping] on a workbench to a
regulated and operated system permitted to fly, the last layer above all the
others being the permission to use what was built.

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 1 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 1, 1 are established and 0 are bespoke.
Kinetic energy is in joules when mass is in kilograms and speed in metres per second, and regulatory impact thresholds stated in other units must be converted before comparison.

**Equation 1, Kinetic Energy at Impact.**
The kinetic energy of the aircraft, half the mass times the square of the speed, measures the severity of a ground impact.
[kinetic energy][ref_kinetic_energy]

$$
 E_k = \tfrac{1}{2} m v^2, 
\tag{1}
$$

### Notation

- $E_k$, the kinetic energy
- $m$, the aircraft mass
- $v$, the speed at impact

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Non-Peer-Reviewed

- *Civil Drones (European Union Aviation Safety Agency)*. n.d. [https://www.easa.europa.eu/en/domains/civil-drones][research_easa]
- *Unmanned Aviation (International Civil Aviation Organization)*. n.d. [https://www.icao.int/safety/UA/Pages/default.aspx][research_icao]

### General Sources

- "Joint Authorities for Rulemaking on Unmanned Systems." n.d. Accessed October 25, 2026. [http://jarus-rpas.org/][research_jarus]

### Tertiary Sources

- "Air Rights." 2026. Wikipedia. Last modified January 7, at 01:37 (UTC). [https://en.wikipedia.org/w/index.php?title=Air\_rights&oldid=1331576511][ref_air_rights]
- "Airspace." 2026. Wikipedia. Last modified May 6, at 16:03 (UTC). [https://en.wikipedia.org/w/index.php?title=Airspace&oldid=1352848546][ref_airspace_class]
- "Airworthiness." 2025. Wikipedia. Last modified November 19, at 21:22 (UTC). [https://en.wikipedia.org/w/index.php?title=Airworthiness&oldid=1323124816][ref_airworthiness]
- "Aviation Safety." 2026. Wikipedia. Last modified May 31, at 18:59 (UTC). [https://en.wikipedia.org/w/index.php?title=Aviation\_safety&oldid=1357097957][ref_air_safety]
- "Civil Aviation Administration of China." 2026. Wikipedia. Last modified May 7, at 20:30 (UTC). [https://en.wikipedia.org/w/index.php?title=Civil\_Aviation\_Administration\_of\_China&oldid=1353043294][ref_caac]
- "Civil Aviation Authority (United Kingdom)." 2026. Wikipedia. Last modified May 28, at 16:30 (UTC). [https://en.wikipedia.org/w/index.php?title=Civil\_Aviation\_Authority\_(United\_Kingdom)&oldid=1356574669][ref_caa_uk]
- "Civil Aviation Safety Authority." 2026. Wikipedia. Last modified January 10, at 01:25 (UTC). [https://en.wikipedia.org/w/index.php?title=Civil\_Aviation\_Safety\_Authority&oldid=1332126203][ref_casa]
- "Convention on International Civil Aviation." 2025. Wikipedia. Last modified November 28, at 19:15 (UTC). [https://en.wikipedia.org/w/index.php?title=Convention\_on\_International\_Civil\_Aviation&oldid=1324626701][ref_chicago]
- "Detect and Avoid." 2025. Wikipedia. Last modified August 25, at 14:46 (UTC). [https://en.wikipedia.org/w/index.php?title=Detect\_and\_avoid&oldid=1307759350][ref_daa]
- "European Union Aviation Safety Agency." 2026. Wikipedia. Last modified May 28, at 19:26 (UTC). [https://en.wikipedia.org/w/index.php?title=European\_Union\_Aviation\_Safety\_Agency&oldid=1356601234][ref_easa]
- "Export Administration Regulations." 2026. Wikipedia. Last modified March 20, at 15:49 (UTC). [https://en.wikipedia.org/w/index.php?title=Export\_Administration\_Regulations&oldid=1344457832][ref_ear]
- "Federal Aviation Administration." 2026. Wikipedia. Last modified May 30, at 03:43 (UTC). [https://en.wikipedia.org/w/index.php?title=Federal\_Aviation\_Administration&oldid=1356839483][ref_faa]
- "General Data Protection Regulation." 2026. Wikipedia. Last modified May 26, at 02:27 (UTC). [https://en.wikipedia.org/w/index.php?title=General\_Data\_Protection\_Regulation&oldid=1356164558][ref_gdpr]
- "Geofence." 2026. Wikipedia. Last modified April 27, at 04:15 (UTC). [https://en.wikipedia.org/w/index.php?title=Geofence&oldid=1351302031][ref_geofence]
- "International Civil Aviation Organization." 2026. Wikipedia. Last modified May 14, at 22:05 (UTC). [https://en.wikipedia.org/w/index.php?title=International\_Civil\_Aviation\_Organization&oldid=1354193425][ref_icao]
- "International Telecommunication Union." 2026. Wikipedia. Last modified May 21, at 11:54 (UTC). [https://en.wikipedia.org/w/index.php?title=International\_Telecommunication\_Union&oldid=1355361388][ref_itu]
- "International Traffic in Arms Regulations." 2026. Wikipedia. Last modified March 6, at 15:46 (UTC). [https://en.wikipedia.org/w/index.php?title=International\_Traffic\_in\_Arms\_Regulations&oldid=1342029930][ref_itar]
- "Just Culture." 2025. Wikipedia. Last modified May 25, at 06:39 (UTC). [https://en.wikipedia.org/w/index.php?title=Just\_culture&oldid=1292104615][ref_just_culture]
- "Kármán Line." 2026. Wikipedia. Last modified May 22, at 09:06 (UTC). [https://en.wikipedia.org/w/index.php?title=K%C3%A1rm%C3%A1n\_line&oldid=1355518761][ref_karman]
- "Kinetic Energy." 2026. Wikipedia. Last modified April 30, at 15:06 (UTC). [https://en.wikipedia.org/w/index.php?title=Kinetic\_energy&oldid=1351851317][ref_kinetic_energy]
- "Outer Space Treaty." 2026. Wikipedia. Last modified April 2, at 14:25 (UTC). [https://en.wikipedia.org/w/index.php?title=Outer\_Space\_Treaty&oldid=1346727738][ref_ost]
- "Range Safety." 2026. Wikipedia. Last modified April 21, at 15:22 (UTC). [https://en.wikipedia.org/w/index.php?title=Range\_safety&oldid=1350372637][ref_flight_termination]
- "Regulation of Unmanned Aerial Vehicles." 2026. Wikipedia. Last modified April 22, at 17:03 (UTC). [https://en.wikipedia.org/w/index.php?title=Regulation\_of\_unmanned\_aerial\_vehicles&oldid=1350564129][ref_uav_regulation]
- "Remote ID." 2026. Wikipedia. Last modified May 2, at 14:24 (UTC). [https://en.wikipedia.org/w/index.php?title=Remote\_ID&oldid=1352168971][ref_remote_id]
- "Safety Management System." 2026. Wikipedia. Last modified May 12, at 13:53 (UTC). [https://en.wikipedia.org/w/index.php?title=Safety\_management\_system&oldid=1353808198][ref_sms]
- "Space Law." 2026. Wikipedia. Last modified May 30, at 21:09 (UTC). [https://en.wikipedia.org/w/index.php?title=Space\_law&oldid=1356948620][ref_space_law]
- "Transport Canada." 2026. Wikipedia. Last modified May 26, at 07:07 (UTC). [https://en.wikipedia.org/w/index.php?title=Transport\_Canada&oldid=1356194109][ref_transport_canada]
- "Type Certificate." 2025. Wikipedia. Last modified August 18, at 21:16 (UTC). [https://en.wikipedia.org/w/index.php?title=Type\_certificate&oldid=1306633418][ref_type_cert]
- "Unmanned Aerial Vehicle." 2026. Wikipedia. Last modified May 30, at 14:34 (UTC). [https://en.wikipedia.org/w/index.php?title=Unmanned\_aerial\_vehicle&oldid=1356899069][ref_bvlos]
- "Unmanned Aircraft System Traffic Management." 2026. Wikipedia. Last modified May 8, at 00:50 (UTC). [https://en.wikipedia.org/w/index.php?title=Unmanned\_aircraft\_system\_traffic\_management&oldid=1353074426][ref_uspace]
- "Vehicular Automation." 2026. Wikipedia. Last modified May 13, at 04:18 (UTC). [https://en.wikipedia.org/w/index.php?title=Vehicular\_automation&oldid=1353915684][ref_automation]
- "Wassenaar Arrangement." 2026. Wikipedia. Last modified March 25, at 11:57 (UTC). [https://en.wikipedia.org/w/index.php?title=Wassenaar\_Arrangement&oldid=1345302772][ref_wassenaar]

### Related Posts

- Sechter, Brendan. 2026. "Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass." *Brendan A R Sechter's Development Blog*, May 30. [https://sgeos.github.io/aerospace/engineering/3d-printing/2026/05/30/prototyping\_fixed\_wing\_aircraft\_with\_lightweight\_pla\_and\_fiberglass.html][related_post_prototyping]
- Sechter, Brendan. 2026. "Guidance, Navigation, and Automatic Landing for Fixed-Wing UAVs." *Brendan A R Sechter's Development Blog*, June 8. [https://sgeos.github.io/aerospace/engineering/uav/2026/06/08/guidance\_navigation\_and\_automatic\_landing\_for\_fixed\_wing\_uavs.html][related_post_gnc]
- Sechter, Brendan. 2026. "Communications and the Command-and-Control Data Link for Fixed-Wing UAVs." *Brendan A R Sechter's Development Blog*, June 9. [https://sgeos.github.io/aerospace/engineering/uav/2026/06/09/communications\_and\_the\_command\_and\_control\_data\_link\_for\_fixed\_wing\_uavs.html][related_post_comms]
- Sechter, Brendan. 2026. "Structures and the Flight Envelope for Fixed-Wing UAVs." *Brendan A R Sechter's Development Blog*, June 10. [https://sgeos.github.io/aerospace/engineering/uav/2026/06/10/structures\_and\_the\_flight\_envelope\_for\_fixed\_wing\_uavs.html][related_post_structures]
- Sechter, Brendan. 2026. "Payload and Mission Systems for Fixed-Wing UAVs." *Brendan A R Sechter's Development Blog*, June 13. [https://sgeos.github.io/aerospace/engineering/uav/2026/06/13/payload\_and\_mission\_systems\_for\_fixed\_wing\_uavs.html][related_post_payload]

[ref_air_rights]: https://en.wikipedia.org/w/index.php?title=Air_rights&oldid=1331576511
[ref_air_safety]: https://en.wikipedia.org/w/index.php?title=Aviation_safety&oldid=1357097957
[ref_airspace_class]: https://en.wikipedia.org/w/index.php?title=Airspace&oldid=1352848546
[ref_airworthiness]: https://en.wikipedia.org/w/index.php?title=Airworthiness&oldid=1323124816
[ref_automation]: https://en.wikipedia.org/w/index.php?title=Vehicular_automation&oldid=1353915684
[ref_bvlos]: https://en.wikipedia.org/w/index.php?title=Unmanned_aerial_vehicle&oldid=1356899069
[ref_caa_uk]: https://en.wikipedia.org/w/index.php?title=Civil_Aviation_Authority_(United_Kingdom)&oldid=1356574669
[ref_caac]: https://en.wikipedia.org/w/index.php?title=Civil_Aviation_Administration_of_China&oldid=1353043294
[ref_casa]: https://en.wikipedia.org/w/index.php?title=Civil_Aviation_Safety_Authority&oldid=1332126203
[ref_chicago]: https://en.wikipedia.org/w/index.php?title=Convention_on_International_Civil_Aviation&oldid=1324626701
[ref_daa]: https://en.wikipedia.org/w/index.php?title=Detect_and_avoid&oldid=1307759350
[ref_ear]: https://en.wikipedia.org/w/index.php?title=Export_Administration_Regulations&oldid=1344457832
[ref_easa]: https://en.wikipedia.org/w/index.php?title=European_Union_Aviation_Safety_Agency&oldid=1356601234
[ref_faa]: https://en.wikipedia.org/w/index.php?title=Federal_Aviation_Administration&oldid=1356839483
[ref_flight_termination]: https://en.wikipedia.org/w/index.php?title=Range_safety&oldid=1350372637
[ref_gdpr]: https://en.wikipedia.org/w/index.php?title=General_Data_Protection_Regulation&oldid=1356164558
[ref_geofence]: https://en.wikipedia.org/w/index.php?title=Geofence&oldid=1351302031
[ref_icao]: https://en.wikipedia.org/w/index.php?title=International_Civil_Aviation_Organization&oldid=1354193425
[ref_itar]: https://en.wikipedia.org/w/index.php?title=International_Traffic_in_Arms_Regulations&oldid=1342029930
[ref_itu]: https://en.wikipedia.org/w/index.php?title=International_Telecommunication_Union&oldid=1355361388
[ref_just_culture]: https://en.wikipedia.org/w/index.php?title=Just_culture&oldid=1292104615
[ref_karman]: https://en.wikipedia.org/w/index.php?title=K%C3%A1rm%C3%A1n_line&oldid=1355518761
[ref_kinetic_energy]: https://en.wikipedia.org/w/index.php?title=Kinetic_energy&oldid=1351851317
[ref_ost]: https://en.wikipedia.org/w/index.php?title=Outer_Space_Treaty&oldid=1346727738
[ref_remote_id]: https://en.wikipedia.org/w/index.php?title=Remote_ID&oldid=1352168971
[ref_sms]: https://en.wikipedia.org/w/index.php?title=Safety_management_system&oldid=1353808198
[ref_space_law]: https://en.wikipedia.org/w/index.php?title=Space_law&oldid=1356948620
[ref_transport_canada]: https://en.wikipedia.org/w/index.php?title=Transport_Canada&oldid=1356194109
[ref_type_cert]: https://en.wikipedia.org/w/index.php?title=Type_certificate&oldid=1306633418
[ref_uav_regulation]: https://en.wikipedia.org/w/index.php?title=Regulation_of_unmanned_aerial_vehicles&oldid=1350564129
[ref_uspace]: https://en.wikipedia.org/w/index.php?title=Unmanned_aircraft_system_traffic_management&oldid=1353074426
[ref_utm]: https://en.wikipedia.org/w/index.php?title=Unmanned_aircraft_system_traffic_management&oldid=1353074426
[ref_wassenaar]: https://en.wikipedia.org/w/index.php?title=Wassenaar_Arrangement&oldid=1345302772
[related_post_comms]: {% post_url 2026-06-09-communications_and_the_command_and_control_data_link_for_fixed_wing_uavs %}
[related_post_gnc]: {% post_url 2026-06-08-guidance_navigation_and_automatic_landing_for_fixed_wing_uavs %}
[related_post_payload]: {% post_url 2026-06-13-payload_and_mission_systems_for_fixed_wing_uavs %}
[related_post_prototyping]: {% post_url 2026-05-30-prototyping_fixed_wing_aircraft_with_lightweight_pla_and_fiberglass %}
[related_post_structures]: {% post_url 2026-06-10-structures_and_the_flight_envelope_for_fixed_wing_uavs %}
[research_easa]: https://www.easa.europa.eu/en/domains/civil-drones
[research_icao]: https://www.icao.int/safety/UA/Pages/default.aspx
[research_jarus]: http://jarus-rpas.org/
