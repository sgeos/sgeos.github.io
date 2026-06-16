---
layout: post
mathjax: false
comments: true
title:  "Sensor and Payload Selection for Search and Rescue Drones"
date:   2026-05-20 09:00:00 +0000
categories: aerospace engineering uav search-and-rescue sensors-and-payloads
---

<!-- A150 -->
<script>console.log("A150");</script>

[The five preceding articles in the SAR drone series][related_post_a149_training]
addressed
the platform classes,
the procurement framework,
the research and development pathway,
the geographic-setting filter,
and the operator training stack
that
the budgeted entity faces
when planning
a search and rescue
unmanned aerial vehicle programme.
The articles
treated the sensor payload
as an attribute of the airframe
rather than
as the central determinant
of mission capability
that it actually is.
A search and rescue programme
that
selects the airframe first
and the sensor second
will discover,
after the first deployment cycle,
that
the airframe
delivered the platform
over the search area
on schedule
while
the sensor
failed to detect
the missing person
in the canopy,
the water,
or the snow.
The sensor
is the mission.
The airframe
is the delivery vehicle.

This article
addresses
the sensor and payload selection
that
a working
search and rescue
drone programme requires,
from
the thermal imaging core
that
detects body heat
against
the environmental background
through
the electro-optical visible camera
that
confirms
the detection
to
the lidar
that
penetrates the canopy
and
the multispectral imager
that
distinguishes
disturbed soil
from
the surrounding terrain.
The article
treats
the sensor stack
as the principal
investment decision
that
the programme manager
makes
after
the airframe
and the operator training,
because
the sensor
determines
what
the platform
can detect,
not
how
the platform
flies.

## Why the Sensor Frames the Mission

A search and rescue drone
that
carries
the wrong sensor
for
the operating environment
returns
no detections
no matter
how well
the operator flies
or
how thoroughly
the search pattern
covers the area.
A thermal imager
with insufficient resolution
cannot resolve
a human figure
at the search altitude
that
the airframe
must maintain
for endurance.
A visible camera
without low-light capability
returns
useless imagery
during
the dawn and dusk hours
that
are
the highest-yield search periods.
A lidar
with insufficient point density
cannot detect
a body
beneath
the forest canopy
where
the visible and thermal sensors
have no line of sight.

The sensor
defines
the detection envelope.
The airframe
defines
the area
that
the sensor
can cover
in
the operating window.
A programme
that
buys
the long-endurance fixed-wing platform
without
the matching sensor capability
buys
endurance over an empty image.
A programme
that
buys
the high-resolution thermal core
on a multicopter
with insufficient endurance
buys
a high-resolution detection envelope
that
covers
a small area
before
the battery exhausts.
The sensor and the airframe
must match
for
the operating environment
and
the mission profile.

This pairing
is
the core of
the buyer's framework
that
[A146][related_post_a146_buying]
described
and
the operator training framework
that
[A149][related_post_a149_training]
described
because
the sensor selection
determines
the operator training
in
the sensor-specific
detection techniques
that
each sensor class
requires.
A thermal-equipped operator
trains
in
the thermal crossover
and
the false-positive signatures
that
rocks, animals, and reflective surfaces
produce.
A lidar-equipped operator
trains
in
the point-cloud analysis
that
the survey-grade lidar
requires
for
canopy-penetrating detection.

## The Sensor Stack Taxonomy

The sensor classes
that
a search and rescue drone programme
considers
fall into
six categories
with distinct
detection physics,
operating envelopes,
and
budget implications.
The article
addresses
each category
in turn
with
the SAR-specific operating considerations
that
distinguish
the SAR application
from
the more common
industrial inspection
and
mapping applications
that
dominate
the commercial drone sensor market.

The six categories are
thermal imaging,
electro-optical visible imaging,
lidar,
multispectral and hyperspectral imaging,
audio sensors and acoustic payloads,
and
specialised sensors
that
do not fit
the other five categories.
The categories
correspond to
distinct physical phenomena
that
each sensor class
exploits
for detection,
and
the programme
typically
deploys
multiple categories
in
a single mission
because
the detection physics
of each class
covers
a different failure mode
of
the other classes.

| Category | Detection Physics | Typical Range | Per-Sensor Cost Tier |
| --- | --- | --- | --- |
| Thermal Imaging | Long-wave infrared emission from heat sources | 30 to 300 metres for human detection | USD 3K to USD 50K |
| Electro-Optical Visible | Reflected visible light | Limited by atmospheric conditions and resolution | USD 1K to USD 30K |
| Lidar | Active laser ranging with surface return | 50 to 500 metres typical | USD 10K to USD 200K |
| Multispectral and Hyperspectral | Reflected light at specific narrow bands | Surface-property dependent | USD 5K to USD 100K |
| Audio Payloads | Acoustic pressure waves | 100 to 500 metres for loudspeakers | USD 1K to USD 10K |
| Specialised Sensors | Various physical phenomena | Application dependent | USD 5K to USD 500K |

The cost tiers
span
two orders of magnitude
within
each category,
which means
the sensor budget
is
the dominant variable
in
the per-platform cost
once
the airframe class
is chosen.
A multicopter
with a basic thermal core
costs
less than
the same multicopter
with
a survey-grade lidar
by
a factor of ten,
and
the survey-grade lidar
costs
less than
the cooled MWIR thermal core
that
the same multicopter
can carry
by
a factor of five.
The sensor budget
deserves
its own line item
in
the programme budget
because
the sensor cost
typically
exceeds
the airframe cost
for
the higher-tier platforms
and
the higher-tier sensors.

## Thermal Imaging

Thermal imaging
is
the SAR mission's
single most
important sensor class
because
the missing person
emits
infrared radiation
that
the surrounding environment
typically
does not match
in
the same way.
A human body
at thirty-seven degrees Celsius
against
a forest floor
at five degrees Celsius
presents
a thirty-two-Kelvin temperature differential
that
even
a modest thermal core
can detect
at typical search altitudes.
A human body
in shallow water
or
under
the forest canopy
presents
a smaller differential
that
only
the higher-grade thermal cores
can detect
reliably.

### Uncooled Long-Wave Infrared Versus Cooled Mid-Wave Infrared

Thermal imagers
fall into
two physical classes
that
have
distinct
detection capabilities,
operating costs,
and
regulatory regimes.
The uncooled long-wave infrared core,
typically called
LWIR or microbolometer,
detects
the eight to fourteen micrometre band
that
human body temperature
radiates most strongly
in.
The cooled mid-wave infrared core,
typically called
MWIR,
detects
the three to five micrometre band
that
warmer objects
radiate more strongly
in,
and
the cooler operating temperature
of the detector
reduces
the thermal noise
in
the image
to
a level
that
the uncooled core
cannot match.

The uncooled LWIR core
operates
at ambient temperature
without
the cooling apparatus
that
the MWIR core
requires.
The uncooled core
is
the dominant choice
for
the SAR drone application
because
the uncooled core
costs
less,
weighs less,
draws less power,
and
operates
without
the warm-up time
that
the cooled core
requires.
The cooled MWIR core
delivers
higher sensitivity
at
the cost
of
five to ten times
the price,
a multi-kilogram weight penalty,
a multi-watt power draw,
and
the export controls
that
[the International Traffic in Arms Regulations][ref_itar]
impose
on
the cooled cores
that
exceed
the threshold sensitivity
that
the Department of State
classifies as
controlled defence article.

A budgeted SAR programme
typically
deploys
the uncooled LWIR core
because
the cooled core
exceeds
the operating budget
for
all but
the largest programmes
and
the export controls
on
the cooled core
restrict
the operator pool
and
the cross-border deployment
that
the cooled-core platform
requires.
The article
treats
the uncooled LWIR core
as
the default thermal payload
for
the rest of
the article
and
notes
the specific operating environments
where
the cooled MWIR core
remains necessary
despite
the cost.

### Noise Equivalent Temperature Difference

The principal performance metric
for
a thermal imager
is
the Noise Equivalent Temperature Difference,
typically abbreviated
NETD.
The NETD
measures
the smallest temperature difference
that
the imager
can resolve
above
the inherent noise floor
of the sensor.
A lower NETD value
indicates
a more sensitive sensor,
expressed
in milliKelvin units.

The thermal core market
spans
NETD values
from
under thirty milliKelvin
for
the high-end uncooled cores
through
the forty-five to fifty milliKelvin range
for
the mid-tier uncooled cores
to
the sixty to eighty milliKelvin range
for
the entry-tier uncooled cores.
The cooled MWIR cores
typically
deliver
NETD values
under twenty milliKelvin,
which is
the principal reason
the cooled cores
remain
the preferred choice
for
the most difficult detection scenarios
where
the temperature differential
between
the target
and
the environment
is small.

For SAR application,
the NETD value
determines
the detection range
for
the more difficult thermal scenarios
that
the operating environment
presents.
A person
in shallow water
presents
a temperature differential
of a few Kelvin
because
the water
buffers
the body's surface temperature
toward
the water temperature.
A person
beneath
a thin canopy
presents
a differential
reduced
by
the canopy temperature
and
the canopy's reflectance.
A person
on snow
presents
a large differential
that
even
the lowest-sensitivity core
can detect,
but
the same person
on a sun-warmed rock
presents
a thermal crossover
that
the sensitive cores
can resolve
where
the less sensitive cores
cannot.

### Sensor Resolution Tiers

