---
layout: post
mathjax: false
comments: true
title: "What Does the United States Space Force Do?"
date: 2026-02-28 00:00:00 +0000
categories: space military
---

<!-- A97 -->

The United States Space Force, or USSF,
is the newest branch of the United States Armed Forces.
Established on 20 December 2019,
it is the first new military service
created since the Air Force separated from the Army in 1947,
a gap of 72 years.
Despite its establishment,
the Space Force remains poorly understood.
Many people, including servicemembers in other branches,
have no clear idea what the Space Force actually does.

This article addresses that gap.
It traces the history that led to the Space Force's creation,
explains why a separate branch was necessary,
and describes the full range of missions
that the Space Force performs today.
Those missions include satellite communications,
global navigation, missile warning,
space domain awareness, launch operations,
nuclear command and control support,
intelligence and reconnaissance,
cyber and electronic warfare,
weather monitoring,
and offensive and defensive space operations.
Together, these capabilities underpin
virtually every military operation
conducted by every other branch.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-02-28 00:00:00 +0000

# OS and Version
$ uname -vm
Darwin Kernel Version 23.6.0: Mon Jul 29 21:14:30 PDT 2024; root:xnu-10063.141.2~1/RELEASE_ARM64_T6000 arm64

$ sw_vers
ProductName:		macOS
ProductVersion:		14.6.1
BuildVersion:		23G93

# Hardware Information
$ system_profiler SPHardwareDataType | sed -n '8,10p'
      Chip: Apple M1 Max
      Total Number of Cores: 10 (8 performance and 2 efficiency)
      Memory: 32 GB

# Shell and Version
$ echo "${SHELL}"
/bin/bash

$ "${SHELL}" --version | head -n 1
GNU bash, version 3.2.57(1)-release (arm64-apple-darwin23)

