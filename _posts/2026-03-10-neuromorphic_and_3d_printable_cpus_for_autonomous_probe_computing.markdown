---
layout: post
mathjax: true
comments: true
title:  "Neuromorphic and 3D Printable CPUs for Autonomous Probe Computing"
date:   2026-03-10 09:47:00 +0000
categories: science philosophy
series: intergalactic_competition
series_title: Intergalactic Competition
series_index: 8
---
<!-- A105 -->
<script>console.log("A105");</script>

The companion articles on
[von Neumann probes][related_post_von_neumann_probes],
the
[error correction recursion problem][related_post_error_correction],
and
[pre-transistor computing][related_post_steampunk]
established that semiconductor fabrication
represents the single hardest closure gap
for self-replicating spacecraft.
The
[roadmap article][related_post_roadmap]
placed this closure gap
in the broader context
of competitive expansion strategy.
Modern integrated circuits
require photolithography
with nanometer resolution,
silicon of extreme purity,
and clean room environments
that no autonomous extraterrestrial factory
could plausibly reproduce.

The previous article explored
one response to this problem,
examining pre-transistor computing technologies
that sidestep semiconductor fabrication entirely.
Mechanical computers, analog electronics,
and hybrid systems
offer manufacturing requirements
that are orders of magnitude
less demanding than modern chip production.
That approach trades performance
for manufacturability.

This article examines two additional approaches
that occupy a middle ground
between conventional semiconductor fabrication
and pre-transistor alternatives.
Neuromorphic computing
draws inspiration from biological neural systems
to build processors
that compute through networks
of spiking neurons
rather than through
Boolean logic gates.
Three-dimensionally printable computing
uses additive manufacturing techniques
to deposit electronic circuits
layer by layer,
potentially enabling a probe
to fabricate processors
without the photolithographic infrastructure
that conventional chip production demands.

Both approaches share a common property.
They reduce the manufacturing precision
required to produce functional computing hardware,
though by different mechanisms
and to different degrees.
Neuromorphic processors
tolerate imprecise components
because neural networks
are inherently fault-tolerant.
Printed processors
tolerate imprecise fabrication
because additive manufacturing
can operate at feature sizes
measured in micrometers
rather than nanometers.

The central question of this article
is whether neuromorphic or printed computing architectures
could provide practical processing capabilities
for long-duration autonomous systems
such as von Neumann probes,
with manufacturing requirements
achievable by an autonomous industrial system
operating from raw materials.
The article surveys the history,
current state,
and future trajectory
of both technologies,
evaluates their suitability
for probe computing workloads,
and examines how they might integrate
with the mechanical and analog systems
described in the companion article.

## Neuromorphic Computing

### History

The intellectual foundations
of neuromorphic computing
predate electronic computers entirely.
Warren McCulloch and Walter Pitts
published their model
of the formal neuron in 1943,
demonstrating that networks
of simplified neurons
could compute any function
computable by a Turing machine.
The [McCulloch-Pitts neuron][ref_mcculloch_pitts]
represented a binary threshold unit
that fires when the weighted sum
of its inputs exceeds a threshold.
This was a mathematical abstraction,
not an engineering proposal,
but it established
the theoretical connection
between neural computation
and general-purpose computing.

[Alan Hodgkin and Andrew Huxley][ref_hodgkin_huxley]
published their biophysical model
of the action potential in 1952,
describing how neurons generate
and propagate electrical spikes
through voltage-gated ion channels
in the squid giant axon.
The Hodgkin-Huxley model
earned the 1963 Nobel Prize
in Physiology or Medicine
and provided the quantitative foundation
for all subsequent work
on biologically realistic
neural simulation.

Frank Rosenblatt built
the Mark I [Perceptron][ref_perceptron]
at the Cornell Aeronautical Laboratory in 1958,
the first hardware implementation
of a neural network
capable of learning.
The Perceptron used
400 photocells connected
to a layer of artificial neurons
with adjustable weights.
Learning occurred
through an error-correction rule
that adjusted weights
based on the difference
between desired and actual outputs.
The machine demonstrated
that hardware neural networks
could learn to classify patterns,
but Marvin Minsky and Seymour Papert's
1969 analysis of the Perceptron's limitations
contributed to a reduction
in neural network research funding
that lasted roughly two decades.

Leon Chua postulated
the [memristor][ref_memristor] in 1971
as the fourth fundamental
passive circuit element,
characterized by a relationship
between charge and magnetic flux linkage.
The memristor's resistance
depends on the history
of current that has flowed through it,
providing a natural electronic analog
of the biological synapse.
This theoretical prediction
would wait 37 years
for physical demonstration.

The term "neuromorphic"
was coined by
[Carver Mead][ref_carver_mead]
in his 1990 paper
"Neuromorphic Electronic Systems"
published in the Proceedings of the IEEE.
Mead argued that analog
Very Large Scale Integration (VLSI) circuits
could implement neural computation
far more efficiently
than digital simulation,
because the physics of transistors
operating in the subthreshold regime
naturally implements
the exponential and logarithmic functions
that describe biological neural dynamics.
His earlier 1989 book
"Analog VLSI and Neural Systems"
laid the engineering groundwork
for this approach.
Mead's insight was
that the "imprecision" of analog circuits
was not a defect to be corrected
but a feature to be exploited,
because biological neural networks
operate with components
that are far less precise
than any manufactured transistor.

The decade following Mead's paper
saw the development
of several early neuromorphic chips.
The silicon retina,
designed by Mead and Mahowald in 1991,
demonstrated that an analog VLSI circuit
could replicate the spatial and temporal
processing of the vertebrate retina.
The silicon cochlea
performed analogous processing
for auditory signals.
These early demonstrations
established that neuromorphic hardware
could process sensory information
with orders of magnitude less power
than digital alternatives.

The field experienced
a significant acceleration
in the 2010s
as advances in fabrication technology
and machine learning theory
converged to make
large-scale neuromorphic processors feasible.
IBM's [TrueNorth][ref_truenorth] chip in 2014,
Intel's [Loihi][ref_loihi] chip in 2018,
and the [SpiNNaker][ref_spinnaker] machine
at the University of Manchester
represented three distinct architectural approaches
to neuromorphic computing at scale.

### Historical and Modern Examples

**IBM TrueNorth (2014).**
The TrueNorth chip
was designed at IBM Research
under the Defense Advanced Research Projects Agency
(DARPA) SyNAPSE program.
It contains 5.4 billion transistors
organized into 4,096 neurosynaptic cores,
each implementing 256 neurons
with 256 synapses per neuron,
for a total of approximately
one million neurons
and 256 million synapses.
TrueNorth was fabricated
in Samsung's 28 nanometer process
and consumes approximately
65 milliwatts during typical workloads,
roughly three orders of magnitude
less power than a conventional processor
performing equivalent pattern recognition tasks.
The chip uses a digital implementation
of spiking neurons
with deterministic operation,
event-driven communication,
and no shared global clock.
Merolla et al. published
the TrueNorth architecture
in Science in 2014.

**Intel Loihi (2018) and Loihi 2 (2021).**
Intel's neuromorphic research chip
[Loihi][ref_loihi]
was described by Davies et al. in 2018.
Fabricated in Intel's 14 nanometer process,
the 60 square millimeter chip
contains 128 neuromorphic cores
with a total capacity
of approximately 130,000 neurons
and 130 million synapses.
Loihi's distinguishing feature
is programmable on-chip learning.
Each synapse can execute
a programmable learning rule
at every spike,
enabling the chip
to implement
[Spike-Timing-Dependent Plasticity][ref_stdp]
(STDP)
and other biologically inspired
learning algorithms
directly in hardware.
Loihi demonstrated
over three orders of magnitude
improvement in energy-delay product
compared to conventional processors
on certain optimization problems.

Loihi 2, announced in 2021,
moved to Intel's pre-production Intel 4 process
and increased capacity
to approximately one million neurons per chip
with 120 million synapses
across 128 neuron cores.
The chip offers
15 times increased density
over its predecessor
at half the die area.
The Hala Point system,
assembled from 1,152 Loihi 2 chips,
contains approximately 1.15 billion neurons
and 128 billion synapses
across 140,544 neuromorphic processing cores,
making it the largest
neuromorphic system
built to date.
Hala Point achieves
up to 20 petaops
at over 15 trillion operations
per second per watt (TOPS/W).

**SpiNNaker (2013 onward).**
The Spiking Neural Network Architecture
([SpiNNaker][ref_spinnaker])
project at the University of Manchester,
led by Steve Furber,
took a fundamentally different approach.
Rather than designing custom
neural silicon,
SpiNNaker used a massively parallel array
of conventional ARM968 processors
connected by a custom
packet-switched network.
The first full-scale SpiNNaker machine,
completed in 2018,
contained 57,600 processing nodes
with 18 ARM cores each,
totaling 1,036,800 cores
and over 7 terabytes of RAM,
capable of simulating
approximately one billion neurons
in biological real time.
Each core runs
a software neuron model,
and spikes are communicated
as small multicast packets
across the network.
Furber et al. published
the SpiNNaker architecture
in the Proceedings of the IEEE in 2014.
The project was supported
by the European Human Brain Project.

SpiNNaker 2,
under development at TU Dresden,
uses a custom 22 nanometer chip
with 152 ARM cores per die
and dedicated neural processing elements,
combining SpiNNaker's
software flexibility
with hardware acceleration
for neural dynamics.
Over 34,500 SpiNNaker 2 chips
have been fabricated.

