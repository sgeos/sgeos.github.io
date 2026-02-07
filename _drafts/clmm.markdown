---
layout: post
mathjax: false
comments: true
title:  "CLMM Calculator"
date:   2026-01-24 05:59:15 +0000
categories: 
---
(Information about CLMM here.)

## Software Versions

```sh
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-01-24 05:59:15 +0000

$ uname -vm
Darwin Kernel Version 23.6.0: Mon Jul 29 21:14:30 PDT 2024; root:xnu-10063.141.2~1/RELEASE_ARM64_T6000 arm64
```

## Instructions

(More information about CLMM here.)

## ...

```sh
echo "Code here."
```

<div id="clmm-master" style="border: 1px solid #d1d5da; padding: 25px; border-radius: 12px; background: #fff; font-family: sans-serif; max-width: 750px; margin: 20px auto; color: #24292e; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
    
    <div style="margin-bottom: 20px;">
        <label style="display:block; font-size: 12px; font-weight: bold; margin-bottom: 5px;">Liquidity Depth (L)</label>
        <input type="number" id="liqField" value="0" step="any" style="width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; font-family: monospace; font-weight: bold; background: #fdfdfd;">
    </div>

    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin-bottom: 20px;">
        <div>
            <label style="display:block; font-size: 12px; font-weight: bold; margin-bottom: 5px;">Min Price</label>
            <input type="number" id="minPrice" value="0.15" step="any" style="width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px;">
        </div>
        <div>
            <label style="display:block; font-size: 12px; font-weight: bold; margin-bottom: 5px;">Current Price</label>
            <input type="number" id="curPrice" value="0" step="any" style="width: 100%; padding: 8px; border: 1px solid #007bff; border-radius: 4px;">
        </div>
        <div>
            <label style="display:block; font-size: 12px; font-weight: bold; margin-bottom: 5px;">Max Price</label>
            <input type="number" id="maxPrice" value="0.25" step="any" style="width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px;">
        </div>
    </div>

    <div style="margin-bottom: 25px; padding: 15px; background: #f6f8fa; border-radius: 6px;">
        <input type="range" id="posSlider" min="0" max="1" step="0.0001" value="0.5" style="width: 100%; cursor: pointer;">
    </div>

    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px;">
        <div>
            <label style="display:block; font-size: 12px; font-weight: bold; margin-bottom: 5px;">Meme Inventory</label>
            <input type="number" id="memeQty" value="0" step="any" style="width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px;">
        </div>
        <div>
            <label style="display:block; font-size: 12px; font-weight: bold; margin-bottom: 5px;">Price Position (0-1)</label>
            <input type="number" id="posInput" value="0.5" step="0.0001" style="width: 100%; padding: 8px; border: 1px solid #007bff; border-radius: 4px;">
        </div>
        <div>
            <label style="display:block; font-size: 12px; font-weight: bold; margin-bottom: 5px;">Stable Inventory</label>
            <input type="number" id="stableQty" value="1000" step="any" style="width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px;">
        </div>
    </div>
</div>

<script>
    const el = {
        liq: document.getElementById('liqField'),
        min: document.getElementById('minPrice'),
        cur: document.getElementById('curPrice'),
        max: document.getElementById('maxPrice'),
        slider: document.getElementById('posSlider'),
        posIn: document.getElementById('posInput'),
        meme: document.getElementById('memeQty'),
        stable: document.getElementById('stableQty')
    };

    function getVal(node) { return parseFloat(node.value) || 0; }

    /**
     * MASTER UPDATE FUNCTION
     * The single source of truth for the calculator state.
     */
    function repopulate(pA, pC, pB, L) {
        el.min.value = pA;
        el.max.value = pB;
        el.cur.value = pC.toFixed(6);
        el.liq.value = L.toFixed(6);

        // Calculate Position (0-1) based on sqrt price
        let pos = (Math.sqrt(pC) - Math.sqrt(pA)) / (Math.sqrt(pB) - Math.sqrt(pA));
        pos = Math.max(0, Math.min(1, pos));
        el.slider.value = pos;
        el.posIn.value = pos.toFixed(4);

        // Calculate Inventories using L and Sqrt Prices
        let x, y;
        if (pC <= pA) {
            x = L * (Math.sqrt(pB) - Math.sqrt(pA)) / (Math.sqrt(pA) * Math.sqrt(pB));
            y = 0;
        } else if (pC >= pB) {
            x = 0;
            y = L * (Math.sqrt(pB) - Math.sqrt(pA));
        } else {
            x = L * (Math.sqrt(pB) - Math.sqrt(pC)) / (Math.sqrt(pC) * Math.sqrt(pB));
            y = L * (Math.sqrt(pC) - Math.sqrt(pA));
        }
        el.meme.value = x.toFixed(2);
        el.stable.value = y.toFixed(2);
    }

    function handleInput(e) {
        const id = e.target.id;
        let pA = getVal(el.min), pB = getVal(el.max), pC = getVal(el.cur), L = getVal(el.liq);

        if (['minPrice', 'maxPrice', 'curPrice', 'liqField'].includes(id)) {
            repopulate(pA, pC, pB, L);
        } 
        else if (id === 'posSlider' || id === 'posInput') {
            const pos = getVal(e.target);
            const sqrtC = Math.sqrt(pA) + pos * (Math.sqrt(pB) - Math.sqrt(pA));
            pC = Math.pow(sqrtC, 2);
            repopulate(pA, pC, pB, L);
        }
        else if (id === 'memeQty' || id === 'stableQty') {
            const x = getVal(el.meme), y = getVal(el.stable);
            // Recalculate L based on standard UniV3 logic
            if (pC <= pA) L = x * (Math.sqrt(pA) * Math.sqrt(pB)) / (Math.sqrt(pB) - Math.sqrt(pA));
            else if (pC >= pB) L = y / (Math.sqrt(pB) - Math.sqrt(pA));
            else {
                const Lx = x * (Math.sqrt(pC) * Math.sqrt(pB)) / (Math.sqrt(pB) - Math.sqrt(pC));
                const Ly = y / (Math.sqrt(pC) - Math.sqrt(pA));
                L = Math.min(Lx, Ly);
            }
            repopulate(pA, pC, pB, L);
        }
    }

    Object.values(el).forEach(input => input.addEventListener('input', handleInput));

    // INITIALIZATION LOGIC
    (function init() {
        const pA = 0.015, pB = 0.025, initialStable = 1000, initialPos = 0.5;
        
        // 1. Calculate L from the "All Stable" condition at pB
        // L = y / (sqrt(pB) - sqrt(pA))
        const initialL = initialStable / (Math.sqrt(pB) - Math.sqrt(pA));
        
        // 2. Calculate pC from the target Price Position (0.5)
        const sqrtC = Math.sqrt(pA) + initialPos * (Math.sqrt(pB) - Math.sqrt(pA));
        const pC = Math.pow(sqrtC, 2);
        
        repopulate(pA, pC, pB, initialL);
    })();
</script>

## References:

- [ref][ref]

[ref]: https://sgeos.github.io

