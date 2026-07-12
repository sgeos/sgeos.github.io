---
layout: post
mathjax: false
comments: true
title:  "Search and Rescue Drone Fleets by Geographic Setting"
date:   2026-05-18 09:00:00 +0000
categories: aerospace engineering uav search-and-rescue geographic-setting
series: search_and_rescue_drones
series_title: Search and Rescue Drones
series_index: 4
---
<!-- A148 -->
<script>console.log("A148");</script>

[The first article in this series][related_post_a145_physics]
analysed
the physics and economics
of fixed-wing, multicopter,
and hybrid vertical-takeoff-and-landing
drones
for search and rescue.
[The second article][related_post_a146_buying]
gave
the buyer's decision framework.
[The third article][related_post_a147_rd]
covered
the research and development side.
The three articles
sized the platforms,
filtered the platforms by mission profile,
and addressed
the development of new platforms.
None of the three
addressed the question
of how
the geographic setting
in which the program operates
shapes
the fleet selection.
That is the fourth question,
and this article answers it.

A search and rescue program
in a dense urban centre,
a suburban county,
a rural agricultural region,
and a frontier wilderness
each
needs
a different fleet.
The mission profile
may be nominally the same
across these settings,
namely
finding a missing person,
but
the airspace,
the regulatory posture,
the funding sources,
the crew complement,
the operational tempo,
and the platform mix
that supports the mission
differ
in ways
that
the mission-profile-only analysis of A146
cannot capture.
A program manager
in a specific jurisdiction
benefits from
an explicit
geographic-setting filter
that runs alongside
the mission-profile filter.

This article
introduces a four-level scheme
mapped to existing federal classification systems,
walks through
the platform mix
appropriate to each level,
addresses
the parallel-operations question
that the prior articles
treated only implicitly,
and closes
with the airspace, regulatory, funding,
and crew considerations
that distinguish
each level.

## Why Setting Matters Beyond Mission Profile

The mission profile
in A146
filtered
on what the program does:
wilderness search,
urban search,
water rescue,
alpine rescue,
or disaster response.
The geographic setting
filters
on where the program does it.
The two filters
are independent.
A small-town fire department
doing urban search
in a rural setting
needs
a different fleet
from
a metropolitan fire department
doing urban search
in a dense city,
even though
both operations
are
"urban search"
by mission profile.

Six structural axes
distinguish
geographic settings
in ways that the platform selection
must respond to.

**Airspace classification.**
[Federal Aviation Administration
Class B controlled airspace][ref_class_b]
surrounds
major metropolitan centres.
[Class C][ref_class_c] surrounds
large secondary metros.
[Class D][ref_class_d] surrounds
airports with operating control towers.
[Class G][ref_class_g] uncontrolled airspace
covers
most rural and frontier areas.
A program operating in
Class B, C, or D
must obtain airspace authorisation
through
the
[Low Altitude Authorization
and Notification Capability][ref_laanc]
programme
or through a specific Certificate of Waiver or Authorization
for each operation.
A program operating in
Class G
proceeds
without prior authorisation.
The platform mix
that operates safely and routinely
in controlled airspace
differs from
the platform mix
that takes advantage
of uncontrolled airspace.

**Operations over people.**
Part 107
[Subpart D][ref_part_107_subpart_d]
restricts
operations
of small unmanned aircraft
over human beings.
The
[Operations Over People final rule of 2021][ref_oop_final_rule]
established
four categories
that admit
operations
over people
under specified conditions.
Category 2 and 3 operations
require
a platform that meets
the
[ASTM F3322 parachute standard][ref_astm_f3322].
The urban-tier program
faces
the operations-over-people question
on every flight.
The frontier-tier program
faces it almost never.
The platform mix
that admits
routine urban operation
must include
parachute-equipped platforms
or platforms
that pass the operations-over-people
categories
by another path.

**Beyond visual line of sight.**
A rural search
across thirty square kilometres
needs
beyond visual line of sight operation.
An urban search
across two square kilometres
does not.
The BVLOS requirement
pulls
the rural and frontier programs
toward
[Section 44807 exemptions][ref_section_44807],
the
[Centres of Excellence for Unmanned Aircraft Systems][ref_faa_coe_uas]
pathway,
or the eventual
[Part 108 final rule][ref_part_108]
once it lands.
None of which
an urban program needs.

**Range and communications.**
Rural and frontier search areas
exceed
the operating range
of consumer data links.
The program
may need
mesh radios
such as
[Doodle Labs Mesh Rider][ref_doodle_labs]
or
[Silvus Technologies StreamCaster][ref_silvus_streamcaster],
or satellite backhaul
through
[Iridium Certus][ref_iridium_certus]
or
[Starlink][ref_starlink]
for the ground station.
The urban program
operates within
the consumer data link range
and does not face
this question.

**Crew complement.**
Urban programs
have access to
full multi-person crews.
Rural programs
often operate with
a single remote pilot in command,
which restricts
the airframe class
that the operation admits.
Frontier programs
deploy teams
that
must
be self-contained
because
no organisation
is nearby to support them.

