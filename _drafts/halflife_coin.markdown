---
layout: post
mathjax: false
comments: true
title:  "Crypto With a Half Life"
date:   2026-01-01 00:00:00 +0000
categories: [tokenomics, game-theory, deflation, blockchain, incentive-design] 
---
In the search for a sustainable "Store of Value," most protocols fail at the extremes. They either inflate into worthlessness or deflate into a liquidity trap where the last holder is left with a bag that no one can mine.

Today we explore an alternative: **The Hierarchical Decay Model.**

### The Core Engine: Fixed Half-Life
Unlike traditional "burn" tokens that rely on transaction volume, this protocol operates on a **Fixed 100-Year Half-Life**. This creates an immutable, predictable "Network Debt" that must be paid to the miners every hour to maintain security.

* **Annual Decay Rate:** ~0.69%
* **Daily Decay Rate:** ~0.0019%
* **Target:** Miners and Validators (Perpetual Security Subsidy)

### The Hierarchy of Reaping
The protocol does not tax all wallets equally. It follows a strict "Cleanup" prioritization that protects large-scale capital by sacrificing the "dust" at the bottom of the ledger.

#### Tier 1: The Fractional Purge (The Shield)
The protocol first targets wallets with **less than 1.0 coin**. It sorts these from **lowest balance to highest** and zeros them out one by one until the decay quota is met.
> **The Result:** If retail "plankton" hold enough collective value to satisfy the 0.69% annual debt, the whales lose nothing. The smallest holders act as a physical shield for the largest.

#### Tier 2: The Mid-Tier Roulette
If you hold between **1 and 143 coins**, the math breaks. Since the protocol only evaporates whole coins, you cannot pay 0.7%. Instead, you enter a probabilistic lottery.
* **The Probability:** A 10-coin holder has a ~7% annual chance of losing 1 whole coin (10% of their wealth) and a 93% chance of losing nothing.

#### Tier 3: The Institutional Whale
For holders with **>1,000 coins**, the decay becomes a "Smooth Tax." The law of large numbers averages out the whole-coin increments into a predictable 0.7% annual management fee.

---

### The Perpetual Security Loop
This isn't a "burn-to-zero" model. The "decayed" coins are harvested and **reminted as miner rewards**.

1. **Holders** pay "Network Rent" via decay.
2. **Miners** receive this rent as a permanent subsidy.
3. **Security** is mathematically guaranteed regardless of transaction volume.
4. **Supply** remains constant, creating a zero-sum recycling economy.

### Closing Thoughts: A Whale’s Sanctuary
From a game-theory perspective, this creates an unprecedented incentive to **consolidate**. The 1.0 coin mark becomes a "Great Filter"—those below it are fuel, while those above it are the protected gentry of the network.

---

### The RISC-V Supercomputer
By moving away from niche VMs and adopting the **RISC-V ISA**, the protocol allows for "Useful Work" that utilizes standard industry compilers (LLVM/GCC).

Holders don't just pay a tax; they fund a global computing resource. When a miner wins the **1.0 Whole Coin Lottery**, they have done so by providing verifiable CPU cycles to a task that actually matters—be it zero-knowledge proof generation or decentralized AI training.

### Practical Usage: The 1.0 Coin Safety Floor
While the protocol supports micro-transactions, users must be wary of the **"Event Horizon."** * **Transaction Cost:** A 0.01 transaction is cheap in fees, but expensive in risk if it pushes your balance below 1.0.
* **UX Suggestion:** Wallets should implement a "Hard Floor" alert, preventing users from spending into the Fractional Pool unless they explicitly intend to "sacrifice" their remaining balance to the miners.

---

### The Worker’s Gamble: Cycles as Lottery Tickets
The network transitions from "Mathematical Crunching" to "Useful Labor." By utilizing deterministic RISC-V execution, the protocol verifies work through result-hash consensus.

To ensure fairness, the **Whole Coin Rewards** (harvested from the decay of holders) are distributed via a Pro Rata Lottery based on verified CPU cycles.

* **Micro-Workers:** A single device performing 1,000,000 cycles has the same proportional chance to win a whole coin as a data center performing 1,000,000,000 cycles.
* **The Subsidy:** Because the "Jackpot" is funded by the fixed 100-year half-life of the holders, the cost for developers to submit tasks remains low, while the reward for miners remains high.

This is the first blockchain where "Dust" and "Decay" aren't just waste—they are the fuel for a global, scientific, and industrial engine.

### Preventing the Spoof: Bound Computation
To ensure that one miner cannot "copy-paste" their results to multiple identities, the protocol utilizes **Miner-Specific Task Binding**.

By salting the RISC-V input with the miner's public key, the resulting hash becomes a unique fingerprint. To "spoof" ten miners, an attacker would have to perform the computation ten times—rendering the attack economically pointless.

### The Lifecycle of a Coin
1. **Dust** is swept (lowest balance first) to fund the lottery.
2. **Whales** pay a pro-rata "security rent" to miners.
3. **Miners** perform assigned, deterministic RISC-V tasks.
4. **Lottery** rewards whole coins to those who provided the most cycles.

