# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-15
**Task**: A91-P1 Draft CLMM Post and Combine Android Drafts

---

## Verification

### A91 "Concentrated Liquidity Market Maker Mathematics"

- Renamed from `clmm.markdown` to `clmm_mathematics.markdown`.
- Categories: `crypto defi rust`.
- Date: 2026-02-22.
- Six references across three categories (Reference, Related Post, Research).
- References A73 "Constant Product AMM Mathematics" and A72 "WASM on a Jekyll Blog" via post_url.

#### Mathematical Sections

1. **Concentrated Liquidity Architecture**: Introduces CLMM as extension of CPAMM, connects to A73.
2. **From Constant Product to Concentrated Liquidity**: Virtual reserves, translated curve invariant, geometric interpretation.
3. **Real Reserves Formulas**: Core equations for $x_r$ and $y_r$ with variable definitions. Corresponds to whitepaper Equations 6.29 and 6.30.
4. **Three Price Regimes**: Below range (all Token X), in range (both), above range (all Token Y). Includes regime transition note.
5. **Computing Liquidity from a Deposit**: $L_x$, $L_y$, and $L = \min(L_x, L_y)$ formulas. Contrast with full-range CPAMM.
6. **Tick Mathematics**: Price discretization, tick-to-price formula, tick spacing, fee tier table (1/5/30/100 bp). Governance note on 1 bp tier.
7. **Capital Efficiency**: Concentration factor formula, 4000x stablecoin example, tradeoff note.
8. **Fee Accrual**: feeGrowthGlobal, feeGrowthOutside, feeGrowthInside, position fee computation.
9. **Impermanent Loss in Concentrated Positions**: CPAMM IL formula, amplification in concentrated positions, position value formula, Loesch et al. citation.

#### Rust WASM Calculator

- Calculator rewritten from JavaScript to Rust using `wasm-bindgen` and `web-sys`.
- Three update modes: FromPricesAndLiquidity, FromPositionSlider, FromReserves.
- `Cargo.toml` and `src/lib.rs` full listings provided.
- Widget JS injection anchor and CSS styling examples included.
- WASM project name: `post_clmm_mathematics`.
- No external math library dependency. Uses f64 arithmetic for educational purposes.

#### Future Reading Section

Covers multi-range strategies, just-in-time liquidity, options-like payoff analysis, and Uniswap v4 hooks.

#### References (4 external, 2 internal)

- Reference, Concentrated Liquidity (Uniswap Documentation) - HTTP 200
- Reference, Uniswap v3 Core (whitepaper PDF) - HTTP 200
- Related Post, Constant Product AMM Mathematics (A73) - post_url
- Related Post, WASM on a Jekyll Blog (A72) - post_url
- Research, Liquidity Math in Uniswap v3 (Elsts) - HTTP 200
- Research, Impermanent Loss in Uniswap v3 (Loesch et al.) - HTTP 200

### Android Development on FreeBSD (Combined Draft)

- Two files merged: `building_android_apks_on_freebsd.markdown` and `android_ndk_builds_on_freebsd.markdown`.
- Combined into `android_development_on_freebsd.markdown`.
- Title: "Android Development on FreeBSD".
- No article number assigned. Not slotted for publication.
- TODO header added listing modernization tasks for future work.
- Structured into five subsections: Linux Emulation Layer, Android SDK and NDK Installation, ADB Setup, Environment Configuration, Build Verification.
- 15 references (union of both original reference lists).
- Original content preserved without modernization per PROMPT.md constraints.

### Draft Summary Sync

- CLMM entry updated from stub (~35%) to RC (A91, ~95%).
- Two Android entries replaced by one combined entry.
- CLMM struck through in candidate future topics table.
- Summary counts updated: 12 files, 6 RCs, 0 stubs.
- Tier structure revised: Tier 2 (CLMM) removed, Android moved to Tier 2, old Tier 4 becomes Tier 3.

---

## Questions for Human Review

- The PROMPT.md references A74 as "another DeFi Rust-based WASM widget example," but A74 is "Claude Code Getting Started." The relevant DeFi WASM widget example is A73 (Constant Product AMM Mathematics). The CLMM article references A73 accordingly. Please confirm this interpretation is correct.
- The CLMM calculator widget requires WASM compilation and deployment to `assets/wasm/post_clmm_mathematics/` before it will function in the Jekyll preview. The code listings in the article are complete and buildable.

---

## Notes

- Next available article number: A92.
- 6 release candidates: A86 "Mission Command Management Style," A87 "Telemeritocracy," A88 "Radioactive Half-Life Demurrage Cryptocurrency Coin," A89 "Cryptotelemeritocracy," A90 "Introduction to Space Studies," A91 "Concentrated Liquidity Market Maker Mathematics."
- 0 stubs.
- Publication order dependency: A86 before A87 before A89. A88, A90, and A91 have no dependencies.
- A86 publication date: 2026-02-18.
- A88 publication date: 2026-02-17.
- A87 publication date: 2026-02-19.
- A89 publication date: 2026-02-20.
- A90 publication date: 2026-02-21.
- A91 publication date: 2026-02-22.