**BrainScaleS (2010 onward).**
The [BrainScaleS][ref_brainscales] system
at Heidelberg University
represents the analog extreme
of neuromorphic hardware.
Where TrueNorth and SpiNNaker
use digital circuits
to simulate neural dynamics,
BrainScaleS implements neurons
and synapses
using physical analog circuits.
The system operates
in an accelerated time domain,
running approximately 1,000 times
faster than biological real time.
The BrainScaleS-2 chip
implements 512 adaptive
integrate-and-fire neuron circuits,
131,000 plastic synapses,
analog parameter storage,
embedded processors,
and digital event routing,
using mixed-signal
analog and digital circuitry
in a 65 nanometer CMOS process.
Because the neuron circuits
are physical analogs
of biological neurons,
they exhibit the same
variability and noise
as their biological counterparts.
The system must learn
to compute despite
this component variability,
which makes it
a natural testbed
for studying fault tolerance
in neural computation.
BrainScaleS-2 is available
for free research access
through the EBRAINS platform.

**BrainChip Akida (2021 onward).**
The Akida processor
from [BrainChip][ref_brainchip]
is one of the few
commercially available
neuromorphic processors.
Akida targets edge inference
and uses a digital,
event-based AI architecture
optimized for deployment
in embedded systems.
The processor features
a scalable fabric
of 1 to 128 nodes
supporting Convolutional Neural Networks (CNNs),
Recurrent Neural Networks (RNNs),
and Temporal Event-based
Neural Networks (TENNs)
in a spiking framework.
The Akida Pico variant
draws under one milliwatt under load.
Akida 2.0 adds
8-bit weight and activation support,
vision transformer acceleration,
and configurable local scratchpads.
BrainChip has targeted
automotive, industrial,
and Internet of Things applications.
An Akida unit was launched
on a SpaceX Falcon 9,
marking one of the first
commercial neuromorphic processors
to reach orbit.

**Tianjic (2019).**
The Tianjic chip
from Tsinghua University
demonstrated a hybrid architecture
that can run both
conventional artificial neural networks
and [spiking neural networks][ref_snn]
on the same hardware.
Fabricated as a 28 nanometer prototype
achieving over 610 gigabytes per second
of internal memory bandwidth,
the chip was demonstrated
controlling an autonomous bicycle robot
that simultaneously performed
object detection, voice recognition,
and balance control.
Pei et al. published
the Tianjic architecture
in Nature in 2019,
showing that hybrid
neural architectures
can handle multiple
distinct computing tasks
on a single chip.

**Memristor-Based Systems.**
The [memristor][ref_memristor],
theoretically described
by Leon Chua in 1971
and first physically demonstrated
by Strukov et al. at HP Labs in 2008
as a titanium dioxide device,
provides a natural substrate
for neuromorphic computing.
A memristor's resistance
depends on the history
of current that has flowed through it,
providing an analog
of synaptic weight
that persists without power.
[Resistive Random-Access Memory][ref_rram] (ReRAM),
a commercial memory technology
based on memristive switching,
has been used to build
crossbar arrays
that implement
matrix-vector multiplication
in a single step.
This operation
is the fundamental computation
in both conventional
and spiking neural networks.
Multiple research groups
have demonstrated
neuromorphic processors
built from memristor crossbar arrays,
including a 54 by 108 passive array
integrated with CMOS interface circuitry,
digital buses,
and an OpenRISC processor
at the University of Michigan.
Memristive devices
can program
multiple non-volatile states,
approximately 100 levels,
with switching energy
as low as approximately 10 femtojoules
per state transition.

### State of the Art

Contemporary neuromorphic processors
span a range of architectures,
but they share
several common properties.

**Spiking Neural Networks.**
Most neuromorphic hardware
implements some form of
[Spiking Neural Network][ref_snn] (SNN).
Unlike conventional artificial neural networks,
which process information
as continuous-valued activations,
SNNs communicate through
discrete events called spikes.
A neuron accumulates input spikes,
integrates them over time,
and fires an output spike
when its membrane potential
exceeds a threshold.
This event-driven behavior
means that neurons
consume energy
only when they fire,
not continuously.
In workloads where
only a small fraction of neurons
are active at any given time,
this sparse activation pattern
yields substantial power savings.
Various decoding methods
exist for interpreting
the outgoing spike train
as a real-value number,
relying on either
the frequency of spikes,
the time to first spike
after stimulation,
or the interval between spikes.

**Learning Rules.**
On-chip learning in neuromorphic systems
uses several approaches.
[Spike-Timing-Dependent Plasticity][ref_stdp]
(STDP)
is a biologically observed rule
in which synaptic strength increases
when a presynaptic spike
precedes a postsynaptic spike
within a narrow time window
and decreases
when the order is reversed.
STDP is an unsupervised,
temporally asymmetric form
of [Hebbian learning][ref_hebbian]
that can be implemented
with purely local information,
requiring no global error signal
and no backpropagation.
The rule was first observed
in biological systems by Markram et al. in 1997
and formalized by
Bi and Poo in 1998.
Surrogate gradient methods,
established by the foundational tutorial
of Neftci, Mostafa, and Zenke (2019),
approximate the non-differentiable
spike function
with a smooth surrogate
during the backward pass,
enabling gradient descent training
of spiking networks.
These methods have closed
much of the accuracy gap
between SNNs and conventional networks
on standard benchmarks.

**Power Consumption.**
Neuromorphic processors
achieve power consumption
measured in milliwatts
for workloads
that require watts
on conventional hardware.
TrueNorth consumes 65 milliwatts.
BrainChip's Akida Pico
operates under one milliwatt.
Loihi-based systems
perform AI inference
using approximately 100 times less energy
at speeds up to 50 times faster
than conventional CPU and GPU architectures.
These figures represent
improvements of 100 to 1,000 times
compared to conventional processors
performing equivalent inference tasks.
The power advantage stems from
event-driven computation,
co-located memory and processing,
and the elimination of
the von Neumann bottleneck
between separate memory and processor.

**Manufacturing.**
Current neuromorphic chips
are manufactured using
standard semiconductor processes
at nodes ranging from
65 nanometers (BrainScaleS-2)
to 14 nanometers (Loihi)
and the Intel 4 node (Loihi 2).
The manufacturing requirements
are currently identical
to those of conventional processors.
However, the fault tolerance
of neural network architectures
means that neuromorphic designs
could potentially function
at much larger feature sizes
than conventional digital logic,
because individual component variability
does not prevent
the network as a whole
from computing correctly.
This property has been demonstrated
by BrainScaleS,
which deliberately operates
with analog component variability
and uses learning
to compensate for
device mismatch.

### Contemporary Applications

Neuromorphic computing
has found applications
in several domains
where its power efficiency
and event-driven processing
provide advantages
over conventional architectures.

**Edge AI and Sensor Processing.**
The most mature application area
is inference at the edge,
where neuromorphic processors
process sensor data locally
without transmitting it
to a cloud server.
Event cameras,
which output spikes
only when pixels change,
pair naturally
with neuromorphic processors
to create vision systems
that consume milliwatts of power
and achieve microsecond-level
visual processing
for object tracking and classification.
BrainChip's Akida
targets this market.
The neuromorphic computing market
is projected to grow
from 28.5 million dollars in 2024
to 1.33 billion dollars by 2030.

**Robotics.**
Neuromorphic processors
have been demonstrated
in robotic control systems
where their low latency
and low power consumption
are advantageous.
The Tianjic bicycle robot
demonstrated real-time
multimodal sensory processing
and motor control
on a single chip.
Intel's Loihi
powers warehouse robots
with real-time sensor fusion
combining LIDAR and camera data,
reducing energy consumption
by approximately 40 percent.
Researchers have used
Loihi for robotic arm control,
gesture recognition,
and adaptive locomotion.

**Optimization.**
Loihi has demonstrated
significant advantages
on constraint satisfaction
and optimization problems.
Spiking networks
can naturally represent
and solve problems
expressible as energy minimization
in recurrent networks,
including graph coloring,
satisfiability,
and shortest path problems.
The original Loihi paper
demonstrated over three orders of magnitude
improvement in energy-delay product
on LASSO optimization problems
compared to conventional solvers.

**Scientific Simulation.**
SpiNNaker's primary mission
is computational neuroscience,
simulating biological neural circuits
in biological real time
to test hypotheses
about brain function.
This application
demonstrates that neuromorphic hardware
can serve as
a general-purpose simulator
for complex dynamical systems.

**Space Applications.**
Several research groups
and space agencies
have investigated
neuromorphic computing
for space applications.
NASA's TechEdSat-13 mission in 2022
achieved the first orbital flight
of a neuromorphic processor,
an Intel Loihi chip,
launched on a Virgin Orbit LauncherOne.
The mission achieved
comprehensive success.
NASA's Jet Propulsion Laboratory
has investigated
neuromorphic approaches
to autonomous navigation
and terrain classification
for planetary rovers,
including neuromorphic event cameras
paired with SNNs
for Mars helicopter autonomy.
The European Space Agency's
Neuro SatCom project
evaluates neuromorphic processors,
specifically SpiNNaker,
for satellite communication
interference detection
and beam management.
ESA's NEUROSPACE project
in 2024 targets
neuromorphic AI acceleration
in space-grade microprocessors.
The Falco Neuro project
operates neuromorphic cameras
on the International Space Station.

