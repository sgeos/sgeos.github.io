---
layout: post
mathjax: true
comments: true
title: "Keleusma Research Spike: What It Costs to Compile a Data Structure Whose Shape Is Already Decided"
date: 2026-08-09 09:00:00 +0000
categories: engineering compilers verification
series: keleusma_native
series_title: Keleusma Native Code Generation
series_index: 4
---
<!-- A372 -->
<script>console.log("A372");</script>

**The largest remaining item in a compiler backend was estimated at a quarter's work. Measured, it is
pointer arithmetic over compile-time constants, and two of the three representation forms it was supposed to
need account for two operations in the entire corpus.**

The item is aggregate data types, meaning structs, tuples, arrays and enumerations. It blocks **34.5 percent of the
corpus**, more than every other unimplemented feature combined, and it had never been scoped because
everyone knew it was large.

**Everyone was reasoning from the wrong artefact.** Aggregates are large in a compiler that must *decide*
their layout. This compiler decided it already, in an earlier pass, and bakes the answer into the
instruction stream. What reaches the backend is not a type system. It is a byte offset and a scalar kind.

The measurement that establishes this took twenty minutes to write and two and a half seconds to run. It
reports that of 331 aggregate operations in the corpus, **300 are a constant offset and a typed load**, **2
need anything resembling a value representation**, and **0 use the general mechanism the instruction set
still carries**.

**This article reports that, and reports why the author's own recommendation to run it deserves more
scepticism than the result.**

### What this is a case study of

The setting is compiler backend scoping and the project is Keleusma, whose backend is described in the
[first][related_post_a369], [second][related_post_a370] and [third][related_post_a371] articles of this
series. **No compiler background is required.**

The general shape is **estimating the cost of a feature from its name rather than from its instances**.
"Aggregate data types" names something with a large literature, a hard general case, and a well-known set of
representation decisions. None of that is evidence about the work in front of you, and the gap between the
category and the instance is where the estimate went wrong.

The transferable question is **what remains once a decision has already been made upstream.** The answer
is often mechanical, and the mechanical residue is easy to mistake for the original problem because it wears
the same name.

## What You Need to Know to Read This

**No compiler background is required, and this section is what makes that claim true.** Six ideas carry the
whole article.

**A program is written once and exists in several forms.** The form a person writes, an intermediate form
that is easy for machines to handle, and the final form the processor actually executes. **The part of the
compiler that produces that last form is called the backend**, and it is the part being scoped here.

**Bytecode is the intermediate form.** It is a simple, regular list of instructions that no physical
processor runs directly. It is easy to reason about, which is why this project proves things about it.

**An aggregate is several values bundled into one.** A point holding an x and a y. A record holding a name,
an age and an address. Every language has them, and how to represent them in memory is one of the classic
hard problems in compiler design, because the compiler must decide where each field sits, how much space it
takes and how it is found again.

**The hard part is deciding the layout, and this compiler decided it early.** Three stages before the
backend, a pass works out that the x sits at byte 0 and the y at byte 8, and **writes those numbers directly
into the instructions**. By the time the backend sees the program, the question is not how to lay out a
record. It is how to add 8 to an address.

**There are two ways to hold an aggregate, and only one of them is expensive.** The **flat** form is a
plain run of bytes with the fields at known positions. The **boxed** form carries extra bookkeeping
alongside the data so that the shape can be discovered while the program runs. Boxing is what makes
aggregates costly, and the measurement below is largely about how often it is actually needed.

**The last thing worth knowing is where the bytes live.** This language allocates from an **arena**, which
is a fixed-size region whose total is known before the program starts. Taking memory from it is a matter of
moving a marker along, and because the region is fixed and the total is proven in advance, memory taken from
the arena is already accounted for.

## The Setting

Keleusma compiles to bytecode for a virtual machine and, since recently, lowers that bytecode to native code
through [LLVM][ref_llvm_langref]. An aggregate in the source language becomes, in the bytecode, a sequence of
instructions that construct and read it.

The version of the language current here made a decision two releases ago called the **flat-byte
representation**. An aggregate is not a tree of tagged values. It is **a contiguous run of bytes**, and every
field access is a byte offset into that run, resolved by the compiler.

**That decision is why this article exists**, and its consequence had never been traced to the backend.

### Notation

Let $\mathcal{A}$ denote the aggregate operations in a corpus. Each carries a compiler-baked operand drawn
from three forms,

$$\mathcal{A} = \mathcal{A}_{\mathsf{Flat}} \;\sqcup\; \mathcal{A}_{\mathsf{Nested}} \;\sqcup\; \mathcal{A}_{\mathsf{Boxed}},$$

which differ in what a backend must supply.

**$\mathsf{Flat}$** carries a pair $(\mathrm{off}, \kappa)$: a byte offset and a scalar kind. Reading it is