The thermal sensor resolution
determines
the spatial resolution
of
the thermal image
at a given altitude.
The thermal sensors
in
the SAR drone market
fall into
four resolution tiers
that
the programme
selects
based on
the search altitude,
the desired
ground sample distance,
and
the budget.

The entry tier
is
the 320 by 256 pixel sensor
that
the [Teledyne FLIR Boson+][ref_flir_boson]
and
similar cores
provide.
The entry tier
delivers
a ground sample distance
of approximately
30 to 60 centimetres
at a 100 metre altitude
with
a typical lens.
The entry tier
suffices
for
detecting
a human figure
at modest altitudes
above
open terrain
but
struggles
in
the cluttered terrain
that
SAR operations
frequently encounter.

The mid tier
is
the 640 by 512 pixel sensor
that
the [Workswell WIRIS Pro][ref_workswell_wiris]
and
[Teledyne FLIR Hadron 640R][ref_flir_hadron]
provide.
The mid tier
delivers
a ground sample distance
of approximately
15 to 30 centimetres
at the same altitude,
which suffices
for
the most SAR detection tasks
in
the operating environments
that
the programme typically encounters.

The upper tier
is
the 1024 by 768 pixel sensor
and the 1280 by 1024 pixel sensor
that
the higher-grade cores provide.
The upper tier
delivers
a ground sample distance
under 15 centimetres
at the same altitude
and
extends
the detection range
to
the higher search altitudes
that
the larger fixed-wing platforms operate at.
The upper tier
costs
approximately
five to ten times
the mid tier
and
weighs
proportionately more,
which limits
the upper tier
to
the larger platforms
that
the programme
operates.

The frontier tier
is
the multi-megapixel cooled MWIR core
that
the [Sierra-Olympia Ventus][ref_sierra_olympia_ventus]
and
similar cores provide.
The frontier tier
operates
at multiple kilometre detection ranges
that
the uncooled cores
cannot match
and
costs
in
the high five-figure
to
six-figure range
per core.
The frontier tier
remains
the province
of
the largest SAR programmes
and
the dual-use SAR-defence programmes
that
the funding regime
of
the defence application
underwrites.

### Radiometric Versus Non-Radiometric

A thermal imager
that
records
calibrated temperature values
at each pixel
is called
radiometric.
A non-radiometric imager
records
relative brightness values
that
correspond
loosely
to temperature
but
do not preserve
the absolute calibration.
The radiometric capability
costs
incrementally more
than
the non-radiometric capability
in
the same sensor family
and
delivers
the post-mission analysis capability
that
the SAR mission frequently requires.

For SAR application,
the radiometric capability
enables
the post-mission analysis
of
the thermal imagery
where
the operator
can confirm
the candidate detection
by measuring
the absolute temperature
of
the candidate signature
against
the surrounding environment.
A signature
at body temperature
that
the operator missed
in
the real-time detection workflow
becomes
detectable
in
the post-mission review
because
the absolute temperature
distinguishes
the human signature
from
the warm-rock signature
and
the animal signature.

The article
recommends
the radiometric capability
for
the SAR programme
that
budgets
the incremental cost
because
the post-mission analysis
captures
the detections
that
the real-time workflow misses,
and
the SAR mission cannot tolerate
the missed detection
that
a colder sensor capability
would have caught.

### Vendor Landscape

The thermal imaging core
that
a SAR drone payload integrates
comes from
a small number
of
sensor manufacturers
that
sell
the core module
to
the integrator
that
builds
the drone payload.
The dominant core manufacturer
is
[Teledyne FLIR][ref_teledyne_flir],
which produces
the Boson, Boson+, Hadron, Tau, and Lepton families
that
appear
in most
commercial thermal payloads.
The other significant manufacturer
is
[Sierra-Olympia Technologies][ref_sierra_olympia],
which produces
the Vinden and Ventus families
of cooled MWIR and uncooled LWIR cores
for
the larger payloads
and
the defence applications.
The third significant manufacturer
is
[Lynred][ref_lynred],
which produces
the cores
that
appear
in
the European thermal payloads.