### Von Neumann Probe Computing Requirements

A self-replicating probe
must perform several categories
of computation continuously
over mission durations
measured in centuries to millennia.
These requirements differ
from terrestrial computing workloads
in their emphasis
on reliability over performance,
energy efficiency over throughput,
and autonomous adaptation
over user-directed processing.

**Navigation and Guidance.**
Interstellar navigation requires
processing star field images,
computing trajectory corrections,
and maintaining an inertial reference frame
over decades of continuous operation.
These are predominantly
signal processing
and linear algebra tasks
with moderate precision requirements.
A probe approaching
a target star system
must additionally classify
planetary bodies,
assess resource availability,
and select landing sites.
These tasks require
pattern recognition capabilities.

**Manufacturing Control.**
Self-replication demands
real-time control
of mining, refining,
and fabrication processes.
Manufacturing control
is predominantly
a feedback loop task,
reading sensor values
and adjusting actuators
to maintain process parameters
within tolerance.
The companion article
on [pre-transistor computing][related_post_steampunk]
demonstrated that analog systems
excel at this category of computation.

**System Monitoring and Repair.**
A probe must continuously monitor
its own subsystems,
detect degradation and failures,
diagnose root causes,
and either repair damage
or reconfigure around failed components.
This requires
anomaly detection,
causal reasoning,
and planning capabilities.

**Communication Encoding and Decoding.**
Interstellar communication
at any data rate
requires error-correcting codes
of substantial complexity.
The companion article
on [error correction][related_post_error_correction]
demonstrated that
digital computation
is essential for this task.
Encoding and decoding
turbo codes or
Low-Density Parity-Check (LDPC) codes
requires discrete arithmetic
that is not well suited
to analog implementation.

**Scientific Data Processing.**
A probe conducting
astronomical observations,
geological surveys,
or atmospheric analysis
must process, compress,
and store scientific data.
The volume of raw data
may be large,
but the required throughput
is modest by terrestrial standards.

These requirements differ
from conventional terrestrial computing
in several important ways.
There is no human user
to provide real-time direction.
There is no opportunity
to download software updates
once the probe
has left communication range.
The computing system must operate
for centuries without hardware replacement.
Energy is strictly limited
to what the probe
can generate from nuclear
or solar sources.
And the penalty for computing errors
in certain critical tasks
is mission failure
with no possibility of recovery.

### Neuromorphic Computing in the Context of Probe Development

Neuromorphic processors
offer several properties
that align well
with probe computing requirements.

**Energy Efficiency.**
The orders-of-magnitude
power advantage
of neuromorphic processors
directly addresses
the energy constraints
of interstellar probes.
A probe powered
by a Radioisotope Thermoelectric Generator (RTG)
has a power budget
measured in hundreds of watts,
declining over decades
as the radioactive source decays.
Allocating milliwatts
rather than watts
to computing
leaves more power available
for propulsion, communication,
and manufacturing.
Event-driven computation
means zero power draw
during periods of no activity,
which is ideal
for long-duration interstellar transit
where the probe
may spend decades
in a low-activity cruise phase.

**Fault Tolerance.**
Neural networks
are inherently tolerant
of component failure.
A network can lose
a substantial fraction
of its neurons
or synapses
and continue to function
with graceful degradation
rather than catastrophic failure.
This property is critical
for a system
that must operate
for centuries
without hardware replacement.
The BrainScaleS system
demonstrates this property directly,
learning to compute correctly
despite significant
analog component variability.

**Radiation Tolerance.**
The fault tolerance
of neural networks
extends to radiation effects.
A single-event upset
that flips a bit
in a conventional processor
can crash the system
or produce incorrect results.
The same radiation event
in a neuromorphic processor
may perturb a few synaptic weights
or disrupt a single spike,
but the distributed nature
of neural computation
means the network
continues to produce
approximately correct outputs.
Naoukin et al. (2023)
surveyed radiation effects
on neuromorphic systems
and proposed radiation-aware algorithms.
NASA's 2022 study
on radiation tolerance
and mitigation
specifically evaluated
neuromorphic architectures
for space environments.
This radiation tolerance
parallels
the inherent adversarial robustness
of analog computing
described in the companion article,
as demonstrated by
Lammie et al. (2025).

**Adaptive Learning.**
On-chip learning
enables a neuromorphic processor
to adapt to
changing environmental conditions
without reprogramming.
A probe encountering
an unexpected situation,
such as unfamiliar geology
at a target star system,
could adjust its behavior
through learning
rather than relying
on pre-programmed responses.
Loihi's programmable learning rules
enable real-time environmental adaptation.
This capability
addresses one of the fundamental challenges
of autonomous systems
operating far
from human oversight.

**Manufacturing Challenges.**
The primary limitation
of neuromorphic computing
for probe applications
is that current neuromorphic chips
are manufactured using
the same semiconductor processes
as conventional processors.
A probe that cannot fabricate
14 nanometer digital logic
also cannot fabricate
14 nanometer neuromorphic logic.
The neuromorphic advantage lies
not in easier manufacturing
of current designs,
but in the potential
to build functional neuromorphic processors
at much larger feature sizes
than would be viable
for conventional digital logic.
A neuromorphic processor
built with micrometer-scale features
would be larger, slower,
and less energy-efficient
than a modern chip,
but it might still
compute correctly,
because neural networks
tolerate component variability
that would render
a conventional processor inoperable.

### Work in Progress and Partial Solutions

**Organic Neuromorphic Devices.**
Researchers have demonstrated
neuromorphic circuits
built from [organic semiconductors][ref_organic_semiconductor]
and organic electrochemical transistors.
These devices
use carbon-based materials
that can be deposited
from solution
using printing techniques,
eliminating the need
for high-temperature
semiconductor processing.
Organic neuromorphic devices
have demonstrated
synaptic plasticity,
short-term and long-term memory,
and basic learning capabilities.
Electrolyte-gated organic transistors
operate at ultra-low voltages
and mimic synaptic plasticity
with promising fidelity.
Their performance is orders of magnitude
slower than silicon devices,
but for applications
where speed is not the primary constraint,
organic neuromorphic circuits
offer a pathway
to neuromorphic computing
without semiconductor fabrication.

**Memristive Neuromorphic Systems.**
Memristor crossbar arrays
provide a natural implementation
of neural network computation.
Each crossbar junction
stores a synaptic weight
as a resistance value,
and matrix-vector multiplication
is performed by applying
input voltages to rows
and reading output currents
from columns.
This analog computation
occurs in a single step
regardless of array size,
providing inherent parallelism.
Memristive devices
can be fabricated
from a variety of metal oxides
using relatively simple
deposition and patterning techniques.
The feature sizes required
for functional memristor arrays
are significantly larger
than those required
for conventional transistor logic.
Active material research frontiers
include MXene-based,
organic,
and perovskite memristors.

**Photonic Neuromorphic Computing.**
Neuromorphic processors
built from optical components
use light rather than electricity
to implement neural computation.
Photonic integrated circuits
implement neural network operators
including coherent
matrix-vector multiplication
and nonlinear activation functions
at the speed of light.
Key advantages include
inherent parallelism
through wavelength-division multiplexing,
near-zero energy for linear operations,
and immunity
to electromagnetic interference.
The manufacturing requirements
for photonic systems
differ substantially
from electronic systems,
potentially offering
alternative fabrication pathways.

**Spintronic Neuromorphic Computing.**
Spintronic systems
using magnetic tunnel junctions,
domain walls,
and skyrmions
can achieve 20 TOPS/W.
Magnetic skyrmions
enable synaptic plasticity emulation
at as low as
0.14 femtojoules per operation.
Room-temperature skyrmion stabilization
with storage densities
exceeding 1 terabit per square inch
has been achieved.
Spintronic neuromorphic devices
represent an alternative pathway
that uses magnetic phenomena
rather than charge transport
for neural computation.

**Neuromorphic Computing at Extreme Temperatures.**
Space environments
subject electronics
to extreme temperature ranges.
Research into neuromorphic computing
at cryogenic temperatures
has shown that
some neuromorphic architectures
maintain functionality
across wider temperature ranges
than conventional digital logic.
Superconducting neuromorphic circuits
using Josephson junctions
operate at cryogenic temperatures
with extremely low power consumption.
Ferroelectric and MRAM devices
maintain neuromorphic functionality
at deep cryogenic temperatures,
relevant for outer solar system
and interstellar environments.

**3D Printed Neuromorphic Devices.**
Yan et al. (2025)
reviewed the convergence
of additive manufacturing
and neuromorphic engineering,
demonstrating 3D-printed memristors,
synaptic transistors,
and reservoir computers.
Shirmohammadli et al. (2023)
demonstrated a fully 3D-printed
contextual computer
using Fused Deposition Modeling (FDM) printing.
These results establish
that neuromorphic computing elements
can be fabricated
through additive manufacturing,
a finding of direct relevance
to probe self-replication.

### Hypothetical and Extrapolated Approaches

