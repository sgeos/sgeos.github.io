---
layout: post
mathjax: true
comments: true
title:  "Roadmap to a Competitive Type III Civilization"
date:   2026-03-01 05:59:31 +0000
categories: science philosophy
---

<!-- A100 -->
<script>console.log("A100");</script>

The companion articles
[Causality and First-Mover Advantage
in Lightcone-Based Competitive
Intergalactic Colonization][related_post_causality]
and
[Tactical and Strategic Assessment
of the Local Galactic Neighborhood][related_post_assessment]
established two results.
First,
the speed of light creates
a $2d$-year offensive gap
that makes intergalactic warfare
structurally asymmetric
and rewards first-mover advantage.
Second,
the Milky Way's [supermassive black hole][ref_sagittarius_a]
ranks near the bottom
of the local hierarchy,
placing any civilization originating here
at a significant resource disadvantage
relative to civilizations
in [Andromeda][ref_andromeda],
[M87][ref_m87],
or other nearby giant galaxies.

This article asks
the operational question
that follows from those results.
If competitive intergalactic colonization
is the rational strategy
under the most severe assumptions,
what must be done to get there?
The answer requires traversing
the full [Kardashev scale][ref_kardashev]
from our current position
at approximately $K \approx 0.73$
to a competitive Type III civilization
capable of projecting force
and establishing presence
across the [Local Group][ref_local_group].

The roadmap was derived backwards.
The analysis began by asking
what a competitive Type III civilization
in the Local Group
must be capable of doing.
From those requirements,
it derived what an infant Type III civilization
must accomplish
to reach competitiveness.
That in turn determined
what a Type II civilization must build
to become an infant Type III.
And that determined
what a Type I civilization must achieve
to begin the transition to Type II.
Finally,
the requirements for reaching Type I
from our current position
fell out of the analysis
as the necessary first step.

The article is presented chronologically
because the backwards derivation,
while necessary for logical completeness,
is less useful operationally.
The reader needs to know
what to do first,
what to do next,
and what each step enables.
The presentation runs forward
from now to the far future,
but each section's requirements
were derived from the demands
of the section that follows it.

The [Kardashev scale][ref_kardashev]
provides the organizing framework.
In its original formulation
by Nikolai Kardashev in 1964,
the scale defines three types
based on a civilization's
total energy consumption.
Type I harnesses the energy
available on its planet,
approximately $10^{16}$ watts.
Type II harnesses the full output
of its star,
approximately $10^{26}$ watts.
Type III harnesses the energy
of its entire galaxy,
approximately $10^{36}$ watts.
Sagan's logarithmic extension
allows continuous values between types.

$$K = \frac{\log_{10}(P) - 6}{10}$$

where $P$ is power consumption in watts.
Humanity currently consumes
approximately $1.8 \times 10^{13}$ watts,
placing us at $K \approx 0.73$.

The distance from 0.73 to 3.0
is not merely a matter
of scaling energy production.
Each transition involves qualitative shifts
in engineering,
governance,
and competitive posture.
A Type I civilization
masters its planet.
A Type II civilization
masters its star.
A Type III civilization
masters its galaxy.
Each mastery is prerequisite for the next,
and each introduces failure modes
that did not exist
at the previous level.

| Type | Energy (W) | K Value | Scale | Key Capability |
|------|-----------|---------|-------|---------------|
| Current | $1.8 \times 10^{13}$ | 0.73 | Partial planetary | Fossil fuels, early renewables |
| Type I | $\sim 10^{16}$ | 1.0 | Full planetary | Planetary energy mastery |
| Type II | $\sim 10^{26}$ | 2.0 | Full stellar | Stellar energy mastery |
| Type III | $\sim 10^{36}$ | 3.0 | Full galactic | Galactic energy mastery |

