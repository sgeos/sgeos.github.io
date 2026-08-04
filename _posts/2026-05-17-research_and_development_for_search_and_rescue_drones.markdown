---
layout: post
mathjax: false
comments: true
title:  "Research and Development for Search and Rescue Drones"
date:   2026-05-17 09:00:00 +0000
categories: aerospace engineering uav search-and-rescue research-and-development
series: search_and_rescue_drones
series_title: Search and Rescue Drones
series_index: 3
---
<!-- A147 -->
<script>console.log("A147");</script>

[The first article in this series][related_post_a145_physics]
analysed
the physics and economics
of fixed-wing, multicopter,
and hybrid vertical-takeoff-and-landing
drones
for search and rescue.
[The second article][related_post_a146_buying]
gave
a buyer's decision framework
for acquiring
the platforms
the first article described.
This article addresses
the program
that has decided
that off-the-shelf platforms
do not solve
its problem,
or that
its program staff
includes
engineers
with the capacity
to extend
the commercial platforms
into novel capability.
The article addresses
how a search and rescue program
builds, modifies,
or partners with others to build
unmanned aerial vehicles
beyond what the commercial market provides.

The research and development audience
is smaller
than the buyer audience.
Most search and rescue programs
buy.
The R&D audience
includes
academic search and rescue research groups,
federal labs
that pursue SAR-relevant capability,
public safety agencies
with embedded engineering staff,
small business
SBIR and STTR awardees,
and the contractor base
that supports them.
The framework
that follows
addresses
the decisions
each of these
faces.

## The Build-Versus-Buy Frame

A research and development program
exists
because
the buyer's market
does not solve
the program's problem.
The question
the program must answer first
is whether
the gap
is large enough
to justify
the development cost.

**Build the whole platform.**
A custom airframe,
a custom autopilot,
custom payloads,
and a custom ground control system.
This option
applies
when the operational concept
is genuinely new,
when the platform's flight envelope
is outside
what commercial aircraft offer,
when the regulatory environment
demands
a clean-sheet certification approach,
or when
the program's funding
admits multi-year
clean-sheet development.
The cost
runs
millions to tens of millions of dollars
in engineering hours
and verification effort.

**Modify a commercial platform.**
A commercial airframe
and autopilot
combined with
a custom payload,
a custom mission algorithm,
or a custom autonomous behaviour.
This option
applies
when the commercial platform's flight envelope
is acceptable
but its sensor suite,
its mission planner,
or its autonomy
does not meet the operational need.
The cost
runs
tens of thousands to several hundred thousand dollars
in engineering hours
plus the cost of the platform
plus the cost of the payload hardware.