$$\mathrm{load}_{\kappa}\bigl(\mathrm{base} + \mathrm{off}\bigr),$$

with $\mathrm{off}$ a compile-time constant. **This is an address computation and a typed load**, being a
[`getelementptr`][ref_llvm_gep] with constant indices followed by a `load`, and it is the same operation the
backend already performs for the program's data segment.

**$\mathsf{Nested}$** carries $(\mathrm{off}, \mathrm{size}, \mathrm{variant})$ and extracts a byte range,
re-wrapping it as an aggregate. **This is the form that requires an aggregate to exist as a value**, which is
the representation question a backend with a uniform machine-word stack cannot dodge.

**$\mathsf{Boxed}$** is the pre-flat form: a metadata table, a heap body, positional indices. It is the
general mechanism, and it is the one whose cost dominates every estimate of this work.

Write $C(\cdot)$ for implementation cost. The estimate everyone carried was

$$C(\mathcal{A}) \approx C(\mathcal{A}_{\mathsf{Boxed}}),$$

because the boxed form is what "implementing aggregates" means in the general case. **The question this
article answers is whether that term has any instances.**

The distinction the article turns on is *which index set the sum runs over*. An estimate anchored on the
category prices every form the **instruction set** defines,

$$C_{\mathrm{est}} \;=\; \sum_{f \in \mathcal{F}} C(f),$$

while the work actually required prices only the forms the **corpus** contains,

$$C_{\mathrm{act}} \;=\; \sum_{f \in \mathcal{F}} \mathbf{1}\bigl[\lvert \mathcal{A}_f \rvert > 0\bigr] \cdot C(f).$$

The two differ by exactly the terms with no instances,

$$C_{\mathrm{est}} - C_{\mathrm{act}} \;=\; \sum_{f \,:\, \lvert \mathcal{A}_f \rvert = 0} C(f),$$

and **nothing in the feature's name distinguishes them**. That is the whole error, stated before the
measurement that exposes it. **The measurement is an evaluation of that sum**, and the article's result is
that the term which dominated the estimate falls inside it.

**The failure mode this identity describes has a literature**, since pricing $\mathcal{F}$ when the work is
indexed by the corpus is anchoring on the category. [Jørgensen 2004][research_jorgensen_2004] reviews expert
estimation of software effort and finds systematic optimism together with strong anchoring on framing, and
[Jørgensen and Grimstad 2011][research_jorgensen_grimstad_2011] show irrelevant information shifting
estimates directly. **The contribution here is not the observation that estimates anchor.** It is that in
this case the anchor is visible in the index set, so the error can be removed by counting instead of by
debiasing.

## The Measurement

The instrument compiles every program in the shipped example corpus and the self-hosted compiler's own
sources, walks every instruction, and classifies each aggregate operation by its baked form.

| Operation | Count | Share |
|---|---|---|
| `NewComposite::Flat` | 239 | 72.2% |
| `GetTupleField::Flat` | 41 | 12.4% |
| `IsEnum` | 29 | 8.8% |
| `GetIndex::Flat` | 14 | 4.2% |
| `GetEnumField::Flat` | 4 | 1.2% |
| `GetField::Flat` | 2 | 0.6% |
| `GetTupleField::FlatNested` | 2 | 0.6% |
| **Total** | **331** | |

Aggregated by form:

$$\lvert \mathcal{A}_{\mathsf{Flat}} \rvert = 300, \qquad \lvert \mathcal{A}_{\mathsf{Nested}} \rvert = 2, \qquad \lvert \mathcal{A}_{\mathsf{Boxed}} \rvert = 0.$$

**Those three counts total 302 and not 331, which is worth explaining instead of leaving a reader to
subtract.** The 29 discriminant tests carry no form tag at all, since testing which variant an enumeration
holds is a comparison rather than an access, and the operation names no layout. They are counted in the work
below and simply have no representation to be classified by.

**The boxed form has no instances.** The general mechanism, the one that carries the metadata table and the
heap body and the whole weight of the estimate, **is not used by any program this compiler is for**. Taken
with the two nested occurrences, **the two forms other than flat account for 2 of the 302 operations that
carry a form at all**, which is the claim the opening makes and this is where it is checkable.

The constructed bodies are small:

$$\mathrm{byte\_size} \in [8, 64], \quad \text{median } 24, \qquad \mathrm{count} \in [1, 5], \quad \text{median } 3.$$

An aggregate in this corpus is **three values in twenty-four bytes**.

## What Remains, Enumerated

With the boxed term empty, the work is:

**Construction**, 239 instances. Reserve $\mathrm{byte\_size}$ bytes **in the arena** and write the popped
values at their baked offsets,

$$\mathrm{body}\bigl[\mathrm{off}_i,\; \mathrm{off}_i + w_i\bigr) \;\leftarrow\; v_i, \qquad i = 1 \ldots \mathrm{count},$$

