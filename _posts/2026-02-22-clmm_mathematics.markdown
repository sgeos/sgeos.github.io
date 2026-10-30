---
layout: post
mathjax: true
comments: true
title: "Concentrated Liquidity Market Maker Mathematics"
date: 2026-02-22 10:01:47 +0000
categories: crypto defi rust
---

<!-- A91 -->
<script>console.log("A91");</script>

Concentrated Liquidity Market Makers (CLMMs) extend the Constant Product model
by allowing liquidity providers to allocate capital within a chosen price range
rather than across the entire price domain.
This post deconstructs the core equations of the Concentrated Liquidity model,
the architecture introduced by Uniswap v3 and now the dominant design
in decentralized finance.

This article assumes familiarity with the
[Constant Product AMM Mathematics][related_post_cpamm] article,
which covers the foundational invariant, liquidity, swap execution, fees,
and impermanent loss for the full-range model.
The CLMM extends every one of those concepts
by restricting the active region of the curve to a finite price interval.
This post will first cover CLMM math.
After that, it will present the code for the following **CLMM calculator widget**.

<style>
  .clmm-widget {
    display: grid;
    grid-template-columns: 1fr;
    gap: 12px;
    padding: 20px;
    border: 2px solid #007bff;
    border-radius: 8px;
    max-width: 750px;
    background-color: #ffffff;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }

  .clmm-widget .clmm-row-1 {
    display: flex;
    flex-direction: column;
    gap: 5px;
  }

  .clmm-widget .clmm-row-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
  }

  .clmm-widget .clmm-row-slider {
    display: flex;
    flex-direction: column;
    gap: 5px;
    padding: 10px;
    background: #f6f8fa;
    border-radius: 6px;
  }

  .clmm-widget .clmm-field {
    display: flex;
    flex-direction: column;
    gap: 5px;
  }

  .clmm-widget label {
    font-size: 0.85rem;
    font-weight: 600;
    color: #333;
  }

  .clmm-widget input[type="text"] {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 1rem;
    width: 100%;
    box-sizing: border-box;
  }

  .clmm-widget input[type="range"] {
    width: 100%;
    margin: 5px 0;
  }

  @media (max-width: 500px) {
    .clmm-widget .clmm-row-3 {
      grid-template-columns: 1fr;
    }
  }
</style>

<script type="module" id="clmm_calculator_ui">
  import init, { inject_ui } from "/assets/wasm/post_clmm_mathematics/post_clmm_mathematics.js";
  async function run() {
    await init();
    inject_ui("clmm_calculator_ui");
  }
  run();
</script>

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-02-22 10:01:47 +0000

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

## Concentrated Liquidity Architecture

At the core of the Constant Product model is the invariant $x \cdot y = L^2$,
where $x$ and $y$ are the reserves of the two tokens
and $L = \sqrt{x \cdot y}$ is the liquidity.
In a full-range Automated Market Maker (AMM),
capital is spread across the entire price domain from zero to infinity.
The vast majority of that capital sits idle at prices far from the current trading price.

The innovation of concentrated liquidity
is to allow each liquidity provider to choose a finite price interval $[p_a, p_b]$
within which their capital is active.
Within that interval, the position behaves exactly like a constant product AMM.
Outside that interval, the position holds only one token and earns no fees.
The result is that a given amount of capital provides substantially deeper liquidity
around the current price,
improving capital efficiency by orders of magnitude for narrow ranges.

A pool aggregates many individual concentrated positions,
each covering potentially different price intervals.
The aggregate liquidity at any given price
is the sum of all positions whose ranges contain that price.

### From Constant Product to Concentrated Liquidity

The starting point is the constant product invariant.

$$
x \cdot y = L^2
\tag{1}
$$

The current price $p$ of Token X in terms of Token Y satisfies $p = \frac{y}{x}$.
The reserves can be expressed in terms of $L$ and $p$ as follows.

$$
x = \frac{L}{\sqrt{p}} \qquad y = L \cdot \sqrt{p}
\tag{2}
$$

These are the **virtual reserves** on the full unbounded curve.
They satisfy $x \cdot y = L^2$ and $\frac{y}{x} = p$.

In a concentrated liquidity position with price range $[p_a, p_b]$,
the contract behaves as though the full $x \cdot y = L^2$ curve exists,
but only the segment between prices $p_a$ and $p_b$ is funded with real tokens.
The virtual reserves at any current price $p$ within the range are as follows.

$$
x_v(p) = \frac{L}{\sqrt{p}} \qquad y_v(p) = L \cdot \sqrt{p}
\tag{3}
$$

The **real reserves** are obtained by translating the constant product curve.
The curve segment between $p_a$ and $p_b$ is shifted
so that the real reserves reach zero at the range boundaries.
The translated invariant is as follows.

$$
\left(x_r + \frac{L}{\sqrt{p_b}}\right) \cdot \left(y_r + L \cdot \sqrt{p_a}\right) = L^2
\tag{4}
$$

