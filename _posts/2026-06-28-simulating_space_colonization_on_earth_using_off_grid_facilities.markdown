---
layout: post
mathjax: true
comments: true
title:  "Simulating Space Colonization on Earth Using Off-Grid Facilities"
date:   2026-06-28 09:00:00 +0000
categories: aerospace engineering space-studies analog-facilities
series: off_grid_space_analogs
series_title: Off-Grid Space Colonization Analogs
series_index: 1
---
<!-- A152 -->
<script>console.log("A152");</script>

A space colony,
in the working sense of the term,
is a permanent or long-duration crewed installation
that depends for its survival
on infrastructure
it carries with it
or produces locally.
Sending one
to the lunar surface
or to Mars
is expensive,
slow,
and difficult to iterate.
The lead time
between a design choice
and the operational consequence of that choice
is measured
in years
and in billions of dollars.
A terrestrial analog facility,
operated under the constraint
of importing nothing
the colony would not have access to off Earth,
shortens the lead time
to months
and the cost
to the price of a research station.
The analog
is the iteration engine
that the actual mission
cannot afford to be.

This article
treats the terrestrial off-grid analog
as a problem in its own right.
It surveys
the prior attempts
that the public record documents,
the criteria
that govern site selection
for new attempts,
the facility-system stack
that any candidate analog
must implement,
and the distinction
between the bootstrap colony,
which carries everything in
and produces everything locally,
and the expansion colony,
which leans on
existing planetary infrastructure
while it grows.
The intent
is to present the problem
in enough breadth
that subsequent articles
can treat each subsystem
in depth.

The framing
borrows from the
[introduction to space studies][related_post_space_studies]
that opened the space-themed cluster
on this blog
and the
[cryptotelemeritocracy for space exploitation][related_post_crypto_space]
article
that treats the governance side
of the same long-horizon problem.
This article
addresses the engineering and operations side.

## The Simulation Honesty Problem

A terrestrial analog
is useful
in proportion to how honestly
it constrains itself
to the resources
the real mission would have.
The dishonest analog
imports food, water, power, replacement parts,
and crew rotation
from the surrounding terrestrial economy
while reporting outcomes
as if it were closed.
The honest analog
draws a clear envelope
around what the simulation includes
and accounts explicitly
for what crosses the envelope.

A small set of axes
distinguishes a credible analog
from a recreational one.
The first axis
is closure.
A fully closed analog
recycles air, water, and biomass
inside the envelope
and accepts mass through the envelope
only on the schedule
the simulated mission would impose.
A partially closed analog
accepts external supply
on a documented cadence
and reports the dependence
as part of the result.
The second axis
is isolation.
A high-isolation analog
restricts crew communication
with the outside
to a delay and bandwidth
matching the simulated mission,
restricts physical egress
to the schedule
the simulated mission would allow,
and operates
under the local environmental hazards
the chosen site presents.
A low-isolation analog
accepts deviation from these constraints
where the research question
does not require them.
The third axis
is duration.
A six-month analog
exercises subsystems
the two-week analog does not,
and a multi-year analog
exercises subsystems
the six-month analog does not.
The fourth axis
is the fidelity
of the local environment
to the target environment.
A pressurised desert habitat
exercises some of the
problems a Mars surface habitat
will face
but not the problems
that low pressure,
ionising radiation,
and reduced gravity
will produce.

Every analog
operates somewhere
on each of these axes.
The honest analog
documents where it sits
and what conclusions
its position licenses.

The closure axis
admits a quantitative expression.
Let $m_{ext}$ denote
the total mass
crossing the envelope
from outside the analog
into the analog
over a mission
and $m_{tot}$ denote
the total mass demand
the analog satisfies
over the same mission.
The closure ratio is

$$ C = 1 - \frac{m_{ext}}{m_{tot}} $$

with $C = 1$ corresponding
to a fully closed analog
and $C = 0$ corresponding
to an analog
supplied entirely
from outside the envelope.
Subsystem-specific closure ratios
are usually more informative
than a single facility-wide value.
The International Space Station
Water Recovery System
operates at approximately
$C \approx 0.98$
for water alone.
The Biosphere 2 first mission
operated at approximately
$C \approx 0.5$
for food calories
across the two-year duration.
Subsystem-specific reporting
is the honest standard.

## Survey of Prior Attempts

The terrestrial analog tradition
predates the space programme
in the form of polar exploration
and submarine operations,
each of which already
solved a version
of the long-duration closed-quarters problem
the space colony will face.
The space-specific analog tradition
runs from the 1960s
through the present
across a handful of major sites.

### Antarctic Stations as Persistent Analogs

[McMurdo Station][ref_mcmurdo]
on Ross Island
in the Antarctic
is the largest United States Antarctic Program facility,
operated by the
[National Science Foundation][ref_nsf_usap]
since 1956.
McMurdo functions
as a logistic hub
for the deeper continental stations
and supports
roughly a thousand personnel
in the austral summer
and roughly two hundred and fifty
in the austral winter.
Its winter-over crew
operates
under physical isolation
of approximately six months
between resupply opportunities,
which makes it
a long-duration analog
for any mission
where the egress option is not present.

[Amundsen-Scott South Pole Station][ref_amundsen_scott]
is the deeper analog.
A winter-over crew
of approximately forty-five personnel
operates
through the austral winter
without resupply
or transport in or out,
under temperatures
that can fall below
minus eighty degrees Celsius.
The station
sits on a moving ice sheet
that has required
periodic replacement
of the structure
since the original 1956 build,
with the current elevated station
opened in 2008.

[Concordia Station][ref_concordia]
at Dome C
on the Antarctic plateau
is the European analog.
It is jointly operated
by the French
[Polar Institute Paul-Emile Victor][ref_ipev]
and the Italian
[National Antarctic Research Programme][ref_pnra]
with the
[European Space Agency][ref_esa_concordia]
participating
in a long-running research collaboration
on isolation,
confinement,
and human physiology
at altitude.
Its winter-over crew
of approximately thirteen
operates
under nine months of physical isolation
at an effective altitude
above three thousand metres
where the partial pressure of oxygen
is comparable
to a habitat at four thousand metres
elsewhere.
ESA treats Concordia
as its principal Earth-based analog
for long-duration deep-space missions.

