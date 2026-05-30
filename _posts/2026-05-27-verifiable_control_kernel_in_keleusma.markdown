---
layout: post
mathjax: false
comments: true
title: "A Verifiable Control Kernel in Keleusma for a Truthful-Machine Architecture"
date:   2026-05-27 09:00:00 +0000
categories: ai rust programming
---

<!-- A109 -->
<script>console.log("A109");</script>

A companion article argued that an assistant
that adheres to the scientific method,
values truthfulness over agreement,
and declines when declining is honest
cannot be a single large language model,
and must instead be a compound system
in which the model proposes
and a deterministic, auditable layer
holds the guarantees the model cannot.
That argument is developed in
[the truthful-machine blueprint][related_post_truthful_machine].
This article takes the one layer of that design
that can be written as ordinary, verifiable code,
namely the control-and-governance kernel,
and implements its skeleton in
[Keleusma][kel_github],
a total functional language
whose verifier proves bounded execution
before a program ever runs.
The Keleusma language itself is introduced in
[an earlier getting-started article][related_post_keleusma].

A statement of scope is necessary first,
because the subject of the blueprint
is a machine that does not overclaim.
The examples below implement only the kernel.
The proposer, the critic ensemble,
the retrieval store, the calibration head,
and the formal verifier of the blueprint
are not written here and cannot be written in Keleusma.
They are large or nondeterministic components
that live in the host program,
and they appear in this article only as
host-supplied inputs and external natives.
Nothing here demonstrates a working truthful machine.
What it demonstrates is that the kernel
that would orchestrate and constrain such a machine
can be expressed in a form
that is proved bounded and total before it runs.
That, and only that, is the claim.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-05-27 09:00:00 +0000

# OS and Version
$ uname -vm
Darwin Kernel Version 25.5.0: Mon Apr 27 20:38:56 PDT 2026; root:xnu-12377.121.6~2/RELEASE_ARM64_T6000 arm64

# Keleusma
$ keleusma --version
keleusma 0.2.1
```

The call-yield-resume driver used in the final section
arrived in the 0.2.1 release. Everything else in this article
also runs unchanged on 0.2.0.

## Why This Layer Fits Keleusma

The blueprint's central principle is that rigidity
must live in deterministic machinery
outside the stochastic model.
Keleusma is built on the same separation.
A Keleusma program is the score,
and the larger host program is the orchestra.
The score does a small, bounded amount of work,
hands control back, and waits.
The properties Keleusma proves before a program runs,
[totality and bounded worst-case execution time
and memory][kel_guide],
are exactly the properties a control kernel needs
if its behavior is to be audited
rather than trusted.
The verifier rejects by default
anything it cannot prove bounded,
which is the same default-deny posture
the governance layer of the blueprint requires.

The sections that follow build the kernel
one piece at a time.
Each listing was compiled and run
with the version shown above,
and the output shown is the actual output produced.

## Typed Claims with a Refinement

The blueprint requires every claim
to carry a confidence value that has a meaning.
A bare integer cannot enforce the range
a confidence must inhabit.
A [refinement type][ref_refinement_type]
can, and the check is proved at construction.

```keleusma
fn in_range(x: Word) -> bool { x >= 0 and x <= 100 }

newtype Confidence = Word where in_range;

fn raw(c: Confidence) -> Word {
    c as Word
}

fn main() -> Word {
    let c = Confidence(64);
    raw(c)
}
```

Running it produces the value.

```sh
$ keleusma run 01_typed_claims.kel
64
```

The value of the refinement is what it refuses.
A confidence outside the range
is not a runtime error to be caught.
It is rejected before the program runs.

```keleusma
fn main() -> Word {
    raw(Confidence(150))
}
```

```sh
$ keleusma run 01b_typed_claims_reject.kel
error: compile: 5:9: refinement check `in_range` provably fails for newtype `Confidence` at compile time on argument 150
```

The rejection is the feature.
A claim whose confidence is meaningless
cannot be constructed.

## Terminal-State Routing

The blueprint insists that the controller
has no terminal state that means
"produce a best guess anyway."
Given a critic verdict and a calibrated confidence,
the controller routes to exactly one
of four terminal states.
The critic is not written here.
Its verdict is an input,
supplied by the host.

```keleusma
fn in_range(x: Word) -> bool { x >= 0 and x <= 100 }
newtype Confidence = Word where in_range;