This is the standard constant product curve
shifted left by $\frac{L}{\sqrt{p_b}}$ and down by $L \cdot \sqrt{p_a}$.
The real reserves $x_r$ and $y_r$ are what the liquidity provider actually deposits and holds.

> **Geometric Interpretation:**
The virtual reserves describe a point on the standard hyperbola $x \cdot y = L^2$.
The real reserves represent the same curve
translated so that the lower-left corner of the active segment sits at the origin.
At price $p_a$, all real reserves are in Token X and $y_r = 0$.
At price $p_b$, all real reserves are in Token Y and $x_r = 0$.

### Real Reserves Formulas

When the current price $p$ is within the range $[p_a, p_b]$,
the real reserves are as follows.

$$
x_r = L \cdot \left(\frac{1}{\sqrt{p}} - \frac{1}{\sqrt{p_b}}\right) = \frac{L \cdot \left(\sqrt{p_b} - \sqrt{p}\right)}{\sqrt{p} \cdot \sqrt{p_b}}
\tag{5}
$$

$$
y_r = L \cdot \left(\sqrt{p} - \sqrt{p_a}\right)
\tag{6}
$$

- **$x_r$ (Token X Real Reserve):**
The amount of Token X held by the position.
This quantity decreases as the price rises
and reaches zero when $p = p_b$.
[**Unit:** Token X]

- **$y_r$ (Token Y Real Reserve):**
The amount of Token Y held by the position.
This quantity increases as the price rises
and reaches its maximum when $p = p_b$.
[**Unit:** Token Y]

- **$L$ (Liquidity):**
The liquidity of the position,
identical in definition to the full-range constant product model.
[**Unit:** $\sqrt{\text{Token X} \cdot \text{Token Y}}$]

- **$p_a, p_b$ (Price Range Boundaries):**
The lower and upper bounds of the liquidity position.
[**Unit:** Token Y / Token X]

These are the core equations.
They correspond to Equations 6.29 and 6.30
in the [Uniswap v3 whitepaper][ref_uniswap_v3_whitepaper].

### Three Price Regimes

The token amounts held by a position
depend on where the current price $p$ falls relative to the range.
There are three regimes.

**Regime 1. Price below range ($p \le p_a$).**
The position is entirely Token X and earns no fees.

$$
x_r = \frac{L \cdot \left(\sqrt{p_b} - \sqrt{p_a}\right)}{\sqrt{p_a} \cdot \sqrt{p_b}} \qquad y_r = 0
\tag{7}
$$

**Regime 2. Price within range ($p_a < p < p_b$).**
The position holds both tokens and earns fees on swaps.

$$
x_r = \frac{L \cdot \left(\sqrt{p_b} - \sqrt{p}\right)}{\sqrt{p} \cdot \sqrt{p_b}} \qquad y_r = L \cdot \left(\sqrt{p} - \sqrt{p_a}\right)
\tag{8}
$$

**Regime 3. Price above range ($p \ge p_b$).**
The position is entirely Token Y and earns no fees.

$$
x_r = 0 \qquad y_r = L \cdot \left(\sqrt{p_b} - \sqrt{p_a}\right)
\tag{9}
$$

> **Note on Regime Transitions:**
As the price rises through the range from $p_a$ to $p_b$,
the position progressively converts Token X into Token Y.
When the price crosses a boundary,
the position becomes fully denominated in a single token.
If the price later re-enters the range, the position resumes earning fees.

### Computing Liquidity from a Deposit

Given a deposit of $\Delta x$ of Token X and $\Delta y$ of Token Y
at current price $p$ within range $[p_a, p_b]$,
the liquidity $L$ is determined by the limiting token.

From the Token X amount, the liquidity implied is as follows.

$$
L_x = \frac{\Delta x \cdot \sqrt{p} \cdot \sqrt{p_b}}{\sqrt{p_b} - \sqrt{p}}
\tag{10}
$$

From the Token Y amount, the liquidity implied is as follows.

$$
L_y = \frac{\Delta y}{\sqrt{p} - \sqrt{p_a}}
\tag{11}
$$

The effective liquidity of the position is the minimum of the two.

$$
L = \min(L_x,\ L_y)
\tag{12}
$$

The minimum is taken because the position is constrained by whichever token is the limiting factor.
Any excess of the other token is returned to the depositor.

When the price is at or below $p_a$, only Token X is required and $L = L_x$.
When the price is at or above $p_b$, only Token Y is required and $L = L_y$.

> **Contrast with Full-Range CPAMM:**
In the Constant Product model,
adding liquidity requires both tokens in proportion to the current price ratio.
In the Concentrated Liquidity model,
the deposit ratio depends on where the current price sits within the chosen range.
At the lower bound, the deposit is entirely Token X.
At the upper bound, the deposit is entirely Token Y.

### Tick Mathematics

Prices in Uniswap v3 are discretized into **ticks**.
Each tick $i$ corresponds to a price as follows.

$$
p(i) = 1.0001^i
\tag{13}
$$

Each tick therefore represents a 0.01% multiplicative change in price,
equivalent to one basis point.
The tick index for a given price is as follows.