The Antarctic stations
share a property
that distinguishes them
from the purpose-built space analogs.
They exist
because national science programmes
need them for science
that requires the location,
not because anyone is simulating Mars.
The crew has a real job
that does not depend on the analog framing,
which yields
a different kind of behavioural data
from a facility
where the simulation is the only purpose.

### Closed Ecological System Experiments

[BIOS-3][ref_bios_3]
at the
[Institute of Biophysics][ref_ibp_krasnoyarsk]
in Krasnoyarsk
operated
from 1972,
with construction begun in 1965,
under the Soviet
and then Russian programme
on closed ecological life support.
Multiple crewed runs
of two to three persons
demonstrated
closed-loop air and water recycling
with food
partially supplied
by intensive cultivation
of wheat and chlorella inside the envelope.
BIOS-3
is the oldest closed ecological system project
that the public record documents,
with present operational status
uncertain in the published record
after the resumed cooperation with ESA
in the mid-2000s.

[Biosphere 2][ref_biosphere_2]
near Oracle, Arizona,
is the largest closed ecological system
constructed at the time of its build.
It enclosed
approximately twelve and a half thousand square metres
of footprint
under glass
across seven biomes
and operated
two crewed missions.
The first
ran from September 1991
to September 1993
with eight crew
across two years.
The second
ran for six months in 1994
with seven crew.
The first mission
encountered a slow decline
in atmospheric oxygen
to approximately fourteen percent
that required external supplementation,
attributed
to faster-than-expected uptake
by the soils
and the concrete
inside the envelope.
The facility transferred
to Columbia University
for atmospheric carbon research
from 1995 through 2003
and to the
[University of Arizona][ref_arizona_biosphere]
under research operations
beginning in 2007
and full ownership
effective July 2011,
where it operates today
as an open research site.

The
[Yuegong-1 facility][ref_yuegong]
at Beihang University in Beijing
is the modern Chinese closed ecological system.
The longest sealed run,
Yuegong-365,
ran from May 2017
to May 2018
with crew rotations across three hundred and seventy days,
demonstrating
sustained closed-loop air, water,
and a partial food cycle
with wheat, soybeans, peanuts,
and yellow mealworm protein
inside the envelope.

The
[Micro-Ecological Life Support System Alternative][ref_melissa]
or MELiSSA programme
at the European Space Agency
has run since 1989
on the engineering
of a closed-loop life support system
suitable for crewed deep-space missions,
with the MELiSSA Pilot Plant
at the Universitat Autonoma de Barcelona
testing the components
that the eventual flight system
would require.
MELiSSA
is engineering research
rather than a long-duration crewed analog,
but it is the closed-loop subsystem source
for several other programmes.

### Mars Surface Analogs

The
[Mars Desert Research Station][ref_mdrs]
near Hanksville, Utah,
has operated
since 2001
under the
[Mars Society][ref_mars_society]
as a Mars surface analog
in high desert terrain.
Crews of six
rotate through two-week missions
that exercise extravehicular activity procedures
in pressure suits,
science operations
in mock-up labs,
and small-vehicle traverse.
Hanksville
is selected for its
geological similarity to Mars,
its remoteness from urban infrastructure,
and its accessibility
for resupply.

The
[Flashline Mars Arctic Research Station][ref_fmars]
on Devon Island in Nunavut, Canada,
is the higher-fidelity sibling.
Devon Island
sits inside a polar desert
inside the Haughton impact crater,
which produces
a terrain
that resembles Mars
in geology, climate, and isolation
to a degree
that the continental United States desert sites cannot.
The
[NASA Haughton Mars Project][ref_haughton_mars]
has used Devon Island
for science operations and EVA research
in collaboration with the Mars Society
for over twenty years.

The
[Hawaii Space Exploration Analog and Simulation][ref_hi_seas]
facility
on the flank of Mauna Loa
at approximately two thousand five hundred metres
operated under the
[University of Hawaii][ref_hi_seas_uh]
from 2013
with funding from
the National Aeronautics and Space Administration
for a sequence of missions
that ran four months,
eight months,
and twelve months.
The twelve-month HI-SEAS IV mission
in 2015 and 2016
is the longest United States Mars analog
on the public record.
The facility transferred
to private operation
under the
[International MoonBase Alliance][ref_imba]
in 2018
and shifted
toward lunar analog missions.

The NASA
[Human Exploration Research Analog][ref_hera]
or HERA
at Johnson Space Center
is the sealed habitat analog
that NASA operates
internally
for crew behavioural research.
Missions run forty-five days
with four-person crews
under simulated communication delay
for the latter portion of the mission.
HERA
does not simulate
the surface environment,
the radiation environment,
or the partial-gravity environment.
It simulates
the isolation and confinement
that any deep-space mission would impose
on the crew.

The
[Crew Health and Performance Exploration Analog][ref_chapea]
or CHAPEA
is the long-duration extension of HERA
at Johnson Space Center.
The Mars Dune Alpha habitat
that hosts CHAPEA missions
is a three-dimensional-printed structure
constructed
by [ICON Technology][ref_icon]
under contract to NASA
in 2021 and 2022.
The first CHAPEA mission
ran from June 2023
to July 2024
with four crew
across three hundred and seventy-eight days,
which is the longest
NASA-operated terrestrial Mars analog
on the record.
A second mission
was scheduled to begin in 2025.

[Mars-500][ref_mars_500]
at the
[Institute of Biomedical Problems][ref_ibmp]
in Moscow
is the Russian long-duration sealed analog.
The flagship five-hundred-and-twenty-day mission
ran from June 2010
to November 2011
with a crew of six
including European and Chinese participants.
Mars-500
simulated
the round-trip transit
and a Mars-surface segment
in a sealed module
at the institute,
with no surface analog component
beyond the simulated EVA inside the chamber.