then yield a reference to the body.

**The bodies go in the arena, not on the machine stack**, and that is the whole of the memory story. The
language's model is a fixed-size arena with countable bytes, and the interpreter already allocates composite
bodies there. A backend that put them on the machine stack instead would be **departing from the memory
model rather than implementing it**, and would forfeit a bound that already exists, since the `byte_size` operand
is documented as the allocation the worst-case-memory pass sums. Arena allocation is a bump pointer against
a region whose size is proven before the program runs.

The machine stack is still involved, since scalars and addresses live in registers and spill, and local
allocations that do arise belong in the entry block per [LLVM's frontend guidance][ref_llvm_perf_tips], so
the promotion pass can lift them. But **the aggregate bodies themselves are not a frame question.**

Since bodies are at most 64 bytes and constructed from at most five values, an aggregate is a bump
allocation and a run of stores.

**Flat access**, 61 instances across four opcodes. An address computation and a typed load. **The backend
already does exactly this** for the program's data segment, where a slot resolves to a base pointer plus a
constant offset, and that path is implemented and tested.

**Discriminant tests**, 29 instances. A variant is identified by a number stored at the front of the body,
so the test loads that word and compares it against a constant the compiler already knows,

$$\bigl[\mathrm{load}_{\mathrm{word}}(\mathrm{base}) = k\bigr], \qquad k \text{ fixed at compile time},$$

which is an integer comparison and names no layout, **which is why these 29 carry no form tag**.

**Nested access**, 2 instances. The only form needing an aggregate as a first-class value. Because the
representation is contiguous, a child body is a sub-range of its parent,

$$\mathrm{addr}(\mathrm{child}) \;=\; \mathrm{addr}(\mathrm{parent}) + \mathrm{off}, \qquad \mathrm{len}(\mathrm{child}) = \mathrm{size},$$

**so no copy is required** and the operation is an address computation as well. Contiguity, chosen upstream
for unrelated reasons, is what makes the one genuinely hard form cheap.

**Boxed anything**, 0 instances. Refused, at no cost to coverage. The claim being made is universal,

$$\Phi_{\mathsf{Boxed}} \;\equiv\; \forall a \in \mathcal{A} : \mathrm{form}(a) \ne \mathsf{Boxed},$$

so **a single counterexample refutes it** and no quantity of confirming instances would have been needed to
state it. That is the same quantifier structure the [second article][related_post_a370] identified, arriving
here with the opposite sign, since there an existential defeated a proposed unification while here a universal
licenses a refusal.

$$C(\mathcal{A}) \;=\; C(\text{arena bump}) + C(\text{constant-offset store}) + C(\text{constant-offset load}) + C(\text{integer compare}),$$

every term of which the backend already implements for other opcodes.

**And the memory term is already bounded, which is the part most likely to be got wrong.** An earlier
version of this article priced aggregate construction as machine-stack growth and warned that it could
enlarge the native machine frame the [previous article][related_post_a371] measures. **That was an error of design and not of arithmetic**, and it is left visible here because it is the more instructive mistake.

Bodies belong in the arena. Writing $M$ for the arena requirement, the construction term is

$$\Delta M \;=\; \sum_{a \in \mathcal{A}^{\mathrm{new}}} \mathrm{byte\_size}(a),$$

which is **exactly the quantity the worst-case-memory pass already sums**, because `byte_size` is the operand
it was given for that purpose. So the memory cost of aggregate lowering is not a new bound to establish. It
is an existing bound the native artefact inherits by allocating where the interpreter allocates.

**The general point is worth more than the correction.** A backend is free to choose a representation, and
choosing one the language's memory model does not describe converts a bounded quantity into an unbounded
one at no benefit. The stack looked cheaper because it is closer to hand.

## The Estimate Was Wrong Because It Named A Category

**Aggregates are genuinely expensive in a compiler that decides their layout.** Field ordering, padding,
alignment, tag placement, niche optimisation, the interaction with generics and with a garbage collector:
that is real work and it fills textbooks.

**None of it is in front of this backend**, because a pass three stages earlier already did it and wrote the
answers into the instruction operands. What arrives is the residue, being constants, in fields, in an instruction
stream.

The failure mode is worth naming precisely. **The estimate was anchored to the hardest thing the name
denotes**, and the name is accurate. Nothing about the phrase "implement aggregate data types" is
misleading. It simply does not describe the work, and only counting the instances reveals that.

## Threats to Validity

**A corpus of one project.** The zero for the boxed form is a fact about programs written so far. The
instruction set still carries that form, so a program could use it, and the estimate would then be wrong in
the expensive direction. **Refusing it is safe and assuming it will never appear is not**, and the difference
matters for what gets built rather than for what gets counted.

**Cost is estimated, not measured.** Every term above is claimed to be cheap because the backend implements
something structurally identical elsewhere. That is an argument from similarity and it has failed in this
series before, when a string constant was judged cheap by the same reasoning and turned out to require an
entire representation decision.

**Estimating by analogy is a studied method and its record is mixed**, which is the right prior to hold here.
[Shepperd and Schofield 1997][research_shepperd_schofield_1997] set out the technique and report it
outperforming algorithmic models on their datasets, while
[Walkerden and Jeffery 1999][research_walkerden_jeffery_1999] find human-selected analogies doing better than
the automated ones and neither dominating. **The method is respectable and it is not a measurement**, and the
present article uses the weaker human form of it.

**Two instances is not zero.** The nested form has two occurrences, and a design that handles 300 cases and
refuses 2 delivers

$$\frac{\lvert \mathcal{A}_{\mathsf{Flat}} \rvert}{\lvert \mathcal{A}_{\mathsf{Flat}} \rvert + \lvert \mathcal{A}_{\mathsf{Nested}} \rvert} \;=\; \frac{300}{302} \;=\; 0.993,$$

which is less than the headline and not by much. Whether those two sit in modules that are otherwise unblocked is
not established here.

**The author scoped work he would then perform.** This is the sharpest threat and it was flagged before the
measurement was taken, since a result reading "cheaper than feared" from a party who benefits from it starting
sooner deserves more scepticism than one reading "expensive". **The association between an investigator's
interest and a favourable result is measured and not merely suspected**, and
[Bekelman, Li and Gross 2003][research_bekelman_2003] give the systematic review for biomedical research,
where the effect is large and consistent. The domain is not this one and the mechanism is not domain-specific.
The mitigation offered is that the central number is a **zero**, which is harder to produce by motivated
reasoning than a favourable ratio, and that the instrument reports counts a reader can reproduce.

## Pattern Extraction

**Estimate from instances, not from the category.** A feature's name inherits the difficulty of its hardest
form. The work in front of you is whatever your inputs actually contain, and the two are related only by
coincidence.

**An upstream decision converts a design problem into a mechanical one, and the mechanical residue keeps the
original name.** That is why the estimate survived, because everyone kept calling it the same thing after it stopped
being the same work.

**A dead general mechanism is worth finding before it is worth building.** The boxed form is fully specified,
implemented in the interpreter, and used by nothing. **Counting it cost twenty minutes and removed the
dominant term from the estimate.**

**Scepticism should scale with who benefits from the answer.** A scoping result that shortens the scoper's
own work is the configuration in which optimism is least detectable. Preferring a zero to a ratio is one
defence, since a zero is refutable by a single counterexample and a ratio absorbs error quietly.

## The Contemporary Literature

**Data representation is a classical compiler subject and its difficulty lives upstream of code
generation.** The standard treatment in [Appel 1998][research_appel_1998] places layout, tagging and access-path
resolution in the middle end, which is exactly why a backend that receives resolved offsets inherits so
little of it.

### The representation problem is a type-system problem, which is why it is not here

The literature that makes aggregates expensive is about deciding representation **in the presence of
polymorphism**, where a function compiled once must handle values whose layout differs per instantiation.
[Peyton Jones and Salkild 1989][research_pj_salkild_1989] give the tagless machine that makes uniform
representation cheap, [Leroy 1992][research_leroy_1992] introduces the coercion-based unboxing analysis,
[Ohori 1995][research_ohori_1995] gives the polymorphic record calculus together with **a compilation
method that resolves field access to an index computation**, which is the closest antecedent to what this
backend receives already resolved,
[Henglein and Jørgensen 1994][research_henglein_1994] characterise optimal boxing placement;
[Harper and Morrisett 1995][research_harper_morrisett_1995] compile polymorphism by passing types at run
time, [Shao and Appel 1995][research_shao_appel_1995] and [Tarditi and others 1996][research_tarditi_1996]
build type-directed compilers around the idea, and [Shao 1997][research_shao_1997] reconciles the
approaches. [Morrisett and others 1999][research_morrisett_1999] carry types all the way to assembly.

**Every one of these is expensive because the layout is not known when the code is compiled.** Keleusma
monomorphises before bytecode, so every aggregate operation in the corpus refers to exactly one concrete
layout, and the entire literature above answers a question this backend is never asked. That is the precise
sense in which the estimate measured somebody else's problem.

### Object layout is expensive for reasons this language does not have

The object-oriented layout literature concerns inheritance, dynamic dispatch and separate compilation.
[Pugh and Weddell 1990][research_pugh_weddell_1990] give bidirectional record layout for multiple
inheritance, [Gil and Sweeney 1999][research_gil_sweeney_1999] pursue space and time efficiency in the same
setting, and [Driesen and Hölzle 1996][research_driesen_holzle_1996] measure what virtual dispatch costs.

**Keleusma has no inheritance, no subtyping and no separate compilation of dependencies**, so none of these
costs arise. The finding is not that this literature is wrong. It is that a backend inherits only the costs
its language's design admits, and enumerating those is cheaper than assuming all of them.

### Layout is also a performance lever, and the design forecloses it

A parallel literature treats layout as something to *optimise* and not merely to fix.
[Chilimbi, Davidson and Larus 1999][research_chilimbi_def_1999] define cache-conscious structures,
[Chilimbi, Hill and Larus 1999][research_chilimbi_layout_1999] lay them out accordingly, and
[Lattner and Adve 2005][research_lattner_adve_2005] pool-allocate by data structure for locality.

**None of this is in scope, and it is worth saying why**, because a reader could reasonably ask whether the
baked-offset design forecloses it. It does, because the offsets are in the instruction stream, so a backend cannot
reorder fields without invalidating them. **That is a real cost of the design, paid in exchange for the
cheapness this article reports.**

**Unboxing and flattening are the transformations that produce this situation on purpose.**
[Leroy 1992][research_leroy_1992] gives the unboxed-representation analysis for polymorphic languages,
[Peyton Jones and Launchbury 1991][research_pj_launchbury_1991] introduce unboxed values into a lazy
functional compiler, and [Shao 1997][research_shao_1997] treats flexible representation analysis. **All three
are about removing indirection before the backend sees it**, and the flat-byte representation this project
adopted is the same move made at the bytecode boundary.

**The boxed form being dead is an instance of a general finding about specified-but-unused mechanism.**
[Richards and others 2010][research_richards_2010] analyse the dynamic behaviour of deployed JavaScript and
find programs exercising a narrow subset of what the language permits, with the assumptions behind common
optimisations holding far less often than expected. **The direction of that finding is the opposite of this
one and the method is the same**, being to count what the corpus does rather than what the specification allows.

**The method has a name and a literature.** [Dyer and others 2014][research_dyer_2014] mine billions of
syntax-tree nodes to compare **actual against potential** usage of Java language features, which is this
article's question stated generally. [Parnin, Bird and Murphy-Hill 2013][research_parnin_2013] track generics
adoption and find it slower and narrower than the feature's prominence suggests, and
[Callaú and others 2011][research_callau_2011] measure how much of a dynamic language's dynamism is used in
practice, finding far less than the language permits.

**The consistent result is that specified capability over-predicts exercised capability**, which is exactly
the gap between $C_{\mathrm{est}}$ and $C_{\mathrm{act}}$ above. The present measurement is a small instance
of a well-replicated finding, and its only novelty is that the gap was sitting inside a backlog estimate
rather than inside a language feature.

### Most bytecodes do NOT bake offsets, which is why this result is unusual

**The comparison that explains the finding is with other bytecode formats.** The
[Java Virtual Machine][ref_jvm_spec] resolves a field access through a symbolic constant-pool reference:
`getfield` names a class, a field and a descriptor, and the offset is computed at run time on first use. The
[Common Language Infrastructure][ref_ecma335] does the same through a metadata token. **In both, layout is
deliberately not fixed by the format**, which buys version tolerance across independently compiled
assemblies and obliges every implementation to resolve, cache and specialise.

The [WebAssembly garbage-collection proposal][ref_wasm_gc] takes the middle position, declaring struct and
array types in the module so that field indices are static while the physical layout stays the engine's
choice. **That position follows from the format's stated design goals**, which
[Haas and others 2017][research_haas_2017] set out as hardware independence together with fast validation,
and a format that fixed byte offsets would forfeit the first to obtain something the engine can supply
anyway.

**Keleusma sits at the far end, with the byte offset in the instruction.** That forecloses independent
recompilation of a dependency, which is a real cost paid elsewhere in the design, and it is exactly why the
backend inherits arithmetic rather than resolution. **The finding of this article is a consequence of that
trade, not a discovery about aggregates in general.**

The same trade appears outside compilers whenever access must be cheap.
[FlatBuffers][ref_flatbuffers] and [Cap'n Proto][ref_capnproto] compute field offsets when the schema is
compiled so that reading a message is pointer arithmetic with no parse step, and the
[Apache Arrow columnar format][ref_arrow] fixes buffer layout in the specification for the same reason.
**Each accepts a rigid layout to make access mechanical**, which is the trade this compiler made and then
did not trace to its own backend for two releases.

### The layout rules the backend does not have to invent

Where layout is *not* predetermined, it is the ABI's problem, and the relevant documents are substantial:
[System V AMD64][ref_sysv_amd64] classifies aggregates recursively to decide register versus memory passing,
[AAPCS64][ref_aapcs64] defines homogeneous aggregate rules, and the
[Itanium C++ ABI][ref_itanium_cxx_abi] specifies object layout including base-class packing. A language may
also expose the decision to the programmer, as the [Rust Reference][ref_rust_layout] does with its
representation attributes.

**None of that reaches this backend**, because aggregates here never cross a foreign boundary as aggregates
, since they are bytes in a region and the boundary sees a pointer. That immunity is worth stating because it
ends the moment the foreign-linkage work begins, where an exported entry point taking a struct by value
would face every one of these rules at once.

**Refusing, and not approximating, is the position the verification tradition requires.**
[Necula 1997][research_necula_1997] formalises proof-carrying code and
[Leroy 2009][research_leroy_2009_cacm] establishes verified compilation; under either stance a backend that
guessed at an unimplemented form would emit code whose semantics were never established. **Refusal is the
correct behaviour and it is also what makes a zero-instance form free to skip.**

**On estimation itself**, the software-engineering literature has documented the anchoring failure this
article instantiates. [Jørgensen 2004][research_jorgensen_2004] reviews expert estimation of software
development effort and finds systematic optimism together with strong anchoring on framing,
[Jørgensen and Grimstad 2011][research_jorgensen_grimstad_2011] show irrelevant and misleading information
shifting estimates directly, and [Jørgensen and Shepperd 2007][research_jorgensen_shepperd_2007] survey the
cost-estimation field as a whole. The underlying mechanism is
[Tversky and Kahneman 1974][research_tversky_kahneman_1974], whose anchoring-and-adjustment account predicts
that an initial value dominates a final estimate even when the anchor is uninformative.

**The present case is anchoring on a category name**, the cheapest possible frame and the one least likely
to be recognised as a frame at all. It is also the rare case where the anchor is **removable by counting**,
since the category decomposes into forms and the forms can be tallied. **That is the practical contribution:
not a better estimate, but an instrument that dissolves the anchor instead of adjusting from it.**

**What the survey shows.** The literature explains why the estimate was wrong and does not contain the
measurement that corrects it, because the measurement is specific to one corpus and one instruction set.
**The transferable part is the method rather than the number.** Classify the instances by the form that
decides implementation cost, and count.

## The Source Base

The instrument is a test in the detached `native_codegen` package. It compiles every `.kel` source in the
example corpus and the self-hosted compiler's stages, discards any that fail to compile, walks every chunk's
instruction sequence and classifies each aggregate operation by the variant of its baked operand. It reports
rather than asserts, because the distribution is a fact about the corpus and not about the code.

## Epistemic State

**Measured, and reproducible from the instrument.** The corpus contains 331 aggregate operations, being 239
`NewComposite::Flat`, 41 `GetTupleField::Flat`, 29 `IsEnum`, 14 `GetIndex::Flat`, 4 `GetEnumField::Flat`, 2
`GetField::Flat` and 2 `GetTupleField::FlatNested`. By form that is 300 flat, 2 nested and **0 boxed**.
Constructed bodies range from 8 to 64 bytes with a median of 24, from 1 to 5 values with a median of 3.
Aggregates block 34.5 percent of the corpus at the module level, established in the previous article.

**Derived, and checkable from the definitions.** That a flat access is an address computation and a typed
load, since its operand is a compile-time byte offset and a scalar kind. That a nested access needs no copy,
since the representation is contiguous and a child body is a sub-range of its parent. That the backend
already implements the same address-plus-constant-offset access for the data segment.

**Verified, and the defect rate is now a series-level observation rather than an incident.** All 26 research
identifiers were resolved against the registry. **Seven needed correction before publication**, a rate of
26.9 percent as first drafted. Two carried the ACM placeholder prefix `10.5555`, which never resolves, and they
were **dropped and not replaced with invented identifiers**, one substituted by a work making the same
point that is registered. One cited the wrong journal volume. Four resolved to **different papers in the
same proceedings**, differing from the correct identifier by one or two digits in the article suffix.

**That last class is the dangerous one and it now dominates.** A neighbouring identifier in the same
volume resolves cleanly, returns a plausible compiler paper, and is wrong. It cannot be caught by checking
that a link works, only by comparing the resolved title against the cited one, which is what the project's
verification script exists to do.

**Across the three articles in this series the rates are 0 of 35, 4 of 27 and 7 of 26**, and the trend
tracks the age and proceedings-density of the bibliography rather than anything about care taken. **Searching
the registry by title is the only reliable method**, and every correction here was obtained that way.

**Corrected during writing, and left visible.** This article first priced aggregate construction as
machine-stack growth, bounded it at 15,296 bytes, and warned that it could enlarge the native machine
frame. **The figure it compared that bound against has since been retracted by the previous article**, whose
frame measurements were taken on code the optimiser had never seen. **The design was wrong, not the arithmetic.** The
language's memory model is a fixed-size arena with countable bytes, the interpreter allocates composite
bodies there, and `byte_size` is documented as the allocation the worst-case-memory pass sums. Arena-allocated
bodies therefore carry an existing bound instead of creating a new unbounded quantity. **A backend that
reached for the machine stack because it was nearer would have converted a bounded quantity into an
unbounded one for no benefit.**

**Assumed, and marked as such.** That structural similarity to implemented operations implies comparable
cost. **This inference has failed in this series before**, when a string constant was judged cheap on the
same grounds and proved to require a whole representation decision.

**What this article does not establish.** The cost in time of any of the terms. Where an aggregate body
lives when it outlives its constructing call, which is an arena question the previous article's findings make
more delicate rather than less. Whether the two nested instances sit in otherwise-unblocked modules.
Whether a future program uses the boxed form.

**The strongest claim the evidence supports** is that the dominant term of the standing estimate has zero
instances in this corpus and can be refused at no cost to coverage. **The weakest link is the cost inference**,
which rests on similarity rather than measurement, and a reader should treat the conclusion as a
redirection of expectations and not as a schedule.

## Out of Scope

The design of the aggregate lowering, which this article scopes and does not specify. Where bodies live
across calls and suspensions. The size of the native machine frame, which the [previous article][related_post_a371] measures and which
aggregate lowering does not change once bodies are arena-allocated. Garbage collection, which this language does not have. The layout decisions themselves, which
happen three passes earlier and are not the backend's to make.

## Conclusion

An item was carried as the largest remaining piece of work because its name denotes something large. The
name is accurate and the work is not, and the distance between them was a twenty-minute measurement nobody
had taken.

The dominant term is empty. What remains is address arithmetic over compile-time constants, discriminant
comparison, and an arena bump for bodies that are three values in twenty-four bytes on average, against a
region whose size the compiler already proves.

**The generalisation is not that aggregates are cheap.** It is that a decision made upstream leaves a residue
that keeps the original name, and an estimate anchored on the name measures the problem somebody else already
solved.

## References

### Reference

- [LLVM Language Reference][ref_llvm_langref]
- [LLVM `getelementptr` FAQ][ref_llvm_gep]

[ref_llvm_gep]: https://llvm.org/docs/GetElementPtr.html
[ref_llvm_langref]: https://llvm.org/docs/LangRef.html
[ref_llvm_perf_tips]: https://llvm.org/docs/Frontend/PerformanceTips.html

### Reference, aggregate layout in application binary interfaces

- [System V Application Binary Interface, AMD64 Architecture Processor Supplement][ref_sysv_amd64]
- [Arm Architecture Procedure Call Standard for the Arm 64-bit Architecture][ref_aapcs64]
- [Itanium C++ ABI][ref_itanium_cxx_abi]
- [The Rust Reference, Type Layout][ref_rust_layout]

[ref_aapcs64]: https://github.com/ARM-software/abi-aa
[ref_itanium_cxx_abi]: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
[ref_rust_layout]: https://doc.rust-lang.org/reference/type-layout.html
[ref_sysv_amd64]: https://gitlab.com/x86-psABIs/x86-64-ABI

### Reference, aggregate access in bytecode formats

- [Oracle Java Virtual Machine Specification][ref_jvm_spec]
- [ECMA-335, Common Language Infrastructure][ref_ecma335]
- [WebAssembly Garbage Collection Proposal][ref_wasm_gc]

[ref_ecma335]: https://www.ecma-international.org/publications-and-standards/standards/ecma-335/
[ref_jvm_spec]: https://docs.oracle.com/javase/specs/jvms/se21/html/index.html
[ref_wasm_gc]: https://github.com/WebAssembly/gc

### Reference, precomputed layout outside compilers

- [FlatBuffers][ref_flatbuffers]
- [Cap'n Proto][ref_capnproto]
- [Apache Arrow Columnar Format][ref_arrow]

[ref_arrow]: https://arrow.apache.org/docs/format/Columnar.html
[ref_capnproto]: https://capnproto.org/
[ref_flatbuffers]: https://flatbuffers.dev/

### Related Post

- [Related Post, Keleusma Research Spike, Blocking Frequency as the Ordering Principle for Instruction-Set Coverage][related_post_a369]
- [Related Post, Keleusma Research Spike, When an Apparent Design Wart Is a Semantic Boundary][related_post_a370]
- [Related Post, Keleusma Research Spike, What a Verified Bound Says About the Code That Actually Runs][related_post_a371]

[related_post_a369]: {% post_url 2026-08-06-native_lowering_coverage %}
[related_post_a370]: {% post_url 2026-08-07-two_calling_conventions %}
[related_post_a371]: {% post_url 2026-08-08-do_proven_bounds_survive_compilation %}

### Research

- [A polymorphic record calculus and its compilation][research_ohori_1995]
- [A review of studies on expert estimation of software development effort][research_jorgensen_2004]
- [A systematic review of software development cost estimation studies][research_jorgensen_shepperd_2007]
- [A type-based compiler for Standard ML][research_shao_appel_1995]
- [Adoption and use of Java generics][research_parnin_2013]
- [An analysis of the dynamic behavior of JavaScript programs][research_richards_2010]
- [An Empirical Study of Analogy-based Software Effort Estimation][research_walkerden_jeffery_1999]
- [Automatic pool allocation: improving performance by controlling data structure layout in the heap][research_lattner_adve_2005]
- [Bringing the web up to speed with WebAssembly][research_haas_2017]
- [Cache-conscious structure definition][research_chilimbi_def_1999]
- [Cache-conscious structure layout][research_chilimbi_layout_1999]
- [Compiling polymorphism using intensional type analysis][research_harper_morrisett_1995]
- [Estimating software project effort using analogies][research_shepperd_schofield_1997]
- [Flexible representation analysis][research_shao_1997]
- [Formal verification of a realistic compiler][research_leroy_2009_cacm]
- [Formally optimal boxing][research_henglein_1994]
- [From System F to typed assembly language][research_morrisett_1999]
- [How developers use the dynamic features of programming languages][research_callau_2011]
- [Judgment under uncertainty: heuristics and biases][research_tversky_kahneman_1974]
- [Mining billions of AST nodes to study actual and potential usage of Java language features][research_dyer_2014]
- [Modern Compiler Implementation in ML][research_appel_1998]
- [Proof-carrying code][research_necula_1997]
- [Scope and Impact of Financial Conflicts of Interest in Biomedical Research][research_bekelman_2003]
- [Space and time-efficient memory layout for multiple inheritance][research_gil_sweeney_1999]
- [The direct cost of virtual function calls in C++][research_driesen_holzle_1996]
- [The impact of irrelevant and misleading information on software development effort estimates][research_jorgensen_grimstad_2011]
- [The spineless tagless G-machine][research_pj_salkild_1989]
- [TIL: a type-directed optimizing compiler for ML][research_tarditi_1996]
- [Two-directional record layout for multiple inheritance][research_pugh_weddell_1990]
- [Unboxed objects and polymorphic typing][research_leroy_1992]
- [Unboxed values as first class citizens in a non-strict functional language][research_pj_launchbury_1991]

[research_appel_1998]: https://doi.org/10.1017/CBO9780511811449
[research_bekelman_2003]: https://doi.org/10.1001/jama.289.4.454
[research_callau_2011]: https://doi.org/10.1145/1985441.1985448
[research_chilimbi_def_1999]: https://doi.org/10.1145/301618.301635
[research_chilimbi_layout_1999]: https://doi.org/10.1145/301618.301633
[research_driesen_holzle_1996]: https://doi.org/10.1145/236337.236369
[research_dyer_2014]: https://doi.org/10.1145/2568225.2568295
[research_gil_sweeney_1999]: https://doi.org/10.1145/320385.320408
[research_haas_2017]: https://doi.org/10.1145/3062341.3062363
[research_harper_morrisett_1995]: https://doi.org/10.1145/199448.199475
[research_henglein_1994]: https://doi.org/10.1145/174675.177874
[research_jorgensen_2004]: https://doi.org/10.1016/s0164-1212(02)00156-5
[research_jorgensen_grimstad_2011]: https://doi.org/10.1109/TSE.2010.78
[research_jorgensen_shepperd_2007]: https://doi.org/10.1109/TSE.2007.256943
[research_lattner_adve_2005]: https://doi.org/10.1145/1065010.1065027
[research_leroy_1992]: https://doi.org/10.1145/143165.143205
[research_leroy_2009_cacm]: https://doi.org/10.1145/1538788.1538814
[research_morrisett_1999]: https://doi.org/10.1145/319301.319345
[research_necula_1997]: https://doi.org/10.1145/263699.263712
[research_ohori_1995]: https://doi.org/10.1145/218570.218572
[research_parnin_2013]: https://doi.org/10.1007/s10664-012-9236-6
[research_pj_launchbury_1991]: https://doi.org/10.1007/3540543961_30
[research_pj_salkild_1989]: https://doi.org/10.1145/99370.99385
[research_pugh_weddell_1990]: https://doi.org/10.1145/93548.93556
[research_richards_2010]: https://doi.org/10.1145/1806596.1806598
[research_shao_1997]: https://doi.org/10.1145/258949.258958
[research_shao_appel_1995]: https://doi.org/10.1145/207110.207123
[research_shepperd_schofield_1997]: https://doi.org/10.1109/32.637387
[research_tarditi_1996]: https://doi.org/10.1145/231379.231414
[research_tversky_kahneman_1974]: https://doi.org/10.1126/science.185.4157.1124
[research_walkerden_jeffery_1999]: https://doi.org/10.1023/a:1009872202035