enum Verdict {
    Refuted,
    Unsupported,
    IllPosed,
    Supported,
}

fn answer_or_hedge(c: Confidence) -> Word {
    let n = c as Word;
    if n >= 80 { 0 } else { 1 }
}

fn decide(v: Verdict, c: Confidence) -> Word {
    match v {
        Verdict::Refuted => 2,
        Verdict::Unsupported => 2,
        Verdict::IllPosed => 3,
        Verdict::Supported => answer_or_hedge(c),
    }
}

fn main() -> Word {
    decide(Verdict::Supported, Confidence(64))
}
```

The decision codes are 0 for answer,
1 for answer with stated uncertainty,
2 for abstain, and 3 for request reframing.
A supported claim at a confidence of 64
falls below the threshold of 80,
so the controller answers with stated uncertainty.

```sh
$ keleusma run 02_route.kel
1
```

A refuted or unsupported claim routes to abstention.
An ill-posed question routes to a request for reframing.
The match is total,
so every verdict has a defined terminal state,
and the verifier confirms it.

## The Fact Gate

The governance layer must guarantee
that an ungrounded claim cannot reach the output
without passing an audited gate.
Keleusma expresses this with an
[information-flow label][kel_guide].
A label rides on a value,
and the language refuses to let a labelled value
flow into a place that does not accept the label.

```keleusma
fn commit(x: Word) -> Word {
    x
}

fn main() -> Word {
    let claim = classify 42@Unverified;
    commit(declassify claim@Unverified)
}
```

The output boundary `commit` accepts only a plain `Word`.
The proposer's claim arrives labelled `Unverified`.
The single line `declassify claim@Unverified`
is the one visible, greppable place
where a verified claim is released.

```sh
$ keleusma run 03_fact_gate.kel
42
```

Remove the gate, and the leak is proved
before the program runs.

```keleusma
fn main() -> Word {
    let claim = classify 42@Unverified;
    commit(claim)
}
```

```sh
$ keleusma run 03b_fact_gate_leak.kel
error: compile: 17:12: type error: argument to `commit` expects Word, got Word@Unverified
```

A reviewer auditing the kernel
finds every release of an unverified claim
by searching for the word `declassify`.
There is no other way out.

## The Call-Yield-Resume Lifecycle

The controller does not run to completion in one piece.
It pauses to let the host run the proposer and the critic,
then resumes with their result and decides.
That is a non-atomic total function,
written with the `yield` keyword.

```keleusma
fn decide_code(0)        -> Word { 2 }  // refuted     -> abstain
fn decide_code(1)        -> Word { 2 }  // unsupported -> abstain
fn decide_code(2)        -> Word { 3 }  // ill-posed   -> request reframing
fn decide_code(n: Word)  -> Word { 0 }  // supported   -> answer

yield main(tick: Word) -> Word {
    let verdict = yield 1;
    decide_code(verdict)
}
```

The runner drives this lifecycle
through a tick-counter convention
that arrived in the 0.2.1 release.
It calls the entry with tick 1.
The script yields a Word,
the host computes the next tick
as the yielded value plus one,
and resumes the script with that value.
A `yield` entry point ends
when control returns from the function,
and the runner prints the final value.
Here the script yields 1,
the host resumes with 2,
and the controller routes verdict code 2,
an ill-posed question,
to terminal state 3, request reframing.

```sh
$ keleusma run 04_controller_tick.kel
Int(3)
```

In a real host the resume value
is the critic's verdict rather than a tick counter,
and the embedding host drives the same lifecycle
through its [runtime interface][kel_github].

The long-running form is a productive divergent function
that yields a decision on every cycle and never finishes,
the steady beat of a governed agent
that runs indefinitely.

```keleusma
fn decide_code(0)       -> Word { 2 }
fn decide_code(1)       -> Word { 2 }
fn decide_code(2)       -> Word { 3 }
fn decide_code(n: Word) -> Word { 0 }

