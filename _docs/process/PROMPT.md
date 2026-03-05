# Prompt Staging Area

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is a staging area for complex human-to-AI instructions. The human pilot drafts and refines prompts here before execution.

---

# Current Prompt

## Comments

Read, but unverified:

- Android Development on FreeBSD
- Android Unit Testing
- Authenticating a Phoenix JSON API with Guardian and Ueberauth
- Claude Code on FreeBSD
- Claude Code on OpenBSD
- Claude Code Over SSH
- Getting Started with Solana Using Rust and Pinocchio
- Solana sBPF Assembly Example

Working through prerelease articles is capacity gated.
There is presently no speculative ETA.

## Objectives

Please revise A102 according to the following feedback.

Thoroughly research the topic and pull in references.
There is no length limit, no reference limit,
and the reference list may be more valuable than the article itself.

### Clarify the Analytical Structure in the Introduction

The introduction blends historical background, technical feasibility, and strategic implications. While this works narratively, it risks giving the impression that the historical material is presented selectively to support the strategic framework.

Consider adding a short transition paragraph early in the article that explicitly separates three questions:

- whether self-replicating machines are theoretically possible,
- whether they are technologically achievable, and
- what their strategic implications would be if deployed.

A sentence such as the following can clarify the structure:

> The analysis in this article distinguishes between three separate questions: whether self-replicating machines are theoretically possible, whether they are technologically achievable with foreseeable technology, and what strategic implications follow if such systems are eventually deployed.

This separation improves analytical clarity and reduces perceived bias.

### Frame Historical Estimates as Model Outputs

Some historical estimates (for example, galaxy colonization timelines) are presented as specific numerical values. These figures depend heavily on assumptions about probe velocity, replication time, and mission architecture.

To avoid unnecessary debate over precise numbers, present these estimates explicitly as outputs of particular models rather than as definitive values.

For example, instead of presenting a specific colonization time as a fixed prediction, describe it as a model-dependent estimate that varies with probe speed and replication assumptions.

### Avoid Overstating Theoretical Claims About Complexity Thresholds

The discussion of von Neumann’s theoretical work suggests that he established a minimum complexity threshold for self-replication. In practice, his work demonstrated logical sufficiency rather than a precise minimum.

A safer phrasing would emphasize that self-replication requires a system capable of both constructing components and copying the instructions describing those components.

For example:

> Von Neumann demonstrated that a self-replicating machine must include both a universal constructor capable of building components and a mechanism for copying the description that specifies the machine itself.

This preserves the conceptual point without implying a proven minimum complexity.

### Strengthen Quantitative Anchors in the Propulsion Discussion

The propulsion discussion would benefit from one explicit order-of-magnitude calculation for the kinetic energy required to accelerate an interstellar probe.

Providing a simple energy estimate (for example, using \(E = \frac{1}{2}mv^2\)) helps ground the discussion and allows comparison to familiar energy scales such as global electricity production or nuclear weapon yields.

Including a brief calculation or reference value reinforces the engineering realism of the analysis.

### Temper Claims of Academic Consensus

The article currently suggests that there is a growing academic consensus that self-replicating probes are primarily an engineering problem. While the literature is expanding, the field remains relatively niche.

Consider replacing strong consensus language with phrasing such as:

> These publications represent a growing body of academic work treating self-replicating probes as a serious engineering problem rather than purely speculative fiction.

This change improves credibility while preserving the point.

### Explicitly Interpret the Colonization Wave Equation

The equation describing colonization wave velocity is technically correct but would benefit from a short interpretation explaining its significance.

A single explanatory sentence can clarify the strategic implication:

> When replication time becomes comparable to transit time, the expansion wave slows dramatically, making reductions in replication time as important as increases in propulsion speed.

This helps readers understand why the equation matters.

### Clarify the Role of Micro-Probe Concepts

The discussion of micro-probe concepts should clarify whether such probes are intended primarily for exploration or for self-replication.

A brief note explaining that extremely small probes may struggle to carry the industrial capacity required for replication will connect this discussion more directly to the closure problem introduced later.

### Expand the Closure Problem With Additional Examples

The closure problem is correctly identified as the central engineering challenge. The discussion could be strengthened by mentioning additional practical bottlenecks, such as:

- ultra-pure material production,
- semiconductor dopants,
- precision optics fabrication.

These additions reinforce the realism of the engineering constraints.

### Refine the Description of Autonomous Industrial Competence

The statement that no existing autonomous system can perform more than two or three steps in the industrial chain may be interpreted as overstated.

A more precise claim would emphasize that no system currently performs the entire chain from raw geological input to finished manufactured components without sustained human supervision.

This preserves the argument while avoiding easy counterexamples.

### Clarify the Power Generation Landscape

The power generation section correctly emphasizes nuclear power for deep-space industrial activity. It may be helpful to briefly acknowledge other conceptual approaches such as fusion reactors or beamed power.

Even a single sentence noting these alternatives helps demonstrate awareness of the broader design space.

### Introduce Quantitative Context for Radiation Exposure

The radiation hardening discussion would benefit from one quantitative reference point, such as typical total ionizing dose limits for spacecraft electronics.

Providing even a rough numerical range reinforces the technical grounding of the section.

### Refine Statements About Solar Power Beyond Jupiter

The statement that solar power is effectively unavailable beyond Jupiter is somewhat stronger than necessary. Solar power becomes increasingly inefficient with distance but remains technically possible.

A more precise formulation would emphasize mass inefficiency rather than absolute infeasibility.

### Clarify the Definition of a Prototype Self-Replicating System

The prototype definition should explicitly reference replication from extraterrestrial raw materials rather than general autonomous operation.

A clearer definition might be:

> a system capable of producing a functionally equivalent copy of itself from raw extraterrestrial materials with minimal imported components.

This ties the definition directly to the closure discussion.

### Identify the Dominant Sources of Timeline Uncertainty

The timeline section would benefit from explicitly identifying the largest uncertainties in the forecast.

In particular, semiconductor fabrication closure and precision optics production represent the most complex industrial processes currently required for full autonomy.

A short paragraph identifying these uncertainties will strengthen the credibility of the range estimate.

### Add a Summary of Primary Engineering Bottlenecks

Before the timeline section, consider adding a short summary list of the primary engineering bottlenecks identified in the analysis.

For example:

- semiconductor manufacturing closure  
- precision optics fabrication  
- autonomous mining and materials processing  
- long-duration nuclear power systems  
- interstellar deceleration technologies  

This summary helps readers synthesize the technical discussion before moving into the development timeline.

### Slightly Moderate the Closing Biological Analogy

The closing statement comparing von Neumann probes to biological self-replication is rhetorically effective but can be framed more neutrally.

A possible revision:

> Biology demonstrates that self-replication at planetary scale is physically achievable, though implementing similar capabilities in engineered systems presents very different challenges.

This preserves the analogy while maintaining a technical tone.

### Freeform Commentary

Please include A102 freeform commentary in your reverse prompt.

## Context

Drafting time!

## Constraints

(none)

## Success Criteria

- A102 revised according to comments.
- A102 dates updated.
- A102 related article links correct.
- A102 published.
- A102 release announcement generated from template and reported in reverse prompt.
- A102 freeform commentary in reverse prompt.

## Notes

(none)
