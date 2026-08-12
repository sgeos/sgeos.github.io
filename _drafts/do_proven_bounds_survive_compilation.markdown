---
layout: post
mathjax: true
comments: true
title: "Do Proven Resource Bounds Survive Compilation? What a Verified Bound Says About the Code That Actually Runs"
date: 2026-08-08 09:00:00 +0000
categories: engineering compilers verification
series: keleusma_native
series_title: Keleusma Native Code Generation
series_index: 3
---
<!-- A371 -->
<script>console.log("A371");</script>

**Somebody proves a program can never use more than a certain amount of memory. Then a compiler rewrites
that program into a different form before it runs. Does the proof still apply?**

**The answer, for the system examined here, is that one half of it does not.** The measurement that shows
it is cheap and quick, which is the uncomfortable part. Nobody had run it.

This article is a case study of a mistake that is easy to make and hard to see. **A property is established
about one thing, and then claimed about a different thing**, with a transformation standing between them
that was never asked to preserve the property. Stated that baldly it sounds like nobody would do it. In
practice it is everywhere.

A performance budget measured in a staging environment and quoted for production. A power draw calculated
from a circuit simulation and quoted for the manufactured board. A safety margin computed for a scale model
and quoted for the full-size structure. **In each case something in between changed the artefact, and in
each case the question is whether it changed the thing being measured.**

The specific case here is a programming language whose entire reason to exist is that it refuses any program
whose time and memory it cannot bound in advance. That language grew the ability to compile down to
machine code. **Nobody had checked whether the bounds still mean anything once the code is machine code.**

## What You Need to Know to Read This

**No compiler background is required, and this section is the reason that claim is true.** Five ideas carry
the whole article.

**A program is written once and exists in several forms.** The form a person writes, an intermediate form
convenient for machines to reason about, and the final form the processor actually executes. **The system
here proves its guarantees about the middle form and ships the last one.**

**Bytecode is that middle form.** It is a simple, regular instruction set that no physical processor
executes directly. A separate program called an interpreter reads it and does what it says. Because bytecode
is simple and regular, **it is unusually easy to reason about**, which is exactly why the guarantees are
proven there.

**Machine code is the final form**, the instructions a physical processor runs. Getting from bytecode to
machine code means running an optimising compiler, and **an optimising compiler is allowed to rewrite the
program almost arbitrarily** as long as the program still computes the same answers. It may delete work,
duplicate work, reorder work and change where values are stored.

**The stack frame is the block of memory a function uses for its own working values.** How large it is
depends on how many values the compiler decides to keep in memory rather than in registers.

**Registers are the processor's small set of very fast storage locations**, and there are only a few dozen.
Deciding which values live in registers and which get pushed out into the stack frame is a job called
**register allocation**, and it is the compiler's decision rather than the programmer's.

**That last point is the whole article.** The guarantee is a statement about the middle form. The stack
frame is a decision the compiler makes about the final form. **They are not the same quantity, and nobody
had written down an argument connecting them.**

## The Uncomfortable Answer

**Verifying that the compiler is correct is not enough**, and this is the part that surprises people who
work on verified compilers for a living. A compiler proved correct guarantees that the program still
computes the same answers. **It says nothing whatever about how much memory or time the program uses**,
because resource consumption is not part of what "the same answers" means.

So a compiler can be perfectly, provably correct and still multiply a program's memory use tenfold.
**Correctness and resource preservation are different properties, and having the first says nothing about
the second.**

## What Was Measured

The system studied here is Keleusma, whose compiler backend is described in the
[first][related_post_a369] and [second][related_post_a370] articles in this series. **Three results
follow, and the one that looks strong is the weak one.**

**The memory bound does not transfer, and this is not a close call.** The bound is denominated in units of
the middle form. The stack frame is decided by the register allocator. Measured across the whole corpus,
the compiler emits **38,601 stack allocations** with optimisation switched off and **exactly zero** after
the pipeline that actually ships. Every one is promoted into a register. **Whatever the shipped code costs
in memory, the proven number is not measuring it.**

**The time bound is in better shape and its evidence is much weaker than it looks.** The argument that a
fast implementation is covered by a slow one's bound is sound in outline, and it rests on an assumption
that is testable. This article tests it. **The test passes and the sample has only three distinct
magnitudes in it**, which makes the pass very nearly meaningless.

**The third result is that the two bounds fail in different ways**, which decides what work each of them
needs. One has to be recomputed from the shipped artefact. The other has to be measured.

## The Setting

Keleusma refuses any program whose worst-case running time or worst-case memory use cannot be established
before it runs. That refusal is the language's reason to exist, and a program that survives it carries two
numbers.

**The first is a worst-case time.** It is found by looking at every path the program could take through the
bytecode, adding up the cost of each instruction along the way, and keeping the most expensive path. The
cost of an instruction comes from a table of measured costs, written $c$ below, calibrated against the
interpreter that executes bytecode. Formally, with $\Pi(k)$ the set of paths through a unit of code $k$,