$$
i = \left\lfloor \frac{\ln(p)}{\ln(1.0001)} \right\rfloor
\tag{14}
$$

The protocol stores $\sqrt{p}$ rather than $p$ directly
because the key reserve formulas involve $\sqrt{p}$
and storing the square root avoids computing it on-chain.
The square root price from a tick index is as follows.

$$
\sqrt{p(i)} = 1.0001^{i/2}
\tag{15}
$$

**Tick spacing** constrains which ticks can serve as position boundaries.
Only tick indices that are multiples of the tick spacing are allowed.
Smaller tick spacing permits more precise ranges
but increases gas costs because each initialized tick crossed during a swap
imposes additional computation.

The standard fee tiers and their corresponding tick spacings are as follows.

| Fee Tier | Basis Points | Tick Spacing |
| :------- | :----------- | :----------- |
| 0.01%    | 1 bp         | 1            |
| 0.05%    | 5 bp         | 10           |
| 0.30%    | 30 bp        | 60           |
| 1.00%    | 100 bp       | 200          |

> **Note on Governance:**
The 1 basis point fee tier was not in the original Uniswap v3 deployment.
It was added by governance vote in March 2022
to improve competitiveness for stablecoin pairs.

### Capital Efficiency

A concentrated position in range $[p_a, p_b]$
provides the same depth of liquidity
as a full-range position that holds significantly more capital.
The intuition is straightforward.
A full-range position must hold reserves to cover trading at every possible price.
A concentrated position only needs reserves for its chosen range,
so the same dollar amount of capital produces proportionally deeper liquidity within that range.

For a position centered at current price $p$ with range $[p_a, p_b]$,
the capital efficiency relative to a full-range position is approximately as follows.

$$
\text{efficiency} \approx \frac{1}{1 - \left(\frac{p_a}{p_b}\right)^{1/4}}
\tag{16}
$$

For very tight stablecoin ranges,
the efficiency multiplier can reach up to 4000x.
For example, a position in the range 0.999 to 1.001 for a stablecoin pair
provides liquidity equivalent to a full-range position
with thousands of times more capital.

> **Tradeoff:**
Higher capital efficiency comes with higher risk.
A narrower range means the position is more likely to move out of range,
at which point it stops earning fees
and is fully converted to the less valuable token.
Selecting a range is therefore a risk management decision.

### Fee Accrual in Concentrated Liquidity

Fees in a CLMM are earned only when the position is in range,
that is, when $p_a \le p \le p_b$.
The protocol tracks fee accumulation using a global variable $f_g$
that records the total fees earned per unit of liquidity since the pool was created.

For each tick boundary,
the protocol tracks $f_o$,
which records fees accumulated on the other side of that tick.
The fees earned within a position's range are computed as follows.

$$
f_{\text{inside}} = f_g - f_{\text{below}}(p_a) - f_{\text{above}}(p_b)
\tag{17}
$$

The fees owed to a specific position are then as follows.

$$
\text{fees} = \left(f_{\text{inside}} - f_{\text{inside,last}}\right) \cdot L
\tag{18}
$$

The value $f_{\text{inside,last}}$
is the inside fee growth at the time the position was last updated.
A position is updated when it is created, modified, or when fees are collected.
The value $L$ is the position's liquidity.

This design means that positions only need to be updated
when their tick boundaries are crossed or when the LP interacts with the position,
rather than on every swap.

### Impermanent Loss in Concentrated Positions

For a standard full-range constant product position,
the impermanent loss as a function of the price ratio $r = \frac{p_{\text{new}}}{p_{\text{old}}}$
is as follows.

$$
IL(r) = \frac{2\sqrt{r}}{1 + r} - 1
\tag{19}
$$

Concentrated liquidity amplifies impermanent loss
because the position is effectively leveraged.
The position converts between Tokens X and Y across a narrower price range,
so the same price movement causes a proportionally larger change in portfolio composition.

The value of a concentrated liquidity position at price $p$
when $p_a \le p \le p_b$ is as follows.

$$
V(p) = x_r \cdot p + y_r = L \cdot \left(2\sqrt{p} - \frac{p}{\sqrt{p_b}} - \sqrt{p_a}\right)
\tag{20}
$$

The impermanent loss for a concentrated position
is the difference between this value
and the value of simply holding the initial token quantities at the new price.
Qualitatively, a position that is $N$ times more capital-efficient
also experiences approximately $N$ times more impermanent loss per unit of capital deployed.

Research by Loesch, Hindman, Richardson, and Welch
demonstrates that even when a liquidity range is large enough
to accommodate prices doubling or halving,
the impermanent loss is nearly four times higher
than a full-range position [research_loesch_il].

> **Note on Range Selection:**
The amplification of impermanent loss is the direct cost
of the capital efficiency gained by concentrating liquidity.
A liquidity provider must weigh the additional fee income
earned from deeper liquidity
against the increased impermanent loss risk.

## From Math to Code