For astronomical context,
[Introduction to Astronomy][related_post_astronomy]
covers observational astronomy
and the mathematical formulas
for stellar distances, luminosity,
and orbital mechanics.
For spaceflight context,
[Introduction to Space Studies][related_post_space_studies]
covers rocket propulsion, orbital mechanics,
and the history of space operations.
For evolutionary context,
[Human Evolution and the Great Filter][related_post_great_filter]
catalogs every major branching point
from the Last Universal Common Ancestor
to Homo sapiens.
For governance context,
[Telemeritocracy][related_post_telemeritocracy]
develops authority frameworks
based on demonstrated competence,
and
[Cryptotelemeritocracy
for Space Exploitation][related_post_crypto_space]
tests those frameworks
against multigenerational space operations
spanning centuries to millennia.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-03-01 05:59:31 +0000
```

## Now to Infant Competitive Type I

### Current Position

Humanity's total primary energy consumption
is approximately $1.8 \times 10^{13}$ watts.
This places us at $K \approx 0.73$
on Sagan's logarithmic extension
of the [Kardashev scale][ref_kardashev].
A Type I civilization
commands approximately $10^{16}$ watts,
corresponding roughly
to the total solar flux
intercepted by the Earth,
which is approximately $1.74 \times 10^{17}$ watts.
The gap between our current consumption
and the Type I threshold
is a factor of approximately 556.

The backwards derivation
reveals why this first transition matters.
A Type II civilization
requires a stable,
technically sophisticated,
unified planetary civilization
as its foundation.
No civilization can construct
a [Dyson swarm][ref_dyson_sphere]
while simultaneously fighting
resource wars on its home planet.
The Type I transition
is not merely about energy.
It is about establishing
the institutional and technological base
from which all subsequent transitions
become possible.

### Energy Infrastructure

Three energy technologies
are candidates for bridging
the gap to Type I.

**[Fusion power][ref_fusion].**
Deuterium-tritium fusion
releases approximately
$3.4 \times 10^{14}$ joules per kilogram
of fuel.
The global deuterium supply
in Earth's oceans
is effectively inexhaustible
at Type I energy consumption levels.
[ITER][ref_iter],
the international fusion research project
under construction in southern France,
is designed to produce
500 MW of fusion power
from 50 MW of input power,
demonstrating net energy gain
at engineering scale.
Commercial fusion reactors
following ITER's demonstration
could provide baseline power
at scales sufficient
for the Type I transition.

**[Space-based solar power][ref_sbsp].**
Solar flux in orbit
is approximately 1,361 watts per square meter,
unattenuated by atmosphere
and available continuously.
A constellation of orbital solar collectors
transmitting power to the surface
via microwave or laser beams
could supplement terrestrial energy production.
The engineering challenges
are substantial but well-understood.
The limiting factor
is launch cost to orbit,
which continues to decline
with reusable launch vehicle development.

**Terrestrial renewable scaling.**
Solar photovoltaic
and wind power installations
have grown at approximately
20 to 25 percent annually
over the past two decades.
If this growth rate persists,
terrestrial renewables alone
could approach Type I energy levels
within 100 to 200 years.
The constraint is storage
and grid infrastructure
rather than generation capacity.

The growth rate
is the critical variable.
At the current global energy growth rate
of approximately 2.3 percent per year,
the time to reach Type I is

$$t_{I} = \frac{\ln(P_{I} / P_0)}{r} = \frac{\ln(10^{16} / 1.8 \times 10^{13})}{0.023} \approx 275 \text{ years}$$

This estimate is sensitive
to the growth rate $r$.
At 1 percent growth,
the timeline extends
to approximately 630 years.
At 5 percent growth,
it compresses
to approximately 125 years.

### The Survival Bottleneck

The backwards derivation
identifies the Type 0 to Type I transition
as the most dangerous point
on the entire roadmap.
Unlike every subsequent transition,
failure at this stage is permanent.
A Type II civilization
that fails to achieve Type III
may stagnate
but retains its stellar energy base.
A Type I civilization
that fails to achieve Type II
may be confined to its planet
but remains viable.
A pre-Type I civilization
that experiences existential catastrophe
ceases to exist.

[Toby Ord][ref_ord] estimates
in [The Precipice][research_ord]
that the probability
of existential catastrophe
during the current century
is approximately one in six.
The dominant risk sources are

| Risk | Estimated Probability | Time Horizon |
|------|----------------------|-------------|
| Unaligned [artificial intelligence][ref_ai_alignment] | ~1 in 10 | This century |
| Engineered pandemic | ~1 in 30 | This century |
| [Nuclear war][ref_nuclear_winter] | ~1 in 1,000 | This century |
| Climate cascade | ~1 in 1,000 | This century |
| Asteroid or comet impact | ~1 in 1,000,000 | Per century |
| Supervolcanic eruption | ~1 in 10,000 | Per century |

The [Great Filter][ref_great_filter] hypothesis
suggests that
at least one step
on the path from dead matter
to galaxy-spanning civilization
is extraordinarily improbable.
The optimistic interpretation
is that the Great Filter
lies behind us,
in the emergence of life
or the development
of complex multicellular organisms.
The pessimistic interpretation
is that the Great Filter
lies ahead,
in the Type 0 to Type I transition
or in some later bottleneck.

The companion causality article's argument
that competitive expansion
is the rational strategy
under severe assumptions
does not help
if the civilization destroys itself
before reaching the starting line.
The first operational requirement
of the roadmap
is survival.

### Governance and Coordination

The backwards derivation
imposes governance requirements
on the Type 0 to Type I transition
that are not obvious
from a purely energy perspective.
A Type II civilization
requires the capacity
to coordinate megastructure construction
across an entire star system.
A Type III civilization
requires the capacity
to maintain strategic coherence
across interstellar distances.
These capabilities do not emerge
spontaneously at the moment
they become necessary.
They develop incrementally
from whatever governance institutions
exist at the time
of the Type I transition.

The minimum governance requirement
for the Type I transition
is sufficient coordination
to manage [existential risks][ref_existential_risk]
without destroying the civilization
in the process.
This does not require
a world government
in the conventional sense.
It requires mechanisms
for credible commitment
on extinction-level threats.
Nuclear arms control treaties,
biosecurity agreements,
and AI safety coordination
are early and imperfect examples
of such mechanisms.

The Messaging Extraterrestrial Intelligence debate
discussed in the
[companion assessment article][related_post_assessment]
is a specific instance
of a broader governance challenge.
Decisions with species-level consequences
are currently made
by individual research groups
or national governments
without species-level authorization.
The Type I transition
requires developing institutions
capable of making binding decisions
on behalf of the species
on matters of existential consequence.

The companion governance articles
propose a candidate framework
for this class of problem.
[Telemeritocracy][related_post_telemeritocracy]
distributes authority
to individuals and groups
who demonstrate the ability
to advance a defined organizational purpose.
Unlike democratic or autocratic systems,
telemeritocratic institutions
assign decision-making power
based on verified competence
relative to the organization's telos.
For existential risk management,
the telos is species survival.
The framework requires
three prerequisites.
The purpose must be definable.
Expertise must be distributed
rather than concentrated
in a single individual or group.
And the quality of contributions
must be assessable
by the institution's participants.

[Cryptotelemeritocracy][related_post_cryptotelemeritocracy]
extends telemeritocracy
with an anonymous oversight layer
specifically designed
to prevent mission drift
over long time horizons.
An anonymous arbitration mechanism
selects reviewers
from a qualified candidate pool,
preventing the targeting
of oversight personnel
by internal or external adversaries.
This counter-espionage property
becomes relevant
at civilization scales
where institutional capture
over centuries
is not merely possible
but historically typical.
[Michels's iron law of oligarchy][ref_iron_law]
predicts that organizations
inevitably concentrate power
in a leadership class
regardless of initial structure.
Cryptotelemeritocratic oversight
is designed to resist this tendency
through structural anonymity.

### Timeline

The most optimistic projections
place the Type I transition
within 100 to 150 years,
assuming sustained exponential growth
in energy production
and successful development
of fusion power.
The most pessimistic projections
that still allow success
place it at 400 to 500 years,
assuming slower growth rates
and periodic setbacks
from regional conflicts
or economic disruptions.

The survival bottleneck
introduces a qualitative uncertainty
that the energy growth models
do not capture.
If Ord's one-in-six estimate
is approximately correct,
the probability of surviving
to Type I
is approximately
$(5/6)^{n}$
where $n$ is the number
of century-equivalent risk periods
between now and the transition.
At 275 years,
$n \approx 2.75$
and the survival probability
is approximately 0.63.
At 500 years,
$n = 5$
and the survival probability
drops to approximately 0.40.

These estimates assume
that existential risk per century
remains constant.
If risk decreases
as governance institutions improve,
the survival probability increases.
If risk increases
as technology makes
catastrophic weapons more accessible,
the survival probability decreases.

## Type I to Infant Competitive Type II

### From Planet to Star

A Type I civilization
commands approximately $10^{16}$ watts.
A Type II civilization
commands the full output
of its host star,
approximately $3.8 \times 10^{26}$ watts
for a Sun-like star.
The gap is a factor
of approximately $10^{10}$.

The backwards derivation
reveals why Type II
is a prerequisite for Type III.
Interstellar colonization
requires energy expenditures
far exceeding what a single planet
can provide.
Accelerating even a modest payload
to a significant fraction
of the speed of light
requires energy inputs
measured in multiples
of current global consumption.
A Type II civilization
with full access
to its star's output
can afford these expenditures.
A Type I civilization cannot.

### The Dyson Swarm

The canonical Type II megastructure
is the [Dyson sphere][ref_dyson_sphere],
or more precisely the Dyson swarm,
a constellation of orbiting collectors
that intercept
and convert a substantial fraction
of the host star's radiation.
Freeman Dyson's original 1960 proposal
envisioned a solid shell
surrounding a star.
Modern treatments favor
a swarm of independent
orbiting collectors
because a solid shell
is gravitationally unstable
and structurally impractical
at stellar scales.
A swarm avoids these problems
by distributing the collection area
across many independent units
in various orbits.

[Armstrong and Sandberg][research_eternity]
analyzed the construction timeline
for a Dyson swarm
using [self-replicating machines][ref_self_replicating].
Their model begins with
a single factory
on [Mercury][ref_mercury].
The factory disassembles
Mercury's surface material,
manufactures solar collectors
and additional factories,
and launches the collectors
into solar orbit.
Each new factory
doubles the production rate.
Mercury's mass is
approximately $3.3 \times 10^{23}$ kilograms.
With an initial doubling time
of one to two years,
the entire planet
can be disassembled
in approximately 40 years.
The resulting swarm
intercepts a significant fraction
of solar output.

The exponential growth
of the self-replicating factory system
means that
nearly all of the construction
occurs in the final few
doubling periods.
For the first 30 years,
the project is nearly invisible.
In the last 10 years,
Mercury visibly shrinks.

### Self-Replicating Industry

The Dyson swarm construction
depends critically
on [self-replicating machines][ref_self_replicating].
Without self-replication,
the manufacturing throughput
required to process
$3.3 \times 10^{23}$ kilograms of material
in a human-relevant timescale
is physically impossible.
With self-replication,
the problem reduces to
building the first factory
and ensuring reliable copying.

The [self-replicating spacecraft][ref_self_replicating_spacecraft] concept
extends self-replication
to interstellar distances.
A self-replicating probe
arrives at a new star system,
uses local resources
to build copies of itself,
and sends those copies
to additional star systems.
The same exponential logic
that makes Mercury disassembly feasible
in 40 years
makes galactic colonization feasible
in millions.

The risk associated
with self-replicating machines
is the [gray goo][ref_gray_goo] scenario,
in which replicators
malfunction or are misdirected
and consume resources
without producing useful output.
This risk is not speculative.
It is the engineering equivalent
of a biological pathogen.
Any civilization deploying
self-replicating technology
must solve the control problem
for replicators
before deploying them.
This is analogous to
the [AI alignment][ref_ai_alignment] problem
at a physical rather than
computational level.

### Solar System Infrastructure

Before constructing a Dyson swarm,
a Type I civilization
must industrialize
the inner solar system.
This requires several
intermediate capabilities.

**[Asteroid mining][ref_asteroid_mining].**
The asteroid belt contains
an estimated $2.4 \times 10^{21}$ kilograms
of material,
including metals, water ice,
and silicates.
Mining asteroids
provides raw materials
for orbital construction
without the energy cost
of lifting material
from a planetary surface.

**Orbital habitats.**
[O'Neill cylinders][ref_oneill]
and similar rotating habitats
provide artificial gravity environments
for permanent human settlement
in space.
A population of billions
living in orbital habitats
provides the workforce
and institutional base
for megastructure construction.

**[Planetary engineering][ref_planetary_engineering].**
Mars [colonization][ref_mars_colonization]
and Venus [terraforming][ref_terraforming]
extend the civilization's
resource base and population.
These projects operate
on century timescales
and provide experience
with the large-scale engineering
required for stellar-scale projects.

### Stellar Engineering

Beyond the Dyson swarm,
a maturing Type II civilization
develops capabilities
for engineering its host star directly.

**[Star lifting][ref_star_lifting].**
Star lifting extracts mass
from a star's outer layers
using magnetic fields
or focused radiation pressure.
The extracted material
provides fusion fuel
and heavy elements
for construction.
Removing mass from the star
also extends its main-sequence lifetime,
providing more time
for the civilization's development.

**[Stellar engines][ref_stellar_engine].**
A [Shkadov thruster][ref_shkadov]
uses a large reflector
to create an asymmetry
in a star's radiation pressure,
producing a net thrust
that moves the entire star system.
At the accelerations achievable,
a Shkadov thruster
can reposition a star
by significant distances
over millions of years.
This capability is relevant
for intergalactic positioning.

**SMBH energy extraction.**
The [Penrose process][ref_penrose]
can extract up to 29 percent
of the rotational energy
of a spinning black hole.
The [Blandford-Znajek process][ref_blandford_znajek]
extracts energy via
magnetic field interactions
with the black hole's ergosphere.
[Sagittarius A*][ref_sagittarius_a]
at $4.3 \times 10^6$ solar masses
represents an enormous energy reserve.
A Type II civilization
that develops SMBH energy extraction
gains an energy source
that persists long after
its host star
exhausts its nuclear fuel.

### Timeline

The time from Type I to Type II
depends on the growth rate
sustained during the transition.
At 2.3 percent annual growth
in energy production,
the time to increase
from $10^{16}$ to $10^{26}$ watts is

$$t_{II} = \frac{\ln(10^{26} / 10^{16})}{0.023} = \frac{10 \ln 10}{0.023} \approx 1{,}000 \text{ years}$$

This estimate assumes
sustained exponential growth,
which may not hold
over millennial timescales.
A logistic growth model
with a carrying capacity
determined by available solar system resources
would produce a longer timeline.

The Armstrong and Sandberg estimate
of 40 years for Mercury disassembly
suggests that
the construction phase itself
is rapid once
self-replicating technology is mature.
The binding constraint
is developing that technology,
not executing the construction.

## Type II to Infant Competitive Type III

### From Star to Galaxy

A Type II civilization
commands approximately $10^{26}$ watts.
A Type III civilization
commands the energy output
of its entire galaxy,
approximately $4 \times 10^{36}$ watts
for a [Milky Way][ref_milky_way]-class galaxy
containing 100 to 400 billion stars.
The gap is again approximately $10^{10}$.

The backwards derivation
identifies the critical requirement.
Competitive presence
in the [Local Group][ref_local_group]
requires controlling
the Milky Way's full resource base.
A civilization that occupies
one star system
cannot defend against
a civilization that occupies
a galaxy.
The Type III transition
is therefore a prerequisite
for competitive viability
at the intergalactic scale.

### Interstellar Propulsion

Reaching other star systems
requires propulsion technologies
beyond anything currently operational.
Several candidates exist
at various levels
of theoretical maturity.

| Propulsion Method | Achievable Speed | Technology Status | Key Constraint |
|---|---|---|---|
| [Laser sail][ref_laser_propulsion] | 0.1c to 0.3c | Demonstrated at small scale | Beam collimation over light-years |
| [Fusion drive][ref_fusion] | 0.05c to 0.1c | Theoretical | Net energy gain required |
| [Nuclear pulse][ref_nuclear_pulse] | 0.03c to 0.1c | Designed but untested | Nuclear test ban treaties |
| [Bussard ramjet][ref_bussard] | Up to 0.9c theoretical | Highly speculative | Interstellar medium drag |
| [Generation ship][ref_generation_ship] | 0.01c to 0.05c | Near-term feasible | Multi-century transit |

The [Breakthrough Starshot][ref_breakthrough_starshot]
initiative proposes
using a ground-based laser array
to accelerate gram-scale probes
to 0.2c,
reaching Alpha Centauri
in approximately 20 years.
Scaling this concept
to payloads sufficient
for colonization
requires laser arrays
with power outputs
measured in gigawatts to terawatts,
which is within the capability
of a Type II civilization.

For colonization purposes,
speed is less important
than the ability to replicate
at the destination.
A [self-replicating probe][ref_self_replicating_spacecraft]
traveling at 0.01c
reaches a star 10 light-years away
in 1,000 years.
It then spends
perhaps decades to centuries
replicating and constructing infrastructure
before sending copies
to the next set of targets.
The colonization wave expands
at a speed determined
by transit speed,
replication time,
and the number of copies
dispatched per generation.

### The Colonization Wave

[Armstrong and Sandberg][research_eternity] model
the colonization of the galaxy
as a wave
expanding from the origin
at some fraction
of the speed of light.
If each probe
reaches a new star in time $t_{\text{transit}}$
and replicates in time $t_{\text{rep}}$,
the effective wave speed is

$$v_{\text{wave}} = \frac{d}{t_{\text{transit}} + t_{\text{rep}}}$$

where $d$ is the average
distance between target stars.

For the Milky Way,
the average distance
between stars
is approximately 4 to 5 light-years.
At a probe speed of 0.1c,
$t_{\text{transit}} \approx 40$ to 50 years.
If $t_{\text{rep}} \approx 50$ years,
then $v_{\text{wave}} \approx 0.05c$.

The Milky Way's disk
has a diameter
of approximately 100,000 light-years.
At $v_{\text{wave}} = 0.05c$,
full colonization takes
approximately 2 million years.
At $v_{\text{wave}} = 0.01c$,
it takes approximately 10 million years.

These timescales are long
by human standards
but short by astronomical ones.
The Milky Way is 13.6 billion years old.
Colonizing it in 2 to 10 million years
uses less than 0.1 percent
of its lifetime.
Any civilization
that arose even slightly earlier
in the galaxy's history
could have colonized
the entire Milky Way by now.
The absence of evidence
for such colonization
is the [Fermi paradox][ref_fermi],
addressed in the companion articles.

### Governance Across Light-Years

As the colonization wave expands,
the civilization that launched it
faces an unprecedented
governance challenge.
Communication across the Milky Way
takes 100,000 years
at the speed of light.
No central authority
can coordinate decisions
across these timescales.

The colonization wave
does not produce
a unified empire.
It produces a diaspora
of increasingly divergent
daughter civilizations,
each adapting to local conditions
and drifting away
from the parent culture.
Over millions of years,
the descendants
of a single origin civilization
may become as different
from each other
as they are from
any independently evolved species.

This divergence
is not merely cultural.
If self-modification,
genetic engineering,
or machine intelligence
are available,
biological and cognitive divergence
will compound cultural divergence.
The civilization that emerges
from Milky Way colonization
may bear no resemblance
to what departed.

The competitive implications
are significant.
A Type III civilization
that cannot maintain
strategic coherence
across its galactic extent
is vulnerable
to internal fragmentation
and external exploitation.
The governance mechanisms
developed during the Type I transition
must evolve continuously
to accommodate
increasing scale and diversity.

The companion governance article on
[cryptotelemeritocracy
for space exploitation][related_post_crypto_space]
quantifies this degradation.
Governance coherence
decays exponentially
with distance and communication latency,
following a half-life model.

$$C(t) = C_0 \cdot 2^{-t/T_{GCH}}$$

where $C(t)$ is governance coherence
at time $t$,
$C_0$ is initial coherence,
and $T_{GCH}$ is
the governance coherence half-life,
the time required
for coherence to halve.
If $T_{GCH}$ is measured in centuries,
a colonization wave
spanning millions of years
reduces governance coherence
to negligible levels
long before the wave
reaches the galactic periphery.

The degradation
proceeds through identifiable phases.
Coordinated behavior
degrades to coordinated meaning
as direct institutional enforcement
gives way to shared
interpretive frameworks.
Coordinated meaning
degrades to propagated narrative
as shared frameworks
lose their connection
to operational reality.
At intergalactic scales,
governance structures
degrade entirely
into myth and eventually superstition.
The civilization's founding purpose
survives only as cultural residue,
unconnected to institutional action.

Two mechanisms resist this degradation.

First,
federated arbitrators
adapted to communication latency
can maintain oversight
within local regions
even when galactic-scale coordination
is impossible.
Each region operates
its own arbitration system
with its own candidate pool
drawn from local expertise.
Inter-regional coordination
occurs on the timescale
permitted by lightspeed communication,
which is slow
but non-zero.

Second,
the spinoff mechanism
provides a structural counter
to the [iron law of oligarchy][ref_iron_law].
When a daughter colony
establishes itself
at a new star system,
it instantiates a new organization
from the parent's template.
The spinoff resets
institutional age to zero,
temporarily restoring
the founding coherence
that older institutions
have lost to drift.
Over millions of years,
the colonization wave
produces a continuous supply
of fresh institutions
even as older ones
degrade toward myth.

The competitive implication is direct.
A Type III civilization
that incorporates
governance coherence mechanisms
into its colonization architecture
maintains strategic coherence
longer than one that does not.
The governance half-life
becomes a competitive variable
alongside growth rate
and resource base.

### Satellite Galaxy Expansion

The [companion assessment article][related_post_assessment]
identified nine priority targets
for colonization
beyond the Milky Way's disk.
The nearest are the satellite galaxies
of the Milky Way,
beginning with
the Sagittarius Dwarf
already undergoing tidal disruption
and the [Large Magellanic Cloud][ref_lmc]
at 160,000 light-years.

Colonizing satellite galaxies
provides two strategic benefits.
First,
it extends the resource base
beyond the Milky Way proper.
Second,
it establishes presence
in multiple gravitationally bound systems,
making the civilization resilient
to catastrophic events
in any single galaxy.

The transition
from Milky Way colonization
to satellite galaxy colonization
is the threshold
between infant Type III
and Type III with
Local Group projection capability.

### Timeline

Milky Way colonization
from a single origin
takes approximately
500,000 to 50 million years,
depending on probe speed,
replication time,
and the fraction of stars targeted.
Satellite galaxy colonization
adds hundreds of thousands
of additional years
for transit across the voids
between the Milky Way
and its companions.

The total time
from Type II to infant Type III
is measured in millions of years.
By comparison,
anatomically modern humans
have existed
for approximately 300,000 years.

## Infant Type III to Local Group Competitive Type III

### Competitive Requirements

The backwards derivation
begins at this level.
A competitive Type III civilization
in the [Local Group][ref_local_group]
must satisfy several requirements
simultaneously.

**Resource parity.**
The civilization must command
energy and material resources
comparable to
those available to any rival
in the Local Group.
From the [companion assessment article][related_post_assessment],
[Andromeda's][ref_andromeda] SMBH
is 25 to 35 times more massive
than Sagittarius A*.
Resource parity requires
either growing
the Milky Way's SMBH
through accretion
or achieving technological advantages
that compensate
for the mass deficit.

**Force projection.**
The civilization must be capable
of projecting force
across intergalactic distances.
This means
either deploying sterilization capability
using the SMBH engine framework
from the [companion causality article][related_post_causality]
or establishing forward presence
in target galaxies
through colonization.

**Defensive coverage.**
The civilization must detect
and respond to threats
from any direction
within the Local Group.
The $2d$-year offensive gap
means that
any incoming attack
is at least $2d$ years
out of date
when it arrives.
Defensive posture requires
distributed sensor networks
and distributed response capability
across the Local Group volume.

**Information warfare capability.**
From the companion assessment article's
analysis of information warfare
across intergalactic distances,
a competitive civilization
must be capable of concealment,
deceptive signaling,
and detection
of adversary information operations.

### Intergalactic Transit Engineering

The interstellar propulsion table above
covers methods for reaching nearby stars
across distances of 4 to 50 light-years.
The jump from stellar
to intergalactic distances
introduces qualitatively different challenges
that the interstellar analysis
does not address.

The void between the Milky Way
and [Andromeda][ref_andromeda]
is approximately 2.5 million light-years
of nearly empty space.
The [intergalactic medium][ref_igm]
has a particle density
of approximately $10^{-6}$
atoms per cubic centimeter,
six orders of magnitude less
than the interstellar medium's
approximately 1 atom
per cubic centimeter.
This density difference
eliminates several propulsion methods
that are viable at interstellar scales.

**Bussard ramjet failure.**
The [Bussard ramjet][ref_bussard]
collects interstellar hydrogen
as fuel through a magnetic scoop.
In the interstellar medium,
the concept is already marginal
because drag from the scoop
may exceed thrust
from the collected fuel.
In the intergalactic medium,
the fuel density is so low
that the ramjet produces
effectively zero thrust.
The Bussard ramjet is inoperable
for intergalactic transit.

**Laser sail deceleration.**
[Laser propulsion][ref_laser_propulsion]
can accelerate a sail
to high velocities
using a beam from the origin system.
However,
deceleration at the destination
requires either
a laser array already in place
at the target,
which does not exist
before colonization,
or an alternative braking mechanism.
[Heller and Hippke][research_heller_hippke]
demonstrated that photon pressure
from the target star
can decelerate a sail
arriving at a nearby star system,
but this technique
requires precise alignment
and works only for arrivals
at luminous targets.
Over 2.5 million light-years,
the origin laser beam
has diverged beyond utility.
The sail must carry
its own deceleration capability.

**Viable intergalactic propulsion.**
Three propulsion approaches
remain viable
for crossing intergalactic voids.

An [antimatter drive][ref_antimatter_rocket]
carries its own fuel
and converts matter-antimatter annihilation
directly into thrust.
The energy density of antimatter,
$9 \times 10^{16}$ joules per kilogram
from $E = mc^2$,
is the highest achievable
under known physics.
An antimatter drive
is independent of the medium density
and can operate
in the intergalactic void
as effectively as near a star.
The constraint is antimatter production,
which requires
a mature Type II energy base
to manufacture sufficient quantities.

A [photon drive][ref_photon_rocket]
achieves thrust
by directing a collimated photon beam
from onboard energy sources.
The exhaust velocity
is the speed of light,
which is the theoretical maximum
for any reaction drive.
The mass ratio
for relativistic velocities
is severe
but the method requires
no external infrastructure
and no medium to push against.

[Hypervelocity stars][ref_hypervelocity_star]
ejected from galactic cores
at speeds of 500 to 1,000 km/s
provide a third option.
These stars traverse
the intergalactic void
on trajectories
determined by their ejection dynamics.
A Type III civilization
could use hypervelocity stars
as transit platforms,
constructing infrastructure
on or around the star
and riding it
across the void.
At 1,000 km/s,
a hypervelocity star
crosses the 2.5 million light-year gap
to Andromeda
in approximately 750 million years.
This is slow
by any operational standard,
but it eliminates
the propulsion problem entirely.
The star carries
its own energy source,
its own gravitational environment,
and sufficient mass
for self-replicating industry
to operate during transit.

A fourth approach
uses the [Shkadov thruster][ref_shkadov]
described in the stellar engineering section
to redirect entire star systems
toward intergalactic targets.
This is equivalent
to manufacturing hypervelocity stars
on demand
rather than waiting
for natural ejection events.

**Energy requirements.**
The energy required
to accelerate a colonization payload
to intergalactic transit speed
scales with mass
and desired velocity.
For a $10^6$ kilogram payload
accelerated to $0.1c$,
the kinetic energy is approximately

$$E_k = \frac{1}{2}mv^2 = \frac{1}{2}(10^6)(3 \times 10^7)^2 \approx 4.5 \times 10^{20} \text{ J}$$

This is approximately 0.001 percent
of the Sun's total luminous output
for one second.
For a Type II civilization
commanding $10^{26}$ watts,
the energy cost
is negligible per probe.
The challenge is not energy
but the engineering
of propulsion systems
that can sustain acceleration
over years to decades
and then decelerate
without external assistance
at the destination.

**Transit duration and replication.**
The intergalactic void
offers no intermediate stops.
Unlike interstellar colonization,
where stars are separated
by 4 to 5 light-years
and the colonization wave
can replicate at each stop,
the intergalactic crossing
is a single unbroken transit.
At $0.1c$,
the Milky Way to Andromeda transit
takes 25 million years.
At $0.01c$,
it takes 250 million years.
The probe or colony ship
must be entirely self-sustaining
for the full duration.

[Fogg][research_fogg]
analyzed the feasibility
of intergalactic colonization
and concluded that
the principal constraint
is not energy or propulsion
but the reliability
of self-sustaining systems
over multimillion-year timescales.

| Method | Speed | Transit Time (MW to Andromeda) | Medium Dependence | Key Constraint |
|--------|-------|-------------------------------|------------------|---------------|
| [Antimatter drive][ref_antimatter_rocket] | 0.05c to 0.3c | 8 to 50 Myr | None | Antimatter production |
| [Photon drive][ref_photon_rocket] | 0.01c to 0.5c | 5 to 250 Myr | None | Extreme mass ratio |
| [Hypervelocity star][ref_hypervelocity_star] | ~0.003c | ~750 Myr | None | Natural ejection rate |
| [Shkadov thruster][ref_shkadov] redirect | 0.001c to 0.01c | 250 Myr to 2.5 Gyr | None | Stellar-scale engineering |
| [Laser sail][ref_laser_propulsion] (no deceleration) | 0.1c to 0.3c | 8 to 25 Myr | None for acceleration | No deceleration mechanism |

### The Andromeda Problem

The most immediate
competitive challenge
is [Andromeda][ref_andromeda],
the nearest major galaxy
at 2.5 million light-years.
The companion assessment article
characterized Andromeda
as a non-peer adversary
with significant advantages
in five dimensions.

The SMBH mass ratio
of 25:1 to 35:1
in Andromeda's favor
is the most consequential asymmetry.
In the sterilization engine framework,
SMBH mass correlates directly
with destructive capability.
The Milky Way's
$4.3 \times 10^6$ solar mass
Sagittarius A*
cannot match
Andromeda's $1.0$ to $1.4 \times 10^8$
solar mass SMBH
in raw power output.

Two strategies address
this asymmetry.

**Technological superiority.**
If energy extraction efficiency
scales with technology level
rather than SMBH mass alone,
a technologically advanced civilization
in the Milky Way
could extract more useful energy
from Sagittarius A*
than a less advanced civilization
extracts from
Andromeda's larger SMBH.
This strategy is a bet
on quality over quantity.

**SMBH growth.**
Supermassive black holes grow
by accretion.
A Type III civilization
could feed material
into Sagittarius A*
to increase its mass over time.
The timescales for significant growth
through accretion
are long,
on the order of hundreds of millions
to billions of years,
but a civilization
with galactic-scale resources
and patience
could meaningfully alter
its SMBH's mass
over these timescales.

### The Merger Window

The [2025 Nature Astronomy study][research_mw_andromeda_collision]
estimates that
the Milky Way and Andromeda
have a 50 percent probability
of colliding
within 10 billion years
and a 2 percent probability
of colliding
within 5 billion years.
The collision,
if it occurs,
would produce a single merged galaxy
over a timescale
of approximately 2 billion years.

The merger
has profound strategic implications.
Before the merger,
the Milky Way and Andromeda
are separated
by the $2d$-year offensive gap
of approximately 5 million years.
After the merger,
they share a single galaxy.
Any civilization in Andromeda
is no longer
an intergalactic adversary.
It is a neighbor.

The pre-merger period
is the competitive window.
A Milky Way civilization
that achieves Type III status
and establishes resource parity
before the merger
enters the merged galaxy
as a peer competitor.
A civilization that fails
to achieve parity
enters as a subordinate.

### Information Warfare at Galactic Scale

The companion assessment article
analyzed information warfare
across intergalactic distances
and identified three equilibria.
The [dark forest][ref_dark_forest] equilibrium
favors concealment.
The fog of war equilibrium
favors active deception.
The growth-dominance equilibrium
favors maximum growth rate
over concealment.

At the Local Group scale,
a competitive Type III civilization
must operate
in all three regimes simultaneously.
Concealment is appropriate
when preparing capabilities
that should not be revealed
before deployment.
Deception is appropriate
when false signals
can misdirect adversary resources.
Growth is always appropriate
because competitive selection
eliminates slow growers
over cosmic timescales.

The thermodynamic constraint
identified in the assessment article
applies here with full force.
A Type III civilization
processing $10^{36}$ watts
cannot conceal itself.
Its waste heat signature
is galactic in scale.
The [Wright et al. survey][research_ghat]
would detect such a civilization
if it existed
within the survey volume.
A competitive Type III civilization
has abandoned concealment
by the fact of its existence.

### Competitive Fitness Summary

| Criterion | Current Humanity | Infant Type III | Competitive Type III |
|-----------|-----------------|----------------|---------------------|
| Energy budget | $1.8 \times 10^{13}$ W | $\sim 10^{36}$ W | $\sim 10^{36}$ W with SMBH |
| SMBH capability | None | Sagittarius A* access | Parity with Andromeda |
| Colonization coverage | 1 planet | Milky Way + satellites | Full Local Group |
| Force projection | None | Milky Way defense | Intergalactic offense and defense |
| Information warfare | None | Milky Way scale | Local Group scale |
| Growth rate | ~2.3% per year | Unknown | Maximum sustainable |

### Timeline

The transition
from infant Type III
to competitive Type III
operates on timescales
measured in millions
to billions of years.
The rate-limiting factor
is not technology development
but physical constraints.
SMBH growth through accretion
takes hundreds of millions of years.
Colonization of the full Local Group
takes millions of years
for transit alone.

The competitive window
is bounded by the Andromeda merger.
If the merger occurs
in 5 to 10 billion years,
the civilization has
at most a few billion years
to establish parity
before the competitive landscape
transforms irreversibly.

## Extrapolation Beyond Local Group Competitiveness

### The Virgo Question

The companion assessment article
posed the Virgo question
as the existential strategic concern
beyond the Local Group.
[M87][ref_m87] at the center
of the [Virgo Cluster][ref_virgo_cluster]
possesses a SMBH
of $6.5 \times 10^9$ solar masses,
1,500 times more massive
than Sagittarius A*.
The Virgo Cluster
lies approximately 53.5 million light-years
from the Milky Way.

The $2d$-year offensive gap
for the Virgo Cluster
is approximately 107 million years.
The Local Group
is falling toward Virgo
at approximately 250 to 300 km/s.
A sterilization sweep
from M87
could be en route
and undetectable
until arrival.

A civilization that achieves
Local Group competitiveness
faces the Virgo question
as the next strategic challenge.
The SMBH asymmetry
is even more severe
than the Andromeda problem.
No amount of Milky Way SMBH growth
can match M87's
$6.5 \times 10^9$ solar mass endowment.

### Supercluster Dynamics

The [Laniakea Supercluster][ref_laniakea]
contains approximately 100,000 galaxies
across 520 million light-years.
The [cosmic web][ref_cosmic_web]
channels matter
along filaments
connecting galaxy clusters,
with voids
occupying the spaces between.

Expansion beyond the Local Group
follows these filaments.
The Local Sheet
connects the Local Group
to the Virgo Cluster
along a filamentary structure.
Expansion in other directions
encounters the Local Void,
a region of extremely low
galaxy density
that offers minimal targets
for colonization.

The large-scale topology
of the cosmic web
constrains expansion corridors.
A civilization cannot expand
equally in all directions.
It must follow the matter distribution,
concentrating resources
along filaments
and bypassing voids.

### Limits of Extrapolation

Several physical constraints
limit the utility
of extrapolation
beyond Local Group competitiveness.

**Accelerating expansion.**
The universe is expanding
at an accelerating rate.
Galaxies beyond a certain distance
are receding faster than
the speed of light
in the metric expansion framework.
Over sufficiently long timescales,
the number of reachable galaxies
decreases.
The Local Group itself
is gravitationally bound
and will not be torn apart
by expansion,
but distant clusters
will become progressively unreachable.

**Heat death.**
The second law of thermodynamics
implies that the universe
will eventually reach
thermodynamic equilibrium,
at which point
no work can be extracted
from any energy gradient.
This ultimate constraint
operates on timescales
of $10^{100}$ years or longer,
far beyond the scope
of any strategic planning.

**Unknown physics.**
The analysis assumes
that the speed of light
is an absolute barrier
to information transfer
and force projection.
If faster-than-light travel
or communication is possible
through mechanisms
such as the [Alcubierre drive][ref_alcubierre]
or traversable wormholes,
the entire strategic framework
changes.
The $2d$-year offensive gap
collapses.
First-mover advantage
may no longer be decisive.
The competitive landscape
becomes radically different.

This analysis
makes no assumptions
about unknown physics.
The roadmap is constructed
from known physical laws.
If new physics is discovered,
the roadmap will need revision.

## Implications of Analysis

### Critical Bottlenecks

Each transition
on the Kardashev scale
has a characteristic bottleneck.

| Transition | Bottleneck | Critical Technology | Failure Mode |
|-----------|-----------|-------------------|-------------|
| Type 0 to I | Survival | Existential risk management | Extinction |
| Type I to II | Self-replication | Von Neumann machines | Technological stagnation |
| Type II to III | Interstellar propulsion | Relativistic drives or sails | Confinement to single star |
| Type III to Competitive | Intergalactic transit and SMBH parity | Antimatter drives, SMBH engineering | Strategic subordination |

The bottlenecks
are qualitatively different.
The Type 0 to Type I bottleneck
is existential.
The Type I to Type II bottleneck
is technological.
The Type II to Type III bottleneck
is propulsive.
The Type III to competitive bottleneck
is material.

No subsequent bottleneck matters
if the first one fails.
This is the fundamental insight
of the backwards derivation.
The competitive requirements
at the top of the Kardashev scale
propagate downward
as prerequisites
at each lower level.
But the existential bottleneck
at the bottom
is a gate
through which all subsequent progress
must pass.

### The Growth Imperative

The companion articles established
that competitive selection
favors the maximum sustainable growth rate.
This conclusion
applies at every level
of the roadmap.

At the Type 0 to Type I level,
faster energy growth
reduces the time
spent in the survival bottleneck.
Every additional year
at pre-Type I levels
is an additional year
of existential vulnerability.

At the Type I to Type II level,
faster growth
means earlier Dyson swarm completion
and earlier access
to interstellar propulsion development.

At the Type II to Type III level,
faster colonization wave speed
means earlier galactic coverage
and earlier establishment
of defensive depth.

At the Type III to competitive level,
faster SMBH growth
and resource accumulation
means earlier parity
with potential adversaries.

The growth imperative
is not a policy preference.
It is a structural consequence
of competitive dynamics.
A civilization that grows slowly
will be overtaken
by a civilization that grows quickly.
This conclusion holds
regardless of whether
any competitor currently exists.
It is sufficient
that a competitor might exist.

### The Concealment-Growth Tradeoff

The companion assessment article
demonstrated that
concealment has value
but imposes a growth rate penalty.
This tradeoff
operates at every level
of the roadmap.

At the Type 0 to Type I level,
humanity's electromagnetic emissions
have been propagating
into space for approximately 100 years.
The concealment question
is already partially moot
for observers within 100 light-years.
For intergalactic observers,
humanity is currently invisible.
The question is whether
to accelerate growth
at the cost of increased visibility
or to prioritize concealment
at the cost of extended
existential vulnerability.

The analysis suggests
that growth dominates concealment
at every level.
The competitive selection argument
from the companion causality article
establishes that
over cosmic timescales,
slow growers are eliminated.
Concealment slows growth.
Therefore concealment
is a losing strategy
in the long run.

This does not mean
that concealment
should be abandoned immediately.
Tactical concealment
during the early stages
of the Type 0 to Type I transition
may reduce risk
from any observer
within detection range.
But strategic concealment
as a permanent posture
is incompatible
with the growth imperative.

### Independence from Threat Assessment

This roadmap
does not require knowing
whether threats currently exist.
The argument proceeds
from the precautionary principle
under existential risk.

If competitive civilizations exist,
the roadmap is necessary
for survival.
If they do not exist,
the roadmap is still valuable
as a framework
for civilizational development.
The energy, technology,
and governance capabilities
described at each level
are intrinsically useful
regardless of whether
they are ever needed
for competitive purposes.

The cost of preparation
when no threat exists
is the resource expenditure
of accelerated growth.
The cost of non-preparation
when threats do exist
is extinction
or permanent subordination.
The asymmetry favors preparation.

### What This Analysis Does Not Capture

Several important factors
lie outside the scope
of this analysis.

**Cooperative equilibria.**
The competitive framing
assumes that civilizations
interact primarily
through conflict
and resource competition.
If civilizations
can communicate,
negotiate,
and establish binding agreements
across intergalactic distances,
cooperative equilibria may dominate.
The $2d$-year communication delay
makes negotiation difficult
but not impossible
over sufficiently long timescales.

**Non-expansion strategies.**
The analysis assumes
that expansion is rational.
A civilization might choose
to invest in
internal development,
simulation,
or contemplation
rather than physical expansion.
A [Matrioshka brain][ref_matrioshka]
converting all available energy
into computation
represents an alternative
to physical colonization.

**Radically different life.**
The analysis assumes
that competitors
are roughly comparable
in their basic capabilities
and constraints.
A civilization based on
fundamentally different physics
or operating in
a fundamentally different medium
might not follow
the competitive logic
described here.

## Conclusion

This article completes
a three-part analysis.

[Causality and First-Mover Advantage][related_post_causality]
established the theoretical framework.
The speed of light
imposes the $2d$-year offensive gap.
First-mover advantage
is effectively irreversible.
Competitive expansion
is the rational strategy
under the most severe assumptions.

The [Tactical and Strategic Assessment
of the Local Galactic Neighborhood][related_post_assessment]
applied that framework
to the specific galaxies
in our neighborhood.
The Milky Way
is poorly armed
relative to Andromeda, M87,
and the Virgo Cluster.
Growth rate is competitively selected.
Information warfare
cannot substitute
for physical resource development.
The first target
is the Large Magellanic Cloud.
The long-term concern
is the Virgo Cluster.

This article
provides the operational roadmap.
The path from $K \approx 0.73$
to competitive Type III
traverses four major transitions,
each with its own bottleneck,
timescale,
and failure mode.

The first transition
is the most urgent
and the most dangerous.
A pre-Type I civilization
that fails to manage
existential risk
ceases to exist.
Every other transition
is contingent on surviving this one.

The second transition
is the most transformative.
Mastering self-replicating technology
and constructing a Dyson swarm
transforms a planetary civilization
into a stellar one.
The energy gap of $10^{10}$
is bridged in centuries
once the key technology
is in hand.

The third transition
is the longest.
Colonizing the Milky Way
takes millions of years
even at optimistic expansion speeds.
The governance challenges
of maintaining coherence
across 100,000 light-years
may be as difficult
as the propulsion challenges
of crossing those distances.

The fourth transition
is the most uncertain.
Competitive viability
in the Local Group
depends on variables
that cannot be measured
from our current position.
The SMBH mass of Andromeda's core.
The existence or non-existence
of civilizations in nearby galaxies.
The possibility of threats
from the Virgo Cluster.

The roadmap is steep
but each step follows logically
from the one before it.
The backwards derivation
ensures that no step is wasted.
Every capability developed
at one level
is prerequisite
for the next.

The first move
remains the same
as in the companion articles.
Survive.
Grow.
Reach the stars
before whatever else is out there
reaches us.

## Future Reading

- [Eternity in Six Hours][research_eternity] by Armstrong and Sandberg demonstrates the feasibility of colonizing the entire observable universe from a single star system using self-replicating probes.
- [The Precipice][research_ord] by Toby Ord provides a rigorous analysis of existential risk and estimates the probability of civilizational catastrophe during the current century.
- The [Kardashev scale][ref_kardashev] article provides the historical context for Kardashev's original classification and Sagan's logarithmic extension.
- The [Grabby Aliens][research_grabby] model by Hanson, Rounding, and Martin connects the timing of human emergence to the expansion dynamics of alien civilizations.
- The [Breakthrough Starshot][ref_breakthrough_starshot] initiative represents the most concrete current proposal for interstellar propulsion.
- [Fogg's intergalactic colonization analysis][research_fogg] is the foundational treatment of the engineering constraints for crossing intergalactic voids, identifying system reliability over multimillion-year timescales as the principal challenge.
- The companion [Tactical and Strategic Assessment][related_post_assessment] provides the galaxy-by-galaxy data underlying the competitive analysis.

## References

- [Reference, AI Alignment][ref_ai_alignment]
- [Reference, Alcubierre Drive][ref_alcubierre]
- [Reference, Andromeda Galaxy][ref_andromeda]
- [Reference, Antimatter Rocket][ref_antimatter_rocket]
- [Reference, Asteroid Mining][ref_asteroid_mining]
- [Reference, Blandford-Znajek Process][ref_blandford_znajek]
- [Reference, Breakthrough Starshot][ref_breakthrough_starshot]
- [Reference, Bussard Ramjet][ref_bussard]
- [Reference, Colonization of Mars][ref_mars_colonization]
- [Reference, Cosmic Web][ref_cosmic_web]
- [Reference, Dark Forest Hypothesis][ref_dark_forest]
- [Reference, Drake Equation][ref_drake]
- [Reference, Dyson Sphere][ref_dyson_sphere]
- [Reference, Existential Risk][ref_existential_risk]
- [Reference, Exponential Growth][ref_exponential]
- [Reference, Fermi Paradox][ref_fermi]
- [Reference, Fusion Power][ref_fusion]
- [Reference, Generation Ship][ref_generation_ship]
- [Reference, Gray Goo][ref_gray_goo]
- [Reference, Great Filter][ref_great_filter]
- [Reference, Hypervelocity Star][ref_hypervelocity_star]
- [Reference, Intergalactic Medium][ref_igm]
- [Reference, Iron Law of Oligarchy][ref_iron_law]
- [Reference, ITER][ref_iter]
- [Reference, Kardashev Scale][ref_kardashev]
- [Reference, Laniakea Supercluster][ref_laniakea]
- [Reference, Large Magellanic Cloud][ref_lmc]
- [Reference, Laser Propulsion][ref_laser_propulsion]
- [Reference, Local Group][ref_local_group]
- [Reference, Matrioshka Brain][ref_matrioshka]
- [Reference, Mercury][ref_mercury]
- [Reference, Messier 87][ref_m87]
- [Reference, Milky Way][ref_milky_way]
- [Reference, Nuclear Pulse Propulsion][ref_nuclear_pulse]
- [Reference, Nuclear Winter][ref_nuclear_winter]
- [Reference, O'Neill Cylinder][ref_oneill]
- [Reference, Penrose Process][ref_penrose]
- [Reference, Photon Rocket][ref_photon_rocket]
- [Reference, Planetary Engineering][ref_planetary_engineering]
- [Reference, Sagittarius A*][ref_sagittarius_a]
- [Reference, Self-Replicating Machine][ref_self_replicating]
- [Reference, Self-Replicating Spacecraft][ref_self_replicating_spacecraft]
- [Reference, Shkadov Thruster][ref_shkadov]
- [Reference, Space-Based Solar Power][ref_sbsp]
- [Reference, Star Lifting][ref_star_lifting]
- [Reference, Stellar Engine][ref_stellar_engine]
- [Reference, Terraforming][ref_terraforming]
- [Reference, Toby Ord][ref_ord]
- [Reference, Virgo Cluster][ref_virgo_cluster]
- [Related Post, Causality and First-Mover Advantage in Lightcone-Based Competitive Intergalactic Colonization][related_post_causality]
- [Related Post, Cryptotelemeritocracy][related_post_cryptotelemeritocracy]
- [Related Post, Cryptotelemeritocracy for Space Exploitation][related_post_crypto_space]
- [Related Post, Human Evolution and the Great Filter][related_post_great_filter]
- [Related Post, Introduction to Astronomy][related_post_astronomy]
- [Related Post, Introduction to Space Studies][related_post_space_studies]
- [Related Post, Tactical and Strategic Assessment of the Local Galactic Neighborhood][related_post_assessment]
- [Related Post, Telemeritocracy][related_post_telemeritocracy]
- [Research, Armstrong and Sandberg, Eternity in Six Hours][research_eternity]
- [Research, Fogg, The Feasibility of Intergalactic Colonisation and its Relevance to SETI][research_fogg]
- [Research, Hanson, Rounding, and Martin, If Loud Aliens Explain Human Earliness, Quiet Aliens Are Also Rare][research_grabby]
- [Research, Heller and Hippke, Deceleration of High-Velocity Interstellar Photon Sails][research_heller_hippke]
- [Research, Milky Way-Andromeda Collision Probability, Nature Astronomy 2025][research_mw_andromeda_collision]
- [Research, Ord, The Precipice][research_ord]
- [Research, Wright et al., G-HAT Infrared Survey][research_ghat]

[ref_ai_alignment]: https://en.wikipedia.org/wiki/AI_alignment
[ref_alcubierre]: https://en.wikipedia.org/wiki/Alcubierre_drive
[ref_andromeda]: https://en.wikipedia.org/wiki/Andromeda_Galaxy
[ref_antimatter_rocket]: https://en.wikipedia.org/wiki/Antimatter_rocket
[ref_asteroid_mining]: https://en.wikipedia.org/wiki/Asteroid_mining
[ref_blandford_znajek]: https://en.wikipedia.org/wiki/Blandford%E2%80%93Znajek_process
[ref_breakthrough_starshot]: https://en.wikipedia.org/wiki/Breakthrough_Starshot
[ref_bussard]: https://en.wikipedia.org/wiki/Bussard_ramjet
[ref_cosmic_web]: https://en.wikipedia.org/wiki/Observable_universe#Large-scale_structure
[ref_dark_forest]: https://en.wikipedia.org/wiki/Dark_forest_hypothesis
[ref_drake]: https://en.wikipedia.org/wiki/Drake_equation
[ref_dyson_sphere]: https://en.wikipedia.org/wiki/Dyson_sphere
[ref_existential_risk]: https://en.wikipedia.org/wiki/Existential_risk
[ref_exponential]: https://en.wikipedia.org/wiki/Exponential_growth
[ref_fermi]: https://en.wikipedia.org/wiki/Fermi_paradox
[ref_fusion]: https://en.wikipedia.org/wiki/Fusion_power
[ref_generation_ship]: https://en.wikipedia.org/wiki/Generation_ship
[ref_gray_goo]: https://en.wikipedia.org/wiki/Gray_goo
[ref_great_filter]: https://en.wikipedia.org/wiki/Great_Filter
[ref_hypervelocity_star]: https://en.wikipedia.org/wiki/Hypervelocity_star
[ref_igm]: https://en.wikipedia.org/wiki/Intergalactic_medium
[ref_iron_law]: https://en.wikipedia.org/wiki/Iron_law_of_oligarchy
[ref_iter]: https://en.wikipedia.org/wiki/ITER
[ref_kardashev]: https://en.wikipedia.org/wiki/Kardashev_scale
[ref_laniakea]: https://en.wikipedia.org/wiki/Laniakea_Supercluster
[ref_laser_propulsion]: https://en.wikipedia.org/wiki/Laser_propulsion
[ref_lmc]: https://en.wikipedia.org/wiki/Large_Magellanic_Cloud
[ref_local_group]: https://en.wikipedia.org/wiki/Local_Group
[ref_m87]: https://en.wikipedia.org/wiki/Messier_87
[ref_mars_colonization]: https://en.wikipedia.org/wiki/Colonization_of_Mars
[ref_matrioshka]: https://en.wikipedia.org/wiki/Matrioshka_brain
[ref_mercury]: https://en.wikipedia.org/wiki/Mercury_(planet)
[ref_milky_way]: https://en.wikipedia.org/wiki/Milky_Way
[ref_nuclear_pulse]: https://en.wikipedia.org/wiki/Nuclear_pulse_propulsion
[ref_nuclear_winter]: https://en.wikipedia.org/wiki/Nuclear_winter
[ref_oneill]: https://en.wikipedia.org/wiki/O%27Neill_cylinder
[ref_ord]: https://en.wikipedia.org/wiki/Toby_Ord
[ref_penrose]: https://en.wikipedia.org/wiki/Penrose_process
[ref_photon_rocket]: https://en.wikipedia.org/wiki/Photon_rocket
[ref_planetary_engineering]: https://en.wikipedia.org/wiki/Planetary_engineering
[ref_sagittarius_a]: https://en.wikipedia.org/wiki/Sagittarius_A*
[ref_sbsp]: https://en.wikipedia.org/wiki/Space-based_solar_power
[ref_self_replicating]: https://en.wikipedia.org/wiki/Self-replicating_machine
[ref_self_replicating_spacecraft]: https://en.wikipedia.org/wiki/Self-replicating_spacecraft
[ref_shkadov]: https://en.wikipedia.org/wiki/Shkadov_thruster
[ref_star_lifting]: https://en.wikipedia.org/wiki/Star_lifting
[ref_stellar_engine]: https://en.wikipedia.org/wiki/Stellar_engine
[ref_terraforming]: https://en.wikipedia.org/wiki/Terraforming
[ref_virgo_cluster]: https://en.wikipedia.org/wiki/Virgo_Cluster
[related_post_causality]: {% post_url 2026-03-01-causality_and_first_mover_advantage_in_lightcone_based_competitive_intergalactic_colonization %}
[related_post_assessment]: {% post_url 2026-03-02-tactical_and_strategic_assessment_of_local_galactic_neighborhood %}
[related_post_astronomy]: {% post_url 2026-02-12-introduction_to_astronomy %}
[related_post_cryptotelemeritocracy]: {% post_url 2026-02-20-cryptotelemeritocracy %}
[related_post_crypto_space]: {% post_url 2026-02-23-cryptotelemeritocracy_for_space_exploitation %}
[related_post_great_filter]: {% post_url 2026-02-26-human_evolution_and_the_great_filter %}
[related_post_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[related_post_telemeritocracy]: {% post_url 2026-02-19-telemeritocracy %}
[research_eternity]: https://www.sciencedirect.com/science/article/abs/pii/S0094576513001148
[research_fogg]: https://ui.adsabs.harvard.edu/abs/1988JBIS...41..491F
[research_ghat]: https://arxiv.org/abs/1408.1133
[research_grabby]: https://arxiv.org/abs/2102.01522
[research_heller_hippke]: https://arxiv.org/abs/1701.08803
[research_mw_andromeda_collision]: https://www.nature.com/articles/s41550-025-02563-1
[research_ord]: https://theprecipice.com/