**Funding landscape.**
The
[Urban Areas Security Initiative][ref_uasi]
funds
designated urban programs.
The
[State Homeland Security Programme][ref_shsp]
funds
the broader state portfolio
including rural programs.
The
[Tribal Homeland Security Grant Program][ref_thsgp]
serves
tribal lands.
Federal frontier-operating agencies
including
[the National Park Service][ref_nps_uas],
[the Bureau of Land Management][ref_blm_uas],
[the United States Forest Service][ref_usfs_uas],
[the United States Coast Guard][ref_uscg_uas],
and
[the United States Fish and Wildlife Service][ref_usfws_uas]
operate
their own UAS programmes
with budgets and constraints
distinct from
state and local programmes.

These six axes
combine
to produce
a platform mix decision
that the mission-profile filter alone
does not yield.
A program manager
running A146's three-branch decision tree
and arriving at
"Tier 3, medium professional"
still has
a fleet-composition question
that the geographic setting answers.

## The Federal Geographic Classifications

The United States federal government
operates
several geographic classification systems
that
the SAR program manager
can use
to identify
the program's operating setting
objectively.

**Rural-Urban Continuum Codes.**
[The US Department of Agriculture
Economic Research Service
Rural-Urban Continuum Codes][ref_rucc]
classify
each US county
into one of nine categories
based on
metropolitan area adjacency
and population.
Category 1 covers
the most-populous metropolitan counties.
Category 9 covers
the smallest non-metropolitan rural counties.
The codes are revised
following each decennial census.

**Rural-Urban Commuting Area Codes.**
[The Rural-Urban Commuting Area Codes][ref_ruca]
classify
each US census tract
into one of ten primary codes
based on
commuting patterns
and population density.
The RUCA codes
operate at finer geographic resolution
than the RUCC codes
because the census tract
is smaller than the county,
and they capture
commuting links
between
urban centres and the surrounding rural population.

**Centers for Disease Control and Prevention
National Center for Health Statistics
Urban-Rural Classification.**
[The CDC NCHS Urban-Rural Classification][ref_cdc_nchs]
classifies
each US county
into one of six categories
oriented around
public health data analysis.
The classification
is used
across federal public-health programmes
and provides
a population-density
basis for comparison
across counties.

**Frontier and Remote Area Codes.**
[The USDA Economic Research Service
Frontier and Remote Area Codes][ref_far]
classify
each US ZIP code
into one of four levels
based on
the population density and
the distance
from the nearest urban centre.
Level 1 covers
the least frontier ZIP codes,
namely those within a short drive of a small urban area.
Level 4 covers
the most frontier ZIP codes,
namely those a long distance from any urban area.
The FAR codes
operate at the ZIP code level
which is finer than the county
and which captures
the frontier-and-remote dimension
that the other classifications underweight.

The four classifications
overlap substantially
and offer different resolutions
of the same underlying urban-rural reality.
A program manager
selecting a classification
for fleet-planning purposes
can use
any of them.
This article
uses
a simplified four-level scheme
that maps
to combinations of RUCC, RUCA,
and FAR
because
four levels
matches
the four-fold operational distinction
the SAR drone fleet decision
requires.

## The Four Operational Levels

The four operational levels
this article uses
combine
the federal classifications
into a fleet-planning shorthand.
Each level
covers
a range of underlying classifications.

| Level | Description | RUCC range | CDC NCHS range | FAR range |
|---|---|---|---|---|
| Level 1 | Densely Urban | 1 to 3 | 1 to 2 | 0 |
| Level 2 | Suburban or Small Urban | 4 to 5 | 3 to 4 | 0 |
| Level 3 | Rural | 6 to 7 | 5 to 6 | 1 to 2 |
| Level 4 | Frontier and Remote | 8 to 9 | not applicable | 3 to 4 |

A program manager
identifying
the operating level
should not
treat the mapping
as a strict membership rule.
A county
straddling
two levels
should
plan
for the higher operational tempo
of the more demanding level.

### Level 1, Densely Urban

A Level 1 program
serves
a major metropolitan area
with substantial population density,
substantial controlled airspace,
substantial built environment,
and substantial federal funding
through
the Urban Areas Security Initiative
where the metro qualifies.
Examples include
the New York City fire department,
the Los Angeles County sheriff,
the Chicago police marine unit,
the Houston police air support,
and the Miami-Dade fire department.

**Mission profile dominance.**
Urban search dominates,
namely
building searches,
vehicle accidents in dense traffic,
missing persons in densely populated parks,
distressed persons in waterways,
and structural collapse after incidents.
Wilderness search and water rescue
appear in metropolitan parks
and along urban shorelines
but cover small geographic footprints.

**Platform mix.**
Multicopters dominate
the Level 1 fleet.
Fixed-wing platforms
are rarely justified
because
the area coverage rate
of a fixed-wing aircraft
exceeds
the search-area-size
of typical urban operations.
Hybrid vertical-takeoff-and-landing platforms
serve
the edge cases
where
a metropolitan park
or coastal stretch
exceeds
the multicopter endurance
but the launch site
admits no fixed-wing operation.