The equations above define the theoretical model.
Translating them into code requires handling floating-point arithmetic
and user interaction across multiple input modes.
The following Rust code implements the CLMM calculator widget
shown at the top of this article.
Integration and usage assumes familiarity with Rust-based WASM,
as documented in [a post on the topic][related_post_wasm].

The calculator supports three update modes.
Editing the liquidity or price fields recomputes inventories.
Moving the position slider interpolates the current price in $\sqrt{p}$ space.
Editing the inventory fields recomputes the liquidity using the $\min(L_x, L_y)$ formula.

**`Cargo.toml` full listing**
```toml
[package]
name = "post_clmm_mathematics"
version = "0.1.0"
edition = "2024"

[lib]
crate-type = ["cdylib"]

[dependencies]
wasm-bindgen = "0.2.108"
web-sys = { version = "0.3.85", features = ["Document", "Element", "Event", "EventTarget", "HtmlElement", "HtmlInputElement", "Node", "Window"] }
```

**`src/lib.rs` full listing**
```rust
use std::rc::Rc;
use wasm_bindgen::JsCast;
use wasm_bindgen::prelude::*;
use web_sys::HtmlInputElement;

struct ClmmCalculatorInputs {
    liq: HtmlInputElement,
    min_price: HtmlInputElement,
    cur_price: HtmlInputElement,
    max_price: HtmlInputElement,
    slider: HtmlInputElement,
    pos_input: HtmlInputElement,
    x: HtmlInputElement,
    y: HtmlInputElement,
}

enum ClmmCalculatorUpdateMode {
    FromPricesAndLiquidity,
    FromPositionSlider,
    FromReserves,
}

fn parse_f64(input: &HtmlInputElement) -> f64 {
    input.value().parse::<f64>().unwrap_or(0.0)
}

fn repopulate(inputs: &ClmmCalculatorInputs, p_a: f64, p_c: f64, p_b: f64, l: f64) {
    if p_a <= 0.0 || p_b <= 0.0 || p_b <= p_a || l < 0.0 {
        return;
    }

    inputs.min_price.set_value(&format!("{}", p_a));
    inputs.max_price.set_value(&format!("{}", p_b));
    inputs.cur_price.set_value(&format!("{:.6}", p_c));
    inputs.liq.set_value(&format!("{:.6}", l));

    let sqrt_a = p_a.sqrt();
    let sqrt_b = p_b.sqrt();
    let sqrt_c = p_c.sqrt();

    // Position slider value in sqrt price space
    let pos = if sqrt_b > sqrt_a {
        ((sqrt_c - sqrt_a) / (sqrt_b - sqrt_a)).clamp(0.0, 1.0)
    } else {
        0.5
    };
    inputs.slider.set_value(&format!("{:.4}", pos));
    inputs.pos_input.set_value(&format!("{:.4}", pos));

    // Token amounts based on price regime
    let (x, y) = if p_c <= p_a {
        // Below range: all Token X
        let x = l * (sqrt_b - sqrt_a) / (sqrt_a * sqrt_b);
        (x, 0.0)
    } else if p_c >= p_b {
        // Above range: all Token Y
        let y = l * (sqrt_b - sqrt_a);
        (0.0, y)
    } else {
        // In range: both tokens
        let x = l * (sqrt_b - sqrt_c) / (sqrt_c * sqrt_b);
        let y = l * (sqrt_c - sqrt_a);
        (x, y)
    };

    inputs.x.set_value(&format!("{:.2}", x));
    inputs.y.set_value(&format!("{:.2}", y));
}

#[wasm_bindgen]
pub fn inject_ui(anchor_id: &str) {
    let window = web_sys::window().expect("Missing window");
    let document = window.document().expect("Missing document");
    let anchor = document
        .get_element_by_id(anchor_id)
        .expect("Missing anchor");

    // UI Container
    let container = document.create_element("div").unwrap();
    container.set_id(&format!("{}-container", anchor_id));
    container.set_attribute("class", "clmm-widget").unwrap();

    // Labeled Input Helper
    let create_input =
        |id: &str, label_text: &str, input_type: &str, css_class: Option<&str>| {
            let div = document.create_element("div").unwrap();
            if let Some(cls) = css_class {
                div.set_attribute("class", cls).unwrap();
            } else {
                div.set_attribute("class", "clmm-field").unwrap();
            }
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

    // Row 1: Liquidity
    let (liq_div, liq_input) = create_input("liq", "Liquidity Depth (L)", "text", Some("clmm-row-1"));
    container.append_child(&liq_div).unwrap();

    // Row 2: Min Price, Current Price, Max Price
    let price_row = document.create_element("div").unwrap();
    price_row.set_attribute("class", "clmm-row-3").unwrap();
    let (min_div, min_input) = create_input("min", "Min Price (p_a)", "text", None);
    let (cur_div, cur_input) = create_input("cur", "Current Price (p)", "text", None);
    let (max_div, max_input) = create_input("max", "Max Price (p_b)", "text", None);
    price_row.append_child(&min_div).unwrap();
    price_row.append_child(&cur_div).unwrap();
    price_row.append_child(&max_div).unwrap();
    container.append_child(&price_row).unwrap();

    // Row 3: Position Slider
    let (slider_div, slider_input) =
        create_input("slider", "Position Slider", "range", Some("clmm-row-slider"));
    slider_input.set_min("0");
    slider_input.set_max("1");
    slider_input.set_step("0.0001");
    container.append_child(&slider_div).unwrap();

    // Row 4: Token X, Position, Token Y
    let inv_row = document.create_element("div").unwrap();
    inv_row.set_attribute("class", "clmm-row-3").unwrap();
    let (x_div, x_input) = create_input("x", "Token X Inventory", "text", None);
    let (pos_div, pos_input) = create_input("pos", "Position (0-1)", "text", None);
    let (y_div, y_input) = create_input("y", "Token Y Inventory", "text", None);
    inv_row.append_child(&x_div).unwrap();
    inv_row.append_child(&pos_div).unwrap();
    inv_row.append_child(&y_div).unwrap();
    container.append_child(&inv_row).unwrap();

    // Anchor Replacement
    anchor
        .parent_node()
        .unwrap()
        .replace_child(&container, &anchor)
        .unwrap();

    // Shared Input State
    let inputs = Rc::new(ClmmCalculatorInputs {
        liq: liq_input,
        min_price: min_input,
        cur_price: cur_input,
        max_price: max_input,
        slider: slider_input,
        pos_input: pos_input,
        x: x_input,
        y: y_input,
    });

    // Centralized Update Logic
    let update_widget = {
        let inputs = inputs.clone();
        move |mode: ClmmCalculatorUpdateMode| {
            let p_a = parse_f64(&inputs.min_price);
            let p_b = parse_f64(&inputs.max_price);

            match mode {
                ClmmCalculatorUpdateMode::FromPricesAndLiquidity => {
                    let p_c = parse_f64(&inputs.cur_price);
                    let l = parse_f64(&inputs.liq);
                    repopulate(&inputs, p_a, p_c, p_b, l);
                }
                ClmmCalculatorUpdateMode::FromPositionSlider => {
                    let pos = parse_f64(&inputs.slider);
                    let sqrt_a = p_a.sqrt();
                    let sqrt_b = p_b.sqrt();
                    let sqrt_c = sqrt_a + pos * (sqrt_b - sqrt_a);
                    let p_c = sqrt_c * sqrt_c;
                    let l = parse_f64(&inputs.liq);
                    repopulate(&inputs, p_a, p_c, p_b, l);
                }
                ClmmCalculatorUpdateMode::FromReserves => {
                    let p_c = parse_f64(&inputs.cur_price);
                    let x = parse_f64(&inputs.x);
                    let y = parse_f64(&inputs.y);
                    let sqrt_a = p_a.sqrt();
                    let sqrt_b = p_b.sqrt();
                    let sqrt_c = p_c.sqrt();

                    let l = if p_c <= p_a {
                        x * sqrt_a * sqrt_b / (sqrt_b - sqrt_a)
                    } else if p_c >= p_b {
                        y / (sqrt_b - sqrt_a)
                    } else {
                        let l_x = x * sqrt_c * sqrt_b / (sqrt_b - sqrt_c);
                        let l_y = y / (sqrt_c - sqrt_a);
                        l_x.min(l_y)
                    };
                    repopulate(&inputs, p_a, p_c, p_b, l);
                }
            }
        }
    };

    // Callback Setup
    let update_rc = Rc::new(update_widget);

    let on_price_liq_change = {
        let u = update_rc.clone();
        Closure::wrap(Box::new(move |_e: web_sys::Event| {
            u(ClmmCalculatorUpdateMode::FromPricesAndLiquidity);
        }) as Box<dyn FnMut(_)>)
    };
    inputs
        .liq
        .add_event_listener_with_callback("input", on_price_liq_change.as_ref().unchecked_ref())
        .unwrap();
    inputs
        .min_price
        .add_event_listener_with_callback("input", on_price_liq_change.as_ref().unchecked_ref())
        .unwrap();
    inputs
        .cur_price
        .add_event_listener_with_callback("input", on_price_liq_change.as_ref().unchecked_ref())
        .unwrap();
    inputs
        .max_price
        .add_event_listener_with_callback("input", on_price_liq_change.as_ref().unchecked_ref())
        .unwrap();
    on_price_liq_change.forget();

    let on_slider_change = {
        let u = update_rc.clone();
        let ins = inputs.clone();
        Closure::wrap(Box::new(move |_e: web_sys::Event| {
            let pos = parse_f64(&ins.slider);
            ins.pos_input.set_value(&format!("{:.4}", pos));
            u(ClmmCalculatorUpdateMode::FromPositionSlider);
        }) as Box<dyn FnMut(_)>)
    };
    inputs
        .slider
        .add_event_listener_with_callback("input", on_slider_change.as_ref().unchecked_ref())
        .unwrap();
    on_slider_change.forget();

    let on_pos_input_change = {
        let u = update_rc.clone();
        let ins = inputs.clone();
        Closure::wrap(Box::new(move |_e: web_sys::Event| {
            let pos = parse_f64(&ins.pos_input).clamp(0.0, 1.0);
            ins.slider.set_value(&format!("{:.4}", pos));
            u(ClmmCalculatorUpdateMode::FromPositionSlider);
        }) as Box<dyn FnMut(_)>)
    };
    inputs
        .pos_input
        .add_event_listener_with_callback("input", on_pos_input_change.as_ref().unchecked_ref())
        .unwrap();
    on_pos_input_change.forget();

    let on_reserve_change = {
        let u = update_rc.clone();
        Closure::wrap(Box::new(move |_e: web_sys::Event| {
            u(ClmmCalculatorUpdateMode::FromReserves);
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

    // Default Values: stablecoin pair range 0.015 to 0.025, position at midpoint
    let p_a = 0.015_f64;
    let p_b = 0.025_f64;
    let initial_stable = 1000.0_f64;
    let initial_pos = 0.5_f64;

    let initial_l = initial_stable / (p_b.sqrt() - p_a.sqrt());
    let sqrt_c = p_a.sqrt() + initial_pos * (p_b.sqrt() - p_a.sqrt());
    let p_c = sqrt_c * sqrt_c;

    repopulate(&inputs, p_a, p_c, p_b, initial_l);
}
```

