---
layout: post
mathjax: true
comments: true
title: "Causality and First-Mover Advantage in Lightcone-Based Competitive Intergalactic Colonization"
date: 2026-03-01 01:39:41 +0000
categories: science philosophy
series: intergalactic_competition
series_title: Intergalactic Competition
series_index: 1
---
<!-- A98 -->
<script>console.log("A98");</script>

The observable universe is 13.8 billion years old
and contains an estimated two trillion galaxies.
Each of those galaxies contains hundreds of billions of stars,
and modern exoplanet surveys
have established that planetary systems
are the norm rather than the exception.
The Kepler space telescope alone
revealed that roughly 22 percent of Sun-like stars
host Earth-sized planets in their habitable zones,
suggesting that the Milky Way contains
on the order of 40 billion potentially habitable worlds.
The ingredients for life appear to be everywhere.
The time available for life to develop
has been enormous.
Yet no confirmed evidence
of extraterrestrial intelligence
has ever been detected.

This silence is the Fermi Paradox,
named after the physicist Enrico Fermi,
who posed the question informally over lunch
at Los Alamos National Laboratory in 1950.
The paradox is not that we have failed to find life.
The paradox is that
given the age and scale of the universe,
we should expect to find evidence of life everywhere
and instead find it nowhere.

This article argues
that the Fermi Paradox is not a paradox at all.
The Drake Equation is broadly correct
and its parameters are increasingly well-constrained.
Humanity is not special.
The universe almost certainly contains
other technological civilizations.
The reason we do not see them yet
is causality.
The speed of light imposes a hard boundary
on observable information,
and the distances involved
are so vast that civilizations
separated by millions of light-years
cannot detect each other
during the brief window
of their technological adolescence.

The thesis of this article is straightforward.
The argument proceeds
through a chain of increasingly constrained observations.
The Drake Equation's astrophysical parameters
are well-constrained
and support a universe rich in habitable worlds.
The oxygen bottleneck
and geological filters
plausibly delay technological civilizations
until relatively late in a planet's lifetime,
making us potentially among the first.
Causal isolation imposed by the speed of light
explains the observed silence
without requiring exotic hypotheses.
Thermodynamic constraints on computation and energy use
determine the observational signatures
of advanced civilizations,
and current surveys constrain only warm ones.
The competitive dynamics
of relativistic expansion
reward the first mover so heavily
that the outcome is effectively binary.
Under competitive expansion assumptions,
a civilization either leads
the colonization of its local volume
or faces the consequences
of another civilization
that moved first.