### Underwater Analogs

The
[NASA Extreme Environment Mission Operations][ref_neemo]
programme,
known as NEEMO,
used the
[Aquarius Reef Base][ref_aquarius]
at the Florida Keys
from 2001
through the most recent announced mission
in 2019,
with no further missions
on the public record,
for crewed runs
of approximately one to two weeks
under saturation diving conditions.
Aquarius
sits at a depth
of approximately eighteen metres
on the seafloor,
and the saturation-dived crew
cannot return to the surface
on demand
without a decompression cycle.
The mission constraint
of immediate egress denial
is closer
to the space mission constraint
than the desert analogs
provide.
Aquarius
is operated by
[Florida International University][ref_fiu_aquarius]
under transfer from the
[National Oceanic and Atmospheric Administration][ref_noaa],
with operational control passing in 2013
and full ownership in 2014.

### Buoyant and Atmospheric Platform Analogs

The terrestrial analog tradition
has concentrated
on facilities
that sit on the ground
or under the sea.
A category of target environment
that this tradition
has not yet built a credible analog for
is the buoyant habitat
suspended in the atmosphere
of another planet.
The
[Venus colonization paper][ref_landis_venus]
that
Geoffrey Landis
of the NASA Glenn Research Center
published in 2003
proposed
a permanent crewed presence
in the Venus upper atmosphere
at approximately fifty to sixty kilometres altitude.
The NASA Langley
[High Altitude Venus Operational Concept][ref_havoc]
study,
published in 2014 and 2015,
formalised
a mission architecture
that builds on
the same physical principle.

The principle
is straightforward.
A habitat
filled with breathing air,
an oxygen and nitrogen mixture
of mean molecular mass
approximately twenty-nine grams per mole,
is buoyant
in the Venus carbon dioxide atmosphere
of mean molecular mass
approximately forty-four grams per mole.
The density ratio

$$ \frac{\rho_{habitat}}{\rho_{atmosphere}} \approx \frac{29}{44} \approx 0.66 $$

provides lift
comparable in fraction
to a helium balloon
on Earth.
At the chosen altitude band,
the temperature
is approximately
zero to seventy degrees Celsius,
the pressure
is approximately
half to one Earth atmosphere,
and the surface gravity
is approximately
ninety percent Earth normal.
Of all candidate human destinations
in the inner solar system
outside Earth,
the Venus cloudtop
offers
the gentlest combination
of pressure,
temperature,
and gravity
on the human envelope.

The terrestrial analog inventory
contains no dedicated Venus cloudtop simulator.
The closest available platform
is the high-altitude pseudo-satellite community
that operates
stratospheric airships and balloons
at approximately twenty to thirty kilometres altitude
in the Earth atmosphere.
The
[World View Stratollite programme][ref_world_view]
and the dormant
[Loon programme][ref_loon]
that ran from 2013 to 2021
under Alphabet
operated stratospheric balloon platforms
for long-duration uncrewed station-keeping.
The
[Sceye programme][ref_sceye]
operates
stratospheric airship platforms
under similar constraints.
None of these vehicles
carry crew
or implement
a closed life support system.
A credible Venus cloudtop analog
would require
a crewed stratospheric airship
of substantial volume
operating for weeks to months at altitude
under a closed life support constraint
that no contemporary programme
is funded to build.
The absence
is one of the major gaps
in the analog tradition
that this article surveys.

### Comparison of Prior Attempts

| Facility | Site | Operator | Longest Crewed Run | Closure | Isolation | Year |
|---|---|---|---|---|---|---|
| BIOS-3 | Krasnoyarsk, Russia | Institute of Biophysics | ~6 months | High | Moderate | 1972+ |
| Biosphere 2 | Oracle, Arizona | University of Arizona | 24 months | High | Low | 1991+ |
| Mars Desert Research Station | Hanksville, Utah | Mars Society | ~2 weeks per crew | Low | High | 2001+ |
| Flashline Mars Arctic Station | Devon Island, Nunavut | Mars Society | ~1 month per crew | Low | High | 2000+ |
| Concordia | Dome C, Antarctica | IPEV, PNRA, ESA | 9 months winter-over | Low | High | 2005+ |
| McMurdo | Ross Island, Antarctica | NSF | 6 months winter-over | Low | High | 1956+ |
| Amundsen-Scott | South Pole, Antarctica | NSF | 9 months winter-over | Low | Very High | 1956+ |
| HI-SEAS | Mauna Loa, Hawaii | University of Hawaii, IMBA | 12 months | Moderate | High | 2013+ |
| HERA | Houston, Texas | NASA | 45 days | High | High | 2014+ |
| Mars-500 | Moscow, Russia | IBMP | 520 days | High | High | 2010-2011 |
| Yuegong-1 | Beijing, China | Beihang University | 370 days | High | High | 2014+ |
| CHAPEA | Houston, Texas | NASA | 378 days | High | High | 2023+ |
| Aquarius (NEEMO) | Florida Keys, USA | FIU | ~2 weeks per crew | Low | High | 2001-2019 |

The pattern
that emerges
across the table
is that no single facility
exercises every axis simultaneously.
A facility
with high closure
typically scores lower on isolation
because the closure infrastructure
sits inside a research campus.
A facility
with high isolation
typically scores lower on closure
because the cost
of building closed ecological systems
in the chosen remote location
is prohibitive.
The honest analog programme
combines results
across facilities
rather than asking
any single facility
to do the whole job.

## Site Selection

A new off-grid analog facility
selects its site
against a set of criteria
that the operational mission
imposes on it.
The criteria
are not all reducible
to a single ordering,
which means
site selection
is a trade study,
not a ranking.

The first criterion
is terrain analogy
to the target environment.
A lunar analog
prefers a site
with low organic content,
basaltic rock,
fine regolith,
and limited vegetation.
A Mars analog
prefers
a site with iron-rich soil,
limited water,
geomorphology resembling
the Martian surface,
and either
high altitude
or thin atmosphere
or both.