$$T_{\mathrm{vm}}(k) \;=\; \max_{\pi \in \Pi(k)} \; \sum_{\iota \in \pi} c(\iota),$$

**The other is a worst-case memory.** Bytecode keeps its intermediate values on a stack, and the verifier
finds the deepest that stack ever gets. Multiplying that depth by the size of one value, written $w$, and
adding a separately computed allocation requirement gives

$$M_{\mathrm{vm}}(k) \;=\; w \cdot \max_{ip} \mathrm{depth}(k, ip) \;+\; \mathrm{arena}(k),$$

**Both numbers are functions of the bytecode and of nothing else.** That is exactly what makes them
provable before the program runs, and it is exactly the property this article puts under strain, because
the artefact that ships is not the bytecode.

The path from one to the other runs through LLVM, a widely used compiler toolkit. The backend translates
bytecode into LLVM's own intermediate form, and LLVM turns that into machine code for whichever processor is
being targeted.

### Notation

Let $P$ denote a program and $\mathcal{B}(P)$ its bytecode. Write

$$T_{\mathrm{vm}}(P), \qquad M_{\mathrm{vm}}(P)$$

for the verifier's time and memory bounds, and

$$T_{\mathrm{nat}}(P), \qquad M_{\mathrm{nat}}(P)$$

for the true worst case of the native artefact on its target. **The claim under examination is the
transfer claim**,

$$T_{\mathrm{nat}}(P) \le \alpha \, T_{\mathrm{vm}}(P) \quad \text{and} \quad M_{\mathrm{nat}}(P) \le \beta \, M_{\mathrm{vm}}(P)$$

for constants $\alpha, \beta$ that do not depend on $P$. **Everything turns on whether such constants exist**,
and the two halves fail differently.

## Result 1: The Memory Bound Does Not Transfer

**The proven memory bound counts slots on the bytecode's own value stack.** Across the units of code this
article measures, which are the entry points of the language's stream construct, it ranges from 384 to
2,464 bytes, with between 6 and 71 named variables each.

**The stack frame contains something else entirely, and the way it is built is worth following.**

The backend does not consult the proven depth at all. For every function it reserves a fixed 64 slots,
whatever the verifier proved, plus one slot for each named variable. In LLVM's intermediate form each of
those reservations is a [stack allocation instruction][ref_llvm_langref]. The rest of the frame is not the
backend's choice either. It is fixed by the target processor's calling convention, which dictates which
registers a function must preserve for its caller and how the frame must be aligned, and those rules come
from documents like [System V AMD64][ref_sysv_amd64] and [AAPCS64][ref_aapcs64].

So with optimisation switched off the frame is

$$M_{\mathrm{nat}}^{O_0}(f) \;=\; 8\bigl(64 + \mathrm{locals}(f)\bigr) + \text{callee-saved} + \text{alignment},$$

in which **the verifier's proven depth does not appear anywhere.** The number of allocations this predicts
is exact rather than approximate, and the measuring instrument asserts it rather than the author eyeballing
it,

$$A_{O_0} \;=\; \sum_{f} \bigl(\mathrm{MAX\_STACK} + \mathrm{locals}(f)\bigr) \;=\; 38{,}601,$$

which matches the measured count across all 19 modules with nothing left over. **An equation printed in an
article is a claim like any other**, so this one is wired to a test that fails if the compiler ever stops
behaving that way. **A unit of code proven to need three slots and one proven to need sixty are given
identical space.**

**And then the optimiser deletes all of it.**

| | |
|---|---|
| stack allocations emitted, optimisation level zero | **38,601** |
| stack allocations surviving the shipped pipeline | **0** |

A standard optimisation pass notices that these values never need a memory address and moves every one of
them into a register. **The frame that actually ships is whatever the register allocator later decides it
cannot fit in registers and must push back out to memory**, which is called spilling. That decision is made
by the [code generator][ref_llvm_codegen] from the number of registers the target processor has, the exact
sequence of optimisation passes, the version of LLVM in use, and the code surrounding the function.

$$M_{\mathrm{nat}}^{O_2}(f) \;=\; \mathrm{spill}(f, \text{target}, \text{pipeline}, \text{version})$$

**There is no $\beta$.** The two quantities are not proportional, not ordered, and not in the same units.
$M_{\mathrm{vm}}$ is a property of the program and $M_{\mathrm{nat}}$ is a property of the compiler's
decisions about the program. A bound on the first constrains the second only through an argument nobody has
made.

**This is the sharpest form of the finding and it is not a defect in the compiler.** The translation is
doing the ordinary thing that every compiler does. **The defect is in the inference**, which was never
stated explicitly and was therefore never examined.

### The same architecture exists in production, and it does not transfer the bound

**The closest thing to this system running in production is inside the Linux kernel**, and it is worth
studying because it faces exactly the same configuration.

