---
layout: post
mathjax: true
comments: true
title: "Constant Product AMM Mathematics"
date: 2026-01-29 17:08:11 +0000
categories: [crypto, defi, rust]
---

<!-- A73 -->

Automated Market Makers (AMMs) revolutionized on-chain liquidity
by replacing central limit order books with deterministic mathematical curves.
This post deconstructs the core equations of the Constant Product model.
This model is the foundation of protocols like Uniswap v2,
covering everything from swap mechanics and fees
to the linear geometry of liquidity and the risks of impermanent loss.

AMM math is also simpler than Concentrated Liquidity Market Maker (CLMM) math.
It is therefore foundational for future study.
This post will first cover AMM math.
After that, it will present the code for the following **AMM calculator widget**.
Other widgets could be written, but this post is sufficiently long as is.

<style>
  .amm-widget {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
    padding: 20px;
    border: 2px solid red;
    border-radius: 8px;
    max-width: 500px;
    background-color: #ffffff;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }

  .amm-widget div:nth-child(3) {
    grid-column: 1 / span 2;
    display: flex;
    flex-direction: column;
  }

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
2026-01-29 17:08:11 +0000

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

> **Concrete Example:**
Assume we have a pool that swaps **PIZZA** and **USD**.
Also, assume that the current price of a pizza is **$10**.
Our pool is trading the **PIZZA/USD** pair.
In financial markets, the price is quoted as 10, meaning **10 USD/PIZZA**.
You may see a price of 10 quoted for the **PIZZA/USD** pair,
and this can be very confusing!
>
The slash in the pair name is just a separator,
while the slash in the price is a mathematical unit.
In finance, the first asset in a pair is the **base (x)**
and the second is the **quote (y)**.
Because pizza is an expensive asset relative to the dollar,
the reserves are weighted toward the quote:
>
- **1000 Pizza** Base Reserves (x)
- **10000 USD** Quote Reserves (y)
- **10.00 Price** ($P = \frac y x$)
- ~3162.28 Liquidity ($L = \sqrt k = \sqrt{x \cdot y}$)

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

> **Liquidity to Reserve Units:**
L has units of $\sqrt{x \cdot y}$, while the term  $\sqrt P = \sqrt \frac y x$
is used to calculate reserves from the liquidity.
For **y reserves**, the units are
$\frac{\sqrt{x} \cdot \sqrt{y}}{1} \cdot \frac{\sqrt y}{\sqrt x} = y$.
Note that $\frac{1}{\sqrt P}$ is the **reciprocal** of the price,
or $\sqrt{\frac x y}$.
The units for **x reserves** are therefore 
$\frac{\sqrt{x} \cdot \sqrt{y}}{1} \cdot \frac{\sqrt x}{\sqrt y} = x$.

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

## From Math to Code

While these equations define the theoretical boundaries of a pool,
translating them into code requires careful handling of fixed-point math
and rounding errors to prevent dust accumulation or drainage.
The code for the AMM calculator is below.
Integration and usage assumes familiarity with Rust-based WASM,
as documented in [a post I wrote on the topic][post_wasm].

**`Cargo.toml` full listing**
```toml
[package]
name = "post_constant_amm_mathematics"
version = "0.1.0"
edition = "2024"

[lib]
crate-type = ["cdylib"]

[dependencies]
js-sys = "0.3.85"
ra-solana-math = "0.1.1"
wasm-bindgen = "0.2.108"
web-sys = { version = "0.3.85", features = ["Document", "Element", "Event", "EventTarget", "HtmlElement", "HtmlInputElement", "Node", "Window"] }
```

**`src/lib.rs` full listing**
```rust
use ra_solana_math::FixedPoint;
use std::rc::Rc;
use wasm_bindgen::JsCast;
use wasm_bindgen::prelude::*;
use web_sys::HtmlInputElement;

struct AmmCalculatorInputs {
    liq: HtmlInputElement,
    price: HtmlInputElement,
    slider: HtmlInputElement,
    x: HtmlInputElement,
    y: HtmlInputElement,
}

enum AmmCalculatorUpdateMode {
    FromLiqPrice,
    FromReserves,
}

#[wasm_bindgen]
pub fn amm_calculator_init(anchor_id: &str) {
    let window = web_sys::window().expect("Missing window");
    let document = window.document().expect("Missing document");
    let anchor = document
        .get_element_by_id(anchor_id)
        .expect("Missing anchor");

    // UI Container Setup
    let container = document.create_element("div").unwrap();
    container.set_id(&format!("{}-container", anchor_id));
    container.set_attribute("class", "amm-widget").unwrap();

    // Labeled Input Helper
    let create_input = |id: &str, label_text: &str, input_type: &str| {
        let div = document.create_element("div").unwrap();
        let label = document.create_element("label").unwrap();
        label.set_text_content(Some(label_text));
        let input = document
            .create_element("input")
            .unwrap()
            .dyn_into::<HtmlInputElement>()
            .unwrap();
        input.set_id(&format!("{}-{}", anchor_id, id));
        input.set_type(input_type);
        div.append_child(&label).unwrap();
        div.append_child(&input).unwrap();
        (div, input)
    };

    let (liq_div, liq_input) = create_input("liq", "Liquidity (L)", "text");
    let (price_div, price_input) = create_input("price", "Price (P)", "text");
    let (slider_div, slider_input) = create_input("slider", "Price Slider (Log)", "range");
    let (x_div, x_input) = create_input("x", "Reserve (X), Meme or Base", "text");
    let (y_div, y_input) = create_input("y", "Reserve (Y), Stable or Quote", "text");

    // Slider Configuration
    slider_input.set_min("-6");
    slider_input.set_max("6");
    slider_input.set_step("0.01");

    container.append_child(&liq_div).unwrap();
    container.append_child(&price_div).unwrap();
    container.append_child(&slider_div).unwrap();
    container.append_child(&x_div).unwrap();
    container.append_child(&y_div).unwrap();

    // Anchor Replacement
    anchor
        .parent_node()
        .unwrap()
        .replace_child(&container, &anchor)
        .unwrap();

    // Centralized Update Logic
    // Wrap inputs in Rc<RefCell> so they can be captured by multiple closures.
    let inputs = Rc::new(AmmCalculatorInputs {
        liq: liq_input,
        price: price_input,
        slider: slider_input,
        x: x_input,
        y: y_input,
    });

    let update_widget = {
        let inputs = inputs.clone();
        let zero = FixedPoint::from_int(0); // Reusable zero
        move |mode: AmmCalculatorUpdateMode| match mode {
            AmmCalculatorUpdateMode::FromLiqPrice => {
                let l_f = inputs.liq.value().parse::<f64>().unwrap_or(0.0);
                let p_f = inputs.price.value().parse::<f64>().unwrap_or(0.0);

                let l = FixedPoint::from_f64(l_f).unwrap_or(zero);
                let p = FixedPoint::from_f64(p_f).unwrap_or(zero);

                if let Ok(sqrt_p) = p.sqrt() {
                    let x = l.div(&sqrt_p).unwrap_or(zero);
                    let y = l.mul(&sqrt_p).unwrap_or(zero);

                    inputs
                        .x
                        .set_value(&format!("{:.6}", x.to_f64().unwrap_or(0.0)));
                    inputs
                        .y
                        .set_value(&format!("{:.6}", y.to_f64().unwrap_or(0.0)));

                    let p_float = p.to_f64().unwrap_or(0.0);
                    inputs.slider.set_value(&p_float.log10().to_string());
                }
            }
            AmmCalculatorUpdateMode::FromReserves => {
                let x_f = inputs.x.value().parse::<f64>().unwrap_or(0.0);
                let y_f = inputs.y.value().parse::<f64>().unwrap_or(0.0);

                let l_f = (x_f * y_f).sqrt();
                let p_f = if x_f != 0.0 { y_f / x_f } else { 0.0 };

                let l = FixedPoint::from_f64(l_f).unwrap_or(zero);
                let p = FixedPoint::from_f64(p_f).unwrap_or(zero);

                inputs
                    .liq
                    .set_value(&format!("{:.6}", l.to_f64().unwrap_or(0.0)));
                inputs
                    .price
                    .set_value(&format!("{:.6}", p.to_f64().unwrap_or(0.0)));

                inputs.slider.set_value(&p_f.log10().to_string());
            }
        }
    };

    // Callback Setup
    let update_rc = Rc::new(update_widget);

    let on_price_change = {
        let u = update_rc.clone();
        Closure::wrap(Box::new(move |_e: web_sys::Event| {
            u(AmmCalculatorUpdateMode::FromLiqPrice);
        }) as Box<dyn FnMut(_)>)
    };
    inputs
        .liq
        .add_event_listener_with_callback("input", on_price_change.as_ref().unchecked_ref())
        .unwrap();
    inputs
        .price
        .add_event_listener_with_callback("input", on_price_change.as_ref().unchecked_ref())
        .unwrap();
    on_price_change.forget();

    let on_slider_change = {
        let u = update_rc.clone();
        let ins = inputs.clone();
        Closure::wrap(Box::new(move |_e: web_sys::Event| {
            let val: f64 = ins.slider.value().parse().unwrap_or(0.0);
            let price = 10.0_f64.powf(val);
            ins.price.set_value(&format!("{:.6}", price));
            u(AmmCalculatorUpdateMode::FromLiqPrice);
        }) as Box<dyn FnMut(_)>)
    };
    inputs
        .slider
        .add_event_listener_with_callback("input", on_slider_change.as_ref().unchecked_ref())
        .unwrap();
    on_slider_change.forget();

    let on_reserve_change = {
        let u = update_rc.clone();
        Closure::wrap(Box::new(move |_e: web_sys::Event| {
            u(AmmCalculatorUpdateMode::FromReserves);
        }) as Box<dyn FnMut(_)>)
    };

    inputs
        .x
        .add_event_listener_with_callback("input", on_reserve_change.as_ref().unchecked_ref())
        .unwrap();
    inputs
        .y
        .add_event_listener_with_callback("input", on_reserve_change.as_ref().unchecked_ref())
        .unwrap();
    on_reserve_change.forget();

    // Default Values
    inputs.liq.set_value("1000000.000000");
    inputs.price.set_value("0.007000");
    update_rc(AmmCalculatorUpdateMode::FromLiqPrice);
}
```

**Widget JS Injection Anchor Example**
```html
<script type="module" id="amm_calculator_ui">
  import init, { amm_calculator_init } from "/assets/wasm/post_constant_amm_mathematics/post_constant_amm_mathematics.js";
  async function run() {
    await init();
    amm_calculator_init("amm_calculator_ui");
  }
  run();
</script>
```

**Widget Inline CSS Styling Example**
```html
<style>
  .amm-widget {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
    padding: 20px;
    border: 2px solid red;
    border-radius: 8px;
    max-width: 500px;
    background-color: #ffffff;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }

  .amm-widget div:nth-child(3) {
    grid-column: 1 / span 2;
    display: flex;
    flex-direction: column;
  }

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

  @media (max-width: 400px) {
    .amm-widget {
      grid-template-columns: 1fr;
    }
    .amm-widget div:nth-child(3) {
      grid-column: 1;
    }
  }
</style>
```

## Conclusion

The Constant Product Formula
is a masterpiece of simple yet profound engineering.
By reducing the complexity of a market to a single invariant ($k$),
it created a system where liquidity is always available,
prices are mathematically predictable, and anyone can become a market maker.
Whether you are building a trading bot or a new DEX,
understanding the relationship between reserves, price,
and liquidity is the first step toward mastering DeFi.

---

## References:

- [Impermanent Loss, How to calculate Impermanent Loss: full derivation][il_derivation]
- [Impermanent Loss, What is Impermanent Loss in Crypto? YouTube][il_video]
- [Impermanent Loss Explained, Binance Academy][il_binance]
- [Related Post, WASM on a Jekyll Blog with Rust and wasm-bindgen][post_wasm]

[il_binance]: https://www.binance.com/en/academy/articles/impermanent-loss-explained
[il_derivation]: https://medium.com/auditless/how-to-calculate-impermanent-loss-full-derivation-803e8b2497b7
[il_video]: https://www.youtube.com/watch?v=_m6Mowq3Ptk
[post_wasm]: {% post_url 2026-01-26-webasm_on_jekyll %}

