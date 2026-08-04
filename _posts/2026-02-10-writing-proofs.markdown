---
layout: post
mathjax: true
comments: true
title: "Writing Proofs"
date: 2026-02-10 01:02:22 +0000
categories: math development ai
---

<!-- A79 -->
<script>console.log("A79");</script>

A mathematical proof is a rigorous argument
that establishes the truth of a statement
with a degree of certainty
that no amount of empirical testing can provide.
A test checks finitely many inputs.
A proof covers all of them.
This distinction matters more now than ever.
As AI coding agents generate increasing volumes of code,
the question of how to verify that code is correct
has become an economic and engineering imperative.
The answer, increasingly, involves the same mathematical proofs
that students learn in their first discrete mathematics course.

This article introduces mathematical proofs
from the ground up.
It covers what proofs are,
how they are written,
and why they matter.
It then examines why proofs are specifically important
to software engineers
and why they have taken on new significance
in the age of agentic workflows
where AI systems generate code
that humans must verify.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-02-10 01:02:22 +0000

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

# Claude Code Installation Versions
$ claude --version
2.1.37 (Claude Code)
```

## What Is a Mathematical Proof

A mathematical proof is a finite sequence of statements,
each of which is either an axiom, a definition,
or a logical consequence of preceding statements,
that concludes with the proposition being proved.
In its purest form, a formal proof is written entirely in symbolic language.
Every step follows mechanically from stated rules of inference.
A proof checker can verify such a proof
without understanding what the symbols mean.

In practice, most mathematical writing uses what is called rigorous informal proof.
The argument is expressed in natural language with embedded notation,
and the reader is expected to fill in routine logical steps.
This is the kind of proof found in textbooks, journal articles,
and the vast majority of mathematical literature.
The gap between the formal and the informal
is a source of both flexibility and risk.
Natural language allows ambiguity.
Ambiguity allows errors to pass undetected.

The fundamental property of a proof
is that it compels agreement.
A correct proof leaves no room for doubt
about the truth of its conclusion,
given the truth of its premises.
This is what distinguishes mathematical knowledge
from empirical knowledge.
An empirical observation can be overturned by new evidence.
A valid proof cannot be overturned
without discovering an error in its reasoning
or rejecting one of its axioms.

## How Proofs Are Written

Several standard proof techniques
form the working vocabulary of mathematical reasoning.
Each technique applies to a particular logical structure
in the statement being proved.

### Direct Proof

A direct proof demonstrates that if $P$ is true,
then $Q$ is true,
by starting from the assumption that $P$ holds
and deriving $Q$ through a chain of logical deductions.
This is the simplest and most common proof technique.

**Example.**
Prove that the sum of two even integers is even.

Let $a$ and $b$ be even integers.
By definition, $a = 2m$ and $b = 2n$ for some integers $m$ and $n$.
Then $a + b = 2m + 2n = 2(m + n)$.
Since $m + n$ is an integer, $a + b$ is even. $\square$

### Proof by Contradiction

To prove a statement $P$ by contradiction,
assume that $P$ is false
and derive a logical contradiction.
The contradiction establishes that the assumption must be wrong,
so $P$ must be true.

**Example.**
Prove that $\sqrt{2}$ is irrational.

Assume for contradiction that $\sqrt{2}$ is rational.
Then $\sqrt{2} = \frac{p}{q}$ where $p$ and $q$ are integers with no common factors.
Squaring both sides gives $2 = \frac{p^2}{q^2}$, so $p^2 = 2q^2$.
This means $p^2$ is even, so $p$ is even.
Write $p = 2k$ for some integer $k$.
Then $4k^2 = 2q^2$, so $q^2 = 2k^2$, which means $q$ is also even.
But then $p$ and $q$ share a common factor of 2,
contradicting the assumption that they have no common factors.
Therefore $\sqrt{2}$ is irrational. $\square$

### Proof by Contrapositive

Rather than proving $P \Rightarrow Q$ directly,
one can prove its logically equivalent contrapositive $\neg Q \Rightarrow \neg P$.
The contrapositive approach is often useful
when the direct path from $P$ to $Q$ is unclear
but the path from $\neg Q$ to $\neg P$ is natural.

**Example.**
Prove that if $n^2$ is odd, then $n$ is odd.

Prove the contrapositive.
Assume $n$ is even.
Then $n = 2k$ for some integer $k$,
so $n^2 = 4k^2 = 2(2k^2)$, which is even.
Therefore if $n^2$ is odd, then $n$ is odd. $\square$

### Mathematical Induction

Induction proves that a statement $P(n)$ holds for all natural numbers
$n \geq n_0$
by establishing two components.
The base case verifies $P(n_0)$.
The inductive step assumes $P(k)$ holds for some $k \geq n_0$
and proves that $P(k+1)$ follows.
Together, these establish $P(n)$ for all $n \geq n_0$.

**Example.**
Prove that $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$ for all $n \geq 1$.

**Base case.** When $n = 1$, the left side is 1 and the right side is $\frac{1 \cdot 2}{2} = 1$.

**Inductive step.** Assume $\sum_{i=1}^{k} i = \frac{k(k+1)}{2}$ for some $k \geq 1$.
Then

$$\sum_{i=1}^{k+1} i = \sum_{i=1}^{k} i + (k+1) = \frac{k(k+1)}{2} + (k+1) = \frac{k(k+1) + 2(k+1)}{2} = \frac{(k+1)(k+2)}{2}.$$

This is the formula with $n = k+1$. $\square$

### Constructive Proof

A constructive proof demonstrates that something exists
by exhibiting a specific example or providing a method to construct one.
This contrasts with non-constructive proofs
that establish existence without producing a witness.
Constructive proofs are particularly valued in computer science
because they correspond to algorithms.
A constructive proof that a solution exists
is also a procedure for computing that solution.

## Why Proofs Matter

### Certainty Beyond Testing

The most fundamental reason proofs matter
is that they provide certainty that testing cannot.
A test suite with one million passing test cases
provides strong evidence that a function works correctly.
It does not prove that the function works correctly
for the million-and-first input.
A proof that a function satisfies its specification
covers every possible input simultaneously.

This distinction is not merely philosophical.
The Pentium FDIV bug of 1994
was a division error that occurred
for fewer than one in nine billion random dividend and divisor pairs.
Intel's testing had not found it.
Thomas Nicely, a mathematics professor,
discovered it through number-theoretic computations.
A formal proof of the division algorithm's correctness
would have caught the error before any chip was manufactured.

### Cumulative Knowledge

Mathematics is cumulative.
Each theorem can serve as a building block for subsequent results.
A theorem about prime numbers
can support a theorem about cryptographic protocols,
which can support a proof that a key exchange algorithm is secure.
Without proofs at each level,
the chain of reasoning rests on unverified assumptions.
The formal mathematics library mathlib for the Lean proof assistant
has formalized over 210,000 theorems and 100,000 definitions,
each building on previously verified results.

### Precision of Thought

The discipline of writing proofs
forces precision that informal reasoning does not.
Writing a proof requires identifying every assumption,
making every logical step explicit,
and verifying that no gaps exist in the argument.
This skill transfers directly to engineering practice.
The same mental discipline that catches a missing case
in a proof by induction
catches a missing branch in a conditional expression.

## Why Proofs Matter to Software Engineers

### Program Correctness

Tony Hoare's 1969 paper "An Axiomatic Basis for Computer Programming"
established the formal framework for reasoning about program correctness.
A Hoare triple $\{P\}\ c\ \{Q\}$ asserts that
if a program $c$ begins executing in a state satisfying precondition $P$
and terminates,
then the final state satisfies postcondition $Q$.
This framework built on Robert Floyd's 1967 work on flowchart verification
and remains the foundation of program verification today.

Hoare logic distinguishes partial correctness,
which states that if the program terminates then the result is correct,
from total correctness,
which additionally requires that the program does terminate.
The halting problem proves that total correctness
is strictly harder to establish,
but partial correctness is mechanically verifiable
for many classes of programs.

### Loop Invariants

Loop invariants are the inductive backbone of program verification.
A loop invariant is a predicate that holds before the first iteration
and, if it holds before any given iteration,
continues to hold after that iteration.
This directly mirrors the structure of mathematical induction.
The base case establishes the invariant before the loop begins.
The inductive step shows that each iteration preserves it.
The invariant combined with the loop's termination condition
establishes the desired postcondition.

Consider a simple loop that computes the sum of an array.

```
s = 0
for i in range(n):
    s = s + a[i]
