---
layout: post
mathjax: false
comments: true
title:  "Keleusma as a Substrate for a Real-Time Hypermedia Desktop"
date:   2026-05-24 09:00:00 +0000
categories: operating-systems keleusma philosophy
series: hypermedia_desktop
series_title: Hypermedia Desktop
series_index: 3
---
<!-- A115 -->
<script>console.log("A115");</script>

[A113][related_post_btron_hypermedia]
laid out the design space
for a real-time hypermedia desktop
in the BTRON lineage.
The article surveyed the BTRON proposition,
the asymmetric history
of the real-time operating systems
that descended from the TRON Project
and the hypermedia desktops
that did not,
and proposed a ten-layer architectural sketch
for a 2026 successor.
The sketch was deliberately substrate-agnostic.
It named seL4, Genode,
Automerge, Yjs, Loro,
the InterPlanetary File System,
Iroh,
the WebAssembly Component Model,
Skia, Cairo Graphics,
HarfBuzz, FreeType,
Servo, the Chromium Embedded Framework,
WebKit,
ProseMirror, TipTap, Lexical, CodeMirror,
the JetBrains Meta Programming System,
and the Model Context Protocol,
without proposing a single language
in which these components compose.

This article asks the obvious next question.
[Keleusma][ref_keleusma_crates] is a small,
verifier-strict, total functional
stream processor
that compiles to bytecode
and runs on a stack-based virtual machine
in `no_std` plus `alloc` environments.
The language has been the subject
of several articles in this blog,
namely
[Getting Started with Keleusma 0.1.1][related_post_keleusma_0_1_1],
[A Verifiable Control Kernel in Keleusma
for a Truthful-Machine Architecture][related_post_keleusma_verifiable_kernel],
[Getting Started with Keleusma 0.2.0][related_post_keleusma_0_2_0],
and
[Information-Flow Control, A Deep Dive with Keleusma][related_post_keleusma_ifc].
Several of the properties that A113 identified
as load-bearing for a real-time hypermedia desktop,
notably verifier-checkable worst-case execution time,
verifier-checkable worst-case memory usage,
language-level information-flow control,
hot code swap under cryptographic signature,
and a total functional discipline
that proves termination
of every accepted module,
are properties Keleusma already provides
at version 0.2.0.

The question is whether the alignment is real.
If Keleusma supplies the load-bearing properties,
how much of the ten-layer sketch
does it cover,
where does it fall short,
and what would the V0.5 and later roadmap
need to add
for the language to credibly underpin
a vertical hypermedia operating system
on the BTRON axis.

This article is the analytical answer.
It takes A113's structural commitments
and ten-layer sketch
as the rubric,
maps Keleusma V0.2.0
and the public V0.5+ roadmap
onto each item,
and reports the verdict
with illustrative code samples
for the load-bearing claims.
The specific vertical
in which a Keleusma-based hypermedia system
would be deployed first,
namely the choice
between aerospace cockpit, medical imaging,
intelligence analyst workstation,
or regulatory submission console,
is the subject of a separate follow-up article.
This article stays general.

## What Keleusma Provides at Version 0.2.0

The published artefacts
that describe the language
are
[the project README on GitHub][ref_keleusma_repo],
[the published crates.io page][ref_keleusma_crates],
[the docs.rs API documentation][ref_keleusma_docs],
and the architectural documents
under `docs/architecture/`
in the project repository.
For the purposes
of the BTRON suitability question,
the load-bearing capabilities
are these.

**Five static guarantees.**
Every Keleusma program that compiles
carries proofs
of totality, productivity,
bounded step, bounded memory,
and safe swapping.
The guarantees are checked
at module load
by the verifier
before any code runs.
A program whose bound
cannot be proved
is rejected with a diagnostic
naming the construct
that defeats the analysis.

**Three function categories.**
The `fn` category
is atomic total.
A `fn` runs straight through
and must terminate.
The `yield` category
is non-atomic total.
A `yield` may pause
and resume,
and it must eventually finish.
The `loop` category
is productive divergent.
A `loop` never finishes
and must hand a value
to its host
on every cycle.
The three-category split
is the language-level
discipline that maps onto
A113's discussion
of handlers
in a hypermedia desktop.

**Worst-case execution time
and worst-case memory usage
analysis.**
Every accepted module
carries a worst-case execution time bound,
reported in pipelined cycles,
and a worst-case memory usage bound,
reported in bytes.
The bounds are computed
by the verifier
from the bytecode
and a cost model.
The cost model
is calibrated per platform
by a multiplicative factor
that converts pipelined cycles
to wall-clock time.
A host applies the factor
to bound the actual execution time
on its specific hardware.

**Information-flow control at the type level.**
A type may carry
a user-defined label set.
The notation `T@L` denotes
the type `T`
carrying the label `L`.
The notation `T@{L1, L2}` denotes
multiple labels.
The two relabel operators are
`classify expr@Label`,
which adds a label,
and `declassify expr@Label`,
which removes a label.
Labels propagate
through every value
that derives from a labelled one,
through arithmetic, comparison,
and branching alike.
The flow rule
at every position
is that the source label set
must be a subset
of the target label set,
otherwise the verifier rejects.

**Hot code swap.**
A module may be replaced
at a defined RESET boundary
while its persistent data segment
survives the swap.
The interface fingerprint
of the new module
is checked against the old
to ensure that public surface
remains compatible.