A typical Level 1 fleet
includes
three to ten
heavy multicopters
with thermal and electro-optical payloads
for primary operations,
five to fifteen
lighter multicopters
for forward operators
and surge capacity,
and optionally
one or two
hybrid platforms
for the rare large-area incident.

**Airspace constraint.**
Class B and C airspace
covers most of the operating area.
LAANC authorisation
is the routine path.
A program operating in Class B
should automate
the LAANC request workflow
because the volume of operations
exceeds
what manual authorisation can sustain.

**Operations over people.**
Routine.
A Level 1 program
flies over people
on most operations.
The platforms
must
either
include parachute recovery systems
under
[Operations Over People Category 2 or Category 3][ref_oop_categories]
that pass
the ASTM F3322 standard,
or
operate under
specific approvals
for closed sets
of operations.

### Level 2, Suburban or Small Urban

A Level 2 program
serves
a mid-size city
or
the suburban counties
around a major metropolitan area.
Examples include
Wake County in North Carolina,
Lubbock County in Texas,
Arapahoe County in Colorado,
Anne Arundel County in Maryland,
and analogous suburban-county jurisdictions.

**Mission profile dominance.**
Mixed urban and outdoor.
The program serves
both
the built environment
of small downtown cores
and the surrounding
agricultural, wooded, or coastal terrain.
The geographic balance
shifts
with the specific county.
A coastal Level 2 county
emphasises water rescue
more than an inland Level 2 county.

**Platform mix.**
A balanced
multicopter-and-hybrid fleet
covers
most Level 2 operations.
Multicopters
handle
the built-environment operations
and the close-target investigation.
Hybrid platforms
handle
the moderate-area searches
of suburban parks
and the coastal stretches.
Fixed-wing platforms
are justifiable
for large rural sectors
within the county
but are not essential.

A typical Level 2 fleet
includes
two to five
heavy multicopters,
three to eight
lighter multicopters,
and one or two
hybrid platforms.
Tier 3 budget
from A146
covers
this configuration.

**Airspace constraint.**
Mixed Class C, D, and G airspace.
LAANC is needed
for the controlled segments
but not for the rural segments
of the county.

**Operations over people.**
Routine in the built segments,
rare in the rural segments.
A Level 2 program
typically operates
a mix of
parachute-equipped
and non-parachute-equipped
platforms,
with the
parachute-equipped platforms
designated
for the urban-segment operations.

### Level 3, Rural

A Level 3 program
serves
a rural county
with small towns,
agricultural land,
and undeveloped terrain.
Examples include
many county sheriff's offices
across the central and western United States,
state-level search and rescue organisations
in less-populated states,
and volunteer programmes
operating across
multi-county areas.

**Mission profile dominance.**
Wilderness search,
water rescue,
agricultural land searches,
and lost-person searches
in unimproved terrain.
Urban search
is limited to
small towns
within the county.

**Platform mix.**
The fixed-wing or hybrid platform
becomes
operationally essential
because
the typical search area
ranges from
twenty to several hundred square kilometres,
which exceeds
the multicopter capability
in any reasonable time budget.
The multicopter
serves
target investigation
and intervention.

A typical Level 3 fleet
includes
one fixed-wing or hybrid platform
with appropriate launch and recovery infrastructure,
two to four
heavy multicopters
with thermal payloads,
and three to six
lighter multicopters
for forward operators.

**Airspace constraint.**
Predominantly Class G uncontrolled airspace.
LAANC is not needed
for routine operations.
A program operating
near small-airport Class D airspace
needs LAANC for the relevant operations only.

**Operations over people.**
Less routine than Level 2,
but still
required
for small-town flyovers
and roadside accidents.
A Level 3 program
typically operates
one or two
parachute-equipped platforms
alongside
non-parachute-equipped platforms
for the rural majority of operations.

### Level 4, Frontier and Remote

A Level 4 program
serves
a sparsely populated area
with vast distances,
challenging terrain,
limited communications infrastructure,
and often
federal land ownership.
Examples include
the National Park Service
incident response teams,
the Coast Guard
Pacific Northwest and Alaska districts,
state-level search and rescue
in Alaska, Montana, Wyoming, and similar low-population-density states,
and tribal lands
operating under
the Tribal Homeland Security Grant Program.

**Mission profile dominance.**
Wilderness search
over very large areas,
water rescue
over open ocean and large lakes,
alpine and desert rescue,
multi-day deployments,
and operations
in coordination with
manned aircraft
and ground teams
from federal agencies.

**Platform mix.**
Fixed-wing platforms
with long endurance
are essential.
The mission area
exceeds
what hybrid platforms
can cover in a sortie.
Multi-day deployments
exceed
what battery-powered platforms can sustain
without resupply,
so
the fixed-wing platform
typically uses
heavy fuel
or
hybrid-electric propulsion.
Multicopters
serve
the close-target operations
once the fixed-wing
identifies a candidate.