The second criterion
is environmental hazard fidelity.
A site
with low temperature,
high winds,
fine dust,
or moderate radiation
exercises subsystems
that a benign site
does not.
A site
where the egress option
is naturally constrained
by terrain or weather
produces
a different operational behaviour
than a site
where the crew can drive out
in an hour.

The third criterion
is isolation
from terrestrial infrastructure.
A site
within a one-hour resupply radius
of a major city
allows
behavioural-isolation simulation
but not
logistic-isolation simulation.
A site
days from the nearest road
constrains the logistic envelope
to something
closer to the real mission.

The fourth criterion
is regulatory and land-tenure feasibility.
A site
on land controlled
by a cooperating agency
or institution
is operable.
A site
on land
whose use rights
are unclear
or contested
is not.

The fifth criterion
is the operational supply chain
that the host country
can deliver to the site.
The cost
of bringing
people, parts, fuel,
and consumables
to the chosen location
sets the floor
on the cost per crewed day.

### United States Sites

The continental United States
offers a small set
of credible analog sites.
The
[Mojave Desert][ref_mojave]
in California and Nevada
combines
low population density,
arid climate,
fine soils,
and existing aerospace infrastructure
through the
[Edwards Air Force Base][ref_edwards]
and Mojave Air and Space Port complex
that supports related work.
The Mojave
lacks the geomorphology
of Mars
and the polar isolation
of Devon Island
but provides
an accessible site
for short-duration analogs.

The
[Great Basin Desert][ref_great_basin]
in Nevada and Utah
provides
a higher-altitude alternative
with greater isolation
than the Mojave
and a longer drive
from the nearest major airport.
The Hanksville area
that hosts MDRS
sits in the Great Basin.

The
[Sonoran Desert][ref_sonoran]
in Arizona
hosts the Biosphere 2 site
and provides
the moderate climate
that the closed-system experiments
preferred.

The
[Mauna Loa][ref_mauna_loa]
and
[Mauna Kea][ref_mauna_kea]
flanks on the island of Hawaii
provide
volcanic regolith analog
and high altitude
to a degree
the continental United States
cannot match.
The HI-SEAS site
on Mauna Loa
is the canonical example.

The
[Alaska Brooks Range][ref_brooks]
and the broader Alaska arctic
provide
the polar desert analog
inside United States territory,
though
the science infrastructure
to support an analog facility
there
is thinner
than the Antarctic.

### International Sites

The
[Atacama Desert][ref_atacama]
in northern Chile
is the canonical Mars-analog site
outside North America.
The combination
of high altitude,
low precipitation,
fine soils,
and biological sparsity
has supported
multiple analog deployments,
including the
[NASA Atacama Rover Astrobiology Drilling Studies][ref_arads]
or ARADS campaign.

[Devon Island][ref_devon]
in Nunavut, Canada,
is the canonical Mars-analog site
in North America
outside the continental United States.
The Haughton impact crater
provides the geological analog,
and the polar desert climate
provides the environmental analog.
Devon Island
hosts the Flashline Mars Arctic Research Station
and the broader Haughton Mars Project.

The
[Pilbara region][ref_pilbara]
of Western Australia
provides
the early-Earth geological analog
that astrobiology research
on Mars
relies upon.
Stromatolites in the Pilbara
date to approximately three and a half billion years ago
and are used
as comparators
for the geological record
that a Mars mission
might encounter.

[Iceland][ref_iceland]
provides
volcanic terrain
that the Apollo astronaut programme
used
for field geology training
in 1965 and 1967
and that the
[Artemis II programme][ref_artemis_iceland]
returned to
in 2024
for lunar geology training.
The European Space Agency
[Planetary Analogue Geological and Astrobiological Exercise for Astronauts][ref_pangaea]
or PANGAEA training programme
operates
across the Lanzarote volcanic terrain
in the Canary Islands,
the Italian Dolomites,
and the Ries impact crater in Germany.

The Antarctic continent
provides
the canonical isolation analog
through the existing
Antarctic Treaty system stations.
Concordia, McMurdo, Amundsen-Scott,
and the Russian Vostok station
each operate
under conditions
no other terrestrial site
can match.

The
[Tibetan Plateau][ref_tibet]
and the
[Pamir Mountains][ref_pamir]
provide
high-altitude long-duration sites
that have been used
for biomedical research
rather than dedicated space analogs
to date.

## The Facility-System Stack

A space-colonization analog
implements the same
subsystem stack
that the real colony
will implement.
The honest analog
makes the implementation
visible
so that the simulated outcome
is traceable
to the simulated input.

### Electricity and Energy Storage

The off-grid analog
generates its own electricity
from sources
that the chosen site supports.
Photovoltaic generation
with battery storage
is the standard primary source
for the southwestern United States sites
and works
at the desert latitudes
where the analog tradition concentrates.
Wind generation
is the standard supplement
where the site provides it.
McMurdo Station
operates the
[Ross Island Wind Energy Project][ref_ross_island_wind]
with three Enercon E33 turbines
that supply
approximately ten percent of station load
in average conditions.
Diesel or propane generators
provide
the redundancy
that the photovoltaic and wind sources
cannot guarantee
through extended overcast
or low-wind periods.

The long-horizon question
that the analog can ask
is what fraction
of total load
the on-site generation supports
under realistic seasonal variation
and what storage capacity
the facility needs
to bridge
the worst case.
A facility
that imports diesel by truck
weekly
is reporting
on its diesel supply chain
as much as
on its photovoltaic build.

Small modular nuclear reactors
are absent
from the current analog inventory
but appear
in the forward-looking lunar and Mars architecture
through projects like the
[NASA Kilopower][ref_kilopower]
and successor
fission surface power efforts.
A current analog
that wanted to exercise
a nuclear primary
would face
regulatory and supply chain barriers
that the photovoltaic primary
does not.

### Electronic Operations and Computing

The analog
needs
local compute,
local data storage,
local display and human interface,
and the network infrastructure
that connects them.
The hard problem
that the analog reproduces
is computational autonomy
under degraded or absent
connection to outside services.
The mission system
runs locally
or it does not run.
Critical workloads
that depend on cloud services
fail
when the network falls below
the round-trip time
the simulation imposes.

