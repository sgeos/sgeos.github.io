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
**stricter than the property it enforces**, excluding ten of twenty-four cases for no reason. That was found
while gathering data for this article rather than by any test.

### How to read this

**The general argument is in the opening, in the section called The Argument That Settled It, and in Pattern Extraction. Those three need nothing but attention.**
The sections between them work the argument through a real case with real numbers, and they use the
vocabulary of the trade. Every term is glossed at first use, but a reader who wants the result rather than
the machinery can take those three and stop.

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
rescue it, because the loss lives in the interface rather than in the instances.

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

The nested case looked like the hard one until it was measured per suspension rather than per chunk. All
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
because the deficiency is in the calling convention rather than in the chunk.

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

**The same statement in bits is the one that generalises.** An interface of $m$ machine words carries $64m$
bits and a trace of $k$ words needs $64k$, so a faithful encoding requires

$$64k \;\le\; 64m \qquad \Longleftrightarrow \qquad k \;\le\; m,$$

and here $k = 2$ against $m = 1$. **The shortfall is 64 bits**, which is to say a whole second word.

The general statement is immediate. For any chunk $k$ and convention $\varepsilon$,

$$\mathrm{obs}(k) \;>\; \mathrm{chan}(\varepsilon) \quad\Longrightarrow\quad \varepsilon \text{ is not injective on } \mathcal{T}(k),$$

and a non-injective encoding is one in which two distinct executions become indistinguishable to the host,
which is precisely what it means for a lowering to be wrong.

**The deficit does not grow with the number of suspensions, which is worth checking rather than assuming.**
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
**The expensive-sounding option costs one bit of information and one register of encoding**, which is a very
different proposition from carrying a second word. The pigeonhole refutes the unification *at the signature
the backend currently emits*, not for all time.

That distinction matters and it was not visible from inside the problem. It surfaces a **third option** ,
which is to widen every coroutine entry point so that it returns a discriminated pair,

$$f : W \longrightarrow (\,\mathsf{tag} \in \{\mathsf{Y}, \mathsf{F}\},\; W\,)$$

so that one convention carries both trace alphabets. The cost is that every call of every coroutine pays a
wider return and a host-side discrimination, including the **95.83 percent** of the corpus, twenty-three
chunks of twenty-four, that need only one letter.

**Whether that is cheaper than two conventions is an empirical question this article does not answer, and the shape of the comparison can be stated without measuring anything.**
Writing $c_{\mathrm{tag}}$ for the per-call cost of the discriminator and $c_{\mathrm{meta}}$ for the
one-off cost of declaring and dispatching two conventions, the totals over $N$ calls are

$$C_{\mathrm{one}} = c_{\mathrm{tag}} N, \qquad C_{\mathrm{two}} = c_{\mathrm{meta}},$$

so the widened return is cheaper only below

$$N^{*} \;=\; \frac{c_{\mathrm{meta}}}{c_{\mathrm{tag}}}.$$

**A per-call term always loses to a constant eventually**, and a stream abstraction exists to be called many
times, so the crossover is the whole question.
**Neither constant is published and this article declines to invent them**, which is why the recommendation
below rests on the memory property rather than on a cost model.

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
which is a statement about the type rather than about how unlikely the value is. Kotlin can afford it
because the sentinel is a reference no user value aliases. A backend whose yielded values are arbitrary
machine words cannot, so for Keleusma the tagged pair is the honest form and the sentinel is unavailable.

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
consumes the $k$-th resume value, which is exactly what the virtual machine does when it writes the resume
value into the entry chunk's parameter slot.

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
the corpus the rule was written against and diverge on the next ten cases, which is the standard failure of
a whitelist standing in for a predicate.

**The cost is measurable and is not correctness.** Nothing is mislowered, because the rule refuses rather
than admits. The cost is coverage. Writing $R$ for what the rule admits and $P$ for what the property
licenses,