A typical Level 4 fleet
includes
one or two
long-endurance fixed-wing platforms
in the AeroVironment Puma 3 AE,
[Edge Autonomy Penguin C Mk2][ref_penguin_c],
or Insitu ScanEagle class,
two to four
heavy multicopters,
and four to eight
lighter multicopters
for forward operator support
across the deployed teams.
Tier 4 budget
from A146
covers
this configuration.

**Airspace constraint.**
Class G dominates,
but
the operating range
often
exceeds visual line of sight.
The program
needs
Section 44807 exemptions
or operates under
the Centres of Excellence
beyond visual line of sight
authorisations.

**Operations over people.**
Rare,
because
people are sparse.
The platform mix
does not need
parachute recovery
as a routine requirement,
though some
platforms may include it
for the rare urban transit
during deployment movement.

**Communications.**
The operating range
exceeds
consumer data link capability.
Mesh radios
through Doodle Labs
or Silvus Technologies,
plus satellite backhaul
through Iridium Certus
or
Starlink ground stations,
are
operationally essential.

## Parallel Operations Patterns

The earlier articles in this series
addressed
the single-aircraft case.
A148's geographic-setting analysis
makes
the multi-aircraft case
explicit
because
the platform mix
in any of the four levels
typically operates
more than one aircraft
during an incident.
Five parallel-operations patterns
recur
across the levels.

**Single-aircraft serial operations.**
One aircraft up at a time.
The default
for very small programs
and for incidents
that
do not require simultaneous coverage.
Common in
the Tier 0 and Tier 1 budgets
that A146 described,
across all four levels.

**Single-class parallel operations.**
Two or more aircraft of the same class
covering
different sectors
of a search area
simultaneously.
Common in
Level 1 and Level 2 multicopter operations
where
the city or county
is divided into search sectors
that
each receive
a dedicated aircraft.
The platforms
share
the ground control station's
multi-aircraft management capability,
typically through
[DJI FlightHub 2][ref_dji_flighthub],
[Dronesense][ref_dronesense],
[Aloft Air Control][ref_aloft_air_control],
or
[Skydio Dock][ref_skydio_dock]
for the persistent-operations model.

**Cross-class parallel operations.**
A fixed-wing or hybrid
in the wide-area search phase
while a multicopter
handles
target investigation
on candidates the fixed-wing identifies.
The default in
Level 3 and Level 4 operations.
The two aircraft
operate
under separate ground control stations
with a
coordinator-position role
that
handles
the handoff
from the wide-area asset
to the close-target asset.
The cross-class parallel pattern
exploits
the complementary strengths
that
A145's physics analysis
identified.

