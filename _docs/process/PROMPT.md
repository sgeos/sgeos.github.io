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

Please revise A104 on the external LLM feedback at the end of prompt.

Thoroughly research the topic and pull in references.
There is no length limit, no reference limit,
and the reference list may be more valuable than the article itself.

### Freeform Commentary

Please include A104 freeform commentary in your reverse prompt.

## Context

Drafting time!

## Constraints

(none)

## Success Criteria

- A104 revised.
- A104 dates updated.
- A104 related article links correct.
- A104 NOT published.
- A104 release announcement NOT generated from template and reported in reverse prompt.
- A104 freeform commentary in reverse prompt.

## Notes

(none)

---

## A104 External LLM Revision Feedback

These recommendations aim to strengthen the argument, improve structural clarity, and more clearly articulate the article’s central design thesis:

**mechanical control → analog computation → minimal digital core**

They also suggest expanding discussion of **information storage** and introducing the concept of **radically devolved analog probes for extremely long-duration intergalactic missions**.

---

### Clarify and Elevate the Core Architectural Thesis

The article currently implies an architectural hierarchy but does not fully foreground it as the central design principle. The piece would benefit from explicitly presenting the following idea early in the introduction:

> A practical probe architecture distributes computation across three technological layers:
> **mechanical control → analog computation → minimal digital core.**

Suggested improvements:

- Introduce this architecture explicitly in the **introduction**.
- Present it as the article’s **sub-thesis** supporting the broader semiconductor-closure argument.
- Provide a short preview diagram or bullet list explaining the roles of each layer:
  - **Mechanical control:** robust low-level actuation and sensing.
  - **Analog computation:** continuous signal processing and feedback control.
  - **Minimal digital core:** planning, encoding, communication, and limited symbolic reasoning.

Reinforce this hierarchy again in the **comparison to requirements** section and in the **conclusion**.

---

### Strengthen the Framing of the Semiconductor Closure Problem

The article successfully reframes the problem from “replicating modern computers” to “replicating sufficient computation,” but this could be made more explicit.

Recommended additions:

- Briefly restate the closure problem in one concise sentence early in the article.
- Clarify that the objective is **functional closure**, not **technological parity**.
- Emphasize that distributing computation across different technologies reduces the burden on semiconductor manufacturing.

This framing helps readers understand why steampunk and analog approaches are relevant.

---

### Expand the Role of Mechanical Control Systems

Mechanical control appears throughout the article but could be more clearly characterized as the **foundation of probe autonomy**.

Suggested additions:

- Mention specific examples of mechanical or quasi-mechanical control systems:
  - governors
  - cams and cam-timed machines
  - differential gear mechanisms
  - hydraulic and pneumatic logic
- Emphasize that these systems:
  - require minimal precision manufacturing
  - tolerate radiation well
  - can be repaired or reproduced using relatively primitive industrial processes.

A short paragraph explaining why **mechanical systems are attractive for long-term autonomous operation** would strengthen the argument.

---

### Expand Discussion of Analog Computation

The analog section is strong but could emphasize its role as the **computational middle layer**.

Suggested additions:

- Clarify that analog electronics are particularly effective for:
  - control loops
  - signal filtering
  - navigation calculations
  - optimization problems.
- Note that analog computers historically solved differential equations directly.
- Mention historical examples such as:
  - differential analyzers
  - fire control computers
  - early aerospace guidance systems.

This reinforces the plausibility of analog systems performing substantial computational work.

---

### Clarify the Role of the Minimal Digital Core

The article should explicitly state **which tasks genuinely require digital computation**.

Suggested additions:

- Identify functions best handled digitally:
  - mission planning
  - symbolic reasoning
  - communications encoding
  - compression
  - error detection and correction
- Emphasize that the digital subsystem can be **very small** relative to modern computers.

You may wish to describe the digital core as:

> a supervisory computer responsible for symbolic tasks and high-level decision making.