**Micrometer-Scale Neuromorphic Processors.**
If a probe could fabricate
transistors with feature sizes
of one to ten micrometers
using the additive manufacturing
or vacuum tube techniques
described in the companion article,
a neuromorphic processor
built at these feature sizes
would be physically large
but potentially functional.
A neuron circuit
that occupies
one square millimeter at micrometer scale
compared to
one square micrometer
at nanometer scale
implies a chip
that is one million times larger
in area per neuron.
A processor with 1,000 neurons,
each occupying one square millimeter,
would require a substrate
of approximately 32 by 32 millimeters,
a large but feasible device.
One thousand neurons
is a small network
by modern standards,
but biological organisms
with fewer than 1,000 neurons,
such as the nematode
[Caenorhabditis elegans][ref_c_elegans]
with its 302 neurons,
demonstrate that
useful behavior
is achievable
with very small neural networks.

**Memristor-Based Probe Computers.**
A probe that can refine metals
and deposit thin films
of metal oxides
could potentially fabricate
memristor crossbar arrays
as its primary computing substrate.
The manufacturing requirements
for memristive devices
are significantly simpler
than for transistor logic.
A memristor crossbar
implements both memory
and computation
in a single structure,
eliminating the need
for separate memory fabrication.
The resulting system
would be a neural network
that stores its weights
in the physical resistance
of its synapses,
with learning implemented
through the natural
memristive write mechanism.

**Hybrid Analog-Neuromorphic Architecture.**
The most plausible probe computing architecture
may combine analog computation
for low-level feedback control
with a neuromorphic processor
for higher-level pattern recognition,
anomaly detection,
and adaptive behavior.
The analog layer
would handle manufacturing control,
sensor processing,
and power management.
The neuromorphic layer
would handle navigation,
system health monitoring,
and decision-making.
A minimal digital core
would handle
communications encoding,
error correction,
and precise arithmetic
where required.
This three-tier architecture
extends the framework
proposed in the companion article
by replacing or augmenting
the minimal digital core
with a neuromorphic processor
that is more tolerant
of manufacturing imprecision.

**Evolved Neuromorphic Architectures.**
A probe civilization
that deploys millions of probes
across thousands of star systems
would generate an enormous
evolutionary search space
for neuromorphic architectures.
Each probe's neuromorphic processor
could be slightly different,
optimized for local conditions
through on-chip learning.
Over generations of replication,
the most effective architectures
would propagate.
This mirrors
the biological evolution
of neural circuits,
which produced
brains of extraordinary capability
through iterative variation
and selection
operating on relatively simple
neural components.

## 3D Printable Computing

### History

The history of printable computing
begins with
the broader history
of [printed electronics][ref_printed_electronics],
which traces back
to the development
of the [printed circuit board][ref_pcb] (PCB).
Paul Eisler invented
the printed circuit
in the United Kingdom around 1936,
using etched copper foil
on an insulating substrate
to create electrical connections.
The technology was adopted
for military applications
during World War II
and entered commercial production
in 1948.
By the 1960s,
printed circuit boards
had become the standard substrate
for all consumer electronics.

The transition
from printed interconnections
to printed components
began with [thick-film technology][ref_thick_film]
in the 1960s.
Screen printing
of conductive, resistive,
and dielectric pastes
onto ceramic substrates
enabled the fabrication
of passive electronic components,
including resistors,
capacitors,
and inductors,
using additive processes.
Typical film thickness ranges
from 0.1 to 100 micrometers.
Thick-film circuits
are still manufactured today
for automotive sensors,
medical devices,
and military electronics
where reliability
at extreme temperatures
is required.

The invention of
[inkjet printing][ref_inkjet_printing]
of electronic materials
in the late 1990s
and early 2000s
expanded the range
of printable electronic components.
Researchers demonstrated
that solutions of conductive nanoparticles,
semiconducting polymers,
and dielectric materials
could be deposited
through standard inkjet printheads
to form functional electronic devices.
The key enabling material
was [conductive ink][ref_conductive_ink],
initially based on
silver nanoparticles
suspended in a solvent.
When printed and sintered,
these inks form
conductive traces
with resistivity
within an order of magnitude
of bulk silver.

The development of
[organic semiconductors][ref_organic_semiconductor]
provided another pathway
to printed computing.
Organic materials
such as pentacene,
rubrene,
and various polymer semiconductors
can be deposited from solution
at low temperatures
onto flexible substrates
including plastic and paper.
[Organic Field-Effect Transistors][ref_ofet] (OFETs)
were first demonstrated in 1986,
and by the 2000s,
organic transistors
had achieved performance levels
sufficient for
simple logic circuits.

The convergence
of [three-dimensional printing][ref_additive_manufacturing] technology
with printable electronics
created the field
of 3D printed computing.
Additive manufacturing techniques,
originally developed
for mechanical prototyping,
were adapted
to deposit multiple materials,
including conductors,
semiconductors,
and insulators,
in a single build process.
This combination enables
the fabrication
of three-dimensional circuits
with embedded components,
a capability
that conventional planar PCB fabrication
does not provide.

### Historical and Modern Examples

**Optomec Aerosol Jet.**
Optomec's [Aerosol Jet][ref_aerosol_jet] technology
uses an aerosol stream
of nanoparticle ink
focused by a gas sheath
to deposit fine lines
of conductive, semiconductive,
or dielectric material.
The system achieves
minimum feature sizes
of approximately 10 micrometers,
roughly three orders of magnitude
larger than modern
semiconductor lithography
but sufficient for
many circuit applications.
Aerosol Jet printing
has been used
to print conformal antennas,
sensors,
interconnects,
and passive components
onto three-dimensional surfaces.
NASA has investigated
Aerosol Jet printing
for fabricating
electronic components in space.

**Nano Dimension DragonFly.**
The Nano Dimension DragonFly system
prints multilayer printed circuit boards
using inkjet deposition
of silver nanoparticle ink
for conductors
and a dielectric polymer
for insulation.
The system enables
rapid prototyping
of PCBs
without the chemical etching
and photolithographic processes
of conventional PCB fabrication.
Feature sizes
are on the order of
tens of micrometers.
This is not transistor fabrication,
but it demonstrates
that the interconnection substrate
for electronic circuits
can be produced
by additive manufacturing.

**Voxel8 Multi-Material Electronics Printing.**
The Voxel8 system,
founded by Jennifer Lewis at Harvard
and commercially launched in 2015,
demonstrated simultaneous printing
of PLA structural material
and conductive silver ink
through dual printheads,
enabling the fabrication
of three-dimensional circuits
with embedded electronic components.
The conductive ink,
using highly conductive silver particles,
is reportedly 5,000 times
more conductive
than standard carbon-based inks
and can reliably interconnect
integrated circuit packages.
At the Consumer Electronics Show,
the company displayed
a quadcopter produced
almost entirely in one piece,
with PLA structure
and conductive circuits
3D printed together,
with motors and batteries
inserted during the print process.

**Printed Transistors and Logic Gates.**
Multiple research groups
have demonstrated
fully printed [thin-film transistors][ref_tft] (TFTs)
using organic semiconductors,
metal oxide semiconductors,
and [carbon nanotube][ref_carbon_nanotube] networks.
Printed complementary logic gates,
including inverters, NAND, and NOR gates,
have been demonstrated
with switching speeds
in the kilohertz range,
roughly six orders of magnitude
slower than conventional CMOS logic
but sufficient for
many control and sensor applications.
In 2024, researchers at MIT
demonstrated semiconductor-free,
monolithically 3D-printed logic gates
using copper-reinforced PLA filament
on standard desktop FDM printers.
These gates survived
over 4,000 switching cycles,
establishing that
functional digital logic
can be fabricated
without any semiconductor material
using consumer-grade equipment.

**Carbon Nanotube Processors.**
In 2019, Hills et al.
at MIT demonstrated RV16X-NANO,
a 16-bit [RISC-V][ref_riscv] microprocessor
built entirely from
complementary [carbon nanotube][ref_carbon_nanotube]
field-effect transistors.
The processor contained
over 14,000 transistors
and successfully executed
the "Hello, World!" program.
Carbon nanotube transistors
can be deposited from solution,
making them compatible
with printing-based fabrication.
This demonstration established
that non-silicon transistor technologies
can implement
complete general-purpose processors.

**PlasticARM: Flexible ARM Processor.**
In 2021, Biesterfeld et al.
published in Nature
a description of PlasticARM,
a 32-bit ARM Cortex-M0 processor
fabricated on a flexible plastic substrate
using [Indium Gallium Zinc Oxide][ref_igzo]
(IGZO) [thin-film transistors][ref_tft].
The processor contained
approximately 18,000 logic gates
and 56,340 transistors,
ran at a clock frequency
on the order of kilohertz,
and was manufactured
using a metal-oxide semiconductor process
with a feature size
of approximately 0.8 micrometers
on a flexible polyimide substrate.
This demonstration
established that
a functional general-purpose processor
can be built
from thin-film transistors
at feature sizes
roughly three orders of magnitude
larger than leading-edge silicon.
The processor is many orders of magnitude
slower than a modern silicon chip,
but it executes
the full ARM Cortex-M0
instruction set correctly.

The same research group,
a collaboration between
PragmatIC Semiconductors
and [imec][ref_imec],
subsequently demonstrated
a flexible [6502][ref_6502] processor
built in a similar technology,
reproducing the classic
8-bit processor
on a flexible substrate
with approximately 16,000
metal-oxide thin-film transistors
on a 24.9 square millimeter die.
The processor ran
real-time complex assembly code
at a maximum clock frequency
of 71.4 kilohertz,
consuming 11.6 milliwatts
at 10 kilohertz
and 134.9 milliwatts
at maximum operating speed.