$$\frac{\lvert R \rvert}{\lvert K_\Sigma \rvert} \;=\; \frac{14}{24} \;=\; 58.33\%, \qquad \frac{\lvert P \rvert}{\lvert K_\Sigma \rvert} \;=\; \frac{24}{24} \;=\; 100\%,$$

so **41.67 percent of the corpus is refused the cheap convention for no reason**, and ten stream chunks that
could use it currently do not. The fix is a small generalisation and it is not attempted here, because this
article's subject is the convention question and a coverage improvement inside it would be a second claim
wearing the first one's clothes.

**It is reported because it was found by writing rather than by testing**, which is the second time in this
series that assembling a table for publication has surfaced something a green test suite did not.

## Method

The instrument compiles every `.kel` source in the project's example directories, the self-hosted compiler
stage sources, and the standalone compiler subproject, discarding any that fail to compile. For each
resulting module it walks every chunk and classifies it.

Suspension nesting is computed with a depth counter over the block-opening instruction set, which was
checked against the full block-structured instruction list rather than assumed. A missed opener would report
a nested suspension as a top-level one and admit a chunk the transformation is wrong for.

The tail-position walk **follows jumps** rather than scanning the instruction stream linearly. This is
necessary rather than fastidious. The instructions textually between a deeply nested suspension and the
reset include the bodies of sibling branches, which are on different paths and never execute after that
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
deferred rather than done.

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
on the underlying proportion at confidence $1 - \alpha$ is

$$p_{\min} \;=\; \alpha^{1/n} \;=\; 0.05^{1/9} \;=\; 0.7169,$$

so **the observation is consistent with 28.31 percent of cases failing**, and at 99 percent confidence the
bound falls to 0.5995. A run of twenty-four would give 0.8827 and still leave 11.73 percent unexcluded, and
licensing a claim of 0.99 at the same confidence would need

$$n \;=\; \frac{\ln \alpha}{\ln 0.99} \;=\; 299$$

consecutive successes. **Nine is not a large number and the arithmetic says so.** That is a separate and
much weaker objection than the one this section rests on, because the counting argument does not need the
sample to be small. **It would refute the unification from a sample of a million.**

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

**Ruled out on evidence:** a single return-based convention for both forms **at a one-word return type**. It
is lossy for the terminating form and no shape analysis rescues it.

**Remaining, and genuinely open:**

**One convention with a widened return.** Every coroutine entry point returns a discriminated pair, which
the [System V AMD64][ref_sysv_amd64] and [AAPCS64][ref_aapcs64] register-pair rules make free of memory
traffic on the two targets that matter. One convention for the host, one discriminator to check, and the
frame property preserved. **This option exists only because the ABI documents were read**, and it was absent
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
coroutine, and if that call were restructured so the suspension belonged to the stream chunk rather than the
callee, the whole corpus would fit one convention. This is a change to the source program rather than the
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
compiler, and the motivating example was a compiler passing tokens between phases, which is close to the
present use. The taxonomy that still governs discussion is
[de Moura and Ierusalimschy 2009][research_demoura_2009], which separates coroutines along three axes,
**symmetric or asymmetric**, **first-class or constrained**, and **stackful or stackless**. Keleusma's two
forms are both asymmetric and constrained, and the article's question is precisely whether the backend must
be stackful.

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

### Continuation-passing style answers the representation question, expensively

The general transformation is known and exact. [Reynolds 1972][research_reynolds_1972] established
continuation passing as a definitional technique, [Strachey and Wadsworth 1974][research_strachey_1974] gave
it its semantics, and [Appel 1992][research_appel_1992] made it a compiler architecture. Under continuation
passing every suspension becomes a call to a continuation and the representation question dissolves, because
there are no returns to collide with.