This framing makes the hybrid architecture clearer.

---

### Introduce the Concept of Radically Devolved Analog Probes

The article would benefit from including a speculative but plausible concept:

**radically devolved probes designed for extremely long missions.**

Add a section discussing probes intended for **intergalactic exploration** where travel times may reach **millions of years**.

Key ideas to include:

- Digital electronics may degrade over extremely long timescales.
- Analog or mechanical systems may be more stable over geological timescales.
- A probe designed for such missions might rely almost entirely on:
  - mechanical systems
  - analog electronics
  - very limited or no digital logic.

These probes could perform:

- slow navigation
- environmental sensing
- extremely simple replication strategies.

Such probes might sacrifice computational sophistication for **maximum longevity and robustness**.

---

### Expand the Discussion of Information Storage

Information storage is essential for probe replication and should be discussed explicitly.

Suggested additions include describing how a probe stores:

- engineering blueprints
- manufacturing procedures
- star maps
- navigation tables
- communication protocols.

Possible storage technologies worth mentioning:

- magnetic storage (tapes or drums)
- optical storage
- mechanically encoded storage (punched tape or plates)
- phase-change materials
- crystalline or chemical data storage.

Also note that the probe must store two categories of information:

1. **Operational data**
   Navigation tables, calibration constants, and mission parameters.

2. **Replication knowledge**
   Detailed instructions for building new probes and industrial infrastructure.

A short subsection explaining the **longevity and redundancy requirements of probe memory** would strengthen the engineering realism.

---

### Discuss Data Redundancy and Error Management

Because probes operate for long periods without human supervision, the article should briefly address data reliability.

Suggested improvements:

- Mention redundancy strategies such as:
  - replicated storage
  - error-correcting codes
  - periodic data verification.
- Explain that the digital subsystem may periodically check stored data and repair corrupted copies.

This ties nicely into the article’s broader themes of **robust autonomous systems**.

---

### Strengthen the Hybrid Systems Section

The hybrid systems discussion is already strong but could emphasize how common such architectures are in modern engineering.

Suggested revision:

- Add a brief statement noting that most real systems combine:
  - mechanical components
  - analog electronics
  - digital control.

This helps readers understand that the probe architecture proposed in the article is not exotic but rather an extension of common engineering practice.

---

### Add a Short Discussion of Manufacturing Implications

The article could briefly connect the proposed architecture to **manufacturing feasibility**.

Suggested points:

- Mechanical systems require relatively simple machining.
- Analog electronics can be built with relatively large-feature components.
- Only a small portion of the probe requires advanced semiconductor fabrication.

This reinforces the argument that the architecture reduces the closure gap.

---

### Improve the Conclusion by Restating the Architecture

The conclusion should explicitly restate the core hierarchy:

**mechanical control → analog computation → minimal digital core**

Suggested structure for the closing paragraph:

1. Restate the semiconductor closure challenge.
2. Summarize the three-layer architecture.
3. Emphasize that the probe only needs **sufficient computation**, not modern computing technology.
4. Note that extremely long missions may rely on even simpler analog or mechanical systems.

This will tie the entire article together.

---

### Minor Structural Improvements

Additional small improvements that may enhance clarity:

- Add a short transitional paragraph between the steampunk and analog sections.
- Ensure each major section clearly references the probe application.
- Reduce repetition in the state-of-the-art discussions where possible.

---

### Summary of Key Revisions

The most important recommended revisions are:

- Explicitly present **mechanical control → analog computation → minimal digital core** as the article’s architectural sub-thesis.
- Expand the discussion of **information storage and data longevity**.
- Introduce the concept of **radically devolved analog probes for intergalactic missions lasting millions of years**.
- Clarify the roles of mechanical, analog, and digital subsystems.
- Strengthen the discussion of hybrid architectures and manufacturing implications.

Together, these revisions will sharpen the article’s central argument and deepen its treatment of autonomous probe design.