**Flex-RV: Flexible RISC-V Processor (2024).**
In 2024, researchers published
in Nature
a description of Flex-RV,
a bendable 32-bit [RISC-V][ref_riscv] microprocessor
fabricated on a flexible
[IGZO][ref_igzo] substrate.
The processor contained
12,600 logic gates,
ran at 60 kilohertz,
consumed 6 milliwatts,
and included an integrated
machine learning accelerator.
Flex-RV operated correctly
while bent around a pencil,
demonstrating mechanical robustness
under extreme deformation.
This is the most advanced
flexible processor demonstrated to date,
executing a standard open-source
instruction set
with machine learning capability
on a substrate
that can be manufactured
without conventional silicon processing.

**Sam Zeloof's Garage Semiconductor Fab.**
In 2018, Sam Zeloof,
a high school student
in New Jersey,
fabricated functional
Metal-Oxide-Semiconductor
Field-Effect Transistors (MOSFETs)
in a home laboratory
using equipment
purchased on secondary markets
and fabrication processes
adapted from published literature.
By 2021,
Zeloof had fabricated
a chip containing
approximately 1,200 transistors.
While this is
orders of magnitude
below industrial scale,
the demonstration established
that semiconductor fabrication
at micrometer feature sizes
is achievable
without access to
a commercial fabrication facility.
The equipment cost
was on the order
of thousands of dollars,
not billions.
This existence proof
is directly relevant
to probe self-replication,
because it demonstrates
that the minimum viable
semiconductor fabrication capability
is far simpler
than the leading edge.

**DARPA Electronics Resurgence Initiative.**
The United States
Defense Advanced Research Projects Agency
(DARPA) launched
the [Electronics Resurgence Initiative][ref_eri] (ERI)
to address challenges
in semiconductor technology
beyond Moore's Law scaling.
Several ERI programs
are relevant to printable computing,
including work on
heterogeneous integration,
novel materials,
and unconventional fabrication techniques.

**RISC-V and Open-Source Processor Design.**
The [RISC-V][ref_riscv]
instruction set architecture,
developed at the University of California, Berkeley,
is an open-source processor design
that can be freely implemented
in any fabrication technology.
RISC-V provides
a complete 32-bit
or 64-bit processor specification
with no licensing fees
or intellectual property restrictions.
For probe computing,
the significance of RISC-V
is that the processor design
is fully documented,
freely available,
and can be synthesized
for any target technology,
including printed electronics
or large-feature-size
semiconductor processes.
A probe carrying
a RISC-V processor design
in its manufacturing database
could fabricate processors
at whatever feature size
its fabrication capability supports.

**RepRap and Self-Replicating Machines.**
The [RepRap][ref_reprap] project,
founded by Adrian Bowyer
at the University of Bath in 2005,
is an open-source initiative
to build self-replicating
three-dimensional printers.
A RepRap printer
can fabricate
many of the structural components
needed to build
another RepRap printer.
The project achieved
partial self-replication,
with early estimates
suggesting that a RepRap
could produce
approximately 50 percent
of its own parts by mass.
The remaining parts,
including motors, electronics,
and the heated extruder,
must be sourced externally.
This partial self-replication
mirrors the challenge
facing von Neumann probes.
Borgue and Hein (2021)
estimated that
a near-term self-replicating probe
could replicate
approximately 70 percent of its mass,
with microelectronics
constituting a significant fraction
of the non-replicable remainder.

### State of the Art

**Additive Manufacturing Techniques.**
Multiple additive manufacturing methods
can deposit electronic materials.
[Inkjet printing][ref_inkjet_printing]
deposits droplets
of functional ink
from piezoelectric or thermal printheads,
achieving feature sizes
of 20 to 50 micrometers.
[Aerosol Jet][ref_aerosol_jet] printing
focuses an aerosol stream
to achieve feature sizes
of approximately 10 micrometers.
[Screen printing][ref_screen_printing]
forces ink through a mesh stencil,
achieving feature sizes
of 50 to 100 micrometers.
Extrusion-based printing
deposits material through a nozzle,
achieving feature sizes
of 100 micrometers to millimeters.
Electrohydrodynamic jet printing
can achieve sub-micrometer features
but at very low throughput.
[Gravure printing][ref_gravure_printing]
and [flexography][ref_flexography]
are high-throughput roll-to-roll methods
that can pattern features
down to approximately 20 micrometers.

**Materials.**
The palette of printable electronic materials
has expanded substantially.
Silver nanoparticle [inks][ref_conductive_ink]
provide conductivity
within one to two orders of magnitude
of bulk silver.
[Carbon nanotube][ref_carbon_nanotube] networks
serve as both conductors
and semiconductors.
[Graphene][ref_graphene] inks
provide conductors
with unique electrical properties.
[IGZO][ref_igzo]
and other metal oxide semiconductors
can be deposited from solution
and provide
the best-performing
printed transistors.
Organic semiconductors
including conjugated polymers
and small molecules
offer flexibility
and low-temperature processing.
Printed dielectrics
include polymer insulators
such as poly(methyl methacrylate) (PMMA)
and parylene.

**Performance.**
The best printed transistors
achieve carrier mobilities
of approximately
10 to 50 square centimeters
per volt-second
for metal oxide semiconductors,
and 0.1 to 10 square centimeters
per volt-second
for organic semiconductors.
For comparison,
crystalline silicon transistors
achieve mobilities
of approximately
500 to 1,400 square centimeters
per volt-second.
This mobility gap
translates directly
into lower switching speeds.
The fastest printed logic circuits
operate in the kilohertz
to low megahertz range,
compared to gigahertz frequencies
for conventional silicon CMOS.

**Feature Sizes.**
The feature sizes
achievable by printing techniques
range from approximately
10 micrometers (Aerosol Jet)
to approximately 100 micrometers
(screen printing).
These are roughly
three to five orders of magnitude
larger than
leading-edge semiconductor lithography
at 3 to 5 nanometers.
However, they are comparable to
or smaller than
the feature sizes
of vacuum tube circuits
discussed in the companion article.
The 0.8 micrometer process
used for the PlasticARM processor
is at the boundary
between printed and lithographic techniques,
using photolithographic patterning
on a thin-film substrate.

### Contemporary Applications

**Flexible Electronics.**
The primary commercial application
of printed electronics
is flexible and wearable devices.
Printed sensors,
displays,
and interconnects
on flexible substrates
enable form factors
impossible with rigid silicon.
Applications include
medical patches
that monitor vital signs,
flexible displays,
and smart packaging.

**Radio-Frequency Identification.**
Printed Radio-Frequency Identification (RFID) tags
represent one of the highest-volume
applications of printed electronics.
Simple printed circuits
containing a printed antenna
and a silicon chip
are produced in the billions annually.
Fully printed RFID tags,
eliminating even the silicon chip,
have been demonstrated
in research but have not yet
achieved commercial scale.

**Photovoltaic Cells.**
Printed organic
and [perovskite][ref_perovskite] solar cells
use roll-to-roll printing
to produce photovoltaic modules
at potentially lower cost
than conventional silicon cells.
The efficiency of printed solar cells
has improved substantially,
with perovskite cells
exceeding 25 percent efficiency
in laboratory demonstrations.

**Sensors.**
Printed chemical sensors,
temperature sensors,
strain gauges,
and biosensors
exploit the ability
of printing techniques
to deposit functional materials
in custom patterns
on arbitrary substrates.
These sensors
are already in commercial use
in medical diagnostics,
food safety monitoring,
and industrial process control.

**Space Applications.**
NASA's Marshall Space Flight Center
has investigated
additive manufacturing
of electronic components
for in-space fabrication.
The ability to print
circuit boards and sensors
from raw materials in orbit
would reduce the mass
of components
that must be launched from Earth.
This research
is directly relevant
to probe self-replication,
as it addresses
the same fundamental challenge
of fabricating electronics
from local resources.

### 3D Printable Computing in the Context of Probe Development

The probe computing requirements
described in the neuromorphic section
apply equally
to printable computing architectures.
The evaluation here
focuses on how
3D printable processors
address those requirements.

**Manufacturability.**
The defining advantage
of printable computing
for probe applications
is that the fabrication process
can be replicated
using equipment
that a probe could plausibly build.
A probe needs an inkjet
or aerosol jet printhead,
a supply of functional inks,
and a precision positioning system.
The printhead
is a mechanical device
with resolution requirements
of tens of micrometers.
The inks can potentially
be synthesized
from raw materials
available on rocky bodies.
The positioning system
is a three-axis motion platform
similar to what the probe
already needs
for mechanical fabrication.
Compared to the clean rooms,
photolithographic steppers,
and chemical vapor deposition systems
required for conventional
semiconductor fabrication,
the equipment for printed electronics
is radically simpler.

**Tolerance to Imperfect Fabrication.**
Printed electronics inherently tolerate
wider process variations
than conventional semiconductors.
A printed line
that is 15 micrometers wide
instead of the target 10 micrometers
still conducts electricity.
A printed transistor
with slightly different threshold voltage
than its neighbor
still switches.
This tolerance
is a fundamental property
of the larger feature sizes involved.
Where a single
out-of-spec transistor
on a conventional chip
renders the entire chip inoperable,
printed circuits
degrade gracefully
as process variation increases.