**It dissolves the question by paying for it everywhere.** The transformation is global, it changes the
calling convention of every function rather than of coroutines alone, and the resulting closures are heap
allocated unless a later analysis recovers the stack discipline.
[Danvy and Nielsen 2001][research_danvy_nielsen_2001] show defunctionalisation recovering first-order code
from the higher-order form, which is the step that makes continuation passing implementable without a
garbage collector, and it is the step a bounded-memory project would have to trust.

Delimited control is the sharper tool. [Danvy and Filinski 1990][research_danvy_filinski_1990] introduced
`shift` and `reset`, [Felleisen 1988][research_felleisen_1988] the prompt-based formulation, and
[Dybvig, Peyton Jones and Sabry 2007][research_dybvig_2007] a monadic framework with an implementation
strategy. [Flatt and others 2007][research_flatt_2007] report adding delimited and composable control to a
production system, which is the closest thing in the literature to a cost report.
**A delimited continuation is exactly a coroutine frame**, and the delimiter is exactly the boundary this
article's reset instruction draws.

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

The alternative is stackful, which the operating-systems literature has costed thoroughly.
[von Behren and others 2003][research_vonbehren_2003] argue for threads with dynamically sized stacks
against event-driven code, and the stack-growth machinery they describe is what a stackful coroutine needs.
For a project whose memory bound must be static, that machinery is not available.

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

### Worst-case resource analysis is why the convention matters at all

If native code did not have to carry a bound, the callback convention would simply win on generality.
[Wilhelm and others 2008][research_wilhelm_2008] survey the worst-case execution-time problem and the tools
that address it, and it remains the standard reference for what a sound timing analysis requires. For the
memory side, [Regehr, Reid and Webb 2005][research_regehr_2005] eliminate stack overflow by abstract
interpretation of machine code, which is exactly the analysis a native Keleusma artefact must support and
exactly what a frame held across arbitrary host execution defeats.

**This is the literature that makes the choice non-obvious**, and it is the one the coroutine implementation
literature does not cite. A runtime that may allocate is free to choose the general mechanism. A bounded
artefact is not, and the trade appears only when both literatures are read together.

### Compiler testing supplies the oracle and warns about its limits

The differential method used here is standard. [Yang and others 2011][research_yang_2011] report Csmith and
the compiler defects it found, [Le, Afshari and Su 2014][research_le_2014] introduce equivalence modulo
inputs, and [Chen and others 2020][research_chen_2020] survey compiler testing as a field.

**The warning these carry is directly applicable.** A differential oracle refutes and does not prove, and
its power is bounded by the inputs supplied. This article's equivalence assertion is checked over a finite
sample of resume sequences chosen by hand, which is the weakest form of the technique. Equivalence modulo
inputs is the natural strengthening and it has not been applied.

### What the survey shows

**The representation question is settled in the literature and the selection question is not.** Four
independent traditions converge on a discriminated return for terminating coroutines, and none of them
addresses whether a bounded-memory artefact should pay that discrimination on every call of a construct that
never terminates. The present article contributes the observation that the two source forms have different
trace alphabets and that the choice can therefore be made per form rather than globally, which the surveyed
work does not consider because no surveyed language separates the two forms in its type system.

**That separation is Keleusma's own contribution to the problem**, and it is the reason the question is even
askable here. It is also why the survey cannot answer it.

## The Source Base

The generator is a detached package inside the Keleusma repository, consuming the reference compiler's
in-memory module representation and emitting [LLVM intermediate representation][ref_llvm_langref] through
the [inkwell][ref_inkwell] bindings. The bytecode it consumes has already passed a structural verifier, in
the tradition the [Java Virtual Machine Specification][ref_jvm_spec] sets out for bytecode verification, so
the backend refuses anything it cannot lower rather than approximating it. The classification instrument is
a test in the same package, reporting rather than asserting, with one guard that fails if the corpus walk
finds nothing, because a broken path and a real zero look identical in a report.