Linux lets ordinary programs load small pieces of code into the kernel to filter network packets, trace
system behaviour and so on. That is obviously dangerous, so the kernel first verifies the submitted
bytecode for termination and resource use, and then compiles it to machine code for speed. **A bytecode
program is verified, then compiled, and the kernel must not be harmed by the result.** The component that
does the verifying is called the [eBPF verifier][ref_ebpf_verifier].

**It does not transfer a memory bound. It fixes one.** The stack is capped at a constant, enforced on the
bytecode, and the just-in-time compiler is written to respect that cap rather than being trusted to preserve
a computed number. The bound is a *contract the compiler is built against*, not a quantity carried across
the boundary.

[WebAssembly][ref_wasm_spec] draws the same line in a different place. Its validation step establishes
properties about types and control flow, and deliberately establishes **nothing at all about the resource
consumption of the compiled result.** Whoever embeds a WebAssembly engine is expected to bound resources by
their own means while the program runs.

**Neither system does what this project has been assuming.** That is the most useful thing the survey
contributes, and it points at the two available answers. **Either fix a bound that the backend is built to
respect, or compute one from the artefact that ships.** Transferring a bound across the boundary is not
among the options anybody deploys.

## Result 2: The Time Bound's Argument Is Sound And Its Evidence Is Thin

**The argument for time is an argument from domination, and in plain terms it is this.** If running each
operation as machine code is never slower than running it in the interpreter, then whatever bound covers the
interpreter also covers the machine code. The slow thing's limit covers the fast thing.

Written out it needs slightly more. It needs a way of saying which machine instructions came from which
bytecode instruction, written $\phi$ below, and it needs each bytecode instruction's real machine cost to
stay inside its modelled cost,

$$\forall \iota \in \mathcal{B}(P): \quad \sum_{\iota' \in \phi^{-1}(\iota)} t_{\mathrm{nat}}(\iota') \;\le\; \kappa \, c(\iota),$$

from which $T_{\mathrm{nat}} \le \kappa \, T_{\mathrm{vm}}$ follows by summing along the worst path.

**The premise is an empirical claim and $\phi$ is the fragile part of it.** An optimising compiler routinely
copies a function's body into its callers, combines several operations into one wide instruction, deletes
work whose result is never used, and shares a computation between two places that both needed it. **Every
one of those destroys the correspondence $\phi$ presumes.** After optimisation there may be no machine
instruction attributable to a given bytecode instruction at all, or one machine instruction attributable to
a dozen.

The argument survives only if the total inequality holds without the correspondence holding, which is a
weaker thing to know and a harder thing to establish. It also requires that **no operation becomes slower**
as machine code, which a safety check, a call back into the runtime, or a memory layout unfriendly to the
processor's cache could each violate.

**The ordering is testable without any timing equipment.** If the bytecode bound is standing in for machine
cost, then a unit of code with a larger bound should not produce a smaller body of machine instructions.

Define an **inversion** as a pair of code units that the two measures order oppositely,

$$\mathrm{inv} = \bigl|\{(a,b) : T_{\mathrm{vm}}(a) < T_{\mathrm{vm}}(b) \;\wedge\; S(a) > S(b)\}\bigr|$$

with $S$ the number of machine instructions emitted. **A single inversion falsifies the proxy.** Only pairs
that the bound actually orders can contribute, so the denominator is not the number of pairs but

$$N_{\prec} = \bigl|\{(a,b) : T_{\mathrm{vm}}(a) < T_{\mathrm{vm}}(b)\}\bigr| \;\le\; \binom{n}{2},$$

and a sample concentrated on a few distinct magnitudes drives $N_{\prec}$ far below $\binom{n}{2}$. The
inversion count is the numerator of a standard rank correlation, so the result can equivalently be read as

$$\tau \;=\; 1 - \frac{2\,\mathrm{inv}}{N_{\prec}},$$

and $\tau = 1$ on a sample of three magnitudes is a much smaller statement than $\tau = 1$ on a spread.

The measurement over every entry point that reaches machine code is as follows.

```
stream chunks with both figures : 9
comparable pairs                : 36
INVERSIONS                      : 0
```

### Why that zero is much weaker than it appears

**Seven of the nine units of code have identical figures**, at $T_{\mathrm{vm}} = 14$ and $S = 72$. The
sample contains exactly **three distinct magnitudes**.

| $T_{\mathrm{vm}}$ | $S$ | code units |
|---|---|---|
| 14 | 72 | 7 |
| 45 | 153 | 1 |
| 164 | 1,143 | 1 |

Of the 36 pairs, only **15 are strictly ordered** by the bound. The remaining 21 are ties and **cannot
invert by construction**. So the headline zero is a zero over fifteen comparisons among three magnitudes,
which is barely a test at all.

**Reporting it as "0 of 36" would be the same error this series has now documented three times**: a figure
that is arithmetically correct and answers a smaller question than it appears to. The honest statement is
that no inversion was found and that the sample lacks the resolution to find one.