Power-aware computing
matters
because the analog electricity budget
is finite.
Server-class hardware
running continuously
imposes a load
that the photovoltaic build
must size for.
Edge compute,
local caching,
and aggressive sleep modes
are the standard mitigations.

### Communications

The analog
operates under
a communications constraint
that matches
the simulated mission.
The one-way light-time delay
between two points
separated by distance $d$
is

$$ \tau = \frac{d}{c} $$

where $c$
is the speed of light.
For Mars,
with the Earth-Mars distance varying
from approximately
$5.6 \times 10^{10}$ metres
at opposition
to approximately
$4.0 \times 10^{11}$ metres
at conjunction,
$\tau$ varies
from approximately three minutes
to approximately twenty-two minutes.
For the Moon,
with $d \approx 3.8 \times 10^{8}$ metres,
$\tau \approx 1.3$ seconds.
A Mars analog
imposes the Mars-scale delay
on crew-to-Earth traffic.
A lunar analog
imposes the lunar-scale delay.
A near-Earth analog
imposes none.
The bandwidth constraint
that the simulated link
provides
is enforced
by the analog
through queue and throttle
on the local network
even when
the physical link
to the surrounding terrestrial network
is broadband.

Satellite internet
through
[Starlink][ref_starlink]
and the
[Iridium constellation][ref_iridium]
provides
the physical link
at most analog sites
where terrestrial internet
is absent.
The same constellations
support
the field camps,
science stations,
and emergency operations
that the analog
shares infrastructure with.
The
[Antarctic Starlink rollout][ref_antarctic_starlink]
at McMurdo
and other stations
has shifted
the practical communications regime
for the polar analog community
substantially
since 2022.

### Food Production

Food is the longest-cycle
closed-loop subsystem
the analog implements.
A two-week mission
can carry shelf-stable rations
without exercising
the food production system at all.
A six-month mission
exercises
the storage and preparation system
but not the production system.
A two-year mission
exercises
the production system.
Biosphere 2's first mission
produced
approximately fifty percent
of crew calories
from intensive horticulture
inside the envelope,
which made
the food system
the dominant labour load
on the crew
through the mission.

The food production strategies
that the analog tradition uses
include
intensive horticulture
in soil or hydroponics,
aeroponics for water efficiency,
controlled-environment agriculture under light-emitting diode arrays,
aquaculture for protein,
single-cell protein from algae,
and edible insect production.
Each approach
imposes
distinct demands
on water, electricity,
labour, and consumables.
The MELiSSA programme
and the Lunar Palace facility
have published
detailed measurements
on closed-loop food production
at the experimental scale.

### Potable Water

Water
recovery
is the highest-leverage subsystem
in any space mission.
The International Space Station
[Water Recovery System][ref_iss_wrs]
recovers
approximately ninety-eight percent
of crew water
across urine, condensate,
and other sources
following the addition
of the Brine Processor Assembly
that the 2023 milestone documented.
The analog
can match
this recovery rate
or report
the achieved rate
against the standard.

The analog
sources water
from
on-site wells,
atmospheric water generation,
rainwater capture,
or trucked-in supply.
Each source
has a fidelity argument
to the simulated mission.
On-site wells
correspond
to a Mars colony
that extracts subsurface ice.
Atmospheric water generation
corresponds
to a Mars colony
that condenses water
from the thin atmosphere
at high cost
in electricity.
Rainwater capture
corresponds
to no expected Mars colony case
but to lunar polar ice extraction
under permanent shadow conditions.
Trucked-in supply
corresponds
to a colony
on the resupply schedule
that the Mars opposition cycle
or the lunar logistics schedule
would impose.

### Sewage and Human Waste

The analog
treats human waste
through one
of a small set of pathways.
Composting toilets
with secondary processing
match
the closed-loop logic
that the long-duration mission
requires
and produce
soil amendment
that the food production loop
can use.
The vacuum toilet
that the International Space Station uses
is the high-fidelity reference
for the closed analog
and routes
liquid and solid streams
into separate processing.
A membrane bioreactor
with downstream disinfection
produces
non-potable water
for greywater use
without solids handling
inside the crew envelope.
A septic system
with leach field
is the local terrestrial standard
that the dishonest analog defaults to
but that no space colony
will have access to.

The fidelity gradient
is clear.
The composting toilet
is the long-duration honest choice.
The septic field
is the convenient terrestrial cheat.

### Physical Operations and Habitat

The habitat structure
is the most visible subsystem
of the analog
and the one
where appearance and substance
diverge most.
A Mars analog
that uses
an aluminium construction trailer
exercises
the interior subsystems
but does not exercise
the pressure vessel envelope
that the real colony will use.
A lunar analog
that uses
a three-dimensional-printed
or rammed-earth structure
exercises
the construction process
that the real colony might use
if the construction process
is the research subject.

The
Mars Dune Alpha habitat
at NASA Johnson Space Center
is the highest-profile
three-dimensional-printed analog habitat
currently operating.
The
[NASA 3D-Printed Habitat Challenge][ref_3d_habitat_challenge]
that ran from 2015 to 2019
funded
the development of several precursor designs
through ICON and other contractors.
The Mars Society
and the Concordia consortium
have used
more conventional construction
for their habitats
because the construction process
is not the research subject.

Airlocks
are the high-fidelity option
for an analog
that wants to simulate
the donning and doffing
of pressure suits
and the constraint
on egress frequency.
A two-stage airlock
with realistic cycle time
and consumable accounting
imposes a behavioural cost
on the crew
that an unlocked door does not.

Pressure suits or mock-ups
for extravehicular activity simulation
are standard
across the Mars analog tradition.
MDRS, FMARS, HI-SEAS, and CHAPEA
all run
mock-EVA protocols
under pressure-suit analogs
that do not pressurise
but that constrain
visual field, glove dexterity,
and communication
to the levels
the real suit imposes.