The differential oracle drives both the virtual machine and the just-in-time compiled native code over
identical bytecode and compares the whole sequence of yielded values. The stream drivers are bounded by a
caller-supplied count, because a productively divergent program will otherwise run until something kills it,
and a hung test reports nothing at all, which is worse than a failing one.

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

**Verified, and the verification method itself produced a finding.** All 31 research identifiers were
resolved against the registry and compared to the cited title.
**Thirty-one of thirty-one resolve to the work they are cited as, an error rate of zero.** A title-overlap
heuristic flagged four, and inspecting each individually vindicated all four, for two distinct reasons worth
separating. Three are cases where the registry splits a title from its subtitle, so that the stored title is
"CakeML", "Coroutines" or "Capriccio" while the cited form carries the full descriptive title, and author
and venue confirm each. The fourth is registered with a different agency than the one queried, since
proceedings in the LIPIcs series deposit with DataCite rather than Crossref, so a Crossref lookup returns
nothing for a perfectly valid identifier.

**The apparent 12.9 percent defect rate was therefore entirely instrument error**, and reporting it as a
citation problem would have been a measurement mistake of exactly the kind this series keeps documenting. It
is recorded because the [previous article][related_post_a369] reported a 5.5 percent rate by the same method
and did not separate these two artefacts from genuine mismatches, which means
**that figure is an upper bound rather than an estimate** and the true rate there may be lower.

**Corrected during writing, and left visible.** The plan this article set out to support was to unify the
two conventions, and it survived until it was traced against a three-instruction example.
**The central claim was also stated in a form stronger than the evidence supported**, assuming a one-word
return until the governing application binary interface documents were read, and the correction opened an
option the draft did not contain. An earlier design in this series specified a reordering transformation for
bodies with several suspension points, of which the corpus contains none. A classification that called
nineteen suspensions "the general case" was collapsing two structurally different situations, and the
per-suspension measurement separated them.

**What this article does not establish.** Which of the remaining options is correct, since that turns on an
ABI decision belonging to a workstream this article does not speak for. Whether the widened-return option is
cheaper than two conventions, which is an empirical question and is not measured here. Whether the
source-restructuring option is reasonable. Whether the corpus resembles the population the generator will
serve.

**The literature survey is a narrative review and not a systematic one.** No protocol was registered, no
database was searched exhaustively, and inclusion was by the author's judgement of relevance. Its claim to
completeness is therefore weak, and a reader should treat the assertion that four traditions converge on a
discriminated return as **an observation over the works cited rather than over the field**. The specific
negative claim, that none of the surveyed work addresses per-form selection in a bounded-memory setting, is
the one most exposed to an omission, and it is stated as a gap in the survey rather than a gap in the
literature.

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

**All references below are primary**, meaning language specifications, application binary interface
documents, and the reference documentation of the compiler infrastructure under discussion.
**No secondary literature survey is offered.**
The [previous article in this series][related_post_a369] reports a 5.5
percent error rate on identifiers supplied from memory, and a survey assembled the same way would carry the
same defect without the verification pass that caught it there. The primary documents below are cited
because each states something the argument depends on, and each is verifiable at its published location.

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