**Widget JS Injection Anchor Example**
```html
<script type="module" id="clmm_calculator_ui">
  import init, { inject_ui } from "/assets/wasm/post_clmm_mathematics/post_clmm_mathematics.js";
  async function run() {
    await init();
    inject_ui("clmm_calculator_ui");
  }
  run();
</script>
```

**Widget Inline CSS Styling Example**
```html
<style>
  .clmm-widget {
    display: grid;
    grid-template-columns: 1fr;
    gap: 12px;
    padding: 20px;
    border: 2px solid #007bff;
    border-radius: 8px;
    max-width: 750px;
    background-color: #ffffff;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }

  .clmm-widget .clmm-row-1 {
    display: flex;
    flex-direction: column;
    gap: 5px;
  }

  .clmm-widget .clmm-row-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
  }

  .clmm-widget .clmm-row-slider {
    display: flex;
    flex-direction: column;
    gap: 5px;
    padding: 10px;
    background: #f6f8fa;
    border-radius: 6px;
  }

  .clmm-widget .clmm-field {
    display: flex;
    flex-direction: column;
    gap: 5px;
  }

  .clmm-widget label {
    font-size: 0.85rem;
    font-weight: 600;
    color: #333;
  }

  .clmm-widget input[type="text"] {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 1rem;
    width: 100%;
    box-sizing: border-box;
  }

  .clmm-widget input[type="range"] {
    width: 100%;
    margin: 5px 0;
  }

  @media (max-width: 500px) {
    .clmm-widget .clmm-row-3 {
      grid-template-columns: 1fr;
    }
  }
</style>
```

