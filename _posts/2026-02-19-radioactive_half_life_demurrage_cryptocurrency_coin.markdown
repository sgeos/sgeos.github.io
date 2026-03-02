---
layout: post
mathjax: true
comments: true
title: "Radioactive Half-Life Demurrage Cryptocurrency Coin"
date: 2026-02-19 01:22:17 +0000
categories: crypto economics math
---

<!-- A88 -->
<script>console.log("A88");</script>

Fixed-supply cryptocurrencies face a structural problem.
As block rewards decline over time,
the security budget that pays miners to protect the network
shrinks with each halving event.
If transaction fees do not grow fast enough to compensate,
the network eventually cannot afford the hash power
required to resist attack.
Bitcoin's halving schedule will reduce the block subsidy to zero
by approximately 2140,
and the transition to fee-only security
remains an open question in cryptocurrency economics.

Demurrage currencies offer an alternative design.
Instead of a subsidy that decays to zero,
a demurrage fee continuously recycles value from holders to miners.
The idea is not new.
Silvio Gesell proposed stamp scrip in the 1910s,
and Irving Fisher championed the concept
during the Great Depression.
Modern implementations include Freicoin and the Chiemgauer.

This article explores a demurrage-based protocol design
that combines three ideas from different domains.
From monetary economics, it borrows demurrage
in the form of a fixed 100-year half-life on all holdings.
From blockchain research, it borrows proof of useful work
to replace hash grinding with verifiable computation.
From nuclear physics, it borrows the mathematics of exponential decay
to create a predictable, immutable security subsidy
that never reaches zero.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-02-19 01:22:17 +0000

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
2.1.42 (Claude Code)
```

## The Security Budget Problem

A blockchain's security budget is the total compensation
paid to miners per unit time.
In Bitcoin, this budget consists of two components.
The block subsidy creates new coins with each block.
Transaction fees are paid by users
who want their transactions included.
The block subsidy currently dominates miner revenue,
accounting for approximately 85% of total compensation
as of the 2024 halving.

Bitcoin's halving schedule reduces the block subsidy
by half every 210,000 blocks,
or approximately every four years.
The original reward of 50 BTC per block
has fallen to 3.125 BTC per block after four halvings.
By design, the subsidy converges to zero.
The network's total supply approaches a hard cap
of 21 million BTC
and will reach it around the year 2140.

The optimistic case assumes that transaction fees will grow
to replace the declining subsidy.
Limited block space and growing adoption
would drive fees upward through competition.
The concerned case observes that transaction fees
have not historically grown
in proportion to subsidy declines.
If miners cannot cover operational costs,
hash rate will fall,
and the network becomes more vulnerable
to double-spend attacks, transaction censorship,
and chain reorganizations.

The security budget problem is not unique to Bitcoin.
Any fixed-supply cryptocurrency
that relies on a diminishing issuance schedule
faces the same structural tension.
The question is whether a protocol can sustain
a sufficient security subsidy
without introducing permanent inflation.

## Demurrage as a Design Primitive

Demurrage is a holding fee applied to money.
The concept was developed
by the German-Argentine economist Silvio Gesell
in the early twentieth century.
Gesell observed that money serves two functions
that are in tension with each other.
As a medium of exchange, money should circulate freely.
As a store of value, money incentivizes hoarding.
Gesell proposed stamp scrip to resolve this tension.
Currency holders would need to purchase and affix stamps
at regular intervals to keep their notes valid.
The cost of the stamps acted as a negative interest rate
that penalized holding and encouraged spending.

Irving Fisher advocated for stamp scrip
during the Great Depression in his 1933 book of the same name.
John Maynard Keynes devoted five pages to Gesell's work
in "The General Theory of Employment, Interest and Money,"
writing that "the idea behind stamped money is sound."
Several experiments with stamp scrip occurred
in the Austrian town of Wörgl
and in scattered American communities,
though none lasted more than a few months.

Modern demurrage currencies
have implemented Gesell's idea digitally.
Freicoin, launched in December 2012,
is a Bitcoin-derived cryptocurrency
that enforces a continuously assessed demurrage fee
of 4.4% per year on all account holders.
The Chiemgauer, a regional currency in Bavaria launched in 2003,
applies a 6% annual demurrage rate
that incentivizes spending within the local economy.

For cryptocurrency protocol design,
demurrage has a specific structural advantage.
A demurrage fee creates a perpetual revenue stream
that can be directed to miners as a security subsidy.
Unlike a block reward that halves to zero,
a demurrage subsidy
is proportional to the total value held on the network.
As long as coins exist, the subsidy exists.

## Half-Life Decay Mathematics

The protocol proposed in this article
applies demurrage using the mathematics of radioactive decay.
Each coin on the network decays exponentially
with a fixed half-life of 100 years.

The standard exponential decay equation is

$$N(t) = N_0 \cdot e^{-\lambda t}$$

where $N(t)$ is the quantity remaining at time $t$,
$N_0$ is the initial quantity,
and $\lambda$ is the decay constant.

The decay constant is related to the half-life $t_{1/2}$ by

$$\lambda = \frac{\ln 2}{t_{1/2}}$$

For a 100-year half-life,
the decay constant is approximately $0.00693$ per year.
This yields an annual decay rate of approximately 0.69%.
Converted to a daily rate,
the decay constant is approximately $0.0000190$ per day,
which produces a daily loss
of approximately 0.0019% of holdings.

The fraction of holdings remaining after $t$ years is

$$\frac{N(t)}{N_0} = \left(\frac{1}{2}\right)^{t/100}$$

After 100 years, exactly half of any holding remains.
After 200 years, one quarter remains.
The total supply is never destroyed.
Decayed coins are collected
and redistributed to miners as rewards.
The protocol is a closed recycling economy
in which total supply $S$ is conserved at all times.

The choice of a 100-year half-life is deliberate.
The annual decay rate of 0.69%
is comparable in kind to Freicoin's 4.4%
but substantially lower in magnitude,
placing a lighter burden on holders.
The rate is high enough
to generate a meaningful security subsidy
but low enough that individual holders
lose less than 1% per year.

## Hierarchical Reaping

The protocol does not collect the decay fee
as a continuous fractional reduction of every balance.
Instead, it uses a hierarchical reaping system
that processes wallets in a strict priority order.
This design is a consequence of whole-coin quantization,
which is discussed in the next section.

### Tier 1. The Fractional Purge

The protocol first targets wallets
with balances less than 1.0 coin.
It sorts these wallets from lowest balance to highest
and zeros them out one by one
until the decay quota for the current period is met.
These fractional balances are collected
and added to the miner reward pool.

If the aggregate value of fractional-balance wallets
is sufficient to satisfy the entire decay quota,
no coins are taken from wallets holding 1.0 or more.
The smallest holders absorb
the full cost of the security subsidy.
This creates a sharp incentive
to consolidate holdings above 1.0 coin.

This consolidation incentive is a deliberate design goal.
The protocol targets institutional and long-term holders
who find a sub-1% annual decay rate acceptable.
Fractional-balance sweeping removes dust from the ledger,
keeping the active wallet set clean
and the reaping process efficient.
Participants are expected to maintain balances
of at least 1.0 coin at all times.

### Tier 2. The Mid-Tier Lottery

Wallets holding between 1.0 and approximately 143 coins
cannot pay a fractional decay fee
because the protocol only operates in whole-coin units.
A 10-coin holder owes approximately 0.07 coins per year in decay,
but the protocol cannot subtract 0.07 from a balance.
Instead, these holders enter a stochastic lottery.
The 10-coin holder
has approximately a 7% annual probability
of losing exactly 1 whole coin
and a 93% probability of losing nothing in a given year.

The expected value of the lottery
matches the continuous decay rate
over large populations and long time horizons.
For any individual holder,
the outcome in any given year is binary.
This is analogous to how radioactive decay
is deterministic for large samples
but stochastic for individual atoms.

### Tier 3. The Institutional Smooth Tax

For holders with large balances,
the law of large numbers
smooths out the stochastic variation.
A holder of 1,000 coins
expects to lose approximately 7 coins per year.
The variance around this expectation
is small relative to the total holding.
For institutional-scale holders,
the decay operates as a predictable management fee
of approximately 0.69% per year.

## Whole-Coin Quantization

All rewards, stakes, and forfeitures in this protocol
are denominated in whole coins.
A miner who wins the lottery receives exactly 1.0 coin.
A miner who stakes collateral deposits exactly 1.0 coin.
A party who loses a dispute forfeits exactly 1.0 coin.

This design choice
eliminates fractional-value accounting
in the incentive layer.
It simplifies the protocol's game-theoretic analysis
because every outcome
is an integer multiple of the base unit.
The 1.0-coin threshold also creates a natural boundary
in the hierarchical reaping system.
Balances below 1.0 are subject to deterministic sweeping.
Balances at or above 1.0 are subject to stochastic decay.

The protocol supports fractional transfers
and micro-transactions at the ledger level.
However, any transaction
that reduces a balance below 1.0
exposes the remaining fraction to deterministic reaping.
Wallet software should alert users
when a transaction would push their balance
below this threshold.

## Proof of Useful Work

Most proof-of-work blockchains
require miners to perform computations
that serve no purpose
beyond demonstrating energy expenditure.
Bitcoin miners compute SHA-256 hashes repeatedly,
searching for an output below a difficulty target.
The computation secures the network
but produces no useful byproduct.

Proof of useful work replaces hash grinding
with computations that produce value beyond consensus.
The concept has both theoretical and practical precedent.
Ball, Rosen, and Sabin demonstrated in their 2017 paper
that useful proof of work can be constructed
for an expandable class of practical problems
while maintaining the security properties
of traditional proof of work.
Primecoin, launched in 2013,
searches for Cunningham chains of prime numbers
as its proof of work.
Gridcoin rewards contributors
to BOINC scientific computing projects.

### RISC-V as an Execution Platform

This protocol specifies
the RISC-V instruction set architecture
as the execution platform for useful work.
RISC-V is a free and open Instruction Set Architecture (ISA)
developed at UC Berkeley beginning in 2010.
Its modular design, minimal base instruction set,
and royalty-free licensing
make it suitable for deterministic, verifiable computation.

The choice of RISC-V over a custom virtual machine
provides two distinct advantages.
Miners can execute tasks on physical RISC-V hardware,
leveraging the growing ecosystem of RISC-V processors
for energy-efficient computation.
Smart contract developers can compile deterministic programs
using standard toolchains such as LLVM and GCC,
removing the need to learn a specialized assembly language
or a domain-specific instruction set.

The open specification
enables formal verification of processor implementations,
and the RISC-V Formal Interface provides
a dedicated framework
for proving correctness properties.

### Task Binding and Verification

The protocol assigns deterministic smart contracts
to $R$ independent miners for resolution.
Each miner receives the smart contract to execute
along with a unique salt value.
After executing the smart contract,
the miner hashes the return value
using a standard hash function.
The resulting hash and the miner's salt
are then used as input
to a trivial proof of work exercise.
The miner is responsible for returning
both the smart contract result
and the solution to the proof of work exercise.

This two-phase structure serves two purposes.
The smart contract execution provides the useful computation.
The proof of work exercise,
parameterized by the result hash and a miner-specific salt,
binds the computation to the miner's identity.
An attacker who wishes to claim credit for $n$ identities
must execute the smart contract $n$ times
and solve $n$ independent proof of work challenges,
rendering the attack economically equivalent
to honest participation.

The protocol requires unanimous agreement
among the $R$ miners on the smart contract result
and final approval from the task issuer.
This selectable redundancy allows issuers
to trade cost for confidence
depending on the criticality of the computation.

## The Economic Loop

The protocol creates a closed economic loop
with four participants and a conserved total supply.

1. Holders pay network rent through decay.
   Their coins are collected
   by the hierarchical reaping process.
2. Decayed coins enter the general reward pool.
3. Miners execute assigned RISC-V smart contracts.
   They earn work credits
   proportional to verified CPU cycles.
4. The reward pool distributes whole-coin prizes
   via a pro rata lottery weighted by work credits.

Because the total supply is fixed
and decayed coins are redistributed rather than destroyed,
the system is a zero-sum recycling economy.
The decay mechanism guarantees a baseline security subsidy
regardless of network transaction volume.
Task issuers may optionally pay fees
to prioritize or fund specific computations,
but the baseline subsidy requires no fee revenue.
No new coins are ever created after the initial distribution.

This loop is self-balancing.
If the coin's value increases,
the decay subsidy in real terms also increases,
attracting more miners and more computation capacity.
If the coin's value decreases,
the subsidy decreases,
and miners with higher costs exit,
leaving the network at a smaller but sustainable scale.

## Staking and Dispute Resolution

### Good Faith Stakes

Participation in the computing network
requires a good faith stake of 1.0 coin.
Both miners and task issuers must post this collateral.
The stake serves as an anti-spam mechanism
and as a bond against misbehavior.

If a miner provides an incorrect result
for a deterministic computation,
their 1.0-coin stake is forfeited
to the fractional decay pool,
accelerating the dust sweep for the rest of the network.
If a task issuer acts in bad faith,
their 1.0-coin stake is forfeited
to a private dispute resolution lottery.

### Verification Licensing

The protocol periodically issues
verification license tasks to randomly selected miners.
These tasks are designed
to test the miner's computational integrity
and the correctness of their execution environment.
Miners who pass the verification task
are elevated to licensed verifier status
for the duration of their license.
Licensed verifiers are eligible to adjudicate disputes
and participate in the private dispute lottery.

Miners who fail a verification task
forfeit their 1.0-coin participation stake
and are removed from the mining pool.
A removed miner must stake another 1.0 coin
to be readmitted to the pool.
Honest mining pool operators
are expected to re-evaluate the reliability
of miners who have been removed,
as repeated failures may indicate
faulty hardware, software misconfiguration,
or intentional misbehavior.

### Dispute Resolution

When a dispute arises over computation results,
licensed verifiers adjudicate the outcome.
The forfeited stake of the losing party
is distributed via a private lottery
among the verifiers who participated in the resolution.

Entry into the private dispute lottery
voids a verifier's work credits
for the general lottery in that cycle.
This creates a trade-off.
Verifiers are motivated to resolve disputes
because the private lottery
offers higher win probability than the general pool,
but they sacrifice
their accumulated work credits to participate.

## Protocol Specification

The following is a condensed specification of the protocol.

**Supply.** Fixed and conserved. Total supply $S$ is constant.

**Decay.** 100-year half-life, approximately 0.69% annually.
Reaping priority targets wallets with less than 1.0 coin first,
sorted from smallest to largest balance.
Spillover applies stochastic pro rata decay
to wallets with 1.0 or more coins,
removing exactly 1.0 coin per lottery loss.

**Computation.** Deterministic RISC-V smart contracts
assigned to $R$ miners with unique salt values.
Miners return smart contract results
and solutions to salt-parameterized proof of work exercises.
Miners must stake 1.0 coin as a good faith deposit.
Task issuers must stake at least 1.0 coin.

**Verification Licensing.** Periodic license tasks
issued to randomly selected miners.
Pass elevates to licensed verifier status.
Fail forfeits 1.0-coin stake and removes miner from pool.

**Dispute Resolution.** Licensed verifiers resolve disputes.
Malicious issuers forfeit 1.0 coin
to a private verifier lottery.
Inaccurate miners forfeit 1.0 coin
to the fractional decay pool.

**Reward Distribution.** Decayed coins fund the general lottery.
Winning the lottery awards exactly 1.0 coin.
Lottery probability is proportional to verified CPU cycles.

## Design Tradeoffs and Open Questions

Task selection in the proof of useful work system
requires governance.
Who decides which computations
are submitted to the network?
An open marketplace allows any issuer to post tasks,
but could result in trivial or adversarial workloads.
A curated model introduces centralization.
The governance of task selection
is an open design question.

The 100-year half-life is a parameter choice
that trades decay speed for holder burden.
A shorter half-life generates a larger security subsidy
but imposes a steeper cost on holders.
A longer half-life reduces cost to holders
but may produce an insufficient subsidy
if the network is small.
The optimal half-life
depends on the network's target security level
and expected adoption trajectory.

The exact stake amounts are tunable.
The current design specifies 1.0 coin
for all stakes and forfeitures.
Because miners participate in a pro rata lottery,
their expected value for any given cycle
is less than 1.0 coin.
Increasing the stake amount
would raise the barrier to entry
while strengthening the bond against misbehavior.
The optimal stake level
depends on the trade-off between accessibility
and the desired deterrent effect.

## Summary

This article presents a thought experiment
in cryptocurrency protocol design
that addresses the security budget problem
through three mechanisms.

Exponential decay with a 100-year half-life
creates a perpetual security subsidy
that never reaches zero.
Hierarchical reaping distributes the decay cost
across three tiers of holders
based on balance size and stochastic fairness.
Proof of useful work on the RISC-V instruction set
replaces energy-wasting hash grinding
with verifiable computation.

The protocol conserves total supply,
recycling decayed coins as miner rewards
in a closed economic loop.
The whole-coin quantization of rewards, stakes, and penalties
simplifies the game-theoretic analysis
and creates a sharp boundary
at the 1.0-coin threshold.

Demurrage is an old idea with a long history.
Gesell proposed it over a century ago,
and modern implementations such as Freicoin
have demonstrated
that the concept translates to digital currency.
The contribution of this design
is the combination of demurrage
with useful work and hierarchical reaping
into a protocol that sustains security
without inflation, deflation,
or dependence on transaction volume.

## Future Reading

The security budget problem is discussed in detail
in the cryptocurrency economics literature,
particularly in analyses of Bitcoin's long-term viability
after block subsidies approach zero.

The theory of demurrage currencies
connects to broader questions in monetary economics
about the velocity of money
and the relationship between store-of-value properties
and medium-of-exchange properties.
Gesell's original work and Fisher's advocacy
provide historical context for the idea.

Proof of useful work
is an active area of research
at the intersection of cryptography
and distributed computing.
The Ball, Rosen, and Sabin framework
provides theoretical foundations,
while projects like Primecoin and Gridcoin
offer practical case studies.

RISC-V formal verification
is relevant to any protocol
that requires deterministic and provably correct computation.
The RISC-V Formal Interface
and associated verification tools
provide the infrastructure needed
to prove properties of RISC-V implementations.
RISC Zero demonstrates a production implementation
of deterministic RISC-V execution
for verifiable computation using zero-knowledge proofs.

## References

- [Book, The General Theory of Employment, Interest and Money][book_general_theory]
- [Book, Stamp Scrip][book_stamp_scrip]
- [Reference, Chiemgauer][ref_chiemgauer]
- [Reference, Demurrage (Currency)][ref_demurrage]
- [Reference, Economics of Bitcoin Halving][ref_economics_halving]
- [Reference, Exponential Decay][ref_exponential_decay]
- [Reference, Freicoin][ref_freicoin]
- [Reference, Gridcoin][ref_gridcoin]
- [Reference, Primecoin][ref_primecoin]
- [Reference, RISC-V][ref_riscv]
- [Reference, RISC Zero][ref_risc_zero]
- [Reference, Silvio Gesell][ref_silvio_gesell]
- [Research, Bitcoin: A Peer-to-Peer Electronic Cash System][research_bitcoin]
- [Research, Proofs of Useful Work][research_pouw]

[book_general_theory]: https://en.wikipedia.org/wiki/The_General_Theory_of_Employment,_Interest_and_Money
[book_stamp_scrip]: https://en.wikipedia.org/wiki/Stamp_scrip
[ref_chiemgauer]: https://en.wikipedia.org/wiki/Chiemgauer
[ref_demurrage]: https://en.wikipedia.org/wiki/Demurrage_(currency)
[ref_economics_halving]: https://www.fidelitydigitalassets.com/research-and-insights/economics-bitcoin-halvinga-miners-perspective
[ref_exponential_decay]: https://en.wikipedia.org/wiki/Exponential_decay
[ref_freicoin]: https://en.bitcoin.it/wiki/Freicoin
[ref_gridcoin]: https://en.wikipedia.org/wiki/Gridcoin
[ref_primecoin]: https://en.wikipedia.org/wiki/Primecoin
[ref_risc_zero]: https://risczero.com/
[ref_riscv]: https://en.wikipedia.org/wiki/RISC-V
[ref_silvio_gesell]: https://en.wikipedia.org/wiki/Silvio_Gesell
[research_bitcoin]: https://bitcoin.org/bitcoin.pdf
[research_pouw]: https://eprint.iacr.org/2017/203.pdf