The payload integrators
that
build
the drone-ready thermal payload
include
[Workswell][ref_workswell]
in
the European market,
[DJI Enterprise][ref_dji_enterprise]
in
the commercial market,
and
[Teledyne FLIR's own UAS payloads][ref_flir_uas]
in
the public-safety market.
The integrators
typically
add
the gimbal,
the visible camera,
the laser rangefinder,
and
the data interface
that
the drone airframe requires
on top of
the bare thermal core
that
the core manufacturer
provides.

The article
recommends
the programme manager
evaluate
the payload integrator
on
the gimbal performance,
the data interface,
the firmware stability,
and
the warranty coverage
in addition to
the underlying thermal core specification,
because
the integrator
adds
substantial value
to
the bare core
in
the integration work
that
the drone airframe requires.

## Electro-Optical Visible Imaging

The electro-optical visible camera
is
the second sensor
that
a SAR drone
typically carries.
The visible camera
confirms
the thermal detection
by providing
the visual identification
that
the operator uses
to distinguish
the missing person
from
the false positive
that
the thermal sensor returned.
The visible camera
also
enables
the daytime visual search
that
the thermal sensor
does not perform well
under high solar load
where
the thermal crossover
across the ground surface
reduces
the temperature differential
that
the thermal sensor relies on.

### Sensor Format and Resolution

The visible camera
in
a SAR drone payload
typically uses
the Sony IMX sensor family
that
dominates
the commercial drone camera market.
The sensor format
ranges from
the half-inch sensor
in
the entry-tier payload
through
the one-inch sensor
in
the mid-tier payload
to
the Micro Four Thirds
and
the full-frame sensor
in
the upper-tier payload.
The larger sensor format
delivers
the better low-light performance
and
the better dynamic range
at the cost
of
the larger payload mass
and
the higher cost
of
the lens system
that
the larger sensor requires.

The resolution
in
the visible camera
ranges from
the 12 megapixel sensor
that
the entry payload provides
through
the 20 to 48 megapixel sensor
in
the mid payload
to
the 100 megapixel sensor
in
the upper payload.
The higher resolution
delivers
the better ground sample distance
at the search altitude
and
extends
the detection range
for
the visual search
to
the higher search altitudes
that
the longer-endurance platforms
operate at.

### Stabilisation

The gimbal stabilisation
that
the visible camera payload requires
falls into
two classes
that
match
the airframe class.
The 2-axis gimbal
stabilises
the pitch and roll axes
and
suffices
for
the fixed-wing platform
that
operates
in steady cruise flight
above
the turbulence layer.
The 3-axis gimbal
adds
the yaw axis stabilisation
and
provides
the precision pointing
that
the multicopter platform
requires
because
the multicopter
operates
in
the lower altitude
where
the turbulence
exceeds
the stabilisation bandwidth
of
the 2-axis gimbal.

The gimbal vendors
that
the SAR programme considers
include
[Gremsy][ref_gremsy],
[Freefly Movi][ref_freefly_movi],
[Tarot][ref_tarot],
and
the integrated gimbals
that
[DJI Zenmuse][ref_dji_zenmuse]
and
[Skydio][ref_skydio_drones]
provide
on
the airframe-specific payload mounts.
The integrated gimbals
typically
deliver
the best performance
on
the airframe-specific mount
because
the gimbal firmware
and
the airframe flight controller
share
the inertial reference
that
the precision pointing requires.

### Low-Light and Starlight Imaging

The SAR mission
frequently operates
in
the low-light conditions
of dawn,
dusk,
and night
where
the standard visible camera
returns
useless imagery.
The low-light visible cameras
that
the SAR programme considers
use
the [Sony Starvis][ref_sony_starvis]
or
the equivalent
near-infrared-sensitive sensor
that
captures
the residual illumination
from
the sky
and
the ambient light sources
at
the search location.

The low-light visible camera
complements
the thermal sensor
because
the visible camera
confirms
the visual identification
that
the thermal sensor cannot provide.
The combined thermal-and-visible payload
is
the dominant SAR drone configuration
because
the two sensors
together
deliver
the detection-and-confirmation workflow
that
the SAR mission requires.

## Lidar

Lidar
is
the third sensor class
that
the SAR drone programme considers.
Lidar
provides
the canopy penetration
that
the thermal and visible sensors
cannot match
and
delivers
the three-dimensional terrain mapping
that
the search planning
and
the post-mission documentation
require.
A SAR programme
that
operates
in
the forested terrain
where
the canopy
obscures
the ground surface
from
the airborne sensors
above
considers
the lidar payload
as
the principal sensor
for
the canopy-obscured search.

### Range, Point Density, and Return Modes

Lidar systems
fall into
three principal performance tiers
that
correspond to
distinct SAR applications.
The short-range lidar tier
operates
at
the 50 to 100 metre range
with
the modest point density
of
approximately 100 to 200 points per square metre
and
the single-return mode
that
captures
the first surface return only.
The short-range tier
suffices
for
the obstacle avoidance application
and
the digital elevation modelling
of
the open terrain
but
does not penetrate
the canopy
because
the single-return mode
captures
the canopy surface
and
not
the ground surface below.

The mid-range survey lidar tier
operates
at
the 200 to 400 metre range
with
the higher point density
of
500 to 1500 points per square metre
and
the multiple-return mode
that
captures
the first surface,
the intermediate returns,
and
the last return
that
typically
corresponds to
the ground surface
beneath
the canopy.
The survey tier
penetrates
the canopy
where
the canopy
has gaps
that
admit
the laser pulse to ground
and
returns
the ground point cloud
that
the SAR analyst
processes
to identify
ground anomalies
that
might correspond to
the missing person.

The frontier lidar tier
operates
at
the 500 metre and longer range
with
the higher point density
of multiple thousand points per square metre
and
the photon-counting mode
that
the Geiger-mode lidar
provides.
The frontier tier
delivers
the canopy penetration
that
the dense canopy
that
the survey tier
cannot fully penetrate
nonetheless reveals
to
the photon-counting receiver.
The frontier tier
costs
in
the six-figure range
per system
and
remains
the province of
the survey-engineering market
and
the defence application.

### Georegistration

The lidar point cloud
delivers
the operational value
that
the SAR mission requires
only
when
the point cloud
is georegistered
to
the ground reference frame
that
the search planning operates in.
The georegistration
combines
the lidar return data
with
the airborne inertial measurement
and
the Global Navigation Satellite System position
to compute
the geodetic coordinates
of
each return point.

The georegistration quality
falls into
two principal classes.
The real-time kinematic GNSS class,
typically called
RTK,
provides
the centimetre-level position accuracy
through
the real-time correction stream
from
the ground reference station
to
the airborne receiver.
The post-processed kinematic GNSS class,
typically called
PPK,
provides
the same centimetre-level accuracy
through
the post-mission processing
of
the airborne GNSS log
against
the ground reference log
that
the survey workflow stores
for later analysis.

The RTK class
suits
the real-time SAR mission
where
the operator
needs
the immediate point cloud
for
the ongoing search.
The PPK class
suits
the post-mission documentation
where
the analyst
has time
to process
the GNSS logs
against
the reference data
and
produce
the higher-accuracy point cloud
that
the final search documentation requires.

### Lidar Vendor Landscape

The lidar vendors
that
the SAR programme considers
include
[LightWare LiDAR][ref_lightware]
for
the short-range altimeter
and
the obstacle-avoidance sensor,
[Ouster][ref_ouster]
for
the rotating mid-range survey sensor,
[Hesai][ref_hesai]
for
the solid-state mid-range survey sensor,
[Livox][ref_livox]
for
the DJI-compatible survey sensor,
and
[YellowScan][ref_yellowscan],
[Phoenix LiDAR Systems][ref_phoenix_lidar],
and
[Riegl][ref_riegl]
for
the survey-grade integrated payloads.

The DJI Enterprise market
provides
the [DJI Zenmuse L2][ref_dji_zenmuse_l2]
as
the dominant payload for
the DJI Matrice 350 RTK
and
the related airframes.
The Zenmuse L2
delivers
the survey-grade performance
at
a price point
substantially below
the survey-engineering payloads
of
the YellowScan and Riegl class
and
suffices
for
the SAR mission
in
the canopy-obscured terrain
that
the SAR programme typically encounters.

The article
recommends
the SAR programme
evaluate
the lidar payload
on
the point density,
the effective range
at
the operating altitude,
the return mode,
and
the georegistration accuracy
in addition to
the payload mass
and
the airframe compatibility,
because
the lidar payload
substantially exceeds
the thermal payload
in
mass,
power draw,
and
data bandwidth
and
constrains
the airframe choice
to
the platforms
that
can carry
the payload
without
the unacceptable endurance penalty.

## Multispectral and Hyperspectral Imaging

Multispectral and hyperspectral imagers
detect
the reflected light
at specific narrow bands
that
correspond to
the spectral signatures
of
the materials
and
the surface features
that
the imager observes.
The multispectral imager
detects
a small number of bands,
typically five to ten,
that
the imager designer
selects
for
the target application.
The hyperspectral imager
detects
hundreds of bands
that
the full spectral signature
of
the observed surface
contains
and
permits
the post-mission analysis
to extract
the spectral signatures
that
the analyst
later identifies as
mission-relevant.

### Wildfire Application

The wildfire application
of
the multispectral imager
uses
the shortwave infrared band
that
the [USGS Landsat program][ref_usgs_landsat]
and
[NASA Earth Observatory][ref_nasa_earth_observatory]
have established
as
the standard hot-spot detection band
for
satellite-borne wildfire monitoring.
The same band
on
the drone-borne multispectral imager
detects
the hot spots
under
the smoke layer
that
the visible camera
cannot penetrate
and
provides
the search advantage
that
the wildfire search-and-rescue mission
requires
when
the missing person
is
in
the active burn area
that
the smoke
obscures.

The [MicaSense Altum-PT][ref_micasense_altum]
and
similar multispectral payloads
provide
the necessary spectral bands
for
the wildfire hotspot detection
at
a price point
that
the larger SAR programme can budget.
The dedicated thermal core
typically
exceeds
the multispectral hot-spot detection
in
the active-burn monitoring application,
but
the multispectral imager
provides
the secondary spectral information
that
the post-mission analysis
uses
to identify
the burn severity
and
the residual heat sources
that
the post-fire search relies on.

### Water Rescue Application

The water rescue application
of
the multispectral imager
uses
the visible-and-near-infrared bands
that
distinguish
the human signature
in shallow water
from
the surrounding water surface.
The technique
exploits
the water absorption
that
attenuates
the near-infrared signal
returning from
the water surface
while
preserving
the near-infrared signal
returning from
the human skin or clothing
that
breaks
the water surface.
The technique
extends
the water rescue search range
beyond
the visible camera detection range
where
the surface glare
and
the wave action
obscure
the visual signature
of
the casualty.

### Ground Anomaly Detection

The ground anomaly detection
application
of
the hyperspectral imager
uses
the full spectral signature
of
the ground surface
to identify
the disturbed soil
that
might correspond to
the missing person
who
has lain
on the surface
for
an extended period
or
to
the buried casualty
that
the search team
has been unable to locate
through
the conventional sensors.
The technique
relies on
the spectral signature differences
that
the disturbed surface vegetation
and
the disturbed soil chemistry
introduce
relative to
the surrounding undisturbed ground.

The hyperspectral imagers
that
the SAR programme considers
include
the [Headwall Photonics][ref_headwall]
Nano-Hyperspec and Micro-Hyperspec families
and
the [Cubert ULTRIS][ref_cubert]
snapshot hyperspectral imagers.
The hyperspectral payload
costs
substantially more than
the multispectral payload
and
requires
the specialist analysis pipeline
that
the SAR programme
does not typically operate.
The hyperspectral payload
remains
the province of
the largest SAR programmes
and
the academic partners
that
the programme works with
under
the research and development
relationships
that
[A147][related_post_a147_rd]
described.

## Audio Sensors and Acoustic Payloads

The audio payload
that
a SAR drone carries
falls into
two distinct categories
that
serve
different mission functions.
The loudspeaker payload
broadcasts
the rescue communication
that
the search team
sends to
the missing person
to direct
them to
a safe location,
to confirm
their presence
through
the audible response,
or
to maintain
the morale
that
the rescue conversation
provides
during
the extended search.
The microphone payload
detects
the distress call
that
the missing person sends
and
permits
the search team
to localise
the response source
relative to
the drone position.

### Loudspeaker Payloads

The drone-mounted loudspeaker
provides
the public-address capability
that
the search team uses
to direct
the missing person.
The loudspeaker payload
delivers
the audible message
at
the search altitude
and
the search distance
that
the airframe operates at
without
the ground-based loudspeaker
that
the search team
would otherwise position
manually.

The loudspeaker payloads
that
the SAR programme considers
include
the [DJI Zenmuse V1][ref_dji_zenmuse_v1]
integrated thermal-and-loudspeaker payload
for
the Matrice 300 RTK,
Matrice 350 RTK,
and Matrice 400 platforms,
the [Sky Speaker-I from Yangda][ref_sky_speaker]
that
the DJI consumer and prosumer platforms can carry
as an aftermarket payload,
and
the integrated public-address modules
that
the public-safety drone vendors
provide
as accessories to
the search-and-rescue airframes.

The principal performance metric
for
the loudspeaker payload
is
the sound pressure level at distance,
typically measured
in decibels at one metre.
The Zenmuse V1
delivers
approximately 127 decibels at one metre
and
operates over
approximately 500 metres of audio range,
which corresponds to
the typical SAR search altitude
where
the audible message
remains intelligible
to
the ground listener.

### Acoustic Detection

The acoustic detection
application
of
the drone-mounted microphone
remains
in
the research phase
at the time
of writing.
The principal challenge
is
the rotor noise
that
the multicopter airframe produces,
which masks
the distress signals
that
the missing person
might send.
The fixed-wing airframe
operates
without
the rotor noise
of the multicopter
but
the wind noise
on
the fixed-wing platform
masks
the distress signal
similarly.
The current research
relies on
the noise-cancellation algorithms
that
the post-processing
applies
to
the recorded audio
to extract
the distress signal
from
the airframe noise.

The acoustic detection research
that
the SAR programme follows
includes
the work
from
the [Carnegie Mellon Robotics Institute AirLab][ref_cmu_robotics]
on
SAR-oriented aerial robotics,
the published [DroneAudioset benchmark][ref_droneaudioset]
that
captures
the rotor-noise interference
under multiple flight conditions
for distress-signal detection research,
and
the [DARPA OFFSET program][ref_darpa_offset]
work
on
the distributed acoustic sensing
that
the swarm-borne microphone
networks
provide.

## Payload Integration

The sensor payload
attaches
to
the airframe
through
the integration mechanisms
that
the airframe vendor provides.
The integration mechanism
determines
the payload mass budget,
the power budget,
the data bandwidth budget,
and
the operational workflow
that
the operator
uses
to switch
the payload
in
the field.

### Payload Mass and Endurance

The payload mass
that
the airframe can carry
trades
directly
against
the endurance
that
the airframe can deliver.
A multicopter
that
carries
the upper-tier thermal payload
of approximately 1.5 kilograms
delivers
approximately 20 minutes of endurance
compared to
the 35 minutes of endurance
that
the same multicopter
delivers
with
the entry-tier thermal payload
of approximately 0.5 kilograms.
The fixed-wing platform
suffers
proportionately less
from
the payload mass
because
the fixed-wing efficiency
that
[A145][related_post_a145_physics]
described
recovers
the lift more efficiently than
the multicopter rotor system.

The programme manager
plans
the payload mass
against
the airframe endurance budget
and
the mission profile
to verify
that
the payload-and-airframe combination
delivers
the operating window
that
the search mission requires.
A search mission
that
requires
60 minutes of on-station time
cannot use
a multicopter
that
delivers only
20 minutes of endurance
with
the necessary payload,
which forces
the programme
to choose
between
the lighter payload
that
extends
the endurance
or
the fixed-wing platform
that
delivers
the necessary endurance
with
the heavier payload.

### Power Budget

The sensor payload
draws
the electrical power
from
the airframe power bus
through
the payload connector
that
the airframe vendor provides.
The drone power buses
do not converge
on
a universal standard
across vendors,
and
the typical payload connector
exposes
a regulated low-voltage rail
in
the 12 volt or 24 to 28 volt range
to
the payload
even where
the main battery stack
operates at
a higher voltage.
The relevant aviation power standards
that
the certified payloads sometimes reference
are
the [MIL-STD-704 aircraft electrical power standard][ref_mil_std_704]
for
the higher-grade airborne integrations
and
the [MIL-STD-1275 ground vehicle 28 volt standard][ref_mil_std_1275]
for
the integrations
that
share components with
the ground-vehicle electronics ecosystem,
without
the drone industry
having adopted
either standard
as
the universal payload bus standard.

The thermal payload
typically
draws
5 to 15 watts
in
the operating mode
and
the standby mode draws
1 to 3 watts.
The lidar payload
draws
20 to 50 watts
in
the active scanning mode
because
the laser power
and
the rotating mechanism
that
the rotating lidar uses
together
exceed
the thermal payload power budget
by
an order of magnitude.
The hyperspectral payload
draws
10 to 30 watts
because
the cooled sensor
and
the spectrometer mechanism
together
consume
substantially more power than
the simple multispectral imager.

The programme manager
plans
the payload power
against
the airframe power budget
in
the same way
as the mass budget.
The airframe
that
delivers
the necessary battery capacity
for
the thermal payload
may not deliver
the necessary capacity
for
the lidar payload
that
draws
three to five times the power
because
the additional load
shortens
the battery life
before
the airframe
reaches the mission endpoint.

### Data Bandwidth

The sensor payload
generates
the imagery data
that
the airframe
must transport
to
the ground station
or
the onboard storage
during
the mission.
The thermal payload
generates
relatively low data rates,
typically
10 to 50 megabits per second
for
the streamed video
and
500 megabytes per hour
for
the recorded radiometric imagery.
The lidar payload
generates
substantially higher data rates,
typically
100 to 500 megabits per second
for
the streamed point cloud
and
multiple gigabytes per hour
for
the recorded raw point cloud
that
the post-processing
later analyses.
The hyperspectral payload
generates
the highest data rates,
typically
multiple gigabits per second
of
the raw spectral data
that
the onboard storage
captures
and
the ground station
processes after
the mission.

The data bandwidth budget
constrains
the operational workflow
of
the higher-bandwidth payloads
because
the airframe data link
typically cannot stream
the full lidar or hyperspectral data
to the ground.
The operator
typically
relies on
the onboard storage
for
the full data
and
the downsampled stream
for
the real-time situation awareness
that
the ground station
displays.

### Gimbal Mount Standards

The payload
attaches to
the airframe
through
the gimbal mount
that
the airframe vendor specifies.
The DJI Enterprise market
uses
the [DJI SkyPort and X-Port][ref_dji_skyport]
mounts on
the Matrice family,
which provide
the mechanical interface,
the power connector,
and
the data interface
for
the DJI-compatible payloads
through
the [DJI Payload SDK][ref_dji_psdk]
that
the third-party payload integrator
develops against.
The fixed-wing platforms
that
the SAR programme uses
typically
provide
a vendor-specific custom mount
for which
the payload-integrator partnership
delivers
the integration work,
because
the [ASTM Committee F38][ref_astm_f38]
on Unmanned Aircraft Systems
has not standardised
a universal payload interface
that
the airframe vendors collectively follow.

The article
recommends
the programme manager
verify
the payload-airframe mount compatibility
before
the payload acquisition
because
the mount incompatibility
forces
either
the custom integration work
that
the integrator
charges substantially for
or
the substitute payload
that
fits
the airframe mount
but
does not deliver
the necessary sensor capability.

### Motion Imagery Metadata Standards

The video metadata standard
that
the public-safety
and defence-adjacent SAR programmes
follow
is
the [Motion Imagery Standards Board][ref_misb]
KLV metadata standard
that
the [STANAG 4609][ref_stanag_4609]
NATO Standardisation Agreement
references.
The KLV metadata embeds
the airborne position,
the camera pointing,
the field of view,
and
the timestamp
in
the video stream
so that
the downstream analysis
can geolocate
the imagery
to
the ground reference frame
that
the search planning operates in.

The programme manager
that
plans
the integration with
the regional or federal SAR command and control
specifies
the KLV-compliant video output
in
the payload acquisition
because
the C2 systems
that
the federal partners operate
require
the KLV-encoded video
for
the situation awareness
that
the federal coordination
relies on.
The civilian-only SAR programme
that
operates
without
the federal C2 integration
may
operate
without
the KLV metadata,
but
the federal integration
that
[A148][related_post_a148_geographic]
described
for
the federal frontier-operating environment
typically requires
the KLV metadata
for
the integration to be approved.

## Sensor Data Management and Chain of Custody

The sensor selection
determines
the data
that
the platform produces,
and
the data
that
the platform produces
constitutes
the deliverable
that
the SAR programme returns
to
the search team,
to
the incident command,
to
the next of kin,
and,
in
the cases
where
the search outcome enters
the legal process,
to
the medical examiner,
the law enforcement investigator,
and
the court.
A SAR drone programme
that
plans
the multi-year capability investment
treats
the data management
as
an inseparable companion to
the sensor selection
because
the choice
of
the radiometric thermal core,
the survey-grade lidar,
or
the KLV-encoded electro-optical video
imposes
the storage burden,
the chain of custody requirement,
the retention obligation,
and
the cybersecurity posture
that
the platform fleet
must support
across
the service life
of
the platform.

### Data Volume by Sensor Class

The sensor classes
that
the article describes
differ
by
an order of magnitude
in
the data volume
that
each produces
per operating hour.
A budgeted programme
that
plans
the data storage
without
the sensor-specific data volume
discovers,
within
the first months of operation,
that
the storage capacity
that
the IT budget allocated
exceeds
or falls short of
the operating need
by
a substantial margin.

The thermal radiometric payload
produces
approximately
500 megabytes to 5 gigabytes per operating hour
in
the radiometric raw imagery,
with
the lower bound corresponding to
the radiometric still image capture mode
and
the upper bound corresponding to
the continuous radiometric video capture mode
that
the larger SAR programmes deploy
for
the post-mission analysis.
The 4K electro-optical video payload
produces
approximately
30 to 60 gigabytes per operating hour
because
the high-bitrate visible video
dominates
the data volume
even where
the thermal sensor
contributes radiometric overhead.
The survey-grade lidar payload
produces
approximately
5 to 50 gigabytes per operating hour
in
the recorded raw point cloud,
with
the higher volumes
corresponding to
the higher point density,
the multiple-return mode
that
the canopy-penetrating mission requires,
and
the higher point-rate sensors
that
the frontier survey-grade systems carry.
The hyperspectral payload
produces
approximately
100 gigabytes to 1 terabyte per operating hour
because
the full spectral data cube
that
the post-mission analysis processes
captures
hundreds of bands
at
the full spatial resolution
of
the imager.

The programme manager
that
plans
the data infrastructure
sums
the per-sortie data volume
across
the operating fleet
and
the operating tempo
to compute
the required storage capacity,
the required ingest bandwidth,
and
the required backup capacity
that
the programme commits to
across
the service life
of
the platform.
A multicopter fleet
of five platforms
flying
two sorties per platform per week
at
one hour per sortie
produces
approximately
5 to 50 gigabytes per week
for
the thermal payload
and
approximately
300 to 600 gigabytes per week
for
the 4K electro-optical payload,
which sums to
approximately
15 to 35 terabytes per year
for
the modest mid-tier programme
that
the A146 framework characterised as
Tier 2.

### Storage Architecture

The storage architecture
that
the programme deploys
falls into
three principal classes
that
the IT decision matches
to
the operating requirements,
the data sovereignty constraints,
and
the budget.

The onboard storage class
captures
the raw sensor data
on
the platform itself
during
the mission
and
the ground station
ingests
the data
after
the platform returns to base.
The onboard class
imposes
no continuous network bandwidth requirement
because
the storage medium
that
the platform carries
holds
the full mission data
until
the ground crew transfers it.
The onboard class
is
the dominant choice
for
the lidar and hyperspectral payloads
that
produce
the data rates
that
the airborne datalink
cannot stream
in real time.

The ground station class
captures
the data
in
the local ground station
that
the operator commands
the platform from,
with
the airborne datalink
streaming
the video,
the lower-bandwidth thermal stream,
and
the platform telemetry
to
the ground station
in real time.
The ground station class
is
the dominant choice
for
the thermal and visible payloads
that
produce
the data rates
that
the airborne datalink
can stream
without
the substantial compression
that
the higher-bandwidth payloads require.

The cloud class
captures
the data
in
the vendor-operated cloud platform
that
the airborne datalink
or
the ground station
forwards
the data to.
The cloud class
is
the dominant choice
for
the multi-platform fleet
that
needs
the centralised data management
across
multiple operating locations
and
the centralised search-team access
across
multiple incident command posts.
The cloud class
introduces
the data residency,
the vendor data handling,
and
the cybersecurity considerations
that
the article addresses below
under
the cybersecurity controls
and
the vendor data handling policies sections.

The programme manager
that
plans
the storage architecture
selects
the class
that
the dominant sensor produces data for
and
designs
the migration pathway
between
the onboard, ground station, and cloud classes
that
the operating workflow requires
across
the mission lifecycle.
The thermal radiometric data
that
the platform produces
typically migrates
from
the onboard storage
to
the ground station
during
the post-flight download,
to
the long-term archive
after
the post-mission analysis,
and,
in
the cases
where
the search outcome enters
the legal process,
to
the evidence repository
that
the receiving agency operates.

### Chain of Custody for Evidentiary Use

The SAR mission outcome
sometimes enters
the legal process
where
the missing person
is determined to have been
the victim of
the criminal act,
where
the search returned
the body of
the missing person
that
the medical examiner processes,
or
where
the search itself
is questioned
in
the negligence action
that
the next of kin brings
against
the responding agency.
In
the cases
where
the sensor imagery
becomes
the evidence
that
the legal process examines,
the chain of custody
that
the programme established
across
the data lifecycle
determines
the admissibility
of
the imagery
under
the [Federal Rules of Evidence][ref_federal_rules_of_evidence]
and
the state evidence rules
that
the receiving court applies.

The chain of custody
for
the SAR drone imagery
combines
three principal elements
that
the programme must establish
from
the moment of data capture
through
the production of
the imagery
to
the court.

The first element
is
the metadata anchor
that
the [MISB ST 0601 KLV standard][ref_misb]
provides
in
the streamed video.
The KLV metadata embeds
the airborne position,
the camera pointing,
the field of view,
and
the timestamp
in
the video stream itself,
which establishes
the where, the when, and the what
of
the imagery
without
the separate metadata file
that
the downstream analysis
might otherwise need
and
that
the chain of custody
might otherwise lose.

The second element
is
the cryptographic integrity record
that
the storage system attaches
to
the captured imagery.
A SHA-256 hash
that
the ground station computes
over
the imagery file
at
the moment of capture
and
that
the storage system records
in
the immutable audit log
establishes
the data integrity
across
the lifecycle.
The trusted timestamp
that
[RFC 3161][ref_rfc_3161]
defines
anchors
the hash record
to
the verifiable time reference
that
the court can independently confirm
through
the timestamping authority.

The third element
is
the calibration record
that
the sensor manufacturer
or
the calibration laboratory
provides
for
the sensor at the time of capture.
A radiometric thermal imager
that
provides
the absolute temperature measurement
that
the post-mission analysis relies on
requires
the calibration record
that
the [ISO IEC 17025 accredited laboratory][ref_iso_17025]
issued
at
the most recent calibration
and
that
the [NIST traceability chain][ref_nist_traceability]
links
to
the primary standards
that
the National Institute of Standards and Technology maintains.

The programme manager
that
plans
the chain of custody
publishes
the standard operating procedure
that
the operator follows
at
each stage of
the data lifecycle,
from
the pre-flight platform check,
through
the in-flight data capture,
to
the post-flight download,
the archival,
and
the evidence production.
The [Scientific Working Group on Digital Evidence][ref_swgde]
publishes
the best practices
for
the digital evidence handling
that
the SAR programme adapts
to
the drone imagery context,
and
the [NIST SP 800-86 Guide to Integrating Forensic Techniques into Incident Response][ref_nist_800_86]
provides
the federal reference
that
the programme cites
in
the standard operating procedure.

### Records Retention and Public Records Implications

The data retention schedule
that
the SAR drone programme operates under
varies
by
the use case
that
the imagery serves
and
the regulatory regime
that
the operating agency belongs to.
A volunteer SAR programme
that
operates
under
no formal records management obligation
may retain
the imagery
indefinitely
in
the practical sense,
but
the same imagery
that
the law enforcement partner
ingests
into
the criminal case file
falls under
the records retention schedule
that
the partner's agency operates.
A federal SAR programme
that
the [Federal Records Act][ref_federal_records_act]
applies to
follows
the records schedule
that
the National Archives and Records Administration
approved
for
the agency.

The civilian SAR programme
that
shares
the imagery
with
the law enforcement partner
encounters
the public records request
that
the media,
the next of kin,
or
the interested public
files
under
the federal [Freedom of Information Act][ref_foia]
or
the equivalent state public records law.
The [FOIA Exemption 7(C)][ref_foia_exemption_7c]
provides
the principal protection
for
the personal privacy
of
the persons depicted in
the imagery,
which
the law enforcement agency
typically invokes
to redact
the faces,
the identifying clothing,
or
the other personally identifying details
that
the search imagery captures.
The state public records laws
operate under
the equivalent exemptions
that
the responding agency applies
in
the same way as
the federal exemption.

The programme manager
publishes
the records retention schedule
that
the operating agency adopts
as
the formal policy
that
the operator follows
and
the FOIA officer applies.
A typical retention schedule
that
the SAR drone programme adopts
distinguishes
the non-evidentiary imagery
that
the programme retains for
30 to 180 days
under
the body-worn camera retention norms
that
the [International Association of Chiefs of Police Body-Worn Camera framework][ref_iacp_bwc]
established
from
the evidentiary imagery
that
the programme retains for
the multi-year period
that
the criminal records schedule
that
the operating agency applies
imposes.

### State Drone Surveillance Laws

The state drone surveillance laws
impose
the use restrictions
and
the data handling restrictions
on
the SAR drone programme
that
operate
within
the state jurisdiction.
The state laws
vary substantially
across
the fifty states
and
the territories,
which means
the programme manager
that
operates
across multiple state jurisdictions
consults
the [National Conference of State Legislatures drone law tracker][ref_ncsl_drone_tracker]
for
the current state of
the law
in
each operating jurisdiction.

A representative sample
of
the state drone surveillance laws
that
the SAR programme encounters
includes
the [Florida Freedom from Unwarranted Surveillance Act in Florida Statute 934.50][ref_florida_drone_law]
that
restricts
the law enforcement use of
drones,
the [Texas Government Code Chapter 423][ref_texas_drone_law]
that
the Texas Privacy Act established
to govern
the drone capture of
images of
persons
and
private property,
the [Illinois Freedom from Drone Surveillance Act in 725 ILCS 167][ref_illinois_drone_law]
that
imposes
the warrant requirement
on
the law enforcement use of
drones
in
the most cases,
and
the [California Civil Code Section 1708.8 framework][ref_california_drone_law]
that
the 2015 Assembly Bill 856 amended
to extend
the physical invasion of privacy liability
into
the airspace above another person's land.

The SAR drone programme
that
operates
under
the public safety exception
that
most of the state laws provide
nonetheless
plans
the data handling workflow
to support
the warrant requirement,
the privacy exemption,
and
the data minimisation principle
that
the state laws impose
where
the search transitions from
the pure SAR mission
to
the law enforcement mission
that
the missing person investigation
sometimes becomes.

### Federal Procurement Restrictions and Data Residency

The federal procurement regime
imposes
the platform-level restrictions
that
the SAR drone programme
encounters
where
the programme receives
federal funding
or
the programme operates
in
the partnership with
the federal agency.
The [American Security Drone Act of 2023][ref_asda_2023],
incorporated into
the National Defense Authorization Act for Fiscal Year 2024,
restricts
the federal agency use of
the covered foreign UAS,
which
the Department of Defense interpretation
extends to
the federal grantee
that
operates
the covered platform
under
the federal grant.
The covered foreign UAS list
that
the [Defense Innovation Unit Blue UAS framework][ref_blue_uas]
governs
identifies
the vetted platforms
that
the federal grantee
can purchase
without
the further review,
with
the cleared platforms list itself
transitioned
in December 2025
from
the Defense Innovation Unit
to
the Defense Contract Management Agency
that
the operational list maintenance
now resides at.

The [DJI Local Data Mode][ref_dji_local_data_mode]
provides
the data residency option
that
the DJI Enterprise platforms support
to operate
without
the cloud connection
that
the default configuration uses,
which addresses
the data residency concern
that
the federal procurement regime
imposes
on
the DJI platforms
that
the [NDAA Section 848 of Fiscal Year 2020][ref_ndaa_848]
identified as
the covered foreign UAS.
The DJI Local Data Mode
does not
remove
the underlying platform
from
the covered foreign UAS list
that
the federal procurement regime targets,
but
the Local Data Mode
permits
the operator
to demonstrate
the data residency
that
the federal partner sometimes requires
as
the operating condition.

The SAR programme
that
operates
in
the federal partnership
typically migrates
to
the Blue UAS-listed platforms
over
the multi-year replacement cycle
that
the platform fleet operates under,
which means
the programme manager
that
plans
the multi-year acquisition
weights
the Blue UAS list
in
the platform selection
that
the A146 framework described,
and
matches
the sensor selection
that
the article describes
to
the platforms
that
the Blue UAS list approves.

### Cybersecurity Controls for the Data Infrastructure

The data infrastructure
that
the SAR drone programme operates
falls under
the cybersecurity controls
that
the operating agency adopts
for
the information system
that
the data resides in.
The federal SAR programme
that
operates
under
the federal information system
applies
the [NIST SP 800-53 Security and Privacy Controls for Information Systems and Organizations][ref_nist_800_53]
control baseline
that
the federal information system category
prescribes.
The federal grantee
that
operates
the non-federal information system
that
processes
the controlled unclassified information
that
the federal grant produces
applies
the [NIST SP 800-171 Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations][ref_nist_800_171]
control baseline
that
the Defense Federal Acquisition Regulation Supplement extends to
the federal grantee.

The Department of Defense contractor
or subcontractor
that
operates
the information system
that
processes
the controlled unclassified information
under
the Department of Defense contract
applies
the [Cybersecurity Maturity Model Certification][ref_cmmc]
that
the Department of Defense administers,
which assesses
the implementation of
the NIST SP 800-171 controls
at
the certification level
that
the contract requires.
The CMMC final procurement rule
became effective
on 10 November 2025
with
a phased three-year implementation,
and
the CMMC requirements
typically apply to
the Department of Defense contracts
rather than
the non-Department of Defense federal grants
that
the SAR programme more commonly operates under.
The SAR drone programme
that
operates
the cloud-hosted data infrastructure
under
the federal partnership
selects
the cloud service provider
from
the [Federal Risk and Authorization Management Programme][ref_fedramp]
list of authorised cloud service providers
that
the federal information system category permits.

The programme manager
that
plans
the cybersecurity controls
publishes
the system security plan
that
the operating agency adopts
as
the formal policy
that
the information system implements
and
the cybersecurity officer audits.
The civilian SAR programme
that
operates
without
the federal partnership
may
not be required
to apply
the federal control baselines,
but
the same controls
constitute
the recognised practice
that
the civilian programme
adopts
to provide
the data integrity,
the data confidentiality,
and
the data availability
that
the SAR mission relies on.

### Vendor Data Handling Policies

The cloud-class storage architecture
that
the SAR drone programme operates
depends on
the vendor data handling policies
that
the cloud platform vendor publishes.
The vendor data handling policies
specify
the data residency,
the data ownership,
the third-party sharing,
the law enforcement disclosure,
and
the data retention
that
the cloud platform applies
to
the imagery
that
the platform fleet uploads.

The DJI Enterprise cloud platform
operates under
the [DJI FlightHub 2 platform terms][ref_dji_flighthub]
that
the SAR programme accepts
when
the programme adopts
the DJI cloud workflow.
The DJI Local Data Mode
provides
the alternative
that
the programme adopts
where
the federal procurement regime
or
the state privacy law
restricts
the cloud upload.
The Skydio cloud platform
operates under
the [Skydio Cloud terms][ref_skydio_cloud]
that
the SAR programme accepts
when
the programme adopts
the Skydio workflow,
with
the data residency
in
the United States data centres
that
the Skydio cloud operates
matching
the federal procurement requirements
that
the Blue UAS-listed Skydio platforms meet.
The Parrot cloud platform
operates under
the [Parrot Cloud terms][ref_parrot_cloud]
that
the European Union General Data Protection Regulation governs.

The third-party data processing platforms
that
the SAR programme uses
for
the post-mission processing of
the lidar point cloud,
the photogrammetric mapping,
and
the multispectral analysis
include
[DroneDeploy][ref_dronedeploy],
[Pix4D][ref_pix4d],
and
[Esri Site Scan][ref_esri_site_scan],
each
operating under
the vendor terms of service
and
the data processing addendum
that
the SAR programme accepts.
The programme manager
that
plans
the data processing workflow
reviews
the data ownership clause,
the third-party sharing clause,
and
the data retention clause
that
each vendor publishes
to verify
the alignment with
the programme's data governance policy.

The Esri ArcGIS platform
operates under
the [Esri ArcGIS public-safety terms][ref_esri_arcgis]
that
many of the regional SAR command and control systems
already operate on,
which provides
the centralised data repository
that
the SAR programme integrates
the platform imagery into
through
the ArcGIS data ingest pipeline
that
the regional command and control
already operates.

### Calibration Records and Evidentiary Support

The calibration record
that
the chain of custody section established
as
the third element of
the evidentiary chain
deserves
the dedicated treatment
that
this section provides
because
the sensor calibration
underwrites
the scientific reliability
that
the [Daubert standard][ref_daubert]
imposes
on
the admissibility of
the sensor-based scientific evidence
under
the Federal Rules of Evidence
and
the equivalent state evidence rules.

The radiometric thermal imager
that
the programme deploys
requires
the periodic calibration
that
the [ISO IEC 17025 accredited calibration laboratory][ref_iso_17025]
performs
at
the calibration cadence
that
the sensor manufacturer specifies,
typically
the annual cadence
for
the field-deployed imager.
The lidar payload
requires
the boresight calibration
that
the manufacturer
or
the integrator performs
after
the assembly,
the major component replacement,
or
the suspected loss of calibration
that
the operating mishap suggests.
The multispectral and hyperspectral imagers
require
the spectral calibration
that
the manufacturer performs
at
the production
and
the periodic re-calibration
that
the laboratory or field calibration target supports.

The programme manager
that
plans
the calibration programme
maintains
the calibration record
for
each sensor
in
the asset management system
that
the operating agency uses
and
links
the calibration record
to
the imagery
that
the sensor captured
through
the metadata anchor
that
the chain of custody section described.
The calibration record
becomes
the evidentiary support
that
the sensor-based scientific evidence requires
under
the Daubert standard,
which
the prosecution or the defence
presents
in
the case
where
the imagery
becomes
the basis for
the criminal charge
or
the negligence claim.

## Sensor Mix by Mission Profile

The sensor mix
that
the SAR programme deploys
varies by
the mission profile
that
the operating environment imposes.
The table
that follows
maps
the principal mission profiles
to
the sensor combinations
that
the SAR programmes
in
the deployed-fleet survey
typically operate.

| Mission Profile | Primary Sensor | Secondary Sensor | Optional Sensor |
| --- | --- | --- | --- |
| Night Land Search | Thermal LWIR (mid tier) | Visible Low-Light | Loudspeaker |
| Day Land Search | Visible (mid tier) | Thermal LWIR (mid tier) | Multispectral |
| Forest Canopy Search | Thermal LWIR (upper tier) | Lidar (mid tier survey) | Hyperspectral |
| Water Surface Search | Thermal LWIR (mid tier) | Visible (mid tier) | Loudspeaker |
| Snow Search | Thermal LWIR (entry tier) | Visible (mid tier) | Loudspeaker |
| Wildfire Search | Thermal MWIR (cooled) | Multispectral SWIR | Visible (mid tier) |
| Urban Search | Visible (upper tier) | Thermal LWIR (mid tier) | Loudspeaker |
| Underwater Search | None airborne | Surface marker only | Underwater payload required |

The mission profile
that
the programme operates in
typically
determines
the primary sensor
that
the airframe carries
on each sortie.
The secondary sensor
provides
the confirmation capability
that
the primary detection requires
and
the optional sensor
provides
the supplementary capability
that
the specific operating environment
benefits from.
The programme
that
operates across
multiple mission profiles
typically
operates
multiple sensor configurations
that
the operator
switches between
according to
the active mission profile.

## Sensor Budget by Program Tier

The sensor budget
that
the SAR programme allocates
maps to
the five programme tiers
that
[A146][related_post_a146_buying]
established.
The table
that follows
describes
the sensor allocation
for
each tier.

| Tier | Programme Size | Sensor Budget Allocation | Sensor Mix |
| --- | --- | --- | --- |
| Tier 0 | Volunteer single-airframe programme | USD 3K to USD 10K total | Thermal LWIR entry + visible (entry tier) |
| Tier 1 | Small dedicated SAR programme | USD 10K to USD 50K total | Thermal LWIR mid + visible low-light (mid tier) |
| Tier 2 | Mid-sized regional SAR programme | USD 50K to USD 250K total | Thermal LWIR upper + visible (mid tier) + lidar (mid tier) |
| Tier 3 | Large urban or county SAR programme | USD 250K to USD 1M total | Multiple thermal cores + lidar (survey grade) + multispectral + loudspeaker |
| Tier 4 | Federal or interstate SAR programme | USD 1M+ total | Cooled MWIR + lidar (frontier tier) + hyperspectral + full sensor suite |

The sensor budget
for
each tier
is approximately
the same magnitude
as
the airframe budget
for
the same tier
that
[A146][related_post_a146_buying]
described.
The total platform cost
that
the programme manager budgets
is approximately
twice
the airframe-only budget
because
the sensor cost
and
the airframe cost
combined
constitute
the platform cost
that
the operating fleet
amortises
over the service life
of
the platform.

The article
recommends
the programme manager
treat
the sensor budget
as
a coequal line item
with
the airframe budget
in
the multi-year capital plan
because
the sensor obsolescence cycle
typically
runs
shorter than
the airframe obsolescence cycle
and
the sensor replacement
is the principal
mid-life capital expenditure
that
the platform fleet
incurs
between
the initial acquisition
and
the airframe retirement.

## Out of Scope

The article
treats
the sensor and payload selection
that
the SAR drone programme
considers
at
the buyer's decision level.
The following topics
are
out of scope.

The article
does not address
the operator training
on
the specific sensor configurations,
which
[A149][related_post_a149_training]
treated
in
the manufacturer-specific training section
that
each payload vendor
provides
through
the platform-specific training programme.

The article
does not address
the maintenance and lifecycle management
of
the sensor payloads,
which
the final article
in this series
will address
in
the context of
the broader platform maintenance programme
that
the SAR drone fleet
requires,
including
the periodic recalibration
that
the radiometric and survey-grade sensors require
and
the firmware lifecycle
that
the platform vendors
publish replacement schedules for.

The article
does not address
the machine learning detection algorithms
that
process
the sensor imagery
for
the automated detection
of
the search target.
The detection algorithms
constitute
a substantial research area
that
the [DRONERESPONDERS][ref_droneresponders_a150]
community
and
the academic SAR research partners
that
[A147][related_post_a147_rd]
described
collectively address.
The next-generation SAR drone platforms
will integrate
the detection algorithms
into
the sensor payload
and
the ground station
software
in
the ways
that
the current research will determine.

The article
does not address
the export control regime
that
the cooled MWIR thermal cores
and
the higher-grade lidar systems
operate under
beyond
the noting
that
the [International Traffic in Arms Regulations][ref_itar]
classify
the most sensitive cores
as
defence articles.
The programme manager
that
considers
the cooled-core payload
or
the survey-grade lidar
consults
the relevant export control counsel
before
the acquisition
to verify
the operating permissions
in
the operating jurisdictions.

The article
does not address
the specialised sensors
that
do not fit
the six categories
that
the article describes,
including
the chemical, biological, radiological, and nuclear sensors
that
the specialised SAR missions
in
the hazardous-environment operating regime
may require.
The specialised sensors
constitute
a separate sensor selection problem
that
the programme manager
addresses
through
the specialised vendor channels
that
the relevant federal hazardous-environment agencies
maintain.

The article
does not address
the underwater payload selection
that
the surface-launched diving drone platforms
operate.
The underwater payload
constitutes
a distinct sensor selection problem
that
the marine SAR programme
addresses
through
the specialised marine drone vendor channels
that
the relevant marine SAR programmes
maintain.

The article
does not address
the international sensor regulatory regimes
beyond
the noting
that
the European Union
operates
the [EASA UAS framework][ref_easa_uas_a150]
that
applies
to
the sensor payloads
in
the same way as
to
the airframes.
The international SAR programmes
that
operate
across multiple regulatory regimes
consult
the relevant national aviation authorities
for
the sensor-specific operating permissions
in
each operating jurisdiction.

## Conclusion

A SAR drone programme
that
plans
the multi-year capability investment
treats
the sensor selection
as
the principal
mission-capability decision
that
the programme manager makes
after
the airframe selection
and
the operator training framework
that
[A146][related_post_a146_buying]
and
[A149][related_post_a149_training]
described.
The sensor selection
determines
what
the platform
can detect
in
the operating environment
that
the mission profile imposes,
which determines
what
the programme can deliver
to
the search team
that
the platform supports.

The thermal imaging core
is
the single most
important sensor
that
the SAR drone carries
because
the missing person
emits
the infrared signature
that
the surrounding environment
typically does not match.
The visible camera
provides
the confirmation capability
that
the thermal detection requires
to distinguish
the human signature
from
the false positives
that
the rocks, animals, and surfaces produce.
The lidar
delivers
the canopy penetration
that
the thermal and visible sensors
cannot match
in
the forested terrain
that
the SAR mission frequently operates in.
The multispectral and hyperspectral
sensors deliver
the specialised spectral capability
that
the wildfire, water rescue, and ground anomaly applications
require.
The audio payload
delivers
the rescue communication
that
the search team uses
to direct
the missing person
to
safety.

The sensor budget
is
a coequal line item
with
the airframe budget
in
the multi-year capital plan
because
the sensor cost
typically equals
or exceeds
the airframe cost
in
the upper tiers
and
the sensor obsolescence cycle
typically runs
shorter than
the airframe obsolescence cycle.
A programme manager
that
plans
the platform fleet
without
the matching sensor budget
will discover,
within
the first replacement cycle,
that
the sensor capability
has fallen behind
the operating environment
that
the programme operates in,
which forces
the platform-and-sensor replacement
at the same time
when
only
the sensor replacement
would have sufficed
had
the original sensor capability
been better matched to
the operating environment.

The final article
in this series
will address
the maintenance and lifecycle management
of
the platform fleet,
covering
the airframe and sensor maintenance schedules,
the periodic recalibration that
the radiometric and survey-grade sensors require,
the firmware lifecycle that
the platform vendors publish replacement schedules for,
and
the multi-year total cost of ownership
that
the operating programme commits to.
Together
the articles
provide
a working reference
for
a budgeted entity
planning
the multi-year
investment
in a SAR drone capability
across
the airframe,
the operator training,
the sensor payload,
the sensor data management,
and
the maintenance programme
that
the mission-capable fleet requires.

## References

- [Reference, American Security Drone Act of 2023 FAR Final Rule][ref_asda_2023]
- [Reference, ASTM Committee F38 on Unmanned Aircraft Systems][ref_astm_f38]
- [Reference, California Civil Code Section 1708.8 as Amended by AB 856][ref_california_drone_law]
- [Reference, Carnegie Mellon Robotics Institute AirLab][ref_cmu_robotics]
- [Reference, Cubert ULTRIS Hyperspectral Imagers][ref_cubert]
- [Reference, Cybersecurity Maturity Model Certification][ref_cmmc]
- [Reference, DARPA OFFSET Program][ref_darpa_offset]
- [Reference, Daubert Standard for Admissibility of Scientific Evidence][ref_daubert]
- [Reference, Defense Innovation Unit Blue UAS Programme][ref_blue_uas]
- [Reference, DJI Enterprise Solutions][ref_dji_enterprise]
- [Reference, DJI FlightHub 2 Cloud Platform Terms][ref_dji_flighthub]
- [Reference, DJI Local Data Mode][ref_dji_local_data_mode]
- [Reference, DJI Payload SDK][ref_dji_psdk]
- [Reference, DJI SkyPort and X-Port Payload Mounts][ref_dji_skyport]
- [Reference, DJI Zenmuse Gimbal Family][ref_dji_zenmuse]
- [Reference, DJI Zenmuse L2 LiDAR Payload][ref_dji_zenmuse_l2]
- [Reference, DJI Zenmuse V1 Thermal-and-Loudspeaker Payload][ref_dji_zenmuse_v1]
- [Reference, DroneDeploy Cloud Mapping Platform][ref_dronedeploy]
- [Reference, DRONERESPONDERS][ref_droneresponders_a150]
- [Reference, DroneAudioset Benchmark][ref_droneaudioset]
- [Reference, EASA UAS Regulatory Framework][ref_easa_uas_a150]
- [Reference, Esri ArcGIS Public-Safety Platform][ref_esri_arcgis]
- [Reference, Esri Site Scan Drone Mapping][ref_esri_site_scan]
- [Reference, Federal Records Act][ref_federal_records_act]
- [Reference, Federal Risk and Authorization Management Programme][ref_fedramp]
- [Reference, Federal Rules of Evidence][ref_federal_rules_of_evidence]
- [Reference, Florida Freedom from Unwarranted Surveillance Act Statute 934.50][ref_florida_drone_law]
- [Reference, Freedom of Information Act][ref_foia]
- [Reference, FOIA Exemption 7(C) for Personal Privacy in Law Enforcement Records][ref_foia_exemption_7c]
- [Reference, Freefly MoVI Gimbal Family][ref_freefly_movi]
- [Reference, Gremsy Gimbal Family][ref_gremsy]
- [Reference, Headwall Photonics Hyperspectral Imagers][ref_headwall]
- [Reference, Hesai Pandar LiDAR Family][ref_hesai]
- [Reference, IACP Body-Worn Camera Framework][ref_iacp_bwc]
- [Reference, Illinois Freedom from Drone Surveillance Act 725 ILCS 167][ref_illinois_drone_law]
- [Reference, International Traffic in Arms Regulations][ref_itar]
- [Reference, ISO IEC 17025 Calibration Laboratory Accreditation][ref_iso_17025]
- [Reference, LightWare LiDAR][ref_lightware]
- [Reference, Livox LiDAR Family][ref_livox]
- [Reference, Lynred Infrared Detector Manufacturer][ref_lynred]
- [Reference, MIL-STD-704 Aircraft Electrical Power Characteristics][ref_mil_std_704]
- [Reference, MIL-STD-1275 Ground Vehicle 28 Volt Standard][ref_mil_std_1275]
- [Reference, MicaSense Altum-PT Multispectral Imager][ref_micasense_altum]
- [Reference, Motion Imagery Standards Board KLV Metadata][ref_misb]
- [Reference, NASA Earth Observatory][ref_nasa_earth_observatory]
- [Reference, National Conference of State Legislatures Drone Law Tracker][ref_ncsl_drone_tracker]
- [Reference, National Defense Authorization Act Section 848 of Fiscal Year 2020][ref_ndaa_848]
- [Reference, NIST Special Publication 800-53 Security and Privacy Controls][ref_nist_800_53]
- [Reference, NIST Special Publication 800-86 Guide to Integrating Forensic Techniques][ref_nist_800_86]
- [Reference, NIST Special Publication 800-171 Protecting Controlled Unclassified Information][ref_nist_800_171]
- [Reference, NIST Traceability Chain for Calibration][ref_nist_traceability]
- [Reference, Ouster LiDAR Family][ref_ouster]
- [Reference, Parrot Cloud Platform Terms][ref_parrot_cloud]
- [Reference, Phoenix LiDAR Systems][ref_phoenix_lidar]
- [Reference, Pix4D Drone Mapping Platform][ref_pix4d]
- [Reference, RFC 3161 Internet X.509 Public Key Infrastructure Time Stamp Protocol][ref_rfc_3161]
- [Reference, Riegl Survey LiDAR Family][ref_riegl]
- [Reference, SWGDE Best Practices for Drone Forensics][ref_swgde]
- [Reference, Sierra-Olympia Technologies][ref_sierra_olympia]
- [Reference, Sierra-Olympia Ventus Cooled MWIR Core][ref_sierra_olympia_ventus]
- [Reference, Skydio Cloud Platform Terms][ref_skydio_cloud]
- [Reference, Skydio Public-Safety Drones][ref_skydio_drones]
- [Reference, Sky Speaker-I from Yangda][ref_sky_speaker]
- [Reference, Sony Starvis Low-Light CMOS][ref_sony_starvis]
- [Reference, STANAG 4609 NATO Motion Imagery Standard][ref_stanag_4609]
- [Reference, Tarot Gimbal Family][ref_tarot]
- [Reference, Teledyne FLIR][ref_teledyne_flir]
- [Reference, Teledyne FLIR Boson Plus Thermal Core][ref_flir_boson]
- [Reference, Teledyne FLIR Hadron 640R Dual Payload][ref_flir_hadron]
- [Reference, Teledyne FLIR UAS Payloads][ref_flir_uas]
- [Reference, Texas Government Code Chapter 423 Use of Unmanned Aircraft][ref_texas_drone_law]
- [Reference, USGS Landsat Program][ref_usgs_landsat]
- [Reference, Workswell][ref_workswell]
- [Reference, Workswell WIRIS Pro Dual Payload][ref_workswell_wiris]
- [Reference, YellowScan Survey LiDAR Family][ref_yellowscan]
- [Related Post, A Buyer's Decision Framework for Search and Rescue Drones][related_post_a146_buying]
- [Related Post, Fixed-Wing Multicopter and Hybrid Drones for Search and Rescue Physics and Economics][related_post_a145_physics]
- [Related Post, Operator Training and Certification for a SAR Drone Program][related_post_a149_training]
- [Related Post, Research and Development for Search and Rescue Drones][related_post_a147_rd]
- [Related Post, Search and Rescue Drone Fleets by Geographic Setting][related_post_a148_geographic]

[ref_asda_2023]: https://www.federalregister.gov/documents/2024/11/12/2024-26061/federal-acquisition-regulation-prohibition-on-unmanned-aircraft-systems-from-covered-foreign
[ref_astm_f38]: https://www.astm.org/COMMITTEE/F38.htm
[ref_blue_uas]: https://www.diu.mil/blue-uas/framework
[ref_california_drone_law]: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1708.8.&lawCode=CIV
[ref_cmmc]: https://dodcio.defense.gov/CMMC/
[ref_cmu_robotics]: https://www.ri.cmu.edu/
[ref_cubert]: https://cubert-hyperspectral.com/
[ref_darpa_offset]: https://www.darpa.mil/research/programs/offensive-swarm-enabled-tactics
[ref_daubert]: https://www.law.cornell.edu/supremecourt/text/509/579
[ref_dji_enterprise]: https://enterprise.dji.com/
[ref_dji_flighthub]: https://www.dji.com/flighthub-2
[ref_dji_local_data_mode]: https://security.dji.com/data
[ref_dronedeploy]: https://www.dronedeploy.com/
[ref_dji_psdk]: https://developer.dji.com/doc/payload-sdk-tutorial/en/
[ref_dji_skyport]: https://developer.dji.com/payload-sdk
[ref_dji_zenmuse]: https://www.dji.com/products/zenmuse
[ref_dji_zenmuse_l2]: https://enterprise.dji.com/zenmuse-l2
[ref_dji_zenmuse_v1]: https://enterprise.dji.com/zenmuse-v1
[ref_droneaudioset]: https://arxiv.org/abs/2510.15383
[ref_droneresponders_a150]: https://www.droneresponders.org/
[ref_easa_uas_a150]: https://www.easa.europa.eu/en/domains/civil-drones/drones-regulatory-framework-background
[ref_esri_arcgis]: https://www.esri.com/en-us/industries/public-safety/overview
[ref_esri_site_scan]: https://www.esri.com/en-us/arcgis/products/site-scan-for-arcgis/overview
[ref_federal_records_act]: https://www.archives.gov/about/laws/fed-agencies.html
[ref_federal_rules_of_evidence]: https://www.law.cornell.edu/rules/fre
[ref_fedramp]: https://www.fedramp.gov/
[ref_flir_boson]: https://oem.flir.com/products/boson-plus
[ref_florida_drone_law]: http://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0900-0999/0934/Sections/0934.50.html
[ref_foia]: https://www.foia.gov/
[ref_foia_exemption_7c]: https://www.foia.gov/faq.html
[ref_flir_hadron]: https://oem.flir.com/products/hadron-640
[ref_flir_uas]: https://www.flir.com/browse/industrial/unmanned-systems/
[ref_freefly_movi]: https://store.freeflysystems.com/products/movi-xl
[ref_gremsy]: https://gremsy.com/
[ref_headwall]: https://headwallphotonics.com/
[ref_hesai]: https://www.hesaitech.com/
[ref_iacp_bwc]: https://www.theiacp.org/resources/policy-center-resource/body-worn-cameras
[ref_illinois_drone_law]: https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=3520&ChapterID=54
[ref_iso_17025]: https://www.iso.org/standard/66912.html
[ref_itar]: https://www.pmddtc.state.gov/ddtc_public?id=ddtc_public_portal_itar_landing
[ref_lightware]: https://lightwarelidar.com/
[ref_livox]: https://www.livoxtech.com/
[ref_lynred]: https://www.lynred.com/
[ref_mil_std_704]: https://en.wikipedia.org/wiki/MIL-STD-704
[ref_mil_std_1275]: https://en.wikipedia.org/wiki/MIL-STD-1275
[ref_micasense_altum]: https://ageagle.com/drone-sensors/altum-pt-camera/
[ref_misb]: https://nsgreg.nga.mil/misb.jsp
[ref_nasa_earth_observatory]: https://earthobservatory.nasa.gov/
[ref_ncsl_drone_tracker]: https://www.ncsl.org/transportation/current-unmanned-aircraft-state-law-landscape
[ref_ndaa_848]: https://www.congress.gov/bill/116th-congress/senate-bill/1790
[ref_nist_800_53]: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
[ref_nist_800_86]: https://csrc.nist.gov/pubs/sp/800/86/final
[ref_nist_800_171]: https://csrc.nist.gov/pubs/sp/800/171/r3/final
[ref_nist_traceability]: https://www.nist.gov/pml/owm/metrology/nist-traceability
[ref_ouster]: https://ouster.com/
[ref_parrot_cloud]: https://www.parrot.com/en/support/cloud
[ref_phoenix_lidar]: https://www.phoenixlidar.com/
[ref_pix4d]: https://www.pix4d.com/
[ref_rfc_3161]: https://datatracker.ietf.org/doc/html/rfc3161
[ref_riegl]: http://www.riegl.com/
[ref_sierra_olympia]: https://sierraolympia.com/
[ref_sierra_olympia_ventus]: https://sierraolympia.com/airborne-cameras/
[ref_sky_speaker]: https://www.yangdaonline.com/sky-speaker-i-megaphone-for-drones/
[ref_skydio_cloud]: https://www.skydio.com/cloud
[ref_skydio_drones]: https://www.skydio.com/
[ref_swgde]: https://www.swgde.org/documents/published-complete-listing/21-f-002-swgde-best-practices-for-drone-forensics/
[ref_sony_starvis]: https://framos.com/products-solutions/image-sensors/sony-starvis/
[ref_stanag_4609]: https://nso.nato.int/nso/zPublic/stanags/CURRENT/4609EFed01.pdf
[ref_tarot]: https://www.tarot-rc.com/
[ref_teledyne_flir]: https://www.flir.com/
[ref_texas_drone_law]: https://statutes.capitol.texas.gov/Docs/GV/htm/GV.423.htm
[ref_usgs_landsat]: https://www.usgs.gov/landsat-missions
[ref_workswell]: https://www.workswell.eu/
[ref_workswell_wiris]: https://workswell.eu/thermal-drone-camera-inspection-wiris-pro/
[ref_yellowscan]: https://www.yellowscan.com/compare-products/
[related_post_a145_physics]: {% post_url 2026-05-15-fixed_wing_multicopter_and_hybrid_drones_for_search_and_rescue %}
[related_post_a146_buying]: {% post_url 2026-05-16-buyers_decision_framework_for_search_and_rescue_drones %}
[related_post_a147_rd]: {% post_url 2026-05-17-research_and_development_for_search_and_rescue_drones %}
[related_post_a148_geographic]: {% post_url 2026-05-18-search_and_rescue_drone_fleets_by_geographic_setting %}
[related_post_a149_training]: {% post_url 2026-05-19-operator_training_and_certification_for_search_and_rescue_drone_programs %}