**Ed25519 module signing.**
With the `signatures` feature,
the compiler can sign
a compiled module's bytes
with an Ed25519 key.
The runtime
refuses to load
a module
whose signature
does not verify
against a host-registered public key.
The mechanism is documented in
[the project README][ref_keleusma_repo]
and is detailed
in the prior articles
on the language.

**Hindley-Milner type inference
with generics and traits.**
The language admits
parametric polymorphism,
trait-based ad hoc polymorphism,
and compile-time monomorphization.
Generic functions, structs, and enums
are instantiated
at every concrete use,
and the verifier checks
each instantiation
against its bounds.

**Target descriptor
for cross-architecture portability.**
A program declares
its target word width,
address width,
and float width.
A program compiled
against one target
may be re-targeted
to another
by recompilation
with no source change
when the program's value range
fits the target's range.

These capabilities
make Keleusma
a verifier-bounded, no_std,
language-level secure substrate
for a class of work
that current alternatives
do not address
under one umbrella.

A first illustrative example
shows a typed structural part
that a hypermedia handler
would process.

```keleusma
struct Citation {
    source_id: Word,
    target_id: Word,
    page:      Word,
}

fn new_citation(source: Word, target: Word, page: Word) -> Citation {
    Citation {
        source_id: source,
        target_id: target,
        page:      page,
    }
}

fn main() -> Word {
    let c = new_citation(7, 42, 3);
    c.target_id
}
```

The program declares
a typed `Citation` part
with three fields,
constructs one,
and returns one of its fields.
The verifier accepts the program
because the struct admits
straight-line construction
and field access
under bounded resource use.
This is the minimum
typed-part shape
that a hypermedia link store
would require.

```sh
$ keleusma run 01_typed_part.kel
42
```

A second example
illustrates the cooperative
handler shape.

```keleusma
loop main(input: Word) -> Word {
    let doubled = input + input;
    let next = yield doubled;
    next
}
```

The program is a `loop main`
that doubles its input
and yields the result
to the host,
then resumes with the host's reply.
The verifier accepts the program
and reports its worst-case
yield-to-yield execution time
and its worst-case memory usage.
The driving host
is responsible for
resuming the loop.
The language enforces
that the loop is productive,
meaning that it yields at least one value
between any two yields.

```sh
$ keleusma compile 02_handler_loop.kel -o /tmp/02.bin
wrote /tmp/02.bin (228 bytes)
```

The compile invocation
verifies the bound
without running the program.
For a `loop` program
the running mode
is host-driven,
and the command-line tool's `run`
applies only to `fn` programs
that produce a single result.
For a real deployment,
the embedding host
calls the language's
`Vm::resume`
between yields.

## The Six Structural Commitments of the Hypermedia Object Model

[A113][related_post_btron_hypermedia]
listed six commitments
that define the hypermedia object model
as distinct from
the file-and-application model.
Each commitment maps
onto Keleusma
with a specific verdict.

**The document is a tree of typed parts.**
A typed part in Keleusma
is a struct.
A document containing
typed parts of multiple types
is a hierarchical composition
of these structs,
expressed through
the generic and trait machinery.
The `Citation` example above
is a typed part.
A larger document
would compose
many such typed parts
through enum variants
and through generic containers.
The verdict is strong fit.

**Parts are addressable.**
The R5.2 interface fingerprint
described in
[the language design document][ref_keleusma_repo]
gives each module
a stable identity
derived from its public surface.
At the module level
this provides addressability.
Part-level addressability
within a document
is not yet specified
in V0.2.0.
A successor design
would extend
the R5.2 mechanism
to track
not only the public surface
of a module
but also the public identities
of individual parts within it.
The verdict is partial fit
with a clear design path.

**Links are first-class objects.**
V0.2.0 does not provide
a link primitive.
The typed-link concept
that BTRON required,
namely a record
of a source, a target,
a type, a direction,
and metadata,
would be a Keleusma module
that declares its own struct
for links
and maintains them
in a `data` block.
The link primitive
does not contradict
any of Keleusma's principles
and is designable.
The verdict is mismatch in V0.2.0
with a clear design path.

**Applications register as handlers
for part types.**
The trait machinery
provides the registration mechanism.
A handler module
implements a trait
parameterised over a typed part
and is selected
by the calling code's type.
For a hypermedia desktop
that admits handlers
from many vendors,
the trait is the contract
and module signing
provides the trust mechanism.
The verdict is strong fit.

**Composition is uniform and recursive.**
Trait-based composition
in Keleusma
is uniform across struct types,
generic types,
and the three function categories.
A handler that composes
sub-handlers
does so
through ordinary trait method calls.
The verifier
admits the composition
under the bounded-resource rules.
The verdict is strong fit.

**Provenance is intrinsic.**
The information-flow labels
described above
provide provenance
at the type level.
The Ed25519 signing
provides provenance
at the module level.
The interface fingerprint
provides version identity.
Together these three mechanisms
cover the provenance commitment
more completely
than the conventional stack
provides
through its mix of
git history,
manual audit trails,
and post-hoc cryptographic attestation.
The verdict is strong fit.

The six-commitment scorecard
is four strong fits,
one partial fit,
and one mismatch.
The mismatch
is the link primitive,
which is a clean engineering addition
rather than a structural obstacle.