## Result 3: The Two Bounds Fail Differently, Which Matters For What To Do

**The memory bound is broken in kind.** No constant relates the two quantities, because one of them is not
a property of the program at all. Fixing it means computing a memory bound from the shipped artefact and
transferring nothing to it.

**The time bound is unbroken in kind and unevidenced in degree.** The domination argument may well hold. It
rests on an assumption that has not been tested at any useful resolution, and on a unit conversion
$\alpha$ that has never been calibrated. The project's own architecture notes that the interpreter cost model does not translate and that
per-platform calibration is needed, which is the same gap stated from the other side.

Writing $\mathcal{R}$ for a resource measure, the two failures differ in kind,

$$\nexists \beta : \mathcal{R}^{\mathrm{mem}}_{\mathrm{nat}} \le \beta\, \mathcal{R}^{\mathrm{mem}}_{\mathrm{vm}}, \qquad \exists \alpha \text{ (uncalibrated)} : \mathcal{R}^{\mathrm{time}}_{\mathrm{nat}} \le \alpha\, \mathcal{R}^{\mathrm{time}}_{\mathrm{vm}},$$

which call for different work, being recomputation in the first case and measurement in the second.

**A project that shipped native artefacts today would be shipping the language's central promise
unsupported**, and would not be lying, because the promise is about the bytecode and the bytecode still
carries it. That is precisely the kind of true statement that misleads.

## Threats to Validity

**The corpus is small and the part of it this article can measure is smaller.** Nine units of code and
three distinct magnitudes. Every claim about the time proxy is bounded by that.

**The instruction count is a proxy for a proxy.** Native instruction count bounds execution time only under
a bound on cycles per instruction,

$$T_{\mathrm{nat}}(f) \;\le\; \mathrm{CPI}_{\max} \cdot S(f),$$

and $\mathrm{CPI}_{\max}$ is exactly what cache misses, branch misprediction and memory stalls make
unbounded without a target model. **That is the assumption the timing-analysis literature exists to
refuse.** Instruction count ignores latency, cache behaviour, branch prediction and superscalar issue. A monotone relationship between bound and
instruction count is weak evidence for a monotone relationship between bound and time, and no evidence at all
about magnitude.

**The frame measurement is at the intermediate representation, not the machine.** Counting stack allocations
before and after the pipeline shows that the verifier's number does not survive into the frame decision. It
does not measure the final frame, which requires reading emitted machine code and is deferred for a
mechanical reason. The per-function frame sizes live in a named section of the object file, closely
related to the metadata [LLVM stack maps][ref_llvm_stackmaps] describe, in the sense the
[ELF generic binary interface][ref_elf_gabi] gives that word, and it is emitted only in that object
format while the development machine produces Mach-O. The equivalent capability exists in other toolchains as
[GCC's `-fstack-usage`][ref_gcc_devopts] and [Clang's stack-size section][ref_clang_cli], so the gap is one
of host configuration rather than of principle.

**The author wrote both the compiler being measured and the instrument measuring it.** The mitigation
offered is that the finding is unfavourable to the author's own prior work and would have been more
comfortable suppressed.

## Pattern Extraction

**Verifying the transformation does not preserve the property.** A formally verified compiler $\mathcal{C}$
proves semantic equivalence,

$$\llbracket \mathcal{C}(P) \rrbracket \;=\; \llbracket P \rrbracket,$$

while the property wanted here is a separate inequality over a resource measure $\mathcal{R}$,

$$\mathcal{R}\bigl(\mathcal{C}(P)\bigr) \;\le\; \beta \, \mathcal{R}(P).$$

**Neither implies the other.** Semantic equivalence quantifies over observable behaviour, and resource use is
not observable behaviour in any of these semantics, so a transformation may multiply the stack tenfold and
remain perfectly correct. **Correctness and resource preservation are independent
properties**, and a project that has the first frequently believes it has the second.

**A property proven of a model constrains the artefact only through a stated argument.** The argument here
was never written down, which is why it was never checked. Where a claim crosses a representation boundary,
the crossing deserves its own explicit statement, and the absence of one is not evidence that it is trivial.

**When two measures disagree in kind, no amount of correlation rescues them.** The memory bound and the
native frame are not weakly correlated. They measure different things, in different units, decided by
different agents. Looking for a constant of proportionality between them is a category error dressed as an
empirical question.

**A zero result inherits the resolution of its sample.** Zero inversions over three distinct magnitudes is
not the same claim as zero inversions over a spread, and the two are reported identically by any instrument
that prints a count. **Report the resolution beside the result or the result will be read as stronger than
it is.**

## The Contemporary Literature

Five literatures bear on whether a resource bound survives translation, and **one of them has solved the
problem this article discovers**. The others each hold a piece. What follows surveys them and marks where the
present project sits, which is behind all five.

### Resource analysis is a field, and it works on the artefact you intend to run