**Raw Material Requirements.**
Printed electronics
require fewer exotic materials
than conventional semiconductors.
The primary conductive material
is silver,
which is relatively common
in asteroid and planetary compositions.
IGZO semiconductor material
requires indium, gallium,
zinc, and oxygen,
all of which
are available
in rocky body compositions.
Organic semiconductors
require carbon-based compounds.
Compared to the ultrapure silicon,
exotic photoresists,
and rare-earth dopants
required for conventional fabrication,
the material requirements
for printed electronics
are substantially more accessible.

**Performance Limitations.**
The primary limitation
of printed computing
is speed.
A printed processor
operating at kilohertz frequencies
is six to nine orders of magnitude
slower than a modern
silicon processor
operating at gigahertz frequencies.
For some probe computing tasks,
this is acceptable.
Manufacturing control loops
operating at kilohertz rates
are adequate for many processes.
Sensor monitoring
does not require
gigahertz sampling rates.
For other tasks,
such as
communication encoding and decoding,
scientific data processing,
and complex planning,
the performance of printed processors
may be insufficient.
A probe might address this limitation
through massive parallelism,
deploying arrays
of thousands of printed processors
to achieve collective throughput
despite individual processor slowness.

**Energy Efficiency.**
Printed transistors
consume more energy per operation
than conventional silicon transistors,
due to their larger size
and lower carrier mobility.
However, the absolute power consumption
of a printed processor
operating at kilohertz frequencies
is modest,
because power scales
with operating frequency.
A kilohertz printed processor
might consume milliwatts of power,
comparable to
a neuromorphic processor
but for fundamentally different reasons.

### Work in Progress and Partial Solutions

**Multi-Material 3D Printing.**
Current research
on multi-material 3D printing
aims to deposit
conductors, semiconductors,
insulators,
and structural materials
in a single integrated build process.
Systems that combine
inkjet printing of electronic materials
with Fused Deposition Modeling (FDM)
of structural polymers
have been demonstrated.

**Roll-to-Roll Manufacturing.**
Roll-to-roll (R2R) printing
applies high-throughput
printing techniques
from the graphic arts industry
to electronic fabrication.
R2R processes
can produce printed circuits
at speeds of
meters per second,
enabling mass production
of printed electronic devices.
For probe applications,
R2R manufacturing
is relevant because
it demonstrates
that printed electronics
can be produced
at scale
using relatively simple
mechanical equipment.

**Printed Memory.**
Printed Resistive Random-Access Memory
(printed [ReRAM][ref_rram])
and printed ferroelectric memory
have been demonstrated
in research laboratories.
These technologies
offer non-volatile storage
fabricated using
the same printing processes
as printed transistors,
enabling integrated
computing and storage
in a single
printed substrate.

**Hybrid Printed and Conventional Systems.**
The most practical near-term approach
combines printed components
with conventional silicon chips.
Printed interconnects,
sensors,
and passive components
surround a conventional
silicon processor
that provides
the computational performance.
For probe applications,
this hybrid approach
suggests that a probe
might carry a supply
of pre-fabricated silicon chips
for critical computing tasks
while printing
all other electronic components
from local materials.
The Borgue and Hein (2021)
probe design
follows this logic,
carrying microelectronics
as non-replicable payload.

### Hypothetical and Extrapolated Approaches

**Printed Neuromorphic Processors.**
The intersection
of neuromorphic computing
and printed electronics
offers a particularly promising
pathway for probe computing.
A neuromorphic processor
tolerates component variability,
and printed fabrication
inherently produces
variable components.
A printed memristor crossbar array,
fabricated from
metal oxide materials
using inkjet or aerosol jet printing,
could implement
a neural network
capable of learning
to compensate
for its own
fabrication imperfections.
This approach combines
the fault tolerance
of neuromorphic architectures
with the manufacturing simplicity
of printed electronics.

**Bootstrapping Fabrication Capability.**
A probe might begin
with printed electronics
at large feature sizes
and gradually bootstrap
to finer fabrication.
The initial printed processors,
operating at kilohertz speeds,
could control
the fabrication equipment
needed to produce
somewhat more precise
electronic components.
Those improved components
could then control
even more precise fabrication,
in an iterative refinement process.
This bootstrapping approach
mirrors the historical development
of semiconductor technology,
where each generation of chips
was used to design
and fabricate
the next generation.

**Cellular Automata Processors.**
A probe might implement
computation through
arrays of identical
printed cells,
each containing
a simple logic element
and connections to neighbors.
[Cellular automata][ref_cellular_automata]
can implement
universal computation,
and their regular structure
is well suited
to manufacturing processes
that deposit
identical elements
in a grid pattern.
Von Neumann himself
formulated his theory
of self-replicating machines
in the cellular automata framework.
A printed cellular automaton processor
would be slow
but could be
arbitrarily scalable,
adding capacity
simply by printing
more cells.

**In-Situ Resource Utilization for Inks.**
A probe that can
mine and refine materials
from asteroids
or planetary surfaces
could potentially
synthesize conductive inks
from local silver,
semiconductor inks
from local metal oxides,
and dielectric materials
from local minerals.
The chemistry
of nanoparticle ink synthesis
is well understood,
though adapting it
to extraterrestrial feedstocks
would require
substantial engineering development.
If a probe could close
the materials loop
for electronic ink production,
it would achieve
full closure
for the fabrication
of printed electronic circuits.

## Information Storage and Memory

A von Neumann probe
must store and preserve
two categories of information
over extremely long mission durations.
Operational data
includes navigation databases,
sensor readings,
and communication logs.
Replication knowledge
includes the engineering blueprints,
manufacturing procedures,
and material specifications
needed to build
a complete copy of the probe.
The companion article
on [pre-transistor computing][related_post_steampunk]
surveyed five pre-semiconductor
storage technologies.
This section examines
storage technologies
compatible with neuromorphic
and printable computing architectures.

### Neuromorphic Memory

In a neuromorphic system,
information is stored
in synaptic weights
distributed across
the neural network.
This is the biological model.
A human brain stores
learned knowledge
in the strengths
of approximately $10^{14}$ synapses.
A neuromorphic processor
stores its learned behavior
in the weights
of its artificial synapses.

The challenge is persistence.
In a digital neuromorphic chip
like TrueNorth or Loihi,
synaptic weights
are stored in SRAM or DRAM,
which requires continuous power
to maintain state.
A power interruption
erases all learned information.
Memristive synapses
solve this problem.
A [memristor][ref_memristor]
retains its resistance state
indefinitely without power,
providing non-volatile
synaptic storage.
A neuromorphic processor
built from memristive crossbar arrays
stores its weights
in the physical resistance
of its junctions,
combining computation and memory
in a single device.

Additional non-volatile memory technologies
compatible with neuromorphic architectures
include Magnetoresistive RAM (MRAM),
where Samsung has demonstrated
MRAM-based in-memory computing
with a "resistance sum" architecture,
Ferroelectric RAM (FeRAM)
investigated for multilevel
analog storage,
and Phase Change Memory (PCM)
exploiting phase change materials
for analog resistance states.

For replication knowledge,
a neuromorphic system
cannot store blueprints
as neural network weights.
Engineering drawings
and manufacturing procedures
require precise digital representation.
A neuromorphic probe
would need
a separate storage system
for this data,
potentially using
one of the technologies
discussed in the companion article,
such as magnetic tape,
punched metal tape,
or 5D optical storage in quartz glass.

### Printed Memory

Printed [ReRAM][ref_rram]
stores information
as resistance states
in a printed metal-oxide layer
sandwiched between
printed electrodes.
The resistance state
is non-volatile,
persisting indefinitely
without power.
Printed ReRAM cells
have been demonstrated
with feature sizes
of tens of micrometers,
compatible with
printed transistor technology.
A fully printed computing system
could integrate
printed processors
and printed ReRAM
on the same substrate.

Printed ferroelectric memory
uses a ferroelectric polymer
whose polarization state
can be switched
by an applied electric field.
The polarization persists
without power,
providing non-volatile storage.
Printed ferroelectric devices
have been demonstrated
using poly(vinylidene fluoride) (PVDF)
and its copolymers.

For long-term storage
of replication knowledge,
printed electronics
could potentially encode information
in physically durable formats.
A printed circuit
that encodes data
as the presence or absence
of conductive traces
in a regular grid
implements a form
of read-only memory (ROM)
that is as durable
as the substrate material.
If printed on ceramic
or metal substrates,
such a ROM
could survive
for centuries or millennia.

### Redundancy and Error Correction

Both neuromorphic
and printed memory systems
require error management strategies
for long-duration missions.

Neural networks
provide natural error correction
through distributed representation.
A memory stored
as a pattern of weights
across thousands of synapses
is robust
against the loss
of individual synapses.
The network can
retrieve approximately correct memories
even after
significant degradation.
This is analogous
to the content-addressable memory
of biological neural systems.

Printed memory systems
can use standard
error-correcting codes,
as described
in the companion article
on [error correction][related_post_error_correction].
The larger feature sizes
of printed memory
reduce susceptibility
to single-event upsets,
because a larger cell
requires more deposited energy
to change its state.
However, the lower integration density
means that
the total storage capacity
is reduced,
making redundancy
more costly in physical volume.

A tiered storage strategy,
matching technology to data criticality,
is appropriate
for both neuromorphic
and printable systems.
Critical replication knowledge
should be stored
in the most durable available format,
replicated across
multiple independent storage devices,
and periodically verified
against checksums.
Operational data
can use less durable
but higher-capacity storage.
Learned neural network weights
can be regenerated
through retraining
if corrupted,
provided the training data
or training environment
can be reconstructed.