| Commitment | Verdict | Keleusma mechanism |
|---|---|---|
| The document is a tree of typed parts | Strong fit | Structs, enums, and generics |
| Parts are addressable | Partial fit | R5.2 interface fingerprint at module level; part-level addressability needs design |
| Links are first-class objects | Mismatch | No link primitive in V0.2.0; designable as a Keleusma module |
| Applications register as handlers for part types | Strong fit | Trait machinery plus module signing for trust |
| Composition is uniform and recursive | Strong fit | Trait-based composition across struct, generic, and function categories |
| Provenance is intrinsic | Strong fit | Information-flow labels at the type level, Ed25519 signing at the module level, and interface fingerprint at the version level |

## The Five Engineering Commitments for Real-Time Hypermedia

A113 listed five further commitments
that distinguish a real-time hypermedia desktop
from a general-purpose desktop.
These are the performance and latency
engineering disciplines
required to compose typed parts
on a deadline-sensitive surface.

**Bounded handler execution time.**
The worst-case execution time analysis
in Keleusma
provides exactly this property
at the handler boundary.
Every accepted `loop main`
carries a yield-to-yield bound.
The verdict is strong fit.

**Deadline propagation
across handler boundaries.**
A handler that calls
into a sub-handler
inherits the sub-handler's
worst-case execution time
into its own bound.
The verifier
performs the propagation
at compile time.
The design extends naturally
to deadline-aware scheduling
in which the kernel assigns
a deadline to each yield slice
and the handlers respect it.
The verdict is partial fit
with strong design alignment.

**Preallocated resources
for safety-critical surfaces.**
The `const data` block
declares fixed compile-time resources
that the worst-case memory usage analysis
includes in the master arena bound.
The example below
shows a fixed registry
that maps part types to handler identifiers.

```keleusma
const data registry {
    prose:   Word = 1,
    figure:  Word = 2,
    table:   Word = 3,
    formula: Word = 4,
}

fn handler_for(part_type: Word) -> Word {
    if part_type == registry.prose {
        10
    } else {
        if part_type == registry.figure {
            20
        } else {
            if part_type == registry.table {
                30
            } else {
                40
            }
        }
    }
}

fn main() -> Word {
    handler_for(registry.figure)
}
```

The verifier checks
that the data block
fits within the declared arena
and that the dispatch function
runs in bounded time.

```sh
$ keleusma run 05_preallocated.kel
20
```

The verdict is strong fit.

**Spatial and temporal isolation
of misbehaving parts.**
Three properties combine
to provide isolation.
First, total functional discipline
prevents a handler
from entering
a non-terminating computation
that would starve other handlers.
Second, per-task arena
bounds the memory
a handler can consume.
Third, information-flow labels
prevent a handler
from contaminating
trusted state
with untrusted values.
The IFC sanitiser pattern
illustrates the third property.

```keleusma
fn render_action(input: Word@Untrusted) -> Word {
    let action = if input == 1 {
        100
    } else {
        if input == 2 {
            200
        } else {
            0
        }
    };
    declassify action@Untrusted
}

fn main() -> Word {
    let untrusted_payload = classify 2@Untrusted;
    render_action(untrusted_payload)
}
```

The input arrives
carrying the `Untrusted` label.
The handler matches it
against discrete values
and produces a labelled action.
The single `declassify` operator
removes the `Untrusted` label
at the reviewable audit point.
The verifier accepts
because the declassify
is the explicit
chokepoint
through which untrusted information
is released to trusted use.

```sh
$ keleusma run 03_ifc_sanitiser.kel
200
```

The same handler
without the declassify
is rejected at compile time,
because the labelled action
would flow
through the return position
without an audit point.

```keleusma
fn render_action_unsafe(input: Word@Untrusted) -> Word {
    if input == 1 {
        100
    } else {
        if input == 2 {
            200
        } else {
            0
        }
    }
}

fn main() -> Word {
    let untrusted_payload = classify 2@Untrusted;
    render_action_unsafe(untrusted_payload)
}
```

```sh
$ keleusma run 04_ifc_reject.kel
error: compile: 7:56: type error: function `render_action_unsafe` returns Word but body produces Word@Untrusted
```

The rejection is the safety property.
A program the verifier accepts
is one in which every untrusted value
that flows to a trusted boundary
passes through
an explicit `declassify` operator.
The discipline composes
across handlers
and across modules.
The verdict is strong fit.

**Admission control
at the surface boundary.**
Per-task worst-case execution time
admission is the verifier's job.
A module whose bound exceeds
the deployment's budget
is rejected before it is loaded.
The mechanism extends
to surface-level admission,
in which a real-time surface
declares its frame deadline
and rejects the embedding
of any handler
whose bound would prevent
the surface from meeting
its overall deadline.
The verdict is strong fit.

The five-commitment scorecard
is four strong fits
and one partial fit.
This is the strongest area
of alignment
between Keleusma
and the A113 thesis.
The performance and latency
engineering section
of A113 reads almost
as a specification
for what Keleusma already provides.

| Commitment | Verdict | Keleusma mechanism |
|---|---|---|
| Bounded handler execution time | Strong fit | Worst-case execution time analysis at the verifier |
| Deadline propagation across handler boundaries | Partial fit | Worst-case execution time propagates through the call graph; deadline-aware scheduling is a natural extension |
| Preallocated resources for safety-critical surfaces | Strong fit | `const data` blocks plus worst-case memory usage verification |
| Spatial and temporal isolation of misbehaving parts | Strong fit | Total functional discipline plus per-task arena plus information-flow labels |
| Admission control at the surface boundary | Strong fit | Per-task worst-case execution time admission rejects modules whose bound exceeds the budget |