The static prediction of time and space from program text is mature.
[Hofmann and Jost 2003][research_hofmann_jost_2003] give a type system inferring heap-space bounds for
first-order functional programs, and [Hoffmann, Aehlig and Hofmann 2012][research_hoffmann_2012] extend
amortised analysis to multivariate bounds. [Danielsson 2008][research_danielsson_2008] shows the same
discipline embedded lightweightly in a dependently typed language.

**Directly on the present configuration**, [Albert and others 2007][research_albert_2007] perform cost
analysis **of Java bytecode**, which is exactly the artefact Keleusma's verifier analyses. That work is
careful about what its bounds mean, and it means them about the bytecode, executed by a virtual machine. It
does not claim them for a just-in-time compiled result.

**The pattern across the field is that the analysis targets the representation that will run.** Nobody in
this literature proves a bound on one representation and ships another, which is what makes the present
project's assumption unusual rather than merely unverified.

### Cost-preserving compilation is the exact problem, and it has a research programme

**The CerCo project is the closest existing work to what this article says is needed.**
[Amadio and Régis-Gianas 2012][research_amadio_2012] and
[Ayache, Amadio and Régis-Gianas 2012][research_ayache_2012] build a certified C compiler that does not
transfer a cost bound but **lifts a cost model upward**: the compiler emits cost annotations on the source,
justified by the assembly it actually produced, so the bound the programmer reasons about is derived from
the artefact and never asserted about a model of it.

That inversion is the whole idea. **The compiler is the thing that knows what the code became**, so it is the
right component to report cost, and a bound computed before compilation is computed by the component with
the least information.

[Carbonneaux, Hoffmann, Ramananandro and Shao 2014][research_carbonneaux_2014] do the memory half and do it
end to end, giving **verified stack-space bounds for C programs proven all the way down to the assembly**,
with the compiler's own frame decisions inside the proof. [Carbonneaux, Hoffmann and Shao 2015][research_carbonneaux_2015] generalise to
compositional certified resource bounds. **This is the literature that already contains the answer to
Result 1**, and its existence means the memory problem here is not open research but unimplemented practice.

### Worst-case execution time analysis will not accept an operation count

**This is the field that predicts how long a program can possibly take on a particular processor**, and it
is the field a native timing claim would have to satisfy. The standard survey,
[Wilhelm and others 2008][research_wilhelm_2008], sets the requirement plainly. A sound timing analysis
needs a model of the target processor's pipeline and memory hierarchy.
[Heckmann and others 2003][research_heckmann_2003] make the sharper point that processor architecture
determines what any tool can achieve, and
[Puschner and Burns 2000][research_puschner_burns_2000] give the earlier review of the same ground.

The techniques are specific and not one of them is a count of operations.
[Li and Malik 1995][research_li_malik_1995] turn the search for the most expensive path into an optimisation
problem that a solver can answer. [Ferdinand and Wilhelm][research_ferdinand_wilhelm] predict cache
behaviour precisely enough for such a search to consume. And [Reineke and others 2007][research_reineke_2007]
show that **the processor's cache replacement policy itself determines whether prediction is possible at
all**, so the same program on the same instruction set can be analysable or not depending on a hardware
choice nobody in the software made.

[Kirner and Puschner 2008][research_kirner_puschner_2008] enumerate the obstacles, and the one that matters
here is stated plainly in that literature. **The compiler is itself an obstacle**, because optimisation
destroys the correspondence between the structure a person or a verifier reasons about and the sequence of
instructions that actually executes.
[Falk and Lokuciejewski 2010][research_falk_2010] respond by building a compiler that optimises *for*
worst-case time, which is the constructive version of the same observation.

**This is the literature that refuses the second half of the transfer claim.** An operation count calibrated
against an interpreter is not an input to any of these methods.

### Translation validation is the technique for a compiler you cannot change

**The idea is to stop trying to prove the compiler correct once and for all, and instead check each
individual run.** [Pnueli, Siegel and Singerman 1998][research_pnueli_1998] introduce it and
[Necula 2000][research_necula_2000] applies it to an optimising compiler. Rather than proving the compiler
correct, prove that this particular output is equivalent to this particular input. [Sewell and others 2013][research_sewell_2013]
carry it to a production operating-system kernel by proving the binary refines the C.

**That fits the present problem well, because the property here is per-artefact and fragile.** A resource
bound depends on decisions an optimiser makes for reasons specific to one program, which is precisely the
situation translation validation was invented for, and it is much cheaper than verifying an entire
backend.

### Verified compilation preserves semantics and says nothing about cost

**A verified compiler is one whose correctness has itself been proven mathematically**, which is a
formidable achievement and a narrower one than it sounds.
[Leroy 2009][research_leroy_2009_cacm] and [Leroy 2009b][research_leroy_2009_jar] establish CompCert, the
best known example. [Blazy and Leroy 2008][research_blazy_leroy_2008] give the model of memory that
underpins it, and [Kumar and others 2014][research_kumar_2014] establish CakeML on the same principle.