# Claude Code Installation Versions
$ claude --version
2.1.42 (Claude Code)
```

## History

### Military Space Before the Space Force

The United States military began conducting space operations
long before the Space Force existed.
After World War II,
the [Army Ballistic Missile Agency][ref_abma]
was established on 1 February 1956
at Redstone Arsenal in Huntsville, Alabama,
under Major General John B. Medaris
with Wernher von Braun as technical director.
Von Braun's team developed the Jupiter-C rocket,
which served as the basis for the Juno I rocket
that launched Explorer 1,
the first American satellite,
on 31 January 1958.
The Army viewed rocketry
as a natural extension of artillery.

The Air Force pursued its own path.
In 1954, the Western Development Division
was established under Brigadier General Bernard A. Schriever
to manage the Atlas intercontinental ballistic missile project.
Schriever's organization rapidly expanded
to include the Titan and Thor missile programs
and became the foundation
for the Air Force's early space activities.
In 1961, the Air Force was designated
as the [Department of Defense][ref_dod_space]
executive agent for space,
and the Space Systems Division
was established as the first Air Force division
focused solely on space.

Over the following decades,
the organizational home for military space
changed names repeatedly.
The Space Systems Division became
the Space and Missile Systems Organization in 1967,
which was renamed the Space Division in 1979.
In October 1981,
the Air Force established
a Directorate of Space Operations
under the Deputy Chief of Staff for Operations.

This organizational fragmentation
led to the creation of
[Air Force Space Command][ref_afspc], or AFSPC,
on 1 September 1982
at Peterson Air Force Base in Colorado.
AFSPC consolidated space operations
under a single major command.
During the 1980s,
it absorbed space missions
from Strategic Air Command
and launch missions from Air Force Systems Command.
By 1984, AFSPC had assumed responsibility
for the Defense Meteorological Satellite Program,
the Defense Support Program,
the Military Strategic and Tactical Relay satellite system
known as Milstar,
and the Global Positioning System, or GPS.
AFSPC would manage military space operations
for the next 37 years.

### The Precedent of Air Force Independence

The debate over whether space operations
deserved a separate military service
directly mirrors an earlier debate
over whether air operations
deserved a separate service.

Army airmen had advocated
for an independent air service [since 1919][ref_af_founding].
Brigadier General Billy Mitchell,
the most prominent early advocate,
argued that air power
was a fundamentally distinct domain of warfare
that could not reach its potential
while subordinated to ground force priorities.
Mitchell was court-martialed in 1925
for publicly accusing senior Army and Navy leaders
of "almost treasonable administration
of the national defense."
His arguments would prove prescient.

During World War II,
the Army Air Corps expanded
into the Army Air Forces,
which functioned as a de facto separate service
with its own chain of command,
its own training pipeline,
and its own strategic doctrine.
After the war,
advocates of air power independence
argued that the Army's leadership culture,
centered on infantry and artillery officers,
systematically deprioritized aviation
in budgets, promotions,
and strategic planning.

The Army resisted.
Army leadership argued
that air and ground operations were inseparable,
that creating a new service
would introduce unnecessary bureaucracy,
and that a unified command structure
was more operationally effective.
The Navy opposed independence as well,
fearing that a new air service
would absorb naval aviation,
as had occurred in the United Kingdom
when the Royal Air Force was created.

On 26 July 1947,
President Truman signed
the [National Security Act of 1947][ref_nsa_1947],
which established
the National Military Establishment,
later renamed the Department of Defense,
the National Security Council,
the Central Intelligence Agency,
and an independent Department of the Air Force.
The United States Air Force
became a separate military service
on [18 September 1947][ref_usaf].

The arguments that the Army used
against Air Force independence
would reappear almost verbatim
seven decades later,
this time from the Air Force itself.

### Calls for a Separate Space Service

The first formal call for a separate space service
came from the Commission to Assess
United States National Security Space Management
and Organization,
chaired by Donald Rumsfeld.
The commission was established in 1999
and released its report
on [11 January 2001][research_rumsfeld_commission].

The Rumsfeld Commission warned
that the United States was
"more dependent on space than any other nation,"
making it an "attractive candidate
for a 'Space Pearl Harbor.'"
The commission examined the costs and benefits
of an independent military department for space
and recommended, as an intermediate step,
a "Space Corps" within the Air Force
analogous to the Marine Corps
within the Department of the Navy.
Rumsfeld became Secretary of Defense in January 2001
and ordered that military space programs
be consolidated under a four-star Air Force general.
The September 11 attacks subsequently redirected
national security priorities,
and the commission's vision was deferred
for more than a decade.

In 2017, Representative Mike Rogers of Alabama,
chairman of the House Armed Services Committee
Strategic Forces Subcommittee,
and Representative Jim Cooper of Tennessee,
the ranking member,
introduced a [bipartisan proposal][research_space_corps_proposal]
to establish a United States Space Corps.
The House Armed Services Committee
voted 60 to 1 to include the Space Corps provision
in its version of the National Defense Authorization Act,
or NDAA.
Rogers and Cooper stated
that "the strategic advantages the U.S. derives
from national security space systems are eroding"
and that "the Department of Defense is unable
to take necessary measures
to address these challenges effectively."

The Air Force lobbied Congress
to defeat the provision.
Rogers [publicly warned][research_rogers_warning]
the Air Force not to resist,
stating that the Air Force had been given
"20 years to get it right and they haven't."
The Space Corps provision was included
in the House version of the NDAA
but was dropped
during conference negotiations with the Senate
in November 2017.

### Air Force Resistance

The [Air Force Association][research_afa_opposition],
or AFA,
the Air Force's primary professional organization,
formally opposed the establishment of a Space Force.
The AFA argued
that "effects from air and space
have been integrated and are indivisible."
Air Force leaders stated
that anything separating space from the joint fight
was "moving us in the wrong direction."

The Air Force raised three primary objections.
First, it projected that standing up
a separate Space Force and Space Command
would cost nearly 13 billion dollars over five years.
Second, it argued that an independent Space Corps
would create an unnecessary parallel bureaucracy,
diverting money to headquarters functions
rather than space operations.
Third, it framed the question
as one of timing rather than principle,
arguing that conditions for a separate armed force
were not yet met.

These arguments are noteworthy
because they are substantively identical
to the arguments
that the Army used against Air Force independence
in the 1940s.
In both cases, the parent service argued
that the domains were inseparable.
In both cases, the parent service argued
that separation would create wasteful bureaucracy.
And in both cases,
the emerging domain's advocates argued
that cultural dominance
by the parent service's core identity,
infantry and artillery for the Army
and fighter pilots for the Air Force,
systematically disadvantaged the emerging mission area.

### Establishment

On 18 June 2018,
at the third public meeting of the National Space Council,
President Trump directed the Department of Defense
to "immediately begin the process necessary
to establish a Space Force as a new military branch."
On 19 February 2019,
Trump signed [Space Policy Directive 4][ref_spd4], or SPD-4,
formally titled
"Establishment of the United States Space Force."
SPD-4 directed the Department of Defense
to develop a legislative proposal
establishing the Space Force
as a sixth branch of the Armed Forces
within the Department of the Air Force.

On 20 December 2019,
President Trump signed
the [National Defense Authorization Act
for Fiscal Year 2020][ref_ndaa_fy2020]
into law.
The legislation, designated Senate bill 1790
and enacted as Public Law 116-92,
passed the House of Representatives 377 to 48
and the Senate 86 to 8.
Section 952 of the Act redesignated
Air Force Space Command
as the United States Space Force.
The Space Force is codified
in [Title 10, United States Code, Section 9081][ref_10usc9081].

General John W. "Jay" Raymond
became the first [Chief of Space Operations][ref_raymond]
on the same day the legislation was signed.
He had previously served
as Commander of Air Force Space Command
since October 2016.
Approximately 16,000 active-duty personnel and civilians
who had been assigned to AFSPC
were redesignated as Space Force personnel.

The Space Force became
the first new branch of the United States Armed Forces
in 72 years.

## Why a Separate Space Force?

### Fighter Pilot Culture

The most fundamental justification
for a separate Space Force
lies in the cultural dynamics
of the organization that previously managed military space.

A study by the [RAND Corporation][research_rand_fighter_culture],
sponsored by the Department of Defense's
Office of Net Assessment,
documented the dominance
of fighter pilots
in Air Force senior leadership.
The study found that
the fighter pilot community
constitutes only approximately 5.3 percent
of the entire Air Force officer corps,
yet holds a disproportionate share
of senior leadership positions.
At the time of the study,
all but 3 of the Air Force's 11 four-star generals
were pilots.
Twenty-five of 40 three-star generals,
nearly two-thirds,
were pilots.
The remaining senior positions
were distributed among navigators, flight surgeons,
lawyers, engineers, logisticians,
and space officers.

The Air Force's cultural hierarchy
places fighter pilots first,
bomber pilots second,
and all other specializations after.
This hierarchy has deep historical roots.
The early Air Force was dominated
by the "Bomber Mafia,"
strategic bombing advocates
such as Carl Spaatz, Hoyt Vandenberg,
and Thomas White.
Over time, fighter pilots supplanted bomber pilots
as the dominant cultural force.
General Norton A. Schwartz,
who served as Chief of Staff from 2008 to 2012,
was notable as the first officer
appointed to that position
who did not have a background
as a fighter or bomber pilot.
He was an airlift and special operations pilot.

This cultural dominance
had measurable consequences for space operators.
Space officers were promoted
at rates [below average][research_space_promotion]
for the ranks of major and lieutenant colonel,
while pilots were promoted at rates above average.
Promotion boards rewarded officers
who commanded tactical units in the field
and had multiple combat deployments,
criteria that structurally favored pilots
over space operations officers.

### Space as a Deprioritized Mission

The fighter pilot culture
translated into tangible resource allocation decisions
that disadvantaged space programs.

Congress funded a Commercial Satellite Communications
Integration program
in the 2019 defense budget,
but the Air Force
did not include the program
in its own budget request for the following year.
Satellite industry executives expressed frustration
that the Pentagon's 2020 budget request
sought no money
for the commercial satellite communications integration program
that Congress had specifically created.

This pattern of congressional intent
being deprioritized by the Air Force
was not an isolated incident.
The criteria used to evaluate officers for promotion
rewarded working in tactical combat roles
and attending programs
like the Air Force Weapons School.
Deep institutional knowledge
of specific space programs,
the kind of expertise essential
for satellite operations and acquisition,
was not valued equivalently.
Space operators who spent their careers
mastering satellite constellations
found themselves competing for promotion
against pilots with combat deployments,
and losing.

One proposed remedy
was to create a separate competitive category
for space officers,
ensuring that space operators would compete
against other space operators for promotions
rather than against pilots.
The creation of a separate Space Force
accomplished this goal at the service level
rather than through internal Air Force reforms.

### Space as a Warfighting Domain

The strategic environment also changed.
Russia reorganized its space military capabilities
under the [Russian Space Forces][ref_russian_space_forces]
and later integrated them
into the Aerospace Forces.
China established the
[People's Liberation Army Strategic Support Force][ref_pla_ssf]
with responsibility for space,
cyber, and electronic warfare.
Both nations developed
and in some cases tested
anti-satellite weapons.

Space was no longer
a benign support function
providing communications and navigation
to terrestrial forces.
It had become a contested warfighting domain
where adversaries could threaten,
degrade, and destroy
the satellite constellations
on which the entire American military depends.
A contested domain requires its own doctrine,
its own culture,
its own acquisition priorities,
and its own career paths.
The Air Force, shaped by decades of fighter pilot culture,
could not provide these.

## What the Space Force Does

### Satellite Communications

The Space Force operates
multiple satellite communication constellations
providing secure, global communications
to all branches of the military and to allied partners.

The oldest active system
is the Military Strategic and Tactical Relay system,
or [Milstar][ref_milstar],
which has exceeded 30 years of operations
and surpassed its design life by three times.
Milstar provides survivable, jam-resistant communications
for strategic and tactical users.

The [Advanced Extremely High Frequency][ref_aehf] satellite system,
or AEHF,
is a constellation of six satellites
in geostationary orbit,
launched between 2010 and 2020.
AEHF provides survivable, global, secure,
protected, and jam-resistant communications
for high-priority military assets
on the ground, at sea, and in the air.
The system is a joint program
serving the United States, the United Kingdom,
Canada, the Netherlands, and Australia.

The [Wideband Global SATCOM][ref_wgs] system, or WGS,
consists of ten satellites
providing high-capacity wideband communications.
International partners include Australia, Canada,
Denmark, Luxembourg, the Netherlands, and New Zealand.

Looking ahead,
the Evolved Strategic SATCOM program, or ESS,
will replace AEHF
as the backbone for joint nuclear command,
control, and communications.
Boeing was awarded a 2.8 billion dollar contract
in July 2025 for the first two ESS satellites,
with initial operational capability expected by 2032.

### Global Positioning System

The Space Force operates
the [Global Positioning System][ref_gps], or GPS,
a constellation of 31 to 32 satellites
in medium Earth orbit
at approximately 20,200 kilometers altitude.
GPS provides positioning, navigation,
and timing services
used by billions of people worldwide
and by virtually all modern military operations.

Military GPS capabilities
extend well beyond civilian navigation.
The GPS III satellites
provide up to eight times the jam resistance
of earlier variants.
The military Precise Positioning Service
uses the encrypted M-code signal,
which offers higher accuracy
and anti-spoofing protection
unavailable to civilian users.
GPS supports precision-guided munitions,
troop movements, logistics, drone operations,
and timing synchronization
for secure communications and electronic warfare.

The ninth GPS III satellite
launched on 27 January 2026
from Cape Canaveral Space Force Station.
The tenth and final GPS III satellite
is scheduled for launch in March 2026,
completing the GPS III program.
Twenty-two GPS IIIF follow-on satellites
are in development with Lockheed Martin,
incorporating enhanced anti-jam capability.

### Missile Warning

The Space Force provides
continuous, global missile warning
through space-based infrared sensors
that detect the heat signatures
of ballistic missile launches within seconds of ignition.

The current system is the
[Space-Based Infrared System][ref_sbirs], or SBIRS,
consisting of six satellites in geostationary orbit
launched between 2011 and 2022
and four sensor payloads
in highly elliptical orbits
providing coverage of polar regions.
SBIRS provides capabilities
in missile warning, missile defense,
battlespace characterization,
and technical intelligence.

The [Next-Generation Overhead Persistent Infrared][ref_next_gen_opir] system,
or Next-Gen OPIR,
is replacing SBIRS
with sensors three times as sensitive
and twice as accurate.
The new system is specifically designed
to detect the weaker infrared signatures
of hypersonic weapons and non-ballistic missiles,
threats that did not exist
when SBIRS was designed.
The first Next-Gen OPIR satellite
was delivered in September 2025,
with launch planned for no earlier than March 2026.

On the ground,
the Space Force operates
the Phased Array Warning System, or PAVE PAWS,
for intercontinental ballistic missile
and submarine-launched ballistic missile detection.
The Perimeter Acquisition Radar
Attack Characterization System, or PARCS,
at Cavalier Space Force Station in North Dakota
provides attack characterization.
The COBRA DANE radar
at Eareckson Air Station in Alaska
provides missile tracking.

The Space Development Agency
is also building a Proliferated Warfighter Space Architecture
Tracking Layer,
a mesh network of smaller satellites
in low Earth orbit
designed to provide near-continuous global coverage
and fire-control-quality tracks for missile defense.

### Space Domain Awareness

The Space Force tracks
all artificial objects in Earth orbit,
from active satellites to debris,
to maintain awareness of the space environment
and detect potential threats.

The official space surveillance catalog
maintained by the 18th Space Defense Squadron
at Vandenberg Space Force Base
contains over 47,000 cataloged objects
larger than 10 centimeters.
Statistical models estimate
that approximately 1.2 million debris objects
larger than 1 centimeter exist in orbit,
though only those 10 centimeters and larger
are actively tracked.

The [Space Surveillance Network][ref_ssn]
is a global network
of ground-based radars, optical telescopes,
and space-based sensors
feeding data to the 18th Space Defense Squadron.
Key sensors include
the Ground-Based Electro-Optical Deep Space Surveillance system,
or GEODSS,
and the [Space Fence][ref_space_fence],
an S-band radar
located on Kwajalein Atoll
in the Marshall Islands
that was declared operational
on 28 March 2020.
The Space Fence can track approximately 200,000 objects
and make 1.5 million observations per day,
roughly ten times the number
made by previous assets.

The [Geosynchronous Space Situational Awareness Program][ref_gssap],
or GSSAP,
operates maneuverable satellites
in near-geosynchronous orbit
to conduct close inspections
of objects in geosynchronous orbit.
The Deep-Space Advanced Radar Capability, or DARC,
is a new radar system
designed to track multiple small objects
in geosynchronous orbit globally.
The first of three planned DARC sites
was constructed in Australia,
with a second site selected in the United Kingdom.

### Launch Operations

The Space Force manages
all national security space launches
through two primary launch ranges.

The Eastern Range
at [Cape Canaveral Space Force Station][ref_cape_canaveral] in Florida
handles launches to low-inclination
and geostationary orbits.
The Western Range
at [Vandenberg Space Force Base][ref_vandenberg] in California
handles launches to polar
and sun-synchronous orbits.
Space Launch Delta 45 manages the Eastern Range
and Space Launch Delta 30 manages the Western Range.

The [National Security Space Launch][ref_nssl] program, or NSSL,
entered Phase 3 in fiscal year 2026.
In April 2025,
the Space Force awarded 13.7 billion dollars
in Phase 3 launch contracts
to Blue Origin, SpaceX, and United Launch Alliance
for approximately 54 missions
from 2027 through 2032.

### Nuclear Command, Control, and Communications

The Space Force provides
critical enabling capabilities
for all three legs of the nuclear triad
through Nuclear Command, Control, and Communications,
or NC3.
NC3 is the secure and resilient system
ensuring effective command and control of nuclear forces
at all times,
including during a nuclear attack.

The AEHF satellites provide
jam-resistant, survivable strategic communications
for nuclear command authority,
ensuring that the President
can communicate with nuclear forces under all conditions.
SBIRS provides the initial missile warning
that triggers nuclear response decision-making,
detecting intercontinental ballistic missile
and submarine-launched ballistic missile launches
within seconds of ignition.
GPS provides precise timing
for secure communications and weapons delivery.

The Evolved Strategic SATCOM program
is designated as the future backbone
for joint nuclear command, control, and communications.
The Congressional Budget Office estimated in 2025
that Department of Defense efforts
to sustain and modernize NC3
would cost 154 billion dollars from 2025 through 2034.

### Intelligence, Surveillance, and Reconnaissance

The Space Force provides
space-based intelligence, surveillance,
and reconnaissance capabilities,
or ISR,
to detect, characterize, and target
adversary space capabilities
and support terrestrial operations.

Space Delta 7, the dedicated ISR and targeting delta
within Combat Forces Command,
provides time-sensitive and actionable intelligence
for space domain operations.
In May 2025,
the Space Force and the
National Geospatial-Intelligence Agency, or NGA,
signed a memorandum of agreement
delineating how the two organizations
share responsibilities
for purchasing commercial space-based intelligence.

The National Reconnaissance Office, or NRO,
remains the primary provider
of classified space-based ISR.
The NRO is currently building
what it describes as the largest government constellation
in history,
with proliferated launches continuing through 2029.
The Space Force and NRO coordinate closely,
with the Space Force retaining
its own tactical ISR capability
separate from the intelligence community.

### Cyber and Electronic Warfare

The Space Force conducts cyber operations
focused on defending space systems from cyber threats
and electronic warfare operations
to protect and deny the electromagnetic spectrum.

Space Delta 6 is the dedicated
cyberspace operations delta,
responsible for defending satellites,
ground control stations,
communication links,
and the broader satellite control infrastructure.
Space Delta 3 conducts
space electronic warfare operations.

The Space Force's cyber posture
is primarily defensive,
though the service acknowledges
it is developing
full-spectrum cyber capabilities.
Adversaries can target space systems
through ground station intrusion,
communication link jamming or spoofing,
and direct cyber attacks
on satellite command and control systems.

### Weather

The Space Force has historically operated
military weather satellites
and is currently navigating a transition
from legacy systems to next-generation capabilities.

The [Defense Meteorological Satellite Program][ref_dmsp], or DMSP,
is a legacy military weather satellite program.
Three DMSP satellites remain operational
but are more than a decade
past their expected end of life.
DMSP is scheduled for discontinuation
in September 2026.

The first Weather System Follow-on Microwave satellite,
or WSF-M,
launched in 2024
and was declared operational in April 2025.
WSF-M provides enhanced ocean surface vector wind
and tropical cyclone intensity data.
The transition from DMSP to its successors
presents a capability gap
that the Department of Defense
is managing through partnerships
with commercial and civil weather data providers.

### Offensive and Defensive Space Operations

In April 2025,
the Space Force published
"Space Warfighting: A Framework for Planners,"
its first doctrine document
explicitly codifying
offensive and defensive counter-space operations.
The document marked a shift
from the Space Force's historically supportive role
to treating space as a contested warfighting domain.

The framework organizes
[counter-space operations][research_warfighting_framework]
across three mission areas.
Orbital warfare encompasses actions
to destroy, disrupt, or degrade
adversary space platforms on orbit.
Electromagnetic warfare encompasses actions
to affect enemy space communications links,
including uplinks, downlinks, and crosslinks.
Cyberspace warfare encompasses actions
against the digital infrastructure
supporting adversary space systems.

Defensive operations include
both active space defense,
meaning real-time actions
to stop or limit adversary attacks
including escort and counterattack,
and passive space defense,
meaning measures to enhance survivability
including hardening, redundancy, maneuvering,
and dispersal across larger constellations.
The "Race to Resilience" initiative
aims to achieve battle-ready,
survivable architectures by 2026.

Space Delta 9, the orbital warfare delta,
is the Space Force's dedicated unit
for offensive space operations.
Specific capabilities and systems remain classified.

## Organization and Personnel

### Organizational Structure

The Space Force is organized
as a military service branch
within the [Department of the Air Force][ref_daf].
The Air Force and the Space Force together
compose the Department of the Air Force,
which is led by the Secretary of the Air Force,
a civilian official.
This structure directly parallels
the relationship between the Marine Corps
and the [Department of the Navy][ref_don],
where the Navy and the Marine Corps
are two separate military services
under a single civilian secretary.

The Chief of Space Operations
is a four-star general
who reports directly to the Secretary of the Air Force
and serves as a member
of the Joint Chiefs of Staff.
The current Chief of Space Operations
is General Chance Saltzman.

The Space Force is organized
into three [Field Commands][ref_ussf_organization].
[Combat Forces Command][ref_cfc], or CFC,
redesignated from Space Operations Command
on 3 November 2025,
oversees approximately 12,000 personnel
across 11 deltas, 82 squadrons,
and 25 units of action.
CFC is responsible for generating
and sustaining combat-ready space forces.
[Space Systems Command][ref_ssc], or SSC,
handles acquisition and development
and is headquartered
at Los Angeles Air Force Base.
Space Training and Readiness Command, or STARCOM,
provides training, education, doctrine,
and test and evaluation
and is headquartered
at Peterson Space Force Base.

The primary operational unit is the delta,
commanded by a colonel.
Mission deltas are responsible
for an entire mission set.
Space base deltas provide installation support.
Space launch deltas combine base support
and launch mission responsibilities.

Key installations include
[Peterson Space Force Base][ref_peterson] in Colorado,
which houses the Space Force headquarters,
STARCOM, United States Space Command,
and the North American Aerospace Defense Command.
[Schriever Space Force Base][ref_schriever] in Colorado
houses the National Space Defense Center
and multiple satellite operations squadrons.
[Buckley Space Force Base][ref_buckley] near Denver
is a critical node for missile warning
and infrared satellite operations.
Cape Canaveral Space Force Station in Florida
and Vandenberg Space Force Base in California
serve as the primary launch sites.

### Guardians

Members of the Space Force
are called [Guardians][ref_ussf].
As of late 2025,
there are approximately 9,670 uniformed Guardians
plus civilians,
for a total workforce exceeding 15,000.
The authorized end strength
for fiscal year 2026 is 10,400,
an increase of 600 from fiscal year 2025.
The Space Force's top enlisted leader
stated in February 2026
that the service needs to double in size
to meet national security requirements.

The Space Force uses
a unique enlisted rank structure.
Enlisted grades E-1 through E-4
use the title "Specialist"
followed by a number from one to four,
a convention unique to the Space Force.
Non-commissioned officer status begins at E-5
with the rank of Sergeant.
Officer ranks use the same titles
as the Army, Marine Corps, and Air Force.

Recruitment has consistently exceeded goals.
The Space Force hit its fiscal year 2025
recruiting goal of 796 three months early,
ultimately enlisting 819 recruits.
By February 2026,
five months into fiscal year 2026,
the Space Force had already exceeded
its annual recruiting goal of 730 by 25 percent.

The Space Force's fiscal year 2026 budget request
was 39.9 billion dollars,
the largest in the service's history
and a 30 percent increase from fiscal year 2025.
This represents approximately 3 percent
of the total Department of Defense budget request.
On a per capita basis,
the Space Force is by far
the most capital-intensive branch,
spending roughly 3.8 million dollars per Guardian
compared to approximately 424,000 dollars per Airman.
This disparity reflects
the extremely high cost of satellite systems,
launch vehicles, and ground infrastructure
rather than personnel expenditure.

## Conclusion

The United States Space Force exists
because space became a contested warfighting domain
that required dedicated institutional advocacy,
career paths, acquisition priorities, and doctrine.
The historical parallel
to the Air Force's separation from the Army
is direct and instructive.
In both cases,
a new domain of warfare
outgrew the institutional capacity
of its parent service.
In both cases,
the parent service resisted separation
with identical arguments.
And in both cases,
the emerging domain's advocates prevailed
because the operational requirements of the new domain
could not be met
within a culture shaped by different priorities.

The Space Force's mission portfolio
is broad and consequential.
Satellite communications
connect every deployed American military unit
to its chain of command.
The Global Positioning System enables
precision navigation, precision munitions,
and the timing synchronization
on which all secure communications depend.
Missile warning satellites
provide the first alert
of ballistic missile and hypersonic weapon launches.
Space domain awareness tracks
over 47,000 objects in orbit
to protect American and allied satellites.
Launch operations place
national security payloads into orbit.
Nuclear command, control, and communications
ensure that the nuclear deterrent
remains credible and survivable.
Intelligence and reconnaissance satellites
provide persistent global coverage.
Cyber and electronic warfare operators
defend space systems
from an expanding spectrum of threats.
Weather satellites inform operational planning.
And offensive and defensive space operators
prepare to fight and win
in a domain that every other branch depends upon.

These are not speculative future capabilities.
They are operational today.
Every precision-guided munition
that uses GPS guidance,
every secure satellite phone call
from a deployed unit,
every early warning of a missile launch,
and every satellite image
used to plan a military operation
depends on systems
that the Space Force operates,
defends, and sustains.

## Future Reading

- [U.S. Space Force Primer][research_csis_primer],
  a comprehensive overview by the Center for Strategic
  and International Studies Aerospace Security Project,
  covering the Space Force's history, organization,
  mission areas, and policy context.

- [United States Space Force][ref_ussf],
  the official Space Force website,
  including fact sheets on all major weapon systems,
  organizational units, and installations.

- [RAND Corporation Study on Air Force Officer Promotion][research_rand_fighter_culture],
  the research report documenting
  the dominance of fighter pilot culture
  in Air Force senior leadership
  and its effects on non-pilot career fields.

- [Rumsfeld Space Commission Report][research_rumsfeld_commission],
  the 2001 commission report
  that first warned of a potential "Space Pearl Harbor"
  and recommended organizational reforms
  for military space.

- [Space Warfighting: A Framework for Planners][research_warfighting_framework],
  the Space Force's 2025 doctrine document
  codifying offensive and defensive counter-space operations
  and establishing space superiority
  as the basis of American military power.

## References

- [Reference, Advanced Extremely High Frequency][ref_aehf]
- [Reference, Air Force Space Command][ref_afspc]
- [Reference, Army Ballistic Missile Agency][ref_abma]
- [Reference, Buckley Space Force Base][ref_buckley]
- [Reference, Cape Canaveral Space Force Station][ref_cape_canaveral]
- [Reference, Combat Forces Command][ref_cfc]
- [Reference, Defense Meteorological Satellite Program][ref_dmsp]
- [Reference, Department of the Air Force][ref_daf]
- [Reference, Department of the Navy][ref_don]
- [Reference, Geosynchronous Space Situational Awareness Program][ref_gssap]
- [Reference, Global Positioning System][ref_gps]
- [Reference, Milstar][ref_milstar]
- [Reference, National Defense Authorization Act FY2020][ref_ndaa_fy2020]
- [Reference, National Security Act of 1947][ref_nsa_1947]
- [Reference, National Security Space Launch][ref_nssl]
- [Reference, Next-Generation OPIR][ref_next_gen_opir]
- [Reference, Peterson Space Force Base][ref_peterson]
- [Reference, PLA Strategic Support Force][ref_pla_ssf]
- [Reference, Russian Space Forces][ref_russian_space_forces]
- [Reference, Schriever Space Force Base][ref_schriever]
- [Reference, Space-Based Infrared System][ref_sbirs]
- [Reference, Space Fence][ref_space_fence]
- [Reference, Space Policy Directive 4][ref_spd4]
- [Reference, Space Surveillance Network][ref_ssn]
- [Reference, Space Systems Command][ref_ssc]
- [Reference, Title 10 USC Section 9081][ref_10usc9081]
- [Reference, United States Air Force][ref_usaf]
- [Reference, United States Space Force][ref_ussf]
- [Reference, USSF Organization][ref_ussf_organization]
- [Reference, Vandenberg Space Force Base][ref_vandenberg]
- [Reference, Wideband Global SATCOM][ref_wgs]
- [Research, AFA Opposes Space Force][research_afa_opposition]
- [Research, Air Force Founding][ref_af_founding]
- [Research, CSIS U.S. Space Force Primer][research_csis_primer]
- [Research, DoD Executive Agent for Space][ref_dod_space]
- [Research, General Jay Raymond Biography][ref_raymond]
- [Research, RAND Fighter Pilot Culture Study][research_rand_fighter_culture]
- [Research, Rogers Warns Air Force][research_rogers_warning]
- [Research, Rumsfeld Commission Report][research_rumsfeld_commission]
- [Research, Space Corps Proposal][research_space_corps_proposal]
- [Research, Space Officer Promotion][research_space_promotion]
- [Research, Space Warfighting Framework][research_warfighting_framework]

[ref_abma]: https://en.wikipedia.org/wiki/Army_Ballistic_Missile_Agency
[ref_aehf]: https://en.wikipedia.org/wiki/Advanced_Extremely_High_Frequency
[ref_af_founding]: https://www.heritage.org/defense/commentary/how-the-air-force-got-its-start-72-years-ago
[ref_afspc]: https://en.wikipedia.org/wiki/Air_Force_Space_Command
[ref_10usc9081]: https://www.law.cornell.edu/uscode/text/10/9081
[ref_buckley]: https://en.wikipedia.org/wiki/Buckley_Space_Force_Base
[ref_cape_canaveral]: https://en.wikipedia.org/wiki/Cape_Canaveral_Space_Force_Station
[ref_cfc]: https://www.spaceforce.mil/News/Article-Display/Article/4337269/us-space-force-establishes-combat-forces-command-welcomes-new-fldcom-commander/
[ref_daf]: https://en.wikipedia.org/wiki/Department_of_the_Air_Force
[ref_dmsp]: https://en.wikipedia.org/wiki/Defense_Meteorological_Satellite_Program
[ref_dod_space]: https://www.dafhistory.af.mil/About-Us/Fact-Sheets/Display/Article/433549/air-force-space-command-usaf/
[ref_don]: https://en.wikipedia.org/wiki/United_States_Department_of_the_Navy
[ref_gps]: https://en.wikipedia.org/wiki/Global_Positioning_System
[ref_gssap]: https://en.wikipedia.org/wiki/Geosynchronous_Space_Situational_Awareness_Program
[ref_milstar]: https://en.wikipedia.org/wiki/Milstar
[ref_ndaa_fy2020]: https://en.wikipedia.org/wiki/National_Defense_Authorization_Act_for_Fiscal_Year_2020
[ref_next_gen_opir]: https://en.wikipedia.org/wiki/Next-Generation_Overhead_Persistent_Infrared
[ref_nsa_1947]: https://en.wikipedia.org/wiki/National_Security_Act_of_1947
[ref_nssl]: https://en.wikipedia.org/wiki/National_Security_Space_Launch
[ref_peterson]: https://en.wikipedia.org/wiki/Peterson_Space_Force_Base
[ref_pla_ssf]: https://en.wikipedia.org/wiki/People%27s_Liberation_Army_Strategic_Support_Force
[ref_raymond]: https://en.wikipedia.org/wiki/John_W._Raymond
[ref_russian_space_forces]: https://en.wikipedia.org/wiki/Russian_Space_Forces
[ref_sbirs]: https://en.wikipedia.org/wiki/Space-Based_Infrared_System
[ref_schriever]: https://en.wikipedia.org/wiki/Schriever_Space_Force_Base
[ref_space_fence]: https://en.wikipedia.org/wiki/Space_Fence
[ref_spd4]: https://trumpwhitehouse.archives.gov/presidential-actions/text-space-policy-directive-4-establishment-united-states-space-force/
[ref_ssn]: https://en.wikipedia.org/wiki/United_States_Space_Surveillance_Network
[ref_ssc]: https://en.wikipedia.org/wiki/Space_Systems_Command
[ref_usaf]: https://en.wikipedia.org/wiki/United_States_Air_Force
[ref_ussf]: https://en.wikipedia.org/wiki/United_States_Space_Force
[ref_ussf_organization]: https://www.spaceforce.mil/About-Us/About-Space-Force/Space-Force-Organization/
[ref_vandenberg]: https://en.wikipedia.org/wiki/Vandenberg_Space_Force_Base
[ref_wgs]: https://en.wikipedia.org/wiki/Wideband_Global_SATCOM
[research_afa_opposition]: https://spacenews.com/air-force-association-opposes-establishment-of-a-space-force-says-air-and-space-are-indivisible/
[research_csis_primer]: https://aerospace.csis.org/us-space-force-primer/
[research_rand_fighter_culture]: https://www.rand.org/pubs/research_reports/RR1936.html
[research_rogers_warning]: https://spacepolicyonline.com/news/rogers-warns-air-force-not-to-resist-space-corps-proposal/
[research_rumsfeld_commission]: https://spp.fas.org/military/commission/report.htm
[research_space_corps_proposal]: https://spacenews.com/house-armed-services-committee-votes-to-create-a-u-s-space-corps/
[research_space_promotion]: https://spacenews.com/space-officers-could-have-a-better-chance-of-promotion-under-new-proposed-guidelines/
[research_warfighting_framework]: https://www.airandspaceforces.com/new-doc-spells-out-how-ussf-will-use-space-control-to-gain-space-superiority/