This creates a self-balancing machine: the more the network is used for computing, the more valuable the coin becomes; the more valuable the coin, the more security (miners) the decay can fund.

### Bespoke Reliability: The $R$-Factor
The protocol introduces **Selectable Redundancy**. Unlike standard chains where every node does everything, or Layer 2s where only one node does the work, our model allows the **Task Issuer** to define the safety margin.

By requiring **Unanimous Consensus** and **Final Issuer Approval**, the network ensures that miners are not just "crunching numbers," but delivering high-fidelity results.

### The Miner's Incentive
Miners are no longer competing against each other in a race to the bottom. They are competing for **Accuracy**.
1. **Accuracy leads to Approval.**
2. **Approval leads to Work Credits.**
3. **Work Credits lead to Whole Coin Wins.**

This completes the circle: The **Whale's Decay** funds a network that is not just "secure," but "useful," "accurate," and "controllable" by the very people who need the computation.

### Bespoke Reliability: The $R$-Factor
The protocol introduces **Selectable Redundancy**. Unlike standard chains where every node does everything, or Layer 2s where only one node does the work, our model allows the **Task Issuer** to define the safety margin.

By requiring **Unanimous Consensus** and **Final Issuer Approval**, the network ensures that miners are not just "crunching numbers," but delivering high-fidelity results.

### The Miner's Incentive
Miners are no longer competing against each other in a race to the bottom. They are competing for **Accuracy**.
1. **Accuracy leads to Approval.**
2. **Approval leads to Work Credits.**
3. **Work Credits lead to Whole Coin Wins.**

This completes the circle: The **Whale's Decay** funds a network that is not just "secure," but "useful," "accurate," and "controllable" by the very people who need the computation.

### The Bonded Market: Miner GFS
Participation in the computing pool requires a **Miner Good Faith Stake**. This stake is the "Anti-Spam" filter. If a miner provides an incorrect deterministic result, the stake is forfeited to the **Fractional Decay Pool**, effectively accelerating the "Dust Sweep" for the rest of the network.

### The Private Lottery: Forfeiting the General
When a dispute arises, the "Truth Seekers" (Verified Miners and Licensed Verifiers) can opt-in to a **Private Lottery** for the forfeited Issuer GFS.

* **The Catch:** Entry into the Private Lottery voids all Work Credits for the General Lottery for that cycle.
* **The Benefit:** This ensures that Verifiers are highly motivated to resolve disputes quickly and accurately, as the Private Lottery offers a much higher "Win Probability" than the global pool.

"In this network, the 'Whole Coin' is the only measure of truth. To work, you stake one. To win, you earn one. To lie, you lose one. By quantizing risk and reward, we have removed the noise of fractional volatility, leaving behind a pure, deterministic engine of value and computation."

# Protocol Spec: The Great Filter (TGF)

1.  **Supply:** Fixed, Conserved (Total Supply = $S$).
2.  **Decay:** 100-year Half-Life ($\approx 0.7\%$ annually).
    * Target: Wallets $< 1.0$ (Sorted smallest to largest).
    * Spillover: Wallets $\ge 1.0$ (Stochastic pro rata lottery for -1.0).
3.  **Compute (PoUW):** Deterministic RISC-V.
    * Miners must stake **1.0 Coin** (Good Faith Stake).
    * Issuers must stake **$\ge 1.0$ Coin** (Good Faith Stake).
4.  **Dispute Resolution:**
    * Licensed Verifiers (Proven via Licensing Tasks).
    * Malicious Issuers forfeit 1.0 GFS to a Private Lottery.
    * Inaccurate Miners forfeit 1.0 GFS to the Fractional Decay Pool.
5.  **Economic Loop:**
    * Decayed coins fund the **General Lottery**.
    * Winning a lottery awards exactly **1.0 Coin**.

#### Abstract
The Great Filter (TGF) is a fixed-supply, perpetual-security protocol utilizing a 100-year half-life decay model to fund a decentralized RISC-V computing network. 

#### Monetary Policy
- **Fixed Ledger:** Total supply is constant; coins are recycled, never destroyed.
- **Hierarchical Decay:** A 0.7% annual "Network Rent" is harvested from holders.
- **The Shield:** Small balances (<1.0) are swept first, providing a buffer for institutional whales.
- **The Roulette:** Mid-tier holders face a stochastic, whole-unit decay.

#### The Labor Market (PoUW)
- **Deterministic RISC-V:** Standard-ISA execution ensures verifiability.
- **Dual-Collateral:** Both Miners and Issuers must stake 1.0 Coin for every task.
- **The Lottery:** Decayed coins are redistributed to miners via a pro rata lottery based on verified CPU cycles.
- **Judicial Integrity:** Licensed Verifiers resolve disputes, with malicious actors forfeiting 1.0 Coin stakes to high-probability private lotteries.

#### Conclusion
TGF solves the "Security Budget" problem of fixed-supply blockchains by replacing dwindling block rewards with a perpetual wealth-recycling loop. It is a "Blue Chip" asset that acts as a self-sustaining utility for the world's computational needs.