**None of these claims resource preservation and none is careless about saying so.** The theorems are about
observable behaviour. A project that reads "verified compiler" as "my bounds survive" has imported a
guarantee that was never offered, which is the misreading Result 1 makes concrete rather than a strawman.

[Necula 1997][research_necula_1997] gives the shape the eventual answer probably takes, in which the
artefact carries machine-checkable evidence about itself, and that is what this project's plan to export a
memory requirement as a linker symbol already gestures at without yet having anything sound to put in it.

### Bounded execution in deployed systems, which is where the practice is

[Regehr, Reid and Webb 2005][research_regehr_2005] eliminate stack overflow by abstract interpretation **of
machine code**, and [Brylow, Damgaard and Palsberg 2001][research_brylow_2001] check interrupt-driven
assembly for stack bounds directly. **Both make the same choice, which is to analyse the thing that executes.**

For the bytecode-then-native configuration specifically,
[Gershuni and others 2019][research_gershuni_2019] give a static analysis for untrusted Linux kernel
extensions, which is the research counterpart of the [eBPF verifier][ref_ebpf_verifier] discussed above.
**That system fixes a stack cap rather than transferring a computed bound**, and the commercial tools
[StackAnalyzer][ref_absint_stackanalyzer] and [aiT][ref_absint_ait] recompute from the binary against a
target model, because [ISO 26262][ref_iso26262] and its siblings ask for evidence about the executable.

### What the survey shows

**The composition this project assumed does not appear anywhere.** Resource analysis targets the
representation that runs. Cost-preserving compilation lifts a model up from the artefact rather than pushing
a bound down onto it. Timing analysis demands a target model. Verified compilation deliberately scopes
itself to semantics. Deployed systems either fix a cap or recompute.

**Five literatures, and not one transfers a resource bound across a compilation boundary.** That is a
stronger statement than saying this article found no support, and it is the survey's actual contribution.
**The assumption is not merely unproven here. It is contrary to the practice of every field that has
addressed the problem.**

The corollary is that Result 1 is **not a research problem**. `Carbonneaux and others 2014` did end-to-end
verified stack bounds a decade ago. What this project has is an unimplemented known technique, which is a far
better position than an open question and a far worse one than the assumption it replaces.


## The Source Base

The backend takes the compiler's own in-memory representation of a module and emits LLVM's intermediate
form through the [inkwell][ref_inkwell] Rust bindings. The two bounds are computed by the verifier from the
same bytecode.

The measuring instrument compiles the whole corpus and translates each module twice, once with optimisation
switched off and once through the pipeline that actually ships, counting stack allocations in each. It then
pairs every entry point's proven bound against the number of machine instructions emitted for it. **It
reports and does not assert**, because the distribution is a fact about this corpus and not a property
the code should be held to. **The whole run takes about nine seconds**, which is the figure behind the
claim in the opening that nobody had looked rather than that looking was hard.

## Epistemic State

**Measured, and reproducible from the instrument.** Across 19 lowerable modules the generator emits 38,601
stack allocations at optimisation level zero and 0 after the shipped pipeline. The fixed operand
provisioning is 64 slots per function. Nine stream entry points carry both a proven bound and an emitted
instruction count, and they span three distinct magnitudes, being $(14, 72)$, $(45, 153)$ and $(164, 1143)$. Over 36
pairs, of which 15 are strictly ordered, there are 0 inversions. Measured memory bounds for stream entry
points range from 384 to 2,464 bytes with 6 to 71 locals.

**Derived, and checkable from the definitions.** That the proven operand depth does not appear in the
unoptimised frame expression, since the provisioning is a constant. That a tie cannot be an inversion, so
the inversion count is taken over 15 pairs rather than 36. That semantic preservation does not entail
resource preservation, since a transformation may change spilling while preserving observable behaviour.

**Assumed, and marked as such.** That instruction count is monotone in execution time. It is not, and the
article's second result should be read as evidence about code size that is suggestive about time. **The
instrument's nine-second runtime is the author's report rather than an independently timed figure**, and
nothing in the argument depends on it.

**Verified, and this time the instrument found real defects.** All 27 research identifiers were resolved
against the registry and compared to the cited work. **Four were wrong, an error rate of 14.8 percent**, and
none of the four was an artefact of the checking method. One digit was transposed, sending
`Static checking of interrupt-driven software` to a different paper in the same proceedings. One cited the
wrong volume and year for the Amadio and Régis-Gianas cost-annotation work. One attributed a 2003 paper by
Heckmann and others to Wilhelm and others in 2009, wrong in author, year and identifier together. One
resolved to a genuine and relevant paper that was **not the one named**, sending a citation of Theiling on
separated cache and path analyses to Ferdinand and Wilhelm on cache behaviour prediction, and that entry was
relabelled to the work the identifier actually designates rather than dropped.