### Storage Longevity

The longevity
of stored information
depends on
the physical medium
and the storage environment.
In the interstellar environment,
cosmic ray bombardment
gradually corrupts
all electronic storage.
The companion article
on [error correction][related_post_error_correction]
quantified this threat.

For neuromorphic systems,
periodic refreshing of weights
through continued learning
can compensate
for gradual degradation.
A neuromorphic probe
that continuously processes
sensor data
and adjusts its weights
accordingly
maintains its knowledge
through ongoing use,
analogous to a biological brain
that maintains memories
through recall and reconsolidation.

For printed storage,
the physical durability
of the substrate
and the deposited materials
determines longevity.
Ceramic substrates
with metallic conductors
can survive
for millennia
in benign environments.
In radiation-rich environments,
metal oxide ReRAM cells
are relatively radiation-tolerant
because the resistance state
is determined by
the physical structure
of a conductive filament,
not by trapped charge.

## Comparison and Architectural Implications

Neuromorphic and printable computing
address the semiconductor closure gap
from different directions,
and their strengths
are largely complementary.

### Manufacturability

Neuromorphic architectures
currently require
conventional semiconductor fabrication,
but their tolerance
for component variability
means they could function
at much larger feature sizes
than conventional digital logic.
Printed computing
can be manufactured
using additive processes
that a probe could plausibly replicate,
but current printed processors
are limited
to very low operating frequencies.
The combination
of a neuromorphic architecture
implemented in printed electronics
offers the best of both approaches.

### Tolerance to Imperfect Fabrication

Neuromorphic systems
are inherently tolerant
of component variability
because neural networks
learn to compute
despite device mismatch.
Printed systems
inherently produce
variable components
due to the stochastic nature
of printing processes.
These properties are synergistic.
A neuromorphic processor
built from printed components
would use its learning capability
to compensate
for the imprecision
of its own fabrication.

### Power Efficiency

Neuromorphic processors
achieve power efficiency
through event-driven computation
and co-located
memory and processing.
Printed processors
achieve low absolute power
through low operating frequency.
A printed neuromorphic processor
would combine both advantages,
consuming power
only when neurons fire
and operating at
the modest frequencies
achievable with printed transistors.

### Scalability

Neuromorphic architectures
scale naturally
through the addition
of more neurons and synapses.
Printed fabrication scales
through the printing
of larger substrates
or more layers.
A probe could increase
its computing capacity
simply by printing
more neuromorphic circuits,
a manufacturing operation
well within the capability
of a system
that can already
fabricate printed electronics.

### Integration with Other Subsystems

The companion article
on [pre-transistor computing][related_post_steampunk]
proposed a three-tier architecture
of mechanical control,
analog computation,
and minimal digital processing.
Neuromorphic and printable computing
fit naturally
into this framework.

Mechanical control systems
handle low-level actuation.
Analog circuits
handle continuous feedback control
and signal conditioning.
A printed neuromorphic processor
handles pattern recognition,
anomaly detection,
adaptive navigation,
and system health monitoring.
A minimal digital core,
potentially fabricated
from printed transistors
or carried as
non-replicable payload,
handles communications encoding,
precise arithmetic,
and error correction.

This four-tier architecture,
mechanical, analog,
neuromorphic,
and minimal digital,
distributes computation
across technologies
of decreasing manufacturing difficulty.
The mechanical layer
requires basic metalworking.
The analog layer
requires vacuum tubes
or printed passive components.
The neuromorphic layer
requires printed transistors
or memristors
at micrometer feature sizes.
The digital layer,
if present,
requires the most precise fabrication
but handles
the smallest share
of the computing workload.

### Suitability for Distributed Probe Networks

Both neuromorphic
and printable computing
are well suited
to distributed probe networks.
Individual probes
in a swarm
need only local intelligence.
A printed neuromorphic processor
providing kilohertz-speed
pattern recognition
and adaptive behavior
is sufficient
for a probe
that coordinates
with thousands of siblings
through simple communication protocols.
The collective intelligence
of the swarm
emerges from
the interactions
of many simple agents,
not from the computational power
of any individual probe.

## Conclusion

Neuromorphic and 3D printable computing
represent two paths
toward reducing
the semiconductor closure gap
for self-replicating spacecraft.
Neither technology
provides a complete solution
in its current form.
Neuromorphic processors today
still require
conventional semiconductor fabrication.
Printed processors today
operate at speeds
that limit their applicability
to certain computing tasks.
But the trajectory
of both technologies
points toward
a convergence
that could enable
functional probe computing.

Neuromorphic computing
contributes fault tolerance,
energy efficiency,
adaptive learning,
and graceful degradation
under component failure.
These properties are essential
for any computing system
that must operate
for centuries
without hardware replacement.
The key insight
is that neural networks
compute correctly
despite imprecise components,
a property
that no conventional
digital architecture shares.

Printable computing contributes
manufacturing simplicity,
tolerance to imperfect fabrication,
accessible raw materials,
and a fabrication process
that an autonomous system
could plausibly replicate.
The key insight
is that additive manufacturing
of electronic circuits
eliminates the need
for the photolithographic infrastructure
that makes conventional
semiconductor fabrication
impossible for autonomous probes.

The most promising approach
combines both technologies.
A printed neuromorphic processor,
fabricated through
additive deposition
of metal oxide
or organic materials
on a robust substrate,
would use the inherent
fault tolerance
of neural computation
to compensate
for the inherent imprecision
of printed fabrication.
Such a processor
would be slow
by modern standards
and large by modern standards,
but it could be built
by a probe
from materials available
on any rocky body.

Integrated into
the four-tier architecture
of mechanical control,
analog computation,
neuromorphic processing,
and minimal digital arithmetic,
this approach distributes
the semiconductor closure gap
across technologies
of decreasing manufacturing difficulty.
The result is a computing architecture
where the most demanding fabrication
handles the smallest share
of the computing workload,
and the least demanding fabrication
handles the largest share.

The companion articles
in this series
have progressively narrowed
the semiconductor closure gap
from a system-wide impossibility
to a constraint
on a single subsystem
performing a limited set of tasks.
Pre-transistor computing
demonstrated that
mechanical and analog systems
can handle
the majority of
probe computing workloads.
Neuromorphic and printable computing
demonstrate that
even the remaining digital tasks
may be addressable
through technologies
with radically simpler
manufacturing requirements.
The closure gap has not been eliminated,
but it has been reduced
to a scale
where engineering solutions
are plausible.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-03-10 09:47:00 +0000

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

## Future Reading

- [Analog VLSI and Neural Systems (Addison-Wesley), Mead, 1989][future_mead_1989]
- [Computing with Memristive Devices (Synthesis Lectures on Emerging Engineering Technologies), James, 2021][future_james_2021]
- [Nature Neuromorphic Hardware and Computing Collection, 2024][future_nature_neuro_2024]
- [Neuromorphic Photonics (CRC Press), Prucnal and Shastri, 2017][future_prucnal_2017]
- [Organic Electronics: Materials, Processing, Devices and Applications (CRC Press), So, 2010][future_so_2010]
- [Printed Electronics: Materials, Technologies, and Applications (Wiley), Cui, 2016][future_cui_2016]

## References

### Reference

- [3D Printing, Wikipedia][ref_additive_manufacturing]
- [Aerosol Jet Printing, Wikipedia][ref_aerosol_jet]
- [BrainChip, Wikipedia][ref_brainchip]
- [BrainScaleS, Wikipedia][ref_brainscales]
- [Caenorhabditis Elegans, Wikipedia][ref_c_elegans]
- [Carbon Nanotube, Wikipedia][ref_carbon_nanotube]
- [Carver Mead, Wikipedia][ref_carver_mead]
- [Cellular Automaton, Wikipedia][ref_cellular_automata]
- [Conductive Ink, Wikipedia][ref_conductive_ink]
- [Electronics Resurgence Initiative, Wikipedia][ref_eri]
- [Flexography, Wikipedia][ref_flexography]
- [Graphene, Wikipedia][ref_graphene]
- [Gravure Printing, Wikipedia][ref_gravure_printing]
- [Hebbian Theory, Wikipedia][ref_hebbian]
- [Hodgkin-Huxley Model, Wikipedia][ref_hodgkin_huxley]
- [IGZO, Wikipedia][ref_igzo]
- [imec, Wikipedia][ref_imec]
- [Inkjet Printing, Wikipedia][ref_inkjet_printing]
- [Loihi, Wikipedia][ref_loihi]
- [McCulloch-Pitts Neuron, Wikipedia][ref_mcculloch_pitts]
- [Memristor, Wikipedia][ref_memristor]
- [MOS Technology 6502, Wikipedia][ref_6502]
- [Neuromorphic Engineering, Wikipedia][ref_neuromorphic]
- [Organic Field-Effect Transistor, Wikipedia][ref_ofet]
- [Organic Semiconductor, Wikipedia][ref_organic_semiconductor]
- [Perceptron, Wikipedia][ref_perceptron]
- [Perovskite Solar Cell, Wikipedia][ref_perovskite]
- [Printed Circuit Board, Wikipedia][ref_pcb]
- [Printed Electronics, Wikipedia][ref_printed_electronics]
- [RepRap Project, Wikipedia][ref_reprap]
- [Resistive Random-Access Memory, Wikipedia][ref_rram]
- [RISC-V, Wikipedia][ref_riscv]
- [Screen Printing, Wikipedia][ref_screen_printing]
- [Spike-Timing-Dependent Plasticity, Wikipedia][ref_stdp]
- [Spiking Neural Network, Wikipedia][ref_snn]
- [SpiNNaker, Wikipedia][ref_spinnaker]
- [Thick-Film Technology, Wikipedia][ref_thick_film]
- [Thin-Film Transistor, Wikipedia][ref_tft]
- [TrueNorth, Wikipedia][ref_truenorth]