### Garbage and Waste Disposal

Solid waste
that is not human waste
and is not consumable packaging
accumulates
in the analog
and requires
a documented disposition.
The honest analog
sorts waste
into categories
that match
the real-mission disposition options.
The realistic options
for a Mars colony
are local storage,
incineration with energy recovery,
mechanical recycling,
chemical recycling,
or material reuse
inside the colony envelope.
The earthbound default
of curbside pickup
corresponds to no mission case.

The analog
that incinerates waste
on site
exercises
the air filtration subsystem
that the incinerator load imposes
and the
ash disposition workflow
that follows.
The analog
that recycles plastic
on site
exercises
the energy budget
and the equipment maintenance burden
that small-scale recycling imposes.
The analog
that stores waste
on site
for the duration of the mission
exercises
the volume accounting
that real missions
take seriously.

### Transportation and Roads

The analog
implements
internal transport
through small vehicles
that match
the operational profile
of the simulated mission.
Pressurised rover analogs
exist
at the Mars Society sites
and at the NASA analog programmes
but are uncommon
because the cost is prohibitive
relative to the research yield.
Unpressurised utility vehicles
substitute
for the EVA scenarios
where the simulation
does not require pressure-vessel fidelity.

Roads
to the analog site
are the dishonest fallback.
A Mars colony
will not have
paved roads
to a port.
A lunar colony
will have
graded berms
rather than roads.
An analog
that depends
on a paved access road
for routine resupply
is reporting
on its terrestrial logistics
rather than
on its colonial logistics.
The analog programmes
that take this seriously
deliberately
locate themselves
at the end of a long unpaved track
or at the end of an air-only access route,
which is the operational reason
Devon Island,
Concordia,
and the Antarctic continental stations
are credible analogs
in a way
the suburban-fringe analogs
are not.

## Bootstrap and Expansion

The analog tradition
distinguishes
two operational regimes
that any space colony will pass through
in sequence.
The first
is the bootstrap regime,
in which
the colony must produce
or pre-position
everything it needs
because no terrestrial-equivalent infrastructure
is available
within reach.
The second
is the expansion regime,
in which
the colony has reached
a size and a maturity
that allows it to rely
on a developing planetary infrastructure
for some inputs
while it continues to grow.

A bootstrap-regime analog
implements
the full subsystem stack
under the constraint
that nothing crosses
the envelope
on demand.
A six-month bootstrap analog
that runs out of food
runs out of food.
The crew
does not order pizza.
The bootstrap analog
is the hardest to operate
and the closest
to the early-mission case.
Biosphere 2's first mission
and the Mars-500 sealed run
sit closest
to this regime
inside the analog tradition,
both
with documented limits
on what crossed the envelope
during the mission.

An expansion-regime analog
implements
the same subsystem stack
but accepts
documented external supply
on the schedule
the simulated mission would impose.
The Mars resupply schedule
is set by
the Mars synodic period

$$ T_{syn} = \frac{1}{\left|\,\dfrac{1}{T_E} - \dfrac{1}{T_M}\,\right|} \approx 780 \text{ days} $$

where $T_E \approx 365.25$ days
is the Earth sidereal period
and $T_M \approx 686.97$ days
is the Mars sidereal period.
A Mars colony
on the practical resupply cadence
receives mass
approximately every twenty-six months,
which the expansion-regime analog
can simulate
through a corresponding gap
between supply events
at the analog site.
A lunar colony
on the practical resupply cadence
receives mass
on a schedule
the operating cadence
of the launch provider
controls,
which is months to weeks
rather than years.
A McMurdo-scale analog
that resupplies
on the austral summer flight schedule
exercises
the resupply logistics
that an established lunar base
would face.
The expansion-regime analog
is more operable
than the bootstrap-regime analog
and supports
longer research campaigns
because the failure modes
do not threaten
the crew.

A serious analog programme
runs both regimes
in sequence
across a multi-year campaign.
The bootstrap regime
exercises
the early-colony failure modes.
The expansion regime
exercises
the established-colony failure modes.
A programme
that only runs
the expansion regime
is reporting
on logistics
rather than colonial autonomy.
A programme
that only runs
the bootstrap regime
will not produce
data
that an established colony
can use.

## Out of Scope

This article
is the introduction to a problem
that subsequent articles
will treat
in depth.
A range of topics
that the introduction
necessarily sets aside
deserve mention
so the reader recognises
where additional research is needed.

**Per-subsystem engineering.**
The facility-system stack
that this article surveys
contains
nine subsystems
each of which
admits
an article on its engineering.
The electricity subsystem alone
spans
generation technology selection,
storage chemistry selection,
demand modelling,
seasonal sizing,
and reliability engineering.
The water subsystem
spans
recovery process design,
microbial control,
material compatibility,
and the regulatory chemistry
that the recovered water
must satisfy.
Each subsystem
will be treated separately
in future articles.

**Crew selection, training, and behavioural research.**
The behavioural research
that the analog tradition
funds and conducts
is the principal research subject
of the major analog programmes.
The crew selection process
that filters applicants
into a mission roster
is itself
a research subject.
This article
does not treat
either topic
beyond the framing
that the analog provides.

**Closed ecological system biology.**
The biology
of a closed ecological system
that supports a crew
across multiple years
is an active research subject
that
the BIOS-3, Biosphere 2, MELiSSA,
and Yuegong programmes
have advanced
without reaching closure.
The biology
deserves a dedicated treatment
that this article
does not attempt.

**Pressure suit and extravehicular activity research.**
The pressure suit
that the real mission will use
is the principal interface
between the crew
and the surface environment.
The analog tradition
substitutes mock-ups
that exercise
some of the behavioural constraint
without exercising
the engineering constraint.
The engineering side
deserves
a dedicated treatment.

**Radiation environment.**
The radiation environment
on the lunar surface
and the Martian surface
is a principal hazard
the analog cannot reproduce.
The analog tradition
addresses radiation
through co-located research
at neutron beam facilities
or particle accelerator sites
rather than through the analog itself.
This article
does not treat
the radiation problem.