**Multi-aircraft swarms.**
Three or more aircraft
under coordinated mission planning,
typically through
custom-developed or research-grade software.
The
[DARPA OFFSET swarm tactics programme][ref_darpa_offset_legacy]
demonstrated
several hundred aircraft
operating cooperatively
on infantry-support missions
that
adapt loosely
to public-safety scenarios.
Most search and rescue programs
do not operate
swarms in 2026,
but
a handful of large federal programs
including the
[Department of Energy ARM Aerial Facility][ref_doe_arm]
and several university research efforts
are
adapting swarm techniques
to civilian missions.
A program considering
swarm operations
should treat the option
as research and development work
under
[A147's framework][related_post_a147_rd]
rather than
as off-the-shelf procurement.

**Manned-unmanned teaming.**
A drone team
operating in coordination with
a manned aircraft,
typically a helicopter or fixed-wing patrol.
Common in
Level 4 federal frontier operations.
The
[Coast Guard][ref_uscg_uas]
operates
multicopters and small fixed-wing aircraft
from the cutters
that carry
manned helicopters.
The
[National Park Service][ref_nps_uas]
operates
multicopters
in coordination with
the rotor wing assets
of cooperating agencies.
The manned aircraft
provides
crew rescue capability
and longer-range communications,
which the drone
cannot match.
The drone
provides
sustained surveillance
and target identification
that
the manned aircraft
cannot afford
to maintain continuously.
The
[Federal Aviation Administration
Air Traffic Organization][ref_faa_ato]
publishes guidance
on
coordinated unmanned-manned operations
that programs operating
in this pattern
should follow.

The five patterns
are not exclusive.
A large incident
may exercise
two or three patterns simultaneously,
namely
single-class parallel
for the multicopter swarm
covering an urban-area perimeter,
cross-class parallel
for the fixed-wing
covering the wilderness area
beyond the perimeter,
and manned-unmanned teaming
for the helicopter
extracting subjects
that the unmanned aircraft locates.
A program preparing
for the largest incidents
in its mission profile
should
plan the multi-pattern operation
through tabletop exercises
before
the incident requires it.

## Airspace and Regulatory Posture by Level

The airspace and regulatory considerations
the program manager faces
follow
the operational level
in predictable ways.

| Level | Dominant airspace | Routine authorisation | OOP exposure | BVLOS need |
|---|---|---|---|---|
| 1 | Class B and C | LAANC every operation | Routine | None |
| 2 | Class C, D, and G | LAANC for controlled segments | Routine in built segments | Rare |
| 3 | Class G with some D | LAANC near small airports | Occasional | Occasional |
| 4 | Class G | None routinely | Rare | Routine |

The
[FAA UAS Facility Maps][ref_uas_facility_maps]
identify
the controlled airspace
that
LAANC covers
across the United States.
A program manager
preparing for operations
should
identify
the LAANC coverage
of the program's typical operating area
before
committing to a platform mix
because
some platforms
have integrated LAANC support
that
substantially reduces
the per-operation overhead.
The
[FAA B4UFLY application][ref_b4ufly]
provides
operator-facing situational awareness
that
the program's pilots
should integrate
into
the pre-flight workflow.

The Operations Over People final rule
established
[four categories][ref_oop_categories]
for operations
over human beings.
Category 1
admits
operations
with platforms
under
0.55 pounds
without rotating parts
that
contact human skin.
Category 2
admits
operations
with platforms
under
55 pounds
that
meet
the ASTM F3322 parachute standard
and other criteria.
Category 3
admits
operations
with the same parachute standard
plus restrictions
on
proximity to open-air assemblies of people.
Category 4
admits
operations
under the platform's
Type Certification.
A Level 1 program
typically operates
under Category 2 or Category 3
with parachute-equipped platforms.
A Level 4 program
typically operates
outside the OOP rules
because
people are not present.

The Beyond Visual Line of Sight
regulatory pathway
follows
[the Section 44807 exemption process][ref_section_44807]
for individual operators,
the
[Centres of Excellence][ref_faa_coe_uas]
authorisations
for programs partnered with the Centres,
and eventually
[the Part 108 final rule][ref_part_108]
once finalised.
A Level 4 program
should consider
BVLOS authorisation
as a baseline operational requirement
rather than
as an exceptional capability,
because
the operating distances
in frontier areas
routinely exceed
visual line of sight.

## Funding by Level

The federal funding map
follows
the operational level
with some overlap.

**Urban Areas Security Initiative.**
[The UASI programme][ref_uasi]
funds
designated urban areas
that meet
the population density
and threat criteria
the
[Department of Homeland Security][ref_dhs]
publishes.
The
[current UASI eligible-areas list][ref_uasi_eligible]
identifies
the metropolitan statistical areas
that
draw UASI funds.
Level 1 programs
in qualifying metros
draw routinely on UASI.
Level 2 programs
in suburban counties
of UASI-qualifying metros
draw indirectly
through sub-recipient arrangements.
Level 3 and Level 4 programs
do not access UASI
because
their operating area
does not qualify.

**State Homeland Security Programme.**
[The SHSP programme][ref_shsp]
funds
state and local government
all-hazards preparedness
including drone acquisition
under approved investment justifications.
Level 2, 3, and 4 programs
draw on SHSP
through
[State Administrative Agency][ref_state_admin_agency]
arrangements.
The Urban Areas Security Initiative
[was consolidated into SHSP for fiscal year 2025][ref_hsgp_consolidation]
under
the
[Department of Homeland Security
Homeland Security Grant Program][ref_dhs_hsgp]
as
A146 noted.

**Tribal Homeland Security Grant Program.**
[The THSGP][ref_thsgp]
funds
recognised tribal governments
for all-hazards preparedness
on tribal lands.
A Level 4 program
operating on
or adjacent to
tribal lands
should
identify
the relevant THSGP applicant
within the tribal government structure.

**Federal Emergency Management Agency
Assistance to Firefighters Grant.**
[The AFG programme][ref_fema_afg]
funds
fire departments
including unmanned aerial vehicle acquisition
where mission alignment is clear.
Available across all four levels.

**Federal frontier-operating agency budgets.**
The
[National Park Service][ref_nps_uas],
[Bureau of Land Management][ref_blm_uas],
[United States Forest Service][ref_usfs_uas],
[United States Coast Guard][ref_uscg_uas],
and
[United States Fish and Wildlife Service][ref_usfws_uas]
operate
their own UAS programmes
funded through
the agency's annual appropriation
rather than through
the grant programmes
that serve state and local programs.
A Level 4 program
operating in cooperation with
a federal agency
should
explore
joint procurement
or asset-sharing arrangements
through the agency's UAS programme office.

**USDA Rural Development.**
[Rural Development][ref_usda_rd]
operates
several grant programmes
that may admit
SAR equipment acquisition
in qualifying rural areas.
The mission alignment
is less clean
than DHS or FEMA programmes
but
a Level 3 or Level 4 program
should check
the current Rural Development priorities
during the funding-source survey.

## Crew Complement by Level

The crew complement
that the program must support
follows
the operational level.

**Level 1.**
Full multi-person crews.
A typical mission
runs
a remote pilot in command,
a visual observer,
a sensor operator,
a search team coordinator,
and a UAS Group Supervisor
who integrates
with the
Incident Command System
under the
[National Incident Management System][ref_nims_framework].
The program supports
five to fifteen qualified operators
on each platform type
to maintain
weather, illness,
and turnover resilience.

**Level 2.**
Similar to Level 1
but with smaller operator populations.
Three to seven operators
per platform type
is typical.
The UAS Group Supervisor role
exists
during major incidents
but may be combined with
the Operations Section Chief role
on smaller incidents.

**Level 3.**
Often single-pilot operations
on routine searches,
with full crews assembled
for major incidents.
Two to five operators
per platform type
is typical.
The crew complement
may include
volunteer operators
under
[DRONERESPONDERS UNITE][ref_droneresponders_unite]
mutual-aid arrangements.

**Level 4.**
Deployed teams
that
must
be self-contained.
A typical deployment
includes
two operators per platform
plus
a maintenance technician
and an Incident Command interface.
The operating tempo
is slow but sustained,
which
favours
operators
with cross-platform qualifications
to maintain readiness
during the slow periods.

| Level | Typical crew per mission | Operators per platform type | UAS Group Supervisor |
|---|---|---|---|
| 1 | 5 to 10 | 5 to 15 | Dedicated role |
| 2 | 4 to 8 | 3 to 7 | Major incidents only |
| 3 | 1 to 5 | 2 to 5 | Major incidents only |
| 4 | 4 to 8 deployed | 2 to 6 deployed | Joint with federal partner |

## The Quartet Reading Order

The four articles in this series
serve
four distinct decisions
that
a SAR program manager faces.
The reading order
depends on
the manager's starting position.

| Article | Decision | Read this if you... |
|---|---|---|
| A145 | Which platform classes are essential | Are starting from zero and need to understand the categories |
| A146 | How to buy the platforms | Have a budget and need to make procurement decisions |
| A147 | When and how to build or modify | Have engineering capacity or are pursuing federal R&D funding |
| A148 | What fleet for your specific setting | Have identified the program's geographic operating environment |

A program manager
beginning a new program
reads
A145 then A146 then A148,
treating A147
as optional
if no in-house engineering capacity
is planned.

A program manager
expanding an existing program
reads
A148 first
to identify
the fleet recommendations
for the program's setting,
then
A146 for the procurement details
and A145 for the underlying physics.

A research and development program manager
reads
A147
as the primary article,
treating
A145 through A148
as the contextual framework.

The quartet
together
addresses
the fleet selection,
the procurement,
the development,
and the geographic deployment
of a search and rescue
unmanned aerial vehicle programme.
The detailed engineering of specific airframes,
the regulatory deep-dive,
and
the operations-in-the-field manuals
remain
the subject
of subsequent articles
or of
specialised reference works
outside this series.

## Out of Scope

This article restricts itself
to the geographic-setting filter
for US-based
search and rescue
unmanned aerial vehicle programmes
in 2026.
Four substantive topics
are deliberately deferred.

**International geographic classification systems.**
The Eurostat
Degree of Urbanisation
classification,
the Canadian Census Metropolitan Area
classification,
and analogous systems
in other jurisdictions
follow different
methodologies
and admit different
fleet decisions
that this article does not address.

**Detailed airspace charting and waiver preparation.**
A program manager
preparing
specific airspace authorisations
should
consult
the
[Federal Aviation Administration UAS Operations][ref_faa_uas_operations]
pages directly
for
the current waiver process,
the LAANC self-service paths,
and
the Certificate of Waiver or Authorization
applications.
A148
points at the requirements
without
walking through
the application procedures.

**Specific operational tactics
for each level.**
The
[DRONERESPONDERS UNITE][ref_droneresponders_unite]
programme
publishes
operational guides
that
the program operators
should consult.
A148 addresses
the platform selection
that the operations support,
not
the operational procedures themselves.

**State-by-state regulatory variation.**
State and local
regulatory environments
overlay
the federal framework
in ways that
this article cannot address
across all fifty states.
A program manager
should consult
state-specific legal advice
before
committing to a fleet
or
to an operational concept.

## Conclusion

A search and rescue
unmanned aerial vehicle programme
in 2026
faces
four sequential decisions
that
the four articles in this series
address in sequence.
A145 explained
which platform classes
the programme needs.
A146 gave
the buyer's framework
for acquiring the platforms.
A147 covered
the research and development
pathway for programmes
that go beyond
the commercial market.
A148 places
the platform selection
in the geographic setting
in which the programme operates,
because
the operating setting
shapes
the platform mix,
the airspace posture,
the funding landscape,
the crew complement,
and the parallel-operations pattern
that the programme must support.

The four operational levels
provide
a coarse but useful
geographic classification
that
maps to existing federal systems.
A Level 1 programme
fields
a multicopter-dominated fleet
under Operations Over People rules
in controlled airspace
with full multi-person crews
funded
through
the Urban Areas Security Initiative
and
the State Homeland Security Programme.
A Level 4 programme
fields
a long-endurance fixed-wing fleet
in uncontrolled airspace
with deployed teams
under
Section 44807 exemptions
funded
through
the federal frontier-operating agency budgets
and
the Tribal Homeland Security Grant Program
where applicable.
Levels 2 and 3
fall between
these extremes
with their characteristic
configurations.

The parallel-operations patterns
that
the four levels
each admit
include
single-aircraft serial,
single-class parallel,
cross-class parallel,
multi-aircraft swarms,
and manned-unmanned teaming.
A programme preparing
for the largest incidents
in its mission profile
should
plan
the multi-pattern operations
through tabletop exercises
before
the incident
requires it.

The quartet of articles
is now complete
for the US-based
search and rescue
unmanned aerial vehicle programme
audience.
A program manager
with the four decisions
in hand
has
the analytical framework
to build,
acquire,
deploy, and
sustain
a credible programme
in the regulatory,
fiscal,
and geographic environment
of 2026.

## References

- [Reference, ASTM F3322 Standard Specification for sUAS Parachutes][ref_astm_f3322]
- [Reference, Bureau of Land Management Unmanned Aircraft Systems][ref_blm_uas]
- [Reference, CDC NCHS Urban-Rural Classification Scheme for Counties][ref_cdc_nchs]
- [Reference, DJI FlightHub 2 Multi-Drone Management][ref_dji_flighthub]
- [Reference, DRONERESPONDERS UNITE Programme][ref_droneresponders_unite]
- [Reference, Doodle Labs Mesh Rider][ref_doodle_labs]
- [Reference, Dronesense Multi-Drone Management][ref_dronesense]
- [Reference, Aloft Air Control][ref_aloft_air_control]
- [Reference, Department of Energy ARM Aerial Facility][ref_doe_arm]
- [Reference, Department of Homeland Security][ref_dhs]
- [Reference, Department of Homeland Security Homeland Security Grant Program][ref_dhs_hsgp]
- [Reference, DARPA OFFSET Swarm Tactics Legacy][ref_darpa_offset_legacy]
- [Reference, Edge Autonomy Penguin C Mk2][ref_penguin_c]
- [Reference, FAA Air Traffic Organization][ref_faa_ato]
- [Reference, FAA Airspace Class B][ref_class_b]
- [Reference, FAA Airspace Class C][ref_class_c]
- [Reference, FAA Airspace Class D][ref_class_d]
- [Reference, FAA Airspace Class G][ref_class_g]
- [Reference, FAA B4UFLY Application][ref_b4ufly]
- [Reference, FAA Centres of Excellence for UAS][ref_faa_coe_uas]
- [Reference, FAA UAS Facility Maps][ref_uas_facility_maps]
- [Reference, FAA UAS Operations][ref_faa_uas_operations]
- [Reference, FEMA Assistance to Firefighters Grant Programme][ref_fema_afg]
- [Reference, FEMA Homeland Security Grant Program Consolidation Notice][ref_hsgp_consolidation]
- [Reference, FEMA State Administrative Agency][ref_state_admin_agency]
- [Reference, FEMA Tribal Homeland Security Grant Program][ref_thsgp]
- [Reference, FEMA Urban Areas Security Initiative][ref_uasi]
- [Reference, FEMA Urban Areas Security Initiative Eligible Areas][ref_uasi_eligible]
- [Reference, Iridium Certus Satellite Communications][ref_iridium_certus]
- [Reference, Low Altitude Authorization and Notification Capability][ref_laanc]
- [Reference, National Incident Management System Framework][ref_nims_framework]
- [Reference, National Park Service Unmanned Aircraft Systems][ref_nps_uas]
- [Reference, Operations Over People Categories][ref_oop_categories]
- [Reference, Operations Over People Final Rule of 2021][ref_oop_final_rule]
- [Reference, Part 107 Subpart D Operations Over Human Beings][ref_part_107_subpart_d]
- [Reference, Part 108 Beyond Visual Line of Sight Rule][ref_part_108]
- [Reference, Section 44807 of Title 49 United States Code][ref_section_44807]
- [Reference, Silvus Technologies StreamCaster][ref_silvus_streamcaster]
- [Reference, Skydio Dock Persistent Operations][ref_skydio_dock]
- [Reference, Starlink Satellite Internet Service][ref_starlink]
- [Reference, State Homeland Security Programme][ref_shsp]
- [Reference, United States Coast Guard Unmanned Aircraft Systems][ref_uscg_uas]
- [Reference, United States Fish and Wildlife Service Unmanned Aircraft Systems][ref_usfws_uas]
- [Reference, United States Forest Service Unmanned Aircraft Systems][ref_usfs_uas]
- [Reference, USDA Economic Research Service Frontier and Remote Area Codes][ref_far]
- [Reference, USDA Economic Research Service Rural-Urban Commuting Area Codes][ref_ruca]
- [Reference, USDA Economic Research Service Rural-Urban Continuum Codes][ref_rucc]
- [Reference, USDA Rural Development][ref_usda_rd]
- [Related Post, A Buyer's Decision Framework for Search and Rescue Drones][related_post_a146_buying]
- [Related Post, Fixed-Wing Multicopter and Hybrid Drones for Search and Rescue Physics and Economics][related_post_a145_physics]
- [Related Post, Research and Development for Search and Rescue Drones][related_post_a147_rd]

[ref_aloft_air_control]: https://www.aloft.ai/
[ref_astm_f3322]: https://store.astm.org/f3322-24a.html
[ref_b4ufly]: https://www.faa.gov/uas/getting_started/b4ufly
[ref_blm_uas]: https://www.blm.gov/programs/aviation/unmanned-aircraft-systems
[ref_cdc_nchs]: https://www.cdc.gov/nchs/data-analysis-tools/urban-rural.html
[ref_class_b]: https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap3_section_2.html
[ref_class_c]: https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap3_section_2.html
[ref_class_d]: https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap3_section_2.html
[ref_class_g]: https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap3_section_3.html
[ref_darpa_offset_legacy]: https://www.darpa.mil/research/programs/offensive-swarm-enabled-tactics
[ref_dhs]: https://www.dhs.gov/
[ref_dhs_hsgp]: https://www.fema.gov/grants/preparedness/homeland-security
[ref_dji_flighthub]: https://enterprise.dji.com/flighthub-2
[ref_doe_arm]: https://www.arm.gov/capabilities/observatories/aaf/uas
[ref_doodle_labs]: https://doodlelabs.com/products/mesh-rider/
[ref_droneresponders_unite]: https://www.droneresponders.org/unite
[ref_dronesense]: https://www.dronesense.com/
[ref_faa_ato]: https://www.faa.gov/about/office_org/headquarters_offices/ato
[ref_faa_coe_uas]: https://www.faa.gov/about/office_org/headquarters_offices/ang/grants/coe_uas
[ref_faa_uas_operations]: https://www.faa.gov/uas/commercial_operators
[ref_far]: https://www.ers.usda.gov/data-products/frontier-and-remote-area-codes
[ref_fema_afg]: https://www.fema.gov/grants/preparedness/firefighters
[ref_hsgp_consolidation]: https://www.fema.gov/grants/preparedness/homeland-security
[ref_iridium_certus]: https://www.iridium.com/markets/uav/
[ref_laanc]: https://www.faa.gov/uas/getting_started/laanc
[ref_nims_framework]: https://www.fema.gov/emergency-managers/nims
[ref_nps_uas]: https://www.nps.gov/subjects/aviation/aviation-search-rescue.htm
[ref_oop_categories]: https://www.faa.gov/uas/commercial_operators/operations_over_people
[ref_oop_final_rule]: https://www.federalregister.gov/documents/2021/01/15/2020-28947/operation-of-small-unmanned-aircraft-systems-over-people
[ref_part_107_subpart_d]: https://www.ecfr.gov/current/title-14/chapter-I/subchapter-F/part-107/subpart-D
[ref_part_108]: https://www.federalregister.gov/documents/2025/08/07/2025-14837/normalizing-unmanned-aircraft-systems-beyond-visual-line-of-sight-operations
[ref_penguin_c]: https://edgeautonomy.io/uncrewed-systems/penguin-c-mk2/
[ref_ruca]: https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes
[ref_rucc]: https://www.ers.usda.gov/data-products/rural-urban-continuum-codes
[ref_section_44807]: https://www.law.cornell.edu/uscode/text/49/44807
[ref_shsp]: https://www.fema.gov/grants/preparedness/homeland-security/state-shsp
[ref_silvus_streamcaster]: https://silvustechnologies.com/products/streamcaster-radios/
[ref_skydio_dock]: https://www.skydio.com/dock
[ref_starlink]: https://www.starlink.com/business
[ref_state_admin_agency]: https://www.fema.gov/grants/preparedness/state-administrative-agency-contacts
[ref_thsgp]: https://www.fema.gov/grants/preparedness/tribal-homeland-security
[ref_uas_facility_maps]: https://udds-faa.opendata.arcgis.com/pages/uas-facility-maps
[ref_uasi]: https://www.fema.gov/grants/preparedness/homeland-security/uasi
[ref_uasi_eligible]: https://www.fema.gov/grants/preparedness/homeland-security/uasi
[ref_uscg_uas]: https://www.dco.uscg.mil/Our-Organization/Assistant-Commandant-for-Acquisitions-CG-9/Programs/Surface-Programs/Unmanned-Aerial-Systems/
[ref_usda_rd]: https://www.rd.usda.gov/programs-services/community-facilities
[ref_usfs_uas]: https://www.fs.usda.gov/managing-land/fire/aviation/uas
[ref_usfws_uas]: https://www.fws.gov/program/aviation/what-we-do
[related_post_a145_physics]: {% post_url 2026-05-15-fixed_wing_multicopter_and_hybrid_drones_for_search_and_rescue %}
[related_post_a146_buying]: {% post_url 2026-05-16-buyers_decision_framework_for_search_and_rescue_drones %}
[related_post_a147_rd]: {% post_url 2026-05-17-research_and_development_for_search_and_rescue_drones %}