## Mapping the Ten-Layer Architectural Sketch

A113 named ten layers
in a concrete architectural sketch
for a 2026 hypermedia operating system.
Each layer named candidate components
drawn from
the contemporary open-source ecosystem.
Keleusma maps onto these layers
with mixed verdicts.

**Layer 1, the verified microkernel.**
A113 named [seL4][ref_sel4]
and the [Genode Operating System Framework][ref_genode]
as candidates for the trusted base.
Keleusma is not a microkernel.
The published in-repository
cooperative microkernel
under `examples/rtos/`
is a Rust kernel core
of approximately three hundred fifty lines
plus a platform trait
that abstracts hardware.
The kernel core is not formally verified
but the per-task Keleusma scripts
running on top of it
carry verified worst-case execution time
and memory bounds.
A future composition
of seL4 user-space
with a Keleusma user layer
would give both verified trusted base
and verified user code,
at the cost
of integration engineering
that is not yet done.
The verdict is partial fit.

**Layer 2, the component runtime.**
A113 named
[Cap'n Proto][ref_capn_proto]
and the
[WebAssembly Component Model][ref_wasm_component_model]
as candidates
for capability-typed
cross-component communication.
Keleusma's three function categories,
total functional discipline,
and information-flow labels
provide a comparable but distinct substrate.
Each Keleusma module
is a typed component
with declared inputs, outputs,
worst-case execution time,
worst-case memory usage,
and information-flow labels.
Modules can be hot-swapped
at RESET boundaries
under Ed25519 signature verification.
The approach is closer to
[JX, the Java-based operating system][ref_jx]
that A113 discussed,
than to the WebAssembly Component Model.
JX argued that language-level type safety
substitutes for hardware-level isolation.
Keleusma extends JX's premise
with worst-case execution time
and worst-case memory usage verification,
which JX did not provide.
For a hypermedia operating system,
the part-and-handler model
maps onto Keleusma modules naturally.
The verdict is strong fit.

**Layer 3, content-addressed storage.**
A113 named
[the InterPlanetary File System][ref_ipfs],
[Iroh][ref_iroh],
and
[Hypercore Protocol][ref_hypercore]
as candidates.
Keleusma does not provide
content-addressed storage.
A successor design
would wrap one of these projects
through a Keleusma native
that exposes
content-addressed storage operations
to Keleusma modules.
The operations themselves
would not enjoy Keleusma's verification.
The verdict is mismatch
with a clear integration path.

**Layer 4, conflict-free replicated data type substrate.**
A113 named
[Automerge][ref_automerge],
[Yjs][ref_yjs],
and
[Loro][ref_loro].
Keleusma does not provide
a conflict-free replicated data type library.
The Keleusma total functional discipline
is in tension
with conflict-free replicated data type semantics,
which require non-trivial
concurrent state convergence.
A pure-Keleusma implementation
is conceivable
but would require careful design
to maintain
worst-case execution time bounds
in the merge operation.
The simpler path
is to treat the conflict-free replicated data type
as a host-provided native
and let the host take responsibility
for convergence.
The verdict is mismatch
with a similar integration path.

**Layer 5, the link store and part registry.**
A113 noted
that this layer
is the novel platform engineering.
No existing open-source project
implements it
as a standard service.
Keleusma's typed-part discipline
at the module level
provides a foundation,
but a link store
as a system service
must be designed from scratch.
The link store
would be a Keleusma module
above the filesystem layer
that exposes
typed link primitives
to handlers.
The IFC label flow
covers the trust model.
The hot-swap interface fingerprint
covers schema migration
across module revisions.
The verdict is partial fit
with substantial novel design work.

**Layer 6, the rendering substrate.**
A113 named
[Skia][ref_skia],
[Cairo Graphics][ref_cairo_graphics],
[HarfBuzz][ref_harfbuzz],
[FreeType][ref_freetype],
[Servo][ref_servo],
the [Chromium Embedded Framework][ref_cef],
and [WebKit][ref_webkit].
None of these projects
has a Keleusma binding.
Skia and Cairo are written in C and C++,
HarfBuzz and FreeType are written in C,
Servo is written in Rust,
and the Chromium Embedded Framework and WebKit
are written in C and C++.
A Keleusma-based rendering surface
for a constrained operator-facing display
can be built
above the framebuffer trait
shape proposed in
the internal RTOS API research,
namely a low-level pixel-access trait
and a higher-level primitive-drawing trait.
For a desktop
with arbitrary user content,
full text shaping
for complex scripts,
and arbitrary embedded media,
Keleusma's current scope
is too narrow
without large native bindings.
The verdict is mismatch
beyond the simple framebuffer level.

**Layer 7, the editor frameworks.**
A113 named
[ProseMirror][ref_prosemirror],
[TipTap][ref_tiptap],
[Lexical][ref_lexical],
[CodeMirror][ref_codemirror],
and the
[JetBrains Meta Programming System][ref_mps].
All five exist
in JavaScript or Java ecosystems.
None has a Keleusma analogue.
A hypermedia operating system
on Keleusma
would require either embedding
a browser engine,
which contradicts
the language's no-embedded-Linux scope,
or building Keleusma-native editor frameworks
from scratch.
The verdict is mismatch.

**Layer 8, the file-world bridge.**
For hosted builds,
the Keleusma standard library
provides
operating system interface natives
that admit a Posix-style file backend.
A bridge to legacy file formats
would be a Keleusma module
above this trait.
Capability-based access control
via [Capsicum][ref_capsicum]
on FreeBSD-derived hosts
is consistent with Keleusma's discipline
but not yet integrated.
Round-trip preservation
of legacy formats
such as Microsoft Office,
PDF, and the major media formats
remains
the harder half of this problem,
as A113 noted.
Format parsers
would be host libraries
called through natives.
The parsing itself
would not enjoy Keleusma's
worst-case execution time guarantees
because the input format complexity
exceeds what a verifier-bounded parser
can handle.
The verdict is partial fit.

**Layer 9, the agent and provenance interface.**
This is the layer
where Keleusma's distinctive properties
most clearly outperform
the conventional alternatives.
Keleusma's information-flow labels
and total functional discipline
are exactly the properties
a [Model Context Protocol][ref_mcp] server
should expose
to language model clients.
A Keleusma module
that exposes its parts
through the Model Context Protocol
with declared
worst-case execution time,
worst-case memory usage,
and information-flow labels
gives a large language model
a typed, bounded,
audit-trail-friendly surface
to work against.
This is stronger than
what conventional
operating systems provide
through their Model Context Protocol implementations.
[Content Credentials][ref_content_credentials]
manifests on derived media
require cryptographic operations.
Ed25519 signing
is already present in Keleusma.
The
[Coalition for Content Provenance and Authenticity][ref_c2pa]
payload schema
would be a Keleusma module.
[PROV-AGENT][research_prov_agent]
provenance entries
would be typed parts
in the link store.
The verdict is partial fit
with strong long-term potential.

**Layer 10, the user-facing shell.**
For a constrained operator interface,
a shell is implementable
as a Keleusma module
above the rendering layer.
For a general-purpose desktop
in the consumer sense,
the design is undone
and the conventional shell ecosystem
is far more mature.
The verdict is partial fit
for the constrained case
and mismatch
for the general-purpose case.

The ten-layer scorecard
is two strong fits,
five partial fits,
and three mismatches.
The mismatches
concentrate in the layers
that depend on
the contemporary
graphics, editor, and content-store
ecosystems.
The strong fits
concentrate in the layers
that depend on
language-level verification
and typed composition.

| Layer | A113 candidates | Verdict |
|---|---|---|
| 1. Verified microkernel | [seL4][ref_sel4], [Genode][ref_genode] | Partial fit |
| 2. Component runtime | [Cap'n Proto][ref_capn_proto], [WebAssembly Component Model][ref_wasm_component_model] | Strong fit |
| 3. Content-addressed storage | [InterPlanetary File System][ref_ipfs], [Iroh][ref_iroh], [Hypercore Protocol][ref_hypercore] | Mismatch |
| 4. Conflict-free replicated data type substrate | [Automerge][ref_automerge], [Yjs][ref_yjs], [Loro][ref_loro] | Mismatch |
| 5. Link store and part registry | Novel | Partial fit |
| 6. Rendering substrate | [Skia][ref_skia], [Cairo Graphics][ref_cairo_graphics], [HarfBuzz][ref_harfbuzz], [FreeType][ref_freetype], [Servo][ref_servo], [Chromium Embedded Framework][ref_cef], [WebKit][ref_webkit] | Mismatch beyond a simple framebuffer |
| 7. Editor frameworks | [ProseMirror][ref_prosemirror], [TipTap][ref_tiptap], [Lexical][ref_lexical], [CodeMirror][ref_codemirror], [JetBrains MPS][ref_mps] | Mismatch |
| 8. File-world bridge | [Capsicum][ref_capsicum] plus format parsers | Partial fit |
| 9. Agent and provenance interface | [Model Context Protocol][ref_mcp], [Content Credentials][ref_content_credentials], [PROV-AGENT][research_prov_agent] | Partial fit with strong long-term potential |
| 10. User-facing shell | — | Partial fit for constrained surfaces, mismatch for the general-purpose case |

## What Keleusma Uniquely Provides

Three properties
that the conventional A113 stack
does not provide
emerge from this mapping.

**Verified totality.**
The conventional stack
runs unverified
C, C++, and JavaScript
through Skia, ProseMirror,
and the other named libraries.
Keleusma's total functional discipline
gives provable termination,
which is stronger than
what any of the named alternatives provide.
The discipline composes
with the type system
and with the information-flow labels
to give static guarantees
that no equivalent
in the conventional stack
matches.

**Verified worst-case execution time
and worst-case memory usage.**
Real-time on the conventional stack
relies on
[the PREEMPT_RT Linux patch][ref_preempt_rt],
careful avoidance
of dynamic allocation,
and empirical profiling.
Keleusma's verifier
provides static bounds
that hold
across all input distributions.
A module that the verifier accepts
will not exceed
its declared bound
on any input,
which is stronger
than any empirical guarantee.

**Information-flow control at the language level.**
The conventional stack
relies on
[the same-origin policy][ref_same_origin_policy]
in browsers,
on capability frameworks like
[Capsicum][ref_capsicum]
at the operating system layer,
and on
[seccomp filters][ref_seccomp]
for process confinement.
Keleusma's information-flow labels
operate
at the type level,
catching violations
at compile time
rather than at runtime.
The discipline
also catches implicit flows
through control structures,
which runtime taint tracking
typically misses.
[A111][related_post_keleusma_ifc]
treats this property
in depth.

These three properties
are the reason
to consider Keleusma
as the substrate
for a vertical hypermedia operating system.
A real-time, IFC-enforced,
verifier-bounded substrate
under a hypermedia user interface
does not exist
in any other configuration
in the open-source ecosystem.

## What Keleusma Does Not Provide

Three properties
that the conventional stack offers
and Keleusma does not.

**Mature ecosystem.**
Skia, HarfBuzz, FreeType,
ProseMirror, Automerge,
the InterPlanetary File System,
and the rest of the components
A113 named
are production-grade
and widely deployed
across consumer software
and the open-source web stack.
Keleusma is a research-grade language
at version 0.2.0
with a small user base.
The ecosystem gap
will not close
on a one-to-two-year timeline.

**General-purpose breadth.**
The conventional stack
admits arbitrary user code
in arbitrary languages.
Keleusma's total functional discipline
excludes
the general-recursive computation
that some applications require.
A program that needs
arbitrary recursion,
unbounded memory allocation,
or non-terminating background computation
must run outside Keleusma's verifier.
The host can host such programs
in Rust or another language
and expose them
to Keleusma through natives,
but they will not enjoy
Keleusma's guarantees.

**Authoring tooling.**
Editors, debuggers, profilers,
package managers,
and continuous integration
for the conventional stack
exist in mature form.
Keleusma's tooling
is research-grade.
A vertical product
on Keleusma
must accept
that some authoring conveniences
will arrive later
than they would
on the conventional stack.

These three properties
are the reason
not to pursue Keleusma
for general-purpose desktop scenarios.
A consumer operating system
on Keleusma
would fail
for the same reasons
all prior such attempts failed,
as A113 documented in detail.

## The Asymmetry and Its Implication

The Keleusma scorecard
is strong where
A113's vertical-first entry strategy
needs it most
and weak where
A113 said
the general-purpose-platform strategy
fails anyway.
The asymmetry is favourable.
A Keleusma-based hypermedia system
would be a credible technical choice
for the regulated industries
A113 identified
as the realistic market.
The same Keleusma-based hypermedia system
would be a poor choice
for the consumer desktop market
that A113 said
no plausible entrant should attempt.

This article does not commit
to a specific vertical.
The vertical-specific treatment
is the subject
of a separate follow-up article.
What this article commits to
is that the language-level fit
between Keleusma
and the BTRON hypermedia thesis
is real and not coincidental.
The properties A113 named
as load-bearing
for a real-time hypermedia desktop
are properties Keleusma already provides
at the language level,
with the engineering work
concentrated
in the integration layers
above the language.

## The Roadmap Path

Keleusma's published roadmap
runs through several major versions
beyond the released V0.2.0.

**V0.3.0 self-hosted compiler.**
The V0.3.0 release
ports the compiler
from Rust to Keleusma.
This reduces the trusted compiler base
to the bootstrapping interpreter
plus the self-hosted compiler itself,
which is verifier-bounded.
For a hypermedia system,
a smaller trusted base
makes the certification argument
shorter.

**V0.4.0 native code generation.**
The V0.4.0 release
adds an
[LLVM][ref_llvm]-based
native code backend
alongside the bytecode virtual machine.
The native backend
emits standard machine code
for the major architectures.
For a hypermedia system,
native code closes
the performance gap
between Keleusma
and the conventional stack
on render hot paths.

**V0.5.0 Keleusma-host-host.**
The V0.5.0 release
moves the host shell
into Keleusma itself.
Sub-coroutines admit
explicit handle storage
and explicit resume,
release, and completion operators.
For a hypermedia system,
sub-coroutines
match the handler model directly.
A document handler
spawns sub-coroutines
for each typed part it displays
and resumes them
as the user interacts.
The kernel sees
only the outermost handler.
The sub-coroutines compose
under the same verification rules.

**V0.5.x interval-graph
mutual exclusion refinement.**
The V0.5.x point releases
add interval-graph analysis
for mutexes
that hold across statically-sequential phases.
For a hypermedia system,
this reduces
the master memory usage sum
on tight memory budgets.

The V0.3.0 through V0.5.x sequence
covers the language-level work.
The hypermedia-specific work,
namely the link store,
the agent-and-provenance interface,
the content-addressed storage wrapper,
and the file-world bridge,
sits above the language
and is independent
of the language's own roadmap.

Estimated effort
beyond the V0.5+ landing
for a credible vertical prototype
is in the eighteen to thirty-six month range
for a single-engineer team
on a single hardware target.
The estimate is consistent
with the multi-decadal horizon
that A113 identified
as the realistic commitment
for any successor
to the BTRON project.

## What Would Need to Be Built

Beyond the existing Keleusma capabilities
and the V0.5+ roadmap,
five layers of additional engineering
would produce a credible
vertical hypermedia operating system
on Keleusma.

The first layer is
the link store and part registry.
Novel design work.
Would extend the filesystem trait
discussed in A113's coexistence section
with link-graph primitives
and persistent
typed part identities.

The second layer is
content-addressed storage
as a Keleusma module.
Wrapping
the InterPlanetary File System
or [Iroh][ref_iroh]
or a similar Rust library
through Keleusma natives.
The wrapping is straightforward
but the content-addressing layer
would not enjoy
Keleusma's verification properties.

The third layer is
the widget layer above the framebuffer trait.
Selection of a widget toolkit
such as
[LVGL][ref_lvgl]
via foreign-function-interface,
[Slint][ref_slint]
which is Rust-native,
or a Keleusma-native
simple toolkit.
The choice is per-deployment.

The fourth layer is
the file-world bridge.
Format parsers
for the legacy formats
the deployment cares about,
integrated through natives.
This is per-format work
that grows
with the number of legacy formats supported.

The fifth layer is
the agent and provenance interface.
A Model Context Protocol server
exposing the link store
and the part registry
to language model clients
under Keleusma's verification properties.
This is the most novel
but also the smallest layer
and the one where
Keleusma's distinctive properties
most clearly outperform
the conventional alternatives.

The first three layers
are tractable
single-engineer multi-quarter projects.
The fourth is open-ended.
The fifth is small and high-leverage.

## Risks and Open Questions

The assessment has several known weaknesses
that any program manager
considering Keleusma
for a vertical hypermedia system
should weigh.

**No prototype yet.**
The mapping above
is design analysis.
A prototype
that exercises
the link store concept
against a real workload
would surface design problems
that the analysis cannot anticipate.

**Cooperative scheduling
under heavy handler composition.**
Keleusma is cooperative-only.
A document with many handlers
may experience starvation
if one handler
does not yield promptly.
The worst-case execution time admission
addresses this
for known modules.
For ad hoc handler combinations
the analysis is less clear.

**Self-hosted compiler timing.**
Several of the proposed extensions
assume the V0.3.0 self-hosted compiler
and the V0.5.0 Keleusma-host-host.
These have not landed.
A vertical product
depending on them
is a multi-year commitment.

**Ecosystem critical mass.**
A platform's value
depends on
the population of handlers.
Keleusma's user base is small.
Bootstrapping a handler ecosystem
is a chicken-and-egg problem
that A113 identified
as a major risk
for any hypermedia platform.

**Certification posture.**
For the aerospace and medical use cases
A113 named,
the chosen substrate
must be certifiable
under
[DO-178C][ref_do_178c],
[ISO 26262][ref_iso_26262],
[IEC 62304][ref_iec_62304],
or equivalent.
Keleusma's verification properties
argue in favour.
The actual certification path
is not yet exercised
and the timeline is unknown.

## Out of Scope

This article restricts itself
to the language-level
suitability question.
Three substantive topics
are deliberately deferred
to follow-up articles.

The first deferred topic
is the specific vertical
in which a Keleusma-based hypermedia system
should be deployed first.
The choice between
aerospace cockpit,
medical imaging console,
intelligence analyst workstation,
or regulatory submission console
depends on a market analysis
that this article
does not undertake.
The vertical
will be the subject
of a separate post.

The second deferred topic
is the detailed link store design.
The article notes
that the link store
is novel platform engineering.
The schema,
the query language,
the persistence model,
and the migration semantics
under hot swap
all require design work
beyond what this article presents.
A future post
will treat this layer
in detail.

The third deferred topic
is the certification path.
A path to certification
under
[DO-178C][ref_do_178c]
or comparable standards
requires
specific verification artefacts
and an interaction with
a certification authority
that this article cannot anticipate.
The path
will be the subject
of a separate post
once a candidate vertical
is chosen.

## Conclusion

[A113][related_post_btron_hypermedia]
showed that
a real-time hypermedia desktop
in the BTRON lineage
remains a defensible technical direction
for a small set
of high-value vertical markets.
This article shows that
[Keleusma][ref_keleusma_crates],
at version 0.2.0
and along its public roadmap
to V0.5 and beyond,
is a credible language-level substrate
for that direction.
The fit is strongest
in the layers
that A113 identified
as load-bearing for vertical deployment,
namely the engineering commitments
for real-time hypermedia composition.
The fit is weakest
in the layers
that A113 identified
as not load-bearing
for a vertical strategy,
namely the consumer-oriented
graphics and editor ecosystems.
The asymmetry is favourable
for the vertical entry strategy
that A113 recommended
as the only path
with historical precedent.

The work required
above Keleusma
remains substantial.
A link store,
a content-addressed storage wrapper,
a widget layer,
a file-world bridge,
and a Model Context Protocol server
are five distinct projects
that compose into
a vertical hypermedia operating system.
Each project
is tractable for a small team
with a decadal horizon.
None of the projects
requires inventing
new languages,
new kernels,
or new graphics systems.
The pieces
exist or are on the roadmap.

Whether anyone will build it
remains
the question A113 ended with.
This article does not answer it.
It only confirms
that the language-level substrate
is no longer
a credible objection
to the program.

## References

- [Reference, Cap'n Proto][ref_capn_proto]
- [Reference, Capsicum][ref_capsicum]
- [Reference, Cairo Graphics 2D Library][ref_cairo_graphics]
- [Reference, Chromium Embedded Framework][ref_cef]
- [Reference, CodeMirror][ref_codemirror]
- [Reference, Coalition for Content Provenance and Authenticity][ref_c2pa]
- [Reference, Content Credentials][ref_content_credentials]
- [Reference, DO-178C][ref_do_178c]
- [Reference, FreeType][ref_freetype]
- [Reference, Genode Operating System Framework][ref_genode]
- [Reference, HarfBuzz][ref_harfbuzz]
- [Reference, Hypercore Protocol][ref_hypercore]
- [Reference, IEC 62304][ref_iec_62304]
- [Reference, InterPlanetary File System][ref_ipfs]
- [Reference, Iroh][ref_iroh]
- [Reference, ISO 26262][ref_iso_26262]
- [Reference, JetBrains Meta Programming System][ref_mps]
- [Reference, JX Operating System][ref_jx]
- [Reference, Keleusma on crates.io][ref_keleusma_crates]
- [Reference, Keleusma on docs.rs][ref_keleusma_docs]
- [Reference, Keleusma source repository][ref_keleusma_repo]
- [Reference, Lexical Editor Framework][ref_lexical]
- [Reference, LLVM Compiler Infrastructure][ref_llvm]
- [Reference, Loro CRDT Library][ref_loro]
- [Reference, LVGL Graphics Library][ref_lvgl]
- [Reference, Model Context Protocol][ref_mcp]
- [Reference, PREEMPT_RT Linux Patch][ref_preempt_rt]
- [Reference, ProseMirror][ref_prosemirror]
- [Reference, Same-Origin Policy][ref_same_origin_policy]
- [Reference, seccomp][ref_seccomp]
- [Reference, seL4 Microkernel][ref_sel4]
- [Reference, Servo Browser Engine][ref_servo]
- [Reference, Skia Graphics Library][ref_skia]
- [Reference, Slint User Interface Toolkit][ref_slint]
- [Reference, TipTap Editor][ref_tiptap]
- [Reference, WebAssembly Component Model][ref_wasm_component_model]
- [Reference, WebKit][ref_webkit]
- [Reference, Yjs CRDT Library][ref_yjs]
- [Reference, Automerge CRDT Library][ref_automerge]
- [Related Post, BTRON, Hypermedia, and the Real-Time Desktop][related_post_btron_hypermedia]
- [Related Post, Getting Started with Keleusma 0.1.1][related_post_keleusma_0_1_1]
- [Related Post, A Verifiable Control Kernel in Keleusma for a Truthful-Machine Architecture][related_post_keleusma_verifiable_kernel]
- [Related Post, Getting Started with Keleusma 0.2.0][related_post_keleusma_0_2_0]
- [Related Post, Information-Flow Control, A Deep Dive with Keleusma][related_post_keleusma_ifc]
- [Research, PROV-AGENT Unified Provenance for AI Agent Interactions, IEEE eScience 2025][research_prov_agent]

[ref_automerge]: https://automerge.org/
[ref_c2pa]: https://c2pa.org/
[ref_cairo_graphics]: https://www.cairographics.org/
[ref_capn_proto]: https://capnproto.org/
[ref_capsicum]: https://papers.freebsd.org/2010/rwatson-capsicum/
[ref_cef]: https://github.com/chromiumembedded/cef
[ref_codemirror]: https://codemirror.net/
[ref_content_credentials]: https://contentcredentials.org/
[ref_do_178c]: https://en.wikipedia.org/wiki/DO-178C
[ref_freetype]: https://freetype.org/
[ref_genode]: https://genode.org/
[ref_harfbuzz]: https://harfbuzz.github.io/
[ref_hypercore]: https://github.com/holepunchto/hypercore
[ref_iec_62304]: https://en.wikipedia.org/wiki/IEC_62304
[ref_ipfs]: https://ipfs.tech/
[ref_iroh]: https://www.iroh.computer/
[ref_iso_26262]: https://en.wikipedia.org/wiki/ISO_26262
[ref_jx]: https://en.wikipedia.org/wiki/JX_(operating_system)
[ref_keleusma_crates]: https://crates.io/crates/keleusma
[ref_keleusma_docs]: https://docs.rs/keleusma
[ref_keleusma_repo]: https://github.com/sgeos/keleusma
[ref_lexical]: https://lexical.dev/
[ref_llvm]: https://llvm.org/
[ref_loro]: https://github.com/loro-dev/loro
[ref_lvgl]: https://lvgl.io/
[ref_mcp]: https://modelcontextprotocol.io/
[ref_mps]: https://www.jetbrains.com/mps/
[ref_preempt_rt]: https://wiki.linuxfoundation.org/realtime/start
[ref_prosemirror]: https://prosemirror.net/
[ref_same_origin_policy]: https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy
[ref_seccomp]: https://en.wikipedia.org/wiki/Seccomp
[ref_sel4]: https://sel4.systems/
[ref_servo]: https://servo.org/
[ref_skia]: https://skia.org/
[ref_slint]: https://slint.dev/
[ref_tiptap]: https://tiptap.dev/
[ref_wasm_component_model]: https://component-model.bytecodealliance.org/
[ref_webkit]: https://webkit.org/
[ref_yjs]: https://yjs.dev/
[related_post_btron_hypermedia]: {% post_url 2026-05-23-btron_hypermedia_and_real_time_desktop %}
[related_post_keleusma_0_1_1]: {% post_url 2026-03-14-keleusma_getting_started %}
[related_post_keleusma_0_2_0]: {% post_url 2026-05-28-keleusma_0_2_0_getting_started %}
[related_post_keleusma_ifc]: {% post_url 2026-05-29-information_flow_control_deep_dive_with_keleusma %}
[related_post_keleusma_verifiable_kernel]: {% post_url 2026-05-27-verifiable_control_kernel_in_keleusma %}
[research_prov_agent]: https://arxiv.org/abs/2508.02866