**Reduced gravity.**
The reduced-gravity environment
on the lunar surface
and the Martian surface
is the second principal hazard
the analog cannot reproduce.
Parabolic flight,
neutral buoyancy,
and bedrest immobilisation
are the partial substitutes
that the analog tradition uses.
This article
does not treat
the gravity problem.

**Programme cost and funding model.**
The cost
of operating
a space-colonization analog
ranges from
the hobbyist budget
of the Mars Desert Research Station
to the institutional budget
of CHAPEA
or Concordia.
The funding sources,
the operating costs,
and the cost per crewed day
deserve
a dedicated economic treatment
that this article does not attempt.

**Regulatory and treaty considerations.**
The Antarctic Treaty system,
the Outer Space Treaty,
and the national regulations
that govern
the operation of the analog
and the conduct of crewed missions
to space
intersect
in ways
that this article
does not treat.

**Governance of the simulated colony.**
The governance question
that
[Cryptotelemeritocracy for Space Exploitation][related_post_crypto_space]
addresses
in the abstract
is one
the analog can exercise
through deliberate procedural design.
A six-month or twelve-month analog mission
can implement
a constitutional charter
and produce
the first behavioural data
on it.
This article
does not treat
the governance side
of the analog tradition.

## Conclusion

A terrestrial off-grid analog
is the iteration engine
for a space colony
that no other instrument
can substitute for.
The honest analog
documents
where it sits
on the axes of closure,
isolation,
duration,
and environmental fidelity
and combines
its results
with results
from other facilities
that sit
at different points on those axes.
The prior attempts
across the analog tradition
demonstrate
the range
that is operationally achievable
and the gaps
the next-generation programmes
must close.
The most conspicuous gap
the survey identifies
is the absence
of a crewed buoyant analog
at altitude
that would correspond
to the Venus cloudtop concept
that
Landis
and the High Altitude Venus Operational Concept study
describe.

Site selection
is a trade study
across terrain analogy,
environmental hazard fidelity,
logistic isolation,
land tenure feasibility,
and operational supply chain cost.
The continental United States
offers credible analog sites
through the Mojave, Great Basin,
Sonoran, and Hawaiian volcanic terrains.
The international set
includes
the Atacama Desert,
Devon Island,
the Pilbara,
Iceland and Lanzarote,
the Antarctic continent,
and the Tibetan Plateau.

The facility-system stack
contains
nine subsystems
each of which
admits dedicated treatment.
The bootstrap regime
and the expansion regime
distinguish
the early-colony case
from the established-colony case
and require
different analog campaigns
to exercise
honestly.

Subsequent articles
in this category
will treat
the per-subsystem engineering,
the closed ecological system biology,
the behavioural and crew side,
and the economic side
of the same problem.
This article
opens
the working reference
that those subsequent articles
will build on.

## References

- [Reference, Amundsen-Scott South Pole Station][ref_amundsen_scott]
- [Reference, Antarctic Starlink Rollout][ref_antarctic_starlink]
- [Reference, Apollo Astronaut Geology Training in Iceland][ref_iceland]
- [Reference, Aquarius Reef Base][ref_aquarius]
- [Reference, Artemis II Lunar Training in Iceland][ref_artemis_iceland]
- [Reference, Atacama Desert Mars Analog][ref_atacama]
- [Reference, BIOS-3 Closed Ecosystem][ref_bios_3]
- [Reference, Biosphere 2][ref_biosphere_2]
- [Reference, Brooks Range, Alaska][ref_brooks]
- [Reference, CHAPEA at NASA Johnson Space Center][ref_chapea]
- [Reference, Concordia Station][ref_concordia]
- [Reference, Devon Island Mars Analog][ref_devon]
- [Reference, Edwards Air Force Base][ref_edwards]
- [Reference, ESA at Concordia][ref_esa_concordia]
- [Reference, Florida International University Aquarius][ref_fiu_aquarius]
- [Reference, Flashline Mars Arctic Research Station][ref_fmars]
- [Reference, Great Basin Desert][ref_great_basin]
- [Reference, Haughton Mars Project][ref_haughton_mars]
- [Reference, HAVOC High Altitude Venus Operational Concept][ref_havoc]
- [Reference, HERA at NASA Johnson Space Center][ref_hera]
- [Reference, HI-SEAS Facility][ref_hi_seas]
- [Reference, HI-SEAS at University of Hawaii][ref_hi_seas_uh]
- [Reference, ICON Technology][ref_icon]
- [Reference, Institute of Biomedical Problems Moscow][ref_ibmp]
- [Reference, Institute of Biophysics Krasnoyarsk][ref_ibp_krasnoyarsk]
- [Reference, International MoonBase Alliance][ref_imba]
- [Reference, Iridium Communications][ref_iridium]
- [Reference, ISS Water Recovery System][ref_iss_wrs]
- [Reference, Italian National Antarctic Research Programme][ref_pnra]
- [Reference, Landis Colonization of Venus Paper][ref_landis_venus]
- [Reference, Loon Stratospheric Balloon Programme][ref_loon]
- [Reference, Mars Desert Research Station][ref_mdrs]
- [Reference, Mars Society][ref_mars_society]
- [Reference, Mars-500 Programme][ref_mars_500]
- [Reference, Mauna Kea][ref_mauna_kea]
- [Reference, Mauna Loa][ref_mauna_loa]
- [Reference, McMurdo Station][ref_mcmurdo]
- [Reference, MELiSSA Closed-Loop Life Support][ref_melissa]
- [Reference, Mojave Desert][ref_mojave]
- [Reference, NASA Atacama Rover Astrobiology Drilling Studies][ref_arads]
- [Reference, NASA Extreme Environment Mission Operations][ref_neemo]
- [Reference, NASA Kilopower Reactor][ref_kilopower]
- [Reference, NASA Three-Dimensional Printed Habitat Challenge][ref_3d_habitat_challenge]
- [Reference, National Oceanic and Atmospheric Administration][ref_noaa]
- [Reference, National Science Foundation US Antarctic Program][ref_nsf_usap]
- [Reference, Pamir Mountains][ref_pamir]
- [Reference, PANGAEA Training Programme][ref_pangaea]
- [Reference, Pilbara Region][ref_pilbara]
- [Reference, Polar Institute Paul-Emile Victor][ref_ipev]
- [Reference, Ross Island Wind Energy Project][ref_ross_island_wind]
- [Reference, Sceye Stratospheric Airship Programme][ref_sceye]
- [Reference, Sonoran Desert][ref_sonoran]
- [Reference, Starlink Satellite Internet][ref_starlink]
- [Reference, Tibetan Plateau][ref_tibet]
- [Reference, University of Arizona at Biosphere 2][ref_arizona_biosphere]
- [Reference, World View Stratollite Programme][ref_world_view]
- [Reference, Yuegong-1 at Beihang University][ref_yuegong]
- [Related Post, Cryptotelemeritocracy for Space Exploitation][related_post_crypto_space]
- [Related Post, Introduction to Space Studies][related_post_space_studies]

