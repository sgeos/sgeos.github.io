#!/usr/bin/env python3
"""Assertion-guarded editing, replacing one hundred and forty-four copies.

WHY. 144 scratch files re-implement this loop and 34 re-implement the equation
guard. Only one, written the day the bug was found, matches across line breaks.
Reflowed files broke every naive copy silently, because a match string carrying
the old line breaks simply fails and, in the copies that bail on first failure,
takes the rest of the batch with it.

THE CONTRACT, which the copies mostly got right and is worth stating once.

  EVERY EDIT MUST MATCH EXACTLY ONCE. Zero matches means the text moved. Two
  matches means the anchor is ambiguous and the edit would land in an arbitrary
  place. Both are errors.

  THE BATCH IS ALL OR NOTHING. A partially applied batch leaves the file in a
  state no one designed, and the natural repair is to re-run it, which then
  fails differently. Nothing is written unless every edit matched.

  EVERY FAILURE IS REPORTED, not just the first, so one run fixes the batch.

  GUARDS RUN BEFORE THE WRITE. Equation count must not fall, and invariant
  defects must not be introduced. An edit that silently drops a display
  equation is the failure mode the count guard exists for.

WHITESPACE TOLERANCE IS THE POINT. `match_ws` turns runs of whitespace in the
search string into `\\s+`, so an edit authored against unwrapped prose still
applies after reflow. This is why the search text may be written naturally.
"""

import re


class EditError(RuntimeError):
    pass


def match_ws(needle):
    """Compile a literal string into a whitespace-tolerant pattern."""
    return re.compile(r"\s+".join(re.escape(tok) for tok in needle.split()))


def count_equations(text):
    return len(re.findall(r"(?m)^\$\$.*\$\$$", text)) + len(re.findall(r"(?m)^\$\$$", text))


def apply_to_text(text, edits, guard_equations=True, guard_invariants=True):
    """Apply (old, new) pairs to text. Returns the new text or raises.

    Edits are applied in order. Each must match exactly once at the moment it
    is applied, so an earlier edit may legitimately create the anchor a later
    one needs.
    """
    eq_before = count_equations(text)
    failures = []
    out = text
    for i, pair in enumerate(edits):
        old, new = pair[0], pair[1]
        if old == new:
            continue
        rx = match_ws(old)
        n = len(rx.findall(out))
        if n != 1:
            failures.append(f"edit {i}: matched {n} times: {old[:72]!r}")
            continue
        out = rx.sub(lambda _m, _n=new: _n, out, count=1)
    if failures:
        raise EditError(f"{len(failures)} of {len(edits)} edits failed; nothing written\n  "
                        + "\n  ".join(failures))
    if guard_equations:
        eq_after = count_equations(out)
        if eq_after < eq_before:
            raise EditError(f"equation count dropped {eq_before} -> {eq_after}; nothing written")
    if guard_invariants:
        import lint
        lint.assert_clean(out)
    return out


def apply(path, edits, reflow_after=False, **kw):
    """Apply a batch to a file on disk. Nothing is written unless all succeed."""
    text = open(path, encoding="utf-8").read()
    out = apply_to_text(text, edits, **kw)
    if reflow_after:
        import reflow as _reflow
        out = _reflow.reflow_post(out)
        if kw.get("guard_invariants", True):
            import lint
            lint.assert_clean(out)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(out)
    return len(edits)


def substitute(path, mapping, reflow_after=False):
    """Fill `{c('key')}` templates from a mapping, tolerating reflowed keys.

    Reflow may wrap a long key across a line, so the key is matched with
    whitespace collapsed. An unknown or empty key raises rather than emitting
    an empty citation cluster, which is how A320 caught a frozen generator.
    """
    text = open(path, encoding="utf-8").read()
    missing = []

    def _sub(m):
        key = re.sub(r"\s+", " ", m.group(1)).strip()
        val = mapping.get(key)
        if not val:
            missing.append(key)
            return m.group(0)
        return val

    out = re.sub(r"\{c\('([^']+)'\)\}", _sub, text, flags=re.S)
    if missing:
        raise EditError(f"{len(missing)} unknown or empty template keys: {missing[:5]}")
    if reflow_after:
        import reflow as _reflow
        out = _reflow.reflow_post(out)
    import lint
    lint.assert_clean(out)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(out)
    return text.count("{c('")