### Related Posts

- [Roadmap to a Competitive Type III Civilization][related_post_roadmap]
- [Steampunk and Analog Electronics for Von Neumann Probe Control][related_post_steampunk]
- [The Error Correction Recursion Problem][related_post_error_correction]
- [Von Neumann Probes][related_post_von_neumann_probes]

### Research

- [3D-Printed Contextual Computer (Advanced Intelligent Systems), Shirmohammadli et al., 2023][research_shirmohammadli]
- [A Bendable Non-Silicon RISC-V Microprocessor (Nature), Myny et al., 2024][research_myny]
- [A Million Spiking-Neuron Integrated Circuit with a Scalable Communication Network and Interface (Science), Merolla et al., 2014][research_merolla]
- [A Modern Microprocessor Built from Complementary Carbon Nanotube Transistors (Nature), Hills et al., 2019][research_hills]
- [A Natively Flexible 32-bit Arm Microprocessor (Nature), Biesterfeld et al., 2021][research_biesterfeld]
- [A Self-Reproducing Interstellar Probe (Journal of the British Interplanetary Society), Freitas, 1980][research_freitas_1980]
- [A Survey Examining Neuromorphic Architecture in Space and Challenges from Radiation (arXiv), Naoukin et al., 2023][research_naoukin]
- [Additive Manufacturing of Neuromorphic Systems (Advanced Materials), Yan et al., 2025][research_yan]
- [Advancing Neuromorphic Computing With Loihi: A Survey of Results and Outlook (Proceedings of the IEEE), Davies et al., 2021][research_davies_2021]
- [Affordable, Rapid Bootstrapping of the Space Industry and Solar System Civilization (Journal of Aerospace Engineering), Metzger et al., 2013][research_metzger]
- [Loihi: A Neuromorphic Manycore Processor with On-Chip Learning (IEEE Micro), Davies et al., 2018][research_davies_2018]
- [Near-Term Self-Replicating Probes: A Concept Design (Acta Astronautica), Borgue and Hein, 2021][research_borgue]
- [Neuromorphic Electronic Systems (Proceedings of the IEEE), Mead, 1990][research_mead_1990]
- [Opportunities for Neuromorphic Computing Algorithms and Applications (Nature Computational Science), Schuman et al., 2022][research_schuman]
- [Surrogate Gradient Learning in Spiking Neural Networks (IEEE Signal Processing Magazine), Neftci, Mostafa, and Zenke, 2019][research_neftci]
- [The Missing Memristor Found (Nature), Strukov et al., 2008][research_strukov]
- [The SpiNNaker Project (Proceedings of the IEEE), Furber et al., 2014][research_furber]
- [Towards Artificial General Intelligence with Hybrid Tianjic Chip Architecture (Nature), Pei et al., 2019][research_pei]

[future_cui_2016]: https://www.wiley.com/en-us/Printed+Electronics%3A+Materials%2C+Technologies+and+Applications-p-9781118920923
[future_james_2021]: https://link.springer.com/book/10.1007/978-3-031-79777-0
[future_mead_1989]: https://en.wikipedia.org/wiki/Analog_VLSI_and_Neural_Systems
[future_nature_neuro_2024]: https://www.nature.com/collections/jaidjgeceb
[future_prucnal_2017]: https://www.cambridge.org/core/books/neuromorphic-photonics/3A5A0EA7A5A99A1CDA03B57B2E22B908
[future_so_2010]: https://www.routledge.com/Organic-Electronics-Materials-Processing-Devices-and-Applications/So/p/book/9780367383596
[ref_6502]: https://en.wikipedia.org/wiki/MOS_Technology_6502
[ref_additive_manufacturing]: https://en.wikipedia.org/wiki/3D_printing
[ref_aerosol_jet]: https://en.wikipedia.org/wiki/Aerosol_jet_printing
[ref_brainchip]: https://en.wikipedia.org/wiki/BrainChip
[ref_brainscales]: https://en.wikipedia.org/wiki/BrainScaleS
[ref_c_elegans]: https://en.wikipedia.org/wiki/Caenorhabditis_elegans
[ref_carbon_nanotube]: https://en.wikipedia.org/wiki/Carbon_nanotube
[ref_carver_mead]: https://en.wikipedia.org/wiki/Carver_Mead
[ref_cellular_automata]: https://en.wikipedia.org/wiki/Cellular_automaton
[ref_conductive_ink]: https://en.wikipedia.org/wiki/Conductive_ink
[ref_eri]: https://en.wikipedia.org/wiki/Electronics_Resurgence_Initiative
[ref_flexography]: https://en.wikipedia.org/wiki/Flexography
[ref_graphene]: https://en.wikipedia.org/wiki/Graphene
[ref_gravure_printing]: https://en.wikipedia.org/wiki/Gravure_printing
[ref_hebbian]: https://en.wikipedia.org/wiki/Hebbian_theory
[ref_hodgkin_huxley]: https://en.wikipedia.org/wiki/Hodgkin%E2%80%93Huxley_model
[ref_igzo]: https://en.wikipedia.org/wiki/Indium_gallium_zinc_oxide
[ref_imec]: https://en.wikipedia.org/wiki/Imec
[ref_inkjet_printing]: https://en.wikipedia.org/wiki/Inkjet_printing
[ref_loihi]: https://en.wikipedia.org/wiki/Loihi_(chip)
[ref_mcculloch_pitts]: https://en.wikipedia.org/wiki/Artificial_neuron
[ref_memristor]: https://en.wikipedia.org/wiki/Memristor
[ref_neuromorphic]: https://en.wikipedia.org/wiki/Neuromorphic_engineering
[ref_ofet]: https://en.wikipedia.org/wiki/Organic_field-effect_transistor
[ref_organic_semiconductor]: https://en.wikipedia.org/wiki/Organic_semiconductor
[ref_pcb]: https://en.wikipedia.org/wiki/Printed_circuit_board
[ref_perceptron]: https://en.wikipedia.org/wiki/Perceptron
[ref_perovskite]: https://en.wikipedia.org/wiki/Perovskite_solar_cell
[ref_printed_electronics]: https://en.wikipedia.org/wiki/Printed_electronics
[ref_reprap]: https://en.wikipedia.org/wiki/RepRap_project
[ref_riscv]: https://en.wikipedia.org/wiki/RISC-V
[ref_rram]: https://en.wikipedia.org/wiki/Resistive_random-access_memory
[ref_screen_printing]: https://en.wikipedia.org/wiki/Screen_printing

[ref_snn]: https://en.wikipedia.org/wiki/Spiking_neural_network
[ref_spinnaker]: https://en.wikipedia.org/wiki/SpiNNaker
[ref_stdp]: https://en.wikipedia.org/wiki/Spike-timing-dependent_plasticity
[ref_tft]: https://en.wikipedia.org/wiki/Thin-film_transistor

[ref_thick_film]: https://en.wikipedia.org/wiki/Thick-film_technology
[ref_truenorth]: https://en.wikipedia.org/wiki/TrueNorth
[related_post_error_correction]: {% post_url 2026-03-06-error_correction_recursion_problem %}
[related_post_roadmap]: {% post_url 2026-03-03-roadmap_to_competitive_type_iii_civilization %}
[related_post_steampunk]: {% post_url 2026-03-08-steampunk_and_analog_electronics_for_von_neumann_probe_control %}
[related_post_von_neumann_probes]: {% post_url 2026-03-05-von_neumann_probes %}

[research_biesterfeld]: https://doi.org/10.1038/s41586-021-03625-w
[research_borgue]: https://doi.org/10.1016/j.actaastro.2021.03.004
[research_davies_2018]: https://doi.org/10.1109/MM.2018.112130359
[research_davies_2021]: https://doi.org/10.1109/JPROC.2021.3067593
[research_freitas_1980]: https://www.rfreitas.com/Astro/ReproJBISJuly1980.htm
[research_furber]: https://doi.org/10.1109/JPROC.2014.2304638
[research_hills]: https://doi.org/10.1038/s41586-019-1493-8
[research_mead_1990]: https://doi.org/10.1109/5.58356
[research_merolla]: https://doi.org/10.1126/science.1254642
[research_metzger]: https://doi.org/10.1061/(ASCE)AS.1943-5525.0000236
[research_myny]: https://doi.org/10.1038/s41586-024-07976-y
[research_naoukin]: https://arxiv.org/abs/2311.15006
[research_neftci]: https://doi.org/10.1109/MSP.2019.2931595
[research_pei]: https://doi.org/10.1038/s41586-019-1424-8
[research_schuman]: https://doi.org/10.1038/s43588-021-00184-y
[research_shirmohammadli]: https://doi.org/10.1002/aisy.202300015
[research_strukov]: https://doi.org/10.1038/nature06932
[research_yan]: https://doi.org/10.1002/adma.202504807