[ref_3d_habitat_challenge]: https://www.nasa.gov/centennial-challenges/
[ref_amundsen_scott]: https://en.wikipedia.org/wiki/Amundsen%E2%80%93Scott_South_Pole_Station
[ref_antarctic_starlink]: https://www.nsf.gov/news/news_summ.jsp?cntn_id=307974
[ref_aquarius]: https://en.wikipedia.org/wiki/Aquarius_Reef_Base
[ref_arads]: https://www.nasa.gov/universe/atacama-rover-astrobiology-drilling-studies-arads/
[ref_arizona_biosphere]: https://biosphere2.org/
[ref_artemis_iceland]: https://science.nasa.gov/missions/artemis/nasas-artemis-ii-crew-uses-iceland-terrain-for-lunar-training/
[ref_atacama]: https://en.wikipedia.org/wiki/Atacama_Desert
[ref_bios_3]: https://en.wikipedia.org/wiki/BIOS-3
[ref_biosphere_2]: https://en.wikipedia.org/wiki/Biosphere_2
[ref_brooks]: https://en.wikipedia.org/wiki/Brooks_Range
[ref_chapea]: https://www.nasa.gov/humans-in-space/chapea/
[ref_concordia]: https://en.wikipedia.org/wiki/Concordia_Station
[ref_devon]: https://en.wikipedia.org/wiki/Devon_Island
[ref_edwards]: https://www.edwards.af.mil/
[ref_esa_concordia]: https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/Concordia
[ref_fiu_aquarius]: https://aquarius.fiu.edu/
[ref_fmars]: https://en.wikipedia.org/wiki/Flashline_Mars_Arctic_Research_Station
[ref_great_basin]: https://en.wikipedia.org/wiki/Great_Basin_Desert
[ref_haughton_mars]: https://en.wikipedia.org/wiki/Haughton%E2%80%93Mars_Project
[ref_havoc]: https://en.wikipedia.org/wiki/High_Altitude_Venus_Operational_Concept
[ref_hera]: https://www.nasa.gov/analog-missions/
[ref_hi_seas]: https://en.wikipedia.org/wiki/HI-SEAS
[ref_hi_seas_uh]: https://www.hawaii.edu/news/2018/06/29/
[ref_ibmp]: https://en.wikipedia.org/wiki/Institute_of_Biomedical_Problems
[ref_ibp_krasnoyarsk]: https://en.wikipedia.org/wiki/Institute_of_Biophysics
[ref_iceland]: https://en.wikipedia.org/wiki/Apollo_program_training
[ref_icon]: https://www.iconbuild.com/
[ref_imba]: https://moonbasealliance.com/
[ref_ipev]: https://www.institut-polaire.fr/en/
[ref_iridium]: https://www.iridium.com/
[ref_iss_wrs]: https://www.nasa.gov/missions/station/iss-research/nasa-achieves-water-recovery-milestone-on-international-space-station/
[ref_kilopower]: https://en.wikipedia.org/wiki/Kilopower
[ref_landis_venus]: https://ntrs.nasa.gov/citations/20030022668
[ref_loon]: https://en.wikipedia.org/wiki/Loon_LLC
[ref_mars_500]: https://en.wikipedia.org/wiki/Mars-500
[ref_mars_society]: https://www.marssociety.org/
[ref_mauna_kea]: https://en.wikipedia.org/wiki/Mauna_Kea
[ref_mauna_loa]: https://en.wikipedia.org/wiki/Mauna_Loa
[ref_mcmurdo]: https://en.wikipedia.org/wiki/McMurdo_Station
[ref_mdrs]: https://en.wikipedia.org/wiki/Mars_Desert_Research_Station
[ref_melissa]: https://www.esa.int/Enabling_Support/Space_Engineering_Technology/Melissa
[ref_mojave]: https://en.wikipedia.org/wiki/Mojave_Desert
[ref_neemo]: https://en.wikipedia.org/wiki/NEEMO
[ref_noaa]: https://www.noaa.gov/
[ref_nsf_usap]: https://www.usap.gov/
[ref_pamir]: https://en.wikipedia.org/wiki/Pamir_Mountains
[ref_pangaea]: https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/CAVES_and_Pangaea/Overview3
[ref_pilbara]: https://en.wikipedia.org/wiki/Pilbara
[ref_pnra]: https://www.pnra.aq/
[ref_ross_island_wind]: https://en.wikipedia.org/wiki/McMurdo_Station
[ref_sceye]: https://www.sceye.com/
[ref_sonoran]: https://en.wikipedia.org/wiki/Sonoran_Desert
[ref_starlink]: https://www.starlink.com/
[ref_tibet]: https://en.wikipedia.org/wiki/Tibetan_Plateau
[ref_world_view]: https://worldview.space/
[ref_yuegong]: https://en.wikipedia.org/wiki/Lunar_Palace_1
[related_post_crypto_space]: {% post_url 2026-02-23-cryptotelemeritocracy_for_space_exploitation %}
[related_post_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}