**This is a materially worse rate than the previous article in this series**, which resolved 31 of 31, and
the difference is instructive rather than random. **This bibliography is larger, older, and drawn from
proceedings series where adjacent identifiers differ by a single digit.** **The error rate rises with the volume
supplied from memory**, which is an argument for searching the registry by title and never recalling an
identifier, and all four corrections here were obtained that way.

**Surveyed rather than measured.** That the eBPF verifier fixes a stack cap rather than transferring a
computed one, and that WebAssembly validation establishes nothing about the compiled result's resource use,
are readings of those specifications and not experiments. They are load-bearing for the conclusion's
recommendation and a reader who doubts them should check the cited documents rather than trust the summary.

**What this article does not establish.** The actual native worst-case memory of any artefact, which requires
reading emitted machine code in an object format this host does not produce. The value of $\alpha$, which
requires per-platform calibration. Whether the domination premise holds for every operation, which was
argued and not measured. Whether any inversion exists at higher resolution.

**The strongest claim the evidence supports** is that the memory bound proven on bytecode does not constrain
the native frame, because the quantity it measures is absent from the frame's determination and the
provisioning it might have constrained is deleted by the optimiser. **The weakest link is the timing
result**, whose zero inversions rest on three distinct magnitudes and should not be cited as support for the
domination argument.

## Out of Scope

The design of a native memory analysis, which is the obvious follow-up and is a separate subject. Per-platform
timing calibration. The choice of calling convention, treated in the [previous article][related_post_a370].
Register allocation and spilling as techniques. Any claim about execution time, which would require a timing
rig this article does not have.

## Conclusion

A language that refuses programs it cannot bound had built a compiler that discards the bound. Not through a
defect, and not through carelessness in the translation, but because **the inference from a verified model
to a generated artefact was never written down and was therefore never examined**. It reads as obvious until the
moment someone counts, and then it reads as two quantities in different units decided by different agents.

The time bound may well transfer. The argument for it is reasonable, the measurement here is consistent with
it, and the measurement is far too coarse to be called support. The memory bound does not transfer, and no
constant of proportionality is available, because the thing it measures is not the thing that ends up in the
frame.

**The deployed systems point at what to do instead, and neither of them transfers.** The eBPF verifier fixes
a stack cap on the bytecode and builds its just-in-time compiler to respect it. The static-analysis tools the
certification regimes consume recompute the property on the shipped binary against a target model. Those are
the two available shapes, **a contract the backend is built against, or a recomputation from the
artefact**, and this project had been assuming a third that nobody deploys.

**The lesson generalises past compilers.** Wherever a property is proven of a model and claimed for an
artefact, the transformation between them is a premise. It is usually invisible, usually unstated, and
occasionally the whole argument.

## References

### Reference

- [Arm Architecture Procedure Call Standard for the Arm 64-bit Architecture][ref_aapcs64]
- [inkwell, safe Rust bindings to LLVM][ref_inkwell]
- [LLVM Code Generator][ref_llvm_codegen]
- [LLVM Language Reference][ref_llvm_langref]
- [LLVM Stack Maps and Patch Points][ref_llvm_stackmaps]
- [System V Application Binary Interface, AMD64 Architecture Processor Supplement][ref_sysv_amd64]

[ref_aapcs64]: https://github.com/ARM-software/abi-aa
[ref_inkwell]: https://github.com/TheDan64/inkwell
[ref_llvm_codegen]: https://llvm.org/docs/CodeGenerator.html
[ref_llvm_langref]: https://llvm.org/docs/LangRef.html
[ref_llvm_stackmaps]: https://llvm.org/docs/StackMaps.html
[ref_sysv_amd64]: https://gitlab.com/x86-psABIs/x86-64-ABI

### Reference, object formats and toolchain capability

- [Clang Command Line Reference][ref_clang_cli]
- [ELF Generic Application Binary Interface][ref_elf_gabi]
- [GCC Developer Options, including `-fstack-usage`][ref_gcc_devopts]

[ref_clang_cli]: https://clang.llvm.org/docs/ClangCommandLineReference.html
[ref_elf_gabi]: https://refspecs.linuxfoundation.org/elf/gabi4+/contents.html
[ref_gcc_devopts]: https://gcc.gnu.org/onlinedocs/gcc/Developer-Options.html

### Reference, bounded execution in deployed systems

- [AbsInt aiT Worst-Case Execution Time Analyzer][ref_absint_ait]
- [AbsInt StackAnalyzer][ref_absint_stackanalyzer]
- [ISO 26262, Road vehicles, functional safety][ref_iso26262]
- [Linux eBPF Verifier][ref_ebpf_verifier]
- [WebAssembly Core Specification][ref_wasm_spec]

[ref_absint_ait]: https://www.absint.com/ait/
[ref_absint_stackanalyzer]: https://www.absint.com/stackanalyzer/
[ref_ebpf_verifier]: https://docs.kernel.org/bpf/verifier.html
[ref_iso26262]: https://www.iso.org/standard/68383.html
[ref_wasm_spec]: https://webassembly.github.io/spec/core/