loop main(verdict: Word) -> Word {
    let decision = decide_code(verdict);
    let _next = yield decision;
    decision
}
```

The runner drives this form continuously,
rate-limited by the `--tick-interval` flag,
and it stops only when the script calls `shell::exit`
or the operator interrupts it.
The stock runner does not print the per-cycle decisions,
so a host that consumes them is needed for visible output,
but the verifier still proves the loop
productive and bounded per cycle before it runs.

On the 0.2.0 release the resume driver is absent.
There the `yield` and `loop` entry points
still lex, type-check, and pass the verifier,
which `keleusma compile` confirms by writing the bytecode,
but the stock 0.2.0 runner cannot drive them to completion.

## What This Does and Does Not Show

The honest accounting matters
more in this subject than in most.

What the kernel shows is that the deterministic spine
of the blueprint can be written
in a language that proves termination
and bounded resources before execution,
that typed claims and their confidence ranges
can be enforced at construction,
that the controller's terminal states are total
with no fall-through to a guess,
and that an unverified claim cannot reach the output
except through a single audited release point.
Keleusma version 0.2.0 also adds
[cryptographic module signing][kel_github],
so the kernel itself can be delivered
as a tamper-evident, origin-authentic artifact,
which is the property the blueprint wants
for any policy or controller module
distributed to a node.

What the kernel does not show is a truthful machine.
The proposer, the critics, the retrieval grounding,
the calibrator, and the formal prover
are absent by necessity.
They are tensor-compute and nondeterministic search,
and Keleusma deliberately keeps that work
on the far side of its external-native boundary.
The information-flow guarantee, moreover,
is a compile-time property of the score,
not of the orchestra.
It disciplines what the kernel expresses,
not what the host does once a value is released.
The refinement checker is conservative as well.
It proves decidable predicates,
not the rich semantic policies
a full verifier would need.

These limits are not failures of the demonstration.
They are the boundary the blueprint itself draws,
made concrete.
The kernel is the part that can be made rigid and auditable,
and it is exactly the part shown here.
The rest remains, correctly, outside it.

## Conclusion

The truthful-machine blueprint is a hypothesis,
and this article does not change that.
What it establishes is narrower and verifiable.
The control-and-governance kernel of that design
is expressible today in a language
that proves the kernel total and bounded
before it runs,
that enforces typed claims and an audited fact gate
at compile time,
and that can ship the kernel as a signed artifact.
The neural and symbolic-prover components
remain unbuilt and, in Keleusma, unbuildable,
which is precisely where the blueprint
says they should live.
A small, exact, trustworthy core
inside a large and untrusted host
is the shape of the kernel
and the shape of the language alike.

## References

- [Keleusma, Crate on crates.io][kel_crate]
- [Keleusma, GitHub Repository][kel_github]
- [Keleusma, Language Guide][kel_guide]
- [Reference, EdDSA and Ed25519][ref_eddsa]
- [Reference, Refinement Type][ref_refinement_type]
- [Reference, Total Functional Programming][ref_total_functional]
- [Reference, Worst-Case Execution Time][ref_wcet]
- [Related Post, A Speculative Neurosymbolic Blueprint for Truthful Machines][related_post_truthful_machine]
- [Related Post, Getting Started with Keleusma 0.1.1][related_post_keleusma]

[kel_crate]: https://crates.io/crates/keleusma
[kel_github]: https://github.com/sgeos/keleusma
[kel_guide]: https://github.com/sgeos/keleusma/tree/master/docs/guide
[ref_eddsa]: https://en.wikipedia.org/wiki/EdDSA
[ref_refinement_type]: https://en.wikipedia.org/wiki/Refinement_type
[ref_total_functional]: https://en.wikipedia.org/wiki/Total_functional_programming
[ref_wcet]: https://en.wikipedia.org/wiki/Worst-case_execution_time
[related_post_truthful_machine]: {% post_url 2026-05-26-neurosymbolic_blueprint_for_truthful_machines %}
[related_post_keleusma]: {% post_url 2026-03-14-keleusma_getting_started %}