For evolutionary context,
the companion [Human Evolution and the Great Filter][related_post_great_filter]
article catalogs every major branching point
from the Last Universal Common Ancestor to Homo sapiens.
For cosmological context,
[Introduction to Astronomy][related_post_astronomy]
covers observational astronomy
and the mathematical formulas
for stellar distances, luminosity, and orbital mechanics.
For spaceflight context,
[Introduction to Space Studies][related_post_space_studies]
covers rocket propulsion, orbital mechanics,
and the history of space operations.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-03-01 01:39:41 +0000

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
```

## The Drake Equation

In November 1961,
astronomer Frank Drake convened a meeting
at the Green Bank Observatory in West Virginia
to discuss the prospects
for detecting extraterrestrial intelligence.
The ten attendees included Carl Sagan,
then a 27-year-old postdoctoral researcher,
the physicist Philip Morrison,
the dolphin communication researcher John Lilly,
and the Nobel laureate Melvin Calvin.
The attendees later adopted the name
"The Order of the Dolphin"
in honor of Lilly's interspecies communication work.

Drake wrote a single equation on the blackboard
to organize the discussion.
The equation estimates $N$,
the number of technological civilizations
currently capable of communication
in the Milky Way galaxy.

$$N = R_* \cdot f_p \cdot n_e \cdot f_l \cdot f_i \cdot f_c \cdot L$$

Each variable captures one factor
in the chain of conditions
required for a detectable civilization to exist.
$R_\*$ is the average rate of star formation
in the galaxy in stars per year.
$f_p$ is the fraction of those stars
that form planetary systems.
$n_e$ is the number of planets per system
that are capable of supporting life.
$f_l$ is the fraction of those planets
where life actually develops.
$f_i$ is the fraction of life-bearing planets
where intelligence evolves.
$f_c$ is the fraction of intelligent species
that develop detectable technology.
$L$ is the average lifetime
of such a technological civilization in years.

### Drake's Original Values

Drake and his colleagues
assigned estimates to each parameter
based on the best available knowledge in 1961.
They used $R_\* = 1$ star per year
as a conservative average
over the lifetime of the galaxy.
They estimated $f_p$ between 0.2 and 0.5,
meaning between one fifth and one half
of all stars would form planets.
They estimated $n_e$ between 1 and 5
habitable planets per planetary system.
They set $f_l = 1$,
considering the emergence of life
to be essentially inevitable
on habitable worlds.
They estimated $f_i = 0.01$
and $f_c = 0.01$,
and assumed $L = 10{,}000$ years.

The key conclusion from the 1961 meeting
was that $N \approx L$.
Using their minimum estimates
yielded approximately 20 civilizations.
Using their maximum estimates
yielded approximately 50 million.
The attendees concluded
that the Milky Way probably contained
between 1,000 and 100 million
civilizations capable of communication.

### Modern Parameter Estimates

Six decades of astronomical observation
have dramatically refined
the astrophysical parameters of the Drake Equation.
The biological and sociological parameters
remain deeply uncertain.

The modern estimate for $R_\*$
is between 1.5 and 3 stars per year,
based on infrared surveys from the Herschel Space Observatory
and gamma-ray measurements.
In terms of mass,
the Milky Way converts approximately 1.7 to 2.0 solar masses
of gas into stars each year.

The fraction of stars with planets $f_p$
has been revised upward to approximately 1.0.
Data from the Kepler space telescope
and the Transiting Exoplanet Survey Satellite, or TESS,
established that planets are the rule
rather than the exception.
Nearly every star has at least one planet.

The combined product $f_p \cdot n_e$
is now estimated at approximately 0.4,
based on Kepler data showing
that roughly 22 percent of Sun-like stars
host Earth-sized planets in their habitable zones.
This translates to approximately 40 billion
potentially habitable worlds in the Milky Way,
with 11 billion orbiting Sun-like stars specifically.

The biological parameters remain the weakest link.
Estimates for $f_l$ range from $10^{-9}$ to 1.0.
Modern estimates for $f_i$ range
from 0.003 percent to 0.2 percent,
dramatically more pessimistic
than Drake's original assumption
that intelligence was inevitable.
Estimates for $L$ range
from 50 years to one billion years,
with only one data point available.

### Dissolving the Paradox Through Uncertainty

A landmark 2018 paper
by Anders Sandberg, Eric Drexler, and Toby Ord
of the Future of Humanity Institute at Oxford
argued that the apparent paradox
arises from the common practice
of using point estimates
for highly uncertain parameters.
When realistic probability distributions
are applied instead,
spanning many orders of magnitude
for the most uncertain parameters,
the result is a substantial probability
that we are alone in the observable universe.
Their method yields approximately
a one-in-three probability
that we are alone in the Milky Way.

This finding does not mean we are alone.
It means that the uncertainty
in the Drake Equation parameters
is so large
that the observed silence
is not surprising
and does not require exotic explanations.

Brandon Carter's "hard steps" model
reinforces this conclusion
from an independent direction.
The model posits
that the emergence of intelligent life
requires passing through
a small number of extremely unlikely
evolutionary transitions,
each with a probability
so low that success is expected
only near the end
of a planet's habitable window.
Yet life on Earth appeared
after only 4.5 billion years
of a roughly 5.6-billion-year
habitable window,
suggesting that we are statistical outliers
who passed through the hard steps
ahead of the galactic average
rather than exemplars of a typical timeline.

### The Revised Drake Equation

Recent research has proposed additional factors
to improve the equation's predictive power.
A 2024 revision introduced $f_{oc}$,
the fraction of habitable exoplanets
with continents and oceans,
estimated between 0.0002 and 0.01.
The revision also introduced $f_{pt}$,
the fraction of those planets
with plate tectonics lasting more than 500 million years,
estimated at less than 0.17.
These geological filters
reduce the expected number of habitable worlds
by several orders of magnitude
relative to naive estimates based on orbital parameters alone.

## Why We Do Not See Anyone Yet

### Causality and the Speed of Light

The speed of light is not merely a speed limit
on the motion of physical objects.
It is the speed of causality itself.
No cause can produce an effect
anywhere in the universe
faster than light can travel the intervening distance.
Events outside one another's light cones
are mutually unobservable
and cannot be causally connected
by any known physical mechanism.

This constraint has direct implications
for the Fermi Paradox.
Even if advanced civilizations exist,
they may be causally disconnected from us.
An observer in the Andromeda Galaxy,
approximately 2.5 million light-years away,
sees Earth as it was 2.5 million years ago.
Conversely,
we see Andromeda as it was 2.5 million years ago.
Both civilizations could be technologically advanced right now,
yet neither would have any way to know
about the other.

### What Other Galaxies See When They Look at Earth

The Andromeda Galaxy, or Messier 31,
is the nearest large galaxy to the Milky Way
at a distance of approximately 2.537 million light-years.
The light currently arriving from Andromeda
left that galaxy 2.5 million years ago.
Symmetrically,
an observer in Andromeda looking at Earth today
would see Earth as it was 2.5 million years ago.

The period 2.5 million years ago
spans the Pliocene-Pleistocene boundary.
Australopithecus afarensis
was the predominant hominin species,
a small-brained, bipedal primate
with protruding facial features.
The earliest known stone tools,
the Oldowan industry,
date to approximately 2.9 million years ago
at sites in Nyayanga, Kenya.
These are the simplest stone tools,
consisting of basic flaked cobblestones.
Homo habilis,
one of the earliest members of the genus Homo,
appeared approximately 2.3 to 2.4 million years ago
in East and South Africa.

An observer in Andromeda
would therefore see a planet
with no cities, no agriculture,
and no detectable technology of any kind.
They would see small bipedal primates
using rudimentary stone tools
that would be indistinguishable
from natural rock formations
at any observational distance.
There would be no electromagnetic emissions,
no atmospheric pollution markers,
and no artificial structures.
Earth would appear
as an unremarkable rocky planet
with a biosphere
but with no signs of technological civilization.

The Triangulum Galaxy, or Messier 33,
is in a similar position
at approximately 2.73 million light-years.
An observer there would see Earth
at an even earlier stage,
before any member of the genus Homo existed.
The Large Magellanic Cloud
at 179,000 light-years
would see Earth
roughly when Homo sapiens
was first developing behavioral modernity.
The Small Magellanic Cloud
at 210,000 light-years
would see a similar picture.

From each of these perspectives,
Earth has nothing to report.
From our perspective,
each of those galaxies has nothing to report either.
Australopithecus-equivalents
may be roaming the most advanced planet
in the Andromeda Galaxy right now,
or a civilization
a million years more advanced than ours
may already control significant portions
of that galaxy.
We cannot tell the difference.
The information has not arrived yet.

### The Local Group

The Milky Way belongs to the Local Group,
a gravitationally bound cluster
of over 80 known galaxies
spanning roughly 10 million light-years.
The Local Group is dominated
by two large spirals,
the Milky Way and Andromeda,
and one medium spiral, Triangulum.
The remaining members are dwarf galaxies.
The following table summarizes
the major galaxies
relevant to the discussion
of intergalactic first-mover dynamics.
Distances and star counts
are approximate and vary by source.

| Name | Designation | Type | Distance | Diameter | Stars | SMBH | Notes |
|---|---|---|---|---|---|---|---|
| Milky Way | — | SBbc | — | ~100,000 ly | 100–400 billion | ~4 million $M_\odot$ | Home galaxy. Central SMBH is Sagittarius A*. |
| Sagittarius Dwarf | SagDEG | dSph/E7 | ~70,000 ly | ~10,000 ly | ~1 billion | None confirmed | Closest satellite. Being tidally disrupted and absorbed by the Milky Way. |
| Large Magellanic Cloud | LMC | SB(s)m | ~160,000 ly | ~32,000 ly | 20–30 billion | None confirmed | Nearest substantial intact galaxy. Naked-eye object from the Southern Hemisphere. |
| Small Magellanic Cloud | SMC / NGC 292 | SB(s)m pec | ~200,000 ly | ~19,000 ly | ~3 billion | None confirmed | Milky Way satellite. Naked-eye object from the Southern Hemisphere. |
| NGC 6822 | Caldwell 57 | IB(s)m | ~1,600,000 ly | ~7,000 ly | ~10 million | None confirmed | Barnard's Galaxy. Nearest non-satellite irregular galaxy to the Milky Way. |
| IC 10 | UGC 192 | dIrr | ~2,200,000 ly | ~5,000 ly | Unknown | None confirmed | Only starburst galaxy in the Local Group. Satellite of Andromeda. |
| M32 | NGC 221 | cE2 | ~2,490,000 ly | ~8,000 ly | ~3 billion | ~3 million $M_\odot$ | Compact elliptical. Andromeda satellite. Possibly a stripped remnant core. |
| Andromeda Galaxy | M31 / NGC 224 | SBb | ~2,540,000 ly | ~220,000 ly | ~1 trillion | ~100 million $M_\odot$ | Largest Local Group member. Approaching the Milky Way at ~110 km/s. |
| M110 | NGC 205 | dE5 pec | ~2,690,000 ly | ~17,000 ly | ~10 billion | None confirmed | Satellite of Andromeda. Contains young blue stars despite elliptical classification. |
| Triangulum Galaxy | M33 / NGC 598 | Sc | ~2,730,000 ly | ~60,000 ly | ~40 billion | None confirmed | Third largest Local Group member. No central bulge. High star formation rate. |

The resource asymmetry
within the Local Group is stark.
Andromeda contains roughly one trillion stars.
The Milky Way contains
100 to 400 billion.
Triangulum contains roughly 40 billion.
The Large Magellanic Cloud,
the nearest substantial intact galaxy,
contains 20 to 30 billion.
All other Local Group members
are dwarf galaxies
with comparatively negligible stellar populations.

For a civilization
pursuing intergalactic colonization
from the Milky Way,
the Large Magellanic Cloud
at approximately 160,000 light-years
represents the nearest major target.
At 10 percent of the speed of light,
a probe reaches the LMC
in 1.6 million years.
Andromeda at 2.5 million light-years
requires 25 million years at the same velocity.
These timescales are long
relative to human history
but short relative to geological
or stellar evolution timescales.

### The Temporal Coincidence Problem

Humanity has existed for roughly 300,000 years.
Detectable radio signals
have been emitted from Earth
for approximately 100 years,
since the 1920s.
Deliberate searches
for extraterrestrial intelligence, or SETI,
have been conducted only since 1960.

Even within the Milky Way,
where average distances
between hypothetical civilizations
might be on the order of 1,000 light-years,
meaningful two-way communication
requires both civilizations
to be technologically active
and listening simultaneously.
A civilization that arose one million years before us
and collapsed after 100,000 years
would have been undetectable to us
in every possible way.
A civilization that will arise
one million years from now
is equally invisible.

The window of temporal overlap
between any two technological civilizations
is vanishingly small
relative to the timescales involved.

### Quantum Communication and Observability

Latham Boyle of the University of Edinburgh
analyzed interstellar quantum communication
in a 2024 paper
and demonstrated
that quantum communication channels
impose far more stringent requirements
than classical radio.
To achieve non-zero quantum channel capacity
between Earth and Proxima Centauri,
the nearest star system at 4.24 light-years,
transmitting and receiving telescopes
would need effective diameters
exceeding 100 kilometers.
No existing or planned telescope approaches this scale.

Boyle argued
that if advanced civilizations
prioritize quantum over classical communication,
they would possess telescopes
capable of determining
that we lack sufficient receiving technology.
Sending quantum communications to us
would serve no purpose
until we develop sufficiently large receivers.
This offers an additional resolution to the paradox.
Advanced civilizations may be communicating
through channels we cannot yet access.

## The Oxygen Bottleneck

### Fire as a Prerequisite for Technology

Amedeo Balbi of the University of Roma Tor Vergata
and Adam Frank of the University of Rochester
published a 2024 paper in Nature Astronomy
titled "The Oxygen Bottleneck for Technospheres"
that identified atmospheric oxygen concentration
as a critical constraint
on the emergence of technological civilizations.

The paper distinguishes
between two different oxygen thresholds.
Complex biology,
including multicellular organisms
and potentially intelligent creatures,
can emerge at oxygen levels
well below present atmospheric levels.
Research suggests that organisms
comparable to advanced metazoans
require oxygen partial pressures
of approximately $10^3$ to $10^4$ pascals,
substantially below the current level
of approximately 21,000 pascals
at 21 percent of one atmosphere.

Technology is a different matter entirely.
Open-air combustion,
which is indispensable
for metallurgy, smelting, ceramics,
and eventually industrial energy production,
requires an oxygen partial pressure
of at least 18 percent.
Below 18 percent,
ignition and sustained combustion
in open-air conditions become unreliable.
Below 16 percent,
combustion is likely not feasible at all.

The implications are significant.
A planet could in principle host intelligent life
that nonetheless remains permanently stuck
at a pre-technological stage
if atmospheric oxygen
never crosses the combustion threshold.
Without fire,
a species cannot forge metal for tools or antennas,
generate the combustion necessary to launch rockets,
burn fossil fuels for power generation,
or fire lasers into the sky.
Such civilizations would be intelligent
but technologically inert
and largely undetectable
by any current SETI methodology.

### Earth's Oxygenation Timeline

Earth's atmospheric oxygen history
unfolded in distinct stages
over approximately four billion years.

**The Anoxic Archean.**
For approximately the first two billion years
of Earth's 4.5-billion-year history,
the atmosphere contained
essentially no free oxygen.
It was a weakly reducing atmosphere
dominated by nitrogen, carbon dioxide,
methane, and water vapor.

**The Great Oxidation Event.**
Approximately 2.4 billion years ago,
cyanobacteria evolved oxygenic photosynthesis,
producing molecular oxygen
as a byproduct of water photolysis.
Oxygen began accumulating in the atmosphere
but reached only about 1 to 10 percent
of present atmospheric levels,
corresponding to roughly 0.2 to 2 percent O$_2$.
This event is also called the Oxygen Catastrophe
because it was lethal
to many anaerobic organisms.

**The Boring Billion.**
After the Great Oxidation Event,
oxygen levels plateaued
at extremely low values
for approximately one billion years,
from 1.8 to 0.8 billion years ago.
Oxygen concentrations may have been
as low as 0.1 percent of modern levels,
corresponding to roughly 0.02 percent O$_2$.
The oceans remained largely anoxic and euxinic.
Despite these harsh conditions,
critical evolutionary innovations occurred,
including the emergence of eukaryotic cells,
multicellularity, and sexual reproduction.
However,
the evolution of complex animal life
was effectively stalled.

**The Neoproterozoic Oxygenation Event.**
Between approximately 850 and 540 million years ago,
oxygen levels rose significantly,
possibly triggered by the breakup
of the supercontinent Rodinia,
Snowball Earth episodes in the Cryogenian,
and increased nutrient delivery to the oceans.
Oxygen may have reached 10 to 18 percent
of present atmospheric levels
by the late Neoproterozoic.

**The Rise to Modern Levels.**
The earliest fossil charcoal,
found in rocks from Wales and Poland,
dates to approximately 430 million years ago,
implying that atmospheric oxygen
had crossed at least 13 to 16 percent by that time.
Near-modern oxygen levels were reached
between the mid-Silurian and mid-Devonian,
approximately 430 to 390 million years ago,
driven in part by the colonization of land
by vascular plants
and the appearance of the first forests
around 390 million years ago.
Oxygen reached approximately 20 percent
around 350 million years ago
and peaked at approximately 35 percent
during the late Carboniferous and early Permian,
the highest levels in Earth's history.

**The Critical Window.**
Earth's atmosphere has been steadily above 18 percent oxygen,
the threshold for reliable open-air combustion,
for only about 200 million years.
Even during the Phanerozoic,
flammability may have switched off completely
for periods of tens of millions of years,
particularly around 180 to 200 million years ago
when oxygen levels may have dipped
below the combustion threshold.

Out of Earth's 4.5-billion-year history,
the window for technology-capable civilizations
has existed for less than 10 percent
of the planet's age,
and for less than 1.5 percent
of the time Earth has had an oxygenated atmosphere.

### First-Generation Intelligent Life

David Catling of the University of Washington
and colleagues published a seminal 2005 paper
in the journal Astrobiology
demonstrating that Earth's "oxygenation time,"
defined as the time required
to reach an oxygen partial pressure
of approximately $10^4$ pascals,
was approximately 3.9 billion years.
This falls within a factor of two
of the Sun's main-sequence lifetime
of approximately 10 billion years.
Oxygenation is therefore a rate-limiting step
that could preclude complex life
on planets orbiting shorter-lived stars,
including F-type stars.

Abraham Loeb of Harvard University,
together with Rafael Batista and David Sloan,
published a 2016 paper arguing
that life on Earth
may be premature from a cosmic perspective.
If red dwarf stars
of approximately 0.1 solar masses
can host habitable planets,
then life is approximately 1,000 times more likely
to arise in the far future,
up to 10 trillion years from now,
than it is today.
The habitable cosmic epoch
began approximately 30 million years after the Big Bang
and will end approximately 10 trillion years from now.

Multiple converging lines of evidence
support the hypothesis
that technologically capable intelligent life
may be a first-generation phenomenon.
Rocky planets could not form
until stellar nucleosynthesis
had enriched the interstellar medium
to at least 10 percent of solar metallicity,
requiring multiple generations of stellar evolution.
Earth-like planets could not have formed
until approximately 8 to 10 billion years
after the Big Bang.
If other Earth-like planets
require a similarly long oxygenation time
of approximately 4 billion years,
then the earliest possible emergence
of technology-capable species on other worlds
would be roughly contemporaneous
with Earth's timeline,
not billions of years earlier.

The Boring Billion further supports this argument.
A one-billion-year stagnation
of oxygen levels on Earth
suggests that even on a planet
where photosynthetic oxygen production
is well-established,
reaching the levels needed for complex life
is not guaranteed to proceed
on any particular timescale.

The oxygen bottleneck
should be understood
as a plausible delay mechanism
rather than a proven universal law.
Earth's oxygenation history
is contingent on factors
that may not generalize.
Plate tectonics,
which drives the carbon-silicate cycle
that regulates atmospheric composition,
may itself be rare among rocky planets.
The combustion threshold
imposes an additional constraint
beyond what is required
for complex biology alone.
Technological windows
may therefore be narrow
relative to planetary lifetimes,
supporting the hypothesis
that we are plausibly among the first
without establishing it as certain.

## The Kardashev Scale

### Measuring Civilizational Advancement

In 1964,
the Soviet astronomer Nikolai Kardashev
proposed a classification system
for advanced civilizations
based on their total energy consumption.
The scale defines three types.

A Type I civilization
harnesses the total energy
available on its planet,
approximately $4 \times 10^{16}$ watts
for an Earth-like world.
A Type II civilization
harnesses the total energy output of its parent star,
approximately $3.8 \times 10^{26}$ watts
for a Sun-like star.
A Type III civilization
harnesses the total energy output of its galaxy,
approximately $4 \times 10^{37}$ watts.

Carl Sagan later proposed a continuous interpolation
using the formula $K = \frac{\log_{10}(P) - 6}{10}$,
where $P$ is the civilization's power consumption in watts
and $K$ is the Kardashev rating.

### Where Humanity Stands

Zhang and colleagues published a 2023 paper
in Scientific Reports
using machine learning models
to forecast humanity's progression
on the Kardashev Scale.
Using random forest
and autoregressive integrated moving average models,
they determined
that humanity currently stands
at approximately Type 0.73.
Their projections indicate
that global energy consumption
will reach on the order of 900 exajoules by 2060,
corresponding to a Kardashev rating
of approximately 0.74.

Humanity currently uses
approximately 0.16 percent
of the total solar energy
available on Earth's surface.
To reach Type I,
humanity would need to harness
approximately 10,000 times more energy
than its current consumption.

### Projected Advancement Timelines

Estimates for the time required
to advance on the Kardashev Scale
vary enormously
depending on assumptions
about growth rates
and technological breakthroughs.

**Type 0 to Type I.**
The physicist Michio Kaku estimated
100 to 200 years
assuming an average energy consumption growth rate
of approximately 3 percent per year.
Freeman Dyson estimated approximately 200 years.
Jonathan Jiang and colleagues
published a 2022 paper
titled "Avoiding the Great Filter"
that placed the transition at the year 2371,
with a range of 2333 to 2404,
accounting for fossil fuel depletion,
renewable energy growth,
and environmental constraints.
The Zhang 2023 machine learning study concluded
that if current energy strategies persist,
reaching Type I could take millennia.

**Type I to Type II.**
Kardashev himself estimated
approximately 3,200 years.
Kaku estimated "a few thousand years."
The key prerequisite
is the development of von Neumann replicators,
self-reproducing factories
that can build copies of themselves.
Stuart Armstrong and Anders Sandberg
of the Future of Humanity Institute at Oxford
demonstrated
that once von Neumann replicator technology exists,
a Dyson swarm could be constructed
by disassembling Mercury for materials
in approximately 31 years
through exponential self-replication.

**Type II to Type III.**
Kardashev estimated approximately 5,800 years,
though this assumes uninterrupted exponential growth.
Kaku estimated 100,000 to one million years.
Frank Tipler calculated in 1980
that self-replicating von Neumann probes,
traveling at less than 1 percent of the speed of light
with a replication rate of 10,000 probes per year,
could colonize the entire Milky Way galaxy
in less than 300 million years.
At 10 percent of the speed of light,
the timeline contracts
to as little as 500,000 to 4 million years.

### Technological Advancement is Exponential Until It Is Not

These projections assume
that exponential growth in energy consumption
can be sustained indefinitely.
There are strong reasons to believe
it cannot.

Tom Murphy of the University of California, San Diego
demonstrated
that at a sustained 2.3 percent annual energy growth rate,
humanity would require
energy equivalent to the Sun's total output
within 1,400 years.
Well before that point,
waste heat alone would make Earth uninhabitable.
If humanity generated Sun-comparable power
on Earth's surface,
the surface temperature would need to exceed
the surface temperature of the Sun
to radiate that energy,
because Earth's surface area
is smaller than the Sun's.

Balbi and Lingam published a 2024 paper
in the journal Astrobiology
demonstrating
that if energy growth rates
remain at approximately 1 percent per year,
the maximal lifetime
of such technospheres
is ephemeral compared to stellar evolution timescales.
Waste heat production
is an inevitable consequence of thermodynamics.

Kardashev himself noted
that exponential growth
is a transitional phase
in the development of a civilization,
inevitably limited by natural factors.

The resolution to this apparent constraint
is that advancement on the Kardashev Scale
does not require exponential growth
on a single planet.
A civilization transitions from Type 0 to Type I
by harnessing its planet's resources,
from Type I to Type II
by expanding into its stellar system
and constructing energy-harvesting megastructures,
and from Type II to Type III
by colonizing its galaxy.
Each transition involves spatial expansion,
not merely intensification of energy use
on a single body.

## Galactic-Scale Engineering

### Dyson Swarms

Freeman Dyson proposed in 1960
that a sufficiently advanced civilization
would eventually construct
a swarm of orbiting solar collectors
that partially or fully enclose its parent star.
A Dyson swarm absorbs visible-spectrum starlight
and converts it to useful energy.
The inevitable waste heat
is re-emitted as thermal infrared radiation
at temperatures typically between 100 and 600 kelvins,
producing emission peaks
in the mid-infrared band
at roughly 5 to 30 micrometers.

Armstrong and Sandberg demonstrated
in their 2013 paper "Eternity in Six Hours,"
published in Acta Astronautica,
that a Dyson swarm
could be bootstrapped
from a single seed of one square kilometer
of solar panels on Mercury.
Through exponential self-replication
of mining, manufacturing, and deployment systems,
Mercury could be completely disassembled
in approximately 31 years.
The title refers to the amount
of the Sun's energy output
needed to initiate the project,
approximately six hours of solar luminosity.

### Matrioshka Brains

Robert Bradbury proposed the Matrioshka brain in 1997
as a hierarchy of concentric Dyson-like shells.
Each shell absorbs waste heat
from the shell inside it,
performs computation,
and radiates at a lower temperature.
The innermost shell
absorbs starlight at thousands of kelvins.
Each successive shell
operates at progressively lower temperatures.
The outermost shell radiates into space.

The thermodynamic efficiency of the entire system
is determined by the temperature
of the outermost shell,
not the star.
If the outer shell radiates
at a temperature near
the cosmic microwave background temperature
of 2.725 kelvins,
the Carnot efficiency approaches

$$\eta = 1 - \frac{T_{cold}}{T_{hot}} = 1 - \frac{2.725}{T_{star}}$$

For a Sun-like star
with $T_{star} \approx 5{,}778$ kelvins,
this gives approximately 99.95 percent efficiency.

However,
Jason Wright of Penn State University
demonstrated in a 2023 paper
in the Astrophysical Journal
that for computation at the Landauer limit,
nested shells provide little to no advantage
over a single optimally designed shell.
The optimal strategy
is to build very small, very hot Dyson spheres.
The Matrioshka brain concept remains relevant
for dissipative activities
such as hosting biospheres
but does not provide
the computational advantages
originally anticipated.

### Star Lifting

Star lifting is the hypothetical removal
of material from a star for industrial use
or stellar life extension.
The concept was first proposed by David Criswell in 1985.
The extracted material emerges as plasma jets
composed primarily of hydrogen and helium.

Several mechanisms have been proposed.
Thermal-driven outflow
uses a partial shell of solar collectors
to reflect starlight
back onto localized regions of the photosphere.
The concentrated heating
causes the chromosphere to expand,
producing eruptions similar to solar flares
that achieve escape velocity.
Electromagnetic polar extraction
establishes a ring current around the star's equator,
generating a powerful toroidal magnetic field
with dipoles over the rotational poles.
This field deflects the enhanced solar wind
into two collimated jets along the rotational axis.
The "Huff-n-Puff" method
modulates the magnetic field
to periodically squeeze the star,
propelling stellar atmosphere
through polar magnetic nozzles.

Using 10 percent of the Sun's total power output
would permit lifting approximately
$5.9 \times 10^{21}$ kilograms of matter per year,
roughly 8 percent of the Moon's mass annually.

### Creating Artificial Red Dwarf Stars

The extracted hydrogen and helium
from star lifting operations
can be separated and repurposed.
Purified hydrogen can be compressed
to ignition conditions
to create small, fully convective red dwarf stars.

Red dwarfs below approximately 0.35 solar masses
lack a radiative core.
Their entire interior is convective,
meaning bulk plasma flows
continuously circulate material
between the core and the surface.
This prevents helium accumulation at the core
and allows the star
to burn a far larger fraction
of its total hydrogen supply
before leaving the main sequence.

The lifespans of fully convective red dwarfs
are extraordinary.
A 0.1 solar mass red dwarf
may remain on the main sequence
for 6 to 12 trillion years,
more than 400 times the current age of the universe.
Adams, Bodenheimer, and Laughlin predicted in 1997
that after exhausting most of their hydrogen
over trillions of years,
fully convective red dwarfs
would gradually increase in surface temperature
and luminosity,
transitioning through a "blue dwarf" phase
rather than becoming red giants.
No blue dwarfs exist yet
because the universe is far too young.

A civilization could in principle
disassemble a single Sun-like star
of 1.0 solar masses
into roughly 10 fully convective red dwarfs
of 0.1 solar masses each.
Although each would be far dimmer than the Sun,
producing roughly 0.001 solar luminosities,
the aggregate energy output
over trillions of years
would vastly exceed
the Sun's total main-sequence energy budget.
This represents a strategy
of trading power for duration.

The helium extracted during star lifting
or accumulated as fusion ash
could be stored in artificial gas giant planets,
used as construction material,
potentially fused in future fusion reactors
using helium-3 as a candidate fuel,
or ejected from the stellar system.

Scoggins and Kipping published a 2023 paper
in the Monthly Notices
of the Royal Astronomical Society
conducting the first numerical investigation
of star lifting as a stellar life extension strategy
using the MESA stellar evolution code.
Stars initially below approximately 0.4 solar masses
can have their main-sequence lifetimes extended
up to 500 billion years
as they are gradually reduced
toward the hydrogen burning limit
of approximately 0.08 solar masses.
For a Sun-like star,
star lifting can extend the main-sequence lifetime
by up to 3 billion years.

### Other Galaxy Optimization Strategies

Beyond star lifting and artificial star creation,
several additional strategies
could optimize a galaxy's energy budget.

**Black hole energy harvesting.**
A "reverse Dyson sphere" concept
involves a civilization orbiting a black hole
and dumping high-entropy waste energy into it.
The black hole acts as an entropy sink,
and the civilization harvests low-entropy energy
from the cosmic microwave background.
Inoue and Yokoo analyzed this scenario
in a 2021 paper
in the Monthly Notices
of the Royal Astronomical Society.
The key thermodynamic insight
is that life depends on the income of energy
with low entropy
and the disposal of energy with high entropy.

**Stellar migration.**
Rather than waiting
for gravitationally bound stars
to drift into optimal configurations over billions of years,
a civilization could use star lifting
to modify stellar orbits
and concentrate useful stars
into energy-efficient clusters.

**Planetary disassembly.**
Gas giants contain enormous reserves
of hydrogen and helium
that could be extracted
and compressed into artificial stars
or used as fusion fuel.
Rocky planets could be disassembled
for construction materials
for megastructures.

## Ghost Galaxies

### Stars That Go Dark

If a Type III civilization
encloses most or all stars in a galaxy
within Dyson swarms or Matrioshka brains,
the galaxy would dim in visible light
while brightening dramatically in the infrared
due to waste heat emission.
The visible stars would effectively vanish.
Such a galaxy is a "ghost galaxy,"
a gravitationally bound system
with the mass and gravitational signature
of a normal galaxy
but without the expected visible starlight.

The transition from visible to ghost
would be gradual.
A civilization expanding outward
from its home system
would enclose stars progressively,
producing a galactic "dimming front"
that an external observer could detect
as a region of the galaxy
losing visible stars
while gaining infrared emission.

### What We Have Looked For

The Glimpsing Heat from Alien Technologies survey,
or G-hat,
led by Jason Wright at Penn State University,
conducted the most systematic search to date
for Type III Kardashev civilizations.
The survey used data
from the Wide-field Infrared Survey Explorer,
or WISE, satellite.

Wright and colleagues published
a series of papers beginning in 2014.
Paper I established the theoretical framework
for detecting waste heat
from alien energy supplies.
Paper II developed a formalism
for translating mid-infrared photometry
into quantitative upper limits
on extraterrestrial energy supplies.
Paper III examined approximately 100,000 galaxies
resolved by WISE
for extreme mid-infrared emission.

The key result was definitive.
Zero galaxies in the sample
hosted a civilization
reprocessing more than 85 percent
of starlight into mid-infrared waste heat.
Only 50 galaxies,
including the ultraluminous infrared galaxy Arp 220,
showed mid-infrared luminosities
consistent with greater than 50 percent reprocessing.
These placed the first empirical upper limits
on the prevalence of galaxy-spanning civilizations.

In 2024,
Matias Suazo and colleagues
published the Project Hephaistos study,
examining approximately 5 million stellar sources
using Gaia, Two Micron All Sky Survey,
and WISE photometry
to search for partial Dyson spheres
around individual stars.
They identified 7 strong candidates,
all M-dwarf stars,
exhibiting unexplained infrared excess.
Natural explanations such as warm debris disks
remain plausible
but are considered rare around M-dwarfs.
M-dwarf stars are also prone
to extreme stellar flares
that strip planetary atmospheres
and irradiate surface environments,
providing a natural filter
that makes technological emergence
on the most common stellar type
substantially less likely.
This further supports
the hypothesis
that G-type stars like the Sun
may constitute the primary habitat
for technologically capable civilizations.

### What We Might See in the Future

If a civilization
in a nearby galaxy
is currently in the process
of constructing Dyson swarms
around its stars,
the dimming would be observable
only after the light from that era reaches us.
A galaxy at 10 million light-years
that began dimming 5 million years ago
would appear normal to us today.
The dimming front has not arrived.

This observation connects directly
to the causality argument.
We may not yet see ghost galaxies
not because they do not exist,
but because the light
from the pre-dimming era
is still the most recent information we have.
Future astronomers may observe
galaxies that begin to go dark,
one star at a time,
region by region,
as the expansion front
of a Type III civilization
becomes visible across intergalactic distances.

If we observe such dimming
in a galaxy closer to us
than the stage of technological development
that dimming implies,
the situation is grave.
That civilization
had a head start.
The first mover has already won
the volume of space it occupies.

## Waste Heat and Masking Strategies

### The Thermodynamic Constraint

The second law of thermodynamics
requires that any energy-harvesting
or computational process must reject waste heat.
There is no physical process
that converts energy to work
with 100 percent efficiency.
This applies universally to Dyson swarms,
Matrioshka brains,
and any other megastructure.

Rolf Landauer established in 1961
that the erasure of one bit of information
requires a minimum energy dissipation of

$$E_{min} = k_B T \ln(2)$$

where $k_B$ is Boltzmann's constant
($1.381 \times 10^{-23}$ joules per kelvin),
$T$ is the absolute temperature
of the thermal reservoir in kelvins,
and $\ln(2) \approx 0.693$.
At room temperature of 300 kelvins,
this equals approximately $2.9 \times 10^{-21}$ joules
per bit erased.
This was experimentally confirmed in 2012
by Berut and colleagues in the journal Nature.

Any irreversible computation
necessarily generates waste heat.
The only theoretical escape
is fully reversible computing,
which preserves all input information
in the output and never erases bits.
Reversible computing faces severe practical challenges.
It requires storing the complete computational history,
and any interaction with the external environment,
including input, output, and error correction,
introduces irreversibility.

### Masking at the Cosmic Microwave Background Temperature

The most widely discussed concealment strategy
involves engineering the outermost radiating surface
of a megastructure
to emit at or near the cosmic microwave background temperature
of 2.725 kelvins.
A Matrioshka brain with its outermost shell
radiating at the cosmic microwave background temperature
would be nearly indistinguishable
from the cosmic microwave background itself.

At intergalactic distances,
such a structure would appear
as a point-like source
of microwave or millimeter-wave emission
at the cosmic microwave background temperature.
It would be effectively invisible
against the cosmic microwave background
in spectral surveys.
It could potentially be detectable only
as an occulting object
that blocks background sources.
It would remain entirely undetectable
by current mid-infrared surveys like WISE,
which are sensitive
to temperatures of roughly 100 to 600 kelvins.

The Stefan-Boltzmann law dictates
that radiated power scales as $T^4$.
Extremely low radiating temperatures
require extremely large surface areas.
A sphere radiating at the cosmic microwave background temperature
would need to be orders of magnitude larger in radius
than a conventional Dyson sphere
to dissipate the same power,
subject to extreme engineering challenges
in constructing and maintaining
a structure of that scale.

### Other Concealment Approaches

A "reverse Dyson sphere"
dumps high-entropy waste energy
into a black hole,
which acts as an entropy sink.
However,
the accretion of matter and energy
into a black hole
can produce observable effects of its own.

A civilization could engineer
its waste heat signature
to resemble natural astrophysical phenomena,
such as a circumstellar dust disk,
a young stellar object,
or a brown dwarf.
The Project Hephaistos results
illustrate this ambiguity
from the observer's perspective.
The seven Dyson sphere candidates identified
could plausibly be explained
by warm debris disks.

A civilization could distribute
its infrastructure across many stars,
keeping the energy fraction
harvested from each star
low enough to remain
within natural variability.
This would make detection
by surveys like G-hat extremely difficult.

Reversible computing reduces
but cannot eliminate
the thermodynamic signature.

A civilization's detectability surface
is ultimately determined
by its radiators.
Every joule of useful work
eventually becomes waste heat
that must be radiated into space.
A civilization that has won its local cluster
might eventually migrate
its computational infrastructure
to the galactic halo
to maximize the surface area
available for heat rejection,
reducing the temperature
of each radiating element
and blending more effectively
into the cosmic microwave background.

### Super-Efficient Matrioshka Brains at a Distance

A Matrioshka brain
operating near thermodynamic optimality
and radiating waste heat
at or near the cosmic microwave background temperature
would be virtually undetectable
at intergalactic distances
using any currently available technology.
The waste heat would blend
into the cosmic microwave background itself.

At galactic distances within the Milky Way,
detection would be more plausible
because the structure
would occult background stars
and produce a measurable gravitational signature.
However,
at megaparsec scales,
a civilization
that has optimized its waste heat management
would be indistinguishable from empty space
to any instrument we currently possess.

This means that the G-hat survey result,
finding zero Type III civilizations
in 100,000 galaxies,
constrains only civilizations
that radiate waste heat
at temperatures between 100 and 600 kelvins.
A civilization radiating at 10 kelvins or below
would evade detection entirely.
The survey tells us
that no galaxy nearby
hosts a "warm" Type III civilization.
It does not tell us
that no galaxy nearby
hosts a "cold" one.

However,
even a cold Type III civilization
would retain a gravitational signature.
A galaxy with the mass of a trillion suns
but the luminosity of a void
would be detectable
through gravitational lensing effects,
anomalous rotation curves in neighboring galaxies,
and its influence on the large-scale structure
of the local cosmic web.
A ghost galaxy
would appear as dark matter
to observers who lack
the instrumentation to resolve
its low-temperature thermal emission.
Future surveys designed
to cross-correlate mass and luminosity
at galactic scales
could in principle distinguish
dark-matter-dominated galaxies
from those whose starlight
has been intercepted by megastructures.

## The Solitude Zone

Antal Veres of the Hungarian University of Agriculture
published a 2025 paper in Acta Astronautica
titled "The Solitude Zone:
A Probabilistic Window for Singular Lifeform Existence"
that introduced a statistical framework
for estimating whether Earth
is the only civilization
at its current technological level.

The model incorporates four core principles.
Complexity ranks lifeforms
on a scale from zero to infinity,
from single-celled organisms
to postbiological intelligence.
Existence likelihood
captures the probability
that a civilization of minimum complexity exists.
Emergence probability
captures the chance
that such a lifeform arises in only one system.
The number of potential systems
is estimated at $10^{24}$ terrestrial planets
across the observable universe.

The framework defines the Solitude Zone
as the statistical window
where the probability of exactly one civilization
at a given technological level
exceeds both the probability of multiple civilizations
and the probability of zero civilizations.
Veres estimates roughly 29 to 30 percent probability
that humanity occupies the Solitude Zone.
This likelihood never surpasses 50 percent
at our current technological level
but increases significantly
for more advanced civilizations.

As a civilization climbs the Kardashev scale,
solitude becomes more likely.
Ultra-advanced societies of Type II or III
may have a higher probability of being alone,
not because others do not exist,
but because they reach states
where communication, detectability,
or even shared physics
may diverge so significantly
that contact becomes impossible.

## The Grabby Aliens Model

Robin Hanson of George Mason University,
together with Daniel Martin, Calvin McCarter,
and Jonathan Paulson,
published a 2021 paper
titled "If Loud Aliens Explain Human Earliness,
Quiet Aliens Are Also Rare."
The paper addresses a puzzle
that arises from the standard "hard steps" model
of advanced life timing.

Under the hard steps model,
the emergence of intelligent life
requires passing through $n$ extremely unlikely
evolutionary transitions.
Life should therefore be far more likely
to appear near the end
of a planet's habitable lifetime.
Yet humanity appeared
after only about 4.5 billion years
of Earth's approximately 5.6-billion-year habitable window.
Humanity appeared surprisingly early.

The Grabby Aliens model
resolves this earliness puzzle
by positing that expanding civilizations
set a deadline.
Life cannot emerge
within volumes already claimed
by "grabby" civilizations.
This compresses the window
for new civilizations to appear,
making our apparently early arrival
a natural consequence of the model
rather than an anomaly.

The model has only three free parameters,
each estimable to within a factor of four
from existing data.
The hard steps power $n$
is estimated between 3 and 12,
with a central estimate of 6.
The expansion speed $s$
is estimated at or above
half the speed of light.
The appearance constant $k$
is estimated by assuming
our date of appearance
is a random sample
from the distribution
of grabby civilization appearance dates.

The model predicts
that grabby civilizations appear
roughly once per million galaxies.
They currently control
approximately 40 to 50 percent
of the observable universe.
Each grabby civilization will eventually control
between 100,000 and 30 million galaxies.
Humanity,
if it becomes grabby,
would encounter the nearest grabby civilization
in roughly 200 million to 2 billion years,
with a central estimate
of approximately 1 billion years.

A selection effect
explains why we do not see grabby civilizations
even though the model predicts they control
a substantial fraction of the universe.
If they expand at near light speed,
their expansion front is only slightly behind
the light that would reveal their origin.
We cannot see them
until they are nearly upon us.

These predictions
depend on the assumed expansion speed,
the number of hard steps,
and the appearance constant.
The universe coverage fraction
is particularly sensitive to expansion speed.
At half the speed of light,
each grabby civilization claims
a large volume before encountering neighbors.
At lower speeds,
the coverage fraction decreases
and the encounter timeline extends.
The model's qualitative conclusions
are robust across parameter ranges,
but the specific numerical predictions
should be treated
as order-of-magnitude estimates
rather than precise forecasts.

## First Mover Wins

### The Hart-Tipler Conjecture

Michael Hart published a foundational paper in 1975
in the Quarterly Journal
of the Royal Astronomical Society
arguing that if any extraterrestrial intelligence
had arisen in the Milky Way,
it would have had ample time
to develop interstellar travel
and colonize nearby stars.
Those colonies would spawn
further colonization efforts,
eventually filling the galaxy.
Since there is no evidence of such a civilization,
Hart argued humanity is alone.

Frank Tipler extended this argument in 1980,
demonstrating that self-replicating von Neumann probes
could colonize the entire Milky Way
in less than 300 million years.
This is less than 5 percent
of the current age of the galaxy.
The argument was further developed
in the book "The Anthropic Cosmological Principle"
by Tipler and John Barrow.

Even the most conservative estimates
indicate that a single civilization
could have filled the galaxy
many times over
within the galaxy's lifetime.

### The Colonization Wavefront

Armstrong and Sandberg
demonstrated in "Eternity in Six Hours"
that a single star-spanning civilization
could launch a colonization project
for the entire reachable universe
using modest energy and resources.
The process involves
constructing a partial Dyson shell
by disassembling Mercury,
then launching self-replicating probes
at half light speed or greater
to every reachable galaxy.
Upon arrival,
each probe disassembles a planet,
builds a Dyson swarm,
and launches a new wave of probes
to every star in that galaxy.
This approach could reach approximately 4 billion galaxies.

Carroll-Nellenback, Frank, Wright, and Scharf
published a 2019 paper
in the Astronomical Journal
modeling settlement dynamics
including the role of stellar motions
as a diffusive component
to the colonization wavefront.
They demonstrated
that the Milky Way can be filled
with settled stellar systems
under conservative assumptions
about interstellar spacecraft velocities
and launch rates.

### What Evidence of Advanced Life Means

The thesis of this article reduces to a simple test.

Consider a galaxy at distance $d$ light-years.
The light we receive from that galaxy
shows us what that galaxy looked like
$d$ years ago.
If that galaxy shows evidence
of a technological civilization
that is more advanced
than humanity was $d$ years ago,
then that civilization had a head start.

For the Andromeda Galaxy at 2.5 million light-years,
this means the comparison is against
what humanity was doing 2.5 million years ago.
Since Australopithecus was using
rudimentary stone tools 2.5 million years ago,
any evidence of electromagnetic emissions,
atmospheric engineering,
or stellar-scale energy harvesting
in Andromeda's current light
would indicate a civilization
millions of years ahead of us.

Such a civilization
would have had sufficient time
to begin expanding through its local volume.
If it expands at even 1 percent of light speed,
it would have expanded
25,000 light-years in 2.5 million years.
At 10 percent of light speed,
250,000 light-years,
more than twice the diameter of the Milky Way.

Under competitive expansion assumptions,
the dynamics of exponential expansion
mean that whoever starts first
claims the resources
of the local cluster.
Second place becomes strategically unstable.
The colonization wavefront
converts available matter
into infrastructure for the expanding civilization.
Stars that have been enclosed in Dyson swarms
and planets that have been disassembled
for construction materials
are no longer available
to later arrivals.

This first-mover analysis
rests on identifiable assumptions
that should be stated explicitly.
It assumes that civilizations
are expansionist
rather than self-limiting.
It assumes competitive resource acquisition
rather than cooperative sharing.
It assumes the absence
of stable coordination equilibria
that might prevent expansion races.
And it assumes
that no universal attractor exists
toward non-expansionist behavior.
These assumptions are not proven.
They represent one end
of a spectrum of possible
civilizational dispositions.
The analysis that follows
is conditional on these premises.

It may be 5 million years
before the future Type III leader
of the local cluster
is performing resource acquisition sweeps
of neighboring volumes.
But from a civilizational perspective,
the question is binary.
We would rather be the leader
of the local cluster
than discover that someone else already is.

The current absence of evidence
does not tell us that no one else exists.
It tells us that the information
has not arrived yet.
We do not see ghost galaxies.
We do not see anomalous dimming.
We do not see mid-infrared excess
in nearby galaxies
consistent with galaxy-spanning energy harvesting.
The G-hat survey found nothing.

These observations show us
what those galaxies looked like
millions of years ago.
The silence we observe
is the silence of the past.
If a civilization in Andromeda
began constructing Dyson swarms
one million years ago,
we will not see the dimming
for another 1.5 million years.
The absence of evidence
is not evidence of absence.
It is a consequence
of the finite speed of information.

This is why evidence of advanced life,
should it ever appear
in the light arriving from a nearby galaxy,
would be the most alarming observation
in the history of science.
That light would show us
the past state of a civilization
that is now $d$ years more advanced
than what we observe.
If that past state already exceeded
our current capabilities,
the situation is strategically grave.
Under competitive expansion assumptions,
the first mover has already claimed
the volume between us,
and we cannot observe the claim
until the colonization wavefront
is nearly upon us.
Unless that civilization
has self-destructed in the intervening years,
the outcome may already be determined.

### Intergalactic Sterilization

According to known physics,
a directed-energy sterilization sweep
would propagate at the speed of light.
A relativistic particle beam
or concentrated gamma-ray burst
directed at a target galaxy
would travel at or near $c$.
The critical consequence
is that the target galaxy
cannot detect the sweep
until the moment it arrives.
Light from the sweep
and the sweep itself
travel at the same velocity.

An expanding civilization
could perform a sterilization sweep
and dispatch intergalactic colonization bootstrappers
immediately afterward.
The bootstrappers,
constrained to subluminal velocities,
would arrive after the sweep
has cleared the target galaxy
of any competing biosphere.
The target galaxy is sterilized and then seeded.

However,
the preparation for such a sweep
would be visible
before the sweep itself arrives.
If the attacking civilization
spent $P$ years assembling
the energy infrastructure
required to sterilize a target galaxy,
then the target galaxy
would observe $P$ years
of preparation activity
before the sweep arrives.
The preparation light
reaches the target first
because it was emitted first.
The sweep follows behind,
arriving at the same instant
as the light from its own launch.

Let $d$ represent the one-way light travel time
in years between two galaxies,
and let $P$ represent the duration
of the preparation phase.
The target galaxy begins observing
the attacker's preparations
at time $d$ after they commence.
The sweep arrives at time $d + P$.
The warning window is therefore

$$t_{\text{warning}} = P$$

A sterilization sweep
that takes millions of years
to cross intergalactic distances
still arrives faster than biological evolution
can produce a technological response.
Evolution operates on timescales
of hundreds of thousands to millions of years.
A pre-technological biosphere
has no possible countermeasure.
A civilization that detects
incoming preparations
would need to develop defenses
within the warning window
or face extinction.

**The sterilization engine.**
A Type III civilization
that has fully harnessed its galaxy
possesses an energy source
of extraordinary magnitude
at the galactic center.
The Milky Way's central supermassive black hole,
Sagittarius A*,
has a mass of approximately
$4.3 \times 10^6$ solar masses.
A spinning black hole
stores rotational energy
that can be extracted
through the Penrose process
or the Blandford-Znajek mechanism.

The maximum rotational energy
extractable from a Kerr black hole
with mass $M_{\text{BH}}$
and dimensionless spin parameter $a_\*$ is

$$E_{\text{rot}} = \left(1 - \sqrt{\frac{1 + \sqrt{1 - a_*^2}}{2}}\right) M_{\text{BH}} c^2$$

For a maximally spinning black hole
with $a_\* = 1$, this reduces to

$$E_{\text{rot,max}} = \left(1 - \frac{1}{\sqrt{2}}\right) M_{\text{BH}} c^2 \approx 0.293 \, M_{\text{BH}} c^2$$

For Sagittarius A*
at $M_{\text{BH}} \approx 4.3 \times 10^6 \, M_\odot$,
the extractable rotational energy
is approximately $2.3 \times 10^{53}$ joules.
For context,
the total gravitational binding energy of Earth
is approximately $2.2 \times 10^{32}$ joules.
The extractable rotational energy
of a single supermassive black hole
could unbind approximately $10^{21}$
Earth-mass planets.
Even distributed across a target galaxy
of 100 billion star systems,
each system would receive
approximately $2.3 \times 10^{42}$ joules,
far exceeding any plausible
sterilization threshold.

The Blandford-Znajek process
provides the astrophysically relevant mechanism
for sustained energy extraction.
A spinning black hole
immersed in a magnetic field
anchored by an accretion disk
generates an outward Poynting flux
along the rotation axis,
producing a collimated relativistic jet.
The power of this jet scales as

$$P_{\text{BZ}} \propto a_*^2 \, B^2 \, M_{\text{BH}}^2$$

where $B$ is the magnetic field strength
at the horizon.
Observed astrophysical jets
from active galactic nuclei
achieve Lorentz factors of 10 to 50,
corresponding to velocities exceeding 0.99$c$,
with intrinsic opening angles
of 1 to 10 degrees.

A Type III civilization
that has engineered
the accretion environment
of its central supermassive black hole
could, assuming sufficiently advanced beam control,
direct a relativistic jet
of arbitrary duration
at a target galaxy,
delivering sterilizing fluence
at effectively the speed of light.
The jet serves simultaneously
as the sterilization mechanism
and as the fastest possible delivery vehicle.
No separate propulsion system is required.
The sterilization sweep
is a beam of energy,
not a fleet of ships.

At intergalactic distances,
beam divergence works in the attacker's favor.
A relativistic jet with an opening angle
of even one degree
subtends a cone
that at 2.5 million light-years
covers a cross-section
far exceeding the diameter
of a typical galaxy.
The jet is a shotgun,
not a sniper rifle.
Precision aiming at individual star systems
is unnecessary.
The entire target galaxy
falls within the beam.

For a target galaxy
without a technological civilization,
the question is moot.
The sweep arrives
before technology evolves to detect it.
This is the ultimate expression
of first-mover advantage.
The first civilization to achieve
intergalactic reach
can preemptively sterilize
every galaxy within its expanding light cone,
seeding each with its own biology
and ensuring that no competitor ever arises.

### The Asymmetry of Intergalactic Warfare

The speed of light
creates a profound asymmetry
between offense and defense
at intergalactic distances.
This asymmetry emerges
from the nature of pseudo-realtime observation.

Consider two peer civilizations,
$A$ and $B$,
separated by distance $d$ light-years.
Each civilization continuously receives
a stream of light from the other,
delayed by $d$ years.
This constitutes pseudo-realtime observation.
Each side watches the other's activities unfold
with a $d$-year lag,
as if viewing a delayed broadcast.
Interactions within this stream
are causally coupled
with a $d$-year period.
Everything that occurred
more recently than $d$ years ago
at the other civilization's location
is unreceived
and must be left to conjecture.

**Offensive challenge.**
At time $t$,
civilization $A$ observes civilization $B$
as $B$ existed at time $t - d$.
To estimate $B$'s current capabilities,
$A$ must extrapolate $d$ years of advancement
beyond the last observation.
If $A$ launches an attack at time $t$
traveling at the speed of light,
the attack arrives at $B$ at time $t + d$.
$A$ must therefore extrapolate
an additional $d$ years
for $B$'s advancement during the attack's transit.
The total offensive gap is

$$\Delta_{\text{offense}} = 2d \text{ years of extrapolated development}$$

The first $d$ years
account for advancement
from the observed state
to the target's present state.
The second $d$ years
account for advancement
during the attack's transit.
For Andromeda at $d = 2.5 \times 10^6$ light-years,
this gap is 5 million years.
The entirety of hominin evolution
from Australopithecus to the present day
spans less than 4 million years.
An intergalactic attack
must cut through technological progress
exceeding the entire span
of human evolutionary history
beyond the last observation.

However,
offense holds one critical advantage.
Information is hidden until it arrives.
Civilization $B$ cannot observe
$A$'s activities
during the most recent $d$ years.
Any weapons, strategies, or technologies
developed during that window
remain unknown to $B$
until the light carrying that information
reaches $B$.
The attacker can exploit
this information asymmetry
by deploying capabilities
that the defender has never observed
and could not have anticipated.

**Defensive advantage.**
Defense operates in observable pseudo-realtime.
Civilization $B$ continuously watches
civilization $A$'s activities
through the incoming light stream,
delayed by $d$ years.
If $A$ begins preparing for an attack,
$B$ observes those preparations
and can begin developing countermeasures
immediately.

When $A$'s attack arrives at $B$,
the attack reflects $A$'s capabilities
as they were at the time of launch,
$d$ years ago.
$B$ observes the attack arriving
in the $d$-year delayed observation stream
and sustains it
as $A$ sent it $d$ years prior.
$B$ is now $d$ years more advanced
than the state $A$ targeted,
and $B$ has been watching $A$'s preparations
unfold throughout the entire buildup.
The defender's advantage is

$$\Delta_{\text{defense}} = d \text{ years of post-observation advancement}$$

The incoming attack was designed
to defeat an obsolete version
of the defending civilization.
The defender has had $d$ years of development
that the attacker could not have known about.
Furthermore,
the defender has been observing
the attacker's preparations in pseudo-realtime
and can tailor countermeasures
to the specific threat observed.

**The causal interaction window.**
The distinction
between pseudo-realtime observation
and conjecture
is the primary driver of intergalactic border stability.
It is not a consequence
of limited intelligence or technology.
It is a structural property of relativistic spacetime.
No improvement in sensor technology
or computational power
can eliminate the $d$-year delay.
The pseudo-realtime observation stream
implies that intergalactic interactions
are causally coupled
with a $d$-year period,
where $d$ is the one-way light-travel time
between the two civilizations.
Observable causal interactions
unfold in pseudo-realtime.
Unreceived interactions,
those within the most recent $d$ years,
remain unknown
and must be left to conjecture.
Defense benefits
from the observable pseudo-realtime stream
because preparations can be watched
and countermeasures developed accordingly.
Offense benefits
from the unreceived window
because hidden developments
cannot be anticipated by the defender.

For Andromeda at $d = 2.5 \times 10^6$ light-years,
the causal interaction period
is 2.5 million years.
Each side would observe the other's actions
with a 2.5-million-year delay
but in a continuous, unbroken stream.
The offensive gap of 5 million years
and the defender's 2.5-million-year head start
make sustained intergalactic conflict
between peer civilizations
extraordinarily protracted
and extraordinarily difficult
for the aggressor.

### Colonizing the Light Cone

The interplay of sterilization capability
and the $2d$-year offensive gap
produces a natural model
for intergalactic expansion.

An expanding Type III civilization
colonizes its light cone.
It sterilizes each target galaxy
with a directed-energy sweep
traveling at the speed of light,
then dispatches subluminal colonization bootstrappers
to seed the cleared volume.
This process continues outward,
galaxy by galaxy,
as the civilization's light cone expands.

Against pre-technological biospheres,
this process encounters no resistance.
The sterilization sweep arrives
before technology evolves to detect it.
The $2d$-year offensive gap
does not apply
because there is no peer
to have advanced.
Against a world of single-celled organisms
or early hominins,
the question of defensive advantage
does not arise.

The expansion continues
until the sterilization front
encounters a galaxy
harboring a civilization
capable of withstanding the sweep.
At that point,
the dynamics shift
from uncontested expansion
to peer Type III intergalactic conflict.
The $2d$-year offensive gap
and the pseudo-realtime defensive advantage
come into full effect.
The aggressor's sterilization sweep,
designed based on intelligence
that is $d$ years old at best,
must contend with a defender
that has been watching the approaching wavefront
in pseudo-realtime
and preparing accordingly.

The strategic implication
of this model is stark.
The moment a civilization detects
a potentially competitive intergalactic rival,
it should assume
that a sterilization sweep
is already en route.
The rival would have launched the sweep
upon first detecting evidence
of a potential competitor.
Seed colonizers would follow
immediately behind the sweep.
The detection itself
is the warning.

This produces an intergalactic landscape
of expanding spheres of control,
each centered on a civilization
that achieved Type III status
and began colonizing its light cone.
These spheres expand
until they collide with one another.
The boundaries between them
become zones of peer conflict
where the $2d$-year offensive gap
enforces a kind of stalemate,
with each side unable to project
decisive force
across the intervening distance.

**Intergalactic topography.**
These expanding spheres
would not expand uniformly.
Galaxies are not distributed evenly
through space.
The large-scale structure of the universe
forms a cosmic web
of filaments, walls, clusters, and voids.
Filaments are thread-like structures
connecting galaxy clusters
and containing roughly half
of all matter in the universe.
Voids are vast underdense regions
occupying approximately 80 percent
of the universe by volume,
with typical diameters ranging
from 30 to 300 million light-years.

An expanding civilization
would colonize along filaments
and through clusters
far more rapidly
than it could cross voids.
Filaments provide a continuous chain of galaxies
that serve as stepping stones
for the sterilize-and-seed process.
Voids offer no such intermediate targets.
The expansion front
would therefore be highly irregular,
tracing the cosmic web topology
rather than expanding
as a uniform sphere.

The Milky Way's Local Group
lies on the periphery
of the Virgo Supercluster,
itself a subsystem
within the Laniakea Supercluster,
which spans approximately 520 million light-years
and contains roughly 100,000 galaxies.
The Local Void,
measuring approximately 75 million light-years across,
borders the Local Group.
A civilization expanding from the Local Group
would spread along the filament
toward the Virgo Cluster
far more readily
than it would cross the Local Void.

The boundaries of competing civilizations
would form along the natural fault lines
of intergalactic topology.
Voids would serve as natural barriers.
Filaments would serve as corridors of expansion.
The zones of peer conflict
predicted by the $2d$-year offensive gap
would follow this same topology,
concentrating along filament boundaries
where expanding spheres of control collide.

## Conclusion

The Fermi Paradox is best understood
not as evidence of cosmic emptiness
but as a consequence of cosmic geometry.
The argument proceeds
through a chain of increasingly constrained steps.
The Drake Equation's astrophysical parameters
are well-constrained
and support a universe
rich in potentially habitable worlds.
The oxygen bottleneck and geological filters
plausibly delay technological civilizations
until relatively late in a planet's lifetime.
Causal isolation imposed by the speed of light
is sufficient to explain the observed silence
without requiring exotic hypotheses
about alien behavior or motivation.
Thermodynamic constraints
determine what advanced civilizations look like,
and current surveys constrain
only warm ones.
The competitive dynamics
of relativistic expansion
create severe first-mover advantages
under competitive assumptions.
Each link in the chain
builds on the previous one,
and each is grounded
in established physics
or well-constrained observation.

We see Andromeda as it was
during the age of Australopithecus.
Andromeda sees us the same way.
The information has not arrived yet.
This is the most defensible
and least speculative element of the thesis.
Silence is expected
under causal isolation.
Observability is asymmetric.
We may be early locally
even if not globally.

The Grabby Aliens model
predicts that expanding civilizations
may already control
a substantial fraction of the observable universe,
though the specific coverage fraction
depends on model parameters.
The G-hat survey found no evidence
of galaxy-spanning civilizations
in 100,000 nearby galaxies,
but this result constrains only warm civilizations
radiating waste heat
between 100 and 600 kelvins.
Cold civilizations radiating near
the cosmic microwave background temperature
would be invisible to current instruments.

Under competitive expansion assumptions,
the strategic implications
of first-mover advantage
in galactic colonization are severe.
Whoever expands first
colonizes their light cone,
sterilizing and seeding each target galaxy
before any competing technological civilization arises.
A sterilization sweep traveling at the speed of light,
in principle delivered via engineered relativistic jet,
arrives before any pre-technological biosphere
can mount a response.
This expansion continues
until the wavefront encounters resistance
from a peer civilization
capable of withstanding the preliminary sweep.

At that boundary,
the dynamics shift
to intergalactic conflict
governed by the $2d$-year offensive gap
and pseudo-realtime defensive observation.
Defense operates
in an observable pseudo-realtime stream,
watching the attacker's preparations unfold
with a $d$-year delay
and developing countermeasures accordingly.
Offense must extrapolate $2d$ years
of the target's advancement
but benefits from information
hidden within the unreceived $d$-year window.
This asymmetry is not a limitation
of technology or intelligence.
It is a structural property of relativistic spacetime
that cannot be overcome
by any known physical mechanism.
The result is a landscape
of expanding spheres of control
that collide and stabilize
into zones of protracted peer conflict,
tracing the topology
of the cosmic web.

Counterarguments to this framework
deserve acknowledgment.
Civilizations may converge
on non-expansionist equilibria,
preferring inward development
or post-biological computation
over territorial expansion.
Coordination or signaling regimes
might emerge among early civilizations,
preventing competitive expansion races.
The simulation hypothesis
offers an alternative framing entirely,
though it is not necessary
to invoke it
when the observed silence
has a sufficient physical explanation.
These possibilities
cannot be ruled out from first principles.
The competitive expansion model
represents one end
of a spectrum of civilizational dispositions.
It is the end
that carries the most severe consequences
if it applies to even one civilization
in our light cone.

The Grabby Aliens model
introduces a deadline
to the analysis.
If expanding civilizations exist,
they are consuming the available volume
at a rate determined
by their expansion speed.
The window for quiet civilizations,
those that do not expand,
is being progressively closed
by grabby ones.
If long-term survival
is the objective,
stagnation is not a neutral choice.
It is an existential risk.
A civilization that does not expand
reduces the unreceived window
from which information might arrive
and cannot influence the outcome
if a competitive expander
already occupies its future light cone.

The current silence is therefore
both reassuring and urgent.
Reassuring because the absence of evidence
in arriving light
is consistent with the hypothesis
that we are among the first
technological civilizations in our local volume.
Under worst-case competitive assumptions,
the moment evidence of a rival appears,
it implies extreme strategic risk.
The detection itself is the warning.

If we are first,
and if long-term survival is the objective,
the path forward is expansion.
Not because the universe is hostile,
but because by expanding our own light cone
we reduce the unreceived window
from which a sterilization sweep could emerge.
The information confirming
whether we are first
has not yet arrived.
The risk asymmetry
favors the civilization that moves
over the civilization that waits.

## Future Reading

- The [Glimpsing Heat from Alien Technologies survey][research_ghat] provides the most comprehensive empirical constraints on Type III civilizations.
- [Eternity in Six Hours][research_eternity] demonstrates the feasibility of universal colonization from a single star system.
- [The Oxygen Bottleneck for Technospheres][research_oxygen_bottleneck] establishes atmospheric oxygen as a rate-limiting factor for technological civilizations.
- [If Loud Aliens Explain Human Earliness, Quiet Aliens Are Also Rare][research_grabby_aliens] presents the Grabby Aliens model and its implications for SETI.
- [Dissolving the Fermi Paradox][ref_dissolving_fermi] demonstrates that parameter uncertainty alone can explain the observed silence.

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- Hsiao, Tiger Yu-Yang, Tomotsugu Goto, Tetsuya Hashimoto, et al. 2021. "A Dyson Sphere around a Black Hole." *Monthly Notices of the Royal Astronomical Society* 506: 1723–32. [https://academic.oup.com/mnras/article/506/2/1723/6312510][ref_dyson_black_hole]
- Scoggins, Matthew T., and David Kipping. 2023. "Lazarus Stars: Numerical Investigations of Stellar Evolution with Star-Lifting as a Life Extension Strategy." *Monthly Notices of the Royal Astronomical Society* 523: 3251–57. [https://academic.oup.com/mnras/article/523/3/3251/7188305][ref_lazarus_stars]

### Primary Sources, Non-Peer-Reviewed

- Armstrong and Sandberg. n.d. *Eternity in Six Hours*. [https://www.sciencedirect.com/science/article/abs/pii/S0094576513001148][ref_eternity_six_hours]
- Balbi, Amedeo, and Adam Frank. 2023. "The Oxygen Bottleneck for Technospheres." Preprint, . [https://arxiv.org/abs/2308.01160][research_oxygen_bottleneck]
- Balbi and Lingam. n.d. "Waste Heat and Habitability." Preprint, . [https://arxiv.org/html/2409.06737][ref_waste_heat_habitability]
- Carroll-Nellenback, Jonathan, Adam Frank, Jason Wright, and Caleb Scharf. 2019. "The Fermi Paradox and the Aurora Effect: Exo-Civilization Settlement, Expansion and Steady States." Preprint, . [https://arxiv.org/abs/1902.04450][ref_aurora_effect]
- Carter, Brandon. 2008. "Five- or Six-Step Scenario for Evolution?" *International Journal of Astrobiology* 7 (2): 177–82. [https://doi.org/10.1017/s1473550408004023][ref_carter_hard_steps]
- Drake Equation. n.d. *SETI Institute*. [https://www.seti.org/research/seti-101/drake-equation/][research_drake_seti]
- *Earliest Known Wildfires*. n.d. [https://www.sciencenews.org/article/earth-oldest-wildfire-430-million-years-ago-fossil-charcoal][research_earliest_wildfires]
- *Eternity in Six Hours*. n.d. [https://ui.adsabs.harvard.edu/abs/2013AcAau..89....1A/abstract][research_eternity]
- Galactic-Scale Energy. n.d. *Do the Math*. [https://dothemath.ucsd.edu/2011/07/galactic-scale-energy/][research_galactic_energy]
- *Glimpsing Heat from Alien Technologies Survey*. n.d. [https://sites.psu.edu/astrowright/the-g-hat-search-for-kardashev-civilizations/][research_ghat]
- *Grabby Aliens*. n.d. [https://grabbyaliens.com/][research_grabby_aliens]
- Green Bank Conference. n.d. *Slate*. [https://slate.com/technology/2013/09/green-bank-conference-seti-frank-drakes-equation-for-estimating-the-extraterrestrial-life.html][research_green_bank]
- Griffith. n.d. "G-hat Survey Paper III." Preprint, . [https://arxiv.org/abs/1504.03418][ref_ghat_paper_iii]
- Hanson, Robin, Daniel Martin, Calvin McCarter, and Jonathan Paulson. 2021. "If Loud Aliens Explain Human Earliness, Quiet Aliens Are Also Rare." Preprint, . [https://arxiv.org/abs/2102.01522][ref_grabby_aliens]
- Jiang, Jonathan H., Fuyang Feng, Philip E. Rosen, et al. 2022. "Avoiding the Great Filter: Predicting the Timeline for Humanity to Reach Kardashev Type I Civilization." Preprint, . [https://arxiv.org/abs/2204.07070][ref_jiang_great_filter]
- Kaku. n.d. *The Physics of Extraterrestrial Civilizations*. [https://mkaku.org/home/articles/the-physics-of-extraterrestrial-civilizations/][research_kaku_physics]
- Lazarus Stars, Scoggins. n.d. *Kipping*. [https://scholar.google.com/scholar?q=Kipping+Lazarus+Stars][research_lazarus_stars]
- Loeb. n.d. "Batista, and Sloan, Relative Likelihood for Life." Preprint, . [https://arxiv.org/abs/1606.08448][ref_loeb_cosmic_time]
- Murphy. n.d. *Galactic-Scale Energy*. [https://dothemath.ucsd.edu/2011/07/galactic-scale-energy/][research_murphy_energy]
- "On Interstellar Quantum Communication and the Fermi Paradox." n.d. Preprint, . [https://arxiv.org/html/2408.02445v1][ref_boyle_quantum]
- Sandberg. n.d. "Drexler, and Ord, Dissolving the Fermi Paradox." Preprint, . [https://arxiv.org/abs/1806.02404][ref_dissolving_fermi]
- Solitude Zone. n.d. *PhysOrg*. [https://phys.org/news/2025-10-solitude-zone-universe.html][research_solitude_phys]
- Suazo, Matías, Erik Zackrisson, Priyatam K. Mahto, et al. 2024. "Project Hephaistos: II. Dyson Sphere Candidates from Gaia DR3, 2MASS, and WISE." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2405.02927][research_hephaistos]
- Wright. n.d.-a. "G-HAT Infrared Survey." Preprint, . [https://arxiv.org/abs/1408.1133][ref_ghat_paper_i]
- Wright, Jason T. 2023. "Application of the Thermodynamics of Radiation to Dyson Spheres as Work Extractors and Computational Engines, and Their Observational Consequences." Preprint, . [https://arxiv.org/abs/2309.06564][ref_wright_thermodynamics]

### General Sources

- Adams and Laughlin. n.d. "Bodenheimer, and Laughlin, Red Dwarfs and the End of the Main Sequence." Accessed October 25, 2026. [https://ui.adsabs.harvard.edu/abs/1997ApJ...482..420L/abstract][ref_adams_red_dwarfs]
- Balbi and Frank. n.d. "The Oxygen Bottleneck for Technospheres." Accessed October 25, 2026. [https://www.nature.com/articles/s41550-023-02112-8][ref_oxygen_bottleneck]
- Berut. n.d. "Experimental Verification of Landauer's Principle." Accessed October 25, 2026. [https://www.nature.com/articles/nature10872][ref_landauer_experimental]
- Bradbury. n.d. "Matrioshka Brains." Accessed October 25, 2026. [https://gwern.net/doc/ai/scaling/hardware/1999-bradbury-matrioshkabrains.pdf][ref_matrioshka_brains]
- Catling. n.d. "Why O2 Is Required by Complex Life." Accessed October 25, 2026. [https://www.liebertpub.com/doi/10.1089/ast.2005.5.415][ref_catling_oxygen]
- Hart. n.d. "Explanation for the Absence of Extraterrestrials on Earth." Accessed October 25, 2026. [https://adsabs.harvard.edu/full/1975QJRAS..16..128H][ref_hart_absence]
- Suazo. n.d. "Project Hephaistos." Accessed October 25, 2026. [https://academic.oup.com/mnras/article/531/1/695/7665761][ref_project_hephaistos]
- Veres. n.d. "The Solitude Zone." Accessed October 25, 2026. [https://www.sciencedirect.com/science/article/pii/S0094576525006599][ref_solitude_zone]
- Wright. n.d.-b. "G-hat Survey Paper II." Accessed October 25, 2026. [https://iopscience.iop.org/article/10.1088/0004-637X/792/1/27][ref_ghat_paper_ii]
- Zhang. n.d. "Forecasting Kardashev Scale Progression." Accessed October 25, 2026. [https://www.nature.com/articles/s41598-023-38351-y][ref_zhang_kardashev]

### Tertiary Sources

- "Andromeda Galaxy." 2026. Wikipedia. Last modified February 20, at 00:42 (UTC). [https://en.wikipedia.org/w/index.php?title=Andromeda\_Galaxy&oldid=1339332569][research_andromeda]
- "Astrophysical Jet." 2026. Wikipedia. Last modified January 21, at 16:22 (UTC). [https://en.wikipedia.org/w/index.php?title=Astrophysical\_jet&oldid=1334110655][ref_relativistic_jet]
- "Blandford–Znajek Process." 2025. Wikipedia. Last modified October 31, at 18:26 (UTC). [https://en.wikipedia.org/w/index.php?title=Blandford%E2%80%93Znajek\_process&oldid=1319761150][ref_blandford_znajek]
- "Drake Equation." 2026. Wikipedia. Last modified February 28, at 15:27 (UTC). [https://en.wikipedia.org/w/index.php?title=Drake\_equation&oldid=1340932506][ref_drake_equation]
- "Dyson Sphere." 2026. Wikipedia. Last modified January 3, at 02:08 (UTC). [https://en.wikipedia.org/w/index.php?title=Dyson\_sphere&oldid=1330872455][ref_dyson_sphere]
- "Fermi Paradox." 2026. Wikipedia. Last modified February 28, at 15:51 (UTC). [https://en.wikipedia.org/w/index.php?title=Fermi\_paradox&oldid=1340935094][ref_fermi_paradox]
- "Geological History of Oxygen." 2026. Wikipedia. Last modified February 9, at 18:04 (UTC). [https://en.wikipedia.org/w/index.php?title=Geological\_history\_of\_oxygen&oldid=1337472897][ref_geological_oxygen]
- "Great Oxidation Event." 2026. Wikipedia. Last modified February 26, at 18:51 (UTC). [https://en.wikipedia.org/w/index.php?title=Great\_Oxidation\_Event&oldid=1340622157][ref_great_oxidation]
- "Kardashev Scale." 2026. Wikipedia. Last modified February 25, at 15:32 (UTC). [https://en.wikipedia.org/w/index.php?title=Kardashev\_scale&oldid=1340413569][ref_kardashev_scale]
- "Landauer's Principle." 2026. Wikipedia. Last modified February 9, at 02:31 (UTC). [https://en.wikipedia.org/w/index.php?title=Landauer's\_principle&oldid=1337373438][ref_landauer_principle]
- "Laniakea Supercluster." 2026. Wikipedia. Last modified February 27, at 13:58 (UTC). [https://en.wikipedia.org/w/index.php?title=Laniakea\_Supercluster&oldid=1340759226][ref_laniakea]
- "Large-Scale Structure of the Universe." 2026. Wikipedia. Last modified January 5, at 23:46 (UTC). [https://en.wikipedia.org/w/index.php?title=Large-scale\_structure\_of\_the\_universe&oldid=1331359053][ref_large_scale_structure]
- "Local Group." 2026. Wikipedia. Last modified January 27, at 01:47 (UTC). [https://en.wikipedia.org/w/index.php?title=Local\_Group&oldid=1335047038][ref_local_group]
- "Local Void." 2025. Wikipedia. Last modified September 29, at 05:00 (UTC). [https://en.wikipedia.org/w/index.php?title=Local\_Void&oldid=1313997875][ref_local_void]
- "Penrose Process." 2026. Wikipedia. Last modified January 17, at 23:46 (UTC). [https://en.wikipedia.org/w/index.php?title=Penrose\_process&oldid=1333468179][ref_penrose_process]
- "Red Dwarf." 2026. Wikipedia. Last modified February 10, at 20:45 (UTC). [https://en.wikipedia.org/w/index.php?title=Red\_dwarf&oldid=1337671698][ref_red_dwarf]
- "Sagittarius A." 2026. Wikipedia. Last modified February 23, at 04:08 (UTC). [https://en.wikipedia.org/w/index.php?title=Sagittarius\_A%2A&oldid=1339956322][ref_sagittarius_a]
- "Self-Replicating Spacecraft." 2026. Wikipedia. Last modified February 26, at 00:59 (UTC). [https://en.wikipedia.org/w/index.php?title=Self-replicating\_spacecraft&oldid=1340490475][research_self_replicating]
- "Star Lifting." 2025. Wikipedia. Last modified November 5, at 18:56 (UTC). [https://en.wikipedia.org/w/index.php?title=Star\_lifting&oldid=1320602371][ref_criswell_star_lifting]
- "Triangulum Galaxy." 2026. Wikipedia. Last modified February 9, at 18:31 (UTC). [https://en.wikipedia.org/w/index.php?title=Triangulum\_Galaxy&oldid=1337476493][research_triangulum]

### Related Posts

- Sechter, Brendan. 2026. "Introduction to Astronomy." *Brendan A R Sechter's Development Blog*, February 12. [https://sgeos.github.io/space/astronomy/science/2026/02/12/introduction\_to\_astronomy.html][related_post_astronomy]
- Sechter, Brendan. 2026. "Introduction to Space Studies." *Brendan A R Sechter's Development Blog*, February 21. [https://sgeos.github.io/space/math/2026/02/21/introduction\_to\_space\_studies.html][related_post_space_studies]
- Sechter, Brendan. 2026. "Human Evolution and the Great Filter." *Brendan A R Sechter's Development Blog*, February 26. [https://sgeos.github.io/science/philosophy/2026/02/26/human\_evolution\_and\_the\_great\_filter.html][related_post_great_filter]

[ref_adams_red_dwarfs]: https://ui.adsabs.harvard.edu/abs/1997ApJ...482..420L/abstract
[ref_aurora_effect]: https://arxiv.org/abs/1902.04450
[ref_blandford_znajek]: https://en.wikipedia.org/w/index.php?title=Blandford%E2%80%93Znajek_process&oldid=1319761150
[ref_boyle_quantum]: https://arxiv.org/html/2408.02445v1
[ref_carter_hard_steps]: https://doi.org/10.1017/s1473550408004023
[ref_catling_oxygen]: https://www.liebertpub.com/doi/10.1089/ast.2005.5.415
[ref_criswell_star_lifting]: https://en.wikipedia.org/w/index.php?title=Star_lifting&oldid=1320602371
[ref_dissolving_fermi]: https://arxiv.org/abs/1806.02404
[ref_drake_equation]: https://en.wikipedia.org/w/index.php?title=Drake_equation&oldid=1340932506
[ref_dyson_black_hole]: https://academic.oup.com/mnras/article/506/2/1723/6312510
[ref_dyson_sphere]: https://en.wikipedia.org/w/index.php?title=Dyson_sphere&oldid=1330872455
[ref_eternity_six_hours]: https://www.sciencedirect.com/science/article/abs/pii/S0094576513001148
[ref_fermi_paradox]: https://en.wikipedia.org/w/index.php?title=Fermi_paradox&oldid=1340935094
[ref_geological_oxygen]: https://en.wikipedia.org/w/index.php?title=Geological_history_of_oxygen&oldid=1337472897
[ref_ghat_paper_i]: https://arxiv.org/abs/1408.1133
[ref_ghat_paper_ii]: https://iopscience.iop.org/article/10.1088/0004-637X/792/1/27
[ref_ghat_paper_iii]: https://arxiv.org/abs/1504.03418
[ref_grabby_aliens]: https://arxiv.org/abs/2102.01522
[ref_great_oxidation]: https://en.wikipedia.org/w/index.php?title=Great_Oxidation_Event&oldid=1340622157
[ref_hart_absence]: https://adsabs.harvard.edu/full/1975QJRAS..16..128H
[ref_jiang_great_filter]: https://arxiv.org/abs/2204.07070
[ref_kardashev_scale]: https://en.wikipedia.org/w/index.php?title=Kardashev_scale&oldid=1340413569
[ref_landauer_experimental]: https://www.nature.com/articles/nature10872
[ref_landauer_principle]: https://en.wikipedia.org/w/index.php?title=Landauer's_principle&oldid=1337373438
[ref_laniakea]: https://en.wikipedia.org/w/index.php?title=Laniakea_Supercluster&oldid=1340759226
[ref_large_scale_structure]: https://en.wikipedia.org/w/index.php?title=Large-scale_structure_of_the_universe&oldid=1331359053
[ref_lazarus_stars]: https://academic.oup.com/mnras/article/523/3/3251/7188305
[ref_local_group]: https://en.wikipedia.org/w/index.php?title=Local_Group&oldid=1335047038
[ref_local_void]: https://en.wikipedia.org/w/index.php?title=Local_Void&oldid=1313997875
[ref_loeb_cosmic_time]: https://arxiv.org/abs/1606.08448
[ref_matrioshka_brains]: https://gwern.net/doc/ai/scaling/hardware/1999-bradbury-matrioshkabrains.pdf
[ref_oxygen_bottleneck]: https://www.nature.com/articles/s41550-023-02112-8
[ref_penrose_process]: https://en.wikipedia.org/w/index.php?title=Penrose_process&oldid=1333468179
[ref_project_hephaistos]: https://academic.oup.com/mnras/article/531/1/695/7665761
[ref_red_dwarf]: https://en.wikipedia.org/w/index.php?title=Red_dwarf&oldid=1337671698
[ref_relativistic_jet]: https://en.wikipedia.org/w/index.php?title=Astrophysical_jet&oldid=1334110655
[ref_sagittarius_a]: https://en.wikipedia.org/w/index.php?title=Sagittarius_A%2A&oldid=1339956322
[ref_solitude_zone]: https://www.sciencedirect.com/science/article/pii/S0094576525006599
[ref_waste_heat_habitability]: https://arxiv.org/html/2409.06737
[ref_wright_thermodynamics]: https://arxiv.org/abs/2309.06564
[ref_zhang_kardashev]: https://www.nature.com/articles/s41598-023-38351-y
[related_post_astronomy]: {% post_url 2026-02-12-introduction_to_astronomy %}
[related_post_great_filter]: {% post_url 2026-02-26-human_evolution_and_the_great_filter %}
[related_post_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[research_andromeda]: https://en.wikipedia.org/w/index.php?title=Andromeda_Galaxy&oldid=1339332569
[research_drake_seti]: https://www.seti.org/research/seti-101/drake-equation/
[research_earliest_wildfires]: https://www.sciencenews.org/article/earth-oldest-wildfire-430-million-years-ago-fossil-charcoal
[research_eternity]: https://ui.adsabs.harvard.edu/abs/2013AcAau..89....1A/abstract
[research_galactic_energy]: https://dothemath.ucsd.edu/2011/07/galactic-scale-energy/
[research_ghat]: https://sites.psu.edu/astrowright/the-g-hat-search-for-kardashev-civilizations/
[research_grabby_aliens]: https://grabbyaliens.com/
[research_green_bank]: https://slate.com/technology/2013/09/green-bank-conference-seti-frank-drakes-equation-for-estimating-the-extraterrestrial-life.html
[research_hephaistos]: https://doi.org/10.48550/arxiv.2405.02927
[research_kaku_physics]: https://mkaku.org/home/articles/the-physics-of-extraterrestrial-civilizations/
[research_lazarus_stars]: https://scholar.google.com/scholar?q=Kipping+Lazarus+Stars
[research_murphy_energy]: https://dothemath.ucsd.edu/2011/07/galactic-scale-energy/
[research_oxygen_bottleneck]: https://arxiv.org/abs/2308.01160
[research_self_replicating]: https://en.wikipedia.org/w/index.php?title=Self-replicating_spacecraft&oldid=1340490475
[research_solitude_phys]: https://phys.org/news/2025-10-solitude-zone-universe.html
[research_triangulum]: https://en.wikipedia.org/w/index.php?title=Triangulum_Galaxy&oldid=1337476493
