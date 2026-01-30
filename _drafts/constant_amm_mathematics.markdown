---
layout: post
mathjax: true
comments: true
title:  "Constant Product AMM Mathematics"
date:   2026-01-27 07:06:41 +0000
categories: [crypto, defi, rust]
---
Automated Market Makers (AMMs) revolutionized on-chain liquidity
by replacing central limit order books with deterministic mathematical curves.
This post deconstructs the core equations of the Constant Product model.
This model is the foundation of protocols like Uniswap v2,
covering everything from swap mechanics and fees
to the linear geometry of liquidity and the risks of impermanent loss.

<style>
  .amm-widget {
    display: grid;
    grid-template-columns: 1fr 1fr; /* Two equal columns */
    gap: 15px;
    padding: 20px;
    border: 2px solid red; /* Red outline as requested */
    border-radius: 8px;
    max-width: 500px;
    background-color: #ffffff;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }

  /* Force the Slider to take up the entire second row */
  .amm-widget div:nth-child(3) {
    grid-column: 1 / span 2;
    display: flex;
    flex-direction: column;
  }

  /* General styling for the input groups */
  .amm-widget div {
    display: flex;
    flex-direction: column;
    gap: 5px;
  }

  .amm-widget label {
    font-size: 0.85rem;
    font-weight: 600;
    color: #333;
  }

  .amm-widget input[type="text"] {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 1rem;
    width: 100%;
    box-sizing: border-box;
  }

  .amm-widget input[type="range"] {
    width: 100%;
    margin: 10px 0;
  }

  /* Responsive adjustment for mobile */
  @media (max-width: 400px) {
    .amm-widget {
      grid-template-columns: 1fr;
    }
    .amm-widget div:nth-child(3) {
      grid-column: 1;
    }
  }
</style>

<script type="module" id="amm_calculator_ui">
  import init, { amm_calculator_init } from "/assets/wasm/post_constant_amm_mathematics/post_constant_amm_mathematics.js";
  async function run() {
    await init();
    amm_calculator_init("amm_calculator_ui");
  }
  run();
</script>

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-01-27 07:06:41 +0000

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

$ "${SHELL}" --version  | head -n 1
GNU bash, version 3.2.57(1)-release (arm64-apple-darwin23)

# Rust Installation Versions
$ cargo --version
cargo 1.93.0 (083ac5135 2025-12-15)
```

## Constant Product AMM Architecture

At the core of Decentralized Finance (DeFi)
is the Constant Product Market Maker (CPMM).
This specific branch of mathematics replaces the traditional order book
with an automated peer-to-pool model,
ensuring that a trade can be executed at any time,
regardless of counterparty availability.

### Constant Product Formula

The vast majority of AMMs use the **Constant Product Formula**
to model the smart contract liquidity pool curve.
This formula is an industry standard, but its use is not a hard rule.
Any smart contract is free to use whatever model it wants,
but this post assumes the Constant Product Formula.
It dictates that the product of the two asset quantities
must remain constant during any trade.

$$x \cdot y = k$$

- **$x$ (Token X Reserve):**
The total inventory of the first asset (e.g., memecoin or basecoin)
currently held in the AMM smart contract. 
[**Unit:** Token X]

- **$y$ (Token Y Reserve):**
The total inventory of the second asset (e.g., stablecoin or quotecoin)
currently held in the AMM smart contract. 
[**Unit:** Token Y]

- **$k$ (Invariant):**
A fixed value that defines the pool's pricing curve.
This value is a constant during swaps and only changes when
liquidity is added to or removed from the pool.
[**Unit:** Token X $\cdot$ Token Y]

> **Base and Quote Convention:**
In financial markets, price is a ratio between two assets.
The asset being priced is the **base**,
and the currency used to measure it is the **quote**.
By convention, price is expressed as
the value of one unit of the base asset in terms of the quote asset.
This maps directly to the AMM formula $P = \frac y x$.
For example, if your price is quoted as **0.007 MEME/USD**, the assignment is:
>
- x (Base Asset) = MEME
- y (Quote Asset) = USD
>
If the price is 0.007 MEME/USD,
your pool will have a large reserve of MEME, and a small reserve of USD.
This is because each MEME is worth very little,
the contract must hold a much higher quantity of them to
maintain the equilibrium of the constant product.

### Liquidity

In modern liquidity pool implementations,
**Liquidity ($L$)** is defined as the square root of the invariant.
This representation allows for a more linear understanding
of pool depth and simplifies the relationship between the price and reserves.

$$L^2 = k = x \cdot y \quad \Big| \quad L = \sqrt k = \sqrt{x \cdot y} \quad \Big| \quad x = \frac{L}{\sqrt P} \quad \Big| \quad y = L \cdot \sqrt P \quad \Big| \quad P = \frac{y}{x}$$

- **$x, y, k$**: Original reserves and invariant as defined in the previous sections.

- **$L$ (Liquidity):**
A measure of the pool's "depth."
This value remains constant during swaps and only changes
when liquidity is added or removed.
[**Unit:** $\sqrt{\text{Token X} \cdot \text{Token Y}}$]

- **$P$ (Spot Price):**
The current marginal exchange rate of the pool.
[**Unit:** Token Y / Token X]

> **Technical Insight:**
The square root operation effectively reduces the two-dimensional area
of the invariant ($k$) to a single linear dimension ($L$).
This linearizes the relationship between capital and pool depth.
*For example, doubling the assets in the pool results in a 2x increase in $L$,
rather than a 4x increase in $k$.*

### Swap Execution Formula

To maintain the invariant ($k$) when a trader interacts with the pool,
we use the **Swap Execution Formula**.
This represents the state of the pool before and after a transaction.
When you perform a swap,
the smart contract calculates exactly how many tokens to move.
This is derived by solving the constant product invariant
for the unknown variable ($\Delta x$ or $\Delta y$).

$$(x - \Delta x) \cdot (y + \Delta y) = k \quad \Big| \quad \Delta x = \frac{x \cdot \Delta y}{y + \Delta y} \quad \Big| \quad \Delta y = \frac{y \cdot \Delta x}{x - \Delta x}$$

- **$x, y, k$**: Original reserves and invariant as defined in the previous sections.

- **$\Delta x$ (Swap Output):**
The number of tokens (e.g., memecoin or basecoin) the trader receives from the pool.
[**Unit:** Token X]

- **$\Delta y$ (Swap Input):**
The number of tokens (e.g., stablecoin or quotecoin) the trader deposits into the pool.
[**Unit:** Token Y]

> **Note on Slippage:**
Because the denominator of the $\Delta x$ solution includes $\Delta y$,
as the input quantity increases, the output does not grow linearly.
This mathematical reality is what creates **Price Impact**.
The more you buy, the more expensive each subsequent unit becomes.

### Swap Execution Formula with Fees

The fee calculations extend the ideal Swap Execution Formula.
Before the trade is executed,
the pool takes a percentage fee ($f$) of the token input
before performing the constant product calculation.
This creates a divergence between the zero fee **ideal swap**
and the actual **net swap** that hits the trader's wallet.

The service fee can be set aside for liquidity providers,
or it can be reinvested into the pool,
depending on how the smart contract is set up.
For real world use cases, see your pool documentation.

$$(x - \Delta x_{net}) \cdot (y + \Delta y_{net}) = k \quad \Big| \quad \Delta x_{net} = \frac{x \cdot \Delta x \cdot (1 - f)}{x - \Delta x \cdot f} = \frac{x \cdot \Delta y \cdot (1 - f)}{y + \Delta y \cdot (1 - f)} \quad \Big| \quad \Delta y_{net} = \Delta y \cdot (1 - f) = \frac{y \cdot \Delta x \cdot (1 - f)}{x - \Delta x}$$

- **$x, y, k$**:
Original reserves and invariant as defined in the previous sections.

- **$\Delta x, \Delta y$**:
Ideal output/input values assuming zero fees, as defined in the previous section.

- **$f$ (Fee):** Service fee taken by the pool (e.g., $0.003$ for $0.3\%$). [**Dimensionless**]

- **$\Delta x_{net}$ (Net Swap Output):**
The actual quantity of tokens (e.g., memecoin or basecoin)
the trader receives after fees are deducted from the input.
[**Unit:** Token X]

- **$\Delta y_{net}$ (Net Swap Input):**
The portion of the trader's deposit (e.g., stablecoin or quotecoin)
that actually shifts the price.
The remainder $(\Delta y \cdot f)$ is the fee collected by the pool.
[**Unit:** Token Y]

### Post-Trade Price Equations

After a trade is executed, the balance of the pool has shifted.
Because there are now more of Token Y and fewer of Token X,
the price of Token X increases.
The **new spot price** represents
the marginal price for the very next trader in line.

$$P_{old} = \frac{y}{x} \quad \Big| \quad P_{effective} = \frac{\Delta y}{\Delta x_{net}} \quad \Big| \quad P_{new} = \frac{y + \Delta y}{x - \Delta x_{net}}$$

- **$P_{old}$ (Pre-Trade Spot Price):**
The market price before the transaction occurs.
[**Unit:** Token Y / Token X]

- **$P_{effective}$ (Execution Price):**
The average price paid for the entire swap.
Due to slippage, this is always higher than $P_{old}$ and lower than $P_{new}$.
Note that although the total gross $\Delta y$ is deposited,
only $\Delta x_{net}$ is received by the trader after fees.
[**Unit:** Token Y / Token X]

- **$P_{new}$ (Post-Trade Spot Price):**
The updated marginal price of the pool after the reserves have been rebalanced.
This assumes the fee is reinvested into the pool.
Use $\Delta y_{net}$ in the numerator if fees are paid out to a treasury.
[**Unit:** Token Y / Token X]

- **$y + \Delta y$**:
New Reserve of Token Y with reinvestment.
Original inventory plus the trader's total deposit.

- **$y + \Delta y_{net}$**:
New Reserve of Token Y without reinvestment.
Original inventory plus the trader's total deposit less fees.

- **$x - \Delta x_{net}$**:
New Reserve of Token X.
Original inventory minus the trader's payout.

> **Note on Price Impact:**
The difference between $P_{old}$ and $P_{effective}$
is what traders refer to as **Price Impact**.
On large trades, the gap between these three prices widens significantly.

### Liquidity Provision Equations

Adding liquidity expands the pool's reserves of both assets simultaneously.
To avoid shifting the market price during a deposit,
assets must be provided proportionally to the existing ratio.
This action pushes the constant product curve outward,
increasing the pool's invariant ($k$).

$$\Delta k = (x + \Delta x)(y + \Delta y) - xy \quad \Big| \quad \Delta x = \frac{x \cdot \Delta y}{y} \quad \Big| \quad \Delta y = \frac{y \cdot \Delta x}{x}$$

- **$x, y, k$**:
Original reserves and invariant as defined in the previous sections.

- **$\Delta x$ (Token X Deposit):**
The amount of Token X (e.g., memecoin or basecoin)
provided by the Liquidity Provider.
[**Unit:** Token X]

- **$\Delta y$ (Token Y Deposit):**
The amount of Token Y (e.g., stablecoin or quotecoin)
provided by the Liquidity Provider.
[**Unit:** Token Y]

- **$\Delta k$ (Change in Invariant):**
The increase in the pool's product.
This represents the added "depth" of the pool.
Generally positive, representing pool growth.
A negative value indicates liquidity withdrawal.
[**Unit:** Token X $\cdot$ Token Y]

> **Note on Price Stability:**
For a standard deposit, the ratio $\frac{\Delta y}{\Delta x}$
must equal the current spot price $\frac{y}{x}$.
If a provider deposits a disproportionate amount,
they are effectively performing a "swap" against the pool,
shifting the price and incurring slippage before their liquidity is staked.
Single-asset and disproportionate deposits are mathematically possible,
but generally disallowed by AMM smart contracts in practice.

### Impermanent Loss Formula

**Impermanent Loss (IL)** is the difference in value between holding
a set of assets in a liquidity pool versus simply holding them
in a private wallet.
It occurs because the AMM's constant product formula rebalances your
position as prices change,
effectively selling the "winner" and buying more of the "loser."

$$IL(r) = \frac{2\sqrt{r}}{1+r} - 1$$

- **$IL(r)$ (Impermanent Loss):**
The percentage difference in the total value
of your position compared to holding.
This result is always $\le 0$ (a loss),
though it is "impermanent" because it can disappear
if the price ratio returns to its original state.
Generally expressed as a percentage.
[**Dimensionless**]

- **$r$ (Price Ratio):**
The ratio of the new price to the original price ($P_{new} / P_{old}$).
For example, if the meme coin price doubles, $r = 2$.
[**Dimensionless**]

### IL Reference Benchmarks

| Price Example ($P_{new}$) | Price Ratio ($r$) | Impermanent Loss |
| :------ | :--- | :----- |
| 0.00700 | 1.00 |   0.0% |
| 0.00875 | 1.25 |  -0.6% |
| 0.01050 | 1.50 |  -2.0% |
| 0.01225 | 1.75 |  -3.8% |
| 0.01400 | 2.00 |  -5.7% |
| 0.02100 | 3.00 | -13.4% |
| 0.02800 | 4.00 | -20.0% |
| 0.03500 | 5.00 | -25.5% |

> **Note on Fees:**
In practice, LPs provide liquidity to earn trading fees.
If the accumulated fees earned during the period are greater than the $IL(r)$,
the liquidity provider still walks away with a net profit.

### From Math to Code

While these equations define the theoretical boundaries of a pool,
translating them into code requires careful handling of fixed-point math
and rounding errors to prevent 'dust' accumulation or drainage.
In the next section, we will implement these formulas
in Rust to build a functional AMM simulator.

---

## References:

- [Impermanent Loss, How to calculate Impermanent Loss: full derivation][il_derivation]
- [Impermanent Loss, What is Impermanent Loss in Crypto? YouTube][il_video]
- [Impermanent Loss Explained, Binance Academy][il_binance]

[il_binance]: https://www.binance.com/en/academy/articles/impermanent-loss-explained
[il_derivation]: https://medium.com/auditless/how-to-calculate-impermanent-loss-full-derivation-803e8b2497b7
[il_video]: https://www.youtube.com/watch?v=_m6Mowq3Ptk