```

The loop invariant is $s = \sum_{j=0}^{i-1} a[j]$.
Before the loop, $i = 0$ and $s = 0 = \sum_{j=0}^{-1} a[j]$ (the empty sum).
After each iteration, $s$ increases by $a[i]$,
maintaining the invariant.
When the loop terminates with $i = n$,
the invariant gives $s = \sum_{j=0}^{n-1} a[j]$,
which is the desired result.

### The Curry-Howard Correspondence

The Curry-Howard correspondence is the deep observation
that proofs and programs are the same thing.
Propositions correspond to types.
Proofs correspond to programs.
Simplifying a proof corresponds to evaluating a program.

Philip Wadler's 2015 paper "Propositions as Types"
provides an authoritative account of this correspondence.
The return type of a function is analogous to a theorem.
The argument types are analogous to hypotheses.
The function body is analogous to a proof
that the hypotheses imply the theorem.

This is not merely an analogy.
In languages with sufficiently expressive type systems,
writing a program that type-checks
is literally constructing a proof
that the type of the program is inhabited.
Dependent type systems like those in Lean, Coq, and Agda
make this correspondence fully explicit.
A Lean program that compiles is a machine-checked proof
of the proposition encoded in its type signature.

### Formal Verification in Practice

Formal verification applies proof to real software systems.
Several tools and success stories illustrate the practical impact.

**TLA+**, developed by Leslie Lamport,
specifies and verifies concurrent and distributed protocols.
Amazon Web Services has used TLA+ since 2011
to verify more than ten core infrastructure components, including S3.
Chris Newcombe and colleagues reported that
"at AWS, formal methods have been a big success.
They have helped us prevent subtle, serious bugs from reaching production,
bugs that we would not have found via any other technique."
One engineer reported that TLA+ would have been
both more reliable and less time consuming
than writing and checking informal proofs for DynamoDB.

**CompCert** is the first practically useful optimizing C compiler
with a complete mechanically checked proof of correctness.
Built using the Coq proof assistant,
CompCert targets ARM, PowerPC, RISC-V, and x86 processors.
Its sixteen compiler passes using ten intermediate languages
all have formally verified semantics preservation.
CompCert received the 2021 ACM Software System Award.

**Lean 4** is both a theorem prover and a programming language.
Its developers received the 2025 ACM SIGPLAN Programming Languages Software Award
for Lean's "significant impact on mathematics, hardware and software verification, and AI."
The mathlib library built on Lean
is the largest unified library of formalized mathematics.

**seL4** is a formally verified microkernel
where a machine-checked proof in Isabelle
guarantees that the implementation correctly refines its specification.
The verification of seL4's 8,700 lines of C code
required 200,000 lines of Isabelle proof.

### Smart Contract Verification

Formal verification has become economically necessary
for high-value smart contracts on blockchain platforms.
When a smart contract manages millions of dollars
and is immutable once deployed,
the cost of a bug is not a patch and a post-mortem.
It is permanent, irrecoverable loss of funds.

Tools for smart contract verification include
Halmos for symbolic execution,
coq-of-solidity for Coq-based verification,
Certora for specification-based checking,
and the K Framework for formal semantics.
Formal verification is considered economically justified
for immutable cross-chain bridges, lending protocols,
and stablecoin reserve management.

## Why Proofs Matter in the Age of Agentic Workflows

### The Verification Problem

AI coding agents generate code
that is plausible but not guaranteed to be correct.
Large Language Models produce output
by predicting the most likely next token,
not by reasoning from verified premises.
The result is code that looks right,
often works on common inputs,
and can fail in ways that are difficult to detect through testing alone.
Hallucination in code generation
is not a bug that will be fixed with better training.
It is an inherent property of statistical prediction.

This creates a verification problem.
If an AI agent generates a thousand lines of code in minutes,
a human reviewer who takes hours to verify that code
has negated the productivity gain.
The economic case for AI-assisted development
depends on finding verification methods
that scale with the rate of code generation.

### Proof Checking as a Verification Strategy

The decisive advantage of formal verification
for AI-generated code
is that proof checking is deterministic.
Writing a proof is hard.
Checking a proof is easy.
An AI agent can generate candidate proofs rapidly,
and a proof checker can accept or reject each candidate
in milliseconds.
Hallucinated proof steps are harmless
because the checker rejects them
and the agent retries.

Martin Kleppmann articulated this insight
in his December 2025 blog post
"Prediction: AI will make formal verification go mainstream."
He observed that the formally verified seL4 microkernel
required twenty person-years and 200,000 lines of Isabelle proof
for 8,700 lines of C code.
That ratio of 23 lines of proof per line of implementation,
at half a person-day per line,
made verification prohibitively expensive for most software.
AI changes this economic equation.
If AI can generate proof scripts
that the checker verifies deterministically,
the cost of verification drops by orders of magnitude.

Kleppmann also identified the remaining bottleneck.
Writing correct formal specifications still requires expertise.
The burden shifts from proof engineering to specification engineering.
Ben Congdon's follow-up post
"The Coming Need for Formal Specification"
developed this observation further,
arguing that as proof generation becomes cheaper,
specification quality becomes the binding constraint.

### AI Systems That Prove Theorems

Recent advances in AI-assisted theorem proving
demonstrate that the generate-and-verify loop works in practice.

**AlphaProof**, published by Google DeepMind in Nature in November 2025,
couples a pre-trained language model
with the AlphaZero reinforcement learning algorithm.
It generates solution candidates
and proves or disproves them
by searching over proof steps in Lean.
At the 2024 International Mathematical Olympiad,
AlphaProof solved three of five non-geometry problems,
including the competition's hardest problem,
achieving silver medal equivalence.
Unlike an LLM generating informal solutions,
every AlphaProof solution is verified by Lean's type checker.
The solutions are guaranteed correct.

By the 2025 IMO, multiple AI systems achieved gold medal performance
with formally verified proofs.
Aristotle, developed by the Harmonic Team,
solved five of six problems
using a combination of Lean proof search,
informal reasoning, and geometry solving.
The pace of advancement from silver in 2024 to gold in 2025
illustrates how rapidly AI-assisted formal reasoning is improving.

### Agentic Frameworks for Verification

Several research frameworks
bridge LLM code generation and formal verification
using agentic architectures.

**Hilbert**, from Apple Research and presented at NeurIPS 2025,
orchestrates four components.
An informal LLM provides mathematical reasoning.
A specialized prover LLM generates Lean 4 tactics.
A formal verifier accepts or rejects each tactic.
A semantic theorem retriever finds relevant lemmas.
Hilbert achieved 94.7% to 99.2% accuracy
on the miniF2F benchmark.

**APOLLO**, also presented at NeurIPS 2025,
is a modular framework
where an LLM generates proofs,
agents analyze and repair proofs using Lean feedback,
automated solvers handle subgoals,
and repaired proofs are recombined and reverified.
APOLLO achieved 84.9% accuracy on miniF2F
among models with fewer than eight billion parameters.

**Safe**, published at ACL 2025,
takes a different approach.
Rather than proving programs correct,
it translates each step of an LLM's chain-of-thought reasoning
into Lean 4 and attempts to formally verify each step.
If a proof fails, the specific reasoning step is identified as flawed.
The authors describe this as
"the first endeavor to utilize formal mathematical language Lean 4
for verifying natural language content generated by LLMs."

These frameworks share a common architecture.
An LLM generates candidate reasoning or code.
A formal verifier accepts or rejects it.
Feedback from the verifier drives iterative refinement.
This generate-verify loop
is the practical application of proof
to the problem of trusting AI-generated output.

### The Specification Bottleneck

The remaining challenge is not proof generation but specification writing.
Current benchmarks like miniF2F and VeriBench
use well-defined mathematical statements
or precisely specified programming tasks.
Real software specifications are often ambiguous, incomplete, or evolving.

VeriBench tested whether LLM-powered agents
can translate Python code into fully proved Lean 4 implementations.
On 113 tasks, direct LLM generation achieved compilation
on only 12.5% of programs.
An agentic self-correcting architecture with iterative Lean feedback
raised success rates to approximately 60%.
These numbers are improving rapidly
but indicate that production-scale verified code generation
remains an active area of research.

Formal verification proves that code matches a specification.
It does not prove that the specification captures the intended behavior.
As AI makes proof generation cheaper,
the quality of specifications becomes the binding constraint on correctness.
The skill that matters most is not writing proofs.
It is writing specifications precise enough to be proved.

## Conclusion

Mathematical proofs are not an abstract academic exercise.
They are the foundation of program correctness,
the mechanism behind type systems and formal verification tools,
and an increasingly practical approach
to verifying the output of AI coding agents.

The core concepts are accessible.
Direct proof, contradiction, contrapositive, and induction
are techniques that any software engineer can learn and apply.
The Curry-Howard correspondence reveals
that programmers who write well-typed programs
are already constructing proofs,
whether they recognize it or not.

The economic equation for formal verification is changing.
Tasks that once required twenty person-years of manual proof engineering
are becoming tractable through AI-assisted proof generation
with deterministic proof checking.
The generate-verify loop,
where an LLM proposes and a proof checker disposes,
may prove to be the most reliable method
for scaling trust in AI-generated code.

The practical recommendation for software engineers
is to learn to think in terms of preconditions, postconditions,
and invariants.
These concepts are the interface
between informal engineering reasoning
and formal mathematical proof.
They are also the specifications
that formal verification tools require.
As the tools improve,
the engineers who can write precise specifications
will have the greatest leverage
over AI-assisted development.

## Future Reading

- [How to Prove It: A Structured Approach][book_velleman]
  by Daniel J. Velleman,
  the standard textbook for learning proof techniques
  with a companion Lean 4 project.

- [Book of Proof][book_hammack]
  by Richard Hammack,
  a freely available introduction to proof techniques
  under a Creative Commons license.

- [Propositions as Types][research_wadler]
  by Philip Wadler,
  an authoritative account of the Curry-Howard correspondence
  and the deep connection between proofs and programs.

- [Prediction: AI Will Make Formal Verification Go Mainstream][blog_kleppmann]
  by Martin Kleppmann,
  arguing that AI changes the economics of formal verification
  from prohibitively expensive to widely accessible.

- [How Amazon Web Services Uses Formal Methods][industry_aws_formal]
  by Chris Newcombe and colleagues,
  documenting AWS's use of TLA+ to verify
  core infrastructure components.

## References

- [Blog, Prediction: AI Will Make Formal Verification Go Mainstream][blog_kleppmann]
- [Blog, The Coming Need for Formal Specification][blog_congdon]
- [Book, Book of Proof][book_hammack]
- [Book, How to Prove It: A Structured Approach][book_velleman]
- [Book, How to Read and Do Proofs][book_solow]
- [Industry, CompCert Verified C Compiler][industry_compcert]
- [Industry, How Amazon Web Services Uses Formal Methods][industry_aws_formal]
- [Research, AI Achieves Silver-Medal Standard at IMO][research_alphaproof_blog]
- [Research, AlphaProof in Nature][research_alphaproof_nature]
- [Research, APOLLO: Automated LLM-Based Framework for Proof Generation][research_apollo]
- [Research, Hilbert: A Lean 4 Agentic Proof Framework][research_hilbert]
- [Research, Propositions as Types][research_wadler]
- [Research, Safe: Step-Aware Formal Verification][research_safe]
- [Research, VeriBench: Benchmarking Verified Code Generation][research_veribench]
- [Tool, Lean Copilot][tool_lean_copilot]

[blog_congdon]: https://benjamincongdon.me/blog/2025/12/12/The-Coming-Need-for-Formal-Specification/
[blog_kleppmann]: https://martin.kleppmann.com/2025/12/08/ai-formal-verification.html
[book_hammack]: https://richardhammack.github.io/BookOfProof/
[book_solow]: https://www.wiley.com/en-us/How+to+Read+and+Do+Proofs:+An+Introduction+to+Mathematical+Thought+Processes,+6th+Edition-p-9781118164020
[book_velleman]: https://www.cambridge.org/us/universitypress/subjects/mathematics/logic-categories-and-sets/how-prove-it-structured-approach-3rd-edition
[industry_aws_formal]: https://cacm.acm.org/research/how-amazon-web-services-uses-formal-methods/
[industry_compcert]: https://compcert.org/
[research_alphaproof_blog]: https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/
[research_alphaproof_nature]: https://www.nature.com/articles/s41586-025-09833-y
[research_apollo]: https://arxiv.org/abs/2505.05758
[research_hilbert]: https://machinelearning.apple.com/research/hilbert
[research_safe]: https://arxiv.org/abs/2506.04592
[research_veribench]: https://openreview.net/forum?id=rWkGFmnSNl
[research_wadler]: https://homepages.inf.ed.ac.uk/wadler/papers/propositions-as-types/propositions-as-types.pdf
[tool_lean_copilot]: https://github.com/lean-dojo/LeanCopilot
