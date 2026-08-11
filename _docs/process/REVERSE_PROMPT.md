# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-11
**Task**: Close the follow-up concerns from the word-usage and housekeeping work. **Committed and
pushed.** Two of the five were defects I had introduced hours earlier.

---

## The Two I Broke

**The collocation annotation contradicted its own arithmetic.** The warning read `` `specific` 59x ...
top collocate `specific impulse` 57x = 86% ``, and 57 of 59 is 97 percent, not 86. The count came from
`_verify.py`'s prose extraction and the share from `_lib/diction.py`'s, which disagree by 59 against 66
on that file. `collocations` and `top_collocate` now take `already_prose`, and the verifier passes its
own extracted body, so **one body of text produces both numbers**. Verified consistent across all five
propellant articles by lifting the exemption and reading the output.

**The `redirects/` mechanism lived only in files that get overwritten.** It is now in `CLAUDE.md` under
Architecture, with the rule that an entry is needed whenever a published post's URL changes.

---

## Two Checks Now Exist Because The Defect Shipped

**`category-slug-collision` is a new `_verify.py` error.** Two categories that slugify to one path
destroy an archive page, which is what `c` and `c++` did while `/categories/cpp/` returned 404 live.
**It is an error rather than a warning because the remedy is not free.** The default permalink joins
every category, so fixing a collision after the category ships moves the post URL and needs a redirect.
Catching it beforehand avoids that entirely. Proven to fire by reintroducing `c++` and reading the
output, then restored.

**The permalink rule is in `CLAUDE.md`.** It previously documented only that the FIRST category shadows
a URL path, which is the note that made me confident the rename was safe. It now states that every
category appears in the URL, with the 2026-08-11 breakage as the reason.

---

## The Harvest Gate Is Shared And The Sampling Is Now The Return Protocol

`_lib/gate.py` carries `Gate`, `select` and `audit`, with the two failures written into the module
docstring.

**The point of the module is `audit`, which samples BOTH sides.** Reading kept records catches a
permissive gate. Reading dropped records catches a narrow one. One side cannot catch both, and no
summary statistic catches either, since a narrow gate reports a small corpus that reads as a thin
literature and a permissive gate reports a large corpus that reads as thoroughness.

**`audit` requires a `seed` and has no default**, so a reviewer can reproduce exactly what was read.
**It always prints**, and the test suite captures stdout rather than being given a quiet flag, because
a quiet flag is precisely what a future caller would reach for to skip the reading the function exists
to force.

`explain` also names the ambiguous terms in a dropped title, which is the signature of a gate written
for the wrong subject and is what would have made the A333 failure visible at drop time.

---

## The Instruments Are Runnable And The Method Is Documented

```sh
python3 _lib/diction.py collocate <word> <path>     evidence for one word, both directions
python3 _lib/diction.py outliers  <path> [glob]     words above the peer maximum
python3 _lib/diction.py tics      <path> [glob]     the enumerated tic class
python3 _lib/diction.py report    <path> [glob]     multi-word constructions
```

`outliers` and `tics` were library functions nothing called. **Both print the caveat that a word above
the peer maximum is usually the subject rather than a tic**, and point at `collocate`.

**`_docs/writing/STYLE_GUIDE.md` gains a How to measure it section**, carrying the commands, the
direction rule, a signature table, and the reason a warning must be resolved either way. The method
previously existed only as a pointer to a log entry.

---

## Verification

- `python3 _verify.py` **0 errors, 0 warnings**.
- `python3 _lib/test_lib.py` **63 of 63**, up from 58. The six new tests cover the slug collision, the
  two front-matter category forms, the strong-versus-ambiguous gate rule, the drop explanation, and
  the reproducible two-sided sample.
- **Isolated production build exit 0 with no conflict, isolated drafts build exit 0**, and both
  redirect pages still generate.

---

## Not Acted On, Deliberately

**`no_std` slugifies to `no-std`**, so `/categories/no-std/` returns 200 while `/categories/no_std/`
returns 404. Post URLs keep the literal underscore. **Nothing is broken and nothing links to the
missing path**, so this is recorded rather than changed. Renaming the category would move two post
URLs and buy nothing.

---

## Standing Work, Unchanged And Needing Your Instruction

**A334, the Boeing X-37**, editorial date 2025-11-12, Part 38 of 72. A four-pass job that starts on
your prompt.

**The thirty-seven X-Planes drafts remain unpublished**, and publication has never been authorised for
them. The eight redated drafts now sit at 2026-08-12 through 2026-08-19 and those dates are arbitrary.
