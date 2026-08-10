# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A369 rendering defects repaired, the same defects fixed corpus-wide, and A369's inline
citation runs converted to lists. All pushed and live.

---

## What Was Broken on the Live Site

**Three defects, reported by the human pilot from the published page, and two of them were corpus-wide.**

**Invisible references.** A link definition renders as nothing, so A369's block of 1,765 `[anchor]: url`
lines produced four empty headings. The corpus convention is a visible `- [text][anchor]` list beside
the definitions. **The convention had broken partway through the X-Planes series**, with `bell_x1`
carrying 337 bullets for 337 definitions and `bensen_x25` carrying none for 3,990. Seventeen drafts were
affected and all are repaired, 20,777 entries in total, with display text recovered from how each body
already cites the anchor.

**Accidental tables.** kramdown reads a paragraph whose first line contains `|` as a table, so inline
math carrying a cardinality bar such as `$|S| = 39$` at a paragraph start turned prose into table cells
and shredded the math across them, leaving raw dollar signs on the page. **A369 had three.** Twenty-one
published posts carried the same hazard, including `spacex_history_governance`, which had one live.
Sixty-two delimiters rewritten to `\lvert` and `\rvert`. Zero remain site-wide.

**A table torn in half**, in `x_planes_ryan_x13`, its header and delimiter row separated from its three
data rows by two equations and a paragraph. Found only by building the whole repaired series, not by any
structural check.

---

## The Citation Runs Are Now Lists

Fourteen runs holding 1,650 links, the largest of them 202, were inline comma-separated text inside
paragraphs. **The longest paragraph on the page was about nineteen thousand characters and is now
1,439.** The links are unchanged and remain in chronological order within each cluster.

---

## Guards Added

`references-invisible` is an error in `_verify.py`, with zero false positives on posts. `math-pipe-table`
is a warning, because the pattern was already widespread. Both were measured across the corpus before
being added, and `emit_blocks` in `_lib/refs.py` now takes display text and emits the visible list.

**One of my own validations was circular and is worth recording.** `emit_blocks` had been proved
byte-identical against A369's own reference block, which was the broken artefact it had produced.
Validating a generator against its own output demonstrates self-consistency and nothing else. The
published A216 was the correct reference and would have exposed the defect immediately.

---

## State

Working tree clean, local matches remote, `_verify.py` at zero errors and the 21-warning baseline, 44
of 44 library tests passing. All 27 X-Planes drafts build together with zero accidental tables and
rendering reference lists.

---

## Awaiting Instruction

**The X-Planes series is ready to resume.** Twenty-seven of seventy-two drafted, A297 through A323, all
four passes complete, none published. The next to draft is **A324, the Lockheed X-27**, editorial date
2025-11-02. The CL-1200 Lancer was never built and never flew, so on the genre document's test, whether
a vehicle existed and produced data, it takes the reduced designation-anomaly order rather than the full
twelve sections. That reading should be confirmed against the record during the draft pass.

**Six published posts carry headerless tables**, `claude_code_getting_started` having twelve. Those
render as valid tables and look deliberate, so they were left alone.