### Related Post

- [Related Post, Compiler Backend Bring-Up: Blocking Frequency as the Ordering Principle][related_post_a369]
- [Related Post, Two Ways of Doing One Thing][related_post_a370]

[related_post_a369]: {% post_url 2026-08-06-native_lowering_coverage %}
[related_post_a370]: {% post_url 2026-08-07-two_calling_conventions %}

### Research

- [A compiler framework for the reduction of worst-case execution times][research_falk_2010]
- [A formally verified compiler back-end][research_leroy_2009_jar]
- [A review of worst-case execution-time analysis][research_puschner_burns_2000]
- [CakeML: a verified implementation of ML][research_kumar_2014]
- [Certifying and reasoning on cost annotations in C programs][research_ayache_2012]
- [Certifying and Reasoning on Cost Annotations of Functional Programs][research_amadio_2012]
- [Compositional certified resource bounds][research_carbonneaux_2015]
- [Cost analysis of Java bytecode][research_albert_2007]
- [Efficient and Precise Cache Behavior Prediction for Real-Time Systems][research_ferdinand_wilhelm]
- [Eliminating stack overflow by abstract interpretation][research_regehr_2005]
- [End-to-end verification of stack-space bounds for C programs][research_carbonneaux_2014]
- [Formal verification of a C-like memory model and its uses for verifying program transformations][research_blazy_leroy_2008]
- [Formal verification of a realistic compiler][research_leroy_2009_cacm]
- [Lightweight semiformal time complexity analysis for purely functional data structures][research_danielsson_2008]
- [Multivariate amortized resource analysis][research_hoffmann_2012]
- [Obstacles in worst-case execution time analysis][research_kirner_puschner_2008]
- [Performance analysis of embedded software using implicit path enumeration][research_li_malik_1995]
- [Proof-carrying code][research_necula_1997]
- [Simple and precise static analysis of untrusted Linux kernel extensions][research_gershuni_2019]
- [Static checking of interrupt-driven software][research_brylow_2001]
- [Static prediction of heap space usage for first-order functional programs][research_hofmann_jost_2003]
- [The influence of processor architecture on the design and the results of WCET tools][research_heckmann_2003]
- [The worst-case execution-time problem: overview of methods and survey of tools][research_wilhelm_2008]
- [Timing predictability of cache replacement policies][research_reineke_2007]
- [Translation validation][research_pnueli_1998]
- [Translation validation for a verified OS kernel][research_sewell_2013]
- [Translation validation for an optimizing compiler][research_necula_2000]

[research_albert_2007]: https://doi.org/10.1007/978-3-540-71316-6_12
[research_amadio_2012]: https://doi.org/10.1007/978-3-642-32495-6_5
[research_ayache_2012]: https://doi.org/10.1007/978-3-642-32469-7_3
[research_blazy_leroy_2008]: https://doi.org/10.1007/s10817-008-9099-0
[research_brylow_2001]: https://doi.org/10.1109/icse.2001.919080
[research_carbonneaux_2014]: https://doi.org/10.1145/2594291.2594301
[research_carbonneaux_2015]: https://doi.org/10.1145/2737924.2737955
[research_danielsson_2008]: https://doi.org/10.1145/1328438.1328457
[research_falk_2010]: https://doi.org/10.1007/s11241-010-9101-x
[research_ferdinand_wilhelm]: https://doi.org/10.1023/A:1008186323068
[research_gershuni_2019]: https://doi.org/10.1145/3314221.3314590
[research_heckmann_2003]: https://doi.org/10.1109/jproc.2003.814618
[research_hoffmann_2012]: https://doi.org/10.1145/2362389.2362393
[research_hofmann_jost_2003]: https://doi.org/10.1145/604131.604148
[research_kirner_puschner_2008]: https://doi.org/10.1109/ISORC.2008.65
[research_kumar_2014]: https://doi.org/10.1145/2535838.2535841
[research_leroy_2009_cacm]: https://doi.org/10.1145/1538788.1538814
[research_leroy_2009_jar]: https://doi.org/10.1007/s10817-009-9155-4
[research_li_malik_1995]: https://doi.org/10.1145/217474.217570
[research_necula_1997]: https://doi.org/10.1145/263699.263712
[research_necula_2000]: https://doi.org/10.1145/349299.349314
[research_pnueli_1998]: https://doi.org/10.1007/BFb0054170
[research_puschner_burns_2000]: https://doi.org/10.1023/A:1008119029962
[research_regehr_2005]: https://doi.org/10.1145/1113830.1113833
[research_reineke_2007]: https://doi.org/10.1007/s11241-007-9032-3
[research_sewell_2013]: https://doi.org/10.1145/2491956.2462183
[research_wilhelm_2008]: https://doi.org/10.1145/1347375.1347389