**Example index.html for Local Testing**
Add above CSS styling to commented location.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CLMM Calculator</title>

    <!-- Inline CSS Here -->
    <style></style>
</head>
<body>
    <h1>CLMM Calculator</h1>

    <script type="module" id="clmm_calculator_ui">
        import init, { inject_ui } from "./pkg/post_clmm_mathematics.js";
        async function run() {
            await init();
            inject_ui("clmm_calculator_ui");
        }
        run();
    </script>
</body>
</html>
```

**Sample Command to Served Example index.html for Local Testing**
```sh
# Terminal A
PORT="8000"
python -m http.server "${PORT}"

PORT="8000"
# Terminal B
open "http://localhost:${PORT}"
```

## Future Reading

The mathematics presented in this article cover the core model.
Several directions extend this foundation.

**Multi-range strategies.**
Active liquidity management strategies deploy capital across multiple overlapping ranges,
rebalancing as the price moves.
Academic research on optimal range selection remains an active area.

**Just-In-Time liquidity.**
Sophisticated participants add concentrated liquidity immediately before a large swap
and remove it immediately after, capturing fees with minimal impermanent loss exposure.
This technique has implications for MEV and fairness.

**Options-like payoff analysis.**
The payoff profile of a concentrated liquidity position
resembles a short straddle in options markets.
Research by Loesch et al. formalizes this connection,
and static replication using European options
has been demonstrated for concentrated liquidity positions.

**Uniswap v4 hooks.**
The successor protocol introduces a hook system
that allows pool deployers to customize swap logic,
fee structures, and oracle behavior.
This extensibility changes the design space for concentrated liquidity strategies.

---

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 20 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 20, 20 are established and 0 are bespoke.
Reserves are counted in tokens of their own kind and every price, including the range boundaries, is quoted as Token Y per Token X, so the liquidity carries the square root of the product of the two token units and a tick index is a pure number.

**Equation 1, Constant Product Invariant in Terms of Liquidity.**
The product of the two reserves equals the square of the liquidity, the invariant of a full-range constant product automated market maker.
[Constant Product AMM Mathematics][related_post_cpamm]

$$
x \cdot y = L^2
\tag{1}
$$

**Equation 2, Virtual Reserves in Terms of Liquidity and Price.**
Each reserve on the full unbounded curve follows from the liquidity and the square root of the price, so that their product is the squared liquidity and their ratio is the price.
[Constant Product AMM Mathematics][related_post_cpamm]

$$
x = \frac{L}{\sqrt{p}} \qquad y = L \cdot \sqrt{p}
\tag{2}
$$

**Equation 3, Virtual Reserves of a Concentrated Position.**
Within its range a concentrated position behaves as though the full constant product curve existed, with virtual reserves given by the same expressions in liquidity and price.

$$
x_v(p) = \frac{L}{\sqrt{p}} \qquad y_v(p) = L \cdot \sqrt{p}
\tag{3}
$$

**Equation 4, Translated Invariant of a Concentrated Position.**
The constant product curve is shifted so that the real reserves reach zero at the range boundaries, which is the invariant of a concentrated liquidity position in the Uniswap v3 design.

$$
\left(x_r + \frac{L}{\sqrt{p_b}}\right) \cdot \left(y_r + L \cdot \sqrt{p_a}\right) = L^2
\tag{4}
$$

**Equation 5, Real Token X Reserve Within the Range.**
The Token X a position holds is the liquidity times the difference of the reciprocal square roots of the current price and the upper boundary, reaching zero at the upper boundary.

$$
x_r = L \cdot \left(\frac{1}{\sqrt{p}} - \frac{1}{\sqrt{p_b}}\right) = \frac{L \cdot \left(\sqrt{p_b} - \sqrt{p}\right)}{\sqrt{p} \cdot \sqrt{p_b}}
\tag{5}
$$

**Equation 6, Real Token Y Reserve Within the Range.**
The Token Y a position holds is the liquidity times the difference of the square roots of the current price and the lower boundary, reaching zero at the lower boundary.

$$
y_r = L \cdot \left(\sqrt{p} - \sqrt{p_a}\right)
\tag{6}
$$

**Equation 7, Real Reserves With the Price Below the Range.**
When the price lies at or below the lower boundary the position holds only Token X, in the amount the in-range formula gives at the lower boundary.

$$
x_r = \frac{L \cdot \left(\sqrt{p_b} - \sqrt{p_a}\right)}{\sqrt{p_a} \cdot \sqrt{p_b}} \qquad y_r = 0
\tag{7}
$$

**Equation 8, Real Reserves With the Price Within the Range.**
When the price lies between the boundaries the position holds both tokens in the amounts the in-range formulas give.

$$
x_r = \frac{L \cdot \left(\sqrt{p_b} - \sqrt{p}\right)}{\sqrt{p} \cdot \sqrt{p_b}} \qquad y_r = L \cdot \left(\sqrt{p} - \sqrt{p_a}\right)
\tag{8}
$$

**Equation 9, Real Reserves With the Price Above the Range.**
When the price lies at or above the upper boundary the position holds only Token Y, in the amount the in-range formula gives at the upper boundary.

$$
x_r = 0 \qquad y_r = L \cdot \left(\sqrt{p_b} - \sqrt{p_a}\right)
\tag{9}
$$

**Equation 10, Liquidity Implied by a Token X Deposit.**
Inverting the real Token X reserve formula gives the liquidity that a deposit of Token X supports at the current price.

$$
L_x = \frac{\Delta x \cdot \sqrt{p} \cdot \sqrt{p_b}}{\sqrt{p_b} - \sqrt{p}}
\tag{10}
$$

**Equation 11, Liquidity Implied by a Token Y Deposit.**
Inverting the real Token Y reserve formula gives the liquidity that a deposit of Token Y supports at the current price.

$$
L_y = \frac{\Delta y}{\sqrt{p} - \sqrt{p_a}}
\tag{11}
$$

**Equation 12, Effective Liquidity of a Deposit.**
The liquidity of the position is the smaller of the two implied values, because the limiting token constrains the position and any excess of the other token is returned.

$$
L = \min(L_x,\ L_y)
\tag{12}
$$

**Equation 13, Price at a Tick.**
Each tick index corresponds to a price that is a power of 1.0001, so adjacent ticks differ by one basis point.

$$
p(i) = 1.0001^i
\tag{13}
$$

**Equation 14, Tick Index of a Price.**
The tick index of a price is the floor of the logarithm of the price to the base 1.0001.

$$
i = \left\lfloor \frac{\ln(p)}{\ln(1.0001)} \right\rfloor
\tag{14}
$$

**Equation 15, Square Root Price at a Tick.**
The square root of the price at a tick is the base 1.0001 raised to half the tick index, the quantity the protocol stores.

$$
\sqrt{p(i)} = 1.0001^{i/2}
\tag{15}
$$

**Equation 16, Capital Efficiency of a Symmetric Range.**
A position whose range is centred geometrically on the current price supplies the same depth as a full-range position with a fraction of the capital, and the multiplier depends only on the ratio of the boundaries.

$$
\text{efficiency} \approx \frac{1}{1 - \left(\frac{p_a}{p_b}\right)^{1/4}}
\tag{16}
$$

**Equation 17, Fee Growth Inside a Range.**
The fees accumulated per unit of liquidity inside a range are the global fee growth less the growth recorded below the lower boundary and above the upper boundary.

$$
f_{\text{inside}} = f_g - f_{\text{below}}(p_a) - f_{\text{above}}(p_b)
\tag{17}
$$

**Equation 18, Fees Owed to a Position.**
The fees owed to a position are the growth of the inside fee accumulator since the position was last updated, multiplied by its liquidity.

$$
\text{fees} = \left(f_{\text{inside}} - f_{\text{inside,last}}\right) \cdot L
\tag{18}
$$

**Equation 19, Impermanent Loss of a Full-Range Position.**
The value of a full-range constant product position relative to holding the deposited tokens depends only on the ratio of the new price to the original price.
[Constant Product AMM Mathematics][related_post_cpamm]

$$
IL(r) = \frac{2\sqrt{r}}{1 + r} - 1
\tag{19}
$$

**Equation 20, Value of a Concentrated Position Within the Range.**
The value of the position in Token Y is the Token X reserve priced at the current price plus the Token Y reserve, written in terms of liquidity and the boundaries.

$$
V(p) = x_r \cdot p + y_r = L \cdot \left(2\sqrt{p} - \frac{p}{\sqrt{p_b}} - \sqrt{p_a}\right)
\tag{20}
$$

### Notation

- $x$, the reserve of Token X on the full constant product curve
- $y$, the reserve of Token Y on the full constant product curve
- $L$, the liquidity of the position, identical in definition to the full-range constant product model
- $p$, the current price in Token Y per Token X
- $p_a$, the lower boundary of the price range of the position
- $p_b$, the upper boundary of the price range of the position
- $x_v(p)$, the virtual reserve of Token X at price $p$
- $y_v(p)$, the virtual reserve of Token Y at price $p$
- $x_r$, the real reserve of Token X held by the position
- $y_r$, the real reserve of Token Y held by the position
- $\Delta x$, the amount of Token X deposited
- $\Delta y$, the amount of Token Y deposited
- $L_x$, the liquidity implied by the Token X deposit
- $L_y$, the liquidity implied by the Token Y deposit
- $i$, the tick index
- $f_g$, the global fee growth per unit of liquidity since the pool was created
- $f_{\text{below}}(p_a)$, the fee growth recorded below the lower boundary of the range
- $f_{\text{above}}(p_b)$, the fee growth recorded above the upper boundary of the range
- $f_{\text{inside}}$, the fee growth per unit of liquidity inside the range of the position
- $f_{\text{inside,last}}$, the inside fee growth when the position was last updated
- $IL(r)$, the impermanent loss of a full-range position, a fraction that is never positive
- $r$, the ratio of the new price to the original price
- $V(p)$, the value of the position at price $p$ in units of Token Y

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Non-Peer-Reviewed

- Liquidity Math in Uniswap v3. n.d. *Elsts*. [https://atiselsts.github.io/pdfs/uniswap-v3-liquidity-math.pdf][research_elsts_liquidity]
- Loesch, Stefan, Nate Hindman, Mark B. Richardson, and Nicholas Welch. 2021. "Impermanent Loss in Uniswap v3." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2111.09192][research_loesch_il]

### General Sources

- "Concentrated Liquidity." n.d. Accessed October 25, 2026. [https://docs.uniswap.org/concepts/protocol/concentrated-liquidity][ref_uniswap_cl]
- Uniswap v3 Core. n.d. "Adams, Zinsmeister, Salem, Keefer, and Robinson." Accessed October 25, 2026. [https://app.uniswap.org/whitepaper-v3.pdf][ref_uniswap_v3_whitepaper]

### Related Posts

- Sechter, Brendan. 2026. "WASM on a Jekyll Blog with Rust and wasm-bindgen." *Brendan A R Sechter's Development Blog*, January 26. [https://sgeos.github.io/rust/wasm/jekyll/2026/01/26/webasm\_on\_jekyll.html][related_post_wasm]
- Sechter, Brendan. 2026. "Constant Product AMM Mathematics." *Brendan A R Sechter's Development Blog*, January 29. [https://sgeos.github.io/crypto/defi/rust/2026/01/29/constant\_amm\_mathematics.html][related_post_cpamm]

[ref_uniswap_cl]: https://docs.uniswap.org/concepts/protocol/concentrated-liquidity
[ref_uniswap_v3_whitepaper]: https://app.uniswap.org/whitepaper-v3.pdf
[related_post_cpamm]: {% post_url 2026-01-29-constant_amm_mathematics %}
[related_post_wasm]: {% post_url 2026-01-26-webasm_on_jekyll %}
[research_elsts_liquidity]: https://atiselsts.github.io/pdfs/uniswap-v3-liquidity-math.pdf
[research_loesch_il]: https://doi.org/10.48550/arxiv.2111.09192