- [Compiling with Continuations][research_appel_1992]
- [Pause 'n' Play: Formalizing Asynchronous C#][research_bierman_2012]
- [A survey of compiler testing][research_chen_2020]
- [Design of a separable transition-diagram compiler][research_conway_1963]
- [Abstracting control][research_danvy_filinski_1990]
- [Defunctionalization at work][research_danvy_nielsen_2001]
- [Revisiting coroutines][research_demoura_2009]
- [A monadic framework for delimited continuations][research_dybvig_2007]
- [Kotlin coroutines: design and implementation][research_elizarov_2021]
- [The theory and practice of first-class prompts][research_felleisen_1988]
- [Adding delimited and composable control to a production programming environment][research_flatt_2007]
- [Liberating effects with rows and handlers][research_hillerstrom_2016]
- [CakeML: a verified implementation of ML][research_kumar_2014]
- [Compiler validation via equivalence modulo inputs][research_le_2014]
- [Type directed compilation of row-typed algebraic effects][research_leijen_2017]
- [Formal verification of a realistic compiler][research_leroy_2009_cacm]
- [A formally verified compiler back-end][research_leroy_2009_jar]
- [Coinductive big-step operational semantics][research_leroy_grall_2009]
- [Coroutines: A Programming Methodology, a Language Design and an Implementation][research_marlin_1980]
- [Proof-carrying code][research_necula_1997]
- [Handlers of algebraic effects][research_plotkin_pretnar_2009]
- [Theory and practice of coroutines with snapshots][research_prokopec_2018]
- [Eliminating stack overflow by abstract interpretation][research_regehr_2005]
- [Definitional interpreters for higher-order programming languages][research_reynolds_1972]
- [Translation validation for a verified OS kernel][research_sewell_2013]
- [Retrofitting effect handlers onto OCaml][research_sivaramakrishnan_2021]
- [Continuations: A mathematical semantics for handling full jumps][research_strachey_1974]
- [The F# asynchronous programming model][research_syme_2011]
- [Capriccio: scalable threads for internet services][research_vonbehren_2003]
- [The worst-case execution-time problem: overview of methods and survey of tools][research_wilhelm_2008]
- [Finding and understanding bugs in C compilers][research_yang_2011]

[research_appel_1992]: https://doi.org/10.1017/CBO9780511609619
[research_bierman_2012]: https://doi.org/10.1007/978-3-642-31057-7_12
[research_chen_2020]: https://doi.org/10.1145/3363562
[research_conway_1963]: https://doi.org/10.1145/366663.366704
[research_danvy_filinski_1990]: https://doi.org/10.1145/91556.91622
[research_danvy_nielsen_2001]: https://doi.org/10.1145/773184.773202
[research_demoura_2009]: https://doi.org/10.1145/1462166.1462167
[research_dybvig_2007]: https://doi.org/10.1017/S0956796807006259
[research_elizarov_2021]: https://doi.org/10.1145/3486607.3486751
[research_felleisen_1988]: https://doi.org/10.1145/73560.73576
[research_flatt_2007]: https://doi.org/10.1145/1291151.1291178
[research_hillerstrom_2016]: https://doi.org/10.1145/2976022.2976033
[research_kumar_2014]: https://doi.org/10.1145/2535838.2535841
[research_le_2014]: https://doi.org/10.1145/2594291.2594334
[research_leijen_2017]: https://doi.org/10.1145/3009837.3009872
[research_leroy_2009_cacm]: https://doi.org/10.1145/1538788.1538814
[research_leroy_2009_jar]: https://doi.org/10.1007/s10817-009-9155-4
[research_leroy_grall_2009]: https://doi.org/10.1016/j.ic.2007.12.004
[research_marlin_1980]: https://doi.org/10.1007/3-540-10256-6
[research_necula_1997]: https://doi.org/10.1145/263699.263712
[research_plotkin_pretnar_2009]: https://doi.org/10.1007/978-3-642-00590-9_7
[research_prokopec_2018]: https://doi.org/10.4230/LIPIcs.ECOOP.2018.3
[research_regehr_2005]: https://doi.org/10.1145/1113830.1113833
[research_reynolds_1972]: https://doi.org/10.1023/A:1010027404223
[research_sewell_2013]: https://doi.org/10.1145/2491956.2462183
[research_sivaramakrishnan_2021]: https://doi.org/10.1145/3453483.3454039
[research_strachey_1974]: https://doi.org/10.1023/A:1010026413531
[research_syme_2011]: https://doi.org/10.1007/978-3-642-18378-2_15
[research_vonbehren_2003]: https://doi.org/10.1145/945445.945471
[research_wilhelm_2008]: https://doi.org/10.1145/1347375.1347389
[research_yang_2011]: https://doi.org/10.1145/1993498.1993532