**Buy and integrate.**
A commercial platform
with a manufacturer-supported
third-party payload integration.
This option
applies
when the commercial platform plus an existing third-party sensor
solves the problem,
even if the integration
requires custom mounting
or custom ground control configuration.
The cost
runs
the platform price
plus the payload price
plus a small integration budget.
This is the path
that
[the buyer's framework in A146][related_post_a146_buying]
addresses.

A program manager
deciding among the three options
should ask
three questions
in order.

**First, does an off-the-shelf platform with an existing payload solve the problem?**
If yes,
buy and integrate.
The cost and schedule
of build or modify
are not justified.
The off-the-shelf market
in 2026
covers
the dominant search-and-rescue
mission profiles
in the small unmanned aerial vehicle class.
[The DJI Payload SDK][ref_dji_payload_sdk],
[the Skydio Connect ecosystem][ref_skydio_connect],
the
[Parrot ANAFI Ai Open Flight Control][ref_parrot_open_flight_control],
and the manufacturer-supported third-party integrations
each
admit
several
sensor and payload combinations
that
small organisations
should exhaust
before considering
modification.

**Second, can a commercial platform with a custom payload solve the problem?**
If yes,
modify.
A custom payload
on a stable commercial platform
delivers
most of the engineering benefit
of a full custom build
at one tenth
the cost.
The modification path
permits
custom sensors,
custom communications equipment,
custom mission planning,
and custom autonomous behaviour,
all of which
the commercial platforms admit
through their software development kits.

**Third, does the operational concept require a clean-sheet platform?**
If yes,
build.
A clean-sheet platform
is justified
by
a novel mission profile,
a unique flight envelope,
or
a regulatory environment
that requires
a certification path
that commercial platforms
do not provide.
The Defense Advanced Research Projects Agency's
[OFFSET swarm programme][ref_darpa_offset],
the
[Subterranean Challenge][ref_darpa_subt]
legacy programmes,
and several
NASA Aeronautics Research Mission Directorate
projects
illustrate
the categories
that
warrant clean-sheet development.

The order matters.
A program manager
who reaches Question Three first
without exhausting Question One and Two
will commit
to a build
that
a third-party integration
could have delivered
at one twentieth the cost.

## When to Build, When to Modify, When to Buy

A small number of operational properties
distinguish the three options
within the search and rescue domain.

**Custom flight envelope.**
A platform that must fly
in
high winds beyond commercial certification,
in
high altitude
above commercial service ceilings,
in
icing conditions
beyond commercial qualification,
or in
combined airspace
not covered by commercial classifications
requires a custom airframe
or a substantially modified commercial one.
Most search-and-rescue missions
fall within
the commercial flight envelope.
The exceptions
are wildfire reconnaissance
in the smoke column,
high-altitude rescue
in alpine terrain,
or
multi-aircraft operations
in classified airspace.

**Custom sensor integration.**
A sensor not available
through manufacturer-supported integration
requires
custom mounting,
custom power management,
custom data downlink,
and custom mission planning.
The
[FLIR Boson Plus][ref_flir_boson_plus],
the
[Workswell WIRIS series][ref_workswell_wiris],
the
[Sierra Olympia Vinden][ref_sierra_olympia_vinden],
and
the
[LightWare LiDAR series][ref_lightware_lidar]
are commonly integrated
through manufacturer programmes.
A sensor not on the supported list
requires custom integration work
at the modification tier.

**Novel autonomous behaviour.**
An autonomous algorithm
not provided
by the platform's stock firmware
requires
either
a software development kit application
on top of the commercial autopilot
or
a fully open-source autopilot
running on commodity hardware.
[PX4 Autopilot][ref_px4]
and
[ArduPilot][ref_ardupilot]
are the open-source autopilots
that admit
algorithm-level modification.
[The Robot Operating System version 2][ref_ros_2]
provides
the higher-level
distributed software architecture
that connects
custom algorithms
to the autopilot.

**Multi-aircraft coordination.**
A program developing
swarm or multi-aircraft coordination
beyond the manufacturer-supported
multi-drone management
needs
custom communications,
custom mission planning,
and custom autonomy.
The DARPA OFFSET programme
demonstrated
several hundred unmanned aerial vehicles
operating cooperatively
under custom coordination algorithms.
A small search and rescue program
typically lacks
the budget
to replicate this work
from scratch
but can adopt
its published results
through ROS 2 and PX4 integration.

**Custom communications.**
A platform operating
on
encrypted communications,
multi-band downlink,
mesh networking,
or low-probability-of-intercept waveforms
requires
custom radio integration
that commercial platforms
do not provide.
The
[Doodle Labs Mesh Rider][ref_doodle_labs]
and
the
[Silvus Technologies StreamCaster][ref_silvus_streamcaster]
are commercial mesh radios
that drone integrators commonly use
at the modification tier.

The decision rule
is that
each additional custom requirement
moves the program
one tier
toward custom build.
A program
with no custom requirements
buys.
A program
with one custom requirement
modifies.
A program
with three or more
custom requirements
builds.
The boundary
is approximate,
because
a single very demanding requirement
can justify a build
where two modest requirements
can be satisfied through modification.

## Federal R&D Funding for SAR Drones

A search and rescue research and development program
funded
through federal grants
draws
from a small number
of recurring sources.

**Department of Homeland Security
Science and Technology Directorate.**
[The DHS S&T Directorate][ref_dhs_st]
operates
several programmes
that fund unmanned aerial vehicle
research and development
for first responder applications.
The
[Long Range Broad Agency Announcement][ref_dhs_st_lrbaa]
allows
proposals
in
all hazards
emergency response capability,
including
search and rescue.
The
[First Responder Capability Group][ref_dhs_first_responders]
identifies
operational gaps
that the Directorate then funds
through research solicitations.
The
[Small Business Innovation Research programme at DHS S&T][ref_dhs_sbir]
supports
proposals
in topics released
each year.

**Small Business Innovation Research
and Small Business Technology Transfer.**
[The federal SBIR and STTR programmes][ref_sbir_gov]
are the dominant federal funding source
for small-business-led research
in search-and-rescue-relevant technology.
[The thirteen-article SBIR and STTR practitioner playbook
in this series][related_post_a132_sbir_intro]
addresses
the programme mechanics
in depth.
[The Department of Defense SBIR portal][ref_dod_sbir]
lists topics
each cycle
that include
small unmanned aerial vehicle technology,
sensor development,
autonomous behaviour,
and command-and-control software.
DHS, NASA, NIST, NOAA, and the Department of the Interior
each release SBIR topics
relevant to search and rescue
on regular cycles.

**National Institute of Standards and Technology
Public Safety Communications Research Division.**
[The NIST Public Safety Communications Research Division][ref_nist_pscr]
funds
research
in communications, location services,
and analytics
for public safety applications
including search and rescue.
PSCR's
[Open Innovation programme][ref_pscr_open_innovation]
admits
small-business and academic proposals
through periodic prize challenges
and grant opportunities.

**National Institute of Standards and Technology
Robotic Systems for Smart Manufacturing
and the Standard Test Methods programme.**
[NIST's Standard Test Methods for Small Unmanned Aircraft Systems][ref_nist_tests]
provide
the test infrastructure
and the proficiency benchmarks
that
public safety operators
use
for platform and operator evaluation.
A research and development programme
that targets
performance against these tests
inherits
an objective benchmark
that
agencies recognise.

**National Aeronautics and Space Administration
Aeronautics Research Mission Directorate.**
[NASA's UAS in the National Airspace System project][ref_nasa_uas_nas]
funds
research
in
beyond visual line of sight operations,
detect-and-avoid systems,
command-and-control reliability,
and
human-machine teaming.
These programmes
target
the regulatory and operational gaps
that current commercial platforms
cannot operate through
under standard waivers.

**National Science Foundation.**
[The NSF Cyber-Physical Systems programme][ref_nsf_cps]
and
[the Smart and Connected Communities programme][ref_nsf_scc]
fund
academic research
in autonomous systems,
search algorithms,
and the deployment of unmanned aerial vehicles
in public-safety applications.
Both programmes
admit
collaborative proposals
between universities
and operational partners.

**Department of Energy national laboratories.**
The
[Department of Energy national laboratory complex][ref_doe_labs],
notably
Sandia,
Oak Ridge,
Idaho National,
and Pacific Northwest National Laboratories,
operates
unmanned aerial vehicle research programmes
that
admit
[Cooperative Research and Development Agreements][ref_crada]
with external partners
including
state and local search-and-rescue agencies.
The
[Sandia
Unmanned Aerial Vehicle research programme][ref_sandia_uas],
in particular,
has historical experience
with
SAR-adjacent missions.

**Defense Advanced Research Projects Agency.**
[DARPA][ref_darpa]
funds
the highest-risk
unmanned aerial vehicle research
in the federal portfolio.
Recent and ongoing programmes
including the
[OFFSET swarm programme][ref_darpa_offset]
and the
[Subterranean Challenge][ref_darpa_subt]
have produced
technology and software releases
that
search and rescue research and development programmes
incorporate
into their own work.

A program manager
constructing
a federal funding strategy
typically draws
from two or three of these sources
in combination.
The
[strategy and portfolio article
in the SBIR and STTR playbook][related_post_a142_strategy]
addresses
the multi-source funding strategy
in depth.

## University and Federal Lab Partnerships

A search and rescue R&D program
operating at any scale
benefits from
partnerships with
universities,
federally funded research and development centres,
and the FAA's designated unmanned aerial vehicle test sites.
These partners
bring
technical capacity,
access to airspace and certifications,
and federal funding pipelines
that smaller programmes lack.

**The Federal Aviation Administration
Unmanned Aircraft Systems Test Sites.**
The FAA
designated
[the original six unmanned aerial vehicle test sites][ref_faa_uas_test_sites]
on 30 December 2013
and added
the University of Alaska Fairbanks
as the seventh
in early 2014
to support unmanned aircraft research,
operations, and testing.
The current sites
include the
[Lone Star Unmanned Aircraft Systems
Centre of Excellence and Innovation at
Texas A&M University][ref_texas_am_lone_star],
the
[Northern Plains Unmanned Aircraft Systems Test Site
in North Dakota][ref_northern_plains],
the
[Mid-Atlantic Aviation Partnership at Virginia Tech][ref_maap],
the
[Nevada Autonomous programme at the
University of Nevada Reno][ref_nias]
(which absorbed the original
Nevada Institute for Autonomous Systems
in March 2022),
the
[University of Alaska Fairbanks Alaska Centre
for Unmanned Aircraft Systems Integration][ref_acuasi],
the
[New York UAS Test Site at Griffiss International Airport][ref_griffiss],
and the
[University of Maryland Research and Operations Center][ref_umd_uroc]
(the former University of Maryland UAS Test Site,
rebranded in October 2022).
A research and development programme
operating in or near
one of the test sites
can partner with the site
for restricted airspace access,
test infrastructure,
and certified test conductors.

**The Mississippi State University
Raspet Flight Research Laboratory.**
[Raspet][ref_raspet]
is the longest-running
unmanned aircraft research laboratory
in the United States university system,
operating
under
the Federal Aviation Administration's
[Centre of Excellence for Unmanned Aircraft Systems][ref_faa_coe_uas].
Raspet's
research
includes
beyond visual line of sight operations,
multi-aircraft coordination,
sensor integration,
and the certification pathway
for medium unmanned aircraft.

**Carnegie Mellon University
National Robotics Engineering Centre.**
The
[National Robotics Engineering Centre][ref_nrec]
operates
unmanned aerial vehicle programmes
that include
SAR-relevant autonomy,
multi-vehicle coordination,
and
field deployment
of research platforms
in operational scenarios.

**Massachusetts Institute of Technology
Lincoln Laboratory.**
[MIT Lincoln Laboratory][ref_mit_lincoln_lab]
operates
unmanned aerial vehicle research programmes
including
[the Search-and-Rescue Optical
Technology Demonstration][ref_mit_ll_sar],
which
develops
optical sensors and search algorithms
for finding humans
in distress
from aerial platforms.

**Johns Hopkins University
Applied Physics Laboratory.**
[Johns Hopkins APL][ref_jhuapl]
operates
unmanned aerial vehicle programmes
including
autonomous mission planning,
multi-domain operations,
and
the research-to-operations transition
of unmanned systems
into federal and state agency use.

**Naval Postgraduate School
Consortium for Robotics and Unmanned Systems
Education and Research.**
[CRUSER at the Naval Postgraduate School][ref_nps_cruser]
operates
several unmanned aerial vehicle research programmes
and
permits
collaborative arrangements
with public safety agencies
through formal partnership agreements.

A program manager
approaching
a university or federally funded research and development centre
should expect
the partnership negotiation
to consume
six to twelve months
through
the formal proposal,
the intellectual property and data rights review,
the security review,
and the contracting cycle.
A pre-existing relationship
through prior collaboration
or a personal connection
to the partner's staff
shortens the cycle substantially.

## The Software Development Kit and Simulator Landscape

A research and development program
working at the modification tier
uses
the platform vendor's software development kit
and one or more flight simulators
to develop
custom algorithms
before deploying them
on operational hardware.

### Vendor Software Development Kits

**DJI software development kits.**
DJI publishes
three SDK families
for different layers of the stack.
[The DJI Mobile SDK][ref_dji_mobile_sdk]
allows
Android and iOS applications
that
communicate with
the drone
through the remote control.
[The DJI Onboard SDK][ref_dji_onboard_sdk]
supports
embedded applications
running on
a companion computer attached to the drone
that
controls the autopilot
through a serial link.
[The DJI Payload SDK][ref_dji_payload_sdk]
admits
custom payload integration
on the
M300, M350, M400, and M30 series airframes
through a hardware-software interface
that the manufacturer supports
for third-party sensor and accessory development.

**Parrot software development kits.**
Parrot's
[Olympe SDK][ref_parrot_olympe]
permits
Python applications
that
communicate with
Parrot ANAFI Ai, Anafi USA, and related drones
through
the Parrot Air SDK protocol.
The
[Parrot Air SDK][ref_parrot_air_sdk]
provides
the on-board API
for custom payload
and autonomous behaviour
development.
Parrot's
[Open Flight Control][ref_parrot_open_flight_control]
on the ANAFI Ai
allows
deeper firmware modification
than Parrot's smaller platforms.

**Skydio software development kit.**
Skydio's
[Connect ecosystem][ref_skydio_connect]
supports
third-party integrations
on the Skydio X10 platform
through
manufacturer-supported APIs.
Skydio's
public software development kit
is more constrained
than the DJI and Parrot options
because Skydio
provides
the autonomy stack
as a closed system.

### Open-Source Autopilots

**PX4 Autopilot.**
[PX4][ref_px4]
is an open-source autopilot
that runs
on
the Pixhawk family of hardware,
the Holybro family,
and several other Pixhawk-compatible boards.
PX4
admits
the
[MAVLink protocol][ref_mavlink]
for ground control station communication
and the
[uORB middleware][ref_uorb]
for inter-process communication
within the flight stack.
PX4
also permits
[hardware-in-the-loop][ref_px4_hitl]
and
[software-in-the-loop simulation][ref_px4_sitl]
for algorithm development
before deployment on real hardware.

**ArduPilot.**
[ArduPilot][ref_ardupilot]
is the other dominant open-source autopilot,
older than PX4
and with a wider hardware support matrix.
ArduPilot
includes
several variants
including
ArduCopter, ArduPlane, ArduRover,
and ArduSub
for different vehicle classes.
ArduPilot
uses the same
MAVLink protocol
as PX4
for ground communication.

### Robot Operating System Version 2

[ROS 2][ref_ros_2]
is the open-source middleware
that drone research and development programmes
use to build
the higher-level software stack
above
the autopilot.
ROS 2
provides
distributed publish-subscribe communication,
service-and-action patterns,
and the launch and configuration infrastructure
that
custom autonomy algorithms
rely on.
[The PX4 ROS 2 bridge][ref_px4_ros2]
and
the
[ArduPilot ROS 2 bridge][ref_ardupilot_ros2]
admit
the higher-level ROS 2 application
to communicate with
the underlying autopilot
without modifying
the autopilot itself.

### Simulators

**PX4 Software in the Loop.**
[PX4 SITL][ref_px4_sitl]
runs the autopilot firmware
on a host computer
without the hardware,
connected to
a flight dynamics simulator
for
algorithm testing.
The default flight dynamics simulator
for PX4 SITL
is
[Gazebo Garden][ref_gazebo],
the open-source
robotics simulator
maintained by
[Open Robotics][ref_open_robotics].

**ArduPilot SITL.**
[ArduPilot SITL][ref_ardupilot_sitl]
provides
the equivalent capability
for the ArduPilot autopilot.

**Microsoft AirSim and its successors.**
[Microsoft AirSim][ref_airsim]
was an Unreal Engine
based
drone and ground vehicle simulator
that
the academic research community
adopted widely
in the late 2010s
and early 2020s.
Microsoft Research
[archived AirSim in July 2022][ref_airsim_archived]
and
released
its successor
Project AirSim
as a commercial Microsoft Azure product,
which Microsoft itself
[discontinued on 15 December 2023][ref_project_airsim_discontinued],
laying off the development team.
The lineage
is continued
by
[IAMAI Simulations][ref_iamai],
a spinout of
the former Microsoft team.
A program adopting AirSim today
either
uses the archived open-source version
in its frozen state,
migrates to
the IAMAI continuation,
or selects
a successor simulator
from the current open landscape.

**NVIDIA Isaac Sim and Isaac for AMR.**
[NVIDIA Isaac Sim][ref_nvidia_isaac_sim]
is a robotics simulator
built on NVIDIA's
Omniverse platform
that supports
unmanned aerial vehicle simulation
through
the Isaac for autonomous mobile robots package.
Isaac Sim
is closed source
but is free for non-commercial use
and is the dominant simulator
in the NVIDIA robotics ecosystem.

**MathWorks UAV Toolbox.**
[The MathWorks UAV Toolbox][ref_matlab_uav_toolbox]
extends
MATLAB and Simulink
with
flight dynamics models,
sensor models,
and the
hardware-in-the-loop infrastructure
that
algorithm development programmes use
to bridge from MATLAB simulation
to flight test.

A research and development programme
typically uses
two or three simulators
across its development cycle,
each at a different fidelity tier.
A high-fidelity simulator
for the dynamics
and a fast simulator
for the autonomy stack
are a common combination.

## Custom Payload Development

A research and development program
modifying a commercial platform
typically focuses
on
the payload integration
because
the payload is the part
of the platform
that
the operational concept
differentiates against.

**Autopilot hardware.**
A custom platform
or a deeply modified commercial platform
runs
[PX4][ref_px4]
or
[ArduPilot][ref_ardupilot]
on
the
[Pixhawk family of autopilot hardware][ref_pixhawk],
the
[Holybro family][ref_holybro],
the
[mRo Robotics family][ref_mro_robotics],
or another Pixhawk-compatible board.
The autopilot hardware
typically costs
two hundred to one thousand US dollars
per unit
and lasts
the life of the platform.

**Thermal infrared payloads.**
The dominant search-and-rescue
thermal payload vendor
is
[Teledyne FLIR][ref_teledyne_flir],
which offers
the Boson and Boson Plus families
for small platform integration
and the Tau series
for medium platforms.
The
[Workswell WIRIS series][ref_workswell_wiris]
provides
mid-range thermal payloads
with integrated gimbals.
The
[Sierra Olympia Vinden series][ref_sierra_olympia_vinden]
provides
higher-end
multi-sensor payloads.
Thermal payload pricing
ranges from
one thousand dollars
for an uncooled module
to thirty thousand dollars
for a cooled high-resolution payload.

**LiDAR payloads.**
Small-form-factor LiDAR
for unmanned aerial vehicle applications
comes from
[LightWare LiDAR][ref_lightware_lidar],
[Velodyne and Ouster][ref_ouster],
and several other vendors.
LiDAR pricing
runs
one thousand to twenty thousand dollars
per unit
depending on range and resolution.

**Custom electronics.**
A platform
that requires
custom signal conditioning,
custom power management,
or
custom communications
typically uses
commercial off-the-shelf microcontroller boards
including the
[Raspberry Pi][ref_raspberry_pi]
or
[NVIDIA Jetson][ref_nvidia_jetson]
families
as companion computers
on the airframe.
The Jetson
in particular
provides
the embedded compute
that
real-time computer vision
and autonomous navigation
require.

**Mounts and structural integration.**
Custom mounts
are typically
three-dimensionally printed
in
polyamide or carbon-reinforced filament
for prototype work
and
machined aluminium or carbon-composite
for production.
Mount design
must account for
vibration isolation,
balance and centre of gravity,
electrical interference shielding,
and
the platform's stated payload-attachment specifications.

**National Defense Authorization Act compliance.**
A platform
intended for federal procurement
under the
[Federal Acquisition Regulation provision 52.240-1][ref_far_52_240_1]
must source
its components
from
the
[Defense Innovation Unit Blue UAS Framework][ref_diu_legacy_blue_uas]
of cleared components
or
through
the
[Defense Contract Management Agency
Blue UAS Cleared List][ref_blue_uas_list].
A research and development program
designing
a future commercial product
that targets federal customers
benefits from
designing-in
NDAA-compliant components
from the start.

## Regulatory Pathways for Experimental Aircraft

A research and development program
operating
a novel or modified platform
faces
a regulatory pathway
that
buyers
of certified commercial platforms
do not face.

**FAA Part 107 commercial operations.**
[Part 107][ref_faa_part_107]
applies to commercial unmanned aircraft operations
of platforms
weighing less than
fifty-five pounds gross takeoff weight.
A research and development program
operating a modified DJI or Skydio platform
under fifty-five pounds
can typically operate
under Part 107
without additional certification
beyond the remote pilot certificate.

**FAA Section 44807 exemption.**
[Section 44807 of Title 49 United States Code][ref_section_44807]
allows
the Secretary of Transportation
to grant exemptions
from the standard commercial-operations rules
for unmanned aircraft research and operations.
A research and development program
operating
a platform above fifty-five pounds gross takeoff weight,
or operating
in a manner that Part 107 does not admit,
applies for a Section 44807 exemption
through the FAA.
The exemption process
typically takes
six to eighteen months
from application to grant.

**FAA Certificate of Waiver or Authorization.**
[A Certificate of Waiver or Authorization][ref_faa_coa]
supports
a public agency or research organisation
to operate
unmanned aircraft
in a specified airspace
under specified conditions
for a specified period.
The seven FAA UAS Test Sites
operate
under blanket COAs
that admit
research operations within their boundaries.
A program partnering with a test site
inherits
the test site's regulatory authority
for the duration
of the partnership.

**FAA Special Airworthiness Certification.**
[A Special Airworthiness Certificate][ref_faa_special_airworthiness]
admits
an experimental aircraft
to fly
under specified conditions
without
full type certification.
A research and development program
operating
a custom-built platform
typically operates
under a Special Airworthiness Certificate
in the experimental category
for the development phase,
then
pursues
[Type Certification][ref_faa_type_certification]
through
[the Aircraft Certification Service][ref_faa_acs]
for production
and commercial sale.

**Beyond visual line of sight operations.**
A research and development program
exploring
beyond visual line of sight operations
operates
under
[the FAA Part 108 Notice of Proposed Rulemaking][ref_part_108]
when finalised,
or
under
exemptions
granted through
Section 44807
or
the Centres of Excellence pathway,
until then.
The
[Centres of Excellence for Unmanned Aircraft Systems][ref_faa_coe_uas]
maintain
multi-agency BVLOS authorisations
that
research programs partnered with the Centres
can operate under.

The regulatory pathway
substantially affects
the program schedule.
A research and development program
that plans
to operate
under Part 107
inherits
a faster development cycle
than a program
that requires
Section 44807 exemptions
or
Special Airworthiness Certificates.
The program manager
should align
the platform design choices
with the intended regulatory pathway
from the outset.

## Intellectual Property in Federally Funded Search and Rescue Research

A research and development program
funded
through federal grants
operates
under
a specific
intellectual property regime
that
the program manager
must understand
before
signing the award agreement.

**The Bayh-Dole Act.**
[The Bayh-Dole Act of 1980][ref_bayh_dole],
codified at
35 USC 200-212,
permits
universities, non-profits,
and small businesses
to retain ownership
of inventions
made under federal funding,
subject to
the government's march-in rights,
the government's royalty-free license
for government use,
and reporting requirements
to
the awarding agency.
A research and development program
working under
SBIR, STTR, NSF, NIH, NASA, DOE, or DHS funding
operates
under Bayh-Dole.
The program manager
must
record inventions,
file patent applications
within the statutory deadlines,
and
provide
the government license
on each invention.

**SBIR and STTR data rights.**
[The federal SBIR and STTR data rights regime][ref_sbir_data_rights],
revised by the Small Business Administration's May 2019
SBIR Policy Directive
and codified for Department of Defense contracts
under the
[Defense Federal Acquisition Regulation Supplement
final rule effective 17 January 2025][ref_dfars_sbir_2025],
protects
the small business's
technical data
and computer software
generated under
SBIR or STTR funding
from
government release
to third parties
for a uniform
twenty-year period
that begins
on the award completion.
The pre-2019 regime,
which provided
a four-year initial protection
followed by twelve years of
SBIR data rights,
no longer applies.
A program manager
operating under
the current regime
should plan
the commercialisation strategy
against the full twenty-year window.
The
[data rights and intellectual property article
in the SBIR and STTR playbook][related_post_a139_data_rights]
addresses
the data rights regime
in depth.

**Cooperative Research and Development Agreements.**
[The Stevenson-Wydler Technology Innovation Act][ref_stevenson_wydler]
authorises
federal laboratories
to enter
[Cooperative Research and Development Agreements][ref_crada]
with non-federal partners
including
state and local agencies,
universities,
and businesses.
A CRADA
defines
the rights to data,
patent rights,
and
exclusive licensing options
for inventions
made under
the agreement.
A program manager
considering
a Department of Energy national laboratory partnership
or
a Department of Defense laboratory partnership
typically enters
through a CRADA.

**DFARS data rights.**
[The Defense Federal Acquisition Regulation Supplement][ref_dfars]
includes
data rights clauses
[DFARS 252.227-7013][ref_dfars_7013]
and
[DFARS 252.227-7014][ref_dfars_7014]
that
apply to technical data
and computer software
delivered under
Department of Defense contracts.
A research and development program
contracting with DOD
should engage
intellectual property counsel
before
the contract negotiation
to ensure that
the markings on delivered data
preserve the intended rights allocation.

**STTR-specific intellectual property allocation.**
The Small Business Technology Transfer programme
requires
the small business
and the research partner
to agree
in advance
on the allocation
of intellectual property
made under
the STTR project.
The standard allocation
gives the small business
the exclusive license
for commercialisation,
with
royalty payments
to the research partner
on commercial sales.
The
[after-the-award article
in the SBIR and STTR playbook][related_post_a141_after_award]
addresses
the STTR-specific
intellectual property issues
in depth.

The intellectual property regime
substantially affects
the program's
ability to commercialise
its work
after the federal funding ends.
A program manager
who treats
the IP arrangements
as paperwork
will discover,
years later,
that
the program's
commercialisation prospects
were forfeit
at the contract signing.

## Technology Transition from Prototype to Operational Use

A research and development program
that delivers
a working prototype
faces
the
[valley of death][ref_valley_of_death]
between
the prototype
and the operational deployment
of the technology.
The valley of death
is the structural gap
between
the federal research funding
that
produces the prototype
and the operational procurement funding
that
produces fielded systems.

**The SBIR Phase III sole-source authority.**
[The federal SBIR programme][ref_sbir_gov]
allows
a sole-source procurement authority
for Phase III work
that
extends
the technology developed
under SBIR Phase I and Phase II
into operational acquisition.
The
[Phase III and the valley of death article
in the SBIR and STTR playbook][related_post_a138_valley_of_death]
addresses
the Phase III pathway
in detail.
A search and rescue research and development program
that targets
federal agency adoption
through
the SBIR programme
should plan
the Phase III transition
from
Phase I onward,
not after Phase II ends.

**The Department of Homeland Security
Technology Transfer and Commercialization Program.**
[The DHS Technology Transfer and Commercialization Program][ref_dhs_t2c]
administers
the technology transfer
of research outputs
from federally funded research laboratories
into commercial development.
[The DHS Commercialization Accelerator Program][ref_dhs_cap]
is the currently funded vehicle
through which
search-and-rescue-relevant technology
developed under DHS S&T funding
transitions to commercial deployment.

**FAA Type Certification as a transition gate.**
A research and development program
that targets
commercial sale
of a new unmanned aircraft platform
must achieve
[Type Certification][ref_faa_type_certification]
through
[the FAA Aircraft Certification Service][ref_faa_acs]
before
the platform supports
non-experimental commercial operation.
Type Certification
for an unmanned aircraft
typically takes
five to ten years
from initial design freeze
to certification grant.
The cost
runs
several million to several hundred million dollars
depending on the platform's complexity.
Most research and development programmes
do not pursue Type Certification
directly.
A program that targets
a Type-Certified product
typically licenses or sells the technology
to an established aircraft manufacturer
that
already operates
within the certification pipeline.

**NIST Standard Test Methods as a transition gate.**
[The NIST Standard Test Methods for
Small Unmanned Aircraft Systems][ref_nist_tests]
provide
the objective performance benchmarks
that
public-safety operators
use
for procurement decisions.
A research and development program
that targets
public-safety operator adoption
should evaluate
its technology
against the NIST test methods
during development,
and
provide
the test results
in the technology's commercial documentation.

**Operator demonstrations and pilot deployments.**
A research and development program
that delivers
a working prototype
typically conducts
operator demonstrations
with
public safety agencies
before
the technology enters
operational procurement.
The
[DRONERESPONDERS UNITE programme][ref_droneresponders_unite]
admits
research-and-development organisations
into the public-safety drone evaluation network.
A program that earns
demonstrated operator endorsement
from a major public-safety agency
inherits
a sales channel
that
no amount of marketing
can replicate.

The transition phase
is the dominant programme risk
for search-and-rescue R&D
because
the federal funding
that produced the prototype
does not extend
to fielded deployment.
A program manager
who plans
the transition phase
from
the proposal stage
onward
has a chance
of successful deployment.
A program manager
who treats
the transition phase
as a post-development concern
typically
fails to deploy
the technology
within the funding window.

## Out of Scope

This article
restricts itself
to the research and development
landscape
for search-and-rescue-relevant
unmanned aerial vehicle programmes
in the United States
in 2026.
Several substantive topics
are deliberately deferred
to follow-up work.

**Detailed engineering of custom platforms.**
The aerodynamic design,
the structural analysis,
the autopilot tuning,
the sensor selection,
and the integration procedures
for a custom unmanned aerial vehicle
are
the subject of
[the fifteen-article fixed-wing UAV engineering series][related_post_a112_prototyping]
that
this blog has published
across A112 through A131.
A research and development program
designing
a custom platform
should
draw on that series
for the engineering content.

**International R&D landscape.**
The research and development landscape
in Europe
under EASA,
in Canada
under Transport Canada,
in the United Kingdom
under the Civil Aviation Authority,
and in
other jurisdictions
differs from
the United States landscape
in
funding sources,
regulatory pathways,
and intellectual property regimes.
This article addresses
the United States only.

**Counter-unmanned aerial systems research.**
A separate research and development domain
addresses
the detection and neutralisation
of unauthorised unmanned aerial systems.
The counter-UAS domain
overlaps with
search-and-rescue operations
where
unauthorised drones
interfere with
ongoing rescue operations,
but
this article
addresses
the friendly-UAV development side only.

**Manned aircraft integration in detail.**
A research and development program
addressing
the integration
of unmanned and manned aircraft
in coordinated search-and-rescue operations
encounters
substantial regulatory and operational complexity
that this article does not address.

**Commercial-only development outside federal funding.**
A research and development program
funded entirely
through commercial sources,
venture capital,
or
the small business's own working capital
operates
outside
the federal intellectual property regime
that
the bulk of this article addresses.
The program manager
should consult
intellectual property counsel
on the contractual arrangements
that
non-federal funding
typically requires.

## Conclusion

A search and rescue research and development program
in 2026
faces
three sequential decisions.
The first decision
is
whether to build, modify, or buy.
The buyer's framework
that A146 addressed
covers
the third option.
The first and second options
require
the engineering capacity
and the funding model
that
this article addresses.

The second decision
is
which combination
of federal funding sources,
university partnerships,
and federal laboratory partnerships
sustains
the research and development cycle.
The federal funding portfolio
includes
SBIR and STTR,
DHS Science and Technology,
NIST Public Safety Communications Research,
NASA Aeronautics,
NSF Cyber-Physical Systems,
and the
Department of Energy national laboratories.
The partnership portfolio
includes
the seven FAA UAS Test Sites,
the FAA Centres of Excellence,
the federally funded research and development centres,
and
the leading university unmanned aerial vehicle research programmes.

The third decision
is
how the program transitions
the prototype
into operational use.
The transition
crosses
the valley of death
between
research funding
and procurement funding.
The SBIR Phase III sole-source authority,
the DHS Transition to Practice programme,
the FAA Type Certification pathway,
and the
NIST Standard Test Methods as a transition gate
each
admit
the program
to operational deployment
under
conditions
that
the program must design for
from the proposal stage.

The research and development audience
is smaller
than the buyer audience
that A146 addressed.
A program that operates
in this space
takes on
substantial regulatory,
intellectual property,
and technology-transition complexity
in exchange for
the capability
to develop systems
that
the commercial market
does not provide.
The program manager
who treats
this complexity as a feature
of the work
rather than as a tax on it
is well positioned
to succeed.

## References

- [Reference, ArduPilot Open Source Autopilot][ref_ardupilot]
- [Reference, ArduPilot ROS 2 Bridge][ref_ardupilot_ros2]
- [Reference, ArduPilot Software in the Loop][ref_ardupilot_sitl]
- [Reference, Bayh-Dole Act of 1980][ref_bayh_dole]
- [Reference, Cooperative Research and Development Agreements][ref_crada]
- [Reference, Defense Advanced Research Projects Agency][ref_darpa]
- [Reference, Defense Contract Management Agency Blue UAS Cleared List][ref_blue_uas_list]
- [Reference, Defense Federal Acquisition Regulation Supplement][ref_dfars]
- [Reference, Defense Federal Acquisition Regulation Supplement SBIR Data Rights Final Rule 2025][ref_dfars_sbir_2025]
- [Reference, Defense Innovation Unit Blue UAS Framework Legacy][ref_diu_legacy_blue_uas]
- [Reference, Department of Defense Small Business Innovation Research Portal][ref_dod_sbir]
- [Reference, Department of Energy National Laboratories][ref_doe_labs]
- [Reference, Department of Homeland Security First Responder Capability Group][ref_dhs_first_responders]
- [Reference, Department of Homeland Security Long Range Broad Agency Announcement][ref_dhs_st_lrbaa]
- [Reference, Department of Homeland Security Science and Technology Directorate][ref_dhs_st]
- [Reference, Department of Homeland Security Small Business Innovation Research Programme][ref_dhs_sbir]
- [Reference, Department of Homeland Security Commercialization Accelerator Program][ref_dhs_cap]
- [Reference, Department of Homeland Security Technology Transfer and Commercialization Program][ref_dhs_t2c]
- [Reference, DFARS 252.227-7013][ref_dfars_7013]
- [Reference, DFARS 252.227-7014][ref_dfars_7014]
- [Reference, DJI Mobile SDK][ref_dji_mobile_sdk]
- [Reference, DJI Onboard SDK][ref_dji_onboard_sdk]
- [Reference, DJI Payload SDK][ref_dji_payload_sdk]
- [Reference, Doodle Labs Mesh Rider][ref_doodle_labs]
- [Reference, DRONERESPONDERS UNITE Programme][ref_droneresponders_unite]
- [Reference, Federal Acquisition Regulation Provision 52.240-1][ref_far_52_240_1]
- [Reference, Federal Aviation Administration Aircraft Certification Service][ref_faa_acs]
- [Reference, Federal Aviation Administration Centres of Excellence for UAS][ref_faa_coe_uas]
- [Reference, Federal Aviation Administration Certificate of Waiver or Authorization][ref_faa_coa]
- [Reference, Federal Aviation Administration Part 107 Small Unmanned Aircraft Rule][ref_faa_part_107]
- [Reference, Federal Aviation Administration Special Airworthiness Certification][ref_faa_special_airworthiness]
- [Reference, Federal Aviation Administration Type Certification][ref_faa_type_certification]
- [Reference, Federal Aviation Administration UAS Test Sites][ref_faa_uas_test_sites]
- [Reference, FLIR Boson Plus Thermal Camera][ref_flir_boson_plus]
- [Reference, Gazebo Robotics Simulator][ref_gazebo]
- [Reference, Holybro Autopilot Hardware][ref_holybro]
- [Reference, IAMAI Simulations AirSim Successor][ref_iamai]
- [Reference, Johns Hopkins Applied Physics Laboratory][ref_jhuapl]
- [Reference, LightWare LiDAR Series][ref_lightware_lidar]
- [Reference, MathWorks UAV Toolbox][ref_matlab_uav_toolbox]
- [Reference, MAVLink Protocol][ref_mavlink]
- [Reference, Mid-Atlantic Aviation Partnership UAS Test Site][ref_maap]
- [Reference, MIT Lincoln Laboratory][ref_mit_lincoln_lab]
- [Reference, MIT Lincoln Laboratory Search-and-Rescue Optical Technology][ref_mit_ll_sar]
- [Reference, mRo Robotics Autopilot Hardware][ref_mro_robotics]
- [Reference, NASA UAS in the National Airspace System Project][ref_nasa_uas_nas]
- [Reference, National Institute of Standards and Technology Public Safety Communications Research Division][ref_nist_pscr]
- [Reference, National Institute of Standards and Technology Standard Test Methods for Small UAS][ref_nist_tests]
- [Reference, National Robotics Engineering Centre][ref_nrec]
- [Reference, National Science Foundation Cyber-Physical Systems Programme][ref_nsf_cps]
- [Reference, National Science Foundation Smart and Connected Communities Programme][ref_nsf_scc]
- [Reference, Naval Postgraduate School Consortium for Robotics and Unmanned Systems Education and Research][ref_nps_cruser]
- [Reference, Nevada Autonomous Programme at the University of Nevada Reno][ref_nias]
- [Reference, New York UAS Test Site at Griffiss International Airport][ref_griffiss]
- [Reference, Northern Plains UAS Test Site North Dakota][ref_northern_plains]
- [Reference, NVIDIA Isaac Sim][ref_nvidia_isaac_sim]
- [Reference, NVIDIA Jetson][ref_nvidia_jetson]
- [Reference, Microsoft AirSim Archive Notice][ref_airsim_archived]
- [Reference, Microsoft AirSim][ref_airsim]
- [Reference, Microsoft Project AirSim Discontinuation Notice][ref_project_airsim_discontinued]
- [Reference, Open Robotics][ref_open_robotics]
- [Reference, Part 108 Beyond Visual Line of Sight Rule][ref_part_108]
- [Reference, Ouster LiDAR Sensors][ref_ouster]
- [Reference, Parrot Air SDK][ref_parrot_air_sdk]
- [Reference, Parrot ANAFI Ai Open Flight Control][ref_parrot_open_flight_control]
- [Reference, Parrot Olympe SDK][ref_parrot_olympe]
- [Reference, Pixhawk Autopilot Hardware][ref_pixhawk]
- [Reference, PSCR Open Innovation Programme][ref_pscr_open_innovation]
- [Reference, PX4 Autopilot][ref_px4]
- [Reference, PX4 Hardware in the Loop Simulation][ref_px4_hitl]
- [Reference, PX4 ROS 2 Bridge][ref_px4_ros2]
- [Reference, PX4 Software in the Loop Simulation][ref_px4_sitl]
- [Reference, Raspberry Pi][ref_raspberry_pi]
- [Reference, Raspet Flight Research Laboratory at Mississippi State University][ref_raspet]
- [Reference, Robot Operating System Version 2][ref_ros_2]
- [Reference, Sandia National Laboratories Unmanned Aerial Vehicle Research][ref_sandia_uas]
- [Reference, Section 44807 of Title 49 United States Code][ref_section_44807]
- [Reference, Sierra Olympia Vinden][ref_sierra_olympia_vinden]
- [Reference, Silvus Technologies StreamCaster][ref_silvus_streamcaster]
- [Reference, Skydio Connect Ecosystem][ref_skydio_connect]
- [Reference, Small Business Innovation Research and Small Business Technology Transfer Portal][ref_sbir_gov]
- [Reference, Small Business Innovation Research Data Rights Regime][ref_sbir_data_rights]
- [Reference, Stevenson-Wydler Technology Innovation Act][ref_stevenson_wydler]
- [Reference, Subterranean Challenge of DARPA][ref_darpa_subt]
- [Reference, Swarm Programme OFFSET of DARPA][ref_darpa_offset]
- [Reference, Teledyne FLIR Aerial Thermal Imaging][ref_teledyne_flir]
- [Reference, Texas A&M Lone Star UAS Centre of Excellence and Innovation][ref_texas_am_lone_star]
- [Reference, uORB Middleware in PX4][ref_uorb]
- [Reference, University of Alaska Fairbanks Alaska Center for UAS Integration][ref_acuasi]
- [Reference, University of Maryland Research and Operations Center][ref_umd_uroc]
- [Reference, Valley of Death in Technology Commercialization][ref_valley_of_death]
- [Reference, Workswell WIRIS Thermal Series][ref_workswell_wiris]
- [Related Post, A Buyer's Decision Framework for Search and Rescue Drones][related_post_a146_buying]
- [Related Post, A Worked SBIR and STTR Campaign for a Fixed-Wing UAV][related_post_a144_sbir_capstone]
- [Related Post, After the Award, Compliance and Reporting for SBIR and STTR][related_post_a141_after_award]
- [Related Post, Data Rights and Intellectual Property for SBIR and STTR][related_post_a139_data_rights]
- [Related Post, Fixed-Wing Multicopter and Hybrid Drones for Search and Rescue Physics and Economics][related_post_a145_physics]
- [Related Post, An Introduction to the SBIR and STTR Programs][related_post_a132_sbir_intro]
- [Related Post, Phase III and the Valley of Death for SBIR and STTR][related_post_a138_valley_of_death]
- [Related Post, Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass][related_post_a112_prototyping]
- [Related Post, Strategy and the Portfolio of SBIR and STTR Awards][related_post_a142_strategy]

[ref_acuasi]: https://acuasi.alaska.edu/
[ref_airsim]: https://microsoft.github.io/AirSim/
[ref_airsim_archived]: https://github.com/microsoft/AirSim
[ref_ardupilot]: https://ardupilot.org/
[ref_ardupilot_ros2]: https://ardupilot.org/dev/docs/ros2.html
[ref_ardupilot_sitl]: https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html
[ref_bayh_dole]: https://www.law.cornell.edu/uscode/text/35/part-II/chapter-18
[ref_blue_uas_list]: https://bluelist.dcma.mil/
[ref_crada]: https://www.energy.gov/technologytransitions/cooperative-research-and-development-agreements-cradas
[ref_darpa]: https://www.darpa.mil/
[ref_darpa_offset]: https://www.darpa.mil/program/offensive-swarm-enabled-tactics
[ref_darpa_subt]: https://www.darpa.mil/program/darpa-subterranean-challenge
[ref_dfars]: https://www.acquisition.gov/dfars
[ref_dfars_7013]: https://www.acquisition.gov/dfars/252.227-7013-rights-technical-data-noncommercial-items.
[ref_dfars_7014]: https://www.acquisition.gov/dfars/252.227-7014-rights-noncommercial-computer-software-and-noncommercial-computer-software-documentation.
[ref_dfars_sbir_2025]: https://www.federalregister.gov/documents/2020/08/31/2020-18641/defense-federal-acquisition-regulation-supplement-small-business-innovation-research-program-data
[ref_dhs_cap]: https://www.dhs.gov/science-and-technology/cap
[ref_dhs_first_responders]: https://www.dhs.gov/science-and-technology/first-responder-capability-group
[ref_dhs_sbir]: https://www.dhs.gov/science-and-technology/sbir
[ref_dhs_st]: https://www.dhs.gov/science-and-technology
[ref_dhs_st_lrbaa]: https://www.dhs.gov/science-and-technology/lrbaa
[ref_dhs_t2c]: https://www.dhs.gov/science-and-technology/technology-transfer-program
[ref_diu_legacy_blue_uas]: https://www.diu.mil/blue-uas-portal
[ref_dji_mobile_sdk]: https://developer.dji.com/mobile-sdk/
[ref_dji_onboard_sdk]: https://developer.dji.com/onboard-sdk/
[ref_dji_payload_sdk]: https://developer.dji.com/payload-sdk/
[ref_dod_sbir]: https://www.defensesbirsttr.mil/
[ref_doe_labs]: https://www.energy.gov/national-laboratories
[ref_doodle_labs]: https://doodlelabs.com/products/mesh-rider/
[ref_droneresponders_unite]: https://www.droneresponders.org/unite
[ref_faa_acs]: https://www.faa.gov/aircraft/air_cert
[ref_faa_coa]: https://www.faa.gov/uas/advanced_operations/certification
[ref_faa_coe_uas]: https://www.faa.gov/about/office_org/headquarters_offices/ang/grants/coe_uas
[ref_faa_part_107]: https://www.ecfr.gov/current/title-14/chapter-I/subchapter-F/part-107
[ref_faa_special_airworthiness]: https://www.faa.gov/aircraft/air_cert/airworthiness_certification/sp_awcert
[ref_faa_type_certification]: https://www.faa.gov/aircraft/air_cert/design_approvals/tc
[ref_faa_uas_test_sites]: https://www.faa.gov/uas/research_development/test_sites
[ref_far_52_240_1]: https://www.acquisition.gov/far/52.240-1
[ref_flir_boson_plus]: https://www.flir.com/products/boson-plus/
[ref_gazebo]: https://gazebosim.org/
[ref_griffiss]: https://nyuasts.com/
[ref_holybro]: https://holybro.com/
[ref_iamai]: https://iamaisims.com/
[ref_jhuapl]: https://www.jhuapl.edu/
[ref_lightware_lidar]: https://lightwarelidar.com/
[ref_maap]: https://www.maap.ictas.vt.edu/
[ref_matlab_uav_toolbox]: https://www.mathworks.com/products/uav.html
[ref_mavlink]: https://mavlink.io/
[ref_mit_lincoln_lab]: https://www.ll.mit.edu/
[ref_mit_ll_sar]: https://www.ll.mit.edu/r-d/projects
[ref_mro_robotics]: https://store.mrobotics.io/
[ref_nasa_uas_nas]: https://www.nasa.gov/aeroresearch/programs/iasp/uas/
[ref_nias]: https://www.unr.edu/ncar/programs/nevada-autonomous
[ref_nist_pscr]: https://www.nist.gov/ctl/pscr
[ref_nist_tests]: https://www.nist.gov/el/intelligent-systems-division-73500/standard-test-methods-response-robots/aerial-drone-tests-0
[ref_northern_plains]: https://www.npuasts.com/
[ref_nps_cruser]: https://nps.edu/web/cruser
[ref_nrec]: https://www.cmu.edu/nrec/
[ref_nsf_cps]: https://www.nsf.gov/funding/opportunities/cps-cyber-physical-systems
[ref_nsf_scc]: https://www.nsf.gov/funding/opportunities/scc-smart-connected-communities
[ref_nvidia_isaac_sim]: https://developer.nvidia.com/isaac/sim
[ref_nvidia_jetson]: https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/
[ref_open_robotics]: https://www.openrobotics.org/
[ref_ouster]: https://ouster.com/
[ref_parrot_air_sdk]: https://developer.parrot.com/docs/airsdk/
[ref_parrot_olympe]: https://developer.parrot.com/docs/olympe/
[ref_parrot_open_flight_control]: https://developer.parrot.com/
[ref_part_108]: https://www.federalregister.gov/documents/2025/08/07/2025-14837/normalizing-unmanned-aircraft-systems-beyond-visual-line-of-sight-operations
[ref_pixhawk]: https://docs.px4.io/main/en/flight_controller/pixhawk_series.html
[ref_project_airsim_discontinued]: https://github.com/microsoft/AirSim
[ref_pscr_open_innovation]: https://www.nist.gov/ctl/pscr/open-innovation-prize-challenges
[ref_px4]: https://px4.io/
[ref_px4_hitl]: https://docs.px4.io/main/en/simulation/hitl.html
[ref_px4_ros2]: https://docs.px4.io/main/en/ros2/
[ref_px4_sitl]: https://docs.px4.io/main/en/simulation/
[ref_raspberry_pi]: https://www.raspberrypi.com/
[ref_raspet]: https://raspet.msstate.edu/
[ref_ros_2]: https://docs.ros.org/en/rolling/index.html
[ref_sandia_uas]: https://www.sandia.gov/research/research_foundations/computing-and-information-sciences/index.html
[ref_sbir_data_rights]: https://www.sbir.gov/data-rights-protections
[ref_sbir_gov]: https://www.sbir.gov/
[ref_section_44807]: https://www.law.cornell.edu/uscode/text/49/44807
[ref_sierra_olympia_vinden]: https://sierraolympia.com/
[ref_silvus_streamcaster]: https://silvustechnologies.com/products/streamcaster-radios/
[ref_skydio_connect]: https://www.skydio.com/products/skydio-connect
[ref_stevenson_wydler]: https://www.law.cornell.edu/uscode/text/15/chapter-63
[ref_teledyne_flir]: https://www.flir.com/instruments/aerial/
[ref_texas_am_lone_star]: https://lsuasc.tamucc.edu/
[ref_umd_uroc]: https://uroc.umd.edu/
[ref_uorb]: https://docs.px4.io/main/en/middleware/uorb.html
[ref_valley_of_death]: https://en.wikipedia.org/wiki/Valley_of_death_(business)
[ref_workswell_wiris]: https://workswell-thermal-camera.com/
[related_post_a112_prototyping]: {% post_url 2026-05-30-prototyping_fixed_wing_aircraft_with_lightweight_pla_and_fiberglass %}
[related_post_a132_sbir_intro]: {% post_url 2026-06-15-introduction_to_the_sbir_and_sttr_programs %}
[related_post_a138_valley_of_death]: {% post_url 2026-06-21-phase_iii_and_the_valley_of_death_for_sbir_and_sttr %}
[related_post_a139_data_rights]: {% post_url 2026-06-22-data_rights_and_intellectual_property_for_sbir_and_sttr %}
[related_post_a141_after_award]: {% post_url 2026-06-24-after_the_award_for_sbir_and_sttr %}
[related_post_a142_strategy]: {% post_url 2026-06-25-strategy_and_the_portfolio_of_sbir_and_sttr_awards %}
[related_post_a144_sbir_capstone]: {% post_url 2026-06-27-worked_sbir_and_sttr_campaign_for_a_fixed_wing_uav %}
[related_post_a145_physics]: {% post_url 2026-05-15-fixed_wing_multicopter_and_hybrid_drones_for_search_and_rescue %}
[related_post_a146_buying]: {% post_url 2026-05-16-buyers_decision_framework_for_search_and_rescue_drones %}
