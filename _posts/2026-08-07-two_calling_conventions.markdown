---
layout: post
mathjax: true
comments: true
title: "Two Ways of Doing One Thing: When an Apparent Design Wart Is a Semantic Boundary"
date: 2026-08-07 09:00:00 +0000
categories: engineering compilers verification
series: keleusma_native
series_title: Keleusma Native Code Generation
series_index: 2
---
<!-- A370 -->
<script>console.log("A370");</script>

**A system had grown two ways of doing what looked like one thing. The obvious move was to tidy them into one. The tidying turns out to be impossible, and the reason it is impossible is the reason the two ways exist.**

**The argument that settles it needs no specialist knowledge and fits in a sentence.** One of the two cases
has two things to report and only one slot to report them in. Whichever thing the slot is given, the other
is lost. The other case has only one thing to report, so the single slot is exactly enough.
**That is a counting argument, it is decided before any code is written, and it is not the argument an engineer reaches for by default.**

The engineer's instinct is to look at the cases and ask whether they resemble one another. They did.
**Every one of the nine measured occurrences had exactly the shape that invited the tidy-up**, and the
measurement encouraged precisely the wrong conclusion. The resemblance was real and it was irrelevant,
because the defect was never in the instances. **It was in the interface they would have had to share.**

**This article is about that distinction**, which is between evidence about members of a class and evidence
about the channel the class must pass through. The second dominates the first and is cheaper to check.

The article reports the measurement, the way the measurement pointed the wrong direction, and the argument
that settled it. It also reports a rule this author shipped one increment earlier which turns out to be
**stricter than the property it enforces**, excluding ten of twenty-four cases for no reason. No test found
that. It surfaced while gathering data for this article.

### How to read this

**The general argument is in the opening, in the section called The Argument That Settled It, and in Pattern Extraction. Those three need nothing but attention.**
The sections between them work the argument through a real case with real numbers, and they use the
vocabulary of the trade. Every term is glossed at first use, but a reader who wants the result and not the
machinery can take those three and stop.

**The mathematics is optional throughout.** It appears because the central result is a counting argument,
and counting arguments are the one place where a line of notation settles what a paragraph of prose can only
assert. Wherever notation appears, the sentence before it says the same thing in words.

### What this is a case study of

The setting is compiler design, and specifically the part of a compiler called the **backend**, which is the
stage that turns a program the compiler has already understood into instructions a processor can run. The
project is Keleusma, whose backend is described in the [previous article in this series][related_post_a369].
**No compiler background is required.** The shape of the problem is a general one. A system offers one
abstraction whose instances divide into two classes with genuinely different observable behaviour, and an
engineer, seeing two implementations, tries to collapse them.

The question this article treats is when that instinct is right and when it is a category error. The answer
offered is a test, and it is this.
**Count the observable events each class produces, and count the channels the proposed unification provides.**
If the counts differ, the unification is lossy and no amount of shape analysis on individual instances will
rescue it, because the loss lives in the interface and not in the instances.

**The instinct to unify is not a bad one.** Two ways of doing one thing is a real cost, paid by every
consumer who must learn both and by every future change that must be made twice. This article does not argue
against tidiness. It argues that tidiness is a claim about the world, and like any other claim it can be
checked before it is acted on, cheaply, and that the check is not the one an engineer reaches for by
default.

## The Setting

A **coroutine** is a computation that can suspend in the middle, hand a value to whoever called it, and
later be resumed with a value handed back.
**The two-flavour split this article is about is not peculiar to Keleusma**, and the language specifications
record it plainly. Python began with generators that only produce values in
[Python Enhancement Proposal 255][ref_pep255] , or PEP 255, and later admitted values back in at the
suspension point in [PEP 342][ref_pep342], which is exactly the step that turns one observable event into
two, then separated the coroutine from the generator entirely in [PEP 492][ref_pep492]. [Lua][ref_lua54]
exposes asymmetric coroutines in which `resume` and `yield` are distinct operations and a coroutine
additionally **returns** when its body completes, so that a caller must distinguish a yield from a return.
The [European Computer Manufacturers Association standard 262][ref_ecma262], or ECMA-262, which specifies
JavaScript, gives its generator results an explicit `done` flag for the same reason,
[C# iterators][ref_ecma334] make the distinction syntactic, and [C++][ref_cpp_coroutines] separates
`co_yield` from `co_return` at the level of the grammar.
**Every one of these designs carries a discriminator**, and that is the fact this article rediscovers from
the compiler side.

Keleusma has two forms.

A **`yield` function** suspends a bounded number of times and then finishes. It is a total function with
interruptions. The type system guarantees it terminates.

A **`loop` function** suspends forever. It is **productively divergent**, which is the property that it
never finishes but always makes progress, so a **host**, meaning whatever program is driving the coroutine
from outside, can pull values from it indefinitely and each pull terminates. This is the language's stream
abstraction and it is the normal way a Keleusma program does work over time.

Both are written with the same `yield` keyword in the body. The difference is the declaration, and the type
checker already separates them into different categories with different rules about what may call what.

### Notation

**The formal machinery below is worth the six symbols it costs, because the central result is a cardinality argument that prose states as an opinion and arithmetic settles in one line.**
A reader who prefers prose can take the following and skip to the results.
**A terminating coroutine emits two values per call and a return slot holds one.**

Let $W$ denote the machine word type, so that $\lvert W \rvert = 2^{64}$ on the present target. Let $K$
denote the set of coroutine **chunks**, a chunk being one compiled unit of code, partitioned by the type
checker into

$$K = K_\Sigma \;\sqcup\; K_\Upsilon$$

where $K_\Sigma$ are the divergent stream chunks and $K_\Upsilon$ the terminating ones. Write $\lvert
K_\Sigma \rvert = 24$ and $\lvert K_\Upsilon \rvert = 1$ for the present corpus.

An execution of a chunk is driven by an initial argument $a \in W$ and a sequence of resume values $\vec{r}
= (r_1, r_2, \ldots)$. It produces an **observable trace**, a sequence over the alphabet $\{\mathsf{Y}(v),
\mathsf{F}(w)\}$ in which $\mathsf{Y}$ marks a suspension carrying $v$ and $\mathsf{F}$ a completion
carrying $w$. For a terminating chunk with $n$ suspensions the trace is finite and ends in a completion,

$$\mathcal{T}_\Upsilon(k, a, \vec{r}) \;=\; \bigl\langle\, \mathsf{Y}(v_1),\, \mathsf{Y}(v_2),\, \ldots,\, \mathsf{Y}(v_n),\, \mathsf{F}(w) \,\bigr\rangle$$

while for a divergent chunk it is infinite and contains no completion at all,

$$\mathcal{T}_\Sigma(k, a, \vec{r}) \;=\; \bigl\langle\, \mathsf{Y}(v_0),\, \mathsf{Y}(v_1),\, \mathsf{Y}(v_2),\, \ldots \,\bigr\rangle.$$

**That asymmetry is the entire article.** The two trace shapes differ not in length but in **alphabet**. One
uses both letters and the other uses one.

A **calling convention** is an encoding $\varepsilon$ that carries a trace into what a host can observe from
native calls. Write $\mathrm{chan}(\varepsilon)$ for the number of distinguishable $W$-valued channels a
single native call exposes under $\varepsilon$, and $\mathrm{obs}(k)$ for the number of distinct observable
values a single call of $k$ must convey.

### The two conventions

The generator emits native code that a host program calls. When the generated code suspends, the value has
to reach the host. Two mechanisms are available.

The **callback convention** declares an external function, here called `kel_yield`, that takes the yielded
value and returns the resume value. Generated code calls it at each suspension point and carries on. The
host implements it. Control passes to the host and back without the generated function returning, so the
generated function's **stack frame** stays live throughout, a stack frame being the scratch space a function
reserves for its own working values and gives back when it returns. This is the stackful shape, of which the
context-switching functions of the [Portable Operating System Interface][ref_posix_ucontext] or POSIX are
the oldest standardised instance, and its defining property is exactly that a frame outlives the suspension.

The **return convention** ends the native call at the suspension. The yielded value is the function's return
value. The host receives it as an ordinary result, does whatever it does, and calls the function again with
the resume value as an argument. No frame persists between suspensions.

The return convention is strictly cheaper. It needs no external symbol, no callback indirection, and
crucially **no stack frame alive during host code**, which matters to a project whose entire premise is
statically bounded memory. A frame held across an arbitrary amount of host activity is a frame the memory
analysis cannot account for.

**The compiler infrastructure this backend targets already names both shapes.** The coroutine intrinsics of
[the Low Level Virtual Machine compiler infrastructure][ref_llvm_coroutines] or LLVM provide a switch-resume
family, in which a coroutine handle is resumed through a function pointer and the frame persists in an
explicit allocation, and a **returned-continuation** family, `llvm.coro.id.retcon`, in which the coroutine
returns at each suspension and hands back a continuation to be called next. The two families correspond
closely to the callback and return conventions described here. Frame liveness across a suspension is the
same property that [LLVM stack maps][ref_llvm_stackmaps] exist to describe, and the
[WebAssembly stack-switching proposal][ref_wasm_stack_switching] is the same design question posed for a
portable target. **None of these settle the choice**, and that is worth saying, because they establish that
both shapes are standard and that the trade is real, not that either is correct here.

### How the backend arrived at two

The `yield` function was implemented first, on the callback convention, because it is the general mechanism
and it was obviously correct.

The `loop` function was implemented later. Its **bytecode**, meaning the compact intermediate instructions
the compiler produces before machine code, has a recognisable shape, being an opening marker, a body, a
stack cleanup, and a reset instruction that rewinds execution to just after the marker and hands control to
the host. The reset clears every local variable. **That clearing is the key structural fact.** If the body's
suspension is the last thing on every path, then no local outlives the suspension, because the reset would
have cleared it anyway. Nothing needs to persist, so nothing needs a frame, so the return convention
applies.

Two conventions resulted, not by design but by two increments arriving from different directions. That is
exactly the situation in which an engineer reaches for a unification.

## The Measurement That Pointed The Wrong Way

Before proposing anything, the corpus was measured. The instrument walks every compiled program in the
project's shipped examples and self-hosted compiler sources, classifies each coroutine chunk, and reports
the distribution.

### The distribution of stream chunks

| Class | Count |
|---|---|
| Single suspension, at the end of the body | 22 |
| Multiple suspensions at the top level | **0** |
| Suspensions nested inside conditionals | 1 |
| No suspension of its own, delegating to a callee | 1 |
| **Total stream chunks** | **24** |

The zero is worth pausing on. An earlier design in this project assumed the general case was a body with
several suspension points that would need to be reordered relative to one another.
**No such body exists in the corpus.** That design was specified in some detail before the count was taken,
and the count deleted it.

The nested case looked like the hard one until it was measured per suspension instead of per chunk. All
nineteen of its suspensions sit inside conditionals and **not one sits inside a loop**. A suspension inside
a conditional is a control-flow join, where every path still suspends once and ends. A suspension inside a
loop crosses a back edge and genuinely needs a frame. The word **nested** had been covering both, and they
have entirely different costs.

### The distribution of terminating coroutines

| Property | Count |
|---|---|
| `yield` function chunks in the whole corpus | **1** |
| ... whose every suspension is immediately followed by a return | **1** |

One. The entire terminating-coroutine population of the corpus is a single chunk, and that chunk has, in
nine of nine cases, precisely the shape that appeared to invite the return convention, which is to suspend
and then return.

**This is where the measurement pointed the wrong way.** A distribution of nine out of nine looks like an
invitation. It reads as evidence that the shape is natural, that the callback is an accident of
implementation order, and that a unification is available at the cost of a shape check. The author of this
article drafted exactly that plan.

## The Argument That Settled It

The plan was checked against the smallest possible instance before it was implemented, which is the only
thing in this article that went right on the first attempt.

Consider a terminating coroutine that suspends once with its argument.

```
yield main(a: Word) -> Word { yield a }
```

It compiles to three instructions, which load the argument, suspend, and return. The suspension instruction
pops the value to yield and pushes the value the host resumes with, so the return instruction returns the
resume value.

Run it on the reference virtual machine and it produces **two observable events**.

1. **Suspension**, carrying `a`, the yielded value. 2. **Completion**, carrying `r`, the resume value.

A return-based **lowering**, meaning a translation from the intermediate form down to machine code, has
**one** return slot. Give the slot the yielded value and the completion is gone. Give it the completion and
the suspension is gone. There is no third option, and **no analysis of the chunk's shape changes this**,
because the deficiency is in the calling convention and not in the chunk.

**The obvious objection is that the completion could arrive on a second call, and the reason it cannot is the part of the return convention that is easiest to skip over.**
The convention has no resumption point. The host drives the chunk by calling a plain function again, passing
the resume value as the argument, so the sequence the host executes is

$$f(a) = v_0, \qquad f(r_1) = v_1, \qquad f(r_2) = v_2, \qquad \ldots$$

**and $f$ carries nothing between calls.** For a divergent chunk that is exactly right, because the reset
instruction rewinds to the same place and clears every local, so re-entering from the top is what resumption
means there. **For a terminating chunk it is wrong.** A second call re-runs the body from the beginning and
suspends again, so it yields a second time and never reaches the completion at all.

**Everything the host will ever learn about one terminating execution therefore has to arrive from the first call**,
which is why the budget is one slot rather than one slot per event.

### The counting argument, stated once

Under the return convention a single native call exposes exactly the return **register**, which is one of
the processor's few named storage slots, so $\mathrm{chan}(\varepsilon_{\mathrm{ret}}) = 1$. The chunk above
must convey both $v$ and $w$ from one call, so $\mathrm{obs}(k) = 2$. An encoding faithful to the trace must
therefore be an injection

$$\varepsilon_{\mathrm{ret}} : W \times W \;\longrightarrow\; W$$

and no such injection exists whenever $\lvert W \rvert \ge 2$, by cardinality,

$$\lvert W \times W \rvert \;=\; \lvert W \rvert^{2} \;=\; 2^{128} \;>\; 2^{64} \;=\; \lvert W \rvert.$$

**The same statement in bits is the one that generalises**, and it is the elementary case of the
channel-capacity argument [Shannon 1948][research_shannon_1948] introduced. An interface of $m$ machine
words carries $64m$ bits and a trace of $k$ words needs $64k$, so a faithful encoding requires

$$64k \;\le\; 64m \qquad \Longleftrightarrow \qquad k \;\le\; m,$$

and here $k = 2$ against $m = 1$. **The shortfall is 64 bits**, which is to say a whole second word.

The general statement is immediate. For any chunk $k$ and convention $\varepsilon$,

$$\mathrm{obs}(k) \;>\; \mathrm{chan}(\varepsilon) \quad\Longrightarrow\quad \varepsilon \text{ is not injective on } \mathcal{T}(k),$$

and a non-injective encoding is one in which two distinct executions become indistinguishable to the host,
which is precisely what it means for a lowering to be wrong.

**The deficit does not grow with the number of suspensions, which deserves a check and not an assumption.**
A terminating chunk with $n$ suspensions emits $n$ yielded values and one completion, so its trace carries
$n+1$ words and the executions it can distinguish number $\lvert W \rvert^{\,n+1}$. The single call it is
granted distinguishes $\lvert W \rvert$ of them, so the collapse factor is

$$\frac{\lvert W \rvert^{\,n+1}}{\lvert W \rvert} \;=\; \lvert W \rvert^{\,n},$$

which is catastrophic at every $n$ and no worse in kind at $n = 9$ than at $n = 1$.
**The smallest instance was therefore the right one to check**, and checking a larger one would have added
nothing.

**The pigeonhole is doing all of the work**, and it is worth noticing how little it needs. It does not
inspect the body, the number of suspensions, the control flow, or the corpus. It needs the alphabet of the
trace and the width of the interface, both of which are known before any code is written.

### The claim is false in its strong form, and the reference work is what showed it

**A return slot is not one word.** The [System V AMD64 application binary interface][ref_sysv_amd64] , or
ABI, which is the document that fixes how functions pass arguments and return results on a given machine,
returns a two-eightbyte aggregate in the register pair `RAX:RDX`, and [AAPCS64][ref_aapcs64] returns small
aggregates in `X0` and `X1`. So $\mathrm{chan}(\varepsilon_{\mathrm{ret}})$ is a property of the chosen
signature rather than a constant of the machine, and the honest statement is conditional.

$$\mathrm{chan}(\varepsilon_{\mathrm{ret}}) = 1 \;\text{ if the return type is } W, \qquad \mathrm{chan}(\varepsilon_{\mathrm{ret}}) = 2 \;\text{ if it is } W \times W.$$

Under a two-word return the injection $\varepsilon : W \times W \to W \times W$ exists trivially, and the
unification this article rejects becomes **representable**.

**Two designs are being run together here and they cost very different amounts, so they are worth separating.**
Cramming both events into one call needs the pair $W \times W$, which is 128 bits against 64,
**a shortfall of a whole word**. Making the convention re-entrant with a discriminator needs only

$$\lvert \{\mathsf{Y}, \mathsf{F}\} \times W \rvert \;=\; 2 \cdot 2^{64} \;=\; 2^{65},$$

**a shortfall of exactly one bit.** That single bit is what forces a second register, since $\lceil 65 / 64
\rceil = 2$, and it is the whole reason the register-pair rules in the two application binary interfaces
matter to this decision.
**The expensive-sounding option costs one bit of information and one register of encoding**, a very
different proposition from carrying a second word. The pigeonhole refutes the unification *at the signature
the backend currently emits*, not for all time.

That distinction matters and it was not visible from inside the problem. It surfaces a **third option** ,
which is to widen every coroutine entry point so that it returns a discriminated pair,

$$f : W \longrightarrow (\,\mathsf{tag} \in \{\mathsf{Y}, \mathsf{F}\},\; W\,)$$

so that one convention carries both trace alphabets.

**That form is sufficient only for a coroutine that suspends at most once per call, and the article as
published did not say so.**
A coroutine resumes at the point it suspended, which is the defining property of the construct. Under the
callback convention that is free, because the native function never returned and its frame, program counter
and locals are all still live. Under a return convention the call has ended and nothing survives. For the
divergent form that costs nothing, since the reset instruction clears every local and the next iteration
legitimately starts from the top. **For the terminating form it is fatal**, because the next call must
resume mid-body and a function entered at its entry point cannot do that.

A widened return must therefore carry, beyond the value and the tag, something identifying where to resume
and with what state. That is a continuation, and it is what
[`llvm.coro.id.retcon`][ref_llvm_coroutines] returns alongside the yielded value. The
returned-continuation family exists because returning a value at a suspension is not sufficient on its own.
The general interface is a triple,

$$f : W \longrightarrow (\,\mathsf{tag} \in \{\mathsf{Y}, \mathsf{F}\},\; W,\; \mathsf{cont}\,)$$

and the continuation implies an allocation for the saved frame whose lifetime spans host execution, which is
the very property this option was credited with preserving.

The cost is therefore that every call of every coroutine pays a wider return and a host-side discrimination,
including the **95.83 percent** of the corpus, twenty-three chunks of twenty-four, that need only one
letter, and that the terminating form pays a frame as well.
**The 95.83 percent is a count of chunks needing one letter and must not be read as the fraction for which a
pair suffices**, because that is a claim about the terminating form and the corpus holds one instance of
it.

**Whether that is cheaper than two conventions is an empirical question this article does not answer, and the shape of the comparison can be stated without measuring anything.**
Writing $c_{\mathrm{tag}}$ for the per-call cost of the discriminator, $c_{\mathrm{frame}}$ for the
amortised cost of allocating and reclaiming the saved frame, and $c_{\mathrm{meta}}$ for the one-off cost
of declaring and dispatching two conventions, the totals over $N$ calls are

$$C_{\mathrm{one}} = (c_{\mathrm{tag}} + c_{\mathrm{frame}}) N, \qquad C_{\mathrm{two}} = c_{\mathrm{meta}},$$

where $c_{\mathrm{frame}} = 0$ only for coroutines that suspend at most once per call, so the widened
return is cheaper only below

$$N^{*} \;=\; \frac{c_{\mathrm{meta}}}{c_{\mathrm{tag}} + c_{\mathrm{frame}}}.$$

**The frame term moves the crossover down**, which strengthens rather than weakens the observation that
follows.

**A per-call term always loses to a constant eventually**, and a stream abstraction exists to be called many
times, so the crossover is the whole question.
**Neither constant is published and this article declines to invent them**, which is why the recommendation
below rests on the memory property and not on a cost model.

**Two production language runtimes already do exactly this**, which is the strongest argument available that
the option is practical rather than merely representable. A [Kotlin][ref_kotlin_coroutines] suspending
function returns its ordinary result, or a distinguished `COROUTINE_SUSPENDED` sentinel to signal that it
suspended instead. That is a discriminated return in the narrowest possible encoding, a single reserved
value carved out of the result type. A [Rust][ref_rust_reference] future's `poll` returns `Poll::Ready(T)`
or `Poll::Pending`, which is the same discrimination made explicit in the type rather than hidden in a
sentinel. Both carry the completion and the suspension through one interface, and both pay the tag on every
call.

**The sentinel form has a hazard the tagged form does not**, and it is worth naming because the narrow
encoding is the tempting one here. Carving a reserved value out of $W$ shrinks the value space to

$$\lvert W \rvert - 1 \;=\; 2^{64} - 1 \;=\; 18{,}446{,}744{,}073{,}709{,}551{,}615,$$

which is 18,446,744,073,709,551,615 usable values, a loss of $2^{-64}$ or about $5.421 \times 10^{-20}$ of
the space, and any program able to produce the reserved value as a legitimate yield becomes unrepresentable.
**The loss is negligible in measure and total in reachability, and only the second of those matters.** A
sentinel is available exactly when the yielded type is a proper subset of $W$ missing at least one element,
a statement about the type and not about how unlikely the value is. Kotlin can afford it because the
sentinel is a reference no user value aliases. A backend whose yielded values are arbitrary machine words
cannot, so for Keleusma the tagged pair is the honest form and the sentinel is unavailable.

**The correction is left in the text rather than folded into the argument**, because the sequence is the
useful part. A counting argument was stated in a form stronger than the evidence supported, and reading the
governing interface specification rather than assuming the register width is what caught it.

The nine-out-of-nine measurement was answering a different question than the one that mattered. It
established that the **shape** is uniform. It said nothing about the **arity of the interface**, and the
arity is what fails.

### Why the divergent case is genuinely different

A `loop` function never completes. The reset instruction rewinds and returns control to the host, so there
is no completion event at all. The count of observable events is one, the count of channels is one, and the
convention fits exactly,

$$\mathrm{obs}(k) = 1 = \mathrm{chan}(\varepsilon_{\mathrm{ret}}) \qquad \text{for all } k \in K_\Sigma \text{ admitted below,}$$

so the required encoding is $\varepsilon_{\mathrm{ret}} : W \to W$, for which the identity suffices. The
host drives the chunk by iterating the native function, and the correspondence with the virtual machine is

$$f(a) = v_0, \qquad f(r_k) = v_k \;\; (k \ge 1),$$

with **no distinguished first call**, because iteration zero consumes the call argument and iteration $k$
consumes the $k$-th resume value, exactly as the virtual machine does when it writes the resume value into
the entry chunk's parameter slot.

**So the two conventions are not an accident awaiting cleanup. They track the boundary between a construct that terminates and one that does not**,
which is a distinction the language already makes, the type checker already enforces, and the memory
analysis already depends on. The backend grew two conventions because there are two things.

### The general form of the test

Stated without reference to compilers, the test reads as follows.

> Let a proposed unification map a class of behaviours onto an interface. Count the
**distinguishable > outcomes** each behaviour can produce and count the
**distinguishable outcomes the interface can carry**. > If the first exceeds the second for any member of
the class, the unification is lossy, and evidence about > the **distribution** of members cannot rescue it.

The failure mode this catches is common, and it is
**collecting evidence about instances when the defect lives in the interface.** Nine out of nine is a fact
about instances. One slot against two events is a fact about the interface. The second dominates the first
entirely, and it is cheaper to check.

## A Rule Stricter Than The Property It Enforces

Gathering the distribution for this article surfaced a defect in code shipped one increment earlier, which
no test had caught because no test asked.

The admissibility rule for the return convention requires that between a suspension and the reset,
**nothing runs except block delimiters and a single stack-cleanup instruction**. The intent is to establish
that the resume value is discarded, since the return convention does not supply one.

Ten of the twenty-four stream chunks fail this rule. All ten are the same program shape and their tail
instruction sequence is the following.

```
PopN(1), Const(0), PopN(1)
```

The source is a body that suspends and then evaluates a trailing constant, so the constant is pushed and
immediately discarded. **The sequence has no observable effect and leaves the stack balanced.** It is
exactly as safe as the sequence the rule admits. The rule refuses it because the rule was written by
enumerating the instructions the author had seen rather than by stating the property.

Write $\delta(\iota) \in \mathbb{Z}$ for the net operand-stack effect of an instruction and
$\mathrm{eff}(\iota)$ for its set of side effects. For a tail segment $\pi$ following a suspension, the
property that actually licenses the transformation is

$$\Delta(\pi) \;=\; \sum_{\iota \in \pi} \delta(\iota) \;=\; -1 \qquad \text{and} \qquad \mathrm{eff}(\pi) \;=\; \varnothing,$$

the $-1$ recording that the segment consumes exactly the resume value the suspension pushed and nothing
else. Both candidate tails satisfy it.

$$\Delta\bigl(\langle \mathtt{PopN(1)} \rangle\bigr) = -1, \qquad \Delta\bigl(\langle \mathtt{PopN(1)},\, \mathtt{Const(0)},\, \mathtt{PopN(1)} \rangle\bigr) = -1 + 1 - 1 = -1.$$

The shipped rule instead tests membership in a fixed instruction set $A = \{\mathtt{PopN(1)}\} \cup D$, with
$D$ the block delimiters. Let $P$ denote the set of tail segments satisfying the property and $R$ the set
the rule admits. The rule is **sound but not complete**,

$$R \;\subsetneq\; P, \qquad \lvert P \setminus R \rvert \;\ge\; 10,$$

and the containment is what makes the defect a coverage loss rather than a correctness loss. The property is
**effect-free and stack-neutral**. The rule is **drawn from a list of two instructions**. Those coincide on
the corpus the rule was written against and diverge on the next ten cases, the standard failure of a
whitelist standing in for a predicate.

**A sound but incomplete rule is the normal condition of static analysis and this instance is not the normal reason for it.**
The framework of [Cousot and Cousot 1977][research_cousot_1977] exists because an exact answer is often
uncomputable, so an analysis deliberately accepts imprecision in exchange for soundness.
**The imprecision here was not forced.** The property is decidable on straight-line bytecode by summing two
integers, so nothing about the problem required an approximation, and the rule is an approximation that
nobody chose. **That is a worse position than the classical one and an easier one to fix.**

**The cost is measurable and is not correctness.** Nothing is mislowered, because the rule refuses rather
than admits. The cost is coverage. Writing $R$ for what the rule admits and $P$ for what the property
licenses,

$$\frac{\lvert R \rvert}{\lvert K_\Sigma \rvert} \;=\; \frac{14}{24} \;=\; 58.33\%, \qquad \frac{\lvert P \rvert}{\lvert K_\Sigma \rvert} \;=\; \frac{24}{24} \;=\; 100\%,$$

so **41.67 percent of the corpus is refused the cheap convention for no reason**, and ten stream chunks that
could use it currently do not. The fix is a small generalisation and it is not attempted here, because this
article's subject is the convention question and a coverage improvement inside it would be a second claim
wearing the first one's clothes.

**It is reported because it was found by writing rather than by testing**, the second time in this series
that assembling a table for publication has surfaced something a green test suite did not.

## Method

The instrument compiles every `.kel` source in the project's example directories, the self-hosted compiler
stage sources, and the standalone compiler subproject, discarding any that fail to compile. For each
resulting module it walks every chunk and classifies it.

Suspension nesting is computed with a depth counter over the block-opening instruction set, which was
checked against the full block-structured instruction list and not assumed. A missed opener would report a
nested suspension as a top-level one and admit a chunk the transformation is wrong for.

The tail-position walk **follows jumps** rather than scanning the instruction stream linearly. This is
necessary, not fastidious. The instructions textually between a deeply nested suspension and the reset
include the bodies of sibling branches, which are on different paths and never execute after that
suspension. A linear scan answers a question nobody asked.

Suspension nesting is summarised by the enclosing block stack. Writing $B(y)$ for the stack of open blocks
at suspension $y$, the distinction that matters is

$$\mathrm{join}(y) \iff \mathtt{Loop} \notin B(y),$$

a suspension that is a control-flow join rather than one crossing a back edge. For the nested chunk the
measurement is $\mathrm{join}(y)$ for all $19$ of its suspensions, at depths $\lvert B(y) \rvert$ ranging
over $2$ to $11$.

Equivalence between the two lowerings is checked by a differential oracle against the reference virtual
machine, comparing **whole sequences of yielded values** rather than final results. Writing
$\mathcal{Y}(\cdot)$ for the projection of a trace onto its suspension letters, the assertion is

$$\mathcal{Y}\bigl(\mathcal{T}^{\mathrm{vm}}(k, a, \vec{r})\bigr)_{1:n} \;=\; \mathcal{Y}\bigl(\mathcal{T}^{\mathrm{nat}}(k, a, \vec{r})\bigr)_{1:n}$$

for a caller-supplied bound $n$, over a finite sample of $\vec{r}$. A stream never produces a final result,
so a comparison of final results would be vacuous for exactly the class under study, and the truncation at
$n$ is not a weakness of the test but a consequence of the trace being infinite.

**The sample is finite and the claim is universally quantified over $\vec{r}$**, so the oracle refutes and
does not prove. The resume values in each case are chosen to differ from one another and from the argument,
and in the nested case to drive different branches on successive iterations, because a $\vec{r}$ that takes
one path every time exercises one return site and licenses nothing about the join.

### How the literature survey was assembled

The 35 hand-selected research references were chosen because a step of the argument depends on
them, and each was read. The 1,945 harvested references were not chosen that way and
were not read individually. **Stating that plainly is the point of this subsection**, because a list of four
thousand citations otherwise implies a reading it does not represent.

The harvest issued keyword queries against Crossref and the NASA technical report server across thirteen
topic clusters, being coroutines, continuations, effect handlers, calling conventions, code generation,
verified compilation, compiler testing, resource analysis, static analysis, concurrency runtimes, bytecode
virtual machines, types and semantics, and a general systems cluster. Each returned record was kept only if
its title carried a subject anchor, meaning a term specific to computing and not one shared with every
discipline. That test discarded 5,313 of the 7,334 retrieved records. Records already
cited by hand were discarded again at assembly so that no work appears twice under two anchors.

**The count that survives is smaller again.** The arithmetic is worth stating and not leaving to be noticed.
Of the records the filter admitted, 85 were duplicates holding the same title and year under two
identifiers, 2 carried a doubled word in the title where a registry had concatenated a title with a book
title, 1 was untitled or undated, and 4 duplicated a hand-selected entry. 1,945
therefore reach the reference list.

**The anchor filter is the step most likely to be wrong, and it was wrong twice before it was right.**

The first version was inherited from an article on a different subject and tested for the presence of that
subject's vocabulary, so it rejected 2,174 compiler-science titles for containing no aircraft. That failure
is loud once looked at and silent otherwise, because a filter that rejects everything reports a small corpus
rather than an error.

The second version was written for this subject and **overcorrected into uselessness**. It admitted generic
stems, being analysis, implementation, generation, evaluation, system, model, performance and interface,
each of which occurs in every discipline that publishes. It admitted 4,305 records, and a sample of them
contained rabies control, seismic depth imaging, breeding soundness examination in veterinary medicine,
supercontinuum generation in photonics, transport appraisal and fibre art.
**A survey listing those has surveyed nothing.** The larger count was the symptom rather than the
reassurance.

The version used here requires a term that is computing-specific on its own, so an ambiguous term
contributes nothing however many of them a title carries. It admits 2,021 records of the
7,334 retrieved.
**The corpus is less than half the size of the one the permissive filter produced.** That reduction is the
result rather than a cost of it.

What the harvested list therefore supports is a claim about **coverage**, being that the survey did not
select for agreement with its conclusion, since the queries were fixed before the records were seen. What it
does not support is any claim about the content of an individual harvested record beyond its title, authors,
year and venue as the registry holds them.

## Threats to Validity

**The corpus is one project's own sources.** It over-represents text processing, because the self-hosted
compiler is a text processor. A terminating-coroutine population of one is not evidence about the language.
It is evidence about this corpus at this date. A user may write many, in shapes not seen here.

**The conclusion does not depend on the corpus.** This is the important asymmetry and it is why the argument
is stated the way it is. The event-counting argument is about the calling convention and holds for a
population of one or one million. The measurement is reported because it is what pointed the wrong way, not
because the conclusion rests on it.

**The classification was written by the party proposing the unification.** The instrument that produced the
nine-out-of-nine figure and the plan that figure encouraged share an author. The mitigation offered is that
the figure is accurate and was not the thing that failed. The reasoning built on it failed, which is the
weaker position for the author and the stronger one for the reader.

**No claim is made about performance.** The return convention is argued to be cheaper on structural grounds,
meaning no external symbol, no indirection, and no frame across the suspension. None of that has been
measured. The machine-code frame sizes that would settle it are emitted only into a section of the
Executable and Linkable Format, or ELF, which this development host does not produce, so the measurement is
deferred and not done.

## Pattern Extraction

The pattern is available wherever an interface is proposed to cover a class of behaviours.

**Two implementations of one abstraction may be tracking a real boundary.** Before unifying, ask what
distinguishes the two implementations, and check whether the source domain distinguishes it too. Here the
type system already had two categories, enforced by a rule about which may call which, and the memory
analysis already depended on the distinction. The backend was not being untidy. It was reflecting something
upstream.
**The tidying instinct treats a difference as noise, and the check is whether anything else in the system treats it as signal.**

**Evidence about instances cannot repair a defect in an interface.** This is the sharper half, and the
reason is a quantifier. Admissibility of a unification is a universal claim over the class,

$$\Phi \;\equiv\; \forall b \in \mathcal{B} : \; \mathrm{obs}(b) \le \mathrm{chan}(\iota),$$

whose negation is existential,

$$\neg\Phi \;\equiv\; \exists b \in \mathcal{B} : \; \mathrm{obs}(b) > \mathrm{chan}(\iota).$$

**A single witness refutes $\Phi$, and no quantity of confirming instances establishes it.** The
nine-out-of-nine figure has the form of a frequency $\hat{p} = 9/9 = 1$ over observed shapes, and a
frequency estimates a proportion. It does not bound a maximum, and $\Phi$ is a statement about a maximum,

$$\Phi \iff \max_{b \in \mathcal{B}} \mathrm{obs}(b) \le \mathrm{chan}(\iota).$$

**The measurement is weak even taken on its own terms, and it is worth putting a number on how weak.**
Reading nine successes from nine trials as a sampling exercise, the exact one-sided lower confidence bound
of [Clopper and Pearson 1934][research_clopper_pearson_1934] on the underlying proportion at confidence $1 -
\alpha$ is

$$p_{\min} \;=\; \alpha^{1/n} \;=\; 0.05^{1/9} \;=\; 0.7169,$$

so **the observation is consistent with 28.31 percent of cases failing**, and at 99 percent confidence the
bound falls to 0.5995. A run of twenty-four would give 0.8827 and still leave 11.73 percent unexcluded, and
licensing a claim of 0.99 at the same confidence would need

$$n \;=\; \frac{\ln \alpha}{\ln 0.99} \;=\; 299$$

consecutive successes. **Nine is not a large number and the arithmetic says so.** The case of no observed
failures is the one [Hanley and Lippman-Hand 1983][research_hanley_lippmanhand_1983] treat under the heading
of whether nothing going wrong means everything is all right, where they give the same bound in its
approximate form as a rule of three.
**Their subject is clinical and the arithmetic is indifferent to that.** That is a separate and much weaker
objection than the one this section rests on, because the counting argument does not need the sample to be
small. **It would refute the unification from a sample of a million.**

A uniformity measurement over instances is genuinely useful for deciding what to build first, which is the
subject of the [previous article in this series][related_post_a369], because that question really is about
proportions. It is useless here. The two questions feel adjacent, and one of them is answerable by counting
slots.

**A whitelist standing in for a predicate coincides with it on the sample it was drawn from.** The
tail-position rule is a small instance of a large pattern. Whenever a condition is written by enumerating
the cases the author has seen, it will pass every case the author has seen. The discipline is to state the
property and then check that the enumeration matches it, in that order, because the reverse order produces a
rule that looks correct and is merely well-sampled.

**Assembling a table for an audience is a distinct verification activity.** Twice now in this series, a
figure gathered for publication has exposed something that a passing test suite did not. The mechanism is
not mysterious. A test asks a question its author thought to ask. A table forces a row for every case,
including the ones nobody thought about, and an empty or surprising cell is a question the author did not
have the imagination to ask directly.

## The Decision This Informs

The spike was commissioned to inform a choice, and it narrows rather than makes it.

**One option is ruled out on evidence.** A single return-based convention for both forms
**at a one-word return type** is lossy for the terminating form, and no shape analysis rescues it.

**Three options remain and all are genuinely open.**

**One convention with a widened return.** Every coroutine entry point returns a discriminated pair, which
the [System V AMD64][ref_sysv_amd64] and [AAPCS64][ref_aapcs64] register-pair rules make free of memory
traffic on the two targets that matter. One convention for the host and one discriminator to check.
**The frame property is preserved only for coroutines that suspend at most once per call**, and is
surrendered otherwise, because resuming mid-body needs a continuation that outlives the call. **This option exists only because the ABI documents were read**, and it was absent
from the draft that preceded the reference pass. It has not been costed.

**Two conventions, declared per entry point.** The artefact states which convention each exported function
uses, and the host dispatches accordingly. Costs a consumer-visible distinction and a metadata field.
Preserves the cheap path for the twenty-three of twenty-four chunks that can use it.

**One callback convention everywhere.** Uniform for the host. Costs every stream chunk an external call and,
more seriously, gives up the property that no frame is live during host execution, which is the property the
bounded-memory analysis wants. That is not a small concession in a project whose value proposition is
definitive worst-case memory.

The memory difference is the one that can be stated exactly. Let $L(\varepsilon)$ denote the set of native
frames live while host code executes between suspensions. Then

$$L(\varepsilon_{\mathrm{ret}}) = \varnothing, \qquad L(\varepsilon_{\mathrm{cb}}) = \{\, \mathrm{frame}(k) \,\} \cup \{\, \mathrm{frame}(c) : c \in \mathrm{callers}(k) \,\},$$

because the return convention has ended the call by the time the host runs and the callback convention has
not. The worst-case native stack bound therefore differs by

$$\Delta M \;=\; \sum_{\phi \in L(\varepsilon_{\mathrm{cb}})} \mathrm{size}(\phi),$$

a quantity that is bounded and computable but **charged for the whole duration of host activity**, which the
analysis does not bound. Under the return convention that term is identically zero.

The host-interaction counts also differ. Writing $s$ for suspensions per iteration, the native call counts
per iteration are

$$\tau_{\mathrm{ret}} = 1, \qquad \tau_{\mathrm{cb}} = 1 + s,$$

against a virtual-machine baseline of two host round-trips per iteration, since the reset instruction
returns control separately from the suspension. Every stream chunk in the corpus has $s = 1$.

**A fourth option this spike did not evaluate**, and which is recorded so it is not mistaken for absent, is
to make the delegating chunk's callee terminate. The one delegating stream chunk calls a terminating
coroutine, and if that call were restructured so the suspension belonged to the stream chunk instead of the
callee, the whole corpus would fit one convention. This is a change to the source program and not the
backend, it is outside the backend's authority, and whether it is reasonable is a language question this
article is not equipped to answer.

**Delegation is a specified problem elsewhere and the specification is instructive.** [PEP 380][ref_pep380]
defines `yield from` so that a subgenerator's yields pass through to the outermost caller while its
**return** value becomes the value of the delegating expression. That is precisely the two-channel
discipline this article arrives at, imposed at the language level rather than at the interface level. The
delegating construct must distinguish the callee's suspensions from the callee's completion, because they go
to different places. The Keleusma delegating chunk has the same structure and currently resolves it by
routing suspensions through the callback while discarding the completion, which works only because the
completion is unused in this program.

The recommendation is **two conventions declared per entry point**, on the grounds that the memory property
is the project's reason for existing and one chunk in twenty-four is a poor reason to give it up. This is a
recommendation and not a conclusion, and the option to restructure the source has not been costed.

## The Contemporary Literature

The question this article treats sits at the intersection of four literatures that rarely cite one another,
being coroutine implementation, continuation-passing transformation, application binary interface design,
and worst-case resource analysis.
**The first three have answered the representation question repeatedly and the fourth is the reason the answer matters here.**
What follows surveys each and marks where the present problem is and is not covered.

### Coroutines were classified before they were implemented well

The construct is old. [Conway 1963][research_conway_1963] introduced coroutines to structure a separable
compiler, and the motivating example was a compiler passing tokens between phases, close to the present use.
The taxonomy that still governs discussion is [de Moura and Ierusalimschy 2009][research_demoura_2009],
which separates coroutines along three axes, **symmetric or asymmetric**, **first-class or constrained**,
and **stackful or stackless**. Keleusma's two forms are both asymmetric and constrained, and the article's
question is precisely whether the backend must be stackful.

That taxonomy already contains the article's finding in a different vocabulary. An asymmetric coroutine
returns to its resumer, and the resumer must distinguish a suspension from a completion, which
[Marlin 1980][research_marlin_1980] treats as a defining obligation of the mechanism rather than an
implementation detail. The literature has never regarded the discriminator as optional, and it took a
backend author rediscovering it from cardinality to notice.

**Where the literature does not reach the present question is this.** It treats coroutines as a language
feature to be provided, not as an interface exposed across a foreign function boundary to a host in another
language. The distinction matters because a language runtime can afford a uniform representation with a tag,
while a statically bounded artefact linked into a C or Ada program is charged for every byte of that
representation by an analysis that must be sound.

The contemporary work on the construct, harvested rather than recalled and listed in full below, is where
the classification stopped being the interesting part and the implementation started being it.

- [Grolaux and others, 2026, Async/await is an Effective Paradigm for Event Management of User Interfaces][research_grolaux_nguyen_2026]
- [Castañeda and Rodríguez, 2026, Asynchronous Wait-Free Runtime Verification and Enforcement of Linearizability][research_castaneda_rodriguez_2026]
- [Han and others, 2026, Design and Implementation of Boss AI for 2D Action Games Using Finite State Machines and Coroutine Chaining][research_han_yoo_2026]
- [Frąszczak and Frąszczak, 2026, PhishingWebCollector Async python library for automated phishing feed collection][research_fraszczak_fraszczak_2026]
- [Magesty and Montandon, 2026, PromiseAwait A Dataset of JavaScript Migrations from Promises to Async/Await][research_magesty_montandon_2026]
- [Williams and Elliott, 2025, Libfork Portable Continuation-Stealing With Stackless Coroutines][research_williams_elliott_2025]
- [Reitz and Posner, 2025, Stackless vs. Stackful Coroutines A Comparative Study for RDMA-based Asynchronous Many-Task AMT Runtimes][research_reitz_posner_2025]
- [Posner and others, 2025, Toward Dynamic Resource Management An Asynchronous Many-Task AMT Runtime System leveraging Dynamic Processes with PSets DPP][research_posner_ellersiek_2025]
- [Shcherbakov and Shcherbakova, 2024, Comparative analysis of coroutine functionality in modern programming languages][research_shcherbakov_shcherbakova_2024]
- [Zhao and others, 2024, COPS A Coroutine-Based Priority Scheduling Framework Perceived by the Operating System][research_zhao_liao_2024]
- [Li and others, 2024, GastCoCo Graph Storage and Coroutine-Based Prefetch Co-Design for Dynamic Graph Processing][research_li_tao_2024]
- [Friese and others, 2024, Lamellar A Rust-based Asynchronous Tasking and PGAS Runtime for High Performance Computing][research_friese_gioiosa_2024]
- [Mykola, 2024, USING ASYNCHRONOUS PROGRAMMING IN PYTHON TO IMPROVE APPLICATION PERFORMANCE][research_mykola_2024]
- [Castañeda and Rodríguez, 2023, Asynchronous Wait-Free Runtime Verification and Enforcement of Linearizability][research_castaneda_rodriguez_2023]
- [Mane Ritesh Pratap and Alpona Das, 2023, Designing a Random Password Generator Using Python Programming Language][research_maneriteshpratap_alponadas_2023]
- [Gore and others, 2023, Sentence Generator for English Language using Formal Semantics][research_gore_bajaj_2023]
- [Daiß and others, 2023, Stellar Mergers with HPX-Kokkos and SYCL Methods of using an Asynchronous Many-Task Runtime System with SYCL][research_daiss_diehl_2023]
- [Weber and others, 2022, A closer look at process-based simulation with stackless coroutines][research_weber_wiesner_2022]
- [Suetterlein and others, 2022, Extending an asynchronous runtime system for high throughput applications A case study][research_suetterlein_manzano_2022]
- [Wang and Huang, 2022, SGPM A coroutine framework for transaction processing][research_wang_huang_2022]
- [Wang and huang, 2022, Sgpm A Coroutine Scheduling Model for Wound-Wait Concurrency Control][research_wang_huang_2022_2]
- [Holmen and others, 2021, A Heterogeneous MPI+PPL Task Scheduling Approach for Asynchronous Many-Task Runtime Systems][research_holmen_sahasrabudhe_2021]
- [Diehl and others, 2021, Performance Measurements Within Asynchronous Task-Based Runtime Systems A Double White Dwarf Merger as an Application][research_diehl_marcello_2021]
- [Zhou and others, 2020, Design and Implementation of Coroutine Scheduling System on SW26010][research_zhou_wu_2020]
- [PIETERS and SCHRIJVERS, 2020, Faster coroutine pipelines A reconstruction][research_pieters_schrijvers_2020]
- [Weber and Fischer, 2020, Process-Based Simulation with Stackless Coroutines][research_weber_fischer_2020]
- [Ataei and Manohar, 2019, AMC An Asynchronous Memory Compiler][research_ataei_manohar_2019]
- [Wagle and others, 2019, Runtime Adaptive Task Inlining on Asynchronous Multitasking Runtime Systems][research_wagle_monil_2019]
- [Wang, 2019, Web Crawler Scheduler Based on Coroutine][research_wang_2019]
- [Corrodi and others, 2018, A semantics comparison workbench for a concurrent, asynchronous, distributed programming language][research_corrodi_heussner_2018]
- [Peterson and others, 2017, Addressing Global Data Dependencies in Heterogeneous Asynchronous Runtime Systems on GPUs][research_peterson_humphrey_2017]
- [Yoo and Kim, 2017, Coroutine based Algorithms for reducing Memory overhead in Virtual Reality][research_yoo_kim_2017]
- [Spivey, 2017, Faster coroutine pipelines][research_spivey_2017]
- [DeBuhr and others, 2017, Scalable Hierarchical Multipole Methods Using an Asynchronous Many-Tasking Runtime System][research_debuhr_zhang_2017]
- [Baskaran and others, 2016, Automatic Code Generation and Data Management for an Asynchronous Task-Based Runtime][research_baskaran_pradelle_2016]
- [Толстікова and others, 2016, Efficiency asynchronous application programming language Python][research_efficiency_asynchronous_application_2016]
- [Wibowo and others, 2015, Unit test code generator for lua programming language][research_wibowo_hendradjaya_2015]

### Continuation-passing style answers the representation question, expensively

The general transformation is known and exact. [Reynolds 1972][research_reynolds_1972] established
continuation passing as a definitional technique, [Strachey and Wadsworth 1974][research_strachey_1974] gave
it its semantics, and [Appel 1992][research_appel_1992] made it a compiler architecture. Under continuation
passing every suspension becomes a call to a continuation and the representation question dissolves, because
there are no returns to collide with.

**It dissolves the question by paying for it everywhere.** The transformation is global, it changes the
calling convention of every function and not of coroutines alone, and the resulting closures are heap
allocated unless a later analysis recovers the stack discipline.
[Danvy and Nielsen 2001][research_danvy_nielsen_2001] show defunctionalisation recovering first-order code
from the higher-order form, the step that makes continuation passing implementable without a garbage
collector, and it is the step a bounded-memory project would have to trust.

Delimited control is the sharper tool. [Danvy and Filinski 1990][research_danvy_filinski_1990] introduced
`shift` and `reset`, [Felleisen 1988][research_felleisen_1988] the prompt-based formulation, and
[Dybvig, Peyton Jones and Sabry 2007][research_dybvig_2007] a monadic framework with an implementation
strategy. [Flatt and others 2007][research_flatt_2007] report adding delimited and composable control to a
production system, the closest thing in the literature to a cost report.
**A delimited continuation is exactly a coroutine frame**, and the delimiter is exactly the boundary this
article's reset instruction draws.

The continuation literature harvested for this survey is listed below. It is the thinnest of the modern
clusters, at 15 records from 2015 onward against 38 earlier
ones, and the imbalance is itself informative. The representation question was answered in the 1970s and
1990s and the modern work has moved to the handler formulation surveyed further down.

- [Todoran and Ciobanu, 2025, Metric Continuation-Passing Semantics for Multiparty Interactions][research_todoran_ciobanu_2025]
- [Pyzik, 2023, Call-By-Name Is Just Call-By-Value with Delimited Control][research_pyzik_2023]
- [VANDENBROUCKE and SCHRIJVERS, 2023, Disjunctive Delimited Control][research_vandenbroucke_schrijvers_2023]
- [Ikemori and others, 2023, Typed Equivalence of Labeled Effect Handlers and Labeled Delimited Control Operators][research_ikemori_cong_2023]
- [Schuster and others, 2022, A typed continuation-passing translation for lexical effect handlers][research_schuster_brachthauser_2022]
- [Ishio and Asai, 2022, Type System for Four Delimited Control Operators][research_ishio_asai_2022]
- [Gibbons, 2021, Continuation-Passing Style, Defunctionalization, Accumulations, and Associativity][research_gibbons_2021]
- [Avanzini and others, 2021, On continuation-passing transformations and expected cost analysis][research_avanzini_barthe_2021]
- [Komolov and others, 2020, An empirical study of multi-threading paradigms Reactive programming vs continuation-passing style][research_komolov_askarbekuly_2020]
- [Todoran, 2020, Metric Semantics for Concurrent Languages Designed in Continuation-Passing Style][research_todoran_2020]
- [FORSTER and others, 2019, On the expressive power of user-defined effects Effect handlers, monadic reflection, delimited control][research_forster_kammar_2019]
- [Abdallah, 2018, PRISM revisited Declarative implementation of a probabilistic programming language using multi-prompt delimited control][research_abdallah_2018]
- [Todoran and Papaspyrou, 2017, Concurrency Semantics in Continuation-Passing Style][research_todoran_papaspyrou_2017]
- [Schöpp, 2017, Defunctionalisation as modular closure conversion][research_schopp_2017]
- [Biernacki and others, 2015, A Dynamic Continuation-Passing Style for Dynamic Delimited Continuations][research_biernacki_danvy_2015]

### The stackless transformation is what production compilers actually ship

The state-machine transformation, in which a coroutine becomes a function over an explicit state record, is
the dominant implementation strategy and it is well documented.
[Syme, Petricek and Lomov 2011][research_syme_2011] describe the F# asynchronous model,
[Bierman and others 2012][research_bierman_2012] formalise the C# `async` transformation, and
[Elizarov and others 2021][research_elizarov_2021] give the design rationale for Kotlin coroutines including
the suspension sentinel discussed above. [Prokopec and Liu 2018][research_prokopec_2018] extend the
treatment to coroutines with snapshots and give a cost model.

**Every one of these reports the same discriminator problem and solves it the same way**, by returning a
tagged or sentinel value. That convergence is the strongest available evidence for the widened-return option
this article identifies, and it was invisible from inside the backend.

**It is also evidence for the correction recorded in the Epistemic State, and reading it carefully would
have prevented the error.** Not one of these systems returns a bare tagged value. Each pairs the tag with a
state object that survives the call, being the state machine in C# and F# and the continuation in Kotlin,
because a coroutine that suspends more than once must resume mid-body. **The literature converged on the
triple, and this article originally read it as converging on the pair.**

The alternative is stackful, which the operating-systems literature has costed thoroughly.
[von Behren and others 2003][research_vonbehren_2003] argue for threads with dynamically sized stacks
against event-driven code, and the stack-growth machinery they describe is what a stackful coroutine needs.
For a project whose memory bound must be static, that machinery is not available.

The code-generation literature this article's backend sits inside is the largest of the survey's topical
clusters, at 201 contemporary records, exceeded only by the general systems cluster
listed at the end. It is here because the stackless transformation is a code-generation decision before it
is a language-design one.

- [Pan and others, 2026, A Backend-Agnostic Compiler for Approximate Query Processing with Probabilistic Tensor Algebra][research_pan_cheney_2026]
- [Zhong and others, 2026, A Multi-Modal Retrieval-Augmented Framework for Compiler Backend Generation with LLMs][research_zhong_lv_2026]
- [Tirichine and others, 2026, A Reinforcement Learning Environment for Automatic Code Optimization in the MLIR Compiler][research_tirichine_ameur_2026]
- [Maldonado and Carrasco-Sáez, 2026, A Reusable J48-Targeting Python Backend for Scikit-Learn Workflows Differential Validation Against WEKA J48][research_maldonado_carrascosaez_2026]
- [Zhong and others, 2026, BePilot An AI Programming Assistant for Compiler Backend Development][research_zhong_sun_2026]
- [Horvat and others, 2026, Comparative Evaluation of Gemini and DeepSeek for LLM-Generated Code Quality and Architectural Robustness in Backend Software Engineering][research_horvat_ursic_2026]
- [Reddy and others, 2026, Compiler-Assisted Instruction Fusion][research_reddy_singh_2026]
- [Kwon and others, 2026, Compiler-Runtime Co-operative Chain of Verification for LLM-Based Code Optimization][research_kwon_shin_2026]
- [Biradar and others, 2026, Design and Development of an AI-Powered Code Generation System with Persistent Memory and Multi-Agent Architecture][research_biradar_dhikale_2026]
- [Wu and others, 2026, Designing quantum chemistry algorithms with just-in-time compilation][research_wu_sun_2026]
- [Alladi and others, 2026, Enabling Automatic Compiler-Driven Vectorization of Transformers][research_alladi_ros_2026]
- [Burgholzer and others, 2026, Focus Session Paper The MQT Compiler Collection A Blueprint for a Future-Proof Quantum-Classical Compilation Framework][research_burgholzer_haag_2026]
- [Zhang and others, 2026, GeoIR-Compiler A Geospatial Intermediate Representation and Compilation Framework for Chinese Urban Spatial Question Answering][research_zhang_deng_2026]
- [Luo and others, 2026, GeoJSON agents a multi-agent LLM architecture for geospatial analysis-function calling vs. code generation][research_luo_lin_2026]
- [Zhang and others, 2026, LEGO-compiler enhancing neural compilation through translation composability][research_zhang_zhao_2026]
- [Fang and others, 2026, LLM-VeriOpt Verification-Guided Reinforcement Learning for LLM-Based Compiler Optimization][research_fang_kang_2026]
- [M, 2026, No-Code Backend Orchestrator with Drag and Drop Architecture and AI-Assisted Contextual Code Generation][research_m_2026]
- [Krogstie and others, 2026, PIP Making Andersen's Points-to Analysis Sound and Practical for Incomplete C Programs][research_krogstie_bahmann_2026]
- [Dickerson and others, 2026, Practical Python FPGA Acceleration with Fast Just-In-Time Compilation and Configuration][research_dickerson_srinivasan_2026]
- [Zhao and others, 2026, QuaMap A Multi-Backend Benchmark Dataset for Quantum Circuit Mapping and Learning-Based Compiler Evaluation][research_zhao_li_2026]
- [Lancellotti and others, 2026, Quantum Oracle Synthesis from HDL Designs via Multi Level Intermediate Representation][research_lancellotti_buda_2026]
- [Baradaran and others, 2026, Reusing Legacy Code in Wasm Key Challenges of Compilation and Code Semantics Preservation][research_baradaran_huang_2026]
- [de Ferrière and others, 2026, SecSwift, a Compiler-Based Framework for Software Countermeasures in Cybersecurity][research_deferriere_janin_2026]
- [Rinard, 2026, Testing, Credible Compilation, and Verification in the Axon Verified Compiler in Lean and Claude Code][research_rinard_2026]
- [Qian and others, 2026, Thinking Fast and Correct Automated Rewriting of Numerical Code through Compiler Augmentation][research_qian_sathia_2026]
- [Ko and Heo, 2026, TinyGen Portable and Compact Code Generation for Tiny Machine Learning][research_ko_heo_2026]
- [Cheng and Wu, 2026, Toward Unified Chinese Multi-Dialectal Speech Recognition via Pinyin Intermediate Representation][research_cheng_wu_2026]
- [Zhong and others, 2026, Towards Fully Automated Compiler Backend Generation with Multi-Agent Systems How Far Are We?][research_zhong_qiu_2026]
- [Schwarz and others, 2026, TPDE A Fast Adaptable Compiler Back-End Framework][research_schwarz_kamm_2026]
- [Yi and others, 2026, Understanding and Finding JIT Compiler Performance Bugs][research_yi_ding_2026]
- [Li and others, 2026, Unleashing Triton on CPUs Compilation and Runtime Co-Optimization for Scalable Vector Architectures][research_li_chai_2026]
- [Kang and others, 2026, WAMI Compilation to WebAssembly through MLIR without Losing Abstraction][research_kang_desai_2026]
- [Maia and others, 2026, Why Just-In-Time Compilation Matters Evaluating Runtime and Energy Efficiency][research_maia_cunha_2026]
- [Zhu and Xie, 2025, A Domain-Specific Compiler for Embedded DSP Development Based on Component Code Generation Architecture and Correctness][research_zhu_xie_2025]
- [Lopoukhine and others, 2025, A Multi-level Compiler Backend for Accelerated Micro-kernels Targeting RISC-V ISA Extensions][research_lopoukhine_ficarelli_2025]
- [Sun and others, 2025, Archs A WebAssembly Runtime for Cross-host Heterogeneous Computing in Serverless][research_sun_tu_2025]
- [Sun and others, 2025, Automating Target Description Processing for Efficient Compiler Backend Development][research_sun_zhong_2025]
- [Lee and others, 2025, Bit-Level Semantics Scalable RAG Retrieval with Neurosymbolic Hyperdimensional Computing][research_lee_jang_2025]
- [Tamura and others, 2025, Bringing Together Cross-ISA Checkpoint/Restoration and AOT Compilation of WebAssembly Programs][research_tamura_kotani_2025]
- [Meier and others, 2025, CertiCoq-Wasm A Verified WebAssembly Backend for CertiCoq][research_meier_jensen_2025]
- [Bryant and others, 2025, Certified Knowledge Compilation with Application to Formally Verified Model Counting][research_bryant_nawrocki_2025]
- [Hammer and others, 2025, Compiler-Like Code Generation for fUML Reducing Overhead in Executable UML][research_hammer_maschotta_2025]
- [Kocourek and others, 2025, Copy-and-Patch Just-in-Time Compiler for R][research_kocourek_krikava_2025]
- [Ali and others, 2025, Does Coding Style Really Survive Compilation? Stylometry of Executable Code Revisited][research_ali_bilgis_2025]
- [Kaynaroglu and others, 2025, EUTROPY A Python-based software optimized with Just-In-Time compilation for simulating eutrophication dynamics in aquatic systems][research_kaynaroglu_razinkovasbaziukas_2025]
- [Ding and others, 2025, HFF-JIT A Hybrid Fuzzing Framework for JIT Compiler Vulnerability Detection in JavaScript][research_ding_li_2025]
- [Lin and others, 2025, Intermediate Representation-Based Approach for Code Refactoring and Quality Evaluation][research_lin_ni_2025]
- [Rong and others, 2025, IRFuzzer Specialized Fuzzing for LLVM Backend Code Generation][research_rong_yu_2025]
- [Souha and others, 2025, Modeling and Automated Code Generation of the Backend of Tourism Applications][research_souha_ouaddi_2025]
- [Ravedutti Lucio Machado and others, 2025, P4IRS An intermediate representation and compiler for parallel and performance-portable particle simulations][research_raveduttiluciomachado_eitzinger_2025]
- [Ramdani and others, 2025, Pengembangan Backend Aplikasi Geoproperty dengan Golang di PT. Nerdvana Solusi Teknologi][research_ramdani_nabarian_2025]
- [Georgakoudis and others, 2025, Proteus Portable Runtime Optimization of GPU Kernel Execution with Just-in-Time Compilation][research_georgakoudis_parasyris_2025]
- [Cieszewski, 2025, PyHLS Intermediate Representation for Versatile High-Level Synthesis][research_cieszewski_2025]
- [Pavlovskiy and Platov, 2025, RESEARCH ON CODE GENERATION OF C/C++ COMPILER FOR HIGH-PERFORMANCE COMPUTING IN MICROPROCESSOR SYSTEMS][research_pavlovskiy_platov_2025]
- [Fruehwirth, 2025, Runtime Repeated Recursion Unfolding in CHR A Just-In-Time Online Program Optimization Strategy That Can Achieve Super-Linear Speedup][research_fruehwirth_2025]
- [Patel and others, 2025, SySTeC A Symmetric Sparse Tensor Compiler][research_patel_ahrens_2025]
- [Gaißert and others, 2025, Tracing Just-in-Time Compilation for Effects and Handlers][research_gaissert_bolztereick_2025]
- [Berger and others, 2025, Translation Validation for LLVM's AArch64 Backend][research_berger_briles_2025]
- [Shaikhha and others, 2024, A Tensor Algebra Compiler for Sparse Differentiation][research_shaikhha_huot_2024]
- [Choi and others, 2024, Accelerating Sensor Software Performance on Edge Devices Through Just-in-Time Compilation][research_choi_park_2024]
- [Robin and Khan, 2024, An open-source P416 compiler backend for reconfigurable match-action table switches Making networking innovation accessible][research_robin_khan_2024]
- [Osborne and others, 2024, Awkward Just-In-Time JIT Compilation A Developer's Experience][research_osborne_pivarski_2024]
- [Raju Cherukuri, 2024, Building Scalable Web Applications Best Practices for Backend Architecture][research_rajucherukuri_2024]
- [Zhong and others, 2024, ComBack A Versatile Dataset for Enhancing Compiler Backend Development Efficiency][research_zhong_lyu_2024]
- [Engelke and Schwarz, 2024, Compile-Time Analysis of Compiler Frameworks for Query Compilation][research_engelke_schwarz_2024]
- [Geeson and Smith, 2024, Compiler Testing with Relaxed Memory Models][research_geeson_smith_2024]
- [Han and others, 2024, Enabling Fine-Grained Incremental Builds by Making Compiler Stateful][research_han_zhao_2024]
- [Jesus and Weiland, 2024, Evaluating and optimising compiler code generation for NVIDIA Grace][research_jesus_weiland_2024]
- [Drescher and Engelke, 2024, Fast Template-Based Code Generation for MLIR][research_drescher_engelke_2024]
- [Mukherjee and others, 2024, HLS-IRT Hardware Trojan Insertion through Modification of Intermediate Representation During High-Level Synthesis][research_mukherjee_ghosh_2024]
- [Nejjar and others, 2024, LLMs for science Usage for code generation and data analysis][research_nejjar_zacharias_2024]
- [Jung, 2024, Miri Practical Undefined Behavior Detection for Rust Keynote][research_jung_2024]
- [GREEN and WOOD, 2024, REASONING ABOUT THE ACOUSTIC REALISATION OF SEMIVOWELS USING AN INTERMEDIATE REPRESENTATION - THE 'SPEECH SKETCH'][research_green_wood_2024]
- [Duhamel and Pillement, 2024, Runtime Task Scheduling for FPGA-Based Embedded Systems Using Just-in-Time Bitstream Prefetching][research_duhamel_pillement_2024]
- [Pham and Odersky, 2024, Stack-Copying Delimited Continuations for Scala Native][research_pham_odersky_2024]
- [Ramesh and others, 2024, ThriveJIT Dynamic Just-In-Time Compilation for Efficient Execution of Arithmetic Expressions][research_ramesh_sukanth_2024]
- [Kwon and others, 2024, Translation Validation for JIT Compiler in the V8 JavaScript Engine][research_kwon_kwon_2024]
- [Bauckholt and Holz, 2024, WebAssembly as a Fuzzing Compilation Target Registered Report][research_bauckholt_holz_2024]
- [Titzer, 2024, Whose Baseline Compiler is it Anyway?][research_titzer_2024]
- [Телегин, 2023, AHEAD-OF-TIME and JUST-IN-TIME technologies][research_ahead_of_time_and_just_in_time_2023]
- [Bhamidipati and Vemuri, 2023, ASPIRE An Intermediate Representation for Abstract Security Policies][research_bhamidipati_vemuri_2023]
- [Lim and Debray, 2023, Automatically Localizing Dynamic Code Generation Bugs in JIT Compiler Back-End][research_lim_debray_2023]
- [Blazy, 2023, CompCert A Journey through the Landscape of Mechanized Semantics for Verified Compilation Keynote][research_blazy_2023]
- [Prinz, 2023, Compilation of Distributed Programs to Services Using Multiple Programming Languages][research_prinz_2023]
- [Abdelmaksoud and others, 2023, DEL Dynamic Symbolic Execution-based Lifter for Enhanced Low-Level Intermediate Representation][research_abdelmaksoud_hammadeh_2023]
- [Shahrokhi and others, 2023, Efficient Query Processing in Python Using Compilation][research_shahrokhi_groeger_2023]
- [Barrière and others, 2023, Formally Verified Native Code Generation in an Effectful JIT Turning the CompCert Backend into a Formally Verified JIT Compiler][research_barriere_blazy_2023]
- [Groß and others, 2023, FUZZILLI Fuzzing for JavaScript JIT Compiler Vulnerabilities][research_gross_koch_2023]
- [2023, Green Supply Chain Management and Competitive Advantage Evidence of Just-in-time Management on Firm Performance SMEs in Indonesia][research_green_supply_2023]
- [Pichler and others, 2023, Hybrid Execution Combining Ahead-of-Time and Just-in-Time Compilation][research_pichler_li_2023]
- [Gourdin, 2023, Lazy Code Transformations in a Formally Verified Compiler][research_gourdin_2023]
- [Thangamani and others, 2023, Lifting Code Generation of Cardiac Physiology Simulation to Novel Compiler Technology][research_thangamani_jost_2023]
- [Gu, 2023, LLM-Based Code Generation Method for Golang Compiler Testing][research_gu_2023]
- [He and others, 2023, Profile Guided Optimization Transfer-Learning for OpenCL/SYCL Kernel Compilation and Runtime][research_he_zhao_2023]
- [Nedoria, 2023, Programming Language for Teaching Compilation and Transformation Technologies][research_nedoria_2023]
- [Wu, 2023, PyTorch 2.0 The Journey to Bringing Compiler Technologies to the Core of PyTorch Keynote][research_wu_2023]
- [Pečimúth, 2023, Remote Just-in-Time Compilation for Dynamic Languages][research_pecimuth_2023]
- [Moron and Wallentowitz, 2023, Support for Just-in-Time Compilation of WebAssembly for Embedded Systems][research_moron_wallentowitz_2023]
- [Lopes, 2023, Torchy A Tracing JIT Compiler for PyTorch][research_lopes_2023]
- [Rivera and others, 2022, A Compiler for Sound Floating-Point Computations using Affine Arithmetic][research_rivera_franchetti_2022]
- [Huang and others, 2022, A High-Performance Bidirectional Compiler for Conversion Between SystemC and Verilog][research_huang_gao_2022]
- [Stepanov and Itsykson, 2022, Backend Bug Finder a platform for effective compiler fuzzing][research_stepanov_itsykson_2022]
- [Schmale and others, 2022, Backend compiler phases for trapped-ion quantum computers][research_schmale_temesi_2022]
- [Jain and others, 2022, Coarse Grained FPGA Overlay for Rapid Just-In-Time Accelerator Compilation][research_jain_maskell_2022]
- [Akanbi and others, 2022, Code Generation Techniques in Compiler Design Conceptual and Structural Review][research_akanbi_ajose_2022]
- [Nguyen and McCaskey, 2022, Extending Python for Quantum-classical Computing via Quantum Just-in-time Compilation][research_nguyen_mccaskey_2022]
- [Polito and others, 2022, Interpreter-guided differential JIT compiler unit testing][research_polito_ducasse_2022]
- [Hartley and others, 2022, Just-In-Time Compilation on ARM-A Closer Look at Call-Site Code Consistency][research_hartley_zakkak_2022]
- [Katel and others, 2022, MLIR-based code generation for GPU tensor cores][research_katel_khandelwal_2022]
- [Serrano, 2022, On JavaScript Ahead-of-Time Compilation Performance Keynote][research_serrano_2022]
- [Ji and Wang, 2022, Optimizing Aggregate Computation of Graph Neural Networks with on-GPU Interpreter-Style Programming][research_ji_wang_2022]
- [Efthymiou and others, 2022, Quantum simulation with just-in-time compilation][research_efthymiou_lazzarin_2022]
- [2022, Supplemental Material for A Just-in-Time Adaptive Intervention to Enhance Physical Activity in the SMARTFAMILY2.0 Trial][research_supplemental_material_2022]
- [Izawa and others, 2022, Threaded Code Generation with a Meta-Tracing JIT Compiler][research_izawa_masuhara_2022]
- [Li and others, 2022, Unleashing the power of compiler intermediate representation to enhance neural program embeddings][research_li_ma_2022]
- [Mzid and others, 2022, Use of Compiler Intermediate Representation for Reverse Engineering A Case Study for GCC Compiler and UML Activity Diagram][research_mzid_charfi_2022]
- [Ortiz, 2022, Using WebAssembly to Teach Code Generation in a Compiler Design Course][research_ortiz_2022]
- [Rand, 2022, Writing and verifying a Quantum optimizing compiler keynote][research_rand_2022]
- [Quiring and others, 2021, 3CPS The Design of an Environment-Focussed Intermediate Representation][research_quiring_reppy_2021]
- [Rivera and others, 2021, An Interval Compiler for Sound Floating-Point Computations][research_rivera_franchetti_2021]
- [Papadimitriou and others, 2021, Automatically exploiting the memory hierarchy of GPUs through just-in-time compilation][research_papadimitriou_fumero_2021]
- [Jamieson and Brown, 2021, Compact native code generation for dynamic languages on micro-core architectures][research_jamieson_brown_2021]
- [Xu and Kjolstad, 2021, Copy-and-patch compilation a fast compilation algorithm for high-level languages and bytecode][research_xu_kjolstad_2021]
- [Barrière and others, 2021, Formally verified speculation and deoptimization in a JIT compiler][research_barriere_blazy_2021]
- [Demmler and others, 2021, Improved Circuit Compilation for Hybrid MPC via Compiler Intermediate Representation][research_demmler_katzenbeisser_2021]
- [Song and Wang, 2021, Monadic Programming Featured Teaching Innovation of Compilation Experiments][research_song_wang_2021]
- [Serrano, 2021, Of JavaScript AOT compilation performance][research_serrano_2021]
- [Liu and others, 2021, Relaxed Peephole Optimization A Novel Compiler Optimization for Quantum Circuits][research_liu_bello_2021]
- [Koehler and Steuwer, 2021, Towards a Domain-Extensible Compiler Optimizing an Image Processing Pipeline on Mobile CPUs][research_koehler_steuwer_2021]
- [Chhak and others, 2021, Towards formally verified compilation of tag-based policy enforcement][research_chhak_tolmach_2021]
- [Sambasivam and others, 2021, Writing P4 compiler backend for packet processing engines][research_sambasivam_subramanian_2021]
- [Loveless and others, 2020, A performance-optimizing compiler for cyber-physical digital microfluidic biochips][research_loveless_ott_2020]
- [Saieva and Kaiser, 2020, Binary Quilting to Generate Patched Executables without Compilation][research_saieva_kaiser_2020]
- [Felker, 2020, Design of Cyanobyte An Intermediate Representation to Standardize Digital Peripheral Datasheets for Automatic Code Generation][research_felker_2020]
- [Blazy, 2020, From Verified Compilation to Secure Compilation a Semantic Approach][research_blazy_2020]
- [Paul and others, 2020, Improving execution efficiency of just-in-time compilation based query processing on GPUs][research_paul_he_2020]
- [Brennan and others, 2020, JIT Leaks Inducing Timing Side Channels through Just-In-Time Compilation][research_brennan_rosner_2020]
- [Schuiki and others, 2020, LLHD a multi-level intermediate representation for hardware description languages][research_schuiki_kurth_2020]
- [Dakkak and others, 2020, The design and implementation of the wolfram language compiler][research_dakkak_wickhamjones_2020]
- [Scheidl, 2020, Valent-Blocks Scalable High-Performance Compilation of WebAssembly Bytecode For Embedded Systems][research_scheidl_2020]
- [Liu and others, 2019, Accelerating sequential consistency for Java with speculative compilation][research_liu_millstein_2019]
- [Finkel and others, 2019, ClangJIT Enhancing C++ with Just-in-Time Compilation][research_finkel_poliakoff_2019]
- [Hariri and others, 2019, Comparing Mutation Testing at the Levels of Source Code and Compiler Intermediate Representation][research_hariri_shi_2019]
- [Namakonov and Podkopaev, 2019, Compilation of OCaml memory model into Power][research_namakonov_podkopaev_2019]
- [Enrici and others, 2019, Efficient Data-Flow Analysis of UML/SysML Diagrams for Optimized Model Compilation of Hardware-software Systems][research_enrici_apvrille_2019]
- [Nappa and others, 2019, Fast Parallel Equivalence Relations in a Datalog Compiler][research_nappa_zhao_2019]
- [HATABA and others, 2019, Generation of Efficient Obfuscated Code through Just-in-Time Compilation][research_hataba_elmahdy_2019]
- [Müssig, 2019, Just enough, just in time, just for me][research_mussig_2019]
- [Schkufza and others, 2019, Just-In-Time Compilation for Verilog][research_schkufza_wei_2019]
- [Bourke and others, 2019, Mechanized semantics and verified compilation for a dataflow synchronous language with reset][research_bourke_brun_2019]
- [Castro-Lopez and Vega-Lopez, 2019, Multi-target Compiler for the Deployment of Machine Learning Models][research_castrolopez_vegalopez_2019]
- [Tine and others, 2019, POSTER Tango An Optimizing Compiler for Just-In-Time RTL Simulation][research_tine_yalamanchili_2019]
- [Zhang and others, 2019, SNC A Cloud Service Platform for Symbolic-Numeric Computation Using Just-In-Time Compilation][research_zhang_liu_2019]
- [KIAM TAN and others, 2019, The verified CakeML compiler backend][research_kiamtan_myreen_2019]
- [Baghdadi and others, 2019, Tiramisu A Polyhedral Compiler for Expressing Fast and Portable Code][research_baghdadi_ray_2019]
- [Turcotte and Vitek, 2019, Towards a Type System for R][research_turcotte_vitek_2019]
- [Tinnerholm and others, 2019, Towards introducing just-in-time compilation in a Modelica compiler][research_tinnerholm_sjolund_2019]
- [Curtis and others, 2018, A compiler for cyber-physical digital microfluidic biochips][research_curtis_grissom_2018]
- [Vandercammen and others, 2018, A flexible framework for studying trace-based just-in-time compilation][research_vandercammen_marr_2018]
- [Leopoldseder and others, 2018, Dominance-based duplication simulation DBDS code duplication to enable compiler optimizations][research_leopoldseder_stadler_2018]
- [Caamaño and Guelton, 2018, Easy Jit compiler assisted library to enable just-in-time compilation in C++ codes][research_caamano_guelton_2018]
- [Ottoni, 2018, HHVM JIT a profile-guided, region-based compiler for PHP and Hack][research_ottoni_2018]
- [., 2018, Just in time and competitive advantage understanding their linkages and impact on operational performance][research_just_in_time_2018]
- [Brock and others, 2018, PAYJIT space-optimal JIT compilation and its practical implementation][research_brock_ding_2018]
- [Caliskan and others, 2018, When Coding Style Survives Compilation De-anonymizing Programmers from Executable Binaries][research_caliskan_yamaguchi_2018]
- [Pape and others, 2017, Adaptive just-in-time value class optimization for lowering memory consumption and improving execution time performance][research_pape_bolz_2017]
- [Su and others, 2017, Automatic generation of fast BLAS3-GEMM A portable compiler approach][research_su_liao_2017]
- [Mainland, 2017, Better living through operational semantics an optimizing compiler for radio protocols][research_mainland_2017]
- [Reis and others, 2017, Compiler Techniques for Efficient MATLAB to OpenCL Code Generation][research_reis_bispo_2017]
- [Basu and others, 2017, Compiler-based code generation and autotuning for geometric multigrid on GPU-accelerated supercomputers][research_basu_williams_2017]
- [Rohr and Lindenstruth, 2017, Fast Failure Erasure Encoding Using Just in Time Compilation for CPUs, GPUs, and FPGAs][research_rohr_lindenstruth_2017]
- [Welch and others, 2017, Formalization IDEs Integrated with a Verifying Compiler][research_welch_durkee_2017]
- [HAMID and ITO, 2017, Image Segmentation to Design Semi-optimized Curve for B-code Generation][research_hamid_ito_2017]
- [Fumero and others, 2017, Just-In-Time GPU Compilation for Interpreted Languages with Partial Evaluation][research_fumero_steuwer_2017]
- [Sharygin and Buchatskiy, 2017, Survey of Just-in-Time Query Compilation Methods][research_sharygin_buchatskiy_2017]
- [Fox and others, 2017, Verified compilation of CakeML to multiple machine-code targets][research_fox_myreen_2017]
- [Zhang and others, 2017, Weak Memory Models Balancing Definitional Simplicity and Implementation Flexibility][research_zhang_vijayaraghavan_2017]
- [Spampinato and Püschel, 2016, A basic linear algebra compiler for structured matrices][research_spampinato_puschel_2016]
- [Tan and others, 2016, A new verified compiler backend for CakeML][research_tan_myreen_2016]
- [Dissegna and others, 2016, An Abstract Interpretation-Based Model of Tracing Just-in-Time Compilation][research_dissegna_logozzo_2016]
- [Bulej and others, 2016, Beneath the bytecode][research_bulej_zheng_2016]
- [Martinsen and others, 2016, Combining thread-level speculation and just-in-time compilation in Google's V8 JavaScript engine][research_martinsen_grahn_2016]
- [Kwon and Bae, 2016, Development of a Code Generation Support System in Integrated Development Environment of an Educational Compiler][research_kwon_bae_2016]
- [Suhendra and Bachtiar, 2016, MIGRATION CODE PADA BACKEND CRIMEZONE DARI PHP KE SCALA][research_suhendra_bachtiar_2016]
- [Li and others, 2016, Modular SDN Compiler Design with Intermediate Representation][research_li_hu_2016]
- [Béra and others, 2016, Practical Validation of Bytecode to Bytecode JIT Compiler Dynamic Deoptimization][research_bera_miranda_2016]
- [Moss and others, 2016, The ARES High-Level Intermediate Representation][research_moss_davis_2016]
- [Alexander and Black, 2016, The performance of object encodings in JavaScript][research_alexander_black_2016]
- [Plangger and Krall, 2016, Vectorization in PyPy's Tracing Just-In-Time Compiler][research_plangger_krall_2016]
- [Xu and Gregg, 2015, An Efficient Vectorization Approach to Nested Thread-level Parallelism for CUDA GPUs][research_xu_gregg_2015]
- [Oh and others, 2015, Bytecode-to-C Ahead-of-Time Compilation for Android Dalvik Virtual Machine][research_oh_yeo_2015]
- [Refaie and Thyabat, 2015, Effect of just-in-time selling strategy on firms' performance in Jordan][research_refaie_thyabat_2015]
- [Lee and others, 2015, Flow-sensitive runtime estimation an enhanced hot spot detection heuristics for embedded Java just-in-time compilers][research_lee_moon_2015]
- [Melrose and others, 2015, Just in Time][research_melrose_sachsenmaier_2015]
- [Khaldi and others, 2015, LLVM parallel intermediate representation][research_khaldi_jouvelot_2015]
- [Hollingshaus and Daddario, 2015, Performance Philosophy Arrived Just in Time?][research_hollingshaus_daddario_2015]
- [Heck and Zaidman, 2015, Quality criteria for just-in-time requirements just enough, just-in-time?][research_heck_zaidman_2015]
- [Khorasani and others, 2015, Scalable SIMD-Efficient Graph Processing on GPUs][research_khorasani_gupta_2015]
- [Heumann and others, 2015, Scalable Task Scheduling and Synchronization Using Hierarchical Effects][research_heumann_tzannes_2015]
- [Meybodi, 2015, The links between just-in-time practices and alignment of benchmarking performance measures][research_meybodi_2015]
- [Santhi and others, 2015, The Simian concept Parallel Discrete Event Simulation with interpreted languages and just-in-time compilation][research_santhi_eidenbenz_2015]

### Effect handlers are the modern generalisation, and they carry the same obligation

Algebraic effects subsume coroutines. [Plotkin and Pretnar 2009][research_plotkin_pretnar_2009] give the
handler formulation, [Leijen 2017][research_leijen_2017] a type-directed compilation,
[Hillerström and Lindley 2016][research_hillerstrom_2016] a row-typed treatment, and
[Sivaramakrishnan and others 2021][research_sivaramakrishnan_2021] a production retrofit onto OCaml with
performance figures.

The relevance here is narrow and worth stating precisely.
**An effect handler's return clause and its operation clauses are syntactically distinct**, which is the
same discriminator appearing a third time, now in the type system rather than the calling convention. A
language that adopted handlers would not face this article's question, because the distinction would already
be in the source. Keleusma does not adopt them, and the V0.4 architecture does not propose to.

- [Segura, 2026, Algebraic effects for bounded prompt pipelines Lawvere theories, handlers, and outcome traces][research_segura_2026]
- [Gillard and others, 2026, Dynamic Wind for OCaml Effect Handlers with Escaping Continuation Support][research_gillard_yamazaki_2026]
- [Trifanov and Schrijvers, 2026, Staging Effect Handlers for Modular Search][research_trifanov_schrijvers_2026]
- [Gao and Parreaux, 2025, A Lightweight Type-and-Effect System for Invalidation Safety Tracking Permanent and Temporary Invalidation with Constraint-Based Subtype Inference][research_gao_parreaux_2025]
- [van Rooij and Krebbers, 2025, Affect An Affine Type and Effect System][research_vanrooij_krebbers_2025]
- [Asai and Fujii, 2025, Defining Algebraic Effects and Handlers via Trails and Metacontinuations][research_asai_fujii_2025]
- [Voigt and others, 2025, Dynamic Wind for Effect Handlers][research_voigt_schuster_2025]
- [Ma, 2025, Lexical Effect Handlers Fast by Design, Correct by Proof][research_ma_2025]
- [Jaafar and Jaber, 2025, Operational Game Semantics for Generative Algebraic Effects and Handlers][research_jaafar_jaber_2025]
- [Ma and others, 2025, Zero-Overhead Lexical Effect Handlers][research_ma_ge_2025]
- [Yoshioka and others, 2024, Abstracting Effect Systems for Algebraic Effect Handlers][research_yoshioka_sekiyama_2024]
- [Mückenschnabel, 2024, Algebraic Effect Handlers with Bidirectional Type-Checking][research_muckenschnabel_2024]
- [SANADA, 2024, Algebraic effects and handlers for arrows][research_sanada_2024]
- [Tsuyama and others, 2024, An Intrinsically Typed Compiler for Algebraic Effect Handlers][research_tsuyama_cong_2024]
- [Kawamata and others, 2024, Answer Refinement Modification Refinement Type System for Algebraic Effects and Handlers][research_kawamata_unno_2024]
- [HILLERSTRÖM and others, 2024, Asymptotic speedup via effect handlers][research_hillerstrom_lindley_2024]
- [Ma and others, 2024, Lexical Effect Handlers, Directly][research_ma_ge_2024]
- [Xie and others, 2024, Parallel Algebraic Effect Handlers][research_xie_johnson_2024]
- [Isoda and others, 2024, Type-Safe Code Generation with Algebraic Effects and Handlers][research_isoda_yokoyama_2024]
- [Sanada, 2023, Category-Graded Algebraic Theories and Effect Handlers][research_sanada_2023]
- [Nguyen and others, 2023, Effect Handlers for Programmable Inference][research_nguyen_perera_2023]
- [Müller and others, 2023, From Capabilities to Regions Enabling Efficient Compilation of Lexical Effect Handlers][research_muller_schuster_2023]
- [New and others, 2023, Gradual Typing for Effect Handlers][research_new_giovannini_2023]
- [Sekiyama and Unno, 2023, Temporal Verification with Answer-Effect Modification Dependent Temporal Type-and-Effect System with Delimited Continuations][research_sekiyama_unno_2023]
- [Cong and Asai, 2023, Towards a Reflection for Effect Handlers][research_cong_asai_2023]
- [Xie and others, 2022, First-class names for effect handlers][research_xie_cong_2022]
- [Ghica and others, 2022, High-level effect handlers in C++][research_ghica_lindley_2022]
- [Hamana, 2022, Modular Termination for Second-Order Computation Rules and Application to Algebraic Effect Handlers][research_hamana_2022]
- [de Vilhena and Pottier, 2021, A separation logic for effect handlers][research_devilhena_pottier_2021]
- [Zyuzin and Nanevski, 2021, Contextual modal types for algebraic effects and handlers][research_zyuzin_nanevski_2021]
- [Karachalias and others, 2021, Efficient compilation of algebraic effect handlers][research_karachalias_koprivec_2021]
- [Xie and Leijen, 2021, Generalized evidence passing for effect handlers efficient compilation of effect handlers to C][research_xie_leijen_2021]
- [Noguchi and others, 2021, Implementing Algebraic Effects and Handlers in Non-functional Programming Languages][research_noguchi_matsumoto_2021]
- [Punchihewa and Wu, 2021, Safe mutation with algebraic effects][research_punchihewa_wu_2021]
- [Liu and others, 2020, A type-and-effect system for object initialization][research_liu_lhotak_2020]
- [Schuster and others, 2020, Compiling effect handlers in capability-passing style][research_schuster_brachthauser_2020]
- [Xie and Leijen, 2020, Effect handlers in Haskell, evidently][research_xie_leijen_2020]
- [HILLERSTRÖM and others, 2020, Effect handlers via generalised continuations][research_hillerstrom_lindley_2020]
- [Xie and others, 2020, Effect handlers, evidently][research_xie_brachthauser_2020]
- [Brachthäuser and others, 2020, Effects as capabilities effect handlers and lightweight effect polymorphism][research_brachthauser_schuster_2020]
- [BRACHTHÄUSER and others, 2020, Effekt Capability-passing style for type- and effect-safe, extensible effect handlers in Scala][research_brachthauser_schuster_2020_2]
- [Zhang and Myers, 2019, Abstraction-safe effect handlers via tunneling][research_zhang_myers_2019]
- [Brachthäuser and others, 2018, Effect handlers for the masses][research_brachthauser_schuster_2018]
- [Leijen, 2018, First class dynamic effect handlers or, polymorphic heaps with dynamic effect handlers][research_leijen_2018]
- [Biernacki and others, 2017, Handle with care relational interpretation of algebraic effects and handlers][research_biernacki_pirog_2017]
- [KAMMAR and PRETNAR, 2017, No value restriction is needed for algebraic effects and handlers][research_kammar_pretnar_2017]
- [Leijen, 2017, Structured asynchrony with algebraic effects][research_leijen_2017_2]
- [SALEH and SCHRIJVERS, 2016, Efficient algebraic effect handlers for Prolog][research_saleh_schrijvers_2016]
- [Pretnar, 2015, An Introduction to Algebraic Effects and Handlers. Invited tutorial paper][research_pretnar_2015]
- [Bauer and Pretnar, 2015, Programming with algebraic effects and handlers][research_bauer_pretnar_2015]

### Verified compilation constrains what the backend may do

The project's stance is that the backend refuses what it cannot lower rather than approximating it, and that
stance has a literature. [Leroy 2009][research_leroy_2009_cacm] reports CompCert and its formally verified
back end in [Leroy 2009b][research_leroy_2009_jar], and [Kumar and others 2014][research_kumar_2014] report
CakeML, a verified implementation of ML with a verified compiler. [Necula 1997][research_necula_1997]
formalises proof-carrying code, in which the artefact carries its own evidence, and
[Sewell and others 2013][research_sewell_2013] report translation validation for a verified operating-system
kernel, which is the technique a project unable to verify its compiler can still use.

**None of these treats the calling convention as a proof obligation**, and that is the gap the present
project sits in. CompCert's correctness theorem is about observable behaviour of whole programs under a
fixed calling convention, and it does not tell you which convention to choose when a source construct emits
two observable event kinds. The theorem shape assumed here, that a lowering is correct when yielded
sequences agree, is a coinductive statement over infinite traces of the kind
[Leroy and Grall 2009][research_leroy_grall_2009] formalise for big-step semantics of diverging programs.
**That paper is the right formal setting for the divergent case and this article does not use it as such**,
which is a real weakness rather than an omission of politeness.

- [Lasnier and others, 2026, Brack A Verified Compiler for Scheme via CakeML][research_lasnier_yallop_2026]
- [Lion and Broman, 2026, Making Time Observable Compiler Correctness for Real-Time C Programs][research_lion_broman_2026]
- [Nezamabadi and others, 2026, Verified VCG and Verified Compiler for Dafny][research_nezamabadi_myreen_2026]
- [Barbosa and others, 2025, Formally Verified Correctness Bounds for Lattice-Based Cryptography][research_barbosa_kannwischer_2025]
- [Kwon and others, 2025, Optimization-Directed Compiler Fuzzing for Continuous Translation Validation][research_kwon_jang_2025]
- [Girault, 2025, Toward a Formally Verified Compiler for a Synchronous, Functional, Data-Flow Programming Language][research_girault_2025]
- [Melquiond and Moreau, 2024, A Safe Low-Level Language for Computer Algebra and Its Formally Verified Compiler][research_melquiond_moreau_2024]
- [Liu and others, 2024, A Verified Compiler for a Functional Tensor Language][research_liu_bernstein_2024]
- [Debnath and others, 2024, ARMOR A Formally Verified Implementation of X.509 Certificate Chain Validation][research_debnath_jenkins_2024]
- [Wang and Xie, 2024, Enhancing Translation Validation of Compiler Transformations with Large Language Models][research_wang_xie_2024]
- [Monniaux, 2024, Memory Simulations, Security and Optimization in a Verified Compiler][research_monniaux_2024]
- [Chavanon and others, 2024, PfComp A Verified Compiler for Packet Filtering Leveraging Binary Decision Diagrams][research_chavanon_besson_2024]
- [Kanabar and others, 2023, PureCake A Verified Compiler for a Lazy Functional Language][research_kanabar_vivien_2023]
- [Derakhshan and others, 2023, Towards End-to-End Verified TEEs via Verified Interface Conformance and Certified Compilers][research_derakhshan_zhang_2023]
- [Panigrahi and Karfa, 2023, Translation Validation of Information Leakage of Compiler Optimizations][research_panigrahi_karfa_2023]
- [Nyangaresi and Ma, 2022, A Formally Verified Message Validation Protocol for Intelligent IoT E-Health Systems][research_nyangaresi_ma_2022]
- [Abdulaziz and Koller, 2022, Formal Semantics and Formally Verified Validation for Temporal Planning][research_abdulaziz_koller_2022]
- [Han and others, 2021, Parallelizing Compiler Translation Validation Using Happens-Before and Task-Set][research_han_yuki_2021]
- [Mittal and others, 2021, Towards an Approach for Translation Validation of Thread-level Parallelizing Transformations using Colored Petri Nets][research_mittal_banerjee_2021]
- [Roessle and others, 2019, Formally verified big step semantics out of x86-64 binaries][research_roessle_verbeek_2019]
- [Tahat and others, 2019, Scalable Translation Validation of Unverified Legacy OS Code][research_tahat_joshi_2019]
- [Patterson and Ahmed, 2019, The next 700 compiler correctness theorems functional pearl][research_patterson_ahmed_2019]
- [Banerjee and Karfa, 2018, Compiler-agnostic Translation Validation][research_banerjee_karfa_2018]
- [Lochbihler, 2018, Mechanising a Type-Safe Model of Multithreaded Java with a Verified Compiler][research_lochbihler_2018]
- [Bourke and others, 2017, A formally verified compiler for Lustre][research_bourke_brun_2017]
- [Avigad and others, 2017, A Formally Verified Proof of the Central Limit Theorem][research_avigad_holzl_2017]
- [Fonseca and others, 2017, An Empirical Study on the Correctness of Formally Verified Distributed Systems][research_fonseca_zhang_2017]
- [Barthe and others, 2017, Verified Translation Validation of Static Analyses][research_barthe_blazy_2017]
- [Tan and others, 2015, A verified type system for CakeML][research_tan_owens_2015]
- [Ngo and others, 2015, Modular translation validation of a full-sized synchronous compiler using off-the-shelf verification tools][research_ngo_talpin_2015]
- [Neis and others, 2015, Pilsner a compositionally verified compiler for a higher-order imperative language][research_neis_hur_2015]
- [Chlipala, 2015, Session details Session 4A Compiler Correctness][research_chlipala_2015]
- [Yang and others, 2015, Towards a verified compiler prototype for the synchronous language SIGNAL][research_yang_bodeveix_2015]

### Worst-case resource analysis is why the convention matters at all

If native code did not have to carry a bound, the callback convention would simply win on generality.
[Wilhelm and others 2008][research_wilhelm_2008] survey the worst-case execution-time problem and the tools
that address it, and it remains the standard reference for what a sound timing analysis requires. For the
memory side, [Regehr, Reid and Webb 2005][research_regehr_2005] eliminate stack overflow by abstract
interpretation of machine code, exactly the analysis a native Keleusma artefact must support and exactly
what a frame held across arbitrary host execution defeats.

**This is the literature that makes the choice non-obvious**, and it is the one the coroutine implementation
literature does not cite. A runtime that may allocate is free to choose the general mechanism. A bounded
artefact is not, and the trade appears only when both literatures are read together.

- [Charmanas and others, 2026, A topic-oriented trend analysis framework for Stack Exchange questions Case study on ChatGPT related queries on Stack Overflow][research_charmanas_georgiou_2026]
- [O Kim and Lee, 2026, Amortised neural acoustic tomography domain-specific encoder design and topology-dependent Eikonal analysis][research_okim_lee_2026]
- [Seidler and others, 2026, Wasm-WCET Worst-Case Execution-Time Analysis of WebAssembly Modules on Updatable Resource-Constrained Embedded Devices][research_seidler_michelis_2026]
- [Zolduoarrati and others, 2025, A cross-continental analysis of how regional cues shape top stack overflow contributors][research_zolduoarrati_licorish_2025]
- [Kaestner and others, 2025, Determining Worst-Case Execution Time Bounds for Multi-Core Processors][research_kaestner_gebhard_2025]
- [Lehmann and others, 2025, Hardware/Software Co-Analysis for Worst Case Execution Time Bounds][research_lehmann_bauer_2025]
- [Djalali and others, 2025, The Evolution of Software Usability in Developer Communities An Empirical Study on Stack Overflow][research_djalali_aljedaani_2025]
- [Wambua, 2025, Topics, Trends, and Sentiments in Software Testing An Analysis of Developers' Engagement on Stack Overflow][research_wambua_2025]
- [Merazga and others, 2025, Worst-Case Execution Time Analysis of a Real-Time System based on Arduino in CAN Network][research_merazga_rahem_2025]
- [Hu and others, 2024, An Abstract Interpretation-Based Framework for WCET Analysis of Parallel Programs][research_hu_liu_2024]
- [Thomas and others, 2024, Analyzing Data Flow and Control Flow of Multicore Software A Solution for Efficient Worst-Case Execution Time Analysis][research_thomas_salehi_2024]
- [Arnström and others, 2024, Exact Worst-Case Execution-Time Analysis for Implicit Model Predictive Control][research_arnstrom_broman_2024]
- [Veit and Böcskei, 2024, IFRS 9 Classification Aspects Measurement of Sustainability-Linked Loans at Amortised Cost or Fair Value][research_veit_bocskei_2024]
- [Bertholon and others, 2024, Interactive Source-to-Source Optimizations Validated using Static Resource Analysis][research_bertholon_chargueraud_2024]
- [Mizikovskiy, 2024, Methodology of management cost accounting and calculation of the cost of not amortised organizational and technological equipment for the production of industrial enterprise products][research_mizikovskiy_2024]
- [Albert and others, 2024, Synthesis of Sound and Precise Storage Cost Bounds via Unsound Resource Analysis and Max-SMT][research_albert_correas_2024]
- [Kumar and others, 2024, Utilizing Machine Learning Techniques for Worst-Case Execution Time Estimation on GPU Architectures][research_kumar_ranjbar_2024]
- [Ghadesi and others, 2024, What causes exceptions in machine learning applications? Mining machine learning-related stack traces on Stack Overflow][research_ghadesi_lamothe_2024]
- [Samiei and others, 2024, Worst-Case Execution Time Analysis of Real-Time Robotic Algorithms Using Reinforcement Learning][research_samiei_kahani_2024]
- [Paraman and Murthy, 2023, Analysis of benchmark program results of worst case execution time for multithreaded programs][research_paraman_murthy_2023]
- [Mondal and others, 2023, Investigating Technology Usage Span by Analyzing Users' QandA Traces in Stack Overflow][research_mondal_mondal_2023]
- [Swillus and Zaidman, 2023, Sentiment overflow in the testing stack Analyzing software testing posts on Stack Overflow][research_swillus_zaidman_2023]
- [Rodriguez Ferrandez and others, 2023, Worst Case Execution Time and Power Estimation of Multicore and GPU Software A Pedestrian Detection Use Case][research_rodriguezferrandez_joveralvarez_2023]
- [ISLAM and others, 2022, An Exploration of npm Package Co-Usage Examples from Stack Overflow A Case Study][research_islam_wang_2022]
- [WanXin and others, 2022, CUDA Acceleration of Worst-Case Execution Time Analysis Based On Model Checking][research_wanxin_tao_2022]
- [Battle and others, 2022, Exploring D3 Implementation Challenges on Stack Overflow][research_battle_feng_2022]
- [Sheth and Damevski, 2022, Grouping related stack overflow comments for software developer recommendation][research_sheth_damevski_2022]
- [Mahajan and Prasad, 2022, Providing Real-time Assistance for Repairing Runtime Exceptions using Stack Overflow Posts][research_mahajan_prasad_2022]
- [Velazquez-Rodriguez and others, 2022, Uncovering Library Features from API Usage on Stack Overflow][research_velazquezrodriguez_constantinou_2022]
- [Susca and others, 2022, Worst-Case Execution Time Estimation for Numerical Controllers][research_susca_mihaly_2022]
- [Friers and others, 2021, Amortised Encoding for Large High-Resolution Displays][research_friers_becher_2021]
- [van der Hoeven and Lecerf, 2021, Amortized Bivariate Multi-point Evaluation][research_vanderhoeven_lecerf_2021]
- [Kumar, 2021, Deep Neural Network Approach to Estimate Early Worst-Case Execution Time][research_kumar_2021]
- [Denzler and others, 2021, Experiences from Adjusting Industrial Software for Worst-Case Execution Time Analysis][research_denzler_fruhwirth_2021]
- [Zhao and others, 2021, Hot question prediction in Stack Overflow][research_zhao_zhang_2021]
- [Costa and others, 2021, Use of Measurements in Worst-Case Execution Time Estimation for Real-Time Systems][research_costa_deoliveira_2021]
- [Búr and others, 2021, Worst-case Execution Time Calculation for Query-based Monitors by Witness Generation][research_bur_marussy_2021]
- [Zhang and others, 2020, A Dynamic Instruction Cache Locking Approach for Minimizing Worst Case Execution Time of a Single Task][research_zhang_zheng_2020]
- [Emerson, 2020, Autoencoding Pixies Amortised Variational Inference with Graph Convolutions for Functional Distributional Semantics][research_emerson_2020]
- [Moser and Schneckenreither, 2020, Automated amortised resource analysis for term rewrite systems][research_moser_schneckenreither_2020]
- [Muts and Falk, 2020, Compiler-based WCET prediction performing function specialization][research_muts_falk_2020]
- [Nadi and Treude, 2020, Essential Sentences for Navigating Stack Overflow Answers][research_nadi_treude_2020]
- [Uddin and others, 2020, Mining API usage scenarios from stack overflow][research_uddin_khomh_2020]
- [Fusi and others, 2020, On the Use of Probabilistic Worst-Case Execution Time Estimation for Parallel Applications in High Performance Systems][research_fusi_mazzocchetti_2020]
- [Azzahra and others, 2020, PRE STACK DEPTH MIGRATION UNTUK KOREKSI EFEK PULL UP DENGAN MENGGUNAKAN METODE HORIZON BASED DEPTH TOMOGRAPHY PADA LAPANGAN 'A1 DAN A2'][research_azzahra_mulyatno_2020]
- [Mahajan and others, 2020, Recommending stack overflow posts for fixing runtime exceptions using failure scenario matching][research_mahajan_abolhassani_2020]
- [Arcaro and others, 2020, Reliability Test based on a Binomial Experiment for Probabilistic Worst-Case Execution Times][research_arcaro_silva_2020]
- [Meng and others, 2020, Survey on Estimation and Optimization of Worst-case Execution Time with Energy Consumption Constraint][research_meng_sun_2020]
- [Ventovaara and others, 2020, Worst-case Execution Time Estimation of Legacy Vehicular Embedded Functions An Industrial Case Study][research_ventovaara_hasanbegovic_2020]
- [Falk and Lokuciejewski, 2019, Correction to A compiler framework for the reduction of worst-case execution times][research_falk_lokuciejewski_2019]
- [Zuepke and Kaiser, 2019, Deterministic Futexes Addressing WCET and Bounded Interference Concerns][research_zuepke_kaiser_2019]
- [Yildiz and others, 2019, Software UART A Use Case for VSCPU Worst-Case Execution Time Analyzer][research_yildiz_iskender_2019]
- [Baltes and others, 2019, SOTorrent Studying the Origin, Evolution, and Usage of Stack Overflow Code Snippets][research_baltes_treude_2019]
- [Kim and others, 2019, WCET-Aware Stack Frame Management of Embedded Systems Using Scratchpad Memories][research_kim_khayatian_2019]
- [Zhang and Deng, 2018, A Depth Variant Seismic Wavelets Extraction Method for Inversion of Post-Stack Depth Domain Seismic Data][research_zhang_deng_2018]
- [Reinhardt and others, 2018, Augmenting stack overflow with API usage patterns mined from GitHub][research_reinhardt_zhang_2018]
- [Szydełko, 2018, BONDS BALANCE SHEET VALUATION IN AMORTISED COST CHOSEN ASPECTS][research_szydelko_2018]
- [Wu and Zhang, 2018, Cache-Aware SPM Allocation to Reduce Worst-Case Execution Time for Hybrid SPM-Caches][research_wu_zhang_2018]
- [Huangfu and Zhang, 2018, Estimating the Worst-Case Execution Time of the Shared Data Cache in Integrated CPU-GPU Architectures][research_huangfu_zhang_2018]
- [Carminati and others, 2018, On the use of static branch prediction to reduce the worst-case execution time of real-time applications][research_carminati_starke_2018]
- [Becker and Chakraborty, 2018, Optimizing Worst-Case Execution Times Using Mainstream Compilers][research_becker_chakraborty_2018]
- [Venkanna and others, 2018, PSO based optimization of worst-case execution time for ASIP application][research_venkanna_rao_2018]
- [Becker and others, 2018, Scalable and precise estimation and debugging of the worst-case execution time for analysis-friendly processors a comeback of model checking][research_becker_metta_2018]
- [Venkanna and Rao, 2018, Static Worst-Case Execution Time Optimization using DPSO for ASIP Architecture][research_venkanna_rao_2018_2]
- [Baltes and Diehl, 2018, Usage and attribution of Stack Overflow code snippets in GitHub projects][research_baltes_diehl_2018]
- [Jha and others, 2018, Worst Case Execution Time Estimation for Control Code of Automation Systems][research_jha_dsouza_2018]
- [Aquino and others, 2018, Worst-Case Execution Time Testing via Evolutionary Symbolic Execution][research_aquino_denaro_2018]
- [Fedasyuk and others, 2017, Architecture of a tool for automated testing the worst-case execution time of real-time embedded systems' firmware][research_fedasyuk_chopey_2017]
- [Tabassam and Obermaisser, 2017, Class-based query-optimization for minimizing worst-case execution times of diagnostic queries in embedded real-time systems][research_tabassam_obermaisser_2017]
- [Carminati and others, 2017, Combining loop unrolling strategies and code predication to reduce the worst-case execution time of real-time software][research_carminati_starke_2017]
- [Hausladen and others, 2017, Integration of Static Worst-Case Execution Time and Stack Usage Analysis for Embedded Systems Software in a Cloud-Based Development Environment][research_hausladen_gerstmayer_2017]
- [Abella and others, 2017, Measurement-Based Worst-Case Execution Time Estimation Using the Coefficient of Variation][research_abella_padilla_2017]
- [Jimenez Gil and others, 2017, Open Challenges for Probabilistic Measurement-Based Worst-Case Execution Time][research_jimenezgil_bate_2017]
- [Knoop and others, 2017, Replacing conjectures by positive knowledge Inferring proven precise worst-case execution time bounds using symbolic execution][research_knoop_kovacs_2017]
- [Zou and others, 2017, Towards comprehending the non-functional requirements through Developers' eyes An exploration of Stack Overflow using topic analysis][research_zou_xu_2017]
- [Mizobuchi and Takayama, 2017, Two improvements to detect duplicates in Stack Overflow][research_mizobuchi_takayama_2017]
- [Puffitsch, 2016, Efficient Worst-Case Execution Time Analysis of Dynamic Branch Prediction][research_puffitsch_2016]
- [Mondal and others, 2016, Embedded Emotion-based Classification of Stack Overflow Questions Towards the Question Quality Prediction][research_mondal_rahman_2016]
- [Seo and Kim, 2016, Measuring Method of Worst-case Execution Time by Analyzing Relation between Source Code and Executable Code][research_seo_kim_2016]
- [Seo and Kim, 2016, Operator-data type pair based execution environments independent worst-case execution time measuring method][research_seo_kim_2016_2]
- [Soleimani and Balarostaghi, 2016, Seismic image enhancement in post stack depth migration by finite offset CDS stack method][research_soleimani_balarostaghi_2016]
- [Mguidich and others, 2016, Time-Accurate ASM as a Refinement Scheme for Worst-Case Execution Time Estimation in Hard Real-Time Systems][research_mguidich_paun_2016]
- [2016, WORST CASE EXECUTION TIME CALCULATION OF PARALLEL EMBEDDED REAL-TIME SOFTWARE][research_worst_case_2016]
- [Al-Bataineh and others, 2015, Accelerating worst case execution time analysis of timed automata models with cyclic behaviour][research_albataineh_reynolds_2015]
- [Mushtaq and others, 2015, Calculation of worst-case execution time for multicore processors using deterministic execution][research_mushtaq_alars_2015]
- [Yu and Cohen, 2015, Guided Test Generation for Finding Worst-Case Stack Usage in Embedded Systems][research_yu_cohen_2015]
- [2015, Incorporating Near-Surface Velocity Anomalies in Pre-Stack Depth Migration Models][research_incorporating_near_surface_2015]
- [Wang and others, 2015, WCET-Aware Energy-Efficient Data Allocation on Scratchpad Memory for Real-Time Embedded Systems][research_wang_gu_2015]

### Compiler testing supplies the oracle and warns about its limits

The differential method used here is standard. [Yang and others 2011][research_yang_2011] report Csmith and
the compiler defects it found, [Le, Afshari and Su 2014][research_le_2014] introduce equivalence modulo
inputs, and [Chen and others 2020][research_chen_2020] survey compiler testing as a field.

**The warning these carry is directly applicable.** A differential oracle refutes and does not prove, and
its power is bounded by the inputs supplied. This article's equivalence assertion is checked over a finite
sample of resume sequences chosen by hand, the weakest form of the technique. Equivalence modulo inputs is
the natural strengthening and it has not been applied.

- [Klimis, 2026, Compilomorphic Fuzzing Turning a Compiler Against Itself][research_klimis_2026]
- [Boda and others, 2026, CPerfSmith A Randomized C Program Generator for Performance-Oriented Compiler Testing][research_boda_chunduri_2026]
- [Oh and Kim, 2026, Detecting Compiler-Introduced Security Bugs via IR Mutation and Coverage-Guided Fuzzing][research_oh_kim_2026]
- [Shirai and others, 2026, Does Programming Language Matter? An Empirical Study of Fuzzing Bug Detection][research_shirai_nourry_2026]
- [Liu and others, 2026, Learning Compiler Fuzzing Mutators from Historical Bugs][research_liu_qin_2026]
- [Zhang and others, 2026, LLM-Powered Silent Bug Fuzzing in Deep Learning Libraries via Versatile and Controlled Bug Transfer][research_zhang_xiao_2026]
- [Berlakovich and others, 2026, LOOL Low-Overhead, Optimization-Log-Guided Compiler Fuzzing][research_berlakovich_schwarcz_2026]
- [Berlakovich and others, 2026, LOOL Low-Overhead, Optimization-Log-Guided Compiler Fuzzing - RCR Report][research_berlakovich_schwarcz_2026_2]
- [Ren and others, 2026, SpiceFuzz LLM-Based Fuzzing for Spice Circuit Simulator Tools Bug Detection][research_ren_liu_2026]
- [Zhang and others, 2026, Transformation-Recipe-Based FPGA Synthesis Compiler Testing][research_zhang_jiang_2026]
- [Zeng and others, 2026, TypeNFuzz Dynamic Type-aware Object Dependence Graph-Guided Fuzzing for JavaScript Library Bug Discovery][research_zeng_wu_2026]
- [Ranjan and others, 2025, ClosureX Compiler Support for Correct Persistent Fuzzing][research_ranjan_paterson_2025]
- [Ali and others, 2025, CrossGuard Runtime-Adaptive LLM Fuzzing for Cross-Contract Vulnerabilities Detection][research_ali_chen_2025]
- [Ye and others, 2025, BazzAFL Moving Fuzzing Campaigns Towards Bugs via Grouping Bug-Oriented Seeds][research_ye_zhu_2025]
- [Liu and others, 2025, BoostPolyGlot A Structured IR Generation-Based Fuzz Testing Framework for GCC Compiler Frontend][research_liu_guo_2025]
- [Kim and others, 2025, Chimera Fuzzing P4 Network Infrastructure for Multi-Plane Bug Detection and Vulnerability Discovery][research_kim_tian_2025]
- [Gao and others, 2025, Clozemaster Fuzzing Rust Compiler by Harnessing Llms for Infilling Masked Real Programs][research_gao_yang_2025]
- [Boonriong and others, 2025, Compiler Fuzzing in Continuous Integration A Case Study on Dafny][research_boonriong_zetzsche_2025]
- [Tang and others, 2025, CTDip a diversity-guided test program synthesis approach for boosting compiler bug detection][research_tang_zeng_2025]
- [Zhu and others, 2025, Emerging Compiler Testing Based on Test Case Reuse][research_zhu_wang_2025]
- [Grabowski, 2025, Encoding Triangular Norms on Bounded Trellises with Mizar Proof Assistant][research_grabowski_2025]
- [Feng and others, 2025, Finding Compiler Bugs through Cross-Language Code Generator and Differential Testing][research_feng_ma_2025]
- [Boo and Lee, 2025, Finding Device Driver Bugs With Fuzzing PCIe Configuration Input][research_boo_lee_2025]
- [Gruner and others, 2025, Finding Information Leaks with Information Flow Fuzzing][research_gruner_brust_2025]
- [Gruner and others, 2025, Finding Information Leaks with Information Flow Fuzzing-RCR Report][research_gruner_brust_2025_2]
- [Qian and others, 2025, FreeWavm Enhanced WebAssembly Runtime Fuzzing Guided by Parse Tree Mutation and Snapshot][research_qian_ying_2025]
- [Kim and others, 2025, Fuzzing Acceleration for Memory Safety Bug Discovery with Slicer][research_kim_ryu_2025]
- [Talaat and others, 2025, GrammLLM Grammar-Guided LLM Test Generation for Compiler Validation][research_talaat_hassan_2025]
- [Ni and Li, 2025, Interleaving Large Language Models for Compiler Testing][research_ni_li_2025]
- [Xie and others, 2025, Kitten A Simple Yet Effective Baseline for Evaluating LLM-Based Compiler Testing Techniques][research_xie_xu_2025]
- [Hyatt and Dewey, 2025, Mutation-Based Fuzzing of the Swift Compiler with Incomplete Type Information][research_hyatt_dewey_2025]
- [Ricardo and others, 2025, On the Practicality of LLM-Based Compiler Fuzzing][research_ricardo_santosjunior_2025]
- [Wang and others, 2025, Research on Compiler Fuzzing Based on Syntax-semantics Dual-Dimensional Classification][research_wang_han_2025]
- [Kokkonis and others, 2025, ROSA Finding Backdoors with Fuzzing][research_kokkonis_marcozzi_2025]
- [Li and others, 2025, Solsmith Solidity Random Program Generator for Compiler Testing][research_li_liu_2025]
- [Hu and others, 2025, SSFuzz Synthesizing and scheduling bug-triggering code segments for history-driven compiler testing][research_hu_fan_2025]
- [Zhao and others, 2025, Thread-sensitive fuzzing for concurrency bug detection][research_zhao_fu_2025]
- [Hazott and others, 2025, Using virtual prototypes and metamorphic testing to verify the hardware/software-stack of embedded graphics libraries][research_hazott_stogmuller_2025]
- [Wu and others, 2025, WBSan WebAssembly Bug Detection for Sanitization and Binary-Only Fuzzing][research_wu_he_2025]
- [Zhou and others, 2024, C-CORE Clustering by Code Representation to Prioritize Test Cases in Compiler Testing][research_zhou_jiang_2024]
- [Tian and others, 2024, Differential testing solidity compiler through deep contract manipulation and mutation][research_tian_wang_2024]
- [Feitosa and Ribeiro, 2024, Differential Testing using Random Well-Typed Haskell Programs][research_feitosa_ribeiro_2024]
- [Georgescu and others, 2024, Evolutionary Generative Fuzzing for Differential Testing of the Kotlin Compiler][research_georgescu_olsthoorn_2024]
- [Suo and others, 2024, Fuzzing MLIR Compiler Infrastructure via Operation Dependency Analysis][research_suo_chen_2024]
- [Fan and others, 2024, History-driven Compiler Fuzzing via Assembling and Scheduling Bug-triggering Code Segments][research_fan_ye_2024]
- [Munley and others, 2024, LLM4VV Developing LLM-driven testsuite for compiler validation][research_munley_jarmusch_2024]
- [Schwarcz and others, 2024, LOOL Low-Overhead, Optimization-Log-Guided Compiler Fuzzing Registered Report][research_schwarcz_berlakovich_2024]
- [Han and others, 2024, Range Specification Bug Detection in Flight Control System Through Fuzzing][research_han_ma_2024]
- [Wang and Jung, 2024, Rustlantis Randomized Differential Testing of the Rust Compiler][research_wang_jung_2024]
- [Li and others, 2024, Simulink Compiler Testing via Configuration Diversification With Reinforcement Learning][research_li_guo_2024]
- [Yang and others, 2024, WhiteFox White-Box Compiler Fuzzing Empowered by Large Language Models][research_yang_deng_2024]
- [Ye and others, 2023, A Generative and Mutational Approach for Synthesizing Bug-Exposing Test Cases to Guide Compiler Fuzzing][research_ye_hu_2023]
- [Wu and others, 2023, Boosting Compiler Testing via Eliminating Test Programs with Long-Execution-Time][research_wu_yang_2023]
- [Lin and others, 2023, DeepDiffer Find Deep Learning Compiler Bugs via Priority-guided Differential Fuzzing][research_lin_song_2023]
- [Tu and others, 2023, Detecting C++ Compiler Front-End Bugs via Grammar Mutation and Differential Testing][research_tu_jiang_2023]
- [Utting and others, 2023, Differential Testing of a Verification Framework for Compiler Optimizations Case Study][research_utting_webb_2023]
- [Li and Su, 2023, Finding Unstable Code via Compiler-Driven Differential Testing][research_li_su_2023]
- [Donaldson and others, 2023, Industrial Deployment of Compiler Fuzzing Techniques for Two GPU Shading Languages][research_donaldson_clayton_2023]
- [Wang and others, 2023, MLIRSmith Random Program Generation for Fuzzing MLIR Compiler Infrastructure][research_wang_chen_2023]
- [Zhong and others, 2023, Neural Network Guided Evolutionary Fuzzing for Finding Traffic Violations of Autonomous Vehicles][research_zhong_kaiser_2023]
- [Kim and Hong, 2023, Poster BugOss A Regression Bug Benchmark for Empirical Study of Regression Fuzzing Techniques][research_kim_hong_2023]
- [Sharma and others, 2023, RustSmith Random Differential Compiler Testing for Rust][research_sharma_yu_2023]
- [Ito and others, 2023, Schfuzz Detecting Concurrency Bugs with Feedback-Guided Fuzzing][research_ito_matsubara_2023]
- [Qu and others, 2023, Scope-based Compiler Differential Testing][research_qu_huang_2023]
- [Li and others, 2022, ALPHAPROG Reinforcement Generation of Valid Programs for Compiler Fuzzing][research_li_liu_2022]
- [Godboley and others, 2022, AV-AFL A Vulnerability Detection Fuzzing Approach by Proving Non-reachable Vulnerabilities using Sound Static Analyser][research_godboley_gupta_2022]
- [Chen and Suo, 2022, Boosting Compiler Testing via Compiler Optimization Exploration][research_chen_suo_2022]
- [Aljaafari and others, 2022, Combining BMC and Fuzzing Techniques for Finding Software Vulnerabilities in Concurrent Programs][research_aljaafari_menezes_2022]
- [Liu and others, 2022, Coverage-guided tensor compiler fuzzing with joint IR-pass mutation][research_liu_wei_2022]
- [Zhong, 2022, Enriching Compiler Testing with Real Program from Bug Report][research_zhong_2022]
- [Groce and others, 2022, Making no-fuss compiler fuzzing effective][research_groce_vantonder_2022]
- [Tu and others, 2022, Remgen Remanufacturing a Random Program Generator for Compiler Testing][research_tu_jiang_2022]
- [Wang and others, 2022, Unleashing Coveraged-Based Fuzzing Through Comprehensive, Efficient, and Faithful Exploitable-Bug Exposing][research_wang_lu_2022]
- [Kasampalis and others, 2021, Language-parametric compiler validation with application to LLVM][research_kasampalis_park_2021]
- [Hazimeh and others, 2021, Magma A Ground-Truth Fuzzing Benchmark][research_hazimeh_herrera_2021]
- [Stepanov and others, 2021, Type-Centric Kotlin Compiler Fuzzing Preserving Test Program Correctness by Preserving Types][research_stepanov_akhin_2021]
- [Xu and others, 2020, DSmith Compiler Fuzzing through Generative Deep Learning Model with Attention][research_xu_wang_2020]
- [Chen and others, 2020, Enhanced compiler bug isolation via memoized search][research_chen_ma_2020]
- [Kim and others, 2020, Finding Bugs in File Systems with an Extensible Fuzzing Framework][research_kim_xu_2020]
- [Marcozzi and others, 2019, Compiler fuzzing how much does it matter?][research_marcozzi_tang_2019]
- [Tang and others, 2019, Compiler testing a systematic literature analysis][research_tang_ren_2019]
- [Koroglu and Wotawa, 2019, Fully Automated Compiler Testing of a Reasoning Engine via Mutated Grammar Fuzzing][research_koroglu_wotawa_2019]
- [Li, 2019, Haskell Compiler Testing Automation Based on Equivalence-Modulo-Inputs Method][research_li_2019]
- [Jeong and others, 2019, Razzer Finding Kernel Race Bugs through Fuzzing][research_jeong_kim_2019]
- [Zaytsev, 2018, An industrial case study in compiler testing tool demo][research_zaytsev_2018]
- [Holmes and Groce, 2018, Causal Distance-Metric-Based Assistance for Debugging after Compiler Fuzzing][research_holmes_groce_2018]
- [Cummins and others, 2018, Compiler fuzzing through deep learning][research_cummins_petoumenos_2018]
- [Barany, 2018, Finding missed compiler optimizations by differential testing][research_barany_2018]
- [Chen, 2018, Learning to accelerate compiler testing][research_chen_2018]
- [Kargén and Shahmehri, 2018, Speeding Up Bug Finding using Focused Fuzzing][research_kargen_shahmehri_2018]
- [Jay and Miller, 2018, Structured random differential testing of instruction decoders][research_jay_miller_2018]
- [Julián-Iranzo and Rubio-Manzano, 2017, A sound and complete semantics for a similarity-based logic programming language][research_julianiranzo_rubiomanzano_2017]
- [Lidman and Svenningsson, 2017, Bridging Static and Dynamic Program Analysis using Fuzzy Logic][research_lidman_svenningsson_2017]
- [Wang and others, 2017, Faster mutation analysis via equivalence modulo states][research_wang_xiong_2017]
- [Zhang and others, 2017, Skeletal program enumeration for rigorous compiler testing][research_zhang_sun_2017]
- [ISHIURA, 2016, Compiler Fuzzing][research_ishiura_2016]
- [Alatawi and others, 2016, Generating source inputs for metamorphic testing using dynamic symbolic execution][research_alatawi_miller_2016]
- [Lidbury and others, 2015, Many-core compiler fuzzing][research_lidbury_lascu_2015]

### The calling convention itself has a literature, and it is mostly about stability

The article treats a calling convention as a design choice, which is the compiler author's view of it. The
larger literature treats it as an interface contract whose principal property is that it must not change,
because every separately compiled artefact already linked against it would break.
**That is the sense in which adding a discriminator to the return convention is expensive**, and it is a
cost the cardinality argument does not see. The cardinality argument says a wider convention is available.
The interface literature says a wider convention is a different convention, and that the cost of adopting it
falls on everything already compiled.

Keleusma is pre-1.0 and has no external artefacts to break, so the article is right that the cost is not yet
being paid. It will be, and the decision made now is the one that will be expensive to revisit.

- [Zapanov, 2025, Foreign Function Interface for Managed Runtime Systems with Lightweight Threading][research_zapanov_2025]
- [Nagata and others, 2024, Evaluation of Interoperability of CNN Models between MATLAB and Python Environments Using ONNX Runtime Model][research_nagata_sakata_2024]
- [Chichereau and others, 2024, Fully Integrated Quantum Method for Classical Register Allocation in LLVM][research_chichereau_vialle_2024]
- [Terci, 2023, A Learning-Based Coloring Algorithm for Register Allocation Problem][research_terci_2023]
- [Panigrahi and Karfa, 2023, An Investigation into the Security of Register Allocation with Spilling and Splitting][research_panigrahi_karfa_2023_2]
- [Petrosino and others, 2023, Cross-Paradigm Interoperability Between Jadescript and Java][research_petrosino_monica_2023]
- [Hammond and others, 2023, MPI Application Binary Interface Standardization][research_hammond_dalcin_2023]
- [Xiao and others, 2023, Read-Write Dependency Aware Register Allocation][research_xiao_chen_2023]
- [Fried and others, 2023, Register Allocation for Compressed ISAs in LLVM][research_fried_stemmergrabow_2023]
- [VenkataKeerthy and others, 2023, RL4ReAl Reinforcement Learning for Register Allocation][research_venkatakeerthy_jain_2023]
- [Tant and others, 2023, Software Compilation Using FPGA Hardware Register Allocation][research_tant_diwakar_2023]
- [De Paula and Ierusalimschy, 2022, A Foreign Function Interface for Pallene][research_depaula_ierusalimschy_2022]
- [Chen and others, 2022, Register allocation compilation technique for ASIP in 5G micro base stations][research_chen_liu_2022]
- [Hu and others, 2022, Research on global register allocation for code containing array-unit dual-usage register names][research_hu_zhang_2022]
- [Wu and others, 2021, Effective Register Allocation for Configurable VLIW Crypto-Processor][research_wu_bie_2021]
- [Das and others, 2020, Deep Learning-based Approximate Graph-Coloring Algorithm for Register Allocation][research_das_ahmad_2020]
- [Doronin, 2019, PROBLEM RESEARCH AND DEVELOPMENT OF A TOOL FOR CHECKING APPLICATION BINARY INTERFACE COMPATIBILITY OF VIRTUAL METHOD TABLES][research_doronin_2019]
- [Yallop and others, 2018, A modular foreign function interface][research_yallop_sheets_2018]
- [Rath and others, 2018, Interoperability-Guided Testing of QUIC Implementations using Symbolic Execution][research_rath_schemmel_2018]
- [Eisl and others, 2018, Parallel trace register allocation][research_eisl_leopoldseder_2018]
- [Bee and bernardo, 2018, Predicting Fork Visibility Performance on Programming Language Interoperability in Open Source Projects][research_bee_bernardo_2018]
- [Caldwell and Chiba, 2017, Reducing calling convention overhead in object-oriented programming on embedded ARM thumb-2 platforms][research_caldwell_chiba_2017]
- [Carlotto and others, 2016, Interoperability of Annotation Schemes Using the Pepper Framework to Display AWA Documents in the ANNIS Interface][research_carlotto_beloki_2016]
- [Lozano and others, 2016, Register allocation and instruction scheduling in Unison][research_lozano_carlsson_2016]
- [Domagała and others, 2016, Register allocation and promotion through combined instruction scheduling and loop unrolling][research_domagala_vanamstel_2016]
- [Burroughs, 2016, Register allocation and spilling using the expected distance heuristic][research_burroughs_2016]
- [Eisl and others, 2016, Trace-based Register Allocation in a JIT Compiler][research_eisl_grimmer_2016]
- [Sukha, 2015, A Compiler-Runtime Application Binary Interface for Pipe-While Loops][research_sukha_2015]
- [Inoue and Kaneko, 2015, Bitwidth-aware register allocation and binding for clock period minimization][research_inoue_kaneko_2015]
- [Krause, 2015, Bytewise Register Allocation][research_krause_2015]
- [Ditu, 2015, Model-Based Function Call Code Generation and Stack Management in Retargetable Compilers Application Binary Interface Modeling of Stack Layout and Function Call Sequence][research_ditu_2015]
- [Eisl, 2015, Trace register allocation][research_eisl_2015]
- [You and Chen, 2015, Vector-aware register allocation for GPU shader processors][research_you_chen_2015]

### Static analysis supplies the vocabulary for a rule stricter than its property

The rule this article examines admits 14 of 24 chunks while the property it enforces holds for all 24, which
is a soundness-preserving imprecision. The literature that names this condition, measures it and reduces it
is large and the article uses only one paper from it.

**The article's position within this literature is unusual and worth being explicit about.** The classical
justification for an over-strict rule is that the exact property is uncomputable, so an approximation is
forced. This article's property is decidable on straight-line bytecode by summing two integers, so the
imprecision is not forced and the rule is simply cruder than it needs to be. That is a better position to be
in than the classical one and it is a different problem.

- [Iyenghar and others, 2026, Incremental Static Analysis for Detecting and Refactoring Data Clumps in TypeScript][research_iyenghar_baumgartner_2026]
- [Bardonek and Zachariasova, 2026, Leveraging design static analysis for vertical reuse Analytical interpretation and scalability behavior][research_bardonek_zachariasova_2026]
- [Negrini, 2026, Whole-value analysis by abstract interpretation][research_negrini_2026]
- [Dimovski, 2025, Imperative Program Synthesis by Abstract Static Analysis and SMT Mutations][research_dimovski_2025]
- [Azmi, 2025, LLM-Aware Static Analysis Adapting Program Analysis to Mixed Human/AI Codebases at Scale][research_azmi_2025]
- [Berg and others, 2025, Manim-DFA Visualising Data Flow Analysis and Abstract Interpretation Algorithms with Automated Video Generation][research_berg_yernaux_2025]
- [Urban and others, 2025, Static analysis by abstract interpretation against data leakage in machine learning][research_urban_subotic_2025]
- [Simonnet and others, 2024, A Dependent Nominal Physical Type System for Static Analysis of Memory in Low Level Code][research_simonnet_lemerre_2024]
- [Baek and Lee, 2024, CaLLi OCaml library for static analysis of LLVM bitcode][research_baek_lee_2024]
- [Guan and Treude, 2024, Enhancing Source Code Representations for Deep Learning with Static Analysis][research_guan_treude_2024]
- [Sharma and Sharma, 2024, Parameterized Static Analysis for Weak Memory Models][research_sharma_sharma_2024]
- [Liu and others, 2024, Research on Higher-Order Operator Transformation Algorithms for Syntax Transformation-Based Model Checking][research_liu_liu_2024]
- [Taft, 2024, Sound and precise static analysis using a generalization of static single assignment and value numbering][research_taft_2024]
- [Schnakenbeck and others, 2023, A Control Flow based Static Analysis of GRAFCET using Abstract Interpretation][research_schnakenbeck_mross_2023]
- [Coward and others, 2023, Combining E-Graphs with Abstract Interpretation][research_coward_constantinides_2023]
- [Wei and others, 2023, Compiling Parallel Symbolic Execution with Continuations][research_wei_jia_2023]
- [Barai and others, 2023, LLVM Static Analysis for Program Characterization and Memory Reuse Profile Estimation][research_barai_santhi_2023]
- [JANA, 2023, Sensitive Information Leakage Analysis of Database Code by Abstract Interpretation][research_jana_2023]
- [Haas and others, 2023, Static Analysis of Memory Models for SMT Encodings][research_haas_maseli_2023]
- [Bau and others, 2022, Abstract interpretation of Michelson smart-contracts][research_bau_mine_2022]
- [Lu and others, 2022, Gradual Soundness Lessons from Static Python][research_lu_greenman_2022]
- [Yang and others, 2022, Simulink Model Static Analysis Results based on Abstract Interpretation][research_yang_wang_2022]
- [Bartsch and others, 2021, Compositional Fault Propagation Analysis in Embedded Systems using Abstract Interpretation][research_bartsch_wilhelm_2021]
- [Shimchik and others, 2021, Improving Accuracy and Completeness of Source Code Static Taint Analysis][research_shimchik_ignatyev_2021]
- [Dimovski, 2021, Lifted termination analysis by abstract interpretation and its applications][research_dimovski_2021]
- [Punnoose, 2020, Ensuring completeness of formal verification with Gap Free Verification][research_punnoose_2020]
- [Wang and others, 2020, RSDS Getting System Call Whitelist for Container Through Dynamic and Static Analysis][research_wang_shen_2020]
- [van Tonder and Le Goues, 2020, Tailoring programs for static analysis via program transformation][research_vantonder_legoues_2020]
- [Yamane and others, 2020, Verification Method of Safety Properties of Embedded Assembly Program by Combining SMT-Based Bounded Model Checking and Reduction of Interrupt Handler Executions][research_yamane_kobashi_2020]
- [Bhushan and Yadav, 2020, Verification of Virtual Machine Architecture in a Hypervisor through Model Checking][research_bhushan_yadav_2020]
- [Sato and others, 2019, Combining higher-order model checking with refinement type inference][research_sato_iwayama_2019]
- [Meyer and Wolff, 2019, Decoupling lock-free data structures from memory reclamation for static analysis][research_meyer_wolff_2019]
- [Blaß and Philippsen, 2019, GPU-accelerated fixpoint algorithms for faster compiler analyses][research_blass_philippsen_2019]
- [Loring and others, 2019, Sound regular expression semantics for dynamic symbolic execution of JavaScript][research_loring_mitchell_2019]
- [Dong, 2018, A sound abstract memory model for static analysis of C programs][research_dong_2018]
- [Keidel and others, 2018, Compositional soundness proofs of abstract interpreters][research_keidel_poulsen_2018]
- [Gerasimov, 2018, Directed Dynamic Symbolic Execution for Static Analysis Warnings Confirmation][research_gerasimov_2018]
- [Roşu, 2018, Finite-trace linear temporal logic coinductive completeness][research_rosu_2018]
- [Sherman, 2018, Redesigning Soot's data-flow analysis framework for abstract interpretation][research_sherman_2018]
- [Alkhalid and Labiche, 2018, Towards GUI Functional Verification using Abstract Interpretation][research_alkhalid_labiche_2018]
- [Liang and others, 2017, Improving the precision of static analysis Symbolic execution based on GCC abstract syntax tree][research_liang_liu_2017]
- [Kobayashi and others, 2017, On the relationship between higher-order recursion schemes and higher-order fixpoint logic][research_kobayashi_lozes_2017]
- [Orlov, 2017, Program Source Code Static Analysis for Memory Access Error Detection Using Backwards Execution][research_orlov_2017]
- [Kusano and Wang, 2017, Thread-modular static analysis for relaxed memory models][research_kusano_wang_2017]
- [Miné, 2017, Tutorial on Static Inference of Numeric Invariants by Abstract Interpretation][research_mine_2017]
- [Suwa and others, 2017, Verification of code generators via higher-order model checking][research_suwa_tsukada_2017]
- [Haase, 2016, Abstract Interpretation of Java Bytecode for Immutability Analysis][research_haase_2016]
- [Ouadjaout and others, 2016, Static analysis by abstract interpretation of functional properties of device drivers in TinyOS][research_ouadjaout_mine_2016]
- [Simon and Kowalewski, 2016, Static analysis of Sequential Function Charts using abstract interpretation][research_simon_kowalewski_2016]
- [Bodin and others, 2015, Certified Abstract Interpretation with Pretty-Big-Step Semantics][research_bodin_jensen_2015]
- [Zhang and Koutsoukos, 2015, Improving the Precision of Abstract Interpretation Based Cache Persistence Analysis][research_zhang_koutsoukos_2015]
- [Cousot, 2015, On Various Abstract Understandings of Abstract Interpretation][research_cousot_2015]
- [Dong, 2015, RSTVL A Sound Abstract Memory Model for Program Static Analysis][research_dong_2015]
- [Montenegro and others, 2015, Space consumption analysis by abstract interpretation Reductivity properties][research_montenegro_pena_2015]
- [Bertrane and others, 2015, Static Analysis and Verification of Aerospace Software by Abstract Interpretation][research_bertrane_cousot_2015]
- [Cousot, 2015, Verification by abstract interpretation, soundness and abstract induction][research_cousot_2015_2]

### The bytecode layer is where the property is actually decidable

The backend consumes a verified bytecode, and the whole argument about stack effects lives at that level and
not at the source or the machine level. The virtual-machine literature is therefore where the article's
decidability claim has to be checked, and it is also the differential oracle's other side, since the oracle
compares the virtual machine against the native code.

- [Parashar and others, 2026, A Comparative Architectural and Performance Analysis of WebAssembly and JavaScript for Computationally Intensive Web Applications][research_parashar_kumawat_2026]
- [Corrias and others, 2026, An Analysis of Modern Web Security Vulnerabilities Inside WebAssembly Applications][research_corrias_pisu_2026]
- [Israel and others, 2026, Exploring WebAssembly as a Runtime Platform for Safety-Critical Edge Systems][research_israel_r_2026]
- [I.Saetchnikov and others, 2026, Microresonator clusters for spectral analysis with machine-learning interpreter][research_isaetchnikov_etcherniavskaia_2026]
- [Hu and others, 2026, QJWasm A lightweight runtime system for efficient WebAssembly execution in resource-constrained environments][research_hu_gu_2026]
- [Wu and others, 2026, Reconfigurable Computing Challenge FPGA-Based WebAssembly Stack Co-Processor][research_wu_liu_2026]
- [Choi and Jeon, 2026, Stack-based static WebAssembly binary slicing and mutation for generating valid sub-binaries][research_choi_jeon_2026]
- [Parra, 2026, SurtGIS A high-performance raster geospatial analysis library in Rust with WebAssembly and Python support][research_parra_2026]
- [Blaak and Van Cutsem, 2026, Towards Least-Privilege WebAssembly Applications Transparent Interposition for WebAssembly Components][research_blaak_vancutsem_2026]
- [Müller and others, 2026, WasmWeaver A Framework for Runtime-Aware WebAssembly Program Generation with Reinforcement Learning][research_muller_mane_2026]
- [Massey and Olivier, 2026, WASP Stack protection for WebAssembly][research_massey_olivier_2026]
- [Ţălu, 2025, A Comparative Study of WebAssembly Runtimes Performance Metrics, Integration Challenges, Application Domains, and Security Features][research_talu_2025]
- [Stepanov and Klym, 2025, A QUANTITATIVE ANALYSIS OF WEBASSEMBLY INTEGRATION ARCHITECTURAL PATTERNS, TOOLING, AND PERFORMANCE EVALUATION][research_stepanov_klym_2025]
- [Moskalenko, 2025, Application of WebAssembly for High-Performance Client-Side Media Content Analysis][research_moskalenko_2025]
- [Watt, 2025, Concurrency in WebAssembly][research_watt_2025]
- [Subramanyan, 2025, CWAMR REIMAGINING A CAPABILITYBASED WEBASSEMBLY RUNTIME VIA CHERI-BASED COMPARTMENTALIZATION][research_subramanyan_2025]
- [Lu and others, 2025, Detecting WebAssembly Runtime Bugs With Grammar-Guided Program Mutation][research_lu_zhou_2025]
- [Jiang and others, 2025, Distinguishability-Guided Test Program Generation for WebAssembly Runtime Performance Testing][research_jiang_zeng_2025]
- [SanthiKumar and others, 2025, Enhancing Machine Learning Performance with AI-Based Virtual Machine Load Balancing][research_santhikumar_sahayasheela_2025]
- [Schlägl and Groβe, 2025, Fast Interpreter-Based Instruction Set Simulation for Virtual Prototypes][research_schlagl_groe_2025]
- [Lei and others, 2025, Furina A Light-weight WebAssembly Runtime for ICS][research_lei_li_2025]
- [Kang and others, 2025, HybridServe Adaptive WebAssembly-Container Runtime Selection for Edge Serverless Computing][research_kang_song_2025]
- [Mallawarachchi and Jayaweera, 2025, Implementation of Wyltl An Imperative Language with a Dual Interpreter Compiler Architecture][research_mallawarachchi_jayaweera_2025]
- [Marcelino and others, 2025, Lumos Performance Characterization of WebAssembly as a Serverless Runtime in the Edge-Cloud Continuum][research_marcelino_krennmair_2025]
- [Kakati and Brorsson, 2025, Performance and Usability Implications of Multiplatform and WebAssembly Containers][research_kakati_brorsson_2025]
- [MIDZIC and NOVAK, 2025, Performance Comparison of WebAssembly and Phaser in Procedural Maze Generation][research_midzic_novak_2025]
- [Kim and others, 2025, Pre-trained Models for Bytecode Instructions][research_kim_kim_2025]
- [Soluian and Lіushenko, 2025, Research of WebAssembly usage for high-performance code development in web applications][research_soluian_lushenko_2025]
- [Mao and others, 2025, Research on a Lightweight Full-Stack Edge Execution Optimization Framework Based on Serverless and WebAssembly][research_mao_chen_2025]
- [Matsubara and others, 2025, Seamless Self-Healing in WebAssembly Container Orchestration with Runtime-Neutral Checkpointing][research_matsubara_saito_2025]
- [Nakata and Matsubara, 2025, Self-Hosted WebAssembly Runtime for Runtime-Neutral Checkpoint/Restore in Edge-Cloud Continuum][research_nakata_matsubara_2025]
- [Satya Teja Muddada, 2025, Serverless 2.0 Unlocking Performance and Portability with WebAssembly][research_satyatejamuddada_2025]
- [Bhoyar and others, 2025, Sign Language Interpreter using Long Short-Term Memory LSTM][research_bhoyar_jain_2025]
- [Parwez and others, 2025, Signease Machine Learning Based Sign Language Interpreter][research_parwez_abrar_2025]
- [Dico and Tata Sutabri, 2025, Virtual Desktop Infrastructure Sebagai Pendukung Perkuliahan Dengan Algoritma Virtual Machine][research_dico_tatasutabri_2025]
- [Liu and others, 2025, WebAssembly for Container Runtime Are We There Yet?][research_liu_shen_2025]
- [Karpovich and Gosudarev, 2025, WebAssembly performance in the Node.js environment][research_karpovich_gosudarev_2025]
- [Titzer, 2025, WebAssembly How Low Can a Bytecode Go?][research_titzer_2025]
- [Krishnamoorthy, 2025, WEBASSEMBLY REVOLUTIONIZING WEB PERFORMANCE AND EXPANDING FRONTIERS OF BROWSER-BASED APPLICATIONS][research_krishnamoorthy_2025]
- [Heinrich and others, 2024, A Categorical Data Approach for Anomaly Detection in WebAssembly Applications][research_heinrich_will_2024]
- [Ménétrey and others, 2024, A Comprehensive Trusted Runtime for WebAssembly With Intel SGX][research_menetrey_pasin_2024]
- [Massidda and others, 2024, Bringing Binary Exploitation at Port 80 Understanding C Vulnerabilities in WebAssembly][research_massidda_pisu_2024]
- [A and others, 2024, Design of Mechatronics Based Virtual Telepresence for Robotic System Using Raspberry Python Interpreter][research_a_s_2024]
- [Silva and others, 2024, Efficient Data Exchange between WebAssembly Modules][research_silva_metrolho_2024]
- [Bunkenburg and Wu, 2024, Making a Curry Interpreter using Effects and Handlers][research_bunkenburg_wu_2024]
- [Michaud and others, 2024, Robust Stack Smashing Protection for WebAssembly][research_michaud_pipereau_2024]
- [Harnes and Morrison, 2024, SoK Analysis Techniques for WebAssembly][research_harnes_morrison_2024]
- [Zhao and others, 2024, Wapplique Testing WebAssembly Runtime via Execution Context-Aware Bytecode Mutation][research_zhao_zeng_2024]
- [Nikhil Sripathi Rao, 2024, WebAssembly Revolutionizing Web User Interface Development through Performance and Cross-Language Integration][research_nikhilsripathirao_2024]
- [Wang and others, 2023, A Comprehensive Study of WebAssembly Runtime Bugs][research_wang_zhou_2023]
- [Verma and others, 2023, Array Bytecode Support in MicroJIT][research_verma_kaur_2023]
- [Rosà and others, 2023, Automated Runtime Transition between Virtual and Platform Threads in the Java Virtual Machine][research_rosa_basso_2023]
- [Park and others, 2023, Bespoke Virtual Machine Orchestrator An Approach for Constructing and Reconfiguring Bespoke Virtual Machine in Private Cloud Environment][research_park_jeong_2023]
- [Zhang and others, 2023, Characterizing and Detecting WebAssembly Runtime Bugs][research_zhang_cao_2023]
- [Lowther and others, 2023, CHERI Performance Enhancement for a Bytecode Interpreter][research_lowther_jacob_2023]
- [Pockstaller and others, 2023, Comparing the Energy Consumption of WebAssembly and JavaScript in Mobile Browsers][research_pockstaller_huber_2023]
- [Marcelino and Nastic, 2023, CWASI A WebAssembly Runtime Shim for Inter-function Communication in the Serverless Edge-Cloud Continuum][research_marcelino_nastic_2023]
- [He and others, 2023, Neural-FEBI Accurate function identification in Ethereum Virtual Machine bytecode][research_he_li_2023]
- [Vepuri and Jiang, 2023, Performance Analysis of Virtual Machine Monitoring System][research_vepuri_jiang_2023]
- [Chung Seo and Kim, 2023, Portable and Efficient Implementation of CRYSTALS-Kyber Based on WebAssembly][research_chungseo_kim_2023]
- [Rokotyanskaya and Abramov, 2023, Studying WebAssembly and comparison of its performance with JavaScript][research_rokotyanskaya_abramov_2023]
- [Johnson and others, 2023, WaVe a verifiably secure WebAssembly sandboxing runtime][research_johnson_laufer_2023]
- [Romano and Wang, 2023, When Function Inlining Meets WebAssembly Counterintuitive Impacts on Runtime Performance][research_romano_wang_2023]
- [Kovačević and others, 2022, Automatic compiler/interpreter generation from programs for Domain-Specific Languages Code bloat problem and performance improvement][research_kovacevic_ravber_2022]
- [Othman and El Ghoul, 2022, BuHamad - The first Qatari virtual interpreter for Qatari Sign Language][research_othman_elghoul_2022]
- [Kyriakou and Tselikas, 2022, Complementing JavaScript in High-Performance Node.js and Web Applications with Rust and WebAssembly][research_kyriakou_tselikas_2022]
- [Sahkhar and others, 2022, Efficient Cloudlet Allocation to Virtual Machine to Impact Cloud System Performance][research_sahkhar_balabantaray_2022]
- [Lehmann and Pradel, 2022, Finding the Dwarf Recovering Precise Types from WebAssembly Binaries][research_lehmann_pradel_2022]
- [Anderton, 2022, Investigating Sign Language Interpreter Rendering and Guiding Methods in Virtual Reality 360-Degree Content][research_anderton_2022]
- [Sai and others, 2022, Machine learning-based malware detection using stacking of opcodes and bytecode sequences][research_sai_tyagi_2022]
- [Jodogne, 2022, Rendering Medical Images using WebAssembly][research_jodogne_2022]
- [Stiévenart and others, 2022, Static stack-preserving intra-procedural slicing of webassembly binaries][research_stievenart_binkley_2022]
- [Chmiel and Spinolo, 2022, Testing the impact of remote interpreting settings on interpreter experience and performance][research_chmiel_spinolo_2022]
- [Thorpe and others, 2022, Verification of Cyber Emulation Experiments Through Virtual Machine and Host Metrics][research_thorpe_swiler_2022]
- [Menetrey and others, 2022, WaTZ A Trusted WebAssembly Runtime Environment with Remote Attestation for TrustZone][research_menetrey_pasin_2022]
- [De Macedo and others, 2022, WebAssembly versus JavaScript Energy and Runtime Performance][research_demacedo_abreu_2022]
- [Thorpe and others, 2022, WiP Verification of Cyber Emulation Experiments Through Virtual Machine and Host Metrics][research_thorpe_swiler_2022_2]
- [Zhang and Yin, 2021, A Virtual Machine Placement Strategy Based on Virtual Machine Selection and Integration][research_zhang_yin_2021]
- [Wang, 2021, Can "micro VM" become the next generation computing platform? Performance comparison between light weight Virtual Machine, container, and traditional Virtual Machine][research_wang_2021]
- [M and Murugesh, 2021, Comparative Study of Binary Classification Algorithms to Analyze the Students Performance on Virtual Machine][research_m_murugesh_2021]
- [Penev and Dimitrov, 2021, Design of a Virtual Machine for Training Compilers][research_penev_dimitrov_2021]
- [Hara and others, 2021, Machine-learning Approach using Solidity Bytecode for Smart-contract Honeypot Detection in the Ethereum][research_hara_takahashi_2021]
- [De Macedo and others, 2021, On the Runtime and Energy Performance of WebAssembly Is WebAssembly superior to JavaScript yet?][research_demacedo_abreu_2021]
- [Menetrey and others, 2021, Twine An Embedded Trusted Runtime for WebAssembly][research_menetrey_pasin_2021]
- [-, 2021, WebAssembly for High-Performance Web Applications A Study on Execution Speed and Efficiency][research_webassembly_for_high_performance_2021]
- [Ke and Chen, 2020, Instruction Verification of Ethereum Virtual Machine by Formal Method][research_ke_chen_2020]
- [Bockisch and others, 2020, Java Bytecode Verification with OCL Why, How and Whenc][research_bockisch_taentzer_2020]
- [E., 2020, Modified Support Vector Machine based Efficient Virtual Machine Consolidation Procedure for Cloud Data Centers][research_e_2020]
- [Wahyudi and Miswanto, 2020, VIRTUAL MACHINE FORENSIC ANALYSIS and RECOVERY VMFAR SEBAGAI FRAMEWORK UNTUK ANALISIS BUKTI DIGITAL PADA VIRTUAL MACHINE][research_wahyudi_miswanto_2020]
- [Pinckney and others, 2020, Wasm/k delimited continuations for WebAssembly][research_pinckney_guha_2020]
- [V and others, 2019, A WEIGHTED ENSEMBLE OF AUTOMATIC ALGORITHMS FOR VIRTUAL MACHINE PERFORMANCE PREDICTION IN CLOUD][research_v_m_2019]
- [Choi and Hong, 2019, Design and implementation of virtual machine control and streaming scheme using Linux kernel-based virtual machine hypercall for virtual mobile infrastructure][research_choi_hong_2019]
- [Zheng and Xia, 2019, Exploring mixed integer programming reformulations for virtual machine placement with disk anti-colocation constraints][research_zheng_xia_2019]
- [Cabrera Arteaga and others, 2019, Scalable comparison of JavaScript V8 bytecode traces][research_cabreraarteaga_monperrus_2019]
- [Salim and others, 2019, Towards a WebAssembly standalone runtime on GraalVM][research_salim_nisbet_2019]
- [Moliavko and others, 2019, uJVM Lightweight Java Virtual Machine for embedded systems][research_moliavko_drozdovskyi_2019]
- [Achour and others, 2018, A Constraint-Based Verification Approach for Java Bytecode Programs][research_achour_chouenyib_2018]
- [Park and others, 2018, A formal verification tool for Ethereum VM bytecode][research_park_zhang_2018]
- [Liu and Li, 2018, A novel virtual machine scheduling policy based on performance prediction model][research_liu_li_2018]
- [Sohrabi and others, 2018, A Novel Virtual Machine Selection Policy for Virtual Machine Consolidation][research_sohrabi_ghods_2018]
- [Kim and Lee, 2018, A Study on the Code Generator for a Virtual Machine Code based JavaScript Compiler][research_kim_lee_2018]
- [Melo Alves and others, 2018, An Interference-Aware Virtual Machine Placement Strategy for High Performance Computing Applications in Clouds][research_meloalves_teylo_2018]
- [Achour and Benattou, 2018, Constraint Based Testing and Verification of Java Bytecode Programs][research_achour_benattou_2018]
- [Jamil, 2018, Design of a Real-Time Interpreter for Arabic Sign Language][research_jamil_2018]
- [Attrapadung and others, 2018, Efficient Two-level Homomorphic Encryption in Prime-order Bilinear Groups and A Fast Implementation in WebAssembly][research_attrapadung_hanaoka_2018]
- [Kuang and others, 2018, Enhance virtual-machine-based code obfuscation security through dynamic bytecode scheduling][research_kuang_tang_2018]
- [Yang, 2018, Formal Process Virtual Machine for Smart Contracts Verification][research_yang_2018]
- [Hale and others, 2018, Interpreter performance in police interviews. Differences between trained interpreters and untrained bilinguals][research_hale_goodmandelahunty_2018]
- [Dobravec, 2018, JAVA BYTECODE INSTRUCTION USAGE COUNTING WITH ALGATOR][research_dobravec_2018]
- [V. Samuel Blessed Nayagam and Shajin Nargunam, 2018, Secure Data Verification and Virtual Machine Monitoring][research_vsamuelblessednayagam_shajinnargunam_2018]
- [Madsen and others, 2018, Tail call elimination and data representation for functional languages on the Java virtual machine][research_madsen_zarifi_2018]
- [Sianipar and others, 2018, Virtual Machine Integrity Verification in Crowd-Resourcing Virtual Laboratory][research_sianipar_willems_2018]
- [Kim and Lee, 2017, A Study on the Light-Weight Virtual Machine Code for IoT Virtual Machine][research_kim_lee_2017]
- [Haas and others, 2017, Bringing the web up to speed with WebAssembly][research_haas_rossberg_2017]
- [Son and others, 2017, Design and Implementation of the RSIL to LLVM IR Translator for Verification of the Intermediate Code on IoT Virtual Machine][research_son_oh_2017]
- [Lee and others, 2017, Design and implementation of the secure compiler and virtual machine for developing secure IoT services][research_lee_jeong_2017]
- [Lee, 2017, Exploring a relationship between students' interpreting self-efficacy and performance triangulating data on interpreter performance assessment][research_lee_2017]
- [Sheinidashtegol and Galloway, 2017, Performance Impact of DDoS Attacks on Three Virtual Machine Hypervisors][research_sheinidashtegol_galloway_2017]
- [2017, The Utilization of Cloud Computing as Virtual Machine][research_the_utilization_2017]
- [2017, Virtual Machine Consolidation using Load Balancing algorithm in Cloud Data Center][research_virtual_machine_2017]
- [Son and Lee, 2016, A Study on the Interpreter for the Light-Weighted Virtual Machine on IoT Environments][research_son_lee_2016]
- [2016, Analytics of Application Resource Utilization within the Virtual Machine][research_analytics_of_2016]
- [Han, 2016, Building the validity foundation for interpreter certification performance testing][research_han_2016]
- [2016, Comparative Study of Virtual Machine Migration Techniques and Challenges in Post Copy Live Virtual Machine Migration][research_comparative_study_2016]
- [Cheng and others, 2016, Formalised EMFTVM bytecode language for sound verification of model transformations][research_cheng_monahan_2016]
- [Tokumoto and others, 2016, MuVM Higher Order Mutation Analysis Virtual Machine for C][research_tokumoto_yoshida_2016]
- [2016, Network-Aware Virtual Machine Placement in the Cloud][research_network_aware_virtual_2016]
- [CLERC, 2016, OCaml-Java The Java Virtual Machine as the target of an OCaml compiler][research_clerc_2016]
- [Zhou and Mu, 2016, Representative Virtual Machine Templates An optimized virtual machine templates management mechanism for an Cloud system based on K-medoids Clustering][research_zhou_mu_2016]
- [O'Loughlin and Gillam, 2015, Addressing Issues of Cloud Resilience, Security and Performance through Simple Detection of Co-locating Sibling Virtual Machine Instances][research_oloughlin_gillam_2015]
- [Nanthaamornphong and others, 2015, Bytecode-based class dependency extraction tool Bytecode-CDET][research_nanthaamornphong_leatongkam_2015]
- [Upadhyaya and Rajan, 2015, Effectively mapping linguistic abstractions for message-passing concurrency to threads on the Java virtual machine][research_upadhyaya_rajan_2015]
- [Gunadi, 2015, Formal Certification of Non-interferent Android Bytecode DEX Bytecode][research_gunadi_2015]
- [Salapura and Harper, 2015, High Performance Virtual Machine Recovery in the Cloud][research_salapura_harper_2015]
- [Pan and others, 2015, Nonvolatile main memory aware garbage collection in high-level language virtual machine][research_pan_xie_2015]
- [Galloway and others, 2015, Performance Metrics of Virtual Machine Live Migration][research_galloway_loewen_2015]
- [Ruan and Chen, 2015, Performance-to-Power Ratio Aware Virtual Machine VM Allocation in Energy-Efficient Clouds][research_ruan_chen_2015]
- [Salapura and Harper, 2015, Remote Restart for a High Performance Virtual Machine Recovery in a Cloud][research_salapura_harper_2015_2]
- [2015, The Deasibility and Properties of Dividing Virtual Machine Resources using the Virtual Machine Cluster as the Unit in Cloud Computing][research_the_deasibility_2015]
- [Hui Zhao and others, 2015, Virtual machine placement based on the VM performance models in cloud][research_huizhao_zheng_2015]

### Types and semantics decide whether the question arises at all

The observation the article contributes is that two source forms have different trace alphabets, which is a
statement about the source language's type system before it is a statement about the backend. A language
whose types separate a stream from a terminating coroutine can select the convention per form. A language
whose types do not cannot, and must widen the convention globally or pay for a general mechanism.
**The type system is therefore the mechanism by which the choice becomes available**, and the literature on
what type systems can express about control effects is where the boundary of that availability is drawn.

- [Arendsee, 2026, morloc a workflow language for multi-lingual programming under a common type system][research_arendsee_2026]
- [DOWNEN and ARIOLA, 2025, A contextual formalization of structural coinduction][research_downen_ariola_2025]
- [Baramashetru and others, 2025, A Type System for Data Privacy Compliance in Active Object Languages][research_baramashetru_giannini_2025]
- [Correnson and Finkbeiner, 2025, Coinductive Proofs for Temporal Hyperliveness][research_correnson_finkbeiner_2025]
- [Kolesar and others, 2025, Coinductive Proofs of Regular Expression Equivalence in Zero Knowledge][research_kolesar_ali_2025]
- [Di Lavore and others, 2025, Coinductive Streams in Monoidal Categories][research_dilavore_defelice_2025]
- [Kidney and Wu, 2025, Formalising Graph Algorithms with Coinduction][research_kidney_wu_2025]
- [Lee and others, 2025, React-tRace A Semantics for Understanding React Hooks An Operational Semantics and a Visualizer for Clarifying React Hooks][research_lee_ahn_2025]
- [Hyvernat, 2025, The Size-Change Principle for Mixed Inductive and Coinductive types][research_hyvernat_2025]
- [Hyvernat, 2025, Totality for Mixed Inductive and Coinductive Types][research_hyvernat_2025_2]
- [Dinikeev, 2025, Type system for a statically typed concatenative programming language with first class function support][research_dinikeev_2025]
- [Smith and Zhang, 2024, A Pure Demand Operational Semantics with Applications to Program Analysis][research_smith_zhang_2024]
- [Chawla and others, 2024, COMPARATIVE STUDY OF PROPOFOL AUTO-COINDUCTION VERSUS KETAMINE PROPOFOL COINDUCTION USING PRIMING PRINCIPLE BY BISPECTRAL INDEX ANALYSIS FOR DAY CARE SURGERY][research_chawla_goyal_2024]
- [Grabmayer, 2023, A Coinductive Reformulation of Milner's Proof System for Regular Expressions Modulo Bisimilarity][research_grabmayer_2023]
- [Francalanza and Tabone, 2023, ElixirST A session-based type system for Elixir modules][research_francalanza_tabone_2023]
- [Castagna and others, 2023, The Design Principles of the Elixir Type System][research_castagna_duboc_2023]
- [Milano and others, 2022, A flexible type system for fearless concurrency][research_milano_turcotti_2022]
- [Mastorou and others, 2022, Coinduction inductively mechanizing coinductive proofs in Liquid Haskell][research_mastorou_papaspyrou_2022]
- [Sangiorgi, 2022, From enhanced coinduction towards enhanced induction][research_sangiorgi_2022]
- [Lambert and others, 2022, Leveraging Compiler-Based Translation to Evaluate a Diversity of Exascale Platforms][research_lambert_monil_2022]
- [Kanatov and Zouev, 2022, Unified type system for the modern general-purpose programing language][research_kanatov_zouev_2022]
- [Mihelic and others, 2021, A denotational semantics of a concatenative/compositional programming language][research_mihelic_steingartner_2021]
- [De and others, 2021, Canonical proof-objects for coinductive programming infinets with infinitely many cuts][research_de_pellissier_2021]
- [Kuperberg and others, 2021, Coinductive Algorithms for Büchi Automata][research_kuperberg_pinault_2021]
- [Kupke and Rot, 2021, Expressive Logics for Coinductive Predicates][research_kupke_rot_2021]
- [Dagnino, 2021, Foundations of regular coinduction][research_dagnino_2021]
- [Farkas and others, 2021, Improving productivity in large scale testing at the compiler level by changing the intermediate language from C++ to Java][research_farkas_szabados_2021]
- [Sato, 2021, Proof Assistant and Type Theory][research_sato_2021]
- [2020, A Fibrational Method of Indexed Coinductive Data Types][research_a_fibrational_2020]
- [Cassola and others, 2020, A Gradual Type System for Elixir][research_cassola_talagorria_2020]
- [Czajka, 2020, A new coinductive confluence proof for infinitary lambda calculus][research_czajka_2020]
- [Zakowski and others, 2020, An equational theory for weak bisimulation via generalized parameterized coinduction][research_zakowski_he_2020]
- [Czajka, 2020, An operational interpretation of coinductive types][research_czajka_2020_2]
- [Dagnino, 2020, Coaxioms flexible coinductive definitions by inference systems][research_dagnino_2020]
- [Zúñiga and Bel-Enguix, 2020, Coinductive Natural Semantics for Compiler Verification in Coq][research_zuniga_belenguix_2020]
- [Abe, 2019, A type system for data independence of loop iterations in a directive-based PGAS language][research_abe_2019]
- [Inoue and Igarashi, 2019, A type system for first-class layers with inheritance, subtyping, and swapping][research_inoue_igarashi_2019]
- [Biernacki and others, 2019, Bisimulations for Delimited-Control Operators][research_biernacki_lenglet_2019]
- [Hirschowitz, 2019, Familial monads and structural operational semantics][research_hirschowitz_2019]
- [Yesua and others, 2019, Keamanan Penggunaan Propofol Auto-Coinduction Dibandingkan Dengan Midazolam Coinduction Berdasarkan Perubahan Hemodinamik Pada Induksi Anestesi Pasien Yang Dilakukan General Anestesi][research_yesua_rahardjo_2019]
- [Nishizaki, 2019, ML Polymorphism of Linear Lambda Calculus with First-class Continuations][research_nishizaki_2019]
- [Pelsmaeker and others, 2019, Towards language-parametric semantic editor services based on declarative type system specifications][research_pelsmaeker_vanantwerpen_2019]
- [Bosse, 2018, A Unified System Modelling and Programming Language based on JavaScript and a Semantic Type System][research_bosse_2018]
- [Gupta and Lewis, 2018, Neural Compositional Denotational Semantics for Question Answering][research_gupta_lewis_2018]
- [Lucanu, 2018, Proving Reachability Properties by Coinduction Extended Abstract][research_lucanu_2018]
- [Sokhatskyi and Maslianko, 2018, The systems engineering of consistent pure language with effect type system for certified applications and higher languages][research_sokhatskyi_maslianko_2018]
- [Komendantskaya and Li, 2018, Towards Coinductive Theory Exploration in Horn Clause Logic Position Paper][research_komendantskaya_li_2018]
- [Goncharov and others, 2018, Unguarded Recursion on Coinductive Resumptions][research_goncharov_schroder_2018]
- [Liu and others, 2017, Analyzing divergence in bisimulation semantics][research_liu_yu_2017]
- [Aristizábal and others, 2017, Environmental Bisimulations for Delimited-Control Operators with Dynamic Prompt Generation][research_aristizabal_biernacki_2017]
- [Harlin and others, 2017, Impact of Using a Static-Type System in Computer Programming][research_harlin_washizaki_2017]
- [Aparanji and others, 2017, INDUCTION OF PROPOFOL WITH COINDUCTION OF PROPOFOL, MIDAZOLAM VERSUS PROPOFOL AUTO COINDUCTION- A COMPARATIVE STUDY][research_aparanji_radhasundari_2017]
- [Nishizaki, 2017, Linear lambda calculus with non-linear first-class continuations][research_nishizaki_2017]
- [Nishizaki, 2017, Type Inference of Linear Lambda Calculus with First-Class Continuations][research_nishizaki_2017_2]
- [Berger and Spreen, 2016, A coinductive approach to computing with compact sets][research_berger_spreen_2016]
- [Swierstra and others, 2016, A Lazy Language Needs a Lazy Type System][research_swierstra_viera_2016]
- [Sculthorpe and others, 2016, A Modular Structural Operational Semantics for Delimited Continuations][research_sculthorpe_torrini_2016]
- [Pous, 2016, Coinduction All the Way Up][research_pous_2016]
- [KOZEN and SILVA, 2016, Practical coinduction][research_kozen_silva_2016]
- [Pattinson and Schröder, 2016, Program Equivalence is Coinductive][research_pattinson_schroder_2016]
- [Rot and others, 2016, Proving language inclusion and equivalence by coinduction][research_rot_bonsangue_2016]
- [Bruza, 2016, Syntax and operational semantics of a probabilistic programming language with scopes][research_bruza_2016]
- [Ciaffaglione, 2016, Towards Turing computability via coinduction][research_ciaffaglione_2016]
- [Basold and Geuvers, 2016, Type Theory based on Dependent Inductive and Coinductive Types][research_basold_geuvers_2016]
- [Nakata and Uustalu, 2015, A Hoare logic for the coinductive trace-based big-step semantics of While][research_nakata_uustalu_2015]
- [Gan and Li, 2015, Coinduction functor in representation stability theory][research_gan_li_2015]
- [Pous, 2015, Coinductive techniques, from automata to coalgebra][research_pous_2015]
- [Bonchi and Pous, 2015, Hacking nondeterminism with induction and coinduction][research_bonchi_pous_2015]
- [Schmidt-Schauß and Sabel, 2015, Improvements in a functional core language with call-by-need operational semantics][research_schmidtschauss_sabel_2015]

### Concurrency runtimes are where the general mechanism is affordable

The callback convention holds a frame across arbitrary host execution, which is what a runtime with a
scheduler does routinely and what a statically bounded artefact cannot do. The contrast is the article's
central trade seen from the other side, so the runtime literature is listed here as the case where the
general answer is correct.

- [Sharma and Reddy, 2025, Analysis of FreeRTOS and Contiki Scheduler Performance with Scalable Task Loads on a Uniform Platform][research_sharma_reddy_2025]
- [Sharma, 2025, Green Threads Human Connection with Nature in Richard Powers' The Overstory][research_sharma_2025]
- [Zhang and others, 2025, Refactoring for Java-Structured Concurrency][research_zhang_shen_2025]
- [Altassan and Ahmad, 2024, Green threads of change Unravelling the gendered and experienced moderators in the sustainable symphony of green HR practices and environmental responsibility][research_altassan_ahmad_2024]
- [Sadanand Giri and others, 2024, Green threads of progress Natural fibers reshaping wastewater cleanup strategies, a review][research_sadanandgiri_subash_2024]
- [Kim and Park, 2023, A Multi-core Based Real-time Scheduler Supporting Periodic and Sporadic Threads and Processes][research_kim_park_2023]
- [Serafin and others, 2023, Pipestitch An energy-minimal dataflow architecture with lightweight threads][research_serafin_ghosh_2023]
- [Jagnik, 2023, Structured Concurrency in Java][research_jagnik_2023]
- [Ciesko and Roussel, 2023, User-Level Threading for HPC Applications][research_ciesko_roussel_2023]
- [Zou and others, 2022, Buddy Stacks Protecting Return Addresses with Efficient Thread-Local Storage and Runtime Re-Randomization][research_zou_wang_2022]
- [Ueno and Ohori, 2022, Concurrent and parallel garbage collection for lightweight threads on multicore processors][research_ueno_ohori_2022]
- [Shiina and others, 2021, Lightweight preemptive user-level threads][research_shiina_iwasaki_2021]
- [Karsten and Barghi, 2020, User-level Threading][research_karsten_barghi_2020]
- [Carvalho and others, 2019, A dataflow runtime environment and static scheduler for edge, fog and in-situ computing][research_carvalho_ferreira_2019]
- [Iwasaki and others, 2018, Lessons Learned from Analyzing Dynamic Promotion for User-Level Threading][research_iwasaki_amer_2018]
- [Kalebe and others, 2017, A library for scheduling lightweight threads in Internet of Things microcontrollers][research_kalebe_girao_2017]
- [Huynh and Taura, 2017, Delay Spotter A Tool for Spotting Scheduler-Caused Delays in Task Parallel Runtime Systems][research_huynh_taura_2017]

### The historical layer

The clusters above are drawn from work published in 2015 or later, which is the survey's contemporary
window. The older records the harvest returned are listed here in one place instead of distributed through
the sections above, because for most of these clusters the pre-2015 work is the foundation the contemporary
work cites rather than a competing account. There are 679 of them.

- [Liu and others, 2011, Coroutine-Based Synthesis of Efficient Embedded Software From SystemC Models][research_liu_xu_2011]
- [Kristensen and others, 1987, Coroutine Sequencing in BETA][research_kristensen_mollerpedersen_1987]
- [Kearns and Lou Soffa, 1983, The implementation of retention in a coroutine environment][research_kearns_lousoffa_1983]
- [Bird, 1982, An implementation of a code generator specification language for table driven code generators][research_bird_1982]
- [Samet, 1980, A Coroutine Approach to Parsing][research_samet_1980]
- [Moody and Richards, 1980, A coroutine mechanism for BCPL][research_moody_richards_1980]
- [Pauli and Soffa, 1980, Coroutine behaviour and implementation][research_pauli_soffa_1980]
- [Donegan and others, 1979, A code generator generator language][research_donegan_noonan_1979]
- [Pritchard, 1976, A proof rule for multiple coroutine systems][research_pritchard_1976]
- [Hanson, 1976, A simple variant of the boundary-tag algorithm for the allocation of coroutine environments][research_hanson_1976]
- [Wang and Dahl, 1971, Coroutine sequencing in a block structured environment][research_wang_dahl_1971]

- [DOWNEN and ARIOLA, 2014, Delimited control and computational effects][research_downen_ariola_2014]
- [Ilik, 2014, Proofs in continuation-passing style][research_ilik_2014]
- [Ilik, 2013, Continuation-passing style models complete for intuitionistic logic][research_ilik_2013]
- [Ilik, 2013, Type Directed Partial Evaluation for Level-1 Shift and Reset][research_ilik_2013_2]
- [Kiselyov, 2012, Delimited control in OCaml, abstractly and concretely][research_kiselyov_2012]
- [Ilik, 2012, Delimited control operators prove Double-negation Shift][research_ilik_2012]
- [Thielecke, 2012, Functional semantics of parsing actions, and left recursion elimination as continuation passing][research_thielecke_2012]
- [Kerneis and Chroboczek, 2011, Continuation-Passing C, compiling threads to events through continuations][research_kerneis_chroboczek_2011]
- [Yu and Haque, 2011, Decentralised web-services orchestration with continuation-passing messaging][research_yu_haque_2011]
- [TARAU, 2011, The BinProlog experience Architecture and implementation choices for continuation passing Prolog and first-class logic engines][research_tarau_2011]
- [Kameyama and Tanaka, 2010, Equational axiomatization of call-by-name delimited control][research_kameyama_tanaka_2010]
- [Garcia and others, 2010, Lazy Evaluation and Delimited Control][research_garcia_lumsdaine_2010]
- [Santo and others, 2009, Continuation-Passing Style and Strong Normalisation for Intuitionistic Sequent Calculi][research_santo_matthes_2009]
- [Masuko and Asai, 2009, Direct implementation of shift and reset in the MinCaml compiler][research_masuko_asai_2009]
- [Garcia and others, 2009, Lazy evaluation and delimited control][research_garcia_lumsdaine_2009]
- [Guerrini and Masini, 2009, Proofs, tests and continuation passing style][research_guerrini_masini_2009]
- [Yu, 2009, Scalable Services Orchestration with Continuation-Passing Messaging][research_yu_2009]
- [Shan, 2007, A static simulation of dynamic delimited control][research_shan_2007]
- [Yu and Yang, 2007, Continuation-passing enactment of distributed recoverable workflows][research_yu_yang_2007]
- [Biernacki and others, 2006, A Dynamic Continuation-Passing Style for Dynamic Delimited Continuations][research_biernacki_danvy_2006]
- [BIERNACKI and DANVY, 2006, THEORETICAL PEARL A simple proof of a folklore theorem about delimited control][research_biernacki_danvy_2006_2]
- [Biernacki and others, 2005, A Dynamic Continuation-Passing Style for Dynamic Delimited Continuations][research_biernacki_danvy_2005]
- [Biernacki and others, 2005, A Dynamic Continuation-Passing Style for Dynamic Delimited Continuations Preliminary Version][research_biernacki_danvy_2005_2]
- [Biernacki and Danvy, 2005, A Simple Proof of a Folklore Theorem about Delimited Control][research_biernacki_danvy_2005_3]
- [Asai, 2004, Offline partial evaluation for shift and reset][research_asai_2004]
- [Thielecke, 2003, From control effects to typed continuation passing][research_thielecke_2003]
- [Berdine and others, 2002, Linear Continuation-Passing][research_berdine_ohearn_2002]
- [Asai, 2002, Online partial evaluation for shift and reset][research_asai_2002]
- [Kelsey, 1995, A correspondence between continuation passing style and static single assignment form][research_kelsey_1995]
- [Hatcliff and Danvy, 1994, A generic account of continuation-passing styles][research_hatcliff_danvy_1994]
- [Okasaki and others, 1994, Call-by-need and continuation-passing style][research_okasaki_lee_1994]
- [De Bosschere and Tarau, 1994, High performance continuation passing style Prolog-to-C mapping][research_debosschere_tarau_1994]
- [Sabry and Felleisen, 1994, Is continuation-passing useful for data flow analysis?][research_sabry_felleisen_1994]
- [Sabry and Felleisen, 1993, Reasoning about programs in continuation-passing style][research_sabry_felleisen_1993]
- [Lawall and Danvy, 1993, Separating stages in the continuation-passing style transformation][research_lawall_danvy_1993]
- [Appel and Shao, 1992, Callee-save registers in continuation-passing style][research_appel_shao_1992]
- [Sabry and Felleisen, 1992, Reasoning about programs in continuation-passing style][research_sabry_felleisen_1992]
- [Appel and Jim, 1989, Continuation-passing, closure-passing style][research_appel_jim_1989]

- [Lindley, 2014, Algebraic effects and effect handlers for idioms and arrows][research_lindley_2014]
- [Bauer and Pretnar, 2014, An Effect System for Algebraic Effects and Handlers][research_bauer_pretnar_2014]
- [Wu and others, 2014, Effect handlers in scope][research_wu_schrijvers_2014]
- [Pretnar, 2014, Inferring Algebraic Effects][research_pretnar_2014]
- [Plotkin and Pretnar, 2013, Handling Algebraic Effects][research_plotkin_pretnar_2013]
- [Ahman and Staton, 2013, Normalization by Evaluation and Algebraic Effects][research_ahman_staton_2013]
- [Brady, 2013, Programming and reasoning with algebraic effects and dependent types][research_brady_2013]
- [Johann and others, 2010, A Generic Operational Metatheory for Algebraic Effects][research_johann_simpson_2010]
- [Plotkin and Pretnar, 2008, A Logic for Algebraic Effects][research_plotkin_pretnar_2008]
- [Hyland and others, 2007, Combining algebraic effects with continuations][research_hyland_levy_2007]
- [Power, 2006, The Universal Algebra of Computational Effects Lawvere Theories and Monads][research_power_2006]

- [Wang and others, 2014, Register allocation for hybrid register architecture in nonvolatile processors][research_wang_jia_2014]
- [Zhang and others, 2013, Register Allocation by Incremental Graph Colouring for Clustered VLIW Processors][research_zhang_wu_2013]
- [Tavares and others, 2011, Decoupled graph-coloring register allocation with hierarchical aliasing][research_tavares_colombet_2011]
- [Colombet and others, 2011, Graph-coloring and treescan register allocation using repairing][research_colombet_boissinot_2011]
- [Lintzmayer and others, 2011, Register Allocation with Graph Coloring by Ant Colony Optimization][research_lintzmayer_mulati_2011]
- [Subha, 2010, A register allocation algorithm][research_subha_2010]
- [Tang and others, 2010, Balanced Bipartite Graph Based Register Allocation for Network Processors in Mobile and Wireless Networks][research_tang_you_2010]
- [Odaira and others, 2010, Coloring-based coalescing for graph coloring register allocation][research_odaira_nakaike_2010]
- [Subha, 2009, A Modified Linear Scan Register Allocation Algorithm][research_subha_2009]
- [Wang and others, 2009, Reducing Code Size by Graph Coloring Register Allocation and Assignment Algorithm for Mixed-Width ISA Processor][research_wang_wu_2009]
- [Baev, 2009, Techniques for Region-Based Register Allocation][research_baev_2009]
- [Rong, 2009, Tree register allocation][research_rong_2009]
- [2009, Tutorial on SSA-Based Register Allocation][research_tutorial_on_2009]
- [Falk, 2009, WCET-aware register allocation based on graph coloring][research_falk_2009]
- [Hong and Ramanujam, 2008, Address Register Allocation in Digital Signal Processors][research_hong_ramanujam_2008]
- [Mahajan and Ali, 2008, Hybrid evolutionary algorithm for graph coloring register allocation][research_mahajan_ali_2008]
- [Guo and others, 2007, A Phase-Coupled Compiler Backend for a New VLIW Processor Architecture Using Two-step Register Allocation][research_guo_liu_2007]
- [Wu and Li, 2007, Extending Traditional Graph-Coloring Register Allocation Exploiting Meta-heuristics for Embedded Systems][research_wu_li_2007]
- [Gao and Shi, 2005, An improved approach of register allocation via graph coloring][research_gao_shi_2005]
- [Chase, 2005, Session details Register allocation][research_chase_2005]
- [Smith and others, 2004, A generalized algorithm for graph-coloring register allocation][research_smith_ramsey_2004]
- [Chaitin, 2004, Register allocation and spilling via graph coloring][research_chaitin_2004]
- [Wall, 2004, Register windows vs. register allocation][research_wall_2004]
- [Boyapati, 2004, Session details Register allocation][research_boyapati_2004]
- [Park and others, 2001, Register Allocation for Banked Register File][research_park_lee_2001]
- [KIM and others, 2000, REGISTER ALLOCATION IN HYPER-BLOCK FOR EPIC PROCESSORS][research_kim_gopinath_2000]
- [de Werra and others, 1999, On a graph-theoretical model for cyclic register allocation][research_dewerra_eisenbeis_1999]
- [Zhou, 1996, Parameter passing and control stack management in Prolog implementation revisited][research_zhou_1996]
- [Elof Frank, 1995, Constrained Register Allocation in Bus Architectures][research_eloffrank_1995]
- [Jui-Ming Chang, 1995, Register Allocation and Binding for Low Power][research_juimingchang_1995]
- [Eichenberger and Davidson, 1995, Register allocation for predicated code][research_eichenberger_davidson_1995]
- [Briggs and others, 1994, Improvements to graph coloring register allocation][research_briggs_cooper_1994]
- [Norris and Pollock, 1994, Register allocation over the program dependence graph][research_norris_pollock_1994]
- [Callahan and Koblenz, 1991, Register allocation via hierarchical graph coloring][research_callahan_koblenz_1991]
- [Nickerson, 1990, Graph coloring register allocation for processors with multi-register operands][research_nickerson_1990]
- [Wall, 1988, Register windows vs. register allocation][research_wall_1988]
- [Wall, 1986, Global register allocation at link time][research_wall_1986]
- [Larus and Hilfinger, 1986, Register allocation in the SPUR Lisp compiler][research_larus_hilfinger_1986]
- [Chaitin, 1982, Register allocation and spilling via graph coloring][research_chaitin_1982]
- [Sites, 1979, Machine-independent register allocation][research_sites_1979]

- [Kolek and others, 2013, Adding microMIPS backend to the LLVM compiler infrastructure][research_kolek_jovanovic_2013]
- [MolinaFraticelli, 2012, Auto Code Generation for Simulink-Based Attitude Determination Control System][research_molinafraticellijosecarlos_2012]
- [Sanmorino, 2012, Development of computer assisted instruction CAI for compiler model The simulation of stack on code generation][research_sanmorino_2012]
- [Inoue and others, 2011, A trace-based Java JIT compiler retrofitted from a method-based compiler][research_inoue_hayashizaki_2011]
- [Yi, 2011, Automated programmable control and parameterization of compiler optimizations][research_yi_2011]
- [Pałka and others, 2011, Testing an optimising compiler by generating random lambda terms][research_palka_claessen_2011]
- [Frenkel and others, 2011, Towards a Modular and Accessible Modelica Compiler Backend][research_frenkel_kunze_2011]
- [Myreen, 2010, Verified just-in-time compiler on x86][research_myreen_2010]
- [Cordes and others, 2009, A Fast and Precise Static Loop Analysis Based on Abstract Interpretation, Program Slicing and Polytope Models][research_cordes_falk_2009]
- [Chen Zhao and others, 2009, Automated test program generation for an industrial optimizing compiler][research_chenzhao_yunzhixue_2009]
- [Böhme and others, 2009, HOL-Boogie-An Interactive Prover-Backend for the Verifying C Compiler][research_bohme_moskal_2009]
- [Ly and others, 2009, Reduced Model for a PEMFC Stack Automated Code Generation and Verification][research_ly_birgersson_2009]
- [Wagstaff and others, 2008, Automatic Code Generation for Instrument Flight Software][research_wagstaffkiril_benowitzedward_2008]
- [Leroy, 2006, Formal certification of a compiler back-end or][research_leroy_2006]
- [Surakka and others, 2005, Towards compiler backend optimization for low energy consumption at instruction level][research_surakka_mikkonen_2005]
- [Klein and Strecker, 2004, Verified bytecode verification and type-certifying compilation][research_klein_strecker_2004]
- [Suganuma and others, 2003, A region-based compilation technique for a Java just-in-time compiler][research_suganuma_yasue_2003]
- [Yoshikawa and others, 2003, Random program generator for Java JIT compiler test system][research_yoshikawa_shimura_2003]
- [Mann, 2003, The Compiler Design Handbook Optimisation and Machine Code Generation][research_mann_2003]
- [Necula, 2000, Translation validation for an optimizing compiler][research_necula_2000]
- [ten Hagen and others, 1996, Codesign of a parallel architecture and an optimizing compiler backend SIN rete processing as a case study][research_tenhagen_steinberg_1996]
- [Bhasker, 1988, Implementation of an optimizing compiler for VHDL][research_bhasker_1988]
- [Fraser and Wendt, 1986, Integrating code generation and optimization][research_fraser_wendt_1986]
- [Ching, 1986, Program analysis and code generation in an APL/370 compiler][research_ching_1986]
- [Powell, 1984, A portable optimizing compiler for Modula-2][research_powell_1984]
- [Karr, 1984, Code generation by coagulation][research_karr_1984]
- [Carter, 1982, Further analysis of code generation for a single register machine][research_carter_1982]
- [Hura, 1982, Optimization of assembly code generation in a compiler][research_hura_1982]
- [Cattell and others, 1979, Code generation in a machine-independent compiler][research_cattell_newcomer_1979]
- [Rudmik and Lee, 1979, Compiler design for efficient code generation and program optimization][research_rudmik_lee_1979]
- [Couch and Hamm, 1977, Semantic Structures for Efficient Code Generation on a Stack Machine][research_couch_hamm_1977]
- [Painter, 1970, Effectiveness of an optimizing compiler for arithmetic expressions][research_painter_1970]

- [Larus, 2011, Session details Compiler correctness][research_larus_2011]
- [Chlipala, 2010, A verified compiler for an impure functional language][research_chlipala_2010]
- [Avigad and others, 2007, A formally verified proof of the prime number theorem][research_avigad_donnelly_2007]
- [Schneider and others, 2006, A Verified Compiler for Synchronous Programs with Local Declarations][research_schneider_brandt_2006]
- [Brady and Hammond, 2006, A verified staged interpreter is a verified compiler][research_brady_hammond_2006]
- [Berghofer and Strecker, 2004, Extracting a formally verified, fully executable compiler from a proof assistant][research_berghofer_strecker_2004]
- [Rushby, 2002, Formally Verified Hardware Encapsulation Mechanism for Security, Integrity, and Safety][research_rushby_2002]
- [Mohnen, 1997, A COMPILER CORRECTNESS PROOF FOR THE STATIC LINK TECHNIQUE BY MEANS OF EVOLVING ALGEBRAS][research_mohnen_1997]

- [Naik, 2013, Session details Compiler validation][research_naik_2013]
- [Tao and others, 2010, An Automatic Testing Approach for Compiler Based on Metamorphic Testing Technique][research_tao_wu_2010]
- [Zaks and Pnueli, 2008, Program analysis for compiler validation][research_zaks_pnueli_2008]
- [Nair and Sarasamma, 2006, Formal Semantics of Ciset Relational Operators][research_nair_sarasamma_2006]
- [Kossatchev and Posypkin, 2005, Survey of compiler testing methods][research_kossatchev_posypkin_2005]
- [Jefferson and others, 1994, Ada Compiler Validation Summary Report Certificate Number 940902S1.11376. UNISYS Corporation IntegrAda for Windows NT, Version 1.0. Intel Deskside Server for Intel Pentium 60 MHz = . Intel Deskside Server with Intel Pentium 60 MHz][research_jefferson_johnson_1994]
- [Jefferson and others, 1994, Ada Compiler Validation Summary Report Certificate Number 940902S1.11377 UNISYS Corporation. IntegrAda for Windows NT, Version 1.0. Intel Deskside Server with Intel 80486DX266 = Intel Deskside Server with Intel 80486DX266][research_jefferson_johnson_1994_2]
- [VISTA RESEARCH CORP TUCSON AZ, 1994, Ada Compiler Validation Summary Report Certificate Number 940223W1. 11338 Green Hills Software, Inc. Green Hills Optimizing Ada Compiler, 1.8.7 SPARCstation 10 under SunOS, Release 4.1.3][research_vistaresearchcorptucsonaz_1994]
- [VISTA RESEARCH CORP TUCSON AZ, 1994, Ada Compiler Validation Summary Report Certificate Number 940305W1. 11335 TLD Systems, Ltd. TLD Comanche VAX/1960 Ada Compiler System, Version 4.1.1 VAX Cluster under VMS 5.5 = Tronix JIAWG Execution Vehicle i960MX under TLD Real Time Executive, Version 4.1.1][research_vistaresearchcorptucsonaz_1994_2]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1992, Ada Compiler Validation Procedures, Version 3.1][research_adajointprogramofficearlingtonva_1992]
- [Lehman, 1992, Ada Compiler Validation Support Fiscal Year 1991][research_lehman_1992]
- [Hook and Lehman, 1992, Ada Compiler Validation Support Fiscal Year 1992][research_hook_lehman_1992]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1991, Ada Compiler Validation Summary Report Certificate Number 910612W1. 11168 Telesoft, IBM Ada/370, Version 1.2.0 without Optimization IBM 3080, V / SP HPO Rel 5.0 Unopt Host and Target][research_adajointprogramofficearlingtonva_1991]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1990, Ada Compiler Validation Procedures. Version 2.1][research_adajointprogramofficearlingtonva_1990]
- [Wilson, 1989, Ada Compiler Validation Capability ACVC Version 1.11 Field-Test Release . ANSI][research_wilson_1989]
- [Wilson, 1989, Ada Compiler Validation Capability ACVC Version 1.11 Field-Test Release . ANSI, BACKUP, TAR][research_wilson_1989_2]
- [Wilson, 1989, Ada Compiler Validation Capability ACVC Version 1.11 Field-Test Release . BACKUP][research_wilson_1989_3]
- [Wilson, 1989, Ada Compiler Validation Capability ACVC Version 1.11 Field-Test Release . TAR][research_wilson_1989_4]
- [Hook and Heilbrunner, 1989, Ada Compiler Validation Procedures][research_hook_heilbrunner_1989]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1989, Ada Compiler Validation Procedures Version 2.0][research_adajointprogramofficearlingtonva_1989]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1989, Ada Compiler Validation Summary Report. CONVEX Computer Corporation, CONVEX Ada, Version 1.1 C210, Host and Target 890508W1.10077][research_adajointprogramofficearlingtonva_1989_2]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1989, Ada Compiler Validation Summary Report. Meridian Software Systems, Inc., AdaVantage, Version 3.0, IBM PS/2 Model 80 with Floating Point Co-Processor Host and Target 890405W1.10049][research_adajointprogramofficearlingtonva_1989_3]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1989, Ada Compiler Validation Summary Report. Verdix Corporation, VAda-110-2323, Version 5.5, Sequent Balance 8000 Host and Target , 890216W1.10029][research_adajointprogramofficearlingtonva_1989_4]
- [NATIONAL BUREAU OF STANDARDS GAITHERSBURG MD, 1989, Ada Compiler Validation Summary Report Certificate Number 880624S1. 09132, Control Data Corporation CYBER 180 Ada Compiler, Version 1.1 HOST and TARGET COMPUTER CYBER 180-930-31][research_nationalbureauofstandardsgaithersburgmd_1989]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1989, Ada Compiler Validation Summary Report Certificate Number 890329I1. 10076 SYSTEAM KG, SYSTEAM Ada Compiler VAX/VMS x MC68020/05-9 Version 1.81][research_adajointprogramofficearlingtonva_1989_5]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1988, Ada Trade Name Compiler Validation Summary Report. Certificate Number 880620W1.09092, Encore Computer Corporation, Encore Verdix Ada Development System, Version 5.5, Encore Multimax 320][research_adajointprogramofficearlingtonva_1988]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1988, Ada Tradename Compiler Validation Summary Report Certificate Number 880201W1.09019 Verdix Corporation VAda-010-2323, Version 5.5 Sequent Balance 8000][research_adajointprogramofficearlingtonva_1988_2]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1988, Ada Tradename Compiler Validation Summary Report Certificate Number 880429W1.09053 Telesoft, Inc. TeleGen2 Ada Compiler for VAX/VMS to 1750A, Version 3.22 MicroVAX 2 to MIL-STD-1750A ECSPO RAID Simulator][research_adajointprogramofficearlingtonva_1988_3]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1988, Ada Tradename Compiler Validation Summary Report Certificate Number 880815W1.09143 Rational VAX-VMS, Version 2.0.45 Rational R1000 Series 200 Model 20 and VAX-11/750 Host and Target][research_adajointprogramofficearlingtonva_1988_4]
- [NATIONAL BUREAU OF STANDARDS GAITHERSBURG MD, 1988, Ada Compiler Validation Summary Report Certificate Number 880708S1. 09151, SoftTech, Inc., Ada 86, Version 3.21 VAX 11/780-11/785 Host and Intel IAPX 80386R Target][research_nationalbureauofstandardsgaithersburgmd_1988]
- [NATIONAL BUREAU OF STANDARDS GAITHERSBURG MD, 1988, Ada Compiler Validation Summary Report Certificate Number 880719S1. 09154, Naval Underwater Systems Command, ADAUYK43 ALS/N Ada/L , Version 1.0, VAX 11/785 Host and AN/UYK-43 Target][research_nationalbureauofstandardsgaithersburgmd_1988_2]
- [NATIONAL BUREAU OF STANDARDS GAITHERSBURG MD, 1988, Ada Compiler Validation Summary Report Compiler Name ADE/32 Revision 3.00. Certificate Number 880527S1.09113. Host MV/20000 under AOS/VS, Revision 7.56. Target ROLM HAWK/32 under AOS/VS, Revision 7.56][research_nationalbureauofstandardsgaithersburgmd_1988_3]
- [Hook, 1987, Export Control of the Ada Trade Name Compiler Validation Capability ACVC][research_hook_1987]
- [Dixon, 1982, A Pascal compiler testing facility][research_dixon_1982]
- [Samet, 1977, A normal form for compiler testing][research_samet_1977]
- [Baird and Johnson, 1977, COBOL Compiler Validation System, 1974. Version 3.0][research_baird_johnson_1977]
- [Samet, 1976, Compiler testing via symbolic interpretation][research_samet_1976]
- [INFORMATION MANAGEMENT INC SAN FRANCISCO CA, 1970, USER'S MANUAL COBOL COMPILER VALIDATION SYSTEM][research_informationmanagementincsanfranciscoca_1970]
- [ELECTRONIC SYSTEMS DIV HANSCOM AFB MA, 1970, USER'S MANUAL JOVIAL COMPILER VALIDATION SYSTEM][research_electronicsystemsdivhanscomafbma_1970]

- [Squire and Funkhouser, 2014, "A Bit of Code" How the Stack Overflow Community Creates Quality Postings][research_squire_funkhouser_2014]
- [Kong and others, 2014, An Overview of Worst-Case Execution Time Estimation for Embedded Programs][research_kong_shi_2014]
- [Henry and others, 2014, How to compute worst-case execution time by optimization modulo theory and a clever encoding of program semantics][research_henry_asavoae_2014]
- [Debenham and Westlake, 2014, Pre-stack depth migration for improved imaging under seafloor canyons 2D case study of Browse Basin, AustraliaFN1][research_debenham_westlake_2014]
- [Bao and others, 2014, PWCET Power-Aware Worst Case Execution Time Analysis][research_bao_tavarageri_2014]
- [Brandner and Jordan, 2014, Refinement of worst-case execution time bounds by graph pruning][research_brandner_jordan_2014]
- [Hardy and Puaut, 2014, Static probabilistic worst case execution time estimation for architectures with faulty instruction caches][research_hardy_puaut_2014]
- [Kong and Chen, 2013, A Worst-Case Execution Time Analysis Approach Based on AOE Networks][research_kong_chen_2013]
- [- and others, 2013, Bounding the Worst-Case Execution Time for the Fixed-Priority Preemptive Systems Based on the Preemption Points][research_bounding_the_worst_case_2013]
- [Freier and Jian-Jia Chen, 2013, Prioritization for real-time embedded systems on dual-core platforms by exploiting the typical- and worst-case execution times][research_freier_jianjiachen_2013]
- [Wu and Zhang, 2013, Reducing worst-case execution time of hybrid SPM-caches][research_wu_zhang_2013]
- [Kleinsorge and others, 2013, Simple analysis of partial worst-case execution paths on general control flow graphs][research_kleinsorge_falk_2013]
- [Hardy and Puaut, 2013, Static probabilistic worst case execution time estimation for architectures with faulty instruction caches][research_hardy_puaut_2013]
- [Allamanis and Sutton, 2013, Why, when, and what Analyzing Stack Overflow questions by topic, type, and code][research_allamanis_sutton_2013]
- [Wu and Zhang, 2012, A Model Checking Based Approach to Bounding Worst-Case Execution Time for Multicore Processors][research_wu_zhang_2012]
- [Kong and Jiang, 2012, A Worst-case execution time analysis approach based on independent paths for ARM programs][research_kong_jiang_2012]
- [Whiteside and others, 2012, Directional Imaging Stack DIS for Shot Based Pre-stack Depth Migrations][research_whiteside_yeh_2012]
- [Harmon and others, 2012, Fast, Interactive Worst-Case Execution Time Analysis With Back-Annotation][research_harmon_schoeberl_2012]
- [Lo and Suh, 2012, Worst-case execution time analysis for parallel run-time monitoring][research_lo_suh_2012]
- [Hepp and Schoeberl, 2012, Worst-Case Execution Time Based Optimization of Real-Time Java Programs][research_hepp_schoeberl_2012]
- [Zhang and others, 2011, A Case Study of Pre-stack Depth Migration Application over a Salt Dome Area][research_zhang_ping_2011]
- [Lu and others, 2011, A new way about using statistical analysis of worst-case execution times][research_lu_nolte_2011]
- [Lu and others, 2011, A trace-based statistical worst-case execution time analysis of component-based real-time embedded systems][research_lu_nolte_2011_2]
- [Zolda and others, 2011, Context-Sensitive Measurement-Based Worst-Case Execution Time Estimation][research_zolda_bunte_2011]
- [Marref, 2011, Fully-automatic derivation of exact program-flow constraints for a tighter worst-case execution-time analysis][research_marref_2011]
- [Louise, 2011, Improving Branch Prediction Related WCET Abstract Interpretation][research_louise_2011]
- [Ermedahl and Puschner, 2011, Preface to the special issue on worst-case execution-time analysis][research_ermedahl_puschner_2011]
- [Wheeler and others, 2011, Video subset selection for measurement based Worst Case Execution Time analysis][research_wheeler_bate_2011]
- [Huber and others, 2011, Worst-case execution time analysis-driven object cache design][research_huber_puffitsch_2011]
- [Falk and Lokuciejewski, 2010, A compiler framework for the reduction of worst-case execution times][research_falk_lokuciejewski_2010]
- [Bartlett and others, 2010, Accurate Determination of Loop Iterations for Worst-Case Execution Time Analysis][research_bartlett_bate_2010]
- [Kirner and others, 2010, Beyond loop bounds comparing annotation languages for worst-case execution time analysis][research_kirner_knoop_2010]
- [Ding and Zhang, 2010, Loop-Based Instruction Prefetching to Reduce the Worst-Case Execution Time][research_ding_zhang_2010]
- [Wang and others, 2010, Stack Bound Inference for Abstract Java Bytecode][research_wang_qiu_2010]
- [Lv and others, 2010, Static worst-case execution time analysis of the μC/OS-II real-time kernel][research_lv_guan_2010]
- [Schoeberl and others, 2010, Worst-case execution time analysis for a Java processor][research_schoeberl_puffitsch_2010]
- [Zhang and Yan, 2009, Accurately Estimating Worst-Case Execution Time for Multi-core Processors with Shared Direct-Mapped Instruction Caches][research_zhang_yan_2009]
- [Ermedahl and others, 2009, Deriving the Worst-Case Execution Time Input Values][research_ermedahl_fredriksson_2009]
- [Berten and others, 2009, Managing Imprecise Worst Case Execution Times on DVFS Platforms][research_berten_chang_2009]
- [Kirner and others, 2009, Precise Worst-Case Execution Time Analysis for Processors with Timing Anomalies][research_kirner_kadlec_2009]
- [Mitra and Givargis, 2009, Session details Microfluidics, worst-case execution time, and cache optimization][research_mitra_givargis_2009]
- [Hanzich and others, 2009, Subsalt Imaging through Pre-Stack Depth Migration - A Case Study from the North Red Sea][research_hanzich_arayapolo_2009]
- [Williams and Roger, 2009, Test generation strategies to measure worst-case execution time][research_williams_roger_2009]
- [Tan, 2009, The worst-case execution time tool challenge 2006][research_tan_2009]
- [LEE and others, 2009, Visualization and Formalization of User Constraints for Tight Estimation of Worst-Case Execution Time][research_lee_bang_2009]
- [Harmon and others, 2008, A Modular Worst-case Execution Time Analysis Tool for Java Processors][research_harmon_schoeberl_2008]
- [Yan and Zhang, 2008, Analyzing the worst-case execution time for instruction caches with prefetching][research_yan_zhang_2008]
- [Nayvelt and Bear, 2008, Case study Anisotropic Pre-Stack Depth Migration on the Louisiana Shelf][research_nayvelt_bear_2008]
- [Bate and Kazakov, 2008, New Directions in Worst-Case Execution Time analysis][research_bate_kazakov_2008]
- [Kirner and Puschner, 2008, Obstacles in Worst-Case Execution Time Analysis][research_kirner_puschner_2008]
- [Hunt and others, 2008, Using global data flow analysis on bytecode to aid worst case execution time analysis for real-time Java programs][research_hunt_tonin_2008]
- [Ferdinand and Heckmann, 2008, Worst-Case Execution Time - A Tool Provider's Perspective][research_ferdinand_heckmann_2008]
- [Mohan, 2008, Worst-case execution time analysis of security policies for deeply embedded real-time systems][research_mohan_2008]
- [Harmon and Klefstad, 2007, A Survey of Worst-Case Execution Time Analysis for Real-Time Java][research_harmon_klefstad_2007]
- [Ji and others, 2007, Automated Worst-Case Execution Time Analysis Based on Program Modes][research_ji_wang_2007]
- [Aissa and others, 2007, Bringing Worst Case Execution Time Awareness to an Open Smart Card OS][research_aissa_grimaud_2007]
- [Nemer and others, 2007, Improving the Worst-Case Execution Time Accuracy by Inter-Task Instruction Cache Analysis][research_nemer_casse_2007]
- [Harmon and Klefstad, 2007, Interactive Back-annotation of Worst-case Execution Time Analysis for Java Microprocessors][research_harmon_klefstad_2007_2]
- [Kirner and Schoeberl, 2007, Modeling the Function Cache for Worst-Case Execution Time Analysis][research_kirner_schoeberl_2007]
- [Kaestner, 2007, Safe worst-case execution time analysis by abstract interpretation of executable code][research_kaestner_2007]
- [Harmon and Klefstad, 2007, Toward a Unified Standard for Worst-Case Execution Time Annotations in Real-Time Java][research_harmon_klefstad_2007_3]
- [Auchterlonie and others, 2007, Velocity Model Building for Pre-Stack Depth Migration - An Onshore Libya Case Study][research_auchterlonie_vinje_2007]
- [Choi and Han, 2006, Optimal register reassignment for register stack overflow minimization][research_choi_han_2006]
- [Gustafsson, 2006, The Worst Case Execution Time Tool Challenge 2006][research_gustafsson_2006]
- [Plasterie and Chagalov, 2006, Wave Equation versus Kirchhoff pre-stack depth migration algorithms ? An Australian case study][research_plasterie_chagalov_2006]
- [Jong-In Lee and others, 2005, A Hybrid Framework of Worst-Case Execution Time Analysis for Real-Time Embedded System Software][research_jonginlee_suhyunpark_2005]
- [Egreteau and Thierry, 2005, Attenuating the Effects of Pre-Stack Depth Migration for AVA Analysis][research_egreteau_thierry_2005]
- [Ritchie and others, 2005, Challenges and opportunities in pre-stack depth imaging of legacy seismic data an overthrust belt case study][research_ritchie_popovici_2005]
- [Park and others, 2005, Implementation of Worst Case Execution Time Analysis Tool For Embedded Software based on XScale Processor][research_park_choi_2005]
- [Askim and others, 2004, 4D Seismic Analysis Using Pre Stack Depth Migration][research_askim_brandsbergdahl_2004]
- [Schuele and Schneider, 2004, Abstraction of assembler programs for symbolic worst case execution time analysis][research_schuele_schneider_2004]
- [Corti and Gross, 2004, Approximation of the worst-case execution time using structural analysis][research_corti_gross_2004]
- [Tadepalli and others, 2003, 3D pre-stack depth imaging and well ties A case history of depth imaging in Gulf of Mexico][research_tadepalli_li_2003]
- [Reshef and Roth, 2003, Anisotropy Corrections after Pre-Stack Depth Migration][research_reshef_roth_2003]
- [Ermedahl and others, 2003, Clustered calculation of worst-case execution times][research_ermedahl_stappert_2003]
- [L. Freitas da Luz and C. Ribeiro Cruz, 2003, The CRS stack as a tool for pre-stack depth migration][research_lfreitasdaluz_cribeirocruz_2003]
- [Engblom and others, 2003, Worst-case execution-time analysis for embedded real-time systems][research_engblom_ermedahl_2003]
- [2002, 3D Pre-Stack Depth Migration V0 Analysis and Monte Carlo Automatic Velocity Picking in Depth][research_3d_pre_stack_2002]
- [Blieberger, 2002, Data-Flow Frameworks for Worst-Case Execution Time Analysis][research_blieberger_2002]
- [Morford, 2001, Analysis Of The Effects Of Varying The Anti - Alias Filter In Kirchoff Pre- Stack Depth Migration][research_morford_2001]
- [Lemaistre and others, 2001, Automatic and Continuous Image Gather Analysis after Pre-Stack Depth Migration][research_lemaistre_hanitzsch_2001]
- [Hanitzsch and others, 2001, Pre-Stack Depth Migration for Time-to-Depth Conversion - the Ultimate Tool?][research_hanitzsch_robein_2001]
- [Petkovski and Bradey, 2001, The success of pre-stack depth migration over the Anama structure in the Papuan Foreland Basin, PNG a case history][research_petkovski_bradey_2001]
- [Morford, 2000, A case study Using 3d pre-stack depth migration to image sub-salt sediments and fault zones in Marbella, Mexico][research_morford_2000]
- [Bernat and Burns, 2000, An Approach to Symbolic Worst-Case Execution Time Analysis][research_bernat_burns_2000]
- [Stappert and Altenbernd, 2000, Complete worst-case execution time analysis of straight-line hard real-time programs][research_stappert_altenbernd_2000]
- [Allen and others, 2000, Subsalt Imaging using 3D Pre-Stack Depth Migration in the UK Southern North Sea - a Case History][research_allen_malaguti_2000]
- [Sen and others, 2000, Velocity analysis using pre-stack depth migration and 3D tomogrphy A case study over steeply dipping salt][research_sen_wagner_2000]
- [Colin and Puaut, 2000, Worst Case Execution Time Analysis for a Processor with Branch Prediction][research_colin_puaut_2000]
- [Morford, 1999, A Case Study Using 3D Pre-Stack Depth Migration To Improve The Sub-Salt Image In Marbella, Mexico, Gulf Of Mexico][research_morford_1999]
- [Oates and others, 1998, The Application of Pre-Stack Depth Migration using Topographic Analysis to Aid in the][research_oates_harinder_1998]
- [Puschner, 1998, Worst-case execution-time analysis at low cost][research_puschner_1998]
- [Puschner, 1997, Worst-Case Execution Time Analysis at Low Cost][research_puschner_1997]
- [Shih and Chen, 1996, Iterative Pre-Stack Depth Migration With Velocity Analysis][research_shih_chen_1996]
- [Boding, 1996, Pre-stack depth migration in three dimensions with the imaging wave machine][research_boding_1996]
- [Levy, 1996, Should caches be split or shared? Analysis using the superposition of bursty stack depth processes][research_levy_1996]
- [Roberts, 1995, 3D Post Stack Depth Migration in the UK Southern North Sea - a Case Study][research_roberts_1995]
- [Nilsen and Rygg, 1995, Worst-case execution time analysis on modern processors][research_nilsen_rygg_1995]
- [Wenes and others, 1994, A Practical implementation of a 3D pre-stack depth migration algorithm][research_wenes_kremer_1994]
- [Jyh-Charn Liu and Hung-Ju Lee, 1994, Deterministic upperbounds of the worst-case execution times of cached programs][research_jyhcharnliu_hungjulee_1994]
- [C. Robinson and others, 1994, Prospect definition by pre-stack depth migration of a grid of seismic lines - A case history][research_crobinson_ptung_1994]
- [P. Jeannot and Berranger, 1994, Ray-mapped focusing - A migration velocity analysis for Kirchoff pre-stack depth imaging][research_pjeannot_berranger_1994]
- [P. Jeannot, 1994, Robust Kirchhoff pre-stack depth imaging with semi-gridded rays][research_pjeannot_1994]
- [Hinkley and others, 1994, Velocity Model Building for 3D Pre-Stack Depth Migration - a Case Study][research_hinkley_ho_1994]
- [Landa and Sorin, 1993, Fast pre-stack depth migration by CRP stacking][research_landa_sorin_1993]
- [R. Granli, 1993, Imaging salt with pre-stack depth migration][research_rgranli_1993]
- [Zhang and others, 1993, Pipelined processors and worst case execution times][research_zhang_burns_1993]
- [Cabrera and others, 1992, 3-D Pre-Stack Depth Migration Implementation and Case History][research_cabrera_perkins_1992]
- [J. Berkhout, 1992, True amplitude aspects of pre-stack depth migration][research_jberkhout_1992]
- [G. Western and Ball, 1991, 3D Pre-stack depth migration in the Gulf of Sueza. A case history][research_gwestern_ball_1991]
- [Tarjan, 1985, Amortized Computational Complexity][research_tarjan_1985]

- [Cousot and Cousot, 2014, A galois connection calculus for abstract interpretation][research_cousot_cousot_2014]
- [Gao and others, 2014, A Method of Binary Code Variable Interval Analysis Based on Abstract Interpretation][research_gao_li_2014]
- [Ravanbakhsh and Sankaranarayanan, 2014, Infinite horizon safety controller synthesis through disjunctive polyhedral abstract interpretation][research_ravanbakhsh_sankaranarayanan_2014]
- [Chudnov and others, 2014, Information Flow Monitoring as Abstract Interpretation for Relational Logic][research_chudnov_kuan_2014]
- [Kowalewski and others, 2013, Model checking and abstract interpretation as building blocks of advanced program analysis techniques][research_kowalewski_philippou_2013]
- [Genaim and Zanardini, 2013, Reachability-based acyclicity analysis by Abstract Interpretation][research_genaim_zanardini_2013]
- [Ranzato, 2013, Session details Abstract interpretation][research_ranzato_2013]
- [Anderson and Loginov, 2013, Static analysis of machine code for supply-chain risk management][research_anderson_loginov_2013]
- [Cousot and Cousot, 2012, An abstract interpretation framework for termination][research_cousot_cousot_2012]
- [Chaumette and others, 2011, Automated extraction of polymorphic virus signatures using abstract interpretation][research_chaumette_ly_2011]
- [Cousot and Cousot, 2011, Grammar semantics, analysis and parsing by abstract interpretation][research_cousot_cousot_2011]
- [Hua and others, 2010, Model-Based Intrusion Detection by Abstract Interpretation][research_hua_nishide_2010]
- [Bertrane and others, 2010, Static Analysis and Verification of Aerospace Software by Abstract Interpretation][research_bertrane_cousot_2010]
- [Blanc and Kadobayashi, 2010, Towards revealing JavaScript program intents using abstract interpretation][research_blanc_kadobayashi_2010]
- [De Francesco and others, 2010, Using abstract interpretation to add type checking for interfaces in Java bytecode verification][research_defrancesco_lettieri_2010]
- [Giacobazzi, 2008, Abstract Interpretation in Code Security][research_giacobazzi_2008]
- [Bernardeschi and others, 2008, Decomposing bytecode verification by abstract interpretation][research_bernardeschi_francesco_2008]
- [Anier, 2008, Motion recognition with abstract interpretation and HMM][research_anier_2008]
- [LI, 2008, Program Verification Techniques Based on the Abstract Interpretation Theory][research_li_2008]
- [Di Pierro and others, 2008, Relational Analysis and Precision via Probabilistic Abstract Interpretation][research_dipierro_sotin_2008]
- [Musumbu, 2008, Static Checking by Means of Abstract Interpretation][research_musumbu_2008]
- [Cortesi, 2008, Widening Operators for Abstract Interpretation][research_cortesi_2008]
- [Seo and others, 2007, Goal-directed weakening of abstract interpretation results][research_seo_yang_2007]
- [Feret and others, 2007, Reachability Analysis of Biological Signalling Pathways by Abstract Interpretation][research_feret_simos_2007]
- [2007, The Role of Abstract Interpretation in Formal Methods][research_the_role_2007]
- [Henriksen and Gallagher, 2006, Abstract Interpretation of PIC Programs through Logic Programming][research_henriksen_gallagher_2006]
- [Christodorescu and Jha, 2006, Static Analysis of Executables to Detect Malicious Patterns][research_christodorescu_jha_2006]
- [Dalla Preda and Giacobazzi, 2005, Control code obfuscation by abstract interpretation][research_dallapreda_giacobazzi_2005]
- [Bayley and Shiel, 2005, JVM Bytecode Verification Without Dataflow Analysis][research_bayley_shiel_2005]
- [Leuschel, 2004, A framework for the integration of partial evaluation and abstract interpretation of logic programs][research_leuschel_2004]
- [Basin and others, 2003, Bytecode Verification by Model Checking][research_basin_friedrich_2003]
- [Cousot and Cousot, 2002, Systematic design of program transformation frameworks by abstract interpretation][research_cousot_cousot_2002]
- [Cousot and Cousot, 2001, A Case Study in Abstract Interpretation Based Program Transformation][research_cousot_cousot_2001]
- [Schmidt, 2000, Abstract interpretation and program modelling][research_schmidt_2000]
- [Baggett, 2000, An Abstract Interpretation of the Wavelet Dimension Function Using Group Representations][research_baggett_2000]
- [Qian, 2000, Standard fixpoint iteration for Java bytecode verification][research_qian_2000]
- [Cousot and Cousot, 2000, Temporal abstract interpretation][research_cousot_cousot_2000]
- [Huch, 1999, Verification of Erlang programs using abstract interpretation and model checking][research_huch_1999]
- [Dams and others, 1997, Abstract interpretation of reactive systems][research_dams_gerth_1997]
- [Cortesi and others, 1997, Complementation in abstract interpretation][research_cortesi_file_1997]
- [Debray, 1995, Abstract interpretation and low-level code optimization][research_debray_1995]
- [Cousot and Cousot, 1995, Formal language, grammar and set-constraint-based program analysis by abstract interpretation][research_cousot_cousot_1995]
- [Deutsch, 1995, Semantic models and abstract interpretation techniques for inductive data structures and pointers][research_deutsch_1995]
- [Monsuez, 1995, Using abstract interpretation to define a strictness type inference system][research_monsuez_1995]
- [Marriott and others, 1994, Denotational abstract interpretation of logic programs][research_marriott_sondergaard_1994]
- [Le Charlier and Van Hentenryck, 1994, Experimental evaluation of a generic abstract interpretation algorithm for PROLOG][research_lecharlier_vanhentenryck_1994]
- [Mycroft, 1993, Completeness and predicate-based abstract interpretation][research_mycroft_1993]
- [Coppo and Ferrari, 1993, Type inference, abstract interpretation and strictness analysis][research_coppo_ferrari_1993]
- [Muller and Zhou, 1992, Abstract interpretation in weak powerdomains][research_muller_zhou_1992]
- [Palsberg and Schwartzbach, 1992, Binding Time Analysis Abstract Interpretation vs. Type Inference][research_palsberg_schwartzbach_1992]
- [Janssens and Bruynooghe, 1992, Deriving descriptions of possible values of program variables by means of abstract interpretation][research_janssens_bruynooghe_1992]
- [Cortesi and Filé, 1991, Abstract interpretation of logic programs][research_cortesi_file_1991]
- [McNerney, 1991, Verifying the correctness of compiler transformations on basic blocks using abstract interpretation][research_mcnerney_1991]
- [Burn, 1990, A relationship between abstract interpretation and projection analysis][research_burn_1990]
- [Nielson, 1988, Strictness analysis and denotational abstract interpretation][research_nielson_1988]
- [Nielson, 1987, Strictness analysis and denotational abstract interpretation][research_nielson_1987]

- [Hu and Zhao, 2014, Analysis on Process Code schedule of Android Dalvik Virtual Machine][research_hu_zhao_2014]
- [Mamdouh and others, 2014, On-demand distributed on-card bytecode verification][research_mamdouh_bahaaeldin_2014]
- [Jiang and Li, 2014, Using Contour Marking Bytecode Verification Algorithm on the Java Card][research_jiang_li_2014]
- [You and Lu, 2012, A markup language for java bytecode][research_you_lu_2012]
- [Kim and others, 2012, Generating Verification Conditions from BIRS Code using Basic Paths for Java Bytecode Verification][research_kim_kim_2012]
- [Santone, 2011, Clone detection through process algebras and Java bytecode][research_santone_2011]
- [Male and others, 2011, Formalisation and implementation of an algorithm for bytecode verification of @NonNull types][research_male_pearce_2011]
- [Haikun Liu and others, 2011, Live Virtual Machine Migration via Asynchronous Replication and State Synchronization][research_haikunliu_haijin_2011]
- [DONG and others, 2011, Logic System for Bytecode Program Modular Certification][research_dong_wang_2011]
- [Moret and others, 2011, Polymorphic bytecode instrumentation][research_moret_binder_2011]
- [Bauml and Brada, 2011, Reconstruction of Type Information from Java Bytecode for Component Compatibility][research_bauml_brada_2011]
- [Chen and others, 2010, Implementation of Bytecode-based Software Watermarking for Java Programs][research_chen_wang_2010]
- [2010, JSIMIL - A Java Bytecode Clone Detector][research_jsimil_2010]
- [Rudolph and Thiemann, 2010, Mnemonics type-safe bytecode generation at run time][research_rudolph_thiemann_2010]
- [DeVries and others, 2009, ActionScript bytecode verification with co-logic programming][research_devries_gupta_2009]
- [DeVries and others, 2009, ActionScript bytecode verification with co-logic programming abstract only][research_devries_gupta_2009_2]
- [Chi and others, 2009, An Improved Bytecode Verification Algorithm on Java Card][research_chi_li_2009]
- [Chen and others, 2009, Bytecode Generation for XQuery Compiler][research_chen_yuan_2009]
- [Gal and others, 2008, Java bytecode verification via static single assignment form][research_gal_probst_2008]
- [Bavera and Bonelli, 2008, Type-based information flow analysis for bytecode languages with variable object field policies][research_bavera_bonelli_2008]
- [Shi and others, 2008, Virtual machine showdown][research_shi_casey_2008]
- [Liu, 2007, Bytecode Verification for Enhanced JVM Access Control][research_liu_2007]
- [Huynh and Roychoudhury, 2007, Memory model sensitive bytecode verification][research_huynh_roychoudhury_2007]
- [Huang and others, 2006, Adaptiveness in well-typed Java bytecode verification][research_huang_jay_2006]
- [Burdy and Pavlova, 2006, Java bytecode specification and verification][research_burdy_pavlova_2006]
- [Bernardeschi and others, 2006, Using Control Dependencies for Space-Aware Bytecode Verification][research_bernardeschi_lettieri_2006]
- [Gal and others, 2005, Integrated Java Bytecode Verification][research_gal_probst_2005]
- [Kot and Kozen, 2005, Kleene Algebra and Bytecode Verification][research_kot_kozen_2005]
- [Klohs and Kastens, 2005, Memory Requirements of Java Bytecode Verification on Limited Devices][research_klohs_kastens_2005]
- [Hansen and Siveroni, 2005, Towards Verification of Well-Formed Transactions in Java Card Bytecode][research_hansen_siveroni_2005]
- [Klein, 2005, Verified Java Bytecode Verification Verified Java Bytecode Verification][research_klein_2005]
- [Bernardeschi and others, 2004, Checking secure information flow in Java bytecode by code transformation and standard bytecode verification][research_bernardeschi_defrancesco_2004]
- [Peng and others, 2004, Code sharing among states for stack-caching interpreter][research_peng_wu_2004]
- [Barbuti and Cataudella, 2004, Java bytecode verification on Java cards][research_barbuti_cataudella_2004]
- [Siveroni, 2004, Operational semantics of the Java Card Virtual Machine][research_siveroni_2004]
- [Coglio, 2004, Simple verification technique for complex Java bytecode subroutines][research_coglio_2004]
- [Freund and Mitchell, 2003, A Type System for the Java Bytecode Language and Verifier][research_freund_mitchell_2003]
- [Coglio, 2003, Improving the official specification of Java bytecode verification][research_coglio_2003]
- [Nipkow, 2003, Java Bytecode Verification][research_nipkow_2003]
- [Avvenuti and others, 2003, Java bytecode verification for secure information flow][research_avvenuti_bernardeschi_2003]
- [Leroy, 2003, Java Bytecode Verification Algorithms and Formalizations][research_leroy_2003]
- [Rose, 2003, Lightweight Bytecode Verification][research_rose_2003]
- [Leroy, 2002, Bytecode verification on Java smart cards][research_leroy_2002]
- [Barbuti and others, 2002, Fixing the Java bytecode verifier by a suitable type domain][research_barbuti_tesei_2002]
- [Knoblock and Rehof, 2001, Type elaboration and subtype completion for Java bytecode][research_knoblock_rehof_2001]
- [Klein and Nipkow, 2001, Verified lightweight bytecode verification][research_klein_nipkow_2001]
- [Knoblock and Rehof, 2000, Type elaboration and subtype completion for Java bytecode][research_knoblock_rehof_2000]
- [O'Callahan, 1999, A simple, comprehensive type system for Java bytecode subroutines][research_ocallahan_1999]
- [Stata and Abadi, 1999, A type system for Java bytecode subroutines][research_stata_abadi_1999]
- [Freund and Mitchell, 1999, A type system for object initialization in the Java bytecode language][research_freund_mitchell_1999]
- [Goldberg, 1998, A specification of Java loading and bytecode verification][research_goldberg_1998]
- [Stata and Abadi, 1998, A type system for Java bytecode subroutines][research_stata_abadi_1998]
- [Freund and Mitchell, 1998, A type system for object initialization in the Java bytecode language][research_freund_mitchell_1998]
- [Freund and Mitchell, 1998, A Type System for Object Initialization In the Java Bytecode Language summary][research_freund_mitchell_1998_2]
- [Shih, 1998, An operational semantic approach to continuation style interpreter of logic programs][research_shih_1998]
- [Hoskins, 1988, The design and implementation of a Karel compiler and interpreter][research_hoskins_1988]

- [Gundersen and others, 2013, Atomic Lambda Calculus A Typed Lambda-Calculus with Explicit Sharing][research_gundersen_heijltjes_2013]
- [Liu and others, 2013, Linking Algebraic Semantics and Operational Semantics for Web Services Using Maude][research_liu_zhu_2013]
- [Zhu and others, 2012, Linking operational semantics and algebraic semantics for a probabilistic timed shared-variable language][research_zhu_yang_2012]
- [Wang and Zhu, 2011, Animating the Approach of Deriving Operational Semantics from Algebraic Semantics for Web Services][research_wang_zhu_2011]
- [Colvin and Hayes, 2011, Structural operational semantics through context-dependent behaviour][research_colvin_hayes_2011]
- [Zhu and others, 2009, Animating the Link Between Operational Semantics and Algebraic Semantics for a Probabilistic Timed Shared-Variable Language][research_zhu_yang_2009]
- [Vu, 2008, Denotational semantics for thread algebra][research_vu_2008]
- [Zhu and others, 2008, From algebraic semantics to denotational semantics for Verilog][research_zhu_he_2008]
- [Yang and Duan, 2008, Operational semantics of Framed Tempura][research_yang_duan_2008]
- [Zhu and others, 2007, Algebraic Approach to Operational Semantics and Observation-Oriented Semantics for a Timed Shared-Variable Language with Probability][research_zhu_he_2007]
- [Edalat and Pattinson, 2007, Denotational semantics of hybrid automata][research_edalat_pattinson_2007]
- [Verdejo and Martí-Oliet, 2006, Executable structural operational semantics in Maude][research_verdejo_martioliet_2006]
- [2004, A structural approach to operational semantics][research_a_structural_2004]
- [Popeea and Chin, 2004, A type system for resource protocol verification and its correctness proof][research_popeea_chin_2004]
- [Aceto and Fokkink, 2004, Guesteditors'introduction Specialissueon Structural Operational Semantics][research_aceto_fokkink_2004]
- [Mosses, 2004, Modular structural operational semantics][research_mosses_2004]
- [PLOTKIN, 2004, The origins of structural operational semantics][research_plotkin_2004]
- [Zhu, 2001, Denotational semantics of programming languages and compiler generation in PowerEpsilon][research_zhu_2001]
- [Puchol and others, 1998, An Operational Semantics and Compiler for Real-Time Specifications1][research_puchol_stuart_1998]
- [Royer, 1986, Transformations of denotational semantics in semantics directed compiler generation][research_royer_1986]
- [Mazaher and Berry, 1985, Deriving a compiler from an operational semantics written in VDL][research_mazaher_berry_1985]
- [Clinger, 1984, The scheme 311 compiler an exercise in denotational semantics][research_clinger_1984]
- [Raskovsky, 1982, Denotational semantics as a specification of code generators][research_raskovsky_1982]
- [Bodwin and others, 1982, Experience with an experimental compiler generator based on denotational semantics][research_bodwin_bradley_1982]
- [Jones, 1980, Compiler Generation from Denotational Semantics][research_jones_1980]

- [Zhu and others, 2009, Locality-Based Normal Form Approach to Linking Algebraic Semantics and Operational Semantics for an Event-Driven System-Level Language][research_zhu_zhao_2009]

- [Shukla and others, 2014, A Formal Approach to the Provably Correct Synthesis of Mission Critical Embedded Software for Multi Core Embedded Platforms][research_shukla_nanjundappa_2014]
- [Son and others, 2014, A Reversing Technique for Symbol Table Verification on Compiler Constructions][research_son_oh_2014]
- [Wang and Yang, 2014, Applied Technology in Front-End Implementation of Tiger Compiler Using Hacs Language][research_wang_yang_2014]
- [Pathiran and Prakash, 2014, Design and implementation of a model-based PI-like control scheme in a reset configuration for stable single-loop systems][research_pathiran_prakash_2014]
- [Matsikoudis and Stergiou, 2014, First Draft of the act Programming Language][research_matsikoudis_stergiou_2014]
- [Xu and Zhang, 2014, Formal verification of software safety criteria using Event-B][research_xu_zhang_2014]
- [Poonguzhali and Vinodha, 2014, IMPLEMENTATION OF ANTI-RESET WINDUP SCHEME IN PI CONTROLLER FOR SPHERICAL TANK PROCESS][research_poonguzhali_vinodha_2014]
- [Balu and Saraswathi, 2014, Implementation of SAAS Compiler in Intranet][research_balu_saraswathi_2014]
- [Krebs and Schmitz, 2014, Jaccie A Java-based compiler-compiler for generating, visualizing and debugging compiler components][research_krebs_schmitz_2014]
- [Odegard and others, 2014, Model-Based GN and C Simulation and Flight Software Development for Orion Missions beyond LEO][research_odegardryan_milenkoviczoran_2014]
- [Radonić and others, 2014, One solution of loop invariant code motion compiler optimisation][research_radonic_ukic_2014]
- [Keaton and Seacord, 2014, Performance of Compiler-Assisted Memory Safety Checking][research_keaton_seacord_2014]
- [Abdulsalam and others, 2014, Program energy efficiency The impact of language, compiler and implementation choices][research_abdulsalam_lakomski_2014]
- [Radooevii and Magdalenii, 2014, Python Implementation of Source Code Generator Based on Dynamic Frames][research_radooevii_magdalenii_2014]
- [Hussain and others, 2014, RUGRAT Evaluating program analysis and testing tools and compilers with large generated random benchmark applications][research_hussain_csallner_2014]
- [Tardieu, 2014, Session details Compiler optimizations][research_tardieu_2014]
- [Boldo and others, 2013, A Formally-Verified C Compiler Supporting Floating-Point Arithmetic][research_boldo_jourdan_2013]
- [Kistel and Vandenhouten, 2013, A metamodel-based ASN.1 editor and compiler for the implementation of communication protocols][research_kistel_vandenhouten_2013]
- [Saraf and Dashora, 2013, An Optimal Code Heuristic Approach for Compiler Optimization using Graph Coloring Technique][research_saraf_dashora_2013]
- [Gorringe and Jain, 2013, Architectural considerations for implementation of the ATML standards in an open systems architecture runtime environment OSA-RTS using a graphical environment][research_gorringe_jain_2013]
- [Dong, 2013, Design and Implementation of Compiler Subsystem for Object Oriented Publish/Subscribe Systems][research_dong_2013]
- [Schwaab and Siek, 2013, Modular type-safety proofs in Agda][research_schwaab_siek_2013]
- [Barash and Shchur, 2013, RNGSSELIB Program library for random number generation. More generators, parallel streams of random numbers and Fortran compatibility][research_barash_shchur_2013]
- [Chatterjee, 2013, Runtime Systems for Extreme Scale Platforms][research_chatterjee_2013]
- [Dejtrakulwong and others, 2013, Sensitivity analysis and cascaded interpretation scheme for subtle seismic signatures in thin shaly-sand reservoirs][research_dejtrakulwong_mavko_2013]
- [Bond, 2013, Session details Garbage collection, runtime, and cache management][research_bond_2013]
- [2012, A Compositional Scheme and Framework for Safety Critical Systems Verification][research_a_compositional_2012]
- [Nair, 2012, A Formal Semantics for Ciset and Ciset Relation Operators][research_nair_2012]
- [Pike and others, 2012, Experience Report A Do-It-Yourself High-Assurance Compiler][research_pikelee_wegmannnis_2012]
- [Grechanik, 2012, Random benchmark application generation for evaluating program analysis and testing tools][research_grechanik_2012]
- [Aung and others, 2011, Compiler-assisted technique for rapid performance estimation of FPGA-based processors][research_aung_lam_2011]
- [Schliephake and others, 2011, Design and Implementation of a Runtime System for Parallel Numerical Simulations on Large-Scale Clusters][research_schliephake_aguilar_2011]
- [Agathos and others, 2011, Design and Implementation of OpenMP Tasks in the OMPi Compiler][research_agathos_hadjidoukas_2011]
- [Bansal and Singh, 2011, Dual Stack Implementation of Mobile IPv6 Software Architecture][research_bansal_singh_2011]
- [Magdalenić and others, 2011, Implementation Model of Source Code Generator][research_magdalenic_radosevic_2011]
- [Zaitsev and Guliaiev, 2011, Stack E6 and Its Implementation within Linux Kernel][research_zaitsev_guliaiev_2011]
- [Larkins and Jones, 2011, Targeting FPGA-based processors for an implementation-driven compiler construction course][research_larkins_jones_2011]
- [Snavely, 2011, Test and Evaluation of Architecture-Aware Compiler Environment][research_snavely_2011]
- [Jiang and others, 2010, A Debugging Approach for Java Runtime Exceptions Based on Program Slicing and Stack Traces][research_jiang_zhang_2010]
- [Eachempati and others, 2010, An open-source compiler and runtime implementation for Coarray Fortran][research_eachempati_jun_2010]
- [Manjunath, 2010, Colored Steganography Implementation Scheme of Images using Transform Technique][research_manjunath_2010]
- [Chalin, 2010, Engineering a Sound Assertion Semantics for the Verifying Compiler][research_chalin_2010]
- [Rosenblum and others, 2010, Extracting compiler provenance from program binaries][research_rosenblum_miller_2010]
- [Orlic, 2010, Implementation by capture with executable UML][research_orlic_2010]
- [Jiang and Yan, 2010, Implementation of Static Web-Pages Generator Using JavaScript][research_jiang_yan_2010]
- [Desai, 2009, A Novel Technique for Orchestration of Compiler Optimization Functions Using Branch and Bound Strategy][research_desai_2009]
- [Rodríguez and others, 2009, CPPC a compiler-assisted tool for portable checkpointing of message-passing applications][research_rodriguez_martin_2009]
- [Canedo and others, 2009, Design and implementation of a queue compiler][research_canedo_abderazek_2009]
- [Denney and Fischer, 2009, Generating Code Review Documentation for Auto-Generated Mission-Critical Software][research_denneyewen_fischerbernd_2009]
- [Hiroyuki, 2009, Idiom Recognition and Program Scheme Recognition Based Program Transformations for Performance Tuning--Beyond Compiler Optimizations][research_hiroyuki_2009]
- [Oiwa, 2009, Implementation of the memory-safe full ANSI-C compiler][research_oiwa_2009]
- [Pasareanu and others, 2009, Model Based Analysis and Test Generation for Flight Software][research_pasareanucorinas_schumannjohannm_2009]
- [Seshia and Rakhlin, 2009, Quantitative Analysis of Embedded Software Using Game-Theoretic Learning][research_seshia_rakhlin_2009]
- [Reb and others, 2008, A JML Compiler Based on AspectJ][research_reb_lima_2008]
- [Bushnell and others, 2008, Automatic Testcase Generation for Flight Software][research_bushnelldavidhenry_pasareanucorina_2008]
- [YU, 2008, Design and implementation of NC code compiler based on ANTLR][research_yu_2008]
- [Leinenbach and Petrova, 2008, Pervasive Compiler Verification From Verified Programs to Verified Systems][research_leinenbach_petrova_2008]
- [Zanardini, 2008, The Semantics of Abstract Program Slicing][research_zanardini_2008]
- [Lucchi and Mazzara, 2007, A pi-calculus based semantics for WS-BPEL][research_lucchi_mazzara_2007]
- [Chalin, 2007, A Sound Assertion Semantics for the Dependable Systems Evolution Verifying Compiler][research_chalin_2007]
- [Bohnet and Dollner, 2007, CGA Call Graph Analyzer - Locating and Understanding Functionality within the Gnu Compiler Collection's Million Lines of Code][research_bohnet_dollner_2007]
- [Chen and others, 2007, Design of a Certifying Compiler Supporting Proof of Program Safety][research_chen_ge_2007]
- [TOKUMORI and others, 2007, Development of Metadata Generation Support System Using Compiler Compiler][research_tokumori_ono_2007]
- [de Niz, 2007, Diagrams and Languages for Model-Based Software Engineering of Embedded Systems UML and AADL][research_deniz_2007]
- [Dubach and others, 2007, Fast compiler optimisation evaluation using code-feature based performance prediction][research_dubach_cavazos_2007]
- [Costagliola and others, 2007, Visual language implementation through standard compiler-compiler techniques][research_costagliola_deufemia_2007]
- [Heimbigner, 2006, A Tamper-Resistant Programming Language System][research_heimbigner_2006]
- [Butterfield and Woodcock, 2006, A "Hardware Compiler" Semantics for Handel-C][research_butterfield_woodcock_2006]
- [Azeemi, 2006, Compiler Directed Battery-Aware Implementation of Mobile Applications][research_azeemi_2006]
- [Bicarregui and others, 2006, The verified software repository a step towards the verifying compiler][research_bicarregui_hoare_2006]
- [Sadat, 2005, A Compiler Driven Simulation Technique for the Analysis of Digital Logic Circuit][research_sadat_2005]
- [Guyer and Lin, 2005, Broadway A Compiler for Exploiting the Domain-Specific Semantics of Software Libraries][research_guyer_lin_2005]
- [2005, Fifth IEEE International Workshop on Source Code Analysis and Manipulation][research_fifth_ieee_2005]
- [Denney and Fischer, 2005, Formal Safety Certification of Aerospace Software][research_denneyewen_fischerbernd_2005]
- [Xia and DiVito, 2005, Software Certification for Temporal Properties With Affordable Tool Qualification][research_xiasongtao_divitobenedettol_2005]
- [Shin and others, 2004, AIRES Automatic Integration of Reusable Embedded Software, Methodologies, Toolkit, and Experiments][research_shin_wang_2004]
- [2004, Fourth IEEE International Workshop on Source Code Analysis and Manipulation][research_fourth_ieee_2004]
- [Amarasinghe, 2004, Session details Compiler and simulator construction][research_amarasinghe_2004]
- [Necula and Lee, 2004, The design and implementation of a certifying compiler][research_necula_lee_2004]
- [Pla, 2004, Weapon System Software Technology Support WSSTS . Delivery Order 0008 Real-Time Java for Embedded Systems RTJES][research_pla_2004]
- [Dold and others, 2003, A Completely Verified Realistic Bootstrap Compiler][research_dold_henke_2003]
- [2003, ART An Implementation on the Active_object RunTime Systems Applicable for the Embedded Systems][research_art_an_2003]
- [2003, Proceedings Third IEEE International Workshop on Source Code Analysis and Manipulation][research_proceedings_third_2003]
- [Uh, 2003, Session details Compiler optimizations][research_uh_2003]
- [Hsu and Kremer, 2003, The design, implementation, and evaluation of a compiler algorithm for CPU energy reduction][research_hsu_kremer_2003]
- [League, 2002, A Type-Preserving Compiler Infrastructure][research_league_2002]
- [Goos, 2002, Compiler Verification and Compiler Architecture][research_goos_2002]
- [2002, Proceedings Second IEEE International Workshop on Source Code Analysis and Manipulation][research_proceedings_second_2002]
- [Orlitsky, 2002, Scalar versus vector quantization worst case analysis][research_orlitsky_2002]
- [Kandemir, 2001, A compiler technique for improving whole-program locality][research_kandemir_2001]
- [Zendra and Colnet, 2001, Coping with aliasing in the GNU Eiffel Compiler implementation][research_zendra_colnet_2001]
- [Kennedy and Syme, 2001, Design and implementation of generics for the .NET Common language runtime][research_kennedy_syme_2001]
- [MacMillen, 2001, Nimble Compiler Environment for Agile Hardware. Volume 1][research_macmillen_2001]
- [Calzarossa and others, 2001, Performance issues of an HPF-like compiler][research_calzarossa_massari_2001]
- [Auguston and others, 2001, Visual Meta-Programming Language][research_auguston_berzins_2001]
- [Lin and Padua, 2000, Compiler analysis of irregular memory accesses][research_lin_padua_2000]
- [Havelund and others, 2000, Formal Analysis of the Remote Agent Before and After Flight][research_havelundklaus_lowrymike_2000]
- [Orr and Henderson, 2000, Space Shuttle Software Development and Certification][research_orrjamesk_hendersonjohnniea_2000]
- [Frigo, 1999, A fast Fourier transform compiler][research_frigo_1999]
- [van Deursen, 1999, Modern Compiler Implementation in Java][research_vandeursen_1999]
- [Nielsen, 1998, Compiler Support for Message Passing Systems][research_nielsen_1998]
- [1998, Compiler technology Tools, translators and language implementation][research_compiler_technology_1998]
- [Stöhr and O'Boyle, 1998, First Fast Sink A compiler algorithm for barrier placement optimisation][research_stohr_oboyle_1998]
- [1998, Modern compiler implementation in Java Revised and expanded edition][research_modern_compiler_1998]
- [Haspert and Beauregard, 1998, The Commercialization of a Rapid Prototyping Development Tool for Real-Time Embedded Software Intensive, Process, and Resource Management Systems][research_haspert_beauregard_1998]
- [Necula and Lee, 1998, The design and implementation of a certifying compiler][research_necula_lee_1998]
- [Nielsen, 1997, Compiler Support for Message Passing Systems][research_nielsen_1997]
- [Stoonkisto and Subhlok, 1997, Coordinating Foreign Modules with a Parallelizing Compiler][research_stoonkisto_subhlok_1997]
- [Kelly, 1997, Formal Methods Specification and Analysis Guidebook for the Verification of Software and Computer Systems Volume II A Practitioner's Companion][research_kellyjohnc_1997]
- [1997, Modern compiler implementation in C Basic techniques][research_modern_compiler_1997]
- [1997, Modern compiler implementation in Java Basic techniques][research_modern_compiler_1997_2]
- [1997, Modern compiler implementation in ML Basic techniques][research_modern_compiler_1997_3]
- [Cousot, 1997, Program analysis][research_cousot_1997]
- [Pratt, 1997, Second Calculus of Binary Relations as a Concurrent Programming Language][research_pratt_1997]
- [Badler, 1996, A Task Networking and Visual Programming Language for Jack][research_badler_1996]
- [Ferrante and Allard, 1996, Introducing a CPS style optimizer into an existing compiler][research_ferrante_allard_1996]
- [Cousot, 1996, Program analysis][research_cousot_1996]
- [Evansi and Sulaiman, 1996, Solving optimisation problems using neucomp-a neural network compiler][research_evansi_sulaiman_1996]
- [Porcher, 1995, Benchmarking the POMPC compiler on the Connection Machine CM-2][research_porcher_1995]
- [1995, Formal Methods Specification and Analysis Guidebook for the Verification of Software and Computer Systems A Practitioner's Companion - Volume 2][research_formal_methods_1995]
- [1995, Formal Methods Specification and Verification Guidebook for Software and Computer Systems Planning and Technology Insertion - Volume 1][research_formal_methods_1995_2]
- [Graham, 1995, Information Technology. Programming Language. The SQL Ada Module Description Language SAMeDL][research_graham_1995]
- [Davenport, 1995, Object-Oriented Visual Programming Language. Phase 1][research_davenport_1995]
- [Ertl, 1995, Stack caching for interpreters][research_ertl_1995]
- [Oliva and others, 1995, The VLISP verified PreScheme compiler][research_oliva_ramsdell_1995]
- [Brodersen, 1994, Anatomy of a Silicon Compiler][research_brodersen_1994]
- [Chi, 1994, Compiler Optimization Technique for Data Cache Prefetching Using a Small CAM Array][research_chi_1994]
- [Atapattu, 1994, Design of a Parallel Object Oriented Programming Language][research_atapattu_1994]
- [Surati, 1993, A Parallelizing Compiler Based on Partial Evaluation][research_surati_1993]
- [Rogers, 1993, Ada Embedded Computer Software Support AECSS][research_rogers_1993]
- [Plishka and Ifarraguerri, 1993, Evaluation of Alsys 037 Ada Compiler][research_plishka_ifarraguerri_1993]
- [Butler and Johnson, 1993, Formal Methods for Life-Critical Software][research_butlerrickyw_johnsonsallyc_1993]
- [Bailin and others, 1993, Model-based reasoning for system and software engineering The Knowledge From Pictures KFP environment][research_bailinsydney_paterrafrank_1993]
- [Gaál, 1993, Parallel compiler generation][research_gaal_1993]
- [Herring and others, 1993, Research in Presistent Simulation Development of the Persistent ModSim Object-Oriented Programming Language][research_herring_kalathil_1993]
- [Consel and Cheng Khoo, 1993, Semantics-directed generation of a prolog compiler][research_consel_chengkhoo_1993]
- [Ching and Katz, 1993, The testing of an APL compiler][research_ching_katz_1993]
- [Mary-Anne K Posenau, 1993, Unstructured Grid Generation Techniques and Software][research_maryannekposenau_1993]
- [Hoang and Rabaey, 1992, A compiler for multiprocessor DSP implementation][research_hoang_rabaey_1992]
- [Harper and Pfenning, 1992, A Module System for a Programming Language Based on the LF Logical Framework][research_harper_pfenning_1992]
- [Russinoff, 1992, A verified prolog compiler for the Warren Abstract Machine][research_russinoff_1992]
- [Ooashi and others, 1992, ASL program written in abstract sequential machine style and its compiler][research_ooashi_taniguchi_1992]
- [Palsberg, 1992, Provably Correct Compiler Generation][research_palsberg_1992]
- [Gifford and others, 1992, Report on the FX-91 Programming Language][research_gifford_jouvelot_1992]
- [Schmitz, 1992, The visual compiler-compiler SIC abstract][research_schmitz_1992]
- [Leavitt and Terrell, 1991, Ada Compiler Evaluation Capability][research_leavitt_terrell_1991]
- [Leavitt and Terrell, 1991, ADA Compiler Evaluation Capability User's Guide, Release 2.0][research_leavitt_terrell_1991_2]
- [Leavitt and Terrell, 1991, Ada Compiler Evaluation Capability. Release 2.0][research_leavitt_terrell_1991_3]
- [Hird, 1991, Formal specification and verification of Ada software][research_hirdgeoffreyr_1991]
- [Lane and Poorman, 1991, Preserving software investment using new fortran compiler technology][research_lane_poorman_1991]
- [Shivers, 1991, The semantics of Scheme control-flow analysis][research_shivers_1991]
- [Ramkumar and Kale, 1990, A Chare kernel implementation of a parallel Prolog compiler][research_ramkumar_kale_1990]
- [Wilson, 1990, Ada/Ed Compiler, Version 1.10 UNIX][research_wilson_1990]
- [Wilson, 1990, Ada/Ed Compiler, Version 1.10 VAX][research_wilson_1990_2]
- [Gupta, 1990, An Incremental Type Inference System for the Programming Language Id][research_gupta_1990]
- [Heuring and others, 1990, Automatic Compiler Construction][research_heuring_waite_1990]
- [Liangliang and Yungui, 1990, Clause representations in a compiler-based prolog database][research_liangliang_yungui_1990]
- [Giorgi and Le Métayer, 1990, Continuation-based parallel implementation of functional programming languages][research_giorgi_lemetayer_1990]
- [Sharp, 1990, Pythia A Parallel Compiler for Delirium][research_sharp_1990]
- [Rosing and others, 1990, The DINO Parallel Programming Language][research_rosing_schnabel_1990]
- [Woronow, 1989, Correction for a "FORTRAN program for generation of multivariate normally distributed random variables"][research_woronow_1989]
- [Harrison, 1989, Research, Development, Training and Education Using the Ada Programming Language][research_harrison_1989]
- [Vegdahl and Pleban, 1989, The runtime environment for Scheme, a Scheme implementation on the 88000][research_vegdahl_pleban_1989]
- [Horwat, 1988, A Concurrent Smalltalk Compiler for the Message-Driven Processor][research_horwat_1988]
- [Weiner and Ramakrishman, 1988, A piggy-back compiler for Prolog][research_weiner_ramakrishman_1988]
- [Harmon, 1988, An Ada implementation of Marsaglia's universal random number generator][research_harmon_1988]
- [Tuck, 1988, An Optimally Portable SIMD Single-Instruction Multiple-Data Programming Language][research_tuck_1988]
- [Keutzer and Wolf, 1988, Anatomy of a hardware compiler][research_keutzer_wolf_1988]
- [Andrews and others, 1988, Design and implementation of the UW Illustrated compiler][research_andrews_henry_1988]
- [Sinharoy, 1988, EPL - Equational Programming Language Parsing and Dimension Propagation][research_sinharoy_1988]
- [Lehman and others, 1988, Sources of Compiler Capability Information in Validation Summary Reports][research_lehman_hook_1988]
- [Manna, 1988, TABLOG The Deductive Tableau Programming Language][research_manna_1988]
- [Ghosh and Kulatilake, 1987, A FORTRAN program for generation of multivariate normally distributed random variables][research_ghosh_kulatilake_1987]
- [Lee and Pleban, 1987, A realistic compiler generator based on high-level semantics another progress report][research_lee_pleban_1987]
- [Donohoe, 1987, A Survey of Real-Time Performance Benchmarks for the Ada Programming Language][research_donohoe_1987]
- [Bonar and Liffick, 1987, A Visual Programming Language for Novices][research_bonar_liffick_1987]
- [Kingsley, 1987, The implementation of a state machine compiler][research_kingsley_1987]
- [Guarna and Jr, 1987, VPC - A Proposal for a Vector Parallel C Programming Language][research_guarna_jr_1987]
- [Scott, 1986, The Interface Between Distributed Operating System and High-Level Programming Language. Revision][research_scott_1986]
- [Sager, 1985, A technique for creating small fast compiler frontends][research_sager_1985]
- [Grover, 1985, Guidelines for a Minimal Ada Runtime Environment][research_grover_1985]
- [Touzeau, 1984, A Fortran compiler for the FPS-164 scientific computer][research_touzeau_1984]
- [Schmidt and Völler, 1984, A multi-language compiler system with automatically generated codegenerators][research_schmidt_voller_1984]
- [Howe, 1984, A Study of the Feasibility of Duplicating JAMPS Applications Software in the Ada Programming Language][research_howe_1984]
- [Blower, 1984, An efficient implementation of visibility in Ada][research_blower_1984]
- [Pleban, 1984, Compiler prototyping using formal semantics][research_pleban_1984]
- [Milos and others, 1984, Direct implementation of compiler specifications or the pascal p-code compiler revisited][research_milos_pleban_1984]
- [Mössenböck, 1984, Ein einfacher Compiler-Compiler für Mikrocomputer / Α simple compiler-compiler for microcomputer][research_mossenbock_1984]
- [Robbins, 1984, Engineering a high-capacity Pascal compiler for high performance][research_robbins_1984]
- [Aigrain and others, 1984, Experience with a Graham-Glanville style code generator][research_aigrain_graham_1984]
- [Christopher and others, 1984, Using dynamic programming to generate optimized code in a Graham-Glanville style code generator][research_christopher_hatcher_1984]
- [Schmeck, 1983, Algebraic semantics of recursive flowchart schemes][research_schmeck_1983]
- [CARNEY and LABAUGH, 1983, Efficient compiler implementation for a spaceborne image processing demonstration system][research_carney_labaugh_1983]
- [Reiss, 1983, Generation of Compiler Symbol Processing Mechanisms from Specifications][research_reiss_1983]
- [Paulson, 1982, A semantics-directed compiler generator][research_paulson_1982]
- [Ganzinger and others, 1982, A truly generative semantics-directed compiler generator][research_ganzinger_giegerich_1982]
- [Moor, 1982, An applicative compiler for a parallel machine][research_moor_1982]
- [Auslander and Hopkins, 1982, An overview of the PL.8 compiler][research_auslander_hopkins_1982]
- [Fusaoka and Hirayama, 1982, Compiler chip][research_fusaoka_hirayama_1982]
- [Koskimies and others, 1982, Compiler construction using attribute grammars][research_koskimies_raiha_1982]
- [Sethi, 1982, Control flow aspects of semantics directed compiling Summary][research_sethi_1982]
- [Falis, 1982, Design and implementation in Ada of a runtime task supervisor][research_falis_1982]
- [Kipps, 1982, Experience with porting techniques on a COBOL 74 compiler][research_kipps_1982]
- [Gallaher, 1982, Investigate Capability of Ada Higher Order Programming Language for Developing Machine Independent Software][research_gallaher_1982]
- [Seyfer, 1982, Tailoring testing to a specific compiler---experiences][research_seyfer_1982]
- [Marshall, 1982, The linear graph package, a compiler building environment][research_marshall_1982]
- [Jones and Christiansen, 1981, Control Flow Treatment in a Simple Semantics-Directed Compiler Generator][research_jones_christiansen_1981]
- [Hart and McClanahan, 1981, JOVIAL J73 Compiler Validator][research_hart_mcclanahan_1981]
- [Loy, 1981, Notes on the Implementation of MUSBOX A Compiler for the Systems Concepts Digital Synthesizer][research_loy_1981]
- [1981, Ruggedized minicomputer hardware and software topics, 1981 Proceedings of the 4th ROLM MIL-SPEC Computer User's Group Conference][research_ruggedized_minicomputer_1981]
- [Leverett and others, 1979, An Overview of the Production Quality Compiler-Compiler Project][research_leverett_cattell_1979]
- [Bonyun, 1979, Euclid Compiler for PDP-11][research_bonyun_1979]
- [Feldman, 1979, Implementation of a portable Fortran 77 compiler using modern tools][research_feldman_1979]
- [Bonkowski and others, 1979, Porting the Zed compiler][research_bonkowski_gentleman_1979]
- [Guessarian, 1979, Program transformations and algebraic semantics][research_guessarian_1979]
- [Deransart, 1979, Proof by semantic attributes of a LISP compiler][research_deransart_1979]
- [Abrahams, 1979, The CIMS PL/I compiler][research_abrahams_1979]
- [Pleban, 1979, The use of transition matrices in a recursive-descent compiler][research_pleban_1979]
- [Evans and others, 1978, A Compiler Compiler and Methodology for Problem Oriented Language Compiler Implementors][research_evans_lockington_1978]
- [Payne, 1978, A formalised technique for expressing compiler exercisers][research_payne_1978]
- [Bonyun and Holt, 1978, EUCLID Compiler for PDP-11][research_bonyun_holt_1978]
- [Lynn, 1978, Interactive Compiler Proving Using Hoare Proof Rules][research_lynn_1978]
- [Johnson, 1978, Tools For Automatic Compiler Generation Panel Discussion][research_johnson_1978]
- [Williams and Bulmer, 1978, Use of a formal notation for static semantics in compiler design][research_williams_bulmer_1978]
- [Baird and Oliver, 1977, Programming Language Standards -- Who Needs Them][research_baird_oliver_1977]
- [Lange and others, 1977, Specification for a STARAN Programming Language][research_lange_cheeseman_1977]
- [Fisher, 1976, A Common Programming Language for the Department of Defense--Background and Technical Requirements][research_fisher_1976]
- [Krzemień and Lukasiewicz, 1976, Automatic generation of lexical analyzers in a compiler-compiler][research_krzemien_lukasiewicz_1976]
- [Goodenough and others, 1976, Evaluation of ALGOL 68, JOVIAL J3B, PASCAL, SIMULA 67, and TACPOL vs. TINMAN Requirements for a Common High Order Programming Language][research_goodenough_mcgowan_1976]
- [Ganzinger and others, 1976, MUG1 - an incremental compiler-compiler][research_ganzinger_ripken_1976]
- [Harrison and others, 1976, Theoretical results in compiler design and implementation Tutorial Session][research_harrison_graham_1976]
- [Snyder, 1975, A Portable Compiler for the Language C][research_snyder_1975]
- [Newey, 1975, Formal Sematics of LISP with Applications to Program Correctness][research_newey_1975]
- [Gorelik and Khukhlaev, 1975, Implementation of the incremental fortran compiler][research_gorelik_khukhlaev_1975]
- [Zelkowitz, 1975, Third generation compiler design][research_zelkowitz_1975]
- [Laliotis, 1973, Implementation aspects of the symbol hardware compiler][research_laliotis_1973]
- [1973, Implementation of a Pascal compiler for the CII IRIS 80 computer][research_implementation_of_1973]
- [Malcolm, 1971, PL360 Revised . A Programming Language for the IBM360][research_malcolm_1971]
- [Cowan and Graham, 1970, Design characteristics of the WATFOR compiler][research_cowan_graham_1970]
- [Cheatham and Standish, 1970, Optimization aspects of compiler- compilers][research_cheatham_standish_1970]
- [Finkelstein, 1968, A compiler optimization technique][research_finkelstein_1968]
- [Moore, 1968, Data Processing with the Compiler Compiler][research_moore_1968]
- [Pankhurst, 1968, GULP---A compiler-compiler for verbal and graphic languages][research_pankhurst_1968]
- [Bayer and others, 1968, MPL MATHEMATICAL PROGRAMMING LANGUAGE][research_bayer_bigelow_1968]
- [Trout, 1967, A compiler---compiler system][research_trout_1967]
- [Mondshein, 1967, VITAL COMPILER SYSTEM REFERENCE MANUAL][research_mondshein_1967]
- [Feldman, 1966, A formal semantics for computer languages and its application in a compiler-compiler][research_feldman_1966]
- [Campbell and Beck, 1965, THE FORAST PROGRAMMING LANGUAGE FOR ORDVAC AND BRLESC REVISED][research_campbell_beck_1965]
- [BOOK and others, 1963, A ONE PASS JOVIAL COMPILER][research_book_bratman_1963]
- [KELLY, 1963, ADVANCED MYSTIC- A COMPILER FOR MANAGEMENT CONTROL OF COMPUTER PROGRAMMING][research_kelly_1963]
- [Jervis, 1963, MOBILE. A MOBIDIC COBOL COMPILER][research_jervis_1963]

### The surrounding systems literature

The harvest returned a large body of work that is adjacent rather than central, being compiler, runtime and
systems research that shares the article's vocabulary without addressing its question.
**It is listed rather than discarded because the selection that produced it is reported in full**, and a
survey that presents only the records supporting its thesis has selected twice, once by query and once by
judgement, while reporting one selection.

- [Kuroda and Yuen, 2026, A Concurrent Extension of Reversible Imperative Programming Language with Runtime][research_kuroda_yuen_2026]
- [Attrot and others, 2026, A Pattern Generation Language for MLIR Compiler Matching and Rewriting][research_attrot_zago_2026]
- [bounpaserth, 2026, A Study of the Computer Programming Language Implementation in Computer Engineering Students using the Flowgorithm Platform versus Common Programming][research_bounpaserth_2026]
- [Sun and Staron, 2026, Agentic Pipelines in Embedded Software Engineering Emerging Practices and Challenges][research_sun_staron_2026]
- [Iida and others, 2026, An Efficient Runtime Verification Toolkit for Self-Adaptive Systems Addressing Runtime System Model Changes][research_iida_oishi_2026]
- [Jadhav and others, 2026, Analysis of Compiler-Level Static and Dynamic Features for Automated Bug Prediction Using Transformer Models][research_jadhav_devale_2026]
- [Aisyiyah and Eviyanti, 2026, Android-based Programming Language to Natural Language Translator App][research_aisyiyah_eviyanti_2026]
- [Qin and others, 2026, Augmenting LLM Code Translation with Compiler Analysis for C to Triton Kernel Generation][research_qin_xia_2026]
- [Kahn and others, 2026, Big-Stop Semantics Small-Step Semantics in a Big-Step Judgment][research_kahn_hoffmann_2026]
- [Kasaraneni and Nandivada, 2026, Compact Representation and Interleaved Solving for Scalable Constraint-Based Points-to Analysis][research_kasaraneni_nandivada_2026]
- [Cheng and others, 2026, Denotation-based Compositional Compiler Verification][research_cheng_wu_2026_2]
- [Deng and others, 2026, Design and Implementation of an OCaml-Based Standalone SystemVerilog Preprocessor Compliant with IEEE 1800-2023][research_deng_he_2026]
- [Altan, 2026, Error-Resilient Quantum Compiler Design for Efficient Qubit Mapping, Gate Optimization, and Noise Mitigation in NISQ-Era Devices][research_altan_2026]
- [Wu and others, 2026, Fluctuation-guided adaptive random compiler for Hamiltonian simulation][research_wu_fan_2026]
- [Arakaki and Hirokawa, 2026, Foundational Design of Multi-Modal Typed Programming Language for Quantum-Classical Hybrid Computing System][research_arakaki_hirokawa_2026]
- [Duţu and others, 2026, From Runtime Reflection to Compile-Time Specialization A Template-Based Approach to Runtime Libraries][research_dutu_guiman_2026]
- [Jackson, 2026, I/O Optimisation at the Compiler Level IOOpt][research_jackson_2026]
- [Lai and others, 2026, Interaction-aware multi-objective optimization method for LLVM compiler option sequences][research_lai_qiao_2026]
- [Xiang and others, 2026, LoopHint A Compiler-Assisted Loop Branch Predictor for Embedded DSPs][research_xiang_xu_2026]
- [2026, NOCI-COMPILER A THEORETICAL ARCHITECTURE FOR THE SEMANTIC TRANSLATION OF NOCICEPTIVE SIGNALS INTO A DIGITAL PAIN ALPHABET][research_noci_compiler_a_2026]
- [Kishorbhai and Patel, 2026, Online Code Compiler A Modern Web Based Programming Platform][research_kishorbhai_patel_2026]
- [Du, 2026, Performance Verification of BFS For Unweighted Maze Solving A Comparative Analysis with DFS and A* Via Ocaml Implementation][research_du_2026]
- [Dong and others, 2026, Presynthesis Towards Scaling Up Program Synthesis with Finer-Grained Abstract Semantics][research_dong_wu_2026]
- [Aziz and Labiche, 2026, ProtoSYCL A Sample Implementation of a SYCL Compiler for Conformance Test Suite Development][research_aziz_labiche_2026]
- [Wang and others, 2026, Random test generators demystified Differences and potential for compiler reliability][research_wang_lu_2026]
- [Maity and Ghose, 2026, SAGE A Compiler-assisted Reinforcement Learning-based Offloading Approach under Near-memory Processing Paradigm][research_maity_ghose_2026]
- [2026, Syntax-Directed Semantics in Programming Language Design][research_syntax_directed_semantics_2026]
- [Arriaga and others, 2026, Tempo An ML-KEM to PAKE Compiler Resilient to Timing Attacks][research_arriaga_barbosa_2026]
- [Avigad and others, 2025, A Proof-Producing Compiler for Blockchain Applications][research_avigad_goldberg_2025]
- [Petchartee, 2025, A Universal Quantum Compiler GPT Multi-Framework Optimization and Translation Using Large Language Models][research_petchartee_2025]
- [Delaët and others, 2025, Abstract machines and small-step semantics a winning ticket for proof automation?][research_delaet_blazy_2025]
- [Fan and others, 2025, Adaptive random compiler for Hamiltonian simulation][research_fan_wu_2025]
- [Pasupuleti, 2025, AI-Guided Quantum Compiler Design Using Superalgebraic Symmetries][research_pasupuleti_2025]
- [Bai and others, 2025, APCer An Agile Physical Compiler for Multi-Port Register File][research_bai_ming_2025]
- [Liu and Lu, 2025, Bi-directional Taint Flow Analysis A High-precision Static Detection Approach for Java Deserialization Vulnerabilities][research_liu_lu_2025]
- [Heo and others, 2025, Bit-level compiler optimization for ultra low-power embedded systems][research_heo_kim_2025]
- [Puranik, 2025, Bridging Formal Methods and Software Engineering Through a Tagless-Final Embedded DSL for Program Semantics][research_puranik_2025]
- [Zhang, 2025, Comparative Implementation of Binary Tree and Recursive Backtracking Maze Generation Algorithms in OCaml][research_zhang_2025]
- [Pandey, 2025, Compiler Design and Its Construction][research_pandey_2025]
- [Wu and others, 2025, Compiler Optimization Testing Based on Optimization-Guided Equivalence Transformations][research_wu_zheng_2025]
- [Matteo R. Donelli, 2025, Compiler-Assisted Optimization Using Neural Code Embeddings for Heterogeneous Architectures][research_matteordonelli_2025]
- [Jadhav and Falk, 2025, Compiler-level DMA-aware multi-objective dynamic SPM allocation][research_jadhav_falk_2025]
- [Astarte, 2025, Conceptualising Programming Language Semantics][research_astarte_2025]
- [Chen and others, 2025, De-duplicating Silent Compiler Bugs via Deep Semantic Representation][research_chen_fan_2025]
- [Hensley and Elgazzar, 2025, DESIGN AND IMPLEMENTATION OF THE MOREHEAD-AZALEA COMPILER MAC][research_hensley_elgazzar_2025]
- [Ghuzdewan, 2025, Development of a Python-Based Program for Pareto Analysis in Construction Project Cost Management][research_ghuzdewan_2025]
- [He and others, 2025, Evaluating Program Semantics Reasoning with Type Inference in System F][research_he_yang_2025]
- [Seassau and others, 2025, Formal Semantics and Program Logics for a Fragment of OCaml][research_seassau_yoon_2025]
- [Yang and others, 2025, Formal Verification of a Custom Compiler for a Fully Homomorphic Encryption Accelerator][research_yang_banerjee_2025]
- [He and Zhong, 2025, From Bug Reports to Workarounds The Real-World Impact of Compiler Bugs][research_he_zhong_2025]
- [Bourke and others, 2025, Functional Stream Semantics for a Synchronous Block-Diagram Compiler][research_bourke_jeanmaire_2025]
- [S and others, 2025, Impact of Peer-Based Feedback Mechanisms on Understanding Programming Language][research_s_v_2025]
- [Minato and others, 2025, Implementation and Evaluation of a System Call Moving Target Defense Applied Multiple Times at Runtime for Binary Injections][research_minato_masumoto_2025]
- [Sack, 2025, Interfacing Programming Language Semantics and Pragmatics What Does "Hello, World" Mean?][research_sack_2025]
- [Brant and others, 2025, IoT-CODIFT Compiler Optimization DIFT for IoT and Embedded Devices][research_brant_sunkara_2025]
- [Olteanu and Oprişa, 2025, LambdaGo A Functional Extension of the Go Programming Language][research_olteanu_oprisa_2025]
- [Li and others, 2025, Lightweight and Holistic-Scalable Serverless Secure Container Runtime for High-Density Deployment and High-Concurrency Startup][research_li_wu_2025]
- [Cummins and others, 2025, LLM Compiler Foundation Language Models for Compiler Optimization][research_cummins_seeker_2025]
- [Chaplygin, 2025, Modeling and implementation of Common LISP functional language compiler][research_chaplygin_2025]
- [Qassir, 2025, MyDSL Front-End Compiler Design for a User-Friendly Language Supporting Hybrid Meta-Heuristics][research_qassir_2025]
- [Recharla, 2025, Parallel Sparse Matrix Algorithms in OCaml v5 Implementation, Performance, and Case Studies][research_recharla_2025]
- [Midtgaard, 2025, Property-Based Testing of OCaml 5's Runtime System][research_midtgaard_2025]
- [2025, Quantum Software Engineering Algorithm Design, Error Mitigation, and Compiler Optimization for Fault-Tolerant Quantum Computing][research_quantum_software_2025]
- [Abu-Yosef and Kong, 2025, Scalable Data-Flow Modeling and Validation of Distributed-Memory Algorithms][research_abuyosef_kong_2025]
- [Austen and others, 2025, Sharing Is Scaring Linking Cloud File-Sharing to Programming Language Semantics][research_austen_krishnamurthi_2025]
- [Zelenova, 2025, Static Memory Layout for Real-Time Operating Systems][research_zelenova_2025]
- [Applis and others, 2025, Suspicious Types and Bad Neighborhoods Filtering Spectra with Compiler Information][research_applis_gissurarson_2025]
- [Tan and others, 2025, The Burden of Proof Automated Tooling for Rapid Iteration on Large Mechanised Proofs][research_tan_donaldson_2025]
- [Rowland and Perugini, 2025, The Formal Semantics and Implementation of a Domain-Specific Language for Mixed-Initiative Dialogs][research_rowland_perugini_2025]
- [S.Venkatesan, 2025, TOWARDS AUTONOMOUS CODE OPTIMIZATION A REINFORCEMENT LEARNING FRAMEWORK FOR COMPILER DESIGN][research_svenkatesan_2025]
- [Carlos Paradis and others, 2025, Towards Streamlining Auditing for Compliance With Requirements in Open-Source Software at NASA][research_carlosparadis_ivanperez_2025]
- [Sholihin and Hidayati, 2024, A Forward Chaining Expert System for Personalized Programming Language Selection][research_sholihin_hidayati_2024]
- [Narkthong and others, 2024, ALLI/O Diagram An Action-based Visual Programming Language for Embedded System][research_narkthong_jariyavajee_2024]
- [Liu and others, 2024, An efficient schedulability analysis based on worst-case interference time for real-time systems][research_liu_yang_2024]
- [Santos and others, 2024, Assessing the Impact of Compiler Optimizations on GPUs Reliability][research_santos_carro_2024]
- [Sanusi and others, 2024, Assuring Correctness, Testing, and Verification of X-Compiler by Integrating Communicating Stream X-Machine][research_sanusi_ogunshile_2024]
- [Johnson and others, 2024, Automating Pruning in Top-Down Enumeration for Program Synthesis Problems with Monotonic Semantics][research_johnson_krishnan_2024]
- [Hück and others, 2024, Compiler-Aided Correctness Checking of CUDA-Aware MPI Applications][research_huck_ziegler_2024]
- [Jeong and others, 2024, Conflict-aware compiler for hierarchical register file on GPUs][research_jeong_park_2024]
- [Jiang and others, 2024, DCIM Compiler - Physical Design Generator][research_jiang_chow_2024]
- [Chen and others, 2024, Design and Implementation of an Aspect-Oriented C Programming Language][research_chen_zhu_2024]
- [Zhao and others, 2024, Design and Implementation of the MTP Compiler][research_zhao_he_2024]
- [Niu and others, 2024, FAIR Flow Type-Aware Pre-Training of Compiler Intermediate Representations][research_niu_li_2024]
- [Talamali and others, 2024, Formal Specification and Verification of MQTT Protocol Using CoQ Proof Assistant][research_talamali_lounas_2024]
- [Nougrahiya and Nandivada, 2024, Homeostasis Design and Implementation of a Self-Stabilizing Compiler][research_nougrahiya_nandivada_2024]
- [Lee and Lee, 2024, IMC-PnG Maximizing runtime performance and timing guarantee for imprecise mixed-criticality real-time scheduling][research_lee_lee_2024]
- [2024, Implementation concept of the IoT platform using C++ programming language][research_implementation_concept_2024]
- [Siambaton and others, 2024, Implementation Draft Programming Oriented Objects in Parking System Application using Language Programming Java][research_siambaton_azis_2024]
- [Zhang and others, 2024, Introducing Compiler Semantics into Large Language Models as Programming Language Translators A Case Study of C to x86 Assembly][research_zhang_zhao_2024]
- [Schlichtkrull and others, 2024, Isabelle-verified correctness of Datalog programs for program analysis][research_schlichtkrull_rydhofhansen_2024]
- [Chirila and Sora, 2024, Java Single vs. Platform vs. Virtual Threads Runtime Performance Assessment in the Context of Key Class Detection][research_chirila_sora_2024]
- [Wang and others, 2024, K-RAPID A Formal Executable Semantics of the RAPID Robot Programming Language][research_wang_wang_2024]
- [Gruetter and others, 2024, Live Verification in an Interactive Proof Assistant][research_gruetter_fukala_2024]
- [Shoushtary and others, 2024, Memento An Adaptive, Compiler-Assisted Register File Cache for GPUs][research_shoushtary_arnau_2024]
- [2024, Online platform learning the Java programming language development, implementation and efficiency][research_online_platform_2024]
- [Donaldson and others, 2024, Randomised Testing of the Compiler for a Verification-Aware Programming Language][research_donaldson_sheth_2024]
- [Hu and Tang, 2024, Research on compiler version recognition based on random forest algorithm][research_hu_tang_2024]
- [Aneesh and others, 2024, Smart Compiler Assistant An AST based Python Code Analysis][research_aneesh_saumik_2024]
- [Xu and others, 2024, SWAT4J Generating System Call Allowlist for Java Container Attack Surface Reduction][research_xu_zhou_2024]
- [Vraný and Shingarov, 2024, Tinyrossa A Compiler Framework for Vertical, Verified Construction of Smalltalk VMs][research_vrany_shingarov_2024]
- [Cunha and others, 2024, Trading Runtime for Energy Efficiency Leveraging Power Caps to Save Energy across Programming Languages][research_cunha_silva_2024]
- [Schoenberger and others, 2024, Using Compiler Frameworks for the Evaluation of Hardware Design Choices in Trapped-Ion Quantum Computers][research_schoenberger_hillmich_2024]
- [Wang, 2024, Worst-Case Blocking Time Optimization in WCRT Analysis for vMPCP on Multi-Core Virtual Machines][research_wang_2024]
- [Makki Mohialden and others, 2023, A Comparative Analysis of Python Code-Line Bug-Finding Methods][research_makkimohialden_mahmoodhussien_2023]
- [Wang and others, 2023, A General-Purpose Compiler Design for Instruction-Based AI Accelerator Implementation][research_wang_linghu_2023]
- [Roy, 2023, A Theorem Proving Approach to Programming Language Semantics][research_roy_2023]
- [Li and others, 2023, A unified proof technique for verifying program correctness with big-step semantics][research_li_zhang_2023]
- [2023, ADAPTIVE PROGRAMMING LANGUAGE LEARNING SYSTEM BASED ON GENERATIVE AI][research_adaptive_programming_2023]
- [Wang and others, 2023, An Automated Verification Framework for HalideIR-Based Compiler Transformations][research_wang_xie_2023]
- [Curry, 2023, An HPC-Oriented Runtime Environment for Enabling Computational Storage][research_curry_2023]
- [Drechsler and Schnieber, 2023, Automated Polynomial Formal Verification Human-Readable Proof Generation][research_drechsler_schnieber_2023]
- [Harshithan, 2023, Batwing Compiler An Artificial Intelligence based Compiler][research_harshithan_2023]
- [Audrito and Haures, 2023, Combining Static and Runtime Verification with AC and Coq][research_audrito_haures_2023]
- [Zhang and others, 2023, Compiler Technologies in Deep Learning Co-Design A Survey][research_zhang_xing_2023]
- [Baroffio and Reghenzani, 2023, Compiler-Injected SIHFT for Embedded Operating Systems][research_baroffio_reghenzani_2023]
- [2023, Development of a mobile robot control system in the Python programming language using Raspberry Pi][research_development_of_2023]
- [Yu and others, 2023, Efficient Generation of Floating-Point Inputs for Compiler-Induced Variability][research_yu_yi_2023]
- [Skarman and others, 2023, Enhancing Compiler-Driven HDL Design with Automatic Waveform Analysis][research_skarman_klemmer_2023]
- [Ceng Giap and Erviana, 2023, Implementation of Face Mask Detection Using Phyton Programming Language][research_cenggiap_erviana_2023]
- [Dange and others, 2023, Implementation on A User Authentication Scheme Using Block Chain-Enabled Fog Nodes][research_dange_mundre_2023]
- [Abi-Karam and others, 2023, INR-Arch A Dataflow Architecture and Compiler for Arbitrary-Order Gradient Computations in Implicit Neural Representation Processing][research_abikaram_sarkar_2023]
- [Sadasue and Isshiki, 2023, LLVM-C2RTL C/C++ Based System Level RTL Design Framework Using LLVM Compiler Infrastructure][research_sadasue_isshiki_2023]
- [Herklotz and others, 2023, Mechanised Semantics for Gated Static Single Assignment][research_herklotz_demange_2023]
- [Strauch, 2023, MRPHS A Verilog RTL to C++ Model Compiler Using Intermediate Representations for Object-oriented Model-driven Prototyping][research_strauch_2023]
- [Mehdi Pourhashem Kallehbasti and Ghafari, 2023, Naturalistic Static Program Analysis][research_mehdipourhashemkallehbasti_ghafari_2023]
- [Alpay and Heuveline, 2023, One Pass to Bind Them The First Single-Pass SYCL Compiler with Unified Code Representation Across Backends][research_alpay_heuveline_2023]
- [Vos and others, 2023, Oraqle A Depth-Aware Secure Computation Compiler][research_vos_conti_2023]
- [Hirata and others, 2023, Program logic for higher-order probabilistic programs in Isabelle/HOL][research_hirata_minamide_2023]
- [Cheng, 2023, QA4C An Intelligent Question and Answering System for the C Programming Language Based on Knowledge Graph][research_cheng_2023]
- [Yu, 2023, Reasoning about MLIR Semantics through Effects and Handlers][research_yu_2023]
- [Affeldt and others, 2023, Semantics of Probabilistic Programs using s-Finite Kernels in Coq][research_affeldt_cohen_2023]
- [Stolyarov, 2023, STATIC ANALYZER IMPLEMENTATION MODEL FOR THE SOLIDTY PROGRAMMING LANGUAGE][research_stolyarov_2023]
- [Denis and others, 2023, Tracing task-based runtime systems Feedbacks from the StarPU case][research_denis_jeannot_2023]
- [Tran and others, 2023, Transport Layer Security 1.0 handshake protocol formal verification case study How to use a proof script generator for existing large proof scores][research_tran_waimon_2023]
- [DelVado Vírseda, 2023, Visualizing Compiler Design Theory from Implementation Through an Interactive Tutoring Tool Experiences and Results][research_delvadovirseda_2023]
- [Vizcaino and others, 2022, Acceleration with long vector architectures Implementation and evaluation of the FFT kernel on NEC SX-Aurora and RISC-V vector extension][research_vizcaino_mantovani_2022]
- [2022, Analysis on Strengthening Scheme of Office Building Based on Function Change][research_analysis_on_2022]
- [Pant and others, 2022, Automatic Software Engineering Position Resume Screening using Natural Language Processing, Word Matching, Character Positioning, and Regex][research_pant_pokhrel_2022]
- [Kobusińska and Wilczynski, 2022, Blocked-based Solidity a Service for Graphically Creating the Smart Contracts in Solidity Programming Language][research_kobusinska_wilczynski_2022]
- [Schiewe, 2022, Bridging the gap between source code and high-level concepts in static code analysis][research_schiewe_2022]
- [2022, Cameleer A deductive verification tool for OCaml][research_cameleer_a_2022]
- [Zhang and others, 2022, Cape compiler-aided program transformation for HTM-based cache side-channel defense][research_zhang_bond_2022]
- [Ding and others, 2022, CARL Compiler Assigned Reference Leasing][research_ding_chen_2022]
- [Oh and others, 2022, CASH-RF A Compiler-Assisted Hierarchical Register File in GPUs][research_oh_jeong_2022]
- [Ambal and others, 2022, Certified Derivation of Small-Step From Big-Step Skeletal Semantics][research_ambal_lenglet_2022]
- [Ozdemir and others, 2022, CirC Compiler infrastructure for proof systems, software verification, and more][research_ozdemir_brown_2022]
- [Sharif and others, 2022, COMPAS Compiler-assisted Software-implemented Hardware Fault Tolerance for RISC-V][research_sharif_muellergritschneder_2022]
- [Bik and others, 2022, Compiler Support for Sparse Tensor Computations in MLIR][research_bik_koanantakool_2022]
- [Huck and others, 2022, Compiler-Aided Type Correctness of Hybrid MPI-OpenMP Applications][research_huck_kreutzer_2022]
- [Agathos and others, 2022, Compiler-assisted, adaptive runtime system for the support of OpenMP in embedded multicores][research_agathos_dimakopoulos_2022]
- [Lenkefi and Mezei, 2022, Connections between Language Semantics and the Query-based Compiler Architecture][research_lenkefi_mezei_2022]
- [Yadav and others, 2022, DISTAL the distributed tensor algebra compiler][research_yadav_aiken_2022]
- [Chaliasos and others, 2022, Finding typing compiler bugs][research_chaliasos_sotiropoulos_2022]
- [Shobaki and others, 2022, Graph transformations for register-pressure-aware instruction scheduling][research_shobaki_bassett_2022]
- [Alpay and Heuveline, 2022, How much SYCL does a compiler need? Experiences from the implementation of SYCL as a library for nvc++][research_alpay_heuveline_2022]
- [Poletanovic and others, 2022, Implementation of Machine Outliner for nanoMIPS in the LLVM Compiler Infrastructure][research_poletanovic_dukic_2022]
- [Mosaner and others, 2022, Improving Vectorization Heuristics in a Dynamic Compiler with Machine Learning Models][research_mosaner_barany_2022]
- [Hikmatyarsyah and Rahardjo, 2022, Integration of Downlink Scheme VLC Access Techniques for Low-cost Implementation Indoor Communication System A Survey][research_hikmatyarsyah_rahardjo_2022]
- [Fayzrakhmanov, 2022, Introducing Programming Language Metrics][research_fayzrakhmanov_2022]
- [Sammler and others, 2022, Islaris verification of machine code against authoritative ISA semantics][research_sammler_hammond_2022]
- [Gordon and others, 2022, Porting the Kitten Lightweight Kernel Operating System to RISC-V][research_gordon_pedretti_2022]
- [Valiron, 2022, Semantics of quantum programming languages Classical control, quantum control][research_valiron_2022]
- [Cho and others, 2022, Sequential reasoning for optimizing compilers under weak memory concurrency][research_cho_lee_2022]
- [Postema and others, 2022, Testing a PL/I Compiler Using Precomputation-based Program Generation][research_postema_fabry_2022]
- [C K, 2022, Video Calling With Build-In Compiler][research_ck_2022]
- [De Blaere and others, 2021, A Compiler Extension to Protect Embedded Systems Against Data Flow Errors][research_deblaere_verstappe_2021]
- [Myreen, 2021, A minimalistic verified bootstrapped compiler proof pearl][research_myreen_2021]
- [Jeon and others, 2021, A practical algorithm for learning disjunctive abstraction heuristics in static program analysis][research_jeon_jeon_2021]
- [Yvon and Feeley, 2021, A small scheme VM, compiler, and REPL in 4k][research_yvon_feeley_2021]
- [Benito-Montoro and others, 2021, A Tool to Assist the Compiler Construction Instructor in Checking the Equivalence of Specifications Based on Regular Expressions][research_benitomontoro_chen_2021]
- [Amaliah and others, 2021, Auto Clustering Source Code To Detect Plagiarism Of Student Programming Assignments in Java Programming Language][research_amaliah_musu_2021]
- [Padmasudha Kannan and others, 2021, Automated high-order curved mesh generator with high-level dynamic programming language julia for photonic applications][research_padmasudhakannan_smitha_2021]
- [Windsor and others, 2021, C4 the C compiler concurrency checker][research_windsor_donaldson_2021]
- [Cruttwell and others, 2021, Categorical semantics of a simple differential programming language][research_cruttwell_gallagher_2021]
- [Hossain and others, 2021, Code Generator based on Voice Command for Multiple Programming Language][research_hossain_emi_2021]
- [Ploensin and others, 2021, Code Transformation Impact on Compiler-based Optimization A Case Study in the CMSSW][research_ploensin_piromsopa_2021]
- [Jung, 2021, CommitBERT Commit Message Generation Using Pre-Trained Programming Language Model][research_jung_2021]
- [Steingartner, 2021, Compiler Module of Abstract Machine Code for Formal Semantics Course][research_steingartner_2021]
- [Bruno and others, 2021, Compiler-assisted object inlining with value fields][research_bruno_jovanovic_2021]
- [Han and others, 2021, Design and Implementation of a Criticality- and Heterogeneity-Aware Runtime System for Task-Parallel Applications][research_han_park_2021]
- [Liu and others, 2021, Design and Implementation of Multi-core Parallel Compiler Based on OpenMP][research_liu_lv_2021]
- [Mpeis and others, 2021, Developer and user-transparent compiler optimization for interactive applications][research_mpeis_petoumenos_2021]
- [Wang, 2021, Helper function inlining in dynamic binary translation][research_wang_2021_2]
- [Pizzolotto and Inoue, 2021, Identifying Compiler and Optimization Level in Binary Code From Multiple Architectures][research_pizzolotto_inoue_2021]
- [Bekiris, 2021, Implementation of UTASTAR Decision Support System in VΒΑ Programming Language][research_bekiris_2021]
- [del Vado Vírseda, 2021, Learning Compiler Design From the Implementation to Theory][research_delvadovirseda_2021]
- [Lööw, 2021, Lutsig a verified Verilog compiler for verified circuit development][research_loow_2021]
- [Antoniadis and others, 2021, Open-Source Memory Compiler for Automatic RRAM Generation and Verification][research_antoniadis_feng_2021]
- [Nowicki and others, 2021, Performance evaluation of Java/PCJ implementation of parallel algorithms on the cloud extended version][research_nowicki_gorski_2021]
- [Chernenko and others, 2021, Proving Reflex Program Verification Conditions in Coq Proof Assistant][research_chernenko_anureev_2021]
- [Guria and others, 2021, RbSyn type- and effect-guided program synthesis][research_guria_foster_2021]
- [Worthington, 2021, Reflections on a decade of MoarVM, a runtime for the Raku programming language keynote][research_worthington_2021]
- [Zhao and others, 2021, Similarity-Aware Architecture/Compiler Co-Designed Context-Reduction Framework for Modulo-Scheduled CGRA][research_zhao_sheng_2021]
- [2021, Socket system in php programming language][research_socket_system_2021]
- [Rao and others, 2021, SODA A Semantics-Aware Optimization Framework for Data-Intensive Applications Using Hybrid Program Analysis][research_rao_liu_2021]
- [Bourke, 2021, Specification and end-to-end proof of a reactive language and its compiler invited talk][research_bourke_2021]
- [Yilmazer‐Metin, 2021, sRSP An efficient and scalable implementation of remote scope promotion][research_yilmazermetin_2021]
- [Aldweesh and others, 2021, The OpBench Ethereum opcode benchmark framework Design, implementation, validation and experiments][research_aldweesh_alharby_2021]
- [Tempel and others, 2021, Towards Reliable Spatial Memory Safety for Embedded Software by Combining Checked C with Concolic Testing][research_tempel_herdt_2021]
- [Xiao, 2021, Transformation System of two Similar Syntax Programs Based on the Compiler Principle][research_xiao_2021]
- [JEONG and others, 2021, Usage Log-Based Testing of Embedded Software and Identification of Dependencies among Environmental Components][research_jeong_cha_2021]
- [Geng and others, 2021, Verification of Open-Source Memory Compiler Framework with a Practical PDK][research_geng_ishikawa_2021]
- [Sorensen and others, 2020, A simulator and compiler framework for agile hardware-software co-design evaluation and exploration][research_sorensen_manocha_2020]
- [Pai T and others, 2020, A Systematic Literature Review of Lexical Analyzer Implementation Techniques in Compiler Design][research_pait_jayanthiladevi_2020]
- [Diamantopoulos and others, 2020, Agile Autotuning of a Transprecision Tensor Accelerator Overlay for TVM Compiler Stack][research_diamantopoulos_ringlein_2020]
- [Barinov and others, 2020, Applying compiler-based binary watermarking technology to ensure binary compatibility in GNU/Linux distribution][research_barinov_kashkarov_2020]
- [Suchy and others, 2020, CARAT a case for virtual memory through compiler- and runtime-based address translation][research_suchy_campanoni_2020]
- [Amarasinghe, 2020, Compiler 2.0][research_amarasinghe_2020]
- [Flatt and Dybvig, 2020, Compiler and runtime support for continuation marks][research_flatt_dybvig_2020]
- [Squar and others, 2020, Compiler Assisted Source Transformation of OpenMP Kernels][research_squar_jammer_2020]
- [Ghosh and others, 2020, Compiler compatible 5.66 Mb/mm2 8T 1R1W register file in 14 nm FinFET technology][research_ghosh_bhattacharya_2020]
- [Kim and others, 2020, Compiler-directed soft error resilience for lightweight GPU register file protection][research_kim_zeng_2020]
- [Chen and others, 2020, CRAC An automatic assistant compiler of checkpoint/restart for OpenCL program][research_chen_zhang_2020]
- [Zhang and Meng, 2020, Design and Implementation of Multi-core DSP Parallel Compiler Based on Otsu Method][research_zhang_meng_2020]
- [Watanabe and others, 2020, Design and Preliminary Evaluation of OpenACC Compiler for FPGA with OpenCL and Stream Processing DSL][research_watanabe_lee_2020]
- [Groenewegen and others, 2020, Evolution of the WebDSL runtime reliability engineering of the WebDSL web programming language][research_groenewegen_chastelet_2020]
- [Queiroz Junior and others, 2020, Finding Effective Compiler Optimization Sequences A Hybrid Approach][research_queirozjunior_dasilva_2020]
- [Luo, 2020, Heap Memory Snapshot Assisted Program Analysis for Android Permission Specification][research_luo_2020]
- [Ranganathan and others, 2020, Hybrid Scalable Action Rule][research_ranganathan_sharma_2020]
- [Bezrąk and Przyłucki, 2020, Impact of the cloud application programming language on the performance of its implementation in selected serverless environments][research_bezrak_przylucki_2020]
- [Georgiou and others, 2020, Lost In Translation Exposing Hidden Compiler Optimization Opportunities][research_georgiou_chamski_2020]
- [Zaytsev, 2020, Modelling of Language Syntax and Semantics The Case of the Assembler Compiler][research_zaytsev_2020]
- [Andrade Guzmán and Hernández Quiroz, 2020, Natural deduction and semantic models of justification logic in the proof assistant Coq][research_andradeguzman_hernandezquiroz_2020]
- [Amato and others, 2020, On collecting semantics for program analysis][research_amato_meo_2020]
- [Phulia and others, 2020, OOElala order-of-evaluation based alias analysis for compiler optimization][research_phulia_bhagee_2020]
- [Vasilyev and Mutilin, 2020, Predicate Extension of Symbolic Memory Graphs for the Analysis of Memory Safety Correctness][research_vasilyev_mutilin_2020]
- [2020, Proceedings of the 2020 International Conference on Embedded Software EMSOFT][research_proceedings_of_2020]
- [Sanders and others, 2020, Robustness Analysis of Scaled Resource Allocation Models Using the Imperial PEPA Compiler][research_sanders_srivastava_2020]
- [Sulema and Glinskii, 2020, Semantics and pragmatics of programming language ASAMPL][research_sulema_glinskii_2020]
- [Cambier and others, 2020, TaskTorrent a Lightweight Distributed Task-Based Runtime System in C++][research_cambier_qian_2020]
- [Natarajan and Broman, 2020, Temporal Property-Based Testing of a Timed C Compiler using Time-Flow Graph Semantics][research_natarajan_broman_2020]
- [Yin and others, 2020, The Implementation of Simple Smart Contract Language and Its Compiler Based on Ethereum Platform][research_yin_pan_2020]
- [Huck and others, 2020, Towards compiler-aided correctness checking of adjoint MPI applications][research_huck_protze_2020]
- [Holmes and Groce, 2020, Using mutants to help developers distinguish and debug compiler faults][research_holmes_groce_2020]
- [Dasgupta and others, 2019, A complete formal semantics of x86-64 user-level instruction set architecture][research_dasgupta_park_2019]
- [Benzaken and Contejean, 2019, A Coq mechanised formal semantics for realistic SQL queries formally reconciling SQL and bag relational algebra][research_benzaken_contejean_2019]
- [Lima and others, 2019, A memory-bounded, deterministic and terminating semantics for the synchronous programming language Céu][research_lima_santos_2019]
- [Feitosa and others, 2019, A monadic semantics for quantum computing in an object oriented language][research_feitosa_vizzotto_2019]
- [ROMPF and AMIN, 2019, A SQL to C compiler in 500 lines of code][research_rompf_amin_2019]
- [Ye and Delaware, 2019, A verified protocol buffer compiler][research_ye_delaware_2019]
- [2019, Automatic Port to OpenACC/OpenMP for Physical Parameterization in Climate and Weather Code Using the CLAW Compiler][research_automatic_port_2019]
- [Bassil, 2019, Compiler Design for Legal Document TranslationIn Digital Government][research_bassil_2019]
- [Elkhouly and others, 2019, Compiler-support for Critical Data Persistence in NVM][research_elkhouly_alshboul_2019]
- [Kondratyev and Promsky, 2019, Correctness of Proof Strategy for the Sisal Program Verification][research_kondratyev_promsky_2019]
- [Zwanziger, 2019, Dependently-Typed Montague Semantics in the Proof Assistant Agda-flat][research_zwanziger_2019]
- [Salánki and Sarvajcz, 2019, Development of a Gait Recognition System in NI LabVIEW Programming Language][research_salanki_sarvajcz_2019]
- [Melnyk and Kozak, 2019, Easy Universal Translator as an Alternative Compiler-Compiler][research_melnyk_kozak_2019]
- [Thiselton and Treude, 2019, Enhancing Python Compiler Error Messages via Stack][research_thiselton_treude_2019]
- [Mao and others, 2019, Exploiting Java Stack Forensics for Runtime Monitoring of IoT Services][research_mao_zhang_2019]
- [Acun and others, 2019, Fine-Grained Energy Efficiency Using Per-Core DVFS with an Adaptive Runtime System][research_acun_chandrasekar_2019]
- [Facchinetti and others, 2019, Higher-order Demand-driven Program Analysis][research_facchinetti_palmer_2019]
- [Duhoux and others, 2019, Implementation of a Feature-Based Context-Oriented Programming Language][research_duhoux_mens_2019]
- [Somani and Srivastava, 2019, Implementation of SAAS Intranet compiler in PHP][research_somani_srivastava_2019]
- [Yim and others, 2019, Implementation of Targeted Advertisement Services on ATSC 3.0 Runtime Environment][research_yim_kim_2019]
- [Oshita and others, 2019, Improving User Experience of C Programming Language Learning System for Novices][research_oshita_kaida_2019]
- [Besson and others, 2019, Information-Flow Preservation in Compiler Optimisations][research_besson_dang_2019]
- [Nguyen and others, 2019, Integrating Static Program Analysis Tools for Verifying Cautions of Microcontroller][research_nguyen_aoki_2019]
- [Zhu and others, 2019, Learning to Restrict Test Range for Compiler Test][research_zhu_wang_2019]
- [Gorodetskiy, 2019, NEXTGEN PROGRAMMING LANGUAGE WITH PROGRAMMABLE SEMANTICS][research_gorodetskiy_2019]
- [Campbell, 2019, Random Compiler for Fast Hamiltonian Simulation][research_campbell_2019]
- [Wang and others, 2019, Reg An Ultra-Lightweight Container That Maximizes Memory Sharing and Minimizes the Runtime Environment][research_wang_zhang_2019]
- [Guerrera and others, 2019, Reproducible stencil compiler benchmarks using prova!][research_guerrera_maffia_2019]
- [Heo and others, 2019, Resource-Aware Program Analysis Via Online Abstraction Coarsening][research_heo_oh_2019]
- [Choi and others, 2019, Reusable inline caching for JavaScript performance][research_choi_shull_2019]
- [Ghorbani and Babamir, 2019, Runtime deadlock tracking and prevention of concurrent multithreaded programs A learning-based approach][research_ghorbani_babamir_2019]
- [Roy and others, 2019, Security Analysis and Efficient Implementation of Code-based Signature Schemes][research_roy_morozov_2019]
- [Ivanov and others, 2019, Software Structure, Program Generation and Schedulability Analysis of Extracorporeal Perfusion Pump Embedded Controller][research_ivanov_gueorguiev_2019]
- [Kim and Ryou, 2019, Source Code Analysis for Static Prediction of Dynamic Memory Usage][research_kim_ryou_2019]
- [Arceri and Mastroeni, 2019, Static Program Analysis for String Manipulation Languages][research_arceri_mastroeni_2019]
- [Delgado-Pérez and Segura, 2019, Study of trivial compiler equivalence on C++ object-oriented mutation operators][research_delgadoperez_segura_2019]
- [Amarasinghe, 2019, The sparse tensor algebra compiler keynote][research_amarasinghe_2019]
- [Ryu and others, 2019, Toward Analysis and Bug Finding in JavaScript Web Applications in the Wild][research_ryu_park_2019]
- [Wang and others, 2019, Tracking runtime concurrent dependences in java threads using thread control profiling][research_wang_li_2019]
- [Tillet and others, 2019, Triton an intermediate language and compiler for tiled neural network computations][research_tillet_kung_2019]
- [Guan and others, 2019, Wootz a compiler-based framework for fast CNN pruning via composability][research_guan_shen_2019]
- [2018, 2018 Proceedings of the International Conference on Embedded Software EMSOFT][research_2018_proceedings_2018]
- [Leopoldseder and others, 2018, A cost model for a graph-based intermediate-representation in a dynamic compiler][research_leopoldseder_stadler_2018_2]
- [Fradet and others, 2018, A Generic Coq Proof of Typical Worst-Case Analysis][research_fradet_lesourd_2018]
- [Waites and others, 2018, A Genetic Circuit Compiler Generating Combinatorial Genetic Circuits with Web Semantics and Inference][research_waites_misirli_2018]
- [Santos and others, 2018, A memory-bounded, deterministic and terminating semantics for the synchronous programming language Céu][research_santos_lima_2018]
- [Asadollah and others, 2018, A Runtime Verification Tool for Detecting Concurrency Bugs in FreeRTOS Embedded Software][research_asadollah_sundmark_2018]
- [Bishnu and Bhatia, 2018, Algorithmic Compiler based FPGA Implementation of Iterative Time-Domain Algorithm for Sparse Channel Estimation][research_bishnu_bhatia_2018]
- [Yi and Lee, 2018, An Educational System Design to Support Learning Transfer from Block-based Programming Language to Text-based Programming Language][research_yi_lee_2018]
- [Sah and others, 2018, An Efficient Hardware-Oriented Runtime Approach for Stack-based Software Buffer Overflow Attacks][research_sah_islam_2018]
- [Tohid and others, 2018, Asynchronous Execution of Python Code on Task-Based Runtime Systems][research_tohid_wagle_2018]
- [Ginsbach and others, 2018, CAnDL a domain specific language for compiler analysis][research_ginsbach_crawford_2018]
- [Belyaev and others, 2018, Comparative Analysis of Two Approaches to Static Taint Analysis][research_belyaev_shimchik_2018]
- [Besson and others, 2018, CompCertS A Memory-Aware Verified C Compiler Using a Pointer as Integer Semantics][research_besson_blazy_2018]
- [Heim, 2018, Compiler and language design for quantum computing keynote][research_heim_2018]
- [Zhang, 2018, Compiler Practice System Integrated with Real Open Source Compiler][research_zhang_2018]
- [Huck and others, 2018, Compiler-aided Type Tracking for Correctness Checking of MPI Applications][research_huck_lehr_2018]
- [Sharrad and others, 2018, Delta Debugging Type Errors with a Blackbox Compiler][research_sharrad_chitil_2018]
- [Medeiros and others, 2018, Evaluation of Compiler Optimization Flags Effects on Soft Error Resiliency][research_medeiros_bortolon_2018]
- [Beaumont and others, 2018, Fast approximation algorithms for task-based runtime systems][research_beaumont_eyrauddubois_2018]
- [Kusmenko and others, 2018, Highly-Optimizing and Multi-Target Compiler for Embedded System Models][research_kusmenko_rumpe_2018]
- [Terao, 2018, Lazy Abstraction for Higher-Order Program Verification][research_terao_2018]
- [Niephaus and others, 2018, Live Multi-language Development and Runtime Environments][research_niephaus_felgentreff_2018]
- [Lyamin, 2018, Method of Formal Program Verification for Post Machine Virtual Laboratory][research_lyamin_2018]
- [Oehlert and others, 2018, Mitigating Data Cache Aging through Compiler-Driven Memory Allocation][research_oehlert_luppold_2018]
- [Salama and others, 2018, Online programming language-Learning management system][research_salama_qazi_2018]
- [Liu and others, 2018, Research of Register Pressure Aware Loop Unrolling Optimizations for Compiler][research_liu_ding_2018]
- [Deng and Namjoshi, 2018, Securing a compiler transformation][research_deng_namjoshi_2018]
- [Ismael and others, 2018, System on Chip Implementation of Compiler Stack with a Delimiter Matching Application][research_ismael_zyad_2018]
- [Bourke and others, 2018, Towards a verified Lustre compiler with modular reset][research_bourke_brun_2018]
- [Bowman and Ahmed, 2018, Typed closure conversion for the calculus of constructions][research_bowman_ahmed_2018]
- [Fumero and Kotselidis, 2018, Using compiler snippets to exploit parallelism on heterogeneous hardware a Java reduction case study][research_fumero_kotselidis_2018]
- [Tatsuoka and Kaneko, 2018, Wire congestion aware high level synthesis flow with source code compiler][research_tatsuoka_kaneko_2018]
- [Takase and others, 2018, Work-in-Progress Design Concept of a Lightweight Runtime Environment for Robot Software Components Onto Embedded Devices][research_takase_mori_2018]
- [Choi and others, 2018, Work-in-Progress Lightweight Deadlock Detection Technique for Embedded Systems via OS-Level Analysis][research_choi_kwon_2018]
- [Janetschek and Prodan, 2017, A compiler transformation-based approach to scientific workflow enactment][research_janetschek_prodan_2017]
- [Imamoglu and Cetinkaya, 2017, A rule based decision support system for programming language selection][research_imamoglu_cetinkaya_2017]
- [Cambou, 2017, A XOR data compiler Combined with physical unclonable function for true random number generation][research_cambou_2017]
- [Shen, 2017, Android Security via Static Program Analysis][research_shen_2017]
- [2017, C# Compiler for Blind][research_c_compiler_2017]
- [Akdur and others, 2017, Characterizing the Development and Usage of Diagrams in Embedded Software Systems][research_akdur_demirors_2017]
- [Lambert and Saunders, 2017, Compiler auto-vectorization of matrix multiplication modulo small primes][research_lambert_saunders_2017]
- [Proy and others, 2017, Compiler-Assisted Loop Hardening Against Fault Attacks][research_proy_heydemann_2017]
- [Yaneva and others, 2017, Compiler-assisted test acceleration on GPUs for embedded software][research_yaneva_rajan_2017]
- [Luo and others, 2017, Compiler-Assisted Threshold Implementation against Power Analysis Attacks][research_luo_athanasiou_2017]
- [Maurer and others, 2017, Compiling without continuations][research_maurer_downen_2017]
- [Akdur and others, 2017, Cross-factor analysis of software modeling practices versus practitioner demographics in the embedded software industry][research_akdur_garousi_2017]
- [Kirichenko and Tarasov, 2017, Development of design flow for multiported register files, which includes a cell library and a compiler for SOI 0.25-μm process][research_kirichenko_tarasov_2017]
- [Prenzel and Provost, 2017, Dynamic Software Updating of IEC 61499 Implementation Using Erlang Runtime System][research_prenzel_provost_2017]
- [Ruberg and others, 2017, Embedded software performance estimations at different compiler optimisation levels][research_ruberg_lass_2017]
- [SulĂ­r and Poruban, 2017, Exposing Runtime Information through Source Code Annotations][research_sular_poruban_2017]
- [Ruchkin and others, 2017, Frame model of a compiler of cluster parallelism for embedded computing systems][research_ruchkin_romanchuk_2017]
- [Pieters and others, 2017, Handlers for Non-Monadic Computations][research_pieters_schrijvers_2017]
- [Tian and others, 2017, LLVM Compiler Implementation for Explicit Parallelization and SIMD Vectorization][research_tian_saito_2017]
- [Endo and others, 2017, On the Interactions Between Value Prediction and Compiler Optimizations in the Context of EOLE][research_endo_perais_2017]
- [Ghica and Alyahya, 2017, On the Learnability of Programming Language Semantics][research_ghica_alyahya_2017]
- [Meghzili and others, 2017, On the Verification of UML State Machine Diagrams to Colored Petri Nets Transformation Using Isabelle/HOL][research_meghzili_chaoui_2017]
- [Wimmer and others, 2017, One compiler deoptimization to optimized code][research_wimmer_jovanovic_2017]
- [Maccabe, 2017, Operating and Runtime Systems Challenges for HPC Systems][research_maccabe_2017]
- [Würthinger and others, 2017, Practical partial evaluation for high-performance dynamic language runtimes][research_wurthinger_wimmer_2017]
- [Chong and others, 2017, Programming languages and compiler design for realistic quantum hardware][research_chong_franklin_2017]
- [Li and others, 2017, Promotion of Educational Effectiveness by Translation-based Programming Language Learning Using Java and Swift][research_li_sakamoto_2017]
- [Baek and Kim, 2017, Prototype implementation of the OpenGL ES 2.0 shading language offline compiler][research_baek_kim_2017]
- [Khatami and others, 2017, Redesigning OP2 Compiler to Use HPX Runtime Asynchronous Techniques][research_khatami_kaiser_2017]
- [Lins and others, 2017, Register File Criticality and Compiler Optimization Effects on Embedded Microprocessors Reliability][research_lins_tambara_2017]
- [Kiefer and others, 2017, Relational Program Reasoning Using Compiler IR][research_kiefer_klebanov_2017]
- [Wang, 2017, Research on the Execution Time Analysis Technology of the Worst Case System in Real Time System][research_wang_2017]
- [Santhiar and Kanade, 2017, Static deadlock detection for asynchronous C# programs][research_santhiar_kanade_2017]
- [Wu and others, 2017, Two Schemes to Improve the Implementation of the Aggregation Based Algebraic Multigrid Preconditioner][research_wu_yin_2017]
- [Zubarev, 2017, TYPE ANALYSIS FOR THE PREDICATE PROGRAMMING LANGUAGE][research_zubarev_2017]
- [Márton and Porkoláb, 2017, Unit Testing in C++ with Compiler Instrumentation and Friends][research_marton_porkolab_2017]
- [Engelke and Weidendorfer, 2017, Using LLVM for Optimized Lightweight Binary Re-Writing at Runtime][research_engelke_weidendorfer_2017]
- [De Luca and Chen, 2017, Visual IoT/Robotics Programming Language in Pi-Calculus][research_deluca_chen_2017]
- [Dave and others, 2016, A 1V 800MHz 140Kb register file compiler using variation aware self-timing in 40nm bulk CMOS][research_dave_dikshit_2016]
- [Zhou and Xue, 2016, A Compiler Approach for Exploiting Partial SIMD Parallelism][research_zhou_xue_2016]
- [Bispo and Cardoso, 2016, A MATLAB subset to C compiler targeting embedded systems][research_bispo_cardoso_2016]
- [Chen and others, 2016, A Process-Visible Compiler Aimed for Teaching Assistant][research_chen_lin_2016]
- [Wenger and others, 2016, A Programming Language and System for Heterogeneous Cloud of Things][research_wenger_zhu_2016]
- [Kalyur and Nagaraja, 2016, A survey of modeling techniques used in compiler design and implementation][research_kalyur_nagaraja_2016]
- [Hmid and others, 2016, A Transfer-Aware Runtime System for Heterogeneous Asynchronous Parallel Execution][research_hmid_coutinho_2016]
- [Horký and others, 2016, Analysis of Overhead in Dynamic Java Performance Monitoring][research_horky_kotrc_2016]
- [Ivey and Riley, 2016, Analysis of Programming Language Overhead in DCE][research_ivey_riley_2016]
- [Chen and Zong, 2016, Android App Energy Efficiency The Impact of Language, Runtime, Compiler, and Implementation][research_chen_zong_2016]
- [Klöckner and others, 2016, Array program transformation with Loo.py by example high-order finite elements][research_klockner_wilcox_2016]
- [Jacek and others, 2016, Assessing the limits of program-specific garbage collection performance][research_jacek_chiu_2016]
- [Schäfer and others, 2016, Axiomatic semantics for compiler verification][research_schafer_schneider_2016]
- [Xu and others, 2016, CAOPLE A Programming Language for Microservices SaaS][research_xu_zhu_2016]
- [Huang and Huang, 2016, Cell-based delay locked loop compiler][research_huang_huang_2016]
- [Mäkelä and others, 2016, Compiler assisted dynamic allocation of finite hardware acceleration resources for parallel tasks][research_makela_forsell_2016]
- [Zhang and others, 2016, Compiler Transformation to Generate Hybrid Sparse Computations][research_zhang_venkat_2016]
- [Tolpin and others, 2016, Design and Implementation of Probabilistic Programming Language Anglican][research_tolpin_vandemeent_2016]
- [Patel and Lee, 2016, Dynamic Analysis of Multi-threaded Embedded Software to Expose Atomicity Violations][research_patel_lee_2016]
- [Hariri and others, 2016, Evaluating the Effects of Compiler Optimizations on Mutation Testing at the Compiler IR Level][research_hariri_shi_2016]
- [Sun and others, 2016, Finding compiler bugs via live code mutation][research_sun_le_2016]
- [Gotti and Mbarki, 2016, Java Swing Modernization Approach - Complete Abstract Representation based on Static and Dynamic Analysis][research_gotti_mbarki_2016]
- [Na and others, 2016, JavaScript Parallelizing Compiler for Exploiting Parallelism from Data-Parallel HTML5 Applications][research_na_kim_2016]
- [Truong and others, 2016, Latte a language, compiler, and runtime for elegant and efficient deep neural networks][research_truong_barik_2016]
- [Yamamoto and others, 2016, Lightweight Ruby Framework for Improving Embedded Software Efficiency][research_yamamoto_oyama_2016]
- [Guo and Si, 2016, Mechanical hydraulic characteristic analysis scheme based on lightweight crowd data in mobile embedded devices][research_guo_si_2016]
- [Tian and others, 2016, Optimizing GPU Register Usage Extensions to OpenACC and Compiler Optimizations][research_tian_khaldi_2016]
- [Raj, 2016, Performance analysis of different specifications of copy propagation transformation using machine SUIF compiler infrastructure][research_raj_2016]
- [Rodríguez and others, 2016, Proving Correctness of a Compiler Using Step-indexed Logical Relations][research_rodriguez_pagano_2016]
- [Gómez-Déniz and others, 2016, Random Tests Combining Mathematica Package and Latex Compiler][research_gomezdeniz_davilacardenes_2016]
- [Gaudet and Stoodley, 2016, Rebuilding an airliner in flight a retrospective on refactoring IBM testarossa production compiler for Eclipse OMR][research_gaudet_stoodley_2016]
- [Lin and others, 2016, Rust as a language for high performance GC implementation][research_lin_blackburn_2016]
- [Xue and Bogdan, 2016, Scalable and realistic benchmark synthesis for efficient NoC performance evaluation][research_xue_bogdan_2016]
- [Zhang, 2016, Selection and Improvement of Computer Programming Language][research_zhang_2016]
- [Cho, 2016, Semantics for a Quantum Programming Language by Operator Algebras][research_cho_2016]
- [Downen and others, 2016, Sequent calculus as a compiler intermediate language][research_downen_maurer_2016]
- [Ruchkin and others, 2016, Smart compiler embedded computing systems based on cluster parallelism][research_ruchkin_mahmudov_2016]
- [Kroening and others, 2016, Sound static deadlock analysis for C/Pthreads][research_kroening_poetzl_2016]
- [Amin and others, 2016, System Verilog Assertions Synthesis Based Compiler][research_amin_ramzy_2016]
- [Campos-López and Wannenwetsch, 2016, The PERICLES Process Compiler Linking BPMN Processes into Complex Workflows for Model-Driven Preservation in Evolving Ecosystems][research_camposlopez_wannenwetsch_2016]
- [Sun and others, 2016, Toward understanding compiler bugs in GCC and LLVM][research_sun_le_2016_2]
- [Khaldi and Chapman, 2016, Towards Automatic HBM Allocation Using LLVM A Case Study with Knights Landing][research_khaldi_chapman_2016]
- [MORIGUCHI and others, 2016, Verification of Content-Centric Networking Using Proof Assistant][research_moriguchi_morishima_2016]
- [Buchwald and others, 2016, Verified construction of static single assignment form][research_buchwald_lohner_2016]
- [Zhou and others, 2016, Worst case response time and schedulability analysis for real-time software transactional memory-lazy conflict detection STM-LCD][research_zhou_li_2016]
- [Mhaske and others, 2015, A 2.48Gb/s FPGA-based QC-LDPC decoder An algorithmic compiler implementation][research_mhaske_uliana_2015]
- [Kyrtatas and others, 2015, A Basic Linear Algebra Compiler for Embedded Processors][research_kyrtatas_spampinato_2015]
- [Murthy and Mellor-Crummey, 2015, A Compiler Transformation to Overlap Communication with Dependent Computation][research_murthy_mellorcrummey_2015]
- [Michels and others, 2015, A new probabilistic constraint logic programming language based on a generalised distribution semantics][research_michels_hommersom_2015]
- [Yamato, 2015, Automatic verification for plural virtual machines patches][research_yamato_2015]
- [Verma and Bakshi, 2015, Chronological Advancement in Compiler Design A Review][research_verma_bakshi_2015]
- [Royuela and others, 2015, Compiler analysis for OpenMP tasks correctness][research_royuela_ferrer_2015]
- [Li and others, 2015, Compiler directed automatic stack trimming for efficient non-volatile processors][research_li_zhao_2015]
- [Haj-Yihia and others, 2015, Compiler-Directed Power Management for Superscalars][research_hajyihia_asher_2015]
- [Basu and others, 2015, Compiler-Directed Transformation for Higher-Order Stencils][research_basu_hall_2015]
- [Mosterman and Zander, 2015, Cyber-physical systems challenges a needs analysis for collaborating embedded software systems][research_mosterman_zander_2015]
- [Abramsky and Horsman, 2015, DEMONIC programming a computational language for single-particle equilibrium thermodynamics, and its formal semantics][research_abramsky_horsman_2015]
- [Gordon and Scholz, 2015, Dynamic adaptation of functional runtime systems through external control][research_gordon_scholz_2015]
- [2015, Efficient Implementation of Class Based Decomposition Schemes for Naive Bayes Classifier][research_efficient_implementation_2015]
- [Kim, 2015, Exploiting Window Query Semantics in Scalable Data Stream Processing][research_kim_2015]
- [Stanisic and others, 2015, Faithful performance prediction of a dynamic task-based runtime system for heterogeneous multi-core architectures][research_stanisic_thibault_2015]
- [Le and others, 2015, Finding deep compiler bugs via guided stochastic program mutation][research_le_sun_2015]
- [Queiroz Junior and da Silva, 2015, Finding Good Compiler Optimization Sets - A Case-based Reasoning Approach][research_queirozjunior_dasilva_2015]
- [Breitner, 2015, Formally proving a compiler transformation safe][research_breitner_2015]
- [Cazzola and Olivares, 2015, Gradually Learning Programming Supported by a Growable Programming Language][research_cazzola_olivares_2015]
- [Jiang and others, 2015, Implementation and Comparison of the Way That Office Document Is Converted to PDF Documents in the Java Runtime Environment][research_jiang_zheng_2015]
- [2015, Implementation of a Motor Imagery based BCI System using Python Programming Language][research_implementation_of_2015]
- [Mehta and Yew, 2015, Improving compiler scalability optimizing large programs at small price][research_mehta_yew_2015]
- [Leopoldseder and others, 2015, Java-to-JavaScript translation via structured control flow reconstruction of compiler IR][research_leopoldseder_stadler_2015]
- [Park and others, 2015, KJS a complete formal semantics of JavaScript][research_park_stefanescu_2015]
- [Ko and others, 2015, LaminarIR compile-time queues for structured streams][research_ko_burgstaller_2015]
- [Iskra and Hoefler, 2015, Operating systems and runtime environments on supercomputers][research_iskra_hoefler_2015]
- [Ghica and Tapus, 2015, Optimized retargetable compiler for embedded processors - GCC vs LLVM][research_ghica_tapus_2015]
- [Yang and Ruiz Varela, 2015, Qualifying non-volatile register files for embedded systems through compiler-directed write minimization and balancing][research_yang_ruizvarela_2015]
- [Mosses, 2015, Semantics of programming languages Using Asf+Sdf][research_mosses_2015]
- [Naish, 2015, Sharing analysis in the Pawns compiler][research_naish_2015]
- [Srinivasan and Reps, 2015, Synthesis of machine code from semantics][research_srinivasan_reps_2015]
- [D'Silva and others, 2015, The Correctness-Security Gap in Compiler Optimization][research_dsilva_payer_2015]
- [Ricketts and others, 2015, Towards verification of hybrid systems in a foundational proof assistant][research_ricketts_malecha_2015]
- [Papadakis and others, 2015, Trivial Compiler Equivalence A Large Scale Empirical Study of a Simple, Fast and Effective Equivalent Mutant Detection Technique][research_papadakis_jia_2015]
- [Lezuo and others, 2015, vanHelsing A Fast Proof Checker for Debuggable Compiler Verification][research_lezuo_dragan_2015]
- [Blazy and others, 2015, Verified Validation of Program Slicing][research_blazy_maroneze_2015]

### What the survey shows

**The representation question is settled in the literature and the selection question is not.** Four
independent traditions converge on a discriminated return for terminating coroutines, and none of them
addresses whether a bounded-memory artefact should pay that discrimination on every call of a construct that
never terminates. The present article contributes the observation that the two source forms have different
trace alphabets and that the choice can therefore be made per form rather than globally, which the surveyed
work does not consider because no surveyed language separates the two forms in its type system.

**That separation is Keleusma's own contribution to the problem**, and it is the reason the question is even
askable here. It is also why the survey cannot answer it.

The scale of the survey should be read for what it is. It lists 1,980 references, of which
35 were selected because the argument depends on them and the rest were harvested by query
across thirteen clusters. **The harvested majority establishes coverage and not agreement.** A reader
looking for the works that carry the argument should read the 35, which are named in the prose
above. A reader checking whether the survey was assembled to flatter its conclusion should note that the
queries were fixed before any record was seen, that every admitted record is listed including the
680 that are merely adjacent, and that the selection procedure is reported in Method with the
count it discarded.

## The Source Base

The generator is a detached package inside the Keleusma repository, consuming the reference compiler's
in-memory module representation and emitting [LLVM intermediate representation][ref_llvm_langref] through
the [inkwell][ref_inkwell] bindings. The bytecode it consumes has already passed a structural verifier, in
the tradition the [Java Virtual Machine Specification][ref_jvm_spec] sets out for bytecode verification, so
the backend declines what it cannot lower and does not approximate it. The classification instrument is a
test in the same package, reporting rather than asserting, with one guard that fails if the corpus walk
finds nothing, because a broken path and a real zero look identical in a report.

The differential oracle drives both the virtual machine and the just-in-time compiled native code over
identical bytecode and compares the whole sequence of yielded values. The stream drivers are bounded by a
caller-supplied count, because a productively divergent program will otherwise run until something kills it,
and a hung test reports nothing at all, worse than a failing one.

## Epistemic State

**Measured, and reproducible from the instrument.** The corpus yields 24 stream chunks, of which 22 have a
single suspension at the end of the body, 0 have multiple top-level suspensions, 1 has suspensions nested in
conditionals, and 1 delegates with no suspension of its own. The nested chunk has 19 suspensions, all inside
conditionals and none inside a loop, at nesting depths from 2 to 11. The corpus contains exactly 1
terminating coroutine chunk, in which 9 of 9 suspensions are immediately followed by a return. Ten stream
chunks are refused by the current tail-position rule for a tail sequence that is effect-free and
stack-neutral.

**Derived, and checkable from the definitions.** That a terminating coroutine produces two distinguishable
observable events while a return-based convention provides one channel, and that the second therefore cannot
carry the first, by $\lvert W \times W \rvert = \lvert W \rvert^2 > \lvert W \rvert$ for $\lvert W \rvert
\ge 2$. That a divergent coroutine produces one, because its trace alphabet omits the completion letter.
That the admissibility rule satisfies $R \subsetneq P$, so its defect is coverage and not soundness. That
$\Delta(\pi) = -1$ for both candidate tail segments. That a suspension inside a conditional is a
control-flow join while one inside a loop crosses a back edge.

**Assumed, and marked as such.** That the return convention is cheaper at run time. The structural grounds
are stated and the frame-size measurement that would establish it was not performed, because the
machine-code section carrying it is not emitted on this host.

**Verified, and the verification method itself produced a finding twice.** All 35 hand-selected research
identifiers were resolved against the registry and compared with the work they are cited as.
**Thirty-five of thirty-five resolve to that work, an error rate of zero.** The 1,945
harvested identifiers were **not** audited that way and do not need to be, because they were transcribed
from the registry that issued them rather than recalled, so the failure mode the audit exists to catch
cannot arise. What the audit would still catch, and did not run for, is a harvested record cited for a claim
it does not support, and no harvested record is cited for any claim.

**Sampled, because checking all of them would be checking the registry against itself.** A random sample of
250 harvested identifiers was resolved, and **250 of 250 exist**. What the sample does establish is a
transcription check on the pipeline in this repository, since a fault there would affect a constant fraction
of records and not a rare one, and no such fraction appeared.

**Twenty-two of the 250, or 8.8 percent, resolved only through the registry.** The identifier resolver did
not serve them. Twenty refused the connection outright, of which 14 were Defense Technical Information
Center deposits, and 2 returned a not-found response from a publisher that no longer serves the landing
page. **In every one of the 22 the identifier is registered and the record is correct.** The defect is
therefore in the resolution path and not in the citation. It is reported because a reader checking a sample
of these references by clicking them will meet roughly one failure in eleven, and that failure is not
evidence of a bad citation.

**Two passes were run with two different instruments and they flagged different records, which is itself the lesson.**
A title-overlap heuristic flagged four. A later check comparing author surname and year flagged five.
**The union is eight distinct records and every one of them was vindicated on individual inspection**, for
four separate reasons.

| Artefact | Records | What the registry does |
|---|---|---|
| Title split from subtitle | 3 | Stores "CakeML", "Coroutines" or "Capriccio" while the citation carries the full descriptive title |
| Wrong registration agency | 1 | Proceedings in the LIPIcs series deposit with DataCite, so a Crossref lookup returns nothing for a valid identifier |
| **Surname particle dropped** | 1 | Stores de Moura as "Moura", so an anchor built from the full surname fails a substring test |
| **Registry typo** | 1 | Stores "Dyvbig" for Dybvig, so the article is right and the registry is wrong |
| **Identifier resolves to a reprint** | 2 | Reynolds 1972 and Strachey and Wadsworth 1974 carry identifiers for their 1998 and 2000 reprints in Higher-Order and Symbolic Computation, so the registry year is later than the year cited |

**The last category is the one worth carrying forward, because it is not an instrument error at all.** The
identifier is correct, the work is correct, and the year genuinely differs, since a foundational paper and
its journal reprint are two publications of one text.
**A checker comparing years will flag every reprinted classic in any bibliography**, and a bibliography of
foundational work is mostly reprinted classics.

**Not one of the eight was a citation defect**, and reporting any of them as one would have been a
measurement mistake of exactly the kind this series keeps documenting. It is recorded because the
[previous article][related_post_a369] reported a 5.5 percent rate by the same method and did not separate
these artefacts from genuine mismatches, which means
**that figure is an upper bound rather than an estimate** and the true rate there may be lower.

**Corrected during writing, and left visible.** The plan this article set out to support was to unify the
two conventions, and it survived until it was traced against a three-instruction example.
**The central claim was also stated in a form stronger than the evidence supported**, assuming a one-word
return until the governing application binary interface documents were read, and the correction opened an
option the draft did not contain. An earlier design in this series specified a reordering transformation for
bodies with several suspension points, of which the corpus contains none. A classification that called
nineteen suspensions "the general case" was collapsing two structurally different situations, and the
per-suspension measurement separated them.

**Corrected after publication, and left visible.** Two defects reached the published text and both are
repaired above rather than silently.

**The widened-return option was published under-costed.** It was presented as costing a wider return and a
host-side discrimination while preserving the frame property. **A widened return does not give
reentrancy.** A terminating coroutine that suspends more than once must resume mid-body, which needs saved
state, which is a frame. The honest interface is a triple carrying a continuation and not a pair carrying a
tag, the per-call model omitted the frame term entirely, and the claim that the frame property is preserved
holds only for a coroutine that suspends at most once per call. **The error was in the direction that made
that option look more attractive than it is**, and the correction therefore strengthens the recommendation
rather than disturbing it. The pigeonhole argument, the semantic-boundary finding and every measurement are
unaffected.

**The corpus could not have exposed it, and that is the article's own lesson turned back on the article.**
The corpus holds exactly one terminating chunk and it suspends at most once per call, so a tagged pair
genuinely does suffice for it, because resuming mid-body and resuming at entry after the sole suspension
coincide. The general case never appears. **A distribution over instances cannot answer a question about an
interface**, which this article establishes at length and then failed to apply when costing an option. It
was raised before publication and did not reach the text.

**The option count contradicted the list beneath it.** The published text read that two options remained
and then set out three. The sentence was introduced by a later editing pass that replaced a colon-led label
with a full sentence and asserted a count the list never had. It now reads three.

**What this article does not establish.** Which of the remaining options is correct, since that turns on an
ABI decision belonging to a workstream this article does not speak for. Whether the widened-return option is
cheaper than two conventions, which is an empirical question and is not measured here. Whether the
source-restructuring option is reasonable. Whether the corpus resembles the population the generator will
serve.

**The literature survey has two layers with different standing and only one of them bears on the argument.**

The 35 hand-selected works were chosen by the author's judgement of relevance, were read, and
are the ones the prose reasons from. **That layer is a narrative review.** No protocol was registered and no
completeness is claimed for it.

The 1,945 harvested works were retrieved by fixed queries against two registries and
admitted by a stated filter, which is reproducible in a way the narrative layer is not.
**It is still not a systematic review.** The query set was written by the same author whose judgement the
narrative layer rests on, only two registries were searched, no grey literature was sought, no inclusion
criteria beyond the title filter were applied, and no harvested record was read.

A reader should therefore treat the assertion that four traditions converge on a discriminated return as
**an observation over the works cited rather than over the field**. The specific negative claim, that none
of the surveyed work addresses per-form selection in a bounded-memory setting, is the one most exposed to an
omission. **The harvest makes that claim more exposed rather than less**, because the harvested titles were
not read and a paper answering the question could sit in the list unremarked. It is stated as a gap in the
survey rather than a gap in the literature.

**The strongest claim the evidence supports** is that the return convention cannot serve terminating
coroutines, on an argument that does not depend on the corpus at all.
**The weakest link is the cost comparison** between the two remaining options, which rests on an unmeasured
performance claim and on a corpus of twenty-four.

## Out of Scope

The design of the lowering for any individual instruction. Register allocation, scheduling and peephole
optimisation. The worst-case execution time analysis, which is a separate subject with a separate method.
The exact frame-size comparison between the two conventions, which requires a target this host does not
emit. Whether the delegating program should be restructured, which is a language question. The Keleusma
language itself, which is covered in [the getting-started article][related_post_keleusma_022] and
[the self-hosting strategy][related_post_keleusma_self_hosting].

## Conclusion

An apparent design wart turned out to be a semantic boundary, and the evidence that made it look like a wart
was accurate. The measurement said nine out of nine, and nine out of nine was true. It was a fact about the
shape of instances, offered in answer to a question about the arity of an interface, and the two are not the
same question.

The check that settled it cost one traced example and produced an argument that holds independently of the
corpus, which the measurement it overturned does not.
**Where a claim can be settled by counting the channels an interface provides against the outcomes a behaviour produces, that count dominates any distribution over instances**,
and it is available before any code is written.

The article also reports a rule shipped one increment earlier that is stricter than its own stated purpose,
refusing ten of twenty-four cases whose tail sequence is provably harmless. It was found by building a
table, not by running a test, which is now the second such finding in this series and no longer looks like a
coincidence.

## References

**The references below come from two sources and the distinction matters.**

35 research references, together with every specification, application binary interface
document and piece of reference documentation, were **selected by hand** because the argument depends on
them. Each states something a step of the reasoning uses, and none is included for completeness.

The remaining 1,945 research references were
**harvested from bibliographic registries by query**
and constitute the survey in The Contemporary Literature. They were not selected for agreement with the
article's conclusion and the selection that produced them is reported in Method.

**The two sources have different failure modes and the previous article was caught by one of them.**
The [previous article in this series][related_post_a369] reports a 5.5
percent error rate on its identifiers, and the cause was that the identifiers were supplied from memory,
which is a generative process that produces plausible identifiers for works that do not carry them.
**Harvesting removes that failure mode rather than reducing it**, because a harvested identifier is
transcribed from the registry that issued it and was never a guess. What harvesting does not remove is the
risk that a correctly transcribed record is cited for a claim it does not support, and that risk falls on
the 35 hand-selected entries, which is why those and only those are also checked against the
work they are cited as. The result of that check is reported in the Epistemic State and not assumed.

### Reference

- [Arm Architecture Procedure Call Standard for the Arm 64-bit Architecture][ref_aapcs64]
- [C++ Coroutines][ref_cpp_coroutines]
- [ECMA-262, ECMAScript Language Specification][ref_ecma262]
- [ECMA-334, C# Language Specification][ref_ecma334]
- [inkwell, safe Rust bindings to LLVM][ref_inkwell]
- [Oracle Java Virtual Machine Specification][ref_jvm_spec]
- [Kotlin Coroutines][ref_kotlin_coroutines]
- [LLVM Coroutines][ref_llvm_coroutines]
- [LLVM Language Reference][ref_llvm_langref]
- [LLVM Stack Maps and Patch Points][ref_llvm_stackmaps]
- [Lua 5.4 Reference Manual][ref_lua54]
- [PEP 255, Simple Generators][ref_pep255]
- [PEP 342, Coroutines via Enhanced Generators][ref_pep342]
- [PEP 380, Syntax for Delegating to a Subgenerator][ref_pep380]
- [PEP 492, Coroutines with async and await Syntax][ref_pep492]
- [POSIX `makecontext` and `swapcontext`][ref_posix_ucontext]
- [The Rust Reference][ref_rust_reference]
- [System V Application Binary Interface, AMD64 Architecture Processor Supplement][ref_sysv_amd64]
- [WebAssembly Stack Switching Proposal][ref_wasm_stack_switching]

[ref_aapcs64]: https://github.com/ARM-software/abi-aa
[ref_cpp_coroutines]: https://en.cppreference.com/w/cpp/language/coroutines
[ref_ecma262]: https://tc39.es/ecma262/
[ref_ecma334]: https://www.ecma-international.org/publications-and-standards/standards/ecma-334/
[ref_inkwell]: https://github.com/TheDan64/inkwell
[ref_jvm_spec]: https://docs.oracle.com/javase/specs/jvms/se21/html/index.html
[ref_kotlin_coroutines]: https://kotlinlang.org/docs/coroutines-overview.html
[ref_llvm_coroutines]: https://llvm.org/docs/Coroutines.html
[ref_llvm_langref]: https://llvm.org/docs/LangRef.html
[ref_llvm_stackmaps]: https://llvm.org/docs/StackMaps.html
[ref_lua54]: https://www.lua.org/manual/5.4/manual.html
[ref_pep255]: https://peps.python.org/pep-0255/
[ref_pep342]: https://peps.python.org/pep-0342/
[ref_pep380]: https://peps.python.org/pep-0380/
[ref_pep492]: https://peps.python.org/pep-0492/
[ref_posix_ucontext]: https://pubs.opengroup.org/onlinepubs/9699919799/functions/makecontext.html
[ref_rust_reference]: https://doc.rust-lang.org/reference/
[ref_sysv_amd64]: https://gitlab.com/x86-psABIs/x86-64-ABI
[ref_wasm_stack_switching]: https://github.com/WebAssembly/stack-switching

### Related Post

- [Related Post, Compiler Backend Bring-Up: Blocking Frequency as the Ordering Principle][related_post_a369]
- [Related Post, Getting Started with Keleusma 0.2.2][related_post_keleusma_022]
- [Related Post, Keleusma's Self-Hosting Strategy][related_post_keleusma_self_hosting]

[related_post_a369]: {% post_url 2026-08-06-native_lowering_coverage %}
[related_post_keleusma_022]: {% post_url 2026-07-11-keleusma_0_2_2_getting_started %}
[related_post_keleusma_self_hosting]: {% post_url 2026-07-12-keleusma_self_hosting_strategy %}

### Research

- [2018, 2018 Proceedings of the International Conference on Embedded Software EMSOFT][research_2018_proceedings_2018]
- [2002, 3D Pre-Stack Depth Migration V0 Analysis and Monte Carlo Automatic Velocity Picking in Depth][research_3d_pre_stack_2002]
- [2012, A Compositional Scheme and Framework for Safety Critical Systems Verification][research_a_compositional_2012]
- [2020, A Fibrational Method of Indexed Coinductive Data Types][research_a_fibrational_2020]
- [A and others, 2024, Design of Mechatronics Based Virtual Telepresence for Robotic System Using Raspberry Python Interpreter][research_a_s_2024]
- [2004, A structural approach to operational semantics][research_a_structural_2004]
- [Abdallah, 2018, PRISM revisited Declarative implementation of a probabilistic programming language using multi-prompt delimited control][research_abdallah_2018]
- [Abdelmaksoud and others, 2023, DEL Dynamic Symbolic Execution-based Lifter for Enhanced Low-Level Intermediate Representation][research_abdelmaksoud_hammadeh_2023]
- [Abdulaziz and Koller, 2022, Formal Semantics and Formally Verified Validation for Temporal Planning][research_abdulaziz_koller_2022]
- [Abdulsalam and others, 2014, Program energy efficiency The impact of language, compiler and implementation choices][research_abdulsalam_lakomski_2014]
- [Abe, 2019, A type system for data independence of loop iterations in a directive-based PGAS language][research_abe_2019]
- [Abella and others, 2017, Measurement-Based Worst-Case Execution Time Estimation Using the Coefficient of Variation][research_abella_padilla_2017]
- [Abi-Karam and others, 2023, INR-Arch A Dataflow Architecture and Compiler for Arbitrary-Order Gradient Computations in Implicit Neural Representation Processing][research_abikaram_sarkar_2023]
- [Abrahams, 1979, The CIMS PL/I compiler][research_abrahams_1979]
- [Abramsky and Horsman, 2015, DEMONIC programming a computational language for single-particle equilibrium thermodynamics, and its formal semantics][research_abramsky_horsman_2015]
- [Abu-Yosef and Kong, 2025, Scalable Data-Flow Modeling and Validation of Distributed-Memory Algorithms][research_abuyosef_kong_2025]
- [Aceto and Fokkink, 2004, Guesteditors'introduction Specialissueon Structural Operational Semantics][research_aceto_fokkink_2004]
- [Achour and Benattou, 2018, Constraint Based Testing and Verification of Java Bytecode Programs][research_achour_benattou_2018]
- [Achour and others, 2018, A Constraint-Based Verification Approach for Java Bytecode Programs][research_achour_chouenyib_2018]
- [Acun and others, 2019, Fine-Grained Energy Efficiency Using Per-Core DVFS with an Adaptive Runtime System][research_acun_chandrasekar_2019]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1988, Ada Trade Name Compiler Validation Summary Report. Certificate Number 880620W1.09092, Encore Computer Corporation, Encore Verdix Ada Development System, Version 5.5, Encore Multimax 320][research_adajointprogramofficearlingtonva_1988]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1988, Ada Tradename Compiler Validation Summary Report Certificate Number 880201W1.09019 Verdix Corporation VAda-010-2323, Version 5.5 Sequent Balance 8000][research_adajointprogramofficearlingtonva_1988_2]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1988, Ada Tradename Compiler Validation Summary Report Certificate Number 880429W1.09053 Telesoft, Inc. TeleGen2 Ada Compiler for VAX/VMS to 1750A, Version 3.22 MicroVAX 2 to MIL-STD-1750A ECSPO RAID Simulator][research_adajointprogramofficearlingtonva_1988_3]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1988, Ada Tradename Compiler Validation Summary Report Certificate Number 880815W1.09143 Rational VAX-VMS, Version 2.0.45 Rational R1000 Series 200 Model 20 and VAX-11/750 Host and Target][research_adajointprogramofficearlingtonva_1988_4]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1989, Ada Compiler Validation Procedures Version 2.0][research_adajointprogramofficearlingtonva_1989]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1989, Ada Compiler Validation Summary Report. CONVEX Computer Corporation, CONVEX Ada, Version 1.1 C210, Host and Target 890508W1.10077][research_adajointprogramofficearlingtonva_1989_2]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1989, Ada Compiler Validation Summary Report. Meridian Software Systems, Inc., AdaVantage, Version 3.0, IBM PS/2 Model 80 with Floating Point Co-Processor Host and Target 890405W1.10049][research_adajointprogramofficearlingtonva_1989_3]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1989, Ada Compiler Validation Summary Report. Verdix Corporation, VAda-110-2323, Version 5.5, Sequent Balance 8000 Host and Target , 890216W1.10029][research_adajointprogramofficearlingtonva_1989_4]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1989, Ada Compiler Validation Summary Report Certificate Number 890329I1. 10076 SYSTEAM KG, SYSTEAM Ada Compiler VAX/VMS x MC68020/05-9 Version 1.81][research_adajointprogramofficearlingtonva_1989_5]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1990, Ada Compiler Validation Procedures. Version 2.1][research_adajointprogramofficearlingtonva_1990]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1991, Ada Compiler Validation Summary Report Certificate Number 910612W1. 11168 Telesoft, IBM Ada/370, Version 1.2.0 without Optimization IBM 3080, V / SP HPO Rel 5.0 Unopt Host and Target][research_adajointprogramofficearlingtonva_1991]
- [ADA JOINT PROGRAM OFFICE ARLINGTON VA, 1992, Ada Compiler Validation Procedures, Version 3.1][research_adajointprogramofficearlingtonva_1992]
- [2023, ADAPTIVE PROGRAMMING LANGUAGE LEARNING SYSTEM BASED ON GENERATIVE AI][research_adaptive_programming_2023]
- [Affeldt and others, 2023, Semantics of Probabilistic Programs using s-Finite Kernels in Coq][research_affeldt_cohen_2023]
- [Agathos and others, 2022, Compiler-assisted, adaptive runtime system for the support of OpenMP in embedded multicores][research_agathos_dimakopoulos_2022]
- [Agathos and others, 2011, Design and Implementation of OpenMP Tasks in the OMPi Compiler][research_agathos_hadjidoukas_2011]
- [Телегин, 2023, AHEAD-OF-TIME and JUST-IN-TIME technologies][research_ahead_of_time_and_just_in_time_2023]
- [Ahman and Staton, 2013, Normalization by Evaluation and Algebraic Effects][research_ahman_staton_2013]
- [Aigrain and others, 1984, Experience with a Graham-Glanville style code generator][research_aigrain_graham_1984]
- [Aissa and others, 2007, Bringing Worst Case Execution Time Awareness to an Open Smart Card OS][research_aissa_grimaud_2007]
- [Aisyiyah and Eviyanti, 2026, Android-based Programming Language to Natural Language Translator App][research_aisyiyah_eviyanti_2026]
- [Akanbi and others, 2022, Code Generation Techniques in Compiler Design Conceptual and Structural Review][research_akanbi_ajose_2022]
- [Akdur and others, 2017, Characterizing the Development and Usage of Diagrams in Embedded Software Systems][research_akdur_demirors_2017]
- [Akdur and others, 2017, Cross-factor analysis of software modeling practices versus practitioner demographics in the embedded software industry][research_akdur_garousi_2017]
- [Alatawi and others, 2016, Generating source inputs for metamorphic testing using dynamic symbolic execution][research_alatawi_miller_2016]
- [Al-Bataineh and others, 2015, Accelerating worst case execution time analysis of timed automata models with cyclic behaviour][research_albataineh_reynolds_2015]
- [Albert and others, 2024, Synthesis of Sound and Precise Storage Cost Bounds via Unsound Resource Analysis and Max-SMT][research_albert_correas_2024]
- [Aldweesh and others, 2021, The OpBench Ethereum opcode benchmark framework Design, implementation, validation and experiments][research_aldweesh_alharby_2021]
- [Alexander and Black, 2016, The performance of object encodings in JavaScript][research_alexander_black_2016]
- [Ali and others, 2025, Does Coding Style Really Survive Compilation? Stylometry of Executable Code Revisited][research_ali_bilgis_2025]
- [Ali and others, 2025, CrossGuard Runtime-Adaptive LLM Fuzzing for Cross-Contract Vulnerabilities Detection][research_ali_chen_2025]
- [Aljaafari and others, 2022, Combining BMC and Fuzzing Techniques for Finding Software Vulnerabilities in Concurrent Programs][research_aljaafari_menezes_2022]
- [Alkhalid and Labiche, 2018, Towards GUI Functional Verification using Abstract Interpretation][research_alkhalid_labiche_2018]
- [Alladi and others, 2026, Enabling Automatic Compiler-Driven Vectorization of Transformers][research_alladi_ros_2026]
- [Allamanis and Sutton, 2013, Why, when, and what Analyzing Stack Overflow questions by topic, type, and code][research_allamanis_sutton_2013]
- [Allen and others, 2000, Subsalt Imaging using 3D Pre-Stack Depth Migration in the UK Southern North Sea - a Case History][research_allen_malaguti_2000]
- [Alpay and Heuveline, 2022, How much SYCL does a compiler need? Experiences from the implementation of SYCL as a library for nvc++][research_alpay_heuveline_2022]
- [Alpay and Heuveline, 2023, One Pass to Bind Them The First Single-Pass SYCL Compiler with Unified Code Representation Across Backends][research_alpay_heuveline_2023]
- [Altan, 2026, Error-Resilient Quantum Compiler Design for Efficient Qubit Mapping, Gate Optimization, and Noise Mitigation in NISQ-Era Devices][research_altan_2026]
- [Altassan and Ahmad, 2024, Green threads of change Unravelling the gendered and experienced moderators in the sustainable symphony of green HR practices and environmental responsibility][research_altassan_ahmad_2024]
- [Amaliah and others, 2021, Auto Clustering Source Code To Detect Plagiarism Of Student Programming Assignments in Java Programming Language][research_amaliah_musu_2021]
- [Amarasinghe, 2004, Session details Compiler and simulator construction][research_amarasinghe_2004]
- [Amarasinghe, 2019, The sparse tensor algebra compiler keynote][research_amarasinghe_2019]
- [Amarasinghe, 2020, Compiler 2.0][research_amarasinghe_2020]
- [Amato and others, 2020, On collecting semantics for program analysis][research_amato_meo_2020]
- [Ambal and others, 2022, Certified Derivation of Small-Step From Big-Step Skeletal Semantics][research_ambal_lenglet_2022]
- [Amin and others, 2016, System Verilog Assertions Synthesis Based Compiler][research_amin_ramzy_2016]
- [2022, Analysis on Strengthening Scheme of Office Building Based on Function Change][research_analysis_on_2022]
- [2016, Analytics of Application Resource Utilization within the Virtual Machine][research_analytics_of_2016]
- [Anderson and Loginov, 2013, Static analysis of machine code for supply-chain risk management][research_anderson_loginov_2013]
- [Anderton, 2022, Investigating Sign Language Interpreter Rendering and Guiding Methods in Virtual Reality 360-Degree Content][research_anderton_2022]
- [Andrade Guzmán and Hernández Quiroz, 2020, Natural deduction and semantic models of justification logic in the proof assistant Coq][research_andradeguzman_hernandezquiroz_2020]
- [Andrews and others, 1988, Design and implementation of the UW Illustrated compiler][research_andrews_henry_1988]
- [Aneesh and others, 2024, Smart Compiler Assistant An AST based Python Code Analysis][research_aneesh_saumik_2024]
- [Anier, 2008, Motion recognition with abstract interpretation and HMM][research_anier_2008]
- [Antoniadis and others, 2021, Open-Source Memory Compiler for Automatic RRAM Generation and Verification][research_antoniadis_feng_2021]
- [Aparanji and others, 2017, INDUCTION OF PROPOFOL WITH COINDUCTION OF PROPOFOL, MIDAZOLAM VERSUS PROPOFOL AUTO COINDUCTION- A COMPARATIVE STUDY][research_aparanji_radhasundari_2017]
- [Compiling with Continuations][research_appel_1992]
- [Appel and Jim, 1989, Continuation-passing, closure-passing style][research_appel_jim_1989]
- [Appel and Shao, 1992, Callee-save registers in continuation-passing style][research_appel_shao_1992]
- [Applis and others, 2025, Suspicious Types and Bad Neighborhoods Filtering Spectra with Compiler Information][research_applis_gissurarson_2025]
- [Aquino and others, 2018, Worst-Case Execution Time Testing via Evolutionary Symbolic Execution][research_aquino_denaro_2018]
- [Arakaki and Hirokawa, 2026, Foundational Design of Multi-Modal Typed Programming Language for Quantum-Classical Hybrid Computing System][research_arakaki_hirokawa_2026]
- [Arcaro and others, 2020, Reliability Test based on a Binomial Experiment for Probabilistic Worst-Case Execution Times][research_arcaro_silva_2020]
- [Arceri and Mastroeni, 2019, Static Program Analysis for String Manipulation Languages][research_arceri_mastroeni_2019]
- [Arendsee, 2026, morloc a workflow language for multi-lingual programming under a common type system][research_arendsee_2026]
- [Aristizábal and others, 2017, Environmental Bisimulations for Delimited-Control Operators with Dynamic Prompt Generation][research_aristizabal_biernacki_2017]
- [Arnström and others, 2024, Exact Worst-Case Execution-Time Analysis for Implicit Model Predictive Control][research_arnstrom_broman_2024]
- [Arriaga and others, 2026, Tempo An ML-KEM to PAKE Compiler Resilient to Timing Attacks][research_arriaga_barbosa_2026]
- [2003, ART An Implementation on the Active_object RunTime Systems Applicable for the Embedded Systems][research_art_an_2003]
- [Asadollah and others, 2018, A Runtime Verification Tool for Detecting Concurrency Bugs in FreeRTOS Embedded Software][research_asadollah_sundmark_2018]
- [Asai, 2002, Online partial evaluation for shift and reset][research_asai_2002]
- [Asai, 2004, Offline partial evaluation for shift and reset][research_asai_2004]
- [Asai and Fujii, 2025, Defining Algebraic Effects and Handlers via Trails and Metacontinuations][research_asai_fujii_2025]
- [Askim and others, 2004, 4D Seismic Analysis Using Pre Stack Depth Migration][research_askim_brandsbergdahl_2004]
- [Astarte, 2025, Conceptualising Programming Language Semantics][research_astarte_2025]
- [Ataei and Manohar, 2019, AMC An Asynchronous Memory Compiler][research_ataei_manohar_2019]
- [Atapattu, 1994, Design of a Parallel Object Oriented Programming Language][research_atapattu_1994]
- [Attrapadung and others, 2018, Efficient Two-level Homomorphic Encryption in Prime-order Bilinear Groups and A Fast Implementation in WebAssembly][research_attrapadung_hanaoka_2018]
- [Attrot and others, 2026, A Pattern Generation Language for MLIR Compiler Matching and Rewriting][research_attrot_zago_2026]
- [Auchterlonie and others, 2007, Velocity Model Building for Pre-Stack Depth Migration - An Onshore Libya Case Study][research_auchterlonie_vinje_2007]
- [Audrito and Haures, 2023, Combining Static and Runtime Verification with AC and Coq][research_audrito_haures_2023]
- [Auguston and others, 2001, Visual Meta-Programming Language][research_auguston_berzins_2001]
- [Aung and others, 2011, Compiler-assisted technique for rapid performance estimation of FPGA-based processors][research_aung_lam_2011]
- [Auslander and Hopkins, 1982, An overview of the PL.8 compiler][research_auslander_hopkins_1982]
- [Austen and others, 2025, Sharing Is Scaring Linking Cloud File-Sharing to Programming Language Semantics][research_austen_krishnamurthi_2025]
- [2019, Automatic Port to OpenACC/OpenMP for Physical Parameterization in Climate and Weather Code Using the CLAW Compiler][research_automatic_port_2019]
- [Avanzini and others, 2021, On continuation-passing transformations and expected cost analysis][research_avanzini_barthe_2021]
- [Avigad and others, 2007, A formally verified proof of the prime number theorem][research_avigad_donnelly_2007]
- [Avigad and others, 2025, A Proof-Producing Compiler for Blockchain Applications][research_avigad_goldberg_2025]
- [Avigad and others, 2017, A Formally Verified Proof of the Central Limit Theorem][research_avigad_holzl_2017]
- [Avvenuti and others, 2003, Java bytecode verification for secure information flow][research_avvenuti_bernardeschi_2003]
- [Azeemi, 2006, Compiler Directed Battery-Aware Implementation of Mobile Applications][research_azeemi_2006]
- [Aziz and Labiche, 2026, ProtoSYCL A Sample Implementation of a SYCL Compiler for Conformance Test Suite Development][research_aziz_labiche_2026]
- [Azmi, 2025, LLM-Aware Static Analysis Adapting Program Analysis to Mixed Human/AI Codebases at Scale][research_azmi_2025]
- [Azzahra and others, 2020, PRE STACK DEPTH MIGRATION UNTUK KOREKSI EFEK PULL UP DENGAN MENGGUNAKAN METODE HORIZON BASED DEPTH TOMOGRAPHY PADA LAPANGAN 'A1 DAN A2'][research_azzahra_mulyatno_2020]
- [Badler, 1996, A Task Networking and Visual Programming Language for Jack][research_badler_1996]
- [Baek and Kim, 2017, Prototype implementation of the OpenGL ES 2.0 shading language offline compiler][research_baek_kim_2017]
- [Baek and Lee, 2024, CaLLi OCaml library for static analysis of LLVM bitcode][research_baek_lee_2024]
- [Baev, 2009, Techniques for Region-Based Register Allocation][research_baev_2009]
- [Baggett, 2000, An Abstract Interpretation of the Wavelet Dimension Function Using Group Representations][research_baggett_2000]
- [Baghdadi and others, 2019, Tiramisu A Polyhedral Compiler for Expressing Fast and Portable Code][research_baghdadi_ray_2019]
- [Bai and others, 2025, APCer An Agile Physical Compiler for Multi-Port Register File][research_bai_ming_2025]
- [Bailin and others, 1993, Model-based reasoning for system and software engineering The Knowledge From Pictures KFP environment][research_bailinsydney_paterrafrank_1993]
- [Baird and Johnson, 1977, COBOL Compiler Validation System, 1974. Version 3.0][research_baird_johnson_1977]
- [Baird and Oliver, 1977, Programming Language Standards -- Who Needs Them][research_baird_oliver_1977]
- [Baltes and Diehl, 2018, Usage and attribution of Stack Overflow code snippets in GitHub projects][research_baltes_diehl_2018]
- [Baltes and others, 2019, SOTorrent Studying the Origin, Evolution, and Usage of Stack Overflow Code Snippets][research_baltes_treude_2019]
- [Balu and Saraswathi, 2014, Implementation of SAAS Compiler in Intranet][research_balu_saraswathi_2014]
- [Banerjee and Karfa, 2018, Compiler-agnostic Translation Validation][research_banerjee_karfa_2018]
- [Bansal and Singh, 2011, Dual Stack Implementation of Mobile IPv6 Software Architecture][research_bansal_singh_2011]
- [Bao and others, 2014, PWCET Power-Aware Worst Case Execution Time Analysis][research_bao_tavarageri_2014]
- [Baradaran and others, 2026, Reusing Legacy Code in Wasm Key Challenges of Compilation and Code Semantics Preservation][research_baradaran_huang_2026]
- [Barai and others, 2023, LLVM Static Analysis for Program Characterization and Memory Reuse Profile Estimation][research_barai_santhi_2023]
- [Baramashetru and others, 2025, A Type System for Data Privacy Compliance in Active Object Languages][research_baramashetru_giannini_2025]
- [Barany, 2018, Finding missed compiler optimizations by differential testing][research_barany_2018]
- [Barash and Shchur, 2013, RNGSSELIB Program library for random number generation. More generators, parallel streams of random numbers and Fortran compatibility][research_barash_shchur_2013]
- [Barbosa and others, 2025, Formally Verified Correctness Bounds for Lattice-Based Cryptography][research_barbosa_kannwischer_2025]
- [Barbuti and Cataudella, 2004, Java bytecode verification on Java cards][research_barbuti_cataudella_2004]
- [Barbuti and others, 2002, Fixing the Java bytecode verifier by a suitable type domain][research_barbuti_tesei_2002]
- [Bardonek and Zachariasova, 2026, Leveraging design static analysis for vertical reuse Analytical interpretation and scalability behavior][research_bardonek_zachariasova_2026]
- [Barinov and others, 2020, Applying compiler-based binary watermarking technology to ensure binary compatibility in GNU/Linux distribution][research_barinov_kashkarov_2020]
- [Baroffio and Reghenzani, 2023, Compiler-Injected SIHFT for Embedded Operating Systems][research_baroffio_reghenzani_2023]
- [Barrière and others, 2021, Formally verified speculation and deoptimization in a JIT compiler][research_barriere_blazy_2021]
- [Barrière and others, 2023, Formally Verified Native Code Generation in an Effectful JIT Turning the CompCert Backend into a Formally Verified JIT Compiler][research_barriere_blazy_2023]
- [Barthe and others, 2017, Verified Translation Validation of Static Analyses][research_barthe_blazy_2017]
- [Bartlett and others, 2010, Accurate Determination of Loop Iterations for Worst-Case Execution Time Analysis][research_bartlett_bate_2010]
- [Bartsch and others, 2021, Compositional Fault Propagation Analysis in Embedded Systems using Abstract Interpretation][research_bartsch_wilhelm_2021]
- [Basin and others, 2003, Bytecode Verification by Model Checking][research_basin_friedrich_2003]
- [Baskaran and others, 2016, Automatic Code Generation and Data Management for an Asynchronous Task-Based Runtime][research_baskaran_pradelle_2016]
- [Basold and Geuvers, 2016, Type Theory based on Dependent Inductive and Coinductive Types][research_basold_geuvers_2016]
- [Bassil, 2019, Compiler Design for Legal Document TranslationIn Digital Government][research_bassil_2019]
- [Basu and others, 2015, Compiler-Directed Transformation for Higher-Order Stencils][research_basu_hall_2015]
- [Basu and others, 2017, Compiler-based code generation and autotuning for geometric multigrid on GPU-accelerated supercomputers][research_basu_williams_2017]
- [Bate and Kazakov, 2008, New Directions in Worst-Case Execution Time analysis][research_bate_kazakov_2008]
- [Battle and others, 2022, Exploring D3 Implementation Challenges on Stack Overflow][research_battle_feng_2022]
- [Bau and others, 2022, Abstract interpretation of Michelson smart-contracts][research_bau_mine_2022]
- [Bauckholt and Holz, 2024, WebAssembly as a Fuzzing Compilation Target Registered Report][research_bauckholt_holz_2024]
- [Bauer and Pretnar, 2014, An Effect System for Algebraic Effects and Handlers][research_bauer_pretnar_2014]
- [Bauer and Pretnar, 2015, Programming with algebraic effects and handlers][research_bauer_pretnar_2015]
- [Bauml and Brada, 2011, Reconstruction of Type Information from Java Bytecode for Component Compatibility][research_bauml_brada_2011]
- [Bavera and Bonelli, 2008, Type-based information flow analysis for bytecode languages with variable object field policies][research_bavera_bonelli_2008]
- [Bayer and others, 1968, MPL MATHEMATICAL PROGRAMMING LANGUAGE][research_bayer_bigelow_1968]
- [Bayley and Shiel, 2005, JVM Bytecode Verification Without Dataflow Analysis][research_bayley_shiel_2005]
- [Beaumont and others, 2018, Fast approximation algorithms for task-based runtime systems][research_beaumont_eyrauddubois_2018]
- [Becker and Chakraborty, 2018, Optimizing Worst-Case Execution Times Using Mainstream Compilers][research_becker_chakraborty_2018]
- [Becker and others, 2018, Scalable and precise estimation and debugging of the worst-case execution time for analysis-friendly processors a comeback of model checking][research_becker_metta_2018]
- [Bee and bernardo, 2018, Predicting Fork Visibility Performance on Programming Language Interoperability in Open Source Projects][research_bee_bernardo_2018]
- [Bekiris, 2021, Implementation of UTASTAR Decision Support System in VΒΑ Programming Language][research_bekiris_2021]
- [Belyaev and others, 2018, Comparative Analysis of Two Approaches to Static Taint Analysis][research_belyaev_shimchik_2018]
- [Benito-Montoro and others, 2021, A Tool to Assist the Compiler Construction Instructor in Checking the Equivalence of Specifications Based on Regular Expressions][research_benitomontoro_chen_2021]
- [Benzaken and Contejean, 2019, A Coq mechanised formal semantics for realistic SQL queries formally reconciling SQL and bag relational algebra][research_benzaken_contejean_2019]
- [Béra and others, 2016, Practical Validation of Bytecode to Bytecode JIT Compiler Dynamic Deoptimization][research_bera_miranda_2016]
- [Berdine and others, 2002, Linear Continuation-Passing][research_berdine_ohearn_2002]
- [Berg and others, 2025, Manim-DFA Visualising Data Flow Analysis and Abstract Interpretation Algorithms with Automated Video Generation][research_berg_yernaux_2025]
- [Berger and others, 2025, Translation Validation for LLVM's AArch64 Backend][research_berger_briles_2025]
- [Berger and Spreen, 2016, A coinductive approach to computing with compact sets][research_berger_spreen_2016]
- [Berghofer and Strecker, 2004, Extracting a formally verified, fully executable compiler from a proof assistant][research_berghofer_strecker_2004]
- [Berlakovich and others, 2026, LOOL Low-Overhead, Optimization-Log-Guided Compiler Fuzzing][research_berlakovich_schwarcz_2026]
- [Berlakovich and others, 2026, LOOL Low-Overhead, Optimization-Log-Guided Compiler Fuzzing - RCR Report][research_berlakovich_schwarcz_2026_2]
- [Bernardeschi and others, 2004, Checking secure information flow in Java bytecode by code transformation and standard bytecode verification][research_bernardeschi_defrancesco_2004]
- [Bernardeschi and others, 2008, Decomposing bytecode verification by abstract interpretation][research_bernardeschi_francesco_2008]
- [Bernardeschi and others, 2006, Using Control Dependencies for Space-Aware Bytecode Verification][research_bernardeschi_lettieri_2006]
- [Bernat and Burns, 2000, An Approach to Symbolic Worst-Case Execution Time Analysis][research_bernat_burns_2000]
- [Berten and others, 2009, Managing Imprecise Worst Case Execution Times on DVFS Platforms][research_berten_chang_2009]
- [Bertholon and others, 2024, Interactive Source-to-Source Optimizations Validated using Static Resource Analysis][research_bertholon_chargueraud_2024]
- [Bertrane and others, 2010, Static Analysis and Verification of Aerospace Software by Abstract Interpretation][research_bertrane_cousot_2010]
- [Bertrane and others, 2015, Static Analysis and Verification of Aerospace Software by Abstract Interpretation][research_bertrane_cousot_2015]
- [Besson and others, 2018, CompCertS A Memory-Aware Verified C Compiler Using a Pointer as Integer Semantics][research_besson_blazy_2018]
- [Besson and others, 2019, Information-Flow Preservation in Compiler Optimisations][research_besson_dang_2019]
- [Bezrąk and Przyłucki, 2020, Impact of the cloud application programming language on the performance of its implementation in selected serverless environments][research_bezrak_przylucki_2020]
- [Bhamidipati and Vemuri, 2023, ASPIRE An Intermediate Representation for Abstract Security Policies][research_bhamidipati_vemuri_2023]
- [Bhasker, 1988, Implementation of an optimizing compiler for VHDL][research_bhasker_1988]
- [Bhoyar and others, 2025, Sign Language Interpreter using Long Short-Term Memory LSTM][research_bhoyar_jain_2025]
- [Bhushan and Yadav, 2020, Verification of Virtual Machine Architecture in a Hypervisor through Model Checking][research_bhushan_yadav_2020]
- [Bicarregui and others, 2006, The verified software repository a step towards the verifying compiler][research_bicarregui_hoare_2006]
- [Pause 'n' Play: Formalizing Asynchronous C#][research_bierman_2012]
- [Biernacki and others, 2005, A Dynamic Continuation-Passing Style for Dynamic Delimited Continuations][research_biernacki_danvy_2005]
- [Biernacki and others, 2005, A Dynamic Continuation-Passing Style for Dynamic Delimited Continuations Preliminary Version][research_biernacki_danvy_2005_2]
- [Biernacki and Danvy, 2005, A Simple Proof of a Folklore Theorem about Delimited Control][research_biernacki_danvy_2005_3]
- [Biernacki and others, 2006, A Dynamic Continuation-Passing Style for Dynamic Delimited Continuations][research_biernacki_danvy_2006]
- [BIERNACKI and DANVY, 2006, THEORETICAL PEARL A simple proof of a folklore theorem about delimited control][research_biernacki_danvy_2006_2]
- [Biernacki and others, 2015, A Dynamic Continuation-Passing Style for Dynamic Delimited Continuations][research_biernacki_danvy_2015]
- [Biernacki and others, 2019, Bisimulations for Delimited-Control Operators][research_biernacki_lenglet_2019]
- [Biernacki and others, 2017, Handle with care relational interpretation of algebraic effects and handlers][research_biernacki_pirog_2017]
- [Bik and others, 2022, Compiler Support for Sparse Tensor Computations in MLIR][research_bik_koanantakool_2022]
- [Biradar and others, 2026, Design and Development of an AI-Powered Code Generation System with Persistent Memory and Multi-Agent Architecture][research_biradar_dhikale_2026]
- [Bird, 1982, An implementation of a code generator specification language for table driven code generators][research_bird_1982]
- [Bishnu and Bhatia, 2018, Algorithmic Compiler based FPGA Implementation of Iterative Time-Domain Algorithm for Sparse Channel Estimation][research_bishnu_bhatia_2018]
- [Bispo and Cardoso, 2016, A MATLAB subset to C compiler targeting embedded systems][research_bispo_cardoso_2016]
- [Blaak and Van Cutsem, 2026, Towards Least-Privilege WebAssembly Applications Transparent Interposition for WebAssembly Components][research_blaak_vancutsem_2026]
- [Blanc and Kadobayashi, 2010, Towards revealing JavaScript program intents using abstract interpretation][research_blanc_kadobayashi_2010]
- [Blaß and Philippsen, 2019, GPU-accelerated fixpoint algorithms for faster compiler analyses][research_blass_philippsen_2019]
- [Blazy, 2020, From Verified Compilation to Secure Compilation a Semantic Approach][research_blazy_2020]
- [Blazy, 2023, CompCert A Journey through the Landscape of Mechanized Semantics for Verified Compilation Keynote][research_blazy_2023]
- [Blazy and others, 2015, Verified Validation of Program Slicing][research_blazy_maroneze_2015]
- [Blieberger, 2002, Data-Flow Frameworks for Worst-Case Execution Time Analysis][research_blieberger_2002]
- [Blower, 1984, An efficient implementation of visibility in Ada][research_blower_1984]
- [Bockisch and others, 2020, Java Bytecode Verification with OCL Why, How and Whenc][research_bockisch_taentzer_2020]
- [Boda and others, 2026, CPerfSmith A Randomized C Program Generator for Performance-Oriented Compiler Testing][research_boda_chunduri_2026]
- [Bodin and others, 2015, Certified Abstract Interpretation with Pretty-Big-Step Semantics][research_bodin_jensen_2015]
- [Boding, 1996, Pre-stack depth migration in three dimensions with the imaging wave machine][research_boding_1996]
- [Bodwin and others, 1982, Experience with an experimental compiler generator based on denotational semantics][research_bodwin_bradley_1982]
- [Böhme and others, 2009, HOL-Boogie-An Interactive Prover-Backend for the Verifying C Compiler][research_bohme_moskal_2009]
- [Bohnet and Dollner, 2007, CGA Call Graph Analyzer - Locating and Understanding Functionality within the Gnu Compiler Collection's Million Lines of Code][research_bohnet_dollner_2007]
- [Boldo and others, 2013, A Formally-Verified C Compiler Supporting Floating-Point Arithmetic][research_boldo_jourdan_2013]
- [Bonar and Liffick, 1987, A Visual Programming Language for Novices][research_bonar_liffick_1987]
- [Bonchi and Pous, 2015, Hacking nondeterminism with induction and coinduction][research_bonchi_pous_2015]
- [Bond, 2013, Session details Garbage collection, runtime, and cache management][research_bond_2013]
- [Bonkowski and others, 1979, Porting the Zed compiler][research_bonkowski_gentleman_1979]
- [Bonyun, 1979, Euclid Compiler for PDP-11][research_bonyun_1979]
- [Bonyun and Holt, 1978, EUCLID Compiler for PDP-11][research_bonyun_holt_1978]
- [Boo and Lee, 2025, Finding Device Driver Bugs With Fuzzing PCIe Configuration Input][research_boo_lee_2025]
- [BOOK and others, 1963, A ONE PASS JOVIAL COMPILER][research_book_bratman_1963]
- [Boonriong and others, 2025, Compiler Fuzzing in Continuous Integration A Case Study on Dafny][research_boonriong_zetzsche_2025]
- [Bosse, 2018, A Unified System Modelling and Programming Language based on JavaScript and a Semantic Type System][research_bosse_2018]
- [- and others, 2013, Bounding the Worst-Case Execution Time for the Fixed-Priority Preemptive Systems Based on the Preemption Points][research_bounding_the_worst_case_2013]
- [bounpaserth, 2026, A Study of the Computer Programming Language Implementation in Computer Engineering Students using the Flowgorithm Platform versus Common Programming][research_bounpaserth_2026]
- [Bourke, 2021, Specification and end-to-end proof of a reactive language and its compiler invited talk][research_bourke_2021]
- [Bourke and others, 2017, A formally verified compiler for Lustre][research_bourke_brun_2017]
- [Bourke and others, 2018, Towards a verified Lustre compiler with modular reset][research_bourke_brun_2018]
- [Bourke and others, 2019, Mechanized semantics and verified compilation for a dataflow synchronous language with reset][research_bourke_brun_2019]
- [Bourke and others, 2025, Functional Stream Semantics for a Synchronous Block-Diagram Compiler][research_bourke_jeanmaire_2025]
- [Bowman and Ahmed, 2018, Typed closure conversion for the calculus of constructions][research_bowman_ahmed_2018]
- [Boyapati, 2004, Session details Register allocation][research_boyapati_2004]
- [Brachthäuser and others, 2018, Effect handlers for the masses][research_brachthauser_schuster_2018]
- [Brachthäuser and others, 2020, Effects as capabilities effect handlers and lightweight effect polymorphism][research_brachthauser_schuster_2020]
- [BRACHTHÄUSER and others, 2020, Effekt Capability-passing style for type- and effect-safe, extensible effect handlers in Scala][research_brachthauser_schuster_2020_2]
- [Brady, 2013, Programming and reasoning with algebraic effects and dependent types][research_brady_2013]
- [Brady and Hammond, 2006, A verified staged interpreter is a verified compiler][research_brady_hammond_2006]
- [Brandner and Jordan, 2014, Refinement of worst-case execution time bounds by graph pruning][research_brandner_jordan_2014]
- [Brant and others, 2025, IoT-CODIFT Compiler Optimization DIFT for IoT and Embedded Devices][research_brant_sunkara_2025]
- [Breitner, 2015, Formally proving a compiler transformation safe][research_breitner_2015]
- [Brennan and others, 2020, JIT Leaks Inducing Timing Side Channels through Just-In-Time Compilation][research_brennan_rosner_2020]
- [Briggs and others, 1994, Improvements to graph coloring register allocation][research_briggs_cooper_1994]
- [Brock and others, 2018, PAYJIT space-optimal JIT compilation and its practical implementation][research_brock_ding_2018]
- [Brodersen, 1994, Anatomy of a Silicon Compiler][research_brodersen_1994]
- [Bruno and others, 2021, Compiler-assisted object inlining with value fields][research_bruno_jovanovic_2021]
- [Bruza, 2016, Syntax and operational semantics of a probabilistic programming language with scopes][research_bruza_2016]
- [Bryant and others, 2025, Certified Knowledge Compilation with Application to Formally Verified Model Counting][research_bryant_nawrocki_2025]
- [Buchwald and others, 2016, Verified construction of static single assignment form][research_buchwald_lohner_2016]
- [Bulej and others, 2016, Beneath the bytecode][research_bulej_zheng_2016]
- [Bunkenburg and Wu, 2024, Making a Curry Interpreter using Effects and Handlers][research_bunkenburg_wu_2024]
- [Búr and others, 2021, Worst-case Execution Time Calculation for Query-based Monitors by Witness Generation][research_bur_marussy_2021]
- [Burdy and Pavlova, 2006, Java bytecode specification and verification][research_burdy_pavlova_2006]
- [Burgholzer and others, 2026, Focus Session Paper The MQT Compiler Collection A Blueprint for a Future-Proof Quantum-Classical Compilation Framework][research_burgholzer_haag_2026]
- [Burn, 1990, A relationship between abstract interpretation and projection analysis][research_burn_1990]
- [Burroughs, 2016, Register allocation and spilling using the expected distance heuristic][research_burroughs_2016]
- [Bushnell and others, 2008, Automatic Testcase Generation for Flight Software][research_bushnelldavidhenry_pasareanucorina_2008]
- [Butler and Johnson, 1993, Formal Methods for Life-Critical Software][research_butlerrickyw_johnsonsallyc_1993]
- [Butterfield and Woodcock, 2006, A "Hardware Compiler" Semantics for Handel-C][research_butterfield_woodcock_2006]
- [2017, C# Compiler for Blind][research_c_compiler_2017]
- [Caamaño and Guelton, 2018, Easy Jit compiler assisted library to enable just-in-time compilation in C++ codes][research_caamano_guelton_2018]
- [Cabrera and others, 1992, 3-D Pre-Stack Depth Migration Implementation and Case History][research_cabrera_perkins_1992]
- [Cabrera Arteaga and others, 2019, Scalable comparison of JavaScript V8 bytecode traces][research_cabreraarteaga_monperrus_2019]
- [Caldwell and Chiba, 2017, Reducing calling convention overhead in object-oriented programming on embedded ARM thumb-2 platforms][research_caldwell_chiba_2017]
- [Caliskan and others, 2018, When Coding Style Survives Compilation De-anonymizing Programmers from Executable Binaries][research_caliskan_yamaguchi_2018]
- [Callahan and Koblenz, 1991, Register allocation via hierarchical graph coloring][research_callahan_koblenz_1991]
- [Calzarossa and others, 2001, Performance issues of an HPF-like compiler][research_calzarossa_massari_2001]
- [Cambier and others, 2020, TaskTorrent a Lightweight Distributed Task-Based Runtime System in C++][research_cambier_qian_2020]
- [Cambou, 2017, A XOR data compiler Combined with physical unclonable function for true random number generation][research_cambou_2017]
- [2022, Cameleer A deductive verification tool for OCaml][research_cameleer_a_2022]
- [Campbell, 2019, Random Compiler for Fast Hamiltonian Simulation][research_campbell_2019]
- [Campbell and Beck, 1965, THE FORAST PROGRAMMING LANGUAGE FOR ORDVAC AND BRLESC REVISED][research_campbell_beck_1965]
- [Campos-López and Wannenwetsch, 2016, The PERICLES Process Compiler Linking BPMN Processes into Complex Workflows for Model-Driven Preservation in Evolving Ecosystems][research_camposlopez_wannenwetsch_2016]
- [Canedo and others, 2009, Design and implementation of a queue compiler][research_canedo_abderazek_2009]
- [Carlos Paradis and others, 2025, Towards Streamlining Auditing for Compliance With Requirements in Open-Source Software at NASA][research_carlosparadis_ivanperez_2025]
- [Carlotto and others, 2016, Interoperability of Annotation Schemes Using the Pepper Framework to Display AWA Documents in the ANNIS Interface][research_carlotto_beloki_2016]
- [Carminati and others, 2017, Combining loop unrolling strategies and code predication to reduce the worst-case execution time of real-time software][research_carminati_starke_2017]
- [Carminati and others, 2018, On the use of static branch prediction to reduce the worst-case execution time of real-time applications][research_carminati_starke_2018]
- [CARNEY and LABAUGH, 1983, Efficient compiler implementation for a spaceborne image processing demonstration system][research_carney_labaugh_1983]
- [Carter, 1982, Further analysis of code generation for a single register machine][research_carter_1982]
- [Carvalho and others, 2019, A dataflow runtime environment and static scheduler for edge, fog and in-situ computing][research_carvalho_ferreira_2019]
- [Cassola and others, 2020, A Gradual Type System for Elixir][research_cassola_talagorria_2020]
- [Castagna and others, 2023, The Design Principles of the Elixir Type System][research_castagna_duboc_2023]
- [Castañeda and Rodríguez, 2023, Asynchronous Wait-Free Runtime Verification and Enforcement of Linearizability][research_castaneda_rodriguez_2023]
- [Castañeda and Rodríguez, 2026, Asynchronous Wait-Free Runtime Verification and Enforcement of Linearizability][research_castaneda_rodriguez_2026]
- [Castro-Lopez and Vega-Lopez, 2019, Multi-target Compiler for the Deployment of Machine Learning Models][research_castrolopez_vegalopez_2019]
- [Cattell and others, 1979, Code generation in a machine-independent compiler][research_cattell_newcomer_1979]
- [Cazzola and Olivares, 2015, Gradually Learning Programming Supported by a Growable Programming Language][research_cazzola_olivares_2015]
- [Ceng Giap and Erviana, 2023, Implementation of Face Mask Detection Using Phyton Programming Language][research_cenggiap_erviana_2023]
- [Chaitin, 1982, Register allocation and spilling via graph coloring][research_chaitin_1982]
- [Chaitin, 2004, Register allocation and spilling via graph coloring][research_chaitin_2004]
- [Chaliasos and others, 2022, Finding typing compiler bugs][research_chaliasos_sotiropoulos_2022]
- [Chalin, 2007, A Sound Assertion Semantics for the Dependable Systems Evolution Verifying Compiler][research_chalin_2007]
- [Chalin, 2010, Engineering a Sound Assertion Semantics for the Verifying Compiler][research_chalin_2010]
- [Chaplygin, 2025, Modeling and implementation of Common LISP functional language compiler][research_chaplygin_2025]
- [Charmanas and others, 2026, A topic-oriented trend analysis framework for Stack Exchange questions Case study on ChatGPT related queries on Stack Overflow][research_charmanas_georgiou_2026]
- [Chase, 2005, Session details Register allocation][research_chase_2005]
- [Chatterjee, 2013, Runtime Systems for Extreme Scale Platforms][research_chatterjee_2013]
- [Chaumette and others, 2011, Automated extraction of polymorphic virus signatures using abstract interpretation][research_chaumette_ly_2011]
- [Chavanon and others, 2024, PfComp A Verified Compiler for Packet Filtering Leveraging Binary Decision Diagrams][research_chavanon_besson_2024]
- [Chawla and others, 2024, COMPARATIVE STUDY OF PROPOFOL AUTO-COINDUCTION VERSUS KETAMINE PROPOFOL COINDUCTION USING PRIMING PRINCIPLE BY BISPECTRAL INDEX ANALYSIS FOR DAY CARE SURGERY][research_chawla_goyal_2024]
- [Cheatham and Standish, 1970, Optimization aspects of compiler- compilers][research_cheatham_standish_1970]
- [Chen, 2018, Learning to accelerate compiler testing][research_chen_2018]
- [A survey of compiler testing][research_chen_2020]
- [Chen and others, 2025, De-duplicating Silent Compiler Bugs via Deep Semantic Representation][research_chen_fan_2025]
- [Chen and others, 2007, Design of a Certifying Compiler Supporting Proof of Program Safety][research_chen_ge_2007]
- [Chen and others, 2016, A Process-Visible Compiler Aimed for Teaching Assistant][research_chen_lin_2016]
- [Chen and others, 2022, Register allocation compilation technique for ASIP in 5G micro base stations][research_chen_liu_2022]
- [Chen and others, 2020, Enhanced compiler bug isolation via memoized search][research_chen_ma_2020]
- [Chen and Suo, 2022, Boosting Compiler Testing via Compiler Optimization Exploration][research_chen_suo_2022]
- [Chen and others, 2010, Implementation of Bytecode-based Software Watermarking for Java Programs][research_chen_wang_2010]
- [Chen and others, 2009, Bytecode Generation for XQuery Compiler][research_chen_yuan_2009]
- [Chen and others, 2020, CRAC An automatic assistant compiler of checkpoint/restart for OpenCL program][research_chen_zhang_2020]
- [Chen and others, 2024, Design and Implementation of an Aspect-Oriented C Programming Language][research_chen_zhu_2024]
- [Chen and Zong, 2016, Android App Energy Efficiency The Impact of Language, Runtime, Compiler, and Implementation][research_chen_zong_2016]
- [Cheng, 2023, QA4C An Intelligent Question and Answering System for the C Programming Language Based on Knowledge Graph][research_cheng_2023]
- [Cheng and others, 2016, Formalised EMFTVM bytecode language for sound verification of model transformations][research_cheng_monahan_2016]
- [Cheng and Wu, 2026, Toward Unified Chinese Multi-Dialectal Speech Recognition via Pinyin Intermediate Representation][research_cheng_wu_2026]
- [Cheng and others, 2026, Denotation-based Compositional Compiler Verification][research_cheng_wu_2026_2]
- [Chen Zhao and others, 2009, Automated test program generation for an industrial optimizing compiler][research_chenzhao_yunzhixue_2009]
- [Chernenko and others, 2021, Proving Reflex Program Verification Conditions in Coq Proof Assistant][research_chernenko_anureev_2021]
- [Chhak and others, 2021, Towards formally verified compilation of tag-based policy enforcement][research_chhak_tolmach_2021]
- [Chi, 1994, Compiler Optimization Technique for Data Cache Prefetching Using a Small CAM Array][research_chi_1994]
- [Chi and others, 2009, An Improved Bytecode Verification Algorithm on Java Card][research_chi_li_2009]
- [Chichereau and others, 2024, Fully Integrated Quantum Method for Classical Register Allocation in LLVM][research_chichereau_vialle_2024]
- [Ching, 1986, Program analysis and code generation in an APL/370 compiler][research_ching_1986]
- [Ching and Katz, 1993, The testing of an APL compiler][research_ching_katz_1993]
- [Chirila and Sora, 2024, Java Single vs. Platform vs. Virtual Threads Runtime Performance Assessment in the Context of Key Class Detection][research_chirila_sora_2024]
- [Chlipala, 2010, A verified compiler for an impure functional language][research_chlipala_2010]
- [Chlipala, 2015, Session details Session 4A Compiler Correctness][research_chlipala_2015]
- [Chmiel and Spinolo, 2022, Testing the impact of remote interpreting settings on interpreter experience and performance][research_chmiel_spinolo_2022]
- [Cho, 2016, Semantics for a Quantum Programming Language by Operator Algebras][research_cho_2016]
- [Cho and others, 2022, Sequential reasoning for optimizing compilers under weak memory concurrency][research_cho_lee_2022]
- [Choi and Han, 2006, Optimal register reassignment for register stack overflow minimization][research_choi_han_2006]
- [Choi and Hong, 2019, Design and implementation of virtual machine control and streaming scheme using Linux kernel-based virtual machine hypercall for virtual mobile infrastructure][research_choi_hong_2019]
- [Choi and Jeon, 2026, Stack-based static WebAssembly binary slicing and mutation for generating valid sub-binaries][research_choi_jeon_2026]
- [Choi and others, 2018, Work-in-Progress Lightweight Deadlock Detection Technique for Embedded Systems via OS-Level Analysis][research_choi_kwon_2018]
- [Choi and others, 2024, Accelerating Sensor Software Performance on Edge Devices Through Just-in-Time Compilation][research_choi_park_2024]
- [Choi and others, 2019, Reusable inline caching for JavaScript performance][research_choi_shull_2019]
- [Chong and others, 2017, Programming languages and compiler design for realistic quantum hardware][research_chong_franklin_2017]
- [Christodorescu and Jha, 2006, Static Analysis of Executables to Detect Malicious Patterns][research_christodorescu_jha_2006]
- [Christopher and others, 1984, Using dynamic programming to generate optimized code in a Graham-Glanville style code generator][research_christopher_hatcher_1984]
- [Chudnov and others, 2014, Information Flow Monitoring as Abstract Interpretation for Relational Logic][research_chudnov_kuan_2014]
- [Chung Seo and Kim, 2023, Portable and Efficient Implementation of CRYSTALS-Kyber Based on WebAssembly][research_chungseo_kim_2023]
- [Ciaffaglione, 2016, Towards Turing computability via coinduction][research_ciaffaglione_2016]
- [Ciesko and Roussel, 2023, User-Level Threading for HPC Applications][research_ciesko_roussel_2023]
- [Cieszewski, 2025, PyHLS Intermediate Representation for Versatile High-Level Synthesis][research_cieszewski_2025]
- [C K, 2022, Video Calling With Build-In Compiler][research_ck_2022]
- [CLERC, 2016, OCaml-Java The Java Virtual Machine as the target of an OCaml compiler][research_clerc_2016]
- [Clinger, 1984, The scheme 311 compiler an exercise in denotational semantics][research_clinger_1984]
- [Clopper and Pearson 1934, The use of confidence or fiducial limits illustrated in the case of the binomial][research_clopper_pearson_1934]
- [Coglio, 2003, Improving the official specification of Java bytecode verification][research_coglio_2003]
- [Coglio, 2004, Simple verification technique for complex Java bytecode subroutines][research_coglio_2004]
- [Colin and Puaut, 2000, Worst Case Execution Time Analysis for a Processor with Branch Prediction][research_colin_puaut_2000]
- [Colombet and others, 2011, Graph-coloring and treescan register allocation using repairing][research_colombet_boissinot_2011]
- [Colvin and Hayes, 2011, Structural operational semantics through context-dependent behaviour][research_colvin_hayes_2011]
- [2016, Comparative Study of Virtual Machine Migration Techniques and Challenges in Post Copy Live Virtual Machine Migration][research_comparative_study_2016]
- [1998, Compiler technology Tools, translators and language implementation][research_compiler_technology_1998]
- [Cong and Asai, 2023, Towards a Reflection for Effect Handlers][research_cong_asai_2023]
- [Consel and Cheng Khoo, 1993, Semantics-directed generation of a prolog compiler][research_consel_chengkhoo_1993]
- [Design of a separable transition-diagram compiler][research_conway_1963]
- [Coppo and Ferrari, 1993, Type inference, abstract interpretation and strictness analysis][research_coppo_ferrari_1993]
- [Cordes and others, 2009, A Fast and Precise Static Loop Analysis Based on Abstract Interpretation, Program Slicing and Polytope Models][research_cordes_falk_2009]
- [Correnson and Finkbeiner, 2025, Coinductive Proofs for Temporal Hyperliveness][research_correnson_finkbeiner_2025]
- [Corrias and others, 2026, An Analysis of Modern Web Security Vulnerabilities Inside WebAssembly Applications][research_corrias_pisu_2026]
- [Corrodi and others, 2018, A semantics comparison workbench for a concurrent, asynchronous, distributed programming language][research_corrodi_heussner_2018]
- [Cortesi, 2008, Widening Operators for Abstract Interpretation][research_cortesi_2008]
- [Cortesi and Filé, 1991, Abstract interpretation of logic programs][research_cortesi_file_1991]
- [Cortesi and others, 1997, Complementation in abstract interpretation][research_cortesi_file_1997]
- [Corti and Gross, 2004, Approximation of the worst-case execution time using structural analysis][research_corti_gross_2004]
- [Costa and others, 2021, Use of Measurements in Worst-Case Execution Time Estimation for Real-Time Systems][research_costa_deoliveira_2021]
- [Costagliola and others, 2007, Visual language implementation through standard compiler-compiler techniques][research_costagliola_deufemia_2007]
- [Couch and Hamm, 1977, Semantic Structures for Efficient Code Generation on a Stack Machine][research_couch_hamm_1977]
- [Cousot and Cousot 1977, Abstract interpretation][research_cousot_1977]
- [Cousot, 1996, Program analysis][research_cousot_1996]
- [Cousot, 1997, Program analysis][research_cousot_1997]
- [Cousot, 2015, On Various Abstract Understandings of Abstract Interpretation][research_cousot_2015]
- [Cousot, 2015, Verification by abstract interpretation, soundness and abstract induction][research_cousot_2015_2]
- [Cousot and Cousot, 1995, Formal language, grammar and set-constraint-based program analysis by abstract interpretation][research_cousot_cousot_1995]
- [Cousot and Cousot, 2000, Temporal abstract interpretation][research_cousot_cousot_2000]
- [Cousot and Cousot, 2001, A Case Study in Abstract Interpretation Based Program Transformation][research_cousot_cousot_2001]
- [Cousot and Cousot, 2002, Systematic design of program transformation frameworks by abstract interpretation][research_cousot_cousot_2002]
- [Cousot and Cousot, 2011, Grammar semantics, analysis and parsing by abstract interpretation][research_cousot_cousot_2011]
- [Cousot and Cousot, 2012, An abstract interpretation framework for termination][research_cousot_cousot_2012]
- [Cousot and Cousot, 2014, A galois connection calculus for abstract interpretation][research_cousot_cousot_2014]
- [Cowan and Graham, 1970, Design characteristics of the WATFOR compiler][research_cowan_graham_1970]
- [Coward and others, 2023, Combining E-Graphs with Abstract Interpretation][research_coward_constantinides_2023]
- [C. Robinson and others, 1994, Prospect definition by pre-stack depth migration of a grid of seismic lines - A case history][research_crobinson_ptung_1994]
- [Cruttwell and others, 2021, Categorical semantics of a simple differential programming language][research_cruttwell_gallagher_2021]
- [Cummins and others, 2018, Compiler fuzzing through deep learning][research_cummins_petoumenos_2018]
- [Cummins and others, 2025, LLM Compiler Foundation Language Models for Compiler Optimization][research_cummins_seeker_2025]
- [Cunha and others, 2024, Trading Runtime for Energy Efficiency Leveraging Power Caps to Save Energy across Programming Languages][research_cunha_silva_2024]
- [Curry, 2023, An HPC-Oriented Runtime Environment for Enabling Computational Storage][research_curry_2023]
- [Curtis and others, 2018, A compiler for cyber-physical digital microfluidic biochips][research_curtis_grissom_2018]
- [Czajka, 2020, A new coinductive confluence proof for infinitary lambda calculus][research_czajka_2020]
- [Czajka, 2020, An operational interpretation of coinductive types][research_czajka_2020_2]
- [Dagnino, 2020, Coaxioms flexible coinductive definitions by inference systems][research_dagnino_2020]
- [Dagnino, 2021, Foundations of regular coinduction][research_dagnino_2021]
- [Daiß and others, 2023, Stellar Mergers with HPX-Kokkos and SYCL Methods of using an Asynchronous Many-Task Runtime System with SYCL][research_daiss_diehl_2023]
- [Dakkak and others, 2020, The design and implementation of the wolfram language compiler][research_dakkak_wickhamjones_2020]
- [Dalla Preda and Giacobazzi, 2005, Control code obfuscation by abstract interpretation][research_dallapreda_giacobazzi_2005]
- [Dams and others, 1997, Abstract interpretation of reactive systems][research_dams_gerth_1997]
- [Dange and others, 2023, Implementation on A User Authentication Scheme Using Block Chain-Enabled Fog Nodes][research_dange_mundre_2023]
- [Abstracting control][research_danvy_filinski_1990]
- [Defunctionalization at work][research_danvy_nielsen_2001]
- [Das and others, 2020, Deep Learning-based Approximate Graph-Coloring Algorithm for Register Allocation][research_das_ahmad_2020]
- [Dasgupta and others, 2019, A complete formal semantics of x86-64 user-level instruction set architecture][research_dasgupta_park_2019]
- [Dave and others, 2016, A 1V 800MHz 140Kb register file compiler using variation aware self-timing in 40nm bulk CMOS][research_dave_dikshit_2016]
- [Davenport, 1995, Object-Oriented Visual Programming Language. Phase 1][research_davenport_1995]
- [De and others, 2021, Canonical proof-objects for coinductive programming infinets with infinitely many cuts][research_de_pellissier_2021]
- [Debenham and Westlake, 2014, Pre-stack depth migration for improved imaging under seafloor canyons 2D case study of Browse Basin, AustraliaFN1][research_debenham_westlake_2014]
- [De Blaere and others, 2021, A Compiler Extension to Protect Embedded Systems Against Data Flow Errors][research_deblaere_verstappe_2021]
- [Debnath and others, 2024, ARMOR A Formally Verified Implementation of X.509 Certificate Chain Validation][research_debnath_jenkins_2024]
- [De Bosschere and Tarau, 1994, High performance continuation passing style Prolog-to-C mapping][research_debosschere_tarau_1994]
- [Debray, 1995, Abstract interpretation and low-level code optimization][research_debray_1995]
- [DeBuhr and others, 2017, Scalable Hierarchical Multipole Methods Using an Asynchronous Many-Tasking Runtime System][research_debuhr_zhang_2017]
- [de Ferrière and others, 2026, SecSwift, a Compiler-Based Framework for Software Countermeasures in Cybersecurity][research_deferriere_janin_2026]
- [De Francesco and others, 2010, Using abstract interpretation to add type checking for interfaces in Java bytecode verification][research_defrancesco_lettieri_2010]
- [Dejtrakulwong and others, 2013, Sensitivity analysis and cascaded interpretation scheme for subtle seismic signatures in thin shaly-sand reservoirs][research_dejtrakulwong_mavko_2013]
- [Delaët and others, 2025, Abstract machines and small-step semantics a winning ticket for proof automation?][research_delaet_blazy_2025]
- [Delgado-Pérez and Segura, 2019, Study of trivial compiler equivalence on C++ object-oriented mutation operators][research_delgadoperez_segura_2019]
- [De Luca and Chen, 2017, Visual IoT/Robotics Programming Language in Pi-Calculus][research_deluca_chen_2017]
- [del Vado Vírseda, 2021, Learning Compiler Design From the Implementation to Theory][research_delvadovirseda_2021]
- [DelVado Vírseda, 2023, Visualizing Compiler Design Theory from Implementation Through an Interactive Tutoring Tool Experiences and Results][research_delvadovirseda_2023]
- [De Macedo and others, 2021, On the Runtime and Energy Performance of WebAssembly Is WebAssembly superior to JavaScript yet?][research_demacedo_abreu_2021]
- [De Macedo and others, 2022, WebAssembly versus JavaScript Energy and Runtime Performance][research_demacedo_abreu_2022]
- [Demmler and others, 2021, Improved Circuit Compilation for Hybrid MPC via Compiler Intermediate Representation][research_demmler_katzenbeisser_2021]
- [Revisiting coroutines][research_demoura_2009]
- [Deng and others, 2026, Design and Implementation of an OCaml-Based Standalone SystemVerilog Preprocessor Compliant with IEEE 1800-2023][research_deng_he_2026]
- [Deng and Namjoshi, 2018, Securing a compiler transformation][research_deng_namjoshi_2018]
- [Denis and others, 2023, Tracing task-based runtime systems Feedbacks from the StarPU case][research_denis_jeannot_2023]
- [de Niz, 2007, Diagrams and Languages for Model-Based Software Engineering of Embedded Systems UML and AADL][research_deniz_2007]
- [Denney and Fischer, 2005, Formal Safety Certification of Aerospace Software][research_denneyewen_fischerbernd_2005]
- [Denney and Fischer, 2009, Generating Code Review Documentation for Auto-Generated Mission-Critical Software][research_denneyewen_fischerbernd_2009]
- [Denzler and others, 2021, Experiences from Adjusting Industrial Software for Worst-Case Execution Time Analysis][research_denzler_fruhwirth_2021]
- [De Paula and Ierusalimschy, 2022, A Foreign Function Interface for Pallene][research_depaula_ierusalimschy_2022]
- [Derakhshan and others, 2023, Towards End-to-End Verified TEEs via Verified Interface Conformance and Certified Compilers][research_derakhshan_zhang_2023]
- [Deransart, 1979, Proof by semantic attributes of a LISP compiler][research_deransart_1979]
- [Desai, 2009, A Novel Technique for Orchestration of Compiler Optimization Functions Using Branch and Bound Strategy][research_desai_2009]
- [Deutsch, 1995, Semantic models and abstract interpretation techniques for inductive data structures and pointers][research_deutsch_1995]
- [2023, Development of a mobile robot control system in the Python programming language using Raspberry Pi][research_development_of_2023]
- [de Vilhena and Pottier, 2021, A separation logic for effect handlers][research_devilhena_pottier_2021]
- [DeVries and others, 2009, ActionScript bytecode verification with co-logic programming][research_devries_gupta_2009]
- [DeVries and others, 2009, ActionScript bytecode verification with co-logic programming abstract only][research_devries_gupta_2009_2]
- [de Werra and others, 1999, On a graph-theoretical model for cyclic register allocation][research_dewerra_eisenbeis_1999]
- [Diamantopoulos and others, 2020, Agile Autotuning of a Transprecision Tensor Accelerator Overlay for TVM Compiler Stack][research_diamantopoulos_ringlein_2020]
- [Dickerson and others, 2026, Practical Python FPGA Acceleration with Fast Just-In-Time Compilation and Configuration][research_dickerson_srinivasan_2026]
- [Dico and Tata Sutabri, 2025, Virtual Desktop Infrastructure Sebagai Pendukung Perkuliahan Dengan Algoritma Virtual Machine][research_dico_tatasutabri_2025]
- [Diehl and others, 2021, Performance Measurements Within Asynchronous Task-Based Runtime Systems A Double White Dwarf Merger as an Application][research_diehl_marcello_2021]
- [Di Lavore and others, 2025, Coinductive Streams in Monoidal Categories][research_dilavore_defelice_2025]
- [Dimovski, 2021, Lifted termination analysis by abstract interpretation and its applications][research_dimovski_2021]
- [Dimovski, 2025, Imperative Program Synthesis by Abstract Static Analysis and SMT Mutations][research_dimovski_2025]
- [Ding and others, 2022, CARL Compiler Assigned Reference Leasing][research_ding_chen_2022]
- [Ding and others, 2025, HFF-JIT A Hybrid Fuzzing Framework for JIT Compiler Vulnerability Detection in JavaScript][research_ding_li_2025]
- [Ding and Zhang, 2010, Loop-Based Instruction Prefetching to Reduce the Worst-Case Execution Time][research_ding_zhang_2010]
- [Dinikeev, 2025, Type system for a statically typed concatenative programming language with first class function support][research_dinikeev_2025]
- [Di Pierro and others, 2008, Relational Analysis and Precision via Probabilistic Abstract Interpretation][research_dipierro_sotin_2008]
- [Dissegna and others, 2016, An Abstract Interpretation-Based Model of Tracing Just-in-Time Compilation][research_dissegna_logozzo_2016]
- [Ditu, 2015, Model-Based Function Call Code Generation and Stack Management in Retargetable Compilers Application Binary Interface Modeling of Stack Layout and Function Call Sequence][research_ditu_2015]
- [Dixon, 1982, A Pascal compiler testing facility][research_dixon_1982]
- [Djalali and others, 2025, The Evolution of Software Usability in Developer Communities An Empirical Study on Stack Overflow][research_djalali_aljedaani_2025]
- [Dobravec, 2018, JAVA BYTECODE INSTRUCTION USAGE COUNTING WITH ALGATOR][research_dobravec_2018]
- [Dold and others, 2003, A Completely Verified Realistic Bootstrap Compiler][research_dold_henke_2003]
- [Domagała and others, 2016, Register allocation and promotion through combined instruction scheduling and loop unrolling][research_domagala_vanamstel_2016]
- [Donaldson and others, 2023, Industrial Deployment of Compiler Fuzzing Techniques for Two GPU Shading Languages][research_donaldson_clayton_2023]
- [Donaldson and others, 2024, Randomised Testing of the Compiler for a Verification-Aware Programming Language][research_donaldson_sheth_2024]
- [Donegan and others, 1979, A code generator generator language][research_donegan_noonan_1979]
- [Dong, 2013, Design and Implementation of Compiler Subsystem for Object Oriented Publish/Subscribe Systems][research_dong_2013]
- [Dong, 2015, RSTVL A Sound Abstract Memory Model for Program Static Analysis][research_dong_2015]
- [Dong, 2018, A sound abstract memory model for static analysis of C programs][research_dong_2018]
- [DONG and others, 2011, Logic System for Bytecode Program Modular Certification][research_dong_wang_2011]
- [Dong and others, 2026, Presynthesis Towards Scaling Up Program Synthesis with Finer-Grained Abstract Semantics][research_dong_wu_2026]
- [Donohoe, 1987, A Survey of Real-Time Performance Benchmarks for the Ada Programming Language][research_donohoe_1987]
- [Doronin, 2019, PROBLEM RESEARCH AND DEVELOPMENT OF A TOOL FOR CHECKING APPLICATION BINARY INTERFACE COMPATIBILITY OF VIRTUAL METHOD TABLES][research_doronin_2019]
- [DOWNEN and ARIOLA, 2014, Delimited control and computational effects][research_downen_ariola_2014]
- [DOWNEN and ARIOLA, 2025, A contextual formalization of structural coinduction][research_downen_ariola_2025]
- [Downen and others, 2016, Sequent calculus as a compiler intermediate language][research_downen_maurer_2016]
- [Drechsler and Schnieber, 2023, Automated Polynomial Formal Verification Human-Readable Proof Generation][research_drechsler_schnieber_2023]
- [Drescher and Engelke, 2024, Fast Template-Based Code Generation for MLIR][research_drescher_engelke_2024]
- [D'Silva and others, 2015, The Correctness-Security Gap in Compiler Optimization][research_dsilva_payer_2015]
- [Du, 2026, Performance Verification of BFS For Unweighted Maze Solving A Comparative Analysis with DFS and A* Via Ocaml Implementation][research_du_2026]
- [Dubach and others, 2007, Fast compiler optimisation evaluation using code-feature based performance prediction][research_dubach_cavazos_2007]
- [Duhamel and Pillement, 2024, Runtime Task Scheduling for FPGA-Based Embedded Systems Using Just-in-Time Bitstream Prefetching][research_duhamel_pillement_2024]
- [Duhoux and others, 2019, Implementation of a Feature-Based Context-Oriented Programming Language][research_duhoux_mens_2019]
- [Duţu and others, 2026, From Runtime Reflection to Compile-Time Specialization A Template-Based Approach to Runtime Libraries][research_dutu_guiman_2026]
- [A monadic framework for delimited continuations][research_dybvig_2007]
- [E., 2020, Modified Support Vector Machine based Efficient Virtual Machine Consolidation Procedure for Cloud Data Centers][research_e_2020]
- [Eachempati and others, 2010, An open-source compiler and runtime implementation for Coarray Fortran][research_eachempati_jun_2010]
- [Edalat and Pattinson, 2007, Denotational semantics of hybrid automata][research_edalat_pattinson_2007]
- [Толстікова and others, 2016, Efficiency asynchronous application programming language Python][research_efficiency_asynchronous_application_2016]
- [2015, Efficient Implementation of Class Based Decomposition Schemes for Naive Bayes Classifier][research_efficient_implementation_2015]
- [Efthymiou and others, 2022, Quantum simulation with just-in-time compilation][research_efthymiou_lazzarin_2022]
- [Egreteau and Thierry, 2005, Attenuating the Effects of Pre-Stack Depth Migration for AVA Analysis][research_egreteau_thierry_2005]
- [Eichenberger and Davidson, 1995, Register allocation for predicated code][research_eichenberger_davidson_1995]
- [Eisl, 2015, Trace register allocation][research_eisl_2015]
- [Eisl and others, 2016, Trace-based Register Allocation in a JIT Compiler][research_eisl_grimmer_2016]
- [Eisl and others, 2018, Parallel trace register allocation][research_eisl_leopoldseder_2018]
- [ELECTRONIC SYSTEMS DIV HANSCOM AFB MA, 1970, USER'S MANUAL JOVIAL COMPILER VALIDATION SYSTEM][research_electronicsystemsdivhanscomafbma_1970]
- [Kotlin coroutines: design and implementation][research_elizarov_2021]
- [Elkhouly and others, 2019, Compiler-support for Critical Data Persistence in NVM][research_elkhouly_alshboul_2019]
- [Elof Frank, 1995, Constrained Register Allocation in Bus Architectures][research_eloffrank_1995]
- [Emerson, 2020, Autoencoding Pixies Amortised Variational Inference with Graph Convolutions for Functional Distributional Semantics][research_emerson_2020]
- [Endo and others, 2017, On the Interactions Between Value Prediction and Compiler Optimizations in the Context of EOLE][research_endo_perais_2017]
- [Engblom and others, 2003, Worst-case execution-time analysis for embedded real-time systems][research_engblom_ermedahl_2003]
- [Engelke and Schwarz, 2024, Compile-Time Analysis of Compiler Frameworks for Query Compilation][research_engelke_schwarz_2024]
- [Engelke and Weidendorfer, 2017, Using LLVM for Optimized Lightweight Binary Re-Writing at Runtime][research_engelke_weidendorfer_2017]
- [Enrici and others, 2019, Efficient Data-Flow Analysis of UML/SysML Diagrams for Optimized Model Compilation of Hardware-software Systems][research_enrici_apvrille_2019]
- [Ermedahl and others, 2009, Deriving the Worst-Case Execution Time Input Values][research_ermedahl_fredriksson_2009]
- [Ermedahl and Puschner, 2011, Preface to the special issue on worst-case execution-time analysis][research_ermedahl_puschner_2011]
- [Ermedahl and others, 2003, Clustered calculation of worst-case execution times][research_ermedahl_stappert_2003]
- [Ertl, 1995, Stack caching for interpreters][research_ertl_1995]
- [Evans and others, 1978, A Compiler Compiler and Methodology for Problem Oriented Language Compiler Implementors][research_evans_lockington_1978]
- [Evansi and Sulaiman, 1996, Solving optimisation problems using neucomp-a neural network compiler][research_evansi_sulaiman_1996]
- [Facchinetti and others, 2019, Higher-order Demand-driven Program Analysis][research_facchinetti_palmer_2019]
- [Falis, 1982, Design and implementation in Ada of a runtime task supervisor][research_falis_1982]
- [Falk, 2009, WCET-aware register allocation based on graph coloring][research_falk_2009]
- [Falk and Lokuciejewski, 2010, A compiler framework for the reduction of worst-case execution times][research_falk_lokuciejewski_2010]
- [Falk and Lokuciejewski, 2019, Correction to A compiler framework for the reduction of worst-case execution times][research_falk_lokuciejewski_2019]
- [Fan and others, 2025, Adaptive random compiler for Hamiltonian simulation][research_fan_wu_2025]
- [Fan and others, 2024, History-driven Compiler Fuzzing via Assembling and Scheduling Bug-triggering Code Segments][research_fan_ye_2024]
- [Fang and others, 2026, LLM-VeriOpt Verification-Guided Reinforcement Learning for LLM-Based Compiler Optimization][research_fang_kang_2026]
- [Farkas and others, 2021, Improving productivity in large scale testing at the compiler level by changing the intermediate language from C++ to Java][research_farkas_szabados_2021]
- [Fayzrakhmanov, 2022, Introducing Programming Language Metrics][research_fayzrakhmanov_2022]
- [Fedasyuk and others, 2017, Architecture of a tool for automated testing the worst-case execution time of real-time embedded systems' firmware][research_fedasyuk_chopey_2017]
- [Feitosa and Ribeiro, 2024, Differential Testing using Random Well-Typed Haskell Programs][research_feitosa_ribeiro_2024]
- [Feitosa and others, 2019, A monadic semantics for quantum computing in an object oriented language][research_feitosa_vizzotto_2019]
- [Feldman, 1966, A formal semantics for computer languages and its application in a compiler-compiler][research_feldman_1966]
- [Feldman, 1979, Implementation of a portable Fortran 77 compiler using modern tools][research_feldman_1979]
- [Felker, 2020, Design of Cyanobyte An Intermediate Representation to Standardize Digital Peripheral Datasheets for Automatic Code Generation][research_felker_2020]
- [The theory and practice of first-class prompts][research_felleisen_1988]
- [Feng and others, 2025, Finding Compiler Bugs through Cross-Language Code Generator and Differential Testing][research_feng_ma_2025]
- [Ferdinand and Heckmann, 2008, Worst-Case Execution Time - A Tool Provider's Perspective][research_ferdinand_heckmann_2008]
- [Feret and others, 2007, Reachability Analysis of Biological Signalling Pathways by Abstract Interpretation][research_feret_simos_2007]
- [Ferrante and Allard, 1996, Introducing a CPS style optimizer into an existing compiler][research_ferrante_allard_1996]
- [2005, Fifth IEEE International Workshop on Source Code Analysis and Manipulation][research_fifth_ieee_2005]
- [Finkel and others, 2019, ClangJIT Enhancing C++ with Just-in-Time Compilation][research_finkel_poliakoff_2019]
- [Finkelstein, 1968, A compiler optimization technique][research_finkelstein_1968]
- [Fisher, 1976, A Common Programming Language for the Department of Defense--Background and Technical Requirements][research_fisher_1976]
- [Adding delimited and composable control to a production programming environment][research_flatt_2007]
- [Flatt and Dybvig, 2020, Compiler and runtime support for continuation marks][research_flatt_dybvig_2020]
- [Fonseca and others, 2017, An Empirical Study on the Correctness of Formally Verified Distributed Systems][research_fonseca_zhang_2017]
- [1995, Formal Methods Specification and Analysis Guidebook for the Verification of Software and Computer Systems A Practitioner's Companion - Volume 2][research_formal_methods_1995]
- [1995, Formal Methods Specification and Verification Guidebook for Software and Computer Systems Planning and Technology Insertion - Volume 1][research_formal_methods_1995_2]
- [FORSTER and others, 2019, On the expressive power of user-defined effects Effect handlers, monadic reflection, delimited control][research_forster_kammar_2019]
- [2004, Fourth IEEE International Workshop on Source Code Analysis and Manipulation][research_fourth_ieee_2004]
- [Fox and others, 2017, Verified compilation of CakeML to multiple machine-code targets][research_fox_myreen_2017]
- [Fradet and others, 2018, A Generic Coq Proof of Typical Worst-Case Analysis][research_fradet_lesourd_2018]
- [Francalanza and Tabone, 2023, ElixirST A session-based type system for Elixir modules][research_francalanza_tabone_2023]
- [Fraser and Wendt, 1986, Integrating code generation and optimization][research_fraser_wendt_1986]
- [Frąszczak and Frąszczak, 2026, PhishingWebCollector Async python library for automated phishing feed collection][research_fraszczak_fraszczak_2026]
- [Freier and Jian-Jia Chen, 2013, Prioritization for real-time embedded systems on dual-core platforms by exploiting the typical- and worst-case execution times][research_freier_jianjiachen_2013]
- [Frenkel and others, 2011, Towards a Modular and Accessible Modelica Compiler Backend][research_frenkel_kunze_2011]
- [Freund and Mitchell, 1998, A type system for object initialization in the Java bytecode language][research_freund_mitchell_1998]
- [Freund and Mitchell, 1998, A Type System for Object Initialization In the Java Bytecode Language summary][research_freund_mitchell_1998_2]
- [Freund and Mitchell, 1999, A type system for object initialization in the Java bytecode language][research_freund_mitchell_1999]
- [Freund and Mitchell, 2003, A Type System for the Java Bytecode Language and Verifier][research_freund_mitchell_2003]
- [Fried and others, 2023, Register Allocation for Compressed ISAs in LLVM][research_fried_stemmergrabow_2023]
- [Friers and others, 2021, Amortised Encoding for Large High-Resolution Displays][research_friers_becher_2021]
- [Friese and others, 2024, Lamellar A Rust-based Asynchronous Tasking and PGAS Runtime for High Performance Computing][research_friese_gioiosa_2024]
- [Frigo, 1999, A fast Fourier transform compiler][research_frigo_1999]
- [Fruehwirth, 2025, Runtime Repeated Recursion Unfolding in CHR A Just-In-Time Online Program Optimization Strategy That Can Achieve Super-Linear Speedup][research_fruehwirth_2025]
- [Fumero and Kotselidis, 2018, Using compiler snippets to exploit parallelism on heterogeneous hardware a Java reduction case study][research_fumero_kotselidis_2018]
- [Fumero and others, 2017, Just-In-Time GPU Compilation for Interpreted Languages with Partial Evaluation][research_fumero_steuwer_2017]
- [Fusaoka and Hirayama, 1982, Compiler chip][research_fusaoka_hirayama_1982]
- [Fusi and others, 2020, On the Use of Probabilistic Worst-Case Execution Time Estimation for Parallel Applications in High Performance Systems][research_fusi_mazzocchetti_2020]
- [Gaál, 1993, Parallel compiler generation][research_gaal_1993]
- [Gaißert and others, 2025, Tracing Just-in-Time Compilation for Effects and Handlers][research_gaissert_bolztereick_2025]
- [Gal and others, 2005, Integrated Java Bytecode Verification][research_gal_probst_2005]
- [Gal and others, 2008, Java bytecode verification via static single assignment form][research_gal_probst_2008]
- [Gallaher, 1982, Investigate Capability of Ada Higher Order Programming Language for Developing Machine Independent Software][research_gallaher_1982]
- [Galloway and others, 2015, Performance Metrics of Virtual Machine Live Migration][research_galloway_loewen_2015]
- [Gan and Li, 2015, Coinduction functor in representation stability theory][research_gan_li_2015]
- [Ganzinger and others, 1982, A truly generative semantics-directed compiler generator][research_ganzinger_giegerich_1982]
- [Ganzinger and others, 1976, MUG1 - an incremental compiler-compiler][research_ganzinger_ripken_1976]
- [Gao and others, 2014, A Method of Binary Code Variable Interval Analysis Based on Abstract Interpretation][research_gao_li_2014]
- [Gao and Parreaux, 2025, A Lightweight Type-and-Effect System for Invalidation Safety Tracking Permanent and Temporary Invalidation with Constraint-Based Subtype Inference][research_gao_parreaux_2025]
- [Gao and Shi, 2005, An improved approach of register allocation via graph coloring][research_gao_shi_2005]
- [Gao and others, 2025, Clozemaster Fuzzing Rust Compiler by Harnessing Llms for Infilling Masked Real Programs][research_gao_yang_2025]
- [Garcia and others, 2009, Lazy evaluation and delimited control][research_garcia_lumsdaine_2009]
- [Garcia and others, 2010, Lazy Evaluation and Delimited Control][research_garcia_lumsdaine_2010]
- [Gaudet and Stoodley, 2016, Rebuilding an airliner in flight a retrospective on refactoring IBM testarossa production compiler for Eclipse OMR][research_gaudet_stoodley_2016]
- [Geeson and Smith, 2024, Compiler Testing with Relaxed Memory Models][research_geeson_smith_2024]
- [Genaim and Zanardini, 2013, Reachability-based acyclicity analysis by Abstract Interpretation][research_genaim_zanardini_2013]
- [Geng and others, 2021, Verification of Open-Source Memory Compiler Framework with a Practical PDK][research_geng_ishikawa_2021]
- [Georgakoudis and others, 2025, Proteus Portable Runtime Optimization of GPU Kernel Execution with Just-in-Time Compilation][research_georgakoudis_parasyris_2025]
- [Georgescu and others, 2024, Evolutionary Generative Fuzzing for Differential Testing of the Kotlin Compiler][research_georgescu_olsthoorn_2024]
- [Georgiou and others, 2020, Lost In Translation Exposing Hidden Compiler Optimization Opportunities][research_georgiou_chamski_2020]
- [Gerasimov, 2018, Directed Dynamic Symbolic Execution for Static Analysis Warnings Confirmation][research_gerasimov_2018]
- [Ghadesi and others, 2024, What causes exceptions in machine learning applications? Mining machine learning-related stack traces on Stack Overflow][research_ghadesi_lamothe_2024]
- [Ghica and Alyahya, 2017, On the Learnability of Programming Language Semantics][research_ghica_alyahya_2017]
- [Ghica and others, 2022, High-level effect handlers in C++][research_ghica_lindley_2022]
- [Ghica and Tapus, 2015, Optimized retargetable compiler for embedded processors - GCC vs LLVM][research_ghica_tapus_2015]
- [Ghorbani and Babamir, 2019, Runtime deadlock tracking and prevention of concurrent multithreaded programs A learning-based approach][research_ghorbani_babamir_2019]
- [Ghosh and others, 2020, Compiler compatible 5.66 Mb/mm2 8T 1R1W register file in 14 nm FinFET technology][research_ghosh_bhattacharya_2020]
- [Ghosh and Kulatilake, 1987, A FORTRAN program for generation of multivariate normally distributed random variables][research_ghosh_kulatilake_1987]
- [Ghuzdewan, 2025, Development of a Python-Based Program for Pareto Analysis in Construction Project Cost Management][research_ghuzdewan_2025]
- [Giacobazzi, 2008, Abstract Interpretation in Code Security][research_giacobazzi_2008]
- [Gibbons, 2021, Continuation-Passing Style, Defunctionalization, Accumulations, and Associativity][research_gibbons_2021]
- [Gifford and others, 1992, Report on the FX-91 Programming Language][research_gifford_jouvelot_1992]
- [Gillard and others, 2026, Dynamic Wind for OCaml Effect Handlers with Escaping Continuation Support][research_gillard_yamazaki_2026]
- [Ginsbach and others, 2018, CAnDL a domain specific language for compiler analysis][research_ginsbach_crawford_2018]
- [Giorgi and Le Métayer, 1990, Continuation-based parallel implementation of functional programming languages][research_giorgi_lemetayer_1990]
- [Girault, 2025, Toward a Formally Verified Compiler for a Synchronous, Functional, Data-Flow Programming Language][research_girault_2025]
- [Godboley and others, 2022, AV-AFL A Vulnerability Detection Fuzzing Approach by Proving Non-reachable Vulnerabilities using Sound Static Analyser][research_godboley_gupta_2022]
- [Goldberg, 1998, A specification of Java loading and bytecode verification][research_goldberg_1998]
- [Gómez-Déniz and others, 2016, Random Tests Combining Mathematica Package and Latex Compiler][research_gomezdeniz_davilacardenes_2016]
- [Goncharov and others, 2018, Unguarded Recursion on Coinductive Resumptions][research_goncharov_schroder_2018]
- [Goodenough and others, 1976, Evaluation of ALGOL 68, JOVIAL J3B, PASCAL, SIMULA 67, and TACPOL vs. TINMAN Requirements for a Common High Order Programming Language][research_goodenough_mcgowan_1976]
- [Goos, 2002, Compiler Verification and Compiler Architecture][research_goos_2002]
- [Gordon and others, 2022, Porting the Kitten Lightweight Kernel Operating System to RISC-V][research_gordon_pedretti_2022]
- [Gordon and Scholz, 2015, Dynamic adaptation of functional runtime systems through external control][research_gordon_scholz_2015]
- [Gore and others, 2023, Sentence Generator for English Language using Formal Semantics][research_gore_bajaj_2023]
- [Gorelik and Khukhlaev, 1975, Implementation of the incremental fortran compiler][research_gorelik_khukhlaev_1975]
- [Gorodetskiy, 2019, NEXTGEN PROGRAMMING LANGUAGE WITH PROGRAMMABLE SEMANTICS][research_gorodetskiy_2019]
- [Gorringe and Jain, 2013, Architectural considerations for implementation of the ATML standards in an open systems architecture runtime environment OSA-RTS using a graphical environment][research_gorringe_jain_2013]
- [Gotti and Mbarki, 2016, Java Swing Modernization Approach - Complete Abstract Representation based on Static and Dynamic Analysis][research_gotti_mbarki_2016]
- [Gourdin, 2023, Lazy Code Transformations in a Formally Verified Compiler][research_gourdin_2023]
- [Grabmayer, 2023, A Coinductive Reformulation of Milner's Proof System for Regular Expressions Modulo Bisimilarity][research_grabmayer_2023]
- [Grabowski, 2025, Encoding Triangular Norms on Bounded Trellises with Mizar Proof Assistant][research_grabowski_2025]
- [Graham, 1995, Information Technology. Programming Language. The SQL Ada Module Description Language SAMeDL][research_graham_1995]
- [Grechanik, 2012, Random benchmark application generation for evaluating program analysis and testing tools][research_grechanik_2012]
- [2023, Green Supply Chain Management and Competitive Advantage Evidence of Just-in-time Management on Firm Performance SMEs in Indonesia][research_green_supply_2023]
- [GREEN and WOOD, 2024, REASONING ABOUT THE ACOUSTIC REALISATION OF SEMIVOWELS USING AN INTERMEDIATE REPRESENTATION - THE 'SPEECH SKETCH'][research_green_wood_2024]
- [Groce and others, 2022, Making no-fuss compiler fuzzing effective][research_groce_vantonder_2022]
- [Groenewegen and others, 2020, Evolution of the WebDSL runtime reliability engineering of the WebDSL web programming language][research_groenewegen_chastelet_2020]
- [Grolaux and others, 2026, Async/await is an Effective Paradigm for Event Management of User Interfaces][research_grolaux_nguyen_2026]
- [Groß and others, 2023, FUZZILLI Fuzzing for JavaScript JIT Compiler Vulnerabilities][research_gross_koch_2023]
- [Grover, 1985, Guidelines for a Minimal Ada Runtime Environment][research_grover_1985]
- [Gruetter and others, 2024, Live Verification in an Interactive Proof Assistant][research_gruetter_fukala_2024]
- [Gruner and others, 2025, Finding Information Leaks with Information Flow Fuzzing][research_gruner_brust_2025]
- [Gruner and others, 2025, Finding Information Leaks with Information Flow Fuzzing-RCR Report][research_gruner_brust_2025_2]
- [Gu, 2023, LLM-Based Code Generation Method for Golang Compiler Testing][research_gu_2023]
- [Guan and others, 2019, Wootz a compiler-based framework for fast CNN pruning via composability][research_guan_shen_2019]
- [Guan and Treude, 2024, Enhancing Source Code Representations for Deep Learning with Static Analysis][research_guan_treude_2024]
- [Guarna and Jr, 1987, VPC - A Proposal for a Vector Parallel C Programming Language][research_guarna_jr_1987]
- [Guerrera and others, 2019, Reproducible stencil compiler benchmarks using prova!][research_guerrera_maffia_2019]
- [Guerrini and Masini, 2009, Proofs, tests and continuation passing style][research_guerrini_masini_2009]
- [Guessarian, 1979, Program transformations and algebraic semantics][research_guessarian_1979]
- [Gunadi, 2015, Formal Certification of Non-interferent Android Bytecode DEX Bytecode][research_gunadi_2015]
- [Gundersen and others, 2013, Atomic Lambda Calculus A Typed Lambda-Calculus with Explicit Sharing][research_gundersen_heijltjes_2013]
- [Guo and others, 2007, A Phase-Coupled Compiler Backend for a New VLIW Processor Architecture Using Two-step Register Allocation][research_guo_liu_2007]
- [Guo and Si, 2016, Mechanical hydraulic characteristic analysis scheme based on lightweight crowd data in mobile embedded devices][research_guo_si_2016]
- [Gupta, 1990, An Incremental Type Inference System for the Programming Language Id][research_gupta_1990]
- [Gupta and Lewis, 2018, Neural Compositional Denotational Semantics for Question Answering][research_gupta_lewis_2018]
- [Guria and others, 2021, RbSyn type- and effect-guided program synthesis][research_guria_foster_2021]
- [Gustafsson, 2006, The Worst Case Execution Time Tool Challenge 2006][research_gustafsson_2006]
- [Guyer and Lin, 2005, Broadway A Compiler for Exploiting the Domain-Specific Semantics of Software Libraries][research_guyer_lin_2005]
- [G. Western and Ball, 1991, 3D Pre-stack depth migration in the Gulf of Sueza. A case history][research_gwestern_ball_1991]
- [Haas and others, 2023, Static Analysis of Memory Models for SMT Encodings][research_haas_maseli_2023]
- [Haas and others, 2017, Bringing the web up to speed with WebAssembly][research_haas_rossberg_2017]
- [Haase, 2016, Abstract Interpretation of Java Bytecode for Immutability Analysis][research_haase_2016]
- [Haikun Liu and others, 2011, Live Virtual Machine Migration via Asynchronous Replication and State Synchronization][research_haikunliu_haijin_2011]
- [Haj-Yihia and others, 2015, Compiler-Directed Power Management for Superscalars][research_hajyihia_asher_2015]
- [Hale and others, 2018, Interpreter performance in police interviews. Differences between trained interpreters and untrained bilinguals][research_hale_goodmandelahunty_2018]
- [Hamana, 2022, Modular Termination for Second-Order Computation Rules and Application to Algebraic Effect Handlers][research_hamana_2022]
- [HAMID and ITO, 2017, Image Segmentation to Design Semi-optimized Curve for B-code Generation][research_hamid_ito_2017]
- [Hammer and others, 2025, Compiler-Like Code Generation for fUML Reducing Overhead in Executable UML][research_hammer_maschotta_2025]
- [Hammond and others, 2023, MPI Application Binary Interface Standardization][research_hammond_dalcin_2023]
- [Han, 2016, Building the validity foundation for interpreter certification performance testing][research_han_2016]
- [Han and others, 2024, Range Specification Bug Detection in Flight Control System Through Fuzzing][research_han_ma_2024]
- [Han and others, 2021, Design and Implementation of a Criticality- and Heterogeneity-Aware Runtime System for Task-Parallel Applications][research_han_park_2021]
- [Han and others, 2026, Design and Implementation of Boss AI for 2D Action Games Using Finite State Machines and Coroutine Chaining][research_han_yoo_2026]
- [Han and others, 2021, Parallelizing Compiler Translation Validation Using Happens-Before and Task-Set][research_han_yuki_2021]
- [Han and others, 2024, Enabling Fine-Grained Incremental Builds by Making Compiler Stateful][research_han_zhao_2024]
- [Hanitzsch and others, 2001, Pre-Stack Depth Migration for Time-to-Depth Conversion - the Ultimate Tool?][research_hanitzsch_robein_2001]
- [Hanley and Lippman-Hand 1983, If nothing goes wrong, is everything all right?][research_hanley_lippmanhand_1983]
- [Hansen and Siveroni, 2005, Towards Verification of Well-Formed Transactions in Java Card Bytecode][research_hansen_siveroni_2005]
- [Hanson, 1976, A simple variant of the boundary-tag algorithm for the allocation of coroutine environments][research_hanson_1976]
- [Hanzich and others, 2009, Subsalt Imaging through Pre-Stack Depth Migration - A Case Study from the North Red Sea][research_hanzich_arayapolo_2009]
- [Hara and others, 2021, Machine-learning Approach using Solidity Bytecode for Smart-contract Honeypot Detection in the Ethereum][research_hara_takahashi_2021]
- [Hardy and Puaut, 2013, Static probabilistic worst case execution time estimation for architectures with faulty instruction caches][research_hardy_puaut_2013]
- [Hardy and Puaut, 2014, Static probabilistic worst case execution time estimation for architectures with faulty instruction caches][research_hardy_puaut_2014]
- [Hariri and others, 2016, Evaluating the Effects of Compiler Optimizations on Mutation Testing at the Compiler IR Level][research_hariri_shi_2016]
- [Hariri and others, 2019, Comparing Mutation Testing at the Levels of Source Code and Compiler Intermediate Representation][research_hariri_shi_2019]
- [Harlin and others, 2017, Impact of Using a Static-Type System in Computer Programming][research_harlin_washizaki_2017]
- [Harmon, 1988, An Ada implementation of Marsaglia's universal random number generator][research_harmon_1988]
- [Harmon and Klefstad, 2007, A Survey of Worst-Case Execution Time Analysis for Real-Time Java][research_harmon_klefstad_2007]
- [Harmon and Klefstad, 2007, Interactive Back-annotation of Worst-case Execution Time Analysis for Java Microprocessors][research_harmon_klefstad_2007_2]
- [Harmon and Klefstad, 2007, Toward a Unified Standard for Worst-Case Execution Time Annotations in Real-Time Java][research_harmon_klefstad_2007_3]
- [Harmon and others, 2008, A Modular Worst-case Execution Time Analysis Tool for Java Processors][research_harmon_schoeberl_2008]
- [Harmon and others, 2012, Fast, Interactive Worst-Case Execution Time Analysis With Back-Annotation][research_harmon_schoeberl_2012]
- [Harnes and Morrison, 2024, SoK Analysis Techniques for WebAssembly][research_harnes_morrison_2024]
- [Harper and Pfenning, 1992, A Module System for a Programming Language Based on the LF Logical Framework][research_harper_pfenning_1992]
- [Harrison, 1989, Research, Development, Training and Education Using the Ada Programming Language][research_harrison_1989]
- [Harrison and others, 1976, Theoretical results in compiler design and implementation Tutorial Session][research_harrison_graham_1976]
- [Harshithan, 2023, Batwing Compiler An Artificial Intelligence based Compiler][research_harshithan_2023]
- [Hart and McClanahan, 1981, JOVIAL J73 Compiler Validator][research_hart_mcclanahan_1981]
- [Hartley and others, 2022, Just-In-Time Compilation on ARM-A Closer Look at Call-Site Code Consistency][research_hartley_zakkak_2022]
- [Haspert and Beauregard, 1998, The Commercialization of a Rapid Prototyping Development Tool for Real-Time Embedded Software Intensive, Process, and Resource Management Systems][research_haspert_beauregard_1998]
- [HATABA and others, 2019, Generation of Efficient Obfuscated Code through Just-in-Time Compilation][research_hataba_elmahdy_2019]
- [Hatcliff and Danvy, 1994, A generic account of continuation-passing styles][research_hatcliff_danvy_1994]
- [Hausladen and others, 2017, Integration of Static Worst-Case Execution Time and Stack Usage Analysis for Embedded Systems Software in a Cloud-Based Development Environment][research_hausladen_gerstmayer_2017]
- [Havelund and others, 2000, Formal Analysis of the Remote Agent Before and After Flight][research_havelundklaus_lowrymike_2000]
- [Hazimeh and others, 2021, Magma A Ground-Truth Fuzzing Benchmark][research_hazimeh_herrera_2021]
- [Hazott and others, 2025, Using virtual prototypes and metamorphic testing to verify the hardware/software-stack of embedded graphics libraries][research_hazott_stogmuller_2025]
- [He and others, 2023, Neural-FEBI Accurate function identification in Ethereum Virtual Machine bytecode][research_he_li_2023]
- [He and others, 2025, Evaluating Program Semantics Reasoning with Type Inference in System F][research_he_yang_2025]
- [He and others, 2023, Profile Guided Optimization Transfer-Learning for OpenCL/SYCL Kernel Compilation and Runtime][research_he_zhao_2023]
- [He and Zhong, 2025, From Bug Reports to Workarounds The Real-World Impact of Compiler Bugs][research_he_zhong_2025]
- [Heck and Zaidman, 2015, Quality criteria for just-in-time requirements just enough, just-in-time?][research_heck_zaidman_2015]
- [Heim, 2018, Compiler and language design for quantum computing keynote][research_heim_2018]
- [Heimbigner, 2006, A Tamper-Resistant Programming Language System][research_heimbigner_2006]
- [Heinrich and others, 2024, A Categorical Data Approach for Anomaly Detection in WebAssembly Applications][research_heinrich_will_2024]
- [Henriksen and Gallagher, 2006, Abstract Interpretation of PIC Programs through Logic Programming][research_henriksen_gallagher_2006]
- [Henry and others, 2014, How to compute worst-case execution time by optimization modulo theory and a clever encoding of program semantics][research_henry_asavoae_2014]
- [Hensley and Elgazzar, 2025, DESIGN AND IMPLEMENTATION OF THE MOREHEAD-AZALEA COMPILER MAC][research_hensley_elgazzar_2025]
- [Heo and others, 2025, Bit-level compiler optimization for ultra low-power embedded systems][research_heo_kim_2025]
- [Heo and others, 2019, Resource-Aware Program Analysis Via Online Abstraction Coarsening][research_heo_oh_2019]
- [Hepp and Schoeberl, 2012, Worst-Case Execution Time Based Optimization of Real-Time Java Programs][research_hepp_schoeberl_2012]
- [Herklotz and others, 2023, Mechanised Semantics for Gated Static Single Assignment][research_herklotz_demange_2023]
- [Herring and others, 1993, Research in Presistent Simulation Development of the Persistent ModSim Object-Oriented Programming Language][research_herring_kalathil_1993]
- [Heumann and others, 2015, Scalable Task Scheduling and Synchronization Using Hierarchical Effects][research_heumann_tzannes_2015]
- [Heuring and others, 1990, Automatic Compiler Construction][research_heuring_waite_1990]
- [Hikmatyarsyah and Rahardjo, 2022, Integration of Downlink Scheme VLC Access Techniques for Low-cost Implementation Indoor Communication System A Survey][research_hikmatyarsyah_rahardjo_2022]
- [Liberating effects with rows and handlers][research_hillerstrom_2016]
- [HILLERSTRÖM and others, 2020, Effect handlers via generalised continuations][research_hillerstrom_lindley_2020]
- [HILLERSTRÖM and others, 2024, Asymptotic speedup via effect handlers][research_hillerstrom_lindley_2024]
- [Hinkley and others, 1994, Velocity Model Building for 3D Pre-Stack Depth Migration - a Case Study][research_hinkley_ho_1994]
- [Hirata and others, 2023, Program logic for higher-order probabilistic programs in Isabelle/HOL][research_hirata_minamide_2023]
- [Hird, 1991, Formal specification and verification of Ada software][research_hirdgeoffreyr_1991]
- [Hiroyuki, 2009, Idiom Recognition and Program Scheme Recognition Based Program Transformations for Performance Tuning--Beyond Compiler Optimizations][research_hiroyuki_2009]
- [Hirschowitz, 2019, Familial monads and structural operational semantics][research_hirschowitz_2019]
- [Hmid and others, 2016, A Transfer-Aware Runtime System for Heterogeneous Asynchronous Parallel Execution][research_hmid_coutinho_2016]
- [Hoang and Rabaey, 1992, A compiler for multiprocessor DSP implementation][research_hoang_rabaey_1992]
- [Hollingshaus and Daddario, 2015, Performance Philosophy Arrived Just in Time?][research_hollingshaus_daddario_2015]
- [Holmen and others, 2021, A Heterogeneous MPI+PPL Task Scheduling Approach for Asynchronous Many-Task Runtime Systems][research_holmen_sahasrabudhe_2021]
- [Holmes and Groce, 2018, Causal Distance-Metric-Based Assistance for Debugging after Compiler Fuzzing][research_holmes_groce_2018]
- [Holmes and Groce, 2020, Using mutants to help developers distinguish and debug compiler faults][research_holmes_groce_2020]
- [Hong and Ramanujam, 2008, Address Register Allocation in Digital Signal Processors][research_hong_ramanujam_2008]
- [Hook, 1987, Export Control of the Ada Trade Name Compiler Validation Capability ACVC][research_hook_1987]
- [Hook and Heilbrunner, 1989, Ada Compiler Validation Procedures][research_hook_heilbrunner_1989]
- [Hook and Lehman, 1992, Ada Compiler Validation Support Fiscal Year 1992][research_hook_lehman_1992]
- [Horký and others, 2016, Analysis of Overhead in Dynamic Java Performance Monitoring][research_horky_kotrc_2016]
- [Horvat and others, 2026, Comparative Evaluation of Gemini and DeepSeek for LLM-Generated Code Quality and Architectural Robustness in Backend Software Engineering][research_horvat_ursic_2026]
- [Horwat, 1988, A Concurrent Smalltalk Compiler for the Message-Driven Processor][research_horwat_1988]
- [Hoskins, 1988, The design and implementation of a Karel compiler and interpreter][research_hoskins_1988]
- [Hossain and others, 2021, Code Generator based on Voice Command for Multiple Programming Language][research_hossain_emi_2021]
- [Howe, 1984, A Study of the Feasibility of Duplicating JAMPS Applications Software in the Ada Programming Language][research_howe_1984]
- [Hsu and Kremer, 2003, The design, implementation, and evaluation of a compiler algorithm for CPU energy reduction][research_hsu_kremer_2003]
- [Hu and others, 2025, SSFuzz Synthesizing and scheduling bug-triggering code segments for history-driven compiler testing][research_hu_fan_2025]
- [Hu and others, 2026, QJWasm A lightweight runtime system for efficient WebAssembly execution in resource-constrained environments][research_hu_gu_2026]
- [Hu and others, 2024, An Abstract Interpretation-Based Framework for WCET Analysis of Parallel Programs][research_hu_liu_2024]
- [Hu and Tang, 2024, Research on compiler version recognition based on random forest algorithm][research_hu_tang_2024]
- [Hu and others, 2022, Research on global register allocation for code containing array-unit dual-usage register names][research_hu_zhang_2022]
- [Hu and Zhao, 2014, Analysis on Process Code schedule of Android Dalvik Virtual Machine][research_hu_zhao_2014]
- [Hua and others, 2010, Model-Based Intrusion Detection by Abstract Interpretation][research_hua_nishide_2010]
- [Huang and others, 2022, A High-Performance Bidirectional Compiler for Conversion Between SystemC and Verilog][research_huang_gao_2022]
- [Huang and Huang, 2016, Cell-based delay locked loop compiler][research_huang_huang_2016]
- [Huang and others, 2006, Adaptiveness in well-typed Java bytecode verification][research_huang_jay_2006]
- [Huangfu and Zhang, 2018, Estimating the Worst-Case Execution Time of the Shared Data Cache in Integrated CPU-GPU Architectures][research_huangfu_zhang_2018]
- [Huber and others, 2011, Worst-case execution time analysis-driven object cache design][research_huber_puffitsch_2011]
- [Huch, 1999, Verification of Erlang programs using abstract interpretation and model checking][research_huch_1999]
- [Huck and others, 2022, Compiler-Aided Type Correctness of Hybrid MPI-OpenMP Applications][research_huck_kreutzer_2022]
- [Huck and others, 2018, Compiler-aided Type Tracking for Correctness Checking of MPI Applications][research_huck_lehr_2018]
- [Huck and others, 2020, Towards compiler-aided correctness checking of adjoint MPI applications][research_huck_protze_2020]
- [Hück and others, 2024, Compiler-Aided Correctness Checking of CUDA-Aware MPI Applications][research_huck_ziegler_2024]
- [Hui Zhao and others, 2015, Virtual machine placement based on the VM performance models in cloud][research_huizhao_zheng_2015]
- [Hunt and others, 2008, Using global data flow analysis on bytecode to aid worst case execution time analysis for real-time Java programs][research_hunt_tonin_2008]
- [Hura, 1982, Optimization of assembly code generation in a compiler][research_hura_1982]
- [Hussain and others, 2014, RUGRAT Evaluating program analysis and testing tools and compilers with large generated random benchmark applications][research_hussain_csallner_2014]
- [Huynh and Roychoudhury, 2007, Memory model sensitive bytecode verification][research_huynh_roychoudhury_2007]
- [Huynh and Taura, 2017, Delay Spotter A Tool for Spotting Scheduler-Caused Delays in Task Parallel Runtime Systems][research_huynh_taura_2017]
- [Hyatt and Dewey, 2025, Mutation-Based Fuzzing of the Swift Compiler with Incomplete Type Information][research_hyatt_dewey_2025]
- [Hyland and others, 2007, Combining algebraic effects with continuations][research_hyland_levy_2007]
- [Hyvernat, 2025, The Size-Change Principle for Mixed Inductive and Coinductive types][research_hyvernat_2025]
- [Hyvernat, 2025, Totality for Mixed Inductive and Coinductive Types][research_hyvernat_2025_2]
- [Iida and others, 2026, An Efficient Runtime Verification Toolkit for Self-Adaptive Systems Addressing Runtime System Model Changes][research_iida_oishi_2026]
- [Ikemori and others, 2023, Typed Equivalence of Labeled Effect Handlers and Labeled Delimited Control Operators][research_ikemori_cong_2023]
- [Ilik, 2012, Delimited control operators prove Double-negation Shift][research_ilik_2012]
- [Ilik, 2013, Continuation-passing style models complete for intuitionistic logic][research_ilik_2013]
- [Ilik, 2013, Type Directed Partial Evaluation for Level-1 Shift and Reset][research_ilik_2013_2]
- [Ilik, 2014, Proofs in continuation-passing style][research_ilik_2014]
- [Imamoglu and Cetinkaya, 2017, A rule based decision support system for programming language selection][research_imamoglu_cetinkaya_2017]
- [2024, Implementation concept of the IoT platform using C++ programming language][research_implementation_concept_2024]
- [1973, Implementation of a Pascal compiler for the CII IRIS 80 computer][research_implementation_of_1973]
- [2015, Implementation of a Motor Imagery based BCI System using Python Programming Language][research_implementation_of_2015]
- [2015, Incorporating Near-Surface Velocity Anomalies in Pre-Stack Depth Migration Models][research_incorporating_near_surface_2015]
- [INFORMATION MANAGEMENT INC SAN FRANCISCO CA, 1970, USER'S MANUAL COBOL COMPILER VALIDATION SYSTEM][research_informationmanagementincsanfranciscoca_1970]
- [Inoue and others, 2011, A trace-based Java JIT compiler retrofitted from a method-based compiler][research_inoue_hayashizaki_2011]
- [Inoue and Igarashi, 2019, A type system for first-class layers with inheritance, subtyping, and swapping][research_inoue_igarashi_2019]
- [Inoue and Kaneko, 2015, Bitwidth-aware register allocation and binding for clock period minimization][research_inoue_kaneko_2015]
- [I.Saetchnikov and others, 2026, Microresonator clusters for spectral analysis with machine-learning interpreter][research_isaetchnikov_etcherniavskaia_2026]
- [Ishio and Asai, 2022, Type System for Four Delimited Control Operators][research_ishio_asai_2022]
- [ISHIURA, 2016, Compiler Fuzzing][research_ishiura_2016]
- [Iskra and Hoefler, 2015, Operating systems and runtime environments on supercomputers][research_iskra_hoefler_2015]
- [ISLAM and others, 2022, An Exploration of npm Package Co-Usage Examples from Stack Overflow A Case Study][research_islam_wang_2022]
- [Ismael and others, 2018, System on Chip Implementation of Compiler Stack with a Delimiter Matching Application][research_ismael_zyad_2018]
- [Isoda and others, 2024, Type-Safe Code Generation with Algebraic Effects and Handlers][research_isoda_yokoyama_2024]
- [Israel and others, 2026, Exploring WebAssembly as a Runtime Platform for Safety-Critical Edge Systems][research_israel_r_2026]
- [Ito and others, 2023, Schfuzz Detecting Concurrency Bugs with Feedback-Guided Fuzzing][research_ito_matsubara_2023]
- [Ivanov and others, 2019, Software Structure, Program Generation and Schedulability Analysis of Extracorporeal Perfusion Pump Embedded Controller][research_ivanov_gueorguiev_2019]
- [Ivey and Riley, 2016, Analysis of Programming Language Overhead in DCE][research_ivey_riley_2016]
- [Iwasaki and others, 2018, Lessons Learned from Analyzing Dynamic Promotion for User-Level Threading][research_iwasaki_amer_2018]
- [Iyenghar and others, 2026, Incremental Static Analysis for Detecting and Refactoring Data Clumps in TypeScript][research_iyenghar_baumgartner_2026]
- [Izawa and others, 2022, Threaded Code Generation with a Meta-Tracing JIT Compiler][research_izawa_masuhara_2022]
- [Jaafar and Jaber, 2025, Operational Game Semantics for Generative Algebraic Effects and Handlers][research_jaafar_jaber_2025]
- [Jacek and others, 2016, Assessing the limits of program-specific garbage collection performance][research_jacek_chiu_2016]
- [Jackson, 2026, I/O Optimisation at the Compiler Level IOOpt][research_jackson_2026]
- [Jadhav and others, 2026, Analysis of Compiler-Level Static and Dynamic Features for Automated Bug Prediction Using Transformer Models][research_jadhav_devale_2026]
- [Jadhav and Falk, 2025, Compiler-level DMA-aware multi-objective dynamic SPM allocation][research_jadhav_falk_2025]
- [Jagnik, 2023, Structured Concurrency in Java][research_jagnik_2023]
- [Jain and others, 2022, Coarse Grained FPGA Overlay for Rapid Just-In-Time Accelerator Compilation][research_jain_maskell_2022]
- [Jamieson and Brown, 2021, Compact native code generation for dynamic languages on micro-core architectures][research_jamieson_brown_2021]
- [Jamil, 2018, Design of a Real-Time Interpreter for Arabic Sign Language][research_jamil_2018]
- [JANA, 2023, Sensitive Information Leakage Analysis of Database Code by Abstract Interpretation][research_jana_2023]
- [Janetschek and Prodan, 2017, A compiler transformation-based approach to scientific workflow enactment][research_janetschek_prodan_2017]
- [Janssens and Bruynooghe, 1992, Deriving descriptions of possible values of program variables by means of abstract interpretation][research_janssens_bruynooghe_1992]
- [Jay and Miller, 2018, Structured random differential testing of instruction decoders][research_jay_miller_2018]
- [J. Berkhout, 1992, True amplitude aspects of pre-stack depth migration][research_jberkhout_1992]
- [Jefferson and others, 1994, Ada Compiler Validation Summary Report Certificate Number 940902S1.11376. UNISYS Corporation IntegrAda for Windows NT, Version 1.0. Intel Deskside Server for Intel Pentium 60 MHz = . Intel Deskside Server with Intel Pentium 60 MHz][research_jefferson_johnson_1994]
- [Jefferson and others, 1994, Ada Compiler Validation Summary Report Certificate Number 940902S1.11377 UNISYS Corporation. IntegrAda for Windows NT, Version 1.0. Intel Deskside Server with Intel 80486DX266 = Intel Deskside Server with Intel 80486DX266][research_jefferson_johnson_1994_2]
- [Jeon and others, 2021, A practical algorithm for learning disjunctive abstraction heuristics in static program analysis][research_jeon_jeon_2021]
- [JEONG and others, 2021, Usage Log-Based Testing of Embedded Software and Identification of Dependencies among Environmental Components][research_jeong_cha_2021]
- [Jeong and others, 2019, Razzer Finding Kernel Race Bugs through Fuzzing][research_jeong_kim_2019]
- [Jeong and others, 2024, Conflict-aware compiler for hierarchical register file on GPUs][research_jeong_park_2024]
- [Jervis, 1963, MOBILE. A MOBIDIC COBOL COMPILER][research_jervis_1963]
- [Jesus and Weiland, 2024, Evaluating and optimising compiler code generation for NVIDIA Grace][research_jesus_weiland_2024]
- [Jha and others, 2018, Worst Case Execution Time Estimation for Control Code of Automation Systems][research_jha_dsouza_2018]
- [Ji and others, 2007, Automated Worst-Case Execution Time Analysis Based on Program Modes][research_ji_wang_2007]
- [Ji and Wang, 2022, Optimizing Aggregate Computation of Graph Neural Networks with on-GPU Interpreter-Style Programming][research_ji_wang_2022]
- [Jiang and others, 2024, DCIM Compiler - Physical Design Generator][research_jiang_chow_2024]
- [Jiang and Li, 2014, Using Contour Marking Bytecode Verification Algorithm on the Java Card][research_jiang_li_2014]
- [Jiang and Yan, 2010, Implementation of Static Web-Pages Generator Using JavaScript][research_jiang_yan_2010]
- [Jiang and others, 2025, Distinguishability-Guided Test Program Generation for WebAssembly Runtime Performance Testing][research_jiang_zeng_2025]
- [Jiang and others, 2010, A Debugging Approach for Java Runtime Exceptions Based on Program Slicing and Stack Traces][research_jiang_zhang_2010]
- [Jiang and others, 2015, Implementation and Comparison of the Way That Office Document Is Converted to PDF Documents in the Java Runtime Environment][research_jiang_zheng_2015]
- [Jimenez Gil and others, 2017, Open Challenges for Probabilistic Measurement-Based Worst-Case Execution Time][research_jimenezgil_bate_2017]
- [Jodogne, 2022, Rendering Medical Images using WebAssembly][research_jodogne_2022]
- [Johann and others, 2010, A Generic Operational Metatheory for Algebraic Effects][research_johann_simpson_2010]
- [Johnson, 1978, Tools For Automatic Compiler Generation Panel Discussion][research_johnson_1978]
- [Johnson and others, 2024, Automating Pruning in Top-Down Enumeration for Program Synthesis Problems with Monotonic Semantics][research_johnson_krishnan_2024]
- [Johnson and others, 2023, WaVe a verifiably secure WebAssembly sandboxing runtime][research_johnson_laufer_2023]
- [Jones, 1980, Compiler Generation from Denotational Semantics][research_jones_1980]
- [Jones and Christiansen, 1981, Control Flow Treatment in a Simple Semantics-Directed Compiler Generator][research_jones_christiansen_1981]
- [Jong-In Lee and others, 2005, A Hybrid Framework of Worst-Case Execution Time Analysis for Real-Time Embedded System Software][research_jonginlee_suhyunpark_2005]
- [2010, JSIMIL - A Java Bytecode Clone Detector][research_jsimil_2010]
- [Jui-Ming Chang, 1995, Register Allocation and Binding for Low Power][research_juimingchang_1995]
- [Julián-Iranzo and Rubio-Manzano, 2017, A sound and complete semantics for a similarity-based logic programming language][research_julianiranzo_rubiomanzano_2017]
- [Jung, 2021, CommitBERT Commit Message Generation Using Pre-Trained Programming Language Model][research_jung_2021]
- [Jung, 2024, Miri Practical Undefined Behavior Detection for Rust Keynote][research_jung_2024]
- [., 2018, Just in time and competitive advantage understanding their linkages and impact on operational performance][research_just_in_time_2018]
- [Jyh-Charn Liu and Hung-Ju Lee, 1994, Deterministic upperbounds of the worst-case execution times of cached programs][research_jyhcharnliu_hungjulee_1994]
- [Kaestner, 2007, Safe worst-case execution time analysis by abstract interpretation of executable code][research_kaestner_2007]
- [Kaestner and others, 2025, Determining Worst-Case Execution Time Bounds for Multi-Core Processors][research_kaestner_gebhard_2025]
- [Kahn and others, 2026, Big-Stop Semantics Small-Step Semantics in a Big-Step Judgment][research_kahn_hoffmann_2026]
- [Kakati and Brorsson, 2025, Performance and Usability Implications of Multiplatform and WebAssembly Containers][research_kakati_brorsson_2025]
- [Kalebe and others, 2017, A library for scheduling lightweight threads in Internet of Things microcontrollers][research_kalebe_girao_2017]
- [Kalyur and Nagaraja, 2016, A survey of modeling techniques used in compiler design and implementation][research_kalyur_nagaraja_2016]
- [Kameyama and Tanaka, 2010, Equational axiomatization of call-by-name delimited control][research_kameyama_tanaka_2010]
- [KAMMAR and PRETNAR, 2017, No value restriction is needed for algebraic effects and handlers][research_kammar_pretnar_2017]
- [Kanabar and others, 2023, PureCake A Verified Compiler for a Lazy Functional Language][research_kanabar_vivien_2023]
- [Kanatov and Zouev, 2022, Unified type system for the modern general-purpose programing language][research_kanatov_zouev_2022]
- [Kandemir, 2001, A compiler technique for improving whole-program locality][research_kandemir_2001]
- [Kang and others, 2026, WAMI Compilation to WebAssembly through MLIR without Losing Abstraction][research_kang_desai_2026]
- [Kang and others, 2025, HybridServe Adaptive WebAssembly-Container Runtime Selection for Edge Serverless Computing][research_kang_song_2025]
- [Karachalias and others, 2021, Efficient compilation of algebraic effect handlers][research_karachalias_koprivec_2021]
- [Kargén and Shahmehri, 2018, Speeding Up Bug Finding using Focused Fuzzing][research_kargen_shahmehri_2018]
- [Karpovich and Gosudarev, 2025, WebAssembly performance in the Node.js environment][research_karpovich_gosudarev_2025]
- [Karr, 1984, Code generation by coagulation][research_karr_1984]
- [Karsten and Barghi, 2020, User-level Threading][research_karsten_barghi_2020]
- [Kasampalis and others, 2021, Language-parametric compiler validation with application to LLVM][research_kasampalis_park_2021]
- [Kasaraneni and Nandivada, 2026, Compact Representation and Interleaved Solving for Scalable Constraint-Based Points-to Analysis][research_kasaraneni_nandivada_2026]
- [Katel and others, 2022, MLIR-based code generation for GPU tensor cores][research_katel_khandelwal_2022]
- [Kawamata and others, 2024, Answer Refinement Modification Refinement Type System for Algebraic Effects and Handlers][research_kawamata_unno_2024]
- [Kaynaroglu and others, 2025, EUTROPY A Python-based software optimized with Just-In-Time compilation for simulating eutrophication dynamics in aquatic systems][research_kaynaroglu_razinkovasbaziukas_2025]
- [Ke and Chen, 2020, Instruction Verification of Ethereum Virtual Machine by Formal Method][research_ke_chen_2020]
- [Kearns and Lou Soffa, 1983, The implementation of retention in a coroutine environment][research_kearns_lousoffa_1983]
- [Keaton and Seacord, 2014, Performance of Compiler-Assisted Memory Safety Checking][research_keaton_seacord_2014]
- [Keidel and others, 2018, Compositional soundness proofs of abstract interpreters][research_keidel_poulsen_2018]
- [KELLY, 1963, ADVANCED MYSTIC- A COMPILER FOR MANAGEMENT CONTROL OF COMPUTER PROGRAMMING][research_kelly_1963]
- [Kelly, 1997, Formal Methods Specification and Analysis Guidebook for the Verification of Software and Computer Systems Volume II A Practitioner's Companion][research_kellyjohnc_1997]
- [Kelsey, 1995, A correspondence between continuation passing style and static single assignment form][research_kelsey_1995]
- [Kennedy and Syme, 2001, Design and implementation of generics for the .NET Common language runtime][research_kennedy_syme_2001]
- [Kerneis and Chroboczek, 2011, Continuation-Passing C, compiling threads to events through continuations][research_kerneis_chroboczek_2011]
- [Keutzer and Wolf, 1988, Anatomy of a hardware compiler][research_keutzer_wolf_1988]
- [Khaldi and Chapman, 2016, Towards Automatic HBM Allocation Using LLVM A Case Study with Knights Landing][research_khaldi_chapman_2016]
- [Khaldi and others, 2015, LLVM parallel intermediate representation][research_khaldi_jouvelot_2015]
- [Khatami and others, 2017, Redesigning OP2 Compiler to Use HPX Runtime Asynchronous Techniques][research_khatami_kaiser_2017]
- [Khorasani and others, 2015, Scalable SIMD-Efficient Graph Processing on GPUs][research_khorasani_gupta_2015]
- [KIAM TAN and others, 2019, The verified CakeML compiler backend][research_kiamtan_myreen_2019]
- [Kidney and Wu, 2025, Formalising Graph Algorithms with Coinduction][research_kidney_wu_2025]
- [Kiefer and others, 2017, Relational Program Reasoning Using Compiler IR][research_kiefer_klebanov_2017]
- [Kim, 2015, Exploiting Window Query Semantics in Scalable Data Stream Processing][research_kim_2015]
- [KIM and others, 2000, REGISTER ALLOCATION IN HYPER-BLOCK FOR EPIC PROCESSORS][research_kim_gopinath_2000]
- [Kim and Hong, 2023, Poster BugOss A Regression Bug Benchmark for Empirical Study of Regression Fuzzing Techniques][research_kim_hong_2023]
- [Kim and others, 2019, WCET-Aware Stack Frame Management of Embedded Systems Using Scratchpad Memories][research_kim_khayatian_2019]
- [Kim and others, 2012, Generating Verification Conditions from BIRS Code using Basic Paths for Java Bytecode Verification][research_kim_kim_2012]
- [Kim and others, 2025, Pre-trained Models for Bytecode Instructions][research_kim_kim_2025]
- [Kim and Lee, 2017, A Study on the Light-Weight Virtual Machine Code for IoT Virtual Machine][research_kim_lee_2017]
- [Kim and Lee, 2018, A Study on the Code Generator for a Virtual Machine Code based JavaScript Compiler][research_kim_lee_2018]
- [Kim and Park, 2023, A Multi-core Based Real-time Scheduler Supporting Periodic and Sporadic Threads and Processes][research_kim_park_2023]
- [Kim and Ryou, 2019, Source Code Analysis for Static Prediction of Dynamic Memory Usage][research_kim_ryou_2019]
- [Kim and others, 2025, Fuzzing Acceleration for Memory Safety Bug Discovery with Slicer][research_kim_ryu_2025]
- [Kim and others, 2025, Chimera Fuzzing P4 Network Infrastructure for Multi-Plane Bug Detection and Vulnerability Discovery][research_kim_tian_2025]
- [Kim and others, 2020, Finding Bugs in File Systems with an Extensible Fuzzing Framework][research_kim_xu_2020]
- [Kim and others, 2020, Compiler-directed soft error resilience for lightweight GPU register file protection][research_kim_zeng_2020]
- [Kingsley, 1987, The implementation of a state machine compiler][research_kingsley_1987]
- [Kipps, 1982, Experience with porting techniques on a COBOL 74 compiler][research_kipps_1982]
- [Kirichenko and Tarasov, 2017, Development of design flow for multiported register files, which includes a cell library and a compiler for SOI 0.25-μm process][research_kirichenko_tarasov_2017]
- [Kirner and others, 2009, Precise Worst-Case Execution Time Analysis for Processors with Timing Anomalies][research_kirner_kadlec_2009]
- [Kirner and others, 2010, Beyond loop bounds comparing annotation languages for worst-case execution time analysis][research_kirner_knoop_2010]
- [Kirner and Puschner, 2008, Obstacles in Worst-Case Execution Time Analysis][research_kirner_puschner_2008]
- [Kirner and Schoeberl, 2007, Modeling the Function Cache for Worst-Case Execution Time Analysis][research_kirner_schoeberl_2007]
- [Kiselyov, 2012, Delimited control in OCaml, abstractly and concretely][research_kiselyov_2012]
- [Kishorbhai and Patel, 2026, Online Code Compiler A Modern Web Based Programming Platform][research_kishorbhai_patel_2026]
- [Kistel and Vandenhouten, 2013, A metamodel-based ASN.1 editor and compiler for the implementation of communication protocols][research_kistel_vandenhouten_2013]
- [Klein, 2005, Verified Java Bytecode Verification Verified Java Bytecode Verification][research_klein_2005]
- [Klein and Nipkow, 2001, Verified lightweight bytecode verification][research_klein_nipkow_2001]
- [Klein and Strecker, 2004, Verified bytecode verification and type-certifying compilation][research_klein_strecker_2004]
- [Kleinsorge and others, 2013, Simple analysis of partial worst-case execution paths on general control flow graphs][research_kleinsorge_falk_2013]
- [Klimis, 2026, Compilomorphic Fuzzing Turning a Compiler Against Itself][research_klimis_2026]
- [Klöckner and others, 2016, Array program transformation with Loo.py by example high-order finite elements][research_klockner_wilcox_2016]
- [Klohs and Kastens, 2005, Memory Requirements of Java Bytecode Verification on Limited Devices][research_klohs_kastens_2005]
- [Knoblock and Rehof, 2000, Type elaboration and subtype completion for Java bytecode][research_knoblock_rehof_2000]
- [Knoblock and Rehof, 2001, Type elaboration and subtype completion for Java bytecode][research_knoblock_rehof_2001]
- [Knoop and others, 2017, Replacing conjectures by positive knowledge Inferring proven precise worst-case execution time bounds using symbolic execution][research_knoop_kovacs_2017]
- [Ko and others, 2015, LaminarIR compile-time queues for structured streams][research_ko_burgstaller_2015]
- [Ko and Heo, 2026, TinyGen Portable and Compact Code Generation for Tiny Machine Learning][research_ko_heo_2026]
- [Kobayashi and others, 2017, On the relationship between higher-order recursion schemes and higher-order fixpoint logic][research_kobayashi_lozes_2017]
- [Kobusińska and Wilczynski, 2022, Blocked-based Solidity a Service for Graphically Creating the Smart Contracts in Solidity Programming Language][research_kobusinska_wilczynski_2022]
- [Kocourek and others, 2025, Copy-and-Patch Just-in-Time Compiler for R][research_kocourek_krikava_2025]
- [Koehler and Steuwer, 2021, Towards a Domain-Extensible Compiler Optimizing an Image Processing Pipeline on Mobile CPUs][research_koehler_steuwer_2021]
- [Kokkonis and others, 2025, ROSA Finding Backdoors with Fuzzing][research_kokkonis_marcozzi_2025]
- [Kolek and others, 2013, Adding microMIPS backend to the LLVM compiler infrastructure][research_kolek_jovanovic_2013]
- [Kolesar and others, 2025, Coinductive Proofs of Regular Expression Equivalence in Zero Knowledge][research_kolesar_ali_2025]
- [Komendantskaya and Li, 2018, Towards Coinductive Theory Exploration in Horn Clause Logic Position Paper][research_komendantskaya_li_2018]
- [Komolov and others, 2020, An empirical study of multi-threading paradigms Reactive programming vs continuation-passing style][research_komolov_askarbekuly_2020]
- [Kondratyev and Promsky, 2019, Correctness of Proof Strategy for the Sisal Program Verification][research_kondratyev_promsky_2019]
- [Kong and Chen, 2013, A Worst-Case Execution Time Analysis Approach Based on AOE Networks][research_kong_chen_2013]
- [Kong and Jiang, 2012, A Worst-case execution time analysis approach based on independent paths for ARM programs][research_kong_jiang_2012]
- [Kong and others, 2014, An Overview of Worst-Case Execution Time Estimation for Embedded Programs][research_kong_shi_2014]
- [Koroglu and Wotawa, 2019, Fully Automated Compiler Testing of a Reasoning Engine via Mutated Grammar Fuzzing][research_koroglu_wotawa_2019]
- [Koskimies and others, 1982, Compiler construction using attribute grammars][research_koskimies_raiha_1982]
- [Kossatchev and Posypkin, 2005, Survey of compiler testing methods][research_kossatchev_posypkin_2005]
- [Kot and Kozen, 2005, Kleene Algebra and Bytecode Verification][research_kot_kozen_2005]
- [Kovačević and others, 2022, Automatic compiler/interpreter generation from programs for Domain-Specific Languages Code bloat problem and performance improvement][research_kovacevic_ravber_2022]
- [Kowalewski and others, 2013, Model checking and abstract interpretation as building blocks of advanced program analysis techniques][research_kowalewski_philippou_2013]
- [KOZEN and SILVA, 2016, Practical coinduction][research_kozen_silva_2016]
- [Krause, 2015, Bytewise Register Allocation][research_krause_2015]
- [Krebs and Schmitz, 2014, Jaccie A Java-based compiler-compiler for generating, visualizing and debugging compiler components][research_krebs_schmitz_2014]
- [Krishnamoorthy, 2025, WEBASSEMBLY REVOLUTIONIZING WEB PERFORMANCE AND EXPANDING FRONTIERS OF BROWSER-BASED APPLICATIONS][research_krishnamoorthy_2025]
- [Kristensen and others, 1987, Coroutine Sequencing in BETA][research_kristensen_mollerpedersen_1987]
- [Kroening and others, 2016, Sound static deadlock analysis for C/Pthreads][research_kroening_poetzl_2016]
- [Krogstie and others, 2026, PIP Making Andersen's Points-to Analysis Sound and Practical for Incomplete C Programs][research_krogstie_bahmann_2026]
- [Krzemień and Lukasiewicz, 1976, Automatic generation of lexical analyzers in a compiler-compiler][research_krzemien_lukasiewicz_1976]
- [Kuang and others, 2018, Enhance virtual-machine-based code obfuscation security through dynamic bytecode scheduling][research_kuang_tang_2018]
- [CakeML: a verified implementation of ML][research_kumar_2014]
- [Kumar, 2021, Deep Neural Network Approach to Estimate Early Worst-Case Execution Time][research_kumar_2021]
- [Kumar and others, 2024, Utilizing Machine Learning Techniques for Worst-Case Execution Time Estimation on GPU Architectures][research_kumar_ranjbar_2024]
- [Kuperberg and others, 2021, Coinductive Algorithms for Büchi Automata][research_kuperberg_pinault_2021]
- [Kupke and Rot, 2021, Expressive Logics for Coinductive Predicates][research_kupke_rot_2021]
- [Kuroda and Yuen, 2026, A Concurrent Extension of Reversible Imperative Programming Language with Runtime][research_kuroda_yuen_2026]
- [Kusano and Wang, 2017, Thread-modular static analysis for relaxed memory models][research_kusano_wang_2017]
- [Kusmenko and others, 2018, Highly-Optimizing and Multi-Target Compiler for Embedded System Models][research_kusmenko_rumpe_2018]
- [Kwon and Bae, 2016, Development of a Code Generation Support System in Integrated Development Environment of an Educational Compiler][research_kwon_bae_2016]
- [Kwon and others, 2025, Optimization-Directed Compiler Fuzzing for Continuous Translation Validation][research_kwon_jang_2025]
- [Kwon and others, 2024, Translation Validation for JIT Compiler in the V8 JavaScript Engine][research_kwon_kwon_2024]
- [Kwon and others, 2026, Compiler-Runtime Co-operative Chain of Verification for LLM-Based Code Optimization][research_kwon_shin_2026]
- [Kyriakou and Tselikas, 2022, Complementing JavaScript in High-Performance Node.js and Web Applications with Rust and WebAssembly][research_kyriakou_tselikas_2022]
- [Kyrtatas and others, 2015, A Basic Linear Algebra Compiler for Embedded Processors][research_kyrtatas_spampinato_2015]
- [Lai and others, 2026, Interaction-aware multi-objective optimization method for LLVM compiler option sequences][research_lai_qiao_2026]
- [Laliotis, 1973, Implementation aspects of the symbol hardware compiler][research_laliotis_1973]
- [Lambert and others, 2022, Leveraging Compiler-Based Translation to Evaluate a Diversity of Exascale Platforms][research_lambert_monil_2022]
- [Lambert and Saunders, 2017, Compiler auto-vectorization of matrix multiplication modulo small primes][research_lambert_saunders_2017]
- [Lancellotti and others, 2026, Quantum Oracle Synthesis from HDL Designs via Multi Level Intermediate Representation][research_lancellotti_buda_2026]
- [Landa and Sorin, 1993, Fast pre-stack depth migration by CRP stacking][research_landa_sorin_1993]
- [Lane and Poorman, 1991, Preserving software investment using new fortran compiler technology][research_lane_poorman_1991]
- [Lange and others, 1977, Specification for a STARAN Programming Language][research_lange_cheeseman_1977]
- [Larkins and Jones, 2011, Targeting FPGA-based processors for an implementation-driven compiler construction course][research_larkins_jones_2011]
- [Larus, 2011, Session details Compiler correctness][research_larus_2011]
- [Larus and Hilfinger, 1986, Register allocation in the SPUR Lisp compiler][research_larus_hilfinger_1986]
- [Lasnier and others, 2026, Brack A Verified Compiler for Scheme via CakeML][research_lasnier_yallop_2026]
- [Lawall and Danvy, 1993, Separating stages in the continuation-passing style transformation][research_lawall_danvy_1993]
- [Compiler validation via equivalence modulo inputs][research_le_2014]
- [Le and others, 2015, Finding deep compiler bugs via guided stochastic program mutation][research_le_sun_2015]
- [League, 2002, A Type-Preserving Compiler Infrastructure][research_league_2002]
- [Leavitt and Terrell, 1991, Ada Compiler Evaluation Capability][research_leavitt_terrell_1991]
- [Leavitt and Terrell, 1991, ADA Compiler Evaluation Capability User's Guide, Release 2.0][research_leavitt_terrell_1991_2]
- [Leavitt and Terrell, 1991, Ada Compiler Evaluation Capability. Release 2.0][research_leavitt_terrell_1991_3]
- [Le Charlier and Van Hentenryck, 1994, Experimental evaluation of a generic abstract interpretation algorithm for PROLOG][research_lecharlier_vanhentenryck_1994]
- [Lee, 2017, Exploring a relationship between students' interpreting self-efficacy and performance triangulating data on interpreter performance assessment][research_lee_2017]
- [Lee and others, 2025, React-tRace A Semantics for Understanding React Hooks An Operational Semantics and a Visualizer for Clarifying React Hooks][research_lee_ahn_2025]
- [LEE and others, 2009, Visualization and Formalization of User Constraints for Tight Estimation of Worst-Case Execution Time][research_lee_bang_2009]
- [Lee and others, 2025, Bit-Level Semantics Scalable RAG Retrieval with Neurosymbolic Hyperdimensional Computing][research_lee_jang_2025]
- [Lee and others, 2017, Design and implementation of the secure compiler and virtual machine for developing secure IoT services][research_lee_jeong_2017]
- [Lee and Lee, 2024, IMC-PnG Maximizing runtime performance and timing guarantee for imprecise mixed-criticality real-time scheduling][research_lee_lee_2024]
- [Lee and others, 2015, Flow-sensitive runtime estimation an enhanced hot spot detection heuristics for embedded Java just-in-time compilers][research_lee_moon_2015]
- [Lee and Pleban, 1987, A realistic compiler generator based on high-level semantics another progress report][research_lee_pleban_1987]
- [Lehman, 1992, Ada Compiler Validation Support Fiscal Year 1991][research_lehman_1992]
- [Lehman and others, 1988, Sources of Compiler Capability Information in Validation Summary Reports][research_lehman_hook_1988]
- [Lehmann and others, 2025, Hardware/Software Co-Analysis for Worst Case Execution Time Bounds][research_lehmann_bauer_2025]
- [Lehmann and Pradel, 2022, Finding the Dwarf Recovering Precise Types from WebAssembly Binaries][research_lehmann_pradel_2022]
- [Lei and others, 2025, Furina A Light-weight WebAssembly Runtime for ICS][research_lei_li_2025]
- [Type directed compilation of row-typed algebraic effects][research_leijen_2017]
- [Leijen, 2017, Structured asynchrony with algebraic effects][research_leijen_2017_2]
- [Leijen, 2018, First class dynamic effect handlers or, polymorphic heaps with dynamic effect handlers][research_leijen_2018]
- [Leinenbach and Petrova, 2008, Pervasive Compiler Verification From Verified Programs to Verified Systems][research_leinenbach_petrova_2008]
- [Lemaistre and others, 2001, Automatic and Continuous Image Gather Analysis after Pre-Stack Depth Migration][research_lemaistre_hanitzsch_2001]
- [Lenkefi and Mezei, 2022, Connections between Language Semantics and the Query-based Compiler Architecture][research_lenkefi_mezei_2022]
- [Leopoldseder and others, 2015, Java-to-JavaScript translation via structured control flow reconstruction of compiler IR][research_leopoldseder_stadler_2015]
- [Leopoldseder and others, 2018, Dominance-based duplication simulation DBDS code duplication to enable compiler optimizations][research_leopoldseder_stadler_2018]
- [Leopoldseder and others, 2018, A cost model for a graph-based intermediate-representation in a dynamic compiler][research_leopoldseder_stadler_2018_2]
- [Leroy, 2002, Bytecode verification on Java smart cards][research_leroy_2002]
- [Leroy, 2003, Java Bytecode Verification Algorithms and Formalizations][research_leroy_2003]
- [Leroy, 2006, Formal certification of a compiler back-end or][research_leroy_2006]
- [Formal verification of a realistic compiler][research_leroy_2009_cacm]
- [A formally verified compiler back-end][research_leroy_2009_jar]
- [Coinductive big-step operational semantics][research_leroy_grall_2009]
- [Leuschel, 2004, A framework for the integration of partial evaluation and abstract interpretation of logic programs][research_leuschel_2004]
- [Leverett and others, 1979, An Overview of the Production Quality Compiler-Compiler Project][research_leverett_cattell_1979]
- [Levy, 1996, Should caches be split or shared? Analysis using the superposition of bursty stack depth processes][research_levy_1996]
- [Lezuo and others, 2015, vanHelsing A Fast Proof Checker for Debuggable Compiler Verification][research_lezuo_dragan_2015]
- [L. Freitas da Luz and C. Ribeiro Cruz, 2003, The CRS stack as a tool for pre-stack depth migration][research_lfreitasdaluz_cribeirocruz_2003]
- [LI, 2008, Program Verification Techniques Based on the Abstract Interpretation Theory][research_li_2008]
- [Li, 2019, Haskell Compiler Testing Automation Based on Equivalence-Modulo-Inputs Method][research_li_2019]
- [Li and others, 2026, Unleashing Triton on CPUs Compilation and Runtime Co-Optimization for Scalable Vector Architectures][research_li_chai_2026]
- [Li and others, 2024, Simulink Compiler Testing via Configuration Diversification With Reinforcement Learning][research_li_guo_2024]
- [Li and others, 2016, Modular SDN Compiler Design with Intermediate Representation][research_li_hu_2016]
- [Li and others, 2022, ALPHAPROG Reinforcement Generation of Valid Programs for Compiler Fuzzing][research_li_liu_2022]
- [Li and others, 2025, Solsmith Solidity Random Program Generator for Compiler Testing][research_li_liu_2025]
- [Li and others, 2022, Unleashing the power of compiler intermediate representation to enhance neural program embeddings][research_li_ma_2022]
- [Li and others, 2017, Promotion of Educational Effectiveness by Translation-based Programming Language Learning Using Java and Swift][research_li_sakamoto_2017]
- [Li and Su, 2023, Finding Unstable Code via Compiler-Driven Differential Testing][research_li_su_2023]
- [Li and others, 2024, GastCoCo Graph Storage and Coroutine-Based Prefetch Co-Design for Dynamic Graph Processing][research_li_tao_2024]
- [Li and others, 2025, Lightweight and Holistic-Scalable Serverless Secure Container Runtime for High-Density Deployment and High-Concurrency Startup][research_li_wu_2025]
- [Li and others, 2023, A unified proof technique for verifying program correctness with big-step semantics][research_li_zhang_2023]
- [Li and others, 2015, Compiler directed automatic stack trimming for efficient non-volatile processors][research_li_zhao_2015]
- [Liang and others, 2017, Improving the precision of static analysis Symbolic execution based on GCC abstract syntax tree][research_liang_liu_2017]
- [Liangliang and Yungui, 1990, Clause representations in a compiler-based prolog database][research_liangliang_yungui_1990]
- [Lidbury and others, 2015, Many-core compiler fuzzing][research_lidbury_lascu_2015]
- [Lidman and Svenningsson, 2017, Bridging Static and Dynamic Program Analysis using Fuzzy Logic][research_lidman_svenningsson_2017]
- [Lim and Debray, 2023, Automatically Localizing Dynamic Code Generation Bugs in JIT Compiler Back-End][research_lim_debray_2023]
- [Lima and others, 2019, A memory-bounded, deterministic and terminating semantics for the synchronous programming language Céu][research_lima_santos_2019]
- [Lin and others, 2016, Rust as a language for high performance GC implementation][research_lin_blackburn_2016]
- [Lin and others, 2025, Intermediate Representation-Based Approach for Code Refactoring and Quality Evaluation][research_lin_ni_2025]
- [Lin and Padua, 2000, Compiler analysis of irregular memory accesses][research_lin_padua_2000]
- [Lin and others, 2023, DeepDiffer Find Deep Learning Compiler Bugs via Priority-guided Differential Fuzzing][research_lin_song_2023]
- [Lindley, 2014, Algebraic effects and effect handlers for idioms and arrows][research_lindley_2014]
- [Lins and others, 2017, Register File Criticality and Compiler Optimization Effects on Embedded Microprocessors Reliability][research_lins_tambara_2017]
- [Lintzmayer and others, 2011, Register Allocation with Graph Coloring by Ant Colony Optimization][research_lintzmayer_mulati_2011]
- [Lion and Broman, 2026, Making Time Observable Compiler Correctness for Real-Time C Programs][research_lion_broman_2026]
- [Liu, 2007, Bytecode Verification for Enhanced JVM Access Control][research_liu_2007]
- [Liu and others, 2021, Relaxed Peephole Optimization A Novel Compiler Optimization for Quantum Circuits][research_liu_bello_2021]
- [Liu and others, 2024, A Verified Compiler for a Functional Tensor Language][research_liu_bernstein_2024]
- [Liu and others, 2018, Research of Register Pressure Aware Loop Unrolling Optimizations for Compiler][research_liu_ding_2018]
- [Liu and others, 2025, BoostPolyGlot A Structured IR Generation-Based Fuzz Testing Framework for GCC Compiler Frontend][research_liu_guo_2025]
- [Liu and others, 2020, A type-and-effect system for object initialization][research_liu_lhotak_2020]
- [Liu and Li, 2018, A novel virtual machine scheduling policy based on performance prediction model][research_liu_li_2018]
- [Liu and others, 2024, Research on Higher-Order Operator Transformation Algorithms for Syntax Transformation-Based Model Checking][research_liu_liu_2024]
- [Liu and Lu, 2025, Bi-directional Taint Flow Analysis A High-precision Static Detection Approach for Java Deserialization Vulnerabilities][research_liu_lu_2025]
- [Liu and others, 2021, Design and Implementation of Multi-core Parallel Compiler Based on OpenMP][research_liu_lv_2021]
- [Liu and others, 2019, Accelerating sequential consistency for Java with speculative compilation][research_liu_millstein_2019]
- [Liu and others, 2026, Learning Compiler Fuzzing Mutators from Historical Bugs][research_liu_qin_2026]
- [Liu and others, 2025, WebAssembly for Container Runtime Are We There Yet?][research_liu_shen_2025]
- [Liu and others, 2022, Coverage-guided tensor compiler fuzzing with joint IR-pass mutation][research_liu_wei_2022]
- [Liu and others, 2011, Coroutine-Based Synthesis of Efficient Embedded Software From SystemC Models][research_liu_xu_2011]
- [Liu and others, 2024, An efficient schedulability analysis based on worst-case interference time for real-time systems][research_liu_yang_2024]
- [Liu and others, 2017, Analyzing divergence in bisimulation semantics][research_liu_yu_2017]
- [Liu and others, 2013, Linking Algebraic Semantics and Operational Semantics for Web Services Using Maude][research_liu_zhu_2013]
- [Lo and Suh, 2012, Worst-case execution time analysis for parallel run-time monitoring][research_lo_suh_2012]
- [Lochbihler, 2018, Mechanising a Type-Safe Model of Multithreaded Java with a Verified Compiler][research_lochbihler_2018]
- [Lööw, 2021, Lutsig a verified Verilog compiler for verified circuit development][research_loow_2021]
- [Lopes, 2023, Torchy A Tracing JIT Compiler for PyTorch][research_lopes_2023]
- [Lopoukhine and others, 2025, A Multi-level Compiler Backend for Accelerated Micro-kernels Targeting RISC-V ISA Extensions][research_lopoukhine_ficarelli_2025]
- [Loring and others, 2019, Sound regular expression semantics for dynamic symbolic execution of JavaScript][research_loring_mitchell_2019]
- [Louise, 2011, Improving Branch Prediction Related WCET Abstract Interpretation][research_louise_2011]
- [Loveless and others, 2020, A performance-optimizing compiler for cyber-physical digital microfluidic biochips][research_loveless_ott_2020]
- [Lowther and others, 2023, CHERI Performance Enhancement for a Bytecode Interpreter][research_lowther_jacob_2023]
- [Loy, 1981, Notes on the Implementation of MUSBOX A Compiler for the Systems Concepts Digital Synthesizer][research_loy_1981]
- [Lozano and others, 2016, Register allocation and instruction scheduling in Unison][research_lozano_carlsson_2016]
- [Lu and others, 2022, Gradual Soundness Lessons from Static Python][research_lu_greenman_2022]
- [Lu and others, 2011, A new way about using statistical analysis of worst-case execution times][research_lu_nolte_2011]
- [Lu and others, 2011, A trace-based statistical worst-case execution time analysis of component-based real-time embedded systems][research_lu_nolte_2011_2]
- [Lu and others, 2025, Detecting WebAssembly Runtime Bugs With Grammar-Guided Program Mutation][research_lu_zhou_2025]
- [Lucanu, 2018, Proving Reachability Properties by Coinduction Extended Abstract][research_lucanu_2018]
- [Lucchi and Mazzara, 2007, A pi-calculus based semantics for WS-BPEL][research_lucchi_mazzara_2007]
- [Luo, 2020, Heap Memory Snapshot Assisted Program Analysis for Android Permission Specification][research_luo_2020]
- [Luo and others, 2017, Compiler-Assisted Threshold Implementation against Power Analysis Attacks][research_luo_athanasiou_2017]
- [Luo and others, 2026, GeoJSON agents a multi-agent LLM architecture for geospatial analysis-function calling vs. code generation][research_luo_lin_2026]
- [Lv and others, 2010, Static worst-case execution time analysis of the μC/OS-II real-time kernel][research_lv_guan_2010]
- [Ly and others, 2009, Reduced Model for a PEMFC Stack Automated Code Generation and Verification][research_ly_birgersson_2009]
- [Lyamin, 2018, Method of Formal Program Verification for Post Machine Virtual Laboratory][research_lyamin_2018]
- [Lynn, 1978, Interactive Compiler Proving Using Hoare Proof Rules][research_lynn_1978]
- [M, 2026, No-Code Backend Orchestrator with Drag and Drop Architecture and AI-Assisted Contextual Code Generation][research_m_2026]
- [M and Murugesh, 2021, Comparative Study of Binary Classification Algorithms to Analyze the Students Performance on Virtual Machine][research_m_murugesh_2021]
- [Ma, 2025, Lexical Effect Handlers Fast by Design, Correct by Proof][research_ma_2025]
- [Ma and others, 2024, Lexical Effect Handlers, Directly][research_ma_ge_2024]
- [Ma and others, 2025, Zero-Overhead Lexical Effect Handlers][research_ma_ge_2025]
- [Maccabe, 2017, Operating and Runtime Systems Challenges for HPC Systems][research_maccabe_2017]
- [MacMillen, 2001, Nimble Compiler Environment for Agile Hardware. Volume 1][research_macmillen_2001]
- [Madsen and others, 2018, Tail call elimination and data representation for functional languages on the Java virtual machine][research_madsen_zarifi_2018]
- [Magdalenić and others, 2011, Implementation Model of Source Code Generator][research_magdalenic_radosevic_2011]
- [Magesty and Montandon, 2026, PromiseAwait A Dataset of JavaScript Migrations from Promises to Async/Await][research_magesty_montandon_2026]
- [Mahajan and others, 2020, Recommending stack overflow posts for fixing runtime exceptions using failure scenario matching][research_mahajan_abolhassani_2020]
- [Mahajan and Ali, 2008, Hybrid evolutionary algorithm for graph coloring register allocation][research_mahajan_ali_2008]
- [Mahajan and Prasad, 2022, Providing Real-time Assistance for Repairing Runtime Exceptions using Stack Overflow Posts][research_mahajan_prasad_2022]
- [Maia and others, 2026, Why Just-In-Time Compilation Matters Evaluating Runtime and Energy Efficiency][research_maia_cunha_2026]
- [Mainland, 2017, Better living through operational semantics an optimizing compiler for radio protocols][research_mainland_2017]
- [Maity and Ghose, 2026, SAGE A Compiler-assisted Reinforcement Learning-based Offloading Approach under Near-memory Processing Paradigm][research_maity_ghose_2026]
- [Mäkelä and others, 2016, Compiler assisted dynamic allocation of finite hardware acceleration resources for parallel tasks][research_makela_forsell_2016]
- [Makki Mohialden and others, 2023, A Comparative Analysis of Python Code-Line Bug-Finding Methods][research_makkimohialden_mahmoodhussien_2023]
- [Malcolm, 1971, PL360 Revised . A Programming Language for the IBM360][research_malcolm_1971]
- [Maldonado and Carrasco-Sáez, 2026, A Reusable J48-Targeting Python Backend for Scikit-Learn Workflows Differential Validation Against WEKA J48][research_maldonado_carrascosaez_2026]
- [Male and others, 2011, Formalisation and implementation of an algorithm for bytecode verification of @NonNull types][research_male_pearce_2011]
- [Mallawarachchi and Jayaweera, 2025, Implementation of Wyltl An Imperative Language with a Dual Interpreter Compiler Architecture][research_mallawarachchi_jayaweera_2025]
- [Mamdouh and others, 2014, On-demand distributed on-card bytecode verification][research_mamdouh_bahaaeldin_2014]
- [Mane Ritesh Pratap and Alpona Das, 2023, Designing a Random Password Generator Using Python Programming Language][research_maneriteshpratap_alponadas_2023]
- [Manjunath, 2010, Colored Steganography Implementation Scheme of Images using Transform Technique][research_manjunath_2010]
- [Mann, 2003, The Compiler Design Handbook Optimisation and Machine Code Generation][research_mann_2003]
- [Manna, 1988, TABLOG The Deductive Tableau Programming Language][research_manna_1988]
- [Mao and others, 2025, Research on a Lightweight Full-Stack Edge Execution Optimization Framework Based on Serverless and WebAssembly][research_mao_chen_2025]
- [Mao and others, 2019, Exploiting Java Stack Forensics for Runtime Monitoring of IoT Services][research_mao_zhang_2019]
- [Marcelino and others, 2025, Lumos Performance Characterization of WebAssembly as a Serverless Runtime in the Edge-Cloud Continuum][research_marcelino_krennmair_2025]
- [Marcelino and Nastic, 2023, CWASI A WebAssembly Runtime Shim for Inter-function Communication in the Serverless Edge-Cloud Continuum][research_marcelino_nastic_2023]
- [Marcozzi and others, 2019, Compiler fuzzing how much does it matter?][research_marcozzi_tang_2019]
- [Coroutines: A Programming Methodology, a Language Design and an Implementation][research_marlin_1980]
- [Marref, 2011, Fully-automatic derivation of exact program-flow constraints for a tighter worst-case execution-time analysis][research_marref_2011]
- [Marriott and others, 1994, Denotational abstract interpretation of logic programs][research_marriott_sondergaard_1994]
- [Marshall, 1982, The linear graph package, a compiler building environment][research_marshall_1982]
- [Martinsen and others, 2016, Combining thread-level speculation and just-in-time compilation in Google's V8 JavaScript engine][research_martinsen_grahn_2016]
- [Márton and Porkoláb, 2017, Unit Testing in C++ with Compiler Instrumentation and Friends][research_marton_porkolab_2017]
- [Mary-Anne K Posenau, 1993, Unstructured Grid Generation Techniques and Software][research_maryannekposenau_1993]
- [Massey and Olivier, 2026, WASP Stack protection for WebAssembly][research_massey_olivier_2026]
- [Massidda and others, 2024, Bringing Binary Exploitation at Port 80 Understanding C Vulnerabilities in WebAssembly][research_massidda_pisu_2024]
- [Mastorou and others, 2022, Coinduction inductively mechanizing coinductive proofs in Liquid Haskell][research_mastorou_papaspyrou_2022]
- [Masuko and Asai, 2009, Direct implementation of shift and reset in the MinCaml compiler][research_masuko_asai_2009]
- [Matsikoudis and Stergiou, 2014, First Draft of the act Programming Language][research_matsikoudis_stergiou_2014]
- [Matsubara and others, 2025, Seamless Self-Healing in WebAssembly Container Orchestration with Runtime-Neutral Checkpointing][research_matsubara_saito_2025]
- [Matteo R. Donelli, 2025, Compiler-Assisted Optimization Using Neural Code Embeddings for Heterogeneous Architectures][research_matteordonelli_2025]
- [Maurer and others, 2017, Compiling without continuations][research_maurer_downen_2017]
- [Mazaher and Berry, 1985, Deriving a compiler from an operational semantics written in VDL][research_mazaher_berry_1985]
- [McNerney, 1991, Verifying the correctness of compiler transformations on basic blocks using abstract interpretation][research_mcnerney_1991]
- [Medeiros and others, 2018, Evaluation of Compiler Optimization Flags Effects on Soft Error Resiliency][research_medeiros_bortolon_2018]
- [Meghzili and others, 2017, On the Verification of UML State Machine Diagrams to Colored Petri Nets Transformation Using Isabelle/HOL][research_meghzili_chaoui_2017]
- [Mehdi Pourhashem Kallehbasti and Ghafari, 2023, Naturalistic Static Program Analysis][research_mehdipourhashemkallehbasti_ghafari_2023]
- [Mehta and Yew, 2015, Improving compiler scalability optimizing large programs at small price][research_mehta_yew_2015]
- [Meier and others, 2025, CertiCoq-Wasm A Verified WebAssembly Backend for CertiCoq][research_meier_jensen_2025]
- [Melnyk and Kozak, 2019, Easy Universal Translator as an Alternative Compiler-Compiler][research_melnyk_kozak_2019]
- [Melo Alves and others, 2018, An Interference-Aware Virtual Machine Placement Strategy for High Performance Computing Applications in Clouds][research_meloalves_teylo_2018]
- [Melquiond and Moreau, 2024, A Safe Low-Level Language for Computer Algebra and Its Formally Verified Compiler][research_melquiond_moreau_2024]
- [Melrose and others, 2015, Just in Time][research_melrose_sachsenmaier_2015]
- [Menetrey and others, 2021, Twine An Embedded Trusted Runtime for WebAssembly][research_menetrey_pasin_2021]
- [Menetrey and others, 2022, WaTZ A Trusted WebAssembly Runtime Environment with Remote Attestation for TrustZone][research_menetrey_pasin_2022]
- [Ménétrey and others, 2024, A Comprehensive Trusted Runtime for WebAssembly With Intel SGX][research_menetrey_pasin_2024]
- [Meng and others, 2020, Survey on Estimation and Optimization of Worst-case Execution Time with Energy Consumption Constraint][research_meng_sun_2020]
- [Merazga and others, 2025, Worst-Case Execution Time Analysis of a Real-Time System based on Arduino in CAN Network][research_merazga_rahem_2025]
- [Meybodi, 2015, The links between just-in-time practices and alignment of benchmarking performance measures][research_meybodi_2015]
- [Meyer and Wolff, 2019, Decoupling lock-free data structures from memory reclamation for static analysis][research_meyer_wolff_2019]
- [Mguidich and others, 2016, Time-Accurate ASM as a Refinement Scheme for Worst-Case Execution Time Estimation in Hard Real-Time Systems][research_mguidich_paun_2016]
- [Mhaske and others, 2015, A 2.48Gb/s FPGA-based QC-LDPC decoder An algorithmic compiler implementation][research_mhaske_uliana_2015]
- [Michaud and others, 2024, Robust Stack Smashing Protection for WebAssembly][research_michaud_pipereau_2024]
- [Michels and others, 2015, A new probabilistic constraint logic programming language based on a generalised distribution semantics][research_michels_hommersom_2015]
- [Midtgaard, 2025, Property-Based Testing of OCaml 5's Runtime System][research_midtgaard_2025]
- [MIDZIC and NOVAK, 2025, Performance Comparison of WebAssembly and Phaser in Procedural Maze Generation][research_midzic_novak_2025]
- [Mihelic and others, 2021, A denotational semantics of a concatenative/compositional programming language][research_mihelic_steingartner_2021]
- [Milano and others, 2022, A flexible type system for fearless concurrency][research_milano_turcotti_2022]
- [Milos and others, 1984, Direct implementation of compiler specifications or the pascal p-code compiler revisited][research_milos_pleban_1984]
- [Minato and others, 2025, Implementation and Evaluation of a System Call Moving Target Defense Applied Multiple Times at Runtime for Binary Injections][research_minato_masumoto_2025]
- [Miné, 2017, Tutorial on Static Inference of Numeric Invariants by Abstract Interpretation][research_mine_2017]
- [Mitra and Givargis, 2009, Session details Microfluidics, worst-case execution time, and cache optimization][research_mitra_givargis_2009]
- [Mittal and others, 2021, Towards an Approach for Translation Validation of Thread-level Parallelizing Transformations using Colored Petri Nets][research_mittal_banerjee_2021]
- [Mizikovskiy, 2024, Methodology of management cost accounting and calculation of the cost of not amortised organizational and technological equipment for the production of industrial enterprise products][research_mizikovskiy_2024]
- [Mizobuchi and Takayama, 2017, Two improvements to detect duplicates in Stack Overflow][research_mizobuchi_takayama_2017]
- [1997, Modern compiler implementation in C Basic techniques][research_modern_compiler_1997]
- [1997, Modern compiler implementation in Java Basic techniques][research_modern_compiler_1997_2]
- [1997, Modern compiler implementation in ML Basic techniques][research_modern_compiler_1997_3]
- [1998, Modern compiler implementation in Java Revised and expanded edition][research_modern_compiler_1998]
- [Mohan, 2008, Worst-case execution time analysis of security policies for deeply embedded real-time systems][research_mohan_2008]
- [Mohnen, 1997, A COMPILER CORRECTNESS PROOF FOR THE STATIC LINK TECHNIQUE BY MEANS OF EVOLVING ALGEBRAS][research_mohnen_1997]
- [Moliavko and others, 2019, uJVM Lightweight Java Virtual Machine for embedded systems][research_moliavko_drozdovskyi_2019]
- [MolinaFraticelli, 2012, Auto Code Generation for Simulink-Based Attitude Determination Control System][research_molinafraticellijosecarlos_2012]
- [Mondal and others, 2023, Investigating Technology Usage Span by Analyzing Users' QandA Traces in Stack Overflow][research_mondal_mondal_2023]
- [Mondal and others, 2016, Embedded Emotion-based Classification of Stack Overflow Questions Towards the Question Quality Prediction][research_mondal_rahman_2016]
- [Mondshein, 1967, VITAL COMPILER SYSTEM REFERENCE MANUAL][research_mondshein_1967]
- [Monniaux, 2024, Memory Simulations, Security and Optimization in a Verified Compiler][research_monniaux_2024]
- [Monsuez, 1995, Using abstract interpretation to define a strictness type inference system][research_monsuez_1995]
- [Montenegro and others, 2015, Space consumption analysis by abstract interpretation Reductivity properties][research_montenegro_pena_2015]
- [Moody and Richards, 1980, A coroutine mechanism for BCPL][research_moody_richards_1980]
- [Moor, 1982, An applicative compiler for a parallel machine][research_moor_1982]
- [Moore, 1968, Data Processing with the Compiler Compiler][research_moore_1968]
- [Moret and others, 2011, Polymorphic bytecode instrumentation][research_moret_binder_2011]
- [Morford, 1999, A Case Study Using 3D Pre-Stack Depth Migration To Improve The Sub-Salt Image In Marbella, Mexico, Gulf Of Mexico][research_morford_1999]
- [Morford, 2000, A case study Using 3d pre-stack depth migration to image sub-salt sediments and fault zones in Marbella, Mexico][research_morford_2000]
- [Morford, 2001, Analysis Of The Effects Of Varying The Anti - Alias Filter In Kirchoff Pre- Stack Depth Migration][research_morford_2001]
- [MORIGUCHI and others, 2016, Verification of Content-Centric Networking Using Proof Assistant][research_moriguchi_morishima_2016]
- [Moron and Wallentowitz, 2023, Support for Just-in-Time Compilation of WebAssembly for Embedded Systems][research_moron_wallentowitz_2023]
- [Mosaner and others, 2022, Improving Vectorization Heuristics in a Dynamic Compiler with Machine Learning Models][research_mosaner_barany_2022]
- [Moser and Schneckenreither, 2020, Automated amortised resource analysis for term rewrite systems][research_moser_schneckenreither_2020]
- [Moskalenko, 2025, Application of WebAssembly for High-Performance Client-Side Media Content Analysis][research_moskalenko_2025]
- [Moss and others, 2016, The ARES High-Level Intermediate Representation][research_moss_davis_2016]
- [Mössenböck, 1984, Ein einfacher Compiler-Compiler für Mikrocomputer / Α simple compiler-compiler for microcomputer][research_mossenbock_1984]
- [Mosses, 2004, Modular structural operational semantics][research_mosses_2004]
- [Mosses, 2015, Semantics of programming languages Using Asf+Sdf][research_mosses_2015]
- [Mosterman and Zander, 2015, Cyber-physical systems challenges a needs analysis for collaborating embedded software systems][research_mosterman_zander_2015]
- [Mpeis and others, 2021, Developer and user-transparent compiler optimization for interactive applications][research_mpeis_petoumenos_2021]
- [Mückenschnabel, 2024, Algebraic Effect Handlers with Bidirectional Type-Checking][research_muckenschnabel_2024]
- [Mukherjee and others, 2024, HLS-IRT Hardware Trojan Insertion through Modification of Intermediate Representation During High-Level Synthesis][research_mukherjee_ghosh_2024]
- [Müller and others, 2026, WasmWeaver A Framework for Runtime-Aware WebAssembly Program Generation with Reinforcement Learning][research_muller_mane_2026]
- [Müller and others, 2023, From Capabilities to Regions Enabling Efficient Compilation of Lexical Effect Handlers][research_muller_schuster_2023]
- [Muller and Zhou, 1992, Abstract interpretation in weak powerdomains][research_muller_zhou_1992]
- [Munley and others, 2024, LLM4VV Developing LLM-driven testsuite for compiler validation][research_munley_jarmusch_2024]
- [Murthy and Mellor-Crummey, 2015, A Compiler Transformation to Overlap Communication with Dependent Computation][research_murthy_mellorcrummey_2015]
- [Mushtaq and others, 2015, Calculation of worst-case execution time for multicore processors using deterministic execution][research_mushtaq_alars_2015]
- [Müssig, 2019, Just enough, just in time, just for me][research_mussig_2019]
- [Musumbu, 2008, Static Checking by Means of Abstract Interpretation][research_musumbu_2008]
- [Muts and Falk, 2020, Compiler-based WCET prediction performing function specialization][research_muts_falk_2020]
- [Mycroft, 1993, Completeness and predicate-based abstract interpretation][research_mycroft_1993]
- [Mykola, 2024, USING ASYNCHRONOUS PROGRAMMING IN PYTHON TO IMPROVE APPLICATION PERFORMANCE][research_mykola_2024]
- [Myreen, 2010, Verified just-in-time compiler on x86][research_myreen_2010]
- [Myreen, 2021, A minimalistic verified bootstrapped compiler proof pearl][research_myreen_2021]
- [Mzid and others, 2022, Use of Compiler Intermediate Representation for Reverse Engineering A Case Study for GCC Compiler and UML Activity Diagram][research_mzid_charfi_2022]
- [Na and others, 2016, JavaScript Parallelizing Compiler for Exploiting Parallelism from Data-Parallel HTML5 Applications][research_na_kim_2016]
- [Nadi and Treude, 2020, Essential Sentences for Navigating Stack Overflow Answers][research_nadi_treude_2020]
- [Nagata and others, 2024, Evaluation of Interoperability of CNN Models between MATLAB and Python Environments Using ONNX Runtime Model][research_nagata_sakata_2024]
- [Naik, 2013, Session details Compiler validation][research_naik_2013]
- [Nair, 2012, A Formal Semantics for Ciset and Ciset Relation Operators][research_nair_2012]
- [Nair and Sarasamma, 2006, Formal Semantics of Ciset Relational Operators][research_nair_sarasamma_2006]
- [Naish, 2015, Sharing analysis in the Pawns compiler][research_naish_2015]
- [Nakata and Matsubara, 2025, Self-Hosted WebAssembly Runtime for Runtime-Neutral Checkpoint/Restore in Edge-Cloud Continuum][research_nakata_matsubara_2025]
- [Nakata and Uustalu, 2015, A Hoare logic for the coinductive trace-based big-step semantics of While][research_nakata_uustalu_2015]
- [Namakonov and Podkopaev, 2019, Compilation of OCaml memory model into Power][research_namakonov_podkopaev_2019]
- [Nanthaamornphong and others, 2015, Bytecode-based class dependency extraction tool Bytecode-CDET][research_nanthaamornphong_leatongkam_2015]
- [Nappa and others, 2019, Fast Parallel Equivalence Relations in a Datalog Compiler][research_nappa_zhao_2019]
- [Narkthong and others, 2024, ALLI/O Diagram An Action-based Visual Programming Language for Embedded System][research_narkthong_jariyavajee_2024]
- [Natarajan and Broman, 2020, Temporal Property-Based Testing of a Timed C Compiler using Time-Flow Graph Semantics][research_natarajan_broman_2020]
- [NATIONAL BUREAU OF STANDARDS GAITHERSBURG MD, 1988, Ada Compiler Validation Summary Report Certificate Number 880708S1. 09151, SoftTech, Inc., Ada 86, Version 3.21 VAX 11/780-11/785 Host and Intel IAPX 80386R Target][research_nationalbureauofstandardsgaithersburgmd_1988]
- [NATIONAL BUREAU OF STANDARDS GAITHERSBURG MD, 1988, Ada Compiler Validation Summary Report Certificate Number 880719S1. 09154, Naval Underwater Systems Command, ADAUYK43 ALS/N Ada/L , Version 1.0, VAX 11/785 Host and AN/UYK-43 Target][research_nationalbureauofstandardsgaithersburgmd_1988_2]
- [NATIONAL BUREAU OF STANDARDS GAITHERSBURG MD, 1988, Ada Compiler Validation Summary Report Compiler Name ADE/32 Revision 3.00. Certificate Number 880527S1.09113. Host MV/20000 under AOS/VS, Revision 7.56. Target ROLM HAWK/32 under AOS/VS, Revision 7.56][research_nationalbureauofstandardsgaithersburgmd_1988_3]
- [NATIONAL BUREAU OF STANDARDS GAITHERSBURG MD, 1989, Ada Compiler Validation Summary Report Certificate Number 880624S1. 09132, Control Data Corporation CYBER 180 Ada Compiler, Version 1.1 HOST and TARGET COMPUTER CYBER 180-930-31][research_nationalbureauofstandardsgaithersburgmd_1989]
- [Nayvelt and Bear, 2008, Case study Anisotropic Pre-Stack Depth Migration on the Louisiana Shelf][research_nayvelt_bear_2008]
- [Proof-carrying code][research_necula_1997]
- [Necula, 2000, Translation validation for an optimizing compiler][research_necula_2000]
- [Necula and Lee, 1998, The design and implementation of a certifying compiler][research_necula_lee_1998]
- [Necula and Lee, 2004, The design and implementation of a certifying compiler][research_necula_lee_2004]
- [Nedoria, 2023, Programming Language for Teaching Compilation and Transformation Technologies][research_nedoria_2023]
- [Negrini, 2026, Whole-value analysis by abstract interpretation][research_negrini_2026]
- [Neis and others, 2015, Pilsner a compositionally verified compiler for a higher-order imperative language][research_neis_hur_2015]
- [Nejjar and others, 2024, LLMs for science Usage for code generation and data analysis][research_nejjar_zacharias_2024]
- [Nemer and others, 2007, Improving the Worst-Case Execution Time Accuracy by Inter-Task Instruction Cache Analysis][research_nemer_casse_2007]
- [2016, Network-Aware Virtual Machine Placement in the Cloud][research_network_aware_virtual_2016]
- [New and others, 2023, Gradual Typing for Effect Handlers][research_new_giovannini_2023]
- [Newey, 1975, Formal Sematics of LISP with Applications to Program Correctness][research_newey_1975]
- [Nezamabadi and others, 2026, Verified VCG and Verified Compiler for Dafny][research_nezamabadi_myreen_2026]
- [Ngo and others, 2015, Modular translation validation of a full-sized synchronous compiler using off-the-shelf verification tools][research_ngo_talpin_2015]
- [Nguyen and others, 2019, Integrating Static Program Analysis Tools for Verifying Cautions of Microcontroller][research_nguyen_aoki_2019]
- [Nguyen and McCaskey, 2022, Extending Python for Quantum-classical Computing via Quantum Just-in-time Compilation][research_nguyen_mccaskey_2022]
- [Nguyen and others, 2023, Effect Handlers for Programmable Inference][research_nguyen_perera_2023]
- [Ni and Li, 2025, Interleaving Large Language Models for Compiler Testing][research_ni_li_2025]
- [Nickerson, 1990, Graph coloring register allocation for processors with multi-register operands][research_nickerson_1990]
- [Nielsen, 1997, Compiler Support for Message Passing Systems][research_nielsen_1997]
- [Nielsen, 1998, Compiler Support for Message Passing Systems][research_nielsen_1998]
- [Nielson, 1987, Strictness analysis and denotational abstract interpretation][research_nielson_1987]
- [Nielson, 1988, Strictness analysis and denotational abstract interpretation][research_nielson_1988]
- [Niephaus and others, 2018, Live Multi-language Development and Runtime Environments][research_niephaus_felgentreff_2018]
- [Nikhil Sripathi Rao, 2024, WebAssembly Revolutionizing Web User Interface Development through Performance and Cross-Language Integration][research_nikhilsripathirao_2024]
- [Nilsen and Rygg, 1995, Worst-case execution time analysis on modern processors][research_nilsen_rygg_1995]
- [Nipkow, 2003, Java Bytecode Verification][research_nipkow_2003]
- [Nishizaki, 2017, Linear lambda calculus with non-linear first-class continuations][research_nishizaki_2017]
- [Nishizaki, 2017, Type Inference of Linear Lambda Calculus with First-Class Continuations][research_nishizaki_2017_2]
- [Nishizaki, 2019, ML Polymorphism of Linear Lambda Calculus with First-class Continuations][research_nishizaki_2019]
- [Niu and others, 2024, FAIR Flow Type-Aware Pre-Training of Compiler Intermediate Representations][research_niu_li_2024]
- [2026, NOCI-COMPILER A THEORETICAL ARCHITECTURE FOR THE SEMANTIC TRANSLATION OF NOCICEPTIVE SIGNALS INTO A DIGITAL PAIN ALPHABET][research_noci_compiler_a_2026]
- [Noguchi and others, 2021, Implementing Algebraic Effects and Handlers in Non-functional Programming Languages][research_noguchi_matsumoto_2021]
- [Norris and Pollock, 1994, Register allocation over the program dependence graph][research_norris_pollock_1994]
- [Nougrahiya and Nandivada, 2024, Homeostasis Design and Implementation of a Self-Stabilizing Compiler][research_nougrahiya_nandivada_2024]
- [Nowicki and others, 2021, Performance evaluation of Java/PCJ implementation of parallel algorithms on the cloud extended version][research_nowicki_gorski_2021]
- [Nyangaresi and Ma, 2022, A Formally Verified Message Validation Protocol for Intelligent IoT E-Health Systems][research_nyangaresi_ma_2022]
- [Oates and others, 1998, The Application of Pre-Stack Depth Migration using Topographic Analysis to Aid in the][research_oates_harinder_1998]
- [O'Callahan, 1999, A simple, comprehensive type system for Java bytecode subroutines][research_ocallahan_1999]
- [Odaira and others, 2010, Coloring-based coalescing for graph coloring register allocation][research_odaira_nakaike_2010]
- [Odegard and others, 2014, Model-Based GN and C Simulation and Flight Software Development for Orion Missions beyond LEO][research_odegardryan_milenkoviczoran_2014]
- [Oehlert and others, 2018, Mitigating Data Cache Aging through Compiler-Driven Memory Allocation][research_oehlert_luppold_2018]
- [Oh and others, 2022, CASH-RF A Compiler-Assisted Hierarchical Register File in GPUs][research_oh_jeong_2022]
- [Oh and Kim, 2026, Detecting Compiler-Introduced Security Bugs via IR Mutation and Coverage-Guided Fuzzing][research_oh_kim_2026]
- [Oh and others, 2015, Bytecode-to-C Ahead-of-Time Compilation for Android Dalvik Virtual Machine][research_oh_yeo_2015]
- [Oiwa, 2009, Implementation of the memory-safe full ANSI-C compiler][research_oiwa_2009]
- [Okasaki and others, 1994, Call-by-need and continuation-passing style][research_okasaki_lee_1994]
- [O Kim and Lee, 2026, Amortised neural acoustic tomography domain-specific encoder design and topology-dependent Eikonal analysis][research_okim_lee_2026]
- [Oliva and others, 1995, The VLISP verified PreScheme compiler][research_oliva_ramsdell_1995]
- [O'Loughlin and Gillam, 2015, Addressing Issues of Cloud Resilience, Security and Performance through Simple Detection of Co-locating Sibling Virtual Machine Instances][research_oloughlin_gillam_2015]
- [Olteanu and Oprişa, 2025, LambdaGo A Functional Extension of the Go Programming Language][research_olteanu_oprisa_2025]
- [2024, Online platform learning the Java programming language development, implementation and efficiency][research_online_platform_2024]
- [Ooashi and others, 1992, ASL program written in abstract sequential machine style and its compiler][research_ooashi_taniguchi_1992]
- [Orlic, 2010, Implementation by capture with executable UML][research_orlic_2010]
- [Orlitsky, 2002, Scalar versus vector quantization worst case analysis][research_orlitsky_2002]
- [Orlov, 2017, Program Source Code Static Analysis for Memory Access Error Detection Using Backwards Execution][research_orlov_2017]
- [Orr and Henderson, 2000, Space Shuttle Software Development and Certification][research_orrjamesk_hendersonjohnniea_2000]
- [Ortiz, 2022, Using WebAssembly to Teach Code Generation in a Compiler Design Course][research_ortiz_2022]
- [Osborne and others, 2024, Awkward Just-In-Time JIT Compilation A Developer's Experience][research_osborne_pivarski_2024]
- [Oshita and others, 2019, Improving User Experience of C Programming Language Learning System for Novices][research_oshita_kaida_2019]
- [Othman and El Ghoul, 2022, BuHamad - The first Qatari virtual interpreter for Qatari Sign Language][research_othman_elghoul_2022]
- [Ottoni, 2018, HHVM JIT a profile-guided, region-based compiler for PHP and Hack][research_ottoni_2018]
- [Ouadjaout and others, 2016, Static analysis by abstract interpretation of functional properties of device drivers in TinyOS][research_ouadjaout_mine_2016]
- [Ozdemir and others, 2022, CirC Compiler infrastructure for proof systems, software verification, and more][research_ozdemir_brown_2022]
- [Padmasudha Kannan and others, 2021, Automated high-order curved mesh generator with high-level dynamic programming language julia for photonic applications][research_padmasudhakannan_smitha_2021]
- [Painter, 1970, Effectiveness of an optimizing compiler for arithmetic expressions][research_painter_1970]
- [Pai T and others, 2020, A Systematic Literature Review of Lexical Analyzer Implementation Techniques in Compiler Design][research_pait_jayanthiladevi_2020]
- [Pałka and others, 2011, Testing an optimising compiler by generating random lambda terms][research_palka_claessen_2011]
- [Palsberg, 1992, Provably Correct Compiler Generation][research_palsberg_1992]
- [Palsberg and Schwartzbach, 1992, Binding Time Analysis Abstract Interpretation vs. Type Inference][research_palsberg_schwartzbach_1992]
- [Pan and others, 2026, A Backend-Agnostic Compiler for Approximate Query Processing with Probabilistic Tensor Algebra][research_pan_cheney_2026]
- [Pan and others, 2015, Nonvolatile main memory aware garbage collection in high-level language virtual machine][research_pan_xie_2015]
- [Pandey, 2025, Compiler Design and Its Construction][research_pandey_2025]
- [Panigrahi and Karfa, 2023, Translation Validation of Information Leakage of Compiler Optimizations][research_panigrahi_karfa_2023]
- [Panigrahi and Karfa, 2023, An Investigation into the Security of Register Allocation with Spilling and Splitting][research_panigrahi_karfa_2023_2]
- [Pankhurst, 1968, GULP---A compiler-compiler for verbal and graphic languages][research_pankhurst_1968]
- [Pant and others, 2022, Automatic Software Engineering Position Resume Screening using Natural Language Processing, Word Matching, Character Positioning, and Regex][research_pant_pokhrel_2022]
- [Papadakis and others, 2015, Trivial Compiler Equivalence A Large Scale Empirical Study of a Simple, Fast and Effective Equivalent Mutant Detection Technique][research_papadakis_jia_2015]
- [Papadimitriou and others, 2021, Automatically exploiting the memory hierarchy of GPUs through just-in-time compilation][research_papadimitriou_fumero_2021]
- [Pape and others, 2017, Adaptive just-in-time value class optimization for lowering memory consumption and improving execution time performance][research_pape_bolz_2017]
- [Paraman and Murthy, 2023, Analysis of benchmark program results of worst case execution time for multithreaded programs][research_paraman_murthy_2023]
- [Parashar and others, 2026, A Comparative Architectural and Performance Analysis of WebAssembly and JavaScript for Computationally Intensive Web Applications][research_parashar_kumawat_2026]
- [Park and others, 2005, Implementation of Worst Case Execution Time Analysis Tool For Embedded Software based on XScale Processor][research_park_choi_2005]
- [Park and others, 2023, Bespoke Virtual Machine Orchestrator An Approach for Constructing and Reconfiguring Bespoke Virtual Machine in Private Cloud Environment][research_park_jeong_2023]
- [Park and others, 2001, Register Allocation for Banked Register File][research_park_lee_2001]
- [Park and others, 2015, KJS a complete formal semantics of JavaScript][research_park_stefanescu_2015]
- [Park and others, 2018, A formal verification tool for Ethereum VM bytecode][research_park_zhang_2018]
- [Parra, 2026, SurtGIS A high-performance raster geospatial analysis library in Rust with WebAssembly and Python support][research_parra_2026]
- [Parwez and others, 2025, Signease Machine Learning Based Sign Language Interpreter][research_parwez_abrar_2025]
- [Pasareanu and others, 2009, Model Based Analysis and Test Generation for Flight Software][research_pasareanucorinas_schumannjohannm_2009]
- [Pasupuleti, 2025, AI-Guided Quantum Compiler Design Using Superalgebraic Symmetries][research_pasupuleti_2025]
- [Patel and others, 2025, SySTeC A Symmetric Sparse Tensor Compiler][research_patel_ahrens_2025]
- [Patel and Lee, 2016, Dynamic Analysis of Multi-threaded Embedded Software to Expose Atomicity Violations][research_patel_lee_2016]
- [Pathiran and Prakash, 2014, Design and implementation of a model-based PI-like control scheme in a reset configuration for stable single-loop systems][research_pathiran_prakash_2014]
- [Patterson and Ahmed, 2019, The next 700 compiler correctness theorems functional pearl][research_patterson_ahmed_2019]
- [Pattinson and Schröder, 2016, Program Equivalence is Coinductive][research_pattinson_schroder_2016]
- [Paul and others, 2020, Improving execution efficiency of just-in-time compilation based query processing on GPUs][research_paul_he_2020]
- [Pauli and Soffa, 1980, Coroutine behaviour and implementation][research_pauli_soffa_1980]
- [Paulson, 1982, A semantics-directed compiler generator][research_paulson_1982]
- [Pavlovskiy and Platov, 2025, RESEARCH ON CODE GENERATION OF C/C++ COMPILER FOR HIGH-PERFORMANCE COMPUTING IN MICROPROCESSOR SYSTEMS][research_pavlovskiy_platov_2025]
- [Payne, 1978, A formalised technique for expressing compiler exercisers][research_payne_1978]
- [Pečimúth, 2023, Remote Just-in-Time Compilation for Dynamic Languages][research_pecimuth_2023]
- [Pelsmaeker and others, 2019, Towards language-parametric semantic editor services based on declarative type system specifications][research_pelsmaeker_vanantwerpen_2019]
- [Penev and Dimitrov, 2021, Design of a Virtual Machine for Training Compilers][research_penev_dimitrov_2021]
- [Peng and others, 2004, Code sharing among states for stack-caching interpreter][research_peng_wu_2004]
- [Petchartee, 2025, A Universal Quantum Compiler GPT Multi-Framework Optimization and Translation Using Large Language Models][research_petchartee_2025]
- [Peterson and others, 2017, Addressing Global Data Dependencies in Heterogeneous Asynchronous Runtime Systems on GPUs][research_peterson_humphrey_2017]
- [Petkovski and Bradey, 2001, The success of pre-stack depth migration over the Anama structure in the Papuan Foreland Basin, PNG a case history][research_petkovski_bradey_2001]
- [Petrosino and others, 2023, Cross-Paradigm Interoperability Between Jadescript and Java][research_petrosino_monica_2023]
- [Pham and Odersky, 2024, Stack-Copying Delimited Continuations for Scala Native][research_pham_odersky_2024]
- [Phulia and others, 2020, OOElala order-of-evaluation based alias analysis for compiler optimization][research_phulia_bhagee_2020]
- [Pichler and others, 2023, Hybrid Execution Combining Ahead-of-Time and Just-in-Time Compilation][research_pichler_li_2023]
- [Pieters and others, 2017, Handlers for Non-Monadic Computations][research_pieters_schrijvers_2017]
- [PIETERS and SCHRIJVERS, 2020, Faster coroutine pipelines A reconstruction][research_pieters_schrijvers_2020]
- [Pike and others, 2012, Experience Report A Do-It-Yourself High-Assurance Compiler][research_pikelee_wegmannnis_2012]
- [Pinckney and others, 2020, Wasm/k delimited continuations for WebAssembly][research_pinckney_guha_2020]
- [Pizzolotto and Inoue, 2021, Identifying Compiler and Optimization Level in Binary Code From Multiple Architectures][research_pizzolotto_inoue_2021]
- [P. Jeannot, 1994, Robust Kirchhoff pre-stack depth imaging with semi-gridded rays][research_pjeannot_1994]
- [P. Jeannot and Berranger, 1994, Ray-mapped focusing - A migration velocity analysis for Kirchoff pre-stack depth imaging][research_pjeannot_berranger_1994]
- [Pla, 2004, Weapon System Software Technology Support WSSTS . Delivery Order 0008 Real-Time Java for Embedded Systems RTJES][research_pla_2004]
- [Plangger and Krall, 2016, Vectorization in PyPy's Tracing Just-In-Time Compiler][research_plangger_krall_2016]
- [Plasterie and Chagalov, 2006, Wave Equation versus Kirchhoff pre-stack depth migration algorithms ? An Australian case study][research_plasterie_chagalov_2006]
- [Pleban, 1979, The use of transition matrices in a recursive-descent compiler][research_pleban_1979]
- [Pleban, 1984, Compiler prototyping using formal semantics][research_pleban_1984]
- [Plishka and Ifarraguerri, 1993, Evaluation of Alsys 037 Ada Compiler][research_plishka_ifarraguerri_1993]
- [Ploensin and others, 2021, Code Transformation Impact on Compiler-based Optimization A Case Study in the CMSSW][research_ploensin_piromsopa_2021]
- [PLOTKIN, 2004, The origins of structural operational semantics][research_plotkin_2004]
- [Plotkin and Pretnar, 2008, A Logic for Algebraic Effects][research_plotkin_pretnar_2008]
- [Handlers of algebraic effects][research_plotkin_pretnar_2009]
- [Plotkin and Pretnar, 2013, Handling Algebraic Effects][research_plotkin_pretnar_2013]
- [Pockstaller and others, 2023, Comparing the Energy Consumption of WebAssembly and JavaScript in Mobile Browsers][research_pockstaller_huber_2023]
- [Poletanovic and others, 2022, Implementation of Machine Outliner for nanoMIPS in the LLVM Compiler Infrastructure][research_poletanovic_dukic_2022]
- [Polito and others, 2022, Interpreter-guided differential JIT compiler unit testing][research_polito_ducasse_2022]
- [Poonguzhali and Vinodha, 2014, IMPLEMENTATION OF ANTI-RESET WINDUP SCHEME IN PI CONTROLLER FOR SPHERICAL TANK PROCESS][research_poonguzhali_vinodha_2014]
- [Popeea and Chin, 2004, A type system for resource protocol verification and its correctness proof][research_popeea_chin_2004]
- [Porcher, 1995, Benchmarking the POMPC compiler on the Connection Machine CM-2][research_porcher_1995]
- [Posner and others, 2025, Toward Dynamic Resource Management An Asynchronous Many-Task AMT Runtime System leveraging Dynamic Processes with PSets DPP][research_posner_ellersiek_2025]
- [Postema and others, 2022, Testing a PL/I Compiler Using Precomputation-based Program Generation][research_postema_fabry_2022]
- [Pous, 2015, Coinductive techniques, from automata to coalgebra][research_pous_2015]
- [Pous, 2016, Coinduction All the Way Up][research_pous_2016]
- [Powell, 1984, A portable optimizing compiler for Modula-2][research_powell_1984]
- [Power, 2006, The Universal Algebra of Computational Effects Lawvere Theories and Monads][research_power_2006]
- [Pratt, 1997, Second Calculus of Binary Relations as a Concurrent Programming Language][research_pratt_1997]
- [Prenzel and Provost, 2017, Dynamic Software Updating of IEC 61499 Implementation Using Erlang Runtime System][research_prenzel_provost_2017]
- [Pretnar, 2014, Inferring Algebraic Effects][research_pretnar_2014]
- [Pretnar, 2015, An Introduction to Algebraic Effects and Handlers. Invited tutorial paper][research_pretnar_2015]
- [Prinz, 2023, Compilation of Distributed Programs to Services Using Multiple Programming Languages][research_prinz_2023]
- [Pritchard, 1976, A proof rule for multiple coroutine systems][research_pritchard_1976]
- [2020, Proceedings of the 2020 International Conference on Embedded Software EMSOFT][research_proceedings_of_2020]
- [2002, Proceedings Second IEEE International Workshop on Source Code Analysis and Manipulation][research_proceedings_second_2002]
- [2003, Proceedings Third IEEE International Workshop on Source Code Analysis and Manipulation][research_proceedings_third_2003]
- [Theory and practice of coroutines with snapshots][research_prokopec_2018]
- [Proy and others, 2017, Compiler-Assisted Loop Hardening Against Fault Attacks][research_proy_heydemann_2017]
- [Puchol and others, 1998, An Operational Semantics and Compiler for Real-Time Specifications1][research_puchol_stuart_1998]
- [Puffitsch, 2016, Efficient Worst-Case Execution Time Analysis of Dynamic Branch Prediction][research_puffitsch_2016]
- [Punchihewa and Wu, 2021, Safe mutation with algebraic effects][research_punchihewa_wu_2021]
- [Punnoose, 2020, Ensuring completeness of formal verification with Gap Free Verification][research_punnoose_2020]
- [Puranik, 2025, Bridging Formal Methods and Software Engineering Through a Tagless-Final Embedded DSL for Program Semantics][research_puranik_2025]
- [Puschner, 1997, Worst-Case Execution Time Analysis at Low Cost][research_puschner_1997]
- [Puschner, 1998, Worst-case execution-time analysis at low cost][research_puschner_1998]
- [Pyzik, 2023, Call-By-Name Is Just Call-By-Value with Delimited Control][research_pyzik_2023]
- [Qassir, 2025, MyDSL Front-End Compiler Design for a User-Friendly Language Supporting Hybrid Meta-Heuristics][research_qassir_2025]
- [Qian, 2000, Standard fixpoint iteration for Java bytecode verification][research_qian_2000]
- [Qian and others, 2026, Thinking Fast and Correct Automated Rewriting of Numerical Code through Compiler Augmentation][research_qian_sathia_2026]
- [Qian and others, 2025, FreeWavm Enhanced WebAssembly Runtime Fuzzing Guided by Parse Tree Mutation and Snapshot][research_qian_ying_2025]
- [Qin and others, 2026, Augmenting LLM Code Translation with Compiler Analysis for C to Triton Kernel Generation][research_qin_xia_2026]
- [Qu and others, 2023, Scope-based Compiler Differential Testing][research_qu_huang_2023]
- [2025, Quantum Software Engineering Algorithm Design, Error Mitigation, and Compiler Optimization for Fault-Tolerant Quantum Computing][research_quantum_software_2025]
- [Queiroz Junior and da Silva, 2015, Finding Good Compiler Optimization Sets - A Case-based Reasoning Approach][research_queirozjunior_dasilva_2015]
- [Queiroz Junior and others, 2020, Finding Effective Compiler Optimization Sequences A Hybrid Approach][research_queirozjunior_dasilva_2020]
- [Quiring and others, 2021, 3CPS The Design of an Environment-Focussed Intermediate Representation][research_quiring_reppy_2021]
- [Radonić and others, 2014, One solution of loop invariant code motion compiler optimisation][research_radonic_ukic_2014]
- [Radooevii and Magdalenii, 2014, Python Implementation of Source Code Generator Based on Dynamic Frames][research_radooevii_magdalenii_2014]
- [Raj, 2016, Performance analysis of different specifications of copy propagation transformation using machine SUIF compiler infrastructure][research_raj_2016]
- [Raju Cherukuri, 2024, Building Scalable Web Applications Best Practices for Backend Architecture][research_rajucherukuri_2024]
- [Ramdani and others, 2025, Pengembangan Backend Aplikasi Geoproperty dengan Golang di PT. Nerdvana Solusi Teknologi][research_ramdani_nabarian_2025]
- [Ramesh and others, 2024, ThriveJIT Dynamic Just-In-Time Compilation for Efficient Execution of Arithmetic Expressions][research_ramesh_sukanth_2024]
- [Ramkumar and Kale, 1990, A Chare kernel implementation of a parallel Prolog compiler][research_ramkumar_kale_1990]
- [Rand, 2022, Writing and verifying a Quantum optimizing compiler keynote][research_rand_2022]
- [Ranganathan and others, 2020, Hybrid Scalable Action Rule][research_ranganathan_sharma_2020]
- [Ranjan and others, 2025, ClosureX Compiler Support for Correct Persistent Fuzzing][research_ranjan_paterson_2025]
- [Ranzato, 2013, Session details Abstract interpretation][research_ranzato_2013]
- [Rao and others, 2021, SODA A Semantics-Aware Optimization Framework for Data-Intensive Applications Using Hybrid Program Analysis][research_rao_liu_2021]
- [Raskovsky, 1982, Denotational semantics as a specification of code generators][research_raskovsky_1982]
- [Rath and others, 2018, Interoperability-Guided Testing of QUIC Implementations using Symbolic Execution][research_rath_schemmel_2018]
- [Ravanbakhsh and Sankaranarayanan, 2014, Infinite horizon safety controller synthesis through disjunctive polyhedral abstract interpretation][research_ravanbakhsh_sankaranarayanan_2014]
- [Ravedutti Lucio Machado and others, 2025, P4IRS An intermediate representation and compiler for parallel and performance-portable particle simulations][research_raveduttiluciomachado_eitzinger_2025]
- [Reb and others, 2008, A JML Compiler Based on AspectJ][research_reb_lima_2008]
- [Recharla, 2025, Parallel Sparse Matrix Algorithms in OCaml v5 Implementation, Performance, and Case Studies][research_recharla_2025]
- [Reddy and others, 2026, Compiler-Assisted Instruction Fusion][research_reddy_singh_2026]
- [Refaie and Thyabat, 2015, Effect of just-in-time selling strategy on firms' performance in Jordan][research_refaie_thyabat_2015]
- [Eliminating stack overflow by abstract interpretation][research_regehr_2005]
- [Reinhardt and others, 2018, Augmenting stack overflow with API usage patterns mined from GitHub][research_reinhardt_zhang_2018]
- [Reis and others, 2017, Compiler Techniques for Efficient MATLAB to OpenCL Code Generation][research_reis_bispo_2017]
- [Reiss, 1983, Generation of Compiler Symbol Processing Mechanisms from Specifications][research_reiss_1983]
- [Reitz and Posner, 2025, Stackless vs. Stackful Coroutines A Comparative Study for RDMA-based Asynchronous Many-Task AMT Runtimes][research_reitz_posner_2025]
- [Ren and others, 2026, SpiceFuzz LLM-Based Fuzzing for Spice Circuit Simulator Tools Bug Detection][research_ren_liu_2026]
- [Reshef and Roth, 2003, Anisotropy Corrections after Pre-Stack Depth Migration][research_reshef_roth_2003]
- [Definitional interpreters for higher-order programming languages][research_reynolds_1972]
- [R. Granli, 1993, Imaging salt with pre-stack depth migration][research_rgranli_1993]
- [Ricardo and others, 2025, On the Practicality of LLM-Based Compiler Fuzzing][research_ricardo_santosjunior_2025]
- [Ricketts and others, 2015, Towards verification of hybrid systems in a foundational proof assistant][research_ricketts_malecha_2015]
- [Rinard, 2026, Testing, Credible Compilation, and Verification in the Axon Verified Compiler in Lean and Claude Code][research_rinard_2026]
- [Ritchie and others, 2005, Challenges and opportunities in pre-stack depth imaging of legacy seismic data an overthrust belt case study][research_ritchie_popovici_2005]
- [Rivera and others, 2021, An Interval Compiler for Sound Floating-Point Computations][research_rivera_franchetti_2021]
- [Rivera and others, 2022, A Compiler for Sound Floating-Point Computations using Affine Arithmetic][research_rivera_franchetti_2022]
- [Robbins, 1984, Engineering a high-capacity Pascal compiler for high performance][research_robbins_1984]
- [Roberts, 1995, 3D Post Stack Depth Migration in the UK Southern North Sea - a Case Study][research_roberts_1995]
- [Robin and Khan, 2024, An open-source P416 compiler backend for reconfigurable match-action table switches Making networking innovation accessible][research_robin_khan_2024]
- [Rodríguez and others, 2009, CPPC a compiler-assisted tool for portable checkpointing of message-passing applications][research_rodriguez_martin_2009]
- [Rodríguez and others, 2016, Proving Correctness of a Compiler Using Step-indexed Logical Relations][research_rodriguez_pagano_2016]
- [Rodriguez Ferrandez and others, 2023, Worst Case Execution Time and Power Estimation of Multicore and GPU Software A Pedestrian Detection Use Case][research_rodriguezferrandez_joveralvarez_2023]
- [Roessle and others, 2019, Formally verified big step semantics out of x86-64 binaries][research_roessle_verbeek_2019]
- [Rogers, 1993, Ada Embedded Computer Software Support AECSS][research_rogers_1993]
- [Rohr and Lindenstruth, 2017, Fast Failure Erasure Encoding Using Just in Time Compilation for CPUs, GPUs, and FPGAs][research_rohr_lindenstruth_2017]
- [Rokotyanskaya and Abramov, 2023, Studying WebAssembly and comparison of its performance with JavaScript][research_rokotyanskaya_abramov_2023]
- [Romano and Wang, 2023, When Function Inlining Meets WebAssembly Counterintuitive Impacts on Runtime Performance][research_romano_wang_2023]
- [ROMPF and AMIN, 2019, A SQL to C compiler in 500 lines of code][research_rompf_amin_2019]
- [Rong, 2009, Tree register allocation][research_rong_2009]
- [Rong and others, 2025, IRFuzzer Specialized Fuzzing for LLVM Backend Code Generation][research_rong_yu_2025]
- [Rosà and others, 2023, Automated Runtime Transition between Virtual and Platform Threads in the Java Virtual Machine][research_rosa_basso_2023]
- [Rose, 2003, Lightweight Bytecode Verification][research_rose_2003]
- [Rosenblum and others, 2010, Extracting compiler provenance from program binaries][research_rosenblum_miller_2010]
- [Rosing and others, 1990, The DINO Parallel Programming Language][research_rosing_schnabel_1990]
- [Roşu, 2018, Finite-trace linear temporal logic coinductive completeness][research_rosu_2018]
- [Rot and others, 2016, Proving language inclusion and equivalence by coinduction][research_rot_bonsangue_2016]
- [Rowland and Perugini, 2025, The Formal Semantics and Implementation of a Domain-Specific Language for Mixed-Initiative Dialogs][research_rowland_perugini_2025]
- [Roy, 2023, A Theorem Proving Approach to Programming Language Semantics][research_roy_2023]
- [Roy and others, 2019, Security Analysis and Efficient Implementation of Code-based Signature Schemes][research_roy_morozov_2019]
- [Royer, 1986, Transformations of denotational semantics in semantics directed compiler generation][research_royer_1986]
- [Royuela and others, 2015, Compiler analysis for OpenMP tasks correctness][research_royuela_ferrer_2015]
- [Ruan and Chen, 2015, Performance-to-Power Ratio Aware Virtual Machine VM Allocation in Energy-Efficient Clouds][research_ruan_chen_2015]
- [Ruberg and others, 2017, Embedded software performance estimations at different compiler optimisation levels][research_ruberg_lass_2017]
- [Ruchkin and others, 2016, Smart compiler embedded computing systems based on cluster parallelism][research_ruchkin_mahmudov_2016]
- [Ruchkin and others, 2017, Frame model of a compiler of cluster parallelism for embedded computing systems][research_ruchkin_romanchuk_2017]
- [Rudmik and Lee, 1979, Compiler design for efficient code generation and program optimization][research_rudmik_lee_1979]
- [Rudolph and Thiemann, 2010, Mnemonics type-safe bytecode generation at run time][research_rudolph_thiemann_2010]
- [1981, Ruggedized minicomputer hardware and software topics, 1981 Proceedings of the 4th ROLM MIL-SPEC Computer User's Group Conference][research_ruggedized_minicomputer_1981]
- [Rushby, 2002, Formally Verified Hardware Encapsulation Mechanism for Security, Integrity, and Safety][research_rushby_2002]
- [Russinoff, 1992, A verified prolog compiler for the Warren Abstract Machine][research_russinoff_1992]
- [Ryu and others, 2019, Toward Analysis and Bug Finding in JavaScript Web Applications in the Wild][research_ryu_park_2019]
- [S and others, 2025, Impact of Peer-Based Feedback Mechanisms on Understanding Programming Language][research_s_v_2025]
- [Sabry and Felleisen, 1992, Reasoning about programs in continuation-passing style][research_sabry_felleisen_1992]
- [Sabry and Felleisen, 1993, Reasoning about programs in continuation-passing style][research_sabry_felleisen_1993]
- [Sabry and Felleisen, 1994, Is continuation-passing useful for data flow analysis?][research_sabry_felleisen_1994]
- [Sack, 2025, Interfacing Programming Language Semantics and Pragmatics What Does "Hello, World" Mean?][research_sack_2025]
- [Sadanand Giri and others, 2024, Green threads of progress Natural fibers reshaping wastewater cleanup strategies, a review][research_sadanandgiri_subash_2024]
- [Sadasue and Isshiki, 2023, LLVM-C2RTL C/C++ Based System Level RTL Design Framework Using LLVM Compiler Infrastructure][research_sadasue_isshiki_2023]
- [Sadat, 2005, A Compiler Driven Simulation Technique for the Analysis of Digital Logic Circuit][research_sadat_2005]
- [Sager, 1985, A technique for creating small fast compiler frontends][research_sager_1985]
- [Sah and others, 2018, An Efficient Hardware-Oriented Runtime Approach for Stack-based Software Buffer Overflow Attacks][research_sah_islam_2018]
- [Sahkhar and others, 2022, Efficient Cloudlet Allocation to Virtual Machine to Impact Cloud System Performance][research_sahkhar_balabantaray_2022]
- [Sai and others, 2022, Machine learning-based malware detection using stacking of opcodes and bytecode sequences][research_sai_tyagi_2022]
- [Saieva and Kaiser, 2020, Binary Quilting to Generate Patched Executables without Compilation][research_saieva_kaiser_2020]
- [Salama and others, 2018, Online programming language-Learning management system][research_salama_qazi_2018]
- [Salánki and Sarvajcz, 2019, Development of a Gait Recognition System in NI LabVIEW Programming Language][research_salanki_sarvajcz_2019]
- [Salapura and Harper, 2015, High Performance Virtual Machine Recovery in the Cloud][research_salapura_harper_2015]
- [Salapura and Harper, 2015, Remote Restart for a High Performance Virtual Machine Recovery in a Cloud][research_salapura_harper_2015_2]
- [SALEH and SCHRIJVERS, 2016, Efficient algebraic effect handlers for Prolog][research_saleh_schrijvers_2016]
- [Salim and others, 2019, Towards a WebAssembly standalone runtime on GraalVM][research_salim_nisbet_2019]
- [Sambasivam and others, 2021, Writing P4 compiler backend for packet processing engines][research_sambasivam_subramanian_2021]
- [Samet, 1976, Compiler testing via symbolic interpretation][research_samet_1976]
- [Samet, 1977, A normal form for compiler testing][research_samet_1977]
- [Samet, 1980, A Coroutine Approach to Parsing][research_samet_1980]
- [Samiei and others, 2024, Worst-Case Execution Time Analysis of Real-Time Robotic Algorithms Using Reinforcement Learning][research_samiei_kahani_2024]
- [Sammler and others, 2022, Islaris verification of machine code against authoritative ISA semantics][research_sammler_hammond_2022]
- [Sanada, 2023, Category-Graded Algebraic Theories and Effect Handlers][research_sanada_2023]
- [SANADA, 2024, Algebraic effects and handlers for arrows][research_sanada_2024]
- [Sanders and others, 2020, Robustness Analysis of Scaled Resource Allocation Models Using the Imperial PEPA Compiler][research_sanders_srivastava_2020]
- [Sangiorgi, 2022, From enhanced coinduction towards enhanced induction][research_sangiorgi_2022]
- [Sanmorino, 2012, Development of computer assisted instruction CAI for compiler model The simulation of stack on code generation][research_sanmorino_2012]
- [Santhi and others, 2015, The Simian concept Parallel Discrete Event Simulation with interpreted languages and just-in-time compilation][research_santhi_eidenbenz_2015]
- [Santhiar and Kanade, 2017, Static deadlock detection for asynchronous C# programs][research_santhiar_kanade_2017]
- [SanthiKumar and others, 2025, Enhancing Machine Learning Performance with AI-Based Virtual Machine Load Balancing][research_santhikumar_sahayasheela_2025]
- [Santo and others, 2009, Continuation-Passing Style and Strong Normalisation for Intuitionistic Sequent Calculi][research_santo_matthes_2009]
- [Santone, 2011, Clone detection through process algebras and Java bytecode][research_santone_2011]
- [Santos and others, 2024, Assessing the Impact of Compiler Optimizations on GPUs Reliability][research_santos_carro_2024]
- [Santos and others, 2018, A memory-bounded, deterministic and terminating semantics for the synchronous programming language Céu][research_santos_lima_2018]
- [Sanusi and others, 2024, Assuring Correctness, Testing, and Verification of X-Compiler by Integrating Communicating Stream X-Machine][research_sanusi_ogunshile_2024]
- [Saraf and Dashora, 2013, An Optimal Code Heuristic Approach for Compiler Optimization using Graph Coloring Technique][research_saraf_dashora_2013]
- [Sato, 2021, Proof Assistant and Type Theory][research_sato_2021]
- [Sato and others, 2019, Combining higher-order model checking with refinement type inference][research_sato_iwayama_2019]
- [Satya Teja Muddada, 2025, Serverless 2.0 Unlocking Performance and Portability with WebAssembly][research_satyatejamuddada_2025]
- [Schäfer and others, 2016, Axiomatic semantics for compiler verification][research_schafer_schneider_2016]
- [Scheidl, 2020, Valent-Blocks Scalable High-Performance Compilation of WebAssembly Bytecode For Embedded Systems][research_scheidl_2020]
- [Schiewe, 2022, Bridging the gap between source code and high-level concepts in static code analysis][research_schiewe_2022]
- [Schkufza and others, 2019, Just-In-Time Compilation for Verilog][research_schkufza_wei_2019]
- [Schlägl and Groβe, 2025, Fast Interpreter-Based Instruction Set Simulation for Virtual Prototypes][research_schlagl_groe_2025]
- [Schlichtkrull and others, 2024, Isabelle-verified correctness of Datalog programs for program analysis][research_schlichtkrull_rydhofhansen_2024]
- [Schliephake and others, 2011, Design and Implementation of a Runtime System for Parallel Numerical Simulations on Large-Scale Clusters][research_schliephake_aguilar_2011]
- [Schmale and others, 2022, Backend compiler phases for trapped-ion quantum computers][research_schmale_temesi_2022]
- [Schmeck, 1983, Algebraic semantics of recursive flowchart schemes][research_schmeck_1983]
- [Schmidt, 2000, Abstract interpretation and program modelling][research_schmidt_2000]
- [Schmidt and Völler, 1984, A multi-language compiler system with automatically generated codegenerators][research_schmidt_voller_1984]
- [Schmidt-Schauß and Sabel, 2015, Improvements in a functional core language with call-by-need operational semantics][research_schmidtschauss_sabel_2015]
- [Schmitz, 1992, The visual compiler-compiler SIC abstract][research_schmitz_1992]
- [Schnakenbeck and others, 2023, A Control Flow based Static Analysis of GRAFCET using Abstract Interpretation][research_schnakenbeck_mross_2023]
- [Schneider and others, 2006, A Verified Compiler for Synchronous Programs with Local Declarations][research_schneider_brandt_2006]
- [Schoeberl and others, 2010, Worst-case execution time analysis for a Java processor][research_schoeberl_puffitsch_2010]
- [Schoenberger and others, 2024, Using Compiler Frameworks for the Evaluation of Hardware Design Choices in Trapped-Ion Quantum Computers][research_schoenberger_hillmich_2024]
- [Schöpp, 2017, Defunctionalisation as modular closure conversion][research_schopp_2017]
- [Schuele and Schneider, 2004, Abstraction of assembler programs for symbolic worst case execution time analysis][research_schuele_schneider_2004]
- [Schuiki and others, 2020, LLHD a multi-level intermediate representation for hardware description languages][research_schuiki_kurth_2020]
- [Schuster and others, 2020, Compiling effect handlers in capability-passing style][research_schuster_brachthauser_2020]
- [Schuster and others, 2022, A typed continuation-passing translation for lexical effect handlers][research_schuster_brachthauser_2022]
- [Schwaab and Siek, 2013, Modular type-safety proofs in Agda][research_schwaab_siek_2013]
- [Schwarcz and others, 2024, LOOL Low-Overhead, Optimization-Log-Guided Compiler Fuzzing Registered Report][research_schwarcz_berlakovich_2024]
- [Schwarz and others, 2026, TPDE A Fast Adaptable Compiler Back-End Framework][research_schwarz_kamm_2026]
- [Scott, 1986, The Interface Between Distributed Operating System and High-Level Programming Language. Revision][research_scott_1986]
- [Sculthorpe and others, 2016, A Modular Structural Operational Semantics for Delimited Continuations][research_sculthorpe_torrini_2016]
- [Seassau and others, 2025, Formal Semantics and Program Logics for a Fragment of OCaml][research_seassau_yoon_2025]
- [Segura, 2026, Algebraic effects for bounded prompt pipelines Lawvere theories, handlers, and outcome traces][research_segura_2026]
- [Seidler and others, 2026, Wasm-WCET Worst-Case Execution-Time Analysis of WebAssembly Modules on Updatable Resource-Constrained Embedded Devices][research_seidler_michelis_2026]
- [Sekiyama and Unno, 2023, Temporal Verification with Answer-Effect Modification Dependent Temporal Type-and-Effect System with Delimited Continuations][research_sekiyama_unno_2023]
- [Sen and others, 2000, Velocity analysis using pre-stack depth migration and 3D tomogrphy A case study over steeply dipping salt][research_sen_wagner_2000]
- [Seo and Kim, 2016, Measuring Method of Worst-case Execution Time by Analyzing Relation between Source Code and Executable Code][research_seo_kim_2016]
- [Seo and Kim, 2016, Operator-data type pair based execution environments independent worst-case execution time measuring method][research_seo_kim_2016_2]
- [Seo and others, 2007, Goal-directed weakening of abstract interpretation results][research_seo_yang_2007]
- [Serafin and others, 2023, Pipestitch An energy-minimal dataflow architecture with lightweight threads][research_serafin_ghosh_2023]
- [Serrano, 2021, Of JavaScript AOT compilation performance][research_serrano_2021]
- [Serrano, 2022, On JavaScript Ahead-of-Time Compilation Performance Keynote][research_serrano_2022]
- [Seshia and Rakhlin, 2009, Quantitative Analysis of Embedded Software Using Game-Theoretic Learning][research_seshia_rakhlin_2009]
- [Sethi, 1982, Control flow aspects of semantics directed compiling Summary][research_sethi_1982]
- [Translation validation for a verified OS kernel][research_sewell_2013]
- [Seyfer, 1982, Tailoring testing to a specific compiler---experiences][research_seyfer_1982]
- [Shahrokhi and others, 2023, Efficient Query Processing in Python Using Compilation][research_shahrokhi_groeger_2023]
- [Shaikhha and others, 2024, A Tensor Algebra Compiler for Sparse Differentiation][research_shaikhha_huot_2024]
- [Shan, 2007, A static simulation of dynamic delimited control][research_shan_2007]
- [Shannon 1948, A mathematical theory of communication][research_shannon_1948]
- [Sharif and others, 2022, COMPAS Compiler-assisted Software-implemented Hardware Fault Tolerance for RISC-V][research_sharif_muellergritschneder_2022]
- [Sharma, 2025, Green Threads Human Connection with Nature in Richard Powers' The Overstory][research_sharma_2025]
- [Sharma and Reddy, 2025, Analysis of FreeRTOS and Contiki Scheduler Performance with Scalable Task Loads on a Uniform Platform][research_sharma_reddy_2025]
- [Sharma and Sharma, 2024, Parameterized Static Analysis for Weak Memory Models][research_sharma_sharma_2024]
- [Sharma and others, 2023, RustSmith Random Differential Compiler Testing for Rust][research_sharma_yu_2023]
- [Sharp, 1990, Pythia A Parallel Compiler for Delirium][research_sharp_1990]
- [Sharrad and others, 2018, Delta Debugging Type Errors with a Blackbox Compiler][research_sharrad_chitil_2018]
- [Sharygin and Buchatskiy, 2017, Survey of Just-in-Time Query Compilation Methods][research_sharygin_buchatskiy_2017]
- [Shcherbakov and Shcherbakova, 2024, Comparative analysis of coroutine functionality in modern programming languages][research_shcherbakov_shcherbakova_2024]
- [Sheinidashtegol and Galloway, 2017, Performance Impact of DDoS Attacks on Three Virtual Machine Hypervisors][research_sheinidashtegol_galloway_2017]
- [Shen, 2017, Android Security via Static Program Analysis][research_shen_2017]
- [Sherman, 2018, Redesigning Soot's data-flow analysis framework for abstract interpretation][research_sherman_2018]
- [Sheth and Damevski, 2022, Grouping related stack overflow comments for software developer recommendation][research_sheth_damevski_2022]
- [Shi and others, 2008, Virtual machine showdown][research_shi_casey_2008]
- [Shih, 1998, An operational semantic approach to continuation style interpreter of logic programs][research_shih_1998]
- [Shih and Chen, 1996, Iterative Pre-Stack Depth Migration With Velocity Analysis][research_shih_chen_1996]
- [Shiina and others, 2021, Lightweight preemptive user-level threads][research_shiina_iwasaki_2021]
- [Shimchik and others, 2021, Improving Accuracy and Completeness of Source Code Static Taint Analysis][research_shimchik_ignatyev_2021]
- [Shin and others, 2004, AIRES Automatic Integration of Reusable Embedded Software, Methodologies, Toolkit, and Experiments][research_shin_wang_2004]
- [Shirai and others, 2026, Does Programming Language Matter? An Empirical Study of Fuzzing Bug Detection][research_shirai_nourry_2026]
- [Shivers, 1991, The semantics of Scheme control-flow analysis][research_shivers_1991]
- [Shobaki and others, 2022, Graph transformations for register-pressure-aware instruction scheduling][research_shobaki_bassett_2022]
- [Sholihin and Hidayati, 2024, A Forward Chaining Expert System for Personalized Programming Language Selection][research_sholihin_hidayati_2024]
- [Shoushtary and others, 2024, Memento An Adaptive, Compiler-Assisted Register File Cache for GPUs][research_shoushtary_arnau_2024]
- [Shukla and others, 2014, A Formal Approach to the Provably Correct Synthesis of Mission Critical Embedded Software for Multi Core Embedded Platforms][research_shukla_nanjundappa_2014]
- [Siambaton and others, 2024, Implementation Draft Programming Oriented Objects in Parking System Application using Language Programming Java][research_siambaton_azis_2024]
- [Sianipar and others, 2018, Virtual Machine Integrity Verification in Crowd-Resourcing Virtual Laboratory][research_sianipar_willems_2018]
- [Silva and others, 2024, Efficient Data Exchange between WebAssembly Modules][research_silva_metrolho_2024]
- [Simon and Kowalewski, 2016, Static analysis of Sequential Function Charts using abstract interpretation][research_simon_kowalewski_2016]
- [Simonnet and others, 2024, A Dependent Nominal Physical Type System for Static Analysis of Memory in Low Level Code][research_simonnet_lemerre_2024]
- [Sinharoy, 1988, EPL - Equational Programming Language Parsing and Dimension Propagation][research_sinharoy_1988]
- [Sites, 1979, Machine-independent register allocation][research_sites_1979]
- [Retrofitting effect handlers onto OCaml][research_sivaramakrishnan_2021]
- [Siveroni, 2004, Operational semantics of the Java Card Virtual Machine][research_siveroni_2004]
- [Skarman and others, 2023, Enhancing Compiler-Driven HDL Design with Automatic Waveform Analysis][research_skarman_klemmer_2023]
- [Smith and others, 2004, A generalized algorithm for graph-coloring register allocation][research_smith_ramsey_2004]
- [Smith and Zhang, 2024, A Pure Demand Operational Semantics with Applications to Program Analysis][research_smith_zhang_2024]
- [Snavely, 2011, Test and Evaluation of Architecture-Aware Compiler Environment][research_snavely_2011]
- [Snyder, 1975, A Portable Compiler for the Language C][research_snyder_1975]
- [2021, Socket system in php programming language][research_socket_system_2021]
- [Sohrabi and others, 2018, A Novel Virtual Machine Selection Policy for Virtual Machine Consolidation][research_sohrabi_ghods_2018]
- [Sokhatskyi and Maslianko, 2018, The systems engineering of consistent pure language with effect type system for certified applications and higher languages][research_sokhatskyi_maslianko_2018]
- [Soleimani and Balarostaghi, 2016, Seismic image enhancement in post stack depth migration by finite offset CDS stack method][research_soleimani_balarostaghi_2016]
- [Soluian and Lіushenko, 2025, Research of WebAssembly usage for high-performance code development in web applications][research_soluian_lushenko_2025]
- [Somani and Srivastava, 2019, Implementation of SAAS Intranet compiler in PHP][research_somani_srivastava_2019]
- [Son and Lee, 2016, A Study on the Interpreter for the Light-Weighted Virtual Machine on IoT Environments][research_son_lee_2016]
- [Son and others, 2014, A Reversing Technique for Symbol Table Verification on Compiler Constructions][research_son_oh_2014]
- [Son and others, 2017, Design and Implementation of the RSIL to LLVM IR Translator for Verification of the Intermediate Code on IoT Virtual Machine][research_son_oh_2017]
- [Song and Wang, 2021, Monadic Programming Featured Teaching Innovation of Compilation Experiments][research_song_wang_2021]
- [Sorensen and others, 2020, A simulator and compiler framework for agile hardware-software co-design evaluation and exploration][research_sorensen_manocha_2020]
- [Souha and others, 2025, Modeling and Automated Code Generation of the Backend of Tourism Applications][research_souha_ouaddi_2025]
- [Spampinato and Püschel, 2016, A basic linear algebra compiler for structured matrices][research_spampinato_puschel_2016]
- [Spivey, 2017, Faster coroutine pipelines][research_spivey_2017]
- [Squar and others, 2020, Compiler Assisted Source Transformation of OpenMP Kernels][research_squar_jammer_2020]
- [Squire and Funkhouser, 2014, "A Bit of Code" How the Stack Overflow Community Creates Quality Postings][research_squire_funkhouser_2014]
- [Srinivasan and Reps, 2015, Synthesis of machine code from semantics][research_srinivasan_reps_2015]
- [Stanisic and others, 2015, Faithful performance prediction of a dynamic task-based runtime system for heterogeneous multi-core architectures][research_stanisic_thibault_2015]
- [Stappert and Altenbernd, 2000, Complete worst-case execution time analysis of straight-line hard real-time programs][research_stappert_altenbernd_2000]
- [Stata and Abadi, 1998, A type system for Java bytecode subroutines][research_stata_abadi_1998]
- [Stata and Abadi, 1999, A type system for Java bytecode subroutines][research_stata_abadi_1999]
- [Steingartner, 2021, Compiler Module of Abstract Machine Code for Formal Semantics Course][research_steingartner_2021]
- [Stepanov and others, 2021, Type-Centric Kotlin Compiler Fuzzing Preserving Test Program Correctness by Preserving Types][research_stepanov_akhin_2021]
- [Stepanov and Itsykson, 2022, Backend Bug Finder a platform for effective compiler fuzzing][research_stepanov_itsykson_2022]
- [Stepanov and Klym, 2025, A QUANTITATIVE ANALYSIS OF WEBASSEMBLY INTEGRATION ARCHITECTURAL PATTERNS, TOOLING, AND PERFORMANCE EVALUATION][research_stepanov_klym_2025]
- [Stiévenart and others, 2022, Static stack-preserving intra-procedural slicing of webassembly binaries][research_stievenart_binkley_2022]
- [Stöhr and O'Boyle, 1998, First Fast Sink A compiler algorithm for barrier placement optimisation][research_stohr_oboyle_1998]
- [Stolyarov, 2023, STATIC ANALYZER IMPLEMENTATION MODEL FOR THE SOLIDTY PROGRAMMING LANGUAGE][research_stolyarov_2023]
- [Stoonkisto and Subhlok, 1997, Coordinating Foreign Modules with a Parallelizing Compiler][research_stoonkisto_subhlok_1997]
- [Continuations: A mathematical semantics for handling full jumps][research_strachey_1974]
- [Strauch, 2023, MRPHS A Verilog RTL to C++ Model Compiler Using Intermediate Representations for Object-oriented Model-driven Prototyping][research_strauch_2023]
- [Su and others, 2017, Automatic generation of fast BLAS3-GEMM A portable compiler approach][research_su_liao_2017]
- [Subha, 2009, A Modified Linear Scan Register Allocation Algorithm][research_subha_2009]
- [Subha, 2010, A register allocation algorithm][research_subha_2010]
- [Subramanyan, 2025, CWAMR REIMAGINING A CAPABILITYBASED WEBASSEMBLY RUNTIME VIA CHERI-BASED COMPARTMENTALIZATION][research_subramanyan_2025]
- [Suchy and others, 2020, CARAT a case for virtual memory through compiler- and runtime-based address translation][research_suchy_campanoni_2020]
- [Suetterlein and others, 2022, Extending an asynchronous runtime system for high throughput applications A case study][research_suetterlein_manzano_2022]
- [Suganuma and others, 2003, A region-based compilation technique for a Java just-in-time compiler][research_suganuma_yasue_2003]
- [Suhendra and Bachtiar, 2016, MIGRATION CODE PADA BACKEND CRIMEZONE DARI PHP KE SCALA][research_suhendra_bachtiar_2016]
- [Sukha, 2015, A Compiler-Runtime Application Binary Interface for Pipe-While Loops][research_sukha_2015]
- [SulĂ­r and Poruban, 2017, Exposing Runtime Information through Source Code Annotations][research_sular_poruban_2017]
- [Sulema and Glinskii, 2020, Semantics and pragmatics of programming language ASAMPL][research_sulema_glinskii_2020]
- [Sun and others, 2016, Finding compiler bugs via live code mutation][research_sun_le_2016]
- [Sun and others, 2016, Toward understanding compiler bugs in GCC and LLVM][research_sun_le_2016_2]
- [Sun and Staron, 2026, Agentic Pipelines in Embedded Software Engineering Emerging Practices and Challenges][research_sun_staron_2026]
- [Sun and others, 2025, Archs A WebAssembly Runtime for Cross-host Heterogeneous Computing in Serverless][research_sun_tu_2025]
- [Sun and others, 2025, Automating Target Description Processing for Efficient Compiler Backend Development][research_sun_zhong_2025]
- [Suo and others, 2024, Fuzzing MLIR Compiler Infrastructure via Operation Dependency Analysis][research_suo_chen_2024]
- [2022, Supplemental Material for A Just-in-Time Adaptive Intervention to Enhance Physical Activity in the SMARTFAMILY2.0 Trial][research_supplemental_material_2022]
- [Surakka and others, 2005, Towards compiler backend optimization for low energy consumption at instruction level][research_surakka_mikkonen_2005]
- [Surati, 1993, A Parallelizing Compiler Based on Partial Evaluation][research_surati_1993]
- [Susca and others, 2022, Worst-Case Execution Time Estimation for Numerical Controllers][research_susca_mihaly_2022]
- [Suwa and others, 2017, Verification of code generators via higher-order model checking][research_suwa_tsukada_2017]
- [S.Venkatesan, 2025, TOWARDS AUTONOMOUS CODE OPTIMIZATION A REINFORCEMENT LEARNING FRAMEWORK FOR COMPILER DESIGN][research_svenkatesan_2025]
- [Swierstra and others, 2016, A Lazy Language Needs a Lazy Type System][research_swierstra_viera_2016]
- [Swillus and Zaidman, 2023, Sentiment overflow in the testing stack Analyzing software testing posts on Stack Overflow][research_swillus_zaidman_2023]
- [The F# asynchronous programming model][research_syme_2011]
- [2026, Syntax-Directed Semantics in Programming Language Design][research_syntax_directed_semantics_2026]
- [Szydełko, 2018, BONDS BALANCE SHEET VALUATION IN AMORTISED COST CHOSEN ASPECTS][research_szydelko_2018]
- [Tabassam and Obermaisser, 2017, Class-based query-optimization for minimizing worst-case execution times of diagnostic queries in embedded real-time systems][research_tabassam_obermaisser_2017]
- [Tadepalli and others, 2003, 3D pre-stack depth imaging and well ties A case history of depth imaging in Gulf of Mexico][research_tadepalli_li_2003]
- [Taft, 2024, Sound and precise static analysis using a generalization of static single assignment and value numbering][research_taft_2024]
- [Tahat and others, 2019, Scalable Translation Validation of Unverified Legacy OS Code][research_tahat_joshi_2019]
- [Takase and others, 2018, Work-in-Progress Design Concept of a Lightweight Runtime Environment for Robot Software Components Onto Embedded Devices][research_takase_mori_2018]
- [Talaat and others, 2025, GrammLLM Grammar-Guided LLM Test Generation for Compiler Validation][research_talaat_hassan_2025]
- [Talamali and others, 2024, Formal Specification and Verification of MQTT Protocol Using CoQ Proof Assistant][research_talamali_lounas_2024]
- [Ţălu, 2025, A Comparative Study of WebAssembly Runtimes Performance Metrics, Integration Challenges, Application Domains, and Security Features][research_talu_2025]
- [Tamura and others, 2025, Bringing Together Cross-ISA Checkpoint/Restoration and AOT Compilation of WebAssembly Programs][research_tamura_kotani_2025]
- [Tan, 2009, The worst-case execution time tool challenge 2006][research_tan_2009]
- [Tan and others, 2025, The Burden of Proof Automated Tooling for Rapid Iteration on Large Mechanised Proofs][research_tan_donaldson_2025]
- [Tan and others, 2016, A new verified compiler backend for CakeML][research_tan_myreen_2016]
- [Tan and others, 2015, A verified type system for CakeML][research_tan_owens_2015]
- [Tang and others, 2019, Compiler testing a systematic literature analysis][research_tang_ren_2019]
- [Tang and others, 2010, Balanced Bipartite Graph Based Register Allocation for Network Processors in Mobile and Wireless Networks][research_tang_you_2010]
- [Tang and others, 2025, CTDip a diversity-guided test program synthesis approach for boosting compiler bug detection][research_tang_zeng_2025]
- [Tant and others, 2023, Software Compilation Using FPGA Hardware Register Allocation][research_tant_diwakar_2023]
- [Tao and others, 2010, An Automatic Testing Approach for Compiler Based on Metamorphic Testing Technique][research_tao_wu_2010]
- [TARAU, 2011, The BinProlog experience Architecture and implementation choices for continuation passing Prolog and first-class logic engines][research_tarau_2011]
- [Tardieu, 2014, Session details Compiler optimizations][research_tardieu_2014]
- [Tarjan, 1985, Amortized Computational Complexity][research_tarjan_1985]
- [Tatsuoka and Kaneko, 2018, Wire congestion aware high level synthesis flow with source code compiler][research_tatsuoka_kaneko_2018]
- [Tavares and others, 2011, Decoupled graph-coloring register allocation with hierarchical aliasing][research_tavares_colombet_2011]
- [Tempel and others, 2021, Towards Reliable Spatial Memory Safety for Embedded Software by Combining Checked C with Concolic Testing][research_tempel_herdt_2021]
- [ten Hagen and others, 1996, Codesign of a parallel architecture and an optimizing compiler backend SIN rete processing as a case study][research_tenhagen_steinberg_1996]
- [Terao, 2018, Lazy Abstraction for Higher-Order Program Verification][research_terao_2018]
- [Terci, 2023, A Learning-Based Coloring Algorithm for Register Allocation Problem][research_terci_2023]
- [Thangamani and others, 2023, Lifting Code Generation of Cardiac Physiology Simulation to Novel Compiler Technology][research_thangamani_jost_2023]
- [2015, The Deasibility and Properties of Dividing Virtual Machine Resources using the Virtual Machine Cluster as the Unit in Cloud Computing][research_the_deasibility_2015]
- [2007, The Role of Abstract Interpretation in Formal Methods][research_the_role_2007]
- [2017, The Utilization of Cloud Computing as Virtual Machine][research_the_utilization_2017]
- [Thielecke, 2003, From control effects to typed continuation passing][research_thielecke_2003]
- [Thielecke, 2012, Functional semantics of parsing actions, and left recursion elimination as continuation passing][research_thielecke_2012]
- [Thiselton and Treude, 2019, Enhancing Python Compiler Error Messages via Stack][research_thiselton_treude_2019]
- [Thomas and others, 2024, Analyzing Data Flow and Control Flow of Multicore Software A Solution for Efficient Worst-Case Execution Time Analysis][research_thomas_salehi_2024]
- [Thorpe and others, 2022, Verification of Cyber Emulation Experiments Through Virtual Machine and Host Metrics][research_thorpe_swiler_2022]
- [Thorpe and others, 2022, WiP Verification of Cyber Emulation Experiments Through Virtual Machine and Host Metrics][research_thorpe_swiler_2022_2]
- [Tian and others, 2016, Optimizing GPU Register Usage Extensions to OpenACC and Compiler Optimizations][research_tian_khaldi_2016]
- [Tian and others, 2017, LLVM Compiler Implementation for Explicit Parallelization and SIMD Vectorization][research_tian_saito_2017]
- [Tian and others, 2024, Differential testing solidity compiler through deep contract manipulation and mutation][research_tian_wang_2024]
- [Tillet and others, 2019, Triton an intermediate language and compiler for tiled neural network computations][research_tillet_kung_2019]
- [Tine and others, 2019, POSTER Tango An Optimizing Compiler for Just-In-Time RTL Simulation][research_tine_yalamanchili_2019]
- [Tinnerholm and others, 2019, Towards introducing just-in-time compilation in a Modelica compiler][research_tinnerholm_sjolund_2019]
- [Tirichine and others, 2026, A Reinforcement Learning Environment for Automatic Code Optimization in the MLIR Compiler][research_tirichine_ameur_2026]
- [Titzer, 2024, Whose Baseline Compiler is it Anyway?][research_titzer_2024]
- [Titzer, 2025, WebAssembly How Low Can a Bytecode Go?][research_titzer_2025]
- [Todoran, 2020, Metric Semantics for Concurrent Languages Designed in Continuation-Passing Style][research_todoran_2020]
- [Todoran and Ciobanu, 2025, Metric Continuation-Passing Semantics for Multiparty Interactions][research_todoran_ciobanu_2025]
- [Todoran and Papaspyrou, 2017, Concurrency Semantics in Continuation-Passing Style][research_todoran_papaspyrou_2017]
- [Tohid and others, 2018, Asynchronous Execution of Python Code on Task-Based Runtime Systems][research_tohid_wagle_2018]
- [TOKUMORI and others, 2007, Development of Metadata Generation Support System Using Compiler Compiler][research_tokumori_ono_2007]
- [Tokumoto and others, 2016, MuVM Higher Order Mutation Analysis Virtual Machine for C][research_tokumoto_yoshida_2016]
- [Tolpin and others, 2016, Design and Implementation of Probabilistic Programming Language Anglican][research_tolpin_vandemeent_2016]
- [Touzeau, 1984, A Fortran compiler for the FPS-164 scientific computer][research_touzeau_1984]
- [Tran and others, 2023, Transport Layer Security 1.0 handshake protocol formal verification case study How to use a proof script generator for existing large proof scores][research_tran_waimon_2023]
- [Trifanov and Schrijvers, 2026, Staging Effect Handlers for Modular Search][research_trifanov_schrijvers_2026]
- [Trout, 1967, A compiler---compiler system][research_trout_1967]
- [Truong and others, 2016, Latte a language, compiler, and runtime for elegant and efficient deep neural networks][research_truong_barik_2016]
- [Tsuyama and others, 2024, An Intrinsically Typed Compiler for Algebraic Effect Handlers][research_tsuyama_cong_2024]
- [Tu and others, 2022, Remgen Remanufacturing a Random Program Generator for Compiler Testing][research_tu_jiang_2022]
- [Tu and others, 2023, Detecting C++ Compiler Front-End Bugs via Grammar Mutation and Differential Testing][research_tu_jiang_2023]
- [Tuck, 1988, An Optimally Portable SIMD Single-Instruction Multiple-Data Programming Language][research_tuck_1988]
- [Turcotte and Vitek, 2019, Towards a Type System for R][research_turcotte_vitek_2019]
- [2009, Tutorial on SSA-Based Register Allocation][research_tutorial_on_2009]
- [Uddin and others, 2020, Mining API usage scenarios from stack overflow][research_uddin_khomh_2020]
- [Ueno and Ohori, 2022, Concurrent and parallel garbage collection for lightweight threads on multicore processors][research_ueno_ohori_2022]
- [Uh, 2003, Session details Compiler optimizations][research_uh_2003]
- [Upadhyaya and Rajan, 2015, Effectively mapping linguistic abstractions for message-passing concurrency to threads on the Java virtual machine][research_upadhyaya_rajan_2015]
- [Urban and others, 2025, Static analysis by abstract interpretation against data leakage in machine learning][research_urban_subotic_2025]
- [Utting and others, 2023, Differential Testing of a Verification Framework for Compiler Optimizations Case Study][research_utting_webb_2023]
- [V and others, 2019, A WEIGHTED ENSEMBLE OF AUTOMATIC ALGORITHMS FOR VIRTUAL MACHINE PERFORMANCE PREDICTION IN CLOUD][research_v_m_2019]
- [Valiron, 2022, Semantics of quantum programming languages Classical control, quantum control][research_valiron_2022]
- [VANDENBROUCKE and SCHRIJVERS, 2023, Disjunctive Delimited Control][research_vandenbroucke_schrijvers_2023]
- [Vandercammen and others, 2018, A flexible framework for studying trace-based just-in-time compilation][research_vandercammen_marr_2018]
- [van der Hoeven and Lecerf, 2021, Amortized Bivariate Multi-point Evaluation][research_vanderhoeven_lecerf_2021]
- [van Deursen, 1999, Modern Compiler Implementation in Java][research_vandeursen_1999]
- [van Rooij and Krebbers, 2025, Affect An Affine Type and Effect System][research_vanrooij_krebbers_2025]
- [van Tonder and Le Goues, 2020, Tailoring programs for static analysis via program transformation][research_vantonder_legoues_2020]
- [Vasilyev and Mutilin, 2020, Predicate Extension of Symbolic Memory Graphs for the Analysis of Memory Safety Correctness][research_vasilyev_mutilin_2020]
- [Vegdahl and Pleban, 1989, The runtime environment for Scheme, a Scheme implementation on the 88000][research_vegdahl_pleban_1989]
- [Veit and Böcskei, 2024, IFRS 9 Classification Aspects Measurement of Sustainability-Linked Loans at Amortised Cost or Fair Value][research_veit_bocskei_2024]
- [Velazquez-Rodriguez and others, 2022, Uncovering Library Features from API Usage on Stack Overflow][research_velazquezrodriguez_constantinou_2022]
- [Venkanna and others, 2018, PSO based optimization of worst-case execution time for ASIP application][research_venkanna_rao_2018]
- [Venkanna and Rao, 2018, Static Worst-Case Execution Time Optimization using DPSO for ASIP Architecture][research_venkanna_rao_2018_2]
- [VenkataKeerthy and others, 2023, RL4ReAl Reinforcement Learning for Register Allocation][research_venkatakeerthy_jain_2023]
- [Ventovaara and others, 2020, Worst-case Execution Time Estimation of Legacy Vehicular Embedded Functions An Industrial Case Study][research_ventovaara_hasanbegovic_2020]
- [Vepuri and Jiang, 2023, Performance Analysis of Virtual Machine Monitoring System][research_vepuri_jiang_2023]
- [Verdejo and Martí-Oliet, 2006, Executable structural operational semantics in Maude][research_verdejo_martioliet_2006]
- [Verma and Bakshi, 2015, Chronological Advancement in Compiler Design A Review][research_verma_bakshi_2015]
- [Verma and others, 2023, Array Bytecode Support in MicroJIT][research_verma_kaur_2023]
- [2017, Virtual Machine Consolidation using Load Balancing algorithm in Cloud Data Center][research_virtual_machine_2017]
- [VISTA RESEARCH CORP TUCSON AZ, 1994, Ada Compiler Validation Summary Report Certificate Number 940223W1. 11338 Green Hills Software, Inc. Green Hills Optimizing Ada Compiler, 1.8.7 SPARCstation 10 under SunOS, Release 4.1.3][research_vistaresearchcorptucsonaz_1994]
- [VISTA RESEARCH CORP TUCSON AZ, 1994, Ada Compiler Validation Summary Report Certificate Number 940305W1. 11335 TLD Systems, Ltd. TLD Comanche VAX/1960 Ada Compiler System, Version 4.1.1 VAX Cluster under VMS 5.5 = Tronix JIAWG Execution Vehicle i960MX under TLD Real Time Executive, Version 4.1.1][research_vistaresearchcorptucsonaz_1994_2]
- [Vizcaino and others, 2022, Acceleration with long vector architectures Implementation and evaluation of the FFT kernel on NEC SX-Aurora and RISC-V vector extension][research_vizcaino_mantovani_2022]
- [Voigt and others, 2025, Dynamic Wind for Effect Handlers][research_voigt_schuster_2025]
- [Capriccio: scalable threads for internet services][research_vonbehren_2003]
- [Vos and others, 2023, Oraqle A Depth-Aware Secure Computation Compiler][research_vos_conti_2023]
- [Vraný and Shingarov, 2024, Tinyrossa A Compiler Framework for Vertical, Verified Construction of Smalltalk VMs][research_vrany_shingarov_2024]
- [V. Samuel Blessed Nayagam and Shajin Nargunam, 2018, Secure Data Verification and Virtual Machine Monitoring][research_vsamuelblessednayagam_shajinnargunam_2018]
- [Vu, 2008, Denotational semantics for thread algebra][research_vu_2008]
- [Wagle and others, 2019, Runtime Adaptive Task Inlining on Asynchronous Multitasking Runtime Systems][research_wagle_monil_2019]
- [Wagstaff and others, 2008, Automatic Code Generation for Instrument Flight Software][research_wagstaffkiril_benowitzedward_2008]
- [Wahyudi and Miswanto, 2020, VIRTUAL MACHINE FORENSIC ANALYSIS and RECOVERY VMFAR SEBAGAI FRAMEWORK UNTUK ANALISIS BUKTI DIGITAL PADA VIRTUAL MACHINE][research_wahyudi_miswanto_2020]
- [Waites and others, 2018, A Genetic Circuit Compiler Generating Combinatorial Genetic Circuits with Web Semantics and Inference][research_waites_misirli_2018]
- [Wall, 1986, Global register allocation at link time][research_wall_1986]
- [Wall, 1988, Register windows vs. register allocation][research_wall_1988]
- [Wall, 2004, Register windows vs. register allocation][research_wall_2004]
- [Wambua, 2025, Topics, Trends, and Sentiments in Software Testing An Analysis of Developers' Engagement on Stack Overflow][research_wambua_2025]
- [Wang, 2017, Research on the Execution Time Analysis Technology of the Worst Case System in Real Time System][research_wang_2017]
- [Wang, 2019, Web Crawler Scheduler Based on Coroutine][research_wang_2019]
- [Wang, 2021, Can "micro VM" become the next generation computing platform? Performance comparison between light weight Virtual Machine, container, and traditional Virtual Machine][research_wang_2021]
- [Wang, 2021, Helper function inlining in dynamic binary translation][research_wang_2021_2]
- [Wang, 2024, Worst-Case Blocking Time Optimization in WCRT Analysis for vMPCP on Multi-Core Virtual Machines][research_wang_2024]
- [Wang and others, 2023, MLIRSmith Random Program Generation for Fuzzing MLIR Compiler Infrastructure][research_wang_chen_2023]
- [Wang and Dahl, 1971, Coroutine sequencing in a block structured environment][research_wang_dahl_1971]
- [Wang and others, 2015, WCET-Aware Energy-Efficient Data Allocation on Scratchpad Memory for Real-Time Embedded Systems][research_wang_gu_2015]
- [Wang and others, 2025, Research on Compiler Fuzzing Based on Syntax-semantics Dual-Dimensional Classification][research_wang_han_2025]
- [Wang and Huang, 2022, SGPM A coroutine framework for transaction processing][research_wang_huang_2022]
- [Wang and huang, 2022, Sgpm A Coroutine Scheduling Model for Wound-Wait Concurrency Control][research_wang_huang_2022_2]
- [Wang and others, 2014, Register allocation for hybrid register architecture in nonvolatile processors][research_wang_jia_2014]
- [Wang and Jung, 2024, Rustlantis Randomized Differential Testing of the Rust Compiler][research_wang_jung_2024]
- [Wang and others, 2019, Tracking runtime concurrent dependences in java threads using thread control profiling][research_wang_li_2019]
- [Wang and others, 2023, A General-Purpose Compiler Design for Instruction-Based AI Accelerator Implementation][research_wang_linghu_2023]
- [Wang and others, 2022, Unleashing Coveraged-Based Fuzzing Through Comprehensive, Efficient, and Faithful Exploitable-Bug Exposing][research_wang_lu_2022]
- [Wang and others, 2026, Random test generators demystified Differences and potential for compiler reliability][research_wang_lu_2026]
- [Wang and others, 2010, Stack Bound Inference for Abstract Java Bytecode][research_wang_qiu_2010]
- [Wang and others, 2020, RSDS Getting System Call Whitelist for Container Through Dynamic and Static Analysis][research_wang_shen_2020]
- [Wang and others, 2024, K-RAPID A Formal Executable Semantics of the RAPID Robot Programming Language][research_wang_wang_2024]
- [Wang and others, 2009, Reducing Code Size by Graph Coloring Register Allocation and Assignment Algorithm for Mixed-Width ISA Processor][research_wang_wu_2009]
- [Wang and others, 2023, An Automated Verification Framework for HalideIR-Based Compiler Transformations][research_wang_xie_2023]
- [Wang and Xie, 2024, Enhancing Translation Validation of Compiler Transformations with Large Language Models][research_wang_xie_2024]
- [Wang and others, 2017, Faster mutation analysis via equivalence modulo states][research_wang_xiong_2017]
- [Wang and Yang, 2014, Applied Technology in Front-End Implementation of Tiger Compiler Using Hacs Language][research_wang_yang_2014]
- [Wang and others, 2019, Reg An Ultra-Lightweight Container That Maximizes Memory Sharing and Minimizes the Runtime Environment][research_wang_zhang_2019]
- [Wang and others, 2023, A Comprehensive Study of WebAssembly Runtime Bugs][research_wang_zhou_2023]
- [Wang and Zhu, 2011, Animating the Approach of Deriving Operational Semantics from Algebraic Semantics for Web Services][research_wang_zhu_2011]
- [WanXin and others, 2022, CUDA Acceleration of Worst-Case Execution Time Analysis Based On Model Checking][research_wanxin_tao_2022]
- [Watanabe and others, 2020, Design and Preliminary Evaluation of OpenACC Compiler for FPGA with OpenCL and Stream Processing DSL][research_watanabe_lee_2020]
- [Watt, 2025, Concurrency in WebAssembly][research_watt_2025]
- [-, 2021, WebAssembly for High-Performance Web Applications A Study on Execution Speed and Efficiency][research_webassembly_for_high_performance_2021]
- [Weber and Fischer, 2020, Process-Based Simulation with Stackless Coroutines][research_weber_fischer_2020]
- [Weber and others, 2022, A closer look at process-based simulation with stackless coroutines][research_weber_wiesner_2022]
- [Wei and others, 2023, Compiling Parallel Symbolic Execution with Continuations][research_wei_jia_2023]
- [Weiner and Ramakrishman, 1988, A piggy-back compiler for Prolog][research_weiner_ramakrishman_1988]
- [Welch and others, 2017, Formalization IDEs Integrated with a Verifying Compiler][research_welch_durkee_2017]
- [Wenes and others, 1994, A Practical implementation of a 3D pre-stack depth migration algorithm][research_wenes_kremer_1994]
- [Wenger and others, 2016, A Programming Language and System for Heterogeneous Cloud of Things][research_wenger_zhu_2016]
- [Wheeler and others, 2011, Video subset selection for measurement based Worst Case Execution Time analysis][research_wheeler_bate_2011]
- [Whiteside and others, 2012, Directional Imaging Stack DIS for Shot Based Pre-stack Depth Migrations][research_whiteside_yeh_2012]
- [Wibowo and others, 2015, Unit test code generator for lua programming language][research_wibowo_hendradjaya_2015]
- [The worst-case execution-time problem: overview of methods and survey of tools][research_wilhelm_2008]
- [Williams and Bulmer, 1978, Use of a formal notation for static semantics in compiler design][research_williams_bulmer_1978]
- [Williams and Elliott, 2025, Libfork Portable Continuation-Stealing With Stackless Coroutines][research_williams_elliott_2025]
- [Williams and Roger, 2009, Test generation strategies to measure worst-case execution time][research_williams_roger_2009]
- [Wilson, 1989, Ada Compiler Validation Capability ACVC Version 1.11 Field-Test Release . ANSI][research_wilson_1989]
- [Wilson, 1989, Ada Compiler Validation Capability ACVC Version 1.11 Field-Test Release . ANSI, BACKUP, TAR][research_wilson_1989_2]
- [Wilson, 1989, Ada Compiler Validation Capability ACVC Version 1.11 Field-Test Release . BACKUP][research_wilson_1989_3]
- [Wilson, 1989, Ada Compiler Validation Capability ACVC Version 1.11 Field-Test Release . TAR][research_wilson_1989_4]
- [Wilson, 1990, Ada/Ed Compiler, Version 1.10 UNIX][research_wilson_1990]
- [Wilson, 1990, Ada/Ed Compiler, Version 1.10 VAX][research_wilson_1990_2]
- [Wimmer and others, 2017, One compiler deoptimization to optimized code][research_wimmer_jovanovic_2017]
- [Windsor and others, 2021, C4 the C compiler concurrency checker][research_windsor_donaldson_2021]
- [Woronow, 1989, Correction for a "FORTRAN program for generation of multivariate normally distributed random variables"][research_woronow_1989]
- [2016, WORST CASE EXECUTION TIME CALCULATION OF PARALLEL EMBEDDED REAL-TIME SOFTWARE][research_worst_case_2016]
- [Worthington, 2021, Reflections on a decade of MoarVM, a runtime for the Raku programming language keynote][research_worthington_2021]
- [Wu, 2023, PyTorch 2.0 The Journey to Bringing Compiler Technologies to the Core of PyTorch Keynote][research_wu_2023]
- [Wu and others, 2021, Effective Register Allocation for Configurable VLIW Crypto-Processor][research_wu_bie_2021]
- [Wu and others, 2026, Fluctuation-guided adaptive random compiler for Hamiltonian simulation][research_wu_fan_2026]
- [Wu and others, 2025, WBSan WebAssembly Bug Detection for Sanitization and Binary-Only Fuzzing][research_wu_he_2025]
- [Wu and Li, 2007, Extending Traditional Graph-Coloring Register Allocation Exploiting Meta-heuristics for Embedded Systems][research_wu_li_2007]
- [Wu and others, 2026, Reconfigurable Computing Challenge FPGA-Based WebAssembly Stack Co-Processor][research_wu_liu_2026]
- [Wu and others, 2014, Effect handlers in scope][research_wu_schrijvers_2014]
- [Wu and others, 2026, Designing quantum chemistry algorithms with just-in-time compilation][research_wu_sun_2026]
- [Wu and others, 2023, Boosting Compiler Testing via Eliminating Test Programs with Long-Execution-Time][research_wu_yang_2023]
- [Wu and others, 2017, Two Schemes to Improve the Implementation of the Aggregation Based Algebraic Multigrid Preconditioner][research_wu_yin_2017]
- [Wu and Zhang, 2012, A Model Checking Based Approach to Bounding Worst-Case Execution Time for Multicore Processors][research_wu_zhang_2012]
- [Wu and Zhang, 2013, Reducing worst-case execution time of hybrid SPM-caches][research_wu_zhang_2013]
- [Wu and Zhang, 2018, Cache-Aware SPM Allocation to Reduce Worst-Case Execution Time for Hybrid SPM-Caches][research_wu_zhang_2018]
- [Wu and others, 2025, Compiler Optimization Testing Based on Optimization-Guided Equivalence Transformations][research_wu_zheng_2025]
- [Würthinger and others, 2017, Practical partial evaluation for high-performance dynamic language runtimes][research_wurthinger_wimmer_2017]
- [Xiang and others, 2026, LoopHint A Compiler-Assisted Loop Branch Predictor for Embedded DSPs][research_xiang_xu_2026]
- [Xiao, 2021, Transformation System of two Similar Syntax Programs Based on the Compiler Principle][research_xiao_2021]
- [Xiao and others, 2023, Read-Write Dependency Aware Register Allocation][research_xiao_chen_2023]
- [Xia and DiVito, 2005, Software Certification for Temporal Properties With Affordable Tool Qualification][research_xiasongtao_divitobenedettol_2005]
- [Xie and others, 2020, Effect handlers, evidently][research_xie_brachthauser_2020]
- [Xie and others, 2022, First-class names for effect handlers][research_xie_cong_2022]
- [Xie and others, 2024, Parallel Algebraic Effect Handlers][research_xie_johnson_2024]
- [Xie and Leijen, 2020, Effect handlers in Haskell, evidently][research_xie_leijen_2020]
- [Xie and Leijen, 2021, Generalized evidence passing for effect handlers efficient compilation of effect handlers to C][research_xie_leijen_2021]
- [Xie and others, 2025, Kitten A Simple Yet Effective Baseline for Evaluating LLM-Based Compiler Testing Techniques][research_xie_xu_2025]
- [Xu and Gregg, 2015, An Efficient Vectorization Approach to Nested Thread-level Parallelism for CUDA GPUs][research_xu_gregg_2015]
- [Xu and Kjolstad, 2021, Copy-and-patch compilation a fast compilation algorithm for high-level languages and bytecode][research_xu_kjolstad_2021]
- [Xu and others, 2020, DSmith Compiler Fuzzing through Generative Deep Learning Model with Attention][research_xu_wang_2020]
- [Xu and Zhang, 2014, Formal verification of software safety criteria using Event-B][research_xu_zhang_2014]
- [Xu and others, 2024, SWAT4J Generating System Call Allowlist for Java Container Attack Surface Reduction][research_xu_zhou_2024]
- [Xu and others, 2016, CAOPLE A Programming Language for Microservices SaaS][research_xu_zhu_2016]
- [Xue and Bogdan, 2016, Scalable and realistic benchmark synthesis for efficient NoC performance evaluation][research_xue_bogdan_2016]
- [Yadav and others, 2022, DISTAL the distributed tensor algebra compiler][research_yadav_aiken_2022]
- [Yallop and others, 2018, A modular foreign function interface][research_yallop_sheets_2018]
- [Yamamoto and others, 2016, Lightweight Ruby Framework for Improving Embedded Software Efficiency][research_yamamoto_oyama_2016]
- [Yamane and others, 2020, Verification Method of Safety Properties of Embedded Assembly Program by Combining SMT-Based Bounded Model Checking and Reduction of Interrupt Handler Executions][research_yamane_kobashi_2020]
- [Yamato, 2015, Automatic verification for plural virtual machines patches][research_yamato_2015]
- [Yan and Zhang, 2008, Analyzing the worst-case execution time for instruction caches with prefetching][research_yan_zhang_2008]
- [Yaneva and others, 2017, Compiler-assisted test acceleration on GPUs for embedded software][research_yaneva_rajan_2017]
- [Finding and understanding bugs in C compilers][research_yang_2011]
- [Yang, 2018, Formal Process Virtual Machine for Smart Contracts Verification][research_yang_2018]
- [Yang and others, 2025, Formal Verification of a Custom Compiler for a Fully Homomorphic Encryption Accelerator][research_yang_banerjee_2025]
- [Yang and others, 2015, Towards a verified compiler prototype for the synchronous language SIGNAL][research_yang_bodeveix_2015]
- [Yang and others, 2024, WhiteFox White-Box Compiler Fuzzing Empowered by Large Language Models][research_yang_deng_2024]
- [Yang and Duan, 2008, Operational semantics of Framed Tempura][research_yang_duan_2008]
- [Yang and Ruiz Varela, 2015, Qualifying non-volatile register files for embedded systems through compiler-directed write minimization and balancing][research_yang_ruizvarela_2015]
- [Yang and others, 2022, Simulink Model Static Analysis Results based on Abstract Interpretation][research_yang_wang_2022]
- [Ye and Delaware, 2019, A verified protocol buffer compiler][research_ye_delaware_2019]
- [Ye and others, 2023, A Generative and Mutational Approach for Synthesizing Bug-Exposing Test Cases to Guide Compiler Fuzzing][research_ye_hu_2023]
- [Ye and others, 2025, BazzAFL Moving Fuzzing Campaigns Towards Bugs via Grouping Bug-Oriented Seeds][research_ye_zhu_2025]
- [Yesua and others, 2019, Keamanan Penggunaan Propofol Auto-Coinduction Dibandingkan Dengan Midazolam Coinduction Berdasarkan Perubahan Hemodinamik Pada Induksi Anestesi Pasien Yang Dilakukan General Anestesi][research_yesua_rahardjo_2019]
- [Yi, 2011, Automated programmable control and parameterization of compiler optimizations][research_yi_2011]
- [Yi and others, 2026, Understanding and Finding JIT Compiler Performance Bugs][research_yi_ding_2026]
- [Yi and Lee, 2018, An Educational System Design to Support Learning Transfer from Block-based Programming Language to Text-based Programming Language][research_yi_lee_2018]
- [Yildiz and others, 2019, Software UART A Use Case for VSCPU Worst-Case Execution Time Analyzer][research_yildiz_iskender_2019]
- [Yilmazer‐Metin, 2021, sRSP An efficient and scalable implementation of remote scope promotion][research_yilmazermetin_2021]
- [Yim and others, 2019, Implementation of Targeted Advertisement Services on ATSC 3.0 Runtime Environment][research_yim_kim_2019]
- [Yin and others, 2020, The Implementation of Simple Smart Contract Language and Its Compiler Based on Ethereum Platform][research_yin_pan_2020]
- [Yoo and Kim, 2017, Coroutine based Algorithms for reducing Memory overhead in Virtual Reality][research_yoo_kim_2017]
- [Yoshikawa and others, 2003, Random program generator for Java JIT compiler test system][research_yoshikawa_shimura_2003]
- [Yoshioka and others, 2024, Abstracting Effect Systems for Algebraic Effect Handlers][research_yoshioka_sekiyama_2024]
- [You and Chen, 2015, Vector-aware register allocation for GPU shader processors][research_you_chen_2015]
- [You and Lu, 2012, A markup language for java bytecode][research_you_lu_2012]
- [YU, 2008, Design and implementation of NC code compiler based on ANTLR][research_yu_2008]
- [Yu, 2009, Scalable Services Orchestration with Continuation-Passing Messaging][research_yu_2009]
- [Yu, 2023, Reasoning about MLIR Semantics through Effects and Handlers][research_yu_2023]
- [Yu and Cohen, 2015, Guided Test Generation for Finding Worst-Case Stack Usage in Embedded Systems][research_yu_cohen_2015]
- [Yu and Haque, 2011, Decentralised web-services orchestration with continuation-passing messaging][research_yu_haque_2011]
- [Yu and Yang, 2007, Continuation-passing enactment of distributed recoverable workflows][research_yu_yang_2007]
- [Yu and others, 2023, Efficient Generation of Floating-Point Inputs for Compiler-Induced Variability][research_yu_yi_2023]
- [Yvon and Feeley, 2021, A small scheme VM, compiler, and REPL in 4k][research_yvon_feeley_2021]
- [Zaitsev and Guliaiev, 2011, Stack E6 and Its Implementation within Linux Kernel][research_zaitsev_guliaiev_2011]
- [Zakowski and others, 2020, An equational theory for weak bisimulation via generalized parameterized coinduction][research_zakowski_he_2020]
- [Zaks and Pnueli, 2008, Program analysis for compiler validation][research_zaks_pnueli_2008]
- [Zanardini, 2008, The Semantics of Abstract Program Slicing][research_zanardini_2008]
- [Zapanov, 2025, Foreign Function Interface for Managed Runtime Systems with Lightweight Threading][research_zapanov_2025]
- [Zaytsev, 2018, An industrial case study in compiler testing tool demo][research_zaytsev_2018]
- [Zaytsev, 2020, Modelling of Language Syntax and Semantics The Case of the Assembler Compiler][research_zaytsev_2020]
- [Zelenova, 2025, Static Memory Layout for Real-Time Operating Systems][research_zelenova_2025]
- [Zelkowitz, 1975, Third generation compiler design][research_zelkowitz_1975]
- [Zendra and Colnet, 2001, Coping with aliasing in the GNU Eiffel Compiler implementation][research_zendra_colnet_2001]
- [Zeng and others, 2026, TypeNFuzz Dynamic Type-aware Object Dependence Graph-Guided Fuzzing for JavaScript Library Bug Discovery][research_zeng_wu_2026]
- [Zhang, 2016, Selection and Improvement of Computer Programming Language][research_zhang_2016]
- [Zhang, 2018, Compiler Practice System Integrated with Real Open Source Compiler][research_zhang_2018]
- [Zhang, 2025, Comparative Implementation of Binary Tree and Recursive Backtracking Maze Generation Algorithms in OCaml][research_zhang_2025]
- [Zhang and others, 2022, Cape compiler-aided program transformation for HTM-based cache side-channel defense][research_zhang_bond_2022]
- [Zhang and others, 1993, Pipelined processors and worst case execution times][research_zhang_burns_1993]
- [Zhang and others, 2023, Characterizing and Detecting WebAssembly Runtime Bugs][research_zhang_cao_2023]
- [Zhang and Deng, 2018, A Depth Variant Seismic Wavelets Extraction Method for Inversion of Post-Stack Depth Domain Seismic Data][research_zhang_deng_2018]
- [Zhang and others, 2026, GeoIR-Compiler A Geospatial Intermediate Representation and Compilation Framework for Chinese Urban Spatial Question Answering][research_zhang_deng_2026]
- [Zhang and others, 2026, Transformation-Recipe-Based FPGA Synthesis Compiler Testing][research_zhang_jiang_2026]
- [Zhang and Koutsoukos, 2015, Improving the Precision of Abstract Interpretation Based Cache Persistence Analysis][research_zhang_koutsoukos_2015]
- [Zhang and others, 2019, SNC A Cloud Service Platform for Symbolic-Numeric Computation Using Just-In-Time Compilation][research_zhang_liu_2019]
- [Zhang and Meng, 2020, Design and Implementation of Multi-core DSP Parallel Compiler Based on Otsu Method][research_zhang_meng_2020]
- [Zhang and Myers, 2019, Abstraction-safe effect handlers via tunneling][research_zhang_myers_2019]
- [Zhang and others, 2011, A Case Study of Pre-stack Depth Migration Application over a Salt Dome Area][research_zhang_ping_2011]
- [Zhang and others, 2025, Refactoring for Java-Structured Concurrency][research_zhang_shen_2025]
- [Zhang and others, 2017, Skeletal program enumeration for rigorous compiler testing][research_zhang_sun_2017]
- [Zhang and others, 2016, Compiler Transformation to Generate Hybrid Sparse Computations][research_zhang_venkat_2016]
- [Zhang and others, 2017, Weak Memory Models Balancing Definitional Simplicity and Implementation Flexibility][research_zhang_vijayaraghavan_2017]
- [Zhang and others, 2013, Register Allocation by Incremental Graph Colouring for Clustered VLIW Processors][research_zhang_wu_2013]
- [Zhang and others, 2026, LLM-Powered Silent Bug Fuzzing in Deep Learning Libraries via Versatile and Controlled Bug Transfer][research_zhang_xiao_2026]
- [Zhang and others, 2023, Compiler Technologies in Deep Learning Co-Design A Survey][research_zhang_xing_2023]
- [Zhang and Yan, 2009, Accurately Estimating Worst-Case Execution Time for Multi-core Processors with Shared Direct-Mapped Instruction Caches][research_zhang_yan_2009]
- [Zhang and Yin, 2021, A Virtual Machine Placement Strategy Based on Virtual Machine Selection and Integration][research_zhang_yin_2021]
- [Zhang and others, 2024, Introducing Compiler Semantics into Large Language Models as Programming Language Translators A Case Study of C to x86 Assembly][research_zhang_zhao_2024]
- [Zhang and others, 2026, LEGO-compiler enhancing neural compilation through translation composability][research_zhang_zhao_2026]
- [Zhang and others, 2020, A Dynamic Instruction Cache Locking Approach for Minimizing Worst Case Execution Time of a Single Task][research_zhang_zheng_2020]
- [Zhao and others, 2025, Thread-sensitive fuzzing for concurrency bug detection][research_zhao_fu_2025]
- [Zhao and others, 2024, Design and Implementation of the MTP Compiler][research_zhao_he_2024]
- [Zhao and others, 2026, QuaMap A Multi-Backend Benchmark Dataset for Quantum Circuit Mapping and Learning-Based Compiler Evaluation][research_zhao_li_2026]
- [Zhao and others, 2024, COPS A Coroutine-Based Priority Scheduling Framework Perceived by the Operating System][research_zhao_liao_2024]
- [Zhao and others, 2021, Similarity-Aware Architecture/Compiler Co-Designed Context-Reduction Framework for Modulo-Scheduled CGRA][research_zhao_sheng_2021]
- [Zhao and others, 2024, Wapplique Testing WebAssembly Runtime via Execution Context-Aware Bytecode Mutation][research_zhao_zeng_2024]
- [Zhao and others, 2021, Hot question prediction in Stack Overflow][research_zhao_zhang_2021]
- [Zheng and Xia, 2019, Exploring mixed integer programming reformulations for virtual machine placement with disk anti-colocation constraints][research_zheng_xia_2019]
- [Zhong, 2022, Enriching Compiler Testing with Real Program from Bug Report][research_zhong_2022]
- [Zhong and others, 2023, Neural Network Guided Evolutionary Fuzzing for Finding Traffic Violations of Autonomous Vehicles][research_zhong_kaiser_2023]
- [Zhong and others, 2026, A Multi-Modal Retrieval-Augmented Framework for Compiler Backend Generation with LLMs][research_zhong_lv_2026]
- [Zhong and others, 2024, ComBack A Versatile Dataset for Enhancing Compiler Backend Development Efficiency][research_zhong_lyu_2024]
- [Zhong and others, 2026, Towards Fully Automated Compiler Backend Generation with Multi-Agent Systems How Far Are We?][research_zhong_qiu_2026]
- [Zhong and others, 2026, BePilot An AI Programming Assistant for Compiler Backend Development][research_zhong_sun_2026]
- [Zhou, 1996, Parameter passing and control stack management in Prolog implementation revisited][research_zhou_1996]
- [Zhou and others, 2024, C-CORE Clustering by Code Representation to Prioritize Test Cases in Compiler Testing][research_zhou_jiang_2024]
- [Zhou and others, 2016, Worst case response time and schedulability analysis for real-time software transactional memory-lazy conflict detection STM-LCD][research_zhou_li_2016]
- [Zhou and Mu, 2016, Representative Virtual Machine Templates An optimized virtual machine templates management mechanism for an Cloud system based on K-medoids Clustering][research_zhou_mu_2016]
- [Zhou and others, 2020, Design and Implementation of Coroutine Scheduling System on SW26010][research_zhou_wu_2020]
- [Zhou and Xue, 2016, A Compiler Approach for Exploiting Partial SIMD Parallelism][research_zhou_xue_2016]
- [Zhu, 2001, Denotational semantics of programming languages and compiler generation in PowerEpsilon][research_zhu_2001]
- [Zhu and others, 2007, Algebraic Approach to Operational Semantics and Observation-Oriented Semantics for a Timed Shared-Variable Language with Probability][research_zhu_he_2007]
- [Zhu and others, 2008, From algebraic semantics to denotational semantics for Verilog][research_zhu_he_2008]
- [Zhu and others, 2019, Learning to Restrict Test Range for Compiler Test][research_zhu_wang_2019]
- [Zhu and others, 2025, Emerging Compiler Testing Based on Test Case Reuse][research_zhu_wang_2025]
- [Zhu and Xie, 2025, A Domain-Specific Compiler for Embedded DSP Development Based on Component Code Generation Architecture and Correctness][research_zhu_xie_2025]
- [Zhu and others, 2009, Animating the Link Between Operational Semantics and Algebraic Semantics for a Probabilistic Timed Shared-Variable Language][research_zhu_yang_2009]
- [Zhu and others, 2012, Linking operational semantics and algebraic semantics for a probabilistic timed shared-variable language][research_zhu_yang_2012]
- [Zhu and others, 2009, Locality-Based Normal Form Approach to Linking Algebraic Semantics and Operational Semantics for an Event-Driven System-Level Language][research_zhu_zhao_2009]
- [Zolda and others, 2011, Context-Sensitive Measurement-Based Worst-Case Execution Time Estimation][research_zolda_bunte_2011]
- [Zolduoarrati and others, 2025, A cross-continental analysis of how regional cues shape top stack overflow contributors][research_zolduoarrati_licorish_2025]
- [Zou and others, 2022, Buddy Stacks Protecting Return Addresses with Efficient Thread-Local Storage and Runtime Re-Randomization][research_zou_wang_2022]
- [Zou and others, 2017, Towards comprehending the non-functional requirements through Developers' eyes An exploration of Stack Overflow using topic analysis][research_zou_xu_2017]
- [Zubarev, 2017, TYPE ANALYSIS FOR THE PREDICATE PROGRAMMING LANGUAGE][research_zubarev_2017]
- [Zuepke and Kaiser, 2019, Deterministic Futexes Addressing WCET and Bounded Interference Concerns][research_zuepke_kaiser_2019]
- [Zúñiga and Bel-Enguix, 2020, Coinductive Natural Semantics for Compiler Verification in Coq][research_zuniga_belenguix_2020]
- [Zwanziger, 2019, Dependently-Typed Montague Semantics in the Proof Assistant Agda-flat][research_zwanziger_2019]
- [Zyuzin and Nanevski, 2021, Contextual modal types for algebraic effects and handlers][research_zyuzin_nanevski_2021]

[research_2018_proceedings_2018]: https://doi.org/10.1109/emsoft.2018.8537228
[research_3d_pre_stack_2002]: https://doi.org/10.1002/cjg2.237
[research_a_compositional_2012]: https://doi.org/10.5220/0004097300150026
[research_a_fibrational_2020]: https://doi.org/10.17559/tv-20191130092745
[research_a_s_2024]: https://doi.org/10.55041/ijsrem37614
[research_a_structural_2004]: https://doi.org/10.1016/j.jlap.2004.05.001
[research_abdallah_2018]: https://doi.org/10.1016/j.ijar.2018.10.012
[research_abdelmaksoud_hammadeh_2023]: https://doi.org/10.23919/date56975.2023.10137253
[research_abdulaziz_koller_2022]: https://doi.org/10.1609/aaai.v36i9.21197
[research_abdulsalam_lakomski_2014]: https://doi.org/10.1109/igcc.2014.7039169
[research_abe_2019]: https://doi.org/10.1145/3357390.3361021
[research_abella_padilla_2017]: https://doi.org/10.1145/3065924
[research_abikaram_sarkar_2023]: https://doi.org/10.1109/iccad57390.2023.10323650
[research_abrahams_1979]: https://doi.org/10.1145/800229.806960
[research_abramsky_horsman_2015]: https://doi.org/10.4204/eptcs.195.1
[research_abuyosef_kong_2025]: https://doi.org/10.1145/3708493.3712690
[research_aceto_fokkink_2004]: https://doi.org/10.1016/j.jlap.2004.03.010
[research_achour_benattou_2018]: https://doi.org/10.1109/cist.2018.8596397
[research_achour_chouenyib_2018]: https://doi.org/10.14257/ijseia.2018.12.2.01
[research_acun_chandrasekar_2019]: https://doi.org/10.1109/igsc48788.2019.8957174
[research_adajointprogramofficearlingtonva_1988]: https://doi.org/10.21236/ada204645
[research_adajointprogramofficearlingtonva_1988_2]: https://doi.org/10.21236/ada205959
[research_adajointprogramofficearlingtonva_1988_3]: https://doi.org/10.21236/ada205958
[research_adajointprogramofficearlingtonva_1988_4]: https://doi.org/10.21236/ada205908
[research_adajointprogramofficearlingtonva_1989]: https://doi.org/10.21236/ada210406
[research_adajointprogramofficearlingtonva_1989_2]: https://doi.org/10.21236/ada209882
[research_adajointprogramofficearlingtonva_1989_3]: https://doi.org/10.21236/ada209883
[research_adajointprogramofficearlingtonva_1989_4]: https://doi.org/10.21236/ada209881
[research_adajointprogramofficearlingtonva_1989_5]: https://doi.org/10.21236/ada210423
[research_adajointprogramofficearlingtonva_1990]: https://doi.org/10.21236/ada228614
[research_adajointprogramofficearlingtonva_1991]: https://doi.org/10.21236/ada246532
[research_adajointprogramofficearlingtonva_1992]: https://doi.org/10.21236/ada257705
[research_adaptive_programming_2023]: https://doi.org/10.48009/3_iis_2023_119
[research_affeldt_cohen_2023]: https://doi.org/10.1145/3573105.3575691
[research_agathos_dimakopoulos_2022]: https://doi.org/10.1016/j.parco.2022.102895
[research_agathos_hadjidoukas_2011]: https://doi.org/10.1109/pci.2011.34
[research_ahead_of_time_and_just_in_time_2023]: https://doi.org/10.18137/rnu.v9187.23.04.p.171
[research_ahman_staton_2013]: https://doi.org/10.1016/j.entcs.2013.09.007
[research_aigrain_graham_1984]: https://doi.org/10.1145/502874.502876
[research_aissa_grimaud_2007]: https://doi.org/10.1109/rtcsa.2007.24
[research_aisyiyah_eviyanti_2026]: https://doi.org/10.58905/saga.v3i1.476
[research_akanbi_ajose_2022]: https://doi.org/10.14445/23497157/ijres-v9i3p101
[research_akdur_demirors_2017]: https://doi.org/10.1109/seaa.2017.13
[research_akdur_garousi_2017]: https://doi.org/10.1109/meco.2017.7977123
[research_alatawi_miller_2016]: https://doi.org/10.1145/2896971.2896980
[research_albataineh_reynolds_2015]: https://doi.org/10.1007/s00165-015-0340-4
[research_albert_correas_2024]: https://doi.org/10.1145/3650212.3680352
[research_aldweesh_alharby_2021]: https://doi.org/10.1016/j.peva.2020.102168
[research_alexander_black_2016]: https://doi.org/10.1145/3012408.3012417
[research_ali_bilgis_2025]: https://doi.org/10.56553/popets-2025-0102
[research_ali_chen_2025]: https://doi.org/10.1002/cpe.70421
[research_aljaafari_menezes_2022]: https://doi.org/10.1109/access.2022.3223359
[research_alkhalid_labiche_2018]: https://doi.org/10.5220/0006917104150422
[research_alladi_ros_2026]: https://doi.org/10.1109/cgo68049.2026.11395226
[research_allamanis_sutton_2013]: https://doi.org/10.1109/msr.2013.6624004
[research_allen_malaguti_2000]: https://doi.org/10.3997/2214-4609-pdb.28.l42
[research_alpay_heuveline_2022]: https://doi.org/10.1145/3529538.3529556
[research_alpay_heuveline_2023]: https://doi.org/10.1145/3585341.3585351
[research_altan_2026]: https://doi.org/10.62802/w6gg1c44
[research_altassan_ahmad_2024]: https://doi.org/10.53894/ijirss.v7i2.2956
[research_amaliah_musu_2021]: https://doi.org/10.1109/icoris52787.2021.9649465
[research_amarasinghe_2004]: https://doi.org/10.1145/3244311
[research_amarasinghe_2019]: https://doi.org/10.1145/3302516.3307361
[research_amarasinghe_2020]: https://doi.org/10.1145/3372799.3397167
[research_amato_meo_2020]: https://doi.org/10.1016/j.tcs.2020.02.021
[research_ambal_lenglet_2022]: https://doi.org/10.1145/3551357.3551384
[research_amin_ramzy_2016]: https://doi.org/10.1109/mtv.2016.22
[research_analysis_on_2022]: https://doi.org/10.47939/et.v3i5(10).09
[research_analytics_of_2016]: https://doi.org/10.21275/v5i4.nov162978
[research_anderson_loginov_2013]: https://doi.org/10.1109/ths.2013.6699090
[research_anderton_2022]: https://doi.org/10.1145/3517428.3563373
[research_andradeguzman_hernandezquiroz_2020]: https://doi.org/10.1093/jigpal/jzaa007
[research_andrews_henry_1988]: https://doi.org/10.1145/960116.54001
[research_aneesh_saumik_2024]: https://doi.org/10.1109/icccnt61001.2024.10724220
[research_anier_2008]: https://doi.org/10.1109/bec.2008.4657511
[research_antoniadis_feng_2021]: https://doi.org/10.1109/mwscas47672.2021.9531908
[research_aparanji_radhasundari_2017]: https://doi.org/10.18410/jebmh/2017/1138
[research_appel_1992]: https://doi.org/10.1017/CBO9780511609619
[research_appel_jim_1989]: https://doi.org/10.1145/75277.75303
[research_appel_shao_1992]: https://doi.org/10.1007/bf01807505
[research_applis_gissurarson_2025]: https://doi.org/10.1109/icst62969.2025.10988920
[research_aquino_denaro_2018]: https://doi.org/10.1109/issre.2018.00019
[research_arakaki_hirokawa_2026]: https://doi.org/10.1109/acdsa67686.2026.11468027
[research_arcaro_silva_2020]: https://doi.org/10.1109/rtss49844.2020.00016
[research_arceri_mastroeni_2019]: https://doi.org/10.4204/eptcs.299.5
[research_arendsee_2026]: https://doi.org/10.7717/peerj-cs.3435
[research_aristizabal_biernacki_2017]: https://doi.org/10.23638/lmcs-13(3:27)2017
[research_arnstrom_broman_2024]: https://doi.org/10.1109/tac.2024.3395521
[research_arriaga_barbosa_2026]: https://doi.org/10.46586/tches.v2026.i3.744-768
[research_art_an_2003]: https://doi.org/10.3745/kipsta.2003.10a.4.295
[research_asadollah_sundmark_2018]: https://doi.org/10.1109/ispdc2018.2018.00032
[research_asai_2002]: https://doi.org/10.1145/509799.503034
[research_asai_2004]: https://doi.org/10.1145/1014007.1014009
[research_asai_fujii_2025]: https://doi.org/10.1145/3759427.3760364
[research_askim_brandsbergdahl_2004]: https://doi.org/10.3997/2214-4609-pdb.3.p205
[research_astarte_2025]: https://doi.org/10.3390/philosophies10040090
[research_ataei_manohar_2019]: https://doi.org/10.1109/async.2019.00009
[research_atapattu_1994]: https://doi.org/10.21236/ada284924
[research_attrapadung_hanaoka_2018]: https://doi.org/10.1145/3196494.3196552
[research_attrot_zago_2026]: https://doi.org/10.1145/3777905
[research_auchterlonie_vinje_2007]: https://doi.org/10.3997/2214-4609.20146495
[research_audrito_haures_2023]: https://doi.org/10.1145/3605159.3605857
[research_auguston_berzins_2001]: https://doi.org/10.21236/ada529617
[research_aung_lam_2011]: https://doi.org/10.1109/socc.2011.6085116
[research_auslander_hopkins_1982]: https://doi.org/10.1145/800230.806977
[research_austen_krishnamurthi_2025]: https://doi.org/10.1145/3759429.3762621
[research_automatic_port_2019]: https://doi.org/10.14529/jsfi190303
[research_avanzini_barthe_2021]: https://doi.org/10.1145/3473592
[research_avigad_donnelly_2007]: https://doi.org/10.1145/1297658.1297660
[research_avigad_goldberg_2025]: https://doi.org/10.1007/s10817-025-09723-y
[research_avigad_holzl_2017]: https://doi.org/10.1007/s10817-017-9404-x
[research_avvenuti_bernardeschi_2003]: https://doi.org/10.1145/966051.966055
[research_azeemi_2006]: https://doi.org/10.1109/icet.2006.335979
[research_aziz_labiche_2026]: https://doi.org/10.1145/3811257.3811263
[research_azmi_2025]: https://doi.org/10.30574/gjeta.2025.24.3.0284
[research_azzahra_mulyatno_2020]: https://doi.org/10.23960/jge.v4i1.6
[research_badler_1996]: https://doi.org/10.21236/ada396354
[research_baek_kim_2017]: https://doi.org/10.1007/s10586-017-1113-z
[research_baek_lee_2024]: https://doi.org/10.1016/j.softx.2024.101810
[research_baev_2009]: https://doi.org/10.1109/cgo.2009.31
[research_baggett_2000]: https://doi.org/10.1006/jfan.1999.3551
[research_baghdadi_ray_2019]: https://doi.org/10.1109/cgo.2019.8661197
[research_bai_ming_2025]: https://doi.org/10.1109/iscas56072.2025.11043756
[research_bailinsydney_paterrafrank_1993]: https://ntrs.nasa.gov/citations/19930016789
[research_baird_johnson_1977]: https://doi.org/10.21236/ada046600
[research_baird_oliver_1977]: https://doi.org/10.21236/ada039740
[research_baltes_diehl_2018]: https://doi.org/10.1007/s10664-018-9650-5
[research_baltes_treude_2019]: https://doi.org/10.1109/msr.2019.00038
[research_balu_saraswathi_2014]: https://doi.org/10.5120/18771-0075
[research_banerjee_karfa_2018]: https://doi.org/10.1145/3172871.3180078
[research_bansal_singh_2011]: https://doi.org/10.5120/3062-4182
[research_bao_tavarageri_2014]: https://doi.org/10.1109/icppw.2014.64
[research_baradaran_huang_2026]: https://doi.org/10.1109/saner67736.2026.00029
[research_barai_santhi_2023]: https://doi.org/10.1145/3631882.3631885
[research_baramashetru_giannini_2025]: https://doi.org/10.22152/programming-journal.org/2025/10/18
[research_barany_2018]: https://doi.org/10.1145/3178372.3179521
[research_barash_shchur_2013]: https://doi.org/10.1016/j.cpc.2013.04.007
[research_barbosa_kannwischer_2025]: https://doi.org/10.1145/3719027.3765218
[research_barbuti_cataudella_2004]: https://doi.org/10.1145/967900.967991
[research_barbuti_tesei_2002]: https://doi.org/10.1145/568760.568826
[research_bardonek_zachariasova_2026]: https://doi.org/10.1016/j.micpro.2026.105300
[research_barinov_kashkarov_2020]: https://doi.org/10.1109/ispras51486.2020.00009
[research_baroffio_reghenzani_2023]: https://doi.org/10.1145/3587135.3589944
[research_barriere_blazy_2021]: https://doi.org/10.1145/3434327
[research_barriere_blazy_2023]: https://doi.org/10.1145/3571202
[research_barthe_blazy_2017]: https://doi.org/10.1109/csf.2017.16
[research_bartlett_bate_2010]: https://doi.org/10.1109/tc.2010.59
[research_bartsch_wilhelm_2021]: https://doi.org/10.1109/itc50571.2021.00057
[research_basin_friedrich_2003]: https://doi.org/10.1023/a:1025059508087
[research_baskaran_pradelle_2016]: https://doi.org/10.1109/espt.2016.009
[research_basold_geuvers_2016]: https://doi.org/10.1145/2933575.2934514
[research_bassil_2019]: https://doi.org/10.14445/22315381/ijett-v67i3p219
[research_basu_hall_2015]: https://doi.org/10.1109/ipdps.2015.103
[research_basu_williams_2017]: https://doi.org/10.1016/j.parco.2017.04.002
[research_bate_kazakov_2008]: https://doi.org/10.1109/cec.2008.4631277
[research_battle_feng_2022]: https://doi.org/10.1109/vis54862.2022.00009
[research_bau_mine_2022]: https://doi.org/10.1145/3520313.3534660
[research_bauckholt_holz_2024]: https://doi.org/10.1145/3678722.3685531
[research_bauer_pretnar_2014]: https://doi.org/10.2168/lmcs-10(4:9)2014
[research_bauer_pretnar_2015]: https://doi.org/10.1016/j.jlamp.2014.02.001
[research_bauml_brada_2011]: https://doi.org/10.1016/j.entcs.2011.02.002
[research_bavera_bonelli_2008]: https://doi.org/10.1145/1363686.1363776
[research_bayer_bigelow_1968]: https://doi.org/10.21236/ad0692681
[research_bayley_shiel_2005]: https://doi.org/10.1016/j.entcs.2005.02.029
[research_beaumont_eyrauddubois_2018]: https://doi.org/10.1002/cpe.4502
[research_becker_chakraborty_2018]: https://doi.org/10.1145/3207719.3207739
[research_becker_metta_2018]: https://doi.org/10.1007/s10009-018-0497-2
[research_bee_bernardo_2018]: https://doi.org/10.14569/ijacsa.2018.090105
[research_bekiris_2021]: https://doi.org/10.2139/ssrn.3803796
[research_belyaev_shimchik_2018]: https://doi.org/10.1134/s036176881806004x
[research_benitomontoro_chen_2021]: https://doi.org/10.1109/siie53363.2021.9583625
[research_benzaken_contejean_2019]: https://doi.org/10.1145/3293880.3294107
[research_bera_miranda_2016]: https://doi.org/10.5381/jot.2016.15.2.a1
[research_berdine_ohearn_2002]: https://doi.org/10.1023/a:1020891112409
[research_berg_yernaux_2025]: https://doi.org/10.5220/0013472000003932
[research_berger_briles_2025]: https://doi.org/10.1145/3763147
[research_berger_spreen_2016]: https://doi.org/10.4115/jla.2016.8.3
[research_berghofer_strecker_2004]: https://doi.org/10.1016/s1571-0661(05)82598-8
[research_berlakovich_schwarcz_2026]: https://doi.org/10.1145/3807508
[research_berlakovich_schwarcz_2026_2]: https://doi.org/10.1145/3806058
[research_bernardeschi_defrancesco_2004]: https://doi.org/10.1002/spe.611
[research_bernardeschi_francesco_2008]: https://doi.org/10.1145/1452044.1452047
[research_bernardeschi_lettieri_2006]: https://doi.org/10.1093/comjnl/bxh161
[research_bernat_burns_2000]: https://doi.org/10.1016/s1474-6670(17)39931-7
[research_berten_chang_2009]: https://doi.org/10.1109/rtcsa.2009.27
[research_bertholon_chargueraud_2024]: https://doi.org/10.1145/3652588.3663320
[research_bertrane_cousot_2010]: https://doi.org/10.2514/6.2010-3385
[research_bertrane_cousot_2015]: https://doi.org/10.1561/2500000002
[research_besson_blazy_2018]: https://doi.org/10.1007/s10817-018-9496-y
[research_besson_dang_2019]: https://doi.org/10.1109/csf.2019.00023
[research_bezrak_przylucki_2020]: https://doi.org/10.35784/jcsi.1572
[research_bhamidipati_vemuri_2023]: https://doi.org/10.1109/vlsid57277.2023.00046
[research_bhasker_1988]: https://doi.org/10.1145/44304.44313
[research_bhoyar_jain_2025]: https://doi.org/10.1109/access65134.2025.11135621
[research_bhushan_yadav_2020]: https://doi.org/10.1016/j.procs.2020.03.183
[research_bicarregui_hoare_2006]: https://doi.org/10.1007/s00165-005-0079-4
[research_bierman_2012]: https://doi.org/10.1007/978-3-642-31057-7_12
[research_biernacki_danvy_2005]: https://doi.org/10.7146/brics.v12i16.21882
[research_biernacki_danvy_2005_2]: https://doi.org/10.7146/brics.v12i5.21871
[research_biernacki_danvy_2005_3]: https://doi.org/10.7146/brics.v12i10.21876
[research_biernacki_danvy_2006]: https://doi.org/10.7146/brics.v13i15.21920
[research_biernacki_danvy_2006_2]: https://doi.org/10.1017/s0956796805005782
[research_biernacki_danvy_2015]: https://doi.org/10.1145/2794078
[research_biernacki_lenglet_2019]: https://doi.org/10.23638/lmcs-15(2:18)2019
[research_biernacki_pirog_2017]: https://doi.org/10.1145/3158096
[research_bik_koanantakool_2022]: https://doi.org/10.1145/3544559
[research_biradar_dhikale_2026]: https://doi.org/10.55248/gengpi.07.0626.16a13
[research_bird_1982]: https://doi.org/10.1145/872726.806979
[research_bishnu_bhatia_2018]: https://doi.org/10.1109/ants.2018.8710145
[research_bispo_cardoso_2016]: https://doi.org/10.1002/spe.2408
[research_blaak_vancutsem_2026]: https://doi.org/10.1145/3801119.3801125
[research_blanc_kadobayashi_2010]: https://doi.org/10.1145/1930286.1930298
[research_blass_philippsen_2019]: https://doi.org/10.1145/3302516.3307352
[research_blazy_2020]: https://doi.org/10.1145/3411506.3417601
[research_blazy_2023]: https://doi.org/10.1145/3573105.3579107
[research_blazy_maroneze_2015]: https://doi.org/10.1145/2676724.2693169
[research_blieberger_2002]: https://doi.org/10.1023/a:1014535317056
[research_blower_1984]: https://doi.org/10.1145/502874.502899
[research_bockisch_taentzer_2020]: https://doi.org/10.5381/jot.2020.19.3.a13
[research_boda_chunduri_2026]: https://doi.org/10.1145/3771775.3786271
[research_bodin_jensen_2015]: https://doi.org/10.1145/2676724.2693174
[research_boding_1996]: https://doi.org/10.1190/1.1826252
[research_bodwin_bradley_1982]: https://doi.org/10.1145/800230.806997
[research_bohme_moskal_2009]: https://doi.org/10.1007/s10817-009-9142-9
[research_bohnet_dollner_2007]: https://doi.org/10.1109/vissof.2007.4290719
[research_boldo_jourdan_2013]: https://doi.org/10.1109/arith.2013.30
[research_bonar_liffick_1987]: https://doi.org/10.21236/ada218940
[research_bonchi_pous_2015]: https://doi.org/10.1145/2713167
[research_bond_2013]: https://doi.org/10.1145/3264366
[research_bonkowski_gentleman_1979]: https://doi.org/10.1145/800229.806958
[research_bonyun_1979]: https://doi.org/10.21236/ada068542
[research_bonyun_holt_1978]: https://doi.org/10.21236/ada061052
[research_boo_lee_2025]: https://doi.org/10.1109/access.2025.3596641
[research_book_bratman_1963]: https://doi.org/10.21236/ad0296834
[research_boonriong_zetzsche_2025]: https://doi.org/10.1109/icst62969.2025.10988954
[research_bosse_2018]: https://doi.org/10.1016/j.promfg.2018.06.005
[research_bounding_the_worst_case_2013]: https://doi.org/10.4156/aiss.vol5.issue10.111
[research_bounpaserth_2026]: https://doi.org/10.69692/sujmrd1202275
[research_bourke_2021]: https://doi.org/10.1145/3486605.3487187
[research_bourke_brun_2017]: https://doi.org/10.1145/3062341.3062358
[research_bourke_brun_2018]: https://doi.org/10.1145/3207719.3207732
[research_bourke_brun_2019]: https://doi.org/10.1145/3371112
[research_bourke_jeanmaire_2025]: https://doi.org/10.1109/lics65433.2025.00052
[research_bowman_ahmed_2018]: https://doi.org/10.1145/3192366.3192372
[research_boyapati_2004]: https://doi.org/10.1145/3244314
[research_brachthauser_schuster_2018]: https://doi.org/10.1145/3276481
[research_brachthauser_schuster_2020]: https://doi.org/10.1145/3428194
[research_brachthauser_schuster_2020_2]: https://doi.org/10.1017/s0956796820000027
[research_brady_2013]: https://doi.org/10.1145/2544174.2500581
[research_brady_hammond_2006]: https://doi.org/10.1145/1173706.1173724
[research_brandner_jordan_2014]: https://doi.org/10.1016/j.cl.2014.09.001
[research_brant_sunkara_2025]: https://doi.org/10.1109/ccnc54725.2025.10976036
[research_breitner_2015]: https://doi.org/10.1145/2887747.2804312
[research_brennan_rosner_2020]: https://doi.org/10.1109/sp40000.2020.00007
[research_briggs_cooper_1994]: https://doi.org/10.1145/177492.177575
[research_brock_ding_2018]: https://doi.org/10.1145/3178372.3179523
[research_brodersen_1994]: https://doi.org/10.21236/ada285395
[research_bruno_jovanovic_2021]: https://doi.org/10.1145/3453483.3454034
[research_bruza_2016]: https://doi.org/10.1016/j.jmp.2016.06.006
[research_bryant_nawrocki_2025]: https://doi.org/10.1613/jair.1.15958
[research_buchwald_lohner_2016]: https://doi.org/10.1145/2892208.2892211
[research_bulej_zheng_2016]: https://doi.org/10.1145/3012408.3012409
[research_bunkenburg_wu_2024]: https://doi.org/10.1145/3677999.3678279
[research_bur_marussy_2021]: https://doi.org/10.1145/3471904
[research_burdy_pavlova_2006]: https://doi.org/10.1145/1141277.1141708
[research_burgholzer_haag_2026]: https://doi.org/10.23919/date69613.2026.11539504
[research_burn_1990]: https://doi.org/10.1145/96709.96724
[research_burroughs_2016]: https://doi.org/10.1002/spe.2393
[research_bushnelldavidhenry_pasareanucorina_2008]: https://ntrs.nasa.gov/citations/20090026335
[research_butlerrickyw_johnsonsallyc_1993]: https://ntrs.nasa.gov/citations/20040129612
[research_butterfield_woodcock_2006]: https://doi.org/10.1016/j.entcs.2006.04.026
[research_c_compiler_2017]: https://doi.org/10.24001/ijaems.icsesd2017.58
[research_caamano_guelton_2018]: https://doi.org/10.1145/3191697.3191725
[research_cabrera_perkins_1992]: https://doi.org/10.1071/eg992043
[research_cabreraarteaga_monperrus_2019]: https://doi.org/10.1145/3358504.3361228
[research_caldwell_chiba_2017]: https://doi.org/10.1145/3170492.3136057
[research_caliskan_yamaguchi_2018]: https://doi.org/10.14722/ndss.2018.23304
[research_callahan_koblenz_1991]: https://doi.org/10.1145/113446.113462
[research_calzarossa_massari_2001]: https://doi.org/10.1016/s0167-739x(01)00049-8
[research_cambier_qian_2020]: https://doi.org/10.1109/pawatm51920.2020.00007
[research_cambou_2017]: https://doi.org/10.1109/sai.2017.8252190
[research_cameleer_a_2022]: https://doi.org/10.32907/ro-130-2767435612
[research_campbell_2019]: https://doi.org/10.1103/physrevlett.123.070503
[research_campbell_beck_1965]: https://doi.org/10.21236/ad0465805
[research_camposlopez_wannenwetsch_2016]: https://doi.org/10.5220/0005759800760083
[research_canedo_abderazek_2009]: https://doi.org/10.1016/j.micpro.2008.09.001
[research_carlosparadis_ivanperez_2025]: https://ntrs.nasa.gov/citations/20250006564
[research_carlotto_beloki_2016]: https://doi.org/10.63317/5k2zxvthjp7h
[research_carminati_starke_2017]: https://doi.org/10.1016/j.aci.2017.03.002
[research_carminati_starke_2018]: https://doi.org/10.1007/s11241-018-9306-y
[research_carney_labaugh_1983]: https://doi.org/10.2514/6.1983-2379
[research_carter_1982]: https://doi.org/10.1007/bf00264435
[research_carvalho_ferreira_2019]: https://doi.org/10.1504/ijguc.2019.099685
[research_cassola_talagorria_2020]: https://doi.org/10.1145/3427081.3427084
[research_castagna_duboc_2023]: https://doi.org/10.22152/programming-journal.org/2024/8/4
[research_castaneda_rodriguez_2023]: https://doi.org/10.1145/3583668.3594563
[research_castaneda_rodriguez_2026]: https://doi.org/10.1145/3777409
[research_castrolopez_vegalopez_2019]: https://doi.org/10.1109/cgo.2019.8661199
[research_cattell_newcomer_1979]: https://doi.org/10.1145/800229.806955
[research_cazzola_olivares_2015]: https://doi.org/10.1109/compsac.2015.82
[research_cenggiap_erviana_2023]: https://doi.org/10.32877/bt.v6i1.893
[research_chaitin_1982]: https://doi.org/10.1145/872726.806984
[research_chaitin_2004]: https://doi.org/10.1145/989393.989403
[research_chaliasos_sotiropoulos_2022]: https://doi.org/10.1145/3519939.3523427
[research_chalin_2007]: https://doi.org/10.1109/icse.2007.9
[research_chalin_2010]: https://doi.org/10.1109/tse.2009.59
[research_chaplygin_2025]: https://doi.org/10.21869/2223-1560-2025-29-3-99-112
[research_charmanas_georgiou_2026]: https://doi.org/10.1016/j.infsof.2025.107969
[research_chase_2005]: https://doi.org/10.1145/3249493
[research_chatterjee_2013]: https://doi.org/10.21236/ad1000607
[research_chaumette_ly_2011]: https://doi.org/10.1109/icnss.2011.6059958
[research_chavanon_besson_2024]: https://doi.org/10.1145/3636501.3636954
[research_chawla_goyal_2024]: https://doi.org/10.21474/ijar01/19924
[research_cheatham_standish_1970]: https://doi.org/10.1145/800028.808482
[research_chen_2018]: https://doi.org/10.1145/3183440.3183456
[research_chen_2020]: https://doi.org/10.1145/3363562
[research_chen_fan_2025]: https://doi.org/10.1145/3729375
[research_chen_ge_2007]: https://doi.org/10.1109/tase.2007.19
[research_chen_lin_2016]: https://doi.org/10.2991/cetcu-15.2016.12
[research_chen_liu_2022]: https://doi.org/10.23919/jcc.2022.08.009
[research_chen_ma_2020]: https://doi.org/10.1145/3324884.3416570
[research_chen_suo_2022]: https://doi.org/10.1145/3508362
[research_chen_wang_2010]: https://doi.org/10.2316/p.2010.726-026
[research_chen_yuan_2009]: https://doi.org/10.1109/dbta.2009.104
[research_chen_zhang_2020]: https://doi.org/10.1002/cpe.6048
[research_chen_zhu_2024]: https://doi.org/10.1145/3649834
[research_chen_zong_2016]: https://doi.org/10.1109/bdcloud-socialcom-sustaincom.2016.77
[research_cheng_2023]: https://doi.org/10.1109/dsa59317.2023.00096
[research_cheng_monahan_2016]: https://doi.org/10.1007/s10270-016-0553-x
[research_cheng_wu_2026]: https://doi.org/10.1109/access.2026.3681804
[research_cheng_wu_2026_2]: https://doi.org/10.1145/3797874
[research_chenzhao_yunzhixue_2009]: https://doi.org/10.1109/iwast.2009.5069039
[research_chernenko_anureev_2021]: https://doi.org/10.1109/edm52169.2021.9507628
[research_chhak_tolmach_2021]: https://doi.org/10.1145/3437992.3439929
[research_chi_1994]: https://doi.org/10.1109/icpp.1994.71
[research_chi_li_2009]: https://doi.org/10.1109/cis.2009.193
[research_chichereau_vialle_2024]: https://doi.org/10.1109/qce60285.2024.10295
[research_ching_1986]: https://doi.org/10.1147/rd.306.0594
[research_ching_katz_1993]: https://doi.org/10.1145/166197.166205
[research_chirila_sora_2024]: https://doi.org/10.1109/saci60582.2024.10619722
[research_chlipala_2010]: https://doi.org/10.1145/1707801.1706312
[research_chlipala_2015]: https://doi.org/10.1145/3264293
[research_chmiel_spinolo_2022]: https://doi.org/10.1075/tcb.00068.chm
[research_cho_2016]: https://doi.org/10.1007/s00354-016-0204-3
[research_cho_lee_2022]: https://doi.org/10.1145/3519939.3523718
[research_choi_han_2006]: https://doi.org/10.1145/1132462.1132467
[research_choi_hong_2019]: https://doi.org/10.1145/3338840.3355690
[research_choi_jeon_2026]: https://doi.org/10.1038/s41598-026-45837-y
[research_choi_kwon_2018]: https://doi.org/10.1109/emsoft.2018.8537214
[research_choi_park_2024]: https://doi.org/10.1109/ictc62082.2024.10827129
[research_choi_shull_2019]: https://doi.org/10.1145/3314221.3314587
[research_chong_franklin_2017]: https://doi.org/10.1038/nature23459
[research_christodorescu_jha_2006]: https://doi.org/10.21236/ada449067
[research_christopher_hatcher_1984]: https://doi.org/10.1145/502874.502877
[research_chudnov_kuan_2014]: https://doi.org/10.1109/csf.2014.12
[research_chungseo_kim_2023]: https://doi.org/10.32604/csse.2023.035064
[research_ciaffaglione_2016]: https://doi.org/10.1016/j.scico.2016.02.004
[research_ciesko_roussel_2023]: https://doi.org/10.2172/2564061
[research_cieszewski_2025]: https://doi.org/10.24425/ijet.2025.156531
[research_ck_2022]: https://doi.org/10.22214/ijraset.2022.43930
[research_clerc_2016]: https://doi.org/10.1017/s0956796816000095
[research_clinger_1984]: https://doi.org/10.1145/800055.802052
[research_clopper_pearson_1934]: https://doi.org/10.1093/biomet/26.4.404
[research_coglio_2003]: https://doi.org/10.1002/cpe.714
[research_coglio_2004]: https://doi.org/10.1002/cpe.798
[research_colin_puaut_2000]: https://doi.org/10.1023/a:1008149332687
[research_colombet_boissinot_2011]: https://doi.org/10.1145/2038698.2038708
[research_colvin_hayes_2011]: https://doi.org/10.1016/j.jlap.2011.05.001
[research_comparative_study_2016]: https://doi.org/10.21275/v5i3.nov161797
[research_compiler_technology_1998]: https://doi.org/10.1016/s0898-1221(98)90103-1
[research_cong_asai_2023]: https://doi.org/10.1145/3571786.3573015
[research_consel_chengkhoo_1993]: https://doi.org/10.1016/0167-6423(93)90011-d
[research_conway_1963]: https://doi.org/10.1145/366663.366704
[research_coppo_ferrari_1993]: https://doi.org/10.1016/0304-3975(93)90086-9
[research_cordes_falk_2009]: https://doi.org/10.1109/cgo.2009.17
[research_correnson_finkbeiner_2025]: https://doi.org/10.1145/3704889
[research_corrias_pisu_2026]: https://doi.org/10.5220/0014597200004061
[research_corrodi_heussner_2018]: https://doi.org/10.1007/s00165-017-0443-1
[research_cortesi_2008]: https://doi.org/10.1109/sefm.2008.20
[research_cortesi_file_1991]: https://doi.org/10.1145/115866.115872
[research_cortesi_file_1997]: https://doi.org/10.1145/239912.239914
[research_corti_gross_2004]: https://doi.org/10.1145/1017753.1017797
[research_costa_deoliveira_2021]: https://doi.org/10.1109/sbesc53686.2021.9628230
[research_costagliola_deufemia_2007]: https://doi.org/10.1016/j.jvlc.2006.06.002
[research_couch_hamm_1977]: https://doi.org/10.1109/mc.1977.315872
[research_cousot_1977]: https://doi.org/10.1145/512950.512973
[research_cousot_1996]: https://doi.org/10.1145/242224.242433
[research_cousot_1997]: https://doi.org/10.1145/251595.251601
[research_cousot_2015]: https://doi.org/10.1109/tase.2015.29
[research_cousot_2015_2]: https://doi.org/10.1145/2790449.2790451
[research_cousot_cousot_1995]: https://doi.org/10.1145/224164.224199
[research_cousot_cousot_2000]: https://doi.org/10.1145/325694.325699
[research_cousot_cousot_2001]: https://doi.org/10.1016/s1571-0661(04)80954-x
[research_cousot_cousot_2002]: https://doi.org/10.1145/565816.503290
[research_cousot_cousot_2011]: https://doi.org/10.1016/j.tcs.2011.06.005
[research_cousot_cousot_2012]: https://doi.org/10.1145/2103656.2103687
[research_cousot_cousot_2014]: https://doi.org/10.1145/2535838.2537850
[research_cowan_graham_1970]: https://doi.org/10.1145/800028.808481
[research_coward_constantinides_2023]: https://doi.org/10.1145/3589250.3596144
[research_crobinson_ptung_1994]: https://doi.org/10.3997/2214-4609.201409800
[research_cruttwell_gallagher_2021]: https://doi.org/10.4204/eptcs.333.20
[research_cummins_petoumenos_2018]: https://doi.org/10.1145/3213846.3213848
[research_cummins_seeker_2025]: https://doi.org/10.1145/3708493.3712691
[research_cunha_silva_2024]: https://doi.org/10.1145/3687997.3695638
[research_curry_2023]: https://doi.org/10.2172/2463070
[research_curtis_grissom_2018]: https://doi.org/10.1145/3168826
[research_czajka_2020]: https://doi.org/10.23638/lmcs-16(1:31)2020
[research_czajka_2020_2]: https://doi.org/10.23638/lmcs-16(1:11)2020
[research_dagnino_2020]: https://doi.org/10.23638/lmcs-15(1:26)2019
[research_dagnino_2021]: https://doi.org/10.46298/lmcs-17(4:2)2021
[research_daiss_diehl_2023]: https://doi.org/10.1145/3585341.3585354
[research_dakkak_wickhamjones_2020]: https://doi.org/10.1145/3368826.3377913
[research_dallapreda_giacobazzi_2005]: https://doi.org/10.1109/sefm.2005.13
[research_dams_gerth_1997]: https://doi.org/10.1145/244795.244800
[research_dange_mundre_2023]: https://doi.org/10.55248/gengpi.234.4.38226
[research_danvy_filinski_1990]: https://doi.org/10.1145/91556.91622
[research_danvy_nielsen_2001]: https://doi.org/10.1145/773184.773202
[research_das_ahmad_2020]: https://doi.org/10.1109/llvmhpchipar51896.2020.00008
[research_dasgupta_park_2019]: https://doi.org/10.1145/3314221.3314601
[research_dave_dikshit_2016]: https://doi.org/10.1109/vlsi-dat.2016.7482553
[research_davenport_1995]: https://doi.org/10.21236/ada300020
[research_de_pellissier_2021]: https://doi.org/10.1145/3479394.3479402
[research_debenham_westlake_2014]: https://doi.org/10.1071/eg12085
[research_deblaere_verstappe_2021]: https://doi.org/10.1109/et52713.2021.9580074
[research_debnath_jenkins_2024]: https://doi.org/10.1109/sp54263.2024.00220
[research_debosschere_tarau_1994]: https://doi.org/10.1145/326619.326786
[research_debray_1995]: https://doi.org/10.1145/215465.215571
[research_debuhr_zhang_2017]: https://doi.org/10.1109/ipdpsw.2017.88
[research_deferriere_janin_2026]: https://doi.org/10.1109/cgo68049.2026.11395204
[research_defrancesco_lettieri_2010]: https://doi.org/10.1016/j.tcs.2010.01.026
[research_dejtrakulwong_mavko_2013]: https://doi.org/10.1190/segam2013-0385.1
[research_delaet_blazy_2025]: https://doi.org/10.1145/3756907.3756926
[research_delgadoperez_segura_2019]: https://doi.org/10.1145/3297280.3297499
[research_deluca_chen_2017]: https://doi.org/10.1109/isads.2017.32
[research_delvadovirseda_2021]: https://doi.org/10.1145/3456565.3460041
[research_delvadovirseda_2023]: https://doi.org/10.5220/0011709800003470
[research_demacedo_abreu_2021]: https://doi.org/10.1109/asew52652.2021.00056
[research_demacedo_abreu_2022]: https://doi.org/10.1109/ict4s55073.2022.00014
[research_demmler_katzenbeisser_2021]: https://doi.org/10.5220/0010540504440451
[research_demoura_2009]: https://doi.org/10.1145/1462166.1462167
[research_deng_he_2026]: https://doi.org/10.3390/electronics15143234
[research_deng_namjoshi_2018]: https://doi.org/10.1007/s10703-017-0313-8
[research_denis_jeannot_2023]: https://doi.org/10.1002/cpe.7920
[research_deniz_2007]: https://doi.org/10.21236/ada633428
[research_denneyewen_fischerbernd_2005]: https://ntrs.nasa.gov/citations/20050241794
[research_denneyewen_fischerbernd_2009]: https://ntrs.nasa.gov/citations/20100023347
[research_denzler_fruhwirth_2021]: https://doi.org/10.1109/isorc52013.2021.00019
[research_depaula_ierusalimschy_2022]: https://doi.org/10.1145/3561320.3561321
[research_derakhshan_zhang_2023]: https://doi.org/10.1109/csf57540.2023.00021
[research_deransart_1979]: https://doi.org/10.1093/comjnl/22.3.240
[research_desai_2009]: https://doi.org/10.1109/iadcc.2009.4809056
[research_deutsch_1995]: https://doi.org/10.1145/215465.215594
[research_development_of_2023]: https://doi.org/10.36652/0869-4931-2023-77-12-567-570
[research_devilhena_pottier_2021]: https://doi.org/10.1145/3434314
[research_devries_gupta_2009]: https://doi.org/10.1145/1554339.1554342
[research_devries_gupta_2009_2]: https://doi.org/10.1145/1667209.1667212
[research_dewerra_eisenbeis_1999]: https://doi.org/10.1016/s0166-218x(99)00105-5
[research_diamantopoulos_ringlein_2020]: https://doi.org/10.1109/fpl50879.2020.00058
[research_dickerson_srinivasan_2026]: https://doi.org/10.1145/3797265
[research_dico_tatasutabri_2025]: https://doi.org/10.36050/8y461v31
[research_diehl_marcello_2021]: https://doi.org/10.1109/mcse.2021.3073626
[research_dilavore_defelice_2025]: https://doi.org/10.46298/lmcs-21(3:18)2025
[research_dimovski_2021]: https://doi.org/10.1145/3486609.3487202
[research_dimovski_2025]: https://doi.org/10.1145/3742876.3742884
[research_ding_chen_2022]: https://doi.org/10.1145/3498730
[research_ding_li_2025]: https://doi.org/10.1109/qrs-c65679.2025.00099
[research_ding_zhang_2010]: https://doi.org/10.1109/tc.2010.44
[research_dinikeev_2025]: https://doi.org/10.18127/j20700814-202505-02
[research_dipierro_sotin_2008]: https://doi.org/10.1016/j.entcs.2008.11.017
[research_dissegna_logozzo_2016]: https://doi.org/10.1145/2853131
[research_ditu_2015]: https://doi.org/10.1109/cscs.2015.38
[research_dixon_1982]: https://doi.org/10.1145/947886.947889
[research_djalali_aljedaani_2025]: https://doi.org/10.3390/software4040027
[research_dobravec_2018]: https://doi.org/10.15546/aeei-2018-0028
[research_dold_henke_2003]: https://doi.org/10.1142/s0129054103001947
[research_domagala_vanamstel_2016]: https://doi.org/10.1145/2892208.2892219
[research_donaldson_clayton_2023]: https://doi.org/10.1109/icst57152.2023.00042
[research_donaldson_sheth_2024]: https://doi.org/10.1109/icst60714.2024.00044
[research_donegan_noonan_1979]: https://doi.org/10.1145/872732.806954
[research_dong_2013]: https://doi.org/10.4028/www.scientific.net/amm.462-463.1036
[research_dong_2015]: https://doi.org/10.1109/cicn.2015.263
[research_dong_2018]: https://doi.org/10.1504/ijcse.2018.091782
[research_dong_wang_2011]: https://doi.org/10.3724/sp.j.1001.2010.03709
[research_dong_wu_2026]: https://doi.org/10.1145/3808288
[research_donohoe_1987]: https://doi.org/10.21236/ada200608
[research_doronin_2019]: https://doi.org/10.5593/sgem2019/2.1/s07.070
[research_downen_ariola_2014]: https://doi.org/10.1017/s0956796813000312
[research_downen_ariola_2025]: https://doi.org/10.1017/s0956796825100026
[research_downen_maurer_2016]: https://doi.org/10.1145/3022670.2951931
[research_drechsler_schnieber_2023]: https://doi.org/10.1109/ises58672.2023.00012
[research_drescher_engelke_2024]: https://doi.org/10.1145/3640537.3641567
[research_dsilva_payer_2015]: https://doi.org/10.1109/spw.2015.33
[research_du_2026]: https://doi.org/10.54097/b1m57229
[research_dubach_cavazos_2007]: https://doi.org/10.1145/1242531.1242553
[research_duhamel_pillement_2024]: https://doi.org/10.1109/access.2024.3507376
[research_duhoux_mens_2019]: https://doi.org/10.1145/3340671.3343357
[research_dutu_guiman_2026]: https://doi.org/10.5220/0015065300004088
[research_dybvig_2007]: https://doi.org/10.1017/S0956796807006259
[research_e_2020]: https://doi.org/10.5373/jardcs/v12sp4/20201515
[research_eachempati_jun_2010]: https://doi.org/10.1145/2020373.2020386
[research_edalat_pattinson_2007]: https://doi.org/10.1016/j.jlap.2007.01.002
[research_efficiency_asynchronous_application_2016]: https://doi.org/10.18372/2073-4751.1.10367
[research_efficient_implementation_2015]: https://doi.org/10.21275/v4i11.nov151091
[research_efthymiou_lazzarin_2022]: https://doi.org/10.22331/q-2022-09-22-814
[research_egreteau_thierry_2005]: https://doi.org/10.3997/2214-4609-pdb.1.p023
[research_eichenberger_davidson_1995]: https://doi.org/10.1109/micro.1995.476825
[research_eisl_2015]: https://doi.org/10.1145/2814189.2814199
[research_eisl_grimmer_2016]: https://doi.org/10.1145/2972206.2972211
[research_eisl_leopoldseder_2018]: https://doi.org/10.1145/3237009.3237010
[research_electronicsystemsdivhanscomafbma_1970]: https://doi.org/10.21236/ad0711370
[research_elizarov_2021]: https://doi.org/10.1145/3486607.3486751
[research_elkhouly_alshboul_2019]: https://doi.org/10.1145/3371236
[research_eloffrank_1995]: https://doi.org/10.1109/dac.1995.250085
[research_emerson_2020]: https://doi.org/10.18653/v1/2020.acl-main.367
[research_endo_perais_2017]: https://doi.org/10.1145/3090634
[research_engblom_ermedahl_2003]: https://doi.org/10.1007/s100090100054
[research_engelke_schwarz_2024]: https://doi.org/10.1109/cgo57630.2024.10444856
[research_engelke_weidendorfer_2017]: https://doi.org/10.1109/ipdpsw.2017.103
[research_enrici_apvrille_2019]: https://doi.org/10.5220/0007377900840095
[research_ermedahl_fredriksson_2009]: https://doi.org/10.1109/ecrts.2009.32
[research_ermedahl_puschner_2011]: https://doi.org/10.1016/j.sysarc.2011.06.001
[research_ermedahl_stappert_2003]: https://doi.org/10.1145/951718.951720
[research_ertl_1995]: https://doi.org/10.1145/207110.207165
[research_evans_lockington_1978]: https://doi.org/10.1093/comjnl/21.2.117
[research_evansi_sulaiman_1996]: https://doi.org/10.1080/00207169608804522
[research_facchinetti_palmer_2019]: https://doi.org/10.1145/3310340
[research_falis_1982]: https://doi.org/10.1145/3304133.3304135
[research_falk_2009]: https://doi.org/10.1145/1629911.1630100
[research_falk_lokuciejewski_2010]: https://doi.org/10.1007/s11241-010-9101-x
[research_falk_lokuciejewski_2019]: https://doi.org/10.1007/s11241-019-09337-9
[research_fan_wu_2025]: https://doi.org/10.1103/4nmq-twj8
[research_fan_ye_2024]: https://doi.org/10.1109/issre62328.2024.00040
[research_fang_kang_2026]: https://doi.org/10.1109/cgo68049.2026.11395239
[research_farkas_szabados_2021]: https://doi.org/10.2478/ausi-2021-0007
[research_fayzrakhmanov_2022]: https://doi.org/10.15514/ispras-2022-34(6)-5
[research_fedasyuk_chopey_2017]: https://doi.org/10.1109/cadsm.2017.7916134
[research_feitosa_ribeiro_2024]: https://doi.org/10.5753/sblp.2024.3462
[research_feitosa_vizzotto_2019]: https://doi.org/10.1016/j.scico.2018.03.003
[research_feldman_1966]: https://doi.org/10.1145/365153.365156
[research_feldman_1979]: https://doi.org/10.1145/872732.806959
[research_felker_2020]: https://doi.org/10.1109/sas48726.2020.9220074
[research_felleisen_1988]: https://doi.org/10.1145/73560.73576
[research_feng_ma_2025]: https://doi.org/10.1145/3763152
[research_ferdinand_heckmann_2008]: https://doi.org/10.1109/isorc.2008.16
[research_feret_simos_2007]: https://doi.org/10.1063/1.2836158
[research_ferrante_allard_1996]: https://doi.org/10.1145/242604.242621
[research_fifth_ieee_2005]: https://doi.org/10.1109/scam.2005.13
[research_finkel_poliakoff_2019]: https://doi.org/10.1109/p3hpc49587.2019.00013
[research_finkelstein_1968]: https://doi.org/10.1093/comjnl/11.1.22
[research_fisher_1976]: https://doi.org/10.21236/ada028297
[research_flatt_2007]: https://doi.org/10.1145/1291151.1291178
[research_flatt_dybvig_2020]: https://doi.org/10.1145/3385412.3385981
[research_fonseca_zhang_2017]: https://doi.org/10.1145/3064176.3064183
[research_formal_methods_1995]: https://ntrs.nasa.gov/citations/19980227975
[research_formal_methods_1995_2]: https://ntrs.nasa.gov/citations/19980228002
[research_forster_kammar_2019]: https://doi.org/10.1017/s0956796819000121
[research_fourth_ieee_2004]: https://doi.org/10.1109/scam.2004.10
[research_fox_myreen_2017]: https://doi.org/10.1145/3018610.3018621
[research_fradet_lesourd_2018]: https://doi.org/10.1109/rtss.2018.00039
[research_francalanza_tabone_2023]: https://doi.org/10.1016/j.jlamp.2023.100891
[research_fraser_wendt_1986]: https://doi.org/10.1145/12276.13335
[research_fraszczak_fraszczak_2026]: https://doi.org/10.1016/j.softx.2025.102463
[research_freier_jianjiachen_2013]: https://doi.org/10.1109/sies.2013.6601467
[research_frenkel_kunze_2011]: https://doi.org/10.3384/ecp11063232
[research_freund_mitchell_1998]: https://doi.org/10.1145/286942.286972
[research_freund_mitchell_1998_2]: https://doi.org/10.1016/s1571-0661(05)80703-0
[research_freund_mitchell_1999]: https://doi.org/10.1145/330643.330646
[research_freund_mitchell_2003]: https://doi.org/10.1023/a:1025011624925
[research_fried_stemmergrabow_2023]: https://doi.org/10.1145/3578360.3580261
[research_friers_becher_2021]: https://doi.org/10.1109/ldav53230.2021.00013
[research_friese_gioiosa_2024]: https://doi.org/10.1109/scw63240.2024.00165
[research_frigo_1999]: https://doi.org/10.1145/301618.301661
[research_fruehwirth_2025]: https://doi.org/10.46298/fi.11547
[research_fumero_kotselidis_2018]: https://doi.org/10.1145/3281287.3281292
[research_fumero_steuwer_2017]: https://doi.org/10.1145/3140607.3050761
[research_fusaoka_hirayama_1982]: https://doi.org/10.1145/960120.801831
[research_fusi_mazzocchetti_2020]: https://doi.org/10.3390/math8030314
[research_gaal_1993]: https://doi.org/10.1016/0165-6074(93)90076-w
[research_gaissert_bolztereick_2025]: https://doi.org/10.1145/3763085
[research_gal_probst_2005]: https://doi.org/10.1016/j.entcs.2005.01.020
[research_gal_probst_2008]: https://doi.org/10.1145/1377492.1377496
[research_gallaher_1982]: https://doi.org/10.21236/ada116070
[research_galloway_loewen_2015]: https://doi.org/10.1109/cloud.2015.90
[research_gan_li_2015]: https://doi.org/10.1112/jlms/jdv043
[research_ganzinger_giegerich_1982]: https://doi.org/10.1145/872726.806993
[research_ganzinger_ripken_1976]: https://doi.org/10.1145/800191.805629
[research_gao_li_2014]: https://doi.org/10.3724/sp.j.1146.2012.01341
[research_gao_parreaux_2025]: https://doi.org/10.1145/3763144
[research_gao_shi_2005]: https://doi.org/10.1117/12.586295
[research_gao_yang_2025]: https://doi.org/10.1109/icse55347.2025.00175
[research_garcia_lumsdaine_2009]: https://doi.org/10.1145/1594834.1480903
[research_garcia_lumsdaine_2010]: https://doi.org/10.2168/lmcs-6(3:1)2010
[research_gaudet_stoodley_2016]: https://doi.org/10.1145/2998415.2998419
[research_geeson_smith_2024]: https://doi.org/10.1109/cgo57630.2024.10444836
[research_genaim_zanardini_2013]: https://doi.org/10.1016/j.tcs.2012.12.018
[research_geng_ishikawa_2021]: https://doi.org/10.1109/iccss51193.2021.9464193
[research_georgakoudis_parasyris_2025]: https://doi.org/10.1145/3696443.3708939
[research_georgescu_olsthoorn_2024]: https://doi.org/10.1145/3663529.3663864
[research_georgiou_chamski_2020]: https://doi.org/10.1093/comjnl/bxaa103
[research_gerasimov_2018]: https://doi.org/10.1134/s036176881805002x
[research_ghadesi_lamothe_2024]: https://doi.org/10.1007/s10664-024-10499-9
[research_ghica_alyahya_2017]: https://doi.org/10.4204/eptcs.261.7
[research_ghica_lindley_2022]: https://doi.org/10.1145/3563445
[research_ghica_tapus_2015]: https://doi.org/10.1109/iccp.2015.7312613
[research_ghorbani_babamir_2019]: https://doi.org/10.1002/cpe.5324
[research_ghosh_bhattacharya_2020]: https://doi.org/10.1016/j.vlsi.2019.08.006
[research_ghosh_kulatilake_1987]: https://doi.org/10.1016/0098-3004(87)90043-4
[research_ghuzdewan_2025]: https://doi.org/10.70609/g-tech.v9i3.7379
[research_giacobazzi_2008]: https://doi.org/10.1109/sefm.2008.49
[research_gibbons_2021]: https://doi.org/10.22152/programming-journal.org/2022/6/7
[research_gifford_jouvelot_1992]: https://doi.org/10.21236/ada256798
[research_gillard_yamazaki_2026]: https://doi.org/10.1145/3806383.3815525
[research_ginsbach_crawford_2018]: https://doi.org/10.1145/3178372.3179515
[research_giorgi_lemetayer_1990]: https://doi.org/10.1145/91556.91648
[research_girault_2025]: https://doi.org/10.1145/3768311
[research_godboley_gupta_2022]: https://doi.org/10.5220/0011032900003176
[research_goldberg_1998]: https://doi.org/10.1145/288090.288104
[research_gomezdeniz_davilacardenes_2016]: https://doi.org/10.5121/ijsea.2016.7401
[research_goncharov_schroder_2018]: https://doi.org/10.23638/lmcs-14(3:10)2018
[research_goodenough_mcgowan_1976]: https://doi.org/10.21236/ada033893
[research_goos_2002]: https://doi.org/10.1016/s1571-0661(04)80392-x
[research_gordon_pedretti_2022]: https://doi.org/10.1109/ross56639.2022.00008
[research_gordon_scholz_2015]: https://doi.org/10.1145/2897336.2897347
[research_gore_bajaj_2023]: https://doi.org/10.47164/ijngc.v14i1.1090
[research_gorelik_khukhlaev_1975]: https://doi.org/10.1016/0041-5553(75)90084-1
[research_gorodetskiy_2019]: https://doi.org/10.33286/978-5-6041917-2-9.286-287
[research_gorringe_jain_2013]: https://doi.org/10.1109/autest.2013.6645070
[research_gotti_mbarki_2016]: https://doi.org/10.5220/0005986002100219
[research_gourdin_2023]: https://doi.org/10.1145/3605158.3605848
[research_grabmayer_2023]: https://doi.org/10.46298/lmcs-19(2:17)2023
[research_grabowski_2025]: https://doi.org/10.1109/fuzz62266.2025.11152116
[research_graham_1995]: https://doi.org/10.21236/ada302319
[research_grechanik_2012]: https://doi.org/10.1145/2382756.2382758
[research_green_supply_2023]: https://doi.org/10.47750/qas/24.195.06
[research_green_wood_2024]: https://doi.org/10.25144/22696
[research_groce_vantonder_2022]: https://doi.org/10.1145/3497776.3517765
[research_groenewegen_chastelet_2020]: https://doi.org/10.1145/3397537.3397553
[research_grolaux_nguyen_2026]: https://doi.org/10.1145/3807968.3810928
[research_gross_koch_2023]: https://doi.org/10.14722/ndss.2023.24290
[research_grover_1985]: https://doi.org/10.21236/ada160451
[research_gruetter_fukala_2024]: https://doi.org/10.1145/3656439
[research_gruner_brust_2025]: https://doi.org/10.1145/3711902
[research_gruner_brust_2025_2]: https://doi.org/10.1145/3711905
[research_gu_2023]: https://doi.org/10.1145/3611643.3617850
[research_guan_shen_2019]: https://doi.org/10.1145/3314221.3314652
[research_guan_treude_2024]: https://doi.org/10.1145/3643916.3644396
[research_guarna_jr_1987]: https://doi.org/10.21236/ada190885
[research_guerrera_maffia_2019]: https://doi.org/10.1016/j.future.2018.05.023
[research_guerrini_masini_2009]: https://doi.org/10.1145/1462179.1462184
[research_guessarian_1979]: https://doi.org/10.1016/0304-3975(79)90005-7
[research_gunadi_2015]: https://doi.org/10.1109/iceccs.2015.36
[research_gundersen_heijltjes_2013]: https://doi.org/10.1109/lics.2013.37
[research_guo_liu_2007]: https://doi.org/10.1109/asap.2007.4459288
[research_guo_si_2016]: https://doi.org/10.1186/s13639-016-0049-3
[research_gupta_1990]: https://doi.org/10.21236/ada230085
[research_gupta_lewis_2018]: https://doi.org/10.18653/v1/d18-1239
[research_guria_foster_2021]: https://doi.org/10.1145/3453483.3454048
[research_gustafsson_2006]: https://doi.org/10.1109/isola.2006.72
[research_guyer_lin_2005]: https://doi.org/10.1109/jproc.2004.840489
[research_gwestern_ball_1991]: https://doi.org/10.3997/2214-4609.201410925
[research_haas_maseli_2023]: https://doi.org/10.1145/3622855
[research_haas_rossberg_2017]: https://doi.org/10.1145/3062341.3062363
[research_haase_2016]: https://doi.org/10.3844/jcssp.2016.314.322
[research_haikunliu_haijin_2011]: https://doi.org/10.1109/tpds.2011.86
[research_hajyihia_asher_2015]: https://doi.org/10.1145/2685393
[research_hale_goodmandelahunty_2018]: https://doi.org/10.1080/1750399x.2018.1541649
[research_hamana_2022]: https://doi.org/10.46298/lmcs-18(2:18)2022
[research_hamid_ito_2017]: https://doi.org/10.1299/jsmedsd.2017.27.2502
[research_hammer_maschotta_2025]: https://doi.org/10.1109/access.2025.3615249
[research_hammond_dalcin_2023]: https://doi.org/10.1145/3615318.3615319
[research_han_2016]: https://doi.org/10.1080/1750399x.2016.1204883
[research_han_ma_2024]: https://doi.org/10.1109/tse.2024.3354739
[research_han_park_2021]: https://doi.org/10.1109/tpds.2020.3031911
[research_han_yoo_2026]: https://doi.org/10.47116/apjcri.2026.05.03
[research_han_yuki_2021]: https://doi.org/10.1109/candarw53999.2021.00022
[research_han_zhao_2024]: https://doi.org/10.1109/cgo57630.2024.10444865
[research_hanitzsch_robein_2001]: https://doi.org/10.3997/2214-4609-pdb.15.iv-4
[research_hanley_lippmanhand_1983]: https://doi.org/10.1001/jama.1983.03330370053031
[research_hansen_siveroni_2005]: https://doi.org/10.1016/j.entcs.2005.02.032
[research_hanson_1976]: https://doi.org/10.1016/0020-0190(76)90057-0
[research_hanzich_arayapolo_2009]: https://doi.org/10.3997/2214-4609.20145760
[research_hara_takahashi_2021]: https://doi.org/10.1109/qrs-c55045.2021.00099
[research_hardy_puaut_2013]: https://doi.org/10.1145/2516821.2516842
[research_hardy_puaut_2014]: https://doi.org/10.1007/s11241-014-9212-x
[research_hariri_shi_2016]: https://doi.org/10.1109/issre.2016.51
[research_hariri_shi_2019]: https://doi.org/10.1109/icst.2019.00021
[research_harlin_washizaki_2017]: https://doi.org/10.1109/hase.2017.17
[research_harmon_1988]: https://doi.org/10.1145/45380.45386
[research_harmon_klefstad_2007]: https://doi.org/10.1109/ipdps.2007.370422
[research_harmon_klefstad_2007_2]: https://doi.org/10.1109/rtcsa.2007.44
[research_harmon_klefstad_2007_3]: https://doi.org/10.1109/ipdps.2007.370346
[research_harmon_schoeberl_2008]: https://doi.org/10.1109/rtas.2008.34
[research_harmon_schoeberl_2012]: https://doi.org/10.1109/tii.2012.2187457
[research_harnes_morrison_2024]: https://doi.org/10.3390/fi16030084
[research_harper_pfenning_1992]: https://doi.org/10.21236/ada256731
[research_harrison_1989]: https://doi.org/10.21236/ada210760
[research_harrison_graham_1976]: https://doi.org/10.1145/800191.805518
[research_harshithan_2023]: https://doi.org/10.1109/icacic59454.2023.10434977
[research_hart_mcclanahan_1981]: https://doi.org/10.21236/ada102386
[research_hartley_zakkak_2022]: https://doi.org/10.1145/3546568
[research_haspert_beauregard_1998]: https://doi.org/10.21236/ada358469
[research_hataba_elmahdy_2019]: https://doi.org/10.1587/transinf.2018edl8180
[research_hatcliff_danvy_1994]: https://doi.org/10.1145/174675.178053
[research_hausladen_gerstmayer_2017]: https://doi.org/10.1115/detc2017-67402
[research_havelundklaus_lowrymike_2000]: https://ntrs.nasa.gov/citations/20000055731
[research_hazimeh_herrera_2021]: https://doi.org/10.1145/3543516.3456276
[research_hazott_stogmuller_2025]: https://doi.org/10.1016/j.vlsi.2024.102320
[research_he_li_2023]: https://doi.org/10.1016/j.jss.2023.111627
[research_he_yang_2025]: https://doi.org/10.52202/085713-0123
[research_he_zhao_2023]: https://doi.org/10.1145/3585341.3585359
[research_he_zhong_2025]: https://doi.org/10.1109/saner64311.2025.00032
[research_heck_zaidman_2015]: https://doi.org/10.1109/jitre.2015.7330170
[research_heim_2018]: https://doi.org/10.1145/3178372.3183636
[research_heimbigner_2006]: https://doi.org/10.21236/ada449363
[research_heinrich_will_2024]: https://doi.org/10.5220/0012252800003648
[research_henriksen_gallagher_2006]: https://doi.org/10.1109/scam.2006.1
[research_henry_asavoae_2014]: https://doi.org/10.1145/2666357.2597817
[research_hensley_elgazzar_2025]: https://doi.org/10.5121/cseij.2025.15133
[research_heo_kim_2025]: https://doi.org/10.1016/j.sysarc.2025.103546
[research_heo_oh_2019]: https://doi.org/10.1109/icse.2019.00027
[research_hepp_schoeberl_2012]: https://doi.org/10.1109/isorc.2012.17
[research_herklotz_demange_2023]: https://doi.org/10.1145/3573105.3575681
[research_herring_kalathil_1993]: https://doi.org/10.21236/ada268568
[research_heumann_tzannes_2015]: https://doi.org/10.1109/pact.2015.25
[research_heuring_waite_1990]: https://doi.org/10.21236/ada218777
[research_hikmatyarsyah_rahardjo_2022]: https://doi.org/10.5220/0010776200003121
[research_hillerstrom_2016]: https://doi.org/10.1145/2976022.2976033
[research_hillerstrom_lindley_2020]: https://doi.org/10.1017/s0956796820000040
[research_hillerstrom_lindley_2024]: https://doi.org/10.1017/s0956796824000030
[research_hinkley_ho_1994]: https://doi.org/10.3997/2214-4609.201407588
[research_hirata_minamide_2023]: https://doi.org/10.1016/j.scico.2023.102993
[research_hirdgeoffreyr_1991]: https://ntrs.nasa.gov/citations/19920034961
[research_hiroyuki_2009]: https://doi.org/10.1109/pdcat.2009.66
[research_hirschowitz_2019]: https://doi.org/10.1145/3290334
[research_hmid_coutinho_2016]: https://doi.org/10.1145/2927964.2927972
[research_hoang_rabaey_1992]: https://doi.org/10.1109/icassp.1992.226553
[research_hollingshaus_daddario_2015]: https://doi.org/10.1353/tt.2015.0002
[research_holmen_sahasrabudhe_2021]: https://doi.org/10.1145/3437359.3465581
[research_holmes_groce_2018]: https://doi.org/10.1109/issre.2018.00027
[research_holmes_groce_2020]: https://doi.org/10.1002/stvr.1727
[research_hong_ramanujam_2008]: https://doi.org/10.1109/icess.2008.88
[research_hook_1987]: https://doi.org/10.21236/ada197503
[research_hook_heilbrunner_1989]: https://doi.org/10.21236/ada224222
[research_hook_lehman_1992]: https://doi.org/10.21236/ada307189
[research_horky_kotrc_2016]: https://doi.org/10.1145/2851553.2851569
[research_horvat_ursic_2026]: https://doi.org/10.3390/electronics15132805
[research_horwat_1988]: https://doi.org/10.21236/ada202182
[research_hoskins_1988]: https://doi.org/10.1145/62162.62166
[research_hossain_emi_2021]: https://doi.org/10.1109/icccnt51525.2021.9579880
[research_howe_1984]: https://doi.org/10.21236/ada140884
[research_hsu_kremer_2003]: https://doi.org/10.1145/781131.781137
[research_hu_fan_2025]: https://doi.org/10.1007/s10664-025-10777-0
[research_hu_gu_2026]: https://doi.org/10.1016/j.sysarc.2026.103926
[research_hu_liu_2024]: https://doi.org/10.1109/icnsc62968.2024.10759926
[research_hu_tang_2024]: https://doi.org/10.1109/iccasit62299.2024.10828126
[research_hu_zhang_2022]: https://doi.org/10.1002/cpe.7519
[research_hu_zhao_2014]: https://doi.org/10.14257/ijhit.2014.7.3.38
[research_hua_nishide_2010]: https://doi.org/10.1109/saint.2010.107
[research_huang_gao_2022]: https://doi.org/10.1145/3546000.3546019
[research_huang_huang_2016]: https://doi.org/10.1109/isocc.2016.7799748
[research_huang_jay_2006]: https://doi.org/10.1145/1188966.1188992
[research_huangfu_zhang_2018]: https://doi.org/10.5626/jcse.2018.12.4.139
[research_huber_puffitsch_2011]: https://doi.org/10.1002/cpe.1763
[research_huch_1999]: https://doi.org/10.1145/317636.317908
[research_huck_kreutzer_2022]: https://doi.org/10.1109/mitp.2021.3093949
[research_huck_lehr_2018]: https://doi.org/10.1109/correctness.2018.00011
[research_huck_protze_2020]: https://doi.org/10.1109/correctness51934.2020.00010
[research_huck_ziegler_2024]: https://doi.org/10.1109/scw63240.2024.00032
[research_huizhao_zheng_2015]: https://doi.org/10.1109/pccc.2015.7410296
[research_hunt_tonin_2008]: https://doi.org/10.1145/1434790.1434806
[research_hura_1982]: https://doi.org/10.1016/s0026-2714(82)80471-x
[research_hussain_csallner_2014]: https://doi.org/10.1002/spe.2290
[research_huynh_roychoudhury_2007]: https://doi.org/10.1007/s10703-007-0041-6
[research_huynh_taura_2017]: https://doi.org/10.1109/cluster.2017.82
[research_hyatt_dewey_2025]: https://doi.org/10.1109/icst62969.2025.10989032
[research_hyland_levy_2007]: https://doi.org/10.1016/j.tcs.2006.12.026
[research_hyvernat_2025]: https://doi.org/10.46298/lmcs-21(3:20)2025
[research_hyvernat_2025_2]: https://doi.org/10.46298/lmcs-21(3:19)2025
[research_iida_oishi_2026]: https://doi.org/10.1109/access.2026.3682704
[research_ikemori_cong_2023]: https://doi.org/10.1145/3610612.3610616
[research_ilik_2012]: https://doi.org/10.1016/j.apal.2011.12.008
[research_ilik_2013]: https://doi.org/10.1016/j.apal.2012.05.003
[research_ilik_2013_2]: https://doi.org/10.4204/eptcs.127.6
[research_ilik_2014]: https://doi.org/10.1145/2643135.2643161
[research_imamoglu_cetinkaya_2017]: https://doi.org/10.1109/ickea.2017.8169904
[research_implementation_concept_2024]: https://doi.org/10.36652/0869-4931-2024-78-7-297-302
[research_implementation_of_1973]: https://doi.org/10.1145/986953.986994
[research_implementation_of_2015]: https://doi.org/10.5220/0005211500350043
[research_incorporating_near_surface_2015]: https://doi.org/10.1071/aseg2015ab071
[research_informationmanagementincsanfranciscoca_1970]: https://doi.org/10.21236/ad0711369
[research_inoue_hayashizaki_2011]: https://doi.org/10.1109/cgo.2011.5764692
[research_inoue_igarashi_2019]: https://doi.org/10.1016/j.scico.2019.03.008
[research_inoue_kaneko_2015]: https://doi.org/10.1109/mwscas.2015.7282093
[research_isaetchnikov_etcherniavskaia_2026]: https://doi.org/10.1109/iclo69056.2026.11624498
[research_ishio_asai_2022]: https://doi.org/10.1145/3564719.3568691
[research_ishiura_2016]: https://doi.org/10.1587/essfr.9.3_188
[research_iskra_hoefler_2015]: https://doi.org/10.1177/1094342014560666
[research_islam_wang_2022]: https://doi.org/10.1587/transinf.2021mpp0003
[research_ismael_zyad_2018]: https://doi.org/10.1109/scee.2018.8684137
[research_isoda_yokoyama_2024]: https://doi.org/10.1145/3689484.3690731
[research_israel_r_2026]: https://doi.org/10.1109/ictmim68190.2026.11507665
[research_ito_matsubara_2023]: https://doi.org/10.5220/0011722100003464
[research_ivanov_gueorguiev_2019]: https://doi.org/10.1109/meco.2019.8760025
[research_ivey_riley_2016]: https://doi.org/10.1145/2915371.2915383
[research_iwasaki_amer_2018]: https://doi.org/10.1109/sc.2018.00026
[research_iyenghar_baumgartner_2026]: https://doi.org/10.5220/0014853500004015
[research_izawa_masuhara_2022]: https://doi.org/10.5381/jot.2022.21.2.a1
[research_jaafar_jaber_2025]: https://doi.org/10.1145/3756907.3756924
[research_jacek_chiu_2016]: https://doi.org/10.1145/2908080.2908120
[research_jackson_2026]: https://doi.org/10.1145/3806645.3816125
[research_jadhav_devale_2026]: https://doi.org/10.1134/s0005117925601058
[research_jadhav_falk_2025]: https://doi.org/10.1007/s11241-025-09436-w
[research_jagnik_2023]: https://doi.org/10.47363/jmca/2023(2)e127
[research_jain_maskell_2022]: https://doi.org/10.1109/tpds.2021.3116859
[research_jamieson_brown_2021]: https://doi.org/10.1145/3446804.3446853
[research_jamil_2018]: https://doi.org/10.1109/secon.2018.8479201
[research_jana_2023]: https://doi.org/10.1504/ijsn.2023.10054893
[research_janetschek_prodan_2017]: https://doi.org/10.1145/3150994.3150999
[research_janssens_bruynooghe_1992]: https://doi.org/10.1016/0743-1066(92)90032-x
[research_jay_miller_2018]: https://doi.org/10.1109/saner.2018.8330199
[research_jberkhout_1992]: https://doi.org/10.3997/2214-4609.201410434
[research_jefferson_johnson_1994]: https://doi.org/10.21236/ada288572
[research_jefferson_johnson_1994_2]: https://doi.org/10.21236/ada288571
[research_jeon_jeon_2021]: https://doi.org/10.1016/j.infsof.2021.106564
[research_jeong_cha_2021]: https://doi.org/10.1587/transinf.2021edl8042
[research_jeong_kim_2019]: https://doi.org/10.1109/sp.2019.00017
[research_jeong_park_2024]: https://doi.org/10.1016/j.sysarc.2024.103099
[research_jervis_1963]: https://doi.org/10.21236/ad0411444
[research_jesus_weiland_2024]: https://doi.org/10.1145/3673038.3673104
[research_jha_dsouza_2018]: https://doi.org/10.1109/icacce.2018.8441723
[research_ji_wang_2007]: https://doi.org/10.1093/comjnl/bxm058
[research_ji_wang_2022]: https://doi.org/10.1145/3559009.3569690
[research_jiang_chow_2024]: https://doi.org/10.1109/newcas58973.2024.10666342
[research_jiang_li_2014]: https://doi.org/10.4028/www.scientific.net/amm.556-562.4120
[research_jiang_yan_2010]: https://doi.org/10.4028/www.scientific.net/amm.39.588
[research_jiang_zeng_2025]: https://doi.org/10.1109/saner64311.2025.00078
[research_jiang_zhang_2010]: https://doi.org/10.1109/qsic.2010.23
[research_jiang_zheng_2015]: https://doi.org/10.18178/ijfcc.2015.4.6.431
[research_jimenezgil_bate_2017]: https://doi.org/10.1109/les.2017.2712858
[research_jodogne_2022]: https://doi.org/10.5220/0010833300003123
[research_johann_simpson_2010]: https://doi.org/10.1109/lics.2010.29
[research_johnson_1978]: https://doi.org/10.1145/800127.804153
[research_johnson_krishnan_2024]: https://doi.org/10.1145/3689744
[research_johnson_laufer_2023]: https://doi.org/10.1109/sp46215.2023.10179357
[research_jones_1980]: https://doi.org/10.7146/dpb.v9i113.6531
[research_jones_christiansen_1981]: https://doi.org/10.7146/dpb.v10i137.7411
[research_jonginlee_suhyunpark_2005]: https://doi.org/10.1109/aero.2005.1559632
[research_jsimil_2010]: https://doi.org/10.5220/0003013403330336
[research_juimingchang_1995]: https://doi.org/10.1109/dac.1995.250019
[research_julianiranzo_rubiomanzano_2017]: https://doi.org/10.1016/j.fss.2016.12.016
[research_jung_2021]: https://doi.org/10.18653/v1/2021.nlp4prog-1.3
[research_jung_2024]: https://doi.org/10.1145/3679005.3695733
[research_just_in_time_2018]: https://doi.org/10.14738/abr.68.5041.
[research_jyhcharnliu_hungjulee_1994]: https://doi.org/10.1109/real.1994.342717
[research_kaestner_2007]: https://doi.org/10.1145/1273444.1254787
[research_kaestner_gebhard_2025]: https://doi.org/10.4271/2025-01-0155
[research_kahn_hoffmann_2026]: https://doi.org/10.1145/3776718
[research_kakati_brorsson_2025]: https://doi.org/10.5220/0013203200003950
[research_kalebe_girao_2017]: https://doi.org/10.1109/iccni.2017.8123793
[research_kalyur_nagaraja_2016]: https://doi.org/10.1109/csitss.2016.7779385
[research_kameyama_tanaka_2010]: https://doi.org/10.1145/1836089.1836100
[research_kammar_pretnar_2017]: https://doi.org/10.1017/s0956796816000320
[research_kanabar_vivien_2023]: https://doi.org/10.1145/3591259
[research_kanatov_zouev_2022]: https://doi.org/10.15514/ispras-2022-34(3)-2
[research_kandemir_2001]: https://doi.org/10.1145/373243.360219
[research_kang_desai_2026]: https://doi.org/10.1145/3828170.3828172
[research_kang_song_2025]: https://doi.org/10.1145/3774899.3775011
[research_karachalias_koprivec_2021]: https://doi.org/10.1145/3485479
[research_kargen_shahmehri_2018]: https://doi.org/10.1145/3230833.3230867
[research_karpovich_gosudarev_2025]: https://doi.org/10.7256/2454-0714.2025.2.74049
[research_karr_1984]: https://doi.org/10.1145/502874.502875
[research_karsten_barghi_2020]: https://doi.org/10.1145/3410048.3410100
[research_kasampalis_park_2021]: https://doi.org/10.1145/3445814.3446751
[research_kasaraneni_nandivada_2026]: https://doi.org/10.1145/3771775.3786280
[research_katel_khandelwal_2022]: https://doi.org/10.1145/3497776.3517770
[research_kawamata_unno_2024]: https://doi.org/10.1145/3633280
[research_kaynaroglu_razinkovasbaziukas_2025]: https://doi.org/10.1016/j.softx.2025.102430
[research_ke_chen_2020]: https://doi.org/10.1109/indo-taiwanican48429.2020.9181334
[research_kearns_lousoffa_1983]: https://doi.org/10.1007/bf00265556
[research_keaton_seacord_2014]: https://doi.org/10.21236/ada610094
[research_keidel_poulsen_2018]: https://doi.org/10.1145/3236767
[research_kelly_1963]: https://doi.org/10.2514/6.1963-102
[research_kellyjohnc_1997]: https://ntrs.nasa.gov/citations/20060035409
[research_kelsey_1995]: https://doi.org/10.1145/202530.202532
[research_kennedy_syme_2001]: https://doi.org/10.1145/378795.378797
[research_kerneis_chroboczek_2011]: https://doi.org/10.1007/s10990-012-9084-5
[research_keutzer_wolf_1988]: https://doi.org/10.1145/53990.54000
[research_khaldi_chapman_2016]: https://doi.org/10.1109/llvm-hpc.2016.007
[research_khaldi_jouvelot_2015]: https://doi.org/10.1145/2833157.2833158
[research_khatami_kaiser_2017]: https://doi.org/10.1109/ipdpsw.2017.14
[research_khorasani_gupta_2015]: https://doi.org/10.1109/pact.2015.15
[research_kiamtan_myreen_2019]: https://doi.org/10.1017/s0956796818000229
[research_kidney_wu_2025]: https://doi.org/10.1145/3704892
[research_kiefer_klebanov_2017]: https://doi.org/10.1007/s10817-017-9433-5
[research_kim_2015]: https://doi.org/10.14257/ijca.2015.8.11.02
[research_kim_gopinath_2000]: https://doi.org/10.1142/9781848160170_0065
[research_kim_hong_2023]: https://doi.org/10.1109/icst57152.2023.00053
[research_kim_khayatian_2019]: https://doi.org/10.1109/vlsid.2019.00127
[research_kim_kim_2012]: https://doi.org/10.9708/jksci.2012.17.8.061
[research_kim_kim_2025]: https://doi.org/10.1109/icst62969.2025.10989012
[research_kim_lee_2017]: https://doi.org/10.14257/ijca.2017.10.12.20
[research_kim_lee_2018]: https://doi.org/10.14257/ijast.2018.119.11
[research_kim_park_2023]: https://doi.org/10.1007/s12555-022-0737-9
[research_kim_ryou_2019]: https://doi.org/10.1109/platcon.2019.8669417
[research_kim_ryu_2025]: https://doi.org/10.1109/acsac67867.2025.00020
[research_kim_tian_2025]: https://doi.org/10.1109/sp61157.2025.00194
[research_kim_xu_2020]: https://doi.org/10.1145/3391202
[research_kim_zeng_2020]: https://doi.org/10.1145/3385412.3386033
[research_kingsley_1987]: https://doi.org/10.1145/37888.37978
[research_kipps_1982]: https://doi.org/10.1145/800230.806976
[research_kirichenko_tarasov_2017]: https://doi.org/10.1134/s1063739717010048
[research_kirner_kadlec_2009]: https://doi.org/10.1109/ecrts.2009.8
[research_kirner_knoop_2010]: https://doi.org/10.1007/s10270-010-0161-0
[research_kirner_puschner_2008]: https://doi.org/10.1109/isorc.2008.65
[research_kirner_schoeberl_2007]: https://doi.org/10.1109/dac.2007.375211
[research_kiselyov_2012]: https://doi.org/10.1016/j.tcs.2012.02.025
[research_kishorbhai_patel_2026]: https://doi.org/10.55248/gengpi.07.0426.b910
[research_kistel_vandenhouten_2013]: https://doi.org/10.15771/0949-8214_2013_1_11
[research_klein_2005]: https://doi.org/10.1524/itit.47.2.107.62257
[research_klein_nipkow_2001]: https://doi.org/10.1002/cpe.597
[research_klein_strecker_2004]: https://doi.org/10.1016/j.jlap.2003.07.004
[research_kleinsorge_falk_2013]: https://doi.org/10.1109/emsoft.2013.6658594
[research_klimis_2026]: https://doi.org/10.1145/3803437.3805569
[research_klockner_wilcox_2016]: https://doi.org/10.1145/2935323.2935325
[research_klohs_kastens_2005]: https://doi.org/10.1016/j.entcs.2005.01.031
[research_knoblock_rehof_2000]: https://doi.org/10.1145/325694.325725
[research_knoblock_rehof_2001]: https://doi.org/10.1145/383043.383045
[research_knoop_kovacs_2017]: https://doi.org/10.1016/j.jsc.2016.07.023
[research_ko_burgstaller_2015]: https://doi.org/10.1145/2737924.2737994
[research_ko_heo_2026]: https://doi.org/10.1145/3771775.3786278
[research_kobayashi_lozes_2017]: https://doi.org/10.1145/3009837.3009854
[research_kobusinska_wilczynski_2022]: https://doi.org/10.24251/hicss.2022.887
[research_kocourek_krikava_2025]: https://doi.org/10.1145/3759548.3763370
[research_koehler_steuwer_2021]: https://doi.org/10.1109/cgo51591.2021.9370337
[research_kokkonis_marcozzi_2025]: https://doi.org/10.1109/icse55347.2025.00183
[research_kolek_jovanovic_2013]: https://doi.org/10.1109/telfor.2013.6716404
[research_kolesar_ali_2025]: https://doi.org/10.1145/3763063
[research_komendantskaya_li_2018]: https://doi.org/10.4204/eptcs.278.5
[research_komolov_askarbekuly_2020]: https://doi.org/10.1145/3418688.3418695
[research_kondratyev_promsky_2019]: https://doi.org/10.1109/sibircon48586.2019.8958225
[research_kong_chen_2013]: https://doi.org/10.4028/www.scientific.net/amr.791-793.1726
[research_kong_jiang_2012]: https://doi.org/10.1007/s11859-012-0860-1
[research_kong_shi_2014]: https://doi.org/10.4028/www.scientific.net/amm.651-653.624
[research_koroglu_wotawa_2019]: https://doi.org/10.1109/ast.2019.00010
[research_koskimies_raiha_1982]: https://doi.org/10.1145/800230.806991
[research_kossatchev_posypkin_2005]: https://doi.org/10.1007/s11086-005-0008-6
[research_kot_kozen_2005]: https://doi.org/10.1016/j.entcs.2005.02.028
[research_kovacevic_ravber_2022]: https://doi.org/10.1016/j.cola.2022.101105
[research_kowalewski_philippou_2013]: https://doi.org/10.1007/s10009-013-0280-3
[research_kozen_silva_2016]: https://doi.org/10.1017/s0960129515000493
[research_krause_2015]: https://doi.org/10.1145/2764967.2764971
[research_krebs_schmitz_2014]: https://doi.org/10.1016/j.scico.2012.03.001
[research_krishnamoorthy_2025]: https://doi.org/10.34218/ijitmis_16_01_059
[research_kristensen_mollerpedersen_1987]: https://doi.org/10.7146/dpb.v16i235.7591
[research_kroening_poetzl_2016]: https://doi.org/10.1145/2970276.2970309
[research_krogstie_bahmann_2026]: https://doi.org/10.1109/cgo68049.2026.11395202
[research_krzemien_lukasiewicz_1976]: https://doi.org/10.1016/0020-0190(76)90088-0
[research_kuang_tang_2018]: https://doi.org/10.1016/j.cose.2018.01.008
[research_kumar_2014]: https://doi.org/10.1145/2535838.2535841
[research_kumar_2021]: https://doi.org/10.1109/dasc52595.2021.9594326
[research_kumar_ranjbar_2024]: https://doi.org/10.1109/access.2024.3379018
[research_kuperberg_pinault_2021]: https://doi.org/10.3233/fi-2021-2046
[research_kupke_rot_2021]: https://doi.org/10.46298/lmcs-17(4:19)2021
[research_kuroda_yuen_2026]: https://doi.org/10.2197/ipsjjip.34.444
[research_kusano_wang_2017]: https://doi.org/10.1145/3106237.3106243
[research_kusmenko_rumpe_2018]: https://doi.org/10.1145/3239372.3239388
[research_kwon_bae_2016]: https://doi.org/10.9708/jksci.2016.21.11.159
[research_kwon_jang_2025]: https://doi.org/10.1145/3729275
[research_kwon_kwon_2024]: https://doi.org/10.1145/3597503.3639189
[research_kwon_shin_2026]: https://doi.org/10.1109/cgo68049.2026.11395240
[research_kyriakou_tselikas_2022]: https://doi.org/10.3390/electronics11193217
[research_kyrtatas_spampinato_2015]: https://doi.org/10.7873/date.2015.0182
[research_lai_qiao_2026]: https://doi.org/10.1016/j.peva.2026.102543
[research_laliotis_1973]: https://doi.org/10.1145/633642.803976
[research_lambert_monil_2022]: https://doi.org/10.1109/p3hpc56579.2022.00007
[research_lambert_saunders_2017]: https://doi.org/10.1145/3115936.3115943
[research_lancellotti_buda_2026]: https://doi.org/10.1109/asp-dac66049.2026.11420750
[research_landa_sorin_1993]: https://doi.org/10.3997/2214-4609.201411670
[research_lane_poorman_1991]: https://doi.org/10.1190/1.1888920
[research_lange_cheeseman_1977]: https://doi.org/10.21236/ada040468
[research_larkins_jones_2011]: https://doi.org/10.1145/2016039.2016056
[research_larus_2011]: https://doi.org/10.1145/3249146
[research_larus_hilfinger_1986]: https://doi.org/10.1145/12276.13337
[research_lasnier_yallop_2026]: https://doi.org/10.1145/3779031.3779098
[research_lawall_danvy_1993]: https://doi.org/10.1145/158511.158613
[research_le_2014]: https://doi.org/10.1145/2594291.2594334
[research_le_sun_2015]: https://doi.org/10.1145/2858965.2814319
[research_league_2002]: https://doi.org/10.21236/ada436496
[research_leavitt_terrell_1991]: https://doi.org/10.21236/ada236716
[research_leavitt_terrell_1991_2]: https://doi.org/10.21236/ada236321
[research_leavitt_terrell_1991_3]: https://doi.org/10.21236/ada238259
[research_lecharlier_vanhentenryck_1994]: https://doi.org/10.1145/174625.174627
[research_lee_2017]: https://doi.org/10.1080/1750399x.2017.1359763
[research_lee_ahn_2025]: https://doi.org/10.1145/3763067
[research_lee_bang_2009]: https://doi.org/10.1587/transinf.e92.d.24
[research_lee_jang_2025]: https://doi.org/10.1109/pact65351.2025.00039
[research_lee_jeong_2017]: https://doi.org/10.1016/j.future.2016.03.014
[research_lee_lee_2024]: https://doi.org/10.1016/j.future.2024.06.015
[research_lee_moon_2015]: https://doi.org/10.1002/spe.2315
[research_lee_pleban_1987]: https://doi.org/10.1145/41625.41651
[research_lehman_1992]: https://doi.org/10.21236/ada249950
[research_lehman_hook_1988]: https://doi.org/10.21236/ada197645
[research_lehmann_bauer_2025]: https://doi.org/10.23919/date64628.2025.10992765
[research_lehmann_pradel_2022]: https://doi.org/10.1145/3519939.3523449
[research_lei_li_2025]: https://doi.org/10.1145/3733823.3764514
[research_leijen_2017]: https://doi.org/10.1145/3009837.3009872
[research_leijen_2017_2]: https://doi.org/10.1145/3122975.3122977
[research_leijen_2018]: https://doi.org/10.1145/3240719.3241789
[research_leinenbach_petrova_2008]: https://doi.org/10.1016/j.entcs.2008.06.040
[research_lemaistre_hanitzsch_2001]: https://doi.org/10.3997/2214-4609-pdb.15.p068
[research_lenkefi_mezei_2022]: https://doi.org/10.5220/0011260400003266
[research_leopoldseder_stadler_2015]: https://doi.org/10.1145/2936313.2816715
[research_leopoldseder_stadler_2018]: https://doi.org/10.1145/3168811
[research_leopoldseder_stadler_2018_2]: https://doi.org/10.1145/3281287.3281290
[research_leroy_2002]: https://doi.org/10.1002/spe.438
[research_leroy_2003]: https://doi.org/10.1023/a:1025055424017
[research_leroy_2006]: https://doi.org/10.1145/1111320.1111042
[research_leroy_2009_cacm]: https://doi.org/10.1145/1538788.1538814
[research_leroy_2009_jar]: https://doi.org/10.1007/s10817-009-9155-4
[research_leroy_grall_2009]: https://doi.org/10.1016/j.ic.2007.12.004
[research_leuschel_2004]: https://doi.org/10.1145/982158.982159
[research_leverett_cattell_1979]: https://doi.org/10.21236/ada955949
[research_levy_1996]: https://doi.org/10.1016/0166-5316(96)00016-8
[research_lezuo_dragan_2015]: https://doi.org/10.1109/synasc.2015.34
[research_lfreitasdaluz_cribeirocruz_2003]: https://doi.org/10.3997/2214-4609-pdb.168.arq_809
[research_li_2008]: https://doi.org/10.3724/sp.j.1145.2008.0001
[research_li_2019]: https://doi.org/10.2991/msbda-19.2019.25
[research_li_chai_2026]: https://doi.org/10.3390/computers15070406
[research_li_guo_2024]: https://doi.org/10.1109/tr.2023.3317643
[research_li_hu_2016]: https://doi.org/10.1145/2934872.2959061
[research_li_liu_2022]: https://doi.org/10.1609/aaai.v36i11.21527
[research_li_liu_2025]: https://doi.org/10.1109/qrs-c65679.2025.00031
[research_li_ma_2022]: https://doi.org/10.1145/3510003.3510217
[research_li_sakamoto_2017]: https://doi.org/10.24251/hicss.2017.016
[research_li_su_2023]: https://doi.org/10.1145/3582016.3582053
[research_li_tao_2024]: https://doi.org/10.14778/3704965.3704986
[research_li_wu_2025]: https://doi.org/10.1109/tc.2025.3566912
[research_li_zhang_2023]: https://doi.org/10.1016/j.sysarc.2022.102820
[research_li_zhao_2015]: https://doi.org/10.1145/2744769.2744809
[research_liang_liu_2017]: https://doi.org/10.1109/snpd.2017.8022752
[research_liangliang_yungui_1990]: https://doi.org/10.1016/0167-739x(90)90005-x
[research_lidbury_lascu_2015]: https://doi.org/10.1145/2737924.2737986
[research_lidman_svenningsson_2017]: https://doi.org/10.4204/eptcs.250.7
[research_lim_debray_2023]: https://doi.org/10.1145/3578360.3580260
[research_lima_santos_2019]: https://doi.org/10.1016/j.sysarc.2019.01.014
[research_lin_blackburn_2016]: https://doi.org/10.1145/3241624.2926707
[research_lin_ni_2025]: https://doi.org/10.1109/seai65851.2025.11108763
[research_lin_padua_2000]: https://doi.org/10.1145/349299.349322
[research_lin_song_2023]: https://doi.org/10.1109/qrs60937.2023.00066
[research_lindley_2014]: https://doi.org/10.1145/2633628.2633636
[research_lins_tambara_2017]: https://doi.org/10.1109/tns.2017.2705150
[research_lintzmayer_mulati_2011]: https://doi.org/10.1109/sccc.2011.32
[research_lion_broman_2026]: https://doi.org/10.1109/facct71761.2026.00011
[research_liu_2007]: https://doi.org/10.1109/ares.2007.55
[research_liu_bello_2021]: https://doi.org/10.1109/cgo51591.2021.9370310
[research_liu_bernstein_2024]: https://doi.org/10.1145/3656390
[research_liu_ding_2018]: https://doi.org/10.1051/matecconf/201822803008
[research_liu_guo_2025]: https://doi.org/10.3390/app15115935
[research_liu_lhotak_2020]: https://doi.org/10.1145/3428243
[research_liu_li_2018]: https://doi.org/10.1504/ijnvo.2018.093649
[research_liu_liu_2024]: https://doi.org/10.1109/auteee62881.2024.10869702
[research_liu_lu_2025]: https://doi.org/10.1109/iscait64916.2025.11010573
[research_liu_lv_2021]: https://doi.org/10.1088/1742-6596/1802/3/032137
[research_liu_millstein_2019]: https://doi.org/10.1145/3314221.3314611
[research_liu_qin_2026]: https://doi.org/10.1145/3793302.3793374
[research_liu_shen_2025]: https://doi.org/10.1145/3712197
[research_liu_wei_2022]: https://doi.org/10.1145/3527317
[research_liu_xu_2011]: https://doi.org/10.1109/les.2011.2112634
[research_liu_yang_2024]: https://doi.org/10.1007/s11432-022-3891-4
[research_liu_yu_2017]: https://doi.org/10.1145/3093333.3009870
[research_liu_zhu_2013]: https://doi.org/10.1109/iceccs.2013.46
[research_lo_suh_2012]: https://doi.org/10.1145/2228360.2228435
[research_lochbihler_2018]: https://doi.org/10.1007/s10817-018-9452-x
[research_loow_2021]: https://doi.org/10.1145/3437992.3439916
[research_lopes_2023]: https://doi.org/10.1145/3578360.3580266
[research_lopoukhine_ficarelli_2025]: https://doi.org/10.1145/3696443.3708952
[research_loring_mitchell_2019]: https://doi.org/10.1145/3314221.3314645
[research_louise_2011]: https://doi.org/10.1109/rtcsa.2011.74
[research_loveless_ott_2020]: https://doi.org/10.1145/3368826.3377925
[research_lowther_jacob_2023]: https://doi.org/10.1145/3623507.3623552
[research_loy_1981]: https://doi.org/10.2307/3679693
[research_lozano_carlsson_2016]: https://doi.org/10.1145/2892208.2892237
[research_lu_greenman_2022]: https://doi.org/10.22152/programming-journal.org/2023/7/2
[research_lu_nolte_2011]: https://doi.org/10.1145/2038617.2038619
[research_lu_nolte_2011_2]: https://doi.org/10.1109/etfa.2011.6059190
[research_lu_zhou_2025]: https://doi.org/10.1109/tr.2025.3614352
[research_lucanu_2018]: https://doi.org/10.1109/synasc.2018.00066
[research_lucchi_mazzara_2007]: https://doi.org/10.1016/j.jlap.2006.05.007
[research_luo_2020]: https://doi.org/10.1109/saner48275.2020.9054795
[research_luo_athanasiou_2017]: https://doi.org/10.1109/iccd.2017.94
[research_luo_lin_2026]: https://doi.org/10.1080/20964471.2026.2615511
[research_lv_guan_2010]: https://doi.org/10.1007/s11704-009-0073-8
[research_ly_birgersson_2009]: https://doi.org/10.1149/ma2009-02/10/794
[research_lyamin_2018]: https://doi.org/10.15217/issn1684-8853.2018.2.104
[research_lynn_1978]: https://doi.org/10.21236/ada052911
[research_m_2026]: https://doi.org/10.22214/ijraset.2026.79963
[research_m_murugesh_2021]: https://doi.org/10.21275/sr21329124355
[research_ma_2025]: https://doi.org/10.1145/3758316.3762822
[research_ma_ge_2024]: https://doi.org/10.1145/3689770
[research_ma_ge_2025]: https://doi.org/10.1145/3763177
[research_maccabe_2017]: https://doi.org/10.1145/3095770.3095771
[research_macmillen_2001]: https://doi.org/10.21236/ada405143
[research_madsen_zarifi_2018]: https://doi.org/10.1145/3178372.3179499
[research_magdalenic_radosevic_2011]: https://doi.org/10.24138/jcomss.v7i2.180
[research_magesty_montandon_2026]: https://doi.org/10.1145/3793655.3793714
[research_mahajan_abolhassani_2020]: https://doi.org/10.1145/3368089.3409764
[research_mahajan_ali_2008]: https://doi.org/10.1109/cec.2008.4630943
[research_mahajan_prasad_2022]: https://doi.org/10.1109/icst53961.2022.00030
[research_maia_cunha_2026]: https://doi.org/10.1145/3806383.3815520
[research_mainland_2017]: https://doi.org/10.1145/3110263
[research_maity_ghose_2026]: https://doi.org/10.1145/3778361
[research_makela_forsell_2016]: https://doi.org/10.1145/2983468.2983494
[research_makkimohialden_mahmoodhussien_2023]: https://doi.org/10.47310/srjecs.2023.v03i02.006
[research_malcolm_1971]: https://doi.org/10.21236/ad0727115
[research_maldonado_carrascosaez_2026]: https://doi.org/10.1109/access.2026.3698445
[research_male_pearce_2011]: https://doi.org/10.1016/j.scico.2010.10.004
[research_mallawarachchi_jayaweera_2025]: https://doi.org/10.54389/cwbl6597
[research_mamdouh_bahaaeldin_2014]: https://doi.org/10.1109/icces.2014.7030964
[research_maneriteshpratap_alponadas_2023]: https://doi.org/10.32628/ijsrset23103138
[research_manjunath_2010]: https://doi.org/10.5120/1682-2166
[research_mann_2003]: https://doi.org/10.1108/k.2003.06732iae.004
[research_manna_1988]: https://doi.org/10.21236/ada202490
[research_mao_chen_2025]: https://doi.org/10.1109/aibdf67964.2025.11440757
[research_mao_zhang_2019]: https://doi.org/10.1109/icc.2019.8761196
[research_marcelino_krennmair_2025]: https://doi.org/10.1145/3770501.3770515
[research_marcelino_nastic_2023]: https://doi.org/10.1145/3583740.3626611
[research_marcozzi_tang_2019]: https://doi.org/10.1145/3360581
[research_marlin_1980]: https://doi.org/10.1007/3-540-10256-6
[research_marref_2011]: https://doi.org/10.1109/samos.2011.6045462
[research_marriott_sondergaard_1994]: https://doi.org/10.1145/177492.177650
[research_marshall_1982]: https://doi.org/10.1145/800230.807003
[research_martinsen_grahn_2016]: https://doi.org/10.1002/cpe.3826
[research_marton_porkolab_2017]: https://doi.org/10.14232/actacyb.23.2.2017.14
[research_maryannekposenau_1993]: https://ntrs.nasa.gov/citations/19940017877
[research_massey_olivier_2026]: https://doi.org/10.1016/j.sysarc.2025.103666
[research_massidda_pisu_2024]: https://doi.org/10.5220/0012852400003767
[research_mastorou_papaspyrou_2022]: https://doi.org/10.1145/3546189.3549922
[research_masuko_asai_2009]: https://doi.org/10.1145/1596627.1596636
[research_matsikoudis_stergiou_2014]: https://doi.org/10.21236/ada603562
[research_matsubara_saito_2025]: https://doi.org/10.1109/candarw68385.2025.00013
[research_matteordonelli_2025]: https://doi.org/10.36676/jmk.v5.i2.93
[research_maurer_downen_2017]: https://doi.org/10.1145/3062341.3062380
[research_mazaher_berry_1985]: https://doi.org/10.1016/0096-0551(85)90004-9
[research_mcnerney_1991]: https://doi.org/10.1145/115865.115877
[research_medeiros_bortolon_2018]: https://doi.org/10.1109/sbcci.2018.8533246
[research_meghzili_chaoui_2017]: https://doi.org/10.1109/iri.2017.63
[research_mehdipourhashemkallehbasti_ghafari_2023]: https://doi.org/10.1109/saner56733.2023.00083
[research_mehta_yew_2015]: https://doi.org/10.1145/2737924.2737954
[research_meier_jensen_2025]: https://doi.org/10.1145/3703595.3705879
[research_melnyk_kozak_2019]: https://doi.org/10.23939/acps2019.02.105
[research_meloalves_teylo_2018]: https://doi.org/10.1109/wscad.2018.00024
[research_melquiond_moreau_2024]: https://doi.org/10.1145/3674629
[research_melrose_sachsenmaier_2015]: https://doi.org/10.1080/13528165.2015.1111060
[research_menetrey_pasin_2021]: https://doi.org/10.1109/icde51399.2021.00025
[research_menetrey_pasin_2022]: https://doi.org/10.1109/icdcs54860.2022.00116
[research_menetrey_pasin_2024]: https://doi.org/10.1109/tdsc.2023.3334516
[research_meng_sun_2020]: https://doi.org/10.1109/cicn49253.2020.9242624
[research_merazga_rahem_2025]: https://doi.org/10.48084/etasr.10990
[research_meybodi_2015]: https://doi.org/10.1108/tqm-08-2013-0098
[research_meyer_wolff_2019]: https://doi.org/10.1145/3290371
[research_mguidich_paun_2016]: https://doi.org/10.1109/rtss.2016.051
[research_mhaske_uliana_2015]: https://doi.org/10.1109/sarnof.2015.7324649
[research_michaud_pipereau_2024]: https://doi.org/10.1109/fnwf63303.2024.11028722
[research_michels_hommersom_2015]: https://doi.org/10.1016/j.artint.2015.06.008
[research_midtgaard_2025]: https://doi.org/10.1145/3759427.3760378
[research_midzic_novak_2025]: https://doi.org/10.55549/epstem.1753850
[research_mihelic_steingartner_2021]: https://doi.org/10.12700/aph.18.4.2021.4.13
[research_milano_turcotti_2022]: https://doi.org/10.1145/3519939.3523443
[research_milos_pleban_1984]: https://doi.org/10.1145/800017.800531
[research_minato_masumoto_2025]: https://doi.org/10.15803/ijnc.15.2_118
[research_mine_2017]: https://doi.org/10.1561/2500000034
[research_mitra_givargis_2009]: https://doi.org/10.1145/3252479
[research_mittal_banerjee_2021]: https://doi.org/10.5220/0010581005330541
[research_mizikovskiy_2024]: https://doi.org/10.36511/2588-0071-2024-1-131-141
[research_mizobuchi_takayama_2017]: https://doi.org/10.1109/saner.2017.7884678
[research_modern_compiler_1997]: https://doi.org/10.1016/s0898-1221(97)84605-6
[research_modern_compiler_1997_2]: https://doi.org/10.1016/s0898-1221(97)84609-3
[research_modern_compiler_1997_3]: https://doi.org/10.1016/s0898-1221(97)84606-8
[research_modern_compiler_1998]: https://doi.org/10.1016/0898-1221(98)90193-6
[research_mohan_2008]: https://doi.org/10.1145/1366283.1366291
[research_mohnen_1997]: https://doi.org/10.3233/fi-1997-29303
[research_moliavko_drozdovskyi_2019]: https://doi.org/10.21105/joss.01338
[research_molinafraticellijosecarlos_2012]: https://ntrs.nasa.gov/citations/20120014979
[research_mondal_mondal_2023]: https://doi.org/10.1109/apsec60848.2023.00076
[research_mondal_rahman_2016]: https://doi.org/10.18293/seke2016-146
[research_mondshein_1967]: https://doi.org/10.21236/ad0649140
[research_monniaux_2024]: https://doi.org/10.1145/3636501.3636952
[research_monsuez_1995]: https://doi.org/10.1145/215465.215574
[research_montenegro_pena_2015]: https://doi.org/10.1016/j.scico.2014.04.014
[research_moody_richards_1980]: https://doi.org/10.1002/spe.4380101002
[research_moor_1982]: https://doi.org/10.1145/800230.807002
[research_moore_1968]: https://doi.org/10.1093/combul/11.4.153
[research_moret_binder_2011]: https://doi.org/10.1145/1960275.1960292
[research_morford_1999]: https://doi.org/10.3997/2214-4609-pdb.215.sbgf421
[research_morford_2000]: https://doi.org/10.1190/1.1815563
[research_morford_2001]: https://doi.org/10.3997/2214-4609-pdb.217.256
[research_moriguchi_morishima_2016]: https://doi.org/10.1587/transcom.2016nep0013
[research_moron_wallentowitz_2023]: https://doi.org/10.1109/meco58584.2023.10155088
[research_mosaner_barany_2022]: https://doi.org/10.1145/3563838.3567679
[research_moser_schneckenreither_2020]: https://doi.org/10.1016/j.scico.2019.102306
[research_moskalenko_2025]: https://doi.org/10.37547/tajet/volume07issue10-17
[research_moss_davis_2016]: https://doi.org/10.1109/llvm-hpc.2016.009
[research_mossenbock_1984]: https://doi.org/10.1524/itit.1984.26.16.186
[research_mosses_2004]: https://doi.org/10.1016/j.jlap.2004.03.008
[research_mosses_2015]: https://doi.org/10.1016/j.scico.2013.11.038
[research_mosterman_zander_2015]: https://doi.org/10.1007/s10270-015-0469-x
[research_mpeis_petoumenos_2021]: https://doi.org/10.1145/3453483.3454043
[research_muckenschnabel_2024]: https://doi.org/10.1145/3689491.3689967
[research_mukherjee_ghosh_2024]: https://doi.org/10.1145/3663477
[research_muller_mane_2026]: https://doi.org/10.1109/saner67736.2026.00045
[research_muller_schuster_2023]: https://doi.org/10.1145/3622831
[research_muller_zhou_1992]: https://doi.org/10.1145/141471.141520
[research_munley_jarmusch_2024]: https://doi.org/10.1016/j.future.2024.05.034
[research_murthy_mellorcrummey_2015]: https://doi.org/10.1109/pgas.2015.17
[research_mushtaq_alars_2015]: https://doi.org/10.1109/patmos.2015.7347584
[research_mussig_2019]: https://doi.org/10.1007/s00735-019-1022-x
[research_musumbu_2008]: https://doi.org/10.1109/iccsit.2008.10
[research_muts_falk_2020]: https://doi.org/10.1145/3378678.3391879
[research_mycroft_1993]: https://doi.org/10.1145/154630.154648
[research_mykola_2024]: https://doi.org/10.37547/tajet/volume06issue12-06
[research_myreen_2010]: https://doi.org/10.1145/1707801.1706313
[research_myreen_2021]: https://doi.org/10.1145/3437992.3439915
[research_mzid_charfi_2022]: https://doi.org/10.5220/0010821700003119
[research_na_kim_2016]: https://doi.org/10.1145/2846098
[research_nadi_treude_2020]: https://doi.org/10.1109/saner48275.2020.9054828
[research_nagata_sakata_2024]: https://doi.org/10.5772/acrt.20240043
[research_naik_2013]: https://doi.org/10.1145/3245331
[research_nair_2012]: https://doi.org/10.1016/j.procs.2012.09.055
[research_nair_sarasamma_2006]: https://doi.org/10.1109/nafips.2006.365407
[research_naish_2015]: https://doi.org/10.7717/peerj-cs.22
[research_nakata_matsubara_2025]: https://doi.org/10.1145/3774898.3778040
[research_nakata_uustalu_2015]: https://doi.org/10.2168/lmcs-11(1:1)2015
[research_namakonov_podkopaev_2019]: https://doi.org/10.15514/ispras-2019-31(5)-4
[research_nanthaamornphong_leatongkam_2015]: https://doi.org/10.1109/iciteed.2015.7408903
[research_nappa_zhao_2019]: https://doi.org/10.1109/pact.2019.00015
[research_narkthong_jariyavajee_2024]: https://doi.org/10.1109/vl/hcc60511.2024.00031
[research_natarajan_broman_2020]: https://doi.org/10.1109/fdl50818.2020.9232935
[research_nationalbureauofstandardsgaithersburgmd_1988]: https://doi.org/10.21236/ada209138
[research_nationalbureauofstandardsgaithersburgmd_1988_2]: https://doi.org/10.21236/ada208498
[research_nationalbureauofstandardsgaithersburgmd_1988_3]: https://doi.org/10.21236/ada204904
[research_nationalbureauofstandardsgaithersburgmd_1989]: https://doi.org/10.21236/ada208475
[research_nayvelt_bear_2008]: https://doi.org/10.1190/1.3064099
[research_necula_1997]: https://doi.org/10.1145/263699.263712
[research_necula_2000]: https://doi.org/10.1145/349299.349314
[research_necula_lee_1998]: https://doi.org/10.1145/277652.277752
[research_necula_lee_2004]: https://doi.org/10.1145/989393.989454
[research_nedoria_2023]: https://doi.org/10.15514/ispras-2023-35(6)-5
[research_negrini_2026]: https://doi.org/10.3389/fcomp.2025.1655377
[research_neis_hur_2015]: https://doi.org/10.1145/2858949.2784764
[research_nejjar_zacharias_2024]: https://doi.org/10.1002/smr.2723
[research_nemer_casse_2007]: https://doi.org/10.1109/sies.2007.4297313
[research_network_aware_virtual_2016]: https://doi.org/10.21275/v5i1.nov152580
[research_new_giovannini_2023]: https://doi.org/10.1145/3622860
[research_newey_1975]: https://doi.org/10.21236/ada005413
[research_nezamabadi_myreen_2026]: https://doi.org/10.1145/3779031.3779092
[research_ngo_talpin_2015]: https://doi.org/10.1145/2764967.2775291
[research_nguyen_aoki_2019]: https://doi.org/10.1109/apsec48747.2019.00021
[research_nguyen_mccaskey_2022]: https://doi.org/10.1145/3544496
[research_nguyen_perera_2023]: https://doi.org/10.1145/3609026.3609729
[research_ni_li_2025]: https://doi.org/10.1145/3763079
[research_nickerson_1990]: https://doi.org/10.1145/93548.93552
[research_nielsen_1997]: https://doi.org/10.21236/ada328290
[research_nielsen_1998]: https://doi.org/10.21236/ada336718
[research_nielson_1987]: https://doi.org/10.1145/41625.41636
[research_nielson_1988]: https://doi.org/10.1016/0890-5401(88)90041-7
[research_niephaus_felgentreff_2018]: https://doi.org/10.22152/programming-journal.org/2018/2/8
[research_nikhilsripathirao_2024]: https://doi.org/10.32628/cseit241061235
[research_nilsen_rygg_1995]: https://doi.org/10.1145/216633.216650
[research_nipkow_2003]: https://doi.org/10.1023/a:1025086804452
[research_nishizaki_2017]: https://doi.org/10.1145/3056662.3056693
[research_nishizaki_2017_2]: https://doi.org/10.1109/icctec.2017.00040
[research_nishizaki_2019]: https://doi.org/10.1145/3316615.3316668
[research_niu_li_2024]: https://doi.org/10.1145/3597503.3608136
[research_noci_compiler_a_2026]: https://doi.org/10.58257/ijprems51382
[research_noguchi_matsumoto_2021]: https://doi.org/10.1109/csde53843.2021.9718480
[research_norris_pollock_1994]: https://doi.org/10.1145/773473.178427
[research_nougrahiya_nandivada_2024]: https://doi.org/10.1145/3649308
[research_nowicki_gorski_2021]: https://doi.org/10.1002/cpe.6536
[research_nyangaresi_ma_2022]: https://doi.org/10.1109/aic55036.2022.9848874
[research_oates_harinder_1998]: https://doi.org/10.2118/39499-ms
[research_ocallahan_1999]: https://doi.org/10.1145/292540.292549
[research_odaira_nakaike_2010]: https://doi.org/10.1145/1772954.1772978
[research_odegardryan_milenkoviczoran_2014]: https://ntrs.nasa.gov/citations/20140003581
[research_oehlert_luppold_2018]: https://doi.org/10.1145/3207719.3207731
[research_oh_jeong_2022]: https://doi.org/10.1109/les.2022.3163749
[research_oh_kim_2026]: https://doi.org/10.1145/3803525.3804981
[research_oh_yeo_2015]: https://doi.org/10.7873/date.2015.0927
[research_oiwa_2009]: https://doi.org/10.1145/1543135.1542505
[research_okasaki_lee_1994]: https://doi.org/10.1007/bf01019945
[research_okim_lee_2026]: https://doi.org/10.1088/1361-6501/ae8c6d
[research_oliva_ramsdell_1995]: https://doi.org/10.1007/bf01128408
[research_oloughlin_gillam_2015]: https://doi.org/10.5220/0005485000600067
[research_olteanu_oprisa_2025]: https://doi.org/10.1109/icstcc66753.2025.11240319
[research_online_platform_2024]: https://doi.org/10.31673/2412-9070.2024.063151
[research_ooashi_taniguchi_1992]: https://doi.org/10.1002/scj.4690230701
[research_orlic_2010]: https://doi.org/10.1109/cee-secr.2010.5783159
[research_orlitsky_2002]: https://doi.org/10.1109/tit.2002.1003829
[research_orlov_2017]: https://doi.org/10.17587/prin.8.291-299
[research_orrjamesk_hendersonjohnniea_2000]: https://ntrs.nasa.gov/citations/20100033619
[research_ortiz_2022]: https://doi.org/10.1145/3478432.3499119
[research_osborne_pivarski_2024]: https://doi.org/10.1051/epjconf/202429506003
[research_oshita_kaida_2019]: https://doi.org/10.1109/iiai-aai.2019.00068
[research_othman_elghoul_2022]: https://doi.org/10.54455/mcn.20.01
[research_ottoni_2018]: https://doi.org/10.1145/3192366.3192374
[research_ouadjaout_mine_2016]: https://doi.org/10.1016/j.jss.2016.07.030
[research_ozdemir_brown_2022]: https://doi.org/10.1109/sp46214.2022.9833782
[research_padmasudhakannan_smitha_2021]: https://doi.org/10.1016/j.matpr.2020.09.706
[research_painter_1970]: https://doi.org/10.1145/800028.808487
[research_pait_jayanthiladevi_2020]: https://doi.org/10.47992/ijaeml.2581.7000.0087
[research_palka_claessen_2011]: https://doi.org/10.1145/1982595.1982615
[research_palsberg_1992]: https://doi.org/10.7146/dpb.v21i422.6736
[research_palsberg_schwartzbach_1992]: https://doi.org/10.7146/dpb.v21i393.6628
[research_pan_cheney_2026]: https://doi.org/10.1145/3802003
[research_pan_xie_2015]: https://doi.org/10.1109/emsoft.2015.7318275
[research_pandey_2025]: https://doi.org/10.55041/ijsrem52649
[research_panigrahi_karfa_2023]: https://doi.org/10.1109/tcad.2023.3269954
[research_panigrahi_karfa_2023_2]: https://doi.org/10.1109/isvlsi59464.2023.10238662
[research_pankhurst_1968]: https://doi.org/10.1145/800186.810605
[research_pant_pokhrel_2022]: https://doi.org/10.1109/ic_aset53395.2022.9765916
[research_papadakis_jia_2015]: https://doi.org/10.1109/icse.2015.103
[research_papadimitriou_fumero_2021]: https://doi.org/10.1145/3453933.3454014
[research_pape_bolz_2017]: https://doi.org/10.1016/j.scico.2016.08.003
[research_paraman_murthy_2023]: https://doi.org/10.11591/ijeecs.v29.i2.pp990-1005
[research_parashar_kumawat_2026]: https://doi.org/10.25258/ijddt.16.54s.58
[research_park_choi_2005]: https://doi.org/10.3745/kipsta.2005.12a.5.365
[research_park_jeong_2023]: https://doi.org/10.3390/app13169161
[research_park_lee_2001]: https://doi.org/10.1145/384197.384205
[research_park_stefanescu_2015]: https://doi.org/10.1145/2737924.2737991
[research_park_zhang_2018]: https://doi.org/10.1145/3236024.3264591
[research_parra_2026]: https://doi.org/10.1016/j.envsoft.2026.107102
[research_parwez_abrar_2025]: https://doi.org/10.1109/icect66235.2025.11381681
[research_pasareanucorinas_schumannjohannm_2009]: https://ntrs.nasa.gov/citations/20090036803
[research_pasupuleti_2025]: https://doi.org/10.62311/nesx/rp0225
[research_patel_ahrens_2025]: https://doi.org/10.1145/3696443.3708919
[research_patel_lee_2016]: https://doi.org/10.1109/icess.2016.30
[research_pathiran_prakash_2014]: https://doi.org/10.1002/cjce.22014
[research_patterson_ahmed_2019]: https://doi.org/10.1145/3341689
[research_pattinson_schroder_2016]: https://doi.org/10.1145/2933575.2934506
[research_paul_he_2020]: https://doi.org/10.14778/3425879.3425890
[research_pauli_soffa_1980]: https://doi.org/10.1002/spe.4380100305
[research_paulson_1982]: https://doi.org/10.1145/582153.582178
[research_pavlovskiy_platov_2025]: https://doi.org/10.32782/2663-5941/2025.2.2/24
[research_payne_1978]: https://doi.org/10.1145/953428.953435
[research_pecimuth_2023]: https://doi.org/10.1145/3618305.3623593
[research_pelsmaeker_vanantwerpen_2019]: https://doi.org/10.1145/3359061.3362782
[research_penev_dimitrov_2021]: https://doi.org/10.1109/icai52893.2021.9639831
[research_peng_wu_2004]: https://doi.org/10.1145/1059579.1059584
[research_petchartee_2025]: https://doi.org/10.1109/icsec67360.2025.11298108
[research_peterson_humphrey_2017]: https://doi.org/10.1145/3152041.3152082
[research_petkovski_bradey_2001]: https://doi.org/10.1071/aseg2001ab108
[research_petrosino_monica_2023]: https://doi.org/10.5220/0011619300003393
[research_pham_odersky_2024]: https://doi.org/10.1145/3679005.3685979
[research_phulia_bhagee_2020]: https://doi.org/10.1145/3385412.3385962
[research_pichler_li_2023]: https://doi.org/10.1145/3623507.3623554
[research_pieters_schrijvers_2017]: https://doi.org/10.1145/3205368.3205372
[research_pieters_schrijvers_2020]: https://doi.org/10.1017/s0956796820000192
[research_pikelee_wegmannnis_2012]: https://ntrs.nasa.gov/citations/20120014570
[research_pinckney_guha_2020]: https://doi.org/10.1145/3426422.3426978
[research_pizzolotto_inoue_2021]: https://doi.org/10.1109/access.2021.3132950
[research_pjeannot_1994]: https://doi.org/10.3997/2214-4609.201410049
[research_pjeannot_berranger_1994]: https://doi.org/10.3997/2214-4609.201409835
[research_pla_2004]: https://doi.org/10.21236/ada425710
[research_plangger_krall_2016]: https://doi.org/10.1145/2906363.2906384
[research_plasterie_chagalov_2006]: https://doi.org/10.1071/aseg2006ab137
[research_pleban_1979]: https://doi.org/10.1145/800229.806964
[research_pleban_1984]: https://doi.org/10.1145/502874.502883
[research_plishka_ifarraguerri_1993]: https://doi.org/10.21236/ada266972
[research_ploensin_piromsopa_2021]: https://doi.org/10.1088/1742-6596/1936/1/012023
[research_plotkin_2004]: https://doi.org/10.1016/s1567-8326(04)00026-8
[research_plotkin_pretnar_2008]: https://doi.org/10.1109/lics.2008.45
[research_plotkin_pretnar_2009]: https://doi.org/10.1007/978-3-642-00590-9_7
[research_plotkin_pretnar_2013]: https://doi.org/10.2168/lmcs-9(4:23)2013
[research_pockstaller_huber_2023]: https://doi.org/10.5220/0012205600003584
[research_poletanovic_dukic_2022]: https://doi.org/10.1109/zinc55034.2022.9840726
[research_polito_ducasse_2022]: https://doi.org/10.1145/3519939.3523457
[research_poonguzhali_vinodha_2014]: https://doi.org/10.2316/journal.205.2014.3.205-5983
[research_popeea_chin_2004]: https://doi.org/10.1145/1014007.1014021
[research_porcher_1995]: https://doi.org/10.1016/0167-739x(94)00044-f
[research_posner_ellersiek_2025]: https://doi.org/10.1007/s42979-025-04405-3
[research_postema_fabry_2022]: https://doi.org/10.1109/icst53961.2022.00042
[research_pous_2015]: https://doi.org/10.1145/2792434.2792440
[research_pous_2016]: https://doi.org/10.1145/2933575.2934564
[research_powell_1984]: https://doi.org/10.1145/502874.502905
[research_power_2006]: https://doi.org/10.14236/ewic/msfp2006.2
[research_pratt_1997]: https://doi.org/10.21236/ada329349
[research_prenzel_provost_2017]: https://doi.org/10.1016/j.ifacol.2017.08.2429
[research_pretnar_2014]: https://doi.org/10.2168/lmcs-10(3:21)2014
[research_pretnar_2015]: https://doi.org/10.1016/j.entcs.2015.12.003
[research_prinz_2023]: https://doi.org/10.5220/0012151500003584
[research_pritchard_1976]: https://doi.org/10.1016/0020-0190(76)90082-x
[research_proceedings_of_2020]: https://doi.org/10.1109/emsoft51651.2020.9244035
[research_proceedings_second_2002]: https://doi.org/10.1109/scam.2002.1134099
[research_proceedings_third_2003]: https://doi.org/10.1109/scam.2003.1238025
[research_prokopec_2018]: https://doi.org/10.4230/LIPIcs.ECOOP.2018.3
[research_proy_heydemann_2017]: https://doi.org/10.1145/3141234
[research_puchol_stuart_1998]: https://doi.org/10.3233/ica-1998-5301
[research_puffitsch_2016]: https://doi.org/10.1109/ecrts.2016.23
[research_punchihewa_wu_2021]: https://doi.org/10.1145/3471874.3472988
[research_punnoose_2020]: https://doi.org/10.2172/1825972
[research_puranik_2025]: https://doi.org/10.1109/iciteics64870.2025.11341094
[research_puschner_1997]: https://doi.org/10.1016/s1474-6670(17)42661-9
[research_puschner_1998]: https://doi.org/10.1016/s0967-0661(97)10050-8
[research_pyzik_2023]: https://doi.org/10.46298/entics.10502
[research_qassir_2025]: https://doi.org/10.18421/tem143-11
[research_qian_2000]: https://doi.org/10.1145/363911.363915
[research_qian_sathia_2026]: https://doi.org/10.1109/cgo68049.2026.11395228
[research_qian_ying_2025]: https://doi.org/10.1145/3728877
[research_qin_xia_2026]: https://doi.org/10.1145/3774895.3812200
[research_qu_huang_2023]: https://doi.org/10.1109/qrs60937.2023.00043
[research_quantum_software_2025]: https://doi.org/10.7753/ijcatr1404.1003
[research_queirozjunior_dasilva_2015]: https://doi.org/10.5220/0005380605040515
[research_queirozjunior_dasilva_2020]: https://doi.org/10.31577/cai_2020_6_1117
[research_quiring_reppy_2021]: https://doi.org/10.1145/3544885.3544889
[research_radonic_ukic_2014]: https://doi.org/10.1109/telfor.2014.7034599
[research_radooevii_magdalenii_2014]: https://doi.org/10.2139/ssrn.2505704
[research_raj_2016]: https://doi.org/10.1109/icett.2016.7873638
[research_rajucherukuri_2024]: https://doi.org/10.21275/es24928085711
[research_ramdani_nabarian_2025]: https://doi.org/10.54914/dbesti.v2i1.1636
[research_ramesh_sukanth_2024]: https://doi.org/10.1109/icccnt61001.2024.10725306
[research_ramkumar_kale_1990]: https://doi.org/10.1145/99164.99175
[research_rand_2022]: https://doi.org/10.1145/3497776.3526941
[research_ranganathan_sharma_2020]: https://doi.org/10.1145/3388142.3388143
[research_ranjan_paterson_2025]: https://doi.org/10.1145/3669940.3707281
[research_ranzato_2013]: https://doi.org/10.1145/3260312
[research_rao_liu_2021]: https://doi.org/10.1109/cloud53861.2021.00058
[research_raskovsky_1982]: https://doi.org/10.1145/800230.806998
[research_rath_schemmel_2018]: https://doi.org/10.1145/3284850.3284853
[research_ravanbakhsh_sankaranarayanan_2014]: https://doi.org/10.1145/2656045.2656060
[research_raveduttiluciomachado_eitzinger_2025]: https://doi.org/10.1177/10943420251405928
[research_reb_lima_2008]: https://doi.org/10.1109/icst.2008.14
[research_recharla_2025]: https://doi.org/10.1109/wispnet64060.2025.11004864
[research_reddy_singh_2026]: https://doi.org/10.1109/cgo68049.2026.11394845
[research_refaie_thyabat_2015]: https://doi.org/10.1504/ijbpm.2015.066020
[research_regehr_2005]: https://doi.org/10.1145/1113830.1113833
[research_reinhardt_zhang_2018]: https://doi.org/10.1145/3236024.3264585
[research_reis_bispo_2017]: https://doi.org/10.1145/3078155.3078186
[research_reiss_1983]: https://doi.org/10.1145/69624.69625
[research_reitz_posner_2025]: https://doi.org/10.1145/3731599.3767502
[research_ren_liu_2026]: https://doi.org/10.1145/3797154
[research_reshef_roth_2003]: https://doi.org/10.3997/2214-4609-pdb.6.e16
[research_reynolds_1972]: https://doi.org/10.1023/A:1010027404223
[research_rgranli_1993]: https://doi.org/10.3997/2214-4609.201411447
[research_ricardo_santosjunior_2025]: https://doi.org/10.5753/sblp.2025.12264
[research_ricketts_malecha_2015]: https://doi.org/10.1109/memcod.2015.7340492
[research_rinard_2026]: https://doi.org/10.1145/3819802.3820579
[research_ritchie_popovici_2005]: https://doi.org/10.1190/1.2142225
[research_rivera_franchetti_2021]: https://doi.org/10.1109/cgo51591.2021.9370307
[research_rivera_franchetti_2022]: https://doi.org/10.1109/cgo53902.2022.9741286
[research_robbins_1984]: https://doi.org/10.1145/502874.502904
[research_roberts_1995]: https://doi.org/10.3997/2214-4609.201409442
[research_robin_khan_2024]: https://doi.org/10.1016/j.comnet.2024.110246
[research_rodriguez_martin_2009]: https://doi.org/10.1002/cpe.1541
[research_rodriguez_pagano_2016]: https://doi.org/10.1016/j.entcs.2016.06.013
[research_rodriguezferrandez_joveralvarez_2023]: https://doi.org/10.1145/3631483.3631502
[research_roessle_verbeek_2019]: https://doi.org/10.1145/3293880.3294102
[research_rogers_1993]: https://doi.org/10.21236/ada291202
[research_rohr_lindenstruth_2017]: https://doi.org/10.1109/cluster.2017.101
[research_rokotyanskaya_abramov_2023]: https://doi.org/10.24143/2072-9502-2023-2-93-100
[research_romano_wang_2023]: https://doi.org/10.1145/3611643.3616311
[research_rompf_amin_2019]: https://doi.org/10.1017/s0956796819000054
[research_rong_2009]: https://doi.org/10.1145/1669112.1669123
[research_rong_yu_2025]: https://doi.org/10.1109/icse55347.2025.00130
[research_rosa_basso_2023]: https://doi.org/10.1109/apsec60848.2023.00080
[research_rose_2003]: https://doi.org/10.1023/b:jars.0000021015.15794.82
[research_rosenblum_miller_2010]: https://doi.org/10.1145/1806672.1806678
[research_rosing_schnabel_1990]: https://doi.org/10.21236/ada459435
[research_rosu_2018]: https://doi.org/10.1007/s10703-018-0321-3
[research_rot_bonsangue_2016]: https://doi.org/10.1016/j.ic.2015.11.009
[research_rowland_perugini_2025]: https://doi.org/10.22152/programming-journal.org/2025/10/7
[research_roy_2023]: https://doi.org/10.1109/icse-seet58685.2023.00021
[research_roy_morozov_2019]: https://doi.org/10.5220/0007259102130220
[research_royer_1986]: https://doi.org/10.1145/12276.13318
[research_royuela_ferrer_2015]: https://doi.org/10.1145/2742854.2742882
[research_ruan_chen_2015]: https://doi.org/10.1109/cluster.2015.46
[research_ruberg_lass_2017]: https://doi.org/10.1109/aieee.2017.8270530
[research_ruchkin_mahmudov_2016]: https://doi.org/10.1109/meco.2016.7525697
[research_ruchkin_romanchuk_2017]: https://doi.org/10.1109/meco.2017.7977243
[research_rudmik_lee_1979]: https://doi.org/10.1145/872732.806962
[research_rudolph_thiemann_2010]: https://doi.org/10.1007/s10990-011-9077-9
[research_ruggedized_minicomputer_1981]: https://ntrs.nasa.gov/citations/19820006956
[research_rushby_2002]: https://doi.org/10.21236/ada403303
[research_russinoff_1992]: https://doi.org/10.1016/0743-1066(92)90054-7
[research_ryu_park_2019]: https://doi.org/10.1109/ms.2018.110113408
[research_s_v_2025]: https://doi.org/10.1109/ciscon66933.2025.11337437
[research_sabry_felleisen_1992]: https://doi.org/10.1145/141478.141563
[research_sabry_felleisen_1993]: https://doi.org/10.1007/bf01019462
[research_sabry_felleisen_1994]: https://doi.org/10.1145/773473.178244
[research_sack_2025]: https://doi.org/10.3390/philosophies10040086
[research_sadanandgiri_subash_2024]: https://doi.org/10.1016/j.hybadv.2024.100237
[research_sadasue_isshiki_2023]: https://doi.org/10.2197/ipsjtsldm.16.12
[research_sadat_2005]: https://doi.org/10.3923/jas.2005.1466.1469
[research_sager_1985]: https://doi.org/10.1145/382286.382384
[research_sah_islam_2018]: https://doi.org/10.1109/asianhost.2018.8607169
[research_sahkhar_balabantaray_2022]: https://doi.org/10.4018/ijismd.297630
[research_sai_tyagi_2022]: https://doi.org/10.1109/pdgc56933.2022.10053307
[research_saieva_kaiser_2020]: https://doi.org/10.1145/3411502.3418424
[research_salama_qazi_2018]: https://doi.org/10.18844/gjit.v8i3.4051
[research_salanki_sarvajcz_2019]: https://doi.org/10.33894/mtk-2019.11.37
[research_salapura_harper_2015]: https://doi.org/10.5220/0005493405590564
[research_salapura_harper_2015_2]: https://doi.org/10.1109/cloud.2015.52
[research_saleh_schrijvers_2016]: https://doi.org/10.1017/s147106841600034x
[research_salim_nisbet_2019]: https://doi.org/10.1145/3359061.3362780
[research_sambasivam_subramanian_2021]: https://doi.org/10.1145/3493425.3502769
[research_samet_1976]: https://doi.org/10.1145/800191.805648
[research_samet_1977]: https://doi.org/10.1145/872736.806945
[research_samet_1980]: https://doi.org/10.1145/357103.357106
[research_samiei_kahani_2024]: https://doi.org/10.1109/cascon62161.2024.10838116
[research_sammler_hammond_2022]: https://doi.org/10.1145/3519939.3523434
[research_sanada_2023]: https://doi.org/10.46298/entics.10491
[research_sanada_2024]: https://doi.org/10.1017/s0956796824000066
[research_sanders_srivastava_2020]: https://doi.org/10.1109/ispdc51135.2020.00018
[research_sangiorgi_2022]: https://doi.org/10.1145/3498679
[research_sanmorino_2012]: https://doi.org/10.1109/gut.2012.6344164
[research_santhi_eidenbenz_2015]: https://doi.org/10.1109/wsc.2015.7408405
[research_santhiar_kanade_2017]: https://doi.org/10.1145/3062341.3062361
[research_santhikumar_sahayasheela_2025]: https://doi.org/10.1109/icetea64585.2025.11099995
[research_santo_matthes_2009]: https://doi.org/10.2168/lmcs-5(2:11)2009
[research_santone_2011]: https://doi.org/10.1145/1985404.1985422
[research_santos_carro_2024]: https://doi.org/10.1145/3638249
[research_santos_lima_2018]: https://doi.org/10.1145/3211332.3211334
[research_sanusi_ogunshile_2024]: https://doi.org/10.1145/3686614.3686622
[research_saraf_dashora_2013]: https://doi.org/10.5120/13708-1461
[research_sato_2021]: https://doi.org/10.4216/jpssj.53.2_3
[research_sato_iwayama_2019]: https://doi.org/10.1145/3294032.3294081
[research_satyatejamuddada_2025]: https://doi.org/10.22399/ijcesen.4130
[research_schafer_schneider_2016]: https://doi.org/10.1145/2854065.2854083
[research_scheidl_2020]: https://doi.org/10.1109/iccece49321.2020.9231154
[research_schiewe_2022]: https://doi.org/10.1145/3477314.3508371
[research_schkufza_wei_2019]: https://doi.org/10.1145/3297858.3304010
[research_schlagl_groe_2025]: https://doi.org/10.23919/date64628.2025.10992929
[research_schlichtkrull_rydhofhansen_2024]: https://doi.org/10.1145/3605098.3636091
[research_schliephake_aguilar_2011]: https://doi.org/10.1016/j.procs.2011.04.230
[research_schmale_temesi_2022]: https://doi.org/10.1109/qsw55613.2022.00020
[research_schmeck_1983]: https://doi.org/10.1016/s0019-9958(83)80032-1
[research_schmidt_2000]: https://doi.org/10.1145/340855.341017
[research_schmidt_voller_1984]: https://doi.org/10.1145/502874.502894
[research_schmidtschauss_sabel_2015]: https://doi.org/10.1145/2790449.2790512
[research_schmitz_1992]: https://doi.org/10.1145/157710.157814
[research_schnakenbeck_mross_2023]: https://doi.org/10.1109/indin51400.2023.10218176
[research_schneider_brandt_2006]: https://doi.org/10.1016/j.entcs.2006.02.028
[research_schoeberl_puffitsch_2010]: https://doi.org/10.1002/spe.968
[research_schoenberger_hillmich_2024]: https://doi.org/10.1109/qce60285.2024.00129
[research_schopp_2017]: https://doi.org/10.1145/3131851.3131868
[research_schuele_schneider_2004]: https://doi.org/10.1145/996566.996602
[research_schuiki_kurth_2020]: https://doi.org/10.1145/3385412.3386024
[research_schuster_brachthauser_2020]: https://doi.org/10.1145/3408975
[research_schuster_brachthauser_2022]: https://doi.org/10.1145/3519939.3523710
[research_schwaab_siek_2013]: https://doi.org/10.1145/2428116.2428120
[research_schwarcz_berlakovich_2024]: https://doi.org/10.1145/3678722.3685533
[research_schwarz_kamm_2026]: https://doi.org/10.1109/cgo68049.2026.11395208
[research_scott_1986]: https://doi.org/10.21236/ada179522
[research_sculthorpe_torrini_2016]: https://doi.org/10.4204/eptcs.212.5
[research_seassau_yoon_2025]: https://doi.org/10.1145/3747509
[research_segura_2026]: https://doi.org/10.1007/s00607-026-01699-w
[research_seidler_michelis_2026]: https://doi.org/10.1109/rtas68450.2026.00024
[research_sekiyama_unno_2023]: https://doi.org/10.1145/3571264
[research_sen_wagner_2000]: https://doi.org/10.1190/1.1816168
[research_seo_kim_2016]: https://doi.org/10.7472/jksii.2016.17.4.51
[research_seo_kim_2016_2]: https://doi.org/10.1109/icis.2016.7550831
[research_seo_yang_2007]: https://doi.org/10.1145/1286821.1286830
[research_serafin_ghosh_2023]: https://doi.org/10.1145/3613424.3614283
[research_serrano_2021]: https://doi.org/10.1145/3473575
[research_serrano_2022]: https://doi.org/10.1145/3546918.3560825
[research_seshia_rakhlin_2009]: https://doi.org/10.21236/ada538736
[research_sethi_1982]: https://doi.org/10.1145/800230.806999
[research_sewell_2013]: https://doi.org/10.1145/2491956.2462183
[research_seyfer_1982]: https://doi.org/10.1145/800230.806990
[research_shahrokhi_groeger_2023]: https://doi.org/10.1145/3555041.3589735
[research_shaikhha_huot_2024]: https://doi.org/10.1109/cgo57630.2024.10444787
[research_shan_2007]: https://doi.org/10.1007/s10990-007-9010-4
[research_shannon_1948]: https://doi.org/10.1002/j.1538-7305.1948.tb00917.x
[research_sharif_muellergritschneder_2022]: https://doi.org/10.1109/meco55406.2022.9797144
[research_sharma_2025]: https://doi.org/10.31995/jgv.2025.v16isi.024
[research_sharma_reddy_2025]: https://doi.org/10.1109/iceteg66194.2025.11473223
[research_sharma_sharma_2024]: https://doi.org/10.1145/3641399.3641443
[research_sharma_yu_2023]: https://doi.org/10.1145/3597926.3604919
[research_sharp_1990]: https://doi.org/10.21236/ada632217
[research_sharrad_chitil_2018]: https://doi.org/10.1145/3310232.3310243
[research_sharygin_buchatskiy_2017]: https://doi.org/10.15514/ispras-2017-29(3)-11
[research_shcherbakov_shcherbakova_2024]: https://doi.org/10.33216/2222-3428-2024-27-5
[research_sheinidashtegol_galloway_2017]: https://doi.org/10.1109/ic2e.2017.18
[research_shen_2017]: https://doi.org/10.1145/3086467.3086469
[research_sherman_2018]: https://doi.org/10.1145/3236454.3236506
[research_sheth_damevski_2022]: https://doi.org/10.1007/s10515-022-00339-9
[research_shi_casey_2008]: https://doi.org/10.1145/1328195.1328197
[research_shih_1998]: https://doi.org/10.1016/s0020-0255(97)10040-8
[research_shih_chen_1996]: https://doi.org/10.3319/tao.1996.7.2.149(t)
[research_shiina_iwasaki_2021]: https://doi.org/10.1145/3437801.3441610
[research_shimchik_ignatyev_2021]: https://doi.org/10.1109/ispras53967.2021.00014
[research_shin_wang_2004]: https://doi.org/10.21236/ada425188
[research_shirai_nourry_2026]: https://doi.org/10.1145/3793302.3793358
[research_shivers_1991]: https://doi.org/10.1145/115865.115884
[research_shobaki_bassett_2022]: https://doi.org/10.1145/3497776.3517771
[research_sholihin_hidayati_2024]: https://doi.org/10.1109/3ict64318.2024.10824631
[research_shoushtary_arnau_2024]: https://doi.org/10.1109/isca59077.2024.00075
[research_shukla_nanjundappa_2014]: https://doi.org/10.21236/ada602193
[research_siambaton_azis_2024]: https://doi.org/10.56211/tsabit24
[research_sianipar_willems_2018]: https://doi.org/10.1109/soca.2018.00032
[research_silva_metrolho_2024]: https://doi.org/10.3390/fi16090341
[research_simon_kowalewski_2016]: https://doi.org/10.1109/etfa.2016.7733648
[research_simonnet_lemerre_2024]: https://doi.org/10.1145/3689712
[research_sinharoy_1988]: https://doi.org/10.21236/ada200722
[research_sites_1979]: https://doi.org/10.1145/800229.806973
[research_sivaramakrishnan_2021]: https://doi.org/10.1145/3453483.3454039
[research_siveroni_2004]: https://doi.org/10.1016/j.jlap.2003.07.003
[research_skarman_klemmer_2023]: https://doi.org/10.1109/fdl59689.2023.10272204
[research_smith_ramsey_2004]: https://doi.org/10.1145/996893.996875
[research_smith_zhang_2024]: https://doi.org/10.1145/3649852
[research_snavely_2011]: https://doi.org/10.21236/ada563246
[research_snyder_1975]: https://doi.org/10.21236/ada010218
[research_socket_system_2021]: https://doi.org/10.52899/978-5-88303-612-4_281
[research_sohrabi_ghods_2018]: https://doi.org/10.1109/iscbi.2018.00016
[research_sokhatskyi_maslianko_2018]: https://doi.org/10.1063/1.5045439
[research_soleimani_balarostaghi_2016]: https://doi.org/10.1007/s13202-016-0235-9
[research_soluian_lushenko_2025]: https://doi.org/10.34185/1562-9945-3-158-2025-19
[research_somani_srivastava_2019]: https://doi.org/10.2139/ssrn.3366275
[research_son_lee_2016]: https://doi.org/10.21742/ijwsesd.2016.3.2.04
[research_son_oh_2014]: https://doi.org/10.14257/astl.2014.60.10
[research_son_oh_2017]: https://doi.org/10.14257/ijca.2017.10.10.11
[research_song_wang_2021]: https://doi.org/10.1145/3468978.3468984
[research_sorensen_manocha_2020]: https://doi.org/10.1145/3400302.3415751
[research_souha_ouaddi_2025]: https://doi.org/10.1109/wincom65874.2025.11313419
[research_spampinato_puschel_2016]: https://doi.org/10.1145/2854038.2854060
[research_spivey_2017]: https://doi.org/10.1145/3110249
[research_squar_jammer_2020]: https://doi.org/10.1109/ispdc51135.2020.00016
[research_squire_funkhouser_2014]: https://doi.org/10.1109/hicss.2014.185
[research_srinivasan_reps_2015]: https://doi.org/10.1145/2737924.2737960
[research_stanisic_thibault_2015]: https://doi.org/10.1002/cpe.3555
[research_stappert_altenbernd_2000]: https://doi.org/10.1016/s1383-7621(99)00010-7
[research_stata_abadi_1998]: https://doi.org/10.1145/268946.268959
[research_stata_abadi_1999]: https://doi.org/10.1145/314602.314606
[research_steingartner_2021]: https://doi.org/10.1109/sami50585.2021.9378696
[research_stepanov_akhin_2021]: https://doi.org/10.1109/icst49551.2021.00044
[research_stepanov_itsykson_2022]: https://doi.org/10.31799/1684-8853-2022-6-31-40
[research_stepanov_klym_2025]: https://doi.org/10.30970/eli.32.10
[research_stievenart_binkley_2022]: https://doi.org/10.1145/3510003.3510070
[research_stohr_oboyle_1998]: https://doi.org/10.1016/s0167-739x(97)00040-x
[research_stolyarov_2023]: https://doi.org/10.32743/usaconf.2023.1.40.350415
[research_stoonkisto_subhlok_1997]: https://doi.org/10.21236/ada327279
[research_strachey_1974]: https://doi.org/10.1023/A:1010026413531
[research_strauch_2023]: https://doi.org/10.1145/3625223.3649276
[research_su_liao_2017]: https://doi.org/10.1109/cgo.2017.7863734
[research_subha_2009]: https://doi.org/10.1109/itng.2009.90
[research_subha_2010]: https://doi.org/10.1109/eit.2010.5612127
[research_subramanyan_2025]: https://doi.org/10.5121/csit.2025.151407
[research_suchy_campanoni_2020]: https://doi.org/10.1145/3385412.3385987
[research_suetterlein_manzano_2022]: https://doi.org/10.1016/j.jpdc.2022.01.027
[research_suganuma_yasue_2003]: https://doi.org/10.1145/781131.781166
[research_suhendra_bachtiar_2016]: https://doi.org/10.21609/jsi.v12i2.489
[research_sukha_2015]: https://doi.org/10.1145/2755573.2755610
[research_sular_poruban_2017]: https://doi.org/10.15546/aeei-2017-0001
[research_sulema_glinskii_2020]: https://doi.org/10.15407/pp2020.01.074
[research_sun_le_2016]: https://doi.org/10.1145/3022671.2984038
[research_sun_le_2016_2]: https://doi.org/10.1145/2931037.2931074
[research_sun_staron_2026]: https://doi.org/10.1109/saner67736.2026.00024
[research_sun_tu_2025]: https://doi.org/10.1145/3774949.3774968
[research_sun_zhong_2025]: https://doi.org/10.1109/icoecai67333.2025.11335621
[research_suo_chen_2024]: https://doi.org/10.1145/3650212.3680360
[research_supplemental_material_2022]: https://doi.org/10.1037/spy0000311.supp
[research_surakka_mikkonen_2005]: https://doi.org/10.3176/eng.2005.4.07
[research_surati_1993]: https://doi.org/10.21236/ada270838
[research_susca_mihaly_2022]: https://doi.org/10.1109/aqtr55203.2022.9802027
[research_suwa_tsukada_2017]: https://doi.org/10.1145/3018882.3018886
[research_svenkatesan_2025]: https://doi.org/10.12732/ijam.v38i11s.1286
[research_swierstra_viera_2016]: https://doi.org/10.1145/3064899.3064906
[research_swillus_zaidman_2023]: https://doi.org/10.1016/j.jss.2023.111804
[research_syme_2011]: https://doi.org/10.1007/978-3-642-18378-2_15
[research_syntax_directed_semantics_2026]: https://doi.org/10.64388/irev9i10-1716556
[research_szydelko_2018]: https://doi.org/10.15611/pn.2018.503.41
[research_tabassam_obermaisser_2017]: https://doi.org/10.1109/indin.2017.8104849
[research_tadepalli_li_2003]: https://doi.org/10.1190/1.1817654
[research_taft_2024]: https://doi.org/10.1007/s10009-024-00762-1
[research_tahat_joshi_2019]: https://doi.org/10.23919/fmcad.2019.8894252
[research_takase_mori_2018]: https://doi.org/10.1109/emsoft.2018.8537199
[research_talaat_hassan_2025]: https://doi.org/10.1109/icm66518.2025.11322450
[research_talamali_lounas_2024]: https://doi.org/10.1109/icaase64542.2024.10850926
[research_talu_2025]: https://doi.org/10.47852/bonviewaaes52024965
[research_tamura_kotani_2025]: https://doi.org/10.1145/3759426.3760985
[research_tan_2009]: https://doi.org/10.1007/s10009-008-0095-9
[research_tan_donaldson_2025]: https://doi.org/10.1109/formalise66629.2025.00010
[research_tan_myreen_2016]: https://doi.org/10.1145/3022670.2951924
[research_tan_owens_2015]: https://doi.org/10.1145/2897336.2897344
[research_tang_ren_2019]: https://doi.org/10.1007/s11704-019-8231-0
[research_tang_you_2010]: https://doi.org/10.1155/2010/986192
[research_tang_zeng_2025]: https://doi.org/10.1007/s10664-025-10642-0
[research_tant_diwakar_2023]: https://doi.org/10.1109/meco58584.2023.10155001
[research_tao_wu_2010]: https://doi.org/10.1109/apsec.2010.39
[research_tarau_2011]: https://doi.org/10.1017/s1471068411000433
[research_tardieu_2014]: https://doi.org/10.1145/3251064
[research_tarjan_1985]: https://doi.org/10.1137/0606031
[research_tatsuoka_kaneko_2018]: https://doi.org/10.1109/icicdt.2018.8399766
[research_tavares_colombet_2011]: https://doi.org/10.1145/1988932.1988934
[research_tempel_herdt_2021]: https://doi.org/10.1109/dac18074.2021.9586170
[research_tenhagen_steinberg_1996]: https://doi.org/10.1007/bf00134686
[research_terao_2018]: https://doi.org/10.1145/3236950.3236969
[research_terci_2023]: https://doi.org/10.1109/siu59756.2023.10223961
[research_thangamani_jost_2023]: https://doi.org/10.1145/3579990.3580008
[research_the_deasibility_2015]: https://doi.org/10.3837/tiis.2015.07.018
[research_the_role_2007]: https://doi.org/10.1109/sefm.2007.42
[research_the_utilization_2017]: https://doi.org/10.23883/ijrter.2017.3371.mfrag
[research_thielecke_2003]: https://doi.org/10.1145/640128.604144
[research_thielecke_2012]: https://doi.org/10.1145/2370776.2370789
[research_thiselton_treude_2019]: https://doi.org/10.1109/esem.2019.8870155
[research_thomas_salehi_2024]: https://doi.org/10.1109/dasc62030.2024.10749649
[research_thorpe_swiler_2022]: https://doi.org/10.1145/3546096.3546115
[research_thorpe_swiler_2022_2]: https://doi.org/10.2172/2002078
[research_tian_khaldi_2016]: https://doi.org/10.1109/icpp.2016.72
[research_tian_saito_2017]: https://doi.org/10.1145/3148173.3148191
[research_tian_wang_2024]: https://doi.org/10.1007/s11219-024-09673-5
[research_tillet_kung_2019]: https://doi.org/10.1145/3315508.3329973
[research_tine_yalamanchili_2019]: https://doi.org/10.1109/pact.2019.00055
[research_tinnerholm_sjolund_2019]: https://doi.org/10.1145/3365984.3365990
[research_tirichine_ameur_2026]: https://doi.org/10.1109/cgo68049.2026.11394838
[research_titzer_2024]: https://doi.org/10.1109/cgo57630.2024.10444855
[research_titzer_2025]: https://doi.org/10.1145/3746172
[research_todoran_2020]: https://doi.org/10.1109/iccp51029.2020.9266182
[research_todoran_ciobanu_2025]: https://doi.org/10.1109/synasc69064.2025.00028
[research_todoran_papaspyrou_2017]: https://doi.org/10.3233/fi-2017-1534
[research_tohid_wagle_2018]: https://doi.org/10.1109/espm2.2018.00009
[research_tokumori_ono_2007]: https://doi.org/10.2964/jsik.17.41
[research_tokumoto_yoshida_2016]: https://doi.org/10.1109/icst.2016.18
[research_tolpin_vandemeent_2016]: https://doi.org/10.1145/3064899.3064910
[research_touzeau_1984]: https://doi.org/10.1145/502874.502879
[research_tran_waimon_2023]: https://doi.org/10.7717/peerj-cs.1284
[research_trifanov_schrijvers_2026]: https://doi.org/10.1145/3779209.3779536
[research_trout_1967]: https://doi.org/10.1145/800196.806002
[research_truong_barik_2016]: https://doi.org/10.1145/2908080.2908105
[research_tsuyama_cong_2024]: https://doi.org/10.1145/3635800.3636968
[research_tu_jiang_2022]: https://doi.org/10.1109/issre55969.2022.00057
[research_tu_jiang_2023]: https://doi.org/10.1109/tr.2022.3171220
[research_tuck_1988]: https://doi.org/10.21236/ada201089
[research_turcotte_vitek_2019]: https://doi.org/10.1145/3340670.3342426
[research_tutorial_on_2009]: https://doi.org/10.1109/cgo.2009.46
[research_uddin_khomh_2020]: https://doi.org/10.1016/j.infsof.2020.106277
[research_ueno_ohori_2022]: https://doi.org/10.1145/3520263.3534652
[research_uh_2003]: https://doi.org/10.1145/3244027
[research_upadhyaya_rajan_2015]: https://doi.org/10.1145/2814270.2814289
[research_urban_subotic_2025]: https://doi.org/10.1016/j.scico.2025.103338
[research_utting_webb_2023]: https://doi.org/10.1109/formalise58978.2023.00015
[research_v_m_2019]: https://doi.org/10.21276/ijcesr.2019.6.6.34
[research_valiron_2022]: https://doi.org/10.1016/j.jlamp.2022.100790
[research_vandenbroucke_schrijvers_2023]: https://doi.org/10.1017/s1471068423000029
[research_vandercammen_marr_2018]: https://doi.org/10.1016/j.cl.2017.07.005
[research_vanderhoeven_lecerf_2021]: https://doi.org/10.1145/3452143.3465531
[research_vandeursen_1999]: https://doi.org/10.1016/s0167-6423(99)00003-9
[research_vanrooij_krebbers_2025]: https://doi.org/10.1145/3704841
[research_vantonder_legoues_2020]: https://doi.org/10.1145/3377811.3380343
[research_vasilyev_mutilin_2020]: https://doi.org/10.1134/s0361768820080071
[research_vegdahl_pleban_1989]: https://doi.org/10.1145/68182.68199
[research_veit_bocskei_2024]: https://doi.org/10.35551/pfq_2024_4_4
[research_velazquezrodriguez_constantinou_2022]: https://doi.org/10.1109/saner53432.2022.00035
[research_venkanna_rao_2018]: https://doi.org/10.14419/ijet.v7i2.33.14162
[research_venkanna_rao_2018_2]: https://doi.org/10.16925/.v14i0.2230
[research_venkatakeerthy_jain_2023]: https://doi.org/10.1145/3578360.3580273
[research_ventovaara_hasanbegovic_2020]: https://doi.org/10.1109/icit45562.2020.9067160
[research_vepuri_jiang_2023]: https://doi.org/10.1109/igessc59090.2023.10321757
[research_verdejo_martioliet_2006]: https://doi.org/10.1016/j.jlap.2005.09.008
[research_verma_bakshi_2015]: https://doi.org/10.13053/rcs-103-1-9
[research_verma_kaur_2023]: https://doi.org/10.1145/3623507.3623557
[research_virtual_machine_2017]: https://doi.org/10.21275/22121601
[research_vistaresearchcorptucsonaz_1994]: https://doi.org/10.21236/ada278081
[research_vistaresearchcorptucsonaz_1994_2]: https://doi.org/10.21236/ada278080
[research_vizcaino_mantovani_2022]: https://doi.org/10.1002/cpe.7424
[research_voigt_schuster_2025]: https://doi.org/10.1145/3763155
[research_vonbehren_2003]: https://doi.org/10.1145/945445.945471
[research_vos_conti_2023]: https://doi.org/10.1145/3689945.3694808
[research_vrany_shingarov_2024]: https://doi.org/10.1145/3660829.3660838
[research_vsamuelblessednayagam_shajinnargunam_2018]: https://doi.org/10.14419/ijet.v7i4.36.24140
[research_vu_2008]: https://doi.org/10.1016/j.jlap.2007.05.002
[research_wagle_monil_2019]: https://doi.org/10.1145/3337821.3337915
[research_wagstaffkiril_benowitzedward_2008]: https://ntrs.nasa.gov/citations/20090031888
[research_wahyudi_miswanto_2020]: https://doi.org/10.35200/explore.v9i2.225
[research_waites_misirli_2018]: https://doi.org/10.1021/acssynbio.8b00201
[research_wall_1986]: https://doi.org/10.1145/12276.13338
[research_wall_1988]: https://doi.org/10.1145/960116.53997
[research_wall_2004]: https://doi.org/10.1145/989393.989422
[research_wambua_2025]: https://doi.org/10.24203/dfjd8332
[research_wang_2017]: https://doi.org/10.1109/icmtma.2017.0102
[research_wang_2019]: https://doi.org/10.1109/icicas48597.2019.00118
[research_wang_2021]: https://doi.org/10.1109/csaiee54046.2021.9543457
[research_wang_2021_2]: https://doi.org/10.1145/3446804.3446851
[research_wang_2024]: https://doi.org/10.1109/access.2024.3432811
[research_wang_chen_2023]: https://doi.org/10.1109/ase56229.2023.00120
[research_wang_dahl_1971]: https://doi.org/10.1007/bf01939412
[research_wang_gu_2015]: https://doi.org/10.1109/tvlsi.2014.2379635
[research_wang_han_2025]: https://doi.org/10.1109/eiecc67963.2025.11409518
[research_wang_huang_2022]: https://doi.org/10.1016/j.parco.2022.102980
[research_wang_huang_2022_2]: https://doi.org/10.2139/ssrn.4022101
[research_wang_jia_2014]: https://doi.org/10.1109/iscas.2014.6865319
[research_wang_jung_2024]: https://doi.org/10.1145/3689780
[research_wang_li_2019]: https://doi.org/10.1016/j.jss.2018.11.003
[research_wang_linghu_2023]: https://doi.org/10.1109/asicon58565.2023.10396051
[research_wang_lu_2022]: https://doi.org/10.1109/tdsc.2021.3079857
[research_wang_lu_2026]: https://doi.org/10.1016/j.scico.2025.103359
[research_wang_qiu_2010]: https://doi.org/10.1109/tase.2010.24
[research_wang_shen_2020]: https://doi.org/10.1109/cloud49709.2020.00089
[research_wang_wang_2024]: https://doi.org/10.1145/3626205.3659149
[research_wang_wu_2009]: https://doi.org/10.1109/cse.2009.100
[research_wang_xie_2023]: https://doi.org/10.23919/date56975.2023.10137308
[research_wang_xie_2024]: https://doi.org/10.1142/s0218194024500475
[research_wang_xiong_2017]: https://doi.org/10.1145/3092703.3092714
[research_wang_yang_2014]: https://doi.org/10.4028/www.scientific.net/amr.952.325
[research_wang_zhang_2019]: https://doi.org/10.1109/icws.2019.00024
[research_wang_zhou_2023]: https://doi.org/10.1109/saner56733.2023.00041
[research_wang_zhu_2011]: https://doi.org/10.1109/hase.2011.56
[research_wanxin_tao_2022]: https://doi.org/10.1109/cbd58033.2022.00044
[research_watanabe_lee_2020]: https://doi.org/10.1145/3373271.3373274
[research_watt_2025]: https://doi.org/10.1145/3747201.3746173
[research_webassembly_for_high_performance_2021]: https://doi.org/10.71097/ijsat.v12.i2.2812
[research_weber_fischer_2020]: https://doi.org/10.1145/3419804.3421450
[research_weber_wiesner_2022]: https://doi.org/10.1016/j.infsof.2021.106695
[research_wei_jia_2023]: https://doi.org/10.1109/icse48619.2023.00116
[research_weiner_ramakrishman_1988]: https://doi.org/10.1145/53990.54019
[research_welch_durkee_2017]: https://doi.org/10.1145/3098572.3098580
[research_wenes_kremer_1994]: https://doi.org/10.3997/2214-4609.201409898
[research_wenger_zhu_2016]: https://doi.org/10.1109/cic.2016.033
[research_wheeler_bate_2011]: https://doi.org/10.1109/sies.2011.5953664
[research_whiteside_yeh_2012]: https://doi.org/10.1190/segam2012-1184.1
[research_wibowo_hendradjaya_2015]: https://doi.org/10.1109/icodse.2015.7437005
[research_wilhelm_2008]: https://doi.org/10.1145/1347375.1347389
[research_williams_bulmer_1978]: https://doi.org/10.1002/spe.4380080507
[research_williams_elliott_2025]: https://doi.org/10.1109/tpds.2025.3543442
[research_williams_roger_2009]: https://doi.org/10.1109/iwast.2009.5069045
[research_wilson_1989]: https://doi.org/10.21236/ada212548
[research_wilson_1989_2]: https://doi.org/10.21236/ada212550
[research_wilson_1989_3]: https://doi.org/10.21236/ada212551
[research_wilson_1989_4]: https://doi.org/10.21236/ada212437
[research_wilson_1990]: https://doi.org/10.21236/ada218688
[research_wilson_1990_2]: https://doi.org/10.21236/ada218687
[research_wimmer_jovanovic_2017]: https://doi.org/10.1145/3033019.3033025
[research_windsor_donaldson_2021]: https://doi.org/10.1145/3460319.3469079
[research_woronow_1989]: https://doi.org/10.1016/0098-3004(89)90019-8
[research_worst_case_2016]: https://doi.org/10.18178/wcse.2016.06.002
[research_worthington_2021]: https://doi.org/10.1145/3486606.3488073
[research_wu_2023]: https://doi.org/10.1145/3579990.3583093
[research_wu_bie_2021]: https://doi.org/10.1109/asicon52560.2021.9620475
[research_wu_fan_2026]: https://doi.org/10.1103/52wr-1hys
[research_wu_he_2025]: https://doi.org/10.1145/3696410.3714622
[research_wu_li_2007]: https://doi.org/10.1109/icnc.2007.366
[research_wu_liu_2026]: https://doi.org/10.1109/fccm68464.2026.00077
[research_wu_schrijvers_2014]: https://doi.org/10.1145/2633357.2633358
[research_wu_sun_2026]: https://doi.org/10.1063/5.0314659
[research_wu_yang_2023]: https://doi.org/10.1109/saner56733.2023.00061
[research_wu_yin_2017]: https://doi.org/10.2991/amms-17.2017.7
[research_wu_zhang_2012]: https://doi.org/10.1145/2331147.2331166
[research_wu_zhang_2013]: https://doi.org/10.1109/pccc.2013.6742770
[research_wu_zhang_2018]: https://doi.org/10.1142/s0218126618500809
[research_wu_zheng_2025]: https://doi.org/10.1145/3696630.3728528
[research_wurthinger_wimmer_2017]: https://doi.org/10.1145/3062341.3062381
[research_xiang_xu_2026]: https://doi.org/10.1145/3814943.3816166
[research_xiao_2021]: https://doi.org/10.1109/icitbs53129.2021.00153
[research_xiao_chen_2023]: https://doi.org/10.32604/csse.2023.027081
[research_xiasongtao_divitobenedettol_2005]: https://ntrs.nasa.gov/citations/20050240928
[research_xie_brachthauser_2020]: https://doi.org/10.1145/3408981
[research_xie_cong_2022]: https://doi.org/10.1145/3563289
[research_xie_johnson_2024]: https://doi.org/10.1145/3674651
[research_xie_leijen_2020]: https://doi.org/10.1145/3406088.3409022
[research_xie_leijen_2021]: https://doi.org/10.1145/3473576
[research_xie_xu_2025]: https://doi.org/10.1145/3713081.3731731
[research_xu_gregg_2015]: https://doi.org/10.1109/pact.2015.56
[research_xu_kjolstad_2021]: https://doi.org/10.1145/3485513
[research_xu_wang_2020]: https://doi.org/10.1109/ijcnn48605.2020.9206911
[research_xu_zhang_2014]: https://doi.org/10.1109/icrms.2014.7107200
[research_xu_zhou_2024]: https://doi.org/10.1109/saner60148.2024.00101
[research_xu_zhu_2016]: https://doi.org/10.1109/sose.2016.46
[research_xue_bogdan_2016]: https://doi.org/10.1145/2968456.2968471
[research_yadav_aiken_2022]: https://doi.org/10.1145/3519939.3523437
[research_yallop_sheets_2018]: https://doi.org/10.1016/j.scico.2017.04.002
[research_yamamoto_oyama_2016]: https://doi.org/10.1109/cpsna.2016.23
[research_yamane_kobashi_2020]: https://doi.org/10.3390/electronics9071060
[research_yamato_2015]: https://doi.org/10.1109/icufn.2015.7182660
[research_yan_zhang_2008]: https://doi.org/10.1145/1457246.1457253
[research_yaneva_rajan_2017]: https://doi.org/10.1145/3092703.3092720
[research_yang_2011]: https://doi.org/10.1145/1993498.1993532
[research_yang_2018]: https://doi.org/10.23940/ijpe.18.08.p9.17261734
[research_yang_banerjee_2025]: https://doi.org/10.1109/isqed65160.2025.11014422
[research_yang_bodeveix_2015]: https://doi.org/10.1007/s11704-015-4364-y
[research_yang_deng_2024]: https://doi.org/10.1145/3689736
[research_yang_duan_2008]: https://doi.org/10.1016/j.jlap.2008.08.001
[research_yang_ruizvarela_2015]: https://doi.org/10.1109/vlsi-soc.2015.7314397
[research_yang_wang_2022]: https://doi.org/10.1109/dsa56465.2022.00087
[research_ye_delaware_2019]: https://doi.org/10.1145/3293880.3294105
[research_ye_hu_2023]: https://doi.org/10.1145/3611643.3616332
[research_ye_zhu_2025]: https://doi.org/10.1109/tdsc.2024.3391795
[research_yesua_rahardjo_2019]: https://doi.org/10.14710/jai.v11i1.22039
[research_yi_2011]: https://doi.org/10.1109/cgo.2011.5764678
[research_yi_ding_2026]: https://doi.org/10.1145/3798245
[research_yi_lee_2018]: https://doi.org/10.18517/ijaseit.8.4-2.5735
[research_yildiz_iskender_2019]: https://doi.org/10.1109/ubmk.2019.8907220
[research_yilmazermetin_2021]: https://doi.org/10.1002/cpe.6483
[research_yim_kim_2019]: https://doi.org/10.1109/bmsb47279.2019.8971863
[research_yin_pan_2020]: https://doi.org/10.1145/3418994.3419010
[research_yoo_kim_2017]: https://doi.org/10.14257/ajmahs.2017.09.79
[research_yoshikawa_shimura_2003]: https://doi.org/10.1109/qsic.2003.1319081
[research_yoshioka_sekiyama_2024]: https://doi.org/10.1145/3674641
[research_you_chen_2015]: https://doi.org/10.1109/cases.2015.7324550
[research_you_lu_2012]: https://doi.org/10.1109/icsai.2012.6223542
[research_yu_2008]: https://doi.org/10.3724/sp.j.1087.2008.00522
[research_yu_2009]: https://doi.org/10.1109/intensive.2009.8
[research_yu_2023]: https://doi.org/10.1145/3597926.3605239
[research_yu_cohen_2015]: https://doi.org/10.1109/icst.2015.7102592
[research_yu_haque_2011]: https://doi.org/10.1504/ijwgs.2011.043532
[research_yu_yang_2007]: https://doi.org/10.1145/1244002.1244114
[research_yu_yi_2023]: https://doi.org/10.1109/saner56733.2023.00030
[research_yvon_feeley_2021]: https://doi.org/10.1145/3486606.3486783
[research_zaitsev_guliaiev_2011]: https://doi.org/10.4236/jsea.2011.46043
[research_zakowski_he_2020]: https://doi.org/10.1145/3372885.3373813
[research_zaks_pnueli_2008]: https://doi.org/10.1145/1512475.1512477
[research_zanardini_2008]: https://doi.org/10.1109/scam.2008.19
[research_zapanov_2025]: https://doi.org/10.1109/edm65517.2025.11096859
[research_zaytsev_2018]: https://doi.org/10.1145/3276604.3276619
[research_zaytsev_2020]: https://doi.org/10.5381/jot.2020.19.2.a5
[research_zelenova_2025]: https://doi.org/10.1134/s036176882570032x
[research_zelkowitz_1975]: https://doi.org/10.1145/800181.810332
[research_zendra_colnet_2001]: https://doi.org/10.1002/spe.373
[research_zeng_wu_2026]: https://doi.org/10.1145/3765760
[research_zhang_2016]: https://doi.org/10.5220/0006448202420245
[research_zhang_2018]: https://doi.org/10.1145/3159450.3162242
[research_zhang_2025]: https://doi.org/10.5220/0014350200004718
[research_zhang_bond_2022]: https://doi.org/10.1145/3497776.3517778
[research_zhang_burns_1993]: https://doi.org/10.1007/bf01088834
[research_zhang_cao_2023]: https://doi.org/10.1145/3624743
[research_zhang_deng_2018]: https://doi.org/10.3997/2214-4609.201800728
[research_zhang_deng_2026]: https://doi.org/10.3390/ijgi15070310
[research_zhang_jiang_2026]: https://doi.org/10.1109/tr.2026.3662048
[research_zhang_koutsoukos_2015]: https://doi.org/10.1145/2808704.2754967
[research_zhang_liu_2019]: https://doi.org/10.1109/tcc.2017.2656088
[research_zhang_meng_2020]: https://doi.org/10.1145/3441250.3441261
[research_zhang_myers_2019]: https://doi.org/10.1145/3290318
[research_zhang_ping_2011]: https://doi.org/10.2523/iptc-14474-ms
[research_zhang_shen_2025]: https://doi.org/10.3390/app15052407
[research_zhang_sun_2017]: https://doi.org/10.1145/3062341.3062379
[research_zhang_venkat_2016]: https://doi.org/10.1109/ia3.2016.011
[research_zhang_vijayaraghavan_2017]: https://doi.org/10.1109/pact.2017.29
[research_zhang_wu_2013]: https://doi.org/10.1109/trustcom.2013.113
[research_zhang_xiao_2026]: https://doi.org/10.1145/3798258
[research_zhang_xing_2023]: https://doi.org/10.34133/icomputing.0040
[research_zhang_yan_2009]: https://doi.org/10.1109/rtcsa.2009.55
[research_zhang_yin_2021]: https://doi.org/10.32604/jiot.2021.016936
[research_zhang_zhao_2024]: https://doi.org/10.18653/v1/2024.findings-emnlp.55
[research_zhang_zhao_2026]: https://doi.org/10.1007/s42514-025-00272-9
[research_zhang_zheng_2020]: https://doi.org/10.1109/access.2020.3038170
[research_zhao_fu_2025]: https://doi.org/10.1016/j.cose.2024.104171
[research_zhao_he_2024]: https://doi.org/10.1109/iseda62518.2024.10617942
[research_zhao_li_2026]: https://doi.org/10.1145/3770854.3785697
[research_zhao_liao_2024]: https://doi.org/10.1109/iucc65928.2024.00031
[research_zhao_sheng_2021]: https://doi.org/10.3390/electronics10182210
[research_zhao_zeng_2024]: https://doi.org/10.1145/3650212.3680340
[research_zhao_zhang_2021]: https://doi.org/10.1049/sfw2.12013
[research_zheng_xia_2019]: https://doi.org/10.1016/j.peva.2019.102035
[research_zhong_2022]: https://doi.org/10.1145/3551349.3556894
[research_zhong_kaiser_2023]: https://doi.org/10.1109/tse.2022.3195640
[research_zhong_lv_2026]: https://doi.org/10.1109/saner67736.2026.00069
[research_zhong_lyu_2024]: https://doi.org/10.52202/079017-3567
[research_zhong_qiu_2026]: https://doi.org/10.1145/3774895.3812193
[research_zhong_sun_2026]: https://doi.org/10.1145/3764585
[research_zhou_1996]: https://doi.org/10.1145/236114.236120
[research_zhou_jiang_2024]: https://doi.org/10.32604/cmes.2023.043248
[research_zhou_li_2016]: https://doi.org/10.1145/2930957.2930959
[research_zhou_mu_2016]: https://doi.org/10.1109/chicc.2016.7554171
[research_zhou_wu_2020]: https://doi.org/10.1145/3404687.3404700
[research_zhou_xue_2016]: https://doi.org/10.1145/2886101
[research_zhu_2001]: https://doi.org/10.1145/609769.609777
[research_zhu_he_2007]: https://doi.org/10.1109/sew.2007.52
[research_zhu_he_2008]: https://doi.org/10.1007/s11334-008-0069-9
[research_zhu_wang_2019]: https://doi.org/10.1109/icstw.2019.00064
[research_zhu_wang_2025]: https://doi.org/10.1145/3755881.3755917
[research_zhu_xie_2025]: https://doi.org/10.1109/icmlca66850.2025.11336697
[research_zhu_yang_2009]: https://doi.org/10.1109/sew.2009.17
[research_zhu_yang_2012]: https://doi.org/10.1016/j.jlap.2011.06.003
[research_zhu_zhao_2009]: https://doi.org/10.1109/aswec.2009.20
[research_zolda_bunte_2011]: https://doi.org/10.1109/rtcsa.2011.73
[research_zolduoarrati_licorish_2025]: https://doi.org/10.1016/j.jss.2025.112338
[research_zou_wang_2022]: https://doi.org/10.1145/3494516
[research_zou_xu_2017]: https://doi.org/10.1016/j.infsof.2016.12.003
[research_zubarev_2017]: https://doi.org/10.31144/si.2307-6410.2017.n9.p1-22
[research_zuepke_kaiser_2019]: https://doi.org/10.1109/rtas.2019.00014
[research_zuniga_belenguix_2020]: https://doi.org/10.3390/math8091573
[research_zwanziger_2019]: https://doi.org/10.18653/v1/w19-5704
[research_zyuzin_nanevski_2021]: https://doi.org/10.1145/3473580
